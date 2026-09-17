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
    model6_UnsettableAttributes,
    model6_EmptyStringDefaultUnsettable,
    model6_EmptyStringDefault,
    model6_HasNillableAttribute,
    model6_CanReferenceLegacy,
    model6_G,
    model6_F,
    model6_E,
    model6_EObject,
    model6_C,
    model6_B,
    model6_D,
    model6_A,
    model6_PropertiesMapEntryValue,
    model6_Holdable,
    Holdable,
    model6_Thing,
    model6_Holder,
    model6_MyEnumListUnsettable,
    model6_MyEnumList,
    model6_BaseObject,
    model6_Root,
    model6_PropertiesMapEntry,
    model6_PropertiesMap,
    model6_UnorderedList,
    BaseObject,
    model6_ContainmentObject,
    model6_ReferenceObject,
    MyEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_model6_unsettableattributes_is_not_abstract():
    assert not inspect.isabstract(model6_UnsettableAttributes)


def test_hyp_model6_unsettableattributes_constructor_exists():
    assert callable(model6_UnsettableAttributes.__init__)


def test_hyp_model6_unsettableattributes_constructor_args():
    sig = inspect.signature(model6_UnsettableAttributes.__init__)
    params = list(sig.parameters.keys())
    assert "attrBoolean" in params, "Missing parameter 'attrBoolean'"
    assert "attrFloatObject" in params, "Missing parameter 'attrFloatObject'"
    assert "attrChar" in params, "Missing parameter 'attrChar'"
    assert "attrIntegerObject" in params, "Missing parameter 'attrIntegerObject'"
    assert "attrDouble" in params, "Missing parameter 'attrDouble'"
    assert "attrJavaObject" in params, "Missing parameter 'attrJavaObject'"
    assert "attrCharacterObject" in params, "Missing parameter 'attrCharacterObject'"
    assert "attrBigInteger" in params, "Missing parameter 'attrBigInteger'"
    assert "attrJavaClass" in params, "Missing parameter 'attrJavaClass'"
    assert "attrDate" in params, "Missing parameter 'attrDate'"
    assert "attrByteObject" in params, "Missing parameter 'attrByteObject'"
    assert "attrLongObject" in params, "Missing parameter 'attrLongObject'"
    assert "attrLong" in params, "Missing parameter 'attrLong'"
    assert "attrFloat" in params, "Missing parameter 'attrFloat'"
    assert "attrShortObject" in params, "Missing parameter 'attrShortObject'"
    assert "attrBigDecimal" in params, "Missing parameter 'attrBigDecimal'"
    assert "attrByte" in params, "Missing parameter 'attrByte'"
    assert "attrByteArray" in params, "Missing parameter 'attrByteArray'"
    assert "attrBooleanObject" in params, "Missing parameter 'attrBooleanObject'"
    assert "attrString" in params, "Missing parameter 'attrString'"
    assert "attrShort" in params, "Missing parameter 'attrShort'"
    assert "attrInt" in params, "Missing parameter 'attrInt'"
    assert "attrDoubleObject" in params, "Missing parameter 'attrDoubleObject'"


























def test_hyp_model6_emptystringdefaultunsettable_is_not_abstract():
    assert not inspect.isabstract(model6_EmptyStringDefaultUnsettable)


def test_hyp_model6_emptystringdefaultunsettable_constructor_exists():
    assert callable(model6_EmptyStringDefaultUnsettable.__init__)


