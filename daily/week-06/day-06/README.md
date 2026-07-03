# Week 06 · Day 06 — Reusable prompt library + brief practice + weekly review

**Estimated time:** ~4 hrs (lighter consolidation + weekly review day)
**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Refactor your best prompts into a small reusable, versioned prompt library.
- [ ] Practice writing a crisp project brief from scratch.
- [ ] Close out the week with a review and updated progress.

## Learn (with resources)
- **Anthropic docs** — Prompt engineering guide overview: skim it once more now that you've built things, noting techniques you didn't use yet: https://docs.anthropic.com
- **DeepLearning.AI short course** — revisit any "ChatGPT Prompt Engineering for Developers" lesson that clicked less the first time.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-prompt-library`.
2. [ ] Create `projects/intermediate/prompt-library/prompts.py` (or a `prompts/` folder of `.txt`/`.md` templates) collecting your reusable prompts (extractor system prompt, chatbot persona, etc.) with:
   - Named constants or files, each with a short comment: purpose + expected inputs/outputs.
   - A tiny helper `fill(template, **kwargs)` that safely substitutes variables.
3. [ ] Write one `projects/intermediate/prompt-library/README.md` documenting how to reuse a prompt in a new script.
4. [ ] **Brief practice:** copy `templates/project-brief-template.md` into `projects/intermediate/prompt-library/next-project-brief.md` and draft a brief for an idea you'd like to build in Week 7 (a RAG doc Q&A over docs you care about).
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Weekly review (Week 06)
6. [ ] Copy `templates/weekly-review-template.md` into a new GitHub issue titled **"Weekly Review — Week 06"** and fill it in.
7. [ ] Update `PROGRESS.md` with PRs merged, what shipped (chatbot!), and confidence scores.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
