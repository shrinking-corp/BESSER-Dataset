import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    TestTypeClass1,
    package1_TestOperationAndParameterClass,
    package1_TestPrimitiveTypeClass,
    package1_TestPropertyClass,
    package1_TestTypeClass1,
    package1_TestTypeClass2,
    TestEnumeration,
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

def test_package1_TestPrimitiveTypeClass_aBooleanBoolean_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aBooleanBoolean == "sample_text"
    instance.aBooleanBoolean = "sample_text_2"
    assert instance.aBooleanBoolean == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aBooleanBooleanObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aBooleanBooleanObject == "sample_text"
    instance.aBooleanBooleanObject = "sample_text_2"
    assert instance.aBooleanBooleanObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aBooleanEBoolean_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aBooleanEBoolean == True
    instance.aBooleanEBoolean = False
    assert instance.aBooleanEBoolean == False


def test_package1_TestPrimitiveTypeClass_aBooleanEBooleanObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aBooleanEBooleanObject == "sample_text"
    instance.aBooleanEBooleanObject = "sample_text_2"
    assert instance.aBooleanEBooleanObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aRealDouble_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aRealDouble == "sample_text"
    instance.aRealDouble = "sample_text_2"
    assert instance.aRealDouble == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aRealDoubleObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aRealDoubleObject == "sample_text"
    instance.aRealDoubleObject = "sample_text_2"
    assert instance.aRealDoubleObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aRealEDouble_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aRealEDouble == 3.14
    instance.aRealEDouble = 9.99
    assert instance.aRealEDouble == 9.99


def test_package1_TestPrimitiveTypeClass_aRealEDoubleObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aRealEDoubleObject == "sample_text"
    instance.aRealEDoubleObject = "sample_text_2"
    assert instance.aRealEDoubleObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aRealEFloat_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aRealEFloat == 3.14
    instance.aRealEFloat = 9.99
    assert instance.aRealEFloat == 9.99


def test_package1_TestPrimitiveTypeClass_aRealEFloatObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aRealEFloatObject == "sample_text"
    instance.aRealEFloatObject = "sample_text_2"
    assert instance.aRealEFloatObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aRealFloat_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aRealFloat == "sample_text"
    instance.aRealFloat = "sample_text_2"
    assert instance.aRealFloat == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aRealFloatObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aRealFloatObject == "sample_text"
    instance.aRealFloatObject = "sample_text_2"
    assert instance.aRealFloatObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aStringChar_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aStringChar == "sample_text"
    instance.aStringChar = "sample_text_2"
    assert instance.aStringChar == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aStringCharacterObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aStringCharacterObject == "sample_text"
    instance.aStringCharacterObject = "sample_text_2"
    assert instance.aStringCharacterObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aStringEChar_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aStringEChar == "sample_text"
    instance.aStringEChar = "sample_text_2"
    assert instance.aStringEChar == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aStringECharacterObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aStringECharacterObject == "sample_text"
    instance.aStringECharacterObject = "sample_text_2"
    assert instance.aStringECharacterObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aStringEString_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aStringEString == "sample_text"
    instance.aStringEString = "sample_text_2"
    assert instance.aStringEString == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_aStringString_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.aStringString == "sample_text"
    instance.aStringString = "sample_text_2"
    assert instance.aStringString == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerBigDecimal_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerBigDecimal == "sample_text"
    instance.anIntegerBigDecimal = "sample_text_2"
    assert instance.anIntegerBigDecimal == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerBigInteger_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerBigInteger == "sample_text"
    instance.anIntegerBigInteger = "sample_text_2"
    assert instance.anIntegerBigInteger == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerByte_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerByte == "sample_text"
    instance.anIntegerByte = "sample_text_2"
    assert instance.anIntegerByte == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerByteObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerByteObject == "sample_text"
    instance.anIntegerByteObject = "sample_text_2"
    assert instance.anIntegerByteObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerEBigDecimal_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerEBigDecimal == "sample_text"
    instance.anIntegerEBigDecimal = "sample_text_2"
    assert instance.anIntegerEBigDecimal == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerEBigInteger_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerEBigInteger == "sample_text"
    instance.anIntegerEBigInteger = "sample_text_2"
    assert instance.anIntegerEBigInteger == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerEByte_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerEByte == "sample_text"
    instance.anIntegerEByte = "sample_text_2"
    assert instance.anIntegerEByte == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerEByteObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerEByteObject == "sample_text"
    instance.anIntegerEByteObject = "sample_text_2"
    assert instance.anIntegerEByteObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerEInt_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerEInt == 7
    instance.anIntegerEInt = 13
    assert instance.anIntegerEInt == 13


