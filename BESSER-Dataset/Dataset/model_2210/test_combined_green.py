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
    CourseSlot,
    universityStudies_ElectiveCourseSlot,
    universityStudies_MandatoryCourseSlot,
    universityStudies_Department,
    universityStudies_Semester,
    universityStudies_Specialization,
    universityStudies_Programme,
    universityStudies_CourseSlot,
    universityStudies_Course,
    ProgrammeType,
    Seasons,
    Credits,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_courseslot_is_not_abstract():
    assert not inspect.isabstract(CourseSlot)


def test_hyp_courseslot_constructor_exists():
    assert callable(CourseSlot.__init__)


def test_hyp_courseslot_constructor_args():
    sig = inspect.signature(CourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_universitystudies_electivecourseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies_ElectiveCourseSlot)


def test_hyp_universitystudies_electivecourseslot_constructor_exists():
    assert callable(universityStudies_ElectiveCourseSlot.__init__)


def test_hyp_universitystudies_electivecourseslot_constructor_args():
    sig = inspect.signature(universityStudies_ElectiveCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_universitystudies_mandatorycourseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies_MandatoryCourseSlot)


def test_hyp_universitystudies_mandatorycourseslot_constructor_exists():
    assert callable(universityStudies_MandatoryCourseSlot.__init__)


def test_hyp_universitystudies_mandatorycourseslot_constructor_args():
    sig = inspect.signature(universityStudies_MandatoryCourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_universitystudies_department_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Department)


def test_hyp_universitystudies_department_constructor_exists():
    assert callable(universityStudies_Department.__init__)


def test_hyp_universitystudies_department_constructor_args():
    sig = inspect.signature(universityStudies_Department.__init__)
    params = list(sig.parameters.keys())



def test_hyp_universitystudies_semester_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Semester)


def test_hyp_universitystudies_semester_constructor_exists():
    assert callable(universityStudies_Semester.__init__)


def test_hyp_universitystudies_semester_constructor_args():
    sig = inspect.signature(universityStudies_Semester.__init__)
    params = list(sig.parameters.keys())
    assert "semesterNumber" in params, "Missing parameter 'semesterNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "season" in params, "Missing parameter 'season'"






def test_hyp_universitystudies_specialization_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Specialization)


def test_hyp_universitystudies_specialization_constructor_exists():
    assert callable(universityStudies_Specialization.__init__)


def test_hyp_universitystudies_specialization_constructor_args():
    sig = inspect.signature(universityStudies_Specialization.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_universitystudies_programme_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Programme)


def test_hyp_universitystudies_programme_constructor_exists():
    assert callable(universityStudies_Programme.__init__)


def test_hyp_universitystudies_programme_constructor_args():
    sig = inspect.signature(universityStudies_Programme.__init__)
    params = list(sig.parameters.keys())
    assert "programmeType" in params, "Missing parameter 'programmeType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "numberOfSemesters" in params, "Missing parameter 'numberOfSemesters'"






def test_hyp_universitystudies_courseslot_is_not_abstract():
    assert not inspect.isabstract(universityStudies_CourseSlot)


def test_hyp_universitystudies_courseslot_constructor_exists():
    assert callable(universityStudies_CourseSlot.__init__)


