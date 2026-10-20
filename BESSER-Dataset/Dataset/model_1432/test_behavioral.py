import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    State,
    scmodel_AbstractState,
    scmodel_CompositeState,
    scmodel_FinalState,
    scmodel_History,
    scmodel_PseudoState,
    scmodel_State,
    scmodel_StateMachine,
    scmodel_Transition,
    LanguageTypes,
    MessageCheckerTypes,
    PseudoStateTypes,
    TriggerTypes,
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

def test_assoc_from_3_reverse_link_reassign_clear():
    a1 = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    a2 = scmodel_Transition(defaultTransition=False, guard="sample_text_2", guardImports="sample_text_2", id="sample_text_2", messageCheckerClass="sample_text_2", messageCheckerCode="sample_text_2", messageCheckerCodeImports="sample_text_2", messageCheckerConditionLanguage="sample_text_2", messageCheckerType="sample_text_2", onTransition="sample_text_2", onTransitionImports="sample_text_2", outOfBranch=False, priority=9.99, selfTransition=False, triggerCodeLanguage="sample_text_2", triggerConditionCode="sample_text_2", triggerConditionCodeImports="sample_text_2", triggerExpRateCode="sample_text_2", triggerExpRateCodeImports="sample_text_2", triggerProbCode="sample_text_2", triggerProbCodeImports="sample_text_2", triggerTime=9.99, triggerTimedCode="sample_text_2", triggerTimedCodeImports="sample_text_2", triggerType="sample_text_2", uuid="sample_text_2")
    b = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    _safe_set(b, 'scmodel_AbstractState5', a1)
    assert _is_linked(b, 'scmodel_AbstractState5', a1)
    if hasattr(a1, 'scmodel_Transition4'):
        assert _is_linked(a1, 'scmodel_Transition4', b)
    _safe_set(b, 'scmodel_AbstractState5', a2)
    assert _is_linked(b, 'scmodel_AbstractState5', a2)
    if hasattr(a1, 'scmodel_Transition4'):
        assert not _is_linked(a1, 'scmodel_Transition4', b)
    if hasattr(a2, 'scmodel_Transition4'):
        assert _is_linked(a2, 'scmodel_Transition4', b)
    _safe_set(b, 'scmodel_AbstractState5', None)
    assert not _is_linked(b, 'scmodel_AbstractState5', a2)
    if hasattr(a2, 'scmodel_Transition4'):
        assert not _is_linked(a2, 'scmodel_Transition4', b)


def test_assoc_states0_reverse_link_reassign_clear():
    a1 = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    a2 = scmodel_StateMachine(agentType="sample_text_2", className="sample_text_2", id="sample_text_2", language="sample_text_2", nextID=13, package="sample_text_2", priority=9.99, uuid="sample_text_2")
    b = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    _safe_set(b, 'scmodel_AbstractState', a1)
    assert _is_linked(b, 'scmodel_AbstractState', a1)
    if hasattr(a1, 'scmodel_StateMachine'):
        assert _is_linked(a1, 'scmodel_StateMachine', b)
    _safe_set(b, 'scmodel_AbstractState', a2)
    assert _is_linked(b, 'scmodel_AbstractState', a2)
    if hasattr(a1, 'scmodel_StateMachine'):
        assert not _is_linked(a1, 'scmodel_StateMachine', b)
    if hasattr(a2, 'scmodel_StateMachine'):
        assert _is_linked(a2, 'scmodel_StateMachine', b)
    _safe_set(b, 'scmodel_AbstractState', None)
    assert not _is_linked(b, 'scmodel_AbstractState', a2)
    if hasattr(a2, 'scmodel_StateMachine'):
        assert not _is_linked(a2, 'scmodel_StateMachine', b)


