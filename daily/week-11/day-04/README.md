# Week 11 · Day 04 — GitHub Actions CI: run pytest on every PR

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Add a GitHub Actions workflow that runs `pytest` on every push/PR.
- [ ] Get a **green check** on your PRs (the exact artifact interviewers love to see).
- [ ] Handle secrets in CI via repository secrets, not committed files.

## Learn (with resources)
- **GitHub Actions docs** — quickstart + "Building and testing Python": https://docs.github.com/actions
- YouTube — **TechWorld with Nana** — GitHub Actions / CI-CD crash course.
- Reuse the tests you wrote in Week 8 (agent) and Week 9 (eval/prompt regression).

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-github-actions-ci`.
2. [ ] `.github/workflows/ci.yml`: trigger on `push` and `pull_request`; set up Python, install deps, run `pytest`. Cache pip if you like.
3. [ ] Make sure fast/offline unit tests run in CI (don't burn API budget on every push — mark live-API tests to skip in CI, e.g., an env flag or `-m "not live"`). Note this decision in the workflow.
4. [ ] If any test needs a key, add it as a GitHub **repository secret** and reference it via `${{ secrets.* }}` — never hard-coded.
5. [ ] Open a PR and confirm the check runs and goes **green**. Intentionally break a test on a scratch commit to watch it go red, then fix it.
6. [ ] `projects/intermediate/llm-api-docker/README.md`: add a CI badge and a line about what the workflow does.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge (only after the check is green).

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
