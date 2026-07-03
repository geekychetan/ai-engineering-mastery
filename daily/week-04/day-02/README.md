# Week 04 · Day 02 — typer CLI apps

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Build a multi-command `typer` app with `@app.command()`.
- [ ] Use typed arguments and options (with defaults, help text, and prompts).
- [ ] Keep logic in testable functions separate from the CLI layer.

## Learn (with resources)
- **CS50P** — no new lecture; applies OOP/functions/files from Weeks 3–4.
- **typer docs** — Tutorial: Commands, Arguments, and Options: https://typer.tiangolo.com
- **Real Python** — "Build a Command-Line To-Do App With Python and Typer": https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-typer-cli`.
2. [ ] `projects/small/notes_cli/notes.py`: a `typer` app with commands `add <text>`, `list`, `search <term>`, and `delete <id>`, storing notes in a JSON file.
3. [ ] Give at least one command a typed `--option` with a default and help text (e.g. `--limit` on `list`), and one that uses `typer.confirm` before deleting.
4. [ ] Add type hints on the command functions and keep the storage logic (load/save/add/search) in separate plain functions.
5. [ ] Run `black`/`ruff` on the file and fix issues. Add a `projects/small/notes_cli/README.md` with usage examples (`python notes.py --help` output).
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
