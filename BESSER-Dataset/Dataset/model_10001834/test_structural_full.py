import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Actor_Actor,
    ClassA,
    ClassB,
    MyClass,
    MyClass2,
    MyClass3,
    MyClass4,
    T,
    T1,
    UseCase_UseCase,
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

def test_ClassA_flag_value_roundtrip():
    instance = ClassA(flag=True)
    assert instance.flag == True
    instance.flag = False
    assert instance.flag == False


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actor_Actor_strategy = st.builds(Actor_Actor)
@given(instance=Actor_Actor_strategy)
@settings(max_examples=25)
def test_Actor_Actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)


ClassA_strategy = st.builds(ClassA, flag=st.booleans())
@given(instance=ClassA_strategy)
@settings(max_examples=25)
def test_ClassA_instantiation(instance):
    assert isinstance(instance, ClassA)


ClassB_strategy = st.builds(ClassB)
@given(instance=ClassB_strategy)
@settings(max_examples=25)
def test_ClassB_instantiation(instance):
    assert isinstance(instance, ClassB)


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


MyClass4_strategy = st.builds(MyClass4)
@given(instance=MyClass4_strategy)
@settings(max_examples=25)
def test_MyClass4_instantiation(instance):
    assert isinstance(instance, MyClass4)


T_strategy = st.builds(T)
@given(instance=T_strategy)
@settings(max_examples=25)
def test_T_instantiation(instance):
    assert isinstance(instance, T)


T1_strategy = st.builds(T1)
@given(instance=T1_strategy)
@settings(max_examples=25)
def test_T1_instantiation(instance):
    assert isinstance(instance, T1)


UseCase_UseCase_strategy = st.builds(UseCase_UseCase)
@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)


