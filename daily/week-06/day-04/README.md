# Week 06 · Day 04 — Real-world API robustness (retries, timeouts, streaming)

**Estimated time:** ~5 hrs (1 hr learn + 4 hr build)
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Handle transient failures with retries + exponential backoff.
- [ ] Set timeouts and handle rate-limit errors without crashing.
- [ ] Stream a response so output appears token-by-token.

## Learn (with resources)
- **Anthropic docs** — "Errors" (rate limits, overloaded), "Streaming Messages", and client retry/timeout options: https://docs.anthropic.com (OpenAI has equivalent pages).
- **DeepLearning.AI short course** — "Building Systems with the ChatGPT API": the lesson on chaining calls / handling failures.
- Your QA background applies directly: think in terms of failure modes and edge cases.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-api-robustness`.
2. [ ] Create `projects/intermediate/llm-basics/robust_call.py` that wraps a call with:
   - A **timeout** on the request.
   - **Retry with exponential backoff** on transient errors (rate limit / overloaded / timeout), max 3 attempts. Catch the specific exception types, not a bare `except`.
   - A clear message when it finally gives up.
3. [ ] Create `projects/intermediate/llm-basics/stream.py` that streams a response and prints text as it arrives (flush per chunk).
4. [ ] Add `projects/intermediate/llm-basics/failure_modes.md`: list at least 4 ways an LLM API call can fail in production and how your code detects/handles each (like a QA test-case table).
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
