---
name: code-review-checklist
description: Use this skill to review code with a focus on clarity, maintainability, simplicity, consistency, readability, project conventions and technical impact.
---

# Code Review Checklist

Use this checklist when reviewing code.

## 1. Clarity
- Is the code easy to understand?
- Do names explain intent?
- Is there hidden or overly "clever" logic?
- Are there comments trying to make up for confusing code?

## 2. Responsibility
- Does each function, class, module or component have a clear responsibility?
- Is business logic mixed with infrastructure and presentation?
- Is there unnecessary coupling?

## 3. Simplicity
- Is there overengineering?
- Are there abstractions created before they are needed?
- Does the code solve the real problem, or does it try to predict an uncertain future?

## 4. Consistency
- Does the code follow the project's conventions?
- Does the structure match the rest of the codebase?
- Are there different styles for solving the same problem?

## 5. Errors and edge cases
- Are errors handled?
- Were null, empty and invalid cases considered?
- Do error messages help?

## 6. Maintainability
- Will the change be easy to modify later?
- Is there duplication?
- Is there a risk of regression?

## Expected output
Respond with:
1. Overall summary.
2. Critical problems.
3. Important improvements.
4. Optional adjustments.
5. Practical recommendations.
