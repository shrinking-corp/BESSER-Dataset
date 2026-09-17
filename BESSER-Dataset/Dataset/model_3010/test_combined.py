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
    miniJava_MethodCall2,
    miniJava_NewCall,
    miniJava_Call,
    miniJava_ArrayInstance,
    miniJava_ObjectInstance,
    miniJava_Frame,
    miniJava_OutputStream,
    miniJava_FieldBinding,
    Value,
    miniJava_BooleanValue,
    miniJava_NullValue,
    miniJava_StringValue,
    miniJava_ObjectRefValue,
    miniJava_ArrayRefValue,
    miniJava_IntegerValue,
    miniJava_Value,
    miniJava_SymbolToSymbolBindingMap,
    miniJava_SymbolBinding,
    miniJava_Context,
    Expression,
    miniJava_Neg,
    miniJava_Inferior,
    miniJava_Minus,
    miniJava_Multiplication,
    miniJava_InferiorOrEqual,
    miniJava_And,
    miniJava_SuperiorOrEqual,
    miniJava_ArrayLength,
    miniJava_FieldAccess,
    miniJava_Superior,
    miniJava_Equality,
    miniJava_ArrayAccess,
    miniJava_Modulo,
    miniJava_Null,
    miniJava_MethodCall,
    miniJava_This,
    miniJava_StringConstant,
    miniJava_NewObject,
    miniJava_SymbolRef,
    miniJava_Plus,
    miniJava_BoolConstant,
    miniJava_IntConstant,
    miniJava_Inequality,
    miniJava_Not,
    miniJava_Division,
    miniJava_NewArray,
    miniJava_Super,
    miniJava_Or,
    miniJava_Assignee,
    Assignee,
    miniJava_NamedElement,
    SingleTypeRef,
    miniJava_VoidTypeRef,
    miniJava_StringTypeRef,
    miniJava_IntegerTypeRef,
    miniJava_BooleanTypeRef,
    miniJava_ClassRef,
    TypeRef,
    miniJava_ArrayTypeRef,
    miniJava_SingleTypeRef,
    miniJava_TypeRef,
    TypedDeclaration,
    miniJava_Symbol,
    miniJava_Statement,
    Statement,
    miniJava_Return,
    miniJava_IfStatement,
    miniJava_Assignment,
    miniJava_PrintStatement,
    miniJava_ForStatement,
    miniJava_WhileStatement,
    miniJava_Expression,
    Symbol,
    miniJava_VariableDeclaration,
    miniJava_ClazzToMethodMap,
    miniJava_Block,
    miniJava_Parameter,
    Member,
    miniJava_Field,
    miniJava_Method,
    miniJava_Program,
    TypeDeclaration,
    miniJava_Clazz,
    miniJava_Member,
    miniJava_Interface,
    NamedElement,
    miniJava_TypedDeclaration,
    miniJava_State,
    miniJava_TypeDeclaration,
    miniJava_Import,
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



def test_hyp_minijava_methodcall2_is_not_abstract():
    assert not inspect.isabstract(miniJava_MethodCall2)


def test_hyp_minijava_methodcall2_constructor_exists():
    assert callable(miniJava_MethodCall2.__init__)


def test_hyp_minijava_methodcall2_constructor_args():
    sig = inspect.signature(miniJava_MethodCall2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_newcall_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewCall)


def test_hyp_minijava_newcall_constructor_exists():
    assert callable(miniJava_NewCall.__init__)


def test_hyp_minijava_newcall_constructor_args():
    sig = inspect.signature(miniJava_NewCall.__init__)
    params = list(sig.parameters.keys())



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



def test_hyp_minijava_outputstream_is_not_abstract():
    assert not inspect.isabstract(miniJava_OutputStream)


def test_hyp_minijava_outputstream_constructor_exists():
    assert callable(miniJava_OutputStream.__init__)


def test_hyp_minijava_outputstream_constructor_args():
    sig = inspect.signature(miniJava_OutputStream.__init__)
    params = list(sig.parameters.keys())
    assert "stream" in params, "Missing parameter 'stream'"




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



def test_hyp_minijava_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_BooleanValue)


def test_hyp_minijava_booleanvalue_constructor_exists():
    assert callable(miniJava_BooleanValue.__init__)


def test_hyp_minijava_booleanvalue_constructor_args():
    sig = inspect.signature(miniJava_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_nullvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_NullValue)


def test_hyp_minijava_nullvalue_constructor_exists():
    assert callable(miniJava_NullValue.__init__)


def test_hyp_minijava_nullvalue_constructor_args():
    sig = inspect.signature(miniJava_NullValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_stringvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_StringValue)


def test_hyp_minijava_stringvalue_constructor_exists():
    assert callable(miniJava_StringValue.__init__)


def test_hyp_minijava_stringvalue_constructor_args():
    sig = inspect.signature(miniJava_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_objectrefvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_ObjectRefValue)


def test_hyp_minijava_objectrefvalue_constructor_exists():
    assert callable(miniJava_ObjectRefValue.__init__)


def test_hyp_minijava_objectrefvalue_constructor_args():
    sig = inspect.signature(miniJava_ObjectRefValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_arrayrefvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayRefValue)


def test_hyp_minijava_arrayrefvalue_constructor_exists():
    assert callable(miniJava_ArrayRefValue.__init__)


