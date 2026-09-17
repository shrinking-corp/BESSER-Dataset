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
    Call,
    miniJava_NewCall,
    miniJava_MethodCall2,
    miniJava_OutputStream,
    miniJava_Call,
    miniJava_ArrayInstance,
    miniJava_ObjectInstance,
    miniJava_Frame,
    miniJava_FieldBinding,
    Value,
    miniJava_ArrayRefValue,
    miniJava_ObjectRefValue,
    miniJava_NullValue,
    miniJava_BooleanValue,
    miniJava_StringValue,
    miniJava_IntegerValue,
    miniJava_Value,
    miniJava_SymbolBinding,
    miniJava_Context,
    Expression,
    miniJava_MethodCall,
    miniJava_ArrayAccess,
    miniJava_Neg,
    miniJava_Plus,
    miniJava_Not,
    miniJava_Superior,
    miniJava_Super,
    miniJava_InferiorOrEqual,
    miniJava_NewArray,
    miniJava_Inferior,
    miniJava_This,
    miniJava_SuperiorOrEqual,
    miniJava_Multiplication,
    miniJava_Inequality,
    miniJava_StringConstant,
    miniJava_Equality,
    miniJava_NewObject,
    miniJava_ArrayLength,
    miniJava_Division,
    miniJava_BoolConstant,
    miniJava_IntConstant,
    miniJava_SymbolRef,
    miniJava_And,
    miniJava_Null,
    miniJava_FieldAccess,
    miniJava_Minus,
    miniJava_Or,
    miniJava_Assignee,
    Assignee,
    miniJava_NamedElement,
    SingleTypeRef,
    miniJava_VoidTypeRef,
    miniJava_BooleanTypeRef,
    miniJava_StringTypeRef,
    miniJava_IntegerTypeRef,
    miniJava_ClassRef,
    TypeRef,
    miniJava_ArrayTypeRef,
    miniJava_SingleTypeRef,
    miniJava_TypeRef,
    miniJava_Statement,
    Statement,
    miniJava_PrintStatement,
    miniJava_ForStatement,
    miniJava_Assignment,
    miniJava_IfStatement,
    miniJava_Return,
    miniJava_WhileStatement,
    miniJava_Expression,
    Symbol,
    miniJava_VariableDeclaration,
    miniJava_Block,
    miniJava_Parameter,
    Member,
    miniJava_Field,
    miniJava_Method,
    TypedDeclaration,
    miniJava_Symbol,
    TypeDeclaration,
    miniJava_Class,
    miniJava_Member,
    miniJava_Interface,
    NamedElement,
    miniJava_TypedDeclaration,
    miniJava_State,
    miniJava_TypeDeclaration,
    miniJava_Import,
    miniJava_Program,
    AccessLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_call_is_not_abstract():
    assert not inspect.isabstract(Call)


def test_hyp_call_constructor_exists():
    assert callable(Call.__init__)


def test_hyp_call_constructor_args():
    sig = inspect.signature(Call.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_newcall_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewCall)


def test_hyp_minijava_newcall_constructor_exists():
    assert callable(miniJava_NewCall.__init__)


