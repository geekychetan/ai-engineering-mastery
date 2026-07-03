# Week 10 · Day 03 — EC2: launch, SSH in, run a script, terminate

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Launch a **Free Tier** EC2 instance (e.g., `t2.micro`/`t3.micro`) with a key pair and a scoped security group.
- [ ] SSH in, install Python, and run a small script on the instance.
- [ ] **Stop and terminate** the instance and confirm nothing is left running.

## Learn (with resources)
- **AWS Getting Started** — "Launch a Linux virtual machine" (EC2) tutorial: https://aws.amazon.com/getting-started
- YouTube — **freeCodeCamp**, "AWS Certified Cloud Practitioner" (EC2 section).

> **Cost discipline:** `t2.micro`/`t3.micro` on Free Tier only. Security group: SSH (22) from **your IP only**. **Terminate the instance at the end of the day** — a forgotten instance is the #1 surprise bill.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-ec2-first-run`.
2. [ ] Launch a Free Tier Amazon Linux/Ubuntu `t2.micro`; create/download a key pair; set the security group to allow SSH from your IP.
3. [ ] SSH in (`ssh -i key.pem user@public-ip`), then install Python/pip and copy up a small script (e.g., your Week 1 `hello.py`) and run it on the box.
4. [ ] `projects/intermediate/aws-ec2/ec2-runbook.md`: step-by-step of what you did — launch flags, SSH command, install commands, and the **teardown** steps.
5. [ ] **Tear down:** stop, then terminate the instance; delete the key pair if unneeded. Confirm in the console that no instances are running and add a note in the runbook.
6. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
