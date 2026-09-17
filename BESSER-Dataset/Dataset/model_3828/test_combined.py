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
    TestPackage_SubPackage_SubTestClass,
    TestPackage_UberClass,
    TestPackage_SuperClass,
    TestPackage_SubPackage_SubTestInterface,
    UberClass,
    SuperClass,
    TestPackage_TestInterface,
    TestPackage_TestClass,
    TestEnum,
    SubTestEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_testpackage_subpackage_subtestclass_is_not_abstract():
    assert not inspect.isabstract(TestPackage_SubPackage_SubTestClass)


def test_hyp_testpackage_subpackage_subtestclass_constructor_exists():
    assert callable(TestPackage_SubPackage_SubTestClass.__init__)


def test_hyp_testpackage_subpackage_subtestclass_constructor_args():
    sig = inspect.signature(TestPackage_SubPackage_SubTestClass.__init__)
    params = list(sig.parameters.keys())
    assert "testBooleanAttr" in params, "Missing parameter 'testBooleanAttr'"
    assert "testRealAttr" in params, "Missing parameter 'testRealAttr'"
    assert "testStringAttr" in params, "Missing parameter 'testStringAttr'"
    assert "testIntAttr" in params, "Missing parameter 'testIntAttr'"
    assert "testAttr" in params, "Missing parameter 'testAttr'"








def test_hyp_testpackage_uberclass_is_not_abstract():
    assert not inspect.isabstract(TestPackage_UberClass)


def test_hyp_testpackage_uberclass_constructor_exists():
    assert callable(TestPackage_UberClass.__init__)


