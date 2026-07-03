# Week 12 · Day 05 — FastAPI backend + basic Streamlit UI

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Expose the agent/RAG pipeline behind a clean FastAPI endpoint.
- [ ] Build a minimal Streamlit UI that talks to the API.
- [ ] Run the whole thing locally: type a question in the UI, get a grounded answer with sources.

## Learn (with resources)
- **FastAPI docs** — first steps + request/response models: https://fastapi.tiangolo.com
- **Streamlit docs** — build a simple chat UI: https://docs.streamlit.io
- **Building Systems with the ChatGPT API** (DeepLearning.AI) — for structuring the request/response layer cleanly.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week12-day05-api-ui`.
2. [ ] Write `app/api.py` (FastAPI): a `POST /ask` endpoint that takes a question, runs the agent, and returns `{answer, sources, tool_trace}`. Add a `GET /health` endpoint. Use Pydantic models for the request/response.
3. [ ] Run it locally with `uvicorn` and confirm it works via `/docs` (Swagger UI) or `curl`.
4. [ ] Write `app/ui.py` (Streamlit): a simple chat box that POSTs to `/ask` and renders the answer, an expandable "Sources" section, and (optionally) the tool trace.
5. [ ] Keep secrets in env vars, not code — add a `.env.example` and make sure real keys are gitignored.
6. [ ] Update the capstone stub README with local run instructions (start API, then UI). Take one screenshot for your build notes later.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
