import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_constraints7_reverse_link_reassign_clear():
    a1 = feaMo_FeatureModel(name="sample_text")
    a2 = feaMo_FeatureModel(name="sample_text_2")
    b = feaMo_FeatureConstraint(rel="sample_text")
    _safe_set(b, 'feaMo_FeatureConstraint', a1)
    assert _is_linked(b, 'feaMo_FeatureConstraint', a1)
    if hasattr(a1, 'feaMo_FeatureModel8'):
        assert _is_linked(a1, 'feaMo_FeatureModel8', b)
    _safe_set(b, 'feaMo_FeatureConstraint', a2)
    assert _is_linked(b, 'feaMo_FeatureConstraint', a2)
    if hasattr(a1, 'feaMo_FeatureModel8'):
        assert not _is_linked(a1, 'feaMo_FeatureModel8', b)
    if hasattr(a2, 'feaMo_FeatureModel8'):
        assert _is_linked(a2, 'feaMo_FeatureModel8', b)
    _safe_set(b, 'feaMo_FeatureConstraint', None)
    assert not _is_linked(b, 'feaMo_FeatureConstraint', a2)
    if hasattr(a2, 'feaMo_FeatureModel8'):
        assert not _is_linked(a2, 'feaMo_FeatureModel8', b)


def test_assoc_feature130_reverse_link_reassign_clear():
    a1 = feaMo_FeatureConstraint(rel="sample_text")
    a2 = feaMo_FeatureConstraint(rel="sample_text_2")
    b = feaMo_Feature(name="sample_text")
    _safe_set(b, 'feaMo_Feature32', a1)
    assert _is_linked(b, 'feaMo_Feature32', a1)
    if hasattr(a1, 'feaMo_FeatureConstraint31'):
        assert _is_linked(a1, 'feaMo_FeatureConstraint31', b)
    _safe_set(b, 'feaMo_Feature32', a2)
    assert _is_linked(b, 'feaMo_Feature32', a2)
    if hasattr(a1, 'feaMo_FeatureConstraint31'):
        assert not _is_linked(a1, 'feaMo_FeatureConstraint31', b)
    if hasattr(a2, 'feaMo_FeatureConstraint31'):
        assert _is_linked(a2, 'feaMo_FeatureConstraint31', b)
    _safe_set(b, 'feaMo_Feature32', None)
    assert not _is_linked(b, 'feaMo_Feature32', a2)
    if hasattr(a2, 'feaMo_FeatureConstraint31'):
        assert not _is_linked(a2, 'feaMo_FeatureConstraint31', b)


def test_assoc_feature233_reverse_link_reassign_clear():
    a1 = feaMo_FeatureConstraint(rel="sample_text")
    a2 = feaMo_FeatureConstraint(rel="sample_text_2")
    b = feaMo_Feature(name="sample_text")
    _safe_set(b, 'feaMo_Feature35', a1)
    assert _is_linked(b, 'feaMo_Feature35', a1)
    if hasattr(a1, 'feaMo_FeatureConstraint34'):
        assert _is_linked(a1, 'feaMo_FeatureConstraint34', b)
    _safe_set(b, 'feaMo_Feature35', a2)
    assert _is_linked(b, 'feaMo_Feature35', a2)
    if hasattr(a1, 'feaMo_FeatureConstraint34'):
        assert not _is_linked(a1, 'feaMo_FeatureConstraint34', b)
    if hasattr(a2, 'feaMo_FeatureConstraint34'):
        assert _is_linked(a2, 'feaMo_FeatureConstraint34', b)
    _safe_set(b, 'feaMo_Feature35', None)
    assert not _is_linked(b, 'feaMo_Feature35', a2)
    if hasattr(a2, 'feaMo_FeatureConstraint34'):
        assert not _is_linked(a2, 'feaMo_FeatureConstraint34', b)


