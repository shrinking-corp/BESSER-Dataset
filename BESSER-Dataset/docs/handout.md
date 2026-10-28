# Benchmark dataset: handout for the benchmarking side

What the dataset repo provides, how its files are built, what generated code
has to look like to be tested, and what we still need to agree on.

## In short

- **5,264 class diagrams** (PlantUML), each with a reference Python
  implementation and a fixed test suite that passes on it. Code generated
  from a diagram, original or shrunk, is judged by running that suite on it.
- **Status:** the data is final. The train/test split is not made yet,
  because the ratio is still open (section 6). An example export
  (200 models) exists and can be shared.
- **What you do with it:** iterate over `manifest.json`; for each model,
  shrink `model.puml`, have the code agent generate `python_code.py`, run
  `test_super_suite.py` on it, and compare.

## 1. What you get

```
<export>/
  manifest.json            split parameters, buckets, source commit, export config, one entry per model
  README.md                the layout below, generated
  train.txt, test.txt      model names on each side
  pilot.txt                100 models for trying the pipeline first (below)
  benchmark_export.toml    the config this export was made with
  train/<model>/  test/<model>/
    model.puml             the class diagram (benchmark input)
    model_buml.py          the same model in BUML, the original dataset's format
    python_code.py         the reference implementation
    test_super_suite.py    the fixed test suite, passes on the reference
    code_structure.json    tree-sitter structure of the reference (classes, attributes, methods, line ranges)
    model_metadata.json    structural counts (classes, attributes, associations, …) and difficulty scores
    test_suite_quality.json  mutation scores of the test suite and of the original-tests baseline
```

Each `manifest.json` entry has `model`, `split`, `bucket`, `difficulty_score`,
`path`, the original file names, and `absent` (optional files a model lacks).

`pilot.txt` is a small, difficulty-balanced set for trying the whole
pipeline before a full run: 10 models from each bucket (all 9 of 90-100,
so 11 of 80-90). It overlaps train and test, so find each model's folder
through `manifest.json`.

The contents are configurable. `benchmark_export.toml` lists every per-model
file (optionally only some keys of a JSON file), extra manifest fields, and
repo files shipped once (e.g. scripts). If you need more of our per-model
data, it's a few lines there, not a code change.

## 2. Where the models come from

- **Source:** the BESSER dataset, 9,082 models in BUML (BESSER's Python
  modelling format), with generated Python code and Hypothesis tests.
- **Usable:** 8,336. Excluded: models with no testable logic, models whose
  original tests could not be measured, and a few with code-generation defects.
- **Unique:** 5,264. 37% of the usable models were copies of another model:
  the same Ecore metamodel scraped from many GitHub repositories. Copies were
  removed by comparing the original BUML, ignoring only set order, statement
  order, comments and the random model ID. The grouping was confirmed two
  more ways (by the PUML, and by the models besser builds). Similar but
  different models are kept as distinct tasks.
- **Difficulty score:** 0-100, from a PCA over 11 structural counts (first
  two components, 62% of variance). It agrees with the reference paper's
  formula at Spearman 0.92 and also captures enums, methods and attribute
  types, which that formula ignores. Ten 10-point buckets.

## 3. The PUML format

Generated from the BUML, sorted throughout (identical model ⇒ identical
file), and **lossless**: every element any BUML model in the dataset
specifies is written out, verified by parsing all 9,082 PUML files back and
comparing them with their BUML models. Examples are real lines from the dataset.

| Element | Syntax | Example |
|---|---|---|
| Frame | `@startuml` … `@enduml` | |
| Metadata (comments) | `' model:`, `' model description:`, `' project:`, `' owner:`, `' description:` | `' project: sampleModel` |
| Class | `class Name {` … `}`, or `abstract class Name {` | `class Login {` |
| Attribute | `  + name : type` | `  + lastLoginTime : date` |
| Operation | `  + name(param : type, …) : returnType`, parameters sorted by name, `void` if no return type | `  + implements(javaMM_type : str) : str` |
| Enumeration | `enum Name {`, one literal per line (can be empty) | `enum account_AccountType {` |
| Generalization | `General <\|-- Specific` | `ASTNode <\|-- javaMM_AbstractMethodInvocation` |
| Association | `A "role min..max" -- "role min..max" B : name` | `Login "login4 0..1" -- "customer5 1..1" customerpackage_Customer : Customer_Login` |
| Composition | `*--` (left class is the whole), `--*` (right class is the whole), `*--*` (both) | `javaMM_Annotation "… 0..9999" --* "… 1..1" javaMM_BodyDeclaration : annotations86` |
| Non-navigable end | `{not navigable}` inside that end's label | `"user_1 1..1 {not navigable}"` |
| OCL constraint | `note top of Class` / `  constraint name (OCL): expression` / `end note` | `  constraint minCredit (OCL): context Account inv: …` |

