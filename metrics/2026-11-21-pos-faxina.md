# Métricas de tokens: pos-faxina (2026-11-21)

Janela: 2026-10-22 a 2026-11-21 (UTC). Tokens da Parte A = ESTIMATIVA (caracteres/4).

## A. Contexto fixo

Skills: 90 | Agentes: 12 | Commands: 6

Ignorados (sem SKILL.md): synced

### Sempre carregado

| Item | Arquivos | Palavras | Caracteres | Tokens (est.) |
|---|---|---|---|---|
| CLAUDE.md | 1 | 1.327 | 8.704 | 2.176 |
| Skills (name+description) | 90 | 3.052 | 22.542 | 5.635 |
| Agentes (name+description) | 12 | 283 | 2.336 | 584 |
| Commands (name+description) | 6 | 138 | 1.060 | 265 |
| **Total** |  | 4.800 | 34.642 | 8.660 |

### Carregado sob demanda (arquivo inteiro)

| Item | Arquivos | Palavras | Caracteres | Tokens (est.) |
|---|---|---|---|---|
| Skills | 90 | 110.740 | 737.000 | 184.254 |
| Agentes | 12 | 5.995 | 41.154 | 10.289 |
| Commands | 6 | 540 | 4.376 | 1.094 |

### Top 15 descrições de skill

| Skill | Palavras | Caracteres | Tokens (est.) |
|---|---|---|---|
| impeccable | 121 | 925 | 231 |
| mobile-native | 127 | 771 | 193 |
| imagegen-frontend-web | 93 | 702 | 176 |
| imagegen-frontend-mobile | 90 | 682 | 170 |
| image-to-code | 83 | 588 | 147 |
| animate-expo | 84 | 555 | 139 |
| yt-audience-insights | 73 | 531 | 133 |
| write-swift | 76 | 513 | 128 |
| ponytail-review | 62 | 507 | 127 |
| animate | 75 | 499 | 125 |
| brandkit | 55 | 492 | 123 |
| improve-animations | 77 | 485 | 121 |
| animation-vocabulary | 76 | 464 | 116 |
| apple-design | 52 | 457 | 114 |
| ask-sonner | 69 | 453 | 113 |

### Top 15 SKILL.md inteiros

| Skill | Palavras | Caracteres | Tokens (est.) |
|---|---|---|---|
| design-taste-frontend | 12.853 | 87.126 | 21.782 |
| write-swift | 6.053 | 42.214 | 10.554 |
| graphify | 5.211 | 41.216 | 10.304 |
| imagegen-frontend-mobile | 6.552 | 40.285 | 10.071 |
| imagegen-frontend-web | 5.819 | 36.780 | 9.195 |
| image-to-code | 5.820 | 36.361 | 9.090 |
| humanizer | 4.593 | 28.696 | 7.174 |
| emil-design-eng | 3.865 | 27.029 | 6.757 |
| apple-design | 3.479 | 22.880 | 5.720 |
| design-taste-frontend-v1 | 2.937 | 21.190 | 5.298 |
| animate-expo | 2.840 | 17.785 | 4.446 |
| mobile-native | 2.690 | 16.787 | 4.197 |
| brandkit | 2.600 | 15.967 | 3.992 |
| redesign-existing-projects | 2.210 | 15.032 | 3.758 |
| animation-vocabulary | 2.208 | 13.181 | 3.295 |

## B. Uso real (transcripts)

| Métrica | Valor |
|---|---|
| Arquivos .jsonl | 181 |
| Linhas malformadas | 0 |
| Linhas assistant na janela | 14.391 |
| Mensagens únicas (dedup message.id) | 6.517 |
| Sessões principais | 14 |
| Execuções de subagente | 163 |
| Mensagens em principais | 1.506 |
| Mensagens em subagentes | 5.011 |

### Totais de usage

| Campo | Tokens |
|---|---|
| input_tokens | 14.088 |
| cache_creation_input_tokens | 51.690.309 |
| cache_read_input_tokens | 1.139.063.777 |
| output_tokens | 7.142.349 |

### Por modelo

| Modelo | Msgs | input | cache_creation | cache_read | output |
|---|---|---|---|---|---|
| claude-opus-5-5 | 6.383 | 13.882 | 50.839.106 | 1.130.525.861 | 6.914.066 |
| claude-haiku-5-5 | 100 | 206 | 851.203 | 8.537.916 | 228.283 |
| <synthetic> | 34 | 0 | 0 | 0 | 0 |

### Por sessão principal

| Métrica | Mediana | Média | p90 |
|---|---|---|---|
| Entrada total (in+cc+cr) | 7.945.248,5 | 29.917.093,9 | 118.947.982 |
| Output | 46.253,5 | 97.148,7 | 289.089 |
| Chamadas | 55,5 | 107,6 | 334 |

### Contexto inicial (1a chamada: in+cc+cr) - métrica-chave

| Tipo | n | Mediana | Mín | Máx |
|---|---|---|---|---|
| Sessão principal | 14 | 54.835,5 | 45.956 | 93.555 |
| Subagente | 163 | 18.572 | 11.493 | 73.371 |

### Top 10 sessões principais por entrada total

| Projeto | sessionId | Entrada total | Chamadas |
|---|---|---|---|
| -Users-bea-Workspace-tcc | 325f7835-c797-47e3-8580-5238182772c4 | 127.479.713 | 334 |
| -Users-bea-workspace-youtube | cc7aee34-f760-4765-9e0c-12d7a5179128 | 118.947.982 | 443 |
| -Users-bea-workspace-Projetos-financas | a79f4740-ad27-4b48-99ac-f3896c1656ba | 97.556.391 | 240 |
| -Users-bea-workspace-portfolio | dd69bca3-04ef-4c2d-b260-8c80f4bd7e77 | 25.279.369 | 123 |
| -Users-bea-workspace-xadrez | c45f4d3e-c093-47ac-80d9-8b3148748747 | 11.027.074 | 73 |
| -Users-bea-Workspace-Lab-inova--o-classifier-prisma | edb3fc26-ad86-46ec-8d04-b002a226de39 | 10.667.987 | 64 |
| -Users-bea-Workspace-workflow-claude-codex-etc | 6ac364d3-76d7-4db0-b8e0-53df6e6dc384 | 8.565.400 | 50 |
| -Users-bea-Workspace-tcc | a9660e51-0176-4b7f-9d8d-de66c8a9d4d8 | 7.325.097 | 61 |
| -Users-bea-Workspace-Lab-inova--o-classifier-prisma | 328e5d50-7d8e-4977-93a7-003078accfc1 | 4.855.764 | 38 |
| -Users-bea-Workspace-workflow-claude-codex-etc | 3189d5fd-9a03-4fbc-9378-08173c07a383 | 2.986.217 | 27 |
