# Week 02 · Day 06 — Consolidation: text-stats CLI + weekly review

**Estimated time:** ~4 hrs (lighter consolidation + weekly review day)
**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Combine the week's skills (strings, lists, dicts, functions, stdlib) into one small program.
- [ ] Build a text-stats CLI that counts words, characters, and sentences.
- [ ] Review the week honestly and record progress.

## Learn (with resources)
- No new lecture today — this is a **build + review** day.
- **Real Python** — "How to Make a Command-Line Interface" (basic `sys.argv` / `input`) for reference: https://realpython.com
- Skim any CS50P Week 1–4 sections that still felt fuzzy this week.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-text-stats`.
2. [ ] `projects/small/text_stats/text_stats.py`: a CLI that reads text (from a file path argument or pasted input) and prints:
   - total character count (with and without spaces),
   - total word count,
   - sentence count (split on `.`, `!`, `?`),
   - the 5 most common words (use `collections.Counter`).
3. [ ] Wrap the logic in small, single-purpose functions (`count_words`, `count_sentences`, `top_words`) each with a docstring, and call them from an `if __name__ == "__main__":` block.
4. [ ] Add a short `projects/small/text_stats/README.md` explaining how to run it and showing sample output.
5. [ ] **Weekly review:** copy `templates/weekly-review-template.md` into a new GitHub issue titled "Weekly Review — Week 02" and fill it in. Update `PROGRESS.md` to mark Week 02 done.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
