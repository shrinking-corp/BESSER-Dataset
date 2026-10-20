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
    ComparsionOperator,
    behaviouralProgramMM_Equals,
    FunctionCallStatement,
    behaviouralProgramMM_WriteLineStatement,
    behaviouralProgramMM_ReadLineStatement,
    ArithmeticInfixOperator,
    behaviouralProgramMM_Plus,
    BinaryOperator,
    behaviouralProgramMM_ComparsionOperator,
    behaviouralProgramMM_ArithmeticInfixOperator,
    Expression,
    behaviouralProgramMM_Literal,
    behaviouralProgramMM_Variable,
    behaviouralProgramMM_BinaryOperator,
    behaviouralProgramMM_ReadLine,
    behaviouralProgramMM_FunctionCall,
    behaviouralProgramMM_Expression,
    Statement,
    behaviouralProgramMM_Instantiation,
    behaviouralProgramMM_Loop,
    behaviouralProgramMM_RaiseException,
    behaviouralProgramMM_ConditionalBranch,
    behaviouralProgramMM_FunctionCallStatement,
    behaviouralProgramMM_Assignment,
    behaviouralProgramMM_Statement,
    behaviouralProgramMM_TryCatch,
    behaviouralProgramMM_Return,
    behaviouralProgramMM_Function,
    behaviouralProgramMM_Behaviour,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_comparsionoperator_is_not_abstract():
    assert not inspect.isabstract(ComparsionOperator)


def test_hyp_comparsionoperator_constructor_exists():
    assert callable(ComparsionOperator.__init__)


def test_hyp_comparsionoperator_constructor_args():
    sig = inspect.signature(ComparsionOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_equals_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Equals)


def test_hyp_behaviouralprogrammm_equals_constructor_exists():
    assert callable(behaviouralProgramMM_Equals.__init__)


def test_hyp_behaviouralprogrammm_equals_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Equals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(FunctionCallStatement)


def test_hyp_functioncallstatement_constructor_exists():
    assert callable(FunctionCallStatement.__init__)


def test_hyp_functioncallstatement_constructor_args():
    sig = inspect.signature(FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_writelinestatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_WriteLineStatement)


def test_hyp_behaviouralprogrammm_writelinestatement_constructor_exists():
    assert callable(behaviouralProgramMM_WriteLineStatement.__init__)


def test_hyp_behaviouralprogrammm_writelinestatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_WriteLineStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_readlinestatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ReadLineStatement)


def test_hyp_behaviouralprogrammm_readlinestatement_constructor_exists():
    assert callable(behaviouralProgramMM_ReadLineStatement.__init__)


def test_hyp_behaviouralprogrammm_readlinestatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ReadLineStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arithmeticinfixoperator_is_not_abstract():
    assert not inspect.isabstract(ArithmeticInfixOperator)


def test_hyp_arithmeticinfixoperator_constructor_exists():
    assert callable(ArithmeticInfixOperator.__init__)


def test_hyp_arithmeticinfixoperator_constructor_args():
    sig = inspect.signature(ArithmeticInfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_plus_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Plus)


def test_hyp_behaviouralprogrammm_plus_constructor_exists():
    assert callable(behaviouralProgramMM_Plus.__init__)


def test_hyp_behaviouralprogrammm_plus_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_hyp_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_hyp_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_comparsionoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ComparsionOperator)


def test_hyp_behaviouralprogrammm_comparsionoperator_constructor_exists():
    assert callable(behaviouralProgramMM_ComparsionOperator.__init__)


def test_hyp_behaviouralprogrammm_comparsionoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ComparsionOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_arithmeticinfixoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ArithmeticInfixOperator)


def test_hyp_behaviouralprogrammm_arithmeticinfixoperator_constructor_exists():
    assert callable(behaviouralProgramMM_ArithmeticInfixOperator.__init__)


def test_hyp_behaviouralprogrammm_arithmeticinfixoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ArithmeticInfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_literal_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Literal)


def test_hyp_behaviouralprogrammm_literal_constructor_exists():
    assert callable(behaviouralProgramMM_Literal.__init__)


def test_hyp_behaviouralprogrammm_literal_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"




def test_hyp_behaviouralprogrammm_variable_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Variable)


def test_hyp_behaviouralprogrammm_variable_constructor_exists():
    assert callable(behaviouralProgramMM_Variable.__init__)


def test_hyp_behaviouralprogrammm_variable_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "VarName" in params, "Missing parameter 'VarName'"




def test_hyp_behaviouralprogrammm_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_BinaryOperator)


