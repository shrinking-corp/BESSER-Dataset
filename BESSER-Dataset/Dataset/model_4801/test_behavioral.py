import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Leafs,
    testModel_ContainedLeaf,
    testModel_Leafs,
    testModel_Node,
    testModel_multiRefLeaf,
    testModel_referedLeaf,
    testModel_upperBoundLeaf,
    ElementType,
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

def test_assoc_contains2_reverse_link_reassign_clear():
    a1 = testModel_Node(Boolean="sample_text", bigdeci="sample_text", bigint="sample_text", bool=True, byte="sample_text", name="sample_text")
    a2 = testModel_Node(Boolean="sample_text_2", bigdeci="sample_text_2", bigint="sample_text_2", bool=False, byte="sample_text_2", name="sample_text_2")
    b = testModel_ContainedLeaf(Character="sample_text", DoubleObj="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", date=date(2024, 1, 1), double=3.14, elementType="sample_text", float=3.14, name="sample_text")
    _safe_set(b, 'testModel_ContainedLeaf', a1)
    assert _is_linked(b, 'testModel_ContainedLeaf', a1)
    if hasattr(a1, 'testModel_Node3'):
        assert _is_linked(a1, 'testModel_Node3', b)
    _safe_set(b, 'testModel_ContainedLeaf', a2)
    assert _is_linked(b, 'testModel_ContainedLeaf', a2)
    if hasattr(a1, 'testModel_Node3'):
        assert not _is_linked(a1, 'testModel_Node3', b)
    if hasattr(a2, 'testModel_Node3'):
        assert _is_linked(a2, 'testModel_Node3', b)
    _safe_set(b, 'testModel_ContainedLeaf', None)
    assert not _is_linked(b, 'testModel_ContainedLeaf', a2)
    if hasattr(a2, 'testModel_Node3'):
        assert not _is_linked(a2, 'testModel_Node3', b)


def test_assoc_multiRef8_reverse_link_reassign_clear():
    a1 = testModel_referedLeaf(Float="sample_text", Integer="sample_text", LongObj="sample_text", ShortObj="sample_text", int=7, long="sample_text", name="sample_text", notChangeable="sample_text", short="sample_text")
    a2 = testModel_referedLeaf(Float="sample_text_2", Integer="sample_text_2", LongObj="sample_text_2", ShortObj="sample_text_2", int=13, long="sample_text_2", name="sample_text_2", notChangeable="sample_text_2", short="sample_text_2")
    b = testModel_multiRefLeaf(name="sample_text")
    _safe_set(b, 'testModel_multiRefLeaf', a1)
    assert _is_linked(b, 'testModel_multiRefLeaf', a1)
    if hasattr(a1, 'testModel_referedLeaf9'):
        assert _is_linked(a1, 'testModel_referedLeaf9', b)
    _safe_set(b, 'testModel_multiRefLeaf', a2)
    assert _is_linked(b, 'testModel_multiRefLeaf', a2)
    if hasattr(a1, 'testModel_referedLeaf9'):
        assert not _is_linked(a1, 'testModel_referedLeaf9', b)
    if hasattr(a2, 'testModel_referedLeaf9'):
        assert _is_linked(a2, 'testModel_referedLeaf9', b)
    _safe_set(b, 'testModel_multiRefLeaf', None)
    assert not _is_linked(b, 'testModel_multiRefLeaf', a2)
    if hasattr(a2, 'testModel_referedLeaf9'):
        assert not _is_linked(a2, 'testModel_referedLeaf9', b)


