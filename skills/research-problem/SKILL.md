---
name: research-problem
description: "Transformar tema de Computação em problema científico e questões investigáveis, quando o tema está mal delimitado."
---

# research-problem

Base: Wazlawick, §§6.1.2–6.1.7 e cap. 8 (operacionalização do agente, não transcrição do livro).

Entrada: tema, contexto, público/sistema, dificuldade percebida, restrições e evidência disponível. Sem literatura, a lacuna é *hipótese a verificar*, nunca descoberta.

## Procedimento
1. Reformular o tema em uma frase neutra, sem tecnologia pré-escolhida.
2. Separar **problema prático** de **problema de conhecimento**; propor o segundo quando houver.
3. Identificar objeto, escopo, contexto, critérios de sucesso e população/ambiente.
4. Gerar uma pergunta principal específica, investigável e viável; derivar até 3 subperguntas.
5. Classificar as questões em exploratórias, descritivas, causais ou de design e explicar a evidência que cada tipo exige.
6. Listar soluções prévias/alternativas a examinar e riscos de irrelevância ou falsa novidade.
7. Formular limites e premissas. Se não houver questão científica, dizer que ainda há apenas um projeto técnico.

## Saída
- Tema delimitado, problema em 1 parágrafo, pergunta principal e subperguntas.
- Evidências necessárias para justificar relevância/lacuna e riscos de escopo.
- O que ainda depende de consulta à literatura.

## Concluído quando
- A pergunta vai além de "como implementar X".
- A resposta pode ser observável, comparável ou demonstrável.
- Nenhum ineditismo é afirmado sem busca.

## Regras
- Não inventar dados, fontes, citações, resultados nem validações; marcar o que falta com [FONTE PENDENTE], [DADO PENDENTE], [RESULTADO NÃO DISPONÍVEL] ou [DECISÃO METODOLÓGICA PENDENTE].
- Rotular cada afirmação como fato com fonte, resultado documentado, hipótese, interpretação ou decisão proposta.
- Ferramenta ou implementação só conta como contribuição científica com a pergunta e a evidência que a sustentam.
- Encaminhamento: lacuna que depende de busca vai para `literature-review`; problema delimitado segue para `research-design`.
