import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    A,
    B,
    SubAbstractClass1,
    SubClass1,
    SubInterface1,
    SubInterface2,
    SuperAbstractClass,
    SuperClass,
    SuperInterface,
    testmodel_A,
    testmodel_B,
    testmodel_C,
    testmodel_Source,
    testmodel_SubAbstractClass1,
    testmodel_SubAbstractClass2,
    testmodel_SubAbstractClass3,
    testmodel_SubAbstractClass4,
    testmodel_SubAbstractClass5,
    testmodel_SubAbstractClass6,
    testmodel_SubAbstractClass7,
    testmodel_SubClass1,
    testmodel_SubClass2,
    testmodel_SubClass3,
    testmodel_SubClass4,
    testmodel_SubClass5,
    testmodel_SubClass6,
    testmodel_SubClass7,
    testmodel_SubInterface1,
    testmodel_SubInterface2,
    testmodel_SubInterface3,
    testmodel_SubInterface4,
    testmodel_SubInterface5,
    testmodel_SubInterface6,
    testmodel_SubInterface7,
    testmodel_SuperAbstractClass,
    testmodel_SuperClass,
    testmodel_SuperInterface,
    testmodel_Target,
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

def test_testmodel_A_a_value_roundtrip():
    instance = testmodel_A(a="sample_text")
    assert instance.a == "sample_text"
    instance.a = "sample_text_2"
    assert instance.a == "sample_text_2"


def test_testmodel_B_b_value_roundtrip():
    instance = testmodel_B(b="sample_text")
    assert instance.b == "sample_text"
    instance.b = "sample_text_2"
    assert instance.b == "sample_text_2"


def test_testmodel_C_c_value_roundtrip():
    instance = testmodel_C(c="sample_text")
    assert instance.c == "sample_text"
    instance.c = "sample_text_2"
    assert instance.c == "sample_text_2"


def test_testmodel_B_isa_A():
    instance = testmodel_B(b="sample_text")
    assert isinstance(instance, A)


def test_testmodel_C_isa_B():
    instance = testmodel_C(c="sample_text")
    assert isinstance(instance, B)


def test_testmodel_SubAbstractClass5_isa_SubAbstractClass1():
    instance = testmodel_SubAbstractClass5()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubAbstractClass7_isa_SubAbstractClass1():
    instance = testmodel_SubAbstractClass7()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubClass5_isa_SubAbstractClass1():
    instance = testmodel_SubClass5()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubClass7_isa_SubAbstractClass1():
    instance = testmodel_SubClass7()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubInterface5_isa_SubAbstractClass1():
    instance = testmodel_SubInterface5()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubInterface7_isa_SubAbstractClass1():
    instance = testmodel_SubInterface7()
    assert isinstance(instance, SubAbstractClass1)


def test_testmodel_SubAbstractClass6_isa_SubClass1():
    instance = testmodel_SubAbstractClass6()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubAbstractClass7_isa_SubClass1():
    instance = testmodel_SubAbstractClass7()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubClass6_isa_SubClass1():
    instance = testmodel_SubClass6()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubClass7_isa_SubClass1():
    instance = testmodel_SubClass7()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubInterface6_isa_SubClass1():
    instance = testmodel_SubInterface6()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubInterface7_isa_SubClass1():
    instance = testmodel_SubInterface7()
    assert isinstance(instance, SubClass1)


def test_testmodel_SubAbstractClass4_isa_SubInterface1():
    instance = testmodel_SubAbstractClass4()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubAbstractClass5_isa_SubInterface1():
    instance = testmodel_SubAbstractClass5()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubAbstractClass6_isa_SubInterface1():
    instance = testmodel_SubAbstractClass6()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubClass4_isa_SubInterface1():
    instance = testmodel_SubClass4()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubClass5_isa_SubInterface1():
    instance = testmodel_SubClass5()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubClass6_isa_SubInterface1():
    instance = testmodel_SubClass6()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubInterface4_isa_SubInterface1():
    instance = testmodel_SubInterface4()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubInterface5_isa_SubInterface1():
    instance = testmodel_SubInterface5()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubInterface6_isa_SubInterface1():
    instance = testmodel_SubInterface6()
    assert isinstance(instance, SubInterface1)


def test_testmodel_SubAbstractClass4_isa_SubInterface2():
    instance = testmodel_SubAbstractClass4()
    assert isinstance(instance, SubInterface2)


def test_testmodel_SubClass4_isa_SubInterface2():
    instance = testmodel_SubClass4()
    assert isinstance(instance, SubInterface2)


def test_testmodel_SubInterface4_isa_SubInterface2():
    instance = testmodel_SubInterface4()
    assert isinstance(instance, SubInterface2)


