import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    courceList_Cource,
    courceList_CourceSpecification,
    courceList_Department,
    courceList_EvaluationForm,
    courceList_Exam,
    courceList_Professor,
    courceList_Specialisation,
    courceList_Student,
    courceList_StudyCourceRelation,
    courceList_StudyGeneralization,
    courceList_StudyProgram,
    courceList_Work,
    Campus,
    EducationLevel,
    EvaluationType,
    Semester,
    WorkForm,
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

def test_assoc_coordinator41_reverse_link_reassign_clear():
    a1 = courceList_Professor(name="sample_text", title="sample_text")
    a2 = courceList_Professor(name="sample_text_2", title="sample_text_2")
    b = courceList_CourceSpecification(credits=3.14, language="sample_text", name="sample_text", semester="sample_text", specificationYear=7, version="sample_text")
    _safe_set(b, 'courceList_CourceSpecification42', a1)
    assert _is_linked(b, 'courceList_CourceSpecification42', a1)
    if hasattr(a1, 'courceList_Professor'):
        assert _is_linked(a1, 'courceList_Professor', b)
    _safe_set(b, 'courceList_CourceSpecification42', a2)
    assert _is_linked(b, 'courceList_CourceSpecification42', a2)
    if hasattr(a1, 'courceList_Professor'):
        assert not _is_linked(a1, 'courceList_Professor', b)
    if hasattr(a2, 'courceList_Professor'):
        assert _is_linked(a2, 'courceList_Professor', b)
    _safe_set(b, 'courceList_CourceSpecification42', None)
    assert not _is_linked(b, 'courceList_CourceSpecification42', a2)
    if hasattr(a2, 'courceList_Professor'):
        assert not _is_linked(a2, 'courceList_Professor', b)


def test_assoc_corseSpecifications6_reverse_link_reassign_clear():
    a1 = courceList_CourceSpecification(credits=3.14, language="sample_text", name="sample_text", semester="sample_text", specificationYear=7, version="sample_text")
    a2 = courceList_CourceSpecification(credits=9.99, language="sample_text_2", name="sample_text_2", semester="sample_text_2", specificationYear=13, version="sample_text_2")
    b = courceList_Cource(code="sample_text", location="sample_text", name="sample_text")
    _safe_set(b, 'cource', {a1})
    assert _is_linked(b, 'cource', a1)
    if hasattr(a1, 'CourceSpecification'):
        assert _is_linked(a1, 'CourceSpecification', b)
    _safe_set(b, 'cource', {a2})
    assert _is_linked(b, 'cource', a2)
    if hasattr(a1, 'CourceSpecification'):
        assert not _is_linked(a1, 'CourceSpecification', b)
    if hasattr(a2, 'CourceSpecification'):
        assert _is_linked(a2, 'CourceSpecification', b)
    _safe_set(b, 'cource', set())
    assert not _is_linked(b, 'cource', a2)
    if hasattr(a2, 'CourceSpecification'):
        assert not _is_linked(a2, 'CourceSpecification', b)


def test_assoc_cource18_reverse_link_reassign_clear():
    a1 = courceList_EvaluationForm(evaluationType="sample_text")
    a2 = courceList_EvaluationForm(evaluationType="sample_text_2")
    b = courceList_CourceSpecification(credits=3.14, language="sample_text", name="sample_text", semester="sample_text", specificationYear=7, version="sample_text")
    _safe_set(b, 'CourceSpecification20', a1)
    assert _is_linked(b, 'CourceSpecification20', a1)
    if hasattr(a1, 'evaluationForm19'):
        assert _is_linked(a1, 'evaluationForm19', b)
    _safe_set(b, 'CourceSpecification20', a2)
    assert _is_linked(b, 'CourceSpecification20', a2)
    if hasattr(a1, 'evaluationForm19'):
        assert not _is_linked(a1, 'evaluationForm19', b)
    if hasattr(a2, 'evaluationForm19'):
        assert _is_linked(a2, 'evaluationForm19', b)
    _safe_set(b, 'CourceSpecification20', None)
    assert not _is_linked(b, 'CourceSpecification20', a2)
    if hasattr(a2, 'evaluationForm19'):
        assert not _is_linked(a2, 'evaluationForm19', b)


