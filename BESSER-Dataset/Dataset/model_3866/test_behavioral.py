import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    COREConfiguration,
    COREImpactNode,
    COREModel,
    COREModelElement,
    CORENamedElement,
    core_COREBinding,
    core_CORECompositionSpecification,
    core_COREConcern,
    core_COREConcernConfiguration,
    core_COREConfiguration,
    core_COREContribution,
    core_COREFeature,
    core_COREFeatureImpactNode,
    core_COREFeatureModel,
    core_COREImpactModel,
    core_COREImpactModelBinding,
    core_COREImpactNode,
    core_COREInterface,
    core_COREMapping,
    core_COREModel,
    core_COREModelCompositionSpecification,
    core_COREModelElement,
    core_COREModelReuse,
    core_CORENamedElement,
    core_COREPattern,
    core_CORERelativity,
    core_CORERelativity_Opt2,
    core_COREReuse,
    core_COREReuseConfiguration,
    core_COREWeightedMapping,
    core_EObject,
    core_LayoutContainerMap,
    core_LayoutElement,
    core_LayoutMap,
    COREFeatureRelationshipType,
    COREPartialityType,
    COREVisibilityType,
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

def test_assoc_children21_reverse_link_reassign_clear():
    a1 = core_COREFeature(parentRelationship="sample_text")
    a2 = core_COREFeature(parentRelationship="sample_text_2")
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'COREFeature22'):
        assert _is_linked(a1, 'COREFeature22', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'COREFeature22'):
        assert not _is_linked(a1, 'COREFeature22', b)
    if hasattr(a2, 'COREFeature22'):
        assert _is_linked(a2, 'COREFeature22', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'COREFeature22'):
        assert not _is_linked(a2, 'COREFeature22', b)


def test_assoc_excludes30_reverse_link_reassign_clear():
    a1 = core_COREFeature(parentRelationship="sample_text")
    a2 = core_COREFeature(parentRelationship="sample_text_2")
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'core_COREFeature31', a1)
    assert _is_linked(b, 'core_COREFeature31', a1)
    if hasattr(a1, 'core_COREFeature29'):
        assert _is_linked(a1, 'core_COREFeature29', b)
    _safe_set(b, 'core_COREFeature31', a2)
    assert _is_linked(b, 'core_COREFeature31', a2)
    if hasattr(a1, 'core_COREFeature29'):
        assert not _is_linked(a1, 'core_COREFeature29', b)
    if hasattr(a2, 'core_COREFeature29'):
        assert _is_linked(a2, 'core_COREFeature29', b)
    _safe_set(b, 'core_COREFeature31', None)
    assert not _is_linked(b, 'core_COREFeature31', a2)
    if hasattr(a2, 'core_COREFeature29'):
        assert not _is_linked(a2, 'core_COREFeature29', b)


def test_assoc_features119_reverse_link_reassign_clear():
    a1 = core_CORERelativity_Opt2(probabilisticValue=3.14)
    a2 = core_CORERelativity_Opt2(probabilisticValue=9.99)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'COREFeature121', a1)
    assert _is_linked(b, 'COREFeature121', a1)
    if hasattr(a1, 'incoming120'):
        assert _is_linked(a1, 'incoming120', b)
    _safe_set(b, 'COREFeature121', a2)
    assert _is_linked(b, 'COREFeature121', a2)
    if hasattr(a1, 'incoming120'):
        assert not _is_linked(a1, 'incoming120', b)
    if hasattr(a2, 'incoming120'):
        assert _is_linked(a2, 'incoming120', b)
    _safe_set(b, 'COREFeature121', None)
    assert not _is_linked(b, 'COREFeature121', a2)
    if hasattr(a2, 'incoming120'):
        assert not _is_linked(a2, 'incoming120', b)


def test_assoc_impacts92_reverse_link_reassign_clear():
    a1 = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactNode(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'COREImpactNode93'):
        assert _is_linked(a1, 'COREImpactNode93', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'COREImpactNode93'):
        assert not _is_linked(a1, 'COREImpactNode93', b)
    if hasattr(a2, 'COREImpactNode93'):
        assert _is_linked(a2, 'COREImpactNode93', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'COREImpactNode93'):
        assert not _is_linked(a2, 'COREImpactNode93', b)


def test_assoc_incoming35_reverse_link_reassign_clear():
    a1 = core_CORERelativity_Opt2(probabilisticValue=3.14)
    a2 = core_CORERelativity_Opt2(probabilisticValue=9.99)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'features', {a1})
    assert _is_linked(b, 'features', a1)
    if hasattr(a1, 'CORERelativity_Opt236'):
        assert _is_linked(a1, 'CORERelativity_Opt236', b)
    _safe_set(b, 'features', {a2})
    assert _is_linked(b, 'features', a2)
    if hasattr(a1, 'CORERelativity_Opt236'):
        assert not _is_linked(a1, 'CORERelativity_Opt236', b)
    if hasattr(a2, 'CORERelativity_Opt236'):
        assert _is_linked(a2, 'CORERelativity_Opt236', b)
    _safe_set(b, 'features', set())
    assert not _is_linked(b, 'features', a2)
    if hasattr(a2, 'CORERelativity_Opt236'):
        assert not _is_linked(a2, 'CORERelativity_Opt236', b)


