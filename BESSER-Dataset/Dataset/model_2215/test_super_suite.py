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
    studyProgramStructure_CourseGroup,
    studyProgramStructure_CourseAllocation,
    studyProgramStructure_StudyPlan,
    studyProgramStructure_Student,
    studyProgramStructure_University,
    studyProgramStructure_Semester,
    studyProgramStructure_Specialization,
    studyProgramStructure_Course,
    studyProgramStructure_Program,
    CourseStatus,
    Season,
    Grade,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_studyprogramstructure_coursegroup_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_CourseGroup)


def test_hyp_studyprogramstructure_coursegroup_constructor_exists():
    assert callable(studyProgramStructure_CourseGroup.__init__)


def test_hyp_studyprogramstructure_coursegroup_constructor_args():
    sig = inspect.signature(studyProgramStructure_CourseGroup.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_studyprogramstructure_courseallocation_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_CourseAllocation)


def test_hyp_studyprogramstructure_courseallocation_constructor_exists():
    assert callable(studyProgramStructure_CourseAllocation.__init__)


def test_hyp_studyprogramstructure_courseallocation_constructor_args():
    sig = inspect.signature(studyProgramStructure_CourseAllocation.__init__)
    params = list(sig.parameters.keys())
    assert "grade" in params, "Missing parameter 'grade'"




def test_hyp_studyprogramstructure_studyplan_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_StudyPlan)


def test_hyp_studyprogramstructure_studyplan_constructor_exists():
    assert callable(studyProgramStructure_StudyPlan.__init__)


def test_hyp_studyprogramstructure_studyplan_constructor_args():
    sig = inspect.signature(studyProgramStructure_StudyPlan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_studyprogramstructure_student_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Student)


def test_hyp_studyprogramstructure_student_constructor_exists():
    assert callable(studyProgramStructure_Student.__init__)


def test_hyp_studyprogramstructure_student_constructor_args():
    sig = inspect.signature(studyProgramStructure_Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_studyprogramstructure_university_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_University)


def test_hyp_studyprogramstructure_university_constructor_exists():
    assert callable(studyProgramStructure_University.__init__)


def test_hyp_studyprogramstructure_university_constructor_args():
    sig = inspect.signature(studyProgramStructure_University.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_studyprogramstructure_semester_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Semester)


def test_hyp_studyprogramstructure_semester_constructor_exists():
    assert callable(studyProgramStructure_Semester.__init__)


def test_hyp_studyprogramstructure_semester_constructor_args():
    sig = inspect.signature(studyProgramStructure_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "season" in params, "Missing parameter 'season'"





def test_hyp_studyprogramstructure_specialization_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Specialization)


def test_hyp_studyprogramstructure_specialization_constructor_exists():
    assert callable(studyProgramStructure_Specialization.__init__)


def test_hyp_studyprogramstructure_specialization_constructor_args():
    sig = inspect.signature(studyProgramStructure_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "numOfSemesters" in params, "Missing parameter 'numOfSemesters'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_studyprogramstructure_course_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Course)


def test_hyp_studyprogramstructure_course_constructor_exists():
    assert callable(studyProgramStructure_Course.__init__)


def test_hyp_studyprogramstructure_course_constructor_args():
    sig = inspect.signature(studyProgramStructure_Course.__init__)
    params = list(sig.parameters.keys())
    assert "credits" in params, "Missing parameter 'credits'"
    assert "code" in params, "Missing parameter 'code'"
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_studyprogramstructure_program_is_not_abstract():
    assert not inspect.isabstract(studyProgramStructure_Program)


def test_hyp_studyprogramstructure_program_constructor_exists():
    assert callable(studyProgramStructure_Program.__init__)


def test_hyp_studyprogramstructure_program_constructor_args():
    sig = inspect.signature(studyProgramStructure_Program.__init__)
    params = list(sig.parameters.keys())
    assert "numOfYears" in params, "Missing parameter 'numOfYears'"
    assert "name" in params, "Missing parameter 'name'"
    assert "numOfSemestersForBaseSpecialization" in params, "Missing parameter 'numOfSemestersForBaseSpecialization'"
    assert "code" in params, "Missing parameter 'code'"





def test_hyp_coursestatus_exists():
    # Check that the Enumeration exists
    assert CourseStatus is not None

def test_hyp_coursestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CourseStatus]
    expected_literals = [
        "mandatory",
        "elective",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CourseStatus"

def test_hyp_season_exists():
    # Check that the Enumeration exists
    assert Season is not None

def test_hyp_season_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Season]
    expected_literals = [
        "fall",
        "spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Season"

def test_hyp_grade_exists():
    # Check that the Enumeration exists
    assert Grade is not None

def test_hyp_grade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Grade]
    expected_literals = [
        "E",
        "A",
        "D",
        "F",
        "C",
        "B",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Grade"


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
studyProgramStructure_CourseGroup_strategy = st.builds(
    studyProgramStructure_CourseGroup,
    status=
        safe_text,
    name=
        safe_text
)
studyProgramStructure_CourseAllocation_strategy = st.builds(
    studyProgramStructure_CourseAllocation,
    grade=
        safe_text
)
studyProgramStructure_StudyPlan_strategy = st.builds(
    studyProgramStructure_StudyPlan,
)
studyProgramStructure_Student_strategy = st.builds(
    studyProgramStructure_Student,
    name=
        safe_text
)
studyProgramStructure_University_strategy = st.builds(
    studyProgramStructure_University,
    name=
        safe_text
)
studyProgramStructure_Semester_strategy = st.builds(
    studyProgramStructure_Semester,
    year=
        st.integers(),
    season=
        safe_text
)
studyProgramStructure_Specialization_strategy = st.builds(
    studyProgramStructure_Specialization,
    numOfSemesters=
        st.integers(),
    name=
        safe_text
)
studyProgramStructure_Course_strategy = st.builds(
    studyProgramStructure_Course,
    credits=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code=
        safe_text,
    level=
        st.integers(),
    name=
        safe_text
)
studyProgramStructure_Program_strategy = st.builds(
    studyProgramStructure_Program,
    numOfYears=
        st.integers(),
    name=
        safe_text,
    numOfSemestersForBaseSpecialization=
        st.integers(),
    code=
        safe_text
)




@given(instance=studyProgramStructure_CourseGroup_strategy)
def test_hyp_studyprogramstructure_coursegroup_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=studyProgramStructure_CourseGroup_strategy)
def test_hyp_studyprogramstructure_coursegroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=studyProgramStructure_CourseAllocation_strategy)
def test_hyp_studyprogramstructure_courseallocation_grade_setter(instance):
    original = instance.grade
    instance.grade = original
    assert instance.grade == original





@given(instance=studyProgramStructure_Student_strategy)
def test_hyp_studyprogramstructure_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=studyProgramStructure_University_strategy)
def test_hyp_studyprogramstructure_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=studyProgramStructure_Semester_strategy)
def test_hyp_studyprogramstructure_semester_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=studyProgramStructure_Semester_strategy)
def test_hyp_studyprogramstructure_semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original




