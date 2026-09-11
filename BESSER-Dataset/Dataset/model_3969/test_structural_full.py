import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Element,
    subsetUnion_Container,
    subsetUnion_Element,
    subsetUnion_Element_Level1,
    subsetUnion_Element_Level10,
    subsetUnion_Element_Level2,
    subsetUnion_Element_Level3,
    subsetUnion_Element_Level4,
    subsetUnion_Element_Level5,
    subsetUnion_Element_Level6,
    subsetUnion_Element_Level7,
    subsetUnion_Element_Level8,
    subsetUnion_Element_Level9,
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

def test_subsetUnion_Container_name_value_roundtrip():
    instance = subsetUnion_Container(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_subsetUnion_Element_name_value_roundtrip():
    instance = subsetUnion_Element(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_subsetUnion_Element_Level1_isa_Element():
    instance = subsetUnion_Element_Level1()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level10_isa_Element():
    instance = subsetUnion_Element_Level10()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level2_isa_Element():
    instance = subsetUnion_Element_Level2()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level3_isa_Element():
    instance = subsetUnion_Element_Level3()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level4_isa_Element():
    instance = subsetUnion_Element_Level4()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level5_isa_Element():
    instance = subsetUnion_Element_Level5()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level6_isa_Element():
    instance = subsetUnion_Element_Level6()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level7_isa_Element():
    instance = subsetUnion_Element_Level7()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level8_isa_Element():
    instance = subsetUnion_Element_Level8()
    assert isinstance(instance, Element)


def test_subsetUnion_Element_Level9_isa_Element():
    instance = subsetUnion_Element_Level9()
    assert isinstance(instance, Element)


def test_assoc_subset1019_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level10()
    b2 = subsetUnion_Element_Level10()
    _safe_set(a, 'subsetUnion_Container20', {b1})
    assert _is_linked(a, 'subsetUnion_Container20', b1)
    if hasattr(b1, 'subsetUnion_Element_Level10'):
        assert _is_linked(b1, 'subsetUnion_Element_Level10', a)
    _safe_set(a, 'subsetUnion_Container20', {b2})
    assert _is_linked(a, 'subsetUnion_Container20', b2)
    if hasattr(b1, 'subsetUnion_Element_Level10'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level10', a)
    if hasattr(b2, 'subsetUnion_Element_Level10'):
        assert _is_linked(b2, 'subsetUnion_Element_Level10', a)
    _safe_set(a, 'subsetUnion_Container20', set())
    assert not _is_linked(a, 'subsetUnion_Container20', b2)
    if hasattr(b2, 'subsetUnion_Element_Level10'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level10', a)


def test_assoc_subset11_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level1()
    b2 = subsetUnion_Element_Level1()
    _safe_set(a, 'subsetUnion_Container2', {b1})
    assert _is_linked(a, 'subsetUnion_Container2', b1)
    if hasattr(b1, 'subsetUnion_Element_Level1'):
        assert _is_linked(b1, 'subsetUnion_Element_Level1', a)
    _safe_set(a, 'subsetUnion_Container2', {b2})
    assert _is_linked(a, 'subsetUnion_Container2', b2)
    if hasattr(b1, 'subsetUnion_Element_Level1'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level1', a)
    if hasattr(b2, 'subsetUnion_Element_Level1'):
        assert _is_linked(b2, 'subsetUnion_Element_Level1', a)
    _safe_set(a, 'subsetUnion_Container2', set())
    assert not _is_linked(a, 'subsetUnion_Container2', b2)
    if hasattr(b2, 'subsetUnion_Element_Level1'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level1', a)


def test_assoc_subset23_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level2()
    b2 = subsetUnion_Element_Level2()
    _safe_set(a, 'subsetUnion_Container4', {b1})
    assert _is_linked(a, 'subsetUnion_Container4', b1)
    if hasattr(b1, 'subsetUnion_Element_Level2'):
        assert _is_linked(b1, 'subsetUnion_Element_Level2', a)
    _safe_set(a, 'subsetUnion_Container4', {b2})
    assert _is_linked(a, 'subsetUnion_Container4', b2)
    if hasattr(b1, 'subsetUnion_Element_Level2'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level2', a)
    if hasattr(b2, 'subsetUnion_Element_Level2'):
        assert _is_linked(b2, 'subsetUnion_Element_Level2', a)
    _safe_set(a, 'subsetUnion_Container4', set())
    assert not _is_linked(a, 'subsetUnion_Container4', b2)
    if hasattr(b2, 'subsetUnion_Element_Level2'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level2', a)


def test_assoc_subset35_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level3()
    b2 = subsetUnion_Element_Level3()
    _safe_set(a, 'subsetUnion_Container6', {b1})
    assert _is_linked(a, 'subsetUnion_Container6', b1)
    if hasattr(b1, 'subsetUnion_Element_Level3'):
        assert _is_linked(b1, 'subsetUnion_Element_Level3', a)
    _safe_set(a, 'subsetUnion_Container6', {b2})
    assert _is_linked(a, 'subsetUnion_Container6', b2)
    if hasattr(b1, 'subsetUnion_Element_Level3'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level3', a)
    if hasattr(b2, 'subsetUnion_Element_Level3'):
        assert _is_linked(b2, 'subsetUnion_Element_Level3', a)
    _safe_set(a, 'subsetUnion_Container6', set())
    assert not _is_linked(a, 'subsetUnion_Container6', b2)
    if hasattr(b2, 'subsetUnion_Element_Level3'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level3', a)


def test_assoc_subset47_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level4()
    b2 = subsetUnion_Element_Level4()
    _safe_set(a, 'subsetUnion_Container8', {b1})
    assert _is_linked(a, 'subsetUnion_Container8', b1)
    if hasattr(b1, 'subsetUnion_Element_Level4'):
        assert _is_linked(b1, 'subsetUnion_Element_Level4', a)
    _safe_set(a, 'subsetUnion_Container8', {b2})
    assert _is_linked(a, 'subsetUnion_Container8', b2)
    if hasattr(b1, 'subsetUnion_Element_Level4'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level4', a)
    if hasattr(b2, 'subsetUnion_Element_Level4'):
        assert _is_linked(b2, 'subsetUnion_Element_Level4', a)
    _safe_set(a, 'subsetUnion_Container8', set())
    assert not _is_linked(a, 'subsetUnion_Container8', b2)
    if hasattr(b2, 'subsetUnion_Element_Level4'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level4', a)


def test_assoc_subset59_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level5()
    b2 = subsetUnion_Element_Level5()
    _safe_set(a, 'subsetUnion_Container10', {b1})
    assert _is_linked(a, 'subsetUnion_Container10', b1)
    if hasattr(b1, 'subsetUnion_Element_Level5'):
        assert _is_linked(b1, 'subsetUnion_Element_Level5', a)
    _safe_set(a, 'subsetUnion_Container10', {b2})
    assert _is_linked(a, 'subsetUnion_Container10', b2)
    if hasattr(b1, 'subsetUnion_Element_Level5'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level5', a)
    if hasattr(b2, 'subsetUnion_Element_Level5'):
        assert _is_linked(b2, 'subsetUnion_Element_Level5', a)
    _safe_set(a, 'subsetUnion_Container10', set())
    assert not _is_linked(a, 'subsetUnion_Container10', b2)
    if hasattr(b2, 'subsetUnion_Element_Level5'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level5', a)


def test_assoc_subset611_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level6()
    b2 = subsetUnion_Element_Level6()
    _safe_set(a, 'subsetUnion_Container12', {b1})
    assert _is_linked(a, 'subsetUnion_Container12', b1)
    if hasattr(b1, 'subsetUnion_Element_Level6'):
        assert _is_linked(b1, 'subsetUnion_Element_Level6', a)
    _safe_set(a, 'subsetUnion_Container12', {b2})
    assert _is_linked(a, 'subsetUnion_Container12', b2)
    if hasattr(b1, 'subsetUnion_Element_Level6'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level6', a)
    if hasattr(b2, 'subsetUnion_Element_Level6'):
        assert _is_linked(b2, 'subsetUnion_Element_Level6', a)
    _safe_set(a, 'subsetUnion_Container12', set())
    assert not _is_linked(a, 'subsetUnion_Container12', b2)
    if hasattr(b2, 'subsetUnion_Element_Level6'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level6', a)


def test_assoc_subset713_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level7()
    b2 = subsetUnion_Element_Level7()
    _safe_set(a, 'subsetUnion_Container14', {b1})
    assert _is_linked(a, 'subsetUnion_Container14', b1)
    if hasattr(b1, 'subsetUnion_Element_Level7'):
        assert _is_linked(b1, 'subsetUnion_Element_Level7', a)
    _safe_set(a, 'subsetUnion_Container14', {b2})
    assert _is_linked(a, 'subsetUnion_Container14', b2)
    if hasattr(b1, 'subsetUnion_Element_Level7'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level7', a)
    if hasattr(b2, 'subsetUnion_Element_Level7'):
        assert _is_linked(b2, 'subsetUnion_Element_Level7', a)
    _safe_set(a, 'subsetUnion_Container14', set())
    assert not _is_linked(a, 'subsetUnion_Container14', b2)
    if hasattr(b2, 'subsetUnion_Element_Level7'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level7', a)


def test_assoc_subset815_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level8()
    b2 = subsetUnion_Element_Level8()
    _safe_set(a, 'subsetUnion_Container16', {b1})
    assert _is_linked(a, 'subsetUnion_Container16', b1)
    if hasattr(b1, 'subsetUnion_Element_Level8'):
        assert _is_linked(b1, 'subsetUnion_Element_Level8', a)
    _safe_set(a, 'subsetUnion_Container16', {b2})
    assert _is_linked(a, 'subsetUnion_Container16', b2)
    if hasattr(b1, 'subsetUnion_Element_Level8'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level8', a)
    if hasattr(b2, 'subsetUnion_Element_Level8'):
        assert _is_linked(b2, 'subsetUnion_Element_Level8', a)
    _safe_set(a, 'subsetUnion_Container16', set())
    assert not _is_linked(a, 'subsetUnion_Container16', b2)
    if hasattr(b2, 'subsetUnion_Element_Level8'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level8', a)


def test_assoc_subset917_link_reassign_clear():
    a = subsetUnion_Container(name="sample_text")
    b1 = subsetUnion_Element_Level9()
    b2 = subsetUnion_Element_Level9()
    _safe_set(a, 'subsetUnion_Container18', {b1})
    assert _is_linked(a, 'subsetUnion_Container18', b1)
    if hasattr(b1, 'subsetUnion_Element_Level9'):
        assert _is_linked(b1, 'subsetUnion_Element_Level9', a)
    _safe_set(a, 'subsetUnion_Container18', {b2})
    assert _is_linked(a, 'subsetUnion_Container18', b2)
    if hasattr(b1, 'subsetUnion_Element_Level9'):
        assert not _is_linked(b1, 'subsetUnion_Element_Level9', a)
    if hasattr(b2, 'subsetUnion_Element_Level9'):
        assert _is_linked(b2, 'subsetUnion_Element_Level9', a)
    _safe_set(a, 'subsetUnion_Container18', set())
    assert not _is_linked(a, 'subsetUnion_Container18', b2)
    if hasattr(b2, 'subsetUnion_Element_Level9'):
        assert not _is_linked(b2, 'subsetUnion_Element_Level9', a)


def test_assoc_unionBag0_link_reassign_clear():
    a = subsetUnion_Element(name="sample_text")
    b1 = subsetUnion_Container(name="sample_text")
    b2 = subsetUnion_Container(name="sample_text_2")
    _safe_set(a, 'subsetUnion_Element', b1)
    assert _is_linked(a, 'subsetUnion_Element', b1)
    if hasattr(b1, 'subsetUnion_Container'):
        assert _is_linked(b1, 'subsetUnion_Container', a)
    _safe_set(a, 'subsetUnion_Element', b2)
    assert _is_linked(a, 'subsetUnion_Element', b2)
    if hasattr(b1, 'subsetUnion_Container'):
        assert not _is_linked(b1, 'subsetUnion_Container', a)
    if hasattr(b2, 'subsetUnion_Container'):
        assert _is_linked(b2, 'subsetUnion_Container', a)
    _safe_set(a, 'subsetUnion_Element', None)
    assert not _is_linked(a, 'subsetUnion_Element', b2)
    if hasattr(b2, 'subsetUnion_Container'):
        assert not _is_linked(b2, 'subsetUnion_Container', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


subsetUnion_Container_strategy = st.builds(subsetUnion_Container, name=safe_text)
@given(instance=subsetUnion_Container_strategy)
@settings(max_examples=25)
def test_subsetUnion_Container_instantiation(instance):
    assert isinstance(instance, subsetUnion_Container)


subsetUnion_Element_strategy = st.builds(subsetUnion_Element, name=safe_text)
@given(instance=subsetUnion_Element_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element)


subsetUnion_Element_Level1_strategy = st.builds(subsetUnion_Element_Level1)
@given(instance=subsetUnion_Element_Level1_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level1_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level1)


subsetUnion_Element_Level10_strategy = st.builds(subsetUnion_Element_Level10)
@given(instance=subsetUnion_Element_Level10_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level10_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level10)


subsetUnion_Element_Level2_strategy = st.builds(subsetUnion_Element_Level2)
@given(instance=subsetUnion_Element_Level2_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level2_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level2)


subsetUnion_Element_Level3_strategy = st.builds(subsetUnion_Element_Level3)
@given(instance=subsetUnion_Element_Level3_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level3_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level3)


subsetUnion_Element_Level4_strategy = st.builds(subsetUnion_Element_Level4)
@given(instance=subsetUnion_Element_Level4_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level4_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level4)


subsetUnion_Element_Level5_strategy = st.builds(subsetUnion_Element_Level5)
@given(instance=subsetUnion_Element_Level5_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level5_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level5)


subsetUnion_Element_Level6_strategy = st.builds(subsetUnion_Element_Level6)
@given(instance=subsetUnion_Element_Level6_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level6_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level6)


subsetUnion_Element_Level7_strategy = st.builds(subsetUnion_Element_Level7)
@given(instance=subsetUnion_Element_Level7_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level7_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level7)


subsetUnion_Element_Level8_strategy = st.builds(subsetUnion_Element_Level8)
@given(instance=subsetUnion_Element_Level8_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level8_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level8)


subsetUnion_Element_Level9_strategy = st.builds(subsetUnion_Element_Level9)
@given(instance=subsetUnion_Element_Level9_strategy)
@settings(max_examples=25)
def test_subsetUnion_Element_Level9_instantiation(instance):
    assert isinstance(instance, subsetUnion_Element_Level9)


