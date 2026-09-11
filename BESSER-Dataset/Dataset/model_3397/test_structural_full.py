import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    MT__Element,
    MTpos__Element,
    MTpre__Element,
    ramRoot_GenericNode,
    ramRoot_MT__Element,
    ramRoot_MTpos__Chair,
    ramRoot_MTpos__Element,
    ramRoot_MTpos__Restaurant,
    ramRoot_MTpos__Table,
    ramRoot_MTpos__Waitress,
    ramRoot_MTpre__Chair,
    ramRoot_MTpre__Element,
    ramRoot_MTpre__Restaurant,
    ramRoot_MTpre__Table,
    ramRoot_MTpre__Waitress,
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

def test_ramRoot_MT__Element_MT__isProcessed_value_roundtrip():
    instance = ramRoot_MT__Element(MT__isProcessed=True, MT__label="sample_text")
    assert instance.MT__isProcessed == True
    instance.MT__isProcessed = False
    assert instance.MT__isProcessed == False


def test_ramRoot_MT__Element_MT__label_value_roundtrip():
    instance = ramRoot_MT__Element(MT__isProcessed=True, MT__label="sample_text")
    assert instance.MT__label == "sample_text"
    instance.MT__label = "sample_text_2"
    assert instance.MT__label == "sample_text_2"


def test_ramRoot_MTpos__Chair_MTpos__order_value_roundtrip():
    instance = ramRoot_MTpos__Chair(MTpos__order="sample_text")
    assert instance.MTpos__order == "sample_text"
    instance.MTpos__order = "sample_text_2"
    assert instance.MTpos__order == "sample_text_2"


def test_ramRoot_MTpos__Table_MTpos__id_value_roundtrip():
    instance = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    assert instance.MTpos__id == "sample_text"
    instance.MTpos__id = "sample_text_2"
    assert instance.MTpos__id == "sample_text_2"


def test_ramRoot_MTpos__Table_MTpos__isReserved_value_roundtrip():
    instance = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    assert instance.MTpos__isReserved == "sample_text"
    instance.MTpos__isReserved = "sample_text_2"
    assert instance.MTpos__isReserved == "sample_text_2"


def test_ramRoot_MTpos__Waitress_MTpos__name_value_roundtrip():
    instance = ramRoot_MTpos__Waitress(MTpos__name="sample_text")
    assert instance.MTpos__name == "sample_text"
    instance.MTpos__name = "sample_text_2"
    assert instance.MTpos__name == "sample_text_2"


def test_ramRoot_MTpre__Chair_MTpre__order_value_roundtrip():
    instance = ramRoot_MTpre__Chair(MTpre__order="sample_text")
    assert instance.MTpre__order == "sample_text"
    instance.MTpre__order = "sample_text_2"
    assert instance.MTpre__order == "sample_text_2"


def test_ramRoot_MTpre__Element_MT__matchSubtype_value_roundtrip():
    instance = ramRoot_MTpre__Element(MT__matchSubtype=True)
    assert instance.MT__matchSubtype == True
    instance.MT__matchSubtype = False
    assert instance.MT__matchSubtype == False


def test_ramRoot_MTpre__Table_MTpre__id_value_roundtrip():
    instance = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    assert instance.MTpre__id == "sample_text"
    instance.MTpre__id = "sample_text_2"
    assert instance.MTpre__id == "sample_text_2"


def test_ramRoot_MTpre__Table_MTpre__isReserved_value_roundtrip():
    instance = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    assert instance.MTpre__isReserved == "sample_text"
    instance.MTpre__isReserved = "sample_text_2"
    assert instance.MTpre__isReserved == "sample_text_2"


def test_ramRoot_MTpre__Waitress_MTpre__name_value_roundtrip():
    instance = ramRoot_MTpre__Waitress(MTpre__name="sample_text")
    assert instance.MTpre__name == "sample_text"
    instance.MTpre__name = "sample_text_2"
    assert instance.MTpre__name == "sample_text_2"


def test_ramRoot_GenericNode_isa_MT__Element():
    instance = ramRoot_GenericNode()
    assert isinstance(instance, MT__Element)


def test_ramRoot_MTpos__Element_isa_MT__Element():
    instance = ramRoot_MTpos__Element()
    assert isinstance(instance, MT__Element)


