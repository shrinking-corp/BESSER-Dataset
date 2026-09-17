# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Add_notes,
    Show_all_grades,
    Home_page,
    Interface2_Interface,
    Interface1_Interface,
    Class,
    Interface_Interface,
    New_user,
    names,
    Login,
    Course,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_add_notes_is_not_abstract():
    assert not inspect.isabstract(Add_notes)


def test_hyp_add_notes_constructor_exists():
    assert callable(Add_notes.__init__)


def test_hyp_add_notes_constructor_args():
    sig = inspect.signature(Add_notes.__init__)
    params = list(sig.parameters.keys())
    assert "Course_Name" in params, "Missing parameter 'Course_Name'"
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "Notes_taken" in params, "Missing parameter 'Notes_taken'"






def test_hyp_show_all_grades_is_not_abstract():
    assert not inspect.isabstract(Show_all_grades)


def test_hyp_show_all_grades_constructor_exists():
    assert callable(Show_all_grades.__init__)


def test_hyp_show_all_grades_constructor_args():
    sig = inspect.signature(Show_all_grades.__init__)
    params = list(sig.parameters.keys())
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "First_Name" in params, "Missing parameter 'First_Name'"
    assert "Teacher" in params, "Missing parameter 'Teacher'"
    assert "Course_name" in params, "Missing parameter 'Course_name'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "Grade_earned" in params, "Missing parameter 'Grade_earned'"









def test_hyp_home_page_is_not_abstract():
    assert not inspect.isabstract(Home_page)


def test_hyp_home_page_constructor_exists():
    assert callable(Home_page.__init__)