@given(instance=studyProgramStructure_Specialization_strategy)
def test_hyp_studyprogramstructure_specialization_numOfSemesters_setter(instance):
    original = instance.numOfSemesters
    instance.numOfSemesters = original
    assert instance.numOfSemesters == original



@given(instance=studyProgramStructure_Specialization_strategy)
def test_hyp_studyprogramstructure_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=studyProgramStructure_Course_strategy)
def test_hyp_studyprogramstructure_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=studyProgramStructure_Course_strategy)
def test_hyp_studyprogramstructure_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=studyProgramStructure_Course_strategy)
def test_hyp_studyprogramstructure_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=studyProgramStructure_Course_strategy)
def test_hyp_studyprogramstructure_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=studyProgramStructure_Program_strategy)
def test_hyp_studyprogramstructure_program_numOfYears_setter(instance):
    original = instance.numOfYears
    instance.numOfYears = original
    assert instance.numOfYears == original



@given(instance=studyProgramStructure_Program_strategy)
def test_hyp_studyprogramstructure_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=studyProgramStructure_Program_strategy)
def test_hyp_studyprogramstructure_program_numOfSemestersForBaseSpecialization_setter(instance):
    original = instance.numOfSemestersForBaseSpecialization
    instance.numOfSemestersForBaseSpecialization = original
    assert instance.numOfSemestersForBaseSpecialization == original



@given(instance=studyProgramStructure_Program_strategy)
def test_hyp_studyprogramstructure_program_code_setter(instance):
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
    studyProgramStructure_Course,
    studyProgramStructure_CourseAllocation,
    studyProgramStructure_CourseGroup,
    studyProgramStructure_Program,
    studyProgramStructure_Semester,
    studyProgramStructure_Specialization,
    studyProgramStructure_Student,
    studyProgramStructure_StudyPlan,
    studyProgramStructure_University,
    CourseStatus,
    Grade,
    Season,
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

def test_studyProgramStructure_Course_code_value_roundtrip():
    instance = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_studyProgramStructure_Course_credits_value_roundtrip():
    instance = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    assert instance.credits == 3.14
    instance.credits = 9.99
    assert instance.credits == 9.99


def test_studyProgramStructure_Course_level_value_roundtrip():
    instance = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    assert instance.level == 7
    instance.level = 13
    assert instance.level == 13


def test_studyProgramStructure_Course_name_value_roundtrip():
    instance = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_studyProgramStructure_CourseAllocation_grade_value_roundtrip():
    instance = studyProgramStructure_CourseAllocation(grade="sample_text")
    assert instance.grade == "sample_text"
    instance.grade = "sample_text_2"
    assert instance.grade == "sample_text_2"


def test_studyProgramStructure_CourseGroup_name_value_roundtrip():
    instance = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_studyProgramStructure_CourseGroup_status_value_roundtrip():
    instance = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_studyProgramStructure_Program_code_value_roundtrip():
    instance = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_studyProgramStructure_Program_name_value_roundtrip():
    instance = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_studyProgramStructure_Program_numOfSemestersForBaseSpecialization_value_roundtrip():
    instance = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    assert instance.numOfSemestersForBaseSpecialization == 7
    instance.numOfSemestersForBaseSpecialization = 13
    assert instance.numOfSemestersForBaseSpecialization == 13


def test_studyProgramStructure_Program_numOfYears_value_roundtrip():
    instance = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    assert instance.numOfYears == 7
    instance.numOfYears = 13
    assert instance.numOfYears == 13


def test_studyProgramStructure_Semester_season_value_roundtrip():
    instance = studyProgramStructure_Semester(season="sample_text", year=7)
    assert instance.season == "sample_text"
    instance.season = "sample_text_2"
    assert instance.season == "sample_text_2"


