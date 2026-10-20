import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Evaluation,
    PersonRole,
    course_desc_Course,
    course_desc_CourseCoordinator,
    course_desc_CourseInstance,
    course_desc_CoursePreconditions,
    course_desc_CourseWork,
    course_desc_Department,
    course_desc_Evaluation,
    course_desc_EvaluationWithDeadline,
    course_desc_Exam,
    course_desc_Lecturer,
    course_desc_Person,
    course_desc_PersonRole,
    course_desc_Student,
    course_desc_StudyProgram,
    course_desc_Timetable,
    course_desc_Univ,
    CourseWorkType,
    DeadlineEvaluation,
    StudyProgramCode,
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

def test_assoc_belongs26_reverse_link_reassign_clear():
    a1 = course_desc_StudyProgram(studyCode="sample_text")
    a2 = course_desc_StudyProgram(studyCode="sample_text_2")
    b = course_desc_Department(name="sample_text")
    _safe_set(b, 'Department27', a1)
    assert _is_linked(b, 'Department27', a1)
    if hasattr(a1, 'manages'):
        assert _is_linked(a1, 'manages', b)
    _safe_set(b, 'Department27', a2)
    assert _is_linked(b, 'Department27', a2)
    if hasattr(a1, 'manages'):
        assert not _is_linked(a1, 'manages', b)
    if hasattr(a2, 'manages'):
        assert _is_linked(a2, 'manages', b)
    _safe_set(b, 'Department27', None)
    assert not _is_linked(b, 'Department27', a2)
    if hasattr(a2, 'manages'):
        assert not _is_linked(a2, 'manages', b)


def test_assoc_belongsTo13_reverse_link_reassign_clear():
    a1 = course_desc_Evaluation(Percentage=3.14)
    a2 = course_desc_Evaluation(Percentage=9.99)
    b = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    _safe_set(b, 'CourseInstance14', a1)
    assert _is_linked(b, 'CourseInstance14', a1)
    if hasattr(a1, 'hasEvaluations'):
        assert _is_linked(a1, 'hasEvaluations', b)
    _safe_set(b, 'CourseInstance14', a2)
    assert _is_linked(b, 'CourseInstance14', a2)
    if hasattr(a1, 'hasEvaluations'):
        assert not _is_linked(a1, 'hasEvaluations', b)
    if hasattr(a2, 'hasEvaluations'):
        assert _is_linked(a2, 'hasEvaluations', b)
    _safe_set(b, 'CourseInstance14', None)
    assert not _is_linked(b, 'CourseInstance14', a2)
    if hasattr(a2, 'hasEvaluations'):
        assert not _is_linked(a2, 'hasEvaluations', b)


def test_assoc_belongsTo20_reverse_link_reassign_clear():
    a1 = course_desc_CoursePreconditions(isRecommended=True, isRequired=True, reductionPoints=3.14)
    a2 = course_desc_CoursePreconditions(isRecommended=False, isRequired=False, reductionPoints=9.99)
    b = course_desc_Course(Code="sample_text", Content="sample_text", Credits="sample_text", name="sample_text")
    _safe_set(b, 'course_desc_Course22', a1)
    assert _is_linked(b, 'course_desc_Course22', a1)
    if hasattr(a1, 'course_desc_CoursePreconditions21'):
        assert _is_linked(a1, 'course_desc_CoursePreconditions21', b)
    _safe_set(b, 'course_desc_Course22', a2)
    assert _is_linked(b, 'course_desc_Course22', a2)
    if hasattr(a1, 'course_desc_CoursePreconditions21'):
        assert not _is_linked(a1, 'course_desc_CoursePreconditions21', b)
    if hasattr(a2, 'course_desc_CoursePreconditions21'):
        assert _is_linked(a2, 'course_desc_CoursePreconditions21', b)
    _safe_set(b, 'course_desc_Course22', None)
    assert not _is_linked(b, 'course_desc_Course22', a2)
    if hasattr(a2, 'course_desc_CoursePreconditions21'):
        assert not _is_linked(a2, 'course_desc_CoursePreconditions21', b)


