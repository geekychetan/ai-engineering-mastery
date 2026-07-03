# Week 10 · Day 01 — Cloud concepts + AWS account, Free Tier & billing alarm

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Explain core cloud concepts: regions, availability zones, and the shared-responsibility model.
- [ ] Create an AWS account on the **Free Tier** and, first thing, set a **billing alarm**.
- [ ] Understand what IAM is (and why you shouldn't use the root user for daily work).

## Learn (with resources)
- **AWS Getting Started + Free Tier**: https://aws.amazon.com/getting-started
- YouTube — **freeCodeCamp**, "AWS Certified Cloud Practitioner" (watch the cloud-concepts + IAM intro sections).
- Skim [Phase 4 README](../../../curriculum/phase-4-cloud-aws/README.md).

> **Cost discipline (every AWS day):** stay on the **Free Tier**, keep the billing alarm on, and **tear down** anything you spin up. Not running up a bill is a professional skill.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-01-aws-account`.
2. [ ] Create your AWS account. Enable MFA on the root user. Pick a home region and note it.
3. [ ] **Set a billing alarm** (CloudWatch billing alarm or AWS Budgets) at a low threshold (e.g., $1–$5) with email alerts. Screenshot it.
4. [ ] `projects/intermediate/aws-notes/cloud-concepts.md`: define region, AZ, shared-responsibility model, and Free Tier limits in your own words.
5. [ ] `projects/intermediate/aws-notes/setup-checklist.md`: a reusable "new AWS project" checklist starting with *set billing alarm* and ending with *tear down resources*. Add the billing-alarm screenshot to the folder.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
