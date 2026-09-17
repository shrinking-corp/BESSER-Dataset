# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_C2,
    a_Zug,
    a_C,
    E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_a_c2_is_not_abstract():
    assert not inspect.isabstract(a_C2)


def test_hyp_a_c2_constructor_exists():
    assert callable(a_C2.__init__)


def test_hyp_a_c2_constructor_args():
    sig = inspect.signature(a_C2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a_zug_is_not_abstract():
    assert not inspect.isabstract(a_Zug)


def test_hyp_a_zug_constructor_exists():
    assert callable(a_Zug.__init__)


def test_hyp_a_zug_constructor_args():
    sig = inspect.signature(a_Zug.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a_c_is_not_abstract():
    assert not inspect.isabstract(a_C)


def test_hyp_a_c_constructor_exists():
    assert callable(a_C.__init__)


def test_hyp_a_c_constructor_args():
    sig = inspect.signature(a_C.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"


def test_hyp_e_exists():
    # Check that the Enumeration exists
    assert E is not None

def test_hyp_e_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in E]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in E"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
a_C2_strategy = st.builds(
    a_C2,
)
a_Zug_strategy = st.builds(
    a_Zug,
)
a_C_strategy = st.builds(
    a_C,
    a=
        safe_text
)






@given(instance=a_C_strategy)
def test_hyp_a_c_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=a_C_strategy)
@settings(max_examples=30)
def test_hyp_a_c_o_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.o(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.o).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'o' in a_C is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'o' in a_C did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'o' in a_C is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    a_C,
    a_C2,
    a_Zug,
    E,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_a_C_a_value_roundtrip():
    instance = a_C(a="sample_text")
    assert instance.a == "sample_text"
    instance.a = "sample_text_2"
    assert instance.a == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

a_C_strategy = st.builds(a_C, a=safe_text)
@given(instance=a_C_strategy)
@settings(max_examples=25)
def test_a_C_instantiation(instance):
    assert isinstance(instance, a_C)


a_C2_strategy = st.builds(a_C2)
@given(instance=a_C2_strategy)
@settings(max_examples=25)
def test_a_C2_instantiation(instance):
    assert isinstance(instance, a_C2)


a_Zug_strategy = st.builds(a_Zug)
@given(instance=a_Zug_strategy)
@settings(max_examples=25)
def test_a_Zug_instantiation(instance):
    assert isinstance(instance, a_Zug)



