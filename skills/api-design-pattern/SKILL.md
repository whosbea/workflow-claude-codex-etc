---
name: api-design-pattern
description: Use esta skill para projetar ou revisar APIs de forma previsível, segura, documentada e consistente, independente de tecnologia.
---

# API Design Pattern

Use esta skill para projetar ou revisar APIs.

## 1. Recursos e rotas
- Rotas representam recursos claros?
- Nomes são consistentes?
- Verbos HTTP foram usados corretamente?
- Existe versionamento quando necessário?

## 2. Contratos
- Entrada e saída têm contrato claro?
- Campos obrigatórios e opcionais estão definidos?
- Existem exemplos?
- A resposta é previsível?

## 3. Status HTTP
- Sucesso usa status adequado?
- Erros usam status adequado?
- Validação retorna erro claro?
- Recurso não encontrado é tratado?

## 4. Paginação, filtro e ordenação
- Listagens têm paginação?
- Filtros são documentados?
- Ordenação é previsível?
- Há limite para evitar abuso?

## 5. Segurança
- Autenticação é exigida onde precisa?
- Autorização é aplicada no backend?
- Dados sensíveis não são expostos?
- Existe rate limit quando necessário?

## 6. Erros
- Erros seguem padrão único?
- Mensagens ajudam o cliente?
- Detalhes internos não vazam?

## 7. Documentação
- A API é documentada?
- Existem exemplos de request e response?
- Casos de erro estão documentados?

## Saída esperada
Responda com:
1. Diagnóstico.
2. Problemas de contrato.
3. Problemas de segurança.
4. Melhorias de consistência.
5. Exemplo de padrão recomendado.
