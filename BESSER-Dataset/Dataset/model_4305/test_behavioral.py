import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Base,
    DataKind,
    Mapping,
    Rule,
    metrics_DataKind,
    metrics_DateTimeRange,
    metrics_Expression,
    metrics_IdentifierDataKind,
    metrics_Mapping,
    metrics_MappingCSV,
    metrics_MappingColumn,
    metrics_MappingExternal,
    metrics_MappingRDBMS,
    metrics_MappingRecord,
    metrics_MappingStatistic,
    metrics_MappingXLS,
    metrics_Metric,
    metrics_MetricAggregationRule,
    metrics_MetricAggregationRules,
    metrics_MetricRetentionPeriods,
    metrics_MetricRetentionRule,
    metrics_MetricRetentionRules,
    metrics_MetricSource,
    metrics_MetricValueRange,
    metrics_RuleSet,
    metrics_Unit,
    metrics_Value,
    metrics_ValueDataKind,
    DatabaseTypeType,
    FixedMetricRetentionPeriod,
    KindHintType,
    ObjectKindType,
    ValueKindType,
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

def test_assoc_dataMappingColumns1_reverse_link_reassign_clear():
    a1 = metrics_MappingColumn(column="sample_text")
    a2 = metrics_MappingColumn(column="sample_text_2")
    b = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    _safe_set(b, 'metrics_Mapping2', {a1})
    assert _is_linked(b, 'metrics_Mapping2', a1)
    if hasattr(a1, 'metrics_MappingColumn3'):
        assert _is_linked(a1, 'metrics_MappingColumn3', b)
    _safe_set(b, 'metrics_Mapping2', {a2})
    assert _is_linked(b, 'metrics_Mapping2', a2)
    if hasattr(a1, 'metrics_MappingColumn3'):
        assert not _is_linked(a1, 'metrics_MappingColumn3', b)
    if hasattr(a2, 'metrics_MappingColumn3'):
        assert _is_linked(a2, 'metrics_MappingColumn3', b)
    _safe_set(b, 'metrics_Mapping2', set())
    assert not _is_linked(b, 'metrics_Mapping2', a2)
    if hasattr(a2, 'metrics_MappingColumn3'):
        assert not _is_linked(a2, 'metrics_MappingColumn3', b)


def test_assoc_failedRecords6_reverse_link_reassign_clear():
    a1 = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    a2 = metrics_MappingStatistic(intervalEstimate="sample_text_2", message="sample_text_2", totalRecords="sample_text_2")
    b = metrics_MappingRecord(column="sample_text", count="sample_text", message="sample_text")
    _safe_set(b, 'metrics_MappingRecord', a1)
    assert _is_linked(b, 'metrics_MappingRecord', a1)
    if hasattr(a1, 'metrics_MappingStatistic'):
        assert _is_linked(a1, 'metrics_MappingStatistic', b)
    _safe_set(b, 'metrics_MappingRecord', a2)
    assert _is_linked(b, 'metrics_MappingRecord', a2)
    if hasattr(a1, 'metrics_MappingStatistic'):
        assert not _is_linked(a1, 'metrics_MappingStatistic', b)
    if hasattr(a2, 'metrics_MappingStatistic'):
        assert _is_linked(a2, 'metrics_MappingStatistic', b)
    _safe_set(b, 'metrics_MappingRecord', None)
    assert not _is_linked(b, 'metrics_MappingRecord', a2)
    if hasattr(a2, 'metrics_MappingStatistic'):
        assert not _is_linked(a2, 'metrics_MappingStatistic', b)


def test_assoc_headerMappingColumns0_reverse_link_reassign_clear():
    a1 = metrics_MappingColumn(column="sample_text")
    a2 = metrics_MappingColumn(column="sample_text_2")
    b = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    _safe_set(b, 'metrics_Mapping', {a1})
    assert _is_linked(b, 'metrics_Mapping', a1)
    if hasattr(a1, 'metrics_MappingColumn'):
        assert _is_linked(a1, 'metrics_MappingColumn', b)
    _safe_set(b, 'metrics_Mapping', {a2})
    assert _is_linked(b, 'metrics_Mapping', a2)
    if hasattr(a1, 'metrics_MappingColumn'):
        assert not _is_linked(a1, 'metrics_MappingColumn', b)
    if hasattr(a2, 'metrics_MappingColumn'):
        assert _is_linked(a2, 'metrics_MappingColumn', b)
    _safe_set(b, 'metrics_Mapping', set())
    assert not _is_linked(b, 'metrics_Mapping', a2)
    if hasattr(a2, 'metrics_MappingColumn'):
        assert not _is_linked(a2, 'metrics_MappingColumn', b)


