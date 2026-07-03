# Week 08 · Day 06 — Guardrails + error handling + weekly review

**Estimated time:** ~4 hrs (lighter day)

**GitHub issue:** (link the Day-06 issue here)

## Objectives
- [ ] Harden the agent against bad inputs, tool failures, and runaway loops.
- [ ] Add clear logging so you can trace what the agent did when something goes wrong.
- [ ] Write the Week 8 review and plan Week 9.

## Learn (with resources)
- **Anthropic docs** — agent reliability / error handling patterns: https://docs.anthropic.com
- Revisit your Week 6 notes on retries, timeouts, and rate limits — the same discipline applies to tool calls.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-06-agent-guardrails`.
2. [ ] In `projects/intermediate/tool-agent/agent.py` add guardrails: (a) validate/clamp tool inputs before calling, (b) wrap each tool call in `try/except` and feed the error back to the model as an observation instead of crashing, (c) enforce `MAX_STEPS` and return a graceful "couldn't complete" message if hit.
3. [ ] `projects/intermediate/tool-agent/test_agent.py`: pytest cases for failure modes — a garbage input, a tool that raises, and a prompt that would loop. Assert the agent degrades gracefully.
4. [ ] Add simple structured logging (step number, tool name, input, output/error) so failures are traceable.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.
6. [ ] **Weekly review:** copy `templates/weekly-review-template.md` into a new GitHub issue titled "Weekly Review — Week 08", fill it in, and update `PROGRESS.md` (mark Week 08 status + days done).

## Reflection
- **Biggest win this week:**
- **What I want to be faster at:**
- **Confidence (1–5): Agents/tools __ · Structured output __ · Shipping __**
- **Time actually spent:**
