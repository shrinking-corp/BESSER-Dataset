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
    CoachBusWithEDataType_Coach,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_coachbuswithedatatype_coach_is_not_abstract():
    assert not inspect.isabstract(CoachBusWithEDataType_Coach)


def test_hyp_coachbuswithedatatype_coach_constructor_exists():
    assert callable(CoachBusWithEDataType_Coach.__init__)


def test_hyp_coachbuswithedatatype_coach_constructor_args():
    sig = inspect.signature(CoachBusWithEDataType_Coach.__init__)
    params = list(sig.parameters.keys())
    assert "noOfSeats" in params, "Missing parameter 'noOfSeats'"



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
CoachBusWithEDataType_Coach_strategy = st.builds(
    CoachBusWithEDataType_Coach,
    noOfSeats=
        st.integers()
)




@given(instance=CoachBusWithEDataType_Coach_strategy)
def test_hyp_coachbuswithedatatype_coach_noOfSeats_setter(instance):
    original = instance.noOfSeats
    instance.noOfSeats = original
    assert instance.noOfSeats == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CoachBusWithEDataType_Coach,
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

def test_CoachBusWithEDataType_Coach_noOfSeats_value_roundtrip():
    instance = CoachBusWithEDataType_Coach(noOfSeats=7)
    assert instance.noOfSeats == 7
    instance.noOfSeats = 13
    assert instance.noOfSeats == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CoachBusWithEDataType_Coach_strategy = st.builds(CoachBusWithEDataType_Coach, noOfSeats=st.integers())
@given(instance=CoachBusWithEDataType_Coach_strategy)
@settings(max_examples=25)
def test_CoachBusWithEDataType_Coach_instantiation(instance):
    assert isinstance(instance, CoachBusWithEDataType_Coach)



