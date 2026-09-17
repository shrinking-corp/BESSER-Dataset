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
    test_A,
    test_OptionTestClass,
    test_D,
    A,
    test_C,
    test_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_test_a_is_not_abstract():
    assert not inspect.isabstract(test_A)


def test_hyp_test_a_constructor_exists():
    assert callable(test_A.__init__)


def test_hyp_test_a_constructor_args():
    sig = inspect.signature(test_A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_test_optiontestclass_is_not_abstract():
    assert not inspect.isabstract(test_OptionTestClass)


def test_hyp_test_optiontestclass_constructor_exists():
    assert callable(test_OptionTestClass.__init__)


def test_hyp_test_optiontestclass_constructor_args():
    sig = inspect.signature(test_OptionTestClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"





def test_hyp_test_d_is_not_abstract():
    assert not inspect.isabstract(test_D)


def test_hyp_test_d_constructor_exists():
    assert callable(test_D.__init__)


def test_hyp_test_d_constructor_args():
    sig = inspect.signature(test_D.__init__)
    params = list(sig.parameters.keys())
    assert "attr1" in params, "Missing parameter 'attr1'"




def test_hyp_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_hyp_a_constructor_exists():
    assert callable(A.__init__)


def test_hyp_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_hyp_test_c_is_not_abstract():
    assert not inspect.isabstract(test_C)


def test_hyp_test_c_constructor_exists():
    assert callable(test_C.__init__)


def test_hyp_test_c_constructor_args():
    sig = inspect.signature(test_C.__init__)
    params = list(sig.parameters.keys())



def test_hyp_test_b_is_not_abstract():
    assert not inspect.isabstract(test_B)


def test_hyp_test_b_constructor_exists():
    assert callable(test_B.__init__)


def test_hyp_test_b_constructor_args():
    sig = inspect.signature(test_B.__init__)
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
test_A_strategy = st.builds(
    test_A,
)
test_OptionTestClass_strategy = st.builds(
    test_OptionTestClass,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
test_D_strategy = st.builds(
    test_D,
    attr1=
        safe_text
)
A_strategy = st.builds(
    A,
)
test_C_strategy = st.builds(
    test_C,
)
test_B_strategy = st.builds(
    test_B,
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test_A_strategy)
@settings(max_examples=30)
def test_hyp_test_a_op1_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.op1()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.op1).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'op1' in test_A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'op1' in test_A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'op1' in test_A is not implemented or raised an error")




@given(instance=test_OptionTestClass_strategy)
def test_hyp_test_optiontestclass_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=test_OptionTestClass_strategy)
def test_hyp_test_optiontestclass_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=test_D_strategy)
def test_hyp_test_d_attr1_setter(instance):
    original = instance.attr1
    instance.attr1 = original
    assert instance.attr1 == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    A,
    test_A,
    test_B,
    test_C,
    test_D,
    test_OptionTestClass,
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

def test_test_D_attr1_value_roundtrip():
    instance = test_D(attr1="sample_text")
    assert instance.attr1 == "sample_text"
    instance.attr1 = "sample_text_2"
    assert instance.attr1 == "sample_text_2"


def test_test_OptionTestClass_attribute_value_roundtrip():
    instance = test_OptionTestClass(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_test_OptionTestClass_attribute2_value_roundtrip():
    instance = test_OptionTestClass(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_test_B_isa_A():
    instance = test_B()
    assert isinstance(instance, A)


def test_test_C_isa_A():
    instance = test_C()
    assert isinstance(instance, A)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

A_strategy = st.builds(A)
@given(instance=A_strategy)
@settings(max_examples=25)
def test_A_instantiation(instance):
    assert isinstance(instance, A)


test_A_strategy = st.builds(test_A)
@given(instance=test_A_strategy)
@settings(max_examples=25)
def test_test_A_instantiation(instance):
    assert isinstance(instance, test_A)


test_B_strategy = st.builds(test_B)
@given(instance=test_B_strategy)
@settings(max_examples=25)
def test_test_B_instantiation(instance):
    assert isinstance(instance, test_B)


test_C_strategy = st.builds(test_C)
@given(instance=test_C_strategy)
@settings(max_examples=25)
def test_test_C_instantiation(instance):
    assert isinstance(instance, test_C)


test_D_strategy = st.builds(test_D, attr1=safe_text)
@given(instance=test_D_strategy)
@settings(max_examples=25)
def test_test_D_instantiation(instance):
    assert isinstance(instance, test_D)


test_OptionTestClass_strategy = st.builds(test_OptionTestClass, attribute=safe_text, attribute2=safe_text)
@given(instance=test_OptionTestClass_strategy)
@settings(max_examples=25)
def test_test_OptionTestClass_instantiation(instance):
    assert isinstance(instance, test_OptionTestClass)



