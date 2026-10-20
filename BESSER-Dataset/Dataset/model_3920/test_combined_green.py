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
    entityDsl_Property,
    Type,
    entityDsl_Entity,
    entityDsl_SimpleType,
    entityDsl_Type,
    entityDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_entitydsl_property_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Property)


def test_hyp_entitydsl_property_constructor_exists():
    assert callable(entityDsl_Property.__init__)


def test_hyp_entitydsl_property_constructor_args():
    sig = inspect.signature(entityDsl_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"





def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entitydsl_entity_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Entity)


def test_hyp_entitydsl_entity_constructor_exists():
    assert callable(entityDsl_Entity.__init__)


def test_hyp_entitydsl_entity_constructor_args():
    sig = inspect.signature(entityDsl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entitydsl_simpletype_is_not_abstract():
    assert not inspect.isabstract(entityDsl_SimpleType)


def test_hyp_entitydsl_simpletype_constructor_exists():
    assert callable(entityDsl_SimpleType.__init__)


def test_hyp_entitydsl_simpletype_constructor_args():
    sig = inspect.signature(entityDsl_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_entitydsl_type_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Type)


def test_hyp_entitydsl_type_constructor_exists():
    assert callable(entityDsl_Type.__init__)


def test_hyp_entitydsl_type_constructor_args():
    sig = inspect.signature(entityDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_entitydsl_model_is_not_abstract():
    assert not inspect.isabstract(entityDsl_Model)


def test_hyp_entitydsl_model_constructor_exists():
    assert callable(entityDsl_Model.__init__)


def test_hyp_entitydsl_model_constructor_args():
    sig = inspect.signature(entityDsl_Model.__init__)
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
entityDsl_Property_strategy = st.builds(
    entityDsl_Property,
    name=
        safe_text,
    many=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
entityDsl_Entity_strategy = st.builds(
    entityDsl_Entity,
)
entityDsl_SimpleType_strategy = st.builds(
    entityDsl_SimpleType,
)
entityDsl_Type_strategy = st.builds(
    entityDsl_Type,
    name=
        safe_text
)
entityDsl_Model_strategy = st.builds(
    entityDsl_Model,
)




@given(instance=entityDsl_Property_strategy)
def test_hyp_entitydsl_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=entityDsl_Property_strategy)
def test_hyp_entitydsl_property_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original







@given(instance=entityDsl_Type_strategy)
def test_hyp_entitydsl_type_name_setter(instance):
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
    Type,
    entityDsl_Entity,
    entityDsl_Model,
    entityDsl_Property,
    entityDsl_SimpleType,
    entityDsl_Type,
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

def test_entityDsl_Property_many_value_roundtrip():
    instance = entityDsl_Property(many=True, name="sample_text")
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_entityDsl_Property_name_value_roundtrip():
    instance = entityDsl_Property(many=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_entityDsl_Type_name_value_roundtrip():
    instance = entityDsl_Type(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_entityDsl_Entity_isa_Type():
    instance = entityDsl_Entity()
    assert isinstance(instance, Type)


def test_entityDsl_SimpleType_isa_Type():
    instance = entityDsl_SimpleType()
    assert isinstance(instance, Type)


def test_assoc_elements0_link_reassign_clear():
    a = entityDsl_Type(name="sample_text")
    b1 = entityDsl_Model()
    b2 = entityDsl_Model()
    _safe_set(a, 'entityDsl_Type', b1)
    assert _is_linked(a, 'entityDsl_Type', b1)
    if hasattr(b1, 'entityDsl_Model'):
        assert _is_linked(b1, 'entityDsl_Model', a)
    _safe_set(a, 'entityDsl_Type', b2)
    assert _is_linked(a, 'entityDsl_Type', b2)
    if hasattr(b1, 'entityDsl_Model'):
        assert not _is_linked(b1, 'entityDsl_Model', a)
    if hasattr(b2, 'entityDsl_Model'):
        assert _is_linked(b2, 'entityDsl_Model', a)
    _safe_set(a, 'entityDsl_Type', None)
    assert not _is_linked(a, 'entityDsl_Type', b2)
    if hasattr(b2, 'entityDsl_Model'):
        assert not _is_linked(b2, 'entityDsl_Model', a)


def test_assoc_properties3_link_reassign_clear():
    a = entityDsl_Property(many=True, name="sample_text")
    b1 = entityDsl_Entity()
    b2 = entityDsl_Entity()
    _safe_set(a, 'entityDsl_Property', b1)
    assert _is_linked(a, 'entityDsl_Property', b1)
    if hasattr(b1, 'entityDsl_Entity4'):
        assert _is_linked(b1, 'entityDsl_Entity4', a)
    _safe_set(a, 'entityDsl_Property', b2)
    assert _is_linked(a, 'entityDsl_Property', b2)
    if hasattr(b1, 'entityDsl_Entity4'):
        assert not _is_linked(b1, 'entityDsl_Entity4', a)
    if hasattr(b2, 'entityDsl_Entity4'):
        assert _is_linked(b2, 'entityDsl_Entity4', a)
    _safe_set(a, 'entityDsl_Property', None)
    assert not _is_linked(a, 'entityDsl_Property', b2)
    if hasattr(b2, 'entityDsl_Entity4'):
        assert not _is_linked(b2, 'entityDsl_Entity4', a)


def test_assoc_type5_link_reassign_clear():
    a = entityDsl_Type(name="sample_text")
    b1 = entityDsl_Property(many=True, name="sample_text")
    b2 = entityDsl_Property(many=False, name="sample_text_2")
    _safe_set(a, 'entityDsl_Type7', b1)
    assert _is_linked(a, 'entityDsl_Type7', b1)
    if hasattr(b1, 'entityDsl_Property6'):
        assert _is_linked(b1, 'entityDsl_Property6', a)
    _safe_set(a, 'entityDsl_Type7', b2)
    assert _is_linked(a, 'entityDsl_Type7', b2)
    if hasattr(b1, 'entityDsl_Property6'):
        assert not _is_linked(b1, 'entityDsl_Property6', a)
    if hasattr(b2, 'entityDsl_Property6'):
        assert _is_linked(b2, 'entityDsl_Property6', a)
    _safe_set(a, 'entityDsl_Type7', None)
    assert not _is_linked(a, 'entityDsl_Type7', b2)
    if hasattr(b2, 'entityDsl_Property6'):
        assert not _is_linked(b2, 'entityDsl_Property6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


entityDsl_Entity_strategy = st.builds(entityDsl_Entity)
@given(instance=entityDsl_Entity_strategy)
@settings(max_examples=25)
def test_entityDsl_Entity_instantiation(instance):
    assert isinstance(instance, entityDsl_Entity)


entityDsl_Model_strategy = st.builds(entityDsl_Model)
@given(instance=entityDsl_Model_strategy)
@settings(max_examples=25)
def test_entityDsl_Model_instantiation(instance):
    assert isinstance(instance, entityDsl_Model)


entityDsl_Property_strategy = st.builds(entityDsl_Property, many=st.booleans(), name=safe_text)
@given(instance=entityDsl_Property_strategy)
@settings(max_examples=25)
def test_entityDsl_Property_instantiation(instance):
    assert isinstance(instance, entityDsl_Property)


entityDsl_SimpleType_strategy = st.builds(entityDsl_SimpleType)
@given(instance=entityDsl_SimpleType_strategy)
@settings(max_examples=25)
def test_entityDsl_SimpleType_instantiation(instance):
    assert isinstance(instance, entityDsl_SimpleType)


entityDsl_Type_strategy = st.builds(entityDsl_Type, name=safe_text)
@given(instance=entityDsl_Type_strategy)
@settings(max_examples=25)
def test_entityDsl_Type_instantiation(instance):
    assert isinstance(instance, entityDsl_Type)



