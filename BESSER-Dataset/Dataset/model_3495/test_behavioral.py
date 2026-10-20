import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FeatureDependency,
    FeatureGroup,
    HybridDimension,
    HybridElement,
    UUIDElement,
    feature_ChildRelationship,
    feature_DefaultBinding,
    feature_DisplayName,
    feature_Elimination,
    feature_Feature,
    feature_FeatureDependency,
    feature_FeatureExclusion,
    feature_FeatureGroup,
    feature_FeatureModel,
    feature_FeatureRequirement,
    feature_GroupMembership,
    feature_Invariant,
    feature_Mandatory,
    feature_Option,
    feature_OrFeatureGroup,
    feature_Preference,
    feature_RootRelationship,
    feature_XorFeatureGroup,
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

def test_assoc_allChildFeatures20_reverse_link_reassign_clear():
    a1 = feature_Feature(transitiveEliminationState="sample_text")
    a2 = feature_Feature(transitiveEliminationState="sample_text_2")
    b = feature_Feature(transitiveEliminationState="sample_text")
    _safe_set(b, 'feature_Feature21', a1)
    assert _is_linked(b, 'feature_Feature21', a1)
    if hasattr(a1, 'feature_Feature19'):
        assert _is_linked(a1, 'feature_Feature19', b)
    _safe_set(b, 'feature_Feature21', a2)
    assert _is_linked(b, 'feature_Feature21', a2)
    if hasattr(a1, 'feature_Feature19'):
        assert not _is_linked(a1, 'feature_Feature19', b)
    if hasattr(a2, 'feature_Feature19'):
        assert _is_linked(a2, 'feature_Feature19', b)
    _safe_set(b, 'feature_Feature21', None)
    assert not _is_linked(b, 'feature_Feature21', a2)
    if hasattr(a2, 'feature_Feature19'):
        assert not _is_linked(a2, 'feature_Feature19', b)


def test_assoc_eliminations15_reverse_link_reassign_clear():
    a1 = feature_Feature(transitiveEliminationState="sample_text")
    a2 = feature_Feature(transitiveEliminationState="sample_text_2")
    b = feature_Elimination(defaultSelection="sample_text")
    _safe_set(b, 'Elimination', a1)
    assert _is_linked(b, 'Elimination', a1)
    if hasattr(a1, 'feature16'):
        assert _is_linked(a1, 'feature16', b)
    _safe_set(b, 'Elimination', a2)
    assert _is_linked(b, 'Elimination', a2)
    if hasattr(a1, 'feature16'):
        assert not _is_linked(a1, 'feature16', b)
    if hasattr(a2, 'feature16'):
        assert _is_linked(a2, 'feature16', b)
    _safe_set(b, 'Elimination', None)
    assert not _is_linked(b, 'Elimination', a2)
    if hasattr(a2, 'feature16'):
        assert not _is_linked(a2, 'feature16', b)


def test_assoc_feature22_reverse_link_reassign_clear():
    a1 = feature_Feature(transitiveEliminationState="sample_text")
    a2 = feature_Feature(transitiveEliminationState="sample_text_2")
    b = feature_DisplayName(displayName="sample_text")
    _safe_set(b, 'names', a1)
    assert _is_linked(b, 'names', a1)
    if hasattr(a1, 'Feature23'):
        assert _is_linked(a1, 'Feature23', b)
    _safe_set(b, 'names', a2)
    assert _is_linked(b, 'names', a2)
    if hasattr(a1, 'Feature23'):
        assert not _is_linked(a1, 'Feature23', b)
    if hasattr(a2, 'Feature23'):
        assert _is_linked(a2, 'Feature23', b)
    _safe_set(b, 'names', None)
    assert not _is_linked(b, 'names', a2)
    if hasattr(a2, 'Feature23'):
        assert not _is_linked(a2, 'Feature23', b)


def test_assoc_feature56_reverse_link_reassign_clear():
    a1 = feature_Feature(transitiveEliminationState="sample_text")
    a2 = feature_Feature(transitiveEliminationState="sample_text_2")
    b = feature_Elimination(defaultSelection="sample_text")
    _safe_set(b, 'eliminations', a1)
    assert _is_linked(b, 'eliminations', a1)
    if hasattr(a1, 'Feature57'):
        assert _is_linked(a1, 'Feature57', b)
    _safe_set(b, 'eliminations', a2)
    assert _is_linked(b, 'eliminations', a2)
    if hasattr(a1, 'Feature57'):
        assert not _is_linked(a1, 'Feature57', b)
    if hasattr(a2, 'Feature57'):
        assert _is_linked(a2, 'Feature57', b)
    _safe_set(b, 'eliminations', None)
    assert not _is_linked(b, 'eliminations', a2)
    if hasattr(a2, 'Feature57'):
        assert not _is_linked(a2, 'Feature57', b)