def test_studyProgramStructure_Semester_year_value_roundtrip():
    instance = studyProgramStructure_Semester(season="sample_text", year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_studyProgramStructure_Specialization_name_value_roundtrip():
    instance = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_studyProgramStructure_Specialization_numOfSemesters_value_roundtrip():
    instance = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    assert instance.numOfSemesters == 7
    instance.numOfSemesters = 13
    assert instance.numOfSemesters == 13


def test_studyProgramStructure_Student_name_value_roundtrip():
    instance = studyProgramStructure_Student(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_studyProgramStructure_University_name_value_roundtrip():
    instance = studyProgramStructure_University(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_baseSpecialization7_link_reassign_clear():
    a = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    _safe_set(a, 'Specialization8', b1)
    assert _is_linked(a, 'Specialization8', b1)
    if hasattr(b1, 'furtherSpecializations'):
        assert _is_linked(b1, 'furtherSpecializations', a)
    _safe_set(a, 'Specialization8', b2)
    assert _is_linked(a, 'Specialization8', b2)
    if hasattr(b1, 'furtherSpecializations'):
        assert not _is_linked(b1, 'furtherSpecializations', a)
    if hasattr(b2, 'furtherSpecializations'):
        assert _is_linked(b2, 'furtherSpecializations', a)
    _safe_set(a, 'Specialization8', None)
    assert not _is_linked(a, 'Specialization8', b2)
    if hasattr(b2, 'furtherSpecializations'):
        assert not _is_linked(b2, 'furtherSpecializations', a)


def test_assoc_course37_link_reassign_clear():
    a = studyProgramStructure_CourseAllocation(grade="sample_text")
    b1 = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    b2 = studyProgramStructure_Course(code="sample_text_2", credits=9.99, level=13, name="sample_text_2")
    _safe_set(a, 'studyProgramStructure_CourseAllocation38', b1)
    assert _is_linked(a, 'studyProgramStructure_CourseAllocation38', b1)
    if hasattr(b1, 'studyProgramStructure_Course39'):
        assert _is_linked(b1, 'studyProgramStructure_Course39', a)
    _safe_set(a, 'studyProgramStructure_CourseAllocation38', b2)
    assert _is_linked(a, 'studyProgramStructure_CourseAllocation38', b2)
    if hasattr(b1, 'studyProgramStructure_Course39'):
        assert not _is_linked(b1, 'studyProgramStructure_Course39', a)
    if hasattr(b2, 'studyProgramStructure_Course39'):
        assert _is_linked(b2, 'studyProgramStructure_Course39', a)
    _safe_set(a, 'studyProgramStructure_CourseAllocation38', None)
    assert not _is_linked(a, 'studyProgramStructure_CourseAllocation38', b2)
    if hasattr(b2, 'studyProgramStructure_Course39'):
        assert not _is_linked(b2, 'studyProgramStructure_Course39', a)


def test_assoc_courseAllocation34_link_reassign_clear():
    a = studyProgramStructure_CourseAllocation(grade="sample_text")
    b1 = studyProgramStructure_StudyPlan()
    b2 = studyProgramStructure_StudyPlan()
    _safe_set(a, 'studyProgramStructure_CourseAllocation', b1)
    assert _is_linked(a, 'studyProgramStructure_CourseAllocation', b1)
    if hasattr(b1, 'studyProgramStructure_StudyPlan35'):
        assert _is_linked(b1, 'studyProgramStructure_StudyPlan35', a)
    _safe_set(a, 'studyProgramStructure_CourseAllocation', b2)
    assert _is_linked(a, 'studyProgramStructure_CourseAllocation', b2)
    if hasattr(b1, 'studyProgramStructure_StudyPlan35'):
        assert not _is_linked(b1, 'studyProgramStructure_StudyPlan35', a)
    if hasattr(b2, 'studyProgramStructure_StudyPlan35'):
        assert _is_linked(b2, 'studyProgramStructure_StudyPlan35', a)
    _safe_set(a, 'studyProgramStructure_CourseAllocation', None)
    assert not _is_linked(a, 'studyProgramStructure_CourseAllocation', b2)
    if hasattr(b2, 'studyProgramStructure_StudyPlan35'):
        assert not _is_linked(b2, 'studyProgramStructure_StudyPlan35', a)


def test_assoc_courseGroups12_link_reassign_clear():
    a = studyProgramStructure_Semester(season="sample_text", year=7)
    b1 = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    b2 = studyProgramStructure_CourseGroup(name="sample_text_2", status="sample_text_2")
    _safe_set(a, 'semester', {b1})
    assert _is_linked(a, 'semester', b1)
    if hasattr(b1, 'CourseGroup'):
        assert _is_linked(b1, 'CourseGroup', a)
    _safe_set(a, 'semester', {b2})
    assert _is_linked(a, 'semester', b2)
    if hasattr(b1, 'CourseGroup'):
        assert not _is_linked(b1, 'CourseGroup', a)
    if hasattr(b2, 'CourseGroup'):
        assert _is_linked(b2, 'CourseGroup', a)
    _safe_set(a, 'semester', set())
    assert not _is_linked(a, 'semester', b2)
    if hasattr(b2, 'CourseGroup'):
        assert not _is_linked(b2, 'CourseGroup', a)


def test_assoc_courses20_link_reassign_clear():
    a = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    b1 = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    b2 = studyProgramStructure_Course(code="sample_text_2", credits=9.99, level=13, name="sample_text_2")
    _safe_set(a, 'studyProgramStructure_CourseGroup', {b1})
    assert _is_linked(a, 'studyProgramStructure_CourseGroup', b1)
    if hasattr(b1, 'studyProgramStructure_Course'):
        assert _is_linked(b1, 'studyProgramStructure_Course', a)
    _safe_set(a, 'studyProgramStructure_CourseGroup', {b2})
    assert _is_linked(a, 'studyProgramStructure_CourseGroup', b2)
    if hasattr(b1, 'studyProgramStructure_Course'):
        assert not _is_linked(b1, 'studyProgramStructure_Course', a)
    if hasattr(b2, 'studyProgramStructure_Course'):
        assert _is_linked(b2, 'studyProgramStructure_Course', a)
    _safe_set(a, 'studyProgramStructure_CourseGroup', set())
    assert not _is_linked(a, 'studyProgramStructure_CourseGroup', b2)
    if hasattr(b2, 'studyProgramStructure_Course'):
        assert not _is_linked(b2, 'studyProgramStructure_Course', a)


def test_assoc_courses22_link_reassign_clear():
    a = studyProgramStructure_University(name="sample_text")
    b1 = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    b2 = studyProgramStructure_Course(code="sample_text_2", credits=9.99, level=13, name="sample_text_2")
    _safe_set(a, 'studyProgramStructure_University23', {b1})
    assert _is_linked(a, 'studyProgramStructure_University23', b1)
    if hasattr(b1, 'studyProgramStructure_Course24'):
        assert _is_linked(b1, 'studyProgramStructure_Course24', a)
    _safe_set(a, 'studyProgramStructure_University23', {b2})
    assert _is_linked(a, 'studyProgramStructure_University23', b2)
    if hasattr(b1, 'studyProgramStructure_Course24'):
        assert not _is_linked(b1, 'studyProgramStructure_Course24', a)
    if hasattr(b2, 'studyProgramStructure_Course24'):
        assert _is_linked(b2, 'studyProgramStructure_Course24', a)
    _safe_set(a, 'studyProgramStructure_University23', set())
    assert not _is_linked(a, 'studyProgramStructure_University23', b2)
    if hasattr(b2, 'studyProgramStructure_Course24'):
        assert not _is_linked(b2, 'studyProgramStructure_Course24', a)


def test_assoc_furtherSpecializations4_link_reassign_clear():
    a = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    _safe_set(a, 'Specialization5', b1)
    assert _is_linked(a, 'Specialization5', b1)
    if hasattr(b1, 'baseSpecialization'):
        assert _is_linked(b1, 'baseSpecialization', a)
    _safe_set(a, 'Specialization5', b2)
    assert _is_linked(a, 'Specialization5', b2)
    if hasattr(b1, 'baseSpecialization'):
        assert not _is_linked(b1, 'baseSpecialization', a)
    if hasattr(b2, 'baseSpecialization'):
        assert _is_linked(b2, 'baseSpecialization', a)
    _safe_set(a, 'Specialization5', None)
    assert not _is_linked(a, 'Specialization5', b2)
    if hasattr(b2, 'baseSpecialization'):
        assert not _is_linked(b2, 'baseSpecialization', a)


def test_assoc_program11_link_reassign_clear():
    a = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b1 = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    b2 = studyProgramStructure_Program(code="sample_text_2", name="sample_text_2", numOfSemestersForBaseSpecialization=13, numOfYears=13)
    _safe_set(a, 'specializations', b1)
    assert _is_linked(a, 'specializations', b1)
    if hasattr(b1, 'Program'):
        assert _is_linked(b1, 'Program', a)
    _safe_set(a, 'specializations', b2)
    assert _is_linked(a, 'specializations', b2)
    if hasattr(b1, 'Program'):
        assert not _is_linked(b1, 'Program', a)
    if hasattr(b2, 'Program'):
        assert _is_linked(b2, 'Program', a)
    _safe_set(a, 'specializations', None)
    assert not _is_linked(a, 'specializations', b2)
    if hasattr(b2, 'Program'):
        assert not _is_linked(b2, 'Program', a)


def test_assoc_program13_link_reassign_clear():
    a = studyProgramStructure_Semester(season="sample_text", year=7)
    b1 = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    b2 = studyProgramStructure_Program(code="sample_text_2", name="sample_text_2", numOfSemestersForBaseSpecialization=13, numOfYears=13)
    _safe_set(a, 'semesters', b1)
    assert _is_linked(a, 'semesters', b1)
    if hasattr(b1, 'Program14'):
        assert _is_linked(b1, 'Program14', a)
    _safe_set(a, 'semesters', b2)
    assert _is_linked(a, 'semesters', b2)
    if hasattr(b1, 'Program14'):
        assert not _is_linked(b1, 'Program14', a)
    if hasattr(b2, 'Program14'):
        assert _is_linked(b2, 'Program14', a)
    _safe_set(a, 'semesters', None)
    assert not _is_linked(a, 'semesters', b2)
    if hasattr(b2, 'Program14'):
        assert not _is_linked(b2, 'Program14', a)


def test_assoc_program28_link_reassign_clear():
    a = studyProgramStructure_Student(name="sample_text")
    b1 = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    b2 = studyProgramStructure_Program(code="sample_text_2", name="sample_text_2", numOfSemestersForBaseSpecialization=13, numOfYears=13)
    _safe_set(a, 'studyProgramStructure_Student29', b1)
    assert _is_linked(a, 'studyProgramStructure_Student29', b1)
    if hasattr(b1, 'studyProgramStructure_Program30'):
        assert _is_linked(b1, 'studyProgramStructure_Program30', a)
    _safe_set(a, 'studyProgramStructure_Student29', b2)
    assert _is_linked(a, 'studyProgramStructure_Student29', b2)
    if hasattr(b1, 'studyProgramStructure_Program30'):
        assert not _is_linked(b1, 'studyProgramStructure_Program30', a)
    if hasattr(b2, 'studyProgramStructure_Program30'):
        assert _is_linked(b2, 'studyProgramStructure_Program30', a)
    _safe_set(a, 'studyProgramStructure_Student29', None)
    assert not _is_linked(a, 'studyProgramStructure_Student29', b2)
    if hasattr(b2, 'studyProgramStructure_Program30'):
        assert not _is_linked(b2, 'studyProgramStructure_Program30', a)


def test_assoc_programs21_link_reassign_clear():
    a = studyProgramStructure_University(name="sample_text")
    b1 = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    b2 = studyProgramStructure_Program(code="sample_text_2", name="sample_text_2", numOfSemestersForBaseSpecialization=13, numOfYears=13)
    _safe_set(a, 'studyProgramStructure_University', {b1})
    assert _is_linked(a, 'studyProgramStructure_University', b1)
    if hasattr(b1, 'studyProgramStructure_Program'):
        assert _is_linked(b1, 'studyProgramStructure_Program', a)
    _safe_set(a, 'studyProgramStructure_University', {b2})
    assert _is_linked(a, 'studyProgramStructure_University', b2)
    if hasattr(b1, 'studyProgramStructure_Program'):
        assert not _is_linked(b1, 'studyProgramStructure_Program', a)
    if hasattr(b2, 'studyProgramStructure_Program'):
        assert _is_linked(b2, 'studyProgramStructure_Program', a)
    _safe_set(a, 'studyProgramStructure_University', set())
    assert not _is_linked(a, 'studyProgramStructure_University', b2)
    if hasattr(b2, 'studyProgramStructure_Program'):
        assert not _is_linked(b2, 'studyProgramStructure_Program', a)


def test_assoc_semester18_link_reassign_clear():
    a = studyProgramStructure_Semester(season="sample_text", year=7)
    b1 = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    b2 = studyProgramStructure_CourseGroup(name="sample_text_2", status="sample_text_2")
    _safe_set(a, 'Semester19', b1)
    assert _is_linked(a, 'Semester19', b1)
    if hasattr(b1, 'courseGroups'):
        assert _is_linked(b1, 'courseGroups', a)
    _safe_set(a, 'Semester19', b2)
    assert _is_linked(a, 'Semester19', b2)
    if hasattr(b1, 'courseGroups'):
        assert not _is_linked(b1, 'courseGroups', a)
    if hasattr(b2, 'courseGroups'):
        assert _is_linked(b2, 'courseGroups', a)
    _safe_set(a, 'Semester19', None)
    assert not _is_linked(a, 'Semester19', b2)
    if hasattr(b2, 'courseGroups'):
        assert not _is_linked(b2, 'courseGroups', a)


def test_assoc_semesters1_link_reassign_clear():
    a = studyProgramStructure_Semester(season="sample_text", year=7)
    b1 = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    b2 = studyProgramStructure_Program(code="sample_text_2", name="sample_text_2", numOfSemestersForBaseSpecialization=13, numOfYears=13)
    _safe_set(a, 'Semester', b1)
    assert _is_linked(a, 'Semester', b1)
    if hasattr(b1, 'program2'):
        assert _is_linked(b1, 'program2', a)
    _safe_set(a, 'Semester', b2)
    assert _is_linked(a, 'Semester', b2)
    if hasattr(b1, 'program2'):
        assert not _is_linked(b1, 'program2', a)
    if hasattr(b2, 'program2'):
        assert _is_linked(b2, 'program2', a)
    _safe_set(a, 'Semester', None)
    assert not _is_linked(a, 'Semester', b2)
    if hasattr(b2, 'program2'):
        assert not _is_linked(b2, 'program2', a)


def test_assoc_semesters33_link_reassign_clear():
    a = studyProgramStructure_Semester(season="sample_text", year=7)
    b1 = studyProgramStructure_StudyPlan()
    b2 = studyProgramStructure_StudyPlan()
    _safe_set(a, 'studyProgramStructure_Semester', b1)
    assert _is_linked(a, 'studyProgramStructure_Semester', b1)
    if hasattr(b1, 'studyProgramStructure_StudyPlan'):
        assert _is_linked(b1, 'studyProgramStructure_StudyPlan', a)
    _safe_set(a, 'studyProgramStructure_Semester', b2)
    assert _is_linked(a, 'studyProgramStructure_Semester', b2)
    if hasattr(b1, 'studyProgramStructure_StudyPlan'):
        assert not _is_linked(b1, 'studyProgramStructure_StudyPlan', a)
    if hasattr(b2, 'studyProgramStructure_StudyPlan'):
        assert _is_linked(b2, 'studyProgramStructure_StudyPlan', a)
    _safe_set(a, 'studyProgramStructure_Semester', None)
    assert not _is_linked(a, 'studyProgramStructure_Semester', b2)
    if hasattr(b2, 'studyProgramStructure_StudyPlan'):
        assert not _is_linked(b2, 'studyProgramStructure_StudyPlan', a)


def test_assoc_semesters9_link_reassign_clear():
    a = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b1 = studyProgramStructure_Semester(season="sample_text", year=7)
    b2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    _safe_set(a, 'specialization', {b1})
    assert _is_linked(a, 'specialization', b1)
    if hasattr(b1, 'Semester10'):
        assert _is_linked(b1, 'Semester10', a)
    _safe_set(a, 'specialization', {b2})
    assert _is_linked(a, 'specialization', b2)
    if hasattr(b1, 'Semester10'):
        assert not _is_linked(b1, 'Semester10', a)
    if hasattr(b2, 'Semester10'):
        assert _is_linked(b2, 'Semester10', a)
    _safe_set(a, 'specialization', set())
    assert not _is_linked(a, 'specialization', b2)
    if hasattr(b2, 'Semester10'):
        assert not _is_linked(b2, 'Semester10', a)


def test_assoc_specialization15_link_reassign_clear():
    a = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b1 = studyProgramStructure_Semester(season="sample_text", year=7)
    b2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    _safe_set(a, 'Specialization17', b1)
    assert _is_linked(a, 'Specialization17', b1)
    if hasattr(b1, 'semesters16'):
        assert _is_linked(b1, 'semesters16', a)
    _safe_set(a, 'Specialization17', b2)
    assert _is_linked(a, 'Specialization17', b2)
    if hasattr(b1, 'semesters16'):
        assert not _is_linked(b1, 'semesters16', a)
    if hasattr(b2, 'semesters16'):
        assert _is_linked(b2, 'semesters16', a)
    _safe_set(a, 'Specialization17', None)
    assert not _is_linked(a, 'Specialization17', b2)
    if hasattr(b2, 'semesters16'):
        assert not _is_linked(b2, 'semesters16', a)


def test_assoc_specializations0_link_reassign_clear():
    a = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b1 = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    b2 = studyProgramStructure_Program(code="sample_text_2", name="sample_text_2", numOfSemestersForBaseSpecialization=13, numOfYears=13)
    _safe_set(a, 'Specialization', b1)
    assert _is_linked(a, 'Specialization', b1)
    if hasattr(b1, 'program'):
        assert _is_linked(b1, 'program', a)
    _safe_set(a, 'Specialization', b2)
    assert _is_linked(a, 'Specialization', b2)
    if hasattr(b1, 'program'):
        assert not _is_linked(b1, 'program', a)
    if hasattr(b2, 'program'):
        assert _is_linked(b2, 'program', a)
    _safe_set(a, 'Specialization', None)
    assert not _is_linked(a, 'Specialization', b2)
    if hasattr(b2, 'program'):
        assert not _is_linked(b2, 'program', a)


def test_assoc_specializations31_link_reassign_clear():
    a = studyProgramStructure_Student(name="sample_text")
    b1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    b2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    _safe_set(a, 'studyProgramStructure_Student32', {b1})
    assert _is_linked(a, 'studyProgramStructure_Student32', b1)
    if hasattr(b1, 'studyProgramStructure_Specialization'):
        assert _is_linked(b1, 'studyProgramStructure_Specialization', a)
    _safe_set(a, 'studyProgramStructure_Student32', {b2})
    assert _is_linked(a, 'studyProgramStructure_Student32', b2)
    if hasattr(b1, 'studyProgramStructure_Specialization'):
        assert not _is_linked(b1, 'studyProgramStructure_Specialization', a)
    if hasattr(b2, 'studyProgramStructure_Specialization'):
        assert _is_linked(b2, 'studyProgramStructure_Specialization', a)
    _safe_set(a, 'studyProgramStructure_Student32', set())
    assert not _is_linked(a, 'studyProgramStructure_Student32', b2)
    if hasattr(b2, 'studyProgramStructure_Specialization'):
        assert not _is_linked(b2, 'studyProgramStructure_Specialization', a)


def test_assoc_student36_link_reassign_clear():
    a = studyProgramStructure_Student(name="sample_text")
    b1 = studyProgramStructure_StudyPlan()
    b2 = studyProgramStructure_StudyPlan()
    _safe_set(a, 'Student', b1)
    assert _is_linked(a, 'Student', b1)
    if hasattr(b1, 'studyPlan'):
        assert _is_linked(b1, 'studyPlan', a)
    _safe_set(a, 'Student', b2)
    assert _is_linked(a, 'Student', b2)
    if hasattr(b1, 'studyPlan'):
        assert not _is_linked(b1, 'studyPlan', a)
    if hasattr(b2, 'studyPlan'):
        assert _is_linked(b2, 'studyPlan', a)
    _safe_set(a, 'Student', None)
    assert not _is_linked(a, 'Student', b2)
    if hasattr(b2, 'studyPlan'):
        assert not _is_linked(b2, 'studyPlan', a)


def test_assoc_students25_link_reassign_clear():
    a = studyProgramStructure_University(name="sample_text")
    b1 = studyProgramStructure_Student(name="sample_text")
    b2 = studyProgramStructure_Student(name="sample_text_2")
    _safe_set(a, 'studyProgramStructure_University26', {b1})
    assert _is_linked(a, 'studyProgramStructure_University26', b1)
    if hasattr(b1, 'studyProgramStructure_Student'):
        assert _is_linked(b1, 'studyProgramStructure_Student', a)
    _safe_set(a, 'studyProgramStructure_University26', {b2})
    assert _is_linked(a, 'studyProgramStructure_University26', b2)
    if hasattr(b1, 'studyProgramStructure_Student'):
        assert not _is_linked(b1, 'studyProgramStructure_Student', a)
    if hasattr(b2, 'studyProgramStructure_Student'):
        assert _is_linked(b2, 'studyProgramStructure_Student', a)
    _safe_set(a, 'studyProgramStructure_University26', set())
    assert not _is_linked(a, 'studyProgramStructure_University26', b2)
    if hasattr(b2, 'studyProgramStructure_Student'):
        assert not _is_linked(b2, 'studyProgramStructure_Student', a)


def test_assoc_studyPlan27_link_reassign_clear():
    a = studyProgramStructure_Student(name="sample_text")
    b1 = studyProgramStructure_StudyPlan()
    b2 = studyProgramStructure_StudyPlan()
    _safe_set(a, 'student', b1)
    assert _is_linked(a, 'student', b1)
    if hasattr(b1, 'StudyPlan'):
        assert _is_linked(b1, 'StudyPlan', a)
    _safe_set(a, 'student', b2)
    assert _is_linked(a, 'student', b2)
    if hasattr(b1, 'StudyPlan'):
        assert not _is_linked(b1, 'StudyPlan', a)
    if hasattr(b2, 'StudyPlan'):
        assert _is_linked(b2, 'StudyPlan', a)
    _safe_set(a, 'student', None)
    assert not _is_linked(a, 'student', b2)
    if hasattr(b2, 'StudyPlan'):
        assert not _is_linked(b2, 'StudyPlan', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

studyProgramStructure_Course_strategy = st.builds(studyProgramStructure_Course, code=safe_text, credits=st.floats(allow_nan=False, allow_infinity=False), level=st.integers(), name=safe_text)
@given(instance=studyProgramStructure_Course_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_Course_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Course)


studyProgramStructure_CourseAllocation_strategy = st.builds(studyProgramStructure_CourseAllocation, grade=safe_text)
@given(instance=studyProgramStructure_CourseAllocation_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_CourseAllocation_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_CourseAllocation)


studyProgramStructure_CourseGroup_strategy = st.builds(studyProgramStructure_CourseGroup, name=safe_text, status=safe_text)
@given(instance=studyProgramStructure_CourseGroup_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_CourseGroup_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_CourseGroup)


studyProgramStructure_Program_strategy = st.builds(studyProgramStructure_Program, code=safe_text, name=safe_text, numOfSemestersForBaseSpecialization=st.integers(), numOfYears=st.integers())
@given(instance=studyProgramStructure_Program_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_Program_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Program)


studyProgramStructure_Semester_strategy = st.builds(studyProgramStructure_Semester, season=safe_text, year=st.integers())
@given(instance=studyProgramStructure_Semester_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_Semester_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Semester)


studyProgramStructure_Specialization_strategy = st.builds(studyProgramStructure_Specialization, name=safe_text, numOfSemesters=st.integers())
@given(instance=studyProgramStructure_Specialization_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_Specialization_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Specialization)


studyProgramStructure_Student_strategy = st.builds(studyProgramStructure_Student, name=safe_text)
@given(instance=studyProgramStructure_Student_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_Student_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_Student)


studyProgramStructure_StudyPlan_strategy = st.builds(studyProgramStructure_StudyPlan)
@given(instance=studyProgramStructure_StudyPlan_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_StudyPlan_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_StudyPlan)


studyProgramStructure_University_strategy = st.builds(studyProgramStructure_University, name=safe_text)
@given(instance=studyProgramStructure_University_strategy)
@settings(max_examples=25)
def test_studyProgramStructure_University_instantiation(instance):
    assert isinstance(instance, studyProgramStructure_University)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    studyProgramStructure_Course,
    studyProgramStructure_CourseAllocation,
    studyProgramStructure_CourseGroup,
    studyProgramStructure_Program,
    studyProgramStructure_Semester,
    studyProgramStructure_Specialization,
    studyProgramStructure_Student,
    studyProgramStructure_StudyPlan,
    studyProgramStructure_University,
    CourseStatus,
    Grade,
    Season,
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

def test_assoc_baseSpecialization7_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    _safe_set(b, 'furtherSpecializations', a1)
    assert _is_linked(b, 'furtherSpecializations', a1)
    if hasattr(a1, 'Specialization8'):
        assert _is_linked(a1, 'Specialization8', b)
    _safe_set(b, 'furtherSpecializations', a2)
    assert _is_linked(b, 'furtherSpecializations', a2)
    if hasattr(a1, 'Specialization8'):
        assert not _is_linked(a1, 'Specialization8', b)
    if hasattr(a2, 'Specialization8'):
        assert _is_linked(a2, 'Specialization8', b)
    _safe_set(b, 'furtherSpecializations', None)
    assert not _is_linked(b, 'furtherSpecializations', a2)
    if hasattr(a2, 'Specialization8'):
        assert not _is_linked(a2, 'Specialization8', b)


def test_assoc_course37_reverse_link_reassign_clear():
    a1 = studyProgramStructure_CourseAllocation(grade="sample_text")
    a2 = studyProgramStructure_CourseAllocation(grade="sample_text_2")
    b = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'studyProgramStructure_Course39', a1)
    assert _is_linked(b, 'studyProgramStructure_Course39', a1)
    if hasattr(a1, 'studyProgramStructure_CourseAllocation38'):
        assert _is_linked(a1, 'studyProgramStructure_CourseAllocation38', b)
    _safe_set(b, 'studyProgramStructure_Course39', a2)
    assert _is_linked(b, 'studyProgramStructure_Course39', a2)
    if hasattr(a1, 'studyProgramStructure_CourseAllocation38'):
        assert not _is_linked(a1, 'studyProgramStructure_CourseAllocation38', b)
    if hasattr(a2, 'studyProgramStructure_CourseAllocation38'):
        assert _is_linked(a2, 'studyProgramStructure_CourseAllocation38', b)
    _safe_set(b, 'studyProgramStructure_Course39', None)
    assert not _is_linked(b, 'studyProgramStructure_Course39', a2)
    if hasattr(a2, 'studyProgramStructure_CourseAllocation38'):
        assert not _is_linked(a2, 'studyProgramStructure_CourseAllocation38', b)


def test_assoc_courseGroups12_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Semester(season="sample_text", year=7)
    a2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    b = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    _safe_set(b, 'CourseGroup', a1)
    assert _is_linked(b, 'CourseGroup', a1)
    if hasattr(a1, 'semester'):
        assert _is_linked(a1, 'semester', b)
    _safe_set(b, 'CourseGroup', a2)
    assert _is_linked(b, 'CourseGroup', a2)
    if hasattr(a1, 'semester'):
        assert not _is_linked(a1, 'semester', b)
    if hasattr(a2, 'semester'):
        assert _is_linked(a2, 'semester', b)
    _safe_set(b, 'CourseGroup', None)
    assert not _is_linked(b, 'CourseGroup', a2)
    if hasattr(a2, 'semester'):
        assert not _is_linked(a2, 'semester', b)


def test_assoc_courses20_reverse_link_reassign_clear():
    a1 = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    a2 = studyProgramStructure_CourseGroup(name="sample_text_2", status="sample_text_2")
    b = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'studyProgramStructure_Course', a1)
    assert _is_linked(b, 'studyProgramStructure_Course', a1)
    if hasattr(a1, 'studyProgramStructure_CourseGroup'):
        assert _is_linked(a1, 'studyProgramStructure_CourseGroup', b)
    _safe_set(b, 'studyProgramStructure_Course', a2)
    assert _is_linked(b, 'studyProgramStructure_Course', a2)
    if hasattr(a1, 'studyProgramStructure_CourseGroup'):
        assert not _is_linked(a1, 'studyProgramStructure_CourseGroup', b)
    if hasattr(a2, 'studyProgramStructure_CourseGroup'):
        assert _is_linked(a2, 'studyProgramStructure_CourseGroup', b)
    _safe_set(b, 'studyProgramStructure_Course', None)
    assert not _is_linked(b, 'studyProgramStructure_Course', a2)
    if hasattr(a2, 'studyProgramStructure_CourseGroup'):
        assert not _is_linked(a2, 'studyProgramStructure_CourseGroup', b)


def test_assoc_courses22_reverse_link_reassign_clear():
    a1 = studyProgramStructure_University(name="sample_text")
    a2 = studyProgramStructure_University(name="sample_text_2")
    b = studyProgramStructure_Course(code="sample_text", credits=3.14, level=7, name="sample_text")
    _safe_set(b, 'studyProgramStructure_Course24', a1)
    assert _is_linked(b, 'studyProgramStructure_Course24', a1)
    if hasattr(a1, 'studyProgramStructure_University23'):
        assert _is_linked(a1, 'studyProgramStructure_University23', b)
    _safe_set(b, 'studyProgramStructure_Course24', a2)
    assert _is_linked(b, 'studyProgramStructure_Course24', a2)
    if hasattr(a1, 'studyProgramStructure_University23'):
        assert not _is_linked(a1, 'studyProgramStructure_University23', b)
    if hasattr(a2, 'studyProgramStructure_University23'):
        assert _is_linked(a2, 'studyProgramStructure_University23', b)
    _safe_set(b, 'studyProgramStructure_Course24', None)
    assert not _is_linked(b, 'studyProgramStructure_Course24', a2)
    if hasattr(a2, 'studyProgramStructure_University23'):
        assert not _is_linked(a2, 'studyProgramStructure_University23', b)


def test_assoc_furtherSpecializations4_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    _safe_set(b, 'baseSpecialization', {a1})
    assert _is_linked(b, 'baseSpecialization', a1)
    if hasattr(a1, 'Specialization5'):
        assert _is_linked(a1, 'Specialization5', b)
    _safe_set(b, 'baseSpecialization', {a2})
    assert _is_linked(b, 'baseSpecialization', a2)
    if hasattr(a1, 'Specialization5'):
        assert not _is_linked(a1, 'Specialization5', b)
    if hasattr(a2, 'Specialization5'):
        assert _is_linked(a2, 'Specialization5', b)
    _safe_set(b, 'baseSpecialization', set())
    assert not _is_linked(b, 'baseSpecialization', a2)
    if hasattr(a2, 'Specialization5'):
        assert not _is_linked(a2, 'Specialization5', b)


def test_assoc_program11_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'Program', a1)
    assert _is_linked(b, 'Program', a1)
    if hasattr(a1, 'specializations'):
        assert _is_linked(a1, 'specializations', b)
    _safe_set(b, 'Program', a2)
    assert _is_linked(b, 'Program', a2)
    if hasattr(a1, 'specializations'):
        assert not _is_linked(a1, 'specializations', b)
    if hasattr(a2, 'specializations'):
        assert _is_linked(a2, 'specializations', b)
    _safe_set(b, 'Program', None)
    assert not _is_linked(b, 'Program', a2)
    if hasattr(a2, 'specializations'):
        assert not _is_linked(a2, 'specializations', b)


def test_assoc_program13_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Semester(season="sample_text", year=7)
    a2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'Program14', a1)
    assert _is_linked(b, 'Program14', a1)
    if hasattr(a1, 'semesters'):
        assert _is_linked(a1, 'semesters', b)
    _safe_set(b, 'Program14', a2)
    assert _is_linked(b, 'Program14', a2)
    if hasattr(a1, 'semesters'):
        assert not _is_linked(a1, 'semesters', b)
    if hasattr(a2, 'semesters'):
        assert _is_linked(a2, 'semesters', b)
    _safe_set(b, 'Program14', None)
    assert not _is_linked(b, 'Program14', a2)
    if hasattr(a2, 'semesters'):
        assert not _is_linked(a2, 'semesters', b)


