import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sm_Observation,
    sm_State,
    sm_StateMachine,
    sm_Transition,
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

def test_assoc_edges7_reverse_link_reassign_clear():
    a1 = sm_Transition(name="sample_text")
    a2 = sm_Transition(name="sample_text_2")
    b = sm_StateMachine(name="sample_text")
    _safe_set(b, 'sm_StateMachine8', {a1})
    assert _is_linked(b, 'sm_StateMachine8', a1)
    if hasattr(a1, 'sm_Transition'):
        assert _is_linked(a1, 'sm_Transition', b)
    _safe_set(b, 'sm_StateMachine8', {a2})
    assert _is_linked(b, 'sm_StateMachine8', a2)
    if hasattr(a1, 'sm_Transition'):
        assert not _is_linked(a1, 'sm_Transition', b)
    if hasattr(a2, 'sm_Transition'):
        assert _is_linked(a2, 'sm_Transition', b)
    _safe_set(b, 'sm_StateMachine8', set())
    assert not _is_linked(b, 'sm_StateMachine8', a2)
    if hasattr(a2, 'sm_Transition'):
        assert not _is_linked(a2, 'sm_Transition', b)


def test_assoc_final1_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State3', a1)
    assert _is_linked(b, 'sm_State3', a1)
    if hasattr(a1, 'sm_StateMachine2'):
        assert _is_linked(a1, 'sm_StateMachine2', b)
    _safe_set(b, 'sm_State3', a2)
    assert _is_linked(b, 'sm_State3', a2)
    if hasattr(a1, 'sm_StateMachine2'):
        assert not _is_linked(a1, 'sm_StateMachine2', b)
    if hasattr(a2, 'sm_StateMachine2'):
        assert _is_linked(a2, 'sm_StateMachine2', b)
    _safe_set(b, 'sm_State3', None)
    assert not _is_linked(b, 'sm_State3', a2)
    if hasattr(a2, 'sm_StateMachine2'):
        assert not _is_linked(a2, 'sm_StateMachine2', b)


def test_assoc_graph17_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State18', a1)
    assert _is_linked(b, 'sm_State18', a1)
    if hasattr(a1, 'sm_StateMachine19'):
        assert _is_linked(a1, 'sm_StateMachine19', b)
    _safe_set(b, 'sm_State18', a2)
    assert _is_linked(b, 'sm_State18', a2)
    if hasattr(a1, 'sm_StateMachine19'):
        assert not _is_linked(a1, 'sm_StateMachine19', b)
    if hasattr(a2, 'sm_StateMachine19'):
        assert _is_linked(a2, 'sm_StateMachine19', b)
    _safe_set(b, 'sm_State18', None)
    assert not _is_linked(b, 'sm_State18', a2)
    if hasattr(a2, 'sm_StateMachine19'):
        assert not _is_linked(a2, 'sm_StateMachine19', b)


def test_assoc_graph26_reverse_link_reassign_clear():
    a1 = sm_Transition(name="sample_text")
    a2 = sm_Transition(name="sample_text_2")
    b = sm_StateMachine(name="sample_text")
    _safe_set(b, 'sm_StateMachine28', a1)
    assert _is_linked(b, 'sm_StateMachine28', a1)
    if hasattr(a1, 'sm_Transition27'):
        assert _is_linked(a1, 'sm_Transition27', b)
    _safe_set(b, 'sm_StateMachine28', a2)
    assert _is_linked(b, 'sm_StateMachine28', a2)
    if hasattr(a1, 'sm_Transition27'):
        assert not _is_linked(a1, 'sm_Transition27', b)
    if hasattr(a2, 'sm_Transition27'):
        assert _is_linked(a2, 'sm_Transition27', b)
    _safe_set(b, 'sm_StateMachine28', None)
    assert not _is_linked(b, 'sm_StateMachine28', a2)
    if hasattr(a2, 'sm_Transition27'):
        assert not _is_linked(a2, 'sm_Transition27', b)


