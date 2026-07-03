# Week 09 · Day 04 — FastAPI backend for an LLM app

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Stand up a FastAPI service with a POST endpoint that wraps an LLM call.
- [ ] Define request/response shapes with pydantic and get automatic validation + `/docs`.
- [ ] Return clean errors (bad input, upstream failure) instead of 500s.

## Learn (with resources)
- **FastAPI docs** — first steps, request body, response model: https://fastapi.tiangolo.com
- pydantic request/response models (reuse what you learned Week 8 Day 04).
- **Anthropic docs** — reference for the LLM call inside the endpoint: https://docs.anthropic.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-fastapi-backend`.
2. [ ] `projects/intermediate/llm-api/main.py`: a FastAPI app with `GET /health` and `POST /chat` that takes a `ChatRequest` (pydantic: `message: str`, optional `system: str`) and returns a `ChatResponse` (`reply: str`, `model: str`, `tokens: int | None`).
3. [ ] Wire `/chat` to your LLM call. Add validation (reject empty messages) and a `try/except` that returns a `502`/clear error on upstream failure.
4. [ ] Run locally with `uvicorn` and exercise it via the auto-generated `/docs` Swagger UI and a `curl` example.
5. [ ] `projects/intermediate/llm-api/requirements.txt` + `README.md`: how to install and run.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
