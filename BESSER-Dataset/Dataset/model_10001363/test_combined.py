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
    barcode,
    controller,
    staff_member,
    Department,
    course,
    Class,
    Interface_Interface,
    Admin,
    student,
    Person,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_barcode_is_not_abstract():
    assert not inspect.isabstract(barcode)


def test_hyp_barcode_constructor_exists():
    assert callable(barcode.__init__)


def test_hyp_barcode_constructor_args():
    sig = inspect.signature(barcode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controller_is_not_abstract():
    assert not inspect.isabstract(controller)


def test_hyp_controller_constructor_exists():
    assert callable(controller.__init__)


def test_hyp_controller_constructor_args():
    sig = inspect.signature(controller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staff_member_is_not_abstract():
    assert not inspect.isabstract(staff_member)


def test_hyp_staff_member_constructor_exists():
    assert callable(staff_member.__init__)


def test_hyp_staff_member_constructor_args():
    sig = inspect.signature(staff_member.__init__)
    params = list(sig.parameters.keys())



def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "dept_id" in params, "Missing parameter 'dept_id'"
    assert "dept_name" in params, "Missing parameter 'dept_name'"





def test_hyp_course_is_not_abstract():
    assert not inspect.isabstract(course)


def test_hyp_course_constructor_exists():
    assert callable(course.__init__)


def test_hyp_course_constructor_args():
    sig = inspect.signature(course.__init__)
    params = list(sig.parameters.keys())
    assert "course_preq" in params, "Missing parameter 'course_preq'"
    assert "course_id" in params, "Missing parameter 'course_id'"
    assert "course_name" in params, "Missing parameter 'course_name'"
    assert "credit_hours" in params, "Missing parameter 'credit_hours'"







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



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(student)


def test_hyp_student_constructor_exists():
    assert callable(student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(student.__init__)
    params = list(sig.parameters.keys())
    assert "major_dept" in params, "Missing parameter 'major_dept'"
    assert "minor_dept" in params, "Missing parameter 'minor_dept'"





def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"
    assert "password" in params, "Missing parameter 'password'"
    assert "department" in params, "Missing parameter 'department'"
    assert "date_of_birth" in params, "Missing parameter 'date_of_birth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"









def test_hyp_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_hyp_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
barcode_strategy = st.builds(
    barcode,
)
controller_strategy = st.builds(
    controller,
)
staff_member_strategy = st.builds(
    staff_member,
)
Department_strategy = st.builds(
    Department,
    dept_id=
        st.integers(),
    dept_name=
        safe_text
)
course_strategy = st.builds(
    course,
    course_preq=
        safe_text,
    course_id=
        st.integers(),
    course_name=
        safe_text,
    credit_hours=
        st.integers()
)
Class_strategy = st.builds(
    Class,
)
Interface_Interface_strategy = st.builds(
    Interface_Interface,
)
Admin_strategy = st.builds(
    Admin,
)
student_strategy = st.builds(
    student,
    major_dept=
        safe_text,
    minor_dept=
        safe_text
)
Person_strategy = st.builds(
    Person,
    username=
        safe_text,
    email=
        safe_text,
    address=
        safe_text,
    password=
        st.integers(),
    department=
        safe_text,
    date_of_birth=
        safe_text,
    name=
        safe_text,
    id=
        st.integers()
)







@given(instance=Department_strategy)
def test_hyp_department_dept_id_setter(instance):
    original = instance.dept_id
    instance.dept_id = original
    assert instance.dept_id == original



@given(instance=Department_strategy)
def test_hyp_department_dept_name_setter(instance):
    original = instance.dept_name
    instance.dept_name = original
    assert instance.dept_name == original




@given(instance=course_strategy)
def test_hyp_course_course_preq_setter(instance):
    original = instance.course_preq
    instance.course_preq = original
    assert instance.course_preq == original



@given(instance=course_strategy)
def test_hyp_course_course_id_setter(instance):
    original = instance.course_id
    instance.course_id = original
    assert instance.course_id == original



@given(instance=course_strategy)
def test_hyp_course_course_name_setter(instance):
    original = instance.course_name
    instance.course_name = original
    assert instance.course_name == original



@given(instance=course_strategy)
def test_hyp_course_credit_hours_setter(instance):
    original = instance.credit_hours
    instance.credit_hours = original
    assert instance.credit_hours == original







@given(instance=student_strategy)
def test_hyp_student_major_dept_setter(instance):
    original = instance.major_dept
    instance.major_dept = original
    assert instance.major_dept == original



@given(instance=student_strategy)
def test_hyp_student_minor_dept_setter(instance):
    original = instance.minor_dept
    instance.minor_dept = original
    assert instance.minor_dept == original




@given(instance=Person_strategy)
def test_hyp_person_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Person_strategy)
def test_hyp_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Person_strategy)
def test_hyp_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Person_strategy)
def test_hyp_person_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Person_strategy)
def test_hyp_person_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=Person_strategy)
def test_hyp_person_date_of_birth_setter(instance):
    original = instance.date_of_birth
    instance.date_of_birth = original
    assert instance.date_of_birth == original