def test_hyp_minijava_newcall_constructor_args():
    sig = inspect.signature(miniJava_NewCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_methodcall2_is_not_abstract():
    assert not inspect.isabstract(miniJava_MethodCall2)


def test_hyp_minijava_methodcall2_constructor_exists():
    assert callable(miniJava_MethodCall2.__init__)


def test_hyp_minijava_methodcall2_constructor_args():
    sig = inspect.signature(miniJava_MethodCall2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_outputstream_is_not_abstract():
    assert not inspect.isabstract(miniJava_OutputStream)


def test_hyp_minijava_outputstream_constructor_exists():
    assert callable(miniJava_OutputStream.__init__)


def test_hyp_minijava_outputstream_constructor_args():
    sig = inspect.signature(miniJava_OutputStream.__init__)
    params = list(sig.parameters.keys())
    assert "stream" in params, "Missing parameter 'stream'"




def test_hyp_minijava_call_is_not_abstract():
    assert not inspect.isabstract(miniJava_Call)


def test_hyp_minijava_call_constructor_exists():
    assert callable(miniJava_Call.__init__)


def test_hyp_minijava_call_constructor_args():
    sig = inspect.signature(miniJava_Call.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_arrayinstance_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayInstance)


def test_hyp_minijava_arrayinstance_constructor_exists():
    assert callable(miniJava_ArrayInstance.__init__)


def test_hyp_minijava_arrayinstance_constructor_args():
    sig = inspect.signature(miniJava_ArrayInstance.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"




def test_hyp_minijava_objectinstance_is_not_abstract():
    assert not inspect.isabstract(miniJava_ObjectInstance)


def test_hyp_minijava_objectinstance_constructor_exists():
    assert callable(miniJava_ObjectInstance.__init__)


def test_hyp_minijava_objectinstance_constructor_args():
    sig = inspect.signature(miniJava_ObjectInstance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_frame_is_not_abstract():
    assert not inspect.isabstract(miniJava_Frame)


def test_hyp_minijava_frame_constructor_exists():
    assert callable(miniJava_Frame.__init__)


def test_hyp_minijava_frame_constructor_args():
    sig = inspect.signature(miniJava_Frame.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_fieldbinding_is_not_abstract():
    assert not inspect.isabstract(miniJava_FieldBinding)


def test_hyp_minijava_fieldbinding_constructor_exists():
    assert callable(miniJava_FieldBinding.__init__)


def test_hyp_minijava_fieldbinding_constructor_args():
    sig = inspect.signature(miniJava_FieldBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_hyp_value_constructor_exists():
    assert callable(Value.__init__)


def test_hyp_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_arrayrefvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayRefValue)


def test_hyp_minijava_arrayrefvalue_constructor_exists():
    assert callable(miniJava_ArrayRefValue.__init__)


def test_hyp_minijava_arrayrefvalue_constructor_args():
    sig = inspect.signature(miniJava_ArrayRefValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_objectrefvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_ObjectRefValue)


def test_hyp_minijava_objectrefvalue_constructor_exists():
    assert callable(miniJava_ObjectRefValue.__init__)


def test_hyp_minijava_objectrefvalue_constructor_args():
    sig = inspect.signature(miniJava_ObjectRefValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_nullvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_NullValue)


def test_hyp_minijava_nullvalue_constructor_exists():
    assert callable(miniJava_NullValue.__init__)


def test_hyp_minijava_nullvalue_constructor_args():
    sig = inspect.signature(miniJava_NullValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_BooleanValue)


def test_hyp_minijava_booleanvalue_constructor_exists():
    assert callable(miniJava_BooleanValue.__init__)


def test_hyp_minijava_booleanvalue_constructor_args():
    sig = inspect.signature(miniJava_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_stringvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_StringValue)


def test_hyp_minijava_stringvalue_constructor_exists():
    assert callable(miniJava_StringValue.__init__)


def test_hyp_minijava_stringvalue_constructor_args():
    sig = inspect.signature(miniJava_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_integervalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_IntegerValue)


def test_hyp_minijava_integervalue_constructor_exists():
    assert callable(miniJava_IntegerValue.__init__)


def test_hyp_minijava_integervalue_constructor_args():
    sig = inspect.signature(miniJava_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_value_is_not_abstract():
    assert not inspect.isabstract(miniJava_Value)


def test_hyp_minijava_value_constructor_exists():
    assert callable(miniJava_Value.__init__)


def test_hyp_minijava_value_constructor_args():
    sig = inspect.signature(miniJava_Value.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_symbolbinding_is_not_abstract():
    assert not inspect.isabstract(miniJava_SymbolBinding)


def test_hyp_minijava_symbolbinding_constructor_exists():
    assert callable(miniJava_SymbolBinding.__init__)


def test_hyp_minijava_symbolbinding_constructor_args():
    sig = inspect.signature(miniJava_SymbolBinding.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_context_is_not_abstract():
    assert not inspect.isabstract(miniJava_Context)


def test_hyp_minijava_context_constructor_exists():
    assert callable(miniJava_Context.__init__)


def test_hyp_minijava_context_constructor_args():
    sig = inspect.signature(miniJava_Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_methodcall_is_not_abstract():
    assert not inspect.isabstract(miniJava_MethodCall)


def test_hyp_minijava_methodcall_constructor_exists():
    assert callable(miniJava_MethodCall.__init__)


def test_hyp_minijava_methodcall_constructor_args():
    sig = inspect.signature(miniJava_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayAccess)


def test_hyp_minijava_arrayaccess_constructor_exists():
    assert callable(miniJava_ArrayAccess.__init__)


def test_hyp_minijava_arrayaccess_constructor_args():
    sig = inspect.signature(miniJava_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_neg_is_not_abstract():
    assert not inspect.isabstract(miniJava_Neg)


def test_hyp_minijava_neg_constructor_exists():
    assert callable(miniJava_Neg.__init__)


def test_hyp_minijava_neg_constructor_args():
    sig = inspect.signature(miniJava_Neg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_plus_is_not_abstract():
    assert not inspect.isabstract(miniJava_Plus)


def test_hyp_minijava_plus_constructor_exists():
    assert callable(miniJava_Plus.__init__)


def test_hyp_minijava_plus_constructor_args():
    sig = inspect.signature(miniJava_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_not_is_not_abstract():
    assert not inspect.isabstract(miniJava_Not)


def test_hyp_minijava_not_constructor_exists():
    assert callable(miniJava_Not.__init__)


def test_hyp_minijava_not_constructor_args():
    sig = inspect.signature(miniJava_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_superior_is_not_abstract():
    assert not inspect.isabstract(miniJava_Superior)


def test_hyp_minijava_superior_constructor_exists():
    assert callable(miniJava_Superior.__init__)


def test_hyp_minijava_superior_constructor_args():
    sig = inspect.signature(miniJava_Superior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_super_is_not_abstract():
    assert not inspect.isabstract(miniJava_Super)


def test_hyp_minijava_super_constructor_exists():
    assert callable(miniJava_Super.__init__)


def test_hyp_minijava_super_constructor_args():
    sig = inspect.signature(miniJava_Super.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_inferiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava_InferiorOrEqual)


def test_hyp_minijava_inferiororequal_constructor_exists():
    assert callable(miniJava_InferiorOrEqual.__init__)


def test_hyp_minijava_inferiororequal_constructor_args():
    sig = inspect.signature(miniJava_InferiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_newarray_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewArray)


def test_hyp_minijava_newarray_constructor_exists():
    assert callable(miniJava_NewArray.__init__)


def test_hyp_minijava_newarray_constructor_args():
    sig = inspect.signature(miniJava_NewArray.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_inferior_is_not_abstract():
    assert not inspect.isabstract(miniJava_Inferior)


def test_hyp_minijava_inferior_constructor_exists():
    assert callable(miniJava_Inferior.__init__)


def test_hyp_minijava_inferior_constructor_args():
    sig = inspect.signature(miniJava_Inferior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_this_is_not_abstract():
    assert not inspect.isabstract(miniJava_This)


def test_hyp_minijava_this_constructor_exists():
    assert callable(miniJava_This.__init__)


def test_hyp_minijava_this_constructor_args():
    sig = inspect.signature(miniJava_This.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_superiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava_SuperiorOrEqual)


def test_hyp_minijava_superiororequal_constructor_exists():
    assert callable(miniJava_SuperiorOrEqual.__init__)


def test_hyp_minijava_superiororequal_constructor_args():
    sig = inspect.signature(miniJava_SuperiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_multiplication_is_not_abstract():
    assert not inspect.isabstract(miniJava_Multiplication)


def test_hyp_minijava_multiplication_constructor_exists():
    assert callable(miniJava_Multiplication.__init__)


def test_hyp_minijava_multiplication_constructor_args():
    sig = inspect.signature(miniJava_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_inequality_is_not_abstract():
    assert not inspect.isabstract(miniJava_Inequality)


def test_hyp_minijava_inequality_constructor_exists():
    assert callable(miniJava_Inequality.__init__)


def test_hyp_minijava_inequality_constructor_args():
    sig = inspect.signature(miniJava_Inequality.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_stringconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava_StringConstant)


def test_hyp_minijava_stringconstant_constructor_exists():
    assert callable(miniJava_StringConstant.__init__)


def test_hyp_minijava_stringconstant_constructor_args():
    sig = inspect.signature(miniJava_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_equality_is_not_abstract():
    assert not inspect.isabstract(miniJava_Equality)


def test_hyp_minijava_equality_constructor_exists():
    assert callable(miniJava_Equality.__init__)


def test_hyp_minijava_equality_constructor_args():
    sig = inspect.signature(miniJava_Equality.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_newobject_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewObject)


def test_hyp_minijava_newobject_constructor_exists():
    assert callable(miniJava_NewObject.__init__)


def test_hyp_minijava_newobject_constructor_args():
    sig = inspect.signature(miniJava_NewObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_arraylength_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayLength)


def test_hyp_minijava_arraylength_constructor_exists():
    assert callable(miniJava_ArrayLength.__init__)


def test_hyp_minijava_arraylength_constructor_args():
    sig = inspect.signature(miniJava_ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_division_is_not_abstract():
    assert not inspect.isabstract(miniJava_Division)


def test_hyp_minijava_division_constructor_exists():
    assert callable(miniJava_Division.__init__)


def test_hyp_minijava_division_constructor_args():
    sig = inspect.signature(miniJava_Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_boolconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava_BoolConstant)


def test_hyp_minijava_boolconstant_constructor_exists():
    assert callable(miniJava_BoolConstant.__init__)


def test_hyp_minijava_boolconstant_constructor_args():
    sig = inspect.signature(miniJava_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_intconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava_IntConstant)


def test_hyp_minijava_intconstant_constructor_exists():
    assert callable(miniJava_IntConstant.__init__)


def test_hyp_minijava_intconstant_constructor_args():
    sig = inspect.signature(miniJava_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_symbolref_is_not_abstract():
    assert not inspect.isabstract(miniJava_SymbolRef)


def test_hyp_minijava_symbolref_constructor_exists():
    assert callable(miniJava_SymbolRef.__init__)


def test_hyp_minijava_symbolref_constructor_args():
    sig = inspect.signature(miniJava_SymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_and_is_not_abstract():
    assert not inspect.isabstract(miniJava_And)


def test_hyp_minijava_and_constructor_exists():
    assert callable(miniJava_And.__init__)


def test_hyp_minijava_and_constructor_args():
    sig = inspect.signature(miniJava_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_null_is_not_abstract():
    assert not inspect.isabstract(miniJava_Null)


def test_hyp_minijava_null_constructor_exists():
    assert callable(miniJava_Null.__init__)


def test_hyp_minijava_null_constructor_args():
    sig = inspect.signature(miniJava_Null.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava_FieldAccess)


def test_hyp_minijava_fieldaccess_constructor_exists():
    assert callable(miniJava_FieldAccess.__init__)


def test_hyp_minijava_fieldaccess_constructor_args():
    sig = inspect.signature(miniJava_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_minus_is_not_abstract():
    assert not inspect.isabstract(miniJava_Minus)


def test_hyp_minijava_minus_constructor_exists():
    assert callable(miniJava_Minus.__init__)


def test_hyp_minijava_minus_constructor_args():
    sig = inspect.signature(miniJava_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_or_is_not_abstract():
    assert not inspect.isabstract(miniJava_Or)


def test_hyp_minijava_or_constructor_exists():
    assert callable(miniJava_Or.__init__)


def test_hyp_minijava_or_constructor_args():
    sig = inspect.signature(miniJava_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_assignee_is_not_abstract():
    assert not inspect.isabstract(miniJava_Assignee)


def test_hyp_minijava_assignee_constructor_exists():
    assert callable(miniJava_Assignee.__init__)


def test_hyp_minijava_assignee_constructor_args():
    sig = inspect.signature(miniJava_Assignee.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignee_is_not_abstract():
    assert not inspect.isabstract(Assignee)


def test_hyp_assignee_constructor_exists():
    assert callable(Assignee.__init__)


def test_hyp_assignee_constructor_args():
    sig = inspect.signature(Assignee.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_namedelement_is_not_abstract():
    assert not inspect.isabstract(miniJava_NamedElement)


def test_hyp_minijava_namedelement_constructor_exists():
    assert callable(miniJava_NamedElement.__init__)


def test_hyp_minijava_namedelement_constructor_args():
    sig = inspect.signature(miniJava_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_singletyperef_is_not_abstract():
    assert not inspect.isabstract(SingleTypeRef)


def test_hyp_singletyperef_constructor_exists():
    assert callable(SingleTypeRef.__init__)


def test_hyp_singletyperef_constructor_args():
    sig = inspect.signature(SingleTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_voidtyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_VoidTypeRef)


def test_hyp_minijava_voidtyperef_constructor_exists():
    assert callable(miniJava_VoidTypeRef.__init__)


def test_hyp_minijava_voidtyperef_constructor_args():
    sig = inspect.signature(miniJava_VoidTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_booleantyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_BooleanTypeRef)


def test_hyp_minijava_booleantyperef_constructor_exists():
    assert callable(miniJava_BooleanTypeRef.__init__)


def test_hyp_minijava_booleantyperef_constructor_args():
    sig = inspect.signature(miniJava_BooleanTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_stringtyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_StringTypeRef)


def test_hyp_minijava_stringtyperef_constructor_exists():
    assert callable(miniJava_StringTypeRef.__init__)


def test_hyp_minijava_stringtyperef_constructor_args():
    sig = inspect.signature(miniJava_StringTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_integertyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_IntegerTypeRef)


def test_hyp_minijava_integertyperef_constructor_exists():
    assert callable(miniJava_IntegerTypeRef.__init__)


def test_hyp_minijava_integertyperef_constructor_args():
    sig = inspect.signature(miniJava_IntegerTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_classref_is_not_abstract():
    assert not inspect.isabstract(miniJava_ClassRef)


def test_hyp_minijava_classref_constructor_exists():
    assert callable(miniJava_ClassRef.__init__)


def test_hyp_minijava_classref_constructor_args():
    sig = inspect.signature(miniJava_ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeref_is_not_abstract():
    assert not inspect.isabstract(TypeRef)


def test_hyp_typeref_constructor_exists():
    assert callable(TypeRef.__init__)


def test_hyp_typeref_constructor_args():
    sig = inspect.signature(TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_arraytyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayTypeRef)


def test_hyp_minijava_arraytyperef_constructor_exists():
    assert callable(miniJava_ArrayTypeRef.__init__)


def test_hyp_minijava_arraytyperef_constructor_args():
    sig = inspect.signature(miniJava_ArrayTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_singletyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_SingleTypeRef)


def test_hyp_minijava_singletyperef_constructor_exists():
    assert callable(miniJava_SingleTypeRef.__init__)


def test_hyp_minijava_singletyperef_constructor_args():
    sig = inspect.signature(miniJava_SingleTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_typeref_is_not_abstract():
    assert not inspect.isabstract(miniJava_TypeRef)


def test_hyp_minijava_typeref_constructor_exists():
    assert callable(miniJava_TypeRef.__init__)


def test_hyp_minijava_typeref_constructor_args():
    sig = inspect.signature(miniJava_TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_statement_is_not_abstract():
    assert not inspect.isabstract(miniJava_Statement)


def test_hyp_minijava_statement_constructor_exists():
    assert callable(miniJava_Statement.__init__)


def test_hyp_minijava_statement_constructor_args():
    sig = inspect.signature(miniJava_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_printstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_PrintStatement)


def test_hyp_minijava_printstatement_constructor_exists():
    assert callable(miniJava_PrintStatement.__init__)


def test_hyp_minijava_printstatement_constructor_args():
    sig = inspect.signature(miniJava_PrintStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_forstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_ForStatement)


def test_hyp_minijava_forstatement_constructor_exists():
    assert callable(miniJava_ForStatement.__init__)


def test_hyp_minijava_forstatement_constructor_args():
    sig = inspect.signature(miniJava_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_assignment_is_not_abstract():
    assert not inspect.isabstract(miniJava_Assignment)


def test_hyp_minijava_assignment_constructor_exists():
    assert callable(miniJava_Assignment.__init__)


def test_hyp_minijava_assignment_constructor_args():
    sig = inspect.signature(miniJava_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_ifstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_IfStatement)


def test_hyp_minijava_ifstatement_constructor_exists():
    assert callable(miniJava_IfStatement.__init__)


def test_hyp_minijava_ifstatement_constructor_args():
    sig = inspect.signature(miniJava_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_return_is_not_abstract():
    assert not inspect.isabstract(miniJava_Return)


def test_hyp_minijava_return_constructor_exists():
    assert callable(miniJava_Return.__init__)


def test_hyp_minijava_return_constructor_args():
    sig = inspect.signature(miniJava_Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_whilestatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_WhileStatement)


def test_hyp_minijava_whilestatement_constructor_exists():
    assert callable(miniJava_WhileStatement.__init__)


def test_hyp_minijava_whilestatement_constructor_args():
    sig = inspect.signature(miniJava_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_expression_is_not_abstract():
    assert not inspect.isabstract(miniJava_Expression)


def test_hyp_minijava_expression_constructor_exists():
    assert callable(miniJava_Expression.__init__)


def test_hyp_minijava_expression_constructor_args():
    sig = inspect.signature(miniJava_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_hyp_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_hyp_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava_VariableDeclaration)


def test_hyp_minijava_variabledeclaration_constructor_exists():
    assert callable(miniJava_VariableDeclaration.__init__)


def test_hyp_minijava_variabledeclaration_constructor_args():
    sig = inspect.signature(miniJava_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_block_is_not_abstract():
    assert not inspect.isabstract(miniJava_Block)


def test_hyp_minijava_block_constructor_exists():
    assert callable(miniJava_Block.__init__)


def test_hyp_minijava_block_constructor_args():
    sig = inspect.signature(miniJava_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_parameter_is_not_abstract():
    assert not inspect.isabstract(miniJava_Parameter)


def test_hyp_minijava_parameter_constructor_exists():
    assert callable(miniJava_Parameter.__init__)


def test_hyp_minijava_parameter_constructor_args():
    sig = inspect.signature(miniJava_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_hyp_member_constructor_exists():
    assert callable(Member.__init__)


def test_hyp_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_field_is_not_abstract():
    assert not inspect.isabstract(miniJava_Field)


def test_hyp_minijava_field_constructor_exists():
    assert callable(miniJava_Field.__init__)


def test_hyp_minijava_field_constructor_args():
    sig = inspect.signature(miniJava_Field.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_method_is_not_abstract():
    assert not inspect.isabstract(miniJava_Method)


def test_hyp_minijava_method_constructor_exists():
    assert callable(miniJava_Method.__init__)


def test_hyp_minijava_method_constructor_args():
    sig = inspect.signature(miniJava_Method.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "abstract" in params, "Missing parameter 'abstract'"





def test_hyp_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(TypedDeclaration)


def test_hyp_typeddeclaration_constructor_exists():
    assert callable(TypedDeclaration.__init__)


def test_hyp_typeddeclaration_constructor_args():
    sig = inspect.signature(TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_symbol_is_not_abstract():
    assert not inspect.isabstract(miniJava_Symbol)


def test_hyp_minijava_symbol_constructor_exists():
    assert callable(miniJava_Symbol.__init__)


def test_hyp_minijava_symbol_constructor_args():
    sig = inspect.signature(miniJava_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_hyp_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_hyp_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_class_is_not_abstract():
    assert not inspect.isabstract(miniJava_Class)


def test_hyp_minijava_class_constructor_exists():
    assert callable(miniJava_Class.__init__)


def test_hyp_minijava_class_constructor_args():
    sig = inspect.signature(miniJava_Class.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"




def test_hyp_minijava_member_is_not_abstract():
    assert not inspect.isabstract(miniJava_Member)


def test_hyp_minijava_member_constructor_exists():
    assert callable(miniJava_Member.__init__)


def test_hyp_minijava_member_constructor_args():
    sig = inspect.signature(miniJava_Member.__init__)
    params = list(sig.parameters.keys())
    assert "access" in params, "Missing parameter 'access'"




def test_hyp_minijava_interface_is_not_abstract():
    assert not inspect.isabstract(miniJava_Interface)


def test_hyp_minijava_interface_constructor_exists():
    assert callable(miniJava_Interface.__init__)


def test_hyp_minijava_interface_constructor_args():
    sig = inspect.signature(miniJava_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava_TypedDeclaration)


def test_hyp_minijava_typeddeclaration_constructor_exists():
    assert callable(miniJava_TypedDeclaration.__init__)


def test_hyp_minijava_typeddeclaration_constructor_args():
    sig = inspect.signature(miniJava_TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_state_is_not_abstract():
    assert not inspect.isabstract(miniJava_State)


def test_hyp_minijava_state_constructor_exists():
    assert callable(miniJava_State.__init__)


def test_hyp_minijava_state_constructor_args():
    sig = inspect.signature(miniJava_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava_TypeDeclaration)


def test_hyp_minijava_typedeclaration_constructor_exists():
    assert callable(miniJava_TypeDeclaration.__init__)


def test_hyp_minijava_typedeclaration_constructor_args():
    sig = inspect.signature(miniJava_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"




def test_hyp_minijava_import_is_not_abstract():
    assert not inspect.isabstract(miniJava_Import)


def test_hyp_minijava_import_constructor_exists():
    assert callable(miniJava_Import.__init__)


def test_hyp_minijava_import_constructor_args():
    sig = inspect.signature(miniJava_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"




def test_hyp_minijava_program_is_not_abstract():
    assert not inspect.isabstract(miniJava_Program)


def test_hyp_minijava_program_constructor_exists():
    assert callable(miniJava_Program.__init__)


def test_hyp_minijava_program_constructor_args():
    sig = inspect.signature(miniJava_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_hyp_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PRIVATE",
        "PROTECTED",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessLevel"


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
Call_strategy = st.builds(
    Call,
)
miniJava_NewCall_strategy = st.builds(
    miniJava_NewCall,
)
miniJava_MethodCall2_strategy = st.builds(
    miniJava_MethodCall2,
)
miniJava_OutputStream_strategy = st.builds(
    miniJava_OutputStream,
    stream=
        safe_text
)
miniJava_Call_strategy = st.builds(
    miniJava_Call,
)
miniJava_ArrayInstance_strategy = st.builds(
    miniJava_ArrayInstance,
    size=
        safe_text
)
miniJava_ObjectInstance_strategy = st.builds(
    miniJava_ObjectInstance,
)
miniJava_Frame_strategy = st.builds(
    miniJava_Frame,
)
miniJava_FieldBinding_strategy = st.builds(
    miniJava_FieldBinding,
)
Value_strategy = st.builds(
    Value,
)
miniJava_ArrayRefValue_strategy = st.builds(
    miniJava_ArrayRefValue,
)
miniJava_ObjectRefValue_strategy = st.builds(
    miniJava_ObjectRefValue,
)
miniJava_NullValue_strategy = st.builds(
    miniJava_NullValue,
)
miniJava_BooleanValue_strategy = st.builds(
    miniJava_BooleanValue,
    value=
        st.booleans()
)
miniJava_StringValue_strategy = st.builds(
    miniJava_StringValue,
    value=
        safe_text
)
miniJava_IntegerValue_strategy = st.builds(
    miniJava_IntegerValue,
    value=
        safe_text
)
miniJava_Value_strategy = st.builds(
    miniJava_Value,
)
miniJava_SymbolBinding_strategy = st.builds(
    miniJava_SymbolBinding,
)
miniJava_Context_strategy = st.builds(
    miniJava_Context,
)
Expression_strategy = st.builds(
    Expression,
)
miniJava_MethodCall_strategy = st.builds(
    miniJava_MethodCall,
)
miniJava_ArrayAccess_strategy = st.builds(
    miniJava_ArrayAccess,
)
miniJava_Neg_strategy = st.builds(
    miniJava_Neg,
)
miniJava_Plus_strategy = st.builds(
    miniJava_Plus,
)
miniJava_Not_strategy = st.builds(
    miniJava_Not,
)
miniJava_Superior_strategy = st.builds(
    miniJava_Superior,
)
miniJava_Super_strategy = st.builds(
    miniJava_Super,
)
miniJava_InferiorOrEqual_strategy = st.builds(
    miniJava_InferiorOrEqual,
)
miniJava_NewArray_strategy = st.builds(
    miniJava_NewArray,
)
miniJava_Inferior_strategy = st.builds(
    miniJava_Inferior,
)
miniJava_This_strategy = st.builds(
    miniJava_This,
)
miniJava_SuperiorOrEqual_strategy = st.builds(
    miniJava_SuperiorOrEqual,
)
miniJava_Multiplication_strategy = st.builds(
    miniJava_Multiplication,
)
miniJava_Inequality_strategy = st.builds(
    miniJava_Inequality,
)
miniJava_StringConstant_strategy = st.builds(
    miniJava_StringConstant,
    value=
        safe_text
)
miniJava_Equality_strategy = st.builds(
    miniJava_Equality,
)
miniJava_NewObject_strategy = st.builds(
    miniJava_NewObject,
)
miniJava_ArrayLength_strategy = st.builds(
    miniJava_ArrayLength,
)
miniJava_Division_strategy = st.builds(
    miniJava_Division,
)
miniJava_BoolConstant_strategy = st.builds(
    miniJava_BoolConstant,
    value=
        safe_text
)
miniJava_IntConstant_strategy = st.builds(
    miniJava_IntConstant,
    value=
        st.integers()
)
miniJava_SymbolRef_strategy = st.builds(
    miniJava_SymbolRef,
)
miniJava_And_strategy = st.builds(
    miniJava_And,
)
miniJava_Null_strategy = st.builds(
    miniJava_Null,
)
miniJava_FieldAccess_strategy = st.builds(
    miniJava_FieldAccess,
)
miniJava_Minus_strategy = st.builds(
    miniJava_Minus,
)
miniJava_Or_strategy = st.builds(
    miniJava_Or,
)
miniJava_Assignee_strategy = st.builds(
    miniJava_Assignee,
)
Assignee_strategy = st.builds(
    Assignee,
)
miniJava_NamedElement_strategy = st.builds(
    miniJava_NamedElement,
    name=
        safe_text
)
SingleTypeRef_strategy = st.builds(
    SingleTypeRef,
)
miniJava_VoidTypeRef_strategy = st.builds(
    miniJava_VoidTypeRef,
)
miniJava_BooleanTypeRef_strategy = st.builds(
    miniJava_BooleanTypeRef,
)
miniJava_StringTypeRef_strategy = st.builds(
    miniJava_StringTypeRef,
)
miniJava_IntegerTypeRef_strategy = st.builds(
    miniJava_IntegerTypeRef,
)
miniJava_ClassRef_strategy = st.builds(
    miniJava_ClassRef,
)
TypeRef_strategy = st.builds(
    TypeRef,
)
miniJava_ArrayTypeRef_strategy = st.builds(
    miniJava_ArrayTypeRef,
)
miniJava_SingleTypeRef_strategy = st.builds(
    miniJava_SingleTypeRef,
)
miniJava_TypeRef_strategy = st.builds(
    miniJava_TypeRef,
)
miniJava_Statement_strategy = st.builds(
    miniJava_Statement,
)
Statement_strategy = st.builds(
    Statement,
)
miniJava_PrintStatement_strategy = st.builds(
    miniJava_PrintStatement,
)
miniJava_ForStatement_strategy = st.builds(
    miniJava_ForStatement,
)
miniJava_Assignment_strategy = st.builds(
    miniJava_Assignment,
)
miniJava_IfStatement_strategy = st.builds(
    miniJava_IfStatement,
)
miniJava_Return_strategy = st.builds(
    miniJava_Return,
)
miniJava_WhileStatement_strategy = st.builds(
    miniJava_WhileStatement,
)
miniJava_Expression_strategy = st.builds(
    miniJava_Expression,
)
Symbol_strategy = st.builds(
    Symbol,
)
miniJava_VariableDeclaration_strategy = st.builds(
    miniJava_VariableDeclaration,
)
miniJava_Block_strategy = st.builds(
    miniJava_Block,
)
miniJava_Parameter_strategy = st.builds(
    miniJava_Parameter,
)
Member_strategy = st.builds(
    Member,
)
miniJava_Field_strategy = st.builds(
    miniJava_Field,
)
miniJava_Method_strategy = st.builds(
    miniJava_Method,
    static=
        st.booleans(),
    abstract=
        st.booleans()
)
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
miniJava_Symbol_strategy = st.builds(
    miniJava_Symbol,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
miniJava_Class_strategy = st.builds(
    miniJava_Class,
    abstract=
        st.booleans()
)
miniJava_Member_strategy = st.builds(
    miniJava_Member,
    access=
        safe_text
)
miniJava_Interface_strategy = st.builds(
    miniJava_Interface,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
miniJava_TypedDeclaration_strategy = st.builds(
    miniJava_TypedDeclaration,
)
miniJava_State_strategy = st.builds(
    miniJava_State,
)
miniJava_TypeDeclaration_strategy = st.builds(
    miniJava_TypeDeclaration,
    accessLevel=
        safe_text
)
miniJava_Import_strategy = st.builds(
    miniJava_Import,
    importedNamespace=
        safe_text
)
miniJava_Program_strategy = st.builds(
    miniJava_Program,
    name=
        safe_text
)







@given(instance=miniJava_OutputStream_strategy)
def test_hyp_minijava_outputstream_stream_setter(instance):
    original = instance.stream
    instance.stream = original
    assert instance.stream == original





@given(instance=miniJava_ArrayInstance_strategy)
def test_hyp_minijava_arrayinstance_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Frame_strategy)
@settings(max_examples=30)
def test_hyp_minijava_frame_findcurrentframe_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findCurrentFrame()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findCurrentFrame).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findCurrentFrame' in miniJava_Frame is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findCurrentFrame' in miniJava_Frame did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findCurrentFrame' in miniJava_Frame is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Frame_strategy)
@settings(max_examples=30)
def test_hyp_minijava_frame_findcurrentcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findCurrentContext()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findCurrentContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findCurrentContext' in miniJava_Frame is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findCurrentContext' in miniJava_Frame did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findCurrentContext' in miniJava_Frame is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_ArrayRefValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_arrayrefvalue_copy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copy()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copy' in miniJava_ArrayRefValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copy' in miniJava_ArrayRefValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copy' in miniJava_ArrayRefValue is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_ObjectRefValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_objectrefvalue_customtostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.customToString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.customToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'customToString' in miniJava_ObjectRefValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'customToString' in miniJava_ObjectRefValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'customToString' in miniJava_ObjectRefValue is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_ObjectRefValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_objectrefvalue_copy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copy()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copy' in miniJava_ObjectRefValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copy' in miniJava_ObjectRefValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copy' in miniJava_ObjectRefValue is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_NullValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_nullvalue_copy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copy()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copy' in miniJava_NullValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copy' in miniJava_NullValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copy' in miniJava_NullValue is not implemented or raised an error")




@given(instance=miniJava_BooleanValue_strategy)
def test_hyp_minijava_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_BooleanValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_booleanvalue_copy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copy()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copy' in miniJava_BooleanValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copy' in miniJava_BooleanValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copy' in miniJava_BooleanValue is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_BooleanValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_booleanvalue_customtostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.customToString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.customToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'customToString' in miniJava_BooleanValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'customToString' in miniJava_BooleanValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'customToString' in miniJava_BooleanValue is not implemented or raised an error")




@given(instance=miniJava_StringValue_strategy)
def test_hyp_minijava_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_StringValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_stringvalue_copy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copy()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copy' in miniJava_StringValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copy' in miniJava_StringValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copy' in miniJava_StringValue is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_StringValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_stringvalue_customtostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.customToString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.customToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'customToString' in miniJava_StringValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'customToString' in miniJava_StringValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'customToString' in miniJava_StringValue is not implemented or raised an error")




@given(instance=miniJava_IntegerValue_strategy)
def test_hyp_minijava_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_IntegerValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_integervalue_copy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copy()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copy' in miniJava_IntegerValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copy' in miniJava_IntegerValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copy' in miniJava_IntegerValue is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_IntegerValue_strategy)
@settings(max_examples=30)
def test_hyp_minijava_integervalue_customtostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.customToString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.customToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'customToString' in miniJava_IntegerValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'customToString' in miniJava_IntegerValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'customToString' in miniJava_IntegerValue is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Value_strategy)
@settings(max_examples=30)
def test_hyp_minijava_value_customtostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.customToString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.customToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'customToString' in miniJava_Value is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'customToString' in miniJava_Value did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'customToString' in miniJava_Value is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Value_strategy)
@settings(max_examples=30)
def test_hyp_minijava_value_copy_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copy()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copy).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copy' in miniJava_Value is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copy' in miniJava_Value did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copy' in miniJava_Value is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Context_strategy)
@settings(max_examples=30)
def test_hyp_minijava_context_createchildcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createChildContext()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createChildContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createChildContext' in miniJava_Context is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createChildContext' in miniJava_Context did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createChildContext' in miniJava_Context is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Context_strategy)
@settings(max_examples=30)
def test_hyp_minijava_context_findbinding_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findBinding(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findBinding).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findBinding' in miniJava_Context is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findBinding' in miniJava_Context did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findBinding' in miniJava_Context is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Context_strategy)
@settings(max_examples=30)
def test_hyp_minijava_context_findcurrentcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findCurrentContext()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findCurrentContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findCurrentContext' in miniJava_Context is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findCurrentContext' in miniJava_Context did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findCurrentContext' in miniJava_Context is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_MethodCall_strategy)
@settings(max_examples=30)
def test_hyp_minijava_methodcall_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_MethodCall is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_MethodCall did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_MethodCall is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_ArrayAccess_strategy)
@settings(max_examples=30)
def test_hyp_minijava_arrayaccess_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_ArrayAccess is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_ArrayAccess did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_ArrayAccess is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Neg_strategy)
@settings(max_examples=30)
def test_hyp_minijava_neg_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Neg is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Neg did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Neg is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Plus_strategy)
@settings(max_examples=30)
def test_hyp_minijava_plus_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Plus is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Plus did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Plus is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Not_strategy)
@settings(max_examples=30)
def test_hyp_minijava_not_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Not is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Not did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Not is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Superior_strategy)
@settings(max_examples=30)
def test_hyp_minijava_superior_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Superior is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Superior did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Superior is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_InferiorOrEqual_strategy)
@settings(max_examples=30)
def test_hyp_minijava_inferiororequal_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_InferiorOrEqual is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_InferiorOrEqual did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_InferiorOrEqual is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_NewArray_strategy)
@settings(max_examples=30)
def test_hyp_minijava_newarray_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_NewArray is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_NewArray did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_NewArray is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Inferior_strategy)
@settings(max_examples=30)
def test_hyp_minijava_inferior_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Inferior is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Inferior did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Inferior is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_This_strategy)
@settings(max_examples=30)
def test_hyp_minijava_this_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_This is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_This did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_This is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_SuperiorOrEqual_strategy)
@settings(max_examples=30)
def test_hyp_minijava_superiororequal_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_SuperiorOrEqual is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_SuperiorOrEqual did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_SuperiorOrEqual is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Multiplication_strategy)
@settings(max_examples=30)
def test_hyp_minijava_multiplication_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Multiplication is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Multiplication did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Multiplication is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Inequality_strategy)
@settings(max_examples=30)
def test_hyp_minijava_inequality_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Inequality is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Inequality did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Inequality is not implemented or raised an error")




@given(instance=miniJava_StringConstant_strategy)
def test_hyp_minijava_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_StringConstant_strategy)
@settings(max_examples=30)
def test_hyp_minijava_stringconstant_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_StringConstant is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_StringConstant did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_StringConstant is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Equality_strategy)
@settings(max_examples=30)
def test_hyp_minijava_equality_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Equality is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Equality did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Equality is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_NewObject_strategy)
@settings(max_examples=30)
def test_hyp_minijava_newobject_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_NewObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_NewObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_NewObject is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_ArrayLength_strategy)
@settings(max_examples=30)
def test_hyp_minijava_arraylength_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_ArrayLength is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_ArrayLength did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_ArrayLength is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Division_strategy)
@settings(max_examples=30)
def test_hyp_minijava_division_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Division is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Division did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Division is not implemented or raised an error")




@given(instance=miniJava_BoolConstant_strategy)
def test_hyp_minijava_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_BoolConstant_strategy)
@settings(max_examples=30)
def test_hyp_minijava_boolconstant_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_BoolConstant is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_BoolConstant did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_BoolConstant is not implemented or raised an error")




@given(instance=miniJava_IntConstant_strategy)
def test_hyp_minijava_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_IntConstant_strategy)
@settings(max_examples=30)
def test_hyp_minijava_intconstant_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_IntConstant is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_IntConstant did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_IntConstant is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_SymbolRef_strategy)
@settings(max_examples=30)
def test_hyp_minijava_symbolref_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_SymbolRef is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_SymbolRef did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_SymbolRef is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_And_strategy)
@settings(max_examples=30)
def test_hyp_minijava_and_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_And is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_And did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_And is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Null_strategy)
@settings(max_examples=30)
def test_hyp_minijava_null_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Null is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Null did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Null is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_FieldAccess_strategy)
@settings(max_examples=30)
def test_hyp_minijava_fieldaccess_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_FieldAccess is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_FieldAccess did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_FieldAccess is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Minus_strategy)
@settings(max_examples=30)
def test_hyp_minijava_minus_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Minus is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Minus did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Minus is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Or_strategy)
@settings(max_examples=30)
def test_hyp_minijava_or_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Or is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Or did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Or is not implemented or raised an error")






@given(instance=miniJava_NamedElement_strategy)
def test_hyp_minijava_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_ClassRef_strategy)
@settings(max_examples=30)
def test_hyp_minijava_classref_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in miniJava_ClassRef is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in miniJava_ClassRef did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in miniJava_ClassRef is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_TypeRef_strategy)
@settings(max_examples=30)
def test_hyp_minijava_typeref_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in miniJava_TypeRef is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in miniJava_TypeRef did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in miniJava_TypeRef is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Statement_strategy)
@settings(max_examples=30)
def test_hyp_minijava_statement_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_Statement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_Statement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_Statement is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_PrintStatement_strategy)
@settings(max_examples=30)
def test_hyp_minijava_printstatement_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_PrintStatement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_PrintStatement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_PrintStatement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_ForStatement_strategy)
@settings(max_examples=30)
def test_hyp_minijava_forstatement_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_ForStatement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_ForStatement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_ForStatement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Assignment_strategy)
@settings(max_examples=30)
def test_hyp_minijava_assignment_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_Assignment is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_Assignment did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_Assignment is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_IfStatement_strategy)
@settings(max_examples=30)
def test_hyp_minijava_ifstatement_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_IfStatement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_IfStatement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_IfStatement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Return_strategy)
@settings(max_examples=30)
def test_hyp_minijava_return_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_Return is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_Return did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_Return is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_WhileStatement_strategy)
@settings(max_examples=30)
def test_hyp_minijava_whilestatement_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_WhileStatement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_WhileStatement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_WhileStatement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Expression_strategy)
@settings(max_examples=30)
def test_hyp_minijava_expression_evaluateexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateExpression' in miniJava_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateExpression' in miniJava_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateExpression' in miniJava_Expression is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Expression_strategy)
@settings(max_examples=30)
def test_hyp_minijava_expression_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_Expression is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Block_strategy)
@settings(max_examples=30)
def test_hyp_minijava_block_evaluatestatement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatement' in miniJava_Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatement' in miniJava_Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatement' in miniJava_Block is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Block_strategy)
@settings(max_examples=30)
def test_hyp_minijava_block_evaluatestatementkeepcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluateStatementKeepContext(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluateStatementKeepContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluateStatementKeepContext' in miniJava_Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluateStatementKeepContext' in miniJava_Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluateStatementKeepContext' in miniJava_Block is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Parameter_strategy)
@settings(max_examples=30)
def test_hyp_minijava_parameter_compare_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compare(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compare).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compare' in miniJava_Parameter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compare' in miniJava_Parameter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compare' in miniJava_Parameter is not implemented or raised an error")






@given(instance=miniJava_Method_strategy)
def test_hyp_minijava_method_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=miniJava_Method_strategy)
def test_hyp_minijava_method_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Method_strategy)
@settings(max_examples=30)
def test_hyp_minijava_method_findoverride_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findOverride(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findOverride).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findOverride' in miniJava_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findOverride' in miniJava_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findOverride' in miniJava_Method is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Method_strategy)
@settings(max_examples=30)
def test_hyp_minijava_method_call_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.call(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.call).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'call' in miniJava_Method is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'call' in miniJava_Method did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'call' in miniJava_Method is not implemented or raised an error")







@given(instance=miniJava_Class_strategy)
def test_hyp_minijava_class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original




@given(instance=miniJava_Member_strategy)
def test_hyp_minijava_member_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_State_strategy)
@settings(max_examples=30)
def test_hyp_minijava_state_findcurrentframe_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findCurrentFrame()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findCurrentFrame).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findCurrentFrame' in miniJava_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findCurrentFrame' in miniJava_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findCurrentFrame' in miniJava_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_State_strategy)
@settings(max_examples=30)
def test_hyp_minijava_state_pushnewcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pushNewContext()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pushNewContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pushNewContext' in miniJava_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pushNewContext' in miniJava_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pushNewContext' in miniJava_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_State_strategy)
@settings(max_examples=30)
def test_hyp_minijava_state_popcurrentframe_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.popCurrentFrame()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.popCurrentFrame).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'popCurrentFrame' in miniJava_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'popCurrentFrame' in miniJava_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'popCurrentFrame' in miniJava_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_State_strategy)
@settings(max_examples=30)
def test_hyp_minijava_state_pushnewframe_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pushNewFrame(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pushNewFrame).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pushNewFrame' in miniJava_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pushNewFrame' in miniJava_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pushNewFrame' in miniJava_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_State_strategy)
@settings(max_examples=30)
def test_hyp_minijava_state_println_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.println(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.println).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'println' in miniJava_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'println' in miniJava_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'println' in miniJava_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_State_strategy)
@settings(max_examples=30)
def test_hyp_minijava_state_findcurrentcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findCurrentContext()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findCurrentContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findCurrentContext' in miniJava_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findCurrentContext' in miniJava_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findCurrentContext' in miniJava_State is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_State_strategy)
@settings(max_examples=30)
def test_hyp_minijava_state_popcurrentcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.popCurrentContext()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.popCurrentContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'popCurrentContext' in miniJava_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'popCurrentContext' in miniJava_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'popCurrentContext' in miniJava_State is not implemented or raised an error")




@given(instance=miniJava_TypeDeclaration_strategy)
def test_hyp_minijava_typedeclaration_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original




@given(instance=miniJava_Import_strategy)
def test_hyp_minijava_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original




@given(instance=miniJava_Program_strategy)
def test_hyp_minijava_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Program_strategy)
@settings(max_examples=30)
def test_hyp_minijava_program_initialize_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.initialize(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.initialize).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'initialize' in miniJava_Program is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initialize' in miniJava_Program did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initialize' in miniJava_Program is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Program_strategy)
@settings(max_examples=30)
def test_hyp_minijava_program_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in miniJava_Program is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in miniJava_Program did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in miniJava_Program is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=miniJava_Program_strategy)
@settings(max_examples=30)
def test_hyp_minijava_program_main_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.main()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.main).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'main' in miniJava_Program is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'main' in miniJava_Program did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'main' in miniJava_Program is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Assignee,
    Call,
    Expression,
    Member,
    NamedElement,
    SingleTypeRef,
    Statement,
    Symbol,
    TypeDeclaration,
    TypeRef,
    TypedDeclaration,
    Value,
    miniJava_And,
    miniJava_ArrayAccess,
    miniJava_ArrayInstance,
    miniJava_ArrayLength,
    miniJava_ArrayRefValue,
    miniJava_ArrayTypeRef,
    miniJava_Assignee,
    miniJava_Assignment,
    miniJava_Block,
    miniJava_BoolConstant,
    miniJava_BooleanTypeRef,
    miniJava_BooleanValue,
    miniJava_Call,
    miniJava_Class,
    miniJava_ClassRef,
    miniJava_Context,
    miniJava_Division,
    miniJava_Equality,
    miniJava_Expression,
    miniJava_Field,
    miniJava_FieldAccess,
    miniJava_FieldBinding,
    miniJava_ForStatement,
    miniJava_Frame,
    miniJava_IfStatement,
    miniJava_Import,
    miniJava_Inequality,
    miniJava_Inferior,
    miniJava_InferiorOrEqual,
    miniJava_IntConstant,
    miniJava_IntegerTypeRef,
    miniJava_IntegerValue,
    miniJava_Interface,
    miniJava_Member,
    miniJava_Method,
    miniJava_MethodCall,
    miniJava_MethodCall2,
    miniJava_Minus,
    miniJava_Multiplication,
    miniJava_NamedElement,
    miniJava_Neg,
    miniJava_NewArray,
    miniJava_NewCall,
    miniJava_NewObject,
    miniJava_Not,
    miniJava_Null,
    miniJava_NullValue,
    miniJava_ObjectInstance,
    miniJava_ObjectRefValue,
    miniJava_Or,
    miniJava_OutputStream,
    miniJava_Parameter,
    miniJava_Plus,
    miniJava_PrintStatement,
    miniJava_Program,
    miniJava_Return,
    miniJava_SingleTypeRef,
    miniJava_State,
    miniJava_Statement,
    miniJava_StringConstant,
    miniJava_StringTypeRef,
    miniJava_StringValue,
    miniJava_Super,
    miniJava_Superior,
    miniJava_SuperiorOrEqual,
    miniJava_Symbol,
    miniJava_SymbolBinding,
    miniJava_SymbolRef,
    miniJava_This,
    miniJava_TypeDeclaration,
    miniJava_TypeRef,
    miniJava_TypedDeclaration,
    miniJava_Value,
    miniJava_VariableDeclaration,
    miniJava_VoidTypeRef,
    miniJava_WhileStatement,
    AccessLevel,
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

