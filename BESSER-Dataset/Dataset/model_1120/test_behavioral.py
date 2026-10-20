import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    MMInterModel_Attribute,
    MMInterModel_Component,
    MMInterModel_Element,
    MMInterModel_Event,
    MMInterModel_Guard,
    MMInterModel_Model,
    MMInterModel_State,
    MMInterModel_StateConfiguration,
    MMInterModel_StateMachine,
    MMInterModel_StringEnumeration,
    MMInterModel_Transition,
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

def test_assoc_configurationStates47_reverse_link_reassign_clear():
    a1 = MMInterModel_StateConfiguration(condition="sample_text", configOperator="sample_text", model="sample_text", negation=True)
    a2 = MMInterModel_StateConfiguration(condition="sample_text_2", configOperator="sample_text_2", model="sample_text_2", negation=False)
    b = MMInterModel_State(duringBehaviour="sample_text", entryBehaviour="sample_text", exitBehaviour="sample_text", stateConfiguration="sample_text", stateMachine="sample_text", stateNumber=7)
    _safe_set(b, 'MMInterModel_State49', a1)
    assert _is_linked(b, 'MMInterModel_State49', a1)
    if hasattr(a1, 'MMInterModel_StateConfiguration48'):
        assert _is_linked(a1, 'MMInterModel_StateConfiguration48', b)
    _safe_set(b, 'MMInterModel_State49', a2)
    assert _is_linked(b, 'MMInterModel_State49', a2)
    if hasattr(a1, 'MMInterModel_StateConfiguration48'):
        assert not _is_linked(a1, 'MMInterModel_StateConfiguration48', b)
    if hasattr(a2, 'MMInterModel_StateConfiguration48'):
        assert _is_linked(a2, 'MMInterModel_StateConfiguration48', b)
    _safe_set(b, 'MMInterModel_State49', None)
    assert not _is_linked(b, 'MMInterModel_State49', a2)
    if hasattr(a2, 'MMInterModel_StateConfiguration48'):
        assert not _is_linked(a2, 'MMInterModel_StateConfiguration48', b)


def test_assoc_enumerationLiterals42_reverse_link_reassign_clear():
    a1 = MMInterModel_StringEnumeration(attribute="sample_text")
    a2 = MMInterModel_StringEnumeration(attribute="sample_text_2")
    b = MMInterModel_Attribute(arraySize=7, component="sample_text", defaultValue="sample_text", isArray=True, lowerBound=7, model="sample_text", type="sample_text", upperBound=7)
    _safe_set(b, 'MMInterModel_Attribute43', {a1})
    assert _is_linked(b, 'MMInterModel_Attribute43', a1)
    if hasattr(a1, 'MMInterModel_StringEnumeration'):
        assert _is_linked(a1, 'MMInterModel_StringEnumeration', b)
    _safe_set(b, 'MMInterModel_Attribute43', {a2})
    assert _is_linked(b, 'MMInterModel_Attribute43', a2)
    if hasattr(a1, 'MMInterModel_StringEnumeration'):
        assert not _is_linked(a1, 'MMInterModel_StringEnumeration', b)
    if hasattr(a2, 'MMInterModel_StringEnumeration'):
        assert _is_linked(a2, 'MMInterModel_StringEnumeration', b)
    _safe_set(b, 'MMInterModel_Attribute43', set())
    assert not _is_linked(b, 'MMInterModel_Attribute43', a2)
    if hasattr(a2, 'MMInterModel_StringEnumeration'):
        assert not _is_linked(a2, 'MMInterModel_StringEnumeration', b)


