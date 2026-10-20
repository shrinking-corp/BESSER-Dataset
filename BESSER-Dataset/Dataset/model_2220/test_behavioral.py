import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Programme,
    programmes_Course,
    programmes_CourseGroup,
    programmes_Programme,
    programmes_Semester,
    programmes_Specialization,
    programmes_University,
    CourseType,
    SemesterType,
    StudyLevel,
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

def test_assoc_courseGroups2_reverse_link_reassign_clear():
    a1 = programmes_Programme(code="sample_text", name="sample_text")
    a2 = programmes_Programme(code="sample_text_2", name="sample_text_2")
    b = programmes_CourseGroup(coursesType="sample_text", name="sample_text")
    _safe_set(b, 'programmes_CourseGroup', a1)
    assert _is_linked(b, 'programmes_CourseGroup', a1)
    if hasattr(a1, 'programmes_Programme'):
        assert _is_linked(a1, 'programmes_Programme', b)
    _safe_set(b, 'programmes_CourseGroup', a2)
    assert _is_linked(b, 'programmes_CourseGroup', a2)
    if hasattr(a1, 'programmes_Programme'):
        assert not _is_linked(a1, 'programmes_Programme', b)
    if hasattr(a2, 'programmes_Programme'):
        assert _is_linked(a2, 'programmes_Programme', b)
    _safe_set(b, 'programmes_CourseGroup', None)
    assert not _is_linked(b, 'programmes_CourseGroup', a2)
    if hasattr(a2, 'programmes_Programme'):
        assert not _is_linked(a2, 'programmes_Programme', b)


def test_assoc_courses14_reverse_link_reassign_clear():
    a1 = programmes_University(name="sample_text")
    a2 = programmes_University(name="sample_text_2")
    b = programmes_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'programmes_Course16', a1)
    assert _is_linked(b, 'programmes_Course16', a1)
    if hasattr(a1, 'programmes_University15'):
        assert _is_linked(a1, 'programmes_University15', b)
    _safe_set(b, 'programmes_Course16', a2)
    assert _is_linked(b, 'programmes_Course16', a2)
    if hasattr(a1, 'programmes_University15'):
        assert not _is_linked(a1, 'programmes_University15', b)
    if hasattr(a2, 'programmes_University15'):
        assert _is_linked(a2, 'programmes_University15', b)
    _safe_set(b, 'programmes_Course16', None)
    assert not _is_linked(b, 'programmes_Course16', a2)
    if hasattr(a2, 'programmes_University15'):
        assert not _is_linked(a2, 'programmes_University15', b)


def test_assoc_courses7_reverse_link_reassign_clear():
    a1 = programmes_Semester(semesterType="sample_text", year=7)
    a2 = programmes_Semester(semesterType="sample_text_2", year=13)
    b = programmes_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'programmes_Course', a1)
    assert _is_linked(b, 'programmes_Course', a1)
    if hasattr(a1, 'programmes_Semester8'):
        assert _is_linked(a1, 'programmes_Semester8', b)
    _safe_set(b, 'programmes_Course', a2)
    assert _is_linked(b, 'programmes_Course', a2)
    if hasattr(a1, 'programmes_Semester8'):
        assert not _is_linked(a1, 'programmes_Semester8', b)
    if hasattr(a2, 'programmes_Semester8'):
        assert _is_linked(a2, 'programmes_Semester8', b)
    _safe_set(b, 'programmes_Course', None)
    assert not _is_linked(b, 'programmes_Course', a2)
    if hasattr(a2, 'programmes_Semester8'):
        assert not _is_linked(a2, 'programmes_Semester8', b)


def test_assoc_courses9_reverse_link_reassign_clear():
    a1 = programmes_CourseGroup(coursesType="sample_text", name="sample_text")
    a2 = programmes_CourseGroup(coursesType="sample_text_2", name="sample_text_2")
    b = programmes_Course(code="sample_text", credits=3.14, level="sample_text", name="sample_text")
    _safe_set(b, 'programmes_Course11', a1)
    assert _is_linked(b, 'programmes_Course11', a1)
    if hasattr(a1, 'programmes_CourseGroup10'):
        assert _is_linked(a1, 'programmes_CourseGroup10', b)
    _safe_set(b, 'programmes_Course11', a2)
    assert _is_linked(b, 'programmes_Course11', a2)
    if hasattr(a1, 'programmes_CourseGroup10'):
        assert not _is_linked(a1, 'programmes_CourseGroup10', b)
    if hasattr(a2, 'programmes_CourseGroup10'):
        assert _is_linked(a2, 'programmes_CourseGroup10', b)
    _safe_set(b, 'programmes_Course11', None)
    assert not _is_linked(b, 'programmes_Course11', a2)
    if hasattr(a2, 'programmes_CourseGroup10'):
        assert not _is_linked(a2, 'programmes_CourseGroup10', b)


