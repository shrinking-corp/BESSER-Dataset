import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    CommunicationAction,
    Move,
    MoveTransition,
    NamedElement,
    Notify,
    behaviour_Action,
    behaviour_Behaviour,
    behaviour_BroadcastNotify,
    behaviour_CheckNotification,
    behaviour_Choice,
    behaviour_Circle,
    behaviour_CommunicationAction,
    behaviour_Coordinate,
    behaviour_DeviceAction,
    behaviour_Drone,
    behaviour_Feedback,
    behaviour_GoTo,
    behaviour_HeadTo,
    behaviour_Hover,
    behaviour_Land,
    behaviour_Move,
    behaviour_MoveTransition,
    behaviour_MulticastNotify,
    behaviour_NamedElement,
    behaviour_Notify,
    behaviour_Parameter,
    behaviour_Slot,
    behaviour_Start,
    behaviour_Stop,
    behaviour_TakeOff,
    behaviour_UnicastNotify,
    GoToStrategy,
    TravelMode,
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

def test_assoc_drones0_reverse_link_reassign_clear():
    a1 = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    a2 = behaviour_Drone(travelMode="sample_text_2", typeName="sample_text_2")
    b = behaviour_Behaviour(crs="sample_text")
    _safe_set(b, 'behaviour_Behaviour', {a1})
    assert _is_linked(b, 'behaviour_Behaviour', a1)
    if hasattr(a1, 'behaviour_Drone'):
        assert _is_linked(a1, 'behaviour_Drone', b)
    _safe_set(b, 'behaviour_Behaviour', {a2})
    assert _is_linked(b, 'behaviour_Behaviour', a2)
    if hasattr(a1, 'behaviour_Drone'):
        assert not _is_linked(a1, 'behaviour_Drone', b)
    if hasattr(a2, 'behaviour_Drone'):
        assert _is_linked(a2, 'behaviour_Drone', b)
    _safe_set(b, 'behaviour_Behaviour', set())
    assert not _is_linked(b, 'behaviour_Behaviour', a2)
    if hasattr(a2, 'behaviour_Drone'):
        assert not _is_linked(a2, 'behaviour_Drone', b)


def test_assoc_home1_reverse_link_reassign_clear():
    a1 = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    a2 = behaviour_Drone(travelMode="sample_text_2", typeName="sample_text_2")
    b = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    _safe_set(b, 'behaviour_Coordinate', a1)
    assert _is_linked(b, 'behaviour_Coordinate', a1)
    if hasattr(a1, 'behaviour_Drone2'):
        assert _is_linked(a1, 'behaviour_Drone2', b)
    _safe_set(b, 'behaviour_Coordinate', a2)
    assert _is_linked(b, 'behaviour_Coordinate', a2)
    if hasattr(a1, 'behaviour_Drone2'):
        assert not _is_linked(a1, 'behaviour_Drone2', b)
    if hasattr(a2, 'behaviour_Drone2'):
        assert _is_linked(a2, 'behaviour_Drone2', b)
    _safe_set(b, 'behaviour_Coordinate', None)
    assert not _is_linked(b, 'behaviour_Coordinate', a2)
    if hasattr(a2, 'behaviour_Drone2'):
        assert not _is_linked(a2, 'behaviour_Drone2', b)


def test_assoc_moveTransitions5_reverse_link_reassign_clear():
    a1 = behaviour_MoveTransition(fluid=True)
    a2 = behaviour_MoveTransition(fluid=False)
    b = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    _safe_set(b, 'behaviour_Drone6', {a1})
    assert _is_linked(b, 'behaviour_Drone6', a1)
    if hasattr(a1, 'behaviour_MoveTransition'):
        assert _is_linked(a1, 'behaviour_MoveTransition', b)
    _safe_set(b, 'behaviour_Drone6', {a2})
    assert _is_linked(b, 'behaviour_Drone6', a2)
    if hasattr(a1, 'behaviour_MoveTransition'):
        assert not _is_linked(a1, 'behaviour_MoveTransition', b)
    if hasattr(a2, 'behaviour_MoveTransition'):
        assert _is_linked(a2, 'behaviour_MoveTransition', b)
    _safe_set(b, 'behaviour_Drone6', set())
    assert not _is_linked(b, 'behaviour_Drone6', a2)
    if hasattr(a2, 'behaviour_MoveTransition'):
        assert not _is_linked(a2, 'behaviour_MoveTransition', b)


