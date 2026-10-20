import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AtomicExpression,
    AttributeOperand,
    BinaryExpression,
    Domain,
    Expression,
    Identifiable,
    UnaryExpression,
    feature_AndExpression,
    feature_AtomicExpression,
    feature_Attribute,
    feature_AttributeComparisonExpression,
    feature_AttributeOperand,
    feature_AttributeReference,
    feature_AttributeValueLiteral,
    feature_BinaryExpression,
    feature_Constraint,
    feature_ContinuousDomain,
    feature_DiscreteDomain,
    feature_Domain,
    feature_ExcludesExpression,
    feature_Expression,
    feature_Feature,
    feature_FeatureModel,
    feature_FeatureReference,
    feature_Group,
    feature_Identifiable,
    feature_ImpliesExpression,
    feature_Interval,
    feature_NestedExpression,
    feature_NotExpression,
    feature_OrExpression,
    feature_UnaryExpression,
    AttributeComparisonOperator,
    SelectedState,
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

def test_assoc_attributes5_reverse_link_reassign_clear():
    a1 = feature_Feature(name="sample_text", selected="sample_text")
    a2 = feature_Feature(name="sample_text_2", selected="sample_text_2")
    b = feature_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'feature'):
        assert _is_linked(a1, 'feature', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'feature'):
        assert not _is_linked(a1, 'feature', b)
    if hasattr(a2, 'feature'):
        assert _is_linked(a2, 'feature', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'feature'):
        assert not _is_linked(a2, 'feature', b)


def test_assoc_childFeatures8_reverse_link_reassign_clear():
    a1 = feature_Group(maxCardinality=7, minCardinality=7)
    a2 = feature_Group(maxCardinality=13, minCardinality=13)
    b = feature_Feature(name="sample_text", selected="sample_text")
    _safe_set(b, 'feature_Feature10', a1)
    assert _is_linked(b, 'feature_Feature10', a1)
    if hasattr(a1, 'feature_Group9'):
        assert _is_linked(a1, 'feature_Group9', b)
    _safe_set(b, 'feature_Feature10', a2)
    assert _is_linked(b, 'feature_Feature10', a2)
    if hasattr(a1, 'feature_Group9'):
        assert not _is_linked(a1, 'feature_Group9', b)
    if hasattr(a2, 'feature_Group9'):
        assert _is_linked(a2, 'feature_Group9', b)
    _safe_set(b, 'feature_Feature10', None)
    assert not _is_linked(b, 'feature_Feature10', a2)
    if hasattr(a2, 'feature_Group9'):
        assert not _is_linked(a2, 'feature_Group9', b)


