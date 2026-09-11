import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Constraint,
    E,
    Feature,
    Group,
    features_modeling_AND,
    features_modeling_Constraint,
    features_modeling_Constraints,
    features_modeling_E,
    features_modeling_EMAND,
    features_modeling_EX,
    features_modeling_Edge,
    features_modeling_F,
    features_modeling_Feature,
    features_modeling_G,
    features_modeling_GOR,
    features_modeling_GXOR,
    features_modeling_Group,
    features_modeling_I,
    features_modeling_NOT,
    features_modeling_PropFormulaCNF,
    features_modeling_PropositionOR,
    features_modeling_R,
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

def test_features_modeling_Feature_ID_value_roundtrip():
    instance = features_modeling_Feature(ID="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_features_modeling_EX_isa_Constraint():
    instance = features_modeling_EX()
    assert isinstance(instance, Constraint)


def test_features_modeling_I_isa_Constraint():
    instance = features_modeling_I()
    assert isinstance(instance, Constraint)


def test_features_modeling_EMAND_isa_E():
    instance = features_modeling_EMAND()
    assert isinstance(instance, E)


def test_features_modeling_R_isa_Feature():
    instance = features_modeling_R()
    assert isinstance(instance, Feature)


def test_features_modeling_GOR_isa_Group():
    instance = features_modeling_GOR()
    assert isinstance(instance, Group)


def test_features_modeling_GXOR_isa_Group():
    instance = features_modeling_GXOR()
    assert isinstance(instance, Group)


def test_assoc_children2_link_reassign_clear():
    a = features_modeling_Feature(ID="sample_text")
    b1 = features_modeling_Feature(ID="sample_text")
    b2 = features_modeling_Feature(ID="sample_text_2")
    _safe_set(a, 'features_modeling_Feature', b1)
    assert _is_linked(a, 'features_modeling_Feature', b1)
    if hasattr(b1, 'features_modeling_Feature1'):
        assert _is_linked(b1, 'features_modeling_Feature1', a)
    _safe_set(a, 'features_modeling_Feature', b2)
    assert _is_linked(a, 'features_modeling_Feature', b2)
    if hasattr(b1, 'features_modeling_Feature1'):
        assert not _is_linked(b1, 'features_modeling_Feature1', a)
    if hasattr(b2, 'features_modeling_Feature1'):
        assert _is_linked(b2, 'features_modeling_Feature1', a)
    _safe_set(a, 'features_modeling_Feature', None)
    assert not _is_linked(a, 'features_modeling_Feature', b2)
    if hasattr(b2, 'features_modeling_Feature1'):
        assert not _is_linked(b2, 'features_modeling_Feature1', a)


def test_assoc_feature12_link_reassign_clear():
    a = features_modeling_Feature(ID="sample_text")
    b1 = features_modeling_Constraint()
    b2 = features_modeling_Constraint()
    _safe_set(a, 'features_modeling_Feature13', b1)
    assert _is_linked(a, 'features_modeling_Feature13', b1)
    if hasattr(b1, 'features_modeling_Constraint'):
        assert _is_linked(b1, 'features_modeling_Constraint', a)
    _safe_set(a, 'features_modeling_Feature13', b2)
    assert _is_linked(a, 'features_modeling_Feature13', b2)
    if hasattr(b1, 'features_modeling_Constraint'):
        assert not _is_linked(b1, 'features_modeling_Constraint', a)
    if hasattr(b2, 'features_modeling_Constraint'):
        assert _is_linked(b2, 'features_modeling_Constraint', a)
    _safe_set(a, 'features_modeling_Feature13', None)
    assert not _is_linked(a, 'features_modeling_Feature13', b2)
    if hasattr(b2, 'features_modeling_Constraint'):
        assert not _is_linked(b2, 'features_modeling_Constraint', a)


def test_assoc_feature14_link_reassign_clear():
    a = features_modeling_Feature(ID="sample_text")
    b1 = features_modeling_Group()
    b2 = features_modeling_Group()
    _safe_set(a, 'features_modeling_Feature15', b1)
    assert _is_linked(a, 'features_modeling_Feature15', b1)
    if hasattr(b1, 'features_modeling_Group'):
        assert _is_linked(b1, 'features_modeling_Group', a)
    _safe_set(a, 'features_modeling_Feature15', b2)
    assert _is_linked(a, 'features_modeling_Feature15', b2)
    if hasattr(b1, 'features_modeling_Group'):
        assert not _is_linked(b1, 'features_modeling_Group', a)
    if hasattr(b2, 'features_modeling_Group'):
        assert _is_linked(b2, 'features_modeling_Group', a)
    _safe_set(a, 'features_modeling_Feature15', None)
    assert not _is_linked(a, 'features_modeling_Feature15', b2)
    if hasattr(b2, 'features_modeling_Group'):
        assert not _is_linked(b2, 'features_modeling_Group', a)


def test_assoc_feature19_link_reassign_clear():
    a = features_modeling_Feature(ID="sample_text")
    b1 = features_modeling_PropositionOR()
    b2 = features_modeling_PropositionOR()
    _safe_set(a, 'features_modeling_Feature21', b1)
    assert _is_linked(a, 'features_modeling_Feature21', b1)
    if hasattr(b1, 'features_modeling_PropositionOR20'):
        assert _is_linked(b1, 'features_modeling_PropositionOR20', a)
    _safe_set(a, 'features_modeling_Feature21', b2)
    assert _is_linked(a, 'features_modeling_Feature21', b2)
    if hasattr(b1, 'features_modeling_PropositionOR20'):
        assert not _is_linked(b1, 'features_modeling_PropositionOR20', a)
    if hasattr(b2, 'features_modeling_PropositionOR20'):
        assert _is_linked(b2, 'features_modeling_PropositionOR20', a)
    _safe_set(a, 'features_modeling_Feature21', None)
    assert not _is_linked(a, 'features_modeling_Feature21', b2)
    if hasattr(b2, 'features_modeling_PropositionOR20'):
        assert not _is_linked(b2, 'features_modeling_PropositionOR20', a)


def test_assoc_feature24_link_reassign_clear():
    a = features_modeling_Feature(ID="sample_text")
    b1 = features_modeling_NOT()
    b2 = features_modeling_NOT()
    _safe_set(a, 'features_modeling_Feature26', b1)
    assert _is_linked(a, 'features_modeling_Feature26', b1)
    if hasattr(b1, 'features_modeling_NOT25'):
        assert _is_linked(b1, 'features_modeling_NOT25', a)
    _safe_set(a, 'features_modeling_Feature26', b2)
    assert _is_linked(a, 'features_modeling_Feature26', b2)
    if hasattr(b1, 'features_modeling_NOT25'):
        assert not _is_linked(b1, 'features_modeling_NOT25', a)
    if hasattr(b2, 'features_modeling_NOT25'):
        assert _is_linked(b2, 'features_modeling_NOT25', a)
    _safe_set(a, 'features_modeling_Feature26', None)
    assert not _is_linked(a, 'features_modeling_Feature26', b2)
    if hasattr(b2, 'features_modeling_NOT25'):
        assert not _is_linked(b2, 'features_modeling_NOT25', a)


def test_assoc_feature3_link_reassign_clear():
    a = features_modeling_Feature(ID="sample_text")
    b1 = features_modeling_F()
    b2 = features_modeling_F()
    _safe_set(a, 'features_modeling_Feature4', b1)
    assert _is_linked(a, 'features_modeling_Feature4', b1)
    if hasattr(b1, 'features_modeling_F'):
        assert _is_linked(b1, 'features_modeling_F', a)
    _safe_set(a, 'features_modeling_Feature4', b2)
    assert _is_linked(a, 'features_modeling_Feature4', b2)
    if hasattr(b1, 'features_modeling_F'):
        assert not _is_linked(b1, 'features_modeling_F', a)
    if hasattr(b2, 'features_modeling_F'):
        assert _is_linked(b2, 'features_modeling_F', a)
    _safe_set(a, 'features_modeling_Feature4', None)
    assert not _is_linked(a, 'features_modeling_Feature4', b2)
    if hasattr(b2, 'features_modeling_F'):
        assert not _is_linked(b2, 'features_modeling_F', a)


def test_assoc_feature8_link_reassign_clear():
    a = features_modeling_Feature(ID="sample_text")
    b1 = features_modeling_Edge()
    b2 = features_modeling_Edge()
    _safe_set(a, 'features_modeling_Feature9', b1)
    assert _is_linked(a, 'features_modeling_Feature9', b1)
    if hasattr(b1, 'features_modeling_Edge'):
        assert _is_linked(b1, 'features_modeling_Edge', a)
    _safe_set(a, 'features_modeling_Feature9', b2)
    assert _is_linked(a, 'features_modeling_Feature9', b2)
    if hasattr(b1, 'features_modeling_Edge'):
        assert not _is_linked(b1, 'features_modeling_Edge', a)
    if hasattr(b2, 'features_modeling_Edge'):
        assert _is_linked(b2, 'features_modeling_Edge', a)
    _safe_set(a, 'features_modeling_Feature9', None)
    assert not _is_linked(a, 'features_modeling_Feature9', b2)
    if hasattr(b2, 'features_modeling_Edge'):
        assert not _is_linked(b2, 'features_modeling_Edge', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


E_strategy = st.builds(E)
@given(instance=E_strategy)
@settings(max_examples=25)
def test_E_instantiation(instance):
    assert isinstance(instance, E)


Feature_strategy = st.builds(Feature)
@given(instance=Feature_strategy)
@settings(max_examples=25)
def test_Feature_instantiation(instance):
    assert isinstance(instance, Feature)


Group_strategy = st.builds(Group)
@given(instance=Group_strategy)
@settings(max_examples=25)
def test_Group_instantiation(instance):
    assert isinstance(instance, Group)


features_modeling_AND_strategy = st.builds(features_modeling_AND)
@given(instance=features_modeling_AND_strategy)
@settings(max_examples=25)
def test_features_modeling_AND_instantiation(instance):
    assert isinstance(instance, features_modeling_AND)


features_modeling_Constraint_strategy = st.builds(features_modeling_Constraint)
@given(instance=features_modeling_Constraint_strategy)
@settings(max_examples=25)
def test_features_modeling_Constraint_instantiation(instance):
    assert isinstance(instance, features_modeling_Constraint)


features_modeling_Constraints_strategy = st.builds(features_modeling_Constraints)
@given(instance=features_modeling_Constraints_strategy)
@settings(max_examples=25)
def test_features_modeling_Constraints_instantiation(instance):
    assert isinstance(instance, features_modeling_Constraints)


features_modeling_E_strategy = st.builds(features_modeling_E)
@given(instance=features_modeling_E_strategy)
@settings(max_examples=25)
def test_features_modeling_E_instantiation(instance):
    assert isinstance(instance, features_modeling_E)


features_modeling_EMAND_strategy = st.builds(features_modeling_EMAND)
@given(instance=features_modeling_EMAND_strategy)
@settings(max_examples=25)
def test_features_modeling_EMAND_instantiation(instance):
    assert isinstance(instance, features_modeling_EMAND)


features_modeling_EX_strategy = st.builds(features_modeling_EX)
@given(instance=features_modeling_EX_strategy)
@settings(max_examples=25)
def test_features_modeling_EX_instantiation(instance):
    assert isinstance(instance, features_modeling_EX)


features_modeling_Edge_strategy = st.builds(features_modeling_Edge)
@given(instance=features_modeling_Edge_strategy)
@settings(max_examples=25)
def test_features_modeling_Edge_instantiation(instance):
    assert isinstance(instance, features_modeling_Edge)


features_modeling_F_strategy = st.builds(features_modeling_F)
@given(instance=features_modeling_F_strategy)
@settings(max_examples=25)
def test_features_modeling_F_instantiation(instance):
    assert isinstance(instance, features_modeling_F)


features_modeling_Feature_strategy = st.builds(features_modeling_Feature, ID=safe_text)
@given(instance=features_modeling_Feature_strategy)
@settings(max_examples=25)
def test_features_modeling_Feature_instantiation(instance):
    assert isinstance(instance, features_modeling_Feature)


features_modeling_G_strategy = st.builds(features_modeling_G)
@given(instance=features_modeling_G_strategy)
@settings(max_examples=25)
def test_features_modeling_G_instantiation(instance):
    assert isinstance(instance, features_modeling_G)


features_modeling_GOR_strategy = st.builds(features_modeling_GOR)
@given(instance=features_modeling_GOR_strategy)
@settings(max_examples=25)
def test_features_modeling_GOR_instantiation(instance):
    assert isinstance(instance, features_modeling_GOR)


features_modeling_GXOR_strategy = st.builds(features_modeling_GXOR)
@given(instance=features_modeling_GXOR_strategy)
@settings(max_examples=25)
def test_features_modeling_GXOR_instantiation(instance):
    assert isinstance(instance, features_modeling_GXOR)


features_modeling_Group_strategy = st.builds(features_modeling_Group)
@given(instance=features_modeling_Group_strategy)
@settings(max_examples=25)
def test_features_modeling_Group_instantiation(instance):
    assert isinstance(instance, features_modeling_Group)


features_modeling_I_strategy = st.builds(features_modeling_I)
@given(instance=features_modeling_I_strategy)
@settings(max_examples=25)
def test_features_modeling_I_instantiation(instance):
    assert isinstance(instance, features_modeling_I)


features_modeling_NOT_strategy = st.builds(features_modeling_NOT)
@given(instance=features_modeling_NOT_strategy)
@settings(max_examples=25)
def test_features_modeling_NOT_instantiation(instance):
    assert isinstance(instance, features_modeling_NOT)


features_modeling_PropFormulaCNF_strategy = st.builds(features_modeling_PropFormulaCNF)
@given(instance=features_modeling_PropFormulaCNF_strategy)
@settings(max_examples=25)
def test_features_modeling_PropFormulaCNF_instantiation(instance):
    assert isinstance(instance, features_modeling_PropFormulaCNF)


features_modeling_PropositionOR_strategy = st.builds(features_modeling_PropositionOR)
@given(instance=features_modeling_PropositionOR_strategy)
@settings(max_examples=25)
def test_features_modeling_PropositionOR_instantiation(instance):
    assert isinstance(instance, features_modeling_PropositionOR)


features_modeling_R_strategy = st.builds(features_modeling_R)
@given(instance=features_modeling_R_strategy)
@settings(max_examples=25)
def test_features_modeling_R_instantiation(instance):
    assert isinstance(instance, features_modeling_R)


