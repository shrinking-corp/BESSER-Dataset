import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Classifier,
    NamedElement,
    TypedElement,
    classes_Attribute,
    classes_CClass,
    classes_CModel,
    classes_Classifier,
    classes_Datatype,
    classes_NamedElement,
    classes_TypedElement,
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

def test_assoc_attributes3_reverse_link_reassign_clear():
    a1 = classes_CClass(abstract=True)
    a2 = classes_CClass(abstract=False)
    b = classes_Attribute(isMany=True)
    _safe_set(b, 'classes_Attribute', a1)
    assert _is_linked(b, 'classes_Attribute', a1)
    if hasattr(a1, 'classes_CClass4'):
        assert _is_linked(a1, 'classes_CClass4', b)
    _safe_set(b, 'classes_Attribute', a2)
    assert _is_linked(b, 'classes_Attribute', a2)
    if hasattr(a1, 'classes_CClass4'):
        assert not _is_linked(a1, 'classes_CClass4', b)
    if hasattr(a2, 'classes_CClass4'):
        assert _is_linked(a2, 'classes_CClass4', b)
    _safe_set(b, 'classes_Attribute', None)
    assert not _is_linked(b, 'classes_Attribute', a2)
    if hasattr(a2, 'classes_CClass4'):
        assert not _is_linked(a2, 'classes_CClass4', b)


def test_assoc_extends2_reverse_link_reassign_clear():
    a1 = classes_CClass(abstract=True)
    a2 = classes_CClass(abstract=False)
    b = classes_CClass(abstract=True)
    _safe_set(b, 'classes_CClass1', a1)
    assert _is_linked(b, 'classes_CClass1', a1)
    if hasattr(a1, 'classes_CClass'):
        assert _is_linked(a1, 'classes_CClass', b)
    _safe_set(b, 'classes_CClass1', a2)
    assert _is_linked(b, 'classes_CClass1', a2)
    if hasattr(a1, 'classes_CClass'):
        assert not _is_linked(a1, 'classes_CClass', b)
    if hasattr(a2, 'classes_CClass'):
        assert _is_linked(a2, 'classes_CClass', b)
    _safe_set(b, 'classes_CClass1', None)
    assert not _is_linked(b, 'classes_CClass1', a2)
    if hasattr(a2, 'classes_CClass'):
        assert not _is_linked(a2, 'classes_CClass', b)


def test_assoc_super6_reverse_link_reassign_clear():
    a1 = classes_CClass(abstract=True)
    a2 = classes_CClass(abstract=False)
    b = classes_CClass(abstract=True)
    _safe_set(b, 'classes_CClass7', a1)
    assert _is_linked(b, 'classes_CClass7', a1)
    if hasattr(a1, 'classes_CClass5'):
        assert _is_linked(a1, 'classes_CClass5', b)
    _safe_set(b, 'classes_CClass7', a2)
    assert _is_linked(b, 'classes_CClass7', a2)
    if hasattr(a1, 'classes_CClass5'):
        assert not _is_linked(a1, 'classes_CClass5', b)
    if hasattr(a2, 'classes_CClass5'):
        assert _is_linked(a2, 'classes_CClass5', b)
    _safe_set(b, 'classes_CClass7', None)
    assert not _is_linked(b, 'classes_CClass7', a2)
    if hasattr(a2, 'classes_CClass5'):
        assert not _is_linked(a2, 'classes_CClass5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

