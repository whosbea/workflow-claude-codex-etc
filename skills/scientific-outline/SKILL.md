---
name: scientific-outline
description: "Criar esqueleto adaptativo de artigo (estrutura, sumário, seções) cobrindo as 20 perguntas geradoras."
---

# scientific-outline

Base: Wazlawick, caps. 10–11 + 20 perguntas geradoras do agente (operacionalização do agente, não transcrição do livro).

Entrada: tema ou pergunta de pesquisa, tipo de artigo, contribuição, evidências já disponíveis e normas do veículo se fornecidas.

## Procedimento
1. Propor 2–3 títulos provisórios específicos, sem superlativos.
2. Identificar o tipo de artigo (teórico, método, empírico, relato etc.) antes de escolher a estrutura.
3. Criar seções e subseções proporcionais ao tipo; esquema padrão: resumo, introdução, relacionados/fundamentação, metodologia/proposta, avaliação/resultados, discussão, conclusão, referências.
4. Para cada seção, indicar função retórica, tópicos indispensáveis, insumos, evidências, figuras/tabelas úteis, questões geradoras e critério de completude.
5. Partir do modelo `templates/esqueleto-artigo.md` e do catálogo `references/20-perguntas-geradoras.md` (nesta pasta da skill); cobrir as 20 perguntas sem forçar uma pergunta em seção inadequada.
6. Construir a matriz pergunta→seção→evidência necessária→status; uma pergunta pode estar em várias seções.
7. Identificar buracos de conhecimento; nunca escrever "resultados demonstram" sem resultados.
8. Indicar a ordem recomendada de escrita, separada da ordem de leitura.

## Saída
Título(s), sumário hierárquico, roteiro tópico por seção em listas curtas, matriz das 20 perguntas, figuras/tabelas propostas e pendências. Seção sem conteúdo previsto fica fora.

## Concluído quando
- Todas as 20 perguntas têm destino, evidência requerida e status.
- Problema, objetivo, método e conclusão pretendida estão alinhados.
- Nenhuma seção promete achados inexistentes.

## Regras
- Não inventar dados, fontes, citações, resultados nem validações; marcar o que falta com [FONTE PENDENTE], [DADO PENDENTE], [RESULTADO NÃO DISPONÍVEL] ou [DECISÃO METODOLÓGICA PENDENTE].
- Rotular cada afirmação como fato com fonte, resultado documentado, hipótese, interpretação ou decisão proposta.
- Ferramenta ou implementação só conta como contribuição científica com a pergunta e a evidência que a sustentam.
- Encaminhamento: redação das seções segue para `scientific-writing`; pergunta geradora sem evidência fica como pendência, sem texto de preenchimento.
