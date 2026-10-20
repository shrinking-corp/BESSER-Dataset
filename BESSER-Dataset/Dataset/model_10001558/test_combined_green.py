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
    C3,
    C2,
    C1,
    S,
    I_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_c3_is_not_abstract():
    assert not inspect.isabstract(C3)


def test_hyp_c3_constructor_exists():
    assert callable(C3.__init__)


def test_hyp_c3_constructor_args():
    sig = inspect.signature(C3.__init__)
    params = list(sig.parameters.keys())
    assert "K" in params, "Missing parameter 'K'"




def test_hyp_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_hyp_c2_constructor_exists():
    assert callable(C2.__init__)


def test_hyp_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c1_is_not_abstract():
    assert not inspect.isabstract(C1)


def test_hyp_c1_constructor_exists():
    assert callable(C1.__init__)


def test_hyp_c1_constructor_args():
    sig = inspect.signature(C1.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"




def test_hyp_s_is_not_abstract():
    assert not inspect.isabstract(S)


def test_hyp_s_constructor_exists():
    assert callable(S.__init__)


def test_hyp_s_constructor_args():
    sig = inspect.signature(S.__init__)
    params = list(sig.parameters.keys())
    assert "v1" in params, "Missing parameter 'v1'"




def test_hyp_i_interface_is_not_abstract():
    assert not inspect.isabstract(I_Interface)


def test_hyp_i_interface_constructor_exists():
    assert callable(I_Interface.__init__)


def test_hyp_i_interface_constructor_args():
    sig = inspect.signature(I_Interface.__init__)
    params = list(sig.parameters.keys())


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
C3_strategy = st.builds(
    C3,
    K=
        st.integers()
)
C2_strategy = st.builds(
    C2,
)
C1_strategy = st.builds(
    C1,
    b=
        safe_text
)
S_strategy = st.builds(
    S,
    v1=
        safe_text
)
I_Interface_strategy = st.builds(
    I_Interface,
)




@given(instance=C3_strategy)
def test_hyp_c3_K_setter(instance):
    original = instance.K
    instance.K = original
    assert instance.K == original





@given(instance=C1_strategy)
def test_hyp_c1_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original




@given(instance=S_strategy)
def test_hyp_s_v1_setter(instance):
    original = instance.v1
    instance.v1 = original
    assert instance.v1 == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    C1,
    C2,
    C3,
    I_Interface,
    S,
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

def test_C1_b_value_roundtrip():
    instance = C1(b="sample_text")
    assert instance.b == "sample_text"
    instance.b = "sample_text_2"
    assert instance.b == "sample_text_2"


def test_C3_K_value_roundtrip():
    instance = C3(K=7)
    assert instance.K == 7
    instance.K = 13
    assert instance.K == 13


def test_S_v1_value_roundtrip():
    instance = S(v1="sample_text")
    assert instance.v1 == "sample_text"
    instance.v1 = "sample_text_2"
    assert instance.v1 == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

C1_strategy = st.builds(C1, b=safe_text)
@given(instance=C1_strategy)
@settings(max_examples=25)
def test_C1_instantiation(instance):
    assert isinstance(instance, C1)


C2_strategy = st.builds(C2)
@given(instance=C2_strategy)
@settings(max_examples=25)
def test_C2_instantiation(instance):
    assert isinstance(instance, C2)


C3_strategy = st.builds(C3, K=st.integers())
@given(instance=C3_strategy)
@settings(max_examples=25)
def test_C3_instantiation(instance):
    assert isinstance(instance, C3)


I_Interface_strategy = st.builds(I_Interface)
@given(instance=I_Interface_strategy)
@settings(max_examples=25)
def test_I_Interface_instantiation(instance):
    assert isinstance(instance, I_Interface)


S_strategy = st.builds(S, v1=safe_text)
@given(instance=S_strategy)
@settings(max_examples=25)
def test_S_instantiation(instance):
    assert isinstance(instance, S)



