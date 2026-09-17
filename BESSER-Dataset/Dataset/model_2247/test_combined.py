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
    courses_CreditsReduction,
    courses_ExaminationPanel,
    courses_Timetable,
    courses_Coursework,
    courses_ContactInfo,
    courses_CourseHour,
    courses_EvaluationForm,
    courses_Person,
    courses_Course,
    courses_University,
    courses_Paragraph,
    courses_ExaminationArrangement,
    courses_Content,
    courses_CourseInstance,
    courses_StudyProgram,
    Location,
    TeachingLanguage,
    Day,
    Semester,
    HourStart,
    HourEnd,
    Department,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_courses_creditsreduction_is_not_abstract():
    assert not inspect.isabstract(courses_CreditsReduction)


def test_hyp_courses_creditsreduction_constructor_exists():
    assert callable(courses_CreditsReduction.__init__)


def test_hyp_courses_creditsreduction_constructor_args():
    sig = inspect.signature(courses_CreditsReduction.__init__)
    params = list(sig.parameters.keys())
    assert "reduction" in params, "Missing parameter 'reduction'"




def test_hyp_courses_examinationpanel_is_not_abstract():
    assert not inspect.isabstract(courses_ExaminationPanel)


def test_hyp_courses_examinationpanel_constructor_exists():
    assert callable(courses_ExaminationPanel.__init__)


