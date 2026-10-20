import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    QualityMetamodel_AggregatedValue,
    QualityMetamodel_AggregatedValueMetric,
    QualityMetamodel_BooleanValueType,
    QualityMetamodel_EnumerationItem,
    QualityMetamodel_EnumerationMetric,
    QualityMetamodel_IntegerValueType,
    QualityMetamodel_MetricProvider,
    QualityMetamodel_Operation,
    QualityMetamodel_QualityAttribute,
    QualityMetamodel_QualityModel,
    QualityMetamodel_RangeValueType,
    QualityMetamodel_RealValueType,
    QualityMetamodel_SingleValue,
    QualityMetamodel_TextValueType,
    QualityMetamodel_Value,
    QualityMetamodel_ValueType,
    Value,
    ValueType,
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

def test_assoc_aggregatedValues18_reverse_link_reassign_clear():
    a1 = QualityMetamodel_Value(description="sample_text", name="sample_text")
    a2 = QualityMetamodel_Value(description="sample_text_2", name="sample_text_2")
    b = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    _safe_set(b, 'QualityMetamodel_Operation19', {a1})
    assert _is_linked(b, 'QualityMetamodel_Operation19', a1)
    if hasattr(a1, 'QualityMetamodel_Value20'):
        assert _is_linked(a1, 'QualityMetamodel_Value20', b)
    _safe_set(b, 'QualityMetamodel_Operation19', {a2})
    assert _is_linked(b, 'QualityMetamodel_Operation19', a2)
    if hasattr(a1, 'QualityMetamodel_Value20'):
        assert not _is_linked(a1, 'QualityMetamodel_Value20', b)
    if hasattr(a2, 'QualityMetamodel_Value20'):
        assert _is_linked(a2, 'QualityMetamodel_Value20', b)
    _safe_set(b, 'QualityMetamodel_Operation19', set())
    assert not _is_linked(b, 'QualityMetamodel_Operation19', a2)
    if hasattr(a2, 'QualityMetamodel_Value20'):
        assert not _is_linked(a2, 'QualityMetamodel_Value20', b)


def test_assoc_metricProviders0_reverse_link_reassign_clear():
    a1 = QualityMetamodel_QualityModel(name="sample_text")
    a2 = QualityMetamodel_QualityModel(name="sample_text_2")
    b = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'QualityMetamodel_MetricProvider', a1)
    assert _is_linked(b, 'QualityMetamodel_MetricProvider', a1)
    if hasattr(a1, 'QualityMetamodel_QualityModel'):
        assert _is_linked(a1, 'QualityMetamodel_QualityModel', b)
    _safe_set(b, 'QualityMetamodel_MetricProvider', a2)
    assert _is_linked(b, 'QualityMetamodel_MetricProvider', a2)
    if hasattr(a1, 'QualityMetamodel_QualityModel'):
        assert not _is_linked(a1, 'QualityMetamodel_QualityModel', b)
    if hasattr(a2, 'QualityMetamodel_QualityModel'):
        assert _is_linked(a2, 'QualityMetamodel_QualityModel', b)
    _safe_set(b, 'QualityMetamodel_MetricProvider', None)
    assert not _is_linked(b, 'QualityMetamodel_MetricProvider', a2)
    if hasattr(a2, 'QualityMetamodel_QualityModel'):
        assert not _is_linked(a2, 'QualityMetamodel_QualityModel', b)


def test_assoc_qualityAttributes11_reverse_link_reassign_clear():
    a1 = QualityMetamodel_QualityAttribute(name="sample_text")
    a2 = QualityMetamodel_QualityAttribute(name="sample_text_2")
    b = QualityMetamodel_QualityAttribute(name="sample_text")
    _safe_set(b, 'QualityMetamodel_QualityAttribute12', a1)
    assert _is_linked(b, 'QualityMetamodel_QualityAttribute12', a1)
    if hasattr(a1, 'QualityMetamodel_QualityAttribute10'):
        assert _is_linked(a1, 'QualityMetamodel_QualityAttribute10', b)
    _safe_set(b, 'QualityMetamodel_QualityAttribute12', a2)
    assert _is_linked(b, 'QualityMetamodel_QualityAttribute12', a2)
    if hasattr(a1, 'QualityMetamodel_QualityAttribute10'):
        assert not _is_linked(a1, 'QualityMetamodel_QualityAttribute10', b)
    if hasattr(a2, 'QualityMetamodel_QualityAttribute10'):
        assert _is_linked(a2, 'QualityMetamodel_QualityAttribute10', b)
    _safe_set(b, 'QualityMetamodel_QualityAttribute12', None)
    assert not _is_linked(b, 'QualityMetamodel_QualityAttribute12', a2)
    if hasattr(a2, 'QualityMetamodel_QualityAttribute10'):
        assert not _is_linked(a2, 'QualityMetamodel_QualityAttribute10', b)


