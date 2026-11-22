---
name: secure-coding-checklist
description: Defensive security review of code: input, authentication, authorization, sensitive data, logs, secrets, queries, uploads, dependencies.
---

# Secure Coding Checklist

Check each area:

1. **Input**: every input validated (type, size, format); external data treated as untrusted.
2. **Authentication**: secure login flow, tokens handled correctly, sessions expire, secrets out of the code.
3. **Authorization**: users reach only what they are allowed to; no IDOR; permissions checked in the backend; sensitive routes protected.
4. **Sensitive data**: personal data minimized; logs and errors expose no sensitive or internal details; no leakage paths.
5. **Database**: parameterized queries, no injection, filters respect the authenticated user.
6. **Uploads**: type and size validated, file names sanitized, public files expose no private data.
7. **Dependencies and configuration**: only necessary, non-suspicious packages; secure CORS, rate limiting and environment settings.

## Output

One table, most severe first; omit severities with no findings:

| Severity (Critical / High / Medium / Low / Recommendation) | Location | Finding | Impact | Mitigation |
|---|---|---|---|---|
