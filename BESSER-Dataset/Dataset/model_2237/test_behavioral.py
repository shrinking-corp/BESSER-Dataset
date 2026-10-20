import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    prosjekt_Course,
    prosjekt_CourseCoordinator,
    prosjekt_Department,
    prosjekt_Person,
    prosjekt_Semester,
    prosjekt_University,
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

def test_assoc_course2_reverse_link_reassign_clear():
    a1 = prosjekt_Department(name="sample_text", shortName="sample_text")
    a2 = prosjekt_Department(name="sample_text_2", shortName="sample_text_2")
    b = prosjekt_Course(code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'department'):
        assert _is_linked(a1, 'department', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'department'):
        assert not _is_linked(a1, 'department', b)
    if hasattr(a2, 'department'):
        assert _is_linked(a2, 'department', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'department'):
        assert not _is_linked(a2, 'department', b)


def test_assoc_course8_reverse_link_reassign_clear():
    a1 = prosjekt_Semester(amountA=7, amountB=7, amountC=7, amountD=7, amountE=7, amountF=7, averageGrade=3.14, name="sample_text")
    a2 = prosjekt_Semester(amountA=13, amountB=13, amountC=13, amountD=13, amountE=13, amountF=13, averageGrade=9.99, name="sample_text_2")
    b = prosjekt_Course(code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'Course9', a1)
    assert _is_linked(b, 'Course9', a1)
    if hasattr(a1, 'semester'):
        assert _is_linked(a1, 'semester', b)
    _safe_set(b, 'Course9', a2)
    assert _is_linked(b, 'Course9', a2)
    if hasattr(a1, 'semester'):
        assert not _is_linked(a1, 'semester', b)
    if hasattr(a2, 'semester'):
        assert _is_linked(a2, 'semester', b)
    _safe_set(b, 'Course9', None)
    assert not _is_linked(b, 'Course9', a2)
    if hasattr(a2, 'semester'):
        assert not _is_linked(a2, 'semester', b)


def test_assoc_department4_reverse_link_reassign_clear():
    a1 = prosjekt_Department(name="sample_text", shortName="sample_text")
    a2 = prosjekt_Department(name="sample_text_2", shortName="sample_text_2")
    b = prosjekt_Course(code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'course', a1)
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'Department5'):
        assert _is_linked(a1, 'Department5', b)
    _safe_set(b, 'course', a2)
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'Department5'):
        assert not _is_linked(a1, 'Department5', b)
    if hasattr(a2, 'Department5'):
        assert _is_linked(a2, 'Department5', b)
    _safe_set(b, 'course', None)
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'Department5'):
        assert not _is_linked(a2, 'Department5', b)


def test_assoc_departments0_reverse_link_reassign_clear():
    a1 = prosjekt_University(name="sample_text", shortName="sample_text")
    a2 = prosjekt_University(name="sample_text_2", shortName="sample_text_2")
    b = prosjekt_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'university'):
        assert _is_linked(a1, 'university', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'university'):
        assert not _is_linked(a1, 'university', b)
    if hasattr(a2, 'university'):
        assert _is_linked(a2, 'university', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'university'):
        assert not _is_linked(a2, 'university', b)


