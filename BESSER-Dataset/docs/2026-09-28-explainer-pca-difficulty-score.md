# PCA and the difficulty score, explained simply — with the real numbers

## The goal

We wanted one number per model, from 0 to 100, saying "how structurally
complex/difficult is this model" — something you could use to sort the
dataset from easiest to hardest, or pick a representative sample across
difficulty levels.

There's a well-known academic formula for this (used in a paper we compared
against): pick a few things that seem important — class count, relationship
count, attribute count — and add them together with fixed weights someone
decided on beforehand. The problem with that approach: *someone decided the
weights beforehand*, for a different, much smaller dataset. We built our own
version that lets the actual data decide what matters, instead of assuming
it in advance.

## Step 1 — collect everything measurable, not just three things

Instead of picking 3–4 structural properties by hand, we used **11**:
number of classes, attributes, associations, compositions, generalizations
(inheritance), abstract classes, enumerations, enumeration literals,
methods, "many-valued" relationship ends (one-to-many/many-to-many), and how
many different attribute *types* a model uses.

(Three more fields exist in our metadata — `association_classes`,
`abstract_methods`, `aggregation` — but every single one of the 9,082
models has the *exact same value* for these, so there's nothing to learn
from them. They're left out for a mathematical reason, not a judgment call:
the next step divides by how much a field varies, and dividing by zero
isn't allowed.)

## Step 2 — put every number on the same footing before comparing

You can't compare "932 classes" to "3 attribute types" directly — one
number just looks bigger than the other, for no meaningful reason. So
before anything else, each of the 11 fields goes through two adjustments,
one field at a time:

**(a) Squash extreme values.** We replace every raw count `x` with
`ln(1 + x)` — a transform called **log1p**, and its effect on the data is
usually called **dampening** (it dampens/dulls the influence of extreme
outlier values without hiding them completely). A model with 900 classes
and a model
with 90 classes don't end up 10× apart anymore — just meaningfully apart —
while a model with 9 classes and one with 0 still separate cleanly too.
This stops a handful of enormous outlier models (some describing UML
itself, with thousands of classes) from completely dominating everything
else.

**(b) Put every field on the same scale.** This step has a formal name:
**standardization**, and the resulting number is called a **z-score**.
After squashing, we subtract that field's own average (across all 9,082
models) and divide by its own spread (**standard deviation** — the formal
name for "how much it typically varies"). The formula, in words: *(this
model's squashed value, minus the dataset's typical squashed value, divided
by how much the dataset typically varies)*, or in symbols:

```
z-score = (squashed_value − mean_squashed_value) / standard_deviation
```

After this step, every field is measured in "how unusual is this model on
this particular trait" (its z-score), not in raw counts — so a field like
`methods` (usually small numbers) and a field like `associations` (usually
bigger numbers) become directly comparable.

The actual dataset-wide averages and spreads baked into this (after the
squash), for each of the 11 fields:

| Field | Typical (squashed) value | How much it varies |
|---|---:|---:|
| classes | 2.66 | 1.06 |
| attributes | 2.19 | 1.17 |
| associations | 1.68 | 1.11 |
| composition | 1.24 | 1.36 |
| generalizations | 1.23 | 1.55 |
| abstract_classes | 0.64 | 0.94 |
| enumerations | 0.37 | 0.64 |
| enumeration_literals | 0.55 | 1.09 |
| methods | 0.26 | 0.83 |
| many_valued_association_ends | 1.60 | 1.10 |
| attribute_type_diversity | 1.07 | 0.51 |

## Step 3 — let the data find the real pattern (this is what "PCA" does)

With all 11 numbers on the same footing, **PCA (Principal Component
Analysis)** looks at all 9,082 models at once and asks: *"is there one
underlying pattern that explains most of the variation here?"*

Think of every model as a single dot placed in an 11-dimensional space (one
direction per field). Most models don't scatter randomly through that
space — a model with more classes usually also has more attributes, more
relationships, more of everything. That shared movement stretches the
cloud of dots out along certain directions far more than others.

Mechanically, PCA finds those stretched-out directions by building a
**correlation matrix** (a table of how strongly every pair of the 11 fields
moves together, once everything is on the z-score scale from Step 2), and
then computing that table's **eigenvectors** and **eigenvalues** — this is
the actual mathematical machinery, and it's worth naming even though the
plain-language version is simpler: an **eigenvector** *is* one of the
"stretched-out directions" described above, and its matching **eigenvalue**
is a number saying exactly how much of the cloud's total spread that
direction accounts for. Sorted from the largest eigenvalue to the smallest,
eigenvector #1 becomes **PC1** ("principal component 1"), #2 becomes
**PC2**, and so on. The share of the total spread each one accounts for is
called its **variance explained**.

