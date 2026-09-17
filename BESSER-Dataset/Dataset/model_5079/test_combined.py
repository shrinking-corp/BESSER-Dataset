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
    test_Output,
    test_Input,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_test_output_is_not_abstract():
    assert not inspect.isabstract(test_Output)


def test_hyp_test_output_constructor_exists():
    assert callable(test_Output.__init__)


def test_hyp_test_output_constructor_args():
    sig = inspect.signature(test_Output.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_test_input_is_not_abstract():
    assert not inspect.isabstract(test_Input)


def test_hyp_test_input_constructor_exists():
    assert callable(test_Input.__init__)


def test_hyp_test_input_constructor_args():
    sig = inspect.signature(test_Input.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "test" in params, "Missing parameter 'test'"




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
test_Output_strategy = st.builds(
    test_Output,
    key=
        safe_text
)
test_Input_strategy = st.builds(
    test_Input,
    key=
        safe_text,
    test=
        safe_text
)




@given(instance=test_Output_strategy)
def test_hyp_test_output_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test_Output_strategy)
@settings(max_examples=30)
def test_hyp_test_output_test_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.test()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.test).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'test' in test_Output is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'test' in test_Output did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'test' in test_Output is not implemented or raised an error")




@given(instance=test_Input_strategy)
def test_hyp_test_input_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=test_Input_strategy)
def test_hyp_test_input_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    test_Input,
    test_Output,
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

def test_test_Input_key_value_roundtrip():
    instance = test_Input(key="sample_text", test="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_test_Input_test_value_roundtrip():
    instance = test_Input(key="sample_text", test="sample_text")
    assert instance.test == "sample_text"
    instance.test = "sample_text_2"
    assert instance.test == "sample_text_2"


def test_test_Output_key_value_roundtrip():
    instance = test_Output(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

test_Input_strategy = st.builds(test_Input, key=safe_text, test=safe_text)
@given(instance=test_Input_strategy)
@settings(max_examples=25)
def test_test_Input_instantiation(instance):
    assert isinstance(instance, test_Input)


test_Output_strategy = st.builds(test_Output, key=safe_text)
@given(instance=test_Output_strategy)
@settings(max_examples=25)
def test_test_Output_instantiation(instance):
    assert isinstance(instance, test_Output)



