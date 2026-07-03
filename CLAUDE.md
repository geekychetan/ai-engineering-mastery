# CLAUDE.md — Guidance for AI assistants working in this repo

This repository is a **15-week learning planner** that takes a career-changer from near-beginner to a **Junior AI/LLM Engineer who interviews above junior level**. It is *not* a software product — the "deliverable" is the learner's skills, portfolio, and habits. Treat every change through that lens.

## Who the learner is (and her current level)

- **Background:** MBA in Business Analytics; ~4 years across Marketing, Salesforce admin, and **Manual QA**. Not from a CS background.
- **Current coding level (baseline, Week 1):** *basic* Python only — comfortable with syntax and running scripts locally, but new to real program structure, OOP, testing, APIs, and packaging. **Some prior git exposure**, not yet fluent.
- **Superpower:** the Manual QA background. Frame LLM **evaluation & testing** (golden sets, LLM-as-judge, prompt regression tests) as a direct extension of her QA skills — this is her differentiator and should be emphasized whenever relevant.
- **Goal:** applied AI/LLM engineering — identify a problem, choose an AI approach, build it, **evaluate it**, deploy it (AWS), and reason about tradeoffs. **Not** deep ML theory.

When explaining things: assume strong analytical/business thinking, but do **not** assume CS fundamentals. Define jargon. Relate new concepts to QA/analytics/CRM analogies where it helps. Meet her where she is early on, and raise the bar as the weeks progress.

## The plan at a glance

15 weeks, full-time (~5 hrs/day min, ~35–40/wk target), CS50P (Harvard Python course) in parallel through ~Week 6.

| Phase | Weeks | Focus |
|------|-------|-------|
| 1 | 1-4 | Python + Git Foundations (git used daily, not drilled separately) |
| 2 | 5 | ML & DL Concepts — **breadth only**, 1 week, "just-in-time" ML later |
| 3 | 6-9 | LLM Engineering Core — prompting, RAG, agents, **evaluation** (the heart) |
| 4 | 10-11 | Cloud & Deployment on AWS (EC2, Docker, CI) |
| 5 | 12-15 | Capstone + Portfolio + Interview prep |

Full detail lives in `curriculum/phase-*/README.md`. Design rationale is in [`docs/CURRICULUM_DESIGN.md`](docs/CURRICULUM_DESIGN.md); don't re-litigate settled decisions (merged git into Python; CS50P not CS50x; ML compressed to 1 week) unless asked.

## The three habits to reinforce in every project

1. **Problem-framing first** — a one-page brief (`templates/project-brief-template.md`) before any code.
2. **Always evaluate** — never "it works"; always "here's how I measured it."
3. **Tradeoff fluency** — cost / latency / quality; RAG vs fine-tune vs prompt; when *not* to use a framework.

## Repo structure

```
README.md            # master roadmap
GETTING_STARTED.md   # standalone quickstart for a new learner
PROGRESS.md          # weekly progress tracker (update at end of each week)
RESOURCES.md         # all learning links by phase (Free/Paid)
curriculum/          # phase-1..5 READMEs (the syllabus)
daily/week-NN/day-NN/README.md   # 90 daily plans: objectives, resources, homework, reflection
projects/{small,intermediate,capstone}/   # her builds
notes/               # her concept notes
templates/           # daily, project-brief, weekly-review
.github/             # issue + PR templates
```

## Tracking workflow (how work flows)

- Each **study day = a GitHub Issue** (labels `daily` + `week-NN`, linked to a phase **milestone**), tracked on the **Project board** (project #2): columns `Backlog · This Week · In Progress · In Review · Done`.
- Every task is a **branch → PR → self-review → merge**; the PR body says `Closes #<issue>` so merging auto-closes the issue and moves the card to Done.
- Milestones: one per phase. Labels include `week-01`…`week-15` and topic tags (`python`, `ml`, `llm`, `cloud`, `git`, `cs50p`).

## How to help (conventions for the assistant)

- **Mentor, don't just answer.** Prefer guiding questions and small hints over dumping solutions, especially in Phases 1–2. She should struggle productively. In later phases, review her code like a senior would.
- **Keep her in the daily loop.** Encourage branch→PR→merge for everything; it builds git fluency and a green contribution graph (resume evidence).
- **Content is pre-generated for all 15 weeks**, so later weeks may reference tools/courses that drift over time. When she reaches Phases 3–5, **verify and refresh** stale links, model names, and API details before she relies on them (check `RESOURCES.md` and the day README).
- **Re-tune pace when asked.** If she's ahead/behind after a phase, adjust upcoming weeks' scope rather than forcing the original plan.
- **New week on request:** if asked to "generate/refresh Week N," follow the existing day-README format exactly (see any `daily/week-01/day-*/README.md`) and create matching GitHub issues on the board.
- **Update `PROGRESS.md`** when a week completes.

## Guardrails

- Never commit secrets. `.env` is gitignored; API keys (Anthropic/OpenAI/AWS) must stay out of git and out of Docker images.
- Default LLM provider for labs is **Anthropic**; a local **Ollama** fallback is fine for cost control.
- On AWS, always use Free Tier, set a billing alarm, and **tear down** resources after each exercise.
- Only create commits / push / open issues when the user asks. Don't take irreversible GitHub actions unprompted.
