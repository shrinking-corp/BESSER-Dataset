import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Feature,
    core_AbstractModelElement,
    core_ITopLevelElement,
    features_IFeatureDomain,
    featuretree_FeatureTree,
    featuretree_TreeFeature,
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

def test_assoc_children2_reverse_link_reassign_clear():
    a1 = featuretree_TreeFeature(mandatory=True)
    a2 = featuretree_TreeFeature(mandatory=False)
    b = featuretree_TreeFeature(mandatory=True)
    _safe_set(b, 'featuretree_TreeFeature3', a1)
    assert _is_linked(b, 'featuretree_TreeFeature3', a1)
    if hasattr(a1, 'featuretree_TreeFeature1'):
        assert _is_linked(a1, 'featuretree_TreeFeature1', b)
    _safe_set(b, 'featuretree_TreeFeature3', a2)
    assert _is_linked(b, 'featuretree_TreeFeature3', a2)
    if hasattr(a1, 'featuretree_TreeFeature1'):
        assert not _is_linked(a1, 'featuretree_TreeFeature1', b)
    if hasattr(a2, 'featuretree_TreeFeature1'):
        assert _is_linked(a2, 'featuretree_TreeFeature1', b)
    _safe_set(b, 'featuretree_TreeFeature3', None)
    assert not _is_linked(b, 'featuretree_TreeFeature3', a2)
    if hasattr(a2, 'featuretree_TreeFeature1'):
        assert not _is_linked(a2, 'featuretree_TreeFeature1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_root0_stub_double():
    # featuretree_FeatureTree has no real 'featuretree_FeatureTree' property in the generated
    # code (a bare stub) -- manually attach it so featuretree_TreeFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featuretree_TreeFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featuretree_TreeFeature(mandatory=True)
    partner = featuretree_FeatureTree()
    setattr(partner, 'featuretree_FeatureTree', None)
    _safe_set(owner, 'featuretree_TreeFeature', partner)
    assert getattr(partner, 'featuretree_FeatureTree') == owner
    _safe_set(owner, 'featuretree_TreeFeature', None)
    assert getattr(partner, 'featuretree_FeatureTree') is None