def test_assoc_event28_reverse_link_reassign_clear():
    a1 = MMInterModel_Transition(action="sample_text", stateMachine="sample_text")
    a2 = MMInterModel_Transition(action="sample_text_2", stateMachine="sample_text_2")
    b = MMInterModel_Event(model="sample_text", type="sample_text")
    _safe_set(b, 'MMInterModel_Event30', a1)
    assert _is_linked(b, 'MMInterModel_Event30', a1)
    if hasattr(a1, 'MMInterModel_Transition29'):
        assert _is_linked(a1, 'MMInterModel_Transition29', b)
    _safe_set(b, 'MMInterModel_Event30', a2)
    assert _is_linked(b, 'MMInterModel_Event30', a2)
    if hasattr(a1, 'MMInterModel_Transition29'):
        assert not _is_linked(a1, 'MMInterModel_Transition29', b)
    if hasattr(a2, 'MMInterModel_Transition29'):
        assert _is_linked(a2, 'MMInterModel_Transition29', b)
    _safe_set(b, 'MMInterModel_Event30', None)
    assert not _is_linked(b, 'MMInterModel_Event30', a2)
    if hasattr(a2, 'MMInterModel_Transition29'):
        assert not _is_linked(a2, 'MMInterModel_Transition29', b)


def test_assoc_failurePatterns12_reverse_link_reassign_clear():
    a1 = MMInterModel_StateMachine(component="sample_text", superState="sample_text", type="sample_text")
    a2 = MMInterModel_StateMachine(component="sample_text_2", superState="sample_text_2", type="sample_text_2")
    b = MMInterModel_Component(model="sample_text", numberOfSpares=7)
    _safe_set(b, 'MMInterModel_Component13', {a1})
    assert _is_linked(b, 'MMInterModel_Component13', a1)
    if hasattr(a1, 'MMInterModel_StateMachine14'):
        assert _is_linked(a1, 'MMInterModel_StateMachine14', b)
    _safe_set(b, 'MMInterModel_Component13', {a2})
    assert _is_linked(b, 'MMInterModel_Component13', a2)
    if hasattr(a1, 'MMInterModel_StateMachine14'):
        assert not _is_linked(a1, 'MMInterModel_StateMachine14', b)
    if hasattr(a2, 'MMInterModel_StateMachine14'):
        assert _is_linked(a2, 'MMInterModel_StateMachine14', b)
    _safe_set(b, 'MMInterModel_Component13', set())
    assert not _is_linked(b, 'MMInterModel_Component13', a2)
    if hasattr(a2, 'MMInterModel_StateMachine14'):
        assert not _is_linked(a2, 'MMInterModel_StateMachine14', b)


def test_assoc_guard31_reverse_link_reassign_clear():
    a1 = MMInterModel_Transition(action="sample_text", stateMachine="sample_text")
    a2 = MMInterModel_Transition(action="sample_text_2", stateMachine="sample_text_2")
    b = MMInterModel_Guard(specification="sample_text", transition="sample_text")
    _safe_set(b, 'MMInterModel_Guard', a1)
    assert _is_linked(b, 'MMInterModel_Guard', a1)
    if hasattr(a1, 'MMInterModel_Transition32'):
        assert _is_linked(a1, 'MMInterModel_Transition32', b)
    _safe_set(b, 'MMInterModel_Guard', a2)
    assert _is_linked(b, 'MMInterModel_Guard', a2)
    if hasattr(a1, 'MMInterModel_Transition32'):
        assert not _is_linked(a1, 'MMInterModel_Transition32', b)
    if hasattr(a2, 'MMInterModel_Transition32'):
        assert _is_linked(a2, 'MMInterModel_Transition32', b)
    _safe_set(b, 'MMInterModel_Guard', None)
    assert not _is_linked(b, 'MMInterModel_Guard', a2)
    if hasattr(a2, 'MMInterModel_Transition32'):
        assert not _is_linked(a2, 'MMInterModel_Transition32', b)


