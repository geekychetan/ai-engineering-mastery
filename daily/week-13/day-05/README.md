# Week 13 · Day 05 — GitHub Actions CI on the capstone repo

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Add a GitHub Actions workflow that runs tests on every PR.
- [ ] Gate merges on green CI (lint + pytest, incl. regression tests).
- [ ] Show a passing CI badge in the capstone README.

## Learn (with resources)
- **GitHub Actions docs** — workflow syntax, Python CI: https://docs.github.com/actions
- **TechWorld with Nana** (YouTube) — CI/CD fundamentals.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week13-day05-ci`.
2. [ ] Add `.github/workflows/ci.yml`: on `pull_request` and `push` to main — set up Python, install deps, run a linter (ruff/flake8) and `pytest`. Cache pip for speed.
3. [ ] Keep the LLM-judge eval OUT of the required CI path (it costs money/tokens and is nondeterministic). Run the fast deterministic regression + guardrail tests in CI; make the full eval a separate manual/scheduled job or a documented local command.
4. [ ] Store any needed test keys as GitHub Actions **secrets**, not in the workflow file. Where possible, stub the LLM in unit tests so CI doesn't need a live key.
5. [ ] Open a throwaway PR to watch CI run; add a branch protection rule requiring the check to pass before merge.
6. [ ] Add the CI status badge to the capstone README.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge (watch your own CI go green).

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
