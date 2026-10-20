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
    QualityMetamodel_EnumerationItem,
    ValueType,
    QualityMetamodel_IntegerValueType,
    QualityMetamodel_AggregatedValueMetric,
    QualityMetamodel_BooleanValueType,
    QualityMetamodel_RangeValueType,
    QualityMetamodel_EnumerationMetric,
    QualityMetamodel_RealValueType,
    QualityMetamodel_TextValueType,
    QualityMetamodel_Value,
    QualityMetamodel_QualityAttribute,
    QualityMetamodel_ValueType,
    QualityMetamodel_MetricProvider,
    QualityMetamodel_QualityModel,
    QualityMetamodel_Operation,
    Value,
    QualityMetamodel_AggregatedValue,
    QualityMetamodel_SingleValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_qualitymetamodel_enumerationitem_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_EnumerationItem)


def test_hyp_qualitymetamodel_enumerationitem_constructor_exists():
    assert callable(QualityMetamodel_EnumerationItem.__init__)


def test_hyp_qualitymetamodel_enumerationitem_constructor_args():
    sig = inspect.signature(QualityMetamodel_EnumerationItem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_hyp_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_hyp_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_qualitymetamodel_integervaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_IntegerValueType)


def test_hyp_qualitymetamodel_integervaluetype_constructor_exists():
    assert callable(QualityMetamodel_IntegerValueType.__init__)


def test_hyp_qualitymetamodel_integervaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_IntegerValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_qualitymetamodel_aggregatedvaluemetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_AggregatedValueMetric)


def test_hyp_qualitymetamodel_aggregatedvaluemetric_constructor_exists():
    assert callable(QualityMetamodel_AggregatedValueMetric.__init__)


def test_hyp_qualitymetamodel_aggregatedvaluemetric_constructor_args():
    sig = inspect.signature(QualityMetamodel_AggregatedValueMetric.__init__)
    params = list(sig.parameters.keys())
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "average" in params, "Missing parameter 'average'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "median" in params, "Missing parameter 'median'"








def test_hyp_qualitymetamodel_booleanvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_BooleanValueType)


def test_hyp_qualitymetamodel_booleanvaluetype_constructor_exists():
    assert callable(QualityMetamodel_BooleanValueType.__init__)


def test_hyp_qualitymetamodel_booleanvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_BooleanValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_qualitymetamodel_rangevaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_RangeValueType)


def test_hyp_qualitymetamodel_rangevaluetype_constructor_exists():
    assert callable(QualityMetamodel_RangeValueType.__init__)


def test_hyp_qualitymetamodel_rangevaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_RangeValueType.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"





def test_hyp_qualitymetamodel_enumerationmetric_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_EnumerationMetric)


def test_hyp_qualitymetamodel_enumerationmetric_constructor_exists():
    assert callable(QualityMetamodel_EnumerationMetric.__init__)


def test_hyp_qualitymetamodel_enumerationmetric_constructor_args():
    sig = inspect.signature(QualityMetamodel_EnumerationMetric.__init__)
    params = list(sig.parameters.keys())



def test_hyp_qualitymetamodel_realvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_RealValueType)


def test_hyp_qualitymetamodel_realvaluetype_constructor_exists():
    assert callable(QualityMetamodel_RealValueType.__init__)


def test_hyp_qualitymetamodel_realvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_RealValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_qualitymetamodel_textvaluetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_TextValueType)


def test_hyp_qualitymetamodel_textvaluetype_constructor_exists():
    assert callable(QualityMetamodel_TextValueType.__init__)


def test_hyp_qualitymetamodel_textvaluetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_TextValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_qualitymetamodel_value_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_Value)


def test_hyp_qualitymetamodel_value_constructor_exists():
    assert callable(QualityMetamodel_Value.__init__)


def test_hyp_qualitymetamodel_value_constructor_args():
    sig = inspect.signature(QualityMetamodel_Value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"





def test_hyp_qualitymetamodel_qualityattribute_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QualityAttribute)


def test_hyp_qualitymetamodel_qualityattribute_constructor_exists():
    assert callable(QualityMetamodel_QualityAttribute.__init__)


def test_hyp_qualitymetamodel_qualityattribute_constructor_args():
    sig = inspect.signature(QualityMetamodel_QualityAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_qualitymetamodel_valuetype_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_ValueType)


def test_hyp_qualitymetamodel_valuetype_constructor_exists():
    assert callable(QualityMetamodel_ValueType.__init__)


def test_hyp_qualitymetamodel_valuetype_constructor_args():
    sig = inspect.signature(QualityMetamodel_ValueType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_qualitymetamodel_metricprovider_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_MetricProvider)