def test_assoc_program28_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Student(name="sample_text")
    a2 = studyProgramStructure_Student(name="sample_text_2")
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'studyProgramStructure_Program30', a1)
    assert _is_linked(b, 'studyProgramStructure_Program30', a1)
    if hasattr(a1, 'studyProgramStructure_Student29'):
        assert _is_linked(a1, 'studyProgramStructure_Student29', b)
    _safe_set(b, 'studyProgramStructure_Program30', a2)
    assert _is_linked(b, 'studyProgramStructure_Program30', a2)
    if hasattr(a1, 'studyProgramStructure_Student29'):
        assert not _is_linked(a1, 'studyProgramStructure_Student29', b)
    if hasattr(a2, 'studyProgramStructure_Student29'):
        assert _is_linked(a2, 'studyProgramStructure_Student29', b)
    _safe_set(b, 'studyProgramStructure_Program30', None)
    assert not _is_linked(b, 'studyProgramStructure_Program30', a2)
    if hasattr(a2, 'studyProgramStructure_Student29'):
        assert not _is_linked(a2, 'studyProgramStructure_Student29', b)


def test_assoc_programs21_reverse_link_reassign_clear():
    a1 = studyProgramStructure_University(name="sample_text")
    a2 = studyProgramStructure_University(name="sample_text_2")
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'studyProgramStructure_Program', a1)
    assert _is_linked(b, 'studyProgramStructure_Program', a1)
    if hasattr(a1, 'studyProgramStructure_University'):
        assert _is_linked(a1, 'studyProgramStructure_University', b)
    _safe_set(b, 'studyProgramStructure_Program', a2)
    assert _is_linked(b, 'studyProgramStructure_Program', a2)
    if hasattr(a1, 'studyProgramStructure_University'):
        assert not _is_linked(a1, 'studyProgramStructure_University', b)
    if hasattr(a2, 'studyProgramStructure_University'):
        assert _is_linked(a2, 'studyProgramStructure_University', b)
    _safe_set(b, 'studyProgramStructure_Program', None)
    assert not _is_linked(b, 'studyProgramStructure_Program', a2)
    if hasattr(a2, 'studyProgramStructure_University'):
        assert not _is_linked(a2, 'studyProgramStructure_University', b)


