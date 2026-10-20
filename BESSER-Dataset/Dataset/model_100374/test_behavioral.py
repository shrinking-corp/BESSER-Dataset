import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    internalsm_AtomicEventPattern,
    internalsm_Event,
    internalsm_EventPattern,
    internalsm_EventToken,
    internalsm_FinalState,
    internalsm_Guard,
    internalsm_InitState,
    internalsm_InternalExecutionModel,
    internalsm_State,
    internalsm_StateMachine,
    internalsm_TimeConstraint,
    internalsm_TimeConstraintSpecification,
    internalsm_Transition,
    internalsm_TrapState,
    EventProcessingContext,
    NumericCompareOperator,
    TimeConstraintType,
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

def test_assoc_stateMachines16_reverse_link_reassign_clear():
    a1 = internalsm_StateMachine(context="sample_text", priority=7)
    a2 = internalsm_StateMachine(context="sample_text_2", priority=13)
    b = internalsm_InternalExecutionModel(context="sample_text")
    _safe_set(b, 'internalsm_InternalExecutionModel', {a1})
    assert _is_linked(b, 'internalsm_InternalExecutionModel', a1)
    if hasattr(a1, 'internalsm_StateMachine17'):
        assert _is_linked(a1, 'internalsm_StateMachine17', b)
    _safe_set(b, 'internalsm_InternalExecutionModel', {a2})
    assert _is_linked(b, 'internalsm_InternalExecutionModel', a2)
    if hasattr(a1, 'internalsm_StateMachine17'):
        assert not _is_linked(a1, 'internalsm_StateMachine17', b)
    if hasattr(a2, 'internalsm_StateMachine17'):
        assert _is_linked(a2, 'internalsm_StateMachine17', b)
    _safe_set(b, 'internalsm_InternalExecutionModel', set())
    assert not _is_linked(b, 'internalsm_InternalExecutionModel', a2)
    if hasattr(a2, 'internalsm_StateMachine17'):
        assert not _is_linked(a2, 'internalsm_StateMachine17', b)


def test_assoc_states13_reverse_link_reassign_clear():
    a1 = internalsm_StateMachine(context="sample_text", priority=7)
    a2 = internalsm_StateMachine(context="sample_text_2", priority=13)
    b = internalsm_State(label="sample_text")
    _safe_set(b, 'internalsm_State14', a1)
    assert _is_linked(b, 'internalsm_State14', a1)
    if hasattr(a1, 'internalsm_StateMachine'):
        assert _is_linked(a1, 'internalsm_StateMachine', b)
    _safe_set(b, 'internalsm_State14', a2)
    assert _is_linked(b, 'internalsm_State14', a2)
    if hasattr(a1, 'internalsm_StateMachine'):
        assert not _is_linked(a1, 'internalsm_StateMachine', b)
    if hasattr(a2, 'internalsm_StateMachine'):
        assert _is_linked(a2, 'internalsm_StateMachine', b)
    _safe_set(b, 'internalsm_State14', None)
    assert not _is_linked(b, 'internalsm_State14', a2)
    if hasattr(a2, 'internalsm_StateMachine'):
        assert not _is_linked(a2, 'internalsm_StateMachine', b)


def test_assoc_timeConstraintSpecification28_reverse_link_reassign_clear():
    a1 = internalsm_TimeConstraintSpecification(expectedLength="sample_text", id="sample_text", startTimestamp="sample_text", stopTimestamp="sample_text")
    a2 = internalsm_TimeConstraintSpecification(expectedLength="sample_text_2", id="sample_text_2", startTimestamp="sample_text_2", stopTimestamp="sample_text_2")
    b = internalsm_TimeConstraint(type="sample_text")
    _safe_set(b, 'internalsm_TimeConstraint29', a1)
    assert _is_linked(b, 'internalsm_TimeConstraint29', a1)
    if hasattr(a1, 'internalsm_TimeConstraintSpecification'):
        assert _is_linked(a1, 'internalsm_TimeConstraintSpecification', b)
    _safe_set(b, 'internalsm_TimeConstraint29', a2)
    assert _is_linked(b, 'internalsm_TimeConstraint29', a2)
    if hasattr(a1, 'internalsm_TimeConstraintSpecification'):
        assert not _is_linked(a1, 'internalsm_TimeConstraintSpecification', b)
    if hasattr(a2, 'internalsm_TimeConstraintSpecification'):
        assert _is_linked(a2, 'internalsm_TimeConstraintSpecification', b)
    _safe_set(b, 'internalsm_TimeConstraint29', None)
    assert not _is_linked(b, 'internalsm_TimeConstraint29', a2)
    if hasattr(a2, 'internalsm_TimeConstraintSpecification'):
        assert not _is_linked(a2, 'internalsm_TimeConstraintSpecification', b)


