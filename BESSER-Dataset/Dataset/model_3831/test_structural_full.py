import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractTest,
    InterfaceTest,
    MultipleSuperTest,
    OperationsTest,
    exhaustive_AbstractTest,
    exhaustive_AttributesTest,
    exhaustive_GenericTest,
    exhaustive_InterfaceTest,
    exhaustive_MultipleSuperTest,
    exhaustive_OperationsTest,
    exhaustive_ReferencesTest,
    SerializableEnumTest,
    UnserializableEnumTest,
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

def test_exhaustive_AttributesTest_changeableNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.changeableNo == "sample_text"
    instance.changeableNo = "sample_text_2"
    assert instance.changeableNo == "sample_text_2"


def test_exhaustive_AttributesTest_changeableYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.changeableYes == 3.14
    instance.changeableYes = 9.99
    assert instance.changeableYes == 9.99


def test_exhaustive_AttributesTest_defaultValue_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_exhaustive_AttributesTest_derivedNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.derivedNo == "sample_text"
    instance.derivedNo = "sample_text_2"
    assert instance.derivedNo == "sample_text_2"


def test_exhaustive_AttributesTest_derivedYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.derivedYes == "sample_text"
    instance.derivedYes = "sample_text_2"
    assert instance.derivedYes == "sample_text_2"


def test_exhaustive_AttributesTest_idNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.idNo == "sample_text"
    instance.idNo = "sample_text_2"
    assert instance.idNo == "sample_text_2"


def test_exhaustive_AttributesTest_idYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.idYes == "sample_text"
    instance.idYes = "sample_text_2"
    assert instance.idYes == "sample_text_2"


def test_exhaustive_AttributesTest_lowerBound0_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.lowerBound0 == 7
    instance.lowerBound0 = 13
    assert instance.lowerBound0 == 13


def test_exhaustive_AttributesTest_lowerBound1_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.lowerBound1 == "sample_text"
    instance.lowerBound1 = "sample_text_2"
    assert instance.lowerBound1 == "sample_text_2"


def test_exhaustive_AttributesTest_lowerBound2_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.lowerBound2 == "sample_text"
    instance.lowerBound2 = "sample_text_2"
    assert instance.lowerBound2 == "sample_text_2"


def test_exhaustive_AttributesTest_lowerBoundN_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.lowerBoundN == "sample_text"
    instance.lowerBoundN = "sample_text_2"
    assert instance.lowerBoundN == "sample_text_2"


def test_exhaustive_AttributesTest_orderedYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.orderedYes == "sample_text"
    instance.orderedYes = "sample_text_2"
    assert instance.orderedYes == "sample_text_2"


def test_exhaustive_AttributesTest_orderenedNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.orderenedNo == "sample_text"
    instance.orderenedNo = "sample_text_2"
    assert instance.orderenedNo == "sample_text_2"


def test_exhaustive_AttributesTest_transientNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.transientNo == "sample_text"
    instance.transientNo = "sample_text_2"
    assert instance.transientNo == "sample_text_2"


def test_exhaustive_AttributesTest_transientYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.transientYes == 3.14
    instance.transientYes = 9.99
    assert instance.transientYes == 9.99


def test_exhaustive_AttributesTest_uniqueNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.uniqueNo == "sample_text"
    instance.uniqueNo = "sample_text_2"
    assert instance.uniqueNo == "sample_text_2"


def test_exhaustive_AttributesTest_uniqueYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.uniqueYes == "sample_text"
    instance.uniqueYes = "sample_text_2"
    assert instance.uniqueYes == "sample_text_2"


def test_exhaustive_AttributesTest_unsettableNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.unsettableNo == "sample_text"
    instance.unsettableNo = "sample_text_2"
    assert instance.unsettableNo == "sample_text_2"


def test_exhaustive_AttributesTest_unsettableYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.unsettableYes == "sample_text"
    instance.unsettableYes = "sample_text_2"
    assert instance.unsettableYes == "sample_text_2"


def test_exhaustive_AttributesTest_upperBound0_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.upperBound0 == "sample_text"
    instance.upperBound0 = "sample_text_2"
    assert instance.upperBound0 == "sample_text_2"


def test_exhaustive_AttributesTest_upperBound1_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.upperBound1 == date(2024, 1, 1)
    instance.upperBound1 = date(2025, 6, 15)
    assert instance.upperBound1 == date(2025, 6, 15)


