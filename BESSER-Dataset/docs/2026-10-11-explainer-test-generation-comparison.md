# Raising mutation score: library-generated tests vs. our own generator, explained simply

> **Correction (2026-10-18).** The earlier versions of this document reported a
> super-suite score of **92.66%** (+41.81 pts over a 50.85% baseline). That was
> wrong. Many of the test files contained tests that fail even on the original,
> unmodified code, and our mutation tool counts *any* failing test run as
> "mutant caught" -- so those models got a fake perfect score. Nothing in our
> measurement checked for this. After fixing it (every suite now has to pass on
> the original code before it is measured), the honest numbers are:
> **super suite 77.55%, baseline 34.52%, lift +43.03 pts**, with 188 of 200
> models improved and none worse. The improvement holds -- it's actually a
> little bigger, because the baseline was inflated even more than the super
> suite. The full story is in "What went wrong, and the honest numbers" below.

## The problem we're solving

Mutation score across this dataset's test suites had been stuck around
35–44%, no matter which suite (old/new/combined) or scope (whole-file/
property-only) we measured. We'd already root-caused why: most generated
tests check that an object *exists* and has the *right type*, not that its
logic actually *behaves* correctly — and where a test does check a value,
it's usually one fixed example, never anything that would catch a subtly
wrong calculation or comparison.