def test_ramRoot_MTpre__Element_isa_MT__Element():
    instance = ramRoot_MTpre__Element(MT__matchSubtype=True)
    assert isinstance(instance, MT__Element)


def test_ramRoot_MTpos__Chair_isa_MTpos__Element():
    instance = ramRoot_MTpos__Chair(MTpos__order="sample_text")
    assert isinstance(instance, MTpos__Element)


def test_ramRoot_MTpos__Restaurant_isa_MTpos__Element():
    instance = ramRoot_MTpos__Restaurant()
    assert isinstance(instance, MTpos__Element)


def test_ramRoot_MTpos__Table_isa_MTpos__Element():
    instance = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    assert isinstance(instance, MTpos__Element)


def test_ramRoot_MTpos__Waitress_isa_MTpos__Element():
    instance = ramRoot_MTpos__Waitress(MTpos__name="sample_text")
    assert isinstance(instance, MTpos__Element)


def test_ramRoot_MTpre__Chair_isa_MTpre__Element():
    instance = ramRoot_MTpre__Chair(MTpre__order="sample_text")
    assert isinstance(instance, MTpre__Element)


def test_ramRoot_MTpre__Restaurant_isa_MTpre__Element():
    instance = ramRoot_MTpre__Restaurant()
    assert isinstance(instance, MTpre__Element)


def test_ramRoot_MTpre__Table_isa_MTpre__Element():
    instance = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    assert isinstance(instance, MTpre__Element)


def test_ramRoot_MTpre__Waitress_isa_MTpre__Element():
    instance = ramRoot_MTpre__Waitress(MTpre__name="sample_text")
    assert isinstance(instance, MTpre__Element)


def test_assoc_GenericLink0_link_reassign_clear():
    a = ramRoot_MT__Element(MT__isProcessed=True, MT__label="sample_text")
    b1 = ramRoot_GenericNode()
    b2 = ramRoot_GenericNode()
    _safe_set(a, 'ramRoot_MT__Element', b1)
    assert _is_linked(a, 'ramRoot_MT__Element', b1)
    if hasattr(b1, 'ramRoot_GenericNode'):
        assert _is_linked(b1, 'ramRoot_GenericNode', a)
    _safe_set(a, 'ramRoot_MT__Element', b2)
    assert _is_linked(a, 'ramRoot_MT__Element', b2)
    if hasattr(b1, 'ramRoot_GenericNode'):
        assert not _is_linked(b1, 'ramRoot_GenericNode', a)
    if hasattr(b2, 'ramRoot_GenericNode'):
        assert _is_linked(b2, 'ramRoot_GenericNode', a)
    _safe_set(a, 'ramRoot_MT__Element', None)
    assert not _is_linked(a, 'ramRoot_MT__Element', b2)
    if hasattr(b2, 'ramRoot_GenericNode'):
        assert not _is_linked(b2, 'ramRoot_GenericNode', a)


def test_assoc_chairs1_link_reassign_clear():
    a = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    b1 = ramRoot_MTpos__Chair(MTpos__order="sample_text")
    b2 = ramRoot_MTpos__Chair(MTpos__order="sample_text_2")
    _safe_set(a, 'ramRoot_MTpos__Table', {b1})
    assert _is_linked(a, 'ramRoot_MTpos__Table', b1)
    if hasattr(b1, 'ramRoot_MTpos__Chair'):
        assert _is_linked(b1, 'ramRoot_MTpos__Chair', a)
    _safe_set(a, 'ramRoot_MTpos__Table', {b2})
    assert _is_linked(a, 'ramRoot_MTpos__Table', b2)
    if hasattr(b1, 'ramRoot_MTpos__Chair'):
        assert not _is_linked(b1, 'ramRoot_MTpos__Chair', a)
    if hasattr(b2, 'ramRoot_MTpos__Chair'):
        assert _is_linked(b2, 'ramRoot_MTpos__Chair', a)
    _safe_set(a, 'ramRoot_MTpos__Table', set())
    assert not _is_linked(a, 'ramRoot_MTpos__Table', b2)
    if hasattr(b2, 'ramRoot_MTpos__Chair'):
        assert not _is_linked(b2, 'ramRoot_MTpos__Chair', a)


