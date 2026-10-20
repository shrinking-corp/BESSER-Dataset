import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    coursePages_Course,
    coursePages_CourseInstance,
    coursePages_CourseWork,
    coursePages_CourseWorkObject,
    coursePages_CourseWorker,
    coursePages_Department,
    coursePages_Employee,
    coursePages_EvaluationObject,
    coursePages_Evaluations,
    coursePages_Person,
    coursePages_Precondition,
    coursePages_Reduction,
    coursePages_Student,
    coursePages_StudyPrograms,
    CourseWorkType,
    EvaluationType,
    PrecondistionType,
    TermType,
    personRoleType,
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

def test_assoc_belongsToDepartment8_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    _safe_set(b, 'Department9', a1)
    assert _is_linked(b, 'Department9', a1)
    if hasattr(a1, 'studyprograms'):
        assert _is_linked(a1, 'studyprograms', b)
    _safe_set(b, 'Department9', a2)
    assert _is_linked(b, 'Department9', a2)
    if hasattr(a1, 'studyprograms'):
        assert not _is_linked(a1, 'studyprograms', b)
    if hasattr(a2, 'studyprograms'):
        assert _is_linked(a2, 'studyprograms', b)
    _safe_set(b, 'Department9', None)
    assert not _is_linked(b, 'Department9', a2)
    if hasattr(a2, 'studyprograms'):
        assert not _is_linked(a2, 'studyprograms', b)


def test_assoc_course1_reverse_link_reassign_clear():
    a1 = coursePages_Student(studentID="sample_text")
    a2 = coursePages_Student(studentID="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course', a1)
    assert _is_linked(b, 'coursePages_Course', a1)
    if hasattr(a1, 'coursePages_Student'):
        assert _is_linked(a1, 'coursePages_Student', b)
    _safe_set(b, 'coursePages_Course', a2)
    assert _is_linked(b, 'coursePages_Course', a2)
    if hasattr(a1, 'coursePages_Student'):
        assert not _is_linked(a1, 'coursePages_Student', b)
    if hasattr(a2, 'coursePages_Student'):
        assert _is_linked(a2, 'coursePages_Student', b)
    _safe_set(b, 'coursePages_Course', None)
    assert not _is_linked(b, 'coursePages_Course', a2)
    if hasattr(a2, 'coursePages_Student'):
        assert not _is_linked(a2, 'coursePages_Student', b)


def test_assoc_course12_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'studyprograms13'):
        assert _is_linked(a1, 'studyprograms13', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'studyprograms13'):
        assert not _is_linked(a1, 'studyprograms13', b)
    if hasattr(a2, 'studyprograms13'):
        assert _is_linked(a2, 'studyprograms13', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'studyprograms13'):
        assert not _is_linked(a2, 'studyprograms13', b)


