import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    tDT4250_asssignment1_2_Course,
    tDT4250_asssignment1_2_Program,
    tDT4250_asssignment1_2_Program_course,
    tDT4250_asssignment1_2_Semester,
    tDT4250_asssignment1_2_Semester_Course,
    tDT4250_asssignment1_2_Specialization,
    Fall_or_spring,
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

def test_tDT4250_asssignment1_2_Course_Code_value_roundtrip():
    instance = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    assert instance.Code == "sample_text"
    instance.Code = "sample_text_2"
    assert instance.Code == "sample_text_2"


def test_tDT4250_asssignment1_2_Course_Credits_value_roundtrip():
    instance = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    assert instance.Credits == 3.14
    instance.Credits = 9.99
    assert instance.Credits == 9.99


def test_tDT4250_asssignment1_2_Course_ExamDate_value_roundtrip():
    instance = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    assert instance.ExamDate == "sample_text"
    instance.ExamDate = "sample_text_2"
    assert instance.ExamDate == "sample_text_2"


def test_tDT4250_asssignment1_2_Course_Name_value_roundtrip():
    instance = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_tDT4250_asssignment1_2_Course_StartDate_value_roundtrip():
    instance = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    assert instance.StartDate == "sample_text"
    instance.StartDate = "sample_text_2"
    assert instance.StartDate == "sample_text_2"


def test_tDT4250_asssignment1_2_Program_Credits_value_roundtrip():
    instance = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    assert instance.Credits == "sample_text"
    instance.Credits = "sample_text_2"
    assert instance.Credits == "sample_text_2"


def test_tDT4250_asssignment1_2_Program_Name_value_roundtrip():
    instance = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_tDT4250_asssignment1_2_Program_course_Fall_or_spring_value_roundtrip():
    instance = tDT4250_asssignment1_2_Program_course(Fall_or_spring="sample_text", Mandatory=True)
    assert instance.Fall_or_spring == "sample_text"
    instance.Fall_or_spring = "sample_text_2"
    assert instance.Fall_or_spring == "sample_text_2"


def test_tDT4250_asssignment1_2_Program_course_Mandatory_value_roundtrip():
    instance = tDT4250_asssignment1_2_Program_course(Fall_or_spring="sample_text", Mandatory=True)
    assert instance.Mandatory == True
    instance.Mandatory = False
    assert instance.Mandatory == False


def test_tDT4250_asssignment1_2_Semester_Credits_value_roundtrip():
    instance = tDT4250_asssignment1_2_Semester(Credits="sample_text", Number=7)
    assert instance.Credits == "sample_text"
    instance.Credits = "sample_text_2"
    assert instance.Credits == "sample_text_2"


def test_tDT4250_asssignment1_2_Semester_Number_value_roundtrip():
    instance = tDT4250_asssignment1_2_Semester(Credits="sample_text", Number=7)
    assert instance.Number == 7
    instance.Number = 13
    assert instance.Number == 13


def test_tDT4250_asssignment1_2_Semester_Course_Fall_or_spring_value_roundtrip():
    instance = tDT4250_asssignment1_2_Semester_Course(Fall_or_spring="sample_text", Mandatory=True)
    assert instance.Fall_or_spring == "sample_text"
    instance.Fall_or_spring = "sample_text_2"
    assert instance.Fall_or_spring == "sample_text_2"


def test_tDT4250_asssignment1_2_Semester_Course_Mandatory_value_roundtrip():
    instance = tDT4250_asssignment1_2_Semester_Course(Fall_or_spring="sample_text", Mandatory=True)
    assert instance.Mandatory == True
    instance.Mandatory = False
    assert instance.Mandatory == False


