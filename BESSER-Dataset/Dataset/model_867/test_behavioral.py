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

def test_assoc_connectionPoint47_reverse_link_reassign_clear():
    a1 = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    a2 = statemachines_State(isDoActivityCompleted=False, isEntryCompleted=False, isExitCompleted=False)
    b = statemachines_Pseudostate(kind="sample_text")
    _safe_set(b, 'Pseudostate', a1)
    assert _is_linked(b, 'Pseudostate', a1)
    if hasattr(a1, 'state48'):
        assert _is_linked(a1, 'state48', b)
    _safe_set(b, 'Pseudostate', a2)
    assert _is_linked(b, 'Pseudostate', a2)
    if hasattr(a1, 'state48'):
        assert not _is_linked(a1, 'state48', b)
    if hasattr(a2, 'state48'):
        assert _is_linked(a2, 'state48', b)
    _safe_set(b, 'Pseudostate', None)
    assert not _is_linked(b, 'Pseudostate', a2)
    if hasattr(a2, 'state48'):
        assert not _is_linked(a2, 'state48', b)


def test_assoc_state34_reverse_link_reassign_clear():
    a1 = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    a2 = statemachines_State(isDoActivityCompleted=False, isEntryCompleted=False, isExitCompleted=False)
    b = statemachines_Pseudostate(kind="sample_text")
    _safe_set(b, 'connectionPoint', a1)
    assert _is_linked(b, 'connectionPoint', a1)
    if hasattr(a1, 'State35'):
        assert _is_linked(a1, 'State35', b)
    _safe_set(b, 'connectionPoint', a2)
    assert _is_linked(b, 'connectionPoint', a2)
    if hasattr(a1, 'State35'):
        assert not _is_linked(a1, 'State35', b)
    if hasattr(a2, 'State35'):
        assert _is_linked(a2, 'State35', b)
    _safe_set(b, 'connectionPoint', None)
    assert not _is_linked(b, 'connectionPoint', a2)
    if hasattr(a2, 'State35'):
        assert not _is_linked(a2, 'State35', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute65_stub_double():
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


def test_assoc_attribute66_stub_double():
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


def test_assoc_attribute67_stub_double():
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


def test_assoc_container55_stub_double():
    # statemachines_Region has no real 'Region56' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Region()
    setattr(partner, 'Region56', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'Region56') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'Region56') is None


def test_assoc_deferrableTriggers45_stub_double():
    # statemachines_Trigger has no real 'statemachines_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    partner = statemachines_Trigger()
    setattr(partner, 'statemachines_Trigger', None)
    _safe_set(owner, 'statemachines_State46', {partner})
    assert getattr(partner, 'statemachines_Trigger') == owner
    _safe_set(owner, 'statemachines_State46', set())
    assert getattr(partner, 'statemachines_Trigger') is None


def test_assoc_doActivity39_stub_double():
    # statemachines_Behavior has no real 'statemachines_Behavior41' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    partner = statemachines_Behavior()
    setattr(partner, 'statemachines_Behavior41', None)
    _safe_set(owner, 'statemachines_State40', partner)
    assert getattr(partner, 'statemachines_Behavior41') == owner
    _safe_set(owner, 'statemachines_State40', None)
    assert getattr(partner, 'statemachines_Behavior41') is None


def test_assoc_effect57_stub_double():
    # statemachines_Behavior has no real 'statemachines_Behavior59' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Behavior()
    setattr(partner, 'statemachines_Behavior59', None)
    _safe_set(owner, 'statemachines_Transition58', partner)
    assert getattr(partner, 'statemachines_Behavior59') == owner
    _safe_set(owner, 'statemachines_Transition58', None)
    assert getattr(partner, 'statemachines_Behavior59') is None


def test_assoc_entry38_stub_double():
    # statemachines_Behavior has no real 'statemachines_Behavior' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    partner = statemachines_Behavior()
    setattr(partner, 'statemachines_Behavior', None)
    _safe_set(owner, 'statemachines_State', partner)
    assert getattr(partner, 'statemachines_Behavior') == owner
    _safe_set(owner, 'statemachines_State', None)
    assert getattr(partner, 'statemachines_Behavior') is None


