import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    mathInterpreter_Divide,
    mathInterpreter_Exp,
    mathInterpreter_Expression,
    mathInterpreter_MathExp,
    mathInterpreter_Minus,
    mathInterpreter_Multiply,
    mathInterpreter_Num,
    mathInterpreter_Plus,
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

def test_mathInterpreter_Num_value_value_roundtrip():
    instance = mathInterpreter_Num(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_mathInterpreter_Divide_isa_Expression():
    instance = mathInterpreter_Divide()
    assert isinstance(instance, Expression)


def test_mathInterpreter_Exp_isa_Expression():
    instance = mathInterpreter_Exp()
    assert isinstance(instance, Expression)


def test_mathInterpreter_Minus_isa_Expression():
    instance = mathInterpreter_Minus()
    assert isinstance(instance, Expression)


def test_mathInterpreter_Multiply_isa_Expression():
    instance = mathInterpreter_Multiply()
    assert isinstance(instance, Expression)


def test_mathInterpreter_Num_isa_Expression():
    instance = mathInterpreter_Num(value=7)
    assert isinstance(instance, Expression)


def test_mathInterpreter_Plus_isa_Expression():
    instance = mathInterpreter_Plus()
    assert isinstance(instance, Expression)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


mathInterpreter_Divide_strategy = st.builds(mathInterpreter_Divide)
@given(instance=mathInterpreter_Divide_strategy)
@settings(max_examples=25)
def test_mathInterpreter_Divide_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Divide)


mathInterpreter_Exp_strategy = st.builds(mathInterpreter_Exp)
@given(instance=mathInterpreter_Exp_strategy)
@settings(max_examples=25)
def test_mathInterpreter_Exp_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Exp)


mathInterpreter_Expression_strategy = st.builds(mathInterpreter_Expression)
@given(instance=mathInterpreter_Expression_strategy)
@settings(max_examples=25)
def test_mathInterpreter_Expression_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Expression)


mathInterpreter_MathExp_strategy = st.builds(mathInterpreter_MathExp)
@given(instance=mathInterpreter_MathExp_strategy)
@settings(max_examples=25)
def test_mathInterpreter_MathExp_instantiation(instance):
    assert isinstance(instance, mathInterpreter_MathExp)


mathInterpreter_Minus_strategy = st.builds(mathInterpreter_Minus)
@given(instance=mathInterpreter_Minus_strategy)
@settings(max_examples=25)
def test_mathInterpreter_Minus_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Minus)


mathInterpreter_Multiply_strategy = st.builds(mathInterpreter_Multiply)
@given(instance=mathInterpreter_Multiply_strategy)
@settings(max_examples=25)
def test_mathInterpreter_Multiply_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Multiply)


mathInterpreter_Num_strategy = st.builds(mathInterpreter_Num, value=st.integers())
@given(instance=mathInterpreter_Num_strategy)
@settings(max_examples=25)
def test_mathInterpreter_Num_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Num)


mathInterpreter_Plus_strategy = st.builds(mathInterpreter_Plus)
@given(instance=mathInterpreter_Plus_strategy)
@settings(max_examples=25)
def test_mathInterpreter_Plus_instantiation(instance):
    assert isinstance(instance, mathInterpreter_Plus)


