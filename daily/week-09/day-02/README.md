# Week 09 · Day 02 — Build an eval harness

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Build a small harness that runs your app over the whole golden set automatically.
- [ ] Score each output — exact/similarity for closed tasks, **LLM-as-judge** against your rubric for open-ended ones.
- [ ] Produce an aggregate report (pass rate / mean score) you can act on.

## Learn (with resources)
- **DeepLearning.AI short course** — "Building and Evaluating Advanced RAG" (the eval-harness portion).
- **Anthropic docs** — running evals + LLM-as-judge prompting: https://docs.anthropic.com
- Reuse yesterday's `golden.jsonl` and `rubric.md`.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-eval-harness`.
2. [ ] `projects/intermediate/eval-harness/run_eval.py`: load the golden set, run the app under test on each `input`, and collect outputs.
3. [ ] `projects/intermediate/eval-harness/judge.py`: a `score(output, reference, rubric)` function that calls the model as a judge, asks it to return a **structured** verdict (pydantic: per-criterion 1–5 + one-line justification), and validates it.
4. [ ] Aggregate results into a printed table + a saved `results.json` (per-row scores, mean per criterion, overall pass rate against a threshold you set).
5. [ ] Run it against your Week 8 agent or Week 6/7 app; note where it scores lowest.
6. [ ] `projects/intermediate/eval-harness/README.md`: how to run it and how to read the report.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
