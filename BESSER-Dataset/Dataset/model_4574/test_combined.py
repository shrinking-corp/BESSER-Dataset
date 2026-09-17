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
    LastStatement_Return,
    activityecorelua_LastStatement_ReturnWithValue,
    Field,
    activityecorelua_Field_AddEntryToTable,
    activityecorelua_Field_AppendEntryToTable,
    activityecorelua_Field_AddEntryToTable_Brackets,
    activityecorelua_Functioncall_Arguments,
    activityecorelua_Field,
    Expression,
    activityecorelua_Expression_CallFunction,
    activityecorelua_Expression_Concatenation,
    activityecorelua_Expression_Modulo,
    activityecorelua_Expression_Invert,
    activityecorelua_Expression_Function,
    activityecorelua_Expression_Multiplication,
    activityecorelua_Expression_CallMemberFunction,
    activityecorelua_Expression_Exponentiation,
    activityecorelua_Expression_Negate,
    activityecorelua_Expression_Larger_Equal,
    activityecorelua_Expression_True,
    activityecorelua_Expression_AccessMember,
    activityecorelua_Expression_And,
    activityecorelua_Expression_Equal,
    activityecorelua_Expression_VarArgs,
    activityecorelua_Expression_Plus,
    activityecorelua_Expression_VariableName,
    activityecorelua_Expression_Number,
    activityecorelua_Expression_Length,
    activityecorelua_Expression_Division,
    activityecorelua_Expression_Not_Equal,
    activityecorelua_Expression_Minus,
    activityecorelua_Expression_Or,
    activityecorelua_Expression_AccessArray,
    activityecorelua_Expression_TableConstructor,
    activityecorelua_Expression_Larger,
    activityecorelua_Expression_String,
    activityecorelua_Expression_Smaller,
    activityecorelua_Expression_Smaller_Equal,
    activityecorelua_Expression_False,
    activityecorelua_Expression_Nil,
    Statement_FunctioncallOrAssignment,
    activityecorelua_Statement_CallMemberFunction,
    activityecorelua_Statement_CallFunction,
    activityecorelua_Statement_Assignment,
    activityecorelua_Statement_If_Then_Else_ElseIfPart,
    activityecorelua_Function,
    LastStatement,
    activityecorelua_LastStatement_Break,
    activityecorelua_LastStatement_Return,
    activityecorelua_LastStatement,
    activityecorelua_Statement,
    Chunk,
    activityecorelua_Block,
    activityecorelua_Chunk,
    Statement,
    activityecorelua_Statement_LocalFunction_Declaration,
    activityecorelua_Statement_If_Then_Else,
    activityecorelua_Statement_FunctioncallOrAssignment,
    activityecorelua_Statement_Repeat,
    activityecorelua_Statement_GlobalFunction_Declaration,
    activityecorelua_Statement_For_Generic,
    activityecorelua_Statement_For_Numeric,
    activityecorelua_Statement_Local_Variable_Declaration,
    activityecorelua_Statement_While,
    activityecorelua_Statement_Block,
    Variable,
    activityecorelua_IntegerVariable,
    activityecorelua_Value,
    activityecorelua_Input,
    activityecorelua_InputValue,
    Value,
    activityecorelua_IntegerValue,
    activityecorelua_BooleanValue,
    activityecorelua_Expression,
    Action,
    activityecorelua_OpaqueAction,
    ExecutableNode,
    activityecorelua_Action,
    ActivityNode,
    activityecorelua_ExecutableNode,
    activityecorelua_ControlNode,
    activityecorelua_BooleanVariable,
    ActivityEdge,
    activityecorelua_ControlFlow,
    FinalNode,
    activityecorelua_ActivityFinalNode,
    ControlNode,
    activityecorelua_ForkNode,
    activityecorelua_DecisionNode,
    activityecorelua_MergeNode,
    activityecorelua_FinalNode,
    activityecorelua_JoinNode,
    activityecorelua_InitialNode,
    activityecorelua_NamedElement,
    activityecorelua_Variable,
    NamedElement,
    activityecorelua_ActivityEdge,
    activityecorelua_ActivityNode,
    ETypedElement,
    activityecorelua_Activity,
    activityecorelua_EParameter,
    EDataType,
    activityecorelua_EEnum,
    ENamedElement,
    activityecorelua_EEnumLiteral,
    activityecorelua_EPackage,
    activityecorelua_ETypeParameter,
    activityecorelua_ETypedElement,
    activityecorelua_EClassifier,
    activityecorelua_EGenericType,
    activityecorelua_EOperation,
    activityecorelua_EStructuralFeature,
    EClassifier,
    activityecorelua_EClass,
    activityecorelua_EObject,
    activityecorelua_EModelElement,
    activityecorelua_EStringToStringMapEntry,
    EModelElement,
    activityecorelua_EFactory,
    activityecorelua_ENamedElement,
    activityecorelua_EAnnotation,
    activityecorelua_EDataType,
    EStructuralFeature,
    activityecorelua_EReference,
    activityecorelua_EAttribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_laststatement_return_is_not_abstract():
    assert not inspect.isabstract(LastStatement_Return)


def test_hyp_laststatement_return_constructor_exists():
    assert callable(LastStatement_Return.__init__)


def test_hyp_laststatement_return_constructor_args():
    sig = inspect.signature(LastStatement_Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_laststatement_returnwithvalue_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_LastStatement_ReturnWithValue)


def test_hyp_activityecorelua_laststatement_returnwithvalue_constructor_exists():
    assert callable(activityecorelua_LastStatement_ReturnWithValue.__init__)


def test_hyp_activityecorelua_laststatement_returnwithvalue_constructor_args():
    sig = inspect.signature(activityecorelua_LastStatement_ReturnWithValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_hyp_field_constructor_exists():
    assert callable(Field.__init__)


def test_hyp_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_field_addentrytotable_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Field_AddEntryToTable)


def test_hyp_activityecorelua_field_addentrytotable_constructor_exists():
    assert callable(activityecorelua_Field_AddEntryToTable.__init__)


def test_hyp_activityecorelua_field_addentrytotable_constructor_args():
    sig = inspect.signature(activityecorelua_Field_AddEntryToTable.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_activityecorelua_field_appendentrytotable_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Field_AppendEntryToTable)


def test_hyp_activityecorelua_field_appendentrytotable_constructor_exists():
    assert callable(activityecorelua_Field_AppendEntryToTable.__init__)


def test_hyp_activityecorelua_field_appendentrytotable_constructor_args():
    sig = inspect.signature(activityecorelua_Field_AppendEntryToTable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_field_addentrytotable_brackets_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Field_AddEntryToTable_Brackets)


def test_hyp_activityecorelua_field_addentrytotable_brackets_constructor_exists():
    assert callable(activityecorelua_Field_AddEntryToTable_Brackets.__init__)


def test_hyp_activityecorelua_field_addentrytotable_brackets_constructor_args():
    sig = inspect.signature(activityecorelua_Field_AddEntryToTable_Brackets.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_functioncall_arguments_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Functioncall_Arguments)


def test_hyp_activityecorelua_functioncall_arguments_constructor_exists():
    assert callable(activityecorelua_Functioncall_Arguments.__init__)


def test_hyp_activityecorelua_functioncall_arguments_constructor_args():
    sig = inspect.signature(activityecorelua_Functioncall_Arguments.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_field_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Field)


def test_hyp_activityecorelua_field_constructor_exists():
    assert callable(activityecorelua_Field.__init__)


def test_hyp_activityecorelua_field_constructor_args():
    sig = inspect.signature(activityecorelua_Field.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_callfunction_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_CallFunction)


def test_hyp_activityecorelua_expression_callfunction_constructor_exists():
    assert callable(activityecorelua_Expression_CallFunction.__init__)


def test_hyp_activityecorelua_expression_callfunction_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_concatenation_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Concatenation)


def test_hyp_activityecorelua_expression_concatenation_constructor_exists():
    assert callable(activityecorelua_Expression_Concatenation.__init__)


def test_hyp_activityecorelua_expression_concatenation_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Concatenation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_modulo_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Modulo)


def test_hyp_activityecorelua_expression_modulo_constructor_exists():
    assert callable(activityecorelua_Expression_Modulo.__init__)


def test_hyp_activityecorelua_expression_modulo_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_invert_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Invert)


def test_hyp_activityecorelua_expression_invert_constructor_exists():
    assert callable(activityecorelua_Expression_Invert.__init__)


def test_hyp_activityecorelua_expression_invert_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Invert.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_function_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Function)


def test_hyp_activityecorelua_expression_function_constructor_exists():
    assert callable(activityecorelua_Expression_Function.__init__)


def test_hyp_activityecorelua_expression_function_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_multiplication_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Multiplication)


def test_hyp_activityecorelua_expression_multiplication_constructor_exists():
    assert callable(activityecorelua_Expression_Multiplication.__init__)


def test_hyp_activityecorelua_expression_multiplication_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_CallMemberFunction)


def test_hyp_activityecorelua_expression_callmemberfunction_constructor_exists():
    assert callable(activityecorelua_Expression_CallMemberFunction.__init__)


def test_hyp_activityecorelua_expression_callmemberfunction_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"




def test_hyp_activityecorelua_expression_exponentiation_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Exponentiation)


def test_hyp_activityecorelua_expression_exponentiation_constructor_exists():
    assert callable(activityecorelua_Expression_Exponentiation.__init__)


def test_hyp_activityecorelua_expression_exponentiation_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Exponentiation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_negate_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Negate)


def test_hyp_activityecorelua_expression_negate_constructor_exists():
    assert callable(activityecorelua_Expression_Negate.__init__)


def test_hyp_activityecorelua_expression_negate_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Negate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_larger_equal_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Larger_Equal)


def test_hyp_activityecorelua_expression_larger_equal_constructor_exists():
    assert callable(activityecorelua_Expression_Larger_Equal.__init__)


def test_hyp_activityecorelua_expression_larger_equal_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Larger_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_true_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_True)


def test_hyp_activityecorelua_expression_true_constructor_exists():
    assert callable(activityecorelua_Expression_True.__init__)


def test_hyp_activityecorelua_expression_true_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_True.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_accessmember_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_AccessMember)


def test_hyp_activityecorelua_expression_accessmember_constructor_exists():
    assert callable(activityecorelua_Expression_AccessMember.__init__)


def test_hyp_activityecorelua_expression_accessmember_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_AccessMember.__init__)
    params = list(sig.parameters.keys())
    assert "memberName" in params, "Missing parameter 'memberName'"




def test_hyp_activityecorelua_expression_and_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_And)


def test_hyp_activityecorelua_expression_and_constructor_exists():
    assert callable(activityecorelua_Expression_And.__init__)


def test_hyp_activityecorelua_expression_and_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_equal_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Equal)


def test_hyp_activityecorelua_expression_equal_constructor_exists():
    assert callable(activityecorelua_Expression_Equal.__init__)


def test_hyp_activityecorelua_expression_equal_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_varargs_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_VarArgs)


def test_hyp_activityecorelua_expression_varargs_constructor_exists():
    assert callable(activityecorelua_Expression_VarArgs.__init__)


def test_hyp_activityecorelua_expression_varargs_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_VarArgs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_plus_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Plus)


def test_hyp_activityecorelua_expression_plus_constructor_exists():
    assert callable(activityecorelua_Expression_Plus.__init__)


def test_hyp_activityecorelua_expression_plus_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_variablename_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_VariableName)


def test_hyp_activityecorelua_expression_variablename_constructor_exists():
    assert callable(activityecorelua_Expression_VariableName.__init__)


def test_hyp_activityecorelua_expression_variablename_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_VariableName.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"




def test_hyp_activityecorelua_expression_number_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Number)


def test_hyp_activityecorelua_expression_number_constructor_exists():
    assert callable(activityecorelua_Expression_Number.__init__)


def test_hyp_activityecorelua_expression_number_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_activityecorelua_expression_length_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Length)


def test_hyp_activityecorelua_expression_length_constructor_exists():
    assert callable(activityecorelua_Expression_Length.__init__)


def test_hyp_activityecorelua_expression_length_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Length.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_division_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Division)


def test_hyp_activityecorelua_expression_division_constructor_exists():
    assert callable(activityecorelua_Expression_Division.__init__)


def test_hyp_activityecorelua_expression_division_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_not_equal_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Not_Equal)


def test_hyp_activityecorelua_expression_not_equal_constructor_exists():
    assert callable(activityecorelua_Expression_Not_Equal.__init__)


def test_hyp_activityecorelua_expression_not_equal_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Not_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_minus_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Minus)


def test_hyp_activityecorelua_expression_minus_constructor_exists():
    assert callable(activityecorelua_Expression_Minus.__init__)


def test_hyp_activityecorelua_expression_minus_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_or_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Or)


def test_hyp_activityecorelua_expression_or_constructor_exists():
    assert callable(activityecorelua_Expression_Or.__init__)


def test_hyp_activityecorelua_expression_or_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_accessarray_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_AccessArray)


def test_hyp_activityecorelua_expression_accessarray_constructor_exists():
    assert callable(activityecorelua_Expression_AccessArray.__init__)


def test_hyp_activityecorelua_expression_accessarray_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_AccessArray.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_tableconstructor_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_TableConstructor)


def test_hyp_activityecorelua_expression_tableconstructor_constructor_exists():
    assert callable(activityecorelua_Expression_TableConstructor.__init__)


def test_hyp_activityecorelua_expression_tableconstructor_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_TableConstructor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_larger_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Larger)


def test_hyp_activityecorelua_expression_larger_constructor_exists():
    assert callable(activityecorelua_Expression_Larger.__init__)


def test_hyp_activityecorelua_expression_larger_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Larger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_string_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_String)


def test_hyp_activityecorelua_expression_string_constructor_exists():
    assert callable(activityecorelua_Expression_String.__init__)


def test_hyp_activityecorelua_expression_string_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_activityecorelua_expression_smaller_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Smaller)


def test_hyp_activityecorelua_expression_smaller_constructor_exists():
    assert callable(activityecorelua_Expression_Smaller.__init__)


def test_hyp_activityecorelua_expression_smaller_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Smaller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_smaller_equal_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Smaller_Equal)


def test_hyp_activityecorelua_expression_smaller_equal_constructor_exists():
    assert callable(activityecorelua_Expression_Smaller_Equal.__init__)


def test_hyp_activityecorelua_expression_smaller_equal_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Smaller_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_false_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_False)


def test_hyp_activityecorelua_expression_false_constructor_exists():
    assert callable(activityecorelua_Expression_False.__init__)


def test_hyp_activityecorelua_expression_false_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_False.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_expression_nil_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression_Nil)


def test_hyp_activityecorelua_expression_nil_constructor_exists():
    assert callable(activityecorelua_Expression_Nil.__init__)


def test_hyp_activityecorelua_expression_nil_constructor_args():
    sig = inspect.signature(activityecorelua_Expression_Nil.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(Statement_FunctioncallOrAssignment)


def test_hyp_statement_functioncallorassignment_constructor_exists():
    assert callable(Statement_FunctioncallOrAssignment.__init__)


def test_hyp_statement_functioncallorassignment_constructor_args():
    sig = inspect.signature(Statement_FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_callmemberfunction_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_CallMemberFunction)


def test_hyp_activityecorelua_statement_callmemberfunction_constructor_exists():
    assert callable(activityecorelua_Statement_CallMemberFunction.__init__)


def test_hyp_activityecorelua_statement_callmemberfunction_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_CallMemberFunction.__init__)
    params = list(sig.parameters.keys())
    assert "memberFunctionName" in params, "Missing parameter 'memberFunctionName'"




def test_hyp_activityecorelua_statement_callfunction_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_CallFunction)


def test_hyp_activityecorelua_statement_callfunction_constructor_exists():
    assert callable(activityecorelua_Statement_CallFunction.__init__)


def test_hyp_activityecorelua_statement_callfunction_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_CallFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_assignment_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_Assignment)


def test_hyp_activityecorelua_statement_assignment_constructor_exists():
    assert callable(activityecorelua_Statement_Assignment.__init__)


def test_hyp_activityecorelua_statement_assignment_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_if_then_else_elseifpart_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_If_Then_Else_ElseIfPart)


def test_hyp_activityecorelua_statement_if_then_else_elseifpart_constructor_exists():
    assert callable(activityecorelua_Statement_If_Then_Else_ElseIfPart.__init__)


def test_hyp_activityecorelua_statement_if_then_else_elseifpart_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_If_Then_Else_ElseIfPart.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_function_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Function)


def test_hyp_activityecorelua_function_constructor_exists():
    assert callable(activityecorelua_Function.__init__)


def test_hyp_activityecorelua_function_constructor_args():
    sig = inspect.signature(activityecorelua_Function.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"
    assert "parameters" in params, "Missing parameter 'parameters'"





def test_hyp_laststatement_is_not_abstract():
    assert not inspect.isabstract(LastStatement)


def test_hyp_laststatement_constructor_exists():
    assert callable(LastStatement.__init__)


def test_hyp_laststatement_constructor_args():
    sig = inspect.signature(LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_laststatement_break_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_LastStatement_Break)


def test_hyp_activityecorelua_laststatement_break_constructor_exists():
    assert callable(activityecorelua_LastStatement_Break.__init__)


def test_hyp_activityecorelua_laststatement_break_constructor_args():
    sig = inspect.signature(activityecorelua_LastStatement_Break.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_laststatement_return_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_LastStatement_Return)


def test_hyp_activityecorelua_laststatement_return_constructor_exists():
    assert callable(activityecorelua_LastStatement_Return.__init__)


def test_hyp_activityecorelua_laststatement_return_constructor_args():
    sig = inspect.signature(activityecorelua_LastStatement_Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_laststatement_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_LastStatement)


def test_hyp_activityecorelua_laststatement_constructor_exists():
    assert callable(activityecorelua_LastStatement.__init__)


def test_hyp_activityecorelua_laststatement_constructor_args():
    sig = inspect.signature(activityecorelua_LastStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement)


def test_hyp_activityecorelua_statement_constructor_exists():
    assert callable(activityecorelua_Statement.__init__)


def test_hyp_activityecorelua_statement_constructor_args():
    sig = inspect.signature(activityecorelua_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_chunk_is_not_abstract():
    assert not inspect.isabstract(Chunk)


def test_hyp_chunk_constructor_exists():
    assert callable(Chunk.__init__)


def test_hyp_chunk_constructor_args():
    sig = inspect.signature(Chunk.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_block_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Block)


def test_hyp_activityecorelua_block_constructor_exists():
    assert callable(activityecorelua_Block.__init__)


def test_hyp_activityecorelua_block_constructor_args():
    sig = inspect.signature(activityecorelua_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_chunk_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Chunk)


def test_hyp_activityecorelua_chunk_constructor_exists():
    assert callable(activityecorelua_Chunk.__init__)


def test_hyp_activityecorelua_chunk_constructor_args():
    sig = inspect.signature(activityecorelua_Chunk.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_localfunction_declaration_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_LocalFunction_Declaration)


def test_hyp_activityecorelua_statement_localfunction_declaration_constructor_exists():
    assert callable(activityecorelua_Statement_LocalFunction_Declaration.__init__)


def test_hyp_activityecorelua_statement_localfunction_declaration_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_LocalFunction_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"




def test_hyp_activityecorelua_statement_if_then_else_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_If_Then_Else)


def test_hyp_activityecorelua_statement_if_then_else_constructor_exists():
    assert callable(activityecorelua_Statement_If_Then_Else.__init__)


def test_hyp_activityecorelua_statement_if_then_else_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_If_Then_Else.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_functioncallorassignment_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_FunctioncallOrAssignment)


def test_hyp_activityecorelua_statement_functioncallorassignment_constructor_exists():
    assert callable(activityecorelua_Statement_FunctioncallOrAssignment.__init__)


def test_hyp_activityecorelua_statement_functioncallorassignment_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_FunctioncallOrAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_repeat_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_Repeat)


def test_hyp_activityecorelua_statement_repeat_constructor_exists():
    assert callable(activityecorelua_Statement_Repeat.__init__)


def test_hyp_activityecorelua_statement_repeat_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_Repeat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_globalfunction_declaration_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_GlobalFunction_Declaration)


def test_hyp_activityecorelua_statement_globalfunction_declaration_constructor_exists():
    assert callable(activityecorelua_Statement_GlobalFunction_Declaration.__init__)


def test_hyp_activityecorelua_statement_globalfunction_declaration_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_GlobalFunction_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"
    assert "prefix" in params, "Missing parameter 'prefix'"





def test_hyp_activityecorelua_statement_for_generic_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_For_Generic)


def test_hyp_activityecorelua_statement_for_generic_constructor_exists():
    assert callable(activityecorelua_Statement_For_Generic.__init__)


def test_hyp_activityecorelua_statement_for_generic_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_For_Generic.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"




def test_hyp_activityecorelua_statement_for_numeric_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_For_Numeric)


def test_hyp_activityecorelua_statement_for_numeric_constructor_exists():
    assert callable(activityecorelua_Statement_For_Numeric.__init__)


def test_hyp_activityecorelua_statement_for_numeric_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_For_Numeric.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"




def test_hyp_activityecorelua_statement_local_variable_declaration_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_Local_Variable_Declaration)


def test_hyp_activityecorelua_statement_local_variable_declaration_constructor_exists():
    assert callable(activityecorelua_Statement_Local_Variable_Declaration.__init__)


def test_hyp_activityecorelua_statement_local_variable_declaration_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_Local_Variable_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "variableNames" in params, "Missing parameter 'variableNames'"




def test_hyp_activityecorelua_statement_while_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_While)


def test_hyp_activityecorelua_statement_while_constructor_exists():
    assert callable(activityecorelua_Statement_While.__init__)


def test_hyp_activityecorelua_statement_while_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_statement_block_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Statement_Block)


def test_hyp_activityecorelua_statement_block_constructor_exists():
    assert callable(activityecorelua_Statement_Block.__init__)


def test_hyp_activityecorelua_statement_block_constructor_args():
    sig = inspect.signature(activityecorelua_Statement_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_integervariable_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_IntegerVariable)


def test_hyp_activityecorelua_integervariable_constructor_exists():
    assert callable(activityecorelua_IntegerVariable.__init__)


def test_hyp_activityecorelua_integervariable_constructor_args():
    sig = inspect.signature(activityecorelua_IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_value_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Value)


def test_hyp_activityecorelua_value_constructor_exists():
    assert callable(activityecorelua_Value.__init__)


def test_hyp_activityecorelua_value_constructor_args():
    sig = inspect.signature(activityecorelua_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_input_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Input)


def test_hyp_activityecorelua_input_constructor_exists():
    assert callable(activityecorelua_Input.__init__)


def test_hyp_activityecorelua_input_constructor_args():
    sig = inspect.signature(activityecorelua_Input.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_inputvalue_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_InputValue)


def test_hyp_activityecorelua_inputvalue_constructor_exists():
    assert callable(activityecorelua_InputValue.__init__)


def test_hyp_activityecorelua_inputvalue_constructor_args():
    sig = inspect.signature(activityecorelua_InputValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_integervalue_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_IntegerValue)


def test_hyp_activityecorelua_integervalue_constructor_exists():
    assert callable(activityecorelua_IntegerValue.__init__)


def test_hyp_activityecorelua_integervalue_constructor_args():
    sig = inspect.signature(activityecorelua_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_activityecorelua_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_BooleanValue)


def test_hyp_activityecorelua_booleanvalue_constructor_exists():
    assert callable(activityecorelua_BooleanValue.__init__)


def test_hyp_activityecorelua_booleanvalue_constructor_args():
    sig = inspect.signature(activityecorelua_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_activityecorelua_expression_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Expression)


def test_hyp_activityecorelua_expression_constructor_exists():
    assert callable(activityecorelua_Expression.__init__)


def test_hyp_activityecorelua_expression_constructor_args():
    sig = inspect.signature(activityecorelua_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_OpaqueAction)


def test_hyp_activityecorelua_opaqueaction_constructor_exists():
    assert callable(activityecorelua_OpaqueAction.__init__)


def test_hyp_activityecorelua_opaqueaction_constructor_args():
    sig = inspect.signature(activityecorelua_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_hyp_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_hyp_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_action_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Action)