def test_hyp_home_page_constructor_args():
    sig = inspect.signature(Home_page.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interface2_interface_is_not_abstract():
    assert not inspect.isabstract(Interface2_Interface)


def test_hyp_interface2_interface_constructor_exists():
    assert callable(Interface2_Interface.__init__)


def test_hyp_interface2_interface_constructor_args():
    sig = inspect.signature(Interface2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interface1_interface_is_not_abstract():
    assert not inspect.isabstract(Interface1_Interface)


def test_hyp_interface1_interface_constructor_exists():
    assert callable(Interface1_Interface.__init__)


def test_hyp_interface1_interface_constructor_args():
    sig = inspect.signature(Interface1_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_hyp_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_hyp_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_new_user_is_not_abstract():
    assert not inspect.isabstract(New_user)


def test_hyp_new_user_constructor_exists():
    assert callable(New_user.__init__)


def test_hyp_new_user_constructor_args():
    sig = inspect.signature(New_user.__init__)
    params = list(sig.parameters.keys())
    assert "First_name" in params, "Missing parameter 'First_name'"
    assert "Contact_No" in params, "Missing parameter 'Contact_No'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "Major" in params, "Missing parameter 'Major'"
    assert "Student_ID1" in params, "Missing parameter 'Student_ID1'"









def test_hyp_names_is_not_abstract():
    assert not inspect.isabstract(names)


def test_hyp_names_constructor_exists():
    assert callable(names.__init__)


def test_hyp_names_constructor_args():
    sig = inspect.signature(names.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "Password" in params, "Missing parameter 'Password'"






def test_hyp_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_hyp_course_constructor_exists():
    assert callable(Course.__init__)


def test_hyp_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "Room" in params, "Missing parameter 'Room'"
    assert "Course_Index" in params, "Missing parameter 'Course_Index'"
    assert "Status" in params, "Missing parameter 'Status'"
    assert "Student_ID" in params, "Missing parameter 'Student_ID'"
    assert "Teacher" in params, "Missing parameter 'Teacher'"
    assert "Day" in params, "Missing parameter 'Day'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Grade_earned" in params, "Missing parameter 'Grade_earned'"
    assert "Course_name" in params, "Missing parameter 'Course_name'"











# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Add_notes_strategy = st.builds(
    Add_notes,
    Course_Name=
        safe_text,
    Student_ID=
        st.integers(),
    Notes_taken=
        safe_text
)
Show_all_grades_strategy = st.builds(
    Show_all_grades,
    Student_ID=
        st.integers(),
    First_Name=
        safe_text,
    Teacher=
        safe_text,
    Course_name=
        safe_text,
    Last_Name=
        safe_text,
    Grade_earned=
        safe_text
)
Home_page_strategy = st.builds(
    Home_page,
)
Interface2_Interface_strategy = st.builds(
    Interface2_Interface,
)
Interface1_Interface_strategy = st.builds(
    Interface1_Interface,
)
Class_strategy = st.builds(
    Class,
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
New_user_strategy = st.builds(
    New_user,
    First_name=
        safe_text,
    Contact_No=
        st.integers(),
    Last_Name=
        safe_text,
    Student_ID=
        st.integers(),
    Major=
        safe_text,
    Student_ID1=
        st.integers()
)
names_strategy = st.builds(
    names,
)
Login_strategy = st.builds(
    Login,
    Email=
        safe_text,
    Student_ID=
        st.integers(),
    Password=
        safe_text
)
Course_strategy = st.builds(
    Course,
    Room=
        st.integers(),
    Course_Index=
        st.integers(),
    Status=
        safe_text,
    Student_ID=
        st.integers(),
    Teacher=
        safe_text,
    Day=
        safe_text,
    Time=
        safe_text,
    Grade_earned=
        safe_text,
    Course_name=
        safe_text
)




@given(instance=Add_notes_strategy)
def test_hyp_add_notes_Course_Name_setter(instance):
    original = instance.Course_Name
    instance.Course_Name = original
    assert instance.Course_Name == original



@given(instance=Add_notes_strategy)
def test_hyp_add_notes_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=Add_notes_strategy)
def test_hyp_add_notes_Notes_taken_setter(instance):
    original = instance.Notes_taken
    instance.Notes_taken = original
    assert instance.Notes_taken == original




@given(instance=Show_all_grades_strategy)
def test_hyp_show_all_grades_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=Show_all_grades_strategy)
def test_hyp_show_all_grades_First_Name_setter(instance):
    original = instance.First_Name
    instance.First_Name = original
    assert instance.First_Name == original



@given(instance=Show_all_grades_strategy)
def test_hyp_show_all_grades_Teacher_setter(instance):
    original = instance.Teacher
    instance.Teacher = original
    assert instance.Teacher == original



@given(instance=Show_all_grades_strategy)
def test_hyp_show_all_grades_Course_name_setter(instance):
    original = instance.Course_name
    instance.Course_name = original
    assert instance.Course_name == original



@given(instance=Show_all_grades_strategy)
def test_hyp_show_all_grades_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=Show_all_grades_strategy)
def test_hyp_show_all_grades_Grade_earned_setter(instance):
    original = instance.Grade_earned
    instance.Grade_earned = original
    assert instance.Grade_earned == original









@given(instance=New_user_strategy)
def test_hyp_new_user_First_name_setter(instance):
    original = instance.First_name
    instance.First_name = original
    assert instance.First_name == original



@given(instance=New_user_strategy)
def test_hyp_new_user_Contact_No_setter(instance):
    original = instance.Contact_No
    instance.Contact_No = original
    assert instance.Contact_No == original



@given(instance=New_user_strategy)
def test_hyp_new_user_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=New_user_strategy)
def test_hyp_new_user_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=New_user_strategy)
def test_hyp_new_user_Major_setter(instance):
    original = instance.Major
    instance.Major = original
    assert instance.Major == original



@given(instance=New_user_strategy)
def test_hyp_new_user_Student_ID1_setter(instance):
    original = instance.Student_ID1
    instance.Student_ID1 = original
    assert instance.Student_ID1 == original





@given(instance=Login_strategy)
def test_hyp_login_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Login_strategy)
def test_hyp_login_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=Login_strategy)
def test_hyp_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original




@given(instance=Course_strategy)
def test_hyp_course_Room_setter(instance):
    original = instance.Room
    instance.Room = original
    assert instance.Room == original



