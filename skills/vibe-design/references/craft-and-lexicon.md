# Craft and Actionable Taste

## Contents

- Translating taste into rules
- Anti-generic patterns
- Twelve craft lenses
- Visual-direction template

## Translating taste into rules

Do not leave aesthetic direction as adjectives. Translate each desired quality into:

1. **Intent**: what the quality should help the user feel or do.
2. **Observable properties**: hierarchy, density, type scale, color roles, geometry, material, imagery, motion.
3. **Constraints**: what must remain rare, fixed, or forbidden.
4. **Acceptance**: what evidence shows the quality is present.

Example:

| Vague word | Executable translation |
| --- | --- |
| restrained | one dominant emphasis per region; low-chroma surfaces; effects reserved for state or depth; no competing gradients |
| premium | precise type hierarchy, deliberate whitespace, limited materials, consistent imagery, no ornamental clutter |
| professional | domain-correct language, dense but scannable structure, predictable controls, visible provenance and status |
| lively | varied rhythm, purposeful accent, responsive feedback, brief stateful motion; never perpetual bounce |
| trustworthy | explicit source/time range, uncertainty and permission boundaries, reversible actions, stable visual grammar |

## Anti-generic patterns

Treat these as warnings unless the product context explicitly justifies them:

- purple-to-blue gradient as default brand expression;
- every section rendered as an equal white rounded card;
- glass blur applied to ordinary containers;
- uppercase micro-labels on every module;
- emoji used as product iconography;
- excessive pill shapes and fully rounded controls;
- large decorative hero copy that obstructs product information;
- random hardcoded colors outside the token system;
- western-first type stacks that produce weak Chinese rhythm;
- bounce, elastic, parallax, or shimmer without an information purpose;
- charts whose color distinguishes series but communicates no meaning;
- visual completeness that hides missing error, permission, or recovery states.

The correction is not “make it plain.” Replace decoration with hierarchy, semantic contrast, product evidence, and purposeful rhythm.

## Twelve craft lenses

### 1. Typography

- Choose language-appropriate type stacks.
- Build hierarchy with size, weight, line height, measure, and spacing before color.
- Keep body copy comfortably readable and labels concise.
- Align numeric formats and units in data-heavy interfaces.
- Prevent truncation from removing the information needed to decide.

### 2. Color

- Assign colors to semantic roles rather than local decoration.
- Keep brand emphasis scarce enough to remain meaningful.
- Use status color consistently and pair it with text/icon cues.
- Check contrast in real component states, not only token swatches.
- Ensure charts remain interpretable without relying on hue alone.

### 3. Iconography

- Use a coherent family, stroke weight, corner logic, and optical size.
- Prefer familiar symbols for familiar actions.
- Pair ambiguous icons with labels or tooltips.
- Do not substitute emoji for system icons.

### 4. Layout

- Make the primary task visually and spatially dominant.
- Use alignment and spacing systems to reveal grouping.
- Let density follow the task: operational consoles can be compact; narrative pages need breathing room.
- Avoid card walls by varying containment according to hierarchy.
- Define overflow and responsive changes explicitly.

### 5. Interaction

- Make affordances and state transitions visible.
- Preserve context across selection, details, and action feedback.
- Confirm consequential actions with specific impact language.
- Support cancel, undo, retry, and recovery where appropriate.
- Prevent dead ends and disconnected controls.

### 6. Motion

- Give every animation a stated purpose: orientation, causality, continuity, feedback, or attention.
- Prefer transform and opacity for smooth UI motion.
- Keep routine UI transitions brief; avoid bounce and overshoot by default.
- Respect reduced-motion settings.
- Do not animate keyboard-triggered actions unnecessarily.

### 7. Accessibility

- Preserve visible keyboard focus.
- Give interactive elements accessible names.
- Maintain usable target size and logical tab order.
- Do not encode meaning through color, motion, or position alone.
- Make loading announcements and errors perceivable and actionable.

### 8. Information architecture

- Group by user decisions and task sequence, not internal organization.
- Keep navigation labels mutually distinct.
- Put frequent and consequential actions where users can predict them.
- Use progressive disclosure for secondary detail, not missing essentials.
- Support scanning with meaningful headings and summary-first structure.

### 9. Copywriting

- Use the user's domain language and concrete verbs.
- State outcome and consequence, especially for risk and confirmation.
- Avoid generic AI filler, inflated claims, and unexplained jargon.
- Make errors explain what happened, what was preserved, and what to do next.
- Mark generated or uncertain information when trust depends on it.

### 10. Tools and system use

- Reuse existing tokens, components, templates, and accessibility behavior.
- Inspect the actual system before inventing a local replacement.
- Record missing system capabilities as gaps.
- Use visual tools for exploration when complexity warrants them, then return decisions to the source of truth.

### 11. Analysis

- Identify the primary user decision and the evidence required for it.
- Separate facts, assumptions, model inference, and recommendation.
- Compare alternatives by task outcome, risk, and implementation fit.
- Evaluate on the actual artifact and observable behavior.

### 12. Components

- Choose by semantic role, not shape similarity.
- Define allowed states and compositions.
- Keep destructive, risky, and irreversible actions visually and behaviorally distinct.
- Avoid new one-off components when the library already expresses the meaning.
- Test components in loading, empty, disabled, error, selected, focus, and responsive states.

## Visual-direction template

```markdown
# Visual Direction

## Intent
- Desired qualities:
- User effect:
- Product/category fit:

## Hierarchy and density
- Primary attention:
- Density:
- Containment strategy:

## Typography
- Language priority:
- Type roles:
- Numeric/data treatment:

## Color and material
- Brand role:
- Semantic states:
- Surface strategy:
- Effects allowed only for:

## Geometry and imagery
- Radius/shape logic:
- Icon/illustration style:

## Motion
- Permitted purposes:
- Duration/easing policy:

## Anti-patterns
- Forbidden defaults:

## Acceptance evidence
- Screenshot checks:
- State checks:
- System/token checks:
```
