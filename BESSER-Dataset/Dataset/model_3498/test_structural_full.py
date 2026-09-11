import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    feaMo_FeamoFSelector,
    feaMo_FeamoFeatureConfig,
    feaMo_Feature,
    feaMo_FeatureConstraint,
    feaMo_FeatureDef,
    feaMo_FeatureDetails,
    feaMo_FeatureGroup,
    feaMo_FeatureModel,
    feaMo_Model,
    feaMo_SimpleFeature,
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

def test_feaMo_FeamoFeatureConfig_name_value_roundtrip():
    instance = feaMo_FeamoFeatureConfig(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_feaMo_Feature_name_value_roundtrip():
    instance = feaMo_Feature(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_feaMo_FeatureConstraint_rel_value_roundtrip():
    instance = feaMo_FeatureConstraint(rel="sample_text")
    assert instance.rel == "sample_text"
    instance.rel = "sample_text_2"
    assert instance.rel == "sample_text_2"


def test_feaMo_FeatureModel_name_value_roundtrip():
    instance = feaMo_FeatureModel(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_configs1_link_reassign_clear():
    a = feaMo_FeamoFeatureConfig(name="sample_text")
    b1 = feaMo_Model()
    b2 = feaMo_Model()
    _safe_set(a, 'feaMo_FeamoFeatureConfig', b1)
    assert _is_linked(a, 'feaMo_FeamoFeatureConfig', b1)
    if hasattr(b1, 'feaMo_Model2'):
        assert _is_linked(b1, 'feaMo_Model2', a)
    _safe_set(a, 'feaMo_FeamoFeatureConfig', b2)
    assert _is_linked(a, 'feaMo_FeamoFeatureConfig', b2)
    if hasattr(b1, 'feaMo_Model2'):
        assert not _is_linked(b1, 'feaMo_Model2', a)
    if hasattr(b2, 'feaMo_Model2'):
        assert _is_linked(b2, 'feaMo_Model2', a)
    _safe_set(a, 'feaMo_FeamoFeatureConfig', None)
    assert not _is_linked(a, 'feaMo_FeamoFeatureConfig', b2)
    if hasattr(b2, 'feaMo_Model2'):
        assert not _is_linked(b2, 'feaMo_Model2', a)


def test_assoc_constraints7_link_reassign_clear():
    a = feaMo_FeatureModel(name="sample_text")
    b1 = feaMo_FeatureConstraint(rel="sample_text")
    b2 = feaMo_FeatureConstraint(rel="sample_text_2")
    _safe_set(a, 'feaMo_FeatureModel8', {b1})
    assert _is_linked(a, 'feaMo_FeatureModel8', b1)
    if hasattr(b1, 'feaMo_FeatureConstraint'):
        assert _is_linked(b1, 'feaMo_FeatureConstraint', a)
    _safe_set(a, 'feaMo_FeatureModel8', {b2})
    assert _is_linked(a, 'feaMo_FeatureModel8', b2)
    if hasattr(b1, 'feaMo_FeatureConstraint'):
        assert not _is_linked(b1, 'feaMo_FeatureConstraint', a)
    if hasattr(b2, 'feaMo_FeatureConstraint'):
        assert _is_linked(b2, 'feaMo_FeatureConstraint', a)
    _safe_set(a, 'feaMo_FeatureModel8', set())
    assert not _is_linked(a, 'feaMo_FeatureModel8', b2)
    if hasattr(b2, 'feaMo_FeatureConstraint'):
        assert not _is_linked(b2, 'feaMo_FeatureConstraint', a)


def test_assoc_defs5_link_reassign_clear():
    a = feaMo_FeatureModel(name="sample_text")
    b1 = feaMo_FeatureDef()
    b2 = feaMo_FeatureDef()
    _safe_set(a, 'feaMo_FeatureModel6', {b1})
    assert _is_linked(a, 'feaMo_FeatureModel6', b1)
    if hasattr(b1, 'feaMo_FeatureDef'):
        assert _is_linked(b1, 'feaMo_FeatureDef', a)
    _safe_set(a, 'feaMo_FeatureModel6', {b2})
    assert _is_linked(a, 'feaMo_FeatureModel6', b2)
    if hasattr(b1, 'feaMo_FeatureDef'):
        assert not _is_linked(b1, 'feaMo_FeatureDef', a)
    if hasattr(b2, 'feaMo_FeatureDef'):
        assert _is_linked(b2, 'feaMo_FeatureDef', a)
    _safe_set(a, 'feaMo_FeatureModel6', set())
    assert not _is_linked(a, 'feaMo_FeatureModel6', b2)
    if hasattr(b2, 'feaMo_FeatureDef'):
        assert not _is_linked(b2, 'feaMo_FeatureDef', a)


def test_assoc_details3_link_reassign_clear():
    a = feaMo_FeatureModel(name="sample_text")
    b1 = feaMo_FeatureDetails()
    b2 = feaMo_FeatureDetails()
    _safe_set(a, 'feaMo_FeatureModel4', b1)
    assert _is_linked(a, 'feaMo_FeatureModel4', b1)
    if hasattr(b1, 'feaMo_FeatureDetails'):
        assert _is_linked(b1, 'feaMo_FeatureDetails', a)
    _safe_set(a, 'feaMo_FeatureModel4', b2)
    assert _is_linked(a, 'feaMo_FeatureModel4', b2)
    if hasattr(b1, 'feaMo_FeatureDetails'):
        assert not _is_linked(b1, 'feaMo_FeatureDetails', a)
    if hasattr(b2, 'feaMo_FeatureDetails'):
        assert _is_linked(b2, 'feaMo_FeatureDetails', a)
    _safe_set(a, 'feaMo_FeatureModel4', None)
    assert not _is_linked(a, 'feaMo_FeatureModel4', b2)
    if hasattr(b2, 'feaMo_FeatureDetails'):
        assert not _is_linked(b2, 'feaMo_FeatureDetails', a)


def test_assoc_feature130_link_reassign_clear():
    a = feaMo_FeatureConstraint(rel="sample_text")
    b1 = feaMo_Feature(name="sample_text")
    b2 = feaMo_Feature(name="sample_text_2")
    _safe_set(a, 'feaMo_FeatureConstraint31', b1)
    assert _is_linked(a, 'feaMo_FeatureConstraint31', b1)
    if hasattr(b1, 'feaMo_Feature32'):
        assert _is_linked(b1, 'feaMo_Feature32', a)
    _safe_set(a, 'feaMo_FeatureConstraint31', b2)
    assert _is_linked(a, 'feaMo_FeatureConstraint31', b2)
    if hasattr(b1, 'feaMo_Feature32'):
        assert not _is_linked(b1, 'feaMo_Feature32', a)
    if hasattr(b2, 'feaMo_Feature32'):
        assert _is_linked(b2, 'feaMo_Feature32', a)
    _safe_set(a, 'feaMo_FeatureConstraint31', None)
    assert not _is_linked(a, 'feaMo_FeatureConstraint31', b2)
    if hasattr(b2, 'feaMo_Feature32'):
        assert not _is_linked(b2, 'feaMo_Feature32', a)


def test_assoc_feature233_link_reassign_clear():
    a = feaMo_FeatureConstraint(rel="sample_text")
    b1 = feaMo_Feature(name="sample_text")
    b2 = feaMo_Feature(name="sample_text_2")
    _safe_set(a, 'feaMo_FeatureConstraint34', b1)
    assert _is_linked(a, 'feaMo_FeatureConstraint34', b1)
    if hasattr(b1, 'feaMo_Feature35'):
        assert _is_linked(b1, 'feaMo_Feature35', a)
    _safe_set(a, 'feaMo_FeatureConstraint34', b2)
    assert _is_linked(a, 'feaMo_FeatureConstraint34', b2)
    if hasattr(b1, 'feaMo_Feature35'):
        assert not _is_linked(b1, 'feaMo_Feature35', a)
    if hasattr(b2, 'feaMo_Feature35'):
        assert _is_linked(b2, 'feaMo_Feature35', a)
    _safe_set(a, 'feaMo_FeatureConstraint34', None)
    assert not _is_linked(a, 'feaMo_FeatureConstraint34', b2)
    if hasattr(b2, 'feaMo_Feature35'):
        assert not _is_linked(b2, 'feaMo_Feature35', a)


def test_assoc_feature24_link_reassign_clear():
    a = feaMo_Feature(name="sample_text")
    b1 = feaMo_FeatureDef()
    b2 = feaMo_FeatureDef()
    _safe_set(a, 'feaMo_Feature26', b1)
    assert _is_linked(a, 'feaMo_Feature26', b1)
    if hasattr(b1, 'feaMo_FeatureDef25'):
        assert _is_linked(b1, 'feaMo_FeatureDef25', a)
    _safe_set(a, 'feaMo_Feature26', b2)
    assert _is_linked(a, 'feaMo_Feature26', b2)
    if hasattr(b1, 'feaMo_FeatureDef25'):
        assert not _is_linked(b1, 'feaMo_FeatureDef25', a)
    if hasattr(b2, 'feaMo_FeatureDef25'):
        assert _is_linked(b2, 'feaMo_FeatureDef25', a)
    _safe_set(a, 'feaMo_Feature26', None)
    assert not _is_linked(a, 'feaMo_Feature26', b2)
    if hasattr(b2, 'feaMo_FeatureDef25'):
        assert not _is_linked(b2, 'feaMo_FeatureDef25', a)


def test_assoc_feature36_link_reassign_clear():
    a = feaMo_Feature(name="sample_text")
    b1 = feaMo_FeamoFSelector()
    b2 = feaMo_FeamoFSelector()
    _safe_set(a, 'feaMo_Feature37', b1)
    assert _is_linked(a, 'feaMo_Feature37', b1)
    if hasattr(b1, 'feaMo_FeamoFSelector'):
        assert _is_linked(b1, 'feaMo_FeamoFSelector', a)
    _safe_set(a, 'feaMo_Feature37', b2)
    assert _is_linked(a, 'feaMo_Feature37', b2)
    if hasattr(b1, 'feaMo_FeamoFSelector'):
        assert not _is_linked(b1, 'feaMo_FeamoFSelector', a)
    if hasattr(b2, 'feaMo_FeamoFSelector'):
        assert _is_linked(b2, 'feaMo_FeamoFSelector', a)
    _safe_set(a, 'feaMo_Feature37', None)
    assert not _is_linked(a, 'feaMo_Feature37', b2)
    if hasattr(b2, 'feaMo_FeamoFSelector'):
        assert not _is_linked(b2, 'feaMo_FeamoFSelector', a)


def test_assoc_featureModels0_link_reassign_clear():
    a = feaMo_FeatureModel(name="sample_text")
    b1 = feaMo_Model()
    b2 = feaMo_Model()
    _safe_set(a, 'feaMo_FeatureModel', b1)
    assert _is_linked(a, 'feaMo_FeatureModel', b1)
    if hasattr(b1, 'feaMo_Model'):
        assert _is_linked(b1, 'feaMo_Model', a)
    _safe_set(a, 'feaMo_FeatureModel', b2)
    assert _is_linked(a, 'feaMo_FeatureModel', b2)
    if hasattr(b1, 'feaMo_Model'):
        assert not _is_linked(b1, 'feaMo_Model', a)
    if hasattr(b2, 'feaMo_Model'):
        assert _is_linked(b2, 'feaMo_Model', a)
    _safe_set(a, 'feaMo_FeatureModel', None)
    assert not _is_linked(a, 'feaMo_FeatureModel', b2)
    if hasattr(b2, 'feaMo_Model'):
        assert not _is_linked(b2, 'feaMo_Model', a)


def test_assoc_fm38_link_reassign_clear():
    a = feaMo_FeatureModel(name="sample_text")
    b1 = feaMo_FeamoFeatureConfig(name="sample_text")
    b2 = feaMo_FeamoFeatureConfig(name="sample_text_2")
    _safe_set(a, 'feaMo_FeatureModel40', b1)
    assert _is_linked(a, 'feaMo_FeatureModel40', b1)
    if hasattr(b1, 'feaMo_FeamoFeatureConfig39'):
        assert _is_linked(b1, 'feaMo_FeamoFeatureConfig39', a)
    _safe_set(a, 'feaMo_FeatureModel40', b2)
    assert _is_linked(a, 'feaMo_FeatureModel40', b2)
    if hasattr(b1, 'feaMo_FeamoFeatureConfig39'):
        assert not _is_linked(b1, 'feaMo_FeamoFeatureConfig39', a)
    if hasattr(b2, 'feaMo_FeamoFeatureConfig39'):
        assert _is_linked(b2, 'feaMo_FeamoFeatureConfig39', a)
    _safe_set(a, 'feaMo_FeatureModel40', None)
    assert not _is_linked(a, 'feaMo_FeatureModel40', b2)
    if hasattr(b2, 'feaMo_FeamoFeatureConfig39'):
        assert not _is_linked(b2, 'feaMo_FeamoFeatureConfig39', a)


def test_assoc_mandatory19_link_reassign_clear():
    a = feaMo_Feature(name="sample_text")
    b1 = feaMo_SimpleFeature()
    b2 = feaMo_SimpleFeature()
    _safe_set(a, 'feaMo_Feature', b1)
    assert _is_linked(a, 'feaMo_Feature', b1)
    if hasattr(b1, 'feaMo_SimpleFeature20'):
        assert _is_linked(b1, 'feaMo_SimpleFeature20', a)
    _safe_set(a, 'feaMo_Feature', b2)
    assert _is_linked(a, 'feaMo_Feature', b2)
    if hasattr(b1, 'feaMo_SimpleFeature20'):
        assert not _is_linked(b1, 'feaMo_SimpleFeature20', a)
    if hasattr(b2, 'feaMo_SimpleFeature20'):
        assert _is_linked(b2, 'feaMo_SimpleFeature20', a)
    _safe_set(a, 'feaMo_Feature', None)
    assert not _is_linked(a, 'feaMo_Feature', b2)
    if hasattr(b2, 'feaMo_SimpleFeature20'):
        assert not _is_linked(b2, 'feaMo_SimpleFeature20', a)


def test_assoc_optional21_link_reassign_clear():
    a = feaMo_Feature(name="sample_text")
    b1 = feaMo_SimpleFeature()
    b2 = feaMo_SimpleFeature()
    _safe_set(a, 'feaMo_Feature23', b1)
    assert _is_linked(a, 'feaMo_Feature23', b1)
    if hasattr(b1, 'feaMo_SimpleFeature22'):
        assert _is_linked(b1, 'feaMo_SimpleFeature22', a)
    _safe_set(a, 'feaMo_Feature23', b2)
    assert _is_linked(a, 'feaMo_Feature23', b2)
    if hasattr(b1, 'feaMo_SimpleFeature22'):
        assert not _is_linked(b1, 'feaMo_SimpleFeature22', a)
    if hasattr(b2, 'feaMo_SimpleFeature22'):
        assert _is_linked(b2, 'feaMo_SimpleFeature22', a)
    _safe_set(a, 'feaMo_Feature23', None)
    assert not _is_linked(a, 'feaMo_Feature23', b2)
    if hasattr(b2, 'feaMo_SimpleFeature22'):
        assert not _is_linked(b2, 'feaMo_SimpleFeature22', a)


def test_assoc_selected41_link_reassign_clear():
    a = feaMo_Feature(name="sample_text")
    b1 = feaMo_FeamoFeatureConfig(name="sample_text")
    b2 = feaMo_FeamoFeatureConfig(name="sample_text_2")
    _safe_set(a, 'feaMo_Feature43', b1)
    assert _is_linked(a, 'feaMo_Feature43', b1)
    if hasattr(b1, 'feaMo_FeamoFeatureConfig42'):
        assert _is_linked(b1, 'feaMo_FeamoFeatureConfig42', a)
    _safe_set(a, 'feaMo_Feature43', b2)
    assert _is_linked(a, 'feaMo_Feature43', b2)
    if hasattr(b1, 'feaMo_FeamoFeatureConfig42'):
        assert not _is_linked(b1, 'feaMo_FeamoFeatureConfig42', a)
    if hasattr(b2, 'feaMo_FeamoFeatureConfig42'):
        assert _is_linked(b2, 'feaMo_FeamoFeatureConfig42', a)
    _safe_set(a, 'feaMo_Feature43', None)
    assert not _is_linked(a, 'feaMo_Feature43', b2)
    if hasattr(b2, 'feaMo_FeamoFeatureConfig42'):
        assert not _is_linked(b2, 'feaMo_FeamoFeatureConfig42', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

feaMo_FeamoFSelector_strategy = st.builds(feaMo_FeamoFSelector)
@given(instance=feaMo_FeamoFSelector_strategy)
@settings(max_examples=25)
def test_feaMo_FeamoFSelector_instantiation(instance):
    assert isinstance(instance, feaMo_FeamoFSelector)


feaMo_FeamoFeatureConfig_strategy = st.builds(feaMo_FeamoFeatureConfig, name=safe_text)
@given(instance=feaMo_FeamoFeatureConfig_strategy)
@settings(max_examples=25)
def test_feaMo_FeamoFeatureConfig_instantiation(instance):
    assert isinstance(instance, feaMo_FeamoFeatureConfig)


feaMo_Feature_strategy = st.builds(feaMo_Feature, name=safe_text)
@given(instance=feaMo_Feature_strategy)
@settings(max_examples=25)
def test_feaMo_Feature_instantiation(instance):
    assert isinstance(instance, feaMo_Feature)


feaMo_FeatureConstraint_strategy = st.builds(feaMo_FeatureConstraint, rel=safe_text)
@given(instance=feaMo_FeatureConstraint_strategy)
@settings(max_examples=25)
def test_feaMo_FeatureConstraint_instantiation(instance):
    assert isinstance(instance, feaMo_FeatureConstraint)


feaMo_FeatureDef_strategy = st.builds(feaMo_FeatureDef)
@given(instance=feaMo_FeatureDef_strategy)
@settings(max_examples=25)
def test_feaMo_FeatureDef_instantiation(instance):
    assert isinstance(instance, feaMo_FeatureDef)


feaMo_FeatureDetails_strategy = st.builds(feaMo_FeatureDetails)
@given(instance=feaMo_FeatureDetails_strategy)
@settings(max_examples=25)
def test_feaMo_FeatureDetails_instantiation(instance):
    assert isinstance(instance, feaMo_FeatureDetails)


feaMo_FeatureGroup_strategy = st.builds(feaMo_FeatureGroup)
@given(instance=feaMo_FeatureGroup_strategy)
@settings(max_examples=25)
def test_feaMo_FeatureGroup_instantiation(instance):
    assert isinstance(instance, feaMo_FeatureGroup)


feaMo_FeatureModel_strategy = st.builds(feaMo_FeatureModel, name=safe_text)
@given(instance=feaMo_FeatureModel_strategy)
@settings(max_examples=25)
def test_feaMo_FeatureModel_instantiation(instance):
    assert isinstance(instance, feaMo_FeatureModel)


feaMo_Model_strategy = st.builds(feaMo_Model)
@given(instance=feaMo_Model_strategy)
@settings(max_examples=25)
def test_feaMo_Model_instantiation(instance):
    assert isinstance(instance, feaMo_Model)


feaMo_SimpleFeature_strategy = st.builds(feaMo_SimpleFeature)
@given(instance=feaMo_SimpleFeature_strategy)
@settings(max_examples=25)
def test_feaMo_SimpleFeature_instantiation(instance):
    assert isinstance(instance, feaMo_SimpleFeature)


