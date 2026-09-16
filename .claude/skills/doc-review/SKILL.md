   ---
   name: doc-review
   description: Use when the user asks to check a documentation page against a checklist.
   ---

   ## Rules

1. Make tone of doc review user-facing, active voice, and full sentences; include what is being checked and why it matters.
2. List doc review entries in the same order as the input commits.
3. When a doc's line is given, try to check the actual documentation. If it disagrees with the provided description, don't silently pick one. Flag the discrepancy back to the user rather than guessing which is correct. Only check the repo if it is known in context; do not search the filesystem or guess at repo locations. If not immediately accessible, mark unverifiable and still write or skip the entry using the description given. Do not stop the response to ask which reading is correct.
4. Do not use internal file names (for example skill, rubric, eval, findings) in doc review.
5. Do not stop to ask the user to disambiguate documentation before finishing the response; decide using the rules above. Pick the reading better supported by the wording, write or skip accordingly, and flag the uncertainty in one clause if it matters. Don't ask which reading is correct. When a description could mean either the feature itself or its portfolio/project-level presence with no stronger signal, default to skip.