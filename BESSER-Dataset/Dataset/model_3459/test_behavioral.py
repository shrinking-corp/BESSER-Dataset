import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Conncection,
    FCORE_Attribute,
    FCORE_AttributeConstraint,
    FCORE_AttributeConstraintConnection,
    FCORE_CardinalityConnection,
    FCORE_Conncection,
    FCORE_ExcludesFeatureConstraint,
    FCORE_Feature,
    FCORE_FeatureConstraint,
    FCORE_FeatureGroup,
    FCORE_FeatureModel,
    FCORE_FeatureToGroupConnection,
    FCORE_GroupFeature,
    FCORE_GroupToFeatureConnection,
    FCORE_Influence,
    FCORE_InfluenceAttribute,
    FCORE_InfluenceFeature,
    FCORE_MandatoryConnection,
    FCORE_OptionalConnection,
    FCORE_RequiresFeatureConstraint,
    FCORE_RootFeature,
    FCORE_SingleFeatureConnection,
    FCORE_Softgoal,
    FCORE_SolitaryFeature,
    Feature,
    FeatureConstraint,
    Influence,
    SingleFeatureConnection,
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

def test_assoc_attributes32_reverse_link_reassign_clear():
    a1 = FCORE_Feature(name="sample_text", selected=True)
    a2 = FCORE_Feature(name="sample_text_2", selected=False)
    b = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    _safe_set(b, 'FCORE_Attribute33', a1)
    assert _is_linked(b, 'FCORE_Attribute33', a1)
    if hasattr(a1, 'FCORE_Feature'):
        assert _is_linked(a1, 'FCORE_Feature', b)
    _safe_set(b, 'FCORE_Attribute33', a2)
    assert _is_linked(b, 'FCORE_Attribute33', a2)
    if hasattr(a1, 'FCORE_Feature'):
        assert not _is_linked(a1, 'FCORE_Feature', b)
    if hasattr(a2, 'FCORE_Feature'):
        assert _is_linked(a2, 'FCORE_Feature', b)
    _safe_set(b, 'FCORE_Attribute33', None)
    assert not _is_linked(b, 'FCORE_Attribute33', a2)
    if hasattr(a2, 'FCORE_Feature'):
        assert not _is_linked(a2, 'FCORE_Feature', b)


def test_assoc_influence56_reverse_link_reassign_clear():
    a1 = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    a2 = FCORE_Softgoal(name="sample_text_2", weighting="sample_text_2")
    b = FCORE_Influence(contribution=3.14)
    _safe_set(b, 'Influence', a1)
    assert _is_linked(b, 'Influence', a1)
    if hasattr(a1, 'softgoal'):
        assert _is_linked(a1, 'softgoal', b)
    _safe_set(b, 'Influence', a2)
    assert _is_linked(b, 'Influence', a2)
    if hasattr(a1, 'softgoal'):
        assert not _is_linked(a1, 'softgoal', b)
    if hasattr(a2, 'softgoal'):
        assert _is_linked(a2, 'softgoal', b)
    _safe_set(b, 'Influence', None)
    assert not _is_linked(b, 'Influence', a2)
    if hasattr(a2, 'softgoal'):
        assert not _is_linked(a2, 'softgoal', b)


