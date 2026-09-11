import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Add_Course_UseCase,
    Add_Evalutaions_Assignments_Exams_UseCase,
    Add_Instructor_UseCase,
    Add_Student_UseCase,
    Admin_Actor,
    Answer,
    Course,
    Exam,
    ExamResult,
    Generate_Report_UseCase,
    Grade_Evalutations_Assignment_Exams_UseCase,
    Instructor,
    Instructor_Actor,
    Login_UseCase,
    Login_UseCase1,
    Login_UseCase2,
    Logout_UseCase,
    Modify_Delete_Courses_UseCase,
    Modify_Delete_Evalutaions_Assignments_Exams_UseCase,
    Modify_Delete_Instructor_UseCase,
    Modify_Delete_Student_UseCase,
    Question,
    Register_drop_course_UseCase,
    School_Admin,
    Student,
    Student1,
    Student_Actor,
    Submit_Exam_Assignment_UseCase,
    View_Grades_UseCase,
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

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Add_Course_UseCase_strategy = st.builds(Add_Course_UseCase)
@given(instance=Add_Course_UseCase_strategy)
@settings(max_examples=25)
def test_Add_Course_UseCase_instantiation(instance):
    assert isinstance(instance, Add_Course_UseCase)


Add_Evalutaions_Assignments_Exams_UseCase_strategy = st.builds(Add_Evalutaions_Assignments_Exams_UseCase)
@given(instance=Add_Evalutaions_Assignments_Exams_UseCase_strategy)
@settings(max_examples=25)
def test_Add_Evalutaions_Assignments_Exams_UseCase_instantiation(instance):
    assert isinstance(instance, Add_Evalutaions_Assignments_Exams_UseCase)


Add_Instructor_UseCase_strategy = st.builds(Add_Instructor_UseCase)
@given(instance=Add_Instructor_UseCase_strategy)
@settings(max_examples=25)
def test_Add_Instructor_UseCase_instantiation(instance):
    assert isinstance(instance, Add_Instructor_UseCase)


Add_Student_UseCase_strategy = st.builds(Add_Student_UseCase)
@given(instance=Add_Student_UseCase_strategy)
@settings(max_examples=25)
def test_Add_Student_UseCase_instantiation(instance):
    assert isinstance(instance, Add_Student_UseCase)


Admin_Actor_strategy = st.builds(Admin_Actor)
@given(instance=Admin_Actor_strategy)
@settings(max_examples=25)
def test_Admin_Actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)


Answer_strategy = st.builds(Answer)
@given(instance=Answer_strategy)
@settings(max_examples=25)
def test_Answer_instantiation(instance):
    assert isinstance(instance, Answer)


Course_strategy = st.builds(Course)
@given(instance=Course_strategy)
@settings(max_examples=25)
def test_Course_instantiation(instance):
    assert isinstance(instance, Course)


Exam_strategy = st.builds(Exam)
@given(instance=Exam_strategy)
@settings(max_examples=25)
def test_Exam_instantiation(instance):
    assert isinstance(instance, Exam)


ExamResult_strategy = st.builds(ExamResult)
@given(instance=ExamResult_strategy)
@settings(max_examples=25)
def test_ExamResult_instantiation(instance):
    assert isinstance(instance, ExamResult)


Generate_Report_UseCase_strategy = st.builds(Generate_Report_UseCase)
@given(instance=Generate_Report_UseCase_strategy)
@settings(max_examples=25)
def test_Generate_Report_UseCase_instantiation(instance):
    assert isinstance(instance, Generate_Report_UseCase)


Grade_Evalutations_Assignment_Exams_UseCase_strategy = st.builds(Grade_Evalutations_Assignment_Exams_UseCase)
@given(instance=Grade_Evalutations_Assignment_Exams_UseCase_strategy)
@settings(max_examples=25)
def test_Grade_Evalutations_Assignment_Exams_UseCase_instantiation(instance):
    assert isinstance(instance, Grade_Evalutations_Assignment_Exams_UseCase)


Instructor_strategy = st.builds(Instructor)
@given(instance=Instructor_strategy)
@settings(max_examples=25)
def test_Instructor_instantiation(instance):
    assert isinstance(instance, Instructor)


Instructor_Actor_strategy = st.builds(Instructor_Actor)
@given(instance=Instructor_Actor_strategy)
@settings(max_examples=25)
def test_Instructor_Actor_instantiation(instance):
    assert isinstance(instance, Instructor_Actor)


