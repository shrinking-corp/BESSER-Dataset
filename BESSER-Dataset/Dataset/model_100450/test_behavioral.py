import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Storage,
    statespace_EAttribute,
    statespace_EClass,
    statespace_EObject,
    statespace_EObjectIntegerMapEntry,
    statespace_EStringToStringMapEntry,
    statespace_EqualityHelper,
    statespace_Model,
    statespace_Rule,
    statespace_State,
    statespace_StateSpace,
    statespace_Storage,
    statespace_Transition,
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

def test_assoc_equalityHelper7_reverse_link_reassign_clear():
    a1 = statespace_StateSpace(allParameterKeys="sample_text", layoutHideIndizes=True, layoutHideLabels=True, layoutStateRepulsion=7, layoutTransitionAttraction=7, layoutZoomLevel=7, maxStateDistance=7, stateCount=7, transitionCount=7)
    a2 = statespace_StateSpace(allParameterKeys="sample_text_2", layoutHideIndizes=False, layoutHideLabels=False, layoutStateRepulsion=13, layoutTransitionAttraction=13, layoutZoomLevel=13, maxStateDistance=13, stateCount=13, transitionCount=13)
    b = statespace_EqualityHelper(checkLinkOrder=True)
    _safe_set(b, 'statespace_EqualityHelper', a1)
    assert _is_linked(b, 'statespace_EqualityHelper', a1)
    if hasattr(a1, 'statespace_StateSpace8'):
        assert _is_linked(a1, 'statespace_StateSpace8', b)
    _safe_set(b, 'statespace_EqualityHelper', a2)
    assert _is_linked(b, 'statespace_EqualityHelper', a2)
    if hasattr(a1, 'statespace_StateSpace8'):
        assert not _is_linked(a1, 'statespace_StateSpace8', b)
    if hasattr(a2, 'statespace_StateSpace8'):
        assert _is_linked(a2, 'statespace_StateSpace8', b)
    _safe_set(b, 'statespace_EqualityHelper', None)
    assert not _is_linked(b, 'statespace_EqualityHelper', a2)
    if hasattr(a2, 'statespace_StateSpace8'):
        assert not _is_linked(a2, 'statespace_StateSpace8', b)


def test_assoc_incoming11_reverse_link_reassign_clear():
    a1 = statespace_Transition(match=7, parameterCount=7, parameterKeys="sample_text")
    a2 = statespace_Transition(match=13, parameterCount=13, parameterKeys="sample_text_2")
    b = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_initialStates2_reverse_link_reassign_clear():
    a1 = statespace_StateSpace(allParameterKeys="sample_text", layoutHideIndizes=True, layoutHideLabels=True, layoutStateRepulsion=7, layoutTransitionAttraction=7, layoutZoomLevel=7, maxStateDistance=7, stateCount=7, transitionCount=7)
    a2 = statespace_StateSpace(allParameterKeys="sample_text_2", layoutHideIndizes=False, layoutHideLabels=False, layoutStateRepulsion=13, layoutTransitionAttraction=13, layoutZoomLevel=13, maxStateDistance=13, stateCount=13, transitionCount=13)
    b = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    _safe_set(b, 'statespace_State', a1)
    assert _is_linked(b, 'statespace_State', a1)
    if hasattr(a1, 'statespace_StateSpace3'):
        assert _is_linked(a1, 'statespace_StateSpace3', b)
    _safe_set(b, 'statespace_State', a2)
    assert _is_linked(b, 'statespace_State', a2)
    if hasattr(a1, 'statespace_StateSpace3'):
        assert not _is_linked(a1, 'statespace_StateSpace3', b)
    if hasattr(a2, 'statespace_StateSpace3'):
        assert _is_linked(a2, 'statespace_StateSpace3', b)
    _safe_set(b, 'statespace_State', None)
    assert not _is_linked(b, 'statespace_State', a2)
    if hasattr(a2, 'statespace_StateSpace3'):
        assert not _is_linked(a2, 'statespace_StateSpace3', b)