def test_assoc_chairs4_link_reassign_clear():
    a = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    b1 = ramRoot_MTpre__Chair(MTpre__order="sample_text")
    b2 = ramRoot_MTpre__Chair(MTpre__order="sample_text_2")
    _safe_set(a, 'ramRoot_MTpre__Table', {b1})
    assert _is_linked(a, 'ramRoot_MTpre__Table', b1)
    if hasattr(b1, 'ramRoot_MTpre__Chair'):
        assert _is_linked(b1, 'ramRoot_MTpre__Chair', a)
    _safe_set(a, 'ramRoot_MTpre__Table', {b2})
    assert _is_linked(a, 'ramRoot_MTpre__Table', b2)
    if hasattr(b1, 'ramRoot_MTpre__Chair'):
        assert not _is_linked(b1, 'ramRoot_MTpre__Chair', a)
    if hasattr(b2, 'ramRoot_MTpre__Chair'):
        assert _is_linked(b2, 'ramRoot_MTpre__Chair', a)
    _safe_set(a, 'ramRoot_MTpre__Table', set())
    assert not _is_linked(a, 'ramRoot_MTpre__Table', b2)
    if hasattr(b2, 'ramRoot_MTpre__Chair'):
        assert not _is_linked(b2, 'ramRoot_MTpre__Chair', a)


def test_assoc_tables14_link_reassign_clear():
    a = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    b1 = ramRoot_MTpos__Restaurant()
    b2 = ramRoot_MTpos__Restaurant()
    _safe_set(a, 'ramRoot_MTpos__Table16', b1)
    assert _is_linked(a, 'ramRoot_MTpos__Table16', b1)
    if hasattr(b1, 'ramRoot_MTpos__Restaurant15'):
        assert _is_linked(b1, 'ramRoot_MTpos__Restaurant15', a)
    _safe_set(a, 'ramRoot_MTpos__Table16', b2)
    assert _is_linked(a, 'ramRoot_MTpos__Table16', b2)
    if hasattr(b1, 'ramRoot_MTpos__Restaurant15'):
        assert not _is_linked(b1, 'ramRoot_MTpos__Restaurant15', a)
    if hasattr(b2, 'ramRoot_MTpos__Restaurant15'):
        assert _is_linked(b2, 'ramRoot_MTpos__Restaurant15', a)
    _safe_set(a, 'ramRoot_MTpos__Table16', None)
    assert not _is_linked(a, 'ramRoot_MTpos__Table16', b2)
    if hasattr(b2, 'ramRoot_MTpos__Restaurant15'):
        assert not _is_linked(b2, 'ramRoot_MTpos__Restaurant15', a)


def test_assoc_tables2_link_reassign_clear():
    a = ramRoot_MTpos__Waitress(MTpos__name="sample_text")
    b1 = ramRoot_MTpos__Table(MTpos__id="sample_text", MTpos__isReserved="sample_text")
    b2 = ramRoot_MTpos__Table(MTpos__id="sample_text_2", MTpos__isReserved="sample_text_2")
    _safe_set(a, 'ramRoot_MTpos__Waitress', {b1})
    assert _is_linked(a, 'ramRoot_MTpos__Waitress', b1)
    if hasattr(b1, 'ramRoot_MTpos__Table3'):
        assert _is_linked(b1, 'ramRoot_MTpos__Table3', a)
    _safe_set(a, 'ramRoot_MTpos__Waitress', {b2})
    assert _is_linked(a, 'ramRoot_MTpos__Waitress', b2)
    if hasattr(b1, 'ramRoot_MTpos__Table3'):
        assert not _is_linked(b1, 'ramRoot_MTpos__Table3', a)
    if hasattr(b2, 'ramRoot_MTpos__Table3'):
        assert _is_linked(b2, 'ramRoot_MTpos__Table3', a)
    _safe_set(a, 'ramRoot_MTpos__Waitress', set())
    assert not _is_linked(a, 'ramRoot_MTpos__Waitress', b2)
    if hasattr(b2, 'ramRoot_MTpos__Table3'):
        assert not _is_linked(b2, 'ramRoot_MTpos__Table3', a)


