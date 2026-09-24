---
name: observability-operations
description: Planeje, implemente ou revise observabilidade e operação de sistemas, incluindo logs, métricas, traces, SLIs/SLOs, alertas, dashboards, incidentes, runbooks, capacidade, backups e recuperação. Use em pedidos sobre monitoramento, confiabilidade, resposta a incidentes ou operação em produção.
---

# Observabilidade e operações

1. Identifique usuários, jornadas críticas, arquitetura, dependências, modos de falha e impacto de negócio.
2. Defina sinais úteis antes das ferramentas: logs estruturados, métricas, traces, eventos e correlação com contexto suficiente.
3. Não registre secrets, tokens, payloads sensíveis ou dados pessoais desnecessários. Defina retenção, acesso, custo e cardinalidade.
4. Escolha SLIs e SLOs ligados à experiência real. Use error budgets quando houver maturidade para decisões baseadas neles.
5. Crie alertas acionáveis com severidade, proprietário, janela, deduplicação e link para runbook. Evite alertas sem ação ou baseados apenas em sintomas internos irrelevantes.
6. Para cada runbook, registre condição, diagnóstico seguro, mitigação, escalonamento, comunicação, rollback e evidência de recuperação.
7. Planeje backups e restauração com RPO/RTO claros; backup não validado por teste de restauração não é garantia de recuperação.
8. Em incidentes, priorize contenção e serviço, preserve evidências e deixe mudanças permanentes para análise posterior.
9. Entregue cobertura proposta, lacunas, dashboards, alertas, runbooks, custos e plano de validação.