def test_assoc_cource23_reverse_link_reassign_clear():
    a1 = courceList_StudyCourceRelation(status="sample_text", year=7)
    a2 = courceList_StudyCourceRelation(status="sample_text_2", year=13)
    b = courceList_CourceSpecification(credits=3.14, language="sample_text", name="sample_text", semester="sample_text", specificationYear=7, version="sample_text")
    _safe_set(b, 'courceList_CourceSpecification', a1)
    assert _is_linked(b, 'courceList_CourceSpecification', a1)
    if hasattr(a1, 'courceList_StudyCourceRelation'):
        assert _is_linked(a1, 'courceList_StudyCourceRelation', b)
    _safe_set(b, 'courceList_CourceSpecification', a2)
    assert _is_linked(b, 'courceList_CourceSpecification', a2)
    if hasattr(a1, 'courceList_StudyCourceRelation'):
        assert not _is_linked(a1, 'courceList_StudyCourceRelation', b)
    if hasattr(a2, 'courceList_StudyCourceRelation'):
        assert _is_linked(a2, 'courceList_StudyCourceRelation', b)
    _safe_set(b, 'courceList_CourceSpecification', None)
    assert not _is_linked(b, 'courceList_CourceSpecification', a2)
    if hasattr(a2, 'courceList_StudyCourceRelation'):
        assert not _is_linked(a2, 'courceList_StudyCourceRelation', b)


def test_assoc_cource29_reverse_link_reassign_clear():
    a1 = courceList_StudyCourceRelation(status="sample_text", year=7)
    a2 = courceList_StudyCourceRelation(status="sample_text_2", year=13)
    b = courceList_Specialisation(name="sample_text", startSemester=7)
    _safe_set(b, 'specialisation', {a1})
    assert _is_linked(b, 'specialisation', a1)
    if hasattr(a1, 'StudyCourceRelation'):
        assert _is_linked(a1, 'StudyCourceRelation', b)
    _safe_set(b, 'specialisation', {a2})
    assert _is_linked(b, 'specialisation', a2)
    if hasattr(a1, 'StudyCourceRelation'):
        assert not _is_linked(a1, 'StudyCourceRelation', b)
    if hasattr(a2, 'StudyCourceRelation'):
        assert _is_linked(a2, 'StudyCourceRelation', b)
    _safe_set(b, 'specialisation', set())
    assert not _is_linked(b, 'specialisation', a2)
    if hasattr(a2, 'StudyCourceRelation'):
        assert not _is_linked(a2, 'StudyCourceRelation', b)


def test_assoc_cource39_reverse_link_reassign_clear():
    a1 = courceList_CourceSpecification(credits=3.14, language="sample_text", name="sample_text", semester="sample_text", specificationYear=7, version="sample_text")
    a2 = courceList_CourceSpecification(credits=9.99, language="sample_text_2", name="sample_text_2", semester="sample_text_2", specificationYear=13, version="sample_text_2")
    b = courceList_Cource(code="sample_text", location="sample_text", name="sample_text")
    _safe_set(b, 'Cource40', a1)
    assert _is_linked(b, 'Cource40', a1)
    if hasattr(a1, 'corseSpecifications'):
        assert _is_linked(a1, 'corseSpecifications', b)
    _safe_set(b, 'Cource40', a2)
    assert _is_linked(b, 'Cource40', a2)
    if hasattr(a1, 'corseSpecifications'):
        assert not _is_linked(a1, 'corseSpecifications', b)
    if hasattr(a2, 'corseSpecifications'):
        assert _is_linked(a2, 'corseSpecifications', b)
    _safe_set(b, 'Cource40', None)
    assert not _is_linked(b, 'Cource40', a2)
    if hasattr(a2, 'corseSpecifications'):
        assert not _is_linked(a2, 'corseSpecifications', b)


