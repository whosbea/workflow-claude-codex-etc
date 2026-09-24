---
name: secure-coding-checklist
description: Use esta skill para revisar segurança de código, APIs, permissões, validação, autenticação, autorização, dados sensíveis, logs, secrets e dependências.
---

# Secure Coding Checklist

Use esta checklist em revisões de segurança defensiva.

## 1. Entrada de dados
- Toda entrada é validada?
- Tipos, tamanhos e formatos são verificados?
- Dados externos são tratados como não confiáveis?

## 2. Autenticação
- O fluxo de login é seguro?
- Tokens são tratados corretamente?
- Sessões expiram?
- Secrets não aparecem no código?

## 3. Autorização
- O usuário só acessa o que pode?
- Há risco de IDOR?
- Permissões são verificadas no backend?
- Rotas sensíveis têm proteção?

## 4. Dados sensíveis
- Dados pessoais são minimizados?
- Logs expõem informação sensível?
- Erros retornam detalhes internos?
- Existe risco de vazamento?

## 5. Banco e queries
- Queries usam parâmetros?
- Há risco de injeção?
- Filtros respeitam o usuário autenticado?

## 6. Uploads e arquivos
- Tipo e tamanho são validados?
- Nomes de arquivo são tratados?
- Arquivos públicos não expõem dados privados?

## 7. Dependências e configuração
- Dependências são necessárias?
- Existem pacotes suspeitos?
- Configuração de CORS, rate limit e ambiente está segura?

## Saída esperada
Classifique achados em:
- Crítico.
- Alto.
- Médio.
- Baixo.
- Recomendação.

Sempre explique impacto e mitigação.
