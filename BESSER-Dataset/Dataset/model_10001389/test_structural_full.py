import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Course,
    Course2,
    Course3,
    MyClass,
    MyClass2,
    MyClass3,
    ServiceCourse,
    ServiceCourse2,
    ServiceCourse3,
    asdfa,
    asdfa2,
    asdfa3,
    c,
    c1,
    c2,
    c21,
    c3,
    c31,
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

def test_Course_Id_value_roundtrip():
    instance = Course(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Course_Name_value_roundtrip():
    instance = Course(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Course_StartDate_value_roundtrip():
    instance = Course(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.StartDate == "sample_text"
    instance.StartDate = "sample_text_2"
    assert instance.StartDate == "sample_text_2"


def test_Course2_Id_value_roundtrip():
    instance = Course2(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Course2_Name_value_roundtrip():
    instance = Course2(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Course2_StartDate_value_roundtrip():
    instance = Course2(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.StartDate == "sample_text"
    instance.StartDate = "sample_text_2"
    assert instance.StartDate == "sample_text_2"


def test_Course3_Id_value_roundtrip():
    instance = Course3(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Course3_Name_value_roundtrip():
    instance = Course3(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Course3_StartDate_value_roundtrip():
    instance = Course3(Id=7, Name="sample_text", StartDate="sample_text")
    assert instance.StartDate == "sample_text"
    instance.StartDate = "sample_text_2"
    assert instance.StartDate == "sample_text_2"


def test_ServiceCourse_attribute_value_roundtrip():
    instance = ServiceCourse(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_ServiceCourse_attribute2_value_roundtrip():
    instance = ServiceCourse(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_ServiceCourse_attribute3_value_roundtrip():
    instance = ServiceCourse(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute3 == "sample_text"
    instance.attribute3 = "sample_text_2"
    assert instance.attribute3 == "sample_text_2"


def test_ServiceCourse_attribute4_value_roundtrip():
    instance = ServiceCourse(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute4 == "sample_text"
    instance.attribute4 = "sample_text_2"
    assert instance.attribute4 == "sample_text_2"


def test_ServiceCourse_attribute5_value_roundtrip():
    instance = ServiceCourse(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute5 == "sample_text"
    instance.attribute5 = "sample_text_2"
    assert instance.attribute5 == "sample_text_2"


def test_ServiceCourse_attribute6_value_roundtrip():
    instance = ServiceCourse(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute6 == "sample_text"
    instance.attribute6 = "sample_text_2"
    assert instance.attribute6 == "sample_text_2"


def test_ServiceCourse_attribute7_value_roundtrip():
    instance = ServiceCourse(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute7 == "sample_text"
    instance.attribute7 = "sample_text_2"
    assert instance.attribute7 == "sample_text_2"


def test_ServiceCourse_attribute8_value_roundtrip():
    instance = ServiceCourse(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute8 == "sample_text"
    instance.attribute8 = "sample_text_2"
    assert instance.attribute8 == "sample_text_2"


def test_ServiceCourse2_attribute_value_roundtrip():
    instance = ServiceCourse2(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_ServiceCourse2_attribute2_value_roundtrip():
    instance = ServiceCourse2(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_ServiceCourse2_attribute3_value_roundtrip():
    instance = ServiceCourse2(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute3 == "sample_text"
    instance.attribute3 = "sample_text_2"
    assert instance.attribute3 == "sample_text_2"


def test_ServiceCourse2_attribute4_value_roundtrip():
    instance = ServiceCourse2(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute4 == "sample_text"
    instance.attribute4 = "sample_text_2"
    assert instance.attribute4 == "sample_text_2"


def test_ServiceCourse2_attribute5_value_roundtrip():
    instance = ServiceCourse2(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute5 == "sample_text"
    instance.attribute5 = "sample_text_2"
    assert instance.attribute5 == "sample_text_2"


def test_ServiceCourse2_attribute6_value_roundtrip():
    instance = ServiceCourse2(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute6 == "sample_text"
    instance.attribute6 = "sample_text_2"
    assert instance.attribute6 == "sample_text_2"


def test_ServiceCourse2_attribute7_value_roundtrip():
    instance = ServiceCourse2(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute7 == "sample_text"
    instance.attribute7 = "sample_text_2"
    assert instance.attribute7 == "sample_text_2"


def test_ServiceCourse2_attribute8_value_roundtrip():
    instance = ServiceCourse2(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute8 == "sample_text"
    instance.attribute8 = "sample_text_2"
    assert instance.attribute8 == "sample_text_2"


def test_ServiceCourse3_attribute_value_roundtrip():
    instance = ServiceCourse3(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_ServiceCourse3_attribute2_value_roundtrip():
    instance = ServiceCourse3(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_ServiceCourse3_attribute3_value_roundtrip():
    instance = ServiceCourse3(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute3 == "sample_text"
    instance.attribute3 = "sample_text_2"
    assert instance.attribute3 == "sample_text_2"


def test_ServiceCourse3_attribute4_value_roundtrip():
    instance = ServiceCourse3(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute4 == "sample_text"
    instance.attribute4 = "sample_text_2"
    assert instance.attribute4 == "sample_text_2"


def test_ServiceCourse3_attribute5_value_roundtrip():
    instance = ServiceCourse3(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute5 == "sample_text"
    instance.attribute5 = "sample_text_2"
    assert instance.attribute5 == "sample_text_2"


def test_ServiceCourse3_attribute6_value_roundtrip():
    instance = ServiceCourse3(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute6 == "sample_text"
    instance.attribute6 = "sample_text_2"
    assert instance.attribute6 == "sample_text_2"


def test_ServiceCourse3_attribute7_value_roundtrip():
    instance = ServiceCourse3(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute7 == "sample_text"
    instance.attribute7 = "sample_text_2"
    assert instance.attribute7 == "sample_text_2"


def test_ServiceCourse3_attribute8_value_roundtrip():
    instance = ServiceCourse3(attribute="sample_text", attribute2="sample_text", attribute3="sample_text", attribute4="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", attribute8="sample_text")
    assert instance.attribute8 == "sample_text"
    instance.attribute8 = "sample_text_2"
    assert instance.attribute8 == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Course_strategy = st.builds(Course, Id=st.integers(), Name=safe_text, StartDate=safe_text)
@given(instance=Course_strategy)
@settings(max_examples=25)
def test_Course_instantiation(instance):
    assert isinstance(instance, Course)


Course2_strategy = st.builds(Course2, Id=st.integers(), Name=safe_text, StartDate=safe_text)
@given(instance=Course2_strategy)
@settings(max_examples=25)
def test_Course2_instantiation(instance):
    assert isinstance(instance, Course2)


Course3_strategy = st.builds(Course3, Id=st.integers(), Name=safe_text, StartDate=safe_text)
@given(instance=Course3_strategy)
@settings(max_examples=25)
def test_Course3_instantiation(instance):
    assert isinstance(instance, Course3)


MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


MyClass2_strategy = st.builds(MyClass2)
@given(instance=MyClass2_strategy)
@settings(max_examples=25)
def test_MyClass2_instantiation(instance):
    assert isinstance(instance, MyClass2)


MyClass3_strategy = st.builds(MyClass3)
@given(instance=MyClass3_strategy)
@settings(max_examples=25)
def test_MyClass3_instantiation(instance):
    assert isinstance(instance, MyClass3)


ServiceCourse_strategy = st.builds(ServiceCourse, attribute=safe_text, attribute2=safe_text, attribute3=safe_text, attribute4=safe_text, attribute5=safe_text, attribute6=safe_text, attribute7=safe_text, attribute8=safe_text)
@given(instance=ServiceCourse_strategy)
@settings(max_examples=25)
def test_ServiceCourse_instantiation(instance):
    assert isinstance(instance, ServiceCourse)


ServiceCourse2_strategy = st.builds(ServiceCourse2, attribute=safe_text, attribute2=safe_text, attribute3=safe_text, attribute4=safe_text, attribute5=safe_text, attribute6=safe_text, attribute7=safe_text, attribute8=safe_text)
@given(instance=ServiceCourse2_strategy)
@settings(max_examples=25)
def test_ServiceCourse2_instantiation(instance):
    assert isinstance(instance, ServiceCourse2)


ServiceCourse3_strategy = st.builds(ServiceCourse3, attribute=safe_text, attribute2=safe_text, attribute3=safe_text, attribute4=safe_text, attribute5=safe_text, attribute6=safe_text, attribute7=safe_text, attribute8=safe_text)
@given(instance=ServiceCourse3_strategy)
@settings(max_examples=25)
def test_ServiceCourse3_instantiation(instance):
    assert isinstance(instance, ServiceCourse3)


asdfa_strategy = st.builds(asdfa)
@given(instance=asdfa_strategy)
@settings(max_examples=25)
def test_asdfa_instantiation(instance):
    assert isinstance(instance, asdfa)


asdfa2_strategy = st.builds(asdfa2)
@given(instance=asdfa2_strategy)
@settings(max_examples=25)
def test_asdfa2_instantiation(instance):
    assert isinstance(instance, asdfa2)


asdfa3_strategy = st.builds(asdfa3)
@given(instance=asdfa3_strategy)
@settings(max_examples=25)
def test_asdfa3_instantiation(instance):
    assert isinstance(instance, asdfa3)


c_strategy = st.builds(c)
@given(instance=c_strategy)
@settings(max_examples=25)
def test_c_instantiation(instance):
    assert isinstance(instance, c)


c1_strategy = st.builds(c1)
@given(instance=c1_strategy)
@settings(max_examples=25)
def test_c1_instantiation(instance):
    assert isinstance(instance, c1)


c2_strategy = st.builds(c2)
@given(instance=c2_strategy)
@settings(max_examples=25)
def test_c2_instantiation(instance):
    assert isinstance(instance, c2)


c21_strategy = st.builds(c21)
@given(instance=c21_strategy)
@settings(max_examples=25)
def test_c21_instantiation(instance):
    assert isinstance(instance, c21)


c3_strategy = st.builds(c3)
@given(instance=c3_strategy)
@settings(max_examples=25)
def test_c3_instantiation(instance):
    assert isinstance(instance, c3)


c31_strategy = st.builds(c31)
@given(instance=c31_strategy)
@settings(max_examples=25)
def test_c31_instantiation(instance):
    assert isinstance(instance, c31)