It found one very clearly: **PC1**, with a variance explained of **48.5%**
of all the variation in the dataset by itself.

> **PC1 = how big/elaborate the model is, overall.**

A model's PC1 score is computed as a weighted sum (mathematically, a **dot
product**) — take each of the 11 z-scores from Step 2, multiply it by a
weight specific to that field, and add all 11 results together. Each of
these per-field weights is called a **loading** — it's literally one entry
of PC1's eigenvector:

```
PC1 score = (loading₁ × z-score₁) + (loading₂ × z-score₂) + ... + (loading₁₁ × z-score₁₁)
```

Here are the actual 11 loadings PC1 uses:

| Field | PC1 loading |
|---|---:|
| classes | +0.358 |
| attributes | +0.290 |
| associations | +0.275 |
| composition | +0.340 |
| generalizations | +0.349 |
| abstract_classes | +0.314 |
| enumerations | +0.306 |
| enumeration_literals | +0.326 |
| methods | +0.202 |
| many_valued_association_ends | +0.347 |
| attribute_type_diversity | +0.125 |

Notice **every single loading is positive**. That's what makes "bigger PC1 =
more complex" a safe, literal reading — there's no field that PC1 treats as
*reducing* complexity. Some fields (classes, generalizations, many-valued
ends) matter a bit more than others (methods, attribute type diversity),
but they all push the same direction.

