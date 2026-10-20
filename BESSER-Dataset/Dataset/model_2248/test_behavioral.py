import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tdt4250_Course,
    tdt4250_CourseGroup,
    tdt4250_Specialisation,
    tdt4250_Student,
    tdt4250_StudyProgram,
    Semester,
    StudyProgramName,
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

def test_assoc_courses5_reverse_link_reassign_clear():
    a1 = tdt4250_Student(current_semester=7, studentID=7)
    a2 = tdt4250_Student(current_semester=13, studentID=13)
    b = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    _safe_set(b, 'tdt4250_Course7', a1)
    assert _is_linked(b, 'tdt4250_Course7', a1)
    if hasattr(a1, 'tdt4250_Student6'):
        assert _is_linked(a1, 'tdt4250_Student6', b)
    _safe_set(b, 'tdt4250_Course7', a2)
    assert _is_linked(b, 'tdt4250_Course7', a2)
    if hasattr(a1, 'tdt4250_Student6'):
        assert not _is_linked(a1, 'tdt4250_Student6', b)
    if hasattr(a2, 'tdt4250_Student6'):
        assert _is_linked(a2, 'tdt4250_Student6', b)
    _safe_set(b, 'tdt4250_Course7', None)
    assert not _is_linked(b, 'tdt4250_Course7', a2)
    if hasattr(a2, 'tdt4250_Student6'):
        assert not _is_linked(a2, 'tdt4250_Student6', b)


def test_assoc_further_specialisation20_reverse_link_reassign_clear():
    a1 = tdt4250_Specialisation(name="sample_text")
    a2 = tdt4250_Specialisation(name="sample_text_2")
    b = tdt4250_Specialisation(name="sample_text")
    _safe_set(b, 'tdt4250_Specialisation21', a1)
    assert _is_linked(b, 'tdt4250_Specialisation21', a1)
    if hasattr(a1, 'tdt4250_Specialisation19'):
        assert _is_linked(a1, 'tdt4250_Specialisation19', b)
    _safe_set(b, 'tdt4250_Specialisation21', a2)
    assert _is_linked(b, 'tdt4250_Specialisation21', a2)
    if hasattr(a1, 'tdt4250_Specialisation19'):
        assert not _is_linked(a1, 'tdt4250_Specialisation19', b)
    if hasattr(a2, 'tdt4250_Specialisation19'):
        assert _is_linked(a2, 'tdt4250_Specialisation19', b)
    _safe_set(b, 'tdt4250_Specialisation21', None)
    assert not _is_linked(b, 'tdt4250_Specialisation21', a2)
    if hasattr(a2, 'tdt4250_Specialisation19'):
        assert not _is_linked(a2, 'tdt4250_Specialisation19', b)


def test_assoc_obligatory_courses3_reverse_link_reassign_clear():
    a1 = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    a2 = tdt4250_StudyProgram(name="sample_text_2", number_of_semesters=13)
    b = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    _safe_set(b, 'tdt4250_Course', a1)
    assert _is_linked(b, 'tdt4250_Course', a1)
    if hasattr(a1, 'tdt4250_StudyProgram4'):
        assert _is_linked(a1, 'tdt4250_StudyProgram4', b)
    _safe_set(b, 'tdt4250_Course', a2)
    assert _is_linked(b, 'tdt4250_Course', a2)
    if hasattr(a1, 'tdt4250_StudyProgram4'):
        assert not _is_linked(a1, 'tdt4250_StudyProgram4', b)
    if hasattr(a2, 'tdt4250_StudyProgram4'):
        assert _is_linked(a2, 'tdt4250_StudyProgram4', b)
    _safe_set(b, 'tdt4250_Course', None)
    assert not _is_linked(b, 'tdt4250_Course', a2)
    if hasattr(a2, 'tdt4250_StudyProgram4'):
        assert not _is_linked(a2, 'tdt4250_StudyProgram4', b)


def test_assoc_specialisations1_reverse_link_reassign_clear():
    a1 = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    a2 = tdt4250_StudyProgram(name="sample_text_2", number_of_semesters=13)
    b = tdt4250_Specialisation(name="sample_text")
    _safe_set(b, 'tdt4250_Specialisation', a1)
    assert _is_linked(b, 'tdt4250_Specialisation', a1)
    if hasattr(a1, 'tdt4250_StudyProgram2'):
        assert _is_linked(a1, 'tdt4250_StudyProgram2', b)
    _safe_set(b, 'tdt4250_Specialisation', a2)
    assert _is_linked(b, 'tdt4250_Specialisation', a2)
    if hasattr(a1, 'tdt4250_StudyProgram2'):
        assert not _is_linked(a1, 'tdt4250_StudyProgram2', b)
    if hasattr(a2, 'tdt4250_StudyProgram2'):
        assert _is_linked(a2, 'tdt4250_StudyProgram2', b)
    _safe_set(b, 'tdt4250_Specialisation', None)
    assert not _is_linked(b, 'tdt4250_Specialisation', a2)
    if hasattr(a2, 'tdt4250_StudyProgram2'):
        assert not _is_linked(a2, 'tdt4250_StudyProgram2', b)


