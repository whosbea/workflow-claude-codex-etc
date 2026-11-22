---
name: code-review-checklist
description: Review code (diff, PR, module) against project conventions: clarity, simplicity, consistency, errors, maintainability.
---

# Code Review Checklist

Check each area:

1. **Clarity**: easy to understand, names explain intent, no hidden or overly "clever" logic, no comments compensating for confusing code.
2. **Responsibility**: each function, class, module or component has one clear responsibility; business logic is not mixed with infrastructure or presentation; no unnecessary coupling.
3. **Simplicity**: no overengineering or premature abstraction; solves the real problem, not an uncertain future.
4. **Consistency**: follows project conventions and the structure of the rest of the codebase; one style per problem.
5. **Errors and edge cases**: errors handled; null, empty and invalid cases considered; error messages help.
6. **Maintainability**: easy to change later, no duplication, regression risk assessed.

## Output

Short lists, skipping empty sections; each finding points to file and line:

1. Summary (2–3 lines).
2. Critical problems.
3. Important improvements.
4. Optional adjustments.