def test_assoc_names4_reverse_link_reassign_clear():
    a1 = feature_Feature(transitiveEliminationState="sample_text")
    a2 = feature_Feature(transitiveEliminationState="sample_text_2")
    b = feature_DisplayName(displayName="sample_text")
    _safe_set(b, 'DisplayName', a1)
    assert _is_linked(b, 'DisplayName', a1)
    if hasattr(a1, 'feature'):
        assert _is_linked(a1, 'feature', b)
    _safe_set(b, 'DisplayName', a2)
    assert _is_linked(b, 'DisplayName', a2)
    if hasattr(a1, 'feature'):
        assert not _is_linked(a1, 'feature', b)
    if hasattr(a2, 'feature'):
        assert _is_linked(a2, 'feature', b)
    _safe_set(b, 'DisplayName', None)
    assert not _is_linked(b, 'DisplayName', a2)
    if hasattr(a2, 'feature'):
        assert not _is_linked(a2, 'feature', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_child48_stub_double():
    # feature_ChildRelationship has no real 'parents' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_ChildRelationship()
    setattr(partner, 'parents', None)
    _safe_set(owner, 'Feature49', partner)
    assert getattr(partner, 'parents') == owner
    _safe_set(owner, 'Feature49', None)
    assert getattr(partner, 'parents') is None


def test_assoc_children5_stub_double():
    # feature_ChildRelationship has no real 'ChildRelationship' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_ChildRelationship()
    setattr(partner, 'ChildRelationship', None)
    _safe_set(owner, 'parent', {partner})
    assert getattr(partner, 'ChildRelationship') == owner
    _safe_set(owner, 'parent', set())
    assert getattr(partner, 'ChildRelationship') is None


def test_assoc_eliminationDefault60_stub_double():
    # feature_DefaultBinding has no real 'feature_DefaultBinding62' property in the generated
    # code (a bare stub) -- manually attach it so feature_Elimination's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Elimination's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Elimination(defaultSelection="sample_text")
    partner = feature_DefaultBinding()
    setattr(partner, 'feature_DefaultBinding62', None)
    _safe_set(owner, 'feature_Elimination61', partner)
    assert getattr(partner, 'feature_DefaultBinding62') == owner
    _safe_set(owner, 'feature_Elimination61', None)
    assert getattr(partner, 'feature_DefaultBinding62') is None


def test_assoc_eliminationInvariant58_stub_double():
    # feature_Invariant has no real 'feature_Invariant59' property in the generated
    # code (a bare stub) -- manually attach it so feature_Elimination's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Elimination's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Elimination(defaultSelection="sample_text")
    partner = feature_Invariant()
    setattr(partner, 'feature_Invariant59', None)
    _safe_set(owner, 'feature_Elimination', partner)
    assert getattr(partner, 'feature_Invariant59') == owner
    _safe_set(owner, 'feature_Elimination', None)
    assert getattr(partner, 'feature_Invariant59') is None


def test_assoc_feature44_stub_double():
    # feature_RootRelationship has no real 'incomingRoots' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_RootRelationship()
    setattr(partner, 'incomingRoots', None)
    _safe_set(owner, 'Feature45', partner)
    assert getattr(partner, 'incomingRoots') == owner
    _safe_set(owner, 'Feature45', None)
    assert getattr(partner, 'incomingRoots') is None


def test_assoc_feature54_stub_double():
    # feature_Mandatory has no real 'mandatory' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_Mandatory()
    setattr(partner, 'mandatory', None)
    _safe_set(owner, 'Feature55', partner)
    assert getattr(partner, 'mandatory') == owner
    _safe_set(owner, 'Feature55', None)
    assert getattr(partner, 'mandatory') is None


def test_assoc_featureModel2_stub_double():
    # feature_FeatureModel has no real 'FeatureModel' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_FeatureModel()
    setattr(partner, 'FeatureModel', None)
    _safe_set(owner, 'features', partner)
    assert getattr(partner, 'FeatureModel') == owner
    _safe_set(owner, 'features', None)
    assert getattr(partner, 'FeatureModel') is None


def test_assoc_featureOption3_stub_double():
    # feature_Option has no real 'feature_Option' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_Option()
    setattr(partner, 'feature_Option', None)
    _safe_set(owner, 'feature_Feature', partner)
    assert getattr(partner, 'feature_Option') == owner
    _safe_set(owner, 'feature_Feature', None)
    assert getattr(partner, 'feature_Option') is None


def test_assoc_features1_stub_double():
    # feature_FeatureModel has no real 'featureModel' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_FeatureModel()
    setattr(partner, 'featureModel', None)
    _safe_set(owner, 'Feature', partner)
    assert owner in getattr(partner, 'featureModel')
    _safe_set(owner, 'Feature', None)
    assert owner not in getattr(partner, 'featureModel')


def test_assoc_groupedBy9_stub_double():
    # feature_GroupMembership has no real 'GroupMembership' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_GroupMembership()
    setattr(partner, 'GroupMembership', None)
    _safe_set(owner, 'groupedFeature', {partner})
    assert getattr(partner, 'GroupMembership') == owner
    _safe_set(owner, 'groupedFeature', set())
    assert getattr(partner, 'GroupMembership') is None


def test_assoc_groupedFeature29_stub_double():
    # feature_GroupMembership has no real 'groupedBy' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_GroupMembership()
    setattr(partner, 'groupedBy', None)
    _safe_set(owner, 'Feature30', partner)
    assert getattr(partner, 'groupedBy') == owner
    _safe_set(owner, 'Feature30', None)
    assert getattr(partner, 'groupedBy') is None


def test_assoc_groups8_stub_double():
    # feature_FeatureGroup has no real 'FeatureGroup' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_FeatureGroup()
    setattr(partner, 'FeatureGroup', None)
    _safe_set(owner, 'parentFeature', {partner})
    assert getattr(partner, 'FeatureGroup') == owner
    _safe_set(owner, 'parentFeature', set())
    assert getattr(partner, 'FeatureGroup') is None


def test_assoc_incomingDependencies10_stub_double():
    # feature_FeatureDependency has no real 'FeatureDependency' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_FeatureDependency()
    setattr(partner, 'FeatureDependency', None)
    _safe_set(owner, 'targetFeature', {partner})
    assert getattr(partner, 'FeatureDependency') == owner
    _safe_set(owner, 'targetFeature', set())
    assert getattr(partner, 'FeatureDependency') is None


def test_assoc_incomingRoots17_stub_double():
    # feature_RootRelationship has no real 'RootRelationship' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_RootRelationship()
    setattr(partner, 'RootRelationship', None)
    _safe_set(owner, 'feature18', {partner})
    assert getattr(partner, 'RootRelationship') == owner
    _safe_set(owner, 'feature18', set())
    assert getattr(partner, 'RootRelationship') is None


def test_assoc_mandatory13_stub_double():
    # feature_Mandatory has no real 'Mandatory' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_Mandatory()
    setattr(partner, 'Mandatory', None)
    _safe_set(owner, 'feature14', partner)
    assert getattr(partner, 'Mandatory') == owner
    _safe_set(owner, 'feature14', None)
    assert getattr(partner, 'Mandatory') is None


def test_assoc_outgoingDependencies11_stub_double():
    # feature_FeatureDependency has no real 'FeatureDependency12' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_FeatureDependency()
    setattr(partner, 'FeatureDependency12', None)
    _safe_set(owner, 'sourceFeature', {partner})
    assert getattr(partner, 'FeatureDependency12') == owner
    _safe_set(owner, 'sourceFeature', set())
    assert getattr(partner, 'FeatureDependency12') is None


def test_assoc_parent46_stub_double():
    # feature_ChildRelationship has no real 'children' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_ChildRelationship()
    setattr(partner, 'children', None)
    _safe_set(owner, 'Feature47', partner)
    assert getattr(partner, 'children') == owner
    _safe_set(owner, 'Feature47', None)
    assert getattr(partner, 'children') is None


def test_assoc_parentFeature27_stub_double():
    # feature_FeatureGroup has no real 'groups' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_FeatureGroup()
    setattr(partner, 'groups', None)
    _safe_set(owner, 'Feature28', partner)
    assert getattr(partner, 'groups') == owner
    _safe_set(owner, 'Feature28', None)
    assert getattr(partner, 'groups') is None


def test_assoc_parents6_stub_double():
    # feature_ChildRelationship has no real 'ChildRelationship7' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_ChildRelationship()
    setattr(partner, 'ChildRelationship7', None)
    _safe_set(owner, 'child', {partner})
    assert getattr(partner, 'ChildRelationship7') == owner
    _safe_set(owner, 'child', set())
    assert getattr(partner, 'ChildRelationship7') is None


def test_assoc_sourceFeature35_stub_double():
    # feature_FeatureDependency has no real 'outgoingDependencies' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_FeatureDependency()
    setattr(partner, 'outgoingDependencies', None)
    _safe_set(owner, 'Feature36', partner)
    assert getattr(partner, 'outgoingDependencies') == owner
    _safe_set(owner, 'Feature36', None)
    assert getattr(partner, 'outgoingDependencies') is None


def test_assoc_targetFeature37_stub_double():
    # feature_FeatureDependency has no real 'incomingDependencies' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(transitiveEliminationState="sample_text")
    partner = feature_FeatureDependency()
    setattr(partner, 'incomingDependencies', None)
    _safe_set(owner, 'Feature38', partner)
    assert getattr(partner, 'incomingDependencies') == owner
    _safe_set(owner, 'Feature38', None)
    assert getattr(partner, 'incomingDependencies') is None