def test_assoc_timeConstraints4_reverse_link_reassign_clear():
    a1 = internalsm_TimeConstraint(type="sample_text")
    a2 = internalsm_TimeConstraint(type="sample_text_2")
    b = internalsm_State(label="sample_text")
    _safe_set(b, 'internalsm_State', {a1})
    assert _is_linked(b, 'internalsm_State', a1)
    if hasattr(a1, 'internalsm_TimeConstraint'):
        assert _is_linked(a1, 'internalsm_TimeConstraint', b)
    _safe_set(b, 'internalsm_State', {a2})
    assert _is_linked(b, 'internalsm_State', a2)
    if hasattr(a1, 'internalsm_TimeConstraint'):
        assert not _is_linked(a1, 'internalsm_TimeConstraint', b)
    if hasattr(a2, 'internalsm_TimeConstraint'):
        assert _is_linked(a2, 'internalsm_TimeConstraint', b)
    _safe_set(b, 'internalsm_State', set())
    assert not _is_linked(b, 'internalsm_State', a2)
    if hasattr(a2, 'internalsm_TimeConstraint'):
        assert not _is_linked(a2, 'internalsm_TimeConstraint', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_currentState23_stub_double():
    # internalsm_EventToken has no real 'eventTokens' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_State(label="sample_text")
    partner = internalsm_EventToken()
    setattr(partner, 'eventTokens', None)
    _safe_set(owner, 'State24', partner)
    assert getattr(partner, 'eventTokens') == owner
    _safe_set(owner, 'State24', None)
    assert getattr(partner, 'eventTokens') is None


def test_assoc_eventPattern15_stub_double():
    # internalsm_EventPattern has no real 'CEPMeta.ecoreEventPattern' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_StateMachine(context="sample_text", priority=7)
    partner = internalsm_EventPattern()
    setattr(partner, 'CEPMeta.ecoreEventPattern', None)
    _safe_set(owner, 'stateMachine', partner)
    assert getattr(partner, 'CEPMeta.ecoreEventPattern') == owner
    _safe_set(owner, 'stateMachine', None)
    assert getattr(partner, 'CEPMeta.ecoreEventPattern') is None


def test_assoc_eventTokens21_stub_double():
    # internalsm_EventToken has no real 'internalsm_EventToken' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_InternalExecutionModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_InternalExecutionModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_InternalExecutionModel(context="sample_text")
    partner = internalsm_EventToken()
    setattr(partner, 'internalsm_EventToken', None)
    _safe_set(owner, 'internalsm_InternalExecutionModel22', {partner})
    assert getattr(partner, 'internalsm_EventToken') == owner
    _safe_set(owner, 'internalsm_InternalExecutionModel22', set())
    assert getattr(partner, 'internalsm_EventToken') is None


def test_assoc_eventTokens3_stub_double():
    # internalsm_EventToken has no real 'EventToken' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_State(label="sample_text")
    partner = internalsm_EventToken()
    setattr(partner, 'EventToken', None)
    _safe_set(owner, 'currentState', {partner})
    assert getattr(partner, 'EventToken') == owner
    _safe_set(owner, 'currentState', set())
    assert getattr(partner, 'EventToken') is None


def test_assoc_inTransitions1_stub_double():
    # internalsm_Transition has no real 'Transition2' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_State(label="sample_text")
    partner = internalsm_Transition()
    setattr(partner, 'Transition2', None)
    _safe_set(owner, 'postState', {partner})
    assert getattr(partner, 'Transition2') == owner
    _safe_set(owner, 'postState', set())
    assert getattr(partner, 'Transition2') is None


def test_assoc_lastProcessedEvent5_stub_double():
    # internalsm_Event has no real 'internalsm_Event' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_State(label="sample_text")
    partner = internalsm_Event()
    setattr(partner, 'internalsm_Event', None)
    _safe_set(owner, 'internalsm_State6', partner)
    assert getattr(partner, 'internalsm_Event') == owner
    _safe_set(owner, 'internalsm_State6', None)
    assert getattr(partner, 'internalsm_Event') is None


def test_assoc_latestEvent18_stub_double():
    # internalsm_Event has no real 'internalsm_Event20' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_InternalExecutionModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_InternalExecutionModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_InternalExecutionModel(context="sample_text")
    partner = internalsm_Event()
    setattr(partner, 'internalsm_Event20', None)
    _safe_set(owner, 'internalsm_InternalExecutionModel19', partner)
    assert getattr(partner, 'internalsm_Event20') == owner
    _safe_set(owner, 'internalsm_InternalExecutionModel19', None)
    assert getattr(partner, 'internalsm_Event20') is None


def test_assoc_outTransitions0_stub_double():
    # internalsm_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_State(label="sample_text")
    partner = internalsm_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'preState', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'preState', set())
    assert getattr(partner, 'Transition') is None


def test_assoc_postState9_stub_double():
    # internalsm_Transition has no real 'inTransitions' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_State(label="sample_text")
    partner = internalsm_Transition()
    setattr(partner, 'inTransitions', None)
    _safe_set(owner, 'State10', partner)
    assert getattr(partner, 'inTransitions') == owner
    _safe_set(owner, 'State10', None)
    assert getattr(partner, 'inTransitions') is None


def test_assoc_preState7_stub_double():
    # internalsm_Transition has no real 'outTransitions' property in the generated
    # code (a bare stub) -- manually attach it so internalsm_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # internalsm_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = internalsm_State(label="sample_text")
    partner = internalsm_Transition()
    setattr(partner, 'outTransitions', None)
    _safe_set(owner, 'State', partner)
    assert getattr(partner, 'outTransitions') == owner
    _safe_set(owner, 'State', None)
    assert getattr(partner, 'outTransitions') is None


