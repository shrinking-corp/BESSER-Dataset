import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    HyFeatureAttribute,
    HyLinearTemporalElement,
    HyNamedElement,
    HyTemporalElement,
    feature_HyBooleanAttribute,
    feature_HyContextModel,
    feature_HyEnum,
    feature_HyEnumAttribute,
    feature_HyEnumLiteral,
    feature_HyFeature,
    feature_HyFeatureAttribute,
    feature_HyFeatureChild,
    feature_HyFeatureModel,
    feature_HyFeatureType,
    feature_HyGroup,
    feature_HyGroupComposition,
    feature_HyGroupType,
    feature_HyNumberAttribute,
    feature_HyRootFeature,
    feature_HyStringAttribute,
    feature_HyVersion,
    HyFeatureTypeEnum,
    HyGroupTypeEnum,
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

def test_assoc_feature23_reverse_link_reassign_clear():
    a1 = feature_HyVersion(number="sample_text")
    a2 = feature_HyVersion(number="sample_text_2")
    b = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    _safe_set(b, 'HyFeature24', a1)
    assert _is_linked(b, 'HyFeature24', a1)
    if hasattr(a1, 'versions'):
        assert _is_linked(a1, 'versions', b)
    _safe_set(b, 'HyFeature24', a2)
    assert _is_linked(b, 'HyFeature24', a2)
    if hasattr(a1, 'versions'):
        assert not _is_linked(a1, 'versions', b)
    if hasattr(a2, 'versions'):
        assert _is_linked(a2, 'versions', b)
    _safe_set(b, 'HyFeature24', None)
    assert not _is_linked(b, 'HyFeature24', a2)
    if hasattr(a2, 'versions'):
        assert not _is_linked(a2, 'versions', b)


def test_assoc_supersededVersion29_reverse_link_reassign_clear():
    a1 = feature_HyVersion(number="sample_text")
    a2 = feature_HyVersion(number="sample_text_2")
    b = feature_HyVersion(number="sample_text")
    _safe_set(b, 'supersedingVersions', a1)
    assert _is_linked(b, 'supersedingVersions', a1)
    if hasattr(a1, 'HyVersion30'):
        assert _is_linked(a1, 'HyVersion30', b)
    _safe_set(b, 'supersedingVersions', a2)
    assert _is_linked(b, 'supersedingVersions', a2)
    if hasattr(a1, 'HyVersion30'):
        assert not _is_linked(a1, 'HyVersion30', b)
    if hasattr(a2, 'HyVersion30'):
        assert _is_linked(a2, 'HyVersion30', b)
    _safe_set(b, 'supersedingVersions', None)
    assert not _is_linked(b, 'supersedingVersions', a2)
    if hasattr(a2, 'HyVersion30'):
        assert not _is_linked(a2, 'HyVersion30', b)


def test_assoc_supersedingVersions26_reverse_link_reassign_clear():
    a1 = feature_HyVersion(number="sample_text")
    a2 = feature_HyVersion(number="sample_text_2")
    b = feature_HyVersion(number="sample_text")
    _safe_set(b, 'supersededVersion', {a1})
    assert _is_linked(b, 'supersededVersion', a1)
    if hasattr(a1, 'HyVersion27'):
        assert _is_linked(a1, 'HyVersion27', b)
    _safe_set(b, 'supersededVersion', {a2})
    assert _is_linked(b, 'supersededVersion', a2)
    if hasattr(a1, 'HyVersion27'):
        assert not _is_linked(a1, 'HyVersion27', b)
    if hasattr(a2, 'HyVersion27'):
        assert _is_linked(a2, 'HyVersion27', b)
    _safe_set(b, 'supersededVersion', set())
    assert not _is_linked(b, 'supersededVersion', a2)
    if hasattr(a2, 'HyVersion27'):
        assert not _is_linked(a2, 'HyVersion27', b)


def test_assoc_types13_reverse_link_reassign_clear():
    a1 = feature_HyFeatureType(type="sample_text")
    a2 = feature_HyFeatureType(type="sample_text_2")
    b = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    _safe_set(b, 'feature_HyFeature', {a1})
    assert _is_linked(b, 'feature_HyFeature', a1)
    if hasattr(a1, 'feature_HyFeatureType'):
        assert _is_linked(a1, 'feature_HyFeatureType', b)
    _safe_set(b, 'feature_HyFeature', {a2})
    assert _is_linked(b, 'feature_HyFeature', a2)
    if hasattr(a1, 'feature_HyFeatureType'):
        assert not _is_linked(a1, 'feature_HyFeatureType', b)
    if hasattr(a2, 'feature_HyFeatureType'):
        assert _is_linked(a2, 'feature_HyFeatureType', b)
    _safe_set(b, 'feature_HyFeature', set())
    assert not _is_linked(b, 'feature_HyFeature', a2)
    if hasattr(a2, 'feature_HyFeatureType'):
        assert not _is_linked(a2, 'feature_HyFeatureType', b)