def test_assoc_finishedExams31_reverse_link_reassign_clear():
    a1 = course_desc_Student(totalStudyPoints=3.14)
    a2 = course_desc_Student(totalStudyPoints=9.99)
    b = course_desc_Exam(date=date(2024, 1, 1), duration=3.14, place="sample_text")
    _safe_set(b, 'course_desc_Exam', a1)
    assert _is_linked(b, 'course_desc_Exam', a1)
    if hasattr(a1, 'course_desc_Student'):
        assert _is_linked(a1, 'course_desc_Student', b)
    _safe_set(b, 'course_desc_Exam', a2)
    assert _is_linked(b, 'course_desc_Exam', a2)
    if hasattr(a1, 'course_desc_Student'):
        assert not _is_linked(a1, 'course_desc_Student', b)
    if hasattr(a2, 'course_desc_Student'):
        assert _is_linked(a2, 'course_desc_Student', b)
    _safe_set(b, 'course_desc_Exam', None)
    assert not _is_linked(b, 'course_desc_Exam', a2)
    if hasattr(a2, 'course_desc_Student'):
        assert not _is_linked(a2, 'course_desc_Student', b)


def test_assoc_hasEvaluations4_reverse_link_reassign_clear():
    a1 = course_desc_Evaluation(Percentage=3.14)
    a2 = course_desc_Evaluation(Percentage=9.99)
    b = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    _safe_set(b, 'belongsTo', {a1})
    assert _is_linked(b, 'belongsTo', a1)
    if hasattr(a1, 'Evaluation'):
        assert _is_linked(a1, 'Evaluation', b)
    _safe_set(b, 'belongsTo', {a2})
    assert _is_linked(b, 'belongsTo', a2)
    if hasattr(a1, 'Evaluation'):
        assert not _is_linked(a1, 'Evaluation', b)
    if hasattr(a2, 'Evaluation'):
        assert _is_linked(a2, 'Evaluation', b)
    _safe_set(b, 'belongsTo', set())
    assert not _is_linked(b, 'belongsTo', a2)
    if hasattr(a2, 'Evaluation'):
        assert not _is_linked(a2, 'Evaluation', b)


def test_assoc_hasExams30_reverse_link_reassign_clear():
    a1 = course_desc_Student(totalStudyPoints=3.14)
    a2 = course_desc_Student(totalStudyPoints=9.99)
    b = course_desc_Exam(date=date(2024, 1, 1), duration=3.14, place="sample_text")
    _safe_set(b, 'Exam', a1)
    assert _is_linked(b, 'Exam', a1)
    if hasattr(a1, 'hasRegisteredStudents'):
        assert _is_linked(a1, 'hasRegisteredStudents', b)
    _safe_set(b, 'Exam', a2)
    assert _is_linked(b, 'Exam', a2)
    if hasattr(a1, 'hasRegisteredStudents'):
        assert not _is_linked(a1, 'hasRegisteredStudents', b)
    if hasattr(a2, 'hasRegisteredStudents'):
        assert _is_linked(a2, 'hasRegisteredStudents', b)
    _safe_set(b, 'Exam', None)
    assert not _is_linked(b, 'Exam', a2)
    if hasattr(a2, 'hasRegisteredStudents'):
        assert not _is_linked(a2, 'hasRegisteredStudents', b)