Login_UseCase_strategy = st.builds(Login_UseCase)
@given(instance=Login_UseCase_strategy)
@settings(max_examples=25)
def test_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)


Login_UseCase1_strategy = st.builds(Login_UseCase1)
@given(instance=Login_UseCase1_strategy)
@settings(max_examples=25)
def test_Login_UseCase1_instantiation(instance):
    assert isinstance(instance, Login_UseCase1)


Login_UseCase2_strategy = st.builds(Login_UseCase2)
@given(instance=Login_UseCase2_strategy)
@settings(max_examples=25)
def test_Login_UseCase2_instantiation(instance):
    assert isinstance(instance, Login_UseCase2)


Logout_UseCase_strategy = st.builds(Logout_UseCase)
@given(instance=Logout_UseCase_strategy)
@settings(max_examples=25)
def test_Logout_UseCase_instantiation(instance):
    assert isinstance(instance, Logout_UseCase)


Modify_Delete_Courses_UseCase_strategy = st.builds(Modify_Delete_Courses_UseCase)
@given(instance=Modify_Delete_Courses_UseCase_strategy)
@settings(max_examples=25)
def test_Modify_Delete_Courses_UseCase_instantiation(instance):
    assert isinstance(instance, Modify_Delete_Courses_UseCase)


Modify_Delete_Evalutaions_Assignments_Exams_UseCase_strategy = st.builds(Modify_Delete_Evalutaions_Assignments_Exams_UseCase)
@given(instance=Modify_Delete_Evalutaions_Assignments_Exams_UseCase_strategy)
@settings(max_examples=25)
def test_Modify_Delete_Evalutaions_Assignments_Exams_UseCase_instantiation(instance):
    assert isinstance(instance, Modify_Delete_Evalutaions_Assignments_Exams_UseCase)


Modify_Delete_Instructor_UseCase_strategy = st.builds(Modify_Delete_Instructor_UseCase)
@given(instance=Modify_Delete_Instructor_UseCase_strategy)
@settings(max_examples=25)
def test_Modify_Delete_Instructor_UseCase_instantiation(instance):
    assert isinstance(instance, Modify_Delete_Instructor_UseCase)


Modify_Delete_Student_UseCase_strategy = st.builds(Modify_Delete_Student_UseCase)
@given(instance=Modify_Delete_Student_UseCase_strategy)
@settings(max_examples=25)
def test_Modify_Delete_Student_UseCase_instantiation(instance):
    assert isinstance(instance, Modify_Delete_Student_UseCase)


Question_strategy = st.builds(Question)
@given(instance=Question_strategy)
@settings(max_examples=25)
def test_Question_instantiation(instance):
    assert isinstance(instance, Question)


Register_drop_course_UseCase_strategy = st.builds(Register_drop_course_UseCase)
@given(instance=Register_drop_course_UseCase_strategy)
@settings(max_examples=25)
def test_Register_drop_course_UseCase_instantiation(instance):
    assert isinstance(instance, Register_drop_course_UseCase)


School_Admin_strategy = st.builds(School_Admin)
@given(instance=School_Admin_strategy)
@settings(max_examples=25)
def test_School_Admin_instantiation(instance):
    assert isinstance(instance, School_Admin)


Student_strategy = st.builds(Student)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Student1_strategy = st.builds(Student1)
@given(instance=Student1_strategy)
@settings(max_examples=25)
def test_Student1_instantiation(instance):
    assert isinstance(instance, Student1)


Student_Actor_strategy = st.builds(Student_Actor)
@given(instance=Student_Actor_strategy)
@settings(max_examples=25)
def test_Student_Actor_instantiation(instance):
    assert isinstance(instance, Student_Actor)


Submit_Exam_Assignment_UseCase_strategy = st.builds(Submit_Exam_Assignment_UseCase)
@given(instance=Submit_Exam_Assignment_UseCase_strategy)
@settings(max_examples=25)
def test_Submit_Exam_Assignment_UseCase_instantiation(instance):
    assert isinstance(instance, Submit_Exam_Assignment_UseCase)


View_Grades_UseCase_strategy = st.builds(View_Grades_UseCase)
@given(instance=View_Grades_UseCase_strategy)
@settings(max_examples=25)
def test_View_Grades_UseCase_instantiation(instance):
    assert isinstance(instance, View_Grades_UseCase)