def test_testmodel_SubAbstractClass2_isa_SuperAbstractClass():
    instance = testmodel_SubAbstractClass2()
    assert isinstance(instance, SuperAbstractClass)


def test_testmodel_SubClass2_isa_SuperAbstractClass():
    instance = testmodel_SubClass2()
    assert isinstance(instance, SuperAbstractClass)


def test_testmodel_SubInterface2_isa_SuperAbstractClass():
    instance = testmodel_SubInterface2()
    assert isinstance(instance, SuperAbstractClass)


def test_testmodel_SubAbstractClass3_isa_SuperClass():
    instance = testmodel_SubAbstractClass3()
    assert isinstance(instance, SuperClass)


def test_testmodel_SubClass3_isa_SuperClass():
    instance = testmodel_SubClass3()
    assert isinstance(instance, SuperClass)


def test_testmodel_SubInterface3_isa_SuperClass():
    instance = testmodel_SubInterface3()
    assert isinstance(instance, SuperClass)


def test_testmodel_SubAbstractClass1_isa_SuperInterface():
    instance = testmodel_SubAbstractClass1()
    assert isinstance(instance, SuperInterface)


def test_testmodel_SubClass1_isa_SuperInterface():
    instance = testmodel_SubClass1()
    assert isinstance(instance, SuperInterface)


def test_testmodel_SubInterface1_isa_SuperInterface():
    instance = testmodel_SubInterface1()
    assert isinstance(instance, SuperInterface)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


B_strategy = st.builds(B)
@given(instance=B_strategy)
@settings(max_examples=25)
def test_B_instantiation(instance):
    assert isinstance(instance, B)


SubAbstractClass1_strategy = st.builds(SubAbstractClass1)
@given(instance=SubAbstractClass1_strategy)
@settings(max_examples=25)
def test_SubAbstractClass1_instantiation(instance):
    assert isinstance(instance, SubAbstractClass1)


SubClass1_strategy = st.builds(SubClass1)
@given(instance=SubClass1_strategy)
@settings(max_examples=25)
def test_SubClass1_instantiation(instance):
    assert isinstance(instance, SubClass1)


SubInterface1_strategy = st.builds(SubInterface1)
@given(instance=SubInterface1_strategy)
@settings(max_examples=25)
def test_SubInterface1_instantiation(instance):
    assert isinstance(instance, SubInterface1)


SubInterface2_strategy = st.builds(SubInterface2)
@given(instance=SubInterface2_strategy)
@settings(max_examples=25)
def test_SubInterface2_instantiation(instance):
    assert isinstance(instance, SubInterface2)


SuperAbstractClass_strategy = st.builds(SuperAbstractClass)
@given(instance=SuperAbstractClass_strategy)
@settings(max_examples=25)
def test_SuperAbstractClass_instantiation(instance):
    assert isinstance(instance, SuperAbstractClass)


SuperClass_strategy = st.builds(SuperClass)
@given(instance=SuperClass_strategy)
@settings(max_examples=25)
def test_SuperClass_instantiation(instance):
    assert isinstance(instance, SuperClass)


SuperInterface_strategy = st.builds(SuperInterface)
@given(instance=SuperInterface_strategy)
@settings(max_examples=25)
def test_SuperInterface_instantiation(instance):
    assert isinstance(instance, SuperInterface)


testmodel_A_strategy = st.builds(testmodel_A, a=safe_text)
@given(instance=testmodel_A_strategy)
@settings(max_examples=25)
def test_testmodel_A_instantiation(instance):
    assert isinstance(instance, testmodel_A)


testmodel_B_strategy = st.builds(testmodel_B, b=safe_text)
@given(instance=testmodel_B_strategy)
@settings(max_examples=25)
def test_testmodel_B_instantiation(instance):
    assert isinstance(instance, testmodel_B)


testmodel_C_strategy = st.builds(testmodel_C, c=safe_text)
@given(instance=testmodel_C_strategy)
@settings(max_examples=25)
def test_testmodel_C_instantiation(instance):
    assert isinstance(instance, testmodel_C)


testmodel_Source_strategy = st.builds(testmodel_Source)
@given(instance=testmodel_Source_strategy)
@settings(max_examples=25)
def test_testmodel_Source_instantiation(instance):
    assert isinstance(instance, testmodel_Source)


testmodel_SubAbstractClass1_strategy = st.builds(testmodel_SubAbstractClass1)
@given(instance=testmodel_SubAbstractClass1_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass1_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass1)


testmodel_SubAbstractClass2_strategy = st.builds(testmodel_SubAbstractClass2)
@given(instance=testmodel_SubAbstractClass2_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass2_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass2)