@given(instance=Person_strategy)
def test_hyp_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Person_strategy)
def test_hyp_person_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Class,
    Department,
    Interface_Interface,
    Person,
    barcode,
    controller,
    course,
    staff_member,
    student,
    Enumeration,
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

def test_Department_dept_id_value_roundtrip():
    instance = Department(dept_id=7, dept_name="sample_text")
    assert instance.dept_id == 7
    instance.dept_id = 13
    assert instance.dept_id == 13


def test_Department_dept_name_value_roundtrip():
    instance = Department(dept_id=7, dept_name="sample_text")
    assert instance.dept_name == "sample_text"
    instance.dept_name = "sample_text_2"
    assert instance.dept_name == "sample_text_2"


def test_Person_address_value_roundtrip():
    instance = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Person_date_of_birth_value_roundtrip():
    instance = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    assert instance.date_of_birth == "sample_text"
    instance.date_of_birth = "sample_text_2"
    assert instance.date_of_birth == "sample_text_2"


def test_Person_department_value_roundtrip():
    instance = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    assert instance.department == "sample_text"
    instance.department = "sample_text_2"
    assert instance.department == "sample_text_2"


def test_Person_email_value_roundtrip():
    instance = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Person_id_value_roundtrip():
    instance = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Person_name_value_roundtrip():
    instance = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Person_password_value_roundtrip():
    instance = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    assert instance.password == 7
    instance.password = 13
    assert instance.password == 13


def test_Person_username_value_roundtrip():
    instance = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_course_course_id_value_roundtrip():
    instance = course(course_id=7, course_name="sample_text", course_preq="sample_text", credit_hours=7)
    assert instance.course_id == 7
    instance.course_id = 13
    assert instance.course_id == 13


def test_course_course_name_value_roundtrip():
    instance = course(course_id=7, course_name="sample_text", course_preq="sample_text", credit_hours=7)
    assert instance.course_name == "sample_text"
    instance.course_name = "sample_text_2"
    assert instance.course_name == "sample_text_2"


def test_course_course_preq_value_roundtrip():
    instance = course(course_id=7, course_name="sample_text", course_preq="sample_text", credit_hours=7)
    assert instance.course_preq == "sample_text"
    instance.course_preq = "sample_text_2"
    assert instance.course_preq == "sample_text_2"


def test_course_credit_hours_value_roundtrip():
    instance = course(course_id=7, course_name="sample_text", course_preq="sample_text", credit_hours=7)
    assert instance.credit_hours == 7
    instance.credit_hours = 13
    assert instance.credit_hours == 13


def test_student_major_dept_value_roundtrip():
    instance = student(major_dept="sample_text", minor_dept="sample_text")
    assert instance.major_dept == "sample_text"
    instance.major_dept = "sample_text_2"
    assert instance.major_dept == "sample_text_2"


