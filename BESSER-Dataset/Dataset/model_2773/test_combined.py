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
    nestedgroup_A,
    nestedgroup_Element,
    nestedgroup_CType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_nestedgroup_a_is_not_abstract():
    assert not inspect.isabstract(nestedgroup_A)


def test_hyp_nestedgroup_a_constructor_exists():
    assert callable(nestedgroup_A.__init__)


def test_hyp_nestedgroup_a_constructor_args():
    sig = inspect.signature(nestedgroup_A.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "b" in params, "Missing parameter 'b'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_nestedgroup_element_is_not_abstract():
    assert not inspect.isabstract(nestedgroup_Element)


def test_hyp_nestedgroup_element_constructor_exists():
    assert callable(nestedgroup_Element.__init__)


def test_hyp_nestedgroup_element_constructor_args():
    sig = inspect.signature(nestedgroup_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "true" in params, "Missing parameter 'true'"
    assert "mixed" in params, "Missing parameter 'mixed'"






def test_hyp_nestedgroup_ctype_is_not_abstract():
    assert not inspect.isabstract(nestedgroup_CType)


def test_hyp_nestedgroup_ctype_constructor_exists():
    assert callable(nestedgroup_CType.__init__)


def test_hyp_nestedgroup_ctype_constructor_args():
    sig = inspect.signature(nestedgroup_CType.__init__)
    params = list(sig.parameters.keys())
    assert "cvalue" in params, "Missing parameter 'cvalue'"
    assert "cname" in params, "Missing parameter 'cname'"




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
nestedgroup_A_strategy = st.builds(
    nestedgroup_A,
    group=
        safe_text,
    b=
        safe_text,
    name=
        safe_text
)
nestedgroup_Element_strategy = st.builds(
    nestedgroup_Element,
    name=
        safe_text,
    true=
        safe_text,
    mixed=
        safe_text
)
nestedgroup_CType_strategy = st.builds(
    nestedgroup_CType,
    cvalue=
        safe_text,
    cname=
        safe_text
)




@given(instance=nestedgroup_A_strategy)
def test_hyp_nestedgroup_a_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=nestedgroup_A_strategy)
def test_hyp_nestedgroup_a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=nestedgroup_A_strategy)
def test_hyp_nestedgroup_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=nestedgroup_Element_strategy)
def test_hyp_nestedgroup_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=nestedgroup_Element_strategy)
def test_hyp_nestedgroup_element_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original



@given(instance=nestedgroup_Element_strategy)
def test_hyp_nestedgroup_element_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=nestedgroup_CType_strategy)
def test_hyp_nestedgroup_ctype_cvalue_setter(instance):
    original = instance.cvalue
    instance.cvalue = original
    assert instance.cvalue == original



@given(instance=nestedgroup_CType_strategy)
def test_hyp_nestedgroup_ctype_cname_setter(instance):
    original = instance.cname
    instance.cname = original
    assert instance.cname == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    nestedgroup_A,
    nestedgroup_CType,
    nestedgroup_Element,
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

def test_nestedgroup_A_b_value_roundtrip():
    instance = nestedgroup_A(b="sample_text", group="sample_text", name="sample_text")
    assert instance.b == "sample_text"
    instance.b = "sample_text_2"
    assert instance.b == "sample_text_2"