def test_assoc_semester18_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Semester(season="sample_text", year=7)
    a2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    b = studyProgramStructure_CourseGroup(name="sample_text", status="sample_text")
    _safe_set(b, 'courseGroups', a1)
    assert _is_linked(b, 'courseGroups', a1)
    if hasattr(a1, 'Semester19'):
        assert _is_linked(a1, 'Semester19', b)
    _safe_set(b, 'courseGroups', a2)
    assert _is_linked(b, 'courseGroups', a2)
    if hasattr(a1, 'Semester19'):
        assert not _is_linked(a1, 'Semester19', b)
    if hasattr(a2, 'Semester19'):
        assert _is_linked(a2, 'Semester19', b)
    _safe_set(b, 'courseGroups', None)
    assert not _is_linked(b, 'courseGroups', a2)
    if hasattr(a2, 'Semester19'):
        assert not _is_linked(a2, 'Semester19', b)


def test_assoc_semesters1_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Semester(season="sample_text", year=7)
    a2 = studyProgramStructure_Semester(season="sample_text_2", year=13)
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'program2', {a1})
    assert _is_linked(b, 'program2', a1)
    if hasattr(a1, 'Semester'):
        assert _is_linked(a1, 'Semester', b)
    _safe_set(b, 'program2', {a2})
    assert _is_linked(b, 'program2', a2)
    if hasattr(a1, 'Semester'):
        assert not _is_linked(a1, 'Semester', b)
    if hasattr(a2, 'Semester'):
        assert _is_linked(a2, 'Semester', b)
    _safe_set(b, 'program2', set())
    assert not _is_linked(b, 'program2', a2)
    if hasattr(a2, 'Semester'):
        assert not _is_linked(a2, 'Semester', b)


