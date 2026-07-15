# Evidence-Based Design Evaluation

## Contents

- Evaluation sequence
- Page shapes and weights
- Six dimensions
- Evidence model
- Scoring and blockers
- Review modes and stopping
- Report contract

## Evaluation sequence

Use an isolated generator/evaluator loop:

1. The generator produces an artifact from the brief and declarations.
2. The evaluator receives the artifact, task, rubric, and observable runtime evidence.
3. The evaluator records subchecks, evidence, deductions, and recommendations.
4. The runtime calculates scores and applies blockers and release policy.
5. Passing artifacts proceed; failing artifacts receive a prioritized return plan.
6. Offline calibration uses real cases to update criteria and thresholds.

Evaluate the delivered artifact, not hidden planning, creator explanations, or future promises.

## Page shapes and weights

Classify the page before scoring it:

| Shape | Primary outcome | Common failure |
| --- | --- | --- |
| Brand landing | Turn attention into interest and trust | generic template, weak memory, unclear promise |
| Product console | Complete an operational task safely | unclear task, dead end, disconnected state |
| Conversational interface | Ask, judge, act, and recover through dialogue | unclear turn state, unsupported answer, no recovery |
| Data dashboard | Judge status and diagnose change | decorative charts, weak hierarchy, missing provenance |
| Content/documentation | Find, understand, and apply knowledge | poor scanability, weak structure, unsupported claims |

Use these default weights when no product-specific rubric exists:

| Dimension | Landing | Console | Conversation | Dashboard | Content |
| --- | ---: | ---: | ---: | ---: | ---: |
| Visual & Brand Expression | 25 | 8 | 8 | 8 | 8 |
| Product Intent | 20 | 22 | 18 | 18 | 18 |
| Information Architecture | 18 | 22 | 16 | 24 | 28 |
| System Craft | 15 | 14 | 12 | 16 | 14 |
| Trust & Domain Fit | 12 | 18 | 22 | 22 | 22 |
| Interaction Readiness | 10 | 16 | 24 | 12 | 10 |

Weights express different priorities, not different definitions of quality.

## Six dimensions

### Product Intent

Check value proposition, target user, primary task, content voice, first-screen focus, and alignment between calls to action and the actual outcome.

### Trust & Domain Fit

Check canonical terminology, data source and freshness, risk meaning, permissions, compliance, uncertainty, AI confidence, evidence, and safe treatment of sensitive or irreversible actions.

### Information Architecture

Check hierarchy, grouping, order, navigation, density, rhythm, scan path, progressive disclosure, and whether the structure supports decisions.

### Interaction Readiness

Check affordance, feedback, main-path completion, loading/error/empty/permission states, recovery, keyboard behavior, focus, and connection between controls, selected objects, details, and results.

### System Craft

Check typography, spacing, radius, elevation, component consistency, token use, responsive behavior, visual states, motion restraint, performance-visible defects, and desktop composition.

### Visual & Brand Expression

Check color, typography weight, imagery, material, motion, distinctiveness, and fit with the brand and product category. Distinctive does not mean ornamental.

## Evidence model

Collect the strongest evidence available:

| Evidence | What it establishes |
| --- | --- |
| DOM/CSS QA | overflow, clipping, contrast, small targets, missing names, broken images |
| Page profile | sections, headlines, CTAs, navigation, real/placeholder paths, clickable targets |
| Click smoke | console/page errors, broken transitions, dialog state, no-feedback actions |
| Screenshots | actual readability, hierarchy, composition, brand fit, visual state |
| Task/data inspection | domain meaning, provenance, workflow correctness, content truth |

DOM completeness does not prove visual success. When DOM claims and the visible result conflict, prioritize what users actually see.

Browser QA is a fact layer, not a design score. A technically healthy page can still be generic or strategically wrong.

## Scoring and blockers

Break each dimension into auditable subchecks. Score each:

- `2 / pass`: substantially satisfies the criterion;
- `1 / partial`: weakness materially affects quality;
- `0 / fail`: does not satisfy it;
- `0 / critical_fail`: failure must also enter blocker evaluation.

Calculate:

```text
dimension_score = sum(subcheck.score) / sum(subcheck.max_score) * 10
final_score = weighted sum of dimension scores
```

Do not invent a top-level score first and rationalize it afterward.

Potential blockers include:

- unclear primary task;
- critical rendering or readability failure;
- wrong domain logic;
- broken key task path or operational dead end;
- disconnected controls and states;
- broken conversational turn or recovery flow;
- untrustworthy AI response or missing evidence;
- brand/category mismatch;
- placeholder-dominated conversion path;
- generic template output;
- inconsistent design system;
- missing screenshot review or auditable subchecks.

A blocker can fail the delivery gate even when the average score exceeds the threshold.

## Review modes and stopping

### Direction draft

Suggested threshold: 7.5. Judge direction, intent, architecture, brand expression, and craft. Backend and placeholder integration issues may remain advisory when they do not invalidate the concept.

### Prototype

Suggested threshold: 8.0. The primary path must show visible simulated states even without a real backend. Interaction failures affect pass/fail.

### Release gate

Suggested threshold: 8.0. Require production paths, navigation, data, permissions, and key states. Placeholder paths may block release.

Stop iteration when:

- threshold is met and no blocker remains;
- the configured maximum round is reached;
- multiple rounds show negligible improvement;
- revisions regress materially, in which case return to the best prior version.

More rounds do not guarantee improvement.

## Report contract

Lead with the decision:

1. pass/return, score, threshold, mode, and reason;
2. blockers;
3. six dimension scores;
4. evidence-backed subchecks;
5. a small prioritized return plan.

Each return item should contain:

```yaml
priority: 1
finding: "What failed"
evidence: "Where and how it was observed"
impact: "Why it matters to the task, trust, or delivery"
dimension: "Interaction Readiness"
owner: "spec.md L4/L5"
instruction: "Concrete next-round change"
verify: "Observable condition for completion"
```

Avoid wish lists such as “improve the visuals and enrich the interaction.” Compress the critique to the few changes most likely to remove blockers and raise the weakest high-weight dimensions.

## Calibration

Maintain standards outside runtime with:

- known-good cases to prevent over-strictness;
- known-bad cases to test blockers;
- mixed cases with strong visuals but broken tasks;
- threshold cases to inspect score stability;
- category cases to prevent one visual taste from dominating all products.

For each rubric change, ask whether it reduces false passes, creates false failures, unfairly penalizes a category, or merely overfits one example.
