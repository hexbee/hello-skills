---
name: url-to-markdown
description: Convert a public webpage URL into Markdown using markdown.new and save it as a reusable `.md` file with the bundled script. Use this whenever the user wants to turn a public webpage, article, documentation page, blog post, release note, or reference URL into Markdown for reading, archiving, summarizing, extraction, RAG prep, or downstream agent reuse, even if they do not explicitly mention markdown, markdown.new, or saving a file.
---

# URL To Markdown

## Overview

Use this skill to fetch a public URL, convert it to Markdown through `https://markdown.new/`, and save the result as a timestamped Markdown file for later agent use.

This skill is execution-oriented. Prefer running the bundled script instead of manually recreating the workflow.

## When To Use

Use this skill when the user asks for any of the following:

- convert a URL or webpage to Markdown
- save an article, doc page, or blog post as `.md`
- ingest a public webpage for later summarization or extraction
- preserve page content in a machine-friendly text format
- pull a documentation page into a local Markdown file

Do not use this skill for:

- private pages that require browser login
- sites the user is not authorized to access
- tasks that require full site crawling rather than a single page fetch

## Inputs

Decide these inputs before running the script:

- `url`: required; must be a public URL
- `method`: optional; one of `auto`, `ai`, `browser`; default `auto`
- `retain_images`: optional; default `false`
- `transport`: optional; one of `auto`, `get`, `post`; default `auto`
- `timeout`: optional; default `30`
- `output`: optional; preferred for agent workflows

If the user does not specify these options, keep the defaults.

## Run The Script

From the skill directory, run:

```bash
python scripts/url_to_md.py "<url>" --output "<output_path>"
```

Common variants:

```bash
python scripts/url_to_md.py "<url>" --output "outputs/page.md"
python scripts/url_to_md.py "<url>" --method browser --retain-images --output "outputs/page.md"
python scripts/url_to_md.py "<url>" --transport post --timeout 45 --output "outputs/page.md"
```

Behavior notes:

- If `--output` is a filename, the script appends a timestamp before the extension.
- If `--output` is a directory, the script creates a slug-based filename with a timestamp.
- If `--output` is omitted, the Markdown is printed to stdout. Use this only when the user clearly wants inline content instead of a saved file.

## Required Output Behavior

Prefer producing both:

1. A saved Markdown file.
2. A short conversational summary.

The summary should include:

- source URL
- whether the conversion succeeded
- saved file path, if a file was written
- key options used if non-default: `method`, `retain_images`, `transport`, `timeout`

## Summary Template

Use this structure:

```text
Source URL: <url>
Status: success
Saved Markdown: <path>
Options: method=<value>, retain_images=<value>, transport=<value>, timeout=<value>
```

If defaults were used, keep `Options` brief.

## Error Handling

If the script fails:

- say that URL-to-Markdown conversion failed
- include the main error briefly
- do not invent page content
- mention likely cause when obvious: network issue, timeout, rate limit, unsupported page access

If the service returns rate limiting, report that directly and avoid pretending a retry succeeded.

## Notes

- Prefer saved Markdown over raw stdout because agents can reuse local files more reliably.
- The bundled script uses only the Python standard library.
- The script supports both importable usage and CLI execution, but this skill should normally use the CLI path.