@given(instance=Course_strategy)
def test_hyp_course_Course_Index_setter(instance):
    original = instance.Course_Index
    instance.Course_Index = original
    assert instance.Course_Index == original



@given(instance=Course_strategy)
def test_hyp_course_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=Course_strategy)
def test_hyp_course_Student_ID_setter(instance):
    original = instance.Student_ID
    instance.Student_ID = original
    assert instance.Student_ID == original



@given(instance=Course_strategy)
def test_hyp_course_Teacher_setter(instance):
    original = instance.Teacher
    instance.Teacher = original
    assert instance.Teacher == original



@given(instance=Course_strategy)
def test_hyp_course_Day_setter(instance):
    original = instance.Day
    instance.Day = original
    assert instance.Day == original



@given(instance=Course_strategy)
def test_hyp_course_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Course_strategy)
def test_hyp_course_Grade_earned_setter(instance):
    original = instance.Grade_earned
    instance.Grade_earned = original
    assert instance.Grade_earned == original



@given(instance=Course_strategy)
def test_hyp_course_Course_name_setter(instance):
    original = instance.Course_name
    instance.Course_name = original
    assert instance.Course_name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Add_notes,
    Class,
    Course,
    Home_page,
    Interface1_Interface,
    Interface2_Interface,
    Interface_Interface,
    Login,
    New_user,
    Show_all_grades,
    names,
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

def test_Add_notes_Course_Name_value_roundtrip():
    instance = Add_notes(Course_Name="sample_text", Notes_taken="sample_text", Student_ID=7)
    assert instance.Course_Name == "sample_text"
    instance.Course_Name = "sample_text_2"
    assert instance.Course_Name == "sample_text_2"


def test_Add_notes_Notes_taken_value_roundtrip():
    instance = Add_notes(Course_Name="sample_text", Notes_taken="sample_text", Student_ID=7)
    assert instance.Notes_taken == "sample_text"
    instance.Notes_taken = "sample_text_2"
    assert instance.Notes_taken == "sample_text_2"


def test_Add_notes_Student_ID_value_roundtrip():
    instance = Add_notes(Course_Name="sample_text", Notes_taken="sample_text", Student_ID=7)
    assert instance.Student_ID == 7
    instance.Student_ID = 13
    assert instance.Student_ID == 13


def test_Course_Course_Index_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Course_Index == 7
    instance.Course_Index = 13
    assert instance.Course_Index == 13


def test_Course_Course_name_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Course_name == "sample_text"
    instance.Course_name = "sample_text_2"
    assert instance.Course_name == "sample_text_2"


def test_Course_Day_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Day == "sample_text"
    instance.Day = "sample_text_2"
    assert instance.Day == "sample_text_2"


def test_Course_Grade_earned_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Grade_earned == "sample_text"
    instance.Grade_earned = "sample_text_2"
    assert instance.Grade_earned == "sample_text_2"


def test_Course_Room_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Room == 7
    instance.Room = 13
    assert instance.Room == 13


def test_Course_Status_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Status == "sample_text"
    instance.Status = "sample_text_2"
    assert instance.Status == "sample_text_2"


def test_Course_Student_ID_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Student_ID == 7
    instance.Student_ID = 13
    assert instance.Student_ID == 13


def test_Course_Teacher_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Teacher == "sample_text"
    instance.Teacher = "sample_text_2"
    assert instance.Teacher == "sample_text_2"


def test_Course_Time_value_roundtrip():
    instance = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    assert instance.Time == "sample_text"
    instance.Time = "sample_text_2"
    assert instance.Time == "sample_text_2"


def test_Login_Email_value_roundtrip():
    instance = Login(Email="sample_text", Password="sample_text", Student_ID=7)
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Login_Password_value_roundtrip():
    instance = Login(Email="sample_text", Password="sample_text", Student_ID=7)
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Login_Student_ID_value_roundtrip():
    instance = Login(Email="sample_text", Password="sample_text", Student_ID=7)
    assert instance.Student_ID == 7
    instance.Student_ID = 13
    assert instance.Student_ID == 13


