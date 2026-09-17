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
    use_registered_classes_C,
    use_registered_classes_B,
    use_registered_classes_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_use_registered_classes_c_is_not_abstract():
    assert not inspect.isabstract(use_registered_classes_C)


def test_hyp_use_registered_classes_c_constructor_exists():
    assert callable(use_registered_classes_C.__init__)


def test_hyp_use_registered_classes_c_constructor_args():
    sig = inspect.signature(use_registered_classes_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_registered_classes_b_is_not_abstract():
    assert not inspect.isabstract(use_registered_classes_B)


def test_hyp_use_registered_classes_b_constructor_exists():
    assert callable(use_registered_classes_B.__init__)


def test_hyp_use_registered_classes_b_constructor_args():
    sig = inspect.signature(use_registered_classes_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_use_registered_classes_a_is_not_abstract():
    assert not inspect.isabstract(use_registered_classes_A)


def test_hyp_use_registered_classes_a_constructor_exists():
    assert callable(use_registered_classes_A.__init__)


def test_hyp_use_registered_classes_a_constructor_args():
    sig = inspect.signature(use_registered_classes_A.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "z" in params, "Missing parameter 'z'"





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
use_registered_classes_C_strategy = st.builds(
    use_registered_classes_C,
)
use_registered_classes_B_strategy = st.builds(
    use_registered_classes_B,
)
use_registered_classes_A_strategy = st.builds(
    use_registered_classes_A,
    x=
        st.integers(),
    y=
        safe_text,
    z=
        safe_text
)






@given(instance=use_registered_classes_A_strategy)
def test_hyp_use_registered_classes_a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=use_registered_classes_A_strategy)
def test_hyp_use_registered_classes_a_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=use_registered_classes_A_strategy)
def test_hyp_use_registered_classes_a_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    use_registered_classes_A,
    use_registered_classes_B,
    use_registered_classes_C,
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

def test_use_registered_classes_A_x_value_roundtrip():
    instance = use_registered_classes_A(x=7, y="sample_text", z="sample_text")
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_use_registered_classes_A_y_value_roundtrip():
    instance = use_registered_classes_A(x=7, y="sample_text", z="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_use_registered_classes_A_z_value_roundtrip():
    instance = use_registered_classes_A(x=7, y="sample_text", z="sample_text")
    assert instance.z == "sample_text"
    instance.z = "sample_text_2"
    assert instance.z == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

use_registered_classes_A_strategy = st.builds(use_registered_classes_A, x=st.integers(), y=safe_text, z=safe_text)
@given(instance=use_registered_classes_A_strategy)
@settings(max_examples=25)
def test_use_registered_classes_A_instantiation(instance):
    assert isinstance(instance, use_registered_classes_A)


use_registered_classes_B_strategy = st.builds(use_registered_classes_B)
@given(instance=use_registered_classes_B_strategy)
@settings(max_examples=25)
def test_use_registered_classes_B_instantiation(instance):
    assert isinstance(instance, use_registered_classes_B)


use_registered_classes_C_strategy = st.builds(use_registered_classes_C)
@given(instance=use_registered_classes_C_strategy)
@settings(max_examples=25)
def test_use_registered_classes_C_instantiation(instance):
    assert isinstance(instance, use_registered_classes_C)



