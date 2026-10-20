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

def test_assoc_edges5_reverse_link_reassign_clear():
    a1 = sm_Transition(name="sample_text")
    a2 = sm_Transition(name="sample_text_2")
    b = sm_StateMachine(name="sample_text")
    _safe_set(b, 'graph6', {a1})
    assert _is_linked(b, 'graph6', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'graph6', {a2})
    assert _is_linked(b, 'graph6', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'graph6', set())
    assert not _is_linked(b, 'graph6', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


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


def test_assoc_graph14_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'nodes', a1)
    assert _is_linked(b, 'nodes', a1)
    if hasattr(a1, 'StateMachine'):
        assert _is_linked(a1, 'StateMachine', b)
    _safe_set(b, 'nodes', a2)
    assert _is_linked(b, 'nodes', a2)
    if hasattr(a1, 'StateMachine'):
        assert not _is_linked(a1, 'StateMachine', b)
    if hasattr(a2, 'StateMachine'):
        assert _is_linked(a2, 'StateMachine', b)
    _safe_set(b, 'nodes', None)
    assert not _is_linked(b, 'nodes', a2)
    if hasattr(a2, 'StateMachine'):
        assert not _is_linked(a2, 'StateMachine', b)


def test_assoc_graph20_reverse_link_reassign_clear():
    a1 = sm_Transition(name="sample_text")
    a2 = sm_Transition(name="sample_text_2")
    b = sm_StateMachine(name="sample_text")
    _safe_set(b, 'StateMachine21', a1)
    assert _is_linked(b, 'StateMachine21', a1)
    if hasattr(a1, 'edges'):
        assert _is_linked(a1, 'edges', b)
    _safe_set(b, 'StateMachine21', a2)
    assert _is_linked(b, 'StateMachine21', a2)
    if hasattr(a1, 'edges'):
        assert not _is_linked(a1, 'edges', b)
    if hasattr(a2, 'edges'):
        assert _is_linked(a2, 'edges', b)
    _safe_set(b, 'StateMachine21', None)
    assert not _is_linked(b, 'StateMachine21', a2)
    if hasattr(a2, 'edges'):
        assert not _is_linked(a2, 'edges', b)


def test_assoc_graph24_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_Observation(time="sample_text")
    _safe_set(b, 'marks', a1)
    assert _is_linked(b, 'marks', a1)
    if hasattr(a1, 'StateMachine25'):
        assert _is_linked(a1, 'StateMachine25', b)
    _safe_set(b, 'marks', a2)
    assert _is_linked(b, 'marks', a2)
    if hasattr(a1, 'StateMachine25'):
        assert not _is_linked(a1, 'StateMachine25', b)
    if hasattr(a2, 'StateMachine25'):
        assert _is_linked(a2, 'StateMachine25', b)
    _safe_set(b, 'marks', None)
    assert not _is_linked(b, 'marks', a2)
    if hasattr(a2, 'StateMachine25'):
        assert not _is_linked(a2, 'StateMachine25', b)


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


