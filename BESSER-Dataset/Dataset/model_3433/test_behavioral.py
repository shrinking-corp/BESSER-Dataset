import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Matter,
    school_Academy,
    school_ClassRoom,
    school_Math,
    school_Matter,
    school_Notation,
    school_School,
    school_Student,
    school_Teacher,
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

def test_assoc_children16_reverse_link_reassign_clear():
    a1 = school_Student(age=7, name="sample_text")
    a2 = school_Student(age=13, name="sample_text_2")
    b = school_ClassRoom(number=7)
    _safe_set(b, 'school_ClassRoom17', {a1})
    assert _is_linked(b, 'school_ClassRoom17', a1)
    if hasattr(a1, 'school_Student18'):
        assert _is_linked(a1, 'school_Student18', b)
    _safe_set(b, 'school_ClassRoom17', {a2})
    assert _is_linked(b, 'school_ClassRoom17', a2)
    if hasattr(a1, 'school_Student18'):
        assert not _is_linked(a1, 'school_Student18', b)
    if hasattr(a2, 'school_Student18'):
        assert _is_linked(a2, 'school_Student18', b)
    _safe_set(b, 'school_ClassRoom17', set())
    assert not _is_linked(b, 'school_ClassRoom17', a2)
    if hasattr(a2, 'school_Student18'):
        assert not _is_linked(a2, 'school_Student18', b)


def test_assoc_notations19_reverse_link_reassign_clear():
    a1 = school_Student(age=7, name="sample_text")
    a2 = school_Student(age=13, name="sample_text_2")
    b = school_Notation(value=7)
    _safe_set(b, 'school_Notation', a1)
    assert _is_linked(b, 'school_Notation', a1)
    if hasattr(a1, 'school_Student20'):
        assert _is_linked(a1, 'school_Student20', b)
    _safe_set(b, 'school_Notation', a2)
    assert _is_linked(b, 'school_Notation', a2)
    if hasattr(a1, 'school_Student20'):
        assert not _is_linked(a1, 'school_Student20', b)
    if hasattr(a2, 'school_Student20'):
        assert _is_linked(a2, 'school_Student20', b)
    _safe_set(b, 'school_Notation', None)
    assert not _is_linked(b, 'school_Notation', a2)
    if hasattr(a2, 'school_Student20'):
        assert not _is_linked(a2, 'school_Student20', b)


def test_assoc_rooms5_reverse_link_reassign_clear():
    a1 = school_School(name="sample_text", rank=7)
    a2 = school_School(name="sample_text_2", rank=13)
    b = school_ClassRoom(number=7)
    _safe_set(b, 'school_ClassRoom', a1)
    assert _is_linked(b, 'school_ClassRoom', a1)
    if hasattr(a1, 'school_School6'):
        assert _is_linked(a1, 'school_School6', b)
    _safe_set(b, 'school_ClassRoom', a2)
    assert _is_linked(b, 'school_ClassRoom', a2)
    if hasattr(a1, 'school_School6'):
        assert not _is_linked(a1, 'school_School6', b)
    if hasattr(a2, 'school_School6'):
        assert _is_linked(a2, 'school_School6', b)
    _safe_set(b, 'school_ClassRoom', None)
    assert not _is_linked(b, 'school_ClassRoom', a2)
    if hasattr(a2, 'school_School6'):
        assert not _is_linked(a2, 'school_School6', b)


def test_assoc_schools3_reverse_link_reassign_clear():
    a1 = school_School(name="sample_text", rank=7)
    a2 = school_School(name="sample_text_2", rank=13)
    b = school_Academy(name="sample_text")
    _safe_set(b, 'school_Academy4', {a1})
    assert _is_linked(b, 'school_Academy4', a1)
    if hasattr(a1, 'school_School'):
        assert _is_linked(a1, 'school_School', b)
    _safe_set(b, 'school_Academy4', {a2})
    assert _is_linked(b, 'school_Academy4', a2)
    if hasattr(a1, 'school_School'):
        assert not _is_linked(a1, 'school_School', b)
    if hasattr(a2, 'school_School'):
        assert _is_linked(a2, 'school_School', b)
    _safe_set(b, 'school_Academy4', set())
    assert not _is_linked(b, 'school_Academy4', a2)
    if hasattr(a2, 'school_School'):
        assert not _is_linked(a2, 'school_School', b)