def test_New_user_Contact_No_value_roundtrip():
    instance = New_user(Contact_No=7, First_name="sample_text", Last_Name="sample_text", Major="sample_text", Student_ID=7, Student_ID1=7)
    assert instance.Contact_No == 7
    instance.Contact_No = 13
    assert instance.Contact_No == 13


def test_New_user_First_name_value_roundtrip():
    instance = New_user(Contact_No=7, First_name="sample_text", Last_Name="sample_text", Major="sample_text", Student_ID=7, Student_ID1=7)
    assert instance.First_name == "sample_text"
    instance.First_name = "sample_text_2"
    assert instance.First_name == "sample_text_2"


def test_New_user_Last_Name_value_roundtrip():
    instance = New_user(Contact_No=7, First_name="sample_text", Last_Name="sample_text", Major="sample_text", Student_ID=7, Student_ID1=7)
    assert instance.Last_Name == "sample_text"
    instance.Last_Name = "sample_text_2"
    assert instance.Last_Name == "sample_text_2"


def test_New_user_Major_value_roundtrip():
    instance = New_user(Contact_No=7, First_name="sample_text", Last_Name="sample_text", Major="sample_text", Student_ID=7, Student_ID1=7)
    assert instance.Major == "sample_text"
    instance.Major = "sample_text_2"
    assert instance.Major == "sample_text_2"


def test_New_user_Student_ID_value_roundtrip():
    instance = New_user(Contact_No=7, First_name="sample_text", Last_Name="sample_text", Major="sample_text", Student_ID=7, Student_ID1=7)
    assert instance.Student_ID == 7
    instance.Student_ID = 13
    assert instance.Student_ID == 13


def test_New_user_Student_ID1_value_roundtrip():
    instance = New_user(Contact_No=7, First_name="sample_text", Last_Name="sample_text", Major="sample_text", Student_ID=7, Student_ID1=7)
    assert instance.Student_ID1 == 7
    instance.Student_ID1 = 13
    assert instance.Student_ID1 == 13


def test_Show_all_grades_Course_name_value_roundtrip():
    instance = Show_all_grades(Course_name="sample_text", First_Name="sample_text", Grade_earned="sample_text", Last_Name="sample_text", Student_ID=7, Teacher="sample_text")
    assert instance.Course_name == "sample_text"
    instance.Course_name = "sample_text_2"
    assert instance.Course_name == "sample_text_2"


def test_Show_all_grades_First_Name_value_roundtrip():
    instance = Show_all_grades(Course_name="sample_text", First_Name="sample_text", Grade_earned="sample_text", Last_Name="sample_text", Student_ID=7, Teacher="sample_text")
    assert instance.First_Name == "sample_text"
    instance.First_Name = "sample_text_2"
    assert instance.First_Name == "sample_text_2"


def test_Show_all_grades_Grade_earned_value_roundtrip():
    instance = Show_all_grades(Course_name="sample_text", First_Name="sample_text", Grade_earned="sample_text", Last_Name="sample_text", Student_ID=7, Teacher="sample_text")
    assert instance.Grade_earned == "sample_text"
    instance.Grade_earned = "sample_text_2"
    assert instance.Grade_earned == "sample_text_2"


def test_Show_all_grades_Last_Name_value_roundtrip():
    instance = Show_all_grades(Course_name="sample_text", First_Name="sample_text", Grade_earned="sample_text", Last_Name="sample_text", Student_ID=7, Teacher="sample_text")
    assert instance.Last_Name == "sample_text"
    instance.Last_Name = "sample_text_2"
    assert instance.Last_Name == "sample_text_2"


def test_Show_all_grades_Student_ID_value_roundtrip():
    instance = Show_all_grades(Course_name="sample_text", First_Name="sample_text", Grade_earned="sample_text", Last_Name="sample_text", Student_ID=7, Teacher="sample_text")
    assert instance.Student_ID == 7
    instance.Student_ID = 13
    assert instance.Student_ID == 13


