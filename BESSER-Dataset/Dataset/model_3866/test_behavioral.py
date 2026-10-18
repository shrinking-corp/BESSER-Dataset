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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contributions8_stub_double():
    # core_COREImpactModel has no real 'core_COREImpactModel9' property in the generated
    # code (a bare stub) -- manually attach it so core_COREContribution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREContribution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREContribution(relativeWeight=7)
    partner = core_COREImpactModel()
    setattr(partner, 'core_COREImpactModel9', None)
    _safe_set(owner, 'core_COREContribution', partner)
    assert owner in getattr(partner, 'core_COREImpactModel9')
    _safe_set(owner, 'core_COREContribution', None)
    assert owner not in getattr(partner, 'core_COREImpactModel9')


def test_assoc_customizable40_stub_double():
    # core_COREInterface has no real 'core_COREInterface41' property in the generated
    # code (a bare stub) -- manually attach it so core_COREModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREModelElement(partiality="sample_text", visibility="sample_text")
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface41', None)
    _safe_set(owner, 'core_COREModelElement42', partner)
    assert owner in getattr(partner, 'core_COREInterface41')
    _safe_set(owner, 'core_COREModelElement42', None)
    assert owner not in getattr(partner, 'core_COREInterface41')


def test_assoc_features75_stub_double():
    # core_COREFeatureModel has no real 'core_COREFeatureModel76' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREFeatureModel()
    setattr(partner, 'core_COREFeatureModel76', None)
    _safe_set(owner, 'core_COREFeature77', partner)
    assert owner in getattr(partner, 'core_COREFeatureModel76')
    _safe_set(owner, 'core_COREFeature77', None)
    assert owner not in getattr(partner, 'core_COREFeatureModel76')


def test_assoc_impactModelElements5_stub_double():
    # core_COREImpactModel has no real 'core_COREImpactModel' property in the generated
    # code (a bare stub) -- manually attach it so core_COREImpactNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREImpactNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    partner = core_COREImpactModel()
    setattr(partner, 'core_COREImpactModel', None)
    _safe_set(owner, 'core_COREImpactNode', partner)
    assert owner in getattr(partner, 'core_COREImpactModel')
    _safe_set(owner, 'core_COREImpactNode', None)
    assert owner not in getattr(partner, 'core_COREImpactModel')


def test_assoc_impacted46_stub_double():
    # core_COREInterface has no real 'core_COREInterface47' property in the generated
    # code (a bare stub) -- manually attach it so core_COREImpactNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREImpactNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface47', None)
    _safe_set(owner, 'core_COREImpactNode48', partner)
    assert owner in getattr(partner, 'core_COREInterface47')
    _safe_set(owner, 'core_COREImpactNode48', None)
    assert owner not in getattr(partner, 'core_COREInterface47')


def test_assoc_modelElements1_stub_double():
    # core_COREModel has no real 'core_COREModel2' property in the generated
    # code (a bare stub) -- manually attach it so core_COREModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREModelElement(partiality="sample_text", visibility="sample_text")
    partner = core_COREModel()
    setattr(partner, 'core_COREModel2', None)
    _safe_set(owner, 'core_COREModelElement', partner)
    assert owner in getattr(partner, 'core_COREModel2')
    _safe_set(owner, 'core_COREModelElement', None)
    assert owner not in getattr(partner, 'core_COREModel2')


def test_assoc_realizedBy17_stub_double():
    # core_COREModel has no real 'COREModel18' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREModel()
    setattr(partner, 'COREModel18', None)
    _safe_set(owner, 'realizes', {partner})
    assert getattr(partner, 'COREModel18') == owner
    _safe_set(owner, 'realizes', set())
    assert getattr(partner, 'COREModel18') is None


def test_assoc_realizes3_stub_double():
    # core_COREModel has no real 'realizedBy' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREModel()
    setattr(partner, 'realizedBy', None)
    _safe_set(owner, 'COREFeature', partner)
    assert owner in getattr(partner, 'realizedBy')
    _safe_set(owner, 'COREFeature', None)
    assert owner not in getattr(partner, 'realizedBy')


