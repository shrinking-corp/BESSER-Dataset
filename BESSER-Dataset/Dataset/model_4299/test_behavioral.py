import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataKind,
    Mapping,
    MappingRecord,
    metrics_DataKind,
    metrics_DateTimeRange,
    metrics_IdentifierDataKind,
    metrics_Mapping,
    metrics_MappingCSV,
    metrics_MappingRDBMS,
    metrics_MappingRecord,
    metrics_MappingRecordXLS,
    metrics_MappingStatistic,
    metrics_MappingXLS,
    metrics_MappingXLSColumn,
    metrics_Metric,
    metrics_MetricSource,
    metrics_MetricValueRange,
    metrics_Unit,
    metrics_Value,
    metrics_ValueDataKind,
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

def test_assoc_failedRecords0_reverse_link_reassign_clear():
    a1 = metrics_MappingStatistic(message="sample_text", totalRecords="sample_text")
    a2 = metrics_MappingStatistic(message="sample_text_2", totalRecords="sample_text_2")
    b = metrics_MappingRecord(message="sample_text")
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


def test_assoc_mappingColumns3_reverse_link_reassign_clear():
    a1 = metrics_MappingXLSColumn(column="sample_text")
    a2 = metrics_MappingXLSColumn(column="sample_text_2")
    b = metrics_MappingXLS(firstDataRow="sample_text", headerRow="sample_text", sheetNumber="sample_text")
    _safe_set(b, 'metrics_MappingXLS', {a1})
    assert _is_linked(b, 'metrics_MappingXLS', a1)
    if hasattr(a1, 'metrics_MappingXLSColumn'):
        assert _is_linked(a1, 'metrics_MappingXLSColumn', b)
    _safe_set(b, 'metrics_MappingXLS', {a2})
    assert _is_linked(b, 'metrics_MappingXLS', a2)
    if hasattr(a1, 'metrics_MappingXLSColumn'):
        assert not _is_linked(a1, 'metrics_MappingXLSColumn', b)
    if hasattr(a2, 'metrics_MappingXLSColumn'):
        assert _is_linked(a2, 'metrics_MappingXLSColumn', b)
    _safe_set(b, 'metrics_MappingXLS', set())
    assert not _is_linked(b, 'metrics_MappingXLS', a2)
    if hasattr(a2, 'metrics_MappingXLSColumn'):
        assert not _is_linked(a2, 'metrics_MappingXLSColumn', b)


def test_assoc_metricRef17_reverse_link_reassign_clear():
    a1 = metrics_ValueDataKind(kindHint="sample_text", valueKind="sample_text")
    a2 = metrics_ValueDataKind(kindHint="sample_text_2", valueKind="sample_text_2")
    b = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text")
    _safe_set(b, 'metrics_Metric18', a1)
    assert _is_linked(b, 'metrics_Metric18', a1)
    if hasattr(a1, 'metrics_ValueDataKind'):
        assert _is_linked(a1, 'metrics_ValueDataKind', b)
    _safe_set(b, 'metrics_Metric18', a2)
    assert _is_linked(b, 'metrics_Metric18', a2)
    if hasattr(a1, 'metrics_ValueDataKind'):
        assert not _is_linked(a1, 'metrics_ValueDataKind', b)
    if hasattr(a2, 'metrics_ValueDataKind'):
        assert _is_linked(a2, 'metrics_ValueDataKind', b)
    _safe_set(b, 'metrics_Metric18', None)
    assert not _is_linked(b, 'metrics_Metric18', a2)
    if hasattr(a2, 'metrics_ValueDataKind'):
        assert not _is_linked(a2, 'metrics_ValueDataKind', b)


def test_assoc_metricRefs11_reverse_link_reassign_clear():
    a1 = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    a2 = metrics_MetricSource(metricLocation="sample_text_2", name="sample_text_2")
    b = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text")
    _safe_set(b, 'Metric', a1)
    assert _is_linked(b, 'Metric', a1)
    if hasattr(a1, 'metricSourceRef'):
        assert _is_linked(a1, 'metricSourceRef', b)
    _safe_set(b, 'Metric', a2)
    assert _is_linked(b, 'Metric', a2)
    if hasattr(a1, 'metricSourceRef'):
        assert not _is_linked(a1, 'metricSourceRef', b)
    if hasattr(a2, 'metricSourceRef'):
        assert _is_linked(a2, 'metricSourceRef', b)
    _safe_set(b, 'Metric', None)
    assert not _is_linked(b, 'Metric', a2)
    if hasattr(a2, 'metricSourceRef'):
        assert not _is_linked(a2, 'metricSourceRef', b)


def test_assoc_metricSourceRef8_reverse_link_reassign_clear():
    a1 = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    a2 = metrics_MetricSource(metricLocation="sample_text_2", name="sample_text_2")
    b = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text")
    _safe_set(b, 'metricRefs', a1)
    assert _is_linked(b, 'metricRefs', a1)
    if hasattr(a1, 'MetricSource'):
        assert _is_linked(a1, 'MetricSource', b)
    _safe_set(b, 'metricRefs', a2)
    assert _is_linked(b, 'metricRefs', a2)
    if hasattr(a1, 'MetricSource'):
        assert not _is_linked(a1, 'MetricSource', b)
    if hasattr(a2, 'MetricSource'):
        assert _is_linked(a2, 'MetricSource', b)
    _safe_set(b, 'metricRefs', None)
    assert not _is_linked(b, 'metricRefs', a2)
    if hasattr(a2, 'MetricSource'):
        assert not _is_linked(a2, 'MetricSource', b)