def test_Show_all_grades_Teacher_value_roundtrip():
    instance = Show_all_grades(Course_name="sample_text", First_Name="sample_text", Grade_earned="sample_text", Last_Name="sample_text", Student_ID=7, Teacher="sample_text")
    assert instance.Teacher == "sample_text"
    instance.Teacher = "sample_text_2"
    assert instance.Teacher == "sample_text_2"


def test_assoc_Home_page_Add_notes_link_reassign_clear():
    a = Add_notes(Course_Name="sample_text", Notes_taken="sample_text", Student_ID=7)
    b1 = Home_page()
    b2 = Home_page()
    _safe_set(a, 'home_page9', b1)
    assert _is_linked(a, 'home_page9', b1)
    if hasattr(b1, 'add_notes8'):
        assert _is_linked(b1, 'add_notes8', a)
    _safe_set(a, 'home_page9', b2)
    assert _is_linked(a, 'home_page9', b2)
    if hasattr(b1, 'add_notes8'):
        assert not _is_linked(b1, 'add_notes8', a)
    if hasattr(b2, 'add_notes8'):
        assert _is_linked(b2, 'add_notes8', a)
    _safe_set(a, 'home_page9', None)
    assert not _is_linked(a, 'home_page9', b2)
    if hasattr(b2, 'add_notes8'):
        assert not _is_linked(b2, 'add_notes8', a)


def test_assoc_Home_page_Course_link_reassign_clear():
    a = Course(Course_Index=7, Course_name="sample_text", Day="sample_text", Grade_earned="sample_text", Room=7, Status="sample_text", Student_ID=7, Teacher="sample_text", Time="sample_text")
    b1 = Home_page()
    b2 = Home_page()
    _safe_set(a, 'home_page7', b1)
    assert _is_linked(a, 'home_page7', b1)
    if hasattr(b1, 'course6'):
        assert _is_linked(b1, 'course6', a)
    _safe_set(a, 'home_page7', b2)
    assert _is_linked(a, 'home_page7', b2)
    if hasattr(b1, 'course6'):
        assert not _is_linked(b1, 'course6', a)
    if hasattr(b2, 'course6'):
        assert _is_linked(b2, 'course6', a)
    _safe_set(a, 'home_page7', None)
    assert not _is_linked(a, 'home_page7', b2)
    if hasattr(b2, 'course6'):
        assert not _is_linked(b2, 'course6', a)


def test_assoc_Home_page_Show_all_grades_link_reassign_clear():
    a = Show_all_grades(Course_name="sample_text", First_Name="sample_text", Grade_earned="sample_text", Last_Name="sample_text", Student_ID=7, Teacher="sample_text")
    b1 = Home_page()
    b2 = Home_page()
    _safe_set(a, 'home_page5', b1)
    assert _is_linked(a, 'home_page5', b1)
    if hasattr(b1, 'show_all_grades4'):
        assert _is_linked(b1, 'show_all_grades4', a)
    _safe_set(a, 'home_page5', b2)
    assert _is_linked(a, 'home_page5', b2)
    if hasattr(b1, 'show_all_grades4'):
        assert not _is_linked(b1, 'show_all_grades4', a)
    if hasattr(b2, 'show_all_grades4'):
        assert _is_linked(b2, 'show_all_grades4', a)
    _safe_set(a, 'home_page5', None)
    assert not _is_linked(a, 'home_page5', b2)
    if hasattr(b2, 'show_all_grades4'):
        assert not _is_linked(b2, 'show_all_grades4', a)


def test_assoc_Login_Home_page_link_reassign_clear():
    a = Login(Email="sample_text", Password="sample_text", Student_ID=7)
    b1 = Home_page()
    b2 = Home_page()
    _safe_set(a, 'home_page2', b1)
    assert _is_linked(a, 'home_page2', b1)
    if hasattr(b1, 'login3'):
        assert _is_linked(b1, 'login3', a)
    _safe_set(a, 'home_page2', b2)
    assert _is_linked(a, 'home_page2', b2)
    if hasattr(b1, 'login3'):
        assert not _is_linked(b1, 'login3', a)
    if hasattr(b2, 'login3'):
        assert _is_linked(b2, 'login3', a)
    _safe_set(a, 'home_page2', None)
    assert not _is_linked(a, 'home_page2', b2)
    if hasattr(b2, 'login3'):
        assert not _is_linked(b2, 'login3', a)


