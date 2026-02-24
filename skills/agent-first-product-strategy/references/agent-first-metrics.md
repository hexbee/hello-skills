# Agent-First Metrics Reference

## Purpose

Use these metrics to measure product value when agents are key software users.

## Core Metrics

### 1) Outcome Cycle Time

- Definition: elapsed time from request accepted to usable result delivered.
- Formula: `result_delivery_timestamp - request_timestamp`.
- Why: captures productivity value directly.

### 2) Unit Outcome Cost

- Definition: average total cost per successful outcome.
- Formula: `(model_cost + infra_cost + support_cost) / successful_outcomes`.
- Why: avoids growth that scales losses.

### 3) First-Call Success Rate

- Definition: share of new integrations that succeed without support tickets.
- Formula: `first_attempt_successful_integrations / total_new_integrations`.
- Why: reflects API/docs quality for agent adoption.

### 4) Integration Lead Time

- Definition: time from first doc/API access to first production success.
- Formula: `first_production_success - first_access_time`.
- Why: measures discoverability and onboarding friction.

### 5) Agent Repeat-Call Ratio

- Definition: fraction of agents/services invoking again within window.
- Formula: `repeat_calling_integrations / active_integrations`.
- Why: proxy for durable utility.

### 6) Reliability SLO Pair

- Definition: API success rate + latency percentile.
- Formula: `success_rate` and `P95 latency`.
- Why: makes "agent will not replace you" operational.

## Guardrails

- Do not optimize one metric by breaking another.
- Pair speed metrics with quality metrics.
- Pair adoption metrics with unit economics.
- Segment by customer type (`agent-first`, `human+agent`, `human-only`) to avoid false conclusions.

## Suggested Dashboard

Track weekly:

- Outcome Cycle Time (P50/P95)
- Unit Outcome Cost
- First-Call Success Rate
- Integration Lead Time
- Agent Repeat-Call Ratio
- API Success Rate + P95 Latency