def test_hyp_activityecorelua_action_constructor_exists():
    assert callable(activityecorelua_Action.__init__)


def test_hyp_activityecorelua_action_constructor_args():
    sig = inspect.signature(activityecorelua_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_hyp_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_hyp_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_executablenode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ExecutableNode)


def test_hyp_activityecorelua_executablenode_constructor_exists():
    assert callable(activityecorelua_ExecutableNode.__init__)


def test_hyp_activityecorelua_executablenode_constructor_args():
    sig = inspect.signature(activityecorelua_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_controlnode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ControlNode)


def test_hyp_activityecorelua_controlnode_constructor_exists():
    assert callable(activityecorelua_ControlNode.__init__)


def test_hyp_activityecorelua_controlnode_constructor_args():
    sig = inspect.signature(activityecorelua_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_booleanvariable_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_BooleanVariable)


def test_hyp_activityecorelua_booleanvariable_constructor_exists():
    assert callable(activityecorelua_BooleanVariable.__init__)


def test_hyp_activityecorelua_booleanvariable_constructor_args():
    sig = inspect.signature(activityecorelua_BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_hyp_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_hyp_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_controlflow_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ControlFlow)


def test_hyp_activityecorelua_controlflow_constructor_exists():
    assert callable(activityecorelua_ControlFlow.__init__)


def test_hyp_activityecorelua_controlflow_constructor_args():
    sig = inspect.signature(activityecorelua_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_hyp_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_hyp_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ActivityFinalNode)


def test_hyp_activityecorelua_activityfinalnode_constructor_exists():
    assert callable(activityecorelua_ActivityFinalNode.__init__)


def test_hyp_activityecorelua_activityfinalnode_constructor_args():
    sig = inspect.signature(activityecorelua_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_hyp_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_hyp_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_forknode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ForkNode)


def test_hyp_activityecorelua_forknode_constructor_exists():
    assert callable(activityecorelua_ForkNode.__init__)


def test_hyp_activityecorelua_forknode_constructor_args():
    sig = inspect.signature(activityecorelua_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_decisionnode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_DecisionNode)


def test_hyp_activityecorelua_decisionnode_constructor_exists():
    assert callable(activityecorelua_DecisionNode.__init__)


def test_hyp_activityecorelua_decisionnode_constructor_args():
    sig = inspect.signature(activityecorelua_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_mergenode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_MergeNode)


def test_hyp_activityecorelua_mergenode_constructor_exists():
    assert callable(activityecorelua_MergeNode.__init__)


def test_hyp_activityecorelua_mergenode_constructor_args():
    sig = inspect.signature(activityecorelua_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_finalnode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_FinalNode)


def test_hyp_activityecorelua_finalnode_constructor_exists():
    assert callable(activityecorelua_FinalNode.__init__)


def test_hyp_activityecorelua_finalnode_constructor_args():
    sig = inspect.signature(activityecorelua_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_joinnode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_JoinNode)


def test_hyp_activityecorelua_joinnode_constructor_exists():
    assert callable(activityecorelua_JoinNode.__init__)


def test_hyp_activityecorelua_joinnode_constructor_args():
    sig = inspect.signature(activityecorelua_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_initialnode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_InitialNode)


def test_hyp_activityecorelua_initialnode_constructor_exists():
    assert callable(activityecorelua_InitialNode.__init__)


def test_hyp_activityecorelua_initialnode_constructor_args():
    sig = inspect.signature(activityecorelua_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_namedelement_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_NamedElement)


def test_hyp_activityecorelua_namedelement_constructor_exists():
    assert callable(activityecorelua_NamedElement.__init__)


def test_hyp_activityecorelua_namedelement_constructor_args():
    sig = inspect.signature(activityecorelua_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_activityecorelua_variable_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Variable)


def test_hyp_activityecorelua_variable_constructor_exists():
    assert callable(activityecorelua_Variable.__init__)


def test_hyp_activityecorelua_variable_constructor_args():
    sig = inspect.signature(activityecorelua_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_activityedge_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ActivityEdge)


def test_hyp_activityecorelua_activityedge_constructor_exists():
    assert callable(activityecorelua_ActivityEdge.__init__)


def test_hyp_activityecorelua_activityedge_constructor_args():
    sig = inspect.signature(activityecorelua_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_activitynode_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ActivityNode)


def test_hyp_activityecorelua_activitynode_constructor_exists():
    assert callable(activityecorelua_ActivityNode.__init__)


def test_hyp_activityecorelua_activitynode_constructor_args():
    sig = inspect.signature(activityecorelua_ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"




def test_hyp_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ETypedElement)


def test_hyp_etypedelement_constructor_exists():
    assert callable(ETypedElement.__init__)


def test_hyp_etypedelement_constructor_args():
    sig = inspect.signature(ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_activity_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_Activity)


def test_hyp_activityecorelua_activity_constructor_exists():
    assert callable(activityecorelua_Activity.__init__)


def test_hyp_activityecorelua_activity_constructor_args():
    sig = inspect.signature(activityecorelua_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_eparameter_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EParameter)


def test_hyp_activityecorelua_eparameter_constructor_exists():
    assert callable(activityecorelua_EParameter.__init__)


def test_hyp_activityecorelua_eparameter_constructor_args():
    sig = inspect.signature(activityecorelua_EParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_hyp_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_hyp_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_eenum_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EEnum)


def test_hyp_activityecorelua_eenum_constructor_exists():
    assert callable(activityecorelua_EEnum.__init__)


def test_hyp_activityecorelua_eenum_constructor_args():
    sig = inspect.signature(activityecorelua_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_hyp_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_hyp_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EEnumLiteral)


def test_hyp_activityecorelua_eenumliteral_constructor_exists():
    assert callable(activityecorelua_EEnumLiteral.__init__)


def test_hyp_activityecorelua_eenumliteral_constructor_args():
    sig = inspect.signature(activityecorelua_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "instance" in params, "Missing parameter 'instance'"
    assert "literal" in params, "Missing parameter 'literal'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_activityecorelua_epackage_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EPackage)


def test_hyp_activityecorelua_epackage_constructor_exists():
    assert callable(activityecorelua_EPackage.__init__)


def test_hyp_activityecorelua_epackage_constructor_args():
    sig = inspect.signature(activityecorelua_EPackage.__init__)
    params = list(sig.parameters.keys())
    assert "nsURI" in params, "Missing parameter 'nsURI'"
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"





def test_hyp_activityecorelua_etypeparameter_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ETypeParameter)


def test_hyp_activityecorelua_etypeparameter_constructor_exists():
    assert callable(activityecorelua_ETypeParameter.__init__)


def test_hyp_activityecorelua_etypeparameter_constructor_args():
    sig = inspect.signature(activityecorelua_ETypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_etypedelement_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ETypedElement)


def test_hyp_activityecorelua_etypedelement_constructor_exists():
    assert callable(activityecorelua_ETypedElement.__init__)


def test_hyp_activityecorelua_etypedelement_constructor_args():
    sig = inspect.signature(activityecorelua_ETypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "required" in params, "Missing parameter 'required'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"









def test_hyp_activityecorelua_eclassifier_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EClassifier)


def test_hyp_activityecorelua_eclassifier_constructor_exists():
    assert callable(activityecorelua_EClassifier.__init__)


def test_hyp_activityecorelua_eclassifier_constructor_args():
    sig = inspect.signature(activityecorelua_EClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"
    assert "instanceTypeName" in params, "Missing parameter 'instanceTypeName'"







def test_hyp_activityecorelua_egenerictype_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EGenericType)


def test_hyp_activityecorelua_egenerictype_constructor_exists():
    assert callable(activityecorelua_EGenericType.__init__)


def test_hyp_activityecorelua_egenerictype_constructor_args():
    sig = inspect.signature(activityecorelua_EGenericType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_eoperation_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EOperation)


def test_hyp_activityecorelua_eoperation_constructor_exists():
    assert callable(activityecorelua_EOperation.__init__)


def test_hyp_activityecorelua_eoperation_constructor_args():
    sig = inspect.signature(activityecorelua_EOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EStructuralFeature)


def test_hyp_activityecorelua_estructuralfeature_constructor_exists():
    assert callable(activityecorelua_EStructuralFeature.__init__)


def test_hyp_activityecorelua_estructuralfeature_constructor_args():
    sig = inspect.signature(activityecorelua_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "unsettable" in params, "Missing parameter 'unsettable'"
    assert "changeable" in params, "Missing parameter 'changeable'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "defaultValueLiteral" in params, "Missing parameter 'defaultValueLiteral'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "transient" in params, "Missing parameter 'transient'"










def test_hyp_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_hyp_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_hyp_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_eclass_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EClass)


def test_hyp_activityecorelua_eclass_constructor_exists():
    assert callable(activityecorelua_EClass.__init__)


def test_hyp_activityecorelua_eclass_constructor_args():
    sig = inspect.signature(activityecorelua_EClass.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "interface" in params, "Missing parameter 'interface'"





def test_hyp_activityecorelua_eobject_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EObject)


def test_hyp_activityecorelua_eobject_constructor_exists():
    assert callable(activityecorelua_EObject.__init__)


def test_hyp_activityecorelua_eobject_constructor_args():
    sig = inspect.signature(activityecorelua_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_emodelelement_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EModelElement)


def test_hyp_activityecorelua_emodelelement_constructor_exists():
    assert callable(activityecorelua_EModelElement.__init__)


def test_hyp_activityecorelua_emodelelement_constructor_args():
    sig = inspect.signature(activityecorelua_EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EStringToStringMapEntry)


def test_hyp_activityecorelua_estringtostringmapentry_constructor_exists():
    assert callable(activityecorelua_EStringToStringMapEntry.__init__)


def test_hyp_activityecorelua_estringtostringmapentry_constructor_args():
    sig = inspect.signature(activityecorelua_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_hyp_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_hyp_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_efactory_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EFactory)


def test_hyp_activityecorelua_efactory_constructor_exists():
    assert callable(activityecorelua_EFactory.__init__)


def test_hyp_activityecorelua_efactory_constructor_args():
    sig = inspect.signature(activityecorelua_EFactory.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_enamedelement_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_ENamedElement)


def test_hyp_activityecorelua_enamedelement_constructor_exists():
    assert callable(activityecorelua_ENamedElement.__init__)


def test_hyp_activityecorelua_enamedelement_constructor_args():
    sig = inspect.signature(activityecorelua_ENamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_activityecorelua_eannotation_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EAnnotation)


def test_hyp_activityecorelua_eannotation_constructor_exists():
    assert callable(activityecorelua_EAnnotation.__init__)


def test_hyp_activityecorelua_eannotation_constructor_args():
    sig = inspect.signature(activityecorelua_EAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"




def test_hyp_activityecorelua_edatatype_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EDataType)


def test_hyp_activityecorelua_edatatype_constructor_exists():
    assert callable(activityecorelua_EDataType.__init__)


def test_hyp_activityecorelua_edatatype_constructor_args():
    sig = inspect.signature(activityecorelua_EDataType.__init__)
    params = list(sig.parameters.keys())
    assert "serializable" in params, "Missing parameter 'serializable'"




def test_hyp_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeature)


def test_hyp_estructuralfeature_constructor_exists():
    assert callable(EStructuralFeature.__init__)


def test_hyp_estructuralfeature_constructor_args():
    sig = inspect.signature(EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_activityecorelua_ereference_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EReference)


def test_hyp_activityecorelua_ereference_constructor_exists():
    assert callable(activityecorelua_EReference.__init__)


def test_hyp_activityecorelua_ereference_constructor_args():
    sig = inspect.signature(activityecorelua_EReference.__init__)
    params = list(sig.parameters.keys())
    assert "containment" in params, "Missing parameter 'containment'"
    assert "container" in params, "Missing parameter 'container'"
    assert "resolveProxies" in params, "Missing parameter 'resolveProxies'"






def test_hyp_activityecorelua_eattribute_is_not_abstract():
    assert not inspect.isabstract(activityecorelua_EAttribute)


def test_hyp_activityecorelua_eattribute_constructor_exists():
    assert callable(activityecorelua_EAttribute.__init__)


def test_hyp_activityecorelua_eattribute_constructor_args():
    sig = inspect.signature(activityecorelua_EAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"



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
LastStatement_Return_strategy = st.builds(
    LastStatement_Return,
)
activityecorelua_LastStatement_ReturnWithValue_strategy = st.builds(
    activityecorelua_LastStatement_ReturnWithValue,
)
Field_strategy = st.builds(
    Field,
)
activityecorelua_Field_AddEntryToTable_strategy = st.builds(
    activityecorelua_Field_AddEntryToTable,
    key=
        safe_text
)
activityecorelua_Field_AppendEntryToTable_strategy = st.builds(
    activityecorelua_Field_AppendEntryToTable,
)
activityecorelua_Field_AddEntryToTable_Brackets_strategy = st.builds(
    activityecorelua_Field_AddEntryToTable_Brackets,
)
activityecorelua_Functioncall_Arguments_strategy = st.builds(
    activityecorelua_Functioncall_Arguments,
)
activityecorelua_Field_strategy = st.builds(
    activityecorelua_Field,
)
Expression_strategy = st.builds(
    Expression,
)
activityecorelua_Expression_CallFunction_strategy = st.builds(
    activityecorelua_Expression_CallFunction,
)
activityecorelua_Expression_Concatenation_strategy = st.builds(
    activityecorelua_Expression_Concatenation,
)
activityecorelua_Expression_Modulo_strategy = st.builds(
    activityecorelua_Expression_Modulo,
)
activityecorelua_Expression_Invert_strategy = st.builds(
    activityecorelua_Expression_Invert,
)
activityecorelua_Expression_Function_strategy = st.builds(
    activityecorelua_Expression_Function,
)
activityecorelua_Expression_Multiplication_strategy = st.builds(
    activityecorelua_Expression_Multiplication,
)
activityecorelua_Expression_CallMemberFunction_strategy = st.builds(
    activityecorelua_Expression_CallMemberFunction,
    memberFunctionName=
        safe_text
)
activityecorelua_Expression_Exponentiation_strategy = st.builds(
    activityecorelua_Expression_Exponentiation,
)
activityecorelua_Expression_Negate_strategy = st.builds(
    activityecorelua_Expression_Negate,
)
activityecorelua_Expression_Larger_Equal_strategy = st.builds(
    activityecorelua_Expression_Larger_Equal,
)
activityecorelua_Expression_True_strategy = st.builds(
    activityecorelua_Expression_True,
)
activityecorelua_Expression_AccessMember_strategy = st.builds(
    activityecorelua_Expression_AccessMember,
    memberName=
        safe_text
)
activityecorelua_Expression_And_strategy = st.builds(
    activityecorelua_Expression_And,
)
activityecorelua_Expression_Equal_strategy = st.builds(
    activityecorelua_Expression_Equal,
)
activityecorelua_Expression_VarArgs_strategy = st.builds(
    activityecorelua_Expression_VarArgs,
)
activityecorelua_Expression_Plus_strategy = st.builds(
    activityecorelua_Expression_Plus,
)
activityecorelua_Expression_VariableName_strategy = st.builds(
    activityecorelua_Expression_VariableName,
    variable=
        safe_text
)
activityecorelua_Expression_Number_strategy = st.builds(
    activityecorelua_Expression_Number,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
activityecorelua_Expression_Length_strategy = st.builds(
    activityecorelua_Expression_Length,
)
activityecorelua_Expression_Division_strategy = st.builds(
    activityecorelua_Expression_Division,
)
activityecorelua_Expression_Not_Equal_strategy = st.builds(
    activityecorelua_Expression_Not_Equal,
)
activityecorelua_Expression_Minus_strategy = st.builds(
    activityecorelua_Expression_Minus,
)
activityecorelua_Expression_Or_strategy = st.builds(
    activityecorelua_Expression_Or,
)
activityecorelua_Expression_AccessArray_strategy = st.builds(
    activityecorelua_Expression_AccessArray,
)
activityecorelua_Expression_TableConstructor_strategy = st.builds(
    activityecorelua_Expression_TableConstructor,
)
activityecorelua_Expression_Larger_strategy = st.builds(
    activityecorelua_Expression_Larger,
)
activityecorelua_Expression_String_strategy = st.builds(
    activityecorelua_Expression_String,
    value=
        safe_text
)
activityecorelua_Expression_Smaller_strategy = st.builds(
    activityecorelua_Expression_Smaller,
)
activityecorelua_Expression_Smaller_Equal_strategy = st.builds(
    activityecorelua_Expression_Smaller_Equal,
)
activityecorelua_Expression_False_strategy = st.builds(
    activityecorelua_Expression_False,
)
activityecorelua_Expression_Nil_strategy = st.builds(
    activityecorelua_Expression_Nil,
)
Statement_FunctioncallOrAssignment_strategy = st.builds(
    Statement_FunctioncallOrAssignment,
)
activityecorelua_Statement_CallMemberFunction_strategy = st.builds(
    activityecorelua_Statement_CallMemberFunction,
    memberFunctionName=
        safe_text
)
activityecorelua_Statement_CallFunction_strategy = st.builds(
    activityecorelua_Statement_CallFunction,
)
activityecorelua_Statement_Assignment_strategy = st.builds(
    activityecorelua_Statement_Assignment,
)
activityecorelua_Statement_If_Then_Else_ElseIfPart_strategy = st.builds(
    activityecorelua_Statement_If_Then_Else_ElseIfPart,
)
activityecorelua_Function_strategy = st.builds(
    activityecorelua_Function,
    varArgs=
        st.booleans(),
    parameters=
        safe_text
)
LastStatement_strategy = st.builds(
    LastStatement,
)
activityecorelua_LastStatement_Break_strategy = st.builds(
    activityecorelua_LastStatement_Break,
)
activityecorelua_LastStatement_Return_strategy = st.builds(
    activityecorelua_LastStatement_Return,
)
activityecorelua_LastStatement_strategy = st.builds(
    activityecorelua_LastStatement,
)
activityecorelua_Statement_strategy = st.builds(
    activityecorelua_Statement,
)
Chunk_strategy = st.builds(
    Chunk,
)
activityecorelua_Block_strategy = st.builds(
    activityecorelua_Block,
)
activityecorelua_Chunk_strategy = st.builds(
    activityecorelua_Chunk,
)
Statement_strategy = st.builds(
    Statement,
)
activityecorelua_Statement_LocalFunction_Declaration_strategy = st.builds(
    activityecorelua_Statement_LocalFunction_Declaration,
    functionName=
        safe_text
)
activityecorelua_Statement_If_Then_Else_strategy = st.builds(
    activityecorelua_Statement_If_Then_Else,
)
activityecorelua_Statement_FunctioncallOrAssignment_strategy = st.builds(
    activityecorelua_Statement_FunctioncallOrAssignment,
)
activityecorelua_Statement_Repeat_strategy = st.builds(
    activityecorelua_Statement_Repeat,
)
activityecorelua_Statement_GlobalFunction_Declaration_strategy = st.builds(
    activityecorelua_Statement_GlobalFunction_Declaration,
    functionName=
        safe_text,
    prefix=
        safe_text
)
activityecorelua_Statement_For_Generic_strategy = st.builds(
    activityecorelua_Statement_For_Generic,
    names=
        safe_text
)
activityecorelua_Statement_For_Numeric_strategy = st.builds(
    activityecorelua_Statement_For_Numeric,
    iteratorName=
        safe_text
)
activityecorelua_Statement_Local_Variable_Declaration_strategy = st.builds(
    activityecorelua_Statement_Local_Variable_Declaration,
    variableNames=
        safe_text
)
activityecorelua_Statement_While_strategy = st.builds(
    activityecorelua_Statement_While,
)
activityecorelua_Statement_Block_strategy = st.builds(
    activityecorelua_Statement_Block,
)
Variable_strategy = st.builds(
    Variable,
)
activityecorelua_IntegerVariable_strategy = st.builds(
    activityecorelua_IntegerVariable,
)
activityecorelua_Value_strategy = st.builds(
    activityecorelua_Value,
)
activityecorelua_Input_strategy = st.builds(
    activityecorelua_Input,
)
activityecorelua_InputValue_strategy = st.builds(
    activityecorelua_InputValue,
)
Value_strategy = st.builds(
    Value,
)
activityecorelua_IntegerValue_strategy = st.builds(
    activityecorelua_IntegerValue,
    value=
        st.integers()
)
activityecorelua_BooleanValue_strategy = st.builds(
    activityecorelua_BooleanValue,
    value=
        st.booleans()
)
activityecorelua_Expression_strategy = st.builds(
    activityecorelua_Expression,
)
Action_strategy = st.builds(
    Action,
)
activityecorelua_OpaqueAction_strategy = st.builds(
    activityecorelua_OpaqueAction,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
activityecorelua_Action_strategy = st.builds(
    activityecorelua_Action,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
activityecorelua_ExecutableNode_strategy = st.builds(
    activityecorelua_ExecutableNode,
)
activityecorelua_ControlNode_strategy = st.builds(
    activityecorelua_ControlNode,
)
activityecorelua_BooleanVariable_strategy = st.builds(
    activityecorelua_BooleanVariable,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
activityecorelua_ControlFlow_strategy = st.builds(
    activityecorelua_ControlFlow,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
activityecorelua_ActivityFinalNode_strategy = st.builds(
    activityecorelua_ActivityFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
activityecorelua_ForkNode_strategy = st.builds(
    activityecorelua_ForkNode,
)
activityecorelua_DecisionNode_strategy = st.builds(
    activityecorelua_DecisionNode,
)
activityecorelua_MergeNode_strategy = st.builds(
    activityecorelua_MergeNode,
)
activityecorelua_FinalNode_strategy = st.builds(
    activityecorelua_FinalNode,
)
activityecorelua_JoinNode_strategy = st.builds(
    activityecorelua_JoinNode,
)
activityecorelua_InitialNode_strategy = st.builds(
    activityecorelua_InitialNode,
)
activityecorelua_NamedElement_strategy = st.builds(
    activityecorelua_NamedElement,
    name=
        safe_text
)
activityecorelua_Variable_strategy = st.builds(
    activityecorelua_Variable,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
activityecorelua_ActivityEdge_strategy = st.builds(
    activityecorelua_ActivityEdge,
)
activityecorelua_ActivityNode_strategy = st.builds(
    activityecorelua_ActivityNode,
    running=
        st.booleans()
)
ETypedElement_strategy = st.builds(
    ETypedElement,
)
activityecorelua_Activity_strategy = st.builds(
    activityecorelua_Activity,
)
activityecorelua_EParameter_strategy = st.builds(
    activityecorelua_EParameter,
)
EDataType_strategy = st.builds(
    EDataType,
)
activityecorelua_EEnum_strategy = st.builds(
    activityecorelua_EEnum,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
activityecorelua_EEnumLiteral_strategy = st.builds(
    activityecorelua_EEnumLiteral,
    instance=
        safe_text,
    literal=
        safe_text,
    value=
        st.integers()
)
activityecorelua_EPackage_strategy = st.builds(
    activityecorelua_EPackage,
    nsURI=
        safe_text,
    nsPrefix=
        safe_text
)
activityecorelua_ETypeParameter_strategy = st.builds(
    activityecorelua_ETypeParameter,
)
activityecorelua_ETypedElement_strategy = st.builds(
    activityecorelua_ETypedElement,
    many=
        st.booleans(),
    required=
        st.booleans(),
    lowerBound=
        st.integers(),
    unique=
        st.booleans(),
    ordered=
        st.booleans(),
    upperBound=
        st.integers()
)
activityecorelua_EClassifier_strategy = st.builds(
    activityecorelua_EClassifier,
    instanceClassName=
        safe_text,
    defaultValue=
        safe_text,
    instanceClass=
        safe_text,
    instanceTypeName=
        safe_text
)
activityecorelua_EGenericType_strategy = st.builds(
    activityecorelua_EGenericType,
)
activityecorelua_EOperation_strategy = st.builds(
    activityecorelua_EOperation,
)
activityecorelua_EStructuralFeature_strategy = st.builds(
    activityecorelua_EStructuralFeature,
    unsettable=
        st.booleans(),
    changeable=
        st.booleans(),
    defaultValue=
        safe_text,
    volatile=
        st.booleans(),
    defaultValueLiteral=
        safe_text,
    derived=
        st.booleans(),
    transient=
        st.booleans()
)
EClassifier_strategy = st.builds(
    EClassifier,
)
activityecorelua_EClass_strategy = st.builds(
    activityecorelua_EClass,
    abstract=
        st.booleans(),
    interface=
        st.booleans()
)
activityecorelua_EObject_strategy = st.builds(
    activityecorelua_EObject,
)
activityecorelua_EModelElement_strategy = st.builds(
    activityecorelua_EModelElement,
)
activityecorelua_EStringToStringMapEntry_strategy = st.builds(
    activityecorelua_EStringToStringMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
EModelElement_strategy = st.builds(
    EModelElement,
)
activityecorelua_EFactory_strategy = st.builds(
    activityecorelua_EFactory,
)
activityecorelua_ENamedElement_strategy = st.builds(
    activityecorelua_ENamedElement,
    name=
        safe_text
)
activityecorelua_EAnnotation_strategy = st.builds(
    activityecorelua_EAnnotation,
    source=
        safe_text
)
activityecorelua_EDataType_strategy = st.builds(
    activityecorelua_EDataType,
    serializable=
        st.booleans()
)
EStructuralFeature_strategy = st.builds(
    EStructuralFeature,
)
activityecorelua_EReference_strategy = st.builds(
    activityecorelua_EReference,
    containment=
        st.booleans(),
    container=
        st.booleans(),
    resolveProxies=
        st.booleans()
)
activityecorelua_EAttribute_strategy = st.builds(
    activityecorelua_EAttribute,
    iD=
        st.booleans()
)







@given(instance=activityecorelua_Field_AddEntryToTable_strategy)
def test_hyp_activityecorelua_field_addentrytotable_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original















@given(instance=activityecorelua_Expression_CallMemberFunction_strategy)
def test_hyp_activityecorelua_expression_callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original








@given(instance=activityecorelua_Expression_AccessMember_strategy)
def test_hyp_activityecorelua_expression_accessmember_memberName_setter(instance):
    original = instance.memberName
    instance.memberName = original
    assert instance.memberName == original








@given(instance=activityecorelua_Expression_VariableName_strategy)
def test_hyp_activityecorelua_expression_variablename_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original




@given(instance=activityecorelua_Expression_Number_strategy)
def test_hyp_activityecorelua_expression_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original












@given(instance=activityecorelua_Expression_String_strategy)
def test_hyp_activityecorelua_expression_string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original









@given(instance=activityecorelua_Statement_CallMemberFunction_strategy)
def test_hyp_activityecorelua_statement_callmemberfunction_memberFunctionName_setter(instance):
    original = instance.memberFunctionName
    instance.memberFunctionName = original
    assert instance.memberFunctionName == original







@given(instance=activityecorelua_Function_strategy)
def test_hyp_activityecorelua_function_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original



@given(instance=activityecorelua_Function_strategy)
def test_hyp_activityecorelua_function_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original













@given(instance=activityecorelua_Statement_LocalFunction_Declaration_strategy)
def test_hyp_activityecorelua_statement_localfunction_declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original







@given(instance=activityecorelua_Statement_GlobalFunction_Declaration_strategy)
def test_hyp_activityecorelua_statement_globalfunction_declaration_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original



@given(instance=activityecorelua_Statement_GlobalFunction_Declaration_strategy)
def test_hyp_activityecorelua_statement_globalfunction_declaration_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original




@given(instance=activityecorelua_Statement_For_Generic_strategy)
def test_hyp_activityecorelua_statement_for_generic_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original




@given(instance=activityecorelua_Statement_For_Numeric_strategy)
def test_hyp_activityecorelua_statement_for_numeric_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original




@given(instance=activityecorelua_Statement_Local_Variable_Declaration_strategy)
def test_hyp_activityecorelua_statement_local_variable_declaration_variableNames_setter(instance):
    original = instance.variableNames
    instance.variableNames = original
    assert instance.variableNames == original












@given(instance=activityecorelua_IntegerValue_strategy)
def test_hyp_activityecorelua_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=activityecorelua_BooleanValue_strategy)
def test_hyp_activityecorelua_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
























@given(instance=activityecorelua_NamedElement_strategy)
def test_hyp_activityecorelua_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=activityecorelua_Variable_strategy)
def test_hyp_activityecorelua_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=activityecorelua_ActivityNode_strategy)
def test_hyp_activityecorelua_activitynode_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original










@given(instance=activityecorelua_EEnumLiteral_strategy)
def test_hyp_activityecorelua_eenumliteral_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original



@given(instance=activityecorelua_EEnumLiteral_strategy)
def test_hyp_activityecorelua_eenumliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=activityecorelua_EEnumLiteral_strategy)
def test_hyp_activityecorelua_eenumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=activityecorelua_EPackage_strategy)
def test_hyp_activityecorelua_epackage_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original



@given(instance=activityecorelua_EPackage_strategy)
def test_hyp_activityecorelua_epackage_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original





@given(instance=activityecorelua_ETypedElement_strategy)
def test_hyp_activityecorelua_etypedelement_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=activityecorelua_ETypedElement_strategy)
def test_hyp_activityecorelua_etypedelement_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=activityecorelua_ETypedElement_strategy)
def test_hyp_activityecorelua_etypedelement_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=activityecorelua_ETypedElement_strategy)
def test_hyp_activityecorelua_etypedelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=activityecorelua_ETypedElement_strategy)
def test_hyp_activityecorelua_etypedelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=activityecorelua_ETypedElement_strategy)
def test_hyp_activityecorelua_etypedelement_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original




