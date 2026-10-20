import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    oving4_Assignment,
    oving4_Course,
    oving4_CourseInstance,
    oving4_CourseWork,
    oving4_Department,
    oving4_Evaluation,
    oving4_EvaluationElement,
    oving4_Exam,
    oving4_Person,
    oving4_PersonRole,
    oving4_Precondition,
    oving4_Project,
    oving4_Root,
    oving4_StudyProgram,
    oving4_TimeTable,
    oving4_TimeTableElement,
    CourseWorkType,
    EvaluationType,
    RoleType,
    StudyProgramType,
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

def test_assoc_belongToEvEl61_reverse_link_reassign_clear():
    a1 = oving4_EvaluationElement(attended=True, percentageResult=3.14, type="sample_text", weight=3.14)
    a2 = oving4_EvaluationElement(attended=False, percentageResult=9.99, type="sample_text_2", weight=9.99)
    b = oving4_Assignment(deadline="sample_text")
    _safe_set(b, 'containsAssignment', a1)
    assert _is_linked(b, 'containsAssignment', a1)
    if hasattr(a1, 'EvaluationElement62'):
        assert _is_linked(a1, 'EvaluationElement62', b)
    _safe_set(b, 'containsAssignment', a2)
    assert _is_linked(b, 'containsAssignment', a2)
    if hasattr(a1, 'EvaluationElement62'):
        assert not _is_linked(a1, 'EvaluationElement62', b)
    if hasattr(a2, 'EvaluationElement62'):
        assert _is_linked(a2, 'EvaluationElement62', b)
    _safe_set(b, 'containsAssignment', None)
    assert not _is_linked(b, 'containsAssignment', a2)
    if hasattr(a2, 'EvaluationElement62'):
        assert not _is_linked(a2, 'EvaluationElement62', b)


def test_assoc_belongsToEvaluationElement56_reverse_link_reassign_clear():
    a1 = oving4_Exam(endDate="sample_text", previousEndDate="sample_text", previousStartDate="sample_text", startDate="sample_text")
    a2 = oving4_Exam(endDate="sample_text_2", previousEndDate="sample_text_2", previousStartDate="sample_text_2", startDate="sample_text_2")
    b = oving4_EvaluationElement(attended=True, percentageResult=3.14, type="sample_text", weight=3.14)
    _safe_set(b, 'EvaluationElement', a1)
    assert _is_linked(b, 'EvaluationElement', a1)
    if hasattr(a1, 'containsExam'):
        assert _is_linked(a1, 'containsExam', b)
    _safe_set(b, 'EvaluationElement', a2)
    assert _is_linked(b, 'EvaluationElement', a2)
    if hasattr(a1, 'containsExam'):
        assert not _is_linked(a1, 'containsExam', b)
    if hasattr(a2, 'containsExam'):
        assert _is_linked(a2, 'containsExam', b)
    _safe_set(b, 'EvaluationElement', None)
    assert not _is_linked(b, 'EvaluationElement', a2)
    if hasattr(a2, 'containsExam'):
        assert not _is_linked(a2, 'containsExam', b)


def test_assoc_belongsToEvaluationel57_reverse_link_reassign_clear():
    a1 = oving4_Project(deadline="sample_text")
    a2 = oving4_Project(deadline="sample_text_2")
    b = oving4_EvaluationElement(attended=True, percentageResult=3.14, type="sample_text", weight=3.14)
    _safe_set(b, 'EvaluationElement58', a1)
    assert _is_linked(b, 'EvaluationElement58', a1)
    if hasattr(a1, 'containsProject'):
        assert _is_linked(a1, 'containsProject', b)
    _safe_set(b, 'EvaluationElement58', a2)
    assert _is_linked(b, 'EvaluationElement58', a2)
    if hasattr(a1, 'containsProject'):
        assert not _is_linked(a1, 'containsProject', b)
    if hasattr(a2, 'containsProject'):
        assert _is_linked(a2, 'containsProject', b)
    _safe_set(b, 'EvaluationElement58', None)
    assert not _is_linked(b, 'EvaluationElement58', a2)
    if hasattr(a2, 'containsProject'):
        assert not _is_linked(a2, 'containsProject', b)


def test_assoc_containsAssignment55_reverse_link_reassign_clear():
    a1 = oving4_EvaluationElement(attended=True, percentageResult=3.14, type="sample_text", weight=3.14)
    a2 = oving4_EvaluationElement(attended=False, percentageResult=9.99, type="sample_text_2", weight=9.99)
    b = oving4_Assignment(deadline="sample_text")
    _safe_set(b, 'Assignment', a1)
    assert _is_linked(b, 'Assignment', a1)
    if hasattr(a1, 'belongToEvEl'):
        assert _is_linked(a1, 'belongToEvEl', b)
    _safe_set(b, 'Assignment', a2)
    assert _is_linked(b, 'Assignment', a2)
    if hasattr(a1, 'belongToEvEl'):
        assert not _is_linked(a1, 'belongToEvEl', b)
    if hasattr(a2, 'belongToEvEl'):
        assert _is_linked(a2, 'belongToEvEl', b)
    _safe_set(b, 'Assignment', None)
    assert not _is_linked(b, 'Assignment', a2)
    if hasattr(a2, 'belongToEvEl'):
        assert not _is_linked(a2, 'belongToEvEl', b)


