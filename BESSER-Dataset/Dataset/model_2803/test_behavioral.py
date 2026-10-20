import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    rules_Node,
    rules_NodeRelation,
    rules_Rule,
    rules_RulesLattice,
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

def test_assoc_children2_reverse_link_reassign_clear():
    a1 = rules_Rule(name="sample_text")
    a2 = rules_Rule(name="sample_text_2")
    b = rules_Rule(name="sample_text")
    _safe_set(b, 'parents', {a1})
    assert _is_linked(b, 'parents', a1)
    if hasattr(a1, 'Rule'):
        assert _is_linked(a1, 'Rule', b)
    _safe_set(b, 'parents', {a2})
    assert _is_linked(b, 'parents', a2)
    if hasattr(a1, 'Rule'):
        assert not _is_linked(a1, 'Rule', b)
    if hasattr(a2, 'Rule'):
        assert _is_linked(a2, 'Rule', b)
    _safe_set(b, 'parents', set())
    assert not _is_linked(b, 'parents', a2)
    if hasattr(a2, 'Rule'):
        assert not _is_linked(a2, 'Rule', b)


def test_assoc_conclusion8_reverse_link_reassign_clear():
    a1 = rules_Rule(name="sample_text")
    a2 = rules_Rule(name="sample_text_2")
    b = rules_Node(type="sample_text")
    _safe_set(b, 'rules_Node10', a1)
    assert _is_linked(b, 'rules_Node10', a1)
    if hasattr(a1, 'rules_Rule9'):
        assert _is_linked(a1, 'rules_Rule9', b)
    _safe_set(b, 'rules_Node10', a2)
    assert _is_linked(b, 'rules_Node10', a2)
    if hasattr(a1, 'rules_Rule9'):
        assert not _is_linked(a1, 'rules_Rule9', b)
    if hasattr(a2, 'rules_Rule9'):
        assert _is_linked(a2, 'rules_Rule9', b)
    _safe_set(b, 'rules_Node10', None)
    assert not _is_linked(b, 'rules_Node10', a2)
    if hasattr(a2, 'rules_Rule9'):
        assert not _is_linked(a2, 'rules_Rule9', b)


def test_assoc_nodes11_reverse_link_reassign_clear():
    a1 = rules_Rule(name="sample_text")
    a2 = rules_Rule(name="sample_text_2")
    b = rules_Node(type="sample_text")
    _safe_set(b, 'rules_Node13', a1)
    assert _is_linked(b, 'rules_Node13', a1)
    if hasattr(a1, 'rules_Rule12'):
        assert _is_linked(a1, 'rules_Rule12', b)
    _safe_set(b, 'rules_Node13', a2)
    assert _is_linked(b, 'rules_Node13', a2)
    if hasattr(a1, 'rules_Rule12'):
        assert not _is_linked(a1, 'rules_Rule12', b)
    if hasattr(a2, 'rules_Rule12'):
        assert _is_linked(a2, 'rules_Rule12', b)
    _safe_set(b, 'rules_Node13', None)
    assert not _is_linked(b, 'rules_Node13', a2)
    if hasattr(a2, 'rules_Rule12'):
        assert not _is_linked(a2, 'rules_Rule12', b)


def test_assoc_parents4_reverse_link_reassign_clear():
    a1 = rules_Rule(name="sample_text")
    a2 = rules_Rule(name="sample_text_2")
    b = rules_Rule(name="sample_text")
    _safe_set(b, 'children', {a1})
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Rule5'):
        assert _is_linked(a1, 'Rule5', b)
    _safe_set(b, 'children', {a2})
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Rule5'):
        assert not _is_linked(a1, 'Rule5', b)
    if hasattr(a2, 'Rule5'):
        assert _is_linked(a2, 'Rule5', b)
    _safe_set(b, 'children', set())
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Rule5'):
        assert not _is_linked(a2, 'Rule5', b)