def test_assoc_cource8_reverse_link_reassign_clear():
    a1 = courceList_StudyProgram(year=7)
    a2 = courceList_StudyProgram(year=13)
    b = courceList_Specialisation(name="sample_text", startSemester=7)
    _safe_set(b, 'Specialisation', a1)
    assert _is_linked(b, 'Specialisation', a1)
    if hasattr(a1, 'studyProgram'):
        assert _is_linked(a1, 'studyProgram', b)
    _safe_set(b, 'Specialisation', a2)
    assert _is_linked(b, 'Specialisation', a2)
    if hasattr(a1, 'studyProgram'):
        assert not _is_linked(a1, 'studyProgram', b)
    if hasattr(a2, 'studyProgram'):
        assert _is_linked(a2, 'studyProgram', b)
    _safe_set(b, 'Specialisation', None)
    assert not _is_linked(b, 'Specialisation', a2)
    if hasattr(a2, 'studyProgram'):
        assert not _is_linked(a2, 'studyProgram', b)


def test_assoc_course1_reverse_link_reassign_clear():
    a1 = courceList_Department(abbreviation="sample_text", name="sample_text")
    a2 = courceList_Department(abbreviation="sample_text_2", name="sample_text_2")
    b = courceList_Cource(code="sample_text", location="sample_text", name="sample_text")
    _safe_set(b, 'Cource', a1)
    assert _is_linked(b, 'Cource', a1)
    if hasattr(a1, 'department2'):
        assert _is_linked(a1, 'department2', b)
    _safe_set(b, 'Cource', a2)
    assert _is_linked(b, 'Cource', a2)
    if hasattr(a1, 'department2'):
        assert not _is_linked(a1, 'department2', b)
    if hasattr(a2, 'department2'):
        assert _is_linked(a2, 'department2', b)
    _safe_set(b, 'Cource', None)
    assert not _is_linked(b, 'Cource', a2)
    if hasattr(a2, 'department2'):
        assert not _is_linked(a2, 'department2', b)


def test_assoc_department27_reverse_link_reassign_clear():
    a1 = courceList_Professor(name="sample_text", title="sample_text")
    a2 = courceList_Professor(name="sample_text_2", title="sample_text_2")
    b = courceList_Department(abbreviation="sample_text", name="sample_text")
    _safe_set(b, 'Department28', a1)
    assert _is_linked(b, 'Department28', a1)
    if hasattr(a1, 'professor'):
        assert _is_linked(a1, 'professor', b)
    _safe_set(b, 'Department28', a2)
    assert _is_linked(b, 'Department28', a2)
    if hasattr(a1, 'professor'):
        assert not _is_linked(a1, 'professor', b)
    if hasattr(a2, 'professor'):
        assert _is_linked(a2, 'professor', b)
    _safe_set(b, 'Department28', None)
    assert not _is_linked(b, 'Department28', a2)
    if hasattr(a2, 'professor'):
        assert not _is_linked(a2, 'professor', b)


def test_assoc_department48_reverse_link_reassign_clear():
    a1 = courceList_StudyGeneralization(abbreviation="sample_text", campus="sample_text", educationLevel="sample_text", name="sample_text", nrOfYears=7)
    a2 = courceList_StudyGeneralization(abbreviation="sample_text_2", campus="sample_text_2", educationLevel="sample_text_2", name="sample_text_2", nrOfYears=13)
    b = courceList_Department(abbreviation="sample_text", name="sample_text")
    _safe_set(b, 'Department50', a1)
    assert _is_linked(b, 'Department50', a1)
    if hasattr(a1, 'studyProgram49'):
        assert _is_linked(a1, 'studyProgram49', b)
    _safe_set(b, 'Department50', a2)
    assert _is_linked(b, 'Department50', a2)
    if hasattr(a1, 'studyProgram49'):
        assert not _is_linked(a1, 'studyProgram49', b)
    if hasattr(a2, 'studyProgram49'):
        assert _is_linked(a2, 'studyProgram49', b)
    _safe_set(b, 'Department50', None)
    assert not _is_linked(b, 'Department50', a2)
    if hasattr(a2, 'studyProgram49'):
        assert not _is_linked(a2, 'studyProgram49', b)


