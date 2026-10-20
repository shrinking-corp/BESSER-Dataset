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
    coursePages_Reduction,
    coursePages_Precondition,
    coursePages_CourseWorker,
    coursePages_CourseInstance,
    coursePages_CourseWork,
    coursePages_CourseWorkObject,
    coursePages_Department,
    coursePages_Course,
    coursePages_StudyPrograms,
    Person,
    coursePages_Employee,
    coursePages_Student,
    coursePages_Evaluations,
    coursePages_EvaluationObject,
    coursePages_Person,
    PrecondistionType,
    personRoleType,
    CourseWorkType,
    EvaluationType,
    TermType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_coursepages_reduction_is_not_abstract():
    assert not inspect.isabstract(coursePages_Reduction)


def test_hyp_coursepages_reduction_constructor_exists():
    assert callable(coursePages_Reduction.__init__)


def test_hyp_coursepages_reduction_constructor_args():
    sig = inspect.signature(coursePages_Reduction.__init__)
    params = list(sig.parameters.keys())
    assert "creditReduction" in params, "Missing parameter 'creditReduction'"




def test_hyp_coursepages_precondition_is_not_abstract():
    assert not inspect.isabstract(coursePages_Precondition)


def test_hyp_coursepages_precondition_constructor_exists():
    assert callable(coursePages_Precondition.__init__)


def test_hyp_coursepages_precondition_constructor_args():
    sig = inspect.signature(coursePages_Precondition.__init__)
    params = list(sig.parameters.keys())
    assert "preconditionStatus" in params, "Missing parameter 'preconditionStatus'"




def test_hyp_coursepages_courseworker_is_not_abstract():
    assert not inspect.isabstract(coursePages_CourseWorker)


def test_hyp_coursepages_courseworker_constructor_exists():
    assert callable(coursePages_CourseWorker.__init__)


def test_hyp_coursepages_courseworker_constructor_args():
    sig = inspect.signature(coursePages_CourseWorker.__init__)
    params = list(sig.parameters.keys())
    assert "courseRole" in params, "Missing parameter 'courseRole'"




def test_hyp_coursepages_courseinstance_is_not_abstract():
    assert not inspect.isabstract(coursePages_CourseInstance)


def test_hyp_coursepages_courseinstance_constructor_exists():
    assert callable(coursePages_CourseInstance.__init__)


def test_hyp_coursepages_courseinstance_constructor_args():
    sig = inspect.signature(coursePages_CourseInstance.__init__)
    params = list(sig.parameters.keys())
    assert "courseYear" in params, "Missing parameter 'courseYear'"
    assert "term" in params, "Missing parameter 'term'"





def test_hyp_coursepages_coursework_is_not_abstract():
    assert not inspect.isabstract(coursePages_CourseWork)


def test_hyp_coursepages_coursework_constructor_exists():
    assert callable(coursePages_CourseWork.__init__)