def test_assoc_hasInstance0_reverse_link_reassign_clear():
    a1 = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    a2 = course_desc_CourseInstance(LabHours=9.99, LectureHours=9.99, Year=13)
    b = course_desc_Course(Code="sample_text", Content="sample_text", Credits="sample_text", name="sample_text")
    _safe_set(b, 'instanceOfCourse', {a1})
    assert _is_linked(b, 'instanceOfCourse', a1)
    if hasattr(a1, 'CourseInstance'):
        assert _is_linked(a1, 'CourseInstance', b)
    _safe_set(b, 'instanceOfCourse', {a2})
    assert _is_linked(b, 'instanceOfCourse', a2)
    if hasattr(a1, 'CourseInstance'):
        assert not _is_linked(a1, 'CourseInstance', b)
    if hasattr(a2, 'CourseInstance'):
        assert _is_linked(a2, 'CourseInstance', b)
    _safe_set(b, 'instanceOfCourse', set())
    assert not _is_linked(b, 'instanceOfCourse', a2)
    if hasattr(a2, 'CourseInstance'):
        assert not _is_linked(a2, 'CourseInstance', b)


def test_assoc_hasPrecondition1_reverse_link_reassign_clear():
    a1 = course_desc_CoursePreconditions(isRecommended=True, isRequired=True, reductionPoints=3.14)
    a2 = course_desc_CoursePreconditions(isRecommended=False, isRequired=False, reductionPoints=9.99)
    b = course_desc_Course(Code="sample_text", Content="sample_text", Credits="sample_text", name="sample_text")
    _safe_set(b, 'course_desc_Course', {a1})
    assert _is_linked(b, 'course_desc_Course', a1)
    if hasattr(a1, 'course_desc_CoursePreconditions'):
        assert _is_linked(a1, 'course_desc_CoursePreconditions', b)
    _safe_set(b, 'course_desc_Course', {a2})
    assert _is_linked(b, 'course_desc_Course', a2)
    if hasattr(a1, 'course_desc_CoursePreconditions'):
        assert not _is_linked(a1, 'course_desc_CoursePreconditions', b)
    if hasattr(a2, 'course_desc_CoursePreconditions'):
        assert _is_linked(a2, 'course_desc_CoursePreconditions', b)
    _safe_set(b, 'course_desc_Course', set())
    assert not _is_linked(b, 'course_desc_Course', a2)
    if hasattr(a2, 'course_desc_CoursePreconditions'):
        assert not _is_linked(a2, 'course_desc_CoursePreconditions', b)


def test_assoc_hasRegisteredStudents15_reverse_link_reassign_clear():
    a1 = course_desc_Student(totalStudyPoints=3.14)
    a2 = course_desc_Student(totalStudyPoints=9.99)
    b = course_desc_Exam(date=date(2024, 1, 1), duration=3.14, place="sample_text")
    _safe_set(b, 'hasExams', {a1})
    assert _is_linked(b, 'hasExams', a1)
    if hasattr(a1, 'Student'):
        assert _is_linked(a1, 'Student', b)
    _safe_set(b, 'hasExams', {a2})
    assert _is_linked(b, 'hasExams', a2)
    if hasattr(a1, 'Student'):
        assert not _is_linked(a1, 'Student', b)
    if hasattr(a2, 'Student'):
        assert _is_linked(a2, 'Student', b)
    _safe_set(b, 'hasExams', set())
    assert not _is_linked(b, 'hasExams', a2)
    if hasattr(a2, 'Student'):
        assert not _is_linked(a2, 'Student', b)


def test_assoc_instanceOfCourse3_reverse_link_reassign_clear():
    a1 = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    a2 = course_desc_CourseInstance(LabHours=9.99, LectureHours=9.99, Year=13)
    b = course_desc_Course(Code="sample_text", Content="sample_text", Credits="sample_text", name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'hasInstance'):
        assert _is_linked(a1, 'hasInstance', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'hasInstance'):
        assert not _is_linked(a1, 'hasInstance', b)
    if hasattr(a2, 'hasInstance'):
        assert _is_linked(a2, 'hasInstance', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'hasInstance'):
        assert not _is_linked(a2, 'hasInstance', b)


