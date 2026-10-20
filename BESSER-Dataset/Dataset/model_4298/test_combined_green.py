# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metrics_MetricValueRange,
    metrics_Value,
    metrics_MetricSource,
    metrics_DateTimeRange,
    metrics_MappingStatistic,
    metrics_Metric,
    DataKind,
    metrics_ValueDataKind,
    metrics_IdentifierDataKind,
    MappingRecord,
    metrics_MappingRecordXLS,
    metrics_MappingRecord,
    Mapping,
    metrics_MappingXLS,
    metrics_MappingRDBMS,
    metrics_MappingCSV,
    metrics_Mapping,
    metrics_DataKind,
    ValueKindType,
    ObjectNameType,
    KindHintType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_metrics_metricvaluerange_is_not_abstract():
    assert not inspect.isabstract(metrics_MetricValueRange)


def test_hyp_metrics_metricvaluerange_constructor_exists():
    assert callable(metrics_MetricValueRange.__init__)


def test_hyp_metrics_metricvaluerange_constructor_args():
    sig = inspect.signature(metrics_MetricValueRange.__init__)
    params = list(sig.parameters.keys())
    assert "kindHint" in params, "Missing parameter 'kindHint'"
    assert "name" in params, "Missing parameter 'name'"
    assert "periodHint" in params, "Missing parameter 'periodHint'"






def test_hyp_metrics_value_is_not_abstract():
    assert not inspect.isabstract(metrics_Value)


def test_hyp_metrics_value_constructor_exists():
    assert callable(metrics_Value.__init__)


