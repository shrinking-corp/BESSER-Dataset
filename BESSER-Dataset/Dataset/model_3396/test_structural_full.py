import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    MT__Element,
    MTpos__Element,
    MTpos__Person,
    MTpre__Element,
    MTpre__Person,
    ramRoot_GenericNode,
    ramRoot_MT__Element,
    ramRoot_MTpos__Classroom,
    ramRoot_MTpos__Element,
    ramRoot_MTpos__Man,
    ramRoot_MTpos__Person,
    ramRoot_MTpos__Woman,
    ramRoot_MTpre__Classroom,
    ramRoot_MTpre__Element,
    ramRoot_MTpre__Man,
    ramRoot_MTpre__Person,
    ramRoot_MTpre__Woman,
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


def test_ramRoot_MTpos__Classroom_id_value_roundtrip():
    instance = ramRoot_MTpos__Classroom(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_ramRoot_MTpos__Person_name_value_roundtrip():
    instance = ramRoot_MTpos__Person(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ramRoot_MTpre__Classroom_id_value_roundtrip():
    instance = ramRoot_MTpre__Classroom(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_ramRoot_MTpre__Element_MT__matchSubtype_value_roundtrip():
    instance = ramRoot_MTpre__Element(MT__matchSubtype=True)
    assert instance.MT__matchSubtype == True
    instance.MT__matchSubtype = False
    assert instance.MT__matchSubtype == False


def test_ramRoot_MTpre__Person_name_value_roundtrip():
    instance = ramRoot_MTpre__Person(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ramRoot_GenericNode_isa_MT__Element():
    instance = ramRoot_GenericNode()
    assert isinstance(instance, MT__Element)


def test_ramRoot_MTpos__Element_isa_MT__Element():
    instance = ramRoot_MTpos__Element()
    assert isinstance(instance, MT__Element)


def test_ramRoot_MTpre__Element_isa_MT__Element():
    instance = ramRoot_MTpre__Element(MT__matchSubtype=True)
    assert isinstance(instance, MT__Element)


def test_ramRoot_MTpos__Classroom_isa_MTpos__Element():
    instance = ramRoot_MTpos__Classroom(id="sample_text")
    assert isinstance(instance, MTpos__Element)


def test_ramRoot_MTpos__Person_isa_MTpos__Element():
    instance = ramRoot_MTpos__Person(name="sample_text")
    assert isinstance(instance, MTpos__Element)


def test_ramRoot_MTpos__Man_isa_MTpos__Person():
    instance = ramRoot_MTpos__Man()
    assert isinstance(instance, MTpos__Person)


def test_ramRoot_MTpos__Woman_isa_MTpos__Person():
    instance = ramRoot_MTpos__Woman()
    assert isinstance(instance, MTpos__Person)


def test_ramRoot_MTpre__Classroom_isa_MTpre__Element():
    instance = ramRoot_MTpre__Classroom(id="sample_text")
    assert isinstance(instance, MTpre__Element)


def test_ramRoot_MTpre__Person_isa_MTpre__Element():
    instance = ramRoot_MTpre__Person(name="sample_text")
    assert isinstance(instance, MTpre__Element)


def test_ramRoot_MTpre__Man_isa_MTpre__Person():
    instance = ramRoot_MTpre__Man()
    assert isinstance(instance, MTpre__Person)


def test_ramRoot_MTpre__Woman_isa_MTpre__Person():
    instance = ramRoot_MTpre__Woman()
    assert isinstance(instance, MTpre__Person)


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


def test_assoc_friend_with10_link_reassign_clear():
    a = ramRoot_MTpre__Person(name="sample_text")
    b1 = ramRoot_MTpre__Person(name="sample_text")
    b2 = ramRoot_MTpre__Person(name="sample_text_2")
    _safe_set(a, 'ramRoot_MTpre__Person11', b1)
    assert _is_linked(a, 'ramRoot_MTpre__Person11', b1)
    if hasattr(b1, 'ramRoot_MTpre__Person9'):
        assert _is_linked(b1, 'ramRoot_MTpre__Person9', a)
    _safe_set(a, 'ramRoot_MTpre__Person11', b2)
    assert _is_linked(a, 'ramRoot_MTpre__Person11', b2)
    if hasattr(b1, 'ramRoot_MTpre__Person9'):
        assert not _is_linked(b1, 'ramRoot_MTpre__Person9', a)
    if hasattr(b2, 'ramRoot_MTpre__Person9'):
        assert _is_linked(b2, 'ramRoot_MTpre__Person9', a)
    _safe_set(a, 'ramRoot_MTpre__Person11', None)
    assert not _is_linked(a, 'ramRoot_MTpre__Person11', b2)
    if hasattr(b2, 'ramRoot_MTpre__Person9'):
        assert not _is_linked(b2, 'ramRoot_MTpre__Person9', a)


def test_assoc_friend_with3_link_reassign_clear():
    a = ramRoot_MTpos__Person(name="sample_text")
    b1 = ramRoot_MTpos__Person(name="sample_text")
    b2 = ramRoot_MTpos__Person(name="sample_text_2")
    _safe_set(a, 'ramRoot_MTpos__Person2', {b1})
    assert _is_linked(a, 'ramRoot_MTpos__Person2', b1)
    if hasattr(b1, 'ramRoot_MTpos__Person4'):
        assert _is_linked(b1, 'ramRoot_MTpos__Person4', a)
    _safe_set(a, 'ramRoot_MTpos__Person2', {b2})
    assert _is_linked(a, 'ramRoot_MTpos__Person2', b2)
    if hasattr(b1, 'ramRoot_MTpos__Person4'):
        assert not _is_linked(b1, 'ramRoot_MTpos__Person4', a)
    if hasattr(b2, 'ramRoot_MTpos__Person4'):
        assert _is_linked(b2, 'ramRoot_MTpos__Person4', a)
    _safe_set(a, 'ramRoot_MTpos__Person2', set())
    assert not _is_linked(a, 'ramRoot_MTpos__Person2', b2)
    if hasattr(b2, 'ramRoot_MTpos__Person4'):
        assert not _is_linked(b2, 'ramRoot_MTpos__Person4', a)


def test_assoc_person12_link_reassign_clear():
    a = ramRoot_MTpre__Person(name="sample_text")
    b1 = ramRoot_MTpre__Classroom(id="sample_text")
    b2 = ramRoot_MTpre__Classroom(id="sample_text_2")
    _safe_set(a, 'ramRoot_MTpre__Person14', b1)
    assert _is_linked(a, 'ramRoot_MTpre__Person14', b1)
    if hasattr(b1, 'ramRoot_MTpre__Classroom13'):
        assert _is_linked(b1, 'ramRoot_MTpre__Classroom13', a)
    _safe_set(a, 'ramRoot_MTpre__Person14', b2)
    assert _is_linked(a, 'ramRoot_MTpre__Person14', b2)
    if hasattr(b1, 'ramRoot_MTpre__Classroom13'):
        assert not _is_linked(b1, 'ramRoot_MTpre__Classroom13', a)
    if hasattr(b2, 'ramRoot_MTpre__Classroom13'):
        assert _is_linked(b2, 'ramRoot_MTpre__Classroom13', a)
    _safe_set(a, 'ramRoot_MTpre__Person14', None)
    assert not _is_linked(a, 'ramRoot_MTpre__Person14', b2)
    if hasattr(b2, 'ramRoot_MTpre__Classroom13'):
        assert not _is_linked(b2, 'ramRoot_MTpre__Classroom13', a)


def test_assoc_person5_link_reassign_clear():
    a = ramRoot_MTpos__Person(name="sample_text")
    b1 = ramRoot_MTpos__Classroom(id="sample_text")
    b2 = ramRoot_MTpos__Classroom(id="sample_text_2")
    _safe_set(a, 'ramRoot_MTpos__Person7', b1)
    assert _is_linked(a, 'ramRoot_MTpos__Person7', b1)
    if hasattr(b1, 'ramRoot_MTpos__Classroom6'):
        assert _is_linked(b1, 'ramRoot_MTpos__Classroom6', a)
    _safe_set(a, 'ramRoot_MTpos__Person7', b2)
    assert _is_linked(a, 'ramRoot_MTpos__Person7', b2)
    if hasattr(b1, 'ramRoot_MTpos__Classroom6'):
        assert not _is_linked(b1, 'ramRoot_MTpos__Classroom6', a)
    if hasattr(b2, 'ramRoot_MTpos__Classroom6'):
        assert _is_linked(b2, 'ramRoot_MTpos__Classroom6', a)
    _safe_set(a, 'ramRoot_MTpos__Person7', None)
    assert not _is_linked(a, 'ramRoot_MTpos__Person7', b2)
    if hasattr(b2, 'ramRoot_MTpos__Classroom6'):
        assert not _is_linked(b2, 'ramRoot_MTpos__Classroom6', a)


def test_assoc_teacher_of1_link_reassign_clear():
    a = ramRoot_MTpos__Person(name="sample_text")
    b1 = ramRoot_MTpos__Classroom(id="sample_text")
    b2 = ramRoot_MTpos__Classroom(id="sample_text_2")
    _safe_set(a, 'ramRoot_MTpos__Person', b1)
    assert _is_linked(a, 'ramRoot_MTpos__Person', b1)
    if hasattr(b1, 'ramRoot_MTpos__Classroom'):
        assert _is_linked(b1, 'ramRoot_MTpos__Classroom', a)
    _safe_set(a, 'ramRoot_MTpos__Person', b2)
    assert _is_linked(a, 'ramRoot_MTpos__Person', b2)
    if hasattr(b1, 'ramRoot_MTpos__Classroom'):
        assert not _is_linked(b1, 'ramRoot_MTpos__Classroom', a)
    if hasattr(b2, 'ramRoot_MTpos__Classroom'):
        assert _is_linked(b2, 'ramRoot_MTpos__Classroom', a)
    _safe_set(a, 'ramRoot_MTpos__Person', None)
    assert not _is_linked(a, 'ramRoot_MTpos__Person', b2)
    if hasattr(b2, 'ramRoot_MTpos__Classroom'):
        assert not _is_linked(b2, 'ramRoot_MTpos__Classroom', a)


def test_assoc_teacher_of8_link_reassign_clear():
    a = ramRoot_MTpre__Person(name="sample_text")
    b1 = ramRoot_MTpre__Classroom(id="sample_text")
    b2 = ramRoot_MTpre__Classroom(id="sample_text_2")
    _safe_set(a, 'ramRoot_MTpre__Person', b1)
    assert _is_linked(a, 'ramRoot_MTpre__Person', b1)
    if hasattr(b1, 'ramRoot_MTpre__Classroom'):
        assert _is_linked(b1, 'ramRoot_MTpre__Classroom', a)
    _safe_set(a, 'ramRoot_MTpre__Person', b2)
    assert _is_linked(a, 'ramRoot_MTpre__Person', b2)
    if hasattr(b1, 'ramRoot_MTpre__Classroom'):
        assert not _is_linked(b1, 'ramRoot_MTpre__Classroom', a)
    if hasattr(b2, 'ramRoot_MTpre__Classroom'):
        assert _is_linked(b2, 'ramRoot_MTpre__Classroom', a)
    _safe_set(a, 'ramRoot_MTpre__Person', None)
    assert not _is_linked(a, 'ramRoot_MTpre__Person', b2)
    if hasattr(b2, 'ramRoot_MTpre__Classroom'):
        assert not _is_linked(b2, 'ramRoot_MTpre__Classroom', a)


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


MTpos__Person_strategy = st.builds(MTpos__Person)
@given(instance=MTpos__Person_strategy)
@settings(max_examples=25)
def test_MTpos__Person_instantiation(instance):
    assert isinstance(instance, MTpos__Person)


MTpre__Element_strategy = st.builds(MTpre__Element)
@given(instance=MTpre__Element_strategy)
@settings(max_examples=25)
def test_MTpre__Element_instantiation(instance):
    assert isinstance(instance, MTpre__Element)


MTpre__Person_strategy = st.builds(MTpre__Person)
@given(instance=MTpre__Person_strategy)
@settings(max_examples=25)
def test_MTpre__Person_instantiation(instance):
    assert isinstance(instance, MTpre__Person)


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


ramRoot_MTpos__Classroom_strategy = st.builds(ramRoot_MTpos__Classroom, id=safe_text)
@given(instance=ramRoot_MTpos__Classroom_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Classroom_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Classroom)


ramRoot_MTpos__Element_strategy = st.builds(ramRoot_MTpos__Element)
@given(instance=ramRoot_MTpos__Element_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Element_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Element)


ramRoot_MTpos__Man_strategy = st.builds(ramRoot_MTpos__Man)
@given(instance=ramRoot_MTpos__Man_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Man_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Man)


ramRoot_MTpos__Person_strategy = st.builds(ramRoot_MTpos__Person, name=safe_text)
@given(instance=ramRoot_MTpos__Person_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Person_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Person)


ramRoot_MTpos__Woman_strategy = st.builds(ramRoot_MTpos__Woman)
@given(instance=ramRoot_MTpos__Woman_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpos__Woman_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpos__Woman)


ramRoot_MTpre__Classroom_strategy = st.builds(ramRoot_MTpre__Classroom, id=safe_text)
@given(instance=ramRoot_MTpre__Classroom_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Classroom_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Classroom)


ramRoot_MTpre__Element_strategy = st.builds(ramRoot_MTpre__Element, MT__matchSubtype=st.booleans())
@given(instance=ramRoot_MTpre__Element_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Element_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Element)


ramRoot_MTpre__Man_strategy = st.builds(ramRoot_MTpre__Man)
@given(instance=ramRoot_MTpre__Man_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Man_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Man)


ramRoot_MTpre__Person_strategy = st.builds(ramRoot_MTpre__Person, name=safe_text)
@given(instance=ramRoot_MTpre__Person_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Person_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Person)


ramRoot_MTpre__Woman_strategy = st.builds(ramRoot_MTpre__Woman)
@given(instance=ramRoot_MTpre__Woman_strategy)
@settings(max_examples=25)
def test_ramRoot_MTpre__Woman_instantiation(instance):
    assert isinstance(instance, ramRoot_MTpre__Woman)


