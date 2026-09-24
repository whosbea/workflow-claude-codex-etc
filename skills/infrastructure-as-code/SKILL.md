---
name: infrastructure-as-code
description: Design, implement or review infrastructure as code with Terraform, OpenTofu, CloudFormation, Pulumi, Ansible or equivalent tools. Use for requests about modules, environments, remote state, networking, IAM, containers, cloud, drift, plans or reviews of infrastructure changes.
---

# Infrastructure as Code

1. Identify the tool, provider, environments, current state, conventions and constraints before proposing code.
2. Model resources declaratively, idempotently, reproducibly and in proportion to the project.
3. Separate configuration per environment without excessive duplication. Protect state, locks, credentials and sensitive data.
4. Apply least privilege to IAM, networking and secret access. Do not write secrets to code, exposed state, logs or examples.
5. Assess dependencies, drift, import of existing resources, cost impact and risk of downtime.
6. Before `apply`, `destroy`, an import or a migration, present the plan, the exact target, the destructive changes, the validation and the rollback; run it only with explicit authorization.
7. Validate formatting, syntax and the plan using the project's tools. Do not treat a plan as an absolute guarantee.
8. Deliver changed files, decisions, validation evidence, impact, rollback and open items.
