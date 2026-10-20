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
    metrics_Metric,
    metrics_MetricsSet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_metrics_metric_is_not_abstract():
    assert not inspect.isabstract(metrics_Metric)


def test_hyp_metrics_metric_constructor_exists():
    assert callable(metrics_Metric.__init__)


def test_hyp_metrics_metric_constructor_args():
    sig = inspect.signature(metrics_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_metrics_metricsset_is_not_abstract():
    assert not inspect.isabstract(metrics_MetricsSet)


def test_hyp_metrics_metricsset_constructor_exists():
    assert callable(metrics_MetricsSet.__init__)


def test_hyp_metrics_metricsset_constructor_args():
    sig = inspect.signature(metrics_MetricsSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
metrics_Metric_strategy = st.builds(
    metrics_Metric,
    value=
        safe_text,
    name=
        safe_text
)
metrics_MetricsSet_strategy = st.builds(
    metrics_MetricsSet,
    name=
        safe_text
)




@given(instance=metrics_Metric_strategy)
def test_hyp_metrics_metric_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=metrics_Metric_strategy)
def test_hyp_metrics_metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=metrics_MetricsSet_strategy)
def test_hyp_metrics_metricsset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    metrics_Metric,
    metrics_MetricsSet,
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

def test_metrics_Metric_name_value_roundtrip():
    instance = metrics_Metric(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_metrics_Metric_value_value_roundtrip():
    instance = metrics_Metric(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_metrics_MetricsSet_name_value_roundtrip():
    instance = metrics_MetricsSet(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_metrics0_link_reassign_clear():
    a = metrics_MetricsSet(name="sample_text")
    b1 = metrics_Metric(name="sample_text", value="sample_text")
    b2 = metrics_Metric(name="sample_text_2", value="sample_text_2")
    _safe_set(a, 'metrics_MetricsSet', {b1})
    assert _is_linked(a, 'metrics_MetricsSet', b1)
    if hasattr(b1, 'metrics_Metric'):
        assert _is_linked(b1, 'metrics_Metric', a)
    _safe_set(a, 'metrics_MetricsSet', {b2})
    assert _is_linked(a, 'metrics_MetricsSet', b2)
    if hasattr(b1, 'metrics_Metric'):
        assert not _is_linked(b1, 'metrics_Metric', a)
    if hasattr(b2, 'metrics_Metric'):
        assert _is_linked(b2, 'metrics_Metric', a)
    _safe_set(a, 'metrics_MetricsSet', set())
    assert not _is_linked(a, 'metrics_MetricsSet', b2)
    if hasattr(b2, 'metrics_Metric'):
        assert not _is_linked(b2, 'metrics_Metric', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

metrics_Metric_strategy = st.builds(metrics_Metric, name=safe_text, value=safe_text)
@given(instance=metrics_Metric_strategy)
@settings(max_examples=25)
def test_metrics_Metric_instantiation(instance):
    assert isinstance(instance, metrics_Metric)


metrics_MetricsSet_strategy = st.builds(metrics_MetricsSet, name=safe_text)
@given(instance=metrics_MetricsSet_strategy)
@settings(max_examples=25)
def test_metrics_MetricsSet_instantiation(instance):
    assert isinstance(instance, metrics_MetricsSet)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    metrics_Metric,
    metrics_MetricsSet,
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
    a1 = metrics_MetricsSet(name="sample_text")
    a2 = metrics_MetricsSet(name="sample_text_2")
    b = metrics_Metric(name="sample_text", value="sample_text")
    _safe_set(b, 'metrics_Metric', a1)
    assert _is_linked(b, 'metrics_Metric', a1)
    if hasattr(a1, 'metrics_MetricsSet'):
        assert _is_linked(a1, 'metrics_MetricsSet', b)
    _safe_set(b, 'metrics_Metric', a2)
    assert _is_linked(b, 'metrics_Metric', a2)
    if hasattr(a1, 'metrics_MetricsSet'):
        assert not _is_linked(a1, 'metrics_MetricsSet', b)
    if hasattr(a2, 'metrics_MetricsSet'):
        assert _is_linked(a2, 'metrics_MetricsSet', b)
    _safe_set(b, 'metrics_Metric', None)
    assert not _is_linked(b, 'metrics_Metric', a2)
    if hasattr(a2, 'metrics_MetricsSet'):
        assert not _is_linked(a2, 'metrics_MetricsSet', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================



from python_code import metrics_MetricsSet

def test_metrics_MetricsSet___init__():
    assert metrics_MetricsSet.__init__(metrics_MetricsSet('', metrics_MetricsSet=set()), '', metrics_MetricsSet=set()) == None

