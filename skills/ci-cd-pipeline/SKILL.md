---
name: ci-cd-pipeline
description: Design, implement or review continuous integration, delivery and deployment pipelines in GitHub Actions, GitLab CI, Jenkins, Azure DevOps or equivalents. Use for requests about builds, tests, artifacts, releases, environments, approvals, deploys, rollback, caches or delivery supply chain security.
---

# CI/CD Pipeline

1. Map triggers, branches, environments, artifacts, dependencies, tests, the current deploy process and approval requirements.
2. Organize explicit stages for lint, tests, build, analysis, packaging, publishing, deploy and verification as needed.
3. Pin versions of actions and images when that reduces risk; treat dependencies, artifacts and external inputs as untrusted.
4. Use temporary credentials or federated identity when available. Restrict tokens and environments by least privilege and never expose secrets in logs.
5. Avoid duplication with proportional reuse. Use caching only with correct keys and invalidation; do not confuse cache with artifacts.
6. Keep production deploys separate, with appropriate protections. Define strategy, health checks, timeout, rollback and handling of partial runs.
7. Do not trigger a real release or deploy without an explicit request and confirmation of the repository, environment and version.
8. Validate syntax and safe behavior; deliver the flow, changes, risks, rollback and how to test.
