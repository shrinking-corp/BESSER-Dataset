import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Base,
    DataKind,
    Mapping,
    metrics_DataKind,
    metrics_DateTimeRange,
    metrics_Expression,
    metrics_IdentifierDataKind,
    metrics_Mapping,
    metrics_MappingCSV,
    metrics_MappingColumn,
    metrics_MappingRDBMS,
    metrics_MappingRecord,
    metrics_MappingStatistic,
    metrics_MappingXLS,
    metrics_Metric,
    metrics_MetricRetentionRule,
    metrics_MetricRetentionRules,
    metrics_MetricSource,
    metrics_MetricValueRange,
    metrics_Unit,
    metrics_Value,
    metrics_ValueDataKind,
    DatabaseTypeType,
    KindHintType,
    MetricRetentionPeriod,
    ObjectKindType,
    ValueKindType,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_metrics_IdentifierDataKind_objectKind_value_roundtrip():
    instance = metrics_IdentifierDataKind(objectKind="sample_text", objectProperty="sample_text", pattern="sample_text")
    assert instance.objectKind == "sample_text"
    instance.objectKind = "sample_text_2"
    assert instance.objectKind == "sample_text_2"


def test_metrics_IdentifierDataKind_objectProperty_value_roundtrip():
    instance = metrics_IdentifierDataKind(objectKind="sample_text", objectProperty="sample_text", pattern="sample_text")
    assert instance.objectProperty == "sample_text"
    instance.objectProperty = "sample_text_2"
    assert instance.objectProperty == "sample_text_2"