PCA then looks for a *second* eigenvector — the next most-stretched
direction, but only counting stretch that PC1's pattern doesn't already
explain (mathematically, PC2's eigenvector is required to be perpendicular,
or "uncorrelated," to PC1's). It found one here too: **PC2**, with a
variance explained of another **14.8%**.

> **PC2 = what kind of big it is (data-heavy vs. hierarchy-heavy), not how big.**

PC2's loadings look very different — this time with a mix of positive and
negative numbers:

| Field | PC2 loading |
|---|---:|
| classes | −0.047 |
| attributes | +0.483 |
| associations | +0.240 |
| composition | −0.251 |
| generalizations | −0.319 |
| abstract_classes | −0.257 |
| enumerations | +0.128 |
| enumeration_literals | −0.060 |
| methods | −0.079 |
| many_valued_association_ends | +0.002 |
| attribute_type_diversity | +0.671 |

Some models are large because they have lots of different *data fields* (a
wide, schema-heavy design — pulls PC2 positive, mainly via
`attribute_type_diversity` and `attributes`); other models are large
because they have a deep *class hierarchy* (lots of inheritance and
abstract classes — pulls PC2 negative). PC2 tells you which of those two
*styles* a given model leans toward — it isn't a second size scale, it's a
style dial.

We checked this wasn't just noise: we looked at the actual models sitting
at both extremes of PC2, and both groups turned out to be large,
substantial models (above-average PC1) — just built in opposite styles. So
it's a real, second dimension of difficulty, not an artifact.

## What about PC3, PC4, ... all the way to PC11?

PCA always produces as many of these directions as there are input fields —
here, 11 in total. We only *use* the first two, but here's what all 11
actually look like, so nothing is a mystery:

| Component | Variance explained | What it mainly contrasts |
|---|---:|---|
| PC1 | 48.5% | Everything together — overall size |
| PC2 | 14.8% | Data-schema-heavy vs. hierarchy-heavy |
| PC3 | 9.9% | Enumeration-heavy vs. association-heavy |
| PC4 | 7.5% | Almost entirely "how many methods," on its own |
| PC5 | 5.9% | Association-heavy vs. type-diversity/inheritance-heavy |
| PC6 | 4.9% | Composition-heavy vs. abstract-class-heavy |
| PC7 | 3.3% | Abstract classes vs. plain class count |
| PC8 | 2.0% | Attribute count vs. attribute type diversity |
| PC9 | 1.4% | Many-valued relationships vs. plain associations |
| PC10 | 1.0% | Generalizations vs. composition |
| PC11 | 0.8% | Enumeration count vs. literals-per-enumeration (the last leftover) |

Why stop at the first two? Two reasons. First, the numbers drop off fast
and then flatten out — PC1+PC2 together already cover 63.3% of everything,
while every remaining one explains less than 10% on its own, trailing off
gradually with no further sharp break. Second, and more important: we only
trust PC2 because we specifically went and checked it against real models
(see above) and confirmed it's a genuine pattern, not a fluke. We never did
that same check for PC3 onward, so we don't fold them into the score — using
an unverified pattern would be exactly the "assume it matters" mistake we
built this whole approach to avoid.

> **Correction (2026-10-18).** The two reasons above don't hold up once
> tested properly. (1) The standard rules for "how many components to keep"
> were never actually run. Now they have been (`experiment_difficulty_score_pca.py`,
> 8,336 usable models): **Kaiser keeps 3, Horn's parallel analysis keeps 3**
> (PC3's eigenvalue 1.12 beats the random-data 95th percentile of 1.04),
> only the broken-stick rule keeps fewer (1). (2) "We never checked PC3"
> is no longer true: the same extremes check that was used for PC2 now runs
> on PC3 too, and PC3 passes it *more* clearly than PC2. Both ends of PC3
> are large models (average PC1 +2.6 and +2.8 for the 5% tails) built in
> opposite styles: enumeration-heavy (≈6.6 enums, 36 literals, almost no
> methods) vs. association/method-heavy (≈31 associations, 17 methods, no
> enums). PC2 holds for its 10 most extreme models, but over its 5% tails
> one end is **average-sized**, not large: ≈12 classes, 30 attributes,
> 8 attribute types, no inheritance (average PC1 −0.38). So PC2 is a real
> style contrast, but it is not purely "two kinds of big model".
>
> **So why still only PC1+PC2?** Because we measured what PC3 would do to
> the score instead of assuming. Adding it barely changes the ranking
> (Spearman 0.986 with the current score). Where it does change scores, it
> moves small enum-heavy models up by up to 10.7 points (e.g. 5 classes,
> 4 enums) and pulls the largest models down by about 12 (271-341 classes),
> because size's share of the points drops from 75 to 64.5. Models with methods are
> not affected differently from models without. For a code-generation
> difficulty score that is a step in the wrong direction, so PC3 is left
> out on purpose. The statistics alone would allow 3; we chose 2 based on
> this measurement. Full argument: `docs/DECISIONS.md` (2026-10-18).

## Did we actually check "why stop at two"? (added 2026-10-11)

The reasoning above for using only PC1+PC2 was "the numbers drop off fast,
and we only verified PC2 is real." That's a good reason to stop trusting
*new, unverified* components — but it doesn't by itself prove that adding
more components would make the score agree *less* with the reference
paper's formula. We checked this directly instead of assuming it, by
building the score 11 different ways — PC1 alone, PC1+PC2, PC1+PC2+PC3, and
so on up to all 11 — and comparing each version's **rank agreement**
(Spearman correlation) with the paper's own formula.

**Surprising result: PC1 *by itself* agrees with the paper's formula better
than our official PC1+PC2 score does** (+0.896 vs. +0.879 — close, but a
real, consistent gap, not noise). Adding PC2 actually makes the two scores
agree *less*, and it keeps getting slightly worse through PC3/PC4
(+0.867), before slowly climbing back up through PC5–PC11 — but never
fully recovering to what PC1 alone already achieved.

Once you think about *why*, this isn't actually surprising, and it isn't a
reason to drop PC2:

- The paper's formula is a simple, unbounded sum of raw counts. A model
  with more of everything scores higher — it's fundamentally a *size*
  measure, nothing more.
- **PC1 is also, fundamentally, a size measure** ("how big/elaborate," see
  Step 3) — so of course it tracks a size-based formula closely.
- **PC2 measures something the paper's formula was never designed to
  capture at all**: not size, but *architectural style* — data-schema-heavy
  vs. hierarchy-heavy. Folding that real, separate signal into the score
  necessarily pulls some models' rank away from a pure size-ordering,
  which is exactly what "agrees less with a size-only formula" means here.

So the right way to read this result is: **the two scores measure
deliberately different things, and this experiment proves that, rather
than just asserting it.** If the goal were "match the reference paper as
closely as possible," PC1 alone would be the better choice. Our goal was
"capture more than one real kind of difficulty" — and PC2 is what does
that, at a small, explainable cost in agreement with a formula that was
only ever measuring one kind of difficulty to begin with.

(One more small, related check: does the final step's percentile-clipping,
described below, distort this ranking? Barely — removing it changes the
Spearman number by a tiny −0.0001, confirming clipping mainly affects a
small number of extreme models' exact *score*, not their relative *order*.
It does affect the extremes concretely, though: without it, 13 out of
8,451 models (0.15%) would score *above* 100 — one reaches 106.2 — which
is exactly the kind of runaway-outlier problem percentile clipping exists
to prevent.)

## Step 4 — combining PC1 and PC2 into one final 0–100 number

A few careful decisions went into this, each for a concrete reason:

- **PC1 keeps its direction (bigger PC1 = harder).** Every one of its 11
  ingredients pushes the same way — more of anything makes PC1 go up — so
  "bigger number = more complex" is a safe, meaningful reading.
- **PC2 is used as an absolute value (`|PC2|`), not its raw sign.** Whether
  "data-heavy" comes out as a positive or negative number is essentially a
  coin flip of how the math happens to be computed — it carries no real
  meaning about which style is "harder." Only "how far toward *either*
  extreme style" is meaningful, which is exactly what taking the absolute
  value measures.
- **PC1 and PC2 don't get an even 50/50 split of the 100 points.** PC1
  explains more of the dataset's real variation (48.5% vs. 14.8%), so it
  gets a proportionally bigger share of the final score. The exact split:

  ```
  PC1's share of 100 points = 100 × 48.5 / (48.5 + 14.8) = 76.64 points
  PC2's share of 100 points = 100 × 14.8 / (48.5 + 14.8) = 23.36 points
  ```

  This ratio comes directly from the data each time it's computed, it
  isn't a number we chose by hand.

- **Spreading each component's score across its point budget (this is the
  "0 to 100" part).** A model's raw PC1/PC2 score isn't naturally bounded —
  it could in principle be any number. The technique used here has two
  named parts, **percentile clipping** followed by **min-max scaling**, to
  turn it into "points out of 76.64" (or "points out of 23.36" for PC2):

  1. **Percentile clipping.** Look at the 1st-percentile and 99th-percentile
     raw scores across all 9,082 models — call them `lo` and `hi`. For PC1,
     `lo = −3.46` and `hi = +7.33`. For `|PC2|`, `lo = 0.00` and
     `hi = 3.02`. Any model's raw score beyond those bounds gets pulled in
     ("clipped") to `lo` or `hi` — so one wildly extreme model can't stretch
     everyone else's scale.
  2. **Min-max scaling.** Spread everything else in between linearly onto
     the point budget:
     ```
     points = (clipped_score − lo) / (hi − lo) × budget
     ```

  Because both pieces are already capped to their own budget before being
  added, the final sum is guaranteed to land between 0 and 100 — no extra
  "clamp it at the end" step is needed.

- **Final score = PC1 points + PC2 points.**

## A complete real example, worked by hand

Take `model_2023` — a genuine 932-class metamodel (used elsewhere in our
reports as the model that breaks the *other* formula's scale). Its 11 raw
counts, run through every step above:

| Field | Raw count | z-score (after log1p + standardization) | Contributes to PC1 (loading × z) | Contributes to PC2 (loading × z) |
|---|---:|---:|---:|---:|
| classes | 932 | 3.95 | +1.41 | −0.19 |
| attributes | 11 | 0.26 | +0.07 | +0.12 |
| associations | 836 | 4.55 | +1.25 | +1.09 |
| composition | 292 | 3.26 | +1.11 | −0.82 |
| generalizations | 332 | 2.95 | +1.03 | −0.94 |
| abstract_classes | 70 | 3.87 | +1.22 | −0.99 |
| enumerations | 0 | −0.58 | −0.18 | −0.07 |
| enumeration_literals | 0 | −0.50 | −0.16 | +0.03 |
| methods | 0 | −0.31 | −0.06 | +0.02 |
| many_valued_association_ends | 661 | 4.44 | +1.54 | +0.01 |
| attribute_type_diversity | 3 | 0.62 | +0.08 | +0.42 |
| **Total (raw PC1 / PC2 score)** | | | **7.30** | **−1.32** |

Now spread each total across its point budget:

- **PC1:** 7.30 sits just inside the [−3.46, 7.33] range (this model is
  right at the edge of the top 1% of the whole dataset). Points =
  `(7.30 − (−3.46)) / (7.33 − (−3.46)) × 76.64` = **76.48 points**.
- **PC2:** `|−1.32| = 1.32`, comfortably inside the [0.00, 3.02] range.
  Points = `(1.32 − 0.00) / (3.02 − 0.00) × 23.36` = **10.18 points**.
- **Final score:** `76.48 + 10.18` = **86.66 out of 100.**

This isn't a rounded illustration — it matches `model_2023`'s actual stored
score exactly (86.6638...), reproduced here by hand, digit for digit.

## What we compared it against

The paper's own formula, applied to this dataset, produces some genuinely
broken results: `model_2023` scores **931 out of an unbounded scale** under
that formula — about 67 times higher than what the paper itself calls an
average "hard" example. That's because the paper's formula was only ever
tuned on 30 small textbook exercises (biggest one: 13 classes) and never
protects against a model this much larger showing up. Our PCA-based score
gives that same model an 86.66 out of 100 — correctly near the top, but not
a number that breaks the scale.

Overall, the two scores agree on *ranking* for the large majority of models
— measured with a statistic called **Spearman rank correlation**, which
came out to 0.89 out of a possible 1.0 (1.0 would mean the two scores put
every model in exactly the same order; 0 would mean no relationship at
all). So our score isn't measuring something unrelated, it's a more
careful, data-driven version of the same idea.

## One-sentence summary for colleagues

*"We used PCA to find that model difficulty in this dataset has two real
dimensions — overall size, and which architectural style a model leans
toward — and combined them into a single 0–100 score, weighted by how much
of the dataset's real variation each dimension actually explains, rather
than guessing weights in advance the way the reference paper's formula
does."*
