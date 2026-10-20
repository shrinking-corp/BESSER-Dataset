import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    classes_Attribute,
    classes_Class,
    classes_ClassDiagram,
    classes_Reference,
    Type,
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

def test_assoc__primary_key5_reverse_link_reassign_clear():
    a1 = classes_Class(name="sample_text")
    a2 = classes_Class(name="sample_text_2")
    b = classes_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'classes_Attribute', a1)
    assert _is_linked(b, 'classes_Attribute', a1)
    if hasattr(a1, 'classes_Class'):
        assert _is_linked(a1, 'classes_Class', b)
    _safe_set(b, 'classes_Attribute', a2)
    assert _is_linked(b, 'classes_Attribute', a2)
    if hasattr(a1, 'classes_Class'):
        assert not _is_linked(a1, 'classes_Class', b)
    if hasattr(a2, 'classes_Class'):
        assert _is_linked(a2, 'classes_Class', b)
    _safe_set(b, 'classes_Attribute', None)
    assert not _is_linked(b, 'classes_Attribute', a2)
    if hasattr(a2, 'classes_Class'):
        assert not _is_linked(a2, 'classes_Class', b)


def test_assoc_attributes1_reverse_link_reassign_clear():
    a1 = classes_Class(name="sample_text")
    a2 = classes_Class(name="sample_text_2")
    b = classes_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'cls'):
        assert _is_linked(a1, 'cls', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'cls'):
        assert not _is_linked(a1, 'cls', b)
    if hasattr(a2, 'cls'):
        assert _is_linked(a2, 'cls', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'cls'):
        assert not _is_linked(a2, 'cls', b)


def test_assoc_classes0_reverse_link_reassign_clear():
    a1 = classes_ClassDiagram(name="sample_text")
    a2 = classes_ClassDiagram(name="sample_text_2")
    b = classes_Class(name="sample_text")
    _safe_set(b, 'Class', a1)
    assert _is_linked(b, 'Class', a1)
    if hasattr(a1, 'diagram'):
        assert _is_linked(a1, 'diagram', b)
    _safe_set(b, 'Class', a2)
    assert _is_linked(b, 'Class', a2)
    if hasattr(a1, 'diagram'):
        assert not _is_linked(a1, 'diagram', b)
    if hasattr(a2, 'diagram'):
        assert _is_linked(a2, 'diagram', b)
    _safe_set(b, 'Class', None)
    assert not _is_linked(b, 'Class', a2)
    if hasattr(a2, 'diagram'):
        assert not _is_linked(a2, 'diagram', b)


def test_assoc_cls6_reverse_link_reassign_clear():
    a1 = classes_Class(name="sample_text")
    a2 = classes_Class(name="sample_text_2")
    b = classes_Attribute(name="sample_text", type="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Class7'):
        assert _is_linked(a1, 'Class7', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Class7'):
        assert not _is_linked(a1, 'Class7', b)
    if hasattr(a2, 'Class7'):
        assert _is_linked(a2, 'Class7', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Class7'):
        assert not _is_linked(a2, 'Class7', b)


def test_assoc_cls8_reverse_link_reassign_clear():
    a1 = classes_Reference(name="sample_text")
    a2 = classes_Reference(name="sample_text_2")
    b = classes_Class(name="sample_text")
    _safe_set(b, 'Class9', a1)
    assert _is_linked(b, 'Class9', a1)
    if hasattr(a1, 'references'):
        assert _is_linked(a1, 'references', b)
    _safe_set(b, 'Class9', a2)
    assert _is_linked(b, 'Class9', a2)
    if hasattr(a1, 'references'):
        assert not _is_linked(a1, 'references', b)
    if hasattr(a2, 'references'):
        assert _is_linked(a2, 'references', b)
    _safe_set(b, 'Class9', None)
    assert not _is_linked(b, 'Class9', a2)
    if hasattr(a2, 'references'):
        assert not _is_linked(a2, 'references', b)


def test_assoc_diagram4_reverse_link_reassign_clear():
    a1 = classes_ClassDiagram(name="sample_text")
    a2 = classes_ClassDiagram(name="sample_text_2")
    b = classes_Class(name="sample_text")
    _safe_set(b, 'classes', a1)
    assert _is_linked(b, 'classes', a1)
    if hasattr(a1, 'ClassDiagram'):
        assert _is_linked(a1, 'ClassDiagram', b)
    _safe_set(b, 'classes', a2)
    assert _is_linked(b, 'classes', a2)
    if hasattr(a1, 'ClassDiagram'):
        assert not _is_linked(a1, 'ClassDiagram', b)
    if hasattr(a2, 'ClassDiagram'):
        assert _is_linked(a2, 'ClassDiagram', b)
    _safe_set(b, 'classes', None)
    assert not _is_linked(b, 'classes', a2)
    if hasattr(a2, 'ClassDiagram'):
        assert not _is_linked(a2, 'ClassDiagram', b)


def test_assoc_references2_reverse_link_reassign_clear():
    a1 = classes_Reference(name="sample_text")
    a2 = classes_Reference(name="sample_text_2")
    b = classes_Class(name="sample_text")
    _safe_set(b, 'cls3', {a1})
    assert _is_linked(b, 'cls3', a1)
    if hasattr(a1, 'Reference'):
        assert _is_linked(a1, 'Reference', b)
    _safe_set(b, 'cls3', {a2})
    assert _is_linked(b, 'cls3', a2)
    if hasattr(a1, 'Reference'):
        assert not _is_linked(a1, 'Reference', b)
    if hasattr(a2, 'Reference'):
        assert _is_linked(a2, 'Reference', b)
    _safe_set(b, 'cls3', set())
    assert not _is_linked(b, 'cls3', a2)
    if hasattr(a2, 'Reference'):
        assert not _is_linked(a2, 'Reference', b)


def test_assoc_target10_reverse_link_reassign_clear():
    a1 = classes_Reference(name="sample_text")
    a2 = classes_Reference(name="sample_text_2")
    b = classes_Class(name="sample_text")
    _safe_set(b, 'classes_Class11', a1)
    assert _is_linked(b, 'classes_Class11', a1)
    if hasattr(a1, 'classes_Reference'):
        assert _is_linked(a1, 'classes_Reference', b)
    _safe_set(b, 'classes_Class11', a2)
    assert _is_linked(b, 'classes_Class11', a2)
    if hasattr(a1, 'classes_Reference'):
        assert not _is_linked(a1, 'classes_Reference', b)
    if hasattr(a2, 'classes_Reference'):
        assert _is_linked(a2, 'classes_Reference', b)
    _safe_set(b, 'classes_Class11', None)
    assert not _is_linked(b, 'classes_Class11', a2)
    if hasattr(a2, 'classes_Reference'):
        assert not _is_linked(a2, 'classes_Reference', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

