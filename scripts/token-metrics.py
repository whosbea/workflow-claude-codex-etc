#!/usr/bin/env python3
"""Mede o gasto de tokens do Claude Code (contexto fixo + uso real dos transcripts).

Uso:
    python3 -I scripts/token-metrics.py --label baseline [--since YYYY-MM-DD] [--until YYYY-MM-DD]

Gera metrics/<hoje>-<label>.json e metrics/<hoje>-<label>.md na raiz do repo.
Tokens do contexto fixo são ESTIMATIVA (caracteres / 4). O que importa é usar
o mesmo método nas duas medições (antes e depois da faxina).
"""

import argparse
import datetime as dt
import json
import re
import statistics
import sys
from pathlib import Path

HOME = Path.home() / ".claude"
REPO = Path(__file__).resolve().parent.parent
USAGE_FIELDS = (
    "input_tokens",
    "cache_creation_input_tokens",
    "cache_read_input_tokens",
    "output_tokens",
)
TOP_N = 15


# ---------- Parte A: contexto fixo ----------

def text_stats(text):
    return {
        "words": len(text.split()),
        "chars": len(text),
        "tokens_est": round(len(text) / 4),
    }


def split_frontmatter(text):
    """Retorna (frontmatter, corpo). Sem frontmatter -> ("", texto)."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def context_frontmatter(fm):
    """Texto bruto das chaves name e description (incluindo linhas de continuação
    indentadas, como em blocos `|` ou `>`). É o que entra no contexto sempre."""
    out, keep = [], False
    for line in fm.splitlines():
        key = re.match(r"^([A-Za-z_][\w-]*)\s*:", line)
        if key:
            keep = key.group(1) in ("name", "description")
        elif line.strip() and not line[:1].isspace():
            keep = False
        if keep:
            out.append(line)
    return "\n".join(out)


def measure_md(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, _ = split_frontmatter(text)
    return {
        "name": path.parent.name if path.name == "SKILL.md" else path.stem,
        "frontmatter": text_stats(context_frontmatter(fm)),
        "body": text_stats(text),  # arquivo inteiro, carregado quando invocado
    }


def summarize(items, key):
    tot = {"files": len(items), "words": 0, "chars": 0, "tokens_est": 0}
    for it in items:
        for k in ("words", "chars", "tokens_est"):
            tot[k] += it[key][k]
    return tot


def top(items, key, n=TOP_N):
    ranked = sorted(items, key=lambda it: it[key]["chars"], reverse=True)[:n]
    return [{"name": it["name"], **it[key]} for it in ranked]


def part_a():
    claude_md = HOME / "CLAUDE.md"
    claude_text = claude_md.resolve().read_text(encoding="utf-8", errors="replace")

    skills, no_skill_md = [], []
    for d in sorted((HOME / "skills").iterdir()):
        if d.name.startswith(".") or not d.is_dir():
            continue
        sk = d / "SKILL.md"
        if sk.is_file():
            skills.append(measure_md(sk))
        else:
            no_skill_md.append(d.name)

    def md_dir(name):
        p = HOME / name
        return [measure_md(f) for f in sorted(p.glob("*.md"))] if p.is_dir() else []

    agents, commands = md_dir("agents"), md_dir("commands")

    always = {
        "claude_md": text_stats(claude_text),
        "skills_frontmatter": summarize(skills, "frontmatter"),
        "agents_frontmatter": summarize(agents, "frontmatter"),
        "commands_frontmatter": summarize(commands, "frontmatter"),
    }
    always_total = {
        k: sum(v[k] for v in always.values()) for k in ("words", "chars", "tokens_est")
    }
    return {
        "claude_md": {"path": str(claude_md), "resolved": str(claude_md.resolve()),
                      "files": 1, **text_stats(claude_text)},
        "counts": {"skills": len(skills), "agents": len(agents), "commands": len(commands)},
        "skills_without_skill_md": no_skill_md,
        "skills": {
            "frontmatter_total": summarize(skills, "frontmatter"),
            "frontmatter_top": top(skills, "frontmatter"),
            "body_total": summarize(skills, "body"),
            "body_top": top(skills, "body"),
        },
        "agents": {
            "frontmatter_total": summarize(agents, "frontmatter"),
            "body_total": summarize(agents, "body"),
            "items": [{"name": a["name"], "frontmatter": a["frontmatter"], "body": a["body"]} for a in agents],
        },
        "commands": {
            "frontmatter_total": summarize(commands, "frontmatter"),
            "body_total": summarize(commands, "body"),
            "items": [{"name": c["name"], "frontmatter": c["frontmatter"], "body": c["body"]} for c in commands],
        },
        "always_loaded_total": always_total,
    }


# ---------- Parte B: uso real ----------

def stats(values):
    if not values:
        return {"n": 0}
    s = sorted(values)
    # p90 por nearest-rank
    p90 = s[max(0, -(-len(s) * 90 // 100) - 1)]
    return {
        "n": len(s),
        "median": statistics.median(s),
        "mean": round(statistics.fmean(s), 1),
        "p90": p90,
        "min": s[0],
        "max": s[-1],
    }


def total_in(u):
    return u["input_tokens"] + u["cache_creation_input_tokens"] + u["cache_read_input_tokens"]


def part_b(since, until):
    root = HOME / "projects"
    files = sorted(root.glob("**/*.jsonl"))
    malformed = 0
    lines_assistant = 0
    msgs = {}  # message.id -> registro (última ocorrência vence)

    for f in files:
        rel = f.relative_to(root).parts
        project = rel[0]
        is_sub = "subagents" in rel
        with f.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    malformed += 1
                    continue
                if not isinstance(obj, dict) or obj.get("type") != "assistant":
                    continue
                msg = obj.get("message")
                ts = obj.get("timestamp")
                if not isinstance(msg, dict) or not msg.get("id") or not isinstance(ts, str):
                    malformed += 1
                    continue
                day = ts[:10]  # data UTC do timestamp ISO
                if not (since <= day <= until):
                    continue
                lines_assistant += 1
                usage = msg.get("usage") or {}
                u = {k: int(usage.get(k) or 0) for k in USAGE_FIELDS}
                # sessão principal = sessionId; subagente = arquivo (cada arquivo é uma execução)
                key = str(f.relative_to(root)) if is_sub else obj.get("sessionId") or f.stem
                msgs[msg["id"]] = {
                    "kind": "sub" if is_sub else "main",
                    "session": key,
                    "project": project,
                    "model": msg.get("model") or "?",
                    "ts": ts,
                    "usage": u,
                }

    totals = {k: 0 for k in USAGE_FIELDS}
    by_model = {}
    sessions = {"main": {}, "sub": {}}
    for m in msgs.values():
        for k in USAGE_FIELDS:
            totals[k] += m["usage"][k]
        bm = by_model.setdefault(m["model"], {"messages": 0, **{k: 0 for k in USAGE_FIELDS}})
        bm["messages"] += 1
        for k in USAGE_FIELDS:
            bm[k] += m["usage"][k]
        sessions[m["kind"]].setdefault(m["session"], []).append(m)

    def per_session(group):
        rows = []
        for sid, ms in group.items():
            ms.sort(key=lambda x: x["ts"])
            # primeira chamada real (ignora mensagens sintéticas com usage zerado)
            real = [x for x in ms if total_in(x["usage"]) > 0]
            rows.append({
                "session": sid,
                "project": ms[0]["project"],
                "calls": len(ms),
                "input_total": sum(total_in(x["usage"]) for x in ms),
                "output": sum(x["usage"]["output_tokens"] for x in ms),
                "initial_context": total_in(real[0]["usage"]) if real else None,
            })
        return rows

    main_rows = per_session(sessions["main"])
    sub_rows = per_session(sessions["sub"])

    def init_ctx(rows):
        s = stats([r["initial_context"] for r in rows if r["initial_context"] is not None])
        return {k: s[k] for k in ("n", "median", "min", "max") if k in s}

    return {
        "files_scanned": len(files),
        "malformed_lines": malformed,
        "assistant_lines_in_window": lines_assistant,
        "assistant_messages_dedup": len(msgs),
        "sessions": {"main": len(main_rows), "subagents": len(sub_rows)},
        "messages_by_kind": {
            "main": sum(r["calls"] for r in main_rows),
            "subagents": sum(r["calls"] for r in sub_rows),
        },
        "usage_totals": totals,
        "by_model": dict(sorted(by_model.items(), key=lambda kv: -kv[1]["messages"])),
        "main_per_session": {
            "input_total": stats([r["input_total"] for r in main_rows]),
            "output": stats([r["output"] for r in main_rows]),
            "calls": stats([r["calls"] for r in main_rows]),
        },
        "initial_context_main": init_ctx(main_rows),
        "initial_context_subagents": init_ctx(sub_rows),
        "top10_main_by_input": [
            {k: r[k] for k in ("project", "session", "input_total", "calls")}
            for r in sorted(main_rows, key=lambda r: -r["input_total"])[:10]
        ],
    }


# ---------- Saída ----------

def fmt(n):
    if n is None:
        return "-"
    if isinstance(n, float) and not n.is_integer():
        return f"{n:,.1f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"{int(n):,}".replace(",", ".")


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def render_md(data):
    a, b, meta = data["part_a"], data["part_b"], data["meta"]
    L = [f"# Métricas de tokens: {meta['label']} ({meta['date']})", "",
         f"Janela: {meta['since']} a {meta['until']} (UTC). "
         "Tokens da Parte A = ESTIMATIVA (caracteres/4).", "",
         "## A. Contexto fixo", "",
         f"Skills: {a['counts']['skills']} | Agentes: {a['counts']['agents']} | "
         f"Commands: {a['counts']['commands']}", ""]
    if a["skills_without_skill_md"]:
        L += ["Ignorados (sem SKILL.md): " + ", ".join(a["skills_without_skill_md"]), ""]

    def row(label, s):
        return [label, s.get("files", 1), fmt(s["words"]), fmt(s["chars"]), fmt(s["tokens_est"])]

    L += ["### Sempre carregado", "",
          table(["Item", "Arquivos", "Palavras", "Caracteres", "Tokens (est.)"], [
              row("CLAUDE.md", a["claude_md"]),
              row("Skills (name+description)", a["skills"]["frontmatter_total"]),
              row("Agentes (name+description)", a["agents"]["frontmatter_total"]),
              row("Commands (name+description)", a["commands"]["frontmatter_total"]),
              ["**Total**", "", fmt(a["always_loaded_total"]["words"]),
               fmt(a["always_loaded_total"]["chars"]), fmt(a["always_loaded_total"]["tokens_est"])],
          ]), "",
          "### Carregado sob demanda (arquivo inteiro)", "",
          table(["Item", "Arquivos", "Palavras", "Caracteres", "Tokens (est.)"], [
              row("Skills", a["skills"]["body_total"]),
              row("Agentes", a["agents"]["body_total"]),
              row("Commands", a["commands"]["body_total"]),
          ]), ""]
    for title, key in (("Top 15 descrições de skill", "frontmatter_top"),
                       ("Top 15 SKILL.md inteiros", "body_top")):
        L += [f"### {title}", "", table(["Skill", "Palavras", "Caracteres", "Tokens (est.)"],
              [[t["name"], fmt(t["words"]), fmt(t["chars"]), fmt(t["tokens_est"])]
               for t in a["skills"][key]]), ""]

    L += ["## B. Uso real (transcripts)", "",
          table(["Métrica", "Valor"], [
              ["Arquivos .jsonl", fmt(b["files_scanned"])],
              ["Linhas malformadas", fmt(b["malformed_lines"])],
              ["Linhas assistant na janela", fmt(b["assistant_lines_in_window"])],
              ["Mensagens únicas (dedup message.id)", fmt(b["assistant_messages_dedup"])],
              ["Sessões principais", fmt(b["sessions"]["main"])],
              ["Execuções de subagente", fmt(b["sessions"]["subagents"])],
              ["Mensagens em principais", fmt(b["messages_by_kind"]["main"])],
              ["Mensagens em subagentes", fmt(b["messages_by_kind"]["subagents"])],
          ]), "",
          "### Totais de usage", "",
          table(["Campo", "Tokens"], [[k, fmt(v)] for k, v in b["usage_totals"].items()]), "",
          "### Por modelo", "",
          table(["Modelo", "Msgs", "input", "cache_creation", "cache_read", "output"],
                [[m, fmt(v["messages"]), fmt(v["input_tokens"]), fmt(v["cache_creation_input_tokens"]),
                  fmt(v["cache_read_input_tokens"]), fmt(v["output_tokens"])]
                 for m, v in b["by_model"].items()]), "",
          "### Por sessão principal", "",
          table(["Métrica", "Mediana", "Média", "p90"],
                [[k, fmt(s.get("median")), fmt(s.get("mean")), fmt(s.get("p90"))]
                 for k, s in (("Entrada total (in+cc+cr)", b["main_per_session"]["input_total"]),
                              ("Output", b["main_per_session"]["output"]),
                              ("Chamadas", b["main_per_session"]["calls"]))]), "",
          "### Contexto inicial (1a chamada: in+cc+cr) - métrica-chave", "",
          table(["Tipo", "n", "Mediana", "Mín", "Máx"],
                [[label, fmt(s.get("n")), fmt(s.get("median")), fmt(s.get("min")), fmt(s.get("max"))]
                 for label, s in (("Sessão principal", b["initial_context_main"]),
                                  ("Subagente", b["initial_context_subagents"]))]), "",
          "### Top 10 sessões principais por entrada total", "",
          table(["Projeto", "sessionId", "Entrada total", "Chamadas"],
                [[t["project"], t["session"], fmt(t["input_total"]), fmt(t["calls"])]
                 for t in b["top10_main_by_input"]]), ""]
    return "\n".join(L)


def parse_date(s):
    return dt.date.fromisoformat(s).isoformat()


def main():
    today = dt.date.today()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--label", required=True)
    ap.add_argument("--since", type=parse_date, default=(today - dt.timedelta(days=30)).isoformat())
    ap.add_argument("--until", type=parse_date, default=today.isoformat())
    args = ap.parse_args()
    if not re.fullmatch(r"[\w-]+", args.label):
        sys.exit("--label só aceita letras, números, '_' e '-'")

    data = {
        "meta": {"label": args.label, "date": today.isoformat(), "since": args.since,
                 "until": args.until, "token_estimate_method": "chars/4"},
        "part_a": part_a(),
        "part_b": part_b(args.since, args.until),
    }
    out_dir = REPO / "metrics"
    out_dir.mkdir(exist_ok=True)
    base = out_dir / f"{today.isoformat()}-{args.label}"
    base.with_suffix(".json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    base.with_suffix(".md").write_text(render_md(data), encoding="utf-8")
    print(f"{base}.json\n{base}.md")


if __name__ == "__main__":
    main()
