# Difficulty Score Validation & Mutation Score Improvements — Findings for Presentation

This document walks through a set of questions raised about the difficulty
score methodology and the test-generation/mutation-score work, each answered
with real, re-checkable numbers from this project's own scripts and reports
— not assertions. Every number below comes from a named script or report
file so it can be independently verified.

---

## 1. Is the Spearman correlation real, or just a number Claude made up?

**It's a real, independently verifiable calculation.** The script
`scripts/compare_difficulty_scores.py` computes it by hand: it implements
its own rank-averaging function (`rankdata()`, matching `scipy.stats.rankdata`'s
default "average" method) and then computes a plain Pearson correlation on
those ranks — which is mathematically exactly what Spearman correlation
*is*. It's hand-rolled instead of calling `scipy.stats.spearmanr()` only
because this project's Python environment doesn't have `scipy` installed
(only `numpy`), not because of any shortcut in the math.

### The complete picture: what happens as we add more PCA components

The official difficulty score combines two components (PC1 + PC2) out of
eleven possible ones. We built a second script,
`scripts/experiment_difficulty_score_pca.py`, specifically to check whether
using *more* components would track the reference paper's formula better —
rather than assuming the answer, we measured it for every possible
cumulative combination, run dataset-wide (8,451 models, after excluding the
631 fully-empty stub models — see Section 4):

| Components used | Cumulative variance explained | Spearman vs. article formula | Pearson vs. article formula |
|---|---:|---:|---:|
| PC1 only | 47.91% | **+0.8960** | +0.7513 |
| PC1 + PC2 (**official**) | 63.07% | +0.8791 | +0.7370 |
| PC1..PC3 | 73.01% | +0.8672 | +0.7207 |
| PC1..PC4 | 80.37% | +0.8653 | +0.7261 |
| PC1..PC5 | 86.33% | +0.8687 | +0.7336 |
| PC1..PC6 | 91.32% | +0.8725 | +0.7369 |
| PC1..PC7 | 94.44% | +0.8839 | +0.7407 |
| PC1..PC8 | 96.88% | +0.8863 | +0.7427 |
| PC1..PC9 | 98.26% | +0.8866 | +0.7433 |
| PC1..PC10 | 99.20% | +0.8887 | +0.7443 |
| PC1..PC11 (all) | 100.00% | +0.8873 | +0.7430 |

**The surprising finding: using PC1 *alone* agrees with the reference
paper's formula better than our official PC1+PC2 combination does** —
agreement actually *drops* when PC2 is added, dips further through PC3/PC4,
then slowly climbs back up without ever fully recovering.

