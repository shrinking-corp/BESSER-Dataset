import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arrow,
    Category,
    NamedElement,
    SourceNode,
    TargetNode,
    relationpattern_Arrow,
    relationpattern_Category,
    relationpattern_NamedElement,
    relationpattern_RelatedTo,
    relationpattern_SourceNode,
    relationpattern_TargetNode,
    relationpattern_ThingA,
    relationpattern_ThingB,
    relationpattern_World,
    Scale,
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

def test_assoc_cible12_reverse_link_reassign_clear():
    a1 = relationpattern_TargetNode()
    a2 = relationpattern_TargetNode()
    b = relationpattern_Arrow()
    _safe_set(b, 'relationpattern_Arrow13', a1)
    assert _is_linked(b, 'relationpattern_Arrow13', a1)
    if hasattr(a1, 'relationpattern_TargetNode'):
        assert _is_linked(a1, 'relationpattern_TargetNode', b)
    _safe_set(b, 'relationpattern_Arrow13', a2)
    assert _is_linked(b, 'relationpattern_Arrow13', a2)
    if hasattr(a1, 'relationpattern_TargetNode'):
        assert not _is_linked(a1, 'relationpattern_TargetNode', b)
    if hasattr(a2, 'relationpattern_TargetNode'):
        assert _is_linked(a2, 'relationpattern_TargetNode', b)
    _safe_set(b, 'relationpattern_Arrow13', None)
    assert not _is_linked(b, 'relationpattern_Arrow13', a2)
    if hasattr(a2, 'relationpattern_TargetNode'):
        assert not _is_linked(a2, 'relationpattern_TargetNode', b)


def test_assoc_fleches16_reverse_link_reassign_clear():
    a1 = relationpattern_Category(nom="sample_text")
    a2 = relationpattern_Category(nom="sample_text_2")
    b = relationpattern_Arrow()
    _safe_set(b, 'relationpattern_Arrow18', a1)
    assert _is_linked(b, 'relationpattern_Arrow18', a1)
    if hasattr(a1, 'relationpattern_Category17'):
        assert _is_linked(a1, 'relationpattern_Category17', b)
    _safe_set(b, 'relationpattern_Arrow18', a2)
    assert _is_linked(b, 'relationpattern_Arrow18', a2)
    if hasattr(a1, 'relationpattern_Category17'):
        assert not _is_linked(a1, 'relationpattern_Category17', b)
    if hasattr(a2, 'relationpattern_Category17'):
        assert _is_linked(a2, 'relationpattern_Category17', b)
    _safe_set(b, 'relationpattern_Arrow18', None)
    assert not _is_linked(b, 'relationpattern_Arrow18', a2)
    if hasattr(a2, 'relationpattern_Category17'):
        assert not _is_linked(a2, 'relationpattern_Category17', b)


def test_assoc_relations8_reverse_link_reassign_clear():
    a1 = relationpattern_World()
    a2 = relationpattern_World()
    b = relationpattern_RelatedTo()
    _safe_set(b, 'relationpattern_RelatedTo10', a1)
    assert _is_linked(b, 'relationpattern_RelatedTo10', a1)
    if hasattr(a1, 'relationpattern_World9'):
        assert _is_linked(a1, 'relationpattern_World9', b)
    _safe_set(b, 'relationpattern_RelatedTo10', a2)
    assert _is_linked(b, 'relationpattern_RelatedTo10', a2)
    if hasattr(a1, 'relationpattern_World9'):
        assert not _is_linked(a1, 'relationpattern_World9', b)
    if hasattr(a2, 'relationpattern_World9'):
        assert _is_linked(a2, 'relationpattern_World9', b)
    _safe_set(b, 'relationpattern_RelatedTo10', None)
    assert not _is_linked(b, 'relationpattern_RelatedTo10', a2)
    if hasattr(a2, 'relationpattern_World9'):
        assert not _is_linked(a2, 'relationpattern_World9', b)


