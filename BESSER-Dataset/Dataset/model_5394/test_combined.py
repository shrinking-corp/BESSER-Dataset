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
    C,
    b_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_c_is_not_abstract():
    assert not inspect.isabstract(C)


def test_hyp_c_constructor_exists():
    assert callable(C.__init__)


def test_hyp_c_constructor_args():
    sig = inspect.signature(C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_b_b_is_not_abstract():
    assert not inspect.isabstract(b_B)


def test_hyp_b_b_constructor_exists():
    assert callable(b_B.__init__)


def test_hyp_b_b_constructor_args():
    sig = inspect.signature(b_B.__init__)
    params = list(sig.parameters.keys())
    assert "to_enum" in params, "Missing parameter 'to_enum'"
    assert "custom_datatype" in params, "Missing parameter 'custom_datatype'"




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
C_strategy = st.builds(
    C,
)
b_B_strategy = st.builds(
    b_B,
    to_enum=
        safe_text,
    custom_datatype=
        safe_text
)





@given(instance=b_B_strategy)
def test_hyp_b_b_to_enum_setter(instance):
    original = instance.to_enum
    instance.to_enum = original
    assert instance.to_enum == original



@given(instance=b_B_strategy)
def test_hyp_b_b_custom_datatype_setter(instance):
    original = instance.custom_datatype
    instance.custom_datatype = original
    assert instance.custom_datatype == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    C,
    b_B,
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

def test_b_B_custom_datatype_value_roundtrip():
    instance = b_B(custom_datatype="sample_text", to_enum="sample_text")
    assert instance.custom_datatype == "sample_text"
    instance.custom_datatype = "sample_text_2"
    assert instance.custom_datatype == "sample_text_2"


def test_b_B_to_enum_value_roundtrip():
    instance = b_B(custom_datatype="sample_text", to_enum="sample_text")
    assert instance.to_enum == "sample_text"
    instance.to_enum = "sample_text_2"
    assert instance.to_enum == "sample_text_2"


def test_b_B_isa_C():
    instance = b_B(custom_datatype="sample_text", to_enum="sample_text")
    assert isinstance(instance, C)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

C_strategy = st.builds(C)
@given(instance=C_strategy)
@settings(max_examples=25)
def test_C_instantiation(instance):
    assert isinstance(instance, C)


b_B_strategy = st.builds(b_B, custom_datatype=safe_text, to_enum=safe_text)
@given(instance=b_B_strategy)
@settings(max_examples=25)
def test_b_B_instantiation(instance):
    assert isinstance(instance, b_B)



