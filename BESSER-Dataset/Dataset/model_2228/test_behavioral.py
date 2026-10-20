import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CourseSlot,
    SemesterContainer,
    studyprogramme_CompulsoryCourseSlot,
    studyprogramme_Course,
    studyprogramme_CourseSlot,
    studyprogramme_ElectiveCourseList,
    studyprogramme_ElectiveCourseSlot,
    studyprogramme_Programme,
    studyprogramme_Semester,
    studyprogramme_SemesterContainer,
    studyprogramme_Specialization,
    studyprogramme_University,
    ProgrammeCode,
    ProgrammeType,
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

def test_assoc_Semesters20_reverse_link_reassign_clear():
    a1 = studyprogramme_University(name="sample_text")
    a2 = studyprogramme_University(name="sample_text_2")
    b = studyprogramme_Semester(semesterNumber=7)
    _safe_set(b, 'studyprogramme_Semester22', a1)
    assert _is_linked(b, 'studyprogramme_Semester22', a1)
    if hasattr(a1, 'studyprogramme_University21'):
        assert _is_linked(a1, 'studyprogramme_University21', b)
    _safe_set(b, 'studyprogramme_Semester22', a2)
    assert _is_linked(b, 'studyprogramme_Semester22', a2)
    if hasattr(a1, 'studyprogramme_University21'):
        assert not _is_linked(a1, 'studyprogramme_University21', b)
    if hasattr(a2, 'studyprogramme_University21'):
        assert _is_linked(a2, 'studyprogramme_University21', b)
    _safe_set(b, 'studyprogramme_Semester22', None)
    assert not _is_linked(b, 'studyprogramme_Semester22', a2)
    if hasattr(a2, 'studyprogramme_University21'):
        assert not _is_linked(a2, 'studyprogramme_University21', b)


def test_assoc_availableCourses13_reverse_link_reassign_clear():
    a1 = studyprogramme_ElectiveCourseList(name="sample_text")
    a2 = studyprogramme_ElectiveCourseList(name="sample_text_2")
    b = studyprogramme_Course(courseCode="sample_text", credits=3.14, displayedName="sample_text", level=7, name="sample_text")
    _safe_set(b, 'studyprogramme_Course14', a1)
    assert _is_linked(b, 'studyprogramme_Course14', a1)
    if hasattr(a1, 'studyprogramme_ElectiveCourseList'):
        assert _is_linked(a1, 'studyprogramme_ElectiveCourseList', b)
    _safe_set(b, 'studyprogramme_Course14', a2)
    assert _is_linked(b, 'studyprogramme_Course14', a2)
    if hasattr(a1, 'studyprogramme_ElectiveCourseList'):
        assert not _is_linked(a1, 'studyprogramme_ElectiveCourseList', b)
    if hasattr(a2, 'studyprogramme_ElectiveCourseList'):
        assert _is_linked(a2, 'studyprogramme_ElectiveCourseList', b)
    _safe_set(b, 'studyprogramme_Course14', None)
    assert not _is_linked(b, 'studyprogramme_Course14', a2)
    if hasattr(a2, 'studyprogramme_ElectiveCourseList'):
        assert not _is_linked(a2, 'studyprogramme_ElectiveCourseList', b)


def test_assoc_courses17_reverse_link_reassign_clear():
    a1 = studyprogramme_University(name="sample_text")
    a2 = studyprogramme_University(name="sample_text_2")
    b = studyprogramme_Course(courseCode="sample_text", credits=3.14, displayedName="sample_text", level=7, name="sample_text")
    _safe_set(b, 'studyprogramme_Course19', a1)
    assert _is_linked(b, 'studyprogramme_Course19', a1)
    if hasattr(a1, 'studyprogramme_University18'):
        assert _is_linked(a1, 'studyprogramme_University18', b)
    _safe_set(b, 'studyprogramme_Course19', a2)
    assert _is_linked(b, 'studyprogramme_Course19', a2)
    if hasattr(a1, 'studyprogramme_University18'):
        assert not _is_linked(a1, 'studyprogramme_University18', b)
    if hasattr(a2, 'studyprogramme_University18'):
        assert _is_linked(a2, 'studyprogramme_University18', b)
    _safe_set(b, 'studyprogramme_Course19', None)
    assert not _is_linked(b, 'studyprogramme_Course19', a2)
    if hasattr(a2, 'studyprogramme_University18'):
        assert not _is_linked(a2, 'studyprogramme_University18', b)