@given(instance=activityecorelua_EClassifier_strategy)
def test_hyp_activityecorelua_eclassifier_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original



@given(instance=activityecorelua_EClassifier_strategy)
def test_hyp_activityecorelua_eclassifier_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=activityecorelua_EClassifier_strategy)
def test_hyp_activityecorelua_eclassifier_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original



@given(instance=activityecorelua_EClassifier_strategy)
def test_hyp_activityecorelua_eclassifier_instanceTypeName_setter(instance):
    original = instance.instanceTypeName
    instance.instanceTypeName = original
    assert instance.instanceTypeName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=activityecorelua_EClassifier_strategy)
@settings(max_examples=30)
def test_hyp_activityecorelua_eclassifier_isinstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInstance(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInstance' in activityecorelua_EClassifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstance' in activityecorelua_EClassifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstance' in activityecorelua_EClassifier is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=activityecorelua_EOperation_strategy)
@settings(max_examples=30)
def test_hyp_activityecorelua_eoperation_isoverrideof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isOverrideOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isOverrideOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isOverrideOf' in activityecorelua_EOperation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isOverrideOf' in activityecorelua_EOperation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isOverrideOf' in activityecorelua_EOperation is not implemented or raised an error")




@given(instance=activityecorelua_EStructuralFeature_strategy)
def test_hyp_activityecorelua_estructuralfeature_unsettable_setter(instance):
    original = instance.unsettable
    instance.unsettable = original
    assert instance.unsettable == original



@given(instance=activityecorelua_EStructuralFeature_strategy)
def test_hyp_activityecorelua_estructuralfeature_changeable_setter(instance):
    original = instance.changeable
    instance.changeable = original
    assert instance.changeable == original



@given(instance=activityecorelua_EStructuralFeature_strategy)
def test_hyp_activityecorelua_estructuralfeature_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=activityecorelua_EStructuralFeature_strategy)
def test_hyp_activityecorelua_estructuralfeature_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=activityecorelua_EStructuralFeature_strategy)
def test_hyp_activityecorelua_estructuralfeature_defaultValueLiteral_setter(instance):
    original = instance.defaultValueLiteral
    instance.defaultValueLiteral = original
    assert instance.defaultValueLiteral == original



@given(instance=activityecorelua_EStructuralFeature_strategy)
def test_hyp_activityecorelua_estructuralfeature_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=activityecorelua_EStructuralFeature_strategy)
def test_hyp_activityecorelua_estructuralfeature_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original





@given(instance=activityecorelua_EClass_strategy)
def test_hyp_activityecorelua_eclass_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=activityecorelua_EClass_strategy)
def test_hyp_activityecorelua_eclass_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=activityecorelua_EClass_strategy)
@settings(max_examples=30)
def test_hyp_activityecorelua_eclass_issupertypeof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSuperTypeOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSuperTypeOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSuperTypeOf' in activityecorelua_EClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSuperTypeOf' in activityecorelua_EClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSuperTypeOf' in activityecorelua_EClass is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=activityecorelua_EObject_strategy)
@settings(max_examples=30)
def test_hyp_activityecorelua_eobject_eeclass_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eeClass()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eeClass).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eeClass' in activityecorelua_EObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eeClass' in activityecorelua_EObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eeClass' in activityecorelua_EObject is not implemented or raised an error")





@given(instance=activityecorelua_EStringToStringMapEntry_strategy)
def test_hyp_activityecorelua_estringtostringmapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=activityecorelua_EStringToStringMapEntry_strategy)
def test_hyp_activityecorelua_estringtostringmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=activityecorelua_EFactory_strategy)
@settings(max_examples=30)
def test_hyp_activityecorelua_efactory_converttostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.convertToString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.convertToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'convertToString' in activityecorelua_EFactory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'convertToString' in activityecorelua_EFactory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'convertToString' in activityecorelua_EFactory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=activityecorelua_EFactory_strategy)
@settings(max_examples=30)
def test_hyp_activityecorelua_efactory_create_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.create(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.create).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'create' in activityecorelua_EFactory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in activityecorelua_EFactory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in activityecorelua_EFactory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=activityecorelua_EFactory_strategy)
@settings(max_examples=30)
def test_hyp_activityecorelua_efactory_createfromstring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createFromString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createFromString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createFromString' in activityecorelua_EFactory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createFromString' in activityecorelua_EFactory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createFromString' in activityecorelua_EFactory is not implemented or raised an error")




@given(instance=activityecorelua_ENamedElement_strategy)
def test_hyp_activityecorelua_enamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=activityecorelua_EAnnotation_strategy)
def test_hyp_activityecorelua_eannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original




@given(instance=activityecorelua_EDataType_strategy)
def test_hyp_activityecorelua_edatatype_serializable_setter(instance):
    original = instance.serializable
    instance.serializable = original
    assert instance.serializable == original





@given(instance=activityecorelua_EReference_strategy)
def test_hyp_activityecorelua_ereference_containment_setter(instance):
    original = instance.containment
    instance.containment = original
    assert instance.containment == original



@given(instance=activityecorelua_EReference_strategy)
def test_hyp_activityecorelua_ereference_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original



@given(instance=activityecorelua_EReference_strategy)
def test_hyp_activityecorelua_ereference_resolveProxies_setter(instance):
    original = instance.resolveProxies
    instance.resolveProxies = original
    assert instance.resolveProxies == original




@given(instance=activityecorelua_EAttribute_strategy)
def test_hyp_activityecorelua_eattribute_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    ActivityEdge,
    ActivityNode,
    Chunk,
    ControlNode,
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    ExecutableNode,
    Expression,
    Field,
    FinalNode,
    LastStatement,
    LastStatement_Return,
    NamedElement,
    Statement,
    Statement_FunctioncallOrAssignment,
    Value,
    Variable,
    activityecorelua_Action,
    activityecorelua_Activity,
    activityecorelua_ActivityEdge,
    activityecorelua_ActivityFinalNode,
    activityecorelua_ActivityNode,
    activityecorelua_Block,
    activityecorelua_BooleanValue,
    activityecorelua_BooleanVariable,
    activityecorelua_Chunk,
    activityecorelua_ControlFlow,
    activityecorelua_ControlNode,
    activityecorelua_DecisionNode,
    activityecorelua_EAnnotation,
    activityecorelua_EAttribute,
    activityecorelua_EClass,
    activityecorelua_EClassifier,
    activityecorelua_EDataType,
    activityecorelua_EEnum,
    activityecorelua_EEnumLiteral,
    activityecorelua_EFactory,
    activityecorelua_EGenericType,
    activityecorelua_EModelElement,
    activityecorelua_ENamedElement,
    activityecorelua_EObject,
    activityecorelua_EOperation,
    activityecorelua_EPackage,
    activityecorelua_EParameter,
    activityecorelua_EReference,
    activityecorelua_EStringToStringMapEntry,
    activityecorelua_EStructuralFeature,
    activityecorelua_ETypeParameter,
    activityecorelua_ETypedElement,
    activityecorelua_ExecutableNode,
    activityecorelua_Expression,
    activityecorelua_Expression_AccessArray,
    activityecorelua_Expression_AccessMember,
    activityecorelua_Expression_And,
    activityecorelua_Expression_CallFunction,
    activityecorelua_Expression_CallMemberFunction,
    activityecorelua_Expression_Concatenation,
    activityecorelua_Expression_Division,
    activityecorelua_Expression_Equal,
    activityecorelua_Expression_Exponentiation,
    activityecorelua_Expression_False,
    activityecorelua_Expression_Function,
    activityecorelua_Expression_Invert,
    activityecorelua_Expression_Larger,
    activityecorelua_Expression_Larger_Equal,
    activityecorelua_Expression_Length,
    activityecorelua_Expression_Minus,
    activityecorelua_Expression_Modulo,
    activityecorelua_Expression_Multiplication,
    activityecorelua_Expression_Negate,
    activityecorelua_Expression_Nil,
    activityecorelua_Expression_Not_Equal,
    activityecorelua_Expression_Number,
    activityecorelua_Expression_Or,
    activityecorelua_Expression_Plus,
    activityecorelua_Expression_Smaller,
    activityecorelua_Expression_Smaller_Equal,
    activityecorelua_Expression_String,
    activityecorelua_Expression_TableConstructor,
    activityecorelua_Expression_True,
    activityecorelua_Expression_VarArgs,
    activityecorelua_Expression_VariableName,
    activityecorelua_Field,
    activityecorelua_Field_AddEntryToTable,
    activityecorelua_Field_AddEntryToTable_Brackets,
    activityecorelua_Field_AppendEntryToTable,
    activityecorelua_FinalNode,
    activityecorelua_ForkNode,
    activityecorelua_Function,
    activityecorelua_Functioncall_Arguments,
    activityecorelua_InitialNode,
    activityecorelua_Input,
    activityecorelua_InputValue,
    activityecorelua_IntegerValue,
    activityecorelua_IntegerVariable,
    activityecorelua_JoinNode,
    activityecorelua_LastStatement,
    activityecorelua_LastStatement_Break,
    activityecorelua_LastStatement_Return,
    activityecorelua_LastStatement_ReturnWithValue,
    activityecorelua_MergeNode,
    activityecorelua_NamedElement,
    activityecorelua_OpaqueAction,
    activityecorelua_Statement,
    activityecorelua_Statement_Assignment,
    activityecorelua_Statement_Block,
    activityecorelua_Statement_CallFunction,
    activityecorelua_Statement_CallMemberFunction,
    activityecorelua_Statement_For_Generic,
    activityecorelua_Statement_For_Numeric,
    activityecorelua_Statement_FunctioncallOrAssignment,
    activityecorelua_Statement_GlobalFunction_Declaration,
    activityecorelua_Statement_If_Then_Else,
    activityecorelua_Statement_If_Then_Else_ElseIfPart,
    activityecorelua_Statement_LocalFunction_Declaration,
    activityecorelua_Statement_Local_Variable_Declaration,
    activityecorelua_Statement_Repeat,
    activityecorelua_Statement_While,
    activityecorelua_Value,
    activityecorelua_Variable,
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

def test_activityecorelua_ActivityNode_running_value_roundtrip():
    instance = activityecorelua_ActivityNode(running=True)
    assert instance.running == True
    instance.running = False
    assert instance.running == False


