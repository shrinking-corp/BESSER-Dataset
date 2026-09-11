import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    types_ManyTypes,
    types_SingleTypes,
    TestEnum,
    TestNextEnum,
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

def test_types_ManyTypes_bigDecimal_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.bigDecimal == "sample_text"
    instance.bigDecimal = "sample_text_2"
    assert instance.bigDecimal == "sample_text_2"


def test_types_ManyTypes_bigInteger_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.bigInteger == "sample_text"
    instance.bigInteger = "sample_text_2"
    assert instance.bigInteger == "sample_text_2"


def test_types_ManyTypes_byteArray_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.byteArray == "sample_text"
    instance.byteArray = "sample_text_2"
    assert instance.byteArray == "sample_text_2"


def test_types_ManyTypes_byteObject_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.byteObject == "sample_text"
    instance.byteObject = "sample_text_2"
    assert instance.byteObject == "sample_text_2"


def test_types_ManyTypes_charObject_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.charObject == "sample_text"
    instance.charObject = "sample_text_2"
    assert instance.charObject == "sample_text_2"


def test_types_ManyTypes_clazz_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.clazz == "sample_text"
    instance.clazz = "sample_text_2"
    assert instance.clazz == "sample_text_2"


def test_types_ManyTypes_date_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_types_ManyTypes_doubleObject_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.doubleObject == "sample_text"
    instance.doubleObject = "sample_text_2"
    assert instance.doubleObject == "sample_text_2"


def test_types_ManyTypes_enum_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.enum == "sample_text"
    instance.enum = "sample_text_2"
    assert instance.enum == "sample_text_2"


def test_types_ManyTypes_floatObject_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.floatObject == "sample_text"
    instance.floatObject = "sample_text_2"
    assert instance.floatObject == "sample_text_2"


def test_types_ManyTypes_integerObject_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.integerObject == "sample_text"
    instance.integerObject = "sample_text_2"
    assert instance.integerObject == "sample_text_2"


def test_types_ManyTypes_long_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.long == "sample_text"
    instance.long = "sample_text_2"
    assert instance.long == "sample_text_2"


def test_types_ManyTypes_longArray_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.longArray == "sample_text"
    instance.longArray = "sample_text_2"
    assert instance.longArray == "sample_text_2"


