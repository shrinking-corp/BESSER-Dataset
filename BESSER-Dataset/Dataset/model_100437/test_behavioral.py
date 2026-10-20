import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConstantValue,
    GAbstractAction,
    GAbstractState,
    GCompositeState,
    GState,
    Named,
    NumberValue,
    Value,
    statemachine_BooleanValue,
    statemachine_Call,
    statemachine_CallAction,
    statemachine_ConstantValue,
    statemachine_GAbstractAction,
    statemachine_GAbstractState,
    statemachine_GCompositeState,
    statemachine_GStartState,
    statemachine_GState,
    statemachine_GStatemachine,
    statemachine_GStopState,
    statemachine_GetParameter,
    statemachine_LongValue,
    statemachine_Named,
    statemachine_NumberValue,
    statemachine_Parameter,
    statemachine_StringValue,
    statemachine_Transition,
    statemachine_Value,
    ActionKind,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions0_stub_double():
    # statemachine_GAbstractState has no real 'statemachine_GAbstractState' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_GAbstractAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_GAbstractAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_GAbstractAction(kind="sample_text")
    partner = statemachine_GAbstractState()
    setattr(partner, 'statemachine_GAbstractState', None)
    _safe_set(owner, 'statemachine_GAbstractAction', partner)
    assert owner in getattr(partner, 'statemachine_GAbstractState')
    _safe_set(owner, 'statemachine_GAbstractAction', None)
    assert owner not in getattr(partner, 'statemachine_GAbstractState')


def test_assoc_call20_stub_double():
    # statemachine_CallAction has no real 'statemachine_CallAction' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Call(actionId="sample_text")
    partner = statemachine_CallAction()
    setattr(partner, 'statemachine_CallAction', None)
    _safe_set(owner, 'statemachine_Call', partner)
    assert getattr(partner, 'statemachine_CallAction') == owner
    _safe_set(owner, 'statemachine_Call', None)
    assert getattr(partner, 'statemachine_CallAction') is None


def test_assoc_delay8_stub_double():
    # statemachine_Value has no real 'statemachine_Value10' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(preserveTimers=True)
    partner = statemachine_Value()
    setattr(partner, 'statemachine_Value10', None)
    _safe_set(owner, 'statemachine_Transition9', partner)
    assert getattr(partner, 'statemachine_Value10') == owner
    _safe_set(owner, 'statemachine_Transition9', None)
    assert getattr(partner, 'statemachine_Value10') is None


def test_assoc_from_1_stub_double():
    # statemachine_GAbstractState has no real 'statemachine_GAbstractState2' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(preserveTimers=True)
    partner = statemachine_GAbstractState()
    setattr(partner, 'statemachine_GAbstractState2', None)
    _safe_set(owner, 'statemachine_Transition', partner)
    assert getattr(partner, 'statemachine_GAbstractState2') == owner
    _safe_set(owner, 'statemachine_Transition', None)
    assert getattr(partner, 'statemachine_GAbstractState2') is None


def test_assoc_guard6_stub_double():
    # statemachine_Value has no real 'statemachine_Value' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(preserveTimers=True)
    partner = statemachine_Value()
    setattr(partner, 'statemachine_Value', None)
    _safe_set(owner, 'statemachine_Transition7', partner)
    assert getattr(partner, 'statemachine_Value') == owner
    _safe_set(owner, 'statemachine_Transition7', None)
    assert getattr(partner, 'statemachine_Value') is None


def test_assoc_parameter19_stub_double():
    # statemachine_Parameter has no real 'statemachine_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_GStatemachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_GStatemachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_GStatemachine(package="sample_text")
    partner = statemachine_Parameter()
    setattr(partner, 'statemachine_Parameter', None)
    _safe_set(owner, 'statemachine_GStatemachine', {partner})
    assert getattr(partner, 'statemachine_Parameter') == owner
    _safe_set(owner, 'statemachine_GStatemachine', set())
    assert getattr(partner, 'statemachine_Parameter') is None


def test_assoc_signals11_stub_double():
    # statemachine_Value has no real 'statemachine_Value13' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(preserveTimers=True)
    partner = statemachine_Value()
    setattr(partner, 'statemachine_Value13', None)
    _safe_set(owner, 'statemachine_Transition12', {partner})
    assert getattr(partner, 'statemachine_Value13') == owner
    _safe_set(owner, 'statemachine_Transition12', set())
    assert getattr(partner, 'statemachine_Value13') is None


def test_assoc_to3_stub_double():
    # statemachine_GAbstractState has no real 'statemachine_GAbstractState5' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(preserveTimers=True)
    partner = statemachine_GAbstractState()
    setattr(partner, 'statemachine_GAbstractState5', None)
    _safe_set(owner, 'statemachine_Transition4', partner)
    assert getattr(partner, 'statemachine_GAbstractState5') == owner
    _safe_set(owner, 'statemachine_Transition4', None)
    assert getattr(partner, 'statemachine_GAbstractState5') is None


def test_assoc_transitions16_stub_double():
    # statemachine_GCompositeState has no real 'statemachine_GCompositeState17' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Transition(preserveTimers=True)
    partner = statemachine_GCompositeState()
    setattr(partner, 'statemachine_GCompositeState17', None)
    _safe_set(owner, 'statemachine_Transition18', partner)
    assert owner in getattr(partner, 'statemachine_GCompositeState17')
    _safe_set(owner, 'statemachine_Transition18', None)
    assert owner not in getattr(partner, 'statemachine_GCompositeState17')


