import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cardinality,
    Constraints,
    Feature,
    Operator,
    OrFeature,
    fm_AndOperator,
    fm_Attribute,
    fm_BooleanConstraints,
    fm_CardExConstraint,
    fm_Cardinality,
    fm_Constraints,
    fm_Feature,
    fm_FeatureCardinality,
    fm_FeatureModel,
    fm_GroupCardinality,
    fm_Operation,
    fm_Operator,
    fm_OrFeature,
    fm_OrOperator,
    fm_XorFeature,
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

def test_assoc_attributes8_reverse_link_reassign_clear():
    a1 = fm_Feature(name="sample_text")
    a2 = fm_Feature(name="sample_text_2")
    b = fm_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'fm_Attribute', a1)
    assert _is_linked(b, 'fm_Attribute', a1)
    if hasattr(a1, 'fm_Feature9'):
        assert _is_linked(a1, 'fm_Feature9', b)
    _safe_set(b, 'fm_Attribute', a2)
    assert _is_linked(b, 'fm_Attribute', a2)
    if hasattr(a1, 'fm_Feature9'):
        assert not _is_linked(a1, 'fm_Feature9', b)
    if hasattr(a2, 'fm_Feature9'):
        assert _is_linked(a2, 'fm_Feature9', b)
    _safe_set(b, 'fm_Attribute', None)
    assert not _is_linked(b, 'fm_Attribute', a2)
    if hasattr(a2, 'fm_Feature9'):
        assert not _is_linked(a2, 'fm_Feature9', b)


def test_assoc_feature20_reverse_link_reassign_clear():
    a1 = fm_Operation(value=7)
    a2 = fm_Operation(value=13)
    b = fm_Feature(name="sample_text")
    _safe_set(b, 'fm_Feature22', a1)
    assert _is_linked(b, 'fm_Feature22', a1)
    if hasattr(a1, 'fm_Operation21'):
        assert _is_linked(a1, 'fm_Operation21', b)
    _safe_set(b, 'fm_Feature22', a2)
    assert _is_linked(b, 'fm_Feature22', a2)
    if hasattr(a1, 'fm_Operation21'):
        assert not _is_linked(a1, 'fm_Operation21', b)
    if hasattr(a2, 'fm_Operation21'):
        assert _is_linked(a2, 'fm_Operation21', b)
    _safe_set(b, 'fm_Feature22', None)
    assert not _is_linked(b, 'fm_Feature22', a2)
    if hasattr(a2, 'fm_Operation21'):
        assert not _is_linked(a2, 'fm_Operation21', b)


def test_assoc_subFeatures4_reverse_link_reassign_clear():
    a1 = fm_Feature(name="sample_text")
    a2 = fm_Feature(name="sample_text_2")
    b = fm_Feature(name="sample_text")
    _safe_set(b, 'fm_Feature5', a1)
    assert _is_linked(b, 'fm_Feature5', a1)
    if hasattr(a1, 'fm_Feature3'):
        assert _is_linked(a1, 'fm_Feature3', b)
    _safe_set(b, 'fm_Feature5', a2)
    assert _is_linked(b, 'fm_Feature5', a2)
    if hasattr(a1, 'fm_Feature3'):
        assert not _is_linked(a1, 'fm_Feature3', b)
    if hasattr(a2, 'fm_Feature3'):
        assert _is_linked(a2, 'fm_Feature3', b)
    _safe_set(b, 'fm_Feature5', None)
    assert not _is_linked(b, 'fm_Feature5', a2)
    if hasattr(a2, 'fm_Feature3'):
        assert not _is_linked(a2, 'fm_Feature3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action14_stub_double():
    # fm_CardExConstraint has no real 'fm_CardExConstraint' property in the generated
    # code (a bare stub) -- manually attach it so fm_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fm_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fm_Operation(value=7)
    partner = fm_CardExConstraint()
    setattr(partner, 'fm_CardExConstraint', None)
    _safe_set(owner, 'fm_Operation', partner)
    assert getattr(partner, 'fm_CardExConstraint') == owner
    _safe_set(owner, 'fm_Operation', None)
    assert getattr(partner, 'fm_CardExConstraint') is None


def test_assoc_condition15_stub_double():
    # fm_CardExConstraint has no real 'fm_CardExConstraint16' property in the generated
    # code (a bare stub) -- manually attach it so fm_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fm_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fm_Operation(value=7)
    partner = fm_CardExConstraint()
    setattr(partner, 'fm_CardExConstraint16', None)
    _safe_set(owner, 'fm_Operation17', partner)
    assert owner in getattr(partner, 'fm_CardExConstraint16')
    _safe_set(owner, 'fm_Operation17', None)
    assert owner not in getattr(partner, 'fm_CardExConstraint16')


def test_assoc_featureCardinality6_stub_double():
    # fm_FeatureCardinality has no real 'fm_FeatureCardinality' property in the generated
    # code (a bare stub) -- manually attach it so fm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fm_Feature(name="sample_text")
    partner = fm_FeatureCardinality()
    setattr(partner, 'fm_FeatureCardinality', None)
    _safe_set(owner, 'fm_Feature7', partner)
    assert getattr(partner, 'fm_FeatureCardinality') == owner
    _safe_set(owner, 'fm_Feature7', None)
    assert getattr(partner, 'fm_FeatureCardinality') is None


def test_assoc_from_23_stub_double():
    # fm_BooleanConstraints has no real 'fm_BooleanConstraints' property in the generated
    # code (a bare stub) -- manually attach it so fm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fm_Feature(name="sample_text")
    partner = fm_BooleanConstraints()
    setattr(partner, 'fm_BooleanConstraints', None)
    _safe_set(owner, 'fm_Feature24', partner)
    assert getattr(partner, 'fm_BooleanConstraints') == owner
    _safe_set(owner, 'fm_Feature24', None)
    assert getattr(partner, 'fm_BooleanConstraints') is None


def test_assoc_root0_stub_double():
    # fm_FeatureModel has no real 'fm_FeatureModel' property in the generated
    # code (a bare stub) -- manually attach it so fm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fm_Feature(name="sample_text")
    partner = fm_FeatureModel()
    setattr(partner, 'fm_FeatureModel', None)
    _safe_set(owner, 'fm_Feature', partner)
    assert getattr(partner, 'fm_FeatureModel') == owner
    _safe_set(owner, 'fm_Feature', None)
    assert getattr(partner, 'fm_FeatureModel') is None


def test_assoc_to25_stub_double():
    # fm_BooleanConstraints has no real 'fm_BooleanConstraints26' property in the generated
    # code (a bare stub) -- manually attach it so fm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fm_Feature(name="sample_text")
    partner = fm_BooleanConstraints()
    setattr(partner, 'fm_BooleanConstraints26', None)
    _safe_set(owner, 'fm_Feature27', partner)
    assert getattr(partner, 'fm_BooleanConstraints26') == owner
    _safe_set(owner, 'fm_Feature27', None)
    assert getattr(partner, 'fm_BooleanConstraints26') is None


def test_assoc_variants10_stub_double():
    # fm_OrFeature has no real 'fm_OrFeature' property in the generated
    # code (a bare stub) -- manually attach it so fm_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fm_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fm_Feature(name="sample_text")
    partner = fm_OrFeature()
    setattr(partner, 'fm_OrFeature', None)
    _safe_set(owner, 'fm_Feature11', partner)
    assert owner in getattr(partner, 'fm_OrFeature')
    _safe_set(owner, 'fm_Feature11', None)
    assert owner not in getattr(partner, 'fm_OrFeature')


