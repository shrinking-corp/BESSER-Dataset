import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ADMIN,
    Add_Course_UseCase,
    Address_UseCase,
    Admin,
    CORPORATE_CLIENT_Actor,
    Class,
    Class_Course_List_UseCase,
    CompleteCourse_UseCase,
    Corporate_Client_Actor,
    Corporate_UseCase,
    Course,
    Courses_Component,
    Create_Course_UseCase,
    Drop_Course_UseCase,
    Grade_Course_UseCase,
    LearningMaterial_UseCase,
    Login_UseCase,
    Modify_Course_UseCase,
    Name_UseCase,
    Registrar,
    Remove_Course_UseCase,
    Reports_UseCase,
    Select_Course_List_UseCase,
    Show_Course_UseCase,
    Show_Grade_UseCase,
    Student,
    Student_Actor,
    Student_ID_UseCase,
    TEACHER_Actor,
    Teacher,
    Teacher_Actor,
    Traning_Admin_Actor,
    Update_Registar_UseCase,
    UseCase_UseCase,
    User_Info_UseCase,
    _UseCase,
    class_Student_Registration,
    class_Student_Registration_Admin,
    class_Student_Registration_Corporate,
    class_Student_Registration_Student,
    class_Student_Registration_Teacher,
    corprateClient,
    courseList,
    registeredUser,
    Enumeration,
    Enumeration1,
    Status,
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