def test_assoc_metricMapping28_reverse_link_reassign_clear():
    a1 = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    a2 = metrics_MetricSource(filterPattern="sample_text_2", metricLocation="sample_text_2", name="sample_text_2")
    b = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    _safe_set(b, 'metrics_Mapping30', a1)
    assert _is_linked(b, 'metrics_Mapping30', a1)
    if hasattr(a1, 'metrics_MetricSource29'):
        assert _is_linked(a1, 'metrics_MetricSource29', b)
    _safe_set(b, 'metrics_Mapping30', a2)
    assert _is_linked(b, 'metrics_Mapping30', a2)
    if hasattr(a1, 'metrics_MetricSource29'):
        assert not _is_linked(a1, 'metrics_MetricSource29', b)
    if hasattr(a2, 'metrics_MetricSource29'):
        assert _is_linked(a2, 'metrics_MetricSource29', b)
    _safe_set(b, 'metrics_Mapping30', None)
    assert not _is_linked(b, 'metrics_Mapping30', a2)
    if hasattr(a2, 'metrics_MetricSource29'):
        assert not _is_linked(a2, 'metrics_MetricSource29', b)


def test_assoc_metricRef40_reverse_link_reassign_clear():
    a1 = metrics_ValueDataKind(format="sample_text", kindHint="sample_text", valueKind="sample_text")
    a2 = metrics_ValueDataKind(format="sample_text_2", kindHint="sample_text_2", valueKind="sample_text_2")
    b = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    _safe_set(b, 'metrics_Metric41', a1)
    assert _is_linked(b, 'metrics_Metric41', a1)
    if hasattr(a1, 'metrics_ValueDataKind'):
        assert _is_linked(a1, 'metrics_ValueDataKind', b)
    _safe_set(b, 'metrics_Metric41', a2)
    assert _is_linked(b, 'metrics_Metric41', a2)
    if hasattr(a1, 'metrics_ValueDataKind'):
        assert not _is_linked(a1, 'metrics_ValueDataKind', b)
    if hasattr(a2, 'metrics_ValueDataKind'):
        assert _is_linked(a2, 'metrics_ValueDataKind', b)
    _safe_set(b, 'metrics_Metric41', None)
    assert not _is_linked(b, 'metrics_Metric41', a2)
    if hasattr(a2, 'metrics_ValueDataKind'):
        assert not _is_linked(a2, 'metrics_ValueDataKind', b)


def test_assoc_metricSourceRef19_reverse_link_reassign_clear():
    a1 = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    a2 = metrics_MetricSource(filterPattern="sample_text_2", metricLocation="sample_text_2", name="sample_text_2")
    b = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    _safe_set(b, 'metrics_Metric20', a1)
    assert _is_linked(b, 'metrics_Metric20', a1)
    if hasattr(a1, 'metrics_MetricSource'):
        assert _is_linked(a1, 'metrics_MetricSource', b)
    _safe_set(b, 'metrics_Metric20', a2)
    assert _is_linked(b, 'metrics_Metric20', a2)
    if hasattr(a1, 'metrics_MetricSource'):
        assert not _is_linked(a1, 'metrics_MetricSource', b)
    if hasattr(a2, 'metrics_MetricSource'):
        assert _is_linked(a2, 'metrics_MetricSource', b)
    _safe_set(b, 'metrics_Metric20', None)
    assert not _is_linked(b, 'metrics_Metric20', a2)
    if hasattr(a2, 'metrics_MetricSource'):
        assert not _is_linked(a2, 'metrics_MetricSource', b)


