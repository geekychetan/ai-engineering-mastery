# Week 13 · Day 02 — LLM-as-judge scoring + before/after metrics

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Implement an LLM-as-judge that scores answers against the golden set.
- [ ] Report real metrics (accuracy/quality, groundedness, refusal-correctness).
- [ ] Produce a before/after comparison after one prompt improvement.

## Learn (with resources)
- **DeepLearning.AI** — "Evaluating and Debugging Generative AI" (judge design, calibration, avoiding judge bias).
- **Anthropic docs** — prompt engineering for structured/JSON judge output: https://docs.anthropic.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week13-day02-llm-judge`.
2. [ ] Extend `eval/run_eval.py`: add an LLM-as-judge that, given `(question, expected_answer, actual_answer, sources)`, returns a structured score — e.g. `{correct: 0-1, grounded: bool, refused_when_should: bool, notes}`. Force JSON output and parse defensively.
3. [ ] Aggregate into a metrics summary: overall accuracy, groundedness rate, and correct-refusal rate on out-of-scope cases. Write it to `eval/results/report.md`.
4. [ ] Sanity-check the judge on 3–4 cases by hand — does its score match your human judgment? Note any judge disagreements (this awareness is itself a strong interview talking point).
5. [ ] Make ONE improvement (tweak the RAG prompt or bump top-k), re-run, and record **before → after** numbers in `report.md`. This delta is the money shot for your README and interviews.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
