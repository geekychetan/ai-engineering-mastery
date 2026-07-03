# Week 08 · Day 05 — Project: a tool-using agent

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-05 issue here)

## Objectives
- [ ] Write a project brief *before* building (the habit that makes you sound beyond junior).
- [ ] Ship an agent that calls a real API, does a calculation, and returns a **structured** answer.
- [ ] Tie together this week's pieces: tool calling + ReAct loop + pydantic output.

## Learn (with resources)
- Re-skim your Day 01–04 notes; this is a build day, not a lecture day.
- **Anthropic docs** — tool use + structured output (reference as needed): https://docs.anthropic.com
- Pick a free, no-auth (or free-key) API: e.g. a currency-rate, weather, or public-data API.

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-05-agent-project`.
2. [ ] **Brief first:** copy `templates/project-brief-template.md` to `projects/intermediate/tool-agent/BRIEF.md` and fill in the problem, why-AI, approach, and success metric.
3. [ ] `projects/intermediate/tool-agent/tools.py`: at least two tools — one that **calls a real API** (e.g., `get_exchange_rate(base, quote)`) and one that **does a calculation** (e.g., `convert(amount, rate)`).
4. [ ] `projects/intermediate/tool-agent/agent.py`: run the ReAct loop with a `MAX_STEPS` cap, and return the final answer as a validated `pydantic` model (e.g., `ConversionResult` with `amount`, `base`, `quote`, `converted`, `rate_used`).
5. [ ] Demo it end-to-end on a prompt like "Convert 500 USD to INR and tell me the rate you used."
6. [ ] `projects/intermediate/tool-agent/README.md`: what it does, how to run it, and the tools/flow.
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