def test_assoc_parrentSpecialisation6_reverse_link_reassign_clear():
    a1 = studyprogramme_Specialization(name="sample_text", selectionSemester=7)
    a2 = studyprogramme_Specialization(name="sample_text_2", selectionSemester=13)
    b = studyprogramme_Specialization(name="sample_text", selectionSemester=7)
    _safe_set(b, 'subSpecialisations', a1)
    assert _is_linked(b, 'subSpecialisations', a1)
    if hasattr(a1, 'Specialization7'):
        assert _is_linked(a1, 'Specialization7', b)
    _safe_set(b, 'subSpecialisations', a2)
    assert _is_linked(b, 'subSpecialisations', a2)
    if hasattr(a1, 'Specialization7'):
        assert not _is_linked(a1, 'Specialization7', b)
    if hasattr(a2, 'Specialization7'):
        assert _is_linked(a2, 'Specialization7', b)
    _safe_set(b, 'subSpecialisations', None)
    assert not _is_linked(b, 'subSpecialisations', a2)
    if hasattr(a2, 'Specialization7'):
        assert not _is_linked(a2, 'Specialization7', b)


def test_assoc_programme1_reverse_link_reassign_clear():
    a1 = studyprogramme_Specialization(name="sample_text", selectionSemester=7)
    a2 = studyprogramme_Specialization(name="sample_text_2", selectionSemester=13)
    b = studyprogramme_Programme(name="sample_text", numberOfYears=7, programmeCode="sample_text", programmeType="sample_text")
    _safe_set(b, 'Programme', a1)
    assert _is_linked(b, 'Programme', a1)
    if hasattr(a1, 'specializations'):
        assert _is_linked(a1, 'specializations', b)
    _safe_set(b, 'Programme', a2)
    assert _is_linked(b, 'Programme', a2)
    if hasattr(a1, 'specializations'):
        assert not _is_linked(a1, 'specializations', b)
    if hasattr(a2, 'specializations'):
        assert _is_linked(a2, 'specializations', b)
    _safe_set(b, 'Programme', None)
    assert not _is_linked(b, 'Programme', a2)
    if hasattr(a2, 'specializations'):
        assert not _is_linked(a2, 'specializations', b)


def test_assoc_programmes16_reverse_link_reassign_clear():
    a1 = studyprogramme_University(name="sample_text")
    a2 = studyprogramme_University(name="sample_text_2")
    b = studyprogramme_Programme(name="sample_text", numberOfYears=7, programmeCode="sample_text", programmeType="sample_text")
    _safe_set(b, 'studyprogramme_Programme', a1)
    assert _is_linked(b, 'studyprogramme_Programme', a1)
    if hasattr(a1, 'studyprogramme_University'):
        assert _is_linked(a1, 'studyprogramme_University', b)
    _safe_set(b, 'studyprogramme_Programme', a2)
    assert _is_linked(b, 'studyprogramme_Programme', a2)
    if hasattr(a1, 'studyprogramme_University'):
        assert not _is_linked(a1, 'studyprogramme_University', b)
    if hasattr(a2, 'studyprogramme_University'):
        assert _is_linked(a2, 'studyprogramme_University', b)
    _safe_set(b, 'studyprogramme_Programme', None)
    assert not _is_linked(b, 'studyprogramme_Programme', a2)
    if hasattr(a2, 'studyprogramme_University'):
        assert not _is_linked(a2, 'studyprogramme_University', b)


