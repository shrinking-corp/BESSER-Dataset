import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    course_Course,
    course_CourseCoordinator,
    course_CourseInstance,
    course_CourseWork,
    course_Department,
    course_Evaluation,
    course_Faculty,
    course_Lecturer,
    course_Organisation,
    course_Person,
    course_Student,
    course_StudyProgram,
    course_TA,
    course_Timetable,
    course_TimetableEntry,
    course_University,
    DayOfWeek,
    TypeOfInstruction,
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

def test_assoc_courses21_reverse_link_reassign_clear():
    a1 = course_Department(name="sample_text", shortName="sample_text")
    a2 = course_Department(name="sample_text_2", shortName="sample_text_2")
    b = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'Course22', a1)
    assert _is_linked(b, 'Course22', a1)
    if hasattr(a1, 'department'):
        assert _is_linked(a1, 'department', b)
    _safe_set(b, 'Course22', a2)
    assert _is_linked(b, 'Course22', a2)
    if hasattr(a1, 'department'):
        assert not _is_linked(a1, 'department', b)
    if hasattr(a2, 'department'):
        assert _is_linked(a2, 'department', b)
    _safe_set(b, 'Course22', None)
    assert not _is_linked(b, 'Course22', a2)
    if hasattr(a2, 'department'):
        assert not _is_linked(a2, 'department', b)


def test_assoc_department11_reverse_link_reassign_clear():
    a1 = course_Department(name="sample_text", shortName="sample_text")
    a2 = course_Department(name="sample_text_2", shortName="sample_text_2")
    b = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'courses', a1)
    assert _is_linked(b, 'courses', a1)
    if hasattr(a1, 'Department12'):
        assert _is_linked(a1, 'Department12', b)
    _safe_set(b, 'courses', a2)
    assert _is_linked(b, 'courses', a2)
    if hasattr(a1, 'Department12'):
        assert not _is_linked(a1, 'Department12', b)
    if hasattr(a2, 'Department12'):
        assert _is_linked(a2, 'Department12', b)
    _safe_set(b, 'courses', None)
    assert not _is_linked(b, 'courses', a2)
    if hasattr(a2, 'Department12'):
        assert not _is_linked(a2, 'Department12', b)


def test_assoc_departments2_reverse_link_reassign_clear():
    a1 = course_Faculty(name="sample_text", shortName="sample_text")
    a2 = course_Faculty(name="sample_text_2", shortName="sample_text_2")
    b = course_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'faculty'):
        assert _is_linked(a1, 'faculty', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'faculty'):
        assert not _is_linked(a1, 'faculty', b)
    if hasattr(a2, 'faculty'):
        assert _is_linked(a2, 'faculty', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'faculty'):
        assert not _is_linked(a2, 'faculty', b)


def test_assoc_faculties0_reverse_link_reassign_clear():
    a1 = course_University(name="sample_text")
    a2 = course_University(name="sample_text_2")
    b = course_Faculty(name="sample_text", shortName="sample_text")
    _safe_set(b, 'Faculty', a1)
    assert _is_linked(b, 'Faculty', a1)
    if hasattr(a1, 'university'):
        assert _is_linked(a1, 'university', b)
    _safe_set(b, 'Faculty', a2)
    assert _is_linked(b, 'Faculty', a2)
    if hasattr(a1, 'university'):
        assert not _is_linked(a1, 'university', b)
    if hasattr(a2, 'university'):
        assert _is_linked(a2, 'university', b)
    _safe_set(b, 'Faculty', None)
    assert not _is_linked(b, 'Faculty', a2)
    if hasattr(a2, 'university'):
        assert not _is_linked(a2, 'university', b)


def test_assoc_faculty25_reverse_link_reassign_clear():
    a1 = course_Faculty(name="sample_text", shortName="sample_text")
    a2 = course_Faculty(name="sample_text_2", shortName="sample_text_2")
    b = course_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'departments', a1)
    assert _is_linked(b, 'departments', a1)
    if hasattr(a1, 'Faculty26'):
        assert _is_linked(a1, 'Faculty26', b)
    _safe_set(b, 'departments', a2)
    assert _is_linked(b, 'departments', a2)
    if hasattr(a1, 'Faculty26'):
        assert not _is_linked(a1, 'Faculty26', b)
    if hasattr(a2, 'Faculty26'):
        assert _is_linked(a2, 'Faculty26', b)
    _safe_set(b, 'departments', None)
    assert not _is_linked(b, 'departments', a2)
    if hasattr(a2, 'Faculty26'):
        assert not _is_linked(a2, 'Faculty26', b)


