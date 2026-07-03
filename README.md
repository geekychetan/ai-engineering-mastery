# AI Engineering Mastery — Zero → Junior AI/LLM Engineer

A 15-week, full-time, project-driven path to becoming a **Junior AI/LLM Engineer** who interviews *above* junior level.

The goal is **applied AI**: frame a problem, pick an AI approach, build it, **evaluate it**, deploy it on AWS, and reason about tradeoffs — not to master ML theory.

---

## Who this is for

A career-changer with an MBA (Business Analytics) and ~4 years across Marketing, Salesforce admin, and Manual QA. Basic Python and some prior git exposure. The QA background is treated as a **superpower** here — it becomes LLM evaluation & testing expertise, which is rare and valuable in junior AI engineers.

## The three habits that make you sound "beyond junior"

1. **Problem-framing first.** Every project starts with a one-page brief (see `templates/project-brief-template.md`): who's the user, what's the problem, why AI, the simplest solution, the success metric, and what could go wrong.
2. **Always evaluate.** Never say "it works." Say "here's how I measured it." Build eval suites, use metrics, show before/after.
3. **Tradeoff fluency.** Talk in cost / latency / quality. Know when to use RAG vs fine-tuning vs a better prompt, and when *not* to reach for a framework.

---

## The 15-week roadmap

| Phase | Weeks | Focus | Detail |
|------|-------|-------|--------|
| 1 | 1-4 | Python + Git Foundations | [curriculum/phase-1-python-git](curriculum/phase-1-python-git/README.md) |
| 2 | 5 | ML & DL Concepts (breadth-only) | [curriculum/phase-2-ml-dl-concepts](curriculum/phase-2-ml-dl-concepts/README.md) |
| 3 | 6-9 | **LLM Engineering Core** (the heart) | [curriculum/phase-3-llm-engineering](curriculum/phase-3-llm-engineering/README.md) |
| 4 | 10-11 | Cloud & Deployment on AWS | [curriculum/phase-4-cloud-aws](curriculum/phase-4-cloud-aws/README.md) |
| 5 | 12-15 | Capstone, Portfolio & Interview Prep | [curriculum/phase-5-capstone](curriculum/phase-5-capstone/README.md) |

**CS50P** ("CS50's Introduction to Programming with Python", Harvard, free) runs in parallel 1–1.5 hr/day, front-loaded into Weeks 1–6.

All learning links live in **[RESOURCES.md](RESOURCES.md)**. Progress is tracked in **[PROGRESS.md](PROGRESS.md)** and on GitHub Issues/Projects.

---

## Time commitment

- **Minimum:** 5 focused hrs/day, 5–6 days/week (keep 1 rest day — burnout kills aggressive plans).
- **Target:** 35–40 hrs/week.
- Below ~25 hrs/week, the 3–4 month goal slips toward ~6 months.

### Daily rhythm

1. **Warm-up (15 min)** — review yesterday's note in `notes/`.
2. **CS50P (60–90 min).**
3. **Core AI learning + build (3–4 hr)** — the day's homework issue.
4. **Commit via PR** — open a PR, self-review, request review.
5. **Reflection (10 min)** — fill the reflection section of the day's README.
6. **Weekly** — open a `weekly-review` issue: wins, gaps, next-week adjustments.

---

## How we track progress (the real SWE workflow)

You learn git/GitHub *by using it every day*, not by drilling it.

- **Each study day = a GitHub Issue** with a homework checklist (label `daily` + `week-NN`).
- **Every task is a branch → Pull Request → review → merge.** Merging closes the issue.
- **GitHub Project board (Kanban):** `Backlog · This Week · In Progress · In Review · Done`.
- **Milestones:** one per phase, so progress rolls up visibly.
- From Phase 4, **GitHub Actions** runs `pytest` on every PR — a green check you can point to in interviews.

### Daily loop cheat-sheet

```bash
git switch -c day-01-setup        # branch for the day/task
# ...do the homework, make commits...
git add -A && git commit -m "day 01: environment + first script"
git push -u origin day-01-setup
gh pr create --fill               # open a PR
# self-review the diff on GitHub, then:
gh pr merge --squash --delete-branch   # closes the linked issue
```

Link a PR to its issue by writing `Closes #<issue-number>` in the PR description.

---

## Repo layout

```
curriculum/   # phase-by-phase syllabus + resources
daily/        # week-NN/day-NN/README.md — objectives, homework, reflection
projects/     # small → intermediate → capstone builds
notes/        # her own concept notes (great for interview review)
templates/    # daily README, project brief, weekly review
.github/      # issue + PR templates
```

---

## Start here

New to this planner? Read **[GETTING_STARTED.md](GETTING_STARTED.md)** first — a self-contained quickstart.

1. Read [GETTING_STARTED.md](GETTING_STARTED.md), then skim this README and [PROGRESS.md](PROGRESS.md).
2. Open [curriculum/phase-1-python-git](curriculum/phase-1-python-git/README.md).
3. Go to [daily/week-01/day-01](daily/week-01/day-01/README.md) and begin.