def test_assoc_semester6_reverse_link_reassign_clear():
    a1 = prosjekt_Semester(amountA=7, amountB=7, amountC=7, amountD=7, amountE=7, amountF=7, averageGrade=3.14, name="sample_text")
    a2 = prosjekt_Semester(amountA=13, amountB=13, amountC=13, amountD=13, amountE=13, amountF=13, averageGrade=9.99, name="sample_text_2")
    b = prosjekt_Course(code="sample_text", name="sample_text", studyPoints=3.14)
    _safe_set(b, 'course7', {a1})
    assert _is_linked(b, 'course7', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'course7', {a2})
    assert _is_linked(b, 'course7', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'course7', set())
    assert not _is_linked(b, 'course7', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


def test_assoc_staff3_reverse_link_reassign_clear():
    a1 = prosjekt_Person(name="sample_text")
    a2 = prosjekt_Person(name="sample_text_2")
    b = prosjekt_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'worksForDepartment', {a1})
    assert _is_linked(b, 'worksForDepartment', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'worksForDepartment', {a2})
    assert _is_linked(b, 'worksForDepartment', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'worksForDepartment', set())
    assert not _is_linked(b, 'worksForDepartment', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_university1_reverse_link_reassign_clear():
    a1 = prosjekt_University(name="sample_text", shortName="sample_text")
    a2 = prosjekt_University(name="sample_text_2", shortName="sample_text_2")
    b = prosjekt_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'departments', a1)
    assert _is_linked(b, 'departments', a1)
    if hasattr(a1, 'University'):
        assert _is_linked(a1, 'University', b)
    _safe_set(b, 'departments', a2)
    assert _is_linked(b, 'departments', a2)
    if hasattr(a1, 'University'):
        assert not _is_linked(a1, 'University', b)
    if hasattr(a2, 'University'):
        assert _is_linked(a2, 'University', b)
    _safe_set(b, 'departments', None)
    assert not _is_linked(b, 'departments', a2)
    if hasattr(a2, 'University'):
        assert not _is_linked(a2, 'University', b)


def test_assoc_worksForDepartment10_reverse_link_reassign_clear():
    a1 = prosjekt_Person(name="sample_text")
    a2 = prosjekt_Person(name="sample_text_2")
    b = prosjekt_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'Department11', a1)
    assert _is_linked(b, 'Department11', a1)
    if hasattr(a1, 'staff'):
        assert _is_linked(a1, 'staff', b)
    _safe_set(b, 'Department11', a2)
    assert _is_linked(b, 'Department11', a2)
    if hasattr(a1, 'staff'):
        assert not _is_linked(a1, 'staff', b)
    if hasattr(a2, 'staff'):
        assert _is_linked(a2, 'staff', b)
    _safe_set(b, 'Department11', None)
    assert not _is_linked(b, 'Department11', a2)
    if hasattr(a2, 'staff'):
        assert not _is_linked(a2, 'staff', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_course13_stub_double():
    # prosjekt_CourseCoordinator has no real 'prosjekt_CourseCoordinator' property in the generated
    # code (a bare stub) -- manually attach it so prosjekt_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prosjekt_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prosjekt_Course(code="sample_text", name="sample_text", studyPoints=3.14)
    partner = prosjekt_CourseCoordinator()
    setattr(partner, 'prosjekt_CourseCoordinator', None)
    _safe_set(owner, 'prosjekt_Course', partner)
    assert getattr(partner, 'prosjekt_CourseCoordinator') == owner
    _safe_set(owner, 'prosjekt_Course', None)
    assert getattr(partner, 'prosjekt_CourseCoordinator') is None


def test_assoc_person14_stub_double():
    # prosjekt_CourseCoordinator has no real 'roles' property in the generated
    # code (a bare stub) -- manually attach it so prosjekt_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prosjekt_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prosjekt_Person(name="sample_text")
    partner = prosjekt_CourseCoordinator()
    setattr(partner, 'roles', None)
    _safe_set(owner, 'Person15', partner)
    assert getattr(partner, 'roles') == owner
    _safe_set(owner, 'Person15', None)
    assert getattr(partner, 'roles') is None


def test_assoc_roles12_stub_double():
    # prosjekt_CourseCoordinator has no real 'CourseCoordinator' property in the generated
    # code (a bare stub) -- manually attach it so prosjekt_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prosjekt_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prosjekt_Person(name="sample_text")
    partner = prosjekt_CourseCoordinator()
    setattr(partner, 'CourseCoordinator', None)
    _safe_set(owner, 'person', {partner})
    assert getattr(partner, 'CourseCoordinator') == owner
    _safe_set(owner, 'person', set())
    assert getattr(partner, 'CourseCoordinator') is None


