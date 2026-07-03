# Week 13 · Day 03 — Prompt regression tests + input/output guardrails

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Turn key eval cases into pytest regression tests that fail loudly on drift.
- [ ] Add input guardrails (validation, length/PII checks) and output guardrails (grounding/format).
- [ ] Make "did I break the prompt?" a question CI can answer, not a vibe.

## Learn (with resources)
- **pytest docs** — parametrized tests + fixtures: https://docs.pytest.org
- **DeepLearning.AI** — "Evaluating and Debugging Generative AI" (regression + guardrails).
- Lean on your manual-QA instincts: what would a malicious or careless user type?

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week13-day03-regression-guardrails`.
2. [ ] Write `tests/test_regression.py`: parametrize over a curated subset of golden cases and assert on stable properties (e.g. out-of-scope questions must refuse; certain questions must cite a source; answer must contain a known fact). Use assertions on structure/behavior, not brittle exact-string matches.
3. [ ] Add `app/guardrails.py`: **input** guards (reject empty/oversized input, strip or flag obvious PII/secrets, cap token length) and **output** guards (require sources for factual claims, validate the response shape, block if the model leaks the system prompt).
4. [ ] Wire the guardrails into the API path and add tests that malicious/empty inputs are handled gracefully.
5. [ ] Run `pytest -q` and confirm green. Deliberately break a prompt and confirm a regression test goes red — then fix it.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
