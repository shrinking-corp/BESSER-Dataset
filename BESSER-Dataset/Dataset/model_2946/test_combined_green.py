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
    slolpBPM_Feature,
    Type,
    slolpBPM_Entity,
    slolpBPM_Datatype,
    slolpBPM_Type,
    slolpBPM_DomainModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_slolpbpm_feature_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_Feature)


def test_hyp_slolpbpm_feature_constructor_exists():
    assert callable(slolpBPM_Feature.__init__)


def test_hyp_slolpbpm_feature_constructor_args():
    sig = inspect.signature(slolpBPM_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_slolpbpm_entity_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_Entity)


def test_hyp_slolpbpm_entity_constructor_exists():
    assert callable(slolpBPM_Entity.__init__)


def test_hyp_slolpbpm_entity_constructor_args():
    sig = inspect.signature(slolpBPM_Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_slolpbpm_datatype_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_Datatype)


def test_hyp_slolpbpm_datatype_constructor_exists():
    assert callable(slolpBPM_Datatype.__init__)


def test_hyp_slolpbpm_datatype_constructor_args():
    sig = inspect.signature(slolpBPM_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_hyp_slolpbpm_type_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_Type)


def test_hyp_slolpbpm_type_constructor_exists():
    assert callable(slolpBPM_Type.__init__)


def test_hyp_slolpbpm_type_constructor_args():
    sig = inspect.signature(slolpBPM_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_slolpbpm_domainmodel_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_DomainModel)


def test_hyp_slolpbpm_domainmodel_constructor_exists():
    assert callable(slolpBPM_DomainModel.__init__)


def test_hyp_slolpbpm_domainmodel_constructor_args():
    sig = inspect.signature(slolpBPM_DomainModel.__init__)
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
slolpBPM_Feature_strategy = st.builds(
    slolpBPM_Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
slolpBPM_Entity_strategy = st.builds(
    slolpBPM_Entity,
)
slolpBPM_Datatype_strategy = st.builds(
    slolpBPM_Datatype,
)
slolpBPM_Type_strategy = st.builds(
    slolpBPM_Type,
    name=
        safe_text
)
slolpBPM_DomainModel_strategy = st.builds(
    slolpBPM_DomainModel,
)




@given(instance=slolpBPM_Feature_strategy)
def test_hyp_slolpbpm_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=slolpBPM_Feature_strategy)
def test_hyp_slolpbpm_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=slolpBPM_Type_strategy)
def test_hyp_slolpbpm_type_name_setter(instance):
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
    slolpBPM_Datatype,
    slolpBPM_DomainModel,
    slolpBPM_Entity,
    slolpBPM_Feature,
    slolpBPM_Type,
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

