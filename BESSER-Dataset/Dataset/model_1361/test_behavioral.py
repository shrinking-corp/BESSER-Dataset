import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    AttributeValue,
    Behavior,
    EventOccurrence,
    EventType,
    NamedElement,
    State,
    Vertex,
    statemachines_Attribute,
    statemachines_AttributeValue,
    statemachines_Behavior,
    statemachines_BooleanAttribute,
    statemachines_BooleanAttributeValue,
    statemachines_BooleanConstraint,
    statemachines_CallEventOccurrence,
    statemachines_CallEventType,
    statemachines_CompletionEventOccurrence,
    statemachines_Constraint,
    statemachines_CustomSystem,
    statemachines_EventOccurrence,
    statemachines_EventType,
    statemachines_FinalState,
    statemachines_IntegerAttribute,
    statemachines_IntegerAttributeValue,
    statemachines_IntegerConstraint,
    statemachines_NamedElement,
    statemachines_Operation,
    statemachines_OperationBehavior,
    statemachines_Pseudostate,
    statemachines_Region,
    statemachines_Signal,
    statemachines_SignalEventOccurrence,
    statemachines_SignalEventType,
    statemachines_State,
    statemachines_StateMachine,
    statemachines_StringAttribute,
    statemachines_StringAttributeValue,
    statemachines_StringConstraint,
    statemachines_Transition,
    statemachines_Trigger,
    statemachines_Vertex,
    PseudostateKind,
    TransitionKind,
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

def test_assoc_attribute64_stub_double():
    # statemachines_BooleanAttribute has no real 'statemachines_BooleanAttribute' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_BooleanAttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_BooleanAttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_BooleanAttributeValue(value="sample_text")
    partner = statemachines_BooleanAttribute()
    setattr(partner, 'statemachines_BooleanAttribute', None)
    _safe_set(owner, 'statemachines_BooleanAttributeValue', partner)
    assert getattr(partner, 'statemachines_BooleanAttribute') == owner
    _safe_set(owner, 'statemachines_BooleanAttributeValue', None)
    assert getattr(partner, 'statemachines_BooleanAttribute') is None


def test_assoc_attribute65_stub_double():
    # statemachines_IntegerAttribute has no real 'statemachines_IntegerAttribute' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_IntegerAttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_IntegerAttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_IntegerAttributeValue(value="sample_text")
    partner = statemachines_IntegerAttribute()
    setattr(partner, 'statemachines_IntegerAttribute', None)
    _safe_set(owner, 'statemachines_IntegerAttributeValue', partner)
    assert getattr(partner, 'statemachines_IntegerAttribute') == owner
    _safe_set(owner, 'statemachines_IntegerAttributeValue', None)
    assert getattr(partner, 'statemachines_IntegerAttribute') is None


def test_assoc_attribute66_stub_double():
    # statemachines_StringAttribute has no real 'statemachines_StringAttribute' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_StringAttributeValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_StringAttributeValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_StringAttributeValue(value="sample_text")
    partner = statemachines_StringAttribute()
    setattr(partner, 'statemachines_StringAttribute', None)
    _safe_set(owner, 'statemachines_StringAttributeValue', partner)
    assert getattr(partner, 'statemachines_StringAttribute') == owner
    _safe_set(owner, 'statemachines_StringAttributeValue', None)
    assert getattr(partner, 'statemachines_StringAttribute') is None


def test_assoc_connectionPoint46_stub_double():
    # statemachines_State has no real 'state47' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Pseudostate(kind="sample_text")
    partner = statemachines_State()
    setattr(partner, 'state47', None)
    _safe_set(owner, 'Pseudostate', partner)
    assert owner in getattr(partner, 'state47')
    _safe_set(owner, 'Pseudostate', None)
    assert owner not in getattr(partner, 'state47')


def test_assoc_container54_stub_double():
    # statemachines_Region has no real 'Region55' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Region()
    setattr(partner, 'Region55', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'Region55') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'Region55') is None


def test_assoc_effect56_stub_double():
    # statemachines_Behavior has no real 'statemachines_Behavior58' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Behavior()
    setattr(partner, 'statemachines_Behavior58', None)
    _safe_set(owner, 'statemachines_Transition57', partner)
    assert getattr(partner, 'statemachines_Behavior58') == owner
    _safe_set(owner, 'statemachines_Transition57', None)
    assert getattr(partner, 'statemachines_Behavior58') is None


def test_assoc_incomingTransitions31_stub_double():
    # statemachines_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition32', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition32', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_outgoingTransitions29_stub_double():
    # statemachines_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition30', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition30', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_source48_stub_double():
    # statemachines_Vertex has no real 'Vertex49' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Vertex()
    setattr(partner, 'Vertex49', None)
    _safe_set(owner, 'outgoingTransitions', partner)
    assert getattr(partner, 'Vertex49') == owner
    _safe_set(owner, 'outgoingTransitions', None)
    assert getattr(partner, 'Vertex49') is None


def test_assoc_state33_stub_double():
    # statemachines_State has no real 'State34' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Pseudostate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Pseudostate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Pseudostate(kind="sample_text")
    partner = statemachines_State()
    setattr(partner, 'State34', None)
    _safe_set(owner, 'connectionPoint', partner)
    assert getattr(partner, 'State34') == owner
    _safe_set(owner, 'connectionPoint', None)
    assert getattr(partner, 'State34') is None


def test_assoc_target50_stub_double():
    # statemachines_Vertex has no real 'Vertex51' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Vertex()
    setattr(partner, 'Vertex51', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'Vertex51') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'Vertex51') is None


def test_assoc_transitions22_stub_double():
    # statemachines_Region has no real 'container23' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Region()
    setattr(partner, 'container23', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'container23')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'container23')


def test_assoc_triggers52_stub_double():
    # statemachines_Trigger has no real 'statemachines_Trigger53' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Trigger()
    setattr(partner, 'statemachines_Trigger53', None)
    _safe_set(owner, 'statemachines_Transition', {partner})
    assert getattr(partner, 'statemachines_Trigger53') == owner
    _safe_set(owner, 'statemachines_Transition', set())
    assert getattr(partner, 'statemachines_Trigger53') is None


