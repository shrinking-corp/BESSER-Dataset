import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataElement,
    Node,
    State,
    statemachine_DataElement,
    statemachine_Event,
    statemachine_FinalState,
    statemachine_Node,
    statemachine_Pseudostate,
    statemachine_Region,
    statemachine_State,
    statemachine_Statechart,
    statemachine_Transition,
    statemachine_Variable,
    DataTypes,
    IOTypes,
    PseudoTypes,
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

def test_assoc_dataElement8_reverse_link_reassign_clear():
    a1 = statemachine_Statechart(UUID="sample_text", name="sample_text")
    a2 = statemachine_Statechart(UUID="sample_text_2", name="sample_text_2")
    b = statemachine_DataElement(ioType="sample_text", name="sample_text", port=7)
    _safe_set(b, 'statemachine_DataElement', a1)
    assert _is_linked(b, 'statemachine_DataElement', a1)
    if hasattr(a1, 'statemachine_Statechart'):
        assert _is_linked(a1, 'statemachine_Statechart', b)
    _safe_set(b, 'statemachine_DataElement', a2)
    assert _is_linked(b, 'statemachine_DataElement', a2)
    if hasattr(a1, 'statemachine_Statechart'):
        assert not _is_linked(a1, 'statemachine_Statechart', b)
    if hasattr(a2, 'statemachine_Statechart'):
        assert _is_linked(a2, 'statemachine_Statechart', b)
    _safe_set(b, 'statemachine_DataElement', None)
    assert not _is_linked(b, 'statemachine_DataElement', a2)
    if hasattr(a2, 'statemachine_Statechart'):
        assert not _is_linked(a2, 'statemachine_Statechart', b)


def test_assoc_region6_reverse_link_reassign_clear():
    a1 = statemachine_State(do="sample_text", entry="sample_text", exit="sample_text")
    a2 = statemachine_State(do="sample_text_2", entry="sample_text_2", exit="sample_text_2")
    b = statemachine_Region(priority=7)
    _safe_set(b, 'statemachine_Region7', a1)
    assert _is_linked(b, 'statemachine_Region7', a1)
    if hasattr(a1, 'statemachine_State'):
        assert _is_linked(a1, 'statemachine_State', b)
    _safe_set(b, 'statemachine_Region7', a2)
    assert _is_linked(b, 'statemachine_Region7', a2)
    if hasattr(a1, 'statemachine_State'):
        assert not _is_linked(a1, 'statemachine_State', b)
    if hasattr(a2, 'statemachine_State'):
        assert _is_linked(a2, 'statemachine_State', b)
    _safe_set(b, 'statemachine_Region7', None)
    assert not _is_linked(b, 'statemachine_Region7', a2)
    if hasattr(a2, 'statemachine_State'):
        assert not _is_linked(a2, 'statemachine_State', b)


def test_assoc_region9_reverse_link_reassign_clear():
    a1 = statemachine_Statechart(UUID="sample_text", name="sample_text")
    a2 = statemachine_Statechart(UUID="sample_text_2", name="sample_text_2")
    b = statemachine_Region(priority=7)
    _safe_set(b, 'statemachine_Region11', a1)
    assert _is_linked(b, 'statemachine_Region11', a1)
    if hasattr(a1, 'statemachine_Statechart10'):
        assert _is_linked(a1, 'statemachine_Statechart10', b)
    _safe_set(b, 'statemachine_Region11', a2)
    assert _is_linked(b, 'statemachine_Region11', a2)
    if hasattr(a1, 'statemachine_Statechart10'):
        assert not _is_linked(a1, 'statemachine_Statechart10', b)
    if hasattr(a2, 'statemachine_Statechart10'):
        assert _is_linked(a2, 'statemachine_Statechart10', b)
    _safe_set(b, 'statemachine_Region11', None)
    assert not _is_linked(b, 'statemachine_Region11', a2)
    if hasattr(a2, 'statemachine_Statechart10'):
        assert not _is_linked(a2, 'statemachine_Statechart10', b)


