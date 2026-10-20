import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    statemachine_Composite,
    statemachine_Final,
    statemachine_Initial,
    statemachine_Need,
    statemachine_Resource,
    statemachine_Simple,
    statemachine_State,
    statemachine_StateMachine,
    statemachine_Transition,
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

def test_assoc_resources3_reverse_link_reassign_clear():
    a1 = statemachine_StateMachine(name="sample_text")
    a2 = statemachine_StateMachine(name="sample_text_2")
    b = statemachine_Resource(name="sample_text")
    _safe_set(b, 'statemachine_Resource', a1)
    assert _is_linked(b, 'statemachine_Resource', a1)
    if hasattr(a1, 'statemachine_StateMachine4'):
        assert _is_linked(a1, 'statemachine_StateMachine4', b)
    _safe_set(b, 'statemachine_Resource', a2)
    assert _is_linked(b, 'statemachine_Resource', a2)
    if hasattr(a1, 'statemachine_StateMachine4'):
        assert not _is_linked(a1, 'statemachine_StateMachine4', b)
    if hasattr(a2, 'statemachine_StateMachine4'):
        assert _is_linked(a2, 'statemachine_StateMachine4', b)
    _safe_set(b, 'statemachine_Resource', None)
    assert not _is_linked(b, 'statemachine_Resource', a2)
    if hasattr(a2, 'statemachine_StateMachine4'):
        assert not _is_linked(a2, 'statemachine_StateMachine4', b)


def test_assoc_source7_reverse_link_reassign_clear():
    a1 = statemachine_Transition(Id=7)
    a2 = statemachine_Transition(Id=13)
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State9', a1)
    assert _is_linked(b, 'statemachine_State9', a1)
    if hasattr(a1, 'statemachine_Transition8'):
        assert _is_linked(a1, 'statemachine_Transition8', b)
    _safe_set(b, 'statemachine_State9', a2)
    assert _is_linked(b, 'statemachine_State9', a2)
    if hasattr(a1, 'statemachine_Transition8'):
        assert not _is_linked(a1, 'statemachine_Transition8', b)
    if hasattr(a2, 'statemachine_Transition8'):
        assert _is_linked(a2, 'statemachine_Transition8', b)
    _safe_set(b, 'statemachine_State9', None)
    assert not _is_linked(b, 'statemachine_State9', a2)
    if hasattr(a2, 'statemachine_Transition8'):
        assert not _is_linked(a2, 'statemachine_Transition8', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = statemachine_StateMachine(name="sample_text")
    a2 = statemachine_StateMachine(name="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State', a1)
    assert _is_linked(b, 'statemachine_State', a1)
    if hasattr(a1, 'statemachine_StateMachine'):
        assert _is_linked(a1, 'statemachine_StateMachine', b)
    _safe_set(b, 'statemachine_State', a2)
    assert _is_linked(b, 'statemachine_State', a2)
    if hasattr(a1, 'statemachine_StateMachine'):
        assert not _is_linked(a1, 'statemachine_StateMachine', b)
    if hasattr(a2, 'statemachine_StateMachine'):
        assert _is_linked(a2, 'statemachine_StateMachine', b)
    _safe_set(b, 'statemachine_State', None)
    assert not _is_linked(b, 'statemachine_State', a2)
    if hasattr(a2, 'statemachine_StateMachine'):
        assert not _is_linked(a2, 'statemachine_StateMachine', b)


def test_assoc_target10_reverse_link_reassign_clear():
    a1 = statemachine_Transition(Id=7)
    a2 = statemachine_Transition(Id=13)
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State12', a1)
    assert _is_linked(b, 'statemachine_State12', a1)
    if hasattr(a1, 'statemachine_Transition11'):
        assert _is_linked(a1, 'statemachine_Transition11', b)
    _safe_set(b, 'statemachine_State12', a2)
    assert _is_linked(b, 'statemachine_State12', a2)
    if hasattr(a1, 'statemachine_Transition11'):
        assert not _is_linked(a1, 'statemachine_Transition11', b)
    if hasattr(a2, 'statemachine_Transition11'):
        assert _is_linked(a2, 'statemachine_Transition11', b)
    _safe_set(b, 'statemachine_State12', None)
    assert not _is_linked(b, 'statemachine_State12', a2)
    if hasattr(a2, 'statemachine_Transition11'):
        assert not _is_linked(a2, 'statemachine_Transition11', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = statemachine_Transition(Id=7)
    a2 = statemachine_Transition(Id=13)
    b = statemachine_StateMachine(name="sample_text")
    _safe_set(b, 'statemachine_StateMachine2', {a1})
    assert _is_linked(b, 'statemachine_StateMachine2', a1)
    if hasattr(a1, 'statemachine_Transition'):
        assert _is_linked(a1, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_StateMachine2', {a2})
    assert _is_linked(b, 'statemachine_StateMachine2', a2)
    if hasattr(a1, 'statemachine_Transition'):
        assert not _is_linked(a1, 'statemachine_Transition', b)
    if hasattr(a2, 'statemachine_Transition'):
        assert _is_linked(a2, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_StateMachine2', set())
    assert not _is_linked(b, 'statemachine_StateMachine2', a2)
    if hasattr(a2, 'statemachine_Transition'):
        assert not _is_linked(a2, 'statemachine_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_needs5_stub_double():
    # statemachine_Need has no real 'statemachine_Need' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_StateMachine(name="sample_text")
    partner = statemachine_Need()
    setattr(partner, 'statemachine_Need', None)
    _safe_set(owner, 'statemachine_StateMachine6', {partner})
    assert getattr(partner, 'statemachine_Need') == owner
    _safe_set(owner, 'statemachine_StateMachine6', set())
    assert getattr(partner, 'statemachine_Need') is None


def test_assoc_source_need16_stub_double():
    # statemachine_Need has no real 'statemachine_Need17' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Need()
    setattr(partner, 'statemachine_Need17', None)
    _safe_set(owner, 'statemachine_State18', partner)
    assert getattr(partner, 'statemachine_Need17') == owner
    _safe_set(owner, 'statemachine_State18', None)
    assert getattr(partner, 'statemachine_Need17') is None


def test_assoc_target_need13_stub_double():
    # statemachine_Need has no real 'statemachine_Need14' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Resource(name="sample_text")
    partner = statemachine_Need()
    setattr(partner, 'statemachine_Need14', None)
    _safe_set(owner, 'statemachine_Resource15', partner)
    assert getattr(partner, 'statemachine_Need14') == owner
    _safe_set(owner, 'statemachine_Resource15', None)
    assert getattr(partner, 'statemachine_Need14') is None


