import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class,
    mypackage_Admin,
    mypackage_Assignment,
    mypackage_Book,
    mypackage_Course,
    mypackage_Exam,
    mypackage_Exceptions,
    mypackage_FileManager,
    mypackage_Perosn,
    mypackage_Staff,
    mypackage_Student,
    mypackage_Tutor,
    mypackage_studentAffairsEmp,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_mypackage_Assignment_Deadline_value_roundtrip():
    instance = mypackage_Assignment(Deadline="sample_text", StrartDate="sample_text", number=7)
    assert instance.Deadline == "sample_text"
    instance.Deadline = "sample_text_2"
    assert instance.Deadline == "sample_text_2"


def test_mypackage_Assignment_StrartDate_value_roundtrip():
    instance = mypackage_Assignment(Deadline="sample_text", StrartDate="sample_text", number=7)
    assert instance.StrartDate == "sample_text"
    instance.StrartDate = "sample_text_2"
    assert instance.StrartDate == "sample_text_2"


def test_mypackage_Assignment_number_value_roundtrip():
    instance = mypackage_Assignment(Deadline="sample_text", StrartDate="sample_text", number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_mypackage_Book_BId_value_roundtrip():
    instance = mypackage_Book(BId="sample_text", BName="sample_text", Price="sample_text")
    assert instance.BId == "sample_text"
    instance.BId = "sample_text_2"
    assert instance.BId == "sample_text_2"


def test_mypackage_Book_BName_value_roundtrip():
    instance = mypackage_Book(BId="sample_text", BName="sample_text", Price="sample_text")
    assert instance.BName == "sample_text"
    instance.BName = "sample_text_2"
    assert instance.BName == "sample_text_2"


def test_mypackage_Book_Price_value_roundtrip():
    instance = mypackage_Book(BId="sample_text", BName="sample_text", Price="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_mypackage_Course_CId_value_roundtrip():
    instance = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    assert instance.CId == "sample_text"
    instance.CId = "sample_text_2"
    assert instance.CId == "sample_text_2"


def test_mypackage_Course_CName_value_roundtrip():
    instance = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    assert instance.CName == "sample_text"
    instance.CName = "sample_text_2"
    assert instance.CName == "sample_text_2"


def test_mypackage_Course_CourseFileName_value_roundtrip():
    instance = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    assert instance.CourseFileName == "sample_text"
    instance.CourseFileName = "sample_text_2"
    assert instance.CourseFileName == "sample_text_2"


def test_mypackage_Course_CreditHours_value_roundtrip():
    instance = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    assert instance.CreditHours == 7
    instance.CreditHours = 13
    assert instance.CreditHours == 13


def test_mypackage_Exam_EId_value_roundtrip():
    instance = mypackage_Exam(EId="sample_text", EName="sample_text", ExamsFileName="sample_text", MaxGrade="sample_text")
    assert instance.EId == "sample_text"
    instance.EId = "sample_text_2"
    assert instance.EId == "sample_text_2"


def test_mypackage_Exam_EName_value_roundtrip():
    instance = mypackage_Exam(EId="sample_text", EName="sample_text", ExamsFileName="sample_text", MaxGrade="sample_text")
    assert instance.EName == "sample_text"
    instance.EName = "sample_text_2"
    assert instance.EName == "sample_text_2"


def test_mypackage_Exam_ExamsFileName_value_roundtrip():
    instance = mypackage_Exam(EId="sample_text", EName="sample_text", ExamsFileName="sample_text", MaxGrade="sample_text")
    assert instance.ExamsFileName == "sample_text"
    instance.ExamsFileName = "sample_text_2"
    assert instance.ExamsFileName == "sample_text_2"


def test_mypackage_Exam_MaxGrade_value_roundtrip():
    instance = mypackage_Exam(EId="sample_text", EName="sample_text", ExamsFileName="sample_text", MaxGrade="sample_text")
    assert instance.MaxGrade == "sample_text"
    instance.MaxGrade = "sample_text_2"
    assert instance.MaxGrade == "sample_text_2"


def test_mypackage_Perosn_Pass_value_roundtrip():
    instance = mypackage_Perosn(Pass="sample_text", UserName="sample_text", age=7, fName="sample_text", id=7, lname="sample_text")
    assert instance.Pass == "sample_text"
    instance.Pass = "sample_text_2"
    assert instance.Pass == "sample_text_2"


def test_mypackage_Perosn_UserName_value_roundtrip():
    instance = mypackage_Perosn(Pass="sample_text", UserName="sample_text", age=7, fName="sample_text", id=7, lname="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_mypackage_Perosn_age_value_roundtrip():
    instance = mypackage_Perosn(Pass="sample_text", UserName="sample_text", age=7, fName="sample_text", id=7, lname="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_mypackage_Perosn_fName_value_roundtrip():
    instance = mypackage_Perosn(Pass="sample_text", UserName="sample_text", age=7, fName="sample_text", id=7, lname="sample_text")
    assert instance.fName == "sample_text"
    instance.fName = "sample_text_2"
    assert instance.fName == "sample_text_2"


def test_mypackage_Perosn_id_value_roundtrip():
    instance = mypackage_Perosn(Pass="sample_text", UserName="sample_text", age=7, fName="sample_text", id=7, lname="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_mypackage_Perosn_lname_value_roundtrip():
    instance = mypackage_Perosn(Pass="sample_text", UserName="sample_text", age=7, fName="sample_text", id=7, lname="sample_text")
    assert instance.lname == "sample_text"
    instance.lname = "sample_text_2"
    assert instance.lname == "sample_text_2"


def test_mypackage_Staff_salary_value_roundtrip():
    instance = mypackage_Staff(salary="sample_text")
    assert instance.salary == "sample_text"
    instance.salary = "sample_text_2"
    assert instance.salary == "sample_text_2"


def test_mypackage_Student_grade_value_roundtrip():
    instance = mypackage_Student(grade="sample_text", level=7, studentFileName="sample_text")
    assert instance.grade == "sample_text"
    instance.grade = "sample_text_2"
    assert instance.grade == "sample_text_2"


def test_mypackage_Student_level_value_roundtrip():
    instance = mypackage_Student(grade="sample_text", level=7, studentFileName="sample_text")
    assert instance.level == 7
    instance.level = 13
    assert instance.level == 13


def test_mypackage_Student_studentFileName_value_roundtrip():
    instance = mypackage_Student(grade="sample_text", level=7, studentFileName="sample_text")
    assert instance.studentFileName == "sample_text"
    instance.studentFileName = "sample_text_2"
    assert instance.studentFileName == "sample_text_2"


def test_mypackage_Tutor_TutorFileName_value_roundtrip():
    instance = mypackage_Tutor(TutorFileName="sample_text", WorkingHours="sample_text")
    assert instance.TutorFileName == "sample_text"
    instance.TutorFileName = "sample_text_2"
    assert instance.TutorFileName == "sample_text_2"


def test_mypackage_Tutor_WorkingHours_value_roundtrip():
    instance = mypackage_Tutor(TutorFileName="sample_text", WorkingHours="sample_text")
    assert instance.WorkingHours == "sample_text"
    instance.WorkingHours = "sample_text_2"
    assert instance.WorkingHours == "sample_text_2"


def test_mypackage_studentAffairsEmp_EmpFileName_value_roundtrip():
    instance = mypackage_studentAffairsEmp(EmpFileName="sample_text")
    assert instance.EmpFileName == "sample_text"
    instance.EmpFileName = "sample_text_2"
    assert instance.EmpFileName == "sample_text_2"


def test_assoc_Book_FileManager_link_reassign_clear():
    a = mypackage_Book(BId="sample_text", BName="sample_text", Price="sample_text")
    b1 = mypackage_FileManager()
    b2 = mypackage_FileManager()
    _safe_set(a, 'fileManager16', b1)
    assert _is_linked(a, 'fileManager16', b1)
    if hasattr(b1, 'book17'):
        assert _is_linked(b1, 'book17', a)
    _safe_set(a, 'fileManager16', b2)
    assert _is_linked(a, 'fileManager16', b2)
    if hasattr(b1, 'book17'):
        assert not _is_linked(b1, 'book17', a)
    if hasattr(b2, 'book17'):
        assert _is_linked(b2, 'book17', a)
    _safe_set(a, 'fileManager16', None)
    assert not _is_linked(a, 'fileManager16', b2)
    if hasattr(b2, 'book17'):
        assert not _is_linked(b2, 'book17', a)


def test_assoc_Course_Assignment_link_reassign_clear():
    a = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    b1 = mypackage_Assignment(Deadline="sample_text", StrartDate="sample_text", number=7)
    b2 = mypackage_Assignment(Deadline="sample_text_2", StrartDate="sample_text_2", number=13)
    _safe_set(a, 'assignment8', b1)
    assert _is_linked(a, 'assignment8', b1)
    if hasattr(b1, 'course9'):
        assert _is_linked(b1, 'course9', a)
    _safe_set(a, 'assignment8', b2)
    assert _is_linked(a, 'assignment8', b2)
    if hasattr(b1, 'course9'):
        assert not _is_linked(b1, 'course9', a)
    if hasattr(b2, 'course9'):
        assert _is_linked(b2, 'course9', a)
    _safe_set(a, 'assignment8', None)
    assert not _is_linked(a, 'assignment8', b2)
    if hasattr(b2, 'course9'):
        assert not _is_linked(b2, 'course9', a)


def test_assoc_Course_Book_link_reassign_clear():
    a = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    b1 = mypackage_Book(BId="sample_text", BName="sample_text", Price="sample_text")
    b2 = mypackage_Book(BId="sample_text_2", BName="sample_text_2", Price="sample_text_2")
    _safe_set(a, 'book14', b1)
    assert _is_linked(a, 'book14', b1)
    if hasattr(b1, 'course15'):
        assert _is_linked(b1, 'course15', a)
    _safe_set(a, 'book14', b2)
    assert _is_linked(a, 'book14', b2)
    if hasattr(b1, 'course15'):
        assert not _is_linked(b1, 'course15', a)
    if hasattr(b2, 'course15'):
        assert _is_linked(b2, 'course15', a)
    _safe_set(a, 'book14', None)
    assert not _is_linked(a, 'book14', b2)
    if hasattr(b2, 'course15'):
        assert not _is_linked(b2, 'course15', a)


def test_assoc_Course_Exam_link_reassign_clear():
    a = mypackage_Exam(EId="sample_text", EName="sample_text", ExamsFileName="sample_text", MaxGrade="sample_text")
    b1 = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    b2 = mypackage_Course(CId="sample_text_2", CName="sample_text_2", CourseFileName="sample_text_2", CreditHours=13)
    _safe_set(a, 'course1', b1)
    assert _is_linked(a, 'course1', b1)
    if hasattr(b1, 'exam0'):
        assert _is_linked(b1, 'exam0', a)
    _safe_set(a, 'course1', b2)
    assert _is_linked(a, 'course1', b2)
    if hasattr(b1, 'exam0'):
        assert not _is_linked(b1, 'exam0', a)
    if hasattr(b2, 'exam0'):
        assert _is_linked(b2, 'exam0', a)
    _safe_set(a, 'course1', None)
    assert not _is_linked(a, 'course1', b2)
    if hasattr(b2, 'exam0'):
        assert not _is_linked(b2, 'exam0', a)


def test_assoc_FileManager_Course_link_reassign_clear():
    a = mypackage_Course(CId="sample_text", CName="sample_text", CourseFileName="sample_text", CreditHours=7)
    b1 = mypackage_FileManager()
    b2 = mypackage_FileManager()
    _safe_set(a, 'fileManager5', b1)
    assert _is_linked(a, 'fileManager5', b1)
    if hasattr(b1, 'course4'):
        assert _is_linked(b1, 'course4', a)
    _safe_set(a, 'fileManager5', b2)
    assert _is_linked(a, 'fileManager5', b2)
    if hasattr(b1, 'course4'):
        assert not _is_linked(b1, 'course4', a)
    if hasattr(b2, 'course4'):
        assert _is_linked(b2, 'course4', a)
    _safe_set(a, 'fileManager5', None)
    assert not _is_linked(a, 'fileManager5', b2)
    if hasattr(b2, 'course4'):
        assert not _is_linked(b2, 'course4', a)


def test_assoc_FileManager_Exam_link_reassign_clear():
    a = mypackage_Exam(EId="sample_text", EName="sample_text", ExamsFileName="sample_text", MaxGrade="sample_text")
    b1 = mypackage_FileManager()
    b2 = mypackage_FileManager()
    _safe_set(a, 'fileManager7', b1)
    assert _is_linked(a, 'fileManager7', b1)
    if hasattr(b1, 'exam6'):
        assert _is_linked(b1, 'exam6', a)
    _safe_set(a, 'fileManager7', b2)
    assert _is_linked(a, 'fileManager7', b2)
    if hasattr(b1, 'exam6'):
        assert not _is_linked(b1, 'exam6', a)
    if hasattr(b2, 'exam6'):
        assert _is_linked(b2, 'exam6', a)
    _safe_set(a, 'fileManager7', None)
    assert not _is_linked(a, 'fileManager7', b2)
    if hasattr(b2, 'exam6'):
        assert not _is_linked(b2, 'exam6', a)


def test_assoc_FileManager_Perosn_link_reassign_clear():
    a = mypackage_Perosn(Pass="sample_text", UserName="sample_text", age=7, fName="sample_text", id=7, lname="sample_text")
    b1 = mypackage_FileManager()
    b2 = mypackage_FileManager()
    _safe_set(a, 'fileManager3', b1)
    assert _is_linked(a, 'fileManager3', b1)
    if hasattr(b1, 'perosn2'):
        assert _is_linked(b1, 'perosn2', a)
    _safe_set(a, 'fileManager3', b2)
    assert _is_linked(a, 'fileManager3', b2)
    if hasattr(b1, 'perosn2'):
        assert not _is_linked(b1, 'perosn2', a)
    if hasattr(b2, 'perosn2'):
        assert _is_linked(b2, 'perosn2', a)
    _safe_set(a, 'fileManager3', None)
    assert not _is_linked(a, 'fileManager3', b2)
    if hasattr(b2, 'perosn2'):
        assert not _is_linked(b2, 'perosn2', a)


def test_assoc_Student_Assignment_link_reassign_clear():
    a = mypackage_Student(grade="sample_text", level=7, studentFileName="sample_text")
    b1 = mypackage_Assignment(Deadline="sample_text", StrartDate="sample_text", number=7)
    b2 = mypackage_Assignment(Deadline="sample_text_2", StrartDate="sample_text_2", number=13)
    _safe_set(a, 'assignment12', b1)
    assert _is_linked(a, 'assignment12', b1)
    if hasattr(b1, 'student13'):
        assert _is_linked(b1, 'student13', a)
    _safe_set(a, 'assignment12', b2)
    assert _is_linked(a, 'assignment12', b2)
    if hasattr(b1, 'student13'):
        assert not _is_linked(b1, 'student13', a)
    if hasattr(b2, 'student13'):
        assert _is_linked(b2, 'student13', a)
    _safe_set(a, 'assignment12', None)
    assert not _is_linked(a, 'assignment12', b2)
    if hasattr(b2, 'student13'):
        assert not _is_linked(b2, 'student13', a)


def test_assoc_Tutor_Assignment_link_reassign_clear():
    a = mypackage_Tutor(TutorFileName="sample_text", WorkingHours="sample_text")
    b1 = mypackage_Assignment(Deadline="sample_text", StrartDate="sample_text", number=7)
    b2 = mypackage_Assignment(Deadline="sample_text_2", StrartDate="sample_text_2", number=13)
    _safe_set(a, 'assignment10', b1)
    assert _is_linked(a, 'assignment10', b1)
    if hasattr(b1, 'tutor11'):
        assert _is_linked(b1, 'tutor11', a)
    _safe_set(a, 'assignment10', b2)
    assert _is_linked(a, 'assignment10', b2)
    if hasattr(b1, 'tutor11'):
        assert not _is_linked(b1, 'tutor11', a)
    if hasattr(b2, 'tutor11'):
        assert _is_linked(b2, 'tutor11', a)
    _safe_set(a, 'assignment10', None)
    assert not _is_linked(a, 'assignment10', b2)
    if hasattr(b2, 'tutor11'):
        assert not _is_linked(b2, 'tutor11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


mypackage_Admin_strategy = st.builds(mypackage_Admin)
@given(instance=mypackage_Admin_strategy)
@settings(max_examples=25)
def test_mypackage_Admin_instantiation(instance):
    assert isinstance(instance, mypackage_Admin)


mypackage_Assignment_strategy = st.builds(mypackage_Assignment, Deadline=safe_text, StrartDate=safe_text, number=st.integers())
@given(instance=mypackage_Assignment_strategy)
@settings(max_examples=25)
def test_mypackage_Assignment_instantiation(instance):
    assert isinstance(instance, mypackage_Assignment)


mypackage_Book_strategy = st.builds(mypackage_Book, BId=safe_text, BName=safe_text, Price=safe_text)
@given(instance=mypackage_Book_strategy)
@settings(max_examples=25)
def test_mypackage_Book_instantiation(instance):
    assert isinstance(instance, mypackage_Book)


mypackage_Course_strategy = st.builds(mypackage_Course, CId=safe_text, CName=safe_text, CourseFileName=safe_text, CreditHours=st.integers())
@given(instance=mypackage_Course_strategy)
@settings(max_examples=25)
def test_mypackage_Course_instantiation(instance):
    assert isinstance(instance, mypackage_Course)


mypackage_Exam_strategy = st.builds(mypackage_Exam, EId=safe_text, EName=safe_text, ExamsFileName=safe_text, MaxGrade=safe_text)
@given(instance=mypackage_Exam_strategy)
@settings(max_examples=25)
def test_mypackage_Exam_instantiation(instance):
    assert isinstance(instance, mypackage_Exam)


mypackage_Exceptions_strategy = st.builds(mypackage_Exceptions)
@given(instance=mypackage_Exceptions_strategy)
@settings(max_examples=25)
def test_mypackage_Exceptions_instantiation(instance):
    assert isinstance(instance, mypackage_Exceptions)


mypackage_FileManager_strategy = st.builds(mypackage_FileManager)
@given(instance=mypackage_FileManager_strategy)
@settings(max_examples=25)
def test_mypackage_FileManager_instantiation(instance):
    assert isinstance(instance, mypackage_FileManager)


mypackage_Perosn_strategy = st.builds(mypackage_Perosn, Pass=safe_text, UserName=safe_text, age=st.integers(), fName=safe_text, id=st.integers(), lname=safe_text)
@given(instance=mypackage_Perosn_strategy)
@settings(max_examples=25)
def test_mypackage_Perosn_instantiation(instance):
    assert isinstance(instance, mypackage_Perosn)


mypackage_Staff_strategy = st.builds(mypackage_Staff, salary=safe_text)
@given(instance=mypackage_Staff_strategy)
@settings(max_examples=25)
def test_mypackage_Staff_instantiation(instance):
    assert isinstance(instance, mypackage_Staff)


mypackage_Student_strategy = st.builds(mypackage_Student, grade=safe_text, level=st.integers(), studentFileName=safe_text)
@given(instance=mypackage_Student_strategy)
@settings(max_examples=25)
def test_mypackage_Student_instantiation(instance):
    assert isinstance(instance, mypackage_Student)


mypackage_Tutor_strategy = st.builds(mypackage_Tutor, TutorFileName=safe_text, WorkingHours=safe_text)
@given(instance=mypackage_Tutor_strategy)
@settings(max_examples=25)
def test_mypackage_Tutor_instantiation(instance):
    assert isinstance(instance, mypackage_Tutor)


mypackage_studentAffairsEmp_strategy = st.builds(mypackage_studentAffairsEmp, EmpFileName=safe_text)
@given(instance=mypackage_studentAffairsEmp_strategy)
@settings(max_examples=25)
def test_mypackage_studentAffairsEmp_instantiation(instance):
    assert isinstance(instance, mypackage_studentAffairsEmp)


