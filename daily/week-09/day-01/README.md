# Week 09 · Day 01 — LLM evaluation concepts

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Explain why "it works on my three examples" is *not* evidence an LLM app is good.
- [ ] Define the core eval building blocks: **golden dataset**, **LLM-as-judge**, and **rubric scoring**.
- [ ] Decide which eval method fits which kind of output (exact-match vs open-ended).

## Learn (with resources)
- **DeepLearning.AI short course** — "Building and Evaluating Advanced RAG" (evaluation lessons) and, from Phase 5 prep, "Evaluating and Debugging Generative AI": https://www.deeplearning.ai/short-courses
- **Anthropic docs** — evaluating prompts / defining success criteria: https://docs.anthropic.com
- This is **your differentiator** — your Manual QA background maps directly: golden set = test suite, rubric = acceptance criteria, LLM-as-judge = an automated grader.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-eval-concepts`.
2. [ ] `projects/intermediate/eval-concepts/NOTES.md`: in your own words, define golden dataset, LLM-as-judge, rubric scoring, and when to use each. Draw the parallel to QA test design.
3. [ ] `projects/intermediate/eval-concepts/golden.jsonl`: hand-write a small golden set (8–12 rows) for a task you already built (e.g., the summarizer or the tool agent). Each row: `input`, `expected`/`reference`, and a short `notes` field on what "good" means.
4. [ ] `projects/intermediate/eval-concepts/rubric.md`: a 3–5 criterion rubric (e.g., accuracy, completeness, tone, format) with a 1–5 scale and what each score means.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