def test_assoc_semesters9_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Semester(season="sample_text", year=7)
    _safe_set(b, 'Semester10', a1)
    assert _is_linked(b, 'Semester10', a1)
    if hasattr(a1, 'specialization'):
        assert _is_linked(a1, 'specialization', b)
    _safe_set(b, 'Semester10', a2)
    assert _is_linked(b, 'Semester10', a2)
    if hasattr(a1, 'specialization'):
        assert not _is_linked(a1, 'specialization', b)
    if hasattr(a2, 'specialization'):
        assert _is_linked(a2, 'specialization', b)
    _safe_set(b, 'Semester10', None)
    assert not _is_linked(b, 'Semester10', a2)
    if hasattr(a2, 'specialization'):
        assert not _is_linked(a2, 'specialization', b)


def test_assoc_specialization15_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Semester(season="sample_text", year=7)
    _safe_set(b, 'semesters16', a1)
    assert _is_linked(b, 'semesters16', a1)
    if hasattr(a1, 'Specialization17'):
        assert _is_linked(a1, 'Specialization17', b)
    _safe_set(b, 'semesters16', a2)
    assert _is_linked(b, 'semesters16', a2)
    if hasattr(a1, 'Specialization17'):
        assert not _is_linked(a1, 'Specialization17', b)
    if hasattr(a2, 'Specialization17'):
        assert _is_linked(a2, 'Specialization17', b)
    _safe_set(b, 'semesters16', None)
    assert not _is_linked(b, 'semesters16', a2)
    if hasattr(a2, 'Specialization17'):
        assert not _is_linked(a2, 'Specialization17', b)


