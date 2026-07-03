# Week 11 · Day 03 — Env/secrets in containers + docker compose (light)

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Explain why you must **never bake API keys into an image** (anyone with the image can read them).
- [ ] Pass secrets/config via environment variables at runtime.
- [ ] Use a light `docker-compose.yml` to run the app (and wire in env) with one command.

## Learn (with resources)
- **Docker docs** — environment variables, `--env-file`, and Compose basics: https://docs.docker.com
- YouTube — **TechWorld with Nana** — Docker Compose crash course.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-secrets-compose`.
2. [ ] Prove the anti-pattern: inspect an image's layers/history and note how a baked-in `ENV KEY=...` or copied `.env` would be exposed. Write the takeaway.
3. [ ] `projects/intermediate/llm-api-docker/.env.example`: template of required env vars (no real values). Confirm the real `.env` is git-ignored **and** docker-ignored.
4. [ ] `projects/intermediate/llm-api-docker/docker-compose.yml`: define the app service, map the port, and pass secrets via `env_file: .env` (not committed). Run with `docker compose up`.
5. [ ] Confirm the app runs with the key supplied at runtime and that the key is not present in the built image.
6. [ ] Update `README.md`: secrets policy + `docker compose` run instructions.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