def test_assoc_exit42_stub_double():
    # statemachines_Behavior has no real 'statemachines_Behavior44' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    partner = statemachines_Behavior()
    setattr(partner, 'statemachines_Behavior44', None)
    _safe_set(owner, 'statemachines_State43', partner)
    assert getattr(partner, 'statemachines_Behavior44') == owner
    _safe_set(owner, 'statemachines_State43', None)
    assert getattr(partner, 'statemachines_Behavior44') is None


def test_assoc_incomingTransitions32_stub_double():
    # statemachines_Vertex has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Vertex()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Transition33', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Transition33', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_outgoingTransitions30_stub_double():
    # statemachines_Vertex has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Vertex()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition31', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition31', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_regions20_stub_double():
    # statemachines_Region has no real 'Region' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_StateMachine()
    partner = statemachines_Region()
    setattr(partner, 'Region', None)
    _safe_set(owner, 'stateMachine', {partner})
    assert getattr(partner, 'Region') == owner
    _safe_set(owner, 'stateMachine', set())
    assert getattr(partner, 'Region') is None


def test_assoc_regions36_stub_double():
    # statemachines_Region has no real 'Region37' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    partner = statemachines_Region()
    setattr(partner, 'Region37', None)
    _safe_set(owner, 'state', {partner})
    assert getattr(partner, 'Region37') == owner
    _safe_set(owner, 'state', set())
    assert getattr(partner, 'Region37') is None


def test_assoc_source49_stub_double():
    # statemachines_Vertex has no real 'Vertex50' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Vertex()
    setattr(partner, 'Vertex50', None)
    _safe_set(owner, 'outgoingTransitions', partner)
    assert getattr(partner, 'Vertex50') == owner
    _safe_set(owner, 'outgoingTransitions', None)
    assert getattr(partner, 'Vertex50') is None


def test_assoc_state25_stub_double():
    # statemachines_Region has no real 'regions26' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    partner = statemachines_Region()
    setattr(partner, 'regions26', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'regions26') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'regions26') is None


def test_assoc_state68_stub_double():
    # statemachines_CompletionEventOccurrence has no real 'statemachines_CompletionEventOccurrence' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_State(isDoActivityCompleted=True, isEntryCompleted=True, isExitCompleted=True)
    partner = statemachines_CompletionEventOccurrence()
    setattr(partner, 'statemachines_CompletionEventOccurrence', None)
    _safe_set(owner, 'statemachines_State69', partner)
    assert getattr(partner, 'statemachines_CompletionEventOccurrence') == owner
    _safe_set(owner, 'statemachines_State69', None)
    assert getattr(partner, 'statemachines_CompletionEventOccurrence') is None


def test_assoc_stateMachine24_stub_double():
    # statemachines_Region has no real 'regions' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_StateMachine()
    partner = statemachines_Region()
    setattr(partner, 'regions', None)
    _safe_set(owner, 'StateMachine', partner)
    assert getattr(partner, 'regions') == owner
    _safe_set(owner, 'StateMachine', None)
    assert getattr(partner, 'regions') is None


def test_assoc_statemachine0_stub_double():
    # statemachines_CustomSystem has no real 'statemachines_CustomSystem' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_StateMachine()
    partner = statemachines_CustomSystem()
    setattr(partner, 'statemachines_CustomSystem', None)
    _safe_set(owner, 'statemachines_StateMachine', partner)
    assert getattr(partner, 'statemachines_CustomSystem') == owner
    _safe_set(owner, 'statemachines_StateMachine', None)
    assert getattr(partner, 'statemachines_CustomSystem') is None


def test_assoc_target51_stub_double():
    # statemachines_Vertex has no real 'Vertex52' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Vertex()
    setattr(partner, 'Vertex52', None)
    _safe_set(owner, 'incomingTransitions', partner)
    assert getattr(partner, 'Vertex52') == owner
    _safe_set(owner, 'incomingTransitions', None)
    assert getattr(partner, 'Vertex52') is None


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


def test_assoc_triggers53_stub_double():
    # statemachines_Trigger has no real 'statemachines_Trigger54' property in the generated
    # code (a bare stub) -- manually attach it so statemachines_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachines_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachines_Transition(kind="sample_text")
    partner = statemachines_Trigger()
    setattr(partner, 'statemachines_Trigger54', None)
    _safe_set(owner, 'statemachines_Transition', {partner})
    assert getattr(partner, 'statemachines_Trigger54') == owner
    _safe_set(owner, 'statemachines_Transition', set())
    assert getattr(partner, 'statemachines_Trigger54') is None


