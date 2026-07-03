# Phase 4 — Cloud & Deployment on AWS (Weeks 10-11)

**Goal:** take LLM apps from "runs on my laptop" to "running in the cloud." Hands-on AWS, Docker, and CI — enough to deploy, operate, and reason about cost.

> Cost discipline: always use the **Free Tier**, set a billing alarm, and **tear down resources** when done. Knowing how to *not* run up a bill is itself a professional skill.

---

## Week 10 — AWS fundamentals + first deploy
- Cloud concepts; regions/availability zones.
- **IAM** (users, roles, least privilege), **security groups**.
- **EC2:** launch an instance, SSH in, install Python, run a FastAPI app.
- **S3:** store files/artifacts.
- Billing alarms + tearing down.
- Deploy a **small open model** (a small HF model, or **Ollama**) on EC2 and query it.

## Week 11 — Docker, CI, and a live LLM app
- **Docker** basics: Dockerfile, build, run, containerize your app.
- Secrets/env management in the cloud (never bake keys into images).
- **GitHub Actions CI:** run `pytest` on every PR (ties QA + git + cloud together — a green check to show interviewers).
- Managed AI overview: **AWS Bedrock**, **Lambda** (concept + one small hands-on).
- **Project:** take an earlier LLM app (RAG or agent) **fully live on AWS**, containerized, with CI.

---

## Exit criteria
- [ ] Launch, SSH into, and deploy an app on an EC2 instance — then tear it down.
- [ ] Explain IAM roles and security groups at a basic level.
- [ ] Write a Dockerfile and run your app in a container.
- [ ] Set up GitHub Actions to run tests on every PR.
- [ ] Deploy an LLM app to a public URL and explain its cost/latency profile.
- [ ] Manage API keys/secrets safely in a deployed environment.

## Resources
See [RESOURCES.md → Phase 4](../../RESOURCES.md#phase-4--cloud--deployment-aws). Primary: **AWS Getting Started + Free Tier**, **TechWorld with Nana** (Docker/CI), **Docker docs**, **GitHub Actions docs**, **Ollama**.

## Project this phase
- `projects/intermediate/` — a prior LLM app deployed live on AWS with Docker + CI.
