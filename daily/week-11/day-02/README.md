# Week 11 · Day 02 — Containerize your FastAPI/LLM app

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Write a production-ish Dockerfile for your Week 9 FastAPI LLM app.
- [ ] Run the app in a container and hit it from your host.
- [ ] Keep the image lean and reproducible (pinned deps, `.dockerignore`).

## Learn (with resources)
- **Docker docs** — Dockerfile best practices, `.dockerignore`: https://docs.docker.com
- YouTube — **TechWorld with Nana** — building a Dockerfile for a real app.
- **FastAPI docs** — deployment in containers (uvicorn command): https://fastapi.tiangolo.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-containerize-app`.
2. [ ] Copy your `llm-api` app into `projects/intermediate/llm-api-docker/` (or work in place). Add a `Dockerfile`: slim Python base, install from `requirements.txt`, copy source, `EXPOSE 8000`, `CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]`.
3. [ ] Add a `.dockerignore` (exclude `.venv`, `__pycache__`, `.env`, `.git`).
4. [ ] Build and run passing the API key at runtime: `docker run -p 8000:8000 -e ANTHROPIC_API_KEY=... llm-api`. Confirm `/health` and `/chat` work.
5. [ ] `projects/intermediate/llm-api-docker/README.md`: build + run instructions (note the key is passed at runtime, never built in — tomorrow's topic).
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