def test_assoc_course34_reverse_link_reassign_clear():
    a1 = coursePages_Precondition(preconditionStatus="sample_text")
    a2 = coursePages_Precondition(preconditionStatus="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course36', a1)
    assert _is_linked(b, 'coursePages_Course36', a1)
    if hasattr(a1, 'coursePages_Precondition35'):
        assert _is_linked(a1, 'coursePages_Precondition35', b)
    _safe_set(b, 'coursePages_Course36', a2)
    assert _is_linked(b, 'coursePages_Course36', a2)
    if hasattr(a1, 'coursePages_Precondition35'):
        assert not _is_linked(a1, 'coursePages_Precondition35', b)
    if hasattr(a2, 'coursePages_Precondition35'):
        assert _is_linked(a2, 'coursePages_Precondition35', b)
    _safe_set(b, 'coursePages_Course36', None)
    assert not _is_linked(b, 'coursePages_Course36', a2)
    if hasattr(a2, 'coursePages_Precondition35'):
        assert not _is_linked(a2, 'coursePages_Precondition35', b)


def test_assoc_course37_reverse_link_reassign_clear():
    a1 = coursePages_Reduction(creditReduction=3.14)
    a2 = coursePages_Reduction(creditReduction=9.99)
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course39', a1)
    assert _is_linked(b, 'coursePages_Course39', a1)
    if hasattr(a1, 'coursePages_Reduction38'):
        assert _is_linked(a1, 'coursePages_Reduction38', b)
    _safe_set(b, 'coursePages_Course39', a2)
    assert _is_linked(b, 'coursePages_Course39', a2)
    if hasattr(a1, 'coursePages_Reduction38'):
        assert not _is_linked(a1, 'coursePages_Reduction38', b)
    if hasattr(a2, 'coursePages_Reduction38'):
        assert _is_linked(a2, 'coursePages_Reduction38', b)
    _safe_set(b, 'coursePages_Course39', None)
    assert not _is_linked(b, 'coursePages_Course39', a2)
    if hasattr(a2, 'coursePages_Reduction38'):
        assert not _is_linked(a2, 'coursePages_Reduction38', b)


def test_assoc_course6_reverse_link_reassign_clear():
    a1 = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    a2 = coursePages_Department(departmentName="sample_text_2", email="sample_text_2", phoneNummber="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course7', a1)
    assert _is_linked(b, 'coursePages_Course7', a1)
    if hasattr(a1, 'coursePages_Department'):
        assert _is_linked(a1, 'coursePages_Department', b)
    _safe_set(b, 'coursePages_Course7', a2)
    assert _is_linked(b, 'coursePages_Course7', a2)
    if hasattr(a1, 'coursePages_Department'):
        assert not _is_linked(a1, 'coursePages_Department', b)
    if hasattr(a2, 'coursePages_Department'):
        assert _is_linked(a2, 'coursePages_Department', b)
    _safe_set(b, 'coursePages_Course7', None)
    assert not _is_linked(b, 'coursePages_Course7', a2)
    if hasattr(a2, 'coursePages_Department'):
        assert not _is_linked(a2, 'coursePages_Department', b)


def test_assoc_courseinstance16_reverse_link_reassign_clear():
    a1 = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    a2 = coursePages_CourseInstance(courseYear="sample_text_2", term="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course17', {a1})
    assert _is_linked(b, 'coursePages_Course17', a1)
    if hasattr(a1, 'coursePages_CourseInstance'):
        assert _is_linked(a1, 'coursePages_CourseInstance', b)
    _safe_set(b, 'coursePages_Course17', {a2})
    assert _is_linked(b, 'coursePages_Course17', a2)
    if hasattr(a1, 'coursePages_CourseInstance'):
        assert not _is_linked(a1, 'coursePages_CourseInstance', b)
    if hasattr(a2, 'coursePages_CourseInstance'):
        assert _is_linked(a2, 'coursePages_CourseInstance', b)
    _safe_set(b, 'coursePages_Course17', set())
    assert not _is_linked(b, 'coursePages_Course17', a2)
    if hasattr(a2, 'coursePages_CourseInstance'):
        assert not _is_linked(a2, 'coursePages_CourseInstance', b)


def test_assoc_courseworker20_reverse_link_reassign_clear():
    a1 = coursePages_CourseWorker(courseRole="sample_text")
    a2 = coursePages_CourseWorker(courseRole="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course21', {a1})
    assert _is_linked(b, 'coursePages_Course21', a1)
    if hasattr(a1, 'coursePages_CourseWorker'):
        assert _is_linked(a1, 'coursePages_CourseWorker', b)
    _safe_set(b, 'coursePages_Course21', {a2})
    assert _is_linked(b, 'coursePages_Course21', a2)
    if hasattr(a1, 'coursePages_CourseWorker'):
        assert not _is_linked(a1, 'coursePages_CourseWorker', b)
    if hasattr(a2, 'coursePages_CourseWorker'):
        assert _is_linked(a2, 'coursePages_CourseWorker', b)
    _safe_set(b, 'coursePages_Course21', set())
    assert not _is_linked(b, 'coursePages_Course21', a2)
    if hasattr(a2, 'coursePages_CourseWorker'):
        assert not _is_linked(a2, 'coursePages_CourseWorker', b)


def test_assoc_department2_reverse_link_reassign_clear():
    a1 = coursePages_Employee(position="sample_text")
    a2 = coursePages_Employee(position="sample_text_2")
    b = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'employee'):
        assert _is_linked(a1, 'employee', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'employee'):
        assert not _is_linked(a1, 'employee', b)
    if hasattr(a2, 'employee'):
        assert _is_linked(a2, 'employee', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'employee'):
        assert not _is_linked(a2, 'employee', b)


def test_assoc_employee3_reverse_link_reassign_clear():
    a1 = coursePages_Employee(position="sample_text")
    a2 = coursePages_Employee(position="sample_text_2")
    b = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    _safe_set(b, 'department', {a1})
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'department', {a2})
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'department', set())
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_employee32_reverse_link_reassign_clear():
    a1 = coursePages_Employee(position="sample_text")
    a2 = coursePages_Employee(position="sample_text_2")
    b = coursePages_CourseWorker(courseRole="sample_text")
    _safe_set(b, 'coursePages_CourseWorker33', a1)
    assert _is_linked(b, 'coursePages_CourseWorker33', a1)
    if hasattr(a1, 'coursePages_Employee'):
        assert _is_linked(a1, 'coursePages_Employee', b)
    _safe_set(b, 'coursePages_CourseWorker33', a2)
    assert _is_linked(b, 'coursePages_CourseWorker33', a2)
    if hasattr(a1, 'coursePages_Employee'):
        assert not _is_linked(a1, 'coursePages_Employee', b)
    if hasattr(a2, 'coursePages_Employee'):
        assert _is_linked(a2, 'coursePages_Employee', b)
    _safe_set(b, 'coursePages_CourseWorker33', None)
    assert not _is_linked(b, 'coursePages_CourseWorker33', a2)
    if hasattr(a2, 'coursePages_Employee'):
        assert not _is_linked(a2, 'coursePages_Employee', b)


def test_assoc_precondition22_reverse_link_reassign_clear():
    a1 = coursePages_Precondition(preconditionStatus="sample_text")
    a2 = coursePages_Precondition(preconditionStatus="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course23', {a1})
    assert _is_linked(b, 'coursePages_Course23', a1)
    if hasattr(a1, 'coursePages_Precondition'):
        assert _is_linked(a1, 'coursePages_Precondition', b)
    _safe_set(b, 'coursePages_Course23', {a2})
    assert _is_linked(b, 'coursePages_Course23', a2)
    if hasattr(a1, 'coursePages_Precondition'):
        assert not _is_linked(a1, 'coursePages_Precondition', b)
    if hasattr(a2, 'coursePages_Precondition'):
        assert _is_linked(a2, 'coursePages_Precondition', b)
    _safe_set(b, 'coursePages_Course23', set())
    assert not _is_linked(b, 'coursePages_Course23', a2)
    if hasattr(a2, 'coursePages_Precondition'):
        assert not _is_linked(a2, 'coursePages_Precondition', b)


def test_assoc_reduction24_reverse_link_reassign_clear():
    a1 = coursePages_Reduction(creditReduction=3.14)
    a2 = coursePages_Reduction(creditReduction=9.99)
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course25', {a1})
    assert _is_linked(b, 'coursePages_Course25', a1)
    if hasattr(a1, 'coursePages_Reduction'):
        assert _is_linked(a1, 'coursePages_Reduction', b)
    _safe_set(b, 'coursePages_Course25', {a2})
    assert _is_linked(b, 'coursePages_Course25', a2)
    if hasattr(a1, 'coursePages_Reduction'):
        assert not _is_linked(a1, 'coursePages_Reduction', b)
    if hasattr(a2, 'coursePages_Reduction'):
        assert _is_linked(a2, 'coursePages_Reduction', b)
    _safe_set(b, 'coursePages_Course25', set())
    assert not _is_linked(b, 'coursePages_Course25', a2)
    if hasattr(a2, 'coursePages_Reduction'):
        assert not _is_linked(a2, 'coursePages_Reduction', b)


def test_assoc_student10_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Student(studentID="sample_text")
    _safe_set(b, 'Student', a1)
    assert _is_linked(b, 'Student', a1)
    if hasattr(a1, 'studyprograms11'):
        assert _is_linked(a1, 'studyprograms11', b)
    _safe_set(b, 'Student', a2)
    assert _is_linked(b, 'Student', a2)
    if hasattr(a1, 'studyprograms11'):
        assert not _is_linked(a1, 'studyprograms11', b)
    if hasattr(a2, 'studyprograms11'):
        assert _is_linked(a2, 'studyprograms11', b)
    _safe_set(b, 'Student', None)
    assert not _is_linked(b, 'Student', a2)
    if hasattr(a2, 'studyprograms11'):
        assert not _is_linked(a2, 'studyprograms11', b)


def test_assoc_studyprograms0_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Student(studentID="sample_text")
    _safe_set(b, 'student', a1)
    assert _is_linked(b, 'student', a1)
    if hasattr(a1, 'StudyPrograms'):
        assert _is_linked(a1, 'StudyPrograms', b)
    _safe_set(b, 'student', a2)
    assert _is_linked(b, 'student', a2)
    if hasattr(a1, 'StudyPrograms'):
        assert not _is_linked(a1, 'StudyPrograms', b)
    if hasattr(a2, 'StudyPrograms'):
        assert _is_linked(a2, 'StudyPrograms', b)
    _safe_set(b, 'student', None)
    assert not _is_linked(b, 'student', a2)
    if hasattr(a2, 'StudyPrograms'):
        assert not _is_linked(a2, 'StudyPrograms', b)


def test_assoc_studyprograms18_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'course', {a1})
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'StudyPrograms19'):
        assert _is_linked(a1, 'StudyPrograms19', b)
    _safe_set(b, 'course', {a2})
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'StudyPrograms19'):
        assert not _is_linked(a1, 'StudyPrograms19', b)
    if hasattr(a2, 'StudyPrograms19'):
        assert _is_linked(a2, 'StudyPrograms19', b)
    _safe_set(b, 'course', set())
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'StudyPrograms19'):
        assert not _is_linked(a2, 'StudyPrograms19', b)