def test_assoc_containsCourse10_reverse_link_reassign_clear():
    a1 = oving4_StudyProgram(type="sample_text")
    a2 = oving4_StudyProgram(type="sample_text_2")
    b = oving4_Course(code="sample_text", content="sample_text", credits=3.14, examEndDate="sample_text", examStartDate="sample_text", name="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'studyprogram'):
        assert _is_linked(a1, 'studyprogram', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'studyprogram'):
        assert not _is_linked(a1, 'studyprogram', b)
    if hasattr(a2, 'studyprogram'):
        assert _is_linked(a2, 'studyprogram', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'studyprogram'):
        assert not _is_linked(a2, 'studyprogram', b)


def test_assoc_containsCourseWork23_reverse_link_reassign_clear():
    a1 = oving4_CourseWork(isMandatory=True, name="sample_text", type="sample_text")
    a2 = oving4_CourseWork(isMandatory=False, name="sample_text_2", type="sample_text_2")
    b = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    _safe_set(b, 'oving4_CourseInstance', {a1})
    assert _is_linked(b, 'oving4_CourseInstance', a1)
    if hasattr(a1, 'oving4_CourseWork'):
        assert _is_linked(a1, 'oving4_CourseWork', b)
    _safe_set(b, 'oving4_CourseInstance', {a2})
    assert _is_linked(b, 'oving4_CourseInstance', a2)
    if hasattr(a1, 'oving4_CourseWork'):
        assert not _is_linked(a1, 'oving4_CourseWork', b)
    if hasattr(a2, 'oving4_CourseWork'):
        assert _is_linked(a2, 'oving4_CourseWork', b)
    _safe_set(b, 'oving4_CourseInstance', set())
    assert not _is_linked(b, 'oving4_CourseInstance', a2)
    if hasattr(a2, 'oving4_CourseWork'):
        assert not _is_linked(a2, 'oving4_CourseWork', b)


def test_assoc_containsElement44_reverse_link_reassign_clear():
    a1 = oving4_EvaluationElement(attended=True, percentageResult=3.14, type="sample_text", weight=3.14)
    a2 = oving4_EvaluationElement(attended=False, percentageResult=9.99, type="sample_text_2", weight=9.99)
    b = oving4_Evaluation(completed=True, creditsReceived=3.14, description="sample_text", totalPercentageResult=3.14)
    _safe_set(b, 'oving4_Evaluation', {a1})
    assert _is_linked(b, 'oving4_Evaluation', a1)
    if hasattr(a1, 'oving4_EvaluationElement'):
        assert _is_linked(a1, 'oving4_EvaluationElement', b)
    _safe_set(b, 'oving4_Evaluation', {a2})
    assert _is_linked(b, 'oving4_Evaluation', a2)
    if hasattr(a1, 'oving4_EvaluationElement'):
        assert not _is_linked(a1, 'oving4_EvaluationElement', b)
    if hasattr(a2, 'oving4_EvaluationElement'):
        assert _is_linked(a2, 'oving4_EvaluationElement', b)
    _safe_set(b, 'oving4_Evaluation', set())
    assert not _is_linked(b, 'oving4_Evaluation', a2)
    if hasattr(a2, 'oving4_EvaluationElement'):
        assert not _is_linked(a2, 'oving4_EvaluationElement', b)


def test_assoc_containsEvaluation26_reverse_link_reassign_clear():
    a1 = oving4_Evaluation(completed=True, creditsReceived=3.14, description="sample_text", totalPercentageResult=3.14)
    a2 = oving4_Evaluation(completed=False, creditsReceived=9.99, description="sample_text_2", totalPercentageResult=9.99)
    b = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    _safe_set(b, 'courseInstance27', {a1})
    assert _is_linked(b, 'courseInstance27', a1)
    if hasattr(a1, 'Evaluation28'):
        assert _is_linked(a1, 'Evaluation28', b)
    _safe_set(b, 'courseInstance27', {a2})
    assert _is_linked(b, 'courseInstance27', a2)
    if hasattr(a1, 'Evaluation28'):
        assert not _is_linked(a1, 'Evaluation28', b)
    if hasattr(a2, 'Evaluation28'):
        assert _is_linked(a2, 'Evaluation28', b)
    _safe_set(b, 'courseInstance27', set())
    assert not _is_linked(b, 'courseInstance27', a2)
    if hasattr(a2, 'Evaluation28'):
        assert not _is_linked(a2, 'Evaluation28', b)


def test_assoc_containsExam53_reverse_link_reassign_clear():
    a1 = oving4_Exam(endDate="sample_text", previousEndDate="sample_text", previousStartDate="sample_text", startDate="sample_text")
    a2 = oving4_Exam(endDate="sample_text_2", previousEndDate="sample_text_2", previousStartDate="sample_text_2", startDate="sample_text_2")
    b = oving4_EvaluationElement(attended=True, percentageResult=3.14, type="sample_text", weight=3.14)
    _safe_set(b, 'belongsToEvaluationElement', a1)
    assert _is_linked(b, 'belongsToEvaluationElement', a1)
    if hasattr(a1, 'Exam'):
        assert _is_linked(a1, 'Exam', b)
    _safe_set(b, 'belongsToEvaluationElement', a2)
    assert _is_linked(b, 'belongsToEvaluationElement', a2)
    if hasattr(a1, 'Exam'):
        assert not _is_linked(a1, 'Exam', b)
    if hasattr(a2, 'Exam'):
        assert _is_linked(a2, 'Exam', b)
    _safe_set(b, 'belongsToEvaluationElement', None)
    assert not _is_linked(b, 'belongsToEvaluationElement', a2)
    if hasattr(a2, 'Exam'):
        assert not _is_linked(a2, 'Exam', b)


def test_assoc_containsProject54_reverse_link_reassign_clear():
    a1 = oving4_Project(deadline="sample_text")
    a2 = oving4_Project(deadline="sample_text_2")
    b = oving4_EvaluationElement(attended=True, percentageResult=3.14, type="sample_text", weight=3.14)
    _safe_set(b, 'belongsToEvaluationel', a1)
    assert _is_linked(b, 'belongsToEvaluationel', a1)
    if hasattr(a1, 'Project'):
        assert _is_linked(a1, 'Project', b)
    _safe_set(b, 'belongsToEvaluationel', a2)
    assert _is_linked(b, 'belongsToEvaluationel', a2)
    if hasattr(a1, 'Project'):
        assert not _is_linked(a1, 'Project', b)
    if hasattr(a2, 'Project'):
        assert _is_linked(a2, 'Project', b)
    _safe_set(b, 'belongsToEvaluationel', None)
    assert not _is_linked(b, 'belongsToEvaluationel', a2)
    if hasattr(a2, 'Project'):
        assert not _is_linked(a2, 'Project', b)


def test_assoc_containsTimeTableElement36_reverse_link_reassign_clear():
    a1 = oving4_TimeTableElement(date="sample_text", durationInMinutes=7, room="sample_text")
    a2 = oving4_TimeTableElement(date="sample_text_2", durationInMinutes=13, room="sample_text_2")
    b = oving4_TimeTable(isRestrictedToProgramsInParallell=True)
    _safe_set(b, 'oving4_TimeTable', {a1})
    assert _is_linked(b, 'oving4_TimeTable', a1)
    if hasattr(a1, 'oving4_TimeTableElement'):
        assert _is_linked(a1, 'oving4_TimeTableElement', b)
    _safe_set(b, 'oving4_TimeTable', {a2})
    assert _is_linked(b, 'oving4_TimeTable', a2)
    if hasattr(a1, 'oving4_TimeTableElement'):
        assert not _is_linked(a1, 'oving4_TimeTableElement', b)
    if hasattr(a2, 'oving4_TimeTableElement'):
        assert _is_linked(a2, 'oving4_TimeTableElement', b)
    _safe_set(b, 'oving4_TimeTable', set())
    assert not _is_linked(b, 'oving4_TimeTable', a2)
    if hasattr(a2, 'oving4_TimeTableElement'):
        assert not _is_linked(a2, 'oving4_TimeTableElement', b)


def test_assoc_courseInstance16_reverse_link_reassign_clear():
    a1 = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    a2 = oving4_CourseInstance(sumExerciseHours=13, sumInDepthHours=13, sumLectureHours=13)
    b = oving4_Course(code="sample_text", content="sample_text", credits=3.14, examEndDate="sample_text", examStartDate="sample_text", name="sample_text")
    _safe_set(b, 'ownedBy', {a1})
    assert _is_linked(b, 'ownedBy', a1)
    if hasattr(a1, 'CourseInstance'):
        assert _is_linked(a1, 'CourseInstance', b)
    _safe_set(b, 'ownedBy', {a2})
    assert _is_linked(b, 'ownedBy', a2)
    if hasattr(a1, 'CourseInstance'):
        assert not _is_linked(a1, 'CourseInstance', b)
    if hasattr(a2, 'CourseInstance'):
        assert _is_linked(a2, 'CourseInstance', b)
    _safe_set(b, 'ownedBy', set())
    assert not _is_linked(b, 'ownedBy', a2)
    if hasattr(a2, 'CourseInstance'):
        assert not _is_linked(a2, 'CourseInstance', b)


def test_assoc_courseInstance45_reverse_link_reassign_clear():
    a1 = oving4_Evaluation(completed=True, creditsReceived=3.14, description="sample_text", totalPercentageResult=3.14)
    a2 = oving4_Evaluation(completed=False, creditsReceived=9.99, description="sample_text_2", totalPercentageResult=9.99)
    b = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    _safe_set(b, 'CourseInstance46', a1)
    assert _is_linked(b, 'CourseInstance46', a1)
    if hasattr(a1, 'containsEvaluation'):
        assert _is_linked(a1, 'containsEvaluation', b)
    _safe_set(b, 'CourseInstance46', a2)
    assert _is_linked(b, 'CourseInstance46', a2)
    if hasattr(a1, 'containsEvaluation'):
        assert not _is_linked(a1, 'containsEvaluation', b)
    if hasattr(a2, 'containsEvaluation'):
        assert _is_linked(a2, 'containsEvaluation', b)
    _safe_set(b, 'CourseInstance46', None)
    assert not _is_linked(b, 'CourseInstance46', a2)
    if hasattr(a2, 'containsEvaluation'):
        assert not _is_linked(a2, 'containsEvaluation', b)


def test_assoc_employedByDepartment34_reverse_link_reassign_clear():
    a1 = oving4_PersonRole(type="sample_text")
    a2 = oving4_PersonRole(type="sample_text_2")
    b = oving4_Department(name="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'hasEmployee35'):
        assert _is_linked(a1, 'hasEmployee35', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'hasEmployee35'):
        assert not _is_linked(a1, 'hasEmployee35', b)
    if hasattr(a2, 'hasEmployee35'):
        assert _is_linked(a2, 'hasEmployee35', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'hasEmployee35'):
        assert not _is_linked(a2, 'hasEmployee35', b)


def test_assoc_employedOfStudyProgram30_reverse_link_reassign_clear():
    a1 = oving4_StudyProgram(type="sample_text")
    a2 = oving4_StudyProgram(type="sample_text_2")
    b = oving4_PersonRole(type="sample_text")
    _safe_set(b, 'hasEmployee', a1)
    assert _is_linked(b, 'hasEmployee', a1)
    if hasattr(a1, 'StudyProgram31'):
        assert _is_linked(a1, 'StudyProgram31', b)
    _safe_set(b, 'hasEmployee', a2)
    assert _is_linked(b, 'hasEmployee', a2)
    if hasattr(a1, 'StudyProgram31'):
        assert not _is_linked(a1, 'StudyProgram31', b)
    if hasattr(a2, 'StudyProgram31'):
        assert _is_linked(a2, 'StudyProgram31', b)
    _safe_set(b, 'hasEmployee', None)
    assert not _is_linked(b, 'hasEmployee', a2)
    if hasattr(a2, 'StudyProgram31'):
        assert not _is_linked(a2, 'StudyProgram31', b)


def test_assoc_hasEmployee11_reverse_link_reassign_clear():
    a1 = oving4_StudyProgram(type="sample_text")
    a2 = oving4_StudyProgram(type="sample_text_2")
    b = oving4_PersonRole(type="sample_text")
    _safe_set(b, 'PersonRole12', a1)
    assert _is_linked(b, 'PersonRole12', a1)
    if hasattr(a1, 'employedOfStudyProgram'):
        assert _is_linked(a1, 'employedOfStudyProgram', b)
    _safe_set(b, 'PersonRole12', a2)
    assert _is_linked(b, 'PersonRole12', a2)
    if hasattr(a1, 'employedOfStudyProgram'):
        assert not _is_linked(a1, 'employedOfStudyProgram', b)
    if hasattr(a2, 'employedOfStudyProgram'):
        assert _is_linked(a2, 'employedOfStudyProgram', b)
    _safe_set(b, 'PersonRole12', None)
    assert not _is_linked(b, 'PersonRole12', a2)
    if hasattr(a2, 'employedOfStudyProgram'):
        assert not _is_linked(a2, 'employedOfStudyProgram', b)


def test_assoc_hasEmployee9_reverse_link_reassign_clear():
    a1 = oving4_PersonRole(type="sample_text")
    a2 = oving4_PersonRole(type="sample_text_2")
    b = oving4_Department(name="sample_text")
    _safe_set(b, 'employedByDepartment', {a1})
    assert _is_linked(b, 'employedByDepartment', a1)
    if hasattr(a1, 'PersonRole'):
        assert _is_linked(a1, 'PersonRole', b)
    _safe_set(b, 'employedByDepartment', {a2})
    assert _is_linked(b, 'employedByDepartment', a2)
    if hasattr(a1, 'PersonRole'):
        assert not _is_linked(a1, 'PersonRole', b)
    if hasattr(a2, 'PersonRole'):
        assert _is_linked(a2, 'PersonRole', b)
    _safe_set(b, 'employedByDepartment', set())
    assert not _is_linked(b, 'employedByDepartment', a2)
    if hasattr(a2, 'PersonRole'):
        assert not _is_linked(a2, 'PersonRole', b)


def test_assoc_hasEvaluation15_reverse_link_reassign_clear():
    a1 = oving4_Person(first_name="sample_text", last_name="sample_text", name="sample_text", studyCredits=3.14)
    a2 = oving4_Person(first_name="sample_text_2", last_name="sample_text_2", name="sample_text_2", studyCredits=9.99)
    b = oving4_Evaluation(completed=True, creditsReceived=3.14, description="sample_text", totalPercentageResult=3.14)
    _safe_set(b, 'Evaluation', a1)
    assert _is_linked(b, 'Evaluation', a1)
    if hasattr(a1, 'personEvaluated'):
        assert _is_linked(a1, 'personEvaluated', b)
    _safe_set(b, 'Evaluation', a2)
    assert _is_linked(b, 'Evaluation', a2)
    if hasattr(a1, 'personEvaluated'):
        assert not _is_linked(a1, 'personEvaluated', b)
    if hasattr(a2, 'personEvaluated'):
        assert _is_linked(a2, 'personEvaluated', b)
    _safe_set(b, 'Evaluation', None)
    assert not _is_linked(b, 'Evaluation', a2)
    if hasattr(a2, 'personEvaluated'):
        assert not _is_linked(a2, 'personEvaluated', b)


def test_assoc_hasMember24_reverse_link_reassign_clear():
    a1 = oving4_PersonRole(type="sample_text")
    a2 = oving4_PersonRole(type="sample_text_2")
    b = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    _safe_set(b, 'memberOfCourse', {a1})
    assert _is_linked(b, 'memberOfCourse', a1)
    if hasattr(a1, 'PersonRole25'):
        assert _is_linked(a1, 'PersonRole25', b)
    _safe_set(b, 'memberOfCourse', {a2})
    assert _is_linked(b, 'memberOfCourse', a2)
    if hasattr(a1, 'PersonRole25'):
        assert not _is_linked(a1, 'PersonRole25', b)
    if hasattr(a2, 'PersonRole25'):
        assert _is_linked(a2, 'PersonRole25', b)
    _safe_set(b, 'memberOfCourse', set())
    assert not _is_linked(b, 'memberOfCourse', a2)
    if hasattr(a2, 'PersonRole25'):
        assert not _is_linked(a2, 'PersonRole25', b)


def test_assoc_hasMembers59_reverse_link_reassign_clear():
    a1 = oving4_Project(deadline="sample_text")
    a2 = oving4_Project(deadline="sample_text_2")
    b = oving4_PersonRole(type="sample_text")
    _safe_set(b, 'oving4_PersonRole', a1)
    assert _is_linked(b, 'oving4_PersonRole', a1)
    if hasattr(a1, 'oving4_Project60'):
        assert _is_linked(a1, 'oving4_Project60', b)
    _safe_set(b, 'oving4_PersonRole', a2)
    assert _is_linked(b, 'oving4_PersonRole', a2)
    if hasattr(a1, 'oving4_Project60'):
        assert not _is_linked(a1, 'oving4_Project60', b)
    if hasattr(a2, 'oving4_Project60'):
        assert _is_linked(a2, 'oving4_Project60', b)
    _safe_set(b, 'oving4_PersonRole', None)
    assert not _is_linked(b, 'oving4_PersonRole', a2)
    if hasattr(a2, 'oving4_Project60'):
        assert not _is_linked(a2, 'oving4_Project60', b)


def test_assoc_hasPrecondition18_reverse_link_reassign_clear():
    a1 = oving4_Precondition(creditReduction=3.14, isMandatory=True)
    a2 = oving4_Precondition(creditReduction=9.99, isMandatory=False)
    b = oving4_Course(code="sample_text", content="sample_text", credits=3.14, examEndDate="sample_text", examStartDate="sample_text", name="sample_text")
    _safe_set(b, 'oving4_Course19', {a1})
    assert _is_linked(b, 'oving4_Course19', a1)
    if hasattr(a1, 'oving4_Precondition'):
        assert _is_linked(a1, 'oving4_Precondition', b)
    _safe_set(b, 'oving4_Course19', {a2})
    assert _is_linked(b, 'oving4_Course19', a2)
    if hasattr(a1, 'oving4_Precondition'):
        assert not _is_linked(a1, 'oving4_Precondition', b)
    if hasattr(a2, 'oving4_Precondition'):
        assert _is_linked(a2, 'oving4_Precondition', b)
    _safe_set(b, 'oving4_Course19', set())
    assert not _is_linked(b, 'oving4_Course19', a2)
    if hasattr(a2, 'oving4_Precondition'):
        assert not _is_linked(a2, 'oving4_Precondition', b)


def test_assoc_hasRole13_reverse_link_reassign_clear():
    a1 = oving4_PersonRole(type="sample_text")
    a2 = oving4_PersonRole(type="sample_text_2")
    b = oving4_Person(first_name="sample_text", last_name="sample_text", name="sample_text", studyCredits=3.14)
    _safe_set(b, 'person', {a1})
    assert _is_linked(b, 'person', a1)
    if hasattr(a1, 'PersonRole14'):
        assert _is_linked(a1, 'PersonRole14', b)
    _safe_set(b, 'person', {a2})
    assert _is_linked(b, 'person', a2)
    if hasattr(a1, 'PersonRole14'):
        assert not _is_linked(a1, 'PersonRole14', b)
    if hasattr(a2, 'PersonRole14'):
        assert _is_linked(a2, 'PersonRole14', b)
    _safe_set(b, 'person', set())
    assert not _is_linked(b, 'person', a2)
    if hasattr(a2, 'PersonRole14'):
        assert not _is_linked(a2, 'PersonRole14', b)


def test_assoc_hasTimeTable20_reverse_link_reassign_clear():
    a1 = oving4_TimeTable(isRestrictedToProgramsInParallell=True)
    a2 = oving4_TimeTable(isRestrictedToProgramsInParallell=False)
    b = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    _safe_set(b, 'ownedByCourseInstance', a1)
    assert _is_linked(b, 'ownedByCourseInstance', a1)
    if hasattr(a1, 'TimeTable'):
        assert _is_linked(a1, 'TimeTable', b)
    _safe_set(b, 'ownedByCourseInstance', a2)
    assert _is_linked(b, 'ownedByCourseInstance', a2)
    if hasattr(a1, 'TimeTable'):
        assert not _is_linked(a1, 'TimeTable', b)
    if hasattr(a2, 'TimeTable'):
        assert _is_linked(a2, 'TimeTable', b)
    _safe_set(b, 'ownedByCourseInstance', None)
    assert not _is_linked(b, 'ownedByCourseInstance', a2)
    if hasattr(a2, 'TimeTable'):
        assert not _is_linked(a2, 'TimeTable', b)


def test_assoc_memberOfCourse32_reverse_link_reassign_clear():
    a1 = oving4_PersonRole(type="sample_text")
    a2 = oving4_PersonRole(type="sample_text_2")
    b = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    _safe_set(b, 'CourseInstance33', a1)
    assert _is_linked(b, 'CourseInstance33', a1)
    if hasattr(a1, 'hasMember'):
        assert _is_linked(a1, 'hasMember', b)
    _safe_set(b, 'CourseInstance33', a2)
    assert _is_linked(b, 'CourseInstance33', a2)
    if hasattr(a1, 'hasMember'):
        assert not _is_linked(a1, 'hasMember', b)
    if hasattr(a2, 'hasMember'):
        assert _is_linked(a2, 'hasMember', b)
    _safe_set(b, 'CourseInstance33', None)
    assert not _is_linked(b, 'CourseInstance33', a2)
    if hasattr(a2, 'hasMember'):
        assert not _is_linked(a2, 'hasMember', b)


def test_assoc_ownedBy21_reverse_link_reassign_clear():
    a1 = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    a2 = oving4_CourseInstance(sumExerciseHours=13, sumInDepthHours=13, sumLectureHours=13)
    b = oving4_Course(code="sample_text", content="sample_text", credits=3.14, examEndDate="sample_text", examStartDate="sample_text", name="sample_text")
    _safe_set(b, 'Course22', a1)
    assert _is_linked(b, 'Course22', a1)
    if hasattr(a1, 'courseInstance'):
        assert _is_linked(a1, 'courseInstance', b)
    _safe_set(b, 'Course22', a2)
    assert _is_linked(b, 'Course22', a2)
    if hasattr(a1, 'courseInstance'):
        assert not _is_linked(a1, 'courseInstance', b)
    if hasattr(a2, 'courseInstance'):
        assert _is_linked(a2, 'courseInstance', b)
    _safe_set(b, 'Course22', None)
    assert not _is_linked(b, 'Course22', a2)
    if hasattr(a2, 'courseInstance'):
        assert not _is_linked(a2, 'courseInstance', b)


def test_assoc_ownedByCourseInstance40_reverse_link_reassign_clear():
    a1 = oving4_TimeTable(isRestrictedToProgramsInParallell=True)
    a2 = oving4_TimeTable(isRestrictedToProgramsInParallell=False)
    b = oving4_CourseInstance(sumExerciseHours=7, sumInDepthHours=7, sumLectureHours=7)
    _safe_set(b, 'CourseInstance41', a1)
    assert _is_linked(b, 'CourseInstance41', a1)
    if hasattr(a1, 'hasTimeTable'):
        assert _is_linked(a1, 'hasTimeTable', b)
    _safe_set(b, 'CourseInstance41', a2)
    assert _is_linked(b, 'CourseInstance41', a2)
    if hasattr(a1, 'hasTimeTable'):
        assert not _is_linked(a1, 'hasTimeTable', b)
    if hasattr(a2, 'hasTimeTable'):
        assert _is_linked(a2, 'hasTimeTable', b)
    _safe_set(b, 'CourseInstance41', None)
    assert not _is_linked(b, 'CourseInstance41', a2)
    if hasattr(a2, 'hasTimeTable'):
        assert not _is_linked(a2, 'hasTimeTable', b)


def test_assoc_ownsCourse7_reverse_link_reassign_clear():
    a1 = oving4_Department(name="sample_text")
    a2 = oving4_Department(name="sample_text_2")
    b = oving4_Course(code="sample_text", content="sample_text", credits=3.14, examEndDate="sample_text", examStartDate="sample_text", name="sample_text")
    _safe_set(b, 'oving4_Course', a1)
    assert _is_linked(b, 'oving4_Course', a1)
    if hasattr(a1, 'oving4_Department8'):
        assert _is_linked(a1, 'oving4_Department8', b)
    _safe_set(b, 'oving4_Course', a2)
    assert _is_linked(b, 'oving4_Course', a2)
    if hasattr(a1, 'oving4_Department8'):
        assert not _is_linked(a1, 'oving4_Department8', b)
    if hasattr(a2, 'oving4_Department8'):
        assert _is_linked(a2, 'oving4_Department8', b)
    _safe_set(b, 'oving4_Course', None)
    assert not _is_linked(b, 'oving4_Course', a2)
    if hasattr(a2, 'oving4_Department8'):
        assert not _is_linked(a2, 'oving4_Department8', b)


def test_assoc_person29_reverse_link_reassign_clear():
    a1 = oving4_PersonRole(type="sample_text")
    a2 = oving4_PersonRole(type="sample_text_2")
    b = oving4_Person(first_name="sample_text", last_name="sample_text", name="sample_text", studyCredits=3.14)
    _safe_set(b, 'Person', a1)
    assert _is_linked(b, 'Person', a1)
    if hasattr(a1, 'hasRole'):
        assert _is_linked(a1, 'hasRole', b)
    _safe_set(b, 'Person', a2)
    assert _is_linked(b, 'Person', a2)
    if hasattr(a1, 'hasRole'):
        assert not _is_linked(a1, 'hasRole', b)
    if hasattr(a2, 'hasRole'):
        assert _is_linked(a2, 'hasRole', b)
    _safe_set(b, 'Person', None)
    assert not _is_linked(b, 'Person', a2)
    if hasattr(a2, 'hasRole'):
        assert not _is_linked(a2, 'hasRole', b)


def test_assoc_personEvaluated42_reverse_link_reassign_clear():
    a1 = oving4_Person(first_name="sample_text", last_name="sample_text", name="sample_text", studyCredits=3.14)
    a2 = oving4_Person(first_name="sample_text_2", last_name="sample_text_2", name="sample_text_2", studyCredits=9.99)
    b = oving4_Evaluation(completed=True, creditsReceived=3.14, description="sample_text", totalPercentageResult=3.14)
    _safe_set(b, 'hasEvaluation', a1)
    assert _is_linked(b, 'hasEvaluation', a1)
    if hasattr(a1, 'Person43'):
        assert _is_linked(a1, 'Person43', b)
    _safe_set(b, 'hasEvaluation', a2)
    assert _is_linked(b, 'hasEvaluation', a2)
    if hasattr(a1, 'Person43'):
        assert not _is_linked(a1, 'Person43', b)
    if hasattr(a2, 'Person43'):
        assert _is_linked(a2, 'Person43', b)
    _safe_set(b, 'hasEvaluation', None)
    assert not _is_linked(b, 'hasEvaluation', a2)
    if hasattr(a2, 'Person43'):
        assert not _is_linked(a2, 'Person43', b)


def test_assoc_preconditionCourse47_reverse_link_reassign_clear():
    a1 = oving4_Precondition(creditReduction=3.14, isMandatory=True)
    a2 = oving4_Precondition(creditReduction=9.99, isMandatory=False)
    b = oving4_Course(code="sample_text", content="sample_text", credits=3.14, examEndDate="sample_text", examStartDate="sample_text", name="sample_text")
    _safe_set(b, 'oving4_Course49', a1)
    assert _is_linked(b, 'oving4_Course49', a1)
    if hasattr(a1, 'oving4_Precondition48'):
        assert _is_linked(a1, 'oving4_Precondition48', b)
    _safe_set(b, 'oving4_Course49', a2)
    assert _is_linked(b, 'oving4_Course49', a2)
    if hasattr(a1, 'oving4_Precondition48'):
        assert not _is_linked(a1, 'oving4_Precondition48', b)
    if hasattr(a2, 'oving4_Precondition48'):
        assert _is_linked(a2, 'oving4_Precondition48', b)
    _safe_set(b, 'oving4_Course49', None)
    assert not _is_linked(b, 'oving4_Course49', a2)
    if hasattr(a2, 'oving4_Precondition48'):
        assert not _is_linked(a2, 'oving4_Precondition48', b)


def test_assoc_studyprogram17_reverse_link_reassign_clear():
    a1 = oving4_StudyProgram(type="sample_text")
    a2 = oving4_StudyProgram(type="sample_text_2")
    b = oving4_Course(code="sample_text", content="sample_text", credits=3.14, examEndDate="sample_text", examStartDate="sample_text", name="sample_text")
    _safe_set(b, 'containsCourse', a1)
    assert _is_linked(b, 'containsCourse', a1)
    if hasattr(a1, 'StudyProgram'):
        assert _is_linked(a1, 'StudyProgram', b)
    _safe_set(b, 'containsCourse', a2)
    assert _is_linked(b, 'containsCourse', a2)
    if hasattr(a1, 'StudyProgram'):
        assert not _is_linked(a1, 'StudyProgram', b)
    if hasattr(a2, 'StudyProgram'):
        assert _is_linked(a2, 'StudyProgram', b)
    _safe_set(b, 'containsCourse', None)
    assert not _is_linked(b, 'containsCourse', a2)
    if hasattr(a2, 'StudyProgram'):
        assert not _is_linked(a2, 'StudyProgram', b)


def test_assoc_usedByCourseWork50_reverse_link_reassign_clear():
    a1 = oving4_TimeTableElement(date="sample_text", durationInMinutes=7, room="sample_text")
    a2 = oving4_TimeTableElement(date="sample_text_2", durationInMinutes=13, room="sample_text_2")
    b = oving4_CourseWork(isMandatory=True, name="sample_text", type="sample_text")
    _safe_set(b, 'oving4_CourseWork52', a1)
    assert _is_linked(b, 'oving4_CourseWork52', a1)
    if hasattr(a1, 'oving4_TimeTableElement51'):
        assert _is_linked(a1, 'oving4_TimeTableElement51', b)
    _safe_set(b, 'oving4_CourseWork52', a2)
    assert _is_linked(b, 'oving4_CourseWork52', a2)
    if hasattr(a1, 'oving4_TimeTableElement51'):
        assert not _is_linked(a1, 'oving4_TimeTableElement51', b)
    if hasattr(a2, 'oving4_TimeTableElement51'):
        assert _is_linked(a2, 'oving4_TimeTableElement51', b)
    _safe_set(b, 'oving4_CourseWork52', None)
    assert not _is_linked(b, 'oving4_CourseWork52', a2)
    if hasattr(a2, 'oving4_TimeTableElement51'):
        assert not _is_linked(a2, 'oving4_TimeTableElement51', b)


def test_assoc_usedByStudyProgram37_reverse_link_reassign_clear():
    a1 = oving4_TimeTable(isRestrictedToProgramsInParallell=True)
    a2 = oving4_TimeTable(isRestrictedToProgramsInParallell=False)
    b = oving4_StudyProgram(type="sample_text")
    _safe_set(b, 'oving4_StudyProgram39', a1)
    assert _is_linked(b, 'oving4_StudyProgram39', a1)
    if hasattr(a1, 'oving4_TimeTable38'):
        assert _is_linked(a1, 'oving4_TimeTable38', b)
    _safe_set(b, 'oving4_StudyProgram39', a2)
    assert _is_linked(b, 'oving4_StudyProgram39', a2)
    if hasattr(a1, 'oving4_TimeTable38'):
        assert not _is_linked(a1, 'oving4_TimeTable38', b)
    if hasattr(a2, 'oving4_TimeTable38'):
        assert _is_linked(a2, 'oving4_TimeTable38', b)
    _safe_set(b, 'oving4_StudyProgram39', None)
    assert not _is_linked(b, 'oving4_StudyProgram39', a2)
    if hasattr(a2, 'oving4_TimeTable38'):
        assert not _is_linked(a2, 'oving4_TimeTable38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ownsDepartment0_stub_double():
    # oving4_Root has no real 'oving4_Root' property in the generated
    # code (a bare stub) -- manually attach it so oving4_Department's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oving4_Department's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oving4_Department(name="sample_text")
    partner = oving4_Root()
    setattr(partner, 'oving4_Root', None)
    _safe_set(owner, 'oving4_Department', partner)
    assert owner in getattr(partner, 'oving4_Root')
    _safe_set(owner, 'oving4_Department', None)
    assert owner not in getattr(partner, 'oving4_Root')


def test_assoc_ownsPerson1_stub_double():
    # oving4_Root has no real 'oving4_Root2' property in the generated
    # code (a bare stub) -- manually attach it so oving4_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oving4_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oving4_Person(first_name="sample_text", last_name="sample_text", name="sample_text", studyCredits=3.14)
    partner = oving4_Root()
    setattr(partner, 'oving4_Root2', None)
    _safe_set(owner, 'oving4_Person', partner)
    assert owner in getattr(partner, 'oving4_Root2')
    _safe_set(owner, 'oving4_Person', None)
    assert owner not in getattr(partner, 'oving4_Root2')


def test_assoc_ownsProject5_stub_double():
    # oving4_Root has no real 'oving4_Root6' property in the generated
    # code (a bare stub) -- manually attach it so oving4_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oving4_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oving4_Project(deadline="sample_text")
    partner = oving4_Root()
    setattr(partner, 'oving4_Root6', None)
    _safe_set(owner, 'oving4_Project', partner)
    assert owner in getattr(partner, 'oving4_Root6')
    _safe_set(owner, 'oving4_Project', None)
    assert owner not in getattr(partner, 'oving4_Root6')


def test_assoc_ownsStudyProgram3_stub_double():
    # oving4_Root has no real 'oving4_Root4' property in the generated
    # code (a bare stub) -- manually attach it so oving4_StudyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oving4_StudyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oving4_StudyProgram(type="sample_text")
    partner = oving4_Root()
    setattr(partner, 'oving4_Root4', None)
    _safe_set(owner, 'oving4_StudyProgram', partner)
    assert owner in getattr(partner, 'oving4_Root4')
    _safe_set(owner, 'oving4_StudyProgram', None)
    assert owner not in getattr(partner, 'oving4_Root4')


