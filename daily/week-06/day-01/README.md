# Week 06 · Day 01 — Your first LLM API call (safely)

**Estimated time:** ~5 hrs (1 hr learn + 4 hr build)
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Get an API key and load it safely from a `.env` file (never committed).
- [ ] Make a first successful API call and read back the response.
- [ ] Explain the messages format, tokens, and roughly how cost is computed.

## Learn (with resources)
- **CS50P** — with CS50P done last week, the freed time goes to building.
- **Anthropic docs** — "Get started" / first API call + the Messages API reference: https://docs.anthropic.com (OpenAI equivalent: https://platform.openai.com/docs — pick one provider and stick with it for the week).
- **DeepLearning.AI short course** — "Building Systems with the ChatGPT API" — first lessons on the request/response loop.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-llm-api`.
2. [ ] Get an API key. Create `projects/intermediate/llm-basics/.env` with `ANTHROPIC_API_KEY=...` (or `OPENAI_API_KEY=...`). Add `.env` to `.gitignore` and confirm `git status` does NOT show it.
3. [ ] `pip install` the SDK + `python-dotenv`; append them to `requirements.txt`.
4. [ ] Create `projects/intermediate/llm-basics/first_call.py` that:
   - Loads the key with `dotenv`.
   - Sends a single user message ("Explain what an API key is in one sentence") and prints the reply.
   - Prints the token usage from the response and estimates the cost from the model's per-token price (hardcode the rate + a comment).
5. [ ] Add `projects/intermediate/llm-basics/README.md` documenting how to set the key and run the script (assume a teammate with no key).
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
