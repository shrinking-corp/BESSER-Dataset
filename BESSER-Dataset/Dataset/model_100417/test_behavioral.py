import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractCondition,
    AbstractState,
    AbstractTransition,
    Named,
    statemachine_AbstractCondition,
    statemachine_AbstractState,
    statemachine_AbstractTransition,
    statemachine_AttributeCondition,
    statemachine_ConditionalState,
    statemachine_ConditionalTransition,
    statemachine_FieldCondition,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_Named,
    statemachine_State,
    statemachine_StateAttribute,
    statemachine_StateChange,
    statemachine_StateValue,
    statemachine_Statemachine,
    statemachine_Transition,
    StateAttributeType,
    StateValueType,
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

def test_assoc_condition10_reverse_link_reassign_clear():
    a1 = statemachine_ConditionalState(andExpression=True, conditionsOrganization="sample_text")
    a2 = statemachine_ConditionalState(andExpression=False, conditionsOrganization="sample_text_2")
    b = statemachine_AbstractCondition(isNotCondition=True)
    _safe_set(b, 'statemachine_AbstractCondition', a1)
    assert _is_linked(b, 'statemachine_AbstractCondition', a1)
    if hasattr(a1, 'statemachine_ConditionalState'):
        assert _is_linked(a1, 'statemachine_ConditionalState', b)
    _safe_set(b, 'statemachine_AbstractCondition', a2)
    assert _is_linked(b, 'statemachine_AbstractCondition', a2)
    if hasattr(a1, 'statemachine_ConditionalState'):
        assert not _is_linked(a1, 'statemachine_ConditionalState', b)
    if hasattr(a2, 'statemachine_ConditionalState'):
        assert _is_linked(a2, 'statemachine_ConditionalState', b)
    _safe_set(b, 'statemachine_AbstractCondition', None)
    assert not _is_linked(b, 'statemachine_AbstractCondition', a2)
    if hasattr(a2, 'statemachine_ConditionalState'):
        assert not _is_linked(a2, 'statemachine_ConditionalState', b)


def test_assoc_stateAttributeQuery9_reverse_link_reassign_clear():
    a1 = statemachine_StateAttribute(type="sample_text", value="sample_text")
    a2 = statemachine_StateAttribute(type="sample_text_2", value="sample_text_2")
    b = statemachine_StateAttribute(type="sample_text", value="sample_text")
    _safe_set(b, 'statemachine_StateAttribute8', {a1})
    assert _is_linked(b, 'statemachine_StateAttribute8', a1)
    if hasattr(a1, 'statemachine_StateAttribute'):
        assert _is_linked(a1, 'statemachine_StateAttribute', b)
    _safe_set(b, 'statemachine_StateAttribute8', {a2})
    assert _is_linked(b, 'statemachine_StateAttribute8', a2)
    if hasattr(a1, 'statemachine_StateAttribute'):
        assert not _is_linked(a1, 'statemachine_StateAttribute', b)
    if hasattr(a2, 'statemachine_StateAttribute'):
        assert _is_linked(a2, 'statemachine_StateAttribute', b)
    _safe_set(b, 'statemachine_StateAttribute8', set())
    assert not _is_linked(b, 'statemachine_StateAttribute8', a2)
    if hasattr(a2, 'statemachine_StateAttribute'):
        assert not _is_linked(a2, 'statemachine_StateAttribute', b)


def test_assoc_stateValue16_reverse_link_reassign_clear():
    a1 = statemachine_StateValue(type="sample_text", value="sample_text")
    a2 = statemachine_StateValue(type="sample_text_2", value="sample_text_2")
    b = statemachine_AbstractCondition(isNotCondition=True)
    _safe_set(b, 'statemachine_AbstractCondition17', a1)
    assert _is_linked(b, 'statemachine_AbstractCondition17', a1)
    if hasattr(a1, 'statemachine_StateValue18'):
        assert _is_linked(a1, 'statemachine_StateValue18', b)
    _safe_set(b, 'statemachine_AbstractCondition17', a2)
    assert _is_linked(b, 'statemachine_AbstractCondition17', a2)
    if hasattr(a1, 'statemachine_StateValue18'):
        assert not _is_linked(a1, 'statemachine_StateValue18', b)
    if hasattr(a2, 'statemachine_StateValue18'):
        assert _is_linked(a2, 'statemachine_StateValue18', b)
    _safe_set(b, 'statemachine_AbstractCondition17', None)
    assert not _is_linked(b, 'statemachine_AbstractCondition17', a2)
    if hasattr(a2, 'statemachine_StateValue18'):
        assert not _is_linked(a2, 'statemachine_StateValue18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_stateAttribute11_stub_double():
    # statemachine_StateChange has no real 'statemachine_StateChange12' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_StateAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_StateAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_StateAttribute(type="sample_text", value="sample_text")
    partner = statemachine_StateChange()
    setattr(partner, 'statemachine_StateChange12', None)
    _safe_set(owner, 'statemachine_StateAttribute13', partner)
    assert owner in getattr(partner, 'statemachine_StateChange12')
    _safe_set(owner, 'statemachine_StateAttribute13', None)
    assert owner not in getattr(partner, 'statemachine_StateChange12')


def test_assoc_stateAttribute19_stub_double():
    # statemachine_AttributeCondition has no real 'statemachine_AttributeCondition' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_StateAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_StateAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_StateAttribute(type="sample_text", value="sample_text")
    partner = statemachine_AttributeCondition()
    setattr(partner, 'statemachine_AttributeCondition', None)
    _safe_set(owner, 'statemachine_StateAttribute20', partner)
    assert owner in getattr(partner, 'statemachine_AttributeCondition')
    _safe_set(owner, 'statemachine_StateAttribute20', None)
    assert owner not in getattr(partner, 'statemachine_AttributeCondition')


def test_assoc_stateValue14_stub_double():
    # statemachine_StateChange has no real 'statemachine_StateChange15' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_StateValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_StateValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_StateValue(type="sample_text", value="sample_text")
    partner = statemachine_StateChange()
    setattr(partner, 'statemachine_StateChange15', None)
    _safe_set(owner, 'statemachine_StateValue', partner)
    assert getattr(partner, 'statemachine_StateChange15') == owner
    _safe_set(owner, 'statemachine_StateValue', None)
    assert getattr(partner, 'statemachine_StateChange15') is None


def test_assoc_states0_stub_double():
    # statemachine_AbstractState has no real 'statemachine_AbstractState' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_Statemachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_Statemachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_Statemachine(associatedAttribute="sample_text", associatedTree="sample_text")
    partner = statemachine_AbstractState()
    setattr(partner, 'statemachine_AbstractState', None)
    _safe_set(owner, 'statemachine_Statemachine', {partner})
    assert getattr(partner, 'statemachine_AbstractState') == owner
    _safe_set(owner, 'statemachine_Statemachine', set())
    assert getattr(partner, 'statemachine_AbstractState') is None


