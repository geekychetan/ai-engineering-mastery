# Week 05 · Day 06 — Transformers & tokenization + project + weekly review

**Estimated time:** ~4 hrs (lighter consolidation + weekly review day)
**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Explain, at a high level, what attention does and why transformers beat older models for language.
- [ ] Tokenize text hands-on and explain why token count matters (cost + context limits).
- [ ] Ship one trained-and-evaluated sklearn model with a written metric-choice justification.

## Learn (with resources)
- **CS50P** — finish CS50P this week: complete the remaining problem set / final project so it wraps here.
- **3Blue1Brown** (YouTube) — "But what is a GPT? Visual intro to transformers" and (optional) "Attention in transformers, visually explained".
- **Hugging Face course** — the tokenizer section for hands-on token counting: https://huggingface.co/learn

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-transformers-project`.
2. [ ] **Tokenization:** create `projects/small/tokenize/tokens.py` that takes a few sentences and prints the token count (use `tiktoken`, or the Anthropic token counter, or a HF tokenizer). Add a short note on how token count relates to API cost/context windows.
3. [ ] **Project (capstone of the week):** in `projects/small/ml-model-writeup/` build `model.py` that trains + evaluates ONE sklearn model (reuse or extend your classifier/regressor) cleanly end to end, and write `WRITEUP.md` covering:
   - The problem and the dataset.
   - Which metric you chose to optimize and **why** (lean on your Day-03 reasoning).
   - Results (the confusion matrix / scores) and one honest limitation.
4. [ ] Add `projects/small/ml-notes/transformers.md`: attention + transformers in your own words, 1 short paragraph.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Weekly review (Week 05)
6. [ ] Copy `templates/weekly-review-template.md` into a new GitHub issue titled **"Weekly Review — Week 05"** and fill it in.
7. [ ] Update `PROGRESS.md` with the week's PRs merged, CS50P completion, and confidence scores.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