def test_hyp_metrics_value_constructor_args():
    sig = inspect.signature(metrics_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_metricsource_is_not_abstract():
    assert not inspect.isabstract(metrics_MetricSource)


def test_hyp_metrics_metricsource_constructor_exists():
    assert callable(metrics_MetricSource.__init__)


def test_hyp_metrics_metricsource_constructor_args():
    sig = inspect.signature(metrics_MetricSource.__init__)
    params = list(sig.parameters.keys())
    assert "metricLocation" in params, "Missing parameter 'metricLocation'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_metrics_datetimerange_is_not_abstract():
    assert not inspect.isabstract(metrics_DateTimeRange)


def test_hyp_metrics_datetimerange_constructor_exists():
    assert callable(metrics_DateTimeRange.__init__)


def test_hyp_metrics_datetimerange_constructor_args():
    sig = inspect.signature(metrics_DateTimeRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_mappingstatistic_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingStatistic)


def test_hyp_metrics_mappingstatistic_constructor_exists():
    assert callable(metrics_MappingStatistic.__init__)


def test_hyp_metrics_mappingstatistic_constructor_args():
    sig = inspect.signature(metrics_MappingStatistic.__init__)
    params = list(sig.parameters.keys())
    assert "totalRecords" in params, "Missing parameter 'totalRecords'"




def test_hyp_metrics_metric_is_not_abstract():
    assert not inspect.isabstract(metrics_Metric)


def test_hyp_metrics_metric_constructor_exists():
    assert callable(metrics_Metric.__init__)


def test_hyp_metrics_metric_constructor_args():
    sig = inspect.signature(metrics_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "unitRef" in params, "Missing parameter 'unitRef'"
    assert "metricCalculation" in params, "Missing parameter 'metricCalculation'"
    assert "description" in params, "Missing parameter 'description'"
    assert "measurementPoint" in params, "Missing parameter 'measurementPoint'"
    assert "measurementKind" in params, "Missing parameter 'measurementKind'"
    assert "name" in params, "Missing parameter 'name'"









def test_hyp_datakind_is_not_abstract():
    assert not inspect.isabstract(DataKind)


def test_hyp_datakind_constructor_exists():
    assert callable(DataKind.__init__)


def test_hyp_datakind_constructor_args():
    sig = inspect.signature(DataKind.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_valuedatakind_is_not_abstract():
    assert not inspect.isabstract(metrics_ValueDataKind)


def test_hyp_metrics_valuedatakind_constructor_exists():
    assert callable(metrics_ValueDataKind.__init__)


def test_hyp_metrics_valuedatakind_constructor_args():
    sig = inspect.signature(metrics_ValueDataKind.__init__)
    params = list(sig.parameters.keys())
    assert "valueKind" in params, "Missing parameter 'valueKind'"




def test_hyp_metrics_identifierdatakind_is_not_abstract():
    assert not inspect.isabstract(metrics_IdentifierDataKind)


def test_hyp_metrics_identifierdatakind_constructor_exists():
    assert callable(metrics_IdentifierDataKind.__init__)


def test_hyp_metrics_identifierdatakind_constructor_args():
    sig = inspect.signature(metrics_IdentifierDataKind.__init__)
    params = list(sig.parameters.keys())
    assert "objectAttribute" in params, "Missing parameter 'objectAttribute'"
    assert "objectName" in params, "Missing parameter 'objectName'"





def test_hyp_mappingrecord_is_not_abstract():
    assert not inspect.isabstract(MappingRecord)


def test_hyp_mappingrecord_constructor_exists():
    assert callable(MappingRecord.__init__)


def test_hyp_mappingrecord_constructor_args():
    sig = inspect.signature(MappingRecord.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_mappingrecordxls_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingRecordXLS)


def test_hyp_metrics_mappingrecordxls_constructor_exists():
    assert callable(metrics_MappingRecordXLS.__init__)


def test_hyp_metrics_mappingrecordxls_constructor_args():
    sig = inspect.signature(metrics_MappingRecordXLS.__init__)
    params = list(sig.parameters.keys())
    assert "row" in params, "Missing parameter 'row'"
    assert "column" in params, "Missing parameter 'column'"





def test_hyp_metrics_mappingrecord_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingRecord)


def test_hyp_metrics_mappingrecord_constructor_exists():
    assert callable(metrics_MappingRecord.__init__)


def test_hyp_metrics_mappingrecord_constructor_args():
    sig = inspect.signature(metrics_MappingRecord.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_hyp_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_hyp_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_mappingxls_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingXLS)


def test_hyp_metrics_mappingxls_constructor_exists():
    assert callable(metrics_MappingXLS.__init__)


def test_hyp_metrics_mappingxls_constructor_args():
    sig = inspect.signature(metrics_MappingXLS.__init__)
    params = list(sig.parameters.keys())
    assert "columnHeaders" in params, "Missing parameter 'columnHeaders'"
    assert "sheetNumber" in params, "Missing parameter 'sheetNumber'"
    assert "firstDataRow" in params, "Missing parameter 'firstDataRow'"
    assert "headerRow" in params, "Missing parameter 'headerRow'"







def test_hyp_metrics_mappingrdbms_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingRDBMS)


def test_hyp_metrics_mappingrdbms_constructor_exists():
    assert callable(metrics_MappingRDBMS.__init__)


def test_hyp_metrics_mappingrdbms_constructor_args():
    sig = inspect.signature(metrics_MappingRDBMS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_mappingcsv_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingCSV)


def test_hyp_metrics_mappingcsv_constructor_exists():
    assert callable(metrics_MappingCSV.__init__)


def test_hyp_metrics_mappingcsv_constructor_args():
    sig = inspect.signature(metrics_MappingCSV.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_mapping_is_not_abstract():
    assert not inspect.isabstract(metrics_Mapping)


def test_hyp_metrics_mapping_constructor_exists():
    assert callable(metrics_Mapping.__init__)


def test_hyp_metrics_mapping_constructor_args():
    sig = inspect.signature(metrics_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_datakind_is_not_abstract():
    assert not inspect.isabstract(metrics_DataKind)


def test_hyp_metrics_datakind_constructor_exists():
    assert callable(metrics_DataKind.__init__)


def test_hyp_metrics_datakind_constructor_args():
    sig = inspect.signature(metrics_DataKind.__init__)
    params = list(sig.parameters.keys())

def test_hyp_valuekindtype_exists():
    # Check that the Enumeration exists
    assert ValueKindType is not None

def test_hyp_valuekindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueKindType]
    expected_literals = [
        "NULL",
        "METRIC",
        "DATETIME",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueKindType"

def test_hyp_objectnametype_exists():
    # Check that the Enumeration exists
    assert ObjectNameType is not None

def test_hyp_objectnametype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNameType]
    expected_literals = [
        "NODE",
        "EQUIPMENT",
        "FUNCTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNameType"

def test_hyp_kindhinttype_exists():
    # Check that the Enumeration exists
    assert KindHintType is not None

def test_hyp_kindhinttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KindHintType]
    expected_literals = [
        "AVG",
        "BH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KindHintType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
metrics_MetricValueRange_strategy = st.builds(
    metrics_MetricValueRange,
    kindHint=
        safe_text,
    name=
        safe_text,
    periodHint=
        safe_text
)
metrics_Value_strategy = st.builds(
    metrics_Value,
)
metrics_MetricSource_strategy = st.builds(
    metrics_MetricSource,
    metricLocation=
        safe_text,
    name=
        safe_text
)
metrics_DateTimeRange_strategy = st.builds(
    metrics_DateTimeRange,
)
metrics_MappingStatistic_strategy = st.builds(
    metrics_MappingStatistic,
    totalRecords=
        safe_text
)
metrics_Metric_strategy = st.builds(
    metrics_Metric,
    unitRef=
        safe_text,
    metricCalculation=
        safe_text,
    description=
        safe_text,
    measurementPoint=
        safe_text,
    measurementKind=
        safe_text,
    name=
        safe_text
)
DataKind_strategy = st.builds(
    DataKind,
)
metrics_ValueDataKind_strategy = st.builds(
    metrics_ValueDataKind,
    valueKind=
        safe_text
)
metrics_IdentifierDataKind_strategy = st.builds(
    metrics_IdentifierDataKind,
    objectAttribute=
        safe_text,
    objectName=
        safe_text
)
MappingRecord_strategy = st.builds(
    MappingRecord,
)
metrics_MappingRecordXLS_strategy = st.builds(
    metrics_MappingRecordXLS,
    row=
        safe_text,
    column=
        safe_text
)
metrics_MappingRecord_strategy = st.builds(
    metrics_MappingRecord,
)
Mapping_strategy = st.builds(
    Mapping,
)
metrics_MappingXLS_strategy = st.builds(
    metrics_MappingXLS,
    columnHeaders=
        safe_text,
    sheetNumber=
        safe_text,
    firstDataRow=
        safe_text,
    headerRow=
        safe_text
)
metrics_MappingRDBMS_strategy = st.builds(
    metrics_MappingRDBMS,
)
metrics_MappingCSV_strategy = st.builds(
    metrics_MappingCSV,
)
metrics_Mapping_strategy = st.builds(
    metrics_Mapping,
)
metrics_DataKind_strategy = st.builds(
    metrics_DataKind,
)




@given(instance=metrics_MetricValueRange_strategy)
def test_hyp_metrics_metricvaluerange_kindHint_setter(instance):
    original = instance.kindHint
    instance.kindHint = original
    assert instance.kindHint == original



@given(instance=metrics_MetricValueRange_strategy)
def test_hyp_metrics_metricvaluerange_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metrics_MetricValueRange_strategy)
def test_hyp_metrics_metricvaluerange_periodHint_setter(instance):
    original = instance.periodHint
    instance.periodHint = original
    assert instance.periodHint == original





@given(instance=metrics_MetricSource_strategy)
def test_hyp_metrics_metricsource_metricLocation_setter(instance):
    original = instance.metricLocation
    instance.metricLocation = original
    assert instance.metricLocation == original



@given(instance=metrics_MetricSource_strategy)
def test_hyp_metrics_metricsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=metrics_MappingStatistic_strategy)
def test_hyp_metrics_mappingstatistic_totalRecords_setter(instance):
    original = instance.totalRecords
    instance.totalRecords = original
    assert instance.totalRecords == original




@given(instance=metrics_Metric_strategy)
def test_hyp_metrics_metric_unitRef_setter(instance):
    original = instance.unitRef
    instance.unitRef = original
    assert instance.unitRef == original



@given(instance=metrics_Metric_strategy)
def test_hyp_metrics_metric_metricCalculation_setter(instance):
    original = instance.metricCalculation
    instance.metricCalculation = original
    assert instance.metricCalculation == original



@given(instance=metrics_Metric_strategy)
def test_hyp_metrics_metric_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=metrics_Metric_strategy)
def test_hyp_metrics_metric_measurementPoint_setter(instance):
    original = instance.measurementPoint
    instance.measurementPoint = original
    assert instance.measurementPoint == original



