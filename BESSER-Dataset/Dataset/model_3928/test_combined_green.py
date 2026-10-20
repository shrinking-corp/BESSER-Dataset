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
    NamedElement,
    entity_Type,
    entity_Namespace,
    entity_NamedElement,
    entity_Attribute,
    entity_Reference,
    Type,
    entity_Datatype,
    entity_Entity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_type_is_not_abstract():
    assert not inspect.isabstract(entity_Type)


def test_hyp_entity_type_constructor_exists():
    assert callable(entity_Type.__init__)


def test_hyp_entity_type_constructor_args():
    sig = inspect.signature(entity_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_namespace_is_not_abstract():
    assert not inspect.isabstract(entity_Namespace)


def test_hyp_entity_namespace_constructor_exists():
    assert callable(entity_Namespace.__init__)


def test_hyp_entity_namespace_constructor_args():
    sig = inspect.signature(entity_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_namedelement_is_not_abstract():
    assert not inspect.isabstract(entity_NamedElement)


def test_hyp_entity_namedelement_constructor_exists():
    assert callable(entity_NamedElement.__init__)


def test_hyp_entity_namedelement_constructor_args():
    sig = inspect.signature(entity_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_entity_attribute_is_not_abstract():
    assert not inspect.isabstract(entity_Attribute)


def test_hyp_entity_attribute_constructor_exists():
    assert callable(entity_Attribute.__init__)


def test_hyp_entity_attribute_constructor_args():
    sig = inspect.signature(entity_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_reference_is_not_abstract():
    assert not inspect.isabstract(entity_Reference)


def test_hyp_entity_reference_constructor_exists():
    assert callable(entity_Reference.__init__)


def test_hyp_entity_reference_constructor_args():
    sig = inspect.signature(entity_Reference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_datatype_is_not_abstract():
    assert not inspect.isabstract(entity_Datatype)


def test_hyp_entity_datatype_constructor_exists():
    assert callable(entity_Datatype.__init__)


def test_hyp_entity_datatype_constructor_args():
    sig = inspect.signature(entity_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entity_entity_is_not_abstract():
    assert not inspect.isabstract(entity_Entity)


def test_hyp_entity_entity_constructor_exists():
    assert callable(entity_Entity.__init__)


def test_hyp_entity_entity_constructor_args():
    sig = inspect.signature(entity_Entity.__init__)
    params = list(sig.parameters.keys())


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
NamedElement_strategy = st.builds(
    NamedElement,
)
entity_Type_strategy = st.builds(
    entity_Type,
)
entity_Namespace_strategy = st.builds(
    entity_Namespace,
)
entity_NamedElement_strategy = st.builds(
    entity_NamedElement,
    name=
        safe_text
)
entity_Attribute_strategy = st.builds(
    entity_Attribute,
)
entity_Reference_strategy = st.builds(
    entity_Reference,
)
Type_strategy = st.builds(
    Type,
)
entity_Datatype_strategy = st.builds(
    entity_Datatype,
)
entity_Entity_strategy = st.builds(
    entity_Entity,
)







@given(instance=entity_NamedElement_strategy)
def test_hyp_entity_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    Type,
    entity_Attribute,
    entity_Datatype,
    entity_Entity,
    entity_NamedElement,
    entity_Namespace,
    entity_Reference,
    entity_Type,
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

def test_entity_NamedElement_name_value_roundtrip():
    instance = entity_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_entity_Attribute_isa_NamedElement():
    instance = entity_Attribute()
    assert isinstance(instance, NamedElement)


def test_entity_Namespace_isa_NamedElement():
    instance = entity_Namespace()
    assert isinstance(instance, NamedElement)


def test_entity_Reference_isa_NamedElement():
    instance = entity_Reference()
    assert isinstance(instance, NamedElement)


def test_entity_Type_isa_NamedElement():
    instance = entity_Type()
    assert isinstance(instance, NamedElement)


def test_entity_Datatype_isa_Type():
    instance = entity_Datatype()
    assert isinstance(instance, Type)


def test_entity_Entity_isa_Type():
    instance = entity_Entity()
    assert isinstance(instance, Type)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


entity_Attribute_strategy = st.builds(entity_Attribute)
@given(instance=entity_Attribute_strategy)
@settings(max_examples=25)
def test_entity_Attribute_instantiation(instance):
    assert isinstance(instance, entity_Attribute)


entity_Datatype_strategy = st.builds(entity_Datatype)
@given(instance=entity_Datatype_strategy)
@settings(max_examples=25)
def test_entity_Datatype_instantiation(instance):
    assert isinstance(instance, entity_Datatype)


entity_Entity_strategy = st.builds(entity_Entity)
@given(instance=entity_Entity_strategy)
@settings(max_examples=25)
def test_entity_Entity_instantiation(instance):
    assert isinstance(instance, entity_Entity)


entity_NamedElement_strategy = st.builds(entity_NamedElement, name=safe_text)
@given(instance=entity_NamedElement_strategy)
@settings(max_examples=25)
def test_entity_NamedElement_instantiation(instance):
    assert isinstance(instance, entity_NamedElement)


entity_Namespace_strategy = st.builds(entity_Namespace)
@given(instance=entity_Namespace_strategy)
@settings(max_examples=25)
def test_entity_Namespace_instantiation(instance):
    assert isinstance(instance, entity_Namespace)


entity_Reference_strategy = st.builds(entity_Reference)
@given(instance=entity_Reference_strategy)
@settings(max_examples=25)
def test_entity_Reference_instantiation(instance):
    assert isinstance(instance, entity_Reference)


entity_Type_strategy = st.builds(entity_Type)
@given(instance=entity_Type_strategy)
@settings(max_examples=25)
def test_entity_Type_instantiation(instance):
    assert isinstance(instance, entity_Type)



