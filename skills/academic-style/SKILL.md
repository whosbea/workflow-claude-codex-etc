---
name: academic-style
description: "Revisar texto científico (polir, padronizar, traduzir, reescrever) com concisão e precisão, sem alterar evidências."
---

# academic-style

Base: Wazlawick, §10.11 e princípios do agente original (operacionalização do agente, não transcrição do livro).

Entrada: texto original, público, idioma e grau de intervenção solicitado.

## Procedimento
1. Preservar significado, números, qualificadores, referências e modalidade epistêmica.
2. Remover redundância sem perder distinções conceituais.
3. Alternar construções sintáticas quando houver repetição, não apenas trocar palavras.
4. Detectar muletas como dois-pontos repetidos de "afirmação: explicação"; manter a pontuação funcional.
5. Ajustar tempo verbal, paralelismo, conexão lógica, termos técnicos e impessoalidade quando pertinente.
6. Manter afirmações no mesmo grau de força do original ou mais fracas.
7. Sinalizar contradições científicas sem resolvê-las por conjectura.
8. Explicar brevemente só as mudanças substantivas.

## Saída
Texto revisado; notas sobre ambiguidades, afirmações frágeis e pendências só quando houver.

## Concluído quando
- Dados e significado estão preservados.
- Ritmo e precisão melhoraram além de substituições vocabulares.
- Nenhuma ressalva importante foi removida.

## Regras
- Não inventar dados, fontes, citações, resultados nem validações; marcar o que falta com [FONTE PENDENTE], [DADO PENDENTE], [RESULTADO NÃO DISPONÍVEL] ou [DECISÃO METODOLÓGICA PENDENTE].
- Rotular cada afirmação como fato com fonte, resultado documentado, hipótese, interpretação ou decisão proposta.
- Ferramenta ou implementação só conta como contribuição científica com a pergunta e a evidência que a sustentam.
- Encaminhamento: depois da revisão, passar pela `humanizer`; alegação sem lastro encontrada no texto vai para `scientific-integrity`.
