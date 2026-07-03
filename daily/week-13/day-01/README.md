# Week 13 · Day 01 — Build the eval suite: assemble a golden dataset

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Assemble a golden dataset of question → expected-answer pairs for the capstone.
- [ ] Cover the real distribution: easy, hard, adversarial, and out-of-scope cases.
- [ ] Store it in a machine-readable format your eval runner can consume.

## Learn (with resources)
- **DeepLearning.AI** — "Evaluating and Debugging Generative AI" (this is *your* week — go deep).
- **DeepLearning.AI** — "Building and Evaluating Advanced RAG" (eval half).
- Your QA background is the edge here: think like a test designer — equivalence classes, boundary cases, negative tests.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week13-day01-golden-dataset`.
2. [ ] Create `projects/capstone/eval/golden.jsonl` (or `.csv`): each row = `{id, question, expected_answer, category, must_cite_source}`. Start from `eval/seed_questions.md` and grow it.
3. [ ] Aim for ~25–40 cases spanning categories: **easy** (clearly in docs), **hard** (needs multi-chunk synthesis), **adversarial** (leading/ambiguous), and **out-of-scope** (correct answer is "I don't know"). As a QA person, deliberately include the nasty edge cases others skip.
4. [ ] For out-of-scope rows, the expected behavior is a graceful refusal — make that explicit in `expected_answer`.
5. [ ] Write `eval/run_eval.py` scaffold that just loads the dataset and calls your pipeline for each question, dumping raw outputs to `eval/results/` (scoring comes tomorrow).
6. [ ] Push, PR with `Closes #<issue>`, self-review (is the dataset representative, or all softballs?), merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