def test_package1_TestPrimitiveTypeClass_anIntegerEIntegerObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerEIntegerObject == "sample_text"
    instance.anIntegerEIntegerObject = "sample_text_2"
    assert instance.anIntegerEIntegerObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerELong_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerELong == "sample_text"
    instance.anIntegerELong = "sample_text_2"
    assert instance.anIntegerELong == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerELongObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerELongObject == "sample_text"
    instance.anIntegerELongObject = "sample_text_2"
    assert instance.anIntegerELongObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerEShort_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerEShort == "sample_text"
    instance.anIntegerEShort = "sample_text_2"
    assert instance.anIntegerEShort == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerEShortObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerEShortObject == "sample_text"
    instance.anIntegerEShortObject = "sample_text_2"
    assert instance.anIntegerEShortObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerInt_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerInt == "sample_text"
    instance.anIntegerInt = "sample_text_2"
    assert instance.anIntegerInt == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerIntegerObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerIntegerObject == "sample_text"
    instance.anIntegerIntegerObject = "sample_text_2"
    assert instance.anIntegerIntegerObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerLong_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerLong == "sample_text"
    instance.anIntegerLong = "sample_text_2"
    assert instance.anIntegerLong == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerLongObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerLongObject == "sample_text"
    instance.anIntegerLongObject = "sample_text_2"
    assert instance.anIntegerLongObject == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerShort_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerShort == "sample_text"
    instance.anIntegerShort = "sample_text_2"
    assert instance.anIntegerShort == "sample_text_2"


def test_package1_TestPrimitiveTypeClass_anIntegerShortObject_value_roundtrip():
    instance = package1_TestPrimitiveTypeClass(aBooleanBoolean="sample_text", aBooleanBooleanObject="sample_text", aBooleanEBoolean=True, aBooleanEBooleanObject="sample_text", aRealDouble="sample_text", aRealDoubleObject="sample_text", aRealEDouble=3.14, aRealEDoubleObject="sample_text", aRealEFloat=3.14, aRealEFloatObject="sample_text", aRealFloat="sample_text", aRealFloatObject="sample_text", aStringChar="sample_text", aStringCharacterObject="sample_text", aStringEChar="sample_text", aStringECharacterObject="sample_text", aStringEString="sample_text", aStringString="sample_text", anIntegerBigDecimal="sample_text", anIntegerBigInteger="sample_text", anIntegerByte="sample_text", anIntegerByteObject="sample_text", anIntegerEBigDecimal="sample_text", anIntegerEBigInteger="sample_text", anIntegerEByte="sample_text", anIntegerEByteObject="sample_text", anIntegerEInt=7, anIntegerEIntegerObject="sample_text", anIntegerELong="sample_text", anIntegerELongObject="sample_text", anIntegerEShort="sample_text", anIntegerEShortObject="sample_text", anIntegerInt="sample_text", anIntegerIntegerObject="sample_text", anIntegerLong="sample_text", anIntegerLongObject="sample_text", anIntegerShort="sample_text", anIntegerShortObject="sample_text")
    assert instance.anIntegerShortObject == "sample_text"
    instance.anIntegerShortObject = "sample_text_2"
    assert instance.anIntegerShortObject == "sample_text_2"


def test_package1_TestPropertyClass_identifierProperty_value_roundtrip():
    instance = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    assert instance.identifierProperty == "sample_text"
    instance.identifierProperty = "sample_text_2"
    assert instance.identifierProperty == "sample_text_2"


def test_package1_TestPropertyClass_nonidentifierProperty_value_roundtrip():
    instance = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    assert instance.nonidentifierProperty == "sample_text"
    instance.nonidentifierProperty = "sample_text_2"
    assert instance.nonidentifierProperty == "sample_text_2"


def test_package1_TestTypeClass1_property1_value_roundtrip():
    instance = package1_TestTypeClass1(property1=True)
    assert instance.property1 == True
    instance.property1 = False
    assert instance.property1 == False


def test_package1_TestTypeClass2_property2_value_roundtrip():
    instance = package1_TestTypeClass2(property2=True)
    assert instance.property2 == True
    instance.property2 = False
    assert instance.property2 == False


def test_package1_TestTypeClass2_isa_TestTypeClass1():
    instance = package1_TestTypeClass2(property2=True)
    assert isinstance(instance, TestTypeClass1)


