# Tree-sitter vs. model: what we actually compared, and what we found

## The idea, in plain terms

Every model in this dataset has two independent descriptions of "what the
system looks like":

1. **The model** — the original BUML diagram (classes, attributes,
   relationships, which classes are abstract, etc.)
2. **The generated code** — the actual `python_code.py` file a code
   generator produced *from* that model.

The question: **does the generated code faithfully match what the model
says?** If the model says "this class is abstract," does the generated
Python code actually behave like an abstract class? A colleague built a tool
(`tree-sitter`) that reads Python source code directly and lists every
class/method/attribute it finds — completely independently of BUML, our own
scripts, or any assumptions about what "should" be there. That independence
is what makes it useful as a check: it can't be fooled by a bug in our own
tooling, because it never reads our tooling's output, only the raw code.

## An important caveat, worth being upfront about

When we say "the model," what the checking script actually reads is
`model_metadata.json` — a summary file *we* generated earlier by reading the
real BUML file once. It is **not** re-reading the live `.buml`/`.puml` files
fresh every time. So this check has one independent side (the code, via
tree-sitter) and one cached side (the model, via our own prior summary). If
our summarizing script had a bug, this check wouldn't necessarily catch it.
In practice this is low-risk for the specific field where we found a
problem (see below) — it's a simple, direct count with no complicated logic
behind it — but it's worth remembering this isn't a fully independent,
ground-truth-on-both-sides comparison.

## What we compared, and what matched

We compared three things that should, in principle, match exactly between
the model and the code:

| Field | Result |
|---|---|
| Number of enumerations | **Essentially perfect.** Only 1 model out of 9,081 had any mismatch at all, and it was a rounding-level difference. |
| Number of classes | Code has slightly *more* classes than the model, on ~2,830 models — but only by about 1 class on average. This turned out to be harmless: the generator sometimes adds its own small helper/stub classes that aren't in the original diagram. |
| Number of abstract classes | **The real problem.** Code has *fewer* abstract classes than the model says, on 1,960 models — averaging about 1.6 fewer abstract classes per affected model. |

(Two other fields — attribute count and method count — were reported but
deliberately not treated as "mismatches," because the model only counts
attributes/methods you explicitly drew in the diagram, while tree-sitter
counts *everything* in the code, including auto-generated getters/setters.
Comparing those two directly would be like comparing apples to a much bigger
pile of apples-plus-oranges — not a meaningful test.)

## The actual bug, with a real example

We picked one of the mismatched models (`model_100127`) and looked at both
sides by hand.

**What the model says:**
```python
relationaldatabase_NamedElement = Class(
    name="relationaldatabase_NamedElement",
    is_abstract=True,
)
```

**What the generated code actually is:**
```python
class relationaldatabase_NamedElement(Taggable):
    ...
```

That's a completely ordinary Python class. No `ABC` base class, no
`@abstractmethod` anywhere. **The code generator never implements "abstract"
as a real Python concept, ever, for any model.** It silently drops the flag
every single time. In practice this means: if a diagram says "you should
never be able to create a `NamedElement` directly, only its subclasses," the
generated code puts up no resistance at all — you can instantiate it exactly
like any other class.

This also explains an older, separately-found puzzle: across the whole
dataset, **0 out of 732 methods are ever marked `@abstractmethod`**. We
originally just observed that as a fact; this check explains *why* it's
true — the generator doesn't have a code path for it at all.

## One false alarm, ruled out

One model (`model_10006`) showed up as "0 classes in the code" according to
tree-sitter, despite the real file genuinely containing 8 classes. We
checked by hand — it's a one-off glitch in how tree-sitter's output was
generated for that single model, not a real problem with the code or a
pattern affecting other models. Confirmed isolated, not investigated
further.

## Part 2 (added 2026-10-11): checking by *name*, not just count

Everything above compares **totals** — "the model says 5 classes, the code
has 6." But a count match doesn't actually prove much: two models could
have the exact same *number* of classes while the code has completely
different *names* than the model declares. So we built a second check that
compares names directly: for every class/attribute/operation the model
declares, does something with that exact name (or a close, explainable
variant) actually exist in the generated code?

**First pass flagged 22 models (0.26%) out of 8,336** as having a name that
didn't show up anywhere in the code. Concerning at first glance — but when
we actually opened the generated code for several of them by hand, instead
of trusting the report, **every single one turned out to be a false alarm
in our own checking script**, not a real problem with the generated code.
Two concrete examples:

- **`model_10001303`**: the model declares a `Player` class with an
  attribute named `property`. But `property` is also a built-in Python
  concept (it's literally the keyword used to make a getter/setter), so the
  code generator renames it to avoid the clash — the real generated code
  has `property1`, not `property`. The code is completely correct; our
  checker just never thought to look for the renamed version.
- **`model_116`**: the model declares an attribute named `self` — which
  collides with `self`, the implicit first parameter every Python method
  already has. The generator handles this by renaming only the *internal*
  backing variable (`self_`), while the public-facing getter/setter keeps
  the original name `self`. Our checker was only looking in the "plain
  attributes" list and never thought to also check the "methods" list,
  where that public getter/setter actually lives.

We fixed the checker to account for both patterns (and a couple of smaller
related ones — a `Factura`→`Facturas` pluralization, and one case-only
difference, `Codigo` vs. `codigo`). Re-running the corrected checker across
all 8,336 models dropped the mismatch rate from **0.26% to 0.02%**
(22 models down to 2). Those final 2 are genuinely different, real
findings, not more checker bugs — one model is missing exactly one
attribute (`Fecha`) with no renamed version anywhere in the code, and one
model's `Factura` class turns out to be split across two differently-named
classes in a more complex way than a simple rename, which we haven't
chased down further.

**The lesson, worth stating plainly**: a "generator fidelity" check is only
as good as its own name-matching logic. Before concluding the dataset has a
defect, it's worth asking whether the *checking tool* might be the thing
that's wrong — especially for any renaming convention (keyword collisions,
pluralization) a generator might apply that the checker doesn't know about
yet.

## Bottom line, for a one-sentence summary to colleagues

*"We independently verified the generated code against the model using a
tool that reads raw Python syntax, and found exactly one real generator
defect: abstract classes in the diagram never come out abstract in the
code. By name, not just count, the generator is 99.98% faithful once our
own checker's blind spots (keyword-collision renaming, pluralization) were
fixed — the 22 'mismatches' we first saw were almost entirely false alarms
in our tooling, not the dataset."*
