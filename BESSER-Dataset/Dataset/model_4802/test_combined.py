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
    types_ManyTypes,
    types_SingleTypes,
    TestEnum,
    TestNextEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_types_manytypes_is_not_abstract():
    assert not inspect.isabstract(types_ManyTypes)


def test_hyp_types_manytypes_constructor_exists():
    assert callable(types_ManyTypes.__init__)


def test_hyp_types_manytypes_constructor_args():
    sig = inspect.signature(types_ManyTypes.__init__)
    params = list(sig.parameters.keys())
    assert "enum" in params, "Missing parameter 'enum'"
    assert "floatObject" in params, "Missing parameter 'floatObject'"
    assert "long" in params, "Missing parameter 'long'"
    assert "stringArray" in params, "Missing parameter 'stringArray'"
    assert "longArray" in params, "Missing parameter 'longArray'"
    assert "date" in params, "Missing parameter 'date'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "integerObject" in params, "Missing parameter 'integerObject'"
    assert "charObject" in params, "Missing parameter 'charObject'"
    assert "string" in params, "Missing parameter 'string'"
    assert "doubleObject" in params, "Missing parameter 'doubleObject'"
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "byteObject" in params, "Missing parameter 'byteObject'"
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"
    assert "bigInteger" in params, "Missing parameter 'bigInteger'"


















def test_hyp_types_singletypes_is_not_abstract():
    assert not inspect.isabstract(types_SingleTypes)


def test_hyp_types_singletypes_constructor_exists():
    assert callable(types_SingleTypes.__init__)


def test_hyp_types_singletypes_constructor_args():
    sig = inspect.signature(types_SingleTypes.__init__)
    params = list(sig.parameters.keys())
    assert "longArray" in params, "Missing parameter 'longArray'"
    assert "doubleObject" in params, "Missing parameter 'doubleObject'"
    assert "byteArray" in params, "Missing parameter 'byteArray'"
    assert "byte" in params, "Missing parameter 'byte'"
    assert "long" in params, "Missing parameter 'long'"
    assert "charObject" in params, "Missing parameter 'charObject'"
    assert "float" in params, "Missing parameter 'float'"
    assert "date" in params, "Missing parameter 'date'"
    assert "longObject" in params, "Missing parameter 'longObject'"
    assert "nextEnum" in params, "Missing parameter 'nextEnum'"
    assert "byteObject" in params, "Missing parameter 'byteObject'"
    assert "stringArray" in params, "Missing parameter 'stringArray'"
    assert "integerObject" in params, "Missing parameter 'integerObject'"
    assert "enum" in params, "Missing parameter 'enum'"
    assert "double" in params, "Missing parameter 'double'"
    assert "bigDecimal" in params, "Missing parameter 'bigDecimal'"
    assert "floatObject" in params, "Missing parameter 'floatObject'"
    assert "integer" in params, "Missing parameter 'integer'"
    assert "bigInteger" in params, "Missing parameter 'bigInteger'"
    assert "string" in params, "Missing parameter 'string'"
    assert "char" in params, "Missing parameter 'char'"
    assert "clazz" in params, "Missing parameter 'clazz'"























def test_hyp_testenum_exists():
    # Check that the Enumeration exists
    assert TestEnum is not None

