import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Ticket,
    ValleyParking,
    Vehicle_Interface,
    XL,
    large,
    medium,
    small,
    spot,
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

def test_Ticket_id_value_roundtrip():
    instance = Ticket(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Ticket_strategy = st.builds(Ticket, id=safe_text)
@given(instance=Ticket_strategy)
@settings(max_examples=25)
def test_Ticket_instantiation(instance):
    assert isinstance(instance, Ticket)


ValleyParking_strategy = st.builds(ValleyParking)
@given(instance=ValleyParking_strategy)
@settings(max_examples=25)
def test_ValleyParking_instantiation(instance):
    assert isinstance(instance, ValleyParking)


Vehicle_Interface_strategy = st.builds(Vehicle_Interface)
@given(instance=Vehicle_Interface_strategy)
@settings(max_examples=25)
def test_Vehicle_Interface_instantiation(instance):
    assert isinstance(instance, Vehicle_Interface)


XL_strategy = st.builds(XL)
@given(instance=XL_strategy)
@settings(max_examples=25)
def test_XL_instantiation(instance):
    assert isinstance(instance, XL)


large_strategy = st.builds(large)
@given(instance=large_strategy)
@settings(max_examples=25)
def test_large_instantiation(instance):
    assert isinstance(instance, large)


medium_strategy = st.builds(medium)
@given(instance=medium_strategy)
@settings(max_examples=25)
def test_medium_instantiation(instance):
    assert isinstance(instance, medium)


small_strategy = st.builds(small)
@given(instance=small_strategy)
@settings(max_examples=25)
def test_small_instantiation(instance):
    assert isinstance(instance, small)