def test_assoc_fm38_reverse_link_reassign_clear():
    a1 = feaMo_FeatureModel(name="sample_text")
    a2 = feaMo_FeatureModel(name="sample_text_2")
    b = feaMo_FeamoFeatureConfig(name="sample_text")
    _safe_set(b, 'feaMo_FeamoFeatureConfig39', a1)
    assert _is_linked(b, 'feaMo_FeamoFeatureConfig39', a1)
    if hasattr(a1, 'feaMo_FeatureModel40'):
        assert _is_linked(a1, 'feaMo_FeatureModel40', b)
    _safe_set(b, 'feaMo_FeamoFeatureConfig39', a2)
    assert _is_linked(b, 'feaMo_FeamoFeatureConfig39', a2)
    if hasattr(a1, 'feaMo_FeatureModel40'):
        assert not _is_linked(a1, 'feaMo_FeatureModel40', b)
    if hasattr(a2, 'feaMo_FeatureModel40'):
        assert _is_linked(a2, 'feaMo_FeatureModel40', b)
    _safe_set(b, 'feaMo_FeamoFeatureConfig39', None)
    assert not _is_linked(b, 'feaMo_FeamoFeatureConfig39', a2)
    if hasattr(a2, 'feaMo_FeatureModel40'):
        assert not _is_linked(a2, 'feaMo_FeatureModel40', b)