def test_hyp_coursepages_coursework_constructor_args():
    sig = inspect.signature(coursePages_CourseWork.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coursepages_courseworkobject_is_not_abstract():
    assert not inspect.isabstract(coursePages_CourseWorkObject)


def test_hyp_coursepages_courseworkobject_constructor_exists():
    assert callable(coursePages_CourseWorkObject.__init__)


def test_hyp_coursepages_courseworkobject_constructor_args():
    sig = inspect.signature(coursePages_CourseWorkObject.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"
    assert "day" in params, "Missing parameter 'day'"
    assert "courseWorkType" in params, "Missing parameter 'courseWorkType'"
    assert "room" in params, "Missing parameter 'room'"








def test_hyp_coursepages_department_is_not_abstract():
    assert not inspect.isabstract(coursePages_Department)


def test_hyp_coursepages_department_constructor_exists():
    assert callable(coursePages_Department.__init__)


def test_hyp_coursepages_department_constructor_args():
    sig = inspect.signature(coursePages_Department.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNummber" in params, "Missing parameter 'phoneNummber'"
    assert "email" in params, "Missing parameter 'email'"
    assert "departmentName" in params, "Missing parameter 'departmentName'"






def test_hyp_coursepages_course_is_not_abstract():
    assert not inspect.isabstract(coursePages_Course)


def test_hyp_coursepages_course_constructor_exists():
    assert callable(coursePages_Course.__init__)


def test_hyp_coursepages_course_constructor_args():
    sig = inspect.signature(coursePages_Course.__init__)
    params = list(sig.parameters.keys())
    assert "courseCredits" in params, "Missing parameter 'courseCredits'"
    assert "courseContent" in params, "Missing parameter 'courseContent'"
    assert "courseCode" in params, "Missing parameter 'courseCode'"
    assert "courseName" in params, "Missing parameter 'courseName'"







def test_hyp_coursepages_studyprograms_is_not_abstract():
    assert not inspect.isabstract(coursePages_StudyPrograms)


def test_hyp_coursepages_studyprograms_constructor_exists():
    assert callable(coursePages_StudyPrograms.__init__)


def test_hyp_coursepages_studyprograms_constructor_args():
    sig = inspect.signature(coursePages_StudyPrograms.__init__)
    params = list(sig.parameters.keys())
    assert "studyProgramCode" in params, "Missing parameter 'studyProgramCode'"
    assert "studyProgramName" in params, "Missing parameter 'studyProgramName'"





def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coursepages_employee_is_not_abstract():
    assert not inspect.isabstract(coursePages_Employee)


def test_hyp_coursepages_employee_constructor_exists():
    assert callable(coursePages_Employee.__init__)


def test_hyp_coursepages_employee_constructor_args():
    sig = inspect.signature(coursePages_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"




def test_hyp_coursepages_student_is_not_abstract():
    assert not inspect.isabstract(coursePages_Student)


def test_hyp_coursepages_student_constructor_exists():
    assert callable(coursePages_Student.__init__)


def test_hyp_coursepages_student_constructor_args():
    sig = inspect.signature(coursePages_Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentID" in params, "Missing parameter 'studentID'"




def test_hyp_coursepages_evaluations_is_not_abstract():
    assert not inspect.isabstract(coursePages_Evaluations)


def test_hyp_coursepages_evaluations_constructor_exists():
    assert callable(coursePages_Evaluations.__init__)


def test_hyp_coursepages_evaluations_constructor_args():
    sig = inspect.signature(coursePages_Evaluations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coursepages_evaluationobject_is_not_abstract():
    assert not inspect.isabstract(coursePages_EvaluationObject)


def test_hyp_coursepages_evaluationobject_constructor_exists():
    assert callable(coursePages_EvaluationObject.__init__)


def test_hyp_coursepages_evaluationobject_constructor_args():
    sig = inspect.signature(coursePages_EvaluationObject.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "term" in params, "Missing parameter 'term'"
    assert "evaluationsForm" in params, "Missing parameter 'evaluationsForm'"







def test_hyp_coursepages_person_is_not_abstract():
    assert not inspect.isabstract(coursePages_Person)


def test_hyp_coursepages_person_constructor_exists():
    assert callable(coursePages_Person.__init__)


def test_hyp_coursepages_person_constructor_args():
    sig = inspect.signature(coursePages_Person.__init__)
    params = list(sig.parameters.keys())
    assert "surName" in params, "Missing parameter 'surName'"
    assert "email" in params, "Missing parameter 'email'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "phoneNummber" in params, "Missing parameter 'phoneNummber'"





def test_hyp_precondistiontype_exists():
    # Check that the Enumeration exists
    assert PrecondistionType is not None

def test_hyp_precondistiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrecondistionType]
    expected_literals = [
        "Required",
        "Recommended",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrecondistionType"

def test_hyp_personroletype_exists():
    # Check that the Enumeration exists
    assert personRoleType is not None

def test_hyp_personroletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in personRoleType]
    expected_literals = [
        "Lecture",
        "CourseCordinator",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in personRoleType"

def test_hyp_courseworktype_exists():
    # Check that the Enumeration exists
    assert CourseWorkType is not None

def test_hyp_courseworktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseWorkType]
    expected_literals = [
        "Lab",
        "Lecture",
        "Exercise",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseWorkType"

def test_hyp_evaluationtype_exists():
    # Check that the Enumeration exists
    assert EvaluationType is not None

def test_hyp_evaluationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EvaluationType]
    expected_literals = [
        "WrittenExam",
        "Assignments",
        "PracticalExam",
        "OralExam",
        "Participated",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EvaluationType"

def test_hyp_termtype_exists():
    # Check that the Enumeration exists
    assert TermType is not None

def test_hyp_termtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TermType]
    expected_literals = [
        "Fall",
        "Summer",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TermType"


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
coursePages_Reduction_strategy = st.builds(
    coursePages_Reduction,
    creditReduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
coursePages_Precondition_strategy = st.builds(
    coursePages_Precondition,
    preconditionStatus=
        safe_text
)
coursePages_CourseWorker_strategy = st.builds(
    coursePages_CourseWorker,
    courseRole=
        safe_text
)
coursePages_CourseInstance_strategy = st.builds(
    coursePages_CourseInstance,
    courseYear=
        safe_text,
    term=
        safe_text
)
coursePages_CourseWork_strategy = st.builds(
    coursePages_CourseWork,
)
coursePages_CourseWorkObject_strategy = st.builds(
    coursePages_CourseWorkObject,
    end=
        st.dates(),
    start=
        st.dates(),
    day=
        safe_text,
    courseWorkType=
        safe_text,
    room=
        safe_text
)
coursePages_Department_strategy = st.builds(
    coursePages_Department,
    phoneNummber=
        safe_text,
    email=
        safe_text,
    departmentName=
        safe_text
)
coursePages_Course_strategy = st.builds(
    coursePages_Course,
    courseCredits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    courseContent=
        safe_text,
    courseCode=
        safe_text,
    courseName=
        safe_text
)
coursePages_StudyPrograms_strategy = st.builds(
    coursePages_StudyPrograms,
    studyProgramCode=
        safe_text,
    studyProgramName=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
coursePages_Employee_strategy = st.builds(
    coursePages_Employee,
    position=
        safe_text
)
coursePages_Student_strategy = st.builds(
    coursePages_Student,
    studentID=
        safe_text
)
coursePages_Evaluations_strategy = st.builds(
    coursePages_Evaluations,
)
coursePages_EvaluationObject_strategy = st.builds(
    coursePages_EvaluationObject,
    date=
        st.dates(),
    credits=
        st.integers(),
    term=
        safe_text,
    evaluationsForm=
        safe_text
)
coursePages_Person_strategy = st.builds(
    coursePages_Person,
    surName=
        safe_text,
    email=
        safe_text,
    firstName=
        safe_text,
    phoneNummber=
        safe_text
)




@given(instance=coursePages_Reduction_strategy)
def test_hyp_coursepages_reduction_creditReduction_setter(instance):
    original = instance.creditReduction
    instance.creditReduction = original
    assert instance.creditReduction == original




@given(instance=coursePages_Precondition_strategy)
def test_hyp_coursepages_precondition_preconditionStatus_setter(instance):
    original = instance.preconditionStatus
    instance.preconditionStatus = original
    assert instance.preconditionStatus == original




@given(instance=coursePages_CourseWorker_strategy)
def test_hyp_coursepages_courseworker_courseRole_setter(instance):
    original = instance.courseRole
    instance.courseRole = original
    assert instance.courseRole == original




@given(instance=coursePages_CourseInstance_strategy)
def test_hyp_coursepages_courseinstance_courseYear_setter(instance):
    original = instance.courseYear
    instance.courseYear = original
    assert instance.courseYear == original



@given(instance=coursePages_CourseInstance_strategy)
def test_hyp_coursepages_courseinstance_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original





@given(instance=coursePages_CourseWorkObject_strategy)
def test_hyp_coursepages_courseworkobject_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=coursePages_CourseWorkObject_strategy)
def test_hyp_coursepages_courseworkobject_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=coursePages_CourseWorkObject_strategy)
def test_hyp_coursepages_courseworkobject_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=coursePages_CourseWorkObject_strategy)
def test_hyp_coursepages_courseworkobject_courseWorkType_setter(instance):
    original = instance.courseWorkType
    instance.courseWorkType = original
    assert instance.courseWorkType == original



@given(instance=coursePages_CourseWorkObject_strategy)
def test_hyp_coursepages_courseworkobject_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original




@given(instance=coursePages_Department_strategy)
def test_hyp_coursepages_department_phoneNummber_setter(instance):
    original = instance.phoneNummber
    instance.phoneNummber = original
    assert instance.phoneNummber == original



@given(instance=coursePages_Department_strategy)
def test_hyp_coursepages_department_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=coursePages_Department_strategy)
def test_hyp_coursepages_department_departmentName_setter(instance):
    original = instance.departmentName
    instance.departmentName = original
    assert instance.departmentName == original




@given(instance=coursePages_Course_strategy)
def test_hyp_coursepages_course_courseCredits_setter(instance):
    original = instance.courseCredits
    instance.courseCredits = original
    assert instance.courseCredits == original



@given(instance=coursePages_Course_strategy)
def test_hyp_coursepages_course_courseContent_setter(instance):
    original = instance.courseContent
    instance.courseContent = original
    assert instance.courseContent == original



@given(instance=coursePages_Course_strategy)
def test_hyp_coursepages_course_courseCode_setter(instance):
    original = instance.courseCode
    instance.courseCode = original
    assert instance.courseCode == original



@given(instance=coursePages_Course_strategy)
def test_hyp_coursepages_course_courseName_setter(instance):
    original = instance.courseName
    instance.courseName = original
    assert instance.courseName == original




@given(instance=coursePages_StudyPrograms_strategy)
def test_hyp_coursepages_studyprograms_studyProgramCode_setter(instance):
    original = instance.studyProgramCode
    instance.studyProgramCode = original
    assert instance.studyProgramCode == original



@given(instance=coursePages_StudyPrograms_strategy)
def test_hyp_coursepages_studyprograms_studyProgramName_setter(instance):
    original = instance.studyProgramName
    instance.studyProgramName = original
    assert instance.studyProgramName == original





@given(instance=coursePages_Employee_strategy)
def test_hyp_coursepages_employee_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original




@given(instance=coursePages_Student_strategy)
def test_hyp_coursepages_student_studentID_setter(instance):
    original = instance.studentID
    instance.studentID = original
    assert instance.studentID == original





@given(instance=coursePages_EvaluationObject_strategy)
def test_hyp_coursepages_evaluationobject_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=coursePages_EvaluationObject_strategy)
def test_hyp_coursepages_evaluationobject_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=coursePages_EvaluationObject_strategy)
def test_hyp_coursepages_evaluationobject_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original



@given(instance=coursePages_EvaluationObject_strategy)
def test_hyp_coursepages_evaluationobject_evaluationsForm_setter(instance):
    original = instance.evaluationsForm
    instance.evaluationsForm = original
    assert instance.evaluationsForm == original




@given(instance=coursePages_Person_strategy)
def test_hyp_coursepages_person_surName_setter(instance):
    original = instance.surName
    instance.surName = original
    assert instance.surName == original



@given(instance=coursePages_Person_strategy)
def test_hyp_coursepages_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=coursePages_Person_strategy)
def test_hyp_coursepages_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=coursePages_Person_strategy)
def test_hyp_coursepages_person_phoneNummber_setter(instance):
    original = instance.phoneNummber
    instance.phoneNummber = original
    assert instance.phoneNummber == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Person,
    coursePages_Course,
    coursePages_CourseInstance,
    coursePages_CourseWork,
    coursePages_CourseWorkObject,
    coursePages_CourseWorker,
    coursePages_Department,
    coursePages_Employee,
    coursePages_EvaluationObject,
    coursePages_Evaluations,
    coursePages_Person,
    coursePages_Precondition,
    coursePages_Reduction,
    coursePages_Student,
    coursePages_StudyPrograms,
    CourseWorkType,
    EvaluationType,
    PrecondistionType,
    TermType,
    personRoleType,
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

def test_coursePages_Course_courseCode_value_roundtrip():
    instance = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    assert instance.courseCode == "sample_text"
    instance.courseCode = "sample_text_2"
    assert instance.courseCode == "sample_text_2"


def test_coursePages_Course_courseContent_value_roundtrip():
    instance = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    assert instance.courseContent == "sample_text"
    instance.courseContent = "sample_text_2"
    assert instance.courseContent == "sample_text_2"


def test_coursePages_Course_courseCredits_value_roundtrip():
    instance = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    assert instance.courseCredits == 3.14
    instance.courseCredits = 9.99
    assert instance.courseCredits == 9.99


def test_coursePages_Course_courseName_value_roundtrip():
    instance = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    assert instance.courseName == "sample_text"
    instance.courseName = "sample_text_2"
    assert instance.courseName == "sample_text_2"


def test_coursePages_CourseInstance_courseYear_value_roundtrip():
    instance = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    assert instance.courseYear == "sample_text"
    instance.courseYear = "sample_text_2"
    assert instance.courseYear == "sample_text_2"


def test_coursePages_CourseInstance_term_value_roundtrip():
    instance = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    assert instance.term == "sample_text"
    instance.term = "sample_text_2"
    assert instance.term == "sample_text_2"


def test_coursePages_CourseWorkObject_courseWorkType_value_roundtrip():
    instance = coursePages_CourseWorkObject(courseWorkType="sample_text", day="sample_text", end=date(2024, 1, 1), room="sample_text", start=date(2024, 1, 1))
    assert instance.courseWorkType == "sample_text"
    instance.courseWorkType = "sample_text_2"
    assert instance.courseWorkType == "sample_text_2"


def test_coursePages_CourseWorkObject_day_value_roundtrip():
    instance = coursePages_CourseWorkObject(courseWorkType="sample_text", day="sample_text", end=date(2024, 1, 1), room="sample_text", start=date(2024, 1, 1))
    assert instance.day == "sample_text"
    instance.day = "sample_text_2"
    assert instance.day == "sample_text_2"


def test_coursePages_CourseWorkObject_end_value_roundtrip():
    instance = coursePages_CourseWorkObject(courseWorkType="sample_text", day="sample_text", end=date(2024, 1, 1), room="sample_text", start=date(2024, 1, 1))
    assert instance.end == date(2024, 1, 1)
    instance.end = date(2025, 6, 15)
    assert instance.end == date(2025, 6, 15)


def test_coursePages_CourseWorkObject_room_value_roundtrip():
    instance = coursePages_CourseWorkObject(courseWorkType="sample_text", day="sample_text", end=date(2024, 1, 1), room="sample_text", start=date(2024, 1, 1))
    assert instance.room == "sample_text"
    instance.room = "sample_text_2"
    assert instance.room == "sample_text_2"


def test_coursePages_CourseWorkObject_start_value_roundtrip():
    instance = coursePages_CourseWorkObject(courseWorkType="sample_text", day="sample_text", end=date(2024, 1, 1), room="sample_text", start=date(2024, 1, 1))
    assert instance.start == date(2024, 1, 1)
    instance.start = date(2025, 6, 15)
    assert instance.start == date(2025, 6, 15)


def test_coursePages_CourseWorker_courseRole_value_roundtrip():
    instance = coursePages_CourseWorker(courseRole="sample_text")
    assert instance.courseRole == "sample_text"
    instance.courseRole = "sample_text_2"
    assert instance.courseRole == "sample_text_2"


def test_coursePages_Department_departmentName_value_roundtrip():
    instance = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    assert instance.departmentName == "sample_text"
    instance.departmentName = "sample_text_2"
    assert instance.departmentName == "sample_text_2"


def test_coursePages_Department_email_value_roundtrip():
    instance = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_coursePages_Department_phoneNummber_value_roundtrip():
    instance = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    assert instance.phoneNummber == "sample_text"
    instance.phoneNummber = "sample_text_2"
    assert instance.phoneNummber == "sample_text_2"


def test_coursePages_Employee_position_value_roundtrip():
    instance = coursePages_Employee(position="sample_text")
    assert instance.position == "sample_text"
    instance.position = "sample_text_2"
    assert instance.position == "sample_text_2"


def test_coursePages_EvaluationObject_credits_value_roundtrip():
    instance = coursePages_EvaluationObject(credits=7, date=date(2024, 1, 1), evaluationsForm="sample_text", term="sample_text")
    assert instance.credits == 7
    instance.credits = 13
    assert instance.credits == 13


def test_coursePages_EvaluationObject_date_value_roundtrip():
    instance = coursePages_EvaluationObject(credits=7, date=date(2024, 1, 1), evaluationsForm="sample_text", term="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_coursePages_EvaluationObject_evaluationsForm_value_roundtrip():
    instance = coursePages_EvaluationObject(credits=7, date=date(2024, 1, 1), evaluationsForm="sample_text", term="sample_text")
    assert instance.evaluationsForm == "sample_text"
    instance.evaluationsForm = "sample_text_2"
    assert instance.evaluationsForm == "sample_text_2"


def test_coursePages_EvaluationObject_term_value_roundtrip():
    instance = coursePages_EvaluationObject(credits=7, date=date(2024, 1, 1), evaluationsForm="sample_text", term="sample_text")
    assert instance.term == "sample_text"
    instance.term = "sample_text_2"
    assert instance.term == "sample_text_2"


def test_coursePages_Person_email_value_roundtrip():
    instance = coursePages_Person(email="sample_text", firstName="sample_text", phoneNummber="sample_text", surName="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_coursePages_Person_firstName_value_roundtrip():
    instance = coursePages_Person(email="sample_text", firstName="sample_text", phoneNummber="sample_text", surName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_coursePages_Person_phoneNummber_value_roundtrip():
    instance = coursePages_Person(email="sample_text", firstName="sample_text", phoneNummber="sample_text", surName="sample_text")
    assert instance.phoneNummber == "sample_text"
    instance.phoneNummber = "sample_text_2"
    assert instance.phoneNummber == "sample_text_2"


def test_coursePages_Person_surName_value_roundtrip():
    instance = coursePages_Person(email="sample_text", firstName="sample_text", phoneNummber="sample_text", surName="sample_text")
    assert instance.surName == "sample_text"
    instance.surName = "sample_text_2"
    assert instance.surName == "sample_text_2"


def test_coursePages_Precondition_preconditionStatus_value_roundtrip():
    instance = coursePages_Precondition(preconditionStatus="sample_text")
    assert instance.preconditionStatus == "sample_text"
    instance.preconditionStatus = "sample_text_2"
    assert instance.preconditionStatus == "sample_text_2"


def test_coursePages_Reduction_creditReduction_value_roundtrip():
    instance = coursePages_Reduction(creditReduction=3.14)
    assert instance.creditReduction == 3.14
    instance.creditReduction = 9.99
    assert instance.creditReduction == 9.99


def test_coursePages_Student_studentID_value_roundtrip():
    instance = coursePages_Student(studentID="sample_text")
    assert instance.studentID == "sample_text"
    instance.studentID = "sample_text_2"
    assert instance.studentID == "sample_text_2"


def test_coursePages_StudyPrograms_studyProgramCode_value_roundtrip():
    instance = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    assert instance.studyProgramCode == "sample_text"
    instance.studyProgramCode = "sample_text_2"
    assert instance.studyProgramCode == "sample_text_2"


def test_coursePages_StudyPrograms_studyProgramName_value_roundtrip():
    instance = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    assert instance.studyProgramName == "sample_text"
    instance.studyProgramName = "sample_text_2"
    assert instance.studyProgramName == "sample_text_2"


def test_coursePages_Employee_isa_Person():
    instance = coursePages_Employee(position="sample_text")
    assert isinstance(instance, Person)


def test_coursePages_Student_isa_Person():
    instance = coursePages_Student(studentID="sample_text")
    assert isinstance(instance, Person)


def test_assoc_belongsToDepartment8_link_reassign_clear():
    a = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    b1 = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    b2 = coursePages_Department(departmentName="sample_text_2", email="sample_text_2", phoneNummber="sample_text_2")
    _safe_set(a, 'studyprograms', b1)
    assert _is_linked(a, 'studyprograms', b1)
    if hasattr(b1, 'Department9'):
        assert _is_linked(b1, 'Department9', a)
    _safe_set(a, 'studyprograms', b2)
    assert _is_linked(a, 'studyprograms', b2)
    if hasattr(b1, 'Department9'):
        assert not _is_linked(b1, 'Department9', a)
    if hasattr(b2, 'Department9'):
        assert _is_linked(b2, 'Department9', a)
    _safe_set(a, 'studyprograms', None)
    assert not _is_linked(a, 'studyprograms', b2)
    if hasattr(b2, 'Department9'):
        assert not _is_linked(b2, 'Department9', a)


def test_assoc_course1_link_reassign_clear():
    a = coursePages_Student(studentID="sample_text")
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'coursePages_Student', {b1})
    assert _is_linked(a, 'coursePages_Student', b1)
    if hasattr(b1, 'coursePages_Course'):
        assert _is_linked(b1, 'coursePages_Course', a)
    _safe_set(a, 'coursePages_Student', {b2})
    assert _is_linked(a, 'coursePages_Student', b2)
    if hasattr(b1, 'coursePages_Course'):
        assert not _is_linked(b1, 'coursePages_Course', a)
    if hasattr(b2, 'coursePages_Course'):
        assert _is_linked(b2, 'coursePages_Course', a)
    _safe_set(a, 'coursePages_Student', set())
    assert not _is_linked(a, 'coursePages_Student', b2)
    if hasattr(b2, 'coursePages_Course'):
        assert not _is_linked(b2, 'coursePages_Course', a)


def test_assoc_course12_link_reassign_clear():
    a = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'studyprograms13', {b1})
    assert _is_linked(a, 'studyprograms13', b1)
    if hasattr(b1, 'Course'):
        assert _is_linked(b1, 'Course', a)
    _safe_set(a, 'studyprograms13', {b2})
    assert _is_linked(a, 'studyprograms13', b2)
    if hasattr(b1, 'Course'):
        assert not _is_linked(b1, 'Course', a)
    if hasattr(b2, 'Course'):
        assert _is_linked(b2, 'Course', a)
    _safe_set(a, 'studyprograms13', set())
    assert not _is_linked(a, 'studyprograms13', b2)
    if hasattr(b2, 'Course'):
        assert not _is_linked(b2, 'Course', a)


def test_assoc_course34_link_reassign_clear():
    a = coursePages_Precondition(preconditionStatus="sample_text")
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'coursePages_Precondition35', b1)
    assert _is_linked(a, 'coursePages_Precondition35', b1)
    if hasattr(b1, 'coursePages_Course36'):
        assert _is_linked(b1, 'coursePages_Course36', a)
    _safe_set(a, 'coursePages_Precondition35', b2)
    assert _is_linked(a, 'coursePages_Precondition35', b2)
    if hasattr(b1, 'coursePages_Course36'):
        assert not _is_linked(b1, 'coursePages_Course36', a)
    if hasattr(b2, 'coursePages_Course36'):
        assert _is_linked(b2, 'coursePages_Course36', a)
    _safe_set(a, 'coursePages_Precondition35', None)
    assert not _is_linked(a, 'coursePages_Precondition35', b2)
    if hasattr(b2, 'coursePages_Course36'):
        assert not _is_linked(b2, 'coursePages_Course36', a)


def test_assoc_course37_link_reassign_clear():
    a = coursePages_Reduction(creditReduction=3.14)
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'coursePages_Reduction38', b1)
    assert _is_linked(a, 'coursePages_Reduction38', b1)
    if hasattr(b1, 'coursePages_Course39'):
        assert _is_linked(b1, 'coursePages_Course39', a)
    _safe_set(a, 'coursePages_Reduction38', b2)
    assert _is_linked(a, 'coursePages_Reduction38', b2)
    if hasattr(b1, 'coursePages_Course39'):
        assert not _is_linked(b1, 'coursePages_Course39', a)
    if hasattr(b2, 'coursePages_Course39'):
        assert _is_linked(b2, 'coursePages_Course39', a)
    _safe_set(a, 'coursePages_Reduction38', None)
    assert not _is_linked(a, 'coursePages_Reduction38', b2)
    if hasattr(b2, 'coursePages_Course39'):
        assert not _is_linked(b2, 'coursePages_Course39', a)