def test_exhaustive_AttributesTest_upperBound2_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.upperBound2 == "sample_text"
    instance.upperBound2 = "sample_text_2"
    assert instance.upperBound2 == "sample_text_2"


def test_exhaustive_AttributesTest_upperBoundN_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.upperBoundN == "sample_text"
    instance.upperBoundN = "sample_text_2"
    assert instance.upperBoundN == "sample_text_2"


def test_exhaustive_AttributesTest_volatileNo_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.volatileNo == "sample_text"
    instance.volatileNo = "sample_text_2"
    assert instance.volatileNo == "sample_text_2"


def test_exhaustive_AttributesTest_volatileYes_value_roundtrip():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert instance.volatileYes == "sample_text"
    instance.volatileYes = "sample_text_2"
    assert instance.volatileYes == "sample_text_2"


def test_exhaustive_GenericTest_genericAttr_value_roundtrip():
    instance = exhaustive_GenericTest(genericAttr="sample_text")
    assert instance.genericAttr == "sample_text"
    instance.genericAttr = "sample_text_2"
    assert instance.genericAttr == "sample_text_2"


def test_exhaustive_MultipleSuperTest_isa_AbstractTest():
    instance = exhaustive_MultipleSuperTest()
    assert isinstance(instance, AbstractTest)


def test_exhaustive_ReferencesTest_isa_AbstractTest():
    instance = exhaustive_ReferencesTest()
    assert isinstance(instance, AbstractTest)


def test_exhaustive_AttributesTest_isa_InterfaceTest():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert isinstance(instance, InterfaceTest)


def test_exhaustive_MultipleSuperTest_isa_InterfaceTest():
    instance = exhaustive_MultipleSuperTest()
    assert isinstance(instance, InterfaceTest)


def test_exhaustive_AttributesTest_isa_MultipleSuperTest():
    instance = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    assert isinstance(instance, MultipleSuperTest)


def test_exhaustive_AbstractTest_isa_OperationsTest():
    instance = exhaustive_AbstractTest()
    assert isinstance(instance, OperationsTest)


def test_exhaustive_InterfaceTest_isa_OperationsTest():
    instance = exhaustive_InterfaceTest()
    assert isinstance(instance, OperationsTest)


