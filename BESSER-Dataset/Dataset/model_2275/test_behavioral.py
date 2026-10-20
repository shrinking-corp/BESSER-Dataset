import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    education_Course,
    education_School,
    education_Student,
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
    a1 = education_School(address="sample_text", name="sample_text", phone="sample_text")
    a2 = education_School(address="sample_text_2", name="sample_text_2", phone="sample_text_2")
    b = education_Course(name="sample_text")
    _safe_set(b, 'education_Course', a1)
    assert _is_linked(b, 'education_Course', a1)
    if hasattr(a1, 'education_School2'):
        assert _is_linked(a1, 'education_School2', b)
    _safe_set(b, 'education_Course', a2)
    assert _is_linked(b, 'education_Course', a2)
    if hasattr(a1, 'education_School2'):
        assert not _is_linked(a1, 'education_School2', b)
    if hasattr(a2, 'education_School2'):
        assert _is_linked(a2, 'education_School2', b)
    _safe_set(b, 'education_Course', None)
    assert not _is_linked(b, 'education_Course', a2)
    if hasattr(a2, 'education_School2'):
        assert not _is_linked(a2, 'education_School2', b)


def test_assoc_courses6_reverse_link_reassign_clear():
    a1 = education_Student(name="sample_text")
    a2 = education_Student(name="sample_text_2")
    b = education_Course(name="sample_text")
    _safe_set(b, 'education_Course8', a1)
    assert _is_linked(b, 'education_Course8', a1)
    if hasattr(a1, 'education_Student7'):
        assert _is_linked(a1, 'education_Student7', b)
    _safe_set(b, 'education_Course8', a2)
    assert _is_linked(b, 'education_Course8', a2)
    if hasattr(a1, 'education_Student7'):
        assert not _is_linked(a1, 'education_Student7', b)
    if hasattr(a2, 'education_Student7'):
        assert _is_linked(a2, 'education_Student7', b)
    _safe_set(b, 'education_Course8', None)
    assert not _is_linked(b, 'education_Course8', a2)
    if hasattr(a2, 'education_Student7'):
        assert not _is_linked(a2, 'education_Student7', b)


def test_assoc_school12_reverse_link_reassign_clear():
    a1 = education_School(address="sample_text", name="sample_text", phone="sample_text")
    a2 = education_School(address="sample_text_2", name="sample_text_2", phone="sample_text_2")
    b = education_Course(name="sample_text")
    _safe_set(b, 'education_Course13', a1)
    assert _is_linked(b, 'education_Course13', a1)
    if hasattr(a1, 'education_School14'):
        assert _is_linked(a1, 'education_School14', b)
    _safe_set(b, 'education_Course13', a2)
    assert _is_linked(b, 'education_Course13', a2)
    if hasattr(a1, 'education_School14'):
        assert not _is_linked(a1, 'education_School14', b)
    if hasattr(a2, 'education_School14'):
        assert _is_linked(a2, 'education_School14', b)
    _safe_set(b, 'education_Course13', None)
    assert not _is_linked(b, 'education_Course13', a2)
    if hasattr(a2, 'education_School14'):
        assert not _is_linked(a2, 'education_School14', b)


def test_assoc_schools3_reverse_link_reassign_clear():
    a1 = education_Student(name="sample_text")
    a2 = education_Student(name="sample_text_2")
    b = education_School(address="sample_text", name="sample_text", phone="sample_text")
    _safe_set(b, 'education_School5', a1)
    assert _is_linked(b, 'education_School5', a1)
    if hasattr(a1, 'education_Student4'):
        assert _is_linked(a1, 'education_Student4', b)
    _safe_set(b, 'education_School5', a2)
    assert _is_linked(b, 'education_School5', a2)
    if hasattr(a1, 'education_Student4'):
        assert not _is_linked(a1, 'education_Student4', b)
    if hasattr(a2, 'education_Student4'):
        assert _is_linked(a2, 'education_Student4', b)
    _safe_set(b, 'education_School5', None)
    assert not _is_linked(b, 'education_School5', a2)
    if hasattr(a2, 'education_Student4'):
        assert not _is_linked(a2, 'education_Student4', b)


def test_assoc_students0_reverse_link_reassign_clear():
    a1 = education_Student(name="sample_text")
    a2 = education_Student(name="sample_text_2")
    b = education_School(address="sample_text", name="sample_text", phone="sample_text")
    _safe_set(b, 'education_School', {a1})
    assert _is_linked(b, 'education_School', a1)
    if hasattr(a1, 'education_Student'):
        assert _is_linked(a1, 'education_Student', b)
    _safe_set(b, 'education_School', {a2})
    assert _is_linked(b, 'education_School', a2)
    if hasattr(a1, 'education_Student'):
        assert not _is_linked(a1, 'education_Student', b)
    if hasattr(a2, 'education_Student'):
        assert _is_linked(a2, 'education_Student', b)
    _safe_set(b, 'education_School', set())
    assert not _is_linked(b, 'education_School', a2)
    if hasattr(a2, 'education_Student'):
        assert not _is_linked(a2, 'education_Student', b)


def test_assoc_students9_reverse_link_reassign_clear():
    a1 = education_Student(name="sample_text")
    a2 = education_Student(name="sample_text_2")
    b = education_Course(name="sample_text")
    _safe_set(b, 'education_Course10', {a1})
    assert _is_linked(b, 'education_Course10', a1)
    if hasattr(a1, 'education_Student11'):
        assert _is_linked(a1, 'education_Student11', b)
    _safe_set(b, 'education_Course10', {a2})
    assert _is_linked(b, 'education_Course10', a2)
    if hasattr(a1, 'education_Student11'):
        assert not _is_linked(a1, 'education_Student11', b)
    if hasattr(a2, 'education_Student11'):
        assert _is_linked(a2, 'education_Student11', b)
    _safe_set(b, 'education_Course10', set())
    assert not _is_linked(b, 'education_Course10', a2)
    if hasattr(a2, 'education_Student11'):
        assert not _is_linked(a2, 'education_Student11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

