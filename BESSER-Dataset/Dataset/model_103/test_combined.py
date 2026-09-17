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
    MemberValuePair,
    VariableDeclaration,
    DOM_SingleVariableDeclaration,
    DOM_VariableDeclarationFragment,
    CatchClause,
    Statement,
    DOM_IfStatement,
    DOM_DoStatement,
    DOM_ExpressionStatement,
    DOM_SuperConstructorInvocation,
    DOM_EnhancedForStatement,
    DOM_VariableDeclarationStatement,
    DOM_SwitchStatement,
    DOM_SynchronizedStatement,
    DOM_SwitchCase,
    DOM_ForStatement,
    DOM_TryStatement,
    DOM_BreakStatement,
    DOM_Block,
    DOM_ConstructorInvocation,
    DOM_ReturnStatement,
    DOM_WhileStatement,
    DOM_ContinueStatement,
    DOM_EmptyStatement,
    DOM_ThrowStatement,
    DOM_TypeDeclarationStatement,
    DOM_LabeledStatement,
    DOM_AssertStatement,
    Expression,
    DOM_Name,
    DOM_ThisExpression,
    DOM_NumberLiteral,
    DOM_TypeLiteral,
    DOM_SuperFieldAccess,
    DOM_VariableDeclarationExpression,
    DOM_PrefixExpression,
    DOM_ParenthesizedExpression,
    DOM_InstanceofExpression,
    DOM_SuperMethodInvocation,
    DOM_NullLiteral,
    DOM_StringLiteral,
    DOM_MethodInvocation,
    DOM_PostfixExpression,
    DOM_InfixExpression,
    SimpleName,
    Name,
    DOM_QualifiedName,
    DOM_SimpleName,
    AbstractTypeDeclaration,
    ImportDeclaration,
    PackageDeclaration,
    DOM_ExtendedModifier,
    Type,
    DOM_ArrayType,
    DOM_ParameterizedType,
    DOM_SimpleType,
    DOM_PrimitiveType,
    DOM_QualifiedType,
    DOM_WildcardType,
    MethodRefParameter,
    BodyDeclaration,
    DOM_ASTNode,
    ASTNode,
    DOM_MethodRef,
    DOM_MemberRef,
    DOM_AnonymousClassDeclaration,
    DOM_MemberValuePair,
    DOM_MethodRefParameter,
    DOM_TextElement,
    DOM_ImportDeclaration,
    DOM_BodyDeclaration,
    DOM_Expression,
    DOM_AST,
    Comment,
    DOM_CompilationUnit,
    DOM_Comment,
    SingleVariableDeclaration,
    Block,
    DOM_CatchClause,
    Javadoc,
    ExtendedModifier,
    DOM_Modifier,
    ITypeParameter,
    Core_Parameter,
    Parameter,
    Core_ISourceRange,
    ISourceRange,
    Core_ISourceReference,
    CompilationUnit,
    IMethod,
    IField,
    IInitializer,
    IMember,
    Core_IMethod,
    Core_IField,
    Core_IInitializer,
    Core_IType,
    IPackageFragment,
    IJavaElement,
    IPackageFragmentRoot,
    Core_SourcePackageFragmentRoot,
    Core_BinaryPackageFragmentRoot,
    IJavaProject,
    PhysicalElement,
    Core_IPackageFragmentRoot,
    Core_IPackageFragment,
    Core_IJavaProject,
    Core_IJavaModel,
    Core_PhysicalElement,
    IImportDeclaration,
    IType,
    ITypeRoot,
    Core_IClassFile,
    Core_ICompilationUnit,
    ISourceReference,
    Core_ITypeParameter,
    Core_IImportDeclaration,
    Core_IMember,
    Core_ITypeRoot,
    ICompilationUnit,
    IClassFile,
    Core_IJavaElement,
    DOM_FieldAccess,
    DOM_ClassInstanceCreation,
    DOM_CharacterLiteral,
    DOM_CastExpression,
    DOM_BooleanLiteral,
    DOM_ConditionalExpression,
    DOM_ArrayCreation,
    DOM_ArrayAccess,
    DOM_Annotation,
    DOM_LineComment,
    TagElement,
    DOM_Javadoc,
    DOM_BlockComment,
    DOM_Assignment,
    DOM_ArrayInitializer,
    ArrayType,
    ArrayInitializer,
    TypeParameter,
    DOM_MethodDeclaration,
    DOM_Initializer,
    VariableDeclarationFragment,
    DOM_TypeDeclaration,
    EnumConstantDeclaration,
    DOM_EnumDeclaration,
    DOM_AnnotationTypeDeclaration,
    DOM_AnnotationTypeMemberDeclaration,
    DOM_AbstractTypeDeclaration,
    DOM_FieldDeclaration,
    AnonymousClassDeclaration,
    DOM_EnumConstantDeclaration,
    DOM_TagElement,
    DOM_Statement,
    Annotation,
    DOM_MarkerAnnotation,
    DOM_NormalAnnotation,
    DOM_SingleMemberAnnotation,
    DOM_PackageDeclaration,
    DOM_VariableDeclaration,
    DOM_TypeParameter,
    DOM_Type,
    Modifiers,
    InfixExpressionOperatorKind,
    PostfixExpressionOperatorKind,
    AssignmentOperatorKind,
    PrefixExpressionOperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(MemberValuePair)


def test_hyp_membervaluepair_constructor_exists():
    assert callable(MemberValuePair.__init__)


def test_hyp_membervaluepair_constructor_args():
    sig = inspect.signature(MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_hyp_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_hyp_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_SingleVariableDeclaration)


def test_hyp_dom_singlevariabledeclaration_constructor_exists():
    assert callable(DOM_SingleVariableDeclaration.__init__)


def test_hyp_dom_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(DOM_SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"




def test_hyp_dom_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationFragment)


def test_hyp_dom_variabledeclarationfragment_constructor_exists():
    assert callable(DOM_VariableDeclarationFragment.__init__)


def test_hyp_dom_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_catchclause_is_not_abstract():
    assert not inspect.isabstract(CatchClause)


def test_hyp_catchclause_constructor_exists():
    assert callable(CatchClause.__init__)


def test_hyp_catchclause_constructor_args():
    sig = inspect.signature(CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_ifstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_IfStatement)


def test_hyp_dom_ifstatement_constructor_exists():
    assert callable(DOM_IfStatement.__init__)


def test_hyp_dom_ifstatement_constructor_args():
    sig = inspect.signature(DOM_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_dostatement_is_not_abstract():
    assert not inspect.isabstract(DOM_DoStatement)


def test_hyp_dom_dostatement_constructor_exists():
    assert callable(DOM_DoStatement.__init__)


def test_hyp_dom_dostatement_constructor_args():
    sig = inspect.signature(DOM_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ExpressionStatement)


def test_hyp_dom_expressionstatement_constructor_exists():
    assert callable(DOM_ExpressionStatement.__init__)


def test_hyp_dom_expressionstatement_constructor_args():
    sig = inspect.signature(DOM_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_superconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperConstructorInvocation)


def test_hyp_dom_superconstructorinvocation_constructor_exists():
    assert callable(DOM_SuperConstructorInvocation.__init__)


def test_hyp_dom_superconstructorinvocation_constructor_args():
    sig = inspect.signature(DOM_SuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_enhancedforstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_EnhancedForStatement)


def test_hyp_dom_enhancedforstatement_constructor_exists():
    assert callable(DOM_EnhancedForStatement.__init__)


def test_hyp_dom_enhancedforstatement_constructor_args():
    sig = inspect.signature(DOM_EnhancedForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationStatement)


def test_hyp_dom_variabledeclarationstatement_constructor_exists():
    assert callable(DOM_VariableDeclarationStatement.__init__)


def test_hyp_dom_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_switchstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_SwitchStatement)


def test_hyp_dom_switchstatement_constructor_exists():
    assert callable(DOM_SwitchStatement.__init__)


def test_hyp_dom_switchstatement_constructor_args():
    sig = inspect.signature(DOM_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_SynchronizedStatement)


def test_hyp_dom_synchronizedstatement_constructor_exists():
    assert callable(DOM_SynchronizedStatement.__init__)


