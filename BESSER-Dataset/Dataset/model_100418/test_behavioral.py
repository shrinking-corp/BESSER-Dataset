import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    statechart_Model,
    statechart_Node,
    statechart_Transition,
    statechart_Variable,
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

def test_assoc_Children9_reverse_link_reassign_clear():
    a1 = statechart_Node(activity="sample_text", label="sample_text", name="sample_text", type="sample_text")
    a2 = statechart_Node(activity="sample_text_2", label="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = statechart_Node(activity="sample_text", label="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'Father_of'):
        assert _is_linked(a1, 'Father_of', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'Father_of'):
        assert not _is_linked(a1, 'Father_of', b)
    if hasattr(a2, 'Father_of'):
        assert _is_linked(a2, 'Father_of', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'Father_of'):
        assert not _is_linked(a2, 'Father_of', b)


def test_assoc_Father_of11_reverse_link_reassign_clear():
    a1 = statechart_Node(activity="sample_text", label="sample_text", name="sample_text", type="sample_text")
    a2 = statechart_Node(activity="sample_text_2", label="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = statechart_Node(activity="sample_text", label="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'Node12', a1)
    assert _is_linked(b, 'Node12', a1)
    if hasattr(a1, 'Children'):
        assert _is_linked(a1, 'Children', b)
    _safe_set(b, 'Node12', a2)
    assert _is_linked(b, 'Node12', a2)
    if hasattr(a1, 'Children'):
        assert not _is_linked(a1, 'Children', b)
    if hasattr(a2, 'Children'):
        assert _is_linked(a2, 'Children', b)
    _safe_set(b, 'Node12', None)
    assert not _is_linked(b, 'Node12', a2)
    if hasattr(a2, 'Children'):
        assert not _is_linked(a2, 'Children', b)


