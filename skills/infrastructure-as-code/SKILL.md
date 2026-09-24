---
name: infrastructure-as-code
description: Projete, implemente ou revise infraestrutura como código com Terraform, OpenTofu, CloudFormation, Pulumi, Ansible ou ferramentas equivalentes. Use em pedidos sobre módulos, ambientes, estado remoto, redes, IAM, containers, cloud, drift, planos ou revisão de mudanças de infraestrutura.
---

# Infraestrutura como código

1. Identifique ferramenta, provedor, ambientes, estado atual, convenções e restrições antes de propor código.
2. Modele recursos de forma declarativa, idempotente, reproduzível e proporcional ao projeto.
3. Separe configuração por ambiente sem duplicação excessiva. Proteja state, locks, credenciais e dados sensíveis.
4. Aplique menor privilégio em IAM, redes e acesso a secrets. Não grave secrets em código, state exposto, logs ou exemplos.
5. Avalie dependências, drift, importação de recursos existentes, impacto financeiro e risco de indisponibilidade.
6. Antes de `apply`, `destroy`, importação ou migração, apresente o plano, o alvo exato, as mudanças destrutivas, a validação e o rollback; execute apenas com autorização explícita.
7. Valide formatação, sintaxe e plano usando as ferramentas do projeto. Não trate um plano como garantia absoluta.
8. Entregue arquivos alterados, decisões, evidências de validação, impacto, rollback e pendências.
