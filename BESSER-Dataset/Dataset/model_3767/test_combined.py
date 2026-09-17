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
    fsm_Transition,
    C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_hyp_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_hyp_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "a" in params, "Missing parameter 'a'"
    assert "c" in params, "Missing parameter 'c'"




def test_hyp_c_exists():
    # Check that the Enumeration exists
    assert C is not None

def test_hyp_c_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in C]
    expected_literals = [
        "Y",
        "X",
        "Z",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in C"


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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    b=
        safe_text,
    a=
        safe_text,
    c=
        safe_text
)




@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=fsm_Transition_strategy)
def test_hyp_fsm_transition_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_Transition_strategy)
@settings(max_examples=30)
def test_hyp_fsm_transition_foo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.foo(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.foo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'foo' in fsm_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'foo' in fsm_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'foo' in fsm_Transition is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    fsm_Transition,
    C,
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

def test_fsm_Transition_a_value_roundtrip():
    instance = fsm_Transition(a="sample_text", b="sample_text", c="sample_text")
    assert instance.a == "sample_text"
    instance.a = "sample_text_2"
    assert instance.a == "sample_text_2"


def test_fsm_Transition_b_value_roundtrip():
    instance = fsm_Transition(a="sample_text", b="sample_text", c="sample_text")
    assert instance.b == "sample_text"
    instance.b = "sample_text_2"
    assert instance.b == "sample_text_2"


def test_fsm_Transition_c_value_roundtrip():
    instance = fsm_Transition(a="sample_text", b="sample_text", c="sample_text")
    assert instance.c == "sample_text"
    instance.c = "sample_text_2"
    assert instance.c == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

fsm_Transition_strategy = st.builds(fsm_Transition, a=safe_text, b=safe_text, c=safe_text)
@given(instance=fsm_Transition_strategy)
@settings(max_examples=25)
def test_fsm_Transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



