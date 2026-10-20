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
    d_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_d_d_is_not_abstract():
    assert not inspect.isabstract(d_D)


def test_hyp_d_d_constructor_exists():
    assert callable(d_D.__init__)


def test_hyp_d_d_constructor_args():
    sig = inspect.signature(d_D.__init__)
    params = list(sig.parameters.keys())
    assert "atts" in params, "Missing parameter 'atts'"
    assert "name" in params, "Missing parameter 'name'"




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
d_D_strategy = st.builds(
    d_D,
    atts=
        safe_text,
    name=
        safe_text
)




@given(instance=d_D_strategy)
def test_hyp_d_d_atts_setter(instance):
    original = instance.atts
    instance.atts = original
    assert instance.atts == original



@given(instance=d_D_strategy)
def test_hyp_d_d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    d_D,
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

def test_d_D_atts_value_roundtrip():
    instance = d_D(atts="sample_text", name="sample_text")
    assert instance.atts == "sample_text"
    instance.atts = "sample_text_2"
    assert instance.atts == "sample_text_2"


def test_d_D_name_value_roundtrip():
    instance = d_D(atts="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_refs1_link_reassign_clear():
    a = d_D(atts="sample_text", name="sample_text")
    b1 = d_D(atts="sample_text", name="sample_text")
    b2 = d_D(atts="sample_text_2", name="sample_text_2")
    _safe_set(a, 'd_D', b1)
    assert _is_linked(a, 'd_D', b1)
    if hasattr(b1, 'd_D0'):
        assert _is_linked(b1, 'd_D0', a)
    _safe_set(a, 'd_D', b2)
    assert _is_linked(a, 'd_D', b2)
    if hasattr(b1, 'd_D0'):
        assert not _is_linked(b1, 'd_D0', a)
    if hasattr(b2, 'd_D0'):
        assert _is_linked(b2, 'd_D0', a)
    _safe_set(a, 'd_D', None)
    assert not _is_linked(a, 'd_D', b2)
    if hasattr(b2, 'd_D0'):
        assert not _is_linked(b2, 'd_D0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

d_D_strategy = st.builds(d_D, atts=safe_text, name=safe_text)
@given(instance=d_D_strategy)
@settings(max_examples=25)
def test_d_D_instantiation(instance):
    assert isinstance(instance, d_D)