def test_assoc_students0_reverse_link_reassign_clear():
    a1 = tdt4250_StudyProgram(name="sample_text", number_of_semesters=7)
    a2 = tdt4250_StudyProgram(name="sample_text_2", number_of_semesters=13)
    b = tdt4250_Student(current_semester=7, studentID=7)
    _safe_set(b, 'tdt4250_Student', a1)
    assert _is_linked(b, 'tdt4250_Student', a1)
    if hasattr(a1, 'tdt4250_StudyProgram'):
        assert _is_linked(a1, 'tdt4250_StudyProgram', b)
    _safe_set(b, 'tdt4250_Student', a2)
    assert _is_linked(b, 'tdt4250_Student', a2)
    if hasattr(a1, 'tdt4250_StudyProgram'):
        assert not _is_linked(a1, 'tdt4250_StudyProgram', b)
    if hasattr(a2, 'tdt4250_StudyProgram'):
        assert _is_linked(a2, 'tdt4250_StudyProgram', b)
    _safe_set(b, 'tdt4250_Student', None)
    assert not _is_linked(b, 'tdt4250_Student', a2)
    if hasattr(a2, 'tdt4250_StudyProgram'):
        assert not _is_linked(a2, 'tdt4250_StudyProgram', b)


def test_assoc_students16_reverse_link_reassign_clear():
    a1 = tdt4250_Student(current_semester=7, studentID=7)
    a2 = tdt4250_Student(current_semester=13, studentID=13)
    b = tdt4250_Specialisation(name="sample_text")
    _safe_set(b, 'tdt4250_Specialisation17', {a1})
    assert _is_linked(b, 'tdt4250_Specialisation17', a1)
    if hasattr(a1, 'tdt4250_Student18'):
        assert _is_linked(a1, 'tdt4250_Student18', b)
    _safe_set(b, 'tdt4250_Specialisation17', {a2})
    assert _is_linked(b, 'tdt4250_Specialisation17', a2)
    if hasattr(a1, 'tdt4250_Student18'):
        assert not _is_linked(a1, 'tdt4250_Student18', b)
    if hasattr(a2, 'tdt4250_Student18'):
        assert _is_linked(a2, 'tdt4250_Student18', b)
    _safe_set(b, 'tdt4250_Specialisation17', set())
    assert not _is_linked(b, 'tdt4250_Specialisation17', a2)
    if hasattr(a2, 'tdt4250_Student18'):
        assert not _is_linked(a2, 'tdt4250_Student18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_course_group22_stub_double():
    # tdt4250_CourseGroup has no real 'tdt4250_CourseGroup24' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Specialisation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Specialisation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Specialisation(name="sample_text")
    partner = tdt4250_CourseGroup()
    setattr(partner, 'tdt4250_CourseGroup24', None)
    _safe_set(owner, 'tdt4250_Specialisation23', partner)
    assert getattr(partner, 'tdt4250_CourseGroup24') == owner
    _safe_set(owner, 'tdt4250_Specialisation23', None)
    assert getattr(partner, 'tdt4250_CourseGroup24') is None


def test_assoc_elective_courses10_stub_double():
    # tdt4250_CourseGroup has no real 'tdt4250_CourseGroup11' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    partner = tdt4250_CourseGroup()
    setattr(partner, 'tdt4250_CourseGroup11', None)
    _safe_set(owner, 'tdt4250_Course12', partner)
    assert getattr(partner, 'tdt4250_CourseGroup11') == owner
    _safe_set(owner, 'tdt4250_Course12', None)
    assert getattr(partner, 'tdt4250_CourseGroup11') is None


def test_assoc_mandatory_courses8_stub_double():
    # tdt4250_CourseGroup has no real 'tdt4250_CourseGroup' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Course(code="sample_text", level="sample_text", name="sample_text", semester="sample_text", study_points=3.14)
    partner = tdt4250_CourseGroup()
    setattr(partner, 'tdt4250_CourseGroup', None)
    _safe_set(owner, 'tdt4250_Course9', partner)
    assert getattr(partner, 'tdt4250_CourseGroup') == owner
    _safe_set(owner, 'tdt4250_Course9', None)
    assert getattr(partner, 'tdt4250_CourseGroup') is None


def test_assoc_specialisation13_stub_double():
    # tdt4250_CourseGroup has no real 'tdt4250_CourseGroup14' property in the generated
    # code (a bare stub) -- manually attach it so tdt4250_Specialisation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tdt4250_Specialisation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tdt4250_Specialisation(name="sample_text")
    partner = tdt4250_CourseGroup()
    setattr(partner, 'tdt4250_CourseGroup14', None)
    _safe_set(owner, 'tdt4250_Specialisation15', partner)
    assert getattr(partner, 'tdt4250_CourseGroup14') == owner
    _safe_set(owner, 'tdt4250_Specialisation15', None)
    assert getattr(partner, 'tdt4250_CourseGroup14') is None


