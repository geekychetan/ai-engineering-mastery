# Week 04 · Day 03 — asyncio basics

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Explain what `async`/`await` do and why they matter for LLM apps (concurrent API calls without threads).
- [ ] Write and run coroutines with `asyncio.run()`.
- [ ] Run several awaitables concurrently with `asyncio.gather()` and observe the speedup vs sequential.

## Learn (with resources)
- **CS50P** — no new lecture; this is a forward-looking topic for Phase 3 (LLM apps).
- **Real Python** — "Async IO in Python: A Complete Walkthrough": https://realpython.com
- **Python docs** — `asyncio`: https://docs.python.org/3/library/asyncio.html

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-asyncio`.
2. [ ] `projects/small/async_demo/sleepers.py`: three `async def` tasks that each `await asyncio.sleep(...)` for different durations and print when they finish. Run them sequentially (awaited one by one) vs concurrently with `asyncio.gather()`; time both with `time.perf_counter()` and print the difference.
3. [ ] Add a comment at the top of the file explaining, in your own words, how this pattern will let an LLM app fire multiple API calls concurrently instead of waiting on each in turn.
4. [ ] `projects/small/async_demo/fetch_many.py`: (optional stretch) use `httpx.AsyncClient` (or `aiohttp`) to GET several URLs from a public API concurrently with `gather`. If you skip it, note why in the PR.
5. [ ] Run `black`/`ruff`; fix issues.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
