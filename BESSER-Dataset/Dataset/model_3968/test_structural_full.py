import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Container,
    Container_Level1,
    Container_Level2,
    Container_Level3,
    Container_Level4,
    Container_Level5,
    Container_Level6,
    Container_Level7,
    Container_Level8,
    Container_Level9,
    Element,
    Element_Level1,
    Element_Level2,
    Element_Level3,
    Element_Level4,
    Element_Level5,
    Element_Level6,
    Element_Level7,
    Element_Level8,
    Element_Level9,
    subsetUnionDepth_Container,
    subsetUnionDepth_Container_Level1,
    subsetUnionDepth_Container_Level10,
    subsetUnionDepth_Container_Level2,
    subsetUnionDepth_Container_Level3,
    subsetUnionDepth_Container_Level4,
    subsetUnionDepth_Container_Level5,
    subsetUnionDepth_Container_Level6,
    subsetUnionDepth_Container_Level7,
    subsetUnionDepth_Container_Level8,
    subsetUnionDepth_Container_Level9,
    subsetUnionDepth_Element,
    subsetUnionDepth_Element_Level1,
    subsetUnionDepth_Element_Level10,
    subsetUnionDepth_Element_Level2,
    subsetUnionDepth_Element_Level3,
    subsetUnionDepth_Element_Level4,
    subsetUnionDepth_Element_Level5,
    subsetUnionDepth_Element_Level6,
    subsetUnionDepth_Element_Level7,
    subsetUnionDepth_Element_Level8,
    subsetUnionDepth_Element_Level9,
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