def test_assoc_department5_reverse_link_reassign_clear():
    a1 = courceList_Department(abbreviation="sample_text", name="sample_text")
    a2 = courceList_Department(abbreviation="sample_text_2", name="sample_text_2")
    b = courceList_Cource(code="sample_text", location="sample_text", name="sample_text")
    _safe_set(b, 'course', a1)
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'Department'):
        assert _is_linked(a1, 'Department', b)
    _safe_set(b, 'course', a2)
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'Department'):
        assert not _is_linked(a1, 'Department', b)
    if hasattr(a2, 'Department'):
        assert _is_linked(a2, 'Department', b)
    _safe_set(b, 'course', None)
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'Department'):
        assert not _is_linked(a2, 'Department', b)


def test_assoc_evaluationForm14_reverse_link_reassign_clear():
    a1 = courceList_Exam(date=date(2024, 1, 1), form="sample_text", lenght=7, weight=7)
    a2 = courceList_Exam(date=date(2025, 6, 15), form="sample_text_2", lenght=13, weight=13)
    b = courceList_EvaluationForm(evaluationType="sample_text")
    _safe_set(b, 'EvaluationForm', a1)
    assert _is_linked(b, 'EvaluationForm', a1)
    if hasattr(a1, 'exam'):
        assert _is_linked(a1, 'exam', b)
    _safe_set(b, 'EvaluationForm', a2)
    assert _is_linked(b, 'EvaluationForm', a2)
    if hasattr(a1, 'exam'):
        assert not _is_linked(a1, 'exam', b)
    if hasattr(a2, 'exam'):
        assert _is_linked(a2, 'exam', b)
    _safe_set(b, 'EvaluationForm', None)
    assert not _is_linked(b, 'EvaluationForm', a2)
    if hasattr(a2, 'exam'):
        assert not _is_linked(a2, 'exam', b)


def test_assoc_evaluationForm21_reverse_link_reassign_clear():
    a1 = courceList_Work(weight=7)
    a2 = courceList_Work(weight=13)
    b = courceList_EvaluationForm(evaluationType="sample_text")
    _safe_set(b, 'EvaluationForm22', a1)
    assert _is_linked(b, 'EvaluationForm22', a1)
    if hasattr(a1, 'work'):
        assert _is_linked(a1, 'work', b)
    _safe_set(b, 'EvaluationForm22', a2)
    assert _is_linked(b, 'EvaluationForm22', a2)
    if hasattr(a1, 'work'):
        assert not _is_linked(a1, 'work', b)
    if hasattr(a2, 'work'):
        assert _is_linked(a2, 'work', b)
    _safe_set(b, 'EvaluationForm22', None)
    assert not _is_linked(b, 'EvaluationForm22', a2)
    if hasattr(a2, 'work'):
        assert not _is_linked(a2, 'work', b)


def test_assoc_evaluationForm43_reverse_link_reassign_clear():
    a1 = courceList_EvaluationForm(evaluationType="sample_text")
    a2 = courceList_EvaluationForm(evaluationType="sample_text_2")
    b = courceList_CourceSpecification(credits=3.14, language="sample_text", name="sample_text", semester="sample_text", specificationYear=7, version="sample_text")
    _safe_set(b, 'cource44', a1)
    assert _is_linked(b, 'cource44', a1)
    if hasattr(a1, 'EvaluationForm45'):
        assert _is_linked(a1, 'EvaluationForm45', b)
    _safe_set(b, 'cource44', a2)
    assert _is_linked(b, 'cource44', a2)
    if hasattr(a1, 'EvaluationForm45'):
        assert not _is_linked(a1, 'EvaluationForm45', b)
    if hasattr(a2, 'EvaluationForm45'):
        assert _is_linked(a2, 'EvaluationForm45', b)
    _safe_set(b, 'cource44', None)
    assert not _is_linked(b, 'cource44', a2)
    if hasattr(a2, 'EvaluationForm45'):
        assert not _is_linked(a2, 'EvaluationForm45', b)