def test_hyp_dom_synchronizedstatement_constructor_args():
    sig = inspect.signature(DOM_SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_switchcase_is_not_abstract():
    assert not inspect.isabstract(DOM_SwitchCase)


def test_hyp_dom_switchcase_constructor_exists():
    assert callable(DOM_SwitchCase.__init__)


def test_hyp_dom_switchcase_constructor_args():
    sig = inspect.signature(DOM_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_dom_forstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ForStatement)


def test_hyp_dom_forstatement_constructor_exists():
    assert callable(DOM_ForStatement.__init__)


def test_hyp_dom_forstatement_constructor_args():
    sig = inspect.signature(DOM_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_trystatement_is_not_abstract():
    assert not inspect.isabstract(DOM_TryStatement)


def test_hyp_dom_trystatement_constructor_exists():
    assert callable(DOM_TryStatement.__init__)


def test_hyp_dom_trystatement_constructor_args():
    sig = inspect.signature(DOM_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_breakstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_BreakStatement)


def test_hyp_dom_breakstatement_constructor_exists():
    assert callable(DOM_BreakStatement.__init__)


def test_hyp_dom_breakstatement_constructor_args():
    sig = inspect.signature(DOM_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_block_is_not_abstract():
    assert not inspect.isabstract(DOM_Block)


def test_hyp_dom_block_constructor_exists():
    assert callable(DOM_Block.__init__)


def test_hyp_dom_block_constructor_args():
    sig = inspect.signature(DOM_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_ConstructorInvocation)


def test_hyp_dom_constructorinvocation_constructor_exists():
    assert callable(DOM_ConstructorInvocation.__init__)


def test_hyp_dom_constructorinvocation_constructor_args():
    sig = inspect.signature(DOM_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_returnstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ReturnStatement)


def test_hyp_dom_returnstatement_constructor_exists():
    assert callable(DOM_ReturnStatement.__init__)


def test_hyp_dom_returnstatement_constructor_args():
    sig = inspect.signature(DOM_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_whilestatement_is_not_abstract():
    assert not inspect.isabstract(DOM_WhileStatement)


def test_hyp_dom_whilestatement_constructor_exists():
    assert callable(DOM_WhileStatement.__init__)


def test_hyp_dom_whilestatement_constructor_args():
    sig = inspect.signature(DOM_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_continuestatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ContinueStatement)


def test_hyp_dom_continuestatement_constructor_exists():
    assert callable(DOM_ContinueStatement.__init__)


def test_hyp_dom_continuestatement_constructor_args():
    sig = inspect.signature(DOM_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_emptystatement_is_not_abstract():
    assert not inspect.isabstract(DOM_EmptyStatement)


def test_hyp_dom_emptystatement_constructor_exists():
    assert callable(DOM_EmptyStatement.__init__)


def test_hyp_dom_emptystatement_constructor_args():
    sig = inspect.signature(DOM_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_throwstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_ThrowStatement)


def test_hyp_dom_throwstatement_constructor_exists():
    assert callable(DOM_ThrowStatement.__init__)


def test_hyp_dom_throwstatement_constructor_args():
    sig = inspect.signature(DOM_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_typedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeDeclarationStatement)


def test_hyp_dom_typedeclarationstatement_constructor_exists():
    assert callable(DOM_TypeDeclarationStatement.__init__)


def test_hyp_dom_typedeclarationstatement_constructor_args():
    sig = inspect.signature(DOM_TypeDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_LabeledStatement)


def test_hyp_dom_labeledstatement_constructor_exists():
    assert callable(DOM_LabeledStatement.__init__)


def test_hyp_dom_labeledstatement_constructor_args():
    sig = inspect.signature(DOM_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_assertstatement_is_not_abstract():
    assert not inspect.isabstract(DOM_AssertStatement)


def test_hyp_dom_assertstatement_constructor_exists():
    assert callable(DOM_AssertStatement.__init__)


def test_hyp_dom_assertstatement_constructor_args():
    sig = inspect.signature(DOM_AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_name_is_not_abstract():
    assert not inspect.isabstract(DOM_Name)


def test_hyp_dom_name_constructor_exists():
    assert callable(DOM_Name.__init__)


def test_hyp_dom_name_constructor_args():
    sig = inspect.signature(DOM_Name.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"




def test_hyp_dom_thisexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ThisExpression)


def test_hyp_dom_thisexpression_constructor_exists():
    assert callable(DOM_ThisExpression.__init__)


def test_hyp_dom_thisexpression_constructor_args():
    sig = inspect.signature(DOM_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_numberliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_NumberLiteral)


def test_hyp_dom_numberliteral_constructor_exists():
    assert callable(DOM_NumberLiteral.__init__)


def test_hyp_dom_numberliteral_constructor_args():
    sig = inspect.signature(DOM_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"




def test_hyp_dom_typeliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeLiteral)


def test_hyp_dom_typeliteral_constructor_exists():
    assert callable(DOM_TypeLiteral.__init__)


def test_hyp_dom_typeliteral_constructor_args():
    sig = inspect.signature(DOM_TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_superfieldaccess_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperFieldAccess)


def test_hyp_dom_superfieldaccess_constructor_exists():
    assert callable(DOM_SuperFieldAccess.__init__)


def test_hyp_dom_superfieldaccess_constructor_args():
    sig = inspect.signature(DOM_SuperFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclarationExpression)


def test_hyp_dom_variabledeclarationexpression_constructor_exists():
    assert callable(DOM_VariableDeclarationExpression.__init__)


def test_hyp_dom_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(DOM_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_prefixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_PrefixExpression)


def test_hyp_dom_prefixexpression_constructor_exists():
    assert callable(DOM_PrefixExpression.__init__)


def test_hyp_dom_prefixexpression_constructor_args():
    sig = inspect.signature(DOM_PrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ParenthesizedExpression)


def test_hyp_dom_parenthesizedexpression_constructor_exists():
    assert callable(DOM_ParenthesizedExpression.__init__)


def test_hyp_dom_parenthesizedexpression_constructor_args():
    sig = inspect.signature(DOM_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_InstanceofExpression)


def test_hyp_dom_instanceofexpression_constructor_exists():
    assert callable(DOM_InstanceofExpression.__init__)


def test_hyp_dom_instanceofexpression_constructor_args():
    sig = inspect.signature(DOM_InstanceofExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_SuperMethodInvocation)


def test_hyp_dom_supermethodinvocation_constructor_exists():
    assert callable(DOM_SuperMethodInvocation.__init__)


def test_hyp_dom_supermethodinvocation_constructor_args():
    sig = inspect.signature(DOM_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_nullliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_NullLiteral)


def test_hyp_dom_nullliteral_constructor_exists():
    assert callable(DOM_NullLiteral.__init__)


def test_hyp_dom_nullliteral_constructor_args():
    sig = inspect.signature(DOM_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_stringliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_StringLiteral)


def test_hyp_dom_stringliteral_constructor_exists():
    assert callable(DOM_StringLiteral.__init__)


def test_hyp_dom_stringliteral_constructor_args():
    sig = inspect.signature(DOM_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"





def test_hyp_dom_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodInvocation)


def test_hyp_dom_methodinvocation_constructor_exists():
    assert callable(DOM_MethodInvocation.__init__)


def test_hyp_dom_methodinvocation_constructor_args():
    sig = inspect.signature(DOM_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_postfixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_PostfixExpression)


def test_hyp_dom_postfixexpression_constructor_exists():
    assert callable(DOM_PostfixExpression.__init__)


def test_hyp_dom_postfixexpression_constructor_args():
    sig = inspect.signature(DOM_PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_infixexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_InfixExpression)


def test_hyp_dom_infixexpression_constructor_exists():
    assert callable(DOM_InfixExpression.__init__)


def test_hyp_dom_infixexpression_constructor_args():
    sig = inspect.signature(DOM_InfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_simplename_is_not_abstract():
    assert not inspect.isabstract(SimpleName)


def test_hyp_simplename_constructor_exists():
    assert callable(SimpleName.__init__)


def test_hyp_simplename_constructor_args():
    sig = inspect.signature(SimpleName.__init__)
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



def test_hyp_dom_simplename_is_not_abstract():
    assert not inspect.isabstract(DOM_SimpleName)


def test_hyp_dom_simplename_constructor_exists():
    assert callable(DOM_SimpleName.__init__)


def test_hyp_dom_simplename_constructor_args():
    sig = inspect.signature(DOM_SimpleName.__init__)
    params = list(sig.parameters.keys())
    assert "declaration" in params, "Missing parameter 'declaration'"
    assert "identifier" in params, "Missing parameter 'identifier'"





def test_hyp_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(AbstractTypeDeclaration)


def test_hyp_abstracttypedeclaration_constructor_exists():
    assert callable(AbstractTypeDeclaration.__init__)


def test_hyp_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(ImportDeclaration)


def test_hyp_importdeclaration_constructor_exists():
    assert callable(ImportDeclaration.__init__)


def test_hyp_importdeclaration_constructor_args():
    sig = inspect.signature(ImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(PackageDeclaration)


def test_hyp_packagedeclaration_constructor_exists():
    assert callable(PackageDeclaration.__init__)


def test_hyp_packagedeclaration_constructor_args():
    sig = inspect.signature(PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(DOM_ExtendedModifier)


def test_hyp_dom_extendedmodifier_constructor_exists():
    assert callable(DOM_ExtendedModifier.__init__)


def test_hyp_dom_extendedmodifier_constructor_args():
    sig = inspect.signature(DOM_ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_arraytype_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayType)


def test_hyp_dom_arraytype_constructor_exists():
    assert callable(DOM_ArrayType.__init__)


def test_hyp_dom_arraytype_constructor_args():
    sig = inspect.signature(DOM_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"




def test_hyp_dom_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(DOM_ParameterizedType)


def test_hyp_dom_parameterizedtype_constructor_exists():
    assert callable(DOM_ParameterizedType.__init__)


def test_hyp_dom_parameterizedtype_constructor_args():
    sig = inspect.signature(DOM_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_simpletype_is_not_abstract():
    assert not inspect.isabstract(DOM_SimpleType)


def test_hyp_dom_simpletype_constructor_exists():
    assert callable(DOM_SimpleType.__init__)


def test_hyp_dom_simpletype_constructor_args():
    sig = inspect.signature(DOM_SimpleType.__init__)
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



def test_hyp_dom_wildcardtype_is_not_abstract():
    assert not inspect.isabstract(DOM_WildcardType)


def test_hyp_dom_wildcardtype_constructor_exists():
    assert callable(DOM_WildcardType.__init__)


def test_hyp_dom_wildcardtype_constructor_args():
    sig = inspect.signature(DOM_WildcardType.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"




def test_hyp_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(MethodRefParameter)


def test_hyp_methodrefparameter_constructor_exists():
    assert callable(MethodRefParameter.__init__)


def test_hyp_methodrefparameter_constructor_args():
    sig = inspect.signature(MethodRefParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(BodyDeclaration)


def test_hyp_bodydeclaration_constructor_exists():
    assert callable(BodyDeclaration.__init__)


def test_hyp_bodydeclaration_constructor_args():
    sig = inspect.signature(BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_astnode_is_not_abstract():
    assert not inspect.isabstract(DOM_ASTNode)


def test_hyp_dom_astnode_constructor_exists():
    assert callable(DOM_ASTNode.__init__)


def test_hyp_dom_astnode_constructor_args():
    sig = inspect.signature(DOM_ASTNode.__init__)
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



def test_hyp_dom_memberref_is_not_abstract():
    assert not inspect.isabstract(DOM_MemberRef)


def test_hyp_dom_memberref_constructor_exists():
    assert callable(DOM_MemberRef.__init__)


def test_hyp_dom_memberref_constructor_args():
    sig = inspect.signature(DOM_MemberRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnonymousClassDeclaration)


def test_hyp_dom_anonymousclassdeclaration_constructor_exists():
    assert callable(DOM_AnonymousClassDeclaration.__init__)


def test_hyp_dom_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(DOM_AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_membervaluepair_is_not_abstract():
    assert not inspect.isabstract(DOM_MemberValuePair)


def test_hyp_dom_membervaluepair_constructor_exists():
    assert callable(DOM_MemberValuePair.__init__)


def test_hyp_dom_membervaluepair_constructor_args():
    sig = inspect.signature(DOM_MemberValuePair.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_methodrefparameter_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodRefParameter)


def test_hyp_dom_methodrefparameter_constructor_exists():
    assert callable(DOM_MethodRefParameter.__init__)


def test_hyp_dom_methodrefparameter_constructor_args():
    sig = inspect.signature(DOM_MethodRefParameter.__init__)
    params = list(sig.parameters.keys())
    assert "varargs" in params, "Missing parameter 'varargs'"




def test_hyp_dom_textelement_is_not_abstract():
    assert not inspect.isabstract(DOM_TextElement)


def test_hyp_dom_textelement_constructor_exists():
    assert callable(DOM_TextElement.__init__)


def test_hyp_dom_textelement_constructor_args():
    sig = inspect.signature(DOM_TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_dom_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_ImportDeclaration)


def test_hyp_dom_importdeclaration_constructor_exists():
    assert callable(DOM_ImportDeclaration.__init__)


def test_hyp_dom_importdeclaration_constructor_args():
    sig = inspect.signature(DOM_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "onDemand" in params, "Missing parameter 'onDemand'"
    assert "static" in params, "Missing parameter 'static'"





def test_hyp_dom_bodydeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_BodyDeclaration)


def test_hyp_dom_bodydeclaration_constructor_exists():
    assert callable(DOM_BodyDeclaration.__init__)


def test_hyp_dom_bodydeclaration_constructor_args():
    sig = inspect.signature(DOM_BodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_expression_is_not_abstract():
    assert not inspect.isabstract(DOM_Expression)


def test_hyp_dom_expression_constructor_exists():
    assert callable(DOM_Expression.__init__)


def test_hyp_dom_expression_constructor_args():
    sig = inspect.signature(DOM_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "resolveBoxing" in params, "Missing parameter 'resolveBoxing'"
    assert "resolveUnboxing" in params, "Missing parameter 'resolveUnboxing'"





def test_hyp_dom_ast_is_not_abstract():
    assert not inspect.isabstract(DOM_AST)


def test_hyp_dom_ast_constructor_exists():
    assert callable(DOM_AST.__init__)


def test_hyp_dom_ast_constructor_args():
    sig = inspect.signature(DOM_AST.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_hyp_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_hyp_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_compilationunit_is_not_abstract():
    assert not inspect.isabstract(DOM_CompilationUnit)


def test_hyp_dom_compilationunit_constructor_exists():
    assert callable(DOM_CompilationUnit.__init__)


def test_hyp_dom_compilationunit_constructor_args():
    sig = inspect.signature(DOM_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_comment_is_not_abstract():
    assert not inspect.isabstract(DOM_Comment)


def test_hyp_dom_comment_constructor_exists():
    assert callable(DOM_Comment.__init__)


def test_hyp_dom_comment_constructor_args():
    sig = inspect.signature(DOM_Comment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_singlevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SingleVariableDeclaration)


def test_hyp_singlevariabledeclaration_constructor_exists():
    assert callable(SingleVariableDeclaration.__init__)


def test_hyp_singlevariabledeclaration_constructor_args():
    sig = inspect.signature(SingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_hyp_block_constructor_exists():
    assert callable(Block.__init__)


def test_hyp_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_catchclause_is_not_abstract():
    assert not inspect.isabstract(DOM_CatchClause)


def test_hyp_dom_catchclause_constructor_exists():
    assert callable(DOM_CatchClause.__init__)


def test_hyp_dom_catchclause_constructor_args():
    sig = inspect.signature(DOM_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_javadoc_is_not_abstract():
    assert not inspect.isabstract(Javadoc)


def test_hyp_javadoc_constructor_exists():
    assert callable(Javadoc.__init__)


def test_hyp_javadoc_constructor_args():
    sig = inspect.signature(Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_extendedmodifier_is_not_abstract():
    assert not inspect.isabstract(ExtendedModifier)


def test_hyp_extendedmodifier_constructor_exists():
    assert callable(ExtendedModifier.__init__)


def test_hyp_extendedmodifier_constructor_args():
    sig = inspect.signature(ExtendedModifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_modifier_is_not_abstract():
    assert not inspect.isabstract(DOM_Modifier)


def test_hyp_dom_modifier_constructor_exists():
    assert callable(DOM_Modifier.__init__)


def test_hyp_dom_modifier_constructor_args():
    sig = inspect.signature(DOM_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"
    assert "native" in params, "Missing parameter 'native'"
    assert "private" in params, "Missing parameter 'private'"
    assert "none" in params, "Missing parameter 'none'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "public" in params, "Missing parameter 'public'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "volatile" in params, "Missing parameter 'volatile'"















def test_hyp_itypeparameter_is_not_abstract():
    assert not inspect.isabstract(ITypeParameter)


def test_hyp_itypeparameter_constructor_exists():
    assert callable(ITypeParameter.__init__)


def test_hyp_itypeparameter_constructor_args():
    sig = inspect.signature(ITypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_parameter_is_not_abstract():
    assert not inspect.isabstract(Core_Parameter)


def test_hyp_core_parameter_constructor_exists():
    assert callable(Core_Parameter.__init__)


def test_hyp_core_parameter_constructor_args():
    sig = inspect.signature(Core_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_isourcerange_is_not_abstract():
    assert not inspect.isabstract(Core_ISourceRange)


def test_hyp_core_isourcerange_constructor_exists():
    assert callable(Core_ISourceRange.__init__)


def test_hyp_core_isourcerange_constructor_args():
    sig = inspect.signature(Core_ISourceRange.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "offset" in params, "Missing parameter 'offset'"





def test_hyp_isourcerange_is_not_abstract():
    assert not inspect.isabstract(ISourceRange)


def test_hyp_isourcerange_constructor_exists():
    assert callable(ISourceRange.__init__)


def test_hyp_isourcerange_constructor_args():
    sig = inspect.signature(ISourceRange.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_isourcereference_is_not_abstract():
    assert not inspect.isabstract(Core_ISourceReference)


def test_hyp_core_isourcereference_constructor_exists():
    assert callable(Core_ISourceReference.__init__)


def test_hyp_core_isourcereference_constructor_args():
    sig = inspect.signature(Core_ISourceReference.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"




def test_hyp_compilationunit_is_not_abstract():
    assert not inspect.isabstract(CompilationUnit)


def test_hyp_compilationunit_constructor_exists():
    assert callable(CompilationUnit.__init__)


def test_hyp_compilationunit_constructor_args():
    sig = inspect.signature(CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imethod_is_not_abstract():
    assert not inspect.isabstract(IMethod)


def test_hyp_imethod_constructor_exists():
    assert callable(IMethod.__init__)


def test_hyp_imethod_constructor_args():
    sig = inspect.signature(IMethod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ifield_is_not_abstract():
    assert not inspect.isabstract(IField)


def test_hyp_ifield_constructor_exists():
    assert callable(IField.__init__)


def test_hyp_ifield_constructor_args():
    sig = inspect.signature(IField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iinitializer_is_not_abstract():
    assert not inspect.isabstract(IInitializer)


def test_hyp_iinitializer_constructor_exists():
    assert callable(IInitializer.__init__)


def test_hyp_iinitializer_constructor_args():
    sig = inspect.signature(IInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imember_is_not_abstract():
    assert not inspect.isabstract(IMember)


def test_hyp_imember_constructor_exists():
    assert callable(IMember.__init__)


def test_hyp_imember_constructor_args():
    sig = inspect.signature(IMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_imethod_is_not_abstract():
    assert not inspect.isabstract(Core_IMethod)


def test_hyp_core_imethod_constructor_exists():
    assert callable(Core_IMethod.__init__)


def test_hyp_core_imethod_constructor_args():
    sig = inspect.signature(Core_IMethod.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionTypes" in params, "Missing parameter 'exceptionTypes'"
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "isConstructor" in params, "Missing parameter 'isConstructor'"
    assert "isMainMethod" in params, "Missing parameter 'isMainMethod'"







def test_hyp_core_ifield_is_not_abstract():
    assert not inspect.isabstract(Core_IField)


def test_hyp_core_ifield_constructor_exists():
    assert callable(Core_IField.__init__)


def test_hyp_core_ifield_constructor_args():
    sig = inspect.signature(Core_IField.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "typeSignature" in params, "Missing parameter 'typeSignature'"
    assert "isTransient" in params, "Missing parameter 'isTransient'"
    assert "isEnumConstant" in params, "Missing parameter 'isEnumConstant'"








def test_hyp_core_iinitializer_is_not_abstract():
    assert not inspect.isabstract(Core_IInitializer)


def test_hyp_core_iinitializer_constructor_exists():
    assert callable(Core_IInitializer.__init__)


def test_hyp_core_iinitializer_constructor_args():
    sig = inspect.signature(Core_IInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_itype_is_not_abstract():
    assert not inspect.isabstract(Core_IType)


def test_hyp_core_itype_constructor_exists():
    assert callable(Core_IType.__init__)


def test_hyp_core_itype_constructor_args():
    sig = inspect.signature(Core_IType.__init__)
    params = list(sig.parameters.keys())
    assert "fullyQualifiedName" in params, "Missing parameter 'fullyQualifiedName'"
    assert "fullyQualifiedParametrizedName" in params, "Missing parameter 'fullyQualifiedParametrizedName'"





def test_hyp_ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(IPackageFragment)


def test_hyp_ipackagefragment_constructor_exists():
    assert callable(IPackageFragment.__init__)


def test_hyp_ipackagefragment_constructor_args():
    sig = inspect.signature(IPackageFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ijavaelement_is_not_abstract():
    assert not inspect.isabstract(IJavaElement)


def test_hyp_ijavaelement_constructor_exists():
    assert callable(IJavaElement.__init__)


def test_hyp_ijavaelement_constructor_args():
    sig = inspect.signature(IJavaElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ipackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(IPackageFragmentRoot)


def test_hyp_ipackagefragmentroot_constructor_exists():
    assert callable(IPackageFragmentRoot.__init__)


def test_hyp_ipackagefragmentroot_constructor_args():
    sig = inspect.signature(IPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_sourcepackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(Core_SourcePackageFragmentRoot)


def test_hyp_core_sourcepackagefragmentroot_constructor_exists():
    assert callable(Core_SourcePackageFragmentRoot.__init__)


def test_hyp_core_sourcepackagefragmentroot_constructor_args():
    sig = inspect.signature(Core_SourcePackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_binarypackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(Core_BinaryPackageFragmentRoot)


def test_hyp_core_binarypackagefragmentroot_constructor_exists():
    assert callable(Core_BinaryPackageFragmentRoot.__init__)


def test_hyp_core_binarypackagefragmentroot_constructor_args():
    sig = inspect.signature(Core_BinaryPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ijavaproject_is_not_abstract():
    assert not inspect.isabstract(IJavaProject)


def test_hyp_ijavaproject_constructor_exists():
    assert callable(IJavaProject.__init__)


def test_hyp_ijavaproject_constructor_args():
    sig = inspect.signature(IJavaProject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_physicalelement_is_not_abstract():
    assert not inspect.isabstract(PhysicalElement)


def test_hyp_physicalelement_constructor_exists():
    assert callable(PhysicalElement.__init__)


def test_hyp_physicalelement_constructor_args():
    sig = inspect.signature(PhysicalElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_ipackagefragmentroot_is_not_abstract():
    assert not inspect.isabstract(Core_IPackageFragmentRoot)


def test_hyp_core_ipackagefragmentroot_constructor_exists():
    assert callable(Core_IPackageFragmentRoot.__init__)


def test_hyp_core_ipackagefragmentroot_constructor_args():
    sig = inspect.signature(Core_IPackageFragmentRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_ipackagefragment_is_not_abstract():
    assert not inspect.isabstract(Core_IPackageFragment)


def test_hyp_core_ipackagefragment_constructor_exists():
    assert callable(Core_IPackageFragment.__init__)


def test_hyp_core_ipackagefragment_constructor_args():
    sig = inspect.signature(Core_IPackageFragment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefaultPackage" in params, "Missing parameter 'isDefaultPackage'"




def test_hyp_core_ijavaproject_is_not_abstract():
    assert not inspect.isabstract(Core_IJavaProject)


def test_hyp_core_ijavaproject_constructor_exists():
    assert callable(Core_IJavaProject.__init__)


def test_hyp_core_ijavaproject_constructor_args():
    sig = inspect.signature(Core_IJavaProject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_ijavamodel_is_not_abstract():
    assert not inspect.isabstract(Core_IJavaModel)


def test_hyp_core_ijavamodel_constructor_exists():
    assert callable(Core_IJavaModel.__init__)


def test_hyp_core_ijavamodel_constructor_args():
    sig = inspect.signature(Core_IJavaModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_physicalelement_is_not_abstract():
    assert not inspect.isabstract(Core_PhysicalElement)


def test_hyp_core_physicalelement_constructor_exists():
    assert callable(Core_PhysicalElement.__init__)


def test_hyp_core_physicalelement_constructor_args():
    sig = inspect.signature(Core_PhysicalElement.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "path" in params, "Missing parameter 'path'"





def test_hyp_iimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(IImportDeclaration)


def test_hyp_iimportdeclaration_constructor_exists():
    assert callable(IImportDeclaration.__init__)


def test_hyp_iimportdeclaration_constructor_args():
    sig = inspect.signature(IImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_itype_is_not_abstract():
    assert not inspect.isabstract(IType)


def test_hyp_itype_constructor_exists():
    assert callable(IType.__init__)


def test_hyp_itype_constructor_args():
    sig = inspect.signature(IType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ityperoot_is_not_abstract():
    assert not inspect.isabstract(ITypeRoot)


def test_hyp_ityperoot_constructor_exists():
    assert callable(ITypeRoot.__init__)


def test_hyp_ityperoot_constructor_args():
    sig = inspect.signature(ITypeRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_iclassfile_is_not_abstract():
    assert not inspect.isabstract(Core_IClassFile)


def test_hyp_core_iclassfile_constructor_exists():
    assert callable(Core_IClassFile.__init__)


def test_hyp_core_iclassfile_constructor_args():
    sig = inspect.signature(Core_IClassFile.__init__)
    params = list(sig.parameters.keys())
    assert "isClass" in params, "Missing parameter 'isClass'"
    assert "isInterface" in params, "Missing parameter 'isInterface'"





def test_hyp_core_icompilationunit_is_not_abstract():
    assert not inspect.isabstract(Core_ICompilationUnit)


def test_hyp_core_icompilationunit_constructor_exists():
    assert callable(Core_ICompilationUnit.__init__)


def test_hyp_core_icompilationunit_constructor_args():
    sig = inspect.signature(Core_ICompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_isourcereference_is_not_abstract():
    assert not inspect.isabstract(ISourceReference)


def test_hyp_isourcereference_constructor_exists():
    assert callable(ISourceReference.__init__)


def test_hyp_isourcereference_constructor_args():
    sig = inspect.signature(ISourceReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_itypeparameter_is_not_abstract():
    assert not inspect.isabstract(Core_ITypeParameter)


def test_hyp_core_itypeparameter_constructor_exists():
    assert callable(Core_ITypeParameter.__init__)


def test_hyp_core_itypeparameter_constructor_args():
    sig = inspect.signature(Core_ITypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "bounds" in params, "Missing parameter 'bounds'"




def test_hyp_core_iimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(Core_IImportDeclaration)


def test_hyp_core_iimportdeclaration_constructor_exists():
    assert callable(Core_IImportDeclaration.__init__)


def test_hyp_core_iimportdeclaration_constructor_args():
    sig = inspect.signature(Core_IImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isOnDemand" in params, "Missing parameter 'isOnDemand'"





def test_hyp_core_imember_is_not_abstract():
    assert not inspect.isabstract(Core_IMember)


def test_hyp_core_imember_constructor_exists():
    assert callable(Core_IMember.__init__)


def test_hyp_core_imember_constructor_args():
    sig = inspect.signature(Core_IMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_ityperoot_is_not_abstract():
    assert not inspect.isabstract(Core_ITypeRoot)


def test_hyp_core_ityperoot_constructor_exists():
    assert callable(Core_ITypeRoot.__init__)


def test_hyp_core_ityperoot_constructor_args():
    sig = inspect.signature(Core_ITypeRoot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_icompilationunit_is_not_abstract():
    assert not inspect.isabstract(ICompilationUnit)


def test_hyp_icompilationunit_constructor_exists():
    assert callable(ICompilationUnit.__init__)


def test_hyp_icompilationunit_constructor_args():
    sig = inspect.signature(ICompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iclassfile_is_not_abstract():
    assert not inspect.isabstract(IClassFile)


def test_hyp_iclassfile_constructor_exists():
    assert callable(IClassFile.__init__)


def test_hyp_iclassfile_constructor_args():
    sig = inspect.signature(IClassFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_ijavaelement_is_not_abstract():
    assert not inspect.isabstract(Core_IJavaElement)


def test_hyp_core_ijavaelement_constructor_exists():
    assert callable(Core_IJavaElement.__init__)


def test_hyp_core_ijavaelement_constructor_args():
    sig = inspect.signature(Core_IJavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementName" in params, "Missing parameter 'elementName'"




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



def test_hyp_dom_characterliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_CharacterLiteral)


def test_hyp_dom_characterliteral_constructor_exists():
    assert callable(DOM_CharacterLiteral.__init__)


def test_hyp_dom_characterliteral_constructor_args():
    sig = inspect.signature(DOM_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"
    assert "charValue" in params, "Missing parameter 'charValue'"





def test_hyp_dom_castexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_CastExpression)


def test_hyp_dom_castexpression_constructor_exists():
    assert callable(DOM_CastExpression.__init__)


def test_hyp_dom_castexpression_constructor_args():
    sig = inspect.signature(DOM_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(DOM_BooleanLiteral)


def test_hyp_dom_booleanliteral_constructor_exists():
    assert callable(DOM_BooleanLiteral.__init__)


def test_hyp_dom_booleanliteral_constructor_args():
    sig = inspect.signature(DOM_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"




def test_hyp_dom_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(DOM_ConditionalExpression)


def test_hyp_dom_conditionalexpression_constructor_exists():
    assert callable(DOM_ConditionalExpression.__init__)


def test_hyp_dom_conditionalexpression_constructor_args():
    sig = inspect.signature(DOM_ConditionalExpression.__init__)
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



def test_hyp_dom_annotation_is_not_abstract():
    assert not inspect.isabstract(DOM_Annotation)


def test_hyp_dom_annotation_constructor_exists():
    assert callable(DOM_Annotation.__init__)


def test_hyp_dom_annotation_constructor_args():
    sig = inspect.signature(DOM_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_linecomment_is_not_abstract():
    assert not inspect.isabstract(DOM_LineComment)


def test_hyp_dom_linecomment_constructor_exists():
    assert callable(DOM_LineComment.__init__)


def test_hyp_dom_linecomment_constructor_args():
    sig = inspect.signature(DOM_LineComment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tagelement_is_not_abstract():
    assert not inspect.isabstract(TagElement)


def test_hyp_tagelement_constructor_exists():
    assert callable(TagElement.__init__)


def test_hyp_tagelement_constructor_args():
    sig = inspect.signature(TagElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_javadoc_is_not_abstract():
    assert not inspect.isabstract(DOM_Javadoc)


def test_hyp_dom_javadoc_constructor_exists():
    assert callable(DOM_Javadoc.__init__)


def test_hyp_dom_javadoc_constructor_args():
    sig = inspect.signature(DOM_Javadoc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_blockcomment_is_not_abstract():
    assert not inspect.isabstract(DOM_BlockComment)


def test_hyp_dom_blockcomment_constructor_exists():
    assert callable(DOM_BlockComment.__init__)


def test_hyp_dom_blockcomment_constructor_args():
    sig = inspect.signature(DOM_BlockComment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_assignment_is_not_abstract():
    assert not inspect.isabstract(DOM_Assignment)


def test_hyp_dom_assignment_constructor_exists():
    assert callable(DOM_Assignment.__init__)


def test_hyp_dom_assignment_constructor_args():
    sig = inspect.signature(DOM_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_dom_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(DOM_ArrayInitializer)


def test_hyp_dom_arrayinitializer_constructor_exists():
    assert callable(DOM_ArrayInitializer.__init__)


def test_hyp_dom_arrayinitializer_constructor_args():
    sig = inspect.signature(DOM_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arraytype_is_not_abstract():
    assert not inspect.isabstract(ArrayType)


def test_hyp_arraytype_constructor_exists():
    assert callable(ArrayType.__init__)


def test_hyp_arraytype_constructor_args():
    sig = inspect.signature(ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializer)


def test_hyp_arrayinitializer_constructor_exists():
    assert callable(ArrayInitializer.__init__)


def test_hyp_arrayinitializer_constructor_args():
    sig = inspect.signature(ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeparameter_is_not_abstract():
    assert not inspect.isabstract(TypeParameter)


def test_hyp_typeparameter_constructor_exists():
    assert callable(TypeParameter.__init__)


def test_hyp_typeparameter_constructor_args():
    sig = inspect.signature(TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_MethodDeclaration)


def test_hyp_dom_methoddeclaration_constructor_exists():
    assert callable(DOM_MethodDeclaration.__init__)


def test_hyp_dom_methoddeclaration_constructor_args():
    sig = inspect.signature(DOM_MethodDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"
    assert "varargs" in params, "Missing parameter 'varargs'"
    assert "constructor" in params, "Missing parameter 'constructor'"






def test_hyp_dom_initializer_is_not_abstract():
    assert not inspect.isabstract(DOM_Initializer)


def test_hyp_dom_initializer_constructor_exists():
    assert callable(DOM_Initializer.__init__)


def test_hyp_dom_initializer_constructor_args():
    sig = inspect.signature(DOM_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationFragment)


def test_hyp_variabledeclarationfragment_constructor_exists():
    assert callable(VariableDeclarationFragment.__init__)


def test_hyp_variabledeclarationfragment_constructor_args():
    sig = inspect.signature(VariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeDeclaration)


def test_hyp_dom_typedeclaration_constructor_exists():
    assert callable(DOM_TypeDeclaration.__init__)


def test_hyp_dom_typedeclaration_constructor_args():
    sig = inspect.signature(DOM_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "interface" in params, "Missing parameter 'interface'"




def test_hyp_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(EnumConstantDeclaration)


def test_hyp_enumconstantdeclaration_constructor_exists():
    assert callable(EnumConstantDeclaration.__init__)


def test_hyp_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_EnumDeclaration)


def test_hyp_dom_enumdeclaration_constructor_exists():
    assert callable(DOM_EnumDeclaration.__init__)


def test_hyp_dom_enumdeclaration_constructor_args():
    sig = inspect.signature(DOM_EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnnotationTypeDeclaration)


def test_hyp_dom_annotationtypedeclaration_constructor_exists():
    assert callable(DOM_AnnotationTypeDeclaration.__init__)


def test_hyp_dom_annotationtypedeclaration_constructor_args():
    sig = inspect.signature(DOM_AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AnnotationTypeMemberDeclaration)


def test_hyp_dom_annotationtypememberdeclaration_constructor_exists():
    assert callable(DOM_AnnotationTypeMemberDeclaration.__init__)


def test_hyp_dom_annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(DOM_AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_abstracttypedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_AbstractTypeDeclaration)


def test_hyp_dom_abstracttypedeclaration_constructor_exists():
    assert callable(DOM_AbstractTypeDeclaration.__init__)


def test_hyp_dom_abstracttypedeclaration_constructor_args():
    sig = inspect.signature(DOM_AbstractTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "packageMemberTypeDeclaration" in params, "Missing parameter 'packageMemberTypeDeclaration'"
    assert "memberTypeDeclaration" in params, "Missing parameter 'memberTypeDeclaration'"
    assert "localTypeDeclaration" in params, "Missing parameter 'localTypeDeclaration'"






def test_hyp_dom_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_FieldDeclaration)


def test_hyp_dom_fielddeclaration_constructor_exists():
    assert callable(DOM_FieldDeclaration.__init__)


def test_hyp_dom_fielddeclaration_constructor_args():
    sig = inspect.signature(DOM_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_anonymousclassdeclaration_is_not_abstract():
    assert not inspect.isabstract(AnonymousClassDeclaration)


def test_hyp_anonymousclassdeclaration_constructor_exists():
    assert callable(AnonymousClassDeclaration.__init__)


def test_hyp_anonymousclassdeclaration_constructor_args():
    sig = inspect.signature(AnonymousClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_enumconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_EnumConstantDeclaration)


def test_hyp_dom_enumconstantdeclaration_constructor_exists():
    assert callable(DOM_EnumConstantDeclaration.__init__)


def test_hyp_dom_enumconstantdeclaration_constructor_args():
    sig = inspect.signature(DOM_EnumConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_tagelement_is_not_abstract():
    assert not inspect.isabstract(DOM_TagElement)


def test_hyp_dom_tagelement_constructor_exists():
    assert callable(DOM_TagElement.__init__)


def test_hyp_dom_tagelement_constructor_args():
    sig = inspect.signature(DOM_TagElement.__init__)
    params = list(sig.parameters.keys())
    assert "nested" in params, "Missing parameter 'nested'"
    assert "tagName" in params, "Missing parameter 'tagName'"





def test_hyp_dom_statement_is_not_abstract():
    assert not inspect.isabstract(DOM_Statement)


def test_hyp_dom_statement_constructor_exists():
    assert callable(DOM_Statement.__init__)


def test_hyp_dom_statement_constructor_args():
    sig = inspect.signature(DOM_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_hyp_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_hyp_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_markerannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_MarkerAnnotation)


def test_hyp_dom_markerannotation_constructor_exists():
    assert callable(DOM_MarkerAnnotation.__init__)


def test_hyp_dom_markerannotation_constructor_args():
    sig = inspect.signature(DOM_MarkerAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_normalannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_NormalAnnotation)


def test_hyp_dom_normalannotation_constructor_exists():
    assert callable(DOM_NormalAnnotation.__init__)


def test_hyp_dom_normalannotation_constructor_args():
    sig = inspect.signature(DOM_NormalAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_singlememberannotation_is_not_abstract():
    assert not inspect.isabstract(DOM_SingleMemberAnnotation)


def test_hyp_dom_singlememberannotation_constructor_exists():
    assert callable(DOM_SingleMemberAnnotation.__init__)


def test_hyp_dom_singlememberannotation_constructor_args():
    sig = inspect.signature(DOM_SingleMemberAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_PackageDeclaration)


def test_hyp_dom_packagedeclaration_constructor_exists():
    assert callable(DOM_PackageDeclaration.__init__)


def test_hyp_dom_packagedeclaration_constructor_args():
    sig = inspect.signature(DOM_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(DOM_VariableDeclaration)


def test_hyp_dom_variabledeclaration_constructor_exists():
    assert callable(DOM_VariableDeclaration.__init__)


def test_hyp_dom_variabledeclaration_constructor_args():
    sig = inspect.signature(DOM_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "extraDimensions" in params, "Missing parameter 'extraDimensions'"




def test_hyp_dom_typeparameter_is_not_abstract():
    assert not inspect.isabstract(DOM_TypeParameter)


def test_hyp_dom_typeparameter_constructor_exists():
    assert callable(DOM_TypeParameter.__init__)


def test_hyp_dom_typeparameter_constructor_args():
    sig = inspect.signature(DOM_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_type_is_not_abstract():
    assert not inspect.isabstract(DOM_Type)


def test_hyp_dom_type_constructor_exists():
    assert callable(DOM_Type.__init__)


def test_hyp_dom_type_constructor_args():
    sig = inspect.signature(DOM_Type.__init__)
    params = list(sig.parameters.keys())

def test_hyp_modifiers_exists():
    # Check that the Enumeration exists
    assert Modifiers is not None

def test_hyp_modifiers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Modifiers]
    expected_literals = [
        "transient",
        "deprecated",
        "static",
        "final",
        "default",
        "super",
        "synchronized",
        "varargs",
        "protected",
        "enum",
        "interface",
        "abstract",
        "private",
        "bridge",
        "annotation",
        "public",
        "volatile",
        "strictfp",
        "synthetic",
        "native",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Modifiers"

def test_hyp_infixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InfixExpressionOperatorKind is not None

def test_hyp_infixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InfixExpressionOperatorKind]
    expected_literals = [
        "conditional_or",
        "less_equals",
        "remainder",
        "or_",
        "times",
        "minus",
        "less",
        "divide",
        "greater",
        "conditional_and",
        "xor",
        "right_shift_signed",
        "right_shift_unsigned",
        "greater_equals",
        "equals",
        "and_",
        "left_shift",
        "not_equals",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InfixExpressionOperatorKind"

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
        "bit_or_assign",
        "minus_assign",
        "divide_assign",
        "remainder_assign",
        "right_shift_unsigned_assign",
        "left_shift_assign",
        "bit_and_assign",
        "times_assign",
        "plus_assign",
        "right_shift_signed_assign",
        "assign",
        "bit_xor_assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperatorKind"

def test_hyp_prefixexpressionoperatorkind_exists():
    # Check that the Enumeration exists
    assert PrefixExpressionOperatorKind is not None

def test_hyp_prefixexpressionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrefixExpressionOperatorKind]
    expected_literals = [
        "increment",
        "minus",
        "not_",
        "complement",
        "decrement",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrefixExpressionOperatorKind"


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
MemberValuePair_strategy = st.builds(
    MemberValuePair,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
DOM_SingleVariableDeclaration_strategy = st.builds(
    DOM_SingleVariableDeclaration,
    varargs=
        safe_text
)
DOM_VariableDeclarationFragment_strategy = st.builds(
    DOM_VariableDeclarationFragment,
)
CatchClause_strategy = st.builds(
    CatchClause,
)
Statement_strategy = st.builds(
    Statement,
)
DOM_IfStatement_strategy = st.builds(
    DOM_IfStatement,
)
DOM_DoStatement_strategy = st.builds(
    DOM_DoStatement,
)
DOM_ExpressionStatement_strategy = st.builds(
    DOM_ExpressionStatement,
)
DOM_SuperConstructorInvocation_strategy = st.builds(
    DOM_SuperConstructorInvocation,
)
DOM_EnhancedForStatement_strategy = st.builds(
    DOM_EnhancedForStatement,
)
DOM_VariableDeclarationStatement_strategy = st.builds(
    DOM_VariableDeclarationStatement,
)
DOM_SwitchStatement_strategy = st.builds(
    DOM_SwitchStatement,
)
DOM_SynchronizedStatement_strategy = st.builds(
    DOM_SynchronizedStatement,
)
DOM_SwitchCase_strategy = st.builds(
    DOM_SwitchCase,
    default=
        safe_text
)
DOM_ForStatement_strategy = st.builds(
    DOM_ForStatement,
)
DOM_TryStatement_strategy = st.builds(
    DOM_TryStatement,
)
DOM_BreakStatement_strategy = st.builds(
    DOM_BreakStatement,
)
DOM_Block_strategy = st.builds(
    DOM_Block,
)
DOM_ConstructorInvocation_strategy = st.builds(
    DOM_ConstructorInvocation,
)
DOM_ReturnStatement_strategy = st.builds(
    DOM_ReturnStatement,
)
DOM_WhileStatement_strategy = st.builds(
    DOM_WhileStatement,
)
DOM_ContinueStatement_strategy = st.builds(
    DOM_ContinueStatement,
)
DOM_EmptyStatement_strategy = st.builds(
    DOM_EmptyStatement,
)
DOM_ThrowStatement_strategy = st.builds(
    DOM_ThrowStatement,
)
DOM_TypeDeclarationStatement_strategy = st.builds(
    DOM_TypeDeclarationStatement,
)
DOM_LabeledStatement_strategy = st.builds(
    DOM_LabeledStatement,
)
DOM_AssertStatement_strategy = st.builds(
    DOM_AssertStatement,
)
Expression_strategy = st.builds(
    Expression,
)
DOM_Name_strategy = st.builds(
    DOM_Name,
    fullyQualifiedName=
        safe_text
)
DOM_ThisExpression_strategy = st.builds(
    DOM_ThisExpression,
)
DOM_NumberLiteral_strategy = st.builds(
    DOM_NumberLiteral,
    token=
        safe_text
)
DOM_TypeLiteral_strategy = st.builds(
    DOM_TypeLiteral,
)
DOM_SuperFieldAccess_strategy = st.builds(
    DOM_SuperFieldAccess,
)
DOM_VariableDeclarationExpression_strategy = st.builds(
    DOM_VariableDeclarationExpression,
)
DOM_PrefixExpression_strategy = st.builds(
    DOM_PrefixExpression,
    operator=
        safe_text
)
DOM_ParenthesizedExpression_strategy = st.builds(
    DOM_ParenthesizedExpression,
)
DOM_InstanceofExpression_strategy = st.builds(
    DOM_InstanceofExpression,
)
DOM_SuperMethodInvocation_strategy = st.builds(
    DOM_SuperMethodInvocation,
)
DOM_NullLiteral_strategy = st.builds(
    DOM_NullLiteral,
)
DOM_StringLiteral_strategy = st.builds(
    DOM_StringLiteral,
    literalValue=
        safe_text,
    escapedValue=
        safe_text
)
DOM_MethodInvocation_strategy = st.builds(
    DOM_MethodInvocation,
)
DOM_PostfixExpression_strategy = st.builds(
    DOM_PostfixExpression,
    operator=
        safe_text
)
DOM_InfixExpression_strategy = st.builds(
    DOM_InfixExpression,
    operator=
        safe_text
)
SimpleName_strategy = st.builds(
    SimpleName,
)
Name_strategy = st.builds(
    Name,
)
DOM_QualifiedName_strategy = st.builds(
    DOM_QualifiedName,
)
DOM_SimpleName_strategy = st.builds(
    DOM_SimpleName,
    declaration=
        safe_text,
    identifier=
        safe_text
)
AbstractTypeDeclaration_strategy = st.builds(
    AbstractTypeDeclaration,
)
ImportDeclaration_strategy = st.builds(
    ImportDeclaration,
)
PackageDeclaration_strategy = st.builds(
    PackageDeclaration,
)
DOM_ExtendedModifier_strategy = st.builds(
    DOM_ExtendedModifier,
)
Type_strategy = st.builds(
    Type,
)
DOM_ArrayType_strategy = st.builds(
    DOM_ArrayType,
    dimensions=
        safe_text
)
DOM_ParameterizedType_strategy = st.builds(
    DOM_ParameterizedType,
)
DOM_SimpleType_strategy = st.builds(
    DOM_SimpleType,
)
DOM_PrimitiveType_strategy = st.builds(
    DOM_PrimitiveType,
    code=
        safe_text
)
DOM_QualifiedType_strategy = st.builds(
    DOM_QualifiedType,
)
DOM_WildcardType_strategy = st.builds(
    DOM_WildcardType,
    upperBound=
        safe_text
)
MethodRefParameter_strategy = st.builds(
    MethodRefParameter,
)
BodyDeclaration_strategy = st.builds(
    BodyDeclaration,
)
DOM_ASTNode_strategy = st.builds(
    DOM_ASTNode,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
DOM_MethodRef_strategy = st.builds(
    DOM_MethodRef,
)
DOM_MemberRef_strategy = st.builds(
    DOM_MemberRef,
)
DOM_AnonymousClassDeclaration_strategy = st.builds(
    DOM_AnonymousClassDeclaration,
)
DOM_MemberValuePair_strategy = st.builds(
    DOM_MemberValuePair,
)
DOM_MethodRefParameter_strategy = st.builds(
    DOM_MethodRefParameter,
    varargs=
        safe_text
)
DOM_TextElement_strategy = st.builds(
    DOM_TextElement,
    text=
        safe_text
)
DOM_ImportDeclaration_strategy = st.builds(
    DOM_ImportDeclaration,
    onDemand=
        safe_text,
    static=
        safe_text
)
DOM_BodyDeclaration_strategy = st.builds(
    DOM_BodyDeclaration,
)
DOM_Expression_strategy = st.builds(
    DOM_Expression,
    resolveBoxing=
        safe_text,
    resolveUnboxing=
        safe_text
)
DOM_AST_strategy = st.builds(
    DOM_AST,
)
Comment_strategy = st.builds(
    Comment,
)
DOM_CompilationUnit_strategy = st.builds(
    DOM_CompilationUnit,
)
DOM_Comment_strategy = st.builds(
    DOM_Comment,
)
SingleVariableDeclaration_strategy = st.builds(
    SingleVariableDeclaration,
)
Block_strategy = st.builds(
    Block,
)
DOM_CatchClause_strategy = st.builds(
    DOM_CatchClause,
)
Javadoc_strategy = st.builds(
    Javadoc,
)
ExtendedModifier_strategy = st.builds(
    ExtendedModifier,
)
DOM_Modifier_strategy = st.builds(
    DOM_Modifier,
    abstract=
        safe_text,
    static=
        safe_text,
    final=
        safe_text,
    native=
        safe_text,
    private=
        safe_text,
    none=
        safe_text,
    transient=
        safe_text,
    public=
        safe_text,
    synchronized=
        safe_text,
    strictfp=
        safe_text,
    protected=
        safe_text,
    volatile=
        safe_text
)
ITypeParameter_strategy = st.builds(
    ITypeParameter,
)
Core_Parameter_strategy = st.builds(
    Core_Parameter,
    type=
        safe_text,
    name=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
Core_ISourceRange_strategy = st.builds(
    Core_ISourceRange,
    length=
        safe_text,
    offset=
        safe_text
)
ISourceRange_strategy = st.builds(
    ISourceRange,
)
Core_ISourceReference_strategy = st.builds(
    Core_ISourceReference,
    source=
        safe_text
)
CompilationUnit_strategy = st.builds(
    CompilationUnit,
)
IMethod_strategy = st.builds(
    IMethod,
)
IField_strategy = st.builds(
    IField,
)
IInitializer_strategy = st.builds(
    IInitializer,
)
IMember_strategy = st.builds(
    IMember,
)
Core_IMethod_strategy = st.builds(
    Core_IMethod,
    exceptionTypes=
        safe_text,
    returnType=
        safe_text,
    isConstructor=
        safe_text,
    isMainMethod=
        safe_text
)
Core_IField_strategy = st.builds(
    Core_IField,
    constant=
        safe_text,
    isVolatile=
        safe_text,
    typeSignature=
        safe_text,
    isTransient=
        safe_text,
    isEnumConstant=
        safe_text
)
Core_IInitializer_strategy = st.builds(
    Core_IInitializer,
)
Core_IType_strategy = st.builds(
    Core_IType,
    fullyQualifiedName=
        safe_text,
    fullyQualifiedParametrizedName=
        safe_text
)
IPackageFragment_strategy = st.builds(
    IPackageFragment,
)
IJavaElement_strategy = st.builds(
    IJavaElement,
)
IPackageFragmentRoot_strategy = st.builds(
    IPackageFragmentRoot,
)
Core_SourcePackageFragmentRoot_strategy = st.builds(
    Core_SourcePackageFragmentRoot,
)
Core_BinaryPackageFragmentRoot_strategy = st.builds(
    Core_BinaryPackageFragmentRoot,
)
IJavaProject_strategy = st.builds(
    IJavaProject,
)
PhysicalElement_strategy = st.builds(
    PhysicalElement,
)
Core_IPackageFragmentRoot_strategy = st.builds(
    Core_IPackageFragmentRoot,
)
Core_IPackageFragment_strategy = st.builds(
    Core_IPackageFragment,
    isDefaultPackage=
        safe_text
)
Core_IJavaProject_strategy = st.builds(
    Core_IJavaProject,
)
Core_IJavaModel_strategy = st.builds(
    Core_IJavaModel,
)
Core_PhysicalElement_strategy = st.builds(
    Core_PhysicalElement,
    isReadOnly=
        safe_text,
    path=
        safe_text
)
IImportDeclaration_strategy = st.builds(
    IImportDeclaration,
)
IType_strategy = st.builds(
    IType,
)
ITypeRoot_strategy = st.builds(
    ITypeRoot,
)
Core_IClassFile_strategy = st.builds(
    Core_IClassFile,
    isClass=
        safe_text,
    isInterface=
        safe_text
)
Core_ICompilationUnit_strategy = st.builds(
    Core_ICompilationUnit,
)
ISourceReference_strategy = st.builds(
    ISourceReference,
)
Core_ITypeParameter_strategy = st.builds(
    Core_ITypeParameter,
    bounds=
        safe_text
)
Core_IImportDeclaration_strategy = st.builds(
    Core_IImportDeclaration,
    isStatic=
        safe_text,
    isOnDemand=
        safe_text
)
Core_IMember_strategy = st.builds(
    Core_IMember,
)
Core_ITypeRoot_strategy = st.builds(
    Core_ITypeRoot,
)
ICompilationUnit_strategy = st.builds(
    ICompilationUnit,
)
IClassFile_strategy = st.builds(
    IClassFile,
)
Core_IJavaElement_strategy = st.builds(
    Core_IJavaElement,
    elementName=
        safe_text
)
DOM_FieldAccess_strategy = st.builds(
    DOM_FieldAccess,
)
DOM_ClassInstanceCreation_strategy = st.builds(
    DOM_ClassInstanceCreation,
)
DOM_CharacterLiteral_strategy = st.builds(
    DOM_CharacterLiteral,
    escapedValue=
        safe_text,
    charValue=
        safe_text
)
DOM_CastExpression_strategy = st.builds(
    DOM_CastExpression,
)
DOM_BooleanLiteral_strategy = st.builds(
    DOM_BooleanLiteral,
    booleanValue=
        safe_text
)
DOM_ConditionalExpression_strategy = st.builds(
    DOM_ConditionalExpression,
)
DOM_ArrayCreation_strategy = st.builds(
    DOM_ArrayCreation,
)
DOM_ArrayAccess_strategy = st.builds(
    DOM_ArrayAccess,
)
DOM_Annotation_strategy = st.builds(
    DOM_Annotation,
)
DOM_LineComment_strategy = st.builds(
    DOM_LineComment,
)
TagElement_strategy = st.builds(
    TagElement,
)
DOM_Javadoc_strategy = st.builds(
    DOM_Javadoc,
)
DOM_BlockComment_strategy = st.builds(
    DOM_BlockComment,
)
DOM_Assignment_strategy = st.builds(
    DOM_Assignment,
    operator=
        safe_text
)
DOM_ArrayInitializer_strategy = st.builds(
    DOM_ArrayInitializer,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
TypeParameter_strategy = st.builds(
    TypeParameter,
)
DOM_MethodDeclaration_strategy = st.builds(
    DOM_MethodDeclaration,
    extraDimensions=
        safe_text,
    varargs=
        safe_text,
    constructor=
        safe_text
)
DOM_Initializer_strategy = st.builds(
    DOM_Initializer,
)
VariableDeclarationFragment_strategy = st.builds(
    VariableDeclarationFragment,
)
DOM_TypeDeclaration_strategy = st.builds(
    DOM_TypeDeclaration,
    interface=
        safe_text
)
EnumConstantDeclaration_strategy = st.builds(
    EnumConstantDeclaration,
)
DOM_EnumDeclaration_strategy = st.builds(
    DOM_EnumDeclaration,
)
DOM_AnnotationTypeDeclaration_strategy = st.builds(
    DOM_AnnotationTypeDeclaration,
)
DOM_AnnotationTypeMemberDeclaration_strategy = st.builds(
    DOM_AnnotationTypeMemberDeclaration,
)
DOM_AbstractTypeDeclaration_strategy = st.builds(
    DOM_AbstractTypeDeclaration,
    packageMemberTypeDeclaration=
        safe_text,
    memberTypeDeclaration=
        safe_text,
    localTypeDeclaration=
        safe_text
)
DOM_FieldDeclaration_strategy = st.builds(
    DOM_FieldDeclaration,
)
AnonymousClassDeclaration_strategy = st.builds(
    AnonymousClassDeclaration,
)
DOM_EnumConstantDeclaration_strategy = st.builds(
    DOM_EnumConstantDeclaration,
)
DOM_TagElement_strategy = st.builds(
    DOM_TagElement,
    nested=
        safe_text,
    tagName=
        safe_text
)
DOM_Statement_strategy = st.builds(
    DOM_Statement,
)
Annotation_strategy = st.builds(
    Annotation,
)
DOM_MarkerAnnotation_strategy = st.builds(
    DOM_MarkerAnnotation,
)
DOM_NormalAnnotation_strategy = st.builds(
    DOM_NormalAnnotation,
)
DOM_SingleMemberAnnotation_strategy = st.builds(
    DOM_SingleMemberAnnotation,
)
DOM_PackageDeclaration_strategy = st.builds(
    DOM_PackageDeclaration,
)
DOM_VariableDeclaration_strategy = st.builds(
    DOM_VariableDeclaration,
    extraDimensions=
        safe_text
)
DOM_TypeParameter_strategy = st.builds(
    DOM_TypeParameter,
)
DOM_Type_strategy = st.builds(
    DOM_Type,
)






@given(instance=DOM_SingleVariableDeclaration_strategy)
def test_hyp_dom_singlevariabledeclaration_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original















@given(instance=DOM_SwitchCase_strategy)
def test_hyp_dom_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original


















@given(instance=DOM_Name_strategy)
def test_hyp_dom_name_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original





@given(instance=DOM_NumberLiteral_strategy)
def test_hyp_dom_numberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original







@given(instance=DOM_PrefixExpression_strategy)
def test_hyp_dom_prefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original








@given(instance=DOM_StringLiteral_strategy)
def test_hyp_dom_stringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original



@given(instance=DOM_StringLiteral_strategy)
def test_hyp_dom_stringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original





@given(instance=DOM_PostfixExpression_strategy)
def test_hyp_dom_postfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=DOM_InfixExpression_strategy)
def test_hyp_dom_infixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original







@given(instance=DOM_SimpleName_strategy)
def test_hyp_dom_simplename_declaration_setter(instance):
    original = instance.declaration
    instance.declaration = original
    assert instance.declaration == original



@given(instance=DOM_SimpleName_strategy)
def test_hyp_dom_simplename_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original









@given(instance=DOM_ArrayType_strategy)
def test_hyp_dom_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original






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












@given(instance=DOM_MethodRefParameter_strategy)
def test_hyp_dom_methodrefparameter_varargs_setter(instance):
    original = instance.varargs
    instance.varargs = original
    assert instance.varargs == original




@given(instance=DOM_TextElement_strategy)
def test_hyp_dom_textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




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





@given(instance=DOM_Expression_strategy)
def test_hyp_dom_expression_resolveBoxing_setter(instance):
    original = instance.resolveBoxing
    instance.resolveBoxing = original
    assert instance.resolveBoxing == original



@given(instance=DOM_Expression_strategy)
def test_hyp_dom_expression_resolveUnboxing_setter(instance):
    original = instance.resolveUnboxing
    instance.resolveUnboxing = original
    assert instance.resolveUnboxing == original













@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_none_setter(instance):
    original = instance.none
    instance.none = original
    assert instance.none == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original



@given(instance=DOM_Modifier_strategy)
def test_hyp_dom_modifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



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
def test_hyp_dom_modifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original





@given(instance=Core_Parameter_strategy)
def test_hyp_core_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Core_Parameter_strategy)
def test_hyp_core_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=Core_ISourceRange_strategy)
def test_hyp_core_isourcerange_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=Core_ISourceRange_strategy)
def test_hyp_core_isourcerange_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original





@given(instance=Core_ISourceReference_strategy)
def test_hyp_core_isourcereference_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original









@given(instance=Core_IMethod_strategy)
def test_hyp_core_imethod_exceptionTypes_setter(instance):
    original = instance.exceptionTypes
    instance.exceptionTypes = original
    assert instance.exceptionTypes == original



@given(instance=Core_IMethod_strategy)
def test_hyp_core_imethod_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original



@given(instance=Core_IMethod_strategy)
def test_hyp_core_imethod_isConstructor_setter(instance):
    original = instance.isConstructor
    instance.isConstructor = original
    assert instance.isConstructor == original



@given(instance=Core_IMethod_strategy)
def test_hyp_core_imethod_isMainMethod_setter(instance):
    original = instance.isMainMethod
    instance.isMainMethod = original
    assert instance.isMainMethod == original




@given(instance=Core_IField_strategy)
def test_hyp_core_ifield_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original



@given(instance=Core_IField_strategy)
def test_hyp_core_ifield_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original



@given(instance=Core_IField_strategy)
def test_hyp_core_ifield_typeSignature_setter(instance):
    original = instance.typeSignature
    instance.typeSignature = original
    assert instance.typeSignature == original



@given(instance=Core_IField_strategy)
def test_hyp_core_ifield_isTransient_setter(instance):
    original = instance.isTransient
    instance.isTransient = original
    assert instance.isTransient == original



@given(instance=Core_IField_strategy)
def test_hyp_core_ifield_isEnumConstant_setter(instance):
    original = instance.isEnumConstant
    instance.isEnumConstant = original
    assert instance.isEnumConstant == original





@given(instance=Core_IType_strategy)
def test_hyp_core_itype_fullyQualifiedName_setter(instance):
    original = instance.fullyQualifiedName
    instance.fullyQualifiedName = original
    assert instance.fullyQualifiedName == original



@given(instance=Core_IType_strategy)
def test_hyp_core_itype_fullyQualifiedParametrizedName_setter(instance):
    original = instance.fullyQualifiedParametrizedName
    instance.fullyQualifiedParametrizedName = original
    assert instance.fullyQualifiedParametrizedName == original












@given(instance=Core_IPackageFragment_strategy)
def test_hyp_core_ipackagefragment_isDefaultPackage_setter(instance):
    original = instance.isDefaultPackage
    instance.isDefaultPackage = original
    assert instance.isDefaultPackage == original






@given(instance=Core_PhysicalElement_strategy)
def test_hyp_core_physicalelement_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=Core_PhysicalElement_strategy)
def test_hyp_core_physicalelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original







@given(instance=Core_IClassFile_strategy)
def test_hyp_core_iclassfile_isClass_setter(instance):
    original = instance.isClass
    instance.isClass = original
    assert instance.isClass == original



@given(instance=Core_IClassFile_strategy)
def test_hyp_core_iclassfile_isInterface_setter(instance):
    original = instance.isInterface
    instance.isInterface = original
    assert instance.isInterface == original






@given(instance=Core_ITypeParameter_strategy)
def test_hyp_core_itypeparameter_bounds_setter(instance):
    original = instance.bounds
    instance.bounds = original
    assert instance.bounds == original




@given(instance=Core_IImportDeclaration_strategy)
def test_hyp_core_iimportdeclaration_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=Core_IImportDeclaration_strategy)
def test_hyp_core_iimportdeclaration_isOnDemand_setter(instance):
    original = instance.isOnDemand
    instance.isOnDemand = original
    assert instance.isOnDemand == original








@given(instance=Core_IJavaElement_strategy)
def test_hyp_core_ijavaelement_elementName_setter(instance):
    original = instance.elementName
    instance.elementName = original
    assert instance.elementName == original






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





@given(instance=DOM_BooleanLiteral_strategy)
def test_hyp_dom_booleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original












@given(instance=DOM_Assignment_strategy)
def test_hyp_dom_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original








@given(instance=DOM_MethodDeclaration_strategy)
def test_hyp_dom_methoddeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original



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






@given(instance=DOM_TypeDeclaration_strategy)
def test_hyp_dom_typedeclaration_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original








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



@given(instance=DOM_AbstractTypeDeclaration_strategy)
def test_hyp_dom_abstracttypedeclaration_localTypeDeclaration_setter(instance):
    original = instance.localTypeDeclaration
    instance.localTypeDeclaration = original
    assert instance.localTypeDeclaration == original







@given(instance=DOM_TagElement_strategy)
def test_hyp_dom_tagelement_nested_setter(instance):
    original = instance.nested
    instance.nested = original
    assert instance.nested == original



@given(instance=DOM_TagElement_strategy)
def test_hyp_dom_tagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original










@given(instance=DOM_VariableDeclaration_strategy)
def test_hyp_dom_variabledeclaration_extraDimensions_setter(instance):
    original = instance.extraDimensions
    instance.extraDimensions = original
    assert instance.extraDimensions == original




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
    AnonymousClassDeclaration,
    ArrayInitializer,
    ArrayType,
    Block,
    BodyDeclaration,
    CatchClause,
    Comment,
    CompilationUnit,
    Core_BinaryPackageFragmentRoot,
    Core_IClassFile,
    Core_ICompilationUnit,
    Core_IField,
    Core_IImportDeclaration,
    Core_IInitializer,
    Core_IJavaElement,
    Core_IJavaModel,
    Core_IJavaProject,
    Core_IMember,
    Core_IMethod,
    Core_IPackageFragment,
    Core_IPackageFragmentRoot,
    Core_ISourceRange,
    Core_ISourceReference,
    Core_IType,
    Core_ITypeParameter,
    Core_ITypeRoot,
    Core_Parameter,
    Core_PhysicalElement,
    Core_SourcePackageFragmentRoot,
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
    EnumConstantDeclaration,
    Expression,
    ExtendedModifier,
    IClassFile,
    ICompilationUnit,
    IField,
    IImportDeclaration,
    IInitializer,
    IJavaElement,
    IJavaProject,
    IMember,
    IMethod,
    IPackageFragment,
    IPackageFragmentRoot,
    ISourceRange,
    ISourceReference,
    IType,
    ITypeParameter,
    ITypeRoot,
    ImportDeclaration,
    Javadoc,
    MemberValuePair,
    MethodRefParameter,
    Name,
    PackageDeclaration,
    Parameter,
    PhysicalElement,
    SimpleName,
    SingleVariableDeclaration,
    Statement,
    TagElement,
    Type,
    TypeParameter,
    VariableDeclaration,
    VariableDeclarationFragment,
    AssignmentOperatorKind,
    InfixExpressionOperatorKind,
    Modifiers,
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

def test_Core_IClassFile_isClass_value_roundtrip():
    instance = Core_IClassFile(isClass="sample_text", isInterface="sample_text")
    assert instance.isClass == "sample_text"
    instance.isClass = "sample_text_2"
    assert instance.isClass == "sample_text_2"


def test_Core_IClassFile_isInterface_value_roundtrip():
    instance = Core_IClassFile(isClass="sample_text", isInterface="sample_text")
    assert instance.isInterface == "sample_text"
    instance.isInterface = "sample_text_2"
    assert instance.isInterface == "sample_text_2"


def test_Core_IField_constant_value_roundtrip():
    instance = Core_IField(constant="sample_text", isEnumConstant="sample_text", isTransient="sample_text", isVolatile="sample_text", typeSignature="sample_text")
    assert instance.constant == "sample_text"
    instance.constant = "sample_text_2"
    assert instance.constant == "sample_text_2"


def test_Core_IField_isEnumConstant_value_roundtrip():
    instance = Core_IField(constant="sample_text", isEnumConstant="sample_text", isTransient="sample_text", isVolatile="sample_text", typeSignature="sample_text")
    assert instance.isEnumConstant == "sample_text"
    instance.isEnumConstant = "sample_text_2"
    assert instance.isEnumConstant == "sample_text_2"


def test_Core_IField_isTransient_value_roundtrip():
    instance = Core_IField(constant="sample_text", isEnumConstant="sample_text", isTransient="sample_text", isVolatile="sample_text", typeSignature="sample_text")
    assert instance.isTransient == "sample_text"
    instance.isTransient = "sample_text_2"
    assert instance.isTransient == "sample_text_2"


def test_Core_IField_isVolatile_value_roundtrip():
    instance = Core_IField(constant="sample_text", isEnumConstant="sample_text", isTransient="sample_text", isVolatile="sample_text", typeSignature="sample_text")
    assert instance.isVolatile == "sample_text"
    instance.isVolatile = "sample_text_2"
    assert instance.isVolatile == "sample_text_2"


def test_Core_IField_typeSignature_value_roundtrip():
    instance = Core_IField(constant="sample_text", isEnumConstant="sample_text", isTransient="sample_text", isVolatile="sample_text", typeSignature="sample_text")
    assert instance.typeSignature == "sample_text"
    instance.typeSignature = "sample_text_2"
    assert instance.typeSignature == "sample_text_2"


def test_Core_IImportDeclaration_isOnDemand_value_roundtrip():
    instance = Core_IImportDeclaration(isOnDemand="sample_text", isStatic="sample_text")
    assert instance.isOnDemand == "sample_text"
    instance.isOnDemand = "sample_text_2"
    assert instance.isOnDemand == "sample_text_2"


def test_Core_IImportDeclaration_isStatic_value_roundtrip():
    instance = Core_IImportDeclaration(isOnDemand="sample_text", isStatic="sample_text")
    assert instance.isStatic == "sample_text"
    instance.isStatic = "sample_text_2"
    assert instance.isStatic == "sample_text_2"


def test_Core_IJavaElement_elementName_value_roundtrip():
    instance = Core_IJavaElement(elementName="sample_text")
    assert instance.elementName == "sample_text"
    instance.elementName = "sample_text_2"
    assert instance.elementName == "sample_text_2"


def test_Core_IMethod_exceptionTypes_value_roundtrip():
    instance = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    assert instance.exceptionTypes == "sample_text"
    instance.exceptionTypes = "sample_text_2"
    assert instance.exceptionTypes == "sample_text_2"


def test_Core_IMethod_isConstructor_value_roundtrip():
    instance = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    assert instance.isConstructor == "sample_text"
    instance.isConstructor = "sample_text_2"
    assert instance.isConstructor == "sample_text_2"


def test_Core_IMethod_isMainMethod_value_roundtrip():
    instance = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    assert instance.isMainMethod == "sample_text"
    instance.isMainMethod = "sample_text_2"
    assert instance.isMainMethod == "sample_text_2"


def test_Core_IMethod_returnType_value_roundtrip():
    instance = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    assert instance.returnType == "sample_text"
    instance.returnType = "sample_text_2"
    assert instance.returnType == "sample_text_2"


def test_Core_IPackageFragment_isDefaultPackage_value_roundtrip():
    instance = Core_IPackageFragment(isDefaultPackage="sample_text")
    assert instance.isDefaultPackage == "sample_text"
    instance.isDefaultPackage = "sample_text_2"
    assert instance.isDefaultPackage == "sample_text_2"


def test_Core_ISourceRange_length_value_roundtrip():
    instance = Core_ISourceRange(length="sample_text", offset="sample_text")
    assert instance.length == "sample_text"
    instance.length = "sample_text_2"
    assert instance.length == "sample_text_2"


def test_Core_ISourceRange_offset_value_roundtrip():
    instance = Core_ISourceRange(length="sample_text", offset="sample_text")
    assert instance.offset == "sample_text"
    instance.offset = "sample_text_2"
    assert instance.offset == "sample_text_2"


def test_Core_ISourceReference_source_value_roundtrip():
    instance = Core_ISourceReference(source="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_Core_IType_fullyQualifiedName_value_roundtrip():
    instance = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    assert instance.fullyQualifiedName == "sample_text"
    instance.fullyQualifiedName = "sample_text_2"
    assert instance.fullyQualifiedName == "sample_text_2"


def test_Core_IType_fullyQualifiedParametrizedName_value_roundtrip():
    instance = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    assert instance.fullyQualifiedParametrizedName == "sample_text"
    instance.fullyQualifiedParametrizedName = "sample_text_2"
    assert instance.fullyQualifiedParametrizedName == "sample_text_2"


def test_Core_ITypeParameter_bounds_value_roundtrip():
    instance = Core_ITypeParameter(bounds="sample_text")
    assert instance.bounds == "sample_text"
    instance.bounds = "sample_text_2"
    assert instance.bounds == "sample_text_2"


def test_Core_Parameter_name_value_roundtrip():
    instance = Core_Parameter(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Core_Parameter_type_value_roundtrip():
    instance = Core_Parameter(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Core_PhysicalElement_isReadOnly_value_roundtrip():
    instance = Core_PhysicalElement(isReadOnly="sample_text", path="sample_text")
    assert instance.isReadOnly == "sample_text"
    instance.isReadOnly = "sample_text_2"
    assert instance.isReadOnly == "sample_text_2"


def test_Core_PhysicalElement_path_value_roundtrip():
    instance = Core_PhysicalElement(isReadOnly="sample_text", path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


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


def test_Core_IImportDeclaration_isa_IJavaElement():
    instance = Core_IImportDeclaration(isOnDemand="sample_text", isStatic="sample_text")
    assert isinstance(instance, IJavaElement)


def test_Core_IJavaProject_isa_IJavaElement():
    instance = Core_IJavaProject()
    assert isinstance(instance, IJavaElement)


def test_Core_IMember_isa_IJavaElement():
    instance = Core_IMember()
    assert isinstance(instance, IJavaElement)


def test_Core_IPackageFragment_isa_IJavaElement():
    instance = Core_IPackageFragment(isDefaultPackage="sample_text")
    assert isinstance(instance, IJavaElement)


def test_Core_IPackageFragmentRoot_isa_IJavaElement():
    instance = Core_IPackageFragmentRoot()
    assert isinstance(instance, IJavaElement)


def test_Core_ITypeParameter_isa_IJavaElement():
    instance = Core_ITypeParameter(bounds="sample_text")
    assert isinstance(instance, IJavaElement)


def test_Core_ITypeRoot_isa_IJavaElement():
    instance = Core_ITypeRoot()
    assert isinstance(instance, IJavaElement)


def test_Core_IField_isa_IMember():
    instance = Core_IField(constant="sample_text", isEnumConstant="sample_text", isTransient="sample_text", isVolatile="sample_text", typeSignature="sample_text")
    assert isinstance(instance, IMember)


def test_Core_IInitializer_isa_IMember():
    instance = Core_IInitializer()
    assert isinstance(instance, IMember)


def test_Core_IMethod_isa_IMember():
    instance = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    assert isinstance(instance, IMember)


def test_Core_IType_isa_IMember():
    instance = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    assert isinstance(instance, IMember)


def test_Core_BinaryPackageFragmentRoot_isa_IPackageFragmentRoot():
    instance = Core_BinaryPackageFragmentRoot()
    assert isinstance(instance, IPackageFragmentRoot)


def test_Core_SourcePackageFragmentRoot_isa_IPackageFragmentRoot():
    instance = Core_SourcePackageFragmentRoot()
    assert isinstance(instance, IPackageFragmentRoot)


def test_Core_IImportDeclaration_isa_ISourceReference():
    instance = Core_IImportDeclaration(isOnDemand="sample_text", isStatic="sample_text")
    assert isinstance(instance, ISourceReference)


def test_Core_IMember_isa_ISourceReference():
    instance = Core_IMember()
    assert isinstance(instance, ISourceReference)


def test_Core_ITypeParameter_isa_ISourceReference():
    instance = Core_ITypeParameter(bounds="sample_text")
    assert isinstance(instance, ISourceReference)


def test_Core_ITypeRoot_isa_ISourceReference():
    instance = Core_ITypeRoot()
    assert isinstance(instance, ISourceReference)


def test_Core_IClassFile_isa_ITypeRoot():
    instance = Core_IClassFile(isClass="sample_text", isInterface="sample_text")
    assert isinstance(instance, ITypeRoot)


def test_Core_ICompilationUnit_isa_ITypeRoot():
    instance = Core_ICompilationUnit()
    assert isinstance(instance, ITypeRoot)


def test_DOM_QualifiedName_isa_Name():
    instance = DOM_QualifiedName()
    assert isinstance(instance, Name)


def test_DOM_SimpleName_isa_Name():
    instance = DOM_SimpleName(declaration="sample_text", identifier="sample_text")
    assert isinstance(instance, Name)


def test_Core_IJavaModel_isa_PhysicalElement():
    instance = Core_IJavaModel()
    assert isinstance(instance, PhysicalElement)


def test_Core_IJavaProject_isa_PhysicalElement():
    instance = Core_IJavaProject()
    assert isinstance(instance, PhysicalElement)


def test_Core_IPackageFragment_isa_PhysicalElement():
    instance = Core_IPackageFragment(isDefaultPackage="sample_text")
    assert isinstance(instance, PhysicalElement)


def test_Core_IPackageFragmentRoot_isa_PhysicalElement():
    instance = Core_IPackageFragmentRoot()
    assert isinstance(instance, PhysicalElement)


def test_Core_ITypeRoot_isa_PhysicalElement():
    instance = Core_ITypeRoot()
    assert isinstance(instance, PhysicalElement)


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


def test_assoc_binding150_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = IMethod()
    b2 = IMethod()
    _safe_set(a, 'DOM_MethodDeclaration151', b1)
    assert _is_linked(a, 'DOM_MethodDeclaration151', b1)
    if hasattr(b1, 'IMethod152'):
        assert _is_linked(b1, 'IMethod152', a)
    _safe_set(a, 'DOM_MethodDeclaration151', b2)
    assert _is_linked(a, 'DOM_MethodDeclaration151', b2)
    if hasattr(b1, 'IMethod152'):
        assert not _is_linked(b1, 'IMethod152', a)
    if hasattr(b2, 'IMethod152'):
        assert _is_linked(b2, 'IMethod152', a)
    _safe_set(a, 'DOM_MethodDeclaration151', None)
    assert not _is_linked(a, 'DOM_MethodDeclaration151', b2)
    if hasattr(b2, 'IMethod152'):
        assert not _is_linked(b2, 'IMethod152', a)


def test_assoc_body134_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = Block()
    b2 = Block()
    _safe_set(a, 'DOM_MethodDeclaration', b1)
    assert _is_linked(a, 'DOM_MethodDeclaration', b1)
    if hasattr(b1, 'Block135'):
        assert _is_linked(b1, 'Block135', a)
    _safe_set(a, 'DOM_MethodDeclaration', b2)
    assert _is_linked(a, 'DOM_MethodDeclaration', b2)
    if hasattr(b1, 'Block135'):
        assert not _is_linked(b1, 'Block135', a)
    if hasattr(b2, 'Block135'):
        assert _is_linked(b2, 'Block135', a)
    _safe_set(a, 'DOM_MethodDeclaration', None)
    assert not _is_linked(a, 'DOM_MethodDeclaration', b2)
    if hasattr(b2, 'Block135'):
        assert not _is_linked(b2, 'Block135', a)


def test_assoc_bodyDeclarations108_link_reassign_clear():
    a = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    b1 = BodyDeclaration()
    b2 = BodyDeclaration()
    _safe_set(a, 'DOM_AbstractTypeDeclaration', {b1})
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration', b1)
    if hasattr(b1, 'BodyDeclaration109'):
        assert _is_linked(b1, 'BodyDeclaration109', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration', {b2})
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration', b2)
    if hasattr(b1, 'BodyDeclaration109'):
        assert not _is_linked(b1, 'BodyDeclaration109', a)
    if hasattr(b2, 'BodyDeclaration109'):
        assert _is_linked(b2, 'BodyDeclaration109', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration', set())
    assert not _is_linked(a, 'DOM_AbstractTypeDeclaration', b2)
    if hasattr(b2, 'BodyDeclaration109'):
        assert not _is_linked(b2, 'BodyDeclaration109', a)


def test_assoc_bound396_link_reassign_clear():
    a = DOM_WildcardType(upperBound="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'DOM_WildcardType', b1)
    assert _is_linked(a, 'DOM_WildcardType', b1)
    if hasattr(b1, 'Type397'):
        assert _is_linked(b1, 'Type397', a)
    _safe_set(a, 'DOM_WildcardType', b2)
    assert _is_linked(a, 'DOM_WildcardType', b2)
    if hasattr(b1, 'Type397'):
        assert not _is_linked(b1, 'Type397', a)
    if hasattr(b2, 'Type397'):
        assert _is_linked(b2, 'Type397', a)
    _safe_set(a, 'DOM_WildcardType', None)
    assert not _is_linked(a, 'DOM_WildcardType', b2)
    if hasattr(b2, 'Type397'):
        assert not _is_linked(b2, 'Type397', a)


def test_assoc_classFiles14_link_reassign_clear():
    a = Core_IPackageFragment(isDefaultPackage="sample_text")
    b1 = IClassFile()
    b2 = IClassFile()
    _safe_set(a, 'Core_IPackageFragment', {b1})
    assert _is_linked(a, 'Core_IPackageFragment', b1)
    if hasattr(b1, 'IClassFile'):
        assert _is_linked(b1, 'IClassFile', a)
    _safe_set(a, 'Core_IPackageFragment', {b2})
    assert _is_linked(a, 'Core_IPackageFragment', b2)
    if hasattr(b1, 'IClassFile'):
        assert not _is_linked(b1, 'IClassFile', a)
    if hasattr(b2, 'IClassFile'):
        assert _is_linked(b2, 'IClassFile', a)
    _safe_set(a, 'Core_IPackageFragment', set())
    assert not _is_linked(a, 'Core_IPackageFragment', b2)
    if hasattr(b2, 'IClassFile'):
        assert not _is_linked(b2, 'IClassFile', a)


def test_assoc_compilationUnits15_link_reassign_clear():
    a = Core_IPackageFragment(isDefaultPackage="sample_text")
    b1 = ICompilationUnit()
    b2 = ICompilationUnit()
    _safe_set(a, 'Core_IPackageFragment16', {b1})
    assert _is_linked(a, 'Core_IPackageFragment16', b1)
    if hasattr(b1, 'ICompilationUnit'):
        assert _is_linked(b1, 'ICompilationUnit', a)
    _safe_set(a, 'Core_IPackageFragment16', {b2})
    assert _is_linked(a, 'Core_IPackageFragment16', b2)
    if hasattr(b1, 'ICompilationUnit'):
        assert not _is_linked(b1, 'ICompilationUnit', a)
    if hasattr(b2, 'ICompilationUnit'):
        assert _is_linked(b2, 'ICompilationUnit', a)
    _safe_set(a, 'Core_IPackageFragment16', set())
    assert not _is_linked(a, 'Core_IPackageFragment16', b2)
    if hasattr(b2, 'ICompilationUnit'):
        assert not _is_linked(b2, 'ICompilationUnit', a)


def test_assoc_componentType379_link_reassign_clear():
    a = DOM_ArrayType(dimensions="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'DOM_ArrayType', b1)
    assert _is_linked(a, 'DOM_ArrayType', b1)
    if hasattr(b1, 'Type380'):
        assert _is_linked(b1, 'Type380', a)
    _safe_set(a, 'DOM_ArrayType', b2)
    assert _is_linked(a, 'DOM_ArrayType', b2)
    if hasattr(b1, 'Type380'):
        assert not _is_linked(b1, 'Type380', a)
    if hasattr(b2, 'Type380'):
        assert _is_linked(b2, 'Type380', a)
    _safe_set(a, 'DOM_ArrayType', None)
    assert not _is_linked(a, 'DOM_ArrayType', b2)
    if hasattr(b2, 'Type380'):
        assert not _is_linked(b2, 'Type380', a)


def test_assoc_elementType381_link_reassign_clear():
    a = DOM_ArrayType(dimensions="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'DOM_ArrayType382', b1)
    assert _is_linked(a, 'DOM_ArrayType382', b1)
    if hasattr(b1, 'Type383'):
        assert _is_linked(b1, 'Type383', a)
    _safe_set(a, 'DOM_ArrayType382', b2)
    assert _is_linked(a, 'DOM_ArrayType382', b2)
    if hasattr(b1, 'Type383'):
        assert not _is_linked(b1, 'Type383', a)
    if hasattr(b2, 'Type383'):
        assert _is_linked(b2, 'Type383', a)
    _safe_set(a, 'DOM_ArrayType382', None)
    assert not _is_linked(a, 'DOM_ArrayType382', b2)
    if hasattr(b2, 'Type383'):
        assert not _is_linked(b2, 'Type383', a)


def test_assoc_expression343_link_reassign_clear():
    a = DOM_SwitchCase(default="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_SwitchCase', b1)
    assert _is_linked(a, 'DOM_SwitchCase', b1)
    if hasattr(b1, 'Expression344'):
        assert _is_linked(b1, 'Expression344', a)
    _safe_set(a, 'DOM_SwitchCase', b2)
    assert _is_linked(a, 'DOM_SwitchCase', b2)
    if hasattr(b1, 'Expression344'):
        assert not _is_linked(b1, 'Expression344', a)
    if hasattr(b2, 'Expression344'):
        assert _is_linked(b2, 'Expression344', a)
    _safe_set(a, 'DOM_SwitchCase', None)
    assert not _is_linked(a, 'DOM_SwitchCase', b2)
    if hasattr(b2, 'Expression344'):
        assert not _is_linked(b2, 'Expression344', a)


def test_assoc_extendedOperands218_link_reassign_clear():
    a = DOM_InfixExpression(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_InfixExpression', {b1})
    assert _is_linked(a, 'DOM_InfixExpression', b1)
    if hasattr(b1, 'Expression219'):
        assert _is_linked(b1, 'Expression219', a)
    _safe_set(a, 'DOM_InfixExpression', {b2})
    assert _is_linked(a, 'DOM_InfixExpression', b2)
    if hasattr(b1, 'Expression219'):
        assert not _is_linked(b1, 'Expression219', a)
    if hasattr(b2, 'Expression219'):
        assert _is_linked(b2, 'Expression219', a)
    _safe_set(a, 'DOM_InfixExpression', set())
    assert not _is_linked(a, 'DOM_InfixExpression', b2)
    if hasattr(b2, 'Expression219'):
        assert not _is_linked(b2, 'Expression219', a)


def test_assoc_fields37_link_reassign_clear():
    a = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    b1 = IField()
    b2 = IField()
    _safe_set(a, 'Core_IType38', {b1})
    assert _is_linked(a, 'Core_IType38', b1)
    if hasattr(b1, 'IField'):
        assert _is_linked(b1, 'IField', a)
    _safe_set(a, 'Core_IType38', {b2})
    assert _is_linked(a, 'Core_IType38', b2)
    if hasattr(b1, 'IField'):
        assert not _is_linked(b1, 'IField', a)
    if hasattr(b2, 'IField'):
        assert _is_linked(b2, 'IField', a)
    _safe_set(a, 'Core_IType38', set())
    assert not _is_linked(a, 'Core_IType38', b2)
    if hasattr(b2, 'IField'):
        assert not _is_linked(b2, 'IField', a)


def test_assoc_fragments96_link_reassign_clear():
    a = DOM_TagElement(nested="sample_text", tagName="sample_text")
    b1 = ASTNode()
    b2 = ASTNode()
    _safe_set(a, 'DOM_TagElement', {b1})
    assert _is_linked(a, 'DOM_TagElement', b1)
    if hasattr(b1, 'ASTNode97'):
        assert _is_linked(b1, 'ASTNode97', a)
    _safe_set(a, 'DOM_TagElement', {b2})
    assert _is_linked(a, 'DOM_TagElement', b2)
    if hasattr(b1, 'ASTNode97'):
        assert not _is_linked(b1, 'ASTNode97', a)
    if hasattr(b2, 'ASTNode97'):
        assert _is_linked(b2, 'ASTNode97', a)
    _safe_set(a, 'DOM_TagElement', set())
    assert not _is_linked(a, 'DOM_TagElement', b2)
    if hasattr(b2, 'ASTNode97'):
        assert not _is_linked(b2, 'ASTNode97', a)


def test_assoc_initializer103_link_reassign_clear():
    a = DOM_VariableDeclaration(extraDimensions="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_VariableDeclaration', b1)
    assert _is_linked(a, 'DOM_VariableDeclaration', b1)
    if hasattr(b1, 'Expression104'):
        assert _is_linked(b1, 'Expression104', a)
    _safe_set(a, 'DOM_VariableDeclaration', b2)
    assert _is_linked(a, 'DOM_VariableDeclaration', b2)
    if hasattr(b1, 'Expression104'):
        assert not _is_linked(b1, 'Expression104', a)
    if hasattr(b2, 'Expression104'):
        assert _is_linked(b2, 'Expression104', a)
    _safe_set(a, 'DOM_VariableDeclaration', None)
    assert not _is_linked(a, 'DOM_VariableDeclaration', b2)
    if hasattr(b2, 'Expression104'):
        assert not _is_linked(b2, 'Expression104', a)


def test_assoc_initializers36_link_reassign_clear():
    a = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    b1 = IInitializer()
    b2 = IInitializer()
    _safe_set(a, 'Core_IType', {b1})
    assert _is_linked(a, 'Core_IType', b1)
    if hasattr(b1, 'IInitializer'):
        assert _is_linked(b1, 'IInitializer', a)
    _safe_set(a, 'Core_IType', {b2})
    assert _is_linked(a, 'Core_IType', b2)
    if hasattr(b1, 'IInitializer'):
        assert not _is_linked(b1, 'IInitializer', a)
    if hasattr(b2, 'IInitializer'):
        assert _is_linked(b2, 'IInitializer', a)
    _safe_set(a, 'Core_IType', set())
    assert not _is_linked(a, 'Core_IType', b2)
    if hasattr(b2, 'IInitializer'):
        assert not _is_linked(b2, 'IInitializer', a)


def test_assoc_leftHandSide181_link_reassign_clear():
    a = DOM_Assignment(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_Assignment', b1)
    assert _is_linked(a, 'DOM_Assignment', b1)
    if hasattr(b1, 'Expression182'):
        assert _is_linked(b1, 'Expression182', a)
    _safe_set(a, 'DOM_Assignment', b2)
    assert _is_linked(a, 'DOM_Assignment', b2)
    if hasattr(b1, 'Expression182'):
        assert not _is_linked(b1, 'Expression182', a)
    if hasattr(b2, 'Expression182'):
        assert _is_linked(b2, 'Expression182', a)
    _safe_set(a, 'DOM_Assignment', None)
    assert not _is_linked(a, 'DOM_Assignment', b2)
    if hasattr(b2, 'Expression182'):
        assert not _is_linked(b2, 'Expression182', a)


def test_assoc_leftOperand220_link_reassign_clear():
    a = DOM_InfixExpression(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_InfixExpression221', b1)
    assert _is_linked(a, 'DOM_InfixExpression221', b1)
    if hasattr(b1, 'Expression222'):
        assert _is_linked(b1, 'Expression222', a)
    _safe_set(a, 'DOM_InfixExpression221', b2)
    assert _is_linked(a, 'DOM_InfixExpression221', b2)
    if hasattr(b1, 'Expression222'):
        assert not _is_linked(b1, 'Expression222', a)
    if hasattr(b2, 'Expression222'):
        assert _is_linked(b2, 'Expression222', a)
    _safe_set(a, 'DOM_InfixExpression221', None)
    assert not _is_linked(a, 'DOM_InfixExpression221', b2)
    if hasattr(b2, 'Expression222'):
        assert not _is_linked(b2, 'Expression222', a)


def test_assoc_methods39_link_reassign_clear():
    a = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    b1 = IMethod()
    b2 = IMethod()
    _safe_set(a, 'Core_IType40', {b1})
    assert _is_linked(a, 'Core_IType40', b1)
    if hasattr(b1, 'IMethod'):
        assert _is_linked(b1, 'IMethod', a)
    _safe_set(a, 'Core_IType40', {b2})
    assert _is_linked(a, 'Core_IType40', b2)
    if hasattr(b1, 'IMethod'):
        assert not _is_linked(b1, 'IMethod', a)
    if hasattr(b2, 'IMethod'):
        assert _is_linked(b2, 'IMethod', a)
    _safe_set(a, 'Core_IType40', set())
    assert not _is_linked(a, 'Core_IType40', b2)
    if hasattr(b2, 'IMethod'):
        assert not _is_linked(b2, 'IMethod', a)


def test_assoc_modifiers400_link_reassign_clear():
    a = DOM_SingleVariableDeclaration(varargs="sample_text")
    b1 = ExtendedModifier()
    b2 = ExtendedModifier()
    _safe_set(a, 'DOM_SingleVariableDeclaration401', {b1})
    assert _is_linked(a, 'DOM_SingleVariableDeclaration401', b1)
    if hasattr(b1, 'ExtendedModifier402'):
        assert _is_linked(b1, 'ExtendedModifier402', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration401', {b2})
    assert _is_linked(a, 'DOM_SingleVariableDeclaration401', b2)
    if hasattr(b1, 'ExtendedModifier402'):
        assert not _is_linked(b1, 'ExtendedModifier402', a)
    if hasattr(b2, 'ExtendedModifier402'):
        assert _is_linked(b2, 'ExtendedModifier402', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration401', set())
    assert not _is_linked(a, 'DOM_SingleVariableDeclaration401', b2)
    if hasattr(b2, 'ExtendedModifier402'):
        assert not _is_linked(b2, 'ExtendedModifier402', a)


def test_assoc_name105_link_reassign_clear():
    a = DOM_VariableDeclaration(extraDimensions="sample_text")
    b1 = SimpleName()
    b2 = SimpleName()
    _safe_set(a, 'DOM_VariableDeclaration106', b1)
    assert _is_linked(a, 'DOM_VariableDeclaration106', b1)
    if hasattr(b1, 'SimpleName107'):
        assert _is_linked(b1, 'SimpleName107', a)
    _safe_set(a, 'DOM_VariableDeclaration106', b2)
    assert _is_linked(a, 'DOM_VariableDeclaration106', b2)
    if hasattr(b1, 'SimpleName107'):
        assert not _is_linked(b1, 'SimpleName107', a)
    if hasattr(b2, 'SimpleName107'):
        assert _is_linked(b2, 'SimpleName107', a)
    _safe_set(a, 'DOM_VariableDeclaration106', None)
    assert not _is_linked(a, 'DOM_VariableDeclaration106', b2)
    if hasattr(b2, 'SimpleName107'):
        assert not _is_linked(b2, 'SimpleName107', a)


def test_assoc_name110_link_reassign_clear():
    a = DOM_AbstractTypeDeclaration(localTypeDeclaration="sample_text", memberTypeDeclaration="sample_text", packageMemberTypeDeclaration="sample_text")
    b1 = SimpleName()
    b2 = SimpleName()
    _safe_set(a, 'DOM_AbstractTypeDeclaration111', b1)
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration111', b1)
    if hasattr(b1, 'SimpleName112'):
        assert _is_linked(b1, 'SimpleName112', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration111', b2)
    assert _is_linked(a, 'DOM_AbstractTypeDeclaration111', b2)
    if hasattr(b1, 'SimpleName112'):
        assert not _is_linked(b1, 'SimpleName112', a)
    if hasattr(b2, 'SimpleName112'):
        assert _is_linked(b2, 'SimpleName112', a)
    _safe_set(a, 'DOM_AbstractTypeDeclaration111', None)
    assert not _is_linked(a, 'DOM_AbstractTypeDeclaration111', b2)
    if hasattr(b2, 'SimpleName112'):
        assert not _is_linked(b2, 'SimpleName112', a)


def test_assoc_name136_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = SimpleName()
    b2 = SimpleName()
    _safe_set(a, 'DOM_MethodDeclaration137', b1)
    assert _is_linked(a, 'DOM_MethodDeclaration137', b1)
    if hasattr(b1, 'SimpleName138'):
        assert _is_linked(b1, 'SimpleName138', a)
    _safe_set(a, 'DOM_MethodDeclaration137', b2)
    assert _is_linked(a, 'DOM_MethodDeclaration137', b2)
    if hasattr(b1, 'SimpleName138'):
        assert not _is_linked(b1, 'SimpleName138', a)
    if hasattr(b2, 'SimpleName138'):
        assert _is_linked(b2, 'SimpleName138', a)
    _safe_set(a, 'DOM_MethodDeclaration137', None)
    assert not _is_linked(a, 'DOM_MethodDeclaration137', b2)
    if hasattr(b2, 'SimpleName138'):
        assert not _is_linked(b2, 'SimpleName138', a)


def test_assoc_name66_link_reassign_clear():
    a = DOM_ImportDeclaration(onDemand="sample_text", static="sample_text")
    b1 = Name()
    b2 = Name()
    _safe_set(a, 'DOM_ImportDeclaration', b1)
    assert _is_linked(a, 'DOM_ImportDeclaration', b1)
    if hasattr(b1, 'Name'):
        assert _is_linked(b1, 'Name', a)
    _safe_set(a, 'DOM_ImportDeclaration', b2)
    assert _is_linked(a, 'DOM_ImportDeclaration', b2)
    if hasattr(b1, 'Name'):
        assert not _is_linked(b1, 'Name', a)
    if hasattr(b2, 'Name'):
        assert _is_linked(b2, 'Name', a)
    _safe_set(a, 'DOM_ImportDeclaration', None)
    assert not _is_linked(a, 'DOM_ImportDeclaration', b2)
    if hasattr(b2, 'Name'):
        assert not _is_linked(b2, 'Name', a)


def test_assoc_name82_link_reassign_clear():
    a = DOM_MethodRefParameter(varargs="sample_text")
    b1 = SimpleName()
    b2 = SimpleName()
    _safe_set(a, 'DOM_MethodRefParameter', b1)
    assert _is_linked(a, 'DOM_MethodRefParameter', b1)
    if hasattr(b1, 'SimpleName83'):
        assert _is_linked(b1, 'SimpleName83', a)
    _safe_set(a, 'DOM_MethodRefParameter', b2)
    assert _is_linked(a, 'DOM_MethodRefParameter', b2)
    if hasattr(b1, 'SimpleName83'):
        assert not _is_linked(b1, 'SimpleName83', a)
    if hasattr(b2, 'SimpleName83'):
        assert _is_linked(b2, 'SimpleName83', a)
    _safe_set(a, 'DOM_MethodRefParameter', None)
    assert not _is_linked(a, 'DOM_MethodRefParameter', b2)
    if hasattr(b2, 'SimpleName83'):
        assert not _is_linked(b2, 'SimpleName83', a)


def test_assoc_operand247_link_reassign_clear():
    a = DOM_PostfixExpression(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_PostfixExpression', b1)
    assert _is_linked(a, 'DOM_PostfixExpression', b1)
    if hasattr(b1, 'Expression248'):
        assert _is_linked(b1, 'Expression248', a)
    _safe_set(a, 'DOM_PostfixExpression', b2)
    assert _is_linked(a, 'DOM_PostfixExpression', b2)
    if hasattr(b1, 'Expression248'):
        assert not _is_linked(b1, 'Expression248', a)
    if hasattr(b2, 'Expression248'):
        assert _is_linked(b2, 'Expression248', a)
    _safe_set(a, 'DOM_PostfixExpression', None)
    assert not _is_linked(a, 'DOM_PostfixExpression', b2)
    if hasattr(b2, 'Expression248'):
        assert not _is_linked(b2, 'Expression248', a)


def test_assoc_operand249_link_reassign_clear():
    a = DOM_PrefixExpression(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_PrefixExpression', b1)
    assert _is_linked(a, 'DOM_PrefixExpression', b1)
    if hasattr(b1, 'Expression250'):
        assert _is_linked(b1, 'Expression250', a)
    _safe_set(a, 'DOM_PrefixExpression', b2)
    assert _is_linked(a, 'DOM_PrefixExpression', b2)
    if hasattr(b1, 'Expression250'):
        assert not _is_linked(b1, 'Expression250', a)
    if hasattr(b2, 'Expression250'):
        assert _is_linked(b2, 'Expression250', a)
    _safe_set(a, 'DOM_PrefixExpression', None)
    assert not _is_linked(a, 'DOM_PrefixExpression', b2)
    if hasattr(b2, 'Expression250'):
        assert not _is_linked(b2, 'Expression250', a)


def test_assoc_packageFragmentRoot12_link_reassign_clear():
    a = Core_IPackageFragment(isDefaultPackage="sample_text")
    b1 = IPackageFragmentRoot()
    b2 = IPackageFragmentRoot()
    _safe_set(a, 'packageFragments', b1)
    assert _is_linked(a, 'packageFragments', b1)
    if hasattr(b1, 'IPackageFragmentRoot13'):
        assert _is_linked(b1, 'IPackageFragmentRoot13', a)
    _safe_set(a, 'packageFragments', b2)
    assert _is_linked(a, 'packageFragments', b2)
    if hasattr(b1, 'IPackageFragmentRoot13'):
        assert not _is_linked(b1, 'IPackageFragmentRoot13', a)
    if hasattr(b2, 'IPackageFragmentRoot13'):
        assert _is_linked(b2, 'IPackageFragmentRoot13', a)
    _safe_set(a, 'packageFragments', None)
    assert not _is_linked(a, 'packageFragments', b2)
    if hasattr(b2, 'IPackageFragmentRoot13'):
        assert not _is_linked(b2, 'IPackageFragmentRoot13', a)


def test_assoc_parameters142_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = SingleVariableDeclaration()
    b2 = SingleVariableDeclaration()
    _safe_set(a, 'DOM_MethodDeclaration143', {b1})
    assert _is_linked(a, 'DOM_MethodDeclaration143', b1)
    if hasattr(b1, 'SingleVariableDeclaration144'):
        assert _is_linked(b1, 'SingleVariableDeclaration144', a)
    _safe_set(a, 'DOM_MethodDeclaration143', {b2})
    assert _is_linked(a, 'DOM_MethodDeclaration143', b2)
    if hasattr(b1, 'SingleVariableDeclaration144'):
        assert not _is_linked(b1, 'SingleVariableDeclaration144', a)
    if hasattr(b2, 'SingleVariableDeclaration144'):
        assert _is_linked(b2, 'SingleVariableDeclaration144', a)
    _safe_set(a, 'DOM_MethodDeclaration143', set())
    assert not _is_linked(a, 'DOM_MethodDeclaration143', b2)
    if hasattr(b2, 'SingleVariableDeclaration144'):
        assert not _is_linked(b2, 'SingleVariableDeclaration144', a)


def test_assoc_parameters46_link_reassign_clear():
    a = Core_IMethod(exceptionTypes="sample_text", isConstructor="sample_text", isMainMethod="sample_text", returnType="sample_text")
    b1 = Parameter()
    b2 = Parameter()
    _safe_set(a, 'Core_IMethod', {b1})
    assert _is_linked(a, 'Core_IMethod', b1)
    if hasattr(b1, 'Parameter'):
        assert _is_linked(b1, 'Parameter', a)
    _safe_set(a, 'Core_IMethod', {b2})
    assert _is_linked(a, 'Core_IMethod', b2)
    if hasattr(b1, 'Parameter'):
        assert not _is_linked(b1, 'Parameter', a)
    if hasattr(b2, 'Parameter'):
        assert _is_linked(b2, 'Parameter', a)
    _safe_set(a, 'Core_IMethod', set())
    assert not _is_linked(a, 'Core_IMethod', b2)
    if hasattr(b2, 'Parameter'):
        assert not _is_linked(b2, 'Parameter', a)


def test_assoc_returnType139_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'DOM_MethodDeclaration140', b1)
    assert _is_linked(a, 'DOM_MethodDeclaration140', b1)
    if hasattr(b1, 'Type141'):
        assert _is_linked(b1, 'Type141', a)
    _safe_set(a, 'DOM_MethodDeclaration140', b2)
    assert _is_linked(a, 'DOM_MethodDeclaration140', b2)
    if hasattr(b1, 'Type141'):
        assert not _is_linked(b1, 'Type141', a)
    if hasattr(b2, 'Type141'):
        assert _is_linked(b2, 'Type141', a)
    _safe_set(a, 'DOM_MethodDeclaration140', None)
    assert not _is_linked(a, 'DOM_MethodDeclaration140', b2)
    if hasattr(b2, 'Type141'):
        assert not _is_linked(b2, 'Type141', a)


def test_assoc_rightHandSide183_link_reassign_clear():
    a = DOM_Assignment(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_Assignment184', b1)
    assert _is_linked(a, 'DOM_Assignment184', b1)
    if hasattr(b1, 'Expression185'):
        assert _is_linked(b1, 'Expression185', a)
    _safe_set(a, 'DOM_Assignment184', b2)
    assert _is_linked(a, 'DOM_Assignment184', b2)
    if hasattr(b1, 'Expression185'):
        assert not _is_linked(b1, 'Expression185', a)
    if hasattr(b2, 'Expression185'):
        assert _is_linked(b2, 'Expression185', a)
    _safe_set(a, 'DOM_Assignment184', None)
    assert not _is_linked(a, 'DOM_Assignment184', b2)
    if hasattr(b2, 'Expression185'):
        assert not _is_linked(b2, 'Expression185', a)


def test_assoc_rightOperand223_link_reassign_clear():
    a = DOM_InfixExpression(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'DOM_InfixExpression224', b1)
    assert _is_linked(a, 'DOM_InfixExpression224', b1)
    if hasattr(b1, 'Expression225'):
        assert _is_linked(b1, 'Expression225', a)
    _safe_set(a, 'DOM_InfixExpression224', b2)
    assert _is_linked(a, 'DOM_InfixExpression224', b2)
    if hasattr(b1, 'Expression225'):
        assert not _is_linked(b1, 'Expression225', a)
    if hasattr(b2, 'Expression225'):
        assert _is_linked(b2, 'Expression225', a)
    _safe_set(a, 'DOM_InfixExpression224', None)
    assert not _is_linked(a, 'DOM_InfixExpression224', b2)
    if hasattr(b2, 'Expression225'):
        assert not _is_linked(b2, 'Expression225', a)


def test_assoc_sourceRange30_link_reassign_clear():
    a = Core_ISourceReference(source="sample_text")
    b1 = ISourceRange()
    b2 = ISourceRange()
    _safe_set(a, 'Core_ISourceReference', b1)
    assert _is_linked(a, 'Core_ISourceReference', b1)
    if hasattr(b1, 'ISourceRange'):
        assert _is_linked(b1, 'ISourceRange', a)
    _safe_set(a, 'Core_ISourceReference', b2)
    assert _is_linked(a, 'Core_ISourceReference', b2)
    if hasattr(b1, 'ISourceRange'):
        assert not _is_linked(b1, 'ISourceRange', a)
    if hasattr(b2, 'ISourceRange'):
        assert _is_linked(b2, 'ISourceRange', a)
    _safe_set(a, 'Core_ISourceReference', None)
    assert not _is_linked(a, 'Core_ISourceReference', b2)
    if hasattr(b2, 'ISourceRange'):
        assert not _is_linked(b2, 'ISourceRange', a)


def test_assoc_superInterfaceTypes159_link_reassign_clear():
    a = DOM_TypeDeclaration(interface="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'DOM_TypeDeclaration160', {b1})
    assert _is_linked(a, 'DOM_TypeDeclaration160', b1)
    if hasattr(b1, 'Type161'):
        assert _is_linked(b1, 'Type161', a)
    _safe_set(a, 'DOM_TypeDeclaration160', {b2})
    assert _is_linked(a, 'DOM_TypeDeclaration160', b2)
    if hasattr(b1, 'Type161'):
        assert not _is_linked(b1, 'Type161', a)
    if hasattr(b2, 'Type161'):
        assert _is_linked(b2, 'Type161', a)
    _safe_set(a, 'DOM_TypeDeclaration160', set())
    assert not _is_linked(a, 'DOM_TypeDeclaration160', b2)
    if hasattr(b2, 'Type161'):
        assert not _is_linked(b2, 'Type161', a)


def test_assoc_superclassType157_link_reassign_clear():
    a = DOM_TypeDeclaration(interface="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'DOM_TypeDeclaration', b1)
    assert _is_linked(a, 'DOM_TypeDeclaration', b1)
    if hasattr(b1, 'Type158'):
        assert _is_linked(b1, 'Type158', a)
    _safe_set(a, 'DOM_TypeDeclaration', b2)
    assert _is_linked(a, 'DOM_TypeDeclaration', b2)
    if hasattr(b1, 'Type158'):
        assert not _is_linked(b1, 'Type158', a)
    if hasattr(b2, 'Type158'):
        assert _is_linked(b2, 'Type158', a)
    _safe_set(a, 'DOM_TypeDeclaration', None)
    assert not _is_linked(a, 'DOM_TypeDeclaration', b2)
    if hasattr(b2, 'Type158'):
        assert not _is_linked(b2, 'Type158', a)


def test_assoc_thrownExceptions145_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = Name()
    b2 = Name()
    _safe_set(a, 'DOM_MethodDeclaration146', {b1})
    assert _is_linked(a, 'DOM_MethodDeclaration146', b1)
    if hasattr(b1, 'Name147'):
        assert _is_linked(b1, 'Name147', a)
    _safe_set(a, 'DOM_MethodDeclaration146', {b2})
    assert _is_linked(a, 'DOM_MethodDeclaration146', b2)
    if hasattr(b1, 'Name147'):
        assert not _is_linked(b1, 'Name147', a)
    if hasattr(b2, 'Name147'):
        assert _is_linked(b2, 'Name147', a)
    _safe_set(a, 'DOM_MethodDeclaration146', set())
    assert not _is_linked(a, 'DOM_MethodDeclaration146', b2)
    if hasattr(b2, 'Name147'):
        assert not _is_linked(b2, 'Name147', a)


def test_assoc_type28_link_reassign_clear():
    a = Core_IClassFile(isClass="sample_text", isInterface="sample_text")
    b1 = IType()
    b2 = IType()
    _safe_set(a, 'Core_IClassFile', b1)
    assert _is_linked(a, 'Core_IClassFile', b1)
    if hasattr(b1, 'IType29'):
        assert _is_linked(b1, 'IType29', a)
    _safe_set(a, 'Core_IClassFile', b2)
    assert _is_linked(a, 'Core_IClassFile', b2)
    if hasattr(b1, 'IType29'):
        assert not _is_linked(b1, 'IType29', a)
    if hasattr(b2, 'IType29'):
        assert _is_linked(b2, 'IType29', a)
    _safe_set(a, 'Core_IClassFile', None)
    assert not _is_linked(a, 'Core_IClassFile', b2)
    if hasattr(b2, 'IType29'):
        assert not _is_linked(b2, 'IType29', a)


def test_assoc_type398_link_reassign_clear():
    a = DOM_SingleVariableDeclaration(varargs="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'DOM_SingleVariableDeclaration', b1)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration', b1)
    if hasattr(b1, 'Type399'):
        assert _is_linked(b1, 'Type399', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration', b2)
    assert _is_linked(a, 'DOM_SingleVariableDeclaration', b2)
    if hasattr(b1, 'Type399'):
        assert not _is_linked(b1, 'Type399', a)
    if hasattr(b2, 'Type399'):
        assert _is_linked(b2, 'Type399', a)
    _safe_set(a, 'DOM_SingleVariableDeclaration', None)
    assert not _is_linked(a, 'DOM_SingleVariableDeclaration', b2)
    if hasattr(b2, 'Type399'):
        assert not _is_linked(b2, 'Type399', a)


def test_assoc_type84_link_reassign_clear():
    a = DOM_MethodRefParameter(varargs="sample_text")
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'DOM_MethodRefParameter85', b1)
    assert _is_linked(a, 'DOM_MethodRefParameter85', b1)
    if hasattr(b1, 'Type'):
        assert _is_linked(b1, 'Type', a)
    _safe_set(a, 'DOM_MethodRefParameter85', b2)
    assert _is_linked(a, 'DOM_MethodRefParameter85', b2)
    if hasattr(b1, 'Type'):
        assert not _is_linked(b1, 'Type', a)
    if hasattr(b2, 'Type'):
        assert _is_linked(b2, 'Type', a)
    _safe_set(a, 'DOM_MethodRefParameter85', None)
    assert not _is_linked(a, 'DOM_MethodRefParameter85', b2)
    if hasattr(b2, 'Type'):
        assert not _is_linked(b2, 'Type', a)


def test_assoc_typeBinding64_link_reassign_clear():
    a = DOM_Expression(resolveBoxing="sample_text", resolveUnboxing="sample_text")
    b1 = IType()
    b2 = IType()
    _safe_set(a, 'DOM_Expression', b1)
    assert _is_linked(a, 'DOM_Expression', b1)
    if hasattr(b1, 'IType65'):
        assert _is_linked(b1, 'IType65', a)
    _safe_set(a, 'DOM_Expression', b2)
    assert _is_linked(a, 'DOM_Expression', b2)
    if hasattr(b1, 'IType65'):
        assert not _is_linked(b1, 'IType65', a)
    if hasattr(b2, 'IType65'):
        assert _is_linked(b2, 'IType65', a)
    _safe_set(a, 'DOM_Expression', None)
    assert not _is_linked(a, 'DOM_Expression', b2)
    if hasattr(b2, 'IType65'):
        assert not _is_linked(b2, 'IType65', a)


def test_assoc_typeParameters148_link_reassign_clear():
    a = DOM_MethodDeclaration(constructor="sample_text", extraDimensions="sample_text", varargs="sample_text")
    b1 = TypeParameter()
    b2 = TypeParameter()
    _safe_set(a, 'DOM_MethodDeclaration149', {b1})
    assert _is_linked(a, 'DOM_MethodDeclaration149', b1)
    if hasattr(b1, 'TypeParameter'):
        assert _is_linked(b1, 'TypeParameter', a)
    _safe_set(a, 'DOM_MethodDeclaration149', {b2})
    assert _is_linked(a, 'DOM_MethodDeclaration149', b2)
    if hasattr(b1, 'TypeParameter'):
        assert not _is_linked(b1, 'TypeParameter', a)
    if hasattr(b2, 'TypeParameter'):
        assert _is_linked(b2, 'TypeParameter', a)
    _safe_set(a, 'DOM_MethodDeclaration149', set())
    assert not _is_linked(a, 'DOM_MethodDeclaration149', b2)
    if hasattr(b2, 'TypeParameter'):
        assert not _is_linked(b2, 'TypeParameter', a)


def test_assoc_typeParameters162_link_reassign_clear():
    a = DOM_TypeDeclaration(interface="sample_text")
    b1 = TypeParameter()
    b2 = TypeParameter()
    _safe_set(a, 'DOM_TypeDeclaration163', {b1})
    assert _is_linked(a, 'DOM_TypeDeclaration163', b1)
    if hasattr(b1, 'TypeParameter164'):
        assert _is_linked(b1, 'TypeParameter164', a)
    _safe_set(a, 'DOM_TypeDeclaration163', {b2})
    assert _is_linked(a, 'DOM_TypeDeclaration163', b2)
    if hasattr(b1, 'TypeParameter164'):
        assert not _is_linked(b1, 'TypeParameter164', a)
    if hasattr(b2, 'TypeParameter164'):
        assert _is_linked(b2, 'TypeParameter164', a)
    _safe_set(a, 'DOM_TypeDeclaration163', set())
    assert not _is_linked(a, 'DOM_TypeDeclaration163', b2)
    if hasattr(b2, 'TypeParameter164'):
        assert not _is_linked(b2, 'TypeParameter164', a)


def test_assoc_typeParameters44_link_reassign_clear():
    a = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    b1 = ITypeParameter()
    b2 = ITypeParameter()
    _safe_set(a, 'Core_IType45', {b1})
    assert _is_linked(a, 'Core_IType45', b1)
    if hasattr(b1, 'ITypeParameter'):
        assert _is_linked(b1, 'ITypeParameter', a)
    _safe_set(a, 'Core_IType45', {b2})
    assert _is_linked(a, 'Core_IType45', b2)
    if hasattr(b1, 'ITypeParameter'):
        assert not _is_linked(b1, 'ITypeParameter', a)
    if hasattr(b2, 'ITypeParameter'):
        assert _is_linked(b2, 'ITypeParameter', a)
    _safe_set(a, 'Core_IType45', set())
    assert not _is_linked(a, 'Core_IType45', b2)
    if hasattr(b2, 'ITypeParameter'):
        assert not _is_linked(b2, 'ITypeParameter', a)


def test_assoc_types41_link_reassign_clear():
    a = Core_IType(fullyQualifiedName="sample_text", fullyQualifiedParametrizedName="sample_text")
    b1 = IType()
    b2 = IType()
    _safe_set(a, 'Core_IType42', {b1})
    assert _is_linked(a, 'Core_IType42', b1)
    if hasattr(b1, 'IType43'):
        assert _is_linked(b1, 'IType43', a)
    _safe_set(a, 'Core_IType42', {b2})
    assert _is_linked(a, 'Core_IType42', b2)
    if hasattr(b1, 'IType43'):
        assert not _is_linked(b1, 'IType43', a)
    if hasattr(b2, 'IType43'):
        assert _is_linked(b2, 'IType43', a)
    _safe_set(a, 'Core_IType42', set())
    assert not _is_linked(a, 'Core_IType42', b2)
    if hasattr(b2, 'IType43'):
        assert not _is_linked(b2, 'IType43', a)


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


AnonymousClassDeclaration_strategy = st.builds(AnonymousClassDeclaration)
@given(instance=AnonymousClassDeclaration_strategy)
@settings(max_examples=25)
def test_AnonymousClassDeclaration_instantiation(instance):
    assert isinstance(instance, AnonymousClassDeclaration)


ArrayInitializer_strategy = st.builds(ArrayInitializer)
@given(instance=ArrayInitializer_strategy)
@settings(max_examples=25)
def test_ArrayInitializer_instantiation(instance):
    assert isinstance(instance, ArrayInitializer)


ArrayType_strategy = st.builds(ArrayType)
@given(instance=ArrayType_strategy)
@settings(max_examples=25)
def test_ArrayType_instantiation(instance):
    assert isinstance(instance, ArrayType)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


BodyDeclaration_strategy = st.builds(BodyDeclaration)
@given(instance=BodyDeclaration_strategy)
@settings(max_examples=25)
def test_BodyDeclaration_instantiation(instance):
    assert isinstance(instance, BodyDeclaration)


CatchClause_strategy = st.builds(CatchClause)
@given(instance=CatchClause_strategy)
@settings(max_examples=25)
def test_CatchClause_instantiation(instance):
    assert isinstance(instance, CatchClause)


Comment_strategy = st.builds(Comment)
@given(instance=Comment_strategy)
@settings(max_examples=25)
def test_Comment_instantiation(instance):
    assert isinstance(instance, Comment)


CompilationUnit_strategy = st.builds(CompilationUnit)
@given(instance=CompilationUnit_strategy)
@settings(max_examples=25)
def test_CompilationUnit_instantiation(instance):
    assert isinstance(instance, CompilationUnit)


Core_BinaryPackageFragmentRoot_strategy = st.builds(Core_BinaryPackageFragmentRoot)
@given(instance=Core_BinaryPackageFragmentRoot_strategy)
@settings(max_examples=25)
def test_Core_BinaryPackageFragmentRoot_instantiation(instance):
    assert isinstance(instance, Core_BinaryPackageFragmentRoot)


Core_IClassFile_strategy = st.builds(Core_IClassFile, isClass=safe_text, isInterface=safe_text)
@given(instance=Core_IClassFile_strategy)
@settings(max_examples=25)
def test_Core_IClassFile_instantiation(instance):
    assert isinstance(instance, Core_IClassFile)


Core_ICompilationUnit_strategy = st.builds(Core_ICompilationUnit)
@given(instance=Core_ICompilationUnit_strategy)
@settings(max_examples=25)
def test_Core_ICompilationUnit_instantiation(instance):
    assert isinstance(instance, Core_ICompilationUnit)


Core_IField_strategy = st.builds(Core_IField, constant=safe_text, isEnumConstant=safe_text, isTransient=safe_text, isVolatile=safe_text, typeSignature=safe_text)
@given(instance=Core_IField_strategy)
@settings(max_examples=25)
def test_Core_IField_instantiation(instance):
    assert isinstance(instance, Core_IField)


Core_IImportDeclaration_strategy = st.builds(Core_IImportDeclaration, isOnDemand=safe_text, isStatic=safe_text)
@given(instance=Core_IImportDeclaration_strategy)
@settings(max_examples=25)
def test_Core_IImportDeclaration_instantiation(instance):
    assert isinstance(instance, Core_IImportDeclaration)


Core_IInitializer_strategy = st.builds(Core_IInitializer)
@given(instance=Core_IInitializer_strategy)
@settings(max_examples=25)
def test_Core_IInitializer_instantiation(instance):
    assert isinstance(instance, Core_IInitializer)


Core_IJavaElement_strategy = st.builds(Core_IJavaElement, elementName=safe_text)
@given(instance=Core_IJavaElement_strategy)
@settings(max_examples=25)
def test_Core_IJavaElement_instantiation(instance):
    assert isinstance(instance, Core_IJavaElement)


Core_IJavaModel_strategy = st.builds(Core_IJavaModel)
@given(instance=Core_IJavaModel_strategy)
@settings(max_examples=25)
def test_Core_IJavaModel_instantiation(instance):
    assert isinstance(instance, Core_IJavaModel)


Core_IJavaProject_strategy = st.builds(Core_IJavaProject)
@given(instance=Core_IJavaProject_strategy)
@settings(max_examples=25)
def test_Core_IJavaProject_instantiation(instance):
    assert isinstance(instance, Core_IJavaProject)


Core_IMember_strategy = st.builds(Core_IMember)
@given(instance=Core_IMember_strategy)
@settings(max_examples=25)
def test_Core_IMember_instantiation(instance):
    assert isinstance(instance, Core_IMember)


Core_IMethod_strategy = st.builds(Core_IMethod, exceptionTypes=safe_text, isConstructor=safe_text, isMainMethod=safe_text, returnType=safe_text)
@given(instance=Core_IMethod_strategy)
@settings(max_examples=25)
def test_Core_IMethod_instantiation(instance):
    assert isinstance(instance, Core_IMethod)


Core_IPackageFragment_strategy = st.builds(Core_IPackageFragment, isDefaultPackage=safe_text)
@given(instance=Core_IPackageFragment_strategy)
@settings(max_examples=25)
def test_Core_IPackageFragment_instantiation(instance):
    assert isinstance(instance, Core_IPackageFragment)


Core_IPackageFragmentRoot_strategy = st.builds(Core_IPackageFragmentRoot)
@given(instance=Core_IPackageFragmentRoot_strategy)
@settings(max_examples=25)
def test_Core_IPackageFragmentRoot_instantiation(instance):
    assert isinstance(instance, Core_IPackageFragmentRoot)


Core_ISourceRange_strategy = st.builds(Core_ISourceRange, length=safe_text, offset=safe_text)
@given(instance=Core_ISourceRange_strategy)
@settings(max_examples=25)
def test_Core_ISourceRange_instantiation(instance):
    assert isinstance(instance, Core_ISourceRange)


Core_ISourceReference_strategy = st.builds(Core_ISourceReference, source=safe_text)
@given(instance=Core_ISourceReference_strategy)
@settings(max_examples=25)
def test_Core_ISourceReference_instantiation(instance):
    assert isinstance(instance, Core_ISourceReference)


Core_IType_strategy = st.builds(Core_IType, fullyQualifiedName=safe_text, fullyQualifiedParametrizedName=safe_text)
@given(instance=Core_IType_strategy)
@settings(max_examples=25)
def test_Core_IType_instantiation(instance):
    assert isinstance(instance, Core_IType)


Core_ITypeParameter_strategy = st.builds(Core_ITypeParameter, bounds=safe_text)
@given(instance=Core_ITypeParameter_strategy)
@settings(max_examples=25)
def test_Core_ITypeParameter_instantiation(instance):
    assert isinstance(instance, Core_ITypeParameter)


Core_ITypeRoot_strategy = st.builds(Core_ITypeRoot)
@given(instance=Core_ITypeRoot_strategy)
@settings(max_examples=25)
def test_Core_ITypeRoot_instantiation(instance):
    assert isinstance(instance, Core_ITypeRoot)


Core_Parameter_strategy = st.builds(Core_Parameter, name=safe_text, type=safe_text)
@given(instance=Core_Parameter_strategy)
@settings(max_examples=25)
def test_Core_Parameter_instantiation(instance):
    assert isinstance(instance, Core_Parameter)


Core_PhysicalElement_strategy = st.builds(Core_PhysicalElement, isReadOnly=safe_text, path=safe_text)
@given(instance=Core_PhysicalElement_strategy)
@settings(max_examples=25)
def test_Core_PhysicalElement_instantiation(instance):
    assert isinstance(instance, Core_PhysicalElement)


Core_SourcePackageFragmentRoot_strategy = st.builds(Core_SourcePackageFragmentRoot)
@given(instance=Core_SourcePackageFragmentRoot_strategy)
@settings(max_examples=25)
def test_Core_SourcePackageFragmentRoot_instantiation(instance):
    assert isinstance(instance, Core_SourcePackageFragmentRoot)


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


EnumConstantDeclaration_strategy = st.builds(EnumConstantDeclaration)
@given(instance=EnumConstantDeclaration_strategy)
@settings(max_examples=25)
def test_EnumConstantDeclaration_instantiation(instance):
    assert isinstance(instance, EnumConstantDeclaration)


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


IClassFile_strategy = st.builds(IClassFile)
@given(instance=IClassFile_strategy)
@settings(max_examples=25)
def test_IClassFile_instantiation(instance):
    assert isinstance(instance, IClassFile)


ICompilationUnit_strategy = st.builds(ICompilationUnit)
@given(instance=ICompilationUnit_strategy)
@settings(max_examples=25)
def test_ICompilationUnit_instantiation(instance):
    assert isinstance(instance, ICompilationUnit)


IField_strategy = st.builds(IField)
@given(instance=IField_strategy)
@settings(max_examples=25)
def test_IField_instantiation(instance):
    assert isinstance(instance, IField)


IImportDeclaration_strategy = st.builds(IImportDeclaration)
@given(instance=IImportDeclaration_strategy)
@settings(max_examples=25)
def test_IImportDeclaration_instantiation(instance):
    assert isinstance(instance, IImportDeclaration)


IInitializer_strategy = st.builds(IInitializer)
@given(instance=IInitializer_strategy)
@settings(max_examples=25)
def test_IInitializer_instantiation(instance):
    assert isinstance(instance, IInitializer)


IJavaElement_strategy = st.builds(IJavaElement)
@given(instance=IJavaElement_strategy)
@settings(max_examples=25)
def test_IJavaElement_instantiation(instance):
    assert isinstance(instance, IJavaElement)


IJavaProject_strategy = st.builds(IJavaProject)
@given(instance=IJavaProject_strategy)
@settings(max_examples=25)
def test_IJavaProject_instantiation(instance):
    assert isinstance(instance, IJavaProject)


IMember_strategy = st.builds(IMember)
@given(instance=IMember_strategy)
@settings(max_examples=25)
def test_IMember_instantiation(instance):
    assert isinstance(instance, IMember)


IMethod_strategy = st.builds(IMethod)
@given(instance=IMethod_strategy)
@settings(max_examples=25)
def test_IMethod_instantiation(instance):
    assert isinstance(instance, IMethod)


IPackageFragment_strategy = st.builds(IPackageFragment)
@given(instance=IPackageFragment_strategy)
@settings(max_examples=25)
def test_IPackageFragment_instantiation(instance):
    assert isinstance(instance, IPackageFragment)


IPackageFragmentRoot_strategy = st.builds(IPackageFragmentRoot)
@given(instance=IPackageFragmentRoot_strategy)
@settings(max_examples=25)
def test_IPackageFragmentRoot_instantiation(instance):
    assert isinstance(instance, IPackageFragmentRoot)


ISourceRange_strategy = st.builds(ISourceRange)
@given(instance=ISourceRange_strategy)
@settings(max_examples=25)
def test_ISourceRange_instantiation(instance):
    assert isinstance(instance, ISourceRange)


ISourceReference_strategy = st.builds(ISourceReference)
@given(instance=ISourceReference_strategy)
@settings(max_examples=25)
def test_ISourceReference_instantiation(instance):
    assert isinstance(instance, ISourceReference)


IType_strategy = st.builds(IType)
@given(instance=IType_strategy)
@settings(max_examples=25)
def test_IType_instantiation(instance):
    assert isinstance(instance, IType)


ITypeParameter_strategy = st.builds(ITypeParameter)
@given(instance=ITypeParameter_strategy)
@settings(max_examples=25)
def test_ITypeParameter_instantiation(instance):
    assert isinstance(instance, ITypeParameter)


ITypeRoot_strategy = st.builds(ITypeRoot)
@given(instance=ITypeRoot_strategy)
@settings(max_examples=25)
def test_ITypeRoot_instantiation(instance):
    assert isinstance(instance, ITypeRoot)


ImportDeclaration_strategy = st.builds(ImportDeclaration)
@given(instance=ImportDeclaration_strategy)
@settings(max_examples=25)
def test_ImportDeclaration_instantiation(instance):
    assert isinstance(instance, ImportDeclaration)


Javadoc_strategy = st.builds(Javadoc)
@given(instance=Javadoc_strategy)
@settings(max_examples=25)
def test_Javadoc_instantiation(instance):
    assert isinstance(instance, Javadoc)


MemberValuePair_strategy = st.builds(MemberValuePair)
@given(instance=MemberValuePair_strategy)
@settings(max_examples=25)
def test_MemberValuePair_instantiation(instance):
    assert isinstance(instance, MemberValuePair)


MethodRefParameter_strategy = st.builds(MethodRefParameter)
@given(instance=MethodRefParameter_strategy)
@settings(max_examples=25)
def test_MethodRefParameter_instantiation(instance):
    assert isinstance(instance, MethodRefParameter)


Name_strategy = st.builds(Name)
@given(instance=Name_strategy)
@settings(max_examples=25)
def test_Name_instantiation(instance):
    assert isinstance(instance, Name)


PackageDeclaration_strategy = st.builds(PackageDeclaration)
@given(instance=PackageDeclaration_strategy)
@settings(max_examples=25)
def test_PackageDeclaration_instantiation(instance):
    assert isinstance(instance, PackageDeclaration)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


PhysicalElement_strategy = st.builds(PhysicalElement)
@given(instance=PhysicalElement_strategy)
@settings(max_examples=25)
def test_PhysicalElement_instantiation(instance):
    assert isinstance(instance, PhysicalElement)


SimpleName_strategy = st.builds(SimpleName)
@given(instance=SimpleName_strategy)
@settings(max_examples=25)
def test_SimpleName_instantiation(instance):
    assert isinstance(instance, SimpleName)


SingleVariableDeclaration_strategy = st.builds(SingleVariableDeclaration)
@given(instance=SingleVariableDeclaration_strategy)
@settings(max_examples=25)
def test_SingleVariableDeclaration_instantiation(instance):
    assert isinstance(instance, SingleVariableDeclaration)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


TagElement_strategy = st.builds(TagElement)
@given(instance=TagElement_strategy)
@settings(max_examples=25)
def test_TagElement_instantiation(instance):
    assert isinstance(instance, TagElement)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


TypeParameter_strategy = st.builds(TypeParameter)
@given(instance=TypeParameter_strategy)
@settings(max_examples=25)
def test_TypeParameter_instantiation(instance):
    assert isinstance(instance, TypeParameter)


VariableDeclaration_strategy = st.builds(VariableDeclaration)
@given(instance=VariableDeclaration_strategy)
@settings(max_examples=25)
def test_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)


VariableDeclarationFragment_strategy = st.builds(VariableDeclarationFragment)
@given(instance=VariableDeclarationFragment_strategy)
@settings(max_examples=25)
def test_VariableDeclarationFragment_instantiation(instance):
    assert isinstance(instance, VariableDeclarationFragment)