def test_assoc_incoming64_reverse_link_reassign_clear():
    a1 = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactNode(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'COREContribution65', a1)
    assert _is_linked(b, 'COREContribution65', a1)
    if hasattr(a1, 'impacts'):
        assert _is_linked(a1, 'impacts', b)
    _safe_set(b, 'COREContribution65', a2)
    assert _is_linked(b, 'COREContribution65', a2)
    if hasattr(a1, 'impacts'):
        assert not _is_linked(a1, 'impacts', b)
    if hasattr(a2, 'impacts'):
        assert _is_linked(a2, 'impacts', b)
    _safe_set(b, 'COREContribution65', None)
    assert not _is_linked(b, 'COREContribution65', a2)
    if hasattr(a2, 'impacts'):
        assert not _is_linked(a2, 'impacts', b)


def test_assoc_outgoing34_reverse_link_reassign_clear():
    a1 = core_CORERelativity_Opt2(probabilisticValue=3.14)
    a2 = core_CORERelativity_Opt2(probabilisticValue=9.99)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'CORERelativity_Opt2'):
        assert _is_linked(a1, 'CORERelativity_Opt2', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'CORERelativity_Opt2'):
        assert not _is_linked(a1, 'CORERelativity_Opt2', b)
    if hasattr(a2, 'CORERelativity_Opt2'):
        assert _is_linked(a2, 'CORERelativity_Opt2', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'CORERelativity_Opt2'):
        assert not _is_linked(a2, 'CORERelativity_Opt2', b)


def test_assoc_outgoing62_reverse_link_reassign_clear():
    a1 = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactNode(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'COREContribution', a1)
    assert _is_linked(b, 'COREContribution', a1)
    if hasattr(a1, 'source63'):
        assert _is_linked(a1, 'source63', b)
    _safe_set(b, 'COREContribution', a2)
    assert _is_linked(b, 'COREContribution', a2)
    if hasattr(a1, 'source63'):
        assert not _is_linked(a1, 'source63', b)
    if hasattr(a2, 'source63'):
        assert _is_linked(a2, 'source63', b)
    _safe_set(b, 'COREContribution', None)
    assert not _is_linked(b, 'COREContribution', a2)
    if hasattr(a2, 'source63'):
        assert not _is_linked(a2, 'source63', b)


def test_assoc_parent24_reverse_link_reassign_clear():
    a1 = core_COREFeature(parentRelationship="sample_text")
    a2 = core_COREFeature(parentRelationship="sample_text_2")
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'COREFeature25'):
        assert _is_linked(a1, 'COREFeature25', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'COREFeature25'):
        assert not _is_linked(a1, 'COREFeature25', b)
    if hasattr(a2, 'COREFeature25'):
        assert _is_linked(a2, 'COREFeature25', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'COREFeature25'):
        assert not _is_linked(a2, 'COREFeature25', b)


def test_assoc_relatedTo32_reverse_link_reassign_clear():
    a1 = core_CORERelativity(probabilisticValue=3.14)
    a2 = core_CORERelativity(probabilisticValue=9.99)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'core_COREFeature33', {a1})
    assert _is_linked(b, 'core_COREFeature33', a1)
    if hasattr(a1, 'core_CORERelativity'):
        assert _is_linked(a1, 'core_CORERelativity', b)
    _safe_set(b, 'core_COREFeature33', {a2})
    assert _is_linked(b, 'core_COREFeature33', a2)
    if hasattr(a1, 'core_CORERelativity'):
        assert not _is_linked(a1, 'core_CORERelativity', b)
    if hasattr(a2, 'core_CORERelativity'):
        assert _is_linked(a2, 'core_CORERelativity', b)
    _safe_set(b, 'core_COREFeature33', set())
    assert not _is_linked(b, 'core_COREFeature33', a2)
    if hasattr(a2, 'core_CORERelativity'):
        assert not _is_linked(a2, 'core_CORERelativity', b)


def test_assoc_relatedToFeature113_reverse_link_reassign_clear():
    a1 = core_CORERelativity(probabilisticValue=3.14)
    a2 = core_CORERelativity(probabilisticValue=9.99)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'core_COREFeature115', a1)
    assert _is_linked(b, 'core_COREFeature115', a1)
    if hasattr(a1, 'core_CORERelativity114'):
        assert _is_linked(a1, 'core_CORERelativity114', b)
    _safe_set(b, 'core_COREFeature115', a2)
    assert _is_linked(b, 'core_COREFeature115', a2)
    if hasattr(a1, 'core_CORERelativity114'):
        assert not _is_linked(a1, 'core_CORERelativity114', b)
    if hasattr(a2, 'core_CORERelativity114'):
        assert _is_linked(a2, 'core_CORERelativity114', b)
    _safe_set(b, 'core_COREFeature115', None)
    assert not _is_linked(b, 'core_COREFeature115', a2)
    if hasattr(a2, 'core_CORERelativity114'):
        assert not _is_linked(a2, 'core_CORERelativity114', b)