So instead of trying to raise test *coverage* further (already shown that
doesn't move mutation score much), we tried **targeted test generation**:
pointing specific tools and techniques directly at the methods that have
real logic, and comparing what each one actually achieves.

## The four approaches, in plain terms

- **Baseline**: the test suite we already had going into this comparison
  (`test_combined.py` — our dataset's original generated tests plus our
  own earlier structural generator, merged and deduplicated).
- **Pynguin**: an external library that *searches* for good test cases
  using a genetic algorithm — it doesn't know anything about this
  dataset's code in advance, it just mutates and evolves candidate tests
  until they cover more of the code / catch more bugs.
- **CrossHair**: a different external library that uses *symbolic
  execution* — instead of guessing test inputs, it mathematically reasons
  about what input would make an assertion fail, and generates exactly
  that concrete counterexample.
- **Behavioral**: a small generator we built ourselves, for one specific,
  diagnosed gap. We traced a real surviving (uncaught) mutant on one model
  back to its root cause: when two classes are linked in both directions
  (e.g. a `Node` has a `next`, and that `next` has a `previous` pointing
  back), our existing tests only ever triggered the link from *one* side
  and trusted the other side to update as a side effect. Behavioral adds
  one new kind of test: call the setter from *both* ends independently.

## Why the fair comparison needed a correction

The first, naive comparison was: each tool's own score vs. baseline's
score averaged across all 200 sample models. That's unfair, because
Pynguin and CrossHair couldn't generate anything at all for every model —
only 192/200 and 177/200 respectively (some models have no plain
"operation" methods for Pynguin to target; some classes are property-only,
which CrossHair structurally cannot reach at all). Comparing a tool's
score on its own easier subset against baseline's score on the *full,
harder* 200 isn't a fair test of either side.

**The fix: compare each tool's score against baseline's score on that
exact same subset.** This reversed part of the naive conclusion.

## The headline numbers

**Honest numbers (2026-10-18, every suite checked to pass on the original code first):**

| Approach | Measured | Score | Baseline, same models | Difference |
|---|---:|---:|---:|---:|
| Baseline | 200/200 | **34.52%** | — | — |
| **Super suite (all three combined)** | 200/200 | **77.55%** | 34.52% | **+43.03 pts** |

**Original table, kept for the record -- these numbers are inflated** (measured
before the fix; several suites contained tests that fail on the original code):

| Approach | Measured | Standalone score | Baseline, same models | Difference |
|---|---:|---:|---:|---:|
| Baseline | 200/200 | ~~50.85%~~ | — | — |
| Behavioral (additive) | 200/200 | ~~59.89%~~ | ~~50.85%~~ | ~~+9.0 pts~~ |
| Pynguin | 192/200 | ~~27.75%~~ | ~~51.54%~~ | ~~−23.79 pts~~ |
| CrossHair | 173/200* | ~~64.24%~~ | ~~52.12%~~ | ~~+12.93 pts~~ |
| Super suite | 200/200 | ~~92.66%~~ | ~~50.85%~~ | ~~+41.81 pts~~ |

The individual Behavioral / Pynguin / CrossHair rows weren't re-measured; the
qualitative conclusions below (Pynguin's assertions are too weak, combining
beats choosing) still match what we saw, but treat their exact percentages as
unreliable.

\* CrossHair's real count: a data-quality bug was found and fixed along the
way — 4 of its original 177 "successful" models had a syntax error in
their own generated test file (CrossHair occasionally writes a raw object
reference into a test instead of a usable value), which cosmic-ray
misread as "every mutant was caught" when really the test file couldn't
even run. Those 4 fake-perfect scores were removed; corrected average
64.24% on 173 genuinely-valid models.

**Pynguin loses, badly, even on its own best-case subset.** This confirms
the root cause directly: without being told otherwise, Pynguin's default
assertions are `isinstance(...)`-only — exactly the same weak pattern the
dataset already had, not an improvement.

**CrossHair wins on average — but it's genuinely a mixed bag per model.**
Measured standalone (replacing baseline outright), CrossHair *helps* 72
models and *hurts* 65 of them, out of the 177 it could generate anything
for. The reason: CrossHair's suite doesn't know what the baseline already
tests, so swapping it in for baseline entirely means losing baseline's own
real coverage of things CrossHair doesn't happen to check.

**Behavioral never hurts a single model, across all 200** — because it's
purely additive, only ever adding new tests on top of what's already
there, never replacing anything.

## The real fix: combine instead of choosing one

The mixed-bag problem above is specifically an artifact of *replacing*
baseline with CrossHair's output. The obvious fix: don't replace, merge —
baseline + Behavioral + CrossHair's tests, all in one file. We built that
("the super suite") and measured it for real:

~~**First measured: 77.59% average, a +26.74 point lift over baseline on
the full 200-model sample — and 123 models improved, 0 worsened, 77
unchanged.**~~ *(Inflated -- see the correction at the top.)*

Combining preserves Behavioral's "never hurts" property even with
CrossHair's real mixed-bag tendencies folded in, because nothing from
baseline ever gets removed — only added to. That part held up in the honest
re-measurement: 188 models improved, 0 worsened, 12 unchanged.

## A second jump that turned out to be partly fake: 77.59% → 92.66%

We'd been treating a chunk of surviving mutants as a permanent, accepted
limit — not a bug, just a structural fact of this dataset we couldn't do
anything about. That turned out to be wrong, and fixing it is most of
where the extra 15 points above came from.

**The situation**: some models declare a relationship between two classes
where only one side is actually *implemented* in the generated code — the
other side is a bare, empty stub, like `class Arc: pass`. The real side's
code tries to keep both ends in sync ("if the other object has this
attribute, update it too"), but since the stub genuinely has nothing on
it, that check is always false. It's not that our tests fail to trigger
this logic — it's that the logic itself never has anything to do, for
*any* test, because the thing it's checking for doesn't exist on the stub
object at all. We'd traced this exact mechanism months earlier and
concluded, reasonably at the time, that nothing could kill mutants hiding
inside it.

**What we missed**: nothing stops a test from *giving* the stub object
that missing attribute itself, by hand, before using it. In plain terms —
if a delivery driver's job is "check if this address has a mailbox, and
if so put the package in it," and we're testing with a house that has no
mailbox, of course nothing happens. But we can tape a mailbox to the
house ourselves before the test starts. That doesn't change what's real
about the house — it's still testing the driver's actual behavior (does
the package correctly go in when the mailbox IS there), using a
stand-in built just enough to make that checkable. This is an entirely
normal thing to do in testing — it's called a *test double*: when a real
collaborator doesn't do what your code expects, you build a minimal
stand-in instead of giving up.

**The fix**: we added a new rule to our test generator — whenever one
side of a relationship is a stub, construct it, manually attach the
attribute a real implementation would have had, then exercise the real
side's logic and check the stand-in's attribute updates correctly. No
LLM involved — once the mechanism was understood, it's a deterministic,
hand-written rule, the same way the original behavioral-test idea became
a permanent rule once diagnosed by hand.

**Result**: on the one model we traced this on by hand, the score for
that model went from 35% (baseline) → 42.5% (first behavioral fix) → 95%.
That result is genuine. Across the full 200-model sample we then reported
77.59% → 92.66% -- **that part was not genuine**, see the next section.

## What went wrong, and the honest numbers

**The trap.** The mutation tool decides "this mutant was caught" when the
test run fails. If a test fails *even on the original, unmodified code*, every
single mutant looks caught and the model gets a perfect score that means
nothing. Our measurement never checked that the tests pass on the original
code first. Running every sample model's super suite once, unmodified, showed
155 of 200 failing.

**Four separate causes**, each from a different source:
1. **Our stub-double tests checked the wrong thing for some shapes.** They
   asserted "the stand-in now points to the owner", which is right when the
   stand-in holds one object -- but when it holds a *collection*, the real
   code puts `{owner}` there, so the test failed every time. We had verified
   the rule by hand on one model whose relationships all happen to be
   single-object, and assumed it held everywhere.
2. **CrossHair wrote tests of Python's own `Enum` class** (not our code), checking
   an exact error message that differs between Python versions.
3. **CrossHair used dates without importing the date module.**
4. **The dataset's own original tests deliberately fail on empty methods** --
   they're there to flag `# TODO: Implement` stubs, not to test behavior. Since
   they're in the baseline too, the *baseline* score was inflated as well.

**The fix.** (1) The mutation tool now runs every suite once on the original
code first and refuses to score a suite that fails -- this catches the
problem no matter where it comes from. (2) Each final test file is "green by
construction": tests that fail on the original code are removed and listed,
and the baseline gets exactly the same treatment so the comparison stays fair.
(3) The CrossHair and stub-double generators were fixed so good tests aren't
thrown away. In the end only the dataset's own empty-method checks (441 tests,
identical in both suites) had to be removed.

**Honest result (200 models, each suite verified to pass on the original code):**

| | Before the fix (inflated) | Honest |
|---|---:|---:|
| Baseline | 50.85% | **34.52%** |
| Super suite | 92.66% | **77.55%** |
| Lift | +41.81 pts | **+43.03 pts** |

Per model: **188 improved, 0 worsened, 12 unchanged**. Perfect scores fell from
157 to 3 in the super suite and from 49 to 0 in the baseline -- the old perfect
scores were almost all fake.

## The recommendation

**Keep Behavioral and CrossHair, merged into one suite. Drop Pynguin.**
This isn't really a choice between the two winners — they target different
parts of the problem (bidirectional-association logic vs. whatever
CrossHair's symbolic reasoning happens to reach) and adding both together
measurably beats adding either alone.

## What's still open

This is "library vs. our own generator" — one half of the real comparison.
The other half, still pending, is **library vs. LLM-driven test
improvement**: a colleague is building a different approach where an LLM
first tries to generalize a fix into the shared generator script (the same
*kind* of improvement Behavioral was, but LLM-found instead of hand-found),
then writes model-specific tests for whatever still survives. Once his
results exist, the real 5-way comparison (baseline, Pynguin, CrossHair,
Behavioral, LLM-driven) replaces this one.

## One-sentence summary for colleagues

*"Combining our own purpose-built test generator with a symbolic-execution
library (CrossHair) on top of the existing suite raises the mutation score
from 34.52% to 77.55% (+43 pts) on a 200-model sample, with 188 models
improved and none worse -- measured only on test suites verified to pass on
the original code, after we discovered and fixed a measurement flaw that had
made earlier, higher numbers (up to 92.66%) look better than they were."*
