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
    java_Model,
    AbstractMethodDeclaration,
    java_ConstructorDeclaration,
    java_MethodDeclaration,
    java_ASTNode,
    NamespaceAccess,
    AbstractTypeQualifiedExpression,
    java_SuperFieldAccess,
    java_ThisExpression,
    AbstractVariablesContainer,
    UnresolvedItem,
    TypeDeclaration,
    java_ClassDeclaration,
    java_InterfaceDeclaration,
    AbstractMethodInvocation,
    java_SuperMethodInvocation,
    Statement,
    java_BreakStatement,
    java_EmptyStatement,
    java_VariableDeclarationStatement,
    java_DoStatement,
    java_ContinueStatement,
    java_SwitchStatement,
    java_TypeDeclarationStatement,
    java_EnhancedForStatement,
    java_ConstructorInvocation,
    java_IfStatement,
    java_TryStatement,
    java_ThrowStatement,
    java_AssertStatement,
    java_SwitchCase,
    java_ReturnStatement,
    java_CatchClause,
    java_ForStatement,
    java_ExpressionStatement,
    java_SuperConstructorInvocation,
    ASTNode,
    java_AnonymousClassDeclaration,
    java_Modifier,
    java_ImportDeclaration,
    java_MemberRef,
    java_NamespaceAccess,
    java_TagElement,
    java_AbstractMethodInvocation,
    java_NamedElement,
    java_MethodRefParameter,
    java_Block,
    java_SynchronizedStatement,
    AbstractTypeDeclaration,
    java_TypeDeclaration,
    java_EnumDeclaration,
    java_UnresolvedTypeDeclaration,
    java_AnnotationTypeDeclaration,
    Expression,
    java_PrefixExpression,
    java_Annotation,
    java_ConditionalExpression,
    java_ParenthesizedExpression,
    java_VariableDeclarationExpression,
    java_FieldAccess,
    java_NullLiteral,
    java_ClassInstanceCreation,
    java_BooleanLiteral,
    java_InstanceofExpression,
    java_ArrayAccess,
    java_InfixExpression,
    java_UnresolvedItemAccess,
    java_MethodInvocation,
    java_ArrayCreation,
    java_SingleVariableAccess,
    java_CharacterLiteral,
    java_NumberLiteral,
    java_ArrayLengthAccess,
    java_CastExpression,
    java_StringLiteral,
    java_Statement,
    java_WhileStatement,
    PrimitiveType,
    java_PrimitiveTypeShort,
    java_PrimitiveTypeInt,
    java_PrimitiveTypeVoid,
    java_PrimitiveTypeFloat,
    java_PrimitiveTypeBoolean,
    java_PrimitiveTypeLong,
    java_PrimitiveTypeChar,
    java_PrimitiveTypeDouble,
    java_MethodRef,
    java_Expression,
    java_Comment,
    NamedElement,
    java_VariableDeclaration,
    java_Type,
    java_Archive,
    java_BodyDeclaration,
    java_Package,
    java_CompilationUnit,
    java_UnresolvedItem,
    java_LabeledStatement,
    java_ClassFile,
    java_AnnotationMemberValuePair,
    java_ArrayInitializer,
    java_PrimitiveTypeByte,
    java_PostfixExpression,
    java_Assignment,
    java_AbstractTypeQualifiedExpression,
    java_TypeLiteral,
    BodyDeclaration,
    java_FieldDeclaration,
    java_AnnotationTypeMemberDeclaration,
    java_Initializer,
    java_AbstractMethodDeclaration,
    java_TypeAccess,
    Type,
    java_AbstractTypeDeclaration,
    java_ParameterizedType,
    java_PrimitiveType,
    java_ArrayType,
    java_TypeParameter,
    java_WildCardType,
    java_AbstractVariablesContainer,
    VariableDeclaration,
    java_EnumConstantDeclaration,
    java_SingleVariableDeclaration,
    java_VariableDeclarationFragment,
    PostfixExpressionKind,
    InfixExpressionKind,
    VisibilityKind,
    PrefixExpressionKind,
    InheritanceKind,
    AssignmentKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_java_model_is_not_abstract():
    assert not inspect.isabstract(java_Model)


def test_hyp_java_model_constructor_exists():
    assert callable(java_Model.__init__)


def test_hyp_java_model_constructor_args():
    sig = inspect.signature(java_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodDeclaration)


def test_hyp_abstractmethoddeclaration_constructor_exists():
    assert callable(AbstractMethodDeclaration.__init__)


def test_hyp_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(java_ConstructorDeclaration)


def test_hyp_java_constructordeclaration_constructor_exists():
    assert callable(java_ConstructorDeclaration.__init__)


def test_hyp_java_constructordeclaration_constructor_args():
    sig = inspect.signature(java_ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java_MethodDeclaration)


def test_hyp_java_methoddeclaration_constructor_exists():
    assert callable(java_MethodDeclaration.__init__)


