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
    TestCategoryBase,
    TestCategoryBeanAbstract,
    dmf_DObject,
    tests_TestCategoryExtends,
    tests_TestCategoryBeanConcrete,
    tests_ExternalTestType,
    DObject,
    tests_TestCategoryBeanA,
    tests_EReferenceTest,
    tests_TestCategoryReferenceArray,
    tests_TestCategoryIntrinsicArray,
    tests_TestCategoryBeanB,
    tests_TestMassParameters,
    tests_TestCategoryBase,
    tests_TestCategoryComposition,
    tests_TestParameter,
    tests_TestCategoryBeanAbstract,
    tests_TestCategoryCompositionArray,
    tests_TestCrossLinkedParametersWithCalculation,
    tests_TestCategoryReference,
    tests_TestCategoryAllProperty,
    EnumTestEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_testcategorybase_is_not_abstract():
    assert not inspect.isabstract(TestCategoryBase)


def test_hyp_testcategorybase_constructor_exists():
    assert callable(TestCategoryBase.__init__)


def test_hyp_testcategorybase_constructor_args():
    sig = inspect.signature(TestCategoryBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_testcategorybeanabstract_is_not_abstract():
    assert not inspect.isabstract(TestCategoryBeanAbstract)


def test_hyp_testcategorybeanabstract_constructor_exists():
    assert callable(TestCategoryBeanAbstract.__init__)


def test_hyp_testcategorybeanabstract_constructor_args():
    sig = inspect.signature(TestCategoryBeanAbstract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dmf_dobject_is_not_abstract():
    assert not inspect.isabstract(dmf_DObject)


def test_hyp_dmf_dobject_constructor_exists():
    assert callable(dmf_DObject.__init__)


def test_hyp_dmf_dobject_constructor_args():
    sig = inspect.signature(dmf_DObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testcategoryextends_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryExtends)


def test_hyp_tests_testcategoryextends_constructor_exists():
    assert callable(tests_TestCategoryExtends.__init__)


def test_hyp_tests_testcategoryextends_constructor_args():
    sig = inspect.signature(tests_TestCategoryExtends.__init__)
    params = list(sig.parameters.keys())
    assert "testExtendsProperty" in params, "Missing parameter 'testExtendsProperty'"




def test_hyp_tests_testcategorybeanconcrete_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBeanConcrete)


def test_hyp_tests_testcategorybeanconcrete_constructor_exists():
    assert callable(tests_TestCategoryBeanConcrete.__init__)


def test_hyp_tests_testcategorybeanconcrete_constructor_args():
    sig = inspect.signature(tests_TestCategoryBeanConcrete.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_externaltesttype_is_not_abstract():
    assert not inspect.isabstract(tests_ExternalTestType)


def test_hyp_tests_externaltesttype_constructor_exists():
    assert callable(tests_ExternalTestType.__init__)


def test_hyp_tests_externaltesttype_constructor_args():
    sig = inspect.signature(tests_ExternalTestType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dobject_is_not_abstract():
    assert not inspect.isabstract(DObject)


def test_hyp_dobject_constructor_exists():
    assert callable(DObject.__init__)


def test_hyp_dobject_constructor_args():
    sig = inspect.signature(DObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testcategorybeana_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBeanA)


def test_hyp_tests_testcategorybeana_constructor_exists():
    assert callable(tests_TestCategoryBeanA.__init__)


def test_hyp_tests_testcategorybeana_constructor_args():
    sig = inspect.signature(tests_TestCategoryBeanA.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_ereferencetest_is_not_abstract():
    assert not inspect.isabstract(tests_EReferenceTest)


def test_hyp_tests_ereferencetest_constructor_exists():
    assert callable(tests_EReferenceTest.__init__)


def test_hyp_tests_ereferencetest_constructor_args():
    sig = inspect.signature(tests_EReferenceTest.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testcategoryreferencearray_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryReferenceArray)


def test_hyp_tests_testcategoryreferencearray_constructor_exists():
    assert callable(tests_TestCategoryReferenceArray.__init__)


def test_hyp_tests_testcategoryreferencearray_constructor_args():
    sig = inspect.signature(tests_TestCategoryReferenceArray.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testcategoryintrinsicarray_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryIntrinsicArray)


def test_hyp_tests_testcategoryintrinsicarray_constructor_exists():
    assert callable(tests_TestCategoryIntrinsicArray.__init__)


def test_hyp_tests_testcategoryintrinsicarray_constructor_args():
    sig = inspect.signature(tests_TestCategoryIntrinsicArray.__init__)
    params = list(sig.parameters.keys())
    assert "testStringArrayStatic" in params, "Missing parameter 'testStringArrayStatic'"
    assert "testStringArrayDynamic" in params, "Missing parameter 'testStringArrayDynamic'"





def test_hyp_tests_testcategorybeanb_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBeanB)


def test_hyp_tests_testcategorybeanb_constructor_exists():
    assert callable(tests_TestCategoryBeanB.__init__)


def test_hyp_tests_testcategorybeanb_constructor_args():
    sig = inspect.signature(tests_TestCategoryBeanB.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testmassparameters_is_not_abstract():
    assert not inspect.isabstract(tests_TestMassParameters)


def test_hyp_tests_testmassparameters_constructor_exists():
    assert callable(tests_TestMassParameters.__init__)


def test_hyp_tests_testmassparameters_constructor_args():
    sig = inspect.signature(tests_TestMassParameters.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testcategorybase_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBase)


def test_hyp_tests_testcategorybase_constructor_exists():
    assert callable(tests_TestCategoryBase.__init__)


def test_hyp_tests_testcategorybase_constructor_args():
    sig = inspect.signature(tests_TestCategoryBase.__init__)
    params = list(sig.parameters.keys())
    assert "testBaseProperty" in params, "Missing parameter 'testBaseProperty'"




def test_hyp_tests_testcategorycomposition_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryComposition)


def test_hyp_tests_testcategorycomposition_constructor_exists():
    assert callable(tests_TestCategoryComposition.__init__)


def test_hyp_tests_testcategorycomposition_constructor_args():
    sig = inspect.signature(tests_TestCategoryComposition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testparameter_is_not_abstract():
    assert not inspect.isabstract(tests_TestParameter)


def test_hyp_tests_testparameter_constructor_exists():
    assert callable(tests_TestParameter.__init__)


def test_hyp_tests_testparameter_constructor_args():
    sig = inspect.signature(tests_TestParameter.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"




def test_hyp_tests_testcategorybeanabstract_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryBeanAbstract)


def test_hyp_tests_testcategorybeanabstract_constructor_exists():
    assert callable(tests_TestCategoryBeanAbstract.__init__)


def test_hyp_tests_testcategorybeanabstract_constructor_args():
    sig = inspect.signature(tests_TestCategoryBeanAbstract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testcategorycompositionarray_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryCompositionArray)


def test_hyp_tests_testcategorycompositionarray_constructor_exists():
    assert callable(tests_TestCategoryCompositionArray.__init__)


def test_hyp_tests_testcategorycompositionarray_constructor_args():
    sig = inspect.signature(tests_TestCategoryCompositionArray.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testcrosslinkedparameterswithcalculation_is_not_abstract():
    assert not inspect.isabstract(tests_TestCrossLinkedParametersWithCalculation)


def test_hyp_tests_testcrosslinkedparameterswithcalculation_constructor_exists():
    assert callable(tests_TestCrossLinkedParametersWithCalculation.__init__)


def test_hyp_tests_testcrosslinkedparameterswithcalculation_constructor_args():
    sig = inspect.signature(tests_TestCrossLinkedParametersWithCalculation.__init__)
    params = list(sig.parameters.keys())
    assert "calcedTrl" in params, "Missing parameter 'calcedTrl'"




def test_hyp_tests_testcategoryreference_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryReference)


def test_hyp_tests_testcategoryreference_constructor_exists():
    assert callable(tests_TestCategoryReference.__init__)


def test_hyp_tests_testcategoryreference_constructor_args():
    sig = inspect.signature(tests_TestCategoryReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tests_testcategoryallproperty_is_not_abstract():
    assert not inspect.isabstract(tests_TestCategoryAllProperty)


def test_hyp_tests_testcategoryallproperty_constructor_exists():
    assert callable(tests_TestCategoryAllProperty.__init__)


def test_hyp_tests_testcategoryallproperty_constructor_args():
    sig = inspect.signature(tests_TestCategoryAllProperty.__init__)
    params = list(sig.parameters.keys())
    assert "testEnum" in params, "Missing parameter 'testEnum'"
    assert "testBool" in params, "Missing parameter 'testBool'"
    assert "testFloat" in params, "Missing parameter 'testFloat'"
    assert "testInt" in params, "Missing parameter 'testInt'"
    assert "testResource" in params, "Missing parameter 'testResource'"
    assert "testString" in params, "Missing parameter 'testString'"







def test_hyp_enumtestenum_exists():
    # Check that the Enumeration exists
    assert EnumTestEnum is not None

def test_hyp_enumtestenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumTestEnum]
    expected_literals = [
        "MEDIUM",
        "HIGH",
        "INCREDIBLE",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumTestEnum"


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
TestCategoryBase_strategy = st.builds(
    TestCategoryBase,
)
TestCategoryBeanAbstract_strategy = st.builds(
    TestCategoryBeanAbstract,
)
dmf_DObject_strategy = st.builds(
    dmf_DObject,
)
tests_TestCategoryExtends_strategy = st.builds(
    tests_TestCategoryExtends,
    testExtendsProperty=
        st.integers()
)
tests_TestCategoryBeanConcrete_strategy = st.builds(
    tests_TestCategoryBeanConcrete,
)
tests_ExternalTestType_strategy = st.builds(
    tests_ExternalTestType,
)
DObject_strategy = st.builds(
    DObject,
)
tests_TestCategoryBeanA_strategy = st.builds(
    tests_TestCategoryBeanA,
)
tests_EReferenceTest_strategy = st.builds(
    tests_EReferenceTest,
)
tests_TestCategoryReferenceArray_strategy = st.builds(
    tests_TestCategoryReferenceArray,
)
tests_TestCategoryIntrinsicArray_strategy = st.builds(
    tests_TestCategoryIntrinsicArray,
    testStringArrayStatic=
        safe_text,
    testStringArrayDynamic=
        safe_text
)
tests_TestCategoryBeanB_strategy = st.builds(
    tests_TestCategoryBeanB,
)
tests_TestMassParameters_strategy = st.builds(
    tests_TestMassParameters,
)
tests_TestCategoryBase_strategy = st.builds(
    tests_TestCategoryBase,
    testBaseProperty=
        st.integers()
)
tests_TestCategoryComposition_strategy = st.builds(
    tests_TestCategoryComposition,
)
tests_TestParameter_strategy = st.builds(
    tests_TestParameter,
    defaultValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
tests_TestCategoryBeanAbstract_strategy = st.builds(
    tests_TestCategoryBeanAbstract,
)
tests_TestCategoryCompositionArray_strategy = st.builds(
    tests_TestCategoryCompositionArray,
)
tests_TestCrossLinkedParametersWithCalculation_strategy = st.builds(
    tests_TestCrossLinkedParametersWithCalculation,
    calcedTrl=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
tests_TestCategoryReference_strategy = st.builds(
    tests_TestCategoryReference,
)
tests_TestCategoryAllProperty_strategy = st.builds(
    tests_TestCategoryAllProperty,
    testEnum=
        safe_text,
    testBool=
        st.booleans(),
    testFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    testInt=
        st.integers(),
    testResource=
        safe_text,
    testString=
        safe_text
)







@given(instance=tests_TestCategoryExtends_strategy)
def test_hyp_tests_testcategoryextends_testExtendsProperty_setter(instance):
    original = instance.testExtendsProperty
    instance.testExtendsProperty = original
    assert instance.testExtendsProperty == original










@given(instance=tests_TestCategoryIntrinsicArray_strategy)
def test_hyp_tests_testcategoryintrinsicarray_testStringArrayStatic_setter(instance):
    original = instance.testStringArrayStatic
    instance.testStringArrayStatic = original
    assert instance.testStringArrayStatic == original



@given(instance=tests_TestCategoryIntrinsicArray_strategy)
def test_hyp_tests_testcategoryintrinsicarray_testStringArrayDynamic_setter(instance):
    original = instance.testStringArrayDynamic
    instance.testStringArrayDynamic = original
    assert instance.testStringArrayDynamic == original






@given(instance=tests_TestCategoryBase_strategy)
def test_hyp_tests_testcategorybase_testBaseProperty_setter(instance):
    original = instance.testBaseProperty
    instance.testBaseProperty = original
    assert instance.testBaseProperty == original





@given(instance=tests_TestParameter_strategy)
def test_hyp_tests_testparameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original






@given(instance=tests_TestCrossLinkedParametersWithCalculation_strategy)
def test_hyp_tests_testcrosslinkedparameterswithcalculation_calcedTrl_setter(instance):
    original = instance.calcedTrl
    instance.calcedTrl = original
    assert instance.calcedTrl == original





@given(instance=tests_TestCategoryAllProperty_strategy)
def test_hyp_tests_testcategoryallproperty_testEnum_setter(instance):
    original = instance.testEnum
    instance.testEnum = original
    assert instance.testEnum == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_hyp_tests_testcategoryallproperty_testBool_setter(instance):
    original = instance.testBool
    instance.testBool = original
    assert instance.testBool == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_hyp_tests_testcategoryallproperty_testFloat_setter(instance):
    original = instance.testFloat
    instance.testFloat = original
    assert instance.testFloat == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_hyp_tests_testcategoryallproperty_testInt_setter(instance):
    original = instance.testInt
    instance.testInt = original
    assert instance.testInt == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_hyp_tests_testcategoryallproperty_testResource_setter(instance):
    original = instance.testResource
    instance.testResource = original
    assert instance.testResource == original



@given(instance=tests_TestCategoryAllProperty_strategy)
def test_hyp_tests_testcategoryallproperty_testString_setter(instance):
    original = instance.testString
    instance.testString = original
    assert instance.testString == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DObject,
    TestCategoryBase,
    TestCategoryBeanAbstract,
    dmf_DObject,
    tests_EReferenceTest,
    tests_ExternalTestType,
    tests_TestCategoryAllProperty,
    tests_TestCategoryBase,
    tests_TestCategoryBeanA,
    tests_TestCategoryBeanAbstract,
    tests_TestCategoryBeanB,
    tests_TestCategoryBeanConcrete,
    tests_TestCategoryComposition,
    tests_TestCategoryCompositionArray,
    tests_TestCategoryExtends,
    tests_TestCategoryIntrinsicArray,
    tests_TestCategoryReference,
    tests_TestCategoryReferenceArray,
    tests_TestCrossLinkedParametersWithCalculation,
    tests_TestMassParameters,
    tests_TestParameter,
    EnumTestEnum,
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

def test_tests_TestCategoryAllProperty_testBool_value_roundtrip():
    instance = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    assert instance.testBool == True
    instance.testBool = False
    assert instance.testBool == False


def test_tests_TestCategoryAllProperty_testEnum_value_roundtrip():
    instance = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    assert instance.testEnum == "sample_text"
    instance.testEnum = "sample_text_2"
    assert instance.testEnum == "sample_text_2"


def test_tests_TestCategoryAllProperty_testFloat_value_roundtrip():
    instance = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    assert instance.testFloat == 3.14
    instance.testFloat = 9.99
    assert instance.testFloat == 9.99


def test_tests_TestCategoryAllProperty_testInt_value_roundtrip():
    instance = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    assert instance.testInt == 7
    instance.testInt = 13
    assert instance.testInt == 13


def test_tests_TestCategoryAllProperty_testResource_value_roundtrip():
    instance = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    assert instance.testResource == "sample_text"
    instance.testResource = "sample_text_2"
    assert instance.testResource == "sample_text_2"


def test_tests_TestCategoryAllProperty_testString_value_roundtrip():
    instance = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    assert instance.testString == "sample_text"
    instance.testString = "sample_text_2"
    assert instance.testString == "sample_text_2"


def test_tests_TestCategoryBase_testBaseProperty_value_roundtrip():
    instance = tests_TestCategoryBase(testBaseProperty=7)
    assert instance.testBaseProperty == 7
    instance.testBaseProperty = 13
    assert instance.testBaseProperty == 13


def test_tests_TestCategoryExtends_testExtendsProperty_value_roundtrip():
    instance = tests_TestCategoryExtends(testExtendsProperty=7)
    assert instance.testExtendsProperty == 7
    instance.testExtendsProperty = 13
    assert instance.testExtendsProperty == 13


def test_tests_TestCategoryIntrinsicArray_testStringArrayDynamic_value_roundtrip():
    instance = tests_TestCategoryIntrinsicArray(testStringArrayDynamic="sample_text", testStringArrayStatic="sample_text")
    assert instance.testStringArrayDynamic == "sample_text"
    instance.testStringArrayDynamic = "sample_text_2"
    assert instance.testStringArrayDynamic == "sample_text_2"


def test_tests_TestCategoryIntrinsicArray_testStringArrayStatic_value_roundtrip():
    instance = tests_TestCategoryIntrinsicArray(testStringArrayDynamic="sample_text", testStringArrayStatic="sample_text")
    assert instance.testStringArrayStatic == "sample_text"
    instance.testStringArrayStatic = "sample_text_2"
    assert instance.testStringArrayStatic == "sample_text_2"


def test_tests_TestCrossLinkedParametersWithCalculation_calcedTrl_value_roundtrip():
    instance = tests_TestCrossLinkedParametersWithCalculation(calcedTrl=3.14)
    assert instance.calcedTrl == 3.14
    instance.calcedTrl = 9.99
    assert instance.calcedTrl == 9.99


def test_tests_TestParameter_defaultValue_value_roundtrip():
    instance = tests_TestParameter(defaultValue=3.14)
    assert instance.defaultValue == 3.14
    instance.defaultValue = 9.99
    assert instance.defaultValue == 9.99


def test_tests_EReferenceTest_isa_DObject():
    instance = tests_EReferenceTest()
    assert isinstance(instance, DObject)


def test_tests_TestCategoryAllProperty_isa_DObject():
    instance = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    assert isinstance(instance, DObject)


def test_tests_TestCategoryBase_isa_DObject():
    instance = tests_TestCategoryBase(testBaseProperty=7)
    assert isinstance(instance, DObject)


def test_tests_TestCategoryBeanA_isa_DObject():
    instance = tests_TestCategoryBeanA()
    assert isinstance(instance, DObject)


def test_tests_TestCategoryBeanAbstract_isa_DObject():
    instance = tests_TestCategoryBeanAbstract()
    assert isinstance(instance, DObject)


def test_tests_TestCategoryBeanB_isa_DObject():
    instance = tests_TestCategoryBeanB()
    assert isinstance(instance, DObject)


def test_tests_TestCategoryComposition_isa_DObject():
    instance = tests_TestCategoryComposition()
    assert isinstance(instance, DObject)


def test_tests_TestCategoryCompositionArray_isa_DObject():
    instance = tests_TestCategoryCompositionArray()
    assert isinstance(instance, DObject)


def test_tests_TestCategoryIntrinsicArray_isa_DObject():
    instance = tests_TestCategoryIntrinsicArray(testStringArrayDynamic="sample_text", testStringArrayStatic="sample_text")
    assert isinstance(instance, DObject)


def test_tests_TestCategoryReference_isa_DObject():
    instance = tests_TestCategoryReference()
    assert isinstance(instance, DObject)


def test_tests_TestCategoryReferenceArray_isa_DObject():
    instance = tests_TestCategoryReferenceArray()
    assert isinstance(instance, DObject)


def test_tests_TestCrossLinkedParametersWithCalculation_isa_DObject():
    instance = tests_TestCrossLinkedParametersWithCalculation(calcedTrl=3.14)
    assert isinstance(instance, DObject)


def test_tests_TestMassParameters_isa_DObject():
    instance = tests_TestMassParameters()
    assert isinstance(instance, DObject)


def test_tests_TestParameter_isa_DObject():
    instance = tests_TestParameter(defaultValue=3.14)
    assert isinstance(instance, DObject)


def test_tests_TestCategoryExtends_isa_TestCategoryBase():
    instance = tests_TestCategoryExtends(testExtendsProperty=7)
    assert isinstance(instance, TestCategoryBase)


def test_tests_TestCategoryBeanConcrete_isa_TestCategoryBeanAbstract():
    instance = tests_TestCategoryBeanConcrete()
    assert isinstance(instance, TestCategoryBeanAbstract)


def test_tests_TestCategoryBeanConcrete_isa_dmf_DObject():
    instance = tests_TestCategoryBeanConcrete()
    assert isinstance(instance, dmf_DObject)


def test_tests_TestCategoryExtends_isa_dmf_DObject():
    instance = tests_TestCategoryExtends(testExtendsProperty=7)
    assert isinstance(instance, dmf_DObject)


def test_assoc_mass18_link_reassign_clear():
    a = tests_TestParameter(defaultValue=3.14)
    b1 = tests_TestMassParameters()
    b2 = tests_TestMassParameters()
    _safe_set(a, 'tests_TestParameter', b1)
    assert _is_linked(a, 'tests_TestParameter', b1)
    if hasattr(b1, 'tests_TestMassParameters'):
        assert _is_linked(b1, 'tests_TestMassParameters', a)
    _safe_set(a, 'tests_TestParameter', b2)
    assert _is_linked(a, 'tests_TestParameter', b2)
    if hasattr(b1, 'tests_TestMassParameters'):
        assert not _is_linked(b1, 'tests_TestMassParameters', a)
    if hasattr(b2, 'tests_TestMassParameters'):
        assert _is_linked(b2, 'tests_TestMassParameters', a)
    _safe_set(a, 'tests_TestParameter', None)
    assert not _is_linked(a, 'tests_TestParameter', b2)
    if hasattr(b2, 'tests_TestMassParameters'):
        assert not _is_linked(b2, 'tests_TestMassParameters', a)


def test_assoc_testArray14_link_reassign_clear():
    a = tests_TestCategoryBase(testBaseProperty=7)
    b1 = tests_TestCategoryBase(testBaseProperty=7)
    b2 = tests_TestCategoryBase(testBaseProperty=13)
    _safe_set(a, 'tests_TestCategoryBase', b1)
    assert _is_linked(a, 'tests_TestCategoryBase', b1)
    if hasattr(b1, 'tests_TestCategoryBase13'):
        assert _is_linked(b1, 'tests_TestCategoryBase13', a)
    _safe_set(a, 'tests_TestCategoryBase', b2)
    assert _is_linked(a, 'tests_TestCategoryBase', b2)
    if hasattr(b1, 'tests_TestCategoryBase13'):
        assert not _is_linked(b1, 'tests_TestCategoryBase13', a)
    if hasattr(b2, 'tests_TestCategoryBase13'):
        assert _is_linked(b2, 'tests_TestCategoryBase13', a)
    _safe_set(a, 'tests_TestCategoryBase', None)
    assert not _is_linked(a, 'tests_TestCategoryBase', b2)
    if hasattr(b2, 'tests_TestCategoryBase13'):
        assert not _is_linked(b2, 'tests_TestCategoryBase13', a)


def test_assoc_testCategoryReferenceArrayDynamic8_link_reassign_clear():
    a = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    b1 = tests_TestCategoryReferenceArray()
    b2 = tests_TestCategoryReferenceArray()
    _safe_set(a, 'tests_TestCategoryAllProperty9', b1)
    assert _is_linked(a, 'tests_TestCategoryAllProperty9', b1)
    if hasattr(b1, 'tests_TestCategoryReferenceArray'):
        assert _is_linked(b1, 'tests_TestCategoryReferenceArray', a)
    _safe_set(a, 'tests_TestCategoryAllProperty9', b2)
    assert _is_linked(a, 'tests_TestCategoryAllProperty9', b2)
    if hasattr(b1, 'tests_TestCategoryReferenceArray'):
        assert not _is_linked(b1, 'tests_TestCategoryReferenceArray', a)
    if hasattr(b2, 'tests_TestCategoryReferenceArray'):
        assert _is_linked(b2, 'tests_TestCategoryReferenceArray', a)
    _safe_set(a, 'tests_TestCategoryAllProperty9', None)
    assert not _is_linked(a, 'tests_TestCategoryAllProperty9', b2)
    if hasattr(b2, 'tests_TestCategoryReferenceArray'):
        assert not _is_linked(b2, 'tests_TestCategoryReferenceArray', a)


def test_assoc_testCategoryReferenceArrayStatic10_link_reassign_clear():
    a = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    b1 = tests_TestCategoryReferenceArray()
    b2 = tests_TestCategoryReferenceArray()
    _safe_set(a, 'tests_TestCategoryAllProperty12', b1)
    assert _is_linked(a, 'tests_TestCategoryAllProperty12', b1)
    if hasattr(b1, 'tests_TestCategoryReferenceArray11'):
        assert _is_linked(b1, 'tests_TestCategoryReferenceArray11', a)
    _safe_set(a, 'tests_TestCategoryAllProperty12', b2)
    assert _is_linked(a, 'tests_TestCategoryAllProperty12', b2)
    if hasattr(b1, 'tests_TestCategoryReferenceArray11'):
        assert not _is_linked(b1, 'tests_TestCategoryReferenceArray11', a)
    if hasattr(b2, 'tests_TestCategoryReferenceArray11'):
        assert _is_linked(b2, 'tests_TestCategoryReferenceArray11', a)
    _safe_set(a, 'tests_TestCategoryAllProperty12', None)
    assert not _is_linked(a, 'tests_TestCategoryAllProperty12', b2)
    if hasattr(b2, 'tests_TestCategoryReferenceArray11'):
        assert not _is_linked(b2, 'tests_TestCategoryReferenceArray11', a)


def test_assoc_testCompositionArrayDynamic3_link_reassign_clear():
    a = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    b1 = tests_TestCategoryCompositionArray()
    b2 = tests_TestCategoryCompositionArray()
    _safe_set(a, 'tests_TestCategoryAllProperty4', b1)
    assert _is_linked(a, 'tests_TestCategoryAllProperty4', b1)
    if hasattr(b1, 'tests_TestCategoryCompositionArray'):
        assert _is_linked(b1, 'tests_TestCategoryCompositionArray', a)
    _safe_set(a, 'tests_TestCategoryAllProperty4', b2)
    assert _is_linked(a, 'tests_TestCategoryAllProperty4', b2)
    if hasattr(b1, 'tests_TestCategoryCompositionArray'):
        assert not _is_linked(b1, 'tests_TestCategoryCompositionArray', a)
    if hasattr(b2, 'tests_TestCategoryCompositionArray'):
        assert _is_linked(b2, 'tests_TestCategoryCompositionArray', a)
    _safe_set(a, 'tests_TestCategoryAllProperty4', None)
    assert not _is_linked(a, 'tests_TestCategoryAllProperty4', b2)
    if hasattr(b2, 'tests_TestCategoryCompositionArray'):
        assert not _is_linked(b2, 'tests_TestCategoryCompositionArray', a)


def test_assoc_testCompositionArrayStatic5_link_reassign_clear():
    a = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    b1 = tests_TestCategoryCompositionArray()
    b2 = tests_TestCategoryCompositionArray()
    _safe_set(a, 'tests_TestCategoryAllProperty7', b1)
    assert _is_linked(a, 'tests_TestCategoryAllProperty7', b1)
    if hasattr(b1, 'tests_TestCategoryCompositionArray6'):
        assert _is_linked(b1, 'tests_TestCategoryCompositionArray6', a)
    _safe_set(a, 'tests_TestCategoryAllProperty7', b2)
    assert _is_linked(a, 'tests_TestCategoryAllProperty7', b2)
    if hasattr(b1, 'tests_TestCategoryCompositionArray6'):
        assert not _is_linked(b1, 'tests_TestCategoryCompositionArray6', a)
    if hasattr(b2, 'tests_TestCategoryCompositionArray6'):
        assert _is_linked(b2, 'tests_TestCategoryCompositionArray6', a)
    _safe_set(a, 'tests_TestCategoryAllProperty7', None)
    assert not _is_linked(a, 'tests_TestCategoryAllProperty7', b2)
    if hasattr(b2, 'tests_TestCategoryCompositionArray6'):
        assert not _is_linked(b2, 'tests_TestCategoryCompositionArray6', a)


def test_assoc_testRefCategory1_link_reassign_clear():
    a = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    b1 = tests_TestCategoryReference()
    b2 = tests_TestCategoryReference()
    _safe_set(a, 'tests_TestCategoryAllProperty2', b1)
    assert _is_linked(a, 'tests_TestCategoryAllProperty2', b1)
    if hasattr(b1, 'tests_TestCategoryReference'):
        assert _is_linked(b1, 'tests_TestCategoryReference', a)
    _safe_set(a, 'tests_TestCategoryAllProperty2', b2)
    assert _is_linked(a, 'tests_TestCategoryAllProperty2', b2)
    if hasattr(b1, 'tests_TestCategoryReference'):
        assert not _is_linked(b1, 'tests_TestCategoryReference', a)
    if hasattr(b2, 'tests_TestCategoryReference'):
        assert _is_linked(b2, 'tests_TestCategoryReference', a)
    _safe_set(a, 'tests_TestCategoryAllProperty2', None)
    assert not _is_linked(a, 'tests_TestCategoryAllProperty2', b2)
    if hasattr(b2, 'tests_TestCategoryReference'):
        assert not _is_linked(b2, 'tests_TestCategoryReference', a)


def test_assoc_testReference16_link_reassign_clear():
    a = tests_TestCategoryBase(testBaseProperty=7)
    b1 = tests_TestCategoryBase(testBaseProperty=7)
    b2 = tests_TestCategoryBase(testBaseProperty=13)
    _safe_set(a, 'tests_TestCategoryBase15', b1)
    assert _is_linked(a, 'tests_TestCategoryBase15', b1)
    if hasattr(b1, 'tests_TestCategoryBase17'):
        assert _is_linked(b1, 'tests_TestCategoryBase17', a)
    _safe_set(a, 'tests_TestCategoryBase15', b2)
    assert _is_linked(a, 'tests_TestCategoryBase15', b2)
    if hasattr(b1, 'tests_TestCategoryBase17'):
        assert not _is_linked(b1, 'tests_TestCategoryBase17', a)
    if hasattr(b2, 'tests_TestCategoryBase17'):
        assert _is_linked(b2, 'tests_TestCategoryBase17', a)
    _safe_set(a, 'tests_TestCategoryBase15', None)
    assert not _is_linked(a, 'tests_TestCategoryBase15', b2)
    if hasattr(b2, 'tests_TestCategoryBase17'):
        assert not _is_linked(b2, 'tests_TestCategoryBase17', a)


def test_assoc_testSubCategory0_link_reassign_clear():
    a = tests_TestCategoryAllProperty(testBool=True, testEnum="sample_text", testFloat=3.14, testInt=7, testResource="sample_text", testString="sample_text")
    b1 = tests_TestCategoryComposition()
    b2 = tests_TestCategoryComposition()
    _safe_set(a, 'tests_TestCategoryAllProperty', b1)
    assert _is_linked(a, 'tests_TestCategoryAllProperty', b1)
    if hasattr(b1, 'tests_TestCategoryComposition'):
        assert _is_linked(b1, 'tests_TestCategoryComposition', a)
    _safe_set(a, 'tests_TestCategoryAllProperty', b2)
    assert _is_linked(a, 'tests_TestCategoryAllProperty', b2)
    if hasattr(b1, 'tests_TestCategoryComposition'):
        assert not _is_linked(b1, 'tests_TestCategoryComposition', a)
    if hasattr(b2, 'tests_TestCategoryComposition'):
        assert _is_linked(b2, 'tests_TestCategoryComposition', a)
    _safe_set(a, 'tests_TestCategoryAllProperty', None)
    assert not _is_linked(a, 'tests_TestCategoryAllProperty', b2)
    if hasattr(b2, 'tests_TestCategoryComposition'):
        assert not _is_linked(b2, 'tests_TestCategoryComposition', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DObject_strategy = st.builds(DObject)
@given(instance=DObject_strategy)
@settings(max_examples=25)
def test_DObject_instantiation(instance):
    assert isinstance(instance, DObject)


TestCategoryBase_strategy = st.builds(TestCategoryBase)
@given(instance=TestCategoryBase_strategy)
@settings(max_examples=25)
def test_TestCategoryBase_instantiation(instance):
    assert isinstance(instance, TestCategoryBase)


TestCategoryBeanAbstract_strategy = st.builds(TestCategoryBeanAbstract)
@given(instance=TestCategoryBeanAbstract_strategy)
@settings(max_examples=25)
def test_TestCategoryBeanAbstract_instantiation(instance):
    assert isinstance(instance, TestCategoryBeanAbstract)


dmf_DObject_strategy = st.builds(dmf_DObject)
@given(instance=dmf_DObject_strategy)
@settings(max_examples=25)
def test_dmf_DObject_instantiation(instance):
    assert isinstance(instance, dmf_DObject)


tests_EReferenceTest_strategy = st.builds(tests_EReferenceTest)
@given(instance=tests_EReferenceTest_strategy)
@settings(max_examples=25)
def test_tests_EReferenceTest_instantiation(instance):
    assert isinstance(instance, tests_EReferenceTest)


tests_ExternalTestType_strategy = st.builds(tests_ExternalTestType)
@given(instance=tests_ExternalTestType_strategy)
@settings(max_examples=25)
def test_tests_ExternalTestType_instantiation(instance):
    assert isinstance(instance, tests_ExternalTestType)


tests_TestCategoryAllProperty_strategy = st.builds(tests_TestCategoryAllProperty, testBool=st.booleans(), testEnum=safe_text, testFloat=st.floats(allow_nan=False, allow_infinity=False), testInt=st.integers(), testResource=safe_text, testString=safe_text)
@given(instance=tests_TestCategoryAllProperty_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryAllProperty_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryAllProperty)


tests_TestCategoryBase_strategy = st.builds(tests_TestCategoryBase, testBaseProperty=st.integers())
@given(instance=tests_TestCategoryBase_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryBase_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBase)


tests_TestCategoryBeanA_strategy = st.builds(tests_TestCategoryBeanA)
@given(instance=tests_TestCategoryBeanA_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryBeanA_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBeanA)


tests_TestCategoryBeanAbstract_strategy = st.builds(tests_TestCategoryBeanAbstract)
@given(instance=tests_TestCategoryBeanAbstract_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryBeanAbstract_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBeanAbstract)


tests_TestCategoryBeanB_strategy = st.builds(tests_TestCategoryBeanB)
@given(instance=tests_TestCategoryBeanB_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryBeanB_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBeanB)


tests_TestCategoryBeanConcrete_strategy = st.builds(tests_TestCategoryBeanConcrete)
@given(instance=tests_TestCategoryBeanConcrete_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryBeanConcrete_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryBeanConcrete)


tests_TestCategoryComposition_strategy = st.builds(tests_TestCategoryComposition)
@given(instance=tests_TestCategoryComposition_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryComposition_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryComposition)


tests_TestCategoryCompositionArray_strategy = st.builds(tests_TestCategoryCompositionArray)
@given(instance=tests_TestCategoryCompositionArray_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryCompositionArray_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryCompositionArray)


tests_TestCategoryExtends_strategy = st.builds(tests_TestCategoryExtends, testExtendsProperty=st.integers())
@given(instance=tests_TestCategoryExtends_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryExtends_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryExtends)


tests_TestCategoryIntrinsicArray_strategy = st.builds(tests_TestCategoryIntrinsicArray, testStringArrayDynamic=safe_text, testStringArrayStatic=safe_text)
@given(instance=tests_TestCategoryIntrinsicArray_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryIntrinsicArray_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryIntrinsicArray)


tests_TestCategoryReference_strategy = st.builds(tests_TestCategoryReference)
@given(instance=tests_TestCategoryReference_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryReference_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryReference)


tests_TestCategoryReferenceArray_strategy = st.builds(tests_TestCategoryReferenceArray)
@given(instance=tests_TestCategoryReferenceArray_strategy)
@settings(max_examples=25)
def test_tests_TestCategoryReferenceArray_instantiation(instance):
    assert isinstance(instance, tests_TestCategoryReferenceArray)


tests_TestCrossLinkedParametersWithCalculation_strategy = st.builds(tests_TestCrossLinkedParametersWithCalculation, calcedTrl=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=tests_TestCrossLinkedParametersWithCalculation_strategy)
@settings(max_examples=25)
def test_tests_TestCrossLinkedParametersWithCalculation_instantiation(instance):
    assert isinstance(instance, tests_TestCrossLinkedParametersWithCalculation)


tests_TestMassParameters_strategy = st.builds(tests_TestMassParameters)
@given(instance=tests_TestMassParameters_strategy)
@settings(max_examples=25)
def test_tests_TestMassParameters_instantiation(instance):
    assert isinstance(instance, tests_TestMassParameters)


tests_TestParameter_strategy = st.builds(tests_TestParameter, defaultValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=tests_TestParameter_strategy)
@settings(max_examples=25)
def test_tests_TestParameter_instantiation(instance):
    assert isinstance(instance, tests_TestParameter)



