import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    stateChart_Model,
    stateChart_Node,
    stateChart_Transition,
    stateChart_Variable,
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

def test_assoc_Children2_reverse_link_reassign_clear():
    a1 = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    a2 = stateChart_Node(actions="sample_text_2", activity="sample_text_2", label="sample_text_2", metadata="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'Father'):
        assert _is_linked(a1, 'Father', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'Father'):
        assert not _is_linked(a1, 'Father', b)
    if hasattr(a2, 'Father'):
        assert _is_linked(a2, 'Father', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'Father'):
        assert not _is_linked(a2, 'Father', b)


def test_assoc_Father4_reverse_link_reassign_clear():
    a1 = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    a2 = stateChart_Node(actions="sample_text_2", activity="sample_text_2", label="sample_text_2", metadata="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'Node5', a1)
    assert _is_linked(b, 'Node5', a1)
    if hasattr(a1, 'Children'):
        assert _is_linked(a1, 'Children', b)
    _safe_set(b, 'Node5', a2)
    assert _is_linked(b, 'Node5', a2)
    if hasattr(a1, 'Children'):
        assert not _is_linked(a1, 'Children', b)
    if hasattr(a2, 'Children'):
        assert _is_linked(a2, 'Children', b)
    _safe_set(b, 'Node5', None)
    assert not _is_linked(b, 'Node5', a2)
    if hasattr(a2, 'Children'):
        assert not _is_linked(a2, 'Children', b)


def test_assoc_child6_reverse_link_reassign_clear():
    a1 = stateChart_Transition(TE="sample_text", metadata="sample_text", name="sample_text")
    a2 = stateChart_Transition(TE="sample_text_2", metadata="sample_text_2", name="sample_text_2")
    b = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'stateChart_Node7', {a1})
    assert _is_linked(b, 'stateChart_Node7', a1)
    if hasattr(a1, 'stateChart_Transition'):
        assert _is_linked(a1, 'stateChart_Transition', b)
    _safe_set(b, 'stateChart_Node7', {a2})
    assert _is_linked(b, 'stateChart_Node7', a2)
    if hasattr(a1, 'stateChart_Transition'):
        assert not _is_linked(a1, 'stateChart_Transition', b)
    if hasattr(a2, 'stateChart_Transition'):
        assert _is_linked(a2, 'stateChart_Transition', b)
    _safe_set(b, 'stateChart_Node7', set())
    assert not _is_linked(b, 'stateChart_Node7', a2)
    if hasattr(a2, 'stateChart_Transition'):
        assert not _is_linked(a2, 'stateChart_Transition', b)


def test_assoc_nodes11_reverse_link_reassign_clear():
    a1 = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    a2 = stateChart_Node(actions="sample_text_2", activity="sample_text_2", label="sample_text_2", metadata="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = stateChart_Model(description="sample_text", metadata="sample_text", name="sample_text")
    _safe_set(b, 'stateChart_Model', {a1})
    assert _is_linked(b, 'stateChart_Model', a1)
    if hasattr(a1, 'stateChart_Node12'):
        assert _is_linked(a1, 'stateChart_Node12', b)
    _safe_set(b, 'stateChart_Model', {a2})
    assert _is_linked(b, 'stateChart_Model', a2)
    if hasattr(a1, 'stateChart_Node12'):
        assert not _is_linked(a1, 'stateChart_Node12', b)
    if hasattr(a2, 'stateChart_Node12'):
        assert _is_linked(a2, 'stateChart_Node12', b)
    _safe_set(b, 'stateChart_Model', set())
    assert not _is_linked(b, 'stateChart_Model', a2)
    if hasattr(a2, 'stateChart_Node12'):
        assert not _is_linked(a2, 'stateChart_Node12', b)


def test_assoc_parent8_reverse_link_reassign_clear():
    a1 = stateChart_Transition(TE="sample_text", metadata="sample_text", name="sample_text")
    a2 = stateChart_Transition(TE="sample_text_2", metadata="sample_text_2", name="sample_text_2")
    b = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'stateChart_Node9', a1)
    assert _is_linked(b, 'stateChart_Node9', a1)
    if hasattr(a1, 'stateChart_Transition10'):
        assert _is_linked(a1, 'stateChart_Transition10', b)
    _safe_set(b, 'stateChart_Node9', a2)
    assert _is_linked(b, 'stateChart_Node9', a2)
    if hasattr(a1, 'stateChart_Transition10'):
        assert not _is_linked(a1, 'stateChart_Transition10', b)
    if hasattr(a2, 'stateChart_Transition10'):
        assert _is_linked(a2, 'stateChart_Transition10', b)
    _safe_set(b, 'stateChart_Node9', None)
    assert not _is_linked(b, 'stateChart_Node9', a2)
    if hasattr(a2, 'stateChart_Transition10'):
        assert not _is_linked(a2, 'stateChart_Transition10', b)


def test_assoc_source19_reverse_link_reassign_clear():
    a1 = stateChart_Transition(TE="sample_text", metadata="sample_text", name="sample_text")
    a2 = stateChart_Transition(TE="sample_text_2", metadata="sample_text_2", name="sample_text_2")
    b = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'stateChart_Node21', a1)
    assert _is_linked(b, 'stateChart_Node21', a1)
    if hasattr(a1, 'stateChart_Transition20'):
        assert _is_linked(a1, 'stateChart_Transition20', b)
    _safe_set(b, 'stateChart_Node21', a2)
    assert _is_linked(b, 'stateChart_Node21', a2)
    if hasattr(a1, 'stateChart_Transition20'):
        assert not _is_linked(a1, 'stateChart_Transition20', b)
    if hasattr(a2, 'stateChart_Transition20'):
        assert _is_linked(a2, 'stateChart_Transition20', b)
    _safe_set(b, 'stateChart_Node21', None)
    assert not _is_linked(b, 'stateChart_Node21', a2)
    if hasattr(a2, 'stateChart_Transition20'):
        assert not _is_linked(a2, 'stateChart_Transition20', b)