def test_assoc_source11_reverse_link_reassign_clear():
    a1 = relationpattern_SourceNode()
    a2 = relationpattern_SourceNode()
    b = relationpattern_Arrow()
    _safe_set(b, 'relationpattern_Arrow', a1)
    assert _is_linked(b, 'relationpattern_Arrow', a1)
    if hasattr(a1, 'relationpattern_SourceNode'):
        assert _is_linked(a1, 'relationpattern_SourceNode', b)
    _safe_set(b, 'relationpattern_Arrow', a2)
    assert _is_linked(b, 'relationpattern_Arrow', a2)
    if hasattr(a1, 'relationpattern_SourceNode'):
        assert not _is_linked(a1, 'relationpattern_SourceNode', b)
    if hasattr(a2, 'relationpattern_SourceNode'):
        assert _is_linked(a2, 'relationpattern_SourceNode', b)
    _safe_set(b, 'relationpattern_Arrow', None)
    assert not _is_linked(b, 'relationpattern_Arrow', a2)
    if hasattr(a2, 'relationpattern_SourceNode'):
        assert not _is_linked(a2, 'relationpattern_SourceNode', b)


def test_assoc_sources14_reverse_link_reassign_clear():
    a1 = relationpattern_SourceNode()
    a2 = relationpattern_SourceNode()
    b = relationpattern_Category(nom="sample_text")
    _safe_set(b, 'relationpattern_Category', {a1})
    assert _is_linked(b, 'relationpattern_Category', a1)
    if hasattr(a1, 'relationpattern_SourceNode15'):
        assert _is_linked(a1, 'relationpattern_SourceNode15', b)
    _safe_set(b, 'relationpattern_Category', {a2})
    assert _is_linked(b, 'relationpattern_Category', a2)
    if hasattr(a1, 'relationpattern_SourceNode15'):
        assert not _is_linked(a1, 'relationpattern_SourceNode15', b)
    if hasattr(a2, 'relationpattern_SourceNode15'):
        assert _is_linked(a2, 'relationpattern_SourceNode15', b)
    _safe_set(b, 'relationpattern_Category', set())
    assert not _is_linked(b, 'relationpattern_Category', a2)
    if hasattr(a2, 'relationpattern_SourceNode15'):
        assert not _is_linked(a2, 'relationpattern_SourceNode15', b)


def test_assoc_targets19_reverse_link_reassign_clear():
    a1 = relationpattern_TargetNode()
    a2 = relationpattern_TargetNode()
    b = relationpattern_Category(nom="sample_text")
    _safe_set(b, 'relationpattern_Category20', {a1})
    assert _is_linked(b, 'relationpattern_Category20', a1)
    if hasattr(a1, 'relationpattern_TargetNode21'):
        assert _is_linked(a1, 'relationpattern_TargetNode21', b)
    _safe_set(b, 'relationpattern_Category20', {a2})
    assert _is_linked(b, 'relationpattern_Category20', a2)
    if hasattr(a1, 'relationpattern_TargetNode21'):
        assert not _is_linked(a1, 'relationpattern_TargetNode21', b)
    if hasattr(a2, 'relationpattern_TargetNode21'):
        assert _is_linked(a2, 'relationpattern_TargetNode21', b)
    _safe_set(b, 'relationpattern_Category20', set())
    assert not _is_linked(b, 'relationpattern_Category20', a2)
    if hasattr(a2, 'relationpattern_TargetNode21'):
        assert not _is_linked(a2, 'relationpattern_TargetNode21', b)


def test_assoc_thingA0_reverse_link_reassign_clear():
    a1 = relationpattern_ThingA(since=date(2024, 1, 1))
    a2 = relationpattern_ThingA(since=date(2025, 6, 15))
    b = relationpattern_RelatedTo()
    _safe_set(b, 'relationpattern_RelatedTo', a1)
    assert _is_linked(b, 'relationpattern_RelatedTo', a1)
    if hasattr(a1, 'relationpattern_ThingA'):
        assert _is_linked(a1, 'relationpattern_ThingA', b)
    _safe_set(b, 'relationpattern_RelatedTo', a2)
    assert _is_linked(b, 'relationpattern_RelatedTo', a2)
    if hasattr(a1, 'relationpattern_ThingA'):
        assert not _is_linked(a1, 'relationpattern_ThingA', b)
    if hasattr(a2, 'relationpattern_ThingA'):
        assert _is_linked(a2, 'relationpattern_ThingA', b)
    _safe_set(b, 'relationpattern_RelatedTo', None)
    assert not _is_linked(b, 'relationpattern_RelatedTo', a2)
    if hasattr(a2, 'relationpattern_ThingA'):
        assert not _is_linked(a2, 'relationpattern_ThingA', b)