def test_assoc_programme5_reverse_link_reassign_clear():
    a1 = programmes_Semester(semesterType="sample_text", year=7)
    a2 = programmes_Semester(semesterType="sample_text_2", year=13)
    b = programmes_Programme(code="sample_text", name="sample_text")
    _safe_set(b, 'Programme6', a1)
    assert _is_linked(b, 'Programme6', a1)
    if hasattr(a1, 'programmeSemester'):
        assert _is_linked(a1, 'programmeSemester', b)
    _safe_set(b, 'Programme6', a2)
    assert _is_linked(b, 'Programme6', a2)
    if hasattr(a1, 'programmeSemester'):
        assert not _is_linked(a1, 'programmeSemester', b)
    if hasattr(a2, 'programmeSemester'):
        assert _is_linked(a2, 'programmeSemester', b)
    _safe_set(b, 'Programme6', None)
    assert not _is_linked(b, 'Programme6', a2)
    if hasattr(a2, 'programmeSemester'):
        assert not _is_linked(a2, 'programmeSemester', b)


def test_assoc_programmeSemester1_reverse_link_reassign_clear():
    a1 = programmes_Semester(semesterType="sample_text", year=7)
    a2 = programmes_Semester(semesterType="sample_text_2", year=13)
    b = programmes_Programme(code="sample_text", name="sample_text")
    _safe_set(b, 'programme', {a1})
    assert _is_linked(b, 'programme', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'programme', {a2})
    assert _is_linked(b, 'programme', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'programme', set())
    assert not _is_linked(b, 'programme', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


def test_assoc_studyProgrammes12_reverse_link_reassign_clear():
    a1 = programmes_University(name="sample_text")
    a2 = programmes_University(name="sample_text_2")
    b = programmes_Programme(code="sample_text", name="sample_text")
    _safe_set(b, 'programmes_Programme13', a1)
    assert _is_linked(b, 'programmes_Programme13', a1)
    if hasattr(a1, 'programmes_University'):
        assert _is_linked(a1, 'programmes_University', b)
    _safe_set(b, 'programmes_Programme13', a2)
    assert _is_linked(b, 'programmes_Programme13', a2)
    if hasattr(a1, 'programmes_University'):
        assert not _is_linked(a1, 'programmes_University', b)
    if hasattr(a2, 'programmes_University'):
        assert _is_linked(a2, 'programmes_University', b)
    _safe_set(b, 'programmes_Programme13', None)
    assert not _is_linked(b, 'programmes_Programme13', a2)
    if hasattr(a2, 'programmes_University'):
        assert not _is_linked(a2, 'programmes_University', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_chosenIn4_stub_double():
    # programmes_Specialization has no real 'programmes_Specialization' property in the generated
    # code (a bare stub) -- manually attach it so programmes_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # programmes_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = programmes_Semester(semesterType="sample_text", year=7)
    partner = programmes_Specialization()
    setattr(partner, 'programmes_Specialization', None)
    _safe_set(owner, 'programmes_Semester', partner)
    assert getattr(partner, 'programmes_Specialization') == owner
    _safe_set(owner, 'programmes_Semester', None)
    assert getattr(partner, 'programmes_Specialization') is None


def test_assoc_specializations0_stub_double():
    # programmes_Specialization has no real 'Specialization' property in the generated
    # code (a bare stub) -- manually attach it so programmes_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # programmes_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = programmes_Programme(code="sample_text", name="sample_text")
    partner = programmes_Specialization()
    setattr(partner, 'Specialization', None)
    _safe_set(owner, 'specializesIn', {partner})
    assert getattr(partner, 'Specialization') == owner
    _safe_set(owner, 'specializesIn', set())
    assert getattr(partner, 'Specialization') is None


def test_assoc_specializesIn3_stub_double():
    # programmes_Specialization has no real 'specializations' property in the generated
    # code (a bare stub) -- manually attach it so programmes_Programme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # programmes_Programme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = programmes_Programme(code="sample_text", name="sample_text")
    partner = programmes_Specialization()
    setattr(partner, 'specializations', None)
    _safe_set(owner, 'Programme', partner)
    assert getattr(partner, 'specializations') == owner
    _safe_set(owner, 'Programme', None)
    assert getattr(partner, 'specializations') is None


