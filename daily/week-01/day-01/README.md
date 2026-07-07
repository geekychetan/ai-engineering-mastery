# Week 01 · Day 01 — Environment setup + the git daily loop

**Estimated time:** ~5 hrs (1–1.5 hr CS50P + 3.5–4 hr setup/build)
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Working Python dev environment (terminal, VS Code, Python) managed with **uv**.
- [ ] Install the project's dependencies and run the test suite locally.
- [ ] Run the full git loop end to end: branch → commit → push → PR → review → merge.
- [ ] Understand the repo layout and how daily work flows.

## Learn (with resources)
- **CS50P** — Week 0 lecture (Functions, Variables): https://cs50.harvard.edu/python
- **uv** (the Python package/project manager we use): https://docs.astral.sh/uv
- **GitHub Skills** "Introduction to GitHub": https://skills.github.com
- **Atlassian** — "Setting up a repository" + "Saving changes": https://www.atlassian.com/git/tutorials

## Homework (do on a branch → PR)
1. [ ] Install/verify: **uv** (`brew install uv`), VS Code, and confirm `git --version` and `gh --version`.
2. [ ] From the repo root, install the project's dependencies. `uv` creates the virtual environment (`.venv/`) for you automatically:
   ```bash
   uv sync
   ```
3. [ ] Run the existing tests to confirm your environment works:
   ```bash
   uv run pytest -q        # expect: 2 passed
   ```
   > `greet.py` and `test_greet.py` in this folder are your worked example — read them to see what a tiny tested Python module looks like.
4. [ ] Create a branch for today:
   ```bash
   git switch -c day-01-setup
   ```
5. [ ] Create `projects/small/hello/hello.py` that prints your name and today's goal, and run it:
   ```bash
   uv run python projects/small/hello/hello.py
   ```
6. [ ] Commit, push, open a PR, self-review the diff on GitHub, then merge:
   ```bash
   git add projects/small/hello/hello.py
   git commit -m "day 01: first script + environment setup"
   git push -u origin day-01-setup
   gh pr create --fill        # add "Closes #<issue>" in the body
   gh pr merge --squash --delete-branch
   ```
7. [ ] Confirm the issue auto-closed when the PR merged.

## Reflection (fill at end of day, 10 min)
- **What clicked:** Learned brew installation, gh library, uv package manager
- **What's still fuzzy:** learning terminal commands
- **One thing to review tomorrow:** Revise and practice terminal commands
- **Time actually spent:** 3 hours
