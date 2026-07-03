# Week 13 · Day 04 — Containerize (Docker) + deploy to AWS

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Containerize the capstone with Docker (API + UI).
- [ ] Run it locally via the container, then deploy to AWS.
- [ ] Reach the app at a public URL and confirm the eval still passes against it.

## Learn (with resources)
- **Docker docs** — Dockerfile + docker compose: https://docs.docker.com
- **TechWorld with Nana** (YouTube) — Docker + deploy walkthrough.
- **AWS Getting Started** — pick the simplest path you know (EC2 with Docker, ECS, or App Runner): https://aws.amazon.com/getting-started

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week13-day04-docker-aws`.
2. [ ] Write a `Dockerfile` for the FastAPI app (and either a second image or a `docker-compose.yml` to also run Streamlit). Use a slim base image and a `.dockerignore`.
3. [ ] Build and run locally: `docker build` → `docker run`, hit `/health` and `/ask`. Confirm secrets come from env, not baked into the image.
4. [ ] Deploy to AWS using the simplest option you're comfortable with (EC2 running the container, or App Runner/ECS). Set env vars/secrets on the AWS side.
5. [ ] Confirm the public endpoint works, then point `eval/run_eval.py` at the deployed URL and re-run — the deployed app should match your local metrics. Record the deployed URL in the capstone README.
6. [ ] Note rough monthly cost + a teardown reminder so you don't burn AWS credits idle.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
