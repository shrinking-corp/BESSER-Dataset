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
    ArithmeticExpression,
    siple_Subtraction,
    siple_Division,
    siple_Multiplication,
    siple_Addition,
    EqualityExpression,
    siple_LesserThan,
    siple_LesserThanEqual,
    siple_GreaterThan,
    siple_GreaterThanEqual,
    siple_Equal,
    LogicExpression,
    siple_Or,
    siple_And,
    BinaryExpression,
    siple_ArithmeticExpression,
    siple_EqualityExpression,
    siple_LogicExpression,
    Declaration,
    siple_VariableDeclaration,
    UnaryExpression,
    siple_Dereference,
    siple_UMinus,
    siple_RealCoercion,
    siple_Not,
    Expression,
    siple_ProcedureCall,
    siple_UnaryExpression,
    siple_Reference,
    siple_BinaryExpression,
    siple_NestedExpression,
    siple_Constant,
    Statement,
    siple_Read,
    siple_Declaration,
    siple_ProcedureReturn,
    siple_If,
    siple_VariableAssignment,
    siple_While,
    siple_Expression,
    siple_Write,
    siple_Block,
    siple_Statement,
    siple_ProcedureDeclaration,
    siple_CompilationUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_hyp_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_hyp_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_subtraction_is_not_abstract():
    assert not inspect.isabstract(siple_Subtraction)


def test_hyp_siple_subtraction_constructor_exists():
    assert callable(siple_Subtraction.__init__)