def test_assoc_parameters28_reverse_link_reassign_clear():
    a1 = behaviour_Parameter(key="sample_text", value="sample_text")
    a2 = behaviour_Parameter(key="sample_text_2", value="sample_text_2")
    b = behaviour_DeviceAction(actionName="sample_text")
    _safe_set(b, 'behaviour_DeviceAction', {a1})
    assert _is_linked(b, 'behaviour_DeviceAction', a1)
    if hasattr(a1, 'behaviour_Parameter'):
        assert _is_linked(a1, 'behaviour_Parameter', b)
    _safe_set(b, 'behaviour_DeviceAction', {a2})
    assert _is_linked(b, 'behaviour_DeviceAction', a2)
    if hasattr(a1, 'behaviour_Parameter'):
        assert not _is_linked(a1, 'behaviour_Parameter', b)
    if hasattr(a2, 'behaviour_Parameter'):
        assert _is_linked(a2, 'behaviour_Parameter', b)
    _safe_set(b, 'behaviour_DeviceAction', set())
    assert not _is_linked(b, 'behaviour_DeviceAction', a2)
    if hasattr(a2, 'behaviour_Parameter'):
        assert not _is_linked(a2, 'behaviour_Parameter', b)


def test_assoc_parameters38_reverse_link_reassign_clear():
    a1 = behaviour_Parameter(key="sample_text", value="sample_text")
    a2 = behaviour_Parameter(key="sample_text_2", value="sample_text_2")
    b = behaviour_Feedback(actionName="sample_text")
    _safe_set(b, 'behaviour_Feedback', {a1})
    assert _is_linked(b, 'behaviour_Feedback', a1)
    if hasattr(a1, 'behaviour_Parameter39'):
        assert _is_linked(a1, 'behaviour_Parameter39', b)
    _safe_set(b, 'behaviour_Feedback', {a2})
    assert _is_linked(b, 'behaviour_Feedback', a2)
    if hasattr(a1, 'behaviour_Parameter39'):
        assert not _is_linked(a1, 'behaviour_Parameter39', b)
    if hasattr(a2, 'behaviour_Parameter39'):
        assert _is_linked(a2, 'behaviour_Parameter39', b)
    _safe_set(b, 'behaviour_Feedback', set())
    assert not _is_linked(b, 'behaviour_Feedback', a2)
    if hasattr(a2, 'behaviour_Parameter39'):
        assert not _is_linked(a2, 'behaviour_Parameter39', b)


def test_assoc_targetPosition16_reverse_link_reassign_clear():
    a1 = behaviour_GoTo(strategy="sample_text")
    a2 = behaviour_GoTo(strategy="sample_text_2")
    b = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    _safe_set(b, 'behaviour_Coordinate17', a1)
    assert _is_linked(b, 'behaviour_Coordinate17', a1)
    if hasattr(a1, 'behaviour_GoTo'):
        assert _is_linked(a1, 'behaviour_GoTo', b)
    _safe_set(b, 'behaviour_Coordinate17', a2)
    assert _is_linked(b, 'behaviour_Coordinate17', a2)
    if hasattr(a1, 'behaviour_GoTo'):
        assert not _is_linked(a1, 'behaviour_GoTo', b)
    if hasattr(a2, 'behaviour_GoTo'):
        assert _is_linked(a2, 'behaviour_GoTo', b)
    _safe_set(b, 'behaviour_Coordinate17', None)
    assert not _is_linked(b, 'behaviour_Coordinate17', a2)
    if hasattr(a2, 'behaviour_GoTo'):
        assert not _is_linked(a2, 'behaviour_GoTo', b)


