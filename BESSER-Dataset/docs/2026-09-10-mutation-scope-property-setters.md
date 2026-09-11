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

# Property-scoped mutation testing: does skipping empty classes/methods matter, and what's left to mutate?

**Status:** script built and smoke-tested (3 models); full 9,082-model
`--write-metadata` run scheduled by the user, completion not yet confirmed in
this document — check `code_metadata.json`'s `mutation_validation_properties`
key / `reports/mutation_properties_report.json` for current status before
citing the full-dataset numbers below as current.
**Related:** [`DECISIONS.md`](DECISIONS.md) — "Property-scoped mutation
testing (`validate_mutation_properties.py`)"; complements the
2026-09-01 mutmut-vs-cosmic-ray entry (mutmut cannot mutate `@property`
methods at all — this is the follow-up question of *how much* of what
cosmic-ray *can* see is actually meaningful).

---

## Motivating question

Almost all of this dataset's `python_code.py` is getter/setter logic (see the
2026-09-10 "zero implemented operations" finding — 19,768 operations, 0
implemented). If mutation testing is dominated by a code shape that's mostly
boilerplate accessors, does the resulting score mean anything, or is it mostly
noise from mutating things too trivial to fail?

## Do empty classes/methods produce mutants at all?

No — and there is **no explicit skip/filter for this anywhere** in either
mutation script. It falls out naturally from what cosmic-ray's 213 operators
can act on: a bare `pass` or a fully empty class body has no operator,
literal, comparison, or branch for any operator to target, so cosmic-ray's
`init` phase generates zero mutation specs for that code region on its own.
Nothing needed to be built to "skip" these — they were never candidates.

The one place this *is* explicit is `validate_coverage_split.py`'s
`find_empty_method_lines()` (2026-09-02 entry) — but that's a coverage-side
exclusion (a trivially-executed stub line shouldn't inflate a percentage), and
it exists precisely *because* coverage counts a line as covered just by
executing it once, a problem mutation testing doesn't share.

## Where does mutable content actually live?

| Code element | Contains mutable content? | How it's handled |
|---|---|---|
| Fully-empty class (`class X: pass`) | Never | Nothing to skip — cosmic-ray's 213 operators generate zero mutants there. No explicit exclusion exists anywhere. |
| Stub `Operation` method (`def op(self): pass`) — the 19,768/19,768-stubbed finding | Never | Same as above — naturally generates nothing. This is the one case `validate_coverage_split.py` *does* explicitly exclude (`find_empty_method_lines()`), but only because coverage counts statements even when trivially executed; mutation testing has no equivalent problem to solve. |
| Plain getter (`@property`, `return self.__x`) — 100% of all getters, dataset-wide | Only via `RemoveDecorator` (strips `@property` itself) | Included in scope for `validate_mutation_properties.py`; near-certain kill (breaks the paired setter's `.setter` decoration). |
| Plain setter (`@x.setter`, plain assignment) — 49.2% of all setters | Only via `RemoveDecorator`, same as getters | Same as getters — included in property scope, but body-wise sterile. |
| Relationship-linked setter (bidirectional `hasattr`/`getattr`/`setattr` wiring) — 50.8% of all setters | Yes — comparisons, conditionals | This is where almost all real mutants come from. |
| `__init__` (default-value `is not None` checks) | Some | In scope for `validate_mutation.py` (whole-file); **deliberately excluded** from `validate_mutation_properties.py`, by design (that's the point of the new scope). |

So, directly: **there is no skip/filter logic for empty classes or stub
methods anywhere in either mutation script.** It's entirely a natural
consequence of what cosmic-ray's operators can act on — nothing exists to
mutate a bare `pass` or a trivial assignment, so those regions simply never
produce mutant candidates in the first place. The only explicit filtering
step in this whole pipeline is `validate_mutation_properties.py`'s
`scope_to_properties()`, and that isn't targeting "emptiness" at all — it
restricts to property/setter line ranges specifically, which happens to
*also* exclude stub methods as a side effect (they were never accessors to
begin with), while still including the sterile getters/plain-setters within
that scope (since structurally they qualify, even though they contribute
nothing but the `RemoveDecorator` case).

## Why build a property-scoped mutation score at all, given ~half of setters are sterile?

Because a whole-file mutation score (`validate_mutation.py`) conflates three
very different things into one number: (1) mutants in dead/stub code that
can't exist (already zero, see above), (2) mutants in sterile accessors that
can only ever die to `RemoveDecorator`, and (3) mutants in real bidirectional-
association logic. A property-scoped score isolates (2)+(3) specifically —
the getter/setter surface that dominates this dataset's actual code — from
whatever `__init__`/operation-level mutants a model happens to have, making
scores comparable across models regardless of how much (or how little)
`__init__` logic each one has.

## Implementation

`scripts/validate_mutation_properties.py` (separate script, not merged into
`validate_mutation.py`, per explicit request so the existing whole-file
metadata/results aren't overwritten):

- `property_line_ranges()` — AST-based; line ranges are decorator-line-inclusive
  (`node.decorator_list[0].lineno`, not `node.lineno`, which excludes
  decorators — the same off-by-decorator bug the whole-file script's
  `RemoveDecorator` attribution needed fixing for earlier).
- `scope_to_properties()` — after `cosmic-ray init` builds its session sqlite
  db, deletes every row whose mutated line falls outside the property/setter
  ranges, *before* the existing `cap_mutants()` sampling step runs.
- Writes to `mutation_validation_properties` in `code_metadata.json` — a
  distinct key from `mutation_validation`, so neither script's results can
  clobber the other's.

## Reproduction

```bash
# Smoke test (3 models):
python scripts/validate_mutation_properties.py --limit 3 --report-name smoke_mutation_properties

# Full dataset:
python scripts/validate_mutation_properties.py --workers 8 --write-metadata
```