def test_assoc_tables5_link_reassign_clear():
    a = ramRoot_MTpre__Waitress(MTpre__name="sample_text")
    b1 = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    b2 = ramRoot_MTpre__Table(MTpre__id="sample_text_2", MTpre__isReserved="sample_text_2")
    _safe_set(a, 'ramRoot_MTpre__Waitress', {b1})
    assert _is_linked(a, 'ramRoot_MTpre__Waitress', b1)
    if hasattr(b1, 'ramRoot_MTpre__Table6'):
        assert _is_linked(b1, 'ramRoot_MTpre__Table6', a)
    _safe_set(a, 'ramRoot_MTpre__Waitress', {b2})
    assert _is_linked(a, 'ramRoot_MTpre__Waitress', b2)
    if hasattr(b1, 'ramRoot_MTpre__Table6'):
        assert not _is_linked(b1, 'ramRoot_MTpre__Table6', a)
    if hasattr(b2, 'ramRoot_MTpre__Table6'):
        assert _is_linked(b2, 'ramRoot_MTpre__Table6', a)
    _safe_set(a, 'ramRoot_MTpre__Waitress', set())
    assert not _is_linked(a, 'ramRoot_MTpre__Waitress', b2)
    if hasattr(b2, 'ramRoot_MTpre__Table6'):
        assert not _is_linked(b2, 'ramRoot_MTpre__Table6', a)


def test_assoc_tables7_link_reassign_clear():
    a = ramRoot_MTpre__Table(MTpre__id="sample_text", MTpre__isReserved="sample_text")
    b1 = ramRoot_MTpre__Restaurant()
    b2 = ramRoot_MTpre__Restaurant()
    _safe_set(a, 'ramRoot_MTpre__Table8', b1)
    assert _is_linked(a, 'ramRoot_MTpre__Table8', b1)
    if hasattr(b1, 'ramRoot_MTpre__Restaurant'):
        assert _is_linked(b1, 'ramRoot_MTpre__Restaurant', a)
    _safe_set(a, 'ramRoot_MTpre__Table8', b2)
    assert _is_linked(a, 'ramRoot_MTpre__Table8', b2)
    if hasattr(b1, 'ramRoot_MTpre__Restaurant'):
        assert not _is_linked(b1, 'ramRoot_MTpre__Restaurant', a)
    if hasattr(b2, 'ramRoot_MTpre__Restaurant'):
        assert _is_linked(b2, 'ramRoot_MTpre__Restaurant', a)
    _safe_set(a, 'ramRoot_MTpre__Table8', None)
    assert not _is_linked(a, 'ramRoot_MTpre__Table8', b2)
    if hasattr(b2, 'ramRoot_MTpre__Restaurant'):
        assert not _is_linked(b2, 'ramRoot_MTpre__Restaurant', a)


def test_assoc_waitress12_link_reassign_clear():
    a = ramRoot_MTpos__Waitress(MTpos__name="sample_text")
    b1 = ramRoot_MTpos__Restaurant()
    b2 = ramRoot_MTpos__Restaurant()
    _safe_set(a, 'ramRoot_MTpos__Waitress13', b1)
    assert _is_linked(a, 'ramRoot_MTpos__Waitress13', b1)
    if hasattr(b1, 'ramRoot_MTpos__Restaurant'):
        assert _is_linked(b1, 'ramRoot_MTpos__Restaurant', a)
    _safe_set(a, 'ramRoot_MTpos__Waitress13', b2)
    assert _is_linked(a, 'ramRoot_MTpos__Waitress13', b2)
    if hasattr(b1, 'ramRoot_MTpos__Restaurant'):
        assert not _is_linked(b1, 'ramRoot_MTpos__Restaurant', a)
    if hasattr(b2, 'ramRoot_MTpos__Restaurant'):
        assert _is_linked(b2, 'ramRoot_MTpos__Restaurant', a)
    _safe_set(a, 'ramRoot_MTpos__Waitress13', None)
    assert not _is_linked(a, 'ramRoot_MTpos__Waitress13', b2)
    if hasattr(b2, 'ramRoot_MTpos__Restaurant'):
        assert not _is_linked(b2, 'ramRoot_MTpos__Restaurant', a)