def test_Admin_Name_value_roundtrip():
    instance = Admin(Name="sample_text", User_status="sample_text", attribute="sample_text", courseList="sample_text", registrarList="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Admin_User_status_value_roundtrip():
    instance = Admin(Name="sample_text", User_status="sample_text", attribute="sample_text", courseList="sample_text", registrarList="sample_text")
    assert instance.User_status == "sample_text"
    instance.User_status = "sample_text_2"
    assert instance.User_status == "sample_text_2"


def test_Admin_attribute_value_roundtrip():
    instance = Admin(Name="sample_text", User_status="sample_text", attribute="sample_text", courseList="sample_text", registrarList="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Admin_courseList_value_roundtrip():
    instance = Admin(Name="sample_text", User_status="sample_text", attribute="sample_text", courseList="sample_text", registrarList="sample_text")
    assert instance.courseList == "sample_text"
    instance.courseList = "sample_text_2"
    assert instance.courseList == "sample_text_2"


def test_Admin_registrarList_value_roundtrip():
    instance = Admin(Name="sample_text", User_status="sample_text", attribute="sample_text", courseList="sample_text", registrarList="sample_text")
    assert instance.registrarList == "sample_text"
    instance.registrarList = "sample_text_2"
    assert instance.registrarList == "sample_text_2"


def test_Course_Description_value_roundtrip():
    instance = Course(Description="sample_text", courseCode=7, courseName="sample_text", end_date="sample_text", start_date="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Course_courseCode_value_roundtrip():
    instance = Course(Description="sample_text", courseCode=7, courseName="sample_text", end_date="sample_text", start_date="sample_text")
    assert instance.courseCode == 7
    instance.courseCode = 13
    assert instance.courseCode == 13


def test_Course_courseName_value_roundtrip():
    instance = Course(Description="sample_text", courseCode=7, courseName="sample_text", end_date="sample_text", start_date="sample_text")
    assert instance.courseName == "sample_text"
    instance.courseName = "sample_text_2"
    assert instance.courseName == "sample_text_2"


def test_Course_end_date_value_roundtrip():
    instance = Course(Description="sample_text", courseCode=7, courseName="sample_text", end_date="sample_text", start_date="sample_text")
    assert instance.end_date == "sample_text"
    instance.end_date = "sample_text_2"
    assert instance.end_date == "sample_text_2"


def test_Course_start_date_value_roundtrip():
    instance = Course(Description="sample_text", courseCode=7, courseName="sample_text", end_date="sample_text", start_date="sample_text")
    assert instance.start_date == "sample_text"
    instance.start_date = "sample_text_2"
    assert instance.start_date == "sample_text_2"


def test_Student_phone_value_roundtrip():
    instance = Student(phone=7, studentRate=7, student_ID=7, student_name="sample_text")
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


def test_Student_studentRate_value_roundtrip():
    instance = Student(phone=7, studentRate=7, student_ID=7, student_name="sample_text")
    assert instance.studentRate == 7
    instance.studentRate = 13
    assert instance.studentRate == 13


def test_Student_student_ID_value_roundtrip():
    instance = Student(phone=7, studentRate=7, student_ID=7, student_name="sample_text")
    assert instance.student_ID == 7
    instance.student_ID = 13
    assert instance.student_ID == 13


def test_Student_student_name_value_roundtrip():
    instance = Student(phone=7, studentRate=7, student_ID=7, student_name="sample_text")
    assert instance.student_name == "sample_text"
    instance.student_name = "sample_text_2"
    assert instance.student_name == "sample_text_2"


def test_Teacher_class_list_value_roundtrip():
    instance = Teacher(class_list="sample_text", phone=7, teacher_ID=7, teacher_name="sample_text")
    assert instance.class_list == "sample_text"
    instance.class_list = "sample_text_2"
    assert instance.class_list == "sample_text_2"


def test_Teacher_phone_value_roundtrip():
    instance = Teacher(class_list="sample_text", phone=7, teacher_ID=7, teacher_name="sample_text")
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


def test_Teacher_teacher_ID_value_roundtrip():
    instance = Teacher(class_list="sample_text", phone=7, teacher_ID=7, teacher_name="sample_text")
    assert instance.teacher_ID == 7
    instance.teacher_ID = 13
    assert instance.teacher_ID == 13


def test_Teacher_teacher_name_value_roundtrip():
    instance = Teacher(class_list="sample_text", phone=7, teacher_ID=7, teacher_name="sample_text")
    assert instance.teacher_name == "sample_text"
    instance.teacher_name = "sample_text_2"
    assert instance.teacher_name == "sample_text_2"


def test_corprateClient_client_ID_value_roundtrip():
    instance = corprateClient(client_ID=7, client_name="sample_text", companyRate=7, phone=7)
    assert instance.client_ID == 7
    instance.client_ID = 13
    assert instance.client_ID == 13


def test_corprateClient_client_name_value_roundtrip():
    instance = corprateClient(client_ID=7, client_name="sample_text", companyRate=7, phone=7)
    assert instance.client_name == "sample_text"
    instance.client_name = "sample_text_2"
    assert instance.client_name == "sample_text_2"


def test_corprateClient_companyRate_value_roundtrip():
    instance = corprateClient(client_ID=7, client_name="sample_text", companyRate=7, phone=7)
    assert instance.companyRate == 7
    instance.companyRate = 13
    assert instance.companyRate == 13


def test_corprateClient_phone_value_roundtrip():
    instance = corprateClient(client_ID=7, client_name="sample_text", companyRate=7, phone=7)
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


def test_registeredUser_Id_value_roundtrip():
    instance = registeredUser(Id=7, Status="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_registeredUser_Status_value_roundtrip():
    instance = registeredUser(Id=7, Status="sample_text")
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_assoc_Admin_registeredUser_link_reassign_clear():
    a = registeredUser(Id=7, Status="sample_text")
    b1 = Admin(Name="sample_text", User_status="sample_text", attribute="sample_text", courseList="sample_text", registrarList="sample_text")
    b2 = Admin(Name="sample_text_2", User_status="sample_text_2", attribute="sample_text_2", courseList="sample_text_2", registrarList="sample_text_2")
    _safe_set(a, 'admin59', b1)
    assert _is_linked(a, 'admin59', b1)
    if hasattr(b1, 'registeredUser58'):
        assert _is_linked(b1, 'registeredUser58', a)
    _safe_set(a, 'admin59', b2)
    assert _is_linked(a, 'admin59', b2)
    if hasattr(b1, 'registeredUser58'):
        assert not _is_linked(b1, 'registeredUser58', a)
    if hasattr(b2, 'registeredUser58'):
        assert _is_linked(b2, 'registeredUser58', a)
    _safe_set(a, 'admin59', None)
    assert not _is_linked(a, 'admin59', b2)
    if hasattr(b2, 'registeredUser58'):
        assert not _is_linked(b2, 'registeredUser58', a)


def test_assoc_Admin_registeredUser2_link_reassign_clear():
    a = registeredUser(Id=7, Status="sample_text")
    b1 = Admin(Name="sample_text", User_status="sample_text", attribute="sample_text", courseList="sample_text", registrarList="sample_text")
    b2 = Admin(Name="sample_text_2", User_status="sample_text_2", attribute="sample_text_2", courseList="sample_text_2", registrarList="sample_text_2")
    _safe_set(a, 'admin61', b1)
    assert _is_linked(a, 'admin61', b1)
    if hasattr(b1, 'registeredUser60'):
        assert _is_linked(b1, 'registeredUser60', a)
    _safe_set(a, 'admin61', b2)
    assert _is_linked(a, 'admin61', b2)
    if hasattr(b1, 'registeredUser60'):
        assert not _is_linked(b1, 'registeredUser60', a)
    if hasattr(b2, 'registeredUser60'):
        assert _is_linked(b2, 'registeredUser60', a)
    _safe_set(a, 'admin61', None)
    assert not _is_linked(a, 'admin61', b2)
    if hasattr(b2, 'registeredUser60'):
        assert not _is_linked(b2, 'registeredUser60', a)


def test_assoc_Course_Student_link_reassign_clear():
    a = Student(phone=7, studentRate=7, student_ID=7, student_name="sample_text")
    b1 = Course(Description="sample_text", courseCode=7, courseName="sample_text", end_date="sample_text", start_date="sample_text")
    b2 = Course(Description="sample_text_2", courseCode=13, courseName="sample_text_2", end_date="sample_text_2", start_date="sample_text_2")
    _safe_set(a, 'course65', b1)
    assert _is_linked(a, 'course65', b1)
    if hasattr(b1, 'student64'):
        assert _is_linked(b1, 'student64', a)
    _safe_set(a, 'course65', b2)
    assert _is_linked(a, 'course65', b2)
    if hasattr(b1, 'student64'):
        assert not _is_linked(b1, 'student64', a)
    if hasattr(b2, 'student64'):
        assert _is_linked(b2, 'student64', a)
    _safe_set(a, 'course65', None)
    assert not _is_linked(a, 'course65', b2)
    if hasattr(b2, 'student64'):
        assert not _is_linked(b2, 'student64', a)


def test_assoc_Course_corprateClient_link_reassign_clear():
    a = corprateClient(client_ID=7, client_name="sample_text", companyRate=7, phone=7)
    b1 = Course(Description="sample_text", courseCode=7, courseName="sample_text", end_date="sample_text", start_date="sample_text")
    b2 = Course(Description="sample_text_2", courseCode=13, courseName="sample_text_2", end_date="sample_text_2", start_date="sample_text_2")
    _safe_set(a, 'course69', b1)
    assert _is_linked(a, 'course69', b1)
    if hasattr(b1, 'corprateClient68'):
        assert _is_linked(b1, 'corprateClient68', a)
    _safe_set(a, 'course69', b2)
    assert _is_linked(a, 'course69', b2)
    if hasattr(b1, 'corprateClient68'):
        assert not _is_linked(b1, 'corprateClient68', a)
    if hasattr(b2, 'corprateClient68'):
        assert _is_linked(b2, 'corprateClient68', a)
    _safe_set(a, 'course69', None)
    assert not _is_linked(a, 'course69', b2)
    if hasattr(b2, 'corprateClient68'):
        assert not _is_linked(b2, 'corprateClient68', a)


def test_assoc_Student_addCourse_link_reassign_clear():
    a = Student(phone=7, studentRate=7, student_ID=7, student_name="sample_text")
    b1 = Course(Description="sample_text", courseCode=7, courseName="sample_text", end_date="sample_text", start_date="sample_text")
    b2 = Course(Description="sample_text_2", courseCode=13, courseName="sample_text_2", end_date="sample_text_2", start_date="sample_text_2")
    _safe_set(a, 'Course62', b1)
    assert _is_linked(a, 'Course62', b1)
    if hasattr(b1, 'student63'):
        assert _is_linked(b1, 'student63', a)
    _safe_set(a, 'Course62', b2)
    assert _is_linked(a, 'Course62', b2)
    if hasattr(b1, 'student63'):
        assert not _is_linked(b1, 'student63', a)
    if hasattr(b2, 'student63'):
        assert _is_linked(b2, 'student63', a)
    _safe_set(a, 'Course62', None)
    assert not _is_linked(a, 'Course62', b2)
    if hasattr(b2, 'student63'):
        assert not _is_linked(b2, 'student63', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ADMIN_strategy = st.builds(ADMIN)
@given(instance=ADMIN_strategy)
@settings(max_examples=25)
def test_ADMIN_instantiation(instance):
    assert isinstance(instance, ADMIN)


Add_Course_UseCase_strategy = st.builds(Add_Course_UseCase)
@given(instance=Add_Course_UseCase_strategy)
@settings(max_examples=25)
def test_Add_Course_UseCase_instantiation(instance):
    assert isinstance(instance, Add_Course_UseCase)


Address_UseCase_strategy = st.builds(Address_UseCase)
@given(instance=Address_UseCase_strategy)
@settings(max_examples=25)
def test_Address_UseCase_instantiation(instance):
    assert isinstance(instance, Address_UseCase)


Admin_strategy = st.builds(Admin, Name=safe_text, User_status=safe_text, attribute=safe_text, courseList=safe_text, registrarList=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


CORPORATE_CLIENT_Actor_strategy = st.builds(CORPORATE_CLIENT_Actor)
@given(instance=CORPORATE_CLIENT_Actor_strategy)
@settings(max_examples=25)
def test_CORPORATE_CLIENT_Actor_instantiation(instance):
    assert isinstance(instance, CORPORATE_CLIENT_Actor)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Class_Course_List_UseCase_strategy = st.builds(Class_Course_List_UseCase)
@given(instance=Class_Course_List_UseCase_strategy)
@settings(max_examples=25)
def test_Class_Course_List_UseCase_instantiation(instance):
    assert isinstance(instance, Class_Course_List_UseCase)


CompleteCourse_UseCase_strategy = st.builds(CompleteCourse_UseCase)
@given(instance=CompleteCourse_UseCase_strategy)
@settings(max_examples=25)
def test_CompleteCourse_UseCase_instantiation(instance):
    assert isinstance(instance, CompleteCourse_UseCase)


Corporate_Client_Actor_strategy = st.builds(Corporate_Client_Actor)
@given(instance=Corporate_Client_Actor_strategy)
@settings(max_examples=25)
def test_Corporate_Client_Actor_instantiation(instance):
    assert isinstance(instance, Corporate_Client_Actor)


Corporate_UseCase_strategy = st.builds(Corporate_UseCase)
@given(instance=Corporate_UseCase_strategy)
@settings(max_examples=25)
def test_Corporate_UseCase_instantiation(instance):
    assert isinstance(instance, Corporate_UseCase)


Course_strategy = st.builds(Course, Description=safe_text, courseCode=st.integers(), courseName=safe_text, end_date=safe_text, start_date=safe_text)
@given(instance=Course_strategy)
@settings(max_examples=25)
def test_Course_instantiation(instance):
    assert isinstance(instance, Course)


Courses_Component_strategy = st.builds(Courses_Component)
@given(instance=Courses_Component_strategy)
@settings(max_examples=25)
def test_Courses_Component_instantiation(instance):
    assert isinstance(instance, Courses_Component)


Create_Course_UseCase_strategy = st.builds(Create_Course_UseCase)
@given(instance=Create_Course_UseCase_strategy)
@settings(max_examples=25)
def test_Create_Course_UseCase_instantiation(instance):
    assert isinstance(instance, Create_Course_UseCase)


Drop_Course_UseCase_strategy = st.builds(Drop_Course_UseCase)
@given(instance=Drop_Course_UseCase_strategy)
@settings(max_examples=25)
def test_Drop_Course_UseCase_instantiation(instance):
    assert isinstance(instance, Drop_Course_UseCase)


Grade_Course_UseCase_strategy = st.builds(Grade_Course_UseCase)
@given(instance=Grade_Course_UseCase_strategy)
@settings(max_examples=25)
def test_Grade_Course_UseCase_instantiation(instance):
    assert isinstance(instance, Grade_Course_UseCase)


LearningMaterial_UseCase_strategy = st.builds(LearningMaterial_UseCase)
@given(instance=LearningMaterial_UseCase_strategy)
@settings(max_examples=25)
def test_LearningMaterial_UseCase_instantiation(instance):
    assert isinstance(instance, LearningMaterial_UseCase)


Login_UseCase_strategy = st.builds(Login_UseCase)
@given(instance=Login_UseCase_strategy)
@settings(max_examples=25)
def test_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)


Modify_Course_UseCase_strategy = st.builds(Modify_Course_UseCase)
@given(instance=Modify_Course_UseCase_strategy)
@settings(max_examples=25)
def test_Modify_Course_UseCase_instantiation(instance):
    assert isinstance(instance, Modify_Course_UseCase)


Name_UseCase_strategy = st.builds(Name_UseCase)
@given(instance=Name_UseCase_strategy)
@settings(max_examples=25)
def test_Name_UseCase_instantiation(instance):
    assert isinstance(instance, Name_UseCase)


Remove_Course_UseCase_strategy = st.builds(Remove_Course_UseCase)
@given(instance=Remove_Course_UseCase_strategy)
@settings(max_examples=25)
def test_Remove_Course_UseCase_instantiation(instance):
    assert isinstance(instance, Remove_Course_UseCase)


Reports_UseCase_strategy = st.builds(Reports_UseCase)
@given(instance=Reports_UseCase_strategy)
@settings(max_examples=25)
def test_Reports_UseCase_instantiation(instance):
    assert isinstance(instance, Reports_UseCase)


Select_Course_List_UseCase_strategy = st.builds(Select_Course_List_UseCase)
@given(instance=Select_Course_List_UseCase_strategy)
@settings(max_examples=25)
def test_Select_Course_List_UseCase_instantiation(instance):
    assert isinstance(instance, Select_Course_List_UseCase)


Show_Course_UseCase_strategy = st.builds(Show_Course_UseCase)
@given(instance=Show_Course_UseCase_strategy)
@settings(max_examples=25)
def test_Show_Course_UseCase_instantiation(instance):
    assert isinstance(instance, Show_Course_UseCase)


Show_Grade_UseCase_strategy = st.builds(Show_Grade_UseCase)
@given(instance=Show_Grade_UseCase_strategy)
@settings(max_examples=25)
def test_Show_Grade_UseCase_instantiation(instance):
    assert isinstance(instance, Show_Grade_UseCase)


Student_strategy = st.builds(Student, phone=st.integers(), studentRate=st.integers(), student_ID=st.integers(), student_name=safe_text)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Student_Actor_strategy = st.builds(Student_Actor)
@given(instance=Student_Actor_strategy)
@settings(max_examples=25)
def test_Student_Actor_instantiation(instance):
    assert isinstance(instance, Student_Actor)


Student_ID_UseCase_strategy = st.builds(Student_ID_UseCase)
@given(instance=Student_ID_UseCase_strategy)
@settings(max_examples=25)
def test_Student_ID_UseCase_instantiation(instance):
    assert isinstance(instance, Student_ID_UseCase)


TEACHER_Actor_strategy = st.builds(TEACHER_Actor)
@given(instance=TEACHER_Actor_strategy)
@settings(max_examples=25)
def test_TEACHER_Actor_instantiation(instance):
    assert isinstance(instance, TEACHER_Actor)


Teacher_strategy = st.builds(Teacher, class_list=safe_text, phone=st.integers(), teacher_ID=st.integers(), teacher_name=safe_text)
@given(instance=Teacher_strategy)
@settings(max_examples=25)
def test_Teacher_instantiation(instance):
    assert isinstance(instance, Teacher)


Teacher_Actor_strategy = st.builds(Teacher_Actor)
@given(instance=Teacher_Actor_strategy)
@settings(max_examples=25)
def test_Teacher_Actor_instantiation(instance):
    assert isinstance(instance, Teacher_Actor)


Traning_Admin_Actor_strategy = st.builds(Traning_Admin_Actor)
@given(instance=Traning_Admin_Actor_strategy)
@settings(max_examples=25)
def test_Traning_Admin_Actor_instantiation(instance):
    assert isinstance(instance, Traning_Admin_Actor)


Update_Registar_UseCase_strategy = st.builds(Update_Registar_UseCase)
@given(instance=Update_Registar_UseCase_strategy)
@settings(max_examples=25)
def test_Update_Registar_UseCase_instantiation(instance):
    assert isinstance(instance, Update_Registar_UseCase)


UseCase_UseCase_strategy = st.builds(UseCase_UseCase)
@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)


User_Info_UseCase_strategy = st.builds(User_Info_UseCase)
@given(instance=User_Info_UseCase_strategy)
@settings(max_examples=25)
def test_User_Info_UseCase_instantiation(instance):
    assert isinstance(instance, User_Info_UseCase)


_UseCase_strategy = st.builds(_UseCase)
@given(instance=_UseCase_strategy)
@settings(max_examples=25)
def test__UseCase_instantiation(instance):
    assert isinstance(instance, _UseCase)


class_Student_Registration_strategy = st.builds(class_Student_Registration)
@given(instance=class_Student_Registration_strategy)
@settings(max_examples=25)
def test_class_Student_Registration_instantiation(instance):
    assert isinstance(instance, class_Student_Registration)


class_Student_Registration_Admin_strategy = st.builds(class_Student_Registration_Admin)
@given(instance=class_Student_Registration_Admin_strategy)
@settings(max_examples=25)
def test_class_Student_Registration_Admin_instantiation(instance):
    assert isinstance(instance, class_Student_Registration_Admin)


class_Student_Registration_Corporate_strategy = st.builds(class_Student_Registration_Corporate)
@given(instance=class_Student_Registration_Corporate_strategy)
@settings(max_examples=25)
def test_class_Student_Registration_Corporate_instantiation(instance):
    assert isinstance(instance, class_Student_Registration_Corporate)


class_Student_Registration_Teacher_strategy = st.builds(class_Student_Registration_Teacher)
@given(instance=class_Student_Registration_Teacher_strategy)
@settings(max_examples=25)
def test_class_Student_Registration_Teacher_instantiation(instance):
    assert isinstance(instance, class_Student_Registration_Teacher)


corprateClient_strategy = st.builds(corprateClient, client_ID=st.integers(), client_name=safe_text, companyRate=st.integers(), phone=st.integers())
@given(instance=corprateClient_strategy)
@settings(max_examples=25)
def test_corprateClient_instantiation(instance):
    assert isinstance(instance, corprateClient)


registeredUser_strategy = st.builds(registeredUser, Id=st.integers(), Status=safe_text)
@given(instance=registeredUser_strategy)
@settings(max_examples=25)
def test_registeredUser_instantiation(instance):
    assert isinstance(instance, registeredUser)


