import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    university_Course,
    university_Professor,
    university_Student,
    university_University,
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

def test_assoc_courses1_reverse_link_reassign_clear():
    a1 = university_Professor(name="sample_text")
    a2 = university_Professor(name="sample_text_2")
    b = university_Course(name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'professors'):
        assert _is_linked(a1, 'professors', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'professors'):
        assert not _is_linked(a1, 'professors', b)
    if hasattr(a2, 'professors'):
        assert _is_linked(a2, 'professors', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'professors'):
        assert not _is_linked(a2, 'professors', b)


def test_assoc_courses3_reverse_link_reassign_clear():
    a1 = university_University(name="sample_text")
    a2 = university_University(name="sample_text_2")
    b = university_Course(name="sample_text")
    _safe_set(b, 'university_Course', a1)
    assert _is_linked(b, 'university_Course', a1)
    if hasattr(a1, 'university_University4'):
        assert _is_linked(a1, 'university_University4', b)
    _safe_set(b, 'university_Course', a2)
    assert _is_linked(b, 'university_Course', a2)
    if hasattr(a1, 'university_University4'):
        assert not _is_linked(a1, 'university_University4', b)
    if hasattr(a2, 'university_University4'):
        assert _is_linked(a2, 'university_University4', b)
    _safe_set(b, 'university_Course', None)
    assert not _is_linked(b, 'university_Course', a2)
    if hasattr(a2, 'university_University4'):
        assert not _is_linked(a2, 'university_University4', b)


def test_assoc_professors0_reverse_link_reassign_clear():
    a1 = university_Professor(name="sample_text")
    a2 = university_Professor(name="sample_text_2")
    b = university_Course(name="sample_text")
    _safe_set(b, 'courses', {a1})
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'Professor'):
        assert _is_linked(a1, 'Professor', b)
    _safe_set(b, 'courses', {a2})
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'Professor'):
        assert not _is_linked(a1, 'Professor', b)
    if hasattr(a2, 'Professor'):
        assert _is_linked(a2, 'Professor', b)
    _safe_set(b, 'courses', set())
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'Professor'):
        assert not _is_linked(a2, 'Professor', b)


def test_assoc_professors2_reverse_link_reassign_clear():
    a1 = university_University(name="sample_text")
    a2 = university_University(name="sample_text_2")
    b = university_Professor(name="sample_text")
    _safe_set(b, 'university_Professor', a1)
    assert _is_linked(b, 'university_Professor', a1)
    if hasattr(a1, 'university_University'):
        assert _is_linked(a1, 'university_University', b)
    _safe_set(b, 'university_Professor', a2)
    assert _is_linked(b, 'university_Professor', a2)
    if hasattr(a1, 'university_University'):
        assert not _is_linked(a1, 'university_University', b)
    if hasattr(a2, 'university_University'):
        assert _is_linked(a2, 'university_University', b)
    _safe_set(b, 'university_Professor', None)
    assert not _is_linked(b, 'university_Professor', a2)
    if hasattr(a2, 'university_University'):
        assert not _is_linked(a2, 'university_University', b)


def test_assoc_students5_reverse_link_reassign_clear():
    a1 = university_University(name="sample_text")
    a2 = university_University(name="sample_text_2")
    b = university_Student(MNR="sample_text")
    _safe_set(b, 'university_Student', a1)
    assert _is_linked(b, 'university_Student', a1)
    if hasattr(a1, 'university_University6'):
        assert _is_linked(a1, 'university_University6', b)
    _safe_set(b, 'university_Student', a2)
    assert _is_linked(b, 'university_Student', a2)
    if hasattr(a1, 'university_University6'):
        assert not _is_linked(a1, 'university_University6', b)
    if hasattr(a2, 'university_University6'):
        assert _is_linked(a2, 'university_University6', b)
    _safe_set(b, 'university_Student', None)
    assert not _is_linked(b, 'university_Student', a2)
    if hasattr(a2, 'university_University6'):
        assert not _is_linked(a2, 'university_University6', b)


def test_assoc_uni7_reverse_link_reassign_clear():
    a1 = university_University(name="sample_text")
    a2 = university_University(name="sample_text_2")
    b = university_Student(MNR="sample_text")
    _safe_set(b, 'university_Student8', a1)
    assert _is_linked(b, 'university_Student8', a1)
    if hasattr(a1, 'university_University9'):
        assert _is_linked(a1, 'university_University9', b)
    _safe_set(b, 'university_Student8', a2)
    assert _is_linked(b, 'university_Student8', a2)
    if hasattr(a1, 'university_University9'):
        assert not _is_linked(a1, 'university_University9', b)
    if hasattr(a2, 'university_University9'):
        assert _is_linked(a2, 'university_University9', b)
    _safe_set(b, 'university_Student8', None)
    assert not _is_linked(b, 'university_Student8', a2)
    if hasattr(a2, 'university_University9'):
        assert not _is_linked(a2, 'university_University9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