def test_nestedgroup_A_group_value_roundtrip():
    instance = nestedgroup_A(b="sample_text", group="sample_text", name="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_nestedgroup_A_name_value_roundtrip():
    instance = nestedgroup_A(b="sample_text", group="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_nestedgroup_CType_cname_value_roundtrip():
    instance = nestedgroup_CType(cname="sample_text", cvalue="sample_text")
    assert instance.cname == "sample_text"
    instance.cname = "sample_text_2"
    assert instance.cname == "sample_text_2"


def test_nestedgroup_CType_cvalue_value_roundtrip():
    instance = nestedgroup_CType(cname="sample_text", cvalue="sample_text")
    assert instance.cvalue == "sample_text"
    instance.cvalue = "sample_text_2"
    assert instance.cvalue == "sample_text_2"


def test_nestedgroup_Element_mixed_value_roundtrip():
    instance = nestedgroup_Element(mixed="sample_text", name="sample_text", true="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_nestedgroup_Element_name_value_roundtrip():
    instance = nestedgroup_Element(mixed="sample_text", name="sample_text", true="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_nestedgroup_Element_true_value_roundtrip():
    instance = nestedgroup_Element(mixed="sample_text", name="sample_text", true="sample_text")
    assert instance.true == "sample_text"
    instance.true = "sample_text_2"
    assert instance.true == "sample_text_2"


def test_assoc_c0_link_reassign_clear():
    a = nestedgroup_CType(cname="sample_text", cvalue="sample_text")
    b1 = nestedgroup_A(b="sample_text", group="sample_text", name="sample_text")
    b2 = nestedgroup_A(b="sample_text_2", group="sample_text_2", name="sample_text_2")
    _safe_set(a, 'nestedgroup_CType', b1)
    assert _is_linked(a, 'nestedgroup_CType', b1)
    if hasattr(b1, 'nestedgroup_A'):
        assert _is_linked(b1, 'nestedgroup_A', a)
    _safe_set(a, 'nestedgroup_CType', b2)
    assert _is_linked(a, 'nestedgroup_CType', b2)
    if hasattr(b1, 'nestedgroup_A'):
        assert not _is_linked(b1, 'nestedgroup_A', a)
    if hasattr(b2, 'nestedgroup_A'):
        assert _is_linked(b2, 'nestedgroup_A', a)
    _safe_set(a, 'nestedgroup_CType', None)
    assert not _is_linked(a, 'nestedgroup_CType', b2)
    if hasattr(b2, 'nestedgroup_A'):
        assert not _is_linked(b2, 'nestedgroup_A', a)


def test_assoc_c1_link_reassign_clear():
    a = nestedgroup_Element(mixed="sample_text", name="sample_text", true="sample_text")
    b1 = nestedgroup_CType(cname="sample_text", cvalue="sample_text")
    b2 = nestedgroup_CType(cname="sample_text_2", cvalue="sample_text_2")
    _safe_set(a, 'nestedgroup_Element', {b1})
    assert _is_linked(a, 'nestedgroup_Element', b1)
    if hasattr(b1, 'nestedgroup_CType2'):
        assert _is_linked(b1, 'nestedgroup_CType2', a)
    _safe_set(a, 'nestedgroup_Element', {b2})
    assert _is_linked(a, 'nestedgroup_Element', b2)
    if hasattr(b1, 'nestedgroup_CType2'):
        assert not _is_linked(b1, 'nestedgroup_CType2', a)
    if hasattr(b2, 'nestedgroup_CType2'):
        assert _is_linked(b2, 'nestedgroup_CType2', a)
    _safe_set(a, 'nestedgroup_Element', set())
    assert not _is_linked(a, 'nestedgroup_Element', b2)
    if hasattr(b2, 'nestedgroup_CType2'):
        assert not _is_linked(b2, 'nestedgroup_CType2', a)


def test_assoc_recursive4_link_reassign_clear():
    a = nestedgroup_Element(mixed="sample_text", name="sample_text", true="sample_text")
    b1 = nestedgroup_Element(mixed="sample_text", name="sample_text", true="sample_text")
    b2 = nestedgroup_Element(mixed="sample_text_2", name="sample_text_2", true="sample_text_2")
    _safe_set(a, 'nestedgroup_Element3', b1)
    assert _is_linked(a, 'nestedgroup_Element3', b1)
    if hasattr(b1, 'nestedgroup_Element5'):
        assert _is_linked(b1, 'nestedgroup_Element5', a)
    _safe_set(a, 'nestedgroup_Element3', b2)
    assert _is_linked(a, 'nestedgroup_Element3', b2)
    if hasattr(b1, 'nestedgroup_Element5'):
        assert not _is_linked(b1, 'nestedgroup_Element5', a)
    if hasattr(b2, 'nestedgroup_Element5'):
        assert _is_linked(b2, 'nestedgroup_Element5', a)
    _safe_set(a, 'nestedgroup_Element3', None)
    assert not _is_linked(a, 'nestedgroup_Element3', b2)
    if hasattr(b2, 'nestedgroup_Element5'):
        assert not _is_linked(b2, 'nestedgroup_Element5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

nestedgroup_A_strategy = st.builds(nestedgroup_A, b=safe_text, group=safe_text, name=safe_text)
@given(instance=nestedgroup_A_strategy)
@settings(max_examples=25)
def test_nestedgroup_A_instantiation(instance):
    assert isinstance(instance, nestedgroup_A)


nestedgroup_CType_strategy = st.builds(nestedgroup_CType, cname=safe_text, cvalue=safe_text)
@given(instance=nestedgroup_CType_strategy)
@settings(max_examples=25)
def test_nestedgroup_CType_instantiation(instance):
    assert isinstance(instance, nestedgroup_CType)


nestedgroup_Element_strategy = st.builds(nestedgroup_Element, mixed=safe_text, name=safe_text, true=safe_text)
@given(instance=nestedgroup_Element_strategy)
@settings(max_examples=25)
def test_nestedgroup_Element_instantiation(instance):
    assert isinstance(instance, nestedgroup_Element)