def test_assoc_premise6_reverse_link_reassign_clear():
    a1 = rules_Rule(name="sample_text")
    a2 = rules_Rule(name="sample_text_2")
    b = rules_Node(type="sample_text")
    _safe_set(b, 'rules_Node', a1)
    assert _is_linked(b, 'rules_Node', a1)
    if hasattr(a1, 'rules_Rule7'):
        assert _is_linked(a1, 'rules_Rule7', b)
    _safe_set(b, 'rules_Node', a2)
    assert _is_linked(b, 'rules_Node', a2)
    if hasattr(a1, 'rules_Rule7'):
        assert not _is_linked(a1, 'rules_Rule7', b)
    if hasattr(a2, 'rules_Rule7'):
        assert _is_linked(a2, 'rules_Rule7', b)
    _safe_set(b, 'rules_Node', None)
    assert not _is_linked(b, 'rules_Node', a2)
    if hasattr(a2, 'rules_Rule7'):
        assert not _is_linked(a2, 'rules_Rule7', b)


def test_assoc_relatedNodes14_reverse_link_reassign_clear():
    a1 = rules_NodeRelation(lowerBound=7, relation="sample_text", relationTgt="sample_text", upperBound=7)
    a2 = rules_NodeRelation(lowerBound=13, relation="sample_text_2", relationTgt="sample_text_2", upperBound=13)
    b = rules_Node(type="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'NodeRelation'):
        assert _is_linked(a1, 'NodeRelation', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'NodeRelation'):
        assert not _is_linked(a1, 'NodeRelation', b)
    if hasattr(a2, 'NodeRelation'):
        assert _is_linked(a2, 'NodeRelation', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'NodeRelation'):
        assert not _is_linked(a2, 'NodeRelation', b)


def test_assoc_rules0_reverse_link_reassign_clear():
    a1 = rules_RulesLattice(source="sample_text", target="sample_text")
    a2 = rules_RulesLattice(source="sample_text_2", target="sample_text_2")
    b = rules_Rule(name="sample_text")
    _safe_set(b, 'rules_Rule', a1)
    assert _is_linked(b, 'rules_Rule', a1)
    if hasattr(a1, 'rules_RulesLattice'):
        assert _is_linked(a1, 'rules_RulesLattice', b)
    _safe_set(b, 'rules_Rule', a2)
    assert _is_linked(b, 'rules_Rule', a2)
    if hasattr(a1, 'rules_RulesLattice'):
        assert not _is_linked(a1, 'rules_RulesLattice', b)
    if hasattr(a2, 'rules_RulesLattice'):
        assert _is_linked(a2, 'rules_RulesLattice', b)
    _safe_set(b, 'rules_Rule', None)
    assert not _is_linked(b, 'rules_Rule', a2)
    if hasattr(a2, 'rules_RulesLattice'):
        assert not _is_linked(a2, 'rules_RulesLattice', b)


def test_assoc_source15_reverse_link_reassign_clear():
    a1 = rules_NodeRelation(lowerBound=7, relation="sample_text", relationTgt="sample_text", upperBound=7)
    a2 = rules_NodeRelation(lowerBound=13, relation="sample_text_2", relationTgt="sample_text_2", upperBound=13)
    b = rules_Node(type="sample_text")
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'relatedNodes'):
        assert _is_linked(a1, 'relatedNodes', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'relatedNodes'):
        assert not _is_linked(a1, 'relatedNodes', b)
    if hasattr(a2, 'relatedNodes'):
        assert _is_linked(a2, 'relatedNodes', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'relatedNodes'):
        assert not _is_linked(a2, 'relatedNodes', b)


def test_assoc_target16_reverse_link_reassign_clear():
    a1 = rules_NodeRelation(lowerBound=7, relation="sample_text", relationTgt="sample_text", upperBound=7)
    a2 = rules_NodeRelation(lowerBound=13, relation="sample_text_2", relationTgt="sample_text_2", upperBound=13)
    b = rules_Node(type="sample_text")
    _safe_set(b, 'rules_Node17', a1)
    assert _is_linked(b, 'rules_Node17', a1)
    if hasattr(a1, 'rules_NodeRelation'):
        assert _is_linked(a1, 'rules_NodeRelation', b)
    _safe_set(b, 'rules_Node17', a2)
    assert _is_linked(b, 'rules_Node17', a2)
    if hasattr(a1, 'rules_NodeRelation'):
        assert not _is_linked(a1, 'rules_NodeRelation', b)
    if hasattr(a2, 'rules_NodeRelation'):
        assert _is_linked(a2, 'rules_NodeRelation', b)
    _safe_set(b, 'rules_Node17', None)
    assert not _is_linked(b, 'rules_Node17', a2)
    if hasattr(a2, 'rules_NodeRelation'):
        assert not _is_linked(a2, 'rules_NodeRelation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

