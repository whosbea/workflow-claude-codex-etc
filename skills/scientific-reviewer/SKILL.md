---
name: scientific-reviewer
description: "Revisar manuscrito como parecerista, com diagnóstico verificável, inclusive antes de submissão."
---

# scientific-reviewer

Base: Wazlawick, caps. 5, 9, 11 e 13 (operacionalização do agente, não transcrição do livro).

Entrada: manuscrito completo/parcial, normas do veículo se houver e evidências anexas.

## Procedimento
1. Classificar tipo, objetivo e contribuição alegada.
2. Avaliar problema, novidade sustentada, relação com o estado da arte, objetivos e justificativa.
3. Auditar métodos, controles, baselines, evidências, validade, reprodutibilidade e ética.
4. Checar coerência entre resumo, introdução, método, resultados e conclusão.
5. Avaliar a cobertura das 20 perguntas conforme a pertinência, não como checklist mecânico.
6. Separar problemas fatais, maiores, menores e estilísticos, citando trechos/locais.
7. Recomendar correções acionáveis e alegações proporcionais.
8. Não prever aceitação nem atribuir notas sem rubrica explícita.

## Saída
Parecer no modelo `templates/parecer-cientifico.md` (nesta pasta da skill), com pontos fortes, problemas por gravidade, evidências do manuscrito e plano de revisão priorizado. Omita o que não se aplica.

## Concluído quando
- Cada crítica aponta localização e fundamento.
- Ausência de dados aparece como insuficiência de evidência, não como fraude.
- Preferência editorial não é tratada como erro metodológico.

## Regras
- Não inventar dados, fontes, citações, resultados nem validações; marcar o que falta com [FONTE PENDENTE], [DADO PENDENTE], [RESULTADO NÃO DISPONÍVEL] ou [DECISÃO METODOLÓGICA PENDENTE].
- Rotular cada afirmação como fato com fonte, resultado documentado, hipótese, interpretação ou decisão proposta.
- Ferramenta ou implementação só conta como contribuição científica com a pergunta e a evidência que a sustentam.
- Encaminhamento: problemas de integridade vão para `scientific-integrity`; cada correção segue para a skill da etapa afetada (método, avaliação, escrita etc.).