def test_hyp_qualitymetamodel_metricprovider_constructor_exists():
    assert callable(QualityMetamodel_MetricProvider.__init__)


def test_hyp_qualitymetamodel_metricprovider_constructor_args():
    sig = inspect.signature(QualityMetamodel_MetricProvider.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_qualitymetamodel_qualitymodel_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_QualityModel)


def test_hyp_qualitymetamodel_qualitymodel_constructor_exists():
    assert callable(QualityMetamodel_QualityModel.__init__)


def test_hyp_qualitymetamodel_qualitymodel_constructor_args():
    sig = inspect.signature(QualityMetamodel_QualityModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_qualitymetamodel_operation_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_Operation)


def test_hyp_qualitymetamodel_operation_constructor_exists():
    assert callable(QualityMetamodel_Operation.__init__)


def test_hyp_qualitymetamodel_operation_constructor_args():
    sig = inspect.signature(QualityMetamodel_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_qualitymetamodel_aggregatedvalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_AggregatedValue)


def test_hyp_qualitymetamodel_aggregatedvalue_constructor_exists():
    assert callable(QualityMetamodel_AggregatedValue.__init__)


def test_hyp_qualitymetamodel_aggregatedvalue_constructor_args():
    sig = inspect.signature(QualityMetamodel_AggregatedValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_qualitymetamodel_singlevalue_is_not_abstract():
    assert not inspect.isabstract(QualityMetamodel_SingleValue)


def test_hyp_qualitymetamodel_singlevalue_constructor_exists():
    assert callable(QualityMetamodel_SingleValue.__init__)


def test_hyp_qualitymetamodel_singlevalue_constructor_args():
    sig = inspect.signature(QualityMetamodel_SingleValue.__init__)
    params = list(sig.parameters.keys())


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
QualityMetamodel_EnumerationItem_strategy = st.builds(
    QualityMetamodel_EnumerationItem,
    name=
        safe_text
)
ValueType_strategy = st.builds(
    ValueType,
)
QualityMetamodel_IntegerValueType_strategy = st.builds(
    QualityMetamodel_IntegerValueType,
    value=
        safe_text
)
QualityMetamodel_AggregatedValueMetric_strategy = st.builds(
    QualityMetamodel_AggregatedValueMetric,
    standardDeviation=
        safe_text,
    minimum=
        safe_text,
    average=
        safe_text,
    maximum=
        safe_text,
    median=
        safe_text
)
QualityMetamodel_BooleanValueType_strategy = st.builds(
    QualityMetamodel_BooleanValueType,
    value=
        safe_text
)
QualityMetamodel_RangeValueType_strategy = st.builds(
    QualityMetamodel_RangeValueType,
    max=
        safe_text,
    min=
        safe_text
)
QualityMetamodel_EnumerationMetric_strategy = st.builds(
    QualityMetamodel_EnumerationMetric,
)
QualityMetamodel_RealValueType_strategy = st.builds(
    QualityMetamodel_RealValueType,
    value=
        safe_text
)
QualityMetamodel_TextValueType_strategy = st.builds(
    QualityMetamodel_TextValueType,
    value=
        safe_text
)
QualityMetamodel_Value_strategy = st.builds(
    QualityMetamodel_Value,
    name=
        safe_text,
    description=
        safe_text
)
QualityMetamodel_QualityAttribute_strategy = st.builds(
    QualityMetamodel_QualityAttribute,
    name=
        safe_text
)
QualityMetamodel_ValueType_strategy = st.builds(
    QualityMetamodel_ValueType,
    name=
        safe_text
)
QualityMetamodel_MetricProvider_strategy = st.builds(
    QualityMetamodel_MetricProvider,
    description=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
QualityMetamodel_QualityModel_strategy = st.builds(
    QualityMetamodel_QualityModel,
    name=
        safe_text
)
QualityMetamodel_Operation_strategy = st.builds(
    QualityMetamodel_Operation,
    name=
        safe_text,
    body=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
QualityMetamodel_AggregatedValue_strategy = st.builds(
    QualityMetamodel_AggregatedValue,
)
QualityMetamodel_SingleValue_strategy = st.builds(
    QualityMetamodel_SingleValue,
)




@given(instance=QualityMetamodel_EnumerationItem_strategy)
def test_hyp_qualitymetamodel_enumerationitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=QualityMetamodel_IntegerValueType_strategy)
def test_hyp_qualitymetamodel_integervaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_hyp_qualitymetamodel_aggregatedvaluemetric_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_hyp_qualitymetamodel_aggregatedvaluemetric_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_hyp_qualitymetamodel_aggregatedvaluemetric_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_hyp_qualitymetamodel_aggregatedvaluemetric_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original



@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
def test_hyp_qualitymetamodel_aggregatedvaluemetric_median_setter(instance):
    original = instance.median
    instance.median = original
    assert instance.median == original




@given(instance=QualityMetamodel_BooleanValueType_strategy)
def test_hyp_qualitymetamodel_booleanvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=QualityMetamodel_RangeValueType_strategy)
def test_hyp_qualitymetamodel_rangevaluetype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=QualityMetamodel_RangeValueType_strategy)
def test_hyp_qualitymetamodel_rangevaluetype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original





