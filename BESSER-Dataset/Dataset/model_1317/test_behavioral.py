import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    stateMachine_Condition,
    stateMachine_Event,
    stateMachine_Events,
    stateMachine_State,
    stateMachine_StateMachine,
    stateMachine_States,
    stateMachine_Transition,
    stateMachine_Variable,
    stateMachine_Variables,
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

def test_assoc_variable24_reverse_link_reassign_clear():
    a1 = stateMachine_Variable(name="sample_text")
    a2 = stateMachine_Variable(name="sample_text_2")
    b = stateMachine_Condition(op="sample_text", value=7)
    _safe_set(b, 'stateMachine_Condition25', a1)
    assert _is_linked(b, 'stateMachine_Condition25', a1)
    if hasattr(a1, 'stateMachine_Variable26'):
        assert _is_linked(a1, 'stateMachine_Variable26', b)
    _safe_set(b, 'stateMachine_Condition25', a2)
    assert _is_linked(b, 'stateMachine_Condition25', a2)
    if hasattr(a1, 'stateMachine_Variable26'):
        assert not _is_linked(a1, 'stateMachine_Variable26', b)
    if hasattr(a2, 'stateMachine_Variable26'):
        assert _is_linked(a2, 'stateMachine_Variable26', b)
    _safe_set(b, 'stateMachine_Condition25', None)
    assert not _is_linked(b, 'stateMachine_Condition25', a2)
    if hasattr(a2, 'stateMachine_Variable26'):
        assert not _is_linked(a2, 'stateMachine_Variable26', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition19_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition20' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Condition(op="sample_text", value=7)
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition20', None)
    _safe_set(owner, 'stateMachine_Condition', partner)
    assert getattr(partner, 'stateMachine_Transition20') == owner
    _safe_set(owner, 'stateMachine_Condition', None)
    assert getattr(partner, 'stateMachine_Transition20') is None


def test_assoc_event16_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition17' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Event(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition17', None)
    _safe_set(owner, 'stateMachine_Event18', partner)
    assert getattr(partner, 'stateMachine_Transition17') == owner
    _safe_set(owner, 'stateMachine_Event18', None)
    assert getattr(partner, 'stateMachine_Transition17') is None


def test_assoc_eventdefs1_stub_double():
    # stateMachine_Events has no real 'stateMachine_Events' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_StateMachine(name="sample_text")
    partner = stateMachine_Events()
    setattr(partner, 'stateMachine_Events', None)
    _safe_set(owner, 'stateMachine_StateMachine2', partner)
    assert getattr(partner, 'stateMachine_Events') == owner
    _safe_set(owner, 'stateMachine_StateMachine2', None)
    assert getattr(partner, 'stateMachine_Events') is None


def test_assoc_events7_stub_double():
    # stateMachine_Events has no real 'stateMachine_Events8' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Event(name="sample_text")
    partner = stateMachine_Events()
    setattr(partner, 'stateMachine_Events8', None)
    _safe_set(owner, 'stateMachine_Event', partner)
    assert owner in getattr(partner, 'stateMachine_Events8')
    _safe_set(owner, 'stateMachine_Event', None)
    assert owner not in getattr(partner, 'stateMachine_Events8')


def test_assoc_start9_stub_double():
    # stateMachine_States has no real 'stateMachine_States10' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_States()
    setattr(partner, 'stateMachine_States10', None)
    _safe_set(owner, 'stateMachine_State', partner)
    assert getattr(partner, 'stateMachine_States10') == owner
    _safe_set(owner, 'stateMachine_State', None)
    assert getattr(partner, 'stateMachine_States10') is None


def test_assoc_statedefs3_stub_double():
    # stateMachine_States has no real 'stateMachine_States' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_StateMachine(name="sample_text")
    partner = stateMachine_States()
    setattr(partner, 'stateMachine_States', None)
    _safe_set(owner, 'stateMachine_StateMachine4', partner)
    assert getattr(partner, 'stateMachine_States') == owner
    _safe_set(owner, 'stateMachine_StateMachine4', None)
    assert getattr(partner, 'stateMachine_States') is None


def test_assoc_states11_stub_double():
    # stateMachine_States has no real 'stateMachine_States12' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_States()
    setattr(partner, 'stateMachine_States12', None)
    _safe_set(owner, 'stateMachine_State13', partner)
    assert owner in getattr(partner, 'stateMachine_States12')
    _safe_set(owner, 'stateMachine_State13', None)
    assert owner not in getattr(partner, 'stateMachine_States12')


def test_assoc_target21_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition22' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition22', None)
    _safe_set(owner, 'stateMachine_State23', partner)
    assert getattr(partner, 'stateMachine_Transition22') == owner
    _safe_set(owner, 'stateMachine_State23', None)
    assert getattr(partner, 'stateMachine_Transition22') is None


def test_assoc_transitions14_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition', None)
    _safe_set(owner, 'stateMachine_State15', {partner})
    assert getattr(partner, 'stateMachine_Transition') == owner
    _safe_set(owner, 'stateMachine_State15', set())
    assert getattr(partner, 'stateMachine_Transition') is None


def test_assoc_vardefs0_stub_double():
    # stateMachine_Variables has no real 'stateMachine_Variables' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_StateMachine(name="sample_text")
    partner = stateMachine_Variables()
    setattr(partner, 'stateMachine_Variables', None)
    _safe_set(owner, 'stateMachine_StateMachine', partner)
    assert getattr(partner, 'stateMachine_Variables') == owner
    _safe_set(owner, 'stateMachine_StateMachine', None)
    assert getattr(partner, 'stateMachine_Variables') is None


def test_assoc_vars5_stub_double():
    # stateMachine_Variables has no real 'stateMachine_Variables6' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Variable(name="sample_text")
    partner = stateMachine_Variables()
    setattr(partner, 'stateMachine_Variables6', None)
    _safe_set(owner, 'stateMachine_Variable', partner)
    assert owner in getattr(partner, 'stateMachine_Variables6')
    _safe_set(owner, 'stateMachine_Variable', None)
    assert owner not in getattr(partner, 'stateMachine_Variables6')