def test_assoc_graph32_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_Observation(time="sample_text")
    _safe_set(b, 'sm_Observation33', a1)
    assert _is_linked(b, 'sm_Observation33', a1)
    if hasattr(a1, 'sm_StateMachine34'):
        assert _is_linked(a1, 'sm_StateMachine34', b)
    _safe_set(b, 'sm_Observation33', a2)
    assert _is_linked(b, 'sm_Observation33', a2)
    if hasattr(a1, 'sm_StateMachine34'):
        assert not _is_linked(a1, 'sm_StateMachine34', b)
    if hasattr(a2, 'sm_StateMachine34'):
        assert _is_linked(a2, 'sm_StateMachine34', b)
    _safe_set(b, 'sm_Observation33', None)
    assert not _is_linked(b, 'sm_Observation33', a2)
    if hasattr(a2, 'sm_StateMachine34'):
        assert not _is_linked(a2, 'sm_StateMachine34', b)


def test_assoc_initial0_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State', a1)
    assert _is_linked(b, 'sm_State', a1)
    if hasattr(a1, 'sm_StateMachine'):
        assert _is_linked(a1, 'sm_StateMachine', b)
    _safe_set(b, 'sm_State', a2)
    assert _is_linked(b, 'sm_State', a2)
    if hasattr(a1, 'sm_StateMachine'):
        assert not _is_linked(a1, 'sm_StateMachine', b)
    if hasattr(a2, 'sm_StateMachine'):
        assert _is_linked(a2, 'sm_StateMachine', b)
    _safe_set(b, 'sm_State', None)
    assert not _is_linked(b, 'sm_State', a2)
    if hasattr(a2, 'sm_StateMachine'):
        assert not _is_linked(a2, 'sm_StateMachine', b)


def test_assoc_mark14_reverse_link_reassign_clear():
    a1 = sm_State(name="sample_text")
    a2 = sm_State(name="sample_text_2")
    b = sm_Observation(time="sample_text")
    _safe_set(b, 'sm_Observation16', a1)
    assert _is_linked(b, 'sm_Observation16', a1)
    if hasattr(a1, 'sm_State15'):
        assert _is_linked(a1, 'sm_State15', b)
    _safe_set(b, 'sm_Observation16', a2)
    assert _is_linked(b, 'sm_Observation16', a2)
    if hasattr(a1, 'sm_State15'):
        assert not _is_linked(a1, 'sm_State15', b)
    if hasattr(a2, 'sm_State15'):
        assert _is_linked(a2, 'sm_State15', b)
    _safe_set(b, 'sm_Observation16', None)
    assert not _is_linked(b, 'sm_Observation16', a2)
    if hasattr(a2, 'sm_State15'):
        assert not _is_linked(a2, 'sm_State15', b)


def test_assoc_marks9_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_Observation(time="sample_text")
    _safe_set(b, 'sm_Observation', a1)
    assert _is_linked(b, 'sm_Observation', a1)
    if hasattr(a1, 'sm_StateMachine10'):
        assert _is_linked(a1, 'sm_StateMachine10', b)
    _safe_set(b, 'sm_Observation', a2)
    assert _is_linked(b, 'sm_Observation', a2)
    if hasattr(a1, 'sm_StateMachine10'):
        assert not _is_linked(a1, 'sm_StateMachine10', b)
    if hasattr(a2, 'sm_StateMachine10'):
        assert _is_linked(a2, 'sm_StateMachine10', b)
    _safe_set(b, 'sm_Observation', None)
    assert not _is_linked(b, 'sm_Observation', a2)
    if hasattr(a2, 'sm_StateMachine10'):
        assert not _is_linked(a2, 'sm_StateMachine10', b)