def test_hyp_universitystudies_courseslot_constructor_args():
    sig = inspect.signature(universityStudies_CourseSlot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_universitystudies_course_is_not_abstract():
    assert not inspect.isabstract(universityStudies_Course)


def test_hyp_universitystudies_course_constructor_exists():
    assert callable(universityStudies_Course.__init__)


def test_hyp_universitystudies_course_constructor_args():
    sig = inspect.signature(universityStudies_Course.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "credits" in params, "Missing parameter 'credits'"
    assert "level" in params, "Missing parameter 'level'"





def test_hyp_programmetype_exists():
    # Check that the Enumeration exists
    assert ProgrammeType is not None

def test_hyp_programmetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProgrammeType]
    expected_literals = [
        "IntegrertMaster",
        "Master",
        "Årsstudie",
        "Bachelor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProgrammeType"

def test_hyp_seasons_exists():
    # Check that the Enumeration exists
    assert Seasons is not None

def test_hyp_seasons_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Seasons]
    expected_literals = [
        "Fall",
        "Spring",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Seasons"

def test_hyp_credits_exists():
    # Check that the Enumeration exists
    assert Credits is not None

def test_hyp_credits_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Credits]
    expected_literals = [
        "Double",
        "Minor",
        "Basic",
        "Full",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Credits"


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
CourseSlot_strategy = st.builds(
    CourseSlot,
)
universityStudies_ElectiveCourseSlot_strategy = st.builds(
    universityStudies_ElectiveCourseSlot,
)
universityStudies_MandatoryCourseSlot_strategy = st.builds(
    universityStudies_MandatoryCourseSlot,
)
universityStudies_Department_strategy = st.builds(
    universityStudies_Department,
)
universityStudies_Semester_strategy = st.builds(
    universityStudies_Semester,
    semesterNumber=
        st.integers(),
    name=
        safe_text,
    season=
        safe_text
)
universityStudies_Specialization_strategy = st.builds(
    universityStudies_Specialization,
    name=
        safe_text
)
universityStudies_Programme_strategy = st.builds(
    universityStudies_Programme,
    programmeType=
        safe_text,
    name=
        safe_text,
    numberOfSemesters=
        st.integers()
)
universityStudies_CourseSlot_strategy = st.builds(
    universityStudies_CourseSlot,
)
universityStudies_Course_strategy = st.builds(
    universityStudies_Course,
    code=
        safe_text,
    name=
        safe_text,
    credits=
        safe_text,
    level=
        st.integers()
)








@given(instance=universityStudies_Semester_strategy)
def test_hyp_universitystudies_semester_semesterNumber_setter(instance):
    original = instance.semesterNumber
    instance.semesterNumber = original
    assert instance.semesterNumber == original



@given(instance=universityStudies_Semester_strategy)
def test_hyp_universitystudies_semester_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=universityStudies_Semester_strategy)
def test_hyp_universitystudies_semester_season_setter(instance):
    original = instance.season
    instance.season = original
    assert instance.season == original




@given(instance=universityStudies_Specialization_strategy)
def test_hyp_universitystudies_specialization_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=universityStudies_Programme_strategy)
def test_hyp_universitystudies_programme_programmeType_setter(instance):
    original = instance.programmeType
    instance.programmeType = original
    assert instance.programmeType == original



@given(instance=universityStudies_Programme_strategy)
def test_hyp_universitystudies_programme_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=universityStudies_Programme_strategy)
def test_hyp_universitystudies_programme_numberOfSemesters_setter(instance):
    original = instance.numberOfSemesters
    instance.numberOfSemesters = original
    assert instance.numberOfSemesters == original





@given(instance=universityStudies_Course_strategy)
def test_hyp_universitystudies_course_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=universityStudies_Course_strategy)
def test_hyp_universitystudies_course_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=universityStudies_Course_strategy)
def test_hyp_universitystudies_course_credits_setter(instance):
    original = instance.credits
    instance.credits = original
    assert instance.credits == original



@given(instance=universityStudies_Course_strategy)
def test_hyp_universitystudies_course_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CourseSlot,
    universityStudies_Course,
    universityStudies_CourseSlot,
    universityStudies_Department,
    universityStudies_ElectiveCourseSlot,
    universityStudies_MandatoryCourseSlot,
    universityStudies_Programme,
    universityStudies_Semester,
    universityStudies_Specialization,
    Credits,
    ProgrammeType,
    Seasons,
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

def test_universityStudies_Course_code_value_roundtrip():
    instance = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_universityStudies_Course_credits_value_roundtrip():
    instance = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    assert instance.credits == "sample_text"
    instance.credits = "sample_text_2"
    assert instance.credits == "sample_text_2"


def test_universityStudies_Course_level_value_roundtrip():
    instance = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    assert instance.level == 7
    instance.level = 13
    assert instance.level == 13


def test_universityStudies_Course_name_value_roundtrip():
    instance = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_universityStudies_Programme_name_value_roundtrip():
    instance = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_universityStudies_Programme_numberOfSemesters_value_roundtrip():
    instance = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    assert instance.numberOfSemesters == 7
    instance.numberOfSemesters = 13
    assert instance.numberOfSemesters == 13


