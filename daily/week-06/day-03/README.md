# Week 06 · Day 03 — Few-shot prompting + structured JSON output

**Estimated time:** ~5 hrs (1 hr learn + 4 hr build)
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Use few-shot examples to steer format and behavior.
- [ ] Get reliable structured/JSON output back and parse it in Python.
- [ ] Write a strong system prompt that sets role, rules, and output contract.

## Learn (with resources)
- **DeepLearning.AI short course** — "ChatGPT Prompt Engineering for Developers": the "Inferring" and "Transforming" lessons (structured extraction).
- **Anthropic docs** — Prompt engineering: "Use examples (multishot prompting)", "Increase output consistency (JSON)", and system prompts: https://docs.anthropic.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-fewshot-json`.
2. [ ] Create `projects/intermediate/prompting/extract.py` — a "review analyzer" that takes a product/support review and returns **JSON** with fields `sentiment` ("positive"/"neutral"/"negative"), `topics` (list), and `urgent` (bool).
   - Use a **system prompt** defining the role + the exact JSON schema.
   - Include **2–3 few-shot examples** in the prompt.
   - Parse the response with `json.loads()` and print the parsed dict; handle a parse failure gracefully.
3. [ ] Run it on 5 sample reviews (put them in `projects/intermediate/prompting/samples.txt`) and save the outputs.
4. [ ] Add a note in `projects/intermediate/prompting/notes.md`: what happened without few-shot examples vs with them, and any time the JSON came back malformed.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
