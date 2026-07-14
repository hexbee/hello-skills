# GPT-5.6 Prompting Guidance

## Contents

- Simplify first
- Define outcomes and stopping conditions
- Control tone and response length
- Set autonomy and approval boundaries
- Route tools deliberately
- Use Programmatic Tool Calling selectively
- Ground claims and budget retrieval
- Manage long-running workflows
- Tune reasoning effort with evals
- Handle frontend and visual work
- Validate before finishing
- Migrate prompts incrementally

## Simplify first

Start from a prompt and tool set that already works. Remove one group at a time, then rerun the same representative evals.

Trim repeated rules, redundant style or process instructions, examples that do not change behavior, scaffolding the model already handles reliably, and unrelated tools. Keep the user-visible outcome, success criteria, stopping conditions, safety and permission boundaries, evidence rules, required tool routing, output contract, and validation requirements.

Check the remaining instructions for contradictions. Prefer one clear rule over several overlapping versions.

## Define outcomes and stopping conditions

Describe what successful completion looks like and let the model select an efficient path. Preserve explicit user values. When a value is implicit, provide decision criteria instead of brittle keyword maps or universal defaults.

Define when to answer, retrieve again, retry, fall back, ask for missing information, abstain, or stop. Minimize loops only after correctness, required evidence, calculations, citations, and validation are satisfied.

## Control tone and response length

Use runtime verbosity controls for the default level of detail when available. Use the prompt for task-specific length, structure, and required content.

Describe concrete writing behavior instead of broad labels. Separate personality—tone, warmth, directness, formality, humor, empathy—from collaboration style—initiative, assumptions, questions, tradeoffs, checking, and uncertainty.

For shorter answers, state what must remain: conclusions, evidence, material caveats, decisions, and next actions. Trim introductions, repetition, generic reassurance, and optional background first.

For editing and rewriting, preserve the requested artifact, length, structure, genre, and factual claims before improving clarity and flow.

## Set autonomy and approval boundaries

Define what each request type authorizes. Reading, diagnosis, planning, local implementation, external writes, destructive actions, purchases, and scope expansion need different boundaries.

Allow safe, in-scope local actions without unnecessary pauses. Require confirmation for external, destructive, costly, or materially scope-expanding actions. Keep the policy in one place and state each rule once.

For long tasks, name the current layer: research, design, implementation, review, or external coordination.

## Route tools deliberately

Expose only relevant tools. Describe what each tool does, when to use it, important return fields, and failure behavior.

Require prerequisite discovery, retrieval, and validation when correctness depends on them. Parallelize independent reads; keep dependent work sequential; synthesize retrieved results before acting.

When results are empty, partial, or suspiciously narrow, try one or two meaningful fallbacks before concluding that nothing exists.

## Use Programmatic Tool Calling selectively

Use Programmatic Tool Calling for bounded deterministic reduction: filtering, joining, sorting, ranking, deduplication, aggregation, batching, repeated validation, or compacting large structured results.

Prefer direct calls when one call is enough, intermediate results are small, semantic judgment changes the next action, approval is required, citations or native artifacts must be preserved, or final validation needs direct inspection.

When using Programmatic Tool Calling, define the bounded stage, eligible tools, compact output schema, retry limit, stop condition, and handoff back to direct judgment. Validate both program output and the final assistant response.

## Ground claims and budget retrieval

Define which claims need citations, what evidence is sufficient, and what to do when evidence is missing. Do not turn absence of evidence into a factual negative.

For ordinary questions, start with one broad, discriminative search. Retrieve again only for a missing required fact, exhaustive coverage, a named artifact, or an important unsupported claim. Do not retrieve again merely to improve prose or add nonessential examples.

Cite only retrieved sources, attach citations to supported claims, label inference, report source conflicts, and narrow the answer instead of guessing.

For creative drafting, do not invent names, metrics, dates, roadmap status, customer outcomes, or product capabilities.

## Manage long-running workflows

For multi-step tool work, give a short preamble before the first call and sparse outcome-based updates at major phase changes. Avoid narrating routine calls.

Preserve assistant phase values when replaying history. Compact after meaningful milestones, keep prompts functionally consistent after compaction, and reuse persisted reasoning only while objectives and assumptions remain stable. Keep reusable prompt prefixes stable when prompt caching matters.

## Tune reasoning effort with evals

Establish a baseline at the current reasoning setting. Test the same setting and one level lower on representative tasks. Increase effort only when evals show a meaningful gain.

Before raising reasoning effort, check for missing success criteria, dependency rules, tool-routing rules, or verification loops.

## Handle frontend and visual work

Provide product context, preserve the existing design system, and name important states and constraints. For incremental frontend work, inspect existing tokens and patterns, avoid unrequested features or decoration, preserve responsive behavior, and render the result before finalizing.

Choose image detail intentionally for vision, computer-use, localization, or OCR tasks. Use original detail when large, dense, or coordinate-sensitive input justifies the extra cost and latency.

## Validate before finishing

Give the model access to relevant validation and state what matters. For code, run targeted tests, type or lint checks, affected builds, and a minimal smoke test as appropriate. If a check cannot run, explain why and name the next best check.

For visual artifacts, render and inspect layout, clipping, spacing, missing content, and consistency. For implementation plans, include requirements, named files and resources, data flow or state transitions, validation, failure behavior, privacy or security concerns, and material open questions.

## Migrate prompts incrementally

When moving to GPT-5.6:

1. Switch the model while preserving the current reasoning effort.
2. Run representative evals before changing the prompt.
3. Remove obsolete scaffolding, repetition, and irrelevant tools.
4. Add only the smallest targeted instruction that fixes a measured regression.
5. Rerun the same cases after every change.

Do not rewrite a working prompt stack all at once. Use real traces to identify the failure mode, make a surgical change, and rerun the same evaluations so the cause remains attributable.
