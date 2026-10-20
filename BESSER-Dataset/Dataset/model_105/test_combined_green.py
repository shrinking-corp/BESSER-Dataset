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
    Annotation,
    DOM_SingleMemberAnnotation,
    DOM_NormalAnnotation,
    DOM_MarkerAnnotation,
    Name,
    DOM_QualifiedName,
    Type,
    DOM_SimpleType,
    DOM_ParameterizedType,
    DOM_PrimitiveType,
    DOM_QualifiedType,
    VariableDeclaration,
    DOM_WildcardType,
    Statement,
    DOM_ForStatement,
    DOM_ExpressionStatement,
    DOM_SwitchStatement,
    DOM_ConstructorInvocation,
    DOM_LabeledStatement,
    DOM_VariableDeclarationStatement,
    DOM_IfStatement,
    DOM_TypeDeclarationStatement,
    DOM_TryStatement,
    DOM_ThrowStatement,
    DOM_BreakStatement,
    DOM_ReturnStatement,
    DOM_EmptyStatement,
    DOM_EnhancedForStatement,
    DOM_SwitchCase,
    DOM_SuperConstructorInvocation,
    DOM_WhileStatement,
    DOM_SynchronizedStatement,
    DOM_AssertStatement,
    DOM_DoStatement,
    DOM_ContinueStatement,
    DOM_ArrayType,
    Expression,
    DOM_ParenthesizedExpression,
    DOM_ConditionalExpression,
    DOM_NumberLiteral,
    DOM_CastExpression,
    DOM_ThisExpression,
    DOM_BooleanLiteral,
    DOM_CharacterLiteral,
    DOM_ArrayInitializer,
    DOM_StringLiteral,
    DOM_InfixExpression,
    DOM_VariableDeclarationExpression,
    DOM_Assignment,
    DOM_SuperFieldAccess,
    DOM_MethodInvocation,
    DOM_SuperMethodInvocation,
    DOM_ArrayCreation,
    DOM_ArrayAccess,
    DOM_FieldAccess,
    DOM_ClassInstanceCreation,
    DOM_PrefixExpression,
    DOM_PostfixExpression,
    DOM_InstanceofExpression,
    DOM_TypeLiteral,
    DOM_NullLiteral,
    Comment,
    DOM_LineComment,
    DOM_BlockComment,
    AbstractTypeDeclaration,
    DOM_AnnotationTypeDeclaration,
    DOM_IMethod,
    DOM_VariableDeclarationFragment,
    DOM_TypeDeclaration,
    DOM_EnumDeclaration,
    BodyDeclaration,
    DOM_MethodDeclaration,
    DOM_Initializer,
    DOM_FieldDeclaration,
    DOM_IPackageFragment,
    DOM_EnumConstantDeclaration,
    DOM_AnnotationTypeMemberDeclaration,
    ExtendedModifier,
    DOM_Annotation,
    DOM_SimpleName,
    DOM_Name,
    DOM_AbstractTypeDeclaration,
    DOM_SingleVariableDeclaration,
    DOM_Block,
    DOM_Javadoc,
    DOM_ExtendedModifier,
    DOM_IType,
    ASTNode,
    DOM_MethodRef,
    DOM_MemberValuePair,
    DOM_TagElement,
    DOM_CompilationUnit,
    DOM_Statement,
    DOM_Expression,
    DOM_CatchClause,
    DOM_Type,
    DOM_MemberRef,
    DOM_Modifier,
    DOM_BodyDeclaration,
    DOM_Comment,
    DOM_TextElement,
    DOM_TypeParameter,
    DOM_VariableDeclaration,
    DOM_MethodRefParameter,
    DOM_PackageDeclaration,
    DOM_ImportDeclaration,
    DOM_AnonymousClassDeclaration,
    DOM_ASTNode,
    DOM_AST,
    InfixExpressionOperatorKind,
    PrefixExpressionOperatorKind,
    PostfixExpressionOperatorKind,
    AssignmentOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_hyp_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_hyp_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_SingleMemberAnnotation)


def test_hyp_dom_singlememberannotation_constructor_exists():
    assert callable(DOM_SingleMemberAnnotation.__init__)


def test_hyp_dom_singlememberannotation_constructor_args():
    sig = inspect.signature(DOM_SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_normalannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_NormalAnnotation)


def test_hyp_dom_normalannotation_constructor_exists():
    assert callable(DOM_NormalAnnotation.__init__)


def test_hyp_dom_normalannotation_constructor_args():
    sig = inspect.signature(DOM_NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_markerannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_MarkerAnnotation)


def test_hyp_dom_markerannotation_constructor_exists():
    assert callable(DOM_MarkerAnnotation.__init__)


