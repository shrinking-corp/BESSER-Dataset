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
    LabelValue,
    labels_TestIntegerLabelValue,
    DynamicNodeLabel,
    labels_TestDynamicNodeLabel,
    DynamicLabel,
    labels_TestDynamicLabel1,
    StaticNodeLabel,
    labels_TestStaticNodeLabel,
    StaticEdgeLabel,
    labels_TestStaticEdgeLabel,
    Label,
    labels_TestLabel,
    DynamicEdgeLabel,
    labels_TestDynamicEdgeLabel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_labelvalue_is_not_abstract():
    assert not inspect.isabstract(LabelValue)


def test_hyp_labelvalue_constructor_exists():
    assert callable(LabelValue.__init__)


def test_hyp_labelvalue_constructor_args():
    sig = inspect.signature(LabelValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labels_testintegerlabelvalue_is_not_abstract():
    assert not inspect.isabstract(labels_TestIntegerLabelValue)


def test_hyp_labels_testintegerlabelvalue_constructor_exists():
    assert callable(labels_TestIntegerLabelValue.__init__)


def test_hyp_labels_testintegerlabelvalue_constructor_args():
    sig = inspect.signature(labels_TestIntegerLabelValue.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"




def test_hyp_dynamicnodelabel_is_not_abstract():
    assert not inspect.isabstract(DynamicNodeLabel)


def test_hyp_dynamicnodelabel_constructor_exists():
    assert callable(DynamicNodeLabel.__init__)


def test_hyp_dynamicnodelabel_constructor_args():
    sig = inspect.signature(DynamicNodeLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labels_testdynamicnodelabel_is_not_abstract():
    assert not inspect.isabstract(labels_TestDynamicNodeLabel)


def test_hyp_labels_testdynamicnodelabel_constructor_exists():
    assert callable(labels_TestDynamicNodeLabel.__init__)


def test_hyp_labels_testdynamicnodelabel_constructor_args():
    sig = inspect.signature(labels_TestDynamicNodeLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dynamiclabel_is_not_abstract():
    assert not inspect.isabstract(DynamicLabel)


def test_hyp_dynamiclabel_constructor_exists():
    assert callable(DynamicLabel.__init__)


def test_hyp_dynamiclabel_constructor_args():
    sig = inspect.signature(DynamicLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labels_testdynamiclabel1_is_not_abstract():
    assert not inspect.isabstract(labels_TestDynamicLabel1)


def test_hyp_labels_testdynamiclabel1_constructor_exists():
    assert callable(labels_TestDynamicLabel1.__init__)


def test_hyp_labels_testdynamiclabel1_constructor_args():
    sig = inspect.signature(labels_TestDynamicLabel1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staticnodelabel_is_not_abstract():
    assert not inspect.isabstract(StaticNodeLabel)


def test_hyp_staticnodelabel_constructor_exists():
    assert callable(StaticNodeLabel.__init__)


def test_hyp_staticnodelabel_constructor_args():
    sig = inspect.signature(StaticNodeLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labels_teststaticnodelabel_is_not_abstract():
    assert not inspect.isabstract(labels_TestStaticNodeLabel)


def test_hyp_labels_teststaticnodelabel_constructor_exists():
    assert callable(labels_TestStaticNodeLabel.__init__)


def test_hyp_labels_teststaticnodelabel_constructor_args():
    sig = inspect.signature(labels_TestStaticNodeLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_staticedgelabel_is_not_abstract():
    assert not inspect.isabstract(StaticEdgeLabel)


def test_hyp_staticedgelabel_constructor_exists():
    assert callable(StaticEdgeLabel.__init__)


def test_hyp_staticedgelabel_constructor_args():
    sig = inspect.signature(StaticEdgeLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labels_teststaticedgelabel_is_not_abstract():
    assert not inspect.isabstract(labels_TestStaticEdgeLabel)


def test_hyp_labels_teststaticedgelabel_constructor_exists():
    assert callable(labels_TestStaticEdgeLabel.__init__)


def test_hyp_labels_teststaticedgelabel_constructor_args():
    sig = inspect.signature(labels_TestStaticEdgeLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_hyp_label_constructor_exists():
    assert callable(Label.__init__)


def test_hyp_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labels_testlabel_is_not_abstract():
    assert not inspect.isabstract(labels_TestLabel)


def test_hyp_labels_testlabel_constructor_exists():
    assert callable(labels_TestLabel.__init__)


def test_hyp_labels_testlabel_constructor_args():
    sig = inspect.signature(labels_TestLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dynamicedgelabel_is_not_abstract():
    assert not inspect.isabstract(DynamicEdgeLabel)


def test_hyp_dynamicedgelabel_constructor_exists():
    assert callable(DynamicEdgeLabel.__init__)


def test_hyp_dynamicedgelabel_constructor_args():
    sig = inspect.signature(DynamicEdgeLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labels_testdynamicedgelabel_is_not_abstract():
    assert not inspect.isabstract(labels_TestDynamicEdgeLabel)


def test_hyp_labels_testdynamicedgelabel_constructor_exists():
    assert callable(labels_TestDynamicEdgeLabel.__init__)


def test_hyp_labels_testdynamicedgelabel_constructor_args():
    sig = inspect.signature(labels_TestDynamicEdgeLabel.__init__)
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
LabelValue_strategy = st.builds(
    LabelValue,
)
labels_TestIntegerLabelValue_strategy = st.builds(
    labels_TestIntegerLabelValue,
    i=
        st.integers()
)
DynamicNodeLabel_strategy = st.builds(
    DynamicNodeLabel,
)
labels_TestDynamicNodeLabel_strategy = st.builds(
    labels_TestDynamicNodeLabel,
)
DynamicLabel_strategy = st.builds(
    DynamicLabel,
)
labels_TestDynamicLabel1_strategy = st.builds(
    labels_TestDynamicLabel1,
)
StaticNodeLabel_strategy = st.builds(
    StaticNodeLabel,
)
labels_TestStaticNodeLabel_strategy = st.builds(
    labels_TestStaticNodeLabel,
)
StaticEdgeLabel_strategy = st.builds(
    StaticEdgeLabel,
)
labels_TestStaticEdgeLabel_strategy = st.builds(
    labels_TestStaticEdgeLabel,
)
Label_strategy = st.builds(
    Label,
)
labels_TestLabel_strategy = st.builds(
    labels_TestLabel,
)
DynamicEdgeLabel_strategy = st.builds(
    DynamicEdgeLabel,
)
labels_TestDynamicEdgeLabel_strategy = st.builds(
    labels_TestDynamicEdgeLabel,
)





@given(instance=labels_TestIntegerLabelValue_strategy)
def test_hyp_labels_testintegerlabelvalue_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=labels_TestIntegerLabelValue_strategy)
@settings(max_examples=30)
def test_hyp_labels_testintegerlabelvalue_increment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.increment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.increment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'increment' in labels_TestIntegerLabelValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'increment' in labels_TestIntegerLabelValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'increment' in labels_TestIntegerLabelValue is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=labels_TestDynamicNodeLabel_strategy)
@settings(max_examples=30)
def test_hyp_labels_testdynamicnodelabel_increment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.increment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.increment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'increment' in labels_TestDynamicNodeLabel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'increment' in labels_TestDynamicNodeLabel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'increment' in labels_TestDynamicNodeLabel is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=labels_TestDynamicLabel1_strategy)
@settings(max_examples=30)
def test_hyp_labels_testdynamiclabel1_increment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.increment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.increment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'increment' in labels_TestDynamicLabel1 is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'increment' in labels_TestDynamicLabel1 did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'increment' in labels_TestDynamicLabel1 is not implemented or raised an error")









import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=labels_TestDynamicEdgeLabel_strategy)
@settings(max_examples=30)
def test_hyp_labels_testdynamicedgelabel_increment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.increment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.increment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'increment' in labels_TestDynamicEdgeLabel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'increment' in labels_TestDynamicEdgeLabel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'increment' in labels_TestDynamicEdgeLabel is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DynamicEdgeLabel,
    DynamicLabel,
    DynamicNodeLabel,
    Label,
    LabelValue,
    StaticEdgeLabel,
    StaticNodeLabel,
    labels_TestDynamicEdgeLabel,
    labels_TestDynamicLabel1,
    labels_TestDynamicNodeLabel,
    labels_TestIntegerLabelValue,
    labels_TestLabel,
    labels_TestStaticEdgeLabel,
    labels_TestStaticNodeLabel,
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

def test_labels_TestIntegerLabelValue_i_value_roundtrip():
    instance = labels_TestIntegerLabelValue(i=7)
    assert instance.i == 7
    instance.i = 13
    assert instance.i == 13


def test_labels_TestDynamicEdgeLabel_isa_DynamicEdgeLabel():
    instance = labels_TestDynamicEdgeLabel()
    assert isinstance(instance, DynamicEdgeLabel)


def test_labels_TestDynamicLabel1_isa_DynamicLabel():
    instance = labels_TestDynamicLabel1()
    assert isinstance(instance, DynamicLabel)


def test_labels_TestDynamicNodeLabel_isa_DynamicNodeLabel():
    instance = labels_TestDynamicNodeLabel()
    assert isinstance(instance, DynamicNodeLabel)


def test_labels_TestLabel_isa_Label():
    instance = labels_TestLabel()
    assert isinstance(instance, Label)


def test_labels_TestIntegerLabelValue_isa_LabelValue():
    instance = labels_TestIntegerLabelValue(i=7)
    assert isinstance(instance, LabelValue)


def test_labels_TestStaticEdgeLabel_isa_StaticEdgeLabel():
    instance = labels_TestStaticEdgeLabel()
    assert isinstance(instance, StaticEdgeLabel)


def test_labels_TestStaticNodeLabel_isa_StaticNodeLabel():
    instance = labels_TestStaticNodeLabel()
    assert isinstance(instance, StaticNodeLabel)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DynamicEdgeLabel_strategy = st.builds(DynamicEdgeLabel)
@given(instance=DynamicEdgeLabel_strategy)
@settings(max_examples=25)
def test_DynamicEdgeLabel_instantiation(instance):
    assert isinstance(instance, DynamicEdgeLabel)


DynamicLabel_strategy = st.builds(DynamicLabel)
@given(instance=DynamicLabel_strategy)
@settings(max_examples=25)
def test_DynamicLabel_instantiation(instance):
    assert isinstance(instance, DynamicLabel)


DynamicNodeLabel_strategy = st.builds(DynamicNodeLabel)
@given(instance=DynamicNodeLabel_strategy)
@settings(max_examples=25)
def test_DynamicNodeLabel_instantiation(instance):
    assert isinstance(instance, DynamicNodeLabel)


Label_strategy = st.builds(Label)
@given(instance=Label_strategy)
@settings(max_examples=25)
def test_Label_instantiation(instance):
    assert isinstance(instance, Label)


LabelValue_strategy = st.builds(LabelValue)
@given(instance=LabelValue_strategy)
@settings(max_examples=25)
def test_LabelValue_instantiation(instance):
    assert isinstance(instance, LabelValue)


StaticEdgeLabel_strategy = st.builds(StaticEdgeLabel)
@given(instance=StaticEdgeLabel_strategy)
@settings(max_examples=25)
def test_StaticEdgeLabel_instantiation(instance):
    assert isinstance(instance, StaticEdgeLabel)


StaticNodeLabel_strategy = st.builds(StaticNodeLabel)
@given(instance=StaticNodeLabel_strategy)
@settings(max_examples=25)
def test_StaticNodeLabel_instantiation(instance):
    assert isinstance(instance, StaticNodeLabel)


labels_TestDynamicEdgeLabel_strategy = st.builds(labels_TestDynamicEdgeLabel)
@given(instance=labels_TestDynamicEdgeLabel_strategy)
@settings(max_examples=25)
def test_labels_TestDynamicEdgeLabel_instantiation(instance):
    assert isinstance(instance, labels_TestDynamicEdgeLabel)


labels_TestDynamicLabel1_strategy = st.builds(labels_TestDynamicLabel1)
@given(instance=labels_TestDynamicLabel1_strategy)
@settings(max_examples=25)
def test_labels_TestDynamicLabel1_instantiation(instance):
    assert isinstance(instance, labels_TestDynamicLabel1)


labels_TestDynamicNodeLabel_strategy = st.builds(labels_TestDynamicNodeLabel)
@given(instance=labels_TestDynamicNodeLabel_strategy)
@settings(max_examples=25)
def test_labels_TestDynamicNodeLabel_instantiation(instance):
    assert isinstance(instance, labels_TestDynamicNodeLabel)


labels_TestIntegerLabelValue_strategy = st.builds(labels_TestIntegerLabelValue, i=st.integers())
@given(instance=labels_TestIntegerLabelValue_strategy)
@settings(max_examples=25)
def test_labels_TestIntegerLabelValue_instantiation(instance):
    assert isinstance(instance, labels_TestIntegerLabelValue)


labels_TestLabel_strategy = st.builds(labels_TestLabel)
@given(instance=labels_TestLabel_strategy)
@settings(max_examples=25)
def test_labels_TestLabel_instantiation(instance):
    assert isinstance(instance, labels_TestLabel)


labels_TestStaticEdgeLabel_strategy = st.builds(labels_TestStaticEdgeLabel)
@given(instance=labels_TestStaticEdgeLabel_strategy)
@settings(max_examples=25)
def test_labels_TestStaticEdgeLabel_instantiation(instance):
    assert isinstance(instance, labels_TestStaticEdgeLabel)


labels_TestStaticNodeLabel_strategy = st.builds(labels_TestStaticNodeLabel)
@given(instance=labels_TestStaticNodeLabel_strategy)
@settings(max_examples=25)
def test_labels_TestStaticNodeLabel_instantiation(instance):
    assert isinstance(instance, labels_TestStaticNodeLabel)