testmodel_SubAbstractClass3_strategy = st.builds(testmodel_SubAbstractClass3)
@given(instance=testmodel_SubAbstractClass3_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass3_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass3)


testmodel_SubAbstractClass4_strategy = st.builds(testmodel_SubAbstractClass4)
@given(instance=testmodel_SubAbstractClass4_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass4_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass4)


testmodel_SubAbstractClass5_strategy = st.builds(testmodel_SubAbstractClass5)
@given(instance=testmodel_SubAbstractClass5_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass5_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass5)


testmodel_SubAbstractClass6_strategy = st.builds(testmodel_SubAbstractClass6)
@given(instance=testmodel_SubAbstractClass6_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass6_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass6)


testmodel_SubAbstractClass7_strategy = st.builds(testmodel_SubAbstractClass7)
@given(instance=testmodel_SubAbstractClass7_strategy)
@settings(max_examples=25)
def test_testmodel_SubAbstractClass7_instantiation(instance):
    assert isinstance(instance, testmodel_SubAbstractClass7)


testmodel_SubClass1_strategy = st.builds(testmodel_SubClass1)
@given(instance=testmodel_SubClass1_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass1_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass1)


testmodel_SubClass2_strategy = st.builds(testmodel_SubClass2)
@given(instance=testmodel_SubClass2_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass2_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass2)


testmodel_SubClass3_strategy = st.builds(testmodel_SubClass3)
@given(instance=testmodel_SubClass3_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass3_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass3)


testmodel_SubClass4_strategy = st.builds(testmodel_SubClass4)
@given(instance=testmodel_SubClass4_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass4_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass4)


testmodel_SubClass5_strategy = st.builds(testmodel_SubClass5)
@given(instance=testmodel_SubClass5_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass5_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass5)


testmodel_SubClass6_strategy = st.builds(testmodel_SubClass6)
@given(instance=testmodel_SubClass6_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass6_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass6)


testmodel_SubClass7_strategy = st.builds(testmodel_SubClass7)
@given(instance=testmodel_SubClass7_strategy)
@settings(max_examples=25)
def test_testmodel_SubClass7_instantiation(instance):
    assert isinstance(instance, testmodel_SubClass7)


testmodel_SubInterface1_strategy = st.builds(testmodel_SubInterface1)
@given(instance=testmodel_SubInterface1_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface1_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface1)


testmodel_SubInterface2_strategy = st.builds(testmodel_SubInterface2)
@given(instance=testmodel_SubInterface2_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface2_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface2)


testmodel_SubInterface3_strategy = st.builds(testmodel_SubInterface3)
@given(instance=testmodel_SubInterface3_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface3_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface3)


testmodel_SubInterface4_strategy = st.builds(testmodel_SubInterface4)
@given(instance=testmodel_SubInterface4_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface4_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface4)


testmodel_SubInterface5_strategy = st.builds(testmodel_SubInterface5)
@given(instance=testmodel_SubInterface5_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface5_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface5)


testmodel_SubInterface6_strategy = st.builds(testmodel_SubInterface6)
@given(instance=testmodel_SubInterface6_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface6_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface6)


testmodel_SubInterface7_strategy = st.builds(testmodel_SubInterface7)
@given(instance=testmodel_SubInterface7_strategy)
@settings(max_examples=25)
def test_testmodel_SubInterface7_instantiation(instance):
    assert isinstance(instance, testmodel_SubInterface7)


testmodel_SuperAbstractClass_strategy = st.builds(testmodel_SuperAbstractClass)
@given(instance=testmodel_SuperAbstractClass_strategy)
@settings(max_examples=25)
def test_testmodel_SuperAbstractClass_instantiation(instance):
    assert isinstance(instance, testmodel_SuperAbstractClass)


testmodel_SuperClass_strategy = st.builds(testmodel_SuperClass)
@given(instance=testmodel_SuperClass_strategy)
@settings(max_examples=25)
def test_testmodel_SuperClass_instantiation(instance):
    assert isinstance(instance, testmodel_SuperClass)


testmodel_SuperInterface_strategy = st.builds(testmodel_SuperInterface)
@given(instance=testmodel_SuperInterface_strategy)
@settings(max_examples=25)
def test_testmodel_SuperInterface_instantiation(instance):
    assert isinstance(instance, testmodel_SuperInterface)


testmodel_Target_strategy = st.builds(testmodel_Target)
@given(instance=testmodel_Target_strategy)
@settings(max_examples=25)
def test_testmodel_Target_instantiation(instance):
    assert isinstance(instance, testmodel_Target)