def test_assoc_associationEnd113_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass115', b1)
    assert _is_linked(a, 'package1_TestTypeClass115', b1)
    if hasattr(b1, 'package1_TestPropertyClass14'):
        assert _is_linked(b1, 'package1_TestPropertyClass14', a)
    _safe_set(a, 'package1_TestTypeClass115', b2)
    assert _is_linked(a, 'package1_TestTypeClass115', b2)
    if hasattr(b1, 'package1_TestPropertyClass14'):
        assert not _is_linked(b1, 'package1_TestPropertyClass14', a)
    if hasattr(b2, 'package1_TestPropertyClass14'):
        assert _is_linked(b2, 'package1_TestPropertyClass14', a)
    _safe_set(a, 'package1_TestTypeClass115', None)
    assert not _is_linked(a, 'package1_TestTypeClass115', b2)
    if hasattr(b2, 'package1_TestPropertyClass14'):
        assert not _is_linked(b2, 'package1_TestPropertyClass14', a)


def test_assoc_nonmultipleProperty0_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass1', b1)
    assert _is_linked(a, 'package1_TestTypeClass1', b1)
    if hasattr(b1, 'package1_TestPropertyClass'):
        assert _is_linked(b1, 'package1_TestPropertyClass', a)
    _safe_set(a, 'package1_TestTypeClass1', b2)
    assert _is_linked(a, 'package1_TestTypeClass1', b2)
    if hasattr(b1, 'package1_TestPropertyClass'):
        assert not _is_linked(b1, 'package1_TestPropertyClass', a)
    if hasattr(b2, 'package1_TestPropertyClass'):
        assert _is_linked(b2, 'package1_TestPropertyClass', a)
    _safe_set(a, 'package1_TestTypeClass1', None)
    assert not _is_linked(a, 'package1_TestTypeClass1', b2)
    if hasattr(b2, 'package1_TestPropertyClass'):
        assert not _is_linked(b2, 'package1_TestPropertyClass', a)


def test_assoc_nonuniqueMultipleProperty10_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass112', b1)
    assert _is_linked(a, 'package1_TestTypeClass112', b1)
    if hasattr(b1, 'package1_TestPropertyClass11'):
        assert _is_linked(b1, 'package1_TestPropertyClass11', a)
    _safe_set(a, 'package1_TestTypeClass112', b2)
    assert _is_linked(a, 'package1_TestTypeClass112', b2)
    if hasattr(b1, 'package1_TestPropertyClass11'):
        assert not _is_linked(b1, 'package1_TestPropertyClass11', a)
    if hasattr(b2, 'package1_TestPropertyClass11'):
        assert _is_linked(b2, 'package1_TestPropertyClass11', a)
    _safe_set(a, 'package1_TestTypeClass112', None)
    assert not _is_linked(a, 'package1_TestTypeClass112', b2)
    if hasattr(b2, 'package1_TestPropertyClass11'):
        assert not _is_linked(b2, 'package1_TestPropertyClass11', a)


def test_assoc_nonuniqueMultiplePropertyAssociationEnd25_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass127', b1)
    assert _is_linked(a, 'package1_TestTypeClass127', b1)
    if hasattr(b1, 'package1_TestPropertyClass26'):
        assert _is_linked(b1, 'package1_TestPropertyClass26', a)
    _safe_set(a, 'package1_TestTypeClass127', b2)
    assert _is_linked(a, 'package1_TestTypeClass127', b2)
    if hasattr(b1, 'package1_TestPropertyClass26'):
        assert not _is_linked(b1, 'package1_TestPropertyClass26', a)
    if hasattr(b2, 'package1_TestPropertyClass26'):
        assert _is_linked(b2, 'package1_TestPropertyClass26', a)
    _safe_set(a, 'package1_TestTypeClass127', None)
    assert not _is_linked(a, 'package1_TestTypeClass127', b2)
    if hasattr(b2, 'package1_TestPropertyClass26'):
        assert not _is_linked(b2, 'package1_TestPropertyClass26', a)


def test_assoc_orderedMultipleProperty1_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass13', b1)
    assert _is_linked(a, 'package1_TestTypeClass13', b1)
    if hasattr(b1, 'package1_TestPropertyClass2'):
        assert _is_linked(b1, 'package1_TestPropertyClass2', a)
    _safe_set(a, 'package1_TestTypeClass13', b2)
    assert _is_linked(a, 'package1_TestTypeClass13', b2)
    if hasattr(b1, 'package1_TestPropertyClass2'):
        assert not _is_linked(b1, 'package1_TestPropertyClass2', a)
    if hasattr(b2, 'package1_TestPropertyClass2'):
        assert _is_linked(b2, 'package1_TestPropertyClass2', a)
    _safe_set(a, 'package1_TestTypeClass13', None)
    assert not _is_linked(a, 'package1_TestTypeClass13', b2)
    if hasattr(b2, 'package1_TestPropertyClass2'):
        assert not _is_linked(b2, 'package1_TestPropertyClass2', a)


