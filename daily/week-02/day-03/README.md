# Week 02 · Day 03 — Dicts & sets deep + dict comprehensions

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Use dicts confidently: create, update, iterate over `.items()`/`.keys()`/`.values()`, and safely read with `.get()` and `.setdefault()`.
- [ ] Work with nested dicts (dict-of-dicts / dict-of-lists) and know when a set is the right tool (membership, dedup).
- [ ] Write a dict comprehension.

## Learn (with resources)
- **CS50P** — Week 2 (Loops) — dictionaries in the lecture and problem set.
- **Corey Schafer** — "Python Tutorial: Dictionaries" video (YouTube).
- **Real Python** — "Dictionaries in Python": https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-dicts-sets`.
2. [ ] `projects/small/collections/word_count.py`: given a sentence, build a dict of `{word: count}` using `.get(word, 0)` (or `.setdefault`). Print the counts sorted by frequency (highest first).
3. [ ] `projects/small/collections/contacts.py`: a nested dict `{name: {"email": ..., "phone": ...}}`. Write functions to add a contact, look one up safely with `.get()`, and iterate over all contacts printing a formatted line each.
4. [ ] `projects/small/collections/sets_demo.py`: given two lists with duplicates, use sets to find the unique items, the intersection, and the difference. Show membership testing (`in`) on a set.
5. [ ] `projects/small/collections/dict_comp.py`: build a dict comprehension mapping numbers 1–10 to their squares, and one that inverts an existing `{k: v}` dict to `{v: k}`.
6. [ ] CS50P Week 2 problem set: complete at least one dictionary-based exercise.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
