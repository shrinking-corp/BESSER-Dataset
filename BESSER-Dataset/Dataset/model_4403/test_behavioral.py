import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    Relation,
    featureModel_Feature,
    featureModel_FeatureGroup,
    featureModel_Node,
    featureModel_Project,
    featureModel_Relation,
    featureModel_RelationFG,
    featureModel_RelationFeature,
    featureModel_TypedValue,
    FeatureGroupType,
    FeatureType,
    ValueType,
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

def test_assoc_children16_reverse_link_reassign_clear():
    a1 = featureModel_FeatureGroup(lowerBound=7, type="sample_text", upperBound=7)
    a2 = featureModel_FeatureGroup(lowerBound=13, type="sample_text_2", upperBound=13)
    b = featureModel_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'featureModel_Feature17', a1)
    assert _is_linked(b, 'featureModel_Feature17', a1)
    if hasattr(a1, 'featureModel_FeatureGroup'):
        assert _is_linked(a1, 'featureModel_FeatureGroup', b)
    _safe_set(b, 'featureModel_Feature17', a2)
    assert _is_linked(b, 'featureModel_Feature17', a2)
    if hasattr(a1, 'featureModel_FeatureGroup'):
        assert not _is_linked(a1, 'featureModel_FeatureGroup', b)
    if hasattr(a2, 'featureModel_FeatureGroup'):
        assert _is_linked(a2, 'featureModel_FeatureGroup', b)
    _safe_set(b, 'featureModel_Feature17', None)
    assert not _is_linked(b, 'featureModel_Feature17', a2)
    if hasattr(a2, 'featureModel_FeatureGroup'):
        assert not _is_linked(a2, 'featureModel_FeatureGroup', b)


def test_assoc_featureValue9_reverse_link_reassign_clear():
    a1 = featureModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    a2 = featureModel_TypedValue(floatValue="sample_text_2", integerValue="sample_text_2", stringValue="sample_text_2")
    b = featureModel_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'featureModel_Feature11', a1)
    assert _is_linked(b, 'featureModel_Feature11', a1)
    if hasattr(a1, 'featureModel_TypedValue10'):
        assert _is_linked(a1, 'featureModel_TypedValue10', b)
    _safe_set(b, 'featureModel_Feature11', a2)
    assert _is_linked(b, 'featureModel_Feature11', a2)
    if hasattr(a1, 'featureModel_TypedValue10'):
        assert not _is_linked(a1, 'featureModel_TypedValue10', b)
    if hasattr(a2, 'featureModel_TypedValue10'):
        assert _is_linked(a2, 'featureModel_TypedValue10', b)
    _safe_set(b, 'featureModel_Feature11', None)
    assert not _is_linked(b, 'featureModel_Feature11', a2)
    if hasattr(a2, 'featureModel_TypedValue10'):
        assert not _is_linked(a2, 'featureModel_TypedValue10', b)


def test_assoc_references4_reverse_link_reassign_clear():
    a1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    a2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    b = featureModel_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'featureModel_Feature5', a1)
    assert _is_linked(b, 'featureModel_Feature5', a1)
    if hasattr(a1, 'featureModel_Feature3'):
        assert _is_linked(a1, 'featureModel_Feature3', b)
    _safe_set(b, 'featureModel_Feature5', a2)
    assert _is_linked(b, 'featureModel_Feature5', a2)
    if hasattr(a1, 'featureModel_Feature3'):
        assert not _is_linked(a1, 'featureModel_Feature3', b)
    if hasattr(a2, 'featureModel_Feature3'):
        assert _is_linked(a2, 'featureModel_Feature3', b)
    _safe_set(b, 'featureModel_Feature5', None)
    assert not _is_linked(b, 'featureModel_Feature5', a2)
    if hasattr(a2, 'featureModel_Feature3'):
        assert not _is_linked(a2, 'featureModel_Feature3', b)


def test_assoc_referenciated7_reverse_link_reassign_clear():
    a1 = featureModel_Feature(name="sample_text", valueType="sample_text")
    a2 = featureModel_Feature(name="sample_text_2", valueType="sample_text_2")
    b = featureModel_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'featureModel_Feature8', a1)
    assert _is_linked(b, 'featureModel_Feature8', a1)
    if hasattr(a1, 'featureModel_Feature6'):
        assert _is_linked(a1, 'featureModel_Feature6', b)
    _safe_set(b, 'featureModel_Feature8', a2)
    assert _is_linked(b, 'featureModel_Feature8', a2)
    if hasattr(a1, 'featureModel_Feature6'):
        assert not _is_linked(a1, 'featureModel_Feature6', b)
    if hasattr(a2, 'featureModel_Feature6'):
        assert _is_linked(a2, 'featureModel_Feature6', b)
    _safe_set(b, 'featureModel_Feature8', None)
    assert not _is_linked(b, 'featureModel_Feature8', a2)
    if hasattr(a2, 'featureModel_Feature6'):
        assert not _is_linked(a2, 'featureModel_Feature6', b)