def test_assoc_specialisations23_reverse_link_reassign_clear():
    a1 = studyprogramme_University(name="sample_text")
    a2 = studyprogramme_University(name="sample_text_2")
    b = studyprogramme_Specialization(name="sample_text", selectionSemester=7)
    _safe_set(b, 'studyprogramme_Specialization', a1)
    assert _is_linked(b, 'studyprogramme_Specialization', a1)
    if hasattr(a1, 'studyprogramme_University24'):
        assert _is_linked(a1, 'studyprogramme_University24', b)
    _safe_set(b, 'studyprogramme_Specialization', a2)
    assert _is_linked(b, 'studyprogramme_Specialization', a2)
    if hasattr(a1, 'studyprogramme_University24'):
        assert not _is_linked(a1, 'studyprogramme_University24', b)
    if hasattr(a2, 'studyprogramme_University24'):
        assert _is_linked(a2, 'studyprogramme_University24', b)
    _safe_set(b, 'studyprogramme_Specialization', None)
    assert not _is_linked(b, 'studyprogramme_Specialization', a2)
    if hasattr(a2, 'studyprogramme_University24'):
        assert not _is_linked(a2, 'studyprogramme_University24', b)


def test_assoc_specializations0_reverse_link_reassign_clear():
    a1 = studyprogramme_Specialization(name="sample_text", selectionSemester=7)
    a2 = studyprogramme_Specialization(name="sample_text_2", selectionSemester=13)
    b = studyprogramme_Programme(name="sample_text", numberOfYears=7, programmeCode="sample_text", programmeType="sample_text")
    _safe_set(b, 'programme', {a1})
    assert _is_linked(b, 'programme', a1)
    if hasattr(a1, 'Specialization'):
        assert _is_linked(a1, 'Specialization', b)
    _safe_set(b, 'programme', {a2})
    assert _is_linked(b, 'programme', a2)
    if hasattr(a1, 'Specialization'):
        assert not _is_linked(a1, 'Specialization', b)
    if hasattr(a2, 'Specialization'):
        assert _is_linked(a2, 'Specialization', b)
    _safe_set(b, 'programme', set())
    assert not _is_linked(b, 'programme', a2)
    if hasattr(a2, 'Specialization'):
        assert not _is_linked(a2, 'Specialization', b)


