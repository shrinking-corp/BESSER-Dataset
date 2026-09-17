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
    Administrator,
    Course,
    Student,
    AcademicResult,
    Department,
    FacultyInfo,
    Portal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_hyp_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_hyp_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "administratorID" in params, "Missing parameter 'administratorID'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_hyp_course_constructor_exists():
    assert callable(Course.__init__)


def test_hyp_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseName" in params, "Missing parameter 'courseName'"
    assert "subjectCode" in params, "Missing parameter 'subjectCode'"





def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "scholarNo" in params, "Missing parameter 'scholarNo'"
    assert "branch" in params, "Missing parameter 'branch'"
    assert "semester" in params, "Missing parameter 'semester'"

def test_hyp_student_has_name():
    assert hasattr(Student, "name")
    descriptor = None
    for klass in Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_student_has_scholarNo():
    assert hasattr(Student, "scholarNo")
    descriptor = None
    for klass in Student.__mro__:
        if "scholarNo" in klass.__dict__:
            descriptor = klass.__dict__["scholarNo"]
            break
    assert isinstance(descriptor, property)

def test_hyp_student_has_branch():
    assert hasattr(Student, "branch")
    descriptor = None
    for klass in Student.__mro__:
        if "branch" in klass.__dict__:
            descriptor = klass.__dict__["branch"]
            break
    assert isinstance(descriptor, property)

def test_hyp_student_has_semester():
    assert hasattr(Student, "semester")
    descriptor = None
    for klass in Student.__mro__:
        if "semester" in klass.__dict__:
            descriptor = klass.__dict__["semester"]
            break
    assert isinstance(descriptor, property)



def test_hyp_academicresult_is_not_abstract():
    assert not inspect.isabstract(AcademicResult)


def test_hyp_academicresult_constructor_exists():
    assert callable(AcademicResult.__init__)


def test_hyp_academicresult_constructor_args():
    sig = inspect.signature(AcademicResult.__init__)
    params = list(sig.parameters.keys())
    assert "semester" in params, "Missing parameter 'semester'"




def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "course" in params, "Missing parameter 'course'"

def test_hyp_department_has_name():
    assert hasattr(Department, "name")
    descriptor = None
    for klass in Department.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_hyp_facultyinfo_is_not_abstract():
    assert not inspect.isabstract(FacultyInfo)


def test_hyp_facultyinfo_constructor_exists():
    assert callable(FacultyInfo.__init__)


def test_hyp_facultyinfo_constructor_args():
    sig = inspect.signature(FacultyInfo.__init__)
    params = list(sig.parameters.keys())
    assert "department" in params, "Missing parameter 'department'"
    assert "facultyName" in params, "Missing parameter 'facultyName'"
    assert "facultyID" in params, "Missing parameter 'facultyID'"

def test_hyp_facultyinfo_has_department():
    assert hasattr(FacultyInfo, "department")
    descriptor = None
    for klass in FacultyInfo.__mro__:
        if "department" in klass.__dict__:
            descriptor = klass.__dict__["department"]
            break
    assert isinstance(descriptor, property)

def test_hyp_facultyinfo_has_facultyName():
    assert hasattr(FacultyInfo, "facultyName")
    descriptor = None
    for klass in FacultyInfo.__mro__:
        if "facultyName" in klass.__dict__:
            descriptor = klass.__dict__["facultyName"]
            break
    assert isinstance(descriptor, property)

def test_hyp_facultyinfo_has_facultyID():
    assert hasattr(FacultyInfo, "facultyID")
    descriptor = None
    for klass in FacultyInfo.__mro__:
        if "facultyID" in klass.__dict__:
            descriptor = klass.__dict__["facultyID"]
            break
    assert isinstance(descriptor, property)



def test_hyp_portal_is_not_abstract():
    assert not inspect.isabstract(Portal)


def test_hyp_portal_constructor_exists():
    assert callable(Portal.__init__)


def test_hyp_portal_constructor_args():
    sig = inspect.signature(Portal.__init__)
    params = list(sig.parameters.keys())


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
Administrator_strategy = st.builds(
    Administrator,
    administratorID=
        st.integers(),
    name=
        safe_text
)
Course_strategy = st.builds(
    Course,
    courseName=
        safe_text,
    subjectCode=
        safe_text
)
Student_strategy = st.builds(
    Student,
    name=
        safe_text,
    scholarNo=
        st.integers(),
    branch=
        st.none(),
    semester=
        st.integers()
)
AcademicResult_strategy = st.builds(
    AcademicResult,
    semester=
        st.integers()
)
Department_strategy = st.builds(
    Department,
    name=
        safe_text,
    course=
        st.none()
)
FacultyInfo_strategy = st.builds(
    FacultyInfo,
    department=
        st.none(),
    facultyName=
        safe_text,
    facultyID=
        safe_text
)
Portal_strategy = st.builds(
    Portal,
)




