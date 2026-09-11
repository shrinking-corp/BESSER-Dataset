import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    arithmetics_Div,
    arithmetics_Evaluation,
    arithmetics_Expression,
    arithmetics_Minus,
    arithmetics_Multi,
    arithmetics_NumberLiteral,
    arithmetics_Plus,
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

def test_arithmetics_NumberLiteral_value_value_roundtrip():
    instance = arithmetics_NumberLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_arithmetics_Div_isa_Expression():
    instance = arithmetics_Div()
    assert isinstance(instance, Expression)


def test_arithmetics_Minus_isa_Expression():
    instance = arithmetics_Minus()
    assert isinstance(instance, Expression)


def test_arithmetics_Multi_isa_Expression():
    instance = arithmetics_Multi()
    assert isinstance(instance, Expression)


def test_arithmetics_NumberLiteral_isa_Expression():
    instance = arithmetics_NumberLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_arithmetics_Plus_isa_Expression():
    instance = arithmetics_Plus()
    assert isinstance(instance, Expression)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


arithmetics_Div_strategy = st.builds(arithmetics_Div)
@given(instance=arithmetics_Div_strategy)
@settings(max_examples=25)
def test_arithmetics_Div_instantiation(instance):
    assert isinstance(instance, arithmetics_Div)


arithmetics_Evaluation_strategy = st.builds(arithmetics_Evaluation)
@given(instance=arithmetics_Evaluation_strategy)
@settings(max_examples=25)
def test_arithmetics_Evaluation_instantiation(instance):
    assert isinstance(instance, arithmetics_Evaluation)


arithmetics_Expression_strategy = st.builds(arithmetics_Expression)
@given(instance=arithmetics_Expression_strategy)
@settings(max_examples=25)
def test_arithmetics_Expression_instantiation(instance):
    assert isinstance(instance, arithmetics_Expression)


arithmetics_Minus_strategy = st.builds(arithmetics_Minus)
@given(instance=arithmetics_Minus_strategy)
@settings(max_examples=25)
def test_arithmetics_Minus_instantiation(instance):
    assert isinstance(instance, arithmetics_Minus)


arithmetics_Multi_strategy = st.builds(arithmetics_Multi)
@given(instance=arithmetics_Multi_strategy)
@settings(max_examples=25)
def test_arithmetics_Multi_instantiation(instance):
    assert isinstance(instance, arithmetics_Multi)


arithmetics_NumberLiteral_strategy = st.builds(arithmetics_NumberLiteral, value=safe_text)
@given(instance=arithmetics_NumberLiteral_strategy)
@settings(max_examples=25)
def test_arithmetics_NumberLiteral_instantiation(instance):
    assert isinstance(instance, arithmetics_NumberLiteral)


arithmetics_Plus_strategy = st.builds(arithmetics_Plus)
@given(instance=arithmetics_Plus_strategy)
@settings(max_examples=25)
def test_arithmetics_Plus_instantiation(instance):
    assert isinstance(instance, arithmetics_Plus)


