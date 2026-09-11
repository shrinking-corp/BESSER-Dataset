<!--
  AI-GENERATED DOCUMENT
  Generated/modified by: Claude Code (VS Code extension)
  Model used:            Claude Sonnet 5 (claude-sonnet-5)
  Generated at:          2026-09-10
-->

> **AI marking** — This document was generated/modified by **Claude Code (VS Code extension)**,
> using **Claude Sonnet 5** (`claude-sonnet-5`), generated at **2026-09-10**.
> Figures were produced by the scripts cited under [Reproduction](#reproduction) and
> cross-checked against the reports in [`../reports/`](../reports/); the
> interpretation is AI-authored and has not been independently reviewed.

# Coverage taxonomy: 6 types discussed, 4 measured, and why not the other 2

**Status:** 4 types implemented and run dataset-wide via
`scripts/validate_coverage_structural.py` → `structural_coverage_validation`
in `code_metadata.json`.
**Related:** [`DECISIONS.md`](DECISIONS.md) — "Structural test generation and
4-type coverage validator"; complements the pre-existing
`coverage_by_section_validation` key (2026-09-02 entry, structural-vs-hypothesis
split of the *original* `test_hypothesis.py`) — this is a different axis
(*what kind* of coverage) measured against a *different* test suite
(`test_structural_full.py`, this session's deterministic-first generator, see
[`2026-09-10-structural-test-generation.md`](2026-09-10-structural-test-generation.md)).

---

## The 6 types considered

1. **Line/statement coverage** — did we execute this line at all, at least
   once? The most basic measure. Sourced straight from coverage.py's own
   `percent_statements_covered`.
2. **Branch coverage** — for every `if`/`for`/`while`, did execution take
   *both* the true and false path at some point (not just entering the block
   once)? Stricter than line coverage — a line can be "covered" while only
   ever being reached from one direction of a branch. From coverage.py's
   `--cov-branch` mode, `percent_branches_covered`.
3. **Function coverage** — of every `def` in the file, how many got called at
   all (at least one of their lines executed)? Computed via a custom AST scan
   of `python_code.py`'s function ranges, cross-referenced against the
   coverage JSON's executed-lines list — **not** coverage.py's native
   per-function grouping, because that groups by `__qualname__`, which
   silently merges a `@property` getter and its `@x.setter` into one entry
   (both share the same qualified name). Confirmed on `model_1`: 20 real
   `def` statements via AST, only 12 entries in coverage.py's own `functions`
   field.
4. **Structural coverage** — specific to this dataset, not a textbook metric:
   of everything the *diagram* declares (every attribute, every
   generalization, every association), how much did a passing test actually
   verify? The denominator is the true BUML total, not just however many the
   test generator managed to emit a test for — so a class that couldn't even
   be constructed (e.g. a required field typed to an empty enum) correctly
   counts *against* the score instead of being quietly excluded from both
   sides of the ratio.
5. **Condition/MC-DC coverage** *(not implemented)* — stricter than branch
   coverage: verifies every individual boolean sub-expression inside a
   condition gets tested both ways, not just the overall branch outcome
   (e.g. for `if a and b`, did we test all four combinations of `a`/`b`, not
   just "the `if` fired" vs. "it didn't")?
6. **Path coverage** *(not implemented)* — every distinct route through a
   function, considering all combinations of its branches together.

## Why 5 and 6 were not attempted

- **Condition/MC-DC:** no standard, actively-maintained Python tool measures
  this reliably against arbitrary code. This dataset's own bidirectional-
  setter conditionals are exactly the place it would matter most (compound
  `is not None and hasattr(...)`-style guards), so it isn't a hypothetical
  gap — but building a reliable custom instrumenter for it, across 9,082
  structurally varied models, is a much bigger undertaking than the other
  four metrics combined, with no evidence yet that the return justifies that
  cost.
- **Path coverage:** combinatorially explodes even for modest functions with
  a handful of independent conditionals (2ⁿ paths for n conditions) — not a
  realistic target at this dataset's scale. Unlike the other four, there is
  also no meaningful *partial* version of it the way "percent of lines" or
  "percent of branches" naturally exist — it's essentially all-or-nothing per
  function, so it doesn't scale down to a percentage metric across 9,082
  models the way the other four do.

Both remain candidates if a specific downstream need for them emerges; they
were deliberately scoped out of this round rather than silently skipped.

## Reproduction

```bash
python scripts/generate_structural_tests.py --workers 8 --write-metadata  # test_structural_full.py, once
python scripts/validate_coverage_structural.py --workers 8 --write-metadata
```

Sources: [`../reports/structural_coverage_report.json`](../reports/structural_coverage_report.json).