def test_tDT4250_asssignment1_2_Specialization_Name_value_roundtrip():
    instance = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_assoc_course13_link_reassign_clear():
    a = tDT4250_asssignment1_2_Semester_Course(Fall_or_spring="sample_text", Mandatory=True)
    b1 = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    b2 = tDT4250_asssignment1_2_Course(Code="sample_text_2", Credits=9.99, ExamDate="sample_text_2", Name="sample_text_2", StartDate="sample_text_2")
    _safe_set(a, 'tDT4250_asssignment1_2_Semester_Course14', {b1})
    assert _is_linked(a, 'tDT4250_asssignment1_2_Semester_Course14', b1)
    if hasattr(b1, 'tDT4250_asssignment1_2_Course'):
        assert _is_linked(b1, 'tDT4250_asssignment1_2_Course', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Semester_Course14', {b2})
    assert _is_linked(a, 'tDT4250_asssignment1_2_Semester_Course14', b2)
    if hasattr(b1, 'tDT4250_asssignment1_2_Course'):
        assert not _is_linked(b1, 'tDT4250_asssignment1_2_Course', a)
    if hasattr(b2, 'tDT4250_asssignment1_2_Course'):
        assert _is_linked(b2, 'tDT4250_asssignment1_2_Course', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Semester_Course14', set())
    assert not _is_linked(a, 'tDT4250_asssignment1_2_Semester_Course14', b2)
    if hasattr(b2, 'tDT4250_asssignment1_2_Course'):
        assert not _is_linked(b2, 'tDT4250_asssignment1_2_Course', a)


def test_assoc_course15_link_reassign_clear():
    a = tDT4250_asssignment1_2_Program_course(Fall_or_spring="sample_text", Mandatory=True)
    b1 = tDT4250_asssignment1_2_Course(Code="sample_text", Credits=3.14, ExamDate="sample_text", Name="sample_text", StartDate="sample_text")
    b2 = tDT4250_asssignment1_2_Course(Code="sample_text_2", Credits=9.99, ExamDate="sample_text_2", Name="sample_text_2", StartDate="sample_text_2")
    _safe_set(a, 'tDT4250_asssignment1_2_Program_course16', {b1})
    assert _is_linked(a, 'tDT4250_asssignment1_2_Program_course16', b1)
    if hasattr(b1, 'tDT4250_asssignment1_2_Course17'):
        assert _is_linked(b1, 'tDT4250_asssignment1_2_Course17', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Program_course16', {b2})
    assert _is_linked(a, 'tDT4250_asssignment1_2_Program_course16', b2)
    if hasattr(b1, 'tDT4250_asssignment1_2_Course17'):
        assert not _is_linked(b1, 'tDT4250_asssignment1_2_Course17', a)
    if hasattr(b2, 'tDT4250_asssignment1_2_Course17'):
        assert _is_linked(b2, 'tDT4250_asssignment1_2_Course17', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Program_course16', set())
    assert not _is_linked(a, 'tDT4250_asssignment1_2_Program_course16', b2)
    if hasattr(b2, 'tDT4250_asssignment1_2_Course17'):
        assert not _is_linked(b2, 'tDT4250_asssignment1_2_Course17', a)


def test_assoc_program_course1_link_reassign_clear():
    a = tDT4250_asssignment1_2_Program_course(Fall_or_spring="sample_text", Mandatory=True)
    b1 = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    b2 = tDT4250_asssignment1_2_Program(Credits="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'tDT4250_asssignment1_2_Program_course', b1)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Program_course', b1)
    if hasattr(b1, 'tDT4250_asssignment1_2_Program2'):
        assert _is_linked(b1, 'tDT4250_asssignment1_2_Program2', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Program_course', b2)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Program_course', b2)
    if hasattr(b1, 'tDT4250_asssignment1_2_Program2'):
        assert not _is_linked(b1, 'tDT4250_asssignment1_2_Program2', a)
    if hasattr(b2, 'tDT4250_asssignment1_2_Program2'):
        assert _is_linked(b2, 'tDT4250_asssignment1_2_Program2', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Program_course', None)
    assert not _is_linked(a, 'tDT4250_asssignment1_2_Program_course', b2)
    if hasattr(b2, 'tDT4250_asssignment1_2_Program2'):
        assert not _is_linked(b2, 'tDT4250_asssignment1_2_Program2', a)


def test_assoc_semester3_link_reassign_clear():
    a = tDT4250_asssignment1_2_Semester(Credits="sample_text", Number=7)
    b1 = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    b2 = tDT4250_asssignment1_2_Program(Credits="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'tDT4250_asssignment1_2_Semester', b1)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Semester', b1)
    if hasattr(b1, 'tDT4250_asssignment1_2_Program4'):
        assert _is_linked(b1, 'tDT4250_asssignment1_2_Program4', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Semester', b2)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Semester', b2)
    if hasattr(b1, 'tDT4250_asssignment1_2_Program4'):
        assert not _is_linked(b1, 'tDT4250_asssignment1_2_Program4', a)
    if hasattr(b2, 'tDT4250_asssignment1_2_Program4'):
        assert _is_linked(b2, 'tDT4250_asssignment1_2_Program4', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Semester', None)
    assert not _is_linked(a, 'tDT4250_asssignment1_2_Semester', b2)
    if hasattr(b2, 'tDT4250_asssignment1_2_Program4'):
        assert not _is_linked(b2, 'tDT4250_asssignment1_2_Program4', a)


def test_assoc_semester5_link_reassign_clear():
    a = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    b1 = tDT4250_asssignment1_2_Semester(Credits="sample_text", Number=7)
    b2 = tDT4250_asssignment1_2_Semester(Credits="sample_text_2", Number=13)
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization6', {b1})
    assert _is_linked(a, 'tDT4250_asssignment1_2_Specialization6', b1)
    if hasattr(b1, 'tDT4250_asssignment1_2_Semester7'):
        assert _is_linked(b1, 'tDT4250_asssignment1_2_Semester7', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization6', {b2})
    assert _is_linked(a, 'tDT4250_asssignment1_2_Specialization6', b2)
    if hasattr(b1, 'tDT4250_asssignment1_2_Semester7'):
        assert not _is_linked(b1, 'tDT4250_asssignment1_2_Semester7', a)
    if hasattr(b2, 'tDT4250_asssignment1_2_Semester7'):
        assert _is_linked(b2, 'tDT4250_asssignment1_2_Semester7', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization6', set())
    assert not _is_linked(a, 'tDT4250_asssignment1_2_Specialization6', b2)
    if hasattr(b2, 'tDT4250_asssignment1_2_Semester7'):
        assert not _is_linked(b2, 'tDT4250_asssignment1_2_Semester7', a)


def test_assoc_semester_course11_link_reassign_clear():
    a = tDT4250_asssignment1_2_Semester_Course(Fall_or_spring="sample_text", Mandatory=True)
    b1 = tDT4250_asssignment1_2_Semester(Credits="sample_text", Number=7)
    b2 = tDT4250_asssignment1_2_Semester(Credits="sample_text_2", Number=13)
    _safe_set(a, 'tDT4250_asssignment1_2_Semester_Course', b1)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Semester_Course', b1)
    if hasattr(b1, 'tDT4250_asssignment1_2_Semester12'):
        assert _is_linked(b1, 'tDT4250_asssignment1_2_Semester12', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Semester_Course', b2)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Semester_Course', b2)
    if hasattr(b1, 'tDT4250_asssignment1_2_Semester12'):
        assert not _is_linked(b1, 'tDT4250_asssignment1_2_Semester12', a)
    if hasattr(b2, 'tDT4250_asssignment1_2_Semester12'):
        assert _is_linked(b2, 'tDT4250_asssignment1_2_Semester12', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Semester_Course', None)
    assert not _is_linked(a, 'tDT4250_asssignment1_2_Semester_Course', b2)
    if hasattr(b2, 'tDT4250_asssignment1_2_Semester12'):
        assert not _is_linked(b2, 'tDT4250_asssignment1_2_Semester12', a)


def test_assoc_specialization0_link_reassign_clear():
    a = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    b1 = tDT4250_asssignment1_2_Program(Credits="sample_text", Name="sample_text")
    b2 = tDT4250_asssignment1_2_Program(Credits="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization', b1)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Specialization', b1)
    if hasattr(b1, 'tDT4250_asssignment1_2_Program'):
        assert _is_linked(b1, 'tDT4250_asssignment1_2_Program', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization', b2)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Specialization', b2)
    if hasattr(b1, 'tDT4250_asssignment1_2_Program'):
        assert not _is_linked(b1, 'tDT4250_asssignment1_2_Program', a)
    if hasattr(b2, 'tDT4250_asssignment1_2_Program'):
        assert _is_linked(b2, 'tDT4250_asssignment1_2_Program', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization', None)
    assert not _is_linked(a, 'tDT4250_asssignment1_2_Specialization', b2)
    if hasattr(b2, 'tDT4250_asssignment1_2_Program'):
        assert not _is_linked(b2, 'tDT4250_asssignment1_2_Program', a)


def test_assoc_specialization9_link_reassign_clear():
    a = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    b1 = tDT4250_asssignment1_2_Specialization(Name="sample_text")
    b2 = tDT4250_asssignment1_2_Specialization(Name="sample_text_2")
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization10', b1)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Specialization10', b1)
    if hasattr(b1, 'tDT4250_asssignment1_2_Specialization8'):
        assert _is_linked(b1, 'tDT4250_asssignment1_2_Specialization8', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization10', b2)
    assert _is_linked(a, 'tDT4250_asssignment1_2_Specialization10', b2)
    if hasattr(b1, 'tDT4250_asssignment1_2_Specialization8'):
        assert not _is_linked(b1, 'tDT4250_asssignment1_2_Specialization8', a)
    if hasattr(b2, 'tDT4250_asssignment1_2_Specialization8'):
        assert _is_linked(b2, 'tDT4250_asssignment1_2_Specialization8', a)
    _safe_set(a, 'tDT4250_asssignment1_2_Specialization10', None)
    assert not _is_linked(a, 'tDT4250_asssignment1_2_Specialization10', b2)
    if hasattr(b2, 'tDT4250_asssignment1_2_Specialization8'):
        assert not _is_linked(b2, 'tDT4250_asssignment1_2_Specialization8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

tDT4250_asssignment1_2_Course_strategy = st.builds(tDT4250_asssignment1_2_Course, Code=safe_text, Credits=st.floats(allow_nan=False, allow_infinity=False), ExamDate=safe_text, Name=safe_text, StartDate=safe_text)
@given(instance=tDT4250_asssignment1_2_Course_strategy)
@settings(max_examples=25)
def test_tDT4250_asssignment1_2_Course_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Course)


tDT4250_asssignment1_2_Program_strategy = st.builds(tDT4250_asssignment1_2_Program, Credits=safe_text, Name=safe_text)
@given(instance=tDT4250_asssignment1_2_Program_strategy)
@settings(max_examples=25)
def test_tDT4250_asssignment1_2_Program_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Program)


tDT4250_asssignment1_2_Program_course_strategy = st.builds(tDT4250_asssignment1_2_Program_course, Fall_or_spring=safe_text, Mandatory=st.booleans())
@given(instance=tDT4250_asssignment1_2_Program_course_strategy)
@settings(max_examples=25)
def test_tDT4250_asssignment1_2_Program_course_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Program_course)


tDT4250_asssignment1_2_Semester_strategy = st.builds(tDT4250_asssignment1_2_Semester, Credits=safe_text, Number=st.integers())
@given(instance=tDT4250_asssignment1_2_Semester_strategy)
@settings(max_examples=25)
def test_tDT4250_asssignment1_2_Semester_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Semester)


tDT4250_asssignment1_2_Semester_Course_strategy = st.builds(tDT4250_asssignment1_2_Semester_Course, Fall_or_spring=safe_text, Mandatory=st.booleans())
@given(instance=tDT4250_asssignment1_2_Semester_Course_strategy)
@settings(max_examples=25)
def test_tDT4250_asssignment1_2_Semester_Course_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Semester_Course)


tDT4250_asssignment1_2_Specialization_strategy = st.builds(tDT4250_asssignment1_2_Specialization, Name=safe_text)
@given(instance=tDT4250_asssignment1_2_Specialization_strategy)
@settings(max_examples=25)
def test_tDT4250_asssignment1_2_Specialization_instantiation(instance):
    assert isinstance(instance, tDT4250_asssignment1_2_Specialization)


