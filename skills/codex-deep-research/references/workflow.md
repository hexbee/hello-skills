# Workflow

Use this staged process for deep-research tasks.

## 1. Classify the request

Confirm the task is actually research-shaped:

- multiple sources likely needed
- current information matters
- the user wants a recommendation, comparison, or evidence-backed judgment
- the downside of missing an important fact is non-trivial

If the request is too vague, ask one narrow clarifying question before starting broad research.

## 2. Rewrite the brief

Create a compact internal brief using [../assets/brief-template.md](../assets/brief-template.md).

The goal is not to restate the user request in fancy language. The goal is to make the research executable:

- what exact question is being answered
- why the user cares
- what is in and out of scope
- what dimensions matter
- what kind of output will best help the user

## 3. Run an initial web sweep

Do a quick first pass before deciding whether to spawn sub-agents. This pass should:

- identify the main entities, products, or topics involved
- find the strongest likely source types
- reveal obvious time sensitivity
- surface whether the space is broad or narrow

The initial sweep is for orientation, not for writing the final report.

## 4. Check complexity

Stay single-agent when:

- the task is narrow
- one strong search path gives sufficient coverage
- the decision surface is simple

Escalate to multi-agent when:

- the work naturally decomposes into independent sub-questions
- parallel search will reduce the risk of blind spots
- the task includes both factual collection and interpretive evaluation
- the stakes justify stronger coverage

Prefer two to four sub-agents. More than that often increases duplication and coordination cost.

## 5. Delegate cleanly

Use [../assets/subagent-task-template.md](../assets/subagent-task-template.md) when delegating.

Good role splits:

- primary and official sources
- recent developments and time-sensitive changes
- alternatives and competitor comparison
- risks, edge cases, and counter-evidence

Each sub-agent should own one clearly bounded question and return concise, source-backed findings rather than a full final answer.

## 6. Synthesize

The main agent owns final synthesis. It should:

- compare overlapping findings
- remove duplication
- spot contradictions
- explain which evidence is strongest
- carry uncertainty forward honestly
- turn raw evidence into user-relevant conclusions

Never outsource final judgment to the sub-agents.

## 7. Write the report

Use [../assets/report-template.md](../assets/report-template.md) as the default shape.

The report should feel like research:

- explain what was investigated
- show how conclusions were reached
- expose the evidence base
- note the main risks and unknowns
- end with a practical recommendation or next step when appropriate

## 8. Decide whether to persist

Default to in-session delivery. Save artifacts only if:

- the user asks
- the output is worth reusing
- auditability matters for follow-on work
