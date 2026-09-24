---
name: doc-review
description: Use when the user asks to check a document against a checklist.
---

## Purpose
This skill checks a document against the checklist in checklist.md and reports the result for each item.

## Rules
1. Check if the document states its purpose in the first paragraph or intro (checklist item 1). Say pass, fail, or unverifiable.
2. Check if the document uses active instead of passive voice, and full sentences instead of sentence fragments (item 2). Say pass, fail, or unverifiable.
3. Check if the document has headings for every section (item 3). Say pass, fail, or unverifiable.
4. Check if the document uses the correct developer or user-facing voice for its audience (item 4). Say pass, fail, or unverifiable.
5. Check if links and code examples work (item 5). Say pass, fail, or unverifiable.
6. Check if the document's format is consistent in terminology, code block style, and headings (item 6). Say pass, fail, or unverifiable.
7. When a checklist rule doesn't apply, for example when the document has no links, no code samples, or sections that need headings, say so and mark it unverifiable. Do not mark the item as fail.
8. Follow the shared rules in shared/house-style.md.
9. When the input is missing, unclear, or out of scope, follow the doc-review section of shared/hard-surfaces.md.