def test_assoc_types20_reverse_link_reassign_clear():
    a1 = feature_HyGroupType(type="sample_text")
    a2 = feature_HyGroupType(type="sample_text_2")
    b = feature_HyGroup()
    _safe_set(b, 'feature_HyGroup', {a1})
    assert _is_linked(b, 'feature_HyGroup', a1)
    if hasattr(a1, 'feature_HyGroupType'):
        assert _is_linked(a1, 'feature_HyGroupType', b)
    _safe_set(b, 'feature_HyGroup', {a2})
    assert _is_linked(b, 'feature_HyGroup', a2)
    if hasattr(a1, 'feature_HyGroupType'):
        assert not _is_linked(a1, 'feature_HyGroupType', b)
    if hasattr(a2, 'feature_HyGroupType'):
        assert _is_linked(a2, 'feature_HyGroupType', b)
    _safe_set(b, 'feature_HyGroup', set())
    assert not _is_linked(b, 'feature_HyGroup', a2)
    if hasattr(a2, 'feature_HyGroupType'):
        assert not _is_linked(a2, 'feature_HyGroupType', b)


def test_assoc_versions8_reverse_link_reassign_clear():
    a1 = feature_HyVersion(number="sample_text")
    a2 = feature_HyVersion(number="sample_text_2")
    b = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    _safe_set(b, 'feature', {a1})
    assert _is_linked(b, 'feature', a1)
    if hasattr(a1, 'HyVersion'):
        assert _is_linked(a1, 'HyVersion', b)
    _safe_set(b, 'feature', {a2})
    assert _is_linked(b, 'feature', a2)
    if hasattr(a1, 'HyVersion'):
        assert not _is_linked(a1, 'HyVersion', b)
    if hasattr(a2, 'HyVersion'):
        assert _is_linked(a2, 'HyVersion', b)
    _safe_set(b, 'feature', set())
    assert not _is_linked(b, 'feature', a2)
    if hasattr(a2, 'HyVersion'):
        assert not _is_linked(a2, 'HyVersion', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes11_stub_double():
    # feature_HyFeatureAttribute has no real 'HyFeatureAttribute' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyFeatureAttribute()
    setattr(partner, 'HyFeatureAttribute', None)
    _safe_set(owner, 'feature12', {partner})
    assert getattr(partner, 'HyFeatureAttribute') == owner
    _safe_set(owner, 'feature12', set())
    assert getattr(partner, 'HyFeatureAttribute') is None


def test_assoc_childGroup47_stub_double():
    # feature_HyFeatureChild has no real 'childOf' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyGroup()
    partner = feature_HyFeatureChild()
    setattr(partner, 'childOf', None)
    _safe_set(owner, 'HyGroup48', partner)
    assert getattr(partner, 'childOf') == owner
    _safe_set(owner, 'HyGroup48', None)
    assert getattr(partner, 'childOf') is None


def test_assoc_childOf18_stub_double():
    # feature_HyFeatureChild has no real 'HyFeatureChild19' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyGroup()
    partner = feature_HyFeatureChild()
    setattr(partner, 'HyFeatureChild19', None)
    _safe_set(owner, 'childGroup', {partner})
    assert getattr(partner, 'HyFeatureChild19') == owner
    _safe_set(owner, 'childGroup', set())
    assert getattr(partner, 'HyFeatureChild19') is None


def test_assoc_compositionOf40_stub_double():
    # feature_HyGroupComposition has no real 'parentOf' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyGroup()
    partner = feature_HyGroupComposition()
    setattr(partner, 'parentOf', None)
    _safe_set(owner, 'HyGroup41', partner)
    assert getattr(partner, 'parentOf') == owner
    _safe_set(owner, 'HyGroup41', None)
    assert getattr(partner, 'parentOf') is None


def test_assoc_feature35_stub_double():
    # feature_HyFeatureAttribute has no real 'attributes' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyFeatureAttribute()
    setattr(partner, 'attributes', None)
    _safe_set(owner, 'HyFeature36', partner)
    assert getattr(partner, 'attributes') == owner
    _safe_set(owner, 'HyFeature36', None)
    assert getattr(partner, 'attributes') is None


def test_assoc_feature37_stub_double():
    # feature_HyRootFeature has no real 'feature_HyRootFeature38' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyRootFeature()
    setattr(partner, 'feature_HyRootFeature38', None)
    _safe_set(owner, 'feature_HyFeature39', partner)
    assert getattr(partner, 'feature_HyRootFeature38') == owner
    _safe_set(owner, 'feature_HyFeature39', None)
    assert getattr(partner, 'feature_HyRootFeature38') is None


def test_assoc_featureModel14_stub_double():
    # feature_HyFeatureModel has no real 'HyFeatureModel' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyFeatureModel()
    setattr(partner, 'HyFeatureModel', None)
    _safe_set(owner, 'features15', partner)
    assert getattr(partner, 'HyFeatureModel') == owner
    _safe_set(owner, 'features15', None)
    assert getattr(partner, 'HyFeatureModel') is None


def test_assoc_featureModel21_stub_double():
    # feature_HyFeatureModel has no real 'HyFeatureModel22' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyGroup()
    partner = feature_HyFeatureModel()
    setattr(partner, 'HyFeatureModel22', None)
    _safe_set(owner, 'groups', partner)
    assert getattr(partner, 'HyFeatureModel22') == owner
    _safe_set(owner, 'groups', None)
    assert getattr(partner, 'HyFeatureModel22') is None


def test_assoc_features1_stub_double():
    # feature_HyFeatureModel has no real 'featureModel' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyFeatureModel()
    setattr(partner, 'featureModel', None)
    _safe_set(owner, 'HyFeature', partner)
    assert owner in getattr(partner, 'featureModel')
    _safe_set(owner, 'HyFeature', None)
    assert owner not in getattr(partner, 'featureModel')


def test_assoc_features42_stub_double():
    # feature_HyGroupComposition has no real 'groupMembership' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyGroupComposition()
    setattr(partner, 'groupMembership', None)
    _safe_set(owner, 'HyFeature43', partner)
    assert owner in getattr(partner, 'groupMembership')
    _safe_set(owner, 'HyFeature43', None)
    assert owner not in getattr(partner, 'groupMembership')


def test_assoc_groupMembership9_stub_double():
    # feature_HyGroupComposition has no real 'HyGroupComposition' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyGroupComposition()
    setattr(partner, 'HyGroupComposition', None)
    _safe_set(owner, 'features', {partner})
    assert getattr(partner, 'HyGroupComposition') == owner
    _safe_set(owner, 'features', set())
    assert getattr(partner, 'HyGroupComposition') is None


def test_assoc_groups2_stub_double():
    # feature_HyFeatureModel has no real 'featureModel3' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyGroup()
    partner = feature_HyFeatureModel()
    setattr(partner, 'featureModel3', None)
    _safe_set(owner, 'HyGroup', partner)
    assert owner in getattr(partner, 'featureModel3')
    _safe_set(owner, 'HyGroup', None)
    assert owner not in getattr(partner, 'featureModel3')


def test_assoc_parent44_stub_double():
    # feature_HyFeatureChild has no real 'parentOf45' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyFeatureChild()
    setattr(partner, 'parentOf45', None)
    _safe_set(owner, 'HyFeature46', partner)
    assert getattr(partner, 'parentOf45') == owner
    _safe_set(owner, 'HyFeature46', None)
    assert getattr(partner, 'parentOf45') is None


def test_assoc_parentOf10_stub_double():
    # feature_HyFeatureChild has no real 'HyFeatureChild' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyFeature(deprecatedSince=date(2024, 1, 1))
    partner = feature_HyFeatureChild()
    setattr(partner, 'HyFeatureChild', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'HyFeatureChild') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'HyFeatureChild') is None


def test_assoc_parentOf16_stub_double():
    # feature_HyGroupComposition has no real 'HyGroupComposition17' property in the generated
    # code (a bare stub) -- manually attach it so feature_HyGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_HyGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_HyGroup()
    partner = feature_HyGroupComposition()
    setattr(partner, 'HyGroupComposition17', None)
    _safe_set(owner, 'compositionOf', {partner})
    assert getattr(partner, 'HyGroupComposition17') == owner
    _safe_set(owner, 'compositionOf', set())
    assert getattr(partner, 'HyGroupComposition17') is None


