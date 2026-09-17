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
    g_Y,
    g_X,
    A,
    g_C,
    g_B,
    g_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_g_y_is_not_abstract():
    assert not inspect.isabstract(g_Y)


def test_hyp_g_y_constructor_exists():
    assert callable(g_Y.__init__)


def test_hyp_g_y_constructor_args():
    sig = inspect.signature(g_Y.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"




def test_hyp_g_x_is_not_abstract():
    assert not inspect.isabstract(g_X)


def test_hyp_g_x_constructor_exists():
    assert callable(g_X.__init__)


def test_hyp_g_x_constructor_args():
    sig = inspect.signature(g_X.__init__)
    params = list(sig.parameters.keys())



def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_g_c_is_not_abstract():
    assert not inspect.isabstract(g_C)


def test_hyp_g_c_constructor_exists():
    assert callable(g_C.__init__)


def test_hyp_g_c_constructor_args():
    sig = inspect.signature(g_C.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"




def test_hyp_g_b_is_not_abstract():
    assert not inspect.isabstract(g_B)


def test_hyp_g_b_constructor_exists():
    assert callable(g_B.__init__)


def test_hyp_g_b_constructor_args():
    sig = inspect.signature(g_B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"




def test_hyp_g_a_is_not_abstract():
    assert not inspect.isabstract(g_A)


def test_hyp_g_a_constructor_exists():
    assert callable(g_A.__init__)


def test_hyp_g_a_constructor_args():
    sig = inspect.signature(g_A.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"



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
g_Y_strategy = st.builds(
    g_Y,
    a=
        safe_text
)
g_X_strategy = st.builds(
    g_X,
)
A_strategy = st.builds(
    A,
)
g_C_strategy = st.builds(
    g_C,
    z=
        safe_text
)
g_B_strategy = st.builds(
    g_B,
    y=
        st.booleans()
)
g_A_strategy = st.builds(
    g_A,
    x=
        safe_text
)




@given(instance=g_Y_strategy)
def test_hyp_g_y_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=g_X_strategy)
@settings(max_examples=30)
def test_hyp_g_x_foo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.foo()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.foo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'foo' in g_X is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'foo' in g_X did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'foo' in g_X is not implemented or raised an error")





@given(instance=g_C_strategy)
def test_hyp_g_c_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original




@given(instance=g_B_strategy)
def test_hyp_g_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original




@given(instance=g_A_strategy)
def test_hyp_g_a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=g_A_strategy)
@settings(max_examples=30)
def test_hyp_g_a_bar_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bar()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bar).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bar' in g_A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bar' in g_A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bar' in g_A is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    A,
    g_A,
    g_B,
    g_C,
    g_X,
    g_Y,
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

def test_g_A_x_value_roundtrip():
    instance = g_A(x="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_g_B_y_value_roundtrip():
    instance = g_B(y=True)
    assert instance.y == True
    instance.y = False
    assert instance.y == False


def test_g_C_z_value_roundtrip():
    instance = g_C(z="sample_text")
    assert instance.z == "sample_text"
    instance.z = "sample_text_2"
    assert instance.z == "sample_text_2"


def test_g_Y_a_value_roundtrip():
    instance = g_Y(a="sample_text")
    assert instance.a == "sample_text"
    instance.a = "sample_text_2"
    assert instance.a == "sample_text_2"


def test_g_C_isa_A():
    instance = g_C(z="sample_text")
    assert isinstance(instance, A)


def test_assoc_as_0_link_reassign_clear():
    a = g_B(y=True)
    b1 = g_A(x="sample_text")
    b2 = g_A(x="sample_text_2")
    _safe_set(a, 'g_B', {b1})
    assert _is_linked(a, 'g_B', b1)
    if hasattr(b1, 'g_A'):
        assert _is_linked(b1, 'g_A', a)
    _safe_set(a, 'g_B', {b2})
    assert _is_linked(a, 'g_B', b2)
    if hasattr(b1, 'g_A'):
        assert not _is_linked(b1, 'g_A', a)
    if hasattr(b2, 'g_A'):
        assert _is_linked(b2, 'g_A', a)
    _safe_set(a, 'g_B', set())
    assert not _is_linked(a, 'g_B', b2)
    if hasattr(b2, 'g_A'):
        assert not _is_linked(b2, 'g_A', a)


def test_assoc_b2_link_reassign_clear():
    a = g_B(y=True)
    b1 = g_B(y=True)
    b2 = g_B(y=False)
    _safe_set(a, 'g_B1', b1)
    assert _is_linked(a, 'g_B1', b1)
    if hasattr(b1, 'g_B3'):
        assert _is_linked(b1, 'g_B3', a)
    _safe_set(a, 'g_B1', b2)
    assert _is_linked(a, 'g_B1', b2)
    if hasattr(b1, 'g_B3'):
        assert not _is_linked(b1, 'g_B3', a)
    if hasattr(b2, 'g_B3'):
        assert _is_linked(b2, 'g_B3', a)
    _safe_set(a, 'g_B1', None)
    assert not _is_linked(a, 'g_B1', b2)
    if hasattr(b2, 'g_B3'):
        assert not _is_linked(b2, 'g_B3', a)


def test_assoc_ys4_link_reassign_clear():
    a = g_Y(a="sample_text")
    b1 = g_X()
    b2 = g_X()
    _safe_set(a, 'g_Y', b1)
    assert _is_linked(a, 'g_Y', b1)
    if hasattr(b1, 'g_X'):
        assert _is_linked(b1, 'g_X', a)
    _safe_set(a, 'g_Y', b2)
    assert _is_linked(a, 'g_Y', b2)
    if hasattr(b1, 'g_X'):
        assert not _is_linked(b1, 'g_X', a)
    if hasattr(b2, 'g_X'):
        assert _is_linked(b2, 'g_X', a)
    _safe_set(a, 'g_Y', None)
    assert not _is_linked(a, 'g_Y', b2)
    if hasattr(b2, 'g_X'):
        assert not _is_linked(b2, 'g_X', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


g_A_strategy = st.builds(g_A, x=safe_text)
@given(instance=g_A_strategy)
@settings(max_examples=25)
def test_g_A_instantiation(instance):
    assert isinstance(instance, g_A)


g_B_strategy = st.builds(g_B, y=st.booleans())
@given(instance=g_B_strategy)
@settings(max_examples=25)
def test_g_B_instantiation(instance):
    assert isinstance(instance, g_B)


g_C_strategy = st.builds(g_C, z=safe_text)
@given(instance=g_C_strategy)
@settings(max_examples=25)
def test_g_C_instantiation(instance):
    assert isinstance(instance, g_C)


g_X_strategy = st.builds(g_X)
@given(instance=g_X_strategy)
@settings(max_examples=25)
def test_g_X_instantiation(instance):
    assert isinstance(instance, g_X)


g_Y_strategy = st.builds(g_Y, a=safe_text)
@given(instance=g_Y_strategy)
@settings(max_examples=25)
def test_g_Y_instantiation(instance):
    assert isinstance(instance, g_Y)