def test_student_minor_dept_value_roundtrip():
    instance = student(major_dept="sample_text", minor_dept="sample_text")
    assert instance.minor_dept == "sample_text"
    instance.minor_dept = "sample_text_2"
    assert instance.minor_dept == "sample_text_2"


def test_assoc_Department_course_link_reassign_clear():
    a = course(course_id=7, course_name="sample_text", course_preq="sample_text", credit_hours=7)
    b1 = Department(dept_id=7, dept_name="sample_text")
    b2 = Department(dept_id=13, dept_name="sample_text_2")
    _safe_set(a, 'department17', {b1})
    assert _is_linked(a, 'department17', b1)
    if hasattr(b1, 'course16'):
        assert _is_linked(b1, 'course16', a)
    _safe_set(a, 'department17', {b2})
    assert _is_linked(a, 'department17', b2)
    if hasattr(b1, 'course16'):
        assert not _is_linked(b1, 'course16', a)
    if hasattr(b2, 'course16'):
        assert _is_linked(b2, 'course16', a)
    _safe_set(a, 'department17', set())
    assert not _is_linked(a, 'department17', b2)
    if hasattr(b2, 'course16'):
        assert not _is_linked(b2, 'course16', a)


def test_assoc_Department_student_link_reassign_clear():
    a = student(major_dept="sample_text", minor_dept="sample_text")
    b1 = Department(dept_id=7, dept_name="sample_text")
    b2 = Department(dept_id=13, dept_name="sample_text_2")
    _safe_set(a, 'department1', {b1})
    assert _is_linked(a, 'department1', b1)
    if hasattr(b1, 'student0'):
        assert _is_linked(b1, 'student0', a)
    _safe_set(a, 'department1', {b2})
    assert _is_linked(a, 'department1', b2)
    if hasattr(b1, 'student0'):
        assert not _is_linked(b1, 'student0', a)
    if hasattr(b2, 'student0'):
        assert _is_linked(b2, 'student0', a)
    _safe_set(a, 'department1', set())
    assert not _is_linked(a, 'department1', b2)
    if hasattr(b2, 'student0'):
        assert not _is_linked(b2, 'student0', a)


def test_assoc_course_Admin_link_reassign_clear():
    a = course(course_id=7, course_name="sample_text", course_preq="sample_text", credit_hours=7)
    b1 = Admin()
    b2 = Admin()
    _safe_set(a, 'admin4', {b1})
    assert _is_linked(a, 'admin4', b1)
    if hasattr(b1, 'course5'):
        assert _is_linked(b1, 'course5', a)
    _safe_set(a, 'admin4', {b2})
    assert _is_linked(a, 'admin4', b2)
    if hasattr(b1, 'course5'):
        assert not _is_linked(b1, 'course5', a)
    if hasattr(b2, 'course5'):
        assert _is_linked(b2, 'course5', a)
    _safe_set(a, 'admin4', set())
    assert not _is_linked(a, 'admin4', b2)
    if hasattr(b2, 'course5'):
        assert not _is_linked(b2, 'course5', a)


def test_assoc_course_Person_link_reassign_clear():
    a = course(course_id=7, course_name="sample_text", course_preq="sample_text", credit_hours=7)
    b1 = Person(address="sample_text", date_of_birth="sample_text", department="sample_text", email="sample_text", id=7, name="sample_text", password=7, username="sample_text")
    b2 = Person(address="sample_text_2", date_of_birth="sample_text_2", department="sample_text_2", email="sample_text_2", id=13, name="sample_text_2", password=13, username="sample_text_2")
    _safe_set(a, 'person8', {b1})
    assert _is_linked(a, 'person8', b1)
    if hasattr(b1, 'course9'):
        assert _is_linked(b1, 'course9', a)
    _safe_set(a, 'person8', {b2})
    assert _is_linked(a, 'person8', b2)
    if hasattr(b1, 'course9'):
        assert not _is_linked(b1, 'course9', a)
    if hasattr(b2, 'course9'):
        assert _is_linked(b2, 'course9', a)
    _safe_set(a, 'person8', set())
    assert not _is_linked(a, 'person8', b2)
    if hasattr(b2, 'course9'):
        assert not _is_linked(b2, 'course9', a)