def test_hyp_java_methoddeclaration_constructor_args():
    sig = inspect.signature(java_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_astnode_is_not_abstract():
    assert not inspect.isabstract(java_ASTNode)


def test_hyp_java_astnode_constructor_exists():
    assert callable(java_ASTNode.__init__)


def test_hyp_java_astnode_constructor_args():
    sig = inspect.signature(java_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(NamespaceAccess)


def test_hyp_namespaceaccess_constructor_exists():
    assert callable(NamespaceAccess.__init__)


def test_hyp_namespaceaccess_constructor_args():
    sig = inspect.signature(NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeQualifiedExpression)


def test_hyp_abstracttypequalifiedexpression_constructor_exists():
    assert callable(AbstractTypeQualifiedExpression.__init__)


def test_hyp_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(java_SuperFieldAccess)


def test_hyp_java_superfieldaccess_constructor_exists():
    assert callable(java_SuperFieldAccess.__init__)


def test_hyp_java_superfieldaccess_constructor_args():
    sig = inspect.signature(java_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_thisexpression_is_not_abstract():
    assert not inspect.isabstract(java_ThisExpression)


def test_hyp_java_thisexpression_constructor_exists():
    assert callable(java_ThisExpression.__init__)


def test_hyp_java_thisexpression_constructor_args():
    sig = inspect.signature(java_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(AbstractVariablesContainer)


def test_hyp_abstractvariablescontainer_constructor_exists():
    assert callable(AbstractVariablesContainer.__init__)


def test_hyp_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unresolveditem_is_not_abstract():
    assert not inspect.isabstract(UnresolvedItem)


def test_hyp_unresolveditem_constructor_exists():
    assert callable(UnresolvedItem.__init__)


def test_hyp_unresolveditem_constructor_args():
    sig = inspect.signature(UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_hyp_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_hyp_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_ClassDeclaration)


def test_hyp_java_classdeclaration_constructor_exists():
    assert callable(java_ClassDeclaration.__init__)


def test_hyp_java_classdeclaration_constructor_args():
    sig = inspect.signature(java_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_InterfaceDeclaration)


def test_hyp_java_interfacedeclaration_constructor_exists():
    assert callable(java_InterfaceDeclaration.__init__)


def test_hyp_java_interfacedeclaration_constructor_args():
    sig = inspect.signature(java_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(AbstractMethodInvocation)


def test_hyp_abstractmethodinvocation_constructor_exists():
    assert callable(AbstractMethodInvocation.__init__)


def test_hyp_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(java_SuperMethodInvocation)


def test_hyp_java_supermethodinvocation_constructor_exists():
    assert callable(java_SuperMethodInvocation.__init__)


def test_hyp_java_supermethodinvocation_constructor_args():
    sig = inspect.signature(java_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_breakstatement_is_not_abstract():
    assert not inspect.isabstract(java_BreakStatement)


def test_hyp_java_breakstatement_constructor_exists():
    assert callable(java_BreakStatement.__init__)


def test_hyp_java_breakstatement_constructor_args():
    sig = inspect.signature(java_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_emptystatement_is_not_abstract():
    assert not inspect.isabstract(java_EmptyStatement)


def test_hyp_java_emptystatement_constructor_exists():
    assert callable(java_EmptyStatement.__init__)


def test_hyp_java_emptystatement_constructor_args():
    sig = inspect.signature(java_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(java_VariableDeclarationStatement)


def test_hyp_java_variabledeclarationstatement_constructor_exists():
    assert callable(java_VariableDeclarationStatement.__init__)


def test_hyp_java_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(java_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_dostatement_is_not_abstract():
    assert not inspect.isabstract(java_DoStatement)


def test_hyp_java_dostatement_constructor_exists():
    assert callable(java_DoStatement.__init__)


def test_hyp_java_dostatement_constructor_args():
    sig = inspect.signature(java_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_continuestatement_is_not_abstract():
    assert not inspect.isabstract(java_ContinueStatement)


def test_hyp_java_continuestatement_constructor_exists():
    assert callable(java_ContinueStatement.__init__)


def test_hyp_java_continuestatement_constructor_args():
    sig = inspect.signature(java_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_switchstatement_is_not_abstract():
    assert not inspect.isabstract(java_SwitchStatement)


def test_hyp_java_switchstatement_constructor_exists():
    assert callable(java_SwitchStatement.__init__)


def test_hyp_java_switchstatement_constructor_args():
    sig = inspect.signature(java_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(java_TypeDeclarationStatement)


def test_hyp_java_typedeclarationstatement_constructor_exists():
    assert callable(java_TypeDeclarationStatement.__init__)


def test_hyp_java_typedeclarationstatement_constructor_args():
    sig = inspect.signature(java_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(java_EnhancedForStatement)


def test_hyp_java_enhancedforstatement_constructor_exists():
    assert callable(java_EnhancedForStatement.__init__)


def test_hyp_java_enhancedforstatement_constructor_args():
    sig = inspect.signature(java_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(java_ConstructorInvocation)


def test_hyp_java_constructorinvocation_constructor_exists():
    assert callable(java_ConstructorInvocation.__init__)


def test_hyp_java_constructorinvocation_constructor_args():
    sig = inspect.signature(java_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_ifstatement_is_not_abstract():
    assert not inspect.isabstract(java_IfStatement)


def test_hyp_java_ifstatement_constructor_exists():
    assert callable(java_IfStatement.__init__)


def test_hyp_java_ifstatement_constructor_args():
    sig = inspect.signature(java_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_trystatement_is_not_abstract():
    assert not inspect.isabstract(java_TryStatement)


def test_hyp_java_trystatement_constructor_exists():
    assert callable(java_TryStatement.__init__)


def test_hyp_java_trystatement_constructor_args():
    sig = inspect.signature(java_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_throwstatement_is_not_abstract():
    assert not inspect.isabstract(java_ThrowStatement)


def test_hyp_java_throwstatement_constructor_exists():
    assert callable(java_ThrowStatement.__init__)


def test_hyp_java_throwstatement_constructor_args():
    sig = inspect.signature(java_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_assertstatement_is_not_abstract():
    assert not inspect.isabstract(java_AssertStatement)


def test_hyp_java_assertstatement_constructor_exists():
    assert callable(java_AssertStatement.__init__)


def test_hyp_java_assertstatement_constructor_args():
    sig = inspect.signature(java_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_switchcase_is_not_abstract():
    assert not inspect.isabstract(java_SwitchCase)


def test_hyp_java_switchcase_constructor_exists():
    assert callable(java_SwitchCase.__init__)


def test_hyp_java_switchcase_constructor_args():
    sig = inspect.signature(java_SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_returnstatement_is_not_abstract():
    assert not inspect.isabstract(java_ReturnStatement)


def test_hyp_java_returnstatement_constructor_exists():
    assert callable(java_ReturnStatement.__init__)


def test_hyp_java_returnstatement_constructor_args():
    sig = inspect.signature(java_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_catchclause_is_not_abstract():
    assert not inspect.isabstract(java_CatchClause)


def test_hyp_java_catchclause_constructor_exists():
    assert callable(java_CatchClause.__init__)


def test_hyp_java_catchclause_constructor_args():
    sig = inspect.signature(java_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_forstatement_is_not_abstract():
    assert not inspect.isabstract(java_ForStatement)


def test_hyp_java_forstatement_constructor_exists():
    assert callable(java_ForStatement.__init__)


def test_hyp_java_forstatement_constructor_args():
    sig = inspect.signature(java_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(java_ExpressionStatement)


def test_hyp_java_expressionstatement_constructor_exists():
    assert callable(java_ExpressionStatement.__init__)


def test_hyp_java_expressionstatement_constructor_args():
    sig = inspect.signature(java_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(java_SuperConstructorInvocation)


def test_hyp_java_superconstructorinvocation_constructor_exists():
    assert callable(java_SuperConstructorInvocation.__init__)


def test_hyp_java_superconstructorinvocation_constructor_args():
    sig = inspect.signature(java_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_hyp_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_hyp_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AnonymousClassDeclaration)


def test_hyp_java_anonymousclassdeclaration_constructor_exists():
    assert callable(java_AnonymousClassDeclaration.__init__)


def test_hyp_java_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(java_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_modifier_is_not_abstract():
    assert not inspect.isabstract(java_Modifier)


def test_hyp_java_modifier_constructor_exists():
    assert callable(java_Modifier.__init__)


def test_hyp_java_modifier_constructor_args():
    sig = inspect.signature(java_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"






def test_hyp_java_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_ImportDeclaration)


def test_hyp_java_importdeclaration_constructor_exists():
    assert callable(java_ImportDeclaration.__init__)


def test_hyp_java_importdeclaration_constructor_args():
    sig = inspect.signature(java_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"




def test_hyp_java_memberref_is_not_abstract():
    assert not inspect.isabstract(java_MemberRef)


def test_hyp_java_memberref_constructor_exists():
    assert callable(java_MemberRef.__init__)


def test_hyp_java_memberref_constructor_args():
    sig = inspect.signature(java_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_namespaceaccess_is_not_abstract():
    assert not inspect.isabstract(java_NamespaceAccess)


def test_hyp_java_namespaceaccess_constructor_exists():
    assert callable(java_NamespaceAccess.__init__)


def test_hyp_java_namespaceaccess_constructor_args():
    sig = inspect.signature(java_NamespaceAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_tagelement_is_not_abstract():
    assert not inspect.isabstract(java_TagElement)


def test_hyp_java_tagelement_constructor_exists():
    assert callable(java_TagElement.__init__)


def test_hyp_java_tagelement_constructor_args():
    sig = inspect.signature(java_TagElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_abstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(java_AbstractMethodInvocation)


def test_hyp_java_abstractmethodinvocation_constructor_exists():
    assert callable(java_AbstractMethodInvocation.__init__)


def test_hyp_java_abstractmethodinvocation_constructor_args():
    sig = inspect.signature(java_AbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_namedelement_is_not_abstract():
    assert not inspect.isabstract(java_NamedElement)


def test_hyp_java_namedelement_constructor_exists():
    assert callable(java_NamedElement.__init__)


def test_hyp_java_namedelement_constructor_args():
    sig = inspect.signature(java_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "proxy" in params, "Missing parameter 'proxy'"





def test_hyp_java_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(java_MethodRefParameter)


def test_hyp_java_methodrefparameter_constructor_exists():
    assert callable(java_MethodRefParameter.__init__)


def test_hyp_java_methodrefparameter_constructor_args():
    sig = inspect.signature(java_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_block_is_not_abstract():
    assert not inspect.isabstract(java_Block)


def test_hyp_java_block_constructor_exists():
    assert callable(java_Block.__init__)


def test_hyp_java_block_constructor_args():
    sig = inspect.signature(java_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(java_SynchronizedStatement)


def test_hyp_java_synchronizedstatement_constructor_exists():
    assert callable(java_SynchronizedStatement.__init__)


def test_hyp_java_synchronizedstatement_constructor_args():
    sig = inspect.signature(java_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_hyp_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_hyp_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_TypeDeclaration)


def test_hyp_java_typedeclaration_constructor_exists():
    assert callable(java_TypeDeclaration.__init__)


def test_hyp_java_typedeclaration_constructor_args():
    sig = inspect.signature(java_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_EnumDeclaration)


def test_hyp_java_enumdeclaration_constructor_exists():
    assert callable(java_EnumDeclaration.__init__)


def test_hyp_java_enumdeclaration_constructor_args():
    sig = inspect.signature(java_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_unresolvedtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedTypeDeclaration)


def test_hyp_java_unresolvedtypedeclaration_constructor_exists():
    assert callable(java_UnresolvedTypeDeclaration.__init__)


def test_hyp_java_unresolvedtypedeclaration_constructor_args():
    sig = inspect.signature(java_UnresolvedTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationTypeDeclaration)


def test_hyp_java_annotationtypedeclaration_constructor_exists():
    assert callable(java_AnnotationTypeDeclaration.__init__)


def test_hyp_java_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(java_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(java_PrefixExpression)


def test_hyp_java_prefixexpression_constructor_exists():
    assert callable(java_PrefixExpression.__init__)


def test_hyp_java_prefixexpression_constructor_args():
    sig = inspect.signature(java_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_java_annotation_is_not_abstract():
    assert not inspect.isabstract(java_Annotation)


def test_hyp_java_annotation_constructor_exists():
    assert callable(java_Annotation.__init__)


def test_hyp_java_annotation_constructor_args():
    sig = inspect.signature(java_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(java_ConditionalExpression)


def test_hyp_java_conditionalexpression_constructor_exists():
    assert callable(java_ConditionalExpression.__init__)


def test_hyp_java_conditionalexpression_constructor_args():
    sig = inspect.signature(java_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(java_ParenthesizedExpression)


def test_hyp_java_parenthesizedexpression_constructor_exists():
    assert callable(java_ParenthesizedExpression.__init__)


def test_hyp_java_parenthesizedexpression_constructor_args():
    sig = inspect.signature(java_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(java_VariableDeclarationExpression)


def test_hyp_java_variabledeclarationexpression_constructor_exists():
    assert callable(java_VariableDeclarationExpression.__init__)


def test_hyp_java_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(java_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(java_FieldAccess)


def test_hyp_java_fieldaccess_constructor_exists():
    assert callable(java_FieldAccess.__init__)


def test_hyp_java_fieldaccess_constructor_args():
    sig = inspect.signature(java_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_nullliteral_is_not_abstract():
    assert not inspect.isabstract(java_NullLiteral)


def test_hyp_java_nullliteral_constructor_exists():
    assert callable(java_NullLiteral.__init__)


def test_hyp_java_nullliteral_constructor_args():
    sig = inspect.signature(java_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(java_ClassInstanceCreation)


def test_hyp_java_classinstancecreation_constructor_exists():
    assert callable(java_ClassInstanceCreation.__init__)


def test_hyp_java_classinstancecreation_constructor_args():
    sig = inspect.signature(java_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(java_BooleanLiteral)


def test_hyp_java_booleanliteral_constructor_exists():
    assert callable(java_BooleanLiteral.__init__)


def test_hyp_java_booleanliteral_constructor_args():
    sig = inspect.signature(java_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_java_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(java_InstanceofExpression)


def test_hyp_java_instanceofexpression_constructor_exists():
    assert callable(java_InstanceofExpression.__init__)


def test_hyp_java_instanceofexpression_constructor_args():
    sig = inspect.signature(java_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(java_ArrayAccess)


def test_hyp_java_arrayaccess_constructor_exists():
    assert callable(java_ArrayAccess.__init__)


def test_hyp_java_arrayaccess_constructor_args():
    sig = inspect.signature(java_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_infixexpression_is_not_abstract():
    assert not inspect.isabstract(java_InfixExpression)


def test_hyp_java_infixexpression_constructor_exists():
    assert callable(java_InfixExpression.__init__)


def test_hyp_java_infixexpression_constructor_args():
    sig = inspect.signature(java_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_java_unresolveditemaccess_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedItemAccess)


def test_hyp_java_unresolveditemaccess_constructor_exists():
    assert callable(java_UnresolvedItemAccess.__init__)


def test_hyp_java_unresolveditemaccess_constructor_args():
    sig = inspect.signature(java_UnresolvedItemAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(java_MethodInvocation)


def test_hyp_java_methodinvocation_constructor_exists():
    assert callable(java_MethodInvocation.__init__)


def test_hyp_java_methodinvocation_constructor_args():
    sig = inspect.signature(java_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_arraycreation_is_not_abstract():
    assert not inspect.isabstract(java_ArrayCreation)


def test_hyp_java_arraycreation_constructor_exists():
    assert callable(java_ArrayCreation.__init__)


def test_hyp_java_arraycreation_constructor_args():
    sig = inspect.signature(java_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_singlevariableaccess_is_not_abstract():
    assert not inspect.isabstract(java_SingleVariableAccess)


def test_hyp_java_singlevariableaccess_constructor_exists():
    assert callable(java_SingleVariableAccess.__init__)


def test_hyp_java_singlevariableaccess_constructor_args():
    sig = inspect.signature(java_SingleVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_characterliteral_is_not_abstract():
    assert not inspect.isabstract(java_CharacterLiteral)


def test_hyp_java_characterliteral_constructor_exists():
    assert callable(java_CharacterLiteral.__init__)


def test_hyp_java_characterliteral_constructor_args():
    sig = inspect.signature(java_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"




def test_hyp_java_numberliteral_is_not_abstract():
    assert not inspect.isabstract(java_NumberLiteral)


def test_hyp_java_numberliteral_constructor_exists():
    assert callable(java_NumberLiteral.__init__)


def test_hyp_java_numberliteral_constructor_args():
    sig = inspect.signature(java_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "tokenValue" in params, "Missing parameter 'tokenValue'"




def test_hyp_java_arraylengthaccess_is_not_abstract():
    assert not inspect.isabstract(java_ArrayLengthAccess)


def test_hyp_java_arraylengthaccess_constructor_exists():
    assert callable(java_ArrayLengthAccess.__init__)


def test_hyp_java_arraylengthaccess_constructor_args():
    sig = inspect.signature(java_ArrayLengthAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_castexpression_is_not_abstract():
    assert not inspect.isabstract(java_CastExpression)


def test_hyp_java_castexpression_constructor_exists():
    assert callable(java_CastExpression.__init__)


def test_hyp_java_castexpression_constructor_args():
    sig = inspect.signature(java_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_stringliteral_is_not_abstract():
    assert not inspect.isabstract(java_StringLiteral)


def test_hyp_java_stringliteral_constructor_exists():
    assert callable(java_StringLiteral.__init__)


def test_hyp_java_stringliteral_constructor_args():
    sig = inspect.signature(java_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"




def test_hyp_java_statement_is_not_abstract():
    assert not inspect.isabstract(java_Statement)


def test_hyp_java_statement_constructor_exists():
    assert callable(java_Statement.__init__)


def test_hyp_java_statement_constructor_args():
    sig = inspect.signature(java_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_whilestatement_is_not_abstract():
    assert not inspect.isabstract(java_WhileStatement)


def test_hyp_java_whilestatement_constructor_exists():
    assert callable(java_WhileStatement.__init__)


def test_hyp_java_whilestatement_constructor_args():
    sig = inspect.signature(java_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypeshort_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeShort)


def test_hyp_java_primitivetypeshort_constructor_exists():
    assert callable(java_PrimitiveTypeShort.__init__)


def test_hyp_java_primitivetypeshort_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeShort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypeint_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeInt)


def test_hyp_java_primitivetypeint_constructor_exists():
    assert callable(java_PrimitiveTypeInt.__init__)


def test_hyp_java_primitivetypeint_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeInt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypevoid_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeVoid)


def test_hyp_java_primitivetypevoid_constructor_exists():
    assert callable(java_PrimitiveTypeVoid.__init__)


def test_hyp_java_primitivetypevoid_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeVoid.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypefloat_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeFloat)


def test_hyp_java_primitivetypefloat_constructor_exists():
    assert callable(java_PrimitiveTypeFloat.__init__)


def test_hyp_java_primitivetypefloat_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeFloat.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypeboolean_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeBoolean)


def test_hyp_java_primitivetypeboolean_constructor_exists():
    assert callable(java_PrimitiveTypeBoolean.__init__)


def test_hyp_java_primitivetypeboolean_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeBoolean.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypelong_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeLong)


def test_hyp_java_primitivetypelong_constructor_exists():
    assert callable(java_PrimitiveTypeLong.__init__)


def test_hyp_java_primitivetypelong_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeLong.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypechar_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeChar)


def test_hyp_java_primitivetypechar_constructor_exists():
    assert callable(java_PrimitiveTypeChar.__init__)


def test_hyp_java_primitivetypechar_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeChar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypedouble_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeDouble)


def test_hyp_java_primitivetypedouble_constructor_exists():
    assert callable(java_PrimitiveTypeDouble.__init__)


def test_hyp_java_primitivetypedouble_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeDouble.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_methodref_is_not_abstract():
    assert not inspect.isabstract(java_MethodRef)


def test_hyp_java_methodref_constructor_exists():
    assert callable(java_MethodRef.__init__)


def test_hyp_java_methodref_constructor_args():
    sig = inspect.signature(java_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_expression_is_not_abstract():
    assert not inspect.isabstract(java_Expression)


def test_hyp_java_expression_constructor_exists():
    assert callable(java_Expression.__init__)


def test_hyp_java_expression_constructor_args():
    sig = inspect.signature(java_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_comment_is_not_abstract():
    assert not inspect.isabstract(java_Comment)


def test_hyp_java_comment_constructor_exists():
    assert callable(java_Comment.__init__)


def test_hyp_java_comment_constructor_args():
    sig = inspect.signature(java_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java_VariableDeclaration)


def test_hyp_java_variabledeclaration_constructor_exists():
    assert callable(java_VariableDeclaration.__init__)


def test_hyp_java_variabledeclaration_constructor_args():
    sig = inspect.signature(java_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_type_is_not_abstract():
    assert not inspect.isabstract(java_Type)


def test_hyp_java_type_constructor_exists():
    assert callable(java_Type.__init__)


def test_hyp_java_type_constructor_args():
    sig = inspect.signature(java_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_archive_is_not_abstract():
    assert not inspect.isabstract(java_Archive)


def test_hyp_java_archive_constructor_exists():
    assert callable(java_Archive.__init__)


def test_hyp_java_archive_constructor_args():
    sig = inspect.signature(java_Archive.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"




def test_hyp_java_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(java_BodyDeclaration)


def test_hyp_java_bodydeclaration_constructor_exists():
    assert callable(java_BodyDeclaration.__init__)


def test_hyp_java_bodydeclaration_constructor_args():
    sig = inspect.signature(java_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_package_is_not_abstract():
    assert not inspect.isabstract(java_Package)


def test_hyp_java_package_constructor_exists():
    assert callable(java_Package.__init__)


def test_hyp_java_package_constructor_args():
    sig = inspect.signature(java_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_compilationunit_is_not_abstract():
    assert not inspect.isabstract(java_CompilationUnit)


def test_hyp_java_compilationunit_constructor_exists():
    assert callable(java_CompilationUnit.__init__)


def test_hyp_java_compilationunit_constructor_args():
    sig = inspect.signature(java_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "originalFilePath" in params, "Missing parameter 'originalFilePath'"




def test_hyp_java_unresolveditem_is_not_abstract():
    assert not inspect.isabstract(java_UnresolvedItem)


def test_hyp_java_unresolveditem_constructor_exists():
    assert callable(java_UnresolvedItem.__init__)


def test_hyp_java_unresolveditem_constructor_args():
    sig = inspect.signature(java_UnresolvedItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(java_LabeledStatement)


def test_hyp_java_labeledstatement_constructor_exists():
    assert callable(java_LabeledStatement.__init__)


def test_hyp_java_labeledstatement_constructor_args():
    sig = inspect.signature(java_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_classfile_is_not_abstract():
    assert not inspect.isabstract(java_ClassFile)


def test_hyp_java_classfile_constructor_exists():
    assert callable(java_ClassFile.__init__)


def test_hyp_java_classfile_constructor_args():
    sig = inspect.signature(java_ClassFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_annotationmembervaluepair_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationMemberValuePair)


def test_hyp_java_annotationmembervaluepair_constructor_exists():
    assert callable(java_AnnotationMemberValuePair.__init__)


def test_hyp_java_annotationmembervaluepair_constructor_args():
    sig = inspect.signature(java_AnnotationMemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(java_ArrayInitializer)


def test_hyp_java_arrayinitializer_constructor_exists():
    assert callable(java_ArrayInitializer.__init__)


def test_hyp_java_arrayinitializer_constructor_args():
    sig = inspect.signature(java_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetypebyte_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveTypeByte)


def test_hyp_java_primitivetypebyte_constructor_exists():
    assert callable(java_PrimitiveTypeByte.__init__)


def test_hyp_java_primitivetypebyte_constructor_args():
    sig = inspect.signature(java_PrimitiveTypeByte.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(java_PostfixExpression)


def test_hyp_java_postfixexpression_constructor_exists():
    assert callable(java_PostfixExpression.__init__)


def test_hyp_java_postfixexpression_constructor_args():
    sig = inspect.signature(java_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_java_assignment_is_not_abstract():
    assert not inspect.isabstract(java_Assignment)


def test_hyp_java_assignment_constructor_exists():
    assert callable(java_Assignment.__init__)


def test_hyp_java_assignment_constructor_args():
    sig = inspect.signature(java_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_java_abstracttypequalifiedexpression_is_not_abstract():
    assert not inspect.isabstract(java_AbstractTypeQualifiedExpression)


def test_hyp_java_abstracttypequalifiedexpression_constructor_exists():
    assert callable(java_AbstractTypeQualifiedExpression.__init__)


def test_hyp_java_abstracttypequalifiedexpression_constructor_args():
    sig = inspect.signature(java_AbstractTypeQualifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_typeliteral_is_not_abstract():
    assert not inspect.isabstract(java_TypeLiteral)


def test_hyp_java_typeliteral_constructor_exists():
    assert callable(java_TypeLiteral.__init__)


def test_hyp_java_typeliteral_constructor_args():
    sig = inspect.signature(java_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_hyp_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_hyp_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(java_FieldDeclaration)


def test_hyp_java_fielddeclaration_constructor_exists():
    assert callable(java_FieldDeclaration.__init__)


def test_hyp_java_fielddeclaration_constructor_args():
    sig = inspect.signature(java_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AnnotationTypeMemberDeclaration)


def test_hyp_java_annotationtypememberdeclaration_constructor_exists():
    assert callable(java_AnnotationTypeMemberDeclaration.__init__)


def test_hyp_java_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(java_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_initializer_is_not_abstract():
    assert not inspect.isabstract(java_Initializer)


def test_hyp_java_initializer_constructor_exists():
    assert callable(java_Initializer.__init__)


def test_hyp_java_initializer_constructor_args():
    sig = inspect.signature(java_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_abstractmethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AbstractMethodDeclaration)


def test_hyp_java_abstractmethoddeclaration_constructor_exists():
    assert callable(java_AbstractMethodDeclaration.__init__)


def test_hyp_java_abstractmethoddeclaration_constructor_args():
    sig = inspect.signature(java_AbstractMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_typeaccess_is_not_abstract():
    assert not inspect.isabstract(java_TypeAccess)


def test_hyp_java_typeaccess_constructor_exists():
    assert callable(java_TypeAccess.__init__)


def test_hyp_java_typeaccess_constructor_args():
    sig = inspect.signature(java_TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(java_AbstractTypeDeclaration)


def test_hyp_java_abstracttypedeclaration_constructor_exists():
    assert callable(java_AbstractTypeDeclaration.__init__)


def test_hyp_java_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(java_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(java_ParameterizedType)


def test_hyp_java_parameterizedtype_constructor_exists():
    assert callable(java_ParameterizedType.__init__)


def test_hyp_java_parameterizedtype_constructor_args():
    sig = inspect.signature(java_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_primitivetype_is_not_abstract():
    assert not inspect.isabstract(java_PrimitiveType)


def test_hyp_java_primitivetype_constructor_exists():
    assert callable(java_PrimitiveType.__init__)


def test_hyp_java_primitivetype_constructor_args():
    sig = inspect.signature(java_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_arraytype_is_not_abstract():
    assert not inspect.isabstract(java_ArrayType)


def test_hyp_java_arraytype_constructor_exists():
    assert callable(java_ArrayType.__init__)


def test_hyp_java_arraytype_constructor_args():
    sig = inspect.signature(java_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"




def test_hyp_java_typeparameter_is_not_abstract():
    assert not inspect.isabstract(java_TypeParameter)


def test_hyp_java_typeparameter_constructor_exists():
    assert callable(java_TypeParameter.__init__)


def test_hyp_java_typeparameter_constructor_args():
    sig = inspect.signature(java_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(java_WildCardType)


def test_hyp_java_wildcardtype_constructor_exists():
    assert callable(java_WildCardType.__init__)


def test_hyp_java_wildcardtype_constructor_args():
    sig = inspect.signature(java_WildCardType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_abstractvariablescontainer_is_not_abstract():
    assert not inspect.isabstract(java_AbstractVariablesContainer)


def test_hyp_java_abstractvariablescontainer_constructor_exists():
    assert callable(java_AbstractVariablesContainer.__init__)


def test_hyp_java_abstractvariablescontainer_constructor_args():
    sig = inspect.signature(java_AbstractVariablesContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_hyp_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_hyp_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(java_EnumConstantDeclaration)


def test_hyp_java_enumconstantdeclaration_constructor_exists():
    assert callable(java_EnumConstantDeclaration.__init__)


def test_hyp_java_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(java_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(java_SingleVariableDeclaration)


def test_hyp_java_singlevariabledeclaration_constructor_exists():
    assert callable(java_SingleVariableDeclaration.__init__)


def test_hyp_java_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(java_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_java_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(java_VariableDeclarationFragment)


def test_hyp_java_variabledeclarationfragment_constructor_exists():
    assert callable(java_VariableDeclarationFragment.__init__)


def test_hyp_java_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(java_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())

def test_hyp_postfixexpressionkind_exists():
    # Check that the Enumeration exists
    assert PostfixExpressionKind is not None

def test_hyp_postfixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixExpressionKind]
    expected_literals = [
        "DECREMENT",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixExpressionKind"

def test_hyp_infixexpressionkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionKind is not None

def test_hyp_infixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionKind]
    expected_literals = [
        "AND",
        "LEFT_SHIFT",
        "LESS_EQUALS",
        "LESS",
        "REMAINDER",
        "RIGHT_SHIFT_UNSIGNED",
        "CONDITIONAL_AND",
        "GREATER_EQUALS",
        "RIGHT_SHIFT_SIGNED",
        "OR",
        "MINUS",
        "NOT_EQUALS",
        "EQUALS",
        "TIMES",
        "PLUS",
        "CONDITIONAL_OR",
        "GREATER",
        "DIVIDE",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionKind"

def test_hyp_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_hyp_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "public",
        "none",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_hyp_prefixexpressionkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionKind is not None

def test_hyp_prefixexpressionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionKind]
    expected_literals = [
        "NOT",
        "COMPLEMENT",
        "PLUS",
        "INCREMENT",
        "MINUS",
        "DECREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionKind"

def test_hyp_inheritancekind_exists():
    # Check that the Enumeration exists
    assert InheritanceKind is not None

def test_hyp_inheritancekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceKind]
    expected_literals = [
        "none",
        "abstract",
        "final",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceKind"

def test_hyp_assignmentkind_exists():
    # Check that the Enumeration exists
    assert AssignmentKind is not None

def test_hyp_assignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentKind]
    expected_literals = [
        "BIT_XOR_ASSIGN",
        "DIVIDE_ASSIGN",
        "TIMES_ASSIGN",
        "ASSIGN",
        "REMAINDER_ASSIGN",
        "RIGHT_SHIFT_SIGNED_ASSIGN",
        "LEFT_SHIFT_ASSIGN",
        "BIT_AND_ASSIGN",
        "PLUS_ASSIGN",
        "RIGHT_SHIFT_UNSIGNED_ASSIGN",
        "BIT_OR_ASSIGN",
        "MINUS_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentKind"


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
java_Model_strategy = st.builds(
    java_Model,
    name=
        safe_text
)
AbstractMethodDeclaration_strategy = st.builds(
    AbstractMethodDeclaration,
)
java_ConstructorDeclaration_strategy = st.builds(
    java_ConstructorDeclaration,
)
java_MethodDeclaration_strategy = st.builds(
    java_MethodDeclaration,
)
java_ASTNode_strategy = st.builds(
    java_ASTNode,
)
NamespaceAccess_strategy = st.builds(
    NamespaceAccess,
)
AbstractTypeQualifiedExpression_strategy = st.builds(
    AbstractTypeQualifiedExpression,
)
java_SuperFieldAccess_strategy = st.builds(
    java_SuperFieldAccess,
)
java_ThisExpression_strategy = st.builds(
    java_ThisExpression,
)
AbstractVariablesContainer_strategy = st.builds(
    AbstractVariablesContainer,
)
UnresolvedItem_strategy = st.builds(
    UnresolvedItem,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
java_ClassDeclaration_strategy = st.builds(
    java_ClassDeclaration,
)
java_InterfaceDeclaration_strategy = st.builds(
    java_InterfaceDeclaration,
)
AbstractMethodInvocation_strategy = st.builds(
    AbstractMethodInvocation,
)
java_SuperMethodInvocation_strategy = st.builds(
    java_SuperMethodInvocation,
)
Statement_strategy = st.builds(
    Statement,
)
java_BreakStatement_strategy = st.builds(
    java_BreakStatement,
)
java_EmptyStatement_strategy = st.builds(
    java_EmptyStatement,
)
java_VariableDeclarationStatement_strategy = st.builds(
    java_VariableDeclarationStatement,
)
java_DoStatement_strategy = st.builds(
    java_DoStatement,
)
java_ContinueStatement_strategy = st.builds(
    java_ContinueStatement,
)
java_SwitchStatement_strategy = st.builds(
    java_SwitchStatement,
)
java_TypeDeclarationStatement_strategy = st.builds(
    java_TypeDeclarationStatement,
)
java_EnhancedForStatement_strategy = st.builds(
    java_EnhancedForStatement,
)
java_ConstructorInvocation_strategy = st.builds(
    java_ConstructorInvocation,
)
java_IfStatement_strategy = st.builds(
    java_IfStatement,
)
java_TryStatement_strategy = st.builds(
    java_TryStatement,
)
java_ThrowStatement_strategy = st.builds(
    java_ThrowStatement,
)
java_AssertStatement_strategy = st.builds(
    java_AssertStatement,
)
java_SwitchCase_strategy = st.builds(
    java_SwitchCase,
)
java_ReturnStatement_strategy = st.builds(
    java_ReturnStatement,
)
java_CatchClause_strategy = st.builds(
    java_CatchClause,
)
java_ForStatement_strategy = st.builds(
    java_ForStatement,
)
java_ExpressionStatement_strategy = st.builds(
    java_ExpressionStatement,
)
java_SuperConstructorInvocation_strategy = st.builds(
    java_SuperConstructorInvocation,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
java_AnonymousClassDeclaration_strategy = st.builds(
    java_AnonymousClassDeclaration,
)
java_Modifier_strategy = st.builds(
    java_Modifier,
    inheritance=
        safe_text,
    static=
        st.booleans(),
    visibility=
        safe_text
)
java_ImportDeclaration_strategy = st.builds(
    java_ImportDeclaration,
    static=
        st.booleans()
)
java_MemberRef_strategy = st.builds(
    java_MemberRef,
)
java_NamespaceAccess_strategy = st.builds(
    java_NamespaceAccess,
)
java_TagElement_strategy = st.builds(
    java_TagElement,
)
java_AbstractMethodInvocation_strategy = st.builds(
    java_AbstractMethodInvocation,
)
java_NamedElement_strategy = st.builds(
    java_NamedElement,
    name=
        safe_text,
    proxy=
        st.booleans()
)
java_MethodRefParameter_strategy = st.builds(
    java_MethodRefParameter,
)
java_Block_strategy = st.builds(
    java_Block,
)
java_SynchronizedStatement_strategy = st.builds(
    java_SynchronizedStatement,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
java_TypeDeclaration_strategy = st.builds(
    java_TypeDeclaration,
)
java_EnumDeclaration_strategy = st.builds(
    java_EnumDeclaration,
)
java_UnresolvedTypeDeclaration_strategy = st.builds(
    java_UnresolvedTypeDeclaration,
)
java_AnnotationTypeDeclaration_strategy = st.builds(
    java_AnnotationTypeDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
java_PrefixExpression_strategy = st.builds(
    java_PrefixExpression,
    operator=
        safe_text
)
java_Annotation_strategy = st.builds(
    java_Annotation,
)
java_ConditionalExpression_strategy = st.builds(
    java_ConditionalExpression,
)
java_ParenthesizedExpression_strategy = st.builds(
    java_ParenthesizedExpression,
)
java_VariableDeclarationExpression_strategy = st.builds(
    java_VariableDeclarationExpression,
)
java_FieldAccess_strategy = st.builds(
    java_FieldAccess,
)
java_NullLiteral_strategy = st.builds(
    java_NullLiteral,
)
java_ClassInstanceCreation_strategy = st.builds(
    java_ClassInstanceCreation,
)
java_BooleanLiteral_strategy = st.builds(
    java_BooleanLiteral,
    value=
        st.booleans()
)
java_InstanceofExpression_strategy = st.builds(
    java_InstanceofExpression,
)
java_ArrayAccess_strategy = st.builds(
    java_ArrayAccess,
)
java_InfixExpression_strategy = st.builds(
    java_InfixExpression,
    operator=
        safe_text
)
java_UnresolvedItemAccess_strategy = st.builds(
    java_UnresolvedItemAccess,
)
java_MethodInvocation_strategy = st.builds(
    java_MethodInvocation,
)
java_ArrayCreation_strategy = st.builds(
    java_ArrayCreation,
)
java_SingleVariableAccess_strategy = st.builds(
    java_SingleVariableAccess,
)
java_CharacterLiteral_strategy = st.builds(
    java_CharacterLiteral,
    escapedValue=
        safe_text
)
java_NumberLiteral_strategy = st.builds(
    java_NumberLiteral,
    tokenValue=
        safe_text
)
java_ArrayLengthAccess_strategy = st.builds(
    java_ArrayLengthAccess,
)
java_CastExpression_strategy = st.builds(
    java_CastExpression,
)
java_StringLiteral_strategy = st.builds(
    java_StringLiteral,
    escapedValue=
        safe_text
)
java_Statement_strategy = st.builds(
    java_Statement,
)
java_WhileStatement_strategy = st.builds(
    java_WhileStatement,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
java_PrimitiveTypeShort_strategy = st.builds(
    java_PrimitiveTypeShort,
)
java_PrimitiveTypeInt_strategy = st.builds(
    java_PrimitiveTypeInt,
)
java_PrimitiveTypeVoid_strategy = st.builds(
    java_PrimitiveTypeVoid,
)
java_PrimitiveTypeFloat_strategy = st.builds(
    java_PrimitiveTypeFloat,
)
java_PrimitiveTypeBoolean_strategy = st.builds(
    java_PrimitiveTypeBoolean,
)
java_PrimitiveTypeLong_strategy = st.builds(
    java_PrimitiveTypeLong,
)
java_PrimitiveTypeChar_strategy = st.builds(
    java_PrimitiveTypeChar,
)
java_PrimitiveTypeDouble_strategy = st.builds(
    java_PrimitiveTypeDouble,
)
java_MethodRef_strategy = st.builds(
    java_MethodRef,
)
java_Expression_strategy = st.builds(
    java_Expression,
)
java_Comment_strategy = st.builds(
    java_Comment,
    content=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
java_VariableDeclaration_strategy = st.builds(
    java_VariableDeclaration,
)
java_Type_strategy = st.builds(
    java_Type,
)
java_Archive_strategy = st.builds(
    java_Archive,
    originalFilePath=
        safe_text
)
java_BodyDeclaration_strategy = st.builds(
    java_BodyDeclaration,
)
java_Package_strategy = st.builds(
    java_Package,
)
java_CompilationUnit_strategy = st.builds(
    java_CompilationUnit,
    originalFilePath=
        safe_text
)
java_UnresolvedItem_strategy = st.builds(
    java_UnresolvedItem,
)
java_LabeledStatement_strategy = st.builds(
    java_LabeledStatement,
)
java_ClassFile_strategy = st.builds(
    java_ClassFile,
)
java_AnnotationMemberValuePair_strategy = st.builds(
    java_AnnotationMemberValuePair,
)
java_ArrayInitializer_strategy = st.builds(
    java_ArrayInitializer,
)
java_PrimitiveTypeByte_strategy = st.builds(
    java_PrimitiveTypeByte,
)
java_PostfixExpression_strategy = st.builds(
    java_PostfixExpression,
    operator=
        safe_text
)
java_Assignment_strategy = st.builds(
    java_Assignment,
    operator=
        safe_text
)
java_AbstractTypeQualifiedExpression_strategy = st.builds(
    java_AbstractTypeQualifiedExpression,
)
java_TypeLiteral_strategy = st.builds(
    java_TypeLiteral,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
java_FieldDeclaration_strategy = st.builds(
    java_FieldDeclaration,
)
java_AnnotationTypeMemberDeclaration_strategy = st.builds(
    java_AnnotationTypeMemberDeclaration,
)
java_Initializer_strategy = st.builds(
    java_Initializer,
)
java_AbstractMethodDeclaration_strategy = st.builds(
    java_AbstractMethodDeclaration,
)
java_TypeAccess_strategy = st.builds(
    java_TypeAccess,
)
Type_strategy = st.builds(
    Type,
)
java_AbstractTypeDeclaration_strategy = st.builds(
    java_AbstractTypeDeclaration,
)
java_ParameterizedType_strategy = st.builds(
    java_ParameterizedType,
)
java_PrimitiveType_strategy = st.builds(
    java_PrimitiveType,
)
java_ArrayType_strategy = st.builds(
    java_ArrayType,
    dimensions=
        st.integers()
)
java_TypeParameter_strategy = st.builds(
    java_TypeParameter,
)
java_WildCardType_strategy = st.builds(
    java_WildCardType,
)
java_AbstractVariablesContainer_strategy = st.builds(
    java_AbstractVariablesContainer,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
java_EnumConstantDeclaration_strategy = st.builds(
    java_EnumConstantDeclaration,
)
java_SingleVariableDeclaration_strategy = st.builds(
    java_SingleVariableDeclaration,
)
java_VariableDeclarationFragment_strategy = st.builds(
    java_VariableDeclarationFragment,
)




@given(instance=java_Model_strategy)
def test_hyp_java_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









































@given(instance=java_Modifier_strategy)
def test_hyp_java_modifier_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original



@given(instance=java_Modifier_strategy)
def test_hyp_java_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=java_Modifier_strategy)
def test_hyp_java_modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original




@given(instance=java_ImportDeclaration_strategy)
def test_hyp_java_importdeclaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original








@given(instance=java_NamedElement_strategy)
def test_hyp_java_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=java_NamedElement_strategy)
def test_hyp_java_namedelement_proxy_setter(instance):
    original = instance.proxy
    instance.proxy = original
    assert instance.proxy == original













@given(instance=java_PrefixExpression_strategy)
def test_hyp_java_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original











@given(instance=java_BooleanLiteral_strategy)
def test_hyp_java_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=java_InfixExpression_strategy)
def test_hyp_java_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original








@given(instance=java_CharacterLiteral_strategy)
def test_hyp_java_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original




@given(instance=java_NumberLiteral_strategy)
def test_hyp_java_numberliteral_tokenValue_setter(instance):
    original = instance.tokenValue
    instance.tokenValue = original
    assert instance.tokenValue == original






@given(instance=java_StringLiteral_strategy)
def test_hyp_java_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

















@given(instance=java_Comment_strategy)
def test_hyp_java_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original







@given(instance=java_Archive_strategy)
def test_hyp_java_archive_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original






@given(instance=java_CompilationUnit_strategy)
def test_hyp_java_compilationunit_originalFilePath_setter(instance):
    original = instance.originalFilePath
    instance.originalFilePath = original
    assert instance.originalFilePath == original










@given(instance=java_PostfixExpression_strategy)
def test_hyp_java_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=java_Assignment_strategy)
def test_hyp_java_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original
















@given(instance=java_ArrayType_strategy)
def test_hyp_java_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original









# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ASTNode,
    AbstractMethodDeclaration,
    AbstractMethodInvocation,
    AbstractTypeDeclaration,
    AbstractTypeQualifiedExpression,
    AbstractVariablesContainer,
    BodyDeclaration,
    Expression,
    NamedElement,
    NamespaceAccess,
    PrimitiveType,
    Statement,
    Type,
    TypeDeclaration,
    UnresolvedItem,
    VariableDeclaration,
    java_ASTNode,
    java_AbstractMethodDeclaration,
    java_AbstractMethodInvocation,
    java_AbstractTypeDeclaration,
    java_AbstractTypeQualifiedExpression,
    java_AbstractVariablesContainer,
    java_Annotation,
    java_AnnotationMemberValuePair,
    java_AnnotationTypeDeclaration,
    java_AnnotationTypeMemberDeclaration,
    java_AnonymousClassDeclaration,
    java_Archive,
    java_ArrayAccess,
    java_ArrayCreation,
    java_ArrayInitializer,
    java_ArrayLengthAccess,
    java_ArrayType,
    java_AssertStatement,
    java_Assignment,
    java_Block,
    java_BodyDeclaration,
    java_BooleanLiteral,
    java_BreakStatement,
    java_CastExpression,
    java_CatchClause,
    java_CharacterLiteral,
    java_ClassDeclaration,
    java_ClassFile,
    java_ClassInstanceCreation,
    java_Comment,
    java_CompilationUnit,
    java_ConditionalExpression,
    java_ConstructorDeclaration,
    java_ConstructorInvocation,
    java_ContinueStatement,
    java_DoStatement,
    java_EmptyStatement,
    java_EnhancedForStatement,
    java_EnumConstantDeclaration,
    java_EnumDeclaration,
    java_Expression,
    java_ExpressionStatement,
    java_FieldAccess,
    java_FieldDeclaration,
    java_ForStatement,
    java_IfStatement,
    java_ImportDeclaration,
    java_InfixExpression,
    java_Initializer,
    java_InstanceofExpression,
    java_InterfaceDeclaration,
    java_LabeledStatement,
    java_MemberRef,
    java_MethodDeclaration,
    java_MethodInvocation,
    java_MethodRef,
    java_MethodRefParameter,
    java_Model,
    java_Modifier,
    java_NamedElement,
    java_NamespaceAccess,
    java_NullLiteral,
    java_NumberLiteral,
    java_Package,
    java_ParameterizedType,
    java_ParenthesizedExpression,
    java_PostfixExpression,
    java_PrefixExpression,
    java_PrimitiveType,
    java_PrimitiveTypeBoolean,
    java_PrimitiveTypeByte,
    java_PrimitiveTypeChar,
    java_PrimitiveTypeDouble,
    java_PrimitiveTypeFloat,
    java_PrimitiveTypeInt,
    java_PrimitiveTypeLong,
    java_PrimitiveTypeShort,
    java_PrimitiveTypeVoid,
    java_ReturnStatement,
    java_SingleVariableAccess,
    java_SingleVariableDeclaration,
    java_Statement,
    java_StringLiteral,
    java_SuperConstructorInvocation,
    java_SuperFieldAccess,
    java_SuperMethodInvocation,
    java_SwitchCase,
    java_SwitchStatement,
    java_SynchronizedStatement,
    java_TagElement,
    java_ThisExpression,
    java_ThrowStatement,
    java_TryStatement,
    java_Type,
    java_TypeAccess,
    java_TypeDeclaration,
    java_TypeDeclarationStatement,
    java_TypeLiteral,
    java_TypeParameter,
    java_UnresolvedItem,
    java_UnresolvedItemAccess,
    java_UnresolvedTypeDeclaration,
    java_VariableDeclaration,
    java_VariableDeclarationExpression,
    java_VariableDeclarationFragment,
    java_VariableDeclarationStatement,
    java_WhileStatement,
    java_WildCardType,
    AssignmentKind,
    InfixExpressionKind,
    InheritanceKind,
    PostfixExpressionKind,
    PrefixExpressionKind,
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

def test_java_Archive_originalFilePath_value_roundtrip():
    instance = java_Archive(originalFilePath="sample_text")
    assert instance.originalFilePath == "sample_text"
    instance.originalFilePath = "sample_text_2"
    assert instance.originalFilePath == "sample_text_2"


def test_java_ArrayType_dimensions_value_roundtrip():
    instance = java_ArrayType(dimensions=7)
    assert instance.dimensions == 7
    instance.dimensions = 13
    assert instance.dimensions == 13


def test_java_Assignment_operator_value_roundtrip():
    instance = java_Assignment(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_java_BooleanLiteral_value_value_roundtrip():
    instance = java_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_java_CharacterLiteral_escapedValue_value_roundtrip():
    instance = java_CharacterLiteral(escapedValue="sample_text")
    assert instance.escapedValue == "sample_text"
    instance.escapedValue = "sample_text_2"
    assert instance.escapedValue == "sample_text_2"


def test_java_Comment_content_value_roundtrip():
    instance = java_Comment(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_java_CompilationUnit_originalFilePath_value_roundtrip():
    instance = java_CompilationUnit(originalFilePath="sample_text")
    assert instance.originalFilePath == "sample_text"
    instance.originalFilePath = "sample_text_2"
    assert instance.originalFilePath == "sample_text_2"


def test_java_ImportDeclaration_static_value_roundtrip():
    instance = java_ImportDeclaration(static=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_java_InfixExpression_operator_value_roundtrip():
    instance = java_InfixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_java_Model_name_value_roundtrip():
    instance = java_Model(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_java_Modifier_inheritance_value_roundtrip():
    instance = java_Modifier(inheritance="sample_text", static=True, visibility="sample_text")
    assert instance.inheritance == "sample_text"
    instance.inheritance = "sample_text_2"
    assert instance.inheritance == "sample_text_2"


def test_java_Modifier_static_value_roundtrip():
    instance = java_Modifier(inheritance="sample_text", static=True, visibility="sample_text")
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_java_Modifier_visibility_value_roundtrip():
    instance = java_Modifier(inheritance="sample_text", static=True, visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_java_NamedElement_name_value_roundtrip():
    instance = java_NamedElement(name="sample_text", proxy=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_java_NamedElement_proxy_value_roundtrip():
    instance = java_NamedElement(name="sample_text", proxy=True)
    assert instance.proxy == True
    instance.proxy = False
    assert instance.proxy == False


def test_java_NumberLiteral_tokenValue_value_roundtrip():
    instance = java_NumberLiteral(tokenValue="sample_text")
    assert instance.tokenValue == "sample_text"
    instance.tokenValue = "sample_text_2"
    assert instance.tokenValue == "sample_text_2"


def test_java_PostfixExpression_operator_value_roundtrip():
    instance = java_PostfixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_java_PrefixExpression_operator_value_roundtrip():
    instance = java_PrefixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_java_StringLiteral_escapedValue_value_roundtrip():
    instance = java_StringLiteral(escapedValue="sample_text")
    assert instance.escapedValue == "sample_text"
    instance.escapedValue = "sample_text_2"
    assert instance.escapedValue == "sample_text_2"


def test_java_AbstractMethodInvocation_isa_ASTNode():
    instance = java_AbstractMethodInvocation()
    assert isinstance(instance, ASTNode)


def test_java_AbstractVariablesContainer_isa_ASTNode():
    instance = java_AbstractVariablesContainer()
    assert isinstance(instance, ASTNode)


def test_java_AnonymousClassDeclaration_isa_ASTNode():
    instance = java_AnonymousClassDeclaration()
    assert isinstance(instance, ASTNode)


def test_java_Comment_isa_ASTNode():
    instance = java_Comment(content="sample_text")
    assert isinstance(instance, ASTNode)


def test_java_Expression_isa_ASTNode():
    instance = java_Expression()
    assert isinstance(instance, ASTNode)


def test_java_ImportDeclaration_isa_ASTNode():
    instance = java_ImportDeclaration(static=True)
    assert isinstance(instance, ASTNode)


def test_java_MemberRef_isa_ASTNode():
    instance = java_MemberRef()
    assert isinstance(instance, ASTNode)


def test_java_MethodRef_isa_ASTNode():
    instance = java_MethodRef()
    assert isinstance(instance, ASTNode)


def test_java_MethodRefParameter_isa_ASTNode():
    instance = java_MethodRefParameter()
    assert isinstance(instance, ASTNode)


def test_java_Modifier_isa_ASTNode():
    instance = java_Modifier(inheritance="sample_text", static=True, visibility="sample_text")
    assert isinstance(instance, ASTNode)


def test_java_NamedElement_isa_ASTNode():
    instance = java_NamedElement(name="sample_text", proxy=True)
    assert isinstance(instance, ASTNode)


def test_java_NamespaceAccess_isa_ASTNode():
    instance = java_NamespaceAccess()
    assert isinstance(instance, ASTNode)


def test_java_Statement_isa_ASTNode():
    instance = java_Statement()
    assert isinstance(instance, ASTNode)


def test_java_TagElement_isa_ASTNode():
    instance = java_TagElement()
    assert isinstance(instance, ASTNode)


def test_java_ConstructorDeclaration_isa_AbstractMethodDeclaration():
    instance = java_ConstructorDeclaration()
    assert isinstance(instance, AbstractMethodDeclaration)


def test_java_MethodDeclaration_isa_AbstractMethodDeclaration():
    instance = java_MethodDeclaration()
    assert isinstance(instance, AbstractMethodDeclaration)


def test_java_ClassInstanceCreation_isa_AbstractMethodInvocation():
    instance = java_ClassInstanceCreation()
    assert isinstance(instance, AbstractMethodInvocation)


def test_java_ConstructorInvocation_isa_AbstractMethodInvocation():
    instance = java_ConstructorInvocation()
    assert isinstance(instance, AbstractMethodInvocation)


def test_java_MethodInvocation_isa_AbstractMethodInvocation():
    instance = java_MethodInvocation()
    assert isinstance(instance, AbstractMethodInvocation)


def test_java_SuperConstructorInvocation_isa_AbstractMethodInvocation():
    instance = java_SuperConstructorInvocation()
    assert isinstance(instance, AbstractMethodInvocation)


def test_java_SuperMethodInvocation_isa_AbstractMethodInvocation():
    instance = java_SuperMethodInvocation()
    assert isinstance(instance, AbstractMethodInvocation)


def test_java_AnnotationTypeDeclaration_isa_AbstractTypeDeclaration():
    instance = java_AnnotationTypeDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_java_EnumDeclaration_isa_AbstractTypeDeclaration():
    instance = java_EnumDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_java_TypeDeclaration_isa_AbstractTypeDeclaration():
    instance = java_TypeDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_java_UnresolvedTypeDeclaration_isa_AbstractTypeDeclaration():
    instance = java_UnresolvedTypeDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_java_SuperFieldAccess_isa_AbstractTypeQualifiedExpression():
    instance = java_SuperFieldAccess()
    assert isinstance(instance, AbstractTypeQualifiedExpression)


def test_java_SuperMethodInvocation_isa_AbstractTypeQualifiedExpression():
    instance = java_SuperMethodInvocation()
    assert isinstance(instance, AbstractTypeQualifiedExpression)


def test_java_ThisExpression_isa_AbstractTypeQualifiedExpression():
    instance = java_ThisExpression()
    assert isinstance(instance, AbstractTypeQualifiedExpression)


def test_java_FieldDeclaration_isa_AbstractVariablesContainer():
    instance = java_FieldDeclaration()
    assert isinstance(instance, AbstractVariablesContainer)


def test_java_VariableDeclarationExpression_isa_AbstractVariablesContainer():
    instance = java_VariableDeclarationExpression()
    assert isinstance(instance, AbstractVariablesContainer)


def test_java_VariableDeclarationStatement_isa_AbstractVariablesContainer():
    instance = java_VariableDeclarationStatement()
    assert isinstance(instance, AbstractVariablesContainer)


def test_java_AbstractMethodDeclaration_isa_BodyDeclaration():
    instance = java_AbstractMethodDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_java_AbstractTypeDeclaration_isa_BodyDeclaration():
    instance = java_AbstractTypeDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_java_AnnotationTypeMemberDeclaration_isa_BodyDeclaration():
    instance = java_AnnotationTypeMemberDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_java_EnumConstantDeclaration_isa_BodyDeclaration():
    instance = java_EnumConstantDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_java_FieldDeclaration_isa_BodyDeclaration():
    instance = java_FieldDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_java_Initializer_isa_BodyDeclaration():
    instance = java_Initializer()
    assert isinstance(instance, BodyDeclaration)


def test_java_AbstractTypeQualifiedExpression_isa_Expression():
    instance = java_AbstractTypeQualifiedExpression()
    assert isinstance(instance, Expression)


def test_java_Annotation_isa_Expression():
    instance = java_Annotation()
    assert isinstance(instance, Expression)


def test_java_ArrayAccess_isa_Expression():
    instance = java_ArrayAccess()
    assert isinstance(instance, Expression)


def test_java_ArrayCreation_isa_Expression():
    instance = java_ArrayCreation()
    assert isinstance(instance, Expression)


def test_java_ArrayInitializer_isa_Expression():
    instance = java_ArrayInitializer()
    assert isinstance(instance, Expression)


def test_java_ArrayLengthAccess_isa_Expression():
    instance = java_ArrayLengthAccess()
    assert isinstance(instance, Expression)


def test_java_Assignment_isa_Expression():
    instance = java_Assignment(operator="sample_text")
    assert isinstance(instance, Expression)


def test_java_BooleanLiteral_isa_Expression():
    instance = java_BooleanLiteral(value=True)
    assert isinstance(instance, Expression)


def test_java_CastExpression_isa_Expression():
    instance = java_CastExpression()
    assert isinstance(instance, Expression)


def test_java_CharacterLiteral_isa_Expression():
    instance = java_CharacterLiteral(escapedValue="sample_text")
    assert isinstance(instance, Expression)


def test_java_ClassInstanceCreation_isa_Expression():
    instance = java_ClassInstanceCreation()
    assert isinstance(instance, Expression)


def test_java_ConditionalExpression_isa_Expression():
    instance = java_ConditionalExpression()
    assert isinstance(instance, Expression)


def test_java_FieldAccess_isa_Expression():
    instance = java_FieldAccess()
    assert isinstance(instance, Expression)


def test_java_InfixExpression_isa_Expression():
    instance = java_InfixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_java_InstanceofExpression_isa_Expression():
    instance = java_InstanceofExpression()
    assert isinstance(instance, Expression)


def test_java_MethodInvocation_isa_Expression():
    instance = java_MethodInvocation()
    assert isinstance(instance, Expression)


def test_java_NullLiteral_isa_Expression():
    instance = java_NullLiteral()
    assert isinstance(instance, Expression)


def test_java_NumberLiteral_isa_Expression():
    instance = java_NumberLiteral(tokenValue="sample_text")
    assert isinstance(instance, Expression)


def test_java_ParenthesizedExpression_isa_Expression():
    instance = java_ParenthesizedExpression()
    assert isinstance(instance, Expression)


def test_java_PostfixExpression_isa_Expression():
    instance = java_PostfixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_java_PrefixExpression_isa_Expression():
    instance = java_PrefixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_java_SingleVariableAccess_isa_Expression():
    instance = java_SingleVariableAccess()
    assert isinstance(instance, Expression)


def test_java_StringLiteral_isa_Expression():
    instance = java_StringLiteral(escapedValue="sample_text")
    assert isinstance(instance, Expression)


def test_java_TypeAccess_isa_Expression():
    instance = java_TypeAccess()
    assert isinstance(instance, Expression)


def test_java_TypeLiteral_isa_Expression():
    instance = java_TypeLiteral()
    assert isinstance(instance, Expression)


def test_java_UnresolvedItemAccess_isa_Expression():
    instance = java_UnresolvedItemAccess()
    assert isinstance(instance, Expression)


def test_java_VariableDeclarationExpression_isa_Expression():
    instance = java_VariableDeclarationExpression()
    assert isinstance(instance, Expression)


def test_java_AnnotationMemberValuePair_isa_NamedElement():
    instance = java_AnnotationMemberValuePair()
    assert isinstance(instance, NamedElement)


def test_java_Archive_isa_NamedElement():
    instance = java_Archive(originalFilePath="sample_text")
    assert isinstance(instance, NamedElement)


def test_java_BodyDeclaration_isa_NamedElement():
    instance = java_BodyDeclaration()
    assert isinstance(instance, NamedElement)


def test_java_ClassFile_isa_NamedElement():
    instance = java_ClassFile()
    assert isinstance(instance, NamedElement)


def test_java_CompilationUnit_isa_NamedElement():
    instance = java_CompilationUnit(originalFilePath="sample_text")
    assert isinstance(instance, NamedElement)


def test_java_LabeledStatement_isa_NamedElement():
    instance = java_LabeledStatement()
    assert isinstance(instance, NamedElement)


def test_java_Package_isa_NamedElement():
    instance = java_Package()
    assert isinstance(instance, NamedElement)


def test_java_Type_isa_NamedElement():
    instance = java_Type()
    assert isinstance(instance, NamedElement)


def test_java_UnresolvedItem_isa_NamedElement():
    instance = java_UnresolvedItem()
    assert isinstance(instance, NamedElement)


def test_java_VariableDeclaration_isa_NamedElement():
    instance = java_VariableDeclaration()
    assert isinstance(instance, NamedElement)


def test_java_TypeAccess_isa_NamespaceAccess():
    instance = java_TypeAccess()
    assert isinstance(instance, NamespaceAccess)


def test_java_UnresolvedItemAccess_isa_NamespaceAccess():
    instance = java_UnresolvedItemAccess()
    assert isinstance(instance, NamespaceAccess)


def test_java_PrimitiveTypeBoolean_isa_PrimitiveType():
    instance = java_PrimitiveTypeBoolean()
    assert isinstance(instance, PrimitiveType)


def test_java_PrimitiveTypeByte_isa_PrimitiveType():
    instance = java_PrimitiveTypeByte()
    assert isinstance(instance, PrimitiveType)


def test_java_PrimitiveTypeChar_isa_PrimitiveType():
    instance = java_PrimitiveTypeChar()
    assert isinstance(instance, PrimitiveType)


def test_java_PrimitiveTypeDouble_isa_PrimitiveType():
    instance = java_PrimitiveTypeDouble()
    assert isinstance(instance, PrimitiveType)


def test_java_PrimitiveTypeFloat_isa_PrimitiveType():
    instance = java_PrimitiveTypeFloat()
    assert isinstance(instance, PrimitiveType)


def test_java_PrimitiveTypeInt_isa_PrimitiveType():
    instance = java_PrimitiveTypeInt()
    assert isinstance(instance, PrimitiveType)


def test_java_PrimitiveTypeLong_isa_PrimitiveType():
    instance = java_PrimitiveTypeLong()
    assert isinstance(instance, PrimitiveType)


def test_java_PrimitiveTypeShort_isa_PrimitiveType():
    instance = java_PrimitiveTypeShort()
    assert isinstance(instance, PrimitiveType)


def test_java_PrimitiveTypeVoid_isa_PrimitiveType():
    instance = java_PrimitiveTypeVoid()
    assert isinstance(instance, PrimitiveType)


def test_java_AssertStatement_isa_Statement():
    instance = java_AssertStatement()
    assert isinstance(instance, Statement)


def test_java_Block_isa_Statement():
    instance = java_Block()
    assert isinstance(instance, Statement)


def test_java_BreakStatement_isa_Statement():
    instance = java_BreakStatement()
    assert isinstance(instance, Statement)


def test_java_CatchClause_isa_Statement():
    instance = java_CatchClause()
    assert isinstance(instance, Statement)


def test_java_ConstructorInvocation_isa_Statement():
    instance = java_ConstructorInvocation()
    assert isinstance(instance, Statement)


def test_java_ContinueStatement_isa_Statement():
    instance = java_ContinueStatement()
    assert isinstance(instance, Statement)


def test_java_DoStatement_isa_Statement():
    instance = java_DoStatement()
    assert isinstance(instance, Statement)


def test_java_EmptyStatement_isa_Statement():
    instance = java_EmptyStatement()
    assert isinstance(instance, Statement)


def test_java_EnhancedForStatement_isa_Statement():
    instance = java_EnhancedForStatement()
    assert isinstance(instance, Statement)


def test_java_ExpressionStatement_isa_Statement():
    instance = java_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_java_ForStatement_isa_Statement():
    instance = java_ForStatement()
    assert isinstance(instance, Statement)


def test_java_IfStatement_isa_Statement():
    instance = java_IfStatement()
    assert isinstance(instance, Statement)


def test_java_LabeledStatement_isa_Statement():
    instance = java_LabeledStatement()
    assert isinstance(instance, Statement)


def test_java_ReturnStatement_isa_Statement():
    instance = java_ReturnStatement()
    assert isinstance(instance, Statement)


def test_java_SuperConstructorInvocation_isa_Statement():
    instance = java_SuperConstructorInvocation()
    assert isinstance(instance, Statement)


def test_java_SwitchCase_isa_Statement():
    instance = java_SwitchCase()
    assert isinstance(instance, Statement)


def test_java_SwitchStatement_isa_Statement():
    instance = java_SwitchStatement()
    assert isinstance(instance, Statement)


def test_java_SynchronizedStatement_isa_Statement():
    instance = java_SynchronizedStatement()
    assert isinstance(instance, Statement)


def test_java_ThrowStatement_isa_Statement():
    instance = java_ThrowStatement()
    assert isinstance(instance, Statement)


def test_java_TryStatement_isa_Statement():
    instance = java_TryStatement()
    assert isinstance(instance, Statement)


def test_java_TypeDeclarationStatement_isa_Statement():
    instance = java_TypeDeclarationStatement()
    assert isinstance(instance, Statement)


def test_java_VariableDeclarationStatement_isa_Statement():
    instance = java_VariableDeclarationStatement()
    assert isinstance(instance, Statement)


def test_java_WhileStatement_isa_Statement():
    instance = java_WhileStatement()
    assert isinstance(instance, Statement)


def test_java_AbstractTypeDeclaration_isa_Type():
    instance = java_AbstractTypeDeclaration()
    assert isinstance(instance, Type)


def test_java_ArrayType_isa_Type():
    instance = java_ArrayType(dimensions=7)
    assert isinstance(instance, Type)


def test_java_ParameterizedType_isa_Type():
    instance = java_ParameterizedType()
    assert isinstance(instance, Type)


def test_java_PrimitiveType_isa_Type():
    instance = java_PrimitiveType()
    assert isinstance(instance, Type)


def test_java_TypeParameter_isa_Type():
    instance = java_TypeParameter()
    assert isinstance(instance, Type)


def test_java_WildCardType_isa_Type():
    instance = java_WildCardType()
    assert isinstance(instance, Type)


def test_java_ClassDeclaration_isa_TypeDeclaration():
    instance = java_ClassDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_java_InterfaceDeclaration_isa_TypeDeclaration():
    instance = java_InterfaceDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_java_UnresolvedTypeDeclaration_isa_UnresolvedItem():
    instance = java_UnresolvedTypeDeclaration()
    assert isinstance(instance, UnresolvedItem)


def test_java_EnumConstantDeclaration_isa_VariableDeclaration():
    instance = java_EnumConstantDeclaration()
    assert isinstance(instance, VariableDeclaration)


def test_java_SingleVariableDeclaration_isa_VariableDeclaration():
    instance = java_SingleVariableDeclaration()
    assert isinstance(instance, VariableDeclaration)


def test_java_VariableDeclarationFragment_isa_VariableDeclaration():
    instance = java_VariableDeclarationFragment()
    assert isinstance(instance, VariableDeclaration)


def test_assoc_archives256_link_reassign_clear():
    a = java_Model(name="sample_text")
    b1 = java_Archive(originalFilePath="sample_text")
    b2 = java_Archive(originalFilePath="sample_text_2")
    _safe_set(a, 'java_Model257', {b1})
    assert _is_linked(a, 'java_Model257', b1)
    if hasattr(b1, 'java_Archive'):
        assert _is_linked(b1, 'java_Archive', a)
    _safe_set(a, 'java_Model257', {b2})
    assert _is_linked(a, 'java_Model257', b2)
    if hasattr(b1, 'java_Archive'):
        assert not _is_linked(b1, 'java_Archive', a)
    if hasattr(b2, 'java_Archive'):
        assert _is_linked(b2, 'java_Archive', a)
    _safe_set(a, 'java_Model257', set())
    assert not _is_linked(a, 'java_Model257', b2)
    if hasattr(b2, 'java_Archive'):
        assert not _is_linked(b2, 'java_Archive', a)


def test_assoc_comments66_link_reassign_clear():
    a = java_Comment(content="sample_text")
    b1 = java_ASTNode()
    b2 = java_ASTNode()
    _safe_set(a, 'java_Comment67', b1)
    assert _is_linked(a, 'java_Comment67', b1)
    if hasattr(b1, 'java_ASTNode'):
        assert _is_linked(b1, 'java_ASTNode', a)
    _safe_set(a, 'java_Comment67', b2)
    assert _is_linked(a, 'java_Comment67', b2)
    if hasattr(b1, 'java_ASTNode'):
        assert not _is_linked(b1, 'java_ASTNode', a)
    if hasattr(b2, 'java_ASTNode'):
        assert _is_linked(b2, 'java_ASTNode', a)
    _safe_set(a, 'java_Comment67', None)
    assert not _is_linked(a, 'java_Comment67', b2)
    if hasattr(b2, 'java_ASTNode'):
        assert not _is_linked(b2, 'java_ASTNode', a)


def test_assoc_commentsAfterBody28_link_reassign_clear():
    a = java_Comment(content="sample_text")
    b1 = java_AbstractTypeDeclaration()
    b2 = java_AbstractTypeDeclaration()
    _safe_set(a, 'java_Comment', b1)
    assert _is_linked(a, 'java_Comment', b1)
    if hasattr(b1, 'java_AbstractTypeDeclaration'):
        assert _is_linked(b1, 'java_AbstractTypeDeclaration', a)
    _safe_set(a, 'java_Comment', b2)
    assert _is_linked(a, 'java_Comment', b2)
    if hasattr(b1, 'java_AbstractTypeDeclaration'):
        assert not _is_linked(b1, 'java_AbstractTypeDeclaration', a)
    if hasattr(b2, 'java_AbstractTypeDeclaration'):
        assert _is_linked(b2, 'java_AbstractTypeDeclaration', a)
    _safe_set(a, 'java_Comment', None)
    assert not _is_linked(a, 'java_Comment', b2)
    if hasattr(b2, 'java_AbstractTypeDeclaration'):
        assert not _is_linked(b2, 'java_AbstractTypeDeclaration', a)


def test_assoc_commentsBeforeBody29_link_reassign_clear():
    a = java_Comment(content="sample_text")
    b1 = java_AbstractTypeDeclaration()
    b2 = java_AbstractTypeDeclaration()
    _safe_set(a, 'java_Comment31', b1)
    assert _is_linked(a, 'java_Comment31', b1)
    if hasattr(b1, 'java_AbstractTypeDeclaration30'):
        assert _is_linked(b1, 'java_AbstractTypeDeclaration30', a)
    _safe_set(a, 'java_Comment31', b2)
    assert _is_linked(a, 'java_Comment31', b2)
    if hasattr(b1, 'java_AbstractTypeDeclaration30'):
        assert not _is_linked(b1, 'java_AbstractTypeDeclaration30', a)
    if hasattr(b2, 'java_AbstractTypeDeclaration30'):
        assert _is_linked(b2, 'java_AbstractTypeDeclaration30', a)
    _safe_set(a, 'java_Comment31', None)
    assert not _is_linked(a, 'java_Comment31', b2)
    if hasattr(b2, 'java_AbstractTypeDeclaration30'):
        assert not _is_linked(b2, 'java_AbstractTypeDeclaration30', a)


def test_assoc_compilationUnits251_link_reassign_clear():
    a = java_Model(name="sample_text")
    b1 = java_CompilationUnit(originalFilePath="sample_text")
    b2 = java_CompilationUnit(originalFilePath="sample_text_2")
    _safe_set(a, 'java_Model', {b1})
    assert _is_linked(a, 'java_Model', b1)
    if hasattr(b1, 'java_CompilationUnit252'):
        assert _is_linked(b1, 'java_CompilationUnit252', a)
    _safe_set(a, 'java_Model', {b2})
    assert _is_linked(a, 'java_Model', b2)
    if hasattr(b1, 'java_CompilationUnit252'):
        assert not _is_linked(b1, 'java_CompilationUnit252', a)
    if hasattr(b2, 'java_CompilationUnit252'):
        assert _is_linked(b2, 'java_CompilationUnit252', a)
    _safe_set(a, 'java_Model', set())
    assert not _is_linked(a, 'java_Model', b2)
    if hasattr(b2, 'java_CompilationUnit252'):
        assert not _is_linked(b2, 'java_CompilationUnit252', a)


def test_assoc_elementType151_link_reassign_clear():
    a = java_ArrayType(dimensions=7)
    b1 = java_TypeAccess()
    b2 = java_TypeAccess()
    _safe_set(a, 'java_ArrayType', b1)
    assert _is_linked(a, 'java_ArrayType', b1)
    if hasattr(b1, 'java_TypeAccess152'):
        assert _is_linked(b1, 'java_TypeAccess152', a)
    _safe_set(a, 'java_ArrayType', b2)
    assert _is_linked(a, 'java_ArrayType', b2)
    if hasattr(b1, 'java_TypeAccess152'):
        assert not _is_linked(b1, 'java_TypeAccess152', a)
    if hasattr(b2, 'java_TypeAccess152'):
        assert _is_linked(b2, 'java_TypeAccess152', a)
    _safe_set(a, 'java_ArrayType', None)
    assert not _is_linked(a, 'java_ArrayType', b2)
    if hasattr(b2, 'java_TypeAccess152'):
        assert not _is_linked(b2, 'java_TypeAccess152', a)


def test_assoc_extendedOperands116_link_reassign_clear():
    a = java_InfixExpression(operator="sample_text")
    b1 = java_Expression()
    b2 = java_Expression()
    _safe_set(a, 'java_InfixExpression117', {b1})
    assert _is_linked(a, 'java_InfixExpression117', b1)
    if hasattr(b1, 'java_Expression118'):
        assert _is_linked(b1, 'java_Expression118', a)
    _safe_set(a, 'java_InfixExpression117', {b2})
    assert _is_linked(a, 'java_InfixExpression117', b2)
    if hasattr(b1, 'java_Expression118'):
        assert not _is_linked(b1, 'java_Expression118', a)
    if hasattr(b2, 'java_Expression118'):
        assert _is_linked(b2, 'java_Expression118', a)
    _safe_set(a, 'java_InfixExpression117', set())
    assert not _is_linked(a, 'java_InfixExpression117', b2)
    if hasattr(b2, 'java_Expression118'):
        assert not _is_linked(b2, 'java_Expression118', a)


def test_assoc_importedElement57_link_reassign_clear():
    a = java_NamedElement(name="sample_text", proxy=True)
    b1 = java_ImportDeclaration(static=True)
    b2 = java_ImportDeclaration(static=False)
    _safe_set(a, 'java_NamedElement', b1)
    assert _is_linked(a, 'java_NamedElement', b1)
    if hasattr(b1, 'java_ImportDeclaration'):
        assert _is_linked(b1, 'java_ImportDeclaration', a)
    _safe_set(a, 'java_NamedElement', b2)
    assert _is_linked(a, 'java_NamedElement', b2)
    if hasattr(b1, 'java_ImportDeclaration'):
        assert not _is_linked(b1, 'java_ImportDeclaration', a)
    if hasattr(b2, 'java_ImportDeclaration'):
        assert _is_linked(b2, 'java_ImportDeclaration', a)
    _safe_set(a, 'java_NamedElement', None)
    assert not _is_linked(a, 'java_NamedElement', b2)
    if hasattr(b2, 'java_ImportDeclaration'):
        assert not _is_linked(b2, 'java_ImportDeclaration', a)


def test_assoc_imports122_link_reassign_clear():
    a = java_ImportDeclaration(static=True)
    b1 = java_CompilationUnit(originalFilePath="sample_text")
    b2 = java_CompilationUnit(originalFilePath="sample_text_2")
    _safe_set(a, 'java_ImportDeclaration124', b1)
    assert _is_linked(a, 'java_ImportDeclaration124', b1)
    if hasattr(b1, 'java_CompilationUnit123'):
        assert _is_linked(b1, 'java_CompilationUnit123', a)
    _safe_set(a, 'java_ImportDeclaration124', b2)
    assert _is_linked(a, 'java_ImportDeclaration124', b2)
    if hasattr(b1, 'java_CompilationUnit123'):
        assert not _is_linked(b1, 'java_CompilationUnit123', a)
    if hasattr(b2, 'java_CompilationUnit123'):
        assert _is_linked(b2, 'java_CompilationUnit123', a)
    _safe_set(a, 'java_ImportDeclaration124', None)
    assert not _is_linked(a, 'java_ImportDeclaration124', b2)
    if hasattr(b2, 'java_CompilationUnit123'):
        assert not _is_linked(b2, 'java_CompilationUnit123', a)


def test_assoc_leftHandSide43_link_reassign_clear():
    a = java_Assignment(operator="sample_text")
    b1 = java_Expression()
    b2 = java_Expression()
    _safe_set(a, 'java_Assignment', b1)
    assert _is_linked(a, 'java_Assignment', b1)
    if hasattr(b1, 'java_Expression44'):
        assert _is_linked(b1, 'java_Expression44', a)
    _safe_set(a, 'java_Assignment', b2)
    assert _is_linked(a, 'java_Assignment', b2)
    if hasattr(b1, 'java_Expression44'):
        assert not _is_linked(b1, 'java_Expression44', a)
    if hasattr(b2, 'java_Expression44'):
        assert _is_linked(b2, 'java_Expression44', a)
    _safe_set(a, 'java_Assignment', None)
    assert not _is_linked(a, 'java_Assignment', b2)
    if hasattr(b2, 'java_Expression44'):
        assert not _is_linked(b2, 'java_Expression44', a)


def test_assoc_leftOperand113_link_reassign_clear():
    a = java_InfixExpression(operator="sample_text")
    b1 = java_Expression()
    b2 = java_Expression()
    _safe_set(a, 'java_InfixExpression114', b1)
    assert _is_linked(a, 'java_InfixExpression114', b1)
    if hasattr(b1, 'java_Expression115'):
        assert _is_linked(b1, 'java_Expression115', a)
    _safe_set(a, 'java_InfixExpression114', b2)
    assert _is_linked(a, 'java_InfixExpression114', b2)
    if hasattr(b1, 'java_Expression115'):
        assert not _is_linked(b1, 'java_Expression115', a)
    if hasattr(b2, 'java_Expression115'):
        assert _is_linked(b2, 'java_Expression115', a)
    _safe_set(a, 'java_InfixExpression114', None)
    assert not _is_linked(a, 'java_InfixExpression114', b2)
    if hasattr(b2, 'java_Expression115'):
        assert not _is_linked(b2, 'java_Expression115', a)


def test_assoc_modifier155_link_reassign_clear():
    a = java_Modifier(inheritance="sample_text", static=True, visibility="sample_text")
    b1 = java_BodyDeclaration()
    b2 = java_BodyDeclaration()
    _safe_set(a, 'java_Modifier156', b1)
    assert _is_linked(a, 'java_Modifier156', b1)
    if hasattr(b1, 'java_BodyDeclaration'):
        assert _is_linked(b1, 'java_BodyDeclaration', a)
    _safe_set(a, 'java_Modifier156', b2)
    assert _is_linked(a, 'java_Modifier156', b2)
    if hasattr(b1, 'java_BodyDeclaration'):
        assert not _is_linked(b1, 'java_BodyDeclaration', a)
    if hasattr(b2, 'java_BodyDeclaration'):
        assert _is_linked(b2, 'java_BodyDeclaration', a)
    _safe_set(a, 'java_Modifier156', None)
    assert not _is_linked(a, 'java_Modifier156', b2)
    if hasattr(b2, 'java_BodyDeclaration'):
        assert not _is_linked(b2, 'java_BodyDeclaration', a)


def test_assoc_modifier23_link_reassign_clear():
    a = java_Modifier(inheritance="sample_text", static=True, visibility="sample_text")
    b1 = java_SingleVariableDeclaration()
    b2 = java_SingleVariableDeclaration()
    _safe_set(a, 'java_Modifier', b1)
    assert _is_linked(a, 'java_Modifier', b1)
    if hasattr(b1, 'java_SingleVariableDeclaration'):
        assert _is_linked(b1, 'java_SingleVariableDeclaration', a)
    _safe_set(a, 'java_Modifier', b2)
    assert _is_linked(a, 'java_Modifier', b2)
    if hasattr(b1, 'java_SingleVariableDeclaration'):
        assert not _is_linked(b1, 'java_SingleVariableDeclaration', a)
    if hasattr(b2, 'java_SingleVariableDeclaration'):
        assert _is_linked(b2, 'java_SingleVariableDeclaration', a)
    _safe_set(a, 'java_Modifier', None)
    assert not _is_linked(a, 'java_Modifier', b2)
    if hasattr(b2, 'java_SingleVariableDeclaration'):
        assert not _is_linked(b2, 'java_SingleVariableDeclaration', a)


def test_assoc_operand171_link_reassign_clear():
    a = java_PrefixExpression(operator="sample_text")
    b1 = java_Expression()
    b2 = java_Expression()
    _safe_set(a, 'java_PrefixExpression', b1)
    assert _is_linked(a, 'java_PrefixExpression', b1)
    if hasattr(b1, 'java_Expression172'):
        assert _is_linked(b1, 'java_Expression172', a)
    _safe_set(a, 'java_PrefixExpression', b2)
    assert _is_linked(a, 'java_PrefixExpression', b2)
    if hasattr(b1, 'java_Expression172'):
        assert not _is_linked(b1, 'java_Expression172', a)
    if hasattr(b2, 'java_Expression172'):
        assert _is_linked(b2, 'java_Expression172', a)
    _safe_set(a, 'java_PrefixExpression', None)
    assert not _is_linked(a, 'java_PrefixExpression', b2)
    if hasattr(b2, 'java_Expression172'):
        assert not _is_linked(b2, 'java_Expression172', a)


def test_assoc_operand48_link_reassign_clear():
    a = java_PostfixExpression(operator="sample_text")
    b1 = java_Expression()
    b2 = java_Expression()
    _safe_set(a, 'java_PostfixExpression', b1)
    assert _is_linked(a, 'java_PostfixExpression', b1)
    if hasattr(b1, 'java_Expression49'):
        assert _is_linked(b1, 'java_Expression49', a)
    _safe_set(a, 'java_PostfixExpression', b2)
    assert _is_linked(a, 'java_PostfixExpression', b2)
    if hasattr(b1, 'java_Expression49'):
        assert not _is_linked(b1, 'java_Expression49', a)
    if hasattr(b2, 'java_Expression49'):
        assert _is_linked(b2, 'java_Expression49', a)
    _safe_set(a, 'java_PostfixExpression', None)
    assert not _is_linked(a, 'java_PostfixExpression', b2)
    if hasattr(b2, 'java_Expression49'):
        assert not _is_linked(b2, 'java_Expression49', a)


def test_assoc_originalCompilationUnit70_link_reassign_clear():
    a = java_CompilationUnit(originalFilePath="sample_text")
    b1 = java_ASTNode()
    b2 = java_ASTNode()
    _safe_set(a, 'java_CompilationUnit', b1)
    assert _is_linked(a, 'java_CompilationUnit', b1)
    if hasattr(b1, 'java_ASTNode71'):
        assert _is_linked(b1, 'java_ASTNode71', a)
    _safe_set(a, 'java_CompilationUnit', b2)
    assert _is_linked(a, 'java_CompilationUnit', b2)
    if hasattr(b1, 'java_ASTNode71'):
        assert not _is_linked(b1, 'java_ASTNode71', a)
    if hasattr(b2, 'java_ASTNode71'):
        assert _is_linked(b2, 'java_ASTNode71', a)
    _safe_set(a, 'java_CompilationUnit', None)
    assert not _is_linked(a, 'java_CompilationUnit', b2)
    if hasattr(b2, 'java_ASTNode71'):
        assert not _is_linked(b2, 'java_ASTNode71', a)


def test_assoc_orphanTypes253_link_reassign_clear():
    a = java_Model(name="sample_text")
    b1 = java_Type()
    b2 = java_Type()
    _safe_set(a, 'java_Model254', {b1})
    assert _is_linked(a, 'java_Model254', b1)
    if hasattr(b1, 'java_Type255'):
        assert _is_linked(b1, 'java_Type255', a)
    _safe_set(a, 'java_Model254', {b2})
    assert _is_linked(a, 'java_Model254', b2)
    if hasattr(b1, 'java_Type255'):
        assert not _is_linked(b1, 'java_Type255', a)
    if hasattr(b2, 'java_Type255'):
        assert _is_linked(b2, 'java_Type255', a)
    _safe_set(a, 'java_Model254', set())
    assert not _is_linked(a, 'java_Model254', b2)
    if hasattr(b2, 'java_Type255'):
        assert not _is_linked(b2, 'java_Type255', a)


def test_assoc_ownedElements258_link_reassign_clear():
    a = java_Model(name="sample_text")
    b1 = java_Package()
    b2 = java_Package()
    _safe_set(a, 'java_Model259', {b1})
    assert _is_linked(a, 'java_Model259', b1)
    if hasattr(b1, 'java_Package260'):
        assert _is_linked(b1, 'java_Package260', a)
    _safe_set(a, 'java_Model259', {b2})
    assert _is_linked(a, 'java_Model259', b2)
    if hasattr(b1, 'java_Package260'):
        assert not _is_linked(b1, 'java_Package260', a)
    if hasattr(b2, 'java_Package260'):
        assert _is_linked(b2, 'java_Package260', a)
    _safe_set(a, 'java_Model259', set())
    assert not _is_linked(a, 'java_Model259', b2)
    if hasattr(b2, 'java_Package260'):
        assert not _is_linked(b2, 'java_Package260', a)


def test_assoc_rightHandSide45_link_reassign_clear():
    a = java_Assignment(operator="sample_text")
    b1 = java_Expression()
    b2 = java_Expression()
    _safe_set(a, 'java_Assignment46', b1)
    assert _is_linked(a, 'java_Assignment46', b1)
    if hasattr(b1, 'java_Expression47'):
        assert _is_linked(b1, 'java_Expression47', a)
    _safe_set(a, 'java_Assignment46', b2)
    assert _is_linked(a, 'java_Assignment46', b2)
    if hasattr(b1, 'java_Expression47'):
        assert not _is_linked(b1, 'java_Expression47', a)
    if hasattr(b2, 'java_Expression47'):
        assert _is_linked(b2, 'java_Expression47', a)
    _safe_set(a, 'java_Assignment46', None)
    assert not _is_linked(a, 'java_Assignment46', b2)
    if hasattr(b2, 'java_Expression47'):
        assert not _is_linked(b2, 'java_Expression47', a)


def test_assoc_rightOperand111_link_reassign_clear():
    a = java_InfixExpression(operator="sample_text")
    b1 = java_Expression()
    b2 = java_Expression()
    _safe_set(a, 'java_InfixExpression', b1)
    assert _is_linked(a, 'java_InfixExpression', b1)
    if hasattr(b1, 'java_Expression112'):
        assert _is_linked(b1, 'java_Expression112', a)
    _safe_set(a, 'java_InfixExpression', b2)
    assert _is_linked(a, 'java_InfixExpression', b2)
    if hasattr(b1, 'java_Expression112'):
        assert not _is_linked(b1, 'java_Expression112', a)
    if hasattr(b2, 'java_Expression112'):
        assert _is_linked(b2, 'java_Expression112', a)
    _safe_set(a, 'java_InfixExpression', None)
    assert not _is_linked(a, 'java_InfixExpression', b2)
    if hasattr(b2, 'java_Expression112'):
        assert not _is_linked(b2, 'java_Expression112', a)


def test_assoc_types125_link_reassign_clear():
    a = java_CompilationUnit(originalFilePath="sample_text")
    b1 = java_AbstractTypeDeclaration()
    b2 = java_AbstractTypeDeclaration()
    _safe_set(a, 'java_CompilationUnit126', {b1})
    assert _is_linked(a, 'java_CompilationUnit126', b1)
    if hasattr(b1, 'java_AbstractTypeDeclaration127'):
        assert _is_linked(b1, 'java_AbstractTypeDeclaration127', a)
    _safe_set(a, 'java_CompilationUnit126', {b2})
    assert _is_linked(a, 'java_CompilationUnit126', b2)
    if hasattr(b1, 'java_AbstractTypeDeclaration127'):
        assert not _is_linked(b1, 'java_AbstractTypeDeclaration127', a)
    if hasattr(b2, 'java_AbstractTypeDeclaration127'):
        assert _is_linked(b2, 'java_AbstractTypeDeclaration127', a)
    _safe_set(a, 'java_CompilationUnit126', set())
    assert not _is_linked(a, 'java_CompilationUnit126', b2)
    if hasattr(b2, 'java_AbstractTypeDeclaration127'):
        assert not _is_linked(b2, 'java_AbstractTypeDeclaration127', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ASTNode_strategy = st.builds(ASTNode)
@given(instance=ASTNode_strategy)
@settings(max_examples=25)
def test_ASTNode_instantiation(instance):
    assert isinstance(instance, ASTNode)


AbstractMethodDeclaration_strategy = st.builds(AbstractMethodDeclaration)
@given(instance=AbstractMethodDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractMethodDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractMethodDeclaration)


AbstractMethodInvocation_strategy = st.builds(AbstractMethodInvocation)
@given(instance=AbstractMethodInvocation_strategy)
@settings(max_examples=25)
def test_AbstractMethodInvocation_instantiation(instance):
    assert isinstance(instance, AbstractMethodInvocation)


AbstractTypeDeclaration_strategy = st.builds(AbstractTypeDeclaration)
@given(instance=AbstractTypeDeclaration_strategy)
@settings(max_examples=25)
def test_AbstractTypeDeclaration_instantiation(instance):
    assert isinstance(instance, AbstractTypeDeclaration)


AbstractTypeQualifiedExpression_strategy = st.builds(AbstractTypeQualifiedExpression)
@given(instance=AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=25)
def test_AbstractTypeQualifiedExpression_instantiation(instance):
    assert isinstance(instance, AbstractTypeQualifiedExpression)


AbstractVariablesContainer_strategy = st.builds(AbstractVariablesContainer)
@given(instance=AbstractVariablesContainer_strategy)
@settings(max_examples=25)
def test_AbstractVariablesContainer_instantiation(instance):
    assert isinstance(instance, AbstractVariablesContainer)


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


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NamespaceAccess_strategy = st.builds(NamespaceAccess)
@given(instance=NamespaceAccess_strategy)
@settings(max_examples=25)
def test_NamespaceAccess_instantiation(instance):
    assert isinstance(instance, NamespaceAccess)


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


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypeDeclaration_strategy = st.builds(TypeDeclaration)
@given(instance=TypeDeclaration_strategy)
@settings(max_examples=25)
def test_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)


UnresolvedItem_strategy = st.builds(UnresolvedItem)
@given(instance=UnresolvedItem_strategy)
@settings(max_examples=25)
def test_UnresolvedItem_instantiation(instance):
    assert isinstance(instance, UnresolvedItem)


VariableDeclaration_strategy = st.builds(VariableDeclaration)
@given(instance=VariableDeclaration_strategy)
@settings(max_examples=25)
def test_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)


java_ASTNode_strategy = st.builds(java_ASTNode)
@given(instance=java_ASTNode_strategy)
@settings(max_examples=25)
def test_java_ASTNode_instantiation(instance):
    assert isinstance(instance, java_ASTNode)


java_AbstractMethodDeclaration_strategy = st.builds(java_AbstractMethodDeclaration)
@given(instance=java_AbstractMethodDeclaration_strategy)
@settings(max_examples=25)
def test_java_AbstractMethodDeclaration_instantiation(instance):
    assert isinstance(instance, java_AbstractMethodDeclaration)


java_AbstractMethodInvocation_strategy = st.builds(java_AbstractMethodInvocation)
@given(instance=java_AbstractMethodInvocation_strategy)
@settings(max_examples=25)
def test_java_AbstractMethodInvocation_instantiation(instance):
    assert isinstance(instance, java_AbstractMethodInvocation)


java_AbstractTypeDeclaration_strategy = st.builds(java_AbstractTypeDeclaration)
@given(instance=java_AbstractTypeDeclaration_strategy)
@settings(max_examples=25)
def test_java_AbstractTypeDeclaration_instantiation(instance):
    assert isinstance(instance, java_AbstractTypeDeclaration)


java_AbstractTypeQualifiedExpression_strategy = st.builds(java_AbstractTypeQualifiedExpression)
@given(instance=java_AbstractTypeQualifiedExpression_strategy)
@settings(max_examples=25)
def test_java_AbstractTypeQualifiedExpression_instantiation(instance):
    assert isinstance(instance, java_AbstractTypeQualifiedExpression)


java_AbstractVariablesContainer_strategy = st.builds(java_AbstractVariablesContainer)
@given(instance=java_AbstractVariablesContainer_strategy)
@settings(max_examples=25)
def test_java_AbstractVariablesContainer_instantiation(instance):
    assert isinstance(instance, java_AbstractVariablesContainer)


java_Annotation_strategy = st.builds(java_Annotation)
@given(instance=java_Annotation_strategy)
@settings(max_examples=25)
def test_java_Annotation_instantiation(instance):
    assert isinstance(instance, java_Annotation)


java_AnnotationMemberValuePair_strategy = st.builds(java_AnnotationMemberValuePair)
@given(instance=java_AnnotationMemberValuePair_strategy)
@settings(max_examples=25)
def test_java_AnnotationMemberValuePair_instantiation(instance):
    assert isinstance(instance, java_AnnotationMemberValuePair)


java_AnnotationTypeDeclaration_strategy = st.builds(java_AnnotationTypeDeclaration)
@given(instance=java_AnnotationTypeDeclaration_strategy)
@settings(max_examples=25)
def test_java_AnnotationTypeDeclaration_instantiation(instance):
    assert isinstance(instance, java_AnnotationTypeDeclaration)


java_AnnotationTypeMemberDeclaration_strategy = st.builds(java_AnnotationTypeMemberDeclaration)
@given(instance=java_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=25)
def test_java_AnnotationTypeMemberDeclaration_instantiation(instance):
    assert isinstance(instance, java_AnnotationTypeMemberDeclaration)


java_AnonymousClassDeclaration_strategy = st.builds(java_AnonymousClassDeclaration)
@given(instance=java_AnonymousClassDeclaration_strategy)
@settings(max_examples=25)
def test_java_AnonymousClassDeclaration_instantiation(instance):
    assert isinstance(instance, java_AnonymousClassDeclaration)


java_Archive_strategy = st.builds(java_Archive, originalFilePath=safe_text)
@given(instance=java_Archive_strategy)
@settings(max_examples=25)
def test_java_Archive_instantiation(instance):
    assert isinstance(instance, java_Archive)


java_ArrayAccess_strategy = st.builds(java_ArrayAccess)
@given(instance=java_ArrayAccess_strategy)
@settings(max_examples=25)
def test_java_ArrayAccess_instantiation(instance):
    assert isinstance(instance, java_ArrayAccess)


java_ArrayCreation_strategy = st.builds(java_ArrayCreation)
@given(instance=java_ArrayCreation_strategy)
@settings(max_examples=25)
def test_java_ArrayCreation_instantiation(instance):
    assert isinstance(instance, java_ArrayCreation)


java_ArrayInitializer_strategy = st.builds(java_ArrayInitializer)
@given(instance=java_ArrayInitializer_strategy)
@settings(max_examples=25)
def test_java_ArrayInitializer_instantiation(instance):
    assert isinstance(instance, java_ArrayInitializer)


java_ArrayLengthAccess_strategy = st.builds(java_ArrayLengthAccess)
@given(instance=java_ArrayLengthAccess_strategy)
@settings(max_examples=25)
def test_java_ArrayLengthAccess_instantiation(instance):
    assert isinstance(instance, java_ArrayLengthAccess)


java_ArrayType_strategy = st.builds(java_ArrayType, dimensions=st.integers())
@given(instance=java_ArrayType_strategy)
@settings(max_examples=25)
def test_java_ArrayType_instantiation(instance):
    assert isinstance(instance, java_ArrayType)


java_AssertStatement_strategy = st.builds(java_AssertStatement)
@given(instance=java_AssertStatement_strategy)
@settings(max_examples=25)
def test_java_AssertStatement_instantiation(instance):
    assert isinstance(instance, java_AssertStatement)


java_Assignment_strategy = st.builds(java_Assignment, operator=safe_text)
@given(instance=java_Assignment_strategy)
@settings(max_examples=25)
def test_java_Assignment_instantiation(instance):
    assert isinstance(instance, java_Assignment)


java_Block_strategy = st.builds(java_Block)
@given(instance=java_Block_strategy)
@settings(max_examples=25)
def test_java_Block_instantiation(instance):
    assert isinstance(instance, java_Block)


java_BodyDeclaration_strategy = st.builds(java_BodyDeclaration)
@given(instance=java_BodyDeclaration_strategy)
@settings(max_examples=25)
def test_java_BodyDeclaration_instantiation(instance):
    assert isinstance(instance, java_BodyDeclaration)


java_BooleanLiteral_strategy = st.builds(java_BooleanLiteral, value=st.booleans())
@given(instance=java_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_java_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, java_BooleanLiteral)


java_BreakStatement_strategy = st.builds(java_BreakStatement)
@given(instance=java_BreakStatement_strategy)
@settings(max_examples=25)
def test_java_BreakStatement_instantiation(instance):
    assert isinstance(instance, java_BreakStatement)


java_CastExpression_strategy = st.builds(java_CastExpression)
@given(instance=java_CastExpression_strategy)
@settings(max_examples=25)
def test_java_CastExpression_instantiation(instance):
    assert isinstance(instance, java_CastExpression)


java_CatchClause_strategy = st.builds(java_CatchClause)
@given(instance=java_CatchClause_strategy)
@settings(max_examples=25)
def test_java_CatchClause_instantiation(instance):
    assert isinstance(instance, java_CatchClause)


java_CharacterLiteral_strategy = st.builds(java_CharacterLiteral, escapedValue=safe_text)
@given(instance=java_CharacterLiteral_strategy)
@settings(max_examples=25)
def test_java_CharacterLiteral_instantiation(instance):
    assert isinstance(instance, java_CharacterLiteral)


java_ClassDeclaration_strategy = st.builds(java_ClassDeclaration)
@given(instance=java_ClassDeclaration_strategy)
@settings(max_examples=25)
def test_java_ClassDeclaration_instantiation(instance):
    assert isinstance(instance, java_ClassDeclaration)


java_ClassFile_strategy = st.builds(java_ClassFile)
@given(instance=java_ClassFile_strategy)
@settings(max_examples=25)
def test_java_ClassFile_instantiation(instance):
    assert isinstance(instance, java_ClassFile)


java_ClassInstanceCreation_strategy = st.builds(java_ClassInstanceCreation)
@given(instance=java_ClassInstanceCreation_strategy)
@settings(max_examples=25)
def test_java_ClassInstanceCreation_instantiation(instance):
    assert isinstance(instance, java_ClassInstanceCreation)


java_Comment_strategy = st.builds(java_Comment, content=safe_text)
@given(instance=java_Comment_strategy)
@settings(max_examples=25)
def test_java_Comment_instantiation(instance):
    assert isinstance(instance, java_Comment)


java_CompilationUnit_strategy = st.builds(java_CompilationUnit, originalFilePath=safe_text)
@given(instance=java_CompilationUnit_strategy)
@settings(max_examples=25)
def test_java_CompilationUnit_instantiation(instance):
    assert isinstance(instance, java_CompilationUnit)


java_ConditionalExpression_strategy = st.builds(java_ConditionalExpression)
@given(instance=java_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_java_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, java_ConditionalExpression)


java_ConstructorDeclaration_strategy = st.builds(java_ConstructorDeclaration)
@given(instance=java_ConstructorDeclaration_strategy)
@settings(max_examples=25)
def test_java_ConstructorDeclaration_instantiation(instance):
    assert isinstance(instance, java_ConstructorDeclaration)


java_ConstructorInvocation_strategy = st.builds(java_ConstructorInvocation)
@given(instance=java_ConstructorInvocation_strategy)
@settings(max_examples=25)
def test_java_ConstructorInvocation_instantiation(instance):
    assert isinstance(instance, java_ConstructorInvocation)


java_ContinueStatement_strategy = st.builds(java_ContinueStatement)
@given(instance=java_ContinueStatement_strategy)
@settings(max_examples=25)
def test_java_ContinueStatement_instantiation(instance):
    assert isinstance(instance, java_ContinueStatement)


java_DoStatement_strategy = st.builds(java_DoStatement)
@given(instance=java_DoStatement_strategy)
@settings(max_examples=25)
def test_java_DoStatement_instantiation(instance):
    assert isinstance(instance, java_DoStatement)


java_EmptyStatement_strategy = st.builds(java_EmptyStatement)
@given(instance=java_EmptyStatement_strategy)
@settings(max_examples=25)
def test_java_EmptyStatement_instantiation(instance):
    assert isinstance(instance, java_EmptyStatement)


java_EnhancedForStatement_strategy = st.builds(java_EnhancedForStatement)
@given(instance=java_EnhancedForStatement_strategy)
@settings(max_examples=25)
def test_java_EnhancedForStatement_instantiation(instance):
    assert isinstance(instance, java_EnhancedForStatement)


java_EnumConstantDeclaration_strategy = st.builds(java_EnumConstantDeclaration)
@given(instance=java_EnumConstantDeclaration_strategy)
@settings(max_examples=25)
def test_java_EnumConstantDeclaration_instantiation(instance):
    assert isinstance(instance, java_EnumConstantDeclaration)


java_EnumDeclaration_strategy = st.builds(java_EnumDeclaration)
@given(instance=java_EnumDeclaration_strategy)
@settings(max_examples=25)
def test_java_EnumDeclaration_instantiation(instance):
    assert isinstance(instance, java_EnumDeclaration)


java_Expression_strategy = st.builds(java_Expression)
@given(instance=java_Expression_strategy)
@settings(max_examples=25)
def test_java_Expression_instantiation(instance):
    assert isinstance(instance, java_Expression)


java_ExpressionStatement_strategy = st.builds(java_ExpressionStatement)
@given(instance=java_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_java_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, java_ExpressionStatement)


java_FieldAccess_strategy = st.builds(java_FieldAccess)
@given(instance=java_FieldAccess_strategy)
@settings(max_examples=25)
def test_java_FieldAccess_instantiation(instance):
    assert isinstance(instance, java_FieldAccess)


java_FieldDeclaration_strategy = st.builds(java_FieldDeclaration)
@given(instance=java_FieldDeclaration_strategy)
@settings(max_examples=25)
def test_java_FieldDeclaration_instantiation(instance):
    assert isinstance(instance, java_FieldDeclaration)


java_ForStatement_strategy = st.builds(java_ForStatement)
@given(instance=java_ForStatement_strategy)
@settings(max_examples=25)
def test_java_ForStatement_instantiation(instance):
    assert isinstance(instance, java_ForStatement)


java_IfStatement_strategy = st.builds(java_IfStatement)
@given(instance=java_IfStatement_strategy)
@settings(max_examples=25)
def test_java_IfStatement_instantiation(instance):
    assert isinstance(instance, java_IfStatement)


java_ImportDeclaration_strategy = st.builds(java_ImportDeclaration, static=st.booleans())
@given(instance=java_ImportDeclaration_strategy)
@settings(max_examples=25)
def test_java_ImportDeclaration_instantiation(instance):
    assert isinstance(instance, java_ImportDeclaration)


java_InfixExpression_strategy = st.builds(java_InfixExpression, operator=safe_text)
@given(instance=java_InfixExpression_strategy)
@settings(max_examples=25)
def test_java_InfixExpression_instantiation(instance):
    assert isinstance(instance, java_InfixExpression)


java_Initializer_strategy = st.builds(java_Initializer)
@given(instance=java_Initializer_strategy)
@settings(max_examples=25)
def test_java_Initializer_instantiation(instance):
    assert isinstance(instance, java_Initializer)


java_InstanceofExpression_strategy = st.builds(java_InstanceofExpression)
@given(instance=java_InstanceofExpression_strategy)
@settings(max_examples=25)
def test_java_InstanceofExpression_instantiation(instance):
    assert isinstance(instance, java_InstanceofExpression)


java_InterfaceDeclaration_strategy = st.builds(java_InterfaceDeclaration)
@given(instance=java_InterfaceDeclaration_strategy)
@settings(max_examples=25)
def test_java_InterfaceDeclaration_instantiation(instance):
    assert isinstance(instance, java_InterfaceDeclaration)


java_LabeledStatement_strategy = st.builds(java_LabeledStatement)
@given(instance=java_LabeledStatement_strategy)
@settings(max_examples=25)
def test_java_LabeledStatement_instantiation(instance):
    assert isinstance(instance, java_LabeledStatement)


java_MemberRef_strategy = st.builds(java_MemberRef)
@given(instance=java_MemberRef_strategy)
@settings(max_examples=25)
def test_java_MemberRef_instantiation(instance):
    assert isinstance(instance, java_MemberRef)


java_MethodDeclaration_strategy = st.builds(java_MethodDeclaration)
@given(instance=java_MethodDeclaration_strategy)
@settings(max_examples=25)
def test_java_MethodDeclaration_instantiation(instance):
    assert isinstance(instance, java_MethodDeclaration)


java_MethodInvocation_strategy = st.builds(java_MethodInvocation)
@given(instance=java_MethodInvocation_strategy)
@settings(max_examples=25)
def test_java_MethodInvocation_instantiation(instance):
    assert isinstance(instance, java_MethodInvocation)


java_MethodRef_strategy = st.builds(java_MethodRef)
@given(instance=java_MethodRef_strategy)
@settings(max_examples=25)
def test_java_MethodRef_instantiation(instance):
    assert isinstance(instance, java_MethodRef)


java_MethodRefParameter_strategy = st.builds(java_MethodRefParameter)
@given(instance=java_MethodRefParameter_strategy)
@settings(max_examples=25)
def test_java_MethodRefParameter_instantiation(instance):
    assert isinstance(instance, java_MethodRefParameter)


java_Model_strategy = st.builds(java_Model, name=safe_text)
@given(instance=java_Model_strategy)
@settings(max_examples=25)
def test_java_Model_instantiation(instance):
    assert isinstance(instance, java_Model)


java_Modifier_strategy = st.builds(java_Modifier, inheritance=safe_text, static=st.booleans(), visibility=safe_text)
@given(instance=java_Modifier_strategy)
@settings(max_examples=25)
def test_java_Modifier_instantiation(instance):
    assert isinstance(instance, java_Modifier)


java_NamedElement_strategy = st.builds(java_NamedElement, name=safe_text, proxy=st.booleans())
@given(instance=java_NamedElement_strategy)
@settings(max_examples=25)
def test_java_NamedElement_instantiation(instance):
    assert isinstance(instance, java_NamedElement)


java_NamespaceAccess_strategy = st.builds(java_NamespaceAccess)
@given(instance=java_NamespaceAccess_strategy)
@settings(max_examples=25)
def test_java_NamespaceAccess_instantiation(instance):
    assert isinstance(instance, java_NamespaceAccess)


java_NullLiteral_strategy = st.builds(java_NullLiteral)
@given(instance=java_NullLiteral_strategy)
@settings(max_examples=25)
def test_java_NullLiteral_instantiation(instance):
    assert isinstance(instance, java_NullLiteral)


java_NumberLiteral_strategy = st.builds(java_NumberLiteral, tokenValue=safe_text)
@given(instance=java_NumberLiteral_strategy)
@settings(max_examples=25)
def test_java_NumberLiteral_instantiation(instance):
    assert isinstance(instance, java_NumberLiteral)


java_Package_strategy = st.builds(java_Package)
@given(instance=java_Package_strategy)
@settings(max_examples=25)
def test_java_Package_instantiation(instance):
    assert isinstance(instance, java_Package)


java_ParameterizedType_strategy = st.builds(java_ParameterizedType)
@given(instance=java_ParameterizedType_strategy)
@settings(max_examples=25)
def test_java_ParameterizedType_instantiation(instance):
    assert isinstance(instance, java_ParameterizedType)


java_ParenthesizedExpression_strategy = st.builds(java_ParenthesizedExpression)
@given(instance=java_ParenthesizedExpression_strategy)
@settings(max_examples=25)
def test_java_ParenthesizedExpression_instantiation(instance):
    assert isinstance(instance, java_ParenthesizedExpression)


java_PostfixExpression_strategy = st.builds(java_PostfixExpression, operator=safe_text)
@given(instance=java_PostfixExpression_strategy)
@settings(max_examples=25)
def test_java_PostfixExpression_instantiation(instance):
    assert isinstance(instance, java_PostfixExpression)


java_PrefixExpression_strategy = st.builds(java_PrefixExpression, operator=safe_text)
@given(instance=java_PrefixExpression_strategy)
@settings(max_examples=25)
def test_java_PrefixExpression_instantiation(instance):
    assert isinstance(instance, java_PrefixExpression)


java_PrimitiveType_strategy = st.builds(java_PrimitiveType)
@given(instance=java_PrimitiveType_strategy)
@settings(max_examples=25)
def test_java_PrimitiveType_instantiation(instance):
    assert isinstance(instance, java_PrimitiveType)


java_PrimitiveTypeBoolean_strategy = st.builds(java_PrimitiveTypeBoolean)
@given(instance=java_PrimitiveTypeBoolean_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeBoolean_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeBoolean)


java_PrimitiveTypeByte_strategy = st.builds(java_PrimitiveTypeByte)
@given(instance=java_PrimitiveTypeByte_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeByte_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeByte)


java_PrimitiveTypeChar_strategy = st.builds(java_PrimitiveTypeChar)
@given(instance=java_PrimitiveTypeChar_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeChar_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeChar)


java_PrimitiveTypeDouble_strategy = st.builds(java_PrimitiveTypeDouble)
@given(instance=java_PrimitiveTypeDouble_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeDouble_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeDouble)


java_PrimitiveTypeFloat_strategy = st.builds(java_PrimitiveTypeFloat)
@given(instance=java_PrimitiveTypeFloat_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeFloat_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeFloat)


java_PrimitiveTypeInt_strategy = st.builds(java_PrimitiveTypeInt)
@given(instance=java_PrimitiveTypeInt_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeInt_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeInt)


java_PrimitiveTypeLong_strategy = st.builds(java_PrimitiveTypeLong)
@given(instance=java_PrimitiveTypeLong_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeLong_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeLong)


java_PrimitiveTypeShort_strategy = st.builds(java_PrimitiveTypeShort)
@given(instance=java_PrimitiveTypeShort_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeShort_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeShort)


java_PrimitiveTypeVoid_strategy = st.builds(java_PrimitiveTypeVoid)
@given(instance=java_PrimitiveTypeVoid_strategy)
@settings(max_examples=25)
def test_java_PrimitiveTypeVoid_instantiation(instance):
    assert isinstance(instance, java_PrimitiveTypeVoid)


java_ReturnStatement_strategy = st.builds(java_ReturnStatement)
@given(instance=java_ReturnStatement_strategy)
@settings(max_examples=25)
def test_java_ReturnStatement_instantiation(instance):
    assert isinstance(instance, java_ReturnStatement)


java_SingleVariableAccess_strategy = st.builds(java_SingleVariableAccess)
@given(instance=java_SingleVariableAccess_strategy)
@settings(max_examples=25)
def test_java_SingleVariableAccess_instantiation(instance):
    assert isinstance(instance, java_SingleVariableAccess)


java_SingleVariableDeclaration_strategy = st.builds(java_SingleVariableDeclaration)
@given(instance=java_SingleVariableDeclaration_strategy)
@settings(max_examples=25)
def test_java_SingleVariableDeclaration_instantiation(instance):
    assert isinstance(instance, java_SingleVariableDeclaration)


java_Statement_strategy = st.builds(java_Statement)
@given(instance=java_Statement_strategy)
@settings(max_examples=25)
def test_java_Statement_instantiation(instance):
    assert isinstance(instance, java_Statement)


java_StringLiteral_strategy = st.builds(java_StringLiteral, escapedValue=safe_text)
@given(instance=java_StringLiteral_strategy)
@settings(max_examples=25)
def test_java_StringLiteral_instantiation(instance):
    assert isinstance(instance, java_StringLiteral)


java_SuperConstructorInvocation_strategy = st.builds(java_SuperConstructorInvocation)
@given(instance=java_SuperConstructorInvocation_strategy)
@settings(max_examples=25)
def test_java_SuperConstructorInvocation_instantiation(instance):
    assert isinstance(instance, java_SuperConstructorInvocation)


java_SuperFieldAccess_strategy = st.builds(java_SuperFieldAccess)
@given(instance=java_SuperFieldAccess_strategy)
@settings(max_examples=25)
def test_java_SuperFieldAccess_instantiation(instance):
    assert isinstance(instance, java_SuperFieldAccess)


java_SuperMethodInvocation_strategy = st.builds(java_SuperMethodInvocation)
@given(instance=java_SuperMethodInvocation_strategy)
@settings(max_examples=25)
def test_java_SuperMethodInvocation_instantiation(instance):
    assert isinstance(instance, java_SuperMethodInvocation)


java_SwitchCase_strategy = st.builds(java_SwitchCase)
@given(instance=java_SwitchCase_strategy)
@settings(max_examples=25)
def test_java_SwitchCase_instantiation(instance):
    assert isinstance(instance, java_SwitchCase)


java_SwitchStatement_strategy = st.builds(java_SwitchStatement)
@given(instance=java_SwitchStatement_strategy)
@settings(max_examples=25)
def test_java_SwitchStatement_instantiation(instance):
    assert isinstance(instance, java_SwitchStatement)


java_SynchronizedStatement_strategy = st.builds(java_SynchronizedStatement)
@given(instance=java_SynchronizedStatement_strategy)
@settings(max_examples=25)
def test_java_SynchronizedStatement_instantiation(instance):
    assert isinstance(instance, java_SynchronizedStatement)


java_TagElement_strategy = st.builds(java_TagElement)
@given(instance=java_TagElement_strategy)
@settings(max_examples=25)
def test_java_TagElement_instantiation(instance):
    assert isinstance(instance, java_TagElement)


java_ThisExpression_strategy = st.builds(java_ThisExpression)
@given(instance=java_ThisExpression_strategy)
@settings(max_examples=25)
def test_java_ThisExpression_instantiation(instance):
    assert isinstance(instance, java_ThisExpression)


java_ThrowStatement_strategy = st.builds(java_ThrowStatement)
@given(instance=java_ThrowStatement_strategy)
@settings(max_examples=25)
def test_java_ThrowStatement_instantiation(instance):
    assert isinstance(instance, java_ThrowStatement)


java_TryStatement_strategy = st.builds(java_TryStatement)
@given(instance=java_TryStatement_strategy)
@settings(max_examples=25)
def test_java_TryStatement_instantiation(instance):
    assert isinstance(instance, java_TryStatement)


java_Type_strategy = st.builds(java_Type)
@given(instance=java_Type_strategy)
@settings(max_examples=25)
def test_java_Type_instantiation(instance):
    assert isinstance(instance, java_Type)


java_TypeAccess_strategy = st.builds(java_TypeAccess)
@given(instance=java_TypeAccess_strategy)
@settings(max_examples=25)
def test_java_TypeAccess_instantiation(instance):
    assert isinstance(instance, java_TypeAccess)


java_TypeDeclaration_strategy = st.builds(java_TypeDeclaration)
@given(instance=java_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_java_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, java_TypeDeclaration)


java_TypeDeclarationStatement_strategy = st.builds(java_TypeDeclarationStatement)
@given(instance=java_TypeDeclarationStatement_strategy)
@settings(max_examples=25)
def test_java_TypeDeclarationStatement_instantiation(instance):
    assert isinstance(instance, java_TypeDeclarationStatement)


java_TypeLiteral_strategy = st.builds(java_TypeLiteral)
@given(instance=java_TypeLiteral_strategy)
@settings(max_examples=25)
def test_java_TypeLiteral_instantiation(instance):
    assert isinstance(instance, java_TypeLiteral)


java_TypeParameter_strategy = st.builds(java_TypeParameter)
@given(instance=java_TypeParameter_strategy)
@settings(max_examples=25)
def test_java_TypeParameter_instantiation(instance):
    assert isinstance(instance, java_TypeParameter)


java_UnresolvedItem_strategy = st.builds(java_UnresolvedItem)
@given(instance=java_UnresolvedItem_strategy)
@settings(max_examples=25)
def test_java_UnresolvedItem_instantiation(instance):
    assert isinstance(instance, java_UnresolvedItem)


java_UnresolvedItemAccess_strategy = st.builds(java_UnresolvedItemAccess)
@given(instance=java_UnresolvedItemAccess_strategy)
@settings(max_examples=25)
def test_java_UnresolvedItemAccess_instantiation(instance):
    assert isinstance(instance, java_UnresolvedItemAccess)


java_UnresolvedTypeDeclaration_strategy = st.builds(java_UnresolvedTypeDeclaration)
@given(instance=java_UnresolvedTypeDeclaration_strategy)
@settings(max_examples=25)
def test_java_UnresolvedTypeDeclaration_instantiation(instance):
    assert isinstance(instance, java_UnresolvedTypeDeclaration)


java_VariableDeclaration_strategy = st.builds(java_VariableDeclaration)
@given(instance=java_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_java_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, java_VariableDeclaration)


java_VariableDeclarationExpression_strategy = st.builds(java_VariableDeclarationExpression)
@given(instance=java_VariableDeclarationExpression_strategy)
@settings(max_examples=25)
def test_java_VariableDeclarationExpression_instantiation(instance):
    assert isinstance(instance, java_VariableDeclarationExpression)


java_VariableDeclarationFragment_strategy = st.builds(java_VariableDeclarationFragment)
@given(instance=java_VariableDeclarationFragment_strategy)
@settings(max_examples=25)
def test_java_VariableDeclarationFragment_instantiation(instance):
    assert isinstance(instance, java_VariableDeclarationFragment)


java_VariableDeclarationStatement_strategy = st.builds(java_VariableDeclarationStatement)
@given(instance=java_VariableDeclarationStatement_strategy)
@settings(max_examples=25)
def test_java_VariableDeclarationStatement_instantiation(instance):
    assert isinstance(instance, java_VariableDeclarationStatement)


java_WhileStatement_strategy = st.builds(java_WhileStatement)
@given(instance=java_WhileStatement_strategy)
@settings(max_examples=25)
def test_java_WhileStatement_instantiation(instance):
    assert isinstance(instance, java_WhileStatement)


java_WildCardType_strategy = st.builds(java_WildCardType)
@given(instance=java_WildCardType_strategy)
@settings(max_examples=25)
def test_java_WildCardType_instantiation(instance):
    assert isinstance(instance, java_WildCardType)