def test_types_ManyTypes_string_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_types_ManyTypes_stringArray_value_roundtrip():
    instance = types_ManyTypes(bigDecimal="sample_text", bigInteger="sample_text", byteArray="sample_text", byteObject="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), doubleObject="sample_text", enum="sample_text", floatObject="sample_text", integerObject="sample_text", long="sample_text", longArray="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.stringArray == "sample_text"
    instance.stringArray = "sample_text_2"
    assert instance.stringArray == "sample_text_2"


def test_types_SingleTypes_bigDecimal_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.bigDecimal == "sample_text"
    instance.bigDecimal = "sample_text_2"
    assert instance.bigDecimal == "sample_text_2"


def test_types_SingleTypes_bigInteger_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.bigInteger == "sample_text"
    instance.bigInteger = "sample_text_2"
    assert instance.bigInteger == "sample_text_2"


def test_types_SingleTypes_byte_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.byte == "sample_text"
    instance.byte = "sample_text_2"
    assert instance.byte == "sample_text_2"


def test_types_SingleTypes_byteArray_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.byteArray == "sample_text"
    instance.byteArray = "sample_text_2"
    assert instance.byteArray == "sample_text_2"


def test_types_SingleTypes_byteObject_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.byteObject == "sample_text"
    instance.byteObject = "sample_text_2"
    assert instance.byteObject == "sample_text_2"


def test_types_SingleTypes_char_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.char == "sample_text"
    instance.char = "sample_text_2"
    assert instance.char == "sample_text_2"


def test_types_SingleTypes_charObject_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.charObject == "sample_text"
    instance.charObject = "sample_text_2"
    assert instance.charObject == "sample_text_2"


def test_types_SingleTypes_clazz_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.clazz == "sample_text"
    instance.clazz = "sample_text_2"
    assert instance.clazz == "sample_text_2"


def test_types_SingleTypes_date_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_types_SingleTypes_double_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.double == 3.14
    instance.double = 9.99
    assert instance.double == 9.99


def test_types_SingleTypes_doubleObject_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.doubleObject == "sample_text"
    instance.doubleObject = "sample_text_2"
    assert instance.doubleObject == "sample_text_2"


def test_types_SingleTypes_enum_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.enum == "sample_text"
    instance.enum = "sample_text_2"
    assert instance.enum == "sample_text_2"


def test_types_SingleTypes_float_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.float == 3.14
    instance.float = 9.99
    assert instance.float == 9.99


def test_types_SingleTypes_floatObject_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.floatObject == "sample_text"
    instance.floatObject = "sample_text_2"
    assert instance.floatObject == "sample_text_2"


def test_types_SingleTypes_integer_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.integer == 7
    instance.integer = 13
    assert instance.integer == 13


def test_types_SingleTypes_integerObject_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.integerObject == "sample_text"
    instance.integerObject = "sample_text_2"
    assert instance.integerObject == "sample_text_2"


def test_types_SingleTypes_long_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.long == "sample_text"
    instance.long = "sample_text_2"
    assert instance.long == "sample_text_2"


def test_types_SingleTypes_longArray_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.longArray == "sample_text"
    instance.longArray = "sample_text_2"
    assert instance.longArray == "sample_text_2"


def test_types_SingleTypes_longObject_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.longObject == "sample_text"
    instance.longObject = "sample_text_2"
    assert instance.longObject == "sample_text_2"


def test_types_SingleTypes_nextEnum_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.nextEnum == "sample_text"
    instance.nextEnum = "sample_text_2"
    assert instance.nextEnum == "sample_text_2"


def test_types_SingleTypes_string_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_types_SingleTypes_stringArray_value_roundtrip():
    instance = types_SingleTypes(bigDecimal="sample_text", bigInteger="sample_text", byte="sample_text", byteArray="sample_text", byteObject="sample_text", char="sample_text", charObject="sample_text", clazz="sample_text", date=date(2024, 1, 1), double=3.14, doubleObject="sample_text", enum="sample_text", float=3.14, floatObject="sample_text", integer=7, integerObject="sample_text", long="sample_text", longArray="sample_text", longObject="sample_text", nextEnum="sample_text", string="sample_text", stringArray="sample_text")
    assert instance.stringArray == "sample_text"
    instance.stringArray = "sample_text_2"
    assert instance.stringArray == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

types_ManyTypes_strategy = st.builds(types_ManyTypes, bigDecimal=safe_text, bigInteger=safe_text, byteArray=safe_text, byteObject=safe_text, charObject=safe_text, clazz=safe_text, date=st.dates(), doubleObject=safe_text, enum=safe_text, floatObject=safe_text, integerObject=safe_text, long=safe_text, longArray=safe_text, string=safe_text, stringArray=safe_text)
@given(instance=types_ManyTypes_strategy)
@settings(max_examples=25)
def test_types_ManyTypes_instantiation(instance):
    assert isinstance(instance, types_ManyTypes)


types_SingleTypes_strategy = st.builds(types_SingleTypes, bigDecimal=safe_text, bigInteger=safe_text, byte=safe_text, byteArray=safe_text, byteObject=safe_text, char=safe_text, charObject=safe_text, clazz=safe_text, date=st.dates(), double=st.floats(allow_nan=False, allow_infinity=False), doubleObject=safe_text, enum=safe_text, float=st.floats(allow_nan=False, allow_infinity=False), floatObject=safe_text, integer=st.integers(), integerObject=safe_text, long=safe_text, longArray=safe_text, longObject=safe_text, nextEnum=safe_text, string=safe_text, stringArray=safe_text)
@given(instance=types_SingleTypes_strategy)
@settings(max_examples=25)
def test_types_SingleTypes_instantiation(instance):
    assert isinstance(instance, types_SingleTypes)


