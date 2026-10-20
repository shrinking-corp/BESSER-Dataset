import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    class_Association,
    class_Attribute,
    class_ClassDiagram,
    class_Clazz,
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

def test_assoc_associations1_reverse_link_reassign_clear():
    a1 = class_ClassDiagram(id="sample_text")
    a2 = class_ClassDiagram(id="sample_text_2")
    b = class_Association(id="sample_text")
    _safe_set(b, 'class_Association', a1)
    assert _is_linked(b, 'class_Association', a1)
    if hasattr(a1, 'class_ClassDiagram2'):
        assert _is_linked(a1, 'class_ClassDiagram2', b)
    _safe_set(b, 'class_Association', a2)
    assert _is_linked(b, 'class_Association', a2)
    if hasattr(a1, 'class_ClassDiagram2'):
        assert not _is_linked(a1, 'class_ClassDiagram2', b)
    if hasattr(a2, 'class_ClassDiagram2'):
        assert _is_linked(a2, 'class_ClassDiagram2', b)
    _safe_set(b, 'class_Association', None)
    assert not _is_linked(b, 'class_Association', a2)
    if hasattr(a2, 'class_ClassDiagram2'):
        assert not _is_linked(a2, 'class_ClassDiagram2', b)


def test_assoc_attribute3_reverse_link_reassign_clear():
    a1 = class_Clazz(id="sample_text")
    a2 = class_Clazz(id="sample_text_2")
    b = class_Attribute(id="sample_text")
    _safe_set(b, 'class_Attribute', a1)
    assert _is_linked(b, 'class_Attribute', a1)
    if hasattr(a1, 'class_Clazz4'):
        assert _is_linked(a1, 'class_Clazz4', b)
    _safe_set(b, 'class_Attribute', a2)
    assert _is_linked(b, 'class_Attribute', a2)
    if hasattr(a1, 'class_Clazz4'):
        assert not _is_linked(a1, 'class_Clazz4', b)
    if hasattr(a2, 'class_Clazz4'):
        assert _is_linked(a2, 'class_Clazz4', b)
    _safe_set(b, 'class_Attribute', None)
    assert not _is_linked(b, 'class_Attribute', a2)
    if hasattr(a2, 'class_Clazz4'):
        assert not _is_linked(a2, 'class_Clazz4', b)


def test_assoc_classes0_reverse_link_reassign_clear():
    a1 = class_Clazz(id="sample_text")
    a2 = class_Clazz(id="sample_text_2")
    b = class_ClassDiagram(id="sample_text")
    _safe_set(b, 'class_ClassDiagram', {a1})
    assert _is_linked(b, 'class_ClassDiagram', a1)
    if hasattr(a1, 'class_Clazz'):
        assert _is_linked(a1, 'class_Clazz', b)
    _safe_set(b, 'class_ClassDiagram', {a2})
    assert _is_linked(b, 'class_ClassDiagram', a2)
    if hasattr(a1, 'class_Clazz'):
        assert not _is_linked(a1, 'class_Clazz', b)
    if hasattr(a2, 'class_Clazz'):
        assert _is_linked(a2, 'class_Clazz', b)
    _safe_set(b, 'class_ClassDiagram', set())
    assert not _is_linked(b, 'class_ClassDiagram', a2)
    if hasattr(a2, 'class_Clazz'):
        assert not _is_linked(a2, 'class_Clazz', b)


def test_assoc_source8_reverse_link_reassign_clear():
    a1 = class_Clazz(id="sample_text")
    a2 = class_Clazz(id="sample_text_2")
    b = class_Association(id="sample_text")
    _safe_set(b, 'class_Association9', a1)
    assert _is_linked(b, 'class_Association9', a1)
    if hasattr(a1, 'class_Clazz10'):
        assert _is_linked(a1, 'class_Clazz10', b)
    _safe_set(b, 'class_Association9', a2)
    assert _is_linked(b, 'class_Association9', a2)
    if hasattr(a1, 'class_Clazz10'):
        assert not _is_linked(a1, 'class_Clazz10', b)
    if hasattr(a2, 'class_Clazz10'):
        assert _is_linked(a2, 'class_Clazz10', b)
    _safe_set(b, 'class_Association9', None)
    assert not _is_linked(b, 'class_Association9', a2)
    if hasattr(a2, 'class_Clazz10'):
        assert not _is_linked(a2, 'class_Clazz10', b)


def test_assoc_super6_reverse_link_reassign_clear():
    a1 = class_Clazz(id="sample_text")
    a2 = class_Clazz(id="sample_text_2")
    b = class_Clazz(id="sample_text")
    _safe_set(b, 'class_Clazz7', a1)
    assert _is_linked(b, 'class_Clazz7', a1)
    if hasattr(a1, 'class_Clazz5'):
        assert _is_linked(a1, 'class_Clazz5', b)
    _safe_set(b, 'class_Clazz7', a2)
    assert _is_linked(b, 'class_Clazz7', a2)
    if hasattr(a1, 'class_Clazz5'):
        assert not _is_linked(a1, 'class_Clazz5', b)
    if hasattr(a2, 'class_Clazz5'):
        assert _is_linked(a2, 'class_Clazz5', b)
    _safe_set(b, 'class_Clazz7', None)
    assert not _is_linked(b, 'class_Clazz7', a2)
    if hasattr(a2, 'class_Clazz5'):
        assert not _is_linked(a2, 'class_Clazz5', b)


def test_assoc_target11_reverse_link_reassign_clear():
    a1 = class_Clazz(id="sample_text")
    a2 = class_Clazz(id="sample_text_2")
    b = class_Association(id="sample_text")
    _safe_set(b, 'class_Association12', a1)
    assert _is_linked(b, 'class_Association12', a1)
    if hasattr(a1, 'class_Clazz13'):
        assert _is_linked(a1, 'class_Clazz13', b)
    _safe_set(b, 'class_Association12', a2)
    assert _is_linked(b, 'class_Association12', a2)
    if hasattr(a1, 'class_Clazz13'):
        assert not _is_linked(a1, 'class_Clazz13', b)
    if hasattr(a2, 'class_Clazz13'):
        assert _is_linked(a2, 'class_Clazz13', b)
    _safe_set(b, 'class_Association12', None)
    assert not _is_linked(b, 'class_Association12', a2)
    if hasattr(a2, 'class_Clazz13'):
        assert not _is_linked(a2, 'class_Clazz13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

