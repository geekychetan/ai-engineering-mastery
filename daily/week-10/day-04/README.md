# Week 10 · Day 04 — Deploy a FastAPI app on EC2

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-04 issue here)

## Objectives
- [ ] Get your Week 9 FastAPI app running on an EC2 instance and reachable via its public IP.
- [ ] Open the right port in the security group (and only that port).
- [ ] Manage the API key on the server via an environment variable, not in code.

## Learn (with resources)
- **AWS Getting Started** — EC2 + connecting/serving an app: https://aws.amazon.com/getting-started
- **FastAPI docs** — running with `uvicorn` (host `0.0.0.0`): https://fastapi.tiangolo.com
- YouTube — **freeCodeCamp** AWS course (EC2 networking section).

> **Cost discipline:** Free Tier `t2.micro` only. Security group: SSH (22) from your IP + the app port (e.g., 8000) from your IP if possible. **Terminate at the end of the session.**

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-04-deploy-fastapi-ec2`.
2. [ ] Launch a Free Tier EC2 instance; SSH in; clone your repo (or copy the `llm-api` app); create a venv and install `requirements.txt`.
3. [ ] Set your LLM API key as an env var on the server (`export ...` / a non-committed `.env`), then run `uvicorn main:app --host 0.0.0.0 --port 8000`.
4. [ ] Add an inbound rule for port 8000 and hit `http://<public-ip>:8000/health` and `/docs` from your laptop browser. Screenshot the working `/docs`.
5. [ ] `projects/intermediate/aws-ec2/deploy-fastapi.md`: the deploy runbook + the teardown steps. Add the screenshot.
6. [ ] **Tear down** the instance and remove the extra inbound rule; confirm nothing is running.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
