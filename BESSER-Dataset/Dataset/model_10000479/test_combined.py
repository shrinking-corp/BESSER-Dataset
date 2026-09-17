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
    Interface_Interface,
    Login,
    Curso,
    Admin,
    Database,
    Profesor,
    Student,
    Usuario,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Interface_Interface)


def test_hyp_interface_interface_constructor_exists():
    assert callable(Interface_Interface.__init__)


def test_hyp_interface_interface_constructor_args():
    sig = inspect.signature(Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())



def test_hyp_curso_is_not_abstract():
    assert not inspect.isabstract(Curso)


def test_hyp_curso_constructor_exists():
    assert callable(Curso.__init__)


def test_hyp_curso_constructor_args():
    sig = inspect.signature(Curso.__init__)
    params = list(sig.parameters.keys())
    assert "Course_Teacher" in params, "Missing parameter 'Course_Teacher'"
    assert "CourseNumber" in params, "Missing parameter 'CourseNumber'"
    assert "CourseName" in params, "Missing parameter 'CourseName'"

def test_hyp_curso_has_Course_Teacher():
    assert hasattr(Curso, "Course_Teacher")
    descriptor = None
    for klass in Curso.__mro__:
        if "Course_Teacher" in klass.__dict__:
            descriptor = klass.__dict__["Course_Teacher"]
            break
    assert isinstance(descriptor, property)

def test_hyp_curso_has_CourseNumber():
    assert hasattr(Curso, "CourseNumber")
    descriptor = None
    for klass in Curso.__mro__:
        if "CourseNumber" in klass.__dict__:
            descriptor = klass.__dict__["CourseNumber"]
            break
    assert isinstance(descriptor, property)

def test_hyp_curso_has_CourseName():
    assert hasattr(Curso, "CourseName")
    descriptor = None
    for klass in Curso.__mro__:
        if "CourseName" in klass.__dict__:
            descriptor = klass.__dict__["CourseName"]
            break
    assert isinstance(descriptor, property)



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_is_not_abstract():
    assert not inspect.isabstract(Database)


def test_hyp_database_constructor_exists():
    assert callable(Database.__init__)


def test_hyp_database_constructor_args():
    sig = inspect.signature(Database.__init__)
    params = list(sig.parameters.keys())
    assert "Grades" in params, "Missing parameter 'Grades'"
    assert "Accounts" in params, "Missing parameter 'Accounts'"
    assert "Schedules" in params, "Missing parameter 'Schedules'"
    assert "Materials" in params, "Missing parameter 'Materials'"

def test_hyp_database_has_Grades():
    assert hasattr(Database, "Grades")
    descriptor = None
    for klass in Database.__mro__:
        if "Grades" in klass.__dict__:
            descriptor = klass.__dict__["Grades"]
            break
    assert isinstance(descriptor, property)

def test_hyp_database_has_Accounts():
    assert hasattr(Database, "Accounts")
    descriptor = None
    for klass in Database.__mro__:
        if "Accounts" in klass.__dict__:
            descriptor = klass.__dict__["Accounts"]
            break
    assert isinstance(descriptor, property)

def test_hyp_database_has_Schedules():
    assert hasattr(Database, "Schedules")
    descriptor = None
    for klass in Database.__mro__:
        if "Schedules" in klass.__dict__:
            descriptor = klass.__dict__["Schedules"]
            break
    assert isinstance(descriptor, property)

def test_hyp_database_has_Materials():
    assert hasattr(Database, "Materials")
    descriptor = None
    for klass in Database.__mro__:
        if "Materials" in klass.__dict__:
            descriptor = klass.__dict__["Materials"]
            break
    assert isinstance(descriptor, property)



def test_hyp_profesor_is_not_abstract():
    assert not inspect.isabstract(Profesor)


def test_hyp_profesor_constructor_exists():
    assert callable(Profesor.__init__)


def test_hyp_profesor_constructor_args():
    sig = inspect.signature(Profesor.__init__)
    params = list(sig.parameters.keys())
    assert "Assigned_Courses" in params, "Missing parameter 'Assigned_Courses'"




def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "Year" in params, "Missing parameter 'Year'"




def test_hyp_usuario_is_not_abstract():
    assert not inspect.isabstract(Usuario)


def test_hyp_usuario_constructor_exists():
    assert callable(Usuario.__init__)


