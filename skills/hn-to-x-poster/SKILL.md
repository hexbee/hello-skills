---
name: hn-to-x-poster
description: Use this when the user wants to review Hacker News top 30 stories, select software or AI related items, and automatically publish a short Chinese summary to x.com or Twitter from an already logged-in browser session.
---

# HN to X Poster

## Overview

Use this skill for a browser-driven workflow that reads the current Hacker News front page, filters the top 30 stories for software or AI relevance, compresses the signal into one short Chinese post, and publishes it to `x.com`.

This skill is for direct execution, not just drafting. Default behavior is to post automatically if `x.com` is already logged in. If posting is blocked, fall back to a ready-to-send Chinese draft and explain the blocker briefly.

## When To Use

Use this skill when the user asks for any combination of:

- Hacker News or HN top stories
- HN top 30, front page, or current HN software or AI items
- posting, tweeting, sending, or publishing the result to `x.com` or Twitter
- a Chinese summary of current HN software or AI topics that should be posted automatically

Do not use this skill when:

- the user only wants HN analysis without posting
- the user wants a multi-post thread
- the user wants deep article research instead of front-page signal extraction

## Required Tooling

Use `chrome-devtools` MCP for the browser workflow.

Do not rely on API access to Hacker News or X unless the user explicitly changes the method.

## Workflow

### 1. Open The Two Sites

- Open or switch to `https://news.ycombinator.com/`
- Open or switch to `https://x.com/`
- Confirm that X is logged in before attempting to post

If X is not logged in, stop automatic posting and return a Chinese draft the user can publish manually.

### 2. Read HN Top 30

- Read the current HN front page
- Capture the first 30 ranked stories only
- Use the front-page title and visible context as the default source of truth

Do not open every article by default. This skill is meant to summarize the HN front-page signal, not to perform full article research.

### 3. Filter For Software Or AI Relevance

Keep items that are clearly about:

- software engineering
- programming languages
- developer tools
- operating systems
- networking, infrastructure, databases, compilers, security, or systems work
- AI, LLMs, agents, model tooling, MCP, inference workflows, or AI product/platform shifts

Usually drop items that are mainly:

- general politics
- culture or biography
- pure science without a software or AI angle
- consumer oddities with no developer or AI relevance

If an item is borderline, prefer keeping it only when a technical audience would plausibly care.

### 4. Build The Post

Write one short Chinese post that:

- sounds natural on X
- highlights only the strongest 4 to 7 software or AI signals
- compresses repeated themes instead of listing everything
- ends with a light conclusion about the pattern when useful

Default style:

- concise
- readable by Chinese tech audiences
- no hashtags unless the user asks
- no thread unless the user asks
- no links unless the user asks

### 5. Enforce Length Before Posting

Before posting, make sure the text is short enough for a standard X post.

If it is too long:

- compress aggressively
- remove low-signal items first
- collapse repeated categories into one phrase
- keep the main pattern, not the full inventory

Prefer one compact paragraph over a long numbered list.

### 6. Post On X

Use the homepage inline composer:

- go to `https://x.com/home`
- confirm the inline composer is visible before typing
- enter the final Chinese text with keyboard-style input
- verify both of these before posting:
  - the post button is enabled
  - the character counter looks normal
- click `Post`

### 7. Verify Completion

After posting:

- go to the account profile or resulting post view
- confirm the new post appears as the latest visible post
- capture the post URL if available

Do not claim success unless the post is visibly present in the browser.

## Failure Handling

### X Not Logged In

Do not attempt login on the user's behalf unless they explicitly ask.

Return:

- a brief note that automatic posting is blocked because X is not logged in
- the final Chinese draft

### Composer Does Not Recognize Input

If text appears in the textbox but the post button stays disabled:

- treat this as an input-recognition failure, not a writing failure
- clear the composer, then re-enter the final text with keyboard-style input
- re-check both the post button and the character counter before posting

### Composer Counter Looks Wrong

If the text length is obviously short enough but X claims it is over limit or otherwise shows a broken counter:

- assume the composer state is corrupted
- refresh or reopen `https://x.com/home`
- re-enter the final text in the homepage inline composer
- do not keep retrying in the broken composer state

### Post Is Too Long

Shorten and retry. Do not stop at the first over-limit failure.

### Posting Still Fails

Return:

- the final Chinese text
- the exact blocker, such as disabled post button or missing login state

## Output Expectations

When successful, give a short result that includes:

- that HN top 30 was reviewed
- that software or AI items were selected
- that the Chinese post was published to X
- the X post URL

When blocked, give:

- a brief reason
- the final Chinese draft

## Operating Notes

- Treat HN as a front-page signal source, not a complete market map
- Prefer a small set of strong signals over exhaustive coverage
- Favor execution reliability over perfect prose
- If the user asks for a draft only, do not auto-post
- On X, use the homepage inline composer as the standard posting path
- Do not trust visible text alone; the post button state and counter state are the real readiness checks
- After clicking post, verify on profile that the new post is actually published before reporting success