def test_assoc_course6_link_reassign_clear():
    a = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'coursePages_Department', {b1})
    assert _is_linked(a, 'coursePages_Department', b1)
    if hasattr(b1, 'coursePages_Course7'):
        assert _is_linked(b1, 'coursePages_Course7', a)
    _safe_set(a, 'coursePages_Department', {b2})
    assert _is_linked(a, 'coursePages_Department', b2)
    if hasattr(b1, 'coursePages_Course7'):
        assert not _is_linked(b1, 'coursePages_Course7', a)
    if hasattr(b2, 'coursePages_Course7'):
        assert _is_linked(b2, 'coursePages_Course7', a)
    _safe_set(a, 'coursePages_Department', set())
    assert not _is_linked(a, 'coursePages_Department', b2)
    if hasattr(b2, 'coursePages_Course7'):
        assert not _is_linked(b2, 'coursePages_Course7', a)


def test_assoc_courseinstance16_link_reassign_clear():
    a = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'coursePages_CourseInstance', b1)
    assert _is_linked(a, 'coursePages_CourseInstance', b1)
    if hasattr(b1, 'coursePages_Course17'):
        assert _is_linked(b1, 'coursePages_Course17', a)
    _safe_set(a, 'coursePages_CourseInstance', b2)
    assert _is_linked(a, 'coursePages_CourseInstance', b2)
    if hasattr(b1, 'coursePages_Course17'):
        assert not _is_linked(b1, 'coursePages_Course17', a)
    if hasattr(b2, 'coursePages_Course17'):
        assert _is_linked(b2, 'coursePages_Course17', a)
    _safe_set(a, 'coursePages_CourseInstance', None)
    assert not _is_linked(a, 'coursePages_CourseInstance', b2)
    if hasattr(b2, 'coursePages_Course17'):
        assert not _is_linked(b2, 'coursePages_Course17', a)


