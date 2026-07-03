# Week 03 · Day 05 — REST APIs with requests + .env secrets

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Make GET and POST requests with `requests`, passing query params and headers.
- [ ] Check status codes, handle errors (`raise_for_status`, timeouts, `try/except`), and parse the JSON response.
- [ ] Keep secrets out of git with a `.env` file loaded via `python-dotenv` (never commit secrets).

## Learn (with resources)
- **CS50P** — Week 4 (Libraries) — using `requests` and third-party packages.
- **Corey Schafer** — "Python Requests Tutorial" (YouTube).
- **Real Python** — "Python's Requests Library (Guide)": https://realpython.com
- **Python docs** — `requests` is third-party; install with `pip install requests python-dotenv`.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-rest-apis`.
2. [ ] Confirm `.venv` is active; `pip install requests python-dotenv` and record them in `requirements.txt`.
3. [ ] `projects/small/api/fetch_json.py`: GET from a free public API (e.g. `https://api.github.com/users/<name>` or `https://jsonplaceholder.typicode.com/todos/1`), call `raise_for_status()`, set a timeout, wrap in `try/except requests.RequestException`, and print selected fields from the JSON.
4. [ ] `projects/small/api/with_params.py`: make a request that uses the `params=` argument and a custom `headers=` dict (e.g. a User-Agent), and print the final requested URL.
5. [ ] Create a `.env` file with a placeholder secret (`API_KEY=changeme`), load it with `dotenv`, and read it via `os.getenv`. **Add `.env` to `.gitignore`** and verify `git status` does not list it. Commit a `.env.example` with the key names only.
6. [ ] Push, PR with `Closes #<issue>`, self-review (double-check no secret leaked into the diff), merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