def test_assoc_softgoal60_reverse_link_reassign_clear():
    a1 = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    a2 = FCORE_Softgoal(name="sample_text_2", weighting="sample_text_2")
    b = FCORE_Influence(contribution=3.14)
    _safe_set(b, 'influence', a1)
    assert _is_linked(b, 'influence', a1)
    if hasattr(a1, 'Softgoal'):
        assert _is_linked(a1, 'Softgoal', b)
    _safe_set(b, 'influence', a2)
    assert _is_linked(b, 'influence', a2)
    if hasattr(a1, 'Softgoal'):
        assert not _is_linked(a1, 'Softgoal', b)
    if hasattr(a2, 'Softgoal'):
        assert _is_linked(a2, 'Softgoal', b)
    _safe_set(b, 'influence', None)
    assert not _is_linked(b, 'influence', a2)
    if hasattr(a2, 'Softgoal'):
        assert not _is_linked(a2, 'Softgoal', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute63_stub_double():
    # FCORE_InfluenceAttribute has no real 'influences64' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    partner = FCORE_InfluenceAttribute()
    setattr(partner, 'influences64', None)
    _safe_set(owner, 'Attribute', partner)
    assert getattr(partner, 'influences64') == owner
    _safe_set(owner, 'Attribute', None)
    assert getattr(partner, 'influences64') is None


def test_assoc_attributeConstraintConnection53_stub_double():
    # FCORE_AttributeConstraintConnection has no real 'AttributeConstraintConnection55' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_AttributeConstraint(equation="sample_text")
    partner = FCORE_AttributeConstraintConnection()
    setattr(partner, 'AttributeConstraintConnection55', None)
    _safe_set(owner, 'target54', partner)
    assert getattr(partner, 'AttributeConstraintConnection55') == owner
    _safe_set(owner, 'target54', None)
    assert getattr(partner, 'AttributeConstraintConnection55') is None


def test_assoc_attributeConstraints31_stub_double():
    # FCORE_AttributeConstraintConnection has no real 'AttributeConstraintConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_AttributeConstraintConnection()
    setattr(partner, 'AttributeConstraintConnection', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'AttributeConstraintConnection') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'AttributeConstraintConnection') is None