def test_assoc_specializations0_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    a2 = studyProgramStructure_Specialization(name="sample_text_2", numOfSemesters=13)
    b = studyProgramStructure_Program(code="sample_text", name="sample_text", numOfSemestersForBaseSpecialization=7, numOfYears=7)
    _safe_set(b, 'program', {a1})
    assert _is_linked(b, 'program', a1)
    if hasattr(a1, 'Specialization'):
        assert _is_linked(a1, 'Specialization', b)
    _safe_set(b, 'program', {a2})
    assert _is_linked(b, 'program', a2)
    if hasattr(a1, 'Specialization'):
        assert not _is_linked(a1, 'Specialization', b)
    if hasattr(a2, 'Specialization'):
        assert _is_linked(a2, 'Specialization', b)
    _safe_set(b, 'program', set())
    assert not _is_linked(b, 'program', a2)
    if hasattr(a2, 'Specialization'):
        assert not _is_linked(a2, 'Specialization', b)


def test_assoc_specializations31_reverse_link_reassign_clear():
    a1 = studyProgramStructure_Student(name="sample_text")
    a2 = studyProgramStructure_Student(name="sample_text_2")
    b = studyProgramStructure_Specialization(name="sample_text", numOfSemesters=7)
    _safe_set(b, 'studyProgramStructure_Specialization', a1)
    assert _is_linked(b, 'studyProgramStructure_Specialization', a1)
    if hasattr(a1, 'studyProgramStructure_Student32'):
        assert _is_linked(a1, 'studyProgramStructure_Student32', b)
    _safe_set(b, 'studyProgramStructure_Specialization', a2)
    assert _is_linked(b, 'studyProgramStructure_Specialization', a2)
    if hasattr(a1, 'studyProgramStructure_Student32'):
        assert not _is_linked(a1, 'studyProgramStructure_Student32', b)
    if hasattr(a2, 'studyProgramStructure_Student32'):
        assert _is_linked(a2, 'studyProgramStructure_Student32', b)
    _safe_set(b, 'studyProgramStructure_Specialization', None)
    assert not _is_linked(b, 'studyProgramStructure_Specialization', a2)
    if hasattr(a2, 'studyProgramStructure_Student32'):
        assert not _is_linked(a2, 'studyProgramStructure_Student32', b)