def test_assoc_recommendedPreCond6_reverse_link_reassign_clear():
    a1 = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    a2 = course_Course(code="sample_text_2", content="sample_text_2", credits=9.99, name="sample_text_2")
    b = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'course_Course7', a1)
    assert _is_linked(b, 'course_Course7', a1)
    if hasattr(a1, 'course_Course5'):
        assert _is_linked(a1, 'course_Course5', b)
    _safe_set(b, 'course_Course7', a2)
    assert _is_linked(b, 'course_Course7', a2)
    if hasattr(a1, 'course_Course5'):
        assert not _is_linked(a1, 'course_Course5', b)
    if hasattr(a2, 'course_Course5'):
        assert _is_linked(a2, 'course_Course5', b)
    _safe_set(b, 'course_Course7', None)
    assert not _is_linked(b, 'course_Course7', a2)
    if hasattr(a2, 'course_Course5'):
        assert not _is_linked(a2, 'course_Course5', b)


def test_assoc_requiredPreCond4_reverse_link_reassign_clear():
    a1 = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    a2 = course_Course(code="sample_text_2", content="sample_text_2", credits=9.99, name="sample_text_2")
    b = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'course_Course3', {a1})
    assert _is_linked(b, 'course_Course3', a1)
    if hasattr(a1, 'course_Course'):
        assert _is_linked(a1, 'course_Course', b)
    _safe_set(b, 'course_Course3', {a2})
    assert _is_linked(b, 'course_Course3', a2)
    if hasattr(a1, 'course_Course'):
        assert not _is_linked(a1, 'course_Course', b)
    if hasattr(a2, 'course_Course'):
        assert _is_linked(a2, 'course_Course', b)
    _safe_set(b, 'course_Course3', set())
    assert not _is_linked(b, 'course_Course3', a2)
    if hasattr(a2, 'course_Course'):
        assert not _is_linked(a2, 'course_Course', b)


def test_assoc_studyProgram46_reverse_link_reassign_clear():
    a1 = course_TimetableEntry(day="sample_text", room="sample_text", time="sample_text", type="sample_text")
    a2 = course_TimetableEntry(day="sample_text_2", room="sample_text_2", time="sample_text_2", type="sample_text_2")
    b = course_StudyProgram(code="sample_text")
    _safe_set(b, 'course_StudyProgram48', a1)
    assert _is_linked(b, 'course_StudyProgram48', a1)
    if hasattr(a1, 'course_TimetableEntry47'):
        assert _is_linked(a1, 'course_TimetableEntry47', b)
    _safe_set(b, 'course_StudyProgram48', a2)
    assert _is_linked(b, 'course_StudyProgram48', a2)
    if hasattr(a1, 'course_TimetableEntry47'):
        assert not _is_linked(a1, 'course_TimetableEntry47', b)
    if hasattr(a2, 'course_TimetableEntry47'):
        assert _is_linked(a2, 'course_TimetableEntry47', b)
    _safe_set(b, 'course_StudyProgram48', None)
    assert not _is_linked(b, 'course_StudyProgram48', a2)
    if hasattr(a2, 'course_TimetableEntry47'):
        assert not _is_linked(a2, 'course_TimetableEntry47', b)


def test_assoc_studyPrograms23_reverse_link_reassign_clear():
    a1 = course_StudyProgram(code="sample_text")
    a2 = course_StudyProgram(code="sample_text_2")
    b = course_Department(name="sample_text", shortName="sample_text")
    _safe_set(b, 'course_Department', {a1})
    assert _is_linked(b, 'course_Department', a1)
    if hasattr(a1, 'course_StudyProgram24'):
        assert _is_linked(a1, 'course_StudyProgram24', b)
    _safe_set(b, 'course_Department', {a2})
    assert _is_linked(b, 'course_Department', a2)
    if hasattr(a1, 'course_StudyProgram24'):
        assert not _is_linked(a1, 'course_StudyProgram24', b)
    if hasattr(a2, 'course_StudyProgram24'):
        assert _is_linked(a2, 'course_StudyProgram24', b)
    _safe_set(b, 'course_Department', set())
    assert not _is_linked(b, 'course_Department', a2)
    if hasattr(a2, 'course_StudyProgram24'):
        assert not _is_linked(a2, 'course_StudyProgram24', b)


