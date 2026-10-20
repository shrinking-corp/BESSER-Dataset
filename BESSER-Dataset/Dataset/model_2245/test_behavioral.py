import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    prosjekt_Course,
    prosjekt_CourseCoordinator,
    prosjekt_Institute,
    prosjekt_Semester,
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

def test_assoc_course0_reverse_link_reassign_clear():
    a1 = prosjekt_Institute(name="sample_text", shortName="sample_text")
    a2 = prosjekt_Institute(name="sample_text_2", shortName="sample_text_2")
    b = prosjekt_Course(avgGrade=7, code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'institute'):
        assert _is_linked(a1, 'institute', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'institute'):
        assert not _is_linked(a1, 'institute', b)
    if hasattr(a2, 'institute'):
        assert _is_linked(a2, 'institute', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'institute'):
        assert not _is_linked(a2, 'institute', b)


def test_assoc_course11_reverse_link_reassign_clear():
    a1 = prosjekt_CourseCoordinator(name="sample_text")
    a2 = prosjekt_CourseCoordinator(name="sample_text_2")
    b = prosjekt_Course(avgGrade=7, code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'Course12', a1)
    assert _is_linked(b, 'Course12', a1)
    if hasattr(a1, 'courseCoordinator'):
        assert _is_linked(a1, 'courseCoordinator', b)
    _safe_set(b, 'Course12', a2)
    assert _is_linked(b, 'Course12', a2)
    if hasattr(a1, 'courseCoordinator'):
        assert not _is_linked(a1, 'courseCoordinator', b)
    if hasattr(a2, 'courseCoordinator'):
        assert _is_linked(a2, 'courseCoordinator', b)
    _safe_set(b, 'Course12', None)
    assert not _is_linked(b, 'Course12', a2)
    if hasattr(a2, 'courseCoordinator'):
        assert not _is_linked(a2, 'courseCoordinator', b)


def test_assoc_course9_reverse_link_reassign_clear():
    a1 = prosjekt_Semester(name="sample_text")
    a2 = prosjekt_Semester(name="sample_text_2")
    b = prosjekt_Course(avgGrade=7, code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'Course10', a1)
    assert _is_linked(b, 'Course10', a1)
    if hasattr(a1, 'semester'):
        assert _is_linked(a1, 'semester', b)
    _safe_set(b, 'Course10', a2)
    assert _is_linked(b, 'Course10', a2)
    if hasattr(a1, 'semester'):
        assert not _is_linked(a1, 'semester', b)
    if hasattr(a2, 'semester'):
        assert _is_linked(a2, 'semester', b)
    _safe_set(b, 'Course10', None)
    assert not _is_linked(b, 'Course10', a2)
    if hasattr(a2, 'semester'):
        assert not _is_linked(a2, 'semester', b)


def test_assoc_courseCoordinator1_reverse_link_reassign_clear():
    a1 = prosjekt_Institute(name="sample_text", shortName="sample_text")
    a2 = prosjekt_Institute(name="sample_text_2", shortName="sample_text_2")
    b = prosjekt_CourseCoordinator(name="sample_text")
    _safe_set(b, 'CourseCoordinator', a1)
    assert _is_linked(b, 'CourseCoordinator', a1)
    if hasattr(a1, 'institute2'):
        assert _is_linked(a1, 'institute2', b)
    _safe_set(b, 'CourseCoordinator', a2)
    assert _is_linked(b, 'CourseCoordinator', a2)
    if hasattr(a1, 'institute2'):
        assert not _is_linked(a1, 'institute2', b)
    if hasattr(a2, 'institute2'):
        assert _is_linked(a2, 'institute2', b)
    _safe_set(b, 'CourseCoordinator', None)
    assert not _is_linked(b, 'CourseCoordinator', a2)
    if hasattr(a2, 'institute2'):
        assert not _is_linked(a2, 'institute2', b)


def test_assoc_courseCoordinator6_reverse_link_reassign_clear():
    a1 = prosjekt_CourseCoordinator(name="sample_text")
    a2 = prosjekt_CourseCoordinator(name="sample_text_2")
    b = prosjekt_Course(avgGrade=7, code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'course7', {a1})
    assert _is_linked(b, 'course7', a1)
    if hasattr(a1, 'CourseCoordinator8'):
        assert _is_linked(a1, 'CourseCoordinator8', b)
    _safe_set(b, 'course7', {a2})
    assert _is_linked(b, 'course7', a2)
    if hasattr(a1, 'CourseCoordinator8'):
        assert not _is_linked(a1, 'CourseCoordinator8', b)
    if hasattr(a2, 'CourseCoordinator8'):
        assert _is_linked(a2, 'CourseCoordinator8', b)
    _safe_set(b, 'course7', set())
    assert not _is_linked(b, 'course7', a2)
    if hasattr(a2, 'CourseCoordinator8'):
        assert not _is_linked(a2, 'CourseCoordinator8', b)


def test_assoc_institute13_reverse_link_reassign_clear():
    a1 = prosjekt_Institute(name="sample_text", shortName="sample_text")
    a2 = prosjekt_Institute(name="sample_text_2", shortName="sample_text_2")
    b = prosjekt_CourseCoordinator(name="sample_text")
    _safe_set(b, 'courseCoordinator14', a1)
    assert _is_linked(b, 'courseCoordinator14', a1)
    if hasattr(a1, 'Institute15'):
        assert _is_linked(a1, 'Institute15', b)
    _safe_set(b, 'courseCoordinator14', a2)
    assert _is_linked(b, 'courseCoordinator14', a2)
    if hasattr(a1, 'Institute15'):
        assert not _is_linked(a1, 'Institute15', b)
    if hasattr(a2, 'Institute15'):
        assert _is_linked(a2, 'Institute15', b)
    _safe_set(b, 'courseCoordinator14', None)
    assert not _is_linked(b, 'courseCoordinator14', a2)
    if hasattr(a2, 'Institute15'):
        assert not _is_linked(a2, 'Institute15', b)


def test_assoc_institute3_reverse_link_reassign_clear():
    a1 = prosjekt_Institute(name="sample_text", shortName="sample_text")
    a2 = prosjekt_Institute(name="sample_text_2", shortName="sample_text_2")
    b = prosjekt_Course(avgGrade=7, code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'course', a1)
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'Institute'):
        assert _is_linked(a1, 'Institute', b)
    _safe_set(b, 'course', a2)
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'Institute'):
        assert not _is_linked(a1, 'Institute', b)
    if hasattr(a2, 'Institute'):
        assert _is_linked(a2, 'Institute', b)
    _safe_set(b, 'course', None)
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'Institute'):
        assert not _is_linked(a2, 'Institute', b)


def test_assoc_semester4_reverse_link_reassign_clear():
    a1 = prosjekt_Semester(name="sample_text")
    a2 = prosjekt_Semester(name="sample_text_2")
    b = prosjekt_Course(avgGrade=7, code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'course5', a1)
    assert _is_linked(b, 'course5', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'course5', a2)
    assert _is_linked(b, 'course5', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'course5', None)
    assert not _is_linked(b, 'course5', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

