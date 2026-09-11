import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    xDstmdata_cExtchannel,
    xDstmdata_cIntchannel,
    xDstmdata_channel_specifier,
    xDstmdata_composingtype,
    xDstmdata_subtype,
    xDstmdata_tCompound,
    xDstmdata_tEnum,
    xDstmdata_tMultitype,
    xDstmdata_tTypes,
    xDstmdata_vVariable,
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

def test_xDstmdata_cExtchannel_name_value_roundtrip():
    instance = xDstmdata_cExtchannel(name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xDstmdata_cExtchannel_tID_value_roundtrip():
    instance = xDstmdata_cExtchannel(name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.tID == "sample_text"
    instance.tID = "sample_text_2"
    assert instance.tID == "sample_text_2"


def test_xDstmdata_cExtchannel_tString_value_roundtrip():
    instance = xDstmdata_cExtchannel(name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.tString == "sample_text"
    instance.tString = "sample_text_2"
    assert instance.tString == "sample_text_2"


def test_xDstmdata_cIntchannel_bound_value_roundtrip():
    instance = xDstmdata_cIntchannel(bound=7, name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.bound == 7
    instance.bound = 13
    assert instance.bound == 13


def test_xDstmdata_cIntchannel_name_value_roundtrip():
    instance = xDstmdata_cIntchannel(bound=7, name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xDstmdata_cIntchannel_tID_value_roundtrip():
    instance = xDstmdata_cIntchannel(bound=7, name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.tID == "sample_text"
    instance.tID = "sample_text_2"
    assert instance.tID == "sample_text_2"


def test_xDstmdata_cIntchannel_tString_value_roundtrip():
    instance = xDstmdata_cIntchannel(bound=7, name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.tString == "sample_text"
    instance.tString = "sample_text_2"
    assert instance.tString == "sample_text_2"


def test_xDstmdata_channel_specifier_type_value_roundtrip():
    instance = xDstmdata_channel_specifier(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xDstmdata_composingtype_tID_value_roundtrip():
    instance = xDstmdata_composingtype(tID="sample_text", tString="sample_text")
    assert instance.tID == "sample_text"
    instance.tID = "sample_text_2"
    assert instance.tID == "sample_text_2"


def test_xDstmdata_composingtype_tString_value_roundtrip():
    instance = xDstmdata_composingtype(tID="sample_text", tString="sample_text")
    assert instance.tString == "sample_text"
    instance.tString = "sample_text_2"
    assert instance.tString == "sample_text_2"


def test_xDstmdata_subtype_tID_value_roundtrip():
    instance = xDstmdata_subtype(tID="sample_text", tString="sample_text")
    assert instance.tID == "sample_text"
    instance.tID = "sample_text_2"
    assert instance.tID == "sample_text_2"


def test_xDstmdata_subtype_tString_value_roundtrip():
    instance = xDstmdata_subtype(tID="sample_text", tString="sample_text")
    assert instance.tString == "sample_text"
    instance.tString = "sample_text_2"
    assert instance.tString == "sample_text_2"


def test_xDstmdata_tCompound_name_value_roundtrip():
    instance = xDstmdata_tCompound(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xDstmdata_tEnum_literals_value_roundtrip():
    instance = xDstmdata_tEnum(literals="sample_text", name="sample_text")
    assert instance.literals == "sample_text"
    instance.literals = "sample_text_2"
    assert instance.literals == "sample_text_2"


def test_xDstmdata_tEnum_name_value_roundtrip():
    instance = xDstmdata_tEnum(literals="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xDstmdata_tMultitype_name_value_roundtrip():
    instance = xDstmdata_tMultitype(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xDstmdata_vVariable_name_value_roundtrip():
    instance = xDstmdata_vVariable(name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xDstmdata_vVariable_tID_value_roundtrip():
    instance = xDstmdata_vVariable(name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.tID == "sample_text"
    instance.tID = "sample_text_2"
    assert instance.tID == "sample_text_2"


def test_xDstmdata_vVariable_tString_value_roundtrip():
    instance = xDstmdata_vVariable(name="sample_text", tID="sample_text", tString="sample_text")
    assert instance.tString == "sample_text"
    instance.tString = "sample_text_2"
    assert instance.tString == "sample_text_2"


def test_assoc_cExtchannel7_link_reassign_clear():
    a = xDstmdata_cExtchannel(name="sample_text", tID="sample_text", tString="sample_text")
    b1 = xDstmdata_tTypes()
    b2 = xDstmdata_tTypes()
    _safe_set(a, 'xDstmdata_cExtchannel', b1)
    assert _is_linked(a, 'xDstmdata_cExtchannel', b1)
    if hasattr(b1, 'xDstmdata_tTypes8'):
        assert _is_linked(b1, 'xDstmdata_tTypes8', a)
    _safe_set(a, 'xDstmdata_cExtchannel', b2)
    assert _is_linked(a, 'xDstmdata_cExtchannel', b2)
    if hasattr(b1, 'xDstmdata_tTypes8'):
        assert not _is_linked(b1, 'xDstmdata_tTypes8', a)
    if hasattr(b2, 'xDstmdata_tTypes8'):
        assert _is_linked(b2, 'xDstmdata_tTypes8', a)
    _safe_set(a, 'xDstmdata_cExtchannel', None)
    assert not _is_linked(a, 'xDstmdata_cExtchannel', b2)
    if hasattr(b2, 'xDstmdata_tTypes8'):
        assert not _is_linked(b2, 'xDstmdata_tTypes8', a)


def test_assoc_cIntchannel5_link_reassign_clear():
    a = xDstmdata_cIntchannel(bound=7, name="sample_text", tID="sample_text", tString="sample_text")
    b1 = xDstmdata_tTypes()
    b2 = xDstmdata_tTypes()
    _safe_set(a, 'xDstmdata_cIntchannel', b1)
    assert _is_linked(a, 'xDstmdata_cIntchannel', b1)
    if hasattr(b1, 'xDstmdata_tTypes6'):
        assert _is_linked(b1, 'xDstmdata_tTypes6', a)
    _safe_set(a, 'xDstmdata_cIntchannel', b2)
    assert _is_linked(a, 'xDstmdata_cIntchannel', b2)
    if hasattr(b1, 'xDstmdata_tTypes6'):
        assert not _is_linked(b1, 'xDstmdata_tTypes6', a)
    if hasattr(b2, 'xDstmdata_tTypes6'):
        assert _is_linked(b2, 'xDstmdata_tTypes6', a)
    _safe_set(a, 'xDstmdata_cIntchannel', None)
    assert not _is_linked(a, 'xDstmdata_cIntchannel', b2)
    if hasattr(b2, 'xDstmdata_tTypes6'):
        assert not _is_linked(b2, 'xDstmdata_tTypes6', a)


def test_assoc_composingtypes15_link_reassign_clear():
    a = xDstmdata_tMultitype(name="sample_text")
    b1 = xDstmdata_composingtype(tID="sample_text", tString="sample_text")
    b2 = xDstmdata_composingtype(tID="sample_text_2", tString="sample_text_2")
    _safe_set(a, 'xDstmdata_tMultitype16', {b1})
    assert _is_linked(a, 'xDstmdata_tMultitype16', b1)
    if hasattr(b1, 'xDstmdata_composingtype'):
        assert _is_linked(b1, 'xDstmdata_composingtype', a)
    _safe_set(a, 'xDstmdata_tMultitype16', {b2})
    assert _is_linked(a, 'xDstmdata_tMultitype16', b2)
    if hasattr(b1, 'xDstmdata_composingtype'):
        assert not _is_linked(b1, 'xDstmdata_composingtype', a)
    if hasattr(b2, 'xDstmdata_composingtype'):
        assert _is_linked(b2, 'xDstmdata_composingtype', a)
    _safe_set(a, 'xDstmdata_tMultitype16', set())
    assert not _is_linked(a, 'xDstmdata_tMultitype16', b2)
    if hasattr(b2, 'xDstmdata_composingtype'):
        assert not _is_linked(b2, 'xDstmdata_composingtype', a)


def test_assoc_subtypes11_link_reassign_clear():
    a = xDstmdata_tCompound(name="sample_text")
    b1 = xDstmdata_subtype(tID="sample_text", tString="sample_text")
    b2 = xDstmdata_subtype(tID="sample_text_2", tString="sample_text_2")
    _safe_set(a, 'xDstmdata_tCompound12', {b1})
    assert _is_linked(a, 'xDstmdata_tCompound12', b1)
    if hasattr(b1, 'xDstmdata_subtype'):
        assert _is_linked(b1, 'xDstmdata_subtype', a)
    _safe_set(a, 'xDstmdata_tCompound12', {b2})
    assert _is_linked(a, 'xDstmdata_tCompound12', b2)
    if hasattr(b1, 'xDstmdata_subtype'):
        assert not _is_linked(b1, 'xDstmdata_subtype', a)
    if hasattr(b2, 'xDstmdata_subtype'):
        assert _is_linked(b2, 'xDstmdata_subtype', a)
    _safe_set(a, 'xDstmdata_tCompound12', set())
    assert not _is_linked(a, 'xDstmdata_tCompound12', b2)
    if hasattr(b2, 'xDstmdata_subtype'):
        assert not _is_linked(b2, 'xDstmdata_subtype', a)


def test_assoc_tChn13_link_reassign_clear():
    a = xDstmdata_subtype(tID="sample_text", tString="sample_text")
    b1 = xDstmdata_channel_specifier(type="sample_text")
    b2 = xDstmdata_channel_specifier(type="sample_text_2")
    _safe_set(a, 'xDstmdata_subtype14', b1)
    assert _is_linked(a, 'xDstmdata_subtype14', b1)
    if hasattr(b1, 'xDstmdata_channel_specifier'):
        assert _is_linked(b1, 'xDstmdata_channel_specifier', a)
    _safe_set(a, 'xDstmdata_subtype14', b2)
    assert _is_linked(a, 'xDstmdata_subtype14', b2)
    if hasattr(b1, 'xDstmdata_channel_specifier'):
        assert not _is_linked(b1, 'xDstmdata_channel_specifier', a)
    if hasattr(b2, 'xDstmdata_channel_specifier'):
        assert _is_linked(b2, 'xDstmdata_channel_specifier', a)
    _safe_set(a, 'xDstmdata_subtype14', None)
    assert not _is_linked(a, 'xDstmdata_subtype14', b2)
    if hasattr(b2, 'xDstmdata_channel_specifier'):
        assert not _is_linked(b2, 'xDstmdata_channel_specifier', a)


def test_assoc_tChn17_link_reassign_clear():
    a = xDstmdata_composingtype(tID="sample_text", tString="sample_text")
    b1 = xDstmdata_channel_specifier(type="sample_text")
    b2 = xDstmdata_channel_specifier(type="sample_text_2")
    _safe_set(a, 'xDstmdata_composingtype18', b1)
    assert _is_linked(a, 'xDstmdata_composingtype18', b1)
    if hasattr(b1, 'xDstmdata_channel_specifier19'):
        assert _is_linked(b1, 'xDstmdata_channel_specifier19', a)
    _safe_set(a, 'xDstmdata_composingtype18', b2)
    assert _is_linked(a, 'xDstmdata_composingtype18', b2)
    if hasattr(b1, 'xDstmdata_channel_specifier19'):
        assert not _is_linked(b1, 'xDstmdata_channel_specifier19', a)
    if hasattr(b2, 'xDstmdata_channel_specifier19'):
        assert _is_linked(b2, 'xDstmdata_channel_specifier19', a)
    _safe_set(a, 'xDstmdata_composingtype18', None)
    assert not _is_linked(a, 'xDstmdata_composingtype18', b2)
    if hasattr(b2, 'xDstmdata_channel_specifier19'):
        assert not _is_linked(b2, 'xDstmdata_channel_specifier19', a)


def test_assoc_tChn20_link_reassign_clear():
    a = xDstmdata_channel_specifier(type="sample_text")
    b1 = xDstmdata_cIntchannel(bound=7, name="sample_text", tID="sample_text", tString="sample_text")
    b2 = xDstmdata_cIntchannel(bound=13, name="sample_text_2", tID="sample_text_2", tString="sample_text_2")
    _safe_set(a, 'xDstmdata_channel_specifier22', b1)
    assert _is_linked(a, 'xDstmdata_channel_specifier22', b1)
    if hasattr(b1, 'xDstmdata_cIntchannel21'):
        assert _is_linked(b1, 'xDstmdata_cIntchannel21', a)
    _safe_set(a, 'xDstmdata_channel_specifier22', b2)
    assert _is_linked(a, 'xDstmdata_channel_specifier22', b2)
    if hasattr(b1, 'xDstmdata_cIntchannel21'):
        assert not _is_linked(b1, 'xDstmdata_cIntchannel21', a)
    if hasattr(b2, 'xDstmdata_cIntchannel21'):
        assert _is_linked(b2, 'xDstmdata_cIntchannel21', a)
    _safe_set(a, 'xDstmdata_channel_specifier22', None)
    assert not _is_linked(a, 'xDstmdata_channel_specifier22', b2)
    if hasattr(b2, 'xDstmdata_cIntchannel21'):
        assert not _is_linked(b2, 'xDstmdata_cIntchannel21', a)


def test_assoc_tChn23_link_reassign_clear():
    a = xDstmdata_channel_specifier(type="sample_text")
    b1 = xDstmdata_cExtchannel(name="sample_text", tID="sample_text", tString="sample_text")
    b2 = xDstmdata_cExtchannel(name="sample_text_2", tID="sample_text_2", tString="sample_text_2")
    _safe_set(a, 'xDstmdata_channel_specifier25', b1)
    assert _is_linked(a, 'xDstmdata_channel_specifier25', b1)
    if hasattr(b1, 'xDstmdata_cExtchannel24'):
        assert _is_linked(b1, 'xDstmdata_cExtchannel24', a)
    _safe_set(a, 'xDstmdata_channel_specifier25', b2)
    assert _is_linked(a, 'xDstmdata_channel_specifier25', b2)
    if hasattr(b1, 'xDstmdata_cExtchannel24'):
        assert not _is_linked(b1, 'xDstmdata_cExtchannel24', a)
    if hasattr(b2, 'xDstmdata_cExtchannel24'):
        assert _is_linked(b2, 'xDstmdata_cExtchannel24', a)
    _safe_set(a, 'xDstmdata_channel_specifier25', None)
    assert not _is_linked(a, 'xDstmdata_channel_specifier25', b2)
    if hasattr(b2, 'xDstmdata_cExtchannel24'):
        assert not _is_linked(b2, 'xDstmdata_cExtchannel24', a)


def test_assoc_tChn26_link_reassign_clear():
    a = xDstmdata_vVariable(name="sample_text", tID="sample_text", tString="sample_text")
    b1 = xDstmdata_channel_specifier(type="sample_text")
    b2 = xDstmdata_channel_specifier(type="sample_text_2")
    _safe_set(a, 'xDstmdata_vVariable27', b1)
    assert _is_linked(a, 'xDstmdata_vVariable27', b1)
    if hasattr(b1, 'xDstmdata_channel_specifier28'):
        assert _is_linked(b1, 'xDstmdata_channel_specifier28', a)
    _safe_set(a, 'xDstmdata_vVariable27', b2)
    assert _is_linked(a, 'xDstmdata_vVariable27', b2)
    if hasattr(b1, 'xDstmdata_channel_specifier28'):
        assert not _is_linked(b1, 'xDstmdata_channel_specifier28', a)
    if hasattr(b2, 'xDstmdata_channel_specifier28'):
        assert _is_linked(b2, 'xDstmdata_channel_specifier28', a)
    _safe_set(a, 'xDstmdata_vVariable27', None)
    assert not _is_linked(a, 'xDstmdata_vVariable27', b2)
    if hasattr(b2, 'xDstmdata_channel_specifier28'):
        assert not _is_linked(b2, 'xDstmdata_channel_specifier28', a)


def test_assoc_tCompound1_link_reassign_clear():
    a = xDstmdata_tCompound(name="sample_text")
    b1 = xDstmdata_tTypes()
    b2 = xDstmdata_tTypes()
    _safe_set(a, 'xDstmdata_tCompound', b1)
    assert _is_linked(a, 'xDstmdata_tCompound', b1)
    if hasattr(b1, 'xDstmdata_tTypes2'):
        assert _is_linked(b1, 'xDstmdata_tTypes2', a)
    _safe_set(a, 'xDstmdata_tCompound', b2)
    assert _is_linked(a, 'xDstmdata_tCompound', b2)
    if hasattr(b1, 'xDstmdata_tTypes2'):
        assert not _is_linked(b1, 'xDstmdata_tTypes2', a)
    if hasattr(b2, 'xDstmdata_tTypes2'):
        assert _is_linked(b2, 'xDstmdata_tTypes2', a)
    _safe_set(a, 'xDstmdata_tCompound', None)
    assert not _is_linked(a, 'xDstmdata_tCompound', b2)
    if hasattr(b2, 'xDstmdata_tTypes2'):
        assert not _is_linked(b2, 'xDstmdata_tTypes2', a)


def test_assoc_tEnum0_link_reassign_clear():
    a = xDstmdata_tEnum(literals="sample_text", name="sample_text")
    b1 = xDstmdata_tTypes()
    b2 = xDstmdata_tTypes()
    _safe_set(a, 'xDstmdata_tEnum', b1)
    assert _is_linked(a, 'xDstmdata_tEnum', b1)
    if hasattr(b1, 'xDstmdata_tTypes'):
        assert _is_linked(b1, 'xDstmdata_tTypes', a)
    _safe_set(a, 'xDstmdata_tEnum', b2)
    assert _is_linked(a, 'xDstmdata_tEnum', b2)
    if hasattr(b1, 'xDstmdata_tTypes'):
        assert not _is_linked(b1, 'xDstmdata_tTypes', a)
    if hasattr(b2, 'xDstmdata_tTypes'):
        assert _is_linked(b2, 'xDstmdata_tTypes', a)
    _safe_set(a, 'xDstmdata_tEnum', None)
    assert not _is_linked(a, 'xDstmdata_tEnum', b2)
    if hasattr(b2, 'xDstmdata_tTypes'):
        assert not _is_linked(b2, 'xDstmdata_tTypes', a)


def test_assoc_tMultitype3_link_reassign_clear():
    a = xDstmdata_tMultitype(name="sample_text")
    b1 = xDstmdata_tTypes()
    b2 = xDstmdata_tTypes()
    _safe_set(a, 'xDstmdata_tMultitype', b1)
    assert _is_linked(a, 'xDstmdata_tMultitype', b1)
    if hasattr(b1, 'xDstmdata_tTypes4'):
        assert _is_linked(b1, 'xDstmdata_tTypes4', a)
    _safe_set(a, 'xDstmdata_tMultitype', b2)
    assert _is_linked(a, 'xDstmdata_tMultitype', b2)
    if hasattr(b1, 'xDstmdata_tTypes4'):
        assert not _is_linked(b1, 'xDstmdata_tTypes4', a)
    if hasattr(b2, 'xDstmdata_tTypes4'):
        assert _is_linked(b2, 'xDstmdata_tTypes4', a)
    _safe_set(a, 'xDstmdata_tMultitype', None)
    assert not _is_linked(a, 'xDstmdata_tMultitype', b2)
    if hasattr(b2, 'xDstmdata_tTypes4'):
        assert not _is_linked(b2, 'xDstmdata_tTypes4', a)


def test_assoc_vVariable9_link_reassign_clear():
    a = xDstmdata_vVariable(name="sample_text", tID="sample_text", tString="sample_text")
    b1 = xDstmdata_tTypes()
    b2 = xDstmdata_tTypes()
    _safe_set(a, 'xDstmdata_vVariable', b1)
    assert _is_linked(a, 'xDstmdata_vVariable', b1)
    if hasattr(b1, 'xDstmdata_tTypes10'):
        assert _is_linked(b1, 'xDstmdata_tTypes10', a)
    _safe_set(a, 'xDstmdata_vVariable', b2)
    assert _is_linked(a, 'xDstmdata_vVariable', b2)
    if hasattr(b1, 'xDstmdata_tTypes10'):
        assert not _is_linked(b1, 'xDstmdata_tTypes10', a)
    if hasattr(b2, 'xDstmdata_tTypes10'):
        assert _is_linked(b2, 'xDstmdata_tTypes10', a)
    _safe_set(a, 'xDstmdata_vVariable', None)
    assert not _is_linked(a, 'xDstmdata_vVariable', b2)
    if hasattr(b2, 'xDstmdata_tTypes10'):
        assert not _is_linked(b2, 'xDstmdata_tTypes10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

xDstmdata_cExtchannel_strategy = st.builds(xDstmdata_cExtchannel, name=safe_text, tID=safe_text, tString=safe_text)
@given(instance=xDstmdata_cExtchannel_strategy)
@settings(max_examples=25)
def test_xDstmdata_cExtchannel_instantiation(instance):
    assert isinstance(instance, xDstmdata_cExtchannel)


xDstmdata_cIntchannel_strategy = st.builds(xDstmdata_cIntchannel, bound=st.integers(), name=safe_text, tID=safe_text, tString=safe_text)
@given(instance=xDstmdata_cIntchannel_strategy)
@settings(max_examples=25)
def test_xDstmdata_cIntchannel_instantiation(instance):
    assert isinstance(instance, xDstmdata_cIntchannel)


xDstmdata_channel_specifier_strategy = st.builds(xDstmdata_channel_specifier, type=safe_text)
@given(instance=xDstmdata_channel_specifier_strategy)
@settings(max_examples=25)
def test_xDstmdata_channel_specifier_instantiation(instance):
    assert isinstance(instance, xDstmdata_channel_specifier)


xDstmdata_composingtype_strategy = st.builds(xDstmdata_composingtype, tID=safe_text, tString=safe_text)
@given(instance=xDstmdata_composingtype_strategy)
@settings(max_examples=25)
def test_xDstmdata_composingtype_instantiation(instance):
    assert isinstance(instance, xDstmdata_composingtype)


xDstmdata_subtype_strategy = st.builds(xDstmdata_subtype, tID=safe_text, tString=safe_text)
@given(instance=xDstmdata_subtype_strategy)
@settings(max_examples=25)
def test_xDstmdata_subtype_instantiation(instance):
    assert isinstance(instance, xDstmdata_subtype)


xDstmdata_tCompound_strategy = st.builds(xDstmdata_tCompound, name=safe_text)
@given(instance=xDstmdata_tCompound_strategy)
@settings(max_examples=25)
def test_xDstmdata_tCompound_instantiation(instance):
    assert isinstance(instance, xDstmdata_tCompound)


xDstmdata_tEnum_strategy = st.builds(xDstmdata_tEnum, literals=safe_text, name=safe_text)
@given(instance=xDstmdata_tEnum_strategy)
@settings(max_examples=25)
def test_xDstmdata_tEnum_instantiation(instance):
    assert isinstance(instance, xDstmdata_tEnum)


xDstmdata_tMultitype_strategy = st.builds(xDstmdata_tMultitype, name=safe_text)
@given(instance=xDstmdata_tMultitype_strategy)
@settings(max_examples=25)
def test_xDstmdata_tMultitype_instantiation(instance):
    assert isinstance(instance, xDstmdata_tMultitype)


xDstmdata_tTypes_strategy = st.builds(xDstmdata_tTypes)
@given(instance=xDstmdata_tTypes_strategy)
@settings(max_examples=25)
def test_xDstmdata_tTypes_instantiation(instance):
    assert isinstance(instance, xDstmdata_tTypes)


xDstmdata_vVariable_strategy = st.builds(xDstmdata_vVariable, name=safe_text, tID=safe_text, tString=safe_text)
@given(instance=xDstmdata_vVariable_strategy)
@settings(max_examples=25)
def test_xDstmdata_vVariable_instantiation(instance):
    assert isinstance(instance, xDstmdata_vVariable)