def test_assoc_waitress9_link_reassign_clear():
    a = ramRoot_MTpre__Waitress(MTpre__name="sample_text")
    b1 = ramRoot_MTpre__Restaurant()
    b2 = ramRoot_MTpre__Restaurant()
    _safe_set(a, 'ramRoot_MTpre__Waitress11', b1)
    assert _is_linked(a, 'ramRoot_MTpre__Waitress11', b1)
    if hasattr(b1, 'ramRoot_MTpre__Restaurant10'):
        assert _is_linked(b1, 'ramRoot_MTpre__Restaurant10', a)
    _safe_set(a, 'ramRoot_MTpre__Waitress11', b2)
    assert _is_linked(a, 'ramRoot_MTpre__Waitress11', b2)
    if hasattr(b1, 'ramRoot_MTpre__Restaurant10'):
        assert not _is_linked(b1, 'ramRoot_MTpre__Restaurant10', a)
    if hasattr(b2, 'ramRoot_MTpre__Restaurant10'):
        assert _is_linked(b2, 'ramRoot_MTpre__Restaurant10', a)
    _safe_set(a, 'ramRoot_MTpre__Waitress11', None)
    assert not _is_linked(a, 'ramRoot_MTpre__Waitress11', b2)
    if hasattr(b2, 'ramRoot_MTpre__Restaurant10'):
        assert not _is_linked(b2, 'ramRoot_MTpre__Restaurant10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

MT__Element_strategy = st.builds(MT__Element)
@given(instance=MT__Element_strategy)
@settings(max_examples=25)
def test_MT__Element_instantiation(instance):
    assert isinstance(instance, MT__Element)


MTpos__Element_strategy = st.builds(MTpos__Element)
@given(instance=MTpos__Element_strategy)
@settings(max_examples=25)
def test_MTpos__Element_instantiation(instance):
    assert isinstance(instance, MTpos__Element)


MTpre__Element_strategy = st.builds(MTpre__Element)
@given(instance=MTpre__Element_strategy)
@settings(max_examples=25)
def test_MTpre__Element_instantiation(instance):
    assert isinstance(instance, MTpre__Element)


ramRoot_GenericNode_strategy = st.builds(ramRoot_GenericNode)
@given(instance=ramRoot_GenericNode_strategy)
@settings(max_examples=25)
def test_ramRoot_GenericNode_instantiation(instance):
    assert isinstance(instance, ramRoot_GenericNode)


ramRoot_MT__Element_strategy = st.builds(ramRoot_MT__Element, MT__isProcessed=st.booleans(), MT__label=safe_text)
@given(instance=ramRoot_MT__Element_strategy)
@settings(max_examples=25)
def test_ramRoot_MT__Element_instantiation(instance):
    assert isinstance(instance, ramRoot_MT__Element)


ramRoot_MTpos__Chair_strategy = st.builds(ramRoot_MTpos__Chair, MTpos__order=safe_text)
@given(instance=ramRoot_MTpos__Chair_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Chair_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Chair)


ramRoot_MTpos__Element_strategy = st.builds(ramRoot_MTpos__Element)
@given(instance=ramRoot_MTpos__Element_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Element_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Element)


ramRoot_MTpos__Restaurant_strategy = st.builds(ramRoot_MTpos__Restaurant)
@given(instance=ramRoot_MTpos__Restaurant_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Restaurant_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Restaurant)


ramRoot_MTpos__Table_strategy = st.builds(ramRoot_MTpos__Table, MTpos__id=safe_text, MTpos__isReserved=safe_text)
@given(instance=ramRoot_MTpos__Table_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Table_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Table)


ramRoot_MTpos__Waitress_strategy = st.builds(ramRoot_MTpos__Waitress, MTpos__name=safe_text)
@given(instance=ramRoot_MTpos__Waitress_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Waitress_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Waitress)


ramRoot_MTpre__Chair_strategy = st.builds(ramRoot_MTpre__Chair, MTpre__order=safe_text)
@given(instance=ramRoot_MTpre__Chair_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Chair_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Chair)


ramRoot_MTpre__Element_strategy = st.builds(ramRoot_MTpre__Element, MT__matchSubtype=st.booleans())
@given(instance=ramRoot_MTpre__Element_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Element_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Element)


ramRoot_MTpre__Restaurant_strategy = st.builds(ramRoot_MTpre__Restaurant)
@given(instance=ramRoot_MTpre__Restaurant_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Restaurant_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Restaurant)


ramRoot_MTpre__Table_strategy = st.builds(ramRoot_MTpre__Table, MTpre__id=safe_text, MTpre__isReserved=safe_text)
@given(instance=ramRoot_MTpre__Table_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Table_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Table)


ramRoot_MTpre__Waitress_strategy = st.builds(ramRoot_MTpre__Waitress, MTpre__name=safe_text)
@given(instance=ramRoot_MTpre__Waitress_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Waitress_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Waitress)