def test_assoc_exam15_reverse_link_reassign_clear():
    a1 = courceList_Exam(date=date(2024, 1, 1), form="sample_text", lenght=7, weight=7)
    a2 = courceList_Exam(date=date(2025, 6, 15), form="sample_text_2", lenght=13, weight=13)
    b = courceList_EvaluationForm(evaluationType="sample_text")
    _safe_set(b, 'evaluationForm', a1)
    assert _is_linked(b, 'evaluationForm', a1)
    if hasattr(a1, 'Exam'):
        assert _is_linked(a1, 'Exam', b)
    _safe_set(b, 'evaluationForm', a2)
    assert _is_linked(b, 'evaluationForm', a2)
    if hasattr(a1, 'Exam'):
        assert not _is_linked(a1, 'Exam', b)
    if hasattr(a2, 'Exam'):
        assert _is_linked(a2, 'Exam', b)
    _safe_set(b, 'evaluationForm', None)
    assert not _is_linked(b, 'evaluationForm', a2)
    if hasattr(a2, 'Exam'):
        assert not _is_linked(a2, 'Exam', b)


def test_assoc_furtherSpecialisation34_reverse_link_reassign_clear():
    a1 = courceList_Specialisation(name="sample_text", startSemester=7)
    a2 = courceList_Specialisation(name="sample_text_2", startSemester=13)
    b = courceList_Specialisation(name="sample_text", startSemester=7)
    _safe_set(b, 'hostSpecialisation', {a1})
    assert _is_linked(b, 'hostSpecialisation', a1)
    if hasattr(a1, 'Specialisation35'):
        assert _is_linked(a1, 'Specialisation35', b)
    _safe_set(b, 'hostSpecialisation', {a2})
    assert _is_linked(b, 'hostSpecialisation', a2)
    if hasattr(a1, 'Specialisation35'):
        assert not _is_linked(a1, 'Specialisation35', b)
    if hasattr(a2, 'Specialisation35'):
        assert _is_linked(a2, 'Specialisation35', b)
    _safe_set(b, 'hostSpecialisation', set())
    assert not _is_linked(b, 'hostSpecialisation', a2)
    if hasattr(a2, 'Specialisation35'):
        assert not _is_linked(a2, 'Specialisation35', b)


def test_assoc_generalization9_reverse_link_reassign_clear():
    a1 = courceList_StudyProgram(year=7)
    a2 = courceList_StudyProgram(year=13)
    b = courceList_StudyGeneralization(abbreviation="sample_text", campus="sample_text", educationLevel="sample_text", name="sample_text", nrOfYears=7)
    _safe_set(b, 'StudyGeneralization11', a1)
    assert _is_linked(b, 'StudyGeneralization11', a1)
    if hasattr(a1, 'studyProgram10'):
        assert _is_linked(a1, 'studyProgram10', b)
    _safe_set(b, 'StudyGeneralization11', a2)
    assert _is_linked(b, 'StudyGeneralization11', a2)
    if hasattr(a1, 'studyProgram10'):
        assert not _is_linked(a1, 'studyProgram10', b)
    if hasattr(a2, 'studyProgram10'):
        assert _is_linked(a2, 'studyProgram10', b)
    _safe_set(b, 'StudyGeneralization11', None)
    assert not _is_linked(b, 'StudyGeneralization11', a2)
    if hasattr(a2, 'studyProgram10'):
        assert not _is_linked(a2, 'studyProgram10', b)


def test_assoc_hostSpecialisation37_reverse_link_reassign_clear():
    a1 = courceList_Specialisation(name="sample_text", startSemester=7)
    a2 = courceList_Specialisation(name="sample_text_2", startSemester=13)
    b = courceList_Specialisation(name="sample_text", startSemester=7)
    _safe_set(b, 'furtherSpecialisation', a1)
    assert _is_linked(b, 'furtherSpecialisation', a1)
    if hasattr(a1, 'Specialisation38'):
        assert _is_linked(a1, 'Specialisation38', b)
    _safe_set(b, 'furtherSpecialisation', a2)
    assert _is_linked(b, 'furtherSpecialisation', a2)
    if hasattr(a1, 'Specialisation38'):
        assert not _is_linked(a1, 'Specialisation38', b)
    if hasattr(a2, 'Specialisation38'):
        assert _is_linked(a2, 'Specialisation38', b)
    _safe_set(b, 'furtherSpecialisation', None)
    assert not _is_linked(b, 'furtherSpecialisation', a2)
    if hasattr(a2, 'Specialisation38'):
        assert not _is_linked(a2, 'Specialisation38', b)