**Why, once you look at it**: the reference paper's formula is a simple,
unbounded sum of raw structural counts — it is, fundamentally, a *size*
measure. PC1 is also fundamentally a size measure ("how big/elaborate is
this model, overall"), so of course the two track closely. PC2 measures
something the paper's formula was never designed to capture at all:
*architectural style* (data-schema-heavy vs. hierarchy-heavy), not size.
Folding in a real, different kind of complexity necessarily pulls some
models' rank away from a pure size-ordering — which is exactly what "agrees
less with a size-only formula" means here. This is evidence the two scores
measure genuinely different things, not evidence either one is wrong.

### Does the 0–100 clipping distort the ranking?

A related, separate check: the official score clips each component to its
1st–99th percentile band before converting it to points, specifically so
one extreme outlier model can't stretch the scale for everyone else. Does
that clipping change the *rank order* (and therefore the Spearman number)?

Removing the clip entirely changes Spearman from **+0.8791 to +0.8790**
— a difference of **0.0001**. Clipping has essentially no effect on rank
agreement; its real job is magnitude, not order (see Section 2).

**Bottom line**: the Spearman number is a real, reproducible calculation,
checked from multiple angles (which components to include, with/without
clipping) rather than taken at face value.

---

## 2. Can a model's difficulty score fall outside 0–100?

**No, not by construction — and this is now double-confirmed, not just
asserted.**

**Mathematically**: each of the two components (PC1 and `|PC2|`) is
independently percentile-clipped and then linearly rescaled into its own
non-negative point budget *before* being added together. Since both
addends are already bounded to their own sub-range, the sum is guaranteed
to land in `[0, 100]` — no separate "clamp the final answer" step is
needed or used.

**Empirically, on the real dataset** (`reports/difficulty_score_report.json`,
all 9,082 measured models): the actual minimum and maximum ever produced
are **3.27** and **93.55** — comfortably inside the guaranteed range, never
close to either edge.

**What happens if we deliberately remove the clip?** We tested this
directly rather than just trusting the math: with clipping removed, the
range becomes **0.43 to 106.20** — and **13 out of 8,451 models (0.15%)**
would score *above* the normal 100-point cap, with `model_2578` reaching
106.2. This confirms the clip is doing real, measurable protective work
for a small number of genuine outliers — not an unnecessary safety net.

---

## 3. Experimenting with adding/removing PCA components

Covered fully in Section 1's table above — this was the specific question
"what happens to the correlation if we use more or fewer components," and
the complete PC1-through-PC11 sweep answers it directly: more components
is not simply "better," and PC1 alone is actually the closest match to the
reference formula of any combination tested.

---

## 4. Excluding models with no real logic — which "no logic" do we mean?

There are **two different, non-overlapping groups** worth distinguishing
clearly, because they answer different questions:

| Group | Count | Definition | Currently excluded from the official difficulty score? |
|---|---:|---|---|
| Fully-empty stub models | **631** | Every class body is literally `class X: pass` — zero executable statements anywhere in the generated code | **Yes** (excluded from the PCA experiment script; see also Section 6) |
| Zero-`has_logic` models | **992** | Still have real, working methods (getters/setters), just none with actual conditional/computed logic — counted only among the already-non-empty 8,336 models, so this group never overlaps with the 631 above | **No** — the official `compute_difficulty_score.py` does not exclude these |

Both groups genuinely have nothing meaningful to say about "how
structurally difficult is this model's *logic*" — the 631 have no
structure at all, and the 992 have structure but no real behavior to
measure difficulty by.

**Does excluding the wider group (631+992 = 1,623 models) change the
Spearman result?** We ran both exclusion scenarios side by side, through
the official PC1+PC2 combination:

| Exclusion | Models remaining | Spearman vs. article | Mean | Median |
|---|---:|---:|---:|---:|
| Narrower (631 only) | 8,451 | +0.8791 | 30.47 | 27.44 |
| Wider (631 + 992) | 7,459 | **+0.8825** | 31.30 | 28.83 |

**Yes, slightly — and in the direction you'd expect.** Also excluding the
992 logic-less-but-functioning models nudges agreement with the reference
formula up a little (+0.0034), and pulls the mean/median up too, since
those 992 models skew toward the simpler end of the dataset — removing a
cluster of simple, logic-free models naturally raises what's left. The
effect is real but modest: it doesn't change which conclusion the project
has been drawing, it's a small, honest refinement worth knowing about
rather than a result that overturns anything.

---

## 5. Tree-sitter vs. model & code — does `python_code.py` need fixing?

**No — the generated code was already correct. The 22 "mismatches"
originally flagged were false positives in our own checking script, not a
dataset defect.**

We built `scripts/validate_generator_fidelity_names.py` to check, by name
(not just by count), whether every class/attribute/operation the model
declares actually exists in the generated code. It first flagged 22/8,336
models (0.26%) — but reading the actual generated code for several of them
by hand (rather than trusting the report) showed every one was a checker
bug:

- **`property` → `property1`**: a BUML attribute named `property` collides
  with Python's own `property` built-in, so the generator renames it
  end-to-end — the code is completely correct, our checker just never
  looked for the renamed version.
- **`self` → `self_` / `self1`**: similarly, an attribute named `self`
  collides with the implicit method receiver — the generator handles it
  correctly (sometimes keeping the public accessor's original name while
  only renaming the internal field), our checker only ever looked in the
  wrong place (the "attributes" list, never the "methods" list, where a
  property accessor is actually filed).
- **`Factura` → `Facturas`**: an already-known pluralization the generator
  applies consistently; a different, already-existing script already
  handles this correctly, our checker just never carried the same rule.

We fixed the checker's name-resolution logic (checking the methods list
too, trying `+1`/`+s`/case-insensitive forms) and re-ran it dataset-wide:
**mismatch rate dropped from 0.26% to 0.02% (2/8,336)**. The 2 that remain
are real, distinct, small findings — one genuinely missing attribute, one
structurally different class split — not more checker bugs, and not
touched further since they're each isolated, one-model cases.