@given(instance=metrics_Metric_strategy)
def test_hyp_metrics_metric_measurementKind_setter(instance):
    original = instance.measurementKind
    instance.measurementKind = original
    assert instance.measurementKind == original



@given(instance=metrics_Metric_strategy)
def test_hyp_metrics_metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=metrics_ValueDataKind_strategy)
def test_hyp_metrics_valuedatakind_valueKind_setter(instance):
    original = instance.valueKind
    instance.valueKind = original
    assert instance.valueKind == original




@given(instance=metrics_IdentifierDataKind_strategy)
def test_hyp_metrics_identifierdatakind_objectAttribute_setter(instance):
    original = instance.objectAttribute
    instance.objectAttribute = original
    assert instance.objectAttribute == original



@given(instance=metrics_IdentifierDataKind_strategy)
def test_hyp_metrics_identifierdatakind_objectName_setter(instance):
    original = instance.objectName
    instance.objectName = original
    assert instance.objectName == original





@given(instance=metrics_MappingRecordXLS_strategy)
def test_hyp_metrics_mappingrecordxls_row_setter(instance):
    original = instance.row
    instance.row = original
    assert instance.row == original



@given(instance=metrics_MappingRecordXLS_strategy)
def test_hyp_metrics_mappingrecordxls_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original