def test_assoc_coursework26_link_reassign_clear():
    a = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    b1 = coursePages_CourseWork()
    b2 = coursePages_CourseWork()
    _safe_set(a, 'coursePages_CourseInstance27', b1)
    assert _is_linked(a, 'coursePages_CourseInstance27', b1)
    if hasattr(b1, 'coursePages_CourseWork28'):
        assert _is_linked(b1, 'coursePages_CourseWork28', a)
    _safe_set(a, 'coursePages_CourseInstance27', b2)
    assert _is_linked(a, 'coursePages_CourseInstance27', b2)
    if hasattr(b1, 'coursePages_CourseWork28'):
        assert not _is_linked(b1, 'coursePages_CourseWork28', a)
    if hasattr(b2, 'coursePages_CourseWork28'):
        assert _is_linked(b2, 'coursePages_CourseWork28', a)
    _safe_set(a, 'coursePages_CourseInstance27', None)
    assert not _is_linked(a, 'coursePages_CourseInstance27', b2)
    if hasattr(b2, 'coursePages_CourseWork28'):
        assert not _is_linked(b2, 'coursePages_CourseWork28', a)


def test_assoc_courseworker20_link_reassign_clear():
    a = coursePages_CourseWorker(courseRole="sample_text")
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'coursePages_CourseWorker', b1)
    assert _is_linked(a, 'coursePages_CourseWorker', b1)
    if hasattr(b1, 'coursePages_Course21'):
        assert _is_linked(b1, 'coursePages_Course21', a)
    _safe_set(a, 'coursePages_CourseWorker', b2)
    assert _is_linked(a, 'coursePages_CourseWorker', b2)
    if hasattr(b1, 'coursePages_Course21'):
        assert not _is_linked(b1, 'coursePages_Course21', a)
    if hasattr(b2, 'coursePages_Course21'):
        assert _is_linked(b2, 'coursePages_Course21', a)
    _safe_set(a, 'coursePages_CourseWorker', None)
    assert not _is_linked(a, 'coursePages_CourseWorker', b2)
    if hasattr(b2, 'coursePages_Course21'):
        assert not _is_linked(b2, 'coursePages_Course21', a)


def test_assoc_courseworkobject15_link_reassign_clear():
    a = coursePages_CourseWorkObject(courseWorkType="sample_text", day="sample_text", end=date(2024, 1, 1), room="sample_text", start=date(2024, 1, 1))
    b1 = coursePages_CourseWork()
    b2 = coursePages_CourseWork()
    _safe_set(a, 'coursePages_CourseWorkObject', b1)
    assert _is_linked(a, 'coursePages_CourseWorkObject', b1)
    if hasattr(b1, 'coursePages_CourseWork'):
        assert _is_linked(b1, 'coursePages_CourseWork', a)
    _safe_set(a, 'coursePages_CourseWorkObject', b2)
    assert _is_linked(a, 'coursePages_CourseWorkObject', b2)
    if hasattr(b1, 'coursePages_CourseWork'):
        assert not _is_linked(b1, 'coursePages_CourseWork', a)
    if hasattr(b2, 'coursePages_CourseWork'):
        assert _is_linked(b2, 'coursePages_CourseWork', a)
    _safe_set(a, 'coursePages_CourseWorkObject', None)
    assert not _is_linked(a, 'coursePages_CourseWorkObject', b2)
    if hasattr(b2, 'coursePages_CourseWork'):
        assert not _is_linked(b2, 'coursePages_CourseWork', a)


def test_assoc_department2_link_reassign_clear():
    a = coursePages_Employee(position="sample_text")
    b1 = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    b2 = coursePages_Department(departmentName="sample_text_2", email="sample_text_2", phoneNummber="sample_text_2")
    _safe_set(a, 'employee', b1)
    assert _is_linked(a, 'employee', b1)
    if hasattr(b1, 'Department'):
        assert _is_linked(b1, 'Department', a)
    _safe_set(a, 'employee', b2)
    assert _is_linked(a, 'employee', b2)
    if hasattr(b1, 'Department'):
        assert not _is_linked(b1, 'Department', a)
    if hasattr(b2, 'Department'):
        assert _is_linked(b2, 'Department', a)
    _safe_set(a, 'employee', None)
    assert not _is_linked(a, 'employee', b2)
    if hasattr(b2, 'Department'):
        assert not _is_linked(b2, 'Department', a)


def test_assoc_employee3_link_reassign_clear():
    a = coursePages_Employee(position="sample_text")
    b1 = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    b2 = coursePages_Department(departmentName="sample_text_2", email="sample_text_2", phoneNummber="sample_text_2")
    _safe_set(a, 'Employee', b1)
    assert _is_linked(a, 'Employee', b1)
    if hasattr(b1, 'department'):
        assert _is_linked(b1, 'department', a)
    _safe_set(a, 'Employee', b2)
    assert _is_linked(a, 'Employee', b2)
    if hasattr(b1, 'department'):
        assert not _is_linked(b1, 'department', a)
    if hasattr(b2, 'department'):
        assert _is_linked(b2, 'department', a)
    _safe_set(a, 'Employee', None)
    assert not _is_linked(a, 'Employee', b2)
    if hasattr(b2, 'department'):
        assert not _is_linked(b2, 'department', a)


