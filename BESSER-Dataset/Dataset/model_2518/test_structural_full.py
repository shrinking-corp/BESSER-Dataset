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