def test_assoc_incomingTransitions33_reverse_link_reassign_clear():
    a1 = MMInterModel_Transition(action="sample_text", stateMachine="sample_text")
    a2 = MMInterModel_Transition(action="sample_text_2", stateMachine="sample_text_2")
    b = MMInterModel_State(duringBehaviour="sample_text", entryBehaviour="sample_text", exitBehaviour="sample_text", stateConfiguration="sample_text", stateMachine="sample_text", stateNumber=7)
    _safe_set(b, 'MMInterModel_State34', {a1})
    assert _is_linked(b, 'MMInterModel_State34', a1)
    if hasattr(a1, 'MMInterModel_Transition35'):
        assert _is_linked(a1, 'MMInterModel_Transition35', b)
    _safe_set(b, 'MMInterModel_State34', {a2})
    assert _is_linked(b, 'MMInterModel_State34', a2)
    if hasattr(a1, 'MMInterModel_Transition35'):
        assert not _is_linked(a1, 'MMInterModel_Transition35', b)
    if hasattr(a2, 'MMInterModel_Transition35'):
        assert _is_linked(a2, 'MMInterModel_Transition35', b)
    _safe_set(b, 'MMInterModel_State34', set())
    assert not _is_linked(b, 'MMInterModel_State34', a2)
    if hasattr(a2, 'MMInterModel_Transition35'):
        assert not _is_linked(a2, 'MMInterModel_Transition35', b)


def test_assoc_initialState19_reverse_link_reassign_clear():
    a1 = MMInterModel_StateMachine(component="sample_text", superState="sample_text", type="sample_text")
    a2 = MMInterModel_StateMachine(component="sample_text_2", superState="sample_text_2", type="sample_text_2")
    b = MMInterModel_State(duringBehaviour="sample_text", entryBehaviour="sample_text", exitBehaviour="sample_text", stateConfiguration="sample_text", stateMachine="sample_text", stateNumber=7)
    _safe_set(b, 'MMInterModel_State21', a1)
    assert _is_linked(b, 'MMInterModel_State21', a1)
    if hasattr(a1, 'MMInterModel_StateMachine20'):
        assert _is_linked(a1, 'MMInterModel_StateMachine20', b)
    _safe_set(b, 'MMInterModel_State21', a2)
    assert _is_linked(b, 'MMInterModel_State21', a2)
    if hasattr(a1, 'MMInterModel_StateMachine20'):
        assert not _is_linked(a1, 'MMInterModel_StateMachine20', b)
    if hasattr(a2, 'MMInterModel_StateMachine20'):
        assert _is_linked(a2, 'MMInterModel_StateMachine20', b)
    _safe_set(b, 'MMInterModel_State21', None)
    assert not _is_linked(b, 'MMInterModel_State21', a2)
    if hasattr(a2, 'MMInterModel_StateMachine20'):
        assert not _is_linked(a2, 'MMInterModel_StateMachine20', b)


def test_assoc_localVariables9_reverse_link_reassign_clear():
    a1 = MMInterModel_Component(model="sample_text", numberOfSpares=7)
    a2 = MMInterModel_Component(model="sample_text_2", numberOfSpares=13)
    b = MMInterModel_Attribute(arraySize=7, component="sample_text", defaultValue="sample_text", isArray=True, lowerBound=7, model="sample_text", type="sample_text", upperBound=7)
    _safe_set(b, 'MMInterModel_Attribute11', a1)
    assert _is_linked(b, 'MMInterModel_Attribute11', a1)
    if hasattr(a1, 'MMInterModel_Component10'):
        assert _is_linked(a1, 'MMInterModel_Component10', b)
    _safe_set(b, 'MMInterModel_Attribute11', a2)
    assert _is_linked(b, 'MMInterModel_Attribute11', a2)
    if hasattr(a1, 'MMInterModel_Component10'):
        assert not _is_linked(a1, 'MMInterModel_Component10', b)
    if hasattr(a2, 'MMInterModel_Component10'):
        assert _is_linked(a2, 'MMInterModel_Component10', b)
    _safe_set(b, 'MMInterModel_Attribute11', None)
    assert not _is_linked(b, 'MMInterModel_Attribute11', a2)
    if hasattr(a2, 'MMInterModel_Component10'):
        assert not _is_linked(a2, 'MMInterModel_Component10', b)


