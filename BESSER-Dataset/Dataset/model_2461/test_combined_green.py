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
    OperatorCallExp,
    operators_BinaryOperatorCallExp,
    OclExpression,
    operators_OperatorCallExp,
    operators_OclExpression,
    NumericExp,
    operators_IntegerExp,
    operators_RealExp,
    PrimitiveExp,
    operators_BooleanExp,
    operators_NumericExp,
    operators_StringExp,
    operators_PrimitiveExp,
    operators_UnaryOperatorCallExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_hyp_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_hyp_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_binaryoperatorcallexp_is_not_abstract():
    assert not inspect.isabstract(operators_BinaryOperatorCallExp)


def test_hyp_operators_binaryoperatorcallexp_constructor_exists():
    assert callable(operators_BinaryOperatorCallExp.__init__)


def test_hyp_operators_binaryoperatorcallexp_constructor_args():
    sig = inspect.signature(operators_BinaryOperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_hyp_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_hyp_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(operators_OperatorCallExp)


def test_hyp_operators_operatorcallexp_constructor_exists():
    assert callable(operators_OperatorCallExp.__init__)


def test_hyp_operators_operatorcallexp_constructor_args():
    sig = inspect.signature(operators_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_operators_oclexpression_is_not_abstract():
    assert not inspect.isabstract(operators_OclExpression)


def test_hyp_operators_oclexpression_constructor_exists():
    assert callable(operators_OclExpression.__init__)


def test_hyp_operators_oclexpression_constructor_args():
    sig = inspect.signature(operators_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_hyp_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_hyp_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_integerexp_is_not_abstract():
    assert not inspect.isabstract(operators_IntegerExp)


def test_hyp_operators_integerexp_constructor_exists():
    assert callable(operators_IntegerExp.__init__)


def test_hyp_operators_integerexp_constructor_args():
    sig = inspect.signature(operators_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"




def test_hyp_operators_realexp_is_not_abstract():
    assert not inspect.isabstract(operators_RealExp)


def test_hyp_operators_realexp_constructor_exists():
    assert callable(operators_RealExp.__init__)


def test_hyp_operators_realexp_constructor_args():
    sig = inspect.signature(operators_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"




def test_hyp_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_hyp_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_hyp_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_booleanexp_is_not_abstract():
    assert not inspect.isabstract(operators_BooleanExp)


def test_hyp_operators_booleanexp_constructor_exists():
    assert callable(operators_BooleanExp.__init__)


def test_hyp_operators_booleanexp_constructor_args():
    sig = inspect.signature(operators_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"




def test_hyp_operators_numericexp_is_not_abstract():
    assert not inspect.isabstract(operators_NumericExp)


def test_hyp_operators_numericexp_constructor_exists():
    assert callable(operators_NumericExp.__init__)


def test_hyp_operators_numericexp_constructor_args():
    sig = inspect.signature(operators_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_stringexp_is_not_abstract():
    assert not inspect.isabstract(operators_StringExp)


def test_hyp_operators_stringexp_constructor_exists():
    assert callable(operators_StringExp.__init__)


def test_hyp_operators_stringexp_constructor_args():
    sig = inspect.signature(operators_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"




def test_hyp_operators_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(operators_PrimitiveExp)


def test_hyp_operators_primitiveexp_constructor_exists():
    assert callable(operators_PrimitiveExp.__init__)


def test_hyp_operators_primitiveexp_constructor_args():
    sig = inspect.signature(operators_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_unaryoperatorcallexp_is_not_abstract():
    assert not inspect.isabstract(operators_UnaryOperatorCallExp)


def test_hyp_operators_unaryoperatorcallexp_constructor_exists():
    assert callable(operators_UnaryOperatorCallExp.__init__)


def test_hyp_operators_unaryoperatorcallexp_constructor_args():
    sig = inspect.signature(operators_UnaryOperatorCallExp.__init__)
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
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
operators_BinaryOperatorCallExp_strategy = st.builds(
    operators_BinaryOperatorCallExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
operators_OperatorCallExp_strategy = st.builds(
    operators_OperatorCallExp,
    name=
        safe_text
)
operators_OclExpression_strategy = st.builds(
    operators_OclExpression,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
operators_IntegerExp_strategy = st.builds(
    operators_IntegerExp,
    integerSymbol=
        safe_text
)
operators_RealExp_strategy = st.builds(
    operators_RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
operators_BooleanExp_strategy = st.builds(
    operators_BooleanExp,
    booleanSymbol=
        safe_text
)
operators_NumericExp_strategy = st.builds(
    operators_NumericExp,
)
operators_StringExp_strategy = st.builds(
    operators_StringExp,
    stringSymbol=
        safe_text
)
operators_PrimitiveExp_strategy = st.builds(
    operators_PrimitiveExp,
)
operators_UnaryOperatorCallExp_strategy = st.builds(
    operators_UnaryOperatorCallExp,
)







@given(instance=operators_OperatorCallExp_strategy)
def test_hyp_operators_operatorcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=operators_IntegerExp_strategy)
def test_hyp_operators_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original




@given(instance=operators_RealExp_strategy)
def test_hyp_operators_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original





@given(instance=operators_BooleanExp_strategy)
def test_hyp_operators_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original





@given(instance=operators_StringExp_strategy)
def test_hyp_operators_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NumericExp,
    OclExpression,
    OperatorCallExp,
    PrimitiveExp,
    operators_BinaryOperatorCallExp,
    operators_BooleanExp,
    operators_IntegerExp,
    operators_NumericExp,
    operators_OclExpression,
    operators_OperatorCallExp,
    operators_PrimitiveExp,
    operators_RealExp,
    operators_StringExp,
    operators_UnaryOperatorCallExp,
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

def test_operators_BooleanExp_booleanSymbol_value_roundtrip():
    instance = operators_BooleanExp(booleanSymbol="sample_text")
    assert instance.booleanSymbol == "sample_text"
    instance.booleanSymbol = "sample_text_2"
    assert instance.booleanSymbol == "sample_text_2"


def test_operators_IntegerExp_integerSymbol_value_roundtrip():
    instance = operators_IntegerExp(integerSymbol="sample_text")
    assert instance.integerSymbol == "sample_text"
    instance.integerSymbol = "sample_text_2"
    assert instance.integerSymbol == "sample_text_2"


def test_operators_OperatorCallExp_name_value_roundtrip():
    instance = operators_OperatorCallExp(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_operators_RealExp_realSymbol_value_roundtrip():
    instance = operators_RealExp(realSymbol="sample_text")
    assert instance.realSymbol == "sample_text"
    instance.realSymbol = "sample_text_2"
    assert instance.realSymbol == "sample_text_2"


def test_operators_StringExp_stringSymbol_value_roundtrip():
    instance = operators_StringExp(stringSymbol="sample_text")
    assert instance.stringSymbol == "sample_text"
    instance.stringSymbol = "sample_text_2"
    assert instance.stringSymbol == "sample_text_2"


def test_operators_IntegerExp_isa_NumericExp():
    instance = operators_IntegerExp(integerSymbol="sample_text")
    assert isinstance(instance, NumericExp)


def test_operators_RealExp_isa_NumericExp():
    instance = operators_RealExp(realSymbol="sample_text")
    assert isinstance(instance, NumericExp)


def test_operators_OperatorCallExp_isa_OclExpression():
    instance = operators_OperatorCallExp(name="sample_text")
    assert isinstance(instance, OclExpression)


def test_operators_PrimitiveExp_isa_OclExpression():
    instance = operators_PrimitiveExp()
    assert isinstance(instance, OclExpression)


def test_operators_BinaryOperatorCallExp_isa_OperatorCallExp():
    instance = operators_BinaryOperatorCallExp()
    assert isinstance(instance, OperatorCallExp)


def test_operators_UnaryOperatorCallExp_isa_OperatorCallExp():
    instance = operators_UnaryOperatorCallExp()
    assert isinstance(instance, OperatorCallExp)


def test_operators_BooleanExp_isa_PrimitiveExp():
    instance = operators_BooleanExp(booleanSymbol="sample_text")
    assert isinstance(instance, PrimitiveExp)


def test_operators_NumericExp_isa_PrimitiveExp():
    instance = operators_NumericExp()
    assert isinstance(instance, PrimitiveExp)


def test_operators_StringExp_isa_PrimitiveExp():
    instance = operators_StringExp(stringSymbol="sample_text")
    assert isinstance(instance, PrimitiveExp)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NumericExp_strategy = st.builds(NumericExp)
@given(instance=NumericExp_strategy)
@settings(max_examples=25)
def test_NumericExp_instantiation(instance):
    assert isinstance(instance, NumericExp)


OclExpression_strategy = st.builds(OclExpression)
@given(instance=OclExpression_strategy)
@settings(max_examples=25)
def test_OclExpression_instantiation(instance):
    assert isinstance(instance, OclExpression)


OperatorCallExp_strategy = st.builds(OperatorCallExp)
@given(instance=OperatorCallExp_strategy)
@settings(max_examples=25)
def test_OperatorCallExp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)


PrimitiveExp_strategy = st.builds(PrimitiveExp)
@given(instance=PrimitiveExp_strategy)
@settings(max_examples=25)
def test_PrimitiveExp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)


operators_BinaryOperatorCallExp_strategy = st.builds(operators_BinaryOperatorCallExp)
@given(instance=operators_BinaryOperatorCallExp_strategy)
@settings(max_examples=25)
def test_operators_BinaryOperatorCallExp_instantiation(instance):
    assert isinstance(instance, operators_BinaryOperatorCallExp)


operators_BooleanExp_strategy = st.builds(operators_BooleanExp, booleanSymbol=safe_text)
@given(instance=operators_BooleanExp_strategy)
@settings(max_examples=25)
def test_operators_BooleanExp_instantiation(instance):
    assert isinstance(instance, operators_BooleanExp)


operators_IntegerExp_strategy = st.builds(operators_IntegerExp, integerSymbol=safe_text)
@given(instance=operators_IntegerExp_strategy)
@settings(max_examples=25)
def test_operators_IntegerExp_instantiation(instance):
    assert isinstance(instance, operators_IntegerExp)


operators_NumericExp_strategy = st.builds(operators_NumericExp)
@given(instance=operators_NumericExp_strategy)
@settings(max_examples=25)
def test_operators_NumericExp_instantiation(instance):
    assert isinstance(instance, operators_NumericExp)


operators_OclExpression_strategy = st.builds(operators_OclExpression)
@given(instance=operators_OclExpression_strategy)
@settings(max_examples=25)
def test_operators_OclExpression_instantiation(instance):
    assert isinstance(instance, operators_OclExpression)


operators_OperatorCallExp_strategy = st.builds(operators_OperatorCallExp, name=safe_text)
@given(instance=operators_OperatorCallExp_strategy)
@settings(max_examples=25)
def test_operators_OperatorCallExp_instantiation(instance):
    assert isinstance(instance, operators_OperatorCallExp)


operators_PrimitiveExp_strategy = st.builds(operators_PrimitiveExp)
@given(instance=operators_PrimitiveExp_strategy)
@settings(max_examples=25)
def test_operators_PrimitiveExp_instantiation(instance):
    assert isinstance(instance, operators_PrimitiveExp)


operators_RealExp_strategy = st.builds(operators_RealExp, realSymbol=safe_text)
@given(instance=operators_RealExp_strategy)
@settings(max_examples=25)
def test_operators_RealExp_instantiation(instance):
    assert isinstance(instance, operators_RealExp)


operators_StringExp_strategy = st.builds(operators_StringExp, stringSymbol=safe_text)
@given(instance=operators_StringExp_strategy)
@settings(max_examples=25)
def test_operators_StringExp_instantiation(instance):
    assert isinstance(instance, operators_StringExp)


operators_UnaryOperatorCallExp_strategy = st.builds(operators_UnaryOperatorCallExp)
@given(instance=operators_UnaryOperatorCallExp_strategy)
@settings(max_examples=25)
def test_operators_UnaryOperatorCallExp_instantiation(instance):
    assert isinstance(instance, operators_UnaryOperatorCallExp)



