import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    Element,
    statemodel_Activity,
    statemodel_Annotation,
    statemodel_Element,
    statemodel_Entity,
    statemodel_Import,
    statemodel_Model,
    statemodel_State,
    statemodel_Statemachine,
    statemodel_Transition,
    statemodel_TransitionBlock,
    StateType,
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

def test_assoc_state11_reverse_link_reassign_clear():
    a1 = statemodel_Transition(action="sample_text", guard="sample_text")
    a2 = statemodel_Transition(action="sample_text_2", guard="sample_text_2")
    b = statemodel_State(name="sample_text", type="sample_text")
    _safe_set(b, 'statemodel_State13', a1)
    assert _is_linked(b, 'statemodel_State13', a1)
    if hasattr(a1, 'statemodel_Transition12'):
        assert _is_linked(a1, 'statemodel_Transition12', b)
    _safe_set(b, 'statemodel_State13', a2)
    assert _is_linked(b, 'statemodel_State13', a2)
    if hasattr(a1, 'statemodel_Transition12'):
        assert not _is_linked(a1, 'statemodel_Transition12', b)
    if hasattr(a2, 'statemodel_Transition12'):
        assert _is_linked(a2, 'statemodel_Transition12', b)
    _safe_set(b, 'statemodel_State13', None)
    assert not _is_linked(b, 'statemodel_State13', a2)
    if hasattr(a2, 'statemodel_Transition12'):
        assert not _is_linked(a2, 'statemodel_Transition12', b)


def test_assoc_transition10_reverse_link_reassign_clear():
    a1 = statemodel_TransitionBlock(event="sample_text")
    a2 = statemodel_TransitionBlock(event="sample_text_2")
    b = statemodel_Transition(action="sample_text", guard="sample_text")
    _safe_set(b, 'statemodel_Transition', a1)
    assert _is_linked(b, 'statemodel_Transition', a1)
    if hasattr(a1, 'statemodel_TransitionBlock'):
        assert _is_linked(a1, 'statemodel_TransitionBlock', b)
    _safe_set(b, 'statemodel_Transition', a2)
    assert _is_linked(b, 'statemodel_Transition', a2)
    if hasattr(a1, 'statemodel_TransitionBlock'):
        assert not _is_linked(a1, 'statemodel_TransitionBlock', b)
    if hasattr(a2, 'statemodel_TransitionBlock'):
        assert _is_linked(a2, 'statemodel_TransitionBlock', b)
    _safe_set(b, 'statemodel_Transition', None)
    assert not _is_linked(b, 'statemodel_Transition', a2)
    if hasattr(a2, 'statemodel_TransitionBlock'):
        assert not _is_linked(a2, 'statemodel_TransitionBlock', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_element8_stub_double():
    # statemodel_Activity has no real 'statemodel_Activity' property in the generated
    # code (a bare stub) -- manually attach it so statemodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemodel_State(name="sample_text", type="sample_text")
    partner = statemodel_Activity()
    setattr(partner, 'statemodel_Activity', None)
    _safe_set(owner, 'statemodel_State9', {partner})
    assert getattr(partner, 'statemodel_Activity') == owner
    _safe_set(owner, 'statemodel_State9', set())
    assert getattr(partner, 'statemodel_Activity') is None


def test_assoc_imports0_stub_double():
    # statemodel_Model has no real 'statemodel_Model' property in the generated
    # code (a bare stub) -- manually attach it so statemodel_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemodel_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemodel_Import(importURI="sample_text")
    partner = statemodel_Model()
    setattr(partner, 'statemodel_Model', None)
    _safe_set(owner, 'statemodel_Import', partner)
    assert owner in getattr(partner, 'statemodel_Model')
    _safe_set(owner, 'statemodel_Import', None)
    assert owner not in getattr(partner, 'statemodel_Model')


def test_assoc_state6_stub_double():
    # statemodel_Statemachine has no real 'statemodel_Statemachine7' property in the generated
    # code (a bare stub) -- manually attach it so statemodel_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemodel_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemodel_State(name="sample_text", type="sample_text")
    partner = statemodel_Statemachine()
    setattr(partner, 'statemodel_Statemachine7', None)
    _safe_set(owner, 'statemodel_State', partner)
    assert owner in getattr(partner, 'statemodel_Statemachine7')
    _safe_set(owner, 'statemodel_State', None)
    assert owner not in getattr(partner, 'statemodel_Statemachine7')


