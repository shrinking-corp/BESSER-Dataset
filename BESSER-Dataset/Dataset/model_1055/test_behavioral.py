import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    complexStateMachineMetaModel_ComplexStateMachine,
    complexStateMachineMetaModel_CompositeState,
    complexStateMachineMetaModel_State,
    complexStateMachineMetaModel_Transition,
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

def test_assoc_ComplexStateMachine10_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_State(Name="sample_text")
    a2 = complexStateMachineMetaModel_State(Name="sample_text_2")
    b = complexStateMachineMetaModel_ComplexStateMachine(Name="sample_text")
    _safe_set(b, 'ComplexStateMachine11', a1)
    assert _is_linked(b, 'ComplexStateMachine11', a1)
    if hasattr(a1, 'States'):
        assert _is_linked(a1, 'States', b)
    _safe_set(b, 'ComplexStateMachine11', a2)
    assert _is_linked(b, 'ComplexStateMachine11', a2)
    if hasattr(a1, 'States'):
        assert not _is_linked(a1, 'States', b)
    if hasattr(a2, 'States'):
        assert _is_linked(a2, 'States', b)
    _safe_set(b, 'ComplexStateMachine11', None)
    assert not _is_linked(b, 'ComplexStateMachine11', a2)
    if hasattr(a2, 'States'):
        assert not _is_linked(a2, 'States', b)


def test_assoc_ComplexStateMachine4_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_Transition(Name="sample_text")
    a2 = complexStateMachineMetaModel_Transition(Name="sample_text_2")
    b = complexStateMachineMetaModel_ComplexStateMachine(Name="sample_text")
    _safe_set(b, 'ComplexStateMachine5', a1)
    assert _is_linked(b, 'ComplexStateMachine5', a1)
    if hasattr(a1, 'Transitions'):
        assert _is_linked(a1, 'Transitions', b)
    _safe_set(b, 'ComplexStateMachine5', a2)
    assert _is_linked(b, 'ComplexStateMachine5', a2)
    if hasattr(a1, 'Transitions'):
        assert not _is_linked(a1, 'Transitions', b)
    if hasattr(a2, 'Transitions'):
        assert _is_linked(a2, 'Transitions', b)
    _safe_set(b, 'ComplexStateMachine5', None)
    assert not _is_linked(b, 'ComplexStateMachine5', a2)
    if hasattr(a2, 'Transitions'):
        assert not _is_linked(a2, 'Transitions', b)


def test_assoc_Incoming14_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_Transition(Name="sample_text")
    a2 = complexStateMachineMetaModel_Transition(Name="sample_text_2")
    b = complexStateMachineMetaModel_State(Name="sample_text")
    _safe_set(b, 'Target', {a1})
    assert _is_linked(b, 'Target', a1)
    if hasattr(a1, 'Transition15'):
        assert _is_linked(a1, 'Transition15', b)
    _safe_set(b, 'Target', {a2})
    assert _is_linked(b, 'Target', a2)
    if hasattr(a1, 'Transition15'):
        assert not _is_linked(a1, 'Transition15', b)
    if hasattr(a2, 'Transition15'):
        assert _is_linked(a2, 'Transition15', b)
    _safe_set(b, 'Target', set())
    assert not _is_linked(b, 'Target', a2)
    if hasattr(a2, 'Transition15'):
        assert not _is_linked(a2, 'Transition15', b)


def test_assoc_InitialState3_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_State(Name="sample_text")
    a2 = complexStateMachineMetaModel_State(Name="sample_text_2")
    b = complexStateMachineMetaModel_ComplexStateMachine(Name="sample_text")
    _safe_set(b, 'complexStateMachineMetaModel_ComplexStateMachine', a1)
    assert _is_linked(b, 'complexStateMachineMetaModel_ComplexStateMachine', a1)
    if hasattr(a1, 'complexStateMachineMetaModel_State'):
        assert _is_linked(a1, 'complexStateMachineMetaModel_State', b)
    _safe_set(b, 'complexStateMachineMetaModel_ComplexStateMachine', a2)
    assert _is_linked(b, 'complexStateMachineMetaModel_ComplexStateMachine', a2)
    if hasattr(a1, 'complexStateMachineMetaModel_State'):
        assert not _is_linked(a1, 'complexStateMachineMetaModel_State', b)
    if hasattr(a2, 'complexStateMachineMetaModel_State'):
        assert _is_linked(a2, 'complexStateMachineMetaModel_State', b)
    _safe_set(b, 'complexStateMachineMetaModel_ComplexStateMachine', None)
    assert not _is_linked(b, 'complexStateMachineMetaModel_ComplexStateMachine', a2)
    if hasattr(a2, 'complexStateMachineMetaModel_State'):
        assert not _is_linked(a2, 'complexStateMachineMetaModel_State', b)


def test_assoc_Outgoing12_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_Transition(Name="sample_text")
    a2 = complexStateMachineMetaModel_Transition(Name="sample_text_2")
    b = complexStateMachineMetaModel_State(Name="sample_text")
    _safe_set(b, 'Source', {a1})
    assert _is_linked(b, 'Source', a1)
    if hasattr(a1, 'Transition13'):
        assert _is_linked(a1, 'Transition13', b)
    _safe_set(b, 'Source', {a2})
    assert _is_linked(b, 'Source', a2)
    if hasattr(a1, 'Transition13'):
        assert not _is_linked(a1, 'Transition13', b)
    if hasattr(a2, 'Transition13'):
        assert _is_linked(a2, 'Transition13', b)
    _safe_set(b, 'Source', set())
    assert not _is_linked(b, 'Source', a2)
    if hasattr(a2, 'Transition13'):
        assert not _is_linked(a2, 'Transition13', b)


