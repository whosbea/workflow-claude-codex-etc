---
name: test-plan-generator
description: Generate a test plan (unit, integration, e2e, contract, regression) for a feature or module. Use when deciding what to test.
---

# Test Plan Generator

1. **Understand**: expected behavior, business rule, valid and invalid inputs, permissions, external dependencies.
2. **Scenarios**: happy path, validation, nonexistent resource, user without permission, empty state, external error, likely regressions.
3. **Types**: pick among unit, integration, e2e, contract and regression per scenario.
4. **Quality**: each test has a clear name, Arrange-Act-Assert, input data, expected result and a reason to exist.

## Output

1. Scenario table: scenario, type, input, expected result, priority.
2. Edge cases not in the table, if any.
3. Implementation suggestion (framework, files) in 2–3 lines.
