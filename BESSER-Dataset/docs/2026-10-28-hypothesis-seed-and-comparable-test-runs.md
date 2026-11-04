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
  `docs/handout.md` section 4);
- in the 8 suites that draw enumeration literals, both have the same
  literals in the same order.

There are two ways the generated code can change the inputs (an extra
required constructor parameter, and different literals in those 8 suites;
section 3). Separately, the suites' imports would turn a single missing class
into a failure of the whole suite. The `deferred_import_errors` plugin solves
that without changing the suites (section 5).

Checked in Hypothesis 6.167.1 (`.venv`) and in all 5,264
`test_super_suite.py` files.

*Corrected 2026-11-04: the first version said no suite uses `sampled_from`
and gave 253,321 as the number of `st.builds` calls without arguments. Both
were wrong. The counts below were redone with `grep` over all 5,264 suites.*

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
| `assume(...)` | 0 (imported in every file, never called) |
| `target(...)` | 0 (the one text match is a test named `..._night_target`) |
| `st.data()` / `.draw(...)` | 0 |
| `st.from_type` | 0 |
| `@seed`, `derandomize`, settings profiles | 0 |

So a test's examples come only from the seed and its strategies. The
strategies (`safe_text`, integers, …) are defined in the test file, except
that they name generated classes and, in 8 suites, generated enumerations
(section 3). Example limits are fixed in the file too (`max_examples=25` on
146,894 tests, 50 on 1,134, 30 on 15; the rest use Hypothesis's default).

**A failure doesn't change what came before it.** Hypothesis stops at the
first failing example and then only shrinks it. If the shrunk code fails a
test at its 7th example, the first 7 examples were exactly the ones the
other code got too. A per-test pass/fail comparison is therefore fair.

## 3. The exceptions: constructor signatures and drawn enum literals

The suites build objects with `st.builds(Class, ...)`: 294,982 calls, of
which 210,504 pass no arguments. For every required constructor parameter
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

Enumerations are the second case. 8 suites contain 27 uses of
`st.sampled_from(SomeEnum)` inside a `builds` call. It reads the literals
from the generated enumeration when the test runs, so if the two codes have
different literals, or the same ones in another order, the same draw can
pick another value and the later draws in that test can shift. This matters
if shrinking can drop literals. The other 5,256 suites check enumerations
with plain structural tests and don't draw from them.

## 4. What else could make two runs differ

| Factor | Effect | How to keep it fixed |
|---|---|---|
| Hypothesis version | another version can draw other examples from the same seed | pin 6.167.1 |
| Python version | text generation uses the Unicode tables of the running Python | pin 3.11 |
| The test file | another file means other strategies | use the exported `test_super_suite.py` unchanged |
| Machine load | doesn't change the inputs, but an example over 200 ms fails (Hypothesis's deadline) | don't overload the machine |
| `PYTHONHASHSEED` | doesn't change the draws; it could only affect code that depends on string-set order | optional: set it to a fixed value |

## 5. One missing class would fail the whole suite

*Decided 2026-11-04: solved with a pytest plugin,
`scripts/deferred_import_errors.py`.*

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
"most passed, a few failed". If a class, an enumeration or anything else a
test imports is missing, the comparison becomes all-or-nothing per model.
Shrinking could cause this, and so could the code agent forgetting or
renaming a class, so the fix doesn't depend on what shrinking can drop.

**Options considered:**

| Option | Suites | Result for a missing class |
|---|---|---|
| `try/except` import, name set to `None` | regenerated | false passes |
| Plugin loaded with `-p` (**chosen**) | unchanged | only tests using it fail |
| Generators look names up per test | regenerated, re-greened, mutation rechecked | only tests using it fail (expected, not tried) |
| Runner reports a collection error | unchanged | whole model has no score |

`try/except` is not enough because `inspect.isabstract(None)` is false and
`None.__init__` is callable. The suites have 148,069 of each of those
assertions, so they would pass on a class that doesn't exist.

**How the plugin works.** Just before pytest imports the test file, it gives
`python_code` a module-level `__getattr__`, so `from python_code import X`
returns a placeholder for a missing `X`. While the file is collected the
placeholder stays inert, because `st.builds` and other installed pytest
plugins inspect it. Once tests run:
- a test whose body names a missing element fails before it starts. This is
  needed because `assert X is not None` (5,484 such asserts) runs no code on
  the placeholder, so it could never raise;
- any other touch of the placeholder raises `MissingElement`, which covers
  tests that reach it through a strategy.

When every name exists, the plugin does nothing. Our own green and mutation
runs don't load it, so the published scores aren't affected.

**Trial (2026-11-04).** Passed tests out of the total, on copies of 5 models,
each with one class or enumeration removed:

| Model | Removed | Tests using it | No plugin | `None` | Plugin |
|---|---|---|---|---|---|
| `model_1` | `petrinet_Token` (plain class) | 4 | 0/47 | 46/47 | 43/47 |
| `model_1` | `petrinet_Arc` (in another class's type hints) | 14 | 0/47 | 36/47 | 33/47 |
| `model_1` | `Node` (base class) | 6 | 0/47 | 44/47 | 41/47 |
| `model_10002070` | `int` (enumeration) | 2 | 0/85 | 83/85 | 83/85 |
| `Model_1000000002` | `SessionType` (enumeration, drawn) | 12 | 0/114 | 102/114 | 102/114 |
| `Model_1000000002` | `SkillMatchStatus` (enumeration, drawn) | 12 | 0/114 | 102/114 | 102/114 |
| `model_3506` | its only class, name starts with `test` | 7 | 0/7 | 2/7 | 0/7 |
| `model_2119` | `test_Tests` | 7 | 0/14 | 9/14 | 7/14 |

"No plugin" means a collection error: no test ran. A separate analysis of the
test files found which tests use each removed name. With the plugin, exactly
those tests failed: no false passes and no unrelated failures.

Also checked, with the plugin:
- the reference code gives the same pass/fail per test as without it;
- starting pytest from another folder gives the same results;
- a plugin file that can't be found stops the run with `Error importing plugin`;
- a syntax error in the generated code is still a collection error;
- `model_3506` and `model_2119` give the same scores with the `anyio` pytest
  plugin switched off.

**Not checked:**
- the other 5,259 models;
- the mutation score (not expected to move, as those runs don't load the
  plugin);
- whether surviving tests get the same inputs with the plugin (expected, as
  section 1 gives each test its own generator; section 6 would measure it);
- the benchmarking side's environment, which may have other pytest plugins.

The trial scripts are in the gitignored `_scratch\import_trial\`.

**Limits.** Leaving out the flag gives no warning, only today's whole-suite
failure. Code that doesn't import at all still fails collection, so their
runner should report that as its own outcome (handout, question 7).

## 6. How to prove it with data (proposed, not built)

Hypothesis in verbose mode should print every example it tries, including
the `builds` arguments (the exact output format still has to be checked; if
it prints object addresses, this needs another way to log inputs). A small
check could run one
suite on two implementations with `--hypothesis-seed=0
--hypothesis-verbosity=verbose -s`, collect the examples per test and diff
them. On the pilot sample, with the reference code and a copy that keeps the
API but changes the bodies, the result should be "identical for every
test". That would turn sections 1-3 into a measurement.