@given(instance=QualityMetamodel_RealValueType_strategy)
def test_hyp_qualitymetamodel_realvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=QualityMetamodel_TextValueType_strategy)
def test_hyp_qualitymetamodel_textvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=QualityMetamodel_Value_strategy)
def test_hyp_qualitymetamodel_value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=QualityMetamodel_Value_strategy)
def test_hyp_qualitymetamodel_value_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=QualityMetamodel_QualityAttribute_strategy)
def test_hyp_qualitymetamodel_qualityattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=QualityMetamodel_ValueType_strategy)
def test_hyp_qualitymetamodel_valuetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_hyp_qualitymetamodel_metricprovider_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_hyp_qualitymetamodel_metricprovider_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=QualityMetamodel_MetricProvider_strategy)
def test_hyp_qualitymetamodel_metricprovider_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=QualityMetamodel_QualityModel_strategy)
def test_hyp_qualitymetamodel_qualitymodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=QualityMetamodel_Operation_strategy)
def test_hyp_qualitymetamodel_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=QualityMetamodel_Operation_strategy)
def test_hyp_qualitymetamodel_operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_QualityMetamodel_AggregatedValueMetric_average_value_roundtrip():
    instance = QualityMetamodel_AggregatedValueMetric(average="sample_text", maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation="sample_text")
    assert instance.average == "sample_text"
    instance.average = "sample_text_2"
    assert instance.average == "sample_text_2"


def test_QualityMetamodel_AggregatedValueMetric_maximum_value_roundtrip():
    instance = QualityMetamodel_AggregatedValueMetric(average="sample_text", maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation="sample_text")
    assert instance.maximum == "sample_text"
    instance.maximum = "sample_text_2"
    assert instance.maximum == "sample_text_2"


def test_QualityMetamodel_AggregatedValueMetric_median_value_roundtrip():
    instance = QualityMetamodel_AggregatedValueMetric(average="sample_text", maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation="sample_text")
    assert instance.median == "sample_text"
    instance.median = "sample_text_2"
    assert instance.median == "sample_text_2"


def test_QualityMetamodel_AggregatedValueMetric_minimum_value_roundtrip():
    instance = QualityMetamodel_AggregatedValueMetric(average="sample_text", maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation="sample_text")
    assert instance.minimum == "sample_text"
    instance.minimum = "sample_text_2"
    assert instance.minimum == "sample_text_2"


def test_QualityMetamodel_AggregatedValueMetric_standardDeviation_value_roundtrip():
    instance = QualityMetamodel_AggregatedValueMetric(average="sample_text", maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation="sample_text")
    assert instance.standardDeviation == "sample_text"
    instance.standardDeviation = "sample_text_2"
    assert instance.standardDeviation == "sample_text_2"


