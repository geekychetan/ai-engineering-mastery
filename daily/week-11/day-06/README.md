# Week 11 · Day 06 — Bedrock + Lambda overview · Phase 4 retro · weekly review

**Estimated time:** ~4 hrs (lighter day)

**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Explain what **AWS Bedrock** (managed foundation models) and **Lambda** (serverless functions) are and when you'd reach for each.
- [ ] Do one small hands-on: invoke a model via Bedrock **or** run a "hello" Lambda.
- [ ] Close out Phase 4 with a retro and write the Week 11 review.

## Learn (with resources)
- **AWS Getting Started** — Bedrock + Lambda intros: https://aws.amazon.com/getting-started
- YouTube — **freeCodeCamp** AWS course (serverless/Lambda section).
- **Anthropic docs** — Claude on Bedrock (reference): https://docs.anthropic.com

> **Cost discipline:** Bedrock model calls and Lambda both have Free-Tier-friendly small usage — keep it tiny. Remove any test functions/roles when done. Keep the billing alarm on.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-bedrock-lambda`.
2. [ ] Pick ONE small hands-on: (a) enable a model in Bedrock and invoke it once from `boto3`, printing the reply; **or** (b) create a tiny Python Lambda that returns a JSON greeting and test it in the console.
3. [ ] `projects/intermediate/aws-bedrock-lambda/notes.md`: what Bedrock and Lambda are, when to use managed vs self-hosted vs serverless, and how today's hands-on went.
4. [ ] Clean up: delete the test Lambda/role or disable the Bedrock access if unneeded.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.
6. [ ] **Phase 4 retro:** reflect on the Phase 4 exit criteria — can you launch+tear down EC2, explain IAM/security groups, write a Dockerfile, run CI on PRs, and deploy an LLM app to a public URL while managing secrets and cost?
7. [ ] **Weekly review:** copy `templates/weekly-review-template.md` into a new GitHub issue titled "Weekly Review — Week 11", fill it in, and update `PROGRESS.md` (mark Week 11 + Phase 4 complete).

## Reflection
- **Biggest win this phase:**
- **What I want to be faster at:**
- **Confidence (1–5): Docker __ · CI/CD __ · Cloud deploy + cost __**
- **Time actually spent:**
