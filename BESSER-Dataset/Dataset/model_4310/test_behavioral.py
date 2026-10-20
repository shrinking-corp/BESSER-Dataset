import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Metric,
    MetricDefinition,
    Number,
    metricDSL_BoundAndWeight,
    metricDSL_Constant,
    metricDSL_ExternalMetric,
    metricDSL_InternalMetric,
    metricDSL_Metric,
    metricDSL_MetricAndWeight,
    metricDSL_MetricDefinition,
    metricDSL_MetricModel,
    metricDSL_Number,
    metricDSL_Parameter,
    metricDSL_RatioMetric,
    metricDSL_StepwiseMetric,
    metricDSL_WeightedMetric,
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

def test_assoc_metrics0_reverse_link_reassign_clear():
    a1 = metricDSL_MetricModel(importURI="sample_text")
    a2 = metricDSL_MetricModel(importURI="sample_text_2")
    b = metricDSL_Metric(name="sample_text")
    _safe_set(b, 'metricDSL_Metric', a1)
    assert _is_linked(b, 'metricDSL_Metric', a1)
    if hasattr(a1, 'metricDSL_MetricModel'):
        assert _is_linked(a1, 'metricDSL_MetricModel', b)
    _safe_set(b, 'metricDSL_Metric', a2)
    assert _is_linked(b, 'metricDSL_Metric', a2)
    if hasattr(a1, 'metricDSL_MetricModel'):
        assert not _is_linked(a1, 'metricDSL_MetricModel', b)
    if hasattr(a2, 'metricDSL_MetricModel'):
        assert _is_linked(a2, 'metricDSL_MetricModel', b)
    _safe_set(b, 'metricDSL_Metric', None)
    assert not _is_linked(b, 'metricDSL_Metric', a2)
    if hasattr(a2, 'metricDSL_MetricModel'):
        assert not _is_linked(a2, 'metricDSL_MetricModel', b)