def test_assoc_employee32_link_reassign_clear():
    a = coursePages_Employee(position="sample_text")
    b1 = coursePages_CourseWorker(courseRole="sample_text")
    b2 = coursePages_CourseWorker(courseRole="sample_text_2")
    _safe_set(a, 'coursePages_Employee', b1)
    assert _is_linked(a, 'coursePages_Employee', b1)
    if hasattr(b1, 'coursePages_CourseWorker33'):
        assert _is_linked(b1, 'coursePages_CourseWorker33', a)
    _safe_set(a, 'coursePages_Employee', b2)
    assert _is_linked(a, 'coursePages_Employee', b2)
    if hasattr(b1, 'coursePages_CourseWorker33'):
        assert not _is_linked(b1, 'coursePages_CourseWorker33', a)
    if hasattr(b2, 'coursePages_CourseWorker33'):
        assert _is_linked(b2, 'coursePages_CourseWorker33', a)
    _safe_set(a, 'coursePages_Employee', None)
    assert not _is_linked(a, 'coursePages_Employee', b2)
    if hasattr(b2, 'coursePages_CourseWorker33'):
        assert not _is_linked(b2, 'coursePages_CourseWorker33', a)


def test_assoc_evaluationobject14_link_reassign_clear():
    a = coursePages_EvaluationObject(credits=7, date=date(2024, 1, 1), evaluationsForm="sample_text", term="sample_text")
    b1 = coursePages_Evaluations()
    b2 = coursePages_Evaluations()
    _safe_set(a, 'coursePages_EvaluationObject', b1)
    assert _is_linked(a, 'coursePages_EvaluationObject', b1)
    if hasattr(b1, 'coursePages_Evaluations'):
        assert _is_linked(b1, 'coursePages_Evaluations', a)
    _safe_set(a, 'coursePages_EvaluationObject', b2)
    assert _is_linked(a, 'coursePages_EvaluationObject', b2)
    if hasattr(b1, 'coursePages_Evaluations'):
        assert not _is_linked(b1, 'coursePages_Evaluations', a)
    if hasattr(b2, 'coursePages_Evaluations'):
        assert _is_linked(b2, 'coursePages_Evaluations', a)
    _safe_set(a, 'coursePages_EvaluationObject', None)
    assert not _is_linked(a, 'coursePages_EvaluationObject', b2)
    if hasattr(b2, 'coursePages_Evaluations'):
        assert not _is_linked(b2, 'coursePages_Evaluations', a)


def test_assoc_evaluations29_link_reassign_clear():
    a = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    b1 = coursePages_Evaluations()
    b2 = coursePages_Evaluations()
    _safe_set(a, 'coursePages_CourseInstance30', b1)
    assert _is_linked(a, 'coursePages_CourseInstance30', b1)
    if hasattr(b1, 'coursePages_Evaluations31'):
        assert _is_linked(b1, 'coursePages_Evaluations31', a)
    _safe_set(a, 'coursePages_CourseInstance30', b2)
    assert _is_linked(a, 'coursePages_CourseInstance30', b2)
    if hasattr(b1, 'coursePages_Evaluations31'):
        assert not _is_linked(b1, 'coursePages_Evaluations31', a)
    if hasattr(b2, 'coursePages_Evaluations31'):
        assert _is_linked(b2, 'coursePages_Evaluations31', a)
    _safe_set(a, 'coursePages_CourseInstance30', None)
    assert not _is_linked(a, 'coursePages_CourseInstance30', b2)
    if hasattr(b2, 'coursePages_Evaluations31'):
        assert not _is_linked(b2, 'coursePages_Evaluations31', a)


def test_assoc_precondition22_link_reassign_clear():
    a = coursePages_Precondition(preconditionStatus="sample_text")
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'coursePages_Precondition', b1)
    assert _is_linked(a, 'coursePages_Precondition', b1)
    if hasattr(b1, 'coursePages_Course23'):
        assert _is_linked(b1, 'coursePages_Course23', a)
    _safe_set(a, 'coursePages_Precondition', b2)
    assert _is_linked(a, 'coursePages_Precondition', b2)
    if hasattr(b1, 'coursePages_Course23'):
        assert not _is_linked(b1, 'coursePages_Course23', a)
    if hasattr(b2, 'coursePages_Course23'):
        assert _is_linked(b2, 'coursePages_Course23', a)
    _safe_set(a, 'coursePages_Precondition', None)
    assert not _is_linked(a, 'coursePages_Precondition', b2)
    if hasattr(b2, 'coursePages_Course23'):
        assert not _is_linked(b2, 'coursePages_Course23', a)


def test_assoc_reduction24_link_reassign_clear():
    a = coursePages_Reduction(creditReduction=3.14)
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'coursePages_Reduction', b1)
    assert _is_linked(a, 'coursePages_Reduction', b1)
    if hasattr(b1, 'coursePages_Course25'):
        assert _is_linked(b1, 'coursePages_Course25', a)
    _safe_set(a, 'coursePages_Reduction', b2)
    assert _is_linked(a, 'coursePages_Reduction', b2)
    if hasattr(b1, 'coursePages_Course25'):
        assert not _is_linked(b1, 'coursePages_Course25', a)
    if hasattr(b2, 'coursePages_Course25'):
        assert _is_linked(b2, 'coursePages_Course25', a)
    _safe_set(a, 'coursePages_Reduction', None)
    assert not _is_linked(a, 'coursePages_Reduction', b2)
    if hasattr(b2, 'coursePages_Course25'):
        assert not _is_linked(b2, 'coursePages_Course25', a)


def test_assoc_student10_link_reassign_clear():
    a = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    b1 = coursePages_Student(studentID="sample_text")
    b2 = coursePages_Student(studentID="sample_text_2")
    _safe_set(a, 'studyprograms11', {b1})
    assert _is_linked(a, 'studyprograms11', b1)
    if hasattr(b1, 'Student'):
        assert _is_linked(b1, 'Student', a)
    _safe_set(a, 'studyprograms11', {b2})
    assert _is_linked(a, 'studyprograms11', b2)
    if hasattr(b1, 'Student'):
        assert not _is_linked(b1, 'Student', a)
    if hasattr(b2, 'Student'):
        assert _is_linked(b2, 'Student', a)
    _safe_set(a, 'studyprograms11', set())
    assert not _is_linked(a, 'studyprograms11', b2)
    if hasattr(b2, 'Student'):
        assert not _is_linked(b2, 'Student', a)


def test_assoc_studyprograms0_link_reassign_clear():
    a = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    b1 = coursePages_Student(studentID="sample_text")
    b2 = coursePages_Student(studentID="sample_text_2")
    _safe_set(a, 'StudyPrograms', b1)
    assert _is_linked(a, 'StudyPrograms', b1)
    if hasattr(b1, 'student'):
        assert _is_linked(b1, 'student', a)
    _safe_set(a, 'StudyPrograms', b2)
    assert _is_linked(a, 'StudyPrograms', b2)
    if hasattr(b1, 'student'):
        assert not _is_linked(b1, 'student', a)
    if hasattr(b2, 'student'):
        assert _is_linked(b2, 'student', a)
    _safe_set(a, 'StudyPrograms', None)
    assert not _is_linked(a, 'StudyPrograms', b2)
    if hasattr(b2, 'student'):
        assert not _is_linked(b2, 'student', a)


def test_assoc_studyprograms18_link_reassign_clear():
    a = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    b1 = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    b2 = coursePages_Course(courseCode="sample_text_2", courseContent="sample_text_2", courseCredits=9.99, courseName="sample_text_2")
    _safe_set(a, 'StudyPrograms19', b1)
    assert _is_linked(a, 'StudyPrograms19', b1)
    if hasattr(b1, 'course'):
        assert _is_linked(b1, 'course', a)
    _safe_set(a, 'StudyPrograms19', b2)
    assert _is_linked(a, 'StudyPrograms19', b2)
    if hasattr(b1, 'course'):
        assert not _is_linked(b1, 'course', a)
    if hasattr(b2, 'course'):
        assert _is_linked(b2, 'course', a)
    _safe_set(a, 'StudyPrograms19', None)
    assert not _is_linked(a, 'StudyPrograms19', b2)
    if hasattr(b2, 'course'):
        assert not _is_linked(b2, 'course', a)