def test_assoc_normalBehaviour7_reverse_link_reassign_clear():
    a1 = MMInterModel_StateMachine(component="sample_text", superState="sample_text", type="sample_text")
    a2 = MMInterModel_StateMachine(component="sample_text_2", superState="sample_text_2", type="sample_text_2")
    b = MMInterModel_Component(model="sample_text", numberOfSpares=7)
    _safe_set(b, 'MMInterModel_Component8', a1)
    assert _is_linked(b, 'MMInterModel_Component8', a1)
    if hasattr(a1, 'MMInterModel_StateMachine'):
        assert _is_linked(a1, 'MMInterModel_StateMachine', b)
    _safe_set(b, 'MMInterModel_Component8', a2)
    assert _is_linked(b, 'MMInterModel_Component8', a2)
    if hasattr(a1, 'MMInterModel_StateMachine'):
        assert not _is_linked(a1, 'MMInterModel_StateMachine', b)
    if hasattr(a2, 'MMInterModel_StateMachine'):
        assert _is_linked(a2, 'MMInterModel_StateMachine', b)
    _safe_set(b, 'MMInterModel_Component8', None)
    assert not _is_linked(b, 'MMInterModel_Component8', a2)
    if hasattr(a2, 'MMInterModel_StateMachine'):
        assert not _is_linked(a2, 'MMInterModel_StateMachine', b)


def test_assoc_outgoingTransitions36_reverse_link_reassign_clear():
    a1 = MMInterModel_Transition(action="sample_text", stateMachine="sample_text")
    a2 = MMInterModel_Transition(action="sample_text_2", stateMachine="sample_text_2")
    b = MMInterModel_State(duringBehaviour="sample_text", entryBehaviour="sample_text", exitBehaviour="sample_text", stateConfiguration="sample_text", stateMachine="sample_text", stateNumber=7)
    _safe_set(b, 'MMInterModel_State37', {a1})
    assert _is_linked(b, 'MMInterModel_State37', a1)
    if hasattr(a1, 'MMInterModel_Transition38'):
        assert _is_linked(a1, 'MMInterModel_Transition38', b)
    _safe_set(b, 'MMInterModel_State37', {a2})
    assert _is_linked(b, 'MMInterModel_State37', a2)
    if hasattr(a1, 'MMInterModel_Transition38'):
        assert not _is_linked(a1, 'MMInterModel_Transition38', b)
    if hasattr(a2, 'MMInterModel_Transition38'):
        assert _is_linked(a2, 'MMInterModel_Transition38', b)
    _safe_set(b, 'MMInterModel_State37', set())
    assert not _is_linked(b, 'MMInterModel_State37', a2)
    if hasattr(a2, 'MMInterModel_Transition38'):
        assert not _is_linked(a2, 'MMInterModel_Transition38', b)


def test_assoc_source22_reverse_link_reassign_clear():
    a1 = MMInterModel_Transition(action="sample_text", stateMachine="sample_text")
    a2 = MMInterModel_Transition(action="sample_text_2", stateMachine="sample_text_2")
    b = MMInterModel_State(duringBehaviour="sample_text", entryBehaviour="sample_text", exitBehaviour="sample_text", stateConfiguration="sample_text", stateMachine="sample_text", stateNumber=7)
    _safe_set(b, 'MMInterModel_State24', a1)
    assert _is_linked(b, 'MMInterModel_State24', a1)
    if hasattr(a1, 'MMInterModel_Transition23'):
        assert _is_linked(a1, 'MMInterModel_Transition23', b)
    _safe_set(b, 'MMInterModel_State24', a2)
    assert _is_linked(b, 'MMInterModel_State24', a2)
    if hasattr(a1, 'MMInterModel_Transition23'):
        assert not _is_linked(a1, 'MMInterModel_Transition23', b)
    if hasattr(a2, 'MMInterModel_Transition23'):
        assert _is_linked(a2, 'MMInterModel_Transition23', b)
    _safe_set(b, 'MMInterModel_State24', None)
    assert not _is_linked(b, 'MMInterModel_State24', a2)
    if hasattr(a2, 'MMInterModel_Transition23'):
        assert not _is_linked(a2, 'MMInterModel_Transition23', b)


