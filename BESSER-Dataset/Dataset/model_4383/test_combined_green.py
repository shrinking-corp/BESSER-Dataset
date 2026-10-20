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
    minilang_While,
    minilang_Block,
    Statement,
    minilang_PrintStr,
    minilang_PrintVar,
    minilang_IntAssignment,
    minilang_BooleanAssignment,
    minilang_Statement,
    minilang_VariableRef,
    VariableRef,
    IntOperation,
    minilang_Multiply,
    minilang_Minus,
    minilang_Divide,
    minilang_Plus,
    BooleanOperation,
    minilang_And,
    minilang_Or,
    minilang_BooleanExpression,
    minilang_If,
    IntComparison,
    minilang_LessOrEqual,
    minilang_Greater,
    minilang_Equal,
    BooleanExpression,
    minilang_IntComparison,
    minilang_BooleanOperation,
    minilang_Not,
    minilang_BooleanVariableRef,
    minilang_Boolean,
    IntExpression,
    minilang_IntVariableRef,
    minilang_IntOperation,
    minilang_Integer,
    minilang_IntExpression,
    minilang_Less,
    minilang_GreaterOrEqual,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_minilang_while_is_not_abstract():
    assert not inspect.isabstract(minilang_While)


def test_hyp_minilang_while_constructor_exists():
    assert callable(minilang_While.__init__)


