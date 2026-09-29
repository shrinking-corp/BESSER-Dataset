# Is the mutation score higher on empty models?

**Short answer: no, not the way you'd expect — the truly empty models never
get scored at all, and the models that do score highest are actually
*bigger than average*, not simpler.**

## The worry

Mutation testing works by deliberately breaking the code in small ways
("mutants") and checking whether the test suite notices. The score is
`killed / run`. The natural worry: if a model has almost no real code, there's
almost nothing to break, so a handful of trivial mutants get killed easily
and the model ends up with a misleadingly perfect-looking score — making the
dataset's average mutation score look better than it really is.

## Finding #1 — completely empty models are already thrown out, not scored

Some models in this dataset are, quite literally, nothing but declarations:

```python
class Token:
    pass

class Place:
    pass
```

No method does anything. A file like this can't produce a single mutant —
there's no operator, no comparison, no literal to change. We checked this
back in September: **631 models** are like this across the whole dataset
(every class is `class X: pass`, confirmed by reading the code directly, no
guessing). These are flagged as `no_logic` and **excluded from the usable
dataset entirely** — they never appear in any mutation report, they don't
get a score of "100%" or anything else. So the literal version of the worry
("empty models score 100%") doesn't happen in our pipeline — they're removed
before scoring, not scored favorably.

## Finding #2 — among the models that remain, very small ones score a bit higher

That's not the whole story, though — a model doesn't have to be *completely*
empty to be small and simple. So we checked: among the 8,336 models that do
get a real score, does having fewer mutants (a proxy for "simpler code")
correlate with a higher score?

| How many mutants were actually run for a model | How many models | Average mutation score |
|---|---|---|
| 1–5 (very few — a tiny model) | 540 | **50.5%** |
| 6–20 | 586 | 45.2% |
| 21–50 (most models hit here, near the 40-mutant cap) | 7,210 | 43.3% |

So yes — there's a real, if modest, effect: the smallest ~6.5% of the
dataset (models with only 1–5 mutants to kill) score about 7 percentage
points higher on average than everyone else. With only a handful of
mutants, a test suite has an easier time catching all of them by chance.

## Finding #3 — but the *big* spike near 100% is NOT these simple models

This is the interesting, counter-to-expectation part. The dataset's mutation
scores form a "bimodal" shape — lots of models bunched near 0%, and a second
big cluster of 906 models sitting at exactly 100%. If the worry above were
the whole explanation, you'd expect that 100% cluster to be full of tiny,
simple models. It isn't:

- Those 906 perfect-scoring models ran an average of **38.9 out of 40**
  possible mutants — right at the cap, meaning they're not small at all,
  they have *plenty* of real code to mutate, and the test suite caught
  essentially all of it.
- Their average structural difficulty score is **46.6**, noticeably
  *higher* than a random model's average of **32.2** (difficulty score is
  our separate 0–100 measure of how large/complex a model's structure is —
  see the PCA-difficulty-score explainer doc).

So the models scoring 100% aren't simple models getting lucky — they're
larger-than-average models whose generated tests genuinely do catch nearly
every injected fault. That's a real, earned result, not an artifact.

## Bottom line

- Completely empty models: excluded before scoring, not an issue.
- Very small (but not empty) models: a real but small inflation effect
  (~7 points higher score, ~6.5% of the dataset).
- The big "near 100%" cluster driving the bimodal shape: genuinely large,
  well-tested models, not an artifact of simplicity.

**What this means for the "why is mutation score low" story:** it doesn't
change the headline finding — the average is still pulled down mainly by
weak assertions (tests that check type but not value, see the mutation-score
investigation in `docs/DECISIONS.md`), not by empty models inflating the
other end. If anything, this makes the ~40% average slightly more
conservative than it would look if we'd left the truly empty models in.