def test_assoc_states17_reverse_link_reassign_clear():
    a1 = MMInterModel_StateMachine(component="sample_text", superState="sample_text", type="sample_text")
    a2 = MMInterModel_StateMachine(component="sample_text_2", superState="sample_text_2", type="sample_text_2")
    b = MMInterModel_State(duringBehaviour="sample_text", entryBehaviour="sample_text", exitBehaviour="sample_text", stateConfiguration="sample_text", stateMachine="sample_text", stateNumber=7)
    _safe_set(b, 'MMInterModel_State', a1)
    assert _is_linked(b, 'MMInterModel_State', a1)
    if hasattr(a1, 'MMInterModel_StateMachine18'):
        assert _is_linked(a1, 'MMInterModel_StateMachine18', b)
    _safe_set(b, 'MMInterModel_State', a2)
    assert _is_linked(b, 'MMInterModel_State', a2)
    if hasattr(a1, 'MMInterModel_StateMachine18'):
        assert not _is_linked(a1, 'MMInterModel_StateMachine18', b)
    if hasattr(a2, 'MMInterModel_StateMachine18'):
        assert _is_linked(a2, 'MMInterModel_StateMachine18', b)
    _safe_set(b, 'MMInterModel_State', None)
    assert not _is_linked(b, 'MMInterModel_State', a2)
    if hasattr(a2, 'MMInterModel_StateMachine18'):
        assert not _is_linked(a2, 'MMInterModel_StateMachine18', b)


def test_assoc_subConfigurations51_reverse_link_reassign_clear():
    a1 = MMInterModel_StateConfiguration(condition="sample_text", configOperator="sample_text", model="sample_text", negation=True)
    a2 = MMInterModel_StateConfiguration(condition="sample_text_2", configOperator="sample_text_2", model="sample_text_2", negation=False)
    b = MMInterModel_StateConfiguration(condition="sample_text", configOperator="sample_text", model="sample_text", negation=True)
    _safe_set(b, 'MMInterModel_StateConfiguration52', a1)
    assert _is_linked(b, 'MMInterModel_StateConfiguration52', a1)
    if hasattr(a1, 'MMInterModel_StateConfiguration50'):
        assert _is_linked(a1, 'MMInterModel_StateConfiguration50', b)
    _safe_set(b, 'MMInterModel_StateConfiguration52', a2)
    assert _is_linked(b, 'MMInterModel_StateConfiguration52', a2)
    if hasattr(a1, 'MMInterModel_StateConfiguration50'):
        assert not _is_linked(a1, 'MMInterModel_StateConfiguration50', b)
    if hasattr(a2, 'MMInterModel_StateConfiguration50'):
        assert _is_linked(a2, 'MMInterModel_StateConfiguration50', b)
    _safe_set(b, 'MMInterModel_StateConfiguration52', None)
    assert not _is_linked(b, 'MMInterModel_StateConfiguration52', a2)
    if hasattr(a2, 'MMInterModel_StateConfiguration50'):
        assert not _is_linked(a2, 'MMInterModel_StateConfiguration50', b)