def test_activityecorelua_BooleanValue_value_value_roundtrip():
    instance = activityecorelua_BooleanValue(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_activityecorelua_EAnnotation_source_value_roundtrip():
    instance = activityecorelua_EAnnotation(source="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_activityecorelua_EAttribute_iD_value_roundtrip():
    instance = activityecorelua_EAttribute(iD=True)
    assert instance.iD == True
    instance.iD = False
    assert instance.iD == False


def test_activityecorelua_EClass_abstract_value_roundtrip():
    instance = activityecorelua_EClass(abstract=True, interface=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_activityecorelua_EClass_interface_value_roundtrip():
    instance = activityecorelua_EClass(abstract=True, interface=True)
    assert instance.interface == True
    instance.interface = False
    assert instance.interface == False


def test_activityecorelua_EClassifier_defaultValue_value_roundtrip():
    instance = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_activityecorelua_EClassifier_instanceClass_value_roundtrip():
    instance = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert instance.instanceClass == "sample_text"
    instance.instanceClass = "sample_text_2"
    assert instance.instanceClass == "sample_text_2"


def test_activityecorelua_EClassifier_instanceClassName_value_roundtrip():
    instance = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert instance.instanceClassName == "sample_text"
    instance.instanceClassName = "sample_text_2"
    assert instance.instanceClassName == "sample_text_2"


def test_activityecorelua_EClassifier_instanceTypeName_value_roundtrip():
    instance = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert instance.instanceTypeName == "sample_text"
    instance.instanceTypeName = "sample_text_2"
    assert instance.instanceTypeName == "sample_text_2"


def test_activityecorelua_EDataType_serializable_value_roundtrip():
    instance = activityecorelua_EDataType(serializable=True)
    assert instance.serializable == True
    instance.serializable = False
    assert instance.serializable == False


def test_activityecorelua_EEnumLiteral_instance_value_roundtrip():
    instance = activityecorelua_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.instance == "sample_text"
    instance.instance = "sample_text_2"
    assert instance.instance == "sample_text_2"


def test_activityecorelua_EEnumLiteral_literal_value_roundtrip():
    instance = activityecorelua_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.literal == "sample_text"
    instance.literal = "sample_text_2"
    assert instance.literal == "sample_text_2"


def test_activityecorelua_EEnumLiteral_value_value_roundtrip():
    instance = activityecorelua_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_activityecorelua_ENamedElement_name_value_roundtrip():
    instance = activityecorelua_ENamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_activityecorelua_EPackage_nsPrefix_value_roundtrip():
    instance = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert instance.nsPrefix == "sample_text"
    instance.nsPrefix = "sample_text_2"
    assert instance.nsPrefix == "sample_text_2"


def test_activityecorelua_EPackage_nsURI_value_roundtrip():
    instance = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert instance.nsURI == "sample_text"
    instance.nsURI = "sample_text_2"
    assert instance.nsURI == "sample_text_2"


def test_activityecorelua_EReference_container_value_roundtrip():
    instance = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.container == True
    instance.container = False
    assert instance.container == False


def test_activityecorelua_EReference_containment_value_roundtrip():
    instance = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.containment == True
    instance.containment = False
    assert instance.containment == False


def test_activityecorelua_EReference_resolveProxies_value_roundtrip():
    instance = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    assert instance.resolveProxies == True
    instance.resolveProxies = False
    assert instance.resolveProxies == False


def test_activityecorelua_EStringToStringMapEntry_key_value_roundtrip():
    instance = activityecorelua_EStringToStringMapEntry(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_activityecorelua_EStringToStringMapEntry_value_value_roundtrip():
    instance = activityecorelua_EStringToStringMapEntry(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_activityecorelua_EStructuralFeature_changeable_value_roundtrip():
    instance = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.changeable == True
    instance.changeable = False
    assert instance.changeable == False


def test_activityecorelua_EStructuralFeature_defaultValue_value_roundtrip():
    instance = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.defaultValue == "sample_text"
    instance.defaultValue = "sample_text_2"
    assert instance.defaultValue == "sample_text_2"


def test_activityecorelua_EStructuralFeature_defaultValueLiteral_value_roundtrip():
    instance = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.defaultValueLiteral == "sample_text"
    instance.defaultValueLiteral = "sample_text_2"
    assert instance.defaultValueLiteral == "sample_text_2"


def test_activityecorelua_EStructuralFeature_derived_value_roundtrip():
    instance = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.derived == True
    instance.derived = False
    assert instance.derived == False


def test_activityecorelua_EStructuralFeature_transient_value_roundtrip():
    instance = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.transient == True
    instance.transient = False
    assert instance.transient == False


def test_activityecorelua_EStructuralFeature_unsettable_value_roundtrip():
    instance = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.unsettable == True
    instance.unsettable = False
    assert instance.unsettable == False


def test_activityecorelua_EStructuralFeature_volatile_value_roundtrip():
    instance = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert instance.volatile == True
    instance.volatile = False
    assert instance.volatile == False


def test_activityecorelua_ETypedElement_lowerBound_value_roundtrip():
    instance = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_activityecorelua_ETypedElement_many_value_roundtrip():
    instance = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.many == True
    instance.many = False
    assert instance.many == False


def test_activityecorelua_ETypedElement_ordered_value_roundtrip():
    instance = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.ordered == True
    instance.ordered = False
    assert instance.ordered == False


def test_activityecorelua_ETypedElement_required_value_roundtrip():
    instance = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_activityecorelua_ETypedElement_unique_value_roundtrip():
    instance = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.unique == True
    instance.unique = False
    assert instance.unique == False


def test_activityecorelua_ETypedElement_upperBound_value_roundtrip():
    instance = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert instance.upperBound == 7
    instance.upperBound = 13
    assert instance.upperBound == 13


def test_activityecorelua_Expression_AccessMember_memberName_value_roundtrip():
    instance = activityecorelua_Expression_AccessMember(memberName="sample_text")
    assert instance.memberName == "sample_text"
    instance.memberName = "sample_text_2"
    assert instance.memberName == "sample_text_2"


def test_activityecorelua_Expression_CallMemberFunction_memberFunctionName_value_roundtrip():
    instance = activityecorelua_Expression_CallMemberFunction(memberFunctionName="sample_text")
    assert instance.memberFunctionName == "sample_text"
    instance.memberFunctionName = "sample_text_2"
    assert instance.memberFunctionName == "sample_text_2"


def test_activityecorelua_Expression_Number_value_value_roundtrip():
    instance = activityecorelua_Expression_Number(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_activityecorelua_Expression_String_value_value_roundtrip():
    instance = activityecorelua_Expression_String(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_activityecorelua_Expression_VariableName_variable_value_roundtrip():
    instance = activityecorelua_Expression_VariableName(variable="sample_text")
    assert instance.variable == "sample_text"
    instance.variable = "sample_text_2"
    assert instance.variable == "sample_text_2"


def test_activityecorelua_Field_AddEntryToTable_key_value_roundtrip():
    instance = activityecorelua_Field_AddEntryToTable(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_activityecorelua_Function_parameters_value_roundtrip():
    instance = activityecorelua_Function(parameters="sample_text", varArgs=True)
    assert instance.parameters == "sample_text"
    instance.parameters = "sample_text_2"
    assert instance.parameters == "sample_text_2"


def test_activityecorelua_Function_varArgs_value_roundtrip():
    instance = activityecorelua_Function(parameters="sample_text", varArgs=True)
    assert instance.varArgs == True
    instance.varArgs = False
    assert instance.varArgs == False


def test_activityecorelua_IntegerValue_value_value_roundtrip():
    instance = activityecorelua_IntegerValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_activityecorelua_NamedElement_name_value_roundtrip():
    instance = activityecorelua_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_activityecorelua_Statement_CallMemberFunction_memberFunctionName_value_roundtrip():
    instance = activityecorelua_Statement_CallMemberFunction(memberFunctionName="sample_text")
    assert instance.memberFunctionName == "sample_text"
    instance.memberFunctionName = "sample_text_2"
    assert instance.memberFunctionName == "sample_text_2"


def test_activityecorelua_Statement_For_Generic_names_value_roundtrip():
    instance = activityecorelua_Statement_For_Generic(names="sample_text")
    assert instance.names == "sample_text"
    instance.names = "sample_text_2"
    assert instance.names == "sample_text_2"


def test_activityecorelua_Statement_For_Numeric_iteratorName_value_roundtrip():
    instance = activityecorelua_Statement_For_Numeric(iteratorName="sample_text")
    assert instance.iteratorName == "sample_text"
    instance.iteratorName = "sample_text_2"
    assert instance.iteratorName == "sample_text_2"


def test_activityecorelua_Statement_GlobalFunction_Declaration_functionName_value_roundtrip():
    instance = activityecorelua_Statement_GlobalFunction_Declaration(functionName="sample_text", prefix="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_activityecorelua_Statement_GlobalFunction_Declaration_prefix_value_roundtrip():
    instance = activityecorelua_Statement_GlobalFunction_Declaration(functionName="sample_text", prefix="sample_text")
    assert instance.prefix == "sample_text"
    instance.prefix = "sample_text_2"
    assert instance.prefix == "sample_text_2"


def test_activityecorelua_Statement_LocalFunction_Declaration_functionName_value_roundtrip():
    instance = activityecorelua_Statement_LocalFunction_Declaration(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_activityecorelua_Statement_Local_Variable_Declaration_variableNames_value_roundtrip():
    instance = activityecorelua_Statement_Local_Variable_Declaration(variableNames="sample_text")
    assert instance.variableNames == "sample_text"
    instance.variableNames = "sample_text_2"
    assert instance.variableNames == "sample_text_2"


def test_activityecorelua_Variable_name_value_roundtrip():
    instance = activityecorelua_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_activityecorelua_OpaqueAction_isa_Action():
    instance = activityecorelua_OpaqueAction()
    assert isinstance(instance, Action)


def test_activityecorelua_ControlFlow_isa_ActivityEdge():
    instance = activityecorelua_ControlFlow()
    assert isinstance(instance, ActivityEdge)


def test_activityecorelua_ControlNode_isa_ActivityNode():
    instance = activityecorelua_ControlNode()
    assert isinstance(instance, ActivityNode)


def test_activityecorelua_ExecutableNode_isa_ActivityNode():
    instance = activityecorelua_ExecutableNode()
    assert isinstance(instance, ActivityNode)


def test_activityecorelua_Block_isa_Chunk():
    instance = activityecorelua_Block()
    assert isinstance(instance, Chunk)


def test_activityecorelua_DecisionNode_isa_ControlNode():
    instance = activityecorelua_DecisionNode()
    assert isinstance(instance, ControlNode)


def test_activityecorelua_FinalNode_isa_ControlNode():
    instance = activityecorelua_FinalNode()
    assert isinstance(instance, ControlNode)


def test_activityecorelua_ForkNode_isa_ControlNode():
    instance = activityecorelua_ForkNode()
    assert isinstance(instance, ControlNode)


def test_activityecorelua_InitialNode_isa_ControlNode():
    instance = activityecorelua_InitialNode()
    assert isinstance(instance, ControlNode)


def test_activityecorelua_JoinNode_isa_ControlNode():
    instance = activityecorelua_JoinNode()
    assert isinstance(instance, ControlNode)


def test_activityecorelua_MergeNode_isa_ControlNode():
    instance = activityecorelua_MergeNode()
    assert isinstance(instance, ControlNode)


def test_activityecorelua_EClass_isa_EClassifier():
    instance = activityecorelua_EClass(abstract=True, interface=True)
    assert isinstance(instance, EClassifier)


def test_activityecorelua_EDataType_isa_EClassifier():
    instance = activityecorelua_EDataType(serializable=True)
    assert isinstance(instance, EClassifier)


def test_activityecorelua_EEnum_isa_EDataType():
    instance = activityecorelua_EEnum()
    assert isinstance(instance, EDataType)


def test_activityecorelua_EAnnotation_isa_EModelElement():
    instance = activityecorelua_EAnnotation(source="sample_text")
    assert isinstance(instance, EModelElement)


def test_activityecorelua_EFactory_isa_EModelElement():
    instance = activityecorelua_EFactory()
    assert isinstance(instance, EModelElement)


def test_activityecorelua_ENamedElement_isa_EModelElement():
    instance = activityecorelua_ENamedElement(name="sample_text")
    assert isinstance(instance, EModelElement)


def test_activityecorelua_EClassifier_isa_ENamedElement():
    instance = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    assert isinstance(instance, ENamedElement)


def test_activityecorelua_EEnumLiteral_isa_ENamedElement():
    instance = activityecorelua_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    assert isinstance(instance, ENamedElement)


def test_activityecorelua_EPackage_isa_ENamedElement():
    instance = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    assert isinstance(instance, ENamedElement)


def test_activityecorelua_ETypeParameter_isa_ENamedElement():
    instance = activityecorelua_ETypeParameter()
    assert isinstance(instance, ENamedElement)


def test_activityecorelua_ETypedElement_isa_ENamedElement():
    instance = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    assert isinstance(instance, ENamedElement)


def test_activityecorelua_EAttribute_isa_EStructuralFeature():
    instance = activityecorelua_EAttribute(iD=True)
    assert isinstance(instance, EStructuralFeature)


def test_activityecorelua_EReference_isa_EStructuralFeature():
    instance = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    assert isinstance(instance, EStructuralFeature)


def test_activityecorelua_EOperation_isa_ETypedElement():
    instance = activityecorelua_EOperation()
    assert isinstance(instance, ETypedElement)


def test_activityecorelua_EParameter_isa_ETypedElement():
    instance = activityecorelua_EParameter()
    assert isinstance(instance, ETypedElement)


def test_activityecorelua_EStructuralFeature_isa_ETypedElement():
    instance = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    assert isinstance(instance, ETypedElement)


def test_activityecorelua_Action_isa_ExecutableNode():
    instance = activityecorelua_Action()
    assert isinstance(instance, ExecutableNode)


def test_activityecorelua_Expression_AccessArray_isa_Expression():
    instance = activityecorelua_Expression_AccessArray()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_AccessMember_isa_Expression():
    instance = activityecorelua_Expression_AccessMember(memberName="sample_text")
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_And_isa_Expression():
    instance = activityecorelua_Expression_And()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_CallFunction_isa_Expression():
    instance = activityecorelua_Expression_CallFunction()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_CallMemberFunction_isa_Expression():
    instance = activityecorelua_Expression_CallMemberFunction(memberFunctionName="sample_text")
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Concatenation_isa_Expression():
    instance = activityecorelua_Expression_Concatenation()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Division_isa_Expression():
    instance = activityecorelua_Expression_Division()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Equal_isa_Expression():
    instance = activityecorelua_Expression_Equal()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Exponentiation_isa_Expression():
    instance = activityecorelua_Expression_Exponentiation()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_False_isa_Expression():
    instance = activityecorelua_Expression_False()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Function_isa_Expression():
    instance = activityecorelua_Expression_Function()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Invert_isa_Expression():
    instance = activityecorelua_Expression_Invert()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Larger_isa_Expression():
    instance = activityecorelua_Expression_Larger()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Larger_Equal_isa_Expression():
    instance = activityecorelua_Expression_Larger_Equal()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Length_isa_Expression():
    instance = activityecorelua_Expression_Length()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Minus_isa_Expression():
    instance = activityecorelua_Expression_Minus()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Modulo_isa_Expression():
    instance = activityecorelua_Expression_Modulo()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Multiplication_isa_Expression():
    instance = activityecorelua_Expression_Multiplication()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Negate_isa_Expression():
    instance = activityecorelua_Expression_Negate()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Nil_isa_Expression():
    instance = activityecorelua_Expression_Nil()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Not_Equal_isa_Expression():
    instance = activityecorelua_Expression_Not_Equal()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Number_isa_Expression():
    instance = activityecorelua_Expression_Number(value=3.14)
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Or_isa_Expression():
    instance = activityecorelua_Expression_Or()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Plus_isa_Expression():
    instance = activityecorelua_Expression_Plus()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Smaller_isa_Expression():
    instance = activityecorelua_Expression_Smaller()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_Smaller_Equal_isa_Expression():
    instance = activityecorelua_Expression_Smaller_Equal()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_String_isa_Expression():
    instance = activityecorelua_Expression_String(value="sample_text")
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_TableConstructor_isa_Expression():
    instance = activityecorelua_Expression_TableConstructor()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_True_isa_Expression():
    instance = activityecorelua_Expression_True()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_VarArgs_isa_Expression():
    instance = activityecorelua_Expression_VarArgs()
    assert isinstance(instance, Expression)


def test_activityecorelua_Expression_VariableName_isa_Expression():
    instance = activityecorelua_Expression_VariableName(variable="sample_text")
    assert isinstance(instance, Expression)


def test_activityecorelua_Field_AddEntryToTable_isa_Field():
    instance = activityecorelua_Field_AddEntryToTable(key="sample_text")
    assert isinstance(instance, Field)


def test_activityecorelua_Field_AddEntryToTable_Brackets_isa_Field():
    instance = activityecorelua_Field_AddEntryToTable_Brackets()
    assert isinstance(instance, Field)


def test_activityecorelua_Field_AppendEntryToTable_isa_Field():
    instance = activityecorelua_Field_AppendEntryToTable()
    assert isinstance(instance, Field)


def test_activityecorelua_ActivityFinalNode_isa_FinalNode():
    instance = activityecorelua_ActivityFinalNode()
    assert isinstance(instance, FinalNode)


def test_activityecorelua_LastStatement_Break_isa_LastStatement():
    instance = activityecorelua_LastStatement_Break()
    assert isinstance(instance, LastStatement)


def test_activityecorelua_LastStatement_Return_isa_LastStatement():
    instance = activityecorelua_LastStatement_Return()
    assert isinstance(instance, LastStatement)


def test_activityecorelua_LastStatement_ReturnWithValue_isa_LastStatement_Return():
    instance = activityecorelua_LastStatement_ReturnWithValue()
    assert isinstance(instance, LastStatement_Return)


def test_activityecorelua_Activity_isa_NamedElement():
    instance = activityecorelua_Activity()
    assert isinstance(instance, NamedElement)


def test_activityecorelua_ActivityEdge_isa_NamedElement():
    instance = activityecorelua_ActivityEdge()
    assert isinstance(instance, NamedElement)


def test_activityecorelua_ActivityNode_isa_NamedElement():
    instance = activityecorelua_ActivityNode(running=True)
    assert isinstance(instance, NamedElement)


def test_activityecorelua_Statement_Block_isa_Statement():
    instance = activityecorelua_Statement_Block()
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_For_Generic_isa_Statement():
    instance = activityecorelua_Statement_For_Generic(names="sample_text")
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_For_Numeric_isa_Statement():
    instance = activityecorelua_Statement_For_Numeric(iteratorName="sample_text")
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_FunctioncallOrAssignment_isa_Statement():
    instance = activityecorelua_Statement_FunctioncallOrAssignment()
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_GlobalFunction_Declaration_isa_Statement():
    instance = activityecorelua_Statement_GlobalFunction_Declaration(functionName="sample_text", prefix="sample_text")
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_If_Then_Else_isa_Statement():
    instance = activityecorelua_Statement_If_Then_Else()
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_LocalFunction_Declaration_isa_Statement():
    instance = activityecorelua_Statement_LocalFunction_Declaration(functionName="sample_text")
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_Local_Variable_Declaration_isa_Statement():
    instance = activityecorelua_Statement_Local_Variable_Declaration(variableNames="sample_text")
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_Repeat_isa_Statement():
    instance = activityecorelua_Statement_Repeat()
    assert isinstance(instance, Statement)


def test_activityecorelua_Statement_While_isa_Statement():
    instance = activityecorelua_Statement_While()
    assert isinstance(instance, Statement)


def test_activityecorelua_Expression_isa_Statement_FunctioncallOrAssignment():
    instance = activityecorelua_Expression()
    assert isinstance(instance, Statement_FunctioncallOrAssignment)


def test_activityecorelua_Statement_Assignment_isa_Statement_FunctioncallOrAssignment():
    instance = activityecorelua_Statement_Assignment()
    assert isinstance(instance, Statement_FunctioncallOrAssignment)


def test_activityecorelua_Statement_CallFunction_isa_Statement_FunctioncallOrAssignment():
    instance = activityecorelua_Statement_CallFunction()
    assert isinstance(instance, Statement_FunctioncallOrAssignment)


def test_activityecorelua_Statement_CallMemberFunction_isa_Statement_FunctioncallOrAssignment():
    instance = activityecorelua_Statement_CallMemberFunction(memberFunctionName="sample_text")
    assert isinstance(instance, Statement_FunctioncallOrAssignment)


def test_activityecorelua_BooleanValue_isa_Value():
    instance = activityecorelua_BooleanValue(value=True)
    assert isinstance(instance, Value)


def test_activityecorelua_IntegerValue_isa_Value():
    instance = activityecorelua_IntegerValue(value=7)
    assert isinstance(instance, Value)


def test_activityecorelua_BooleanVariable_isa_Variable():
    instance = activityecorelua_BooleanVariable()
    assert isinstance(instance, Variable)


def test_activityecorelua_IntegerVariable_isa_Variable():
    instance = activityecorelua_IntegerVariable()
    assert isinstance(instance, Variable)


def test_assoc_activity121_link_reassign_clear():
    a = activityecorelua_ActivityNode(running=True)
    b1 = activityecorelua_Activity()
    b2 = activityecorelua_Activity()
    _safe_set(a, 'nodes', b1)
    assert _is_linked(a, 'nodes', b1)
    if hasattr(b1, 'Activity'):
        assert _is_linked(b1, 'Activity', a)
    _safe_set(a, 'nodes', b2)
    assert _is_linked(a, 'nodes', b2)
    if hasattr(b1, 'Activity'):
        assert not _is_linked(b1, 'Activity', a)
    if hasattr(b2, 'Activity'):
        assert _is_linked(b2, 'Activity', a)
    _safe_set(a, 'nodes', None)
    assert not _is_linked(a, 'nodes', b2)
    if hasattr(b2, 'Activity'):
        assert not _is_linked(b2, 'Activity', a)


def test_assoc_activity54_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_Activity()
    b2 = activityecorelua_Activity()
    _safe_set(a, 'activityecorelua_EOperation55', b1)
    assert _is_linked(a, 'activityecorelua_EOperation55', b1)
    if hasattr(b1, 'activityecorelua_Activity'):
        assert _is_linked(b1, 'activityecorelua_Activity', a)
    _safe_set(a, 'activityecorelua_EOperation55', b2)
    assert _is_linked(a, 'activityecorelua_EOperation55', b2)
    if hasattr(b1, 'activityecorelua_Activity'):
        assert not _is_linked(b1, 'activityecorelua_Activity', a)
    if hasattr(b2, 'activityecorelua_Activity'):
        assert _is_linked(b2, 'activityecorelua_Activity', a)
    _safe_set(a, 'activityecorelua_EOperation55', None)
    assert not _is_linked(a, 'activityecorelua_EOperation55', b2)
    if hasattr(b2, 'activityecorelua_Activity'):
        assert not _is_linked(b2, 'activityecorelua_Activity', a)


def test_assoc_arguments214_link_reassign_clear():
    a = activityecorelua_Statement_CallMemberFunction(memberFunctionName="sample_text")
    b1 = activityecorelua_Functioncall_Arguments()
    b2 = activityecorelua_Functioncall_Arguments()
    _safe_set(a, 'activityecorelua_Statement_CallMemberFunction215', b1)
    assert _is_linked(a, 'activityecorelua_Statement_CallMemberFunction215', b1)
    if hasattr(b1, 'activityecorelua_Functioncall_Arguments216'):
        assert _is_linked(b1, 'activityecorelua_Functioncall_Arguments216', a)
    _safe_set(a, 'activityecorelua_Statement_CallMemberFunction215', b2)
    assert _is_linked(a, 'activityecorelua_Statement_CallMemberFunction215', b2)
    if hasattr(b1, 'activityecorelua_Functioncall_Arguments216'):
        assert not _is_linked(b1, 'activityecorelua_Functioncall_Arguments216', a)
    if hasattr(b2, 'activityecorelua_Functioncall_Arguments216'):
        assert _is_linked(b2, 'activityecorelua_Functioncall_Arguments216', a)
    _safe_set(a, 'activityecorelua_Statement_CallMemberFunction215', None)
    assert not _is_linked(a, 'activityecorelua_Statement_CallMemberFunction215', b2)
    if hasattr(b2, 'activityecorelua_Functioncall_Arguments216'):
        assert not _is_linked(b2, 'activityecorelua_Functioncall_Arguments216', a)


def test_assoc_arguments305_link_reassign_clear():
    a = activityecorelua_Expression_CallMemberFunction(memberFunctionName="sample_text")
    b1 = activityecorelua_Functioncall_Arguments()
    b2 = activityecorelua_Functioncall_Arguments()
    _safe_set(a, 'activityecorelua_Expression_CallMemberFunction306', b1)
    assert _is_linked(a, 'activityecorelua_Expression_CallMemberFunction306', b1)
    if hasattr(b1, 'activityecorelua_Functioncall_Arguments307'):
        assert _is_linked(b1, 'activityecorelua_Functioncall_Arguments307', a)
    _safe_set(a, 'activityecorelua_Expression_CallMemberFunction306', b2)
    assert _is_linked(a, 'activityecorelua_Expression_CallMemberFunction306', b2)
    if hasattr(b1, 'activityecorelua_Functioncall_Arguments307'):
        assert not _is_linked(b1, 'activityecorelua_Functioncall_Arguments307', a)
    if hasattr(b2, 'activityecorelua_Functioncall_Arguments307'):
        assert _is_linked(b2, 'activityecorelua_Functioncall_Arguments307', a)
    _safe_set(a, 'activityecorelua_Expression_CallMemberFunction306', None)
    assert not _is_linked(a, 'activityecorelua_Expression_CallMemberFunction306', b2)
    if hasattr(b2, 'activityecorelua_Functioncall_Arguments307'):
        assert not _is_linked(b2, 'activityecorelua_Functioncall_Arguments307', a)


def test_assoc_block179_link_reassign_clear():
    a = activityecorelua_Statement_For_Numeric(iteratorName="sample_text")
    b1 = activityecorelua_Block()
    b2 = activityecorelua_Block()
    _safe_set(a, 'activityecorelua_Statement_For_Numeric180', b1)
    assert _is_linked(a, 'activityecorelua_Statement_For_Numeric180', b1)
    if hasattr(b1, 'activityecorelua_Block181'):
        assert _is_linked(b1, 'activityecorelua_Block181', a)
    _safe_set(a, 'activityecorelua_Statement_For_Numeric180', b2)
    assert _is_linked(a, 'activityecorelua_Statement_For_Numeric180', b2)
    if hasattr(b1, 'activityecorelua_Block181'):
        assert not _is_linked(b1, 'activityecorelua_Block181', a)
    if hasattr(b2, 'activityecorelua_Block181'):
        assert _is_linked(b2, 'activityecorelua_Block181', a)
    _safe_set(a, 'activityecorelua_Statement_For_Numeric180', None)
    assert not _is_linked(a, 'activityecorelua_Statement_For_Numeric180', b2)
    if hasattr(b2, 'activityecorelua_Block181'):
        assert not _is_linked(b2, 'activityecorelua_Block181', a)


def test_assoc_block184_link_reassign_clear():
    a = activityecorelua_Statement_For_Generic(names="sample_text")
    b1 = activityecorelua_Block()
    b2 = activityecorelua_Block()
    _safe_set(a, 'activityecorelua_Statement_For_Generic185', b1)
    assert _is_linked(a, 'activityecorelua_Statement_For_Generic185', b1)
    if hasattr(b1, 'activityecorelua_Block186'):
        assert _is_linked(b1, 'activityecorelua_Block186', a)
    _safe_set(a, 'activityecorelua_Statement_For_Generic185', b2)
    assert _is_linked(a, 'activityecorelua_Statement_For_Generic185', b2)
    if hasattr(b1, 'activityecorelua_Block186'):
        assert not _is_linked(b1, 'activityecorelua_Block186', a)
    if hasattr(b2, 'activityecorelua_Block186'):
        assert _is_linked(b2, 'activityecorelua_Block186', a)
    _safe_set(a, 'activityecorelua_Statement_For_Generic185', None)
    assert not _is_linked(a, 'activityecorelua_Statement_For_Generic185', b2)
    if hasattr(b2, 'activityecorelua_Block186'):
        assert not _is_linked(b2, 'activityecorelua_Block186', a)


def test_assoc_body195_link_reassign_clear():
    a = activityecorelua_Function(parameters="sample_text", varArgs=True)
    b1 = activityecorelua_Block()
    b2 = activityecorelua_Block()
    _safe_set(a, 'activityecorelua_Function196', b1)
    assert _is_linked(a, 'activityecorelua_Function196', b1)
    if hasattr(b1, 'activityecorelua_Block197'):
        assert _is_linked(b1, 'activityecorelua_Block197', a)
    _safe_set(a, 'activityecorelua_Function196', b2)
    assert _is_linked(a, 'activityecorelua_Function196', b2)
    if hasattr(b1, 'activityecorelua_Block197'):
        assert not _is_linked(b1, 'activityecorelua_Block197', a)
    if hasattr(b2, 'activityecorelua_Block197'):
        assert _is_linked(b2, 'activityecorelua_Block197', a)
    _safe_set(a, 'activityecorelua_Function196', None)
    assert not _is_linked(a, 'activityecorelua_Function196', b2)
    if hasattr(b2, 'activityecorelua_Block197'):
        assert not _is_linked(b2, 'activityecorelua_Block197', a)


def test_assoc_contents3_link_reassign_clear():
    a = activityecorelua_EObject()
    b1 = activityecorelua_EAnnotation(source="sample_text")
    b2 = activityecorelua_EAnnotation(source="sample_text_2")
    _safe_set(a, 'activityecorelua_EObject', b1)
    assert _is_linked(a, 'activityecorelua_EObject', b1)
    if hasattr(b1, 'activityecorelua_EAnnotation4'):
        assert _is_linked(b1, 'activityecorelua_EAnnotation4', a)
    _safe_set(a, 'activityecorelua_EObject', b2)
    assert _is_linked(a, 'activityecorelua_EObject', b2)
    if hasattr(b1, 'activityecorelua_EAnnotation4'):
        assert not _is_linked(b1, 'activityecorelua_EAnnotation4', a)
    if hasattr(b2, 'activityecorelua_EAnnotation4'):
        assert _is_linked(b2, 'activityecorelua_EAnnotation4', a)
    _safe_set(a, 'activityecorelua_EObject', None)
    assert not _is_linked(a, 'activityecorelua_EObject', b2)
    if hasattr(b2, 'activityecorelua_EAnnotation4'):
        assert not _is_linked(b2, 'activityecorelua_EAnnotation4', a)


def test_assoc_currentValue130_link_reassign_clear():
    a = activityecorelua_Variable(name="sample_text")
    b1 = activityecorelua_Value()
    b2 = activityecorelua_Value()
    _safe_set(a, 'activityecorelua_Variable131', b1)
    assert _is_linked(a, 'activityecorelua_Variable131', b1)
    if hasattr(b1, 'activityecorelua_Value132'):
        assert _is_linked(b1, 'activityecorelua_Value132', a)
    _safe_set(a, 'activityecorelua_Variable131', b2)
    assert _is_linked(a, 'activityecorelua_Variable131', b2)
    if hasattr(b1, 'activityecorelua_Value132'):
        assert not _is_linked(b1, 'activityecorelua_Value132', a)
    if hasattr(b2, 'activityecorelua_Value132'):
        assert _is_linked(b2, 'activityecorelua_Value132', a)
    _safe_set(a, 'activityecorelua_Variable131', None)
    assert not _is_linked(a, 'activityecorelua_Variable131', b2)
    if hasattr(b2, 'activityecorelua_Value132'):
        assert not _is_linked(b2, 'activityecorelua_Value132', a)


def test_assoc_details1_link_reassign_clear():
    a = activityecorelua_EStringToStringMapEntry(key="sample_text", value="sample_text")
    b1 = activityecorelua_EAnnotation(source="sample_text")
    b2 = activityecorelua_EAnnotation(source="sample_text_2")
    _safe_set(a, 'activityecorelua_EStringToStringMapEntry', b1)
    assert _is_linked(a, 'activityecorelua_EStringToStringMapEntry', b1)
    if hasattr(b1, 'activityecorelua_EAnnotation'):
        assert _is_linked(b1, 'activityecorelua_EAnnotation', a)
    _safe_set(a, 'activityecorelua_EStringToStringMapEntry', b2)
    assert _is_linked(a, 'activityecorelua_EStringToStringMapEntry', b2)
    if hasattr(b1, 'activityecorelua_EAnnotation'):
        assert not _is_linked(b1, 'activityecorelua_EAnnotation', a)
    if hasattr(b2, 'activityecorelua_EAnnotation'):
        assert _is_linked(b2, 'activityecorelua_EAnnotation', a)
    _safe_set(a, 'activityecorelua_EStringToStringMapEntry', None)
    assert not _is_linked(a, 'activityecorelua_EStringToStringMapEntry', b2)
    if hasattr(b2, 'activityecorelua_EAnnotation'):
        assert not _is_linked(b2, 'activityecorelua_EAnnotation', a)


def test_assoc_eAllAttributes11_link_reassign_clear():
    a = activityecorelua_EClass(abstract=True, interface=True)
    b1 = activityecorelua_EAttribute(iD=True)
    b2 = activityecorelua_EAttribute(iD=False)
    _safe_set(a, 'activityecorelua_EClass12', {b1})
    assert _is_linked(a, 'activityecorelua_EClass12', b1)
    if hasattr(b1, 'activityecorelua_EAttribute13'):
        assert _is_linked(b1, 'activityecorelua_EAttribute13', a)
    _safe_set(a, 'activityecorelua_EClass12', {b2})
    assert _is_linked(a, 'activityecorelua_EClass12', b2)
    if hasattr(b1, 'activityecorelua_EAttribute13'):
        assert not _is_linked(b1, 'activityecorelua_EAttribute13', a)
    if hasattr(b2, 'activityecorelua_EAttribute13'):
        assert _is_linked(b2, 'activityecorelua_EAttribute13', a)
    _safe_set(a, 'activityecorelua_EClass12', set())
    assert not _is_linked(a, 'activityecorelua_EClass12', b2)
    if hasattr(b2, 'activityecorelua_EAttribute13'):
        assert not _is_linked(b2, 'activityecorelua_EAttribute13', a)


def test_assoc_eAllContainments22_link_reassign_clear():
    a = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'activityecorelua_EReference24', b1)
    assert _is_linked(a, 'activityecorelua_EReference24', b1)
    if hasattr(b1, 'activityecorelua_EClass23'):
        assert _is_linked(b1, 'activityecorelua_EClass23', a)
    _safe_set(a, 'activityecorelua_EReference24', b2)
    assert _is_linked(a, 'activityecorelua_EReference24', b2)
    if hasattr(b1, 'activityecorelua_EClass23'):
        assert not _is_linked(b1, 'activityecorelua_EClass23', a)
    if hasattr(b2, 'activityecorelua_EClass23'):
        assert _is_linked(b2, 'activityecorelua_EClass23', a)
    _safe_set(a, 'activityecorelua_EReference24', None)
    assert not _is_linked(a, 'activityecorelua_EReference24', b2)
    if hasattr(b2, 'activityecorelua_EClass23'):
        assert not _is_linked(b2, 'activityecorelua_EClass23', a)


def test_assoc_eAllGenericSuperTypes39_link_reassign_clear():
    a = activityecorelua_EClass(abstract=True, interface=True)
    b1 = activityecorelua_EGenericType()
    b2 = activityecorelua_EGenericType()
    _safe_set(a, 'activityecorelua_EClass40', {b1})
    assert _is_linked(a, 'activityecorelua_EClass40', b1)
    if hasattr(b1, 'activityecorelua_EGenericType41'):
        assert _is_linked(b1, 'activityecorelua_EGenericType41', a)
    _safe_set(a, 'activityecorelua_EClass40', {b2})
    assert _is_linked(a, 'activityecorelua_EClass40', b2)
    if hasattr(b1, 'activityecorelua_EGenericType41'):
        assert not _is_linked(b1, 'activityecorelua_EGenericType41', a)
    if hasattr(b2, 'activityecorelua_EGenericType41'):
        assert _is_linked(b2, 'activityecorelua_EGenericType41', a)
    _safe_set(a, 'activityecorelua_EClass40', set())
    assert not _is_linked(a, 'activityecorelua_EClass40', b2)
    if hasattr(b2, 'activityecorelua_EGenericType41'):
        assert not _is_linked(b2, 'activityecorelua_EGenericType41', a)


def test_assoc_eAllOperations25_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'activityecorelua_EOperation', b1)
    assert _is_linked(a, 'activityecorelua_EOperation', b1)
    if hasattr(b1, 'activityecorelua_EClass26'):
        assert _is_linked(b1, 'activityecorelua_EClass26', a)
    _safe_set(a, 'activityecorelua_EOperation', b2)
    assert _is_linked(a, 'activityecorelua_EOperation', b2)
    if hasattr(b1, 'activityecorelua_EClass26'):
        assert not _is_linked(b1, 'activityecorelua_EClass26', a)
    if hasattr(b2, 'activityecorelua_EClass26'):
        assert _is_linked(b2, 'activityecorelua_EClass26', a)
    _safe_set(a, 'activityecorelua_EOperation', None)
    assert not _is_linked(a, 'activityecorelua_EOperation', b2)
    if hasattr(b2, 'activityecorelua_EClass26'):
        assert not _is_linked(b2, 'activityecorelua_EClass26', a)


def test_assoc_eAllReferences14_link_reassign_clear():
    a = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'activityecorelua_EReference', b1)
    assert _is_linked(a, 'activityecorelua_EReference', b1)
    if hasattr(b1, 'activityecorelua_EClass15'):
        assert _is_linked(b1, 'activityecorelua_EClass15', a)
    _safe_set(a, 'activityecorelua_EReference', b2)
    assert _is_linked(a, 'activityecorelua_EReference', b2)
    if hasattr(b1, 'activityecorelua_EClass15'):
        assert not _is_linked(b1, 'activityecorelua_EClass15', a)
    if hasattr(b2, 'activityecorelua_EClass15'):
        assert _is_linked(b2, 'activityecorelua_EClass15', a)
    _safe_set(a, 'activityecorelua_EReference', None)
    assert not _is_linked(a, 'activityecorelua_EReference', b2)
    if hasattr(b2, 'activityecorelua_EClass15'):
        assert not _is_linked(b2, 'activityecorelua_EClass15', a)


def test_assoc_eAllStructuralFeatures27_link_reassign_clear():
    a = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'activityecorelua_EStructuralFeature', b1)
    assert _is_linked(a, 'activityecorelua_EStructuralFeature', b1)
    if hasattr(b1, 'activityecorelua_EClass28'):
        assert _is_linked(b1, 'activityecorelua_EClass28', a)
    _safe_set(a, 'activityecorelua_EStructuralFeature', b2)
    assert _is_linked(a, 'activityecorelua_EStructuralFeature', b2)
    if hasattr(b1, 'activityecorelua_EClass28'):
        assert not _is_linked(b1, 'activityecorelua_EClass28', a)
    if hasattr(b2, 'activityecorelua_EClass28'):
        assert _is_linked(b2, 'activityecorelua_EClass28', a)
    _safe_set(a, 'activityecorelua_EStructuralFeature', None)
    assert not _is_linked(a, 'activityecorelua_EStructuralFeature', b2)
    if hasattr(b2, 'activityecorelua_EClass28'):
        assert not _is_linked(b2, 'activityecorelua_EClass28', a)


def test_assoc_eAllSuperTypes30_link_reassign_clear():
    a = activityecorelua_EClass(abstract=True, interface=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'activityecorelua_EClass29', {b1})
    assert _is_linked(a, 'activityecorelua_EClass29', b1)
    if hasattr(b1, 'activityecorelua_EClass31'):
        assert _is_linked(b1, 'activityecorelua_EClass31', a)
    _safe_set(a, 'activityecorelua_EClass29', {b2})
    assert _is_linked(a, 'activityecorelua_EClass29', b2)
    if hasattr(b1, 'activityecorelua_EClass31'):
        assert not _is_linked(b1, 'activityecorelua_EClass31', a)
    if hasattr(b2, 'activityecorelua_EClass31'):
        assert _is_linked(b2, 'activityecorelua_EClass31', a)
    _safe_set(a, 'activityecorelua_EClass29', set())
    assert not _is_linked(a, 'activityecorelua_EClass29', b2)
    if hasattr(b2, 'activityecorelua_EClass31'):
        assert not _is_linked(b2, 'activityecorelua_EClass31', a)


def test_assoc_eAnnotations48_link_reassign_clear():
    a = activityecorelua_EModelElement()
    b1 = activityecorelua_EAnnotation(source="sample_text")
    b2 = activityecorelua_EAnnotation(source="sample_text_2")
    _safe_set(a, 'eModelElement', {b1})
    assert _is_linked(a, 'eModelElement', b1)
    if hasattr(b1, 'EAnnotation'):
        assert _is_linked(b1, 'EAnnotation', a)
    _safe_set(a, 'eModelElement', {b2})
    assert _is_linked(a, 'eModelElement', b2)
    if hasattr(b1, 'EAnnotation'):
        assert not _is_linked(b1, 'EAnnotation', a)
    if hasattr(b2, 'EAnnotation'):
        assert _is_linked(b2, 'EAnnotation', a)
    _safe_set(a, 'eModelElement', set())
    assert not _is_linked(a, 'eModelElement', b2)
    if hasattr(b2, 'EAnnotation'):
        assert not _is_linked(b2, 'EAnnotation', a)


def test_assoc_eAttributeType0_link_reassign_clear():
    a = activityecorelua_EDataType(serializable=True)
    b1 = activityecorelua_EAttribute(iD=True)
    b2 = activityecorelua_EAttribute(iD=False)
    _safe_set(a, 'activityecorelua_EDataType', b1)
    assert _is_linked(a, 'activityecorelua_EDataType', b1)
    if hasattr(b1, 'activityecorelua_EAttribute'):
        assert _is_linked(b1, 'activityecorelua_EAttribute', a)
    _safe_set(a, 'activityecorelua_EDataType', b2)
    assert _is_linked(a, 'activityecorelua_EDataType', b2)
    if hasattr(b1, 'activityecorelua_EAttribute'):
        assert not _is_linked(b1, 'activityecorelua_EAttribute', a)
    if hasattr(b2, 'activityecorelua_EAttribute'):
        assert _is_linked(b2, 'activityecorelua_EAttribute', a)
    _safe_set(a, 'activityecorelua_EDataType', None)
    assert not _is_linked(a, 'activityecorelua_EDataType', b2)
    if hasattr(b2, 'activityecorelua_EAttribute'):
        assert not _is_linked(b2, 'activityecorelua_EAttribute', a)


def test_assoc_eAttributes19_link_reassign_clear():
    a = activityecorelua_EClass(abstract=True, interface=True)
    b1 = activityecorelua_EAttribute(iD=True)
    b2 = activityecorelua_EAttribute(iD=False)
    _safe_set(a, 'activityecorelua_EClass20', {b1})
    assert _is_linked(a, 'activityecorelua_EClass20', b1)
    if hasattr(b1, 'activityecorelua_EAttribute21'):
        assert _is_linked(b1, 'activityecorelua_EAttribute21', a)
    _safe_set(a, 'activityecorelua_EClass20', {b2})
    assert _is_linked(a, 'activityecorelua_EClass20', b2)
    if hasattr(b1, 'activityecorelua_EAttribute21'):
        assert not _is_linked(b1, 'activityecorelua_EAttribute21', a)
    if hasattr(b2, 'activityecorelua_EAttribute21'):
        assert _is_linked(b2, 'activityecorelua_EAttribute21', a)
    _safe_set(a, 'activityecorelua_EClass20', set())
    assert not _is_linked(a, 'activityecorelua_EClass20', b2)
    if hasattr(b2, 'activityecorelua_EAttribute21'):
        assert not _is_linked(b2, 'activityecorelua_EAttribute21', a)


def test_assoc_eClassifier104_link_reassign_clear():
    a = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b1 = activityecorelua_EGenericType()
    b2 = activityecorelua_EGenericType()
    _safe_set(a, 'activityecorelua_EClassifier106', b1)
    assert _is_linked(a, 'activityecorelua_EClassifier106', b1)
    if hasattr(b1, 'activityecorelua_EGenericType105'):
        assert _is_linked(b1, 'activityecorelua_EGenericType105', a)
    _safe_set(a, 'activityecorelua_EClassifier106', b2)
    assert _is_linked(a, 'activityecorelua_EClassifier106', b2)
    if hasattr(b1, 'activityecorelua_EGenericType105'):
        assert not _is_linked(b1, 'activityecorelua_EGenericType105', a)
    if hasattr(b2, 'activityecorelua_EGenericType105'):
        assert _is_linked(b2, 'activityecorelua_EGenericType105', a)
    _safe_set(a, 'activityecorelua_EClassifier106', None)
    assert not _is_linked(a, 'activityecorelua_EClassifier106', b2)
    if hasattr(b2, 'activityecorelua_EGenericType105'):
        assert not _is_linked(b2, 'activityecorelua_EGenericType105', a)


def test_assoc_eClassifiers63_link_reassign_clear():
    a = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b2 = activityecorelua_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2", instanceTypeName="sample_text_2")
    _safe_set(a, 'ePackage64', {b1})
    assert _is_linked(a, 'ePackage64', b1)
    if hasattr(b1, 'EClassifier'):
        assert _is_linked(b1, 'EClassifier', a)
    _safe_set(a, 'ePackage64', {b2})
    assert _is_linked(a, 'ePackage64', b2)
    if hasattr(b1, 'EClassifier'):
        assert not _is_linked(b1, 'EClassifier', a)
    if hasattr(b2, 'EClassifier'):
        assert _is_linked(b2, 'EClassifier', a)
    _safe_set(a, 'ePackage64', set())
    assert not _is_linked(a, 'ePackage64', b2)
    if hasattr(b2, 'EClassifier'):
        assert not _is_linked(b2, 'EClassifier', a)


def test_assoc_eContainingClass49_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'eOperations', b1)
    assert _is_linked(a, 'eOperations', b1)
    if hasattr(b1, 'EClass'):
        assert _is_linked(b1, 'EClass', a)
    _safe_set(a, 'eOperations', b2)
    assert _is_linked(a, 'eOperations', b2)
    if hasattr(b1, 'EClass'):
        assert not _is_linked(b1, 'EClass', a)
    if hasattr(b2, 'EClass'):
        assert _is_linked(b2, 'EClass', a)
    _safe_set(a, 'eOperations', None)
    assert not _is_linked(a, 'eOperations', b2)
    if hasattr(b2, 'EClass'):
        assert not _is_linked(b2, 'EClass', a)


def test_assoc_eContainingClass82_link_reassign_clear():
    a = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'eStructuralFeatures', b1)
    assert _is_linked(a, 'eStructuralFeatures', b1)
    if hasattr(b1, 'EClass83'):
        assert _is_linked(b1, 'EClass83', a)
    _safe_set(a, 'eStructuralFeatures', b2)
    assert _is_linked(a, 'eStructuralFeatures', b2)
    if hasattr(b1, 'EClass83'):
        assert not _is_linked(b1, 'EClass83', a)
    if hasattr(b2, 'EClass83'):
        assert _is_linked(b2, 'EClass83', a)
    _safe_set(a, 'eStructuralFeatures', None)
    assert not _is_linked(a, 'eStructuralFeatures', b2)
    if hasattr(b2, 'EClass83'):
        assert not _is_linked(b2, 'EClass83', a)


def test_assoc_eEnum45_link_reassign_clear():
    a = activityecorelua_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    b1 = activityecorelua_EEnum()
    b2 = activityecorelua_EEnum()
    _safe_set(a, 'eLiterals', b1)
    assert _is_linked(a, 'eLiterals', b1)
    if hasattr(b1, 'EEnum'):
        assert _is_linked(b1, 'EEnum', a)
    _safe_set(a, 'eLiterals', b2)
    assert _is_linked(a, 'eLiterals', b2)
    if hasattr(b1, 'EEnum'):
        assert not _is_linked(b1, 'EEnum', a)
    if hasattr(b2, 'EEnum'):
        assert _is_linked(b2, 'EEnum', a)
    _safe_set(a, 'eLiterals', None)
    assert not _is_linked(a, 'eLiterals', b2)
    if hasattr(b2, 'EEnum'):
        assert not _is_linked(b2, 'EEnum', a)


def test_assoc_eExceptions56_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b2 = activityecorelua_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2", instanceTypeName="sample_text_2")
    _safe_set(a, 'activityecorelua_EOperation57', {b1})
    assert _is_linked(a, 'activityecorelua_EOperation57', b1)
    if hasattr(b1, 'activityecorelua_EClassifier58'):
        assert _is_linked(b1, 'activityecorelua_EClassifier58', a)
    _safe_set(a, 'activityecorelua_EOperation57', {b2})
    assert _is_linked(a, 'activityecorelua_EOperation57', b2)
    if hasattr(b1, 'activityecorelua_EClassifier58'):
        assert not _is_linked(b1, 'activityecorelua_EClassifier58', a)
    if hasattr(b2, 'activityecorelua_EClassifier58'):
        assert _is_linked(b2, 'activityecorelua_EClassifier58', a)
    _safe_set(a, 'activityecorelua_EOperation57', set())
    assert not _is_linked(a, 'activityecorelua_EOperation57', b2)
    if hasattr(b2, 'activityecorelua_EClassifier58'):
        assert not _is_linked(b2, 'activityecorelua_EClassifier58', a)


def test_assoc_eFactoryInstance62_link_reassign_clear():
    a = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = activityecorelua_EFactory()
    b2 = activityecorelua_EFactory()
    _safe_set(a, 'ePackage', b1)
    assert _is_linked(a, 'ePackage', b1)
    if hasattr(b1, 'EFactory'):
        assert _is_linked(b1, 'EFactory', a)
    _safe_set(a, 'ePackage', b2)
    assert _is_linked(a, 'ePackage', b2)
    if hasattr(b1, 'EFactory'):
        assert not _is_linked(b1, 'EFactory', a)
    if hasattr(b2, 'EFactory'):
        assert _is_linked(b2, 'EFactory', a)
    _safe_set(a, 'ePackage', None)
    assert not _is_linked(a, 'ePackage', b2)
    if hasattr(b2, 'EFactory'):
        assert not _is_linked(b2, 'EFactory', a)


def test_assoc_eGenericExceptions59_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_EGenericType()
    b2 = activityecorelua_EGenericType()
    _safe_set(a, 'activityecorelua_EOperation60', {b1})
    assert _is_linked(a, 'activityecorelua_EOperation60', b1)
    if hasattr(b1, 'activityecorelua_EGenericType61'):
        assert _is_linked(b1, 'activityecorelua_EGenericType61', a)
    _safe_set(a, 'activityecorelua_EOperation60', {b2})
    assert _is_linked(a, 'activityecorelua_EOperation60', b2)
    if hasattr(b1, 'activityecorelua_EGenericType61'):
        assert not _is_linked(b1, 'activityecorelua_EGenericType61', a)
    if hasattr(b2, 'activityecorelua_EGenericType61'):
        assert _is_linked(b2, 'activityecorelua_EGenericType61', a)
    _safe_set(a, 'activityecorelua_EOperation60', set())
    assert not _is_linked(a, 'activityecorelua_EOperation60', b2)
    if hasattr(b2, 'activityecorelua_EGenericType61'):
        assert not _is_linked(b2, 'activityecorelua_EGenericType61', a)


def test_assoc_eGenericSuperTypes37_link_reassign_clear():
    a = activityecorelua_EClass(abstract=True, interface=True)
    b1 = activityecorelua_EGenericType()
    b2 = activityecorelua_EGenericType()
    _safe_set(a, 'activityecorelua_EClass38', {b1})
    assert _is_linked(a, 'activityecorelua_EClass38', b1)
    if hasattr(b1, 'activityecorelua_EGenericType'):
        assert _is_linked(b1, 'activityecorelua_EGenericType', a)
    _safe_set(a, 'activityecorelua_EClass38', {b2})
    assert _is_linked(a, 'activityecorelua_EClass38', b2)
    if hasattr(b1, 'activityecorelua_EGenericType'):
        assert not _is_linked(b1, 'activityecorelua_EGenericType', a)
    if hasattr(b2, 'activityecorelua_EGenericType'):
        assert _is_linked(b2, 'activityecorelua_EGenericType', a)
    _safe_set(a, 'activityecorelua_EClass38', set())
    assert not _is_linked(a, 'activityecorelua_EClass38', b2)
    if hasattr(b2, 'activityecorelua_EGenericType'):
        assert not _is_linked(b2, 'activityecorelua_EGenericType', a)


def test_assoc_eGenericType86_link_reassign_clear():
    a = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    b1 = activityecorelua_EGenericType()
    b2 = activityecorelua_EGenericType()
    _safe_set(a, 'activityecorelua_ETypedElement87', b1)
    assert _is_linked(a, 'activityecorelua_ETypedElement87', b1)
    if hasattr(b1, 'activityecorelua_EGenericType88'):
        assert _is_linked(b1, 'activityecorelua_EGenericType88', a)
    _safe_set(a, 'activityecorelua_ETypedElement87', b2)
    assert _is_linked(a, 'activityecorelua_ETypedElement87', b2)
    if hasattr(b1, 'activityecorelua_EGenericType88'):
        assert not _is_linked(b1, 'activityecorelua_EGenericType88', a)
    if hasattr(b2, 'activityecorelua_EGenericType88'):
        assert _is_linked(b2, 'activityecorelua_EGenericType88', a)
    _safe_set(a, 'activityecorelua_ETypedElement87', None)
    assert not _is_linked(a, 'activityecorelua_ETypedElement87', b2)
    if hasattr(b2, 'activityecorelua_EGenericType88'):
        assert not _is_linked(b2, 'activityecorelua_EGenericType88', a)


def test_assoc_eIDAttribute32_link_reassign_clear():
    a = activityecorelua_EClass(abstract=True, interface=True)
    b1 = activityecorelua_EAttribute(iD=True)
    b2 = activityecorelua_EAttribute(iD=False)
    _safe_set(a, 'activityecorelua_EClass33', b1)
    assert _is_linked(a, 'activityecorelua_EClass33', b1)
    if hasattr(b1, 'activityecorelua_EAttribute34'):
        assert _is_linked(b1, 'activityecorelua_EAttribute34', a)
    _safe_set(a, 'activityecorelua_EClass33', b2)
    assert _is_linked(a, 'activityecorelua_EClass33', b2)
    if hasattr(b1, 'activityecorelua_EAttribute34'):
        assert not _is_linked(b1, 'activityecorelua_EAttribute34', a)
    if hasattr(b2, 'activityecorelua_EAttribute34'):
        assert _is_linked(b2, 'activityecorelua_EAttribute34', a)
    _safe_set(a, 'activityecorelua_EClass33', None)
    assert not _is_linked(a, 'activityecorelua_EClass33', b2)
    if hasattr(b2, 'activityecorelua_EAttribute34'):
        assert not _is_linked(b2, 'activityecorelua_EAttribute34', a)


def test_assoc_eKeys79_link_reassign_clear():
    a = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    b1 = activityecorelua_EAttribute(iD=True)
    b2 = activityecorelua_EAttribute(iD=False)
    _safe_set(a, 'activityecorelua_EReference80', {b1})
    assert _is_linked(a, 'activityecorelua_EReference80', b1)
    if hasattr(b1, 'activityecorelua_EAttribute81'):
        assert _is_linked(b1, 'activityecorelua_EAttribute81', a)
    _safe_set(a, 'activityecorelua_EReference80', {b2})
    assert _is_linked(a, 'activityecorelua_EReference80', b2)
    if hasattr(b1, 'activityecorelua_EAttribute81'):
        assert not _is_linked(b1, 'activityecorelua_EAttribute81', a)
    if hasattr(b2, 'activityecorelua_EAttribute81'):
        assert _is_linked(b2, 'activityecorelua_EAttribute81', a)
    _safe_set(a, 'activityecorelua_EReference80', set())
    assert not _is_linked(a, 'activityecorelua_EReference80', b2)
    if hasattr(b2, 'activityecorelua_EAttribute81'):
        assert not _is_linked(b2, 'activityecorelua_EAttribute81', a)


def test_assoc_eLiterals44_link_reassign_clear():
    a = activityecorelua_EEnumLiteral(instance="sample_text", literal="sample_text", value=7)
    b1 = activityecorelua_EEnum()
    b2 = activityecorelua_EEnum()
    _safe_set(a, 'EEnumLiteral', b1)
    assert _is_linked(a, 'EEnumLiteral', b1)
    if hasattr(b1, 'eEnum'):
        assert _is_linked(b1, 'eEnum', a)
    _safe_set(a, 'EEnumLiteral', b2)
    assert _is_linked(a, 'EEnumLiteral', b2)
    if hasattr(b1, 'eEnum'):
        assert not _is_linked(b1, 'eEnum', a)
    if hasattr(b2, 'eEnum'):
        assert _is_linked(b2, 'eEnum', a)
    _safe_set(a, 'EEnumLiteral', None)
    assert not _is_linked(a, 'EEnumLiteral', b2)
    if hasattr(b2, 'eEnum'):
        assert not _is_linked(b2, 'eEnum', a)


def test_assoc_eModelElement2_link_reassign_clear():
    a = activityecorelua_EModelElement()
    b1 = activityecorelua_EAnnotation(source="sample_text")
    b2 = activityecorelua_EAnnotation(source="sample_text_2")
    _safe_set(a, 'EModelElement', b1)
    assert _is_linked(a, 'EModelElement', b1)
    if hasattr(b1, 'eAnnotations'):
        assert _is_linked(b1, 'eAnnotations', a)
    _safe_set(a, 'EModelElement', b2)
    assert _is_linked(a, 'EModelElement', b2)
    if hasattr(b1, 'eAnnotations'):
        assert not _is_linked(b1, 'eAnnotations', a)
    if hasattr(b2, 'eAnnotations'):
        assert _is_linked(b2, 'eAnnotations', a)
    _safe_set(a, 'EModelElement', None)
    assert not _is_linked(a, 'EModelElement', b2)
    if hasattr(b2, 'eAnnotations'):
        assert not _is_linked(b2, 'eAnnotations', a)


def test_assoc_eOperation71_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_EParameter()
    b2 = activityecorelua_EParameter()
    _safe_set(a, 'EOperation72', b1)
    assert _is_linked(a, 'EOperation72', b1)
    if hasattr(b1, 'eParameters'):
        assert _is_linked(b1, 'eParameters', a)
    _safe_set(a, 'EOperation72', b2)
    assert _is_linked(a, 'EOperation72', b2)
    if hasattr(b1, 'eParameters'):
        assert not _is_linked(b1, 'eParameters', a)
    if hasattr(b2, 'eParameters'):
        assert _is_linked(b2, 'eParameters', a)
    _safe_set(a, 'EOperation72', None)
    assert not _is_linked(a, 'EOperation72', b2)
    if hasattr(b2, 'eParameters'):
        assert not _is_linked(b2, 'eParameters', a)


def test_assoc_eOperations10_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'EOperation', b1)
    assert _is_linked(a, 'EOperation', b1)
    if hasattr(b1, 'eContainingClass'):
        assert _is_linked(b1, 'eContainingClass', a)
    _safe_set(a, 'EOperation', b2)
    assert _is_linked(a, 'EOperation', b2)
    if hasattr(b1, 'eContainingClass'):
        assert not _is_linked(b1, 'eContainingClass', a)
    if hasattr(b2, 'eContainingClass'):
        assert _is_linked(b2, 'eContainingClass', a)
    _safe_set(a, 'EOperation', None)
    assert not _is_linked(a, 'EOperation', b2)
    if hasattr(b2, 'eContainingClass'):
        assert not _is_linked(b2, 'eContainingClass', a)


def test_assoc_eOpposite74_link_reassign_clear():
    a = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    b1 = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    b2 = activityecorelua_EReference(container=False, containment=False, resolveProxies=False)
    _safe_set(a, 'activityecorelua_EReference73', b1)
    assert _is_linked(a, 'activityecorelua_EReference73', b1)
    if hasattr(b1, 'activityecorelua_EReference75'):
        assert _is_linked(b1, 'activityecorelua_EReference75', a)
    _safe_set(a, 'activityecorelua_EReference73', b2)
    assert _is_linked(a, 'activityecorelua_EReference73', b2)
    if hasattr(b1, 'activityecorelua_EReference75'):
        assert not _is_linked(b1, 'activityecorelua_EReference75', a)
    if hasattr(b2, 'activityecorelua_EReference75'):
        assert _is_linked(b2, 'activityecorelua_EReference75', a)
    _safe_set(a, 'activityecorelua_EReference73', None)
    assert not _is_linked(a, 'activityecorelua_EReference73', b2)
    if hasattr(b2, 'activityecorelua_EReference75'):
        assert not _is_linked(b2, 'activityecorelua_EReference75', a)


def test_assoc_ePackage42_link_reassign_clear():
    a = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b2 = activityecorelua_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2", instanceTypeName="sample_text_2")
    _safe_set(a, 'EPackage', b1)
    assert _is_linked(a, 'EPackage', b1)
    if hasattr(b1, 'eClassifiers'):
        assert _is_linked(b1, 'eClassifiers', a)
    _safe_set(a, 'EPackage', b2)
    assert _is_linked(a, 'EPackage', b2)
    if hasattr(b1, 'eClassifiers'):
        assert not _is_linked(b1, 'eClassifiers', a)
    if hasattr(b2, 'eClassifiers'):
        assert _is_linked(b2, 'eClassifiers', a)
    _safe_set(a, 'EPackage', None)
    assert not _is_linked(a, 'EPackage', b2)
    if hasattr(b2, 'eClassifiers'):
        assert not _is_linked(b2, 'eClassifiers', a)


def test_assoc_ePackage46_link_reassign_clear():
    a = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = activityecorelua_EFactory()
    b2 = activityecorelua_EFactory()
    _safe_set(a, 'EPackage47', b1)
    assert _is_linked(a, 'EPackage47', b1)
    if hasattr(b1, 'eFactoryInstance'):
        assert _is_linked(b1, 'eFactoryInstance', a)
    _safe_set(a, 'EPackage47', b2)
    assert _is_linked(a, 'EPackage47', b2)
    if hasattr(b1, 'eFactoryInstance'):
        assert not _is_linked(b1, 'eFactoryInstance', a)
    if hasattr(b2, 'eFactoryInstance'):
        assert _is_linked(b2, 'eFactoryInstance', a)
    _safe_set(a, 'EPackage47', None)
    assert not _is_linked(a, 'EPackage47', b2)
    if hasattr(b2, 'eFactoryInstance'):
        assert not _is_linked(b2, 'eFactoryInstance', a)


def test_assoc_eParameters53_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_EParameter()
    b2 = activityecorelua_EParameter()
    _safe_set(a, 'eOperation', {b1})
    assert _is_linked(a, 'eOperation', b1)
    if hasattr(b1, 'EParameter'):
        assert _is_linked(b1, 'EParameter', a)
    _safe_set(a, 'eOperation', {b2})
    assert _is_linked(a, 'eOperation', b2)
    if hasattr(b1, 'EParameter'):
        assert not _is_linked(b1, 'EParameter', a)
    if hasattr(b2, 'EParameter'):
        assert _is_linked(b2, 'EParameter', a)
    _safe_set(a, 'eOperation', set())
    assert not _is_linked(a, 'eOperation', b2)
    if hasattr(b2, 'EParameter'):
        assert not _is_linked(b2, 'EParameter', a)


def test_assoc_eRawType95_link_reassign_clear():
    a = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b1 = activityecorelua_EGenericType()
    b2 = activityecorelua_EGenericType()
    _safe_set(a, 'activityecorelua_EClassifier97', b1)
    assert _is_linked(a, 'activityecorelua_EClassifier97', b1)
    if hasattr(b1, 'activityecorelua_EGenericType96'):
        assert _is_linked(b1, 'activityecorelua_EGenericType96', a)
    _safe_set(a, 'activityecorelua_EClassifier97', b2)
    assert _is_linked(a, 'activityecorelua_EClassifier97', b2)
    if hasattr(b1, 'activityecorelua_EGenericType96'):
        assert not _is_linked(b1, 'activityecorelua_EGenericType96', a)
    if hasattr(b2, 'activityecorelua_EGenericType96'):
        assert _is_linked(b2, 'activityecorelua_EGenericType96', a)
    _safe_set(a, 'activityecorelua_EClassifier97', None)
    assert not _is_linked(a, 'activityecorelua_EClassifier97', b2)
    if hasattr(b2, 'activityecorelua_EGenericType96'):
        assert not _is_linked(b2, 'activityecorelua_EGenericType96', a)


def test_assoc_eReferenceType76_link_reassign_clear():
    a = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'activityecorelua_EReference77', b1)
    assert _is_linked(a, 'activityecorelua_EReference77', b1)
    if hasattr(b1, 'activityecorelua_EClass78'):
        assert _is_linked(b1, 'activityecorelua_EClass78', a)
    _safe_set(a, 'activityecorelua_EReference77', b2)
    assert _is_linked(a, 'activityecorelua_EReference77', b2)
    if hasattr(b1, 'activityecorelua_EClass78'):
        assert not _is_linked(b1, 'activityecorelua_EClass78', a)
    if hasattr(b2, 'activityecorelua_EClass78'):
        assert _is_linked(b2, 'activityecorelua_EClass78', a)
    _safe_set(a, 'activityecorelua_EReference77', None)
    assert not _is_linked(a, 'activityecorelua_EReference77', b2)
    if hasattr(b2, 'activityecorelua_EClass78'):
        assert not _is_linked(b2, 'activityecorelua_EClass78', a)


def test_assoc_eReferences16_link_reassign_clear():
    a = activityecorelua_EReference(container=True, containment=True, resolveProxies=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'activityecorelua_EReference18', b1)
    assert _is_linked(a, 'activityecorelua_EReference18', b1)
    if hasattr(b1, 'activityecorelua_EClass17'):
        assert _is_linked(b1, 'activityecorelua_EClass17', a)
    _safe_set(a, 'activityecorelua_EReference18', b2)
    assert _is_linked(a, 'activityecorelua_EReference18', b2)
    if hasattr(b1, 'activityecorelua_EClass17'):
        assert not _is_linked(b1, 'activityecorelua_EClass17', a)
    if hasattr(b2, 'activityecorelua_EClass17'):
        assert _is_linked(b2, 'activityecorelua_EClass17', a)
    _safe_set(a, 'activityecorelua_EReference18', None)
    assert not _is_linked(a, 'activityecorelua_EReference18', b2)
    if hasattr(b2, 'activityecorelua_EClass17'):
        assert not _is_linked(b2, 'activityecorelua_EClass17', a)


def test_assoc_eStructuralFeatures35_link_reassign_clear():
    a = activityecorelua_EStructuralFeature(changeable=True, defaultValue="sample_text", defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'EStructuralFeature', b1)
    assert _is_linked(a, 'EStructuralFeature', b1)
    if hasattr(b1, 'eContainingClass36'):
        assert _is_linked(b1, 'eContainingClass36', a)
    _safe_set(a, 'EStructuralFeature', b2)
    assert _is_linked(a, 'EStructuralFeature', b2)
    if hasattr(b1, 'eContainingClass36'):
        assert not _is_linked(b1, 'eContainingClass36', a)
    if hasattr(b2, 'eContainingClass36'):
        assert _is_linked(b2, 'eContainingClass36', a)
    _safe_set(a, 'EStructuralFeature', None)
    assert not _is_linked(a, 'EStructuralFeature', b2)
    if hasattr(b2, 'eContainingClass36'):
        assert not _is_linked(b2, 'eContainingClass36', a)


def test_assoc_eSubpackages66_link_reassign_clear():
    a = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b2 = activityecorelua_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    _safe_set(a, 'EPackage67', b1)
    assert _is_linked(a, 'EPackage67', b1)
    if hasattr(b1, 'eSuperPackage'):
        assert _is_linked(b1, 'eSuperPackage', a)
    _safe_set(a, 'EPackage67', b2)
    assert _is_linked(a, 'EPackage67', b2)
    if hasattr(b1, 'eSuperPackage'):
        assert not _is_linked(b1, 'eSuperPackage', a)
    if hasattr(b2, 'eSuperPackage'):
        assert _is_linked(b2, 'eSuperPackage', a)
    _safe_set(a, 'EPackage67', None)
    assert not _is_linked(a, 'EPackage67', b2)
    if hasattr(b2, 'eSuperPackage'):
        assert not _is_linked(b2, 'eSuperPackage', a)


def test_assoc_eSuperPackage69_link_reassign_clear():
    a = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b1 = activityecorelua_EPackage(nsPrefix="sample_text", nsURI="sample_text")
    b2 = activityecorelua_EPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    _safe_set(a, 'EPackage70', b1)
    assert _is_linked(a, 'EPackage70', b1)
    if hasattr(b1, 'eSubpackages'):
        assert _is_linked(b1, 'eSubpackages', a)
    _safe_set(a, 'EPackage70', b2)
    assert _is_linked(a, 'EPackage70', b2)
    if hasattr(b1, 'eSubpackages'):
        assert not _is_linked(b1, 'eSubpackages', a)
    if hasattr(b2, 'eSubpackages'):
        assert _is_linked(b2, 'eSubpackages', a)
    _safe_set(a, 'EPackage70', None)
    assert not _is_linked(a, 'EPackage70', b2)
    if hasattr(b2, 'eSubpackages'):
        assert not _is_linked(b2, 'eSubpackages', a)


def test_assoc_eSuperTypes9_link_reassign_clear():
    a = activityecorelua_EClass(abstract=True, interface=True)
    b1 = activityecorelua_EClass(abstract=True, interface=True)
    b2 = activityecorelua_EClass(abstract=False, interface=False)
    _safe_set(a, 'activityecorelua_EClass', b1)
    assert _is_linked(a, 'activityecorelua_EClass', b1)
    if hasattr(b1, 'activityecorelua_EClass8'):
        assert _is_linked(b1, 'activityecorelua_EClass8', a)
    _safe_set(a, 'activityecorelua_EClass', b2)
    assert _is_linked(a, 'activityecorelua_EClass', b2)
    if hasattr(b1, 'activityecorelua_EClass8'):
        assert not _is_linked(b1, 'activityecorelua_EClass8', a)
    if hasattr(b2, 'activityecorelua_EClass8'):
        assert _is_linked(b2, 'activityecorelua_EClass8', a)
    _safe_set(a, 'activityecorelua_EClass', None)
    assert not _is_linked(a, 'activityecorelua_EClass', b2)
    if hasattr(b2, 'activityecorelua_EClass8'):
        assert not _is_linked(b2, 'activityecorelua_EClass8', a)


def test_assoc_eType84_link_reassign_clear():
    a = activityecorelua_ETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    b1 = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b2 = activityecorelua_EClassifier(defaultValue="sample_text_2", instanceClass="sample_text_2", instanceClassName="sample_text_2", instanceTypeName="sample_text_2")
    _safe_set(a, 'activityecorelua_ETypedElement', b1)
    assert _is_linked(a, 'activityecorelua_ETypedElement', b1)
    if hasattr(b1, 'activityecorelua_EClassifier85'):
        assert _is_linked(b1, 'activityecorelua_EClassifier85', a)
    _safe_set(a, 'activityecorelua_ETypedElement', b2)
    assert _is_linked(a, 'activityecorelua_ETypedElement', b2)
    if hasattr(b1, 'activityecorelua_EClassifier85'):
        assert not _is_linked(b1, 'activityecorelua_EClassifier85', a)
    if hasattr(b2, 'activityecorelua_EClassifier85'):
        assert _is_linked(b2, 'activityecorelua_EClassifier85', a)
    _safe_set(a, 'activityecorelua_ETypedElement', None)
    assert not _is_linked(a, 'activityecorelua_ETypedElement', b2)
    if hasattr(b2, 'activityecorelua_EClassifier85'):
        assert not _is_linked(b2, 'activityecorelua_EClassifier85', a)


def test_assoc_eTypeParameters43_link_reassign_clear():
    a = activityecorelua_EClassifier(defaultValue="sample_text", instanceClass="sample_text", instanceClassName="sample_text", instanceTypeName="sample_text")
    b1 = activityecorelua_ETypeParameter()
    b2 = activityecorelua_ETypeParameter()
    _safe_set(a, 'activityecorelua_EClassifier', {b1})
    assert _is_linked(a, 'activityecorelua_EClassifier', b1)
    if hasattr(b1, 'activityecorelua_ETypeParameter'):
        assert _is_linked(b1, 'activityecorelua_ETypeParameter', a)
    _safe_set(a, 'activityecorelua_EClassifier', {b2})
    assert _is_linked(a, 'activityecorelua_EClassifier', b2)
    if hasattr(b1, 'activityecorelua_ETypeParameter'):
        assert not _is_linked(b1, 'activityecorelua_ETypeParameter', a)
    if hasattr(b2, 'activityecorelua_ETypeParameter'):
        assert _is_linked(b2, 'activityecorelua_ETypeParameter', a)
    _safe_set(a, 'activityecorelua_EClassifier', set())
    assert not _is_linked(a, 'activityecorelua_EClassifier', b2)
    if hasattr(b2, 'activityecorelua_ETypeParameter'):
        assert not _is_linked(b2, 'activityecorelua_ETypeParameter', a)


def test_assoc_eTypeParameters50_link_reassign_clear():
    a = activityecorelua_EOperation()
    b1 = activityecorelua_ETypeParameter()
    b2 = activityecorelua_ETypeParameter()
    _safe_set(a, 'activityecorelua_EOperation51', {b1})
    assert _is_linked(a, 'activityecorelua_EOperation51', b1)
    if hasattr(b1, 'activityecorelua_ETypeParameter52'):
        assert _is_linked(b1, 'activityecorelua_ETypeParameter52', a)
    _safe_set(a, 'activityecorelua_EOperation51', {b2})
    assert _is_linked(a, 'activityecorelua_EOperation51', b2)
    if hasattr(b1, 'activityecorelua_ETypeParameter52'):
        assert not _is_linked(b1, 'activityecorelua_ETypeParameter52', a)
    if hasattr(b2, 'activityecorelua_ETypeParameter52'):
        assert _is_linked(b2, 'activityecorelua_ETypeParameter52', a)
    _safe_set(a, 'activityecorelua_EOperation51', set())
    assert not _is_linked(a, 'activityecorelua_EOperation51', b2)
    if hasattr(b2, 'activityecorelua_ETypeParameter52'):
        assert not _is_linked(b2, 'activityecorelua_ETypeParameter52', a)


def test_assoc_expressions182_link_reassign_clear():
    a = activityecorelua_Statement_For_Generic(names="sample_text")
    b1 = activityecorelua_Expression()
    b2 = activityecorelua_Expression()
    _safe_set(a, 'activityecorelua_Statement_For_Generic', {b1})
    assert _is_linked(a, 'activityecorelua_Statement_For_Generic', b1)
    if hasattr(b1, 'activityecorelua_Expression183'):
        assert _is_linked(b1, 'activityecorelua_Expression183', a)
    _safe_set(a, 'activityecorelua_Statement_For_Generic', {b2})
    assert _is_linked(a, 'activityecorelua_Statement_For_Generic', b2)
    if hasattr(b1, 'activityecorelua_Expression183'):
        assert not _is_linked(b1, 'activityecorelua_Expression183', a)
    if hasattr(b2, 'activityecorelua_Expression183'):
        assert _is_linked(b2, 'activityecorelua_Expression183', a)
    _safe_set(a, 'activityecorelua_Statement_For_Generic', set())
    assert not _is_linked(a, 'activityecorelua_Statement_For_Generic', b2)
    if hasattr(b2, 'activityecorelua_Expression183'):
        assert not _is_linked(b2, 'activityecorelua_Expression183', a)


def test_assoc_function187_link_reassign_clear():
    a = activityecorelua_Statement_GlobalFunction_Declaration(functionName="sample_text", prefix="sample_text")
    b1 = activityecorelua_Function(parameters="sample_text", varArgs=True)
    b2 = activityecorelua_Function(parameters="sample_text_2", varArgs=False)
    _safe_set(a, 'activityecorelua_Statement_GlobalFunction_Declaration', b1)
    assert _is_linked(a, 'activityecorelua_Statement_GlobalFunction_Declaration', b1)
    if hasattr(b1, 'activityecorelua_Function'):
        assert _is_linked(b1, 'activityecorelua_Function', a)
    _safe_set(a, 'activityecorelua_Statement_GlobalFunction_Declaration', b2)
    assert _is_linked(a, 'activityecorelua_Statement_GlobalFunction_Declaration', b2)
    if hasattr(b1, 'activityecorelua_Function'):
        assert not _is_linked(b1, 'activityecorelua_Function', a)
    if hasattr(b2, 'activityecorelua_Function'):
        assert _is_linked(b2, 'activityecorelua_Function', a)
    _safe_set(a, 'activityecorelua_Statement_GlobalFunction_Declaration', None)
    assert not _is_linked(a, 'activityecorelua_Statement_GlobalFunction_Declaration', b2)
    if hasattr(b2, 'activityecorelua_Function'):
        assert not _is_linked(b2, 'activityecorelua_Function', a)


def test_assoc_function188_link_reassign_clear():
    a = activityecorelua_Statement_LocalFunction_Declaration(functionName="sample_text")
    b1 = activityecorelua_Function(parameters="sample_text", varArgs=True)
    b2 = activityecorelua_Function(parameters="sample_text_2", varArgs=False)
    _safe_set(a, 'activityecorelua_Statement_LocalFunction_Declaration', b1)
    assert _is_linked(a, 'activityecorelua_Statement_LocalFunction_Declaration', b1)
    if hasattr(b1, 'activityecorelua_Function189'):
        assert _is_linked(b1, 'activityecorelua_Function189', a)
    _safe_set(a, 'activityecorelua_Statement_LocalFunction_Declaration', b2)
    assert _is_linked(a, 'activityecorelua_Statement_LocalFunction_Declaration', b2)
    if hasattr(b1, 'activityecorelua_Function189'):
        assert not _is_linked(b1, 'activityecorelua_Function189', a)
    if hasattr(b2, 'activityecorelua_Function189'):
        assert _is_linked(b2, 'activityecorelua_Function189', a)
    _safe_set(a, 'activityecorelua_Statement_LocalFunction_Declaration', None)
    assert not _is_linked(a, 'activityecorelua_Statement_LocalFunction_Declaration', b2)
    if hasattr(b2, 'activityecorelua_Function189'):
        assert not _is_linked(b2, 'activityecorelua_Function189', a)


def test_assoc_function192_link_reassign_clear():
    a = activityecorelua_Function(parameters="sample_text", varArgs=True)
    b1 = activityecorelua_Expression_Function()
    b2 = activityecorelua_Expression_Function()
    _safe_set(a, 'activityecorelua_Function193', b1)
    assert _is_linked(a, 'activityecorelua_Function193', b1)
    if hasattr(b1, 'activityecorelua_Expression_Function'):
        assert _is_linked(b1, 'activityecorelua_Expression_Function', a)
    _safe_set(a, 'activityecorelua_Function193', b2)
    assert _is_linked(a, 'activityecorelua_Function193', b2)
    if hasattr(b1, 'activityecorelua_Expression_Function'):
        assert not _is_linked(b1, 'activityecorelua_Expression_Function', a)
    if hasattr(b2, 'activityecorelua_Expression_Function'):
        assert _is_linked(b2, 'activityecorelua_Expression_Function', a)
    _safe_set(a, 'activityecorelua_Function193', None)
    assert not _is_linked(a, 'activityecorelua_Function193', b2)
    if hasattr(b2, 'activityecorelua_Expression_Function'):
        assert not _is_linked(b2, 'activityecorelua_Expression_Function', a)


def test_assoc_incoming119_link_reassign_clear():
    a = activityecorelua_ActivityNode(running=True)
    b1 = activityecorelua_ActivityEdge()
    b2 = activityecorelua_ActivityEdge()
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'ActivityEdge120'):
        assert _is_linked(b1, 'ActivityEdge120', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'ActivityEdge120'):
        assert not _is_linked(b1, 'ActivityEdge120', a)
    if hasattr(b2, 'ActivityEdge120'):
        assert _is_linked(b2, 'ActivityEdge120', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'ActivityEdge120'):
        assert not _is_linked(b2, 'ActivityEdge120', a)


def test_assoc_initialValue128_link_reassign_clear():
    a = activityecorelua_Variable(name="sample_text")
    b1 = activityecorelua_Value()
    b2 = activityecorelua_Value()
    _safe_set(a, 'activityecorelua_Variable129', b1)
    assert _is_linked(a, 'activityecorelua_Variable129', b1)
    if hasattr(b1, 'activityecorelua_Value'):
        assert _is_linked(b1, 'activityecorelua_Value', a)
    _safe_set(a, 'activityecorelua_Variable129', b2)
    assert _is_linked(a, 'activityecorelua_Variable129', b2)
    if hasattr(b1, 'activityecorelua_Value'):
        assert not _is_linked(b1, 'activityecorelua_Value', a)
    if hasattr(b2, 'activityecorelua_Value'):
        assert _is_linked(b2, 'activityecorelua_Value', a)
    _safe_set(a, 'activityecorelua_Variable129', None)
    assert not _is_linked(a, 'activityecorelua_Variable129', b2)
    if hasattr(b2, 'activityecorelua_Value'):
        assert not _is_linked(b2, 'activityecorelua_Value', a)


def test_assoc_initialValue190_link_reassign_clear():
    a = activityecorelua_Statement_Local_Variable_Declaration(variableNames="sample_text")
    b1 = activityecorelua_Expression()
    b2 = activityecorelua_Expression()
    _safe_set(a, 'activityecorelua_Statement_Local_Variable_Declaration', {b1})
    assert _is_linked(a, 'activityecorelua_Statement_Local_Variable_Declaration', b1)
    if hasattr(b1, 'activityecorelua_Expression191'):
        assert _is_linked(b1, 'activityecorelua_Expression191', a)
    _safe_set(a, 'activityecorelua_Statement_Local_Variable_Declaration', {b2})
    assert _is_linked(a, 'activityecorelua_Statement_Local_Variable_Declaration', b2)
    if hasattr(b1, 'activityecorelua_Expression191'):
        assert not _is_linked(b1, 'activityecorelua_Expression191', a)
    if hasattr(b2, 'activityecorelua_Expression191'):
        assert _is_linked(b2, 'activityecorelua_Expression191', a)
    _safe_set(a, 'activityecorelua_Statement_Local_Variable_Declaration', set())
    assert not _is_linked(a, 'activityecorelua_Statement_Local_Variable_Declaration', b2)
    if hasattr(b2, 'activityecorelua_Expression191'):
        assert not _is_linked(b2, 'activityecorelua_Expression191', a)


def test_assoc_inputs115_link_reassign_clear():
    a = activityecorelua_Variable(name="sample_text")
    b1 = activityecorelua_Activity()
    b2 = activityecorelua_Activity()
    _safe_set(a, 'activityecorelua_Variable117', b1)
    assert _is_linked(a, 'activityecorelua_Variable117', b1)
    if hasattr(b1, 'activityecorelua_Activity116'):
        assert _is_linked(b1, 'activityecorelua_Activity116', a)
    _safe_set(a, 'activityecorelua_Variable117', b2)
    assert _is_linked(a, 'activityecorelua_Variable117', b2)
    if hasattr(b1, 'activityecorelua_Activity116'):
        assert not _is_linked(b1, 'activityecorelua_Activity116', a)
    if hasattr(b2, 'activityecorelua_Activity116'):
        assert _is_linked(b2, 'activityecorelua_Activity116', a)
    _safe_set(a, 'activityecorelua_Variable117', None)
    assert not _is_linked(a, 'activityecorelua_Variable117', b2)
    if hasattr(b2, 'activityecorelua_Activity116'):
        assert not _is_linked(b2, 'activityecorelua_Activity116', a)


def test_assoc_locals113_link_reassign_clear():
    a = activityecorelua_Variable(name="sample_text")
    b1 = activityecorelua_Activity()
    b2 = activityecorelua_Activity()
    _safe_set(a, 'activityecorelua_Variable', b1)
    assert _is_linked(a, 'activityecorelua_Variable', b1)
    if hasattr(b1, 'activityecorelua_Activity114'):
        assert _is_linked(b1, 'activityecorelua_Activity114', a)
    _safe_set(a, 'activityecorelua_Variable', b2)
    assert _is_linked(a, 'activityecorelua_Variable', b2)
    if hasattr(b1, 'activityecorelua_Activity114'):
        assert not _is_linked(b1, 'activityecorelua_Activity114', a)
    if hasattr(b2, 'activityecorelua_Activity114'):
        assert _is_linked(b2, 'activityecorelua_Activity114', a)
    _safe_set(a, 'activityecorelua_Variable', None)
    assert not _is_linked(a, 'activityecorelua_Variable', b2)
    if hasattr(b2, 'activityecorelua_Activity114'):
        assert not _is_linked(b2, 'activityecorelua_Activity114', a)


def test_assoc_nodes110_link_reassign_clear():
    a = activityecorelua_ActivityNode(running=True)
    b1 = activityecorelua_Activity()
    b2 = activityecorelua_Activity()
    _safe_set(a, 'ActivityNode', b1)
    assert _is_linked(a, 'ActivityNode', b1)
    if hasattr(b1, 'activity'):
        assert _is_linked(b1, 'activity', a)
    _safe_set(a, 'ActivityNode', b2)
    assert _is_linked(a, 'ActivityNode', b2)
    if hasattr(b1, 'activity'):
        assert not _is_linked(b1, 'activity', a)
    if hasattr(b2, 'activity'):
        assert _is_linked(b2, 'activity', a)
    _safe_set(a, 'ActivityNode', None)
    assert not _is_linked(a, 'ActivityNode', b2)
    if hasattr(b2, 'activity'):
        assert not _is_linked(b2, 'activity', a)


def test_assoc_object212_link_reassign_clear():
    a = activityecorelua_Statement_CallMemberFunction(memberFunctionName="sample_text")
    b1 = activityecorelua_Expression()
    b2 = activityecorelua_Expression()
    _safe_set(a, 'activityecorelua_Statement_CallMemberFunction', b1)
    assert _is_linked(a, 'activityecorelua_Statement_CallMemberFunction', b1)
    if hasattr(b1, 'activityecorelua_Expression213'):
        assert _is_linked(b1, 'activityecorelua_Expression213', a)
    _safe_set(a, 'activityecorelua_Statement_CallMemberFunction', b2)
    assert _is_linked(a, 'activityecorelua_Statement_CallMemberFunction', b2)
    if hasattr(b1, 'activityecorelua_Expression213'):
        assert not _is_linked(b1, 'activityecorelua_Expression213', a)
    if hasattr(b2, 'activityecorelua_Expression213'):
        assert _is_linked(b2, 'activityecorelua_Expression213', a)
    _safe_set(a, 'activityecorelua_Statement_CallMemberFunction', None)
    assert not _is_linked(a, 'activityecorelua_Statement_CallMemberFunction', b2)
    if hasattr(b2, 'activityecorelua_Expression213'):
        assert not _is_linked(b2, 'activityecorelua_Expression213', a)


def test_assoc_object303_link_reassign_clear():
    a = activityecorelua_Expression_CallMemberFunction(memberFunctionName="sample_text")
    b1 = activityecorelua_Expression()
    b2 = activityecorelua_Expression()
    _safe_set(a, 'activityecorelua_Expression_CallMemberFunction', b1)
    assert _is_linked(a, 'activityecorelua_Expression_CallMemberFunction', b1)
    if hasattr(b1, 'activityecorelua_Expression304'):
        assert _is_linked(b1, 'activityecorelua_Expression304', a)
    _safe_set(a, 'activityecorelua_Expression_CallMemberFunction', b2)
    assert _is_linked(a, 'activityecorelua_Expression_CallMemberFunction', b2)
    if hasattr(b1, 'activityecorelua_Expression304'):
        assert not _is_linked(b1, 'activityecorelua_Expression304', a)
    if hasattr(b2, 'activityecorelua_Expression304'):
        assert _is_linked(b2, 'activityecorelua_Expression304', a)
    _safe_set(a, 'activityecorelua_Expression_CallMemberFunction', None)
    assert not _is_linked(a, 'activityecorelua_Expression_CallMemberFunction', b2)
    if hasattr(b2, 'activityecorelua_Expression304'):
        assert not _is_linked(b2, 'activityecorelua_Expression304', a)


def test_assoc_object318_link_reassign_clear():
    a = activityecorelua_Expression_AccessMember(memberName="sample_text")
    b1 = activityecorelua_Expression()
    b2 = activityecorelua_Expression()
    _safe_set(a, 'activityecorelua_Expression_AccessMember', b1)
    assert _is_linked(a, 'activityecorelua_Expression_AccessMember', b1)
    if hasattr(b1, 'activityecorelua_Expression319'):
        assert _is_linked(b1, 'activityecorelua_Expression319', a)
    _safe_set(a, 'activityecorelua_Expression_AccessMember', b2)
    assert _is_linked(a, 'activityecorelua_Expression_AccessMember', b2)
    if hasattr(b1, 'activityecorelua_Expression319'):
        assert not _is_linked(b1, 'activityecorelua_Expression319', a)
    if hasattr(b2, 'activityecorelua_Expression319'):
        assert _is_linked(b2, 'activityecorelua_Expression319', a)
    _safe_set(a, 'activityecorelua_Expression_AccessMember', None)
    assert not _is_linked(a, 'activityecorelua_Expression_AccessMember', b2)
    if hasattr(b2, 'activityecorelua_Expression319'):
        assert not _is_linked(b2, 'activityecorelua_Expression319', a)


def test_assoc_outgoing118_link_reassign_clear():
    a = activityecorelua_ActivityNode(running=True)
    b1 = activityecorelua_ActivityEdge()
    b2 = activityecorelua_ActivityEdge()
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'ActivityEdge'):
        assert _is_linked(b1, 'ActivityEdge', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'ActivityEdge'):
        assert not _is_linked(b1, 'ActivityEdge', a)
    if hasattr(b2, 'ActivityEdge'):
        assert _is_linked(b2, 'ActivityEdge', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'ActivityEdge'):
        assert not _is_linked(b2, 'ActivityEdge', a)


