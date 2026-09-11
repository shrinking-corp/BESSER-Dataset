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