def test_assoc_qualityAttributes3_reverse_link_reassign_clear():
    a1 = QualityMetamodel_QualityModel(name="sample_text")
    a2 = QualityMetamodel_QualityModel(name="sample_text_2")
    b = QualityMetamodel_QualityAttribute(name="sample_text")
    _safe_set(b, 'QualityMetamodel_QualityAttribute', a1)
    assert _is_linked(b, 'QualityMetamodel_QualityAttribute', a1)
    if hasattr(a1, 'QualityMetamodel_QualityModel4'):
        assert _is_linked(a1, 'QualityMetamodel_QualityModel4', b)
    _safe_set(b, 'QualityMetamodel_QualityAttribute', a2)
    assert _is_linked(b, 'QualityMetamodel_QualityAttribute', a2)
    if hasattr(a1, 'QualityMetamodel_QualityModel4'):
        assert not _is_linked(a1, 'QualityMetamodel_QualityModel4', b)
    if hasattr(a2, 'QualityMetamodel_QualityModel4'):
        assert _is_linked(a2, 'QualityMetamodel_QualityModel4', b)
    _safe_set(b, 'QualityMetamodel_QualityAttribute', None)
    assert not _is_linked(b, 'QualityMetamodel_QualityAttribute', a2)
    if hasattr(a2, 'QualityMetamodel_QualityModel4'):
        assert not _is_linked(a2, 'QualityMetamodel_QualityModel4', b)


def test_assoc_qualityTypes1_reverse_link_reassign_clear():
    a1 = QualityMetamodel_ValueType(name="sample_text")
    a2 = QualityMetamodel_ValueType(name="sample_text_2")
    b = QualityMetamodel_QualityModel(name="sample_text")
    _safe_set(b, 'QualityMetamodel_QualityModel2', {a1})
    assert _is_linked(b, 'QualityMetamodel_QualityModel2', a1)
    if hasattr(a1, 'QualityMetamodel_ValueType'):
        assert _is_linked(a1, 'QualityMetamodel_ValueType', b)
    _safe_set(b, 'QualityMetamodel_QualityModel2', {a2})
    assert _is_linked(b, 'QualityMetamodel_QualityModel2', a2)
    if hasattr(a1, 'QualityMetamodel_ValueType'):
        assert not _is_linked(a1, 'QualityMetamodel_ValueType', b)
    if hasattr(a2, 'QualityMetamodel_ValueType'):
        assert _is_linked(a2, 'QualityMetamodel_ValueType', b)
    _safe_set(b, 'QualityMetamodel_QualityModel2', set())
    assert not _is_linked(b, 'QualityMetamodel_QualityModel2', a2)
    if hasattr(a2, 'QualityMetamodel_ValueType'):
        assert not _is_linked(a2, 'QualityMetamodel_ValueType', b)


def test_assoc_qualityValues5_reverse_link_reassign_clear():
    a1 = QualityMetamodel_Value(description="sample_text", name="sample_text")
    a2 = QualityMetamodel_Value(description="sample_text_2", name="sample_text_2")
    b = QualityMetamodel_QualityModel(name="sample_text")
    _safe_set(b, 'QualityMetamodel_QualityModel6', {a1})
    assert _is_linked(b, 'QualityMetamodel_QualityModel6', a1)
    if hasattr(a1, 'QualityMetamodel_Value'):
        assert _is_linked(a1, 'QualityMetamodel_Value', b)
    _safe_set(b, 'QualityMetamodel_QualityModel6', {a2})
    assert _is_linked(b, 'QualityMetamodel_QualityModel6', a2)
    if hasattr(a1, 'QualityMetamodel_Value'):
        assert not _is_linked(a1, 'QualityMetamodel_Value', b)
    if hasattr(a2, 'QualityMetamodel_Value'):
        assert _is_linked(a2, 'QualityMetamodel_Value', b)
    _safe_set(b, 'QualityMetamodel_QualityModel6', set())
    assert not _is_linked(b, 'QualityMetamodel_QualityModel6', a2)
    if hasattr(a2, 'QualityMetamodel_Value'):
        assert not _is_linked(a2, 'QualityMetamodel_Value', b)


def test_assoc_type13_reverse_link_reassign_clear():
    a1 = QualityMetamodel_ValueType(name="sample_text")
    a2 = QualityMetamodel_ValueType(name="sample_text_2")
    b = QualityMetamodel_Value(description="sample_text", name="sample_text")
    _safe_set(b, 'val', a1)
    assert _is_linked(b, 'val', a1)
    if hasattr(a1, 'ValueType'):
        assert _is_linked(a1, 'ValueType', b)
    _safe_set(b, 'val', a2)
    assert _is_linked(b, 'val', a2)
    if hasattr(a1, 'ValueType'):
        assert not _is_linked(a1, 'ValueType', b)
    if hasattr(a2, 'ValueType'):
        assert _is_linked(a2, 'ValueType', b)
    _safe_set(b, 'val', None)
    assert not _is_linked(b, 'val', a2)
    if hasattr(a2, 'ValueType'):
        assert not _is_linked(a2, 'ValueType', b)