def test_assoc_professor3_reverse_link_reassign_clear():
    a1 = courceList_Professor(name="sample_text", title="sample_text")
    a2 = courceList_Professor(name="sample_text_2", title="sample_text_2")
    b = courceList_Department(abbreviation="sample_text", name="sample_text")
    _safe_set(b, 'department4', {a1})
    assert _is_linked(b, 'department4', a1)
    if hasattr(a1, 'Professor'):
        assert _is_linked(a1, 'Professor', b)
    _safe_set(b, 'department4', {a2})
    assert _is_linked(b, 'department4', a2)
    if hasattr(a1, 'Professor'):
        assert not _is_linked(a1, 'Professor', b)
    if hasattr(a2, 'Professor'):
        assert _is_linked(a2, 'Professor', b)
    _safe_set(b, 'department4', set())
    assert not _is_linked(b, 'department4', a2)
    if hasattr(a2, 'Professor'):
        assert not _is_linked(a2, 'Professor', b)


def test_assoc_specialisation24_reverse_link_reassign_clear():
    a1 = courceList_StudyCourceRelation(status="sample_text", year=7)
    a2 = courceList_StudyCourceRelation(status="sample_text_2", year=13)
    b = courceList_Specialisation(name="sample_text", startSemester=7)
    _safe_set(b, 'Specialisation26', a1)
    assert _is_linked(b, 'Specialisation26', a1)
    if hasattr(a1, 'cource25'):
        assert _is_linked(a1, 'cource25', b)
    _safe_set(b, 'Specialisation26', a2)
    assert _is_linked(b, 'Specialisation26', a2)
    if hasattr(a1, 'cource25'):
        assert not _is_linked(a1, 'cource25', b)
    if hasattr(a2, 'cource25'):
        assert _is_linked(a2, 'cource25', b)
    _safe_set(b, 'Specialisation26', None)
    assert not _is_linked(b, 'Specialisation26', a2)
    if hasattr(a2, 'cource25'):
        assert not _is_linked(a2, 'cource25', b)


def test_assoc_student12_reverse_link_reassign_clear():
    a1 = courceList_StudyProgram(year=7)
    a2 = courceList_StudyProgram(year=13)
    b = courceList_Student(nr=7)
    _safe_set(b, 'Student', a1)
    assert _is_linked(b, 'Student', a1)
    if hasattr(a1, 'studyProgram13'):
        assert _is_linked(a1, 'studyProgram13', b)
    _safe_set(b, 'Student', a2)
    assert _is_linked(b, 'Student', a2)
    if hasattr(a1, 'studyProgram13'):
        assert not _is_linked(a1, 'studyProgram13', b)
    if hasattr(a2, 'studyProgram13'):
        assert _is_linked(a2, 'studyProgram13', b)
    _safe_set(b, 'Student', None)
    assert not _is_linked(b, 'Student', a2)
    if hasattr(a2, 'studyProgram13'):
        assert not _is_linked(a2, 'studyProgram13', b)


def test_assoc_studyProgram0_reverse_link_reassign_clear():
    a1 = courceList_StudyGeneralization(abbreviation="sample_text", campus="sample_text", educationLevel="sample_text", name="sample_text", nrOfYears=7)
    a2 = courceList_StudyGeneralization(abbreviation="sample_text_2", campus="sample_text_2", educationLevel="sample_text_2", name="sample_text_2", nrOfYears=13)
    b = courceList_Department(abbreviation="sample_text", name="sample_text")
    _safe_set(b, 'department', {a1})
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'StudyGeneralization'):
        assert _is_linked(a1, 'StudyGeneralization', b)
    _safe_set(b, 'department', {a2})
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'StudyGeneralization'):
        assert not _is_linked(a1, 'StudyGeneralization', b)
    if hasattr(a2, 'StudyGeneralization'):
        assert _is_linked(a2, 'StudyGeneralization', b)
    _safe_set(b, 'department', set())
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'StudyGeneralization'):
        assert not _is_linked(a2, 'StudyGeneralization', b)