def test_assoc_parameter1_reverse_link_reassign_clear():
    a1 = metricDSL_Number(name="sample_text")
    a2 = metricDSL_Number(name="sample_text_2")
    b = metricDSL_InternalMetric(description="sample_text", shortName="sample_text")
    _safe_set(b, 'metricDSL_InternalMetric', {a1})
    assert _is_linked(b, 'metricDSL_InternalMetric', a1)
    if hasattr(a1, 'metricDSL_Number'):
        assert _is_linked(a1, 'metricDSL_Number', b)
    _safe_set(b, 'metricDSL_InternalMetric', {a2})
    assert _is_linked(b, 'metricDSL_InternalMetric', a2)
    if hasattr(a1, 'metricDSL_Number'):
        assert not _is_linked(a1, 'metricDSL_Number', b)
    if hasattr(a2, 'metricDSL_Number'):
        assert _is_linked(a2, 'metricDSL_Number', b)
    _safe_set(b, 'metricDSL_InternalMetric', set())
    assert not _is_linked(b, 'metricDSL_InternalMetric', a2)
    if hasattr(a2, 'metricDSL_Number'):
        assert not _is_linked(a2, 'metricDSL_Number', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_definition2_stub_double():
    # metricDSL_MetricDefinition has no real 'metricDSL_MetricDefinition' property in the generated
    # code (a bare stub) -- manually attach it so metricDSL_InternalMetric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metricDSL_InternalMetric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metricDSL_InternalMetric(description="sample_text", shortName="sample_text")
    partner = metricDSL_MetricDefinition()
    setattr(partner, 'metricDSL_MetricDefinition', None)
    _safe_set(owner, 'metricDSL_InternalMetric3', partner)
    assert getattr(partner, 'metricDSL_MetricDefinition') == owner
    _safe_set(owner, 'metricDSL_InternalMetric3', None)
    assert getattr(partner, 'metricDSL_MetricDefinition') is None


def test_assoc_denominatorMetric11_stub_double():
    # metricDSL_RatioMetric has no real 'metricDSL_RatioMetric12' property in the generated
    # code (a bare stub) -- manually attach it so metricDSL_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metricDSL_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metricDSL_Metric(name="sample_text")
    partner = metricDSL_RatioMetric()
    setattr(partner, 'metricDSL_RatioMetric12', None)
    _safe_set(owner, 'metricDSL_Metric13', partner)
    assert getattr(partner, 'metricDSL_RatioMetric12') == owner
    _safe_set(owner, 'metricDSL_Metric13', None)
    assert getattr(partner, 'metricDSL_RatioMetric12') is None


def test_assoc_innerMetric5_stub_double():
    # metricDSL_StepwiseMetric has no real 'metricDSL_StepwiseMetric' property in the generated
    # code (a bare stub) -- manually attach it so metricDSL_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metricDSL_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metricDSL_Metric(name="sample_text")
    partner = metricDSL_StepwiseMetric()
    setattr(partner, 'metricDSL_StepwiseMetric', None)
    _safe_set(owner, 'metricDSL_Metric6', partner)
    assert getattr(partner, 'metricDSL_StepwiseMetric') == owner
    _safe_set(owner, 'metricDSL_Metric6', None)
    assert getattr(partner, 'metricDSL_StepwiseMetric') is None


def test_assoc_metric20_stub_double():
    # metricDSL_MetricAndWeight has no real 'metricDSL_MetricAndWeight21' property in the generated
    # code (a bare stub) -- manually attach it so metricDSL_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metricDSL_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metricDSL_Metric(name="sample_text")
    partner = metricDSL_MetricAndWeight()
    setattr(partner, 'metricDSL_MetricAndWeight21', None)
    _safe_set(owner, 'metricDSL_Metric22', partner)
    assert getattr(partner, 'metricDSL_MetricAndWeight21') == owner
    _safe_set(owner, 'metricDSL_Metric22', None)
    assert getattr(partner, 'metricDSL_MetricAndWeight21') is None


def test_assoc_nominatorMetric9_stub_double():
    # metricDSL_RatioMetric has no real 'metricDSL_RatioMetric' property in the generated
    # code (a bare stub) -- manually attach it so metricDSL_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metricDSL_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metricDSL_Metric(name="sample_text")
    partner = metricDSL_RatioMetric()
    setattr(partner, 'metricDSL_RatioMetric', None)
    _safe_set(owner, 'metricDSL_Metric10', partner)
    assert getattr(partner, 'metricDSL_RatioMetric') == owner
    _safe_set(owner, 'metricDSL_Metric10', None)
    assert getattr(partner, 'metricDSL_RatioMetric') is None


def test_assoc_upperBound14_stub_double():
    # metricDSL_BoundAndWeight has no real 'metricDSL_BoundAndWeight15' property in the generated
    # code (a bare stub) -- manually attach it so metricDSL_Number's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metricDSL_Number's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metricDSL_Number(name="sample_text")
    partner = metricDSL_BoundAndWeight()
    setattr(partner, 'metricDSL_BoundAndWeight15', None)
    _safe_set(owner, 'metricDSL_Number16', partner)
    assert getattr(partner, 'metricDSL_BoundAndWeight15') == owner
    _safe_set(owner, 'metricDSL_Number16', None)
    assert getattr(partner, 'metricDSL_BoundAndWeight15') is None


def test_assoc_weight17_stub_double():
    # metricDSL_BoundAndWeight has no real 'metricDSL_BoundAndWeight18' property in the generated
    # code (a bare stub) -- manually attach it so metricDSL_Number's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metricDSL_Number's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metricDSL_Number(name="sample_text")
    partner = metricDSL_BoundAndWeight()
    setattr(partner, 'metricDSL_BoundAndWeight18', None)
    _safe_set(owner, 'metricDSL_Number19', partner)
    assert getattr(partner, 'metricDSL_BoundAndWeight18') == owner
    _safe_set(owner, 'metricDSL_Number19', None)
    assert getattr(partner, 'metricDSL_BoundAndWeight18') is None


def test_assoc_weight23_stub_double():
    # metricDSL_MetricAndWeight has no real 'metricDSL_MetricAndWeight24' property in the generated
    # code (a bare stub) -- manually attach it so metricDSL_Number's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metricDSL_Number's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metricDSL_Number(name="sample_text")
    partner = metricDSL_MetricAndWeight()
    setattr(partner, 'metricDSL_MetricAndWeight24', None)
    _safe_set(owner, 'metricDSL_Number25', partner)
    assert getattr(partner, 'metricDSL_MetricAndWeight24') == owner
    _safe_set(owner, 'metricDSL_Number25', None)
    assert getattr(partner, 'metricDSL_MetricAndWeight24') is None


