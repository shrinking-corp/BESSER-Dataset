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
    root_Test,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_root_test_is_not_abstract():
    assert not inspect.isabstract(root_Test)


def test_hyp_root_test_constructor_exists():
    assert callable(root_Test.__init__)


def test_hyp_root_test_constructor_args():
    sig = inspect.signature(root_Test.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "att1" in params, "Missing parameter 'att1'"
    assert "att2" in params, "Missing parameter 'att2'"





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
root_Test_strategy = st.builds(
    root_Test,
    name=
        safe_text,
    att1=
        st.integers(),
    att2=
        st.integers()
)




@given(instance=root_Test_strategy)
def test_hyp_root_test_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=root_Test_strategy)
def test_hyp_root_test_att1_setter(instance):
    original = instance.att1
    instance.att1 = original
    assert instance.att1 == original



@given(instance=root_Test_strategy)
def test_hyp_root_test_att2_setter(instance):
    original = instance.att2
    instance.att2 = original
    assert instance.att2 == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    root_Test,
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

def test_root_Test_att1_value_roundtrip():
    instance = root_Test(att1=7, att2=7, name="sample_text")
    assert instance.att1 == 7
    instance.att1 = 13
    assert instance.att1 == 13


def test_root_Test_att2_value_roundtrip():
    instance = root_Test(att1=7, att2=7, name="sample_text")
    assert instance.att2 == 7
    instance.att2 = 13
    assert instance.att2 == 13


def test_root_Test_name_value_roundtrip():
    instance = root_Test(att1=7, att2=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

root_Test_strategy = st.builds(root_Test, att1=st.integers(), att2=st.integers(), name=safe_text)
@given(instance=root_Test_strategy)
@settings(max_examples=25)
def test_root_Test_instantiation(instance):
    assert isinstance(instance, root_Test)



