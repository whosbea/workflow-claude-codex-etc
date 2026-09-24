# md-convert.awk — operações em Markdown com frontmatter YAML simples.
#
# Usado pelo install.sh. Só depende de awk POSIX (BSD awk do macOS, gawk, mawk).
# Rode com LC_ALL=C para processar bytes de forma determinística (UTF-8 é
# preservado byte a byte).
#
# Modos (-v mode=...):
#   get          -v key=K         imprime o valor de K no frontmatter ("" se ausente)
#   set-name     -v newname=N     reescreve (ou insere) "name:" e mantém o resto intacto
#   agent-toml   [-v name=N] [-v label=L]
#                                 converte um agente Claude Code (.md) no formato
#                                 ~/.codex/agents/<nome>.toml (name, description,
#                                 developer_instructions)
#   command-skill -v name=N [-v label=L]
#                                 converte um slash command do Claude Code em
#                                 SKILL.md (Codex e ferramentas de ~/.agents/skills)
#
# Exemplo:
#   LC_ALL=C awk -v mode=agent-toml -f scripts/md-convert.awk agents/backend-engineer.md
#
# Parser YAML deliberadamente mínimo: "chave: valor", valores entre aspas simples
# ou duplas e blocos ">" / "|" (linhas indentadas unidas por espaço). É o que os
# arquivos deste repo e dos terceiros usam; não é um parser YAML completo.

BEGIN {
    ctrl = ""
    for (i = 1; i < 32; i++)
        if (i != 9 && i != 10)
            ctrl = ctrl sprintf("%c", i)
    ctrl = ctrl sprintf("%c", 127)
    state = "start"
    nf = 0
    nb = 0
}

# Escapa para string básica TOML e string YAML entre aspas duplas.
# Remove caracteres de controle (inválidos em TOML), exceto tab (vira \t).
function esc(s,    out, i, c) {
    out = ""
    for (i = 1; i <= length(s); i++) {
        c = substr(s, i, 1)
        if (c == "\\") out = out "\\\\"
        else if (c == "\"") out = out "\\\""
        else if (c == "\t") out = out "\\t"
        else if (index(ctrl, c) > 0) continue
        else out = out c
    }
    return out
}

# Desfaz escapes comuns de string YAML entre aspas duplas.
function unesc_dq(s,    out, i, c, n) {
    out = ""
    for (i = 1; i <= length(s); i++) {
        c = substr(s, i, 1)
        if (c == "\\" && i < length(s)) {
            n = substr(s, ++i, 1)
            if (n == "n" || n == "t") out = out " "
            else out = out n
        } else out = out c
    }
    return out
}

function trim(s) {
    sub(/^[ \t]+/, "", s)
    sub(/[ \t]+$/, "", s)
    return s
}

function fmget(key,    i, line, v, out, l) {
    for (i = 1; i <= nf; i++) {
        line = fm[i]
        if (index(line, key ":") != 1) continue
        v = trim(substr(line, length(key) + 2))
        if (v ~ /^[>|][-+]?[0-9]*$/) {
            out = ""
            for (i++; i <= nf; i++) {
                l = fm[i]
                if (l != "" && l !~ /^[ \t]/) break
                l = trim(l)
                if (l != "") out = (out == "" ? l : out " " l)
            }
            return out
        }
        if (length(v) >= 2 && substr(v, 1, 1) == "\"" && substr(v, length(v), 1) == "\"")
            return unesc_dq(substr(v, 2, length(v) - 2))
        if (length(v) >= 2 && substr(v, 1, 1) == "'" && substr(v, length(v), 1) == "'") {
            v = substr(v, 2, length(v) - 2)
            gsub(/''/, "'", v)
            return v
        }
        return v
    }
    return ""
}

# Primeira/última linha não vazia do corpo.
function body_bounds() {
    bfirst = 1
    while (bfirst <= nb && trim(body[bfirst]) == "") bfirst++
    blast = nb
    while (blast >= bfirst && trim(body[blast]) == "") blast--
}

mode != "set-name" { sub(/\r$/, "") }

state == "start" {
    if ($0 ~ /^---[ \t\r]*$/) { state = "fm"; next }
    state = "body"
}
state == "fm" {
    if ($0 ~ /^---[ \t\r]*$/) { state = "body"; next }
    fm[++nf] = $0
    next
}
{ body[++nb] = $0 }

END {
    if (state == "fm") {
        print "md-convert: frontmatter sem '---' de fechamento em " FILENAME > "/dev/stderr"
        exit 2
    }

    if (mode == "get") {
        print fmget(key)
        exit 0
    }

    if (mode == "set-name") {
        if (newname == "") { print "md-convert: newname vazio" > "/dev/stderr"; exit 2 }
        print "---"
        done = 0
        for (i = 1; i <= nf; i++) {
            if (!done && index(fm[i], "name:") == 1) { print "name: " newname; done = 1 }
            else print fm[i]
        }
        if (!done) print "name: " newname
        print "---"
        for (i = 1; i <= nb; i++) print body[i]
        exit 0
    }

    if (mode == "agent-toml") {
        if (name == "") name = fmget("name")
        if (name == "") { print "md-convert: agente sem name em " FILENAME > "/dev/stderr"; exit 2 }
        desc = fmget("description")
        body_bounds()
        if (label != "")
            print "# Gerado pelo install.sh (workflow-ai) a partir de " label ". Não edite aqui: altere a origem e rode ./install.sh."
        print "name = \"" esc(name) "\""
        print "description = \"" esc(desc) "\""
        print "developer_instructions = \"\"\""
        for (i = bfirst; i <= blast; i++) print esc(body[i])
        print "\"\"\""
        exit 0
    }

    if (mode == "command-skill") {
        if (name == "") { print "md-convert: name obrigatório no modo command-skill" > "/dev/stderr"; exit 2 }
        body_bounds()
        desc = fmget("description")
        if (desc == "") {
            desc = body[bfirst]
            sub(/^#+[ \t]*/, "", desc)
            desc = trim(desc)
        }
        desc = desc " Equivale ao comando /" name " do Claude Code; use quando o usuário pedir " name "."
        print "---"
        print "name: " name
        print "description: \"" esc(desc) "\""
        print "---"
        print ""
        if (label != "") {
            print "<!-- Gerado pelo install.sh (workflow-ai) a partir de " label ". Não edite aqui: altere a origem e rode ./install.sh. -->"
            print ""
        }
        for (i = bfirst; i <= blast; i++) {
            line = body[i]
            gsub(/\$ARGUMENTS/, "(o pedido do usuário na mensagem que acionou esta skill)", line)
            print line
        }
        exit 0
    }

    print "md-convert: modo desconhecido: " mode > "/dev/stderr"
    exit 2
}