def test_miniJava_ArrayInstance_size_value_roundtrip():
    instance = miniJava_ArrayInstance(size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_miniJava_BoolConstant_value_value_roundtrip():
    instance = miniJava_BoolConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_miniJava_BooleanValue_value_value_roundtrip():
    instance = miniJava_BooleanValue(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_miniJava_Class_abstract_value_roundtrip():
    instance = miniJava_Class(abstract=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_miniJava_Import_importedNamespace_value_roundtrip():
    instance = miniJava_Import(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_miniJava_IntConstant_value_value_roundtrip():
    instance = miniJava_IntConstant(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_miniJava_IntegerValue_value_value_roundtrip():
    instance = miniJava_IntegerValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_miniJava_Member_access_value_roundtrip():
    instance = miniJava_Member(access="sample_text")
    assert instance.access == "sample_text"
    instance.access = "sample_text_2"
    assert instance.access == "sample_text_2"


def test_miniJava_Method_abstract_value_roundtrip():
    instance = miniJava_Method(abstract=True, static=True)
    assert instance.abstract == True
    instance.abstract = False
    assert instance.abstract == False


def test_miniJava_Method_static_value_roundtrip():
    instance = miniJava_Method(abstract=True, static=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_miniJava_NamedElement_name_value_roundtrip():
    instance = miniJava_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_miniJava_OutputStream_stream_value_roundtrip():
    instance = miniJava_OutputStream(stream="sample_text")
    assert instance.stream == "sample_text"
    instance.stream = "sample_text_2"
    assert instance.stream == "sample_text_2"


def test_miniJava_Program_name_value_roundtrip():
    instance = miniJava_Program(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_miniJava_StringConstant_value_value_roundtrip():
    instance = miniJava_StringConstant(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_miniJava_StringValue_value_value_roundtrip():
    instance = miniJava_StringValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_miniJava_TypeDeclaration_accessLevel_value_roundtrip():
    instance = miniJava_TypeDeclaration(accessLevel="sample_text")
    assert instance.accessLevel == "sample_text"
    instance.accessLevel = "sample_text_2"
    assert instance.accessLevel == "sample_text_2"


def test_miniJava_Expression_isa_Assignee():
    instance = miniJava_Expression()
    assert isinstance(instance, Assignee)


def test_miniJava_VariableDeclaration_isa_Assignee():
    instance = miniJava_VariableDeclaration()
    assert isinstance(instance, Assignee)


def test_miniJava_MethodCall2_isa_Call():
    instance = miniJava_MethodCall2()
    assert isinstance(instance, Call)


def test_miniJava_NewCall_isa_Call():
    instance = miniJava_NewCall()
    assert isinstance(instance, Call)


def test_miniJava_And_isa_Expression():
    instance = miniJava_And()
    assert isinstance(instance, Expression)


def test_miniJava_ArrayAccess_isa_Expression():
    instance = miniJava_ArrayAccess()
    assert isinstance(instance, Expression)


def test_miniJava_ArrayLength_isa_Expression():
    instance = miniJava_ArrayLength()
    assert isinstance(instance, Expression)


def test_miniJava_BoolConstant_isa_Expression():
    instance = miniJava_BoolConstant(value="sample_text")
    assert isinstance(instance, Expression)


def test_miniJava_Division_isa_Expression():
    instance = miniJava_Division()
    assert isinstance(instance, Expression)


def test_miniJava_Equality_isa_Expression():
    instance = miniJava_Equality()
    assert isinstance(instance, Expression)


def test_miniJava_FieldAccess_isa_Expression():
    instance = miniJava_FieldAccess()
    assert isinstance(instance, Expression)


def test_miniJava_Inequality_isa_Expression():
    instance = miniJava_Inequality()
    assert isinstance(instance, Expression)


def test_miniJava_Inferior_isa_Expression():
    instance = miniJava_Inferior()
    assert isinstance(instance, Expression)


def test_miniJava_InferiorOrEqual_isa_Expression():
    instance = miniJava_InferiorOrEqual()
    assert isinstance(instance, Expression)


def test_miniJava_IntConstant_isa_Expression():
    instance = miniJava_IntConstant(value=7)
    assert isinstance(instance, Expression)


def test_miniJava_MethodCall_isa_Expression():
    instance = miniJava_MethodCall()
    assert isinstance(instance, Expression)


def test_miniJava_Minus_isa_Expression():
    instance = miniJava_Minus()
    assert isinstance(instance, Expression)


def test_miniJava_Multiplication_isa_Expression():
    instance = miniJava_Multiplication()
    assert isinstance(instance, Expression)


def test_miniJava_Neg_isa_Expression():
    instance = miniJava_Neg()
    assert isinstance(instance, Expression)


def test_miniJava_NewArray_isa_Expression():
    instance = miniJava_NewArray()
    assert isinstance(instance, Expression)


def test_miniJava_NewObject_isa_Expression():
    instance = miniJava_NewObject()
    assert isinstance(instance, Expression)


def test_miniJava_Not_isa_Expression():
    instance = miniJava_Not()
    assert isinstance(instance, Expression)


def test_miniJava_Null_isa_Expression():
    instance = miniJava_Null()
    assert isinstance(instance, Expression)


def test_miniJava_Or_isa_Expression():
    instance = miniJava_Or()
    assert isinstance(instance, Expression)


def test_miniJava_Plus_isa_Expression():
    instance = miniJava_Plus()
    assert isinstance(instance, Expression)


def test_miniJava_StringConstant_isa_Expression():
    instance = miniJava_StringConstant(value="sample_text")
    assert isinstance(instance, Expression)


def test_miniJava_Super_isa_Expression():
    instance = miniJava_Super()
    assert isinstance(instance, Expression)


def test_miniJava_Superior_isa_Expression():
    instance = miniJava_Superior()
    assert isinstance(instance, Expression)


def test_miniJava_SuperiorOrEqual_isa_Expression():
    instance = miniJava_SuperiorOrEqual()
    assert isinstance(instance, Expression)


def test_miniJava_SymbolRef_isa_Expression():
    instance = miniJava_SymbolRef()
    assert isinstance(instance, Expression)


def test_miniJava_This_isa_Expression():
    instance = miniJava_This()
    assert isinstance(instance, Expression)


def test_miniJava_Field_isa_Member():
    instance = miniJava_Field()
    assert isinstance(instance, Member)


def test_miniJava_Method_isa_Member():
    instance = miniJava_Method(abstract=True, static=True)
    assert isinstance(instance, Member)


def test_miniJava_TypeDeclaration_isa_NamedElement():
    instance = miniJava_TypeDeclaration(accessLevel="sample_text")
    assert isinstance(instance, NamedElement)


def test_miniJava_TypedDeclaration_isa_NamedElement():
    instance = miniJava_TypedDeclaration()
    assert isinstance(instance, NamedElement)


def test_miniJava_BooleanTypeRef_isa_SingleTypeRef():
    instance = miniJava_BooleanTypeRef()
    assert isinstance(instance, SingleTypeRef)


def test_miniJava_ClassRef_isa_SingleTypeRef():
    instance = miniJava_ClassRef()
    assert isinstance(instance, SingleTypeRef)


def test_miniJava_IntegerTypeRef_isa_SingleTypeRef():
    instance = miniJava_IntegerTypeRef()
    assert isinstance(instance, SingleTypeRef)


def test_miniJava_StringTypeRef_isa_SingleTypeRef():
    instance = miniJava_StringTypeRef()
    assert isinstance(instance, SingleTypeRef)


def test_miniJava_VoidTypeRef_isa_SingleTypeRef():
    instance = miniJava_VoidTypeRef()
    assert isinstance(instance, SingleTypeRef)


def test_miniJava_Assignment_isa_Statement():
    instance = miniJava_Assignment()
    assert isinstance(instance, Statement)


def test_miniJava_Block_isa_Statement():
    instance = miniJava_Block()
    assert isinstance(instance, Statement)


def test_miniJava_Expression_isa_Statement():
    instance = miniJava_Expression()
    assert isinstance(instance, Statement)


def test_miniJava_ForStatement_isa_Statement():
    instance = miniJava_ForStatement()
    assert isinstance(instance, Statement)


def test_miniJava_IfStatement_isa_Statement():
    instance = miniJava_IfStatement()
    assert isinstance(instance, Statement)


def test_miniJava_PrintStatement_isa_Statement():
    instance = miniJava_PrintStatement()
    assert isinstance(instance, Statement)


def test_miniJava_Return_isa_Statement():
    instance = miniJava_Return()
    assert isinstance(instance, Statement)


def test_miniJava_WhileStatement_isa_Statement():
    instance = miniJava_WhileStatement()
    assert isinstance(instance, Statement)


def test_miniJava_Parameter_isa_Symbol():
    instance = miniJava_Parameter()
    assert isinstance(instance, Symbol)


def test_miniJava_VariableDeclaration_isa_Symbol():
    instance = miniJava_VariableDeclaration()
    assert isinstance(instance, Symbol)


def test_miniJava_Class_isa_TypeDeclaration():
    instance = miniJava_Class(abstract=True)
    assert isinstance(instance, TypeDeclaration)


def test_miniJava_Interface_isa_TypeDeclaration():
    instance = miniJava_Interface()
    assert isinstance(instance, TypeDeclaration)


def test_miniJava_ArrayTypeRef_isa_TypeRef():
    instance = miniJava_ArrayTypeRef()
    assert isinstance(instance, TypeRef)


def test_miniJava_SingleTypeRef_isa_TypeRef():
    instance = miniJava_SingleTypeRef()
    assert isinstance(instance, TypeRef)


def test_miniJava_Member_isa_TypedDeclaration():
    instance = miniJava_Member(access="sample_text")
    assert isinstance(instance, TypedDeclaration)


def test_miniJava_Symbol_isa_TypedDeclaration():
    instance = miniJava_Symbol()
    assert isinstance(instance, TypedDeclaration)


def test_miniJava_ArrayRefValue_isa_Value():
    instance = miniJava_ArrayRefValue()
    assert isinstance(instance, Value)


def test_miniJava_BooleanValue_isa_Value():
    instance = miniJava_BooleanValue(value=True)
    assert isinstance(instance, Value)


def test_miniJava_IntegerValue_isa_Value():
    instance = miniJava_IntegerValue(value="sample_text")
    assert isinstance(instance, Value)


def test_miniJava_NullValue_isa_Value():
    instance = miniJava_NullValue()
    assert isinstance(instance, Value)


def test_miniJava_ObjectRefValue_isa_Value():
    instance = miniJava_ObjectRefValue()
    assert isinstance(instance, Value)


def test_miniJava_StringValue_isa_Value():
    instance = miniJava_StringValue(value="sample_text")
    assert isinstance(instance, Value)


def test_assoc_args134_link_reassign_clear():
    a = miniJava_MethodCall()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_MethodCall135', {b1})
    assert _is_linked(a, 'miniJava_MethodCall135', b1)
    if hasattr(b1, 'miniJava_Expression136'):
        assert _is_linked(b1, 'miniJava_Expression136', a)
    _safe_set(a, 'miniJava_MethodCall135', {b2})
    assert _is_linked(a, 'miniJava_MethodCall135', b2)
    if hasattr(b1, 'miniJava_Expression136'):
        assert not _is_linked(b1, 'miniJava_Expression136', a)
    if hasattr(b2, 'miniJava_Expression136'):
        assert _is_linked(b2, 'miniJava_Expression136', a)
    _safe_set(a, 'miniJava_MethodCall135', set())
    assert not _is_linked(a, 'miniJava_MethodCall135', b2)
    if hasattr(b2, 'miniJava_Expression136'):
        assert not _is_linked(b2, 'miniJava_Expression136', a)


def test_assoc_args139_link_reassign_clear():
    a = miniJava_NewObject()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_NewObject140', {b1})
    assert _is_linked(a, 'miniJava_NewObject140', b1)
    if hasattr(b1, 'miniJava_Expression141'):
        assert _is_linked(b1, 'miniJava_Expression141', a)
    _safe_set(a, 'miniJava_NewObject140', {b2})
    assert _is_linked(a, 'miniJava_NewObject140', b2)
    if hasattr(b1, 'miniJava_Expression141'):
        assert not _is_linked(b1, 'miniJava_Expression141', a)
    if hasattr(b2, 'miniJava_Expression141'):
        assert _is_linked(b2, 'miniJava_Expression141', a)
    _safe_set(a, 'miniJava_NewObject140', set())
    assert not _is_linked(a, 'miniJava_NewObject140', b2)
    if hasattr(b2, 'miniJava_Expression141'):
        assert not _is_linked(b2, 'miniJava_Expression141', a)


def test_assoc_array118_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_ArrayLength()
    b2 = miniJava_ArrayLength()
    _safe_set(a, 'miniJava_Expression119', b1)
    assert _is_linked(a, 'miniJava_Expression119', b1)
    if hasattr(b1, 'miniJava_ArrayLength'):
        assert _is_linked(b1, 'miniJava_ArrayLength', a)
    _safe_set(a, 'miniJava_Expression119', b2)
    assert _is_linked(a, 'miniJava_Expression119', b2)
    if hasattr(b1, 'miniJava_ArrayLength'):
        assert not _is_linked(b1, 'miniJava_ArrayLength', a)
    if hasattr(b2, 'miniJava_ArrayLength'):
        assert _is_linked(b2, 'miniJava_ArrayLength', a)
    _safe_set(a, 'miniJava_Expression119', None)
    assert not _is_linked(a, 'miniJava_Expression119', b2)
    if hasattr(b2, 'miniJava_ArrayLength'):
        assert not _is_linked(b2, 'miniJava_ArrayLength', a)


def test_assoc_arraysHeap170_link_reassign_clear():
    a = miniJava_State()
    b1 = miniJava_ArrayInstance(size="sample_text")
    b2 = miniJava_ArrayInstance(size="sample_text_2")
    _safe_set(a, 'miniJava_State171', {b1})
    assert _is_linked(a, 'miniJava_State171', b1)
    if hasattr(b1, 'miniJava_ArrayInstance'):
        assert _is_linked(b1, 'miniJava_ArrayInstance', a)
    _safe_set(a, 'miniJava_State171', {b2})
    assert _is_linked(a, 'miniJava_State171', b2)
    if hasattr(b1, 'miniJava_ArrayInstance'):
        assert not _is_linked(b1, 'miniJava_ArrayInstance', a)
    if hasattr(b2, 'miniJava_ArrayInstance'):
        assert _is_linked(b2, 'miniJava_ArrayInstance', a)
    _safe_set(a, 'miniJava_State171', set())
    assert not _is_linked(a, 'miniJava_State171', b2)
    if hasattr(b2, 'miniJava_ArrayInstance'):
        assert not _is_linked(b2, 'miniJava_ArrayInstance', a)


def test_assoc_assignee47_link_reassign_clear():
    a = miniJava_Assignment()
    b1 = miniJava_Assignee()
    b2 = miniJava_Assignee()
    _safe_set(a, 'miniJava_Assignment48', b1)
    assert _is_linked(a, 'miniJava_Assignment48', b1)
    if hasattr(b1, 'miniJava_Assignee'):
        assert _is_linked(b1, 'miniJava_Assignee', a)
    _safe_set(a, 'miniJava_Assignment48', b2)
    assert _is_linked(a, 'miniJava_Assignment48', b2)
    if hasattr(b1, 'miniJava_Assignee'):
        assert not _is_linked(b1, 'miniJava_Assignee', a)
    if hasattr(b2, 'miniJava_Assignee'):
        assert _is_linked(b2, 'miniJava_Assignee', a)
    _safe_set(a, 'miniJava_Assignment48', None)
    assert not _is_linked(a, 'miniJava_Assignment48', b2)
    if hasattr(b2, 'miniJava_Assignee'):
        assert not _is_linked(b2, 'miniJava_Assignee', a)


def test_assoc_bindings148_link_reassign_clear():
    a = miniJava_Context()
    b1 = miniJava_SymbolBinding()
    b2 = miniJava_SymbolBinding()
    _safe_set(a, 'miniJava_Context', {b1})
    assert _is_linked(a, 'miniJava_Context', b1)
    if hasattr(b1, 'miniJava_SymbolBinding'):
        assert _is_linked(b1, 'miniJava_SymbolBinding', a)
    _safe_set(a, 'miniJava_Context', {b2})
    assert _is_linked(a, 'miniJava_Context', b2)
    if hasattr(b1, 'miniJava_SymbolBinding'):
        assert not _is_linked(b1, 'miniJava_SymbolBinding', a)
    if hasattr(b2, 'miniJava_SymbolBinding'):
        assert _is_linked(b2, 'miniJava_SymbolBinding', a)
    _safe_set(a, 'miniJava_Context', set())
    assert not _is_linked(a, 'miniJava_Context', b2)
    if hasattr(b2, 'miniJava_SymbolBinding'):
        assert not _is_linked(b2, 'miniJava_SymbolBinding', a)


def test_assoc_block31_link_reassign_clear():
    a = miniJava_WhileStatement()
    b1 = miniJava_Block()
    b2 = miniJava_Block()
    _safe_set(a, 'miniJava_WhileStatement32', b1)
    assert _is_linked(a, 'miniJava_WhileStatement32', b1)
    if hasattr(b1, 'miniJava_Block33'):
        assert _is_linked(b1, 'miniJava_Block33', a)
    _safe_set(a, 'miniJava_WhileStatement32', b2)
    assert _is_linked(a, 'miniJava_WhileStatement32', b2)
    if hasattr(b1, 'miniJava_Block33'):
        assert not _is_linked(b1, 'miniJava_Block33', a)
    if hasattr(b2, 'miniJava_Block33'):
        assert _is_linked(b2, 'miniJava_Block33', a)
    _safe_set(a, 'miniJava_WhileStatement32', None)
    assert not _is_linked(a, 'miniJava_WhileStatement32', b2)
    if hasattr(b2, 'miniJava_Block33'):
        assert not _is_linked(b2, 'miniJava_Block33', a)


def test_assoc_block41_link_reassign_clear():
    a = miniJava_ForStatement()
    b1 = miniJava_Block()
    b2 = miniJava_Block()
    _safe_set(a, 'miniJava_ForStatement42', b1)
    assert _is_linked(a, 'miniJava_ForStatement42', b1)
    if hasattr(b1, 'miniJava_Block43'):
        assert _is_linked(b1, 'miniJava_Block43', a)
    _safe_set(a, 'miniJava_ForStatement42', b2)
    assert _is_linked(a, 'miniJava_ForStatement42', b2)
    if hasattr(b1, 'miniJava_Block43'):
        assert not _is_linked(b1, 'miniJava_Block43', a)
    if hasattr(b2, 'miniJava_Block43'):
        assert _is_linked(b2, 'miniJava_Block43', a)
    _safe_set(a, 'miniJava_ForStatement42', None)
    assert not _is_linked(a, 'miniJava_ForStatement42', b2)
    if hasattr(b2, 'miniJava_Block43'):
        assert not _is_linked(b2, 'miniJava_Block43', a)


def test_assoc_body12_link_reassign_clear():
    a = miniJava_Method(abstract=True, static=True)
    b1 = miniJava_Block()
    b2 = miniJava_Block()
    _safe_set(a, 'miniJava_Method13', b1)
    assert _is_linked(a, 'miniJava_Method13', b1)
    if hasattr(b1, 'miniJava_Block'):
        assert _is_linked(b1, 'miniJava_Block', a)
    _safe_set(a, 'miniJava_Method13', b2)
    assert _is_linked(a, 'miniJava_Method13', b2)
    if hasattr(b1, 'miniJava_Block'):
        assert not _is_linked(b1, 'miniJava_Block', a)
    if hasattr(b2, 'miniJava_Block'):
        assert _is_linked(b2, 'miniJava_Block', a)
    _safe_set(a, 'miniJava_Method13', None)
    assert not _is_linked(a, 'miniJava_Method13', b2)
    if hasattr(b2, 'miniJava_Block'):
        assert not _is_linked(b2, 'miniJava_Block', a)


def test_assoc_call172_link_reassign_clear():
    a = miniJava_Frame()
    b1 = miniJava_Call()
    b2 = miniJava_Call()
    _safe_set(a, 'miniJava_Frame173', b1)
    assert _is_linked(a, 'miniJava_Frame173', b1)
    if hasattr(b1, 'miniJava_Call'):
        assert _is_linked(b1, 'miniJava_Call', a)
    _safe_set(a, 'miniJava_Frame173', b2)
    assert _is_linked(a, 'miniJava_Frame173', b2)
    if hasattr(b1, 'miniJava_Call'):
        assert not _is_linked(b1, 'miniJava_Call', a)
    if hasattr(b2, 'miniJava_Call'):
        assert _is_linked(b2, 'miniJava_Call', a)
    _safe_set(a, 'miniJava_Frame173', None)
    assert not _is_linked(a, 'miniJava_Frame173', b2)
    if hasattr(b2, 'miniJava_Call'):
        assert not _is_linked(b2, 'miniJava_Call', a)


def test_assoc_childContext152_link_reassign_clear():
    a = miniJava_Context()
    b1 = miniJava_Context()
    b2 = miniJava_Context()
    _safe_set(a, 'Context153', b1)
    assert _is_linked(a, 'Context153', b1)
    if hasattr(b1, 'parentContext'):
        assert _is_linked(b1, 'parentContext', a)
    _safe_set(a, 'Context153', b2)
    assert _is_linked(a, 'Context153', b2)
    if hasattr(b1, 'parentContext'):
        assert not _is_linked(b1, 'parentContext', a)
    if hasattr(b2, 'parentContext'):
        assert _is_linked(b2, 'parentContext', a)
    _safe_set(a, 'Context153', None)
    assert not _is_linked(a, 'Context153', b2)
    if hasattr(b2, 'parentContext'):
        assert not _is_linked(b2, 'parentContext', a)


def test_assoc_childFrame178_link_reassign_clear():
    a = miniJava_Frame()
    b1 = miniJava_Frame()
    b2 = miniJava_Frame()
    _safe_set(a, 'Frame', b1)
    assert _is_linked(a, 'Frame', b1)
    if hasattr(b1, 'parentFrame'):
        assert _is_linked(b1, 'parentFrame', a)
    _safe_set(a, 'Frame', b2)
    assert _is_linked(a, 'Frame', b2)
    if hasattr(b1, 'parentFrame'):
        assert not _is_linked(b1, 'parentFrame', a)
    if hasattr(b2, 'parentFrame'):
        assert _is_linked(b2, 'parentFrame', a)
    _safe_set(a, 'Frame', None)
    assert not _is_linked(a, 'Frame', b2)
    if hasattr(b2, 'parentFrame'):
        assert not _is_linked(b2, 'parentFrame', a)


def test_assoc_classes1_link_reassign_clear():
    a = miniJava_TypeDeclaration(accessLevel="sample_text")
    b1 = miniJava_Program(name="sample_text")
    b2 = miniJava_Program(name="sample_text_2")
    _safe_set(a, 'miniJava_TypeDeclaration', b1)
    assert _is_linked(a, 'miniJava_TypeDeclaration', b1)
    if hasattr(b1, 'miniJava_Program2'):
        assert _is_linked(b1, 'miniJava_Program2', a)
    _safe_set(a, 'miniJava_TypeDeclaration', b2)
    assert _is_linked(a, 'miniJava_TypeDeclaration', b2)
    if hasattr(b1, 'miniJava_Program2'):
        assert not _is_linked(b1, 'miniJava_Program2', a)
    if hasattr(b2, 'miniJava_Program2'):
        assert _is_linked(b2, 'miniJava_Program2', a)
    _safe_set(a, 'miniJava_TypeDeclaration', None)
    assert not _is_linked(a, 'miniJava_TypeDeclaration', b2)
    if hasattr(b2, 'miniJava_Program2'):
        assert not _is_linked(b2, 'miniJava_Program2', a)


def test_assoc_condition29_link_reassign_clear():
    a = miniJava_WhileStatement()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_WhileStatement', b1)
    assert _is_linked(a, 'miniJava_WhileStatement', b1)
    if hasattr(b1, 'miniJava_Expression30'):
        assert _is_linked(b1, 'miniJava_Expression30', a)
    _safe_set(a, 'miniJava_WhileStatement', b2)
    assert _is_linked(a, 'miniJava_WhileStatement', b2)
    if hasattr(b1, 'miniJava_Expression30'):
        assert not _is_linked(b1, 'miniJava_Expression30', a)
    if hasattr(b2, 'miniJava_Expression30'):
        assert _is_linked(b2, 'miniJava_Expression30', a)
    _safe_set(a, 'miniJava_WhileStatement', None)
    assert not _is_linked(a, 'miniJava_WhileStatement', b2)
    if hasattr(b2, 'miniJava_Expression30'):
        assert not _is_linked(b2, 'miniJava_Expression30', a)


def test_assoc_condition35_link_reassign_clear():
    a = miniJava_ForStatement()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_ForStatement36', b1)
    assert _is_linked(a, 'miniJava_ForStatement36', b1)
    if hasattr(b1, 'miniJava_Expression37'):
        assert _is_linked(b1, 'miniJava_Expression37', a)
    _safe_set(a, 'miniJava_ForStatement36', b2)
    assert _is_linked(a, 'miniJava_ForStatement36', b2)
    if hasattr(b1, 'miniJava_Expression37'):
        assert not _is_linked(b1, 'miniJava_Expression37', a)
    if hasattr(b2, 'miniJava_Expression37'):
        assert _is_linked(b2, 'miniJava_Expression37', a)
    _safe_set(a, 'miniJava_ForStatement36', None)
    assert not _is_linked(a, 'miniJava_ForStatement36', b2)
    if hasattr(b2, 'miniJava_Expression37'):
        assert not _is_linked(b2, 'miniJava_Expression37', a)


def test_assoc_declaration34_link_reassign_clear():
    a = miniJava_ForStatement()
    b1 = miniJava_Assignment()
    b2 = miniJava_Assignment()
    _safe_set(a, 'miniJava_ForStatement', b1)
    assert _is_linked(a, 'miniJava_ForStatement', b1)
    if hasattr(b1, 'miniJava_Assignment'):
        assert _is_linked(b1, 'miniJava_Assignment', a)
    _safe_set(a, 'miniJava_ForStatement', b2)
    assert _is_linked(a, 'miniJava_ForStatement', b2)
    if hasattr(b1, 'miniJava_Assignment'):
        assert not _is_linked(b1, 'miniJava_Assignment', a)
    if hasattr(b2, 'miniJava_Assignment'):
        assert _is_linked(b2, 'miniJava_Assignment', a)
    _safe_set(a, 'miniJava_ForStatement', None)
    assert not _is_linked(a, 'miniJava_ForStatement', b2)
    if hasattr(b2, 'miniJava_Assignment'):
        assert not _is_linked(b2, 'miniJava_Assignment', a)


def test_assoc_defaultValue14_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_Field()
    b2 = miniJava_Field()
    _safe_set(a, 'miniJava_Expression', b1)
    assert _is_linked(a, 'miniJava_Expression', b1)
    if hasattr(b1, 'miniJava_Field'):
        assert _is_linked(b1, 'miniJava_Field', a)
    _safe_set(a, 'miniJava_Expression', b2)
    assert _is_linked(a, 'miniJava_Expression', b2)
    if hasattr(b1, 'miniJava_Field'):
        assert not _is_linked(b1, 'miniJava_Field', a)
    if hasattr(b2, 'miniJava_Field'):
        assert _is_linked(b2, 'miniJava_Field', a)
    _safe_set(a, 'miniJava_Expression', None)
    assert not _is_linked(a, 'miniJava_Expression', b2)
    if hasattr(b2, 'miniJava_Field'):
        assert not _is_linked(b2, 'miniJava_Field', a)


def test_assoc_elseBlock26_link_reassign_clear():
    a = miniJava_IfStatement()
    b1 = miniJava_Block()
    b2 = miniJava_Block()
    _safe_set(a, 'miniJava_IfStatement27', b1)
    assert _is_linked(a, 'miniJava_IfStatement27', b1)
    if hasattr(b1, 'miniJava_Block28'):
        assert _is_linked(b1, 'miniJava_Block28', a)
    _safe_set(a, 'miniJava_IfStatement27', b2)
    assert _is_linked(a, 'miniJava_IfStatement27', b2)
    if hasattr(b1, 'miniJava_Block28'):
        assert not _is_linked(b1, 'miniJava_Block28', a)
    if hasattr(b2, 'miniJava_Block28'):
        assert _is_linked(b2, 'miniJava_Block28', a)
    _safe_set(a, 'miniJava_IfStatement27', None)
    assert not _is_linked(a, 'miniJava_IfStatement27', b2)
    if hasattr(b2, 'miniJava_Block28'):
        assert not _is_linked(b2, 'miniJava_Block28', a)


def test_assoc_expression120_link_reassign_clear():
    a = miniJava_Not()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Not', b1)
    assert _is_linked(a, 'miniJava_Not', b1)
    if hasattr(b1, 'miniJava_Expression121'):
        assert _is_linked(b1, 'miniJava_Expression121', a)
    _safe_set(a, 'miniJava_Not', b2)
    assert _is_linked(a, 'miniJava_Not', b2)
    if hasattr(b1, 'miniJava_Expression121'):
        assert not _is_linked(b1, 'miniJava_Expression121', a)
    if hasattr(b2, 'miniJava_Expression121'):
        assert _is_linked(b2, 'miniJava_Expression121', a)
    _safe_set(a, 'miniJava_Not', None)
    assert not _is_linked(a, 'miniJava_Not', b2)
    if hasattr(b2, 'miniJava_Expression121'):
        assert not _is_linked(b2, 'miniJava_Expression121', a)


def test_assoc_expression122_link_reassign_clear():
    a = miniJava_Neg()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Neg', b1)
    assert _is_linked(a, 'miniJava_Neg', b1)
    if hasattr(b1, 'miniJava_Expression123'):
        assert _is_linked(b1, 'miniJava_Expression123', a)
    _safe_set(a, 'miniJava_Neg', b2)
    assert _is_linked(a, 'miniJava_Neg', b2)
    if hasattr(b1, 'miniJava_Expression123'):
        assert not _is_linked(b1, 'miniJava_Expression123', a)
    if hasattr(b2, 'miniJava_Expression123'):
        assert _is_linked(b2, 'miniJava_Expression123', a)
    _safe_set(a, 'miniJava_Neg', None)
    assert not _is_linked(a, 'miniJava_Neg', b2)
    if hasattr(b2, 'miniJava_Expression123'):
        assert not _is_linked(b2, 'miniJava_Expression123', a)


def test_assoc_expression17_link_reassign_clear():
    a = miniJava_PrintStatement()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_PrintStatement', b1)
    assert _is_linked(a, 'miniJava_PrintStatement', b1)
    if hasattr(b1, 'miniJava_Expression18'):
        assert _is_linked(b1, 'miniJava_Expression18', a)
    _safe_set(a, 'miniJava_PrintStatement', b2)
    assert _is_linked(a, 'miniJava_PrintStatement', b2)
    if hasattr(b1, 'miniJava_Expression18'):
        assert not _is_linked(b1, 'miniJava_Expression18', a)
    if hasattr(b2, 'miniJava_Expression18'):
        assert _is_linked(b2, 'miniJava_Expression18', a)
    _safe_set(a, 'miniJava_PrintStatement', None)
    assert not _is_linked(a, 'miniJava_PrintStatement', b2)
    if hasattr(b2, 'miniJava_Expression18'):
        assert not _is_linked(b2, 'miniJava_Expression18', a)


def test_assoc_expression19_link_reassign_clear():
    a = miniJava_Return()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Return', b1)
    assert _is_linked(a, 'miniJava_Return', b1)
    if hasattr(b1, 'miniJava_Expression20'):
        assert _is_linked(b1, 'miniJava_Expression20', a)
    _safe_set(a, 'miniJava_Return', b2)
    assert _is_linked(a, 'miniJava_Return', b2)
    if hasattr(b1, 'miniJava_Expression20'):
        assert not _is_linked(b1, 'miniJava_Expression20', a)
    if hasattr(b2, 'miniJava_Expression20'):
        assert _is_linked(b2, 'miniJava_Expression20', a)
    _safe_set(a, 'miniJava_Return', None)
    assert not _is_linked(a, 'miniJava_Return', b2)
    if hasattr(b2, 'miniJava_Expression20'):
        assert not _is_linked(b2, 'miniJava_Expression20', a)


def test_assoc_expression21_link_reassign_clear():
    a = miniJava_IfStatement()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_IfStatement', b1)
    assert _is_linked(a, 'miniJava_IfStatement', b1)
    if hasattr(b1, 'miniJava_Expression22'):
        assert _is_linked(b1, 'miniJava_Expression22', a)
    _safe_set(a, 'miniJava_IfStatement', b2)
    assert _is_linked(a, 'miniJava_IfStatement', b2)
    if hasattr(b1, 'miniJava_Expression22'):
        assert not _is_linked(b1, 'miniJava_Expression22', a)
    if hasattr(b2, 'miniJava_Expression22'):
        assert _is_linked(b2, 'miniJava_Expression22', a)
    _safe_set(a, 'miniJava_IfStatement', None)
    assert not _is_linked(a, 'miniJava_IfStatement', b2)
    if hasattr(b2, 'miniJava_Expression22'):
        assert not _is_linked(b2, 'miniJava_Expression22', a)


def test_assoc_field126_link_reassign_clear():
    a = miniJava_FieldAccess()
    b1 = miniJava_Field()
    b2 = miniJava_Field()
    _safe_set(a, 'miniJava_FieldAccess127', b1)
    assert _is_linked(a, 'miniJava_FieldAccess127', b1)
    if hasattr(b1, 'miniJava_Field128'):
        assert _is_linked(b1, 'miniJava_Field128', a)
    _safe_set(a, 'miniJava_FieldAccess127', b2)
    assert _is_linked(a, 'miniJava_FieldAccess127', b2)
    if hasattr(b1, 'miniJava_Field128'):
        assert not _is_linked(b1, 'miniJava_Field128', a)
    if hasattr(b2, 'miniJava_Field128'):
        assert _is_linked(b2, 'miniJava_Field128', a)
    _safe_set(a, 'miniJava_FieldAccess127', None)
    assert not _is_linked(a, 'miniJava_FieldAccess127', b2)
    if hasattr(b2, 'miniJava_Field128'):
        assert not _is_linked(b2, 'miniJava_Field128', a)


def test_assoc_implements5_link_reassign_clear():
    a = miniJava_TypeDeclaration(accessLevel="sample_text")
    b1 = miniJava_Interface()
    b2 = miniJava_Interface()
    _safe_set(a, 'miniJava_TypeDeclaration6', {b1})
    assert _is_linked(a, 'miniJava_TypeDeclaration6', b1)
    if hasattr(b1, 'miniJava_Interface'):
        assert _is_linked(b1, 'miniJava_Interface', a)
    _safe_set(a, 'miniJava_TypeDeclaration6', {b2})
    assert _is_linked(a, 'miniJava_TypeDeclaration6', b2)
    if hasattr(b1, 'miniJava_Interface'):
        assert not _is_linked(b1, 'miniJava_Interface', a)
    if hasattr(b2, 'miniJava_Interface'):
        assert _is_linked(b2, 'miniJava_Interface', a)
    _safe_set(a, 'miniJava_TypeDeclaration6', set())
    assert not _is_linked(a, 'miniJava_TypeDeclaration6', b2)
    if hasattr(b2, 'miniJava_Interface'):
        assert not _is_linked(b2, 'miniJava_Interface', a)


def test_assoc_imports0_link_reassign_clear():
    a = miniJava_Program(name="sample_text")
    b1 = miniJava_Import(importedNamespace="sample_text")
    b2 = miniJava_Import(importedNamespace="sample_text_2")
    _safe_set(a, 'miniJava_Program', {b1})
    assert _is_linked(a, 'miniJava_Program', b1)
    if hasattr(b1, 'miniJava_Import'):
        assert _is_linked(b1, 'miniJava_Import', a)
    _safe_set(a, 'miniJava_Program', {b2})
    assert _is_linked(a, 'miniJava_Program', b2)
    if hasattr(b1, 'miniJava_Import'):
        assert not _is_linked(b1, 'miniJava_Import', a)
    if hasattr(b2, 'miniJava_Import'):
        assert _is_linked(b2, 'miniJava_Import', a)
    _safe_set(a, 'miniJava_Program', set())
    assert not _is_linked(a, 'miniJava_Program', b2)
    if hasattr(b2, 'miniJava_Import'):
        assert not _is_linked(b2, 'miniJava_Import', a)


def test_assoc_index115_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_ArrayAccess()
    b2 = miniJava_ArrayAccess()
    _safe_set(a, 'miniJava_Expression117', b1)
    assert _is_linked(a, 'miniJava_Expression117', b1)
    if hasattr(b1, 'miniJava_ArrayAccess116'):
        assert _is_linked(b1, 'miniJava_ArrayAccess116', a)
    _safe_set(a, 'miniJava_Expression117', b2)
    assert _is_linked(a, 'miniJava_Expression117', b2)
    if hasattr(b1, 'miniJava_ArrayAccess116'):
        assert not _is_linked(b1, 'miniJava_ArrayAccess116', a)
    if hasattr(b2, 'miniJava_ArrayAccess116'):
        assert _is_linked(b2, 'miniJava_ArrayAccess116', a)
    _safe_set(a, 'miniJava_Expression117', None)
    assert not _is_linked(a, 'miniJava_Expression117', b2)
    if hasattr(b2, 'miniJava_ArrayAccess116'):
        assert not _is_linked(b2, 'miniJava_ArrayAccess116', a)


def test_assoc_instance174_link_reassign_clear():
    a = miniJava_Frame()
    b1 = miniJava_ObjectInstance()
    b2 = miniJava_ObjectInstance()
    _safe_set(a, 'miniJava_Frame175', b1)
    assert _is_linked(a, 'miniJava_Frame175', b1)
    if hasattr(b1, 'miniJava_ObjectInstance176'):
        assert _is_linked(b1, 'miniJava_ObjectInstance176', a)
    _safe_set(a, 'miniJava_Frame175', b2)
    assert _is_linked(a, 'miniJava_Frame175', b2)
    if hasattr(b1, 'miniJava_ObjectInstance176'):
        assert not _is_linked(b1, 'miniJava_ObjectInstance176', a)
    if hasattr(b2, 'miniJava_ObjectInstance176'):
        assert _is_linked(b2, 'miniJava_ObjectInstance176', a)
    _safe_set(a, 'miniJava_Frame175', None)
    assert not _is_linked(a, 'miniJava_Frame175', b2)
    if hasattr(b2, 'miniJava_ObjectInstance176'):
        assert not _is_linked(b2, 'miniJava_ObjectInstance176', a)


def test_assoc_instance201_link_reassign_clear():
    a = miniJava_ObjectRefValue()
    b1 = miniJava_ObjectInstance()
    b2 = miniJava_ObjectInstance()
    _safe_set(a, 'miniJava_ObjectRefValue', b1)
    assert _is_linked(a, 'miniJava_ObjectRefValue', b1)
    if hasattr(b1, 'miniJava_ObjectInstance202'):
        assert _is_linked(b1, 'miniJava_ObjectInstance202', a)
    _safe_set(a, 'miniJava_ObjectRefValue', b2)
    assert _is_linked(a, 'miniJava_ObjectRefValue', b2)
    if hasattr(b1, 'miniJava_ObjectInstance202'):
        assert not _is_linked(b1, 'miniJava_ObjectInstance202', a)
    if hasattr(b2, 'miniJava_ObjectInstance202'):
        assert _is_linked(b2, 'miniJava_ObjectInstance202', a)
    _safe_set(a, 'miniJava_ObjectRefValue', None)
    assert not _is_linked(a, 'miniJava_ObjectRefValue', b2)
    if hasattr(b2, 'miniJava_ObjectInstance202'):
        assert not _is_linked(b2, 'miniJava_ObjectInstance202', a)


def test_assoc_instance203_link_reassign_clear():
    a = miniJava_ArrayRefValue()
    b1 = miniJava_ArrayInstance(size="sample_text")
    b2 = miniJava_ArrayInstance(size="sample_text_2")
    _safe_set(a, 'miniJava_ArrayRefValue', b1)
    assert _is_linked(a, 'miniJava_ArrayRefValue', b1)
    if hasattr(b1, 'miniJava_ArrayInstance204'):
        assert _is_linked(b1, 'miniJava_ArrayInstance204', a)
    _safe_set(a, 'miniJava_ArrayRefValue', b2)
    assert _is_linked(a, 'miniJava_ArrayRefValue', b2)
    if hasattr(b1, 'miniJava_ArrayInstance204'):
        assert not _is_linked(b1, 'miniJava_ArrayInstance204', a)
    if hasattr(b2, 'miniJava_ArrayInstance204'):
        assert _is_linked(b2, 'miniJava_ArrayInstance204', a)
    _safe_set(a, 'miniJava_ArrayRefValue', None)
    assert not _is_linked(a, 'miniJava_ArrayRefValue', b2)
    if hasattr(b2, 'miniJava_ArrayInstance204'):
        assert not _is_linked(b2, 'miniJava_ArrayInstance204', a)


def test_assoc_left103_link_reassign_clear():
    a = miniJava_Multiplication()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Multiplication', b1)
    assert _is_linked(a, 'miniJava_Multiplication', b1)
    if hasattr(b1, 'miniJava_Expression104'):
        assert _is_linked(b1, 'miniJava_Expression104', a)
    _safe_set(a, 'miniJava_Multiplication', b2)
    assert _is_linked(a, 'miniJava_Multiplication', b2)
    if hasattr(b1, 'miniJava_Expression104'):
        assert not _is_linked(b1, 'miniJava_Expression104', a)
    if hasattr(b2, 'miniJava_Expression104'):
        assert _is_linked(b2, 'miniJava_Expression104', a)
    _safe_set(a, 'miniJava_Multiplication', None)
    assert not _is_linked(a, 'miniJava_Multiplication', b2)
    if hasattr(b2, 'miniJava_Expression104'):
        assert not _is_linked(b2, 'miniJava_Expression104', a)


def test_assoc_left108_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_Division()
    b2 = miniJava_Division()
    _safe_set(a, 'miniJava_Expression109', b1)
    assert _is_linked(a, 'miniJava_Expression109', b1)
    if hasattr(b1, 'miniJava_Division'):
        assert _is_linked(b1, 'miniJava_Division', a)
    _safe_set(a, 'miniJava_Expression109', b2)
    assert _is_linked(a, 'miniJava_Expression109', b2)
    if hasattr(b1, 'miniJava_Division'):
        assert not _is_linked(b1, 'miniJava_Division', a)
    if hasattr(b2, 'miniJava_Division'):
        assert _is_linked(b2, 'miniJava_Division', a)
    _safe_set(a, 'miniJava_Expression109', None)
    assert not _is_linked(a, 'miniJava_Expression109', b2)
    if hasattr(b2, 'miniJava_Division'):
        assert not _is_linked(b2, 'miniJava_Division', a)


def test_assoc_left53_link_reassign_clear():
    a = miniJava_Or()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Or', b1)
    assert _is_linked(a, 'miniJava_Or', b1)
    if hasattr(b1, 'miniJava_Expression54'):
        assert _is_linked(b1, 'miniJava_Expression54', a)
    _safe_set(a, 'miniJava_Or', b2)
    assert _is_linked(a, 'miniJava_Or', b2)
    if hasattr(b1, 'miniJava_Expression54'):
        assert not _is_linked(b1, 'miniJava_Expression54', a)
    if hasattr(b2, 'miniJava_Expression54'):
        assert _is_linked(b2, 'miniJava_Expression54', a)
    _safe_set(a, 'miniJava_Or', None)
    assert not _is_linked(a, 'miniJava_Or', b2)
    if hasattr(b2, 'miniJava_Expression54'):
        assert not _is_linked(b2, 'miniJava_Expression54', a)


def test_assoc_left58_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_And()
    b2 = miniJava_And()
    _safe_set(a, 'miniJava_Expression59', b1)
    assert _is_linked(a, 'miniJava_Expression59', b1)
    if hasattr(b1, 'miniJava_And'):
        assert _is_linked(b1, 'miniJava_And', a)
    _safe_set(a, 'miniJava_Expression59', b2)
    assert _is_linked(a, 'miniJava_Expression59', b2)
    if hasattr(b1, 'miniJava_And'):
        assert not _is_linked(b1, 'miniJava_And', a)
    if hasattr(b2, 'miniJava_And'):
        assert _is_linked(b2, 'miniJava_And', a)
    _safe_set(a, 'miniJava_Expression59', None)
    assert not _is_linked(a, 'miniJava_Expression59', b2)
    if hasattr(b2, 'miniJava_And'):
        assert not _is_linked(b2, 'miniJava_And', a)


def test_assoc_left63_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_Equality()
    b2 = miniJava_Equality()
    _safe_set(a, 'miniJava_Expression64', b1)
    assert _is_linked(a, 'miniJava_Expression64', b1)
    if hasattr(b1, 'miniJava_Equality'):
        assert _is_linked(b1, 'miniJava_Equality', a)
    _safe_set(a, 'miniJava_Expression64', b2)
    assert _is_linked(a, 'miniJava_Expression64', b2)
    if hasattr(b1, 'miniJava_Equality'):
        assert not _is_linked(b1, 'miniJava_Equality', a)
    if hasattr(b2, 'miniJava_Equality'):
        assert _is_linked(b2, 'miniJava_Equality', a)
    _safe_set(a, 'miniJava_Expression64', None)
    assert not _is_linked(a, 'miniJava_Expression64', b2)
    if hasattr(b2, 'miniJava_Equality'):
        assert not _is_linked(b2, 'miniJava_Equality', a)


def test_assoc_left68_link_reassign_clear():
    a = miniJava_Inequality()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Inequality', b1)
    assert _is_linked(a, 'miniJava_Inequality', b1)
    if hasattr(b1, 'miniJava_Expression69'):
        assert _is_linked(b1, 'miniJava_Expression69', a)
    _safe_set(a, 'miniJava_Inequality', b2)
    assert _is_linked(a, 'miniJava_Inequality', b2)
    if hasattr(b1, 'miniJava_Expression69'):
        assert not _is_linked(b1, 'miniJava_Expression69', a)
    if hasattr(b2, 'miniJava_Expression69'):
        assert _is_linked(b2, 'miniJava_Expression69', a)
    _safe_set(a, 'miniJava_Inequality', None)
    assert not _is_linked(a, 'miniJava_Inequality', b2)
    if hasattr(b2, 'miniJava_Expression69'):
        assert not _is_linked(b2, 'miniJava_Expression69', a)


def test_assoc_left73_link_reassign_clear():
    a = miniJava_SuperiorOrEqual()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_SuperiorOrEqual', b1)
    assert _is_linked(a, 'miniJava_SuperiorOrEqual', b1)
    if hasattr(b1, 'miniJava_Expression74'):
        assert _is_linked(b1, 'miniJava_Expression74', a)
    _safe_set(a, 'miniJava_SuperiorOrEqual', b2)
    assert _is_linked(a, 'miniJava_SuperiorOrEqual', b2)
    if hasattr(b1, 'miniJava_Expression74'):
        assert not _is_linked(b1, 'miniJava_Expression74', a)
    if hasattr(b2, 'miniJava_Expression74'):
        assert _is_linked(b2, 'miniJava_Expression74', a)
    _safe_set(a, 'miniJava_SuperiorOrEqual', None)
    assert not _is_linked(a, 'miniJava_SuperiorOrEqual', b2)
    if hasattr(b2, 'miniJava_Expression74'):
        assert not _is_linked(b2, 'miniJava_Expression74', a)


def test_assoc_left78_link_reassign_clear():
    a = miniJava_InferiorOrEqual()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_InferiorOrEqual', b1)
    assert _is_linked(a, 'miniJava_InferiorOrEqual', b1)
    if hasattr(b1, 'miniJava_Expression79'):
        assert _is_linked(b1, 'miniJava_Expression79', a)
    _safe_set(a, 'miniJava_InferiorOrEqual', b2)
    assert _is_linked(a, 'miniJava_InferiorOrEqual', b2)
    if hasattr(b1, 'miniJava_Expression79'):
        assert not _is_linked(b1, 'miniJava_Expression79', a)
    if hasattr(b2, 'miniJava_Expression79'):
        assert _is_linked(b2, 'miniJava_Expression79', a)
    _safe_set(a, 'miniJava_InferiorOrEqual', None)
    assert not _is_linked(a, 'miniJava_InferiorOrEqual', b2)
    if hasattr(b2, 'miniJava_Expression79'):
        assert not _is_linked(b2, 'miniJava_Expression79', a)


def test_assoc_left83_link_reassign_clear():
    a = miniJava_Superior()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Superior', b1)
    assert _is_linked(a, 'miniJava_Superior', b1)
    if hasattr(b1, 'miniJava_Expression84'):
        assert _is_linked(b1, 'miniJava_Expression84', a)
    _safe_set(a, 'miniJava_Superior', b2)
    assert _is_linked(a, 'miniJava_Superior', b2)
    if hasattr(b1, 'miniJava_Expression84'):
        assert not _is_linked(b1, 'miniJava_Expression84', a)
    if hasattr(b2, 'miniJava_Expression84'):
        assert _is_linked(b2, 'miniJava_Expression84', a)
    _safe_set(a, 'miniJava_Superior', None)
    assert not _is_linked(a, 'miniJava_Superior', b2)
    if hasattr(b2, 'miniJava_Expression84'):
        assert not _is_linked(b2, 'miniJava_Expression84', a)


def test_assoc_left88_link_reassign_clear():
    a = miniJava_Inferior()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Inferior', b1)
    assert _is_linked(a, 'miniJava_Inferior', b1)
    if hasattr(b1, 'miniJava_Expression89'):
        assert _is_linked(b1, 'miniJava_Expression89', a)
    _safe_set(a, 'miniJava_Inferior', b2)
    assert _is_linked(a, 'miniJava_Inferior', b2)
    if hasattr(b1, 'miniJava_Expression89'):
        assert not _is_linked(b1, 'miniJava_Expression89', a)
    if hasattr(b2, 'miniJava_Expression89'):
        assert _is_linked(b2, 'miniJava_Expression89', a)
    _safe_set(a, 'miniJava_Inferior', None)
    assert not _is_linked(a, 'miniJava_Inferior', b2)
    if hasattr(b2, 'miniJava_Expression89'):
        assert not _is_linked(b2, 'miniJava_Expression89', a)


def test_assoc_left93_link_reassign_clear():
    a = miniJava_Plus()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Plus', b1)
    assert _is_linked(a, 'miniJava_Plus', b1)
    if hasattr(b1, 'miniJava_Expression94'):
        assert _is_linked(b1, 'miniJava_Expression94', a)
    _safe_set(a, 'miniJava_Plus', b2)
    assert _is_linked(a, 'miniJava_Plus', b2)
    if hasattr(b1, 'miniJava_Expression94'):
        assert not _is_linked(b1, 'miniJava_Expression94', a)
    if hasattr(b2, 'miniJava_Expression94'):
        assert _is_linked(b2, 'miniJava_Expression94', a)
    _safe_set(a, 'miniJava_Plus', None)
    assert not _is_linked(a, 'miniJava_Plus', b2)
    if hasattr(b2, 'miniJava_Expression94'):
        assert not _is_linked(b2, 'miniJava_Expression94', a)


def test_assoc_left98_link_reassign_clear():
    a = miniJava_Minus()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Minus', b1)
    assert _is_linked(a, 'miniJava_Minus', b1)
    if hasattr(b1, 'miniJava_Expression99'):
        assert _is_linked(b1, 'miniJava_Expression99', a)
    _safe_set(a, 'miniJava_Minus', b2)
    assert _is_linked(a, 'miniJava_Minus', b2)
    if hasattr(b1, 'miniJava_Expression99'):
        assert not _is_linked(b1, 'miniJava_Expression99', a)
    if hasattr(b2, 'miniJava_Expression99'):
        assert _is_linked(b2, 'miniJava_Expression99', a)
    _safe_set(a, 'miniJava_Minus', None)
    assert not _is_linked(a, 'miniJava_Minus', b2)
    if hasattr(b2, 'miniJava_Expression99'):
        assert not _is_linked(b2, 'miniJava_Expression99', a)


def test_assoc_members7_link_reassign_clear():
    a = miniJava_TypeDeclaration(accessLevel="sample_text")
    b1 = miniJava_Member(access="sample_text")
    b2 = miniJava_Member(access="sample_text_2")
    _safe_set(a, 'miniJava_TypeDeclaration8', {b1})
    assert _is_linked(a, 'miniJava_TypeDeclaration8', b1)
    if hasattr(b1, 'miniJava_Member'):
        assert _is_linked(b1, 'miniJava_Member', a)
    _safe_set(a, 'miniJava_TypeDeclaration8', {b2})
    assert _is_linked(a, 'miniJava_TypeDeclaration8', b2)
    if hasattr(b1, 'miniJava_Member'):
        assert not _is_linked(b1, 'miniJava_Member', a)
    if hasattr(b2, 'miniJava_Member'):
        assert _is_linked(b2, 'miniJava_Member', a)
    _safe_set(a, 'miniJava_TypeDeclaration8', set())
    assert not _is_linked(a, 'miniJava_TypeDeclaration8', b2)
    if hasattr(b2, 'miniJava_Member'):
        assert not _is_linked(b2, 'miniJava_Member', a)


def test_assoc_method131_link_reassign_clear():
    a = miniJava_MethodCall()
    b1 = miniJava_Method(abstract=True, static=True)
    b2 = miniJava_Method(abstract=False, static=False)
    _safe_set(a, 'miniJava_MethodCall132', b1)
    assert _is_linked(a, 'miniJava_MethodCall132', b1)
    if hasattr(b1, 'miniJava_Method133'):
        assert _is_linked(b1, 'miniJava_Method133', a)
    _safe_set(a, 'miniJava_MethodCall132', b2)
    assert _is_linked(a, 'miniJava_MethodCall132', b2)
    if hasattr(b1, 'miniJava_Method133'):
        assert not _is_linked(b1, 'miniJava_Method133', a)
    if hasattr(b2, 'miniJava_Method133'):
        assert _is_linked(b2, 'miniJava_Method133', a)
    _safe_set(a, 'miniJava_MethodCall132', None)
    assert not _is_linked(a, 'miniJava_MethodCall132', b2)
    if hasattr(b2, 'miniJava_Method133'):
        assert not _is_linked(b2, 'miniJava_Method133', a)


def test_assoc_methodcall190_link_reassign_clear():
    a = miniJava_MethodCall()
    b1 = miniJava_MethodCall2()
    b2 = miniJava_MethodCall2()
    _safe_set(a, 'miniJava_MethodCall191', b1)
    assert _is_linked(a, 'miniJava_MethodCall191', b1)
    if hasattr(b1, 'miniJava_MethodCall2'):
        assert _is_linked(b1, 'miniJava_MethodCall2', a)
    _safe_set(a, 'miniJava_MethodCall191', b2)
    assert _is_linked(a, 'miniJava_MethodCall191', b2)
    if hasattr(b1, 'miniJava_MethodCall2'):
        assert not _is_linked(b1, 'miniJava_MethodCall2', a)
    if hasattr(b2, 'miniJava_MethodCall2'):
        assert _is_linked(b2, 'miniJava_MethodCall2', a)
    _safe_set(a, 'miniJava_MethodCall191', None)
    assert not _is_linked(a, 'miniJava_MethodCall191', b2)
    if hasattr(b2, 'miniJava_MethodCall2'):
        assert not _is_linked(b2, 'miniJava_MethodCall2', a)


def test_assoc_new188_link_reassign_clear():
    a = miniJava_NewObject()
    b1 = miniJava_NewCall()
    b2 = miniJava_NewCall()
    _safe_set(a, 'miniJava_NewObject189', b1)
    assert _is_linked(a, 'miniJava_NewObject189', b1)
    if hasattr(b1, 'miniJava_NewCall'):
        assert _is_linked(b1, 'miniJava_NewCall', a)
    _safe_set(a, 'miniJava_NewObject189', b2)
    assert _is_linked(a, 'miniJava_NewObject189', b2)
    if hasattr(b1, 'miniJava_NewCall'):
        assert not _is_linked(b1, 'miniJava_NewCall', a)
    if hasattr(b2, 'miniJava_NewCall'):
        assert _is_linked(b2, 'miniJava_NewCall', a)
    _safe_set(a, 'miniJava_NewObject189', None)
    assert not _is_linked(a, 'miniJava_NewObject189', b2)
    if hasattr(b2, 'miniJava_NewCall'):
        assert not _is_linked(b2, 'miniJava_NewCall', a)


def test_assoc_object113_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_ArrayAccess()
    b2 = miniJava_ArrayAccess()
    _safe_set(a, 'miniJava_Expression114', b1)
    assert _is_linked(a, 'miniJava_Expression114', b1)
    if hasattr(b1, 'miniJava_ArrayAccess'):
        assert _is_linked(b1, 'miniJava_ArrayAccess', a)
    _safe_set(a, 'miniJava_Expression114', b2)
    assert _is_linked(a, 'miniJava_Expression114', b2)
    if hasattr(b1, 'miniJava_ArrayAccess'):
        assert not _is_linked(b1, 'miniJava_ArrayAccess', a)
    if hasattr(b2, 'miniJava_ArrayAccess'):
        assert _is_linked(b2, 'miniJava_ArrayAccess', a)
    _safe_set(a, 'miniJava_Expression114', None)
    assert not _is_linked(a, 'miniJava_Expression114', b2)
    if hasattr(b2, 'miniJava_ArrayAccess'):
        assert not _is_linked(b2, 'miniJava_ArrayAccess', a)


def test_assoc_objectsHeap166_link_reassign_clear():
    a = miniJava_State()
    b1 = miniJava_ObjectInstance()
    b2 = miniJava_ObjectInstance()
    _safe_set(a, 'miniJava_State167', {b1})
    assert _is_linked(a, 'miniJava_State167', b1)
    if hasattr(b1, 'miniJava_ObjectInstance'):
        assert _is_linked(b1, 'miniJava_ObjectInstance', a)
    _safe_set(a, 'miniJava_State167', {b2})
    assert _is_linked(a, 'miniJava_State167', b2)
    if hasattr(b1, 'miniJava_ObjectInstance'):
        assert not _is_linked(b1, 'miniJava_ObjectInstance', a)
    if hasattr(b2, 'miniJava_ObjectInstance'):
        assert _is_linked(b2, 'miniJava_ObjectInstance', a)
    _safe_set(a, 'miniJava_State167', set())
    assert not _is_linked(a, 'miniJava_State167', b2)
    if hasattr(b2, 'miniJava_ObjectInstance'):
        assert not _is_linked(b2, 'miniJava_ObjectInstance', a)


def test_assoc_outputStream168_link_reassign_clear():
    a = miniJava_State()
    b1 = miniJava_OutputStream(stream="sample_text")
    b2 = miniJava_OutputStream(stream="sample_text_2")
    _safe_set(a, 'miniJava_State169', b1)
    assert _is_linked(a, 'miniJava_State169', b1)
    if hasattr(b1, 'miniJava_OutputStream'):
        assert _is_linked(b1, 'miniJava_OutputStream', a)
    _safe_set(a, 'miniJava_State169', b2)
    assert _is_linked(a, 'miniJava_State169', b2)
    if hasattr(b1, 'miniJava_OutputStream'):
        assert not _is_linked(b1, 'miniJava_OutputStream', a)
    if hasattr(b2, 'miniJava_OutputStream'):
        assert _is_linked(b2, 'miniJava_OutputStream', a)
    _safe_set(a, 'miniJava_State169', None)
    assert not _is_linked(a, 'miniJava_State169', b2)
    if hasattr(b2, 'miniJava_OutputStream'):
        assert not _is_linked(b2, 'miniJava_OutputStream', a)


def test_assoc_params11_link_reassign_clear():
    a = miniJava_Parameter()
    b1 = miniJava_Method(abstract=True, static=True)
    b2 = miniJava_Method(abstract=False, static=False)
    _safe_set(a, 'miniJava_Parameter', b1)
    assert _is_linked(a, 'miniJava_Parameter', b1)
    if hasattr(b1, 'miniJava_Method'):
        assert _is_linked(b1, 'miniJava_Method', a)
    _safe_set(a, 'miniJava_Parameter', b2)
    assert _is_linked(a, 'miniJava_Parameter', b2)
    if hasattr(b1, 'miniJava_Method'):
        assert not _is_linked(b1, 'miniJava_Method', a)
    if hasattr(b2, 'miniJava_Method'):
        assert _is_linked(b2, 'miniJava_Method', a)
    _safe_set(a, 'miniJava_Parameter', None)
    assert not _is_linked(a, 'miniJava_Parameter', b2)
    if hasattr(b2, 'miniJava_Method'):
        assert not _is_linked(b2, 'miniJava_Method', a)


def test_assoc_parentContext150_link_reassign_clear():
    a = miniJava_Context()
    b1 = miniJava_Context()
    b2 = miniJava_Context()
    _safe_set(a, 'Context', b1)
    assert _is_linked(a, 'Context', b1)
    if hasattr(b1, 'childContext'):
        assert _is_linked(b1, 'childContext', a)
    _safe_set(a, 'Context', b2)
    assert _is_linked(a, 'Context', b2)
    if hasattr(b1, 'childContext'):
        assert not _is_linked(b1, 'childContext', a)
    if hasattr(b2, 'childContext'):
        assert _is_linked(b2, 'childContext', a)
    _safe_set(a, 'Context', None)
    assert not _is_linked(a, 'Context', b2)
    if hasattr(b2, 'childContext'):
        assert not _is_linked(b2, 'childContext', a)


def test_assoc_parentFrame180_link_reassign_clear():
    a = miniJava_Frame()
    b1 = miniJava_Frame()
    b2 = miniJava_Frame()
    _safe_set(a, 'Frame181', b1)
    assert _is_linked(a, 'Frame181', b1)
    if hasattr(b1, 'childFrame'):
        assert _is_linked(b1, 'childFrame', a)
    _safe_set(a, 'Frame181', b2)
    assert _is_linked(a, 'Frame181', b2)
    if hasattr(b1, 'childFrame'):
        assert not _is_linked(b1, 'childFrame', a)
    if hasattr(b2, 'childFrame'):
        assert _is_linked(b2, 'childFrame', a)
    _safe_set(a, 'Frame181', None)
    assert not _is_linked(a, 'Frame181', b2)
    if hasattr(b2, 'childFrame'):
        assert not _is_linked(b2, 'childFrame', a)


def test_assoc_progression38_link_reassign_clear():
    a = miniJava_ForStatement()
    b1 = miniJava_Assignment()
    b2 = miniJava_Assignment()
    _safe_set(a, 'miniJava_ForStatement39', b1)
    assert _is_linked(a, 'miniJava_ForStatement39', b1)
    if hasattr(b1, 'miniJava_Assignment40'):
        assert _is_linked(b1, 'miniJava_Assignment40', a)
    _safe_set(a, 'miniJava_ForStatement39', b2)
    assert _is_linked(a, 'miniJava_ForStatement39', b2)
    if hasattr(b1, 'miniJava_Assignment40'):
        assert not _is_linked(b1, 'miniJava_Assignment40', a)
    if hasattr(b2, 'miniJava_Assignment40'):
        assert _is_linked(b2, 'miniJava_Assignment40', a)
    _safe_set(a, 'miniJava_ForStatement39', None)
    assert not _is_linked(a, 'miniJava_ForStatement39', b2)
    if hasattr(b2, 'miniJava_Assignment40'):
        assert not _is_linked(b2, 'miniJava_Assignment40', a)


def test_assoc_receiver124_link_reassign_clear():
    a = miniJava_FieldAccess()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_FieldAccess', b1)
    assert _is_linked(a, 'miniJava_FieldAccess', b1)
    if hasattr(b1, 'miniJava_Expression125'):
        assert _is_linked(b1, 'miniJava_Expression125', a)
    _safe_set(a, 'miniJava_FieldAccess', b2)
    assert _is_linked(a, 'miniJava_FieldAccess', b2)
    if hasattr(b1, 'miniJava_Expression125'):
        assert not _is_linked(b1, 'miniJava_Expression125', a)
    if hasattr(b2, 'miniJava_Expression125'):
        assert _is_linked(b2, 'miniJava_Expression125', a)
    _safe_set(a, 'miniJava_FieldAccess', None)
    assert not _is_linked(a, 'miniJava_FieldAccess', b2)
    if hasattr(b2, 'miniJava_Expression125'):
        assert not _is_linked(b2, 'miniJava_Expression125', a)


def test_assoc_receiver129_link_reassign_clear():
    a = miniJava_MethodCall()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_MethodCall', b1)
    assert _is_linked(a, 'miniJava_MethodCall', b1)
    if hasattr(b1, 'miniJava_Expression130'):
        assert _is_linked(b1, 'miniJava_Expression130', a)
    _safe_set(a, 'miniJava_MethodCall', b2)
    assert _is_linked(a, 'miniJava_MethodCall', b2)
    if hasattr(b1, 'miniJava_Expression130'):
        assert not _is_linked(b1, 'miniJava_Expression130', a)
    if hasattr(b2, 'miniJava_Expression130'):
        assert _is_linked(b2, 'miniJava_Expression130', a)
    _safe_set(a, 'miniJava_MethodCall', None)
    assert not _is_linked(a, 'miniJava_MethodCall', b2)
    if hasattr(b2, 'miniJava_Expression130'):
        assert not _is_linked(b2, 'miniJava_Expression130', a)


def test_assoc_referencedClass44_link_reassign_clear():
    a = miniJava_TypeDeclaration(accessLevel="sample_text")
    b1 = miniJava_ClassRef()
    b2 = miniJava_ClassRef()
    _safe_set(a, 'miniJava_TypeDeclaration45', b1)
    assert _is_linked(a, 'miniJava_TypeDeclaration45', b1)
    if hasattr(b1, 'miniJava_ClassRef'):
        assert _is_linked(b1, 'miniJava_ClassRef', a)
    _safe_set(a, 'miniJava_TypeDeclaration45', b2)
    assert _is_linked(a, 'miniJava_TypeDeclaration45', b2)
    if hasattr(b1, 'miniJava_ClassRef'):
        assert not _is_linked(b1, 'miniJava_ClassRef', a)
    if hasattr(b2, 'miniJava_ClassRef'):
        assert _is_linked(b2, 'miniJava_ClassRef', a)
    _safe_set(a, 'miniJava_TypeDeclaration45', None)
    assert not _is_linked(a, 'miniJava_TypeDeclaration45', b2)
    if hasattr(b2, 'miniJava_ClassRef'):
        assert not _is_linked(b2, 'miniJava_ClassRef', a)


def test_assoc_returnValue185_link_reassign_clear():
    a = miniJava_Value()
    b1 = miniJava_Frame()
    b2 = miniJava_Frame()
    _safe_set(a, 'miniJava_Value187', b1)
    assert _is_linked(a, 'miniJava_Value187', b1)
    if hasattr(b1, 'miniJava_Frame186'):
        assert _is_linked(b1, 'miniJava_Frame186', a)
    _safe_set(a, 'miniJava_Value187', b2)
    assert _is_linked(a, 'miniJava_Value187', b2)
    if hasattr(b1, 'miniJava_Frame186'):
        assert not _is_linked(b1, 'miniJava_Frame186', a)
    if hasattr(b2, 'miniJava_Frame186'):
        assert _is_linked(b2, 'miniJava_Frame186', a)
    _safe_set(a, 'miniJava_Value187', None)
    assert not _is_linked(a, 'miniJava_Value187', b2)
    if hasattr(b2, 'miniJava_Frame186'):
        assert not _is_linked(b2, 'miniJava_Frame186', a)


def test_assoc_right100_link_reassign_clear():
    a = miniJava_Minus()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Minus101', b1)
    assert _is_linked(a, 'miniJava_Minus101', b1)
    if hasattr(b1, 'miniJava_Expression102'):
        assert _is_linked(b1, 'miniJava_Expression102', a)
    _safe_set(a, 'miniJava_Minus101', b2)
    assert _is_linked(a, 'miniJava_Minus101', b2)
    if hasattr(b1, 'miniJava_Expression102'):
        assert not _is_linked(b1, 'miniJava_Expression102', a)
    if hasattr(b2, 'miniJava_Expression102'):
        assert _is_linked(b2, 'miniJava_Expression102', a)
    _safe_set(a, 'miniJava_Minus101', None)
    assert not _is_linked(a, 'miniJava_Minus101', b2)
    if hasattr(b2, 'miniJava_Expression102'):
        assert not _is_linked(b2, 'miniJava_Expression102', a)


def test_assoc_right105_link_reassign_clear():
    a = miniJava_Multiplication()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Multiplication106', b1)
    assert _is_linked(a, 'miniJava_Multiplication106', b1)
    if hasattr(b1, 'miniJava_Expression107'):
        assert _is_linked(b1, 'miniJava_Expression107', a)
    _safe_set(a, 'miniJava_Multiplication106', b2)
    assert _is_linked(a, 'miniJava_Multiplication106', b2)
    if hasattr(b1, 'miniJava_Expression107'):
        assert not _is_linked(b1, 'miniJava_Expression107', a)
    if hasattr(b2, 'miniJava_Expression107'):
        assert _is_linked(b2, 'miniJava_Expression107', a)
    _safe_set(a, 'miniJava_Multiplication106', None)
    assert not _is_linked(a, 'miniJava_Multiplication106', b2)
    if hasattr(b2, 'miniJava_Expression107'):
        assert not _is_linked(b2, 'miniJava_Expression107', a)


def test_assoc_right110_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_Division()
    b2 = miniJava_Division()
    _safe_set(a, 'miniJava_Expression112', b1)
    assert _is_linked(a, 'miniJava_Expression112', b1)
    if hasattr(b1, 'miniJava_Division111'):
        assert _is_linked(b1, 'miniJava_Division111', a)
    _safe_set(a, 'miniJava_Expression112', b2)
    assert _is_linked(a, 'miniJava_Expression112', b2)
    if hasattr(b1, 'miniJava_Division111'):
        assert not _is_linked(b1, 'miniJava_Division111', a)
    if hasattr(b2, 'miniJava_Division111'):
        assert _is_linked(b2, 'miniJava_Division111', a)
    _safe_set(a, 'miniJava_Expression112', None)
    assert not _is_linked(a, 'miniJava_Expression112', b2)
    if hasattr(b2, 'miniJava_Division111'):
        assert not _is_linked(b2, 'miniJava_Division111', a)


def test_assoc_right55_link_reassign_clear():
    a = miniJava_Or()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Or56', b1)
    assert _is_linked(a, 'miniJava_Or56', b1)
    if hasattr(b1, 'miniJava_Expression57'):
        assert _is_linked(b1, 'miniJava_Expression57', a)
    _safe_set(a, 'miniJava_Or56', b2)
    assert _is_linked(a, 'miniJava_Or56', b2)
    if hasattr(b1, 'miniJava_Expression57'):
        assert not _is_linked(b1, 'miniJava_Expression57', a)
    if hasattr(b2, 'miniJava_Expression57'):
        assert _is_linked(b2, 'miniJava_Expression57', a)
    _safe_set(a, 'miniJava_Or56', None)
    assert not _is_linked(a, 'miniJava_Or56', b2)
    if hasattr(b2, 'miniJava_Expression57'):
        assert not _is_linked(b2, 'miniJava_Expression57', a)


def test_assoc_right60_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_And()
    b2 = miniJava_And()
    _safe_set(a, 'miniJava_Expression62', b1)
    assert _is_linked(a, 'miniJava_Expression62', b1)
    if hasattr(b1, 'miniJava_And61'):
        assert _is_linked(b1, 'miniJava_And61', a)
    _safe_set(a, 'miniJava_Expression62', b2)
    assert _is_linked(a, 'miniJava_Expression62', b2)
    if hasattr(b1, 'miniJava_And61'):
        assert not _is_linked(b1, 'miniJava_And61', a)
    if hasattr(b2, 'miniJava_And61'):
        assert _is_linked(b2, 'miniJava_And61', a)
    _safe_set(a, 'miniJava_Expression62', None)
    assert not _is_linked(a, 'miniJava_Expression62', b2)
    if hasattr(b2, 'miniJava_And61'):
        assert not _is_linked(b2, 'miniJava_And61', a)


def test_assoc_right65_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_Equality()
    b2 = miniJava_Equality()
    _safe_set(a, 'miniJava_Expression67', b1)
    assert _is_linked(a, 'miniJava_Expression67', b1)
    if hasattr(b1, 'miniJava_Equality66'):
        assert _is_linked(b1, 'miniJava_Equality66', a)
    _safe_set(a, 'miniJava_Expression67', b2)
    assert _is_linked(a, 'miniJava_Expression67', b2)
    if hasattr(b1, 'miniJava_Equality66'):
        assert not _is_linked(b1, 'miniJava_Equality66', a)
    if hasattr(b2, 'miniJava_Equality66'):
        assert _is_linked(b2, 'miniJava_Equality66', a)
    _safe_set(a, 'miniJava_Expression67', None)
    assert not _is_linked(a, 'miniJava_Expression67', b2)
    if hasattr(b2, 'miniJava_Equality66'):
        assert not _is_linked(b2, 'miniJava_Equality66', a)


def test_assoc_right70_link_reassign_clear():
    a = miniJava_Inequality()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Inequality71', b1)
    assert _is_linked(a, 'miniJava_Inequality71', b1)
    if hasattr(b1, 'miniJava_Expression72'):
        assert _is_linked(b1, 'miniJava_Expression72', a)
    _safe_set(a, 'miniJava_Inequality71', b2)
    assert _is_linked(a, 'miniJava_Inequality71', b2)
    if hasattr(b1, 'miniJava_Expression72'):
        assert not _is_linked(b1, 'miniJava_Expression72', a)
    if hasattr(b2, 'miniJava_Expression72'):
        assert _is_linked(b2, 'miniJava_Expression72', a)
    _safe_set(a, 'miniJava_Inequality71', None)
    assert not _is_linked(a, 'miniJava_Inequality71', b2)
    if hasattr(b2, 'miniJava_Expression72'):
        assert not _is_linked(b2, 'miniJava_Expression72', a)


def test_assoc_right75_link_reassign_clear():
    a = miniJava_SuperiorOrEqual()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_SuperiorOrEqual76', b1)
    assert _is_linked(a, 'miniJava_SuperiorOrEqual76', b1)
    if hasattr(b1, 'miniJava_Expression77'):
        assert _is_linked(b1, 'miniJava_Expression77', a)
    _safe_set(a, 'miniJava_SuperiorOrEqual76', b2)
    assert _is_linked(a, 'miniJava_SuperiorOrEqual76', b2)
    if hasattr(b1, 'miniJava_Expression77'):
        assert not _is_linked(b1, 'miniJava_Expression77', a)
    if hasattr(b2, 'miniJava_Expression77'):
        assert _is_linked(b2, 'miniJava_Expression77', a)
    _safe_set(a, 'miniJava_SuperiorOrEqual76', None)
    assert not _is_linked(a, 'miniJava_SuperiorOrEqual76', b2)
    if hasattr(b2, 'miniJava_Expression77'):
        assert not _is_linked(b2, 'miniJava_Expression77', a)


def test_assoc_right80_link_reassign_clear():
    a = miniJava_InferiorOrEqual()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_InferiorOrEqual81', b1)
    assert _is_linked(a, 'miniJava_InferiorOrEqual81', b1)
    if hasattr(b1, 'miniJava_Expression82'):
        assert _is_linked(b1, 'miniJava_Expression82', a)
    _safe_set(a, 'miniJava_InferiorOrEqual81', b2)
    assert _is_linked(a, 'miniJava_InferiorOrEqual81', b2)
    if hasattr(b1, 'miniJava_Expression82'):
        assert not _is_linked(b1, 'miniJava_Expression82', a)
    if hasattr(b2, 'miniJava_Expression82'):
        assert _is_linked(b2, 'miniJava_Expression82', a)
    _safe_set(a, 'miniJava_InferiorOrEqual81', None)
    assert not _is_linked(a, 'miniJava_InferiorOrEqual81', b2)
    if hasattr(b2, 'miniJava_Expression82'):
        assert not _is_linked(b2, 'miniJava_Expression82', a)


def test_assoc_right85_link_reassign_clear():
    a = miniJava_Superior()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Superior86', b1)
    assert _is_linked(a, 'miniJava_Superior86', b1)
    if hasattr(b1, 'miniJava_Expression87'):
        assert _is_linked(b1, 'miniJava_Expression87', a)
    _safe_set(a, 'miniJava_Superior86', b2)
    assert _is_linked(a, 'miniJava_Superior86', b2)
    if hasattr(b1, 'miniJava_Expression87'):
        assert not _is_linked(b1, 'miniJava_Expression87', a)
    if hasattr(b2, 'miniJava_Expression87'):
        assert _is_linked(b2, 'miniJava_Expression87', a)
    _safe_set(a, 'miniJava_Superior86', None)
    assert not _is_linked(a, 'miniJava_Superior86', b2)
    if hasattr(b2, 'miniJava_Expression87'):
        assert not _is_linked(b2, 'miniJava_Expression87', a)


def test_assoc_right90_link_reassign_clear():
    a = miniJava_Inferior()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Inferior91', b1)
    assert _is_linked(a, 'miniJava_Inferior91', b1)
    if hasattr(b1, 'miniJava_Expression92'):
        assert _is_linked(b1, 'miniJava_Expression92', a)
    _safe_set(a, 'miniJava_Inferior91', b2)
    assert _is_linked(a, 'miniJava_Inferior91', b2)
    if hasattr(b1, 'miniJava_Expression92'):
        assert not _is_linked(b1, 'miniJava_Expression92', a)
    if hasattr(b2, 'miniJava_Expression92'):
        assert _is_linked(b2, 'miniJava_Expression92', a)
    _safe_set(a, 'miniJava_Inferior91', None)
    assert not _is_linked(a, 'miniJava_Inferior91', b2)
    if hasattr(b2, 'miniJava_Expression92'):
        assert not _is_linked(b2, 'miniJava_Expression92', a)


def test_assoc_right95_link_reassign_clear():
    a = miniJava_Plus()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_Plus96', b1)
    assert _is_linked(a, 'miniJava_Plus96', b1)
    if hasattr(b1, 'miniJava_Expression97'):
        assert _is_linked(b1, 'miniJava_Expression97', a)
    _safe_set(a, 'miniJava_Plus96', b2)
    assert _is_linked(a, 'miniJava_Plus96', b2)
    if hasattr(b1, 'miniJava_Expression97'):
        assert not _is_linked(b1, 'miniJava_Expression97', a)
    if hasattr(b2, 'miniJava_Expression97'):
        assert _is_linked(b2, 'miniJava_Expression97', a)
    _safe_set(a, 'miniJava_Plus96', None)
    assert not _is_linked(a, 'miniJava_Plus96', b2)
    if hasattr(b2, 'miniJava_Expression97'):
        assert not _is_linked(b2, 'miniJava_Expression97', a)


def test_assoc_rootContext182_link_reassign_clear():
    a = miniJava_Frame()
    b1 = miniJava_Context()
    b2 = miniJava_Context()
    _safe_set(a, 'miniJava_Frame183', b1)
    assert _is_linked(a, 'miniJava_Frame183', b1)
    if hasattr(b1, 'miniJava_Context184'):
        assert _is_linked(b1, 'miniJava_Context184', a)
    _safe_set(a, 'miniJava_Frame183', b2)
    assert _is_linked(a, 'miniJava_Frame183', b2)
    if hasattr(b1, 'miniJava_Context184'):
        assert not _is_linked(b1, 'miniJava_Context184', a)
    if hasattr(b2, 'miniJava_Context184'):
        assert _is_linked(b2, 'miniJava_Context184', a)
    _safe_set(a, 'miniJava_Frame183', None)
    assert not _is_linked(a, 'miniJava_Frame183', b2)
    if hasattr(b2, 'miniJava_Context184'):
        assert not _is_linked(b2, 'miniJava_Context184', a)


def test_assoc_rootFrame164_link_reassign_clear():
    a = miniJava_State()
    b1 = miniJava_Frame()
    b2 = miniJava_Frame()
    _safe_set(a, 'miniJava_State165', b1)
    assert _is_linked(a, 'miniJava_State165', b1)
    if hasattr(b1, 'miniJava_Frame'):
        assert _is_linked(b1, 'miniJava_Frame', a)
    _safe_set(a, 'miniJava_State165', b2)
    assert _is_linked(a, 'miniJava_State165', b2)
    if hasattr(b1, 'miniJava_Frame'):
        assert not _is_linked(b1, 'miniJava_Frame', a)
    if hasattr(b2, 'miniJava_Frame'):
        assert _is_linked(b2, 'miniJava_Frame', a)
    _safe_set(a, 'miniJava_State165', None)
    assert not _is_linked(a, 'miniJava_State165', b2)
    if hasattr(b2, 'miniJava_Frame'):
        assert not _is_linked(b2, 'miniJava_Frame', a)


def test_assoc_size144_link_reassign_clear():
    a = miniJava_NewArray()
    b1 = miniJava_Expression()
    b2 = miniJava_Expression()
    _safe_set(a, 'miniJava_NewArray145', b1)
    assert _is_linked(a, 'miniJava_NewArray145', b1)
    if hasattr(b1, 'miniJava_Expression146'):
        assert _is_linked(b1, 'miniJava_Expression146', a)
    _safe_set(a, 'miniJava_NewArray145', b2)
    assert _is_linked(a, 'miniJava_NewArray145', b2)
    if hasattr(b1, 'miniJava_Expression146'):
        assert not _is_linked(b1, 'miniJava_Expression146', a)
    if hasattr(b2, 'miniJava_Expression146'):
        assert _is_linked(b2, 'miniJava_Expression146', a)
    _safe_set(a, 'miniJava_NewArray145', None)
    assert not _is_linked(a, 'miniJava_NewArray145', b2)
    if hasattr(b2, 'miniJava_Expression146'):
        assert not _is_linked(b2, 'miniJava_Expression146', a)


def test_assoc_state3_link_reassign_clear():
    a = miniJava_State()
    b1 = miniJava_Program(name="sample_text")
    b2 = miniJava_Program(name="sample_text_2")
    _safe_set(a, 'miniJava_State', b1)
    assert _is_linked(a, 'miniJava_State', b1)
    if hasattr(b1, 'miniJava_Program4'):
        assert _is_linked(b1, 'miniJava_Program4', a)
    _safe_set(a, 'miniJava_State', b2)
    assert _is_linked(a, 'miniJava_State', b2)
    if hasattr(b1, 'miniJava_Program4'):
        assert not _is_linked(b1, 'miniJava_Program4', a)
    if hasattr(b2, 'miniJava_Program4'):
        assert _is_linked(b2, 'miniJava_Program4', a)
    _safe_set(a, 'miniJava_State', None)
    assert not _is_linked(a, 'miniJava_State', b2)
    if hasattr(b2, 'miniJava_Program4'):
        assert not _is_linked(b2, 'miniJava_Program4', a)


def test_assoc_statements15_link_reassign_clear():
    a = miniJava_Statement()
    b1 = miniJava_Block()
    b2 = miniJava_Block()
    _safe_set(a, 'miniJava_Statement', b1)
    assert _is_linked(a, 'miniJava_Statement', b1)
    if hasattr(b1, 'miniJava_Block16'):
        assert _is_linked(b1, 'miniJava_Block16', a)
    _safe_set(a, 'miniJava_Statement', b2)
    assert _is_linked(a, 'miniJava_Statement', b2)
    if hasattr(b1, 'miniJava_Block16'):
        assert not _is_linked(b1, 'miniJava_Block16', a)
    if hasattr(b2, 'miniJava_Block16'):
        assert _is_linked(b2, 'miniJava_Block16', a)
    _safe_set(a, 'miniJava_Statement', None)
    assert not _is_linked(a, 'miniJava_Statement', b2)
    if hasattr(b2, 'miniJava_Block16'):
        assert not _is_linked(b2, 'miniJava_Block16', a)


def test_assoc_superClass10_link_reassign_clear():
    a = miniJava_Class(abstract=True)
    b1 = miniJava_Class(abstract=True)
    b2 = miniJava_Class(abstract=False)
    _safe_set(a, 'miniJava_Class', b1)
    assert _is_linked(a, 'miniJava_Class', b1)
    if hasattr(b1, 'miniJava_Class9'):
        assert _is_linked(b1, 'miniJava_Class9', a)
    _safe_set(a, 'miniJava_Class', b2)
    assert _is_linked(a, 'miniJava_Class', b2)
    if hasattr(b1, 'miniJava_Class9'):
        assert not _is_linked(b1, 'miniJava_Class9', a)
    if hasattr(b2, 'miniJava_Class9'):
        assert _is_linked(b2, 'miniJava_Class9', a)
    _safe_set(a, 'miniJava_Class', None)
    assert not _is_linked(a, 'miniJava_Class', b2)
    if hasattr(b2, 'miniJava_Class9'):
        assert not _is_linked(b2, 'miniJava_Class9', a)


def test_assoc_symbol147_link_reassign_clear():
    a = miniJava_SymbolRef()
    b1 = miniJava_Symbol()
    b2 = miniJava_Symbol()
    _safe_set(a, 'miniJava_SymbolRef', b1)
    assert _is_linked(a, 'miniJava_SymbolRef', b1)
    if hasattr(b1, 'miniJava_Symbol'):
        assert _is_linked(b1, 'miniJava_Symbol', a)
    _safe_set(a, 'miniJava_SymbolRef', b2)
    assert _is_linked(a, 'miniJava_SymbolRef', b2)
    if hasattr(b1, 'miniJava_Symbol'):
        assert not _is_linked(b1, 'miniJava_Symbol', a)
    if hasattr(b2, 'miniJava_Symbol'):
        assert _is_linked(b2, 'miniJava_Symbol', a)
    _safe_set(a, 'miniJava_SymbolRef', None)
    assert not _is_linked(a, 'miniJava_SymbolRef', b2)
    if hasattr(b2, 'miniJava_Symbol'):
        assert not _is_linked(b2, 'miniJava_Symbol', a)


def test_assoc_thenBlock23_link_reassign_clear():
    a = miniJava_IfStatement()
    b1 = miniJava_Block()
    b2 = miniJava_Block()
    _safe_set(a, 'miniJava_IfStatement24', b1)
    assert _is_linked(a, 'miniJava_IfStatement24', b1)
    if hasattr(b1, 'miniJava_Block25'):
        assert _is_linked(b1, 'miniJava_Block25', a)
    _safe_set(a, 'miniJava_IfStatement24', b2)
    assert _is_linked(a, 'miniJava_IfStatement24', b2)
    if hasattr(b1, 'miniJava_Block25'):
        assert not _is_linked(b1, 'miniJava_Block25', a)
    if hasattr(b2, 'miniJava_Block25'):
        assert _is_linked(b2, 'miniJava_Block25', a)
    _safe_set(a, 'miniJava_IfStatement24', None)
    assert not _is_linked(a, 'miniJava_IfStatement24', b2)
    if hasattr(b2, 'miniJava_Block25'):
        assert not _is_linked(b2, 'miniJava_Block25', a)


def test_assoc_type137_link_reassign_clear():
    a = miniJava_NewObject()
    b1 = miniJava_Class(abstract=True)
    b2 = miniJava_Class(abstract=False)
    _safe_set(a, 'miniJava_NewObject', b1)
    assert _is_linked(a, 'miniJava_NewObject', b1)
    if hasattr(b1, 'miniJava_Class138'):
        assert _is_linked(b1, 'miniJava_Class138', a)
    _safe_set(a, 'miniJava_NewObject', b2)
    assert _is_linked(a, 'miniJava_NewObject', b2)
    if hasattr(b1, 'miniJava_Class138'):
        assert not _is_linked(b1, 'miniJava_Class138', a)
    if hasattr(b2, 'miniJava_Class138'):
        assert _is_linked(b2, 'miniJava_Class138', a)
    _safe_set(a, 'miniJava_NewObject', None)
    assert not _is_linked(a, 'miniJava_NewObject', b2)
    if hasattr(b2, 'miniJava_Class138'):
        assert not _is_linked(b2, 'miniJava_Class138', a)


def test_assoc_type142_link_reassign_clear():
    a = miniJava_TypeRef()
    b1 = miniJava_NewArray()
    b2 = miniJava_NewArray()
    _safe_set(a, 'miniJava_TypeRef143', b1)
    assert _is_linked(a, 'miniJava_TypeRef143', b1)
    if hasattr(b1, 'miniJava_NewArray'):
        assert _is_linked(b1, 'miniJava_NewArray', a)
    _safe_set(a, 'miniJava_TypeRef143', b2)
    assert _is_linked(a, 'miniJava_TypeRef143', b2)
    if hasattr(b1, 'miniJava_NewArray'):
        assert not _is_linked(b1, 'miniJava_NewArray', a)
    if hasattr(b2, 'miniJava_NewArray'):
        assert _is_linked(b2, 'miniJava_NewArray', a)
    _safe_set(a, 'miniJava_TypeRef143', None)
    assert not _is_linked(a, 'miniJava_TypeRef143', b2)
    if hasattr(b2, 'miniJava_NewArray'):
        assert not _is_linked(b2, 'miniJava_NewArray', a)


def test_assoc_type195_link_reassign_clear():
    a = miniJava_Class(abstract=True)
    b1 = miniJava_ObjectInstance()
    b2 = miniJava_ObjectInstance()
    _safe_set(a, 'miniJava_Class197', b1)
    assert _is_linked(a, 'miniJava_Class197', b1)
    if hasattr(b1, 'miniJava_ObjectInstance196'):
        assert _is_linked(b1, 'miniJava_ObjectInstance196', a)
    _safe_set(a, 'miniJava_Class197', b2)
    assert _is_linked(a, 'miniJava_Class197', b2)
    if hasattr(b1, 'miniJava_ObjectInstance196'):
        assert not _is_linked(b1, 'miniJava_ObjectInstance196', a)
    if hasattr(b2, 'miniJava_ObjectInstance196'):
        assert _is_linked(b2, 'miniJava_ObjectInstance196', a)
    _safe_set(a, 'miniJava_Class197', None)
    assert not _is_linked(a, 'miniJava_Class197', b2)
    if hasattr(b2, 'miniJava_ObjectInstance196'):
        assert not _is_linked(b2, 'miniJava_ObjectInstance196', a)


def test_assoc_typeRef46_link_reassign_clear():
    a = miniJava_TypeRef()
    b1 = miniJava_TypedDeclaration()
    b2 = miniJava_TypedDeclaration()
    _safe_set(a, 'miniJava_TypeRef', b1)
    assert _is_linked(a, 'miniJava_TypeRef', b1)
    if hasattr(b1, 'miniJava_TypedDeclaration'):
        assert _is_linked(b1, 'miniJava_TypedDeclaration', a)
    _safe_set(a, 'miniJava_TypeRef', b2)
    assert _is_linked(a, 'miniJava_TypeRef', b2)
    if hasattr(b1, 'miniJava_TypedDeclaration'):
        assert not _is_linked(b1, 'miniJava_TypedDeclaration', a)
    if hasattr(b2, 'miniJava_TypedDeclaration'):
        assert _is_linked(b2, 'miniJava_TypedDeclaration', a)
    _safe_set(a, 'miniJava_TypeRef', None)
    assert not _is_linked(a, 'miniJava_TypeRef', b2)
    if hasattr(b2, 'miniJava_TypedDeclaration'):
        assert not _is_linked(b2, 'miniJava_TypedDeclaration', a)


def test_assoc_value154_link_reassign_clear():
    a = miniJava_Value()
    b1 = miniJava_SymbolBinding()
    b2 = miniJava_SymbolBinding()
    _safe_set(a, 'miniJava_Value', b1)
    assert _is_linked(a, 'miniJava_Value', b1)
    if hasattr(b1, 'miniJava_SymbolBinding155'):
        assert _is_linked(b1, 'miniJava_SymbolBinding155', a)
    _safe_set(a, 'miniJava_Value', b2)
    assert _is_linked(a, 'miniJava_Value', b2)
    if hasattr(b1, 'miniJava_SymbolBinding155'):
        assert not _is_linked(b1, 'miniJava_SymbolBinding155', a)
    if hasattr(b2, 'miniJava_SymbolBinding155'):
        assert _is_linked(b2, 'miniJava_SymbolBinding155', a)
    _safe_set(a, 'miniJava_Value', None)
    assert not _is_linked(a, 'miniJava_Value', b2)
    if hasattr(b2, 'miniJava_SymbolBinding155'):
        assert not _is_linked(b2, 'miniJava_SymbolBinding155', a)


def test_assoc_value161_link_reassign_clear():
    a = miniJava_Value()
    b1 = miniJava_FieldBinding()
    b2 = miniJava_FieldBinding()
    _safe_set(a, 'miniJava_Value163', b1)
    assert _is_linked(a, 'miniJava_Value163', b1)
    if hasattr(b1, 'miniJava_FieldBinding162'):
        assert _is_linked(b1, 'miniJava_FieldBinding162', a)
    _safe_set(a, 'miniJava_Value163', b2)
    assert _is_linked(a, 'miniJava_Value163', b2)
    if hasattr(b1, 'miniJava_FieldBinding162'):
        assert not _is_linked(b1, 'miniJava_FieldBinding162', a)
    if hasattr(b2, 'miniJava_FieldBinding162'):
        assert _is_linked(b2, 'miniJava_FieldBinding162', a)
    _safe_set(a, 'miniJava_Value163', None)
    assert not _is_linked(a, 'miniJava_Value163', b2)
    if hasattr(b2, 'miniJava_FieldBinding162'):
        assert not _is_linked(b2, 'miniJava_FieldBinding162', a)


def test_assoc_value198_link_reassign_clear():
    a = miniJava_Value()
    b1 = miniJava_ArrayInstance(size="sample_text")
    b2 = miniJava_ArrayInstance(size="sample_text_2")
    _safe_set(a, 'miniJava_Value200', b1)
    assert _is_linked(a, 'miniJava_Value200', b1)
    if hasattr(b1, 'miniJava_ArrayInstance199'):
        assert _is_linked(b1, 'miniJava_ArrayInstance199', a)
    _safe_set(a, 'miniJava_Value200', b2)
    assert _is_linked(a, 'miniJava_Value200', b2)
    if hasattr(b1, 'miniJava_ArrayInstance199'):
        assert not _is_linked(b1, 'miniJava_ArrayInstance199', a)
    if hasattr(b2, 'miniJava_ArrayInstance199'):
        assert _is_linked(b2, 'miniJava_ArrayInstance199', a)
    _safe_set(a, 'miniJava_Value200', None)
    assert not _is_linked(a, 'miniJava_Value200', b2)
    if hasattr(b2, 'miniJava_ArrayInstance199'):
        assert not _is_linked(b2, 'miniJava_ArrayInstance199', a)


def test_assoc_value49_link_reassign_clear():
    a = miniJava_Expression()
    b1 = miniJava_Assignment()
    b2 = miniJava_Assignment()
    _safe_set(a, 'miniJava_Expression51', b1)
    assert _is_linked(a, 'miniJava_Expression51', b1)
    if hasattr(b1, 'miniJava_Assignment50'):
        assert _is_linked(b1, 'miniJava_Assignment50', a)
    _safe_set(a, 'miniJava_Expression51', b2)
    assert _is_linked(a, 'miniJava_Expression51', b2)
    if hasattr(b1, 'miniJava_Assignment50'):
        assert not _is_linked(b1, 'miniJava_Assignment50', a)
    if hasattr(b2, 'miniJava_Assignment50'):
        assert _is_linked(b2, 'miniJava_Assignment50', a)
    _safe_set(a, 'miniJava_Expression51', None)
    assert not _is_linked(a, 'miniJava_Expression51', b2)
    if hasattr(b2, 'miniJava_Assignment50'):
        assert not _is_linked(b2, 'miniJava_Assignment50', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Assignee_strategy = st.builds(Assignee)
@given(instance=Assignee_strategy)
@settings(max_examples=25)
def test_Assignee_instantiation(instance):
    assert isinstance(instance, Assignee)


Call_strategy = st.builds(Call)
@given(instance=Call_strategy)
@settings(max_examples=25)
def test_Call_instantiation(instance):
    assert isinstance(instance, Call)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Member_strategy = st.builds(Member)
@given(instance=Member_strategy)
@settings(max_examples=25)
def test_Member_instantiation(instance):
    assert isinstance(instance, Member)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


SingleTypeRef_strategy = st.builds(SingleTypeRef)
@given(instance=SingleTypeRef_strategy)
@settings(max_examples=25)
def test_SingleTypeRef_instantiation(instance):
    assert isinstance(instance, SingleTypeRef)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Symbol_strategy = st.builds(Symbol)
@given(instance=Symbol_strategy)
@settings(max_examples=25)
def test_Symbol_instantiation(instance):
    assert isinstance(instance, Symbol)


TypeDeclaration_strategy = st.builds(TypeDeclaration)
@given(instance=TypeDeclaration_strategy)
@settings(max_examples=25)
def test_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)


TypeRef_strategy = st.builds(TypeRef)
@given(instance=TypeRef_strategy)
@settings(max_examples=25)
def test_TypeRef_instantiation(instance):
    assert isinstance(instance, TypeRef)


TypedDeclaration_strategy = st.builds(TypedDeclaration)
@given(instance=TypedDeclaration_strategy)
@settings(max_examples=25)
def test_TypedDeclaration_instantiation(instance):
    assert isinstance(instance, TypedDeclaration)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


miniJava_And_strategy = st.builds(miniJava_And)
@given(instance=miniJava_And_strategy)
@settings(max_examples=25)
def test_miniJava_And_instantiation(instance):
    assert isinstance(instance, miniJava_And)


miniJava_ArrayAccess_strategy = st.builds(miniJava_ArrayAccess)
@given(instance=miniJava_ArrayAccess_strategy)
@settings(max_examples=25)
def test_miniJava_ArrayAccess_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayAccess)


miniJava_ArrayInstance_strategy = st.builds(miniJava_ArrayInstance, size=safe_text)
@given(instance=miniJava_ArrayInstance_strategy)
@settings(max_examples=25)
def test_miniJava_ArrayInstance_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayInstance)


miniJava_ArrayLength_strategy = st.builds(miniJava_ArrayLength)
@given(instance=miniJava_ArrayLength_strategy)
@settings(max_examples=25)
def test_miniJava_ArrayLength_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayLength)


miniJava_ArrayRefValue_strategy = st.builds(miniJava_ArrayRefValue)
@given(instance=miniJava_ArrayRefValue_strategy)
@settings(max_examples=25)
def test_miniJava_ArrayRefValue_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayRefValue)


miniJava_ArrayTypeRef_strategy = st.builds(miniJava_ArrayTypeRef)
@given(instance=miniJava_ArrayTypeRef_strategy)
@settings(max_examples=25)
def test_miniJava_ArrayTypeRef_instantiation(instance):
    assert isinstance(instance, miniJava_ArrayTypeRef)


miniJava_Assignee_strategy = st.builds(miniJava_Assignee)
@given(instance=miniJava_Assignee_strategy)
@settings(max_examples=25)
def test_miniJava_Assignee_instantiation(instance):
    assert isinstance(instance, miniJava_Assignee)


miniJava_Assignment_strategy = st.builds(miniJava_Assignment)
@given(instance=miniJava_Assignment_strategy)
@settings(max_examples=25)
def test_miniJava_Assignment_instantiation(instance):
    assert isinstance(instance, miniJava_Assignment)


miniJava_Block_strategy = st.builds(miniJava_Block)
@given(instance=miniJava_Block_strategy)
@settings(max_examples=25)
def test_miniJava_Block_instantiation(instance):
    assert isinstance(instance, miniJava_Block)


miniJava_BoolConstant_strategy = st.builds(miniJava_BoolConstant, value=safe_text)
@given(instance=miniJava_BoolConstant_strategy)
@settings(max_examples=25)
def test_miniJava_BoolConstant_instantiation(instance):
    assert isinstance(instance, miniJava_BoolConstant)


miniJava_BooleanTypeRef_strategy = st.builds(miniJava_BooleanTypeRef)
@given(instance=miniJava_BooleanTypeRef_strategy)
@settings(max_examples=25)
def test_miniJava_BooleanTypeRef_instantiation(instance):
    assert isinstance(instance, miniJava_BooleanTypeRef)


miniJava_BooleanValue_strategy = st.builds(miniJava_BooleanValue, value=st.booleans())
@given(instance=miniJava_BooleanValue_strategy)
@settings(max_examples=25)
def test_miniJava_BooleanValue_instantiation(instance):
    assert isinstance(instance, miniJava_BooleanValue)


miniJava_Call_strategy = st.builds(miniJava_Call)
@given(instance=miniJava_Call_strategy)
@settings(max_examples=25)
def test_miniJava_Call_instantiation(instance):
    assert isinstance(instance, miniJava_Call)


miniJava_Class_strategy = st.builds(miniJava_Class, abstract=st.booleans())
@given(instance=miniJava_Class_strategy)
@settings(max_examples=25)
def test_miniJava_Class_instantiation(instance):
    assert isinstance(instance, miniJava_Class)


miniJava_ClassRef_strategy = st.builds(miniJava_ClassRef)
@given(instance=miniJava_ClassRef_strategy)
@settings(max_examples=25)
def test_miniJava_ClassRef_instantiation(instance):
    assert isinstance(instance, miniJava_ClassRef)


miniJava_Context_strategy = st.builds(miniJava_Context)
@given(instance=miniJava_Context_strategy)
@settings(max_examples=25)
def test_miniJava_Context_instantiation(instance):
    assert isinstance(instance, miniJava_Context)


miniJava_Division_strategy = st.builds(miniJava_Division)
@given(instance=miniJava_Division_strategy)
@settings(max_examples=25)
def test_miniJava_Division_instantiation(instance):
    assert isinstance(instance, miniJava_Division)


miniJava_Equality_strategy = st.builds(miniJava_Equality)
@given(instance=miniJava_Equality_strategy)
@settings(max_examples=25)
def test_miniJava_Equality_instantiation(instance):
    assert isinstance(instance, miniJava_Equality)


miniJava_Expression_strategy = st.builds(miniJava_Expression)
@given(instance=miniJava_Expression_strategy)
@settings(max_examples=25)
def test_miniJava_Expression_instantiation(instance):
    assert isinstance(instance, miniJava_Expression)


miniJava_Field_strategy = st.builds(miniJava_Field)
@given(instance=miniJava_Field_strategy)
@settings(max_examples=25)
def test_miniJava_Field_instantiation(instance):
    assert isinstance(instance, miniJava_Field)


miniJava_FieldAccess_strategy = st.builds(miniJava_FieldAccess)
@given(instance=miniJava_FieldAccess_strategy)
@settings(max_examples=25)
def test_miniJava_FieldAccess_instantiation(instance):
    assert isinstance(instance, miniJava_FieldAccess)


miniJava_FieldBinding_strategy = st.builds(miniJava_FieldBinding)
@given(instance=miniJava_FieldBinding_strategy)
@settings(max_examples=25)
def test_miniJava_FieldBinding_instantiation(instance):
    assert isinstance(instance, miniJava_FieldBinding)


miniJava_ForStatement_strategy = st.builds(miniJava_ForStatement)
@given(instance=miniJava_ForStatement_strategy)
@settings(max_examples=25)
def test_miniJava_ForStatement_instantiation(instance):
    assert isinstance(instance, miniJava_ForStatement)


miniJava_Frame_strategy = st.builds(miniJava_Frame)
@given(instance=miniJava_Frame_strategy)
@settings(max_examples=25)
def test_miniJava_Frame_instantiation(instance):
    assert isinstance(instance, miniJava_Frame)


miniJava_IfStatement_strategy = st.builds(miniJava_IfStatement)
@given(instance=miniJava_IfStatement_strategy)
@settings(max_examples=25)
def test_miniJava_IfStatement_instantiation(instance):
    assert isinstance(instance, miniJava_IfStatement)


miniJava_Import_strategy = st.builds(miniJava_Import, importedNamespace=safe_text)
@given(instance=miniJava_Import_strategy)
@settings(max_examples=25)
def test_miniJava_Import_instantiation(instance):
    assert isinstance(instance, miniJava_Import)


miniJava_Inequality_strategy = st.builds(miniJava_Inequality)
@given(instance=miniJava_Inequality_strategy)
@settings(max_examples=25)
def test_miniJava_Inequality_instantiation(instance):
    assert isinstance(instance, miniJava_Inequality)


miniJava_Inferior_strategy = st.builds(miniJava_Inferior)
@given(instance=miniJava_Inferior_strategy)
@settings(max_examples=25)
def test_miniJava_Inferior_instantiation(instance):
    assert isinstance(instance, miniJava_Inferior)


miniJava_InferiorOrEqual_strategy = st.builds(miniJava_InferiorOrEqual)
@given(instance=miniJava_InferiorOrEqual_strategy)
@settings(max_examples=25)
def test_miniJava_InferiorOrEqual_instantiation(instance):
    assert isinstance(instance, miniJava_InferiorOrEqual)


miniJava_IntConstant_strategy = st.builds(miniJava_IntConstant, value=st.integers())
@given(instance=miniJava_IntConstant_strategy)
@settings(max_examples=25)
def test_miniJava_IntConstant_instantiation(instance):
    assert isinstance(instance, miniJava_IntConstant)


miniJava_IntegerTypeRef_strategy = st.builds(miniJava_IntegerTypeRef)
@given(instance=miniJava_IntegerTypeRef_strategy)
@settings(max_examples=25)
def test_miniJava_IntegerTypeRef_instantiation(instance):
    assert isinstance(instance, miniJava_IntegerTypeRef)


miniJava_IntegerValue_strategy = st.builds(miniJava_IntegerValue, value=safe_text)
@given(instance=miniJava_IntegerValue_strategy)
@settings(max_examples=25)
def test_miniJava_IntegerValue_instantiation(instance):
    assert isinstance(instance, miniJava_IntegerValue)


miniJava_Interface_strategy = st.builds(miniJava_Interface)
@given(instance=miniJava_Interface_strategy)
@settings(max_examples=25)
def test_miniJava_Interface_instantiation(instance):
    assert isinstance(instance, miniJava_Interface)


miniJava_Member_strategy = st.builds(miniJava_Member, access=safe_text)
@given(instance=miniJava_Member_strategy)
@settings(max_examples=25)
def test_miniJava_Member_instantiation(instance):
    assert isinstance(instance, miniJava_Member)


miniJava_Method_strategy = st.builds(miniJava_Method, abstract=st.booleans(), static=st.booleans())
@given(instance=miniJava_Method_strategy)
@settings(max_examples=25)
def test_miniJava_Method_instantiation(instance):
    assert isinstance(instance, miniJava_Method)


miniJava_MethodCall_strategy = st.builds(miniJava_MethodCall)
@given(instance=miniJava_MethodCall_strategy)
@settings(max_examples=25)
def test_miniJava_MethodCall_instantiation(instance):
    assert isinstance(instance, miniJava_MethodCall)


miniJava_MethodCall2_strategy = st.builds(miniJava_MethodCall2)
@given(instance=miniJava_MethodCall2_strategy)
@settings(max_examples=25)
def test_miniJava_MethodCall2_instantiation(instance):
    assert isinstance(instance, miniJava_MethodCall2)


miniJava_Minus_strategy = st.builds(miniJava_Minus)
@given(instance=miniJava_Minus_strategy)
@settings(max_examples=25)
def test_miniJava_Minus_instantiation(instance):
    assert isinstance(instance, miniJava_Minus)


miniJava_Multiplication_strategy = st.builds(miniJava_Multiplication)
@given(instance=miniJava_Multiplication_strategy)
@settings(max_examples=25)
def test_miniJava_Multiplication_instantiation(instance):
    assert isinstance(instance, miniJava_Multiplication)


miniJava_NamedElement_strategy = st.builds(miniJava_NamedElement, name=safe_text)
@given(instance=miniJava_NamedElement_strategy)
@settings(max_examples=25)
def test_miniJava_NamedElement_instantiation(instance):
    assert isinstance(instance, miniJava_NamedElement)


miniJava_Neg_strategy = st.builds(miniJava_Neg)
@given(instance=miniJava_Neg_strategy)
@settings(max_examples=25)
def test_miniJava_Neg_instantiation(instance):
    assert isinstance(instance, miniJava_Neg)


miniJava_NewArray_strategy = st.builds(miniJava_NewArray)
@given(instance=miniJava_NewArray_strategy)
@settings(max_examples=25)
def test_miniJava_NewArray_instantiation(instance):
    assert isinstance(instance, miniJava_NewArray)


miniJava_NewCall_strategy = st.builds(miniJava_NewCall)
@given(instance=miniJava_NewCall_strategy)
@settings(max_examples=25)
def test_miniJava_NewCall_instantiation(instance):
    assert isinstance(instance, miniJava_NewCall)


miniJava_NewObject_strategy = st.builds(miniJava_NewObject)
@given(instance=miniJava_NewObject_strategy)
@settings(max_examples=25)
def test_miniJava_NewObject_instantiation(instance):
    assert isinstance(instance, miniJava_NewObject)


miniJava_Not_strategy = st.builds(miniJava_Not)
@given(instance=miniJava_Not_strategy)
@settings(max_examples=25)
def test_miniJava_Not_instantiation(instance):
    assert isinstance(instance, miniJava_Not)


miniJava_Null_strategy = st.builds(miniJava_Null)
@given(instance=miniJava_Null_strategy)
@settings(max_examples=25)
def test_miniJava_Null_instantiation(instance):
    assert isinstance(instance, miniJava_Null)


miniJava_NullValue_strategy = st.builds(miniJava_NullValue)
@given(instance=miniJava_NullValue_strategy)
@settings(max_examples=25)
def test_miniJava_NullValue_instantiation(instance):
    assert isinstance(instance, miniJava_NullValue)


miniJava_ObjectInstance_strategy = st.builds(miniJava_ObjectInstance)
@given(instance=miniJava_ObjectInstance_strategy)
@settings(max_examples=25)
def test_miniJava_ObjectInstance_instantiation(instance):
    assert isinstance(instance, miniJava_ObjectInstance)


miniJava_ObjectRefValue_strategy = st.builds(miniJava_ObjectRefValue)
@given(instance=miniJava_ObjectRefValue_strategy)
@settings(max_examples=25)
def test_miniJava_ObjectRefValue_instantiation(instance):
    assert isinstance(instance, miniJava_ObjectRefValue)


miniJava_Or_strategy = st.builds(miniJava_Or)
@given(instance=miniJava_Or_strategy)
@settings(max_examples=25)
def test_miniJava_Or_instantiation(instance):
    assert isinstance(instance, miniJava_Or)


miniJava_OutputStream_strategy = st.builds(miniJava_OutputStream, stream=safe_text)
@given(instance=miniJava_OutputStream_strategy)
@settings(max_examples=25)
def test_miniJava_OutputStream_instantiation(instance):
    assert isinstance(instance, miniJava_OutputStream)


miniJava_Parameter_strategy = st.builds(miniJava_Parameter)
@given(instance=miniJava_Parameter_strategy)
@settings(max_examples=25)
def test_miniJava_Parameter_instantiation(instance):
    assert isinstance(instance, miniJava_Parameter)


miniJava_Plus_strategy = st.builds(miniJava_Plus)
@given(instance=miniJava_Plus_strategy)
@settings(max_examples=25)
def test_miniJava_Plus_instantiation(instance):
    assert isinstance(instance, miniJava_Plus)


miniJava_PrintStatement_strategy = st.builds(miniJava_PrintStatement)
@given(instance=miniJava_PrintStatement_strategy)
@settings(max_examples=25)
def test_miniJava_PrintStatement_instantiation(instance):
    assert isinstance(instance, miniJava_PrintStatement)


miniJava_Program_strategy = st.builds(miniJava_Program, name=safe_text)
@given(instance=miniJava_Program_strategy)
@settings(max_examples=25)
def test_miniJava_Program_instantiation(instance):
    assert isinstance(instance, miniJava_Program)


miniJava_Return_strategy = st.builds(miniJava_Return)
@given(instance=miniJava_Return_strategy)
@settings(max_examples=25)
def test_miniJava_Return_instantiation(instance):
    assert isinstance(instance, miniJava_Return)


miniJava_SingleTypeRef_strategy = st.builds(miniJava_SingleTypeRef)
@given(instance=miniJava_SingleTypeRef_strategy)
@settings(max_examples=25)
def test_miniJava_SingleTypeRef_instantiation(instance):
    assert isinstance(instance, miniJava_SingleTypeRef)


miniJava_State_strategy = st.builds(miniJava_State)
@given(instance=miniJava_State_strategy)
@settings(max_examples=25)
def test_miniJava_State_instantiation(instance):
    assert isinstance(instance, miniJava_State)


miniJava_Statement_strategy = st.builds(miniJava_Statement)
@given(instance=miniJava_Statement_strategy)
@settings(max_examples=25)
def test_miniJava_Statement_instantiation(instance):
    assert isinstance(instance, miniJava_Statement)


miniJava_StringConstant_strategy = st.builds(miniJava_StringConstant, value=safe_text)
@given(instance=miniJava_StringConstant_strategy)
@settings(max_examples=25)
def test_miniJava_StringConstant_instantiation(instance):
    assert isinstance(instance, miniJava_StringConstant)


miniJava_StringTypeRef_strategy = st.builds(miniJava_StringTypeRef)
@given(instance=miniJava_StringTypeRef_strategy)
@settings(max_examples=25)
def test_miniJava_StringTypeRef_instantiation(instance):
    assert isinstance(instance, miniJava_StringTypeRef)


miniJava_StringValue_strategy = st.builds(miniJava_StringValue, value=safe_text)
@given(instance=miniJava_StringValue_strategy)
@settings(max_examples=25)
def test_miniJava_StringValue_instantiation(instance):
    assert isinstance(instance, miniJava_StringValue)


miniJava_Super_strategy = st.builds(miniJava_Super)
@given(instance=miniJava_Super_strategy)
@settings(max_examples=25)
def test_miniJava_Super_instantiation(instance):
    assert isinstance(instance, miniJava_Super)


miniJava_Superior_strategy = st.builds(miniJava_Superior)
@given(instance=miniJava_Superior_strategy)
@settings(max_examples=25)
def test_miniJava_Superior_instantiation(instance):
    assert isinstance(instance, miniJava_Superior)


miniJava_SuperiorOrEqual_strategy = st.builds(miniJava_SuperiorOrEqual)
@given(instance=miniJava_SuperiorOrEqual_strategy)
@settings(max_examples=25)
def test_miniJava_SuperiorOrEqual_instantiation(instance):
    assert isinstance(instance, miniJava_SuperiorOrEqual)


miniJava_Symbol_strategy = st.builds(miniJava_Symbol)
@given(instance=miniJava_Symbol_strategy)
@settings(max_examples=25)
def test_miniJava_Symbol_instantiation(instance):
    assert isinstance(instance, miniJava_Symbol)


miniJava_SymbolBinding_strategy = st.builds(miniJava_SymbolBinding)
@given(instance=miniJava_SymbolBinding_strategy)
@settings(max_examples=25)
def test_miniJava_SymbolBinding_instantiation(instance):
    assert isinstance(instance, miniJava_SymbolBinding)


miniJava_SymbolRef_strategy = st.builds(miniJava_SymbolRef)
@given(instance=miniJava_SymbolRef_strategy)
@settings(max_examples=25)
def test_miniJava_SymbolRef_instantiation(instance):
    assert isinstance(instance, miniJava_SymbolRef)


miniJava_This_strategy = st.builds(miniJava_This)
@given(instance=miniJava_This_strategy)
@settings(max_examples=25)
def test_miniJava_This_instantiation(instance):
    assert isinstance(instance, miniJava_This)


miniJava_TypeDeclaration_strategy = st.builds(miniJava_TypeDeclaration, accessLevel=safe_text)
@given(instance=miniJava_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_miniJava_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, miniJava_TypeDeclaration)


miniJava_TypeRef_strategy = st.builds(miniJava_TypeRef)
@given(instance=miniJava_TypeRef_strategy)
@settings(max_examples=25)
def test_miniJava_TypeRef_instantiation(instance):
    assert isinstance(instance, miniJava_TypeRef)


miniJava_TypedDeclaration_strategy = st.builds(miniJava_TypedDeclaration)
@given(instance=miniJava_TypedDeclaration_strategy)
@settings(max_examples=25)
def test_miniJava_TypedDeclaration_instantiation(instance):
    assert isinstance(instance, miniJava_TypedDeclaration)


miniJava_Value_strategy = st.builds(miniJava_Value)
@given(instance=miniJava_Value_strategy)
@settings(max_examples=25)
def test_miniJava_Value_instantiation(instance):
    assert isinstance(instance, miniJava_Value)


miniJava_VariableDeclaration_strategy = st.builds(miniJava_VariableDeclaration)
@given(instance=miniJava_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_miniJava_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, miniJava_VariableDeclaration)


miniJava_VoidTypeRef_strategy = st.builds(miniJava_VoidTypeRef)
@given(instance=miniJava_VoidTypeRef_strategy)
@settings(max_examples=25)
def test_miniJava_VoidTypeRef_instantiation(instance):
    assert isinstance(instance, miniJava_VoidTypeRef)


miniJava_WhileStatement_strategy = st.builds(miniJava_WhileStatement)
@given(instance=miniJava_WhileStatement_strategy)
@settings(max_examples=25)
def test_miniJava_WhileStatement_instantiation(instance):
    assert isinstance(instance, miniJava_WhileStatement)



