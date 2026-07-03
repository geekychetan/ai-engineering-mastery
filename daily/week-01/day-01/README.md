# Week 01 · Day 01 — Environment setup + the git daily loop

**Estimated time:** ~5 hrs (1–1.5 hr CS50P + 3.5–4 hr setup/build)
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Working Python dev environment (terminal, VS Code, Python, venv, pip).
- [ ] Run the full git loop end to end: branch → commit → push → PR → review → merge.
- [ ] Understand the repo layout and how daily work flows.

## Learn (with resources)
- **CS50P** — Week 0 lecture (Functions, Variables): https://cs50.harvard.edu/python
- **GitHub Skills** "Introduction to GitHub": https://skills.github.com
- **Atlassian** — "Setting up a repository" + "Saving changes": https://www.atlassian.com/git/tutorials

## Homework (do on a branch → PR)
1. [ ] Install/verify: Python (via `pyenv` or python.org), VS Code, and confirm `git --version` and `gh --version`.
2. [ ] In this repo, create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   python --version
   ```
3. [ ] Create a branch for today:
   ```bash
   git switch -c day-01-setup
   ```
4. [ ] Create `projects/small/hello/hello.py` that prints your name and today's goal, and run it:
   ```bash
   python projects/small/hello/hello.py
   ```
5. [ ] Commit, push, open a PR, self-review the diff on GitHub, then merge:
   ```bash
   git add projects/small/hello/hello.py
   git commit -m "day 01: first script + environment setup"
   git push -u origin day-01-setup
   gh pr create --fill        # add "Closes #<issue>" in the body
   gh pr merge --squash --delete-branch
   ```
6. [ ] Confirm the issue auto-closed when the PR merged.

## Reflection (fill at end of day, 10 min)
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
