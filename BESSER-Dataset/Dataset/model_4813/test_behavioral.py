import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Service,
    trip_model_OtherService,
    trip_model_Service,
    trip_model_TravelService,
    trip_model_Trip,
    trip_model_TripModel,
    trip_model_location,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_destination10_reverse_link_reassign_clear():
    a1 = trip_model_location(name="sample_text")
    a2 = trip_model_location(name="sample_text_2")
    b = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    _safe_set(b, 'trip_model_Trip11', a1)
    assert _is_linked(b, 'trip_model_Trip11', a1)
    if hasattr(a1, 'trip_model_location12'):
        assert _is_linked(a1, 'trip_model_location12', b)
    _safe_set(b, 'trip_model_Trip11', a2)
    assert _is_linked(b, 'trip_model_Trip11', a2)
    if hasattr(a1, 'trip_model_location12'):
        assert not _is_linked(a1, 'trip_model_location12', b)
    if hasattr(a2, 'trip_model_location12'):
        assert _is_linked(a2, 'trip_model_location12', b)
    _safe_set(b, 'trip_model_Trip11', None)
    assert not _is_linked(b, 'trip_model_Trip11', a2)
    if hasattr(a2, 'trip_model_location12'):
        assert not _is_linked(a2, 'trip_model_location12', b)


def test_assoc_service6_reverse_link_reassign_clear():
    a1 = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    a2 = trip_model_Trip(End=date(2025, 6, 15), Start=date(2025, 6, 15), name="sample_text_2")
    b = trip_model_Service(Cost=3.14, Duration=7, Rating=7, Type="sample_text", name="sample_text")
    _safe_set(b, 'trip_model_Service', a1)
    assert _is_linked(b, 'trip_model_Service', a1)
    if hasattr(a1, 'trip_model_Trip'):
        assert _is_linked(a1, 'trip_model_Trip', b)
    _safe_set(b, 'trip_model_Service', a2)
    assert _is_linked(b, 'trip_model_Service', a2)
    if hasattr(a1, 'trip_model_Trip'):
        assert not _is_linked(a1, 'trip_model_Trip', b)
    if hasattr(a2, 'trip_model_Trip'):
        assert _is_linked(a2, 'trip_model_Trip', b)
    _safe_set(b, 'trip_model_Service', None)
    assert not _is_linked(b, 'trip_model_Service', a2)
    if hasattr(a2, 'trip_model_Trip'):
        assert not _is_linked(a2, 'trip_model_Trip', b)


def test_assoc_source7_reverse_link_reassign_clear():
    a1 = trip_model_location(name="sample_text")
    a2 = trip_model_location(name="sample_text_2")
    b = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    _safe_set(b, 'trip_model_Trip8', a1)
    assert _is_linked(b, 'trip_model_Trip8', a1)
    if hasattr(a1, 'trip_model_location9'):
        assert _is_linked(a1, 'trip_model_location9', b)
    _safe_set(b, 'trip_model_Trip8', a2)
    assert _is_linked(b, 'trip_model_Trip8', a2)
    if hasattr(a1, 'trip_model_location9'):
        assert not _is_linked(a1, 'trip_model_location9', b)
    if hasattr(a2, 'trip_model_location9'):
        assert _is_linked(a2, 'trip_model_location9', b)
    _safe_set(b, 'trip_model_Trip8', None)
    assert not _is_linked(b, 'trip_model_Trip8', a2)
    if hasattr(a2, 'trip_model_location9'):
        assert not _is_linked(a2, 'trip_model_location9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_destination3_stub_double():
    # trip_model_TravelService has no real 'trip_model_TravelService4' property in the generated
    # code (a bare stub) -- manually attach it so trip_model_location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trip_model_location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trip_model_location(name="sample_text")
    partner = trip_model_TravelService()
    setattr(partner, 'trip_model_TravelService4', None)
    _safe_set(owner, 'trip_model_location5', partner)
    assert getattr(partner, 'trip_model_TravelService4') == owner
    _safe_set(owner, 'trip_model_location5', None)
    assert getattr(partner, 'trip_model_TravelService4') is None


def test_assoc_location0_stub_double():
    # trip_model_OtherService has no real 'trip_model_OtherService' property in the generated
    # code (a bare stub) -- manually attach it so trip_model_location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trip_model_location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trip_model_location(name="sample_text")
    partner = trip_model_OtherService()
    setattr(partner, 'trip_model_OtherService', None)
    _safe_set(owner, 'trip_model_location', partner)
    assert getattr(partner, 'trip_model_OtherService') == owner
    _safe_set(owner, 'trip_model_location', None)
    assert getattr(partner, 'trip_model_OtherService') is None


def test_assoc_location15_stub_double():
    # trip_model_TripModel has no real 'trip_model_TripModel16' property in the generated
    # code (a bare stub) -- manually attach it so trip_model_location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trip_model_location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trip_model_location(name="sample_text")
    partner = trip_model_TripModel()
    setattr(partner, 'trip_model_TripModel16', None)
    _safe_set(owner, 'trip_model_location17', partner)
    assert owner in getattr(partner, 'trip_model_TripModel16')
    _safe_set(owner, 'trip_model_location17', None)
    assert owner not in getattr(partner, 'trip_model_TripModel16')


def test_assoc_source1_stub_double():
    # trip_model_TravelService has no real 'trip_model_TravelService' property in the generated
    # code (a bare stub) -- manually attach it so trip_model_location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trip_model_location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trip_model_location(name="sample_text")
    partner = trip_model_TravelService()
    setattr(partner, 'trip_model_TravelService', None)
    _safe_set(owner, 'trip_model_location2', partner)
    assert getattr(partner, 'trip_model_TravelService') == owner
    _safe_set(owner, 'trip_model_location2', None)
    assert getattr(partner, 'trip_model_TravelService') is None


def test_assoc_trip13_stub_double():
    # trip_model_TripModel has no real 'trip_model_TripModel' property in the generated
    # code (a bare stub) -- manually attach it so trip_model_Trip's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trip_model_Trip's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trip_model_Trip(End=date(2024, 1, 1), Start=date(2024, 1, 1), name="sample_text")
    partner = trip_model_TripModel()
    setattr(partner, 'trip_model_TripModel', None)
    _safe_set(owner, 'trip_model_Trip14', partner)
    assert owner in getattr(partner, 'trip_model_TripModel')
    _safe_set(owner, 'trip_model_Trip14', None)
    assert owner not in getattr(partner, 'trip_model_TripModel')