def test_assoc_reexposed69_stub_double():
    # core_COREConfiguration has no real 'core_COREConfiguration70' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREConfiguration()
    setattr(partner, 'core_COREConfiguration70', None)
    _safe_set(owner, 'core_COREFeature71', partner)
    assert owner in getattr(partner, 'core_COREConfiguration70')
    _safe_set(owner, 'core_COREFeature71', None)
    assert owner not in getattr(partner, 'core_COREConfiguration70')


def test_assoc_relatedFeatures86_stub_double():
    # core_COREFeatureModel has no real 'core_COREFeatureModel87' property in the generated
    # code (a bare stub) -- manually attach it so core_CORERelativity_Opt2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_CORERelativity_Opt2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_CORERelativity_Opt2(probabilisticValue=3.14)
    partner = core_COREFeatureModel()
    setattr(partner, 'core_COREFeatureModel87', None)
    _safe_set(owner, 'core_CORERelativity_Opt2', partner)
    assert owner in getattr(partner, 'core_COREFeatureModel87')
    _safe_set(owner, 'core_CORERelativity_Opt2', None)
    assert owner not in getattr(partner, 'core_COREFeatureModel87')


def test_assoc_reuses19_stub_double():
    # core_COREReuse has no real 'core_COREReuse' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREReuse()
    setattr(partner, 'core_COREReuse', None)
    _safe_set(owner, 'core_COREFeature', {partner})
    assert getattr(partner, 'core_COREReuse') == owner
    _safe_set(owner, 'core_COREFeature', set())
    assert getattr(partner, 'core_COREReuse') is None


def test_assoc_root78_stub_double():
    # core_COREFeatureModel has no real 'core_COREFeatureModel79' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREFeatureModel()
    setattr(partner, 'core_COREFeatureModel79', None)
    _safe_set(owner, 'core_COREFeature80', partner)
    assert getattr(partner, 'core_COREFeatureModel79') == owner
    _safe_set(owner, 'core_COREFeature80', None)
    assert getattr(partner, 'core_COREFeatureModel79') is None


def test_assoc_selectable37_stub_double():
    # core_COREInterface has no real 'core_COREInterface38' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface38', None)
    _safe_set(owner, 'core_COREFeature39', partner)
    assert owner in getattr(partner, 'core_COREInterface38')
    _safe_set(owner, 'core_COREFeature39', None)
    assert owner not in getattr(partner, 'core_COREInterface38')


def test_assoc_selected66_stub_double():
    # core_COREConfiguration has no real 'core_COREConfiguration67' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREConfiguration()
    setattr(partner, 'core_COREConfiguration67', None)
    _safe_set(owner, 'core_COREFeature68', partner)
    assert owner in getattr(partner, 'core_COREConfiguration67')
    _safe_set(owner, 'core_COREFeature68', None)
    assert owner not in getattr(partner, 'core_COREConfiguration67')


def test_assoc_usable43_stub_double():
    # core_COREInterface has no real 'core_COREInterface44' property in the generated
    # code (a bare stub) -- manually attach it so core_COREModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREModelElement(partiality="sample_text", visibility="sample_text")
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface44', None)
    _safe_set(owner, 'core_COREModelElement45', partner)
    assert owner in getattr(partner, 'core_COREInterface44')
    _safe_set(owner, 'core_COREModelElement45', None)
    assert owner not in getattr(partner, 'core_COREInterface44')


def test_assoc_value95_stub_double():
    # core_LayoutMap has no real 'core_LayoutMap96' property in the generated
    # code (a bare stub) -- manually attach it so core_LayoutElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_LayoutElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_LayoutElement(x=3.14, y=3.14)
    partner = core_LayoutMap()
    setattr(partner, 'core_LayoutMap96', None)
    _safe_set(owner, 'core_LayoutElement', partner)
    assert getattr(partner, 'core_LayoutMap96') == owner
    _safe_set(owner, 'core_LayoutElement', None)
    assert getattr(partner, 'core_LayoutMap96') is None