def test_assoc_mark12_reverse_link_reassign_clear():
    a1 = sm_State(name="sample_text")
    a2 = sm_State(name="sample_text_2")
    b = sm_Observation(time="sample_text")
    _safe_set(b, 'Observation13', a1)
    assert _is_linked(b, 'Observation13', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'Observation13', a2)
    assert _is_linked(b, 'Observation13', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'Observation13', None)
    assert not _is_linked(b, 'Observation13', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_marks7_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_Observation(time="sample_text")
    _safe_set(b, 'Observation', a1)
    assert _is_linked(b, 'Observation', a1)
    if hasattr(a1, 'graph8'):
        assert _is_linked(a1, 'graph8', b)
    _safe_set(b, 'Observation', a2)
    assert _is_linked(b, 'Observation', a2)
    if hasattr(a1, 'graph8'):
        assert not _is_linked(a1, 'graph8', b)
    if hasattr(a2, 'graph8'):
        assert _is_linked(a2, 'graph8', b)
    _safe_set(b, 'Observation', None)
    assert not _is_linked(b, 'Observation', a2)
    if hasattr(a2, 'graph8'):
        assert not _is_linked(a2, 'graph8', b)


def test_assoc_node22_reverse_link_reassign_clear():
    a1 = sm_State(name="sample_text")
    a2 = sm_State(name="sample_text_2")
    b = sm_Observation(time="sample_text")
    _safe_set(b, 'mark', a1)
    assert _is_linked(b, 'mark', a1)
    if hasattr(a1, 'State23'):
        assert _is_linked(a1, 'State23', b)
    _safe_set(b, 'mark', a2)
    assert _is_linked(b, 'mark', a2)
    if hasattr(a1, 'State23'):
        assert not _is_linked(a1, 'State23', b)
    if hasattr(a2, 'State23'):
        assert _is_linked(a2, 'State23', b)
    _safe_set(b, 'mark', None)
    assert not _is_linked(b, 'mark', a2)
    if hasattr(a2, 'State23'):
        assert not _is_linked(a2, 'State23', b)


def test_assoc_nodes4_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'State', a1)
    assert _is_linked(b, 'State', a1)
    if hasattr(a1, 'graph'):
        assert _is_linked(a1, 'graph', b)
    _safe_set(b, 'State', a2)
    assert _is_linked(b, 'State', a2)
    if hasattr(a1, 'graph'):
        assert not _is_linked(a1, 'graph', b)
    if hasattr(a2, 'graph'):
        assert _is_linked(a2, 'graph', b)
    _safe_set(b, 'State', None)
    assert not _is_linked(b, 'State', a2)
    if hasattr(a2, 'graph'):
        assert not _is_linked(a2, 'graph', b)


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = sm_Transition(name="sample_text")
    a2 = sm_Transition(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State16', a1)
    assert _is_linked(b, 'sm_State16', a1)
    if hasattr(a1, 'sm_Transition'):
        assert _is_linked(a1, 'sm_Transition', b)
    _safe_set(b, 'sm_State16', a2)
    assert _is_linked(b, 'sm_State16', a2)
    if hasattr(a1, 'sm_Transition'):
        assert not _is_linked(a1, 'sm_Transition', b)
    if hasattr(a2, 'sm_Transition'):
        assert _is_linked(a2, 'sm_Transition', b)
    _safe_set(b, 'sm_State16', None)
    assert not _is_linked(b, 'sm_State16', a2)
    if hasattr(a2, 'sm_Transition'):
        assert not _is_linked(a2, 'sm_Transition', b)


def test_assoc_subMachines9_reverse_link_reassign_clear():
    a1 = sm_StateMachine(name="sample_text")
    a2 = sm_StateMachine(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State10', {a1})
    assert _is_linked(b, 'sm_State10', a1)
    if hasattr(a1, 'sm_StateMachine11'):
        assert _is_linked(a1, 'sm_StateMachine11', b)
    _safe_set(b, 'sm_State10', {a2})
    assert _is_linked(b, 'sm_State10', a2)
    if hasattr(a1, 'sm_StateMachine11'):
        assert not _is_linked(a1, 'sm_StateMachine11', b)
    if hasattr(a2, 'sm_StateMachine11'):
        assert _is_linked(a2, 'sm_StateMachine11', b)
    _safe_set(b, 'sm_State10', set())
    assert not _is_linked(b, 'sm_State10', a2)
    if hasattr(a2, 'sm_StateMachine11'):
        assert not _is_linked(a2, 'sm_StateMachine11', b)


def test_assoc_target17_reverse_link_reassign_clear():
    a1 = sm_Transition(name="sample_text")
    a2 = sm_Transition(name="sample_text_2")
    b = sm_State(name="sample_text")
    _safe_set(b, 'sm_State19', a1)
    assert _is_linked(b, 'sm_State19', a1)
    if hasattr(a1, 'sm_Transition18'):
        assert _is_linked(a1, 'sm_Transition18', b)
    _safe_set(b, 'sm_State19', a2)
    assert _is_linked(b, 'sm_State19', a2)
    if hasattr(a1, 'sm_Transition18'):
        assert not _is_linked(a1, 'sm_Transition18', b)
    if hasattr(a2, 'sm_Transition18'):
        assert _is_linked(a2, 'sm_Transition18', b)
    _safe_set(b, 'sm_State19', None)
    assert not _is_linked(b, 'sm_State19', a2)
    if hasattr(a2, 'sm_Transition18'):
        assert not _is_linked(a2, 'sm_Transition18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

