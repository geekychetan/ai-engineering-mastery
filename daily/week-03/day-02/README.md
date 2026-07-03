# Week 03 · Day 02 — OOP more: dunders, properties, light inheritance

**Estimated time:** ~5 hrs
**GitHub issue:** (link the Day-02 issue here)

## Objectives
- [ ] Implement `__str__` and `__repr__` and explain the difference.
- [ ] Use `@property` to expose a computed/validated attribute.
- [ ] Create a simple subclass and override a method (light inheritance + `super()`).

## Learn (with resources)
- **CS50P** — Week 8 (OOP) — the sections on special methods, properties, and inheritance.
- **Corey Schafer** — "Python OOP Tutorial 3: `classmethods`/`staticmethods`" and "Tutorial 4: Inheritance" (YouTube).
- **Real Python** — "Python's `.__repr__()` vs `.__str__()`" and "Property" articles: https://realpython.com

## Homework (branch → PR)
1. [ ] Branch: `git switch -c day-02-oop-more`.
2. [ ] Extend `projects/small/oop/bank_account.py` (or a copy `bank_account2.py`): add `__str__` (human-friendly) and `__repr__` (debug-friendly, unambiguous). Print an instance both ways.
3. [ ] `projects/small/oop/temperature.py`: a `Temperature` class storing Celsius internally, with a `fahrenheit` `@property` (getter + setter) that converts. Validate that temperature can't go below absolute zero in the setter.
4. [ ] `projects/small/oop/shapes.py`: a base `Shape` with an `area()` method, and subclasses `Circle` and `Square` that override it. Use `super().__init__()` where it makes sense. Loop over a list of shapes and print each area.
5. [ ] Push, PR with `Closes #<issue>`, self-review, merge.

## Reflection
- **What clicked:**
- **What's still fuzzy:**
- **One thing to review tomorrow:**
- **Time actually spent:**