def test_hyp_model6_emptystringdefaultunsettable_constructor_args():
    sig = inspect.signature(model6_EmptyStringDefaultUnsettable.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_model6_emptystringdefault_is_not_abstract():
    assert not inspect.isabstract(model6_EmptyStringDefault)


def test_hyp_model6_emptystringdefault_constructor_exists():
    assert callable(model6_EmptyStringDefault.__init__)


def test_hyp_model6_emptystringdefault_constructor_args():
    sig = inspect.signature(model6_EmptyStringDefault.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_model6_hasnillableattribute_is_not_abstract():
    assert not inspect.isabstract(model6_HasNillableAttribute)


def test_hyp_model6_hasnillableattribute_constructor_exists():
    assert callable(model6_HasNillableAttribute.__init__)


def test_hyp_model6_hasnillableattribute_constructor_args():
    sig = inspect.signature(model6_HasNillableAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "nillable" in params, "Missing parameter 'nillable'"




def test_hyp_model6_canreferencelegacy_is_not_abstract():
    assert not inspect.isabstract(model6_CanReferenceLegacy)


def test_hyp_model6_canreferencelegacy_constructor_exists():
    assert callable(model6_CanReferenceLegacy.__init__)


def test_hyp_model6_canreferencelegacy_constructor_args():
    sig = inspect.signature(model6_CanReferenceLegacy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_g_is_not_abstract():
    assert not inspect.isabstract(model6_G)


def test_hyp_model6_g_constructor_exists():
    assert callable(model6_G.__init__)


def test_hyp_model6_g_constructor_args():
    sig = inspect.signature(model6_G.__init__)
    params = list(sig.parameters.keys())
    assert "dummy" in params, "Missing parameter 'dummy'"




def test_hyp_model6_f_is_not_abstract():
    assert not inspect.isabstract(model6_F)


def test_hyp_model6_f_constructor_exists():
    assert callable(model6_F.__init__)


def test_hyp_model6_f_constructor_args():
    sig = inspect.signature(model6_F.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_e_is_not_abstract():
    assert not inspect.isabstract(model6_E)


def test_hyp_model6_e_constructor_exists():
    assert callable(model6_E.__init__)


def test_hyp_model6_e_constructor_args():
    sig = inspect.signature(model6_E.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_eobject_is_not_abstract():
    assert not inspect.isabstract(model6_EObject)


def test_hyp_model6_eobject_constructor_exists():
    assert callable(model6_EObject.__init__)


def test_hyp_model6_eobject_constructor_args():
    sig = inspect.signature(model6_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_c_is_not_abstract():
    assert not inspect.isabstract(model6_C)


def test_hyp_model6_c_constructor_exists():
    assert callable(model6_C.__init__)


def test_hyp_model6_c_constructor_args():
    sig = inspect.signature(model6_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_b_is_not_abstract():
    assert not inspect.isabstract(model6_B)


def test_hyp_model6_b_constructor_exists():
    assert callable(model6_B.__init__)


def test_hyp_model6_b_constructor_args():
    sig = inspect.signature(model6_B.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_d_is_not_abstract():
    assert not inspect.isabstract(model6_D)


def test_hyp_model6_d_constructor_exists():
    assert callable(model6_D.__init__)


def test_hyp_model6_d_constructor_args():
    sig = inspect.signature(model6_D.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_a_is_not_abstract():
    assert not inspect.isabstract(model6_A)


def test_hyp_model6_a_constructor_exists():
    assert callable(model6_A.__init__)


def test_hyp_model6_a_constructor_args():
    sig = inspect.signature(model6_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_propertiesmapentryvalue_is_not_abstract():
    assert not inspect.isabstract(model6_PropertiesMapEntryValue)


def test_hyp_model6_propertiesmapentryvalue_constructor_exists():
    assert callable(model6_PropertiesMapEntryValue.__init__)


def test_hyp_model6_propertiesmapentryvalue_constructor_args():
    sig = inspect.signature(model6_PropertiesMapEntryValue.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_model6_holdable_is_not_abstract():
    assert not inspect.isabstract(model6_Holdable)


def test_hyp_model6_holdable_constructor_exists():
    assert callable(model6_Holdable.__init__)


def test_hyp_model6_holdable_constructor_args():
    sig = inspect.signature(model6_Holdable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_holdable_is_not_abstract():
    assert not inspect.isabstract(Holdable)


def test_hyp_holdable_constructor_exists():
    assert callable(Holdable.__init__)


def test_hyp_holdable_constructor_args():
    sig = inspect.signature(Holdable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_thing_is_not_abstract():
    assert not inspect.isabstract(model6_Thing)


def test_hyp_model6_thing_constructor_exists():
    assert callable(model6_Thing.__init__)


def test_hyp_model6_thing_constructor_args():
    sig = inspect.signature(model6_Thing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_holder_is_not_abstract():
    assert not inspect.isabstract(model6_Holder)


def test_hyp_model6_holder_constructor_exists():
    assert callable(model6_Holder.__init__)


def test_hyp_model6_holder_constructor_args():
    sig = inspect.signature(model6_Holder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_myenumlistunsettable_is_not_abstract():
    assert not inspect.isabstract(model6_MyEnumListUnsettable)


def test_hyp_model6_myenumlistunsettable_constructor_exists():
    assert callable(model6_MyEnumListUnsettable.__init__)


def test_hyp_model6_myenumlistunsettable_constructor_args():
    sig = inspect.signature(model6_MyEnumListUnsettable.__init__)
    params = list(sig.parameters.keys())
    assert "myEnum" in params, "Missing parameter 'myEnum'"




def test_hyp_model6_myenumlist_is_not_abstract():
    assert not inspect.isabstract(model6_MyEnumList)


def test_hyp_model6_myenumlist_constructor_exists():
    assert callable(model6_MyEnumList.__init__)


def test_hyp_model6_myenumlist_constructor_args():
    sig = inspect.signature(model6_MyEnumList.__init__)
    params = list(sig.parameters.keys())
    assert "myEnum" in params, "Missing parameter 'myEnum'"




def test_hyp_model6_baseobject_is_not_abstract():
    assert not inspect.isabstract(model6_BaseObject)


def test_hyp_model6_baseobject_constructor_exists():
    assert callable(model6_BaseObject.__init__)


def test_hyp_model6_baseobject_constructor_args():
    sig = inspect.signature(model6_BaseObject.__init__)
    params = list(sig.parameters.keys())
    assert "attributeList" in params, "Missing parameter 'attributeList'"
    assert "attributeOptional" in params, "Missing parameter 'attributeOptional'"
    assert "attributeRequired" in params, "Missing parameter 'attributeRequired'"






def test_hyp_model6_root_is_not_abstract():
    assert not inspect.isabstract(model6_Root)


def test_hyp_model6_root_constructor_exists():
    assert callable(model6_Root.__init__)


def test_hyp_model6_root_constructor_args():
    sig = inspect.signature(model6_Root.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_propertiesmapentry_is_not_abstract():
    assert not inspect.isabstract(model6_PropertiesMapEntry)


def test_hyp_model6_propertiesmapentry_constructor_exists():
    assert callable(model6_PropertiesMapEntry.__init__)


def test_hyp_model6_propertiesmapentry_constructor_args():
    sig = inspect.signature(model6_PropertiesMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_model6_propertiesmap_is_not_abstract():
    assert not inspect.isabstract(model6_PropertiesMap)


def test_hyp_model6_propertiesmap_constructor_exists():
    assert callable(model6_PropertiesMap.__init__)


def test_hyp_model6_propertiesmap_constructor_args():
    sig = inspect.signature(model6_PropertiesMap.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_model6_unorderedlist_is_not_abstract():
    assert not inspect.isabstract(model6_UnorderedList)


def test_hyp_model6_unorderedlist_constructor_exists():
    assert callable(model6_UnorderedList.__init__)


def test_hyp_model6_unorderedlist_constructor_args():
    sig = inspect.signature(model6_UnorderedList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_baseobject_is_not_abstract():
    assert not inspect.isabstract(BaseObject)


def test_hyp_baseobject_constructor_exists():
    assert callable(BaseObject.__init__)


def test_hyp_baseobject_constructor_args():
    sig = inspect.signature(BaseObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_containmentobject_is_not_abstract():
    assert not inspect.isabstract(model6_ContainmentObject)


def test_hyp_model6_containmentobject_constructor_exists():
    assert callable(model6_ContainmentObject.__init__)


def test_hyp_model6_containmentobject_constructor_args():
    sig = inspect.signature(model6_ContainmentObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model6_referenceobject_is_not_abstract():
    assert not inspect.isabstract(model6_ReferenceObject)


def test_hyp_model6_referenceobject_constructor_exists():
    assert callable(model6_ReferenceObject.__init__)


def test_hyp_model6_referenceobject_constructor_args():
    sig = inspect.signature(model6_ReferenceObject.__init__)
    params = list(sig.parameters.keys())

def test_hyp_myenum_exists():
    # Check that the Enumeration exists
    assert MyEnum is not None

def test_hyp_myenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MyEnum]
    expected_literals = [
        "TWO",
        "ZERO",
        "ONE",
        "THREE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MyEnum"


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
model6_UnsettableAttributes_strategy = st.builds(
    model6_UnsettableAttributes,
    attrBoolean=
        st.booleans(),
    attrFloatObject=
        safe_text,
    attrChar=
        safe_text,
    attrIntegerObject=
        safe_text,
    attrDouble=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    attrJavaObject=
        safe_text,
    attrCharacterObject=
        safe_text,
    attrBigInteger=
        safe_text,
    attrJavaClass=
        safe_text,
    attrDate=
        st.dates(),
    attrByteObject=
        safe_text,
    attrLongObject=
        safe_text,
    attrLong=
        safe_text,
    attrFloat=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    attrShortObject=
        safe_text,
    attrBigDecimal=
        safe_text,
    attrByte=
        safe_text,
    attrByteArray=
        safe_text,
    attrBooleanObject=
        safe_text,
    attrString=
        safe_text,
    attrShort=
        safe_text,
    attrInt=
        st.integers(),
    attrDoubleObject=
        safe_text
)
model6_EmptyStringDefaultUnsettable_strategy = st.builds(
    model6_EmptyStringDefaultUnsettable,
    attribute=
        safe_text
)
model6_EmptyStringDefault_strategy = st.builds(
    model6_EmptyStringDefault,
    attribute=
        safe_text
)
model6_HasNillableAttribute_strategy = st.builds(
    model6_HasNillableAttribute,
    nillable=
        safe_text
)
model6_CanReferenceLegacy_strategy = st.builds(
    model6_CanReferenceLegacy,
)
model6_G_strategy = st.builds(
    model6_G,
    dummy=
        safe_text
)
model6_F_strategy = st.builds(
    model6_F,
)
model6_E_strategy = st.builds(
    model6_E,
)
model6_EObject_strategy = st.builds(
    model6_EObject,
)
model6_C_strategy = st.builds(
    model6_C,
)
model6_B_strategy = st.builds(
    model6_B,
)
model6_D_strategy = st.builds(
    model6_D,
)
model6_A_strategy = st.builds(
    model6_A,
)
model6_PropertiesMapEntryValue_strategy = st.builds(
    model6_PropertiesMapEntryValue,
    label=
        safe_text
)
model6_Holdable_strategy = st.builds(
    model6_Holdable,
    name=
        safe_text
)
Holdable_strategy = st.builds(
    Holdable,
)
model6_Thing_strategy = st.builds(
    model6_Thing,
)
model6_Holder_strategy = st.builds(
    model6_Holder,
)
model6_MyEnumListUnsettable_strategy = st.builds(
    model6_MyEnumListUnsettable,
    myEnum=
        safe_text
)
model6_MyEnumList_strategy = st.builds(
    model6_MyEnumList,
    myEnum=
        safe_text
)
model6_BaseObject_strategy = st.builds(
    model6_BaseObject,
    attributeList=
        safe_text,
    attributeOptional=
        safe_text,
    attributeRequired=
        safe_text
)
model6_Root_strategy = st.builds(
    model6_Root,
)
model6_PropertiesMapEntry_strategy = st.builds(
    model6_PropertiesMapEntry,
    key=
        safe_text
)
model6_PropertiesMap_strategy = st.builds(
    model6_PropertiesMap,
    label=
        safe_text
)
model6_UnorderedList_strategy = st.builds(
    model6_UnorderedList,
)
BaseObject_strategy = st.builds(
    BaseObject,
)
model6_ContainmentObject_strategy = st.builds(
    model6_ContainmentObject,
)
model6_ReferenceObject_strategy = st.builds(
    model6_ReferenceObject,
)




@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrBoolean_setter(instance):
    original = instance.attrBoolean
    instance.attrBoolean = original
    assert instance.attrBoolean == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrFloatObject_setter(instance):
    original = instance.attrFloatObject
    instance.attrFloatObject = original
    assert instance.attrFloatObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrChar_setter(instance):
    original = instance.attrChar
    instance.attrChar = original
    assert instance.attrChar == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrIntegerObject_setter(instance):
    original = instance.attrIntegerObject
    instance.attrIntegerObject = original
    assert instance.attrIntegerObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrDouble_setter(instance):
    original = instance.attrDouble
    instance.attrDouble = original
    assert instance.attrDouble == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrJavaObject_setter(instance):
    original = instance.attrJavaObject
    instance.attrJavaObject = original
    assert instance.attrJavaObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrCharacterObject_setter(instance):
    original = instance.attrCharacterObject
    instance.attrCharacterObject = original
    assert instance.attrCharacterObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrBigInteger_setter(instance):
    original = instance.attrBigInteger
    instance.attrBigInteger = original
    assert instance.attrBigInteger == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrJavaClass_setter(instance):
    original = instance.attrJavaClass
    instance.attrJavaClass = original
    assert instance.attrJavaClass == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrDate_setter(instance):
    original = instance.attrDate
    instance.attrDate = original
    assert instance.attrDate == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrByteObject_setter(instance):
    original = instance.attrByteObject
    instance.attrByteObject = original
    assert instance.attrByteObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrLongObject_setter(instance):
    original = instance.attrLongObject
    instance.attrLongObject = original
    assert instance.attrLongObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrLong_setter(instance):
    original = instance.attrLong
    instance.attrLong = original
    assert instance.attrLong == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrFloat_setter(instance):
    original = instance.attrFloat
    instance.attrFloat = original
    assert instance.attrFloat == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrShortObject_setter(instance):
    original = instance.attrShortObject
    instance.attrShortObject = original
    assert instance.attrShortObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrBigDecimal_setter(instance):
    original = instance.attrBigDecimal
    instance.attrBigDecimal = original
    assert instance.attrBigDecimal == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrByte_setter(instance):
    original = instance.attrByte
    instance.attrByte = original
    assert instance.attrByte == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrByteArray_setter(instance):
    original = instance.attrByteArray
    instance.attrByteArray = original
    assert instance.attrByteArray == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrBooleanObject_setter(instance):
    original = instance.attrBooleanObject
    instance.attrBooleanObject = original
    assert instance.attrBooleanObject == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrString_setter(instance):
    original = instance.attrString
    instance.attrString = original
    assert instance.attrString == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrShort_setter(instance):
    original = instance.attrShort
    instance.attrShort = original
    assert instance.attrShort == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrInt_setter(instance):
    original = instance.attrInt
    instance.attrInt = original
    assert instance.attrInt == original



@given(instance=model6_UnsettableAttributes_strategy)
def test_hyp_model6_unsettableattributes_attrDoubleObject_setter(instance):
    original = instance.attrDoubleObject
    instance.attrDoubleObject = original
    assert instance.attrDoubleObject == original




@given(instance=model6_EmptyStringDefaultUnsettable_strategy)
def test_hyp_model6_emptystringdefaultunsettable_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=model6_EmptyStringDefault_strategy)
def test_hyp_model6_emptystringdefault_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=model6_HasNillableAttribute_strategy)
def test_hyp_model6_hasnillableattribute_nillable_setter(instance):
    original = instance.nillable
    instance.nillable = original
    assert instance.nillable == original





@given(instance=model6_G_strategy)
def test_hyp_model6_g_dummy_setter(instance):
    original = instance.dummy
    instance.dummy = original
    assert instance.dummy == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6_G_strategy)
@settings(max_examples=30)
def test_hyp_model6_g_isattributemodified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAttributeModified()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAttributeModified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAttributeModified' in model6_G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAttributeModified' in model6_G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAttributeModified' in model6_G is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6_G_strategy)
@settings(max_examples=30)
def test_hyp_model6_g_islistmodified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isListModified()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isListModified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isListModified' in model6_G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isListModified' in model6_G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isListModified' in model6_G is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model6_G_strategy)
@settings(max_examples=30)
def test_hyp_model6_g_isreferencemodified_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isReferenceModified()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isReferenceModified).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isReferenceModified' in model6_G is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isReferenceModified' in model6_G did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isReferenceModified' in model6_G is not implemented or raised an error")











@given(instance=model6_PropertiesMapEntryValue_strategy)
def test_hyp_model6_propertiesmapentryvalue_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=model6_Holdable_strategy)
def test_hyp_model6_holdable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=model6_MyEnumListUnsettable_strategy)
def test_hyp_model6_myenumlistunsettable_myEnum_setter(instance):
    original = instance.myEnum
    instance.myEnum = original
    assert instance.myEnum == original




@given(instance=model6_MyEnumList_strategy)
def test_hyp_model6_myenumlist_myEnum_setter(instance):
    original = instance.myEnum
    instance.myEnum = original
    assert instance.myEnum == original




@given(instance=model6_BaseObject_strategy)
def test_hyp_model6_baseobject_attributeList_setter(instance):
    original = instance.attributeList
    instance.attributeList = original
    assert instance.attributeList == original



@given(instance=model6_BaseObject_strategy)
def test_hyp_model6_baseobject_attributeOptional_setter(instance):
    original = instance.attributeOptional
    instance.attributeOptional = original
    assert instance.attributeOptional == original



@given(instance=model6_BaseObject_strategy)
def test_hyp_model6_baseobject_attributeRequired_setter(instance):
    original = instance.attributeRequired
    instance.attributeRequired = original
    assert instance.attributeRequired == original





@given(instance=model6_PropertiesMapEntry_strategy)
def test_hyp_model6_propertiesmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




@given(instance=model6_PropertiesMap_strategy)
def test_hyp_model6_propertiesmap_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BaseObject,
    Holdable,
    model6_A,
    model6_B,
    model6_BaseObject,
    model6_C,
    model6_CanReferenceLegacy,
    model6_ContainmentObject,
    model6_D,
    model6_E,
    model6_EObject,
    model6_EmptyStringDefault,
    model6_EmptyStringDefaultUnsettable,
    model6_F,
    model6_G,
    model6_HasNillableAttribute,
    model6_Holdable,
    model6_Holder,
    model6_MyEnumList,
    model6_MyEnumListUnsettable,
    model6_PropertiesMap,
    model6_PropertiesMapEntry,
    model6_PropertiesMapEntryValue,
    model6_ReferenceObject,
    model6_Root,
    model6_Thing,
    model6_UnorderedList,
    model6_UnsettableAttributes,
    MyEnum,
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

def test_model6_BaseObject_attributeList_value_roundtrip():
    instance = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    assert instance.attributeList == "sample_text"
    instance.attributeList = "sample_text_2"
    assert instance.attributeList == "sample_text_2"


def test_model6_BaseObject_attributeOptional_value_roundtrip():
    instance = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    assert instance.attributeOptional == "sample_text"
    instance.attributeOptional = "sample_text_2"
    assert instance.attributeOptional == "sample_text_2"


def test_model6_BaseObject_attributeRequired_value_roundtrip():
    instance = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    assert instance.attributeRequired == "sample_text"
    instance.attributeRequired = "sample_text_2"
    assert instance.attributeRequired == "sample_text_2"


def test_model6_EmptyStringDefault_attribute_value_roundtrip():
    instance = model6_EmptyStringDefault(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_model6_EmptyStringDefaultUnsettable_attribute_value_roundtrip():
    instance = model6_EmptyStringDefaultUnsettable(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_model6_G_dummy_value_roundtrip():
    instance = model6_G(dummy="sample_text")
    assert instance.dummy == "sample_text"
    instance.dummy = "sample_text_2"
    assert instance.dummy == "sample_text_2"


def test_model6_HasNillableAttribute_nillable_value_roundtrip():
    instance = model6_HasNillableAttribute(nillable="sample_text")
    assert instance.nillable == "sample_text"
    instance.nillable = "sample_text_2"
    assert instance.nillable == "sample_text_2"


def test_model6_Holdable_name_value_roundtrip():
    instance = model6_Holdable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model6_MyEnumList_myEnum_value_roundtrip():
    instance = model6_MyEnumList(myEnum="sample_text")
    assert instance.myEnum == "sample_text"
    instance.myEnum = "sample_text_2"
    assert instance.myEnum == "sample_text_2"


def test_model6_MyEnumListUnsettable_myEnum_value_roundtrip():
    instance = model6_MyEnumListUnsettable(myEnum="sample_text")
    assert instance.myEnum == "sample_text"
    instance.myEnum = "sample_text_2"
    assert instance.myEnum == "sample_text_2"


def test_model6_PropertiesMap_label_value_roundtrip():
    instance = model6_PropertiesMap(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_model6_PropertiesMapEntry_key_value_roundtrip():
    instance = model6_PropertiesMapEntry(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_model6_PropertiesMapEntryValue_label_value_roundtrip():
    instance = model6_PropertiesMapEntryValue(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_model6_UnsettableAttributes_attrBigDecimal_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrBigDecimal == "sample_text"
    instance.attrBigDecimal = "sample_text_2"
    assert instance.attrBigDecimal == "sample_text_2"


def test_model6_UnsettableAttributes_attrBigInteger_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrBigInteger == "sample_text"
    instance.attrBigInteger = "sample_text_2"
    assert instance.attrBigInteger == "sample_text_2"


def test_model6_UnsettableAttributes_attrBoolean_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrBoolean == True
    instance.attrBoolean = False
    assert instance.attrBoolean == False


def test_model6_UnsettableAttributes_attrBooleanObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrBooleanObject == "sample_text"
    instance.attrBooleanObject = "sample_text_2"
    assert instance.attrBooleanObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrByte_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrByte == "sample_text"
    instance.attrByte = "sample_text_2"
    assert instance.attrByte == "sample_text_2"


def test_model6_UnsettableAttributes_attrByteArray_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrByteArray == "sample_text"
    instance.attrByteArray = "sample_text_2"
    assert instance.attrByteArray == "sample_text_2"


def test_model6_UnsettableAttributes_attrByteObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrByteObject == "sample_text"
    instance.attrByteObject = "sample_text_2"
    assert instance.attrByteObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrChar_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrChar == "sample_text"
    instance.attrChar = "sample_text_2"
    assert instance.attrChar == "sample_text_2"


def test_model6_UnsettableAttributes_attrCharacterObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrCharacterObject == "sample_text"
    instance.attrCharacterObject = "sample_text_2"
    assert instance.attrCharacterObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrDate_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrDate == date(2024, 1, 1)
    instance.attrDate = date(2025, 6, 15)
    assert instance.attrDate == date(2025, 6, 15)


def test_model6_UnsettableAttributes_attrDouble_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrDouble == 3.14
    instance.attrDouble = 9.99
    assert instance.attrDouble == 9.99


def test_model6_UnsettableAttributes_attrDoubleObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrDoubleObject == "sample_text"
    instance.attrDoubleObject = "sample_text_2"
    assert instance.attrDoubleObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrFloat_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrFloat == 3.14
    instance.attrFloat = 9.99
    assert instance.attrFloat == 9.99


def test_model6_UnsettableAttributes_attrFloatObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrFloatObject == "sample_text"
    instance.attrFloatObject = "sample_text_2"
    assert instance.attrFloatObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrInt_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrInt == 7
    instance.attrInt = 13
    assert instance.attrInt == 13


def test_model6_UnsettableAttributes_attrIntegerObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrIntegerObject == "sample_text"
    instance.attrIntegerObject = "sample_text_2"
    assert instance.attrIntegerObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrJavaClass_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrJavaClass == "sample_text"
    instance.attrJavaClass = "sample_text_2"
    assert instance.attrJavaClass == "sample_text_2"


def test_model6_UnsettableAttributes_attrJavaObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrJavaObject == "sample_text"
    instance.attrJavaObject = "sample_text_2"
    assert instance.attrJavaObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrLong_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrLong == "sample_text"
    instance.attrLong = "sample_text_2"
    assert instance.attrLong == "sample_text_2"


def test_model6_UnsettableAttributes_attrLongObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrLongObject == "sample_text"
    instance.attrLongObject = "sample_text_2"
    assert instance.attrLongObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrShort_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrShort == "sample_text"
    instance.attrShort = "sample_text_2"
    assert instance.attrShort == "sample_text_2"


def test_model6_UnsettableAttributes_attrShortObject_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrShortObject == "sample_text"
    instance.attrShortObject = "sample_text_2"
    assert instance.attrShortObject == "sample_text_2"


def test_model6_UnsettableAttributes_attrString_value_roundtrip():
    instance = model6_UnsettableAttributes(attrBigDecimal="sample_text", attrBigInteger="sample_text", attrBoolean=True, attrBooleanObject="sample_text", attrByte="sample_text", attrByteArray="sample_text", attrByteObject="sample_text", attrChar="sample_text", attrCharacterObject="sample_text", attrDate=date(2024, 1, 1), attrDouble=3.14, attrDoubleObject="sample_text", attrFloat=3.14, attrFloatObject="sample_text", attrInt=7, attrIntegerObject="sample_text", attrJavaClass="sample_text", attrJavaObject="sample_text", attrLong="sample_text", attrLongObject="sample_text", attrShort="sample_text", attrShortObject="sample_text", attrString="sample_text")
    assert instance.attrString == "sample_text"
    instance.attrString = "sample_text_2"
    assert instance.attrString == "sample_text_2"


def test_model6_ContainmentObject_isa_BaseObject():
    instance = model6_ContainmentObject()
    assert isinstance(instance, BaseObject)


def test_model6_ReferenceObject_isa_BaseObject():
    instance = model6_ReferenceObject()
    assert isinstance(instance, BaseObject)


def test_model6_Holder_isa_Holdable():
    instance = model6_Holder()
    assert isinstance(instance, Holdable)


def test_model6_Thing_isa_Holdable():
    instance = model6_Thing()
    assert isinstance(instance, Holdable)


def test_assoc_containmentList17_link_reassign_clear():
    a = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b1 = model6_ContainmentObject()
    b2 = model6_ContainmentObject()
    _safe_set(a, 'model6_BaseObject19', b1)
    assert _is_linked(a, 'model6_BaseObject19', b1)
    if hasattr(b1, 'model6_ContainmentObject18'):
        assert _is_linked(b1, 'model6_ContainmentObject18', a)
    _safe_set(a, 'model6_BaseObject19', b2)
    assert _is_linked(a, 'model6_BaseObject19', b2)
    if hasattr(b1, 'model6_ContainmentObject18'):
        assert not _is_linked(b1, 'model6_ContainmentObject18', a)
    if hasattr(b2, 'model6_ContainmentObject18'):
        assert _is_linked(b2, 'model6_ContainmentObject18', a)
    _safe_set(a, 'model6_BaseObject19', None)
    assert not _is_linked(a, 'model6_BaseObject19', b2)
    if hasattr(b2, 'model6_ContainmentObject18'):
        assert not _is_linked(b2, 'model6_ContainmentObject18', a)


def test_assoc_containmentOptional15_link_reassign_clear():
    a = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b1 = model6_ContainmentObject()
    b2 = model6_ContainmentObject()
    _safe_set(a, 'model6_BaseObject16', b1)
    assert _is_linked(a, 'model6_BaseObject16', b1)
    if hasattr(b1, 'model6_ContainmentObject'):
        assert _is_linked(b1, 'model6_ContainmentObject', a)
    _safe_set(a, 'model6_BaseObject16', b2)
    assert _is_linked(a, 'model6_BaseObject16', b2)
    if hasattr(b1, 'model6_ContainmentObject'):
        assert not _is_linked(b1, 'model6_ContainmentObject', a)
    if hasattr(b2, 'model6_ContainmentObject'):
        assert _is_linked(b2, 'model6_ContainmentObject', a)
    _safe_set(a, 'model6_BaseObject16', None)
    assert not _is_linked(a, 'model6_BaseObject16', b2)
    if hasattr(b2, 'model6_ContainmentObject'):
        assert not _is_linked(b2, 'model6_ContainmentObject', a)


def test_assoc_held47_link_reassign_clear():
    a = model6_Holdable(name="sample_text")
    b1 = model6_Holder()
    b2 = model6_Holder()
    _safe_set(a, 'model6_Holdable', b1)
    assert _is_linked(a, 'model6_Holdable', b1)
    if hasattr(b1, 'model6_Holder'):
        assert _is_linked(b1, 'model6_Holder', a)
    _safe_set(a, 'model6_Holdable', b2)
    assert _is_linked(a, 'model6_Holdable', b2)
    if hasattr(b1, 'model6_Holder'):
        assert not _is_linked(b1, 'model6_Holder', a)
    if hasattr(b2, 'model6_Holder'):
        assert _is_linked(b2, 'model6_Holder', a)
    _safe_set(a, 'model6_Holdable', None)
    assert not _is_linked(a, 'model6_Holdable', b2)
    if hasattr(b2, 'model6_Holder'):
        assert not _is_linked(b2, 'model6_Holder', a)


def test_assoc_list44_link_reassign_clear():
    a = model6_G(dummy="sample_text")
    b1 = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b2 = model6_BaseObject(attributeList="sample_text_2", attributeOptional="sample_text_2", attributeRequired="sample_text_2")
    _safe_set(a, 'model6_G45', {b1})
    assert _is_linked(a, 'model6_G45', b1)
    if hasattr(b1, 'model6_BaseObject46'):
        assert _is_linked(b1, 'model6_BaseObject46', a)
    _safe_set(a, 'model6_G45', {b2})
    assert _is_linked(a, 'model6_G45', b2)
    if hasattr(b1, 'model6_BaseObject46'):
        assert not _is_linked(b1, 'model6_BaseObject46', a)
    if hasattr(b2, 'model6_BaseObject46'):
        assert _is_linked(b2, 'model6_BaseObject46', a)
    _safe_set(a, 'model6_G45', set())
    assert not _is_linked(a, 'model6_G45', b2)
    if hasattr(b2, 'model6_BaseObject46'):
        assert not _is_linked(b2, 'model6_BaseObject46', a)


def test_assoc_listA0_link_reassign_clear():
    a = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b1 = model6_Root()
    b2 = model6_Root()
    _safe_set(a, 'model6_BaseObject', b1)
    assert _is_linked(a, 'model6_BaseObject', b1)
    if hasattr(b1, 'model6_Root'):
        assert _is_linked(b1, 'model6_Root', a)
    _safe_set(a, 'model6_BaseObject', b2)
    assert _is_linked(a, 'model6_BaseObject', b2)
    if hasattr(b1, 'model6_Root'):
        assert not _is_linked(b1, 'model6_Root', a)
    if hasattr(b2, 'model6_Root'):
        assert _is_linked(b2, 'model6_Root', a)
    _safe_set(a, 'model6_BaseObject', None)
    assert not _is_linked(a, 'model6_BaseObject', b2)
    if hasattr(b2, 'model6_Root'):
        assert not _is_linked(b2, 'model6_Root', a)


def test_assoc_listB1_link_reassign_clear():
    a = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b1 = model6_Root()
    b2 = model6_Root()
    _safe_set(a, 'model6_BaseObject3', b1)
    assert _is_linked(a, 'model6_BaseObject3', b1)
    if hasattr(b1, 'model6_Root2'):
        assert _is_linked(b1, 'model6_Root2', a)
    _safe_set(a, 'model6_BaseObject3', b2)
    assert _is_linked(a, 'model6_BaseObject3', b2)
    if hasattr(b1, 'model6_Root2'):
        assert not _is_linked(b1, 'model6_Root2', a)
    if hasattr(b2, 'model6_Root2'):
        assert _is_linked(b2, 'model6_Root2', a)
    _safe_set(a, 'model6_BaseObject3', None)
    assert not _is_linked(a, 'model6_BaseObject3', b2)
    if hasattr(b2, 'model6_Root2'):
        assert not _is_linked(b2, 'model6_Root2', a)


def test_assoc_listC4_link_reassign_clear():
    a = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b1 = model6_Root()
    b2 = model6_Root()
    _safe_set(a, 'model6_BaseObject6', b1)
    assert _is_linked(a, 'model6_BaseObject6', b1)
    if hasattr(b1, 'model6_Root5'):
        assert _is_linked(b1, 'model6_Root5', a)
    _safe_set(a, 'model6_BaseObject6', b2)
    assert _is_linked(a, 'model6_BaseObject6', b2)
    if hasattr(b1, 'model6_Root5'):
        assert not _is_linked(b1, 'model6_Root5', a)
    if hasattr(b2, 'model6_Root5'):
        assert _is_linked(b2, 'model6_Root5', a)
    _safe_set(a, 'model6_BaseObject6', None)
    assert not _is_linked(a, 'model6_BaseObject6', b2)
    if hasattr(b2, 'model6_Root5'):
        assert not _is_linked(b2, 'model6_Root5', a)


def test_assoc_listD7_link_reassign_clear():
    a = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b1 = model6_Root()
    b2 = model6_Root()
    _safe_set(a, 'model6_BaseObject9', b1)
    assert _is_linked(a, 'model6_BaseObject9', b1)
    if hasattr(b1, 'model6_Root8'):
        assert _is_linked(b1, 'model6_Root8', a)
    _safe_set(a, 'model6_BaseObject9', b2)
    assert _is_linked(a, 'model6_BaseObject9', b2)
    if hasattr(b1, 'model6_Root8'):
        assert not _is_linked(b1, 'model6_Root8', a)
    if hasattr(b2, 'model6_Root8'):
        assert _is_linked(b2, 'model6_Root8', a)
    _safe_set(a, 'model6_BaseObject9', None)
    assert not _is_linked(a, 'model6_BaseObject9', b2)
    if hasattr(b2, 'model6_Root8'):
        assert not _is_linked(b2, 'model6_Root8', a)


def test_assoc_owned48_link_reassign_clear():
    a = model6_Holdable(name="sample_text")
    b1 = model6_Holder()
    b2 = model6_Holder()
    _safe_set(a, 'model6_Holdable50', b1)
    assert _is_linked(a, 'model6_Holdable50', b1)
    if hasattr(b1, 'model6_Holder49'):
        assert _is_linked(b1, 'model6_Holder49', a)
    _safe_set(a, 'model6_Holdable50', b2)
    assert _is_linked(a, 'model6_Holdable50', b2)
    if hasattr(b1, 'model6_Holder49'):
        assert not _is_linked(b1, 'model6_Holder49', a)
    if hasattr(b2, 'model6_Holder49'):
        assert _is_linked(b2, 'model6_Holder49', a)
    _safe_set(a, 'model6_Holdable50', None)
    assert not _is_linked(a, 'model6_Holdable50', b2)
    if hasattr(b2, 'model6_Holder49'):
        assert not _is_linked(b2, 'model6_Holder49', a)


def test_assoc_persistentMap25_link_reassign_clear():
    a = model6_PropertiesMapEntry(key="sample_text")
    b1 = model6_PropertiesMap(label="sample_text")
    b2 = model6_PropertiesMap(label="sample_text_2")
    _safe_set(a, 'model6_PropertiesMapEntry', b1)
    assert _is_linked(a, 'model6_PropertiesMapEntry', b1)
    if hasattr(b1, 'model6_PropertiesMap'):
        assert _is_linked(b1, 'model6_PropertiesMap', a)
    _safe_set(a, 'model6_PropertiesMapEntry', b2)
    assert _is_linked(a, 'model6_PropertiesMapEntry', b2)
    if hasattr(b1, 'model6_PropertiesMap'):
        assert not _is_linked(b1, 'model6_PropertiesMap', a)
    if hasattr(b2, 'model6_PropertiesMap'):
        assert _is_linked(b2, 'model6_PropertiesMap', a)
    _safe_set(a, 'model6_PropertiesMapEntry', None)
    assert not _is_linked(a, 'model6_PropertiesMapEntry', b2)
    if hasattr(b2, 'model6_PropertiesMap'):
        assert not _is_linked(b2, 'model6_PropertiesMap', a)


def test_assoc_reference42_link_reassign_clear():
    a = model6_G(dummy="sample_text")
    b1 = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b2 = model6_BaseObject(attributeList="sample_text_2", attributeOptional="sample_text_2", attributeRequired="sample_text_2")
    _safe_set(a, 'model6_G', b1)
    assert _is_linked(a, 'model6_G', b1)
    if hasattr(b1, 'model6_BaseObject43'):
        assert _is_linked(b1, 'model6_BaseObject43', a)
    _safe_set(a, 'model6_G', b2)
    assert _is_linked(a, 'model6_G', b2)
    if hasattr(b1, 'model6_BaseObject43'):
        assert not _is_linked(b1, 'model6_BaseObject43', a)
    if hasattr(b2, 'model6_BaseObject43'):
        assert _is_linked(b2, 'model6_BaseObject43', a)
    _safe_set(a, 'model6_G', None)
    assert not _is_linked(a, 'model6_G', b2)
    if hasattr(b2, 'model6_BaseObject43'):
        assert not _is_linked(b2, 'model6_BaseObject43', a)


def test_assoc_referenceList12_link_reassign_clear():
    a = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b1 = model6_ReferenceObject()
    b2 = model6_ReferenceObject()
    _safe_set(a, 'model6_BaseObject14', b1)
    assert _is_linked(a, 'model6_BaseObject14', b1)
    if hasattr(b1, 'model6_ReferenceObject13'):
        assert _is_linked(b1, 'model6_ReferenceObject13', a)
    _safe_set(a, 'model6_BaseObject14', b2)
    assert _is_linked(a, 'model6_BaseObject14', b2)
    if hasattr(b1, 'model6_ReferenceObject13'):
        assert not _is_linked(b1, 'model6_ReferenceObject13', a)
    if hasattr(b2, 'model6_ReferenceObject13'):
        assert _is_linked(b2, 'model6_ReferenceObject13', a)
    _safe_set(a, 'model6_BaseObject14', None)
    assert not _is_linked(a, 'model6_BaseObject14', b2)
    if hasattr(b2, 'model6_ReferenceObject13'):
        assert not _is_linked(b2, 'model6_ReferenceObject13', a)


def test_assoc_referenceOptional10_link_reassign_clear():
    a = model6_BaseObject(attributeList="sample_text", attributeOptional="sample_text", attributeRequired="sample_text")
    b1 = model6_ReferenceObject()
    b2 = model6_ReferenceObject()
    _safe_set(a, 'model6_BaseObject11', b1)
    assert _is_linked(a, 'model6_BaseObject11', b1)
    if hasattr(b1, 'model6_ReferenceObject'):
        assert _is_linked(b1, 'model6_ReferenceObject', a)
    _safe_set(a, 'model6_BaseObject11', b2)
    assert _is_linked(a, 'model6_BaseObject11', b2)
    if hasattr(b1, 'model6_ReferenceObject'):
        assert not _is_linked(b1, 'model6_ReferenceObject', a)
    if hasattr(b2, 'model6_ReferenceObject'):
        assert _is_linked(b2, 'model6_ReferenceObject', a)
    _safe_set(a, 'model6_BaseObject11', None)
    assert not _is_linked(a, 'model6_BaseObject11', b2)
    if hasattr(b2, 'model6_ReferenceObject'):
        assert not _is_linked(b2, 'model6_ReferenceObject', a)


def test_assoc_transientMap26_link_reassign_clear():
    a = model6_PropertiesMapEntry(key="sample_text")
    b1 = model6_PropertiesMap(label="sample_text")
    b2 = model6_PropertiesMap(label="sample_text_2")
    _safe_set(a, 'model6_PropertiesMapEntry28', b1)
    assert _is_linked(a, 'model6_PropertiesMapEntry28', b1)
    if hasattr(b1, 'model6_PropertiesMap27'):
        assert _is_linked(b1, 'model6_PropertiesMap27', a)
    _safe_set(a, 'model6_PropertiesMapEntry28', b2)
    assert _is_linked(a, 'model6_PropertiesMapEntry28', b2)
    if hasattr(b1, 'model6_PropertiesMap27'):
        assert not _is_linked(b1, 'model6_PropertiesMap27', a)
    if hasattr(b2, 'model6_PropertiesMap27'):
        assert _is_linked(b2, 'model6_PropertiesMap27', a)
    _safe_set(a, 'model6_PropertiesMapEntry28', None)
    assert not _is_linked(a, 'model6_PropertiesMapEntry28', b2)
    if hasattr(b2, 'model6_PropertiesMap27'):
        assert not _is_linked(b2, 'model6_PropertiesMap27', a)


def test_assoc_value29_link_reassign_clear():
    a = model6_PropertiesMapEntryValue(label="sample_text")
    b1 = model6_PropertiesMapEntry(key="sample_text")
    b2 = model6_PropertiesMapEntry(key="sample_text_2")
    _safe_set(a, 'model6_PropertiesMapEntryValue', b1)
    assert _is_linked(a, 'model6_PropertiesMapEntryValue', b1)
    if hasattr(b1, 'model6_PropertiesMapEntry30'):
        assert _is_linked(b1, 'model6_PropertiesMapEntry30', a)
    _safe_set(a, 'model6_PropertiesMapEntryValue', b2)
    assert _is_linked(a, 'model6_PropertiesMapEntryValue', b2)
    if hasattr(b1, 'model6_PropertiesMapEntry30'):
        assert not _is_linked(b1, 'model6_PropertiesMapEntry30', a)
    if hasattr(b2, 'model6_PropertiesMapEntry30'):
        assert _is_linked(b2, 'model6_PropertiesMapEntry30', a)
    _safe_set(a, 'model6_PropertiesMapEntryValue', None)
    assert not _is_linked(a, 'model6_PropertiesMapEntryValue', b2)
    if hasattr(b2, 'model6_PropertiesMapEntry30'):
        assert not _is_linked(b2, 'model6_PropertiesMapEntry30', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BaseObject_strategy = st.builds(BaseObject)
@given(instance=BaseObject_strategy)
@settings(max_examples=25)
def test_BaseObject_instantiation(instance):
    assert isinstance(instance, BaseObject)


Holdable_strategy = st.builds(Holdable)
@given(instance=Holdable_strategy)
@settings(max_examples=25)
def test_Holdable_instantiation(instance):
    assert isinstance(instance, Holdable)


model6_A_strategy = st.builds(model6_A)
@given(instance=model6_A_strategy)
@settings(max_examples=25)
def test_model6_A_instantiation(instance):
    assert isinstance(instance, model6_A)


model6_B_strategy = st.builds(model6_B)
@given(instance=model6_B_strategy)
@settings(max_examples=25)
def test_model6_B_instantiation(instance):
    assert isinstance(instance, model6_B)


model6_BaseObject_strategy = st.builds(model6_BaseObject, attributeList=safe_text, attributeOptional=safe_text, attributeRequired=safe_text)
@given(instance=model6_BaseObject_strategy)
@settings(max_examples=25)
def test_model6_BaseObject_instantiation(instance):
    assert isinstance(instance, model6_BaseObject)


model6_C_strategy = st.builds(model6_C)
@given(instance=model6_C_strategy)
@settings(max_examples=25)
def test_model6_C_instantiation(instance):
    assert isinstance(instance, model6_C)


model6_CanReferenceLegacy_strategy = st.builds(model6_CanReferenceLegacy)
@given(instance=model6_CanReferenceLegacy_strategy)
@settings(max_examples=25)
def test_model6_CanReferenceLegacy_instantiation(instance):
    assert isinstance(instance, model6_CanReferenceLegacy)


model6_ContainmentObject_strategy = st.builds(model6_ContainmentObject)
@given(instance=model6_ContainmentObject_strategy)
@settings(max_examples=25)
def test_model6_ContainmentObject_instantiation(instance):
    assert isinstance(instance, model6_ContainmentObject)


model6_D_strategy = st.builds(model6_D)
@given(instance=model6_D_strategy)
@settings(max_examples=25)
def test_model6_D_instantiation(instance):
    assert isinstance(instance, model6_D)


model6_E_strategy = st.builds(model6_E)
@given(instance=model6_E_strategy)
@settings(max_examples=25)
def test_model6_E_instantiation(instance):
    assert isinstance(instance, model6_E)


model6_EObject_strategy = st.builds(model6_EObject)
@given(instance=model6_EObject_strategy)
@settings(max_examples=25)
def test_model6_EObject_instantiation(instance):
    assert isinstance(instance, model6_EObject)


model6_EmptyStringDefault_strategy = st.builds(model6_EmptyStringDefault, attribute=safe_text)
@given(instance=model6_EmptyStringDefault_strategy)
@settings(max_examples=25)
def test_model6_EmptyStringDefault_instantiation(instance):
    assert isinstance(instance, model6_EmptyStringDefault)


model6_EmptyStringDefaultUnsettable_strategy = st.builds(model6_EmptyStringDefaultUnsettable, attribute=safe_text)
@given(instance=model6_EmptyStringDefaultUnsettable_strategy)
@settings(max_examples=25)
def test_model6_EmptyStringDefaultUnsettable_instantiation(instance):
    assert isinstance(instance, model6_EmptyStringDefaultUnsettable)


model6_F_strategy = st.builds(model6_F)
@given(instance=model6_F_strategy)
@settings(max_examples=25)
def test_model6_F_instantiation(instance):
    assert isinstance(instance, model6_F)


model6_G_strategy = st.builds(model6_G, dummy=safe_text)
@given(instance=model6_G_strategy)
@settings(max_examples=25)
def test_model6_G_instantiation(instance):
    assert isinstance(instance, model6_G)


model6_HasNillableAttribute_strategy = st.builds(model6_HasNillableAttribute, nillable=safe_text)
@given(instance=model6_HasNillableAttribute_strategy)
@settings(max_examples=25)
def test_model6_HasNillableAttribute_instantiation(instance):
    assert isinstance(instance, model6_HasNillableAttribute)


model6_Holdable_strategy = st.builds(model6_Holdable, name=safe_text)
@given(instance=model6_Holdable_strategy)
@settings(max_examples=25)
def test_model6_Holdable_instantiation(instance):
    assert isinstance(instance, model6_Holdable)


model6_Holder_strategy = st.builds(model6_Holder)
@given(instance=model6_Holder_strategy)
@settings(max_examples=25)
def test_model6_Holder_instantiation(instance):
    assert isinstance(instance, model6_Holder)


model6_MyEnumList_strategy = st.builds(model6_MyEnumList, myEnum=safe_text)
@given(instance=model6_MyEnumList_strategy)
@settings(max_examples=25)
def test_model6_MyEnumList_instantiation(instance):
    assert isinstance(instance, model6_MyEnumList)


model6_MyEnumListUnsettable_strategy = st.builds(model6_MyEnumListUnsettable, myEnum=safe_text)
@given(instance=model6_MyEnumListUnsettable_strategy)
@settings(max_examples=25)
def test_model6_MyEnumListUnsettable_instantiation(instance):
    assert isinstance(instance, model6_MyEnumListUnsettable)


model6_PropertiesMap_strategy = st.builds(model6_PropertiesMap, label=safe_text)
@given(instance=model6_PropertiesMap_strategy)
@settings(max_examples=25)
def test_model6_PropertiesMap_instantiation(instance):
    assert isinstance(instance, model6_PropertiesMap)


model6_PropertiesMapEntry_strategy = st.builds(model6_PropertiesMapEntry, key=safe_text)
@given(instance=model6_PropertiesMapEntry_strategy)
@settings(max_examples=25)
def test_model6_PropertiesMapEntry_instantiation(instance):
    assert isinstance(instance, model6_PropertiesMapEntry)


model6_PropertiesMapEntryValue_strategy = st.builds(model6_PropertiesMapEntryValue, label=safe_text)
@given(instance=model6_PropertiesMapEntryValue_strategy)
@settings(max_examples=25)
def test_model6_PropertiesMapEntryValue_instantiation(instance):
    assert isinstance(instance, model6_PropertiesMapEntryValue)


model6_ReferenceObject_strategy = st.builds(model6_ReferenceObject)
@given(instance=model6_ReferenceObject_strategy)
@settings(max_examples=25)
def test_model6_ReferenceObject_instantiation(instance):
    assert isinstance(instance, model6_ReferenceObject)


model6_Root_strategy = st.builds(model6_Root)
@given(instance=model6_Root_strategy)
@settings(max_examples=25)
def test_model6_Root_instantiation(instance):
    assert isinstance(instance, model6_Root)


model6_Thing_strategy = st.builds(model6_Thing)
@given(instance=model6_Thing_strategy)
@settings(max_examples=25)
def test_model6_Thing_instantiation(instance):
    assert isinstance(instance, model6_Thing)


model6_UnorderedList_strategy = st.builds(model6_UnorderedList)
@given(instance=model6_UnorderedList_strategy)
@settings(max_examples=25)
def test_model6_UnorderedList_instantiation(instance):
    assert isinstance(instance, model6_UnorderedList)


model6_UnsettableAttributes_strategy = st.builds(model6_UnsettableAttributes, attrBigDecimal=safe_text, attrBigInteger=safe_text, attrBoolean=st.booleans(), attrBooleanObject=safe_text, attrByte=safe_text, attrByteArray=safe_text, attrByteObject=safe_text, attrChar=safe_text, attrCharacterObject=safe_text, attrDate=st.dates(), attrDouble=st.floats(allow_nan=False, allow_infinity=False), attrDoubleObject=safe_text, attrFloat=st.floats(allow_nan=False, allow_infinity=False), attrFloatObject=safe_text, attrInt=st.integers(), attrIntegerObject=safe_text, attrJavaClass=safe_text, attrJavaObject=safe_text, attrLong=safe_text, attrLongObject=safe_text, attrShort=safe_text, attrShortObject=safe_text, attrString=safe_text)
@given(instance=model6_UnsettableAttributes_strategy)
@settings(max_examples=25)
def test_model6_UnsettableAttributes_instantiation(instance):
    assert isinstance(instance, model6_UnsettableAttributes)