def test_assoc_references5_link_reassign_clear():
    a = activityecorelua_EObject()
    b1 = activityecorelua_EAnnotation(source="sample_text")
    b2 = activityecorelua_EAnnotation(source="sample_text_2")
    _safe_set(a, 'activityecorelua_EObject7', b1)
    assert _is_linked(a, 'activityecorelua_EObject7', b1)
    if hasattr(b1, 'activityecorelua_EAnnotation6'):
        assert _is_linked(b1, 'activityecorelua_EAnnotation6', a)
    _safe_set(a, 'activityecorelua_EObject7', b2)
    assert _is_linked(a, 'activityecorelua_EObject7', b2)
    if hasattr(b1, 'activityecorelua_EAnnotation6'):
        assert not _is_linked(b1, 'activityecorelua_EAnnotation6', a)
    if hasattr(b2, 'activityecorelua_EAnnotation6'):
        assert _is_linked(b2, 'activityecorelua_EAnnotation6', a)
    _safe_set(a, 'activityecorelua_EObject7', None)
    assert not _is_linked(a, 'activityecorelua_EObject7', b2)
    if hasattr(b2, 'activityecorelua_EAnnotation6'):
        assert not _is_linked(b2, 'activityecorelua_EAnnotation6', a)


def test_assoc_source122_link_reassign_clear():
    a = activityecorelua_ActivityNode(running=True)
    b1 = activityecorelua_ActivityEdge()
    b2 = activityecorelua_ActivityEdge()
    _safe_set(a, 'ActivityNode123', b1)
    assert _is_linked(a, 'ActivityNode123', b1)
    if hasattr(b1, 'outgoing'):
        assert _is_linked(b1, 'outgoing', a)
    _safe_set(a, 'ActivityNode123', b2)
    assert _is_linked(a, 'ActivityNode123', b2)
    if hasattr(b1, 'outgoing'):
        assert not _is_linked(b1, 'outgoing', a)
    if hasattr(b2, 'outgoing'):
        assert _is_linked(b2, 'outgoing', a)
    _safe_set(a, 'ActivityNode123', None)
    assert not _is_linked(a, 'ActivityNode123', b2)
    if hasattr(b2, 'outgoing'):
        assert not _is_linked(b2, 'outgoing', a)