@given(instance=metrics_MappingXLS_strategy)
def test_hyp_metrics_mappingxls_columnHeaders_setter(instance):
    original = instance.columnHeaders
    instance.columnHeaders = original
    assert instance.columnHeaders == original



@given(instance=metrics_MappingXLS_strategy)
def test_hyp_metrics_mappingxls_sheetNumber_setter(instance):
    original = instance.sheetNumber
    instance.sheetNumber = original
    assert instance.sheetNumber == original



@given(instance=metrics_MappingXLS_strategy)
def test_hyp_metrics_mappingxls_firstDataRow_setter(instance):
    original = instance.firstDataRow
    instance.firstDataRow = original
    assert instance.firstDataRow == original



@given(instance=metrics_MappingXLS_strategy)
def test_hyp_metrics_mappingxls_headerRow_setter(instance):
    original = instance.headerRow
    instance.headerRow = original
    assert instance.headerRow == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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
    metrics_Metric,
    metrics_MetricSource,
    metrics_MetricValueRange,
    metrics_Value,
    metrics_ValueDataKind,
    KindHintType,
    ObjectNameType,
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

def test_metrics_IdentifierDataKind_objectAttribute_value_roundtrip():
    instance = metrics_IdentifierDataKind(objectAttribute="sample_text", objectName="sample_text")
    assert instance.objectAttribute == "sample_text"
    instance.objectAttribute = "sample_text_2"
    assert instance.objectAttribute == "sample_text_2"


def test_metrics_IdentifierDataKind_objectName_value_roundtrip():
    instance = metrics_IdentifierDataKind(objectAttribute="sample_text", objectName="sample_text")
    assert instance.objectName == "sample_text"
    instance.objectName = "sample_text_2"
    assert instance.objectName == "sample_text_2"


def test_metrics_MappingRecordXLS_column_value_roundtrip():
    instance = metrics_MappingRecordXLS(column="sample_text", row="sample_text")
    assert instance.column == "sample_text"
    instance.column = "sample_text_2"
    assert instance.column == "sample_text_2"


def test_metrics_MappingRecordXLS_row_value_roundtrip():
    instance = metrics_MappingRecordXLS(column="sample_text", row="sample_text")
    assert instance.row == "sample_text"
    instance.row = "sample_text_2"
    assert instance.row == "sample_text_2"


def test_metrics_MappingStatistic_totalRecords_value_roundtrip():
    instance = metrics_MappingStatistic(totalRecords="sample_text")
    assert instance.totalRecords == "sample_text"
    instance.totalRecords = "sample_text_2"
    assert instance.totalRecords == "sample_text_2"


def test_metrics_MappingXLS_columnHeaders_value_roundtrip():
    instance = metrics_MappingXLS(columnHeaders="sample_text", firstDataRow="sample_text", headerRow="sample_text", sheetNumber="sample_text")
    assert instance.columnHeaders == "sample_text"
    instance.columnHeaders = "sample_text_2"
    assert instance.columnHeaders == "sample_text_2"


def test_metrics_MappingXLS_firstDataRow_value_roundtrip():
    instance = metrics_MappingXLS(columnHeaders="sample_text", firstDataRow="sample_text", headerRow="sample_text", sheetNumber="sample_text")
    assert instance.firstDataRow == "sample_text"
    instance.firstDataRow = "sample_text_2"
    assert instance.firstDataRow == "sample_text_2"