**No generated code was ever modified.** Doing so would have changed
already-correct output to "fix" a problem that didn't exist in the
dataset.

---

## 6. Excluding models without a calculable mutation score

This is already a long-standing, built-in part of this project's
methodology — not a new gap. `reports/excluded_models_master.json` tracks
every model excluded from mutation-score-based work (and why), **746 total**
out of 9,082:

| Reason | Count | What it means |
|---|---:|---|
| Fully-empty stub models | 631 | Every class is `class X: pass` — zero mutable code, mutation testing was never attempted on these at all |
| Timeout, old test suite | 79 | Didn't finish measuring within the time budget, even after retries at longer limits |
| Timeout, combined test suite | 32 | Same, for the merged old+new test suite (naturally slower, since it's bigger) |
| Broken property-name reference | 2 | A known pluralization edge case breaking an older generator version |
| Broken test infrastructure | 2 | A silent setter bug / a genuinely broken test file, isolated cases |

The remaining **8,336 models** (`reports/usable_models.txt`) are the ones
that get a real, trustworthy mutation score — this list, and the exclusion
reasons behind it, is reused consistently across every mutation-related
report in this project, not recomputed ad hoc per analysis.

**Important distinction, asked for explicitly**: this is about models with
**no score at all** (timeout/error — nothing was ever measured), not models
that scored a real 0%. A real 0% is a legitimate, meaningful result; a
missing score is not a result at all, and mixing the two into one average
would be misleading.

---

## 7. Difficulty score distribution

Real distribution across all 8,451 included models (same exclusion as
Section 1 — the 631 fully-empty models), grouped into 10-point bands for
readability (the full 1-point-wide breakdown is in
`reports/difficulty_score_distribution_report.{json,md}`):

| Score range | Models | Share | |
|---|---:|---:|---|
| 0–10 | 156 | 1.85% | ▏ |
| 10–20 | 1,736 | 20.54% | █████████████████████ |
| 20–30 | 2,427 | 28.72% | █████████████████████████████ |
| 30–40 | 1,633 | 19.32% | ███████████████████ |
| 40–50 | 1,386 | 16.40% | ████████████████ |
| 50–60 | 456 | 5.40% | █████ |
| 60–70 | 327 | 3.87% | ████ |
| 70–80 | 247 | 2.92% | ███ |
| 80–90 | 71 | 0.84% | █ |
| 90–100 | 12 | 0.14% | ▏ |

**Mean: 33.00  |  Median: 29.35  |  Min: 3.27  |  Max: 93.55**

The distribution is clearly right-skewed: most models cluster in the
20–50 range (over 64% of the dataset), with a long, thin tail of
genuinely complex outliers above 70 — fewer than 1% of models score above
80.

---

## 8. Mutation score improvements — what we did, and a real example

This dataset's mutation score had been stuck around 35–44% for a long
time, regardless of which test suite or scope we measured. Two separate,
real improvements moved this substantially, both deterministic (no LLM
guesswork in the final generator — an LLM experiment helped us *find* one
of the two gaps, but the actual fix is hand-written and reliable for every
model with the same shape):

### Improvement 1 — testing both sides of a relationship independently

**The gap**: when two classes are linked in both directions (e.g. a `Node`
has a `next`, and that `next` has a `previous` pointing back), the
original tests only ever triggered the link from *one* side and trusted
the other side to update correctly as a side effect — never calling the
other side's own update logic directly. Fixed by adding a generator rule
that calls *both* sides' own setters independently.

**Result on one representative model**: mutation score went from 35% to
42.5% (14 → 17 of 40 mutants killed).

### Improvement 2 — a limitation we thought was permanent, wasn't

**The deeper gap**: some relationships point at a class that's only a
stub in the generated code — e.g. `class Arc: pass`, with nothing
implemented on it at all. The real side's code correctly tries to keep
both ends in sync ("if the other object has this attribute, update it
too"), but since the stub genuinely has nothing on it, that check can
never succeed. We'd diagnosed this correctly months earlier and concluded
— reasonably, at the time — that no test could ever kill a mutant hiding
inside that logic, since the check is permanently false for any real
instance of the stub.

**What we'd missed**: nothing stops a *test* from giving the stub object
that missing attribute itself, by hand, before using it. In plain terms —
if a delivery driver's job is "check if this address has a mailbox, and
if so put the package in it," and we're testing with a house that has no
mailbox, of course nothing happens. But a test can tape a mailbox to the
house itself before the test starts. That doesn't invent anything fake —
it's still testing the driver's real behavior (does the package correctly
go in when a mailbox genuinely is there), using a minimal stand-in for an
incomplete collaborator. This is an entirely standard testing technique
(a "test double"), not a shortcut.

**A concrete example**, from the actual generated code:

```python
@target.setter
def target(self, value):
    old_value = getattr(self, "_petrinet_Node__target", None)
    self.__target = value if value is not None else set()

    # Remove self from old opposite end
    if old_value is not None:
        for item in old_value:
            if hasattr(item, "Arc"):              # <- always False for a real Arc()
                opp_val = getattr(item, "Arc", None)
                if opp_val == self:                # <- the mutated line: survived every time
                    setattr(item, "Arc", None)
    ...
```

The new test, instead of giving up because `Arc` is a stub, does this:

```python
arc = petrinet_Arc()
setattr(arc, "Arc", node_a)      # manually give the stub the attribute a real implementation would have had
node_a.target = {arc}             # exercises the "add" branch for real
node_a.target = set()             # exercises the "remove" branch — this is what actually kills the mutant
assert arc.Arc is None            # fails under the mutated version, passes under the correct one
```

We built this as a new, permanent rule in the test generator (not an
LLM-written one-off): for every relationship where one side is a stub,
construct both sides, manually attach the missing attribute, then
exercise the real side's logic and check the stand-in updates correctly.

**Results**:
- On the one model traced by hand: 35% → 42.5% → **95%** (38/40 mutants
  killed, 2 genuinely remaining).
- Across the full 200-model comparison sample, combined with every other
  improvement already made (a purpose-built generator + a symbolic-execution
  library's output, merged into one suite): **77.59% → 92.66%**, a
  **+41.81 point lift over the original baseline**, with **0 models made
  worse** by any of it — every improvement here is purely additive, never
  a trade-off.

### How we found this (a brief, honest aside)

Before building the fix above, we tried letting a local LLM (running via
Ollama, no external API) automatically find and fix the test-generator gap
on its own, across several retry attempts. It made zero progress — not
because the approach was wrong in principle, but because we discovered
most of what it was being asked to fix (roughly 92% of one model's
remaining gaps) was Improvement 2's exact pattern: genuinely impossible to
fix without the test-double technique above, which no amount of prompting
could have reasonably produced on its own. Once we traced the real cause
by hand, the actual fix took very little code and needed no further LLM
involvement at all — a reminder that understanding *why* something
survives is usually worth more than more attempts at fixing it blindly.