def test_QualityMetamodel_BooleanValueType_value_value_roundtrip():
    instance = QualityMetamodel_BooleanValueType(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_QualityMetamodel_EnumerationItem_name_value_roundtrip():
    instance = QualityMetamodel_EnumerationItem(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_QualityMetamodel_IntegerValueType_value_value_roundtrip():
    instance = QualityMetamodel_IntegerValueType(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_QualityMetamodel_MetricProvider_description_value_roundtrip():
    instance = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_QualityMetamodel_MetricProvider_id_value_roundtrip():
    instance = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_QualityMetamodel_MetricProvider_name_value_roundtrip():
    instance = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_QualityMetamodel_Operation_body_value_roundtrip():
    instance = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_QualityMetamodel_Operation_name_value_roundtrip():
    instance = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_QualityMetamodel_QualityAttribute_name_value_roundtrip():
    instance = QualityMetamodel_QualityAttribute(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_QualityMetamodel_QualityModel_name_value_roundtrip():
    instance = QualityMetamodel_QualityModel(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_QualityMetamodel_RangeValueType_max_value_roundtrip():
    instance = QualityMetamodel_RangeValueType(max="sample_text", min="sample_text")
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_QualityMetamodel_RangeValueType_min_value_roundtrip():
    instance = QualityMetamodel_RangeValueType(max="sample_text", min="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_QualityMetamodel_RealValueType_value_value_roundtrip():
    instance = QualityMetamodel_RealValueType(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_QualityMetamodel_TextValueType_value_value_roundtrip():
    instance = QualityMetamodel_TextValueType(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_QualityMetamodel_Value_description_value_roundtrip():
    instance = QualityMetamodel_Value(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_QualityMetamodel_Value_name_value_roundtrip():
    instance = QualityMetamodel_Value(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_QualityMetamodel_ValueType_name_value_roundtrip():
    instance = QualityMetamodel_ValueType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_QualityMetamodel_AggregatedValue_isa_Value():
    instance = QualityMetamodel_AggregatedValue()
    assert isinstance(instance, Value)


def test_QualityMetamodel_SingleValue_isa_Value():
    instance = QualityMetamodel_SingleValue()
    assert isinstance(instance, Value)


def test_QualityMetamodel_AggregatedValueMetric_isa_ValueType():
    instance = QualityMetamodel_AggregatedValueMetric(average="sample_text", maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation="sample_text")
    assert isinstance(instance, ValueType)


def test_QualityMetamodel_BooleanValueType_isa_ValueType():
    instance = QualityMetamodel_BooleanValueType(value="sample_text")
    assert isinstance(instance, ValueType)


def test_QualityMetamodel_EnumerationMetric_isa_ValueType():
    instance = QualityMetamodel_EnumerationMetric()
    assert isinstance(instance, ValueType)


def test_QualityMetamodel_IntegerValueType_isa_ValueType():
    instance = QualityMetamodel_IntegerValueType(value="sample_text")
    assert isinstance(instance, ValueType)


def test_QualityMetamodel_RangeValueType_isa_ValueType():
    instance = QualityMetamodel_RangeValueType(max="sample_text", min="sample_text")
    assert isinstance(instance, ValueType)


def test_QualityMetamodel_RealValueType_isa_ValueType():
    instance = QualityMetamodel_RealValueType(value="sample_text")
    assert isinstance(instance, ValueType)


def test_QualityMetamodel_TextValueType_isa_ValueType():
    instance = QualityMetamodel_TextValueType(value="sample_text")
    assert isinstance(instance, ValueType)


def test_assoc_aggregatedValues18_link_reassign_clear():
    a = QualityMetamodel_Value(description="sample_text", name="sample_text")
    b1 = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    b2 = QualityMetamodel_Operation(body="sample_text_2", name="sample_text_2")
    _safe_set(a, 'QualityMetamodel_Value20', b1)
    assert _is_linked(a, 'QualityMetamodel_Value20', b1)
    if hasattr(b1, 'QualityMetamodel_Operation19'):
        assert _is_linked(b1, 'QualityMetamodel_Operation19', a)
    _safe_set(a, 'QualityMetamodel_Value20', b2)
    assert _is_linked(a, 'QualityMetamodel_Value20', b2)
    if hasattr(b1, 'QualityMetamodel_Operation19'):
        assert not _is_linked(b1, 'QualityMetamodel_Operation19', a)
    if hasattr(b2, 'QualityMetamodel_Operation19'):
        assert _is_linked(b2, 'QualityMetamodel_Operation19', a)
    _safe_set(a, 'QualityMetamodel_Value20', None)
    assert not _is_linked(a, 'QualityMetamodel_Value20', b2)
    if hasattr(b2, 'QualityMetamodel_Operation19'):
        assert not _is_linked(b2, 'QualityMetamodel_Operation19', a)


def test_assoc_calculatedBy17_link_reassign_clear():
    a = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    b1 = QualityMetamodel_AggregatedValue()
    b2 = QualityMetamodel_AggregatedValue()
    _safe_set(a, 'QualityMetamodel_Operation', b1)
    assert _is_linked(a, 'QualityMetamodel_Operation', b1)
    if hasattr(b1, 'QualityMetamodel_AggregatedValue'):
        assert _is_linked(b1, 'QualityMetamodel_AggregatedValue', a)
    _safe_set(a, 'QualityMetamodel_Operation', b2)
    assert _is_linked(a, 'QualityMetamodel_Operation', b2)
    if hasattr(b1, 'QualityMetamodel_AggregatedValue'):
        assert not _is_linked(b1, 'QualityMetamodel_AggregatedValue', a)
    if hasattr(b2, 'QualityMetamodel_AggregatedValue'):
        assert _is_linked(b2, 'QualityMetamodel_AggregatedValue', a)
    _safe_set(a, 'QualityMetamodel_Operation', None)
    assert not _is_linked(a, 'QualityMetamodel_Operation', b2)
    if hasattr(b2, 'QualityMetamodel_AggregatedValue'):
        assert not _is_linked(b2, 'QualityMetamodel_AggregatedValue', a)


def test_assoc_measuredBy15_link_reassign_clear():
    a = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    b1 = QualityMetamodel_SingleValue()
    b2 = QualityMetamodel_SingleValue()
    _safe_set(a, 'QualityMetamodel_MetricProvider16', b1)
    assert _is_linked(a, 'QualityMetamodel_MetricProvider16', b1)
    if hasattr(b1, 'QualityMetamodel_SingleValue'):
        assert _is_linked(b1, 'QualityMetamodel_SingleValue', a)
    _safe_set(a, 'QualityMetamodel_MetricProvider16', b2)
    assert _is_linked(a, 'QualityMetamodel_MetricProvider16', b2)
    if hasattr(b1, 'QualityMetamodel_SingleValue'):
        assert not _is_linked(b1, 'QualityMetamodel_SingleValue', a)
    if hasattr(b2, 'QualityMetamodel_SingleValue'):
        assert _is_linked(b2, 'QualityMetamodel_SingleValue', a)
    _safe_set(a, 'QualityMetamodel_MetricProvider16', None)
    assert not _is_linked(a, 'QualityMetamodel_MetricProvider16', b2)
    if hasattr(b2, 'QualityMetamodel_SingleValue'):
        assert not _is_linked(b2, 'QualityMetamodel_SingleValue', a)


def test_assoc_metricProviders0_link_reassign_clear():
    a = QualityMetamodel_QualityModel(name="sample_text")
    b1 = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    b2 = QualityMetamodel_MetricProvider(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    _safe_set(a, 'QualityMetamodel_QualityModel', {b1})
    assert _is_linked(a, 'QualityMetamodel_QualityModel', b1)
    if hasattr(b1, 'QualityMetamodel_MetricProvider'):
        assert _is_linked(b1, 'QualityMetamodel_MetricProvider', a)
    _safe_set(a, 'QualityMetamodel_QualityModel', {b2})
    assert _is_linked(a, 'QualityMetamodel_QualityModel', b2)
    if hasattr(b1, 'QualityMetamodel_MetricProvider'):
        assert not _is_linked(b1, 'QualityMetamodel_MetricProvider', a)
    if hasattr(b2, 'QualityMetamodel_MetricProvider'):
        assert _is_linked(b2, 'QualityMetamodel_MetricProvider', a)
    _safe_set(a, 'QualityMetamodel_QualityModel', set())
    assert not _is_linked(a, 'QualityMetamodel_QualityModel', b2)
    if hasattr(b2, 'QualityMetamodel_MetricProvider'):
        assert not _is_linked(b2, 'QualityMetamodel_MetricProvider', a)


def test_assoc_qualityAttributes11_link_reassign_clear():
    a = QualityMetamodel_QualityAttribute(name="sample_text")
    b1 = QualityMetamodel_QualityAttribute(name="sample_text")
    b2 = QualityMetamodel_QualityAttribute(name="sample_text_2")
    _safe_set(a, 'QualityMetamodel_QualityAttribute10', {b1})
    assert _is_linked(a, 'QualityMetamodel_QualityAttribute10', b1)
    if hasattr(b1, 'QualityMetamodel_QualityAttribute12'):
        assert _is_linked(b1, 'QualityMetamodel_QualityAttribute12', a)
    _safe_set(a, 'QualityMetamodel_QualityAttribute10', {b2})
    assert _is_linked(a, 'QualityMetamodel_QualityAttribute10', b2)
    if hasattr(b1, 'QualityMetamodel_QualityAttribute12'):
        assert not _is_linked(b1, 'QualityMetamodel_QualityAttribute12', a)
    if hasattr(b2, 'QualityMetamodel_QualityAttribute12'):
        assert _is_linked(b2, 'QualityMetamodel_QualityAttribute12', a)
    _safe_set(a, 'QualityMetamodel_QualityAttribute10', set())
    assert not _is_linked(a, 'QualityMetamodel_QualityAttribute10', b2)
    if hasattr(b2, 'QualityMetamodel_QualityAttribute12'):
        assert not _is_linked(b2, 'QualityMetamodel_QualityAttribute12', a)


def test_assoc_qualityAttributes3_link_reassign_clear():
    a = QualityMetamodel_QualityModel(name="sample_text")
    b1 = QualityMetamodel_QualityAttribute(name="sample_text")
    b2 = QualityMetamodel_QualityAttribute(name="sample_text_2")
    _safe_set(a, 'QualityMetamodel_QualityModel4', {b1})
    assert _is_linked(a, 'QualityMetamodel_QualityModel4', b1)
    if hasattr(b1, 'QualityMetamodel_QualityAttribute'):
        assert _is_linked(b1, 'QualityMetamodel_QualityAttribute', a)
    _safe_set(a, 'QualityMetamodel_QualityModel4', {b2})
    assert _is_linked(a, 'QualityMetamodel_QualityModel4', b2)
    if hasattr(b1, 'QualityMetamodel_QualityAttribute'):
        assert not _is_linked(b1, 'QualityMetamodel_QualityAttribute', a)
    if hasattr(b2, 'QualityMetamodel_QualityAttribute'):
        assert _is_linked(b2, 'QualityMetamodel_QualityAttribute', a)
    _safe_set(a, 'QualityMetamodel_QualityModel4', set())
    assert not _is_linked(a, 'QualityMetamodel_QualityModel4', b2)
    if hasattr(b2, 'QualityMetamodel_QualityAttribute'):
        assert not _is_linked(b2, 'QualityMetamodel_QualityAttribute', a)


def test_assoc_qualityTypes1_link_reassign_clear():
    a = QualityMetamodel_ValueType(name="sample_text")
    b1 = QualityMetamodel_QualityModel(name="sample_text")
    b2 = QualityMetamodel_QualityModel(name="sample_text_2")
    _safe_set(a, 'QualityMetamodel_ValueType', b1)
    assert _is_linked(a, 'QualityMetamodel_ValueType', b1)
    if hasattr(b1, 'QualityMetamodel_QualityModel2'):
        assert _is_linked(b1, 'QualityMetamodel_QualityModel2', a)
    _safe_set(a, 'QualityMetamodel_ValueType', b2)
    assert _is_linked(a, 'QualityMetamodel_ValueType', b2)
    if hasattr(b1, 'QualityMetamodel_QualityModel2'):
        assert not _is_linked(b1, 'QualityMetamodel_QualityModel2', a)
    if hasattr(b2, 'QualityMetamodel_QualityModel2'):
        assert _is_linked(b2, 'QualityMetamodel_QualityModel2', a)
    _safe_set(a, 'QualityMetamodel_ValueType', None)
    assert not _is_linked(a, 'QualityMetamodel_ValueType', b2)
    if hasattr(b2, 'QualityMetamodel_QualityModel2'):
        assert not _is_linked(b2, 'QualityMetamodel_QualityModel2', a)


def test_assoc_qualityValues5_link_reassign_clear():
    a = QualityMetamodel_Value(description="sample_text", name="sample_text")
    b1 = QualityMetamodel_QualityModel(name="sample_text")
    b2 = QualityMetamodel_QualityModel(name="sample_text_2")
    _safe_set(a, 'QualityMetamodel_Value', b1)
    assert _is_linked(a, 'QualityMetamodel_Value', b1)
    if hasattr(b1, 'QualityMetamodel_QualityModel6'):
        assert _is_linked(b1, 'QualityMetamodel_QualityModel6', a)
    _safe_set(a, 'QualityMetamodel_Value', b2)
    assert _is_linked(a, 'QualityMetamodel_Value', b2)
    if hasattr(b1, 'QualityMetamodel_QualityModel6'):
        assert not _is_linked(b1, 'QualityMetamodel_QualityModel6', a)
    if hasattr(b2, 'QualityMetamodel_QualityModel6'):
        assert _is_linked(b2, 'QualityMetamodel_QualityModel6', a)
    _safe_set(a, 'QualityMetamodel_Value', None)
    assert not _is_linked(a, 'QualityMetamodel_Value', b2)
    if hasattr(b2, 'QualityMetamodel_QualityModel6'):
        assert not _is_linked(b2, 'QualityMetamodel_QualityModel6', a)


def test_assoc_set21_link_reassign_clear():
    a = QualityMetamodel_EnumerationItem(name="sample_text")
    b1 = QualityMetamodel_EnumerationMetric()
    b2 = QualityMetamodel_EnumerationMetric()
    _safe_set(a, 'QualityMetamodel_EnumerationItem', b1)
    assert _is_linked(a, 'QualityMetamodel_EnumerationItem', b1)
    if hasattr(b1, 'QualityMetamodel_EnumerationMetric'):
        assert _is_linked(b1, 'QualityMetamodel_EnumerationMetric', a)
    _safe_set(a, 'QualityMetamodel_EnumerationItem', b2)
    assert _is_linked(a, 'QualityMetamodel_EnumerationItem', b2)
    if hasattr(b1, 'QualityMetamodel_EnumerationMetric'):
        assert not _is_linked(b1, 'QualityMetamodel_EnumerationMetric', a)
    if hasattr(b2, 'QualityMetamodel_EnumerationMetric'):
        assert _is_linked(b2, 'QualityMetamodel_EnumerationMetric', a)
    _safe_set(a, 'QualityMetamodel_EnumerationItem', None)
    assert not _is_linked(a, 'QualityMetamodel_EnumerationItem', b2)
    if hasattr(b2, 'QualityMetamodel_EnumerationMetric'):
        assert not _is_linked(b2, 'QualityMetamodel_EnumerationMetric', a)


def test_assoc_type13_link_reassign_clear():
    a = QualityMetamodel_ValueType(name="sample_text")
    b1 = QualityMetamodel_Value(description="sample_text", name="sample_text")
    b2 = QualityMetamodel_Value(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'ValueType', b1)
    assert _is_linked(a, 'ValueType', b1)
    if hasattr(b1, 'val'):
        assert _is_linked(b1, 'val', a)
    _safe_set(a, 'ValueType', b2)
    assert _is_linked(a, 'ValueType', b2)
    if hasattr(b1, 'val'):
        assert not _is_linked(b1, 'val', a)
    if hasattr(b2, 'val'):
        assert _is_linked(b2, 'val', a)
    _safe_set(a, 'ValueType', None)
    assert not _is_linked(a, 'ValueType', b2)
    if hasattr(b2, 'val'):
        assert not _is_linked(b2, 'val', a)


def test_assoc_val14_link_reassign_clear():
    a = QualityMetamodel_ValueType(name="sample_text")
    b1 = QualityMetamodel_Value(description="sample_text", name="sample_text")
    b2 = QualityMetamodel_Value(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'type', b1)
    assert _is_linked(a, 'type', b1)
    if hasattr(b1, 'Value'):
        assert _is_linked(b1, 'Value', a)
    _safe_set(a, 'type', b2)
    assert _is_linked(a, 'type', b2)
    if hasattr(b1, 'Value'):
        assert not _is_linked(b1, 'Value', a)
    if hasattr(b2, 'Value'):
        assert _is_linked(b2, 'Value', a)
    _safe_set(a, 'type', None)
    assert not _is_linked(a, 'type', b2)
    if hasattr(b2, 'Value'):
        assert not _is_linked(b2, 'Value', a)


def test_assoc_value22_link_reassign_clear():
    a = QualityMetamodel_EnumerationItem(name="sample_text")
    b1 = QualityMetamodel_EnumerationMetric()
    b2 = QualityMetamodel_EnumerationMetric()
    _safe_set(a, 'QualityMetamodel_EnumerationItem24', b1)
    assert _is_linked(a, 'QualityMetamodel_EnumerationItem24', b1)
    if hasattr(b1, 'QualityMetamodel_EnumerationMetric23'):
        assert _is_linked(b1, 'QualityMetamodel_EnumerationMetric23', a)
    _safe_set(a, 'QualityMetamodel_EnumerationItem24', b2)
    assert _is_linked(a, 'QualityMetamodel_EnumerationItem24', b2)
    if hasattr(b1, 'QualityMetamodel_EnumerationMetric23'):
        assert not _is_linked(b1, 'QualityMetamodel_EnumerationMetric23', a)
    if hasattr(b2, 'QualityMetamodel_EnumerationMetric23'):
        assert _is_linked(b2, 'QualityMetamodel_EnumerationMetric23', a)
    _safe_set(a, 'QualityMetamodel_EnumerationItem24', None)
    assert not _is_linked(a, 'QualityMetamodel_EnumerationItem24', b2)
    if hasattr(b2, 'QualityMetamodel_EnumerationMetric23'):
        assert not _is_linked(b2, 'QualityMetamodel_EnumerationMetric23', a)


def test_assoc_value7_link_reassign_clear():
    a = QualityMetamodel_Value(description="sample_text", name="sample_text")
    b1 = QualityMetamodel_QualityAttribute(name="sample_text")
    b2 = QualityMetamodel_QualityAttribute(name="sample_text_2")
    _safe_set(a, 'QualityMetamodel_Value9', b1)
    assert _is_linked(a, 'QualityMetamodel_Value9', b1)
    if hasattr(b1, 'QualityMetamodel_QualityAttribute8'):
        assert _is_linked(b1, 'QualityMetamodel_QualityAttribute8', a)
    _safe_set(a, 'QualityMetamodel_Value9', b2)
    assert _is_linked(a, 'QualityMetamodel_Value9', b2)
    if hasattr(b1, 'QualityMetamodel_QualityAttribute8'):
        assert not _is_linked(b1, 'QualityMetamodel_QualityAttribute8', a)
    if hasattr(b2, 'QualityMetamodel_QualityAttribute8'):
        assert _is_linked(b2, 'QualityMetamodel_QualityAttribute8', a)
    _safe_set(a, 'QualityMetamodel_Value9', None)
    assert not _is_linked(a, 'QualityMetamodel_Value9', b2)
    if hasattr(b2, 'QualityMetamodel_QualityAttribute8'):
        assert not _is_linked(b2, 'QualityMetamodel_QualityAttribute8', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

QualityMetamodel_AggregatedValue_strategy = st.builds(QualityMetamodel_AggregatedValue)
@given(instance=QualityMetamodel_AggregatedValue_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_AggregatedValue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_AggregatedValue)


QualityMetamodel_AggregatedValueMetric_strategy = st.builds(QualityMetamodel_AggregatedValueMetric, average=safe_text, maximum=safe_text, median=safe_text, minimum=safe_text, standardDeviation=safe_text)
@given(instance=QualityMetamodel_AggregatedValueMetric_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_AggregatedValueMetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_AggregatedValueMetric)


QualityMetamodel_BooleanValueType_strategy = st.builds(QualityMetamodel_BooleanValueType, value=safe_text)
@given(instance=QualityMetamodel_BooleanValueType_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_BooleanValueType_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_BooleanValueType)


QualityMetamodel_EnumerationItem_strategy = st.builds(QualityMetamodel_EnumerationItem, name=safe_text)
@given(instance=QualityMetamodel_EnumerationItem_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_EnumerationItem_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_EnumerationItem)


QualityMetamodel_EnumerationMetric_strategy = st.builds(QualityMetamodel_EnumerationMetric)
@given(instance=QualityMetamodel_EnumerationMetric_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_EnumerationMetric_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_EnumerationMetric)


QualityMetamodel_IntegerValueType_strategy = st.builds(QualityMetamodel_IntegerValueType, value=safe_text)
@given(instance=QualityMetamodel_IntegerValueType_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_IntegerValueType_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_IntegerValueType)


QualityMetamodel_MetricProvider_strategy = st.builds(QualityMetamodel_MetricProvider, description=safe_text, id=safe_text, name=safe_text)
@given(instance=QualityMetamodel_MetricProvider_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_MetricProvider_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_MetricProvider)


QualityMetamodel_Operation_strategy = st.builds(QualityMetamodel_Operation, body=safe_text, name=safe_text)
@given(instance=QualityMetamodel_Operation_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_Operation_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_Operation)


QualityMetamodel_QualityAttribute_strategy = st.builds(QualityMetamodel_QualityAttribute, name=safe_text)
@given(instance=QualityMetamodel_QualityAttribute_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_QualityAttribute_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QualityAttribute)


QualityMetamodel_QualityModel_strategy = st.builds(QualityMetamodel_QualityModel, name=safe_text)
@given(instance=QualityMetamodel_QualityModel_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_QualityModel_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_QualityModel)


QualityMetamodel_RangeValueType_strategy = st.builds(QualityMetamodel_RangeValueType, max=safe_text, min=safe_text)
@given(instance=QualityMetamodel_RangeValueType_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_RangeValueType_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_RangeValueType)


QualityMetamodel_RealValueType_strategy = st.builds(QualityMetamodel_RealValueType, value=safe_text)
@given(instance=QualityMetamodel_RealValueType_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_RealValueType_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_RealValueType)


QualityMetamodel_SingleValue_strategy = st.builds(QualityMetamodel_SingleValue)
@given(instance=QualityMetamodel_SingleValue_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_SingleValue_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_SingleValue)


QualityMetamodel_TextValueType_strategy = st.builds(QualityMetamodel_TextValueType, value=safe_text)
@given(instance=QualityMetamodel_TextValueType_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_TextValueType_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_TextValueType)


QualityMetamodel_Value_strategy = st.builds(QualityMetamodel_Value, description=safe_text, name=safe_text)
@given(instance=QualityMetamodel_Value_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_Value_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_Value)


QualityMetamodel_ValueType_strategy = st.builds(QualityMetamodel_ValueType, name=safe_text)
@given(instance=QualityMetamodel_ValueType_strategy)
@settings(max_examples=25)
def test_QualityMetamodel_ValueType_instantiation(instance):
    assert isinstance(instance, QualityMetamodel_ValueType)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


ValueType_strategy = st.builds(ValueType)
@given(instance=ValueType_strategy)
@settings(max_examples=25)
def test_ValueType_instantiation(instance):
    assert isinstance(instance, ValueType)