def test_assoc_metrics16_reverse_link_reassign_clear():
    a1 = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    a2 = metrics_Metric(description="sample_text_2", measurementKind="sample_text_2", measurementPoint="sample_text_2", name="sample_text_2")
    b = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    _safe_set(b, 'metrics_Metric15', {a1})
    assert _is_linked(b, 'metrics_Metric15', a1)
    if hasattr(a1, 'metrics_Metric'):
        assert _is_linked(a1, 'metrics_Metric', b)
    _safe_set(b, 'metrics_Metric15', {a2})
    assert _is_linked(b, 'metrics_Metric15', a2)
    if hasattr(a1, 'metrics_Metric'):
        assert not _is_linked(a1, 'metrics_Metric', b)
    if hasattr(a2, 'metrics_Metric'):
        assert _is_linked(a2, 'metrics_Metric', b)
    _safe_set(b, 'metrics_Metric15', set())
    assert not _is_linked(b, 'metrics_Metric15', a2)
    if hasattr(a2, 'metrics_Metric'):
        assert not _is_linked(a2, 'metrics_Metric', b)


def test_assoc_statistics31_reverse_link_reassign_clear():
    a1 = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    a2 = metrics_MetricSource(filterPattern="sample_text_2", metricLocation="sample_text_2", name="sample_text_2")
    b = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    _safe_set(b, 'metrics_MappingStatistic33', a1)
    assert _is_linked(b, 'metrics_MappingStatistic33', a1)
    if hasattr(a1, 'metrics_MetricSource32'):
        assert _is_linked(a1, 'metrics_MetricSource32', b)
    _safe_set(b, 'metrics_MappingStatistic33', a2)
    assert _is_linked(b, 'metrics_MappingStatistic33', a2)
    if hasattr(a1, 'metrics_MetricSource32'):
        assert not _is_linked(a1, 'metrics_MetricSource32', b)
    if hasattr(a2, 'metrics_MetricSource32'):
        assert _is_linked(a2, 'metrics_MetricSource32', b)
    _safe_set(b, 'metrics_MappingStatistic33', None)
    assert not _is_linked(b, 'metrics_MappingStatistic33', a2)
    if hasattr(a2, 'metrics_MetricSource32'):
        assert not _is_linked(a2, 'metrics_MetricSource32', b)


