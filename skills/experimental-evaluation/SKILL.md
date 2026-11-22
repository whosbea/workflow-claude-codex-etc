---
name: experimental-evaluation
description: "Planejar avaliação experimental em Computação com baselines e validade: benchmark, simulação, estudo de usuário, comparação."
---

# experimental-evaluation

Base: critérios de avaliação de Wazlawick, caps. 5–6; práticas específicas dependem da subárea (operacionalização do agente, não transcrição do livro).

Entrada: método/proposta, dados e métricas possíveis, recursos, cenários e alegações de desempenho.

## Procedimento
1. Transformar alegações em questões/hipóteses avaliáveis.
2. Escolher baselines adequados (estado da arte, prática corrente e/ou ablação), justificando a ausência quando inevitável.
3. Definir datasets, divisão treino/validação/teste quando pertinente e proteção contra vazamento.
4. Definir métricas primárias e secundárias, unidades, custos, robustez, eficiência e trade-offs.
5. Estabelecer repetições, sementes, intervalos de confiança/testes quando justificáveis, respeitando os pressupostos de cada teste.
6. Prever controles, ablações, sensibilidade, casos negativos e ameaças à validade externa, interna e de constructo.
7. Registrar ambiente, versões, parâmetros e protocolo de reprodutibilidade.
8. Entregar plano de análise e tabelas vazias; só preencher resultados com dados reais.

## Saída
Matriz hipótese→baseline→dados→métrica→análise, protocolo executável, checklist de ameaças e tabelas-modelo.

## Concluído quando
- As comparações sustentam a afirmação científica.
- Significância estatística não é tratada como relevância prática.

## Regras
- Não inventar dados, fontes, citações, resultados nem validações; marcar o que falta com [FONTE PENDENTE], [DADO PENDENTE], [RESULTADO NÃO DISPONÍVEL] ou [DECISÃO METODOLÓGICA PENDENTE].
- Rotular cada afirmação como fato com fonte, resultado documentado, hipótese, interpretação ou decisão proposta.
- Ferramenta ou implementação só conta como contribuição científica com a pergunta e a evidência que a sustentam.
- Encaminhamento: com dados reais em mãos, seguir para `results-discussion`; risco ético em estudo com pessoas vai para `scientific-integrity`.