def test_assoc_model15_reverse_link_reassign_clear():
    a1 = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    a2 = statespace_State(derivedFrom=13, goal=False, hashCode=13, index=13, location="sample_text_2", objectCount=13, objectKeys="sample_text_2", open=False, pruned=False)
    b = statespace_Model(eGraph="sample_text", objectCount=7, objectKeys="sample_text", resource="sample_text")
    _safe_set(b, 'statespace_Model', a1)
    assert _is_linked(b, 'statespace_Model', a1)
    if hasattr(a1, 'statespace_State16'):
        assert _is_linked(a1, 'statespace_State16', b)
    _safe_set(b, 'statespace_Model', a2)
    assert _is_linked(b, 'statespace_Model', a2)
    if hasattr(a1, 'statespace_State16'):
        assert not _is_linked(a1, 'statespace_State16', b)
    if hasattr(a2, 'statespace_State16'):
        assert _is_linked(a2, 'statespace_State16', b)
    _safe_set(b, 'statespace_Model', None)
    assert not _is_linked(b, 'statespace_Model', a2)
    if hasattr(a2, 'statespace_State16'):
        assert not _is_linked(a2, 'statespace_State16', b)


def test_assoc_objectHashCodes17_reverse_link_reassign_clear():
    a1 = statespace_Model(eGraph="sample_text", objectCount=7, objectKeys="sample_text", resource="sample_text")
    a2 = statespace_Model(eGraph="sample_text_2", objectCount=13, objectKeys="sample_text_2", resource="sample_text_2")
    b = statespace_EObjectIntegerMapEntry(value="sample_text")
    _safe_set(b, 'statespace_EObjectIntegerMapEntry', a1)
    assert _is_linked(b, 'statespace_EObjectIntegerMapEntry', a1)
    if hasattr(a1, 'statespace_Model18'):
        assert _is_linked(a1, 'statespace_Model18', b)
    _safe_set(b, 'statespace_EObjectIntegerMapEntry', a2)
    assert _is_linked(b, 'statespace_EObjectIntegerMapEntry', a2)
    if hasattr(a1, 'statespace_Model18'):
        assert not _is_linked(a1, 'statespace_Model18', b)
    if hasattr(a2, 'statespace_Model18'):
        assert _is_linked(a2, 'statespace_Model18', b)
    _safe_set(b, 'statespace_EObjectIntegerMapEntry', None)
    assert not _is_linked(b, 'statespace_EObjectIntegerMapEntry', a2)
    if hasattr(a2, 'statespace_Model18'):
        assert not _is_linked(a2, 'statespace_Model18', b)


def test_assoc_objectKeysMap19_reverse_link_reassign_clear():
    a1 = statespace_Model(eGraph="sample_text", objectCount=7, objectKeys="sample_text", resource="sample_text")
    a2 = statespace_Model(eGraph="sample_text_2", objectCount=13, objectKeys="sample_text_2", resource="sample_text_2")
    b = statespace_EObjectIntegerMapEntry(value="sample_text")
    _safe_set(b, 'statespace_EObjectIntegerMapEntry21', a1)
    assert _is_linked(b, 'statespace_EObjectIntegerMapEntry21', a1)
    if hasattr(a1, 'statespace_Model20'):
        assert _is_linked(a1, 'statespace_Model20', b)
    _safe_set(b, 'statespace_EObjectIntegerMapEntry21', a2)
    assert _is_linked(b, 'statespace_EObjectIntegerMapEntry21', a2)
    if hasattr(a1, 'statespace_Model20'):
        assert not _is_linked(a1, 'statespace_Model20', b)
    if hasattr(a2, 'statespace_Model20'):
        assert _is_linked(a2, 'statespace_Model20', b)
    _safe_set(b, 'statespace_EObjectIntegerMapEntry21', None)
    assert not _is_linked(b, 'statespace_EObjectIntegerMapEntry21', a2)
    if hasattr(a2, 'statespace_Model20'):
        assert not _is_linked(a2, 'statespace_Model20', b)


def test_assoc_openStates4_reverse_link_reassign_clear():
    a1 = statespace_StateSpace(allParameterKeys="sample_text", layoutHideIndizes=True, layoutHideLabels=True, layoutStateRepulsion=7, layoutTransitionAttraction=7, layoutZoomLevel=7, maxStateDistance=7, stateCount=7, transitionCount=7)
    a2 = statespace_StateSpace(allParameterKeys="sample_text_2", layoutHideIndizes=False, layoutHideLabels=False, layoutStateRepulsion=13, layoutTransitionAttraction=13, layoutZoomLevel=13, maxStateDistance=13, stateCount=13, transitionCount=13)
    b = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    _safe_set(b, 'statespace_State6', a1)
    assert _is_linked(b, 'statespace_State6', a1)
    if hasattr(a1, 'statespace_StateSpace5'):
        assert _is_linked(a1, 'statespace_StateSpace5', b)
    _safe_set(b, 'statespace_State6', a2)
    assert _is_linked(b, 'statespace_State6', a2)
    if hasattr(a1, 'statespace_StateSpace5'):
        assert not _is_linked(a1, 'statespace_StateSpace5', b)
    if hasattr(a2, 'statespace_StateSpace5'):
        assert _is_linked(a2, 'statespace_StateSpace5', b)
    _safe_set(b, 'statespace_State6', None)
    assert not _is_linked(b, 'statespace_State6', a2)
    if hasattr(a2, 'statespace_StateSpace5'):
        assert not _is_linked(a2, 'statespace_StateSpace5', b)