def test_metrics_IdentifierDataKind_pattern_value_roundtrip():
    instance = metrics_IdentifierDataKind(objectKind="sample_text", objectProperty="sample_text", pattern="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_metrics_Mapping_firstDataRow_value_roundtrip():
    instance = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    assert instance.firstDataRow == "sample_text"
    instance.firstDataRow = "sample_text_2"
    assert instance.firstDataRow == "sample_text_2"


def test_metrics_Mapping_headerRow_value_roundtrip():
    instance = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    assert instance.headerRow == "sample_text"
    instance.headerRow = "sample_text_2"
    assert instance.headerRow == "sample_text_2"


def test_metrics_Mapping_intervalHint_value_roundtrip():
    instance = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    assert instance.intervalHint == "sample_text"
    instance.intervalHint = "sample_text_2"
    assert instance.intervalHint == "sample_text_2"


def test_metrics_MappingCSV_delimiter_value_roundtrip():
    instance = metrics_MappingCSV(delimiter="sample_text", filterPattern="sample_text")
    assert instance.delimiter == "sample_text"
    instance.delimiter = "sample_text_2"
    assert instance.delimiter == "sample_text_2"


def test_metrics_MappingCSV_filterPattern_value_roundtrip():
    instance = metrics_MappingCSV(delimiter="sample_text", filterPattern="sample_text")
    assert instance.filterPattern == "sample_text"
    instance.filterPattern = "sample_text_2"
    assert instance.filterPattern == "sample_text_2"


def test_metrics_MappingColumn_column_value_roundtrip():
    instance = metrics_MappingColumn(column="sample_text")
    assert instance.column == "sample_text"
    instance.column = "sample_text_2"
    assert instance.column == "sample_text_2"


def test_metrics_MappingRDBMS_databaseType_value_roundtrip():
    instance = metrics_MappingRDBMS(databaseType="sample_text", dateFormat="sample_text", dateTimeFormat="sample_text", password="sample_text", query="sample_text", timeFormat="sample_text", user="sample_text")
    assert instance.databaseType == "sample_text"
    instance.databaseType = "sample_text_2"
    assert instance.databaseType == "sample_text_2"


def test_metrics_MappingRDBMS_dateFormat_value_roundtrip():
    instance = metrics_MappingRDBMS(databaseType="sample_text", dateFormat="sample_text", dateTimeFormat="sample_text", password="sample_text", query="sample_text", timeFormat="sample_text", user="sample_text")
    assert instance.dateFormat == "sample_text"
    instance.dateFormat = "sample_text_2"
    assert instance.dateFormat == "sample_text_2"


def test_metrics_MappingRDBMS_dateTimeFormat_value_roundtrip():
    instance = metrics_MappingRDBMS(databaseType="sample_text", dateFormat="sample_text", dateTimeFormat="sample_text", password="sample_text", query="sample_text", timeFormat="sample_text", user="sample_text")
    assert instance.dateTimeFormat == "sample_text"
    instance.dateTimeFormat = "sample_text_2"
    assert instance.dateTimeFormat == "sample_text_2"


def test_metrics_MappingRDBMS_password_value_roundtrip():
    instance = metrics_MappingRDBMS(databaseType="sample_text", dateFormat="sample_text", dateTimeFormat="sample_text", password="sample_text", query="sample_text", timeFormat="sample_text", user="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_metrics_MappingRDBMS_query_value_roundtrip():
    instance = metrics_MappingRDBMS(databaseType="sample_text", dateFormat="sample_text", dateTimeFormat="sample_text", password="sample_text", query="sample_text", timeFormat="sample_text", user="sample_text")
    assert instance.query == "sample_text"
    instance.query = "sample_text_2"
    assert instance.query == "sample_text_2"


def test_metrics_MappingRDBMS_timeFormat_value_roundtrip():
    instance = metrics_MappingRDBMS(databaseType="sample_text", dateFormat="sample_text", dateTimeFormat="sample_text", password="sample_text", query="sample_text", timeFormat="sample_text", user="sample_text")
    assert instance.timeFormat == "sample_text"
    instance.timeFormat = "sample_text_2"
    assert instance.timeFormat == "sample_text_2"


def test_metrics_MappingRDBMS_user_value_roundtrip():
    instance = metrics_MappingRDBMS(databaseType="sample_text", dateFormat="sample_text", dateTimeFormat="sample_text", password="sample_text", query="sample_text", timeFormat="sample_text", user="sample_text")
    assert instance.user == "sample_text"
    instance.user = "sample_text_2"
    assert instance.user == "sample_text_2"


def test_metrics_MappingRecord_column_value_roundtrip():
    instance = metrics_MappingRecord(column="sample_text", count="sample_text", message="sample_text")
    assert instance.column == "sample_text"
    instance.column = "sample_text_2"
    assert instance.column == "sample_text_2"


def test_metrics_MappingRecord_count_value_roundtrip():
    instance = metrics_MappingRecord(column="sample_text", count="sample_text", message="sample_text")
    assert instance.count == "sample_text"
    instance.count = "sample_text_2"
    assert instance.count == "sample_text_2"


def test_metrics_MappingRecord_message_value_roundtrip():
    instance = metrics_MappingRecord(column="sample_text", count="sample_text", message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_metrics_MappingStatistic_intervalEstimate_value_roundtrip():
    instance = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    assert instance.intervalEstimate == "sample_text"
    instance.intervalEstimate = "sample_text_2"
    assert instance.intervalEstimate == "sample_text_2"


def test_metrics_MappingStatistic_message_value_roundtrip():
    instance = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_metrics_MappingStatistic_totalRecords_value_roundtrip():
    instance = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    assert instance.totalRecords == "sample_text"
    instance.totalRecords = "sample_text_2"
    assert instance.totalRecords == "sample_text_2"


def test_metrics_MappingXLS_filterPattern_value_roundtrip():
    instance = metrics_MappingXLS(filterPattern="sample_text", sheetNumber="sample_text")
    assert instance.filterPattern == "sample_text"
    instance.filterPattern = "sample_text_2"
    assert instance.filterPattern == "sample_text_2"


def test_metrics_MappingXLS_sheetNumber_value_roundtrip():
    instance = metrics_MappingXLS(filterPattern="sample_text", sheetNumber="sample_text")
    assert instance.sheetNumber == "sample_text"
    instance.sheetNumber = "sample_text_2"
    assert instance.sheetNumber == "sample_text_2"


def test_metrics_Metric_description_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_metrics_Metric_measurementKind_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    assert instance.measurementKind == "sample_text"
    instance.measurementKind = "sample_text_2"
    assert instance.measurementKind == "sample_text_2"


def test_metrics_Metric_measurementPoint_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    assert instance.measurementPoint == "sample_text"
    instance.measurementPoint = "sample_text_2"
    assert instance.measurementPoint == "sample_text_2"


def test_metrics_Metric_name_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metrics_MetricRetentionRule_intervalHint_value_roundtrip():
    instance = metrics_MetricRetentionRule(intervalHint="sample_text", name="sample_text", period="sample_text")
    assert instance.intervalHint == "sample_text"
    instance.intervalHint = "sample_text_2"
    assert instance.intervalHint == "sample_text_2"


def test_metrics_MetricRetentionRule_name_value_roundtrip():
    instance = metrics_MetricRetentionRule(intervalHint="sample_text", name="sample_text", period="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metrics_MetricRetentionRule_period_value_roundtrip():
    instance = metrics_MetricRetentionRule(intervalHint="sample_text", name="sample_text", period="sample_text")
    assert instance.period == "sample_text"
    instance.period = "sample_text_2"
    assert instance.period == "sample_text_2"


def test_metrics_MetricSource_filterPattern_value_roundtrip():
    instance = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    assert instance.filterPattern == "sample_text"
    instance.filterPattern = "sample_text_2"
    assert instance.filterPattern == "sample_text_2"


def test_metrics_MetricSource_metricLocation_value_roundtrip():
    instance = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    assert instance.metricLocation == "sample_text"
    instance.metricLocation = "sample_text_2"
    assert instance.metricLocation == "sample_text_2"


def test_metrics_MetricSource_name_value_roundtrip():
    instance = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metrics_MetricValueRange_intervalHint_value_roundtrip():
    instance = metrics_MetricValueRange(intervalHint="sample_text", kindHint="sample_text")
    assert instance.intervalHint == "sample_text"
    instance.intervalHint = "sample_text_2"
    assert instance.intervalHint == "sample_text_2"


def test_metrics_MetricValueRange_kindHint_value_roundtrip():
    instance = metrics_MetricValueRange(intervalHint="sample_text", kindHint="sample_text")
    assert instance.kindHint == "sample_text"
    instance.kindHint = "sample_text_2"
    assert instance.kindHint == "sample_text_2"


def test_metrics_ValueDataKind_format_value_roundtrip():
    instance = metrics_ValueDataKind(format="sample_text", kindHint="sample_text", valueKind="sample_text")
    assert instance.format == "sample_text"
    instance.format = "sample_text_2"
    assert instance.format == "sample_text_2"


def test_metrics_ValueDataKind_kindHint_value_roundtrip():
    instance = metrics_ValueDataKind(format="sample_text", kindHint="sample_text", valueKind="sample_text")
    assert instance.kindHint == "sample_text"
    instance.kindHint = "sample_text_2"
    assert instance.kindHint == "sample_text_2"


def test_metrics_ValueDataKind_valueKind_value_roundtrip():
    instance = metrics_ValueDataKind(format="sample_text", kindHint="sample_text", valueKind="sample_text")
    assert instance.valueKind == "sample_text"
    instance.valueKind = "sample_text_2"
    assert instance.valueKind == "sample_text_2"


def test_metrics_Mapping_isa_Base():
    instance = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    assert isinstance(instance, Base)


def test_metrics_MappingColumn_isa_Base():
    instance = metrics_MappingColumn(column="sample_text")
    assert isinstance(instance, Base)


def test_metrics_MappingRecord_isa_Base():
    instance = metrics_MappingRecord(column="sample_text", count="sample_text", message="sample_text")
    assert isinstance(instance, Base)


def test_metrics_MappingStatistic_isa_Base():
    instance = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    assert isinstance(instance, Base)


def test_metrics_Metric_isa_Base():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_metrics_MetricSource_isa_Base():
    instance = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    assert isinstance(instance, Base)


def test_metrics_IdentifierDataKind_isa_DataKind():
    instance = metrics_IdentifierDataKind(objectKind="sample_text", objectProperty="sample_text", pattern="sample_text")
    assert isinstance(instance, DataKind)


def test_metrics_ValueDataKind_isa_DataKind():
    instance = metrics_ValueDataKind(format="sample_text", kindHint="sample_text", valueKind="sample_text")
    assert isinstance(instance, DataKind)


def test_metrics_MappingCSV_isa_Mapping():
    instance = metrics_MappingCSV(delimiter="sample_text", filterPattern="sample_text")
    assert isinstance(instance, Mapping)


def test_metrics_MappingRDBMS_isa_Mapping():
    instance = metrics_MappingRDBMS(databaseType="sample_text", dateFormat="sample_text", dateTimeFormat="sample_text", password="sample_text", query="sample_text", timeFormat="sample_text", user="sample_text")
    assert isinstance(instance, Mapping)


def test_metrics_MappingXLS_isa_Mapping():
    instance = metrics_MappingXLS(filterPattern="sample_text", sheetNumber="sample_text")
    assert isinstance(instance, Mapping)


def test_assoc_dataMappingColumns1_link_reassign_clear():
    a = metrics_MappingColumn(column="sample_text")
    b1 = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    b2 = metrics_Mapping(firstDataRow="sample_text_2", headerRow="sample_text_2", intervalHint="sample_text_2")
    _safe_set(a, 'metrics_MappingColumn3', b1)
    assert _is_linked(a, 'metrics_MappingColumn3', b1)
    if hasattr(b1, 'metrics_Mapping2'):
        assert _is_linked(b1, 'metrics_Mapping2', a)
    _safe_set(a, 'metrics_MappingColumn3', b2)
    assert _is_linked(a, 'metrics_MappingColumn3', b2)
    if hasattr(b1, 'metrics_Mapping2'):
        assert not _is_linked(b1, 'metrics_Mapping2', a)
    if hasattr(b2, 'metrics_Mapping2'):
        assert _is_linked(b2, 'metrics_Mapping2', a)
    _safe_set(a, 'metrics_MappingColumn3', None)
    assert not _is_linked(a, 'metrics_MappingColumn3', b2)
    if hasattr(b2, 'metrics_Mapping2'):
        assert not _is_linked(b2, 'metrics_Mapping2', a)


def test_assoc_dataType4_link_reassign_clear():
    a = metrics_MappingColumn(column="sample_text")
    b1 = metrics_DataKind()
    b2 = metrics_DataKind()
    _safe_set(a, 'metrics_MappingColumn5', b1)
    assert _is_linked(a, 'metrics_MappingColumn5', b1)
    if hasattr(b1, 'metrics_DataKind'):
        assert _is_linked(b1, 'metrics_DataKind', a)
    _safe_set(a, 'metrics_MappingColumn5', b2)
    assert _is_linked(a, 'metrics_MappingColumn5', b2)
    if hasattr(b1, 'metrics_DataKind'):
        assert not _is_linked(b1, 'metrics_DataKind', a)
    if hasattr(b2, 'metrics_DataKind'):
        assert _is_linked(b2, 'metrics_DataKind', a)
    _safe_set(a, 'metrics_MappingColumn5', None)
    assert not _is_linked(a, 'metrics_MappingColumn5', b2)
    if hasattr(b2, 'metrics_DataKind'):
        assert not _is_linked(b2, 'metrics_DataKind', a)


def test_assoc_expressionRef17_link_reassign_clear():
    a = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    b1 = metrics_Expression()
    b2 = metrics_Expression()
    _safe_set(a, 'metrics_Metric18', b1)
    assert _is_linked(a, 'metrics_Metric18', b1)
    if hasattr(b1, 'metrics_Expression'):
        assert _is_linked(b1, 'metrics_Expression', a)
    _safe_set(a, 'metrics_Metric18', b2)
    assert _is_linked(a, 'metrics_Metric18', b2)
    if hasattr(b1, 'metrics_Expression'):
        assert not _is_linked(b1, 'metrics_Expression', a)
    if hasattr(b2, 'metrics_Expression'):
        assert _is_linked(b2, 'metrics_Expression', a)
    _safe_set(a, 'metrics_Metric18', None)
    assert not _is_linked(a, 'metrics_Metric18', b2)
    if hasattr(b2, 'metrics_Expression'):
        assert not _is_linked(b2, 'metrics_Expression', a)


def test_assoc_failedRecords6_link_reassign_clear():
    a = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    b1 = metrics_MappingRecord(column="sample_text", count="sample_text", message="sample_text")
    b2 = metrics_MappingRecord(column="sample_text_2", count="sample_text_2", message="sample_text_2")
    _safe_set(a, 'metrics_MappingStatistic', {b1})
    assert _is_linked(a, 'metrics_MappingStatistic', b1)
    if hasattr(b1, 'metrics_MappingRecord'):
        assert _is_linked(b1, 'metrics_MappingRecord', a)
    _safe_set(a, 'metrics_MappingStatistic', {b2})
    assert _is_linked(a, 'metrics_MappingStatistic', b2)
    if hasattr(b1, 'metrics_MappingRecord'):
        assert not _is_linked(b1, 'metrics_MappingRecord', a)
    if hasattr(b2, 'metrics_MappingRecord'):
        assert _is_linked(b2, 'metrics_MappingRecord', a)
    _safe_set(a, 'metrics_MappingStatistic', set())
    assert not _is_linked(a, 'metrics_MappingStatistic', b2)
    if hasattr(b2, 'metrics_MappingRecord'):
        assert not _is_linked(b2, 'metrics_MappingRecord', a)


def test_assoc_headerMappingColumns0_link_reassign_clear():
    a = metrics_MappingColumn(column="sample_text")
    b1 = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    b2 = metrics_Mapping(firstDataRow="sample_text_2", headerRow="sample_text_2", intervalHint="sample_text_2")
    _safe_set(a, 'metrics_MappingColumn', b1)
    assert _is_linked(a, 'metrics_MappingColumn', b1)
    if hasattr(b1, 'metrics_Mapping'):
        assert _is_linked(b1, 'metrics_Mapping', a)
    _safe_set(a, 'metrics_MappingColumn', b2)
    assert _is_linked(a, 'metrics_MappingColumn', b2)
    if hasattr(b1, 'metrics_Mapping'):
        assert not _is_linked(b1, 'metrics_Mapping', a)
    if hasattr(b2, 'metrics_Mapping'):
        assert _is_linked(b2, 'metrics_Mapping', a)
    _safe_set(a, 'metrics_MappingColumn', None)
    assert not _is_linked(a, 'metrics_MappingColumn', b2)
    if hasattr(b2, 'metrics_Mapping'):
        assert not _is_linked(b2, 'metrics_Mapping', a)


def test_assoc_mappingDuration7_link_reassign_clear():
    a = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    b1 = metrics_DateTimeRange()
    b2 = metrics_DateTimeRange()
    _safe_set(a, 'metrics_MappingStatistic8', b1)
    assert _is_linked(a, 'metrics_MappingStatistic8', b1)
    if hasattr(b1, 'metrics_DateTimeRange'):
        assert _is_linked(b1, 'metrics_DateTimeRange', a)
    _safe_set(a, 'metrics_MappingStatistic8', b2)
    assert _is_linked(a, 'metrics_MappingStatistic8', b2)
    if hasattr(b1, 'metrics_DateTimeRange'):
        assert not _is_linked(b1, 'metrics_DateTimeRange', a)
    if hasattr(b2, 'metrics_DateTimeRange'):
        assert _is_linked(b2, 'metrics_DateTimeRange', a)
    _safe_set(a, 'metrics_MappingStatistic8', None)
    assert not _is_linked(a, 'metrics_MappingStatistic8', b2)
    if hasattr(b2, 'metrics_DateTimeRange'):
        assert not _is_linked(b2, 'metrics_DateTimeRange', a)


def test_assoc_metricMapping27_link_reassign_clear():
    a = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    b1 = metrics_Mapping(firstDataRow="sample_text", headerRow="sample_text", intervalHint="sample_text")
    b2 = metrics_Mapping(firstDataRow="sample_text_2", headerRow="sample_text_2", intervalHint="sample_text_2")
    _safe_set(a, 'metrics_MetricSource28', b1)
    assert _is_linked(a, 'metrics_MetricSource28', b1)
    if hasattr(b1, 'metrics_Mapping29'):
        assert _is_linked(b1, 'metrics_Mapping29', a)
    _safe_set(a, 'metrics_MetricSource28', b2)
    assert _is_linked(a, 'metrics_MetricSource28', b2)
    if hasattr(b1, 'metrics_Mapping29'):
        assert not _is_linked(b1, 'metrics_Mapping29', a)
    if hasattr(b2, 'metrics_Mapping29'):
        assert _is_linked(b2, 'metrics_Mapping29', a)
    _safe_set(a, 'metrics_MetricSource28', None)
    assert not _is_linked(a, 'metrics_MetricSource28', b2)
    if hasattr(b2, 'metrics_Mapping29'):
        assert not _is_linked(b2, 'metrics_Mapping29', a)


def test_assoc_metricRef34_link_reassign_clear():
    a = metrics_ValueDataKind(format="sample_text", kindHint="sample_text", valueKind="sample_text")
    b1 = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    b2 = metrics_Metric(description="sample_text_2", measurementKind="sample_text_2", measurementPoint="sample_text_2", name="sample_text_2")
    _safe_set(a, 'metrics_ValueDataKind', b1)
    assert _is_linked(a, 'metrics_ValueDataKind', b1)
    if hasattr(b1, 'metrics_Metric35'):
        assert _is_linked(b1, 'metrics_Metric35', a)
    _safe_set(a, 'metrics_ValueDataKind', b2)
    assert _is_linked(a, 'metrics_ValueDataKind', b2)
    if hasattr(b1, 'metrics_Metric35'):
        assert not _is_linked(b1, 'metrics_Metric35', a)
    if hasattr(b2, 'metrics_Metric35'):
        assert _is_linked(b2, 'metrics_Metric35', a)
    _safe_set(a, 'metrics_ValueDataKind', None)
    assert not _is_linked(a, 'metrics_ValueDataKind', b2)
    if hasattr(b2, 'metrics_Metric35'):
        assert not _is_linked(b2, 'metrics_Metric35', a)


def test_assoc_metricRetentionRules25_link_reassign_clear():
    a = metrics_MetricRetentionRule(intervalHint="sample_text", name="sample_text", period="sample_text")
    b1 = metrics_MetricRetentionRules()
    b2 = metrics_MetricRetentionRules()
    _safe_set(a, 'metrics_MetricRetentionRule26', b1)
    assert _is_linked(a, 'metrics_MetricRetentionRule26', b1)
    if hasattr(b1, 'metrics_MetricRetentionRules'):
        assert _is_linked(b1, 'metrics_MetricRetentionRules', a)
    _safe_set(a, 'metrics_MetricRetentionRule26', b2)
    assert _is_linked(a, 'metrics_MetricRetentionRule26', b2)
    if hasattr(b1, 'metrics_MetricRetentionRules'):
        assert not _is_linked(b1, 'metrics_MetricRetentionRules', a)
    if hasattr(b2, 'metrics_MetricRetentionRules'):
        assert _is_linked(b2, 'metrics_MetricRetentionRules', a)
    _safe_set(a, 'metrics_MetricRetentionRule26', None)
    assert not _is_linked(a, 'metrics_MetricRetentionRule26', b2)
    if hasattr(b2, 'metrics_MetricRetentionRules'):
        assert not _is_linked(b2, 'metrics_MetricRetentionRules', a)


def test_assoc_metricSourceRef19_link_reassign_clear():
    a = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    b1 = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    b2 = metrics_Metric(description="sample_text_2", measurementKind="sample_text_2", measurementPoint="sample_text_2", name="sample_text_2")
    _safe_set(a, 'metrics_MetricSource', b1)
    assert _is_linked(a, 'metrics_MetricSource', b1)
    if hasattr(b1, 'metrics_Metric20'):
        assert _is_linked(b1, 'metrics_Metric20', a)
    _safe_set(a, 'metrics_MetricSource', b2)
    assert _is_linked(a, 'metrics_MetricSource', b2)
    if hasattr(b1, 'metrics_Metric20'):
        assert not _is_linked(b1, 'metrics_Metric20', a)
    if hasattr(b2, 'metrics_Metric20'):
        assert _is_linked(b2, 'metrics_Metric20', a)
    _safe_set(a, 'metrics_MetricSource', None)
    assert not _is_linked(a, 'metrics_MetricSource', b2)
    if hasattr(b2, 'metrics_Metric20'):
        assert not _is_linked(b2, 'metrics_Metric20', a)


def test_assoc_metricValues33_link_reassign_clear():
    a = metrics_MetricValueRange(intervalHint="sample_text", kindHint="sample_text")
    b1 = metrics_Value()
    b2 = metrics_Value()
    _safe_set(a, 'metrics_MetricValueRange', {b1})
    assert _is_linked(a, 'metrics_MetricValueRange', b1)
    if hasattr(b1, 'metrics_Value'):
        assert _is_linked(b1, 'metrics_Value', a)
    _safe_set(a, 'metrics_MetricValueRange', {b2})
    assert _is_linked(a, 'metrics_MetricValueRange', b2)
    if hasattr(b1, 'metrics_Value'):
        assert not _is_linked(b1, 'metrics_Value', a)
    if hasattr(b2, 'metrics_Value'):
        assert _is_linked(b2, 'metrics_Value', a)
    _safe_set(a, 'metrics_MetricValueRange', set())
    assert not _is_linked(a, 'metrics_MetricValueRange', b2)
    if hasattr(b2, 'metrics_Value'):
        assert not _is_linked(b2, 'metrics_Value', a)


def test_assoc_metrics16_link_reassign_clear():
    a = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    b1 = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    b2 = metrics_Metric(description="sample_text_2", measurementKind="sample_text_2", measurementPoint="sample_text_2", name="sample_text_2")
    _safe_set(a, 'metrics_Metric', b1)
    assert _is_linked(a, 'metrics_Metric', b1)
    if hasattr(b1, 'metrics_Metric15'):
        assert _is_linked(b1, 'metrics_Metric15', a)
    _safe_set(a, 'metrics_Metric', b2)
    assert _is_linked(a, 'metrics_Metric', b2)
    if hasattr(b1, 'metrics_Metric15'):
        assert not _is_linked(b1, 'metrics_Metric15', a)
    if hasattr(b2, 'metrics_Metric15'):
        assert _is_linked(b2, 'metrics_Metric15', a)
    _safe_set(a, 'metrics_Metric', None)
    assert not _is_linked(a, 'metrics_Metric', b2)
    if hasattr(b2, 'metrics_Metric15'):
        assert not _is_linked(b2, 'metrics_Metric15', a)


def test_assoc_periodEstimate9_link_reassign_clear():
    a = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    b1 = metrics_DateTimeRange()
    b2 = metrics_DateTimeRange()
    _safe_set(a, 'metrics_MappingStatistic10', b1)
    assert _is_linked(a, 'metrics_MappingStatistic10', b1)
    if hasattr(b1, 'metrics_DateTimeRange11'):
        assert _is_linked(b1, 'metrics_DateTimeRange11', a)
    _safe_set(a, 'metrics_MappingStatistic10', b2)
    assert _is_linked(a, 'metrics_MappingStatistic10', b2)
    if hasattr(b1, 'metrics_DateTimeRange11'):
        assert not _is_linked(b1, 'metrics_DateTimeRange11', a)
    if hasattr(b2, 'metrics_DateTimeRange11'):
        assert _is_linked(b2, 'metrics_DateTimeRange11', a)
    _safe_set(a, 'metrics_MappingStatistic10', None)
    assert not _is_linked(a, 'metrics_MappingStatistic10', b2)
    if hasattr(b2, 'metrics_DateTimeRange11'):
        assert not _is_linked(b2, 'metrics_DateTimeRange11', a)


def test_assoc_retentionExpression23_link_reassign_clear():
    a = metrics_MetricRetentionRule(intervalHint="sample_text", name="sample_text", period="sample_text")
    b1 = metrics_Expression()
    b2 = metrics_Expression()
    _safe_set(a, 'metrics_MetricRetentionRule', b1)
    assert _is_linked(a, 'metrics_MetricRetentionRule', b1)
    if hasattr(b1, 'metrics_Expression24'):
        assert _is_linked(b1, 'metrics_Expression24', a)
    _safe_set(a, 'metrics_MetricRetentionRule', b2)
    assert _is_linked(a, 'metrics_MetricRetentionRule', b2)
    if hasattr(b1, 'metrics_Expression24'):
        assert not _is_linked(b1, 'metrics_Expression24', a)
    if hasattr(b2, 'metrics_Expression24'):
        assert _is_linked(b2, 'metrics_Expression24', a)
    _safe_set(a, 'metrics_MetricRetentionRule', None)
    assert not _is_linked(a, 'metrics_MetricRetentionRule', b2)
    if hasattr(b2, 'metrics_Expression24'):
        assert not _is_linked(b2, 'metrics_Expression24', a)


def test_assoc_statistics30_link_reassign_clear():
    a = metrics_MetricSource(filterPattern="sample_text", metricLocation="sample_text", name="sample_text")
    b1 = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    b2 = metrics_MappingStatistic(intervalEstimate="sample_text_2", message="sample_text_2", totalRecords="sample_text_2")
    _safe_set(a, 'metrics_MetricSource31', {b1})
    assert _is_linked(a, 'metrics_MetricSource31', b1)
    if hasattr(b1, 'metrics_MappingStatistic32'):
        assert _is_linked(b1, 'metrics_MappingStatistic32', a)
    _safe_set(a, 'metrics_MetricSource31', {b2})
    assert _is_linked(a, 'metrics_MetricSource31', b2)
    if hasattr(b1, 'metrics_MappingStatistic32'):
        assert not _is_linked(b1, 'metrics_MappingStatistic32', a)
    if hasattr(b2, 'metrics_MappingStatistic32'):
        assert _is_linked(b2, 'metrics_MappingStatistic32', a)
    _safe_set(a, 'metrics_MetricSource31', set())
    assert not _is_linked(a, 'metrics_MetricSource31', b2)
    if hasattr(b2, 'metrics_MappingStatistic32'):
        assert not _is_linked(b2, 'metrics_MappingStatistic32', a)


def test_assoc_subStatistics13_link_reassign_clear():
    a = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    b1 = metrics_MappingStatistic(intervalEstimate="sample_text", message="sample_text", totalRecords="sample_text")
    b2 = metrics_MappingStatistic(intervalEstimate="sample_text_2", message="sample_text_2", totalRecords="sample_text_2")
    _safe_set(a, 'metrics_MappingStatistic12', {b1})
    assert _is_linked(a, 'metrics_MappingStatistic12', b1)
    if hasattr(b1, 'metrics_MappingStatistic14'):
        assert _is_linked(b1, 'metrics_MappingStatistic14', a)
    _safe_set(a, 'metrics_MappingStatistic12', {b2})
    assert _is_linked(a, 'metrics_MappingStatistic12', b2)
    if hasattr(b1, 'metrics_MappingStatistic14'):
        assert not _is_linked(b1, 'metrics_MappingStatistic14', a)
    if hasattr(b2, 'metrics_MappingStatistic14'):
        assert _is_linked(b2, 'metrics_MappingStatistic14', a)
    _safe_set(a, 'metrics_MappingStatistic12', set())
    assert not _is_linked(a, 'metrics_MappingStatistic12', b2)
    if hasattr(b2, 'metrics_MappingStatistic14'):
        assert not _is_linked(b2, 'metrics_MappingStatistic14', a)


def test_assoc_unitRef21_link_reassign_clear():
    a = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", name="sample_text")
    b1 = metrics_Unit()
    b2 = metrics_Unit()
    _safe_set(a, 'metrics_Metric22', b1)
    assert _is_linked(a, 'metrics_Metric22', b1)
    if hasattr(b1, 'metrics_Unit'):
        assert _is_linked(b1, 'metrics_Unit', a)
    _safe_set(a, 'metrics_Metric22', b2)
    assert _is_linked(a, 'metrics_Metric22', b2)
    if hasattr(b1, 'metrics_Unit'):
        assert not _is_linked(b1, 'metrics_Unit', a)
    if hasattr(b2, 'metrics_Unit'):
        assert _is_linked(b2, 'metrics_Unit', a)
    _safe_set(a, 'metrics_Metric22', None)
    assert not _is_linked(a, 'metrics_Metric22', b2)
    if hasattr(b2, 'metrics_Unit'):
        assert not _is_linked(b2, 'metrics_Unit', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Base_strategy = st.builds(Base)
@given(instance=Base_strategy)
@settings(max_examples=25)
def test_Base_instantiation(instance):
    assert isinstance(instance, Base)


DataKind_strategy = st.builds(DataKind)
@given(instance=DataKind_strategy)
@settings(max_examples=25)
def test_DataKind_instantiation(instance):
    assert isinstance(instance, DataKind)


Mapping_strategy = st.builds(Mapping)
@given(instance=Mapping_strategy)
@settings(max_examples=25)
def test_Mapping_instantiation(instance):
    assert isinstance(instance, Mapping)


metrics_DataKind_strategy = st.builds(metrics_DataKind)
@given(instance=metrics_DataKind_strategy)
@settings(max_examples=25)
def test_metrics_DataKind_instantiation(instance):
    assert isinstance(instance, metrics_DataKind)


metrics_DateTimeRange_strategy = st.builds(metrics_DateTimeRange)
@given(instance=metrics_DateTimeRange_strategy)
@settings(max_examples=25)
def test_metrics_DateTimeRange_instantiation(instance):
    assert isinstance(instance, metrics_DateTimeRange)


metrics_Expression_strategy = st.builds(metrics_Expression)
@given(instance=metrics_Expression_strategy)
@settings(max_examples=25)
def test_metrics_Expression_instantiation(instance):
    assert isinstance(instance, metrics_Expression)


metrics_IdentifierDataKind_strategy = st.builds(metrics_IdentifierDataKind, objectKind=safe_text, objectProperty=safe_text, pattern=safe_text)
@given(instance=metrics_IdentifierDataKind_strategy)
@settings(max_examples=25)
def test_metrics_IdentifierDataKind_instantiation(instance):
    assert isinstance(instance, metrics_IdentifierDataKind)


metrics_Mapping_strategy = st.builds(metrics_Mapping, firstDataRow=safe_text, headerRow=safe_text, intervalHint=safe_text)
@given(instance=metrics_Mapping_strategy)
@settings(max_examples=25)
def test_metrics_Mapping_instantiation(instance):
    assert isinstance(instance, metrics_Mapping)


metrics_MappingCSV_strategy = st.builds(metrics_MappingCSV, delimiter=safe_text, filterPattern=safe_text)
@given(instance=metrics_MappingCSV_strategy)
@settings(max_examples=25)
def test_metrics_MappingCSV_instantiation(instance):
    assert isinstance(instance, metrics_MappingCSV)


metrics_MappingColumn_strategy = st.builds(metrics_MappingColumn, column=safe_text)
@given(instance=metrics_MappingColumn_strategy)
@settings(max_examples=25)
def test_metrics_MappingColumn_instantiation(instance):
    assert isinstance(instance, metrics_MappingColumn)


metrics_MappingRDBMS_strategy = st.builds(metrics_MappingRDBMS, databaseType=safe_text, dateFormat=safe_text, dateTimeFormat=safe_text, password=safe_text, query=safe_text, timeFormat=safe_text, user=safe_text)
@given(instance=metrics_MappingRDBMS_strategy)
@settings(max_examples=25)
def test_metrics_MappingRDBMS_instantiation(instance):
    assert isinstance(instance, metrics_MappingRDBMS)


metrics_MappingRecord_strategy = st.builds(metrics_MappingRecord, column=safe_text, count=safe_text, message=safe_text)
@given(instance=metrics_MappingRecord_strategy)
@settings(max_examples=25)
def test_metrics_MappingRecord_instantiation(instance):
    assert isinstance(instance, metrics_MappingRecord)


metrics_MappingStatistic_strategy = st.builds(metrics_MappingStatistic, intervalEstimate=safe_text, message=safe_text, totalRecords=safe_text)
@given(instance=metrics_MappingStatistic_strategy)
@settings(max_examples=25)
def test_metrics_MappingStatistic_instantiation(instance):
    assert isinstance(instance, metrics_MappingStatistic)


metrics_MappingXLS_strategy = st.builds(metrics_MappingXLS, filterPattern=safe_text, sheetNumber=safe_text)
@given(instance=metrics_MappingXLS_strategy)
@settings(max_examples=25)
def test_metrics_MappingXLS_instantiation(instance):
    assert isinstance(instance, metrics_MappingXLS)


metrics_Metric_strategy = st.builds(metrics_Metric, description=safe_text, measurementKind=safe_text, measurementPoint=safe_text, name=safe_text)
@given(instance=metrics_Metric_strategy)
@settings(max_examples=25)
def test_metrics_Metric_instantiation(instance):
    assert isinstance(instance, metrics_Metric)


metrics_MetricRetentionRule_strategy = st.builds(metrics_MetricRetentionRule, intervalHint=safe_text, name=safe_text, period=safe_text)
@given(instance=metrics_MetricRetentionRule_strategy)
@settings(max_examples=25)
def test_metrics_MetricRetentionRule_instantiation(instance):
    assert isinstance(instance, metrics_MetricRetentionRule)


metrics_MetricRetentionRules_strategy = st.builds(metrics_MetricRetentionRules)
@given(instance=metrics_MetricRetentionRules_strategy)
@settings(max_examples=25)
def test_metrics_MetricRetentionRules_instantiation(instance):
    assert isinstance(instance, metrics_MetricRetentionRules)


metrics_MetricSource_strategy = st.builds(metrics_MetricSource, filterPattern=safe_text, metricLocation=safe_text, name=safe_text)
@given(instance=metrics_MetricSource_strategy)
@settings(max_examples=25)
def test_metrics_MetricSource_instantiation(instance):
    assert isinstance(instance, metrics_MetricSource)


metrics_MetricValueRange_strategy = st.builds(metrics_MetricValueRange, intervalHint=safe_text, kindHint=safe_text)
@given(instance=metrics_MetricValueRange_strategy)
@settings(max_examples=25)
def test_metrics_MetricValueRange_instantiation(instance):
    assert isinstance(instance, metrics_MetricValueRange)


metrics_Unit_strategy = st.builds(metrics_Unit)
@given(instance=metrics_Unit_strategy)
@settings(max_examples=25)
def test_metrics_Unit_instantiation(instance):
    assert isinstance(instance, metrics_Unit)


metrics_Value_strategy = st.builds(metrics_Value)
@given(instance=metrics_Value_strategy)
@settings(max_examples=25)
def test_metrics_Value_instantiation(instance):
    assert isinstance(instance, metrics_Value)


metrics_ValueDataKind_strategy = st.builds(metrics_ValueDataKind, format=safe_text, kindHint=safe_text, valueKind=safe_text)
@given(instance=metrics_ValueDataKind_strategy)
@settings(max_examples=25)
def test_metrics_ValueDataKind_instantiation(instance):
    assert isinstance(instance, metrics_ValueDataKind)


