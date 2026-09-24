---
name: ci-cd-pipeline
description: Projete, implemente ou revise pipelines de integração, entrega e deploy contínuos em GitHub Actions, GitLab CI, Jenkins, Azure DevOps ou equivalentes. Use em pedidos sobre build, testes, artefatos, releases, ambientes, aprovações, deploy, rollback, caches ou segurança da cadeia de entrega.
---

# Pipeline CI/CD

1. Mapeie gatilhos, branches, ambientes, artefatos, dependências, testes, deploy atual e requisitos de aprovação.
2. Organize etapas explícitas para lint, testes, build, análise, empacotamento, publicação, deploy e verificação conforme necessário.
3. Fixe versões de actions e imagens quando isso reduzir risco; trate dependências, artefatos e entradas externas como não confiáveis.
4. Use credenciais temporárias ou identidade federada quando disponível. Restrinja tokens e ambientes pelo menor privilégio e nunca exponha secrets em logs.
5. Evite duplicação com reutilização proporcional. Use cache somente com chaves e invalidação corretas; não confunda cache com artefato.
6. Separe deploy de produção com proteções adequadas. Defina estratégia, health checks, timeout, rollback e tratamento de execução parcial.
7. Não dispare release ou deploy real sem pedido explícito e confirmação do repositório, ambiente e versão.
8. Valide sintaxe e comportamento seguro; entregue fluxo, mudanças, riscos, rollback e como testar.
