---
name: test-plan-generator
description: Use this skill to generate a test plan covering unit, integration, e2e, contract and regression tests for a feature or module.
---

# Test Plan Generator

Use this skill to turn a feature into a test plan.

## 1. Understanding
Identify:
- The expected behavior.
- The business rule.
- Valid inputs.
- Invalid inputs.
- Permissions involved.
- External dependencies.

## 2. Scenarios
Cover:
- Happy path.
- Validation.
- Nonexistent resource.
- User without permission.
- Empty state.
- External error.
- Likely regressions.

## 3. Test types
Suggest:
- Unit.
- Integration.
- E2E.
- Contract.
- Regression.

## 4. Quality
Each test must have:
- A clear name.
- Arrange, Act, Assert.
- Input data.
- Expected result.
- A reason to exist.

## Expected output
Respond with:
1. Overall plan.
2. Scenario table.
3. Priority tests.
4. Edge cases.
5. Implementation suggestion.