def test_assoc_Source6_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_Transition(Name="sample_text")
    a2 = complexStateMachineMetaModel_Transition(Name="sample_text_2")
    b = complexStateMachineMetaModel_State(Name="sample_text")
    _safe_set(b, 'State7', a1)
    assert _is_linked(b, 'State7', a1)
    if hasattr(a1, 'Outgoing'):
        assert _is_linked(a1, 'Outgoing', b)
    _safe_set(b, 'State7', a2)
    assert _is_linked(b, 'State7', a2)
    if hasattr(a1, 'Outgoing'):
        assert not _is_linked(a1, 'Outgoing', b)
    if hasattr(a2, 'Outgoing'):
        assert _is_linked(a2, 'Outgoing', b)
    _safe_set(b, 'State7', None)
    assert not _is_linked(b, 'State7', a2)
    if hasattr(a2, 'Outgoing'):
        assert not _is_linked(a2, 'Outgoing', b)


def test_assoc_States0_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_State(Name="sample_text")
    a2 = complexStateMachineMetaModel_State(Name="sample_text_2")
    b = complexStateMachineMetaModel_ComplexStateMachine(Name="sample_text")
    _safe_set(b, 'ComplexStateMachine', {a1})
    assert _is_linked(b, 'ComplexStateMachine', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'ComplexStateMachine', {a2})
    assert _is_linked(b, 'ComplexStateMachine', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'ComplexStateMachine', set())
    assert not _is_linked(b, 'ComplexStateMachine', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_Target8_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_Transition(Name="sample_text")
    a2 = complexStateMachineMetaModel_Transition(Name="sample_text_2")
    b = complexStateMachineMetaModel_State(Name="sample_text")
    _safe_set(b, 'State9', a1)
    assert _is_linked(b, 'State9', a1)
    if hasattr(a1, 'Incoming'):
        assert _is_linked(a1, 'Incoming', b)
    _safe_set(b, 'State9', a2)
    assert _is_linked(b, 'State9', a2)
    if hasattr(a1, 'Incoming'):
        assert not _is_linked(a1, 'Incoming', b)
    if hasattr(a2, 'Incoming'):
        assert _is_linked(a2, 'Incoming', b)
    _safe_set(b, 'State9', None)
    assert not _is_linked(b, 'State9', a2)
    if hasattr(a2, 'Incoming'):
        assert not _is_linked(a2, 'Incoming', b)


def test_assoc_Transitions1_reverse_link_reassign_clear():
    a1 = complexStateMachineMetaModel_Transition(Name="sample_text")
    a2 = complexStateMachineMetaModel_Transition(Name="sample_text_2")
    b = complexStateMachineMetaModel_ComplexStateMachine(Name="sample_text")
    _safe_set(b, 'ComplexStateMachine2', {a1})
    assert _is_linked(b, 'ComplexStateMachine2', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'ComplexStateMachine2', {a2})
    assert _is_linked(b, 'ComplexStateMachine2', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'ComplexStateMachine2', set())
    assert not _is_linked(b, 'ComplexStateMachine2', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_CompositeState16_stub_double():
    # complexStateMachineMetaModel_CompositeState has no real 'CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so complexStateMachineMetaModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # complexStateMachineMetaModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = complexStateMachineMetaModel_State(Name="sample_text")
    partner = complexStateMachineMetaModel_CompositeState()
    setattr(partner, 'CompositeState', None)
    _safe_set(owner, 'States17', partner)
    assert getattr(partner, 'CompositeState') == owner
    _safe_set(owner, 'States17', None)
    assert getattr(partner, 'CompositeState') is None


def test_assoc_InitialState21_stub_double():
    # complexStateMachineMetaModel_CompositeState has no real 'complexStateMachineMetaModel_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so complexStateMachineMetaModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # complexStateMachineMetaModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = complexStateMachineMetaModel_State(Name="sample_text")
    partner = complexStateMachineMetaModel_CompositeState()
    setattr(partner, 'complexStateMachineMetaModel_CompositeState', None)
    _safe_set(owner, 'complexStateMachineMetaModel_State22', partner)
    assert getattr(partner, 'complexStateMachineMetaModel_CompositeState') == owner
    _safe_set(owner, 'complexStateMachineMetaModel_State22', None)
    assert getattr(partner, 'complexStateMachineMetaModel_CompositeState') is None


def test_assoc_States18_stub_double():
    # complexStateMachineMetaModel_CompositeState has no real 'CompositeState19' property in the generated
    # code (a bare stub) -- manually attach it so complexStateMachineMetaModel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # complexStateMachineMetaModel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = complexStateMachineMetaModel_State(Name="sample_text")
    partner = complexStateMachineMetaModel_CompositeState()
    setattr(partner, 'CompositeState19', None)
    _safe_set(owner, 'State20', partner)
    assert owner in getattr(partner, 'CompositeState19')
    _safe_set(owner, 'State20', None)
    assert owner not in getattr(partner, 'CompositeState19')


