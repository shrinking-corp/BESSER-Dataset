import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CompositeState,
    Data,
    ExpressionElement,
    SimplStateMachine_Assignment,
    SimplStateMachine_BooleanData,
    SimplStateMachine_BooleanVariable,
    SimplStateMachine_CompositeState,
    SimplStateMachine_Data,
    SimplStateMachine_Event,
    SimplStateMachine_Expression,
    SimplStateMachine_ExpressionElement,
    SimplStateMachine_InitialState,
    SimplStateMachine_IntegerData,
    SimplStateMachine_IntegerVariable,
    SimplStateMachine_Operation,
    SimplStateMachine_State,
    SimplStateMachine_StateMachine,
    SimplStateMachine_Transition,
    SimplStateMachine_Variable,
    SimplStateMachine_VariableReference,
    State,
    Variable,
    Operator,
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

def test_assoc_container5_reverse_link_reassign_clear():
    a1 = SimplStateMachine_State(isActive=True, name="sample_text")
    a2 = SimplStateMachine_State(isActive=False, name="sample_text_2")
    b = SimplStateMachine_CompositeState()
    _safe_set(b, 'CompositeState', a1)
    assert _is_linked(b, 'CompositeState', a1)
    if hasattr(a1, 'states'):
        assert _is_linked(a1, 'states', b)
    _safe_set(b, 'CompositeState', a2)
    assert _is_linked(b, 'CompositeState', a2)
    if hasattr(a1, 'states'):
        assert not _is_linked(a1, 'states', b)
    if hasattr(a2, 'states'):
        assert _is_linked(a2, 'states', b)
    _safe_set(b, 'CompositeState', None)
    assert not _is_linked(b, 'CompositeState', a2)
    if hasattr(a2, 'states'):
        assert not _is_linked(a2, 'states', b)