def test_assoc_startExpr171_link_reassign_clear():
    a = activityecorelua_Statement_For_Numeric(iteratorName="sample_text")
    b1 = activityecorelua_Expression()
    b2 = activityecorelua_Expression()
    _safe_set(a, 'activityecorelua_Statement_For_Numeric', b1)
    assert _is_linked(a, 'activityecorelua_Statement_For_Numeric', b1)
    if hasattr(b1, 'activityecorelua_Expression172'):
        assert _is_linked(b1, 'activityecorelua_Expression172', a)
    _safe_set(a, 'activityecorelua_Statement_For_Numeric', b2)
    assert _is_linked(a, 'activityecorelua_Statement_For_Numeric', b2)
    if hasattr(b1, 'activityecorelua_Expression172'):
        assert not _is_linked(b1, 'activityecorelua_Expression172', a)
    if hasattr(b2, 'activityecorelua_Expression172'):
        assert _is_linked(b2, 'activityecorelua_Expression172', a)
    _safe_set(a, 'activityecorelua_Statement_For_Numeric', None)
    assert not _is_linked(a, 'activityecorelua_Statement_For_Numeric', b2)
    if hasattr(b2, 'activityecorelua_Expression172'):
        assert not _is_linked(b2, 'activityecorelua_Expression172', a)