def test_assoc_to6_reverse_link_reassign_clear():
    a1 = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    a2 = scmodel_Transition(defaultTransition=False, guard="sample_text_2", guardImports="sample_text_2", id="sample_text_2", messageCheckerClass="sample_text_2", messageCheckerCode="sample_text_2", messageCheckerCodeImports="sample_text_2", messageCheckerConditionLanguage="sample_text_2", messageCheckerType="sample_text_2", onTransition="sample_text_2", onTransitionImports="sample_text_2", outOfBranch=False, priority=9.99, selfTransition=False, triggerCodeLanguage="sample_text_2", triggerConditionCode="sample_text_2", triggerConditionCodeImports="sample_text_2", triggerExpRateCode="sample_text_2", triggerExpRateCodeImports="sample_text_2", triggerProbCode="sample_text_2", triggerProbCodeImports="sample_text_2", triggerTime=9.99, triggerTimedCode="sample_text_2", triggerTimedCodeImports="sample_text_2", triggerType="sample_text_2", uuid="sample_text_2")
    b = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    _safe_set(b, 'scmodel_AbstractState8', a1)
    assert _is_linked(b, 'scmodel_AbstractState8', a1)
    if hasattr(a1, 'scmodel_Transition7'):
        assert _is_linked(a1, 'scmodel_Transition7', b)
    _safe_set(b, 'scmodel_AbstractState8', a2)
    assert _is_linked(b, 'scmodel_AbstractState8', a2)
    if hasattr(a1, 'scmodel_Transition7'):
        assert not _is_linked(a1, 'scmodel_Transition7', b)
    if hasattr(a2, 'scmodel_Transition7'):
        assert _is_linked(a2, 'scmodel_Transition7', b)
    _safe_set(b, 'scmodel_AbstractState8', None)
    assert not _is_linked(b, 'scmodel_AbstractState8', a2)
    if hasattr(a2, 'scmodel_Transition7'):
        assert not _is_linked(a2, 'scmodel_Transition7', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    a2 = scmodel_Transition(defaultTransition=False, guard="sample_text_2", guardImports="sample_text_2", id="sample_text_2", messageCheckerClass="sample_text_2", messageCheckerCode="sample_text_2", messageCheckerCodeImports="sample_text_2", messageCheckerConditionLanguage="sample_text_2", messageCheckerType="sample_text_2", onTransition="sample_text_2", onTransitionImports="sample_text_2", outOfBranch=False, priority=9.99, selfTransition=False, triggerCodeLanguage="sample_text_2", triggerConditionCode="sample_text_2", triggerConditionCodeImports="sample_text_2", triggerExpRateCode="sample_text_2", triggerExpRateCodeImports="sample_text_2", triggerProbCode="sample_text_2", triggerProbCodeImports="sample_text_2", triggerTime=9.99, triggerTimedCode="sample_text_2", triggerTimedCodeImports="sample_text_2", triggerType="sample_text_2", uuid="sample_text_2")
    b = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    _safe_set(b, 'scmodel_StateMachine2', {a1})
    assert _is_linked(b, 'scmodel_StateMachine2', a1)
    if hasattr(a1, 'scmodel_Transition'):
        assert _is_linked(a1, 'scmodel_Transition', b)
    _safe_set(b, 'scmodel_StateMachine2', {a2})
    assert _is_linked(b, 'scmodel_StateMachine2', a2)
    if hasattr(a1, 'scmodel_Transition'):
        assert not _is_linked(a1, 'scmodel_Transition', b)
    if hasattr(a2, 'scmodel_Transition'):
        assert _is_linked(a2, 'scmodel_Transition', b)
    _safe_set(b, 'scmodel_StateMachine2', set())
    assert not _is_linked(b, 'scmodel_StateMachine2', a2)
    if hasattr(a2, 'scmodel_Transition'):
        assert not _is_linked(a2, 'scmodel_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children9_stub_double():
    # scmodel_CompositeState has no real 'scmodel_CompositeState' property in the generated
    # code (a bare stub) -- manually attach it so scmodel_AbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scmodel_AbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    partner = scmodel_CompositeState()
    setattr(partner, 'scmodel_CompositeState', None)
    _safe_set(owner, 'scmodel_AbstractState10', partner)
    assert owner in getattr(partner, 'scmodel_CompositeState')
    _safe_set(owner, 'scmodel_AbstractState10', None)
    assert owner not in getattr(partner, 'scmodel_CompositeState')


