---
name: api-design-pattern
description: Use this skill to design or review APIs so they are predictable, secure, documented and consistent, regardless of technology.
---

# API Design Pattern

Use this skill to design or review APIs.

## 1. Resources and routes
- Do routes represent clear resources?
- Are names consistent?
- Are HTTP verbs used correctly?
- Is there versioning when needed?

## 2. Contracts
- Do input and output have a clear contract?
- Are required and optional fields defined?
- Are there examples?
- Is the response predictable?

## 3. HTTP status codes
- Does success use the appropriate status?
- Do errors use the appropriate status?
- Does validation return a clear error?
- Is "resource not found" handled?

## 4. Pagination, filtering and sorting
- Do list endpoints have pagination?
- Are filters documented?
- Is sorting predictable?
- Is there a limit to prevent abuse?

## 5. Security
- Is authentication required where needed?
- Is authorization enforced in the backend?
- Is sensitive data kept from being exposed?
- Is there rate limiting when needed?

## 6. Errors
- Do errors follow a single standard?
- Do messages help the client?
- Are internal details kept from leaking?

## 7. Documentation
- Is the API documented?
- Are there request and response examples?
- Are error cases documented?

## Expected output
Respond with:
1. Diagnosis.
2. Contract problems.
3. Security problems.
4. Consistency improvements.
5. Example of the recommended pattern.