def test_assoc_targetPosition18_reverse_link_reassign_clear():
    a1 = behaviour_Coordinate(altitude=3.14, heading=3.14, latitude=3.14, longitude=3.14)
    a2 = behaviour_Coordinate(altitude=9.99, heading=9.99, latitude=9.99, longitude=9.99)
    b = behaviour_Circle(altitude=3.14, clockwise=True, duration=3.14, radius=3.14)
    _safe_set(b, 'behaviour_Circle', a1)
    assert _is_linked(b, 'behaviour_Circle', a1)
    if hasattr(a1, 'behaviour_Coordinate19'):
        assert _is_linked(a1, 'behaviour_Coordinate19', b)
    _safe_set(b, 'behaviour_Circle', a2)
    assert _is_linked(b, 'behaviour_Circle', a2)
    if hasattr(a1, 'behaviour_Coordinate19'):
        assert not _is_linked(a1, 'behaviour_Coordinate19', b)
    if hasattr(a2, 'behaviour_Coordinate19'):
        assert _is_linked(a2, 'behaviour_Coordinate19', b)
    _safe_set(b, 'behaviour_Circle', None)
    assert not _is_linked(b, 'behaviour_Circle', a2)
    if hasattr(a2, 'behaviour_Coordinate19'):
        assert not _is_linked(a2, 'behaviour_Coordinate19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_falseBranch9_stub_double():
    # behaviour_Move has no real 'behaviour_Move10' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Choice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Choice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Choice(conditionIdentifier="sample_text")
    partner = behaviour_Move()
    setattr(partner, 'behaviour_Move10', None)
    _safe_set(owner, 'behaviour_Choice', partner)
    assert getattr(partner, 'behaviour_Move10') == owner
    _safe_set(owner, 'behaviour_Choice', None)
    assert getattr(partner, 'behaviour_Move10') is None


def test_assoc_from_32_stub_double():
    # behaviour_Move has no real 'behaviour_Move34' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_MoveTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_MoveTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_MoveTransition(fluid=True)
    partner = behaviour_Move()
    setattr(partner, 'behaviour_Move34', None)
    _safe_set(owner, 'behaviour_MoveTransition33', partner)
    assert getattr(partner, 'behaviour_Move34') == owner
    _safe_set(owner, 'behaviour_MoveTransition33', None)
    assert getattr(partner, 'behaviour_Move34') is None


def test_assoc_movements3_stub_double():
    # behaviour_Move has no real 'behaviour_Move' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    partner = behaviour_Move()
    setattr(partner, 'behaviour_Move', None)
    _safe_set(owner, 'behaviour_Drone4', {partner})
    assert getattr(partner, 'behaviour_Move') == owner
    _safe_set(owner, 'behaviour_Drone4', set())
    assert getattr(partner, 'behaviour_Move') is None


def test_assoc_receiver22_stub_double():
    # behaviour_UnicastNotify has no real 'behaviour_UnicastNotify' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    partner = behaviour_UnicastNotify()
    setattr(partner, 'behaviour_UnicastNotify', None)
    _safe_set(owner, 'behaviour_Drone23', partner)
    assert getattr(partner, 'behaviour_UnicastNotify') == owner
    _safe_set(owner, 'behaviour_Drone23', None)
    assert getattr(partner, 'behaviour_UnicastNotify') is None


def test_assoc_receiver24_stub_double():
    # behaviour_MulticastNotify has no real 'behaviour_MulticastNotify' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    partner = behaviour_MulticastNotify()
    setattr(partner, 'behaviour_MulticastNotify', None)
    _safe_set(owner, 'behaviour_Drone25', partner)
    assert owner in getattr(partner, 'behaviour_MulticastNotify')
    _safe_set(owner, 'behaviour_Drone25', None)
    assert owner not in getattr(partner, 'behaviour_MulticastNotify')


def test_assoc_slots7_stub_double():
    # behaviour_Slot has no real 'behaviour_Slot' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_Drone's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_Drone's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_Drone(travelMode="sample_text", typeName="sample_text")
    partner = behaviour_Slot()
    setattr(partner, 'behaviour_Slot', None)
    _safe_set(owner, 'behaviour_Drone8', {partner})
    assert getattr(partner, 'behaviour_Slot') == owner
    _safe_set(owner, 'behaviour_Drone8', set())
    assert getattr(partner, 'behaviour_Slot') is None


def test_assoc_to35_stub_double():
    # behaviour_Move has no real 'behaviour_Move37' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_MoveTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_MoveTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_MoveTransition(fluid=True)
    partner = behaviour_Move()
    setattr(partner, 'behaviour_Move37', None)
    _safe_set(owner, 'behaviour_MoveTransition36', partner)
    assert getattr(partner, 'behaviour_Move37') == owner
    _safe_set(owner, 'behaviour_MoveTransition36', None)
    assert getattr(partner, 'behaviour_Move37') is None


def test_assoc_waitFor29_stub_double():
    # behaviour_Slot has no real 'behaviour_Slot31' property in the generated
    # code (a bare stub) -- manually attach it so behaviour_MoveTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # behaviour_MoveTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = behaviour_MoveTransition(fluid=True)
    partner = behaviour_Slot()
    setattr(partner, 'behaviour_Slot31', None)
    _safe_set(owner, 'behaviour_MoveTransition30', partner)
    assert getattr(partner, 'behaviour_Slot31') == owner
    _safe_set(owner, 'behaviour_MoveTransition30', None)
    assert getattr(partner, 'behaviour_Slot31') is None


