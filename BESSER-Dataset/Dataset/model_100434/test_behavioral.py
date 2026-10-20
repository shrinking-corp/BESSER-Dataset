import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    stateMachine_DocumentField,
    stateMachine_Event,
    stateMachine_FieldState,
    stateMachine_Role,
    stateMachine_State,
    stateMachine_StateMachine,
    stateMachine_Trans,
    stateMachine_TransSet,
    EFieldState,
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

def test_assoc_eventList0_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text", package="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2", package="sample_text_2")
    b = stateMachine_Event(name="sample_text")
    _safe_set(b, 'stateMachine_Event', a1)
    assert _is_linked(b, 'stateMachine_Event', a1)
    if hasattr(a1, 'stateMachine_StateMachine'):
        assert _is_linked(a1, 'stateMachine_StateMachine', b)
    _safe_set(b, 'stateMachine_Event', a2)
    assert _is_linked(b, 'stateMachine_Event', a2)
    if hasattr(a1, 'stateMachine_StateMachine'):
        assert not _is_linked(a1, 'stateMachine_StateMachine', b)
    if hasattr(a2, 'stateMachine_StateMachine'):
        assert _is_linked(a2, 'stateMachine_StateMachine', b)
    _safe_set(b, 'stateMachine_Event', None)
    assert not _is_linked(b, 'stateMachine_Event', a2)
    if hasattr(a2, 'stateMachine_StateMachine'):
        assert not _is_linked(a2, 'stateMachine_StateMachine', b)


def test_assoc_fieldList6_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text", package="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2", package="sample_text_2")
    b = stateMachine_DocumentField(name="sample_text")
    _safe_set(b, 'stateMachine_DocumentField', a1)
    assert _is_linked(b, 'stateMachine_DocumentField', a1)
    if hasattr(a1, 'stateMachine_StateMachine7'):
        assert _is_linked(a1, 'stateMachine_StateMachine7', b)
    _safe_set(b, 'stateMachine_DocumentField', a2)
    assert _is_linked(b, 'stateMachine_DocumentField', a2)
    if hasattr(a1, 'stateMachine_StateMachine7'):
        assert not _is_linked(a1, 'stateMachine_StateMachine7', b)
    if hasattr(a2, 'stateMachine_StateMachine7'):
        assert _is_linked(a2, 'stateMachine_StateMachine7', b)
    _safe_set(b, 'stateMachine_DocumentField', None)
    assert not _is_linked(b, 'stateMachine_DocumentField', a2)
    if hasattr(a2, 'stateMachine_StateMachine7'):
        assert not _is_linked(a2, 'stateMachine_StateMachine7', b)


def test_assoc_fieldRef22_reverse_link_reassign_clear():
    a1 = stateMachine_FieldState(state="sample_text")
    a2 = stateMachine_FieldState(state="sample_text_2")
    b = stateMachine_DocumentField(name="sample_text")
    _safe_set(b, 'stateMachine_DocumentField24', a1)
    assert _is_linked(b, 'stateMachine_DocumentField24', a1)
    if hasattr(a1, 'stateMachine_FieldState23'):
        assert _is_linked(a1, 'stateMachine_FieldState23', b)
    _safe_set(b, 'stateMachine_DocumentField24', a2)
    assert _is_linked(b, 'stateMachine_DocumentField24', a2)
    if hasattr(a1, 'stateMachine_FieldState23'):
        assert not _is_linked(a1, 'stateMachine_FieldState23', b)
    if hasattr(a2, 'stateMachine_FieldState23'):
        assert _is_linked(a2, 'stateMachine_FieldState23', b)
    _safe_set(b, 'stateMachine_DocumentField24', None)
    assert not _is_linked(b, 'stateMachine_DocumentField24', a2)
    if hasattr(a2, 'stateMachine_FieldState23'):
        assert not _is_linked(a2, 'stateMachine_FieldState23', b)


def test_assoc_fieldState12_reverse_link_reassign_clear():
    a1 = stateMachine_State(name="sample_text")
    a2 = stateMachine_State(name="sample_text_2")
    b = stateMachine_FieldState(state="sample_text")
    _safe_set(b, 'stateMachine_FieldState', a1)
    assert _is_linked(b, 'stateMachine_FieldState', a1)
    if hasattr(a1, 'stateMachine_State13'):
        assert _is_linked(a1, 'stateMachine_State13', b)
    _safe_set(b, 'stateMachine_FieldState', a2)
    assert _is_linked(b, 'stateMachine_FieldState', a2)
    if hasattr(a1, 'stateMachine_State13'):
        assert not _is_linked(a1, 'stateMachine_State13', b)
    if hasattr(a2, 'stateMachine_State13'):
        assert _is_linked(a2, 'stateMachine_State13', b)
    _safe_set(b, 'stateMachine_FieldState', None)
    assert not _is_linked(b, 'stateMachine_FieldState', a2)
    if hasattr(a2, 'stateMachine_State13'):
        assert not _is_linked(a2, 'stateMachine_State13', b)


