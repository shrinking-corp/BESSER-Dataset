<!--
  AI-GENERATED DOCUMENT
  Generated/modified by: Claude Code (VS Code extension)
  Model used:            Claude Sonnet 5 (claude-sonnet-5)
  Generated at:          2026-09-16
-->

> **AI marking** — This document was generated/modified by **Claude Code (VS Code extension)**,
> using **Claude Sonnet 5** (`claude-sonnet-5`), generated at **2026-09-16**.
> Interpretation is AI-authored and has not been independently reviewed.

# Tree-sitter-based generator fidelity and class coverage

**Status:** both scripts run full-dataset, results current as of 2026-09-16.
**Related:** [`DECISIONS.md`](DECISIONS.md) — same-day entries; builds on the
colleague's `scripts/extract_structure.py` + `scripts/generate_code_structure.py`
(tree-sitter, already run full-dataset, 9,081/9,082 extracted into a
per-model `code_structure.json`).

---

## Why tree-sitter's output is useful here

`code_structure.json` reads `python_code.py`'s actual syntax tree — classes,
methods, attributes, bases, decorators — directly, independent of both the
BUML model (`model_metadata.json`, via `besser`) and of this project's own
test generator's name-resolution logic. That independence is what makes two
new checks possible that weren't before.

## 1. `scripts/validate_generator_fidelity.py`

Cross-references `model_metadata.json` (what the diagram declares) against
`code_structure.json` (what the generated code actually has) — a
comparison that had never been made before, since the two files come from
completely different tools (`besser` vs. tree-sitter) reading completely
different artifacts (BUML source vs. generated Python).

Three fields are directly comparable (`classes`, `abstract_classes`,
`enumerations`/`enum_classes`); two more (`attributes`, `methods`) are
reported but never flagged as mismatches, because a mismatch there is
*expected* — model-side attribute/method counts only cover BUML-declared
ones, while tree-sitter counts every `self.x = ...` assignment and every
method including generated `@property`/`@x.setter` accessors and
association-derived fields.

**Run: 9,081/9,082 compared, 40.87% mismatch rate (3,711 models)** on the
three directly-comparable fields. `classes` mismatches average +0.99
(code has slightly more classes than the model, nonzero for 2,830 models) —
largely explainable by generator-side stub/helper classes not present in
the BUML count. `abstract_classes` mismatches average **-1.56** (code has
*fewer* abstract classes, nonzero for 1,960 models) — the significant one.

**Confirmed root cause, on `model_100127`:** BUML declares
```python
relationaldatabase_NamedElement = Class(name="relationaldatabase_NamedElement", is_abstract=True)
```
but the generated code is:
```python
class relationaldatabase_NamedElement(Taggable):
```
No `ABC`, no `@abstractmethod` anywhere. **The code generator never
implements UML's "abstract" concept in Python at all** — it silently drops
the flag for every abstract class, unconditionally. This is the root cause
behind the earlier, independently-found "0/732 methods are actually
`@abstractmethod`" observation (see the 2026-09-10 structural-test-generation
entry) — that finding described the *symptom* (nothing blocks direct
instantiation); this one confirms the *mechanism* (the generator never
tries to enforce abstractness in the first place).

One isolated data artifact found and ruled out during this check:
`model_10006`'s `code_structure.json` reports zero classes despite
`python_code.py` genuinely having eight — confirmed via direct grep this is
the only such case (1 of 2,830 classes-mismatches), not a systemic
extraction problem.

## 2. `scripts/validate_class_coverage.py`

Of every class tree-sitter finds in `python_code.py`, what fraction got at
least one **passing** test — a class counts as covered if any passing test
references it via a direct constructor call (`ClassName(...)`) or an
`isinstance()`/`issubclass()` check, detected via a single AST walk per test
function. Denominator is tree-sitter's class list specifically because it's
independent of the BUML model and of this project's own generator's
name-resolution quirks. Supports `--test-file`/`--metadata-key` the same way
as the other validators (`TEST_FILE_METADATA_KEYS`).

| Suite | Measured | Avg class coverage |
|---|---|---|
| New (`test_structural_full.py`) | 9,043/9,082 | 93.64% |
| Old (`test_hypothesis.py`) | 8,259/8,368 | 95.96% (109 timeouts, same Hypothesis-variance class as elsewhere) |

(New suite's run predates the exclusion-list updates and used the full
9,082, not `usable_models.txt` — the two numbers aren't yet on the same
denominator; noted for the final consolidated comparison.)

## A process bug worth remembering: report-name is not test-file

Running class coverage for both suites used the **same default
`--report-name class_coverage_report`** for both invocations. The second
run's cache-resume logic found "9,082/9,082 already done" from the *first*
run and reused those results verbatim under the new
`class_coverage_validation_hypothesis` key — meaning every model's supposed
old-suite class coverage was silently a byte-for-byte copy of the new
suite's data (confirmed: identical `checked_at` timestamps and values in
`model_1`'s `code_metadata.json`). `--test-file` itself worked correctly;
nothing tied the cache to *which* test file was measured. Fixed by using a
distinct `--report-name` per test file and re-running for real. **Not yet
fixed at the code level**: the script should probably default its
report-name to include the test-file so this can't silently recur — noted,
not built as of this writing.

## Reproduction

```bash
python scripts/validate_generator_fidelity.py --workers 24 --write-metadata
python scripts/validate_class_coverage.py --workers 24 --write-metadata
python scripts/validate_class_coverage.py --test-file test_hypothesis.py --report-name class_coverage_hypothesis_report --workers 24 --write-metadata
```
