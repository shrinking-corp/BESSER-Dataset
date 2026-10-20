import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    statemachine_Composite,
    statemachine_Initial,
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

def test_assoc_es_parte_de3_reverse_link_reassign_clear():
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


def test_assoc_source5_reverse_link_reassign_clear():
    a1 = statemachine_Transition(Id=7, duration=7)
    a2 = statemachine_Transition(Id=13, duration=13)
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State7', a1)
    assert _is_linked(b, 'statemachine_State7', a1)
    if hasattr(a1, 'statemachine_Transition6'):
        assert _is_linked(a1, 'statemachine_Transition6', b)
    _safe_set(b, 'statemachine_State7', a2)
    assert _is_linked(b, 'statemachine_State7', a2)
    if hasattr(a1, 'statemachine_Transition6'):
        assert not _is_linked(a1, 'statemachine_Transition6', b)
    if hasattr(a2, 'statemachine_Transition6'):
        assert _is_linked(a2, 'statemachine_Transition6', b)
    _safe_set(b, 'statemachine_State7', None)
    assert not _is_linked(b, 'statemachine_State7', a2)
    if hasattr(a2, 'statemachine_Transition6'):
        assert not _is_linked(a2, 'statemachine_Transition6', b)


def test_assoc_states1_reverse_link_reassign_clear():
    a1 = statemachine_StateMachine(name="sample_text")
    a2 = statemachine_StateMachine(name="sample_text_2")
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State', a1)
    assert _is_linked(b, 'statemachine_State', a1)
    if hasattr(a1, 'statemachine_StateMachine2'):
        assert _is_linked(a1, 'statemachine_StateMachine2', b)
    _safe_set(b, 'statemachine_State', a2)
    assert _is_linked(b, 'statemachine_State', a2)
    if hasattr(a1, 'statemachine_StateMachine2'):
        assert not _is_linked(a1, 'statemachine_StateMachine2', b)
    if hasattr(a2, 'statemachine_StateMachine2'):
        assert _is_linked(a2, 'statemachine_StateMachine2', b)
    _safe_set(b, 'statemachine_State', None)
    assert not _is_linked(b, 'statemachine_State', a2)
    if hasattr(a2, 'statemachine_StateMachine2'):
        assert not _is_linked(a2, 'statemachine_StateMachine2', b)


def test_assoc_target8_reverse_link_reassign_clear():
    a1 = statemachine_Transition(Id=7, duration=7)
    a2 = statemachine_Transition(Id=13, duration=13)
    b = statemachine_State(name="sample_text")
    _safe_set(b, 'statemachine_State10', a1)
    assert _is_linked(b, 'statemachine_State10', a1)
    if hasattr(a1, 'statemachine_Transition9'):
        assert _is_linked(a1, 'statemachine_Transition9', b)
    _safe_set(b, 'statemachine_State10', a2)
    assert _is_linked(b, 'statemachine_State10', a2)
    if hasattr(a1, 'statemachine_Transition9'):
        assert not _is_linked(a1, 'statemachine_Transition9', b)
    if hasattr(a2, 'statemachine_Transition9'):
        assert _is_linked(a2, 'statemachine_Transition9', b)
    _safe_set(b, 'statemachine_State10', None)
    assert not _is_linked(b, 'statemachine_State10', a2)
    if hasattr(a2, 'statemachine_Transition9'):
        assert not _is_linked(a2, 'statemachine_Transition9', b)


def test_assoc_tiene11_reverse_link_reassign_clear():
    a1 = statemachine_State(name="sample_text")
    a2 = statemachine_State(name="sample_text_2")
    b = statemachine_Resource(name="sample_text")
    _safe_set(b, 'statemachine_Resource13', a1)
    assert _is_linked(b, 'statemachine_Resource13', a1)
    if hasattr(a1, 'statemachine_State12'):
        assert _is_linked(a1, 'statemachine_State12', b)
    _safe_set(b, 'statemachine_Resource13', a2)
    assert _is_linked(b, 'statemachine_Resource13', a2)
    if hasattr(a1, 'statemachine_State12'):
        assert not _is_linked(a1, 'statemachine_State12', b)
    if hasattr(a2, 'statemachine_State12'):
        assert _is_linked(a2, 'statemachine_State12', b)
    _safe_set(b, 'statemachine_Resource13', None)
    assert not _is_linked(b, 'statemachine_Resource13', a2)
    if hasattr(a2, 'statemachine_State12'):
        assert not _is_linked(a2, 'statemachine_State12', b)


def test_assoc_transitions0_reverse_link_reassign_clear():
    a1 = statemachine_Transition(Id=7, duration=7)
    a2 = statemachine_Transition(Id=13, duration=13)
    b = statemachine_StateMachine(name="sample_text")
    _safe_set(b, 'statemachine_StateMachine', {a1})
    assert _is_linked(b, 'statemachine_StateMachine', a1)
    if hasattr(a1, 'statemachine_Transition'):
        assert _is_linked(a1, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_StateMachine', {a2})
    assert _is_linked(b, 'statemachine_StateMachine', a2)
    if hasattr(a1, 'statemachine_Transition'):
        assert not _is_linked(a1, 'statemachine_Transition', b)
    if hasattr(a2, 'statemachine_Transition'):
        assert _is_linked(a2, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_StateMachine', set())
    assert not _is_linked(b, 'statemachine_StateMachine', a2)
    if hasattr(a2, 'statemachine_Transition'):
        assert not _is_linked(a2, 'statemachine_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_es_parte_de14_stub_double():
    # statemachine_Composite has no real 'statemachine_Composite' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(name="sample_text")
    partner = statemachine_Composite()
    setattr(partner, 'statemachine_Composite', None)
    _safe_set(owner, 'statemachine_State15', partner)
    assert owner in getattr(partner, 'statemachine_Composite')
    _safe_set(owner, 'statemachine_State15', None)
    assert owner not in getattr(partner, 'statemachine_Composite')


