# Week 03 · Day 03 — Error handling

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-03 issue here)

## Objectives
- [ ] Use `try/except/else/finally` correctly and catch specific exceptions (not bare `except`).
- [ ] `raise` exceptions deliberately and read a traceback to locate a bug.
- [ ] Define and raise a custom exception class.

## Learn (with resources)
- **CS50P** — Week 3 (Exceptions) lecture.
- **Corey Schafer** — "Python Tutorial: Exception Handling" (YouTube).
- **Real Python** — "Python Exceptions: An Introduction": https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-03-errors`.
2. [ ] `projects/small/errors/safe_divide.py`: a function that divides two numbers, catching `ZeroDivisionError` and `TypeError` separately with helpful messages, using `else` for the success path and `finally` to print "done".
3. [ ] `projects/small/errors/get_int.py`: prompt the user for an integer in a loop, catching `ValueError` until valid input is given (mirrors the CS50P style).
4. [ ] `projects/small/errors/withdraw.py`: reuse your `BankAccount` idea — define a custom `InsufficientFundsError(Exception)` and `raise` it from `withdraw()` when the balance is too low; catch it at the call site and print a friendly message.
5. [ ] Add a comment to one file explaining, from a QA lens, why catching specific exceptions beats a bare `except:`.
6. [ ] CS50P Week 3 problem set: complete at least one exercise (e.g. `Grocery List` or `Outdated`).
7. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