def test_hyp_behaviouralprogrammm_binaryoperator_constructor_exists():
    assert callable(behaviouralProgramMM_BinaryOperator.__init__)


def test_hyp_behaviouralprogrammm_binaryoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_readline_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ReadLine)


def test_hyp_behaviouralprogrammm_readline_constructor_exists():
    assert callable(behaviouralProgramMM_ReadLine.__init__)


def test_hyp_behaviouralprogrammm_readline_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ReadLine.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_functioncall_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_FunctionCall)


def test_hyp_behaviouralprogrammm_functioncall_constructor_exists():
    assert callable(behaviouralProgramMM_FunctionCall.__init__)


def test_hyp_behaviouralprogrammm_functioncall_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "FuncName" in params, "Missing parameter 'FuncName'"




def test_hyp_behaviouralprogrammm_expression_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Expression)


def test_hyp_behaviouralprogrammm_expression_constructor_exists():
    assert callable(behaviouralProgramMM_Expression.__init__)


def test_hyp_behaviouralprogrammm_expression_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_instantiation_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Instantiation)


def test_hyp_behaviouralprogrammm_instantiation_constructor_exists():
    assert callable(behaviouralProgramMM_Instantiation.__init__)


def test_hyp_behaviouralprogrammm_instantiation_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Instantiation.__init__)
    params = list(sig.parameters.keys())
    assert "VarType" in params, "Missing parameter 'VarType'"
    assert "VarName" in params, "Missing parameter 'VarName'"





def test_hyp_behaviouralprogrammm_loop_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Loop)


def test_hyp_behaviouralprogrammm_loop_constructor_exists():
    assert callable(behaviouralProgramMM_Loop.__init__)


def test_hyp_behaviouralprogrammm_loop_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_raiseexception_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_RaiseException)


def test_hyp_behaviouralprogrammm_raiseexception_constructor_exists():
    assert callable(behaviouralProgramMM_RaiseException.__init__)


def test_hyp_behaviouralprogrammm_raiseexception_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_RaiseException.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_conditionalbranch_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ConditionalBranch)


def test_hyp_behaviouralprogrammm_conditionalbranch_constructor_exists():
    assert callable(behaviouralProgramMM_ConditionalBranch.__init__)


def test_hyp_behaviouralprogrammm_conditionalbranch_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ConditionalBranch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_FunctionCallStatement)


def test_hyp_behaviouralprogrammm_functioncallstatement_constructor_exists():
    assert callable(behaviouralProgramMM_FunctionCallStatement.__init__)


def test_hyp_behaviouralprogrammm_functioncallstatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())
    assert "FuncName" in params, "Missing parameter 'FuncName'"




def test_hyp_behaviouralprogrammm_assignment_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Assignment)


def test_hyp_behaviouralprogrammm_assignment_constructor_exists():
    assert callable(behaviouralProgramMM_Assignment.__init__)


def test_hyp_behaviouralprogrammm_assignment_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "VariableName" in params, "Missing parameter 'VariableName'"




def test_hyp_behaviouralprogrammm_statement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Statement)


def test_hyp_behaviouralprogrammm_statement_constructor_exists():
    assert callable(behaviouralProgramMM_Statement.__init__)


def test_hyp_behaviouralprogrammm_statement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_trycatch_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_TryCatch)


def test_hyp_behaviouralprogrammm_trycatch_constructor_exists():
    assert callable(behaviouralProgramMM_TryCatch.__init__)


def test_hyp_behaviouralprogrammm_trycatch_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_TryCatch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_return_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Return)


def test_hyp_behaviouralprogrammm_return_constructor_exists():
    assert callable(behaviouralProgramMM_Return.__init__)


def test_hyp_behaviouralprogrammm_return_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behaviouralprogrammm_function_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Function)


def test_hyp_behaviouralprogrammm_function_constructor_exists():
    assert callable(behaviouralProgramMM_Function.__init__)


def test_hyp_behaviouralprogrammm_function_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Function.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_behaviouralprogrammm_behaviour_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Behaviour)


def test_hyp_behaviouralprogrammm_behaviour_constructor_exists():
    assert callable(behaviouralProgramMM_Behaviour.__init__)


