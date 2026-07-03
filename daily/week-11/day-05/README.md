# Week 11 · Day 05 — Deploy the containerized LLM app live on AWS

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Run your Docker image on EC2 and reach the app from the public internet.
- [ ] Supply the API key on the server via env, not baked into the image.
- [ ] Confirm the full stack works end to end, then tear it down cleanly.

## Learn (with resources)
- **AWS Getting Started** — EC2 (reuse your Week 10 runbook): https://aws.amazon.com/getting-started
- **Docker docs** — running on a remote host / installing Docker on Linux: https://docs.docker.com
- YouTube — **TechWorld with Nana** — deploying a container to a server.

> **Cost discipline:** Free Tier `t2.micro`. Open only the app port (from your IP if possible). **Terminate the instance as soon as your demo/screenshots are captured.** Billing alarm stays on.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-deploy-container-aws`.
2. [ ] Launch a Free Tier EC2 instance; install Docker on it; get your image onto it (build from a git clone, or pull from Docker Hub / ECR).
3. [ ] Run the container with the API key passed at runtime (`-e`/`--env-file`), mapping the app port. Add the security-group inbound rule.
4. [ ] Hit the public IP from your laptop; test `/health`, `/chat`, and (if wired) the Streamlit UI. Screenshot the live app.
5. [ ] `projects/intermediate/llm-api-docker/DEPLOY.md`: the live-deploy runbook + teardown steps + the screenshot. This is a portfolio artifact — write it cleanly.
6. [ ] **Tear down:** stop/terminate the instance, remove the inbound rule; confirm nothing runs.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
