---
name: api-design-pattern
description: Design or review APIs and endpoints: routes, contracts, status codes, errors, pagination, auth.
---

# API Design Pattern

Check each area:

1. **Resources and routes**: clear resources, consistent names, correct HTTP verbs, versioning when needed.
2. **Contracts**: clear input and output, required vs optional fields defined, examples, predictable responses.
3. **Status codes**: appropriate codes for success and errors, clear validation errors, "not found" handled.
4. **Lists**: pagination, documented filters, predictable sorting, a limit that prevents abuse.
5. **Security**: authentication where needed, authorization enforced in the backend, no sensitive data exposed, rate limiting when needed.
6. **Errors**: one error format, messages that help the client, no internal details leaked.
7. **Documentation**: request and response examples, error cases documented.

## Output

Short lists, skipping empty sections:

1. Diagnosis (2–3 lines).
2. Contract problems.
3. Security problems.
4. Consistency improvements.
5. One example of the recommended pattern.
