# Week 03 · Day 06 — pytest intro + tested typer CLI + weekly review

**Estimated time:** ~4 hrs (lighter consolidation + weekly review day)
**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Write and run tests with `pytest` (test functions, `assert`, a simple fixture).
- [ ] Build a small `typer` CLI and cover its core logic with tests (your QA strength).
- [ ] Review the week and record progress.

## Learn (with resources)
- **pytest docs** — Getting Started + "How to write and report assertions": https://docs.pytest.org
- **ArjanCodes / Corey Schafer** — unit-testing videos (YouTube).
- **typer docs** — First Steps: https://typer.tiangolo.com (`pip install typer pytest`).

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-pytest-cli`.
2. [ ] `pip install typer pytest` and add them to `requirements.txt`.
3. [ ] `projects/small/todo_cli/todo.py`: a `typer` CLI with commands `add <task>`, `list`, and `done <index>`, persisting tasks to a JSON file. Keep the persistence/logic in plain functions so they're testable independently of the CLI.
4. [ ] `projects/small/todo_cli/test_todo.py`: pytest tests for the logic functions — adding a task, marking done, and one edge case (e.g. `done` on an out-of-range index). Use a `tmp_path` fixture so tests don't touch real files.
5. [ ] Run `pytest -v` and make all tests pass; paste the summary into the PR description.
6. [ ] **Weekly review:** copy `templates/weekly-review-template.md` into a new GitHub issue titled "Weekly Review — Week 03" and fill it in. Update `PROGRESS.md` to mark Week 03 done.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