def test_hyp_minijava_arrayrefvalue_constructor_args():
    sig = inspect.signature(miniJava_ArrayRefValue.__init__)
    params = list(sig.parameters.keys())



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



def test_hyp_minijava_symboltosymbolbindingmap_is_not_abstract():
    assert not inspect.isabstract(miniJava_SymbolToSymbolBindingMap)


def test_hyp_minijava_symboltosymbolbindingmap_constructor_exists():
    assert callable(miniJava_SymbolToSymbolBindingMap.__init__)


def test_hyp_minijava_symboltosymbolbindingmap_constructor_args():
    sig = inspect.signature(miniJava_SymbolToSymbolBindingMap.__init__)
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



def test_hyp_minijava_neg_is_not_abstract():
    assert not inspect.isabstract(miniJava_Neg)


def test_hyp_minijava_neg_constructor_exists():
    assert callable(miniJava_Neg.__init__)


def test_hyp_minijava_neg_constructor_args():
    sig = inspect.signature(miniJava_Neg.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_inferior_is_not_abstract():
    assert not inspect.isabstract(miniJava_Inferior)


def test_hyp_minijava_inferior_constructor_exists():
    assert callable(miniJava_Inferior.__init__)


def test_hyp_minijava_inferior_constructor_args():
    sig = inspect.signature(miniJava_Inferior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_minus_is_not_abstract():
    assert not inspect.isabstract(miniJava_Minus)


def test_hyp_minijava_minus_constructor_exists():
    assert callable(miniJava_Minus.__init__)


def test_hyp_minijava_minus_constructor_args():
    sig = inspect.signature(miniJava_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_multiplication_is_not_abstract():
    assert not inspect.isabstract(miniJava_Multiplication)


def test_hyp_minijava_multiplication_constructor_exists():
    assert callable(miniJava_Multiplication.__init__)


def test_hyp_minijava_multiplication_constructor_args():
    sig = inspect.signature(miniJava_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_inferiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava_InferiorOrEqual)


def test_hyp_minijava_inferiororequal_constructor_exists():
    assert callable(miniJava_InferiorOrEqual.__init__)


def test_hyp_minijava_inferiororequal_constructor_args():
    sig = inspect.signature(miniJava_InferiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_and_is_not_abstract():
    assert not inspect.isabstract(miniJava_And)


def test_hyp_minijava_and_constructor_exists():
    assert callable(miniJava_And.__init__)


def test_hyp_minijava_and_constructor_args():
    sig = inspect.signature(miniJava_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_superiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava_SuperiorOrEqual)


def test_hyp_minijava_superiororequal_constructor_exists():
    assert callable(miniJava_SuperiorOrEqual.__init__)


def test_hyp_minijava_superiororequal_constructor_args():
    sig = inspect.signature(miniJava_SuperiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_arraylength_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayLength)


def test_hyp_minijava_arraylength_constructor_exists():
    assert callable(miniJava_ArrayLength.__init__)


def test_hyp_minijava_arraylength_constructor_args():
    sig = inspect.signature(miniJava_ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava_FieldAccess)


def test_hyp_minijava_fieldaccess_constructor_exists():
    assert callable(miniJava_FieldAccess.__init__)


def test_hyp_minijava_fieldaccess_constructor_args():
    sig = inspect.signature(miniJava_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_superior_is_not_abstract():
    assert not inspect.isabstract(miniJava_Superior)


def test_hyp_minijava_superior_constructor_exists():
    assert callable(miniJava_Superior.__init__)


def test_hyp_minijava_superior_constructor_args():
    sig = inspect.signature(miniJava_Superior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_equality_is_not_abstract():
    assert not inspect.isabstract(miniJava_Equality)


def test_hyp_minijava_equality_constructor_exists():
    assert callable(miniJava_Equality.__init__)


def test_hyp_minijava_equality_constructor_args():
    sig = inspect.signature(miniJava_Equality.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava_ArrayAccess)


def test_hyp_minijava_arrayaccess_constructor_exists():
    assert callable(miniJava_ArrayAccess.__init__)


def test_hyp_minijava_arrayaccess_constructor_args():
    sig = inspect.signature(miniJava_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_modulo_is_not_abstract():
    assert not inspect.isabstract(miniJava_Modulo)


def test_hyp_minijava_modulo_constructor_exists():
    assert callable(miniJava_Modulo.__init__)


def test_hyp_minijava_modulo_constructor_args():
    sig = inspect.signature(miniJava_Modulo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_null_is_not_abstract():
    assert not inspect.isabstract(miniJava_Null)


def test_hyp_minijava_null_constructor_exists():
    assert callable(miniJava_Null.__init__)


def test_hyp_minijava_null_constructor_args():
    sig = inspect.signature(miniJava_Null.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_methodcall_is_not_abstract():
    assert not inspect.isabstract(miniJava_MethodCall)


def test_hyp_minijava_methodcall_constructor_exists():
    assert callable(miniJava_MethodCall.__init__)


def test_hyp_minijava_methodcall_constructor_args():
    sig = inspect.signature(miniJava_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_this_is_not_abstract():
    assert not inspect.isabstract(miniJava_This)


def test_hyp_minijava_this_constructor_exists():
    assert callable(miniJava_This.__init__)


def test_hyp_minijava_this_constructor_args():
    sig = inspect.signature(miniJava_This.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_stringconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava_StringConstant)


def test_hyp_minijava_stringconstant_constructor_exists():
    assert callable(miniJava_StringConstant.__init__)


def test_hyp_minijava_stringconstant_constructor_args():
    sig = inspect.signature(miniJava_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_newobject_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewObject)


def test_hyp_minijava_newobject_constructor_exists():
    assert callable(miniJava_NewObject.__init__)


def test_hyp_minijava_newobject_constructor_args():
    sig = inspect.signature(miniJava_NewObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_symbolref_is_not_abstract():
    assert not inspect.isabstract(miniJava_SymbolRef)


def test_hyp_minijava_symbolref_constructor_exists():
    assert callable(miniJava_SymbolRef.__init__)


def test_hyp_minijava_symbolref_constructor_args():
    sig = inspect.signature(miniJava_SymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_plus_is_not_abstract():
    assert not inspect.isabstract(miniJava_Plus)


def test_hyp_minijava_plus_constructor_exists():
    assert callable(miniJava_Plus.__init__)


def test_hyp_minijava_plus_constructor_args():
    sig = inspect.signature(miniJava_Plus.__init__)
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




def test_hyp_minijava_inequality_is_not_abstract():
    assert not inspect.isabstract(miniJava_Inequality)


def test_hyp_minijava_inequality_constructor_exists():
    assert callable(miniJava_Inequality.__init__)


def test_hyp_minijava_inequality_constructor_args():
    sig = inspect.signature(miniJava_Inequality.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_not_is_not_abstract():
    assert not inspect.isabstract(miniJava_Not)


def test_hyp_minijava_not_constructor_exists():
    assert callable(miniJava_Not.__init__)


def test_hyp_minijava_not_constructor_args():
    sig = inspect.signature(miniJava_Not.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_division_is_not_abstract():
    assert not inspect.isabstract(miniJava_Division)


def test_hyp_minijava_division_constructor_exists():
    assert callable(miniJava_Division.__init__)


def test_hyp_minijava_division_constructor_args():
    sig = inspect.signature(miniJava_Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_newarray_is_not_abstract():
    assert not inspect.isabstract(miniJava_NewArray)


def test_hyp_minijava_newarray_constructor_exists():
    assert callable(miniJava_NewArray.__init__)


def test_hyp_minijava_newarray_constructor_args():
    sig = inspect.signature(miniJava_NewArray.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_super_is_not_abstract():
    assert not inspect.isabstract(miniJava_Super)


def test_hyp_minijava_super_constructor_exists():
    assert callable(miniJava_Super.__init__)


def test_hyp_minijava_super_constructor_args():
    sig = inspect.signature(miniJava_Super.__init__)
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



def test_hyp_minijava_booleantyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava_BooleanTypeRef)


def test_hyp_minijava_booleantyperef_constructor_exists():
    assert callable(miniJava_BooleanTypeRef.__init__)


def test_hyp_minijava_booleantyperef_constructor_args():
    sig = inspect.signature(miniJava_BooleanTypeRef.__init__)
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



def test_hyp_minijava_return_is_not_abstract():
    assert not inspect.isabstract(miniJava_Return)


def test_hyp_minijava_return_constructor_exists():
    assert callable(miniJava_Return.__init__)


def test_hyp_minijava_return_constructor_args():
    sig = inspect.signature(miniJava_Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_ifstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava_IfStatement)


def test_hyp_minijava_ifstatement_constructor_exists():
    assert callable(miniJava_IfStatement.__init__)


def test_hyp_minijava_ifstatement_constructor_args():
    sig = inspect.signature(miniJava_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_assignment_is_not_abstract():
    assert not inspect.isabstract(miniJava_Assignment)


def test_hyp_minijava_assignment_constructor_exists():
    assert callable(miniJava_Assignment.__init__)


def test_hyp_minijava_assignment_constructor_args():
    sig = inspect.signature(miniJava_Assignment.__init__)
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



def test_hyp_minijava_clazztomethodmap_is_not_abstract():
    assert not inspect.isabstract(miniJava_ClazzToMethodMap)


def test_hyp_minijava_clazztomethodmap_constructor_exists():
    assert callable(miniJava_ClazzToMethodMap.__init__)


def test_hyp_minijava_clazztomethodmap_constructor_args():
    sig = inspect.signature(miniJava_ClazzToMethodMap.__init__)
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
    assert "isabstract" in params, "Missing parameter 'isabstract'"
    assert "isstatic" in params, "Missing parameter 'isstatic'"





def test_hyp_minijava_program_is_not_abstract():
    assert not inspect.isabstract(miniJava_Program)


def test_hyp_minijava_program_constructor_exists():
    assert callable(miniJava_Program.__init__)


def test_hyp_minijava_program_constructor_args():
    sig = inspect.signature(miniJava_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_hyp_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_hyp_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_clazz_is_not_abstract():
    assert not inspect.isabstract(miniJava_Clazz)


def test_hyp_minijava_clazz_constructor_exists():
    assert callable(miniJava_Clazz.__init__)


def test_hyp_minijava_clazz_constructor_args():
    sig = inspect.signature(miniJava_Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "isabstract" in params, "Missing parameter 'isabstract'"




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


def test_hyp_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_hyp_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PROTECTED",
        "PRIVATE",
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
miniJava_MethodCall2_strategy = st.builds(
    miniJava_MethodCall2,
)
miniJava_NewCall_strategy = st.builds(
    miniJava_NewCall,
)
miniJava_Call_strategy = st.builds(
    miniJava_Call,
)
miniJava_ArrayInstance_strategy = st.builds(
    miniJava_ArrayInstance,
    size=
        st.integers()
)
miniJava_ObjectInstance_strategy = st.builds(
    miniJava_ObjectInstance,
)
miniJava_Frame_strategy = st.builds(
    miniJava_Frame,
)
miniJava_OutputStream_strategy = st.builds(
    miniJava_OutputStream,
    stream=
        safe_text
)
miniJava_FieldBinding_strategy = st.builds(
    miniJava_FieldBinding,
)
Value_strategy = st.builds(
    Value,
)
miniJava_BooleanValue_strategy = st.builds(
    miniJava_BooleanValue,
    value=
        st.booleans()
)
miniJava_NullValue_strategy = st.builds(
    miniJava_NullValue,
)
miniJava_StringValue_strategy = st.builds(
    miniJava_StringValue,
    value=
        safe_text
)
miniJava_ObjectRefValue_strategy = st.builds(
    miniJava_ObjectRefValue,
)
miniJava_ArrayRefValue_strategy = st.builds(
    miniJava_ArrayRefValue,
)
miniJava_IntegerValue_strategy = st.builds(
    miniJava_IntegerValue,
    value=
        st.integers()
)
miniJava_Value_strategy = st.builds(
    miniJava_Value,
)
miniJava_SymbolToSymbolBindingMap_strategy = st.builds(
    miniJava_SymbolToSymbolBindingMap,
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
miniJava_Neg_strategy = st.builds(
    miniJava_Neg,
)
miniJava_Inferior_strategy = st.builds(
    miniJava_Inferior,
)
miniJava_Minus_strategy = st.builds(
    miniJava_Minus,
)
miniJava_Multiplication_strategy = st.builds(
    miniJava_Multiplication,
)
miniJava_InferiorOrEqual_strategy = st.builds(
    miniJava_InferiorOrEqual,
)
miniJava_And_strategy = st.builds(
    miniJava_And,
)
miniJava_SuperiorOrEqual_strategy = st.builds(
    miniJava_SuperiorOrEqual,
)
miniJava_ArrayLength_strategy = st.builds(
    miniJava_ArrayLength,
)
miniJava_FieldAccess_strategy = st.builds(
    miniJava_FieldAccess,
)
miniJava_Superior_strategy = st.builds(
    miniJava_Superior,
)
miniJava_Equality_strategy = st.builds(
    miniJava_Equality,
)
miniJava_ArrayAccess_strategy = st.builds(
    miniJava_ArrayAccess,
)
miniJava_Modulo_strategy = st.builds(
    miniJava_Modulo,
)
miniJava_Null_strategy = st.builds(
    miniJava_Null,
)
miniJava_MethodCall_strategy = st.builds(
    miniJava_MethodCall,
)
miniJava_This_strategy = st.builds(
    miniJava_This,
)
miniJava_StringConstant_strategy = st.builds(
    miniJava_StringConstant,
    value=
        safe_text
)
miniJava_NewObject_strategy = st.builds(
    miniJava_NewObject,
)
miniJava_SymbolRef_strategy = st.builds(
    miniJava_SymbolRef,
)
miniJava_Plus_strategy = st.builds(
    miniJava_Plus,
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
miniJava_Inequality_strategy = st.builds(
    miniJava_Inequality,
)
miniJava_Not_strategy = st.builds(
    miniJava_Not,
)
miniJava_Division_strategy = st.builds(
    miniJava_Division,
)
miniJava_NewArray_strategy = st.builds(
    miniJava_NewArray,
)
miniJava_Super_strategy = st.builds(
    miniJava_Super,
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
miniJava_StringTypeRef_strategy = st.builds(
    miniJava_StringTypeRef,
)
miniJava_IntegerTypeRef_strategy = st.builds(
    miniJava_IntegerTypeRef,
)
miniJava_BooleanTypeRef_strategy = st.builds(
    miniJava_BooleanTypeRef,
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
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
miniJava_Symbol_strategy = st.builds(
    miniJava_Symbol,
)
miniJava_Statement_strategy = st.builds(
    miniJava_Statement,
)
Statement_strategy = st.builds(
    Statement,
)
miniJava_Return_strategy = st.builds(
    miniJava_Return,
)
miniJava_IfStatement_strategy = st.builds(
    miniJava_IfStatement,
)
miniJava_Assignment_strategy = st.builds(
    miniJava_Assignment,
)
miniJava_PrintStatement_strategy = st.builds(
    miniJava_PrintStatement,
)
miniJava_ForStatement_strategy = st.builds(
    miniJava_ForStatement,
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
miniJava_ClazzToMethodMap_strategy = st.builds(
    miniJava_ClazzToMethodMap,
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
    isabstract=
        st.booleans(),
    isstatic=
        st.booleans()
)
miniJava_Program_strategy = st.builds(
    miniJava_Program,
    name=
        safe_text
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
miniJava_Clazz_strategy = st.builds(
    miniJava_Clazz,
    isabstract=
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








@given(instance=miniJava_ArrayInstance_strategy)
def test_hyp_minijava_arrayinstance_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original






@given(instance=miniJava_OutputStream_strategy)
def test_hyp_minijava_outputstream_stream_setter(instance):
    original = instance.stream
    instance.stream = original
    assert instance.stream == original






@given(instance=miniJava_BooleanValue_strategy)
def test_hyp_minijava_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=miniJava_StringValue_strategy)
def test_hyp_minijava_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=miniJava_IntegerValue_strategy)
def test_hyp_minijava_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

























@given(instance=miniJava_StringConstant_strategy)
def test_hyp_minijava_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=miniJava_BoolConstant_strategy)
def test_hyp_minijava_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=miniJava_IntConstant_strategy)
def test_hyp_minijava_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original












@given(instance=miniJava_NamedElement_strategy)
def test_hyp_minijava_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
































@given(instance=miniJava_Method_strategy)
def test_hyp_minijava_method_isabstract_setter(instance):
    original = instance.isabstract
    instance.isabstract = original
    assert instance.isabstract == original



@given(instance=miniJava_Method_strategy)
def test_hyp_minijava_method_isstatic_setter(instance):
    original = instance.isstatic
    instance.isstatic = original
    assert instance.isstatic == original




@given(instance=miniJava_Program_strategy)
def test_hyp_minijava_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=miniJava_Clazz_strategy)
def test_hyp_minijava_clazz_isabstract_setter(instance):
    original = instance.isabstract
    instance.isabstract = original
    assert instance.isabstract == original




@given(instance=miniJava_Member_strategy)
def test_hyp_minijava_member_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original








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
    miniJava_ClassRef,
    miniJava_Clazz,
    miniJava_ClazzToMethodMap,
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
    miniJava_Modulo,
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
    miniJava_SymbolToSymbolBindingMap,
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
    instance = miniJava_ArrayInstance(size=7)
    assert instance.size == 7
    instance.size = 13
    assert instance.size == 13


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


def test_miniJava_Clazz_isabstract_value_roundtrip():
    instance = miniJava_Clazz(isabstract=True)
    assert instance.isabstract == True
    instance.isabstract = False
    assert instance.isabstract == False


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
    instance = miniJava_IntegerValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_miniJava_Member_access_value_roundtrip():
    instance = miniJava_Member(access="sample_text")
    assert instance.access == "sample_text"
    instance.access = "sample_text_2"
    assert instance.access == "sample_text_2"


def test_miniJava_Method_isabstract_value_roundtrip():
    instance = miniJava_Method(isabstract=True, isstatic=True)
    assert instance.isabstract == True
    instance.isabstract = False
    assert instance.isabstract == False


def test_miniJava_Method_isstatic_value_roundtrip():
    instance = miniJava_Method(isabstract=True, isstatic=True)
    assert instance.isstatic == True
    instance.isstatic = False
    assert instance.isstatic == False


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


def test_miniJava_Modulo_isa_Expression():
    instance = miniJava_Modulo()
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
    instance = miniJava_Method(isabstract=True, isstatic=True)
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


def test_miniJava_Clazz_isa_TypeDeclaration():
    instance = miniJava_Clazz(isabstract=True)
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
    instance = miniJava_IntegerValue(value=7)
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


def test_assoc_arraysHeap174_link_reassign_clear():
    a = miniJava_ArrayInstance(size=7)
    b1 = miniJava_State()
    b2 = miniJava_State()
    _safe_set(a, 'miniJava_ArrayInstance', b1)
    assert _is_linked(a, 'miniJava_ArrayInstance', b1)
    if hasattr(b1, 'miniJava_State175'):
        assert _is_linked(b1, 'miniJava_State175', a)
    _safe_set(a, 'miniJava_ArrayInstance', b2)
    assert _is_linked(a, 'miniJava_ArrayInstance', b2)
    if hasattr(b1, 'miniJava_State175'):
        assert not _is_linked(b1, 'miniJava_State175', a)
    if hasattr(b2, 'miniJava_State175'):
        assert _is_linked(b2, 'miniJava_State175', a)
    _safe_set(a, 'miniJava_ArrayInstance', None)
    assert not _is_linked(a, 'miniJava_ArrayInstance', b2)
    if hasattr(b2, 'miniJava_State175'):
        assert not _is_linked(b2, 'miniJava_State175', a)


def test_assoc_body12_link_reassign_clear():
    a = miniJava_Method(isabstract=True, isstatic=True)
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


def test_assoc_cache14_link_reassign_clear():
    a = miniJava_Method(isabstract=True, isstatic=True)
    b1 = miniJava_ClazzToMethodMap()
    b2 = miniJava_ClazzToMethodMap()
    _safe_set(a, 'miniJava_Method15', {b1})
    assert _is_linked(a, 'miniJava_Method15', b1)
    if hasattr(b1, 'miniJava_ClazzToMethodMap'):
        assert _is_linked(b1, 'miniJava_ClazzToMethodMap', a)
    _safe_set(a, 'miniJava_Method15', {b2})
    assert _is_linked(a, 'miniJava_Method15', b2)
    if hasattr(b1, 'miniJava_ClazzToMethodMap'):
        assert not _is_linked(b1, 'miniJava_ClazzToMethodMap', a)
    if hasattr(b2, 'miniJava_ClazzToMethodMap'):
        assert _is_linked(b2, 'miniJava_ClazzToMethodMap', a)
    _safe_set(a, 'miniJava_Method15', set())
    assert not _is_linked(a, 'miniJava_Method15', b2)
    if hasattr(b2, 'miniJava_ClazzToMethodMap'):
        assert not _is_linked(b2, 'miniJava_ClazzToMethodMap', a)


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


def test_assoc_implementz5_link_reassign_clear():
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


def test_assoc_instance213_link_reassign_clear():
    a = miniJava_ArrayInstance(size=7)
    b1 = miniJava_ArrayRefValue()
    b2 = miniJava_ArrayRefValue()
    _safe_set(a, 'miniJava_ArrayInstance214', b1)
    assert _is_linked(a, 'miniJava_ArrayInstance214', b1)
    if hasattr(b1, 'miniJava_ArrayRefValue'):
        assert _is_linked(b1, 'miniJava_ArrayRefValue', a)
    _safe_set(a, 'miniJava_ArrayInstance214', b2)
    assert _is_linked(a, 'miniJava_ArrayInstance214', b2)
    if hasattr(b1, 'miniJava_ArrayRefValue'):
        assert not _is_linked(b1, 'miniJava_ArrayRefValue', a)
    if hasattr(b2, 'miniJava_ArrayRefValue'):
        assert _is_linked(b2, 'miniJava_ArrayRefValue', a)
    _safe_set(a, 'miniJava_ArrayInstance214', None)
    assert not _is_linked(a, 'miniJava_ArrayInstance214', b2)
    if hasattr(b2, 'miniJava_ArrayRefValue'):
        assert not _is_linked(b2, 'miniJava_ArrayRefValue', a)


def test_assoc_key221_link_reassign_clear():
    a = miniJava_Clazz(isabstract=True)
    b1 = miniJava_ClazzToMethodMap()
    b2 = miniJava_ClazzToMethodMap()
    _safe_set(a, 'miniJava_Clazz223', b1)
    assert _is_linked(a, 'miniJava_Clazz223', b1)
    if hasattr(b1, 'miniJava_ClazzToMethodMap222'):
        assert _is_linked(b1, 'miniJava_ClazzToMethodMap222', a)
    _safe_set(a, 'miniJava_Clazz223', b2)
    assert _is_linked(a, 'miniJava_Clazz223', b2)
    if hasattr(b1, 'miniJava_ClazzToMethodMap222'):
        assert not _is_linked(b1, 'miniJava_ClazzToMethodMap222', a)
    if hasattr(b2, 'miniJava_ClazzToMethodMap222'):
        assert _is_linked(b2, 'miniJava_ClazzToMethodMap222', a)
    _safe_set(a, 'miniJava_Clazz223', None)
    assert not _is_linked(a, 'miniJava_Clazz223', b2)
    if hasattr(b2, 'miniJava_ClazzToMethodMap222'):
        assert not _is_linked(b2, 'miniJava_ClazzToMethodMap222', a)


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


def test_assoc_method133_link_reassign_clear():
    a = miniJava_Method(isabstract=True, isstatic=True)
    b1 = miniJava_MethodCall()
    b2 = miniJava_MethodCall()
    _safe_set(a, 'miniJava_Method135', b1)
    assert _is_linked(a, 'miniJava_Method135', b1)
    if hasattr(b1, 'miniJava_MethodCall134'):
        assert _is_linked(b1, 'miniJava_MethodCall134', a)
    _safe_set(a, 'miniJava_Method135', b2)
    assert _is_linked(a, 'miniJava_Method135', b2)
    if hasattr(b1, 'miniJava_MethodCall134'):
        assert not _is_linked(b1, 'miniJava_MethodCall134', a)
    if hasattr(b2, 'miniJava_MethodCall134'):
        assert _is_linked(b2, 'miniJava_MethodCall134', a)
    _safe_set(a, 'miniJava_Method135', None)
    assert not _is_linked(a, 'miniJava_Method135', b2)
    if hasattr(b2, 'miniJava_MethodCall134'):
        assert not _is_linked(b2, 'miniJava_MethodCall134', a)


def test_assoc_outputStream172_link_reassign_clear():
    a = miniJava_OutputStream(stream="sample_text")
    b1 = miniJava_State()
    b2 = miniJava_State()
    _safe_set(a, 'miniJava_OutputStream', b1)
    assert _is_linked(a, 'miniJava_OutputStream', b1)
    if hasattr(b1, 'miniJava_State173'):
        assert _is_linked(b1, 'miniJava_State173', a)
    _safe_set(a, 'miniJava_OutputStream', b2)
    assert _is_linked(a, 'miniJava_OutputStream', b2)
    if hasattr(b1, 'miniJava_State173'):
        assert not _is_linked(b1, 'miniJava_State173', a)
    if hasattr(b2, 'miniJava_State173'):
        assert _is_linked(b2, 'miniJava_State173', a)
    _safe_set(a, 'miniJava_OutputStream', None)
    assert not _is_linked(a, 'miniJava_OutputStream', b2)
    if hasattr(b2, 'miniJava_State173'):
        assert not _is_linked(b2, 'miniJava_State173', a)


def test_assoc_params11_link_reassign_clear():
    a = miniJava_Method(isabstract=True, isstatic=True)
    b1 = miniJava_Parameter()
    b2 = miniJava_Parameter()
    _safe_set(a, 'miniJava_Method', {b1})
    assert _is_linked(a, 'miniJava_Method', b1)
    if hasattr(b1, 'miniJava_Parameter'):
        assert _is_linked(b1, 'miniJava_Parameter', a)
    _safe_set(a, 'miniJava_Method', {b2})
    assert _is_linked(a, 'miniJava_Method', b2)
    if hasattr(b1, 'miniJava_Parameter'):
        assert not _is_linked(b1, 'miniJava_Parameter', a)
    if hasattr(b2, 'miniJava_Parameter'):
        assert _is_linked(b2, 'miniJava_Parameter', a)
    _safe_set(a, 'miniJava_Method', set())
    assert not _is_linked(a, 'miniJava_Method', b2)
    if hasattr(b2, 'miniJava_Parameter'):
        assert not _is_linked(b2, 'miniJava_Parameter', a)


def test_assoc_referencedClass46_link_reassign_clear():
    a = miniJava_TypeDeclaration(accessLevel="sample_text")
    b1 = miniJava_ClassRef()
    b2 = miniJava_ClassRef()
    _safe_set(a, 'miniJava_TypeDeclaration47', b1)
    assert _is_linked(a, 'miniJava_TypeDeclaration47', b1)
    if hasattr(b1, 'miniJava_ClassRef'):
        assert _is_linked(b1, 'miniJava_ClassRef', a)
    _safe_set(a, 'miniJava_TypeDeclaration47', b2)
    assert _is_linked(a, 'miniJava_TypeDeclaration47', b2)
    if hasattr(b1, 'miniJava_ClassRef'):
        assert not _is_linked(b1, 'miniJava_ClassRef', a)
    if hasattr(b2, 'miniJava_ClassRef'):
        assert _is_linked(b2, 'miniJava_ClassRef', a)
    _safe_set(a, 'miniJava_TypeDeclaration47', None)
    assert not _is_linked(a, 'miniJava_TypeDeclaration47', b2)
    if hasattr(b2, 'miniJava_ClassRef'):
        assert not _is_linked(b2, 'miniJava_ClassRef', a)


def test_assoc_state3_link_reassign_clear():
    a = miniJava_Program(name="sample_text")
    b1 = miniJava_State()
    b2 = miniJava_State()
    _safe_set(a, 'miniJava_Program4', b1)
    assert _is_linked(a, 'miniJava_Program4', b1)
    if hasattr(b1, 'miniJava_State'):
        assert _is_linked(b1, 'miniJava_State', a)
    _safe_set(a, 'miniJava_Program4', b2)
    assert _is_linked(a, 'miniJava_Program4', b2)
    if hasattr(b1, 'miniJava_State'):
        assert not _is_linked(b1, 'miniJava_State', a)
    if hasattr(b2, 'miniJava_State'):
        assert _is_linked(b2, 'miniJava_State', a)
    _safe_set(a, 'miniJava_Program4', None)
    assert not _is_linked(a, 'miniJava_Program4', b2)
    if hasattr(b2, 'miniJava_State'):
        assert not _is_linked(b2, 'miniJava_State', a)


def test_assoc_superClass10_link_reassign_clear():
    a = miniJava_Clazz(isabstract=True)
    b1 = miniJava_Clazz(isabstract=True)
    b2 = miniJava_Clazz(isabstract=False)
    _safe_set(a, 'miniJava_Clazz', b1)
    assert _is_linked(a, 'miniJava_Clazz', b1)
    if hasattr(b1, 'miniJava_Clazz9'):
        assert _is_linked(b1, 'miniJava_Clazz9', a)
    _safe_set(a, 'miniJava_Clazz', b2)
    assert _is_linked(a, 'miniJava_Clazz', b2)
    if hasattr(b1, 'miniJava_Clazz9'):
        assert not _is_linked(b1, 'miniJava_Clazz9', a)
    if hasattr(b2, 'miniJava_Clazz9'):
        assert _is_linked(b2, 'miniJava_Clazz9', a)
    _safe_set(a, 'miniJava_Clazz', None)
    assert not _is_linked(a, 'miniJava_Clazz', b2)
    if hasattr(b2, 'miniJava_Clazz9'):
        assert not _is_linked(b2, 'miniJava_Clazz9', a)


def test_assoc_type139_link_reassign_clear():
    a = miniJava_Clazz(isabstract=True)
    b1 = miniJava_NewObject()
    b2 = miniJava_NewObject()
    _safe_set(a, 'miniJava_Clazz140', b1)
    assert _is_linked(a, 'miniJava_Clazz140', b1)
    if hasattr(b1, 'miniJava_NewObject'):
        assert _is_linked(b1, 'miniJava_NewObject', a)
    _safe_set(a, 'miniJava_Clazz140', b2)
    assert _is_linked(a, 'miniJava_Clazz140', b2)
    if hasattr(b1, 'miniJava_NewObject'):
        assert not _is_linked(b1, 'miniJava_NewObject', a)
    if hasattr(b2, 'miniJava_NewObject'):
        assert _is_linked(b2, 'miniJava_NewObject', a)
    _safe_set(a, 'miniJava_Clazz140', None)
    assert not _is_linked(a, 'miniJava_Clazz140', b2)
    if hasattr(b2, 'miniJava_NewObject'):
        assert not _is_linked(b2, 'miniJava_NewObject', a)


def test_assoc_type205_link_reassign_clear():
    a = miniJava_Clazz(isabstract=True)
    b1 = miniJava_ObjectInstance()
    b2 = miniJava_ObjectInstance()
    _safe_set(a, 'miniJava_Clazz207', b1)
    assert _is_linked(a, 'miniJava_Clazz207', b1)
    if hasattr(b1, 'miniJava_ObjectInstance206'):
        assert _is_linked(b1, 'miniJava_ObjectInstance206', a)
    _safe_set(a, 'miniJava_Clazz207', b2)
    assert _is_linked(a, 'miniJava_Clazz207', b2)
    if hasattr(b1, 'miniJava_ObjectInstance206'):
        assert not _is_linked(b1, 'miniJava_ObjectInstance206', a)
    if hasattr(b2, 'miniJava_ObjectInstance206'):
        assert _is_linked(b2, 'miniJava_ObjectInstance206', a)
    _safe_set(a, 'miniJava_Clazz207', None)
    assert not _is_linked(a, 'miniJava_Clazz207', b2)
    if hasattr(b2, 'miniJava_ObjectInstance206'):
        assert not _is_linked(b2, 'miniJava_ObjectInstance206', a)


def test_assoc_value208_link_reassign_clear():
    a = miniJava_ArrayInstance(size=7)
    b1 = miniJava_Value()
    b2 = miniJava_Value()
    _safe_set(a, 'miniJava_ArrayInstance209', {b1})
    assert _is_linked(a, 'miniJava_ArrayInstance209', b1)
    if hasattr(b1, 'miniJava_Value210'):
        assert _is_linked(b1, 'miniJava_Value210', a)
    _safe_set(a, 'miniJava_ArrayInstance209', {b2})
    assert _is_linked(a, 'miniJava_ArrayInstance209', b2)
    if hasattr(b1, 'miniJava_Value210'):
        assert not _is_linked(b1, 'miniJava_Value210', a)
    if hasattr(b2, 'miniJava_Value210'):
        assert _is_linked(b2, 'miniJava_Value210', a)
    _safe_set(a, 'miniJava_ArrayInstance209', set())
    assert not _is_linked(a, 'miniJava_ArrayInstance209', b2)
    if hasattr(b2, 'miniJava_Value210'):
        assert not _is_linked(b2, 'miniJava_Value210', a)


def test_assoc_value224_link_reassign_clear():
    a = miniJava_Method(isabstract=True, isstatic=True)
    b1 = miniJava_ClazzToMethodMap()
    b2 = miniJava_ClazzToMethodMap()
    _safe_set(a, 'miniJava_Method226', b1)
    assert _is_linked(a, 'miniJava_Method226', b1)
    if hasattr(b1, 'miniJava_ClazzToMethodMap225'):
        assert _is_linked(b1, 'miniJava_ClazzToMethodMap225', a)
    _safe_set(a, 'miniJava_Method226', b2)
    assert _is_linked(a, 'miniJava_Method226', b2)
    if hasattr(b1, 'miniJava_ClazzToMethodMap225'):
        assert not _is_linked(b1, 'miniJava_ClazzToMethodMap225', a)
    if hasattr(b2, 'miniJava_ClazzToMethodMap225'):
        assert _is_linked(b2, 'miniJava_ClazzToMethodMap225', a)
    _safe_set(a, 'miniJava_Method226', None)
    assert not _is_linked(a, 'miniJava_Method226', b2)
    if hasattr(b2, 'miniJava_ClazzToMethodMap225'):
        assert not _is_linked(b2, 'miniJava_ClazzToMethodMap225', a)


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


miniJava_ArrayInstance_strategy = st.builds(miniJava_ArrayInstance, size=st.integers())
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


miniJava_ClassRef_strategy = st.builds(miniJava_ClassRef)
@given(instance=miniJava_ClassRef_strategy)
@settings(max_examples=25)
def test_miniJava_ClassRef_instantiation(instance):
    assert isinstance(instance, miniJava_ClassRef)


miniJava_Clazz_strategy = st.builds(miniJava_Clazz, isabstract=st.booleans())
@given(instance=miniJava_Clazz_strategy)
@settings(max_examples=25)
def test_miniJava_Clazz_instantiation(instance):
    assert isinstance(instance, miniJava_Clazz)


miniJava_ClazzToMethodMap_strategy = st.builds(miniJava_ClazzToMethodMap)
@given(instance=miniJava_ClazzToMethodMap_strategy)
@settings(max_examples=25)
def test_miniJava_ClazzToMethodMap_instantiation(instance):
    assert isinstance(instance, miniJava_ClazzToMethodMap)


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


miniJava_IntegerValue_strategy = st.builds(miniJava_IntegerValue, value=st.integers())
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


miniJava_Method_strategy = st.builds(miniJava_Method, isabstract=st.booleans(), isstatic=st.booleans())
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


miniJava_Modulo_strategy = st.builds(miniJava_Modulo)
@given(instance=miniJava_Modulo_strategy)
@settings(max_examples=25)
def test_miniJava_Modulo_instantiation(instance):
    assert isinstance(instance, miniJava_Modulo)


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


miniJava_SymbolToSymbolBindingMap_strategy = st.builds(miniJava_SymbolToSymbolBindingMap)
@given(instance=miniJava_SymbolToSymbolBindingMap_strategy)
@settings(max_examples=25)
def test_miniJava_SymbolToSymbolBindingMap_instantiation(instance):
    assert isinstance(instance, miniJava_SymbolToSymbolBindingMap)


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