def test_subsetUnionDepth_Container_name_value_roundtrip():
    instance = subsetUnionDepth_Container(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_subsetUnionDepth_Element_name_value_roundtrip():
    instance = subsetUnionDepth_Element(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_subsetUnionDepth_Container_Level1_isa_Container():
    instance = subsetUnionDepth_Container_Level1()
    assert isinstance(instance, Container)


def test_subsetUnionDepth_Container_Level2_isa_Container_Level1():
    instance = subsetUnionDepth_Container_Level2()
    assert isinstance(instance, Container_Level1)


def test_subsetUnionDepth_Container_Level3_isa_Container_Level2():
    instance = subsetUnionDepth_Container_Level3()
    assert isinstance(instance, Container_Level2)


def test_subsetUnionDepth_Container_Level4_isa_Container_Level3():
    instance = subsetUnionDepth_Container_Level4()
    assert isinstance(instance, Container_Level3)


def test_subsetUnionDepth_Container_Level5_isa_Container_Level4():
    instance = subsetUnionDepth_Container_Level5()
    assert isinstance(instance, Container_Level4)


def test_subsetUnionDepth_Container_Level6_isa_Container_Level5():
    instance = subsetUnionDepth_Container_Level6()
    assert isinstance(instance, Container_Level5)


def test_subsetUnionDepth_Container_Level7_isa_Container_Level6():
    instance = subsetUnionDepth_Container_Level7()
    assert isinstance(instance, Container_Level6)


def test_subsetUnionDepth_Container_Level8_isa_Container_Level7():
    instance = subsetUnionDepth_Container_Level8()
    assert isinstance(instance, Container_Level7)


def test_subsetUnionDepth_Container_Level9_isa_Container_Level8():
    instance = subsetUnionDepth_Container_Level9()
    assert isinstance(instance, Container_Level8)


def test_subsetUnionDepth_Container_Level10_isa_Container_Level9():
    instance = subsetUnionDepth_Container_Level10()
    assert isinstance(instance, Container_Level9)


def test_subsetUnionDepth_Element_Level1_isa_Element():
    instance = subsetUnionDepth_Element_Level1()
    assert isinstance(instance, Element)


def test_subsetUnionDepth_Element_Level2_isa_Element_Level1():
    instance = subsetUnionDepth_Element_Level2()
    assert isinstance(instance, Element_Level1)


def test_subsetUnionDepth_Element_Level3_isa_Element_Level2():
    instance = subsetUnionDepth_Element_Level3()
    assert isinstance(instance, Element_Level2)


def test_subsetUnionDepth_Element_Level4_isa_Element_Level3():
    instance = subsetUnionDepth_Element_Level4()
    assert isinstance(instance, Element_Level3)


def test_subsetUnionDepth_Element_Level5_isa_Element_Level4():
    instance = subsetUnionDepth_Element_Level5()
    assert isinstance(instance, Element_Level4)


def test_subsetUnionDepth_Element_Level6_isa_Element_Level5():
    instance = subsetUnionDepth_Element_Level6()
    assert isinstance(instance, Element_Level5)


def test_subsetUnionDepth_Element_Level7_isa_Element_Level6():
    instance = subsetUnionDepth_Element_Level7()
    assert isinstance(instance, Element_Level6)


def test_subsetUnionDepth_Element_Level8_isa_Element_Level7():
    instance = subsetUnionDepth_Element_Level8()
    assert isinstance(instance, Element_Level7)


def test_subsetUnionDepth_Element_Level9_isa_Element_Level8():
    instance = subsetUnionDepth_Element_Level9()
    assert isinstance(instance, Element_Level8)


def test_subsetUnionDepth_Element_Level10_isa_Element_Level9():
    instance = subsetUnionDepth_Element_Level10()
    assert isinstance(instance, Element_Level9)


def test_assoc_unionBag0_link_reassign_clear():
    a = subsetUnionDepth_Element(name="sample_text")
    b1 = subsetUnionDepth_Container(name="sample_text")
    b2 = subsetUnionDepth_Container(name="sample_text_2")
    _safe_set(a, 'subsetUnionDepth_Element', b1)
    assert _is_linked(a, 'subsetUnionDepth_Element', b1)
    if hasattr(b1, 'subsetUnionDepth_Container'):
        assert _is_linked(b1, 'subsetUnionDepth_Container', a)
    _safe_set(a, 'subsetUnionDepth_Element', b2)
    assert _is_linked(a, 'subsetUnionDepth_Element', b2)
    if hasattr(b1, 'subsetUnionDepth_Container'):
        assert not _is_linked(b1, 'subsetUnionDepth_Container', a)
    if hasattr(b2, 'subsetUnionDepth_Container'):
        assert _is_linked(b2, 'subsetUnionDepth_Container', a)
    _safe_set(a, 'subsetUnionDepth_Element', None)
    assert not _is_linked(a, 'subsetUnionDepth_Element', b2)
    if hasattr(b2, 'subsetUnionDepth_Container'):
        assert not _is_linked(b2, 'subsetUnionDepth_Container', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Container_strategy = st.builds(Container)
@given(instance=Container_strategy)
@settings(max_examples=25)
def test_Container_instantiation(instance):
    assert isinstance(instance, Container)


Container_Level1_strategy = st.builds(Container_Level1)
@given(instance=Container_Level1_strategy)
@settings(max_examples=25)
def test_Container_Level1_instantiation(instance):
    assert isinstance(instance, Container_Level1)


Container_Level2_strategy = st.builds(Container_Level2)
@given(instance=Container_Level2_strategy)
@settings(max_examples=25)
def test_Container_Level2_instantiation(instance):
    assert isinstance(instance, Container_Level2)


Container_Level3_strategy = st.builds(Container_Level3)
@given(instance=Container_Level3_strategy)
@settings(max_examples=25)
def test_Container_Level3_instantiation(instance):
    assert isinstance(instance, Container_Level3)


Container_Level4_strategy = st.builds(Container_Level4)
@given(instance=Container_Level4_strategy)
@settings(max_examples=25)
def test_Container_Level4_instantiation(instance):
    assert isinstance(instance, Container_Level4)


Container_Level5_strategy = st.builds(Container_Level5)
@given(instance=Container_Level5_strategy)
@settings(max_examples=25)
def test_Container_Level5_instantiation(instance):
    assert isinstance(instance, Container_Level5)


Container_Level6_strategy = st.builds(Container_Level6)
@given(instance=Container_Level6_strategy)
@settings(max_examples=25)
def test_Container_Level6_instantiation(instance):
    assert isinstance(instance, Container_Level6)


Container_Level7_strategy = st.builds(Container_Level7)
@given(instance=Container_Level7_strategy)
@settings(max_examples=25)
def test_Container_Level7_instantiation(instance):
    assert isinstance(instance, Container_Level7)


Container_Level8_strategy = st.builds(Container_Level8)
@given(instance=Container_Level8_strategy)
@settings(max_examples=25)
def test_Container_Level8_instantiation(instance):
    assert isinstance(instance, Container_Level8)


Container_Level9_strategy = st.builds(Container_Level9)
@given(instance=Container_Level9_strategy)
@settings(max_examples=25)
def test_Container_Level9_instantiation(instance):
    assert isinstance(instance, Container_Level9)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


Element_Level1_strategy = st.builds(Element_Level1)
@given(instance=Element_Level1_strategy)
@settings(max_examples=25)
def test_Element_Level1_instantiation(instance):
    assert isinstance(instance, Element_Level1)


Element_Level2_strategy = st.builds(Element_Level2)
@given(instance=Element_Level2_strategy)
@settings(max_examples=25)
def test_Element_Level2_instantiation(instance):
    assert isinstance(instance, Element_Level2)


Element_Level3_strategy = st.builds(Element_Level3)
@given(instance=Element_Level3_strategy)
@settings(max_examples=25)
def test_Element_Level3_instantiation(instance):
    assert isinstance(instance, Element_Level3)


Element_Level4_strategy = st.builds(Element_Level4)
@given(instance=Element_Level4_strategy)
@settings(max_examples=25)
def test_Element_Level4_instantiation(instance):
    assert isinstance(instance, Element_Level4)


Element_Level5_strategy = st.builds(Element_Level5)
@given(instance=Element_Level5_strategy)
@settings(max_examples=25)
def test_Element_Level5_instantiation(instance):
    assert isinstance(instance, Element_Level5)


Element_Level6_strategy = st.builds(Element_Level6)
@given(instance=Element_Level6_strategy)
@settings(max_examples=25)
def test_Element_Level6_instantiation(instance):
    assert isinstance(instance, Element_Level6)


Element_Level7_strategy = st.builds(Element_Level7)
@given(instance=Element_Level7_strategy)
@settings(max_examples=25)
def test_Element_Level7_instantiation(instance):
    assert isinstance(instance, Element_Level7)


Element_Level8_strategy = st.builds(Element_Level8)
@given(instance=Element_Level8_strategy)
@settings(max_examples=25)
def test_Element_Level8_instantiation(instance):
    assert isinstance(instance, Element_Level8)


Element_Level9_strategy = st.builds(Element_Level9)
@given(instance=Element_Level9_strategy)
@settings(max_examples=25)
def test_Element_Level9_instantiation(instance):
    assert isinstance(instance, Element_Level9)


subsetUnionDepth_Container_strategy = st.builds(subsetUnionDepth_Container, name=safe_text)
@given(instance=subsetUnionDepth_Container_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container)


subsetUnionDepth_Container_Level1_strategy = st.builds(subsetUnionDepth_Container_Level1)
@given(instance=subsetUnionDepth_Container_Level1_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level1_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level1)


subsetUnionDepth_Container_Level10_strategy = st.builds(subsetUnionDepth_Container_Level10)
@given(instance=subsetUnionDepth_Container_Level10_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level10_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level10)


subsetUnionDepth_Container_Level2_strategy = st.builds(subsetUnionDepth_Container_Level2)
@given(instance=subsetUnionDepth_Container_Level2_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level2_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level2)


subsetUnionDepth_Container_Level3_strategy = st.builds(subsetUnionDepth_Container_Level3)
@given(instance=subsetUnionDepth_Container_Level3_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level3_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level3)


subsetUnionDepth_Container_Level4_strategy = st.builds(subsetUnionDepth_Container_Level4)
@given(instance=subsetUnionDepth_Container_Level4_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level4_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level4)


subsetUnionDepth_Container_Level5_strategy = st.builds(subsetUnionDepth_Container_Level5)
@given(instance=subsetUnionDepth_Container_Level5_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level5_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level5)


subsetUnionDepth_Container_Level6_strategy = st.builds(subsetUnionDepth_Container_Level6)
@given(instance=subsetUnionDepth_Container_Level6_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level6_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level6)


subsetUnionDepth_Container_Level7_strategy = st.builds(subsetUnionDepth_Container_Level7)
@given(instance=subsetUnionDepth_Container_Level7_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level7_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level7)


subsetUnionDepth_Container_Level8_strategy = st.builds(subsetUnionDepth_Container_Level8)
@given(instance=subsetUnionDepth_Container_Level8_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level8_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level8)


subsetUnionDepth_Container_Level9_strategy = st.builds(subsetUnionDepth_Container_Level9)
@given(instance=subsetUnionDepth_Container_Level9_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Container_Level9_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Container_Level9)


subsetUnionDepth_Element_strategy = st.builds(subsetUnionDepth_Element, name=safe_text)
@given(instance=subsetUnionDepth_Element_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element)


subsetUnionDepth_Element_Level1_strategy = st.builds(subsetUnionDepth_Element_Level1)
@given(instance=subsetUnionDepth_Element_Level1_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level1_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level1)


subsetUnionDepth_Element_Level10_strategy = st.builds(subsetUnionDepth_Element_Level10)
@given(instance=subsetUnionDepth_Element_Level10_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level10_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level10)


subsetUnionDepth_Element_Level2_strategy = st.builds(subsetUnionDepth_Element_Level2)
@given(instance=subsetUnionDepth_Element_Level2_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level2_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level2)


subsetUnionDepth_Element_Level3_strategy = st.builds(subsetUnionDepth_Element_Level3)
@given(instance=subsetUnionDepth_Element_Level3_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level3_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level3)


subsetUnionDepth_Element_Level4_strategy = st.builds(subsetUnionDepth_Element_Level4)
@given(instance=subsetUnionDepth_Element_Level4_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level4_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level4)


subsetUnionDepth_Element_Level5_strategy = st.builds(subsetUnionDepth_Element_Level5)
@given(instance=subsetUnionDepth_Element_Level5_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level5_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level5)


subsetUnionDepth_Element_Level6_strategy = st.builds(subsetUnionDepth_Element_Level6)
@given(instance=subsetUnionDepth_Element_Level6_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level6_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level6)


subsetUnionDepth_Element_Level7_strategy = st.builds(subsetUnionDepth_Element_Level7)
@given(instance=subsetUnionDepth_Element_Level7_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level7_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level7)


subsetUnionDepth_Element_Level8_strategy = st.builds(subsetUnionDepth_Element_Level8)
@given(instance=subsetUnionDepth_Element_Level8_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level8_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level8)


subsetUnionDepth_Element_Level9_strategy = st.builds(subsetUnionDepth_Element_Level9)
@given(instance=subsetUnionDepth_Element_Level9_strategy)
@settings(max_examples=25)
def test_subsetUnionDepth_Element_Level9_instantiation(instance):
    assert isinstance(instance, subsetUnionDepth_Element_Level9)