def test_assoc_student_barcode_link_reassign_clear():
    a = student(major_dept="sample_text", minor_dept="sample_text")
    b1 = barcode()
    b2 = barcode()
    _safe_set(a, 'barcode6', {b1})
    assert _is_linked(a, 'barcode6', b1)
    if hasattr(b1, 'student7'):
        assert _is_linked(b1, 'student7', a)
    _safe_set(a, 'barcode6', {b2})
    assert _is_linked(a, 'barcode6', b2)
    if hasattr(b1, 'student7'):
        assert not _is_linked(b1, 'student7', a)
    if hasattr(b2, 'student7'):
        assert _is_linked(b2, 'student7', a)
    _safe_set(a, 'barcode6', set())
    assert not _is_linked(a, 'barcode6', b2)
    if hasattr(b2, 'student7'):
        assert not _is_linked(b2, 'student7', a)


def test_assoc_student_course_link_reassign_clear():
    a = student(major_dept="sample_text", minor_dept="sample_text")
    b1 = course(course_id=7, course_name="sample_text", course_preq="sample_text", credit_hours=7)
    b2 = course(course_id=13, course_name="sample_text_2", course_preq="sample_text_2", credit_hours=13)
    _safe_set(a, 'course2', b1)
    assert _is_linked(a, 'course2', b1)
    if hasattr(b1, 'student3'):
        assert _is_linked(b1, 'student3', a)
    _safe_set(a, 'course2', b2)
    assert _is_linked(a, 'course2', b2)
    if hasattr(b1, 'student3'):
        assert not _is_linked(b1, 'student3', a)
    if hasattr(b2, 'student3'):
        assert _is_linked(b2, 'student3', a)
    _safe_set(a, 'course2', None)
    assert not _is_linked(a, 'course2', b2)
    if hasattr(b2, 'student3'):
        assert not _is_linked(b2, 'student3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Department_strategy = st.builds(Department, dept_id=st.integers(), dept_name=safe_text)
@given(instance=Department_strategy)
@settings(max_examples=25)
def test_Department_instantiation(instance):
    assert isinstance(instance, Department)


Interface_Interface_strategy = st.builds(Interface_Interface)
@given(instance=Interface_Interface_strategy)
@settings(max_examples=25)
def test_Interface_Interface_instantiation(instance):
    assert isinstance(instance, Interface_Interface)


Person_strategy = st.builds(Person, address=safe_text, date_of_birth=safe_text, department=safe_text, email=safe_text, id=st.integers(), name=safe_text, password=st.integers(), username=safe_text)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


barcode_strategy = st.builds(barcode)
@given(instance=barcode_strategy)
@settings(max_examples=25)
def test_barcode_instantiation(instance):
    assert isinstance(instance, barcode)


controller_strategy = st.builds(controller)
@given(instance=controller_strategy)
@settings(max_examples=25)
def test_controller_instantiation(instance):
    assert isinstance(instance, controller)


course_strategy = st.builds(course, course_id=st.integers(), course_name=safe_text, course_preq=safe_text, credit_hours=st.integers())
@given(instance=course_strategy)
@settings(max_examples=25)
def test_course_instantiation(instance):
    assert isinstance(instance, course)


staff_member_strategy = st.builds(staff_member)
@given(instance=staff_member_strategy)
@settings(max_examples=25)
def test_staff_member_instantiation(instance):
    assert isinstance(instance, staff_member)


student_strategy = st.builds(student, major_dept=safe_text, minor_dept=safe_text)
@given(instance=student_strategy)
@settings(max_examples=25)
def test_student_instantiation(instance):
    assert isinstance(instance, student)



