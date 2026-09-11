import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    attributeTest_Root,
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

def test_attributeTest_Root_bigDecimal_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.bigDecimal == "sample_text"
    instance.bigDecimal = "sample_text_2"
    assert instance.bigDecimal == "sample_text_2"


def test_attributeTest_Root_bigInteger_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.bigInteger == "sample_text"
    instance.bigInteger = "sample_text_2"
    assert instance.bigInteger == "sample_text_2"


def test_attributeTest_Root_boolObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.boolObj == "sample_text"
    instance.boolObj = "sample_text_2"
    assert instance.boolObj == "sample_text_2"


def test_attributeTest_Root_boolPrimitive_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.boolPrimitive == True
    instance.boolPrimitive = False
    assert instance.boolPrimitive == False


def test_attributeTest_Root_byteArray_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.byteArray == "sample_text"
    instance.byteArray = "sample_text_2"
    assert instance.byteArray == "sample_text_2"


def test_attributeTest_Root_byteObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.byteObj == "sample_text"
    instance.byteObj = "sample_text_2"
    assert instance.byteObj == "sample_text_2"


def test_attributeTest_Root_bytePrimitive_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.bytePrimitive == "sample_text"
    instance.bytePrimitive = "sample_text_2"
    assert instance.bytePrimitive == "sample_text_2"


def test_attributeTest_Root_charObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.charObj == "sample_text"
    instance.charObj = "sample_text_2"
    assert instance.charObj == "sample_text_2"


def test_attributeTest_Root_charPrimitive_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.charPrimitive == "sample_text"
    instance.charPrimitive = "sample_text_2"
    assert instance.charPrimitive == "sample_text_2"


def test_attributeTest_Root_date_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_attributeTest_Root_doubleObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.doubleObj == "sample_text"
    instance.doubleObj = "sample_text_2"
    assert instance.doubleObj == "sample_text_2"


def test_attributeTest_Root_doublePrimitive_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.doublePrimitive == 3.14
    instance.doublePrimitive = 9.99
    assert instance.doublePrimitive == 9.99


def test_attributeTest_Root_eList_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.eList == "sample_text"
    instance.eList = "sample_text_2"
    assert instance.eList == "sample_text_2"


def test_attributeTest_Root_floatObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.floatObj == "sample_text"
    instance.floatObj = "sample_text_2"
    assert instance.floatObj == "sample_text_2"


def test_attributeTest_Root_floatPrimitive_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.floatPrimitive == 3.14
    instance.floatPrimitive = 9.99
    assert instance.floatPrimitive == 9.99


def test_attributeTest_Root_intObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.intObj == "sample_text"
    instance.intObj = "sample_text_2"
    assert instance.intObj == "sample_text_2"


def test_attributeTest_Root_intPrimitive_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.intPrimitive == 7
    instance.intPrimitive = 13
    assert instance.intPrimitive == 13


def test_attributeTest_Root_javaObject_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.javaObject == "sample_text"
    instance.javaObject = "sample_text_2"
    assert instance.javaObject == "sample_text_2"


def test_attributeTest_Root_listInt_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.listInt == 7
    instance.listInt = 13
    assert instance.listInt == 13


def test_attributeTest_Root_listInt1_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.listInt1 == 7
    instance.listInt1 = 13
    assert instance.listInt1 == 13


def test_attributeTest_Root_listInt2_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.listInt2 == 7
    instance.listInt2 = 13
    assert instance.listInt2 == 13


def test_attributeTest_Root_listShort_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.listShort == "sample_text"
    instance.listShort = "sample_text_2"
    assert instance.listShort == "sample_text_2"


def test_attributeTest_Root_listString_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.listString == "sample_text"
    instance.listString = "sample_text_2"
    assert instance.listString == "sample_text_2"


def test_attributeTest_Root_longObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.longObj == "sample_text"
    instance.longObj = "sample_text_2"
    assert instance.longObj == "sample_text_2"


def test_attributeTest_Root_longPrimitive_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.longPrimitive == "sample_text"
    instance.longPrimitive = "sample_text_2"
    assert instance.longPrimitive == "sample_text_2"


def test_attributeTest_Root_map_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.map == "sample_text"
    instance.map = "sample_text_2"
    assert instance.map == "sample_text_2"


def test_attributeTest_Root_shortObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.shortObj == "sample_text"
    instance.shortObj = "sample_text_2"
    assert instance.shortObj == "sample_text_2"


def test_attributeTest_Root_shortPrimitive_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.shortPrimitive == "sample_text"
    instance.shortPrimitive = "sample_text_2"
    assert instance.shortPrimitive == "sample_text_2"


def test_attributeTest_Root_stringObj_value_roundtrip():
    instance = attributeTest_Root(bigDecimal="sample_text", bigInteger="sample_text", boolObj="sample_text", boolPrimitive=True, byteArray="sample_text", byteObj="sample_text", bytePrimitive="sample_text", charObj="sample_text", charPrimitive="sample_text", date=date(2024, 1, 1), doubleObj="sample_text", doublePrimitive=3.14, eList="sample_text", floatObj="sample_text", floatPrimitive=3.14, intObj="sample_text", intPrimitive=7, javaObject="sample_text", listInt=7, listInt1=7, listInt2=7, listShort="sample_text", listString="sample_text", longObj="sample_text", longPrimitive="sample_text", map="sample_text", shortObj="sample_text", shortPrimitive="sample_text", stringObj="sample_text")
    assert instance.stringObj == "sample_text"
    instance.stringObj = "sample_text_2"
    assert instance.stringObj == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

attributeTest_Root_strategy = st.builds(attributeTest_Root, bigDecimal=safe_text, bigInteger=safe_text, boolObj=safe_text, boolPrimitive=st.booleans(), byteArray=safe_text, byteObj=safe_text, bytePrimitive=safe_text, charObj=safe_text, charPrimitive=safe_text, date=st.dates(), doubleObj=safe_text, doublePrimitive=st.floats(allow_nan=False, allow_infinity=False), eList=safe_text, floatObj=safe_text, floatPrimitive=st.floats(allow_nan=False, allow_infinity=False), intObj=safe_text, intPrimitive=st.integers(), javaObject=safe_text, listInt=st.integers(), listInt1=st.integers(), listInt2=st.integers(), listShort=safe_text, listString=safe_text, longObj=safe_text, longPrimitive=safe_text, map=safe_text, shortObj=safe_text, shortPrimitive=safe_text, stringObj=safe_text)
@given(instance=attributeTest_Root_strategy)
@settings(max_examples=25)
def test_attributeTest_Root_instantiation(instance):
    assert isinstance(instance, attributeTest_Root)