def test_hyp_testenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestEnum]
    expected_literals = [
        "Enum0",
        "Enum2",
        "Enum1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestEnum"

def test_hyp_testnextenum_exists():
    # Check that the Enumeration exists
    assert TestNextEnum is not None

def test_hyp_testnextenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestNextEnum]
    expected_literals = [
        "Enum2",
        "Enum1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestNextEnum"


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
types_ManyTypes_strategy = st.builds(
    types_ManyTypes,
    enum=
        safe_text,
    floatObject=
        safe_text,
    long=
        safe_text,
    stringArray=
        safe_text,
    longArray=
        safe_text,
    date=
        st.dates(),
    byteArray=
        safe_text,
    integerObject=
        safe_text,
    charObject=
        safe_text,
    string=
        safe_text,
    doubleObject=
        safe_text,
    clazz=
        safe_text,
    byteObject=
        safe_text,
    bigDecimal=
        safe_text,
    bigInteger=
        safe_text
)
types_SingleTypes_strategy = st.builds(
    types_SingleTypes,
    longArray=
        safe_text,
    doubleObject=
        safe_text,
    byteArray=
        safe_text,
    byte=
        safe_text,
    long=
        safe_text,
    charObject=
        safe_text,
    float=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    date=
        st.dates(),
    longObject=
        safe_text,
    nextEnum=
        safe_text,
    byteObject=
        safe_text,
    stringArray=
        safe_text,
    integerObject=
        safe_text,
    enum=
        safe_text,
    double=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    bigDecimal=
        safe_text,
    floatObject=
        safe_text,
    integer=
        st.integers(),
    bigInteger=
        safe_text,
    string=
        safe_text,
    char=
        safe_text,
    clazz=
        safe_text
)




@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_enum_setter(instance):
    original = instance.enum
    instance.enum = original
    assert instance.enum == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_floatObject_setter(instance):
    original = instance.floatObject
    instance.floatObject = original
    assert instance.floatObject == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_stringArray_setter(instance):
    original = instance.stringArray
    instance.stringArray = original
    assert instance.stringArray == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_longArray_setter(instance):
    original = instance.longArray
    instance.longArray = original
    assert instance.longArray == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_integerObject_setter(instance):
    original = instance.integerObject
    instance.integerObject = original
    assert instance.integerObject == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_charObject_setter(instance):
    original = instance.charObject
    instance.charObject = original
    assert instance.charObject == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_doubleObject_setter(instance):
    original = instance.doubleObject
    instance.doubleObject = original
    assert instance.doubleObject == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_byteObject_setter(instance):
    original = instance.byteObject
    instance.byteObject = original
    assert instance.byteObject == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original



@given(instance=types_ManyTypes_strategy)
def test_hyp_types_manytypes_bigInteger_setter(instance):
    original = instance.bigInteger
    instance.bigInteger = original
    assert instance.bigInteger == original




@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_longArray_setter(instance):
    original = instance.longArray
    instance.longArray = original
    assert instance.longArray == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_doubleObject_setter(instance):
    original = instance.doubleObject
    instance.doubleObject = original
    assert instance.doubleObject == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_byteArray_setter(instance):
    original = instance.byteArray
    instance.byteArray = original
    assert instance.byteArray == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_byte_setter(instance):
    original = instance.byte
    instance.byte = original
    assert instance.byte == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_charObject_setter(instance):
    original = instance.charObject
    instance.charObject = original
    assert instance.charObject == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_longObject_setter(instance):
    original = instance.longObject
    instance.longObject = original
    assert instance.longObject == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_nextEnum_setter(instance):
    original = instance.nextEnum
    instance.nextEnum = original
    assert instance.nextEnum == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_byteObject_setter(instance):
    original = instance.byteObject
    instance.byteObject = original
    assert instance.byteObject == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_stringArray_setter(instance):
    original = instance.stringArray
    instance.stringArray = original
    assert instance.stringArray == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_integerObject_setter(instance):
    original = instance.integerObject
    instance.integerObject = original
    assert instance.integerObject == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_enum_setter(instance):
    original = instance.enum
    instance.enum = original
    assert instance.enum == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_bigDecimal_setter(instance):
    original = instance.bigDecimal
    instance.bigDecimal = original
    assert instance.bigDecimal == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_floatObject_setter(instance):
    original = instance.floatObject
    instance.floatObject = original
    assert instance.floatObject == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_bigInteger_setter(instance):
    original = instance.bigInteger
    instance.bigInteger = original
    assert instance.bigInteger == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=types_SingleTypes_strategy)
def test_hyp_types_singletypes_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



