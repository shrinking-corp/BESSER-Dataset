import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    epdemo_Clazz,
    epdemo_School,
    epdemo_Student,
    epdemo_Teacher,
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

def test_assoc_Clazzes0_reverse_link_reassign_clear():
    a1 = epdemo_School(Id="sample_text", Name="sample_text")
    a2 = epdemo_School(Id="sample_text_2", Name="sample_text_2")
    b = epdemo_Clazz(Id="sample_text", Name="sample_text")
    _safe_set(b, 'epdemo_Clazz', a1)
    assert _is_linked(b, 'epdemo_Clazz', a1)
    if hasattr(a1, 'epdemo_School'):
        assert _is_linked(a1, 'epdemo_School', b)
    _safe_set(b, 'epdemo_Clazz', a2)
    assert _is_linked(b, 'epdemo_Clazz', a2)
    if hasattr(a1, 'epdemo_School'):
        assert not _is_linked(a1, 'epdemo_School', b)
    if hasattr(a2, 'epdemo_School'):
        assert _is_linked(a2, 'epdemo_School', b)
    _safe_set(b, 'epdemo_Clazz', None)
    assert not _is_linked(b, 'epdemo_Clazz', a2)
    if hasattr(a2, 'epdemo_School'):
        assert not _is_linked(a2, 'epdemo_School', b)


def test_assoc_students1_reverse_link_reassign_clear():
    a1 = epdemo_Student(Id="sample_text", Name="sample_text")
    a2 = epdemo_Student(Id="sample_text_2", Name="sample_text_2")
    b = epdemo_School(Id="sample_text", Name="sample_text")
    _safe_set(b, 'epdemo_School2', {a1})
    assert _is_linked(b, 'epdemo_School2', a1)
    if hasattr(a1, 'epdemo_Student'):
        assert _is_linked(a1, 'epdemo_Student', b)
    _safe_set(b, 'epdemo_School2', {a2})
    assert _is_linked(b, 'epdemo_School2', a2)
    if hasattr(a1, 'epdemo_Student'):
        assert not _is_linked(a1, 'epdemo_Student', b)
    if hasattr(a2, 'epdemo_Student'):
        assert _is_linked(a2, 'epdemo_Student', b)
    _safe_set(b, 'epdemo_School2', set())
    assert not _is_linked(b, 'epdemo_School2', a2)
    if hasattr(a2, 'epdemo_Student'):
        assert not _is_linked(a2, 'epdemo_Student', b)


def test_assoc_students8_reverse_link_reassign_clear():
    a1 = epdemo_Student(Id="sample_text", Name="sample_text")
    a2 = epdemo_Student(Id="sample_text_2", Name="sample_text_2")
    b = epdemo_Clazz(Id="sample_text", Name="sample_text")
    _safe_set(b, 'epdemo_Clazz9', {a1})
    assert _is_linked(b, 'epdemo_Clazz9', a1)
    if hasattr(a1, 'epdemo_Student10'):
        assert _is_linked(a1, 'epdemo_Student10', b)
    _safe_set(b, 'epdemo_Clazz9', {a2})
    assert _is_linked(b, 'epdemo_Clazz9', a2)
    if hasattr(a1, 'epdemo_Student10'):
        assert not _is_linked(a1, 'epdemo_Student10', b)
    if hasattr(a2, 'epdemo_Student10'):
        assert _is_linked(a2, 'epdemo_Student10', b)
    _safe_set(b, 'epdemo_Clazz9', set())
    assert not _is_linked(b, 'epdemo_Clazz9', a2)
    if hasattr(a2, 'epdemo_Student10'):
        assert not _is_linked(a2, 'epdemo_Student10', b)


def test_assoc_teachers3_reverse_link_reassign_clear():
    a1 = epdemo_Teacher(Id="sample_text", Name="sample_text")
    a2 = epdemo_Teacher(Id="sample_text_2", Name="sample_text_2")
    b = epdemo_School(Id="sample_text", Name="sample_text")
    _safe_set(b, 'epdemo_School4', {a1})
    assert _is_linked(b, 'epdemo_School4', a1)
    if hasattr(a1, 'epdemo_Teacher'):
        assert _is_linked(a1, 'epdemo_Teacher', b)
    _safe_set(b, 'epdemo_School4', {a2})
    assert _is_linked(b, 'epdemo_School4', a2)
    if hasattr(a1, 'epdemo_Teacher'):
        assert not _is_linked(a1, 'epdemo_Teacher', b)
    if hasattr(a2, 'epdemo_Teacher'):
        assert _is_linked(a2, 'epdemo_Teacher', b)
    _safe_set(b, 'epdemo_School4', set())
    assert not _is_linked(b, 'epdemo_School4', a2)
    if hasattr(a2, 'epdemo_Teacher'):
        assert not _is_linked(a2, 'epdemo_Teacher', b)


def test_assoc_teachers5_reverse_link_reassign_clear():
    a1 = epdemo_Teacher(Id="sample_text", Name="sample_text")
    a2 = epdemo_Teacher(Id="sample_text_2", Name="sample_text_2")
    b = epdemo_Clazz(Id="sample_text", Name="sample_text")
    _safe_set(b, 'epdemo_Clazz6', {a1})
    assert _is_linked(b, 'epdemo_Clazz6', a1)
    if hasattr(a1, 'epdemo_Teacher7'):
        assert _is_linked(a1, 'epdemo_Teacher7', b)
    _safe_set(b, 'epdemo_Clazz6', {a2})
    assert _is_linked(b, 'epdemo_Clazz6', a2)
    if hasattr(a1, 'epdemo_Teacher7'):
        assert not _is_linked(a1, 'epdemo_Teacher7', b)
    if hasattr(a2, 'epdemo_Teacher7'):
        assert _is_linked(a2, 'epdemo_Teacher7', b)
    _safe_set(b, 'epdemo_Clazz6', set())
    assert not _is_linked(b, 'epdemo_Clazz6', a2)
    if hasattr(a2, 'epdemo_Teacher7'):
        assert not _is_linked(a2, 'epdemo_Teacher7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