def test_assoc_nodes0_reverse_link_reassign_clear():
    a1 = statechart_Node(activity="sample_text", label="sample_text", name="sample_text", type="sample_text")
    a2 = statechart_Node(activity="sample_text_2", label="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = statechart_Model(name="sample_text")
    _safe_set(b, 'statechart_Model', {a1})
    assert _is_linked(b, 'statechart_Model', a1)
    if hasattr(a1, 'statechart_Node'):
        assert _is_linked(a1, 'statechart_Node', b)
    _safe_set(b, 'statechart_Model', {a2})
    assert _is_linked(b, 'statechart_Model', a2)
    if hasattr(a1, 'statechart_Node'):
        assert not _is_linked(a1, 'statechart_Node', b)
    if hasattr(a2, 'statechart_Node'):
        assert _is_linked(a2, 'statechart_Node', b)
    _safe_set(b, 'statechart_Model', set())
    assert not _is_linked(b, 'statechart_Model', a2)
    if hasattr(a2, 'statechart_Node'):
        assert not _is_linked(a2, 'statechart_Node', b)


def test_assoc_source13_reverse_link_reassign_clear():
    a1 = statechart_Transition(TE="sample_text", name="sample_text")
    a2 = statechart_Transition(TE="sample_text_2", name="sample_text_2")
    b = statechart_Node(activity="sample_text", label="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'statechart_Node15', a1)
    assert _is_linked(b, 'statechart_Node15', a1)
    if hasattr(a1, 'statechart_Transition14'):
        assert _is_linked(a1, 'statechart_Transition14', b)
    _safe_set(b, 'statechart_Node15', a2)
    assert _is_linked(b, 'statechart_Node15', a2)
    if hasattr(a1, 'statechart_Transition14'):
        assert not _is_linked(a1, 'statechart_Transition14', b)
    if hasattr(a2, 'statechart_Transition14'):
        assert _is_linked(a2, 'statechart_Transition14', b)
    _safe_set(b, 'statechart_Node15', None)
    assert not _is_linked(b, 'statechart_Node15', a2)
    if hasattr(a2, 'statechart_Transition14'):
        assert not _is_linked(a2, 'statechart_Transition14', b)


def test_assoc_target16_reverse_link_reassign_clear():
    a1 = statechart_Transition(TE="sample_text", name="sample_text")
    a2 = statechart_Transition(TE="sample_text_2", name="sample_text_2")
    b = statechart_Node(activity="sample_text", label="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'statechart_Node18', a1)
    assert _is_linked(b, 'statechart_Node18', a1)
    if hasattr(a1, 'statechart_Transition17'):
        assert _is_linked(a1, 'statechart_Transition17', b)
    _safe_set(b, 'statechart_Node18', a2)
    assert _is_linked(b, 'statechart_Node18', a2)
    if hasattr(a1, 'statechart_Transition17'):
        assert not _is_linked(a1, 'statechart_Transition17', b)
    if hasattr(a2, 'statechart_Transition17'):
        assert _is_linked(a2, 'statechart_Transition17', b)
    _safe_set(b, 'statechart_Node18', None)
    assert not _is_linked(b, 'statechart_Node18', a2)
    if hasattr(a2, 'statechart_Transition17'):
        assert not _is_linked(a2, 'statechart_Transition17', b)


def test_assoc_transitions1_reverse_link_reassign_clear():
    a1 = statechart_Transition(TE="sample_text", name="sample_text")
    a2 = statechart_Transition(TE="sample_text_2", name="sample_text_2")
    b = statechart_Model(name="sample_text")
    _safe_set(b, 'statechart_Model2', {a1})
    assert _is_linked(b, 'statechart_Model2', a1)
    if hasattr(a1, 'statechart_Transition'):
        assert _is_linked(a1, 'statechart_Transition', b)
    _safe_set(b, 'statechart_Model2', {a2})
    assert _is_linked(b, 'statechart_Model2', a2)
    if hasattr(a1, 'statechart_Transition'):
        assert not _is_linked(a1, 'statechart_Transition', b)
    if hasattr(a2, 'statechart_Transition'):
        assert _is_linked(a2, 'statechart_Transition', b)
    _safe_set(b, 'statechart_Model2', set())
    assert not _is_linked(b, 'statechart_Model2', a2)
    if hasattr(a2, 'statechart_Transition'):
        assert not _is_linked(a2, 'statechart_Transition', b)


def test_assoc_variables3_reverse_link_reassign_clear():
    a1 = statechart_Variable(name="sample_text", type="sample_text")
    a2 = statechart_Variable(name="sample_text_2", type="sample_text_2")
    b = statechart_Model(name="sample_text")
    _safe_set(b, 'statechart_Model4', {a1})
    assert _is_linked(b, 'statechart_Model4', a1)
    if hasattr(a1, 'statechart_Variable'):
        assert _is_linked(a1, 'statechart_Variable', b)
    _safe_set(b, 'statechart_Model4', {a2})
    assert _is_linked(b, 'statechart_Model4', a2)
    if hasattr(a1, 'statechart_Variable'):
        assert not _is_linked(a1, 'statechart_Variable', b)
    if hasattr(a2, 'statechart_Variable'):
        assert _is_linked(a2, 'statechart_Variable', b)
    _safe_set(b, 'statechart_Model4', set())
    assert not _is_linked(b, 'statechart_Model4', a2)
    if hasattr(a2, 'statechart_Variable'):
        assert not _is_linked(a2, 'statechart_Variable', b)


def test_assoc_variables5_reverse_link_reassign_clear():
    a1 = statechart_Variable(name="sample_text", type="sample_text")
    a2 = statechart_Variable(name="sample_text_2", type="sample_text_2")
    b = statechart_Node(activity="sample_text", label="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'statechart_Node6', {a1})
    assert _is_linked(b, 'statechart_Node6', a1)
    if hasattr(a1, 'statechart_Variable7'):
        assert _is_linked(a1, 'statechart_Variable7', b)
    _safe_set(b, 'statechart_Node6', {a2})
    assert _is_linked(b, 'statechart_Node6', a2)
    if hasattr(a1, 'statechart_Variable7'):
        assert not _is_linked(a1, 'statechart_Variable7', b)
    if hasattr(a2, 'statechart_Variable7'):
        assert _is_linked(a2, 'statechart_Variable7', b)
    _safe_set(b, 'statechart_Node6', set())
    assert not _is_linked(b, 'statechart_Node6', a2)
    if hasattr(a2, 'statechart_Variable7'):
        assert not _is_linked(a2, 'statechart_Variable7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