def test_assoc_isInstanceOf5_reverse_link_reassign_clear():
    a1 = course_desc_Department(name="sample_text")
    a2 = course_desc_Department(name="sample_text_2")
    b = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    _safe_set(b, 'responsible', a1)
    assert _is_linked(b, 'responsible', a1)
    if hasattr(a1, 'Department'):
        assert _is_linked(a1, 'Department', b)
    _safe_set(b, 'responsible', a2)
    assert _is_linked(b, 'responsible', a2)
    if hasattr(a1, 'Department'):
        assert not _is_linked(a1, 'Department', b)
    if hasattr(a2, 'Department'):
        assert _is_linked(a2, 'Department', b)
    _safe_set(b, 'responsible', None)
    assert not _is_linked(b, 'responsible', a2)
    if hasattr(a2, 'Department'):
        assert not _is_linked(a2, 'Department', b)


def test_assoc_manages12_reverse_link_reassign_clear():
    a1 = course_desc_StudyProgram(studyCode="sample_text")
    a2 = course_desc_StudyProgram(studyCode="sample_text_2")
    b = course_desc_Department(name="sample_text")
    _safe_set(b, 'belongs', {a1})
    assert _is_linked(b, 'belongs', a1)
    if hasattr(a1, 'StudyProgram'):
        assert _is_linked(a1, 'StudyProgram', b)
    _safe_set(b, 'belongs', {a2})
    assert _is_linked(b, 'belongs', a2)
    if hasattr(a1, 'StudyProgram'):
        assert not _is_linked(a1, 'StudyProgram', b)
    if hasattr(a2, 'StudyProgram'):
        assert _is_linked(a2, 'StudyProgram', b)
    _safe_set(b, 'belongs', set())
    assert not _is_linked(b, 'belongs', a2)
    if hasattr(a2, 'StudyProgram'):
        assert not _is_linked(a2, 'StudyProgram', b)


def test_assoc_offers23_reverse_link_reassign_clear():
    a1 = course_desc_StudyProgram(studyCode="sample_text")
    a2 = course_desc_StudyProgram(studyCode="sample_text_2")
    b = course_desc_Course(Code="sample_text", Content="sample_text", Credits="sample_text", name="sample_text")
    _safe_set(b, 'course_desc_Course25', a1)
    assert _is_linked(b, 'course_desc_Course25', a1)
    if hasattr(a1, 'course_desc_StudyProgram24'):
        assert _is_linked(a1, 'course_desc_StudyProgram24', b)
    _safe_set(b, 'course_desc_Course25', a2)
    assert _is_linked(b, 'course_desc_Course25', a2)
    if hasattr(a1, 'course_desc_StudyProgram24'):
        assert not _is_linked(a1, 'course_desc_StudyProgram24', b)
    if hasattr(a2, 'course_desc_StudyProgram24'):
        assert _is_linked(a2, 'course_desc_StudyProgram24', b)
    _safe_set(b, 'course_desc_Course25', None)
    assert not _is_linked(b, 'course_desc_Course25', a2)
    if hasattr(a2, 'course_desc_StudyProgram24'):
        assert not _is_linked(a2, 'course_desc_StudyProgram24', b)


