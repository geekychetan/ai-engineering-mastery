# Week 06 · Day 02 — Prompt engineering fundamentals

**Estimated time:** ~5 hrs (1 hr learn + 4 hr build)
**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Write clear, specific instructions and use roles + delimiters to structure a prompt.
- [ ] Show, with before/after examples, how a vague prompt becomes a good one.
- [ ] Explain why specificity and delimiters reduce ambiguity for the model.

## Learn (with resources)
- **DeepLearning.AI short course** — "ChatGPT Prompt Engineering for Developers" (Isa Fulford & Andrew Ng): the "Guidelines" and "Iterative" lessons.
- **Anthropic docs** — Prompt engineering guide: "Be clear and direct", "Use XML tags", "Give Claude a role": https://docs.anthropic.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-prompt-fundamentals`.
2. [ ] Create `projects/intermediate/prompting/prompt_playground.py` — a small script that takes a prompt string and prints the model's reply, so you can iterate fast.
3. [ ] Create `projects/intermediate/prompting/before_after.md`. Pick 3 tasks (e.g. "summarize this review", "extract the action items", "rewrite this email politely"). For each, record:
   - A **vague** prompt + the messy result.
   - An **improved** prompt using: explicit instructions, a role, delimiters (XML tags or triple backticks) around the input, and a desired output shape.
   - The improved result + one sentence on why it's better.
4. [ ] Use delimiters correctly in at least one prompt to separate instructions from user-supplied text (and note why that matters for safety).
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