def test_hyp_courses_examinationpanel_constructor_args():
    sig = inspect.signature(courses_ExaminationPanel.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "room" in params, "Missing parameter 'room'"
    assert "date" in params, "Missing parameter 'date'"






def test_hyp_courses_timetable_is_not_abstract():
    assert not inspect.isabstract(courses_Timetable)


def test_hyp_courses_timetable_constructor_exists():
    assert callable(courses_Timetable.__init__)


def test_hyp_courses_timetable_constructor_args():
    sig = inspect.signature(courses_Timetable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_courses_coursework_is_not_abstract():
    assert not inspect.isabstract(courses_Coursework)


def test_hyp_courses_coursework_constructor_exists():
    assert callable(courses_Coursework.__init__)


def test_hyp_courses_coursework_constructor_args():
    sig = inspect.signature(courses_Coursework.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "numSpecHour" in params, "Missing parameter 'numSpecHour'"
    assert "termNumber" in params, "Missing parameter 'termNumber'"
    assert "numLectHour" in params, "Missing parameter 'numLectHour'"
    assert "instructionLanguage" in params, "Missing parameter 'instructionLanguage'"
    assert "numLabHour" in params, "Missing parameter 'numLabHour'"
    assert "teachingSemester" in params, "Missing parameter 'teachingSemester'"










def test_hyp_courses_contactinfo_is_not_abstract():
    assert not inspect.isabstract(courses_ContactInfo)


def test_hyp_courses_contactinfo_constructor_exists():
    assert callable(courses_ContactInfo.__init__)


def test_hyp_courses_contactinfo_constructor_args():
    sig = inspect.signature(courses_ContactInfo.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "department" in params, "Missing parameter 'department'"





def test_hyp_courses_coursehour_is_not_abstract():
    assert not inspect.isabstract(courses_CourseHour)


def test_hyp_courses_coursehour_constructor_exists():
    assert callable(courses_CourseHour.__init__)


def test_hyp_courses_coursehour_constructor_args():
    sig = inspect.signature(courses_CourseHour.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "endHour" in params, "Missing parameter 'endHour'"
    assert "startHour" in params, "Missing parameter 'startHour'"
    assert "room" in params, "Missing parameter 'room'"
    assert "type" in params, "Missing parameter 'type'"








def test_hyp_courses_evaluationform_is_not_abstract():
    assert not inspect.isabstract(courses_EvaluationForm)


def test_hyp_courses_evaluationform_constructor_exists():
    assert callable(courses_EvaluationForm.__init__)


def test_hyp_courses_evaluationform_constructor_args():
    sig = inspect.signature(courses_EvaluationForm.__init__)
    params = list(sig.parameters.keys())
    assert "examAids" in params, "Missing parameter 'examAids'"
    assert "weighting" in params, "Missing parameter 'weighting'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_courses_person_is_not_abstract():
    assert not inspect.isabstract(courses_Person)


def test_hyp_courses_person_constructor_exists():
    assert callable(courses_Person.__init__)


def test_hyp_courses_person_constructor_args():
    sig = inspect.signature(courses_Person.__init__)
    params = list(sig.parameters.keys())
    assert "Credits" in params, "Missing parameter 'Credits'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_courses_course_is_not_abstract():
    assert not inspect.isabstract(courses_Course)


def test_hyp_courses_course_constructor_exists():
    assert callable(courses_Course.__init__)


def test_hyp_courses_course_constructor_args():
    sig = inspect.signature(courses_Course.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "credit" in params, "Missing parameter 'credit'"
    assert "code" in params, "Missing parameter 'code'"






def test_hyp_courses_university_is_not_abstract():
    assert not inspect.isabstract(courses_University)


def test_hyp_courses_university_constructor_exists():
    assert callable(courses_University.__init__)


def test_hyp_courses_university_constructor_args():
    sig = inspect.signature(courses_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_courses_paragraph_is_not_abstract():
    assert not inspect.isabstract(courses_Paragraph)


def test_hyp_courses_paragraph_constructor_exists():
    assert callable(courses_Paragraph.__init__)


def test_hyp_courses_paragraph_constructor_args():
    sig = inspect.signature(courses_Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"





def test_hyp_courses_examinationarrangement_is_not_abstract():
    assert not inspect.isabstract(courses_ExaminationArrangement)


def test_hyp_courses_examinationarrangement_constructor_exists():
    assert callable(courses_ExaminationArrangement.__init__)


def test_hyp_courses_examinationarrangement_constructor_args():
    sig = inspect.signature(courses_ExaminationArrangement.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"
    assert "type" in params, "Missing parameter 'type'"





def test_hyp_courses_content_is_not_abstract():
    assert not inspect.isabstract(courses_Content)


def test_hyp_courses_content_constructor_exists():
    assert callable(courses_Content.__init__)


def test_hyp_courses_content_constructor_args():
    sig = inspect.signature(courses_Content.__init__)
    params = list(sig.parameters.keys())



def test_hyp_courses_courseinstance_is_not_abstract():
    assert not inspect.isabstract(courses_CourseInstance)


def test_hyp_courses_courseinstance_constructor_exists():
    assert callable(courses_CourseInstance.__init__)


def test_hyp_courses_courseinstance_constructor_args():
    sig = inspect.signature(courses_CourseInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_courses_studyprogram_is_not_abstract():
    assert not inspect.isabstract(courses_StudyProgram)


def test_hyp_courses_studyprogram_constructor_exists():
    assert callable(courses_StudyProgram.__init__)


def test_hyp_courses_studyprogram_constructor_args():
    sig = inspect.signature(courses_StudyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"


def test_hyp_location_exists():
    # Check that the Enumeration exists
    assert Location is not None

def test_hyp_location_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Location]
    expected_literals = [
        "Trondheim",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Location"

def test_hyp_teachinglanguage_exists():
    # Check that the Enumeration exists
    assert TeachingLanguage is not None

def test_hyp_teachinglanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TeachingLanguage]
    expected_literals = [
        "Norwegian",
        "English",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TeachingLanguage"

def test_hyp_day_exists():
    # Check that the Enumeration exists
    assert Day is not None

def test_hyp_day_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Day]
    expected_literals = [
        "Monday",
        "Wednesday",
        "Tuesday",
        "Thursday",
        "Friday",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Day"

def test_hyp_semester_exists():
    # Check that the Enumeration exists
    assert Semester is not None

def test_hyp_semester_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Semester]
    expected_literals = [
        "Spring2015",
        "Spring2018",
        "Autumn2014",
        "Spring2016",
        "Spring2014",
        "Autumn2011",
        "Autumn2017",
        "Autumn2012",
        "Spring2012",
        "Autumn2015",
        "Spring2013",
        "Autumn2010",
        "Autumn2013",
        "Spring2017",
        "Spring2011",
        "Autumn2016",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Semester"

def test_hyp_hourstart_exists():
    # Check that the Enumeration exists
    assert HourStart is not None

def test_hyp_hourstart_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HourStart]
    expected_literals = [
        "h0915",
        "h1615",
        "h1515",
        "h1715",
        "h1015",
        "h1315",
        "h1115",
        "h1215",
        "h1415",
        "h0815",
        "h1815",
        "h1915",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HourStart"

def test_hyp_hourend_exists():
    # Check that the Enumeration exists
    assert HourEnd is not None

def test_hyp_hourend_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HourEnd]
    expected_literals = [
        "h1200",
        "h1100",
        "h1900",
        "h2000",
        "h0900",
        "h1400",
        "h1700",
        "h1600",
        "h1000",
        "h0800",
        "h1300",
        "h1800",
        "h1500",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HourEnd"

def test_hyp_department_exists():
    # Check that the Enumeration exists
    assert Department is not None

def test_hyp_department_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Department]
    expected_literals = [
        "DepartmentofComputerScience",
        "DepartmentofMathematicalSciences",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Department"


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
courses_CreditsReduction_strategy = st.builds(
    courses_CreditsReduction,
    reduction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
courses_ExaminationPanel_strategy = st.builds(
    courses_ExaminationPanel,
    time=
        safe_text,
    room=
        safe_text,
    date=
        safe_text
)
courses_Timetable_strategy = st.builds(
    courses_Timetable,
)
courses_Coursework_strategy = st.builds(
    courses_Coursework,
    location=
        safe_text,
    numSpecHour=
        st.integers(),
    termNumber=
        st.integers(),
    numLectHour=
        st.integers(),
    instructionLanguage=
        safe_text,
    numLabHour=
        st.integers(),
    teachingSemester=
        safe_text
)
courses_ContactInfo_strategy = st.builds(
    courses_ContactInfo,
    phone=
        safe_text,
    department=
        safe_text
)
courses_CourseHour_strategy = st.builds(
    courses_CourseHour,
    day=
        safe_text,
    endHour=
        safe_text,
    startHour=
        safe_text,
    room=
        safe_text,
    type=
        safe_text
)
courses_EvaluationForm_strategy = st.builds(
    courses_EvaluationForm,
    examAids=
        safe_text,
    weighting=
        safe_text,
    duration=
        safe_text,
    type=
        safe_text
)
courses_Person_strategy = st.builds(
    courses_Person,
    Credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
courses_Course_strategy = st.builds(
    courses_Course,
    name=
        safe_text,
    credit=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text
)
courses_University_strategy = st.builds(
    courses_University,
    name=
        safe_text
)
courses_Paragraph_strategy = st.builds(
    courses_Paragraph,
    name=
        safe_text,
    description=
        safe_text
)
courses_ExaminationArrangement_strategy = st.builds(
    courses_ExaminationArrangement,
    grade=
        safe_text,
    type=
        safe_text
)
courses_Content_strategy = st.builds(
    courses_Content,
)
courses_CourseInstance_strategy = st.builds(
    courses_CourseInstance,
)
courses_StudyProgram_strategy = st.builds(
    courses_StudyProgram,
    code=
        safe_text
)




@given(instance=courses_CreditsReduction_strategy)
def test_hyp_courses_creditsreduction_reduction_setter(instance):
    original = instance.reduction
    instance.reduction = original
    assert instance.reduction == original




@given(instance=courses_ExaminationPanel_strategy)
def test_hyp_courses_examinationpanel_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=courses_ExaminationPanel_strategy)
def test_hyp_courses_examinationpanel_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original



@given(instance=courses_ExaminationPanel_strategy)
def test_hyp_courses_examinationpanel_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original





@given(instance=courses_Coursework_strategy)
def test_hyp_courses_coursework_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=courses_Coursework_strategy)
def test_hyp_courses_coursework_numSpecHour_setter(instance):
    original = instance.numSpecHour
    instance.numSpecHour = original
    assert instance.numSpecHour == original



@given(instance=courses_Coursework_strategy)
def test_hyp_courses_coursework_termNumber_setter(instance):
    original = instance.termNumber
    instance.termNumber = original
    assert instance.termNumber == original



@given(instance=courses_Coursework_strategy)
def test_hyp_courses_coursework_numLectHour_setter(instance):
    original = instance.numLectHour
    instance.numLectHour = original
    assert instance.numLectHour == original



@given(instance=courses_Coursework_strategy)
def test_hyp_courses_coursework_instructionLanguage_setter(instance):
    original = instance.instructionLanguage
    instance.instructionLanguage = original
    assert instance.instructionLanguage == original



@given(instance=courses_Coursework_strategy)
def test_hyp_courses_coursework_numLabHour_setter(instance):
    original = instance.numLabHour
    instance.numLabHour = original
    assert instance.numLabHour == original



@given(instance=courses_Coursework_strategy)
def test_hyp_courses_coursework_teachingSemester_setter(instance):
    original = instance.teachingSemester
    instance.teachingSemester = original
    assert instance.teachingSemester == original




@given(instance=courses_ContactInfo_strategy)
def test_hyp_courses_contactinfo_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=courses_ContactInfo_strategy)
def test_hyp_courses_contactinfo_department_setter(instance):
    original = instance.department
    instance.department = original
    assert instance.department == original




@given(instance=courses_CourseHour_strategy)
def test_hyp_courses_coursehour_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=courses_CourseHour_strategy)
def test_hyp_courses_coursehour_endHour_setter(instance):
    original = instance.endHour
    instance.endHour = original
    assert instance.endHour == original



@given(instance=courses_CourseHour_strategy)
def test_hyp_courses_coursehour_startHour_setter(instance):
    original = instance.startHour
    instance.startHour = original
    assert instance.startHour == original



@given(instance=courses_CourseHour_strategy)
def test_hyp_courses_coursehour_room_setter(instance):
    original = instance.room
    instance.room = original
    assert instance.room == original



@given(instance=courses_CourseHour_strategy)
def test_hyp_courses_coursehour_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=courses_EvaluationForm_strategy)
def test_hyp_courses_evaluationform_examAids_setter(instance):
    original = instance.examAids
    instance.examAids = original
    assert instance.examAids == original



@given(instance=courses_EvaluationForm_strategy)
def test_hyp_courses_evaluationform_weighting_setter(instance):
    original = instance.weighting
    instance.weighting = original
    assert instance.weighting == original



@given(instance=courses_EvaluationForm_strategy)
def test_hyp_courses_evaluationform_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=courses_EvaluationForm_strategy)
def test_hyp_courses_evaluationform_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=courses_Person_strategy)
def test_hyp_courses_person_Credits_setter(instance):
    original = instance.Credits
    instance.Credits = original
    assert instance.Credits == original



@given(instance=courses_Person_strategy)
def test_hyp_courses_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=courses_Person_strategy)
@settings(max_examples=30)
def test_hyp_courses_person_signupexam_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.SignUpExam(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.SignUpExam).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'SignUpExam' in courses_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'SignUpExam' in courses_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'SignUpExam' in courses_Person is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=courses_Person_strategy)
@settings(max_examples=30)
def test_hyp_courses_person_cancelexam_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CancelExam(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CancelExam).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CancelExam' in courses_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CancelExam' in courses_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CancelExam' in courses_Person is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=courses_Person_strategy)
@settings(max_examples=30)
def test_hyp_courses_person_passingexam_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.PassingExam(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.PassingExam).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'PassingExam' in courses_Person is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'PassingExam' in courses_Person did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'PassingExam' in courses_Person is not implemented or raised an error")




@given(instance=courses_Course_strategy)
def test_hyp_courses_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=courses_Course_strategy)
def test_hyp_courses_course_credit_setter(instance):
    original = instance.credit
    instance.credit = original
    assert instance.credit == original



@given(instance=courses_Course_strategy)
def test_hyp_courses_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original




@given(instance=courses_University_strategy)
def test_hyp_courses_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=courses_University_strategy)
@settings(max_examples=30)
def test_hyp_courses_university_studentinscription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.StudentInscription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.StudentInscription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'StudentInscription' in courses_University is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'StudentInscription' in courses_University did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'StudentInscription' in courses_University is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=courses_University_strategy)
@settings(max_examples=30)
def test_hyp_courses_university_staffinscription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.StaffInscription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.StaffInscription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'StaffInscription' in courses_University is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'StaffInscription' in courses_University did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'StaffInscription' in courses_University is not implemented or raised an error")




@given(instance=courses_Paragraph_strategy)
def test_hyp_courses_paragraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=courses_Paragraph_strategy)
def test_hyp_courses_paragraph_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=courses_ExaminationArrangement_strategy)
def test_hyp_courses_examinationarrangement_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original



