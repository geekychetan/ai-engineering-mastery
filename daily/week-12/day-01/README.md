# Week 12 · Day 01 — Choose the capstone + write the brief + architecture diagram

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-01 issue here)

## Objectives
- [ ] Commit to ONE capstone domain that plays to your QA/eval strengths.
- [ ] Write the FULL project brief before writing any code.
- [ ] Draw a clear architecture diagram in Excalidraw and export it into the repo.

## Learn (with resources)
- **Curriculum** — re-read [Phase 5 → Weeks 12-13 capstone spec](../../../curriculum/phase-5-capstone/README.md). Your app = RAG + an agent + an eval suite, containerized, deployed on AWS.
- **Excalidraw** for the architecture diagram: https://excalidraw.com
- **ByteByteGo** (YouTube) — system-design intuition; watch one video and adapt the "boxes + data flow" style to an LLM app.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c week12-day01-capstone-brief`.
2. [ ] Pick the anchor domain and write it down at the top of the brief. Favor your differentiator — recommended: an **LLM-powered QA/testing assistant** (e.g., generates test cases from a requirements doc + triages bug reports against a knowledge base), OR a **RAG assistant with a rigorous eval harness**.
3. [ ] Copy `templates/project-brief-template.md` → `projects/capstone/BRIEF.md` and fill in ALL six sections. Be concrete: name the user, the painful status quo, the model + tools chosen and *why* (cost/latency/quality), and the success metric you'll actually measure.
4. [ ] In section 4, write down the **baseline to beat** and how you'll evaluate (golden set + LLM-as-judge). This is the spine of Week 13 — do not hand-wave it.
5. [ ] Draw the architecture in Excalidraw: ingestion → vector store → retriever → agent/tool layer → LLM → API → UI, plus the eval loop off to the side. Export as PNG **and** the editable `.excalidraw` file to `projects/capstone/docs/architecture.png` and `.../architecture.excalidraw`.
6. [ ] Push, PR with `Closes #<issue>`, self-review the diff (read your own brief critically — is scope realistic for 2 weeks?), merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