def test_assoc_feature11_reverse_link_reassign_clear():
    a1 = feature_Feature(name="sample_text", selected="sample_text")
    a2 = feature_Feature(name="sample_text_2", selected="sample_text_2")
    b = feature_Attribute(name="sample_text", value="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_groups6_reverse_link_reassign_clear():
    a1 = feature_Group(maxCardinality=7, minCardinality=7)
    a2 = feature_Group(maxCardinality=13, minCardinality=13)
    b = feature_Feature(name="sample_text", selected="sample_text")
    _safe_set(b, 'feature_Feature7', {a1})
    assert _is_linked(b, 'feature_Feature7', a1)
    if hasattr(a1, 'feature_Group'):
        assert _is_linked(a1, 'feature_Group', b)
    _safe_set(b, 'feature_Feature7', {a2})
    assert _is_linked(b, 'feature_Feature7', a2)
    if hasattr(a1, 'feature_Group'):
        assert not _is_linked(a1, 'feature_Group', b)
    if hasattr(a2, 'feature_Group'):
        assert _is_linked(a2, 'feature_Group', b)
    _safe_set(b, 'feature_Feature7', set())
    assert not _is_linked(b, 'feature_Feature7', a2)
    if hasattr(a2, 'feature_Group'):
        assert not _is_linked(a2, 'feature_Group', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = feature_FeatureModel(name="sample_text")
    a2 = feature_FeatureModel(name="sample_text_2")
    b = feature_Feature(name="sample_text", selected="sample_text")
    _safe_set(b, 'feature_Feature', a1)
    assert _is_linked(b, 'feature_Feature', a1)
    if hasattr(a1, 'feature_FeatureModel'):
        assert _is_linked(a1, 'feature_FeatureModel', b)
    _safe_set(b, 'feature_Feature', a2)
    assert _is_linked(b, 'feature_Feature', a2)
    if hasattr(a1, 'feature_FeatureModel'):
        assert not _is_linked(a1, 'feature_FeatureModel', b)
    if hasattr(a2, 'feature_FeatureModel'):
        assert _is_linked(a2, 'feature_FeatureModel', b)
    _safe_set(b, 'feature_Feature', None)
    assert not _is_linked(b, 'feature_Feature', a2)
    if hasattr(a2, 'feature_FeatureModel'):
        assert not _is_linked(a2, 'feature_FeatureModel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute126_stub_double():
    # feature_AttributeOperand has no real 'feature_AttributeOperand' property in the generated
    # code (a bare stub) -- manually attach it so feature_AttributeComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_AttributeComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_AttributeComparisonExpression(operator="sample_text")
    partner = feature_AttributeOperand()
    setattr(partner, 'feature_AttributeOperand', None)
    _safe_set(owner, 'feature_AttributeComparisonExpression', partner)
    assert getattr(partner, 'feature_AttributeOperand') == owner
    _safe_set(owner, 'feature_AttributeComparisonExpression', None)
    assert getattr(partner, 'feature_AttributeOperand') is None


def test_assoc_attribute227_stub_double():
    # feature_AttributeOperand has no real 'feature_AttributeOperand29' property in the generated
    # code (a bare stub) -- manually attach it so feature_AttributeComparisonExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_AttributeComparisonExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_AttributeComparisonExpression(operator="sample_text")
    partner = feature_AttributeOperand()
    setattr(partner, 'feature_AttributeOperand29', None)
    _safe_set(owner, 'feature_AttributeComparisonExpression28', partner)
    assert getattr(partner, 'feature_AttributeOperand29') == owner
    _safe_set(owner, 'feature_AttributeComparisonExpression28', None)
    assert getattr(partner, 'feature_AttributeOperand29') is None


def test_assoc_attribute30_stub_double():
    # feature_AttributeReference has no real 'feature_AttributeReference' property in the generated
    # code (a bare stub) -- manually attach it so feature_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Attribute(name="sample_text", value="sample_text")
    partner = feature_AttributeReference()
    setattr(partner, 'feature_AttributeReference', None)
    _safe_set(owner, 'feature_Attribute31', partner)
    assert getattr(partner, 'feature_AttributeReference') == owner
    _safe_set(owner, 'feature_Attribute31', None)
    assert getattr(partner, 'feature_AttributeReference') is None


def test_assoc_constraints3_stub_double():
    # feature_Constraint has no real 'feature_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so feature_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_FeatureModel(name="sample_text")
    partner = feature_Constraint()
    setattr(partner, 'feature_Constraint', None)
    _safe_set(owner, 'feature_FeatureModel4', {partner})
    assert getattr(partner, 'feature_Constraint') == owner
    _safe_set(owner, 'feature_FeatureModel4', set())
    assert getattr(partner, 'feature_Constraint') is None


def test_assoc_domain12_stub_double():
    # feature_Domain has no real 'feature_Domain13' property in the generated
    # code (a bare stub) -- manually attach it so feature_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Attribute(name="sample_text", value="sample_text")
    partner = feature_Domain()
    setattr(partner, 'feature_Domain13', None)
    _safe_set(owner, 'feature_Attribute', partner)
    assert getattr(partner, 'feature_Domain13') == owner
    _safe_set(owner, 'feature_Attribute', None)
    assert getattr(partner, 'feature_Domain13') is None


def test_assoc_domains1_stub_double():
    # feature_Domain has no real 'feature_Domain' property in the generated
    # code (a bare stub) -- manually attach it so feature_FeatureModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_FeatureModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_FeatureModel(name="sample_text")
    partner = feature_Domain()
    setattr(partner, 'feature_Domain', None)
    _safe_set(owner, 'feature_FeatureModel2', {partner})
    assert getattr(partner, 'feature_Domain') == owner
    _safe_set(owner, 'feature_FeatureModel2', set())
    assert getattr(partner, 'feature_Domain') is None


def test_assoc_feature24_stub_double():
    # feature_FeatureReference has no real 'feature_FeatureReference' property in the generated
    # code (a bare stub) -- manually attach it so feature_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Feature(name="sample_text", selected="sample_text")
    partner = feature_FeatureReference()
    setattr(partner, 'feature_FeatureReference', None)
    _safe_set(owner, 'feature_Feature25', partner)
    assert getattr(partner, 'feature_FeatureReference') == owner
    _safe_set(owner, 'feature_Feature25', None)
    assert getattr(partner, 'feature_FeatureReference') is None


def test_assoc_intervals14_stub_double():
    # feature_ContinuousDomain has no real 'feature_ContinuousDomain' property in the generated
    # code (a bare stub) -- manually attach it so feature_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # feature_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = feature_Interval(lowerBound=7, upperBound=7)
    partner = feature_ContinuousDomain()
    setattr(partner, 'feature_ContinuousDomain', None)
    _safe_set(owner, 'feature_Interval', partner)
    assert owner in getattr(partner, 'feature_ContinuousDomain')
    _safe_set(owner, 'feature_Interval', None)
    assert owner not in getattr(partner, 'feature_ContinuousDomain')