How to read an association: each label sits next to the class that end
**points to**, and its role name is the attribute the **other** class uses.
In the `Login`–`Customer` line above, `Login` has an attribute `customer5`
(one Customer) and `customerpackage_Customer` has `login4` (zero or one
Login). **`9999` means unbounded** (`*`).

Rare or unused:
- `{not navigable}` occurs in one model only.
- OCL constraints occur in a few dozen models.
- `*--*`, aggregation (`o--`) and association classes are supported but never occur.
- Free text in comments and constraints is kept on one line, with `\n` and
  `\\` escaped.
- The `' model:` line is a random ID. It differs between otherwise identical
  models, so ignore it.

**Changed from the earlier format** (your parser may need updating):
- role names in the end labels (before, multiplicities only)
- composition on either or both ends
- `{not navigable}` (before, encoded as arrows)
- constraint notes
- the `'` header comments

The role names matter most: they are the attribute names every association
test uses, so code generated from a PUML without them could never pass.

## 4. The test suite (`test_super_suite.py`)

**What's in it:**
- the dataset's own Hypothesis tests
- our structural tests (attributes, constructors, generalizations, both
  directions of every association)
- behavioral tests (each bidirectional association driven from both ends)
- CrossHair tests (symbolic execution)

**Every suite is green.** Every test that failed on the reference was
removed (6,250 tests in 650 models, almost all of them the dataset's own
checks that fail on empty operations). A test that fails on the reference
can't judge generated code.

**It doesn't encode the reference's stubs.** No model specifies operation
bodies, so every operation in the reference is an empty stub. CrossHair
assertions on what such a stub returns were turned into plain calls (3,371
tests in 407 models). The suite checks that an operation exists and accepts
its parameters, not what it returns.

**How good it is:** a property-scoped mutation score of **75.61%**, against
**35.60%** for the dataset's original tests (+40.01 points; 0 of 5,264
models worse). The gap grows with difficulty (+30 points in the easiest
bucket, +61 in the hardest). Per model: `test_suite_quality.json`.

**How to run it**, the same way the suites were made green:
- in a folder containing the generated `python_code.py` and `test_super_suite.py`
- Python 3.11, pytest 9.1.1, hypothesis 6.167.1
- `python -m pytest test_super_suite.py -q -p no:cacheprovider --hypothesis-seed=0`
- a time limit of at least 360 s per run (we needed 1,200 s for 7 very
  large models)

The seed matters: unseeded Hypothesis draws different examples on every
run. `--hypothesis-seed=0` is given once, on the command line, and every
`@given` test then starts from its own generator seeded with 0. So the
examples don't depend on which tests or models ran before, or in what
order, and with a seed Hypothesis doesn't use its example database at all.
What a test draws still depends on its strategies, and some build objects
from the generated classes themselves (see the type-hint rule below). In
short, runs on code from the original and from the shrunk diagram see
identical inputs as long as both follow the API below. The evidence is in
`docs/2026-10-28-hypothesis-seed-and-comparable-test-runs.md`.

Two more things to keep steady:
- **Load.** Hypothesis fails an example that takes over 200 ms (its
  deadline), so don't run so many suites in parallel that the machine is
  overloaded.
- **Versions.** Another Hypothesis version can draw different examples
  from the same seed.

Score a model by its pass rate (passed / total), because suite sizes vary a
lot: median 90 tests, 90% of models under 481, maximum 4,137
(`reports/test_count_distribution.md`).

**What generated code must look like.** The suite tests the API the
reference generator produces. Code that implements the diagram differently
fails even if it is reasonable, so the code agent's prompt has to state
these rules, or include one reference implementation as an example:
- One module, `python_code.py`. One class per PUML class with the same name
  (characters invalid in Python identifiers dropped). Enumerations are
  `Enum` subclasses with one member per literal (`minutes = "minutes"`).
  Generalizations are Python inheritance.
- **Every class must be instantiable, including the PUML's `abstract`
  ones.** The tests construct them and assert
  `not inspect.isabstract(...)` on every class, so no `@abstractmethod`.
  Deriving from `abc.ABC` alone is harmless (the reference does it for some
  abstract classes and not others).
- **Constructor:** one keyword parameter per attribute (required), then one
  per association end the class can navigate, named by its role (optional,
  default `None`). A many-valued end (max > 1) is a `set`, empty by default.
  **Annotate the attribute parameters with their types** (`name: str`), as
  the reference does: the suite builds some objects with
  `st.builds(Class)`, which fills required parameters from their type
  hints, and fails on a required parameter without one.