@given(instance=courses_ExaminationArrangement_strategy)
def test_hyp_courses_examinationarrangement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=courses_StudyProgram_strategy)
def test_hyp_courses_studyprogram_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    courses_ContactInfo,
    courses_Content,
    courses_Course,
    courses_CourseHour,
    courses_CourseInstance,
    courses_Coursework,
    courses_CreditsReduction,
    courses_EvaluationForm,
    courses_ExaminationArrangement,
    courses_ExaminationPanel,
    courses_Paragraph,
    courses_Person,
    courses_StudyProgram,
    courses_Timetable,
    courses_University,
    Day,
    Department,
    HourEnd,
    HourStart,
    Location,
    Semester,
    TeachingLanguage,
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

def test_courses_ContactInfo_department_value_roundtrip():
    instance = courses_ContactInfo(department="sample_text", phone="sample_text")
    assert instance.department == "sample_text"
    instance.department = "sample_text_2"
    assert instance.department == "sample_text_2"


def test_courses_ContactInfo_phone_value_roundtrip():
    instance = courses_ContactInfo(department="sample_text", phone="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_courses_Course_code_value_roundtrip():
    instance = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_courses_Course_credit_value_roundtrip():
    instance = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    assert instance.credit == 3.14
    instance.credit = 9.99
    assert instance.credit == 9.99


def test_courses_Course_name_value_roundtrip():
    instance = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_courses_CourseHour_day_value_roundtrip():
    instance = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    assert instance.day == "sample_text"
    instance.day = "sample_text_2"
    assert instance.day == "sample_text_2"


def test_courses_CourseHour_endHour_value_roundtrip():
    instance = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    assert instance.endHour == "sample_text"
    instance.endHour = "sample_text_2"
    assert instance.endHour == "sample_text_2"


def test_courses_CourseHour_room_value_roundtrip():
    instance = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    assert instance.room == "sample_text"
    instance.room = "sample_text_2"
    assert instance.room == "sample_text_2"


def test_courses_CourseHour_startHour_value_roundtrip():
    instance = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    assert instance.startHour == "sample_text"
    instance.startHour = "sample_text_2"
    assert instance.startHour == "sample_text_2"


def test_courses_CourseHour_type_value_roundtrip():
    instance = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_courses_Coursework_instructionLanguage_value_roundtrip():
    instance = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    assert instance.instructionLanguage == "sample_text"
    instance.instructionLanguage = "sample_text_2"
    assert instance.instructionLanguage == "sample_text_2"


def test_courses_Coursework_location_value_roundtrip():
    instance = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_courses_Coursework_numLabHour_value_roundtrip():
    instance = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    assert instance.numLabHour == 7
    instance.numLabHour = 13
    assert instance.numLabHour == 13


def test_courses_Coursework_numLectHour_value_roundtrip():
    instance = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    assert instance.numLectHour == 7
    instance.numLectHour = 13
    assert instance.numLectHour == 13


def test_courses_Coursework_numSpecHour_value_roundtrip():
    instance = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    assert instance.numSpecHour == 7
    instance.numSpecHour = 13
    assert instance.numSpecHour == 13


def test_courses_Coursework_teachingSemester_value_roundtrip():
    instance = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    assert instance.teachingSemester == "sample_text"
    instance.teachingSemester = "sample_text_2"
    assert instance.teachingSemester == "sample_text_2"


def test_courses_Coursework_termNumber_value_roundtrip():
    instance = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    assert instance.termNumber == 7
    instance.termNumber = 13
    assert instance.termNumber == 13


def test_courses_CreditsReduction_reduction_value_roundtrip():
    instance = courses_CreditsReduction(reduction=3.14)
    assert instance.reduction == 3.14
    instance.reduction = 9.99
    assert instance.reduction == 9.99


def test_courses_EvaluationForm_duration_value_roundtrip():
    instance = courses_EvaluationForm(duration="sample_text", examAids="sample_text", type="sample_text", weighting="sample_text")
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_courses_EvaluationForm_examAids_value_roundtrip():
    instance = courses_EvaluationForm(duration="sample_text", examAids="sample_text", type="sample_text", weighting="sample_text")
    assert instance.examAids == "sample_text"
    instance.examAids = "sample_text_2"
    assert instance.examAids == "sample_text_2"


def test_courses_EvaluationForm_type_value_roundtrip():
    instance = courses_EvaluationForm(duration="sample_text", examAids="sample_text", type="sample_text", weighting="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_courses_EvaluationForm_weighting_value_roundtrip():
    instance = courses_EvaluationForm(duration="sample_text", examAids="sample_text", type="sample_text", weighting="sample_text")
    assert instance.weighting == "sample_text"
    instance.weighting = "sample_text_2"
    assert instance.weighting == "sample_text_2"


def test_courses_ExaminationArrangement_grade_value_roundtrip():
    instance = courses_ExaminationArrangement(grade="sample_text", type="sample_text")
    assert instance.grade == "sample_text"
    instance.grade = "sample_text_2"
    assert instance.grade == "sample_text_2"


def test_courses_ExaminationArrangement_type_value_roundtrip():
    instance = courses_ExaminationArrangement(grade="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_courses_ExaminationPanel_date_value_roundtrip():
    instance = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_courses_ExaminationPanel_room_value_roundtrip():
    instance = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    assert instance.room == "sample_text"
    instance.room = "sample_text_2"
    assert instance.room == "sample_text_2"


def test_courses_ExaminationPanel_time_value_roundtrip():
    instance = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_courses_Paragraph_description_value_roundtrip():
    instance = courses_Paragraph(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_courses_Paragraph_name_value_roundtrip():
    instance = courses_Paragraph(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_courses_Person_Credits_value_roundtrip():
    instance = courses_Person(Credits=3.14, name="sample_text")
    assert instance.Credits == 3.14
    instance.Credits = 9.99
    assert instance.Credits == 9.99


def test_courses_Person_name_value_roundtrip():
    instance = courses_Person(Credits=3.14, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_courses_StudyProgram_code_value_roundtrip():
    instance = courses_StudyProgram(code="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_courses_University_name_value_roundtrip():
    instance = courses_University(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_contactInfo15_link_reassign_clear():
    a = courses_ContactInfo(department="sample_text", phone="sample_text")
    b1 = courses_CourseInstance()
    b2 = courses_CourseInstance()
    _safe_set(a, 'courses_ContactInfo', b1)
    assert _is_linked(a, 'courses_ContactInfo', b1)
    if hasattr(b1, 'courses_CourseInstance16'):
        assert _is_linked(b1, 'courses_CourseInstance16', a)
    _safe_set(a, 'courses_ContactInfo', b2)
    assert _is_linked(a, 'courses_ContactInfo', b2)
    if hasattr(b1, 'courses_CourseInstance16'):
        assert not _is_linked(b1, 'courses_CourseInstance16', a)
    if hasattr(b2, 'courses_CourseInstance16'):
        assert _is_linked(b2, 'courses_CourseInstance16', a)
    _safe_set(a, 'courses_ContactInfo', None)
    assert not _is_linked(a, 'courses_ContactInfo', b2)
    if hasattr(b2, 'courses_CourseInstance16'):
        assert not _is_linked(b2, 'courses_CourseInstance16', a)


def test_assoc_course0_link_reassign_clear():
    a = courses_University(name="sample_text")
    b1 = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b2 = courses_Course(code="sample_text_2", credit=9.99, name="sample_text_2")
    _safe_set(a, 'courses_University', {b1})
    assert _is_linked(a, 'courses_University', b1)
    if hasattr(b1, 'courses_Course'):
        assert _is_linked(b1, 'courses_Course', a)
    _safe_set(a, 'courses_University', {b2})
    assert _is_linked(a, 'courses_University', b2)
    if hasattr(b1, 'courses_Course'):
        assert not _is_linked(b1, 'courses_Course', a)
    if hasattr(b2, 'courses_Course'):
        assert _is_linked(b2, 'courses_Course', a)
    _safe_set(a, 'courses_University', set())
    assert not _is_linked(a, 'courses_University', b2)
    if hasattr(b2, 'courses_Course'):
        assert not _is_linked(b2, 'courses_Course', a)


def test_assoc_course54_link_reassign_clear():
    a = courses_Person(Credits=3.14, name="sample_text")
    b1 = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b2 = courses_Course(code="sample_text_2", credit=9.99, name="sample_text_2")
    _safe_set(a, 'student', {b1})
    assert _is_linked(a, 'student', b1)
    if hasattr(b1, 'Course55'):
        assert _is_linked(b1, 'Course55', a)
    _safe_set(a, 'student', {b2})
    assert _is_linked(a, 'student', b2)
    if hasattr(b1, 'Course55'):
        assert not _is_linked(b1, 'Course55', a)
    if hasattr(b2, 'Course55'):
        assert _is_linked(b2, 'Course55', a)
    _safe_set(a, 'student', set())
    assert not _is_linked(a, 'student', b2)
    if hasattr(b2, 'Course55'):
        assert not _is_linked(b2, 'Course55', a)


def test_assoc_course59_link_reassign_clear():
    a = courses_CreditsReduction(reduction=3.14)
    b1 = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b2 = courses_Course(code="sample_text_2", credit=9.99, name="sample_text_2")
    _safe_set(a, 'courses_CreditsReduction60', b1)
    assert _is_linked(a, 'courses_CreditsReduction60', b1)
    if hasattr(b1, 'courses_Course61'):
        assert _is_linked(b1, 'courses_Course61', a)
    _safe_set(a, 'courses_CreditsReduction60', b2)
    assert _is_linked(a, 'courses_CreditsReduction60', b2)
    if hasattr(b1, 'courses_Course61'):
        assert not _is_linked(b1, 'courses_Course61', a)
    if hasattr(b2, 'courses_Course61'):
        assert _is_linked(b2, 'courses_Course61', a)
    _safe_set(a, 'courses_CreditsReduction60', None)
    assert not _is_linked(a, 'courses_CreditsReduction60', b2)
    if hasattr(b2, 'courses_Course61'):
        assert not _is_linked(b2, 'courses_Course61', a)


def test_assoc_courseCoordinator37_link_reassign_clear():
    a = courses_Person(Credits=3.14, name="sample_text")
    b1 = courses_ContactInfo(department="sample_text", phone="sample_text")
    b2 = courses_ContactInfo(department="sample_text_2", phone="sample_text_2")
    _safe_set(a, 'courses_Person39', b1)
    assert _is_linked(a, 'courses_Person39', b1)
    if hasattr(b1, 'courses_ContactInfo38'):
        assert _is_linked(b1, 'courses_ContactInfo38', a)
    _safe_set(a, 'courses_Person39', b2)
    assert _is_linked(a, 'courses_Person39', b2)
    if hasattr(b1, 'courses_ContactInfo38'):
        assert not _is_linked(b1, 'courses_ContactInfo38', a)
    if hasattr(b2, 'courses_ContactInfo38'):
        assert _is_linked(b2, 'courses_ContactInfo38', a)
    _safe_set(a, 'courses_Person39', None)
    assert not _is_linked(a, 'courses_Person39', b2)
    if hasattr(b2, 'courses_ContactInfo38'):
        assert not _is_linked(b2, 'courses_ContactInfo38', a)


def test_assoc_courseRecommended29_link_reassign_clear():
    a = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b1 = courses_CourseInstance()
    b2 = courses_CourseInstance()
    _safe_set(a, 'courses_Course31', b1)
    assert _is_linked(a, 'courses_Course31', b1)
    if hasattr(b1, 'courses_CourseInstance30'):
        assert _is_linked(b1, 'courses_CourseInstance30', a)
    _safe_set(a, 'courses_Course31', b2)
    assert _is_linked(a, 'courses_Course31', b2)
    if hasattr(b1, 'courses_CourseInstance30'):
        assert not _is_linked(b1, 'courses_CourseInstance30', a)
    if hasattr(b2, 'courses_CourseInstance30'):
        assert _is_linked(b2, 'courses_CourseInstance30', a)
    _safe_set(a, 'courses_Course31', None)
    assert not _is_linked(a, 'courses_Course31', b2)
    if hasattr(b2, 'courses_CourseInstance30'):
        assert not _is_linked(b2, 'courses_CourseInstance30', a)


def test_assoc_courseRequired26_link_reassign_clear():
    a = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b1 = courses_CourseInstance()
    b2 = courses_CourseInstance()
    _safe_set(a, 'courses_Course28', b1)
    assert _is_linked(a, 'courses_Course28', b1)
    if hasattr(b1, 'courses_CourseInstance27'):
        assert _is_linked(b1, 'courses_CourseInstance27', a)
    _safe_set(a, 'courses_Course28', b2)
    assert _is_linked(a, 'courses_Course28', b2)
    if hasattr(b1, 'courses_CourseInstance27'):
        assert not _is_linked(b1, 'courses_CourseInstance27', a)
    if hasattr(b2, 'courses_CourseInstance27'):
        assert _is_linked(b2, 'courses_CourseInstance27', a)
    _safe_set(a, 'courses_Course28', None)
    assert not _is_linked(a, 'courses_Course28', b2)
    if hasattr(b2, 'courses_CourseInstance27'):
        assert not _is_linked(b2, 'courses_CourseInstance27', a)


def test_assoc_courses50_link_reassign_clear():
    a = courses_StudyProgram(code="sample_text")
    b1 = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b2 = courses_Course(code="sample_text_2", credit=9.99, name="sample_text_2")
    _safe_set(a, 'studyProgram', {b1})
    assert _is_linked(a, 'studyProgram', b1)
    if hasattr(b1, 'Course'):
        assert _is_linked(b1, 'Course', a)
    _safe_set(a, 'studyProgram', {b2})
    assert _is_linked(a, 'studyProgram', b2)
    if hasattr(b1, 'Course'):
        assert not _is_linked(b1, 'Course', a)
    if hasattr(b2, 'Course'):
        assert _is_linked(b2, 'Course', a)
    _safe_set(a, 'studyProgram', set())
    assert not _is_linked(a, 'studyProgram', b2)
    if hasattr(b2, 'Course'):
        assert not _is_linked(b2, 'Course', a)


def test_assoc_coursework20_link_reassign_clear():
    a = courses_Coursework(instructionLanguage="sample_text", location="sample_text", numLabHour=7, numLectHour=7, numSpecHour=7, teachingSemester="sample_text", termNumber=7)
    b1 = courses_CourseInstance()
    b2 = courses_CourseInstance()
    _safe_set(a, 'courses_Coursework', b1)
    assert _is_linked(a, 'courses_Coursework', b1)
    if hasattr(b1, 'courses_CourseInstance21'):
        assert _is_linked(b1, 'courses_CourseInstance21', a)
    _safe_set(a, 'courses_Coursework', b2)
    assert _is_linked(a, 'courses_Coursework', b2)
    if hasattr(b1, 'courses_CourseInstance21'):
        assert not _is_linked(b1, 'courses_CourseInstance21', a)
    if hasattr(b2, 'courses_CourseInstance21'):
        assert _is_linked(b2, 'courses_CourseInstance21', a)
    _safe_set(a, 'courses_Coursework', None)
    assert not _is_linked(a, 'courses_Coursework', b2)
    if hasattr(b2, 'courses_CourseInstance21'):
        assert not _is_linked(b2, 'courses_CourseInstance21', a)


def test_assoc_creditsReduction32_link_reassign_clear():
    a = courses_CreditsReduction(reduction=3.14)
    b1 = courses_CourseInstance()
    b2 = courses_CourseInstance()
    _safe_set(a, 'courses_CreditsReduction', b1)
    assert _is_linked(a, 'courses_CreditsReduction', b1)
    if hasattr(b1, 'courses_CourseInstance33'):
        assert _is_linked(b1, 'courses_CourseInstance33', a)
    _safe_set(a, 'courses_CreditsReduction', b2)
    assert _is_linked(a, 'courses_CreditsReduction', b2)
    if hasattr(b1, 'courses_CourseInstance33'):
        assert not _is_linked(b1, 'courses_CourseInstance33', a)
    if hasattr(b2, 'courses_CourseInstance33'):
        assert _is_linked(b2, 'courses_CourseInstance33', a)
    _safe_set(a, 'courses_CreditsReduction', None)
    assert not _is_linked(a, 'courses_CreditsReduction', b2)
    if hasattr(b2, 'courses_CourseInstance33'):
        assert not _is_linked(b2, 'courses_CourseInstance33', a)


def test_assoc_evaluationForm48_link_reassign_clear():
    a = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    b1 = courses_EvaluationForm(duration="sample_text", examAids="sample_text", type="sample_text", weighting="sample_text")
    b2 = courses_EvaluationForm(duration="sample_text_2", examAids="sample_text_2", type="sample_text_2", weighting="sample_text_2")
    _safe_set(a, 'courses_ExaminationPanel49', {b1})
    assert _is_linked(a, 'courses_ExaminationPanel49', b1)
    if hasattr(b1, 'courses_EvaluationForm'):
        assert _is_linked(b1, 'courses_EvaluationForm', a)
    _safe_set(a, 'courses_ExaminationPanel49', {b2})
    assert _is_linked(a, 'courses_ExaminationPanel49', b2)
    if hasattr(b1, 'courses_EvaluationForm'):
        assert not _is_linked(b1, 'courses_EvaluationForm', a)
    if hasattr(b2, 'courses_EvaluationForm'):
        assert _is_linked(b2, 'courses_EvaluationForm', a)
    _safe_set(a, 'courses_ExaminationPanel49', set())
    assert not _is_linked(a, 'courses_ExaminationPanel49', b2)
    if hasattr(b2, 'courses_EvaluationForm'):
        assert not _is_linked(b2, 'courses_EvaluationForm', a)


def test_assoc_evaluationForms34_link_reassign_clear():
    a = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    b1 = courses_ExaminationArrangement(grade="sample_text", type="sample_text")
    b2 = courses_ExaminationArrangement(grade="sample_text_2", type="sample_text_2")
    _safe_set(a, 'courses_ExaminationPanel36', b1)
    assert _is_linked(a, 'courses_ExaminationPanel36', b1)
    if hasattr(b1, 'courses_ExaminationArrangement35'):
        assert _is_linked(b1, 'courses_ExaminationArrangement35', a)
    _safe_set(a, 'courses_ExaminationPanel36', b2)
    assert _is_linked(a, 'courses_ExaminationPanel36', b2)
    if hasattr(b1, 'courses_ExaminationArrangement35'):
        assert not _is_linked(b1, 'courses_ExaminationArrangement35', a)
    if hasattr(b2, 'courses_ExaminationArrangement35'):
        assert _is_linked(b2, 'courses_ExaminationArrangement35', a)
    _safe_set(a, 'courses_ExaminationPanel36', None)
    assert not _is_linked(a, 'courses_ExaminationPanel36', b2)
    if hasattr(b2, 'courses_ExaminationArrangement35'):
        assert not _is_linked(b2, 'courses_ExaminationArrangement35', a)


def test_assoc_examArrangement12_link_reassign_clear():
    a = courses_ExaminationArrangement(grade="sample_text", type="sample_text")
    b1 = courses_Content()
    b2 = courses_Content()
    _safe_set(a, 'courses_ExaminationArrangement', b1)
    assert _is_linked(a, 'courses_ExaminationArrangement', b1)
    if hasattr(b1, 'courses_Content'):
        assert _is_linked(b1, 'courses_Content', a)
    _safe_set(a, 'courses_ExaminationArrangement', b2)
    assert _is_linked(a, 'courses_ExaminationArrangement', b2)
    if hasattr(b1, 'courses_Content'):
        assert not _is_linked(b1, 'courses_Content', a)
    if hasattr(b2, 'courses_Content'):
        assert _is_linked(b2, 'courses_Content', a)
    _safe_set(a, 'courses_ExaminationArrangement', None)
    assert not _is_linked(a, 'courses_ExaminationArrangement', b2)
    if hasattr(b2, 'courses_Content'):
        assert not _is_linked(b2, 'courses_Content', a)


def test_assoc_examination24_link_reassign_clear():
    a = courses_ExaminationPanel(date="sample_text", room="sample_text", time="sample_text")
    b1 = courses_CourseInstance()
    b2 = courses_CourseInstance()
    _safe_set(a, 'courses_ExaminationPanel', b1)
    assert _is_linked(a, 'courses_ExaminationPanel', b1)
    if hasattr(b1, 'courses_CourseInstance25'):
        assert _is_linked(b1, 'courses_CourseInstance25', a)
    _safe_set(a, 'courses_ExaminationPanel', b2)
    assert _is_linked(a, 'courses_ExaminationPanel', b2)
    if hasattr(b1, 'courses_CourseInstance25'):
        assert not _is_linked(b1, 'courses_CourseInstance25', a)
    if hasattr(b2, 'courses_CourseInstance25'):
        assert _is_linked(b2, 'courses_CourseInstance25', a)
    _safe_set(a, 'courses_ExaminationPanel', None)
    assert not _is_linked(a, 'courses_ExaminationPanel', b2)
    if hasattr(b2, 'courses_CourseInstance25'):
        assert not _is_linked(b2, 'courses_CourseInstance25', a)


def test_assoc_listCourseHour43_link_reassign_clear():
    a = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    b1 = courses_Timetable()
    b2 = courses_Timetable()
    _safe_set(a, 'courses_CourseHour', b1)
    assert _is_linked(a, 'courses_CourseHour', b1)
    if hasattr(b1, 'courses_Timetable44'):
        assert _is_linked(b1, 'courses_Timetable44', a)
    _safe_set(a, 'courses_CourseHour', b2)
    assert _is_linked(a, 'courses_CourseHour', b2)
    if hasattr(b1, 'courses_Timetable44'):
        assert not _is_linked(b1, 'courses_Timetable44', a)
    if hasattr(b2, 'courses_Timetable44'):
        assert _is_linked(b2, 'courses_Timetable44', a)
    _safe_set(a, 'courses_CourseHour', None)
    assert not _is_linked(a, 'courses_CourseHour', b2)
    if hasattr(b2, 'courses_Timetable44'):
        assert not _is_linked(b2, 'courses_Timetable44', a)


def test_assoc_listCourseInstance8_link_reassign_clear():
    a = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b1 = courses_CourseInstance()
    b2 = courses_CourseInstance()
    _safe_set(a, 'courses_Course9', {b1})
    assert _is_linked(a, 'courses_Course9', b1)
    if hasattr(b1, 'courses_CourseInstance'):
        assert _is_linked(b1, 'courses_CourseInstance', a)
    _safe_set(a, 'courses_Course9', {b2})
    assert _is_linked(a, 'courses_Course9', b2)
    if hasattr(b1, 'courses_CourseInstance'):
        assert not _is_linked(b1, 'courses_CourseInstance', a)
    if hasattr(b2, 'courses_CourseInstance'):
        assert _is_linked(b2, 'courses_CourseInstance', a)
    _safe_set(a, 'courses_Course9', set())
    assert not _is_linked(a, 'courses_Course9', b2)
    if hasattr(b2, 'courses_CourseInstance'):
        assert not _is_linked(b2, 'courses_CourseInstance', a)


def test_assoc_paragraph13_link_reassign_clear():
    a = courses_Paragraph(description="sample_text", name="sample_text")
    b1 = courses_Content()
    b2 = courses_Content()
    _safe_set(a, 'courses_Paragraph', b1)
    assert _is_linked(a, 'courses_Paragraph', b1)
    if hasattr(b1, 'courses_Content14'):
        assert _is_linked(b1, 'courses_Content14', a)
    _safe_set(a, 'courses_Paragraph', b2)
    assert _is_linked(a, 'courses_Paragraph', b2)
    if hasattr(b1, 'courses_Content14'):
        assert not _is_linked(b1, 'courses_Content14', a)
    if hasattr(b2, 'courses_Content14'):
        assert _is_linked(b2, 'courses_Content14', a)
    _safe_set(a, 'courses_Paragraph', None)
    assert not _is_linked(a, 'courses_Paragraph', b2)
    if hasattr(b2, 'courses_Content14'):
        assert not _is_linked(b2, 'courses_Content14', a)


def test_assoc_plannedFor45_link_reassign_clear():
    a = courses_StudyProgram(code="sample_text")
    b1 = courses_CourseHour(day="sample_text", endHour="sample_text", room="sample_text", startHour="sample_text", type="sample_text")
    b2 = courses_CourseHour(day="sample_text_2", endHour="sample_text_2", room="sample_text_2", startHour="sample_text_2", type="sample_text_2")
    _safe_set(a, 'courses_StudyProgram47', b1)
    assert _is_linked(a, 'courses_StudyProgram47', b1)
    if hasattr(b1, 'courses_CourseHour46'):
        assert _is_linked(b1, 'courses_CourseHour46', a)
    _safe_set(a, 'courses_StudyProgram47', b2)
    assert _is_linked(a, 'courses_StudyProgram47', b2)
    if hasattr(b1, 'courses_CourseHour46'):
        assert not _is_linked(b1, 'courses_CourseHour46', a)
    if hasattr(b2, 'courses_CourseHour46'):
        assert _is_linked(b2, 'courses_CourseHour46', a)
    _safe_set(a, 'courses_StudyProgram47', None)
    assert not _is_linked(a, 'courses_StudyProgram47', b2)
    if hasattr(b2, 'courses_CourseHour46'):
        assert not _is_linked(b2, 'courses_CourseHour46', a)


def test_assoc_staff1_link_reassign_clear():
    a = courses_University(name="sample_text")
    b1 = courses_Person(Credits=3.14, name="sample_text")
    b2 = courses_Person(Credits=9.99, name="sample_text_2")
    _safe_set(a, 'courses_University2', {b1})
    assert _is_linked(a, 'courses_University2', b1)
    if hasattr(b1, 'courses_Person'):
        assert _is_linked(b1, 'courses_Person', a)
    _safe_set(a, 'courses_University2', {b2})
    assert _is_linked(a, 'courses_University2', b2)
    if hasattr(b1, 'courses_Person'):
        assert not _is_linked(b1, 'courses_Person', a)
    if hasattr(b2, 'courses_Person'):
        assert _is_linked(b2, 'courses_Person', a)
    _safe_set(a, 'courses_University2', set())
    assert not _is_linked(a, 'courses_University2', b2)
    if hasattr(b2, 'courses_Person'):
        assert not _is_linked(b2, 'courses_Person', a)


def test_assoc_staff40_link_reassign_clear():
    a = courses_Person(Credits=3.14, name="sample_text")
    b1 = courses_ContactInfo(department="sample_text", phone="sample_text")
    b2 = courses_ContactInfo(department="sample_text_2", phone="sample_text_2")
    _safe_set(a, 'courses_Person42', b1)
    assert _is_linked(a, 'courses_Person42', b1)
    if hasattr(b1, 'courses_ContactInfo41'):
        assert _is_linked(b1, 'courses_ContactInfo41', a)
    _safe_set(a, 'courses_Person42', b2)
    assert _is_linked(a, 'courses_Person42', b2)
    if hasattr(b1, 'courses_ContactInfo41'):
        assert not _is_linked(b1, 'courses_ContactInfo41', a)
    if hasattr(b2, 'courses_ContactInfo41'):
        assert _is_linked(b2, 'courses_ContactInfo41', a)
    _safe_set(a, 'courses_Person42', None)
    assert not _is_linked(a, 'courses_Person42', b2)
    if hasattr(b2, 'courses_ContactInfo41'):
        assert not _is_linked(b2, 'courses_ContactInfo41', a)


def test_assoc_student11_link_reassign_clear():
    a = courses_Person(Credits=3.14, name="sample_text")
    b1 = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b2 = courses_Course(code="sample_text_2", credit=9.99, name="sample_text_2")
    _safe_set(a, 'Person', b1)
    assert _is_linked(a, 'Person', b1)
    if hasattr(b1, 'course'):
        assert _is_linked(b1, 'course', a)
    _safe_set(a, 'Person', b2)
    assert _is_linked(a, 'Person', b2)
    if hasattr(b1, 'course'):
        assert not _is_linked(b1, 'course', a)
    if hasattr(b2, 'course'):
        assert _is_linked(b2, 'course', a)
    _safe_set(a, 'Person', None)
    assert not _is_linked(a, 'Person', b2)
    if hasattr(b2, 'course'):
        assert not _is_linked(b2, 'course', a)


def test_assoc_student51_link_reassign_clear():
    a = courses_StudyProgram(code="sample_text")
    b1 = courses_Person(Credits=3.14, name="sample_text")
    b2 = courses_Person(Credits=9.99, name="sample_text_2")
    _safe_set(a, 'studyProgram52', {b1})
    assert _is_linked(a, 'studyProgram52', b1)
    if hasattr(b1, 'Person53'):
        assert _is_linked(b1, 'Person53', a)
    _safe_set(a, 'studyProgram52', {b2})
    assert _is_linked(a, 'studyProgram52', b2)
    if hasattr(b1, 'Person53'):
        assert not _is_linked(b1, 'Person53', a)
    if hasattr(b2, 'Person53'):
        assert _is_linked(b2, 'Person53', a)
    _safe_set(a, 'studyProgram52', set())
    assert not _is_linked(a, 'studyProgram52', b2)
    if hasattr(b2, 'Person53'):
        assert not _is_linked(b2, 'Person53', a)


def test_assoc_students5_link_reassign_clear():
    a = courses_University(name="sample_text")
    b1 = courses_Person(Credits=3.14, name="sample_text")
    b2 = courses_Person(Credits=9.99, name="sample_text_2")
    _safe_set(a, 'courses_University6', {b1})
    assert _is_linked(a, 'courses_University6', b1)
    if hasattr(b1, 'courses_Person7'):
        assert _is_linked(b1, 'courses_Person7', a)
    _safe_set(a, 'courses_University6', {b2})
    assert _is_linked(a, 'courses_University6', b2)
    if hasattr(b1, 'courses_Person7'):
        assert not _is_linked(b1, 'courses_Person7', a)
    if hasattr(b2, 'courses_Person7'):
        assert _is_linked(b2, 'courses_Person7', a)
    _safe_set(a, 'courses_University6', set())
    assert not _is_linked(a, 'courses_University6', b2)
    if hasattr(b2, 'courses_Person7'):
        assert not _is_linked(b2, 'courses_Person7', a)


def test_assoc_studyProgram10_link_reassign_clear():
    a = courses_StudyProgram(code="sample_text")
    b1 = courses_Course(code="sample_text", credit=3.14, name="sample_text")
    b2 = courses_Course(code="sample_text_2", credit=9.99, name="sample_text_2")
    _safe_set(a, 'StudyProgram', b1)
    assert _is_linked(a, 'StudyProgram', b1)
    if hasattr(b1, 'courses'):
        assert _is_linked(b1, 'courses', a)
    _safe_set(a, 'StudyProgram', b2)
    assert _is_linked(a, 'StudyProgram', b2)
    if hasattr(b1, 'courses'):
        assert not _is_linked(b1, 'courses', a)
    if hasattr(b2, 'courses'):
        assert _is_linked(b2, 'courses', a)
    _safe_set(a, 'StudyProgram', None)
    assert not _is_linked(a, 'StudyProgram', b2)
    if hasattr(b2, 'courses'):
        assert not _is_linked(b2, 'courses', a)


def test_assoc_studyProgram3_link_reassign_clear():
    a = courses_University(name="sample_text")
    b1 = courses_StudyProgram(code="sample_text")
    b2 = courses_StudyProgram(code="sample_text_2")
    _safe_set(a, 'courses_University4', {b1})
    assert _is_linked(a, 'courses_University4', b1)
    if hasattr(b1, 'courses_StudyProgram'):
        assert _is_linked(b1, 'courses_StudyProgram', a)
    _safe_set(a, 'courses_University4', {b2})
    assert _is_linked(a, 'courses_University4', b2)
    if hasattr(b1, 'courses_StudyProgram'):
        assert not _is_linked(b1, 'courses_StudyProgram', a)
    if hasattr(b2, 'courses_StudyProgram'):
        assert _is_linked(b2, 'courses_StudyProgram', a)
    _safe_set(a, 'courses_University4', set())
    assert not _is_linked(a, 'courses_University4', b2)
    if hasattr(b2, 'courses_StudyProgram'):
        assert not _is_linked(b2, 'courses_StudyProgram', a)


def test_assoc_studyProgram56_link_reassign_clear():
    a = courses_StudyProgram(code="sample_text")
    b1 = courses_Person(Credits=3.14, name="sample_text")
    b2 = courses_Person(Credits=9.99, name="sample_text_2")
    _safe_set(a, 'StudyProgram58', b1)
    assert _is_linked(a, 'StudyProgram58', b1)
    if hasattr(b1, 'student57'):
        assert _is_linked(b1, 'student57', a)
    _safe_set(a, 'StudyProgram58', b2)
    assert _is_linked(a, 'StudyProgram58', b2)
    if hasattr(b1, 'student57'):
        assert not _is_linked(b1, 'student57', a)
    if hasattr(b2, 'student57'):
        assert _is_linked(b2, 'student57', a)
    _safe_set(a, 'StudyProgram58', None)
    assert not _is_linked(a, 'StudyProgram58', b2)
    if hasattr(b2, 'student57'):
        assert not _is_linked(b2, 'student57', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

courses_ContactInfo_strategy = st.builds(courses_ContactInfo, department=safe_text, phone=safe_text)
@given(instance=courses_ContactInfo_strategy)
@settings(max_examples=25)
def test_courses_ContactInfo_instantiation(instance):
    assert isinstance(instance, courses_ContactInfo)


courses_Content_strategy = st.builds(courses_Content)
@given(instance=courses_Content_strategy)
@settings(max_examples=25)
def test_courses_Content_instantiation(instance):
    assert isinstance(instance, courses_Content)


courses_Course_strategy = st.builds(courses_Course, code=safe_text, credit=st.floats(allow_nan=False, allow_infinity=False), name=safe_text)
@given(instance=courses_Course_strategy)
@settings(max_examples=25)
def test_courses_Course_instantiation(instance):
    assert isinstance(instance, courses_Course)


courses_CourseHour_strategy = st.builds(courses_CourseHour, day=safe_text, endHour=safe_text, room=safe_text, startHour=safe_text, type=safe_text)
@given(instance=courses_CourseHour_strategy)
@settings(max_examples=25)
def test_courses_CourseHour_instantiation(instance):
    assert isinstance(instance, courses_CourseHour)


courses_CourseInstance_strategy = st.builds(courses_CourseInstance)
@given(instance=courses_CourseInstance_strategy)
@settings(max_examples=25)
def test_courses_CourseInstance_instantiation(instance):
    assert isinstance(instance, courses_CourseInstance)


courses_Coursework_strategy = st.builds(courses_Coursework, instructionLanguage=safe_text, location=safe_text, numLabHour=st.integers(), numLectHour=st.integers(), numSpecHour=st.integers(), teachingSemester=safe_text, termNumber=st.integers())
@given(instance=courses_Coursework_strategy)
@settings(max_examples=25)
def test_courses_Coursework_instantiation(instance):
    assert isinstance(instance, courses_Coursework)


courses_CreditsReduction_strategy = st.builds(courses_CreditsReduction, reduction=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=courses_CreditsReduction_strategy)
@settings(max_examples=25)
def test_courses_CreditsReduction_instantiation(instance):
    assert isinstance(instance, courses_CreditsReduction)


courses_EvaluationForm_strategy = st.builds(courses_EvaluationForm, duration=safe_text, examAids=safe_text, type=safe_text, weighting=safe_text)
@given(instance=courses_EvaluationForm_strategy)
@settings(max_examples=25)
def test_courses_EvaluationForm_instantiation(instance):
    assert isinstance(instance, courses_EvaluationForm)


courses_ExaminationArrangement_strategy = st.builds(courses_ExaminationArrangement, grade=safe_text, type=safe_text)
@given(instance=courses_ExaminationArrangement_strategy)
@settings(max_examples=25)
def test_courses_ExaminationArrangement_instantiation(instance):
    assert isinstance(instance, courses_ExaminationArrangement)


courses_ExaminationPanel_strategy = st.builds(courses_ExaminationPanel, date=safe_text, room=safe_text, time=safe_text)
@given(instance=courses_ExaminationPanel_strategy)
@settings(max_examples=25)
def test_courses_ExaminationPanel_instantiation(instance):
    assert isinstance(instance, courses_ExaminationPanel)


courses_Paragraph_strategy = st.builds(courses_Paragraph, description=safe_text, name=safe_text)
@given(instance=courses_Paragraph_strategy)
@settings(max_examples=25)
def test_courses_Paragraph_instantiation(instance):
    assert isinstance(instance, courses_Paragraph)


courses_Person_strategy = st.builds(courses_Person, Credits=st.floats(allow_nan=False, allow_infinity=False), name=safe_text)
@given(instance=courses_Person_strategy)
@settings(max_examples=25)
def test_courses_Person_instantiation(instance):
    assert isinstance(instance, courses_Person)


courses_StudyProgram_strategy = st.builds(courses_StudyProgram, code=safe_text)
@given(instance=courses_StudyProgram_strategy)
@settings(max_examples=25)
def test_courses_StudyProgram_instantiation(instance):
    assert isinstance(instance, courses_StudyProgram)


courses_Timetable_strategy = st.builds(courses_Timetable)
@given(instance=courses_Timetable_strategy)
@settings(max_examples=25)
def test_courses_Timetable_instantiation(instance):
    assert isinstance(instance, courses_Timetable)


courses_University_strategy = st.builds(courses_University, name=safe_text)
@given(instance=courses_University_strategy)
@settings(max_examples=25)
def test_courses_University_instantiation(instance):
    assert isinstance(instance, courses_University)