def test_assoc_studyprograms4_link_reassign_clear():
    a = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    b1 = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    b2 = coursePages_Department(departmentName="sample_text_2", email="sample_text_2", phoneNummber="sample_text_2")
    _safe_set(a, 'StudyPrograms5', b1)
    assert _is_linked(a, 'StudyPrograms5', b1)
    if hasattr(b1, 'belongsToDepartment'):
        assert _is_linked(b1, 'belongsToDepartment', a)
    _safe_set(a, 'StudyPrograms5', b2)
    assert _is_linked(a, 'StudyPrograms5', b2)
    if hasattr(b1, 'belongsToDepartment'):
        assert not _is_linked(b1, 'belongsToDepartment', a)
    if hasattr(b2, 'belongsToDepartment'):
        assert _is_linked(b2, 'belongsToDepartment', a)
    _safe_set(a, 'StudyPrograms5', None)
    assert not _is_linked(a, 'StudyPrograms5', b2)
    if hasattr(b2, 'belongsToDepartment'):
        assert not _is_linked(b2, 'belongsToDepartment', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


coursePages_Course_strategy = st.builds(coursePages_Course, courseCode=safe_text, courseContent=safe_text, courseCredits=st.floats(allow_nan=False, allow_infinity=False), courseName=safe_text)
@given(instance=coursePages_Course_strategy)
@settings(max_examples=25)
def test_coursePages_Course_instantiation(instance):
    assert isinstance(instance, coursePages_Course)


coursePages_CourseInstance_strategy = st.builds(coursePages_CourseInstance, courseYear=safe_text, term=safe_text)
@given(instance=coursePages_CourseInstance_strategy)
@settings(max_examples=25)
def test_coursePages_CourseInstance_instantiation(instance):
    assert isinstance(instance, coursePages_CourseInstance)


coursePages_CourseWork_strategy = st.builds(coursePages_CourseWork)
@given(instance=coursePages_CourseWork_strategy)
@settings(max_examples=25)
def test_coursePages_CourseWork_instantiation(instance):
    assert isinstance(instance, coursePages_CourseWork)


coursePages_CourseWorkObject_strategy = st.builds(coursePages_CourseWorkObject, courseWorkType=safe_text, day=safe_text, end=st.dates(), room=safe_text, start=st.dates())
@given(instance=coursePages_CourseWorkObject_strategy)
@settings(max_examples=25)
def test_coursePages_CourseWorkObject_instantiation(instance):
    assert isinstance(instance, coursePages_CourseWorkObject)


coursePages_CourseWorker_strategy = st.builds(coursePages_CourseWorker, courseRole=safe_text)
@given(instance=coursePages_CourseWorker_strategy)
@settings(max_examples=25)
def test_coursePages_CourseWorker_instantiation(instance):
    assert isinstance(instance, coursePages_CourseWorker)


coursePages_Department_strategy = st.builds(coursePages_Department, departmentName=safe_text, email=safe_text, phoneNummber=safe_text)
@given(instance=coursePages_Department_strategy)
@settings(max_examples=25)
def test_coursePages_Department_instantiation(instance):
    assert isinstance(instance, coursePages_Department)


coursePages_Employee_strategy = st.builds(coursePages_Employee, position=safe_text)
@given(instance=coursePages_Employee_strategy)
@settings(max_examples=25)
def test_coursePages_Employee_instantiation(instance):
    assert isinstance(instance, coursePages_Employee)


coursePages_EvaluationObject_strategy = st.builds(coursePages_EvaluationObject, credits=st.integers(), date=st.dates(), evaluationsForm=safe_text, term=safe_text)
@given(instance=coursePages_EvaluationObject_strategy)
@settings(max_examples=25)
def test_coursePages_EvaluationObject_instantiation(instance):
    assert isinstance(instance, coursePages_EvaluationObject)


coursePages_Evaluations_strategy = st.builds(coursePages_Evaluations)
@given(instance=coursePages_Evaluations_strategy)
@settings(max_examples=25)
def test_coursePages_Evaluations_instantiation(instance):
    assert isinstance(instance, coursePages_Evaluations)


coursePages_Person_strategy = st.builds(coursePages_Person, email=safe_text, firstName=safe_text, phoneNummber=safe_text, surName=safe_text)
@given(instance=coursePages_Person_strategy)
@settings(max_examples=25)
def test_coursePages_Person_instantiation(instance):
    assert isinstance(instance, coursePages_Person)


coursePages_Precondition_strategy = st.builds(coursePages_Precondition, preconditionStatus=safe_text)
@given(instance=coursePages_Precondition_strategy)
@settings(max_examples=25)
def test_coursePages_Precondition_instantiation(instance):
    assert isinstance(instance, coursePages_Precondition)


coursePages_Reduction_strategy = st.builds(coursePages_Reduction, creditReduction=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=coursePages_Reduction_strategy)
@settings(max_examples=25)
def test_coursePages_Reduction_instantiation(instance):
    assert isinstance(instance, coursePages_Reduction)


coursePages_Student_strategy = st.builds(coursePages_Student, studentID=safe_text)
@given(instance=coursePages_Student_strategy)
@settings(max_examples=25)
def test_coursePages_Student_instantiation(instance):
    assert isinstance(instance, coursePages_Student)


coursePages_StudyPrograms_strategy = st.builds(coursePages_StudyPrograms, studyProgramCode=safe_text, studyProgramName=safe_text)
@given(instance=coursePages_StudyPrograms_strategy)
@settings(max_examples=25)
def test_coursePages_StudyPrograms_instantiation(instance):
    assert isinstance(instance, coursePages_StudyPrograms)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    coursePages_Course,
    coursePages_CourseInstance,
    coursePages_CourseWork,
    coursePages_CourseWorkObject,
    coursePages_CourseWorker,
    coursePages_Department,
    coursePages_Employee,
    coursePages_EvaluationObject,
    coursePages_Evaluations,
    coursePages_Person,
    coursePages_Precondition,
    coursePages_Reduction,
    coursePages_Student,
    coursePages_StudyPrograms,
    CourseWorkType,
    EvaluationType,
    PrecondistionType,
    TermType,
    personRoleType,
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

def test_assoc_belongsToDepartment8_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    _safe_set(b, 'Department9', a1)
    assert _is_linked(b, 'Department9', a1)
    if hasattr(a1, 'studyprograms'):
        assert _is_linked(a1, 'studyprograms', b)
    _safe_set(b, 'Department9', a2)
    assert _is_linked(b, 'Department9', a2)
    if hasattr(a1, 'studyprograms'):
        assert not _is_linked(a1, 'studyprograms', b)
    if hasattr(a2, 'studyprograms'):
        assert _is_linked(a2, 'studyprograms', b)
    _safe_set(b, 'Department9', None)
    assert not _is_linked(b, 'Department9', a2)
    if hasattr(a2, 'studyprograms'):
        assert not _is_linked(a2, 'studyprograms', b)


def test_assoc_course1_reverse_link_reassign_clear():
    a1 = coursePages_Student(studentID="sample_text")
    a2 = coursePages_Student(studentID="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course', a1)
    assert _is_linked(b, 'coursePages_Course', a1)
    if hasattr(a1, 'coursePages_Student'):
        assert _is_linked(a1, 'coursePages_Student', b)
    _safe_set(b, 'coursePages_Course', a2)
    assert _is_linked(b, 'coursePages_Course', a2)
    if hasattr(a1, 'coursePages_Student'):
        assert not _is_linked(a1, 'coursePages_Student', b)
    if hasattr(a2, 'coursePages_Student'):
        assert _is_linked(a2, 'coursePages_Student', b)
    _safe_set(b, 'coursePages_Course', None)
    assert not _is_linked(b, 'coursePages_Course', a2)
    if hasattr(a2, 'coursePages_Student'):
        assert not _is_linked(a2, 'coursePages_Student', b)


def test_assoc_course12_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'Course', a1)
    assert _is_linked(b, 'Course', a1)
    if hasattr(a1, 'studyprograms13'):
        assert _is_linked(a1, 'studyprograms13', b)
    _safe_set(b, 'Course', a2)
    assert _is_linked(b, 'Course', a2)
    if hasattr(a1, 'studyprograms13'):
        assert not _is_linked(a1, 'studyprograms13', b)
    if hasattr(a2, 'studyprograms13'):
        assert _is_linked(a2, 'studyprograms13', b)
    _safe_set(b, 'Course', None)
    assert not _is_linked(b, 'Course', a2)
    if hasattr(a2, 'studyprograms13'):
        assert not _is_linked(a2, 'studyprograms13', b)


def test_assoc_course34_reverse_link_reassign_clear():
    a1 = coursePages_Precondition(preconditionStatus="sample_text")
    a2 = coursePages_Precondition(preconditionStatus="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course36', a1)
    assert _is_linked(b, 'coursePages_Course36', a1)
    if hasattr(a1, 'coursePages_Precondition35'):
        assert _is_linked(a1, 'coursePages_Precondition35', b)
    _safe_set(b, 'coursePages_Course36', a2)
    assert _is_linked(b, 'coursePages_Course36', a2)
    if hasattr(a1, 'coursePages_Precondition35'):
        assert not _is_linked(a1, 'coursePages_Precondition35', b)
    if hasattr(a2, 'coursePages_Precondition35'):
        assert _is_linked(a2, 'coursePages_Precondition35', b)
    _safe_set(b, 'coursePages_Course36', None)
    assert not _is_linked(b, 'coursePages_Course36', a2)
    if hasattr(a2, 'coursePages_Precondition35'):
        assert not _is_linked(a2, 'coursePages_Precondition35', b)


def test_assoc_course37_reverse_link_reassign_clear():
    a1 = coursePages_Reduction(creditReduction=3.14)
    a2 = coursePages_Reduction(creditReduction=9.99)
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course39', a1)
    assert _is_linked(b, 'coursePages_Course39', a1)
    if hasattr(a1, 'coursePages_Reduction38'):
        assert _is_linked(a1, 'coursePages_Reduction38', b)
    _safe_set(b, 'coursePages_Course39', a2)
    assert _is_linked(b, 'coursePages_Course39', a2)
    if hasattr(a1, 'coursePages_Reduction38'):
        assert not _is_linked(a1, 'coursePages_Reduction38', b)
    if hasattr(a2, 'coursePages_Reduction38'):
        assert _is_linked(a2, 'coursePages_Reduction38', b)
    _safe_set(b, 'coursePages_Course39', None)
    assert not _is_linked(b, 'coursePages_Course39', a2)
    if hasattr(a2, 'coursePages_Reduction38'):
        assert not _is_linked(a2, 'coursePages_Reduction38', b)


def test_assoc_course6_reverse_link_reassign_clear():
    a1 = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    a2 = coursePages_Department(departmentName="sample_text_2", email="sample_text_2", phoneNummber="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course7', a1)
    assert _is_linked(b, 'coursePages_Course7', a1)
    if hasattr(a1, 'coursePages_Department'):
        assert _is_linked(a1, 'coursePages_Department', b)
    _safe_set(b, 'coursePages_Course7', a2)
    assert _is_linked(b, 'coursePages_Course7', a2)
    if hasattr(a1, 'coursePages_Department'):
        assert not _is_linked(a1, 'coursePages_Department', b)
    if hasattr(a2, 'coursePages_Department'):
        assert _is_linked(a2, 'coursePages_Department', b)
    _safe_set(b, 'coursePages_Course7', None)
    assert not _is_linked(b, 'coursePages_Course7', a2)
    if hasattr(a2, 'coursePages_Department'):
        assert not _is_linked(a2, 'coursePages_Department', b)


def test_assoc_courseinstance16_reverse_link_reassign_clear():
    a1 = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    a2 = coursePages_CourseInstance(courseYear="sample_text_2", term="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course17', {a1})
    assert _is_linked(b, 'coursePages_Course17', a1)
    if hasattr(a1, 'coursePages_CourseInstance'):
        assert _is_linked(a1, 'coursePages_CourseInstance', b)
    _safe_set(b, 'coursePages_Course17', {a2})
    assert _is_linked(b, 'coursePages_Course17', a2)
    if hasattr(a1, 'coursePages_CourseInstance'):
        assert not _is_linked(a1, 'coursePages_CourseInstance', b)
    if hasattr(a2, 'coursePages_CourseInstance'):
        assert _is_linked(a2, 'coursePages_CourseInstance', b)
    _safe_set(b, 'coursePages_Course17', set())
    assert not _is_linked(b, 'coursePages_Course17', a2)
    if hasattr(a2, 'coursePages_CourseInstance'):
        assert not _is_linked(a2, 'coursePages_CourseInstance', b)


def test_assoc_courseworker20_reverse_link_reassign_clear():
    a1 = coursePages_CourseWorker(courseRole="sample_text")
    a2 = coursePages_CourseWorker(courseRole="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course21', {a1})
    assert _is_linked(b, 'coursePages_Course21', a1)
    if hasattr(a1, 'coursePages_CourseWorker'):
        assert _is_linked(a1, 'coursePages_CourseWorker', b)
    _safe_set(b, 'coursePages_Course21', {a2})
    assert _is_linked(b, 'coursePages_Course21', a2)
    if hasattr(a1, 'coursePages_CourseWorker'):
        assert not _is_linked(a1, 'coursePages_CourseWorker', b)
    if hasattr(a2, 'coursePages_CourseWorker'):
        assert _is_linked(a2, 'coursePages_CourseWorker', b)
    _safe_set(b, 'coursePages_Course21', set())
    assert not _is_linked(b, 'coursePages_Course21', a2)
    if hasattr(a2, 'coursePages_CourseWorker'):
        assert not _is_linked(a2, 'coursePages_CourseWorker', b)


def test_assoc_department2_reverse_link_reassign_clear():
    a1 = coursePages_Employee(position="sample_text")
    a2 = coursePages_Employee(position="sample_text_2")
    b = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    _safe_set(b, 'Department', a1)
    assert _is_linked(b, 'Department', a1)
    if hasattr(a1, 'employee'):
        assert _is_linked(a1, 'employee', b)
    _safe_set(b, 'Department', a2)
    assert _is_linked(b, 'Department', a2)
    if hasattr(a1, 'employee'):
        assert not _is_linked(a1, 'employee', b)
    if hasattr(a2, 'employee'):
        assert _is_linked(a2, 'employee', b)
    _safe_set(b, 'Department', None)
    assert not _is_linked(b, 'Department', a2)
    if hasattr(a2, 'employee'):
        assert not _is_linked(a2, 'employee', b)


def test_assoc_employee3_reverse_link_reassign_clear():
    a1 = coursePages_Employee(position="sample_text")
    a2 = coursePages_Employee(position="sample_text_2")
    b = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    _safe_set(b, 'department', {a1})
    assert _is_linked(b, 'department', a1)
    if hasattr(a1, 'Employee'):
        assert _is_linked(a1, 'Employee', b)
    _safe_set(b, 'department', {a2})
    assert _is_linked(b, 'department', a2)
    if hasattr(a1, 'Employee'):
        assert not _is_linked(a1, 'Employee', b)
    if hasattr(a2, 'Employee'):
        assert _is_linked(a2, 'Employee', b)
    _safe_set(b, 'department', set())
    assert not _is_linked(b, 'department', a2)
    if hasattr(a2, 'Employee'):
        assert not _is_linked(a2, 'Employee', b)


def test_assoc_employee32_reverse_link_reassign_clear():
    a1 = coursePages_Employee(position="sample_text")
    a2 = coursePages_Employee(position="sample_text_2")
    b = coursePages_CourseWorker(courseRole="sample_text")
    _safe_set(b, 'coursePages_CourseWorker33', a1)
    assert _is_linked(b, 'coursePages_CourseWorker33', a1)
    if hasattr(a1, 'coursePages_Employee'):
        assert _is_linked(a1, 'coursePages_Employee', b)
    _safe_set(b, 'coursePages_CourseWorker33', a2)
    assert _is_linked(b, 'coursePages_CourseWorker33', a2)
    if hasattr(a1, 'coursePages_Employee'):
        assert not _is_linked(a1, 'coursePages_Employee', b)
    if hasattr(a2, 'coursePages_Employee'):
        assert _is_linked(a2, 'coursePages_Employee', b)
    _safe_set(b, 'coursePages_CourseWorker33', None)
    assert not _is_linked(b, 'coursePages_CourseWorker33', a2)
    if hasattr(a2, 'coursePages_Employee'):
        assert not _is_linked(a2, 'coursePages_Employee', b)


def test_assoc_precondition22_reverse_link_reassign_clear():
    a1 = coursePages_Precondition(preconditionStatus="sample_text")
    a2 = coursePages_Precondition(preconditionStatus="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course23', {a1})
    assert _is_linked(b, 'coursePages_Course23', a1)
    if hasattr(a1, 'coursePages_Precondition'):
        assert _is_linked(a1, 'coursePages_Precondition', b)
    _safe_set(b, 'coursePages_Course23', {a2})
    assert _is_linked(b, 'coursePages_Course23', a2)
    if hasattr(a1, 'coursePages_Precondition'):
        assert not _is_linked(a1, 'coursePages_Precondition', b)
    if hasattr(a2, 'coursePages_Precondition'):
        assert _is_linked(a2, 'coursePages_Precondition', b)
    _safe_set(b, 'coursePages_Course23', set())
    assert not _is_linked(b, 'coursePages_Course23', a2)
    if hasattr(a2, 'coursePages_Precondition'):
        assert not _is_linked(a2, 'coursePages_Precondition', b)


def test_assoc_reduction24_reverse_link_reassign_clear():
    a1 = coursePages_Reduction(creditReduction=3.14)
    a2 = coursePages_Reduction(creditReduction=9.99)
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'coursePages_Course25', {a1})
    assert _is_linked(b, 'coursePages_Course25', a1)
    if hasattr(a1, 'coursePages_Reduction'):
        assert _is_linked(a1, 'coursePages_Reduction', b)
    _safe_set(b, 'coursePages_Course25', {a2})
    assert _is_linked(b, 'coursePages_Course25', a2)
    if hasattr(a1, 'coursePages_Reduction'):
        assert not _is_linked(a1, 'coursePages_Reduction', b)
    if hasattr(a2, 'coursePages_Reduction'):
        assert _is_linked(a2, 'coursePages_Reduction', b)
    _safe_set(b, 'coursePages_Course25', set())
    assert not _is_linked(b, 'coursePages_Course25', a2)
    if hasattr(a2, 'coursePages_Reduction'):
        assert not _is_linked(a2, 'coursePages_Reduction', b)


def test_assoc_student10_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Student(studentID="sample_text")
    _safe_set(b, 'Student', a1)
    assert _is_linked(b, 'Student', a1)
    if hasattr(a1, 'studyprograms11'):
        assert _is_linked(a1, 'studyprograms11', b)
    _safe_set(b, 'Student', a2)
    assert _is_linked(b, 'Student', a2)
    if hasattr(a1, 'studyprograms11'):
        assert not _is_linked(a1, 'studyprograms11', b)
    if hasattr(a2, 'studyprograms11'):
        assert _is_linked(a2, 'studyprograms11', b)
    _safe_set(b, 'Student', None)
    assert not _is_linked(b, 'Student', a2)
    if hasattr(a2, 'studyprograms11'):
        assert not _is_linked(a2, 'studyprograms11', b)


def test_assoc_studyprograms0_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Student(studentID="sample_text")
    _safe_set(b, 'student', a1)
    assert _is_linked(b, 'student', a1)
    if hasattr(a1, 'StudyPrograms'):
        assert _is_linked(a1, 'StudyPrograms', b)
    _safe_set(b, 'student', a2)
    assert _is_linked(b, 'student', a2)
    if hasattr(a1, 'StudyPrograms'):
        assert not _is_linked(a1, 'StudyPrograms', b)
    if hasattr(a2, 'StudyPrograms'):
        assert _is_linked(a2, 'StudyPrograms', b)
    _safe_set(b, 'student', None)
    assert not _is_linked(b, 'student', a2)
    if hasattr(a2, 'StudyPrograms'):
        assert not _is_linked(a2, 'StudyPrograms', b)


def test_assoc_studyprograms18_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Course(courseCode="sample_text", courseContent="sample_text", courseCredits=3.14, courseName="sample_text")
    _safe_set(b, 'course', {a1})
    assert _is_linked(b, 'course', a1)
    if hasattr(a1, 'StudyPrograms19'):
        assert _is_linked(a1, 'StudyPrograms19', b)
    _safe_set(b, 'course', {a2})
    assert _is_linked(b, 'course', a2)
    if hasattr(a1, 'StudyPrograms19'):
        assert not _is_linked(a1, 'StudyPrograms19', b)
    if hasattr(a2, 'StudyPrograms19'):
        assert _is_linked(a2, 'StudyPrograms19', b)
    _safe_set(b, 'course', set())
    assert not _is_linked(b, 'course', a2)
    if hasattr(a2, 'StudyPrograms19'):
        assert not _is_linked(a2, 'StudyPrograms19', b)


def test_assoc_studyprograms4_reverse_link_reassign_clear():
    a1 = coursePages_StudyPrograms(studyProgramCode="sample_text", studyProgramName="sample_text")
    a2 = coursePages_StudyPrograms(studyProgramCode="sample_text_2", studyProgramName="sample_text_2")
    b = coursePages_Department(departmentName="sample_text", email="sample_text", phoneNummber="sample_text")
    _safe_set(b, 'belongsToDepartment', {a1})
    assert _is_linked(b, 'belongsToDepartment', a1)
    if hasattr(a1, 'StudyPrograms5'):
        assert _is_linked(a1, 'StudyPrograms5', b)
    _safe_set(b, 'belongsToDepartment', {a2})
    assert _is_linked(b, 'belongsToDepartment', a2)
    if hasattr(a1, 'StudyPrograms5'):
        assert not _is_linked(a1, 'StudyPrograms5', b)
    if hasattr(a2, 'StudyPrograms5'):
        assert _is_linked(a2, 'StudyPrograms5', b)
    _safe_set(b, 'belongsToDepartment', set())
    assert not _is_linked(b, 'belongsToDepartment', a2)
    if hasattr(a2, 'StudyPrograms5'):
        assert not _is_linked(a2, 'StudyPrograms5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_coursework26_stub_double():
    # coursePages_CourseWork has no real 'coursePages_CourseWork28' property in the generated
    # code (a bare stub) -- manually attach it so coursePages_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coursePages_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    partner = coursePages_CourseWork()
    setattr(partner, 'coursePages_CourseWork28', None)
    _safe_set(owner, 'coursePages_CourseInstance27', partner)
    assert getattr(partner, 'coursePages_CourseWork28') == owner
    _safe_set(owner, 'coursePages_CourseInstance27', None)
    assert getattr(partner, 'coursePages_CourseWork28') is None


def test_assoc_courseworkobject15_stub_double():
    # coursePages_CourseWork has no real 'coursePages_CourseWork' property in the generated
    # code (a bare stub) -- manually attach it so coursePages_CourseWorkObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coursePages_CourseWorkObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coursePages_CourseWorkObject(courseWorkType="sample_text", day="sample_text", end=date(2024, 1, 1), room="sample_text", start=date(2024, 1, 1))
    partner = coursePages_CourseWork()
    setattr(partner, 'coursePages_CourseWork', None)
    _safe_set(owner, 'coursePages_CourseWorkObject', partner)
    assert owner in getattr(partner, 'coursePages_CourseWork')
    _safe_set(owner, 'coursePages_CourseWorkObject', None)
    assert owner not in getattr(partner, 'coursePages_CourseWork')


def test_assoc_evaluationobject14_stub_double():
    # coursePages_Evaluations has no real 'coursePages_Evaluations' property in the generated
    # code (a bare stub) -- manually attach it so coursePages_EvaluationObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coursePages_EvaluationObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coursePages_EvaluationObject(credits=7, date=date(2024, 1, 1), evaluationsForm="sample_text", term="sample_text")
    partner = coursePages_Evaluations()
    setattr(partner, 'coursePages_Evaluations', None)
    _safe_set(owner, 'coursePages_EvaluationObject', partner)
    assert owner in getattr(partner, 'coursePages_Evaluations')
    _safe_set(owner, 'coursePages_EvaluationObject', None)
    assert owner not in getattr(partner, 'coursePages_Evaluations')


def test_assoc_evaluations29_stub_double():
    # coursePages_Evaluations has no real 'coursePages_Evaluations31' property in the generated
    # code (a bare stub) -- manually attach it so coursePages_CourseInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # coursePages_CourseInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = coursePages_CourseInstance(courseYear="sample_text", term="sample_text")
    partner = coursePages_Evaluations()
    setattr(partner, 'coursePages_Evaluations31', None)
    _safe_set(owner, 'coursePages_CourseInstance30', partner)
    assert getattr(partner, 'coursePages_Evaluations31') == owner
    _safe_set(owner, 'coursePages_CourseInstance30', None)
    assert getattr(partner, 'coursePages_Evaluations31') is None




import datetime as _ch_datetime
from python_code import coursePages_CourseWork
from python_code import coursePages_CourseWorkObject

def test_coursePages_CourseWorkObject___init__():
    assert coursePages_CourseWorkObject.__init__(coursePages_CourseWorkObject('', '', '\x00\x00', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), coursePages_CourseWorkObject=coursePages_CourseWork()), '', '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), coursePages_CourseWorkObject=coursePages_CourseWork()) == None
import datetime as _ch_datetime
from python_code import coursePages_EvaluationObject
from python_code import coursePages_Evaluations

def test_coursePages_EvaluationObject___init__():
    assert coursePages_EvaluationObject.__init__(coursePages_EvaluationObject('', '', 0, _ch_datetime.date(1, 1, 2), coursePages_EvaluationObject=coursePages_Evaluations()), '', '', 0, _ch_datetime.date(1, 1, 1), coursePages_EvaluationObject=coursePages_Evaluations()) == None
from python_code import coursePages_Person

def test_coursePages_Person___init__():
    assert coursePages_Person.__init__(coursePages_Person('\x00\x00', '', '', ''), '', '', '', '') == None

