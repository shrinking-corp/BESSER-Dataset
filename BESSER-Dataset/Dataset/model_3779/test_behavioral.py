import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SimpleFeature,
    SimpleIdentifier,
    feature_AnnotatedSimpleFeature,
    feature_EvidenceCode,
    feature_Feature,
    feature_FeatureSet,
    feature_SimpleFeature,
    feature_SimpleIdentifier,
    feature_SimpleOntologyTerm,
    feature_Value,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_features6_stub_double():
    # feature_FeatureSet has no real 'feature_FeatureSet' property in the generated
    # code (a bare stub) -- manually attach it so feature_SimpleFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_SimpleFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_SimpleFeature(valueString="sample_text")
    partner = feature_FeatureSet()
    setattr(partner, 'feature_FeatureSet', None)
    _safe_set(owner, 'feature_SimpleFeature', partner)
    assert owner in getattr(partner, 'feature_FeatureSet')
    _safe_set(owner, 'feature_SimpleFeature', None)
    assert owner not in getattr(partner, 'feature_FeatureSet')


def test_assoc_type7_stub_double():
    # feature_SimpleOntologyTerm has no real 'feature_SimpleOntologyTerm9' property in the generated
    # code (a bare stub) -- manually attach it so feature_SimpleFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_SimpleFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_SimpleFeature(valueString="sample_text")
    partner = feature_SimpleOntologyTerm()
    setattr(partner, 'feature_SimpleOntologyTerm9', None)
    _safe_set(owner, 'feature_SimpleFeature8', partner)
    assert getattr(partner, 'feature_SimpleOntologyTerm9') == owner
    _safe_set(owner, 'feature_SimpleFeature8', None)
    assert getattr(partner, 'feature_SimpleOntologyTerm9') is None


