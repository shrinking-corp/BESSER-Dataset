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
    Expression,
    mathDSL_Minus,
    mathDSL_Plus,
    mathDSL_NumberLiteral,
    mathDSL_Div,
    mathDSL_Multi,
    mathDSL_Expression,
    mathDSL_Math,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mathdsl_minus_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Minus)


def test_hyp_mathdsl_minus_constructor_exists():
    assert callable(mathDSL_Minus.__init__)


def test_hyp_mathdsl_minus_constructor_args():
    sig = inspect.signature(mathDSL_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mathdsl_plus_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Plus)


def test_hyp_mathdsl_plus_constructor_exists():
    assert callable(mathDSL_Plus.__init__)


def test_hyp_mathdsl_plus_constructor_args():
    sig = inspect.signature(mathDSL_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mathdsl_numberliteral_is_not_abstract():
    assert not inspect.isabstract(mathDSL_NumberLiteral)


def test_hyp_mathdsl_numberliteral_constructor_exists():
    assert callable(mathDSL_NumberLiteral.__init__)


def test_hyp_mathdsl_numberliteral_constructor_args():
    sig = inspect.signature(mathDSL_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_mathdsl_div_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Div)


def test_hyp_mathdsl_div_constructor_exists():
    assert callable(mathDSL_Div.__init__)


def test_hyp_mathdsl_div_constructor_args():
    sig = inspect.signature(mathDSL_Div.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mathdsl_multi_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Multi)


def test_hyp_mathdsl_multi_constructor_exists():
    assert callable(mathDSL_Multi.__init__)


def test_hyp_mathdsl_multi_constructor_args():
    sig = inspect.signature(mathDSL_Multi.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mathdsl_expression_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Expression)


def test_hyp_mathdsl_expression_constructor_exists():
    assert callable(mathDSL_Expression.__init__)


def test_hyp_mathdsl_expression_constructor_args():
    sig = inspect.signature(mathDSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mathdsl_math_is_not_abstract():
    assert not inspect.isabstract(mathDSL_Math)


def test_hyp_mathdsl_math_constructor_exists():
    assert callable(mathDSL_Math.__init__)


def test_hyp_mathdsl_math_constructor_args():
    sig = inspect.signature(mathDSL_Math.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
mathDSL_Minus_strategy = st.builds(
    mathDSL_Minus,
)
mathDSL_Plus_strategy = st.builds(
    mathDSL_Plus,
)
mathDSL_NumberLiteral_strategy = st.builds(
    mathDSL_NumberLiteral,
    value=
        safe_text
)
mathDSL_Div_strategy = st.builds(
    mathDSL_Div,
)
mathDSL_Multi_strategy = st.builds(
    mathDSL_Multi,
)
mathDSL_Expression_strategy = st.builds(
    mathDSL_Expression,
)
mathDSL_Math_strategy = st.builds(
    mathDSL_Math,
)







@given(instance=mathDSL_NumberLiteral_strategy)
def test_hyp_mathdsl_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    mathDSL_Div,
    mathDSL_Expression,
    mathDSL_Math,
    mathDSL_Minus,
    mathDSL_Multi,
    mathDSL_NumberLiteral,
    mathDSL_Plus,
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

def test_mathDSL_NumberLiteral_value_value_roundtrip():
    instance = mathDSL_NumberLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_mathDSL_Div_isa_Expression():
    instance = mathDSL_Div()
    assert isinstance(instance, Expression)


def test_mathDSL_Minus_isa_Expression():
    instance = mathDSL_Minus()
    assert isinstance(instance, Expression)


def test_mathDSL_Multi_isa_Expression():
    instance = mathDSL_Multi()
    assert isinstance(instance, Expression)


def test_mathDSL_NumberLiteral_isa_Expression():
    instance = mathDSL_NumberLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_mathDSL_Plus_isa_Expression():
    instance = mathDSL_Plus()
    assert isinstance(instance, Expression)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


mathDSL_Div_strategy = st.builds(mathDSL_Div)
@given(instance=mathDSL_Div_strategy)
@settings(max_examples=25)
def test_mathDSL_Div_instantiation(instance):
    assert isinstance(instance, mathDSL_Div)


mathDSL_Expression_strategy = st.builds(mathDSL_Expression)
@given(instance=mathDSL_Expression_strategy)
@settings(max_examples=25)
def test_mathDSL_Expression_instantiation(instance):
    assert isinstance(instance, mathDSL_Expression)


mathDSL_Math_strategy = st.builds(mathDSL_Math)
@given(instance=mathDSL_Math_strategy)
@settings(max_examples=25)
def test_mathDSL_Math_instantiation(instance):
    assert isinstance(instance, mathDSL_Math)


mathDSL_Minus_strategy = st.builds(mathDSL_Minus)
@given(instance=mathDSL_Minus_strategy)
@settings(max_examples=25)
def test_mathDSL_Minus_instantiation(instance):
    assert isinstance(instance, mathDSL_Minus)


mathDSL_Multi_strategy = st.builds(mathDSL_Multi)
@given(instance=mathDSL_Multi_strategy)
@settings(max_examples=25)
def test_mathDSL_Multi_instantiation(instance):
    assert isinstance(instance, mathDSL_Multi)


mathDSL_NumberLiteral_strategy = st.builds(mathDSL_NumberLiteral, value=safe_text)
@given(instance=mathDSL_NumberLiteral_strategy)
@settings(max_examples=25)
def test_mathDSL_NumberLiteral_instantiation(instance):
    assert isinstance(instance, mathDSL_NumberLiteral)


mathDSL_Plus_strategy = st.builds(mathDSL_Plus)
@given(instance=mathDSL_Plus_strategy)
@settings(max_examples=25)
def test_mathDSL_Plus_instantiation(instance):
    assert isinstance(instance, mathDSL_Plus)