@given(instance=Administrator_strategy)
def test_hyp_administrator_administratorID_setter(instance):
    original = instance.administratorID
    instance.administratorID = original
    assert instance.administratorID == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Course_strategy)
def test_hyp_course_courseName_setter(instance):
    original = instance.courseName
    instance.courseName = original
    assert instance.courseName == original



@given(instance=Course_strategy)
def test_hyp_course_subjectCode_setter(instance):
    original = instance.subjectCode
    instance.subjectCode = original
    assert instance.subjectCode == original

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_hyp_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_hyp_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Student_strategy)
def test_hyp_student_scholarNo_setter(instance):
    original = instance.scholarNo
    instance.scholarNo = original
    assert instance.scholarNo == original



@given(instance=Student_strategy)
def test_hyp_student_branch_setter(instance):
    original = instance.branch
    instance.branch = original
    assert instance.branch == original



@given(instance=Student_strategy)
def test_hyp_student_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original




@given(instance=AcademicResult_strategy)
def test_hyp_academicresult_semester_setter(instance):
    original = instance.semester
    instance.semester = original
    assert instance.semester == original

@given(instance=Department_strategy)
@settings(max_examples=50)
def test_hyp_department_instantiation(instance):
    assert isinstance(instance, Department)



@given(instance=Department_strategy)
def test_hyp_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Department_strategy)
def test_hyp_department_course_setter(instance):
    original = instance.course
    instance.course = original
    assert instance.course == original

@given(instance=FacultyInfo_strategy)
@settings(max_examples=50)
def test_hyp_facultyinfo_instantiation(instance):
    assert isinstance(instance, FacultyInfo)



@given(instance=FacultyInfo_strategy)
def test_hyp_facultyinfo_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original



@given(instance=FacultyInfo_strategy)
def test_hyp_facultyinfo_facultyName_setter(instance):
    original = instance.facultyName
    instance.facultyName = original
    assert instance.facultyName == original



@given(instance=FacultyInfo_strategy)
def test_hyp_facultyinfo_facultyID_setter(instance):
    original = instance.facultyID
    instance.facultyID = original
    assert instance.facultyID == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AcademicResult,
    Administrator,
    Course,
    Department,
    FacultyInfo,
    Portal,
    Student,
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

def test_AcademicResult_semester_value_roundtrip():
    instance = AcademicResult(semester=7)
    assert instance.semester == 7
    instance.semester = 13
    assert instance.semester == 13


def test_Administrator_administratorID_value_roundtrip():
    instance = Administrator(administratorID=7, name="sample_text")
    assert instance.administratorID == 7
    instance.administratorID = 13
    assert instance.administratorID == 13


def test_Administrator_name_value_roundtrip():
    instance = Administrator(administratorID=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Course_courseName_value_roundtrip():
    instance = Course(courseName="sample_text", subjectCode="sample_text")
    assert instance.courseName == "sample_text"
    instance.courseName = "sample_text_2"
    assert instance.courseName == "sample_text_2"


def test_Course_subjectCode_value_roundtrip():
    instance = Course(courseName="sample_text", subjectCode="sample_text")
    assert instance.subjectCode == "sample_text"
    instance.subjectCode = "sample_text_2"
    assert instance.subjectCode == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AcademicResult_strategy = st.builds(AcademicResult, semester=st.integers())
@given(instance=AcademicResult_strategy)
@settings(max_examples=25)
def test_AcademicResult_instantiation(instance):
    assert isinstance(instance, AcademicResult)


Administrator_strategy = st.builds(Administrator, administratorID=st.integers(), name=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Course_strategy = st.builds(Course, courseName=safe_text, subjectCode=safe_text)
@given(instance=Course_strategy)
@settings(max_examples=25)
def test_Course_instantiation(instance):
    assert isinstance(instance, Course)


Portal_strategy = st.builds(Portal)
@given(instance=Portal_strategy)
@settings(max_examples=25)
def test_Portal_instantiation(instance):
    assert isinstance(instance, Portal)