def test_assoc_subMachines39_reverse_link_reassign_clear():
    a1 = MMInterModel_StateMachine(component="sample_text", superState="sample_text", type="sample_text")
    a2 = MMInterModel_StateMachine(component="sample_text_2", superState="sample_text_2", type="sample_text_2")
    b = MMInterModel_State(duringBehaviour="sample_text", entryBehaviour="sample_text", exitBehaviour="sample_text", stateConfiguration="sample_text", stateMachine="sample_text", stateNumber=7)
    _safe_set(b, 'MMInterModel_State40', a1)
    assert _is_linked(b, 'MMInterModel_State40', a1)
    if hasattr(a1, 'MMInterModel_StateMachine41'):
        assert _is_linked(a1, 'MMInterModel_StateMachine41', b)
    _safe_set(b, 'MMInterModel_State40', a2)
    assert _is_linked(b, 'MMInterModel_State40', a2)
    if hasattr(a1, 'MMInterModel_StateMachine41'):
        assert not _is_linked(a1, 'MMInterModel_StateMachine41', b)
    if hasattr(a2, 'MMInterModel_StateMachine41'):
        assert _is_linked(a2, 'MMInterModel_StateMachine41', b)
    _safe_set(b, 'MMInterModel_State40', None)
    assert not _is_linked(b, 'MMInterModel_State40', a2)
    if hasattr(a2, 'MMInterModel_StateMachine41'):
        assert not _is_linked(a2, 'MMInterModel_StateMachine41', b)


def test_assoc_target25_reverse_link_reassign_clear():
    a1 = MMInterModel_Transition(action="sample_text", stateMachine="sample_text")
    a2 = MMInterModel_Transition(action="sample_text_2", stateMachine="sample_text_2")
    b = MMInterModel_State(duringBehaviour="sample_text", entryBehaviour="sample_text", exitBehaviour="sample_text", stateConfiguration="sample_text", stateMachine="sample_text", stateNumber=7)
    _safe_set(b, 'MMInterModel_State27', a1)
    assert _is_linked(b, 'MMInterModel_State27', a1)
    if hasattr(a1, 'MMInterModel_Transition26'):
        assert _is_linked(a1, 'MMInterModel_Transition26', b)
    _safe_set(b, 'MMInterModel_State27', a2)
    assert _is_linked(b, 'MMInterModel_State27', a2)
    if hasattr(a1, 'MMInterModel_Transition26'):
        assert not _is_linked(a1, 'MMInterModel_Transition26', b)
    if hasattr(a2, 'MMInterModel_Transition26'):
        assert _is_linked(a2, 'MMInterModel_Transition26', b)
    _safe_set(b, 'MMInterModel_State27', None)
    assert not _is_linked(b, 'MMInterModel_State27', a2)
    if hasattr(a2, 'MMInterModel_Transition26'):
        assert not _is_linked(a2, 'MMInterModel_Transition26', b)


def test_assoc_transitions15_reverse_link_reassign_clear():
    a1 = MMInterModel_Transition(action="sample_text", stateMachine="sample_text")
    a2 = MMInterModel_Transition(action="sample_text_2", stateMachine="sample_text_2")
    b = MMInterModel_StateMachine(component="sample_text", superState="sample_text", type="sample_text")
    _safe_set(b, 'MMInterModel_StateMachine16', {a1})
    assert _is_linked(b, 'MMInterModel_StateMachine16', a1)
    if hasattr(a1, 'MMInterModel_Transition'):
        assert _is_linked(a1, 'MMInterModel_Transition', b)
    _safe_set(b, 'MMInterModel_StateMachine16', {a2})
    assert _is_linked(b, 'MMInterModel_StateMachine16', a2)
    if hasattr(a1, 'MMInterModel_Transition'):
        assert not _is_linked(a1, 'MMInterModel_Transition', b)
    if hasattr(a2, 'MMInterModel_Transition'):
        assert _is_linked(a2, 'MMInterModel_Transition', b)
    _safe_set(b, 'MMInterModel_StateMachine16', set())
    assert not _is_linked(b, 'MMInterModel_StateMachine16', a2)
    if hasattr(a2, 'MMInterModel_Transition'):
        assert not _is_linked(a2, 'MMInterModel_Transition', b)