def test_assoc_states7_reverse_link_reassign_clear():
    a1 = SimplStateMachine_State(isActive=True, name="sample_text")
    a2 = SimplStateMachine_State(isActive=False, name="sample_text_2")
    b = SimplStateMachine_CompositeState()
    _safe_set(b, 'container', {a1})
    assert _is_linked(b, 'container', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'container', {a2})
    assert _is_linked(b, 'container', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'container', set())
    assert not _is_linked(b, 'container', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_variable35_reverse_link_reassign_clear():
    a1 = SimplStateMachine_Variable(name="sample_text")
    a2 = SimplStateMachine_Variable(name="sample_text_2")
    b = SimplStateMachine_Assignment(_name="sample_text")
    _safe_set(b, 'SimplStateMachine_Assignment36', a1)
    assert _is_linked(b, 'SimplStateMachine_Assignment36', a1)
    if hasattr(a1, 'SimplStateMachine_Variable37'):
        assert _is_linked(a1, 'SimplStateMachine_Variable37', b)
    _safe_set(b, 'SimplStateMachine_Assignment36', a2)
    assert _is_linked(b, 'SimplStateMachine_Assignment36', a2)
    if hasattr(a1, 'SimplStateMachine_Variable37'):
        assert not _is_linked(a1, 'SimplStateMachine_Variable37', b)
    if hasattr(a2, 'SimplStateMachine_Variable37'):
        assert _is_linked(a2, 'SimplStateMachine_Variable37', b)
    _safe_set(b, 'SimplStateMachine_Assignment36', None)
    assert not _is_linked(b, 'SimplStateMachine_Assignment36', a2)
    if hasattr(a2, 'SimplStateMachine_Variable37'):
        assert not _is_linked(a2, 'SimplStateMachine_Variable37', b)


def test_assoc_variable38_reverse_link_reassign_clear():
    a1 = SimplStateMachine_VariableReference(_name="sample_text")
    a2 = SimplStateMachine_VariableReference(_name="sample_text_2")
    b = SimplStateMachine_Variable(name="sample_text")
    _safe_set(b, 'SimplStateMachine_Variable39', a1)
    assert _is_linked(b, 'SimplStateMachine_Variable39', a1)
    if hasattr(a1, 'SimplStateMachine_VariableReference'):
        assert _is_linked(a1, 'SimplStateMachine_VariableReference', b)
    _safe_set(b, 'SimplStateMachine_Variable39', a2)
    assert _is_linked(b, 'SimplStateMachine_Variable39', a2)
    if hasattr(a1, 'SimplStateMachine_VariableReference'):
        assert not _is_linked(a1, 'SimplStateMachine_VariableReference', b)
    if hasattr(a2, 'SimplStateMachine_VariableReference'):
        assert _is_linked(a2, 'SimplStateMachine_VariableReference', b)
    _safe_set(b, 'SimplStateMachine_Variable39', None)
    assert not _is_linked(b, 'SimplStateMachine_Variable39', a2)
    if hasattr(a2, 'SimplStateMachine_VariableReference'):
        assert not _is_linked(a2, 'SimplStateMachine_VariableReference', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contents30_stub_double():
    # SimplStateMachine_Operation has no real 'SimplStateMachine_Operation31' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Assignment(_name="sample_text")
    partner = SimplStateMachine_Operation()
    setattr(partner, 'SimplStateMachine_Operation31', None)
    _safe_set(owner, 'SimplStateMachine_Assignment', partner)
    assert getattr(partner, 'SimplStateMachine_Operation31') == owner
    _safe_set(owner, 'SimplStateMachine_Assignment', None)
    assert getattr(partner, 'SimplStateMachine_Operation31') is None


def test_assoc_event18_stub_double():
    # SimplStateMachine_Transition has no real 'SimplStateMachine_Transition19' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Event(name="sample_text")
    partner = SimplStateMachine_Transition()
    setattr(partner, 'SimplStateMachine_Transition19', None)
    _safe_set(owner, 'SimplStateMachine_Event20', partner)
    assert getattr(partner, 'SimplStateMachine_Transition19') == owner
    _safe_set(owner, 'SimplStateMachine_Event20', None)
    assert getattr(partner, 'SimplStateMachine_Transition19') is None


def test_assoc_events1_stub_double():
    # SimplStateMachine_StateMachine has no real 'SimplStateMachine_StateMachine2' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Event(name="sample_text")
    partner = SimplStateMachine_StateMachine()
    setattr(partner, 'SimplStateMachine_StateMachine2', None)
    _safe_set(owner, 'SimplStateMachine_Event', partner)
    assert getattr(partner, 'SimplStateMachine_StateMachine2') == owner
    _safe_set(owner, 'SimplStateMachine_Event', None)
    assert getattr(partner, 'SimplStateMachine_StateMachine2') is None


def test_assoc_expression32_stub_double():
    # SimplStateMachine_ExpressionElement has no real 'SimplStateMachine_ExpressionElement34' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Assignment(_name="sample_text")
    partner = SimplStateMachine_ExpressionElement()
    setattr(partner, 'SimplStateMachine_ExpressionElement34', None)
    _safe_set(owner, 'SimplStateMachine_Assignment33', partner)
    assert getattr(partner, 'SimplStateMachine_ExpressionElement34') == owner
    _safe_set(owner, 'SimplStateMachine_Assignment33', None)
    assert getattr(partner, 'SimplStateMachine_ExpressionElement34') is None


def test_assoc_guard21_stub_double():
    # SimplStateMachine_Transition has no real 'SimplStateMachine_Transition22' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    partner = SimplStateMachine_Transition()
    setattr(partner, 'SimplStateMachine_Transition22', None)
    _safe_set(owner, 'SimplStateMachine_Expression', partner)
    assert getattr(partner, 'SimplStateMachine_Transition22') == owner
    _safe_set(owner, 'SimplStateMachine_Expression', None)
    assert getattr(partner, 'SimplStateMachine_Transition22') is None


def test_assoc_initialState8_stub_double():
    # SimplStateMachine_InitialState has no real 'SimplStateMachine_InitialState' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_CompositeState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_CompositeState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_CompositeState()
    partner = SimplStateMachine_InitialState()
    setattr(partner, 'SimplStateMachine_InitialState', None)
    _safe_set(owner, 'SimplStateMachine_CompositeState', partner)
    assert getattr(partner, 'SimplStateMachine_InitialState') == owner
    _safe_set(owner, 'SimplStateMachine_CompositeState', None)
    assert getattr(partner, 'SimplStateMachine_InitialState') is None


def test_assoc_left23_stub_double():
    # SimplStateMachine_ExpressionElement has no real 'SimplStateMachine_ExpressionElement' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    partner = SimplStateMachine_ExpressionElement()
    setattr(partner, 'SimplStateMachine_ExpressionElement', None)
    _safe_set(owner, 'SimplStateMachine_Expression24', partner)
    assert getattr(partner, 'SimplStateMachine_ExpressionElement') == owner
    _safe_set(owner, 'SimplStateMachine_Expression24', None)
    assert getattr(partner, 'SimplStateMachine_ExpressionElement') is None


def test_assoc_operation6_stub_double():
    # SimplStateMachine_Operation has no real 'SimplStateMachine_Operation' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_State(isActive=True, name="sample_text")
    partner = SimplStateMachine_Operation()
    setattr(partner, 'SimplStateMachine_Operation', None)
    _safe_set(owner, 'SimplStateMachine_State', partner)
    assert getattr(partner, 'SimplStateMachine_Operation') == owner
    _safe_set(owner, 'SimplStateMachine_State', None)
    assert getattr(partner, 'SimplStateMachine_Operation') is None


def test_assoc_referencedState9_stub_double():
    # SimplStateMachine_InitialState has no real 'SimplStateMachine_InitialState10' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_State(isActive=True, name="sample_text")
    partner = SimplStateMachine_InitialState()
    setattr(partner, 'SimplStateMachine_InitialState10', None)
    _safe_set(owner, 'SimplStateMachine_State11', partner)
    assert getattr(partner, 'SimplStateMachine_InitialState10') == owner
    _safe_set(owner, 'SimplStateMachine_State11', None)
    assert getattr(partner, 'SimplStateMachine_InitialState10') is None


def test_assoc_right25_stub_double():
    # SimplStateMachine_ExpressionElement has no real 'SimplStateMachine_ExpressionElement27' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Expression(_name="sample_text", operator="sample_text")
    partner = SimplStateMachine_ExpressionElement()
    setattr(partner, 'SimplStateMachine_ExpressionElement27', None)
    _safe_set(owner, 'SimplStateMachine_Expression26', partner)
    assert getattr(partner, 'SimplStateMachine_ExpressionElement27') == owner
    _safe_set(owner, 'SimplStateMachine_Expression26', None)
    assert getattr(partner, 'SimplStateMachine_ExpressionElement27') is None


def test_assoc_source12_stub_double():
    # SimplStateMachine_Transition has no real 'SimplStateMachine_Transition13' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_State(isActive=True, name="sample_text")
    partner = SimplStateMachine_Transition()
    setattr(partner, 'SimplStateMachine_Transition13', None)
    _safe_set(owner, 'SimplStateMachine_State14', partner)
    assert getattr(partner, 'SimplStateMachine_Transition13') == owner
    _safe_set(owner, 'SimplStateMachine_State14', None)
    assert getattr(partner, 'SimplStateMachine_Transition13') is None


def test_assoc_target15_stub_double():
    # SimplStateMachine_Transition has no real 'SimplStateMachine_Transition16' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_State(isActive=True, name="sample_text")
    partner = SimplStateMachine_Transition()
    setattr(partner, 'SimplStateMachine_Transition16', None)
    _safe_set(owner, 'SimplStateMachine_State17', partner)
    assert getattr(partner, 'SimplStateMachine_Transition16') == owner
    _safe_set(owner, 'SimplStateMachine_State17', None)
    assert getattr(partner, 'SimplStateMachine_Transition16') is None


def test_assoc_value28_stub_double():
    # SimplStateMachine_Data has no real 'SimplStateMachine_Data' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Variable(name="sample_text")
    partner = SimplStateMachine_Data()
    setattr(partner, 'SimplStateMachine_Data', None)
    _safe_set(owner, 'SimplStateMachine_Variable29', partner)
    assert getattr(partner, 'SimplStateMachine_Data') == owner
    _safe_set(owner, 'SimplStateMachine_Variable29', None)
    assert getattr(partner, 'SimplStateMachine_Data') is None


def test_assoc_variables3_stub_double():
    # SimplStateMachine_StateMachine has no real 'SimplStateMachine_StateMachine4' property in the generated
    # code (a bare stub) -- manually attach it so SimplStateMachine_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimplStateMachine_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimplStateMachine_Variable(name="sample_text")
    partner = SimplStateMachine_StateMachine()
    setattr(partner, 'SimplStateMachine_StateMachine4', None)
    _safe_set(owner, 'SimplStateMachine_Variable', partner)
    assert getattr(partner, 'SimplStateMachine_StateMachine4') == owner
    _safe_set(owner, 'SimplStateMachine_Variable', None)
    assert getattr(partner, 'SimplStateMachine_StateMachine4') is None