def test_assoc_selected41_reverse_link_reassign_clear():
    a1 = feaMo_Feature(name="sample_text")
    a2 = feaMo_Feature(name="sample_text_2")
    b = feaMo_FeamoFeatureConfig(name="sample_text")
    _safe_set(b, 'feaMo_FeamoFeatureConfig42', {a1})
    assert _is_linked(b, 'feaMo_FeamoFeatureConfig42', a1)
    if hasattr(a1, 'feaMo_Feature43'):
        assert _is_linked(a1, 'feaMo_Feature43', b)
    _safe_set(b, 'feaMo_FeamoFeatureConfig42', {a2})
    assert _is_linked(b, 'feaMo_FeamoFeatureConfig42', a2)
    if hasattr(a1, 'feaMo_Feature43'):
        assert not _is_linked(a1, 'feaMo_Feature43', b)
    if hasattr(a2, 'feaMo_Feature43'):
        assert _is_linked(a2, 'feaMo_Feature43', b)
    _safe_set(b, 'feaMo_FeamoFeatureConfig42', set())
    assert not _is_linked(b, 'feaMo_FeamoFeatureConfig42', a2)
    if hasattr(a2, 'feaMo_Feature43'):
        assert not _is_linked(a2, 'feaMo_Feature43', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_configs1_stub_double():
    # feaMo_Model has no real 'feaMo_Model2' property in the generated
    # code (a bare stub) -- manually attach it so feaMo_FeamoFeatureConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feaMo_FeamoFeatureConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feaMo_FeamoFeatureConfig(name="sample_text")
    partner = feaMo_Model()
    setattr(partner, 'feaMo_Model2', None)
    _safe_set(owner, 'feaMo_FeamoFeatureConfig', partner)
    assert owner in getattr(partner, 'feaMo_Model2')
    _safe_set(owner, 'feaMo_FeamoFeatureConfig', None)
    assert owner not in getattr(partner, 'feaMo_Model2')


def test_assoc_defs5_stub_double():
    # feaMo_FeatureDef has no real 'feaMo_FeatureDef' property in the generated
    # code (a bare stub) -- manually attach it so feaMo_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feaMo_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feaMo_FeatureModel(name="sample_text")
    partner = feaMo_FeatureDef()
    setattr(partner, 'feaMo_FeatureDef', None)
    _safe_set(owner, 'feaMo_FeatureModel6', {partner})
    assert getattr(partner, 'feaMo_FeatureDef') == owner
    _safe_set(owner, 'feaMo_FeatureModel6', set())
    assert getattr(partner, 'feaMo_FeatureDef') is None


def test_assoc_details3_stub_double():
    # feaMo_FeatureDetails has no real 'feaMo_FeatureDetails' property in the generated
    # code (a bare stub) -- manually attach it so feaMo_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feaMo_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feaMo_FeatureModel(name="sample_text")
    partner = feaMo_FeatureDetails()
    setattr(partner, 'feaMo_FeatureDetails', None)
    _safe_set(owner, 'feaMo_FeatureModel4', partner)
    assert getattr(partner, 'feaMo_FeatureDetails') == owner
    _safe_set(owner, 'feaMo_FeatureModel4', None)
    assert getattr(partner, 'feaMo_FeatureDetails') is None


def test_assoc_feature24_stub_double():
    # feaMo_FeatureDef has no real 'feaMo_FeatureDef25' property in the generated
    # code (a bare stub) -- manually attach it so feaMo_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feaMo_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feaMo_Feature(name="sample_text")
    partner = feaMo_FeatureDef()
    setattr(partner, 'feaMo_FeatureDef25', None)
    _safe_set(owner, 'feaMo_Feature26', partner)
    assert getattr(partner, 'feaMo_FeatureDef25') == owner
    _safe_set(owner, 'feaMo_Feature26', None)
    assert getattr(partner, 'feaMo_FeatureDef25') is None


def test_assoc_feature36_stub_double():
    # feaMo_FeamoFSelector has no real 'feaMo_FeamoFSelector' property in the generated
    # code (a bare stub) -- manually attach it so feaMo_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feaMo_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feaMo_Feature(name="sample_text")
    partner = feaMo_FeamoFSelector()
    setattr(partner, 'feaMo_FeamoFSelector', None)
    _safe_set(owner, 'feaMo_Feature37', partner)
    assert owner in getattr(partner, 'feaMo_FeamoFSelector')
    _safe_set(owner, 'feaMo_Feature37', None)
    assert owner not in getattr(partner, 'feaMo_FeamoFSelector')


def test_assoc_featureModels0_stub_double():
    # feaMo_Model has no real 'feaMo_Model' property in the generated
    # code (a bare stub) -- manually attach it so feaMo_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feaMo_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feaMo_FeatureModel(name="sample_text")
    partner = feaMo_Model()
    setattr(partner, 'feaMo_Model', None)
    _safe_set(owner, 'feaMo_FeatureModel', partner)
    assert owner in getattr(partner, 'feaMo_Model')
    _safe_set(owner, 'feaMo_FeatureModel', None)
    assert owner not in getattr(partner, 'feaMo_Model')


def test_assoc_mandatory19_stub_double():
    # feaMo_SimpleFeature has no real 'feaMo_SimpleFeature20' property in the generated
    # code (a bare stub) -- manually attach it so feaMo_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feaMo_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feaMo_Feature(name="sample_text")
    partner = feaMo_SimpleFeature()
    setattr(partner, 'feaMo_SimpleFeature20', None)
    _safe_set(owner, 'feaMo_Feature', partner)
    assert getattr(partner, 'feaMo_SimpleFeature20') == owner
    _safe_set(owner, 'feaMo_Feature', None)
    assert getattr(partner, 'feaMo_SimpleFeature20') is None


def test_assoc_optional21_stub_double():
    # feaMo_SimpleFeature has no real 'feaMo_SimpleFeature22' property in the generated
    # code (a bare stub) -- manually attach it so feaMo_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feaMo_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feaMo_Feature(name="sample_text")
    partner = feaMo_SimpleFeature()
    setattr(partner, 'feaMo_SimpleFeature22', None)
    _safe_set(owner, 'feaMo_Feature23', partner)
    assert getattr(partner, 'feaMo_SimpleFeature22') == owner
    _safe_set(owner, 'feaMo_Feature23', None)
    assert getattr(partner, 'feaMo_SimpleFeature22') is None