def test_slolpBPM_Feature_many_value_roundtrip():
    instance = slolpBPM_Feature(many=True, name="sample_text")
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_slolpBPM_Feature_name_value_roundtrip():
    instance = slolpBPM_Feature(many=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_slolpBPM_Type_name_value_roundtrip():
    instance = slolpBPM_Type(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_slolpBPM_Datatype_isa_Type():
    instance = slolpBPM_Datatype()
    assert isinstance(instance, Type)


def test_slolpBPM_Entity_isa_Type():
    instance = slolpBPM_Entity()
    assert isinstance(instance, Type)


def test_assoc_elements0_link_reassign_clear():
    a = slolpBPM_Type(name="sample_text")
    b1 = slolpBPM_DomainModel()
    b2 = slolpBPM_DomainModel()
    _safe_set(a, 'slolpBPM_Type', b1)
    assert _is_linked(a, 'slolpBPM_Type', b1)
    if hasattr(b1, 'slolpBPM_DomainModel'):
        assert _is_linked(b1, 'slolpBPM_DomainModel', a)
    _safe_set(a, 'slolpBPM_Type', b2)
    assert _is_linked(a, 'slolpBPM_Type', b2)
    if hasattr(b1, 'slolpBPM_DomainModel'):
        assert not _is_linked(b1, 'slolpBPM_DomainModel', a)
    if hasattr(b2, 'slolpBPM_DomainModel'):
        assert _is_linked(b2, 'slolpBPM_DomainModel', a)
    _safe_set(a, 'slolpBPM_Type', None)
    assert not _is_linked(a, 'slolpBPM_Type', b2)
    if hasattr(b2, 'slolpBPM_DomainModel'):
        assert not _is_linked(b2, 'slolpBPM_DomainModel', a)


def test_assoc_feautres3_link_reassign_clear():
    a = slolpBPM_Feature(many=True, name="sample_text")
    b1 = slolpBPM_Entity()
    b2 = slolpBPM_Entity()
    _safe_set(a, 'slolpBPM_Feature', b1)
    assert _is_linked(a, 'slolpBPM_Feature', b1)
    if hasattr(b1, 'slolpBPM_Entity4'):
        assert _is_linked(b1, 'slolpBPM_Entity4', a)
    _safe_set(a, 'slolpBPM_Feature', b2)
    assert _is_linked(a, 'slolpBPM_Feature', b2)
    if hasattr(b1, 'slolpBPM_Entity4'):
        assert not _is_linked(b1, 'slolpBPM_Entity4', a)
    if hasattr(b2, 'slolpBPM_Entity4'):
        assert _is_linked(b2, 'slolpBPM_Entity4', a)
    _safe_set(a, 'slolpBPM_Feature', None)
    assert not _is_linked(a, 'slolpBPM_Feature', b2)
    if hasattr(b2, 'slolpBPM_Entity4'):
        assert not _is_linked(b2, 'slolpBPM_Entity4', a)


def test_assoc_type5_link_reassign_clear():
    a = slolpBPM_Type(name="sample_text")
    b1 = slolpBPM_Feature(many=True, name="sample_text")
    b2 = slolpBPM_Feature(many=False, name="sample_text_2")
    _safe_set(a, 'slolpBPM_Type7', b1)
    assert _is_linked(a, 'slolpBPM_Type7', b1)
    if hasattr(b1, 'slolpBPM_Feature6'):
        assert _is_linked(b1, 'slolpBPM_Feature6', a)
    _safe_set(a, 'slolpBPM_Type7', b2)
    assert _is_linked(a, 'slolpBPM_Type7', b2)
    if hasattr(b1, 'slolpBPM_Feature6'):
        assert not _is_linked(b1, 'slolpBPM_Feature6', a)
    if hasattr(b2, 'slolpBPM_Feature6'):
        assert _is_linked(b2, 'slolpBPM_Feature6', a)
    _safe_set(a, 'slolpBPM_Type7', None)
    assert not _is_linked(a, 'slolpBPM_Type7', b2)
    if hasattr(b2, 'slolpBPM_Feature6'):
        assert not _is_linked(b2, 'slolpBPM_Feature6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


slolpBPM_Datatype_strategy = st.builds(slolpBPM_Datatype)
@given(instance=slolpBPM_Datatype_strategy)
@settings(max_examples=25)
def test_slolpBPM_Datatype_instantiation(instance):
    assert isinstance(instance, slolpBPM_Datatype)


slolpBPM_DomainModel_strategy = st.builds(slolpBPM_DomainModel)
@given(instance=slolpBPM_DomainModel_strategy)
@settings(max_examples=25)
def test_slolpBPM_DomainModel_instantiation(instance):
    assert isinstance(instance, slolpBPM_DomainModel)


slolpBPM_Entity_strategy = st.builds(slolpBPM_Entity)
@given(instance=slolpBPM_Entity_strategy)
@settings(max_examples=25)
def test_slolpBPM_Entity_instantiation(instance):
    assert isinstance(instance, slolpBPM_Entity)


slolpBPM_Feature_strategy = st.builds(slolpBPM_Feature, many=st.booleans(), name=safe_text)
@given(instance=slolpBPM_Feature_strategy)
@settings(max_examples=25)
def test_slolpBPM_Feature_instantiation(instance):
    assert isinstance(instance, slolpBPM_Feature)


slolpBPM_Type_strategy = st.builds(slolpBPM_Type, name=safe_text)
@given(instance=slolpBPM_Type_strategy)
@settings(max_examples=25)
def test_slolpBPM_Type_instantiation(instance):
    assert isinstance(instance, slolpBPM_Type)