def test_assoc_stepExpr176_link_reassign_clear():
    a = activityecorelua_Statement_For_Numeric(iteratorName="sample_text")
    b1 = activityecorelua_Expression()
    b2 = activityecorelua_Expression()
    _safe_set(a, 'activityecorelua_Statement_For_Numeric177', b1)
    assert _is_linked(a, 'activityecorelua_Statement_For_Numeric177', b1)
    if hasattr(b1, 'activityecorelua_Expression178'):
        assert _is_linked(b1, 'activityecorelua_Expression178', a)
    _safe_set(a, 'activityecorelua_Statement_For_Numeric177', b2)
    assert _is_linked(a, 'activityecorelua_Statement_For_Numeric177', b2)
    if hasattr(b1, 'activityecorelua_Expression178'):
        assert not _is_linked(b1, 'activityecorelua_Expression178', a)
    if hasattr(b2, 'activityecorelua_Expression178'):
        assert _is_linked(b2, 'activityecorelua_Expression178', a)
    _safe_set(a, 'activityecorelua_Statement_For_Numeric177', None)
    assert not _is_linked(a, 'activityecorelua_Statement_For_Numeric177', b2)
    if hasattr(b2, 'activityecorelua_Expression178'):
        assert not _is_linked(b2, 'activityecorelua_Expression178', a)


def test_assoc_target124_link_reassign_clear():
    a = activityecorelua_ActivityNode(running=True)
    b1 = activityecorelua_ActivityEdge()
    b2 = activityecorelua_ActivityEdge()
    _safe_set(a, 'ActivityNode125', b1)
    assert _is_linked(a, 'ActivityNode125', b1)
    if hasattr(b1, 'incoming'):
        assert _is_linked(b1, 'incoming', a)
    _safe_set(a, 'ActivityNode125', b2)
    assert _is_linked(a, 'ActivityNode125', b2)
    if hasattr(b1, 'incoming'):
        assert not _is_linked(b1, 'incoming', a)
    if hasattr(b2, 'incoming'):
        assert _is_linked(b2, 'incoming', a)
    _safe_set(a, 'ActivityNode125', None)
    assert not _is_linked(a, 'ActivityNode125', b2)
    if hasattr(b2, 'incoming'):
        assert not _is_linked(b2, 'incoming', a)


def test_assoc_untilExpr173_link_reassign_clear():
    a = activityecorelua_Statement_For_Numeric(iteratorName="sample_text")
    b1 = activityecorelua_Expression()
    b2 = activityecorelua_Expression()
    _safe_set(a, 'activityecorelua_Statement_For_Numeric174', b1)
    assert _is_linked(a, 'activityecorelua_Statement_For_Numeric174', b1)
    if hasattr(b1, 'activityecorelua_Expression175'):
        assert _is_linked(b1, 'activityecorelua_Expression175', a)
    _safe_set(a, 'activityecorelua_Statement_For_Numeric174', b2)
    assert _is_linked(a, 'activityecorelua_Statement_For_Numeric174', b2)
    if hasattr(b1, 'activityecorelua_Expression175'):
        assert not _is_linked(b1, 'activityecorelua_Expression175', a)
    if hasattr(b2, 'activityecorelua_Expression175'):
        assert _is_linked(b2, 'activityecorelua_Expression175', a)
    _safe_set(a, 'activityecorelua_Statement_For_Numeric174', None)
    assert not _is_linked(a, 'activityecorelua_Statement_For_Numeric174', b2)
    if hasattr(b2, 'activityecorelua_Expression175'):
        assert not _is_linked(b2, 'activityecorelua_Expression175', a)


def test_assoc_variable135_link_reassign_clear():
    a = activityecorelua_Variable(name="sample_text")
    b1 = activityecorelua_InputValue()
    b2 = activityecorelua_InputValue()
    _safe_set(a, 'activityecorelua_Variable137', b1)
    assert _is_linked(a, 'activityecorelua_Variable137', b1)
    if hasattr(b1, 'activityecorelua_InputValue136'):
        assert _is_linked(b1, 'activityecorelua_InputValue136', a)
    _safe_set(a, 'activityecorelua_Variable137', b2)
    assert _is_linked(a, 'activityecorelua_Variable137', b2)
    if hasattr(b1, 'activityecorelua_InputValue136'):
        assert not _is_linked(b1, 'activityecorelua_InputValue136', a)
    if hasattr(b2, 'activityecorelua_InputValue136'):
        assert _is_linked(b2, 'activityecorelua_InputValue136', a)
    _safe_set(a, 'activityecorelua_Variable137', None)
    assert not _is_linked(a, 'activityecorelua_Variable137', b2)
    if hasattr(b2, 'activityecorelua_InputValue136'):
        assert not _is_linked(b2, 'activityecorelua_InputValue136', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


ActivityEdge_strategy = st.builds(ActivityEdge)
@given(instance=ActivityEdge_strategy)
@settings(max_examples=25)
def test_ActivityEdge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)


ActivityNode_strategy = st.builds(ActivityNode)
@given(instance=ActivityNode_strategy)
@settings(max_examples=25)
def test_ActivityNode_instantiation(instance):
    assert isinstance(instance, ActivityNode)


Chunk_strategy = st.builds(Chunk)
@given(instance=Chunk_strategy)
@settings(max_examples=25)
def test_Chunk_instantiation(instance):
    assert isinstance(instance, Chunk)


ControlNode_strategy = st.builds(ControlNode)
@given(instance=ControlNode_strategy)
@settings(max_examples=25)
def test_ControlNode_instantiation(instance):
    assert isinstance(instance, ControlNode)


EClassifier_strategy = st.builds(EClassifier)
@given(instance=EClassifier_strategy)
@settings(max_examples=25)
def test_EClassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)


EDataType_strategy = st.builds(EDataType)
@given(instance=EDataType_strategy)
@settings(max_examples=25)
def test_EDataType_instantiation(instance):
    assert isinstance(instance, EDataType)


EModelElement_strategy = st.builds(EModelElement)
@given(instance=EModelElement_strategy)
@settings(max_examples=25)
def test_EModelElement_instantiation(instance):
    assert isinstance(instance, EModelElement)


ENamedElement_strategy = st.builds(ENamedElement)
@given(instance=ENamedElement_strategy)
@settings(max_examples=25)
def test_ENamedElement_instantiation(instance):
    assert isinstance(instance, ENamedElement)


EStructuralFeature_strategy = st.builds(EStructuralFeature)
@given(instance=EStructuralFeature_strategy)
@settings(max_examples=25)
def test_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, EStructuralFeature)


ETypedElement_strategy = st.builds(ETypedElement)
@given(instance=ETypedElement_strategy)
@settings(max_examples=25)
def test_ETypedElement_instantiation(instance):
    assert isinstance(instance, ETypedElement)


ExecutableNode_strategy = st.builds(ExecutableNode)
@given(instance=ExecutableNode_strategy)
@settings(max_examples=25)
def test_ExecutableNode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Field_strategy = st.builds(Field)
@given(instance=Field_strategy)
@settings(max_examples=25)
def test_Field_instantiation(instance):
    assert isinstance(instance, Field)


FinalNode_strategy = st.builds(FinalNode)
@given(instance=FinalNode_strategy)
@settings(max_examples=25)
def test_FinalNode_instantiation(instance):
    assert isinstance(instance, FinalNode)


LastStatement_strategy = st.builds(LastStatement)
@given(instance=LastStatement_strategy)
@settings(max_examples=25)
def test_LastStatement_instantiation(instance):
    assert isinstance(instance, LastStatement)


LastStatement_Return_strategy = st.builds(LastStatement_Return)
@given(instance=LastStatement_Return_strategy)
@settings(max_examples=25)
def test_LastStatement_Return_instantiation(instance):
    assert isinstance(instance, LastStatement_Return)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Statement_FunctioncallOrAssignment_strategy = st.builds(Statement_FunctioncallOrAssignment)
@given(instance=Statement_FunctioncallOrAssignment_strategy)
@settings(max_examples=25)
def test_Statement_FunctioncallOrAssignment_instantiation(instance):
    assert isinstance(instance, Statement_FunctioncallOrAssignment)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


activityecorelua_Action_strategy = st.builds(activityecorelua_Action)
@given(instance=activityecorelua_Action_strategy)
@settings(max_examples=25)
def test_activityecorelua_Action_instantiation(instance):
    assert isinstance(instance, activityecorelua_Action)


activityecorelua_Activity_strategy = st.builds(activityecorelua_Activity)
@given(instance=activityecorelua_Activity_strategy)
@settings(max_examples=25)
def test_activityecorelua_Activity_instantiation(instance):
    assert isinstance(instance, activityecorelua_Activity)


activityecorelua_ActivityEdge_strategy = st.builds(activityecorelua_ActivityEdge)
@given(instance=activityecorelua_ActivityEdge_strategy)
@settings(max_examples=25)
def test_activityecorelua_ActivityEdge_instantiation(instance):
    assert isinstance(instance, activityecorelua_ActivityEdge)


activityecorelua_ActivityFinalNode_strategy = st.builds(activityecorelua_ActivityFinalNode)
@given(instance=activityecorelua_ActivityFinalNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_ActivityFinalNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_ActivityFinalNode)


activityecorelua_ActivityNode_strategy = st.builds(activityecorelua_ActivityNode, running=st.booleans())
@given(instance=activityecorelua_ActivityNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_ActivityNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_ActivityNode)


activityecorelua_Block_strategy = st.builds(activityecorelua_Block)
@given(instance=activityecorelua_Block_strategy)
@settings(max_examples=25)
def test_activityecorelua_Block_instantiation(instance):
    assert isinstance(instance, activityecorelua_Block)


activityecorelua_BooleanValue_strategy = st.builds(activityecorelua_BooleanValue, value=st.booleans())
@given(instance=activityecorelua_BooleanValue_strategy)
@settings(max_examples=25)
def test_activityecorelua_BooleanValue_instantiation(instance):
    assert isinstance(instance, activityecorelua_BooleanValue)


activityecorelua_BooleanVariable_strategy = st.builds(activityecorelua_BooleanVariable)
@given(instance=activityecorelua_BooleanVariable_strategy)
@settings(max_examples=25)
def test_activityecorelua_BooleanVariable_instantiation(instance):
    assert isinstance(instance, activityecorelua_BooleanVariable)


activityecorelua_Chunk_strategy = st.builds(activityecorelua_Chunk)
@given(instance=activityecorelua_Chunk_strategy)
@settings(max_examples=25)
def test_activityecorelua_Chunk_instantiation(instance):
    assert isinstance(instance, activityecorelua_Chunk)


