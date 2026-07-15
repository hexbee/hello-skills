# Design Engineering Reference

## Contents

- Design I/O
- Six declarations
- Execution contracts
- End-to-end workflow
- Artifact templates
- Failure routing

## Design I/O

Treat interface generation as an inspectable chain:

`brief → understand/plan → structure → fill → refine → evaluate → deliver or return`

Three mechanisms keep the chain controlled:

1. The main chain turns intent into an artifact through explicit stages.
2. Tokens and system rules apply throughout, not only during visual polish.
3. Critique returns to the stage and declaration that caused the failure.

Upstream errors compound. Resolve product intent, boundaries, and structure before polishing components.

## Six declarations

### `spec.md`: functional truth

Define:

1. Position and intent: one-sentence definition, users, scenarios, non-goals, automation boundary.
2. Information architecture: regions, responsibilities, growth/overflow rules.
3. Core flows: states, main path, branch paths, transitions.
4. Component behavior: actions and default/hover/loading/disabled/error/selected states.
5. Edge conditions: empty, loading, error, permission, timeout, partial success, recovery.
6. Acceptance: Given/When/Then scenarios and definition of done.

Do not put visual styling, component catalog rules, or execution instructions here.

### `domain.md`: business responsibility

Define only rules that are true because of the domain:

- canonical terms and entities;
- state and risk meanings;
- data provenance and time windows;
- permissions and role boundaries;
- destructive or irreversible actions;
- sensitive-data display, reveal, logging, and masking;
- compliance or trust requirements;
- safe defaults and escalation rules.

Example distinction: domain defines what “high risk” means; `design.md` defines which token represents it; `craft.md` checks whether emphasis is proportionate.

### `craft.md`: cross-domain execution quality

Cover observable rules for:

- typography and reading rhythm;
- hierarchy, density, geometry, and spacing;
- color and material restraint;
- data visualization clarity;
- loading, feedback, recovery, and state transition;
- motion purpose and duration;
- accessibility and input modality;
- known generic-generation anti-patterns.

Write rules as `observable symptom → required action → acceptance check`.

Useful loading policy when no product rule overrides it:

- under 300 ms: avoid visible loading feedback that flashes;
- 300 ms–2 s: preserve layout with a skeleton or local pending state;
- over 2 s: show progress context;
- over 10 s: show timeout guidance and a recovery action.

### `design.md`: visual source of truth

Organize the visual system in seven layers:

1. Intent: brand emotion, density, neutral temperature, language priority.
2. Roles: brand, primary action, link, surface, status, risk, chart, focus.
3. Values: color, type, spacing, radius, elevation, duration, easing, z-index.
4. Derivation: scales, hover/active/surface variants, density and theme transforms.
5. Component states: default, hover, pressed, selected, disabled, loading, error, focus, responsive behavior.
6. Graphics and data visuals: icons, illustrations, empty states, chart palettes and semantics.
7. Execution and gaps: token-first policy, fallback rules, gap logging, forbidden literals.

Never hide a missing token by inventing a local convention. Use an approved fallback and record the gap, or stop and request a system decision when the gap is material.

### `components`: product grammar

For each component, define:

- source: product library, third-party library, or domain-specific component;
- semantic role: status, risk, category, action, container, navigation, feedback;
- supported variants and states;
- allowed composition and forbidden substitutions;
- accessibility and behavior constraints.

Common distinctions:

| Pair | Distinction |
| --- | --- |
| Badge / Tag | Badge communicates attached status/count; Tag communicates category, selection, or removable metadata. |
| Dialog / Drawer | Dialog handles focused decisions; Drawer preserves surrounding context for denser secondary work. |
| Tabs / mode switch | Tabs move between peer views; a switch changes interpretation or mode. |
| Dropdown / Menu / Command | Dropdown selects a value; Menu offers actions; Command supports search-driven operation. |

Do not choose by appearance alone.

### `template`: structural starting point

Define:

- applicable scenario and primary task;
- shell, main region, side/context region, action region, status region;
- default information and control density;
- growth, overflow, and responsive behavior;
- required regions;
- forbidden use of sample/playground structures in production.

A template is a starting skeleton, not a screenshot to copy. Adapt content and density to the actual task without breaking its structural rationale.

## Execution contracts

### Skill contract

A useful design skill contains:

1. trigger conditions;
2. a decision process;
3. selective references for detail;
4. known failure patterns;
5. an explicit output and verification contract.

Its job is to schedule declarations, not invent a competing rule set.

### Evaluator contract

Convert declarations into checks. Every failed check must identify:

- evidence;
- user or business impact;
- owning declaration;
- next action;
- verification condition.

The evaluator protects the exit of the chain; it does not replace upstream specification.

## End-to-end workflow

1. Expand the brief into a six-layer spec.
2. Confirm visual direction early enough to prevent default styling from shaping the structure.
3. Select or create the information architecture based on attention priority.
4. Map domain semantics to the correct components.
5. Add edge states, feedback, recovery, motion, and accessibility.
6. Evaluate against the same declarations.
7. Route failures to the declaration that owns them; do not patch the entire screen indiscriminately.

## Artifact templates

### Compact `spec.md`

```markdown
# [Feature] Interaction Spec

## L1 Position and intent
- Definition:
- Users:
- Scenarios:
- Non-goals:
- Automation boundary: always / confirm / never

## L2 Information architecture
- Regions and responsibilities:
- Growth and overflow:

## L3 Flows
- Main path:
- Branch paths:
- State transitions:

## L4 Component behavior
| Component | Purpose | Actions | States |
| --- | --- | --- | --- |

## L5 Edge conditions
| Condition | User sees | Available action | Recovery |
| --- | --- | --- | --- |

## L6 Acceptance
- Given ..., when ..., then ...
```

### Compact `domain.md`

```markdown
# [Domain] Rules

## Canonical entities and terms
## State and risk semantics
## Data provenance and freshness
## Permissions and automation boundaries
## Destructive actions
## Sensitive data
## Trust and compliance
```

### Compact component record

```yaml
component: RiskBadge
source: product-library
semantic: domain risk level
allowed_values: [critical, high, medium, low, unknown]
visual_source: design.md
meaning_source: domain.md
forbidden_substitutions: [Tag]
states: [default, loading, unavailable]
```

### Compact return item

```yaml
problem: "Primary action has no visible pending or success state"
evidence: "Click test leaves the screen unchanged"
impact: "User cannot tell whether the task started"
owner: "spec.md L4/L5"
action: "Add pending, success, failure, and retry behavior"
verify: "Each transition is visible and the failure state is recoverable"
```

## Failure routing

| Symptom | Return to |
| --- | --- |
| Missing empty/error/permission/recovery state | `spec.md` |
| Wrong risk, data, permission, or domain semantics | `domain.md` |
| Generic AI styling, weak hierarchy, purposeless motion | `craft.md` |
| Hardcoded or inconsistent visual values | `design.md` |
| Component looks plausible but means the wrong thing | `components` |
| Page feels like the wrong product shape or card wall | `template` |
| Review cannot explain why something failed | evaluator contract |
