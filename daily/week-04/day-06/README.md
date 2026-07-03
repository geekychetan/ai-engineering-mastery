# Week 04 · Day 06 — PROJECT: API → pandas → tests + Phase 1 retro

**Estimated time:** ~4 hrs (lighter build + weekly review + phase retro)
**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Combine the phase's skills into one script: call a public REST API, process the data with pandas, output a small result.
- [ ] Cover the data-processing logic with `pytest` tests (your QA strength).
- [ ] Close out Phase 1 with a weekly review and a short phase retro.

## Learn (with resources)
- No new lecture — this is the **Phase 1 capstone build + review** day.
- Reference back to Week 3 Day 05 (`requests` + `.env`), Week 3 Day 06 (`pytest`), and Week 4 Day 05 (`pandas`).
- **pytest docs**: https://docs.pytest.org · **Real Python** requests/pandas guides: https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-phase1-project`.
2. [ ] `projects/small/api_pandas/fetch.py`: fetch JSON from a free public API (e.g. `https://jsonplaceholder.typicode.com/posts` or a public weather/crypto API). Handle errors with `raise_for_status`, a timeout, and `try/except`. Keep any key in `.env` (never committed).
3. [ ] `projects/small/api_pandas/process.py`: load the JSON into a pandas `DataFrame` and compute at least one meaningful result (e.g. counts per group, top-N, or an average). Return the result from a pure function so it's testable.
4. [ ] `projects/small/api_pandas/test_process.py`: pytest tests that feed the processing function **sample/fixture data** (not a live call) and assert the computed result. Include at least one edge case.
5. [ ] Run `pytest -v`, `black`, and `ruff`; make everything pass. Add a `projects/small/api_pandas/README.md` with how to run it and sample output.
6. [ ] **Weekly review:** copy `templates/weekly-review-template.md` into a new GitHub issue titled "Weekly Review — Week 04" and fill it in. Update `PROGRESS.md` to mark Week 04 / Phase 1 done.
7. [ ] **Phase 1 retro:** add a short note (in the weekly-review issue or `PROGRESS.md`) covering: which exit criteria you can now do unaided, what still feels shaky, and what to shore up before Phase 2.
8. [ ] Push, PR with `Closes #<issue>`, self-review (confirm no secrets in the diff), merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