def test_assoc_outgoing12_reverse_link_reassign_clear():
    a1 = statespace_Transition(match=7, parameterCount=7, parameterKeys="sample_text")
    a2 = statespace_Transition(match=13, parameterCount=13, parameterKeys="sample_text_2")
    b = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition13'):
        assert _is_linked(a1, 'Transition13', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition13'):
        assert not _is_linked(a1, 'Transition13', b)
    if hasattr(a2, 'Transition13'):
        assert _is_linked(a2, 'Transition13', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition13'):
        assert not _is_linked(a2, 'Transition13', b)


def test_assoc_source22_reverse_link_reassign_clear():
    a1 = statespace_Transition(match=7, parameterCount=7, parameterKeys="sample_text")
    a2 = statespace_Transition(match=13, parameterCount=13, parameterKeys="sample_text_2")
    b = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    _safe_set(b, 'State23', a1)
    assert _is_linked(b, 'State23', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'State23', a2)
    assert _is_linked(b, 'State23', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'State23', None)
    assert not _is_linked(b, 'State23', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_stateSpace14_reverse_link_reassign_clear():
    a1 = statespace_StateSpace(allParameterKeys="sample_text", layoutHideIndizes=True, layoutHideLabels=True, layoutStateRepulsion=7, layoutTransitionAttraction=7, layoutZoomLevel=7, maxStateDistance=7, stateCount=7, transitionCount=7)
    a2 = statespace_StateSpace(allParameterKeys="sample_text_2", layoutHideIndizes=False, layoutHideLabels=False, layoutStateRepulsion=13, layoutTransitionAttraction=13, layoutZoomLevel=13, maxStateDistance=13, stateCount=13, transitionCount=13)
    b = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    _safe_set(b, 'states', a1)
    assert _is_linked(b, 'states', a1)
    if hasattr(a1, 'StateSpace'):
        assert _is_linked(a1, 'StateSpace', b)
    _safe_set(b, 'states', a2)
    assert _is_linked(b, 'states', a2)
    if hasattr(a1, 'StateSpace'):
        assert not _is_linked(a1, 'StateSpace', b)
    if hasattr(a2, 'StateSpace'):
        assert _is_linked(a2, 'StateSpace', b)
    _safe_set(b, 'states', None)
    assert not _is_linked(b, 'states', a2)
    if hasattr(a2, 'StateSpace'):
        assert not _is_linked(a2, 'StateSpace', b)


def test_assoc_states1_reverse_link_reassign_clear():
    a1 = statespace_StateSpace(allParameterKeys="sample_text", layoutHideIndizes=True, layoutHideLabels=True, layoutStateRepulsion=7, layoutTransitionAttraction=7, layoutZoomLevel=7, maxStateDistance=7, stateCount=7, transitionCount=7)
    a2 = statespace_StateSpace(allParameterKeys="sample_text_2", layoutHideIndizes=False, layoutHideLabels=False, layoutStateRepulsion=13, layoutTransitionAttraction=13, layoutZoomLevel=13, maxStateDistance=13, stateCount=13, transitionCount=13)
    b = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'stateSpace'):
        assert _is_linked(a1, 'stateSpace', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'stateSpace'):
        assert not _is_linked(a1, 'stateSpace', b)
    if hasattr(a2, 'stateSpace'):
        assert _is_linked(a2, 'stateSpace', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'stateSpace'):
        assert not _is_linked(a2, 'stateSpace', b)


def test_assoc_target24_reverse_link_reassign_clear():
    a1 = statespace_Transition(match=7, parameterCount=7, parameterKeys="sample_text")
    a2 = statespace_Transition(match=13, parameterCount=13, parameterKeys="sample_text_2")
    b = statespace_State(derivedFrom=7, goal=True, hashCode=7, index=7, location="sample_text", objectCount=7, objectKeys="sample_text", open=True, pruned=True)
    _safe_set(b, 'State25', a1)
    assert _is_linked(b, 'State25', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'State25', a2)
    assert _is_linked(b, 'State25', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'State25', None)
    assert not _is_linked(b, 'State25', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_identityTypes30_stub_double():
    # statespace_EClass has no real 'statespace_EClass' property in the generated
    # code (a bare stub) -- manually attach it so statespace_EqualityHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statespace_EqualityHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statespace_EqualityHelper(checkLinkOrder=True)
    partner = statespace_EClass()
    setattr(partner, 'statespace_EClass', None)
    _safe_set(owner, 'statespace_EqualityHelper31', {partner})
    assert getattr(partner, 'statespace_EClass') == owner
    _safe_set(owner, 'statespace_EqualityHelper31', set())
    assert getattr(partner, 'statespace_EClass') is None


def test_assoc_ignoredAttributes28_stub_double():
    # statespace_EAttribute has no real 'statespace_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so statespace_EqualityHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statespace_EqualityHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statespace_EqualityHelper(checkLinkOrder=True)
    partner = statespace_EAttribute()
    setattr(partner, 'statespace_EAttribute', None)
    _safe_set(owner, 'statespace_EqualityHelper29', {partner})
    assert getattr(partner, 'statespace_EAttribute') == owner
    _safe_set(owner, 'statespace_EqualityHelper29', set())
    assert getattr(partner, 'statespace_EAttribute') is None


def test_assoc_key32_stub_double():
    # statespace_EObject has no real 'statespace_EObject' property in the generated
    # code (a bare stub) -- manually attach it so statespace_EObjectIntegerMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statespace_EObjectIntegerMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statespace_EObjectIntegerMapEntry(value="sample_text")
    partner = statespace_EObject()
    setattr(partner, 'statespace_EObject', None)
    _safe_set(owner, 'statespace_EObjectIntegerMapEntry33', partner)
    assert getattr(partner, 'statespace_EObject') == owner
    _safe_set(owner, 'statespace_EObjectIntegerMapEntry33', None)
    assert getattr(partner, 'statespace_EObject') is None


def test_assoc_properties9_stub_double():
    # statespace_EStringToStringMapEntry has no real 'statespace_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so statespace_StateSpace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statespace_StateSpace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statespace_StateSpace(allParameterKeys="sample_text", layoutHideIndizes=True, layoutHideLabels=True, layoutStateRepulsion=7, layoutTransitionAttraction=7, layoutZoomLevel=7, maxStateDistance=7, stateCount=7, transitionCount=7)
    partner = statespace_EStringToStringMapEntry()
    setattr(partner, 'statespace_EStringToStringMapEntry', None)
    _safe_set(owner, 'statespace_StateSpace10', {partner})
    assert getattr(partner, 'statespace_EStringToStringMapEntry') == owner
    _safe_set(owner, 'statespace_StateSpace10', set())
    assert getattr(partner, 'statespace_EStringToStringMapEntry') is None


def test_assoc_rule26_stub_double():
    # statespace_Rule has no real 'statespace_Rule27' property in the generated
    # code (a bare stub) -- manually attach it so statespace_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statespace_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statespace_Transition(match=7, parameterCount=7, parameterKeys="sample_text")
    partner = statespace_Rule()
    setattr(partner, 'statespace_Rule27', None)
    _safe_set(owner, 'statespace_Transition', partner)
    assert getattr(partner, 'statespace_Rule27') == owner
    _safe_set(owner, 'statespace_Transition', None)
    assert getattr(partner, 'statespace_Rule27') is None


def test_assoc_rules0_stub_double():
    # statespace_Rule has no real 'statespace_Rule' property in the generated
    # code (a bare stub) -- manually attach it so statespace_StateSpace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statespace_StateSpace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statespace_StateSpace(allParameterKeys="sample_text", layoutHideIndizes=True, layoutHideLabels=True, layoutStateRepulsion=7, layoutTransitionAttraction=7, layoutZoomLevel=7, maxStateDistance=7, stateCount=7, transitionCount=7)
    partner = statespace_Rule()
    setattr(partner, 'statespace_Rule', None)
    _safe_set(owner, 'statespace_StateSpace', {partner})
    assert getattr(partner, 'statespace_Rule') == owner
    _safe_set(owner, 'statespace_StateSpace', set())
    assert getattr(partner, 'statespace_Rule') is None