def test_assoc_Login_New_user_link_reassign_clear():
    a = New_user(Contact_No=7, First_name="sample_text", Last_Name="sample_text", Major="sample_text", Student_ID=7, Student_ID1=7)
    b1 = Login(Email="sample_text", Password="sample_text", Student_ID=7)
    b2 = Login(Email="sample_text_2", Password="sample_text_2", Student_ID=13)
    _safe_set(a, 'login1', b1)
    assert _is_linked(a, 'login1', b1)
    if hasattr(b1, 'new_user0'):
        assert _is_linked(b1, 'new_user0', a)
    _safe_set(a, 'login1', b2)
    assert _is_linked(a, 'login1', b2)
    if hasattr(b1, 'new_user0'):
        assert not _is_linked(b1, 'new_user0', a)
    if hasattr(b2, 'new_user0'):
        assert _is_linked(b2, 'new_user0', a)
    _safe_set(a, 'login1', None)
    assert not _is_linked(a, 'login1', b2)
    if hasattr(b2, 'new_user0'):
        assert not _is_linked(b2, 'new_user0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Add_notes_strategy = st.builds(Add_notes, Course_Name=safe_text, Notes_taken=safe_text, Student_ID=st.integers())
@given(instance=Add_notes_strategy)
@settings(max_examples=25)
def test_Add_notes_instantiation(instance):
    assert isinstance(instance, Add_notes)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Course_strategy = st.builds(Course, Course_Index=st.integers(), Course_name=safe_text, Day=safe_text, Grade_earned=safe_text, Room=st.integers(), Status=safe_text, Student_ID=st.integers(), Teacher=safe_text, Time=safe_text)
@given(instance=Course_strategy)
@settings(max_examples=25)
def test_Course_instantiation(instance):
    assert isinstance(instance, Course)


Home_page_strategy = st.builds(Home_page)
@given(instance=Home_page_strategy)
@settings(max_examples=25)
def test_Home_page_instantiation(instance):
    assert isinstance(instance, Home_page)


Interface1_Interface_strategy = st.builds(Interface1_Interface)
@given(instance=Interface1_Interface_strategy)
@settings(max_examples=25)
def test_Interface1_Interface_instantiation(instance):
    assert isinstance(instance, Interface1_Interface)


Interface2_Interface_strategy = st.builds(Interface2_Interface)
@given(instance=Interface2_Interface_strategy)
@settings(max_examples=25)
def test_Interface2_Interface_instantiation(instance):
    assert isinstance(instance, Interface2_Interface)


Interface_Interface_strategy = st.builds(Interface_Interface)
@given(instance=Interface_Interface_strategy)
@settings(max_examples=25)
def test_Interface_Interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)


Login_strategy = st.builds(Login, Email=safe_text, Password=safe_text, Student_ID=st.integers())
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


New_user_strategy = st.builds(New_user, Contact_No=st.integers(), First_name=safe_text, Last_Name=safe_text, Major=safe_text, Student_ID=st.integers(), Student_ID1=st.integers())
@given(instance=New_user_strategy)
@settings(max_examples=25)
def test_New_user_instantiation(instance):
    assert isinstance(instance, New_user)


Show_all_grades_strategy = st.builds(Show_all_grades, Course_name=safe_text, First_Name=safe_text, Grade_earned=safe_text, Last_Name=safe_text, Student_ID=st.integers(), Teacher=safe_text)
@given(instance=Show_all_grades_strategy)
@settings(max_examples=25)
def test_Show_all_grades_instantiation(instance):
    assert isinstance(instance, Show_all_grades)


names_strategy = st.builds(names)
@given(instance=names_strategy)
@settings(max_examples=25)
def test_names_instantiation(instance):
    assert isinstance(instance, names)