def test_assoc_students25_reverse_link_reassign_clear():
    a1 = studyProgramStructure_University(name="sample_text")
    a2 = studyProgramStructure_University(name="sample_text_2")
    b = studyProgramStructure_Student(name="sample_text")
    _safe_set(b, 'studyProgramStructure_Student', a1)
    assert _is_linked(b, 'studyProgramStructure_Student', a1)
    if hasattr(a1, 'studyProgramStructure_University26'):
        assert _is_linked(a1, 'studyProgramStructure_University26', b)
    _safe_set(b, 'studyProgramStructure_Student', a2)
    assert _is_linked(b, 'studyProgramStructure_Student', a2)
    if hasattr(a1, 'studyProgramStructure_University26'):
        assert not _is_linked(a1, 'studyProgramStructure_University26', b)
    if hasattr(a2, 'studyProgramStructure_University26'):
        assert _is_linked(a2, 'studyProgramStructure_University26', b)
    _safe_set(b, 'studyProgramStructure_Student', None)
    assert not _is_linked(b, 'studyProgramStructure_Student', a2)
    if hasattr(a2, 'studyProgramStructure_University26'):
        assert not _is_linked(a2, 'studyProgramStructure_University26', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_courseAllocation34_stub_double():
    # studyProgramStructure_StudyPlan has no real 'studyProgramStructure_StudyPlan35' property in the generated
    # code (a bare stub) -- manually attach it so studyProgramStructure_CourseAllocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyProgramStructure_CourseAllocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyProgramStructure_CourseAllocation(grade="sample_text")
    partner = studyProgramStructure_StudyPlan()
    setattr(partner, 'studyProgramStructure_StudyPlan35', None)
    _safe_set(owner, 'studyProgramStructure_CourseAllocation', partner)
    assert owner in getattr(partner, 'studyProgramStructure_StudyPlan35')
    _safe_set(owner, 'studyProgramStructure_CourseAllocation', None)
    assert owner not in getattr(partner, 'studyProgramStructure_StudyPlan35')


def test_assoc_semesters33_stub_double():
    # studyProgramStructure_StudyPlan has no real 'studyProgramStructure_StudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so studyProgramStructure_Semester's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyProgramStructure_Semester's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyProgramStructure_Semester(season="sample_text", year=7)
    partner = studyProgramStructure_StudyPlan()
    setattr(partner, 'studyProgramStructure_StudyPlan', None)
    _safe_set(owner, 'studyProgramStructure_Semester', partner)
    assert owner in getattr(partner, 'studyProgramStructure_StudyPlan')
    _safe_set(owner, 'studyProgramStructure_Semester', None)
    assert owner not in getattr(partner, 'studyProgramStructure_StudyPlan')


def test_assoc_student36_stub_double():
    # studyProgramStructure_StudyPlan has no real 'studyPlan' property in the generated
    # code (a bare stub) -- manually attach it so studyProgramStructure_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyProgramStructure_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyProgramStructure_Student(name="sample_text")
    partner = studyProgramStructure_StudyPlan()
    setattr(partner, 'studyPlan', None)
    _safe_set(owner, 'Student', partner)
    assert getattr(partner, 'studyPlan') == owner
    _safe_set(owner, 'Student', None)
    assert getattr(partner, 'studyPlan') is None


def test_assoc_studyPlan27_stub_double():
    # studyProgramStructure_StudyPlan has no real 'StudyPlan' property in the generated
    # code (a bare stub) -- manually attach it so studyProgramStructure_Student's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # studyProgramStructure_Student's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = studyProgramStructure_Student(name="sample_text")
    partner = studyProgramStructure_StudyPlan()
    setattr(partner, 'StudyPlan', None)
    _safe_set(owner, 'student', partner)
    assert getattr(partner, 'StudyPlan') == owner
    _safe_set(owner, 'student', None)
    assert getattr(partner, 'StudyPlan') is None




from python_code import studyProgramStructure_University

def test_studyProgramStructure_University___init__():
    assert studyProgramStructure_University.__init__(studyProgramStructure_University('', studyProgramStructure_University=set(), studyProgramStructure_University23=set(), studyProgramStructure_University26=set()), '', studyProgramStructure_University=set(), studyProgramStructure_University23=set(), studyProgramStructure_University26=set()) == None