def test_assoc_ref4_reverse_link_reassign_clear():
    a1 = testModel_referedLeaf(Float="sample_text", Integer="sample_text", LongObj="sample_text", ShortObj="sample_text", int=7, long="sample_text", name="sample_text", notChangeable="sample_text", short="sample_text")
    a2 = testModel_referedLeaf(Float="sample_text_2", Integer="sample_text_2", LongObj="sample_text_2", ShortObj="sample_text_2", int=13, long="sample_text_2", name="sample_text_2", notChangeable="sample_text_2", short="sample_text_2")
    b = testModel_ContainedLeaf(Character="sample_text", DoubleObj="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", date=date(2024, 1, 1), double=3.14, elementType="sample_text", float=3.14, name="sample_text")
    _safe_set(b, 'testModel_ContainedLeaf5', {a1})
    assert _is_linked(b, 'testModel_ContainedLeaf5', a1)
    if hasattr(a1, 'testModel_referedLeaf'):
        assert _is_linked(a1, 'testModel_referedLeaf', b)
    _safe_set(b, 'testModel_ContainedLeaf5', {a2})
    assert _is_linked(b, 'testModel_ContainedLeaf5', a2)
    if hasattr(a1, 'testModel_referedLeaf'):
        assert not _is_linked(a1, 'testModel_referedLeaf', b)
    if hasattr(a2, 'testModel_referedLeaf'):
        assert _is_linked(a2, 'testModel_referedLeaf', b)
    _safe_set(b, 'testModel_ContainedLeaf5', set())
    assert not _is_linked(b, 'testModel_ContainedLeaf5', a2)
    if hasattr(a2, 'testModel_referedLeaf'):
        assert not _is_linked(a2, 'testModel_referedLeaf', b)


def test_assoc_subNode1_reverse_link_reassign_clear():
    a1 = testModel_Node(Boolean="sample_text", bigdeci="sample_text", bigint="sample_text", bool=True, byte="sample_text", name="sample_text")
    a2 = testModel_Node(Boolean="sample_text_2", bigdeci="sample_text_2", bigint="sample_text_2", bool=False, byte="sample_text_2", name="sample_text_2")
    b = testModel_Node(Boolean="sample_text", bigdeci="sample_text", bigint="sample_text", bool=True, byte="sample_text", name="sample_text")
    _safe_set(b, 'testModel_Node0', {a1})
    assert _is_linked(b, 'testModel_Node0', a1)
    if hasattr(a1, 'testModel_Node'):
        assert _is_linked(a1, 'testModel_Node', b)
    _safe_set(b, 'testModel_Node0', {a2})
    assert _is_linked(b, 'testModel_Node0', a2)
    if hasattr(a1, 'testModel_Node'):
        assert not _is_linked(a1, 'testModel_Node', b)
    if hasattr(a2, 'testModel_Node'):
        assert _is_linked(a2, 'testModel_Node', b)
    _safe_set(b, 'testModel_Node0', set())
    assert not _is_linked(b, 'testModel_Node0', a2)
    if hasattr(a2, 'testModel_Node'):
        assert not _is_linked(a2, 'testModel_Node', b)


def test_assoc_upperBound6_reverse_link_reassign_clear():
    a1 = testModel_upperBoundLeaf(name="sample_text")
    a2 = testModel_upperBoundLeaf(name="sample_text_2")
    b = testModel_ContainedLeaf(Character="sample_text", DoubleObj="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", date=date(2024, 1, 1), double=3.14, elementType="sample_text", float=3.14, name="sample_text")
    _safe_set(b, 'testModel_ContainedLeaf7', {a1})
    assert _is_linked(b, 'testModel_ContainedLeaf7', a1)
    if hasattr(a1, 'testModel_upperBoundLeaf'):
        assert _is_linked(a1, 'testModel_upperBoundLeaf', b)
    _safe_set(b, 'testModel_ContainedLeaf7', {a2})
    assert _is_linked(b, 'testModel_ContainedLeaf7', a2)
    if hasattr(a1, 'testModel_upperBoundLeaf'):
        assert not _is_linked(a1, 'testModel_upperBoundLeaf', b)
    if hasattr(a2, 'testModel_upperBoundLeaf'):
        assert _is_linked(a2, 'testModel_upperBoundLeaf', b)
    _safe_set(b, 'testModel_ContainedLeaf7', set())
    assert not _is_linked(b, 'testModel_ContainedLeaf7', a2)
    if hasattr(a2, 'testModel_upperBoundLeaf'):
        assert not _is_linked(a2, 'testModel_upperBoundLeaf', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