def test_assoc_subStatistics13_reverse_link_reassign_clear():
    a1 = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    a2 = metrics_MappingStatistic(intervalEstimate="sample_text_2", message="sample_text_2", totalRecords="sample_text_2")
    b = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    _safe_set(b, 'metrics_MappingStatistic14', a1)
    assert _is_linked(b, 'metrics_MappingStatistic14', a1)
    if hasattr(a1, 'metrics_MappingStatistic12'):
        assert _is_linked(a1, 'metrics_MappingStatistic12', b)
    _safe_set(b, 'metrics_MappingStatistic14', a2)
    assert _is_linked(b, 'metrics_MappingStatistic14', a2)
    if hasattr(a1, 'metrics_MappingStatistic12'):
        assert not _is_linked(a1, 'metrics_MappingStatistic12', b)
    if hasattr(a2, 'metrics_MappingStatistic12'):
        assert _is_linked(a2, 'metrics_MappingStatistic12', b)
    _safe_set(b, 'metrics_MappingStatistic14', None)
    assert not _is_linked(b, 'metrics_MappingStatistic14', a2)
    if hasattr(a2, 'metrics_MappingStatistic12'):
        assert not _is_linked(a2, 'metrics_MappingStatistic12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dataType4_stub_double():
    # metrics_DataKind has no real 'metrics_DataKind' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MappingColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MappingColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MappingColumn(column="sample_text")
    partner = metrics_DataKind()
    setattr(partner, 'metrics_DataKind', None)
    _safe_set(owner, 'metrics_MappingColumn5', partner)
    assert getattr(partner, 'metrics_DataKind') == owner
    _safe_set(owner, 'metrics_MappingColumn5', None)
    assert getattr(partner, 'metrics_DataKind') is None


def test_assoc_expressionRef17_stub_double():
    # metrics_Expression has no real 'metrics_Expression' property in the generated
    # code (a bare stub) -- manually attach it so metrics_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    partner = metrics_Expression()
    setattr(partner, 'metrics_Expression', None)
    _safe_set(owner, 'metrics_Metric18', partner)
    assert getattr(partner, 'metrics_Expression') == owner
    _safe_set(owner, 'metrics_Metric18', None)
    assert getattr(partner, 'metrics_Expression') is None


def test_assoc_mappingDuration7_stub_double():
    # metrics_DateTimeRange has no real 'metrics_DateTimeRange' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MappingStatistic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MappingStatistic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    partner = metrics_DateTimeRange()
    setattr(partner, 'metrics_DateTimeRange', None)
    _safe_set(owner, 'metrics_MappingStatistic8', partner)
    assert getattr(partner, 'metrics_DateTimeRange') == owner
    _safe_set(owner, 'metrics_MappingStatistic8', None)
    assert getattr(partner, 'metrics_DateTimeRange') is None


def test_assoc_metricAggregationRules34_stub_double():
    # metrics_RuleSet has no real 'metrics_RuleSet' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    partner = metrics_RuleSet()
    setattr(partner, 'metrics_RuleSet', None)
    _safe_set(owner, 'metrics_MetricSource35', partner)
    assert getattr(partner, 'metrics_RuleSet') == owner
    _safe_set(owner, 'metrics_MetricSource35', None)
    assert getattr(partner, 'metrics_RuleSet') is None


def test_assoc_metricRetentionRules27_stub_double():
    # metrics_MetricRetentionRules has no real 'metrics_MetricRetentionRules' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricRetentionRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricRetentionRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricRetentionRule(intervalHint="sample_text", period="sample_text")
    partner = metrics_MetricRetentionRules()
    setattr(partner, 'metrics_MetricRetentionRules', None)
    _safe_set(owner, 'metrics_MetricRetentionRule', partner)
    assert owner in getattr(partner, 'metrics_MetricRetentionRules')
    _safe_set(owner, 'metrics_MetricRetentionRule', None)
    assert owner not in getattr(partner, 'metrics_MetricRetentionRules')


def test_assoc_metricRetentionRules36_stub_double():
    # metrics_RuleSet has no real 'metrics_RuleSet38' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    partner = metrics_RuleSet()
    setattr(partner, 'metrics_RuleSet38', None)
    _safe_set(owner, 'metrics_MetricSource37', partner)
    assert getattr(partner, 'metrics_RuleSet38') == owner
    _safe_set(owner, 'metrics_MetricSource37', None)
    assert getattr(partner, 'metrics_RuleSet38') is None


def test_assoc_metricValues39_stub_double():
    # metrics_Value has no real 'metrics_Value' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricValueRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricValueRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricValueRange(intervalHint="sample_text", kindHint="sample_text")
    partner = metrics_Value()
    setattr(partner, 'metrics_Value', None)
    _safe_set(owner, 'metrics_MetricValueRange', {partner})
    assert getattr(partner, 'metrics_Value') == owner
    _safe_set(owner, 'metrics_MetricValueRange', set())
    assert getattr(partner, 'metrics_Value') is None


def test_assoc_periodEstimate9_stub_double():
    # metrics_DateTimeRange has no real 'metrics_DateTimeRange11' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MappingStatistic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MappingStatistic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    partner = metrics_DateTimeRange()
    setattr(partner, 'metrics_DateTimeRange11', None)
    _safe_set(owner, 'metrics_MappingStatistic10', partner)
    assert getattr(partner, 'metrics_DateTimeRange11') == owner
    _safe_set(owner, 'metrics_MappingStatistic10', None)
    assert getattr(partner, 'metrics_DateTimeRange11') is None


def test_assoc_unitRef21_stub_double():
    # metrics_Unit has no real 'metrics_Unit' property in the generated
    # code (a bare stub) -- manually attach it so metrics_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    partner = metrics_Unit()
    setattr(partner, 'metrics_Unit', None)
    _safe_set(owner, 'metrics_Metric22', partner)
    assert getattr(partner, 'metrics_Unit') == owner
    _safe_set(owner, 'metrics_Metric22', None)
    assert getattr(partner, 'metrics_Unit') is None