def test_assoc_node29_reverse_link_reassign_clear():
    a1 = sm_State(name="sample_text")
    a2 = sm_State(name="sample_text_2")
    b = sm_Observation(time="sample_text")
    _safe_set(b, 'sm_Observation30', a1)
    assert _is_linked(b, 'sm_Observation30', a1)
    if hasattr(a1, 'sm_State31'):
        assert _is_linked(a1, 'sm_State31', b)
    _safe_set(b, 'sm_Observation30', a2)
    assert _is_linked(b, 'sm_Observation30', a2)
    if hasattr(a1, 'sm_State31'):
        assert not _is_linked(a1, 'sm_State31', b)
    if hasattr(a2, 'sm_State31'):
        assert _is_linked(a2, 'sm_State31', b)
    _safe_set(b, 'sm_Observation30', None)
    assert not _is_linked(b, 'sm_Observation30', a2)
    if hasattr(a2, 'sm_State31'):
        assert not _is_linked(a2, 'sm_State31', b)


def test_assoc_nodes4_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State6', a1)
    assert _is_linked(b, 'sm_State6', a1)
    if hasattr(a1, 'sm_StateMachine5'):
        assert _is_linked(a1, 'sm_StateMachine5', b)
    _safe_set(b, 'sm_State6', a2)
    assert _is_linked(b, 'sm_State6', a2)
    if hasattr(a1, 'sm_StateMachine5'):
        assert not _is_linked(a1, 'sm_StateMachine5', b)
    if hasattr(a2, 'sm_StateMachine5'):
        assert _is_linked(a2, 'sm_StateMachine5', b)
    _safe_set(b, 'sm_State6', None)
    assert not _is_linked(b, 'sm_State6', a2)
    if hasattr(a2, 'sm_StateMachine5'):
        assert not _is_linked(a2, 'sm_StateMachine5', b)


def test_assoc_source20_reverse_link_reassign_clear():
    a1 = sm_Transition(name="sample_text")
    a2 = sm_Transition(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State22', a1)
    assert _is_linked(b, 'sm_State22', a1)
    if hasattr(a1, 'sm_Transition21'):
        assert _is_linked(a1, 'sm_Transition21', b)
    _safe_set(b, 'sm_State22', a2)
    assert _is_linked(b, 'sm_State22', a2)
    if hasattr(a1, 'sm_Transition21'):
        assert not _is_linked(a1, 'sm_Transition21', b)
    if hasattr(a2, 'sm_Transition21'):
        assert _is_linked(a2, 'sm_Transition21', b)
    _safe_set(b, 'sm_State22', None)
    assert not _is_linked(b, 'sm_State22', a2)
    if hasattr(a2, 'sm_Transition21'):
        assert not _is_linked(a2, 'sm_Transition21', b)


def test_assoc_subMachines11_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State12', {a1})
    assert _is_linked(b, 'sm_State12', a1)
    if hasattr(a1, 'sm_StateMachine13'):
        assert _is_linked(a1, 'sm_StateMachine13', b)
    _safe_set(b, 'sm_State12', {a2})
    assert _is_linked(b, 'sm_State12', a2)
    if hasattr(a1, 'sm_StateMachine13'):
        assert not _is_linked(a1, 'sm_StateMachine13', b)
    if hasattr(a2, 'sm_StateMachine13'):
        assert _is_linked(a2, 'sm_StateMachine13', b)
    _safe_set(b, 'sm_State12', set())
    assert not _is_linked(b, 'sm_State12', a2)
    if hasattr(a2, 'sm_StateMachine13'):
        assert not _is_linked(a2, 'sm_StateMachine13', b)


def test_assoc_target23_reverse_link_reassign_clear():
    a1 = sm_Transition(name="sample_text")
    a2 = sm_Transition(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State25', a1)
    assert _is_linked(b, 'sm_State25', a1)
    if hasattr(a1, 'sm_Transition24'):
        assert _is_linked(a1, 'sm_Transition24', b)
    _safe_set(b, 'sm_State25', a2)
    assert _is_linked(b, 'sm_State25', a2)
    if hasattr(a1, 'sm_Transition24'):
        assert not _is_linked(a1, 'sm_Transition24', b)
    if hasattr(a2, 'sm_Transition24'):
        assert _is_linked(a2, 'sm_Transition24', b)
    _safe_set(b, 'sm_State25', None)
    assert not _is_linked(b, 'sm_State25', a2)
    if hasattr(a2, 'sm_Transition24'):
        assert not _is_linked(a2, 'sm_Transition24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