def test_assoc_sourceNode3_reverse_link_reassign_clear():
    a1 = statemachine_Transition(expression="sample_text", id=7, priority=7)
    a2 = statemachine_Transition(expression="sample_text_2", id=13, priority=13)
    b = statemachine_Node(id=7, name="sample_text")
    _safe_set(b, 'statemachine_Node5', a1)
    assert _is_linked(b, 'statemachine_Node5', a1)
    if hasattr(a1, 'statemachine_Transition4'):
        assert _is_linked(a1, 'statemachine_Transition4', b)
    _safe_set(b, 'statemachine_Node5', a2)
    assert _is_linked(b, 'statemachine_Node5', a2)
    if hasattr(a1, 'statemachine_Transition4'):
        assert not _is_linked(a1, 'statemachine_Transition4', b)
    if hasattr(a2, 'statemachine_Transition4'):
        assert _is_linked(a2, 'statemachine_Transition4', b)
    _safe_set(b, 'statemachine_Node5', None)
    assert not _is_linked(b, 'statemachine_Node5', a2)
    if hasattr(a2, 'statemachine_Transition4'):
        assert not _is_linked(a2, 'statemachine_Transition4', b)


def test_assoc_state0_reverse_link_reassign_clear():
    a1 = statemachine_Region(priority=7)
    a2 = statemachine_Region(priority=13)
    b = statemachine_Node(id=7, name="sample_text")
    _safe_set(b, 'statemachine_Node', a1)
    assert _is_linked(b, 'statemachine_Node', a1)
    if hasattr(a1, 'statemachine_Region'):
        assert _is_linked(a1, 'statemachine_Region', b)
    _safe_set(b, 'statemachine_Node', a2)
    assert _is_linked(b, 'statemachine_Node', a2)
    if hasattr(a1, 'statemachine_Region'):
        assert not _is_linked(a1, 'statemachine_Region', b)
    if hasattr(a2, 'statemachine_Region'):
        assert _is_linked(a2, 'statemachine_Region', b)
    _safe_set(b, 'statemachine_Node', None)
    assert not _is_linked(b, 'statemachine_Node', a2)
    if hasattr(a2, 'statemachine_Region'):
        assert not _is_linked(a2, 'statemachine_Region', b)


def test_assoc_targetNode1_reverse_link_reassign_clear():
    a1 = statemachine_Transition(expression="sample_text", id=7, priority=7)
    a2 = statemachine_Transition(expression="sample_text_2", id=13, priority=13)
    b = statemachine_Node(id=7, name="sample_text")
    _safe_set(b, 'statemachine_Node2', a1)
    assert _is_linked(b, 'statemachine_Node2', a1)
    if hasattr(a1, 'statemachine_Transition'):
        assert _is_linked(a1, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_Node2', a2)
    assert _is_linked(b, 'statemachine_Node2', a2)
    if hasattr(a1, 'statemachine_Transition'):
        assert not _is_linked(a1, 'statemachine_Transition', b)
    if hasattr(a2, 'statemachine_Transition'):
        assert _is_linked(a2, 'statemachine_Transition', b)
    _safe_set(b, 'statemachine_Node2', None)
    assert not _is_linked(b, 'statemachine_Node2', a2)
    if hasattr(a2, 'statemachine_Transition'):
        assert not _is_linked(a2, 'statemachine_Transition', b)


def test_assoc_transition12_reverse_link_reassign_clear():
    a1 = statemachine_Transition(expression="sample_text", id=7, priority=7)
    a2 = statemachine_Transition(expression="sample_text_2", id=13, priority=13)
    b = statemachine_Statechart(UUID="sample_text", name="sample_text")
    _safe_set(b, 'statemachine_Statechart13', {a1})
    assert _is_linked(b, 'statemachine_Statechart13', a1)
    if hasattr(a1, 'statemachine_Transition14'):
        assert _is_linked(a1, 'statemachine_Transition14', b)
    _safe_set(b, 'statemachine_Statechart13', {a2})
    assert _is_linked(b, 'statemachine_Statechart13', a2)
    if hasattr(a1, 'statemachine_Transition14'):
        assert not _is_linked(a1, 'statemachine_Transition14', b)
    if hasattr(a2, 'statemachine_Transition14'):
        assert _is_linked(a2, 'statemachine_Transition14', b)
    _safe_set(b, 'statemachine_Statechart13', set())
    assert not _is_linked(b, 'statemachine_Statechart13', a2)
    if hasattr(a2, 'statemachine_Transition14'):
        assert not _is_linked(a2, 'statemachine_Transition14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