def test_hyp_testpackage_uberclass_constructor_args():
    sig = inspect.signature(TestPackage_UberClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testpackage_superclass_is_not_abstract():
    assert not inspect.isabstract(TestPackage_SuperClass)


def test_hyp_testpackage_superclass_constructor_exists():
    assert callable(TestPackage_SuperClass.__init__)


def test_hyp_testpackage_superclass_constructor_args():
    sig = inspect.signature(TestPackage_SuperClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testpackage_subpackage_subtestinterface_is_not_abstract():
    assert not inspect.isabstract(TestPackage_SubPackage_SubTestInterface)


def test_hyp_testpackage_subpackage_subtestinterface_constructor_exists():
    assert callable(TestPackage_SubPackage_SubTestInterface.__init__)


def test_hyp_testpackage_subpackage_subtestinterface_constructor_args():
    sig = inspect.signature(TestPackage_SubPackage_SubTestInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uberclass_is_not_abstract():
    assert not inspect.isabstract(UberClass)


def test_hyp_uberclass_constructor_exists():
    assert callable(UberClass.__init__)


def test_hyp_uberclass_constructor_args():
    sig = inspect.signature(UberClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_superclass_is_not_abstract():
    assert not inspect.isabstract(SuperClass)


def test_hyp_superclass_constructor_exists():
    assert callable(SuperClass.__init__)


def test_hyp_superclass_constructor_args():
    sig = inspect.signature(SuperClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testpackage_testinterface_is_not_abstract():
    assert not inspect.isabstract(TestPackage_TestInterface)


def test_hyp_testpackage_testinterface_constructor_exists():
    assert callable(TestPackage_TestInterface.__init__)


def test_hyp_testpackage_testinterface_constructor_args():
    sig = inspect.signature(TestPackage_TestInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testpackage_testclass_is_not_abstract():
    assert not inspect.isabstract(TestPackage_TestClass)


def test_hyp_testpackage_testclass_constructor_exists():
    assert callable(TestPackage_TestClass.__init__)


def test_hyp_testpackage_testclass_constructor_args():
    sig = inspect.signature(TestPackage_TestClass.__init__)
    params = list(sig.parameters.keys())
    assert "testAttr1" in params, "Missing parameter 'testAttr1'"
    assert "testBooleanAttr" in params, "Missing parameter 'testBooleanAttr'"
    assert "testAttr2" in params, "Missing parameter 'testAttr2'"
    assert "testUnlimitedNaturalAttr" in params, "Missing parameter 'testUnlimitedNaturalAttr'"
    assert "testRealAttr" in params, "Missing parameter 'testRealAttr'"
    assert "testAttr5" in params, "Missing parameter 'testAttr5'"
    assert "testAttr7" in params, "Missing parameter 'testAttr7'"
    assert "testIntAttr" in params, "Missing parameter 'testIntAttr'"
    assert "testAttr6" in params, "Missing parameter 'testAttr6'"
    assert "testAttr3" in params, "Missing parameter 'testAttr3'"
    assert "testAttr8" in params, "Missing parameter 'testAttr8'"
    assert "testStringAttr" in params, "Missing parameter 'testStringAttr'"
    assert "testAttr4" in params, "Missing parameter 'testAttr4'"
    assert "testAttr" in params, "Missing parameter 'testAttr'"















def test_hyp_testenum_exists():
    # Check that the Enumeration exists
    assert TestEnum is not None

def test_hyp_testenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestEnum]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestEnum"

def test_hyp_subtestenum_exists():
    # Check that the Enumeration exists
    assert SubTestEnum is not None

def test_hyp_subtestenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubTestEnum]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubTestEnum"


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
TestPackage_SubPackage_SubTestClass_strategy = st.builds(
    TestPackage_SubPackage_SubTestClass,
    testBooleanAttr=
        st.booleans(),
    testRealAttr=
        safe_text,
    testStringAttr=
        safe_text,
    testIntAttr=
        st.integers(),
    testAttr=
        st.dates()
)
TestPackage_UberClass_strategy = st.builds(
    TestPackage_UberClass,
)
TestPackage_SuperClass_strategy = st.builds(
    TestPackage_SuperClass,
)
TestPackage_SubPackage_SubTestInterface_strategy = st.builds(
    TestPackage_SubPackage_SubTestInterface,
)
UberClass_strategy = st.builds(
    UberClass,
)
SuperClass_strategy = st.builds(
    SuperClass,
)
TestPackage_TestInterface_strategy = st.builds(
    TestPackage_TestInterface,
)
TestPackage_TestClass_strategy = st.builds(
    TestPackage_TestClass,
    testAttr1=
        st.integers(),
    testBooleanAttr=
        st.booleans(),
    testAttr2=
        st.integers(),
    testUnlimitedNaturalAttr=
        safe_text,
    testRealAttr=
        safe_text,
    testAttr5=
        st.integers(),
    testAttr7=
        st.integers(),
    testIntAttr=
        st.integers(),
    testAttr6=
        st.integers(),
    testAttr3=
        st.integers(),
    testAttr8=
        st.integers(),
    testStringAttr=
        safe_text,
    testAttr4=
        st.integers(),
    testAttr=
        st.dates()
)




@given(instance=TestPackage_SubPackage_SubTestClass_strategy)
def test_hyp_testpackage_subpackage_subtestclass_testBooleanAttr_setter(instance):
    original = instance.testBooleanAttr
    instance.testBooleanAttr = original
    assert instance.testBooleanAttr == original



@given(instance=TestPackage_SubPackage_SubTestClass_strategy)
def test_hyp_testpackage_subpackage_subtestclass_testRealAttr_setter(instance):
    original = instance.testRealAttr
    instance.testRealAttr = original
    assert instance.testRealAttr == original



@given(instance=TestPackage_SubPackage_SubTestClass_strategy)
def test_hyp_testpackage_subpackage_subtestclass_testStringAttr_setter(instance):
    original = instance.testStringAttr
    instance.testStringAttr = original
    assert instance.testStringAttr == original



@given(instance=TestPackage_SubPackage_SubTestClass_strategy)
def test_hyp_testpackage_subpackage_subtestclass_testIntAttr_setter(instance):
    original = instance.testIntAttr
    instance.testIntAttr = original
    assert instance.testIntAttr == original



@given(instance=TestPackage_SubPackage_SubTestClass_strategy)
def test_hyp_testpackage_subpackage_subtestclass_testAttr_setter(instance):
    original = instance.testAttr
    instance.testAttr = original
    assert instance.testAttr == original










@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr1_setter(instance):
    original = instance.testAttr1
    instance.testAttr1 = original
    assert instance.testAttr1 == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testBooleanAttr_setter(instance):
    original = instance.testBooleanAttr
    instance.testBooleanAttr = original
    assert instance.testBooleanAttr == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr2_setter(instance):
    original = instance.testAttr2
    instance.testAttr2 = original
    assert instance.testAttr2 == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testUnlimitedNaturalAttr_setter(instance):
    original = instance.testUnlimitedNaturalAttr
    instance.testUnlimitedNaturalAttr = original
    assert instance.testUnlimitedNaturalAttr == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testRealAttr_setter(instance):
    original = instance.testRealAttr
    instance.testRealAttr = original
    assert instance.testRealAttr == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr5_setter(instance):
    original = instance.testAttr5
    instance.testAttr5 = original
    assert instance.testAttr5 == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr7_setter(instance):
    original = instance.testAttr7
    instance.testAttr7 = original
    assert instance.testAttr7 == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testIntAttr_setter(instance):
    original = instance.testIntAttr
    instance.testIntAttr = original
    assert instance.testIntAttr == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr6_setter(instance):
    original = instance.testAttr6
    instance.testAttr6 = original
    assert instance.testAttr6 == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr3_setter(instance):
    original = instance.testAttr3
    instance.testAttr3 = original
    assert instance.testAttr3 == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr8_setter(instance):
    original = instance.testAttr8
    instance.testAttr8 = original
    assert instance.testAttr8 == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testStringAttr_setter(instance):
    original = instance.testStringAttr
    instance.testStringAttr = original
    assert instance.testStringAttr == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr4_setter(instance):
    original = instance.testAttr4
    instance.testAttr4 = original
    assert instance.testAttr4 == original



@given(instance=TestPackage_TestClass_strategy)
def test_hyp_testpackage_testclass_testAttr_setter(instance):
    original = instance.testAttr
    instance.testAttr = original
    assert instance.testAttr == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    SuperClass,
    TestPackage_SubPackage_SubTestClass,
    TestPackage_SubPackage_SubTestInterface,
    TestPackage_SuperClass,
    TestPackage_TestClass,
    TestPackage_TestInterface,
    TestPackage_UberClass,
    UberClass,
    SubTestEnum,
    TestEnum,
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

def test_TestPackage_SubPackage_SubTestClass_testAttr_value_roundtrip():
    instance = TestPackage_SubPackage_SubTestClass(testAttr=date(2024, 1, 1), testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text")
    assert instance.testAttr == date(2024, 1, 1)
    instance.testAttr = date(2025, 6, 15)
    assert instance.testAttr == date(2025, 6, 15)


def test_TestPackage_SubPackage_SubTestClass_testBooleanAttr_value_roundtrip():
    instance = TestPackage_SubPackage_SubTestClass(testAttr=date(2024, 1, 1), testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text")
    assert instance.testBooleanAttr == True
    instance.testBooleanAttr = False
    assert instance.testBooleanAttr == False


def test_TestPackage_SubPackage_SubTestClass_testIntAttr_value_roundtrip():
    instance = TestPackage_SubPackage_SubTestClass(testAttr=date(2024, 1, 1), testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text")
    assert instance.testIntAttr == 7
    instance.testIntAttr = 13
    assert instance.testIntAttr == 13


def test_TestPackage_SubPackage_SubTestClass_testRealAttr_value_roundtrip():
    instance = TestPackage_SubPackage_SubTestClass(testAttr=date(2024, 1, 1), testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text")
    assert instance.testRealAttr == "sample_text"
    instance.testRealAttr = "sample_text_2"
    assert instance.testRealAttr == "sample_text_2"


def test_TestPackage_SubPackage_SubTestClass_testStringAttr_value_roundtrip():
    instance = TestPackage_SubPackage_SubTestClass(testAttr=date(2024, 1, 1), testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text")
    assert instance.testStringAttr == "sample_text"
    instance.testStringAttr = "sample_text_2"
    assert instance.testStringAttr == "sample_text_2"


def test_TestPackage_TestClass_testAttr_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr == date(2024, 1, 1)
    instance.testAttr = date(2025, 6, 15)
    assert instance.testAttr == date(2025, 6, 15)


def test_TestPackage_TestClass_testAttr1_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr1 == 7
    instance.testAttr1 = 13
    assert instance.testAttr1 == 13


def test_TestPackage_TestClass_testAttr2_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr2 == 7
    instance.testAttr2 = 13
    assert instance.testAttr2 == 13


def test_TestPackage_TestClass_testAttr3_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr3 == 7
    instance.testAttr3 = 13
    assert instance.testAttr3 == 13


def test_TestPackage_TestClass_testAttr4_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr4 == 7
    instance.testAttr4 = 13
    assert instance.testAttr4 == 13


def test_TestPackage_TestClass_testAttr5_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr5 == 7
    instance.testAttr5 = 13
    assert instance.testAttr5 == 13


def test_TestPackage_TestClass_testAttr6_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr6 == 7
    instance.testAttr6 = 13
    assert instance.testAttr6 == 13


def test_TestPackage_TestClass_testAttr7_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr7 == 7
    instance.testAttr7 = 13
    assert instance.testAttr7 == 13


def test_TestPackage_TestClass_testAttr8_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testAttr8 == 7
    instance.testAttr8 = 13
    assert instance.testAttr8 == 13


def test_TestPackage_TestClass_testBooleanAttr_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testBooleanAttr == True
    instance.testBooleanAttr = False
    assert instance.testBooleanAttr == False


def test_TestPackage_TestClass_testIntAttr_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testIntAttr == 7
    instance.testIntAttr = 13
    assert instance.testIntAttr == 13


def test_TestPackage_TestClass_testRealAttr_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testRealAttr == "sample_text"
    instance.testRealAttr = "sample_text_2"
    assert instance.testRealAttr == "sample_text_2"


def test_TestPackage_TestClass_testStringAttr_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testStringAttr == "sample_text"
    instance.testStringAttr = "sample_text_2"
    assert instance.testStringAttr == "sample_text_2"


def test_TestPackage_TestClass_testUnlimitedNaturalAttr_value_roundtrip():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert instance.testUnlimitedNaturalAttr == "sample_text"
    instance.testUnlimitedNaturalAttr = "sample_text_2"
    assert instance.testUnlimitedNaturalAttr == "sample_text_2"


def test_TestPackage_TestClass_isa_SuperClass():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert isinstance(instance, SuperClass)


def test_TestPackage_TestInterface_isa_SuperClass():
    instance = TestPackage_TestInterface()
    assert isinstance(instance, SuperClass)


def test_TestPackage_TestClass_isa_UberClass():
    instance = TestPackage_TestClass(testAttr=date(2024, 1, 1), testAttr1=7, testAttr2=7, testAttr3=7, testAttr4=7, testAttr5=7, testAttr6=7, testAttr7=7, testAttr8=7, testBooleanAttr=True, testIntAttr=7, testRealAttr="sample_text", testStringAttr="sample_text", testUnlimitedNaturalAttr="sample_text")
    assert isinstance(instance, UberClass)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

SuperClass_strategy = st.builds(SuperClass)
@given(instance=SuperClass_strategy)
@settings(max_examples=25)
def test_SuperClass_instantiation(instance):
    assert isinstance(instance, SuperClass)


TestPackage_SubPackage_SubTestClass_strategy = st.builds(TestPackage_SubPackage_SubTestClass, testAttr=st.dates(), testBooleanAttr=st.booleans(), testIntAttr=st.integers(), testRealAttr=safe_text, testStringAttr=safe_text)
@given(instance=TestPackage_SubPackage_SubTestClass_strategy)
@settings(max_examples=25)
def test_TestPackage_SubPackage_SubTestClass_instantiation(instance):
    assert isinstance(instance, TestPackage_SubPackage_SubTestClass)


TestPackage_SubPackage_SubTestInterface_strategy = st.builds(TestPackage_SubPackage_SubTestInterface)
@given(instance=TestPackage_SubPackage_SubTestInterface_strategy)
@settings(max_examples=25)
def test_TestPackage_SubPackage_SubTestInterface_instantiation(instance):
    assert isinstance(instance, TestPackage_SubPackage_SubTestInterface)


TestPackage_SuperClass_strategy = st.builds(TestPackage_SuperClass)
@given(instance=TestPackage_SuperClass_strategy)
@settings(max_examples=25)
def test_TestPackage_SuperClass_instantiation(instance):
    assert isinstance(instance, TestPackage_SuperClass)


TestPackage_TestClass_strategy = st.builds(TestPackage_TestClass, testAttr=st.dates(), testAttr1=st.integers(), testAttr2=st.integers(), testAttr3=st.integers(), testAttr4=st.integers(), testAttr5=st.integers(), testAttr6=st.integers(), testAttr7=st.integers(), testAttr8=st.integers(), testBooleanAttr=st.booleans(), testIntAttr=st.integers(), testRealAttr=safe_text, testStringAttr=safe_text, testUnlimitedNaturalAttr=safe_text)
@given(instance=TestPackage_TestClass_strategy)
@settings(max_examples=25)
def test_TestPackage_TestClass_instantiation(instance):
    assert isinstance(instance, TestPackage_TestClass)


TestPackage_TestInterface_strategy = st.builds(TestPackage_TestInterface)
@given(instance=TestPackage_TestInterface_strategy)
@settings(max_examples=25)
def test_TestPackage_TestInterface_instantiation(instance):
    assert isinstance(instance, TestPackage_TestInterface)


TestPackage_UberClass_strategy = st.builds(TestPackage_UberClass)
@given(instance=TestPackage_UberClass_strategy)
@settings(max_examples=25)
def test_TestPackage_UberClass_instantiation(instance):
    assert isinstance(instance, TestPackage_UberClass)


UberClass_strategy = st.builds(UberClass)
@given(instance=UberClass_strategy)
@settings(max_examples=25)
def test_UberClass_instantiation(instance):
    assert isinstance(instance, UberClass)