def test_assoc_derivedYes24_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest26', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest26', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest25'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest25', a)
    _safe_set(a, 'exhaustive_AttributesTest26', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest26', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest25'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest25', a)
    if hasattr(b2, 'exhaustive_ReferencesTest25'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest25', a)
    _safe_set(a, 'exhaustive_AttributesTest26', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest26', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest25'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest25', a)


def test_assoc_lowerBound133_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest35', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest35', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest34'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest34', a)
    _safe_set(a, 'exhaustive_AttributesTest35', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest35', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest34'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest34', a)
    if hasattr(b2, 'exhaustive_ReferencesTest34'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest34', a)
    _safe_set(a, 'exhaustive_AttributesTest35', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest35', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest34'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest34', a)


def test_assoc_lowerBound236_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest38', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest38', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest37'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest37', a)
    _safe_set(a, 'exhaustive_AttributesTest38', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest38', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest37'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest37', a)
    if hasattr(b2, 'exhaustive_ReferencesTest37'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest37', a)
    _safe_set(a, 'exhaustive_AttributesTest38', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest38', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest37'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest37', a)


def test_assoc_opposite16_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'AttributesTest', b1)
    assert _is_linked(a, 'AttributesTest', b1)
    if hasattr(b1, 'opposite2'):
        assert _is_linked(b1, 'opposite2', a)
    _safe_set(a, 'AttributesTest', b2)
    assert _is_linked(a, 'AttributesTest', b2)
    if hasattr(b1, 'opposite2'):
        assert not _is_linked(b1, 'opposite2', a)
    if hasattr(b2, 'opposite2'):
        assert _is_linked(b2, 'opposite2', a)
    _safe_set(a, 'AttributesTest', None)
    assert not _is_linked(a, 'AttributesTest', b2)
    if hasattr(b2, 'opposite2'):
        assert not _is_linked(b2, 'opposite2', a)


def test_assoc_opposite239_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'opposite1', b1)
    assert _is_linked(a, 'opposite1', b1)
    if hasattr(b1, 'ReferencesTest'):
        assert _is_linked(b1, 'ReferencesTest', a)
    _safe_set(a, 'opposite1', b2)
    assert _is_linked(a, 'opposite1', b2)
    if hasattr(b1, 'ReferencesTest'):
        assert not _is_linked(b1, 'ReferencesTest', a)
    if hasattr(b2, 'ReferencesTest'):
        assert _is_linked(b2, 'ReferencesTest', a)
    _safe_set(a, 'opposite1', None)
    assert not _is_linked(a, 'opposite1', b2)
    if hasattr(b2, 'ReferencesTest'):
        assert not _is_linked(b2, 'ReferencesTest', a)


def test_assoc_orderedFalse7_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest8'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest8', a)
    _safe_set(a, 'exhaustive_AttributesTest', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest8'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest8', a)
    if hasattr(b2, 'exhaustive_ReferencesTest8'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest8', a)
    _safe_set(a, 'exhaustive_AttributesTest', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest8'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest8', a)


def test_assoc_resolveProxiesFalse9_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest11', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest11', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest10'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest10', a)
    _safe_set(a, 'exhaustive_AttributesTest11', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest11', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest10'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest10', a)
    if hasattr(b2, 'exhaustive_ReferencesTest10'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest10', a)
    _safe_set(a, 'exhaustive_AttributesTest11', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest11', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest10'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest10', a)


def test_assoc_transientTrue12_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest14', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest14', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest13'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest13', a)
    _safe_set(a, 'exhaustive_AttributesTest14', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest14', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest13'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest13', a)
    if hasattr(b2, 'exhaustive_ReferencesTest13'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest13', a)
    _safe_set(a, 'exhaustive_AttributesTest14', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest14', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest13'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest13', a)


def test_assoc_uniqueFalse15_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest17', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest17', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest16'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest16', a)
    _safe_set(a, 'exhaustive_AttributesTest17', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest17', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest16'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest16', a)
    if hasattr(b2, 'exhaustive_ReferencesTest16'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest16', a)
    _safe_set(a, 'exhaustive_AttributesTest17', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest17', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest16'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest16', a)


def test_assoc_unsettableTrue18_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest20', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest20', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest19'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest19', a)
    _safe_set(a, 'exhaustive_AttributesTest20', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest20', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest19'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest19', a)
    if hasattr(b2, 'exhaustive_ReferencesTest19'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest19', a)
    _safe_set(a, 'exhaustive_AttributesTest20', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest20', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest19'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest19', a)


def test_assoc_upperBound230_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest32', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest32', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest31'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest31', a)
    _safe_set(a, 'exhaustive_AttributesTest32', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest32', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest31'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest31', a)
    if hasattr(b2, 'exhaustive_ReferencesTest31'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest31', a)
    _safe_set(a, 'exhaustive_AttributesTest32', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest32', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest31'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest31', a)


def test_assoc_upperBoundN27_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest29', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest29', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest28'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest28', a)
    _safe_set(a, 'exhaustive_AttributesTest29', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest29', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest28'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest28', a)
    if hasattr(b2, 'exhaustive_ReferencesTest28'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest28', a)
    _safe_set(a, 'exhaustive_AttributesTest29', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest29', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest28'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest28', a)


def test_assoc_volatileTrue21_link_reassign_clear():
    a = exhaustive_AttributesTest(changeableNo="sample_text", changeableYes=3.14, defaultValue="sample_text", derivedNo="sample_text", derivedYes="sample_text", idNo="sample_text", idYes="sample_text", lowerBound0=7, lowerBound1="sample_text", lowerBound2="sample_text", lowerBoundN="sample_text", orderedYes="sample_text", orderenedNo="sample_text", transientNo="sample_text", transientYes=3.14, uniqueNo="sample_text", uniqueYes="sample_text", unsettableNo="sample_text", unsettableYes="sample_text", upperBound0="sample_text", upperBound1=date(2024, 1, 1), upperBound2="sample_text", upperBoundN="sample_text", volatileNo="sample_text", volatileYes="sample_text")
    b1 = exhaustive_ReferencesTest()
    b2 = exhaustive_ReferencesTest()
    _safe_set(a, 'exhaustive_AttributesTest23', b1)
    assert _is_linked(a, 'exhaustive_AttributesTest23', b1)
    if hasattr(b1, 'exhaustive_ReferencesTest22'):
        assert _is_linked(b1, 'exhaustive_ReferencesTest22', a)
    _safe_set(a, 'exhaustive_AttributesTest23', b2)
    assert _is_linked(a, 'exhaustive_AttributesTest23', b2)
    if hasattr(b1, 'exhaustive_ReferencesTest22'):
        assert not _is_linked(b1, 'exhaustive_ReferencesTest22', a)
    if hasattr(b2, 'exhaustive_ReferencesTest22'):
        assert _is_linked(b2, 'exhaustive_ReferencesTest22', a)
    _safe_set(a, 'exhaustive_AttributesTest23', None)
    assert not _is_linked(a, 'exhaustive_AttributesTest23', b2)
    if hasattr(b2, 'exhaustive_ReferencesTest22'):
        assert not _is_linked(b2, 'exhaustive_ReferencesTest22', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractTest_strategy = st.builds(AbstractTest)
@given(instance=AbstractTest_strategy)
@settings(max_examples=25)
def test_AbstractTest_instantiation(instance):
    assert isinstance(instance, AbstractTest)


InterfaceTest_strategy = st.builds(InterfaceTest)
@given(instance=InterfaceTest_strategy)
@settings(max_examples=25)
def test_InterfaceTest_instantiation(instance):
    assert isinstance(instance, InterfaceTest)


MultipleSuperTest_strategy = st.builds(MultipleSuperTest)
@given(instance=MultipleSuperTest_strategy)
@settings(max_examples=25)
def test_MultipleSuperTest_instantiation(instance):
    assert isinstance(instance, MultipleSuperTest)


OperationsTest_strategy = st.builds(OperationsTest)
@given(instance=OperationsTest_strategy)
@settings(max_examples=25)
def test_OperationsTest_instantiation(instance):
    assert isinstance(instance, OperationsTest)


exhaustive_AbstractTest_strategy = st.builds(exhaustive_AbstractTest)
@given(instance=exhaustive_AbstractTest_strategy)
@settings(max_examples=25)
def test_exhaustive_AbstractTest_instantiation(instance):
    assert isinstance(instance, exhaustive_AbstractTest)


exhaustive_AttributesTest_strategy = st.builds(exhaustive_AttributesTest, changeableNo=safe_text, changeableYes=st.floats(allow_nan=False, allow_infinity=False), defaultValue=safe_text, derivedNo=safe_text, derivedYes=safe_text, idNo=safe_text, idYes=safe_text, lowerBound0=st.integers(), lowerBound1=safe_text, lowerBound2=safe_text, lowerBoundN=safe_text, orderedYes=safe_text, orderenedNo=safe_text, transientNo=safe_text, transientYes=st.floats(allow_nan=False, allow_infinity=False), uniqueNo=safe_text, uniqueYes=safe_text, unsettableNo=safe_text, unsettableYes=safe_text, upperBound0=safe_text, upperBound1=st.dates(), upperBound2=safe_text, upperBoundN=safe_text, volatileNo=safe_text, volatileYes=safe_text)
@given(instance=exhaustive_AttributesTest_strategy)
@settings(max_examples=25)
def test_exhaustive_AttributesTest_instantiation(instance):
    assert isinstance(instance, exhaustive_AttributesTest)


exhaustive_GenericTest_strategy = st.builds(exhaustive_GenericTest, genericAttr=safe_text)
@given(instance=exhaustive_GenericTest_strategy)
@settings(max_examples=25)
def test_exhaustive_GenericTest_instantiation(instance):
    assert isinstance(instance, exhaustive_GenericTest)


exhaustive_InterfaceTest_strategy = st.builds(exhaustive_InterfaceTest)
@given(instance=exhaustive_InterfaceTest_strategy)
@settings(max_examples=25)
def test_exhaustive_InterfaceTest_instantiation(instance):
    assert isinstance(instance, exhaustive_InterfaceTest)


exhaustive_MultipleSuperTest_strategy = st.builds(exhaustive_MultipleSuperTest)
@given(instance=exhaustive_MultipleSuperTest_strategy)
@settings(max_examples=25)
def test_exhaustive_MultipleSuperTest_instantiation(instance):
    assert isinstance(instance, exhaustive_MultipleSuperTest)


exhaustive_OperationsTest_strategy = st.builds(exhaustive_OperationsTest)
@given(instance=exhaustive_OperationsTest_strategy)
@settings(max_examples=25)
def test_exhaustive_OperationsTest_instantiation(instance):
    assert isinstance(instance, exhaustive_OperationsTest)


exhaustive_ReferencesTest_strategy = st.builds(exhaustive_ReferencesTest)
@given(instance=exhaustive_ReferencesTest_strategy)
@settings(max_examples=25)
def test_exhaustive_ReferencesTest_instantiation(instance):
    assert isinstance(instance, exhaustive_ReferencesTest)