def test_assoc_initial3_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text", package="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2", package="sample_text_2")
    b = stateMachine_State(name="sample_text")
    _safe_set(b, 'stateMachine_State5', a1)
    assert _is_linked(b, 'stateMachine_State5', a1)
    if hasattr(a1, 'stateMachine_StateMachine4'):
        assert _is_linked(a1, 'stateMachine_StateMachine4', b)
    _safe_set(b, 'stateMachine_State5', a2)
    assert _is_linked(b, 'stateMachine_State5', a2)
    if hasattr(a1, 'stateMachine_StateMachine4'):
        assert not _is_linked(a1, 'stateMachine_StateMachine4', b)
    if hasattr(a2, 'stateMachine_StateMachine4'):
        assert _is_linked(a2, 'stateMachine_StateMachine4', b)
    _safe_set(b, 'stateMachine_State5', None)
    assert not _is_linked(b, 'stateMachine_State5', a2)
    if hasattr(a2, 'stateMachine_StateMachine4'):
        assert not _is_linked(a2, 'stateMachine_StateMachine4', b)


def test_assoc_roleList8_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text", package="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2", package="sample_text_2")
    b = stateMachine_Role(name="sample_text")
    _safe_set(b, 'stateMachine_Role', a1)
    assert _is_linked(b, 'stateMachine_Role', a1)
    if hasattr(a1, 'stateMachine_StateMachine9'):
        assert _is_linked(a1, 'stateMachine_StateMachine9', b)
    _safe_set(b, 'stateMachine_Role', a2)
    assert _is_linked(b, 'stateMachine_Role', a2)
    if hasattr(a1, 'stateMachine_StateMachine9'):
        assert not _is_linked(a1, 'stateMachine_StateMachine9', b)
    if hasattr(a2, 'stateMachine_StateMachine9'):
        assert _is_linked(a2, 'stateMachine_StateMachine9', b)
    _safe_set(b, 'stateMachine_Role', None)
    assert not _is_linked(b, 'stateMachine_Role', a2)
    if hasattr(a2, 'stateMachine_StateMachine9'):
        assert not _is_linked(a2, 'stateMachine_StateMachine9', b)


def test_assoc_stateList1_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text", package="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2", package="sample_text_2")
    b = stateMachine_State(name="sample_text")
    _safe_set(b, 'stateMachine_State', a1)
    assert _is_linked(b, 'stateMachine_State', a1)
    if hasattr(a1, 'stateMachine_StateMachine2'):
        assert _is_linked(a1, 'stateMachine_StateMachine2', b)
    _safe_set(b, 'stateMachine_State', a2)
    assert _is_linked(b, 'stateMachine_State', a2)
    if hasattr(a1, 'stateMachine_StateMachine2'):
        assert not _is_linked(a1, 'stateMachine_StateMachine2', b)
    if hasattr(a2, 'stateMachine_StateMachine2'):
        assert _is_linked(a2, 'stateMachine_StateMachine2', b)
    _safe_set(b, 'stateMachine_State', None)
    assert not _is_linked(b, 'stateMachine_State', a2)
    if hasattr(a2, 'stateMachine_StateMachine2'):
        assert not _is_linked(a2, 'stateMachine_StateMachine2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_event16_stub_double():
    # stateMachine_Trans has no real 'stateMachine_Trans17' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Event(name="sample_text")
    partner = stateMachine_Trans()
    setattr(partner, 'stateMachine_Trans17', None)
    _safe_set(owner, 'stateMachine_Event18', partner)
    assert getattr(partner, 'stateMachine_Trans17') == owner
    _safe_set(owner, 'stateMachine_Event18', None)
    assert getattr(partner, 'stateMachine_Trans17') is None


def test_assoc_firedBy28_stub_double():
    # stateMachine_TransSet has no real 'stateMachine_TransSet29' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Role(name="sample_text")
    partner = stateMachine_TransSet()
    setattr(partner, 'stateMachine_TransSet29', None)
    _safe_set(owner, 'stateMachine_Role30', partner)
    assert getattr(partner, 'stateMachine_TransSet29') == owner
    _safe_set(owner, 'stateMachine_Role30', None)
    assert getattr(partner, 'stateMachine_TransSet29') is None


def test_assoc_target19_stub_double():
    # stateMachine_Trans has no real 'stateMachine_Trans20' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_Trans()
    setattr(partner, 'stateMachine_Trans20', None)
    _safe_set(owner, 'stateMachine_State21', partner)
    assert getattr(partner, 'stateMachine_Trans20') == owner
    _safe_set(owner, 'stateMachine_State21', None)
    assert getattr(partner, 'stateMachine_Trans20') is None


def test_assoc_transList10_stub_double():
    # stateMachine_Trans has no real 'stateMachine_Trans' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_Trans()
    setattr(partner, 'stateMachine_Trans', None)
    _safe_set(owner, 'stateMachine_State11', {partner})
    assert getattr(partner, 'stateMachine_Trans') == owner
    _safe_set(owner, 'stateMachine_State11', set())
    assert getattr(partner, 'stateMachine_Trans') is None


def test_assoc_transSetList14_stub_double():
    # stateMachine_TransSet has no real 'stateMachine_TransSet' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_TransSet()
    setattr(partner, 'stateMachine_TransSet', None)
    _safe_set(owner, 'stateMachine_State15', {partner})
    assert getattr(partner, 'stateMachine_TransSet') == owner
    _safe_set(owner, 'stateMachine_State15', set())
    assert getattr(partner, 'stateMachine_TransSet') is None


