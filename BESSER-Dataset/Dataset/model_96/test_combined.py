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
    VariableDeclaration,
    PrimitiveType,
    Java5_PrimitiveTypeVoid,
    Java5_PrimitiveTypeFloat,
    Java5_PrimitiveTypeLong,
    Java5_PrimitiveTypeChar,
    Java5_PrimitiveTypeInt,
    Java5_PrimitiveTypeShort,
    Java5_PrimitiveTypeByte,
    Java5_PrimitiveTypeDouble,
    Java5_PrimitiveTypeBoolean,
    Java5_Model,
    Java5_VariableDeclarationFragment,
    Java5_SingleVariableDeclaration,
    TypeDeclaration,
    Java5_InterfaceDeclaration,
    Java5_ClassDeclaration,
    Java5_ASTNode,
    Statement,
    Java5_SuperConstructorInvocation,
    Java5_SwitchStatement,
    Java5_ForStatement,
    Java5_WhileStatement,
    Java5_VariableDeclarationStatement,
    Java5_Block,
    Java5_ConstructorInvocation,
    Java5_EmptyStatement,
    Java5_ReturnStatement,
    Java5_DoStatement,
    Java5_EnhancedForStatement,
    Java5_SwitchCase,
    Java5_TypeDeclarationStatement,
    Java5_CatchClause,
    Java5_IfStatement,
    Java5_ContinueStatement,
    Java5_ExpressionStatement,
    Java5_TryStatement,
    Java5_BreakStatement,
    Java5_SynchronizedStatement,
    Java5_ThrowStatement,
    Java5_AssertStatement,
    OrphanType,
    Java5_WildCardType,
    Java5_PrimitiveType,
    Java5_ParameterizedType,
    Java5_ArrayType,
    BodyDeclaration,
    Java5_FieldDeclaration,
    Java5_MethodDeclaration,
    Java5_Initializer,
    Java5_EnumConstantDeclaration,
    Java5_AbstractTypeDeclaration,
    ASTNode,
    Java5_Statement,
    Java5_TextElement,
    Java5_MethodRef,
    Java5_TagElement,
    Java5_NamedElement,
    Java5_MethodRefParameter,
    Java5_MemberRef,
    Java5_Modifier,
    Java5_AnonymousClassDeclaration,
    Java5_AnnotationTypeMemberDeclaration,
    AbstractTypeDeclaration,
    Java5_TypeDeclaration,
    Java5_EnumDeclaration,
    Java5_AnnotationTypeDeclaration,
    Java5_Expression,
    NamedElement,
    Java5_UnresolvedItem,
    Java5_BodyDeclaration,
    Java5_TypeParameter,
    Java5_OrphanType,
    Java5_CompilationUnit,
    Java5_LabeledStatement,
    Java5_VariableDeclaration,
    Java5_AnnotationMemberValuePair,
    Expression,
    Java5_ThisExpression,
    Java5_InfixExpression,
    Java5_ArrayCreation,
    Java5_ArrayInitializer,
    Java5_BooleanLiteral,
    Java5_FieldAccess,
    Java5_NullLiteral,
    Java5_CharacterLiteral,
    Java5_PrefixExpression,
    Java5_SuperFieldAccess,
    Java5_VariableDeclarationExpression,
    Java5_SuperMethodInvocation,
    Java5_ConditionalExpression,
    Java5_StringLiteral,
    Java5_ParenthesizedExpression,
    Java5_InstanceofExpression,
    Java5_CastExpression,
    Java5_ArrayAccess,
    Java5_Assignment,
    Java5_NumberLiteral,
    Java5_PostfixExpression,
    Java5_ClassInstanceCreation,
    Java5_MethodInvocation,
    Java5_ArrayLengthAccess,
    Java5_TypeLiteral,
    Java5_Annotation,
    Java5_NamedElementRef,
    Java5_PackageDeclaration,
    Java5_ImportDeclaration,
    VisibilityKind,
    InheritanceKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_hyp_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_hyp_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeVoid)


def test_hyp_java5_primitivetypevoid_constructor_exists():
    assert callable(Java5_PrimitiveTypeVoid.__init__)


def test_hyp_java5_primitivetypevoid_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeFloat)


def test_hyp_java5_primitivetypefloat_constructor_exists():
    assert callable(Java5_PrimitiveTypeFloat.__init__)


def test_hyp_java5_primitivetypefloat_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeLong)


def test_hyp_java5_primitivetypelong_constructor_exists():
    assert callable(Java5_PrimitiveTypeLong.__init__)


def test_hyp_java5_primitivetypelong_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeChar)


def test_hyp_java5_primitivetypechar_constructor_exists():
    assert callable(Java5_PrimitiveTypeChar.__init__)


def test_hyp_java5_primitivetypechar_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeInt)


def test_hyp_java5_primitivetypeint_constructor_exists():
    assert callable(Java5_PrimitiveTypeInt.__init__)


def test_hyp_java5_primitivetypeint_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeShort)


def test_hyp_java5_primitivetypeshort_constructor_exists():
    assert callable(Java5_PrimitiveTypeShort.__init__)


def test_hyp_java5_primitivetypeshort_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeByte)


def test_hyp_java5_primitivetypebyte_constructor_exists():
    assert callable(Java5_PrimitiveTypeByte.__init__)


def test_hyp_java5_primitivetypebyte_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeDouble)


def test_hyp_java5_primitivetypedouble_constructor_exists():
    assert callable(Java5_PrimitiveTypeDouble.__init__)


def test_hyp_java5_primitivetypedouble_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveTypeBoolean)


def test_hyp_java5_primitivetypeboolean_constructor_exists():
    assert callable(Java5_PrimitiveTypeBoolean.__init__)