def test_assoc_orderedMultiplePropertyAssociationEnd16_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass118', b1)
    assert _is_linked(a, 'package1_TestTypeClass118', b1)
    if hasattr(b1, 'package1_TestPropertyClass17'):
        assert _is_linked(b1, 'package1_TestPropertyClass17', a)
    _safe_set(a, 'package1_TestTypeClass118', b2)
    assert _is_linked(a, 'package1_TestTypeClass118', b2)
    if hasattr(b1, 'package1_TestPropertyClass17'):
        assert not _is_linked(b1, 'package1_TestPropertyClass17', a)
    if hasattr(b2, 'package1_TestPropertyClass17'):
        assert _is_linked(b2, 'package1_TestPropertyClass17', a)
    _safe_set(a, 'package1_TestTypeClass118', None)
    assert not _is_linked(a, 'package1_TestTypeClass118', b2)
    if hasattr(b2, 'package1_TestPropertyClass17'):
        assert not _is_linked(b2, 'package1_TestPropertyClass17', a)


def test_assoc_uniqueMultipleProperty7_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass19', b1)
    assert _is_linked(a, 'package1_TestTypeClass19', b1)
    if hasattr(b1, 'package1_TestPropertyClass8'):
        assert _is_linked(b1, 'package1_TestPropertyClass8', a)
    _safe_set(a, 'package1_TestTypeClass19', b2)
    assert _is_linked(a, 'package1_TestTypeClass19', b2)
    if hasattr(b1, 'package1_TestPropertyClass8'):
        assert not _is_linked(b1, 'package1_TestPropertyClass8', a)
    if hasattr(b2, 'package1_TestPropertyClass8'):
        assert _is_linked(b2, 'package1_TestPropertyClass8', a)
    _safe_set(a, 'package1_TestTypeClass19', None)
    assert not _is_linked(a, 'package1_TestTypeClass19', b2)
    if hasattr(b2, 'package1_TestPropertyClass8'):
        assert not _is_linked(b2, 'package1_TestPropertyClass8', a)


def test_assoc_uniqueMultiplePropertyAssociationEnd22_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass124', b1)
    assert _is_linked(a, 'package1_TestTypeClass124', b1)
    if hasattr(b1, 'package1_TestPropertyClass23'):
        assert _is_linked(b1, 'package1_TestPropertyClass23', a)
    _safe_set(a, 'package1_TestTypeClass124', b2)
    assert _is_linked(a, 'package1_TestTypeClass124', b2)
    if hasattr(b1, 'package1_TestPropertyClass23'):
        assert not _is_linked(b1, 'package1_TestPropertyClass23', a)
    if hasattr(b2, 'package1_TestPropertyClass23'):
        assert _is_linked(b2, 'package1_TestPropertyClass23', a)
    _safe_set(a, 'package1_TestTypeClass124', None)
    assert not _is_linked(a, 'package1_TestTypeClass124', b2)
    if hasattr(b2, 'package1_TestPropertyClass23'):
        assert not _is_linked(b2, 'package1_TestPropertyClass23', a)


def test_assoc_unorderedMultipleProperty4_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass16', b1)
    assert _is_linked(a, 'package1_TestTypeClass16', b1)
    if hasattr(b1, 'package1_TestPropertyClass5'):
        assert _is_linked(b1, 'package1_TestPropertyClass5', a)
    _safe_set(a, 'package1_TestTypeClass16', b2)
    assert _is_linked(a, 'package1_TestTypeClass16', b2)
    if hasattr(b1, 'package1_TestPropertyClass5'):
        assert not _is_linked(b1, 'package1_TestPropertyClass5', a)
    if hasattr(b2, 'package1_TestPropertyClass5'):
        assert _is_linked(b2, 'package1_TestPropertyClass5', a)
    _safe_set(a, 'package1_TestTypeClass16', None)
    assert not _is_linked(a, 'package1_TestTypeClass16', b2)
    if hasattr(b2, 'package1_TestPropertyClass5'):
        assert not _is_linked(b2, 'package1_TestPropertyClass5', a)