- **Every attribute and association end is a `@property` with a setter.**
  Tests check for the property itself, not just that the attribute exists.
- **Association setters keep both ends consistent.** Setting
  `login.customer5 = c` also sets `c.login4 = login`, and replacing or
  removing a link updates the old partner.
- **Operations:** methods with the PUML's parameters. The body is free, but
  it must not raise: tests call the operation.

## 5. Other per-model data

- `code_structure.json`: tree-sitter extraction of the reference (classes,
  bases, attributes, methods with line ranges). The same extractor can be
  run on generated code to compare structure.
- `model_metadata.json`: classes, abstract classes, enumerations, literals,
  attributes, methods, generalizations, associations, compositions,
  many-valued ends, attribute type diversity, plus the difficulty score and
  its components.
- `test_suite_quality.json`: mutation results (40 mutants per model, seed 0)
  for the test suite and for the original-tests baseline.

## 6. The split

Stratified by difficulty bucket, seeded (42), at least one test model per
bucket. Each cell is **train / test**:

| Train / test | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 | 80-90 | 90-100 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| *models in bucket* | *363* | *1,239* | *1,294* | *1,002* | *647* | *336* | *188* | *127* | *59* | *9* | *5,264* |
| **90 / 10** | 327 / 36 | 1,115 / 124 | 1,165 / 129 | 902 / 100 | 582 / 65 | 302 / 34 | 169 / 19 | 114 / 13 | 53 / 6 | 8 / 1 | **4,737 / 527** |
| **85 / 15** | 309 / 54 | 1,053 / 186 | 1,100 / 194 | 852 / 150 | 550 / 97 | 286 / 50 | 160 / 28 | 108 / 19 | 50 / 9 | 8 / 1 | **4,476 / 788** |
| **80 / 20** | 290 / 73 | 991 / 248 | 1,035 / 259 | 802 / 200 | 518 / 129 | 269 / 67 | 150 / 38 | 102 / 25 | 47 / 12 | 7 / 2 | **4,211 / 1,053** |
| **75 / 25** | 272 / 91 | 929 / 310 | 970 / 324 | 752 / 250 | 485 / 162 | 252 / 84 | 141 / 47 | 95 / 32 | 44 / 15 | 7 / 2 | **3,947 / 1,317** |
| **70 / 30** | 254 / 109 | 867 / 372 | 906 / 388 | 701 / 301 | 453 / 194 | 235 / 101 | 132 / 56 | 89 / 38 | 41 / 18 | 6 / 3 | **3,684 / 1,580** |
| **67 / 33** | 242 / 121 | 826 / 413 | 863 / 431 | 668 / 334 | 431 / 216 | 224 / 112 | 125 / 63 | 85 / 42 | 39 / 20 | 6 / 3 | **3,509 / 1,755** |
| **60 / 40** | 218 / 145 | 743 / 496 | 776 / 518 | 601 / 401 | 388 / 259 | 202 / 134 | 113 / 75 | 76 / 51 | 35 / 24 | 5 / 4 | **3,157 / 2,107** |
| **50 / 50** | 181 / 182 | 619 / 620 | 647 / 647 | 501 / 501 | 323 / 324 | 168 / 168 | 94 / 94 | 63 / 64 | 29 / 30 | 5 / 4 | **2,630 / 2,634** |

## 7. Questions for you

1. **Train ratio:** which row of the table?
2. **Test runner:** should the export ship a small reference runner? It would
   take a model folder and a generated `python_code.py`, run the suite
   exactly as above, and return per-test results as JSON. That way every
   run uses the same settings.
3. **`python_code.py`:** ship the reference implementation (useful as a
   prompt example and for debugging), or keep it out so the code agent can't
   see it?
4. **Where the export lives:** its own git repository, a release archive,
   or a folder you copy?
5. **More data:** do you need anything else per model, such as coverage,
   per-method logic classification, or the original Hypothesis tests on
   their own?
6. **PUML format:** does your shrinker parse the format in section 3 as it is?
7. **Can shrinking drop diagram elements** (a class, an enumeration, an
   attribute)? Every suite imports all model names at the top, so code
   missing one class fails the whole suite at collection: 0 tests run, not
   "a few failed". If shrinking can drop elements, we'd change the suites
   so a missing class fails only the tests that use it. Otherwise, your
   runner could report a collection error as its own outcome.
   Details: `docs/2026-10-28-hypothesis-seed-and-comparable-test-runs.md`.