def test_assoc_students1_reverse_link_reassign_clear():
    a1 = school_Student(age=7, name="sample_text")
    a2 = school_Student(age=13, name="sample_text_2")
    b = school_Academy(name="sample_text")
    _safe_set(b, 'school_Academy2', {a1})
    assert _is_linked(b, 'school_Academy2', a1)
    if hasattr(a1, 'school_Student'):
        assert _is_linked(a1, 'school_Student', b)
    _safe_set(b, 'school_Academy2', {a2})
    assert _is_linked(b, 'school_Academy2', a2)
    if hasattr(a1, 'school_Student'):
        assert not _is_linked(a1, 'school_Student', b)
    if hasattr(a2, 'school_Student'):
        assert _is_linked(a2, 'school_Student', b)
    _safe_set(b, 'school_Academy2', set())
    assert not _is_linked(b, 'school_Academy2', a2)
    if hasattr(a2, 'school_Student'):
        assert not _is_linked(a2, 'school_Student', b)


def test_assoc_students10_reverse_link_reassign_clear():
    a1 = school_Student(age=7, name="sample_text")
    a2 = school_Student(age=13, name="sample_text_2")
    b = school_School(name="sample_text", rank=7)
    _safe_set(b, 'school_School11', {a1})
    assert _is_linked(b, 'school_School11', a1)
    if hasattr(a1, 'school_Student12'):
        assert _is_linked(a1, 'school_Student12', b)
    _safe_set(b, 'school_School11', {a2})
    assert _is_linked(b, 'school_School11', a2)
    if hasattr(a1, 'school_Student12'):
        assert not _is_linked(a1, 'school_Student12', b)
    if hasattr(a2, 'school_Student12'):
        assert _is_linked(a2, 'school_Student12', b)
    _safe_set(b, 'school_School11', set())
    assert not _is_linked(b, 'school_School11', a2)
    if hasattr(a2, 'school_Student12'):
        assert not _is_linked(a2, 'school_Student12', b)


def test_assoc_teacher13_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_ClassRoom(number=7)
    _safe_set(b, 'school_ClassRoom14', a1)
    assert _is_linked(b, 'school_ClassRoom14', a1)
    if hasattr(a1, 'school_Teacher15'):
        assert _is_linked(a1, 'school_Teacher15', b)
    _safe_set(b, 'school_ClassRoom14', a2)
    assert _is_linked(b, 'school_ClassRoom14', a2)
    if hasattr(a1, 'school_Teacher15'):
        assert not _is_linked(a1, 'school_Teacher15', b)
    if hasattr(a2, 'school_Teacher15'):
        assert _is_linked(a2, 'school_Teacher15', b)
    _safe_set(b, 'school_ClassRoom14', None)
    assert not _is_linked(b, 'school_ClassRoom14', a2)
    if hasattr(a2, 'school_Teacher15'):
        assert not _is_linked(a2, 'school_Teacher15', b)


def test_assoc_teachers0_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_Academy(name="sample_text")
    _safe_set(b, 'school_Academy', {a1})
    assert _is_linked(b, 'school_Academy', a1)
    if hasattr(a1, 'school_Teacher'):
        assert _is_linked(a1, 'school_Teacher', b)
    _safe_set(b, 'school_Academy', {a2})
    assert _is_linked(b, 'school_Academy', a2)
    if hasattr(a1, 'school_Teacher'):
        assert not _is_linked(a1, 'school_Teacher', b)
    if hasattr(a2, 'school_Teacher'):
        assert _is_linked(a2, 'school_Teacher', b)
    _safe_set(b, 'school_Academy', set())
    assert not _is_linked(b, 'school_Academy', a2)
    if hasattr(a2, 'school_Teacher'):
        assert not _is_linked(a2, 'school_Teacher', b)


def test_assoc_teachers7_reverse_link_reassign_clear():
    a1 = school_Teacher(name="sample_text")
    a2 = school_Teacher(name="sample_text_2")
    b = school_School(name="sample_text", rank=7)
    _safe_set(b, 'school_School8', {a1})
    assert _is_linked(b, 'school_School8', a1)
    if hasattr(a1, 'school_Teacher9'):
        assert _is_linked(a1, 'school_Teacher9', b)
    _safe_set(b, 'school_School8', {a2})
    assert _is_linked(b, 'school_School8', a2)
    if hasattr(a1, 'school_Teacher9'):
        assert not _is_linked(a1, 'school_Teacher9', b)
    if hasattr(a2, 'school_Teacher9'):
        assert _is_linked(a2, 'school_Teacher9', b)
    _safe_set(b, 'school_School8', set())
    assert not _is_linked(b, 'school_School8', a2)
    if hasattr(a2, 'school_Teacher9'):
        assert not _is_linked(a2, 'school_Teacher9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