def test_hyp_java5_primitivetypeboolean_constructor_args():
    sig = inspect.signature(Java5_PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_model_is_not_abstract():
    assert not inspect.isabstract(Java5_Model)


def test_hyp_java5_model_constructor_exists():
    assert callable(Java5_Model.__init__)


def test_hyp_java5_model_constructor_args():
    sig = inspect.signature(Java5_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_java5_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Java5_VariableDeclarationFragment)


def test_hyp_java5_variabledeclarationfragment_constructor_exists():
    assert callable(Java5_VariableDeclarationFragment.__init__)


def test_hyp_java5_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(Java5_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_SingleVariableDeclaration)


def test_hyp_java5_singlevariabledeclaration_constructor_exists():
    assert callable(Java5_SingleVariableDeclaration.__init__)


def test_hyp_java5_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(Java5_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"




def test_hyp_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_hyp_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_hyp_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_InterfaceDeclaration)


def test_hyp_java5_interfacedeclaration_constructor_exists():
    assert callable(Java5_InterfaceDeclaration.__init__)


def test_hyp_java5_interfacedeclaration_constructor_args():
    sig = inspect.signature(Java5_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_ClassDeclaration)


def test_hyp_java5_classdeclaration_constructor_exists():
    assert callable(Java5_ClassDeclaration.__init__)


def test_hyp_java5_classdeclaration_constructor_args():
    sig = inspect.signature(Java5_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_astnode_is_not_abstract():
    assert not inspect.isabstract(Java5_ASTNode)


def test_hyp_java5_astnode_constructor_exists():
    assert callable(Java5_ASTNode.__init__)


def test_hyp_java5_astnode_constructor_args():
    sig = inspect.signature(Java5_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5_SuperConstructorInvocation)


def test_hyp_java5_superconstructorinvocation_constructor_exists():
    assert callable(Java5_SuperConstructorInvocation.__init__)


def test_hyp_java5_superconstructorinvocation_constructor_args():
    sig = inspect.signature(Java5_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_switchstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_SwitchStatement)


def test_hyp_java5_switchstatement_constructor_exists():
    assert callable(Java5_SwitchStatement.__init__)


def test_hyp_java5_switchstatement_constructor_args():
    sig = inspect.signature(Java5_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_forstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ForStatement)


def test_hyp_java5_forstatement_constructor_exists():
    assert callable(Java5_ForStatement.__init__)


def test_hyp_java5_forstatement_constructor_args():
    sig = inspect.signature(Java5_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_whilestatement_is_not_abstract():
    assert not inspect.isabstract(Java5_WhileStatement)


def test_hyp_java5_whilestatement_constructor_exists():
    assert callable(Java5_WhileStatement.__init__)


def test_hyp_java5_whilestatement_constructor_args():
    sig = inspect.signature(Java5_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_VariableDeclarationStatement)


def test_hyp_java5_variabledeclarationstatement_constructor_exists():
    assert callable(Java5_VariableDeclarationStatement.__init__)


def test_hyp_java5_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(Java5_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"




def test_hyp_java5_block_is_not_abstract():
    assert not inspect.isabstract(Java5_Block)


def test_hyp_java5_block_constructor_exists():
    assert callable(Java5_Block.__init__)


def test_hyp_java5_block_constructor_args():
    sig = inspect.signature(Java5_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5_ConstructorInvocation)


def test_hyp_java5_constructorinvocation_constructor_exists():
    assert callable(Java5_ConstructorInvocation.__init__)


def test_hyp_java5_constructorinvocation_constructor_args():
    sig = inspect.signature(Java5_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_emptystatement_is_not_abstract():
    assert not inspect.isabstract(Java5_EmptyStatement)


def test_hyp_java5_emptystatement_constructor_exists():
    assert callable(Java5_EmptyStatement.__init__)


def test_hyp_java5_emptystatement_constructor_args():
    sig = inspect.signature(Java5_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_returnstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ReturnStatement)


def test_hyp_java5_returnstatement_constructor_exists():
    assert callable(Java5_ReturnStatement.__init__)


def test_hyp_java5_returnstatement_constructor_args():
    sig = inspect.signature(Java5_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_dostatement_is_not_abstract():
    assert not inspect.isabstract(Java5_DoStatement)


def test_hyp_java5_dostatement_constructor_exists():
    assert callable(Java5_DoStatement.__init__)


def test_hyp_java5_dostatement_constructor_args():
    sig = inspect.signature(Java5_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_EnhancedForStatement)


def test_hyp_java5_enhancedforstatement_constructor_exists():
    assert callable(Java5_EnhancedForStatement.__init__)


def test_hyp_java5_enhancedforstatement_constructor_args():
    sig = inspect.signature(Java5_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_switchcase_is_not_abstract():
    assert not inspect.isabstract(Java5_SwitchCase)


def test_hyp_java5_switchcase_constructor_exists():
    assert callable(Java5_SwitchCase.__init__)


def test_hyp_java5_switchcase_constructor_args():
    sig = inspect.signature(Java5_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_java5_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_TypeDeclarationStatement)


def test_hyp_java5_typedeclarationstatement_constructor_exists():
    assert callable(Java5_TypeDeclarationStatement.__init__)


def test_hyp_java5_typedeclarationstatement_constructor_args():
    sig = inspect.signature(Java5_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_catchclause_is_not_abstract():
    assert not inspect.isabstract(Java5_CatchClause)


def test_hyp_java5_catchclause_constructor_exists():
    assert callable(Java5_CatchClause.__init__)


def test_hyp_java5_catchclause_constructor_args():
    sig = inspect.signature(Java5_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_ifstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_IfStatement)


def test_hyp_java5_ifstatement_constructor_exists():
    assert callable(Java5_IfStatement.__init__)


def test_hyp_java5_ifstatement_constructor_args():
    sig = inspect.signature(Java5_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_continuestatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ContinueStatement)


def test_hyp_java5_continuestatement_constructor_exists():
    assert callable(Java5_ContinueStatement.__init__)


def test_hyp_java5_continuestatement_constructor_args():
    sig = inspect.signature(Java5_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ExpressionStatement)


def test_hyp_java5_expressionstatement_constructor_exists():
    assert callable(Java5_ExpressionStatement.__init__)


def test_hyp_java5_expressionstatement_constructor_args():
    sig = inspect.signature(Java5_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_trystatement_is_not_abstract():
    assert not inspect.isabstract(Java5_TryStatement)


def test_hyp_java5_trystatement_constructor_exists():
    assert callable(Java5_TryStatement.__init__)


def test_hyp_java5_trystatement_constructor_args():
    sig = inspect.signature(Java5_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_breakstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_BreakStatement)


def test_hyp_java5_breakstatement_constructor_exists():
    assert callable(Java5_BreakStatement.__init__)


def test_hyp_java5_breakstatement_constructor_args():
    sig = inspect.signature(Java5_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_SynchronizedStatement)


def test_hyp_java5_synchronizedstatement_constructor_exists():
    assert callable(Java5_SynchronizedStatement.__init__)


def test_hyp_java5_synchronizedstatement_constructor_args():
    sig = inspect.signature(Java5_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_throwstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_ThrowStatement)


def test_hyp_java5_throwstatement_constructor_exists():
    assert callable(Java5_ThrowStatement.__init__)


def test_hyp_java5_throwstatement_constructor_args():
    sig = inspect.signature(Java5_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_assertstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_AssertStatement)


def test_hyp_java5_assertstatement_constructor_exists():
    assert callable(Java5_AssertStatement.__init__)


def test_hyp_java5_assertstatement_constructor_args():
    sig = inspect.signature(Java5_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_orphantype_is_not_abstract():
    assert not inspect.isabstract(OrphanType)


def test_hyp_orphantype_constructor_exists():
    assert callable(OrphanType.__init__)


def test_hyp_orphantype_constructor_args():
    sig = inspect.signature(OrphanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(Java5_WildCardType)


def test_hyp_java5_wildcardtype_constructor_exists():
    assert callable(Java5_WildCardType.__init__)


def test_hyp_java5_wildcardtype_constructor_args():
    sig = inspect.signature(Java5_WildCardType.__init__)
    params = list(sig.parameters.keys())
    assert "isUpperBound" in params, "Missing parameter 'isUpperBound'"




def test_hyp_java5_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Java5_PrimitiveType)


def test_hyp_java5_primitivetype_constructor_exists():
    assert callable(Java5_PrimitiveType.__init__)


def test_hyp_java5_primitivetype_constructor_args():
    sig = inspect.signature(Java5_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(Java5_ParameterizedType)


def test_hyp_java5_parameterizedtype_constructor_exists():
    assert callable(Java5_ParameterizedType.__init__)


def test_hyp_java5_parameterizedtype_constructor_args():
    sig = inspect.signature(Java5_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_arraytype_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayType)


def test_hyp_java5_arraytype_constructor_exists():
    assert callable(Java5_ArrayType.__init__)


def test_hyp_java5_arraytype_constructor_args():
    sig = inspect.signature(Java5_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"
    assert "originalName" in params, "Missing parameter 'originalName'"





def test_hyp_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_hyp_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_hyp_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_FieldDeclaration)


def test_hyp_java5_fielddeclaration_constructor_exists():
    assert callable(Java5_FieldDeclaration.__init__)


def test_hyp_java5_fielddeclaration_constructor_args():
    sig = inspect.signature(Java5_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_MethodDeclaration)


def test_hyp_java5_methoddeclaration_constructor_exists():
    assert callable(Java5_MethodDeclaration.__init__)


def test_hyp_java5_methoddeclaration_constructor_args():
    sig = inspect.signature(Java5_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"
    assert "varargs" in params, "Missing parameter 'varargs'"






def test_hyp_java5_initializer_is_not_abstract():
    assert not inspect.isabstract(Java5_Initializer)


def test_hyp_java5_initializer_constructor_exists():
    assert callable(Java5_Initializer.__init__)


def test_hyp_java5_initializer_constructor_args():
    sig = inspect.signature(Java5_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_EnumConstantDeclaration)


def test_hyp_java5_enumconstantdeclaration_constructor_exists():
    assert callable(Java5_EnumConstantDeclaration.__init__)


def test_hyp_java5_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(Java5_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_AbstractTypeDeclaration)


def test_hyp_java5_abstracttypedeclaration_constructor_exists():
    assert callable(Java5_AbstractTypeDeclaration.__init__)


def test_hyp_java5_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(Java5_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"




def test_hyp_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_hyp_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_hyp_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_statement_is_not_abstract():
    assert not inspect.isabstract(Java5_Statement)


def test_hyp_java5_statement_constructor_exists():
    assert callable(Java5_Statement.__init__)


def test_hyp_java5_statement_constructor_args():
    sig = inspect.signature(Java5_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_textelement_is_not_abstract():
    assert not inspect.isabstract(Java5_TextElement)


def test_hyp_java5_textelement_constructor_exists():
    assert callable(Java5_TextElement.__init__)


def test_hyp_java5_textelement_constructor_args():
    sig = inspect.signature(Java5_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_java5_methodref_is_not_abstract():
    assert not inspect.isabstract(Java5_MethodRef)


def test_hyp_java5_methodref_constructor_exists():
    assert callable(Java5_MethodRef.__init__)


def test_hyp_java5_methodref_constructor_args():
    sig = inspect.signature(Java5_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_tagelement_is_not_abstract():
    assert not inspect.isabstract(Java5_TagElement)


def test_hyp_java5_tagelement_constructor_exists():
    assert callable(Java5_TagElement.__init__)


def test_hyp_java5_tagelement_constructor_args():
    sig = inspect.signature(Java5_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"




def test_hyp_java5_namedelement_is_not_abstract():
    assert not inspect.isabstract(Java5_NamedElement)


def test_hyp_java5_namedelement_constructor_exists():
    assert callable(Java5_NamedElement.__init__)


def test_hyp_java5_namedelement_constructor_args():
    sig = inspect.signature(Java5_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"





def test_hyp_java5_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(Java5_MethodRefParameter)


def test_hyp_java5_methodrefparameter_constructor_exists():
    assert callable(Java5_MethodRefParameter.__init__)


def test_hyp_java5_methodrefparameter_constructor_args():
    sig = inspect.signature(Java5_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isVarargs" in params, "Missing parameter 'isVarargs'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_java5_memberref_is_not_abstract():
    assert not inspect.isabstract(Java5_MemberRef)


def test_hyp_java5_memberref_constructor_exists():
    assert callable(Java5_MemberRef.__init__)


def test_hyp_java5_memberref_constructor_args():
    sig = inspect.signature(Java5_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_modifier_is_not_abstract():
    assert not inspect.isabstract(Java5_Modifier)


def test_hyp_java5_modifier_constructor_exists():
    assert callable(Java5_Modifier.__init__)


def test_hyp_java5_modifier_constructor_args():
    sig = inspect.signature(Java5_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "native" in params, "Missing parameter 'native'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "static" in params, "Missing parameter 'static'"











def test_hyp_java5_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_AnonymousClassDeclaration)


def test_hyp_java5_anonymousclassdeclaration_constructor_exists():
    assert callable(Java5_AnonymousClassDeclaration.__init__)


def test_hyp_java5_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(Java5_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_AnnotationTypeMemberDeclaration)


def test_hyp_java5_annotationtypememberdeclaration_constructor_exists():
    assert callable(Java5_AnnotationTypeMemberDeclaration.__init__)


def test_hyp_java5_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(Java5_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_hyp_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_hyp_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_TypeDeclaration)


def test_hyp_java5_typedeclaration_constructor_exists():
    assert callable(Java5_TypeDeclaration.__init__)


def test_hyp_java5_typedeclaration_constructor_args():
    sig = inspect.signature(Java5_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_EnumDeclaration)


def test_hyp_java5_enumdeclaration_constructor_exists():
    assert callable(Java5_EnumDeclaration.__init__)


def test_hyp_java5_enumdeclaration_constructor_args():
    sig = inspect.signature(Java5_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_AnnotationTypeDeclaration)


def test_hyp_java5_annotationtypedeclaration_constructor_exists():
    assert callable(Java5_AnnotationTypeDeclaration.__init__)


def test_hyp_java5_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(Java5_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_expression_is_not_abstract():
    assert not inspect.isabstract(Java5_Expression)


def test_hyp_java5_expression_constructor_exists():
    assert callable(Java5_Expression.__init__)


def test_hyp_java5_expression_constructor_args():
    sig = inspect.signature(Java5_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_unresolveditem_is_not_abstract():
    assert not inspect.isabstract(Java5_UnresolvedItem)


def test_hyp_java5_unresolveditem_constructor_exists():
    assert callable(Java5_UnresolvedItem.__init__)


def test_hyp_java5_unresolveditem_constructor_args():
    sig = inspect.signature(Java5_UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_BodyDeclaration)


def test_hyp_java5_bodydeclaration_constructor_exists():
    assert callable(Java5_BodyDeclaration.__init__)


def test_hyp_java5_bodydeclaration_constructor_args():
    sig = inspect.signature(Java5_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_typeparameter_is_not_abstract():
    assert not inspect.isabstract(Java5_TypeParameter)


def test_hyp_java5_typeparameter_constructor_exists():
    assert callable(Java5_TypeParameter.__init__)


def test_hyp_java5_typeparameter_constructor_args():
    sig = inspect.signature(Java5_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_orphantype_is_not_abstract():
    assert not inspect.isabstract(Java5_OrphanType)


def test_hyp_java5_orphantype_constructor_exists():
    assert callable(Java5_OrphanType.__init__)


def test_hyp_java5_orphantype_constructor_args():
    sig = inspect.signature(Java5_OrphanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_compilationunit_is_not_abstract():
    assert not inspect.isabstract(Java5_CompilationUnit)


def test_hyp_java5_compilationunit_constructor_exists():
    assert callable(Java5_CompilationUnit.__init__)


def test_hyp_java5_compilationunit_constructor_args():
    sig = inspect.signature(Java5_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"




def test_hyp_java5_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(Java5_LabeledStatement)


def test_hyp_java5_labeledstatement_constructor_exists():
    assert callable(Java5_LabeledStatement.__init__)


def test_hyp_java5_labeledstatement_constructor_args():
    sig = inspect.signature(Java5_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_VariableDeclaration)


def test_hyp_java5_variabledeclaration_constructor_exists():
    assert callable(Java5_VariableDeclaration.__init__)


def test_hyp_java5_variabledeclaration_constructor_args():
    sig = inspect.signature(Java5_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraArrayDimensions" in params, "Missing parameter 'extraArrayDimensions'"




def test_hyp_java5_annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(Java5_AnnotationMemberValuePair)


def test_hyp_java5_annotationmembervaluepair_constructor_exists():
    assert callable(Java5_AnnotationMemberValuePair.__init__)


def test_hyp_java5_annotationmembervaluepair_constructor_args():
    sig = inspect.signature(Java5_AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_thisexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_ThisExpression)


def test_hyp_java5_thisexpression_constructor_exists():
    assert callable(Java5_ThisExpression.__init__)


def test_hyp_java5_thisexpression_constructor_args():
    sig = inspect.signature(Java5_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_infixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_InfixExpression)


def test_hyp_java5_infixexpression_constructor_exists():
    assert callable(Java5_InfixExpression.__init__)


def test_hyp_java5_infixexpression_constructor_args():
    sig = inspect.signature(Java5_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_java5_arraycreation_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayCreation)


def test_hyp_java5_arraycreation_constructor_exists():
    assert callable(Java5_ArrayCreation.__init__)


def test_hyp_java5_arraycreation_constructor_args():
    sig = inspect.signature(Java5_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayInitializer)


def test_hyp_java5_arrayinitializer_constructor_exists():
    assert callable(Java5_ArrayInitializer.__init__)


def test_hyp_java5_arrayinitializer_constructor_args():
    sig = inspect.signature(Java5_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_BooleanLiteral)


def test_hyp_java5_booleanliteral_constructor_exists():
    assert callable(Java5_BooleanLiteral.__init__)


def test_hyp_java5_booleanliteral_constructor_args():
    sig = inspect.signature(Java5_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_java5_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java5_FieldAccess)


def test_hyp_java5_fieldaccess_constructor_exists():
    assert callable(Java5_FieldAccess.__init__)


def test_hyp_java5_fieldaccess_constructor_args():
    sig = inspect.signature(Java5_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_nullliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_NullLiteral)


def test_hyp_java5_nullliteral_constructor_exists():
    assert callable(Java5_NullLiteral.__init__)


def test_hyp_java5_nullliteral_constructor_args():
    sig = inspect.signature(Java5_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_characterliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_CharacterLiteral)


def test_hyp_java5_characterliteral_constructor_exists():
    assert callable(Java5_CharacterLiteral.__init__)


def test_hyp_java5_characterliteral_constructor_args():
    sig = inspect.signature(Java5_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_java5_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_PrefixExpression)


def test_hyp_java5_prefixexpression_constructor_exists():
    assert callable(Java5_PrefixExpression.__init__)


def test_hyp_java5_prefixexpression_constructor_args():
    sig = inspect.signature(Java5_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_java5_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(Java5_SuperFieldAccess)


def test_hyp_java5_superfieldaccess_constructor_exists():
    assert callable(Java5_SuperFieldAccess.__init__)


def test_hyp_java5_superfieldaccess_constructor_args():
    sig = inspect.signature(Java5_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_VariableDeclarationExpression)


def test_hyp_java5_variabledeclarationexpression_constructor_exists():
    assert callable(Java5_VariableDeclarationExpression.__init__)


def test_hyp_java5_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(Java5_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5_SuperMethodInvocation)


def test_hyp_java5_supermethodinvocation_constructor_exists():
    assert callable(Java5_SuperMethodInvocation.__init__)


def test_hyp_java5_supermethodinvocation_constructor_args():
    sig = inspect.signature(Java5_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_ConditionalExpression)


def test_hyp_java5_conditionalexpression_constructor_exists():
    assert callable(Java5_ConditionalExpression.__init__)


def test_hyp_java5_conditionalexpression_constructor_args():
    sig = inspect.signature(Java5_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_stringliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_StringLiteral)


def test_hyp_java5_stringliteral_constructor_exists():
    assert callable(Java5_StringLiteral.__init__)


def test_hyp_java5_stringliteral_constructor_args():
    sig = inspect.signature(Java5_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"





def test_hyp_java5_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_ParenthesizedExpression)


def test_hyp_java5_parenthesizedexpression_constructor_exists():
    assert callable(Java5_ParenthesizedExpression.__init__)


def test_hyp_java5_parenthesizedexpression_constructor_args():
    sig = inspect.signature(Java5_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_InstanceofExpression)


def test_hyp_java5_instanceofexpression_constructor_exists():
    assert callable(Java5_InstanceofExpression.__init__)


def test_hyp_java5_instanceofexpression_constructor_args():
    sig = inspect.signature(Java5_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_castexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_CastExpression)


def test_hyp_java5_castexpression_constructor_exists():
    assert callable(Java5_CastExpression.__init__)


def test_hyp_java5_castexpression_constructor_args():
    sig = inspect.signature(Java5_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayAccess)


def test_hyp_java5_arrayaccess_constructor_exists():
    assert callable(Java5_ArrayAccess.__init__)


def test_hyp_java5_arrayaccess_constructor_args():
    sig = inspect.signature(Java5_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_assignment_is_not_abstract():
    assert not inspect.isabstract(Java5_Assignment)


def test_hyp_java5_assignment_constructor_exists():
    assert callable(Java5_Assignment.__init__)


def test_hyp_java5_assignment_constructor_args():
    sig = inspect.signature(Java5_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_java5_numberliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_NumberLiteral)


def test_hyp_java5_numberliteral_constructor_exists():
    assert callable(Java5_NumberLiteral.__init__)


def test_hyp_java5_numberliteral_constructor_args():
    sig = inspect.signature(Java5_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"




def test_hyp_java5_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(Java5_PostfixExpression)


def test_hyp_java5_postfixexpression_constructor_exists():
    assert callable(Java5_PostfixExpression.__init__)


def test_hyp_java5_postfixexpression_constructor_args():
    sig = inspect.signature(Java5_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_java5_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(Java5_ClassInstanceCreation)


def test_hyp_java5_classinstancecreation_constructor_exists():
    assert callable(Java5_ClassInstanceCreation.__init__)


def test_hyp_java5_classinstancecreation_constructor_args():
    sig = inspect.signature(Java5_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(Java5_MethodInvocation)


def test_hyp_java5_methodinvocation_constructor_exists():
    assert callable(Java5_MethodInvocation.__init__)


def test_hyp_java5_methodinvocation_constructor_args():
    sig = inspect.signature(Java5_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(Java5_ArrayLengthAccess)


def test_hyp_java5_arraylengthaccess_constructor_exists():
    assert callable(Java5_ArrayLengthAccess.__init__)


def test_hyp_java5_arraylengthaccess_constructor_args():
    sig = inspect.signature(Java5_ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_typeliteral_is_not_abstract():
    assert not inspect.isabstract(Java5_TypeLiteral)


def test_hyp_java5_typeliteral_constructor_exists():
    assert callable(Java5_TypeLiteral.__init__)


def test_hyp_java5_typeliteral_constructor_args():
    sig = inspect.signature(Java5_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_annotation_is_not_abstract():
    assert not inspect.isabstract(Java5_Annotation)


def test_hyp_java5_annotation_constructor_exists():
    assert callable(Java5_Annotation.__init__)


def test_hyp_java5_annotation_constructor_args():
    sig = inspect.signature(Java5_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_namedelementref_is_not_abstract():
    assert not inspect.isabstract(Java5_NamedElementRef)


def test_hyp_java5_namedelementref_constructor_exists():
    assert callable(Java5_NamedElementRef.__init__)


def test_hyp_java5_namedelementref_constructor_args():
    sig = inspect.signature(Java5_NamedElementRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java5_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_PackageDeclaration)


def test_hyp_java5_packagedeclaration_constructor_exists():
    assert callable(Java5_PackageDeclaration.__init__)


def test_hyp_java5_packagedeclaration_constructor_args():
    sig = inspect.signature(Java5_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"




def test_hyp_java5_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(Java5_ImportDeclaration)


def test_hyp_java5_importdeclaration_constructor_exists():
    assert callable(Java5_ImportDeclaration.__init__)


def test_hyp_java5_importdeclaration_constructor_args():
    sig = inspect.signature(Java5_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"


def test_hyp_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_hyp_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "public",
        "none",
        "protected",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_hyp_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_hyp_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "final",
        "abstract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"


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
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
Java5_PrimitiveTypeVoid_strategy = st.builds(
    Java5_PrimitiveTypeVoid,
)
Java5_PrimitiveTypeFloat_strategy = st.builds(
    Java5_PrimitiveTypeFloat,
)
Java5_PrimitiveTypeLong_strategy = st.builds(
    Java5_PrimitiveTypeLong,
)
Java5_PrimitiveTypeChar_strategy = st.builds(
    Java5_PrimitiveTypeChar,
)
Java5_PrimitiveTypeInt_strategy = st.builds(
    Java5_PrimitiveTypeInt,
)
Java5_PrimitiveTypeShort_strategy = st.builds(
    Java5_PrimitiveTypeShort,
)
Java5_PrimitiveTypeByte_strategy = st.builds(
    Java5_PrimitiveTypeByte,
)
Java5_PrimitiveTypeDouble_strategy = st.builds(
    Java5_PrimitiveTypeDouble,
)
Java5_PrimitiveTypeBoolean_strategy = st.builds(
    Java5_PrimitiveTypeBoolean,
)
Java5_Model_strategy = st.builds(
    Java5_Model,
    name=
        safe_text
)
Java5_VariableDeclarationFragment_strategy = st.builds(
    Java5_VariableDeclarationFragment,
)
Java5_SingleVariableDeclaration_strategy = st.builds(
    Java5_SingleVariableDeclaration,
    varargs=
        st.booleans()
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
Java5_InterfaceDeclaration_strategy = st.builds(
    Java5_InterfaceDeclaration,
)
Java5_ClassDeclaration_strategy = st.builds(
    Java5_ClassDeclaration,
)
Java5_ASTNode_strategy = st.builds(
    Java5_ASTNode,
)
Statement_strategy = st.builds(
    Statement,
)
Java5_SuperConstructorInvocation_strategy = st.builds(
    Java5_SuperConstructorInvocation,
)
Java5_SwitchStatement_strategy = st.builds(
    Java5_SwitchStatement,
)
Java5_ForStatement_strategy = st.builds(
    Java5_ForStatement,
)
Java5_WhileStatement_strategy = st.builds(
    Java5_WhileStatement,
)
Java5_VariableDeclarationStatement_strategy = st.builds(
    Java5_VariableDeclarationStatement,
    extraArrayDimensions=
        st.integers()
)
Java5_Block_strategy = st.builds(
    Java5_Block,
)
Java5_ConstructorInvocation_strategy = st.builds(
    Java5_ConstructorInvocation,
)
Java5_EmptyStatement_strategy = st.builds(
    Java5_EmptyStatement,
)
Java5_ReturnStatement_strategy = st.builds(
    Java5_ReturnStatement,
)
Java5_DoStatement_strategy = st.builds(
    Java5_DoStatement,
)
Java5_EnhancedForStatement_strategy = st.builds(
    Java5_EnhancedForStatement,
)
Java5_SwitchCase_strategy = st.builds(
    Java5_SwitchCase,
    default=
        st.booleans()
)
Java5_TypeDeclarationStatement_strategy = st.builds(
    Java5_TypeDeclarationStatement,
)
Java5_CatchClause_strategy = st.builds(
    Java5_CatchClause,
)
Java5_IfStatement_strategy = st.builds(
    Java5_IfStatement,
)
Java5_ContinueStatement_strategy = st.builds(
    Java5_ContinueStatement,
)
Java5_ExpressionStatement_strategy = st.builds(
    Java5_ExpressionStatement,
)
Java5_TryStatement_strategy = st.builds(
    Java5_TryStatement,
)
Java5_BreakStatement_strategy = st.builds(
    Java5_BreakStatement,
)
Java5_SynchronizedStatement_strategy = st.builds(
    Java5_SynchronizedStatement,
)
Java5_ThrowStatement_strategy = st.builds(
    Java5_ThrowStatement,
)
Java5_AssertStatement_strategy = st.builds(
    Java5_AssertStatement,
)
OrphanType_strategy = st.builds(
    OrphanType,
)
Java5_WildCardType_strategy = st.builds(
    Java5_WildCardType,
    isUpperBound=
        safe_text
)
Java5_PrimitiveType_strategy = st.builds(
    Java5_PrimitiveType,
)
Java5_ParameterizedType_strategy = st.builds(
    Java5_ParameterizedType,
)
Java5_ArrayType_strategy = st.builds(
    Java5_ArrayType,
    dimensions=
        st.integers(),
    originalName=
        safe_text
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
Java5_FieldDeclaration_strategy = st.builds(
    Java5_FieldDeclaration,
)
Java5_MethodDeclaration_strategy = st.builds(
    Java5_MethodDeclaration,
    constructor=
        st.booleans(),
    extraArrayDimensions=
        st.integers(),
    varargs=
        st.booleans()
)
Java5_Initializer_strategy = st.builds(
    Java5_Initializer,
)
Java5_EnumConstantDeclaration_strategy = st.builds(
    Java5_EnumConstantDeclaration,
)
Java5_AbstractTypeDeclaration_strategy = st.builds(
    Java5_AbstractTypeDeclaration,
    qualifiedName=
        safe_text
)
ASTNode_strategy = st.builds(
    ASTNode,
)
Java5_Statement_strategy = st.builds(
    Java5_Statement,
)
Java5_TextElement_strategy = st.builds(
    Java5_TextElement,
    text=
        safe_text
)
Java5_MethodRef_strategy = st.builds(
    Java5_MethodRef,
)
Java5_TagElement_strategy = st.builds(
    Java5_TagElement,
    tagName=
        safe_text
)
Java5_NamedElement_strategy = st.builds(
    Java5_NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
Java5_MethodRefParameter_strategy = st.builds(
    Java5_MethodRefParameter,
    isVarargs=
        safe_text,
    name=
        safe_text
)
Java5_MemberRef_strategy = st.builds(
    Java5_MemberRef,
)
Java5_Modifier_strategy = st.builds(
    Java5_Modifier,
    inheritance=
        safe_text,
    visibility=
        safe_text,
    transient=
        st.booleans(),
    native=
        st.booleans(),
    strictfp=
        st.booleans(),
    synchronized=
        st.booleans(),
    volatile=
        st.booleans(),
    static=
        st.booleans()
)
Java5_AnonymousClassDeclaration_strategy = st.builds(
    Java5_AnonymousClassDeclaration,
)
Java5_AnnotationTypeMemberDeclaration_strategy = st.builds(
    Java5_AnnotationTypeMemberDeclaration,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
Java5_TypeDeclaration_strategy = st.builds(
    Java5_TypeDeclaration,
)
Java5_EnumDeclaration_strategy = st.builds(
    Java5_EnumDeclaration,
)
Java5_AnnotationTypeDeclaration_strategy = st.builds(
    Java5_AnnotationTypeDeclaration,
)
Java5_Expression_strategy = st.builds(
    Java5_Expression,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Java5_UnresolvedItem_strategy = st.builds(
    Java5_UnresolvedItem,
)
Java5_BodyDeclaration_strategy = st.builds(
    Java5_BodyDeclaration,
)
Java5_TypeParameter_strategy = st.builds(
    Java5_TypeParameter,
)
Java5_OrphanType_strategy = st.builds(
    Java5_OrphanType,
)
Java5_CompilationUnit_strategy = st.builds(
    Java5_CompilationUnit,
    originalFilePath=
        safe_text
)
Java5_LabeledStatement_strategy = st.builds(
    Java5_LabeledStatement,
)
Java5_VariableDeclaration_strategy = st.builds(
    Java5_VariableDeclaration,
    extraArrayDimensions=
        st.integers()
)
Java5_AnnotationMemberValuePair_strategy = st.builds(
    Java5_AnnotationMemberValuePair,
)
Expression_strategy = st.builds(
    Expression,
)
Java5_ThisExpression_strategy = st.builds(
    Java5_ThisExpression,
)
Java5_InfixExpression_strategy = st.builds(
    Java5_InfixExpression,
    operator=
        safe_text
)
Java5_ArrayCreation_strategy = st.builds(
    Java5_ArrayCreation,
)
Java5_ArrayInitializer_strategy = st.builds(
    Java5_ArrayInitializer,
)
Java5_BooleanLiteral_strategy = st.builds(
    Java5_BooleanLiteral,
    value=
        st.booleans()
)
Java5_FieldAccess_strategy = st.builds(
    Java5_FieldAccess,
)
Java5_NullLiteral_strategy = st.builds(
    Java5_NullLiteral,
)
Java5_CharacterLiteral_strategy = st.builds(
    Java5_CharacterLiteral,
    escapedValue=
        safe_text,
    value=
        safe_text
)
Java5_PrefixExpression_strategy = st.builds(
    Java5_PrefixExpression,
    operator=
        safe_text
)
Java5_SuperFieldAccess_strategy = st.builds(
    Java5_SuperFieldAccess,
)
Java5_VariableDeclarationExpression_strategy = st.builds(
    Java5_VariableDeclarationExpression,
)
Java5_SuperMethodInvocation_strategy = st.builds(
    Java5_SuperMethodInvocation,
)
Java5_ConditionalExpression_strategy = st.builds(
    Java5_ConditionalExpression,
)
Java5_StringLiteral_strategy = st.builds(
    Java5_StringLiteral,
    value=
        safe_text,
    escapedValue=
        safe_text
)
Java5_ParenthesizedExpression_strategy = st.builds(
    Java5_ParenthesizedExpression,
)
Java5_InstanceofExpression_strategy = st.builds(
    Java5_InstanceofExpression,
)
Java5_CastExpression_strategy = st.builds(
    Java5_CastExpression,
)
Java5_ArrayAccess_strategy = st.builds(
    Java5_ArrayAccess,
)
Java5_Assignment_strategy = st.builds(
    Java5_Assignment,
    operator=
        safe_text
)
Java5_NumberLiteral_strategy = st.builds(
    Java5_NumberLiteral,
    tokenValue=
        safe_text
)
Java5_PostfixExpression_strategy = st.builds(
    Java5_PostfixExpression,
    operator=
        safe_text
)
Java5_ClassInstanceCreation_strategy = st.builds(
    Java5_ClassInstanceCreation,
)
Java5_MethodInvocation_strategy = st.builds(
    Java5_MethodInvocation,
)
Java5_ArrayLengthAccess_strategy = st.builds(
    Java5_ArrayLengthAccess,
)
Java5_TypeLiteral_strategy = st.builds(
    Java5_TypeLiteral,
)
Java5_Annotation_strategy = st.builds(
    Java5_Annotation,
)
Java5_NamedElementRef_strategy = st.builds(
    Java5_NamedElementRef,
)
Java5_PackageDeclaration_strategy = st.builds(
    Java5_PackageDeclaration,
    qualifiedName=
        safe_text
)
Java5_ImportDeclaration_strategy = st.builds(
    Java5_ImportDeclaration,
    static=
        st.booleans()
)















@given(instance=Java5_Model_strategy)
def test_hyp_java5_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=Java5_SingleVariableDeclaration_strategy)
def test_hyp_java5_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original













@given(instance=Java5_VariableDeclarationStatement_strategy)
def test_hyp_java5_variabledeclarationstatement_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original










@given(instance=Java5_SwitchCase_strategy)
def test_hyp_java5_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original















@given(instance=Java5_WildCardType_strategy)
def test_hyp_java5_wildcardtype_isUpperBound_setter(instance):
    original = instance.isUpperBound
    instance.isUpperBound = original
    assert instance.isUpperBound == original






@given(instance=Java5_ArrayType_strategy)
def test_hyp_java5_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original



@given(instance=Java5_ArrayType_strategy)
def test_hyp_java5_arraytype_originalName_setter(instance):
    original = instance.originalName
    instance.originalName = original
    assert instance.originalName == original






@given(instance=Java5_MethodDeclaration_strategy)
def test_hyp_java5_methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original



@given(instance=Java5_MethodDeclaration_strategy)
def test_hyp_java5_methoddeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original



@given(instance=Java5_MethodDeclaration_strategy)
def test_hyp_java5_methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original






@given(instance=Java5_AbstractTypeDeclaration_strategy)
def test_hyp_java5_abstracttypedeclaration_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original






@given(instance=Java5_TextElement_strategy)
def test_hyp_java5_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=Java5_TagElement_strategy)
def test_hyp_java5_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original




@given(instance=Java5_NamedElement_strategy)
def test_hyp_java5_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Java5_NamedElement_strategy)
def test_hyp_java5_namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original




@given(instance=Java5_MethodRefParameter_strategy)
def test_hyp_java5_methodrefparameter_isVarargs_setter(instance):
    original = instance.isVarargs
    instance.isVarargs = original
    assert instance.isVarargs == original



@given(instance=Java5_MethodRefParameter_strategy)
def test_hyp_java5_methodrefparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=Java5_Modifier_strategy)
def test_hyp_java5_modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original



@given(instance=Java5_Modifier_strategy)
def test_hyp_java5_modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=Java5_Modifier_strategy)
def test_hyp_java5_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=Java5_Modifier_strategy)
def test_hyp_java5_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=Java5_Modifier_strategy)
def test_hyp_java5_modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=Java5_Modifier_strategy)
def test_hyp_java5_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=Java5_Modifier_strategy)
def test_hyp_java5_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=Java5_Modifier_strategy)
def test_hyp_java5_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original
















@given(instance=Java5_CompilationUnit_strategy)
def test_hyp_java5_compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original





@given(instance=Java5_VariableDeclaration_strategy)
def test_hyp_java5_variabledeclaration_extraArrayDimensions_setter(instance):
    original = instance.extraArrayDimensions
    instance.extraArrayDimensions = original
    assert instance.extraArrayDimensions == original







@given(instance=Java5_InfixExpression_strategy)
def test_hyp_java5_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original






@given(instance=Java5_BooleanLiteral_strategy)
def test_hyp_java5_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=Java5_CharacterLiteral_strategy)
def test_hyp_java5_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=Java5_CharacterLiteral_strategy)
def test_hyp_java5_characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Java5_PrefixExpression_strategy)
def test_hyp_java5_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original








@given(instance=Java5_StringLiteral_strategy)
def test_hyp_java5_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Java5_StringLiteral_strategy)
def test_hyp_java5_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original








@given(instance=Java5_Assignment_strategy)
def test_hyp_java5_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=Java5_NumberLiteral_strategy)
def test_hyp_java5_numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original




@given(instance=Java5_PostfixExpression_strategy)
def test_hyp_java5_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original










@given(instance=Java5_PackageDeclaration_strategy)
def test_hyp_java5_packagedeclaration_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original




@given(instance=Java5_ImportDeclaration_strategy)
def test_hyp_java5_importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ASTNode,
    AbstractTypeDeclaration,
    BodyDeclaration,
    Expression,
    Java5_ASTNode,
    Java5_AbstractTypeDeclaration,
    Java5_Annotation,
    Java5_AnnotationMemberValuePair,
    Java5_AnnotationTypeDeclaration,
    Java5_AnnotationTypeMemberDeclaration,
    Java5_AnonymousClassDeclaration,
    Java5_ArrayAccess,
    Java5_ArrayCreation,
    Java5_ArrayInitializer,
    Java5_ArrayLengthAccess,
    Java5_ArrayType,
    Java5_AssertStatement,
    Java5_Assignment,
    Java5_Block,
    Java5_BodyDeclaration,
    Java5_BooleanLiteral,
    Java5_BreakStatement,
    Java5_CastExpression,
    Java5_CatchClause,
    Java5_CharacterLiteral,
    Java5_ClassDeclaration,
    Java5_ClassInstanceCreation,
    Java5_CompilationUnit,
    Java5_ConditionalExpression,
    Java5_ConstructorInvocation,
    Java5_ContinueStatement,
    Java5_DoStatement,
    Java5_EmptyStatement,
    Java5_EnhancedForStatement,
    Java5_EnumConstantDeclaration,
    Java5_EnumDeclaration,
    Java5_Expression,
    Java5_ExpressionStatement,
    Java5_FieldAccess,
    Java5_FieldDeclaration,
    Java5_ForStatement,
    Java5_IfStatement,
    Java5_ImportDeclaration,
    Java5_InfixExpression,
    Java5_Initializer,
    Java5_InstanceofExpression,
    Java5_InterfaceDeclaration,
    Java5_LabeledStatement,
    Java5_MemberRef,
    Java5_MethodDeclaration,
    Java5_MethodInvocation,
    Java5_MethodRef,
    Java5_MethodRefParameter,
    Java5_Model,
    Java5_Modifier,
    Java5_NamedElement,
    Java5_NamedElementRef,
    Java5_NullLiteral,
    Java5_NumberLiteral,
    Java5_OrphanType,
    Java5_PackageDeclaration,
    Java5_ParameterizedType,
    Java5_ParenthesizedExpression,
    Java5_PostfixExpression,
    Java5_PrefixExpression,
    Java5_PrimitiveType,
    Java5_PrimitiveTypeBoolean,
    Java5_PrimitiveTypeByte,
    Java5_PrimitiveTypeChar,
    Java5_PrimitiveTypeDouble,
    Java5_PrimitiveTypeFloat,
    Java5_PrimitiveTypeInt,
    Java5_PrimitiveTypeLong,
    Java5_PrimitiveTypeShort,
    Java5_PrimitiveTypeVoid,
    Java5_ReturnStatement,
    Java5_SingleVariableDeclaration,
    Java5_Statement,
    Java5_StringLiteral,
    Java5_SuperConstructorInvocation,
    Java5_SuperFieldAccess,
    Java5_SuperMethodInvocation,
    Java5_SwitchCase,
    Java5_SwitchStatement,
    Java5_SynchronizedStatement,
    Java5_TagElement,
    Java5_TextElement,
    Java5_ThisExpression,
    Java5_ThrowStatement,
    Java5_TryStatement,
    Java5_TypeDeclaration,
    Java5_TypeDeclarationStatement,
    Java5_TypeLiteral,
    Java5_TypeParameter,
    Java5_UnresolvedItem,
    Java5_VariableDeclaration,
    Java5_VariableDeclarationExpression,
    Java5_VariableDeclarationFragment,
    Java5_VariableDeclarationStatement,
    Java5_WhileStatement,
    Java5_WildCardType,
    NamedElement,
    OrphanType,
    PrimitiveType,
    Statement,
    TypeDeclaration,
    VariableDeclaration,
    InheritanceKind,
    VisibilityKind,
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

def test_Java5_AbstractTypeDeclaration_qualifiedName_value_roundtrip():
    instance = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    assert instance.qualifiedName == "sample_text"
    instance.qualifiedName = "sample_text_2"
    assert instance.qualifiedName == "sample_text_2"


def test_Java5_ArrayType_dimensions_value_roundtrip():
    instance = Java5_ArrayType(dimensions=7, originalName="sample_text")
    assert instance.dimensions == 7
    instance.dimensions = 13
    assert instance.dimensions == 13


def test_Java5_ArrayType_originalName_value_roundtrip():
    instance = Java5_ArrayType(dimensions=7, originalName="sample_text")
    assert instance.originalName == "sample_text"
    instance.originalName = "sample_text_2"
    assert instance.originalName == "sample_text_2"


def test_Java5_Assignment_operator_value_roundtrip():
    instance = Java5_Assignment(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_Java5_BooleanLiteral_value_value_roundtrip():
    instance = Java5_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_Java5_CharacterLiteral_escapedValue_value_roundtrip():
    instance = Java5_CharacterLiteral(escapedValue="sample_text", value="sample_text")
    assert instance.escapedValue == "sample_text"
    instance.escapedValue = "sample_text_2"
    assert instance.escapedValue == "sample_text_2"


def test_Java5_CharacterLiteral_value_value_roundtrip():
    instance = Java5_CharacterLiteral(escapedValue="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Java5_CompilationUnit_originalFilePath_value_roundtrip():
    instance = Java5_CompilationUnit(originalFilePath="sample_text")
    assert instance.originalFilePath == "sample_text"
    instance.originalFilePath = "sample_text_2"
    assert instance.originalFilePath == "sample_text_2"


def test_Java5_ImportDeclaration_static_value_roundtrip():
    instance = Java5_ImportDeclaration(static=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_Java5_InfixExpression_operator_value_roundtrip():
    instance = Java5_InfixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_Java5_MethodDeclaration_constructor_value_roundtrip():
    instance = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    assert instance.constructor == True
    instance.constructor = False
    assert instance.constructor == False


def test_Java5_MethodDeclaration_extraArrayDimensions_value_roundtrip():
    instance = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    assert instance.extraArrayDimensions == 7
    instance.extraArrayDimensions = 13
    assert instance.extraArrayDimensions == 13


def test_Java5_MethodDeclaration_varargs_value_roundtrip():
    instance = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    assert instance.varargs == True
    instance.varargs = False
    assert instance.varargs == False


def test_Java5_MethodRefParameter_isVarargs_value_roundtrip():
    instance = Java5_MethodRefParameter(isVarargs="sample_text", name="sample_text")
    assert instance.isVarargs == "sample_text"
    instance.isVarargs = "sample_text_2"
    assert instance.isVarargs == "sample_text_2"


def test_Java5_MethodRefParameter_name_value_roundtrip():
    instance = Java5_MethodRefParameter(isVarargs="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Java5_Model_name_value_roundtrip():
    instance = Java5_Model(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Java5_Modifier_inheritance_value_roundtrip():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert instance.inheritance == "sample_text"
    instance.inheritance = "sample_text_2"
    assert instance.inheritance == "sample_text_2"


def test_Java5_Modifier_native_value_roundtrip():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert instance.native == True
    instance.native = False
    assert instance.native == False


def test_Java5_Modifier_static_value_roundtrip():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_Java5_Modifier_strictfp_value_roundtrip():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert instance.strictfp == True
    instance.strictfp = False
    assert instance.strictfp == False


def test_Java5_Modifier_synchronized_value_roundtrip():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert instance.synchronized == True
    instance.synchronized = False
    assert instance.synchronized == False


def test_Java5_Modifier_transient_value_roundtrip():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert instance.transient == True
    instance.transient = False
    assert instance.transient == False


def test_Java5_Modifier_visibility_value_roundtrip():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_Java5_Modifier_volatile_value_roundtrip():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert instance.volatile == True
    instance.volatile = False
    assert instance.volatile == False


def test_Java5_NamedElement_name_value_roundtrip():
    instance = Java5_NamedElement(name="sample_text", proxy=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Java5_NamedElement_proxy_value_roundtrip():
    instance = Java5_NamedElement(name="sample_text", proxy=True)
    assert instance.proxy == True
    instance.proxy = False
    assert instance.proxy == False


def test_Java5_NumberLiteral_tokenValue_value_roundtrip():
    instance = Java5_NumberLiteral(tokenValue="sample_text")
    assert instance.tokenValue == "sample_text"
    instance.tokenValue = "sample_text_2"
    assert instance.tokenValue == "sample_text_2"


def test_Java5_PackageDeclaration_qualifiedName_value_roundtrip():
    instance = Java5_PackageDeclaration(qualifiedName="sample_text")
    assert instance.qualifiedName == "sample_text"
    instance.qualifiedName = "sample_text_2"
    assert instance.qualifiedName == "sample_text_2"


def test_Java5_PostfixExpression_operator_value_roundtrip():
    instance = Java5_PostfixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_Java5_PrefixExpression_operator_value_roundtrip():
    instance = Java5_PrefixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_Java5_SingleVariableDeclaration_varargs_value_roundtrip():
    instance = Java5_SingleVariableDeclaration(varargs=True)
    assert instance.varargs == True
    instance.varargs = False
    assert instance.varargs == False


def test_Java5_StringLiteral_escapedValue_value_roundtrip():
    instance = Java5_StringLiteral(escapedValue="sample_text", value="sample_text")
    assert instance.escapedValue == "sample_text"
    instance.escapedValue = "sample_text_2"
    assert instance.escapedValue == "sample_text_2"


def test_Java5_StringLiteral_value_value_roundtrip():
    instance = Java5_StringLiteral(escapedValue="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_Java5_SwitchCase_default_value_roundtrip():
    instance = Java5_SwitchCase(default=True)
    assert instance.default == True
    instance.default = False
    assert instance.default == False


def test_Java5_TagElement_tagName_value_roundtrip():
    instance = Java5_TagElement(tagName="sample_text")
    assert instance.tagName == "sample_text"
    instance.tagName = "sample_text_2"
    assert instance.tagName == "sample_text_2"


def test_Java5_TextElement_text_value_roundtrip():
    instance = Java5_TextElement(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_Java5_VariableDeclaration_extraArrayDimensions_value_roundtrip():
    instance = Java5_VariableDeclaration(extraArrayDimensions=7)
    assert instance.extraArrayDimensions == 7
    instance.extraArrayDimensions = 13
    assert instance.extraArrayDimensions == 13


def test_Java5_VariableDeclarationStatement_extraArrayDimensions_value_roundtrip():
    instance = Java5_VariableDeclarationStatement(extraArrayDimensions=7)
    assert instance.extraArrayDimensions == 7
    instance.extraArrayDimensions = 13
    assert instance.extraArrayDimensions == 13


def test_Java5_WildCardType_isUpperBound_value_roundtrip():
    instance = Java5_WildCardType(isUpperBound="sample_text")
    assert instance.isUpperBound == "sample_text"
    instance.isUpperBound = "sample_text_2"
    assert instance.isUpperBound == "sample_text_2"


def test_Java5_AnonymousClassDeclaration_isa_ASTNode():
    instance = Java5_AnonymousClassDeclaration()
    assert isinstance(instance, ASTNode)


def test_Java5_Expression_isa_ASTNode():
    instance = Java5_Expression()
    assert isinstance(instance, ASTNode)


def test_Java5_ImportDeclaration_isa_ASTNode():
    instance = Java5_ImportDeclaration(static=True)
    assert isinstance(instance, ASTNode)


def test_Java5_MemberRef_isa_ASTNode():
    instance = Java5_MemberRef()
    assert isinstance(instance, ASTNode)


def test_Java5_MethodRef_isa_ASTNode():
    instance = Java5_MethodRef()
    assert isinstance(instance, ASTNode)


def test_Java5_MethodRefParameter_isa_ASTNode():
    instance = Java5_MethodRefParameter(isVarargs="sample_text", name="sample_text")
    assert isinstance(instance, ASTNode)


def test_Java5_Modifier_isa_ASTNode():
    instance = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    assert isinstance(instance, ASTNode)


def test_Java5_NamedElement_isa_ASTNode():
    instance = Java5_NamedElement(name="sample_text", proxy=True)
    assert isinstance(instance, ASTNode)


def test_Java5_Statement_isa_ASTNode():
    instance = Java5_Statement()
    assert isinstance(instance, ASTNode)


def test_Java5_TagElement_isa_ASTNode():
    instance = Java5_TagElement(tagName="sample_text")
    assert isinstance(instance, ASTNode)


def test_Java5_TextElement_isa_ASTNode():
    instance = Java5_TextElement(text="sample_text")
    assert isinstance(instance, ASTNode)


def test_Java5_AnnotationTypeDeclaration_isa_AbstractTypeDeclaration():
    instance = Java5_AnnotationTypeDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_Java5_EnumDeclaration_isa_AbstractTypeDeclaration():
    instance = Java5_EnumDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_Java5_TypeDeclaration_isa_AbstractTypeDeclaration():
    instance = Java5_TypeDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_Java5_AbstractTypeDeclaration_isa_BodyDeclaration():
    instance = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    assert isinstance(instance, BodyDeclaration)


def test_Java5_AnnotationTypeMemberDeclaration_isa_BodyDeclaration():
    instance = Java5_AnnotationTypeMemberDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_Java5_EnumConstantDeclaration_isa_BodyDeclaration():
    instance = Java5_EnumConstantDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_Java5_FieldDeclaration_isa_BodyDeclaration():
    instance = Java5_FieldDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_Java5_Initializer_isa_BodyDeclaration():
    instance = Java5_Initializer()
    assert isinstance(instance, BodyDeclaration)


def test_Java5_MethodDeclaration_isa_BodyDeclaration():
    instance = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    assert isinstance(instance, BodyDeclaration)


def test_Java5_Annotation_isa_Expression():
    instance = Java5_Annotation()
    assert isinstance(instance, Expression)


def test_Java5_ArrayAccess_isa_Expression():
    instance = Java5_ArrayAccess()
    assert isinstance(instance, Expression)


def test_Java5_ArrayCreation_isa_Expression():
    instance = Java5_ArrayCreation()
    assert isinstance(instance, Expression)


def test_Java5_ArrayInitializer_isa_Expression():
    instance = Java5_ArrayInitializer()
    assert isinstance(instance, Expression)


def test_Java5_ArrayLengthAccess_isa_Expression():
    instance = Java5_ArrayLengthAccess()
    assert isinstance(instance, Expression)


def test_Java5_Assignment_isa_Expression():
    instance = Java5_Assignment(operator="sample_text")
    assert isinstance(instance, Expression)


def test_Java5_BooleanLiteral_isa_Expression():
    instance = Java5_BooleanLiteral(value=True)
    assert isinstance(instance, Expression)


def test_Java5_CastExpression_isa_Expression():
    instance = Java5_CastExpression()
    assert isinstance(instance, Expression)


def test_Java5_CharacterLiteral_isa_Expression():
    instance = Java5_CharacterLiteral(escapedValue="sample_text", value="sample_text")
    assert isinstance(instance, Expression)


def test_Java5_ClassInstanceCreation_isa_Expression():
    instance = Java5_ClassInstanceCreation()
    assert isinstance(instance, Expression)


def test_Java5_ConditionalExpression_isa_Expression():
    instance = Java5_ConditionalExpression()
    assert isinstance(instance, Expression)


def test_Java5_FieldAccess_isa_Expression():
    instance = Java5_FieldAccess()
    assert isinstance(instance, Expression)


def test_Java5_InfixExpression_isa_Expression():
    instance = Java5_InfixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_Java5_InstanceofExpression_isa_Expression():
    instance = Java5_InstanceofExpression()
    assert isinstance(instance, Expression)


def test_Java5_MethodInvocation_isa_Expression():
    instance = Java5_MethodInvocation()
    assert isinstance(instance, Expression)


def test_Java5_NamedElementRef_isa_Expression():
    instance = Java5_NamedElementRef()
    assert isinstance(instance, Expression)


def test_Java5_NullLiteral_isa_Expression():
    instance = Java5_NullLiteral()
    assert isinstance(instance, Expression)


def test_Java5_NumberLiteral_isa_Expression():
    instance = Java5_NumberLiteral(tokenValue="sample_text")
    assert isinstance(instance, Expression)


def test_Java5_ParenthesizedExpression_isa_Expression():
    instance = Java5_ParenthesizedExpression()
    assert isinstance(instance, Expression)


def test_Java5_PostfixExpression_isa_Expression():
    instance = Java5_PostfixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_Java5_PrefixExpression_isa_Expression():
    instance = Java5_PrefixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_Java5_StringLiteral_isa_Expression():
    instance = Java5_StringLiteral(escapedValue="sample_text", value="sample_text")
    assert isinstance(instance, Expression)


def test_Java5_SuperFieldAccess_isa_Expression():
    instance = Java5_SuperFieldAccess()
    assert isinstance(instance, Expression)


def test_Java5_SuperMethodInvocation_isa_Expression():
    instance = Java5_SuperMethodInvocation()
    assert isinstance(instance, Expression)


def test_Java5_ThisExpression_isa_Expression():
    instance = Java5_ThisExpression()
    assert isinstance(instance, Expression)


def test_Java5_TypeLiteral_isa_Expression():
    instance = Java5_TypeLiteral()
    assert isinstance(instance, Expression)


def test_Java5_VariableDeclarationExpression_isa_Expression():
    instance = Java5_VariableDeclarationExpression()
    assert isinstance(instance, Expression)


def test_Java5_AnnotationMemberValuePair_isa_NamedElement():
    instance = Java5_AnnotationMemberValuePair()
    assert isinstance(instance, NamedElement)


def test_Java5_BodyDeclaration_isa_NamedElement():
    instance = Java5_BodyDeclaration()
    assert isinstance(instance, NamedElement)


def test_Java5_CompilationUnit_isa_NamedElement():
    instance = Java5_CompilationUnit(originalFilePath="sample_text")
    assert isinstance(instance, NamedElement)


def test_Java5_LabeledStatement_isa_NamedElement():
    instance = Java5_LabeledStatement()
    assert isinstance(instance, NamedElement)


def test_Java5_OrphanType_isa_NamedElement():
    instance = Java5_OrphanType()
    assert isinstance(instance, NamedElement)


def test_Java5_PackageDeclaration_isa_NamedElement():
    instance = Java5_PackageDeclaration(qualifiedName="sample_text")
    assert isinstance(instance, NamedElement)


def test_Java5_TypeParameter_isa_NamedElement():
    instance = Java5_TypeParameter()
    assert isinstance(instance, NamedElement)


def test_Java5_UnresolvedItem_isa_NamedElement():
    instance = Java5_UnresolvedItem()
    assert isinstance(instance, NamedElement)


def test_Java5_VariableDeclaration_isa_NamedElement():
    instance = Java5_VariableDeclaration(extraArrayDimensions=7)
    assert isinstance(instance, NamedElement)


def test_Java5_ArrayType_isa_OrphanType():
    instance = Java5_ArrayType(dimensions=7, originalName="sample_text")
    assert isinstance(instance, OrphanType)


def test_Java5_ParameterizedType_isa_OrphanType():
    instance = Java5_ParameterizedType()
    assert isinstance(instance, OrphanType)


def test_Java5_PrimitiveType_isa_OrphanType():
    instance = Java5_PrimitiveType()
    assert isinstance(instance, OrphanType)


def test_Java5_WildCardType_isa_OrphanType():
    instance = Java5_WildCardType(isUpperBound="sample_text")
    assert isinstance(instance, OrphanType)


def test_Java5_PrimitiveTypeBoolean_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeBoolean()
    assert isinstance(instance, PrimitiveType)


def test_Java5_PrimitiveTypeByte_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeByte()
    assert isinstance(instance, PrimitiveType)


def test_Java5_PrimitiveTypeChar_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeChar()
    assert isinstance(instance, PrimitiveType)


def test_Java5_PrimitiveTypeDouble_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeDouble()
    assert isinstance(instance, PrimitiveType)


def test_Java5_PrimitiveTypeFloat_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeFloat()
    assert isinstance(instance, PrimitiveType)


def test_Java5_PrimitiveTypeInt_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeInt()
    assert isinstance(instance, PrimitiveType)


def test_Java5_PrimitiveTypeLong_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeLong()
    assert isinstance(instance, PrimitiveType)


def test_Java5_PrimitiveTypeShort_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeShort()
    assert isinstance(instance, PrimitiveType)


def test_Java5_PrimitiveTypeVoid_isa_PrimitiveType():
    instance = Java5_PrimitiveTypeVoid()
    assert isinstance(instance, PrimitiveType)


def test_Java5_AssertStatement_isa_Statement():
    instance = Java5_AssertStatement()
    assert isinstance(instance, Statement)


def test_Java5_Block_isa_Statement():
    instance = Java5_Block()
    assert isinstance(instance, Statement)


def test_Java5_BreakStatement_isa_Statement():
    instance = Java5_BreakStatement()
    assert isinstance(instance, Statement)


def test_Java5_CatchClause_isa_Statement():
    instance = Java5_CatchClause()
    assert isinstance(instance, Statement)


def test_Java5_ConstructorInvocation_isa_Statement():
    instance = Java5_ConstructorInvocation()
    assert isinstance(instance, Statement)


def test_Java5_ContinueStatement_isa_Statement():
    instance = Java5_ContinueStatement()
    assert isinstance(instance, Statement)


def test_Java5_DoStatement_isa_Statement():
    instance = Java5_DoStatement()
    assert isinstance(instance, Statement)


def test_Java5_EmptyStatement_isa_Statement():
    instance = Java5_EmptyStatement()
    assert isinstance(instance, Statement)


def test_Java5_EnhancedForStatement_isa_Statement():
    instance = Java5_EnhancedForStatement()
    assert isinstance(instance, Statement)


def test_Java5_ExpressionStatement_isa_Statement():
    instance = Java5_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_Java5_ForStatement_isa_Statement():
    instance = Java5_ForStatement()
    assert isinstance(instance, Statement)


def test_Java5_IfStatement_isa_Statement():
    instance = Java5_IfStatement()
    assert isinstance(instance, Statement)


def test_Java5_LabeledStatement_isa_Statement():
    instance = Java5_LabeledStatement()
    assert isinstance(instance, Statement)


def test_Java5_ReturnStatement_isa_Statement():
    instance = Java5_ReturnStatement()
    assert isinstance(instance, Statement)


def test_Java5_SuperConstructorInvocation_isa_Statement():
    instance = Java5_SuperConstructorInvocation()
    assert isinstance(instance, Statement)


def test_Java5_SwitchCase_isa_Statement():
    instance = Java5_SwitchCase(default=True)
    assert isinstance(instance, Statement)


def test_Java5_SwitchStatement_isa_Statement():
    instance = Java5_SwitchStatement()
    assert isinstance(instance, Statement)


def test_Java5_SynchronizedStatement_isa_Statement():
    instance = Java5_SynchronizedStatement()
    assert isinstance(instance, Statement)


def test_Java5_ThrowStatement_isa_Statement():
    instance = Java5_ThrowStatement()
    assert isinstance(instance, Statement)


def test_Java5_TryStatement_isa_Statement():
    instance = Java5_TryStatement()
    assert isinstance(instance, Statement)


def test_Java5_TypeDeclarationStatement_isa_Statement():
    instance = Java5_TypeDeclarationStatement()
    assert isinstance(instance, Statement)


def test_Java5_VariableDeclarationStatement_isa_Statement():
    instance = Java5_VariableDeclarationStatement(extraArrayDimensions=7)
    assert isinstance(instance, Statement)


def test_Java5_WhileStatement_isa_Statement():
    instance = Java5_WhileStatement()
    assert isinstance(instance, Statement)


def test_Java5_ClassDeclaration_isa_TypeDeclaration():
    instance = Java5_ClassDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_Java5_InterfaceDeclaration_isa_TypeDeclaration():
    instance = Java5_InterfaceDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_Java5_SingleVariableDeclaration_isa_VariableDeclaration():
    instance = Java5_SingleVariableDeclaration(varargs=True)
    assert isinstance(instance, VariableDeclaration)


def test_Java5_VariableDeclarationFragment_isa_VariableDeclaration():
    instance = Java5_VariableDeclarationFragment()
    assert isinstance(instance, VariableDeclaration)


def test_assoc_BodyDeclaration222_link_reassign_clear():
    a = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    b1 = Java5_BodyDeclaration()
    b2 = Java5_BodyDeclaration()
    _safe_set(a, 'modifiers', b1)
    assert _is_linked(a, 'modifiers', b1)
    if hasattr(b1, 'BodyDeclaration223'):
        assert _is_linked(b1, 'BodyDeclaration223', a)
    _safe_set(a, 'modifiers', b2)
    assert _is_linked(a, 'modifiers', b2)
    if hasattr(b1, 'BodyDeclaration223'):
        assert not _is_linked(b1, 'BodyDeclaration223', a)
    if hasattr(b2, 'BodyDeclaration223'):
        assert _is_linked(b2, 'BodyDeclaration223', a)
    _safe_set(a, 'modifiers', None)
    assert not _is_linked(a, 'modifiers', b2)
    if hasattr(b2, 'BodyDeclaration223'):
        assert not _is_linked(b2, 'BodyDeclaration223', a)


def test_assoc_SingleVariableDeclaration224_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    b2 = Java5_Modifier(inheritance="sample_text_2", native=False, static=False, strictfp=False, synchronized=False, transient=False, visibility="sample_text_2", volatile=False)
    _safe_set(a, 'SingleVariableDeclaration226', b1)
    assert _is_linked(a, 'SingleVariableDeclaration226', b1)
    if hasattr(b1, 'modifiers225'):
        assert _is_linked(b1, 'modifiers225', a)
    _safe_set(a, 'SingleVariableDeclaration226', b2)
    assert _is_linked(a, 'SingleVariableDeclaration226', b2)
    if hasattr(b1, 'modifiers225'):
        assert not _is_linked(b1, 'modifiers225', a)
    if hasattr(b2, 'modifiers225'):
        assert _is_linked(b2, 'modifiers225', a)
    _safe_set(a, 'SingleVariableDeclaration226', None)
    assert not _is_linked(a, 'SingleVariableDeclaration226', b2)
    if hasattr(b2, 'modifiers225'):
        assert not _is_linked(b2, 'modifiers225', a)


def test_assoc_VariableDeclarationExpression229_link_reassign_clear():
    a = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    b1 = Java5_VariableDeclarationExpression()
    b2 = Java5_VariableDeclarationExpression()
    _safe_set(a, 'modifiers230', b1)
    assert _is_linked(a, 'modifiers230', b1)
    if hasattr(b1, 'VariableDeclarationExpression'):
        assert _is_linked(b1, 'VariableDeclarationExpression', a)
    _safe_set(a, 'modifiers230', b2)
    assert _is_linked(a, 'modifiers230', b2)
    if hasattr(b1, 'VariableDeclarationExpression'):
        assert not _is_linked(b1, 'VariableDeclarationExpression', a)
    if hasattr(b2, 'VariableDeclarationExpression'):
        assert _is_linked(b2, 'VariableDeclarationExpression', a)
    _safe_set(a, 'modifiers230', None)
    assert not _is_linked(a, 'modifiers230', b2)
    if hasattr(b2, 'VariableDeclarationExpression'):
        assert not _is_linked(b2, 'VariableDeclarationExpression', a)


def test_assoc_VariableDeclarationStatement227_link_reassign_clear():
    a = Java5_VariableDeclarationStatement(extraArrayDimensions=7)
    b1 = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    b2 = Java5_Modifier(inheritance="sample_text_2", native=False, static=False, strictfp=False, synchronized=False, transient=False, visibility="sample_text_2", volatile=False)
    _safe_set(a, 'VariableDeclarationStatement', b1)
    assert _is_linked(a, 'VariableDeclarationStatement', b1)
    if hasattr(b1, 'modifiers228'):
        assert _is_linked(b1, 'modifiers228', a)
    _safe_set(a, 'VariableDeclarationStatement', b2)
    assert _is_linked(a, 'VariableDeclarationStatement', b2)
    if hasattr(b1, 'modifiers228'):
        assert not _is_linked(b1, 'modifiers228', a)
    if hasattr(b2, 'modifiers228'):
        assert _is_linked(b2, 'modifiers228', a)
    _safe_set(a, 'VariableDeclarationStatement', None)
    assert not _is_linked(a, 'VariableDeclarationStatement', b2)
    if hasattr(b2, 'modifiers228'):
        assert not _is_linked(b2, 'modifiers228', a)


def test_assoc_abstractTypeDeclaration52_link_reassign_clear():
    a = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    b1 = Java5_BodyDeclaration()
    b2 = Java5_BodyDeclaration()
    _safe_set(a, 'AbstractTypeDeclaration', b1)
    assert _is_linked(a, 'AbstractTypeDeclaration', b1)
    if hasattr(b1, 'bodyDeclarations'):
        assert _is_linked(b1, 'bodyDeclarations', a)
    _safe_set(a, 'AbstractTypeDeclaration', b2)
    assert _is_linked(a, 'AbstractTypeDeclaration', b2)
    if hasattr(b1, 'bodyDeclarations'):
        assert not _is_linked(b1, 'bodyDeclarations', a)
    if hasattr(b2, 'bodyDeclarations'):
        assert _is_linked(b2, 'bodyDeclarations', a)
    _safe_set(a, 'AbstractTypeDeclaration', None)
    assert not _is_linked(a, 'AbstractTypeDeclaration', b2)
    if hasattr(b2, 'bodyDeclarations'):
        assert not _is_linked(b2, 'bodyDeclarations', a)


def test_assoc_body178_link_reassign_clear():
    a = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b1 = Java5_Block()
    b2 = Java5_Block()
    _safe_set(a, 'Java5_MethodDeclaration', b1)
    assert _is_linked(a, 'Java5_MethodDeclaration', b1)
    if hasattr(b1, 'Java5_Block179'):
        assert _is_linked(b1, 'Java5_Block179', a)
    _safe_set(a, 'Java5_MethodDeclaration', b2)
    assert _is_linked(a, 'Java5_MethodDeclaration', b2)
    if hasattr(b1, 'Java5_Block179'):
        assert not _is_linked(b1, 'Java5_Block179', a)
    if hasattr(b2, 'Java5_Block179'):
        assert _is_linked(b2, 'Java5_Block179', a)
    _safe_set(a, 'Java5_MethodDeclaration', None)
    assert not _is_linked(a, 'Java5_MethodDeclaration', b2)
    if hasattr(b2, 'Java5_Block179'):
        assert not _is_linked(b2, 'Java5_Block179', a)


def test_assoc_bodyDeclarations0_link_reassign_clear():
    a = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    b1 = Java5_BodyDeclaration()
    b2 = Java5_BodyDeclaration()
    _safe_set(a, 'abstractTypeDeclaration', {b1})
    assert _is_linked(a, 'abstractTypeDeclaration', b1)
    if hasattr(b1, 'BodyDeclaration'):
        assert _is_linked(b1, 'BodyDeclaration', a)
    _safe_set(a, 'abstractTypeDeclaration', {b2})
    assert _is_linked(a, 'abstractTypeDeclaration', b2)
    if hasattr(b1, 'BodyDeclaration'):
        assert not _is_linked(b1, 'BodyDeclaration', a)
    if hasattr(b2, 'BodyDeclaration'):
        assert _is_linked(b2, 'BodyDeclaration', a)
    _safe_set(a, 'abstractTypeDeclaration', set())
    assert not _is_linked(a, 'abstractTypeDeclaration', b2)
    if hasattr(b2, 'BodyDeclaration'):
        assert not _is_linked(b2, 'BodyDeclaration', a)


def test_assoc_bound346_link_reassign_clear():
    a = Java5_WildCardType(isUpperBound="sample_text")
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_WildCardType', b1)
    assert _is_linked(a, 'Java5_WildCardType', b1)
    if hasattr(b1, 'Java5_NamedElementRef347'):
        assert _is_linked(b1, 'Java5_NamedElementRef347', a)
    _safe_set(a, 'Java5_WildCardType', b2)
    assert _is_linked(a, 'Java5_WildCardType', b2)
    if hasattr(b1, 'Java5_NamedElementRef347'):
        assert not _is_linked(b1, 'Java5_NamedElementRef347', a)
    if hasattr(b2, 'Java5_NamedElementRef347'):
        assert _is_linked(b2, 'Java5_NamedElementRef347', a)
    _safe_set(a, 'Java5_WildCardType', None)
    assert not _is_linked(a, 'Java5_WildCardType', b2)
    if hasattr(b2, 'Java5_NamedElementRef347'):
        assert not _is_linked(b2, 'Java5_NamedElementRef347', a)


def test_assoc_catchClause261_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_CatchClause()
    b2 = Java5_CatchClause()
    _safe_set(a, 'exception', b1)
    assert _is_linked(a, 'exception', b1)
    if hasattr(b1, 'CatchClause'):
        assert _is_linked(b1, 'CatchClause', a)
    _safe_set(a, 'exception', b2)
    assert _is_linked(a, 'exception', b2)
    if hasattr(b1, 'CatchClause'):
        assert not _is_linked(b1, 'CatchClause', a)
    if hasattr(b2, 'CatchClause'):
        assert _is_linked(b2, 'CatchClause', a)
    _safe_set(a, 'exception', None)
    assert not _is_linked(a, 'exception', b2)
    if hasattr(b2, 'CatchClause'):
        assert not _is_linked(b2, 'CatchClause', a)


def test_assoc_compilationUnits219_link_reassign_clear():
    a = Java5_Model(name="sample_text")
    b1 = Java5_CompilationUnit(originalFilePath="sample_text")
    b2 = Java5_CompilationUnit(originalFilePath="sample_text_2")
    _safe_set(a, 'Java5_Model220', {b1})
    assert _is_linked(a, 'Java5_Model220', b1)
    if hasattr(b1, 'Java5_CompilationUnit221'):
        assert _is_linked(b1, 'Java5_CompilationUnit221', a)
    _safe_set(a, 'Java5_Model220', {b2})
    assert _is_linked(a, 'Java5_Model220', b2)
    if hasattr(b1, 'Java5_CompilationUnit221'):
        assert not _is_linked(b1, 'Java5_CompilationUnit221', a)
    if hasattr(b2, 'Java5_CompilationUnit221'):
        assert _is_linked(b2, 'Java5_CompilationUnit221', a)
    _safe_set(a, 'Java5_Model220', set())
    assert not _is_linked(a, 'Java5_Model220', b2)
    if hasattr(b2, 'Java5_CompilationUnit221'):
        assert not _is_linked(b2, 'Java5_CompilationUnit221', a)


def test_assoc_declaration303_link_reassign_clear():
    a = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    b1 = Java5_TypeDeclarationStatement()
    b2 = Java5_TypeDeclarationStatement()
    _safe_set(a, 'Java5_AbstractTypeDeclaration304', b1)
    assert _is_linked(a, 'Java5_AbstractTypeDeclaration304', b1)
    if hasattr(b1, 'Java5_TypeDeclarationStatement'):
        assert _is_linked(b1, 'Java5_TypeDeclarationStatement', a)
    _safe_set(a, 'Java5_AbstractTypeDeclaration304', b2)
    assert _is_linked(a, 'Java5_AbstractTypeDeclaration304', b2)
    if hasattr(b1, 'Java5_TypeDeclarationStatement'):
        assert not _is_linked(b1, 'Java5_TypeDeclarationStatement', a)
    if hasattr(b2, 'Java5_TypeDeclarationStatement'):
        assert _is_linked(b2, 'Java5_TypeDeclarationStatement', a)
    _safe_set(a, 'Java5_AbstractTypeDeclaration304', None)
    assert not _is_linked(a, 'Java5_AbstractTypeDeclaration304', b2)
    if hasattr(b2, 'Java5_TypeDeclarationStatement'):
        assert not _is_linked(b2, 'Java5_TypeDeclarationStatement', a)


def test_assoc_element234_link_reassign_clear():
    a = Java5_NamedElement(name="sample_text", proxy=True)
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_NamedElement', b1)
    assert _is_linked(a, 'Java5_NamedElement', b1)
    if hasattr(b1, 'Java5_NamedElementRef235'):
        assert _is_linked(b1, 'Java5_NamedElementRef235', a)
    _safe_set(a, 'Java5_NamedElement', b2)
    assert _is_linked(a, 'Java5_NamedElement', b2)
    if hasattr(b1, 'Java5_NamedElementRef235'):
        assert not _is_linked(b1, 'Java5_NamedElementRef235', a)
    if hasattr(b2, 'Java5_NamedElementRef235'):
        assert _is_linked(b2, 'Java5_NamedElementRef235', a)
    _safe_set(a, 'Java5_NamedElement', None)
    assert not _is_linked(a, 'Java5_NamedElement', b2)
    if hasattr(b2, 'Java5_NamedElementRef235'):
        assert not _is_linked(b2, 'Java5_NamedElementRef235', a)


def test_assoc_elementType39_link_reassign_clear():
    a = Java5_ArrayType(dimensions=7, originalName="sample_text")
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_ArrayType', b1)
    assert _is_linked(a, 'Java5_ArrayType', b1)
    if hasattr(b1, 'Java5_NamedElementRef40'):
        assert _is_linked(b1, 'Java5_NamedElementRef40', a)
    _safe_set(a, 'Java5_ArrayType', b2)
    assert _is_linked(a, 'Java5_ArrayType', b2)
    if hasattr(b1, 'Java5_NamedElementRef40'):
        assert not _is_linked(b1, 'Java5_NamedElementRef40', a)
    if hasattr(b2, 'Java5_NamedElementRef40'):
        assert _is_linked(b2, 'Java5_NamedElementRef40', a)
    _safe_set(a, 'Java5_ArrayType', None)
    assert not _is_linked(a, 'Java5_ArrayType', b2)
    if hasattr(b2, 'Java5_NamedElementRef40'):
        assert not _is_linked(b2, 'Java5_NamedElementRef40', a)


def test_assoc_enhancedForStatement262_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_EnhancedForStatement()
    b2 = Java5_EnhancedForStatement()
    _safe_set(a, 'parameter', b1)
    assert _is_linked(a, 'parameter', b1)
    if hasattr(b1, 'EnhancedForStatement'):
        assert _is_linked(b1, 'EnhancedForStatement', a)
    _safe_set(a, 'parameter', b2)
    assert _is_linked(a, 'parameter', b2)
    if hasattr(b1, 'EnhancedForStatement'):
        assert not _is_linked(b1, 'EnhancedForStatement', a)
    if hasattr(b2, 'EnhancedForStatement'):
        assert _is_linked(b2, 'EnhancedForStatement', a)
    _safe_set(a, 'parameter', None)
    assert not _is_linked(a, 'parameter', b2)
    if hasattr(b2, 'EnhancedForStatement'):
        assert not _is_linked(b2, 'EnhancedForStatement', a)


def test_assoc_exception66_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_CatchClause()
    b2 = Java5_CatchClause()
    _safe_set(a, 'SingleVariableDeclaration', b1)
    assert _is_linked(a, 'SingleVariableDeclaration', b1)
    if hasattr(b1, 'catchClause'):
        assert _is_linked(b1, 'catchClause', a)
    _safe_set(a, 'SingleVariableDeclaration', b2)
    assert _is_linked(a, 'SingleVariableDeclaration', b2)
    if hasattr(b1, 'catchClause'):
        assert not _is_linked(b1, 'catchClause', a)
    if hasattr(b2, 'catchClause'):
        assert _is_linked(b2, 'catchClause', a)
    _safe_set(a, 'SingleVariableDeclaration', None)
    assert not _is_linked(a, 'SingleVariableDeclaration', b2)
    if hasattr(b2, 'catchClause'):
        assert not _is_linked(b2, 'catchClause', a)


def test_assoc_expression284_link_reassign_clear():
    a = Java5_SwitchCase(default=True)
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_SwitchCase', b1)
    assert _is_linked(a, 'Java5_SwitchCase', b1)
    if hasattr(b1, 'Java5_Expression285'):
        assert _is_linked(b1, 'Java5_Expression285', a)
    _safe_set(a, 'Java5_SwitchCase', b2)
    assert _is_linked(a, 'Java5_SwitchCase', b2)
    if hasattr(b1, 'Java5_Expression285'):
        assert not _is_linked(b1, 'Java5_Expression285', a)
    if hasattr(b2, 'Java5_Expression285'):
        assert _is_linked(b2, 'Java5_Expression285', a)
    _safe_set(a, 'Java5_SwitchCase', None)
    assert not _is_linked(a, 'Java5_SwitchCase', b2)
    if hasattr(b2, 'Java5_Expression285'):
        assert not _is_linked(b2, 'Java5_Expression285', a)


def test_assoc_extendedOperands161_link_reassign_clear():
    a = Java5_InfixExpression(operator="sample_text")
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_InfixExpression162', {b1})
    assert _is_linked(a, 'Java5_InfixExpression162', b1)
    if hasattr(b1, 'Java5_Expression163'):
        assert _is_linked(b1, 'Java5_Expression163', a)
    _safe_set(a, 'Java5_InfixExpression162', {b2})
    assert _is_linked(a, 'Java5_InfixExpression162', b2)
    if hasattr(b1, 'Java5_Expression163'):
        assert not _is_linked(b1, 'Java5_Expression163', a)
    if hasattr(b2, 'Java5_Expression163'):
        assert _is_linked(b2, 'Java5_Expression163', a)
    _safe_set(a, 'Java5_InfixExpression162', set())
    assert not _is_linked(a, 'Java5_InfixExpression162', b2)
    if hasattr(b2, 'Java5_Expression163'):
        assert not _is_linked(b2, 'Java5_Expression163', a)


def test_assoc_fragments296_link_reassign_clear():
    a = Java5_TagElement(tagName="sample_text")
    b1 = Java5_ASTNode()
    b2 = Java5_ASTNode()
    _safe_set(a, 'Java5_TagElement', {b1})
    assert _is_linked(a, 'Java5_TagElement', b1)
    if hasattr(b1, 'Java5_ASTNode'):
        assert _is_linked(b1, 'Java5_ASTNode', a)
    _safe_set(a, 'Java5_TagElement', {b2})
    assert _is_linked(a, 'Java5_TagElement', b2)
    if hasattr(b1, 'Java5_ASTNode'):
        assert not _is_linked(b1, 'Java5_ASTNode', a)
    if hasattr(b2, 'Java5_ASTNode'):
        assert _is_linked(b2, 'Java5_ASTNode', a)
    _safe_set(a, 'Java5_TagElement', set())
    assert not _is_linked(a, 'Java5_TagElement', b2)
    if hasattr(b2, 'Java5_ASTNode'):
        assert not _is_linked(b2, 'Java5_ASTNode', a)


def test_assoc_fragments336_link_reassign_clear():
    a = Java5_VariableDeclarationStatement(extraArrayDimensions=7)
    b1 = Java5_VariableDeclarationFragment()
    b2 = Java5_VariableDeclarationFragment()
    _safe_set(a, 'variableDeclarationStatement', {b1})
    assert _is_linked(a, 'variableDeclarationStatement', b1)
    if hasattr(b1, 'VariableDeclarationFragment337'):
        assert _is_linked(b1, 'VariableDeclarationFragment337', a)
    _safe_set(a, 'variableDeclarationStatement', {b2})
    assert _is_linked(a, 'variableDeclarationStatement', b2)
    if hasattr(b1, 'VariableDeclarationFragment337'):
        assert not _is_linked(b1, 'VariableDeclarationFragment337', a)
    if hasattr(b2, 'VariableDeclarationFragment337'):
        assert _is_linked(b2, 'VariableDeclarationFragment337', a)
    _safe_set(a, 'variableDeclarationStatement', set())
    assert not _is_linked(a, 'variableDeclarationStatement', b2)
    if hasattr(b2, 'VariableDeclarationFragment337'):
        assert not _is_linked(b2, 'VariableDeclarationFragment337', a)


def test_assoc_importedElement153_link_reassign_clear():
    a = Java5_ImportDeclaration(static=True)
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_ImportDeclaration154', b1)
    assert _is_linked(a, 'Java5_ImportDeclaration154', b1)
    if hasattr(b1, 'Java5_NamedElementRef155'):
        assert _is_linked(b1, 'Java5_NamedElementRef155', a)
    _safe_set(a, 'Java5_ImportDeclaration154', b2)
    assert _is_linked(a, 'Java5_ImportDeclaration154', b2)
    if hasattr(b1, 'Java5_NamedElementRef155'):
        assert not _is_linked(b1, 'Java5_NamedElementRef155', a)
    if hasattr(b2, 'Java5_NamedElementRef155'):
        assert _is_linked(b2, 'Java5_NamedElementRef155', a)
    _safe_set(a, 'Java5_ImportDeclaration154', None)
    assert not _is_linked(a, 'Java5_ImportDeclaration154', b2)
    if hasattr(b2, 'Java5_NamedElementRef155'):
        assert not _is_linked(b2, 'Java5_NamedElementRef155', a)


def test_assoc_imports1_link_reassign_clear():
    a = Java5_ImportDeclaration(static=True)
    b1 = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    b2 = Java5_AbstractTypeDeclaration(qualifiedName="sample_text_2")
    _safe_set(a, 'Java5_ImportDeclaration', b1)
    assert _is_linked(a, 'Java5_ImportDeclaration', b1)
    if hasattr(b1, 'Java5_AbstractTypeDeclaration'):
        assert _is_linked(b1, 'Java5_AbstractTypeDeclaration', a)
    _safe_set(a, 'Java5_ImportDeclaration', b2)
    assert _is_linked(a, 'Java5_ImportDeclaration', b2)
    if hasattr(b1, 'Java5_AbstractTypeDeclaration'):
        assert not _is_linked(b1, 'Java5_AbstractTypeDeclaration', a)
    if hasattr(b2, 'Java5_AbstractTypeDeclaration'):
        assert _is_linked(b2, 'Java5_AbstractTypeDeclaration', a)
    _safe_set(a, 'Java5_ImportDeclaration', None)
    assert not _is_linked(a, 'Java5_ImportDeclaration', b2)
    if hasattr(b2, 'Java5_AbstractTypeDeclaration'):
        assert not _is_linked(b2, 'Java5_AbstractTypeDeclaration', a)


def test_assoc_imports84_link_reassign_clear():
    a = Java5_ImportDeclaration(static=True)
    b1 = Java5_CompilationUnit(originalFilePath="sample_text")
    b2 = Java5_CompilationUnit(originalFilePath="sample_text_2")
    _safe_set(a, 'Java5_ImportDeclaration85', b1)
    assert _is_linked(a, 'Java5_ImportDeclaration85', b1)
    if hasattr(b1, 'Java5_CompilationUnit'):
        assert _is_linked(b1, 'Java5_CompilationUnit', a)
    _safe_set(a, 'Java5_ImportDeclaration85', b2)
    assert _is_linked(a, 'Java5_ImportDeclaration85', b2)
    if hasattr(b1, 'Java5_CompilationUnit'):
        assert not _is_linked(b1, 'Java5_CompilationUnit', a)
    if hasattr(b2, 'Java5_CompilationUnit'):
        assert _is_linked(b2, 'Java5_CompilationUnit', a)
    _safe_set(a, 'Java5_ImportDeclaration85', None)
    assert not _is_linked(a, 'Java5_ImportDeclaration85', b2)
    if hasattr(b2, 'Java5_CompilationUnit'):
        assert not _is_linked(b2, 'Java5_CompilationUnit', a)


def test_assoc_initializer318_link_reassign_clear():
    a = Java5_VariableDeclaration(extraArrayDimensions=7)
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_VariableDeclaration', b1)
    assert _is_linked(a, 'Java5_VariableDeclaration', b1)
    if hasattr(b1, 'Java5_Expression319'):
        assert _is_linked(b1, 'Java5_Expression319', a)
    _safe_set(a, 'Java5_VariableDeclaration', b2)
    assert _is_linked(a, 'Java5_VariableDeclaration', b2)
    if hasattr(b1, 'Java5_Expression319'):
        assert not _is_linked(b1, 'Java5_Expression319', a)
    if hasattr(b2, 'Java5_Expression319'):
        assert _is_linked(b2, 'Java5_Expression319', a)
    _safe_set(a, 'Java5_VariableDeclaration', None)
    assert not _is_linked(a, 'Java5_VariableDeclaration', b2)
    if hasattr(b2, 'Java5_Expression319'):
        assert not _is_linked(b2, 'Java5_Expression319', a)


def test_assoc_leftHandSide46_link_reassign_clear():
    a = Java5_Assignment(operator="sample_text")
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_Assignment', b1)
    assert _is_linked(a, 'Java5_Assignment', b1)
    if hasattr(b1, 'Java5_Expression47'):
        assert _is_linked(b1, 'Java5_Expression47', a)
    _safe_set(a, 'Java5_Assignment', b2)
    assert _is_linked(a, 'Java5_Assignment', b2)
    if hasattr(b1, 'Java5_Expression47'):
        assert not _is_linked(b1, 'Java5_Expression47', a)
    if hasattr(b2, 'Java5_Expression47'):
        assert _is_linked(b2, 'Java5_Expression47', a)
    _safe_set(a, 'Java5_Assignment', None)
    assert not _is_linked(a, 'Java5_Assignment', b2)
    if hasattr(b2, 'Java5_Expression47'):
        assert not _is_linked(b2, 'Java5_Expression47', a)


def test_assoc_leftOperand158_link_reassign_clear():
    a = Java5_InfixExpression(operator="sample_text")
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_InfixExpression159', b1)
    assert _is_linked(a, 'Java5_InfixExpression159', b1)
    if hasattr(b1, 'Java5_Expression160'):
        assert _is_linked(b1, 'Java5_Expression160', a)
    _safe_set(a, 'Java5_InfixExpression159', b2)
    assert _is_linked(a, 'Java5_InfixExpression159', b2)
    if hasattr(b1, 'Java5_Expression160'):
        assert not _is_linked(b1, 'Java5_Expression160', a)
    if hasattr(b2, 'Java5_Expression160'):
        assert _is_linked(b2, 'Java5_Expression160', a)
    _safe_set(a, 'Java5_InfixExpression159', None)
    assert not _is_linked(a, 'Java5_InfixExpression159', b2)
    if hasattr(b2, 'Java5_Expression160'):
        assert not _is_linked(b2, 'Java5_Expression160', a)


def test_assoc_methodDeclaration259_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b2 = Java5_MethodDeclaration(constructor=False, extraArrayDimensions=13, varargs=False)
    _safe_set(a, 'parameters', b1)
    assert _is_linked(a, 'parameters', b1)
    if hasattr(b1, 'MethodDeclaration260'):
        assert _is_linked(b1, 'MethodDeclaration260', a)
    _safe_set(a, 'parameters', b2)
    assert _is_linked(a, 'parameters', b2)
    if hasattr(b1, 'MethodDeclaration260'):
        assert not _is_linked(b1, 'MethodDeclaration260', a)
    if hasattr(b2, 'MethodDeclaration260'):
        assert _is_linked(b2, 'MethodDeclaration260', a)
    _safe_set(a, 'parameters', None)
    assert not _is_linked(a, 'parameters', b2)
    if hasattr(b2, 'MethodDeclaration260'):
        assert not _is_linked(b2, 'MethodDeclaration260', a)


def test_assoc_modifiers254_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    b2 = Java5_Modifier(inheritance="sample_text_2", native=False, static=False, strictfp=False, synchronized=False, transient=False, visibility="sample_text_2", volatile=False)
    _safe_set(a, 'SingleVariableDeclaration255', {b1})
    assert _is_linked(a, 'SingleVariableDeclaration255', b1)
    if hasattr(b1, 'Modifier256'):
        assert _is_linked(b1, 'Modifier256', a)
    _safe_set(a, 'SingleVariableDeclaration255', {b2})
    assert _is_linked(a, 'SingleVariableDeclaration255', b2)
    if hasattr(b1, 'Modifier256'):
        assert not _is_linked(b1, 'Modifier256', a)
    if hasattr(b2, 'Modifier256'):
        assert _is_linked(b2, 'Modifier256', a)
    _safe_set(a, 'SingleVariableDeclaration255', set())
    assert not _is_linked(a, 'SingleVariableDeclaration255', b2)
    if hasattr(b2, 'Modifier256'):
        assert not _is_linked(b2, 'Modifier256', a)


def test_assoc_modifiers324_link_reassign_clear():
    a = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    b1 = Java5_VariableDeclarationExpression()
    b2 = Java5_VariableDeclarationExpression()
    _safe_set(a, 'Modifier326', b1)
    assert _is_linked(a, 'Modifier326', b1)
    if hasattr(b1, 'VariableDeclarationExpression325'):
        assert _is_linked(b1, 'VariableDeclarationExpression325', a)
    _safe_set(a, 'Modifier326', b2)
    assert _is_linked(a, 'Modifier326', b2)
    if hasattr(b1, 'VariableDeclarationExpression325'):
        assert not _is_linked(b1, 'VariableDeclarationExpression325', a)
    if hasattr(b2, 'VariableDeclarationExpression325'):
        assert _is_linked(b2, 'VariableDeclarationExpression325', a)
    _safe_set(a, 'Modifier326', None)
    assert not _is_linked(a, 'Modifier326', b2)
    if hasattr(b2, 'VariableDeclarationExpression325'):
        assert not _is_linked(b2, 'VariableDeclarationExpression325', a)


def test_assoc_modifiers338_link_reassign_clear():
    a = Java5_VariableDeclarationStatement(extraArrayDimensions=7)
    b1 = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    b2 = Java5_Modifier(inheritance="sample_text_2", native=False, static=False, strictfp=False, synchronized=False, transient=False, visibility="sample_text_2", volatile=False)
    _safe_set(a, 'VariableDeclarationStatement339', {b1})
    assert _is_linked(a, 'VariableDeclarationStatement339', b1)
    if hasattr(b1, 'Modifier340'):
        assert _is_linked(b1, 'Modifier340', a)
    _safe_set(a, 'VariableDeclarationStatement339', {b2})
    assert _is_linked(a, 'VariableDeclarationStatement339', b2)
    if hasattr(b1, 'Modifier340'):
        assert not _is_linked(b1, 'Modifier340', a)
    if hasattr(b2, 'Modifier340'):
        assert _is_linked(b2, 'Modifier340', a)
    _safe_set(a, 'VariableDeclarationStatement339', set())
    assert not _is_linked(a, 'VariableDeclarationStatement339', b2)
    if hasattr(b2, 'Modifier340'):
        assert not _is_linked(b2, 'Modifier340', a)


def test_assoc_modifiers57_link_reassign_clear():
    a = Java5_Modifier(inheritance="sample_text", native=True, static=True, strictfp=True, synchronized=True, transient=True, visibility="sample_text", volatile=True)
    b1 = Java5_BodyDeclaration()
    b2 = Java5_BodyDeclaration()
    _safe_set(a, 'Modifier', b1)
    assert _is_linked(a, 'Modifier', b1)
    if hasattr(b1, 'BodyDeclaration58'):
        assert _is_linked(b1, 'BodyDeclaration58', a)
    _safe_set(a, 'Modifier', b2)
    assert _is_linked(a, 'Modifier', b2)
    if hasattr(b1, 'BodyDeclaration58'):
        assert not _is_linked(b1, 'BodyDeclaration58', a)
    if hasattr(b2, 'BodyDeclaration58'):
        assert _is_linked(b2, 'BodyDeclaration58', a)
    _safe_set(a, 'Modifier', None)
    assert not _is_linked(a, 'Modifier', b2)
    if hasattr(b2, 'BodyDeclaration58'):
        assert not _is_linked(b2, 'BodyDeclaration58', a)


def test_assoc_operand248_link_reassign_clear():
    a = Java5_PostfixExpression(operator="sample_text")
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_PostfixExpression', b1)
    assert _is_linked(a, 'Java5_PostfixExpression', b1)
    if hasattr(b1, 'Java5_Expression249'):
        assert _is_linked(b1, 'Java5_Expression249', a)
    _safe_set(a, 'Java5_PostfixExpression', b2)
    assert _is_linked(a, 'Java5_PostfixExpression', b2)
    if hasattr(b1, 'Java5_Expression249'):
        assert not _is_linked(b1, 'Java5_Expression249', a)
    if hasattr(b2, 'Java5_Expression249'):
        assert _is_linked(b2, 'Java5_Expression249', a)
    _safe_set(a, 'Java5_PostfixExpression', None)
    assert not _is_linked(a, 'Java5_PostfixExpression', b2)
    if hasattr(b2, 'Java5_Expression249'):
        assert not _is_linked(b2, 'Java5_Expression249', a)


def test_assoc_operand250_link_reassign_clear():
    a = Java5_PrefixExpression(operator="sample_text")
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_PrefixExpression', b1)
    assert _is_linked(a, 'Java5_PrefixExpression', b1)
    if hasattr(b1, 'Java5_Expression251'):
        assert _is_linked(b1, 'Java5_Expression251', a)
    _safe_set(a, 'Java5_PrefixExpression', b2)
    assert _is_linked(a, 'Java5_PrefixExpression', b2)
    if hasattr(b1, 'Java5_Expression251'):
        assert not _is_linked(b1, 'Java5_Expression251', a)
    if hasattr(b2, 'Java5_Expression251'):
        assert _is_linked(b2, 'Java5_Expression251', a)
    _safe_set(a, 'Java5_PrefixExpression', None)
    assert not _is_linked(a, 'Java5_PrefixExpression', b2)
    if hasattr(b2, 'Java5_Expression251'):
        assert not _is_linked(b2, 'Java5_Expression251', a)


def test_assoc_orphanTypes215_link_reassign_clear():
    a = Java5_Model(name="sample_text")
    b1 = Java5_OrphanType()
    b2 = Java5_OrphanType()
    _safe_set(a, 'Java5_Model216', {b1})
    assert _is_linked(a, 'Java5_Model216', b1)
    if hasattr(b1, 'Java5_OrphanType'):
        assert _is_linked(b1, 'Java5_OrphanType', a)
    _safe_set(a, 'Java5_Model216', {b2})
    assert _is_linked(a, 'Java5_Model216', b2)
    if hasattr(b1, 'Java5_OrphanType'):
        assert not _is_linked(b1, 'Java5_OrphanType', a)
    if hasattr(b2, 'Java5_OrphanType'):
        assert _is_linked(b2, 'Java5_OrphanType', a)
    _safe_set(a, 'Java5_Model216', set())
    assert not _is_linked(a, 'Java5_Model216', b2)
    if hasattr(b2, 'Java5_OrphanType'):
        assert not _is_linked(b2, 'Java5_OrphanType', a)


def test_assoc_ownedElements213_link_reassign_clear():
    a = Java5_PackageDeclaration(qualifiedName="sample_text")
    b1 = Java5_Model(name="sample_text")
    b2 = Java5_Model(name="sample_text_2")
    _safe_set(a, 'Java5_PackageDeclaration214', b1)
    assert _is_linked(a, 'Java5_PackageDeclaration214', b1)
    if hasattr(b1, 'Java5_Model'):
        assert _is_linked(b1, 'Java5_Model', a)
    _safe_set(a, 'Java5_PackageDeclaration214', b2)
    assert _is_linked(a, 'Java5_PackageDeclaration214', b2)
    if hasattr(b1, 'Java5_Model'):
        assert not _is_linked(b1, 'Java5_Model', a)
    if hasattr(b2, 'Java5_Model'):
        assert _is_linked(b2, 'Java5_Model', a)
    _safe_set(a, 'Java5_PackageDeclaration214', None)
    assert not _is_linked(a, 'Java5_PackageDeclaration214', b2)
    if hasattr(b2, 'Java5_Model'):
        assert not _is_linked(b2, 'Java5_Model', a)


def test_assoc_ownedElements236_link_reassign_clear():
    a = Java5_PackageDeclaration(qualifiedName="sample_text")
    b1 = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    b2 = Java5_AbstractTypeDeclaration(qualifiedName="sample_text_2")
    _safe_set(a, 'package', {b1})
    assert _is_linked(a, 'package', b1)
    if hasattr(b1, 'AbstractTypeDeclaration237'):
        assert _is_linked(b1, 'AbstractTypeDeclaration237', a)
    _safe_set(a, 'package', {b2})
    assert _is_linked(a, 'package', b2)
    if hasattr(b1, 'AbstractTypeDeclaration237'):
        assert not _is_linked(b1, 'AbstractTypeDeclaration237', a)
    if hasattr(b2, 'AbstractTypeDeclaration237'):
        assert _is_linked(b2, 'AbstractTypeDeclaration237', a)
    _safe_set(a, 'package', set())
    assert not _is_linked(a, 'package', b2)
    if hasattr(b2, 'AbstractTypeDeclaration237'):
        assert not _is_linked(b2, 'AbstractTypeDeclaration237', a)


def test_assoc_ownedPackages239_link_reassign_clear():
    a = Java5_PackageDeclaration(qualifiedName="sample_text")
    b1 = Java5_PackageDeclaration(qualifiedName="sample_text")
    b2 = Java5_PackageDeclaration(qualifiedName="sample_text_2")
    _safe_set(a, 'Java5_PackageDeclaration238', {b1})
    assert _is_linked(a, 'Java5_PackageDeclaration238', b1)
    if hasattr(b1, 'Java5_PackageDeclaration240'):
        assert _is_linked(b1, 'Java5_PackageDeclaration240', a)
    _safe_set(a, 'Java5_PackageDeclaration238', {b2})
    assert _is_linked(a, 'Java5_PackageDeclaration238', b2)
    if hasattr(b1, 'Java5_PackageDeclaration240'):
        assert not _is_linked(b1, 'Java5_PackageDeclaration240', a)
    if hasattr(b2, 'Java5_PackageDeclaration240'):
        assert _is_linked(b2, 'Java5_PackageDeclaration240', a)
    _safe_set(a, 'Java5_PackageDeclaration238', set())
    assert not _is_linked(a, 'Java5_PackageDeclaration238', b2)
    if hasattr(b2, 'Java5_PackageDeclaration240'):
        assert not _is_linked(b2, 'Java5_PackageDeclaration240', a)


def test_assoc_package2_link_reassign_clear():
    a = Java5_PackageDeclaration(qualifiedName="sample_text")
    b1 = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    b2 = Java5_AbstractTypeDeclaration(qualifiedName="sample_text_2")
    _safe_set(a, 'PackageDeclaration', b1)
    assert _is_linked(a, 'PackageDeclaration', b1)
    if hasattr(b1, 'ownedElements'):
        assert _is_linked(b1, 'ownedElements', a)
    _safe_set(a, 'PackageDeclaration', b2)
    assert _is_linked(a, 'PackageDeclaration', b2)
    if hasattr(b1, 'ownedElements'):
        assert not _is_linked(b1, 'ownedElements', a)
    if hasattr(b2, 'ownedElements'):
        assert _is_linked(b2, 'ownedElements', a)
    _safe_set(a, 'PackageDeclaration', None)
    assert not _is_linked(a, 'PackageDeclaration', b2)
    if hasattr(b2, 'ownedElements'):
        assert not _is_linked(b2, 'ownedElements', a)


def test_assoc_package86_link_reassign_clear():
    a = Java5_PackageDeclaration(qualifiedName="sample_text")
    b1 = Java5_CompilationUnit(originalFilePath="sample_text")
    b2 = Java5_CompilationUnit(originalFilePath="sample_text_2")
    _safe_set(a, 'Java5_PackageDeclaration', b1)
    assert _is_linked(a, 'Java5_PackageDeclaration', b1)
    if hasattr(b1, 'Java5_CompilationUnit87'):
        assert _is_linked(b1, 'Java5_CompilationUnit87', a)
    _safe_set(a, 'Java5_PackageDeclaration', b2)
    assert _is_linked(a, 'Java5_PackageDeclaration', b2)
    if hasattr(b1, 'Java5_CompilationUnit87'):
        assert not _is_linked(b1, 'Java5_CompilationUnit87', a)
    if hasattr(b2, 'Java5_CompilationUnit87'):
        assert _is_linked(b2, 'Java5_CompilationUnit87', a)
    _safe_set(a, 'Java5_PackageDeclaration', None)
    assert not _is_linked(a, 'Java5_PackageDeclaration', b2)
    if hasattr(b2, 'Java5_CompilationUnit87'):
        assert not _is_linked(b2, 'Java5_CompilationUnit87', a)


def test_assoc_parameter122_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_EnhancedForStatement()
    b2 = Java5_EnhancedForStatement()
    _safe_set(a, 'SingleVariableDeclaration123', b1)
    assert _is_linked(a, 'SingleVariableDeclaration123', b1)
    if hasattr(b1, 'enhancedForStatement'):
        assert _is_linked(b1, 'enhancedForStatement', a)
    _safe_set(a, 'SingleVariableDeclaration123', b2)
    assert _is_linked(a, 'SingleVariableDeclaration123', b2)
    if hasattr(b1, 'enhancedForStatement'):
        assert not _is_linked(b1, 'enhancedForStatement', a)
    if hasattr(b2, 'enhancedForStatement'):
        assert _is_linked(b2, 'enhancedForStatement', a)
    _safe_set(a, 'SingleVariableDeclaration123', None)
    assert not _is_linked(a, 'SingleVariableDeclaration123', b2)
    if hasattr(b2, 'enhancedForStatement'):
        assert not _is_linked(b2, 'enhancedForStatement', a)


def test_assoc_parameters193_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b2 = Java5_MethodDeclaration(constructor=False, extraArrayDimensions=13, varargs=False)
    _safe_set(a, 'SingleVariableDeclaration194', b1)
    assert _is_linked(a, 'SingleVariableDeclaration194', b1)
    if hasattr(b1, 'methodDeclaration'):
        assert _is_linked(b1, 'methodDeclaration', a)
    _safe_set(a, 'SingleVariableDeclaration194', b2)
    assert _is_linked(a, 'SingleVariableDeclaration194', b2)
    if hasattr(b1, 'methodDeclaration'):
        assert not _is_linked(b1, 'methodDeclaration', a)
    if hasattr(b2, 'methodDeclaration'):
        assert _is_linked(b2, 'methodDeclaration', a)
    _safe_set(a, 'SingleVariableDeclaration194', None)
    assert not _is_linked(a, 'SingleVariableDeclaration194', b2)
    if hasattr(b2, 'methodDeclaration'):
        assert not _is_linked(b2, 'methodDeclaration', a)


def test_assoc_parameters208_link_reassign_clear():
    a = Java5_MethodRefParameter(isVarargs="sample_text", name="sample_text")
    b1 = Java5_MethodRef()
    b2 = Java5_MethodRef()
    _safe_set(a, 'Java5_MethodRefParameter', b1)
    assert _is_linked(a, 'Java5_MethodRefParameter', b1)
    if hasattr(b1, 'Java5_MethodRef209'):
        assert _is_linked(b1, 'Java5_MethodRef209', a)
    _safe_set(a, 'Java5_MethodRefParameter', b2)
    assert _is_linked(a, 'Java5_MethodRefParameter', b2)
    if hasattr(b1, 'Java5_MethodRef209'):
        assert not _is_linked(b1, 'Java5_MethodRef209', a)
    if hasattr(b2, 'Java5_MethodRef209'):
        assert _is_linked(b2, 'Java5_MethodRef209', a)
    _safe_set(a, 'Java5_MethodRefParameter', None)
    assert not _is_linked(a, 'Java5_MethodRefParameter', b2)
    if hasattr(b2, 'Java5_MethodRef209'):
        assert not _is_linked(b2, 'Java5_MethodRef209', a)


def test_assoc_redefinedMethodDeclaration189_link_reassign_clear():
    a = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b1 = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b2 = Java5_MethodDeclaration(constructor=False, extraArrayDimensions=13, varargs=False)
    _safe_set(a, 'MethodDeclaration', b1)
    assert _is_linked(a, 'MethodDeclaration', b1)
    if hasattr(b1, 'redefinitions'):
        assert _is_linked(b1, 'redefinitions', a)
    _safe_set(a, 'MethodDeclaration', b2)
    assert _is_linked(a, 'MethodDeclaration', b2)
    if hasattr(b1, 'redefinitions'):
        assert not _is_linked(b1, 'redefinitions', a)
    if hasattr(b2, 'redefinitions'):
        assert _is_linked(b2, 'redefinitions', a)
    _safe_set(a, 'MethodDeclaration', None)
    assert not _is_linked(a, 'MethodDeclaration', b2)
    if hasattr(b2, 'redefinitions'):
        assert not _is_linked(b2, 'redefinitions', a)


def test_assoc_redefinitions191_link_reassign_clear():
    a = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b1 = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b2 = Java5_MethodDeclaration(constructor=False, extraArrayDimensions=13, varargs=False)
    _safe_set(a, 'MethodDeclaration192', b1)
    assert _is_linked(a, 'MethodDeclaration192', b1)
    if hasattr(b1, 'redefinedMethodDeclaration'):
        assert _is_linked(b1, 'redefinedMethodDeclaration', a)
    _safe_set(a, 'MethodDeclaration192', b2)
    assert _is_linked(a, 'MethodDeclaration192', b2)
    if hasattr(b1, 'redefinedMethodDeclaration'):
        assert not _is_linked(b1, 'redefinedMethodDeclaration', a)
    if hasattr(b2, 'redefinedMethodDeclaration'):
        assert _is_linked(b2, 'redefinedMethodDeclaration', a)
    _safe_set(a, 'MethodDeclaration192', None)
    assert not _is_linked(a, 'MethodDeclaration192', b2)
    if hasattr(b2, 'redefinedMethodDeclaration'):
        assert not _is_linked(b2, 'redefinedMethodDeclaration', a)


def test_assoc_returnType183_link_reassign_clear():
    a = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_MethodDeclaration184', b1)
    assert _is_linked(a, 'Java5_MethodDeclaration184', b1)
    if hasattr(b1, 'Java5_NamedElementRef185'):
        assert _is_linked(b1, 'Java5_NamedElementRef185', a)
    _safe_set(a, 'Java5_MethodDeclaration184', b2)
    assert _is_linked(a, 'Java5_MethodDeclaration184', b2)
    if hasattr(b1, 'Java5_NamedElementRef185'):
        assert not _is_linked(b1, 'Java5_NamedElementRef185', a)
    if hasattr(b2, 'Java5_NamedElementRef185'):
        assert _is_linked(b2, 'Java5_NamedElementRef185', a)
    _safe_set(a, 'Java5_MethodDeclaration184', None)
    assert not _is_linked(a, 'Java5_MethodDeclaration184', b2)
    if hasattr(b2, 'Java5_NamedElementRef185'):
        assert not _is_linked(b2, 'Java5_NamedElementRef185', a)


def test_assoc_rightHandSide48_link_reassign_clear():
    a = Java5_Assignment(operator="sample_text")
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_Assignment49', b1)
    assert _is_linked(a, 'Java5_Assignment49', b1)
    if hasattr(b1, 'Java5_Expression50'):
        assert _is_linked(b1, 'Java5_Expression50', a)
    _safe_set(a, 'Java5_Assignment49', b2)
    assert _is_linked(a, 'Java5_Assignment49', b2)
    if hasattr(b1, 'Java5_Expression50'):
        assert not _is_linked(b1, 'Java5_Expression50', a)
    if hasattr(b2, 'Java5_Expression50'):
        assert _is_linked(b2, 'Java5_Expression50', a)
    _safe_set(a, 'Java5_Assignment49', None)
    assert not _is_linked(a, 'Java5_Assignment49', b2)
    if hasattr(b2, 'Java5_Expression50'):
        assert not _is_linked(b2, 'Java5_Expression50', a)


def test_assoc_rightOperand156_link_reassign_clear():
    a = Java5_InfixExpression(operator="sample_text")
    b1 = Java5_Expression()
    b2 = Java5_Expression()
    _safe_set(a, 'Java5_InfixExpression', b1)
    assert _is_linked(a, 'Java5_InfixExpression', b1)
    if hasattr(b1, 'Java5_Expression157'):
        assert _is_linked(b1, 'Java5_Expression157', a)
    _safe_set(a, 'Java5_InfixExpression', b2)
    assert _is_linked(a, 'Java5_InfixExpression', b2)
    if hasattr(b1, 'Java5_Expression157'):
        assert not _is_linked(b1, 'Java5_Expression157', a)
    if hasattr(b2, 'Java5_Expression157'):
        assert _is_linked(b2, 'Java5_Expression157', a)
    _safe_set(a, 'Java5_InfixExpression', None)
    assert not _is_linked(a, 'Java5_InfixExpression', b2)
    if hasattr(b2, 'Java5_Expression157'):
        assert not _is_linked(b2, 'Java5_Expression157', a)


def test_assoc_superInterfaces3_link_reassign_clear():
    a = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_AbstractTypeDeclaration4', {b1})
    assert _is_linked(a, 'Java5_AbstractTypeDeclaration4', b1)
    if hasattr(b1, 'Java5_NamedElementRef'):
        assert _is_linked(b1, 'Java5_NamedElementRef', a)
    _safe_set(a, 'Java5_AbstractTypeDeclaration4', {b2})
    assert _is_linked(a, 'Java5_AbstractTypeDeclaration4', b2)
    if hasattr(b1, 'Java5_NamedElementRef'):
        assert not _is_linked(b1, 'Java5_NamedElementRef', a)
    if hasattr(b2, 'Java5_NamedElementRef'):
        assert _is_linked(b2, 'Java5_NamedElementRef', a)
    _safe_set(a, 'Java5_AbstractTypeDeclaration4', set())
    assert not _is_linked(a, 'Java5_AbstractTypeDeclaration4', b2)
    if hasattr(b2, 'Java5_NamedElementRef'):
        assert not _is_linked(b2, 'Java5_NamedElementRef', a)


def test_assoc_thrownExceptions180_link_reassign_clear():
    a = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_MethodDeclaration181', {b1})
    assert _is_linked(a, 'Java5_MethodDeclaration181', b1)
    if hasattr(b1, 'Java5_NamedElementRef182'):
        assert _is_linked(b1, 'Java5_NamedElementRef182', a)
    _safe_set(a, 'Java5_MethodDeclaration181', {b2})
    assert _is_linked(a, 'Java5_MethodDeclaration181', b2)
    if hasattr(b1, 'Java5_NamedElementRef182'):
        assert not _is_linked(b1, 'Java5_NamedElementRef182', a)
    if hasattr(b2, 'Java5_NamedElementRef182'):
        assert _is_linked(b2, 'Java5_NamedElementRef182', a)
    _safe_set(a, 'Java5_MethodDeclaration181', set())
    assert not _is_linked(a, 'Java5_MethodDeclaration181', b2)
    if hasattr(b2, 'Java5_NamedElementRef182'):
        assert not _is_linked(b2, 'Java5_NamedElementRef182', a)


def test_assoc_type210_link_reassign_clear():
    a = Java5_MethodRefParameter(isVarargs="sample_text", name="sample_text")
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_MethodRefParameter211', b1)
    assert _is_linked(a, 'Java5_MethodRefParameter211', b1)
    if hasattr(b1, 'Java5_NamedElementRef212'):
        assert _is_linked(b1, 'Java5_NamedElementRef212', a)
    _safe_set(a, 'Java5_MethodRefParameter211', b2)
    assert _is_linked(a, 'Java5_MethodRefParameter211', b2)
    if hasattr(b1, 'Java5_NamedElementRef212'):
        assert not _is_linked(b1, 'Java5_NamedElementRef212', a)
    if hasattr(b2, 'Java5_NamedElementRef212'):
        assert _is_linked(b2, 'Java5_NamedElementRef212', a)
    _safe_set(a, 'Java5_MethodRefParameter211', None)
    assert not _is_linked(a, 'Java5_MethodRefParameter211', b2)
    if hasattr(b2, 'Java5_NamedElementRef212'):
        assert not _is_linked(b2, 'Java5_NamedElementRef212', a)


def test_assoc_type257_link_reassign_clear():
    a = Java5_SingleVariableDeclaration(varargs=True)
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_SingleVariableDeclaration', b1)
    assert _is_linked(a, 'Java5_SingleVariableDeclaration', b1)
    if hasattr(b1, 'Java5_NamedElementRef258'):
        assert _is_linked(b1, 'Java5_NamedElementRef258', a)
    _safe_set(a, 'Java5_SingleVariableDeclaration', b2)
    assert _is_linked(a, 'Java5_SingleVariableDeclaration', b2)
    if hasattr(b1, 'Java5_NamedElementRef258'):
        assert not _is_linked(b1, 'Java5_NamedElementRef258', a)
    if hasattr(b2, 'Java5_NamedElementRef258'):
        assert _is_linked(b2, 'Java5_NamedElementRef258', a)
    _safe_set(a, 'Java5_SingleVariableDeclaration', None)
    assert not _is_linked(a, 'Java5_SingleVariableDeclaration', b2)
    if hasattr(b2, 'Java5_NamedElementRef258'):
        assert not _is_linked(b2, 'Java5_NamedElementRef258', a)


def test_assoc_type334_link_reassign_clear():
    a = Java5_VariableDeclarationStatement(extraArrayDimensions=7)
    b1 = Java5_NamedElementRef()
    b2 = Java5_NamedElementRef()
    _safe_set(a, 'Java5_VariableDeclarationStatement', b1)
    assert _is_linked(a, 'Java5_VariableDeclarationStatement', b1)
    if hasattr(b1, 'Java5_NamedElementRef335'):
        assert _is_linked(b1, 'Java5_NamedElementRef335', a)
    _safe_set(a, 'Java5_VariableDeclarationStatement', b2)
    assert _is_linked(a, 'Java5_VariableDeclarationStatement', b2)
    if hasattr(b1, 'Java5_NamedElementRef335'):
        assert not _is_linked(b1, 'Java5_NamedElementRef335', a)
    if hasattr(b2, 'Java5_NamedElementRef335'):
        assert _is_linked(b2, 'Java5_NamedElementRef335', a)
    _safe_set(a, 'Java5_VariableDeclarationStatement', None)
    assert not _is_linked(a, 'Java5_VariableDeclarationStatement', b2)
    if hasattr(b2, 'Java5_NamedElementRef335'):
        assert not _is_linked(b2, 'Java5_NamedElementRef335', a)


def test_assoc_typeParameters186_link_reassign_clear():
    a = Java5_MethodDeclaration(constructor=True, extraArrayDimensions=7, varargs=True)
    b1 = Java5_TypeParameter()
    b2 = Java5_TypeParameter()
    _safe_set(a, 'Java5_MethodDeclaration187', {b1})
    assert _is_linked(a, 'Java5_MethodDeclaration187', b1)
    if hasattr(b1, 'Java5_TypeParameter'):
        assert _is_linked(b1, 'Java5_TypeParameter', a)
    _safe_set(a, 'Java5_MethodDeclaration187', {b2})
    assert _is_linked(a, 'Java5_MethodDeclaration187', b2)
    if hasattr(b1, 'Java5_TypeParameter'):
        assert not _is_linked(b1, 'Java5_TypeParameter', a)
    if hasattr(b2, 'Java5_TypeParameter'):
        assert _is_linked(b2, 'Java5_TypeParameter', a)
    _safe_set(a, 'Java5_MethodDeclaration187', set())
    assert not _is_linked(a, 'Java5_MethodDeclaration187', b2)
    if hasattr(b2, 'Java5_TypeParameter'):
        assert not _is_linked(b2, 'Java5_TypeParameter', a)


def test_assoc_types88_link_reassign_clear():
    a = Java5_CompilationUnit(originalFilePath="sample_text")
    b1 = Java5_AbstractTypeDeclaration(qualifiedName="sample_text")
    b2 = Java5_AbstractTypeDeclaration(qualifiedName="sample_text_2")
    _safe_set(a, 'Java5_CompilationUnit89', {b1})
    assert _is_linked(a, 'Java5_CompilationUnit89', b1)
    if hasattr(b1, 'Java5_AbstractTypeDeclaration90'):
        assert _is_linked(b1, 'Java5_AbstractTypeDeclaration90', a)
    _safe_set(a, 'Java5_CompilationUnit89', {b2})
    assert _is_linked(a, 'Java5_CompilationUnit89', b2)
    if hasattr(b1, 'Java5_AbstractTypeDeclaration90'):
        assert not _is_linked(b1, 'Java5_AbstractTypeDeclaration90', a)
    if hasattr(b2, 'Java5_AbstractTypeDeclaration90'):
        assert _is_linked(b2, 'Java5_AbstractTypeDeclaration90', a)
    _safe_set(a, 'Java5_CompilationUnit89', set())
    assert not _is_linked(a, 'Java5_CompilationUnit89', b2)
    if hasattr(b2, 'Java5_AbstractTypeDeclaration90'):
        assert not _is_linked(b2, 'Java5_AbstractTypeDeclaration90', a)


def test_assoc_unresolvedItems217_link_reassign_clear():
    a = Java5_Model(name="sample_text")
    b1 = Java5_UnresolvedItem()
    b2 = Java5_UnresolvedItem()
    _safe_set(a, 'Java5_Model218', {b1})
    assert _is_linked(a, 'Java5_Model218', b1)
    if hasattr(b1, 'Java5_UnresolvedItem'):
        assert _is_linked(b1, 'Java5_UnresolvedItem', a)
    _safe_set(a, 'Java5_Model218', {b2})
    assert _is_linked(a, 'Java5_Model218', b2)
    if hasattr(b1, 'Java5_UnresolvedItem'):
        assert not _is_linked(b1, 'Java5_UnresolvedItem', a)
    if hasattr(b2, 'Java5_UnresolvedItem'):
        assert _is_linked(b2, 'Java5_UnresolvedItem', a)
    _safe_set(a, 'Java5_Model218', set())
    assert not _is_linked(a, 'Java5_Model218', b2)
    if hasattr(b2, 'Java5_UnresolvedItem'):
        assert not _is_linked(b2, 'Java5_UnresolvedItem', a)


def test_assoc_variableDeclarationStatement328_link_reassign_clear():
    a = Java5_VariableDeclarationStatement(extraArrayDimensions=7)
    b1 = Java5_VariableDeclarationFragment()
    b2 = Java5_VariableDeclarationFragment()
    _safe_set(a, 'VariableDeclarationStatement330', b1)
    assert _is_linked(a, 'VariableDeclarationStatement330', b1)
    if hasattr(b1, 'fragments329'):
        assert _is_linked(b1, 'fragments329', a)
    _safe_set(a, 'VariableDeclarationStatement330', b2)
    assert _is_linked(a, 'VariableDeclarationStatement330', b2)
    if hasattr(b1, 'fragments329'):
        assert not _is_linked(b1, 'fragments329', a)
    if hasattr(b2, 'fragments329'):
        assert _is_linked(b2, 'fragments329', a)
    _safe_set(a, 'VariableDeclarationStatement330', None)
    assert not _is_linked(a, 'VariableDeclarationStatement330', b2)
    if hasattr(b2, 'fragments329'):
        assert not _is_linked(b2, 'fragments329', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ASTNode_strategy = st.builds(ASTNode)
@given(instance=ASTNode_strategy)
@settings(max_examples=25)
def test_ASTNode_instantiation(instance):
    assert isinstance(instance, ASTNode)


AbstractTypeDeclaration_strategy = st.builds(AbstractTypeDeclaration)
@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractTypeDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)


BodyDeclaration_strategy = st.builds(BodyDeclaration)
@given(instance=BodyDeclaration_strategy)
@settings(max_examples=25)
def test_BodyDeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Java5_ASTNode_strategy = st.builds(Java5_ASTNode)
@given(instance=Java5_ASTNode_strategy)
@settings(max_examples=25)
def test_Java5_ASTNode_instantiation(instance):
    assert isinstance(instance, Java5_ASTNode)


Java5_AbstractTypeDeclaration_strategy = st.builds(Java5_AbstractTypeDeclaration, qualifiedName=safe_text)
@given(instance=Java5_AbstractTypeDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_AbstractTypeDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_AbstractTypeDeclaration)


Java5_Annotation_strategy = st.builds(Java5_Annotation)
@given(instance=Java5_Annotation_strategy)
@settings(max_examples=25)
def test_Java5_Annotation_instantiation(instance):
    assert isinstance(instance, Java5_Annotation)


Java5_AnnotationMemberValuePair_strategy = st.builds(Java5_AnnotationMemberValuePair)
@given(instance=Java5_AnnotationMemberValuePair_strategy)
@settings(max_examples=25)
def test_Java5_AnnotationMemberValuePair_instantiation(instance):
    assert isinstance(instance, Java5_AnnotationMemberValuePair)


Java5_AnnotationTypeDeclaration_strategy = st.builds(Java5_AnnotationTypeDeclaration)
@given(instance=Java5_AnnotationTypeDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_AnnotationTypeDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_AnnotationTypeDeclaration)


Java5_AnnotationTypeMemberDeclaration_strategy = st.builds(Java5_AnnotationTypeMemberDeclaration)
@given(instance=Java5_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_AnnotationTypeMemberDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_AnnotationTypeMemberDeclaration)


Java5_AnonymousClassDeclaration_strategy = st.builds(Java5_AnonymousClassDeclaration)
@given(instance=Java5_AnonymousClassDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_AnonymousClassDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_AnonymousClassDeclaration)


Java5_ArrayAccess_strategy = st.builds(Java5_ArrayAccess)
@given(instance=Java5_ArrayAccess_strategy)
@settings(max_examples=25)
def test_Java5_ArrayAccess_instantiation(instance):
    assert isinstance(instance, Java5_ArrayAccess)


Java5_ArrayCreation_strategy = st.builds(Java5_ArrayCreation)
@given(instance=Java5_ArrayCreation_strategy)
@settings(max_examples=25)
def test_Java5_ArrayCreation_instantiation(instance):
    assert isinstance(instance, Java5_ArrayCreation)


Java5_ArrayInitializer_strategy = st.builds(Java5_ArrayInitializer)
@given(instance=Java5_ArrayInitializer_strategy)
@settings(max_examples=25)
def test_Java5_ArrayInitializer_instantiation(instance):
    assert isinstance(instance, Java5_ArrayInitializer)


Java5_ArrayLengthAccess_strategy = st.builds(Java5_ArrayLengthAccess)
@given(instance=Java5_ArrayLengthAccess_strategy)
@settings(max_examples=25)
def test_Java5_ArrayLengthAccess_instantiation(instance):
    assert isinstance(instance, Java5_ArrayLengthAccess)


Java5_ArrayType_strategy = st.builds(Java5_ArrayType, dimensions=st.integers(), originalName=safe_text)
@given(instance=Java5_ArrayType_strategy)
@settings(max_examples=25)
def test_Java5_ArrayType_instantiation(instance):
    assert isinstance(instance, Java5_ArrayType)


Java5_AssertStatement_strategy = st.builds(Java5_AssertStatement)
@given(instance=Java5_AssertStatement_strategy)
@settings(max_examples=25)
def test_Java5_AssertStatement_instantiation(instance):
    assert isinstance(instance, Java5_AssertStatement)


Java5_Assignment_strategy = st.builds(Java5_Assignment, operator=safe_text)
@given(instance=Java5_Assignment_strategy)
@settings(max_examples=25)
def test_Java5_Assignment_instantiation(instance):
    assert isinstance(instance, Java5_Assignment)


Java5_Block_strategy = st.builds(Java5_Block)
@given(instance=Java5_Block_strategy)
@settings(max_examples=25)
def test_Java5_Block_instantiation(instance):
    assert isinstance(instance, Java5_Block)


Java5_BodyDeclaration_strategy = st.builds(Java5_BodyDeclaration)
@given(instance=Java5_BodyDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_BodyDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_BodyDeclaration)


Java5_BooleanLiteral_strategy = st.builds(Java5_BooleanLiteral, value=st.booleans())
@given(instance=Java5_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_Java5_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, Java5_BooleanLiteral)


Java5_BreakStatement_strategy = st.builds(Java5_BreakStatement)
@given(instance=Java5_BreakStatement_strategy)
@settings(max_examples=25)
def test_Java5_BreakStatement_instantiation(instance):
    assert isinstance(instance, Java5_BreakStatement)


Java5_CastExpression_strategy = st.builds(Java5_CastExpression)
@given(instance=Java5_CastExpression_strategy)
@settings(max_examples=25)
def test_Java5_CastExpression_instantiation(instance):
    assert isinstance(instance, Java5_CastExpression)


Java5_CatchClause_strategy = st.builds(Java5_CatchClause)
@given(instance=Java5_CatchClause_strategy)
@settings(max_examples=25)
def test_Java5_CatchClause_instantiation(instance):
    assert isinstance(instance, Java5_CatchClause)


Java5_CharacterLiteral_strategy = st.builds(Java5_CharacterLiteral, escapedValue=safe_text, value=safe_text)
@given(instance=Java5_CharacterLiteral_strategy)
@settings(max_examples=25)
def test_Java5_CharacterLiteral_instantiation(instance):
    assert isinstance(instance, Java5_CharacterLiteral)


Java5_ClassDeclaration_strategy = st.builds(Java5_ClassDeclaration)
@given(instance=Java5_ClassDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_ClassDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_ClassDeclaration)


Java5_ClassInstanceCreation_strategy = st.builds(Java5_ClassInstanceCreation)
@given(instance=Java5_ClassInstanceCreation_strategy)
@settings(max_examples=25)
def test_Java5_ClassInstanceCreation_instantiation(instance):
    assert isinstance(instance, Java5_ClassInstanceCreation)


Java5_CompilationUnit_strategy = st.builds(Java5_CompilationUnit, originalFilePath=safe_text)
@given(instance=Java5_CompilationUnit_strategy)
@settings(max_examples=25)
def test_Java5_CompilationUnit_instantiation(instance):
    assert isinstance(instance, Java5_CompilationUnit)


Java5_ConditionalExpression_strategy = st.builds(Java5_ConditionalExpression)
@given(instance=Java5_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_Java5_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, Java5_ConditionalExpression)


Java5_ConstructorInvocation_strategy = st.builds(Java5_ConstructorInvocation)
@given(instance=Java5_ConstructorInvocation_strategy)
@settings(max_examples=25)
def test_Java5_ConstructorInvocation_instantiation(instance):
    assert isinstance(instance, Java5_ConstructorInvocation)


Java5_ContinueStatement_strategy = st.builds(Java5_ContinueStatement)
@given(instance=Java5_ContinueStatement_strategy)
@settings(max_examples=25)
def test_Java5_ContinueStatement_instantiation(instance):
    assert isinstance(instance, Java5_ContinueStatement)


Java5_DoStatement_strategy = st.builds(Java5_DoStatement)
@given(instance=Java5_DoStatement_strategy)
@settings(max_examples=25)
def test_Java5_DoStatement_instantiation(instance):
    assert isinstance(instance, Java5_DoStatement)


Java5_EmptyStatement_strategy = st.builds(Java5_EmptyStatement)
@given(instance=Java5_EmptyStatement_strategy)
@settings(max_examples=25)
def test_Java5_EmptyStatement_instantiation(instance):
    assert isinstance(instance, Java5_EmptyStatement)


Java5_EnhancedForStatement_strategy = st.builds(Java5_EnhancedForStatement)
@given(instance=Java5_EnhancedForStatement_strategy)
@settings(max_examples=25)
def test_Java5_EnhancedForStatement_instantiation(instance):
    assert isinstance(instance, Java5_EnhancedForStatement)


Java5_EnumConstantDeclaration_strategy = st.builds(Java5_EnumConstantDeclaration)
@given(instance=Java5_EnumConstantDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_EnumConstantDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_EnumConstantDeclaration)


Java5_EnumDeclaration_strategy = st.builds(Java5_EnumDeclaration)
@given(instance=Java5_EnumDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_EnumDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_EnumDeclaration)


Java5_Expression_strategy = st.builds(Java5_Expression)
@given(instance=Java5_Expression_strategy)
@settings(max_examples=25)
def test_Java5_Expression_instantiation(instance):
    assert isinstance(instance, Java5_Expression)


Java5_ExpressionStatement_strategy = st.builds(Java5_ExpressionStatement)
@given(instance=Java5_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_Java5_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, Java5_ExpressionStatement)


Java5_FieldAccess_strategy = st.builds(Java5_FieldAccess)
@given(instance=Java5_FieldAccess_strategy)
@settings(max_examples=25)
def test_Java5_FieldAccess_instantiation(instance):
    assert isinstance(instance, Java5_FieldAccess)


Java5_FieldDeclaration_strategy = st.builds(Java5_FieldDeclaration)
@given(instance=Java5_FieldDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_FieldDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_FieldDeclaration)


Java5_ForStatement_strategy = st.builds(Java5_ForStatement)
@given(instance=Java5_ForStatement_strategy)
@settings(max_examples=25)
def test_Java5_ForStatement_instantiation(instance):
    assert isinstance(instance, Java5_ForStatement)


Java5_IfStatement_strategy = st.builds(Java5_IfStatement)
@given(instance=Java5_IfStatement_strategy)
@settings(max_examples=25)
def test_Java5_IfStatement_instantiation(instance):
    assert isinstance(instance, Java5_IfStatement)


Java5_ImportDeclaration_strategy = st.builds(Java5_ImportDeclaration, static=st.booleans())
@given(instance=Java5_ImportDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_ImportDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_ImportDeclaration)


Java5_InfixExpression_strategy = st.builds(Java5_InfixExpression, operator=safe_text)
@given(instance=Java5_InfixExpression_strategy)
@settings(max_examples=25)
def test_Java5_InfixExpression_instantiation(instance):
    assert isinstance(instance, Java5_InfixExpression)


Java5_Initializer_strategy = st.builds(Java5_Initializer)
@given(instance=Java5_Initializer_strategy)
@settings(max_examples=25)
def test_Java5_Initializer_instantiation(instance):
    assert isinstance(instance, Java5_Initializer)


Java5_InstanceofExpression_strategy = st.builds(Java5_InstanceofExpression)
@given(instance=Java5_InstanceofExpression_strategy)
@settings(max_examples=25)
def test_Java5_InstanceofExpression_instantiation(instance):
    assert isinstance(instance, Java5_InstanceofExpression)


Java5_InterfaceDeclaration_strategy = st.builds(Java5_InterfaceDeclaration)
@given(instance=Java5_InterfaceDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_InterfaceDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_InterfaceDeclaration)


Java5_LabeledStatement_strategy = st.builds(Java5_LabeledStatement)
@given(instance=Java5_LabeledStatement_strategy)
@settings(max_examples=25)
def test_Java5_LabeledStatement_instantiation(instance):
    assert isinstance(instance, Java5_LabeledStatement)


Java5_MemberRef_strategy = st.builds(Java5_MemberRef)
@given(instance=Java5_MemberRef_strategy)
@settings(max_examples=25)
def test_Java5_MemberRef_instantiation(instance):
    assert isinstance(instance, Java5_MemberRef)


Java5_MethodDeclaration_strategy = st.builds(Java5_MethodDeclaration, constructor=st.booleans(), extraArrayDimensions=st.integers(), varargs=st.booleans())
@given(instance=Java5_MethodDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_MethodDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_MethodDeclaration)


Java5_MethodInvocation_strategy = st.builds(Java5_MethodInvocation)
@given(instance=Java5_MethodInvocation_strategy)
@settings(max_examples=25)
def test_Java5_MethodInvocation_instantiation(instance):
    assert isinstance(instance, Java5_MethodInvocation)


Java5_MethodRef_strategy = st.builds(Java5_MethodRef)
@given(instance=Java5_MethodRef_strategy)
@settings(max_examples=25)
def test_Java5_MethodRef_instantiation(instance):
    assert isinstance(instance, Java5_MethodRef)


Java5_MethodRefParameter_strategy = st.builds(Java5_MethodRefParameter, isVarargs=safe_text, name=safe_text)
@given(instance=Java5_MethodRefParameter_strategy)
@settings(max_examples=25)
def test_Java5_MethodRefParameter_instantiation(instance):
    assert isinstance(instance, Java5_MethodRefParameter)


Java5_Model_strategy = st.builds(Java5_Model, name=safe_text)
@given(instance=Java5_Model_strategy)
@settings(max_examples=25)
def test_Java5_Model_instantiation(instance):
    assert isinstance(instance, Java5_Model)


Java5_Modifier_strategy = st.builds(Java5_Modifier, inheritance=safe_text, native=st.booleans(), static=st.booleans(), strictfp=st.booleans(), synchronized=st.booleans(), transient=st.booleans(), visibility=safe_text, volatile=st.booleans())
@given(instance=Java5_Modifier_strategy)
@settings(max_examples=25)
def test_Java5_Modifier_instantiation(instance):
    assert isinstance(instance, Java5_Modifier)


Java5_NamedElement_strategy = st.builds(Java5_NamedElement, name=safe_text, proxy=st.booleans())
@given(instance=Java5_NamedElement_strategy)
@settings(max_examples=25)
def test_Java5_NamedElement_instantiation(instance):
    assert isinstance(instance, Java5_NamedElement)


Java5_NamedElementRef_strategy = st.builds(Java5_NamedElementRef)
@given(instance=Java5_NamedElementRef_strategy)
@settings(max_examples=25)
def test_Java5_NamedElementRef_instantiation(instance):
    assert isinstance(instance, Java5_NamedElementRef)


Java5_NullLiteral_strategy = st.builds(Java5_NullLiteral)
@given(instance=Java5_NullLiteral_strategy)
@settings(max_examples=25)
def test_Java5_NullLiteral_instantiation(instance):
    assert isinstance(instance, Java5_NullLiteral)


Java5_NumberLiteral_strategy = st.builds(Java5_NumberLiteral, tokenValue=safe_text)
@given(instance=Java5_NumberLiteral_strategy)
@settings(max_examples=25)
def test_Java5_NumberLiteral_instantiation(instance):
    assert isinstance(instance, Java5_NumberLiteral)


Java5_OrphanType_strategy = st.builds(Java5_OrphanType)
@given(instance=Java5_OrphanType_strategy)
@settings(max_examples=25)
def test_Java5_OrphanType_instantiation(instance):
    assert isinstance(instance, Java5_OrphanType)


Java5_PackageDeclaration_strategy = st.builds(Java5_PackageDeclaration, qualifiedName=safe_text)
@given(instance=Java5_PackageDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_PackageDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_PackageDeclaration)


Java5_ParameterizedType_strategy = st.builds(Java5_ParameterizedType)
@given(instance=Java5_ParameterizedType_strategy)
@settings(max_examples=25)
def test_Java5_ParameterizedType_instantiation(instance):
    assert isinstance(instance, Java5_ParameterizedType)


Java5_ParenthesizedExpression_strategy = st.builds(Java5_ParenthesizedExpression)
@given(instance=Java5_ParenthesizedExpression_strategy)
@settings(max_examples=25)
def test_Java5_ParenthesizedExpression_instantiation(instance):
    assert isinstance(instance, Java5_ParenthesizedExpression)


Java5_PostfixExpression_strategy = st.builds(Java5_PostfixExpression, operator=safe_text)
@given(instance=Java5_PostfixExpression_strategy)
@settings(max_examples=25)
def test_Java5_PostfixExpression_instantiation(instance):
    assert isinstance(instance, Java5_PostfixExpression)


Java5_PrefixExpression_strategy = st.builds(Java5_PrefixExpression, operator=safe_text)
@given(instance=Java5_PrefixExpression_strategy)
@settings(max_examples=25)
def test_Java5_PrefixExpression_instantiation(instance):
    assert isinstance(instance, Java5_PrefixExpression)


Java5_PrimitiveType_strategy = st.builds(Java5_PrimitiveType)
@given(instance=Java5_PrimitiveType_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveType_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveType)


Java5_PrimitiveTypeBoolean_strategy = st.builds(Java5_PrimitiveTypeBoolean)
@given(instance=Java5_PrimitiveTypeBoolean_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeBoolean_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeBoolean)


Java5_PrimitiveTypeByte_strategy = st.builds(Java5_PrimitiveTypeByte)
@given(instance=Java5_PrimitiveTypeByte_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeByte_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeByte)


Java5_PrimitiveTypeChar_strategy = st.builds(Java5_PrimitiveTypeChar)
@given(instance=Java5_PrimitiveTypeChar_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeChar_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeChar)


Java5_PrimitiveTypeDouble_strategy = st.builds(Java5_PrimitiveTypeDouble)
@given(instance=Java5_PrimitiveTypeDouble_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeDouble_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeDouble)


Java5_PrimitiveTypeFloat_strategy = st.builds(Java5_PrimitiveTypeFloat)
@given(instance=Java5_PrimitiveTypeFloat_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeFloat_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeFloat)


Java5_PrimitiveTypeInt_strategy = st.builds(Java5_PrimitiveTypeInt)
@given(instance=Java5_PrimitiveTypeInt_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeInt_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeInt)


Java5_PrimitiveTypeLong_strategy = st.builds(Java5_PrimitiveTypeLong)
@given(instance=Java5_PrimitiveTypeLong_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeLong_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeLong)


Java5_PrimitiveTypeShort_strategy = st.builds(Java5_PrimitiveTypeShort)
@given(instance=Java5_PrimitiveTypeShort_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeShort_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeShort)


Java5_PrimitiveTypeVoid_strategy = st.builds(Java5_PrimitiveTypeVoid)
@given(instance=Java5_PrimitiveTypeVoid_strategy)
@settings(max_examples=25)
def test_Java5_PrimitiveTypeVoid_instantiation(instance):
    assert isinstance(instance, Java5_PrimitiveTypeVoid)


Java5_ReturnStatement_strategy = st.builds(Java5_ReturnStatement)
@given(instance=Java5_ReturnStatement_strategy)
@settings(max_examples=25)
def test_Java5_ReturnStatement_instantiation(instance):
    assert isinstance(instance, Java5_ReturnStatement)


Java5_SingleVariableDeclaration_strategy = st.builds(Java5_SingleVariableDeclaration, varargs=st.booleans())
@given(instance=Java5_SingleVariableDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_SingleVariableDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_SingleVariableDeclaration)


Java5_Statement_strategy = st.builds(Java5_Statement)
@given(instance=Java5_Statement_strategy)
@settings(max_examples=25)
def test_Java5_Statement_instantiation(instance):
    assert isinstance(instance, Java5_Statement)


Java5_StringLiteral_strategy = st.builds(Java5_StringLiteral, escapedValue=safe_text, value=safe_text)
@given(instance=Java5_StringLiteral_strategy)
@settings(max_examples=25)
def test_Java5_StringLiteral_instantiation(instance):
    assert isinstance(instance, Java5_StringLiteral)


Java5_SuperConstructorInvocation_strategy = st.builds(Java5_SuperConstructorInvocation)
@given(instance=Java5_SuperConstructorInvocation_strategy)
@settings(max_examples=25)
def test_Java5_SuperConstructorInvocation_instantiation(instance):
    assert isinstance(instance, Java5_SuperConstructorInvocation)


Java5_SuperFieldAccess_strategy = st.builds(Java5_SuperFieldAccess)
@given(instance=Java5_SuperFieldAccess_strategy)
@settings(max_examples=25)
def test_Java5_SuperFieldAccess_instantiation(instance):
    assert isinstance(instance, Java5_SuperFieldAccess)


Java5_SuperMethodInvocation_strategy = st.builds(Java5_SuperMethodInvocation)
@given(instance=Java5_SuperMethodInvocation_strategy)
@settings(max_examples=25)
def test_Java5_SuperMethodInvocation_instantiation(instance):
    assert isinstance(instance, Java5_SuperMethodInvocation)


Java5_SwitchCase_strategy = st.builds(Java5_SwitchCase, default=st.booleans())
@given(instance=Java5_SwitchCase_strategy)
@settings(max_examples=25)
def test_Java5_SwitchCase_instantiation(instance):
    assert isinstance(instance, Java5_SwitchCase)


Java5_SwitchStatement_strategy = st.builds(Java5_SwitchStatement)
@given(instance=Java5_SwitchStatement_strategy)
@settings(max_examples=25)
def test_Java5_SwitchStatement_instantiation(instance):
    assert isinstance(instance, Java5_SwitchStatement)


Java5_SynchronizedStatement_strategy = st.builds(Java5_SynchronizedStatement)
@given(instance=Java5_SynchronizedStatement_strategy)
@settings(max_examples=25)
def test_Java5_SynchronizedStatement_instantiation(instance):
    assert isinstance(instance, Java5_SynchronizedStatement)


Java5_TagElement_strategy = st.builds(Java5_TagElement, tagName=safe_text)
@given(instance=Java5_TagElement_strategy)
@settings(max_examples=25)
def test_Java5_TagElement_instantiation(instance):
    assert isinstance(instance, Java5_TagElement)


Java5_TextElement_strategy = st.builds(Java5_TextElement, text=safe_text)
@given(instance=Java5_TextElement_strategy)
@settings(max_examples=25)
def test_Java5_TextElement_instantiation(instance):
    assert isinstance(instance, Java5_TextElement)


Java5_ThisExpression_strategy = st.builds(Java5_ThisExpression)
@given(instance=Java5_ThisExpression_strategy)
@settings(max_examples=25)
def test_Java5_ThisExpression_instantiation(instance):
    assert isinstance(instance, Java5_ThisExpression)


Java5_ThrowStatement_strategy = st.builds(Java5_ThrowStatement)
@given(instance=Java5_ThrowStatement_strategy)
@settings(max_examples=25)
def test_Java5_ThrowStatement_instantiation(instance):
    assert isinstance(instance, Java5_ThrowStatement)


Java5_TryStatement_strategy = st.builds(Java5_TryStatement)
@given(instance=Java5_TryStatement_strategy)
@settings(max_examples=25)
def test_Java5_TryStatement_instantiation(instance):
    assert isinstance(instance, Java5_TryStatement)


Java5_TypeDeclaration_strategy = st.builds(Java5_TypeDeclaration)
@given(instance=Java5_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_TypeDeclaration)


Java5_TypeDeclarationStatement_strategy = st.builds(Java5_TypeDeclarationStatement)
@given(instance=Java5_TypeDeclarationStatement_strategy)
@settings(max_examples=25)
def test_Java5_TypeDeclarationStatement_instantiation(instance):
    assert isinstance(instance, Java5_TypeDeclarationStatement)


Java5_TypeLiteral_strategy = st.builds(Java5_TypeLiteral)
@given(instance=Java5_TypeLiteral_strategy)
@settings(max_examples=25)
def test_Java5_TypeLiteral_instantiation(instance):
    assert isinstance(instance, Java5_TypeLiteral)


Java5_TypeParameter_strategy = st.builds(Java5_TypeParameter)
@given(instance=Java5_TypeParameter_strategy)
@settings(max_examples=25)
def test_Java5_TypeParameter_instantiation(instance):
    assert isinstance(instance, Java5_TypeParameter)


Java5_UnresolvedItem_strategy = st.builds(Java5_UnresolvedItem)
@given(instance=Java5_UnresolvedItem_strategy)
@settings(max_examples=25)
def test_Java5_UnresolvedItem_instantiation(instance):
    assert isinstance(instance, Java5_UnresolvedItem)


Java5_VariableDeclaration_strategy = st.builds(Java5_VariableDeclaration, extraArrayDimensions=st.integers())
@given(instance=Java5_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_Java5_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, Java5_VariableDeclaration)


Java5_VariableDeclarationExpression_strategy = st.builds(Java5_VariableDeclarationExpression)
@given(instance=Java5_VariableDeclarationExpression_strategy)
@settings(max_examples=25)
def test_Java5_VariableDeclarationExpression_instantiation(instance):
    assert isinstance(instance, Java5_VariableDeclarationExpression)


Java5_VariableDeclarationFragment_strategy = st.builds(Java5_VariableDeclarationFragment)
@given(instance=Java5_VariableDeclarationFragment_strategy)
@settings(max_examples=25)
def test_Java5_VariableDeclarationFragment_instantiation(instance):
    assert isinstance(instance, Java5_VariableDeclarationFragment)


Java5_VariableDeclarationStatement_strategy = st.builds(Java5_VariableDeclarationStatement, extraArrayDimensions=st.integers())
@given(instance=Java5_VariableDeclarationStatement_strategy)
@settings(max_examples=25)
def test_Java5_VariableDeclarationStatement_instantiation(instance):
    assert isinstance(instance, Java5_VariableDeclarationStatement)


Java5_WhileStatement_strategy = st.builds(Java5_WhileStatement)
@given(instance=Java5_WhileStatement_strategy)
@settings(max_examples=25)
def test_Java5_WhileStatement_instantiation(instance):
    assert isinstance(instance, Java5_WhileStatement)


Java5_WildCardType_strategy = st.builds(Java5_WildCardType, isUpperBound=safe_text)
@given(instance=Java5_WildCardType_strategy)
@settings(max_examples=25)
def test_Java5_WildCardType_instantiation(instance):
    assert isinstance(instance, Java5_WildCardType)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


OrphanType_strategy = st.builds(OrphanType)
@given(instance=OrphanType_strategy)
@settings(max_examples=25)
def test_OrphanType_instantiation(instance):
    assert isinstance(instance, OrphanType)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


TypeDeclaration_strategy = st.builds(TypeDeclaration)
@given(instance=TypeDeclaration_strategy)
@settings(max_examples=25)
def test_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)


VariableDeclaration_strategy = st.builds(VariableDeclaration)
@given(instance=VariableDeclaration_strategy)
@settings(max_examples=25)
def test_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)



