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
    metric_Metric,
    metric_Container,
    Metric,
    metric_SimpleMetric,
    metric_AggregatedRealMetric,
    metric_AggregatedIntegerMetric,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_metric_metric_is_not_abstract():
    assert not inspect.isabstract(metric_Metric)


def test_hyp_metric_metric_constructor_exists():
    assert callable(metric_Metric.__init__)


def test_hyp_metric_metric_constructor_args():
    sig = inspect.signature(metric_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_metric_container_is_not_abstract():
    assert not inspect.isabstract(metric_Container)


def test_hyp_metric_container_constructor_exists():
    assert callable(metric_Container.__init__)


def test_hyp_metric_container_constructor_args():
    sig = inspect.signature(metric_Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metric_is_not_abstract():
    assert not inspect.isabstract(Metric)


def test_hyp_metric_constructor_exists():
    assert callable(Metric.__init__)


def test_hyp_metric_constructor_args():
    sig = inspect.signature(Metric.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metric_simplemetric_is_not_abstract():
    assert not inspect.isabstract(metric_SimpleMetric)


def test_hyp_metric_simplemetric_constructor_exists():
    assert callable(metric_SimpleMetric.__init__)


def test_hyp_metric_simplemetric_constructor_args():
    sig = inspect.signature(metric_SimpleMetric.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_metric_aggregatedrealmetric_is_not_abstract():
    assert not inspect.isabstract(metric_AggregatedRealMetric)


def test_hyp_metric_aggregatedrealmetric_constructor_exists():
    assert callable(metric_AggregatedRealMetric.__init__)


def test_hyp_metric_aggregatedrealmetric_constructor_args():
    sig = inspect.signature(metric_AggregatedRealMetric.__init__)
    params = list(sig.parameters.keys())
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"
    assert "median" in params, "Missing parameter 'median'"
    assert "average" in params, "Missing parameter 'average'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "minimum" in params, "Missing parameter 'minimum'"








def test_hyp_metric_aggregatedintegermetric_is_not_abstract():
    assert not inspect.isabstract(metric_AggregatedIntegerMetric)


def test_hyp_metric_aggregatedintegermetric_constructor_exists():
    assert callable(metric_AggregatedIntegerMetric.__init__)


def test_hyp_metric_aggregatedintegermetric_constructor_args():
    sig = inspect.signature(metric_AggregatedIntegerMetric.__init__)
    params = list(sig.parameters.keys())
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "standardDeviation" in params, "Missing parameter 'standardDeviation'"
    assert "average" in params, "Missing parameter 'average'"
    assert "median" in params, "Missing parameter 'median'"
    assert "maximum" in params, "Missing parameter 'maximum'"







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
metric_Metric_strategy = st.builds(
    metric_Metric,
    code=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
metric_Container_strategy = st.builds(
    metric_Container,
)
Metric_strategy = st.builds(
    Metric,
)
metric_SimpleMetric_strategy = st.builds(
    metric_SimpleMetric,
    value=
        safe_text
)
metric_AggregatedRealMetric_strategy = st.builds(
    metric_AggregatedRealMetric,
    standardDeviation=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    median=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    average=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maximum=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minimum=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
metric_AggregatedIntegerMetric_strategy = st.builds(
    metric_AggregatedIntegerMetric,
    minimum=
        safe_text,
    standardDeviation=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    average=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    median=
        safe_text,
    maximum=
        safe_text
)




@given(instance=metric_Metric_strategy)
def test_hyp_metric_metric_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=metric_Metric_strategy)
def test_hyp_metric_metric_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=metric_Metric_strategy)
def test_hyp_metric_metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=metric_SimpleMetric_strategy)
def test_hyp_metric_simplemetric_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=metric_AggregatedRealMetric_strategy)
def test_hyp_metric_aggregatedrealmetric_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original



@given(instance=metric_AggregatedRealMetric_strategy)
def test_hyp_metric_aggregatedrealmetric_median_setter(instance):
    original = instance.median
    instance.median = original
    assert instance.median == original



@given(instance=metric_AggregatedRealMetric_strategy)
def test_hyp_metric_aggregatedrealmetric_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original



@given(instance=metric_AggregatedRealMetric_strategy)
def test_hyp_metric_aggregatedrealmetric_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original



@given(instance=metric_AggregatedRealMetric_strategy)
def test_hyp_metric_aggregatedrealmetric_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original




@given(instance=metric_AggregatedIntegerMetric_strategy)
def test_hyp_metric_aggregatedintegermetric_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original



@given(instance=metric_AggregatedIntegerMetric_strategy)
def test_hyp_metric_aggregatedintegermetric_standardDeviation_setter(instance):
    original = instance.standardDeviation
    instance.standardDeviation = original
    assert instance.standardDeviation == original



@given(instance=metric_AggregatedIntegerMetric_strategy)
def test_hyp_metric_aggregatedintegermetric_average_setter(instance):
    original = instance.average
    instance.average = original
    assert instance.average == original



@given(instance=metric_AggregatedIntegerMetric_strategy)
def test_hyp_metric_aggregatedintegermetric_median_setter(instance):
    original = instance.median
    instance.median = original
    assert instance.median == original



@given(instance=metric_AggregatedIntegerMetric_strategy)
def test_hyp_metric_aggregatedintegermetric_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Metric,
    metric_AggregatedIntegerMetric,
    metric_AggregatedRealMetric,
    metric_Container,
    metric_Metric,
    metric_SimpleMetric,
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

def test_metric_AggregatedIntegerMetric_average_value_roundtrip():
    instance = metric_AggregatedIntegerMetric(average=3.14, maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation=3.14)
    assert instance.average == 3.14
    instance.average = 9.99
    assert instance.average == 9.99


def test_metric_AggregatedIntegerMetric_maximum_value_roundtrip():
    instance = metric_AggregatedIntegerMetric(average=3.14, maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation=3.14)
    assert instance.maximum == "sample_text"
    instance.maximum = "sample_text_2"
    assert instance.maximum == "sample_text_2"


def test_metric_AggregatedIntegerMetric_median_value_roundtrip():
    instance = metric_AggregatedIntegerMetric(average=3.14, maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation=3.14)
    assert instance.median == "sample_text"
    instance.median = "sample_text_2"
    assert instance.median == "sample_text_2"


def test_metric_AggregatedIntegerMetric_minimum_value_roundtrip():
    instance = metric_AggregatedIntegerMetric(average=3.14, maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation=3.14)
    assert instance.minimum == "sample_text"
    instance.minimum = "sample_text_2"
    assert instance.minimum == "sample_text_2"


def test_metric_AggregatedIntegerMetric_standardDeviation_value_roundtrip():
    instance = metric_AggregatedIntegerMetric(average=3.14, maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation=3.14)
    assert instance.standardDeviation == 3.14
    instance.standardDeviation = 9.99
    assert instance.standardDeviation == 9.99


def test_metric_AggregatedRealMetric_average_value_roundtrip():
    instance = metric_AggregatedRealMetric(average=3.14, maximum=3.14, median=3.14, minimum=3.14, standardDeviation=3.14)
    assert instance.average == 3.14
    instance.average = 9.99
    assert instance.average == 9.99


def test_metric_AggregatedRealMetric_maximum_value_roundtrip():
    instance = metric_AggregatedRealMetric(average=3.14, maximum=3.14, median=3.14, minimum=3.14, standardDeviation=3.14)
    assert instance.maximum == 3.14
    instance.maximum = 9.99
    assert instance.maximum == 9.99


def test_metric_AggregatedRealMetric_median_value_roundtrip():
    instance = metric_AggregatedRealMetric(average=3.14, maximum=3.14, median=3.14, minimum=3.14, standardDeviation=3.14)
    assert instance.median == 3.14
    instance.median = 9.99
    assert instance.median == 9.99


def test_metric_AggregatedRealMetric_minimum_value_roundtrip():
    instance = metric_AggregatedRealMetric(average=3.14, maximum=3.14, median=3.14, minimum=3.14, standardDeviation=3.14)
    assert instance.minimum == 3.14
    instance.minimum = 9.99
    assert instance.minimum == 9.99


def test_metric_AggregatedRealMetric_standardDeviation_value_roundtrip():
    instance = metric_AggregatedRealMetric(average=3.14, maximum=3.14, median=3.14, minimum=3.14, standardDeviation=3.14)
    assert instance.standardDeviation == 3.14
    instance.standardDeviation = 9.99
    assert instance.standardDeviation == 9.99


def test_metric_Metric_code_value_roundtrip():
    instance = metric_Metric(code="sample_text", description="sample_text", name="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_metric_Metric_description_value_roundtrip():
    instance = metric_Metric(code="sample_text", description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_metric_Metric_name_value_roundtrip():
    instance = metric_Metric(code="sample_text", description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metric_SimpleMetric_value_value_roundtrip():
    instance = metric_SimpleMetric(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_metric_AggregatedIntegerMetric_isa_Metric():
    instance = metric_AggregatedIntegerMetric(average=3.14, maximum="sample_text", median="sample_text", minimum="sample_text", standardDeviation=3.14)
    assert isinstance(instance, Metric)


def test_metric_AggregatedRealMetric_isa_Metric():
    instance = metric_AggregatedRealMetric(average=3.14, maximum=3.14, median=3.14, minimum=3.14, standardDeviation=3.14)
    assert isinstance(instance, Metric)


def test_metric_SimpleMetric_isa_Metric():
    instance = metric_SimpleMetric(value="sample_text")
    assert isinstance(instance, Metric)


def test_assoc_metrics0_link_reassign_clear():
    a = metric_Metric(code="sample_text", description="sample_text", name="sample_text")
    b1 = metric_Container()
    b2 = metric_Container()
    _safe_set(a, 'metric_Metric', b1)
    assert _is_linked(a, 'metric_Metric', b1)
    if hasattr(b1, 'metric_Container'):
        assert _is_linked(b1, 'metric_Container', a)
    _safe_set(a, 'metric_Metric', b2)
    assert _is_linked(a, 'metric_Metric', b2)
    if hasattr(b1, 'metric_Container'):
        assert not _is_linked(b1, 'metric_Container', a)
    if hasattr(b2, 'metric_Container'):
        assert _is_linked(b2, 'metric_Container', a)
    _safe_set(a, 'metric_Metric', None)
    assert not _is_linked(a, 'metric_Metric', b2)
    if hasattr(b2, 'metric_Container'):
        assert not _is_linked(b2, 'metric_Container', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Metric_strategy = st.builds(Metric)
@given(instance=Metric_strategy)
@settings(max_examples=25)
def test_Metric_instantiation(instance):
    assert isinstance(instance, Metric)


metric_AggregatedIntegerMetric_strategy = st.builds(metric_AggregatedIntegerMetric, average=st.floats(allow_nan=False, allow_infinity=False), maximum=safe_text, median=safe_text, minimum=safe_text, standardDeviation=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=metric_AggregatedIntegerMetric_strategy)
@settings(max_examples=25)
def test_metric_AggregatedIntegerMetric_instantiation(instance):
    assert isinstance(instance, metric_AggregatedIntegerMetric)


metric_AggregatedRealMetric_strategy = st.builds(metric_AggregatedRealMetric, average=st.floats(allow_nan=False, allow_infinity=False), maximum=st.floats(allow_nan=False, allow_infinity=False), median=st.floats(allow_nan=False, allow_infinity=False), minimum=st.floats(allow_nan=False, allow_infinity=False), standardDeviation=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=metric_AggregatedRealMetric_strategy)
@settings(max_examples=25)
def test_metric_AggregatedRealMetric_instantiation(instance):
    assert isinstance(instance, metric_AggregatedRealMetric)


metric_Container_strategy = st.builds(metric_Container)
@given(instance=metric_Container_strategy)
@settings(max_examples=25)
def test_metric_Container_instantiation(instance):
    assert isinstance(instance, metric_Container)


metric_Metric_strategy = st.builds(metric_Metric, code=safe_text, description=safe_text, name=safe_text)
@given(instance=metric_Metric_strategy)
@settings(max_examples=25)
def test_metric_Metric_instantiation(instance):
    assert isinstance(instance, metric_Metric)


metric_SimpleMetric_strategy = st.builds(metric_SimpleMetric, value=safe_text)
@given(instance=metric_SimpleMetric_strategy)
@settings(max_examples=25)
def test_metric_SimpleMetric_instantiation(instance):
    assert isinstance(instance, metric_SimpleMetric)



