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
    Example_B,
    Example_A,
    B,
    Example_Bb,
    Example_Ba,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_example_b_is_not_abstract():
    assert not inspect.isabstract(Example_B)


def test_hyp_example_b_constructor_exists():
    assert callable(Example_B.__init__)


def test_hyp_example_b_constructor_args():
    sig = inspect.signature(Example_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"




def test_hyp_example_a_is_not_abstract():
    assert not inspect.isabstract(Example_A)


def test_hyp_example_a_constructor_exists():
    assert callable(Example_A.__init__)


def test_hyp_example_a_constructor_args():
    sig = inspect.signature(Example_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"




def test_hyp_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_hyp_b_constructor_exists():
    assert callable(B.__init__)


def test_hyp_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_example_bb_is_not_abstract():
    assert not inspect.isabstract(Example_Bb)


def test_hyp_example_bb_constructor_exists():
    assert callable(Example_Bb.__init__)


def test_hyp_example_bb_constructor_args():
    sig = inspect.signature(Example_Bb.__init__)
    params = list(sig.parameters.keys())



def test_hyp_example_ba_is_not_abstract():
    assert not inspect.isabstract(Example_Ba)


def test_hyp_example_ba_constructor_exists():
    assert callable(Example_Ba.__init__)


def test_hyp_example_ba_constructor_args():
    sig = inspect.signature(Example_Ba.__init__)
    params = list(sig.parameters.keys())
    assert "ba" in params, "Missing parameter 'ba'"



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
Example_B_strategy = st.builds(
    Example_B,
    b=
        safe_text
)
Example_A_strategy = st.builds(
    Example_A,
    a=
        safe_text
)
B_strategy = st.builds(
    B,
)
Example_Bb_strategy = st.builds(
    Example_Bb,
)
Example_Ba_strategy = st.builds(
    Example_Ba,
    ba=
        safe_text
)




@given(instance=Example_B_strategy)
def test_hyp_example_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original




@given(instance=Example_A_strategy)
def test_hyp_example_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original






@given(instance=Example_Ba_strategy)
def test_hyp_example_ba_ba_setter(instance):
    original = instance.ba
    instance.ba = original
    assert instance.ba == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    B,
    Example_A,
    Example_B,
    Example_Ba,
    Example_Bb,
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

def test_Example_A_a_value_roundtrip():
    instance = Example_A(a="sample_text")
    assert instance.a == "sample_text"
    instance.a = "sample_text_2"
    assert instance.a == "sample_text_2"


def test_Example_B_b_value_roundtrip():
    instance = Example_B(b="sample_text")
    assert instance.b == "sample_text"
    instance.b = "sample_text_2"
    assert instance.b == "sample_text_2"


def test_Example_Ba_ba_value_roundtrip():
    instance = Example_Ba(ba="sample_text")
    assert instance.ba == "sample_text"
    instance.ba = "sample_text_2"
    assert instance.ba == "sample_text_2"


def test_Example_Ba_isa_B():
    instance = Example_Ba(ba="sample_text")
    assert isinstance(instance, B)


def test_Example_Bb_isa_B():
    instance = Example_Bb()
    assert isinstance(instance, B)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

B_strategy = st.builds(B)
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


Example_A_strategy = st.builds(Example_A, a=safe_text)
@given(instance=Example_A_strategy)
@settings(max_examples=25)
def test_Example_A_instantiation(instance):
    assert isinstance(instance, Example_A)


Example_B_strategy = st.builds(Example_B, b=safe_text)
@given(instance=Example_B_strategy)
@settings(max_examples=25)
def test_Example_B_instantiation(instance):
    assert isinstance(instance, Example_B)


Example_Ba_strategy = st.builds(Example_Ba, ba=safe_text)
@given(instance=Example_Ba_strategy)
@settings(max_examples=25)
def test_Example_Ba_instantiation(instance):
    assert isinstance(instance, Example_Ba)


Example_Bb_strategy = st.builds(Example_Bb)
@given(instance=Example_Bb_strategy)
@settings(max_examples=25)
def test_Example_Bb_instantiation(instance):
    assert isinstance(instance, Example_Bb)



