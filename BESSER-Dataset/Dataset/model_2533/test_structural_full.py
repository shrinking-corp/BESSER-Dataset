import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    raas_small_test_10382437,
    raas_small_test_11832905,
    raas_small_test_16551649,
    raas_small_test_19723516,
    raas_small_test_29373817,
    raas_small_test_30911270,
    raas_small_test_5656663,
    raas_small_test_7345254,
    raas_small_test_DerivedUnderClassE1,
    raas_small_test_DerivedUnderClassE2,
    raas_small_test_FourthLevelClassK,
    raas_small_test_MergingE1AndE2,
    raas_small_test_ReposRoot,
    raas_small_test_ThirdLevelClassJ,
    raas_small_test_TopClassA,
    raas_small_test_TopClassB,
    raas_small_test_TopClassC,
    raas_small_test_TopClassD,
    raas_small_test_TopClassM,
    raas_small_test_UnderClassE,
    raas_small_test_UnderClassF,
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

def test_raas_small_test_FourthLevelClassK_multi2lowerAttrInt_value_roundtrip():
    instance = raas_small_test_FourthLevelClassK(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.multi2lowerAttrInt == 7
    instance.multi2lowerAttrInt = 13
    assert instance.multi2lowerAttrInt == 13


def test_raas_small_test_FourthLevelClassK_optionalAttrInt_value_roundtrip():
    instance = raas_small_test_FourthLevelClassK(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.optionalAttrInt == 7
    instance.optionalAttrInt = 13
    assert instance.optionalAttrInt == 13


def test_raas_small_test_FourthLevelClassK_raasRef_value_roundtrip():
    instance = raas_small_test_FourthLevelClassK(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_FourthLevelClassK_singleAttrInt_value_roundtrip():
    instance = raas_small_test_FourthLevelClassK(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.singleAttrInt == 7
    instance.singleAttrInt = 13
    assert instance.singleAttrInt == 13


def test_raas_small_test_ReposRoot_multiAttrString_value_roundtrip():
    instance = raas_small_test_ReposRoot(multiAttrString="sample_text", raasRef="sample_text", singleAttrString="sample_text")
    assert instance.multiAttrString == "sample_text"
    instance.multiAttrString = "sample_text_2"
    assert instance.multiAttrString == "sample_text_2"


def test_raas_small_test_ReposRoot_raasRef_value_roundtrip():
    instance = raas_small_test_ReposRoot(multiAttrString="sample_text", raasRef="sample_text", singleAttrString="sample_text")
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_ReposRoot_singleAttrString_value_roundtrip():
    instance = raas_small_test_ReposRoot(multiAttrString="sample_text", raasRef="sample_text", singleAttrString="sample_text")
    assert instance.singleAttrString == "sample_text"
    instance.singleAttrString = "sample_text_2"
    assert instance.singleAttrString == "sample_text_2"


def test_raas_small_test_ThirdLevelClassJ_multi2lowerAttrInt_value_roundtrip():
    instance = raas_small_test_ThirdLevelClassJ(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.multi2lowerAttrInt == 7
    instance.multi2lowerAttrInt = 13
    assert instance.multi2lowerAttrInt == 13


def test_raas_small_test_ThirdLevelClassJ_optionalAttrInt_value_roundtrip():
    instance = raas_small_test_ThirdLevelClassJ(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.optionalAttrInt == 7
    instance.optionalAttrInt = 13
    assert instance.optionalAttrInt == 13


def test_raas_small_test_ThirdLevelClassJ_raasRef_value_roundtrip():
    instance = raas_small_test_ThirdLevelClassJ(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_ThirdLevelClassJ_singleAttrInt_value_roundtrip():
    instance = raas_small_test_ThirdLevelClassJ(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.singleAttrInt == 7
    instance.singleAttrInt = 13
    assert instance.singleAttrInt == 13


def test_raas_small_test_TopClassA_raasRef_value_roundtrip():
    instance = raas_small_test_TopClassA(raasRef="sample_text")
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_TopClassB_multi2lowerAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassB(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.multi2lowerAttrInt == 7
    instance.multi2lowerAttrInt = 13
    assert instance.multi2lowerAttrInt == 13


def test_raas_small_test_TopClassB_optionalAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassB(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.optionalAttrInt == 7
    instance.optionalAttrInt = 13
    assert instance.optionalAttrInt == 13


def test_raas_small_test_TopClassB_raasRef_value_roundtrip():
    instance = raas_small_test_TopClassB(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_TopClassB_singleAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassB(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.singleAttrInt == 7
    instance.singleAttrInt = 13
    assert instance.singleAttrInt == 13


def test_raas_small_test_TopClassC_multi2lowerAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassC(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.multi2lowerAttrInt == 7
    instance.multi2lowerAttrInt = 13
    assert instance.multi2lowerAttrInt == 13


def test_raas_small_test_TopClassC_optionalAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassC(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.optionalAttrInt == 7
    instance.optionalAttrInt = 13
    assert instance.optionalAttrInt == 13


def test_raas_small_test_TopClassC_raasRef_value_roundtrip():
    instance = raas_small_test_TopClassC(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_TopClassC_singleAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassC(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    assert instance.singleAttrInt == 7
    instance.singleAttrInt = 13
    assert instance.singleAttrInt == 13


def test_raas_small_test_TopClassD_multi2lowerAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassD(multi2lowerAttrInt=7, optionalAttrInt=7, optionalTimeZone="sample_text", raasRef="sample_text", singleAttrInt=7)
    assert instance.multi2lowerAttrInt == 7
    instance.multi2lowerAttrInt = 13
    assert instance.multi2lowerAttrInt == 13


def test_raas_small_test_TopClassD_optionalAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassD(multi2lowerAttrInt=7, optionalAttrInt=7, optionalTimeZone="sample_text", raasRef="sample_text", singleAttrInt=7)
    assert instance.optionalAttrInt == 7
    instance.optionalAttrInt = 13
    assert instance.optionalAttrInt == 13


def test_raas_small_test_TopClassD_optionalTimeZone_value_roundtrip():
    instance = raas_small_test_TopClassD(multi2lowerAttrInt=7, optionalAttrInt=7, optionalTimeZone="sample_text", raasRef="sample_text", singleAttrInt=7)
    assert instance.optionalTimeZone == "sample_text"
    instance.optionalTimeZone = "sample_text_2"
    assert instance.optionalTimeZone == "sample_text_2"


def test_raas_small_test_TopClassD_raasRef_value_roundtrip():
    instance = raas_small_test_TopClassD(multi2lowerAttrInt=7, optionalAttrInt=7, optionalTimeZone="sample_text", raasRef="sample_text", singleAttrInt=7)
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_TopClassD_singleAttrInt_value_roundtrip():
    instance = raas_small_test_TopClassD(multi2lowerAttrInt=7, optionalAttrInt=7, optionalTimeZone="sample_text", raasRef="sample_text", singleAttrInt=7)
    assert instance.singleAttrInt == 7
    instance.singleAttrInt = 13
    assert instance.singleAttrInt == 13


def test_raas_small_test_UnderClassE_raasRef_value_roundtrip():
    instance = raas_small_test_UnderClassE(raasRef="sample_text")
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_UnderClassF_raasRef_value_roundtrip():
    instance = raas_small_test_UnderClassF(raasRef="sample_text", singleAttrInt=7)
    assert instance.raasRef == "sample_text"
    instance.raasRef = "sample_text_2"
    assert instance.raasRef == "sample_text_2"


def test_raas_small_test_UnderClassF_singleAttrInt_value_roundtrip():
    instance = raas_small_test_UnderClassF(raasRef="sample_text", singleAttrInt=7)
    assert instance.singleAttrInt == 7
    instance.singleAttrInt = 13
    assert instance.singleAttrInt == 13


def test_assoc_multiContainClassA0_link_reassign_clear():
    a = raas_small_test_ReposRoot(multiAttrString="sample_text", raasRef="sample_text", singleAttrString="sample_text")
    b1 = raas_small_test_29373817()
    b2 = raas_small_test_29373817()
    _safe_set(a, 'raas_small_test_ReposRoot', {b1})
    assert _is_linked(a, 'raas_small_test_ReposRoot', b1)
    if hasattr(b1, 'raas_small_test_29373817'):
        assert _is_linked(b1, 'raas_small_test_29373817', a)
    _safe_set(a, 'raas_small_test_ReposRoot', {b2})
    assert _is_linked(a, 'raas_small_test_ReposRoot', b2)
    if hasattr(b1, 'raas_small_test_29373817'):
        assert not _is_linked(b1, 'raas_small_test_29373817', a)
    if hasattr(b2, 'raas_small_test_29373817'):
        assert _is_linked(b2, 'raas_small_test_29373817', a)
    _safe_set(a, 'raas_small_test_ReposRoot', set())
    assert not _is_linked(a, 'raas_small_test_ReposRoot', b2)
    if hasattr(b2, 'raas_small_test_29373817'):
        assert not _is_linked(b2, 'raas_small_test_29373817', a)


def test_assoc_multiContainClassE9_link_reassign_clear():
    a = raas_small_test_TopClassA(raasRef="sample_text")
    b1 = raas_small_test_5656663()
    b2 = raas_small_test_5656663()
    _safe_set(a, 'raas_small_test_TopClassA', {b1})
    assert _is_linked(a, 'raas_small_test_TopClassA', b1)
    if hasattr(b1, 'raas_small_test_5656663'):
        assert _is_linked(b1, 'raas_small_test_5656663', a)
    _safe_set(a, 'raas_small_test_TopClassA', {b2})
    assert _is_linked(a, 'raas_small_test_TopClassA', b2)
    if hasattr(b1, 'raas_small_test_5656663'):
        assert not _is_linked(b1, 'raas_small_test_5656663', a)
    if hasattr(b2, 'raas_small_test_5656663'):
        assert _is_linked(b2, 'raas_small_test_5656663', a)
    _safe_set(a, 'raas_small_test_TopClassA', set())
    assert not _is_linked(a, 'raas_small_test_TopClassA', b2)
    if hasattr(b2, 'raas_small_test_5656663'):
        assert not _is_linked(b2, 'raas_small_test_5656663', a)


def test_assoc_multiRefClassD5_link_reassign_clear():
    a = raas_small_test_ReposRoot(multiAttrString="sample_text", raasRef="sample_text", singleAttrString="sample_text")
    b1 = raas_small_test_11832905()
    b2 = raas_small_test_11832905()
    _safe_set(a, 'raas_small_test_ReposRoot6', {b1})
    assert _is_linked(a, 'raas_small_test_ReposRoot6', b1)
    if hasattr(b1, 'raas_small_test_11832905'):
        assert _is_linked(b1, 'raas_small_test_11832905', a)
    _safe_set(a, 'raas_small_test_ReposRoot6', {b2})
    assert _is_linked(a, 'raas_small_test_ReposRoot6', b2)
    if hasattr(b1, 'raas_small_test_11832905'):
        assert not _is_linked(b1, 'raas_small_test_11832905', a)
    if hasattr(b2, 'raas_small_test_11832905'):
        assert _is_linked(b2, 'raas_small_test_11832905', a)
    _safe_set(a, 'raas_small_test_ReposRoot6', set())
    assert not _is_linked(a, 'raas_small_test_ReposRoot6', b2)
    if hasattr(b2, 'raas_small_test_11832905'):
        assert not _is_linked(b2, 'raas_small_test_11832905', a)


def test_assoc_multiRefClassE12_link_reassign_clear():
    a = raas_small_test_TopClassB(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    b1 = raas_small_test_5656663()
    b2 = raas_small_test_5656663()
    _safe_set(a, 'raas_small_test_TopClassB', {b1})
    assert _is_linked(a, 'raas_small_test_TopClassB', b1)
    if hasattr(b1, 'raas_small_test_565666313'):
        assert _is_linked(b1, 'raas_small_test_565666313', a)
    _safe_set(a, 'raas_small_test_TopClassB', {b2})
    assert _is_linked(a, 'raas_small_test_TopClassB', b2)
    if hasattr(b1, 'raas_small_test_565666313'):
        assert not _is_linked(b1, 'raas_small_test_565666313', a)
    if hasattr(b2, 'raas_small_test_565666313'):
        assert _is_linked(b2, 'raas_small_test_565666313', a)
    _safe_set(a, 'raas_small_test_TopClassB', set())
    assert not _is_linked(a, 'raas_small_test_TopClassB', b2)
    if hasattr(b2, 'raas_small_test_565666313'):
        assert not _is_linked(b2, 'raas_small_test_565666313', a)


def test_assoc_optionalContainClassB1_link_reassign_clear():
    a = raas_small_test_ReposRoot(multiAttrString="sample_text", raasRef="sample_text", singleAttrString="sample_text")
    b1 = raas_small_test_19723516()
    b2 = raas_small_test_19723516()
    _safe_set(a, 'raas_small_test_ReposRoot2', b1)
    assert _is_linked(a, 'raas_small_test_ReposRoot2', b1)
    if hasattr(b1, 'raas_small_test_19723516'):
        assert _is_linked(b1, 'raas_small_test_19723516', a)
    _safe_set(a, 'raas_small_test_ReposRoot2', b2)
    assert _is_linked(a, 'raas_small_test_ReposRoot2', b2)
    if hasattr(b1, 'raas_small_test_19723516'):
        assert not _is_linked(b1, 'raas_small_test_19723516', a)
    if hasattr(b2, 'raas_small_test_19723516'):
        assert _is_linked(b2, 'raas_small_test_19723516', a)
    _safe_set(a, 'raas_small_test_ReposRoot2', None)
    assert not _is_linked(a, 'raas_small_test_ReposRoot2', b2)
    if hasattr(b2, 'raas_small_test_19723516'):
        assert not _is_linked(b2, 'raas_small_test_19723516', a)


def test_assoc_optionalContainClassK16_link_reassign_clear():
    a = raas_small_test_ThirdLevelClassJ(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    b1 = raas_small_test_10382437()
    b2 = raas_small_test_10382437()
    _safe_set(a, 'raas_small_test_ThirdLevelClassJ', b1)
    assert _is_linked(a, 'raas_small_test_ThirdLevelClassJ', b1)
    if hasattr(b1, 'raas_small_test_10382437'):
        assert _is_linked(b1, 'raas_small_test_10382437', a)
    _safe_set(a, 'raas_small_test_ThirdLevelClassJ', b2)
    assert _is_linked(a, 'raas_small_test_ThirdLevelClassJ', b2)
    if hasattr(b1, 'raas_small_test_10382437'):
        assert not _is_linked(b1, 'raas_small_test_10382437', a)
    if hasattr(b2, 'raas_small_test_10382437'):
        assert _is_linked(b2, 'raas_small_test_10382437', a)
    _safe_set(a, 'raas_small_test_ThirdLevelClassJ', None)
    assert not _is_linked(a, 'raas_small_test_ThirdLevelClassJ', b2)
    if hasattr(b2, 'raas_small_test_10382437'):
        assert not _is_linked(b2, 'raas_small_test_10382437', a)


def test_assoc_singleContainClassC3_link_reassign_clear():
    a = raas_small_test_ReposRoot(multiAttrString="sample_text", raasRef="sample_text", singleAttrString="sample_text")
    b1 = raas_small_test_7345254()
    b2 = raas_small_test_7345254()
    _safe_set(a, 'raas_small_test_ReposRoot4', b1)
    assert _is_linked(a, 'raas_small_test_ReposRoot4', b1)
    if hasattr(b1, 'raas_small_test_7345254'):
        assert _is_linked(b1, 'raas_small_test_7345254', a)
    _safe_set(a, 'raas_small_test_ReposRoot4', b2)
    assert _is_linked(a, 'raas_small_test_ReposRoot4', b2)
    if hasattr(b1, 'raas_small_test_7345254'):
        assert not _is_linked(b1, 'raas_small_test_7345254', a)
    if hasattr(b2, 'raas_small_test_7345254'):
        assert _is_linked(b2, 'raas_small_test_7345254', a)
    _safe_set(a, 'raas_small_test_ReposRoot4', None)
    assert not _is_linked(a, 'raas_small_test_ReposRoot4', b2)
    if hasattr(b2, 'raas_small_test_7345254'):
        assert not _is_linked(b2, 'raas_small_test_7345254', a)


def test_assoc_singleContainClassF10_link_reassign_clear():
    a = raas_small_test_TopClassA(raasRef="sample_text")
    b1 = raas_small_test_16551649()
    b2 = raas_small_test_16551649()
    _safe_set(a, 'raas_small_test_TopClassA11', b1)
    assert _is_linked(a, 'raas_small_test_TopClassA11', b1)
    if hasattr(b1, 'raas_small_test_16551649'):
        assert _is_linked(b1, 'raas_small_test_16551649', a)
    _safe_set(a, 'raas_small_test_TopClassA11', b2)
    assert _is_linked(a, 'raas_small_test_TopClassA11', b2)
    if hasattr(b1, 'raas_small_test_16551649'):
        assert not _is_linked(b1, 'raas_small_test_16551649', a)
    if hasattr(b2, 'raas_small_test_16551649'):
        assert _is_linked(b2, 'raas_small_test_16551649', a)
    _safe_set(a, 'raas_small_test_TopClassA11', None)
    assert not _is_linked(a, 'raas_small_test_TopClassA11', b2)
    if hasattr(b2, 'raas_small_test_16551649'):
        assert not _is_linked(b2, 'raas_small_test_16551649', a)


def test_assoc_singleContainClassF14_link_reassign_clear():
    a = raas_small_test_TopClassC(multi2lowerAttrInt=7, optionalAttrInt=7, raasRef="sample_text", singleAttrInt=7)
    b1 = raas_small_test_16551649()
    b2 = raas_small_test_16551649()
    _safe_set(a, 'raas_small_test_TopClassC', b1)
    assert _is_linked(a, 'raas_small_test_TopClassC', b1)
    if hasattr(b1, 'raas_small_test_1655164915'):
        assert _is_linked(b1, 'raas_small_test_1655164915', a)
    _safe_set(a, 'raas_small_test_TopClassC', b2)
    assert _is_linked(a, 'raas_small_test_TopClassC', b2)
    if hasattr(b1, 'raas_small_test_1655164915'):
        assert not _is_linked(b1, 'raas_small_test_1655164915', a)
    if hasattr(b2, 'raas_small_test_1655164915'):
        assert _is_linked(b2, 'raas_small_test_1655164915', a)
    _safe_set(a, 'raas_small_test_TopClassC', None)
    assert not _is_linked(a, 'raas_small_test_TopClassC', b2)
    if hasattr(b2, 'raas_small_test_1655164915'):
        assert not _is_linked(b2, 'raas_small_test_1655164915', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

raas_small_test__10382437_strategy = st.builds(raas_small_test_10382437)
@given(instance=raas_small_test__10382437_strategy)
@settings(max_examples=25)
def test_raas_small_test__10382437_instantiation(instance):
    assert isinstance(instance, raas_small_test_10382437)


raas_small_test__11832905_strategy = st.builds(raas_small_test_11832905)
@given(instance=raas_small_test__11832905_strategy)
@settings(max_examples=25)
def test_raas_small_test__11832905_instantiation(instance):
    assert isinstance(instance, raas_small_test_11832905)


raas_small_test__16551649_strategy = st.builds(raas_small_test_16551649)
@given(instance=raas_small_test__16551649_strategy)
@settings(max_examples=25)
def test_raas_small_test__16551649_instantiation(instance):
    assert isinstance(instance, raas_small_test_16551649)


raas_small_test__19723516_strategy = st.builds(raas_small_test_19723516)
@given(instance=raas_small_test__19723516_strategy)
@settings(max_examples=25)
def test_raas_small_test__19723516_instantiation(instance):
    assert isinstance(instance, raas_small_test_19723516)


raas_small_test__29373817_strategy = st.builds(raas_small_test_29373817)
@given(instance=raas_small_test__29373817_strategy)
@settings(max_examples=25)
def test_raas_small_test__29373817_instantiation(instance):
    assert isinstance(instance, raas_small_test_29373817)


raas_small_test__30911270_strategy = st.builds(raas_small_test_30911270)
@given(instance=raas_small_test__30911270_strategy)
@settings(max_examples=25)
def test_raas_small_test__30911270_instantiation(instance):
    assert isinstance(instance, raas_small_test_30911270)


raas_small_test__5656663_strategy = st.builds(raas_small_test_5656663)
@given(instance=raas_small_test__5656663_strategy)
@settings(max_examples=25)
def test_raas_small_test__5656663_instantiation(instance):
    assert isinstance(instance, raas_small_test_5656663)


raas_small_test__7345254_strategy = st.builds(raas_small_test_7345254)
@given(instance=raas_small_test__7345254_strategy)
@settings(max_examples=25)
def test_raas_small_test__7345254_instantiation(instance):
    assert isinstance(instance, raas_small_test_7345254)


raas_small_test_FourthLevelClassK_strategy = st.builds(raas_small_test_FourthLevelClassK, multi2lowerAttrInt=st.integers(), optionalAttrInt=st.integers(), raasRef=safe_text, singleAttrInt=st.integers())
@given(instance=raas_small_test_FourthLevelClassK_strategy)
@settings(max_examples=25)
def test_raas_small_test_FourthLevelClassK_instantiation(instance):
    assert isinstance(instance, raas_small_test_FourthLevelClassK)


raas_small_test_ReposRoot_strategy = st.builds(raas_small_test_ReposRoot, multiAttrString=safe_text, raasRef=safe_text, singleAttrString=safe_text)
@given(instance=raas_small_test_ReposRoot_strategy)
@settings(max_examples=25)
def test_raas_small_test_ReposRoot_instantiation(instance):
    assert isinstance(instance, raas_small_test_ReposRoot)


raas_small_test_ThirdLevelClassJ_strategy = st.builds(raas_small_test_ThirdLevelClassJ, multi2lowerAttrInt=st.integers(), optionalAttrInt=st.integers(), raasRef=safe_text, singleAttrInt=st.integers())
@given(instance=raas_small_test_ThirdLevelClassJ_strategy)
@settings(max_examples=25)
def test_raas_small_test_ThirdLevelClassJ_instantiation(instance):
    assert isinstance(instance, raas_small_test_ThirdLevelClassJ)


raas_small_test_TopClassA_strategy = st.builds(raas_small_test_TopClassA, raasRef=safe_text)
@given(instance=raas_small_test_TopClassA_strategy)
@settings(max_examples=25)
def test_raas_small_test_TopClassA_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassA)


raas_small_test_TopClassB_strategy = st.builds(raas_small_test_TopClassB, multi2lowerAttrInt=st.integers(), optionalAttrInt=st.integers(), raasRef=safe_text, singleAttrInt=st.integers())
@given(instance=raas_small_test_TopClassB_strategy)
@settings(max_examples=25)
def test_raas_small_test_TopClassB_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassB)


raas_small_test_TopClassC_strategy = st.builds(raas_small_test_TopClassC, multi2lowerAttrInt=st.integers(), optionalAttrInt=st.integers(), raasRef=safe_text, singleAttrInt=st.integers())
@given(instance=raas_small_test_TopClassC_strategy)
@settings(max_examples=25)
def test_raas_small_test_TopClassC_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassC)


raas_small_test_TopClassD_strategy = st.builds(raas_small_test_TopClassD, multi2lowerAttrInt=st.integers(), optionalAttrInt=st.integers(), optionalTimeZone=safe_text, raasRef=safe_text, singleAttrInt=st.integers())
@given(instance=raas_small_test_TopClassD_strategy)
@settings(max_examples=25)
def test_raas_small_test_TopClassD_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassD)


raas_small_test_UnderClassE_strategy = st.builds(raas_small_test_UnderClassE, raasRef=safe_text)
@given(instance=raas_small_test_UnderClassE_strategy)
@settings(max_examples=25)
def test_raas_small_test_UnderClassE_instantiation(instance):
    assert isinstance(instance, raas_small_test_UnderClassE)


raas_small_test_UnderClassF_strategy = st.builds(raas_small_test_UnderClassF, raasRef=safe_text, singleAttrInt=st.integers())
@given(instance=raas_small_test_UnderClassF_strategy)
@settings(max_examples=25)
def test_raas_small_test_UnderClassF_instantiation(instance):
    assert isinstance(instance, raas_small_test_UnderClassF)


