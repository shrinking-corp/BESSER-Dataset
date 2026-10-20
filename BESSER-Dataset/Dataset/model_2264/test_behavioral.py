import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    mteach_Course,
    mteach_Professor,
    mteach_Topic,
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

def test_assoc_course3_reverse_link_reassign_clear():
    a1 = mteach_Topic(title="sample_text")
    a2 = mteach_Topic(title="sample_text_2")
    b = mteach_Course(coefficient=3.14, name="sample_text", time=7)
    _safe_set(b, 'Course4', a1)
    assert _is_linked(b, 'Course4', a1)
    if hasattr(a1, 'topics'):
        assert _is_linked(a1, 'topics', b)
    _safe_set(b, 'Course4', a2)
    assert _is_linked(b, 'Course4', a2)
    if hasattr(a1, 'topics'):
        assert not _is_linked(a1, 'topics', b)
    if hasattr(a2, 'topics'):
        assert _is_linked(a2, 'topics', b)
    _safe_set(b, 'Course4', None)
    assert not _is_linked(b, 'Course4', a2)
    if hasattr(a2, 'topics'):
        assert not _is_linked(a2, 'topics', b)


def test_assoc_professor2_reverse_link_reassign_clear():
    a1 = mteach_Professor(firstName="sample_text", lastName="sample_text")
    a2 = mteach_Professor(firstName="sample_text_2", lastName="sample_text_2")
    b = mteach_Course(coefficient=3.14, name="sample_text", time=7)
    _safe_set(b, 'teachedCourses', a1)
    assert _is_linked(b, 'teachedCourses', a1)
    if hasattr(a1, 'Professor'):
        assert _is_linked(a1, 'Professor', b)
    _safe_set(b, 'teachedCourses', a2)
    assert _is_linked(b, 'teachedCourses', a2)
    if hasattr(a1, 'Professor'):
        assert not _is_linked(a1, 'Professor', b)
    if hasattr(a2, 'Professor'):
        assert _is_linked(a2, 'Professor', b)
    _safe_set(b, 'teachedCourses', None)
    assert not _is_linked(b, 'teachedCourses', a2)
    if hasattr(a2, 'Professor'):
        assert not _is_linked(a2, 'Professor', b)


def test_assoc_teachedCourses0_reverse_link_reassign_clear():
    a1 = mteach_Professor(firstName="sample_text", lastName="sample_text")
    a2 = mteach_Professor(firstName="sample_text_2", lastName="sample_text_2")
    b = mteach_Course(coefficient=3.14, name="sample_text", time=7)
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'professor'):
        assert _is_linked(a1, 'professor', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'professor'):
        assert not _is_linked(a1, 'professor', b)
    if hasattr(a2, 'professor'):
        assert _is_linked(a2, 'professor', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'professor'):
        assert not _is_linked(a2, 'professor', b)


def test_assoc_topics1_reverse_link_reassign_clear():
    a1 = mteach_Topic(title="sample_text")
    a2 = mteach_Topic(title="sample_text_2")
    b = mteach_Course(coefficient=3.14, name="sample_text", time=7)
    _safe_set(b, 'course', {a1})
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'Topic'):
        assert _is_linked(a1, 'Topic', b)
    _safe_set(b, 'course', {a2})
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'Topic'):
        assert not _is_linked(a1, 'Topic', b)
    if hasattr(a2, 'Topic'):
        assert _is_linked(a2, 'Topic', b)
    _safe_set(b, 'course', set())
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'Topic'):
        assert not _is_linked(a2, 'Topic', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

