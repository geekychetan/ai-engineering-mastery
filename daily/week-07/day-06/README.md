# Week 07 · Day 06 — Improve RAG (chunk sizes, reranking) + weekly review

**Estimated time:** ~4 hrs (lighter consolidation + weekly review day)
**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Run an experiment: measure how chunk size / top-k changes answer quality on your golden set.
- [ ] Add a reranking step and judge whether it helps.
- [ ] Write up the tradeoffs you actually observed.

## Learn (with resources)
- **DeepLearning.AI short course** — "Building and Evaluating Advanced RAG": the sentence-window / reranking lessons.
- **LangChain docs (Python)** — retrievers + a cross-encoder / reranker (or a simple LLM-rerank prompt): https://python.langchain.com
- Your evaluation instinct from QA is the point of today: change one variable, measure, compare.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-rag-improve`.
2. [ ] Create `projects/intermediate/rag-qa/experiments.py` that runs your `golden_questions.md` through the pipeline under 2–3 settings (e.g. chunk size 500 vs 1000; top-k 3 vs 5) and records for each: how many answers were correct + correctly cited.
3. [ ] Add a **reranking** pass: retrieve more candidates than needed, then rerank (cross-encoder or an LLM-rerank prompt) and keep the best. Re-run the golden set and compare.
4. [ ] Write `projects/intermediate/rag-qa/EXPERIMENTS.md` with a small results table and your conclusion: which settings won, what got worse, and the cost/latency tradeoff you'd accept.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Weekly review (Week 07)
6. [ ] Copy `templates/weekly-review-template.md` into a new GitHub issue titled **"Weekly Review — Week 07"** and fill it in.
7. [ ] Update `PROGRESS.md` with PRs merged, the RAG app shipped, experiment findings, and confidence scores.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