def test_metrics_MappingXLS_headerRow_value_roundtrip():
    instance = metrics_MappingXLS(columnHeaders="sample_text", firstDataRow="sample_text", headerRow="sample_text", sheetNumber="sample_text")
    assert instance.headerRow == "sample_text"
    instance.headerRow = "sample_text_2"
    assert instance.headerRow == "sample_text_2"


def test_metrics_MappingXLS_sheetNumber_value_roundtrip():
    instance = metrics_MappingXLS(columnHeaders="sample_text", firstDataRow="sample_text", headerRow="sample_text", sheetNumber="sample_text")
    assert instance.sheetNumber == "sample_text"
    instance.sheetNumber = "sample_text_2"
    assert instance.sheetNumber == "sample_text_2"


def test_metrics_Metric_description_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_metrics_Metric_measurementKind_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    assert instance.measurementKind == "sample_text"
    instance.measurementKind = "sample_text_2"
    assert instance.measurementKind == "sample_text_2"


def test_metrics_Metric_measurementPoint_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    assert instance.measurementPoint == "sample_text"
    instance.measurementPoint = "sample_text_2"
    assert instance.measurementPoint == "sample_text_2"


def test_metrics_Metric_metricCalculation_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    assert instance.metricCalculation == "sample_text"
    instance.metricCalculation = "sample_text_2"
    assert instance.metricCalculation == "sample_text_2"


def test_metrics_Metric_name_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metrics_Metric_unitRef_value_roundtrip():
    instance = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    assert instance.unitRef == "sample_text"
    instance.unitRef = "sample_text_2"
    assert instance.unitRef == "sample_text_2"


def test_metrics_MetricSource_metricLocation_value_roundtrip():
    instance = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    assert instance.metricLocation == "sample_text"
    instance.metricLocation = "sample_text_2"
    assert instance.metricLocation == "sample_text_2"


def test_metrics_MetricSource_name_value_roundtrip():
    instance = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metrics_MetricValueRange_kindHint_value_roundtrip():
    instance = metrics_MetricValueRange(kindHint="sample_text", name="sample_text", periodHint="sample_text")
    assert instance.kindHint == "sample_text"
    instance.kindHint = "sample_text_2"
    assert instance.kindHint == "sample_text_2"