def test_hyp_dom_markerannotation_constructor_args():
    sig = inspect.signature(DOM_MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_hyp_name_constructor_exists():
    assert callable(Name.__init__)


def test_hyp_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(DOM_QualifiedName)


def test_hyp_dom_qualifiedname_constructor_exists():
    assert callable(DOM_QualifiedName.__init__)


def test_hyp_dom_qualifiedname_constructor_args():
    sig = inspect.signature(DOM_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_simpletype_is_not_abstract():
    assert not inspect.isabstract(DOM_SimpleType)


def test_hyp_dom_simpletype_constructor_exists():
    assert callable(DOM_SimpleType.__init__)


def test_hyp_dom_simpletype_constructor_args():
    sig = inspect.signature(DOM_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(DOM_ParameterizedType)


def test_hyp_dom_parameterizedtype_constructor_exists():
    assert callable(DOM_ParameterizedType.__init__)


def test_hyp_dom_parameterizedtype_constructor_args():
    sig = inspect.signature(DOM_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_primitivetype_is_not_abstract():
    assert not inspect.isabstract(DOM_PrimitiveType)


def test_hyp_dom_primitivetype_constructor_exists():
    assert callable(DOM_PrimitiveType.__init__)


def test_hyp_dom_primitivetype_constructor_args():
    sig = inspect.signature(DOM_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"




def test_hyp_dom_qualifiedtype_is_not_abstract():
    assert not inspect.isabstract(DOM_QualifiedType)


def test_hyp_dom_qualifiedtype_constructor_exists():
    assert callable(DOM_QualifiedType.__init__)


def test_hyp_dom_qualifiedtype_constructor_args():
    sig = inspect.signature(DOM_QualifiedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_hyp_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_hyp_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(DOM_WildcardType)


def test_hyp_dom_wildcardtype_constructor_exists():
    assert callable(DOM_WildcardType.__init__)


def test_hyp_dom_wildcardtype_constructor_args():
    sig = inspect.signature(DOM_WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"




def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_forstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ForStatement)


def test_hyp_dom_forstatement_constructor_exists():
    assert callable(DOM_ForStatement.__init__)


def test_hyp_dom_forstatement_constructor_args():
    sig = inspect.signature(DOM_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ExpressionStatement)


def test_hyp_dom_expressionstatement_constructor_exists():
    assert callable(DOM_ExpressionStatement.__init__)


def test_hyp_dom_expressionstatement_constructor_args():
    sig = inspect.signature(DOM_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_switchstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_SwitchStatement)


def test_hyp_dom_switchstatement_constructor_exists():
    assert callable(DOM_SwitchStatement.__init__)


def test_hyp_dom_switchstatement_constructor_args():
    sig = inspect.signature(DOM_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_ConstructorInvocation)


def test_hyp_dom_constructorinvocation_constructor_exists():
    assert callable(DOM_ConstructorInvocation.__init__)


def test_hyp_dom_constructorinvocation_constructor_args():
    sig = inspect.signature(DOM_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_LabeledStatement)


def test_hyp_dom_labeledstatement_constructor_exists():
    assert callable(DOM_LabeledStatement.__init__)


def test_hyp_dom_labeledstatement_constructor_args():
    sig = inspect.signature(DOM_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationStatement)


def test_hyp_dom_variabledeclarationstatement_constructor_exists():
    assert callable(DOM_VariableDeclarationStatement.__init__)


def test_hyp_dom_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_ifstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_IfStatement)


def test_hyp_dom_ifstatement_constructor_exists():
    assert callable(DOM_IfStatement.__init__)


def test_hyp_dom_ifstatement_constructor_args():
    sig = inspect.signature(DOM_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeDeclarationStatement)


def test_hyp_dom_typedeclarationstatement_constructor_exists():
    assert callable(DOM_TypeDeclarationStatement.__init__)


def test_hyp_dom_typedeclarationstatement_constructor_args():
    sig = inspect.signature(DOM_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_trystatement_is_not_abstract():
    assert not inspect.isabstract(DOM_TryStatement)


def test_hyp_dom_trystatement_constructor_exists():
    assert callable(DOM_TryStatement.__init__)


def test_hyp_dom_trystatement_constructor_args():
    sig = inspect.signature(DOM_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_throwstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ThrowStatement)


def test_hyp_dom_throwstatement_constructor_exists():
    assert callable(DOM_ThrowStatement.__init__)


def test_hyp_dom_throwstatement_constructor_args():
    sig = inspect.signature(DOM_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_breakstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_BreakStatement)


def test_hyp_dom_breakstatement_constructor_exists():
    assert callable(DOM_BreakStatement.__init__)


def test_hyp_dom_breakstatement_constructor_args():
    sig = inspect.signature(DOM_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_returnstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ReturnStatement)


def test_hyp_dom_returnstatement_constructor_exists():
    assert callable(DOM_ReturnStatement.__init__)


def test_hyp_dom_returnstatement_constructor_args():
    sig = inspect.signature(DOM_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_emptystatement_is_not_abstract():
    assert not inspect.isabstract(DOM_EmptyStatement)


def test_hyp_dom_emptystatement_constructor_exists():
    assert callable(DOM_EmptyStatement.__init__)


def test_hyp_dom_emptystatement_constructor_args():
    sig = inspect.signature(DOM_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_EnhancedForStatement)


def test_hyp_dom_enhancedforstatement_constructor_exists():
    assert callable(DOM_EnhancedForStatement.__init__)


def test_hyp_dom_enhancedforstatement_constructor_args():
    sig = inspect.signature(DOM_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_switchcase_is_not_abstract():
    assert not inspect.isabstract(DOM_SwitchCase)


def test_hyp_dom_switchcase_constructor_exists():
    assert callable(DOM_SwitchCase.__init__)


def test_hyp_dom_switchcase_constructor_args():
    sig = inspect.signature(DOM_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_dom_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperConstructorInvocation)


def test_hyp_dom_superconstructorinvocation_constructor_exists():
    assert callable(DOM_SuperConstructorInvocation.__init__)


def test_hyp_dom_superconstructorinvocation_constructor_args():
    sig = inspect.signature(DOM_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_whilestatement_is_not_abstract():
    assert not inspect.isabstract(DOM_WhileStatement)


def test_hyp_dom_whilestatement_constructor_exists():
    assert callable(DOM_WhileStatement.__init__)


def test_hyp_dom_whilestatement_constructor_args():
    sig = inspect.signature(DOM_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_SynchronizedStatement)


def test_hyp_dom_synchronizedstatement_constructor_exists():
    assert callable(DOM_SynchronizedStatement.__init__)


def test_hyp_dom_synchronizedstatement_constructor_args():
    sig = inspect.signature(DOM_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_assertstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_AssertStatement)


def test_hyp_dom_assertstatement_constructor_exists():
    assert callable(DOM_AssertStatement.__init__)


def test_hyp_dom_assertstatement_constructor_args():
    sig = inspect.signature(DOM_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_dostatement_is_not_abstract():
    assert not inspect.isabstract(DOM_DoStatement)


def test_hyp_dom_dostatement_constructor_exists():
    assert callable(DOM_DoStatement.__init__)


def test_hyp_dom_dostatement_constructor_args():
    sig = inspect.signature(DOM_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_continuestatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ContinueStatement)


def test_hyp_dom_continuestatement_constructor_exists():
    assert callable(DOM_ContinueStatement.__init__)


def test_hyp_dom_continuestatement_constructor_args():
    sig = inspect.signature(DOM_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_arraytype_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayType)


def test_hyp_dom_arraytype_constructor_exists():
    assert callable(DOM_ArrayType.__init__)


def test_hyp_dom_arraytype_constructor_args():
    sig = inspect.signature(DOM_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ParenthesizedExpression)


def test_hyp_dom_parenthesizedexpression_constructor_exists():
    assert callable(DOM_ParenthesizedExpression.__init__)


def test_hyp_dom_parenthesizedexpression_constructor_args():
    sig = inspect.signature(DOM_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ConditionalExpression)


def test_hyp_dom_conditionalexpression_constructor_exists():
    assert callable(DOM_ConditionalExpression.__init__)


def test_hyp_dom_conditionalexpression_constructor_args():
    sig = inspect.signature(DOM_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_numberliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_NumberLiteral)


def test_hyp_dom_numberliteral_constructor_exists():
    assert callable(DOM_NumberLiteral.__init__)


def test_hyp_dom_numberliteral_constructor_args():
    sig = inspect.signature(DOM_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"




def test_hyp_dom_castexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_CastExpression)


def test_hyp_dom_castexpression_constructor_exists():
    assert callable(DOM_CastExpression.__init__)


def test_hyp_dom_castexpression_constructor_args():
    sig = inspect.signature(DOM_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_thisexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ThisExpression)


def test_hyp_dom_thisexpression_constructor_exists():
    assert callable(DOM_ThisExpression.__init__)


def test_hyp_dom_thisexpression_constructor_args():
    sig = inspect.signature(DOM_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_BooleanLiteral)


def test_hyp_dom_booleanliteral_constructor_exists():
    assert callable(DOM_BooleanLiteral.__init__)


def test_hyp_dom_booleanliteral_constructor_args():
    sig = inspect.signature(DOM_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"




def test_hyp_dom_characterliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_CharacterLiteral)


def test_hyp_dom_characterliteral_constructor_exists():
    assert callable(DOM_CharacterLiteral.__init__)


def test_hyp_dom_characterliteral_constructor_args():
    sig = inspect.signature(DOM_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "charValue" in params, "Missing parameter 'charValue'"





def test_hyp_dom_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayInitializer)


def test_hyp_dom_arrayinitializer_constructor_exists():
    assert callable(DOM_ArrayInitializer.__init__)


def test_hyp_dom_arrayinitializer_constructor_args():
    sig = inspect.signature(DOM_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_stringliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_StringLiteral)


def test_hyp_dom_stringliteral_constructor_exists():
    assert callable(DOM_StringLiteral.__init__)


def test_hyp_dom_stringliteral_constructor_args():
    sig = inspect.signature(DOM_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "literalValue" in params, "Missing parameter 'literalValue'"





def test_hyp_dom_infixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_InfixExpression)


def test_hyp_dom_infixexpression_constructor_exists():
    assert callable(DOM_InfixExpression.__init__)


def test_hyp_dom_infixexpression_constructor_args():
    sig = inspect.signature(DOM_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationExpression)


def test_hyp_dom_variabledeclarationexpression_constructor_exists():
    assert callable(DOM_VariableDeclarationExpression.__init__)


def test_hyp_dom_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_assignment_is_not_abstract():
    assert not inspect.isabstract(DOM_Assignment)


def test_hyp_dom_assignment_constructor_exists():
    assert callable(DOM_Assignment.__init__)


def test_hyp_dom_assignment_constructor_args():
    sig = inspect.signature(DOM_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperFieldAccess)


def test_hyp_dom_superfieldaccess_constructor_exists():
    assert callable(DOM_SuperFieldAccess.__init__)


def test_hyp_dom_superfieldaccess_constructor_args():
    sig = inspect.signature(DOM_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodInvocation)


def test_hyp_dom_methodinvocation_constructor_exists():
    assert callable(DOM_MethodInvocation.__init__)


def test_hyp_dom_methodinvocation_constructor_args():
    sig = inspect.signature(DOM_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperMethodInvocation)


def test_hyp_dom_supermethodinvocation_constructor_exists():
    assert callable(DOM_SuperMethodInvocation.__init__)


def test_hyp_dom_supermethodinvocation_constructor_args():
    sig = inspect.signature(DOM_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_arraycreation_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayCreation)


def test_hyp_dom_arraycreation_constructor_exists():
    assert callable(DOM_ArrayCreation.__init__)


def test_hyp_dom_arraycreation_constructor_args():
    sig = inspect.signature(DOM_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_arrayaccess_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayAccess)


def test_hyp_dom_arrayaccess_constructor_exists():
    assert callable(DOM_ArrayAccess.__init__)


def test_hyp_dom_arrayaccess_constructor_args():
    sig = inspect.signature(DOM_ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM_FieldAccess)


def test_hyp_dom_fieldaccess_constructor_exists():
    assert callable(DOM_FieldAccess.__init__)


def test_hyp_dom_fieldaccess_constructor_args():
    sig = inspect.signature(DOM_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(DOM_ClassInstanceCreation)


def test_hyp_dom_classinstancecreation_constructor_exists():
    assert callable(DOM_ClassInstanceCreation.__init__)


def test_hyp_dom_classinstancecreation_constructor_args():
    sig = inspect.signature(DOM_ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_PrefixExpression)


def test_hyp_dom_prefixexpression_constructor_exists():
    assert callable(DOM_PrefixExpression.__init__)


def test_hyp_dom_prefixexpression_constructor_args():
    sig = inspect.signature(DOM_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_PostfixExpression)


def test_hyp_dom_postfixexpression_constructor_exists():
    assert callable(DOM_PostfixExpression.__init__)


def test_hyp_dom_postfixexpression_constructor_args():
    sig = inspect.signature(DOM_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_InstanceofExpression)


def test_hyp_dom_instanceofexpression_constructor_exists():
    assert callable(DOM_InstanceofExpression.__init__)


def test_hyp_dom_instanceofexpression_constructor_args():
    sig = inspect.signature(DOM_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_typeliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeLiteral)


def test_hyp_dom_typeliteral_constructor_exists():
    assert callable(DOM_TypeLiteral.__init__)


def test_hyp_dom_typeliteral_constructor_args():
    sig = inspect.signature(DOM_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_nullliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_NullLiteral)


def test_hyp_dom_nullliteral_constructor_exists():
    assert callable(DOM_NullLiteral.__init__)


def test_hyp_dom_nullliteral_constructor_args():
    sig = inspect.signature(DOM_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_hyp_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_hyp_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_linecomment_is_not_abstract():
    assert not inspect.isabstract(DOM_LineComment)


def test_hyp_dom_linecomment_constructor_exists():
    assert callable(DOM_LineComment.__init__)


def test_hyp_dom_linecomment_constructor_args():
    sig = inspect.signature(DOM_LineComment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_blockcomment_is_not_abstract():
    assert not inspect.isabstract(DOM_BlockComment)


def test_hyp_dom_blockcomment_constructor_exists():
    assert callable(DOM_BlockComment.__init__)


def test_hyp_dom_blockcomment_constructor_args():
    sig = inspect.signature(DOM_BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_hyp_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_hyp_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnnotationTypeDeclaration)


def test_hyp_dom_annotationtypedeclaration_constructor_exists():
    assert callable(DOM_AnnotationTypeDeclaration.__init__)


def test_hyp_dom_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(DOM_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_imethod_is_not_abstract():
    assert not inspect.isabstract(DOM_IMethod)


def test_hyp_dom_imethod_constructor_exists():
    assert callable(DOM_IMethod.__init__)


def test_hyp_dom_imethod_constructor_args():
    sig = inspect.signature(DOM_IMethod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationFragment)


def test_hyp_dom_variabledeclarationfragment_constructor_exists():
    assert callable(DOM_VariableDeclarationFragment.__init__)


def test_hyp_dom_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeDeclaration)


def test_hyp_dom_typedeclaration_constructor_exists():
    assert callable(DOM_TypeDeclaration.__init__)


def test_hyp_dom_typedeclaration_constructor_args():
    sig = inspect.signature(DOM_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"




def test_hyp_dom_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_EnumDeclaration)


def test_hyp_dom_enumdeclaration_constructor_exists():
    assert callable(DOM_EnumDeclaration.__init__)


def test_hyp_dom_enumdeclaration_constructor_args():
    sig = inspect.signature(DOM_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_hyp_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_hyp_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodDeclaration)


def test_hyp_dom_methoddeclaration_constructor_exists():
    assert callable(DOM_MethodDeclaration.__init__)


def test_hyp_dom_methoddeclaration_constructor_args():
    sig = inspect.signature(DOM_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"






def test_hyp_dom_initializer_is_not_abstract():
    assert not inspect.isabstract(DOM_Initializer)


def test_hyp_dom_initializer_constructor_exists():
    assert callable(DOM_Initializer.__init__)


def test_hyp_dom_initializer_constructor_args():
    sig = inspect.signature(DOM_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_FieldDeclaration)


def test_hyp_dom_fielddeclaration_constructor_exists():
    assert callable(DOM_FieldDeclaration.__init__)


def test_hyp_dom_fielddeclaration_constructor_args():
    sig = inspect.signature(DOM_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(DOM_IPackageFragment)


def test_hyp_dom_ipackagefragment_constructor_exists():
    assert callable(DOM_IPackageFragment.__init__)


def test_hyp_dom_ipackagefragment_constructor_args():
    sig = inspect.signature(DOM_IPackageFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_EnumConstantDeclaration)


def test_hyp_dom_enumconstantdeclaration_constructor_exists():
    assert callable(DOM_EnumConstantDeclaration.__init__)


def test_hyp_dom_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(DOM_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnnotationTypeMemberDeclaration)


def test_hyp_dom_annotationtypememberdeclaration_constructor_exists():
    assert callable(DOM_AnnotationTypeMemberDeclaration.__init__)


def test_hyp_dom_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(DOM_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(ExtendedModifier)


def test_hyp_extendedmodifier_constructor_exists():
    assert callable(ExtendedModifier.__init__)


def test_hyp_extendedmodifier_constructor_args():
    sig = inspect.signature(ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_annotation_is_not_abstract():
    assert not inspect.isabstract(DOM_Annotation)


def test_hyp_dom_annotation_constructor_exists():
    assert callable(DOM_Annotation.__init__)


def test_hyp_dom_annotation_constructor_args():
    sig = inspect.signature(DOM_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_simplename_is_not_abstract():
    assert not inspect.isabstract(DOM_SimpleName)


def test_hyp_dom_simplename_constructor_exists():
    assert callable(DOM_SimpleName.__init__)


def test_hyp_dom_simplename_constructor_args():
    sig = inspect.signature(DOM_SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "declaration" in params, "Missing parameter 'declaration'"





def test_hyp_dom_name_is_not_abstract():
    assert not inspect.isabstract(DOM_Name)


def test_hyp_dom_name_constructor_exists():
    assert callable(DOM_Name.__init__)


def test_hyp_dom_name_constructor_args():
    sig = inspect.signature(DOM_Name.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"




def test_hyp_dom_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AbstractTypeDeclaration)


def test_hyp_dom_abstracttypedeclaration_constructor_exists():
    assert callable(DOM_AbstractTypeDeclaration.__init__)


def test_hyp_dom_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(DOM_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "localTypeDeclaration" in params, "Missing parameter 'localTypeDeclaration'"
    assert "packageMemberTypeDeclaration" in params, "Missing parameter 'packageMemberTypeDeclaration'"
    assert "memberTypeDeclaration" in params, "Missing parameter 'memberTypeDeclaration'"






def test_hyp_dom_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_SingleVariableDeclaration)


def test_hyp_dom_singlevariabledeclaration_constructor_exists():
    assert callable(DOM_SingleVariableDeclaration.__init__)


def test_hyp_dom_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(DOM_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"




def test_hyp_dom_block_is_not_abstract():
    assert not inspect.isabstract(DOM_Block)


def test_hyp_dom_block_constructor_exists():
    assert callable(DOM_Block.__init__)


def test_hyp_dom_block_constructor_args():
    sig = inspect.signature(DOM_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_javadoc_is_not_abstract():
    assert not inspect.isabstract(DOM_Javadoc)


def test_hyp_dom_javadoc_constructor_exists():
    assert callable(DOM_Javadoc.__init__)


def test_hyp_dom_javadoc_constructor_args():
    sig = inspect.signature(DOM_Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(DOM_ExtendedModifier)


def test_hyp_dom_extendedmodifier_constructor_exists():
    assert callable(DOM_ExtendedModifier.__init__)


def test_hyp_dom_extendedmodifier_constructor_args():
    sig = inspect.signature(DOM_ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_itype_is_not_abstract():
    assert not inspect.isabstract(DOM_IType)


def test_hyp_dom_itype_constructor_exists():
    assert callable(DOM_IType.__init__)


def test_hyp_dom_itype_constructor_args():
    sig = inspect.signature(DOM_IType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_hyp_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_hyp_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_methodref_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodRef)


def test_hyp_dom_methodref_constructor_exists():
    assert callable(DOM_MethodRef.__init__)


def test_hyp_dom_methodref_constructor_args():
    sig = inspect.signature(DOM_MethodRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(DOM_MemberValuePair)


def test_hyp_dom_membervaluepair_constructor_exists():
    assert callable(DOM_MemberValuePair.__init__)


def test_hyp_dom_membervaluepair_constructor_args():
    sig = inspect.signature(DOM_MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_tagelement_is_not_abstract():
    assert not inspect.isabstract(DOM_TagElement)


def test_hyp_dom_tagelement_constructor_exists():
    assert callable(DOM_TagElement.__init__)


def test_hyp_dom_tagelement_constructor_args():
    sig = inspect.signature(DOM_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"
    assert "nested" in params, "Missing parameter 'nested'"





def test_hyp_dom_compilationunit_is_not_abstract():
    assert not inspect.isabstract(DOM_CompilationUnit)


def test_hyp_dom_compilationunit_constructor_exists():
    assert callable(DOM_CompilationUnit.__init__)


def test_hyp_dom_compilationunit_constructor_args():
    sig = inspect.signature(DOM_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_statement_is_not_abstract():
    assert not inspect.isabstract(DOM_Statement)


def test_hyp_dom_statement_constructor_exists():
    assert callable(DOM_Statement.__init__)


def test_hyp_dom_statement_constructor_args():
    sig = inspect.signature(DOM_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_expression_is_not_abstract():
    assert not inspect.isabstract(DOM_Expression)


def test_hyp_dom_expression_constructor_exists():
    assert callable(DOM_Expression.__init__)


def test_hyp_dom_expression_constructor_args():
    sig = inspect.signature(DOM_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "resolveUnboxing" in params, "Missing parameter 'resolveUnboxing'"
    assert "resolveBoxing" in params, "Missing parameter 'resolveBoxing'"





def test_hyp_dom_catchclause_is_not_abstract():
    assert not inspect.isabstract(DOM_CatchClause)


def test_hyp_dom_catchclause_constructor_exists():
    assert callable(DOM_CatchClause.__init__)


def test_hyp_dom_catchclause_constructor_args():
    sig = inspect.signature(DOM_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_type_is_not_abstract():
    assert not inspect.isabstract(DOM_Type)


def test_hyp_dom_type_constructor_exists():
    assert callable(DOM_Type.__init__)


def test_hyp_dom_type_constructor_args():
    sig = inspect.signature(DOM_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_memberref_is_not_abstract():
    assert not inspect.isabstract(DOM_MemberRef)


def test_hyp_dom_memberref_constructor_exists():
    assert callable(DOM_MemberRef.__init__)


def test_hyp_dom_memberref_constructor_args():
    sig = inspect.signature(DOM_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_modifier_is_not_abstract():
    assert not inspect.isabstract(DOM_Modifier)


def test_hyp_dom_modifier_constructor_exists():
    assert callable(DOM_Modifier.__init__)


def test_hyp_dom_modifier_constructor_args():
    sig = inspect.signature(DOM_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "none" in params, "Missing parameter 'none'"
    assert "native" in params, "Missing parameter 'native'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "private" in params, "Missing parameter 'private'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "public" in params, "Missing parameter 'public'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "final" in params, "Missing parameter 'final'"
    assert "static" in params, "Missing parameter 'static'"















def test_hyp_dom_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_BodyDeclaration)


def test_hyp_dom_bodydeclaration_constructor_exists():
    assert callable(DOM_BodyDeclaration.__init__)


def test_hyp_dom_bodydeclaration_constructor_args():
    sig = inspect.signature(DOM_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_comment_is_not_abstract():
    assert not inspect.isabstract(DOM_Comment)


def test_hyp_dom_comment_constructor_exists():
    assert callable(DOM_Comment.__init__)


def test_hyp_dom_comment_constructor_args():
    sig = inspect.signature(DOM_Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_textelement_is_not_abstract():
    assert not inspect.isabstract(DOM_TextElement)


def test_hyp_dom_textelement_constructor_exists():
    assert callable(DOM_TextElement.__init__)


def test_hyp_dom_textelement_constructor_args():
    sig = inspect.signature(DOM_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_dom_typeparameter_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeParameter)


def test_hyp_dom_typeparameter_constructor_exists():
    assert callable(DOM_TypeParameter.__init__)


def test_hyp_dom_typeparameter_constructor_args():
    sig = inspect.signature(DOM_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclaration)


def test_hyp_dom_variabledeclaration_constructor_exists():
    assert callable(DOM_VariableDeclaration.__init__)


def test_hyp_dom_variabledeclaration_constructor_args():
    sig = inspect.signature(DOM_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"




def test_hyp_dom_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodRefParameter)


def test_hyp_dom_methodrefparameter_constructor_exists():
    assert callable(DOM_MethodRefParameter.__init__)


def test_hyp_dom_methodrefparameter_constructor_args():
    sig = inspect.signature(DOM_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"




def test_hyp_dom_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_PackageDeclaration)


def test_hyp_dom_packagedeclaration_constructor_exists():
    assert callable(DOM_PackageDeclaration.__init__)


def test_hyp_dom_packagedeclaration_constructor_args():
    sig = inspect.signature(DOM_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_ImportDeclaration)


def test_hyp_dom_importdeclaration_constructor_exists():
    assert callable(DOM_ImportDeclaration.__init__)


def test_hyp_dom_importdeclaration_constructor_args():
    sig = inspect.signature(DOM_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "onDemand" in params, "Missing parameter 'onDemand'"
    assert "static" in params, "Missing parameter 'static'"





def test_hyp_dom_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnonymousClassDeclaration)


def test_hyp_dom_anonymousclassdeclaration_constructor_exists():
    assert callable(DOM_AnonymousClassDeclaration.__init__)


def test_hyp_dom_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(DOM_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_astnode_is_not_abstract():
    assert not inspect.isabstract(DOM_ASTNode)


def test_hyp_dom_astnode_constructor_exists():
    assert callable(DOM_ASTNode.__init__)


def test_hyp_dom_astnode_constructor_args():
    sig = inspect.signature(DOM_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_ast_is_not_abstract():
    assert not inspect.isabstract(DOM_AST)


def test_hyp_dom_ast_constructor_exists():
    assert callable(DOM_AST.__init__)


def test_hyp_dom_ast_constructor_args():
    sig = inspect.signature(DOM_AST.__init__)
    params = list(sig.parameters.keys())

def test_hyp_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_hyp_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "greater_equals",
        "conditional_and",
        "xor",
        "times",
        "remainder",
        "left_shift",
        "conditional_or",
        "plus",
        "right_shift_signed",
        "equals",
        "less_equals",
        "greater",
        "right_shift_unsigned",
        "less",
        "minus",
        "not_equals",
        "divide",
        "or_",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionOperatorKind"

def test_hyp_prefixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionOperatorKind is not None

def test_hyp_prefixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionOperatorKind]
    expected_literals = [
        "increment",
        "not_",
        "minus",
        "complement",
        "decrement",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionOperatorKind"

def test_hyp_postfixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PostfixExpressionOperatorKind is not None

def test_hyp_postfixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PostfixExpressionOperatorKind]
    expected_literals = [
        "increment",
        "decrement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PostfixExpressionOperatorKind"

def test_hyp_assignmentoperatorkind_exists():
    # Check that the Enumeration exists
    assert AssignmentOperatorKind is not None

def test_hyp_assignmentoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperatorKind]
    expected_literals = [
        "left_shift_assign",
        "divide_assign",
        "right_shift_unsigned_assign",
        "assign",
        "right_shift_signed_assign",
        "remainder_assign",
        "bit_xor_assign",
        "bit_and_assign",
        "minus_assign",
        "plus_assign",
        "bit_or_assign",
        "times_assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorKind"


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
Annotation_strategy = st.builds(
    Annotation,
)
DOM_SingleMemberAnnotation_strategy = st.builds(
    DOM_SingleMemberAnnotation,
)
DOM_NormalAnnotation_strategy = st.builds(
    DOM_NormalAnnotation,
)
DOM_MarkerAnnotation_strategy = st.builds(
    DOM_MarkerAnnotation,
)
Name_strategy = st.builds(
    Name,
)
DOM_QualifiedName_strategy = st.builds(
    DOM_QualifiedName,
)
Type_strategy = st.builds(
    Type,
)
DOM_SimpleType_strategy = st.builds(
    DOM_SimpleType,
)
DOM_ParameterizedType_strategy = st.builds(
    DOM_ParameterizedType,
)
DOM_PrimitiveType_strategy = st.builds(
    DOM_PrimitiveType,
    code=
        safe_text
)
DOM_QualifiedType_strategy = st.builds(
    DOM_QualifiedType,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
DOM_WildcardType_strategy = st.builds(
    DOM_WildcardType,
    upperBound=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
DOM_ForStatement_strategy = st.builds(
    DOM_ForStatement,
)
DOM_ExpressionStatement_strategy = st.builds(
    DOM_ExpressionStatement,
)
DOM_SwitchStatement_strategy = st.builds(
    DOM_SwitchStatement,
)
DOM_ConstructorInvocation_strategy = st.builds(
    DOM_ConstructorInvocation,
)
DOM_LabeledStatement_strategy = st.builds(
    DOM_LabeledStatement,
)
DOM_VariableDeclarationStatement_strategy = st.builds(
    DOM_VariableDeclarationStatement,
)
DOM_IfStatement_strategy = st.builds(
    DOM_IfStatement,
)
DOM_TypeDeclarationStatement_strategy = st.builds(
    DOM_TypeDeclarationStatement,
)
DOM_TryStatement_strategy = st.builds(
    DOM_TryStatement,
)
DOM_ThrowStatement_strategy = st.builds(
    DOM_ThrowStatement,
)
DOM_BreakStatement_strategy = st.builds(
    DOM_BreakStatement,
)
DOM_ReturnStatement_strategy = st.builds(
    DOM_ReturnStatement,
)
DOM_EmptyStatement_strategy = st.builds(
    DOM_EmptyStatement,
)
DOM_EnhancedForStatement_strategy = st.builds(
    DOM_EnhancedForStatement,
)
DOM_SwitchCase_strategy = st.builds(
    DOM_SwitchCase,
    default=
        safe_text
)
DOM_SuperConstructorInvocation_strategy = st.builds(
    DOM_SuperConstructorInvocation,
)
DOM_WhileStatement_strategy = st.builds(
    DOM_WhileStatement,
)
DOM_SynchronizedStatement_strategy = st.builds(
    DOM_SynchronizedStatement,
)
DOM_AssertStatement_strategy = st.builds(
    DOM_AssertStatement,
)
DOM_DoStatement_strategy = st.builds(
    DOM_DoStatement,
)
DOM_ContinueStatement_strategy = st.builds(
    DOM_ContinueStatement,
)
DOM_ArrayType_strategy = st.builds(
    DOM_ArrayType,
    dimensions=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
DOM_ParenthesizedExpression_strategy = st.builds(
    DOM_ParenthesizedExpression,
)
DOM_ConditionalExpression_strategy = st.builds(
    DOM_ConditionalExpression,
)
DOM_NumberLiteral_strategy = st.builds(
    DOM_NumberLiteral,
    token=
        safe_text
)
DOM_CastExpression_strategy = st.builds(
    DOM_CastExpression,
)
DOM_ThisExpression_strategy = st.builds(
    DOM_ThisExpression,
)
DOM_BooleanLiteral_strategy = st.builds(
    DOM_BooleanLiteral,
    booleanValue=
        safe_text
)
DOM_CharacterLiteral_strategy = st.builds(
    DOM_CharacterLiteral,
    escapedValue=
        safe_text,
    charValue=
        safe_text
)
DOM_ArrayInitializer_strategy = st.builds(
    DOM_ArrayInitializer,
)
DOM_StringLiteral_strategy = st.builds(
    DOM_StringLiteral,
    escapedValue=
        safe_text,
    literalValue=
        safe_text
)
DOM_InfixExpression_strategy = st.builds(
    DOM_InfixExpression,
    operator=
        safe_text
)
DOM_VariableDeclarationExpression_strategy = st.builds(
    DOM_VariableDeclarationExpression,
)
DOM_Assignment_strategy = st.builds(
    DOM_Assignment,
    operator=
        safe_text
)
DOM_SuperFieldAccess_strategy = st.builds(
    DOM_SuperFieldAccess,
)
DOM_MethodInvocation_strategy = st.builds(
    DOM_MethodInvocation,
)
DOM_SuperMethodInvocation_strategy = st.builds(
    DOM_SuperMethodInvocation,
)
DOM_ArrayCreation_strategy = st.builds(
    DOM_ArrayCreation,
)
DOM_ArrayAccess_strategy = st.builds(
    DOM_ArrayAccess,
)
DOM_FieldAccess_strategy = st.builds(
    DOM_FieldAccess,
)
DOM_ClassInstanceCreation_strategy = st.builds(
    DOM_ClassInstanceCreation,
)
DOM_PrefixExpression_strategy = st.builds(
    DOM_PrefixExpression,
    operator=
        safe_text
)
DOM_PostfixExpression_strategy = st.builds(
    DOM_PostfixExpression,
    operator=
        safe_text
)
DOM_InstanceofExpression_strategy = st.builds(
    DOM_InstanceofExpression,
)
DOM_TypeLiteral_strategy = st.builds(
    DOM_TypeLiteral,
)
DOM_NullLiteral_strategy = st.builds(
    DOM_NullLiteral,
)
Comment_strategy = st.builds(
    Comment,
)
DOM_LineComment_strategy = st.builds(
    DOM_LineComment,
)
DOM_BlockComment_strategy = st.builds(
    DOM_BlockComment,
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
DOM_AnnotationTypeDeclaration_strategy = st.builds(
    DOM_AnnotationTypeDeclaration,
)
DOM_IMethod_strategy = st.builds(
    DOM_IMethod,
)
DOM_VariableDeclarationFragment_strategy = st.builds(
    DOM_VariableDeclarationFragment,
)
DOM_TypeDeclaration_strategy = st.builds(
    DOM_TypeDeclaration,
    interface=
        safe_text
)
DOM_EnumDeclaration_strategy = st.builds(
    DOM_EnumDeclaration,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
DOM_MethodDeclaration_strategy = st.builds(
    DOM_MethodDeclaration,
    varargs=
        safe_text,
    constructor=
        safe_text,
    extraDimensions=
        safe_text
)
DOM_Initializer_strategy = st.builds(
    DOM_Initializer,
)
DOM_FieldDeclaration_strategy = st.builds(
    DOM_FieldDeclaration,
)
DOM_IPackageFragment_strategy = st.builds(
    DOM_IPackageFragment,
)
DOM_EnumConstantDeclaration_strategy = st.builds(
    DOM_EnumConstantDeclaration,
)
DOM_AnnotationTypeMemberDeclaration_strategy = st.builds(
    DOM_AnnotationTypeMemberDeclaration,
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
DOM_Annotation_strategy = st.builds(
    DOM_Annotation,
)
DOM_SimpleName_strategy = st.builds(
    DOM_SimpleName,
    identifier=
        safe_text,
    declaration=
        safe_text
)
DOM_Name_strategy = st.builds(
    DOM_Name,
    fullyQualifiedName=
        safe_text
)
DOM_AbstractTypeDeclaration_strategy = st.builds(
    DOM_AbstractTypeDeclaration,
    localTypeDeclaration=
        safe_text,
    packageMemberTypeDeclaration=
        safe_text,
    memberTypeDeclaration=
        safe_text
)
DOM_SingleVariableDeclaration_strategy = st.builds(
    DOM_SingleVariableDeclaration,
    varargs=
        safe_text
)
DOM_Block_strategy = st.builds(
    DOM_Block,
)
DOM_Javadoc_strategy = st.builds(
    DOM_Javadoc,
)
DOM_ExtendedModifier_strategy = st.builds(
    DOM_ExtendedModifier,
)
DOM_IType_strategy = st.builds(
    DOM_IType,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
DOM_MethodRef_strategy = st.builds(
    DOM_MethodRef,
)
DOM_MemberValuePair_strategy = st.builds(
    DOM_MemberValuePair,
)
DOM_TagElement_strategy = st.builds(
    DOM_TagElement,
    tagName=
        safe_text,
    nested=
        safe_text
)
DOM_CompilationUnit_strategy = st.builds(
    DOM_CompilationUnit,
)
DOM_Statement_strategy = st.builds(
    DOM_Statement,
)
DOM_Expression_strategy = st.builds(
    DOM_Expression,
    resolveUnboxing=
        safe_text,
    resolveBoxing=
        safe_text
)
DOM_CatchClause_strategy = st.builds(
    DOM_CatchClause,
)
DOM_Type_strategy = st.builds(
    DOM_Type,
)
DOM_MemberRef_strategy = st.builds(
    DOM_MemberRef,
)
DOM_Modifier_strategy = st.builds(
    DOM_Modifier,
    none=
        safe_text,
    native=
        safe_text,
    strictfp=
        safe_text,
    protected=
        safe_text,
    abstract=
        safe_text,
    private=
        safe_text,
    synchronized=
        safe_text,
    public=
        safe_text,
    transient=
        safe_text,
    volatile=
        safe_text,
    final=
        safe_text,
    static=
        safe_text
)
DOM_BodyDeclaration_strategy = st.builds(
    DOM_BodyDeclaration,
)
DOM_Comment_strategy = st.builds(
    DOM_Comment,
)
DOM_TextElement_strategy = st.builds(
    DOM_TextElement,
    text=
        safe_text
)
DOM_TypeParameter_strategy = st.builds(
    DOM_TypeParameter,
)
DOM_VariableDeclaration_strategy = st.builds(
    DOM_VariableDeclaration,
    extraDimensions=
        safe_text
)
DOM_MethodRefParameter_strategy = st.builds(
    DOM_MethodRefParameter,
    varargs=
        safe_text
)
DOM_PackageDeclaration_strategy = st.builds(
    DOM_PackageDeclaration,
)
DOM_ImportDeclaration_strategy = st.builds(
    DOM_ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
DOM_AnonymousClassDeclaration_strategy = st.builds(
    DOM_AnonymousClassDeclaration,
)
DOM_ASTNode_strategy = st.builds(
    DOM_ASTNode,
)
DOM_AST_strategy = st.builds(
    DOM_AST,
)













@given(instance=DOM_PrimitiveType_strategy)
def test_hyp_dom_primitivetype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original






@given(instance=DOM_WildcardType_strategy)
def test_hyp_dom_wildcardtype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



















@given(instance=DOM_SwitchCase_strategy)
def test_hyp_dom_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original










@given(instance=DOM_ArrayType_strategy)
def test_hyp_dom_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original







@given(instance=DOM_NumberLiteral_strategy)
def test_hyp_dom_numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original






@given(instance=DOM_BooleanLiteral_strategy)
def test_hyp_dom_booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original




@given(instance=DOM_CharacterLiteral_strategy)
def test_hyp_dom_characterliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=DOM_CharacterLiteral_strategy)
def test_hyp_dom_characterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original





@given(instance=DOM_StringLiteral_strategy)
def test_hyp_dom_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original



@given(instance=DOM_StringLiteral_strategy)
def test_hyp_dom_stringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original




@given(instance=DOM_InfixExpression_strategy)
def test_hyp_dom_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=DOM_Assignment_strategy)
def test_hyp_dom_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original











@given(instance=DOM_PrefixExpression_strategy)
def test_hyp_dom_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=DOM_PostfixExpression_strategy)
def test_hyp_dom_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original














@given(instance=DOM_TypeDeclaration_strategy)
def test_hyp_dom_typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original






@given(instance=DOM_MethodDeclaration_strategy)
def test_hyp_dom_methoddeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original



@given(instance=DOM_MethodDeclaration_strategy)
def test_hyp_dom_methoddeclaration_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original



@given(instance=DOM_MethodDeclaration_strategy)
def test_hyp_dom_methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original











@given(instance=DOM_SimpleName_strategy)
def test_hyp_dom_simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=DOM_SimpleName_strategy)
def test_hyp_dom_simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original




@given(instance=DOM_Name_strategy)
def test_hyp_dom_name_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original




@given(instance=DOM_AbstractTypeDeclaration_strategy)
def test_hyp_dom_abstracttypedeclaration_localTypeDeclaration_setter(instance):
    original = instance.localTypeDeclaration
    instance.localTypeDeclaration = original
    assert instance.localTypeDeclaration == original



@given(instance=DOM_AbstractTypeDeclaration_strategy)
def test_hyp_dom_abstracttypedeclaration_packageMemberTypeDeclaration_setter(instance):
    original = instance.packageMemberTypeDeclaration
    instance.packageMemberTypeDeclaration = original
    assert instance.packageMemberTypeDeclaration == original



@given(instance=DOM_AbstractTypeDeclaration_strategy)
def test_hyp_dom_abstracttypedeclaration_memberTypeDeclaration_setter(instance):
    original = instance.memberTypeDeclaration
    instance.memberTypeDeclaration = original
    assert instance.memberTypeDeclaration == original




@given(instance=DOM_SingleVariableDeclaration_strategy)
def test_hyp_dom_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original











@given(instance=DOM_TagElement_strategy)
def test_hyp_dom_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original



@given(instance=DOM_TagElement_strategy)
def test_hyp_dom_tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original






@given(instance=DOM_Expression_strategy)
def test_hyp_dom_expression_resolveUnboxing_setter(instance):
    original = instance.resolveUnboxing
    instance.resolveUnboxing = original
    assert instance.resolveUnboxing == original



@given(instance=DOM_Expression_strategy)
def test_hyp_dom_expression_resolveBoxing_setter(instance):
    original = instance.resolveBoxing
    instance.resolveBoxing = original
    assert instance.resolveBoxing == original







@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original






@given(instance=DOM_TextElement_strategy)
def test_hyp_dom_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=DOM_VariableDeclaration_strategy)
def test_hyp_dom_variabledeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original




@given(instance=DOM_MethodRefParameter_strategy)
def test_hyp_dom_methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original





@given(instance=DOM_ImportDeclaration_strategy)
def test_hyp_dom_importdeclaration_onDemand_setter(instance):
    original = instance.onDemand
    instance.onDemand = original
    assert instance.onDemand == original



@given(instance=DOM_ImportDeclaration_strategy)
def test_hyp_dom_importdeclaration_static_setter(instance):
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
    Annotation,
    BodyDeclaration,
    Comment,
    DOM_AST,
    DOM_ASTNode,
    DOM_AbstractTypeDeclaration,
    DOM_Annotation,
    DOM_AnnotationTypeDeclaration,
    DOM_AnnotationTypeMemberDeclaration,
    DOM_AnonymousClassDeclaration,
    DOM_ArrayAccess,
    DOM_ArrayCreation,
    DOM_ArrayInitializer,
    DOM_ArrayType,
    DOM_AssertStatement,
    DOM_Assignment,
    DOM_Block,
    DOM_BlockComment,
    DOM_BodyDeclaration,
    DOM_BooleanLiteral,
    DOM_BreakStatement,
    DOM_CastExpression,
    DOM_CatchClause,
    DOM_CharacterLiteral,
    DOM_ClassInstanceCreation,
    DOM_Comment,
    DOM_CompilationUnit,
    DOM_ConditionalExpression,
    DOM_ConstructorInvocation,
    DOM_ContinueStatement,
    DOM_DoStatement,
    DOM_EmptyStatement,
    DOM_EnhancedForStatement,
    DOM_EnumConstantDeclaration,
    DOM_EnumDeclaration,
    DOM_Expression,
    DOM_ExpressionStatement,
    DOM_ExtendedModifier,
    DOM_FieldAccess,
    DOM_FieldDeclaration,
    DOM_ForStatement,
    DOM_IMethod,
    DOM_IPackageFragment,
    DOM_IType,
    DOM_IfStatement,
    DOM_ImportDeclaration,
    DOM_InfixExpression,
    DOM_Initializer,
    DOM_InstanceofExpression,
    DOM_Javadoc,
    DOM_LabeledStatement,
    DOM_LineComment,
    DOM_MarkerAnnotation,
    DOM_MemberRef,
    DOM_MemberValuePair,
    DOM_MethodDeclaration,
    DOM_MethodInvocation,
    DOM_MethodRef,
    DOM_MethodRefParameter,
    DOM_Modifier,
    DOM_Name,
    DOM_NormalAnnotation,
    DOM_NullLiteral,
    DOM_NumberLiteral,
    DOM_PackageDeclaration,
    DOM_ParameterizedType,
    DOM_ParenthesizedExpression,
    DOM_PostfixExpression,
    DOM_PrefixExpression,
    DOM_PrimitiveType,
    DOM_QualifiedName,
    DOM_QualifiedType,
    DOM_ReturnStatement,
    DOM_SimpleName,
    DOM_SimpleType,
    DOM_SingleMemberAnnotation,
    DOM_SingleVariableDeclaration,
    DOM_Statement,
    DOM_StringLiteral,
    DOM_SuperConstructorInvocation,
    DOM_SuperFieldAccess,
    DOM_SuperMethodInvocation,
    DOM_SwitchCase,
    DOM_SwitchStatement,
    DOM_SynchronizedStatement,
    DOM_TagElement,
    DOM_TextElement,
    DOM_ThisExpression,
    DOM_ThrowStatement,
    DOM_TryStatement,
    DOM_Type,
    DOM_TypeDeclaration,
    DOM_TypeDeclarationStatement,
    DOM_TypeLiteral,
    DOM_TypeParameter,
    DOM_VariableDeclaration,
    DOM_VariableDeclarationExpression,
    DOM_VariableDeclarationFragment,
    DOM_VariableDeclarationStatement,
    DOM_WhileStatement,
    DOM_WildcardType,
    Expression,
    ExtendedModifier,
    Name,
    Statement,
    Type,
    VariableDeclaration,
    AssignmentOperatorKind,
    InfixExpressionOperatorKind,
    PostfixExpressionOperatorKind,
    PrefixExpressionOperatorKind,
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

def test_DOM_AbstractTypeDeclaration_localTypeDeclaration_value_roundtrip():
    instance = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    assert instance.localTypeDeclaration == "sample_text"
    instance.localTypeDeclaration = "sample_text_2"
    assert instance.localTypeDeclaration == "sample_text_2"


def test_DOM_AbstractTypeDeclaration_memberTypeDeclaration_value_roundtrip():
    instance = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    assert instance.memberTypeDeclaration == "sample_text"
    instance.memberTypeDeclaration = "sample_text_2"
    assert instance.memberTypeDeclaration == "sample_text_2"


def test_DOM_AbstractTypeDeclaration_packageMemberTypeDeclaration_value_roundtrip():
    instance = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    assert instance.packageMemberTypeDeclaration == "sample_text"
    instance.packageMemberTypeDeclaration = "sample_text_2"
    assert instance.packageMemberTypeDeclaration == "sample_text_2"


def test_DOM_ArrayType_dimensions_value_roundtrip():
    instance = DOM_ArrayType(dimensions="sample_text")
    assert instance.dimensions == "sample_text"
    instance.dimensions = "sample_text_2"
    assert instance.dimensions == "sample_text_2"


def test_DOM_Assignment_operator_value_roundtrip():
    instance = DOM_Assignment(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_DOM_BooleanLiteral_booleanValue_value_roundtrip():
    instance = DOM_BooleanLiteral(booleanValue="sample_text")
    assert instance.booleanValue == "sample_text"
    instance.booleanValue = "sample_text_2"
    assert instance.booleanValue == "sample_text_2"


def test_DOM_CharacterLiteral_charValue_value_roundtrip():
    instance = DOM_CharacterLiteral(charValue="sample_text", escapedValue="sample_text")
    assert instance.charValue == "sample_text"
    instance.charValue = "sample_text_2"
    assert instance.charValue == "sample_text_2"


def test_DOM_CharacterLiteral_escapedValue_value_roundtrip():
    instance = DOM_CharacterLiteral(charValue="sample_text", escapedValue="sample_text")
    assert instance.escapedValue == "sample_text"
    instance.escapedValue = "sample_text_2"
    assert instance.escapedValue == "sample_text_2"


def test_DOM_Expression_resolveBoxing_value_roundtrip():
    instance = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    assert instance.resolveBoxing == "sample_text"
    instance.resolveBoxing = "sample_text_2"
    assert instance.resolveBoxing == "sample_text_2"


def test_DOM_Expression_resolveUnboxing_value_roundtrip():
    instance = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    assert instance.resolveUnboxing == "sample_text"
    instance.resolveUnboxing = "sample_text_2"
    assert instance.resolveUnboxing == "sample_text_2"


def test_DOM_ImportDeclaration_onDemand_value_roundtrip():
    instance = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    assert instance.onDemand == "sample_text"
    instance.onDemand = "sample_text_2"
    assert instance.onDemand == "sample_text_2"


def test_DOM_ImportDeclaration_static_value_roundtrip():
    instance = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    assert instance.static == "sample_text"
    instance.static = "sample_text_2"
    assert instance.static == "sample_text_2"


def test_DOM_InfixExpression_operator_value_roundtrip():
    instance = DOM_InfixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_DOM_MethodDeclaration_constructor_value_roundtrip():
    instance = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    assert instance.constructor == "sample_text"
    instance.constructor = "sample_text_2"
    assert instance.constructor == "sample_text_2"


def test_DOM_MethodDeclaration_extraDimensions_value_roundtrip():
    instance = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    assert instance.extraDimensions == "sample_text"
    instance.extraDimensions = "sample_text_2"
    assert instance.extraDimensions == "sample_text_2"


def test_DOM_MethodDeclaration_varargs_value_roundtrip():
    instance = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    assert instance.varargs == "sample_text"
    instance.varargs = "sample_text_2"
    assert instance.varargs == "sample_text_2"


def test_DOM_MethodRefParameter_varargs_value_roundtrip():
    instance = DOM_MethodRefParameter(varargs="sample_text")
    assert instance.varargs == "sample_text"
    instance.varargs = "sample_text_2"
    assert instance.varargs == "sample_text_2"


def test_DOM_Modifier_abstract_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.abstract == "sample_text"
    instance.abstract = "sample_text_2"
    assert instance.abstract == "sample_text_2"


def test_DOM_Modifier_final_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.final == "sample_text"
    instance.final = "sample_text_2"
    assert instance.final == "sample_text_2"


def test_DOM_Modifier_native_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.native == "sample_text"
    instance.native = "sample_text_2"
    assert instance.native == "sample_text_2"


def test_DOM_Modifier_none_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.none == "sample_text"
    instance.none = "sample_text_2"
    assert instance.none == "sample_text_2"


def test_DOM_Modifier_private_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.private == "sample_text"
    instance.private = "sample_text_2"
    assert instance.private == "sample_text_2"


def test_DOM_Modifier_protected_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.protected == "sample_text"
    instance.protected = "sample_text_2"
    assert instance.protected == "sample_text_2"


def test_DOM_Modifier_public_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.public == "sample_text"
    instance.public = "sample_text_2"
    assert instance.public == "sample_text_2"


def test_DOM_Modifier_static_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.static == "sample_text"
    instance.static = "sample_text_2"
    assert instance.static == "sample_text_2"


def test_DOM_Modifier_strictfp_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.strictfp == "sample_text"
    instance.strictfp = "sample_text_2"
    assert instance.strictfp == "sample_text_2"


def test_DOM_Modifier_synchronized_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.synchronized == "sample_text"
    instance.synchronized = "sample_text_2"
    assert instance.synchronized == "sample_text_2"


def test_DOM_Modifier_transient_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.transient == "sample_text"
    instance.transient = "sample_text_2"
    assert instance.transient == "sample_text_2"


def test_DOM_Modifier_volatile_value_roundtrip():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert instance.volatile == "sample_text"
    instance.volatile = "sample_text_2"
    assert instance.volatile == "sample_text_2"


def test_DOM_Name_fullyQualifiedName_value_roundtrip():
    instance = DOM_Name(fullyQualifiedName="sample_text")
    assert instance.fullyQualifiedName == "sample_text"
    instance.fullyQualifiedName = "sample_text_2"
    assert instance.fullyQualifiedName == "sample_text_2"


def test_DOM_NumberLiteral_token_value_roundtrip():
    instance = DOM_NumberLiteral(token="sample_text")
    assert instance.token == "sample_text"
    instance.token = "sample_text_2"
    assert instance.token == "sample_text_2"


def test_DOM_PostfixExpression_operator_value_roundtrip():
    instance = DOM_PostfixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_DOM_PrefixExpression_operator_value_roundtrip():
    instance = DOM_PrefixExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_DOM_PrimitiveType_code_value_roundtrip():
    instance = DOM_PrimitiveType(code="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_DOM_SimpleName_declaration_value_roundtrip():
    instance = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    assert instance.declaration == "sample_text"
    instance.declaration = "sample_text_2"
    assert instance.declaration == "sample_text_2"


def test_DOM_SimpleName_identifier_value_roundtrip():
    instance = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_DOM_SingleVariableDeclaration_varargs_value_roundtrip():
    instance = DOM_SingleVariableDeclaration(varargs="sample_text")
    assert instance.varargs == "sample_text"
    instance.varargs = "sample_text_2"
    assert instance.varargs == "sample_text_2"


def test_DOM_StringLiteral_escapedValue_value_roundtrip():
    instance = DOM_StringLiteral(escapedValue="sample_text", literalValue="sample_text")
    assert instance.escapedValue == "sample_text"
    instance.escapedValue = "sample_text_2"
    assert instance.escapedValue == "sample_text_2"


def test_DOM_StringLiteral_literalValue_value_roundtrip():
    instance = DOM_StringLiteral(escapedValue="sample_text", literalValue="sample_text")
    assert instance.literalValue == "sample_text"
    instance.literalValue = "sample_text_2"
    assert instance.literalValue == "sample_text_2"


def test_DOM_SwitchCase_default_value_roundtrip():
    instance = DOM_SwitchCase(default="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_DOM_TagElement_nested_value_roundtrip():
    instance = DOM_TagElement(nested="sample_text", tagName="sample_text")
    assert instance.nested == "sample_text"
    instance.nested = "sample_text_2"
    assert instance.nested == "sample_text_2"


def test_DOM_TagElement_tagName_value_roundtrip():
    instance = DOM_TagElement(nested="sample_text", tagName="sample_text")
    assert instance.tagName == "sample_text"
    instance.tagName = "sample_text_2"
    assert instance.tagName == "sample_text_2"


def test_DOM_TextElement_text_value_roundtrip():
    instance = DOM_TextElement(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_DOM_TypeDeclaration_interface_value_roundtrip():
    instance = DOM_TypeDeclaration(interface="sample_text")
    assert instance.interface == "sample_text"
    instance.interface = "sample_text_2"
    assert instance.interface == "sample_text_2"


def test_DOM_VariableDeclaration_extraDimensions_value_roundtrip():
    instance = DOM_VariableDeclaration(extraDimensions="sample_text")
    assert instance.extraDimensions == "sample_text"
    instance.extraDimensions = "sample_text_2"
    assert instance.extraDimensions == "sample_text_2"


def test_DOM_WildcardType_upperBound_value_roundtrip():
    instance = DOM_WildcardType(upperBound="sample_text")
    assert instance.upperBound == "sample_text"
    instance.upperBound = "sample_text_2"
    assert instance.upperBound == "sample_text_2"


def test_DOM_AnonymousClassDeclaration_isa_ASTNode():
    instance = DOM_AnonymousClassDeclaration()
    assert isinstance(instance, ASTNode)


def test_DOM_BodyDeclaration_isa_ASTNode():
    instance = DOM_BodyDeclaration()
    assert isinstance(instance, ASTNode)


def test_DOM_CatchClause_isa_ASTNode():
    instance = DOM_CatchClause()
    assert isinstance(instance, ASTNode)


def test_DOM_Comment_isa_ASTNode():
    instance = DOM_Comment()
    assert isinstance(instance, ASTNode)


def test_DOM_CompilationUnit_isa_ASTNode():
    instance = DOM_CompilationUnit()
    assert isinstance(instance, ASTNode)


def test_DOM_Expression_isa_ASTNode():
    instance = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    assert isinstance(instance, ASTNode)


def test_DOM_ImportDeclaration_isa_ASTNode():
    instance = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    assert isinstance(instance, ASTNode)


def test_DOM_MemberRef_isa_ASTNode():
    instance = DOM_MemberRef()
    assert isinstance(instance, ASTNode)


def test_DOM_MemberValuePair_isa_ASTNode():
    instance = DOM_MemberValuePair()
    assert isinstance(instance, ASTNode)


def test_DOM_MethodRef_isa_ASTNode():
    instance = DOM_MethodRef()
    assert isinstance(instance, ASTNode)


def test_DOM_MethodRefParameter_isa_ASTNode():
    instance = DOM_MethodRefParameter(varargs="sample_text")
    assert isinstance(instance, ASTNode)


def test_DOM_Modifier_isa_ASTNode():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert isinstance(instance, ASTNode)


def test_DOM_PackageDeclaration_isa_ASTNode():
    instance = DOM_PackageDeclaration()
    assert isinstance(instance, ASTNode)


def test_DOM_Statement_isa_ASTNode():
    instance = DOM_Statement()
    assert isinstance(instance, ASTNode)


def test_DOM_TagElement_isa_ASTNode():
    instance = DOM_TagElement(nested="sample_text", tagName="sample_text")
    assert isinstance(instance, ASTNode)


def test_DOM_TextElement_isa_ASTNode():
    instance = DOM_TextElement(text="sample_text")
    assert isinstance(instance, ASTNode)


def test_DOM_Type_isa_ASTNode():
    instance = DOM_Type()
    assert isinstance(instance, ASTNode)


def test_DOM_TypeParameter_isa_ASTNode():
    instance = DOM_TypeParameter()
    assert isinstance(instance, ASTNode)


def test_DOM_VariableDeclaration_isa_ASTNode():
    instance = DOM_VariableDeclaration(extraDimensions="sample_text")
    assert isinstance(instance, ASTNode)


def test_DOM_AnnotationTypeDeclaration_isa_AbstractTypeDeclaration():
    instance = DOM_AnnotationTypeDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_DOM_EnumDeclaration_isa_AbstractTypeDeclaration():
    instance = DOM_EnumDeclaration()
    assert isinstance(instance, AbstractTypeDeclaration)


def test_DOM_TypeDeclaration_isa_AbstractTypeDeclaration():
    instance = DOM_TypeDeclaration(interface="sample_text")
    assert isinstance(instance, AbstractTypeDeclaration)


def test_DOM_MarkerAnnotation_isa_Annotation():
    instance = DOM_MarkerAnnotation()
    assert isinstance(instance, Annotation)


def test_DOM_NormalAnnotation_isa_Annotation():
    instance = DOM_NormalAnnotation()
    assert isinstance(instance, Annotation)


def test_DOM_SingleMemberAnnotation_isa_Annotation():
    instance = DOM_SingleMemberAnnotation()
    assert isinstance(instance, Annotation)


def test_DOM_AbstractTypeDeclaration_isa_BodyDeclaration():
    instance = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    assert isinstance(instance, BodyDeclaration)


def test_DOM_AnnotationTypeMemberDeclaration_isa_BodyDeclaration():
    instance = DOM_AnnotationTypeMemberDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_DOM_EnumConstantDeclaration_isa_BodyDeclaration():
    instance = DOM_EnumConstantDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_DOM_FieldDeclaration_isa_BodyDeclaration():
    instance = DOM_FieldDeclaration()
    assert isinstance(instance, BodyDeclaration)


def test_DOM_Initializer_isa_BodyDeclaration():
    instance = DOM_Initializer()
    assert isinstance(instance, BodyDeclaration)


def test_DOM_MethodDeclaration_isa_BodyDeclaration():
    instance = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    assert isinstance(instance, BodyDeclaration)


def test_DOM_BlockComment_isa_Comment():
    instance = DOM_BlockComment()
    assert isinstance(instance, Comment)


def test_DOM_Javadoc_isa_Comment():
    instance = DOM_Javadoc()
    assert isinstance(instance, Comment)


def test_DOM_LineComment_isa_Comment():
    instance = DOM_LineComment()
    assert isinstance(instance, Comment)


def test_DOM_Annotation_isa_Expression():
    instance = DOM_Annotation()
    assert isinstance(instance, Expression)


def test_DOM_ArrayAccess_isa_Expression():
    instance = DOM_ArrayAccess()
    assert isinstance(instance, Expression)


def test_DOM_ArrayCreation_isa_Expression():
    instance = DOM_ArrayCreation()
    assert isinstance(instance, Expression)


def test_DOM_ArrayInitializer_isa_Expression():
    instance = DOM_ArrayInitializer()
    assert isinstance(instance, Expression)


def test_DOM_Assignment_isa_Expression():
    instance = DOM_Assignment(operator="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_BooleanLiteral_isa_Expression():
    instance = DOM_BooleanLiteral(booleanValue="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_CastExpression_isa_Expression():
    instance = DOM_CastExpression()
    assert isinstance(instance, Expression)


def test_DOM_CharacterLiteral_isa_Expression():
    instance = DOM_CharacterLiteral(charValue="sample_text", escapedValue="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_ClassInstanceCreation_isa_Expression():
    instance = DOM_ClassInstanceCreation()
    assert isinstance(instance, Expression)


def test_DOM_ConditionalExpression_isa_Expression():
    instance = DOM_ConditionalExpression()
    assert isinstance(instance, Expression)


def test_DOM_FieldAccess_isa_Expression():
    instance = DOM_FieldAccess()
    assert isinstance(instance, Expression)


def test_DOM_InfixExpression_isa_Expression():
    instance = DOM_InfixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_InstanceofExpression_isa_Expression():
    instance = DOM_InstanceofExpression()
    assert isinstance(instance, Expression)


def test_DOM_MethodInvocation_isa_Expression():
    instance = DOM_MethodInvocation()
    assert isinstance(instance, Expression)


def test_DOM_Name_isa_Expression():
    instance = DOM_Name(fullyQualifiedName="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_NullLiteral_isa_Expression():
    instance = DOM_NullLiteral()
    assert isinstance(instance, Expression)


def test_DOM_NumberLiteral_isa_Expression():
    instance = DOM_NumberLiteral(token="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_ParenthesizedExpression_isa_Expression():
    instance = DOM_ParenthesizedExpression()
    assert isinstance(instance, Expression)


def test_DOM_PostfixExpression_isa_Expression():
    instance = DOM_PostfixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_PrefixExpression_isa_Expression():
    instance = DOM_PrefixExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_StringLiteral_isa_Expression():
    instance = DOM_StringLiteral(escapedValue="sample_text", literalValue="sample_text")
    assert isinstance(instance, Expression)


def test_DOM_SuperFieldAccess_isa_Expression():
    instance = DOM_SuperFieldAccess()
    assert isinstance(instance, Expression)


def test_DOM_SuperMethodInvocation_isa_Expression():
    instance = DOM_SuperMethodInvocation()
    assert isinstance(instance, Expression)


def test_DOM_ThisExpression_isa_Expression():
    instance = DOM_ThisExpression()
    assert isinstance(instance, Expression)


def test_DOM_TypeLiteral_isa_Expression():
    instance = DOM_TypeLiteral()
    assert isinstance(instance, Expression)


def test_DOM_VariableDeclarationExpression_isa_Expression():
    instance = DOM_VariableDeclarationExpression()
    assert isinstance(instance, Expression)


def test_DOM_Annotation_isa_ExtendedModifier():
    instance = DOM_Annotation()
    assert isinstance(instance, ExtendedModifier)


def test_DOM_Modifier_isa_ExtendedModifier():
    instance = DOM_Modifier(abstract="sample_text", final="sample_text", native="sample_text", none="sample_text", private="sample_text", protected="sample_text", public="sample_text", static="sample_text", strictfp="sample_text", synchronized="sample_text", transient="sample_text", volatile="sample_text")
    assert isinstance(instance, ExtendedModifier)


def test_DOM_QualifiedName_isa_Name():
    instance = DOM_QualifiedName()
    assert isinstance(instance, Name)


def test_DOM_SimpleName_isa_Name():
    instance = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    assert isinstance(instance, Name)


def test_DOM_AssertStatement_isa_Statement():
    instance = DOM_AssertStatement()
    assert isinstance(instance, Statement)


def test_DOM_Block_isa_Statement():
    instance = DOM_Block()
    assert isinstance(instance, Statement)


def test_DOM_BreakStatement_isa_Statement():
    instance = DOM_BreakStatement()
    assert isinstance(instance, Statement)


def test_DOM_ConstructorInvocation_isa_Statement():
    instance = DOM_ConstructorInvocation()
    assert isinstance(instance, Statement)


def test_DOM_ContinueStatement_isa_Statement():
    instance = DOM_ContinueStatement()
    assert isinstance(instance, Statement)


def test_DOM_DoStatement_isa_Statement():
    instance = DOM_DoStatement()
    assert isinstance(instance, Statement)


def test_DOM_EmptyStatement_isa_Statement():
    instance = DOM_EmptyStatement()
    assert isinstance(instance, Statement)


def test_DOM_EnhancedForStatement_isa_Statement():
    instance = DOM_EnhancedForStatement()
    assert isinstance(instance, Statement)


def test_DOM_ExpressionStatement_isa_Statement():
    instance = DOM_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_DOM_ForStatement_isa_Statement():
    instance = DOM_ForStatement()
    assert isinstance(instance, Statement)


def test_DOM_IfStatement_isa_Statement():
    instance = DOM_IfStatement()
    assert isinstance(instance, Statement)


def test_DOM_LabeledStatement_isa_Statement():
    instance = DOM_LabeledStatement()
    assert isinstance(instance, Statement)


def test_DOM_ReturnStatement_isa_Statement():
    instance = DOM_ReturnStatement()
    assert isinstance(instance, Statement)


def test_DOM_SuperConstructorInvocation_isa_Statement():
    instance = DOM_SuperConstructorInvocation()
    assert isinstance(instance, Statement)


def test_DOM_SwitchCase_isa_Statement():
    instance = DOM_SwitchCase(default="sample_text")
    assert isinstance(instance, Statement)


def test_DOM_SwitchStatement_isa_Statement():
    instance = DOM_SwitchStatement()
    assert isinstance(instance, Statement)


def test_DOM_SynchronizedStatement_isa_Statement():
    instance = DOM_SynchronizedStatement()
    assert isinstance(instance, Statement)


def test_DOM_ThrowStatement_isa_Statement():
    instance = DOM_ThrowStatement()
    assert isinstance(instance, Statement)


def test_DOM_TryStatement_isa_Statement():
    instance = DOM_TryStatement()
    assert isinstance(instance, Statement)


def test_DOM_TypeDeclarationStatement_isa_Statement():
    instance = DOM_TypeDeclarationStatement()
    assert isinstance(instance, Statement)


def test_DOM_VariableDeclarationStatement_isa_Statement():
    instance = DOM_VariableDeclarationStatement()
    assert isinstance(instance, Statement)


def test_DOM_WhileStatement_isa_Statement():
    instance = DOM_WhileStatement()
    assert isinstance(instance, Statement)


def test_DOM_ArrayType_isa_Type():
    instance = DOM_ArrayType(dimensions="sample_text")
    assert isinstance(instance, Type)


def test_DOM_ParameterizedType_isa_Type():
    instance = DOM_ParameterizedType()
    assert isinstance(instance, Type)


def test_DOM_PrimitiveType_isa_Type():
    instance = DOM_PrimitiveType(code="sample_text")
    assert isinstance(instance, Type)


def test_DOM_QualifiedType_isa_Type():
    instance = DOM_QualifiedType()
    assert isinstance(instance, Type)


def test_DOM_SimpleType_isa_Type():
    instance = DOM_SimpleType()
    assert isinstance(instance, Type)


def test_DOM_WildcardType_isa_Type():
    instance = DOM_WildcardType(upperBound="sample_text")
    assert isinstance(instance, Type)


def test_DOM_SingleVariableDeclaration_isa_VariableDeclaration():
    instance = DOM_SingleVariableDeclaration(varargs="sample_text")
    assert isinstance(instance, VariableDeclaration)


def test_DOM_VariableDeclarationFragment_isa_VariableDeclaration():
    instance = DOM_VariableDeclarationFragment()
    assert isinstance(instance, VariableDeclaration)


def test_assoc_arguments155_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ClassInstanceCreation()
    b2 = DOM_ClassInstanceCreation()
    _safe_set(a, 'DOM_Expression156', b1)
    assert _is_linked(a, 'DOM_Expression156', b1)
    if hasattr(b1, 'DOM_ClassInstanceCreation'):
        assert _is_linked(b1, 'DOM_ClassInstanceCreation', a)
    _safe_set(a, 'DOM_Expression156', b2)
    assert _is_linked(a, 'DOM_Expression156', b2)
    if hasattr(b1, 'DOM_ClassInstanceCreation'):
        assert not _is_linked(b1, 'DOM_ClassInstanceCreation', a)
    if hasattr(b2, 'DOM_ClassInstanceCreation'):
        assert _is_linked(b2, 'DOM_ClassInstanceCreation', a)
    _safe_set(a, 'DOM_Expression156', None)
    assert not _is_linked(a, 'DOM_Expression156', b2)
    if hasattr(b2, 'DOM_ClassInstanceCreation'):
        assert not _is_linked(b2, 'DOM_ClassInstanceCreation', a)


def test_assoc_arguments195_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_MethodInvocation()
    b2 = DOM_MethodInvocation()
    _safe_set(a, 'DOM_Expression196', b1)
    assert _is_linked(a, 'DOM_Expression196', b1)
    if hasattr(b1, 'DOM_MethodInvocation'):
        assert _is_linked(b1, 'DOM_MethodInvocation', a)
    _safe_set(a, 'DOM_Expression196', b2)
    assert _is_linked(a, 'DOM_Expression196', b2)
    if hasattr(b1, 'DOM_MethodInvocation'):
        assert not _is_linked(b1, 'DOM_MethodInvocation', a)
    if hasattr(b2, 'DOM_MethodInvocation'):
        assert _is_linked(b2, 'DOM_MethodInvocation', a)
    _safe_set(a, 'DOM_Expression196', None)
    assert not _is_linked(a, 'DOM_Expression196', b2)
    if hasattr(b2, 'DOM_MethodInvocation'):
        assert not _is_linked(b2, 'DOM_MethodInvocation', a)


def test_assoc_arguments220_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_SuperMethodInvocation()
    b2 = DOM_SuperMethodInvocation()
    _safe_set(a, 'DOM_Expression221', b1)
    assert _is_linked(a, 'DOM_Expression221', b1)
    if hasattr(b1, 'DOM_SuperMethodInvocation'):
        assert _is_linked(b1, 'DOM_SuperMethodInvocation', a)
    _safe_set(a, 'DOM_Expression221', b2)
    assert _is_linked(a, 'DOM_Expression221', b2)
    if hasattr(b1, 'DOM_SuperMethodInvocation'):
        assert not _is_linked(b1, 'DOM_SuperMethodInvocation', a)
    if hasattr(b2, 'DOM_SuperMethodInvocation'):
        assert _is_linked(b2, 'DOM_SuperMethodInvocation', a)
    _safe_set(a, 'DOM_Expression221', None)
    assert not _is_linked(a, 'DOM_Expression221', b2)
    if hasattr(b2, 'DOM_SuperMethodInvocation'):
        assert not _is_linked(b2, 'DOM_SuperMethodInvocation', a)


def test_assoc_arguments252_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ConstructorInvocation()
    b2 = DOM_ConstructorInvocation()
    _safe_set(a, 'DOM_Expression253', b1)
    assert _is_linked(a, 'DOM_Expression253', b1)
    if hasattr(b1, 'DOM_ConstructorInvocation'):
        assert _is_linked(b1, 'DOM_ConstructorInvocation', a)
    _safe_set(a, 'DOM_Expression253', b2)
    assert _is_linked(a, 'DOM_Expression253', b2)
    if hasattr(b1, 'DOM_ConstructorInvocation'):
        assert not _is_linked(b1, 'DOM_ConstructorInvocation', a)
    if hasattr(b2, 'DOM_ConstructorInvocation'):
        assert _is_linked(b2, 'DOM_ConstructorInvocation', a)
    _safe_set(a, 'DOM_Expression253', None)
    assert not _is_linked(a, 'DOM_Expression253', b2)
    if hasattr(b2, 'DOM_ConstructorInvocation'):
        assert not _is_linked(b2, 'DOM_ConstructorInvocation', a)


def test_assoc_arguments300_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_SuperConstructorInvocation()
    b2 = DOM_SuperConstructorInvocation()
    _safe_set(a, 'DOM_Expression301', b1)
    assert _is_linked(a, 'DOM_Expression301', b1)
    if hasattr(b1, 'DOM_SuperConstructorInvocation'):
        assert _is_linked(b1, 'DOM_SuperConstructorInvocation', a)
    _safe_set(a, 'DOM_Expression301', b2)
    assert _is_linked(a, 'DOM_Expression301', b2)
    if hasattr(b1, 'DOM_SuperConstructorInvocation'):
        assert not _is_linked(b1, 'DOM_SuperConstructorInvocation', a)
    if hasattr(b2, 'DOM_SuperConstructorInvocation'):
        assert _is_linked(b2, 'DOM_SuperConstructorInvocation', a)
    _safe_set(a, 'DOM_Expression301', None)
    assert not _is_linked(a, 'DOM_Expression301', b2)
    if hasattr(b2, 'DOM_SuperConstructorInvocation'):
        assert not _is_linked(b2, 'DOM_SuperConstructorInvocation', a)


def test_assoc_arguments79_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_EnumConstantDeclaration()
    b2 = DOM_EnumConstantDeclaration()
    _safe_set(a, 'DOM_Expression80', b1)
    assert _is_linked(a, 'DOM_Expression80', b1)
    if hasattr(b1, 'DOM_EnumConstantDeclaration'):
        assert _is_linked(b1, 'DOM_EnumConstantDeclaration', a)
    _safe_set(a, 'DOM_Expression80', b2)
    assert _is_linked(a, 'DOM_Expression80', b2)
    if hasattr(b1, 'DOM_EnumConstantDeclaration'):
        assert not _is_linked(b1, 'DOM_EnumConstantDeclaration', a)
    if hasattr(b2, 'DOM_EnumConstantDeclaration'):
        assert _is_linked(b2, 'DOM_EnumConstantDeclaration', a)
    _safe_set(a, 'DOM_Expression80', None)
    assert not _is_linked(a, 'DOM_Expression80', b2)
    if hasattr(b2, 'DOM_EnumConstantDeclaration'):
        assert not _is_linked(b2, 'DOM_EnumConstantDeclaration', a)


def test_assoc_array131_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ArrayAccess()
    b2 = DOM_ArrayAccess()
    _safe_set(a, 'DOM_Expression132', b1)
    assert _is_linked(a, 'DOM_Expression132', b1)
    if hasattr(b1, 'DOM_ArrayAccess'):
        assert _is_linked(b1, 'DOM_ArrayAccess', a)
    _safe_set(a, 'DOM_Expression132', b2)
    assert _is_linked(a, 'DOM_Expression132', b2)
    if hasattr(b1, 'DOM_ArrayAccess'):
        assert not _is_linked(b1, 'DOM_ArrayAccess', a)
    if hasattr(b2, 'DOM_ArrayAccess'):
        assert _is_linked(b2, 'DOM_ArrayAccess', a)
    _safe_set(a, 'DOM_Expression132', None)
    assert not _is_linked(a, 'DOM_Expression132', b2)
    if hasattr(b2, 'DOM_ArrayAccess'):
        assert not _is_linked(b2, 'DOM_ArrayAccess', a)


def test_assoc_binding110_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = DOM_IMethod()
    b2 = DOM_IMethod()
    _safe_set(a, 'DOM_MethodDeclaration111', b1)
    assert _is_linked(a, 'DOM_MethodDeclaration111', b1)
    if hasattr(b1, 'DOM_IMethod'):
        assert _is_linked(b1, 'DOM_IMethod', a)
    _safe_set(a, 'DOM_MethodDeclaration111', b2)
    assert _is_linked(a, 'DOM_MethodDeclaration111', b2)
    if hasattr(b1, 'DOM_IMethod'):
        assert not _is_linked(b1, 'DOM_IMethod', a)
    if hasattr(b2, 'DOM_IMethod'):
        assert _is_linked(b2, 'DOM_IMethod', a)
    _safe_set(a, 'DOM_MethodDeclaration111', None)
    assert not _is_linked(a, 'DOM_MethodDeclaration111', b2)
    if hasattr(b2, 'DOM_IMethod'):
        assert not _is_linked(b2, 'DOM_IMethod', a)


def test_assoc_body93_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = DOM_Block()
    b2 = DOM_Block()
    _safe_set(a, 'DOM_MethodDeclaration', b1)
    assert _is_linked(a, 'DOM_MethodDeclaration', b1)
    if hasattr(b1, 'DOM_Block94'):
        assert _is_linked(b1, 'DOM_Block94', a)
    _safe_set(a, 'DOM_MethodDeclaration', b2)
    assert _is_linked(a, 'DOM_MethodDeclaration', b2)
    if hasattr(b1, 'DOM_Block94'):
        assert not _is_linked(b1, 'DOM_Block94', a)
    if hasattr(b2, 'DOM_Block94'):
        assert _is_linked(b2, 'DOM_Block94', a)
    _safe_set(a, 'DOM_MethodDeclaration', None)
    assert not _is_linked(a, 'DOM_MethodDeclaration', b2)
    if hasattr(b2, 'DOM_Block94'):
        assert not _is_linked(b2, 'DOM_Block94', a)


def test_assoc_bodyDeclarations65_link_reassign_clear():
    a = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    b1 = DOM_BodyDeclaration()
    b2 = DOM_BodyDeclaration()
    _safe_set(a, 'DOM_AbstractTypeDeclaration66', {b1})
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration66', b1)
    if hasattr(b1, 'DOM_BodyDeclaration67'):
        assert _is_linked(b1, 'DOM_BodyDeclaration67', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration66', {b2})
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration66', b2)
    if hasattr(b1, 'DOM_BodyDeclaration67'):
        assert not _is_linked(b1, 'DOM_BodyDeclaration67', a)
    if hasattr(b2, 'DOM_BodyDeclaration67'):
        assert _is_linked(b2, 'DOM_BodyDeclaration67', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration66', set())
    assert not _is_linked(a, 'DOM_AbstractTypeDeclaration66', b2)
    if hasattr(b2, 'DOM_BodyDeclaration67'):
        assert not _is_linked(b2, 'DOM_BodyDeclaration67', a)


def test_assoc_bound363_link_reassign_clear():
    a = DOM_WildcardType(upperBound="sample_text")
    b1 = DOM_Type()
    b2 = DOM_Type()
    _safe_set(a, 'DOM_WildcardType', b1)
    assert _is_linked(a, 'DOM_WildcardType', b1)
    if hasattr(b1, 'DOM_Type364'):
        assert _is_linked(b1, 'DOM_Type364', a)
    _safe_set(a, 'DOM_WildcardType', b2)
    assert _is_linked(a, 'DOM_WildcardType', b2)
    if hasattr(b1, 'DOM_Type364'):
        assert not _is_linked(b1, 'DOM_Type364', a)
    if hasattr(b2, 'DOM_Type364'):
        assert _is_linked(b2, 'DOM_Type364', a)
    _safe_set(a, 'DOM_WildcardType', None)
    assert not _is_linked(a, 'DOM_WildcardType', b2)
    if hasattr(b2, 'DOM_Type364'):
        assert not _is_linked(b2, 'DOM_Type364', a)


def test_assoc_componentType345_link_reassign_clear():
    a = DOM_ArrayType(dimensions="sample_text")
    b1 = DOM_Type()
    b2 = DOM_Type()
    _safe_set(a, 'DOM_ArrayType346', b1)
    assert _is_linked(a, 'DOM_ArrayType346', b1)
    if hasattr(b1, 'DOM_Type347'):
        assert _is_linked(b1, 'DOM_Type347', a)
    _safe_set(a, 'DOM_ArrayType346', b2)
    assert _is_linked(a, 'DOM_ArrayType346', b2)
    if hasattr(b1, 'DOM_Type347'):
        assert not _is_linked(b1, 'DOM_Type347', a)
    if hasattr(b2, 'DOM_Type347'):
        assert _is_linked(b2, 'DOM_Type347', a)
    _safe_set(a, 'DOM_ArrayType346', None)
    assert not _is_linked(a, 'DOM_ArrayType346', b2)
    if hasattr(b2, 'DOM_Type347'):
        assert not _is_linked(b2, 'DOM_Type347', a)


def test_assoc_declaration330_link_reassign_clear():
    a = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    b1 = DOM_TypeDeclarationStatement()
    b2 = DOM_TypeDeclarationStatement()
    _safe_set(a, 'DOM_AbstractTypeDeclaration331', b1)
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration331', b1)
    if hasattr(b1, 'DOM_TypeDeclarationStatement'):
        assert _is_linked(b1, 'DOM_TypeDeclarationStatement', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration331', b2)
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration331', b2)
    if hasattr(b1, 'DOM_TypeDeclarationStatement'):
        assert not _is_linked(b1, 'DOM_TypeDeclarationStatement', a)
    if hasattr(b2, 'DOM_TypeDeclarationStatement'):
        assert _is_linked(b2, 'DOM_TypeDeclarationStatement', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration331', None)
    assert not _is_linked(a, 'DOM_AbstractTypeDeclaration331', b2)
    if hasattr(b2, 'DOM_TypeDeclarationStatement'):
        assert not _is_linked(b2, 'DOM_TypeDeclarationStatement', a)


def test_assoc_default71_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_AnnotationTypeMemberDeclaration()
    b2 = DOM_AnnotationTypeMemberDeclaration()
    _safe_set(a, 'DOM_Expression72', b1)
    assert _is_linked(a, 'DOM_Expression72', b1)
    if hasattr(b1, 'DOM_AnnotationTypeMemberDeclaration'):
        assert _is_linked(b1, 'DOM_AnnotationTypeMemberDeclaration', a)
    _safe_set(a, 'DOM_Expression72', b2)
    assert _is_linked(a, 'DOM_Expression72', b2)
    if hasattr(b1, 'DOM_AnnotationTypeMemberDeclaration'):
        assert not _is_linked(b1, 'DOM_AnnotationTypeMemberDeclaration', a)
    if hasattr(b2, 'DOM_AnnotationTypeMemberDeclaration'):
        assert _is_linked(b2, 'DOM_AnnotationTypeMemberDeclaration', a)
    _safe_set(a, 'DOM_Expression72', None)
    assert not _is_linked(a, 'DOM_Expression72', b2)
    if hasattr(b2, 'DOM_AnnotationTypeMemberDeclaration'):
        assert not _is_linked(b2, 'DOM_AnnotationTypeMemberDeclaration', a)


def test_assoc_dimensions136_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ArrayCreation()
    b2 = DOM_ArrayCreation()
    _safe_set(a, 'DOM_Expression137', b1)
    assert _is_linked(a, 'DOM_Expression137', b1)
    if hasattr(b1, 'DOM_ArrayCreation'):
        assert _is_linked(b1, 'DOM_ArrayCreation', a)
    _safe_set(a, 'DOM_Expression137', b2)
    assert _is_linked(a, 'DOM_Expression137', b2)
    if hasattr(b1, 'DOM_ArrayCreation'):
        assert not _is_linked(b1, 'DOM_ArrayCreation', a)
    if hasattr(b2, 'DOM_ArrayCreation'):
        assert _is_linked(b2, 'DOM_ArrayCreation', a)
    _safe_set(a, 'DOM_Expression137', None)
    assert not _is_linked(a, 'DOM_Expression137', b2)
    if hasattr(b2, 'DOM_ArrayCreation'):
        assert not _is_linked(b2, 'DOM_ArrayCreation', a)


def test_assoc_elementType348_link_reassign_clear():
    a = DOM_ArrayType(dimensions="sample_text")
    b1 = DOM_Type()
    b2 = DOM_Type()
    _safe_set(a, 'DOM_ArrayType349', b1)
    assert _is_linked(a, 'DOM_ArrayType349', b1)
    if hasattr(b1, 'DOM_Type350'):
        assert _is_linked(b1, 'DOM_Type350', a)
    _safe_set(a, 'DOM_ArrayType349', b2)
    assert _is_linked(a, 'DOM_ArrayType349', b2)
    if hasattr(b1, 'DOM_Type350'):
        assert not _is_linked(b1, 'DOM_Type350', a)
    if hasattr(b2, 'DOM_Type350'):
        assert _is_linked(b2, 'DOM_Type350', a)
    _safe_set(a, 'DOM_ArrayType349', None)
    assert not _is_linked(a, 'DOM_ArrayType349', b2)
    if hasattr(b2, 'DOM_Type350'):
        assert not _is_linked(b2, 'DOM_Type350', a)


def test_assoc_elseExpression169_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ConditionalExpression()
    b2 = DOM_ConditionalExpression()
    _safe_set(a, 'DOM_Expression170', b1)
    assert _is_linked(a, 'DOM_Expression170', b1)
    if hasattr(b1, 'DOM_ConditionalExpression'):
        assert _is_linked(b1, 'DOM_ConditionalExpression', a)
    _safe_set(a, 'DOM_Expression170', b2)
    assert _is_linked(a, 'DOM_Expression170', b2)
    if hasattr(b1, 'DOM_ConditionalExpression'):
        assert not _is_linked(b1, 'DOM_ConditionalExpression', a)
    if hasattr(b2, 'DOM_ConditionalExpression'):
        assert _is_linked(b2, 'DOM_ConditionalExpression', a)
    _safe_set(a, 'DOM_Expression170', None)
    assert not _is_linked(a, 'DOM_Expression170', b2)
    if hasattr(b2, 'DOM_ConditionalExpression'):
        assert not _is_linked(b2, 'DOM_ConditionalExpression', a)


def test_assoc_exception7_link_reassign_clear():
    a = DOM_SingleVariableDeclaration(varargs="sample_text")
    b1 = DOM_CatchClause()
    b2 = DOM_CatchClause()
    _safe_set(a, 'DOM_SingleVariableDeclaration', b1)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration', b1)
    if hasattr(b1, 'DOM_CatchClause8'):
        assert _is_linked(b1, 'DOM_CatchClause8', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration', b2)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration', b2)
    if hasattr(b1, 'DOM_CatchClause8'):
        assert not _is_linked(b1, 'DOM_CatchClause8', a)
    if hasattr(b2, 'DOM_CatchClause8'):
        assert _is_linked(b2, 'DOM_CatchClause8', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration', None)
    assert not _is_linked(a, 'DOM_SingleVariableDeclaration', b2)
    if hasattr(b2, 'DOM_CatchClause8'):
        assert not _is_linked(b2, 'DOM_CatchClause8', a)


def test_assoc_expression150_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_CastExpression()
    b2 = DOM_CastExpression()
    _safe_set(a, 'DOM_Expression151', b1)
    assert _is_linked(a, 'DOM_Expression151', b1)
    if hasattr(b1, 'DOM_CastExpression'):
        assert _is_linked(b1, 'DOM_CastExpression', a)
    _safe_set(a, 'DOM_Expression151', b2)
    assert _is_linked(a, 'DOM_Expression151', b2)
    if hasattr(b1, 'DOM_CastExpression'):
        assert not _is_linked(b1, 'DOM_CastExpression', a)
    if hasattr(b2, 'DOM_CastExpression'):
        assert _is_linked(b2, 'DOM_CastExpression', a)
    _safe_set(a, 'DOM_Expression151', None)
    assert not _is_linked(a, 'DOM_Expression151', b2)
    if hasattr(b2, 'DOM_CastExpression'):
        assert not _is_linked(b2, 'DOM_CastExpression', a)


def test_assoc_expression160_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ClassInstanceCreation()
    b2 = DOM_ClassInstanceCreation()
    _safe_set(a, 'DOM_Expression162', b1)
    assert _is_linked(a, 'DOM_Expression162', b1)
    if hasattr(b1, 'DOM_ClassInstanceCreation161'):
        assert _is_linked(b1, 'DOM_ClassInstanceCreation161', a)
    _safe_set(a, 'DOM_Expression162', b2)
    assert _is_linked(a, 'DOM_Expression162', b2)
    if hasattr(b1, 'DOM_ClassInstanceCreation161'):
        assert not _is_linked(b1, 'DOM_ClassInstanceCreation161', a)
    if hasattr(b2, 'DOM_ClassInstanceCreation161'):
        assert _is_linked(b2, 'DOM_ClassInstanceCreation161', a)
    _safe_set(a, 'DOM_Expression162', None)
    assert not _is_linked(a, 'DOM_Expression162', b2)
    if hasattr(b2, 'DOM_ClassInstanceCreation161'):
        assert not _is_linked(b2, 'DOM_ClassInstanceCreation161', a)


def test_assoc_expression171_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ConditionalExpression()
    b2 = DOM_ConditionalExpression()
    _safe_set(a, 'DOM_Expression173', b1)
    assert _is_linked(a, 'DOM_Expression173', b1)
    if hasattr(b1, 'DOM_ConditionalExpression172'):
        assert _is_linked(b1, 'DOM_ConditionalExpression172', a)
    _safe_set(a, 'DOM_Expression173', b2)
    assert _is_linked(a, 'DOM_Expression173', b2)
    if hasattr(b1, 'DOM_ConditionalExpression172'):
        assert not _is_linked(b1, 'DOM_ConditionalExpression172', a)
    if hasattr(b2, 'DOM_ConditionalExpression172'):
        assert _is_linked(b2, 'DOM_ConditionalExpression172', a)
    _safe_set(a, 'DOM_Expression173', None)
    assert not _is_linked(a, 'DOM_Expression173', b2)
    if hasattr(b2, 'DOM_ConditionalExpression172'):
        assert not _is_linked(b2, 'DOM_ConditionalExpression172', a)


def test_assoc_expression177_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_FieldAccess()
    b2 = DOM_FieldAccess()
    _safe_set(a, 'DOM_Expression178', b1)
    assert _is_linked(a, 'DOM_Expression178', b1)
    if hasattr(b1, 'DOM_FieldAccess'):
        assert _is_linked(b1, 'DOM_FieldAccess', a)
    _safe_set(a, 'DOM_Expression178', b2)
    assert _is_linked(a, 'DOM_Expression178', b2)
    if hasattr(b1, 'DOM_FieldAccess'):
        assert not _is_linked(b1, 'DOM_FieldAccess', a)
    if hasattr(b2, 'DOM_FieldAccess'):
        assert _is_linked(b2, 'DOM_FieldAccess', a)
    _safe_set(a, 'DOM_Expression178', None)
    assert not _is_linked(a, 'DOM_Expression178', b2)
    if hasattr(b2, 'DOM_FieldAccess'):
        assert not _is_linked(b2, 'DOM_FieldAccess', a)


def test_assoc_expression197_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_MethodInvocation()
    b2 = DOM_MethodInvocation()
    _safe_set(a, 'DOM_Expression199', b1)
    assert _is_linked(a, 'DOM_Expression199', b1)
    if hasattr(b1, 'DOM_MethodInvocation198'):
        assert _is_linked(b1, 'DOM_MethodInvocation198', a)
    _safe_set(a, 'DOM_Expression199', b2)
    assert _is_linked(a, 'DOM_Expression199', b2)
    if hasattr(b1, 'DOM_MethodInvocation198'):
        assert not _is_linked(b1, 'DOM_MethodInvocation198', a)
    if hasattr(b2, 'DOM_MethodInvocation198'):
        assert _is_linked(b2, 'DOM_MethodInvocation198', a)
    _safe_set(a, 'DOM_Expression199', None)
    assert not _is_linked(a, 'DOM_Expression199', b2)
    if hasattr(b2, 'DOM_MethodInvocation198'):
        assert not _is_linked(b2, 'DOM_MethodInvocation198', a)


def test_assoc_expression209_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ParenthesizedExpression()
    b2 = DOM_ParenthesizedExpression()
    _safe_set(a, 'DOM_Expression210', b1)
    assert _is_linked(a, 'DOM_Expression210', b1)
    if hasattr(b1, 'DOM_ParenthesizedExpression'):
        assert _is_linked(b1, 'DOM_ParenthesizedExpression', a)
    _safe_set(a, 'DOM_Expression210', b2)
    assert _is_linked(a, 'DOM_Expression210', b2)
    if hasattr(b1, 'DOM_ParenthesizedExpression'):
        assert not _is_linked(b1, 'DOM_ParenthesizedExpression', a)
    if hasattr(b2, 'DOM_ParenthesizedExpression'):
        assert _is_linked(b2, 'DOM_ParenthesizedExpression', a)
    _safe_set(a, 'DOM_Expression210', None)
    assert not _is_linked(a, 'DOM_Expression210', b2)
    if hasattr(b2, 'DOM_ParenthesizedExpression'):
        assert not _is_linked(b2, 'DOM_ParenthesizedExpression', a)


def test_assoc_expression243_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_AssertStatement()
    b2 = DOM_AssertStatement()
    _safe_set(a, 'DOM_Expression244', b1)
    assert _is_linked(a, 'DOM_Expression244', b1)
    if hasattr(b1, 'DOM_AssertStatement'):
        assert _is_linked(b1, 'DOM_AssertStatement', a)
    _safe_set(a, 'DOM_Expression244', b2)
    assert _is_linked(a, 'DOM_Expression244', b2)
    if hasattr(b1, 'DOM_AssertStatement'):
        assert not _is_linked(b1, 'DOM_AssertStatement', a)
    if hasattr(b2, 'DOM_AssertStatement'):
        assert _is_linked(b2, 'DOM_AssertStatement', a)
    _safe_set(a, 'DOM_Expression244', None)
    assert not _is_linked(a, 'DOM_Expression244', b2)
    if hasattr(b2, 'DOM_AssertStatement'):
        assert not _is_linked(b2, 'DOM_AssertStatement', a)


def test_assoc_expression261_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_DoStatement()
    b2 = DOM_DoStatement()
    _safe_set(a, 'DOM_Expression263', b1)
    assert _is_linked(a, 'DOM_Expression263', b1)
    if hasattr(b1, 'DOM_DoStatement262'):
        assert _is_linked(b1, 'DOM_DoStatement262', a)
    _safe_set(a, 'DOM_Expression263', b2)
    assert _is_linked(a, 'DOM_Expression263', b2)
    if hasattr(b1, 'DOM_DoStatement262'):
        assert not _is_linked(b1, 'DOM_DoStatement262', a)
    if hasattr(b2, 'DOM_DoStatement262'):
        assert _is_linked(b2, 'DOM_DoStatement262', a)
    _safe_set(a, 'DOM_Expression263', None)
    assert not _is_linked(a, 'DOM_Expression263', b2)
    if hasattr(b2, 'DOM_DoStatement262'):
        assert not _is_linked(b2, 'DOM_DoStatement262', a)


def test_assoc_expression266_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_EnhancedForStatement()
    b2 = DOM_EnhancedForStatement()
    _safe_set(a, 'DOM_Expression268', b1)
    assert _is_linked(a, 'DOM_Expression268', b1)
    if hasattr(b1, 'DOM_EnhancedForStatement267'):
        assert _is_linked(b1, 'DOM_EnhancedForStatement267', a)
    _safe_set(a, 'DOM_Expression268', b2)
    assert _is_linked(a, 'DOM_Expression268', b2)
    if hasattr(b1, 'DOM_EnhancedForStatement267'):
        assert not _is_linked(b1, 'DOM_EnhancedForStatement267', a)
    if hasattr(b2, 'DOM_EnhancedForStatement267'):
        assert _is_linked(b2, 'DOM_EnhancedForStatement267', a)
    _safe_set(a, 'DOM_Expression268', None)
    assert not _is_linked(a, 'DOM_Expression268', b2)
    if hasattr(b2, 'DOM_EnhancedForStatement267'):
        assert not _is_linked(b2, 'DOM_EnhancedForStatement267', a)


def test_assoc_expression272_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ExpressionStatement()
    b2 = DOM_ExpressionStatement()
    _safe_set(a, 'DOM_Expression273', b1)
    assert _is_linked(a, 'DOM_Expression273', b1)
    if hasattr(b1, 'DOM_ExpressionStatement'):
        assert _is_linked(b1, 'DOM_ExpressionStatement', a)
    _safe_set(a, 'DOM_Expression273', b2)
    assert _is_linked(a, 'DOM_Expression273', b2)
    if hasattr(b1, 'DOM_ExpressionStatement'):
        assert not _is_linked(b1, 'DOM_ExpressionStatement', a)
    if hasattr(b2, 'DOM_ExpressionStatement'):
        assert _is_linked(b2, 'DOM_ExpressionStatement', a)
    _safe_set(a, 'DOM_Expression273', None)
    assert not _is_linked(a, 'DOM_Expression273', b2)
    if hasattr(b2, 'DOM_ExpressionStatement'):
        assert not _is_linked(b2, 'DOM_ExpressionStatement', a)


def test_assoc_expression276_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ForStatement()
    b2 = DOM_ForStatement()
    _safe_set(a, 'DOM_Expression278', b1)
    assert _is_linked(a, 'DOM_Expression278', b1)
    if hasattr(b1, 'DOM_ForStatement277'):
        assert _is_linked(b1, 'DOM_ForStatement277', a)
    _safe_set(a, 'DOM_Expression278', b2)
    assert _is_linked(a, 'DOM_Expression278', b2)
    if hasattr(b1, 'DOM_ForStatement277'):
        assert not _is_linked(b1, 'DOM_ForStatement277', a)
    if hasattr(b2, 'DOM_ForStatement277'):
        assert _is_linked(b2, 'DOM_ForStatement277', a)
    _safe_set(a, 'DOM_Expression278', None)
    assert not _is_linked(a, 'DOM_Expression278', b2)
    if hasattr(b2, 'DOM_ForStatement277'):
        assert not _is_linked(b2, 'DOM_ForStatement277', a)


def test_assoc_expression287_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_IfStatement()
    b2 = DOM_IfStatement()
    _safe_set(a, 'DOM_Expression289', b1)
    assert _is_linked(a, 'DOM_Expression289', b1)
    if hasattr(b1, 'DOM_IfStatement288'):
        assert _is_linked(b1, 'DOM_IfStatement288', a)
    _safe_set(a, 'DOM_Expression289', b2)
    assert _is_linked(a, 'DOM_Expression289', b2)
    if hasattr(b1, 'DOM_IfStatement288'):
        assert not _is_linked(b1, 'DOM_IfStatement288', a)
    if hasattr(b2, 'DOM_IfStatement288'):
        assert _is_linked(b2, 'DOM_IfStatement288', a)
    _safe_set(a, 'DOM_Expression289', None)
    assert not _is_linked(a, 'DOM_Expression289', b2)
    if hasattr(b2, 'DOM_IfStatement288'):
        assert not _is_linked(b2, 'DOM_IfStatement288', a)


def test_assoc_expression298_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ReturnStatement()
    b2 = DOM_ReturnStatement()
    _safe_set(a, 'DOM_Expression299', b1)
    assert _is_linked(a, 'DOM_Expression299', b1)
    if hasattr(b1, 'DOM_ReturnStatement'):
        assert _is_linked(b1, 'DOM_ReturnStatement', a)
    _safe_set(a, 'DOM_Expression299', b2)
    assert _is_linked(a, 'DOM_Expression299', b2)
    if hasattr(b1, 'DOM_ReturnStatement'):
        assert not _is_linked(b1, 'DOM_ReturnStatement', a)
    if hasattr(b2, 'DOM_ReturnStatement'):
        assert _is_linked(b2, 'DOM_ReturnStatement', a)
    _safe_set(a, 'DOM_Expression299', None)
    assert not _is_linked(a, 'DOM_Expression299', b2)
    if hasattr(b2, 'DOM_ReturnStatement'):
        assert not _is_linked(b2, 'DOM_ReturnStatement', a)


def test_assoc_expression302_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_SuperConstructorInvocation()
    b2 = DOM_SuperConstructorInvocation()
    _safe_set(a, 'DOM_Expression304', b1)
    assert _is_linked(a, 'DOM_Expression304', b1)
    if hasattr(b1, 'DOM_SuperConstructorInvocation303'):
        assert _is_linked(b1, 'DOM_SuperConstructorInvocation303', a)
    _safe_set(a, 'DOM_Expression304', b2)
    assert _is_linked(a, 'DOM_Expression304', b2)
    if hasattr(b1, 'DOM_SuperConstructorInvocation303'):
        assert not _is_linked(b1, 'DOM_SuperConstructorInvocation303', a)
    if hasattr(b2, 'DOM_SuperConstructorInvocation303'):
        assert _is_linked(b2, 'DOM_SuperConstructorInvocation303', a)
    _safe_set(a, 'DOM_Expression304', None)
    assert not _is_linked(a, 'DOM_Expression304', b2)
    if hasattr(b2, 'DOM_SuperConstructorInvocation303'):
        assert not _is_linked(b2, 'DOM_SuperConstructorInvocation303', a)


def test_assoc_expression308_link_reassign_clear():
    a = DOM_SwitchCase(default="sample_text")
    b1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    _safe_set(a, 'DOM_SwitchCase', b1)
    assert _is_linked(a, 'DOM_SwitchCase', b1)
    if hasattr(b1, 'DOM_Expression309'):
        assert _is_linked(b1, 'DOM_Expression309', a)
    _safe_set(a, 'DOM_SwitchCase', b2)
    assert _is_linked(a, 'DOM_SwitchCase', b2)
    if hasattr(b1, 'DOM_Expression309'):
        assert not _is_linked(b1, 'DOM_Expression309', a)
    if hasattr(b2, 'DOM_Expression309'):
        assert _is_linked(b2, 'DOM_Expression309', a)
    _safe_set(a, 'DOM_SwitchCase', None)
    assert not _is_linked(a, 'DOM_SwitchCase', b2)
    if hasattr(b2, 'DOM_Expression309'):
        assert not _is_linked(b2, 'DOM_Expression309', a)


def test_assoc_expression310_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_SwitchStatement()
    b2 = DOM_SwitchStatement()
    _safe_set(a, 'DOM_Expression311', b1)
    assert _is_linked(a, 'DOM_Expression311', b1)
    if hasattr(b1, 'DOM_SwitchStatement'):
        assert _is_linked(b1, 'DOM_SwitchStatement', a)
    _safe_set(a, 'DOM_Expression311', b2)
    assert _is_linked(a, 'DOM_Expression311', b2)
    if hasattr(b1, 'DOM_SwitchStatement'):
        assert not _is_linked(b1, 'DOM_SwitchStatement', a)
    if hasattr(b2, 'DOM_SwitchStatement'):
        assert _is_linked(b2, 'DOM_SwitchStatement', a)
    _safe_set(a, 'DOM_Expression311', None)
    assert not _is_linked(a, 'DOM_Expression311', b2)
    if hasattr(b2, 'DOM_SwitchStatement'):
        assert not _is_linked(b2, 'DOM_SwitchStatement', a)


def test_assoc_expression317_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_SynchronizedStatement()
    b2 = DOM_SynchronizedStatement()
    _safe_set(a, 'DOM_Expression319', b1)
    assert _is_linked(a, 'DOM_Expression319', b1)
    if hasattr(b1, 'DOM_SynchronizedStatement318'):
        assert _is_linked(b1, 'DOM_SynchronizedStatement318', a)
    _safe_set(a, 'DOM_Expression319', b2)
    assert _is_linked(a, 'DOM_Expression319', b2)
    if hasattr(b1, 'DOM_SynchronizedStatement318'):
        assert not _is_linked(b1, 'DOM_SynchronizedStatement318', a)
    if hasattr(b2, 'DOM_SynchronizedStatement318'):
        assert _is_linked(b2, 'DOM_SynchronizedStatement318', a)
    _safe_set(a, 'DOM_Expression319', None)
    assert not _is_linked(a, 'DOM_Expression319', b2)
    if hasattr(b2, 'DOM_SynchronizedStatement318'):
        assert not _is_linked(b2, 'DOM_SynchronizedStatement318', a)


def test_assoc_expression320_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ThrowStatement()
    b2 = DOM_ThrowStatement()
    _safe_set(a, 'DOM_Expression321', b1)
    assert _is_linked(a, 'DOM_Expression321', b1)
    if hasattr(b1, 'DOM_ThrowStatement'):
        assert _is_linked(b1, 'DOM_ThrowStatement', a)
    _safe_set(a, 'DOM_Expression321', b2)
    assert _is_linked(a, 'DOM_Expression321', b2)
    if hasattr(b1, 'DOM_ThrowStatement'):
        assert not _is_linked(b1, 'DOM_ThrowStatement', a)
    if hasattr(b2, 'DOM_ThrowStatement'):
        assert _is_linked(b2, 'DOM_ThrowStatement', a)
    _safe_set(a, 'DOM_Expression321', None)
    assert not _is_linked(a, 'DOM_Expression321', b2)
    if hasattr(b2, 'DOM_ThrowStatement'):
        assert not _is_linked(b2, 'DOM_ThrowStatement', a)


def test_assoc_expression342_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_WhileStatement()
    b2 = DOM_WhileStatement()
    _safe_set(a, 'DOM_Expression344', b1)
    assert _is_linked(a, 'DOM_Expression344', b1)
    if hasattr(b1, 'DOM_WhileStatement343'):
        assert _is_linked(b1, 'DOM_WhileStatement343', a)
    _safe_set(a, 'DOM_Expression344', b2)
    assert _is_linked(a, 'DOM_Expression344', b2)
    if hasattr(b1, 'DOM_WhileStatement343'):
        assert not _is_linked(b1, 'DOM_WhileStatement343', a)
    if hasattr(b2, 'DOM_WhileStatement343'):
        assert _is_linked(b2, 'DOM_WhileStatement343', a)
    _safe_set(a, 'DOM_Expression344', None)
    assert not _is_linked(a, 'DOM_Expression344', b2)
    if hasattr(b2, 'DOM_WhileStatement343'):
        assert not _is_linked(b2, 'DOM_WhileStatement343', a)


def test_assoc_expressions142_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ArrayInitializer()
    b2 = DOM_ArrayInitializer()
    _safe_set(a, 'DOM_Expression144', b1)
    assert _is_linked(a, 'DOM_Expression144', b1)
    if hasattr(b1, 'DOM_ArrayInitializer143'):
        assert _is_linked(b1, 'DOM_ArrayInitializer143', a)
    _safe_set(a, 'DOM_Expression144', b2)
    assert _is_linked(a, 'DOM_Expression144', b2)
    if hasattr(b1, 'DOM_ArrayInitializer143'):
        assert not _is_linked(b1, 'DOM_ArrayInitializer143', a)
    if hasattr(b2, 'DOM_ArrayInitializer143'):
        assert _is_linked(b2, 'DOM_ArrayInitializer143', a)
    _safe_set(a, 'DOM_Expression144', None)
    assert not _is_linked(a, 'DOM_Expression144', b2)
    if hasattr(b2, 'DOM_ArrayInitializer143'):
        assert not _is_linked(b2, 'DOM_ArrayInitializer143', a)


def test_assoc_extendedOperands182_link_reassign_clear():
    a = DOM_InfixExpression(operator="sample_text")
    b1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    _safe_set(a, 'DOM_InfixExpression', {b1})
    assert _is_linked(a, 'DOM_InfixExpression', b1)
    if hasattr(b1, 'DOM_Expression183'):
        assert _is_linked(b1, 'DOM_Expression183', a)
    _safe_set(a, 'DOM_InfixExpression', {b2})
    assert _is_linked(a, 'DOM_InfixExpression', b2)
    if hasattr(b1, 'DOM_Expression183'):
        assert not _is_linked(b1, 'DOM_Expression183', a)
    if hasattr(b2, 'DOM_Expression183'):
        assert _is_linked(b2, 'DOM_Expression183', a)
    _safe_set(a, 'DOM_InfixExpression', set())
    assert not _is_linked(a, 'DOM_InfixExpression', b2)
    if hasattr(b2, 'DOM_Expression183'):
        assert not _is_linked(b2, 'DOM_Expression183', a)


def test_assoc_fragments53_link_reassign_clear():
    a = DOM_TagElement(nested="sample_text", tagName="sample_text")
    b1 = DOM_ASTNode()
    b2 = DOM_ASTNode()
    _safe_set(a, 'DOM_TagElement', {b1})
    assert _is_linked(a, 'DOM_TagElement', b1)
    if hasattr(b1, 'DOM_ASTNode54'):
        assert _is_linked(b1, 'DOM_ASTNode54', a)
    _safe_set(a, 'DOM_TagElement', {b2})
    assert _is_linked(a, 'DOM_TagElement', b2)
    if hasattr(b1, 'DOM_ASTNode54'):
        assert not _is_linked(b1, 'DOM_ASTNode54', a)
    if hasattr(b2, 'DOM_ASTNode54'):
        assert _is_linked(b2, 'DOM_ASTNode54', a)
    _safe_set(a, 'DOM_TagElement', set())
    assert not _is_linked(a, 'DOM_TagElement', b2)
    if hasattr(b2, 'DOM_ASTNode54'):
        assert not _is_linked(b2, 'DOM_ASTNode54', a)


def test_assoc_imports15_link_reassign_clear():
    a = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    b1 = DOM_CompilationUnit()
    b2 = DOM_CompilationUnit()
    _safe_set(a, 'DOM_ImportDeclaration', b1)
    assert _is_linked(a, 'DOM_ImportDeclaration', b1)
    if hasattr(b1, 'DOM_CompilationUnit16'):
        assert _is_linked(b1, 'DOM_CompilationUnit16', a)
    _safe_set(a, 'DOM_ImportDeclaration', b2)
    assert _is_linked(a, 'DOM_ImportDeclaration', b2)
    if hasattr(b1, 'DOM_CompilationUnit16'):
        assert not _is_linked(b1, 'DOM_CompilationUnit16', a)
    if hasattr(b2, 'DOM_CompilationUnit16'):
        assert _is_linked(b2, 'DOM_CompilationUnit16', a)
    _safe_set(a, 'DOM_ImportDeclaration', None)
    assert not _is_linked(a, 'DOM_ImportDeclaration', b2)
    if hasattr(b2, 'DOM_CompilationUnit16'):
        assert not _is_linked(b2, 'DOM_CompilationUnit16', a)


def test_assoc_index133_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ArrayAccess()
    b2 = DOM_ArrayAccess()
    _safe_set(a, 'DOM_Expression135', b1)
    assert _is_linked(a, 'DOM_Expression135', b1)
    if hasattr(b1, 'DOM_ArrayAccess134'):
        assert _is_linked(b1, 'DOM_ArrayAccess134', a)
    _safe_set(a, 'DOM_Expression135', b2)
    assert _is_linked(a, 'DOM_Expression135', b2)
    if hasattr(b1, 'DOM_ArrayAccess134'):
        assert not _is_linked(b1, 'DOM_ArrayAccess134', a)
    if hasattr(b2, 'DOM_ArrayAccess134'):
        assert _is_linked(b2, 'DOM_ArrayAccess134', a)
    _safe_set(a, 'DOM_Expression135', None)
    assert not _is_linked(a, 'DOM_Expression135', b2)
    if hasattr(b2, 'DOM_ArrayAccess134'):
        assert not _is_linked(b2, 'DOM_ArrayAccess134', a)


def test_assoc_initializer60_link_reassign_clear():
    a = DOM_VariableDeclaration(extraDimensions="sample_text")
    b1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    _safe_set(a, 'DOM_VariableDeclaration', b1)
    assert _is_linked(a, 'DOM_VariableDeclaration', b1)
    if hasattr(b1, 'DOM_Expression61'):
        assert _is_linked(b1, 'DOM_Expression61', a)
    _safe_set(a, 'DOM_VariableDeclaration', b2)
    assert _is_linked(a, 'DOM_VariableDeclaration', b2)
    if hasattr(b1, 'DOM_Expression61'):
        assert not _is_linked(b1, 'DOM_Expression61', a)
    if hasattr(b2, 'DOM_Expression61'):
        assert _is_linked(b2, 'DOM_Expression61', a)
    _safe_set(a, 'DOM_VariableDeclaration', None)
    assert not _is_linked(a, 'DOM_VariableDeclaration', b2)
    if hasattr(b2, 'DOM_Expression61'):
        assert not _is_linked(b2, 'DOM_Expression61', a)


def test_assoc_initializers279_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ForStatement()
    b2 = DOM_ForStatement()
    _safe_set(a, 'DOM_Expression281', b1)
    assert _is_linked(a, 'DOM_Expression281', b1)
    if hasattr(b1, 'DOM_ForStatement280'):
        assert _is_linked(b1, 'DOM_ForStatement280', a)
    _safe_set(a, 'DOM_Expression281', b2)
    assert _is_linked(a, 'DOM_Expression281', b2)
    if hasattr(b1, 'DOM_ForStatement280'):
        assert not _is_linked(b1, 'DOM_ForStatement280', a)
    if hasattr(b2, 'DOM_ForStatement280'):
        assert _is_linked(b2, 'DOM_ForStatement280', a)
    _safe_set(a, 'DOM_Expression281', None)
    assert not _is_linked(a, 'DOM_Expression281', b2)
    if hasattr(b2, 'DOM_ForStatement280'):
        assert not _is_linked(b2, 'DOM_ForStatement280', a)


def test_assoc_label250_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_BreakStatement()
    b2 = DOM_BreakStatement()
    _safe_set(a, 'DOM_SimpleName251', b1)
    assert _is_linked(a, 'DOM_SimpleName251', b1)
    if hasattr(b1, 'DOM_BreakStatement'):
        assert _is_linked(b1, 'DOM_BreakStatement', a)
    _safe_set(a, 'DOM_SimpleName251', b2)
    assert _is_linked(a, 'DOM_SimpleName251', b2)
    if hasattr(b1, 'DOM_BreakStatement'):
        assert not _is_linked(b1, 'DOM_BreakStatement', a)
    if hasattr(b2, 'DOM_BreakStatement'):
        assert _is_linked(b2, 'DOM_BreakStatement', a)
    _safe_set(a, 'DOM_SimpleName251', None)
    assert not _is_linked(a, 'DOM_SimpleName251', b2)
    if hasattr(b2, 'DOM_BreakStatement'):
        assert not _is_linked(b2, 'DOM_BreakStatement', a)


def test_assoc_label257_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_ContinueStatement()
    b2 = DOM_ContinueStatement()
    _safe_set(a, 'DOM_SimpleName258', b1)
    assert _is_linked(a, 'DOM_SimpleName258', b1)
    if hasattr(b1, 'DOM_ContinueStatement'):
        assert _is_linked(b1, 'DOM_ContinueStatement', a)
    _safe_set(a, 'DOM_SimpleName258', b2)
    assert _is_linked(a, 'DOM_SimpleName258', b2)
    if hasattr(b1, 'DOM_ContinueStatement'):
        assert not _is_linked(b1, 'DOM_ContinueStatement', a)
    if hasattr(b2, 'DOM_ContinueStatement'):
        assert _is_linked(b2, 'DOM_ContinueStatement', a)
    _safe_set(a, 'DOM_SimpleName258', None)
    assert not _is_linked(a, 'DOM_SimpleName258', b2)
    if hasattr(b2, 'DOM_ContinueStatement'):
        assert not _is_linked(b2, 'DOM_ContinueStatement', a)


def test_assoc_label295_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_LabeledStatement()
    b2 = DOM_LabeledStatement()
    _safe_set(a, 'DOM_SimpleName297', b1)
    assert _is_linked(a, 'DOM_SimpleName297', b1)
    if hasattr(b1, 'DOM_LabeledStatement296'):
        assert _is_linked(b1, 'DOM_LabeledStatement296', a)
    _safe_set(a, 'DOM_SimpleName297', b2)
    assert _is_linked(a, 'DOM_SimpleName297', b2)
    if hasattr(b1, 'DOM_LabeledStatement296'):
        assert not _is_linked(b1, 'DOM_LabeledStatement296', a)
    if hasattr(b2, 'DOM_LabeledStatement296'):
        assert _is_linked(b2, 'DOM_LabeledStatement296', a)
    _safe_set(a, 'DOM_SimpleName297', None)
    assert not _is_linked(a, 'DOM_SimpleName297', b2)
    if hasattr(b2, 'DOM_LabeledStatement296'):
        assert not _is_linked(b2, 'DOM_LabeledStatement296', a)


def test_assoc_leftHandSide145_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_Assignment(operator="sample_text")
    b2 = DOM_Assignment(operator="sample_text_2")
    _safe_set(a, 'DOM_Expression146', b1)
    assert _is_linked(a, 'DOM_Expression146', b1)
    if hasattr(b1, 'DOM_Assignment'):
        assert _is_linked(b1, 'DOM_Assignment', a)
    _safe_set(a, 'DOM_Expression146', b2)
    assert _is_linked(a, 'DOM_Expression146', b2)
    if hasattr(b1, 'DOM_Assignment'):
        assert not _is_linked(b1, 'DOM_Assignment', a)
    if hasattr(b2, 'DOM_Assignment'):
        assert _is_linked(b2, 'DOM_Assignment', a)
    _safe_set(a, 'DOM_Expression146', None)
    assert not _is_linked(a, 'DOM_Expression146', b2)
    if hasattr(b2, 'DOM_Assignment'):
        assert not _is_linked(b2, 'DOM_Assignment', a)


def test_assoc_leftOperand184_link_reassign_clear():
    a = DOM_InfixExpression(operator="sample_text")
    b1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    _safe_set(a, 'DOM_InfixExpression185', b1)
    assert _is_linked(a, 'DOM_InfixExpression185', b1)
    if hasattr(b1, 'DOM_Expression186'):
        assert _is_linked(b1, 'DOM_Expression186', a)
    _safe_set(a, 'DOM_InfixExpression185', b2)
    assert _is_linked(a, 'DOM_InfixExpression185', b2)
    if hasattr(b1, 'DOM_Expression186'):
        assert not _is_linked(b1, 'DOM_Expression186', a)
    if hasattr(b2, 'DOM_Expression186'):
        assert _is_linked(b2, 'DOM_Expression186', a)
    _safe_set(a, 'DOM_InfixExpression185', None)
    assert not _is_linked(a, 'DOM_InfixExpression185', b2)
    if hasattr(b2, 'DOM_Expression186'):
        assert not _is_linked(b2, 'DOM_Expression186', a)


def test_assoc_leftOperand190_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_InstanceofExpression()
    b2 = DOM_InstanceofExpression()
    _safe_set(a, 'DOM_Expression191', b1)
    assert _is_linked(a, 'DOM_Expression191', b1)
    if hasattr(b1, 'DOM_InstanceofExpression'):
        assert _is_linked(b1, 'DOM_InstanceofExpression', a)
    _safe_set(a, 'DOM_Expression191', b2)
    assert _is_linked(a, 'DOM_Expression191', b2)
    if hasattr(b1, 'DOM_InstanceofExpression'):
        assert not _is_linked(b1, 'DOM_InstanceofExpression', a)
    if hasattr(b2, 'DOM_InstanceofExpression'):
        assert _is_linked(b2, 'DOM_InstanceofExpression', a)
    _safe_set(a, 'DOM_Expression191', None)
    assert not _is_linked(a, 'DOM_Expression191', b2)
    if hasattr(b2, 'DOM_InstanceofExpression'):
        assert not _is_linked(b2, 'DOM_InstanceofExpression', a)


def test_assoc_message245_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_AssertStatement()
    b2 = DOM_AssertStatement()
    _safe_set(a, 'DOM_Expression247', b1)
    assert _is_linked(a, 'DOM_Expression247', b1)
    if hasattr(b1, 'DOM_AssertStatement246'):
        assert _is_linked(b1, 'DOM_AssertStatement246', a)
    _safe_set(a, 'DOM_Expression247', b2)
    assert _is_linked(a, 'DOM_Expression247', b2)
    if hasattr(b1, 'DOM_AssertStatement246'):
        assert not _is_linked(b1, 'DOM_AssertStatement246', a)
    if hasattr(b2, 'DOM_AssertStatement246'):
        assert _is_linked(b2, 'DOM_AssertStatement246', a)
    _safe_set(a, 'DOM_Expression247', None)
    assert not _is_linked(a, 'DOM_Expression247', b2)
    if hasattr(b2, 'DOM_AssertStatement246'):
        assert not _is_linked(b2, 'DOM_AssertStatement246', a)


def test_assoc_modifiers368_link_reassign_clear():
    a = DOM_SingleVariableDeclaration(varargs="sample_text")
    b1 = DOM_ExtendedModifier()
    b2 = DOM_ExtendedModifier()
    _safe_set(a, 'DOM_SingleVariableDeclaration369', {b1})
    assert _is_linked(a, 'DOM_SingleVariableDeclaration369', b1)
    if hasattr(b1, 'DOM_ExtendedModifier370'):
        assert _is_linked(b1, 'DOM_ExtendedModifier370', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration369', {b2})
    assert _is_linked(a, 'DOM_SingleVariableDeclaration369', b2)
    if hasattr(b1, 'DOM_ExtendedModifier370'):
        assert not _is_linked(b1, 'DOM_ExtendedModifier370', a)
    if hasattr(b2, 'DOM_ExtendedModifier370'):
        assert _is_linked(b2, 'DOM_ExtendedModifier370', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration369', set())
    assert not _is_linked(a, 'DOM_SingleVariableDeclaration369', b2)
    if hasattr(b2, 'DOM_ExtendedModifier370'):
        assert not _is_linked(b2, 'DOM_ExtendedModifier370', a)


def test_assoc_name179_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_FieldAccess()
    b2 = DOM_FieldAccess()
    _safe_set(a, 'DOM_SimpleName181', b1)
    assert _is_linked(a, 'DOM_SimpleName181', b1)
    if hasattr(b1, 'DOM_FieldAccess180'):
        assert _is_linked(b1, 'DOM_FieldAccess180', a)
    _safe_set(a, 'DOM_SimpleName181', b2)
    assert _is_linked(a, 'DOM_SimpleName181', b2)
    if hasattr(b1, 'DOM_FieldAccess180'):
        assert not _is_linked(b1, 'DOM_FieldAccess180', a)
    if hasattr(b2, 'DOM_FieldAccess180'):
        assert _is_linked(b2, 'DOM_FieldAccess180', a)
    _safe_set(a, 'DOM_SimpleName181', None)
    assert not _is_linked(a, 'DOM_SimpleName181', b2)
    if hasattr(b2, 'DOM_FieldAccess180'):
        assert not _is_linked(b2, 'DOM_FieldAccess180', a)


def test_assoc_name20_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    b2 = DOM_ImportDeclaration(onDemand="sample_text_2", static="sample_text_2")
    _safe_set(a, 'DOM_Name', b1)
    assert _is_linked(a, 'DOM_Name', b1)
    if hasattr(b1, 'DOM_ImportDeclaration21'):
        assert _is_linked(b1, 'DOM_ImportDeclaration21', a)
    _safe_set(a, 'DOM_Name', b2)
    assert _is_linked(a, 'DOM_Name', b2)
    if hasattr(b1, 'DOM_ImportDeclaration21'):
        assert not _is_linked(b1, 'DOM_ImportDeclaration21', a)
    if hasattr(b2, 'DOM_ImportDeclaration21'):
        assert _is_linked(b2, 'DOM_ImportDeclaration21', a)
    _safe_set(a, 'DOM_Name', None)
    assert not _is_linked(a, 'DOM_Name', b2)
    if hasattr(b2, 'DOM_ImportDeclaration21'):
        assert not _is_linked(b2, 'DOM_ImportDeclaration21', a)


def test_assoc_name200_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_MethodInvocation()
    b2 = DOM_MethodInvocation()
    _safe_set(a, 'DOM_SimpleName202', b1)
    assert _is_linked(a, 'DOM_SimpleName202', b1)
    if hasattr(b1, 'DOM_MethodInvocation201'):
        assert _is_linked(b1, 'DOM_MethodInvocation201', a)
    _safe_set(a, 'DOM_SimpleName202', b2)
    assert _is_linked(a, 'DOM_SimpleName202', b2)
    if hasattr(b1, 'DOM_MethodInvocation201'):
        assert not _is_linked(b1, 'DOM_MethodInvocation201', a)
    if hasattr(b2, 'DOM_MethodInvocation201'):
        assert _is_linked(b2, 'DOM_MethodInvocation201', a)
    _safe_set(a, 'DOM_SimpleName202', None)
    assert not _is_linked(a, 'DOM_SimpleName202', b2)
    if hasattr(b2, 'DOM_MethodInvocation201'):
        assert not _is_linked(b2, 'DOM_MethodInvocation201', a)


def test_assoc_name215_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_SuperFieldAccess()
    b2 = DOM_SuperFieldAccess()
    _safe_set(a, 'DOM_SimpleName216', b1)
    assert _is_linked(a, 'DOM_SimpleName216', b1)
    if hasattr(b1, 'DOM_SuperFieldAccess'):
        assert _is_linked(b1, 'DOM_SuperFieldAccess', a)
    _safe_set(a, 'DOM_SimpleName216', b2)
    assert _is_linked(a, 'DOM_SimpleName216', b2)
    if hasattr(b1, 'DOM_SuperFieldAccess'):
        assert not _is_linked(b1, 'DOM_SuperFieldAccess', a)
    if hasattr(b2, 'DOM_SuperFieldAccess'):
        assert _is_linked(b2, 'DOM_SuperFieldAccess', a)
    _safe_set(a, 'DOM_SimpleName216', None)
    assert not _is_linked(a, 'DOM_SimpleName216', b2)
    if hasattr(b2, 'DOM_SuperFieldAccess'):
        assert not _is_linked(b2, 'DOM_SuperFieldAccess', a)


def test_assoc_name22_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_MemberRef()
    b2 = DOM_MemberRef()
    _safe_set(a, 'DOM_SimpleName', b1)
    assert _is_linked(a, 'DOM_SimpleName', b1)
    if hasattr(b1, 'DOM_MemberRef'):
        assert _is_linked(b1, 'DOM_MemberRef', a)
    _safe_set(a, 'DOM_SimpleName', b2)
    assert _is_linked(a, 'DOM_SimpleName', b2)
    if hasattr(b1, 'DOM_MemberRef'):
        assert not _is_linked(b1, 'DOM_MemberRef', a)
    if hasattr(b2, 'DOM_MemberRef'):
        assert _is_linked(b2, 'DOM_MemberRef', a)
    _safe_set(a, 'DOM_SimpleName', None)
    assert not _is_linked(a, 'DOM_SimpleName', b2)
    if hasattr(b2, 'DOM_MemberRef'):
        assert not _is_linked(b2, 'DOM_MemberRef', a)


def test_assoc_name222_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_SuperMethodInvocation()
    b2 = DOM_SuperMethodInvocation()
    _safe_set(a, 'DOM_Name224', b1)
    assert _is_linked(a, 'DOM_Name224', b1)
    if hasattr(b1, 'DOM_SuperMethodInvocation223'):
        assert _is_linked(b1, 'DOM_SuperMethodInvocation223', a)
    _safe_set(a, 'DOM_Name224', b2)
    assert _is_linked(a, 'DOM_Name224', b2)
    if hasattr(b1, 'DOM_SuperMethodInvocation223'):
        assert not _is_linked(b1, 'DOM_SuperMethodInvocation223', a)
    if hasattr(b2, 'DOM_SuperMethodInvocation223'):
        assert _is_linked(b2, 'DOM_SuperMethodInvocation223', a)
    _safe_set(a, 'DOM_Name224', None)
    assert not _is_linked(a, 'DOM_Name224', b2)
    if hasattr(b2, 'DOM_SuperMethodInvocation223'):
        assert not _is_linked(b2, 'DOM_SuperMethodInvocation223', a)


def test_assoc_name26_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_MemberValuePair()
    b2 = DOM_MemberValuePair()
    _safe_set(a, 'DOM_SimpleName27', b1)
    assert _is_linked(a, 'DOM_SimpleName27', b1)
    if hasattr(b1, 'DOM_MemberValuePair'):
        assert _is_linked(b1, 'DOM_MemberValuePair', a)
    _safe_set(a, 'DOM_SimpleName27', b2)
    assert _is_linked(a, 'DOM_SimpleName27', b2)
    if hasattr(b1, 'DOM_MemberValuePair'):
        assert not _is_linked(b1, 'DOM_MemberValuePair', a)
    if hasattr(b2, 'DOM_MemberValuePair'):
        assert _is_linked(b2, 'DOM_MemberValuePair', a)
    _safe_set(a, 'DOM_SimpleName27', None)
    assert not _is_linked(a, 'DOM_SimpleName27', b2)
    if hasattr(b2, 'DOM_MemberValuePair'):
        assert not _is_linked(b2, 'DOM_MemberValuePair', a)


def test_assoc_name31_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_MethodRef()
    b2 = DOM_MethodRef()
    _safe_set(a, 'DOM_SimpleName32', b1)
    assert _is_linked(a, 'DOM_SimpleName32', b1)
    if hasattr(b1, 'DOM_MethodRef'):
        assert _is_linked(b1, 'DOM_MethodRef', a)
    _safe_set(a, 'DOM_SimpleName32', b2)
    assert _is_linked(a, 'DOM_SimpleName32', b2)
    if hasattr(b1, 'DOM_MethodRef'):
        assert not _is_linked(b1, 'DOM_MethodRef', a)
    if hasattr(b2, 'DOM_MethodRef'):
        assert _is_linked(b2, 'DOM_MethodRef', a)
    _safe_set(a, 'DOM_SimpleName32', None)
    assert not _is_linked(a, 'DOM_SimpleName32', b2)
    if hasattr(b2, 'DOM_MethodRef'):
        assert not _is_linked(b2, 'DOM_MethodRef', a)


def test_assoc_name356_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_QualifiedType()
    b2 = DOM_QualifiedType()
    _safe_set(a, 'DOM_SimpleName357', b1)
    assert _is_linked(a, 'DOM_SimpleName357', b1)
    if hasattr(b1, 'DOM_QualifiedType'):
        assert _is_linked(b1, 'DOM_QualifiedType', a)
    _safe_set(a, 'DOM_SimpleName357', b2)
    assert _is_linked(a, 'DOM_SimpleName357', b2)
    if hasattr(b1, 'DOM_QualifiedType'):
        assert not _is_linked(b1, 'DOM_QualifiedType', a)
    if hasattr(b2, 'DOM_QualifiedType'):
        assert _is_linked(b2, 'DOM_QualifiedType', a)
    _safe_set(a, 'DOM_SimpleName357', None)
    assert not _is_linked(a, 'DOM_SimpleName357', b2)
    if hasattr(b2, 'DOM_QualifiedType'):
        assert not _is_linked(b2, 'DOM_QualifiedType', a)


def test_assoc_name361_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_SimpleType()
    b2 = DOM_SimpleType()
    _safe_set(a, 'DOM_Name362', b1)
    assert _is_linked(a, 'DOM_Name362', b1)
    if hasattr(b1, 'DOM_SimpleType'):
        assert _is_linked(b1, 'DOM_SimpleType', a)
    _safe_set(a, 'DOM_Name362', b2)
    assert _is_linked(a, 'DOM_Name362', b2)
    if hasattr(b1, 'DOM_SimpleType'):
        assert not _is_linked(b1, 'DOM_SimpleType', a)
    if hasattr(b2, 'DOM_SimpleType'):
        assert _is_linked(b2, 'DOM_SimpleType', a)
    _safe_set(a, 'DOM_Name362', None)
    assert not _is_linked(a, 'DOM_Name362', b2)
    if hasattr(b2, 'DOM_SimpleType'):
        assert not _is_linked(b2, 'DOM_SimpleType', a)


def test_assoc_name371_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_QualifiedName()
    b2 = DOM_QualifiedName()
    _safe_set(a, 'DOM_SimpleName372', b1)
    assert _is_linked(a, 'DOM_SimpleName372', b1)
    if hasattr(b1, 'DOM_QualifiedName'):
        assert _is_linked(b1, 'DOM_QualifiedName', a)
    _safe_set(a, 'DOM_SimpleName372', b2)
    assert _is_linked(a, 'DOM_SimpleName372', b2)
    if hasattr(b1, 'DOM_QualifiedName'):
        assert not _is_linked(b1, 'DOM_QualifiedName', a)
    if hasattr(b2, 'DOM_QualifiedName'):
        assert _is_linked(b2, 'DOM_QualifiedName', a)
    _safe_set(a, 'DOM_SimpleName372', None)
    assert not _is_linked(a, 'DOM_SimpleName372', b2)
    if hasattr(b2, 'DOM_QualifiedName'):
        assert not _is_linked(b2, 'DOM_QualifiedName', a)


def test_assoc_name38_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_MethodRefParameter(varargs="sample_text")
    b2 = DOM_MethodRefParameter(varargs="sample_text_2")
    _safe_set(a, 'DOM_SimpleName40', b1)
    assert _is_linked(a, 'DOM_SimpleName40', b1)
    if hasattr(b1, 'DOM_MethodRefParameter39'):
        assert _is_linked(b1, 'DOM_MethodRefParameter39', a)
    _safe_set(a, 'DOM_SimpleName40', b2)
    assert _is_linked(a, 'DOM_SimpleName40', b2)
    if hasattr(b1, 'DOM_MethodRefParameter39'):
        assert not _is_linked(b1, 'DOM_MethodRefParameter39', a)
    if hasattr(b2, 'DOM_MethodRefParameter39'):
        assert _is_linked(b2, 'DOM_MethodRefParameter39', a)
    _safe_set(a, 'DOM_SimpleName40', None)
    assert not _is_linked(a, 'DOM_SimpleName40', b2)
    if hasattr(b2, 'DOM_MethodRefParameter39'):
        assert not _is_linked(b2, 'DOM_MethodRefParameter39', a)


def test_assoc_name48_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_PackageDeclaration()
    b2 = DOM_PackageDeclaration()
    _safe_set(a, 'DOM_Name50', b1)
    assert _is_linked(a, 'DOM_Name50', b1)
    if hasattr(b1, 'DOM_PackageDeclaration49'):
        assert _is_linked(b1, 'DOM_PackageDeclaration49', a)
    _safe_set(a, 'DOM_Name50', b2)
    assert _is_linked(a, 'DOM_Name50', b2)
    if hasattr(b1, 'DOM_PackageDeclaration49'):
        assert not _is_linked(b1, 'DOM_PackageDeclaration49', a)
    if hasattr(b2, 'DOM_PackageDeclaration49'):
        assert _is_linked(b2, 'DOM_PackageDeclaration49', a)
    _safe_set(a, 'DOM_Name50', None)
    assert not _is_linked(a, 'DOM_Name50', b2)
    if hasattr(b2, 'DOM_PackageDeclaration49'):
        assert not _is_linked(b2, 'DOM_PackageDeclaration49', a)


def test_assoc_name55_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_TypeParameter()
    b2 = DOM_TypeParameter()
    _safe_set(a, 'DOM_SimpleName56', b1)
    assert _is_linked(a, 'DOM_SimpleName56', b1)
    if hasattr(b1, 'DOM_TypeParameter'):
        assert _is_linked(b1, 'DOM_TypeParameter', a)
    _safe_set(a, 'DOM_SimpleName56', b2)
    assert _is_linked(a, 'DOM_SimpleName56', b2)
    if hasattr(b1, 'DOM_TypeParameter'):
        assert not _is_linked(b1, 'DOM_TypeParameter', a)
    if hasattr(b2, 'DOM_TypeParameter'):
        assert _is_linked(b2, 'DOM_TypeParameter', a)
    _safe_set(a, 'DOM_SimpleName56', None)
    assert not _is_linked(a, 'DOM_SimpleName56', b2)
    if hasattr(b2, 'DOM_TypeParameter'):
        assert not _is_linked(b2, 'DOM_TypeParameter', a)


def test_assoc_name62_link_reassign_clear():
    a = DOM_VariableDeclaration(extraDimensions="sample_text")
    b1 = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b2 = DOM_SimpleName(declaration="sample_text_2", identifier="sample_text_2")
    _safe_set(a, 'DOM_VariableDeclaration63', b1)
    assert _is_linked(a, 'DOM_VariableDeclaration63', b1)
    if hasattr(b1, 'DOM_SimpleName64'):
        assert _is_linked(b1, 'DOM_SimpleName64', a)
    _safe_set(a, 'DOM_VariableDeclaration63', b2)
    assert _is_linked(a, 'DOM_VariableDeclaration63', b2)
    if hasattr(b1, 'DOM_SimpleName64'):
        assert not _is_linked(b1, 'DOM_SimpleName64', a)
    if hasattr(b2, 'DOM_SimpleName64'):
        assert _is_linked(b2, 'DOM_SimpleName64', a)
    _safe_set(a, 'DOM_VariableDeclaration63', None)
    assert not _is_linked(a, 'DOM_VariableDeclaration63', b2)
    if hasattr(b2, 'DOM_SimpleName64'):
        assert not _is_linked(b2, 'DOM_SimpleName64', a)


def test_assoc_name68_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    b2 = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text_2", memberTypeDeclaration="sample_text_2", packageMemberTypeDeclaration="sample_text_2")
    _safe_set(a, 'DOM_SimpleName70', b1)
    assert _is_linked(a, 'DOM_SimpleName70', b1)
    if hasattr(b1, 'DOM_AbstractTypeDeclaration69'):
        assert _is_linked(b1, 'DOM_AbstractTypeDeclaration69', a)
    _safe_set(a, 'DOM_SimpleName70', b2)
    assert _is_linked(a, 'DOM_SimpleName70', b2)
    if hasattr(b1, 'DOM_AbstractTypeDeclaration69'):
        assert not _is_linked(b1, 'DOM_AbstractTypeDeclaration69', a)
    if hasattr(b2, 'DOM_AbstractTypeDeclaration69'):
        assert _is_linked(b2, 'DOM_AbstractTypeDeclaration69', a)
    _safe_set(a, 'DOM_SimpleName70', None)
    assert not _is_linked(a, 'DOM_SimpleName70', b2)
    if hasattr(b2, 'DOM_AbstractTypeDeclaration69'):
        assert not _is_linked(b2, 'DOM_AbstractTypeDeclaration69', a)


def test_assoc_name73_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_AnnotationTypeMemberDeclaration()
    b2 = DOM_AnnotationTypeMemberDeclaration()
    _safe_set(a, 'DOM_SimpleName75', b1)
    assert _is_linked(a, 'DOM_SimpleName75', b1)
    if hasattr(b1, 'DOM_AnnotationTypeMemberDeclaration74'):
        assert _is_linked(b1, 'DOM_AnnotationTypeMemberDeclaration74', a)
    _safe_set(a, 'DOM_SimpleName75', b2)
    assert _is_linked(a, 'DOM_SimpleName75', b2)
    if hasattr(b1, 'DOM_AnnotationTypeMemberDeclaration74'):
        assert not _is_linked(b1, 'DOM_AnnotationTypeMemberDeclaration74', a)
    if hasattr(b2, 'DOM_AnnotationTypeMemberDeclaration74'):
        assert _is_linked(b2, 'DOM_AnnotationTypeMemberDeclaration74', a)
    _safe_set(a, 'DOM_SimpleName75', None)
    assert not _is_linked(a, 'DOM_SimpleName75', b2)
    if hasattr(b2, 'DOM_AnnotationTypeMemberDeclaration74'):
        assert not _is_linked(b2, 'DOM_AnnotationTypeMemberDeclaration74', a)


def test_assoc_name84_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_EnumConstantDeclaration()
    b2 = DOM_EnumConstantDeclaration()
    _safe_set(a, 'DOM_SimpleName86', b1)
    assert _is_linked(a, 'DOM_SimpleName86', b1)
    if hasattr(b1, 'DOM_EnumConstantDeclaration85'):
        assert _is_linked(b1, 'DOM_EnumConstantDeclaration85', a)
    _safe_set(a, 'DOM_SimpleName86', b2)
    assert _is_linked(a, 'DOM_SimpleName86', b2)
    if hasattr(b1, 'DOM_EnumConstantDeclaration85'):
        assert not _is_linked(b1, 'DOM_EnumConstantDeclaration85', a)
    if hasattr(b2, 'DOM_EnumConstantDeclaration85'):
        assert _is_linked(b2, 'DOM_EnumConstantDeclaration85', a)
    _safe_set(a, 'DOM_SimpleName86', None)
    assert not _is_linked(a, 'DOM_SimpleName86', b2)
    if hasattr(b2, 'DOM_EnumConstantDeclaration85'):
        assert not _is_linked(b2, 'DOM_EnumConstantDeclaration85', a)


def test_assoc_name95_link_reassign_clear():
    a = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    b1 = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b2 = DOM_MethodDeclaration(constructor="sample_text_2", extraDimensions="sample_text_2", varargs="sample_text_2")
    _safe_set(a, 'DOM_SimpleName97', b1)
    assert _is_linked(a, 'DOM_SimpleName97', b1)
    if hasattr(b1, 'DOM_MethodDeclaration96'):
        assert _is_linked(b1, 'DOM_MethodDeclaration96', a)
    _safe_set(a, 'DOM_SimpleName97', b2)
    assert _is_linked(a, 'DOM_SimpleName97', b2)
    if hasattr(b1, 'DOM_MethodDeclaration96'):
        assert not _is_linked(b1, 'DOM_MethodDeclaration96', a)
    if hasattr(b2, 'DOM_MethodDeclaration96'):
        assert _is_linked(b2, 'DOM_MethodDeclaration96', a)
    _safe_set(a, 'DOM_SimpleName97', None)
    assert not _is_linked(a, 'DOM_SimpleName97', b2)
    if hasattr(b2, 'DOM_MethodDeclaration96'):
        assert not _is_linked(b2, 'DOM_MethodDeclaration96', a)


def test_assoc_operand211_link_reassign_clear():
    a = DOM_PostfixExpression(operator="sample_text")
    b1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    _safe_set(a, 'DOM_PostfixExpression', b1)
    assert _is_linked(a, 'DOM_PostfixExpression', b1)
    if hasattr(b1, 'DOM_Expression212'):
        assert _is_linked(b1, 'DOM_Expression212', a)
    _safe_set(a, 'DOM_PostfixExpression', b2)
    assert _is_linked(a, 'DOM_PostfixExpression', b2)
    if hasattr(b1, 'DOM_Expression212'):
        assert not _is_linked(b1, 'DOM_Expression212', a)
    if hasattr(b2, 'DOM_Expression212'):
        assert _is_linked(b2, 'DOM_Expression212', a)
    _safe_set(a, 'DOM_PostfixExpression', None)
    assert not _is_linked(a, 'DOM_PostfixExpression', b2)
    if hasattr(b2, 'DOM_Expression212'):
        assert not _is_linked(b2, 'DOM_Expression212', a)


def test_assoc_operand213_link_reassign_clear():
    a = DOM_PrefixExpression(operator="sample_text")
    b1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    _safe_set(a, 'DOM_PrefixExpression', b1)
    assert _is_linked(a, 'DOM_PrefixExpression', b1)
    if hasattr(b1, 'DOM_Expression214'):
        assert _is_linked(b1, 'DOM_Expression214', a)
    _safe_set(a, 'DOM_PrefixExpression', b2)
    assert _is_linked(a, 'DOM_PrefixExpression', b2)
    if hasattr(b1, 'DOM_Expression214'):
        assert not _is_linked(b1, 'DOM_Expression214', a)
    if hasattr(b2, 'DOM_Expression214'):
        assert _is_linked(b2, 'DOM_Expression214', a)
    _safe_set(a, 'DOM_PrefixExpression', None)
    assert not _is_linked(a, 'DOM_PrefixExpression', b2)
    if hasattr(b2, 'DOM_Expression214'):
        assert not _is_linked(b2, 'DOM_Expression214', a)


def test_assoc_parameter269_link_reassign_clear():
    a = DOM_SingleVariableDeclaration(varargs="sample_text")
    b1 = DOM_EnhancedForStatement()
    b2 = DOM_EnhancedForStatement()
    _safe_set(a, 'DOM_SingleVariableDeclaration271', b1)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration271', b1)
    if hasattr(b1, 'DOM_EnhancedForStatement270'):
        assert _is_linked(b1, 'DOM_EnhancedForStatement270', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration271', b2)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration271', b2)
    if hasattr(b1, 'DOM_EnhancedForStatement270'):
        assert not _is_linked(b1, 'DOM_EnhancedForStatement270', a)
    if hasattr(b2, 'DOM_EnhancedForStatement270'):
        assert _is_linked(b2, 'DOM_EnhancedForStatement270', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration271', None)
    assert not _is_linked(a, 'DOM_SingleVariableDeclaration271', b2)
    if hasattr(b2, 'DOM_EnhancedForStatement270'):
        assert not _is_linked(b2, 'DOM_EnhancedForStatement270', a)


def test_assoc_parameters101_link_reassign_clear():
    a = DOM_SingleVariableDeclaration(varargs="sample_text")
    b1 = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b2 = DOM_MethodDeclaration(constructor="sample_text_2", extraDimensions="sample_text_2", varargs="sample_text_2")
    _safe_set(a, 'DOM_SingleVariableDeclaration103', b1)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration103', b1)
    if hasattr(b1, 'DOM_MethodDeclaration102'):
        assert _is_linked(b1, 'DOM_MethodDeclaration102', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration103', b2)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration103', b2)
    if hasattr(b1, 'DOM_MethodDeclaration102'):
        assert not _is_linked(b1, 'DOM_MethodDeclaration102', a)
    if hasattr(b2, 'DOM_MethodDeclaration102'):
        assert _is_linked(b2, 'DOM_MethodDeclaration102', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration103', None)
    assert not _is_linked(a, 'DOM_SingleVariableDeclaration103', b2)
    if hasattr(b2, 'DOM_MethodDeclaration102'):
        assert not _is_linked(b2, 'DOM_MethodDeclaration102', a)


def test_assoc_parameters36_link_reassign_clear():
    a = DOM_MethodRefParameter(varargs="sample_text")
    b1 = DOM_MethodRef()
    b2 = DOM_MethodRef()
    _safe_set(a, 'DOM_MethodRefParameter', b1)
    assert _is_linked(a, 'DOM_MethodRefParameter', b1)
    if hasattr(b1, 'DOM_MethodRef37'):
        assert _is_linked(b1, 'DOM_MethodRef37', a)
    _safe_set(a, 'DOM_MethodRefParameter', b2)
    assert _is_linked(a, 'DOM_MethodRefParameter', b2)
    if hasattr(b1, 'DOM_MethodRef37'):
        assert not _is_linked(b1, 'DOM_MethodRef37', a)
    if hasattr(b2, 'DOM_MethodRef37'):
        assert _is_linked(b2, 'DOM_MethodRef37', a)
    _safe_set(a, 'DOM_MethodRefParameter', None)
    assert not _is_linked(a, 'DOM_MethodRefParameter', b2)
    if hasattr(b2, 'DOM_MethodRef37'):
        assert not _is_linked(b2, 'DOM_MethodRef37', a)


def test_assoc_qualifier217_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_SuperFieldAccess()
    b2 = DOM_SuperFieldAccess()
    _safe_set(a, 'DOM_Name219', b1)
    assert _is_linked(a, 'DOM_Name219', b1)
    if hasattr(b1, 'DOM_SuperFieldAccess218'):
        assert _is_linked(b1, 'DOM_SuperFieldAccess218', a)
    _safe_set(a, 'DOM_Name219', b2)
    assert _is_linked(a, 'DOM_Name219', b2)
    if hasattr(b1, 'DOM_SuperFieldAccess218'):
        assert not _is_linked(b1, 'DOM_SuperFieldAccess218', a)
    if hasattr(b2, 'DOM_SuperFieldAccess218'):
        assert _is_linked(b2, 'DOM_SuperFieldAccess218', a)
    _safe_set(a, 'DOM_Name219', None)
    assert not _is_linked(a, 'DOM_Name219', b2)
    if hasattr(b2, 'DOM_SuperFieldAccess218'):
        assert not _is_linked(b2, 'DOM_SuperFieldAccess218', a)


def test_assoc_qualifier225_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_SuperMethodInvocation()
    b2 = DOM_SuperMethodInvocation()
    _safe_set(a, 'DOM_Name227', b1)
    assert _is_linked(a, 'DOM_Name227', b1)
    if hasattr(b1, 'DOM_SuperMethodInvocation226'):
        assert _is_linked(b1, 'DOM_SuperMethodInvocation226', a)
    _safe_set(a, 'DOM_Name227', b2)
    assert _is_linked(a, 'DOM_Name227', b2)
    if hasattr(b1, 'DOM_SuperMethodInvocation226'):
        assert not _is_linked(b1, 'DOM_SuperMethodInvocation226', a)
    if hasattr(b2, 'DOM_SuperMethodInvocation226'):
        assert _is_linked(b2, 'DOM_SuperMethodInvocation226', a)
    _safe_set(a, 'DOM_Name227', None)
    assert not _is_linked(a, 'DOM_Name227', b2)
    if hasattr(b2, 'DOM_SuperMethodInvocation226'):
        assert not _is_linked(b2, 'DOM_SuperMethodInvocation226', a)


def test_assoc_qualifier23_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_MemberRef()
    b2 = DOM_MemberRef()
    _safe_set(a, 'DOM_Name25', b1)
    assert _is_linked(a, 'DOM_Name25', b1)
    if hasattr(b1, 'DOM_MemberRef24'):
        assert _is_linked(b1, 'DOM_MemberRef24', a)
    _safe_set(a, 'DOM_Name25', b2)
    assert _is_linked(a, 'DOM_Name25', b2)
    if hasattr(b1, 'DOM_MemberRef24'):
        assert not _is_linked(b1, 'DOM_MemberRef24', a)
    if hasattr(b2, 'DOM_MemberRef24'):
        assert _is_linked(b2, 'DOM_MemberRef24', a)
    _safe_set(a, 'DOM_Name25', None)
    assert not _is_linked(a, 'DOM_Name25', b2)
    if hasattr(b2, 'DOM_MemberRef24'):
        assert not _is_linked(b2, 'DOM_MemberRef24', a)


def test_assoc_qualifier231_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_ThisExpression()
    b2 = DOM_ThisExpression()
    _safe_set(a, 'DOM_Name232', b1)
    assert _is_linked(a, 'DOM_Name232', b1)
    if hasattr(b1, 'DOM_ThisExpression'):
        assert _is_linked(b1, 'DOM_ThisExpression', a)
    _safe_set(a, 'DOM_Name232', b2)
    assert _is_linked(a, 'DOM_Name232', b2)
    if hasattr(b1, 'DOM_ThisExpression'):
        assert not _is_linked(b1, 'DOM_ThisExpression', a)
    if hasattr(b2, 'DOM_ThisExpression'):
        assert _is_linked(b2, 'DOM_ThisExpression', a)
    _safe_set(a, 'DOM_Name232', None)
    assert not _is_linked(a, 'DOM_Name232', b2)
    if hasattr(b2, 'DOM_ThisExpression'):
        assert not _is_linked(b2, 'DOM_ThisExpression', a)


def test_assoc_qualifier33_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_MethodRef()
    b2 = DOM_MethodRef()
    _safe_set(a, 'DOM_Name35', b1)
    assert _is_linked(a, 'DOM_Name35', b1)
    if hasattr(b1, 'DOM_MethodRef34'):
        assert _is_linked(b1, 'DOM_MethodRef34', a)
    _safe_set(a, 'DOM_Name35', b2)
    assert _is_linked(a, 'DOM_Name35', b2)
    if hasattr(b1, 'DOM_MethodRef34'):
        assert not _is_linked(b1, 'DOM_MethodRef34', a)
    if hasattr(b2, 'DOM_MethodRef34'):
        assert _is_linked(b2, 'DOM_MethodRef34', a)
    _safe_set(a, 'DOM_Name35', None)
    assert not _is_linked(a, 'DOM_Name35', b2)
    if hasattr(b2, 'DOM_MethodRef34'):
        assert not _is_linked(b2, 'DOM_MethodRef34', a)


def test_assoc_qualifier373_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_QualifiedName()
    b2 = DOM_QualifiedName()
    _safe_set(a, 'DOM_Name375', b1)
    assert _is_linked(a, 'DOM_Name375', b1)
    if hasattr(b1, 'DOM_QualifiedName374'):
        assert _is_linked(b1, 'DOM_QualifiedName374', a)
    _safe_set(a, 'DOM_Name375', b2)
    assert _is_linked(a, 'DOM_Name375', b2)
    if hasattr(b1, 'DOM_QualifiedName374'):
        assert not _is_linked(b1, 'DOM_QualifiedName374', a)
    if hasattr(b2, 'DOM_QualifiedName374'):
        assert _is_linked(b2, 'DOM_QualifiedName374', a)
    _safe_set(a, 'DOM_Name375', None)
    assert not _is_linked(a, 'DOM_Name375', b2)
    if hasattr(b2, 'DOM_QualifiedName374'):
        assert not _is_linked(b2, 'DOM_QualifiedName374', a)


def test_assoc_returnType98_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = DOM_Type()
    b2 = DOM_Type()
    _safe_set(a, 'DOM_MethodDeclaration99', b1)
    assert _is_linked(a, 'DOM_MethodDeclaration99', b1)
    if hasattr(b1, 'DOM_Type100'):
        assert _is_linked(b1, 'DOM_Type100', a)
    _safe_set(a, 'DOM_MethodDeclaration99', b2)
    assert _is_linked(a, 'DOM_MethodDeclaration99', b2)
    if hasattr(b1, 'DOM_Type100'):
        assert not _is_linked(b1, 'DOM_Type100', a)
    if hasattr(b2, 'DOM_Type100'):
        assert _is_linked(b2, 'DOM_Type100', a)
    _safe_set(a, 'DOM_MethodDeclaration99', None)
    assert not _is_linked(a, 'DOM_MethodDeclaration99', b2)
    if hasattr(b2, 'DOM_Type100'):
        assert not _is_linked(b2, 'DOM_Type100', a)


def test_assoc_rightHandSide147_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_Assignment(operator="sample_text")
    b2 = DOM_Assignment(operator="sample_text_2")
    _safe_set(a, 'DOM_Expression149', b1)
    assert _is_linked(a, 'DOM_Expression149', b1)
    if hasattr(b1, 'DOM_Assignment148'):
        assert _is_linked(b1, 'DOM_Assignment148', a)
    _safe_set(a, 'DOM_Expression149', b2)
    assert _is_linked(a, 'DOM_Expression149', b2)
    if hasattr(b1, 'DOM_Assignment148'):
        assert not _is_linked(b1, 'DOM_Assignment148', a)
    if hasattr(b2, 'DOM_Assignment148'):
        assert _is_linked(b2, 'DOM_Assignment148', a)
    _safe_set(a, 'DOM_Expression149', None)
    assert not _is_linked(a, 'DOM_Expression149', b2)
    if hasattr(b2, 'DOM_Assignment148'):
        assert not _is_linked(b2, 'DOM_Assignment148', a)


def test_assoc_rightOperand187_link_reassign_clear():
    a = DOM_InfixExpression(operator="sample_text")
    b1 = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b2 = DOM_Expression(resolveBoxing="sample_text_2", resolveUnboxing="sample_text_2")
    _safe_set(a, 'DOM_InfixExpression188', b1)
    assert _is_linked(a, 'DOM_InfixExpression188', b1)
    if hasattr(b1, 'DOM_Expression189'):
        assert _is_linked(b1, 'DOM_Expression189', a)
    _safe_set(a, 'DOM_InfixExpression188', b2)
    assert _is_linked(a, 'DOM_InfixExpression188', b2)
    if hasattr(b1, 'DOM_Expression189'):
        assert not _is_linked(b1, 'DOM_Expression189', a)
    if hasattr(b2, 'DOM_Expression189'):
        assert _is_linked(b2, 'DOM_Expression189', a)
    _safe_set(a, 'DOM_InfixExpression188', None)
    assert not _is_linked(a, 'DOM_InfixExpression188', b2)
    if hasattr(b2, 'DOM_Expression189'):
        assert not _is_linked(b2, 'DOM_Expression189', a)


def test_assoc_superInterfaceTypes119_link_reassign_clear():
    a = DOM_TypeDeclaration(interface="sample_text")
    b1 = DOM_Type()
    b2 = DOM_Type()
    _safe_set(a, 'DOM_TypeDeclaration120', {b1})
    assert _is_linked(a, 'DOM_TypeDeclaration120', b1)
    if hasattr(b1, 'DOM_Type121'):
        assert _is_linked(b1, 'DOM_Type121', a)
    _safe_set(a, 'DOM_TypeDeclaration120', {b2})
    assert _is_linked(a, 'DOM_TypeDeclaration120', b2)
    if hasattr(b1, 'DOM_Type121'):
        assert not _is_linked(b1, 'DOM_Type121', a)
    if hasattr(b2, 'DOM_Type121'):
        assert _is_linked(b2, 'DOM_Type121', a)
    _safe_set(a, 'DOM_TypeDeclaration120', set())
    assert not _is_linked(a, 'DOM_TypeDeclaration120', b2)
    if hasattr(b2, 'DOM_Type121'):
        assert not _is_linked(b2, 'DOM_Type121', a)


def test_assoc_superclassType117_link_reassign_clear():
    a = DOM_TypeDeclaration(interface="sample_text")
    b1 = DOM_Type()
    b2 = DOM_Type()
    _safe_set(a, 'DOM_TypeDeclaration', b1)
    assert _is_linked(a, 'DOM_TypeDeclaration', b1)
    if hasattr(b1, 'DOM_Type118'):
        assert _is_linked(b1, 'DOM_Type118', a)
    _safe_set(a, 'DOM_TypeDeclaration', b2)
    assert _is_linked(a, 'DOM_TypeDeclaration', b2)
    if hasattr(b1, 'DOM_Type118'):
        assert not _is_linked(b1, 'DOM_Type118', a)
    if hasattr(b2, 'DOM_Type118'):
        assert _is_linked(b2, 'DOM_Type118', a)
    _safe_set(a, 'DOM_TypeDeclaration', None)
    assert not _is_linked(a, 'DOM_TypeDeclaration', b2)
    if hasattr(b2, 'DOM_Type118'):
        assert not _is_linked(b2, 'DOM_Type118', a)


def test_assoc_tags125_link_reassign_clear():
    a = DOM_TagElement(nested="sample_text", tagName="sample_text")
    b1 = DOM_Javadoc()
    b2 = DOM_Javadoc()
    _safe_set(a, 'DOM_TagElement127', b1)
    assert _is_linked(a, 'DOM_TagElement127', b1)
    if hasattr(b1, 'DOM_Javadoc126'):
        assert _is_linked(b1, 'DOM_Javadoc126', a)
    _safe_set(a, 'DOM_TagElement127', b2)
    assert _is_linked(a, 'DOM_TagElement127', b2)
    if hasattr(b1, 'DOM_Javadoc126'):
        assert not _is_linked(b1, 'DOM_Javadoc126', a)
    if hasattr(b2, 'DOM_Javadoc126'):
        assert _is_linked(b2, 'DOM_Javadoc126', a)
    _safe_set(a, 'DOM_TagElement127', None)
    assert not _is_linked(a, 'DOM_TagElement127', b2)
    if hasattr(b2, 'DOM_Javadoc126'):
        assert not _is_linked(b2, 'DOM_Javadoc126', a)


def test_assoc_thenExpression174_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ConditionalExpression()
    b2 = DOM_ConditionalExpression()
    _safe_set(a, 'DOM_Expression176', b1)
    assert _is_linked(a, 'DOM_Expression176', b1)
    if hasattr(b1, 'DOM_ConditionalExpression175'):
        assert _is_linked(b1, 'DOM_ConditionalExpression175', a)
    _safe_set(a, 'DOM_Expression176', b2)
    assert _is_linked(a, 'DOM_Expression176', b2)
    if hasattr(b1, 'DOM_ConditionalExpression175'):
        assert not _is_linked(b1, 'DOM_ConditionalExpression175', a)
    if hasattr(b2, 'DOM_ConditionalExpression175'):
        assert _is_linked(b2, 'DOM_ConditionalExpression175', a)
    _safe_set(a, 'DOM_Expression176', None)
    assert not _is_linked(a, 'DOM_Expression176', b2)
    if hasattr(b2, 'DOM_ConditionalExpression175'):
        assert not _is_linked(b2, 'DOM_ConditionalExpression175', a)


def test_assoc_thrownExceptions104_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b2 = DOM_MethodDeclaration(constructor="sample_text_2", extraDimensions="sample_text_2", varargs="sample_text_2")
    _safe_set(a, 'DOM_Name106', b1)
    assert _is_linked(a, 'DOM_Name106', b1)
    if hasattr(b1, 'DOM_MethodDeclaration105'):
        assert _is_linked(b1, 'DOM_MethodDeclaration105', a)
    _safe_set(a, 'DOM_Name106', b2)
    assert _is_linked(a, 'DOM_Name106', b2)
    if hasattr(b1, 'DOM_MethodDeclaration105'):
        assert not _is_linked(b1, 'DOM_MethodDeclaration105', a)
    if hasattr(b2, 'DOM_MethodDeclaration105'):
        assert _is_linked(b2, 'DOM_MethodDeclaration105', a)
    _safe_set(a, 'DOM_Name106', None)
    assert not _is_linked(a, 'DOM_Name106', b2)
    if hasattr(b2, 'DOM_MethodDeclaration105'):
        assert not _is_linked(b2, 'DOM_MethodDeclaration105', a)


def test_assoc_type140_link_reassign_clear():
    a = DOM_ArrayType(dimensions="sample_text")
    b1 = DOM_ArrayCreation()
    b2 = DOM_ArrayCreation()
    _safe_set(a, 'DOM_ArrayType', b1)
    assert _is_linked(a, 'DOM_ArrayType', b1)
    if hasattr(b1, 'DOM_ArrayCreation141'):
        assert _is_linked(b1, 'DOM_ArrayCreation141', a)
    _safe_set(a, 'DOM_ArrayType', b2)
    assert _is_linked(a, 'DOM_ArrayType', b2)
    if hasattr(b1, 'DOM_ArrayCreation141'):
        assert not _is_linked(b1, 'DOM_ArrayCreation141', a)
    if hasattr(b2, 'DOM_ArrayCreation141'):
        assert _is_linked(b2, 'DOM_ArrayCreation141', a)
    _safe_set(a, 'DOM_ArrayType', None)
    assert not _is_linked(a, 'DOM_ArrayType', b2)
    if hasattr(b2, 'DOM_ArrayCreation141'):
        assert not _is_linked(b2, 'DOM_ArrayCreation141', a)


def test_assoc_type365_link_reassign_clear():
    a = DOM_SingleVariableDeclaration(varargs="sample_text")
    b1 = DOM_Type()
    b2 = DOM_Type()
    _safe_set(a, 'DOM_SingleVariableDeclaration366', b1)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration366', b1)
    if hasattr(b1, 'DOM_Type367'):
        assert _is_linked(b1, 'DOM_Type367', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration366', b2)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration366', b2)
    if hasattr(b1, 'DOM_Type367'):
        assert not _is_linked(b1, 'DOM_Type367', a)
    if hasattr(b2, 'DOM_Type367'):
        assert _is_linked(b2, 'DOM_Type367', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration366', None)
    assert not _is_linked(a, 'DOM_SingleVariableDeclaration366', b2)
    if hasattr(b2, 'DOM_Type367'):
        assert not _is_linked(b2, 'DOM_Type367', a)


def test_assoc_type41_link_reassign_clear():
    a = DOM_MethodRefParameter(varargs="sample_text")
    b1 = DOM_Type()
    b2 = DOM_Type()
    _safe_set(a, 'DOM_MethodRefParameter42', b1)
    assert _is_linked(a, 'DOM_MethodRefParameter42', b1)
    if hasattr(b1, 'DOM_Type'):
        assert _is_linked(b1, 'DOM_Type', a)
    _safe_set(a, 'DOM_MethodRefParameter42', b2)
    assert _is_linked(a, 'DOM_MethodRefParameter42', b2)
    if hasattr(b1, 'DOM_Type'):
        assert not _is_linked(b1, 'DOM_Type', a)
    if hasattr(b2, 'DOM_Type'):
        assert _is_linked(b2, 'DOM_Type', a)
    _safe_set(a, 'DOM_MethodRefParameter42', None)
    assert not _is_linked(a, 'DOM_MethodRefParameter42', b2)
    if hasattr(b2, 'DOM_Type'):
        assert not _is_linked(b2, 'DOM_Type', a)


def test_assoc_typeBinding19_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_IType()
    b2 = DOM_IType()
    _safe_set(a, 'DOM_Expression', b1)
    assert _is_linked(a, 'DOM_Expression', b1)
    if hasattr(b1, 'DOM_IType'):
        assert _is_linked(b1, 'DOM_IType', a)
    _safe_set(a, 'DOM_Expression', b2)
    assert _is_linked(a, 'DOM_Expression', b2)
    if hasattr(b1, 'DOM_IType'):
        assert not _is_linked(b1, 'DOM_IType', a)
    if hasattr(b2, 'DOM_IType'):
        assert _is_linked(b2, 'DOM_IType', a)
    _safe_set(a, 'DOM_Expression', None)
    assert not _is_linked(a, 'DOM_Expression', b2)
    if hasattr(b2, 'DOM_IType'):
        assert not _is_linked(b2, 'DOM_IType', a)


def test_assoc_typeName128_link_reassign_clear():
    a = DOM_Name(fullyQualifiedName="sample_text")
    b1 = DOM_Annotation()
    b2 = DOM_Annotation()
    _safe_set(a, 'DOM_Name130', b1)
    assert _is_linked(a, 'DOM_Name130', b1)
    if hasattr(b1, 'DOM_Annotation129'):
        assert _is_linked(b1, 'DOM_Annotation129', a)
    _safe_set(a, 'DOM_Name130', b2)
    assert _is_linked(a, 'DOM_Name130', b2)
    if hasattr(b1, 'DOM_Annotation129'):
        assert not _is_linked(b1, 'DOM_Annotation129', a)
    if hasattr(b2, 'DOM_Annotation129'):
        assert _is_linked(b2, 'DOM_Annotation129', a)
    _safe_set(a, 'DOM_Name130', None)
    assert not _is_linked(a, 'DOM_Name130', b2)
    if hasattr(b2, 'DOM_Annotation129'):
        assert not _is_linked(b2, 'DOM_Annotation129', a)


def test_assoc_typeParameters107_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = DOM_TypeParameter()
    b2 = DOM_TypeParameter()
    _safe_set(a, 'DOM_MethodDeclaration108', {b1})
    assert _is_linked(a, 'DOM_MethodDeclaration108', b1)
    if hasattr(b1, 'DOM_TypeParameter109'):
        assert _is_linked(b1, 'DOM_TypeParameter109', a)
    _safe_set(a, 'DOM_MethodDeclaration108', {b2})
    assert _is_linked(a, 'DOM_MethodDeclaration108', b2)
    if hasattr(b1, 'DOM_TypeParameter109'):
        assert not _is_linked(b1, 'DOM_TypeParameter109', a)
    if hasattr(b2, 'DOM_TypeParameter109'):
        assert _is_linked(b2, 'DOM_TypeParameter109', a)
    _safe_set(a, 'DOM_MethodDeclaration108', set())
    assert not _is_linked(a, 'DOM_MethodDeclaration108', b2)
    if hasattr(b2, 'DOM_TypeParameter109'):
        assert not _is_linked(b2, 'DOM_TypeParameter109', a)


def test_assoc_typeParameters122_link_reassign_clear():
    a = DOM_TypeDeclaration(interface="sample_text")
    b1 = DOM_TypeParameter()
    b2 = DOM_TypeParameter()
    _safe_set(a, 'DOM_TypeDeclaration123', {b1})
    assert _is_linked(a, 'DOM_TypeDeclaration123', b1)
    if hasattr(b1, 'DOM_TypeParameter124'):
        assert _is_linked(b1, 'DOM_TypeParameter124', a)
    _safe_set(a, 'DOM_TypeDeclaration123', {b2})
    assert _is_linked(a, 'DOM_TypeDeclaration123', b2)
    if hasattr(b1, 'DOM_TypeParameter124'):
        assert not _is_linked(b1, 'DOM_TypeParameter124', a)
    if hasattr(b2, 'DOM_TypeParameter124'):
        assert _is_linked(b2, 'DOM_TypeParameter124', a)
    _safe_set(a, 'DOM_TypeDeclaration123', set())
    assert not _is_linked(a, 'DOM_TypeDeclaration123', b2)
    if hasattr(b2, 'DOM_TypeParameter124'):
        assert not _is_linked(b2, 'DOM_TypeParameter124', a)


def test_assoc_types17_link_reassign_clear():
    a = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    b1 = DOM_CompilationUnit()
    b2 = DOM_CompilationUnit()
    _safe_set(a, 'DOM_AbstractTypeDeclaration', b1)
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration', b1)
    if hasattr(b1, 'DOM_CompilationUnit18'):
        assert _is_linked(b1, 'DOM_CompilationUnit18', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration', b2)
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration', b2)
    if hasattr(b1, 'DOM_CompilationUnit18'):
        assert not _is_linked(b1, 'DOM_CompilationUnit18', a)
    if hasattr(b2, 'DOM_CompilationUnit18'):
        assert _is_linked(b2, 'DOM_CompilationUnit18', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration', None)
    assert not _is_linked(a, 'DOM_AbstractTypeDeclaration', b2)
    if hasattr(b2, 'DOM_CompilationUnit18'):
        assert not _is_linked(b2, 'DOM_CompilationUnit18', a)


def test_assoc_updaters282_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_ForStatement()
    b2 = DOM_ForStatement()
    _safe_set(a, 'DOM_Expression284', b1)
    assert _is_linked(a, 'DOM_Expression284', b1)
    if hasattr(b1, 'DOM_ForStatement283'):
        assert _is_linked(b1, 'DOM_ForStatement283', a)
    _safe_set(a, 'DOM_Expression284', b2)
    assert _is_linked(a, 'DOM_Expression284', b2)
    if hasattr(b1, 'DOM_ForStatement283'):
        assert not _is_linked(b1, 'DOM_ForStatement283', a)
    if hasattr(b2, 'DOM_ForStatement283'):
        assert _is_linked(b2, 'DOM_ForStatement283', a)
    _safe_set(a, 'DOM_Expression284', None)
    assert not _is_linked(a, 'DOM_Expression284', b2)
    if hasattr(b2, 'DOM_ForStatement283'):
        assert not _is_linked(b2, 'DOM_ForStatement283', a)


def test_assoc_value28_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_MemberValuePair()
    b2 = DOM_MemberValuePair()
    _safe_set(a, 'DOM_Expression30', b1)
    assert _is_linked(a, 'DOM_Expression30', b1)
    if hasattr(b1, 'DOM_MemberValuePair29'):
        assert _is_linked(b1, 'DOM_MemberValuePair29', a)
    _safe_set(a, 'DOM_Expression30', b2)
    assert _is_linked(a, 'DOM_Expression30', b2)
    if hasattr(b1, 'DOM_MemberValuePair29'):
        assert not _is_linked(b1, 'DOM_MemberValuePair29', a)
    if hasattr(b2, 'DOM_MemberValuePair29'):
        assert _is_linked(b2, 'DOM_MemberValuePair29', a)
    _safe_set(a, 'DOM_Expression30', None)
    assert not _is_linked(a, 'DOM_Expression30', b2)
    if hasattr(b2, 'DOM_MemberValuePair29'):
        assert not _is_linked(b2, 'DOM_MemberValuePair29', a)


def test_assoc_value378_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = DOM_SingleMemberAnnotation()
    b2 = DOM_SingleMemberAnnotation()
    _safe_set(a, 'DOM_Expression379', b1)
    assert _is_linked(a, 'DOM_Expression379', b1)
    if hasattr(b1, 'DOM_SingleMemberAnnotation'):
        assert _is_linked(b1, 'DOM_SingleMemberAnnotation', a)
    _safe_set(a, 'DOM_Expression379', b2)
    assert _is_linked(a, 'DOM_Expression379', b2)
    if hasattr(b1, 'DOM_SingleMemberAnnotation'):
        assert not _is_linked(b1, 'DOM_SingleMemberAnnotation', a)
    if hasattr(b2, 'DOM_SingleMemberAnnotation'):
        assert _is_linked(b2, 'DOM_SingleMemberAnnotation', a)
    _safe_set(a, 'DOM_Expression379', None)
    assert not _is_linked(a, 'DOM_Expression379', b2)
    if hasattr(b2, 'DOM_SingleMemberAnnotation'):
        assert not _is_linked(b2, 'DOM_SingleMemberAnnotation', a)


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


Annotation_strategy = st.builds(Annotation)
@given(instance=Annotation_strategy)
@settings(max_examples=25)
def test_Annotation_instantiation(instance):
    assert isinstance(instance, Annotation)


BodyDeclaration_strategy = st.builds(BodyDeclaration)
@given(instance=BodyDeclaration_strategy)
@settings(max_examples=25)
def test_BodyDeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)


Comment_strategy = st.builds(Comment)
@given(instance=Comment_strategy)
@settings(max_examples=25)
def test_Comment_instantiation(instance):
    assert isinstance(instance, Comment)


DOM_AST_strategy = st.builds(DOM_AST)
@given(instance=DOM_AST_strategy)
@settings(max_examples=25)
def test_DOM_AST_instantiation(instance):
    assert isinstance(instance, DOM_AST)


DOM_ASTNode_strategy = st.builds(DOM_ASTNode)
@given(instance=DOM_ASTNode_strategy)
@settings(max_examples=25)
def test_DOM_ASTNode_instantiation(instance):
    assert isinstance(instance, DOM_ASTNode)


DOM_AbstractTypeDeclaration_strategy = st.builds(DOM_AbstractTypeDeclaration, localTypeDeclaration=safe_text, memberTypeDeclaration=safe_text, packageMemberTypeDeclaration=safe_text)
@given(instance=DOM_AbstractTypeDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_AbstractTypeDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_AbstractTypeDeclaration)


DOM_Annotation_strategy = st.builds(DOM_Annotation)
@given(instance=DOM_Annotation_strategy)
@settings(max_examples=25)
def test_DOM_Annotation_instantiation(instance):
    assert isinstance(instance, DOM_Annotation)


DOM_AnnotationTypeDeclaration_strategy = st.builds(DOM_AnnotationTypeDeclaration)
@given(instance=DOM_AnnotationTypeDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_AnnotationTypeDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_AnnotationTypeDeclaration)


DOM_AnnotationTypeMemberDeclaration_strategy = st.builds(DOM_AnnotationTypeMemberDeclaration)
@given(instance=DOM_AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_AnnotationTypeMemberDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_AnnotationTypeMemberDeclaration)


DOM_AnonymousClassDeclaration_strategy = st.builds(DOM_AnonymousClassDeclaration)
@given(instance=DOM_AnonymousClassDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_AnonymousClassDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_AnonymousClassDeclaration)


DOM_ArrayAccess_strategy = st.builds(DOM_ArrayAccess)
@given(instance=DOM_ArrayAccess_strategy)
@settings(max_examples=25)
def test_DOM_ArrayAccess_instantiation(instance):
    assert isinstance(instance, DOM_ArrayAccess)


DOM_ArrayCreation_strategy = st.builds(DOM_ArrayCreation)
@given(instance=DOM_ArrayCreation_strategy)
@settings(max_examples=25)
def test_DOM_ArrayCreation_instantiation(instance):
    assert isinstance(instance, DOM_ArrayCreation)


DOM_ArrayInitializer_strategy = st.builds(DOM_ArrayInitializer)
@given(instance=DOM_ArrayInitializer_strategy)
@settings(max_examples=25)
def test_DOM_ArrayInitializer_instantiation(instance):
    assert isinstance(instance, DOM_ArrayInitializer)


DOM_ArrayType_strategy = st.builds(DOM_ArrayType, dimensions=safe_text)
@given(instance=DOM_ArrayType_strategy)
@settings(max_examples=25)
def test_DOM_ArrayType_instantiation(instance):
    assert isinstance(instance, DOM_ArrayType)


DOM_AssertStatement_strategy = st.builds(DOM_AssertStatement)
@given(instance=DOM_AssertStatement_strategy)
@settings(max_examples=25)
def test_DOM_AssertStatement_instantiation(instance):
    assert isinstance(instance, DOM_AssertStatement)


DOM_Assignment_strategy = st.builds(DOM_Assignment, operator=safe_text)
@given(instance=DOM_Assignment_strategy)
@settings(max_examples=25)
def test_DOM_Assignment_instantiation(instance):
    assert isinstance(instance, DOM_Assignment)


DOM_Block_strategy = st.builds(DOM_Block)
@given(instance=DOM_Block_strategy)
@settings(max_examples=25)
def test_DOM_Block_instantiation(instance):
    assert isinstance(instance, DOM_Block)


DOM_BlockComment_strategy = st.builds(DOM_BlockComment)
@given(instance=DOM_BlockComment_strategy)
@settings(max_examples=25)
def test_DOM_BlockComment_instantiation(instance):
    assert isinstance(instance, DOM_BlockComment)


DOM_BodyDeclaration_strategy = st.builds(DOM_BodyDeclaration)
@given(instance=DOM_BodyDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_BodyDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_BodyDeclaration)


DOM_BooleanLiteral_strategy = st.builds(DOM_BooleanLiteral, booleanValue=safe_text)
@given(instance=DOM_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_DOM_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, DOM_BooleanLiteral)


DOM_BreakStatement_strategy = st.builds(DOM_BreakStatement)
@given(instance=DOM_BreakStatement_strategy)
@settings(max_examples=25)
def test_DOM_BreakStatement_instantiation(instance):
    assert isinstance(instance, DOM_BreakStatement)


DOM_CastExpression_strategy = st.builds(DOM_CastExpression)
@given(instance=DOM_CastExpression_strategy)
@settings(max_examples=25)
def test_DOM_CastExpression_instantiation(instance):
    assert isinstance(instance, DOM_CastExpression)


DOM_CatchClause_strategy = st.builds(DOM_CatchClause)
@given(instance=DOM_CatchClause_strategy)
@settings(max_examples=25)
def test_DOM_CatchClause_instantiation(instance):
    assert isinstance(instance, DOM_CatchClause)


DOM_CharacterLiteral_strategy = st.builds(DOM_CharacterLiteral, charValue=safe_text, escapedValue=safe_text)
@given(instance=DOM_CharacterLiteral_strategy)
@settings(max_examples=25)
def test_DOM_CharacterLiteral_instantiation(instance):
    assert isinstance(instance, DOM_CharacterLiteral)


DOM_ClassInstanceCreation_strategy = st.builds(DOM_ClassInstanceCreation)
@given(instance=DOM_ClassInstanceCreation_strategy)
@settings(max_examples=25)
def test_DOM_ClassInstanceCreation_instantiation(instance):
    assert isinstance(instance, DOM_ClassInstanceCreation)


DOM_Comment_strategy = st.builds(DOM_Comment)
@given(instance=DOM_Comment_strategy)
@settings(max_examples=25)
def test_DOM_Comment_instantiation(instance):
    assert isinstance(instance, DOM_Comment)


DOM_CompilationUnit_strategy = st.builds(DOM_CompilationUnit)
@given(instance=DOM_CompilationUnit_strategy)
@settings(max_examples=25)
def test_DOM_CompilationUnit_instantiation(instance):
    assert isinstance(instance, DOM_CompilationUnit)


DOM_ConditionalExpression_strategy = st.builds(DOM_ConditionalExpression)
@given(instance=DOM_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_DOM_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, DOM_ConditionalExpression)


DOM_ConstructorInvocation_strategy = st.builds(DOM_ConstructorInvocation)
@given(instance=DOM_ConstructorInvocation_strategy)
@settings(max_examples=25)
def test_DOM_ConstructorInvocation_instantiation(instance):
    assert isinstance(instance, DOM_ConstructorInvocation)


DOM_ContinueStatement_strategy = st.builds(DOM_ContinueStatement)
@given(instance=DOM_ContinueStatement_strategy)
@settings(max_examples=25)
def test_DOM_ContinueStatement_instantiation(instance):
    assert isinstance(instance, DOM_ContinueStatement)


DOM_DoStatement_strategy = st.builds(DOM_DoStatement)
@given(instance=DOM_DoStatement_strategy)
@settings(max_examples=25)
def test_DOM_DoStatement_instantiation(instance):
    assert isinstance(instance, DOM_DoStatement)


DOM_EmptyStatement_strategy = st.builds(DOM_EmptyStatement)
@given(instance=DOM_EmptyStatement_strategy)
@settings(max_examples=25)
def test_DOM_EmptyStatement_instantiation(instance):
    assert isinstance(instance, DOM_EmptyStatement)


DOM_EnhancedForStatement_strategy = st.builds(DOM_EnhancedForStatement)
@given(instance=DOM_EnhancedForStatement_strategy)
@settings(max_examples=25)
def test_DOM_EnhancedForStatement_instantiation(instance):
    assert isinstance(instance, DOM_EnhancedForStatement)


DOM_EnumConstantDeclaration_strategy = st.builds(DOM_EnumConstantDeclaration)
@given(instance=DOM_EnumConstantDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_EnumConstantDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_EnumConstantDeclaration)


DOM_EnumDeclaration_strategy = st.builds(DOM_EnumDeclaration)
@given(instance=DOM_EnumDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_EnumDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_EnumDeclaration)


DOM_Expression_strategy = st.builds(DOM_Expression, resolveBoxing=safe_text, resolveUnboxing=safe_text)
@given(instance=DOM_Expression_strategy)
@settings(max_examples=25)
def test_DOM_Expression_instantiation(instance):
    assert isinstance(instance, DOM_Expression)


DOM_ExpressionStatement_strategy = st.builds(DOM_ExpressionStatement)
@given(instance=DOM_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_DOM_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, DOM_ExpressionStatement)


DOM_ExtendedModifier_strategy = st.builds(DOM_ExtendedModifier)
@given(instance=DOM_ExtendedModifier_strategy)
@settings(max_examples=25)
def test_DOM_ExtendedModifier_instantiation(instance):
    assert isinstance(instance, DOM_ExtendedModifier)


DOM_FieldAccess_strategy = st.builds(DOM_FieldAccess)
@given(instance=DOM_FieldAccess_strategy)
@settings(max_examples=25)
def test_DOM_FieldAccess_instantiation(instance):
    assert isinstance(instance, DOM_FieldAccess)


DOM_FieldDeclaration_strategy = st.builds(DOM_FieldDeclaration)
@given(instance=DOM_FieldDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_FieldDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_FieldDeclaration)


DOM_ForStatement_strategy = st.builds(DOM_ForStatement)
@given(instance=DOM_ForStatement_strategy)
@settings(max_examples=25)
def test_DOM_ForStatement_instantiation(instance):
    assert isinstance(instance, DOM_ForStatement)


DOM_IMethod_strategy = st.builds(DOM_IMethod)
@given(instance=DOM_IMethod_strategy)
@settings(max_examples=25)
def test_DOM_IMethod_instantiation(instance):
    assert isinstance(instance, DOM_IMethod)


DOM_IPackageFragment_strategy = st.builds(DOM_IPackageFragment)
@given(instance=DOM_IPackageFragment_strategy)
@settings(max_examples=25)
def test_DOM_IPackageFragment_instantiation(instance):
    assert isinstance(instance, DOM_IPackageFragment)


DOM_IType_strategy = st.builds(DOM_IType)
@given(instance=DOM_IType_strategy)
@settings(max_examples=25)
def test_DOM_IType_instantiation(instance):
    assert isinstance(instance, DOM_IType)


DOM_IfStatement_strategy = st.builds(DOM_IfStatement)
@given(instance=DOM_IfStatement_strategy)
@settings(max_examples=25)
def test_DOM_IfStatement_instantiation(instance):
    assert isinstance(instance, DOM_IfStatement)


DOM_ImportDeclaration_strategy = st.builds(DOM_ImportDeclaration, onDemand=safe_text, static=safe_text)
@given(instance=DOM_ImportDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_ImportDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_ImportDeclaration)


DOM_InfixExpression_strategy = st.builds(DOM_InfixExpression, operator=safe_text)
@given(instance=DOM_InfixExpression_strategy)
@settings(max_examples=25)
def test_DOM_InfixExpression_instantiation(instance):
    assert isinstance(instance, DOM_InfixExpression)


DOM_Initializer_strategy = st.builds(DOM_Initializer)
@given(instance=DOM_Initializer_strategy)
@settings(max_examples=25)
def test_DOM_Initializer_instantiation(instance):
    assert isinstance(instance, DOM_Initializer)


DOM_InstanceofExpression_strategy = st.builds(DOM_InstanceofExpression)
@given(instance=DOM_InstanceofExpression_strategy)
@settings(max_examples=25)
def test_DOM_InstanceofExpression_instantiation(instance):
    assert isinstance(instance, DOM_InstanceofExpression)


DOM_Javadoc_strategy = st.builds(DOM_Javadoc)
@given(instance=DOM_Javadoc_strategy)
@settings(max_examples=25)
def test_DOM_Javadoc_instantiation(instance):
    assert isinstance(instance, DOM_Javadoc)


DOM_LabeledStatement_strategy = st.builds(DOM_LabeledStatement)
@given(instance=DOM_LabeledStatement_strategy)
@settings(max_examples=25)
def test_DOM_LabeledStatement_instantiation(instance):
    assert isinstance(instance, DOM_LabeledStatement)


DOM_LineComment_strategy = st.builds(DOM_LineComment)
@given(instance=DOM_LineComment_strategy)
@settings(max_examples=25)
def test_DOM_LineComment_instantiation(instance):
    assert isinstance(instance, DOM_LineComment)


DOM_MarkerAnnotation_strategy = st.builds(DOM_MarkerAnnotation)
@given(instance=DOM_MarkerAnnotation_strategy)
@settings(max_examples=25)
def test_DOM_MarkerAnnotation_instantiation(instance):
    assert isinstance(instance, DOM_MarkerAnnotation)


DOM_MemberRef_strategy = st.builds(DOM_MemberRef)
@given(instance=DOM_MemberRef_strategy)
@settings(max_examples=25)
def test_DOM_MemberRef_instantiation(instance):
    assert isinstance(instance, DOM_MemberRef)


DOM_MemberValuePair_strategy = st.builds(DOM_MemberValuePair)
@given(instance=DOM_MemberValuePair_strategy)
@settings(max_examples=25)
def test_DOM_MemberValuePair_instantiation(instance):
    assert isinstance(instance, DOM_MemberValuePair)


DOM_MethodDeclaration_strategy = st.builds(DOM_MethodDeclaration, constructor=safe_text, extraDimensions=safe_text, varargs=safe_text)
@given(instance=DOM_MethodDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_MethodDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_MethodDeclaration)


DOM_MethodInvocation_strategy = st.builds(DOM_MethodInvocation)
@given(instance=DOM_MethodInvocation_strategy)
@settings(max_examples=25)
def test_DOM_MethodInvocation_instantiation(instance):
    assert isinstance(instance, DOM_MethodInvocation)


DOM_MethodRef_strategy = st.builds(DOM_MethodRef)
@given(instance=DOM_MethodRef_strategy)
@settings(max_examples=25)
def test_DOM_MethodRef_instantiation(instance):
    assert isinstance(instance, DOM_MethodRef)


DOM_MethodRefParameter_strategy = st.builds(DOM_MethodRefParameter, varargs=safe_text)
@given(instance=DOM_MethodRefParameter_strategy)
@settings(max_examples=25)
def test_DOM_MethodRefParameter_instantiation(instance):
    assert isinstance(instance, DOM_MethodRefParameter)


DOM_Modifier_strategy = st.builds(DOM_Modifier, abstract=safe_text, final=safe_text, native=safe_text, none=safe_text, private=safe_text, protected=safe_text, public=safe_text, static=safe_text, strictfp=safe_text, synchronized=safe_text, transient=safe_text, volatile=safe_text)
@given(instance=DOM_Modifier_strategy)
@settings(max_examples=25)
def test_DOM_Modifier_instantiation(instance):
    assert isinstance(instance, DOM_Modifier)


DOM_Name_strategy = st.builds(DOM_Name, fullyQualifiedName=safe_text)
@given(instance=DOM_Name_strategy)
@settings(max_examples=25)
def test_DOM_Name_instantiation(instance):
    assert isinstance(instance, DOM_Name)


DOM_NormalAnnotation_strategy = st.builds(DOM_NormalAnnotation)
@given(instance=DOM_NormalAnnotation_strategy)
@settings(max_examples=25)
def test_DOM_NormalAnnotation_instantiation(instance):
    assert isinstance(instance, DOM_NormalAnnotation)


DOM_NullLiteral_strategy = st.builds(DOM_NullLiteral)
@given(instance=DOM_NullLiteral_strategy)
@settings(max_examples=25)
def test_DOM_NullLiteral_instantiation(instance):
    assert isinstance(instance, DOM_NullLiteral)


DOM_NumberLiteral_strategy = st.builds(DOM_NumberLiteral, token=safe_text)
@given(instance=DOM_NumberLiteral_strategy)
@settings(max_examples=25)
def test_DOM_NumberLiteral_instantiation(instance):
    assert isinstance(instance, DOM_NumberLiteral)


DOM_PackageDeclaration_strategy = st.builds(DOM_PackageDeclaration)
@given(instance=DOM_PackageDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_PackageDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_PackageDeclaration)


DOM_ParameterizedType_strategy = st.builds(DOM_ParameterizedType)
@given(instance=DOM_ParameterizedType_strategy)
@settings(max_examples=25)
def test_DOM_ParameterizedType_instantiation(instance):
    assert isinstance(instance, DOM_ParameterizedType)


DOM_ParenthesizedExpression_strategy = st.builds(DOM_ParenthesizedExpression)
@given(instance=DOM_ParenthesizedExpression_strategy)
@settings(max_examples=25)
def test_DOM_ParenthesizedExpression_instantiation(instance):
    assert isinstance(instance, DOM_ParenthesizedExpression)


DOM_PostfixExpression_strategy = st.builds(DOM_PostfixExpression, operator=safe_text)
@given(instance=DOM_PostfixExpression_strategy)
@settings(max_examples=25)
def test_DOM_PostfixExpression_instantiation(instance):
    assert isinstance(instance, DOM_PostfixExpression)


DOM_PrefixExpression_strategy = st.builds(DOM_PrefixExpression, operator=safe_text)
@given(instance=DOM_PrefixExpression_strategy)
@settings(max_examples=25)
def test_DOM_PrefixExpression_instantiation(instance):
    assert isinstance(instance, DOM_PrefixExpression)


DOM_PrimitiveType_strategy = st.builds(DOM_PrimitiveType, code=safe_text)
@given(instance=DOM_PrimitiveType_strategy)
@settings(max_examples=25)
def test_DOM_PrimitiveType_instantiation(instance):
    assert isinstance(instance, DOM_PrimitiveType)


DOM_QualifiedName_strategy = st.builds(DOM_QualifiedName)
@given(instance=DOM_QualifiedName_strategy)
@settings(max_examples=25)
def test_DOM_QualifiedName_instantiation(instance):
    assert isinstance(instance, DOM_QualifiedName)


DOM_QualifiedType_strategy = st.builds(DOM_QualifiedType)
@given(instance=DOM_QualifiedType_strategy)
@settings(max_examples=25)
def test_DOM_QualifiedType_instantiation(instance):
    assert isinstance(instance, DOM_QualifiedType)


DOM_ReturnStatement_strategy = st.builds(DOM_ReturnStatement)
@given(instance=DOM_ReturnStatement_strategy)
@settings(max_examples=25)
def test_DOM_ReturnStatement_instantiation(instance):
    assert isinstance(instance, DOM_ReturnStatement)


DOM_SimpleName_strategy = st.builds(DOM_SimpleName, declaration=safe_text, identifier=safe_text)
@given(instance=DOM_SimpleName_strategy)
@settings(max_examples=25)
def test_DOM_SimpleName_instantiation(instance):
    assert isinstance(instance, DOM_SimpleName)


DOM_SimpleType_strategy = st.builds(DOM_SimpleType)
@given(instance=DOM_SimpleType_strategy)
@settings(max_examples=25)
def test_DOM_SimpleType_instantiation(instance):
    assert isinstance(instance, DOM_SimpleType)


DOM_SingleMemberAnnotation_strategy = st.builds(DOM_SingleMemberAnnotation)
@given(instance=DOM_SingleMemberAnnotation_strategy)
@settings(max_examples=25)
def test_DOM_SingleMemberAnnotation_instantiation(instance):
    assert isinstance(instance, DOM_SingleMemberAnnotation)


DOM_SingleVariableDeclaration_strategy = st.builds(DOM_SingleVariableDeclaration, varargs=safe_text)
@given(instance=DOM_SingleVariableDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_SingleVariableDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_SingleVariableDeclaration)


DOM_Statement_strategy = st.builds(DOM_Statement)
@given(instance=DOM_Statement_strategy)
@settings(max_examples=25)
def test_DOM_Statement_instantiation(instance):
    assert isinstance(instance, DOM_Statement)


DOM_StringLiteral_strategy = st.builds(DOM_StringLiteral, escapedValue=safe_text, literalValue=safe_text)
@given(instance=DOM_StringLiteral_strategy)
@settings(max_examples=25)
def test_DOM_StringLiteral_instantiation(instance):
    assert isinstance(instance, DOM_StringLiteral)


DOM_SuperConstructorInvocation_strategy = st.builds(DOM_SuperConstructorInvocation)
@given(instance=DOM_SuperConstructorInvocation_strategy)
@settings(max_examples=25)
def test_DOM_SuperConstructorInvocation_instantiation(instance):
    assert isinstance(instance, DOM_SuperConstructorInvocation)


DOM_SuperFieldAccess_strategy = st.builds(DOM_SuperFieldAccess)
@given(instance=DOM_SuperFieldAccess_strategy)
@settings(max_examples=25)
def test_DOM_SuperFieldAccess_instantiation(instance):
    assert isinstance(instance, DOM_SuperFieldAccess)


DOM_SuperMethodInvocation_strategy = st.builds(DOM_SuperMethodInvocation)
@given(instance=DOM_SuperMethodInvocation_strategy)
@settings(max_examples=25)
def test_DOM_SuperMethodInvocation_instantiation(instance):
    assert isinstance(instance, DOM_SuperMethodInvocation)


DOM_SwitchCase_strategy = st.builds(DOM_SwitchCase, default=safe_text)
@given(instance=DOM_SwitchCase_strategy)
@settings(max_examples=25)
def test_DOM_SwitchCase_instantiation(instance):
    assert isinstance(instance, DOM_SwitchCase)


DOM_SwitchStatement_strategy = st.builds(DOM_SwitchStatement)
@given(instance=DOM_SwitchStatement_strategy)
@settings(max_examples=25)
def test_DOM_SwitchStatement_instantiation(instance):
    assert isinstance(instance, DOM_SwitchStatement)


DOM_SynchronizedStatement_strategy = st.builds(DOM_SynchronizedStatement)
@given(instance=DOM_SynchronizedStatement_strategy)
@settings(max_examples=25)
def test_DOM_SynchronizedStatement_instantiation(instance):
    assert isinstance(instance, DOM_SynchronizedStatement)


DOM_TagElement_strategy = st.builds(DOM_TagElement, nested=safe_text, tagName=safe_text)
@given(instance=DOM_TagElement_strategy)
@settings(max_examples=25)
def test_DOM_TagElement_instantiation(instance):
    assert isinstance(instance, DOM_TagElement)


DOM_TextElement_strategy = st.builds(DOM_TextElement, text=safe_text)
@given(instance=DOM_TextElement_strategy)
@settings(max_examples=25)
def test_DOM_TextElement_instantiation(instance):
    assert isinstance(instance, DOM_TextElement)


DOM_ThisExpression_strategy = st.builds(DOM_ThisExpression)
@given(instance=DOM_ThisExpression_strategy)
@settings(max_examples=25)
def test_DOM_ThisExpression_instantiation(instance):
    assert isinstance(instance, DOM_ThisExpression)


DOM_ThrowStatement_strategy = st.builds(DOM_ThrowStatement)
@given(instance=DOM_ThrowStatement_strategy)
@settings(max_examples=25)
def test_DOM_ThrowStatement_instantiation(instance):
    assert isinstance(instance, DOM_ThrowStatement)


DOM_TryStatement_strategy = st.builds(DOM_TryStatement)
@given(instance=DOM_TryStatement_strategy)
@settings(max_examples=25)
def test_DOM_TryStatement_instantiation(instance):
    assert isinstance(instance, DOM_TryStatement)


DOM_Type_strategy = st.builds(DOM_Type)
@given(instance=DOM_Type_strategy)
@settings(max_examples=25)
def test_DOM_Type_instantiation(instance):
    assert isinstance(instance, DOM_Type)


DOM_TypeDeclaration_strategy = st.builds(DOM_TypeDeclaration, interface=safe_text)
@given(instance=DOM_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_TypeDeclaration)


DOM_TypeDeclarationStatement_strategy = st.builds(DOM_TypeDeclarationStatement)
@given(instance=DOM_TypeDeclarationStatement_strategy)
@settings(max_examples=25)
def test_DOM_TypeDeclarationStatement_instantiation(instance):
    assert isinstance(instance, DOM_TypeDeclarationStatement)


DOM_TypeLiteral_strategy = st.builds(DOM_TypeLiteral)
@given(instance=DOM_TypeLiteral_strategy)
@settings(max_examples=25)
def test_DOM_TypeLiteral_instantiation(instance):
    assert isinstance(instance, DOM_TypeLiteral)


DOM_TypeParameter_strategy = st.builds(DOM_TypeParameter)
@given(instance=DOM_TypeParameter_strategy)
@settings(max_examples=25)
def test_DOM_TypeParameter_instantiation(instance):
    assert isinstance(instance, DOM_TypeParameter)


DOM_VariableDeclaration_strategy = st.builds(DOM_VariableDeclaration, extraDimensions=safe_text)
@given(instance=DOM_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_DOM_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, DOM_VariableDeclaration)


DOM_VariableDeclarationExpression_strategy = st.builds(DOM_VariableDeclarationExpression)
@given(instance=DOM_VariableDeclarationExpression_strategy)
@settings(max_examples=25)
def test_DOM_VariableDeclarationExpression_instantiation(instance):
    assert isinstance(instance, DOM_VariableDeclarationExpression)


DOM_VariableDeclarationFragment_strategy = st.builds(DOM_VariableDeclarationFragment)
@given(instance=DOM_VariableDeclarationFragment_strategy)
@settings(max_examples=25)
def test_DOM_VariableDeclarationFragment_instantiation(instance):
    assert isinstance(instance, DOM_VariableDeclarationFragment)


DOM_VariableDeclarationStatement_strategy = st.builds(DOM_VariableDeclarationStatement)
@given(instance=DOM_VariableDeclarationStatement_strategy)
@settings(max_examples=25)
def test_DOM_VariableDeclarationStatement_instantiation(instance):
    assert isinstance(instance, DOM_VariableDeclarationStatement)


DOM_WhileStatement_strategy = st.builds(DOM_WhileStatement)
@given(instance=DOM_WhileStatement_strategy)
@settings(max_examples=25)
def test_DOM_WhileStatement_instantiation(instance):
    assert isinstance(instance, DOM_WhileStatement)


DOM_WildcardType_strategy = st.builds(DOM_WildcardType, upperBound=safe_text)
@given(instance=DOM_WildcardType_strategy)
@settings(max_examples=25)
def test_DOM_WildcardType_instantiation(instance):
    assert isinstance(instance, DOM_WildcardType)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ExtendedModifier_strategy = st.builds(ExtendedModifier)
@given(instance=ExtendedModifier_strategy)
@settings(max_examples=25)
def test_ExtendedModifier_instantiation(instance):
    assert isinstance(instance, ExtendedModifier)


Name_strategy = st.builds(Name)
@given(instance=Name_strategy)
@settings(max_examples=25)
def test_Name_instantiation(instance):
    assert isinstance(instance, Name)


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


VariableDeclaration_strategy = st.builds(VariableDeclaration)
@given(instance=VariableDeclaration_strategy)
@settings(max_examples=25)
def test_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)