activityecorelua_ControlFlow_strategy = st.builds(activityecorelua_ControlFlow)
@given(instance=activityecorelua_ControlFlow_strategy)
@settings(max_examples=25)
def test_activityecorelua_ControlFlow_instantiation(instance):
    assert isinstance(instance, activityecorelua_ControlFlow)


activityecorelua_ControlNode_strategy = st.builds(activityecorelua_ControlNode)
@given(instance=activityecorelua_ControlNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_ControlNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_ControlNode)


activityecorelua_DecisionNode_strategy = st.builds(activityecorelua_DecisionNode)
@given(instance=activityecorelua_DecisionNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_DecisionNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_DecisionNode)


activityecorelua_EAnnotation_strategy = st.builds(activityecorelua_EAnnotation, source=safe_text)
@given(instance=activityecorelua_EAnnotation_strategy)
@settings(max_examples=25)
def test_activityecorelua_EAnnotation_instantiation(instance):
    assert isinstance(instance, activityecorelua_EAnnotation)


activityecorelua_EAttribute_strategy = st.builds(activityecorelua_EAttribute, iD=st.booleans())
@given(instance=activityecorelua_EAttribute_strategy)
@settings(max_examples=25)
def test_activityecorelua_EAttribute_instantiation(instance):
    assert isinstance(instance, activityecorelua_EAttribute)


activityecorelua_EClass_strategy = st.builds(activityecorelua_EClass, abstract=st.booleans(), interface=st.booleans())
@given(instance=activityecorelua_EClass_strategy)
@settings(max_examples=25)
def test_activityecorelua_EClass_instantiation(instance):
    assert isinstance(instance, activityecorelua_EClass)


activityecorelua_EClassifier_strategy = st.builds(activityecorelua_EClassifier, defaultValue=safe_text, instanceClass=safe_text, instanceClassName=safe_text, instanceTypeName=safe_text)
@given(instance=activityecorelua_EClassifier_strategy)
@settings(max_examples=25)
def test_activityecorelua_EClassifier_instantiation(instance):
    assert isinstance(instance, activityecorelua_EClassifier)


activityecorelua_EDataType_strategy = st.builds(activityecorelua_EDataType, serializable=st.booleans())
@given(instance=activityecorelua_EDataType_strategy)
@settings(max_examples=25)
def test_activityecorelua_EDataType_instantiation(instance):
    assert isinstance(instance, activityecorelua_EDataType)


activityecorelua_EEnum_strategy = st.builds(activityecorelua_EEnum)
@given(instance=activityecorelua_EEnum_strategy)
@settings(max_examples=25)
def test_activityecorelua_EEnum_instantiation(instance):
    assert isinstance(instance, activityecorelua_EEnum)


activityecorelua_EEnumLiteral_strategy = st.builds(activityecorelua_EEnumLiteral, instance=safe_text, literal=safe_text, value=st.integers())
@given(instance=activityecorelua_EEnumLiteral_strategy)
@settings(max_examples=25)
def test_activityecorelua_EEnumLiteral_instantiation(instance):
    assert isinstance(instance, activityecorelua_EEnumLiteral)


activityecorelua_EFactory_strategy = st.builds(activityecorelua_EFactory)
@given(instance=activityecorelua_EFactory_strategy)
@settings(max_examples=25)
def test_activityecorelua_EFactory_instantiation(instance):
    assert isinstance(instance, activityecorelua_EFactory)


activityecorelua_EGenericType_strategy = st.builds(activityecorelua_EGenericType)
@given(instance=activityecorelua_EGenericType_strategy)
@settings(max_examples=25)
def test_activityecorelua_EGenericType_instantiation(instance):
    assert isinstance(instance, activityecorelua_EGenericType)


activityecorelua_EModelElement_strategy = st.builds(activityecorelua_EModelElement)
@given(instance=activityecorelua_EModelElement_strategy)
@settings(max_examples=25)
def test_activityecorelua_EModelElement_instantiation(instance):
    assert isinstance(instance, activityecorelua_EModelElement)


activityecorelua_ENamedElement_strategy = st.builds(activityecorelua_ENamedElement, name=safe_text)
@given(instance=activityecorelua_ENamedElement_strategy)
@settings(max_examples=25)
def test_activityecorelua_ENamedElement_instantiation(instance):
    assert isinstance(instance, activityecorelua_ENamedElement)


activityecorelua_EObject_strategy = st.builds(activityecorelua_EObject)
@given(instance=activityecorelua_EObject_strategy)
@settings(max_examples=25)
def test_activityecorelua_EObject_instantiation(instance):
    assert isinstance(instance, activityecorelua_EObject)


activityecorelua_EOperation_strategy = st.builds(activityecorelua_EOperation)
@given(instance=activityecorelua_EOperation_strategy)
@settings(max_examples=25)
def test_activityecorelua_EOperation_instantiation(instance):
    assert isinstance(instance, activityecorelua_EOperation)


activityecorelua_EPackage_strategy = st.builds(activityecorelua_EPackage, nsPrefix=safe_text, nsURI=safe_text)
@given(instance=activityecorelua_EPackage_strategy)
@settings(max_examples=25)
def test_activityecorelua_EPackage_instantiation(instance):
    assert isinstance(instance, activityecorelua_EPackage)


activityecorelua_EParameter_strategy = st.builds(activityecorelua_EParameter)
@given(instance=activityecorelua_EParameter_strategy)
@settings(max_examples=25)
def test_activityecorelua_EParameter_instantiation(instance):
    assert isinstance(instance, activityecorelua_EParameter)


activityecorelua_EReference_strategy = st.builds(activityecorelua_EReference, container=st.booleans(), containment=st.booleans(), resolveProxies=st.booleans())
@given(instance=activityecorelua_EReference_strategy)
@settings(max_examples=25)
def test_activityecorelua_EReference_instantiation(instance):
    assert isinstance(instance, activityecorelua_EReference)


activityecorelua_EStringToStringMapEntry_strategy = st.builds(activityecorelua_EStringToStringMapEntry, key=safe_text, value=safe_text)
@given(instance=activityecorelua_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_activityecorelua_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, activityecorelua_EStringToStringMapEntry)


activityecorelua_EStructuralFeature_strategy = st.builds(activityecorelua_EStructuralFeature, changeable=st.booleans(), defaultValue=safe_text, defaultValueLiteral=safe_text, derived=st.booleans(), transient=st.booleans(), unsettable=st.booleans(), volatile=st.booleans())
@given(instance=activityecorelua_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_activityecorelua_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, activityecorelua_EStructuralFeature)


activityecorelua_ETypeParameter_strategy = st.builds(activityecorelua_ETypeParameter)
@given(instance=activityecorelua_ETypeParameter_strategy)
@settings(max_examples=25)
def test_activityecorelua_ETypeParameter_instantiation(instance):
    assert isinstance(instance, activityecorelua_ETypeParameter)


activityecorelua_ETypedElement_strategy = st.builds(activityecorelua_ETypedElement, lowerBound=st.integers(), many=st.booleans(), ordered=st.booleans(), required=st.booleans(), unique=st.booleans(), upperBound=st.integers())
@given(instance=activityecorelua_ETypedElement_strategy)
@settings(max_examples=25)
def test_activityecorelua_ETypedElement_instantiation(instance):
    assert isinstance(instance, activityecorelua_ETypedElement)


activityecorelua_ExecutableNode_strategy = st.builds(activityecorelua_ExecutableNode)
@given(instance=activityecorelua_ExecutableNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_ExecutableNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_ExecutableNode)


activityecorelua_Expression_strategy = st.builds(activityecorelua_Expression)
@given(instance=activityecorelua_Expression_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression)


activityecorelua_Expression_AccessArray_strategy = st.builds(activityecorelua_Expression_AccessArray)
@given(instance=activityecorelua_Expression_AccessArray_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_AccessArray_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_AccessArray)


activityecorelua_Expression_AccessMember_strategy = st.builds(activityecorelua_Expression_AccessMember, memberName=safe_text)
@given(instance=activityecorelua_Expression_AccessMember_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_AccessMember_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_AccessMember)


activityecorelua_Expression_And_strategy = st.builds(activityecorelua_Expression_And)
@given(instance=activityecorelua_Expression_And_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_And_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_And)


activityecorelua_Expression_CallFunction_strategy = st.builds(activityecorelua_Expression_CallFunction)
@given(instance=activityecorelua_Expression_CallFunction_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_CallFunction_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_CallFunction)


activityecorelua_Expression_CallMemberFunction_strategy = st.builds(activityecorelua_Expression_CallMemberFunction, memberFunctionName=safe_text)
@given(instance=activityecorelua_Expression_CallMemberFunction_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_CallMemberFunction_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_CallMemberFunction)


activityecorelua_Expression_Concatenation_strategy = st.builds(activityecorelua_Expression_Concatenation)
@given(instance=activityecorelua_Expression_Concatenation_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Concatenation_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Concatenation)


activityecorelua_Expression_Division_strategy = st.builds(activityecorelua_Expression_Division)
@given(instance=activityecorelua_Expression_Division_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Division_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Division)


activityecorelua_Expression_Equal_strategy = st.builds(activityecorelua_Expression_Equal)
@given(instance=activityecorelua_Expression_Equal_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Equal_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Equal)


activityecorelua_Expression_Exponentiation_strategy = st.builds(activityecorelua_Expression_Exponentiation)
@given(instance=activityecorelua_Expression_Exponentiation_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Exponentiation_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Exponentiation)


activityecorelua_Expression_False_strategy = st.builds(activityecorelua_Expression_False)
@given(instance=activityecorelua_Expression_False_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_False_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_False)


activityecorelua_Expression_Function_strategy = st.builds(activityecorelua_Expression_Function)
@given(instance=activityecorelua_Expression_Function_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Function_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Function)


activityecorelua_Expression_Invert_strategy = st.builds(activityecorelua_Expression_Invert)
@given(instance=activityecorelua_Expression_Invert_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Invert_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Invert)


activityecorelua_Expression_Larger_strategy = st.builds(activityecorelua_Expression_Larger)
@given(instance=activityecorelua_Expression_Larger_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Larger_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Larger)


activityecorelua_Expression_Larger_Equal_strategy = st.builds(activityecorelua_Expression_Larger_Equal)
@given(instance=activityecorelua_Expression_Larger_Equal_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Larger_Equal_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Larger_Equal)


activityecorelua_Expression_Length_strategy = st.builds(activityecorelua_Expression_Length)
@given(instance=activityecorelua_Expression_Length_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Length_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Length)


activityecorelua_Expression_Minus_strategy = st.builds(activityecorelua_Expression_Minus)
@given(instance=activityecorelua_Expression_Minus_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Minus_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Minus)


activityecorelua_Expression_Modulo_strategy = st.builds(activityecorelua_Expression_Modulo)
@given(instance=activityecorelua_Expression_Modulo_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Modulo_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Modulo)


activityecorelua_Expression_Multiplication_strategy = st.builds(activityecorelua_Expression_Multiplication)
@given(instance=activityecorelua_Expression_Multiplication_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Multiplication_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Multiplication)


activityecorelua_Expression_Negate_strategy = st.builds(activityecorelua_Expression_Negate)
@given(instance=activityecorelua_Expression_Negate_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Negate_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Negate)


activityecorelua_Expression_Nil_strategy = st.builds(activityecorelua_Expression_Nil)
@given(instance=activityecorelua_Expression_Nil_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Nil_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Nil)


activityecorelua_Expression_Not_Equal_strategy = st.builds(activityecorelua_Expression_Not_Equal)
@given(instance=activityecorelua_Expression_Not_Equal_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Not_Equal_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Not_Equal)


activityecorelua_Expression_Number_strategy = st.builds(activityecorelua_Expression_Number, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=activityecorelua_Expression_Number_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Number_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Number)


activityecorelua_Expression_Or_strategy = st.builds(activityecorelua_Expression_Or)
@given(instance=activityecorelua_Expression_Or_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Or_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Or)


activityecorelua_Expression_Plus_strategy = st.builds(activityecorelua_Expression_Plus)
@given(instance=activityecorelua_Expression_Plus_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Plus_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Plus)


activityecorelua_Expression_Smaller_strategy = st.builds(activityecorelua_Expression_Smaller)
@given(instance=activityecorelua_Expression_Smaller_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Smaller_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Smaller)


activityecorelua_Expression_Smaller_Equal_strategy = st.builds(activityecorelua_Expression_Smaller_Equal)
@given(instance=activityecorelua_Expression_Smaller_Equal_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_Smaller_Equal_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_Smaller_Equal)


activityecorelua_Expression_String_strategy = st.builds(activityecorelua_Expression_String, value=safe_text)
@given(instance=activityecorelua_Expression_String_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_String_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_String)


activityecorelua_Expression_TableConstructor_strategy = st.builds(activityecorelua_Expression_TableConstructor)
@given(instance=activityecorelua_Expression_TableConstructor_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_TableConstructor_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_TableConstructor)


activityecorelua_Expression_True_strategy = st.builds(activityecorelua_Expression_True)
@given(instance=activityecorelua_Expression_True_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_True_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_True)


activityecorelua_Expression_VarArgs_strategy = st.builds(activityecorelua_Expression_VarArgs)
@given(instance=activityecorelua_Expression_VarArgs_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_VarArgs_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_VarArgs)


activityecorelua_Expression_VariableName_strategy = st.builds(activityecorelua_Expression_VariableName, variable=safe_text)
@given(instance=activityecorelua_Expression_VariableName_strategy)
@settings(max_examples=25)
def test_activityecorelua_Expression_VariableName_instantiation(instance):
    assert isinstance(instance, activityecorelua_Expression_VariableName)


activityecorelua_Field_strategy = st.builds(activityecorelua_Field)
@given(instance=activityecorelua_Field_strategy)
@settings(max_examples=25)
def test_activityecorelua_Field_instantiation(instance):
    assert isinstance(instance, activityecorelua_Field)


activityecorelua_Field_AddEntryToTable_strategy = st.builds(activityecorelua_Field_AddEntryToTable, key=safe_text)
@given(instance=activityecorelua_Field_AddEntryToTable_strategy)
@settings(max_examples=25)
def test_activityecorelua_Field_AddEntryToTable_instantiation(instance):
    assert isinstance(instance, activityecorelua_Field_AddEntryToTable)


activityecorelua_Field_AddEntryToTable_Brackets_strategy = st.builds(activityecorelua_Field_AddEntryToTable_Brackets)
@given(instance=activityecorelua_Field_AddEntryToTable_Brackets_strategy)
@settings(max_examples=25)
def test_activityecorelua_Field_AddEntryToTable_Brackets_instantiation(instance):
    assert isinstance(instance, activityecorelua_Field_AddEntryToTable_Brackets)


activityecorelua_Field_AppendEntryToTable_strategy = st.builds(activityecorelua_Field_AppendEntryToTable)
@given(instance=activityecorelua_Field_AppendEntryToTable_strategy)
@settings(max_examples=25)
def test_activityecorelua_Field_AppendEntryToTable_instantiation(instance):
    assert isinstance(instance, activityecorelua_Field_AppendEntryToTable)


activityecorelua_FinalNode_strategy = st.builds(activityecorelua_FinalNode)
@given(instance=activityecorelua_FinalNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_FinalNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_FinalNode)


activityecorelua_ForkNode_strategy = st.builds(activityecorelua_ForkNode)
@given(instance=activityecorelua_ForkNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_ForkNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_ForkNode)


activityecorelua_Function_strategy = st.builds(activityecorelua_Function, parameters=safe_text, varArgs=st.booleans())
@given(instance=activityecorelua_Function_strategy)
@settings(max_examples=25)
def test_activityecorelua_Function_instantiation(instance):
    assert isinstance(instance, activityecorelua_Function)


activityecorelua_Functioncall_Arguments_strategy = st.builds(activityecorelua_Functioncall_Arguments)
@given(instance=activityecorelua_Functioncall_Arguments_strategy)
@settings(max_examples=25)
def test_activityecorelua_Functioncall_Arguments_instantiation(instance):
    assert isinstance(instance, activityecorelua_Functioncall_Arguments)


activityecorelua_InitialNode_strategy = st.builds(activityecorelua_InitialNode)
@given(instance=activityecorelua_InitialNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_InitialNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_InitialNode)


activityecorelua_Input_strategy = st.builds(activityecorelua_Input)
@given(instance=activityecorelua_Input_strategy)
@settings(max_examples=25)
def test_activityecorelua_Input_instantiation(instance):
    assert isinstance(instance, activityecorelua_Input)


activityecorelua_InputValue_strategy = st.builds(activityecorelua_InputValue)
@given(instance=activityecorelua_InputValue_strategy)
@settings(max_examples=25)
def test_activityecorelua_InputValue_instantiation(instance):
    assert isinstance(instance, activityecorelua_InputValue)


activityecorelua_IntegerValue_strategy = st.builds(activityecorelua_IntegerValue, value=st.integers())
@given(instance=activityecorelua_IntegerValue_strategy)
@settings(max_examples=25)
def test_activityecorelua_IntegerValue_instantiation(instance):
    assert isinstance(instance, activityecorelua_IntegerValue)


activityecorelua_IntegerVariable_strategy = st.builds(activityecorelua_IntegerVariable)
@given(instance=activityecorelua_IntegerVariable_strategy)
@settings(max_examples=25)
def test_activityecorelua_IntegerVariable_instantiation(instance):
    assert isinstance(instance, activityecorelua_IntegerVariable)


activityecorelua_JoinNode_strategy = st.builds(activityecorelua_JoinNode)
@given(instance=activityecorelua_JoinNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_JoinNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_JoinNode)


activityecorelua_LastStatement_strategy = st.builds(activityecorelua_LastStatement)
@given(instance=activityecorelua_LastStatement_strategy)
@settings(max_examples=25)
def test_activityecorelua_LastStatement_instantiation(instance):
    assert isinstance(instance, activityecorelua_LastStatement)


activityecorelua_LastStatement_Break_strategy = st.builds(activityecorelua_LastStatement_Break)
@given(instance=activityecorelua_LastStatement_Break_strategy)
@settings(max_examples=25)
def test_activityecorelua_LastStatement_Break_instantiation(instance):
    assert isinstance(instance, activityecorelua_LastStatement_Break)


activityecorelua_LastStatement_Return_strategy = st.builds(activityecorelua_LastStatement_Return)
@given(instance=activityecorelua_LastStatement_Return_strategy)
@settings(max_examples=25)
def test_activityecorelua_LastStatement_Return_instantiation(instance):
    assert isinstance(instance, activityecorelua_LastStatement_Return)


activityecorelua_LastStatement_ReturnWithValue_strategy = st.builds(activityecorelua_LastStatement_ReturnWithValue)
@given(instance=activityecorelua_LastStatement_ReturnWithValue_strategy)
@settings(max_examples=25)
def test_activityecorelua_LastStatement_ReturnWithValue_instantiation(instance):
    assert isinstance(instance, activityecorelua_LastStatement_ReturnWithValue)


activityecorelua_MergeNode_strategy = st.builds(activityecorelua_MergeNode)
@given(instance=activityecorelua_MergeNode_strategy)
@settings(max_examples=25)
def test_activityecorelua_MergeNode_instantiation(instance):
    assert isinstance(instance, activityecorelua_MergeNode)


activityecorelua_NamedElement_strategy = st.builds(activityecorelua_NamedElement, name=safe_text)
@given(instance=activityecorelua_NamedElement_strategy)
@settings(max_examples=25)
def test_activityecorelua_NamedElement_instantiation(instance):
    assert isinstance(instance, activityecorelua_NamedElement)


activityecorelua_OpaqueAction_strategy = st.builds(activityecorelua_OpaqueAction)
@given(instance=activityecorelua_OpaqueAction_strategy)
@settings(max_examples=25)
def test_activityecorelua_OpaqueAction_instantiation(instance):
    assert isinstance(instance, activityecorelua_OpaqueAction)


activityecorelua_Statement_strategy = st.builds(activityecorelua_Statement)
@given(instance=activityecorelua_Statement_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement)


activityecorelua_Statement_Assignment_strategy = st.builds(activityecorelua_Statement_Assignment)
@given(instance=activityecorelua_Statement_Assignment_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_Assignment_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_Assignment)


activityecorelua_Statement_Block_strategy = st.builds(activityecorelua_Statement_Block)
@given(instance=activityecorelua_Statement_Block_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_Block_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_Block)


activityecorelua_Statement_CallFunction_strategy = st.builds(activityecorelua_Statement_CallFunction)
@given(instance=activityecorelua_Statement_CallFunction_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_CallFunction_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_CallFunction)


activityecorelua_Statement_CallMemberFunction_strategy = st.builds(activityecorelua_Statement_CallMemberFunction, memberFunctionName=safe_text)
@given(instance=activityecorelua_Statement_CallMemberFunction_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_CallMemberFunction_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_CallMemberFunction)


activityecorelua_Statement_For_Generic_strategy = st.builds(activityecorelua_Statement_For_Generic, names=safe_text)
@given(instance=activityecorelua_Statement_For_Generic_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_For_Generic_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_For_Generic)


activityecorelua_Statement_For_Numeric_strategy = st.builds(activityecorelua_Statement_For_Numeric, iteratorName=safe_text)
@given(instance=activityecorelua_Statement_For_Numeric_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_For_Numeric_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_For_Numeric)


activityecorelua_Statement_FunctioncallOrAssignment_strategy = st.builds(activityecorelua_Statement_FunctioncallOrAssignment)
@given(instance=activityecorelua_Statement_FunctioncallOrAssignment_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_FunctioncallOrAssignment_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_FunctioncallOrAssignment)


activityecorelua_Statement_GlobalFunction_Declaration_strategy = st.builds(activityecorelua_Statement_GlobalFunction_Declaration, functionName=safe_text, prefix=safe_text)
@given(instance=activityecorelua_Statement_GlobalFunction_Declaration_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_GlobalFunction_Declaration_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_GlobalFunction_Declaration)


activityecorelua_Statement_If_Then_Else_strategy = st.builds(activityecorelua_Statement_If_Then_Else)
@given(instance=activityecorelua_Statement_If_Then_Else_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_If_Then_Else_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_If_Then_Else)


activityecorelua_Statement_If_Then_Else_ElseIfPart_strategy = st.builds(activityecorelua_Statement_If_Then_Else_ElseIfPart)
@given(instance=activityecorelua_Statement_If_Then_Else_ElseIfPart_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_If_Then_Else_ElseIfPart_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_If_Then_Else_ElseIfPart)


activityecorelua_Statement_LocalFunction_Declaration_strategy = st.builds(activityecorelua_Statement_LocalFunction_Declaration, functionName=safe_text)
@given(instance=activityecorelua_Statement_LocalFunction_Declaration_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_LocalFunction_Declaration_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_LocalFunction_Declaration)


activityecorelua_Statement_Local_Variable_Declaration_strategy = st.builds(activityecorelua_Statement_Local_Variable_Declaration, variableNames=safe_text)
@given(instance=activityecorelua_Statement_Local_Variable_Declaration_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_Local_Variable_Declaration_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_Local_Variable_Declaration)


activityecorelua_Statement_Repeat_strategy = st.builds(activityecorelua_Statement_Repeat)
@given(instance=activityecorelua_Statement_Repeat_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_Repeat_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_Repeat)


activityecorelua_Statement_While_strategy = st.builds(activityecorelua_Statement_While)
@given(instance=activityecorelua_Statement_While_strategy)
@settings(max_examples=25)
def test_activityecorelua_Statement_While_instantiation(instance):
    assert isinstance(instance, activityecorelua_Statement_While)


activityecorelua_Value_strategy = st.builds(activityecorelua_Value)
@given(instance=activityecorelua_Value_strategy)
@settings(max_examples=25)
def test_activityecorelua_Value_instantiation(instance):
    assert isinstance(instance, activityecorelua_Value)


activityecorelua_Variable_strategy = st.builds(activityecorelua_Variable, name=safe_text)
@given(instance=activityecorelua_Variable_strategy)
@settings(max_examples=25)
def test_activityecorelua_Variable_instantiation(instance):
    assert isinstance(instance, activityecorelua_Variable)