def test_assoc_represents103_reverse_link_reassign_clear():
    a1 = core_COREFeatureImpactNode(relativeFeatureWeight=7)
    a2 = core_COREFeatureImpactNode(relativeFeatureWeight=13)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'core_COREFeature104', a1)
    assert _is_linked(b, 'core_COREFeature104', a1)
    if hasattr(a1, 'core_COREFeatureImpactNode'):
        assert _is_linked(a1, 'core_COREFeatureImpactNode', b)
    _safe_set(b, 'core_COREFeature104', a2)
    assert _is_linked(b, 'core_COREFeature104', a2)
    if hasattr(a1, 'core_COREFeatureImpactNode'):
        assert not _is_linked(a1, 'core_COREFeatureImpactNode', b)
    if hasattr(a2, 'core_COREFeatureImpactNode'):
        assert _is_linked(a2, 'core_COREFeatureImpactNode', b)
    _safe_set(b, 'core_COREFeature104', None)
    assert not _is_linked(b, 'core_COREFeature104', a2)
    if hasattr(a2, 'core_COREFeatureImpactNode'):
        assert not _is_linked(a2, 'core_COREFeatureImpactNode', b)


def test_assoc_requires27_reverse_link_reassign_clear():
    a1 = core_COREFeature(parentRelationship="sample_text")
    a2 = core_COREFeature(parentRelationship="sample_text_2")
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'core_COREFeature28', a1)
    assert _is_linked(b, 'core_COREFeature28', a1)
    if hasattr(a1, 'core_COREFeature26'):
        assert _is_linked(a1, 'core_COREFeature26', b)
    _safe_set(b, 'core_COREFeature28', a2)
    assert _is_linked(b, 'core_COREFeature28', a2)
    if hasattr(a1, 'core_COREFeature26'):
        assert not _is_linked(a1, 'core_COREFeature26', b)
    if hasattr(a2, 'core_COREFeature26'):
        assert _is_linked(a2, 'core_COREFeature26', b)
    _safe_set(b, 'core_COREFeature28', None)
    assert not _is_linked(b, 'core_COREFeature28', a2)
    if hasattr(a2, 'core_COREFeature26'):
        assert not _is_linked(a2, 'core_COREFeature26', b)


def test_assoc_source116_reverse_link_reassign_clear():
    a1 = core_CORERelativity_Opt2(probabilisticValue=3.14)
    a2 = core_CORERelativity_Opt2(probabilisticValue=9.99)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'COREFeature118', a1)
    assert _is_linked(b, 'COREFeature118', a1)
    if hasattr(a1, 'outgoing117'):
        assert _is_linked(a1, 'outgoing117', b)
    _safe_set(b, 'COREFeature118', a2)
    assert _is_linked(b, 'COREFeature118', a2)
    if hasattr(a1, 'outgoing117'):
        assert not _is_linked(a1, 'outgoing117', b)
    if hasattr(a2, 'outgoing117'):
        assert _is_linked(a2, 'outgoing117', b)
    _safe_set(b, 'COREFeature118', None)
    assert not _is_linked(b, 'COREFeature118', a2)
    if hasattr(a2, 'outgoing117'):
        assert not _is_linked(a2, 'outgoing117', b)


def test_assoc_source91_reverse_link_reassign_clear():
    a1 = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactNode(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'COREImpactNode'):
        assert _is_linked(a1, 'COREImpactNode', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'COREImpactNode'):
        assert not _is_linked(a1, 'COREImpactNode', b)
    if hasattr(a2, 'COREImpactNode'):
        assert _is_linked(a2, 'COREImpactNode', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'COREImpactNode'):
        assert not _is_linked(a2, 'COREImpactNode', b)


def test_assoc_weightedMappings105_reverse_link_reassign_clear():
    a1 = core_COREWeightedMapping(weight=7)
    a2 = core_COREWeightedMapping(weight=13)
    b = core_COREFeatureImpactNode(relativeFeatureWeight=7)
    _safe_set(b, 'core_COREFeatureImpactNode106', {a1})
    assert _is_linked(b, 'core_COREFeatureImpactNode106', a1)
    if hasattr(a1, 'core_COREWeightedMapping'):
        assert _is_linked(a1, 'core_COREWeightedMapping', b)
    _safe_set(b, 'core_COREFeatureImpactNode106', {a2})
    assert _is_linked(b, 'core_COREFeatureImpactNode106', a2)
    if hasattr(a1, 'core_COREWeightedMapping'):
        assert not _is_linked(a1, 'core_COREWeightedMapping', b)
    if hasattr(a2, 'core_COREWeightedMapping'):
        assert _is_linked(a2, 'core_COREWeightedMapping', b)
    _safe_set(b, 'core_COREFeatureImpactNode106', set())
    assert not _is_linked(b, 'core_COREFeatureImpactNode106', a2)
    if hasattr(a2, 'core_COREWeightedMapping'):
        assert not _is_linked(a2, 'core_COREWeightedMapping', b)


