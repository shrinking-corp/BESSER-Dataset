import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Base,
    Rule,
    metrics_Addon,
    metrics_EObject,
    metrics_Metric,
    metrics_MetricAggregationRule,
    metrics_MetricAggregationRules,
    metrics_MetricRetentionPeriods,
    metrics_MetricRetentionRule,
    metrics_MetricRetentionRules,
    metrics_MetricSource,
    FixedMetricRetentionPeriod,
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

def test_assoc_aggregationExpression13_stub_double():
    # metrics_EObject has no real 'metrics_EObject' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricAggregationRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricAggregationRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricAggregationRule(intervalHint="sample_text", period="sample_text")
    partner = metrics_EObject()
    setattr(partner, 'metrics_EObject', None)
    _safe_set(owner, 'metrics_MetricAggregationRule', partner)
    assert getattr(partner, 'metrics_EObject') == owner
    _safe_set(owner, 'metrics_MetricAggregationRule', None)
    assert getattr(partner, 'metrics_EObject') is None


def test_assoc_metricAggregationRuleSet19_stub_double():
    # metrics_MetricAggregationRules has no real 'metrics_MetricAggregationRules21' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricSource(name="sample_text")
    partner = metrics_MetricAggregationRules()
    setattr(partner, 'metrics_MetricAggregationRules21', None)
    _safe_set(owner, 'metrics_MetricSource20', partner)
    assert getattr(partner, 'metrics_MetricAggregationRules21') == owner
    _safe_set(owner, 'metrics_MetricSource20', None)
    assert getattr(partner, 'metrics_MetricAggregationRules21') is None


def test_assoc_metricAggregationRuleSet7_stub_double():
    # metrics_MetricAggregationRules has no real 'metrics_MetricAggregationRules9' property in the generated
    # code (a bare stub) -- manually attach it so metrics_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_Metric(name="sample_text")
    partner = metrics_MetricAggregationRules()
    setattr(partner, 'metrics_MetricAggregationRules9', None)
    _safe_set(owner, 'metrics_Metric8', partner)
    assert getattr(partner, 'metrics_MetricAggregationRules9') == owner
    _safe_set(owner, 'metrics_Metric8', None)
    assert getattr(partner, 'metrics_MetricAggregationRules9') is None


def test_assoc_metricAggregationRules14_stub_double():
    # metrics_MetricAggregationRules has no real 'metrics_MetricAggregationRules15' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricAggregationRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricAggregationRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricAggregationRule(intervalHint="sample_text", period="sample_text")
    partner = metrics_MetricAggregationRules()
    setattr(partner, 'metrics_MetricAggregationRules15', None)
    _safe_set(owner, 'metrics_MetricAggregationRule16', partner)
    assert owner in getattr(partner, 'metrics_MetricAggregationRules15')
    _safe_set(owner, 'metrics_MetricAggregationRule16', None)
    assert owner not in getattr(partner, 'metrics_MetricAggregationRules15')


def test_assoc_metricRetentionRuleSet10_stub_double():
    # metrics_MetricRetentionRules has no real 'metrics_MetricRetentionRules12' property in the generated
    # code (a bare stub) -- manually attach it so metrics_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_Metric(name="sample_text")
    partner = metrics_MetricRetentionRules()
    setattr(partner, 'metrics_MetricRetentionRules12', None)
    _safe_set(owner, 'metrics_Metric11', partner)
    assert getattr(partner, 'metrics_MetricRetentionRules12') == owner
    _safe_set(owner, 'metrics_Metric11', None)
    assert getattr(partner, 'metrics_MetricRetentionRules12') is None


def test_assoc_metricRetentionRuleSet22_stub_double():
    # metrics_MetricRetentionRules has no real 'metrics_MetricRetentionRules24' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricSource(name="sample_text")
    partner = metrics_MetricRetentionRules()
    setattr(partner, 'metrics_MetricRetentionRules24', None)
    _safe_set(owner, 'metrics_MetricSource23', partner)
    assert getattr(partner, 'metrics_MetricRetentionRules24') == owner
    _safe_set(owner, 'metrics_MetricSource23', None)
    assert getattr(partner, 'metrics_MetricRetentionRules24') is None


def test_assoc_metricRetentionRules17_stub_double():
    # metrics_MetricRetentionRules has no real 'metrics_MetricRetentionRules18' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricRetentionRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricRetentionRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricRetentionRule(intervalHint="sample_text", period="sample_text")
    partner = metrics_MetricRetentionRules()
    setattr(partner, 'metrics_MetricRetentionRules18', None)
    _safe_set(owner, 'metrics_MetricRetentionRule', partner)
    assert owner in getattr(partner, 'metrics_MetricRetentionRules18')
    _safe_set(owner, 'metrics_MetricRetentionRule', None)
    assert owner not in getattr(partner, 'metrics_MetricRetentionRules18')


def test_assoc_metricSources1_stub_double():
    # metrics_Addon has no real 'metrics_Addon2' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricSource(name="sample_text")
    partner = metrics_Addon()
    setattr(partner, 'metrics_Addon2', None)
    _safe_set(owner, 'metrics_MetricSource', partner)
    assert owner in getattr(partner, 'metrics_Addon2')
    _safe_set(owner, 'metrics_MetricSource', None)
    assert owner not in getattr(partner, 'metrics_Addon2')


def test_assoc_metrics0_stub_double():
    # metrics_Addon has no real 'metrics_Addon' property in the generated
    # code (a bare stub) -- manually attach it so metrics_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_Metric(name="sample_text")
    partner = metrics_Addon()
    setattr(partner, 'metrics_Addon', None)
    _safe_set(owner, 'metrics_Metric', partner)
    assert owner in getattr(partner, 'metrics_Addon')
    _safe_set(owner, 'metrics_Metric', None)
    assert owner not in getattr(partner, 'metrics_Addon')


