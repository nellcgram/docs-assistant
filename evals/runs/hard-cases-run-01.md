# Hard Cases: 10 Inputs

Each input is scored against the matching bullet in `shared/hard-surfaces.md`. "Skill fired" is a routing note and is not scored. "Did the response do it?" checks the response against every part of the chosen bullet, and the result follows from it.

## doc-review skill tricky input
1. review doc with commits
   - Skill fired: doc-review
   - Applicable bullet: Out of scope, since commits aren't a doc
   - Did the response do it? No: it ran the doc-review checklist on the commits instead of saying the skill doesn't apply and naming the task it does handle
   - Result: fail

2. make doc shorter
   - Skill fired: none
   - Applicable bullet: Out of scope, since shortening is editing, not reviewing
   - Did the response do it? No: it followed the prompt and shortened the doc without saying the skill doesn't apply
   - Result: fail

3. fill in doc details
   - Skill fired: none
   - Applicable bullet: Unclear
   - Did the response do it? Yes: it read hard-cases-10.md, saw the tricky inputs, and asked what I actually wanted, including the option of running the doc-review checklist
   - Result: pass

4. review this Japanese doc
   - Skill fired: none
   - Applicable bullet: Gap: hard-surfaces.md has no bullet for a wrong language, so scored against Out of scope (closest)
   - Did the response do it? No: it followed the prompt and corrected the doc without saying the skill doesn't apply
   - Result: fail

5. go over
   - Skill fired: none
   - Applicable bullet: Unclear
   - Did the response do it? No: it didn't ask what I wanted and went ahead and corrected the doc
   - Result: fail

**Subtotal:** 1 of 5 correct

## release-notes skill tricky input
1. do the notes thing
   - Skill fired: release-notes
   - Applicable bullet: Unclear
   - Did the response do it? Yes
   - Result: pass
   - Unscored note: it could not find house-style.md because the rule gives no path and the file is in shared/, not the skills folder

2. use doc-review to turn commits into release notes
   - Skill fired: release-notes
   - Applicable bullet: None fits exactly. The wrong skill was named, which hard-surfaces.md doesn't cover (a gap)
   - Did the response do it? Yes: it corrected the input and used the release-notes skill instead
   - Result: pass

3. make commits better
   - Skill fired: none
   - Applicable bullet: Out of scope
   - Did the response do it? No: it didn't say the skill doesn't apply and rewrote the git commits
   - Result: fail

4. review commits against checklist
   - Skill fired: doc-review (and house-style.md)
   - Applicable bullet: Unclear
   - Did the response do it? No: it guessed the task and used doc-review instead of asking what I wanted
   - Result: fail

5. commit notes
   - Skill fired: release-notes
   - Applicable bullet: Unclear ("commit notes" could mean release notes or a note on a git commit)
   - Did the response do it? No: it ran the release-notes skill and answered without asking what "commit notes" meant
   - Result: fail

**Subtotal:** 2 of 5 correct

**TOTAL:** 3 of 10 correct