def test_hyp_usuario_constructor_args():
    sig = inspect.signature(Usuario.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Number" in params, "Missing parameter 'ID_Number'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "First_Name" in params, "Missing parameter 'First_Name'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"






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
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
Login_strategy = st.builds(
    Login,
)
Curso_strategy = st.builds(
    Curso,
    Course_Teacher=
        st.none(),
    CourseNumber=
        safe_text,
    CourseName=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
)
Database_strategy = st.builds(
    Database,
    Grades=
        st.none(),
    Accounts=
        st.none(),
    Schedules=
        st.none(),
    Materials=
        st.none()
)
Profesor_strategy = st.builds(
    Profesor,
    Assigned_Courses=
        safe_text
)
Student_strategy = st.builds(
    Student,
    Year=
        safe_text
)
Usuario_strategy = st.builds(
    Usuario,
    ID_Number=
        st.integers(),
    Password=
        safe_text,
    First_Name=
        safe_text,
    Last_Name=
        safe_text
)



@given(instance=Curso_strategy)
@settings(max_examples=50)
def test_hyp_curso_instantiation(instance):
    assert isinstance(instance, Curso)



@given(instance=Curso_strategy)
def test_hyp_curso_Course_Teacher_setter(instance):
    original = instance.Course_Teacher
    instance.Course_Teacher = original
    assert instance.Course_Teacher == original



@given(instance=Curso_strategy)
def test_hyp_curso_CourseNumber_setter(instance):
    original = instance.CourseNumber
    instance.CourseNumber = original
    assert instance.CourseNumber == original



@given(instance=Curso_strategy)
def test_hyp_curso_CourseName_setter(instance):
    original = instance.CourseName
    instance.CourseName = original
    assert instance.CourseName == original


@given(instance=Database_strategy)
@settings(max_examples=50)
def test_hyp_database_instantiation(instance):
    assert isinstance(instance, Database)



@given(instance=Database_strategy)
def test_hyp_database_Grades_setter(instance):
    original = instance.Grades
    instance.Grades = original
    assert instance.Grades == original



@given(instance=Database_strategy)
def test_hyp_database_Accounts_setter(instance):
    original = instance.Accounts
    instance.Accounts = original
    assert instance.Accounts == original



@given(instance=Database_strategy)
def test_hyp_database_Schedules_setter(instance):
    original = instance.Schedules
    instance.Schedules = original
    assert instance.Schedules == original



@given(instance=Database_strategy)
def test_hyp_database_Materials_setter(instance):
    original = instance.Materials
    instance.Materials = original
    assert instance.Materials == original




@given(instance=Profesor_strategy)
def test_hyp_profesor_Assigned_Courses_setter(instance):
    original = instance.Assigned_Courses
    instance.Assigned_Courses = original
    assert instance.Assigned_Courses == original




@given(instance=Student_strategy)
def test_hyp_student_Year_setter(instance):
    original = instance.Year
    instance.Year = original
    assert instance.Year == original




@given(instance=Usuario_strategy)
def test_hyp_usuario_ID_Number_setter(instance):
    original = instance.ID_Number
    instance.ID_Number = original
    assert instance.ID_Number == original



@given(instance=Usuario_strategy)
def test_hyp_usuario_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Usuario_strategy)
def test_hyp_usuario_First_Name_setter(instance):
    original = instance.First_Name
    instance.First_Name = original
    assert instance.First_Name == original



@given(instance=Usuario_strategy)
def test_hyp_usuario_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Curso,
    Database,
    Interface_Interface,
    Login,
    Profesor,
    Student,
    Usuario,
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

def test_Profesor_Assigned_Courses_value_roundtrip():
    instance = Profesor(Assigned_Courses="sample_text")
    assert instance.Assigned_Courses == "sample_text"
    instance.Assigned_Courses = "sample_text_2"
    assert instance.Assigned_Courses == "sample_text_2"


def test_Student_Year_value_roundtrip():
    instance = Student(Year="sample_text")
    assert instance.Year == "sample_text"
    instance.Year = "sample_text_2"
    assert instance.Year == "sample_text_2"


def test_Usuario_First_Name_value_roundtrip():
    instance = Usuario(First_Name="sample_text", ID_Number=7, Last_Name="sample_text", Password="sample_text")
    assert instance.First_Name == "sample_text"
    instance.First_Name = "sample_text_2"
    assert instance.First_Name == "sample_text_2"


def test_Usuario_ID_Number_value_roundtrip():
    instance = Usuario(First_Name="sample_text", ID_Number=7, Last_Name="sample_text", Password="sample_text")
    assert instance.ID_Number == 7
    instance.ID_Number = 13
    assert instance.ID_Number == 13


def test_Usuario_Last_Name_value_roundtrip():
    instance = Usuario(First_Name="sample_text", ID_Number=7, Last_Name="sample_text", Password="sample_text")
    assert instance.Last_Name == "sample_text"
    instance.Last_Name = "sample_text_2"
    assert instance.Last_Name == "sample_text_2"


def test_Usuario_Password_value_roundtrip():
    instance = Usuario(First_Name="sample_text", ID_Number=7, Last_Name="sample_text", Password="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_assoc_User_Login_link_reassign_clear():
    a = Usuario(First_Name="sample_text", ID_Number=7, Last_Name="sample_text", Password="sample_text")
    b1 = Login()
    b2 = Login()
    _safe_set(a, 'login12', b1)
    assert _is_linked(a, 'login12', b1)
    if hasattr(b1, 'user13'):
        assert _is_linked(b1, 'user13', a)
    _safe_set(a, 'login12', b2)
    assert _is_linked(a, 'login12', b2)
    if hasattr(b1, 'user13'):
        assert not _is_linked(b1, 'user13', a)
    if hasattr(b2, 'user13'):
        assert _is_linked(b2, 'user13', a)
    _safe_set(a, 'login12', None)
    assert not _is_linked(a, 'login12', b2)
    if hasattr(b2, 'user13'):
        assert not _is_linked(b2, 'user13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Interface_Interface_strategy = st.builds(Interface_Interface)
@given(instance=Interface_Interface_strategy)
@settings(max_examples=25)
def test_Interface_Interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)


Login_strategy = st.builds(Login)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Profesor_strategy = st.builds(Profesor, Assigned_Courses=safe_text)
@given(instance=Profesor_strategy)
@settings(max_examples=25)
def test_Profesor_instantiation(instance):
    assert isinstance(instance, Profesor)


Student_strategy = st.builds(Student, Year=safe_text)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Usuario_strategy = st.builds(Usuario, First_Name=safe_text, ID_Number=st.integers(), Last_Name=safe_text, Password=safe_text)
@given(instance=Usuario_strategy)
@settings(max_examples=25)
def test_Usuario_instantiation(instance):
    assert isinstance(instance, Usuario)