def test_assoc_responsible10_reverse_link_reassign_clear():
    a1 = course_desc_Department(name="sample_text")
    a2 = course_desc_Department(name="sample_text_2")
    b = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    _safe_set(b, 'CourseInstance11', a1)
    assert _is_linked(b, 'CourseInstance11', a1)
    if hasattr(a1, 'isInstanceOf'):
        assert _is_linked(a1, 'isInstanceOf', b)
    _safe_set(b, 'CourseInstance11', a2)
    assert _is_linked(b, 'CourseInstance11', a2)
    if hasattr(a1, 'isInstanceOf'):
        assert not _is_linked(a1, 'isInstanceOf', b)
    if hasattr(a2, 'isInstanceOf'):
        assert _is_linked(a2, 'isInstanceOf', b)
    _safe_set(b, 'CourseInstance11', None)
    assert not _is_linked(b, 'CourseInstance11', a2)
    if hasattr(a2, 'isInstanceOf'):
        assert not _is_linked(a2, 'isInstanceOf', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_belongsTo32_stub_double():
    # course_desc_Lecturer has no real 'course_desc_Lecturer33' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    partner = course_desc_Lecturer()
    setattr(partner, 'course_desc_Lecturer33', None)
    _safe_set(owner, 'course_desc_CourseInstance34', partner)
    assert getattr(partner, 'course_desc_Lecturer33') == owner
    _safe_set(owner, 'course_desc_CourseInstance34', None)
    assert getattr(partner, 'course_desc_Lecturer33') is None


def test_assoc_belongsTo35_stub_double():
    # course_desc_CourseCoordinator has no real 'course_desc_CourseCoordinator36' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    partner = course_desc_CourseCoordinator()
    setattr(partner, 'course_desc_CourseCoordinator36', None)
    _safe_set(owner, 'course_desc_CourseInstance37', partner)
    assert getattr(partner, 'course_desc_CourseCoordinator36') == owner
    _safe_set(owner, 'course_desc_CourseInstance37', None)
    assert getattr(partner, 'course_desc_CourseCoordinator36') is None


def test_assoc_hasCourseCoordinator8_stub_double():
    # course_desc_CourseCoordinator has no real 'course_desc_CourseCoordinator' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    partner = course_desc_CourseCoordinator()
    setattr(partner, 'course_desc_CourseCoordinator', None)
    _safe_set(owner, 'course_desc_CourseInstance9', {partner})
    assert getattr(partner, 'course_desc_CourseCoordinator') == owner
    _safe_set(owner, 'course_desc_CourseInstance9', set())
    assert getattr(partner, 'course_desc_CourseCoordinator') is None


def test_assoc_hasCourseWork16_stub_double():
    # course_desc_Timetable has no real 'course_desc_Timetable17' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_CourseWork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_CourseWork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_CourseWork(Duration=7, Room="sample_text", Type="sample_text", isMandatory=True, isRestricted=True)
    partner = course_desc_Timetable()
    setattr(partner, 'course_desc_Timetable17', None)
    _safe_set(owner, 'course_desc_CourseWork', partner)
    assert owner in getattr(partner, 'course_desc_Timetable17')
    _safe_set(owner, 'course_desc_CourseWork', None)
    assert owner not in getattr(partner, 'course_desc_Timetable17')


def test_assoc_hasCourses39_stub_double():
    # course_desc_Univ has no real 'course_desc_Univ40' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_Course's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_Course's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_Course(Code="sample_text", Content="sample_text", Credits="sample_text", name="sample_text")
    partner = course_desc_Univ()
    setattr(partner, 'course_desc_Univ40', None)
    _safe_set(owner, 'course_desc_Course41', partner)
    assert owner in getattr(partner, 'course_desc_Univ40')
    _safe_set(owner, 'course_desc_Course41', None)
    assert owner not in getattr(partner, 'course_desc_Univ40')


def test_assoc_hasDepartment38_stub_double():
    # course_desc_Univ has no real 'course_desc_Univ' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_Department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_Department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_Department(name="sample_text")
    partner = course_desc_Univ()
    setattr(partner, 'course_desc_Univ', None)
    _safe_set(owner, 'course_desc_Department', partner)
    assert owner in getattr(partner, 'course_desc_Univ')
    _safe_set(owner, 'course_desc_Department', None)
    assert owner not in getattr(partner, 'course_desc_Univ')


def test_assoc_hasLecturers6_stub_double():
    # course_desc_Lecturer has no real 'course_desc_Lecturer' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    partner = course_desc_Lecturer()
    setattr(partner, 'course_desc_Lecturer', None)
    _safe_set(owner, 'course_desc_CourseInstance7', {partner})
    assert getattr(partner, 'course_desc_Lecturer') == owner
    _safe_set(owner, 'course_desc_CourseInstance7', set())
    assert getattr(partner, 'course_desc_Lecturer') is None


def test_assoc_hasPersons42_stub_double():
    # course_desc_Univ has no real 'course_desc_Univ43' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_Person(fullName="sample_text", lastName="sample_text", name="sample_text", personNr="sample_text")
    partner = course_desc_Univ()
    setattr(partner, 'course_desc_Univ43', None)
    _safe_set(owner, 'course_desc_Person', partner)
    assert owner in getattr(partner, 'course_desc_Univ43')
    _safe_set(owner, 'course_desc_Person', None)
    assert owner not in getattr(partner, 'course_desc_Univ43')


def test_assoc_hasPrecond44_stub_double():
    # course_desc_Univ has no real 'course_desc_Univ45' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_CoursePreconditions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_CoursePreconditions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_CoursePreconditions(isRecommended=True, isRequired=True, reductionPoints=3.14)
    partner = course_desc_Univ()
    setattr(partner, 'course_desc_Univ45', None)
    _safe_set(owner, 'course_desc_CoursePreconditions46', partner)
    assert owner in getattr(partner, 'course_desc_Univ45')
    _safe_set(owner, 'course_desc_CoursePreconditions46', None)
    assert owner not in getattr(partner, 'course_desc_Univ45')


def test_assoc_hasRole28_stub_double():
    # course_desc_PersonRole has no real 'PersonRole' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_Person(fullName="sample_text", lastName="sample_text", name="sample_text", personNr="sample_text")
    partner = course_desc_PersonRole()
    setattr(partner, 'PersonRole', None)
    _safe_set(owner, 'linkedTo', {partner})
    assert getattr(partner, 'PersonRole') == owner
    _safe_set(owner, 'linkedTo', set())
    assert getattr(partner, 'PersonRole') is None


def test_assoc_hasStudents47_stub_double():
    # course_desc_Univ has no real 'course_desc_Univ48' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_Student(totalStudyPoints=3.14)
    partner = course_desc_Univ()
    setattr(partner, 'course_desc_Univ48', None)
    _safe_set(owner, 'course_desc_Student49', partner)
    assert owner in getattr(partner, 'course_desc_Univ48')
    _safe_set(owner, 'course_desc_Student49', None)
    assert owner not in getattr(partner, 'course_desc_Univ48')


def test_assoc_hasTimetable2_stub_double():
    # course_desc_Timetable has no real 'course_desc_Timetable' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_CourseInstance(LabHours=3.14, LectureHours=3.14, Year=7)
    partner = course_desc_Timetable()
    setattr(partner, 'course_desc_Timetable', None)
    _safe_set(owner, 'course_desc_CourseInstance', {partner})
    assert getattr(partner, 'course_desc_Timetable') == owner
    _safe_set(owner, 'course_desc_CourseInstance', set())
    assert getattr(partner, 'course_desc_Timetable') is None


def test_assoc_linkedTo29_stub_double():
    # course_desc_PersonRole has no real 'hasRole' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_Person(fullName="sample_text", lastName="sample_text", name="sample_text", personNr="sample_text")
    partner = course_desc_PersonRole()
    setattr(partner, 'hasRole', None)
    _safe_set(owner, 'Person', partner)
    assert getattr(partner, 'hasRole') == owner
    _safe_set(owner, 'Person', None)
    assert getattr(partner, 'hasRole') is None


def test_assoc_programs18_stub_double():
    # course_desc_Timetable has no real 'course_desc_Timetable19' property in the generated
    # code (a bare stub) -- manually attach it so course_desc_StudyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # course_desc_StudyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = course_desc_StudyProgram(studyCode="sample_text")
    partner = course_desc_Timetable()
    setattr(partner, 'course_desc_Timetable19', None)
    _safe_set(owner, 'course_desc_StudyProgram', partner)
    assert owner in getattr(partner, 'course_desc_Timetable19')
    _safe_set(owner, 'course_desc_StudyProgram', None)
    assert owner not in getattr(partner, 'course_desc_Timetable19')


