# Dynamic Interaction Reference

## Contents

- Agent Experience Loop
- Fixed UI versus GenUI
- A2UI contract
- Transparency, trust, and control
- Common interface roles
- Review checklist

## Agent Experience Loop

Design for a continuous loop rather than a single prompt and response:

`express goal → complete context → collaborate during execution → present evidence → evaluate result → revise direction`

Agent experiences reduce the execution gap: users need not translate a goal into every system action. They increase the evaluation gap: users did not perform every step, so they need stronger evidence, control, and recovery.

Before designing the loop, answer:

- What goal is the user trying to achieve, beyond the literal wording?
- What context is known, missing, stale, or permission-constrained?
- What may run automatically, what needs confirmation, and what is prohibited?
- What level of process visibility supports the next decision?
- What evidence, citation, data provenance, or confidence signal supports trust?
- Can the user cancel, undo, correct, retry, or return to a prior state?

## Fixed UI versus GenUI

Keep stable structures fixed when users benefit from learned location and predictable behavior:

- durable navigation;
- settings and account management;
- repeated approval flows;
- stable dashboards and information architecture;
- high-frequency deterministic tasks.

Use GenUI when at least one material element varies with context:

- the task path;
- missing information;
- evidence or result structure;
- a decision point;
- the next available action;
- the amount of detail needed for judgment.

Do not generate UI merely because generation is possible. The dynamic portion should improve understanding or action over structured text or fixed UI.

## A2UI contract

Separate declaration from rendering.

The Agent may declare:

- intent and task status;
- domain data and provenance;
- content structure;
- available user actions;
- whether execution waits for the user;
- validation, timeout, risk, and confirmation needs.

The client must own:

- allowed component catalog;
- design tokens and themes;
- layout and responsive rules;
- accessibility and focus behavior;
- input validation and action dispatch;
- security constraints;
- loading, error, timeout, and unsupported fallbacks.

Example declaration shape:

```json
{
  "intent": "confirm",
  "status": "pending",
  "title": "Confirm the analysis scope",
  "context": {
    "object": "workspace-42",
    "time_range": "last 24 hours",
    "finding": "Three anomalies need prioritization"
  },
  "content": {
    "type": "options",
    "items": []
  },
  "actions": [
    { "id": "analyze_selected", "label": "Analyze selected", "primary": true }
  ],
  "behavior": {
    "requires_user_decision": true,
    "blocks_agent_execution": true
  }
}
```

Field names may change. Preserve the responsibility boundary.

## Transparency, trust, and control

Process transparency is not maximal trace exposure. Reveal information according to task phase, risk, and decision need:

1. Show the current objective and status by default.
2. Summarize completed and pending work.
3. Surface assumptions, uncertainty, permissions, and material risks before commitment.
4. Attach evidence and provenance to consequential findings.
5. Put low-level logs and traces behind progressive disclosure.
6. Offer cancellation or correction while a reversible action is running.

For high-risk or irreversible actions:

- describe the consequence, not merely “Are you sure?”;
- identify affected objects and scope;
- require explicit confirmation;
- show the resulting state;
- provide rollback when technically possible;
- record the action when the domain requires auditability.

## Common interface roles

### Intent entry

Use an omnibox-style entry to combine natural language with objects, files, time range, knowledge sources, history, and permissions. The output should be structured task context, not only a chat message.

### Process collaboration

Use controlled cards or embedded forms for clarification, option comparison, authorization, risk confirmation, and mid-task correction. Return the user's action to Agent context as structured data.

### Result artifact

Use a durable generated report when the result is complex, shareable, revisitable, or action-oriented. It should expose:

- key outcomes;
- risks or structural findings;
- supporting evidence and provenance;
- recommended actions and follow-up state.

The report may vary in structure, but bind required data, evidence, risk, and action sections to controlled schemas and components.

## Review checklist

- Does the experience start from the user's goal rather than the product's menu structure?
- Is missing context requested at the right time?
- Are automatic, confirm-first, and prohibited actions explicit?
- Does every waiting state explain what is happening and what the user can do?
- Are consequential claims supported by evidence or uncertainty?
- Do dynamic elements use controlled components and safe fallbacks?
- Can the user intervene, revise, retry, or recover?
- Does the result lead to a meaningful next action?
- Are stable structures kept predictable rather than unnecessarily regenerated?
