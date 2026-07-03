# Week 10 · Day 02 — IAM (users, roles, least privilege) + security groups

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Create an IAM user for daily use (stop using root) and understand users vs roles.
- [ ] Explain **least privilege** and attach only the policies you actually need.
- [ ] Understand what a **security group** is (a virtual firewall) and how inbound rules work.

## Learn (with resources)
- **AWS Getting Started** — IAM tutorials: https://aws.amazon.com/getting-started
- YouTube — **freeCodeCamp**, "AWS Certified Cloud Practitioner" (IAM + networking/security-groups sections).

> **Cost discipline:** nothing here should incur charges, but keep the billing alarm on and confirm you created no stray resources.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-iam-security`.
2. [ ] Create an IAM **user** with console + programmatic access for your own daily work; attach a scoped policy (not `AdministratorAccess` if you can avoid it). Configure the AWS CLI with its access key.
3. [ ] Read about an IAM **role** (assumed by a service like EC2) and note how it differs from a user (no long-lived keys).
4. [ ] `projects/intermediate/aws-notes/iam-security-groups.md`: explain users vs roles, least privilege, and security groups; include an example inbound rule (e.g., allow SSH port 22 from *your IP only*, not `0.0.0.0/0`).
5. [ ] Verify the CLI works: `aws sts get-caller-identity`. Paste the (redacted) output into your notes.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
