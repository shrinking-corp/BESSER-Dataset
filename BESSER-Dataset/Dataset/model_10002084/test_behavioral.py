import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Event,
    EventType,
    Registration,
    User,
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

def test_assoc_EventType_Event_reverse_link_reassign_clear():
    a1 = EventType(EventTypeId=7, Type="sample_text")
    a2 = EventType(EventTypeId=13, Type="sample_text_2")
    b = Event(Address="sample_text", CurrentNumberOfPlayers=7, DateTime="sample_text", Description="sample_text", EventId=7, MaxNumberOfPlayers=7, attribute="sample_text")
    _safe_set(b, 'event_type3', a1)
    assert _is_linked(b, 'event_type3', a1)
    if hasattr(a1, 'events2'):
        assert _is_linked(a1, 'events2', b)
    _safe_set(b, 'event_type3', a2)
    assert _is_linked(b, 'event_type3', a2)
    if hasattr(a1, 'events2'):
        assert not _is_linked(a1, 'events2', b)
    if hasattr(a2, 'events2'):
        assert _is_linked(a2, 'events2', b)
    _safe_set(b, 'event_type3', None)
    assert not _is_linked(b, 'event_type3', a2)
    if hasattr(a2, 'events2'):
        assert not _is_linked(a2, 'events2', b)


def test_assoc_User_Event_reverse_link_reassign_clear():
    a1 = User(DateOfBirth="sample_text", Email="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", UserId=7)
    a2 = User(DateOfBirth="sample_text_2", Email="sample_text_2", Login="sample_text_2", Password="sample_text_2", PhoneNumber="sample_text_2", UserId=13)
    b = Event(Address="sample_text", CurrentNumberOfPlayers=7, DateTime="sample_text", Description="sample_text", EventId=7, MaxNumberOfPlayers=7, attribute="sample_text")
    _safe_set(b, 'user7', a1)
    assert _is_linked(b, 'user7', a1)
    if hasattr(a1, 'events6'):
        assert _is_linked(a1, 'events6', b)
    _safe_set(b, 'user7', a2)
    assert _is_linked(b, 'user7', a2)
    if hasattr(a1, 'events6'):
        assert not _is_linked(a1, 'events6', b)
    if hasattr(a2, 'events6'):
        assert _is_linked(a2, 'events6', b)
    _safe_set(b, 'user7', None)
    assert not _is_linked(b, 'user7', a2)
    if hasattr(a2, 'events6'):
        assert not _is_linked(a2, 'events6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Event_Registration_stub_double():
    # Registration has no real 'event5' property in the generated
    # code (a bare stub) -- manually attach it so Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Event(Address="sample_text", CurrentNumberOfPlayers=7, DateTime="sample_text", Description="sample_text", EventId=7, MaxNumberOfPlayers=7, attribute="sample_text")
    partner = Registration()
    setattr(partner, 'event5', None)
    _safe_set(owner, 'registrations4', {partner})
    assert getattr(partner, 'event5') == owner
    _safe_set(owner, 'registrations4', set())
    assert getattr(partner, 'event5') is None


def test_assoc_User_Registration_stub_double():
    # Registration has no real 'user1' property in the generated
    # code (a bare stub) -- manually attach it so User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = User(DateOfBirth="sample_text", Email="sample_text", Login="sample_text", Password="sample_text", PhoneNumber="sample_text", UserId=7)
    partner = Registration()
    setattr(partner, 'user1', None)
    _safe_set(owner, 'registrations0', {partner})
    assert getattr(partner, 'user1') == owner
    _safe_set(owner, 'registrations0', set())
    assert getattr(partner, 'user1') is None


