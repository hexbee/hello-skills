---
name: resume-builder
description: Generate and revise job resumes from raw notes, existing resumes, career histories, or profile snippets. Use when Codex needs to create, redesign, tighten, or review a resume/CV, especially for Chinese or English A4 resumes, PDF/HTML output, first-screen hiring signal, skill ordering, pagination balance, header/contact layout, or reframing an engineering background for AI-focused roles.
---

# Resume Builder

Build resumes for hiring, not for decoration. Prioritize first-screen signal, readable pagination, and recruiter-friendly structure over template fidelity.

## Workflow

1. Classify the input.
2. Lock the resume decisions before editing.
3. Rewrite the content to fit the target role.
4. Lay out the resume with print-first rules.
5. Verify first screen, pagination, and PDF output.

## Step 1: Classify The Input

Choose one path before touching layout:

- `structured resume`: the user already has sections, bullets, and dates.
- `partial resume`: the user has section fragments or an outdated resume.
- `raw career notes`: the user has experience notes, a LinkedIn-style summary, or scattered facts.

For `raw career notes`, extract:

- role titles
- company names
- dates
- technologies
- measurable results
- target job direction

If key facts are missing, ask once. Do not silently invent metrics, dates, team sizes, or ownership.

## Step 2: Lock The Decisions

Before editing, decide these five items explicitly:

1. `target role`: what job should the resume optimize for?
2. `language`: Chinese or English?
3. `print style`: default to pure white, print-safe A4.
4. `first-screen order`: which sections must appear before the reader scrolls?
5. `pagination anchor`: where should page 2 begin?

Default ordering for most resumes:

1. header
2. metrics or summary chips
3. personal summary
4. core skills
5. evolution / highlights / key projects
6. experience / education / certificates

Do not leave these decisions implicit. Most layout churn comes from skipping this step.

## Step 3: Rewrite The Content

Write for recruiter scanning speed.

- Lead with the target role and the strongest relevant signal.
- Use data and scope instead of adjectives.
- Convert generic duties into `context -> action -> result`.
- Remove hedge language such as `也可关注`, `也可以考虑`, or long fallback job lists unless the user explicitly wants broad positioning.
- Keep the summary short enough to read in one pass.

When the user is pivoting roles, rewrite the story around transferable value rather than chronology. For technical-to-AI or adjacent-domain pivots, read [references/ai-transition-resume.md](references/ai-transition-resume.md).

For Chinese resumes, read [references/cn-resume.md](references/cn-resume.md).

## Step 4: Apply Print-First Layout Rules

Treat PDF as the source of truth. HTML preview is secondary.

- Separate `screen preview` styling from `print/PDF` styling.
- Default the resume body background to pure white.
- Use screen-only shadow, centered paper, or page labels inside `@media screen` only.
- Do not let preview polish distort PDF judgment.

Header rules:

- Prefer two-line contact layout when the title and contact info would otherwise mix awkwardly.
- Keep the identity block stable: avatar optional, name prominent, title separate from contact metadata.
- Birth year/month may be preferable to computed age when the user wants a more formal presentation.

Section rules:

- Move `core skills` earlier when the target role is skills-driven.
- Keep time ranges on one line.
- Keep metrics values on one line.
- Split `certificates` and `job target` unless there is a strong reason to merge them.

## Step 5: Control Pagination

Do not hard-code page 2 too early.

- First, let page 1 absorb natural content.
- Only force a page break when page 2 needs a clean anchor and page 1 is already balanced.
- Avoid pushing an entire section to page 2 if page 1 still has obvious unused space.
- Let lower-priority project blocks flow across pages when that creates better balance.
- Protect only genuinely fragile blocks with `break-inside: avoid`.

The goal is not mathematical symmetry. The goal is to avoid:

- page 1 with a large empty tail
- page 2 starting too high or too cramped
- dense text above and wasted whitespace below

## Step 6: Verify Before Hand-Off

Always do one explicit visual QA pass. Read [references/review-checklist.md](references/review-checklist.md).

Minimum checks:

- Does the first screen show the target role and strongest differentiators?
- Are `core skills` visible early enough?
- Are there odd line breaks in dates, metrics, or left-column labels?
- Is the top margin formal enough for print?
- Is whitespace balanced across page 1 and page 2?
- Does the PDF still fit the expected page count?

If HTML and PDF disagree, trust PDF for content and pagination, then patch screen preview separately.