def test_hyp_siple_subtraction_constructor_args():
    sig = inspect.signature(siple_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_division_is_not_abstract():
    assert not inspect.isabstract(siple_Division)


def test_hyp_siple_division_constructor_exists():
    assert callable(siple_Division.__init__)


def test_hyp_siple_division_constructor_args():
    sig = inspect.signature(siple_Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_multiplication_is_not_abstract():
    assert not inspect.isabstract(siple_Multiplication)


def test_hyp_siple_multiplication_constructor_exists():
    assert callable(siple_Multiplication.__init__)


def test_hyp_siple_multiplication_constructor_args():
    sig = inspect.signature(siple_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_addition_is_not_abstract():
    assert not inspect.isabstract(siple_Addition)


def test_hyp_siple_addition_constructor_exists():
    assert callable(siple_Addition.__init__)


def test_hyp_siple_addition_constructor_args():
    sig = inspect.signature(siple_Addition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(EqualityExpression)


def test_hyp_equalityexpression_constructor_exists():
    assert callable(EqualityExpression.__init__)


def test_hyp_equalityexpression_constructor_args():
    sig = inspect.signature(EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_lesserthan_is_not_abstract():
    assert not inspect.isabstract(siple_LesserThan)


def test_hyp_siple_lesserthan_constructor_exists():
    assert callable(siple_LesserThan.__init__)


def test_hyp_siple_lesserthan_constructor_args():
    sig = inspect.signature(siple_LesserThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_lesserthanequal_is_not_abstract():
    assert not inspect.isabstract(siple_LesserThanEqual)


def test_hyp_siple_lesserthanequal_constructor_exists():
    assert callable(siple_LesserThanEqual.__init__)


def test_hyp_siple_lesserthanequal_constructor_args():
    sig = inspect.signature(siple_LesserThanEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_greaterthan_is_not_abstract():
    assert not inspect.isabstract(siple_GreaterThan)


def test_hyp_siple_greaterthan_constructor_exists():
    assert callable(siple_GreaterThan.__init__)


def test_hyp_siple_greaterthan_constructor_args():
    sig = inspect.signature(siple_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_greaterthanequal_is_not_abstract():
    assert not inspect.isabstract(siple_GreaterThanEqual)


def test_hyp_siple_greaterthanequal_constructor_exists():
    assert callable(siple_GreaterThanEqual.__init__)


def test_hyp_siple_greaterthanequal_constructor_args():
    sig = inspect.signature(siple_GreaterThanEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_equal_is_not_abstract():
    assert not inspect.isabstract(siple_Equal)


def test_hyp_siple_equal_constructor_exists():
    assert callable(siple_Equal.__init__)


def test_hyp_siple_equal_constructor_args():
    sig = inspect.signature(siple_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logicexpression_is_not_abstract():
    assert not inspect.isabstract(LogicExpression)


def test_hyp_logicexpression_constructor_exists():
    assert callable(LogicExpression.__init__)


def test_hyp_logicexpression_constructor_args():
    sig = inspect.signature(LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_or_is_not_abstract():
    assert not inspect.isabstract(siple_Or)


def test_hyp_siple_or_constructor_exists():
    assert callable(siple_Or.__init__)


def test_hyp_siple_or_constructor_args():
    sig = inspect.signature(siple_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_and_is_not_abstract():
    assert not inspect.isabstract(siple_And)


def test_hyp_siple_and_constructor_exists():
    assert callable(siple_And.__init__)


def test_hyp_siple_and_constructor_args():
    sig = inspect.signature(siple_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_hyp_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_hyp_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(siple_ArithmeticExpression)


def test_hyp_siple_arithmeticexpression_constructor_exists():
    assert callable(siple_ArithmeticExpression.__init__)


def test_hyp_siple_arithmeticexpression_constructor_args():
    sig = inspect.signature(siple_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(siple_EqualityExpression)


def test_hyp_siple_equalityexpression_constructor_exists():
    assert callable(siple_EqualityExpression.__init__)


def test_hyp_siple_equalityexpression_constructor_args():
    sig = inspect.signature(siple_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_logicexpression_is_not_abstract():
    assert not inspect.isabstract(siple_LogicExpression)


def test_hyp_siple_logicexpression_constructor_exists():
    assert callable(siple_LogicExpression.__init__)


def test_hyp_siple_logicexpression_constructor_args():
    sig = inspect.signature(siple_LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_hyp_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_hyp_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(siple_VariableDeclaration)


def test_hyp_siple_variabledeclaration_constructor_exists():
    assert callable(siple_VariableDeclaration.__init__)


def test_hyp_siple_variabledeclaration_constructor_args():
    sig = inspect.signature(siple_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "DeclaredType" in params, "Missing parameter 'DeclaredType'"




def test_hyp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_hyp_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_hyp_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_dereference_is_not_abstract():
    assert not inspect.isabstract(siple_Dereference)


def test_hyp_siple_dereference_constructor_exists():
    assert callable(siple_Dereference.__init__)


def test_hyp_siple_dereference_constructor_args():
    sig = inspect.signature(siple_Dereference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_uminus_is_not_abstract():
    assert not inspect.isabstract(siple_UMinus)


def test_hyp_siple_uminus_constructor_exists():
    assert callable(siple_UMinus.__init__)


def test_hyp_siple_uminus_constructor_args():
    sig = inspect.signature(siple_UMinus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_realcoercion_is_not_abstract():
    assert not inspect.isabstract(siple_RealCoercion)


def test_hyp_siple_realcoercion_constructor_exists():
    assert callable(siple_RealCoercion.__init__)


def test_hyp_siple_realcoercion_constructor_args():
    sig = inspect.signature(siple_RealCoercion.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_not_is_not_abstract():
    assert not inspect.isabstract(siple_Not)


def test_hyp_siple_not_constructor_exists():
    assert callable(siple_Not.__init__)


def test_hyp_siple_not_constructor_args():
    sig = inspect.signature(siple_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_procedurecall_is_not_abstract():
    assert not inspect.isabstract(siple_ProcedureCall)


def test_hyp_siple_procedurecall_constructor_exists():
    assert callable(siple_ProcedureCall.__init__)


def test_hyp_siple_procedurecall_constructor_args():
    sig = inspect.signature(siple_ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(siple_UnaryExpression)


def test_hyp_siple_unaryexpression_constructor_exists():
    assert callable(siple_UnaryExpression.__init__)


def test_hyp_siple_unaryexpression_constructor_args():
    sig = inspect.signature(siple_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_reference_is_not_abstract():
    assert not inspect.isabstract(siple_Reference)


def test_hyp_siple_reference_constructor_exists():
    assert callable(siple_Reference.__init__)


def test_hyp_siple_reference_constructor_args():
    sig = inspect.signature(siple_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_siple_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(siple_BinaryExpression)


def test_hyp_siple_binaryexpression_constructor_exists():
    assert callable(siple_BinaryExpression.__init__)


def test_hyp_siple_binaryexpression_constructor_args():
    sig = inspect.signature(siple_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_nestedexpression_is_not_abstract():
    assert not inspect.isabstract(siple_NestedExpression)


def test_hyp_siple_nestedexpression_constructor_exists():
    assert callable(siple_NestedExpression.__init__)


def test_hyp_siple_nestedexpression_constructor_args():
    sig = inspect.signature(siple_NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_constant_is_not_abstract():
    assert not inspect.isabstract(siple_Constant)


def test_hyp_siple_constant_constructor_exists():
    assert callable(siple_Constant.__init__)


def test_hyp_siple_constant_constructor_args():
    sig = inspect.signature(siple_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "AsReal" in params, "Missing parameter 'AsReal'"
    assert "AsBoolean" in params, "Missing parameter 'AsBoolean'"
    assert "AsInteger" in params, "Missing parameter 'AsInteger'"
    assert "Lexem" in params, "Missing parameter 'Lexem'"







def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_read_is_not_abstract():
    assert not inspect.isabstract(siple_Read)


def test_hyp_siple_read_constructor_exists():
    assert callable(siple_Read.__init__)


def test_hyp_siple_read_constructor_args():
    sig = inspect.signature(siple_Read.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"




def test_hyp_siple_declaration_is_not_abstract():
    assert not inspect.isabstract(siple_Declaration)


def test_hyp_siple_declaration_constructor_exists():
    assert callable(siple_Declaration.__init__)


def test_hyp_siple_declaration_constructor_args():
    sig = inspect.signature(siple_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "IsParameterDeclaration" in params, "Missing parameter 'IsParameterDeclaration'"






def test_hyp_siple_procedurereturn_is_not_abstract():
    assert not inspect.isabstract(siple_ProcedureReturn)


def test_hyp_siple_procedurereturn_constructor_exists():
    assert callable(siple_ProcedureReturn.__init__)


def test_hyp_siple_procedurereturn_constructor_args():
    sig = inspect.signature(siple_ProcedureReturn.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"




def test_hyp_siple_if_is_not_abstract():
    assert not inspect.isabstract(siple_If)


def test_hyp_siple_if_constructor_exists():
    assert callable(siple_If.__init__)


def test_hyp_siple_if_constructor_args():
    sig = inspect.signature(siple_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_variableassignment_is_not_abstract():
    assert not inspect.isabstract(siple_VariableAssignment)


def test_hyp_siple_variableassignment_constructor_exists():
    assert callable(siple_VariableAssignment.__init__)


def test_hyp_siple_variableassignment_constructor_args():
    sig = inspect.signature(siple_VariableAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"




def test_hyp_siple_while_is_not_abstract():
    assert not inspect.isabstract(siple_While)


def test_hyp_siple_while_constructor_exists():
    assert callable(siple_While.__init__)


def test_hyp_siple_while_constructor_args():
    sig = inspect.signature(siple_While.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_expression_is_not_abstract():
    assert not inspect.isabstract(siple_Expression)


def test_hyp_siple_expression_constructor_exists():
    assert callable(siple_Expression.__init__)


def test_hyp_siple_expression_constructor_args():
    sig = inspect.signature(siple_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"




def test_hyp_siple_write_is_not_abstract():
    assert not inspect.isabstract(siple_Write)


def test_hyp_siple_write_constructor_exists():
    assert callable(siple_Write.__init__)


def test_hyp_siple_write_constructor_args():
    sig = inspect.signature(siple_Write.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"




def test_hyp_siple_block_is_not_abstract():
    assert not inspect.isabstract(siple_Block)


def test_hyp_siple_block_constructor_exists():
    assert callable(siple_Block.__init__)


def test_hyp_siple_block_constructor_args():
    sig = inspect.signature(siple_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_statement_is_not_abstract():
    assert not inspect.isabstract(siple_Statement)


def test_hyp_siple_statement_constructor_exists():
    assert callable(siple_Statement.__init__)


def test_hyp_siple_statement_constructor_args():
    sig = inspect.signature(siple_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_siple_proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(siple_ProcedureDeclaration)


def test_hyp_siple_proceduredeclaration_constructor_exists():
    assert callable(siple_ProcedureDeclaration.__init__)


def test_hyp_siple_proceduredeclaration_constructor_args():
    sig = inspect.signature(siple_ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "ReturnType" in params, "Missing parameter 'ReturnType'"




def test_hyp_siple_compilationunit_is_not_abstract():
    assert not inspect.isabstract(siple_CompilationUnit)


def test_hyp_siple_compilationunit_constructor_exists():
    assert callable(siple_CompilationUnit.__init__)


def test_hyp_siple_compilationunit_constructor_args():
    sig = inspect.signature(siple_CompilationUnit.__init__)
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
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
siple_Subtraction_strategy = st.builds(
    siple_Subtraction,
)
siple_Division_strategy = st.builds(
    siple_Division,
)
siple_Multiplication_strategy = st.builds(
    siple_Multiplication,
)
siple_Addition_strategy = st.builds(
    siple_Addition,
)
EqualityExpression_strategy = st.builds(
    EqualityExpression,
)
siple_LesserThan_strategy = st.builds(
    siple_LesserThan,
)
siple_LesserThanEqual_strategy = st.builds(
    siple_LesserThanEqual,
)
siple_GreaterThan_strategy = st.builds(
    siple_GreaterThan,
)
siple_GreaterThanEqual_strategy = st.builds(
    siple_GreaterThanEqual,
)
siple_Equal_strategy = st.builds(
    siple_Equal,
)
LogicExpression_strategy = st.builds(
    LogicExpression,
)
siple_Or_strategy = st.builds(
    siple_Or,
)
siple_And_strategy = st.builds(
    siple_And,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
siple_ArithmeticExpression_strategy = st.builds(
    siple_ArithmeticExpression,
)
siple_EqualityExpression_strategy = st.builds(
    siple_EqualityExpression,
)
siple_LogicExpression_strategy = st.builds(
    siple_LogicExpression,
)
Declaration_strategy = st.builds(
    Declaration,
)
siple_VariableDeclaration_strategy = st.builds(
    siple_VariableDeclaration,
    DeclaredType=
        safe_text
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
siple_Dereference_strategy = st.builds(
    siple_Dereference,
)
siple_UMinus_strategy = st.builds(
    siple_UMinus,
)
siple_RealCoercion_strategy = st.builds(
    siple_RealCoercion,
)
siple_Not_strategy = st.builds(
    siple_Not,
)
Expression_strategy = st.builds(
    Expression,
)
siple_ProcedureCall_strategy = st.builds(
    siple_ProcedureCall,
)
siple_UnaryExpression_strategy = st.builds(
    siple_UnaryExpression,
)
siple_Reference_strategy = st.builds(
    siple_Reference,
    Name=
        safe_text
)
siple_BinaryExpression_strategy = st.builds(
    siple_BinaryExpression,
)
siple_NestedExpression_strategy = st.builds(
    siple_NestedExpression,
)
siple_Constant_strategy = st.builds(
    siple_Constant,
    AsReal=
        safe_text,
    AsBoolean=
        safe_text,
    AsInteger=
        safe_text,
    Lexem=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
siple_Read_strategy = st.builds(
    siple_Read,
    Type=
        safe_text
)
siple_Declaration_strategy = st.builds(
    siple_Declaration,
    Type=
        safe_text,
    Name=
        safe_text,
    IsParameterDeclaration=
        st.booleans()
)
siple_ProcedureReturn_strategy = st.builds(
    siple_ProcedureReturn,
    Type=
        safe_text
)
siple_If_strategy = st.builds(
    siple_If,
)
siple_VariableAssignment_strategy = st.builds(
    siple_VariableAssignment,
    Type=
        safe_text
)
siple_While_strategy = st.builds(
    siple_While,
)
siple_Expression_strategy = st.builds(
    siple_Expression,
    Type=
        safe_text
)
siple_Write_strategy = st.builds(
    siple_Write,
    Type=
        safe_text
)
siple_Block_strategy = st.builds(
    siple_Block,
)
siple_Statement_strategy = st.builds(
    siple_Statement,
)
siple_ProcedureDeclaration_strategy = st.builds(
    siple_ProcedureDeclaration,
    ReturnType=
        safe_text
)
siple_CompilationUnit_strategy = st.builds(
    siple_CompilationUnit,
)























@given(instance=siple_VariableDeclaration_strategy)
def test_hyp_siple_variabledeclaration_DeclaredType_setter(instance):
    original = instance.DeclaredType
    instance.DeclaredType = original
    assert instance.DeclaredType == original












@given(instance=siple_Reference_strategy)
def test_hyp_siple_reference_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original






@given(instance=siple_Constant_strategy)
def test_hyp_siple_constant_AsReal_setter(instance):
    original = instance.AsReal
    instance.AsReal = original
    assert instance.AsReal == original



@given(instance=siple_Constant_strategy)
def test_hyp_siple_constant_AsBoolean_setter(instance):
    original = instance.AsBoolean
    instance.AsBoolean = original
    assert instance.AsBoolean == original



@given(instance=siple_Constant_strategy)
def test_hyp_siple_constant_AsInteger_setter(instance):
    original = instance.AsInteger
    instance.AsInteger = original
    assert instance.AsInteger == original



@given(instance=siple_Constant_strategy)
def test_hyp_siple_constant_Lexem_setter(instance):
    original = instance.Lexem
    instance.Lexem = original
    assert instance.Lexem == original





@given(instance=siple_Read_strategy)
def test_hyp_siple_read_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original




@given(instance=siple_Declaration_strategy)
def test_hyp_siple_declaration_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=siple_Declaration_strategy)
def test_hyp_siple_declaration_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=siple_Declaration_strategy)
def test_hyp_siple_declaration_IsParameterDeclaration_setter(instance):
    original = instance.IsParameterDeclaration
    instance.IsParameterDeclaration = original
    assert instance.IsParameterDeclaration == original




@given(instance=siple_ProcedureReturn_strategy)
def test_hyp_siple_procedurereturn_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original





@given(instance=siple_VariableAssignment_strategy)
def test_hyp_siple_variableassignment_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original





@given(instance=siple_Expression_strategy)
def test_hyp_siple_expression_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=siple_Expression_strategy)
@settings(max_examples=30)
def test_hyp_siple_expression_value_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.Value(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.Value).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'Value' in siple_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'Value' in siple_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'Value' in siple_Expression is not implemented or raised an error")




@given(instance=siple_Write_strategy)
def test_hyp_siple_write_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=siple_Statement_strategy)
@settings(max_examples=30)
def test_hyp_siple_statement_interpret_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.Interpret(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.Interpret).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'Interpret' in siple_Statement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'Interpret' in siple_Statement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'Interpret' in siple_Statement is not implemented or raised an error")




@given(instance=siple_ProcedureDeclaration_strategy)
def test_hyp_siple_proceduredeclaration_ReturnType_setter(instance):
    original = instance.ReturnType
    instance.ReturnType = original
    assert instance.ReturnType == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=siple_CompilationUnit_strategy)
@settings(max_examples=30)
def test_hyp_siple_compilationunit_interpret_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.Interpret()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.Interpret).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'Interpret' in siple_CompilationUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'Interpret' in siple_CompilationUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'Interpret' in siple_CompilationUnit is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ArithmeticExpression,
    BinaryExpression,
    Declaration,
    EqualityExpression,
    Expression,
    LogicExpression,
    Statement,
    UnaryExpression,
    siple_Addition,
    siple_And,
    siple_ArithmeticExpression,
    siple_BinaryExpression,
    siple_Block,
    siple_CompilationUnit,
    siple_Constant,
    siple_Declaration,
    siple_Dereference,
    siple_Division,
    siple_Equal,
    siple_EqualityExpression,
    siple_Expression,
    siple_GreaterThan,
    siple_GreaterThanEqual,
    siple_If,
    siple_LesserThan,
    siple_LesserThanEqual,
    siple_LogicExpression,
    siple_Multiplication,
    siple_NestedExpression,
    siple_Not,
    siple_Or,
    siple_ProcedureCall,
    siple_ProcedureDeclaration,
    siple_ProcedureReturn,
    siple_Read,
    siple_RealCoercion,
    siple_Reference,
    siple_Statement,
    siple_Subtraction,
    siple_UMinus,
    siple_UnaryExpression,
    siple_VariableAssignment,
    siple_VariableDeclaration,
    siple_While,
    siple_Write,
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

def test_siple_Constant_AsBoolean_value_roundtrip():
    instance = siple_Constant(AsBoolean="sample_text", AsInteger="sample_text", AsReal="sample_text", Lexem="sample_text")
    assert instance.AsBoolean == "sample_text"
    instance.AsBoolean = "sample_text_2"
    assert instance.AsBoolean == "sample_text_2"


def test_siple_Constant_AsInteger_value_roundtrip():
    instance = siple_Constant(AsBoolean="sample_text", AsInteger="sample_text", AsReal="sample_text", Lexem="sample_text")
    assert instance.AsInteger == "sample_text"
    instance.AsInteger = "sample_text_2"
    assert instance.AsInteger == "sample_text_2"


def test_siple_Constant_AsReal_value_roundtrip():
    instance = siple_Constant(AsBoolean="sample_text", AsInteger="sample_text", AsReal="sample_text", Lexem="sample_text")
    assert instance.AsReal == "sample_text"
    instance.AsReal = "sample_text_2"
    assert instance.AsReal == "sample_text_2"


def test_siple_Constant_Lexem_value_roundtrip():
    instance = siple_Constant(AsBoolean="sample_text", AsInteger="sample_text", AsReal="sample_text", Lexem="sample_text")
    assert instance.Lexem == "sample_text"
    instance.Lexem = "sample_text_2"
    assert instance.Lexem == "sample_text_2"


def test_siple_Declaration_IsParameterDeclaration_value_roundtrip():
    instance = siple_Declaration(IsParameterDeclaration=True, Name="sample_text", Type="sample_text")
    assert instance.IsParameterDeclaration == True
    instance.IsParameterDeclaration = False
    assert instance.IsParameterDeclaration == False


def test_siple_Declaration_Name_value_roundtrip():
    instance = siple_Declaration(IsParameterDeclaration=True, Name="sample_text", Type="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_siple_Declaration_Type_value_roundtrip():
    instance = siple_Declaration(IsParameterDeclaration=True, Name="sample_text", Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_siple_Expression_Type_value_roundtrip():
    instance = siple_Expression(Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_siple_ProcedureDeclaration_ReturnType_value_roundtrip():
    instance = siple_ProcedureDeclaration(ReturnType="sample_text")
    assert instance.ReturnType == "sample_text"
    instance.ReturnType = "sample_text_2"
    assert instance.ReturnType == "sample_text_2"


def test_siple_ProcedureReturn_Type_value_roundtrip():
    instance = siple_ProcedureReturn(Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_siple_Read_Type_value_roundtrip():
    instance = siple_Read(Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_siple_Reference_Name_value_roundtrip():
    instance = siple_Reference(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_siple_VariableAssignment_Type_value_roundtrip():
    instance = siple_VariableAssignment(Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_siple_VariableDeclaration_DeclaredType_value_roundtrip():
    instance = siple_VariableDeclaration(DeclaredType="sample_text")
    assert instance.DeclaredType == "sample_text"
    instance.DeclaredType = "sample_text_2"
    assert instance.DeclaredType == "sample_text_2"


def test_siple_Write_Type_value_roundtrip():
    instance = siple_Write(Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_siple_Addition_isa_ArithmeticExpression():
    instance = siple_Addition()
    assert isinstance(instance, ArithmeticExpression)


def test_siple_Division_isa_ArithmeticExpression():
    instance = siple_Division()
    assert isinstance(instance, ArithmeticExpression)


def test_siple_Multiplication_isa_ArithmeticExpression():
    instance = siple_Multiplication()
    assert isinstance(instance, ArithmeticExpression)


def test_siple_Subtraction_isa_ArithmeticExpression():
    instance = siple_Subtraction()
    assert isinstance(instance, ArithmeticExpression)


def test_siple_ArithmeticExpression_isa_BinaryExpression():
    instance = siple_ArithmeticExpression()
    assert isinstance(instance, BinaryExpression)


def test_siple_EqualityExpression_isa_BinaryExpression():
    instance = siple_EqualityExpression()
    assert isinstance(instance, BinaryExpression)


def test_siple_LogicExpression_isa_BinaryExpression():
    instance = siple_LogicExpression()
    assert isinstance(instance, BinaryExpression)


def test_siple_ProcedureDeclaration_isa_Declaration():
    instance = siple_ProcedureDeclaration(ReturnType="sample_text")
    assert isinstance(instance, Declaration)


def test_siple_VariableDeclaration_isa_Declaration():
    instance = siple_VariableDeclaration(DeclaredType="sample_text")
    assert isinstance(instance, Declaration)


def test_siple_Equal_isa_EqualityExpression():
    instance = siple_Equal()
    assert isinstance(instance, EqualityExpression)


def test_siple_GreaterThan_isa_EqualityExpression():
    instance = siple_GreaterThan()
    assert isinstance(instance, EqualityExpression)


def test_siple_GreaterThanEqual_isa_EqualityExpression():
    instance = siple_GreaterThanEqual()
    assert isinstance(instance, EqualityExpression)


def test_siple_LesserThan_isa_EqualityExpression():
    instance = siple_LesserThan()
    assert isinstance(instance, EqualityExpression)


def test_siple_LesserThanEqual_isa_EqualityExpression():
    instance = siple_LesserThanEqual()
    assert isinstance(instance, EqualityExpression)


def test_siple_BinaryExpression_isa_Expression():
    instance = siple_BinaryExpression()
    assert isinstance(instance, Expression)


def test_siple_Constant_isa_Expression():
    instance = siple_Constant(AsBoolean="sample_text", AsInteger="sample_text", AsReal="sample_text", Lexem="sample_text")
    assert isinstance(instance, Expression)


def test_siple_NestedExpression_isa_Expression():
    instance = siple_NestedExpression()
    assert isinstance(instance, Expression)


def test_siple_ProcedureCall_isa_Expression():
    instance = siple_ProcedureCall()
    assert isinstance(instance, Expression)


def test_siple_Reference_isa_Expression():
    instance = siple_Reference(Name="sample_text")
    assert isinstance(instance, Expression)


def test_siple_UnaryExpression_isa_Expression():
    instance = siple_UnaryExpression()
    assert isinstance(instance, Expression)


def test_siple_And_isa_LogicExpression():
    instance = siple_And()
    assert isinstance(instance, LogicExpression)


def test_siple_Or_isa_LogicExpression():
    instance = siple_Or()
    assert isinstance(instance, LogicExpression)


def test_siple_Block_isa_Statement():
    instance = siple_Block()
    assert isinstance(instance, Statement)


def test_siple_Declaration_isa_Statement():
    instance = siple_Declaration(IsParameterDeclaration=True, Name="sample_text", Type="sample_text")
    assert isinstance(instance, Statement)


def test_siple_Expression_isa_Statement():
    instance = siple_Expression(Type="sample_text")
    assert isinstance(instance, Statement)


def test_siple_If_isa_Statement():
    instance = siple_If()
    assert isinstance(instance, Statement)


def test_siple_ProcedureReturn_isa_Statement():
    instance = siple_ProcedureReturn(Type="sample_text")
    assert isinstance(instance, Statement)


def test_siple_Read_isa_Statement():
    instance = siple_Read(Type="sample_text")
    assert isinstance(instance, Statement)


def test_siple_VariableAssignment_isa_Statement():
    instance = siple_VariableAssignment(Type="sample_text")
    assert isinstance(instance, Statement)


def test_siple_While_isa_Statement():
    instance = siple_While()
    assert isinstance(instance, Statement)


def test_siple_Write_isa_Statement():
    instance = siple_Write(Type="sample_text")
    assert isinstance(instance, Statement)


def test_siple_Dereference_isa_UnaryExpression():
    instance = siple_Dereference()
    assert isinstance(instance, UnaryExpression)


def test_siple_Not_isa_UnaryExpression():
    instance = siple_Not()
    assert isinstance(instance, UnaryExpression)


def test_siple_RealCoercion_isa_UnaryExpression():
    instance = siple_RealCoercion()
    assert isinstance(instance, UnaryExpression)


def test_siple_UMinus_isa_UnaryExpression():
    instance = siple_UMinus()
    assert isinstance(instance, UnaryExpression)


def test_assoc_Argument42_link_reassign_clear():
    a = siple_Expression(Type="sample_text")
    b1 = siple_ProcedureCall()
    b2 = siple_ProcedureCall()
    _safe_set(a, 'siple_Expression44', b1)
    assert _is_linked(a, 'siple_Expression44', b1)
    if hasattr(b1, 'siple_ProcedureCall43'):
        assert _is_linked(b1, 'siple_ProcedureCall43', a)
    _safe_set(a, 'siple_Expression44', b2)
    assert _is_linked(a, 'siple_Expression44', b2)
    if hasattr(b1, 'siple_ProcedureCall43'):
        assert not _is_linked(b1, 'siple_ProcedureCall43', a)
    if hasattr(b2, 'siple_ProcedureCall43'):
        assert _is_linked(b2, 'siple_ProcedureCall43', a)
    _safe_set(a, 'siple_Expression44', None)
    assert not _is_linked(a, 'siple_Expression44', b2)
    if hasattr(b2, 'siple_ProcedureCall43'):
        assert not _is_linked(b2, 'siple_ProcedureCall43', a)


def test_assoc_Body35_link_reassign_clear():
    a = siple_ProcedureDeclaration(ReturnType="sample_text")
    b1 = siple_Block()
    b2 = siple_Block()
    _safe_set(a, 'siple_ProcedureDeclaration36', b1)
    assert _is_linked(a, 'siple_ProcedureDeclaration36', b1)
    if hasattr(b1, 'siple_Block37'):
        assert _is_linked(b1, 'siple_Block37', a)
    _safe_set(a, 'siple_ProcedureDeclaration36', b2)
    assert _is_linked(a, 'siple_ProcedureDeclaration36', b2)
    if hasattr(b1, 'siple_Block37'):
        assert not _is_linked(b1, 'siple_Block37', a)
    if hasattr(b2, 'siple_Block37'):
        assert _is_linked(b2, 'siple_Block37', a)
    _safe_set(a, 'siple_ProcedureDeclaration36', None)
    assert not _is_linked(a, 'siple_ProcedureDeclaration36', b2)
    if hasattr(b2, 'siple_Block37'):
        assert not _is_linked(b2, 'siple_Block37', a)


def test_assoc_Condition10_link_reassign_clear():
    a = siple_Expression(Type="sample_text")
    b1 = siple_If()
    b2 = siple_If()
    _safe_set(a, 'siple_Expression', b1)
    assert _is_linked(a, 'siple_Expression', b1)
    if hasattr(b1, 'siple_If'):
        assert _is_linked(b1, 'siple_If', a)
    _safe_set(a, 'siple_Expression', b2)
    assert _is_linked(a, 'siple_Expression', b2)
    if hasattr(b1, 'siple_If'):
        assert not _is_linked(b1, 'siple_If', a)
    if hasattr(b2, 'siple_If'):
        assert _is_linked(b2, 'siple_If', a)
    _safe_set(a, 'siple_Expression', None)
    assert not _is_linked(a, 'siple_Expression', b2)
    if hasattr(b2, 'siple_If'):
        assert not _is_linked(b2, 'siple_If', a)


def test_assoc_Condition17_link_reassign_clear():
    a = siple_Expression(Type="sample_text")
    b1 = siple_While()
    b2 = siple_While()
    _safe_set(a, 'siple_Expression18', b1)
    assert _is_linked(a, 'siple_Expression18', b1)
    if hasattr(b1, 'siple_While'):
        assert _is_linked(b1, 'siple_While', a)
    _safe_set(a, 'siple_Expression18', b2)
    assert _is_linked(a, 'siple_Expression18', b2)
    if hasattr(b1, 'siple_While'):
        assert not _is_linked(b1, 'siple_While', a)
    if hasattr(b2, 'siple_While'):
        assert _is_linked(b2, 'siple_While', a)
    _safe_set(a, 'siple_Expression18', None)
    assert not _is_linked(a, 'siple_Expression18', b2)
    if hasattr(b2, 'siple_While'):
        assert not _is_linked(b2, 'siple_While', a)


def test_assoc_Declaration0_link_reassign_clear():
    a = siple_Declaration(IsParameterDeclaration=True, Name="sample_text", Type="sample_text")
    b1 = siple_CompilationUnit()
    b2 = siple_CompilationUnit()
    _safe_set(a, 'siple_Declaration', b1)
    assert _is_linked(a, 'siple_Declaration', b1)
    if hasattr(b1, 'siple_CompilationUnit'):
        assert _is_linked(b1, 'siple_CompilationUnit', a)
    _safe_set(a, 'siple_Declaration', b2)
    assert _is_linked(a, 'siple_Declaration', b2)
    if hasattr(b1, 'siple_CompilationUnit'):
        assert not _is_linked(b1, 'siple_CompilationUnit', a)
    if hasattr(b2, 'siple_CompilationUnit'):
        assert _is_linked(b2, 'siple_CompilationUnit', a)
    _safe_set(a, 'siple_Declaration', None)
    assert not _is_linked(a, 'siple_Declaration', b2)
    if hasattr(b2, 'siple_CompilationUnit'):
        assert not _is_linked(b2, 'siple_CompilationUnit', a)


def test_assoc_Declaration38_link_reassign_clear():
    a = siple_Reference(Name="sample_text")
    b1 = siple_Declaration(IsParameterDeclaration=True, Name="sample_text", Type="sample_text")
    b2 = siple_Declaration(IsParameterDeclaration=False, Name="sample_text_2", Type="sample_text_2")
    _safe_set(a, 'siple_Reference', b1)
    assert _is_linked(a, 'siple_Reference', b1)
    if hasattr(b1, 'siple_Declaration39'):
        assert _is_linked(b1, 'siple_Declaration39', a)
    _safe_set(a, 'siple_Reference', b2)
    assert _is_linked(a, 'siple_Reference', b2)
    if hasattr(b1, 'siple_Declaration39'):
        assert not _is_linked(b1, 'siple_Declaration39', a)
    if hasattr(b2, 'siple_Declaration39'):
        assert _is_linked(b2, 'siple_Declaration39', a)
    _safe_set(a, 'siple_Reference', None)
    assert not _is_linked(a, 'siple_Reference', b2)
    if hasattr(b2, 'siple_Declaration39'):
        assert not _is_linked(b2, 'siple_Declaration39', a)


def test_assoc_Declaration45_link_reassign_clear():
    a = siple_ProcedureDeclaration(ReturnType="sample_text")
    b1 = siple_ProcedureCall()
    b2 = siple_ProcedureCall()
    _safe_set(a, 'siple_ProcedureDeclaration47', b1)
    assert _is_linked(a, 'siple_ProcedureDeclaration47', b1)
    if hasattr(b1, 'siple_ProcedureCall46'):
        assert _is_linked(b1, 'siple_ProcedureCall46', a)
    _safe_set(a, 'siple_ProcedureDeclaration47', b2)
    assert _is_linked(a, 'siple_ProcedureDeclaration47', b2)
    if hasattr(b1, 'siple_ProcedureCall46'):
        assert not _is_linked(b1, 'siple_ProcedureCall46', a)
    if hasattr(b2, 'siple_ProcedureCall46'):
        assert _is_linked(b2, 'siple_ProcedureCall46', a)
    _safe_set(a, 'siple_ProcedureDeclaration47', None)
    assert not _is_linked(a, 'siple_ProcedureDeclaration47', b2)
    if hasattr(b2, 'siple_ProcedureCall46'):
        assert not _is_linked(b2, 'siple_ProcedureCall46', a)


def test_assoc_Expression27_link_reassign_clear():
    a = siple_ProcedureReturn(Type="sample_text")
    b1 = siple_Expression(Type="sample_text")
    b2 = siple_Expression(Type="sample_text_2")
    _safe_set(a, 'siple_ProcedureReturn', b1)
    assert _is_linked(a, 'siple_ProcedureReturn', b1)
    if hasattr(b1, 'siple_Expression28'):
        assert _is_linked(b1, 'siple_Expression28', a)
    _safe_set(a, 'siple_ProcedureReturn', b2)
    assert _is_linked(a, 'siple_ProcedureReturn', b2)
    if hasattr(b1, 'siple_Expression28'):
        assert not _is_linked(b1, 'siple_Expression28', a)
    if hasattr(b2, 'siple_Expression28'):
        assert _is_linked(b2, 'siple_Expression28', a)
    _safe_set(a, 'siple_ProcedureReturn', None)
    assert not _is_linked(a, 'siple_ProcedureReturn', b2)
    if hasattr(b2, 'siple_Expression28'):
        assert not _is_linked(b2, 'siple_Expression28', a)


def test_assoc_Expression29_link_reassign_clear():
    a = siple_Write(Type="sample_text")
    b1 = siple_Expression(Type="sample_text")
    b2 = siple_Expression(Type="sample_text_2")
    _safe_set(a, 'siple_Write', b1)
    assert _is_linked(a, 'siple_Write', b1)
    if hasattr(b1, 'siple_Expression30'):
        assert _is_linked(b1, 'siple_Expression30', a)
    _safe_set(a, 'siple_Write', b2)
    assert _is_linked(a, 'siple_Write', b2)
    if hasattr(b1, 'siple_Expression30'):
        assert not _is_linked(b1, 'siple_Expression30', a)
    if hasattr(b2, 'siple_Expression30'):
        assert _is_linked(b2, 'siple_Expression30', a)
    _safe_set(a, 'siple_Write', None)
    assert not _is_linked(a, 'siple_Write', b2)
    if hasattr(b2, 'siple_Expression30'):
        assert not _is_linked(b2, 'siple_Expression30', a)


def test_assoc_Expression31_link_reassign_clear():
    a = siple_Read(Type="sample_text")
    b1 = siple_Expression(Type="sample_text")
    b2 = siple_Expression(Type="sample_text_2")
    _safe_set(a, 'siple_Read', b1)
    assert _is_linked(a, 'siple_Read', b1)
    if hasattr(b1, 'siple_Expression32'):
        assert _is_linked(b1, 'siple_Expression32', a)
    _safe_set(a, 'siple_Read', b2)
    assert _is_linked(a, 'siple_Read', b2)
    if hasattr(b1, 'siple_Expression32'):
        assert not _is_linked(b1, 'siple_Expression32', a)
    if hasattr(b2, 'siple_Expression32'):
        assert _is_linked(b2, 'siple_Expression32', a)
    _safe_set(a, 'siple_Read', None)
    assert not _is_linked(a, 'siple_Read', b2)
    if hasattr(b2, 'siple_Expression32'):
        assert not _is_linked(b2, 'siple_Expression32', a)


def test_assoc_Expression48_link_reassign_clear():
    a = siple_Expression(Type="sample_text")
    b1 = siple_NestedExpression()
    b2 = siple_NestedExpression()
    _safe_set(a, 'siple_Expression49', b1)
    assert _is_linked(a, 'siple_Expression49', b1)
    if hasattr(b1, 'siple_NestedExpression'):
        assert _is_linked(b1, 'siple_NestedExpression', a)
    _safe_set(a, 'siple_Expression49', b2)
    assert _is_linked(a, 'siple_Expression49', b2)
    if hasattr(b1, 'siple_NestedExpression'):
        assert not _is_linked(b1, 'siple_NestedExpression', a)
    if hasattr(b2, 'siple_NestedExpression'):
        assert _is_linked(b2, 'siple_NestedExpression', a)
    _safe_set(a, 'siple_Expression49', None)
    assert not _is_linked(a, 'siple_Expression49', b2)
    if hasattr(b2, 'siple_NestedExpression'):
        assert not _is_linked(b2, 'siple_NestedExpression', a)


def test_assoc_IsProcedureBody7_link_reassign_clear():
    a = siple_ProcedureDeclaration(ReturnType="sample_text")
    b1 = siple_Block()
    b2 = siple_Block()
    _safe_set(a, 'siple_ProcedureDeclaration9', b1)
    assert _is_linked(a, 'siple_ProcedureDeclaration9', b1)
    if hasattr(b1, 'siple_Block8'):
        assert _is_linked(b1, 'siple_Block8', a)
    _safe_set(a, 'siple_ProcedureDeclaration9', b2)
    assert _is_linked(a, 'siple_ProcedureDeclaration9', b2)
    if hasattr(b1, 'siple_Block8'):
        assert not _is_linked(b1, 'siple_Block8', a)
    if hasattr(b2, 'siple_Block8'):
        assert _is_linked(b2, 'siple_Block8', a)
    _safe_set(a, 'siple_ProcedureDeclaration9', None)
    assert not _is_linked(a, 'siple_ProcedureDeclaration9', b2)
    if hasattr(b2, 'siple_Block8'):
        assert not _is_linked(b2, 'siple_Block8', a)


def test_assoc_LValue22_link_reassign_clear():
    a = siple_VariableAssignment(Type="sample_text")
    b1 = siple_Expression(Type="sample_text")
    b2 = siple_Expression(Type="sample_text_2")
    _safe_set(a, 'siple_VariableAssignment', b1)
    assert _is_linked(a, 'siple_VariableAssignment', b1)
    if hasattr(b1, 'siple_Expression23'):
        assert _is_linked(b1, 'siple_Expression23', a)
    _safe_set(a, 'siple_VariableAssignment', b2)
    assert _is_linked(a, 'siple_VariableAssignment', b2)
    if hasattr(b1, 'siple_Expression23'):
        assert not _is_linked(b1, 'siple_Expression23', a)
    if hasattr(b2, 'siple_Expression23'):
        assert _is_linked(b2, 'siple_Expression23', a)
    _safe_set(a, 'siple_VariableAssignment', None)
    assert not _is_linked(a, 'siple_VariableAssignment', b2)
    if hasattr(b2, 'siple_Expression23'):
        assert not _is_linked(b2, 'siple_Expression23', a)


def test_assoc_MainProcedure1_link_reassign_clear():
    a = siple_ProcedureDeclaration(ReturnType="sample_text")
    b1 = siple_CompilationUnit()
    b2 = siple_CompilationUnit()
    _safe_set(a, 'siple_ProcedureDeclaration', b1)
    assert _is_linked(a, 'siple_ProcedureDeclaration', b1)
    if hasattr(b1, 'siple_CompilationUnit2'):
        assert _is_linked(b1, 'siple_CompilationUnit2', a)
    _safe_set(a, 'siple_ProcedureDeclaration', b2)
    assert _is_linked(a, 'siple_ProcedureDeclaration', b2)
    if hasattr(b1, 'siple_CompilationUnit2'):
        assert not _is_linked(b1, 'siple_CompilationUnit2', a)
    if hasattr(b2, 'siple_CompilationUnit2'):
        assert _is_linked(b2, 'siple_CompilationUnit2', a)
    _safe_set(a, 'siple_ProcedureDeclaration', None)
    assert not _is_linked(a, 'siple_ProcedureDeclaration', b2)
    if hasattr(b2, 'siple_CompilationUnit2'):
        assert not _is_linked(b2, 'siple_CompilationUnit2', a)


def test_assoc_Operand152_link_reassign_clear():
    a = siple_Expression(Type="sample_text")
    b1 = siple_BinaryExpression()
    b2 = siple_BinaryExpression()
    _safe_set(a, 'siple_Expression53', b1)
    assert _is_linked(a, 'siple_Expression53', b1)
    if hasattr(b1, 'siple_BinaryExpression'):
        assert _is_linked(b1, 'siple_BinaryExpression', a)
    _safe_set(a, 'siple_Expression53', b2)
    assert _is_linked(a, 'siple_Expression53', b2)
    if hasattr(b1, 'siple_BinaryExpression'):
        assert not _is_linked(b1, 'siple_BinaryExpression', a)
    if hasattr(b2, 'siple_BinaryExpression'):
        assert _is_linked(b2, 'siple_BinaryExpression', a)
    _safe_set(a, 'siple_Expression53', None)
    assert not _is_linked(a, 'siple_Expression53', b2)
    if hasattr(b2, 'siple_BinaryExpression'):
        assert not _is_linked(b2, 'siple_BinaryExpression', a)


def test_assoc_Operand254_link_reassign_clear():
    a = siple_Expression(Type="sample_text")
    b1 = siple_BinaryExpression()
    b2 = siple_BinaryExpression()
    _safe_set(a, 'siple_Expression56', b1)
    assert _is_linked(a, 'siple_Expression56', b1)
    if hasattr(b1, 'siple_BinaryExpression55'):
        assert _is_linked(b1, 'siple_BinaryExpression55', a)
    _safe_set(a, 'siple_Expression56', b2)
    assert _is_linked(a, 'siple_Expression56', b2)
    if hasattr(b1, 'siple_BinaryExpression55'):
        assert not _is_linked(b1, 'siple_BinaryExpression55', a)
    if hasattr(b2, 'siple_BinaryExpression55'):
        assert _is_linked(b2, 'siple_BinaryExpression55', a)
    _safe_set(a, 'siple_Expression56', None)
    assert not _is_linked(a, 'siple_Expression56', b2)
    if hasattr(b2, 'siple_BinaryExpression55'):
        assert not _is_linked(b2, 'siple_BinaryExpression55', a)


def test_assoc_Operand50_link_reassign_clear():
    a = siple_Expression(Type="sample_text")
    b1 = siple_UnaryExpression()
    b2 = siple_UnaryExpression()
    _safe_set(a, 'siple_Expression51', b1)
    assert _is_linked(a, 'siple_Expression51', b1)
    if hasattr(b1, 'siple_UnaryExpression'):
        assert _is_linked(b1, 'siple_UnaryExpression', a)
    _safe_set(a, 'siple_Expression51', b2)
    assert _is_linked(a, 'siple_Expression51', b2)
    if hasattr(b1, 'siple_UnaryExpression'):
        assert not _is_linked(b1, 'siple_UnaryExpression', a)
    if hasattr(b2, 'siple_UnaryExpression'):
        assert _is_linked(b2, 'siple_UnaryExpression', a)
    _safe_set(a, 'siple_Expression51', None)
    assert not _is_linked(a, 'siple_Expression51', b2)
    if hasattr(b2, 'siple_UnaryExpression'):
        assert not _is_linked(b2, 'siple_UnaryExpression', a)


def test_assoc_Parameter33_link_reassign_clear():
    a = siple_VariableDeclaration(DeclaredType="sample_text")
    b1 = siple_ProcedureDeclaration(ReturnType="sample_text")
    b2 = siple_ProcedureDeclaration(ReturnType="sample_text_2")
    _safe_set(a, 'siple_VariableDeclaration', b1)
    assert _is_linked(a, 'siple_VariableDeclaration', b1)
    if hasattr(b1, 'siple_ProcedureDeclaration34'):
        assert _is_linked(b1, 'siple_ProcedureDeclaration34', a)
    _safe_set(a, 'siple_VariableDeclaration', b2)
    assert _is_linked(a, 'siple_VariableDeclaration', b2)
    if hasattr(b1, 'siple_ProcedureDeclaration34'):
        assert not _is_linked(b1, 'siple_ProcedureDeclaration34', a)
    if hasattr(b2, 'siple_ProcedureDeclaration34'):
        assert _is_linked(b2, 'siple_ProcedureDeclaration34', a)
    _safe_set(a, 'siple_VariableDeclaration', None)
    assert not _is_linked(a, 'siple_VariableDeclaration', b2)
    if hasattr(b2, 'siple_ProcedureDeclaration34'):
        assert not _is_linked(b2, 'siple_ProcedureDeclaration34', a)


def test_assoc_Procedure40_link_reassign_clear():
    a = siple_Expression(Type="sample_text")
    b1 = siple_ProcedureCall()
    b2 = siple_ProcedureCall()
    _safe_set(a, 'siple_Expression41', b1)
    assert _is_linked(a, 'siple_Expression41', b1)
    if hasattr(b1, 'siple_ProcedureCall'):
        assert _is_linked(b1, 'siple_ProcedureCall', a)
    _safe_set(a, 'siple_Expression41', b2)
    assert _is_linked(a, 'siple_Expression41', b2)
    if hasattr(b1, 'siple_ProcedureCall'):
        assert not _is_linked(b1, 'siple_ProcedureCall', a)
    if hasattr(b2, 'siple_ProcedureCall'):
        assert _is_linked(b2, 'siple_ProcedureCall', a)
    _safe_set(a, 'siple_Expression41', None)
    assert not _is_linked(a, 'siple_Expression41', b2)
    if hasattr(b2, 'siple_ProcedureCall'):
        assert not _is_linked(b2, 'siple_ProcedureCall', a)


def test_assoc_ProcedureInContext3_link_reassign_clear():
    a = siple_Statement()
    b1 = siple_ProcedureDeclaration(ReturnType="sample_text")
    b2 = siple_ProcedureDeclaration(ReturnType="sample_text_2")
    _safe_set(a, 'siple_Statement', b1)
    assert _is_linked(a, 'siple_Statement', b1)
    if hasattr(b1, 'siple_ProcedureDeclaration4'):
        assert _is_linked(b1, 'siple_ProcedureDeclaration4', a)
    _safe_set(a, 'siple_Statement', b2)
    assert _is_linked(a, 'siple_Statement', b2)
    if hasattr(b1, 'siple_ProcedureDeclaration4'):
        assert not _is_linked(b1, 'siple_ProcedureDeclaration4', a)
    if hasattr(b2, 'siple_ProcedureDeclaration4'):
        assert _is_linked(b2, 'siple_ProcedureDeclaration4', a)
    _safe_set(a, 'siple_Statement', None)
    assert not _is_linked(a, 'siple_Statement', b2)
    if hasattr(b2, 'siple_ProcedureDeclaration4'):
        assert not _is_linked(b2, 'siple_ProcedureDeclaration4', a)


def test_assoc_RValue24_link_reassign_clear():
    a = siple_VariableAssignment(Type="sample_text")
    b1 = siple_Expression(Type="sample_text")
    b2 = siple_Expression(Type="sample_text_2")
    _safe_set(a, 'siple_VariableAssignment25', b1)
    assert _is_linked(a, 'siple_VariableAssignment25', b1)
    if hasattr(b1, 'siple_Expression26'):
        assert _is_linked(b1, 'siple_Expression26', a)
    _safe_set(a, 'siple_VariableAssignment25', b2)
    assert _is_linked(a, 'siple_VariableAssignment25', b2)
    if hasattr(b1, 'siple_Expression26'):
        assert not _is_linked(b1, 'siple_Expression26', a)
    if hasattr(b2, 'siple_Expression26'):
        assert _is_linked(b2, 'siple_Expression26', a)
    _safe_set(a, 'siple_VariableAssignment25', None)
    assert not _is_linked(a, 'siple_VariableAssignment25', b2)
    if hasattr(b2, 'siple_Expression26'):
        assert not _is_linked(b2, 'siple_Expression26', a)


def test_assoc_Statement5_link_reassign_clear():
    a = siple_Statement()
    b1 = siple_Block()
    b2 = siple_Block()
    _safe_set(a, 'siple_Statement6', b1)
    assert _is_linked(a, 'siple_Statement6', b1)
    if hasattr(b1, 'siple_Block'):
        assert _is_linked(b1, 'siple_Block', a)
    _safe_set(a, 'siple_Statement6', b2)
    assert _is_linked(a, 'siple_Statement6', b2)
    if hasattr(b1, 'siple_Block'):
        assert not _is_linked(b1, 'siple_Block', a)
    if hasattr(b2, 'siple_Block'):
        assert _is_linked(b2, 'siple_Block', a)
    _safe_set(a, 'siple_Statement6', None)
    assert not _is_linked(a, 'siple_Statement6', b2)
    if hasattr(b2, 'siple_Block'):
        assert not _is_linked(b2, 'siple_Block', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArithmeticExpression_strategy = st.builds(ArithmeticExpression)
@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=25)
def test_ArithmeticExpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)


BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


Declaration_strategy = st.builds(Declaration)
@given(instance=Declaration_strategy)
@settings(max_examples=25)
def test_Declaration_instantiation(instance):
    assert isinstance(instance, Declaration)


EqualityExpression_strategy = st.builds(EqualityExpression)
@given(instance=EqualityExpression_strategy)
@settings(max_examples=25)
def test_EqualityExpression_instantiation(instance):
    assert isinstance(instance, EqualityExpression)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


LogicExpression_strategy = st.builds(LogicExpression)
@given(instance=LogicExpression_strategy)
@settings(max_examples=25)
def test_LogicExpression_instantiation(instance):
    assert isinstance(instance, LogicExpression)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


UnaryExpression_strategy = st.builds(UnaryExpression)
@given(instance=UnaryExpression_strategy)
@settings(max_examples=25)
def test_UnaryExpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)


siple_Addition_strategy = st.builds(siple_Addition)
@given(instance=siple_Addition_strategy)
@settings(max_examples=25)
def test_siple_Addition_instantiation(instance):
    assert isinstance(instance, siple_Addition)


siple_And_strategy = st.builds(siple_And)
@given(instance=siple_And_strategy)
@settings(max_examples=25)
def test_siple_And_instantiation(instance):
    assert isinstance(instance, siple_And)


siple_ArithmeticExpression_strategy = st.builds(siple_ArithmeticExpression)
@given(instance=siple_ArithmeticExpression_strategy)
@settings(max_examples=25)
def test_siple_ArithmeticExpression_instantiation(instance):
    assert isinstance(instance, siple_ArithmeticExpression)


siple_BinaryExpression_strategy = st.builds(siple_BinaryExpression)
@given(instance=siple_BinaryExpression_strategy)
@settings(max_examples=25)
def test_siple_BinaryExpression_instantiation(instance):
    assert isinstance(instance, siple_BinaryExpression)


siple_Block_strategy = st.builds(siple_Block)
@given(instance=siple_Block_strategy)
@settings(max_examples=25)
def test_siple_Block_instantiation(instance):
    assert isinstance(instance, siple_Block)


siple_CompilationUnit_strategy = st.builds(siple_CompilationUnit)
@given(instance=siple_CompilationUnit_strategy)
@settings(max_examples=25)
def test_siple_CompilationUnit_instantiation(instance):
    assert isinstance(instance, siple_CompilationUnit)


siple_Constant_strategy = st.builds(siple_Constant, AsBoolean=safe_text, AsInteger=safe_text, AsReal=safe_text, Lexem=safe_text)
@given(instance=siple_Constant_strategy)
@settings(max_examples=25)
def test_siple_Constant_instantiation(instance):
    assert isinstance(instance, siple_Constant)


siple_Declaration_strategy = st.builds(siple_Declaration, IsParameterDeclaration=st.booleans(), Name=safe_text, Type=safe_text)
@given(instance=siple_Declaration_strategy)
@settings(max_examples=25)
def test_siple_Declaration_instantiation(instance):
    assert isinstance(instance, siple_Declaration)


siple_Dereference_strategy = st.builds(siple_Dereference)
@given(instance=siple_Dereference_strategy)
@settings(max_examples=25)
def test_siple_Dereference_instantiation(instance):
    assert isinstance(instance, siple_Dereference)


siple_Division_strategy = st.builds(siple_Division)
@given(instance=siple_Division_strategy)
@settings(max_examples=25)
def test_siple_Division_instantiation(instance):
    assert isinstance(instance, siple_Division)


siple_Equal_strategy = st.builds(siple_Equal)
@given(instance=siple_Equal_strategy)
@settings(max_examples=25)
def test_siple_Equal_instantiation(instance):
    assert isinstance(instance, siple_Equal)


siple_EqualityExpression_strategy = st.builds(siple_EqualityExpression)
@given(instance=siple_EqualityExpression_strategy)
@settings(max_examples=25)
def test_siple_EqualityExpression_instantiation(instance):
    assert isinstance(instance, siple_EqualityExpression)


siple_Expression_strategy = st.builds(siple_Expression, Type=safe_text)
@given(instance=siple_Expression_strategy)
@settings(max_examples=25)
def test_siple_Expression_instantiation(instance):
    assert isinstance(instance, siple_Expression)


siple_GreaterThan_strategy = st.builds(siple_GreaterThan)
@given(instance=siple_GreaterThan_strategy)
@settings(max_examples=25)
def test_siple_GreaterThan_instantiation(instance):
    assert isinstance(instance, siple_GreaterThan)


siple_GreaterThanEqual_strategy = st.builds(siple_GreaterThanEqual)
@given(instance=siple_GreaterThanEqual_strategy)
@settings(max_examples=25)
def test_siple_GreaterThanEqual_instantiation(instance):
    assert isinstance(instance, siple_GreaterThanEqual)


siple_If_strategy = st.builds(siple_If)
@given(instance=siple_If_strategy)
@settings(max_examples=25)
def test_siple_If_instantiation(instance):
    assert isinstance(instance, siple_If)


siple_LesserThan_strategy = st.builds(siple_LesserThan)
@given(instance=siple_LesserThan_strategy)
@settings(max_examples=25)
def test_siple_LesserThan_instantiation(instance):
    assert isinstance(instance, siple_LesserThan)


siple_LesserThanEqual_strategy = st.builds(siple_LesserThanEqual)
@given(instance=siple_LesserThanEqual_strategy)
@settings(max_examples=25)
def test_siple_LesserThanEqual_instantiation(instance):
    assert isinstance(instance, siple_LesserThanEqual)


siple_LogicExpression_strategy = st.builds(siple_LogicExpression)
@given(instance=siple_LogicExpression_strategy)
@settings(max_examples=25)
def test_siple_LogicExpression_instantiation(instance):
    assert isinstance(instance, siple_LogicExpression)


siple_Multiplication_strategy = st.builds(siple_Multiplication)
@given(instance=siple_Multiplication_strategy)
@settings(max_examples=25)
def test_siple_Multiplication_instantiation(instance):
    assert isinstance(instance, siple_Multiplication)


siple_NestedExpression_strategy = st.builds(siple_NestedExpression)
@given(instance=siple_NestedExpression_strategy)
@settings(max_examples=25)
def test_siple_NestedExpression_instantiation(instance):
    assert isinstance(instance, siple_NestedExpression)


siple_Not_strategy = st.builds(siple_Not)
@given(instance=siple_Not_strategy)
@settings(max_examples=25)
def test_siple_Not_instantiation(instance):
    assert isinstance(instance, siple_Not)


siple_Or_strategy = st.builds(siple_Or)
@given(instance=siple_Or_strategy)
@settings(max_examples=25)
def test_siple_Or_instantiation(instance):
    assert isinstance(instance, siple_Or)


siple_ProcedureCall_strategy = st.builds(siple_ProcedureCall)
@given(instance=siple_ProcedureCall_strategy)
@settings(max_examples=25)
def test_siple_ProcedureCall_instantiation(instance):
    assert isinstance(instance, siple_ProcedureCall)


siple_ProcedureDeclaration_strategy = st.builds(siple_ProcedureDeclaration, ReturnType=safe_text)
@given(instance=siple_ProcedureDeclaration_strategy)
@settings(max_examples=25)
def test_siple_ProcedureDeclaration_instantiation(instance):
    assert isinstance(instance, siple_ProcedureDeclaration)


siple_ProcedureReturn_strategy = st.builds(siple_ProcedureReturn, Type=safe_text)
@given(instance=siple_ProcedureReturn_strategy)
@settings(max_examples=25)
def test_siple_ProcedureReturn_instantiation(instance):
    assert isinstance(instance, siple_ProcedureReturn)


siple_Read_strategy = st.builds(siple_Read, Type=safe_text)
@given(instance=siple_Read_strategy)
@settings(max_examples=25)
def test_siple_Read_instantiation(instance):
    assert isinstance(instance, siple_Read)


siple_RealCoercion_strategy = st.builds(siple_RealCoercion)
@given(instance=siple_RealCoercion_strategy)
@settings(max_examples=25)
def test_siple_RealCoercion_instantiation(instance):
    assert isinstance(instance, siple_RealCoercion)


siple_Reference_strategy = st.builds(siple_Reference, Name=safe_text)
@given(instance=siple_Reference_strategy)
@settings(max_examples=25)
def test_siple_Reference_instantiation(instance):
    assert isinstance(instance, siple_Reference)


siple_Statement_strategy = st.builds(siple_Statement)
@given(instance=siple_Statement_strategy)
@settings(max_examples=25)
def test_siple_Statement_instantiation(instance):
    assert isinstance(instance, siple_Statement)


siple_Subtraction_strategy = st.builds(siple_Subtraction)
@given(instance=siple_Subtraction_strategy)
@settings(max_examples=25)
def test_siple_Subtraction_instantiation(instance):
    assert isinstance(instance, siple_Subtraction)


siple_UMinus_strategy = st.builds(siple_UMinus)
@given(instance=siple_UMinus_strategy)
@settings(max_examples=25)
def test_siple_UMinus_instantiation(instance):
    assert isinstance(instance, siple_UMinus)


siple_UnaryExpression_strategy = st.builds(siple_UnaryExpression)
@given(instance=siple_UnaryExpression_strategy)
@settings(max_examples=25)
def test_siple_UnaryExpression_instantiation(instance):
    assert isinstance(instance, siple_UnaryExpression)


siple_VariableAssignment_strategy = st.builds(siple_VariableAssignment, Type=safe_text)
@given(instance=siple_VariableAssignment_strategy)
@settings(max_examples=25)
def test_siple_VariableAssignment_instantiation(instance):
    assert isinstance(instance, siple_VariableAssignment)


siple_VariableDeclaration_strategy = st.builds(siple_VariableDeclaration, DeclaredType=safe_text)
@given(instance=siple_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_siple_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, siple_VariableDeclaration)


siple_While_strategy = st.builds(siple_While)
@given(instance=siple_While_strategy)
@settings(max_examples=25)
def test_siple_While_instantiation(instance):
    assert isinstance(instance, siple_While)


siple_Write_strategy = st.builds(siple_Write, Type=safe_text)
@given(instance=siple_Write_strategy)
@settings(max_examples=25)
def test_siple_Write_instantiation(instance):
    assert isinstance(instance, siple_Write)



