---
name: secure-coding-checklist
description: Use this skill to review the security of code, APIs, permissions, validation, authentication, authorization, sensitive data, logs, secrets and dependencies.
---

# Secure Coding Checklist

Use this checklist in defensive security reviews.

## 1. Data input
- Is every input validated?
- Are types, sizes and formats checked?
- Is external data treated as untrusted?

## 2. Authentication
- Is the login flow secure?
- Are tokens handled correctly?
- Do sessions expire?
- Are secrets kept out of the code?

## 3. Authorization
- Can users access only what they are allowed to?
- Is there an IDOR risk?
- Are permissions checked in the backend?
- Are sensitive routes protected?

## 4. Sensitive data
- Is personal data minimized?
- Do logs expose sensitive information?
- Do errors return internal details?
- Is there a risk of data leakage?

## 5. Database and queries
- Do queries use parameters?
- Is there an injection risk?
- Do filters respect the authenticated user?

## 6. Uploads and files
- Are type and size validated?
- Are file names sanitized?
- Do public files avoid exposing private data?

## 7. Dependencies and configuration
- Are the dependencies necessary?
- Are there suspicious packages?
- Are CORS, rate limiting and environment settings secure?

## Expected output
Classify findings as:
- Critical.
- High.
- Medium.
- Low.
- Recommendation.

Always explain impact and mitigation.