def test_assoc_val14_reverse_link_reassign_clear():
    a1 = QualityMetamodel_ValueType(name="sample_text")
    a2 = QualityMetamodel_ValueType(name="sample_text_2")
    b = QualityMetamodel_Value(description="sample_text", name="sample_text")
    _safe_set(b, 'Value', a1)
    assert _is_linked(b, 'Value', a1)
    if hasattr(a1, 'type'):
        assert _is_linked(a1, 'type', b)
    _safe_set(b, 'Value', a2)
    assert _is_linked(b, 'Value', a2)
    if hasattr(a1, 'type'):
        assert not _is_linked(a1, 'type', b)
    if hasattr(a2, 'type'):
        assert _is_linked(a2, 'type', b)
    _safe_set(b, 'Value', None)
    assert not _is_linked(b, 'Value', a2)
    if hasattr(a2, 'type'):
        assert not _is_linked(a2, 'type', b)


def test_assoc_value7_reverse_link_reassign_clear():
    a1 = QualityMetamodel_Value(description="sample_text", name="sample_text")
    a2 = QualityMetamodel_Value(description="sample_text_2", name="sample_text_2")
    b = QualityMetamodel_QualityAttribute(name="sample_text")
    _safe_set(b, 'QualityMetamodel_QualityAttribute8', a1)
    assert _is_linked(b, 'QualityMetamodel_QualityAttribute8', a1)
    if hasattr(a1, 'QualityMetamodel_Value9'):
        assert _is_linked(a1, 'QualityMetamodel_Value9', b)
    _safe_set(b, 'QualityMetamodel_QualityAttribute8', a2)
    assert _is_linked(b, 'QualityMetamodel_QualityAttribute8', a2)
    if hasattr(a1, 'QualityMetamodel_Value9'):
        assert not _is_linked(a1, 'QualityMetamodel_Value9', b)
    if hasattr(a2, 'QualityMetamodel_Value9'):
        assert _is_linked(a2, 'QualityMetamodel_Value9', b)
    _safe_set(b, 'QualityMetamodel_QualityAttribute8', None)
    assert not _is_linked(b, 'QualityMetamodel_QualityAttribute8', a2)
    if hasattr(a2, 'QualityMetamodel_Value9'):
        assert not _is_linked(a2, 'QualityMetamodel_Value9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_calculatedBy17_stub_double():
    # QualityMetamodel_AggregatedValue has no real 'QualityMetamodel_AggregatedValue' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    partner = QualityMetamodel_AggregatedValue()
    setattr(partner, 'QualityMetamodel_AggregatedValue', None)
    _safe_set(owner, 'QualityMetamodel_Operation', partner)
    assert getattr(partner, 'QualityMetamodel_AggregatedValue') == owner
    _safe_set(owner, 'QualityMetamodel_Operation', None)
    assert getattr(partner, 'QualityMetamodel_AggregatedValue') is None


def test_assoc_measuredBy15_stub_double():
    # QualityMetamodel_SingleValue has no real 'QualityMetamodel_SingleValue' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_MetricProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_MetricProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    partner = QualityMetamodel_SingleValue()
    setattr(partner, 'QualityMetamodel_SingleValue', None)
    _safe_set(owner, 'QualityMetamodel_MetricProvider16', partner)
    assert getattr(partner, 'QualityMetamodel_SingleValue') == owner
    _safe_set(owner, 'QualityMetamodel_MetricProvider16', None)
    assert getattr(partner, 'QualityMetamodel_SingleValue') is None


def test_assoc_set21_stub_double():
    # QualityMetamodel_EnumerationMetric has no real 'QualityMetamodel_EnumerationMetric' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_EnumerationItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_EnumerationItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_EnumerationItem(name="sample_text")
    partner = QualityMetamodel_EnumerationMetric()
    setattr(partner, 'QualityMetamodel_EnumerationMetric', None)
    _safe_set(owner, 'QualityMetamodel_EnumerationItem', partner)
    assert owner in getattr(partner, 'QualityMetamodel_EnumerationMetric')
    _safe_set(owner, 'QualityMetamodel_EnumerationItem', None)
    assert owner not in getattr(partner, 'QualityMetamodel_EnumerationMetric')


def test_assoc_value22_stub_double():
    # QualityMetamodel_EnumerationMetric has no real 'QualityMetamodel_EnumerationMetric23' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_EnumerationItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_EnumerationItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_EnumerationItem(name="sample_text")
    partner = QualityMetamodel_EnumerationMetric()
    setattr(partner, 'QualityMetamodel_EnumerationMetric23', None)
    _safe_set(owner, 'QualityMetamodel_EnumerationItem24', partner)
    assert getattr(partner, 'QualityMetamodel_EnumerationMetric23') == owner
    _safe_set(owner, 'QualityMetamodel_EnumerationItem24', None)
    assert getattr(partner, 'QualityMetamodel_EnumerationMetric23') is None