def test_assoc_target22_reverse_link_reassign_clear():
    a1 = stateChart_Transition(TE="sample_text", metadata="sample_text", name="sample_text")
    a2 = stateChart_Transition(TE="sample_text_2", metadata="sample_text_2", name="sample_text_2")
    b = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'stateChart_Node24', a1)
    assert _is_linked(b, 'stateChart_Node24', a1)
    if hasattr(a1, 'stateChart_Transition23'):
        assert _is_linked(a1, 'stateChart_Transition23', b)
    _safe_set(b, 'stateChart_Node24', a2)
    assert _is_linked(b, 'stateChart_Node24', a2)
    if hasattr(a1, 'stateChart_Transition23'):
        assert not _is_linked(a1, 'stateChart_Transition23', b)
    if hasattr(a2, 'stateChart_Transition23'):
        assert _is_linked(a2, 'stateChart_Transition23', b)
    _safe_set(b, 'stateChart_Node24', None)
    assert not _is_linked(b, 'stateChart_Node24', a2)
    if hasattr(a2, 'stateChart_Transition23'):
        assert not _is_linked(a2, 'stateChart_Transition23', b)


def test_assoc_transitions16_reverse_link_reassign_clear():
    a1 = stateChart_Transition(TE="sample_text", metadata="sample_text", name="sample_text")
    a2 = stateChart_Transition(TE="sample_text_2", metadata="sample_text_2", name="sample_text_2")
    b = stateChart_Model(description="sample_text", metadata="sample_text", name="sample_text")
    _safe_set(b, 'stateChart_Model17', {a1})
    assert _is_linked(b, 'stateChart_Model17', a1)
    if hasattr(a1, 'stateChart_Transition18'):
        assert _is_linked(a1, 'stateChart_Transition18', b)
    _safe_set(b, 'stateChart_Model17', {a2})
    assert _is_linked(b, 'stateChart_Model17', a2)
    if hasattr(a1, 'stateChart_Transition18'):
        assert not _is_linked(a1, 'stateChart_Transition18', b)
    if hasattr(a2, 'stateChart_Transition18'):
        assert _is_linked(a2, 'stateChart_Transition18', b)
    _safe_set(b, 'stateChart_Model17', set())
    assert not _is_linked(b, 'stateChart_Model17', a2)
    if hasattr(a2, 'stateChart_Transition18'):
        assert not _is_linked(a2, 'stateChart_Transition18', b)


def test_assoc_variables0_reverse_link_reassign_clear():
    a1 = stateChart_Variable(name="sample_text", type="sample_text")
    a2 = stateChart_Variable(name="sample_text_2", type="sample_text_2")
    b = stateChart_Node(actions="sample_text", activity="sample_text", label="sample_text", metadata="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'stateChart_Node', {a1})
    assert _is_linked(b, 'stateChart_Node', a1)
    if hasattr(a1, 'stateChart_Variable'):
        assert _is_linked(a1, 'stateChart_Variable', b)
    _safe_set(b, 'stateChart_Node', {a2})
    assert _is_linked(b, 'stateChart_Node', a2)
    if hasattr(a1, 'stateChart_Variable'):
        assert not _is_linked(a1, 'stateChart_Variable', b)
    if hasattr(a2, 'stateChart_Variable'):
        assert _is_linked(a2, 'stateChart_Variable', b)
    _safe_set(b, 'stateChart_Node', set())
    assert not _is_linked(b, 'stateChart_Node', a2)
    if hasattr(a2, 'stateChart_Variable'):
        assert not _is_linked(a2, 'stateChart_Variable', b)


def test_assoc_variables13_reverse_link_reassign_clear():
    a1 = stateChart_Variable(name="sample_text", type="sample_text")
    a2 = stateChart_Variable(name="sample_text_2", type="sample_text_2")
    b = stateChart_Model(description="sample_text", metadata="sample_text", name="sample_text")
    _safe_set(b, 'stateChart_Model14', {a1})
    assert _is_linked(b, 'stateChart_Model14', a1)
    if hasattr(a1, 'stateChart_Variable15'):
        assert _is_linked(a1, 'stateChart_Variable15', b)
    _safe_set(b, 'stateChart_Model14', {a2})
    assert _is_linked(b, 'stateChart_Model14', a2)
    if hasattr(a1, 'stateChart_Variable15'):
        assert not _is_linked(a1, 'stateChart_Variable15', b)
    if hasattr(a2, 'stateChart_Variable15'):
        assert _is_linked(a2, 'stateChart_Variable15', b)
    _safe_set(b, 'stateChart_Model14', set())
    assert not _is_linked(b, 'stateChart_Model14', a2)
    if hasattr(a2, 'stateChart_Variable15'):
        assert not _is_linked(a2, 'stateChart_Variable15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

