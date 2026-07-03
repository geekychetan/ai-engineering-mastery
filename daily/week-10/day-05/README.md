# Week 10 · Day 05 — S3 basics + use an object from your app

**Estimated time:** ~5 hrs

**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Create an S3 bucket and upload/download objects (console + `boto3`).
- [ ] Read an object from S3 inside a small Python app.
- [ ] Understand bucket privacy defaults (keep it private — no public buckets).

## Learn (with resources)
- **AWS Getting Started** — "Store files in S3" tutorial: https://aws.amazon.com/getting-started
- `boto3` docs (S3 client: `put_object`, `get_object`, `download_file`): search "boto3 S3".
- YouTube — **freeCodeCamp** AWS course (S3 section).

> **Cost discipline:** S3 Free Tier covers small storage/requests. Keep buckets **private**. Delete objects + the bucket when done to avoid lingering storage costs.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-s3-basics`.
2. [ ] Create a private S3 bucket. Upload a file via the console, then download it — confirm the round trip.
3. [ ] `projects/intermediate/aws-s3/s3_demo.py`: use `boto3` to upload a local file, list bucket contents, and download it back. Read credentials from your configured AWS profile (not hard-coded keys).
4. [ ] `projects/intermediate/aws-s3/use_object.py`: have a tiny app fetch an object from S3 (e.g., a prompt template or a golden-set file) and use it — showing S3 as app config/data storage.
5. [ ] `projects/intermediate/aws-s3/README.md`: what you built + teardown steps.
6. [ ] **Tear down:** delete the objects and the bucket. Confirm it's gone.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
