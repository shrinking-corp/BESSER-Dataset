# Do two benchmark runs test with the same Hypothesis inputs?

**Question (2026-10-28).** The benchmark runs a model's `test_super_suite.py`
twice: once on code generated from the original diagram, once on code
generated from the shrunk diagram. Both runs use `--hypothesis-seed=0`.
Do both runs feed the same test inputs, or can the random values differ
between runs (e.g. because tests or models run in another order)? If they
differ, comparing the two runs would be invalid.

**Answer.** The inputs are the same. With the seed, every test gets the same
examples in every run, whatever the order of tests, models or runs, as long
as:
- both runs use the same test file, Python 3.11 and Hypothesis 6.167.1;
- both generated codes have the same constructor signatures (the API in
  `docs/handout.md` section 4).

There is one way the generated code can change the inputs (an extra
required constructor parameter), and it only happens when that code already
breaks the API. Separately, the suites' imports turn a single missing class
into a failure of the whole suite. That is a real risk for the comparison
and still open (last section).

Checked in Hypothesis 6.167.1 (`.venv`) and in all 5,264
`test_super_suite.py` files.

## 1. The seed is per test, not one shared stream

`hypothesis/core.py`, `get_random_for_wrapped_test` (around line 712):

```python
if global_force_seed is not None:
    return Random(global_force_seed)
```

`--hypothesis-seed=0` sets `global_force_seed`. Every `@given` test then
starts its own new `Random(0)`. It does not take numbers from one generator
shared by all tests. A test's examples therefore don't depend on which tests
ran before it, in which order, in which process, or for which model.

`run_engine` (around line 1409):

```python
if global_force_seed is None:
    database_key = function_digest(self.test)
else:
    database_key = None
```

With a seed, Hypothesis does not use its example database at all. No
example saved by an earlier run, such as a failure found on the other code,
is replayed. (Before this check we advised redirecting the database. That is
harmless but unnecessary for seeded runs.)

## 2. The code under test doesn't steer the draws

A test can make Hypothesis's next draws depend on the code's behaviour
through `assume()` (rejected examples), `target()` (search towards a value)
or `st.data()` (drawing inside the test body). Counted over all 5,264
super suites:

| Construct | Uses |
|---|---:|
| `assume(...)` | 0 (imported in some files, never called) |
| `target(...)` | 0 |
| `st.data()` / `.draw(...)` inside a test | 0 |
| `st.sampled_from`, `st.from_type` | 0 |

So a test's examples come only from the seed and its strategies. The
strategies (`safe_text`, integers, …) are defined in the test file. Enum
literals are checked by plain structural tests, not drawn. Example limits
are fixed in the file too (`max_examples=25` on 146,894 tests, 50 on 1,134,
30 on 15; the rest use Hypothesis's default).

**A failure doesn't change what came before it.** Hypothesis stops at the
first failing example and then only shrinks it. If the shrunk code fails a
test at its 7th example, the first 7 examples were exactly the ones the
other code got too. A per-test pass/fail comparison is therefore fair.

## 3. The exception: constructor signatures

The suites build objects with `st.builds(Class, ...)`: 294,982 calls, of
which 253,321 pass no arguments. For every required constructor parameter
that isn't passed explicitly, `builds` infers a strategy from the type hint
(`hypothesis/strategies/_internal/core.py`, `builds`, around line 1231). It
reads the hint from the class being tested, i.e. the generated code:

| The generated class, compared with the reference | Effect on the inputs |
|---|---|
| Same constructor parameters (no extra required ones) | nothing extra is drawn; the inputs are identical |
| An extra required parameter with a type hint | an extra value is drawn for it, and the later draws in that test shift |
| An extra required parameter without a type hint | `builds` can't fill it; the test fails |

The last two rows only occur when the generated code breaks the API the
suite tests, and such a test would very likely fail anyway. The handout
asks for type hints on attribute parameters for this reason.

## 4. What else could make two runs differ

| Factor | Effect | How to keep it fixed |
|---|---|---|
| Hypothesis version | another version can draw other examples from the same seed | pin 6.167.1 |
| Python version | text generation uses the Unicode tables of the running Python | pin 3.11 |
| The test file | another file means other strategies | use the exported `test_super_suite.py` unchanged |
| Machine load | doesn't change the inputs, but an example over 200 ms fails (Hypothesis's deadline) | don't overload the machine |
| `PYTHONHASHSEED` | doesn't change the draws; it could only affect code that depends on string-set order | optional: set it to a fixed value |

## 5. Open: one missing class fails the whole suite

Every suite imports the code under test at module level, for example in
`model_1`:

```python
from python_code import (
    petrinet_Node,
    petrinet_Petrinet,
    ...
)
```

If the generated code lacks even one of those names, the import fails while
pytest collects the file. No test runs, and the model scores 0 passed, not
"most passed, a few failed". If shrinking can drop a class, an enumeration
or anything else a test imports, the comparison becomes all-or-nothing per
model.

Options, depending on the benchmarking side's answer to whether shrinking
can drop diagram elements:
- **In our generator:** look names up when a test runs (`python_code.X`
  inside the test body), so a missing class fails only the tests that use
  it. This needs the suites regenerated and re-greened. The mutation score
  should be rechecked at least on the pilot sample, to show it doesn't move.
- **On their side:** the runner reports a collection error as its own
  outcome ("the code doesn't provide the API") rather than as 0%.

## 6. How to prove it with data (proposed, not built)

Hypothesis in verbose mode prints every example it tries, with the
`builds` arguments, not object addresses (`Trying example:
test_x(instance=petrinet_Node(name='...'))`). A small check could run one
suite on two implementations with `--hypothesis-seed=0
--hypothesis-verbosity=verbose -s`, collect the examples per test and diff
them. On the pilot sample, with the reference code and a copy that keeps the
API but changes the bodies, the result should be "identical for every
test". That would turn sections 1-3 into a measurement.