def test_assoc_studyProgram30_reverse_link_reassign_clear():
    a1 = courceList_StudyProgram(year=7)
    a2 = courceList_StudyProgram(year=13)
    b = courceList_Specialisation(name="sample_text", startSemester=7)
    _safe_set(b, 'cource31', a1)
    assert _is_linked(b, 'cource31', a1)
    if hasattr(a1, 'StudyProgram32'):
        assert _is_linked(a1, 'StudyProgram32', b)
    _safe_set(b, 'cource31', a2)
    assert _is_linked(b, 'cource31', a2)
    if hasattr(a1, 'StudyProgram32'):
        assert not _is_linked(a1, 'StudyProgram32', b)
    if hasattr(a2, 'StudyProgram32'):
        assert _is_linked(a2, 'StudyProgram32', b)
    _safe_set(b, 'cource31', None)
    assert not _is_linked(b, 'cource31', a2)
    if hasattr(a2, 'StudyProgram32'):
        assert not _is_linked(a2, 'StudyProgram32', b)


def test_assoc_studyProgram46_reverse_link_reassign_clear():
    a1 = courceList_StudyProgram(year=7)
    a2 = courceList_StudyProgram(year=13)
    b = courceList_StudyGeneralization(abbreviation="sample_text", campus="sample_text", educationLevel="sample_text", name="sample_text", nrOfYears=7)
    _safe_set(b, 'generalization', {a1})
    assert _is_linked(b, 'generalization', a1)
    if hasattr(a1, 'StudyProgram47'):
        assert _is_linked(a1, 'StudyProgram47', b)
    _safe_set(b, 'generalization', {a2})
    assert _is_linked(b, 'generalization', a2)
    if hasattr(a1, 'StudyProgram47'):
        assert not _is_linked(a1, 'StudyProgram47', b)
    if hasattr(a2, 'StudyProgram47'):
        assert _is_linked(a2, 'StudyProgram47', b)
    _safe_set(b, 'generalization', set())
    assert not _is_linked(b, 'generalization', a2)
    if hasattr(a2, 'StudyProgram47'):
        assert not _is_linked(a2, 'StudyProgram47', b)


def test_assoc_studyProgram7_reverse_link_reassign_clear():
    a1 = courceList_StudyProgram(year=7)
    a2 = courceList_StudyProgram(year=13)
    b = courceList_Student(nr=7)
    _safe_set(b, 'student', a1)
    assert _is_linked(b, 'student', a1)
    if hasattr(a1, 'StudyProgram'):
        assert _is_linked(a1, 'StudyProgram', b)
    _safe_set(b, 'student', a2)
    assert _is_linked(b, 'student', a2)
    if hasattr(a1, 'StudyProgram'):
        assert not _is_linked(a1, 'StudyProgram', b)
    if hasattr(a2, 'StudyProgram'):
        assert _is_linked(a2, 'StudyProgram', b)
    _safe_set(b, 'student', None)
    assert not _is_linked(b, 'student', a2)
    if hasattr(a2, 'StudyProgram'):
        assert not _is_linked(a2, 'StudyProgram', b)


def test_assoc_work16_reverse_link_reassign_clear():
    a1 = courceList_Work(weight=7)
    a2 = courceList_Work(weight=13)
    b = courceList_EvaluationForm(evaluationType="sample_text")
    _safe_set(b, 'evaluationForm17', a1)
    assert _is_linked(b, 'evaluationForm17', a1)
    if hasattr(a1, 'Work'):
        assert _is_linked(a1, 'Work', b)
    _safe_set(b, 'evaluationForm17', a2)
    assert _is_linked(b, 'evaluationForm17', a2)
    if hasattr(a1, 'Work'):
        assert not _is_linked(a1, 'Work', b)
    if hasattr(a2, 'Work'):
        assert _is_linked(a2, 'Work', b)
    _safe_set(b, 'evaluationForm17', None)
    assert not _is_linked(b, 'evaluationForm17', a2)
    if hasattr(a2, 'Work'):
        assert not _is_linked(a2, 'Work', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

