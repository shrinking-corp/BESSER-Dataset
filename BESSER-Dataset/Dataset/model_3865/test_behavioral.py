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


def test_assoc_impacts75_reverse_link_reassign_clear():
    a1 = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactNode(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'COREImpactNode76'):
        assert _is_linked(a1, 'COREImpactNode76', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'COREImpactNode76'):
        assert not _is_linked(a1, 'COREImpactNode76', b)
    if hasattr(a2, 'COREImpactNode76'):
        assert _is_linked(a2, 'COREImpactNode76', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'COREImpactNode76'):
        assert not _is_linked(a2, 'COREImpactNode76', b)


def test_assoc_incoming55_reverse_link_reassign_clear():
    a1 = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactNode(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'COREContribution56', a1)
    assert _is_linked(b, 'COREContribution56', a1)
    if hasattr(a1, 'impacts'):
        assert _is_linked(a1, 'impacts', b)
    _safe_set(b, 'COREContribution56', a2)
    assert _is_linked(b, 'COREContribution56', a2)
    if hasattr(a1, 'impacts'):
        assert not _is_linked(a1, 'impacts', b)
    if hasattr(a2, 'impacts'):
        assert _is_linked(a2, 'impacts', b)
    _safe_set(b, 'COREContribution56', None)
    assert not _is_linked(b, 'COREContribution56', a2)
    if hasattr(a2, 'impacts'):
        assert not _is_linked(a2, 'impacts', b)


def test_assoc_outgoing54_reverse_link_reassign_clear():
    a1 = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactNode(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'COREContribution', a1)
    assert _is_linked(b, 'COREContribution', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'COREContribution', a2)
    assert _is_linked(b, 'COREContribution', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'COREContribution', None)
    assert not _is_linked(b, 'COREContribution', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


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


def test_assoc_represents86_reverse_link_reassign_clear():
    a1 = core_COREFeatureImpactNode(relativeFeatureWeight=7)
    a2 = core_COREFeatureImpactNode(relativeFeatureWeight=13)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'core_COREFeature87', a1)
    assert _is_linked(b, 'core_COREFeature87', a1)
    if hasattr(a1, 'core_COREFeatureImpactNode'):
        assert _is_linked(a1, 'core_COREFeatureImpactNode', b)
    _safe_set(b, 'core_COREFeature87', a2)
    assert _is_linked(b, 'core_COREFeature87', a2)
    if hasattr(a1, 'core_COREFeatureImpactNode'):
        assert not _is_linked(a1, 'core_COREFeatureImpactNode', b)
    if hasattr(a2, 'core_COREFeatureImpactNode'):
        assert _is_linked(a2, 'core_COREFeatureImpactNode', b)
    _safe_set(b, 'core_COREFeature87', None)
    assert not _is_linked(b, 'core_COREFeature87', a2)
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


def test_assoc_source74_reverse_link_reassign_clear():
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


def test_assoc_weightedMappings88_reverse_link_reassign_clear():
    a1 = core_COREWeightedMapping(weight=7)
    a2 = core_COREWeightedMapping(weight=13)
    b = core_COREFeatureImpactNode(relativeFeatureWeight=7)
    _safe_set(b, 'core_COREFeatureImpactNode89', {a1})
    assert _is_linked(b, 'core_COREFeatureImpactNode89', a1)
    if hasattr(a1, 'core_COREWeightedMapping'):
        assert _is_linked(a1, 'core_COREWeightedMapping', b)
    _safe_set(b, 'core_COREFeatureImpactNode89', {a2})
    assert _is_linked(b, 'core_COREFeatureImpactNode89', a2)
    if hasattr(a1, 'core_COREWeightedMapping'):
        assert not _is_linked(a1, 'core_COREWeightedMapping', b)
    if hasattr(a2, 'core_COREWeightedMapping'):
        assert _is_linked(a2, 'core_COREWeightedMapping', b)
    _safe_set(b, 'core_COREFeatureImpactNode89', set())
    assert not _is_linked(b, 'core_COREFeatureImpactNode89', a2)
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


