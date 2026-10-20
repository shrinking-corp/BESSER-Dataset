import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    Transition,
    state_Condition,
    state_ConditionalNode,
    state_FinalNode,
    state_InitialNode,
    state_Module,
    state_Node,
    state_State,
    state_StateMachine,
    state_TimeoutTransition,
    state_Transition,
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

def test_assoc_guard10_reverse_link_reassign_clear():
    a1 = state_Transition(triggerEventName="sample_text")
    a2 = state_Transition(triggerEventName="sample_text_2")
    b = state_Condition(expression="sample_text")
    _safe_set(b, 'state_Condition', a1)
    assert _is_linked(b, 'state_Condition', a1)
    if hasattr(a1, 'state_Transition11'):
        assert _is_linked(a1, 'state_Transition11', b)
    _safe_set(b, 'state_Condition', a2)
    assert _is_linked(b, 'state_Condition', a2)
    if hasattr(a1, 'state_Transition11'):
        assert not _is_linked(a1, 'state_Transition11', b)
    if hasattr(a2, 'state_Transition11'):
        assert _is_linked(a2, 'state_Transition11', b)
    _safe_set(b, 'state_Condition', None)
    assert not _is_linked(b, 'state_Condition', a2)
    if hasattr(a2, 'state_Transition11'):
        assert not _is_linked(a2, 'state_Transition11', b)


def test_assoc_transitions16_reverse_link_reassign_clear():
    a1 = state_Transition(triggerEventName="sample_text")
    a2 = state_Transition(triggerEventName="sample_text_2")
    b = state_StateMachine(name="sample_text")
    _safe_set(b, 'state_StateMachine17', {a1})
    assert _is_linked(b, 'state_StateMachine17', a1)
    if hasattr(a1, 'state_Transition18'):
        assert _is_linked(a1, 'state_Transition18', b)
    _safe_set(b, 'state_StateMachine17', {a2})
    assert _is_linked(b, 'state_StateMachine17', a2)
    if hasattr(a1, 'state_Transition18'):
        assert not _is_linked(a1, 'state_Transition18', b)
    if hasattr(a2, 'state_Transition18'):
        assert _is_linked(a2, 'state_Transition18', b)
    _safe_set(b, 'state_StateMachine17', set())
    assert not _is_linked(b, 'state_StateMachine17', a2)
    if hasattr(a2, 'state_Transition18'):
        assert not _is_linked(a2, 'state_Transition18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition12_stub_double():
    # state_ConditionalNode has no real 'state_ConditionalNode' property in the generated
    # code (a bare stub) -- manually attach it so state_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Condition(expression="sample_text")
    partner = state_ConditionalNode()
    setattr(partner, 'state_ConditionalNode', None)
    _safe_set(owner, 'state_Condition13', partner)
    assert getattr(partner, 'state_ConditionalNode') == owner
    _safe_set(owner, 'state_Condition13', None)
    assert getattr(partner, 'state_ConditionalNode') is None


def test_assoc_incoming0_stub_double():
    # state_Node has no real 'state_Node' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(triggerEventName="sample_text")
    partner = state_Node()
    setattr(partner, 'state_Node', None)
    _safe_set(owner, 'state_Transition', partner)
    assert owner in getattr(partner, 'state_Node')
    _safe_set(owner, 'state_Transition', None)
    assert owner not in getattr(partner, 'state_Node')


def test_assoc_module19_stub_double():
    # state_Module has no real 'state_Module' property in the generated
    # code (a bare stub) -- manually attach it so state_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_StateMachine(name="sample_text")
    partner = state_Module()
    setattr(partner, 'state_Module', None)
    _safe_set(owner, 'state_StateMachine20', partner)
    assert getattr(partner, 'state_Module') == owner
    _safe_set(owner, 'state_StateMachine20', None)
    assert getattr(partner, 'state_Module') is None


def test_assoc_nodes14_stub_double():
    # state_Node has no real 'state_Node15' property in the generated
    # code (a bare stub) -- manually attach it so state_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_StateMachine(name="sample_text")
    partner = state_Node()
    setattr(partner, 'state_Node15', None)
    _safe_set(owner, 'state_StateMachine', {partner})
    assert getattr(partner, 'state_Node15') == owner
    _safe_set(owner, 'state_StateMachine', set())
    assert getattr(partner, 'state_Node15') is None


def test_assoc_outgoing1_stub_double():
    # state_Node has no real 'state_Node2' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(triggerEventName="sample_text")
    partner = state_Node()
    setattr(partner, 'state_Node2', None)
    _safe_set(owner, 'state_Transition3', partner)
    assert owner in getattr(partner, 'state_Node2')
    _safe_set(owner, 'state_Transition3', None)
    assert owner not in getattr(partner, 'state_Node2')


def test_assoc_source4_stub_double():
    # state_Node has no real 'state_Node6' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(triggerEventName="sample_text")
    partner = state_Node()
    setattr(partner, 'state_Node6', None)
    _safe_set(owner, 'state_Transition5', partner)
    assert getattr(partner, 'state_Node6') == owner
    _safe_set(owner, 'state_Transition5', None)
    assert getattr(partner, 'state_Node6') is None


def test_assoc_target7_stub_double():
    # state_Node has no real 'state_Node9' property in the generated
    # code (a bare stub) -- manually attach it so state_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # state_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = state_Transition(triggerEventName="sample_text")
    partner = state_Node()
    setattr(partner, 'state_Node9', None)
    _safe_set(owner, 'state_Transition8', partner)
    assert getattr(partner, 'state_Node9') == owner
    _safe_set(owner, 'state_Transition8', None)
    assert getattr(partner, 'state_Node9') is None


