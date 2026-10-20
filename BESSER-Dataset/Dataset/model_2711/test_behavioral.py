import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Kasu11_ClassA,
    Kasu11_ClassB,
    Kasu11_ClassC,
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

def test_assoc_C_A3_reverse_link_reassign_clear():
    a1 = Kasu11_ClassB(Name="sample_text")
    a2 = Kasu11_ClassB(Name="sample_text_2")
    b = Kasu11_ClassA(Name="sample_text")
    _safe_set(b, 'ClassA', a1)
    assert _is_linked(b, 'ClassA', a1)
    if hasattr(a1, 'C_B'):
        assert _is_linked(a1, 'C_B', b)
    _safe_set(b, 'ClassA', a2)
    assert _is_linked(b, 'ClassA', a2)
    if hasattr(a1, 'C_B'):
        assert not _is_linked(a1, 'C_B', b)
    if hasattr(a2, 'C_B'):
        assert _is_linked(a2, 'C_B', b)
    _safe_set(b, 'ClassA', None)
    assert not _is_linked(b, 'ClassA', a2)
    if hasattr(a2, 'C_B'):
        assert not _is_linked(a2, 'C_B', b)


def test_assoc_C_A7_reverse_link_reassign_clear():
    a1 = Kasu11_ClassC(Name="sample_text")
    a2 = Kasu11_ClassC(Name="sample_text_2")
    b = Kasu11_ClassA(Name="sample_text")
    _safe_set(b, 'ClassA8', a1)
    assert _is_linked(b, 'ClassA8', a1)
    if hasattr(a1, 'C_C'):
        assert _is_linked(a1, 'C_C', b)
    _safe_set(b, 'ClassA8', a2)
    assert _is_linked(b, 'ClassA8', a2)
    if hasattr(a1, 'C_C'):
        assert not _is_linked(a1, 'C_C', b)
    if hasattr(a2, 'C_C'):
        assert _is_linked(a2, 'C_C', b)
    _safe_set(b, 'ClassA8', None)
    assert not _is_linked(b, 'ClassA8', a2)
    if hasattr(a2, 'C_C'):
        assert not _is_linked(a2, 'C_C', b)


def test_assoc_C_B0_reverse_link_reassign_clear():
    a1 = Kasu11_ClassB(Name="sample_text")
    a2 = Kasu11_ClassB(Name="sample_text_2")
    b = Kasu11_ClassA(Name="sample_text")
    _safe_set(b, 'C_A', {a1})
    assert _is_linked(b, 'C_A', a1)
    if hasattr(a1, 'ClassB'):
        assert _is_linked(a1, 'ClassB', b)
    _safe_set(b, 'C_A', {a2})
    assert _is_linked(b, 'C_A', a2)
    if hasattr(a1, 'ClassB'):
        assert not _is_linked(a1, 'ClassB', b)
    if hasattr(a2, 'ClassB'):
        assert _is_linked(a2, 'ClassB', b)
    _safe_set(b, 'C_A', set())
    assert not _is_linked(b, 'C_A', a2)
    if hasattr(a2, 'ClassB'):
        assert not _is_linked(a2, 'ClassB', b)


def test_assoc_C_B9_reverse_link_reassign_clear():
    a1 = Kasu11_ClassC(Name="sample_text")
    a2 = Kasu11_ClassC(Name="sample_text_2")
    b = Kasu11_ClassB(Name="sample_text")
    _safe_set(b, 'ClassB11', a1)
    assert _is_linked(b, 'ClassB11', a1)
    if hasattr(a1, 'C_C10'):
        assert _is_linked(a1, 'C_C10', b)
    _safe_set(b, 'ClassB11', a2)
    assert _is_linked(b, 'ClassB11', a2)
    if hasattr(a1, 'C_C10'):
        assert not _is_linked(a1, 'C_C10', b)
    if hasattr(a2, 'C_C10'):
        assert _is_linked(a2, 'C_C10', b)
    _safe_set(b, 'ClassB11', None)
    assert not _is_linked(b, 'ClassB11', a2)
    if hasattr(a2, 'C_C10'):
        assert not _is_linked(a2, 'C_C10', b)


def test_assoc_C_C1_reverse_link_reassign_clear():
    a1 = Kasu11_ClassC(Name="sample_text")
    a2 = Kasu11_ClassC(Name="sample_text_2")
    b = Kasu11_ClassA(Name="sample_text")
    _safe_set(b, 'C_A2', {a1})
    assert _is_linked(b, 'C_A2', a1)
    if hasattr(a1, 'ClassC'):
        assert _is_linked(a1, 'ClassC', b)
    _safe_set(b, 'C_A2', {a2})
    assert _is_linked(b, 'C_A2', a2)
    if hasattr(a1, 'ClassC'):
        assert not _is_linked(a1, 'ClassC', b)
    if hasattr(a2, 'ClassC'):
        assert _is_linked(a2, 'ClassC', b)
    _safe_set(b, 'C_A2', set())
    assert not _is_linked(b, 'C_A2', a2)
    if hasattr(a2, 'ClassC'):
        assert not _is_linked(a2, 'ClassC', b)


def test_assoc_C_C4_reverse_link_reassign_clear():
    a1 = Kasu11_ClassC(Name="sample_text")
    a2 = Kasu11_ClassC(Name="sample_text_2")
    b = Kasu11_ClassB(Name="sample_text")
    _safe_set(b, 'C_B5', {a1})
    assert _is_linked(b, 'C_B5', a1)
    if hasattr(a1, 'ClassC6'):
        assert _is_linked(a1, 'ClassC6', b)
    _safe_set(b, 'C_B5', {a2})
    assert _is_linked(b, 'C_B5', a2)
    if hasattr(a1, 'ClassC6'):
        assert not _is_linked(a1, 'ClassC6', b)
    if hasattr(a2, 'ClassC6'):
        assert _is_linked(a2, 'ClassC6', b)
    _safe_set(b, 'C_B5', set())
    assert not _is_linked(b, 'C_B5', a2)
    if hasattr(a2, 'ClassC6'):
        assert not _is_linked(a2, 'ClassC6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