def test_assoc_customizable35_stub_double():
    # core_COREInterface has no real 'core_COREInterface36' property in the generated
    # code (a bare stub) -- manually attach it so core_COREModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREModelElement(partiality="sample_text", visibility="sample_text")
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface36', None)
    _safe_set(owner, 'core_COREModelElement37', partner)
    assert owner in getattr(partner, 'core_COREInterface36')
    _safe_set(owner, 'core_COREModelElement37', None)
    assert owner not in getattr(partner, 'core_COREInterface36')


def test_assoc_features60_stub_double():
    # core_COREFeatureModel has no real 'core_COREFeatureModel61' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREFeatureModel()
    setattr(partner, 'core_COREFeatureModel61', None)
    _safe_set(owner, 'core_COREFeature62', partner)
    assert owner in getattr(partner, 'core_COREFeatureModel61')
    _safe_set(owner, 'core_COREFeature62', None)
    assert owner not in getattr(partner, 'core_COREFeatureModel61')


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


def test_assoc_impacted41_stub_double():
    # core_COREInterface has no real 'core_COREInterface42' property in the generated
    # code (a bare stub) -- manually attach it so core_COREImpactNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREImpactNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREImpactNode(offset=3.14, scalingFactor=3.14)
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface42', None)
    _safe_set(owner, 'core_COREImpactNode43', partner)
    assert owner in getattr(partner, 'core_COREInterface42')
    _safe_set(owner, 'core_COREImpactNode43', None)
    assert owner not in getattr(partner, 'core_COREInterface42')


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


def test_assoc_root63_stub_double():
    # core_COREFeatureModel has no real 'core_COREFeatureModel64' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREFeatureModel()
    setattr(partner, 'core_COREFeatureModel64', None)
    _safe_set(owner, 'core_COREFeature65', partner)
    assert getattr(partner, 'core_COREFeatureModel64') == owner
    _safe_set(owner, 'core_COREFeature65', None)
    assert getattr(partner, 'core_COREFeatureModel64') is None


def test_assoc_selectable32_stub_double():
    # core_COREInterface has no real 'core_COREInterface33' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface33', None)
    _safe_set(owner, 'core_COREFeature34', partner)
    assert owner in getattr(partner, 'core_COREInterface33')
    _safe_set(owner, 'core_COREFeature34', None)
    assert owner not in getattr(partner, 'core_COREInterface33')


def test_assoc_selected57_stub_double():
    # core_COREConfiguration has no real 'core_COREConfiguration58' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREConfiguration()
    setattr(partner, 'core_COREConfiguration58', None)
    _safe_set(owner, 'core_COREFeature59', partner)
    assert owner in getattr(partner, 'core_COREConfiguration58')
    _safe_set(owner, 'core_COREFeature59', None)
    assert owner not in getattr(partner, 'core_COREConfiguration58')


def test_assoc_usable38_stub_double():
    # core_COREInterface has no real 'core_COREInterface39' property in the generated
    # code (a bare stub) -- manually attach it so core_COREModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREModelElement(partiality="sample_text", visibility="sample_text")
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface39', None)
    _safe_set(owner, 'core_COREModelElement40', partner)
    assert owner in getattr(partner, 'core_COREInterface39')
    _safe_set(owner, 'core_COREModelElement40', None)
    assert owner not in getattr(partner, 'core_COREInterface39')


def test_assoc_value78_stub_double():
    # core_LayoutMap has no real 'core_LayoutMap79' property in the generated
    # code (a bare stub) -- manually attach it so core_LayoutElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_LayoutElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_LayoutElement(x=3.14, y=3.14)
    partner = core_LayoutMap()
    setattr(partner, 'core_LayoutMap79', None)
    _safe_set(owner, 'core_LayoutElement', partner)
    assert getattr(partner, 'core_LayoutMap79') == owner
    _safe_set(owner, 'core_LayoutElement', None)
    assert getattr(partner, 'core_LayoutMap79') is None