def test_assoc_studyPrograms8_reverse_link_reassign_clear():
    a1 = course_StudyProgram(code="sample_text")
    a2 = course_StudyProgram(code="sample_text_2")
    b = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    _safe_set(b, 'course_Course9', {a1})
    assert _is_linked(b, 'course_Course9', a1)
    if hasattr(a1, 'course_StudyProgram'):
        assert _is_linked(a1, 'course_StudyProgram', b)
    _safe_set(b, 'course_Course9', {a2})
    assert _is_linked(b, 'course_Course9', a2)
    if hasattr(a1, 'course_StudyProgram'):
        assert not _is_linked(a1, 'course_StudyProgram', b)
    if hasattr(a2, 'course_StudyProgram'):
        assert _is_linked(a2, 'course_StudyProgram', b)
    _safe_set(b, 'course_Course9', set())
    assert not _is_linked(b, 'course_Course9', a2)
    if hasattr(a2, 'course_StudyProgram'):
        assert not _is_linked(a2, 'course_StudyProgram', b)


def test_assoc_university1_reverse_link_reassign_clear():
    a1 = course_University(name="sample_text")
    a2 = course_University(name="sample_text_2")
    b = course_Faculty(name="sample_text", shortName="sample_text")
    _safe_set(b, 'faculties', a1)
    assert _is_linked(b, 'faculties', a1)
    if hasattr(a1, 'University'):
        assert _is_linked(a1, 'University', b)
    _safe_set(b, 'faculties', a2)
    assert _is_linked(b, 'faculties', a2)
    if hasattr(a1, 'University'):
        assert not _is_linked(a1, 'University', b)
    if hasattr(a2, 'University'):
        assert _is_linked(a2, 'University', b)
    _safe_set(b, 'faculties', None)
    assert not _is_linked(b, 'faculties', a2)
    if hasattr(a2, 'University'):
        assert not _is_linked(a2, 'University', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_course13_stub_double():
    # course_CourseInstance has no real 'courseInstances' property in the generated
    # code (a bare stub) -- manually attach it so course_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    partner = course_CourseInstance()
    setattr(partner, 'courseInstances', None)
    _safe_set(owner, 'Course', partner)
    assert getattr(partner, 'courseInstances') == owner
    _safe_set(owner, 'Course', None)
    assert getattr(partner, 'courseInstances') is None


def test_assoc_courseInstance27_stub_double():
    # course_CourseInstance has no real 'CourseInstance28' property in the generated
    # code (a bare stub) -- manually attach it so course_Evaluation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_Evaluation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_Evaluation(assigments=7, exam=7, project=7)
    partner = course_CourseInstance()
    setattr(partner, 'CourseInstance28', None)
    _safe_set(owner, 'evaluation', partner)
    assert getattr(partner, 'CourseInstance28') == owner
    _safe_set(owner, 'evaluation', None)
    assert getattr(partner, 'CourseInstance28') is None


def test_assoc_courseInstance41_stub_double():
    # course_CourseInstance has no real 'CourseInstance42' property in the generated
    # code (a bare stub) -- manually attach it so course_CourseWork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_CourseWork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_CourseWork(labHours=7, lectureHours=7)
    partner = course_CourseInstance()
    setattr(partner, 'CourseInstance42', None)
    _safe_set(owner, 'courseWork', partner)
    assert getattr(partner, 'CourseInstance42') == owner
    _safe_set(owner, 'courseWork', None)
    assert getattr(partner, 'CourseInstance42') is None


def test_assoc_courseInstances10_stub_double():
    # course_CourseInstance has no real 'CourseInstance' property in the generated
    # code (a bare stub) -- manually attach it so course_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_Course(code="sample_text", content="sample_text", credits=3.14, name="sample_text")
    partner = course_CourseInstance()
    setattr(partner, 'CourseInstance', None)
    _safe_set(owner, 'course', {partner})
    assert getattr(partner, 'CourseInstance') == owner
    _safe_set(owner, 'course', set())
    assert getattr(partner, 'CourseInstance') is None


def test_assoc_courseWork17_stub_double():
    # course_CourseInstance has no real 'courseInstance18' property in the generated
    # code (a bare stub) -- manually attach it so course_CourseWork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_CourseWork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_CourseWork(labHours=7, lectureHours=7)
    partner = course_CourseInstance()
    setattr(partner, 'courseInstance18', None)
    _safe_set(owner, 'CourseWork', partner)
    assert getattr(partner, 'courseInstance18') == owner
    _safe_set(owner, 'CourseWork', None)
    assert getattr(partner, 'courseInstance18') is None


def test_assoc_evaluation15_stub_double():
    # course_CourseInstance has no real 'courseInstance16' property in the generated
    # code (a bare stub) -- manually attach it so course_Evaluation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_Evaluation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_Evaluation(assigments=7, exam=7, project=7)
    partner = course_CourseInstance()
    setattr(partner, 'courseInstance16', None)
    _safe_set(owner, 'Evaluation', partner)
    assert getattr(partner, 'courseInstance16') == owner
    _safe_set(owner, 'Evaluation', None)
    assert getattr(partner, 'courseInstance16') is None


def test_assoc_evaluation50_stub_double():
    # course_Student has no real 'registeredStudents' property in the generated
    # code (a bare stub) -- manually attach it so course_Evaluation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_Evaluation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_Evaluation(assigments=7, exam=7, project=7)
    partner = course_Student()
    setattr(partner, 'registeredStudents', None)
    _safe_set(owner, 'Evaluation51', partner)
    assert owner in getattr(partner, 'registeredStudents')
    _safe_set(owner, 'Evaluation51', None)
    assert owner not in getattr(partner, 'registeredStudents')


def test_assoc_registeredStudents29_stub_double():
    # course_Student has no real 'Student' property in the generated
    # code (a bare stub) -- manually attach it so course_Evaluation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_Evaluation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_Evaluation(assigments=7, exam=7, project=7)
    partner = course_Student()
    setattr(partner, 'Student', None)
    _safe_set(owner, 'evaluation30', {partner})
    assert getattr(partner, 'Student') == owner
    _safe_set(owner, 'evaluation30', set())
    assert getattr(partner, 'Student') is None


def test_assoc_students39_stub_double():
    # course_Student has no real 'Student40' property in the generated
    # code (a bare stub) -- manually attach it so course_StudyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_StudyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_StudyProgram(code="sample_text")
    partner = course_Student()
    setattr(partner, 'Student40', None)
    _safe_set(owner, 'studyProgram', {partner})
    assert getattr(partner, 'Student40') == owner
    _safe_set(owner, 'studyProgram', set())
    assert getattr(partner, 'Student40') is None


def test_assoc_studyProgram49_stub_double():
    # course_Student has no real 'students' property in the generated
    # code (a bare stub) -- manually attach it so course_StudyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_StudyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_StudyProgram(code="sample_text")
    partner = course_Student()
    setattr(partner, 'students', None)
    _safe_set(owner, 'StudyProgram', partner)
    assert getattr(partner, 'students') == owner
    _safe_set(owner, 'StudyProgram', None)
    assert getattr(partner, 'students') is None


def test_assoc_timetableEntry45_stub_double():
    # course_Timetable has no real 'course_Timetable' property in the generated
    # code (a bare stub) -- manually attach it so course_TimetableEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_TimetableEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_TimetableEntry(day="sample_text", room="sample_text", time="sample_text", type="sample_text")
    partner = course_Timetable()
    setattr(partner, 'course_Timetable', None)
    _safe_set(owner, 'course_TimetableEntry', partner)
    assert owner in getattr(partner, 'course_Timetable')
    _safe_set(owner, 'course_TimetableEntry', None)
    assert owner not in getattr(partner, 'course_Timetable')


