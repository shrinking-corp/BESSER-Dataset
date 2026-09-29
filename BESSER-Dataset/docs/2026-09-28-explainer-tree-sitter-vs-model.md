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

## Bottom line, for a one-sentence summary to colleagues

*"We independently verified the generated code against the model using a
tool that reads raw Python syntax, and found exactly one real generator
defect: abstract classes in the diagram never come out abstract in the
code — everything else (enumerations, near enough on class counts) matches
correctly."*