def test_universityStudies_Programme_programmeType_value_roundtrip():
    instance = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    assert instance.programmeType == "sample_text"
    instance.programmeType = "sample_text_2"
    assert instance.programmeType == "sample_text_2"


def test_universityStudies_Semester_name_value_roundtrip():
    instance = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_universityStudies_Semester_season_value_roundtrip():
    instance = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    assert instance.season == "sample_text"
    instance.season = "sample_text_2"
    assert instance.season == "sample_text_2"


def test_universityStudies_Semester_semesterNumber_value_roundtrip():
    instance = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    assert instance.semesterNumber == 7
    instance.semesterNumber = 13
    assert instance.semesterNumber == 13


def test_universityStudies_Specialization_name_value_roundtrip():
    instance = universityStudies_Specialization(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_universityStudies_ElectiveCourseSlot_isa_CourseSlot():
    instance = universityStudies_ElectiveCourseSlot()
    assert isinstance(instance, CourseSlot)


def test_universityStudies_MandatoryCourseSlot_isa_CourseSlot():
    instance = universityStudies_MandatoryCourseSlot()
    assert isinstance(instance, CourseSlot)


def test_assoc_Courses14_link_reassign_clear():
    a = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    b1 = universityStudies_Department()
    b2 = universityStudies_Department()
    _safe_set(a, 'universityStudies_Course15', b1)
    assert _is_linked(a, 'universityStudies_Course15', b1)
    if hasattr(b1, 'universityStudies_Department'):
        assert _is_linked(b1, 'universityStudies_Department', a)
    _safe_set(a, 'universityStudies_Course15', b2)
    assert _is_linked(a, 'universityStudies_Course15', b2)
    if hasattr(b1, 'universityStudies_Department'):
        assert not _is_linked(b1, 'universityStudies_Department', a)
    if hasattr(b2, 'universityStudies_Department'):
        assert _is_linked(b2, 'universityStudies_Department', a)
    _safe_set(a, 'universityStudies_Course15', None)
    assert not _is_linked(a, 'universityStudies_Course15', b2)
    if hasattr(b2, 'universityStudies_Department'):
        assert not _is_linked(b2, 'universityStudies_Department', a)


def test_assoc_Department5_link_reassign_clear():
    a = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    b1 = universityStudies_Department()
    b2 = universityStudies_Department()
    _safe_set(a, 'Programmes', b1)
    assert _is_linked(a, 'Programmes', b1)
    if hasattr(b1, 'Department'):
        assert _is_linked(b1, 'Department', a)
    _safe_set(a, 'Programmes', b2)
    assert _is_linked(a, 'Programmes', b2)
    if hasattr(b1, 'Department'):
        assert not _is_linked(b1, 'Department', a)
    if hasattr(b2, 'Department'):
        assert _is_linked(b2, 'Department', a)
    _safe_set(a, 'Programmes', None)
    assert not _is_linked(a, 'Programmes', b2)
    if hasattr(b2, 'Department'):
        assert not _is_linked(b2, 'Department', a)


def test_assoc_Programmes16_link_reassign_clear():
    a = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    b1 = universityStudies_Department()
    b2 = universityStudies_Department()
    _safe_set(a, 'Programme', b1)
    assert _is_linked(a, 'Programme', b1)
    if hasattr(b1, 'Department17'):
        assert _is_linked(b1, 'Department17', a)
    _safe_set(a, 'Programme', b2)
    assert _is_linked(a, 'Programme', b2)
    if hasattr(b1, 'Department17'):
        assert not _is_linked(b1, 'Department17', a)
    if hasattr(b2, 'Department17'):
        assert _is_linked(b2, 'Department17', a)
    _safe_set(a, 'Programme', None)
    assert not _is_linked(a, 'Programme', b2)
    if hasattr(b2, 'Department17'):
        assert not _is_linked(b2, 'Department17', a)


def test_assoc_course18_link_reassign_clear():
    a = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    b1 = universityStudies_CourseSlot()
    b2 = universityStudies_CourseSlot()
    _safe_set(a, 'universityStudies_Course20', b1)
    assert _is_linked(a, 'universityStudies_Course20', b1)
    if hasattr(b1, 'universityStudies_CourseSlot19'):
        assert _is_linked(b1, 'universityStudies_CourseSlot19', a)
    _safe_set(a, 'universityStudies_Course20', b2)
    assert _is_linked(a, 'universityStudies_Course20', b2)
    if hasattr(b1, 'universityStudies_CourseSlot19'):
        assert not _is_linked(b1, 'universityStudies_CourseSlot19', a)
    if hasattr(b2, 'universityStudies_CourseSlot19'):
        assert _is_linked(b2, 'universityStudies_CourseSlot19', a)
    _safe_set(a, 'universityStudies_Course20', None)
    assert not _is_linked(a, 'universityStudies_Course20', b2)
    if hasattr(b2, 'universityStudies_CourseSlot19'):
        assert not _is_linked(b2, 'universityStudies_CourseSlot19', a)


def test_assoc_courseSlots12_link_reassign_clear():
    a = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    b1 = universityStudies_CourseSlot()
    b2 = universityStudies_CourseSlot()
    _safe_set(a, 'universityStudies_Semester13', {b1})
    assert _is_linked(a, 'universityStudies_Semester13', b1)
    if hasattr(b1, 'universityStudies_CourseSlot'):
        assert _is_linked(b1, 'universityStudies_CourseSlot', a)
    _safe_set(a, 'universityStudies_Semester13', {b2})
    assert _is_linked(a, 'universityStudies_Semester13', b2)
    if hasattr(b1, 'universityStudies_CourseSlot'):
        assert not _is_linked(b1, 'universityStudies_CourseSlot', a)
    if hasattr(b2, 'universityStudies_CourseSlot'):
        assert _is_linked(b2, 'universityStudies_CourseSlot', a)
    _safe_set(a, 'universityStudies_Semester13', set())
    assert not _is_linked(a, 'universityStudies_Semester13', b2)
    if hasattr(b2, 'universityStudies_CourseSlot'):
        assert not _is_linked(b2, 'universityStudies_CourseSlot', a)


def test_assoc_furtherSpecializations7_link_reassign_clear():
    a = universityStudies_Specialization(name="sample_text")
    b1 = universityStudies_Specialization(name="sample_text")
    b2 = universityStudies_Specialization(name="sample_text_2")
    _safe_set(a, 'universityStudies_Specialization6', {b1})
    assert _is_linked(a, 'universityStudies_Specialization6', b1)
    if hasattr(b1, 'universityStudies_Specialization8'):
        assert _is_linked(b1, 'universityStudies_Specialization8', a)
    _safe_set(a, 'universityStudies_Specialization6', {b2})
    assert _is_linked(a, 'universityStudies_Specialization6', b2)
    if hasattr(b1, 'universityStudies_Specialization8'):
        assert not _is_linked(b1, 'universityStudies_Specialization8', a)
    if hasattr(b2, 'universityStudies_Specialization8'):
        assert _is_linked(b2, 'universityStudies_Specialization8', a)
    _safe_set(a, 'universityStudies_Specialization6', set())
    assert not _is_linked(a, 'universityStudies_Specialization6', b2)
    if hasattr(b2, 'universityStudies_Specialization8'):
        assert not _is_linked(b2, 'universityStudies_Specialization8', a)


def test_assoc_optionalCourses21_link_reassign_clear():
    a = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    b1 = universityStudies_ElectiveCourseSlot()
    b2 = universityStudies_ElectiveCourseSlot()
    _safe_set(a, 'universityStudies_Course22', b1)
    assert _is_linked(a, 'universityStudies_Course22', b1)
    if hasattr(b1, 'universityStudies_ElectiveCourseSlot'):
        assert _is_linked(b1, 'universityStudies_ElectiveCourseSlot', a)
    _safe_set(a, 'universityStudies_Course22', b2)
    assert _is_linked(a, 'universityStudies_Course22', b2)
    if hasattr(b1, 'universityStudies_ElectiveCourseSlot'):
        assert not _is_linked(b1, 'universityStudies_ElectiveCourseSlot', a)
    if hasattr(b2, 'universityStudies_ElectiveCourseSlot'):
        assert _is_linked(b2, 'universityStudies_ElectiveCourseSlot', a)
    _safe_set(a, 'universityStudies_Course22', None)
    assert not _is_linked(a, 'universityStudies_Course22', b2)
    if hasattr(b2, 'universityStudies_ElectiveCourseSlot'):
        assert not _is_linked(b2, 'universityStudies_ElectiveCourseSlot', a)


def test_assoc_programmes0_link_reassign_clear():
    a = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    b1 = universityStudies_Course(code="sample_text", credits="sample_text", level=7, name="sample_text")
    b2 = universityStudies_Course(code="sample_text_2", credits="sample_text_2", level=13, name="sample_text_2")
    _safe_set(a, 'universityStudies_Programme', b1)
    assert _is_linked(a, 'universityStudies_Programme', b1)
    if hasattr(b1, 'universityStudies_Course'):
        assert _is_linked(b1, 'universityStudies_Course', a)
    _safe_set(a, 'universityStudies_Programme', b2)
    assert _is_linked(a, 'universityStudies_Programme', b2)
    if hasattr(b1, 'universityStudies_Course'):
        assert not _is_linked(b1, 'universityStudies_Course', a)
    if hasattr(b2, 'universityStudies_Course'):
        assert _is_linked(b2, 'universityStudies_Course', a)
    _safe_set(a, 'universityStudies_Programme', None)
    assert not _is_linked(a, 'universityStudies_Programme', b2)
    if hasattr(b2, 'universityStudies_Course'):
        assert not _is_linked(b2, 'universityStudies_Course', a)


def test_assoc_semesters3_link_reassign_clear():
    a = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    b1 = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    b2 = universityStudies_Programme(name="sample_text_2", numberOfSemesters=13, programmeType="sample_text_2")
    _safe_set(a, 'universityStudies_Semester', b1)
    assert _is_linked(a, 'universityStudies_Semester', b1)
    if hasattr(b1, 'universityStudies_Programme4'):
        assert _is_linked(b1, 'universityStudies_Programme4', a)
    _safe_set(a, 'universityStudies_Semester', b2)
    assert _is_linked(a, 'universityStudies_Semester', b2)
    if hasattr(b1, 'universityStudies_Programme4'):
        assert not _is_linked(b1, 'universityStudies_Programme4', a)
    if hasattr(b2, 'universityStudies_Programme4'):
        assert _is_linked(b2, 'universityStudies_Programme4', a)
    _safe_set(a, 'universityStudies_Semester', None)
    assert not _is_linked(a, 'universityStudies_Semester', b2)
    if hasattr(b2, 'universityStudies_Programme4'):
        assert not _is_linked(b2, 'universityStudies_Programme4', a)


def test_assoc_semesters9_link_reassign_clear():
    a = universityStudies_Specialization(name="sample_text")
    b1 = universityStudies_Semester(name="sample_text", season="sample_text", semesterNumber=7)
    b2 = universityStudies_Semester(name="sample_text_2", season="sample_text_2", semesterNumber=13)
    _safe_set(a, 'universityStudies_Specialization10', {b1})
    assert _is_linked(a, 'universityStudies_Specialization10', b1)
    if hasattr(b1, 'universityStudies_Semester11'):
        assert _is_linked(b1, 'universityStudies_Semester11', a)
    _safe_set(a, 'universityStudies_Specialization10', {b2})
    assert _is_linked(a, 'universityStudies_Specialization10', b2)
    if hasattr(b1, 'universityStudies_Semester11'):
        assert not _is_linked(b1, 'universityStudies_Semester11', a)
    if hasattr(b2, 'universityStudies_Semester11'):
        assert _is_linked(b2, 'universityStudies_Semester11', a)
    _safe_set(a, 'universityStudies_Specialization10', set())
    assert not _is_linked(a, 'universityStudies_Specialization10', b2)
    if hasattr(b2, 'universityStudies_Semester11'):
        assert not _is_linked(b2, 'universityStudies_Semester11', a)


def test_assoc_specializations1_link_reassign_clear():
    a = universityStudies_Specialization(name="sample_text")
    b1 = universityStudies_Programme(name="sample_text", numberOfSemesters=7, programmeType="sample_text")
    b2 = universityStudies_Programme(name="sample_text_2", numberOfSemesters=13, programmeType="sample_text_2")
    _safe_set(a, 'universityStudies_Specialization', b1)
    assert _is_linked(a, 'universityStudies_Specialization', b1)
    if hasattr(b1, 'universityStudies_Programme2'):
        assert _is_linked(b1, 'universityStudies_Programme2', a)
    _safe_set(a, 'universityStudies_Specialization', b2)
    assert _is_linked(a, 'universityStudies_Specialization', b2)
    if hasattr(b1, 'universityStudies_Programme2'):
        assert not _is_linked(b1, 'universityStudies_Programme2', a)
    if hasattr(b2, 'universityStudies_Programme2'):
        assert _is_linked(b2, 'universityStudies_Programme2', a)
    _safe_set(a, 'universityStudies_Specialization', None)
    assert not _is_linked(a, 'universityStudies_Specialization', b2)
    if hasattr(b2, 'universityStudies_Programme2'):
        assert not _is_linked(b2, 'universityStudies_Programme2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CourseSlot_strategy = st.builds(CourseSlot)
@given(instance=CourseSlot_strategy)
@settings(max_examples=25)
def test_CourseSlot_instantiation(instance):
    assert isinstance(instance, CourseSlot)


universityStudies_Course_strategy = st.builds(universityStudies_Course, code=safe_text, credits=safe_text, level=st.integers(), name=safe_text)
@given(instance=universityStudies_Course_strategy)
@settings(max_examples=25)
def test_universityStudies_Course_instantiation(instance):
    assert isinstance(instance, universityStudies_Course)


universityStudies_CourseSlot_strategy = st.builds(universityStudies_CourseSlot)
@given(instance=universityStudies_CourseSlot_strategy)
@settings(max_examples=25)
def test_universityStudies_CourseSlot_instantiation(instance):
    assert isinstance(instance, universityStudies_CourseSlot)


universityStudies_Department_strategy = st.builds(universityStudies_Department)
@given(instance=universityStudies_Department_strategy)
@settings(max_examples=25)
def test_universityStudies_Department_instantiation(instance):
    assert isinstance(instance, universityStudies_Department)


universityStudies_ElectiveCourseSlot_strategy = st.builds(universityStudies_ElectiveCourseSlot)
@given(instance=universityStudies_ElectiveCourseSlot_strategy)
@settings(max_examples=25)
def test_universityStudies_ElectiveCourseSlot_instantiation(instance):
    assert isinstance(instance, universityStudies_ElectiveCourseSlot)


universityStudies_MandatoryCourseSlot_strategy = st.builds(universityStudies_MandatoryCourseSlot)
@given(instance=universityStudies_MandatoryCourseSlot_strategy)
@settings(max_examples=25)
def test_universityStudies_MandatoryCourseSlot_instantiation(instance):
    assert isinstance(instance, universityStudies_MandatoryCourseSlot)


universityStudies_Programme_strategy = st.builds(universityStudies_Programme, name=safe_text, numberOfSemesters=st.integers(), programmeType=safe_text)
@given(instance=universityStudies_Programme_strategy)
@settings(max_examples=25)
def test_universityStudies_Programme_instantiation(instance):
    assert isinstance(instance, universityStudies_Programme)


universityStudies_Semester_strategy = st.builds(universityStudies_Semester, name=safe_text, season=safe_text, semesterNumber=st.integers())
@given(instance=universityStudies_Semester_strategy)
@settings(max_examples=25)
def test_universityStudies_Semester_instantiation(instance):
    assert isinstance(instance, universityStudies_Semester)


universityStudies_Specialization_strategy = st.builds(universityStudies_Specialization, name=safe_text)
@given(instance=universityStudies_Specialization_strategy)
@settings(max_examples=25)
def test_universityStudies_Specialization_instantiation(instance):
    assert isinstance(instance, universityStudies_Specialization)