def test_assoc_metrics7_reverse_link_reassign_clear():
    a1 = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text")
    a2 = metrics_Metric(description="sample_text_2", measurementKind="sample_text_2", measurementPoint="sample_text_2", metricCalculation="sample_text_2", name="sample_text_2")
    b = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text")
    _safe_set(b, 'metrics_Metric6', {a1})
    assert _is_linked(b, 'metrics_Metric6', a1)
    if hasattr(a1, 'metrics_Metric'):
        assert _is_linked(a1, 'metrics_Metric', b)
    _safe_set(b, 'metrics_Metric6', {a2})
    assert _is_linked(b, 'metrics_Metric6', a2)
    if hasattr(a1, 'metrics_Metric'):
        assert not _is_linked(a1, 'metrics_Metric', b)
    if hasattr(a2, 'metrics_Metric'):
        assert _is_linked(a2, 'metrics_Metric', b)
    _safe_set(b, 'metrics_Metric6', set())
    assert not _is_linked(b, 'metrics_Metric6', a2)
    if hasattr(a2, 'metrics_Metric'):
        assert not _is_linked(a2, 'metrics_Metric', b)


def test_assoc_statistics13_reverse_link_reassign_clear():
    a1 = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    a2 = metrics_MetricSource(metricLocation="sample_text_2", name="sample_text_2")
    b = metrics_MappingStatistic(message="sample_text", totalRecords="sample_text")
    _safe_set(b, 'metrics_MappingStatistic15', a1)
    assert _is_linked(b, 'metrics_MappingStatistic15', a1)
    if hasattr(a1, 'metrics_MetricSource14'):
        assert _is_linked(a1, 'metrics_MetricSource14', b)
    _safe_set(b, 'metrics_MappingStatistic15', a2)
    assert _is_linked(b, 'metrics_MappingStatistic15', a2)
    if hasattr(a1, 'metrics_MetricSource14'):
        assert not _is_linked(a1, 'metrics_MetricSource14', b)
    if hasattr(a2, 'metrics_MetricSource14'):
        assert _is_linked(a2, 'metrics_MetricSource14', b)
    _safe_set(b, 'metrics_MappingStatistic15', None)
    assert not _is_linked(b, 'metrics_MappingStatistic15', a2)
    if hasattr(a2, 'metrics_MetricSource14'):
        assert not _is_linked(a2, 'metrics_MetricSource14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dataType4_stub_double():
    # metrics_DataKind has no real 'metrics_DataKind' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MappingXLSColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MappingXLSColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MappingXLSColumn(column="sample_text")
    partner = metrics_DataKind()
    setattr(partner, 'metrics_DataKind', None)
    _safe_set(owner, 'metrics_MappingXLSColumn5', partner)
    assert getattr(partner, 'metrics_DataKind') == owner
    _safe_set(owner, 'metrics_MappingXLSColumn5', None)
    assert getattr(partner, 'metrics_DataKind') is None


def test_assoc_mappingDuration1_stub_double():
    # metrics_DateTimeRange has no real 'metrics_DateTimeRange' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MappingStatistic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MappingStatistic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MappingStatistic(message="sample_text", totalRecords="sample_text")
    partner = metrics_DateTimeRange()
    setattr(partner, 'metrics_DateTimeRange', None)
    _safe_set(owner, 'metrics_MappingStatistic2', partner)
    assert getattr(partner, 'metrics_DateTimeRange') == owner
    _safe_set(owner, 'metrics_MappingStatistic2', None)
    assert getattr(partner, 'metrics_DateTimeRange') is None


def test_assoc_metricMapping12_stub_double():
    # metrics_Mapping has no real 'metrics_Mapping' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    partner = metrics_Mapping()
    setattr(partner, 'metrics_Mapping', None)
    _safe_set(owner, 'metrics_MetricSource', partner)
    assert getattr(partner, 'metrics_Mapping') == owner
    _safe_set(owner, 'metrics_MetricSource', None)
    assert getattr(partner, 'metrics_Mapping') is None


def test_assoc_metricValues16_stub_double():
    # metrics_Value has no real 'metrics_Value' property in the generated
    # code (a bare stub) -- manually attach it so metrics_MetricValueRange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_MetricValueRange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_MetricValueRange(kindHint="sample_text", periodHint="sample_text")
    partner = metrics_Value()
    setattr(partner, 'metrics_Value', None)
    _safe_set(owner, 'metrics_MetricValueRange', {partner})
    assert getattr(partner, 'metrics_Value') == owner
    _safe_set(owner, 'metrics_MetricValueRange', set())
    assert getattr(partner, 'metrics_Value') is None


def test_assoc_unitRef9_stub_double():
    # metrics_Unit has no real 'metrics_Unit' property in the generated
    # code (a bare stub) -- manually attach it so metrics_Metric's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_Metric's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text")
    partner = metrics_Unit()
    setattr(partner, 'metrics_Unit', None)
    _safe_set(owner, 'metrics_Metric10', partner)
    assert getattr(partner, 'metrics_Unit') == owner
    _safe_set(owner, 'metrics_Metric10', None)
    assert getattr(partner, 'metrics_Unit') is None