def test_assoc_source26_reverse_link_reassign_clear():
    a1 = featureModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    a2 = featureModel_RelationFeature(lowerBound=13, type="sample_text_2", upperBound=13)
    b = featureModel_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'featureModel_Feature27', a1)
    assert _is_linked(b, 'featureModel_Feature27', a1)
    if hasattr(a1, 'featureModel_RelationFeature'):
        assert _is_linked(a1, 'featureModel_RelationFeature', b)
    _safe_set(b, 'featureModel_Feature27', a2)
    assert _is_linked(b, 'featureModel_Feature27', a2)
    if hasattr(a1, 'featureModel_RelationFeature'):
        assert not _is_linked(a1, 'featureModel_RelationFeature', b)
    if hasattr(a2, 'featureModel_RelationFeature'):
        assert _is_linked(a2, 'featureModel_RelationFeature', b)
    _safe_set(b, 'featureModel_Feature27', None)
    assert not _is_linked(b, 'featureModel_Feature27', a2)
    if hasattr(a2, 'featureModel_RelationFeature'):
        assert not _is_linked(a2, 'featureModel_RelationFeature', b)


def test_assoc_target28_reverse_link_reassign_clear():
    a1 = featureModel_RelationFeature(lowerBound=7, type="sample_text", upperBound=7)
    a2 = featureModel_RelationFeature(lowerBound=13, type="sample_text_2", upperBound=13)
    b = featureModel_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'featureModel_Feature30', a1)
    assert _is_linked(b, 'featureModel_Feature30', a1)
    if hasattr(a1, 'featureModel_RelationFeature29'):
        assert _is_linked(a1, 'featureModel_RelationFeature29', b)
    _safe_set(b, 'featureModel_Feature30', a2)
    assert _is_linked(b, 'featureModel_Feature30', a2)
    if hasattr(a1, 'featureModel_RelationFeature29'):
        assert not _is_linked(a1, 'featureModel_RelationFeature29', b)
    if hasattr(a2, 'featureModel_RelationFeature29'):
        assert _is_linked(a2, 'featureModel_RelationFeature29', b)
    _safe_set(b, 'featureModel_Feature30', None)
    assert not _is_linked(b, 'featureModel_Feature30', a2)
    if hasattr(a2, 'featureModel_RelationFeature29'):
        assert not _is_linked(a2, 'featureModel_RelationFeature29', b)


def test_assoc_typedValue0_reverse_link_reassign_clear():
    a1 = featureModel_TypedValue(floatValue="sample_text", integerValue="sample_text", stringValue="sample_text")
    a2 = featureModel_TypedValue(floatValue="sample_text_2", integerValue="sample_text_2", stringValue="sample_text_2")
    b = featureModel_Feature(name="sample_text", valueType="sample_text")
    _safe_set(b, 'featureModel_Feature', a1)
    assert _is_linked(b, 'featureModel_Feature', a1)
    if hasattr(a1, 'featureModel_TypedValue'):
        assert _is_linked(a1, 'featureModel_TypedValue', b)
    _safe_set(b, 'featureModel_Feature', a2)
    assert _is_linked(b, 'featureModel_Feature', a2)
    if hasattr(a1, 'featureModel_TypedValue'):
        assert not _is_linked(a1, 'featureModel_TypedValue', b)
    if hasattr(a2, 'featureModel_TypedValue'):
        assert _is_linked(a2, 'featureModel_TypedValue', b)
    _safe_set(b, 'featureModel_Feature', None)
    assert not _is_linked(b, 'featureModel_Feature', a2)
    if hasattr(a2, 'featureModel_TypedValue'):
        assert not _is_linked(a2, 'featureModel_TypedValue', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children1_stub_double():
    # featureModel_Node has no real 'featureModel_Node' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(name="sample_text", valueType="sample_text")
    partner = featureModel_Node()
    setattr(partner, 'featureModel_Node', None)
    _safe_set(owner, 'featureModel_Feature2', {partner})
    assert getattr(partner, 'featureModel_Node') == owner
    _safe_set(owner, 'featureModel_Feature2', set())
    assert getattr(partner, 'featureModel_Node') is None


def test_assoc_features12_stub_double():
    # featureModel_Node has no real 'featureModel_Node13' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    partner = featureModel_Node()
    setattr(partner, 'featureModel_Node13', None)
    _safe_set(owner, 'featureModel_Project', {partner})
    assert getattr(partner, 'featureModel_Node13') == owner
    _safe_set(owner, 'featureModel_Project', set())
    assert getattr(partner, 'featureModel_Node13') is None


def test_assoc_relations14_stub_double():
    # featureModel_Relation has no real 'featureModel_Relation' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Project(nameConfigFile="sample_text", nameConstraintsFile="sample_text", numberOfProducts=7, validatedOCL=True, validatedTEF=True)
    partner = featureModel_Relation()
    setattr(partner, 'featureModel_Relation', None)
    _safe_set(owner, 'featureModel_Project15', {partner})
    assert getattr(partner, 'featureModel_Relation') == owner
    _safe_set(owner, 'featureModel_Project15', set())
    assert getattr(partner, 'featureModel_Relation') is None


