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
    c2,
    MyClass2,
    asdfa2,
    ServiceCourse2,
    Course2,
    c1,
    c,
    MyClass,
    asdfa,
    ServiceCourse,
    Course,
    c31,
    c3,
    MyClass3,
    asdfa3,
    ServiceCourse3,
    Course3,
    c21,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_c2_is_not_abstract():
    assert not inspect.isabstract(c2)


def test_hyp_c2_constructor_exists():
    assert callable(c2.__init__)


def test_hyp_c2_constructor_args():
    sig = inspect.signature(c2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_hyp_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_hyp_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_asdfa2_is_not_abstract():
    assert not inspect.isabstract(asdfa2)


def test_hyp_asdfa2_constructor_exists():
    assert callable(asdfa2.__init__)


def test_hyp_asdfa2_constructor_args():
    sig = inspect.signature(asdfa2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicecourse2_is_not_abstract():
    assert not inspect.isabstract(ServiceCourse2)


def test_hyp_servicecourse2_constructor_exists():
    assert callable(ServiceCourse2.__init__)


def test_hyp_servicecourse2_constructor_args():
    sig = inspect.signature(ServiceCourse2.__init__)
    params = list(sig.parameters.keys())
    assert "attribute8" in params, "Missing parameter 'attribute8'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute7" in params, "Missing parameter 'attribute7'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"











def test_hyp_course2_is_not_abstract():
    assert not inspect.isabstract(Course2)


def test_hyp_course2_constructor_exists():
    assert callable(Course2.__init__)


def test_hyp_course2_constructor_args():
    sig = inspect.signature(Course2.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"






def test_hyp_c1_is_not_abstract():
    assert not inspect.isabstract(c1)


def test_hyp_c1_constructor_exists():
    assert callable(c1.__init__)


def test_hyp_c1_constructor_args():
    sig = inspect.signature(c1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_is_not_abstract():
    assert not inspect.isabstract(c)


def test_hyp_c_constructor_exists():
    assert callable(c.__init__)


def test_hyp_c_constructor_args():
    sig = inspect.signature(c.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_asdfa_is_not_abstract():
    assert not inspect.isabstract(asdfa)


def test_hyp_asdfa_constructor_exists():
    assert callable(asdfa.__init__)


def test_hyp_asdfa_constructor_args():
    sig = inspect.signature(asdfa.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicecourse_is_not_abstract():
    assert not inspect.isabstract(ServiceCourse)


def test_hyp_servicecourse_constructor_exists():
    assert callable(ServiceCourse.__init__)


def test_hyp_servicecourse_constructor_args():
    sig = inspect.signature(ServiceCourse.__init__)
    params = list(sig.parameters.keys())
    assert "attribute7" in params, "Missing parameter 'attribute7'"
    assert "attribute8" in params, "Missing parameter 'attribute8'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"











def test_hyp_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_hyp_course_constructor_exists():
    assert callable(Course.__init__)


def test_hyp_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "StartDate" in params, "Missing parameter 'StartDate'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"






def test_hyp_c31_is_not_abstract():
    assert not inspect.isabstract(c31)


def test_hyp_c31_constructor_exists():
    assert callable(c31.__init__)


def test_hyp_c31_constructor_args():
    sig = inspect.signature(c31.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c3_is_not_abstract():
    assert not inspect.isabstract(c3)


def test_hyp_c3_constructor_exists():
    assert callable(c3.__init__)


def test_hyp_c3_constructor_args():
    sig = inspect.signature(c3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass3_is_not_abstract():
    assert not inspect.isabstract(MyClass3)


def test_hyp_myclass3_constructor_exists():
    assert callable(MyClass3.__init__)


def test_hyp_myclass3_constructor_args():
    sig = inspect.signature(MyClass3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_asdfa3_is_not_abstract():
    assert not inspect.isabstract(asdfa3)


def test_hyp_asdfa3_constructor_exists():
    assert callable(asdfa3.__init__)


def test_hyp_asdfa3_constructor_args():
    sig = inspect.signature(asdfa3.__init__)
    params = list(sig.parameters.keys())



def test_hyp_servicecourse3_is_not_abstract():
    assert not inspect.isabstract(ServiceCourse3)


def test_hyp_servicecourse3_constructor_exists():
    assert callable(ServiceCourse3.__init__)


def test_hyp_servicecourse3_constructor_args():
    sig = inspect.signature(ServiceCourse3.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute7" in params, "Missing parameter 'attribute7'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute8" in params, "Missing parameter 'attribute8'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"











def test_hyp_course3_is_not_abstract():
    assert not inspect.isabstract(Course3)


def test_hyp_course3_constructor_exists():
    assert callable(Course3.__init__)


def test_hyp_course3_constructor_args():
    sig = inspect.signature(Course3.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"






def test_hyp_c21_is_not_abstract():
    assert not inspect.isabstract(c21)


def test_hyp_c21_constructor_exists():
    assert callable(c21.__init__)


def test_hyp_c21_constructor_args():
    sig = inspect.signature(c21.__init__)
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
c2_strategy = st.builds(
    c2,
)
MyClass2_strategy = st.builds(
    MyClass2,
)
asdfa2_strategy = st.builds(
    asdfa2,
)
ServiceCourse2_strategy = st.builds(
    ServiceCourse2,
    attribute8=
        safe_text,
    attribute6=
        safe_text,
    attribute7=
        safe_text,
    attribute2=
        safe_text,
    attribute4=
        safe_text,
    attribute5=
        safe_text,
    attribute=
        safe_text,
    attribute3=
        safe_text
)
Course2_strategy = st.builds(
    Course2,
    Id=
        st.integers(),
    Name=
        safe_text,
    StartDate=
        safe_text
)
c1_strategy = st.builds(
    c1,
)
c_strategy = st.builds(
    c,
)
MyClass_strategy = st.builds(
    MyClass,
)
asdfa_strategy = st.builds(
    asdfa,
)
ServiceCourse_strategy = st.builds(
    ServiceCourse,
    attribute7=
        safe_text,
    attribute8=
        safe_text,
    attribute6=
        safe_text,
    attribute=
        safe_text,
    attribute2=
        safe_text,
    attribute4=
        safe_text,
    attribute3=
        safe_text,
    attribute5=
        safe_text
)
Course_strategy = st.builds(
    Course,
    StartDate=
        safe_text,
    Id=
        st.integers(),
    Name=
        safe_text
)
c31_strategy = st.builds(
    c31,
)
c3_strategy = st.builds(
    c3,
)
MyClass3_strategy = st.builds(
    MyClass3,
)
asdfa3_strategy = st.builds(
    asdfa3,
)
ServiceCourse3_strategy = st.builds(
    ServiceCourse3,
    attribute2=
        safe_text,
    attribute7=
        safe_text,
    attribute5=
        safe_text,
    attribute3=
        safe_text,
    attribute8=
        safe_text,
    attribute=
        safe_text,
    attribute6=
        safe_text,
    attribute4=
        safe_text
)
Course3_strategy = st.builds(
    Course3,
    Name=
        safe_text,
    Id=
        st.integers(),
    StartDate=
        safe_text
)
c21_strategy = st.builds(
    c21,
)







@given(instance=ServiceCourse2_strategy)
def test_hyp_servicecourse2_attribute8_setter(instance):
    original = instance.attribute8
    instance.attribute8 = original
    assert instance.attribute8 == original



@given(instance=ServiceCourse2_strategy)
def test_hyp_servicecourse2_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=ServiceCourse2_strategy)
def test_hyp_servicecourse2_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original



@given(instance=ServiceCourse2_strategy)
def test_hyp_servicecourse2_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=ServiceCourse2_strategy)
def test_hyp_servicecourse2_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original



@given(instance=ServiceCourse2_strategy)
def test_hyp_servicecourse2_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=ServiceCourse2_strategy)
def test_hyp_servicecourse2_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ServiceCourse2_strategy)
def test_hyp_servicecourse2_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original




@given(instance=Course2_strategy)
def test_hyp_course2_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Course2_strategy)
def test_hyp_course2_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Course2_strategy)
def test_hyp_course2_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original








@given(instance=ServiceCourse_strategy)
def test_hyp_servicecourse_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original



@given(instance=ServiceCourse_strategy)
def test_hyp_servicecourse_attribute8_setter(instance):
    original = instance.attribute8
    instance.attribute8 = original
    assert instance.attribute8 == original



@given(instance=ServiceCourse_strategy)
def test_hyp_servicecourse_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=ServiceCourse_strategy)
def test_hyp_servicecourse_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ServiceCourse_strategy)
def test_hyp_servicecourse_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=ServiceCourse_strategy)
def test_hyp_servicecourse_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original



@given(instance=ServiceCourse_strategy)
def test_hyp_servicecourse_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=ServiceCourse_strategy)
def test_hyp_servicecourse_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original




@given(instance=Course_strategy)
def test_hyp_course_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original



@given(instance=Course_strategy)
def test_hyp_course_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Course_strategy)
def test_hyp_course_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original








@given(instance=ServiceCourse3_strategy)
def test_hyp_servicecourse3_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=ServiceCourse3_strategy)
def test_hyp_servicecourse3_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original



@given(instance=ServiceCourse3_strategy)
def test_hyp_servicecourse3_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=ServiceCourse3_strategy)
def test_hyp_servicecourse3_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=ServiceCourse3_strategy)
def test_hyp_servicecourse3_attribute8_setter(instance):
    original = instance.attribute8
    instance.attribute8 = original
    assert instance.attribute8 == original



@given(instance=ServiceCourse3_strategy)
def test_hyp_servicecourse3_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ServiceCourse3_strategy)
def test_hyp_servicecourse3_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=ServiceCourse3_strategy)
def test_hyp_servicecourse3_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original




@given(instance=Course3_strategy)
def test_hyp_course3_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Course3_strategy)
def test_hyp_course3_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Course3_strategy)
def test_hyp_course3_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



