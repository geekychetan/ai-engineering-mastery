# Week 01 · Day 05 — Modules, debugging + a deliberate merge conflict

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Split code into modules and import between files.
- [ ] Read tracebacks and debug methodically.
- [ ] Create and **resolve a merge conflict** on purpose (this removes future fear of them).

## Learn (with resources)
- **CS50P** — Week 4 (Libraries) — importing and using modules.
- **Atlassian** — "Merging" and "Resolving merge conflicts": https://www.atlassian.com/git/tutorials

## Homework (branch → PR)
1. [ ] `projects/small/basics/mathutils.py`: functions `mean(nums)` and `is_prime(n)` with docstrings. Import and use them from a `main.py`.
2. [ ] Introduce a bug, use `print()` / VS Code debugger to find it, fix it. Describe the process in the reflection.
3. [ ] **Merge conflict drill:**
   ```bash
   git switch -c day-05-conflict-a && echo "line A" >> notes/conflict-demo.md && git add -A && git commit -m "branch A edit"
   git switch main && git switch -c day-05-conflict-b && echo "line B" >> notes/conflict-demo.md && git add -A && git commit -m "branch B edit"
   git merge day-05-conflict-a    # conflict! open the file, resolve, commit
   ```
   Resolve the conflict, keeping both lines sensibly. Explain what the `<<<<<<<`, `=======`, `>>>>>>>` markers meant.
4. [ ] Push your module work as a PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