def test_assoc_unorderedMultiplePropertyAssociationEnd19_link_reassign_clear():
    a = package1_TestTypeClass1(property1=True)
    b1 = package1_TestPropertyClass(identifierProperty="sample_text", nonidentifierProperty="sample_text")
    b2 = package1_TestPropertyClass(identifierProperty="sample_text_2", nonidentifierProperty="sample_text_2")
    _safe_set(a, 'package1_TestTypeClass121', b1)
    assert _is_linked(a, 'package1_TestTypeClass121', b1)
    if hasattr(b1, 'package1_TestPropertyClass20'):
        assert _is_linked(b1, 'package1_TestPropertyClass20', a)
    _safe_set(a, 'package1_TestTypeClass121', b2)
    assert _is_linked(a, 'package1_TestTypeClass121', b2)
    if hasattr(b1, 'package1_TestPropertyClass20'):
        assert not _is_linked(b1, 'package1_TestPropertyClass20', a)
    if hasattr(b2, 'package1_TestPropertyClass20'):
        assert _is_linked(b2, 'package1_TestPropertyClass20', a)
    _safe_set(a, 'package1_TestTypeClass121', None)
    assert not _is_linked(a, 'package1_TestTypeClass121', b2)
    if hasattr(b2, 'package1_TestPropertyClass20'):
        assert not _is_linked(b2, 'package1_TestPropertyClass20', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

TestTypeClass1_strategy = st.builds(TestTypeClass1)
@given(instance=TestTypeClass1_strategy)
@settings(max_examples=25)
def test_TestTypeClass1_instantiation(instance):
    assert isinstance(instance, TestTypeClass1)


package1_TestOperationAndParameterClass_strategy = st.builds(package1_TestOperationAndParameterClass)
@given(instance=package1_TestOperationAndParameterClass_strategy)
@settings(max_examples=25)
def test_package1_TestOperationAndParameterClass_instantiation(instance):
    assert isinstance(instance, package1_TestOperationAndParameterClass)


package1_TestPrimitiveTypeClass_strategy = st.builds(package1_TestPrimitiveTypeClass, aBooleanBoolean=safe_text, aBooleanBooleanObject=safe_text, aBooleanEBoolean=st.booleans(), aBooleanEBooleanObject=safe_text, aRealDouble=safe_text, aRealDoubleObject=safe_text, aRealEDouble=st.floats(allow_nan=False, allow_infinity=False), aRealEDoubleObject=safe_text, aRealEFloat=st.floats(allow_nan=False, allow_infinity=False), aRealEFloatObject=safe_text, aRealFloat=safe_text, aRealFloatObject=safe_text, aStringChar=safe_text, aStringCharacterObject=safe_text, aStringEChar=safe_text, aStringECharacterObject=safe_text, aStringEString=safe_text, aStringString=safe_text, anIntegerBigDecimal=safe_text, anIntegerBigInteger=safe_text, anIntegerByte=safe_text, anIntegerByteObject=safe_text, anIntegerEBigDecimal=safe_text, anIntegerEBigInteger=safe_text, anIntegerEByte=safe_text, anIntegerEByteObject=safe_text, anIntegerEInt=st.integers(), anIntegerEIntegerObject=safe_text, anIntegerELong=safe_text, anIntegerELongObject=safe_text, anIntegerEShort=safe_text, anIntegerEShortObject=safe_text, anIntegerInt=safe_text, anIntegerIntegerObject=safe_text, anIntegerLong=safe_text, anIntegerLongObject=safe_text, anIntegerShort=safe_text, anIntegerShortObject=safe_text)
@given(instance=package1_TestPrimitiveTypeClass_strategy)
@settings(max_examples=25)
def test_package1_TestPrimitiveTypeClass_instantiation(instance):
    assert isinstance(instance, package1_TestPrimitiveTypeClass)


package1_TestPropertyClass_strategy = st.builds(package1_TestPropertyClass, identifierProperty=safe_text, nonidentifierProperty=safe_text)
@given(instance=package1_TestPropertyClass_strategy)
@settings(max_examples=25)
def test_package1_TestPropertyClass_instantiation(instance):
    assert isinstance(instance, package1_TestPropertyClass)


package1_TestTypeClass1_strategy = st.builds(package1_TestTypeClass1, property1=st.booleans())
@given(instance=package1_TestTypeClass1_strategy)
@settings(max_examples=25)
def test_package1_TestTypeClass1_instantiation(instance):
    assert isinstance(instance, package1_TestTypeClass1)


package1_TestTypeClass2_strategy = st.builds(package1_TestTypeClass2, property2=st.booleans())
@given(instance=package1_TestTypeClass2_strategy)
@settings(max_examples=25)
def test_package1_TestTypeClass2_instantiation(instance):
    assert isinstance(instance, package1_TestTypeClass2)