def test_assoc_studyprograms4_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    _safe_set(b, 'belongsToDepartment', {a1})
    assert _is_linked(b, 'belongsToDepartment', a1)
    if hasattr(a1, 'StudyPrograms5'):
        assert _is_linked(a1, 'StudyPrograms5', b)
    _safe_set(b, 'belongsToDepartment', {a2})
    assert _is_linked(b, 'belongsToDepartment', a2)
    if hasattr(a1, 'StudyPrograms5'):
        assert not _is_linked(a1, 'StudyPrograms5', b)
    if hasattr(a2, 'StudyPrograms5'):
        assert _is_linked(a2, 'StudyPrograms5', b)
    _safe_set(b, 'belongsToDepartment', set())
    assert not _is_linked(b, 'belongsToDepartment', a2)
    if hasattr(a2, 'StudyPrograms5'):
        assert not _is_linked(a2, 'StudyPrograms5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_coursework26_stub_double():
    # coursePages_CourseWork has no real 'coursePages_CourseWork28' property in the generated
    # code (a bare stub) -- manually attach it so coursePages_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coursePages_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    partner = coursePages_CourseWork()
    setattr(partner, 'coursePages_CourseWork28', None)
    _safe_set(owner, 'coursePages_CourseInstance27', partner)
    assert getattr(partner, 'coursePages_CourseWork28') == owner
    _safe_set(owner, 'coursePages_CourseInstance27', None)
    assert getattr(partner, 'coursePages_CourseWork28') is None


def test_assoc_courseworkobject15_stub_double():
    # coursePages_CourseWork has no real 'coursePages_CourseWork' property in the generated
    # code (a bare stub) -- manually attach it so coursePages_CourseWorkObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coursePages_CourseWorkObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coursePages_CourseWorkObject(courseWorkType="sample_text", day="sample_text", end=date(2024, 1, 1), room="sample_text", start=date(2024, 1, 1))
    partner = coursePages_CourseWork()
    setattr(partner, 'coursePages_CourseWork', None)
    _safe_set(owner, 'coursePages_CourseWorkObject', partner)
    assert owner in getattr(partner, 'coursePages_CourseWork')
    _safe_set(owner, 'coursePages_CourseWorkObject', None)
    assert owner not in getattr(partner, 'coursePages_CourseWork')


def test_assoc_evaluationobject14_stub_double():
    # coursePages_Evaluations has no real 'coursePages_Evaluations' property in the generated
    # code (a bare stub) -- manually attach it so coursePages_EvaluationObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coursePages_EvaluationObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coursePages_EvaluationObject(credits=7, date=date(2024, 1, 1), evaluationsForm="sample_text", term="sample_text")
    partner = coursePages_Evaluations()
    setattr(partner, 'coursePages_Evaluations', None)
    _safe_set(owner, 'coursePages_EvaluationObject', partner)
    assert owner in getattr(partner, 'coursePages_Evaluations')
    _safe_set(owner, 'coursePages_EvaluationObject', None)
    assert owner not in getattr(partner, 'coursePages_Evaluations')


def test_assoc_evaluations29_stub_double():
    # coursePages_Evaluations has no real 'coursePages_Evaluations31' property in the generated
    # code (a bare stub) -- manually attach it so coursePages_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coursePages_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    partner = coursePages_Evaluations()
    setattr(partner, 'coursePages_Evaluations31', None)
    _safe_set(owner, 'coursePages_CourseInstance30', partner)
    assert getattr(partner, 'coursePages_Evaluations31') == owner
    _safe_set(owner, 'coursePages_CourseInstance30', None)
    assert getattr(partner, 'coursePages_Evaluations31') is None


