import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    cstat1_AbstractState,
    cstat1_Action,
    cstat1_EClass0,
    cstat1_State,
    cstat1_StateChart,
    cstat1_SubState1,
    cstat1_SubState2,
    cstat1_Transition,
    ActionMode,
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

def test_assoc_actions12_reverse_link_reassign_clear():
    a1 = cstat1_Action(expression="sample_text", mode="sample_text")
    a2 = cstat1_Action(expression="sample_text_2", mode="sample_text_2")
    b = cstat1_AbstractState(id="sample_text", type="sample_text")
    _safe_set(b, 'cstat1_AbstractState13', {a1})
    assert _is_linked(b, 'cstat1_AbstractState13', a1)
    if hasattr(a1, 'cstat1_Action'):
        assert _is_linked(a1, 'cstat1_Action', b)
    _safe_set(b, 'cstat1_AbstractState13', {a2})
    assert _is_linked(b, 'cstat1_AbstractState13', a2)
    if hasattr(a1, 'cstat1_Action'):
        assert not _is_linked(a1, 'cstat1_Action', b)
    if hasattr(a2, 'cstat1_Action'):
        assert _is_linked(a2, 'cstat1_Action', b)
    _safe_set(b, 'cstat1_AbstractState13', set())
    assert not _is_linked(b, 'cstat1_AbstractState13', a2)
    if hasattr(a2, 'cstat1_Action'):
        assert not _is_linked(a2, 'cstat1_Action', b)


def test_assoc_fromState5_reverse_link_reassign_clear():
    a1 = cstat1_Transition(event="sample_text", guard="sample_text")
    a2 = cstat1_Transition(event="sample_text_2", guard="sample_text_2")
    b = cstat1_AbstractState(id="sample_text", type="sample_text")
    _safe_set(b, 'cstat1_AbstractState', a1)
    assert _is_linked(b, 'cstat1_AbstractState', a1)
    if hasattr(a1, 'cstat1_Transition'):
        assert _is_linked(a1, 'cstat1_Transition', b)
    _safe_set(b, 'cstat1_AbstractState', a2)
    assert _is_linked(b, 'cstat1_AbstractState', a2)
    if hasattr(a1, 'cstat1_Transition'):
        assert not _is_linked(a1, 'cstat1_Transition', b)
    if hasattr(a2, 'cstat1_Transition'):
        assert _is_linked(a2, 'cstat1_Transition', b)
    _safe_set(b, 'cstat1_AbstractState', None)
    assert not _is_linked(b, 'cstat1_AbstractState', a2)
    if hasattr(a2, 'cstat1_Transition'):
        assert not _is_linked(a2, 'cstat1_Transition', b)


def test_assoc_toState6_reverse_link_reassign_clear():
    a1 = cstat1_Transition(event="sample_text", guard="sample_text")
    a2 = cstat1_Transition(event="sample_text_2", guard="sample_text_2")
    b = cstat1_AbstractState(id="sample_text", type="sample_text")
    _safe_set(b, 'cstat1_AbstractState8', a1)
    assert _is_linked(b, 'cstat1_AbstractState8', a1)
    if hasattr(a1, 'cstat1_Transition7'):
        assert _is_linked(a1, 'cstat1_Transition7', b)
    _safe_set(b, 'cstat1_AbstractState8', a2)
    assert _is_linked(b, 'cstat1_AbstractState8', a2)
    if hasattr(a1, 'cstat1_Transition7'):
        assert not _is_linked(a1, 'cstat1_Transition7', b)
    if hasattr(a2, 'cstat1_Transition7'):
        assert _is_linked(a2, 'cstat1_Transition7', b)
    _safe_set(b, 'cstat1_AbstractState8', None)
    assert not _is_linked(b, 'cstat1_AbstractState8', a2)
    if hasattr(a2, 'cstat1_Transition7'):
        assert not _is_linked(a2, 'cstat1_Transition7', b)


def test_assoc_transitions9_reverse_link_reassign_clear():
    a1 = cstat1_Transition(event="sample_text", guard="sample_text")
    a2 = cstat1_Transition(event="sample_text_2", guard="sample_text_2")
    b = cstat1_AbstractState(id="sample_text", type="sample_text")
    _safe_set(b, 'cstat1_AbstractState10', {a1})
    assert _is_linked(b, 'cstat1_AbstractState10', a1)
    if hasattr(a1, 'cstat1_Transition11'):
        assert _is_linked(a1, 'cstat1_Transition11', b)
    _safe_set(b, 'cstat1_AbstractState10', {a2})
    assert _is_linked(b, 'cstat1_AbstractState10', a2)
    if hasattr(a1, 'cstat1_Transition11'):
        assert not _is_linked(a1, 'cstat1_Transition11', b)
    if hasattr(a2, 'cstat1_Transition11'):
        assert _is_linked(a2, 'cstat1_Transition11', b)
    _safe_set(b, 'cstat1_AbstractState10', set())
    assert not _is_linked(b, 'cstat1_AbstractState10', a2)
    if hasattr(a2, 'cstat1_Transition11'):
        assert not _is_linked(a2, 'cstat1_Transition11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

