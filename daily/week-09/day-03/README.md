# Week 09 · Day 03 — Prompt regression testing

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Treat prompts like code: version them and test them so a "small tweak" can't silently break quality.
- [ ] Write `pytest` tests that fail when output quality drops below a threshold.
- [ ] Understand flakiness (non-determinism) and how to keep eval tests stable.

## Learn (with resources)
- **pytest docs** (fixtures, parametrize, assertions): https://docs.pytest.org
- **Anthropic docs** — prompt versioning & regression testing: https://docs.anthropic.com
- Your QA lens is the whole point here — this is regression testing, applied to prompts.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-prompt-regression`.
2. [ ] `projects/intermediate/prompt-regression/prompts.py`: keep the current prompt as a named, versioned string (e.g., `SUMMARIZER_V1`).
3. [ ] `projects/intermediate/prompt-regression/test_prompt_quality.py`: `@pytest.mark.parametrize` over your golden set; call the app; assert the judge score for each row is `>=` a threshold, and assert structural invariants (valid JSON, required fields present, no forbidden phrases).
4. [ ] Reduce flakiness: set temperature low/0 for the tested calls, and consider asserting on a *mean* over a small set rather than a single call. Note the tradeoff in the README.
5. [ ] Prove it works: intentionally break the prompt, run `pytest`, watch it go red, then fix it and watch it go green. Capture that in the reflection.
6. [ ] `projects/intermediate/prompt-regression/README.md`: why prompts are code and how to run the tests.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
