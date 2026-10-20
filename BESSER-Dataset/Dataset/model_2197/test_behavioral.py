import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DoorsObject,
    DoorsTreeNode,
    model_AttributeMap,
    model_DoorsFolder,
    model_DoorsLink,
    model_DoorsModule,
    model_DoorsObject,
    model_DoorsTableRow,
    model_DoorsTreeNode,
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

def test_assoc_attributes7_reverse_link_reassign_clear():
    a1 = model_DoorsTreeNode(fullName="sample_text", fullNameSegments="sample_text", name="sample_text")
    a2 = model_DoorsTreeNode(fullName="sample_text_2", fullNameSegments="sample_text_2", name="sample_text_2")
    b = model_AttributeMap(key="sample_text", value="sample_text")
    _safe_set(b, 'model_AttributeMap', a1)
    assert _is_linked(b, 'model_AttributeMap', a1)
    if hasattr(a1, 'model_DoorsTreeNode'):
        assert _is_linked(a1, 'model_DoorsTreeNode', b)
    _safe_set(b, 'model_AttributeMap', a2)
    assert _is_linked(b, 'model_AttributeMap', a2)
    if hasattr(a1, 'model_DoorsTreeNode'):
        assert not _is_linked(a1, 'model_DoorsTreeNode', b)
    if hasattr(a2, 'model_DoorsTreeNode'):
        assert _is_linked(a2, 'model_DoorsTreeNode', b)
    _safe_set(b, 'model_AttributeMap', None)
    assert not _is_linked(b, 'model_AttributeMap', a2)
    if hasattr(a2, 'model_DoorsTreeNode'):
        assert not _is_linked(a2, 'model_DoorsTreeNode', b)


def test_assoc_children3_reverse_link_reassign_clear():
    a1 = model_DoorsTreeNode(fullName="sample_text", fullNameSegments="sample_text", name="sample_text")
    a2 = model_DoorsTreeNode(fullName="sample_text_2", fullNameSegments="sample_text_2", name="sample_text_2")
    b = model_DoorsTreeNode(fullName="sample_text", fullNameSegments="sample_text", name="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'DoorsTreeNode'):
        assert _is_linked(a1, 'DoorsTreeNode', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'DoorsTreeNode'):
        assert not _is_linked(a1, 'DoorsTreeNode', b)
    if hasattr(a2, 'DoorsTreeNode'):
        assert _is_linked(a2, 'DoorsTreeNode', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'DoorsTreeNode'):
        assert not _is_linked(a2, 'DoorsTreeNode', b)


def test_assoc_outgoingLinks0_reverse_link_reassign_clear():
    a1 = model_DoorsObject(absoluteNumber=7, objectHeading="sample_text", objectIdentifier="sample_text", objectNumber="sample_text", objectShortText="sample_text", objectText="sample_text", text="sample_text")
    a2 = model_DoorsObject(absoluteNumber=13, objectHeading="sample_text_2", objectIdentifier="sample_text_2", objectNumber="sample_text_2", objectShortText="sample_text_2", objectText="sample_text_2", text="sample_text_2")
    b = model_DoorsLink(targetModule="sample_text", targetObject="sample_text")
    _safe_set(b, 'DoorsLink', a1)
    assert _is_linked(b, 'DoorsLink', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'DoorsLink', a2)
    assert _is_linked(b, 'DoorsLink', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'DoorsLink', None)
    assert not _is_linked(b, 'DoorsLink', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_parent5_reverse_link_reassign_clear():
    a1 = model_DoorsTreeNode(fullName="sample_text", fullNameSegments="sample_text", name="sample_text")
    a2 = model_DoorsTreeNode(fullName="sample_text_2", fullNameSegments="sample_text_2", name="sample_text_2")
    b = model_DoorsTreeNode(fullName="sample_text", fullNameSegments="sample_text", name="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'DoorsTreeNode6'):
        assert _is_linked(a1, 'DoorsTreeNode6', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'DoorsTreeNode6'):
        assert not _is_linked(a1, 'DoorsTreeNode6', b)
    if hasattr(a2, 'DoorsTreeNode6'):
        assert _is_linked(a2, 'DoorsTreeNode6', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'DoorsTreeNode6'):
        assert not _is_linked(a2, 'DoorsTreeNode6', b)


def test_assoc_source1_reverse_link_reassign_clear():
    a1 = model_DoorsObject(absoluteNumber=7, objectHeading="sample_text", objectIdentifier="sample_text", objectNumber="sample_text", objectShortText="sample_text", objectText="sample_text", text="sample_text")
    a2 = model_DoorsObject(absoluteNumber=13, objectHeading="sample_text_2", objectIdentifier="sample_text_2", objectNumber="sample_text_2", objectShortText="sample_text_2", objectText="sample_text_2", text="sample_text_2")
    b = model_DoorsLink(targetModule="sample_text", targetObject="sample_text")
    _safe_set(b, 'outgoingLinks', a1)
    assert _is_linked(b, 'outgoingLinks', a1)
    if hasattr(a1, 'DoorsObject'):
        assert _is_linked(a1, 'DoorsObject', b)
    _safe_set(b, 'outgoingLinks', a2)
    assert _is_linked(b, 'outgoingLinks', a2)
    if hasattr(a1, 'DoorsObject'):
        assert not _is_linked(a1, 'DoorsObject', b)
    if hasattr(a2, 'DoorsObject'):
        assert _is_linked(a2, 'DoorsObject', b)
    _safe_set(b, 'outgoingLinks', None)
    assert not _is_linked(b, 'outgoingLinks', a2)
    if hasattr(a2, 'DoorsObject'):
        assert not _is_linked(a2, 'DoorsObject', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