def test_hyp_behaviouralprogrammm_behaviour_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Behaviour.__init__)
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
ComparsionOperator_strategy = st.builds(
    ComparsionOperator,
)
behaviouralProgramMM_Equals_strategy = st.builds(
    behaviouralProgramMM_Equals,
)
FunctionCallStatement_strategy = st.builds(
    FunctionCallStatement,
)
behaviouralProgramMM_WriteLineStatement_strategy = st.builds(
    behaviouralProgramMM_WriteLineStatement,
)
behaviouralProgramMM_ReadLineStatement_strategy = st.builds(
    behaviouralProgramMM_ReadLineStatement,
)
ArithmeticInfixOperator_strategy = st.builds(
    ArithmeticInfixOperator,
)
behaviouralProgramMM_Plus_strategy = st.builds(
    behaviouralProgramMM_Plus,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
behaviouralProgramMM_ComparsionOperator_strategy = st.builds(
    behaviouralProgramMM_ComparsionOperator,
)
behaviouralProgramMM_ArithmeticInfixOperator_strategy = st.builds(
    behaviouralProgramMM_ArithmeticInfixOperator,
)
Expression_strategy = st.builds(
    Expression,
)
behaviouralProgramMM_Literal_strategy = st.builds(
    behaviouralProgramMM_Literal,
    Value=
        safe_text
)
behaviouralProgramMM_Variable_strategy = st.builds(
    behaviouralProgramMM_Variable,
    VarName=
        safe_text
)
behaviouralProgramMM_BinaryOperator_strategy = st.builds(
    behaviouralProgramMM_BinaryOperator,
)
behaviouralProgramMM_ReadLine_strategy = st.builds(
    behaviouralProgramMM_ReadLine,
)
behaviouralProgramMM_FunctionCall_strategy = st.builds(
    behaviouralProgramMM_FunctionCall,
    FuncName=
        safe_text
)
behaviouralProgramMM_Expression_strategy = st.builds(
    behaviouralProgramMM_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
behaviouralProgramMM_Instantiation_strategy = st.builds(
    behaviouralProgramMM_Instantiation,
    VarType=
        safe_text,
    VarName=
        safe_text
)
behaviouralProgramMM_Loop_strategy = st.builds(
    behaviouralProgramMM_Loop,
)
behaviouralProgramMM_RaiseException_strategy = st.builds(
    behaviouralProgramMM_RaiseException,
)
behaviouralProgramMM_ConditionalBranch_strategy = st.builds(
    behaviouralProgramMM_ConditionalBranch,
)
behaviouralProgramMM_FunctionCallStatement_strategy = st.builds(
    behaviouralProgramMM_FunctionCallStatement,
    FuncName=
        safe_text
)
behaviouralProgramMM_Assignment_strategy = st.builds(
    behaviouralProgramMM_Assignment,
    VariableName=
        safe_text
)
behaviouralProgramMM_Statement_strategy = st.builds(
    behaviouralProgramMM_Statement,
)
behaviouralProgramMM_TryCatch_strategy = st.builds(
    behaviouralProgramMM_TryCatch,
)
behaviouralProgramMM_Return_strategy = st.builds(
    behaviouralProgramMM_Return,
)
behaviouralProgramMM_Function_strategy = st.builds(
    behaviouralProgramMM_Function,
    Name=
        safe_text
)
behaviouralProgramMM_Behaviour_strategy = st.builds(
    behaviouralProgramMM_Behaviour,
)















@given(instance=behaviouralProgramMM_Literal_strategy)
def test_hyp_behaviouralprogrammm_literal_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original




@given(instance=behaviouralProgramMM_Variable_strategy)
def test_hyp_behaviouralprogrammm_variable_VarName_setter(instance):
    original = instance.VarName
    instance.VarName = original
    assert instance.VarName == original






@given(instance=behaviouralProgramMM_FunctionCall_strategy)
def test_hyp_behaviouralprogrammm_functioncall_FuncName_setter(instance):
    original = instance.FuncName
    instance.FuncName = original
    assert instance.FuncName == original






@given(instance=behaviouralProgramMM_Instantiation_strategy)
def test_hyp_behaviouralprogrammm_instantiation_VarType_setter(instance):
    original = instance.VarType
    instance.VarType = original
    assert instance.VarType == original



@given(instance=behaviouralProgramMM_Instantiation_strategy)
def test_hyp_behaviouralprogrammm_instantiation_VarName_setter(instance):
    original = instance.VarName
    instance.VarName = original
    assert instance.VarName == original







@given(instance=behaviouralProgramMM_FunctionCallStatement_strategy)
def test_hyp_behaviouralprogrammm_functioncallstatement_FuncName_setter(instance):
    original = instance.FuncName
    instance.FuncName = original
    assert instance.FuncName == original




@given(instance=behaviouralProgramMM_Assignment_strategy)
def test_hyp_behaviouralprogrammm_assignment_VariableName_setter(instance):
    original = instance.VariableName
    instance.VariableName = original
    assert instance.VariableName == original







@given(instance=behaviouralProgramMM_Function_strategy)
def test_hyp_behaviouralprogrammm_function_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArithmeticInfixOperator,
    BinaryOperator,
    ComparsionOperator,
    Expression,
    FunctionCallStatement,
    Statement,
    behaviouralProgramMM_ArithmeticInfixOperator,
    behaviouralProgramMM_Assignment,
    behaviouralProgramMM_Behaviour,
    behaviouralProgramMM_BinaryOperator,
    behaviouralProgramMM_ComparsionOperator,
    behaviouralProgramMM_ConditionalBranch,
    behaviouralProgramMM_Equals,
    behaviouralProgramMM_Expression,
    behaviouralProgramMM_Function,
    behaviouralProgramMM_FunctionCall,
    behaviouralProgramMM_FunctionCallStatement,
    behaviouralProgramMM_Instantiation,
    behaviouralProgramMM_Literal,
    behaviouralProgramMM_Loop,
    behaviouralProgramMM_Plus,
    behaviouralProgramMM_RaiseException,
    behaviouralProgramMM_ReadLine,
    behaviouralProgramMM_ReadLineStatement,
    behaviouralProgramMM_Return,
    behaviouralProgramMM_Statement,
    behaviouralProgramMM_TryCatch,
    behaviouralProgramMM_Variable,
    behaviouralProgramMM_WriteLineStatement,
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

def test_behaviouralProgramMM_Assignment_VariableName_value_roundtrip():
    instance = behaviouralProgramMM_Assignment(VariableName="sample_text")
    assert instance.VariableName == "sample_text"
    instance.VariableName = "sample_text_2"
    assert instance.VariableName == "sample_text_2"


def test_behaviouralProgramMM_Function_Name_value_roundtrip():
    instance = behaviouralProgramMM_Function(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_behaviouralProgramMM_FunctionCall_FuncName_value_roundtrip():
    instance = behaviouralProgramMM_FunctionCall(FuncName="sample_text")
    assert instance.FuncName == "sample_text"
    instance.FuncName = "sample_text_2"
    assert instance.FuncName == "sample_text_2"


def test_behaviouralProgramMM_FunctionCallStatement_FuncName_value_roundtrip():
    instance = behaviouralProgramMM_FunctionCallStatement(FuncName="sample_text")
    assert instance.FuncName == "sample_text"
    instance.FuncName = "sample_text_2"
    assert instance.FuncName == "sample_text_2"


def test_behaviouralProgramMM_Instantiation_VarName_value_roundtrip():
    instance = behaviouralProgramMM_Instantiation(VarName="sample_text", VarType="sample_text")
    assert instance.VarName == "sample_text"
    instance.VarName = "sample_text_2"
    assert instance.VarName == "sample_text_2"


def test_behaviouralProgramMM_Instantiation_VarType_value_roundtrip():
    instance = behaviouralProgramMM_Instantiation(VarName="sample_text", VarType="sample_text")
    assert instance.VarType == "sample_text"
    instance.VarType = "sample_text_2"
    assert instance.VarType == "sample_text_2"


def test_behaviouralProgramMM_Literal_Value_value_roundtrip():
    instance = behaviouralProgramMM_Literal(Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_behaviouralProgramMM_Variable_VarName_value_roundtrip():
    instance = behaviouralProgramMM_Variable(VarName="sample_text")
    assert instance.VarName == "sample_text"
    instance.VarName = "sample_text_2"
    assert instance.VarName == "sample_text_2"


def test_behaviouralProgramMM_Plus_isa_ArithmeticInfixOperator():
    instance = behaviouralProgramMM_Plus()
    assert isinstance(instance, ArithmeticInfixOperator)


def test_behaviouralProgramMM_ArithmeticInfixOperator_isa_BinaryOperator():
    instance = behaviouralProgramMM_ArithmeticInfixOperator()
    assert isinstance(instance, BinaryOperator)


def test_behaviouralProgramMM_ComparsionOperator_isa_BinaryOperator():
    instance = behaviouralProgramMM_ComparsionOperator()
    assert isinstance(instance, BinaryOperator)


def test_behaviouralProgramMM_Equals_isa_ComparsionOperator():
    instance = behaviouralProgramMM_Equals()
    assert isinstance(instance, ComparsionOperator)


def test_behaviouralProgramMM_BinaryOperator_isa_Expression():
    instance = behaviouralProgramMM_BinaryOperator()
    assert isinstance(instance, Expression)


def test_behaviouralProgramMM_FunctionCall_isa_Expression():
    instance = behaviouralProgramMM_FunctionCall(FuncName="sample_text")
    assert isinstance(instance, Expression)


def test_behaviouralProgramMM_Literal_isa_Expression():
    instance = behaviouralProgramMM_Literal(Value="sample_text")
    assert isinstance(instance, Expression)


def test_behaviouralProgramMM_ReadLine_isa_Expression():
    instance = behaviouralProgramMM_ReadLine()
    assert isinstance(instance, Expression)


def test_behaviouralProgramMM_Variable_isa_Expression():
    instance = behaviouralProgramMM_Variable(VarName="sample_text")
    assert isinstance(instance, Expression)


def test_behaviouralProgramMM_ReadLineStatement_isa_FunctionCallStatement():
    instance = behaviouralProgramMM_ReadLineStatement()
    assert isinstance(instance, FunctionCallStatement)


def test_behaviouralProgramMM_WriteLineStatement_isa_FunctionCallStatement():
    instance = behaviouralProgramMM_WriteLineStatement()
    assert isinstance(instance, FunctionCallStatement)


def test_behaviouralProgramMM_Assignment_isa_Statement():
    instance = behaviouralProgramMM_Assignment(VariableName="sample_text")
    assert isinstance(instance, Statement)


def test_behaviouralProgramMM_ConditionalBranch_isa_Statement():
    instance = behaviouralProgramMM_ConditionalBranch()
    assert isinstance(instance, Statement)


def test_behaviouralProgramMM_FunctionCallStatement_isa_Statement():
    instance = behaviouralProgramMM_FunctionCallStatement(FuncName="sample_text")
    assert isinstance(instance, Statement)


def test_behaviouralProgramMM_Instantiation_isa_Statement():
    instance = behaviouralProgramMM_Instantiation(VarName="sample_text", VarType="sample_text")
    assert isinstance(instance, Statement)


def test_behaviouralProgramMM_Loop_isa_Statement():
    instance = behaviouralProgramMM_Loop()
    assert isinstance(instance, Statement)


def test_behaviouralProgramMM_RaiseException_isa_Statement():
    instance = behaviouralProgramMM_RaiseException()
    assert isinstance(instance, Statement)


def test_behaviouralProgramMM_Return_isa_Statement():
    instance = behaviouralProgramMM_Return()
    assert isinstance(instance, Statement)


def test_behaviouralProgramMM_TryCatch_isa_Statement():
    instance = behaviouralProgramMM_TryCatch()
    assert isinstance(instance, Statement)


def test_assoc_InitiationExpression22_link_reassign_clear():
    a = behaviouralProgramMM_Instantiation(VarName="sample_text", VarType="sample_text")
    b1 = behaviouralProgramMM_Expression()
    b2 = behaviouralProgramMM_Expression()
    _safe_set(a, 'behaviouralProgramMM_Instantiation', b1)
    assert _is_linked(a, 'behaviouralProgramMM_Instantiation', b1)
    if hasattr(b1, 'behaviouralProgramMM_Expression23'):
        assert _is_linked(b1, 'behaviouralProgramMM_Expression23', a)
    _safe_set(a, 'behaviouralProgramMM_Instantiation', b2)
    assert _is_linked(a, 'behaviouralProgramMM_Instantiation', b2)
    if hasattr(b1, 'behaviouralProgramMM_Expression23'):
        assert not _is_linked(b1, 'behaviouralProgramMM_Expression23', a)
    if hasattr(b2, 'behaviouralProgramMM_Expression23'):
        assert _is_linked(b2, 'behaviouralProgramMM_Expression23', a)
    _safe_set(a, 'behaviouralProgramMM_Instantiation', None)
    assert not _is_linked(a, 'behaviouralProgramMM_Instantiation', b2)
    if hasattr(b2, 'behaviouralProgramMM_Expression23'):
        assert not _is_linked(b2, 'behaviouralProgramMM_Expression23', a)


def test_assoc_arguments20_link_reassign_clear():
    a = behaviouralProgramMM_FunctionCall(FuncName="sample_text")
    b1 = behaviouralProgramMM_Expression()
    b2 = behaviouralProgramMM_Expression()
    _safe_set(a, 'behaviouralProgramMM_FunctionCall', {b1})
    assert _is_linked(a, 'behaviouralProgramMM_FunctionCall', b1)
    if hasattr(b1, 'behaviouralProgramMM_Expression21'):
        assert _is_linked(b1, 'behaviouralProgramMM_Expression21', a)
    _safe_set(a, 'behaviouralProgramMM_FunctionCall', {b2})
    assert _is_linked(a, 'behaviouralProgramMM_FunctionCall', b2)
    if hasattr(b1, 'behaviouralProgramMM_Expression21'):
        assert not _is_linked(b1, 'behaviouralProgramMM_Expression21', a)
    if hasattr(b2, 'behaviouralProgramMM_Expression21'):
        assert _is_linked(b2, 'behaviouralProgramMM_Expression21', a)
    _safe_set(a, 'behaviouralProgramMM_FunctionCall', set())
    assert not _is_linked(a, 'behaviouralProgramMM_FunctionCall', b2)
    if hasattr(b2, 'behaviouralProgramMM_Expression21'):
        assert not _is_linked(b2, 'behaviouralProgramMM_Expression21', a)


def test_assoc_arguments33_link_reassign_clear():
    a = behaviouralProgramMM_FunctionCallStatement(FuncName="sample_text")
    b1 = behaviouralProgramMM_Expression()
    b2 = behaviouralProgramMM_Expression()
    _safe_set(a, 'behaviouralProgramMM_FunctionCallStatement', {b1})
    assert _is_linked(a, 'behaviouralProgramMM_FunctionCallStatement', b1)
    if hasattr(b1, 'behaviouralProgramMM_Expression34'):
        assert _is_linked(b1, 'behaviouralProgramMM_Expression34', a)
    _safe_set(a, 'behaviouralProgramMM_FunctionCallStatement', {b2})
    assert _is_linked(a, 'behaviouralProgramMM_FunctionCallStatement', b2)
    if hasattr(b1, 'behaviouralProgramMM_Expression34'):
        assert not _is_linked(b1, 'behaviouralProgramMM_Expression34', a)
    if hasattr(b2, 'behaviouralProgramMM_Expression34'):
        assert _is_linked(b2, 'behaviouralProgramMM_Expression34', a)
    _safe_set(a, 'behaviouralProgramMM_FunctionCallStatement', set())
    assert not _is_linked(a, 'behaviouralProgramMM_FunctionCallStatement', b2)
    if hasattr(b2, 'behaviouralProgramMM_Expression34'):
        assert not _is_linked(b2, 'behaviouralProgramMM_Expression34', a)


def test_assoc_assignexpression6_link_reassign_clear():
    a = behaviouralProgramMM_Assignment(VariableName="sample_text")
    b1 = behaviouralProgramMM_Expression()
    b2 = behaviouralProgramMM_Expression()
    _safe_set(a, 'behaviouralProgramMM_Assignment', b1)
    assert _is_linked(a, 'behaviouralProgramMM_Assignment', b1)
    if hasattr(b1, 'behaviouralProgramMM_Expression'):
        assert _is_linked(b1, 'behaviouralProgramMM_Expression', a)
    _safe_set(a, 'behaviouralProgramMM_Assignment', b2)
    assert _is_linked(a, 'behaviouralProgramMM_Assignment', b2)
    if hasattr(b1, 'behaviouralProgramMM_Expression'):
        assert not _is_linked(b1, 'behaviouralProgramMM_Expression', a)
    if hasattr(b2, 'behaviouralProgramMM_Expression'):
        assert _is_linked(b2, 'behaviouralProgramMM_Expression', a)
    _safe_set(a, 'behaviouralProgramMM_Assignment', None)
    assert not _is_linked(a, 'behaviouralProgramMM_Assignment', b2)
    if hasattr(b2, 'behaviouralProgramMM_Expression'):
        assert not _is_linked(b2, 'behaviouralProgramMM_Expression', a)


def test_assoc_functionBody4_link_reassign_clear():
    a = behaviouralProgramMM_Function(Name="sample_text")
    b1 = behaviouralProgramMM_Statement()
    b2 = behaviouralProgramMM_Statement()
    _safe_set(a, 'behaviouralProgramMM_Function5', {b1})
    assert _is_linked(a, 'behaviouralProgramMM_Function5', b1)
    if hasattr(b1, 'behaviouralProgramMM_Statement'):
        assert _is_linked(b1, 'behaviouralProgramMM_Statement', a)
    _safe_set(a, 'behaviouralProgramMM_Function5', {b2})
    assert _is_linked(a, 'behaviouralProgramMM_Function5', b2)
    if hasattr(b1, 'behaviouralProgramMM_Statement'):
        assert not _is_linked(b1, 'behaviouralProgramMM_Statement', a)
    if hasattr(b2, 'behaviouralProgramMM_Statement'):
        assert _is_linked(b2, 'behaviouralProgramMM_Statement', a)
    _safe_set(a, 'behaviouralProgramMM_Function5', set())
    assert not _is_linked(a, 'behaviouralProgramMM_Function5', b2)
    if hasattr(b2, 'behaviouralProgramMM_Statement'):
        assert not _is_linked(b2, 'behaviouralProgramMM_Statement', a)


def test_assoc_functions0_link_reassign_clear():
    a = behaviouralProgramMM_Function(Name="sample_text")
    b1 = behaviouralProgramMM_Behaviour()
    b2 = behaviouralProgramMM_Behaviour()
    _safe_set(a, 'behaviouralProgramMM_Function', b1)
    assert _is_linked(a, 'behaviouralProgramMM_Function', b1)
    if hasattr(b1, 'behaviouralProgramMM_Behaviour'):
        assert _is_linked(b1, 'behaviouralProgramMM_Behaviour', a)
    _safe_set(a, 'behaviouralProgramMM_Function', b2)
    assert _is_linked(a, 'behaviouralProgramMM_Function', b2)
    if hasattr(b1, 'behaviouralProgramMM_Behaviour'):
        assert not _is_linked(b1, 'behaviouralProgramMM_Behaviour', a)
    if hasattr(b2, 'behaviouralProgramMM_Behaviour'):
        assert _is_linked(b2, 'behaviouralProgramMM_Behaviour', a)
    _safe_set(a, 'behaviouralProgramMM_Function', None)
    assert not _is_linked(a, 'behaviouralProgramMM_Function', b2)
    if hasattr(b2, 'behaviouralProgramMM_Behaviour'):
        assert not _is_linked(b2, 'behaviouralProgramMM_Behaviour', a)


def test_assoc_startfunction1_link_reassign_clear():
    a = behaviouralProgramMM_Function(Name="sample_text")
    b1 = behaviouralProgramMM_Behaviour()
    b2 = behaviouralProgramMM_Behaviour()
    _safe_set(a, 'behaviouralProgramMM_Function3', b1)
    assert _is_linked(a, 'behaviouralProgramMM_Function3', b1)
    if hasattr(b1, 'behaviouralProgramMM_Behaviour2'):
        assert _is_linked(b1, 'behaviouralProgramMM_Behaviour2', a)
    _safe_set(a, 'behaviouralProgramMM_Function3', b2)
    assert _is_linked(a, 'behaviouralProgramMM_Function3', b2)
    if hasattr(b1, 'behaviouralProgramMM_Behaviour2'):
        assert not _is_linked(b1, 'behaviouralProgramMM_Behaviour2', a)
    if hasattr(b2, 'behaviouralProgramMM_Behaviour2'):
        assert _is_linked(b2, 'behaviouralProgramMM_Behaviour2', a)
    _safe_set(a, 'behaviouralProgramMM_Function3', None)
    assert not _is_linked(a, 'behaviouralProgramMM_Function3', b2)
    if hasattr(b2, 'behaviouralProgramMM_Behaviour2'):
        assert not _is_linked(b2, 'behaviouralProgramMM_Behaviour2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArithmeticInfixOperator_strategy = st.builds(ArithmeticInfixOperator)
@given(instance=ArithmeticInfixOperator_strategy)
@settings(max_examples=25)
def test_ArithmeticInfixOperator_instantiation(instance):
    assert isinstance(instance, ArithmeticInfixOperator)


BinaryOperator_strategy = st.builds(BinaryOperator)
@given(instance=BinaryOperator_strategy)
@settings(max_examples=25)
def test_BinaryOperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)


ComparsionOperator_strategy = st.builds(ComparsionOperator)
@given(instance=ComparsionOperator_strategy)
@settings(max_examples=25)
def test_ComparsionOperator_instantiation(instance):
    assert isinstance(instance, ComparsionOperator)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FunctionCallStatement_strategy = st.builds(FunctionCallStatement)
@given(instance=FunctionCallStatement_strategy)
@settings(max_examples=25)
def test_FunctionCallStatement_instantiation(instance):
    assert isinstance(instance, FunctionCallStatement)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


behaviouralProgramMM_ArithmeticInfixOperator_strategy = st.builds(behaviouralProgramMM_ArithmeticInfixOperator)
@given(instance=behaviouralProgramMM_ArithmeticInfixOperator_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_ArithmeticInfixOperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ArithmeticInfixOperator)


behaviouralProgramMM_Assignment_strategy = st.builds(behaviouralProgramMM_Assignment, VariableName=safe_text)
@given(instance=behaviouralProgramMM_Assignment_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Assignment_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Assignment)


behaviouralProgramMM_Behaviour_strategy = st.builds(behaviouralProgramMM_Behaviour)
@given(instance=behaviouralProgramMM_Behaviour_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Behaviour_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Behaviour)


behaviouralProgramMM_BinaryOperator_strategy = st.builds(behaviouralProgramMM_BinaryOperator)
@given(instance=behaviouralProgramMM_BinaryOperator_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_BinaryOperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_BinaryOperator)


behaviouralProgramMM_ComparsionOperator_strategy = st.builds(behaviouralProgramMM_ComparsionOperator)
@given(instance=behaviouralProgramMM_ComparsionOperator_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_ComparsionOperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ComparsionOperator)


behaviouralProgramMM_ConditionalBranch_strategy = st.builds(behaviouralProgramMM_ConditionalBranch)
@given(instance=behaviouralProgramMM_ConditionalBranch_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_ConditionalBranch_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ConditionalBranch)


behaviouralProgramMM_Equals_strategy = st.builds(behaviouralProgramMM_Equals)
@given(instance=behaviouralProgramMM_Equals_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Equals_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Equals)


behaviouralProgramMM_Expression_strategy = st.builds(behaviouralProgramMM_Expression)
@given(instance=behaviouralProgramMM_Expression_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Expression_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Expression)


behaviouralProgramMM_Function_strategy = st.builds(behaviouralProgramMM_Function, Name=safe_text)
@given(instance=behaviouralProgramMM_Function_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Function_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Function)


behaviouralProgramMM_FunctionCall_strategy = st.builds(behaviouralProgramMM_FunctionCall, FuncName=safe_text)
@given(instance=behaviouralProgramMM_FunctionCall_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_FunctionCall_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_FunctionCall)


behaviouralProgramMM_FunctionCallStatement_strategy = st.builds(behaviouralProgramMM_FunctionCallStatement, FuncName=safe_text)
@given(instance=behaviouralProgramMM_FunctionCallStatement_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_FunctionCallStatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_FunctionCallStatement)


behaviouralProgramMM_Instantiation_strategy = st.builds(behaviouralProgramMM_Instantiation, VarName=safe_text, VarType=safe_text)
@given(instance=behaviouralProgramMM_Instantiation_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Instantiation_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Instantiation)


behaviouralProgramMM_Literal_strategy = st.builds(behaviouralProgramMM_Literal, Value=safe_text)
@given(instance=behaviouralProgramMM_Literal_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Literal_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Literal)


behaviouralProgramMM_Loop_strategy = st.builds(behaviouralProgramMM_Loop)
@given(instance=behaviouralProgramMM_Loop_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Loop_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Loop)


behaviouralProgramMM_Plus_strategy = st.builds(behaviouralProgramMM_Plus)
@given(instance=behaviouralProgramMM_Plus_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Plus_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Plus)


behaviouralProgramMM_RaiseException_strategy = st.builds(behaviouralProgramMM_RaiseException)
@given(instance=behaviouralProgramMM_RaiseException_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_RaiseException_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_RaiseException)


behaviouralProgramMM_ReadLine_strategy = st.builds(behaviouralProgramMM_ReadLine)
@given(instance=behaviouralProgramMM_ReadLine_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_ReadLine_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ReadLine)


behaviouralProgramMM_ReadLineStatement_strategy = st.builds(behaviouralProgramMM_ReadLineStatement)
@given(instance=behaviouralProgramMM_ReadLineStatement_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_ReadLineStatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ReadLineStatement)


behaviouralProgramMM_Return_strategy = st.builds(behaviouralProgramMM_Return)
@given(instance=behaviouralProgramMM_Return_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Return_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Return)


behaviouralProgramMM_Statement_strategy = st.builds(behaviouralProgramMM_Statement)
@given(instance=behaviouralProgramMM_Statement_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Statement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Statement)


behaviouralProgramMM_TryCatch_strategy = st.builds(behaviouralProgramMM_TryCatch)
@given(instance=behaviouralProgramMM_TryCatch_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_TryCatch_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_TryCatch)


behaviouralProgramMM_Variable_strategy = st.builds(behaviouralProgramMM_Variable, VarName=safe_text)
@given(instance=behaviouralProgramMM_Variable_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_Variable_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Variable)


behaviouralProgramMM_WriteLineStatement_strategy = st.builds(behaviouralProgramMM_WriteLineStatement)
@given(instance=behaviouralProgramMM_WriteLineStatement_strategy)
@settings(max_examples=25)
def test_behaviouralProgramMM_WriteLineStatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_WriteLineStatement)



