# Week 03 · Day 04 — File I/O + JSON + pathlib

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Read and write text files with `open()` + `with` (context managers).
- [ ] Parse and write JSON with `json.load`/`json.dump` (and `loads`/`dumps`).
- [ ] Work with paths using `pathlib.Path` instead of string concatenation.

## Learn (with resources)
- **CS50P** — Week 6 (File I/O) lecture.
- **Corey Schafer** — "Python Tutorial: File Objects" and "Working with JSON Data" (YouTube).
- **Python docs** — `pathlib`: https://docs.python.org/3/library/pathlib.html and `json`: https://docs.python.org/3/library/json.html

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-files-json`.
2. [ ] `projects/small/files/notes.py`: append user-entered notes to `notes.txt` (create it with `pathlib.Path` if missing), then read the file back and print all notes numbered.
3. [ ] `projects/small/files/contacts_json.py`: load a list of contacts from `contacts.json` (handle the file-not-found case by starting empty), let the user add a contact, then write the updated list back with `json.dump(..., indent=2)`.
4. [ ] `projects/small/files/paths_demo.py`: use `pathlib.Path` to print the current file's name, its parent directory, and glob-list all `*.py` files in the folder.
5. [ ] Make sure any generated data files that shouldn't be committed are added to `.gitignore` if appropriate.
6. [ ] CS50P Week 6 problem set: complete at least one exercise (e.g. `Lines of Code` or `Pizza Py`).
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
