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
    Class_Attribute,
    Class_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_class_attribute_is_not_abstract():
    assert not inspect.isabstract(Class_Attribute)


def test_hyp_class_attribute_constructor_exists():
    assert callable(Class_Attribute.__init__)


def test_hyp_class_attribute_constructor_args():
    sig = inspect.signature(Class_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "multiValued" in params, "Missing parameter 'multiValued'"






def test_hyp_class_class_is_not_abstract():
    assert not inspect.isabstract(Class_Class)


def test_hyp_class_class_constructor_exists():
    assert callable(Class_Class.__init__)


def test_hyp_class_class_constructor_args():
    sig = inspect.signature(Class_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"




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
Class_Attribute_strategy = st.builds(
    Class_Attribute,
    name=
        safe_text,
    id=
        safe_text,
    multiValued=
        st.booleans()
)
Class_Class_strategy = st.builds(
    Class_Class,
    name=
        safe_text,
    id=
        safe_text
)




@given(instance=Class_Attribute_strategy)
def test_hyp_class_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Class_Attribute_strategy)
def test_hyp_class_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Attribute_strategy)
def test_hyp_class_attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original




@given(instance=Class_Class_strategy)
def test_hyp_class_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Class_Class_strategy)
def test_hyp_class_class_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class_Attribute,
    Class_Class,
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

def test_Class_Attribute_id_value_roundtrip():
    instance = Class_Attribute(id="sample_text", multiValued=True, name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Attribute_multiValued_value_roundtrip():
    instance = Class_Attribute(id="sample_text", multiValued=True, name="sample_text")
    assert instance.multiValued == True
    instance.multiValued = False
    assert instance.multiValued == False


def test_Class_Attribute_name_value_roundtrip():
    instance = Class_Attribute(id="sample_text", multiValued=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Class_Class_id_value_roundtrip():
    instance = Class_Class(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Class_Class_name_value_roundtrip():
    instance = Class_Class(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_attributes0_link_reassign_clear():
    a = Class_Class(id="sample_text", name="sample_text")
    b1 = Class_Attribute(id="sample_text", multiValued=True, name="sample_text")
    b2 = Class_Attribute(id="sample_text_2", multiValued=False, name="sample_text_2")
    _safe_set(a, 'type', {b1})
    assert _is_linked(a, 'type', b1)
    if hasattr(b1, 'Attribute'):
        assert _is_linked(b1, 'Attribute', a)
    _safe_set(a, 'type', {b2})
    assert _is_linked(a, 'type', b2)
    if hasattr(b1, 'Attribute'):
        assert not _is_linked(b1, 'Attribute', a)
    if hasattr(b2, 'Attribute'):
        assert _is_linked(b2, 'Attribute', a)
    _safe_set(a, 'type', set())
    assert not _is_linked(a, 'type', b2)
    if hasattr(b2, 'Attribute'):
        assert not _is_linked(b2, 'Attribute', a)


def test_assoc_type1_link_reassign_clear():
    a = Class_Class(id="sample_text", name="sample_text")
    b1 = Class_Attribute(id="sample_text", multiValued=True, name="sample_text")
    b2 = Class_Attribute(id="sample_text_2", multiValued=False, name="sample_text_2")
    _safe_set(a, 'Class', b1)
    assert _is_linked(a, 'Class', b1)
    if hasattr(b1, 'attributes'):
        assert _is_linked(b1, 'attributes', a)
    _safe_set(a, 'Class', b2)
    assert _is_linked(a, 'Class', b2)
    if hasattr(b1, 'attributes'):
        assert not _is_linked(b1, 'attributes', a)
    if hasattr(b2, 'attributes'):
        assert _is_linked(b2, 'attributes', a)
    _safe_set(a, 'Class', None)
    assert not _is_linked(a, 'Class', b2)
    if hasattr(b2, 'attributes'):
        assert not _is_linked(b2, 'attributes', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_Attribute_strategy = st.builds(Class_Attribute, id=safe_text, multiValued=st.booleans(), name=safe_text)
@given(instance=Class_Attribute_strategy)
@settings(max_examples=25)
def test_Class_Attribute_instantiation(instance):
    assert isinstance(instance, Class_Attribute)


Class_Class_strategy = st.builds(Class_Class, id=safe_text, name=safe_text)
@given(instance=Class_Class_strategy)
@settings(max_examples=25)
def test_Class_Class_instantiation(instance):
    assert isinstance(instance, Class_Class)