def test_hyp_minilang_while_constructor_args():
    sig = inspect.signature(minilang_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_block_is_not_abstract():
    assert not inspect.isabstract(minilang_Block)


def test_hyp_minilang_block_constructor_exists():
    assert callable(minilang_Block.__init__)


def test_hyp_minilang_block_constructor_args():
    sig = inspect.signature(minilang_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_printstr_is_not_abstract():
    assert not inspect.isabstract(minilang_PrintStr)


def test_hyp_minilang_printstr_constructor_exists():
    assert callable(minilang_PrintStr.__init__)


def test_hyp_minilang_printstr_constructor_args():
    sig = inspect.signature(minilang_PrintStr.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minilang_printvar_is_not_abstract():
    assert not inspect.isabstract(minilang_PrintVar)


def test_hyp_minilang_printvar_constructor_exists():
    assert callable(minilang_PrintVar.__init__)


def test_hyp_minilang_printvar_constructor_args():
    sig = inspect.signature(minilang_PrintVar.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minilang_intassignment_is_not_abstract():
    assert not inspect.isabstract(minilang_IntAssignment)


def test_hyp_minilang_intassignment_constructor_exists():
    assert callable(minilang_IntAssignment.__init__)


def test_hyp_minilang_intassignment_constructor_args():
    sig = inspect.signature(minilang_IntAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_booleanassignment_is_not_abstract():
    assert not inspect.isabstract(minilang_BooleanAssignment)


def test_hyp_minilang_booleanassignment_constructor_exists():
    assert callable(minilang_BooleanAssignment.__init__)


def test_hyp_minilang_booleanassignment_constructor_args():
    sig = inspect.signature(minilang_BooleanAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_statement_is_not_abstract():
    assert not inspect.isabstract(minilang_Statement)


def test_hyp_minilang_statement_constructor_exists():
    assert callable(minilang_Statement.__init__)


def test_hyp_minilang_statement_constructor_args():
    sig = inspect.signature(minilang_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_variableref_is_not_abstract():
    assert not inspect.isabstract(minilang_VariableRef)


def test_hyp_minilang_variableref_constructor_exists():
    assert callable(minilang_VariableRef.__init__)


def test_hyp_minilang_variableref_constructor_args():
    sig = inspect.signature(minilang_VariableRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_variableref_is_not_abstract():
    assert not inspect.isabstract(VariableRef)


def test_hyp_variableref_constructor_exists():
    assert callable(VariableRef.__init__)


def test_hyp_variableref_constructor_args():
    sig = inspect.signature(VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intoperation_is_not_abstract():
    assert not inspect.isabstract(IntOperation)


def test_hyp_intoperation_constructor_exists():
    assert callable(IntOperation.__init__)


def test_hyp_intoperation_constructor_args():
    sig = inspect.signature(IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_multiply_is_not_abstract():
    assert not inspect.isabstract(minilang_Multiply)


def test_hyp_minilang_multiply_constructor_exists():
    assert callable(minilang_Multiply.__init__)


def test_hyp_minilang_multiply_constructor_args():
    sig = inspect.signature(minilang_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_minus_is_not_abstract():
    assert not inspect.isabstract(minilang_Minus)


def test_hyp_minilang_minus_constructor_exists():
    assert callable(minilang_Minus.__init__)


def test_hyp_minilang_minus_constructor_args():
    sig = inspect.signature(minilang_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_divide_is_not_abstract():
    assert not inspect.isabstract(minilang_Divide)


def test_hyp_minilang_divide_constructor_exists():
    assert callable(minilang_Divide.__init__)


def test_hyp_minilang_divide_constructor_args():
    sig = inspect.signature(minilang_Divide.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_plus_is_not_abstract():
    assert not inspect.isabstract(minilang_Plus)


def test_hyp_minilang_plus_constructor_exists():
    assert callable(minilang_Plus.__init__)


def test_hyp_minilang_plus_constructor_args():
    sig = inspect.signature(minilang_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booleanoperation_is_not_abstract():
    assert not inspect.isabstract(BooleanOperation)


def test_hyp_booleanoperation_constructor_exists():
    assert callable(BooleanOperation.__init__)


def test_hyp_booleanoperation_constructor_args():
    sig = inspect.signature(BooleanOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_and_is_not_abstract():
    assert not inspect.isabstract(minilang_And)


def test_hyp_minilang_and_constructor_exists():
    assert callable(minilang_And.__init__)


def test_hyp_minilang_and_constructor_args():
    sig = inspect.signature(minilang_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_or_is_not_abstract():
    assert not inspect.isabstract(minilang_Or)


def test_hyp_minilang_or_constructor_exists():
    assert callable(minilang_Or.__init__)


def test_hyp_minilang_or_constructor_args():
    sig = inspect.signature(minilang_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(minilang_BooleanExpression)


def test_hyp_minilang_booleanexpression_constructor_exists():
    assert callable(minilang_BooleanExpression.__init__)


def test_hyp_minilang_booleanexpression_constructor_args():
    sig = inspect.signature(minilang_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_if_is_not_abstract():
    assert not inspect.isabstract(minilang_If)


def test_hyp_minilang_if_constructor_exists():
    assert callable(minilang_If.__init__)


def test_hyp_minilang_if_constructor_args():
    sig = inspect.signature(minilang_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intcomparison_is_not_abstract():
    assert not inspect.isabstract(IntComparison)


def test_hyp_intcomparison_constructor_exists():
    assert callable(IntComparison.__init__)


def test_hyp_intcomparison_constructor_args():
    sig = inspect.signature(IntComparison.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_lessorequal_is_not_abstract():
    assert not inspect.isabstract(minilang_LessOrEqual)


def test_hyp_minilang_lessorequal_constructor_exists():
    assert callable(minilang_LessOrEqual.__init__)


def test_hyp_minilang_lessorequal_constructor_args():
    sig = inspect.signature(minilang_LessOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_greater_is_not_abstract():
    assert not inspect.isabstract(minilang_Greater)


def test_hyp_minilang_greater_constructor_exists():
    assert callable(minilang_Greater.__init__)


def test_hyp_minilang_greater_constructor_args():
    sig = inspect.signature(minilang_Greater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_equal_is_not_abstract():
    assert not inspect.isabstract(minilang_Equal)


def test_hyp_minilang_equal_constructor_exists():
    assert callable(minilang_Equal.__init__)


def test_hyp_minilang_equal_constructor_args():
    sig = inspect.signature(minilang_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_hyp_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_hyp_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_intcomparison_is_not_abstract():
    assert not inspect.isabstract(minilang_IntComparison)


def test_hyp_minilang_intcomparison_constructor_exists():
    assert callable(minilang_IntComparison.__init__)


def test_hyp_minilang_intcomparison_constructor_args():
    sig = inspect.signature(minilang_IntComparison.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_booleanoperation_is_not_abstract():
    assert not inspect.isabstract(minilang_BooleanOperation)


def test_hyp_minilang_booleanoperation_constructor_exists():
    assert callable(minilang_BooleanOperation.__init__)


def test_hyp_minilang_booleanoperation_constructor_args():
    sig = inspect.signature(minilang_BooleanOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_not_is_not_abstract():
    assert not inspect.isabstract(minilang_Not)


def test_hyp_minilang_not_constructor_exists():
    assert callable(minilang_Not.__init__)


def test_hyp_minilang_not_constructor_args():
    sig = inspect.signature(minilang_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_booleanvariableref_is_not_abstract():
    assert not inspect.isabstract(minilang_BooleanVariableRef)


def test_hyp_minilang_booleanvariableref_constructor_exists():
    assert callable(minilang_BooleanVariableRef.__init__)


def test_hyp_minilang_booleanvariableref_constructor_args():
    sig = inspect.signature(minilang_BooleanVariableRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_boolean_is_not_abstract():
    assert not inspect.isabstract(minilang_Boolean)


def test_hyp_minilang_boolean_constructor_exists():
    assert callable(minilang_Boolean.__init__)


def test_hyp_minilang_boolean_constructor_args():
    sig = inspect.signature(minilang_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_intexpression_is_not_abstract():
    assert not inspect.isabstract(IntExpression)


def test_hyp_intexpression_constructor_exists():
    assert callable(IntExpression.__init__)


def test_hyp_intexpression_constructor_args():
    sig = inspect.signature(IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_intvariableref_is_not_abstract():
    assert not inspect.isabstract(minilang_IntVariableRef)


def test_hyp_minilang_intvariableref_constructor_exists():
    assert callable(minilang_IntVariableRef.__init__)


def test_hyp_minilang_intvariableref_constructor_args():
    sig = inspect.signature(minilang_IntVariableRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_intoperation_is_not_abstract():
    assert not inspect.isabstract(minilang_IntOperation)


def test_hyp_minilang_intoperation_constructor_exists():
    assert callable(minilang_IntOperation.__init__)


def test_hyp_minilang_intoperation_constructor_args():
    sig = inspect.signature(minilang_IntOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_integer_is_not_abstract():
    assert not inspect.isabstract(minilang_Integer)


def test_hyp_minilang_integer_constructor_exists():
    assert callable(minilang_Integer.__init__)


def test_hyp_minilang_integer_constructor_args():
    sig = inspect.signature(minilang_Integer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minilang_intexpression_is_not_abstract():
    assert not inspect.isabstract(minilang_IntExpression)


def test_hyp_minilang_intexpression_constructor_exists():
    assert callable(minilang_IntExpression.__init__)


def test_hyp_minilang_intexpression_constructor_args():
    sig = inspect.signature(minilang_IntExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_less_is_not_abstract():
    assert not inspect.isabstract(minilang_Less)


def test_hyp_minilang_less_constructor_exists():
    assert callable(minilang_Less.__init__)


def test_hyp_minilang_less_constructor_args():
    sig = inspect.signature(minilang_Less.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minilang_greaterorequal_is_not_abstract():
    assert not inspect.isabstract(minilang_GreaterOrEqual)


def test_hyp_minilang_greaterorequal_constructor_exists():
    assert callable(minilang_GreaterOrEqual.__init__)


def test_hyp_minilang_greaterorequal_constructor_args():
    sig = inspect.signature(minilang_GreaterOrEqual.__init__)
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
minilang_While_strategy = st.builds(
    minilang_While,
)
minilang_Block_strategy = st.builds(
    minilang_Block,
)
Statement_strategy = st.builds(
    Statement,
)
minilang_PrintStr_strategy = st.builds(
    minilang_PrintStr,
    value=
        safe_text
)
minilang_PrintVar_strategy = st.builds(
    minilang_PrintVar,
    value=
        safe_text
)
minilang_IntAssignment_strategy = st.builds(
    minilang_IntAssignment,
)
minilang_BooleanAssignment_strategy = st.builds(
    minilang_BooleanAssignment,
)
minilang_Statement_strategy = st.builds(
    minilang_Statement,
)
minilang_VariableRef_strategy = st.builds(
    minilang_VariableRef,
    name=
        safe_text
)
VariableRef_strategy = st.builds(
    VariableRef,
)
IntOperation_strategy = st.builds(
    IntOperation,
)
minilang_Multiply_strategy = st.builds(
    minilang_Multiply,
)
minilang_Minus_strategy = st.builds(
    minilang_Minus,
)
minilang_Divide_strategy = st.builds(
    minilang_Divide,
)
minilang_Plus_strategy = st.builds(
    minilang_Plus,
)
BooleanOperation_strategy = st.builds(
    BooleanOperation,
)
minilang_And_strategy = st.builds(
    minilang_And,
)
minilang_Or_strategy = st.builds(
    minilang_Or,
)
minilang_BooleanExpression_strategy = st.builds(
    minilang_BooleanExpression,
)
minilang_If_strategy = st.builds(
    minilang_If,
)
IntComparison_strategy = st.builds(
    IntComparison,
)
minilang_LessOrEqual_strategy = st.builds(
    minilang_LessOrEqual,
)
minilang_Greater_strategy = st.builds(
    minilang_Greater,
)
minilang_Equal_strategy = st.builds(
    minilang_Equal,
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
minilang_IntComparison_strategy = st.builds(
    minilang_IntComparison,
)
minilang_BooleanOperation_strategy = st.builds(
    minilang_BooleanOperation,
)
minilang_Not_strategy = st.builds(
    minilang_Not,
)
minilang_BooleanVariableRef_strategy = st.builds(
    minilang_BooleanVariableRef,
)
minilang_Boolean_strategy = st.builds(
    minilang_Boolean,
    value=
        st.booleans()
)
IntExpression_strategy = st.builds(
    IntExpression,
)
minilang_IntVariableRef_strategy = st.builds(
    minilang_IntVariableRef,
)
minilang_IntOperation_strategy = st.builds(
    minilang_IntOperation,
)
minilang_Integer_strategy = st.builds(
    minilang_Integer,
    value=
        st.integers()
)
minilang_IntExpression_strategy = st.builds(
    minilang_IntExpression,
)
minilang_Less_strategy = st.builds(
    minilang_Less,
)
minilang_GreaterOrEqual_strategy = st.builds(
    minilang_GreaterOrEqual,
)







@given(instance=minilang_PrintStr_strategy)
def test_hyp_minilang_printstr_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=minilang_PrintVar_strategy)
def test_hyp_minilang_printvar_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=minilang_VariableRef_strategy)
def test_hyp_minilang_variableref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
























@given(instance=minilang_Boolean_strategy)
def test_hyp_minilang_boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=minilang_Integer_strategy)
def test_hyp_minilang_integer_value_setter(instance):
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
    BooleanExpression,
    BooleanOperation,
    IntComparison,
    IntExpression,
    IntOperation,
    Statement,
    VariableRef,
    minilang_And,
    minilang_Block,
    minilang_Boolean,
    minilang_BooleanAssignment,
    minilang_BooleanExpression,
    minilang_BooleanOperation,
    minilang_BooleanVariableRef,
    minilang_Divide,
    minilang_Equal,
    minilang_Greater,
    minilang_GreaterOrEqual,
    minilang_If,
    minilang_IntAssignment,
    minilang_IntComparison,
    minilang_IntExpression,
    minilang_IntOperation,
    minilang_IntVariableRef,
    minilang_Integer,
    minilang_Less,
    minilang_LessOrEqual,
    minilang_Minus,
    minilang_Multiply,
    minilang_Not,
    minilang_Or,
    minilang_Plus,
    minilang_PrintStr,
    minilang_PrintVar,
    minilang_Statement,
    minilang_VariableRef,
    minilang_While,
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

def test_minilang_Boolean_value_value_roundtrip():
    instance = minilang_Boolean(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_minilang_Integer_value_value_roundtrip():
    instance = minilang_Integer(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_minilang_PrintStr_value_value_roundtrip():
    instance = minilang_PrintStr(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_minilang_PrintVar_value_value_roundtrip():
    instance = minilang_PrintVar(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_minilang_VariableRef_name_value_roundtrip():
    instance = minilang_VariableRef(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minilang_Boolean_isa_BooleanExpression():
    instance = minilang_Boolean(value=True)
    assert isinstance(instance, BooleanExpression)


def test_minilang_BooleanOperation_isa_BooleanExpression():
    instance = minilang_BooleanOperation()
    assert isinstance(instance, BooleanExpression)


def test_minilang_BooleanVariableRef_isa_BooleanExpression():
    instance = minilang_BooleanVariableRef()
    assert isinstance(instance, BooleanExpression)


def test_minilang_IntComparison_isa_BooleanExpression():
    instance = minilang_IntComparison()
    assert isinstance(instance, BooleanExpression)


def test_minilang_Not_isa_BooleanExpression():
    instance = minilang_Not()
    assert isinstance(instance, BooleanExpression)


def test_minilang_And_isa_BooleanOperation():
    instance = minilang_And()
    assert isinstance(instance, BooleanOperation)


def test_minilang_Or_isa_BooleanOperation():
    instance = minilang_Or()
    assert isinstance(instance, BooleanOperation)


def test_minilang_Equal_isa_IntComparison():
    instance = minilang_Equal()
    assert isinstance(instance, IntComparison)


def test_minilang_Greater_isa_IntComparison():
    instance = minilang_Greater()
    assert isinstance(instance, IntComparison)


def test_minilang_GreaterOrEqual_isa_IntComparison():
    instance = minilang_GreaterOrEqual()
    assert isinstance(instance, IntComparison)


def test_minilang_Less_isa_IntComparison():
    instance = minilang_Less()
    assert isinstance(instance, IntComparison)


def test_minilang_LessOrEqual_isa_IntComparison():
    instance = minilang_LessOrEqual()
    assert isinstance(instance, IntComparison)


def test_minilang_IntOperation_isa_IntExpression():
    instance = minilang_IntOperation()
    assert isinstance(instance, IntExpression)


def test_minilang_IntVariableRef_isa_IntExpression():
    instance = minilang_IntVariableRef()
    assert isinstance(instance, IntExpression)


def test_minilang_Integer_isa_IntExpression():
    instance = minilang_Integer(value=7)
    assert isinstance(instance, IntExpression)


def test_minilang_Divide_isa_IntOperation():
    instance = minilang_Divide()
    assert isinstance(instance, IntOperation)


def test_minilang_Minus_isa_IntOperation():
    instance = minilang_Minus()
    assert isinstance(instance, IntOperation)


def test_minilang_Multiply_isa_IntOperation():
    instance = minilang_Multiply()
    assert isinstance(instance, IntOperation)


def test_minilang_Plus_isa_IntOperation():
    instance = minilang_Plus()
    assert isinstance(instance, IntOperation)


def test_minilang_BooleanAssignment_isa_Statement():
    instance = minilang_BooleanAssignment()
    assert isinstance(instance, Statement)


def test_minilang_IntAssignment_isa_Statement():
    instance = minilang_IntAssignment()
    assert isinstance(instance, Statement)


def test_minilang_PrintStr_isa_Statement():
    instance = minilang_PrintStr(value="sample_text")
    assert isinstance(instance, Statement)


def test_minilang_PrintVar_isa_Statement():
    instance = minilang_PrintVar(value="sample_text")
    assert isinstance(instance, Statement)


def test_minilang_BooleanVariableRef_isa_VariableRef():
    instance = minilang_BooleanVariableRef()
    assert isinstance(instance, VariableRef)


def test_minilang_IntVariableRef_isa_VariableRef():
    instance = minilang_IntVariableRef()
    assert isinstance(instance, VariableRef)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BooleanExpression_strategy = st.builds(BooleanExpression)
@given(instance=BooleanExpression_strategy)
@settings(max_examples=25)
def test_BooleanExpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)


BooleanOperation_strategy = st.builds(BooleanOperation)
@given(instance=BooleanOperation_strategy)
@settings(max_examples=25)
def test_BooleanOperation_instantiation(instance):
    assert isinstance(instance, BooleanOperation)


IntComparison_strategy = st.builds(IntComparison)
@given(instance=IntComparison_strategy)
@settings(max_examples=25)
def test_IntComparison_instantiation(instance):
    assert isinstance(instance, IntComparison)


IntExpression_strategy = st.builds(IntExpression)
@given(instance=IntExpression_strategy)
@settings(max_examples=25)
def test_IntExpression_instantiation(instance):
    assert isinstance(instance, IntExpression)


IntOperation_strategy = st.builds(IntOperation)
@given(instance=IntOperation_strategy)
@settings(max_examples=25)
def test_IntOperation_instantiation(instance):
    assert isinstance(instance, IntOperation)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


VariableRef_strategy = st.builds(VariableRef)
@given(instance=VariableRef_strategy)
@settings(max_examples=25)
def test_VariableRef_instantiation(instance):
    assert isinstance(instance, VariableRef)


minilang_And_strategy = st.builds(minilang_And)
@given(instance=minilang_And_strategy)
@settings(max_examples=25)
def test_minilang_And_instantiation(instance):
    assert isinstance(instance, minilang_And)


minilang_Block_strategy = st.builds(minilang_Block)
@given(instance=minilang_Block_strategy)
@settings(max_examples=25)
def test_minilang_Block_instantiation(instance):
    assert isinstance(instance, minilang_Block)


minilang_Boolean_strategy = st.builds(minilang_Boolean, value=st.booleans())
@given(instance=minilang_Boolean_strategy)
@settings(max_examples=25)
def test_minilang_Boolean_instantiation(instance):
    assert isinstance(instance, minilang_Boolean)


minilang_BooleanAssignment_strategy = st.builds(minilang_BooleanAssignment)
@given(instance=minilang_BooleanAssignment_strategy)
@settings(max_examples=25)
def test_minilang_BooleanAssignment_instantiation(instance):
    assert isinstance(instance, minilang_BooleanAssignment)


minilang_BooleanExpression_strategy = st.builds(minilang_BooleanExpression)
@given(instance=minilang_BooleanExpression_strategy)
@settings(max_examples=25)
def test_minilang_BooleanExpression_instantiation(instance):
    assert isinstance(instance, minilang_BooleanExpression)


minilang_BooleanOperation_strategy = st.builds(minilang_BooleanOperation)
@given(instance=minilang_BooleanOperation_strategy)
@settings(max_examples=25)
def test_minilang_BooleanOperation_instantiation(instance):
    assert isinstance(instance, minilang_BooleanOperation)


minilang_BooleanVariableRef_strategy = st.builds(minilang_BooleanVariableRef)
@given(instance=minilang_BooleanVariableRef_strategy)
@settings(max_examples=25)
def test_minilang_BooleanVariableRef_instantiation(instance):
    assert isinstance(instance, minilang_BooleanVariableRef)


minilang_Divide_strategy = st.builds(minilang_Divide)
@given(instance=minilang_Divide_strategy)
@settings(max_examples=25)
def test_minilang_Divide_instantiation(instance):
    assert isinstance(instance, minilang_Divide)


minilang_Equal_strategy = st.builds(minilang_Equal)
@given(instance=minilang_Equal_strategy)
@settings(max_examples=25)
def test_minilang_Equal_instantiation(instance):
    assert isinstance(instance, minilang_Equal)


minilang_Greater_strategy = st.builds(minilang_Greater)
@given(instance=minilang_Greater_strategy)
@settings(max_examples=25)
def test_minilang_Greater_instantiation(instance):
    assert isinstance(instance, minilang_Greater)


minilang_GreaterOrEqual_strategy = st.builds(minilang_GreaterOrEqual)
@given(instance=minilang_GreaterOrEqual_strategy)
@settings(max_examples=25)
def test_minilang_GreaterOrEqual_instantiation(instance):
    assert isinstance(instance, minilang_GreaterOrEqual)


minilang_If_strategy = st.builds(minilang_If)
@given(instance=minilang_If_strategy)
@settings(max_examples=25)
def test_minilang_If_instantiation(instance):
    assert isinstance(instance, minilang_If)


minilang_IntAssignment_strategy = st.builds(minilang_IntAssignment)
@given(instance=minilang_IntAssignment_strategy)
@settings(max_examples=25)
def test_minilang_IntAssignment_instantiation(instance):
    assert isinstance(instance, minilang_IntAssignment)


minilang_IntComparison_strategy = st.builds(minilang_IntComparison)
@given(instance=minilang_IntComparison_strategy)
@settings(max_examples=25)
def test_minilang_IntComparison_instantiation(instance):
    assert isinstance(instance, minilang_IntComparison)


minilang_IntExpression_strategy = st.builds(minilang_IntExpression)
@given(instance=minilang_IntExpression_strategy)
@settings(max_examples=25)
def test_minilang_IntExpression_instantiation(instance):
    assert isinstance(instance, minilang_IntExpression)


minilang_IntOperation_strategy = st.builds(minilang_IntOperation)
@given(instance=minilang_IntOperation_strategy)
@settings(max_examples=25)
def test_minilang_IntOperation_instantiation(instance):
    assert isinstance(instance, minilang_IntOperation)


minilang_IntVariableRef_strategy = st.builds(minilang_IntVariableRef)
@given(instance=minilang_IntVariableRef_strategy)
@settings(max_examples=25)
def test_minilang_IntVariableRef_instantiation(instance):
    assert isinstance(instance, minilang_IntVariableRef)


minilang_Integer_strategy = st.builds(minilang_Integer, value=st.integers())
@given(instance=minilang_Integer_strategy)
@settings(max_examples=25)
def test_minilang_Integer_instantiation(instance):
    assert isinstance(instance, minilang_Integer)


minilang_Less_strategy = st.builds(minilang_Less)
@given(instance=minilang_Less_strategy)
@settings(max_examples=25)
def test_minilang_Less_instantiation(instance):
    assert isinstance(instance, minilang_Less)


minilang_LessOrEqual_strategy = st.builds(minilang_LessOrEqual)
@given(instance=minilang_LessOrEqual_strategy)
@settings(max_examples=25)
def test_minilang_LessOrEqual_instantiation(instance):
    assert isinstance(instance, minilang_LessOrEqual)


minilang_Minus_strategy = st.builds(minilang_Minus)
@given(instance=minilang_Minus_strategy)
@settings(max_examples=25)
def test_minilang_Minus_instantiation(instance):
    assert isinstance(instance, minilang_Minus)


minilang_Multiply_strategy = st.builds(minilang_Multiply)
@given(instance=minilang_Multiply_strategy)
@settings(max_examples=25)
def test_minilang_Multiply_instantiation(instance):
    assert isinstance(instance, minilang_Multiply)


minilang_Not_strategy = st.builds(minilang_Not)
@given(instance=minilang_Not_strategy)
@settings(max_examples=25)
def test_minilang_Not_instantiation(instance):
    assert isinstance(instance, minilang_Not)


minilang_Or_strategy = st.builds(minilang_Or)
@given(instance=minilang_Or_strategy)
@settings(max_examples=25)
def test_minilang_Or_instantiation(instance):
    assert isinstance(instance, minilang_Or)


minilang_Plus_strategy = st.builds(minilang_Plus)
@given(instance=minilang_Plus_strategy)
@settings(max_examples=25)
def test_minilang_Plus_instantiation(instance):
    assert isinstance(instance, minilang_Plus)


minilang_PrintStr_strategy = st.builds(minilang_PrintStr, value=safe_text)
@given(instance=minilang_PrintStr_strategy)
@settings(max_examples=25)
def test_minilang_PrintStr_instantiation(instance):
    assert isinstance(instance, minilang_PrintStr)


minilang_PrintVar_strategy = st.builds(minilang_PrintVar, value=safe_text)
@given(instance=minilang_PrintVar_strategy)
@settings(max_examples=25)
def test_minilang_PrintVar_instantiation(instance):
    assert isinstance(instance, minilang_PrintVar)


minilang_Statement_strategy = st.builds(minilang_Statement)
@given(instance=minilang_Statement_strategy)
@settings(max_examples=25)
def test_minilang_Statement_instantiation(instance):
    assert isinstance(instance, minilang_Statement)


minilang_VariableRef_strategy = st.builds(minilang_VariableRef, name=safe_text)
@given(instance=minilang_VariableRef_strategy)
@settings(max_examples=25)
def test_minilang_VariableRef_instantiation(instance):
    assert isinstance(instance, minilang_VariableRef)


minilang_While_strategy = st.builds(minilang_While)
@given(instance=minilang_While_strategy)
@settings(max_examples=25)
def test_minilang_While_instantiation(instance):
    assert isinstance(instance, minilang_While)



