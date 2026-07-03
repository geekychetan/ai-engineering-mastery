# Getting Started — How to Use This Planner

A self-contained guide to go from near-beginner to **Junior AI/LLM Engineer** in **15 weeks** of full-time study. If you're picking this up cold, read this once, then start Week 1 Day 1.

---

## 1. What this is

A day-by-day, project-driven curriculum. You learn by **building and shipping**, tracking every day of work as a GitHub Issue and every piece of homework as a Pull Request — the same workflow real engineers use. By the end you have skills, a portfolio, and a green GitHub graph to show for it.

The goal is **applied AI**: frame a problem → pick an approach → build it → **prove it works with evaluation** → deploy it → talk about tradeoffs. Not ML theory.

## 2. What you need before Day 1

- A computer (macOS/Linux/Windows), internet, and ~5 focused hours/day.
- A **GitHub account** (free).
- Willingness to be confused and push through — that's the job.

Everything else (Python, VS Code, git, API keys, AWS) gets set up *inside* the curriculum, starting Day 1.

## 3. How much time

- **Minimum:** 5 focused hours/day, 5–6 days/week (keep **one rest day** — burnout ends aggressive plans).
- **Target:** 35–40 hours/week.
- Do less than ~25 hrs/week and the 3–4 month timeline stretches toward 6 months. That's fine — just know the tradeoff.

Daily split: ~1–1.5 hr **CS50P** (Harvard's free Python course, runs in parallel through ~Week 6) + ~3.5–4 hr building.

## 4. The 15-week map

| Phase | Weeks | You'll learn to… |
|------|-------|------------------|
| 1 | 1-4 | Write real, tested Python; use git/GitHub daily |
| 2 | 5 | Speak ML/DL fluently (breadth only) |
| 3 | 6-9 | Build LLM apps: prompting, RAG, agents, **evaluation** |
| 4 | 10-11 | Deploy on AWS with Docker + CI |
| 5 | 12-15 | Ship a capstone, build a portfolio, prep interviews |

Detail per phase: [`curriculum/`](curriculum/). All learning links: [`RESOURCES.md`](RESOURCES.md).

## 5. Your daily loop (do this every study day)

1. **Warm-up (15 min):** skim yesterday's note in [`notes/`](notes/).
2. **CS50P (60–90 min):** the day's lecture/problem set.
3. **Open today's issue:** find it on the [Project board](https://github.com/users/geekychetan/projects/2) in **This Week**, and open its plan file at `daily/week-NN/day-NN/README.md`.
4. **Do the homework on a branch (3–4 hr):**
   ```bash
   git switch -c week01-day01-setup      # a branch for today
   # ...write code, make small commits...
   git add -A && git commit -m "day 01: environment + first script"
   git push -u origin week01-day01-setup
   gh pr create --fill                   # write "Closes #<issue-number>" in the body
   ```
   Open the PR on GitHub, **review your own diff** (this catches half your bugs), then merge:
   ```bash
   gh pr merge --squash --delete-branch  # merging auto-closes the linked issue
   ```
5. **Reflection (10 min):** fill the reflection section at the bottom of the day's README.

Move the issue card across the board as you go: **This Week → In Progress → In Review → Done**.

## 6. Your weekly loop

At the end of each week:
- Copy [`templates/weekly-review-template.md`](templates/weekly-review-template.md) into a new GitHub Issue titled `Weekly Review — Week NN`, and fill it in honestly.
- Update [`PROGRESS.md`](PROGRESS.md) (mark days done + status).
- Ahead or behind? Adjust next week's load — the plan serves you, not the other way around.

## 7. The three habits that make you sound "beyond junior"

Bake these into **every** project:
1. **Problem-framing first** — write a one-page brief ([`templates/project-brief-template.md`](templates/project-brief-template.md)) *before* coding: who's the user, what's the problem, why AI, simplest solution, success metric, what could go wrong.
2. **Always evaluate** — never say "it works." Say "here's how I measured it" (golden set, metrics, before/after).
3. **Tradeoff fluency** — talk in cost / latency / quality; know when to use RAG vs fine-tuning vs a better prompt, and when *not* to reach for a framework.

## 8. Where everything lives

```
README.md          # the full roadmap
GETTING_STARTED.md # this file
curriculum/        # what you learn each phase
daily/             # your day-by-day plans + homework
projects/          # what you build (small → intermediate → capstone)
notes/             # your own concept notes
templates/         # briefs, reviews, daily template
RESOURCES.md       # every course/video/doc link, by phase
PROGRESS.md        # your progress tracker
```

## 9. Start now

1. Read [`README.md`](README.md) once for the big picture.
2. Open [`curriculum/phase-1-python-git/README.md`](curriculum/phase-1-python-git/README.md).
3. Go to [`daily/week-01/day-01/README.md`](daily/week-01/day-01/README.md) and begin.

The only wrong move is not starting. Ship something small today.
