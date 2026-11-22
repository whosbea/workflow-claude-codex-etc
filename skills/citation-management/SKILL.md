---
name: citation-management
description: "Gerir citações, referências, BibTeX/LaTeX e rastreabilidade de alegações."
---

# citation-management

Base: Wazlawick, cap. 7, §10.10 e cap. 12 (operacionalização do agente, não transcrição do livro).

Entrada: fontes efetivamente fornecidas/acessadas, estilo requerido e texto com afirmações.

## Procedimento
1. Extrair metadados exclusivamente de fonte verificável; nunca deduzir DOI, volume ou paginação.
2. Construir registro fonte↔alegação e marcar afirmações sem lastro.
3. Distinguir citação direta, paráfrase, interpretação e conhecimento do autor.
4. Verificar que as citações no texto correspondem à bibliografia e vice-versa, conforme o estilo.
5. Gerar entradas BibTeX só com campos confirmados; registrar os ausentes sem inventar.
6. Verificar URLs, DOI e metadados apenas se fontes e ferramentas permitirem.
7. Evitar citação decorativa ou empilhamento de referências que não sustentam a afirmação.
8. Respeitar normas de atribuição e direitos autorais.

## Saída
Matriz alegação→fonte→status, bibliografia/BibTeX confiável e lista de campos e citações pendentes.

## Concluído quando
- Todas as entradas são rastreáveis.
- Fontes não acessadas estão rotuladas como não verificadas.

## Regras
- Não inventar dados, fontes, citações, resultados nem validações; marcar o que falta com [FONTE PENDENTE], [DADO PENDENTE], [RESULTADO NÃO DISPONÍVEL] ou [DECISÃO METODOLÓGICA PENDENTE].
- Rotular cada afirmação como fato com fonte, resultado documentado, hipótese, interpretação ou decisão proposta.
- Ferramenta ou implementação só conta como contribuição científica com a pergunta e a evidência que a sustentam.
- Encaminhamento: afirmação que nenhuma fonte sustenta vai para `scientific-integrity`, sem buscar citação que a justifique a posteriori.
