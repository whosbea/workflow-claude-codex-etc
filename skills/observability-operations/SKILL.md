---
name: observability-operations
description: Plan, implement or review system observability and operations, including logs, metrics, traces, SLIs/SLOs, alerts, dashboards, incidents, runbooks, capacity, backups and recovery. Use for requests about monitoring, reliability, incident response or production operations.
---

# Observability and Operations

1. Identify users, critical journeys, architecture, dependencies, failure modes and business impact.
2. Define useful signals before tools: structured logs, metrics, traces, events and correlation with enough context.
3. Do not log secrets, tokens, sensitive payloads or unnecessary personal data. Define retention, access, cost and cardinality.
4. Choose SLIs and SLOs tied to the real user experience. Use error budgets when the team is mature enough to make decisions based on them.
5. Create actionable alerts with severity, owner, window, deduplication and a runbook link. Avoid alerts with no action or based only on irrelevant internal symptoms.
6. For each runbook, record the condition, safe diagnosis, mitigation, escalation, communication, rollback and evidence of recovery.
7. Plan backups and restores with clear RPO/RTO; a backup not validated by a restore test is no guarantee of recovery.
8. During incidents, prioritize containment and service, preserve evidence and leave permanent changes for later analysis.
9. Deliver proposed coverage, gaps, dashboards, alerts, runbooks, costs and a validation plan.