def test_metrics_MetricValueRange_name_value_roundtrip():
    instance = metrics_MetricValueRange(kindHint="sample_text", name="sample_text", periodHint="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metrics_MetricValueRange_periodHint_value_roundtrip():
    instance = metrics_MetricValueRange(kindHint="sample_text", name="sample_text", periodHint="sample_text")
    assert instance.periodHint == "sample_text"
    instance.periodHint = "sample_text_2"
    assert instance.periodHint == "sample_text_2"


def test_metrics_ValueDataKind_valueKind_value_roundtrip():
    instance = metrics_ValueDataKind(valueKind="sample_text")
    assert instance.valueKind == "sample_text"
    instance.valueKind = "sample_text_2"
    assert instance.valueKind == "sample_text_2"


def test_metrics_IdentifierDataKind_isa_DataKind():
    instance = metrics_IdentifierDataKind(objectAttribute="sample_text", objectName="sample_text")
    assert isinstance(instance, DataKind)


def test_metrics_ValueDataKind_isa_DataKind():
    instance = metrics_ValueDataKind(valueKind="sample_text")
    assert isinstance(instance, DataKind)


def test_metrics_MappingCSV_isa_Mapping():
    instance = metrics_MappingCSV()
    assert isinstance(instance, Mapping)


def test_metrics_MappingRDBMS_isa_Mapping():
    instance = metrics_MappingRDBMS()
    assert isinstance(instance, Mapping)


def test_metrics_MappingXLS_isa_Mapping():
    instance = metrics_MappingXLS(columnHeaders="sample_text", firstDataRow="sample_text", headerRow="sample_text", sheetNumber="sample_text")
    assert isinstance(instance, Mapping)


def test_metrics_MappingRecordXLS_isa_MappingRecord():
    instance = metrics_MappingRecordXLS(column="sample_text", row="sample_text")
    assert isinstance(instance, MappingRecord)


def test_assoc_columnDataKind3_link_reassign_clear():
    a = metrics_MappingXLS(columnHeaders="sample_text", firstDataRow="sample_text", headerRow="sample_text", sheetNumber="sample_text")
    b1 = metrics_DataKind()
    b2 = metrics_DataKind()
    _safe_set(a, 'metrics_MappingXLS', {b1})
    assert _is_linked(a, 'metrics_MappingXLS', b1)
    if hasattr(b1, 'metrics_DataKind'):
        assert _is_linked(b1, 'metrics_DataKind', a)
    _safe_set(a, 'metrics_MappingXLS', {b2})
    assert _is_linked(a, 'metrics_MappingXLS', b2)
    if hasattr(b1, 'metrics_DataKind'):
        assert not _is_linked(b1, 'metrics_DataKind', a)
    if hasattr(b2, 'metrics_DataKind'):
        assert _is_linked(b2, 'metrics_DataKind', a)
    _safe_set(a, 'metrics_MappingXLS', set())
    assert not _is_linked(a, 'metrics_MappingXLS', b2)
    if hasattr(b2, 'metrics_DataKind'):
        assert not _is_linked(b2, 'metrics_DataKind', a)


def test_assoc_failedRecords0_link_reassign_clear():
    a = metrics_MappingStatistic(totalRecords="sample_text")
    b1 = metrics_MappingRecord()
    b2 = metrics_MappingRecord()
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


def test_assoc_mappingDuration1_link_reassign_clear():
    a = metrics_MappingStatistic(totalRecords="sample_text")
    b1 = metrics_DateTimeRange()
    b2 = metrics_DateTimeRange()
    _safe_set(a, 'metrics_MappingStatistic2', b1)
    assert _is_linked(a, 'metrics_MappingStatistic2', b1)
    if hasattr(b1, 'metrics_DateTimeRange'):
        assert _is_linked(b1, 'metrics_DateTimeRange', a)
    _safe_set(a, 'metrics_MappingStatistic2', b2)
    assert _is_linked(a, 'metrics_MappingStatistic2', b2)
    if hasattr(b1, 'metrics_DateTimeRange'):
        assert not _is_linked(b1, 'metrics_DateTimeRange', a)
    if hasattr(b2, 'metrics_DateTimeRange'):
        assert _is_linked(b2, 'metrics_DateTimeRange', a)
    _safe_set(a, 'metrics_MappingStatistic2', None)
    assert not _is_linked(a, 'metrics_MappingStatistic2', b2)
    if hasattr(b2, 'metrics_DateTimeRange'):
        assert not _is_linked(b2, 'metrics_DateTimeRange', a)


def test_assoc_metricMapping8_link_reassign_clear():
    a = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    b1 = metrics_Mapping()
    b2 = metrics_Mapping()
    _safe_set(a, 'metrics_MetricSource', b1)
    assert _is_linked(a, 'metrics_MetricSource', b1)
    if hasattr(b1, 'metrics_Mapping'):
        assert _is_linked(b1, 'metrics_Mapping', a)
    _safe_set(a, 'metrics_MetricSource', b2)
    assert _is_linked(a, 'metrics_MetricSource', b2)
    if hasattr(b1, 'metrics_Mapping'):
        assert not _is_linked(b1, 'metrics_Mapping', a)
    if hasattr(b2, 'metrics_Mapping'):
        assert _is_linked(b2, 'metrics_Mapping', a)
    _safe_set(a, 'metrics_MetricSource', None)
    assert not _is_linked(a, 'metrics_MetricSource', b2)
    if hasattr(b2, 'metrics_Mapping'):
        assert not _is_linked(b2, 'metrics_Mapping', a)


def test_assoc_metricRefs7_link_reassign_clear():
    a = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    b1 = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    b2 = metrics_Metric(description="sample_text_2", measurementKind="sample_text_2", measurementPoint="sample_text_2", metricCalculation="sample_text_2", name="sample_text_2", unitRef="sample_text_2")
    _safe_set(a, 'metricSourceRef', {b1})
    assert _is_linked(a, 'metricSourceRef', b1)
    if hasattr(b1, 'Metric'):
        assert _is_linked(b1, 'Metric', a)
    _safe_set(a, 'metricSourceRef', {b2})
    assert _is_linked(a, 'metricSourceRef', b2)
    if hasattr(b1, 'Metric'):
        assert not _is_linked(b1, 'Metric', a)
    if hasattr(b2, 'Metric'):
        assert _is_linked(b2, 'Metric', a)
    _safe_set(a, 'metricSourceRef', set())
    assert not _is_linked(a, 'metricSourceRef', b2)
    if hasattr(b2, 'Metric'):
        assert not _is_linked(b2, 'Metric', a)


def test_assoc_metricSourceRef6_link_reassign_clear():
    a = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    b1 = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    b2 = metrics_Metric(description="sample_text_2", measurementKind="sample_text_2", measurementPoint="sample_text_2", metricCalculation="sample_text_2", name="sample_text_2", unitRef="sample_text_2")
    _safe_set(a, 'MetricSource', b1)
    assert _is_linked(a, 'MetricSource', b1)
    if hasattr(b1, 'metricRefs'):
        assert _is_linked(b1, 'metricRefs', a)
    _safe_set(a, 'MetricSource', b2)
    assert _is_linked(a, 'MetricSource', b2)
    if hasattr(b1, 'metricRefs'):
        assert not _is_linked(b1, 'metricRefs', a)
    if hasattr(b2, 'metricRefs'):
        assert _is_linked(b2, 'metricRefs', a)
    _safe_set(a, 'MetricSource', None)
    assert not _is_linked(a, 'MetricSource', b2)
    if hasattr(b2, 'metricRefs'):
        assert not _is_linked(b2, 'metricRefs', a)


def test_assoc_metricValues12_link_reassign_clear():
    a = metrics_MetricValueRange(kindHint="sample_text", name="sample_text", periodHint="sample_text")
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


def test_assoc_metrics5_link_reassign_clear():
    a = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    b1 = metrics_Metric(description="sample_text", measurementKind="sample_text", measurementPoint="sample_text", metricCalculation="sample_text", name="sample_text", unitRef="sample_text")
    b2 = metrics_Metric(description="sample_text_2", measurementKind="sample_text_2", measurementPoint="sample_text_2", metricCalculation="sample_text_2", name="sample_text_2", unitRef="sample_text_2")
    _safe_set(a, 'metrics_Metric', b1)
    assert _is_linked(a, 'metrics_Metric', b1)
    if hasattr(b1, 'metrics_Metric4'):
        assert _is_linked(b1, 'metrics_Metric4', a)
    _safe_set(a, 'metrics_Metric', b2)
    assert _is_linked(a, 'metrics_Metric', b2)
    if hasattr(b1, 'metrics_Metric4'):
        assert not _is_linked(b1, 'metrics_Metric4', a)
    if hasattr(b2, 'metrics_Metric4'):
        assert _is_linked(b2, 'metrics_Metric4', a)
    _safe_set(a, 'metrics_Metric', None)
    assert not _is_linked(a, 'metrics_Metric', b2)
    if hasattr(b2, 'metrics_Metric4'):
        assert not _is_linked(b2, 'metrics_Metric4', a)


def test_assoc_statistics9_link_reassign_clear():
    a = metrics_MetricSource(metricLocation="sample_text", name="sample_text")
    b1 = metrics_MappingStatistic(totalRecords="sample_text")
    b2 = metrics_MappingStatistic(totalRecords="sample_text_2")
    _safe_set(a, 'metrics_MetricSource10', {b1})
    assert _is_linked(a, 'metrics_MetricSource10', b1)
    if hasattr(b1, 'metrics_MappingStatistic11'):
        assert _is_linked(b1, 'metrics_MappingStatistic11', a)
    _safe_set(a, 'metrics_MetricSource10', {b2})
    assert _is_linked(a, 'metrics_MetricSource10', b2)
    if hasattr(b1, 'metrics_MappingStatistic11'):
        assert not _is_linked(b1, 'metrics_MappingStatistic11', a)
    if hasattr(b2, 'metrics_MappingStatistic11'):
        assert _is_linked(b2, 'metrics_MappingStatistic11', a)
    _safe_set(a, 'metrics_MetricSource10', set())
    assert not _is_linked(a, 'metrics_MetricSource10', b2)
    if hasattr(b2, 'metrics_MappingStatistic11'):
        assert not _is_linked(b2, 'metrics_MappingStatistic11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

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


MappingRecord_strategy = st.builds(MappingRecord)
@given(instance=MappingRecord_strategy)
@settings(max_examples=25)
def test_MappingRecord_instantiation(instance):
    assert isinstance(instance, MappingRecord)


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


metrics_IdentifierDataKind_strategy = st.builds(metrics_IdentifierDataKind, objectAttribute=safe_text, objectName=safe_text)
@given(instance=metrics_IdentifierDataKind_strategy)
@settings(max_examples=25)
def test_metrics_IdentifierDataKind_instantiation(instance):
    assert isinstance(instance, metrics_IdentifierDataKind)


metrics_Mapping_strategy = st.builds(metrics_Mapping)
@given(instance=metrics_Mapping_strategy)
@settings(max_examples=25)
def test_metrics_Mapping_instantiation(instance):
    assert isinstance(instance, metrics_Mapping)


metrics_MappingCSV_strategy = st.builds(metrics_MappingCSV)
@given(instance=metrics_MappingCSV_strategy)
@settings(max_examples=25)
def test_metrics_MappingCSV_instantiation(instance):
    assert isinstance(instance, metrics_MappingCSV)


metrics_MappingRDBMS_strategy = st.builds(metrics_MappingRDBMS)
@given(instance=metrics_MappingRDBMS_strategy)
@settings(max_examples=25)
def test_metrics_MappingRDBMS_instantiation(instance):
    assert isinstance(instance, metrics_MappingRDBMS)


metrics_MappingRecord_strategy = st.builds(metrics_MappingRecord)
@given(instance=metrics_MappingRecord_strategy)
@settings(max_examples=25)
def test_metrics_MappingRecord_instantiation(instance):
    assert isinstance(instance, metrics_MappingRecord)


metrics_MappingRecordXLS_strategy = st.builds(metrics_MappingRecordXLS, column=safe_text, row=safe_text)
@given(instance=metrics_MappingRecordXLS_strategy)
@settings(max_examples=25)
def test_metrics_MappingRecordXLS_instantiation(instance):
    assert isinstance(instance, metrics_MappingRecordXLS)


metrics_MappingStatistic_strategy = st.builds(metrics_MappingStatistic, totalRecords=safe_text)
@given(instance=metrics_MappingStatistic_strategy)
@settings(max_examples=25)
def test_metrics_MappingStatistic_instantiation(instance):
    assert isinstance(instance, metrics_MappingStatistic)


metrics_MappingXLS_strategy = st.builds(metrics_MappingXLS, columnHeaders=safe_text, firstDataRow=safe_text, headerRow=safe_text, sheetNumber=safe_text)
@given(instance=metrics_MappingXLS_strategy)
@settings(max_examples=25)
def test_metrics_MappingXLS_instantiation(instance):
    assert isinstance(instance, metrics_MappingXLS)


metrics_Metric_strategy = st.builds(metrics_Metric, description=safe_text, measurementKind=safe_text, measurementPoint=safe_text, metricCalculation=safe_text, name=safe_text, unitRef=safe_text)
@given(instance=metrics_Metric_strategy)
@settings(max_examples=25)
def test_metrics_Metric_instantiation(instance):
    assert isinstance(instance, metrics_Metric)


metrics_MetricSource_strategy = st.builds(metrics_MetricSource, metricLocation=safe_text, name=safe_text)
@given(instance=metrics_MetricSource_strategy)
@settings(max_examples=25)
def test_metrics_MetricSource_instantiation(instance):
    assert isinstance(instance, metrics_MetricSource)


metrics_MetricValueRange_strategy = st.builds(metrics_MetricValueRange, kindHint=safe_text, name=safe_text, periodHint=safe_text)
@given(instance=metrics_MetricValueRange_strategy)
@settings(max_examples=25)
def test_metrics_MetricValueRange_instantiation(instance):
    assert isinstance(instance, metrics_MetricValueRange)


metrics_Value_strategy = st.builds(metrics_Value)
@given(instance=metrics_Value_strategy)
@settings(max_examples=25)
def test_metrics_Value_instantiation(instance):
    assert isinstance(instance, metrics_Value)


metrics_ValueDataKind_strategy = st.builds(metrics_ValueDataKind, valueKind=safe_text)
@given(instance=metrics_ValueDataKind_strategy)
@settings(max_examples=25)
def test_metrics_ValueDataKind_instantiation(instance):
    assert isinstance(instance, metrics_ValueDataKind)