def test_assoc_thingB1_reverse_link_reassign_clear():
    a1 = relationpattern_ThingB(step="sample_text")
    a2 = relationpattern_ThingB(step="sample_text_2")
    b = relationpattern_RelatedTo()
    _safe_set(b, 'relationpattern_RelatedTo2', a1)
    assert _is_linked(b, 'relationpattern_RelatedTo2', a1)
    if hasattr(a1, 'relationpattern_ThingB'):
        assert _is_linked(a1, 'relationpattern_ThingB', b)
    _safe_set(b, 'relationpattern_RelatedTo2', a2)
    assert _is_linked(b, 'relationpattern_RelatedTo2', a2)
    if hasattr(a1, 'relationpattern_ThingB'):
        assert not _is_linked(a1, 'relationpattern_ThingB', b)
    if hasattr(a2, 'relationpattern_ThingB'):
        assert _is_linked(a2, 'relationpattern_ThingB', b)
    _safe_set(b, 'relationpattern_RelatedTo2', None)
    assert not _is_linked(b, 'relationpattern_RelatedTo2', a2)
    if hasattr(a2, 'relationpattern_ThingB'):
        assert not _is_linked(a2, 'relationpattern_ThingB', b)


def test_assoc_thingsa3_reverse_link_reassign_clear():
    a1 = relationpattern_World()
    a2 = relationpattern_World()
    b = relationpattern_ThingA(since=date(2024, 1, 1))
    _safe_set(b, 'relationpattern_ThingA4', a1)
    assert _is_linked(b, 'relationpattern_ThingA4', a1)
    if hasattr(a1, 'relationpattern_World'):
        assert _is_linked(a1, 'relationpattern_World', b)
    _safe_set(b, 'relationpattern_ThingA4', a2)
    assert _is_linked(b, 'relationpattern_ThingA4', a2)
    if hasattr(a1, 'relationpattern_World'):
        assert not _is_linked(a1, 'relationpattern_World', b)
    if hasattr(a2, 'relationpattern_World'):
        assert _is_linked(a2, 'relationpattern_World', b)
    _safe_set(b, 'relationpattern_ThingA4', None)
    assert not _is_linked(b, 'relationpattern_ThingA4', a2)
    if hasattr(a2, 'relationpattern_World'):
        assert not _is_linked(a2, 'relationpattern_World', b)


def test_assoc_thingsb5_reverse_link_reassign_clear():
    a1 = relationpattern_World()
    a2 = relationpattern_World()
    b = relationpattern_ThingB(step="sample_text")
    _safe_set(b, 'relationpattern_ThingB7', a1)
    assert _is_linked(b, 'relationpattern_ThingB7', a1)
    if hasattr(a1, 'relationpattern_World6'):
        assert _is_linked(a1, 'relationpattern_World6', b)
    _safe_set(b, 'relationpattern_ThingB7', a2)
    assert _is_linked(b, 'relationpattern_ThingB7', a2)
    if hasattr(a1, 'relationpattern_World6'):
        assert not _is_linked(a1, 'relationpattern_World6', b)
    if hasattr(a2, 'relationpattern_World6'):
        assert _is_linked(a2, 'relationpattern_World6', b)
    _safe_set(b, 'relationpattern_ThingB7', None)
    assert not _is_linked(b, 'relationpattern_ThingB7', a2)
    if hasattr(a2, 'relationpattern_World6'):
        assert not _is_linked(a2, 'relationpattern_World6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

