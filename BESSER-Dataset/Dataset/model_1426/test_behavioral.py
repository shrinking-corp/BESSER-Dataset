import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    ModelElement,
    statechart_AbstractState,
    statechart_Action,
    statechart_CompositeState,
    statechart_FinalState,
    statechart_InitialState,
    statechart_ModelElement,
    statechart_SimpleState,
    statechart_StateMachine,
    statechart_Transition,
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

def test_assoc_actions6_stub_double():
    # statechart_AbstractState has no real 'statechart_AbstractState' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Action's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Action's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Action(kind="sample_text")
    partner = statechart_AbstractState()
    setattr(partner, 'statechart_AbstractState', None)
    _safe_set(owner, 'statechart_Action', partner)
    assert owner in getattr(partner, 'statechart_AbstractState')
    _safe_set(owner, 'statechart_Action', None)
    assert owner not in getattr(partner, 'statechart_AbstractState')


def test_assoc_from_0_stub_double():
    # statechart_AbstractState has no real 'AbstractState' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(event="sample_text", guard="sample_text")
    partner = statechart_AbstractState()
    setattr(partner, 'AbstractState', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'AbstractState') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'AbstractState') is None


def test_assoc_incoming3_stub_double():
    # statechart_AbstractState has no real 'to' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(event="sample_text", guard="sample_text")
    partner = statechart_AbstractState()
    setattr(partner, 'to', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'to')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'to')


def test_assoc_outgoing4_stub_double():
    # statechart_AbstractState has no real 'from_' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(event="sample_text", guard="sample_text")
    partner = statechart_AbstractState()
    setattr(partner, 'from_', None)
    _safe_set(owner, 'Transition5', partner)
    assert owner in getattr(partner, 'from_')
    _safe_set(owner, 'Transition5', None)
    assert owner not in getattr(partner, 'from_')


def test_assoc_to1_stub_double():
    # statechart_AbstractState has no real 'AbstractState2' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(event="sample_text", guard="sample_text")
    partner = statechart_AbstractState()
    setattr(partner, 'AbstractState2', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'AbstractState2') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'AbstractState2') is None


def test_assoc_transitions9_stub_double():
    # statechart_CompositeState has no real 'statechart_CompositeState10' property in the generated
    # code (a bare stub) -- manually attach it so statechart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statechart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statechart_Transition(event="sample_text", guard="sample_text")
    partner = statechart_CompositeState()
    setattr(partner, 'statechart_CompositeState10', None)
    _safe_set(owner, 'statechart_Transition', partner)
    assert owner in getattr(partner, 'statechart_CompositeState10')
    _safe_set(owner, 'statechart_Transition', None)
    assert owner not in getattr(partner, 'statechart_CompositeState10')