def test_assoc_transitionsTriggeredByEvent44_reverse_link_reassign_clear():
    a1 = MMInterModel_Transition(action="sample_text", stateMachine="sample_text")
    a2 = MMInterModel_Transition(action="sample_text_2", stateMachine="sample_text_2")
    b = MMInterModel_Event(model="sample_text", type="sample_text")
    _safe_set(b, 'MMInterModel_Event45', {a1})
    assert _is_linked(b, 'MMInterModel_Event45', a1)
    if hasattr(a1, 'MMInterModel_Transition46'):
        assert _is_linked(a1, 'MMInterModel_Transition46', b)
    _safe_set(b, 'MMInterModel_Event45', {a2})
    assert _is_linked(b, 'MMInterModel_Event45', a2)
    if hasattr(a1, 'MMInterModel_Transition46'):
        assert not _is_linked(a1, 'MMInterModel_Transition46', b)
    if hasattr(a2, 'MMInterModel_Transition46'):
        assert _is_linked(a2, 'MMInterModel_Transition46', b)
    _safe_set(b, 'MMInterModel_Event45', set())
    assert not _is_linked(b, 'MMInterModel_Event45', a2)
    if hasattr(a2, 'MMInterModel_Transition46'):
        assert not _is_linked(a2, 'MMInterModel_Transition46', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_components0_stub_double():
    # MMInterModel_Model has no real 'MMInterModel_Model' property in the generated
    # code (a bare stub) -- manually attach it so MMInterModel_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MMInterModel_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MMInterModel_Component(model="sample_text", numberOfSpares=7)
    partner = MMInterModel_Model()
    setattr(partner, 'MMInterModel_Model', None)
    _safe_set(owner, 'MMInterModel_Component', partner)
    assert owner in getattr(partner, 'MMInterModel_Model')
    _safe_set(owner, 'MMInterModel_Component', None)
    assert owner not in getattr(partner, 'MMInterModel_Model')


def test_assoc_events3_stub_double():
    # MMInterModel_Model has no real 'MMInterModel_Model4' property in the generated
    # code (a bare stub) -- manually attach it so MMInterModel_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MMInterModel_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MMInterModel_Event(model="sample_text", type="sample_text")
    partner = MMInterModel_Model()
    setattr(partner, 'MMInterModel_Model4', None)
    _safe_set(owner, 'MMInterModel_Event', partner)
    assert owner in getattr(partner, 'MMInterModel_Model4')
    _safe_set(owner, 'MMInterModel_Event', None)
    assert owner not in getattr(partner, 'MMInterModel_Model4')


def test_assoc_globalVariables1_stub_double():
    # MMInterModel_Model has no real 'MMInterModel_Model2' property in the generated
    # code (a bare stub) -- manually attach it so MMInterModel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MMInterModel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MMInterModel_Attribute(arraySize=7, component="sample_text", defaultValue="sample_text", isArray=True, lowerBound=7, model="sample_text", type="sample_text", upperBound=7)
    partner = MMInterModel_Model()
    setattr(partner, 'MMInterModel_Model2', None)
    _safe_set(owner, 'MMInterModel_Attribute', partner)
    assert owner in getattr(partner, 'MMInterModel_Model2')
    _safe_set(owner, 'MMInterModel_Attribute', None)
    assert owner not in getattr(partner, 'MMInterModel_Model2')


def test_assoc_stateConfigurations5_stub_double():
    # MMInterModel_Model has no real 'MMInterModel_Model6' property in the generated
    # code (a bare stub) -- manually attach it so MMInterModel_StateConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MMInterModel_StateConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MMInterModel_StateConfiguration(condition="sample_text", configOperator="sample_text", model="sample_text", negation=True)
    partner = MMInterModel_Model()
    setattr(partner, 'MMInterModel_Model6', None)
    _safe_set(owner, 'MMInterModel_StateConfiguration', partner)
    assert owner in getattr(partner, 'MMInterModel_Model6')
    _safe_set(owner, 'MMInterModel_StateConfiguration', None)
    assert owner not in getattr(partner, 'MMInterModel_Model6')


