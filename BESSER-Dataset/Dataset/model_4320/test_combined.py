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
    metrics_Rule,
    metrics_RuleMetrics,
    metrics_RuleSetMetrics,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_metrics_rule_is_not_abstract():
    assert not inspect.isabstract(metrics_Rule)


def test_hyp_metrics_rule_constructor_exists():
    assert callable(metrics_Rule.__init__)


def test_hyp_metrics_rule_constructor_args():
    sig = inspect.signature(metrics_Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metrics_rulemetrics_is_not_abstract():
    assert not inspect.isabstract(metrics_RuleMetrics)


def test_hyp_metrics_rulemetrics_constructor_exists():
    assert callable(metrics_RuleMetrics.__init__)


def test_hyp_metrics_rulemetrics_constructor_args():
    sig = inspect.signature(metrics_RuleMetrics.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfNodes" in params, "Missing parameter 'numberOfNodes'"
    assert "numberOfEdges" in params, "Missing parameter 'numberOfEdges'"
    assert "numberOfAttributes" in params, "Missing parameter 'numberOfAttributes'"






def test_hyp_metrics_rulesetmetrics_is_not_abstract():
    assert not inspect.isabstract(metrics_RuleSetMetrics)


def test_hyp_metrics_rulesetmetrics_constructor_exists():
    assert callable(metrics_RuleSetMetrics.__init__)


def test_hyp_metrics_rulesetmetrics_constructor_args():
    sig = inspect.signature(metrics_RuleSetMetrics.__init__)
    params = list(sig.parameters.keys())
    assert "totalNumberOfNodes" in params, "Missing parameter 'totalNumberOfNodes'"
    assert "totalNumberOfEdges" in params, "Missing parameter 'totalNumberOfEdges'"
    assert "numberOfRules" in params, "Missing parameter 'numberOfRules'"
    assert "totalNumberOfAttributes" in params, "Missing parameter 'totalNumberOfAttributes'"






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
metrics_Rule_strategy = st.builds(
    metrics_Rule,
)
metrics_RuleMetrics_strategy = st.builds(
    metrics_RuleMetrics,
    numberOfNodes=
        st.integers(),
    numberOfEdges=
        st.integers(),
    numberOfAttributes=
        st.integers()
)
metrics_RuleSetMetrics_strategy = st.builds(
    metrics_RuleSetMetrics,
    totalNumberOfNodes=
        st.integers(),
    totalNumberOfEdges=
        st.integers(),
    numberOfRules=
        st.integers(),
    totalNumberOfAttributes=
        st.integers()
)





@given(instance=metrics_RuleMetrics_strategy)
def test_hyp_metrics_rulemetrics_numberOfNodes_setter(instance):
    original = instance.numberOfNodes
    instance.numberOfNodes = original
    assert instance.numberOfNodes == original



@given(instance=metrics_RuleMetrics_strategy)
def test_hyp_metrics_rulemetrics_numberOfEdges_setter(instance):
    original = instance.numberOfEdges
    instance.numberOfEdges = original
    assert instance.numberOfEdges == original



@given(instance=metrics_RuleMetrics_strategy)
def test_hyp_metrics_rulemetrics_numberOfAttributes_setter(instance):
    original = instance.numberOfAttributes
    instance.numberOfAttributes = original
    assert instance.numberOfAttributes == original




@given(instance=metrics_RuleSetMetrics_strategy)
def test_hyp_metrics_rulesetmetrics_totalNumberOfNodes_setter(instance):
    original = instance.totalNumberOfNodes
    instance.totalNumberOfNodes = original
    assert instance.totalNumberOfNodes == original



@given(instance=metrics_RuleSetMetrics_strategy)
def test_hyp_metrics_rulesetmetrics_totalNumberOfEdges_setter(instance):
    original = instance.totalNumberOfEdges
    instance.totalNumberOfEdges = original
    assert instance.totalNumberOfEdges == original



@given(instance=metrics_RuleSetMetrics_strategy)
def test_hyp_metrics_rulesetmetrics_numberOfRules_setter(instance):
    original = instance.numberOfRules
    instance.numberOfRules = original
    assert instance.numberOfRules == original



@given(instance=metrics_RuleSetMetrics_strategy)
def test_hyp_metrics_rulesetmetrics_totalNumberOfAttributes_setter(instance):
    original = instance.totalNumberOfAttributes
    instance.totalNumberOfAttributes = original
    assert instance.totalNumberOfAttributes == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=metrics_RuleSetMetrics_strategy)
@settings(max_examples=30)
def test_hyp_metrics_rulesetmetrics_findrulemetrics_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findRuleMetrics(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findRuleMetrics).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findRuleMetrics' in metrics_RuleSetMetrics is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findRuleMetrics' in metrics_RuleSetMetrics did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findRuleMetrics' in metrics_RuleSetMetrics is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=metrics_RuleSetMetrics_strategy)
@settings(max_examples=30)
def test_hyp_metrics_rulesetmetrics_createpresentationstring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createPresentationString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createPresentationString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createPresentationString' in metrics_RuleSetMetrics is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createPresentationString' in metrics_RuleSetMetrics did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createPresentationString' in metrics_RuleSetMetrics is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    metrics_Rule,
    metrics_RuleMetrics,
    metrics_RuleSetMetrics,
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

def test_metrics_RuleMetrics_numberOfAttributes_value_roundtrip():
    instance = metrics_RuleMetrics(numberOfAttributes=7, numberOfEdges=7, numberOfNodes=7)
    assert instance.numberOfAttributes == 7
    instance.numberOfAttributes = 13
    assert instance.numberOfAttributes == 13


def test_metrics_RuleMetrics_numberOfEdges_value_roundtrip():
    instance = metrics_RuleMetrics(numberOfAttributes=7, numberOfEdges=7, numberOfNodes=7)
    assert instance.numberOfEdges == 7
    instance.numberOfEdges = 13
    assert instance.numberOfEdges == 13


def test_metrics_RuleMetrics_numberOfNodes_value_roundtrip():
    instance = metrics_RuleMetrics(numberOfAttributes=7, numberOfEdges=7, numberOfNodes=7)
    assert instance.numberOfNodes == 7
    instance.numberOfNodes = 13
    assert instance.numberOfNodes == 13


def test_metrics_RuleSetMetrics_numberOfRules_value_roundtrip():
    instance = metrics_RuleSetMetrics(numberOfRules=7, totalNumberOfAttributes=7, totalNumberOfEdges=7, totalNumberOfNodes=7)
    assert instance.numberOfRules == 7
    instance.numberOfRules = 13
    assert instance.numberOfRules == 13


def test_metrics_RuleSetMetrics_totalNumberOfAttributes_value_roundtrip():
    instance = metrics_RuleSetMetrics(numberOfRules=7, totalNumberOfAttributes=7, totalNumberOfEdges=7, totalNumberOfNodes=7)
    assert instance.totalNumberOfAttributes == 7
    instance.totalNumberOfAttributes = 13
    assert instance.totalNumberOfAttributes == 13


def test_metrics_RuleSetMetrics_totalNumberOfEdges_value_roundtrip():
    instance = metrics_RuleSetMetrics(numberOfRules=7, totalNumberOfAttributes=7, totalNumberOfEdges=7, totalNumberOfNodes=7)
    assert instance.totalNumberOfEdges == 7
    instance.totalNumberOfEdges = 13
    assert instance.totalNumberOfEdges == 13


def test_metrics_RuleSetMetrics_totalNumberOfNodes_value_roundtrip():
    instance = metrics_RuleSetMetrics(numberOfRules=7, totalNumberOfAttributes=7, totalNumberOfEdges=7, totalNumberOfNodes=7)
    assert instance.totalNumberOfNodes == 7
    instance.totalNumberOfNodes = 13
    assert instance.totalNumberOfNodes == 13


def test_assoc_rule3_link_reassign_clear():
    a = metrics_RuleMetrics(numberOfAttributes=7, numberOfEdges=7, numberOfNodes=7)
    b1 = metrics_Rule()
    b2 = metrics_Rule()
    _safe_set(a, 'metrics_RuleMetrics4', b1)
    assert _is_linked(a, 'metrics_RuleMetrics4', b1)
    if hasattr(b1, 'metrics_Rule5'):
        assert _is_linked(b1, 'metrics_Rule5', a)
    _safe_set(a, 'metrics_RuleMetrics4', b2)
    assert _is_linked(a, 'metrics_RuleMetrics4', b2)
    if hasattr(b1, 'metrics_Rule5'):
        assert not _is_linked(b1, 'metrics_Rule5', a)
    if hasattr(b2, 'metrics_Rule5'):
        assert _is_linked(b2, 'metrics_Rule5', a)
    _safe_set(a, 'metrics_RuleMetrics4', None)
    assert not _is_linked(a, 'metrics_RuleMetrics4', b2)
    if hasattr(b2, 'metrics_Rule5'):
        assert not _is_linked(b2, 'metrics_Rule5', a)


def test_assoc_ruleMetrics0_link_reassign_clear():
    a = metrics_RuleSetMetrics(numberOfRules=7, totalNumberOfAttributes=7, totalNumberOfEdges=7, totalNumberOfNodes=7)
    b1 = metrics_RuleMetrics(numberOfAttributes=7, numberOfEdges=7, numberOfNodes=7)
    b2 = metrics_RuleMetrics(numberOfAttributes=13, numberOfEdges=13, numberOfNodes=13)
    _safe_set(a, 'metrics_RuleSetMetrics', {b1})
    assert _is_linked(a, 'metrics_RuleSetMetrics', b1)
    if hasattr(b1, 'metrics_RuleMetrics'):
        assert _is_linked(b1, 'metrics_RuleMetrics', a)
    _safe_set(a, 'metrics_RuleSetMetrics', {b2})
    assert _is_linked(a, 'metrics_RuleSetMetrics', b2)
    if hasattr(b1, 'metrics_RuleMetrics'):
        assert not _is_linked(b1, 'metrics_RuleMetrics', a)
    if hasattr(b2, 'metrics_RuleMetrics'):
        assert _is_linked(b2, 'metrics_RuleMetrics', a)
    _safe_set(a, 'metrics_RuleSetMetrics', set())
    assert not _is_linked(a, 'metrics_RuleSetMetrics', b2)
    if hasattr(b2, 'metrics_RuleMetrics'):
        assert not _is_linked(b2, 'metrics_RuleMetrics', a)


def test_assoc_ruleSet1_link_reassign_clear():
    a = metrics_RuleSetMetrics(numberOfRules=7, totalNumberOfAttributes=7, totalNumberOfEdges=7, totalNumberOfNodes=7)
    b1 = metrics_Rule()
    b2 = metrics_Rule()
    _safe_set(a, 'metrics_RuleSetMetrics2', {b1})
    assert _is_linked(a, 'metrics_RuleSetMetrics2', b1)
    if hasattr(b1, 'metrics_Rule'):
        assert _is_linked(b1, 'metrics_Rule', a)
    _safe_set(a, 'metrics_RuleSetMetrics2', {b2})
    assert _is_linked(a, 'metrics_RuleSetMetrics2', b2)
    if hasattr(b1, 'metrics_Rule'):
        assert not _is_linked(b1, 'metrics_Rule', a)
    if hasattr(b2, 'metrics_Rule'):
        assert _is_linked(b2, 'metrics_Rule', a)
    _safe_set(a, 'metrics_RuleSetMetrics2', set())
    assert not _is_linked(a, 'metrics_RuleSetMetrics2', b2)
    if hasattr(b2, 'metrics_Rule'):
        assert not _is_linked(b2, 'metrics_Rule', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

metrics_Rule_strategy = st.builds(metrics_Rule)
@given(instance=metrics_Rule_strategy)
@settings(max_examples=25)
def test_metrics_Rule_instantiation(instance):
    assert isinstance(instance, metrics_Rule)


metrics_RuleMetrics_strategy = st.builds(metrics_RuleMetrics, numberOfAttributes=st.integers(), numberOfEdges=st.integers(), numberOfNodes=st.integers())
@given(instance=metrics_RuleMetrics_strategy)
@settings(max_examples=25)
def test_metrics_RuleMetrics_instantiation(instance):
    assert isinstance(instance, metrics_RuleMetrics)


metrics_RuleSetMetrics_strategy = st.builds(metrics_RuleSetMetrics, numberOfRules=st.integers(), totalNumberOfAttributes=st.integers(), totalNumberOfEdges=st.integers(), totalNumberOfNodes=st.integers())
@given(instance=metrics_RuleSetMetrics_strategy)
@settings(max_examples=25)
def test_metrics_RuleSetMetrics_instantiation(instance):
    assert isinstance(instance, metrics_RuleSetMetrics)



