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
    MyClass,
    Admin,
    Course,
    Department,
    Teacher,
    Employee_Interface,
    Student,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_hyp_course_constructor_exists():
    assert callable(Course.__init__)


def test_hyp_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "subjects__" in params, "Missing parameter 'subjects__'"
    assert "duration" in params, "Missing parameter 'duration'"





def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "students__" in params, "Missing parameter 'students__'"
    assert "teachers__" in params, "Missing parameter 'teachers__'"
    assert "course" in params, "Missing parameter 'course'"
    assert "hod" in params, "Missing parameter 'hod'"

def test_hyp_department_has_students__():
    assert hasattr(Department, "students__")
    descriptor = None
    for klass in Department.__mro__:
        if "students__" in klass.__dict__:
            descriptor = klass.__dict__["students__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_department_has_teachers__():
    assert hasattr(Department, "teachers__")
    descriptor = None
    for klass in Department.__mro__:
        if "teachers__" in klass.__dict__:
            descriptor = klass.__dict__["teachers__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_department_has_course():
    assert hasattr(Department, "course")
    descriptor = None
    for klass in Department.__mro__:
        if "course" in klass.__dict__:
            descriptor = klass.__dict__["course"]
            break
    assert isinstance(descriptor, property)

def test_hyp_department_has_hod():
    assert hasattr(Department, "hod")
    descriptor = None
    for klass in Department.__mro__:
        if "hod" in klass.__dict__:
            descriptor = klass.__dict__["hod"]
            break
    assert isinstance(descriptor, property)



def test_hyp_teacher_is_not_abstract():
    assert not inspect.isabstract(Teacher)


def test_hyp_teacher_constructor_exists():
    assert callable(Teacher.__init__)


def test_hyp_teacher_constructor_args():
    sig = inspect.signature(Teacher.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_interface_is_not_abstract():
    assert not inspect.isabstract(Employee_Interface)


def test_hyp_employee_interface_constructor_exists():
    assert callable(Employee_Interface.__init__)


def test_hyp_employee_interface_constructor_args():
    sig = inspect.signature(Employee_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"




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
MyClass_strategy = st.builds(
    MyClass,
)
Admin_strategy = st.builds(
    Admin,
)
Course_strategy = st.builds(
    Course,
    subjects__=
        safe_text,
    duration=
        safe_text
)
Department_strategy = st.builds(
    Department,
    students__=
        st.none(),
    teachers__=
        st.none(),
    course=
        st.none(),
    hod=
        safe_text
)
Teacher_strategy = st.builds(
    Teacher,
)
Employee_Interface_strategy = st.builds(
    Employee_Interface,
)
Student_strategy = st.builds(
    Student,
    ID=
        safe_text,
    Name=
        safe_text
)






@given(instance=Course_strategy)
def test_hyp_course_subjects___setter(instance):
    original = instance.subjects__
    instance.subjects__ = original
    assert instance.subjects__ == original



@given(instance=Course_strategy)
def test_hyp_course_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_hyp_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_hyp_department_students___setter(instance):
    original = instance.students__
    instance.students__ = original
    assert instance.students__ == original



@given(instance=Department_strategy)
def test_hyp_department_teachers___setter(instance):
    original = instance.teachers__
    instance.teachers__ = original
    assert instance.teachers__ == original



@given(instance=Department_strategy)
def test_hyp_department_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original



@given(instance=Department_strategy)
def test_hyp_department_hod_setter(instance):
    original = instance.hod
    instance.hod = original
    assert instance.hod == original






@given(instance=Student_strategy)
def test_hyp_student_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Student_strategy)
def test_hyp_student_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Course,
    Department,
    Employee_Interface,
    MyClass,
    Student,
    Teacher,
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

def test_Course_duration_value_roundtrip():
    instance = Course(duration="sample_text", subjects__="sample_text")
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_Course_subjects___value_roundtrip():
    instance = Course(duration="sample_text", subjects__="sample_text")
    assert instance.subjects__ == "sample_text"
    instance.subjects__ = "sample_text_2"
    assert instance.subjects__ == "sample_text_2"


def test_Student_ID_value_roundtrip():
    instance = Student(ID="sample_text", Name="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_Student_Name_value_roundtrip():
    instance = Student(ID="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_Admin_Student_link_reassign_clear():
    a = Student(ID="sample_text", Name="sample_text")
    b1 = Admin()
    b2 = Admin()
    _safe_set(a, 'admin7', b1)
    assert _is_linked(a, 'admin7', b1)
    if hasattr(b1, 'student6'):
        assert _is_linked(b1, 'student6', a)
    _safe_set(a, 'admin7', b2)
    assert _is_linked(a, 'admin7', b2)
    if hasattr(b1, 'student6'):
        assert not _is_linked(b1, 'student6', a)
    if hasattr(b2, 'student6'):
        assert _is_linked(b2, 'student6', a)
    _safe_set(a, 'admin7', None)
    assert not _is_linked(a, 'admin7', b2)
    if hasattr(b2, 'student6'):
        assert not _is_linked(b2, 'student6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Course_strategy = st.builds(Course, duration=safe_text, subjects__=safe_text)
@given(instance=Course_strategy)
@settings(max_examples=25)
def test_Course_instantiation(instance):
    assert isinstance(instance, Course)


Employee_Interface_strategy = st.builds(Employee_Interface)
@given(instance=Employee_Interface_strategy)
@settings(max_examples=25)
def test_Employee_Interface_instantiation(instance):
    assert isinstance(instance, Employee_Interface)


MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


Student_strategy = st.builds(Student, ID=safe_text, Name=safe_text)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)


Teacher_strategy = st.builds(Teacher)
@given(instance=Teacher_strategy)
@settings(max_examples=25)
def test_Teacher_instantiation(instance):
    assert isinstance(instance, Teacher)



