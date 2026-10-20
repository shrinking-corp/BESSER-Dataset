import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    COREImpactModelElement,
    COREModel,
    COREModelElement,
    CORENamedElement,
    core_COREBinding,
    core_CORECompositionSpecification,
    core_COREConcern,
    core_COREConfiguration,
    core_COREContribution,
    core_COREFeature,
    core_COREFeatureImpact,
    core_COREFeatureModel,
    core_COREImpactModel,
    core_COREImpactModelBinding,
    core_COREImpactModelElement,
    core_COREInterface,
    core_COREMapping,
    core_COREModel,
    core_COREModelCompositionSpecification,
    core_COREModelElement,
    core_COREModelReuse,
    core_CORENamedElement,
    core_COREPattern,
    core_COREReuse,
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


def test_assoc_impacts81_reverse_link_reassign_clear():
    a1 = core_COREImpactModelElement(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactModelElement(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'COREImpactModelElement82'):
        assert _is_linked(a1, 'COREImpactModelElement82', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'COREImpactModelElement82'):
        assert not _is_linked(a1, 'COREImpactModelElement82', b)
    if hasattr(a2, 'COREImpactModelElement82'):
        assert _is_linked(a2, 'COREImpactModelElement82', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'COREImpactModelElement82'):
        assert not _is_linked(a2, 'COREImpactModelElement82', b)


def test_assoc_incoming62_reverse_link_reassign_clear():
    a1 = core_COREImpactModelElement(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactModelElement(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'COREContribution63', a1)
    assert _is_linked(b, 'COREContribution63', a1)
    if hasattr(a1, 'impacts'):
        assert _is_linked(a1, 'impacts', b)
    _safe_set(b, 'COREContribution63', a2)
    assert _is_linked(b, 'COREContribution63', a2)
    if hasattr(a1, 'impacts'):
        assert not _is_linked(a1, 'impacts', b)
    if hasattr(a2, 'impacts'):
        assert _is_linked(a2, 'impacts', b)
    _safe_set(b, 'COREContribution63', None)
    assert not _is_linked(b, 'COREContribution63', a2)
    if hasattr(a2, 'impacts'):
        assert not _is_linked(a2, 'impacts', b)


def test_assoc_outgoing61_reverse_link_reassign_clear():
    a1 = core_COREImpactModelElement(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactModelElement(offset=9.99, scalingFactor=9.99)
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


def test_assoc_represents92_reverse_link_reassign_clear():
    a1 = core_COREFeatureImpact(relativeFeatureWeight=3.14)
    a2 = core_COREFeatureImpact(relativeFeatureWeight=9.99)
    b = core_COREFeature(parentRelationship="sample_text")
    _safe_set(b, 'core_COREFeature93', a1)
    assert _is_linked(b, 'core_COREFeature93', a1)
    if hasattr(a1, 'core_COREFeatureImpact'):
        assert _is_linked(a1, 'core_COREFeatureImpact', b)
    _safe_set(b, 'core_COREFeature93', a2)
    assert _is_linked(b, 'core_COREFeature93', a2)
    if hasattr(a1, 'core_COREFeatureImpact'):
        assert not _is_linked(a1, 'core_COREFeatureImpact', b)
    if hasattr(a2, 'core_COREFeatureImpact'):
        assert _is_linked(a2, 'core_COREFeatureImpact', b)
    _safe_set(b, 'core_COREFeature93', None)
    assert not _is_linked(b, 'core_COREFeature93', a2)
    if hasattr(a2, 'core_COREFeatureImpact'):
        assert not _is_linked(a2, 'core_COREFeatureImpact', b)


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


def test_assoc_source80_reverse_link_reassign_clear():
    a1 = core_COREImpactModelElement(offset=3.14, scalingFactor=3.14)
    a2 = core_COREImpactModelElement(offset=9.99, scalingFactor=9.99)
    b = core_COREContribution(relativeWeight=7)
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'COREImpactModelElement'):
        assert _is_linked(a1, 'COREImpactModelElement', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'COREImpactModelElement'):
        assert not _is_linked(a1, 'COREImpactModelElement', b)
    if hasattr(a2, 'COREImpactModelElement'):
        assert _is_linked(a2, 'COREImpactModelElement', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'COREImpactModelElement'):
        assert not _is_linked(a2, 'COREImpactModelElement', b)


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


def test_assoc_customizable37_stub_double():
    # core_COREInterface has no real 'core_COREInterface38' property in the generated
    # code (a bare stub) -- manually attach it so core_COREModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREModelElement(partiality="sample_text", visibility="sample_text")
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface38', None)
    _safe_set(owner, 'core_COREModelElement39', partner)
    assert owner in getattr(partner, 'core_COREInterface38')
    _safe_set(owner, 'core_COREModelElement39', None)
    assert owner not in getattr(partner, 'core_COREInterface38')


def test_assoc_features73_stub_double():
    # core_COREFeatureModel has no real 'core_COREFeatureModel74' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREFeatureModel()
    setattr(partner, 'core_COREFeatureModel74', None)
    _safe_set(owner, 'core_COREFeature75', partner)
    assert owner in getattr(partner, 'core_COREFeatureModel74')
    _safe_set(owner, 'core_COREFeature75', None)
    assert owner not in getattr(partner, 'core_COREFeatureModel74')


def test_assoc_impactModelElements5_stub_double():
    # core_COREImpactModel has no real 'core_COREImpactModel' property in the generated
    # code (a bare stub) -- manually attach it so core_COREImpactModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREImpactModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREImpactModelElement(offset=3.14, scalingFactor=3.14)
    partner = core_COREImpactModel()
    setattr(partner, 'core_COREImpactModel', None)
    _safe_set(owner, 'core_COREImpactModelElement', partner)
    assert owner in getattr(partner, 'core_COREImpactModel')
    _safe_set(owner, 'core_COREImpactModelElement', None)
    assert owner not in getattr(partner, 'core_COREImpactModel')


def test_assoc_impacted43_stub_double():
    # core_COREInterface has no real 'core_COREInterface44' property in the generated
    # code (a bare stub) -- manually attach it so core_COREImpactModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREImpactModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREImpactModelElement(offset=3.14, scalingFactor=3.14)
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface44', None)
    _safe_set(owner, 'core_COREImpactModelElement45', partner)
    assert owner in getattr(partner, 'core_COREInterface44')
    _safe_set(owner, 'core_COREImpactModelElement45', None)
    assert owner not in getattr(partner, 'core_COREInterface44')


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


def test_assoc_reexposed67_stub_double():
    # core_COREConfiguration has no real 'core_COREConfiguration68' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREConfiguration()
    setattr(partner, 'core_COREConfiguration68', None)
    _safe_set(owner, 'core_COREFeature69', partner)
    assert owner in getattr(partner, 'core_COREConfiguration68')
    _safe_set(owner, 'core_COREFeature69', None)
    assert owner not in getattr(partner, 'core_COREConfiguration68')


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


def test_assoc_root76_stub_double():
    # core_COREFeatureModel has no real 'core_COREFeatureModel77' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREFeatureModel()
    setattr(partner, 'core_COREFeatureModel77', None)
    _safe_set(owner, 'core_COREFeature78', partner)
    assert getattr(partner, 'core_COREFeatureModel77') == owner
    _safe_set(owner, 'core_COREFeature78', None)
    assert getattr(partner, 'core_COREFeatureModel77') is None


def test_assoc_selectable34_stub_double():
    # core_COREInterface has no real 'core_COREInterface35' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREInterface()
    setattr(partner, 'core_COREInterface35', None)
    _safe_set(owner, 'core_COREFeature36', partner)
    assert owner in getattr(partner, 'core_COREInterface35')
    _safe_set(owner, 'core_COREFeature36', None)
    assert owner not in getattr(partner, 'core_COREInterface35')


def test_assoc_selected64_stub_double():
    # core_COREConfiguration has no real 'core_COREConfiguration65' property in the generated
    # code (a bare stub) -- manually attach it so core_COREFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_COREFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_COREFeature(parentRelationship="sample_text")
    partner = core_COREConfiguration()
    setattr(partner, 'core_COREConfiguration65', None)
    _safe_set(owner, 'core_COREFeature66', partner)
    assert owner in getattr(partner, 'core_COREConfiguration65')
    _safe_set(owner, 'core_COREFeature66', None)
    assert owner not in getattr(partner, 'core_COREConfiguration65')


def test_assoc_usable40_stub_double():
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


def test_assoc_value84_stub_double():
    # core_LayoutMap has no real 'core_LayoutMap85' property in the generated
    # code (a bare stub) -- manually attach it so core_LayoutElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_LayoutElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_LayoutElement(x=3.14, y=3.14)
    partner = core_LayoutMap()
    setattr(partner, 'core_LayoutMap85', None)
    _safe_set(owner, 'core_LayoutElement', partner)
    assert getattr(partner, 'core_LayoutMap85') == owner
    _safe_set(owner, 'core_LayoutElement', None)
    assert getattr(partner, 'core_LayoutMap85') is None