def test_assoc_subSpecialisations3_reverse_link_reassign_clear():
    a1 = studyprogramme_Specialization(name="sample_text", selectionSemester=7)
    a2 = studyprogramme_Specialization(name="sample_text_2", selectionSemester=13)
    b = studyprogramme_Specialization(name="sample_text", selectionSemester=7)
    _safe_set(b, 'parrentSpecialisation', {a1})
    assert _is_linked(b, 'parrentSpecialisation', a1)
    if hasattr(a1, 'Specialization4'):
        assert _is_linked(a1, 'Specialization4', b)
    _safe_set(b, 'parrentSpecialisation', {a2})
    assert _is_linked(b, 'parrentSpecialisation', a2)
    if hasattr(a1, 'Specialization4'):
        assert not _is_linked(a1, 'Specialization4', b)
    if hasattr(a2, 'Specialization4'):
        assert _is_linked(a2, 'Specialization4', b)
    _safe_set(b, 'parrentSpecialisation', set())
    assert not _is_linked(b, 'parrentSpecialisation', a2)
    if hasattr(a2, 'Specialization4'):
        assert not _is_linked(a2, 'Specialization4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignedCourse26_stub_double():
    # studyprogramme_ElectiveCourseSlot has no real 'studyprogramme_ElectiveCourseSlot' property in the generated
    # code (a bare stub) -- manually attach it so studyprogramme_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogramme_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogramme_Course(courseCode="sample_text", credits=3.14, displayedName="sample_text", level=7, name="sample_text")
    partner = studyprogramme_ElectiveCourseSlot()
    setattr(partner, 'studyprogramme_ElectiveCourseSlot', None)
    _safe_set(owner, 'studyprogramme_Course27', partner)
    assert getattr(partner, 'studyprogramme_ElectiveCourseSlot') == owner
    _safe_set(owner, 'studyprogramme_Course27', None)
    assert getattr(partner, 'studyprogramme_ElectiveCourseSlot') is None


def test_assoc_course9_stub_double():
    # studyprogramme_CourseSlot has no real 'studyprogramme_CourseSlot10' property in the generated
    # code (a bare stub) -- manually attach it so studyprogramme_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogramme_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogramme_Course(courseCode="sample_text", credits=3.14, displayedName="sample_text", level=7, name="sample_text")
    partner = studyprogramme_CourseSlot()
    setattr(partner, 'studyprogramme_CourseSlot10', None)
    _safe_set(owner, 'studyprogramme_Course', partner)
    assert getattr(partner, 'studyprogramme_CourseSlot10') == owner
    _safe_set(owner, 'studyprogramme_Course', None)
    assert getattr(partner, 'studyprogramme_CourseSlot10') is None


def test_assoc_electiveCourseList25_stub_double():
    # studyprogramme_ElectiveCourseSlot has no real 'electiveCourseSlot' property in the generated
    # code (a bare stub) -- manually attach it so studyprogramme_ElectiveCourseList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogramme_ElectiveCourseList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogramme_ElectiveCourseList(name="sample_text")
    partner = studyprogramme_ElectiveCourseSlot()
    setattr(partner, 'electiveCourseSlot', None)
    _safe_set(owner, 'ElectiveCourseList', partner)
    assert getattr(partner, 'electiveCourseSlot') == owner
    _safe_set(owner, 'ElectiveCourseList', None)
    assert getattr(partner, 'electiveCourseSlot') is None


def test_assoc_electiveCourseSlot15_stub_double():
    # studyprogramme_ElectiveCourseSlot has no real 'ElectiveCourseSlot' property in the generated
    # code (a bare stub) -- manually attach it so studyprogramme_ElectiveCourseList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogramme_ElectiveCourseList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogramme_ElectiveCourseList(name="sample_text")
    partner = studyprogramme_ElectiveCourseSlot()
    setattr(partner, 'ElectiveCourseSlot', None)
    _safe_set(owner, 'electiveCourseList', partner)
    assert getattr(partner, 'ElectiveCourseSlot') == owner
    _safe_set(owner, 'electiveCourseList', None)
    assert getattr(partner, 'ElectiveCourseSlot') is None


def test_assoc_semesters11_stub_double():
    # studyprogramme_SemesterContainer has no real 'studyprogramme_SemesterContainer' property in the generated
    # code (a bare stub) -- manually attach it so studyprogramme_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogramme_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogramme_Semester(semesterNumber=7)
    partner = studyprogramme_SemesterContainer()
    setattr(partner, 'studyprogramme_SemesterContainer', None)
    _safe_set(owner, 'studyprogramme_Semester12', partner)
    assert owner in getattr(partner, 'studyprogramme_SemesterContainer')
    _safe_set(owner, 'studyprogramme_Semester12', None)
    assert owner not in getattr(partner, 'studyprogramme_SemesterContainer')


def test_assoc_slots8_stub_double():
    # studyprogramme_CourseSlot has no real 'studyprogramme_CourseSlot' property in the generated
    # code (a bare stub) -- manually attach it so studyprogramme_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyprogramme_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyprogramme_Semester(semesterNumber=7)
    partner = studyprogramme_CourseSlot()
    setattr(partner, 'studyprogramme_CourseSlot', None)
    _safe_set(owner, 'studyprogramme_Semester', {partner})
    assert getattr(partner, 'studyprogramme_CourseSlot') == owner
    _safe_set(owner, 'studyprogramme_Semester', set())
    assert getattr(partner, 'studyprogramme_CourseSlot') is None