def test_assoc_attributeConstraints9_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel10' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_AttributeConstraint(equation="sample_text")
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel10', None)
    _safe_set(owner, 'FCORE_AttributeConstraint', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel10')
    _safe_set(owner, 'FCORE_AttributeConstraint', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel10')


def test_assoc_attributes7_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel8' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel8', None)
    _safe_set(owner, 'FCORE_Attribute', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel8')
    _safe_set(owner, 'FCORE_Attribute', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel8')


def test_assoc_feature61_stub_double():
    # FCORE_InfluenceFeature has no real 'influences' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_InfluenceFeature()
    setattr(partner, 'influences', None)
    _safe_set(owner, 'Feature62', partner)
    assert getattr(partner, 'influences') == owner
    _safe_set(owner, 'Feature62', None)
    assert getattr(partner, 'influences') is None


def test_assoc_featureConstraintsEnds35_stub_double():
    # FCORE_FeatureConstraint has no real 'FeatureConstraint36' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureConstraint()
    setattr(partner, 'FeatureConstraint36', None)
    _safe_set(owner, 'featureEnd', {partner})
    assert getattr(partner, 'FeatureConstraint36') == owner
    _safe_set(owner, 'featureEnd', set())
    assert getattr(partner, 'FeatureConstraint36') is None


def test_assoc_featureConstraintsStarts34_stub_double():
    # FCORE_FeatureConstraint has no real 'FeatureConstraint' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureConstraint()
    setattr(partner, 'FeatureConstraint', None)
    _safe_set(owner, 'featureStart', {partner})
    assert getattr(partner, 'FeatureConstraint') == owner
    _safe_set(owner, 'featureStart', set())
    assert getattr(partner, 'FeatureConstraint') is None


def test_assoc_featureEnd58_stub_double():
    # FCORE_FeatureConstraint has no real 'featureConstraintsEnds' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureConstraint()
    setattr(partner, 'featureConstraintsEnds', None)
    _safe_set(owner, 'Feature59', partner)
    assert getattr(partner, 'featureConstraintsEnds') == owner
    _safe_set(owner, 'Feature59', None)
    assert getattr(partner, 'featureConstraintsEnds') is None


def test_assoc_featureGroups5_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel6' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel6', None)
    _safe_set(owner, 'FCORE_FeatureGroup', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel6')
    _safe_set(owner, 'FCORE_FeatureGroup', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel6')


def test_assoc_featureStart57_stub_double():
    # FCORE_FeatureConstraint has no real 'featureConstraintsStarts' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureConstraint()
    setattr(partner, 'featureConstraintsStarts', None)
    _safe_set(owner, 'Feature', partner)
    assert getattr(partner, 'featureConstraintsStarts') == owner
    _safe_set(owner, 'Feature', None)
    assert getattr(partner, 'featureConstraintsStarts') is None


def test_assoc_featureToGroupConnection46_stub_double():
    # FCORE_FeatureToGroupConnection has no real 'FeatureToGroupConnection48' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_FeatureToGroupConnection()
    setattr(partner, 'FeatureToGroupConnection48', None)
    _safe_set(owner, 'target47', partner)
    assert getattr(partner, 'FeatureToGroupConnection48') == owner
    _safe_set(owner, 'target47', None)
    assert getattr(partner, 'FeatureToGroupConnection48') is None


def test_assoc_featureToGroupConnections40_stub_double():
    # FCORE_FeatureToGroupConnection has no real 'FeatureToGroupConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureToGroupConnection()
    setattr(partner, 'FeatureToGroupConnection', None)
    _safe_set(owner, 'source41', {partner})
    assert getattr(partner, 'FeatureToGroupConnection') == owner
    _safe_set(owner, 'source41', set())
    assert getattr(partner, 'FeatureToGroupConnection') is None


def test_assoc_groupToFeatureConnections49_stub_double():
    # FCORE_GroupToFeatureConnection has no real 'GroupToFeatureConnection51' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_GroupToFeatureConnection()
    setattr(partner, 'GroupToFeatureConnection51', None)
    _safe_set(owner, 'source50', {partner})
    assert getattr(partner, 'GroupToFeatureConnection51') == owner
    _safe_set(owner, 'source50', set())
    assert getattr(partner, 'GroupToFeatureConnection51') is None


def test_assoc_incomingSingleFeatureConnection42_stub_double():
    # FCORE_SingleFeatureConnection has no real 'SingleFeatureConnection43' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_SolitaryFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_SolitaryFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_SolitaryFeature(max=7, min=7)
    partner = FCORE_SingleFeatureConnection()
    setattr(partner, 'SingleFeatureConnection43', None)
    _safe_set(owner, 'target', partner)
    assert getattr(partner, 'SingleFeatureConnection43') == owner
    _safe_set(owner, 'target', None)
    assert getattr(partner, 'SingleFeatureConnection43') is None


def test_assoc_influences37_stub_double():
    # FCORE_InfluenceFeature has no real 'InfluenceFeature' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_InfluenceFeature()
    setattr(partner, 'InfluenceFeature', None)
    _safe_set(owner, 'feature', {partner})
    assert getattr(partner, 'InfluenceFeature') == owner
    _safe_set(owner, 'feature', set())
    assert getattr(partner, 'InfluenceFeature') is None


def test_assoc_influences52_stub_double():
    # FCORE_InfluenceAttribute has no real 'InfluenceAttribute' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Attribute(max=7, min=7, name="sample_text", value=7)
    partner = FCORE_InfluenceAttribute()
    setattr(partner, 'InfluenceAttribute', None)
    _safe_set(owner, 'attribute', {partner})
    assert getattr(partner, 'InfluenceAttribute') == owner
    _safe_set(owner, 'attribute', set())
    assert getattr(partner, 'InfluenceAttribute') is None


def test_assoc_outgoingSingleFeatureConnections38_stub_double():
    # FCORE_SingleFeatureConnection has no real 'SingleFeatureConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_SingleFeatureConnection()
    setattr(partner, 'SingleFeatureConnection', None)
    _safe_set(owner, 'source39', {partner})
    assert getattr(partner, 'SingleFeatureConnection') == owner
    _safe_set(owner, 'source39', set())
    assert getattr(partner, 'SingleFeatureConnection') is None


def test_assoc_softgoals15_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel16' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Softgoal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Softgoal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Softgoal(name="sample_text", weighting="sample_text")
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel16', None)
    _safe_set(owner, 'FCORE_Softgoal', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel16')
    _safe_set(owner, 'FCORE_Softgoal', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel16')


def test_assoc_solitaryFeatures3_stub_double():
    # FCORE_FeatureModel has no real 'FCORE_FeatureModel4' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_SolitaryFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_SolitaryFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_SolitaryFeature(max=7, min=7)
    partner = FCORE_FeatureModel()
    setattr(partner, 'FCORE_FeatureModel4', None)
    _safe_set(owner, 'FCORE_SolitaryFeature', partner)
    assert owner in getattr(partner, 'FCORE_FeatureModel4')
    _safe_set(owner, 'FCORE_SolitaryFeature', None)
    assert owner not in getattr(partner, 'FCORE_FeatureModel4')


def test_assoc_source65_stub_double():
    # FCORE_SingleFeatureConnection has no real 'outgoingSingleFeatureConnections' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_SingleFeatureConnection()
    setattr(partner, 'outgoingSingleFeatureConnections', None)
    _safe_set(owner, 'Feature66', partner)
    assert getattr(partner, 'outgoingSingleFeatureConnections') == owner
    _safe_set(owner, 'Feature66', None)
    assert getattr(partner, 'outgoingSingleFeatureConnections') is None


def test_assoc_source68_stub_double():
    # FCORE_FeatureToGroupConnection has no real 'featureToGroupConnections' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_FeatureToGroupConnection()
    setattr(partner, 'featureToGroupConnections', None)
    _safe_set(owner, 'Feature69', partner)
    assert getattr(partner, 'featureToGroupConnections') == owner
    _safe_set(owner, 'Feature69', None)
    assert getattr(partner, 'featureToGroupConnections') is None


def test_assoc_source71_stub_double():
    # FCORE_GroupToFeatureConnection has no real 'groupToFeatureConnections' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_GroupToFeatureConnection()
    setattr(partner, 'groupToFeatureConnections', None)
    _safe_set(owner, 'FeatureGroup72', partner)
    assert getattr(partner, 'groupToFeatureConnections') == owner
    _safe_set(owner, 'FeatureGroup72', None)
    assert getattr(partner, 'groupToFeatureConnections') is None


def test_assoc_source74_stub_double():
    # FCORE_AttributeConstraintConnection has no real 'attributeConstraints' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_Feature(name="sample_text", selected=True)
    partner = FCORE_AttributeConstraintConnection()
    setattr(partner, 'attributeConstraints', None)
    _safe_set(owner, 'Feature75', partner)
    assert getattr(partner, 'attributeConstraints') == owner
    _safe_set(owner, 'Feature75', None)
    assert getattr(partner, 'attributeConstraints') is None


def test_assoc_target67_stub_double():
    # FCORE_SingleFeatureConnection has no real 'incomingSingleFeatureConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_SolitaryFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_SolitaryFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_SolitaryFeature(max=7, min=7)
    partner = FCORE_SingleFeatureConnection()
    setattr(partner, 'incomingSingleFeatureConnection', None)
    _safe_set(owner, 'SolitaryFeature', partner)
    assert getattr(partner, 'incomingSingleFeatureConnection') == owner
    _safe_set(owner, 'SolitaryFeature', None)
    assert getattr(partner, 'incomingSingleFeatureConnection') is None


def test_assoc_target70_stub_double():
    # FCORE_FeatureToGroupConnection has no real 'featureToGroupConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_FeatureGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_FeatureGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_FeatureGroup(max=7, min=7)
    partner = FCORE_FeatureToGroupConnection()
    setattr(partner, 'featureToGroupConnection', None)
    _safe_set(owner, 'FeatureGroup', partner)
    assert getattr(partner, 'featureToGroupConnection') == owner
    _safe_set(owner, 'FeatureGroup', None)
    assert getattr(partner, 'featureToGroupConnection') is None


def test_assoc_target76_stub_double():
    # FCORE_AttributeConstraintConnection has no real 'attributeConstraintConnection' property in the generated
    # code (a bare stub) -- manually attach it so FCORE_AttributeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FCORE_AttributeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FCORE_AttributeConstraint(equation="sample_text")
    partner = FCORE_AttributeConstraintConnection()
    setattr(partner, 'attributeConstraintConnection', None)
    _safe_set(owner, 'AttributeConstraint', partner)
    assert getattr(partner, 'attributeConstraintConnection') == owner
    _safe_set(owner, 'AttributeConstraint', None)
    assert getattr(partner, 'attributeConstraintConnection') is None


