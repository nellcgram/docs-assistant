# Example

## Rule 1
- Example: "Checked your already-read list before recommending, so you were not shown books you had already read."

## Rule 4
   - Technical example: A commit adding "a pre-run check against the already-read-books file" sounds like an internal implementation detail, but it changes which books the recommender shows; include it instead of skipping it.
   - Meta example: a commit described as "Removed agentic AI section from portfolio site" is a project meta-change that you can skip.

   ## Rule 9
   Examples:
   - Vague (fails): "Adjusted when the recommender asked which genre you were interested in, so it only asked while you were available to respond."
   - Specific (passes): "Adjusted when the recommender asked which genre you were interested in: defaulted to contemporary genre when you were not available, and told you it had defaulted."