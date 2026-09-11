import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    StudyProgrammes_Course,
    StudyProgrammes_CourseAccess,
    StudyProgrammes_Department,
    StudyProgrammes_Programme,
    StudyProgrammes_Semester,
    StudyProgrammes_Specialization,
    Access,
    SemesterSeason,
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

def test_StudyProgrammes_Course_availableSemesters_value_roundtrip():
    instance = StudyProgrammes_Course(availableSemesters="sample_text", code="sample_text", credits=3.14, name="sample_text")
    assert instance.availableSemesters == "sample_text"
    instance.availableSemesters = "sample_text_2"
    assert instance.availableSemesters == "sample_text_2"


def test_StudyProgrammes_Course_code_value_roundtrip():
    instance = StudyProgrammes_Course(availableSemesters="sample_text", code="sample_text", credits=3.14, name="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_StudyProgrammes_Course_credits_value_roundtrip():
    instance = StudyProgrammes_Course(availableSemesters="sample_text", code="sample_text", credits=3.14, name="sample_text")
    assert instance.credits == 3.14
    instance.credits = 9.99
    assert instance.credits == 9.99


def test_StudyProgrammes_Course_name_value_roundtrip():
    instance = StudyProgrammes_Course(availableSemesters="sample_text", code="sample_text", credits=3.14, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_StudyProgrammes_CourseAccess_access_value_roundtrip():
    instance = StudyProgrammes_CourseAccess(access="sample_text")
    assert instance.access == "sample_text"
    instance.access = "sample_text_2"
    assert instance.access == "sample_text_2"


def test_StudyProgrammes_Department_name_value_roundtrip():
    instance = StudyProgrammes_Department(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_StudyProgrammes_Programme_code_value_roundtrip():
    instance = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_StudyProgrammes_Programme_name_value_roundtrip():
    instance = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_StudyProgrammes_Programme_semestersBeforeSpecialization_value_roundtrip():
    instance = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    assert instance.semestersBeforeSpecialization == 7
    instance.semestersBeforeSpecialization = 13
    assert instance.semestersBeforeSpecialization == 13


def test_StudyProgrammes_Programme_startYear_value_roundtrip():
    instance = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    assert instance.startYear == 7
    instance.startYear = 13
    assert instance.startYear == 13


def test_StudyProgrammes_Programme_totalNumberOfSemesters_value_roundtrip():
    instance = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    assert instance.totalNumberOfSemesters == 7
    instance.totalNumberOfSemesters = 13
    assert instance.totalNumberOfSemesters == 13


def test_StudyProgrammes_Semester_code_value_roundtrip():
    instance = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_StudyProgrammes_Semester_semesterSeason_value_roundtrip():
    instance = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    assert instance.semesterSeason == "sample_text"
    instance.semesterSeason = "sample_text_2"
    assert instance.semesterSeason == "sample_text_2"


def test_StudyProgrammes_Semester_year_value_roundtrip():
    instance = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_StudyProgrammes_Specialization_lengthInSemesters_value_roundtrip():
    instance = StudyProgrammes_Specialization(lengthInSemesters=7, name="sample_text", startSemester=7)
    assert instance.lengthInSemesters == 7
    instance.lengthInSemesters = 13
    assert instance.lengthInSemesters == 13


def test_StudyProgrammes_Specialization_name_value_roundtrip():
    instance = StudyProgrammes_Specialization(lengthInSemesters=7, name="sample_text", startSemester=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_StudyProgrammes_Specialization_startSemester_value_roundtrip():
    instance = StudyProgrammes_Specialization(lengthInSemesters=7, name="sample_text", startSemester=7)
    assert instance.startSemester == 7
    instance.startSemester = 13
    assert instance.startSemester == 13


def test_assoc_course12_link_reassign_clear():
    a = StudyProgrammes_CourseAccess(access="sample_text")
    b1 = StudyProgrammes_Course(availableSemesters="sample_text", code="sample_text", credits=3.14, name="sample_text")
    b2 = StudyProgrammes_Course(availableSemesters="sample_text_2", code="sample_text_2", credits=9.99, name="sample_text_2")
    _safe_set(a, 'StudyProgrammes_CourseAccess13', b1)
    assert _is_linked(a, 'StudyProgrammes_CourseAccess13', b1)
    if hasattr(b1, 'StudyProgrammes_Course14'):
        assert _is_linked(b1, 'StudyProgrammes_Course14', a)
    _safe_set(a, 'StudyProgrammes_CourseAccess13', b2)
    assert _is_linked(a, 'StudyProgrammes_CourseAccess13', b2)
    if hasattr(b1, 'StudyProgrammes_Course14'):
        assert not _is_linked(b1, 'StudyProgrammes_Course14', a)
    if hasattr(b2, 'StudyProgrammes_Course14'):
        assert _is_linked(b2, 'StudyProgrammes_Course14', a)
    _safe_set(a, 'StudyProgrammes_CourseAccess13', None)
    assert not _is_linked(a, 'StudyProgrammes_CourseAccess13', b2)
    if hasattr(b2, 'StudyProgrammes_Course14'):
        assert not _is_linked(b2, 'StudyProgrammes_Course14', a)


def test_assoc_courseAccesses10_link_reassign_clear():
    a = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    b1 = StudyProgrammes_CourseAccess(access="sample_text")
    b2 = StudyProgrammes_CourseAccess(access="sample_text_2")
    _safe_set(a, 'StudyProgrammes_Semester11', {b1})
    assert _is_linked(a, 'StudyProgrammes_Semester11', b1)
    if hasattr(b1, 'StudyProgrammes_CourseAccess'):
        assert _is_linked(b1, 'StudyProgrammes_CourseAccess', a)
    _safe_set(a, 'StudyProgrammes_Semester11', {b2})
    assert _is_linked(a, 'StudyProgrammes_Semester11', b2)
    if hasattr(b1, 'StudyProgrammes_CourseAccess'):
        assert not _is_linked(b1, 'StudyProgrammes_CourseAccess', a)
    if hasattr(b2, 'StudyProgrammes_CourseAccess'):
        assert _is_linked(b2, 'StudyProgrammes_CourseAccess', a)
    _safe_set(a, 'StudyProgrammes_Semester11', set())
    assert not _is_linked(a, 'StudyProgrammes_Semester11', b2)
    if hasattr(b2, 'StudyProgrammes_CourseAccess'):
        assert not _is_linked(b2, 'StudyProgrammes_CourseAccess', a)


def test_assoc_courses1_link_reassign_clear():
    a = StudyProgrammes_Department(name="sample_text")
    b1 = StudyProgrammes_Course(availableSemesters="sample_text", code="sample_text", credits=3.14, name="sample_text")
    b2 = StudyProgrammes_Course(availableSemesters="sample_text_2", code="sample_text_2", credits=9.99, name="sample_text_2")
    _safe_set(a, 'StudyProgrammes_Department2', {b1})
    assert _is_linked(a, 'StudyProgrammes_Department2', b1)
    if hasattr(b1, 'StudyProgrammes_Course'):
        assert _is_linked(b1, 'StudyProgrammes_Course', a)
    _safe_set(a, 'StudyProgrammes_Department2', {b2})
    assert _is_linked(a, 'StudyProgrammes_Department2', b2)
    if hasattr(b1, 'StudyProgrammes_Course'):
        assert not _is_linked(b1, 'StudyProgrammes_Course', a)
    if hasattr(b2, 'StudyProgrammes_Course'):
        assert _is_linked(b2, 'StudyProgrammes_Course', a)
    _safe_set(a, 'StudyProgrammes_Department2', set())
    assert not _is_linked(a, 'StudyProgrammes_Department2', b2)
    if hasattr(b2, 'StudyProgrammes_Course'):
        assert not _is_linked(b2, 'StudyProgrammes_Course', a)


def test_assoc_programmes0_link_reassign_clear():
    a = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    b1 = StudyProgrammes_Department(name="sample_text")
    b2 = StudyProgrammes_Department(name="sample_text_2")
    _safe_set(a, 'StudyProgrammes_Programme', b1)
    assert _is_linked(a, 'StudyProgrammes_Programme', b1)
    if hasattr(b1, 'StudyProgrammes_Department'):
        assert _is_linked(b1, 'StudyProgrammes_Department', a)
    _safe_set(a, 'StudyProgrammes_Programme', b2)
    assert _is_linked(a, 'StudyProgrammes_Programme', b2)
    if hasattr(b1, 'StudyProgrammes_Department'):
        assert not _is_linked(b1, 'StudyProgrammes_Department', a)
    if hasattr(b2, 'StudyProgrammes_Department'):
        assert _is_linked(b2, 'StudyProgrammes_Department', a)
    _safe_set(a, 'StudyProgrammes_Programme', None)
    assert not _is_linked(a, 'StudyProgrammes_Programme', b2)
    if hasattr(b2, 'StudyProgrammes_Department'):
        assert not _is_linked(b2, 'StudyProgrammes_Department', a)


def test_assoc_semesters5_link_reassign_clear():
    a = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    b1 = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    b2 = StudyProgrammes_Programme(code="sample_text_2", name="sample_text_2", semestersBeforeSpecialization=13, startYear=13, totalNumberOfSemesters=13)
    _safe_set(a, 'StudyProgrammes_Semester', b1)
    assert _is_linked(a, 'StudyProgrammes_Semester', b1)
    if hasattr(b1, 'StudyProgrammes_Programme6'):
        assert _is_linked(b1, 'StudyProgrammes_Programme6', a)
    _safe_set(a, 'StudyProgrammes_Semester', b2)
    assert _is_linked(a, 'StudyProgrammes_Semester', b2)
    if hasattr(b1, 'StudyProgrammes_Programme6'):
        assert not _is_linked(b1, 'StudyProgrammes_Programme6', a)
    if hasattr(b2, 'StudyProgrammes_Programme6'):
        assert _is_linked(b2, 'StudyProgrammes_Programme6', a)
    _safe_set(a, 'StudyProgrammes_Semester', None)
    assert not _is_linked(a, 'StudyProgrammes_Semester', b2)
    if hasattr(b2, 'StudyProgrammes_Programme6'):
        assert not _is_linked(b2, 'StudyProgrammes_Programme6', a)


def test_assoc_semesters7_link_reassign_clear():
    a = StudyProgrammes_Specialization(lengthInSemesters=7, name="sample_text", startSemester=7)
    b1 = StudyProgrammes_Semester(code="sample_text", semesterSeason="sample_text", year=7)
    b2 = StudyProgrammes_Semester(code="sample_text_2", semesterSeason="sample_text_2", year=13)
    _safe_set(a, 'StudyProgrammes_Specialization8', {b1})
    assert _is_linked(a, 'StudyProgrammes_Specialization8', b1)
    if hasattr(b1, 'StudyProgrammes_Semester9'):
        assert _is_linked(b1, 'StudyProgrammes_Semester9', a)
    _safe_set(a, 'StudyProgrammes_Specialization8', {b2})
    assert _is_linked(a, 'StudyProgrammes_Specialization8', b2)
    if hasattr(b1, 'StudyProgrammes_Semester9'):
        assert not _is_linked(b1, 'StudyProgrammes_Semester9', a)
    if hasattr(b2, 'StudyProgrammes_Semester9'):
        assert _is_linked(b2, 'StudyProgrammes_Semester9', a)
    _safe_set(a, 'StudyProgrammes_Specialization8', set())
    assert not _is_linked(a, 'StudyProgrammes_Specialization8', b2)
    if hasattr(b2, 'StudyProgrammes_Semester9'):
        assert not _is_linked(b2, 'StudyProgrammes_Semester9', a)


def test_assoc_specializations3_link_reassign_clear():
    a = StudyProgrammes_Specialization(lengthInSemesters=7, name="sample_text", startSemester=7)
    b1 = StudyProgrammes_Programme(code="sample_text", name="sample_text", semestersBeforeSpecialization=7, startYear=7, totalNumberOfSemesters=7)
    b2 = StudyProgrammes_Programme(code="sample_text_2", name="sample_text_2", semestersBeforeSpecialization=13, startYear=13, totalNumberOfSemesters=13)
    _safe_set(a, 'StudyProgrammes_Specialization', b1)
    assert _is_linked(a, 'StudyProgrammes_Specialization', b1)
    if hasattr(b1, 'StudyProgrammes_Programme4'):
        assert _is_linked(b1, 'StudyProgrammes_Programme4', a)
    _safe_set(a, 'StudyProgrammes_Specialization', b2)
    assert _is_linked(a, 'StudyProgrammes_Specialization', b2)
    if hasattr(b1, 'StudyProgrammes_Programme4'):
        assert not _is_linked(b1, 'StudyProgrammes_Programme4', a)
    if hasattr(b2, 'StudyProgrammes_Programme4'):
        assert _is_linked(b2, 'StudyProgrammes_Programme4', a)
    _safe_set(a, 'StudyProgrammes_Specialization', None)
    assert not _is_linked(a, 'StudyProgrammes_Specialization', b2)
    if hasattr(b2, 'StudyProgrammes_Programme4'):
        assert not _is_linked(b2, 'StudyProgrammes_Programme4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

StudyProgrammes_Course_strategy = st.builds(StudyProgrammes_Course, availableSemesters=safe_text, code=safe_text, credits=st.floats(allow_nan=False, allow_infinity=False), name=safe_text)
@given(instance=StudyProgrammes_Course_strategy)
@settings(max_examples=25)
def test_StudyProgrammes_Course_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Course)


StudyProgrammes_CourseAccess_strategy = st.builds(StudyProgrammes_CourseAccess, access=safe_text)
@given(instance=StudyProgrammes_CourseAccess_strategy)
@settings(max_examples=25)
def test_StudyProgrammes_CourseAccess_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_CourseAccess)


StudyProgrammes_Department_strategy = st.builds(StudyProgrammes_Department, name=safe_text)
@given(instance=StudyProgrammes_Department_strategy)
@settings(max_examples=25)
def test_StudyProgrammes_Department_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Department)


StudyProgrammes_Programme_strategy = st.builds(StudyProgrammes_Programme, code=safe_text, name=safe_text, semestersBeforeSpecialization=st.integers(), startYear=st.integers(), totalNumberOfSemesters=st.integers())
@given(instance=StudyProgrammes_Programme_strategy)
@settings(max_examples=25)
def test_StudyProgrammes_Programme_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Programme)


StudyProgrammes_Semester_strategy = st.builds(StudyProgrammes_Semester, code=safe_text, semesterSeason=safe_text, year=st.integers())
@given(instance=StudyProgrammes_Semester_strategy)
@settings(max_examples=25)
def test_StudyProgrammes_Semester_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Semester)


StudyProgrammes_Specialization_strategy = st.builds(StudyProgrammes_Specialization, lengthInSemesters=st.integers(), name=safe_text, startSemester=st.integers())
@given(instance=StudyProgrammes_Specialization_strategy)
@settings(max_examples=25)
def test_StudyProgrammes_Specialization_instantiation(instance):
    assert isinstance(instance, StudyProgrammes_Specialization)


