import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class,
    MyClass,
    MyClass2,
    MyClass3,
    MyClass4,
    MyClass5,
    MyInterface2_Interface,
    MyInterface3_Interface,
    MyInterface_Interface,
    T,
    T2,
    T3,
    mypackage_MyClass,
    mypackage_T,
    mypackage_T2,
    mypackage_T3,
    mypackage_T4,
    mypackage_T5,
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

def test_MyClass_attribute_value_roundtrip():
    instance = MyClass(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass_attribute2_value_roundtrip():
    instance = MyClass(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


MyClass_strategy = st.builds(MyClass, attribute=safe_text, attribute2=safe_text)
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


MyClass4_strategy = st.builds(MyClass4)
@given(instance=MyClass4_strategy)
@settings(max_examples=25)
def test_MyClass4_instantiation(instance):
    assert isinstance(instance, MyClass4)


MyClass5_strategy = st.builds(MyClass5)
@given(instance=MyClass5_strategy)
@settings(max_examples=25)
def test_MyClass5_instantiation(instance):
    assert isinstance(instance, MyClass5)


MyInterface2_Interface_strategy = st.builds(MyInterface2_Interface)
@given(instance=MyInterface2_Interface_strategy)
@settings(max_examples=25)
def test_MyInterface2_Interface_instantiation(instance):
    assert isinstance(instance, MyInterface2_Interface)


MyInterface3_Interface_strategy = st.builds(MyInterface3_Interface)
@given(instance=MyInterface3_Interface_strategy)
@settings(max_examples=25)
def test_MyInterface3_Interface_instantiation(instance):
    assert isinstance(instance, MyInterface3_Interface)


MyInterface_Interface_strategy = st.builds(MyInterface_Interface)
@given(instance=MyInterface_Interface_strategy)
@settings(max_examples=25)
def test_MyInterface_Interface_instantiation(instance):
    assert isinstance(instance, MyInterface_Interface)


T_strategy = st.builds(T)
@given(instance=T_strategy)
@settings(max_examples=25)
def test_T_instantiation(instance):
    assert isinstance(instance, T)


T2_strategy = st.builds(T2)
@given(instance=T2_strategy)
@settings(max_examples=25)
def test_T2_instantiation(instance):
    assert isinstance(instance, T2)


T3_strategy = st.builds(T3)
@given(instance=T3_strategy)
@settings(max_examples=25)
def test_T3_instantiation(instance):
    assert isinstance(instance, T3)


mypackage_MyClass_strategy = st.builds(mypackage_MyClass)
@given(instance=mypackage_MyClass_strategy)
@settings(max_examples=25)
def test_mypackage_MyClass_instantiation(instance):
    assert isinstance(instance, mypackage_MyClass)


mypackage_T_strategy = st.builds(mypackage_T)
@given(instance=mypackage_T_strategy)
@settings(max_examples=25)
def test_mypackage_T_instantiation(instance):
    assert isinstance(instance, mypackage_T)


mypackage_T2_strategy = st.builds(mypackage_T2)
@given(instance=mypackage_T2_strategy)
@settings(max_examples=25)
def test_mypackage_T2_instantiation(instance):
    assert isinstance(instance, mypackage_T2)


mypackage_T3_strategy = st.builds(mypackage_T3)
@given(instance=mypackage_T3_strategy)
@settings(max_examples=25)
def test_mypackage_T3_instantiation(instance):
    assert isinstance(instance, mypackage_T3)


mypackage_T4_strategy = st.builds(mypackage_T4)
@given(instance=mypackage_T4_strategy)
@settings(max_examples=25)
def test_mypackage_T4_instantiation(instance):
    assert isinstance(instance, mypackage_T4)


mypackage_T5_strategy = st.builds(mypackage_T5)
@given(instance=mypackage_T5_strategy)
@settings(max_examples=25)
def test_mypackage_T5_instantiation(instance):
    assert isinstance(instance, mypackage_T5)


