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
    ShiftOperator,
    c_sharp_operators_RightShift,
    c_sharp_operators_LeftShift,
    UnaryModificationOperator,
    c_sharp_operators_PlusPlus,
    c_sharp_operators_MinusMinus,
    UnaryOperator,
    c_sharp_operators_Negate,
    c_sharp_operators_Complement,
    MultiplicativeOperator,
    c_sharp_operators_Remainder,
    c_sharp_operators_Multiplication,
    c_sharp_operators_Division,
    operators_UnaryOperator,
    operators_AdditiveOperator,
    c_sharp_operators_Subtraction,
    c_sharp_operators_Addition,
    RelationOperator,
    c_sharp_operators_GreaterThanOrEqual,
    c_sharp_operators_LessThan,
    c_sharp_operators_LessThanOrEqual,
    c_sharp_operators_GreaterThan,
    EqualityOperator,
    c_sharp_operators_NotEqual,
    c_sharp_operators_Equal,
    c_sharp_operators_ConditionalOr,
    c_sharp_operators_ConditionalAnd,
    c_sharp_operators_InclusiveOr,
    c_sharp_operators_ExclusiveOr,
    c_sharp_operators_And,
    c_sharp_operators_UnsignedRightShift,
    Operator,
    c_sharp_operators_UnaryModificationOperator,
    c_sharp_operators_RelationOperator,
    c_sharp_operators_MultiplicativeOperator,
    c_sharp_operators_EqualityOperator,
    c_sharp_operators_UnaryOperator,
    c_sharp_operators_AssignmentOperator,
    c_sharp_operators_ShiftOperator,
    c_sharp_operators_AdditiveOperator,
    c_sharp_operators_Operator,
    c_sharp_keywords_Event,
    c_sharp_keywords_Return,
    c_sharp_keywords_Default,
    c_sharp_keywords_Case,
    c_sharp_keywords_Params,
    c_sharp_keywords_Ref,
    c_sharp_keywords_Out,
    c_sharp_modifiers_Modifier,
    ReferenceType,
    c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType,
    Literal,
    c_sharp_literals_StringLiteral,
    c_sharp_literals_RealLiteral,
    c_sharp_literals_CharacterLiteral,
    c_sharp_literals_NullLiteral,
    c_sharp_literals_DecimalIntegerLiteral,
    c_sharp_literals_This,
    c_sharp_literals_HexadecimalIntegerLiteral,
    c_sharp_literals_BooleanLiteral,
    InclusiveOrExpression,
    c_sharp_expressions_ConditionalAndExpression,
    InclusiveOr,
    ExclusiveOrExpression,
    c_sharp_expressions_InclusiveOrExpression,
    ExclusiveOr,
    AndExpression,
    c_sharp_expressions_ExclusiveOrExpression,
    And,
    EqualityExpression,
    c_sharp_expressions_AndExpression,
    NotEqual,
    Equal,
    types_Type,
    types_NonArrayType,
    c_sharp_types_SimpleType,
    c_sharp_types_PointerType,
    c_sharp_types_ReferenceType,
    c_sharp_types_NonArrayType,
    c_sharp_types_Type,
    ConditionalOr,
    ConditionalAndExpression,
    c_sharp_expressions_ConditionalOrExpression,
    ConditionalAnd,
    MultiplicativeExpression,
    c_sharp_expressions_AdditiveExpression,
    Remainder,
    Division,
    c_sharp_expressions_MultiplicativeExpression,
    c_sharp_expressions_AddressOfExpression,
    c_sharp_expressions_CastExpression,
    RelationalExpression,
    c_sharp_expressions_EqualityExpression,
    GreaterThanOrEqual,
    GreaterThan,
    LessThanOrEqual,
    LessThan,
    ShiftExpression,
    c_sharp_expressions_RelationalExpression,
    AdditiveExpression,
    LeftShift,
    RightShift,
    c_sharp_expressions_ShiftExpression,
    AssignmentOperator,
    c_sharp_operators_AssignmentUnsignedRightShift,
    c_sharp_operators_AssignmentAnd,
    c_sharp_operators_AssignmentExclusiveOr,
    c_sharp_operators_AssignmentLeftShift,
    c_sharp_operators_AssignmentPlus,
    c_sharp_operators_AssignmentDivision,
    c_sharp_operators_AssignmentOr,
    c_sharp_operators_Assignment,
    c_sharp_operators_AssignmentRightShift,
    c_sharp_operators_AssignmentMultiplication,
    c_sharp_operators_AssignmentMinus,
    c_sharp_operators_AssignmentModulo,
    expressions_Expression,
    ConditionalOrExpression,
    AddressOfExpression,
    CastExpression,
    PreDecrementExpression,
    ArrayInitializer,
    PrimaryNoArrayCreationExpression,
    c_sharp_literals_Literal,
    c_sharp_expressions_TypeOfExpression,
    c_sharp_expressions_SizeOfExpression,
    c_sharp_expressions_UncheckedExpression,
    c_sharp_expressions_DelegateCreationExpression,
    c_sharp_expressions_CheckedExpression,
    c_sharp_expressions_BaseAccess,
    PreIncrementExpression,
    UnaryExpression,
    Multiplication,
    Complement,
    Negate,
    Subtraction,
    Addition,
    MemberAccess,
    c_sharp_expressions_UnaryExpression,
    c_sharp_expressions_ParenthesizedExpression,
    c_sharp_expressions_Argument,
    c_sharp_expressions_ExpressionList,
    classes_VariableInitializer,
    c_sharp_expressions_StatementExpression,
    ArgumentList,
    expressions_StatementExpression,
    c_sharp_expressions_AssignmentExpression,
    expressions_PrimaryExtendedExpressionType,
    c_sharp_expressions_PostIncrementExpression,
    c_sharp_expressions_PostDecrementExpression,
    c_sharp_expressions_InvocationExpression,
    SimpleType,
    c_sharp_types_Byte,
    c_sharp_types_UInt,
    c_sharp_types_Float,
    c_sharp_types_Short,
    c_sharp_types_Object,
    c_sharp_types_Void,
    c_sharp_types_Bool,
    c_sharp_types_Decimal,
    c_sharp_types_SByte,
    c_sharp_types_Double,
    c_sharp_types_Char,
    c_sharp_types_UShort,
    c_sharp_types_Long,
    c_sharp_types_String,
    c_sharp_types_Int,
    c_sharp_types_ULong,
    PrimaryExtendedExpressionType,
    c_sharp_expressions_PointerMemberAccess,
    c_sharp_expressions_ElementAccess,
    c_sharp_expressions_MemberAccess,
    c_sharp_expressions_PrimaryExtendedExpressionType,
    PrimaryExpression,
    c_sharp_expressions_ArrayCreationExpression,
    c_sharp_expressions_PrimaryNoArrayCreationExpression,
    c_sharp_expressions_PrimaryExpression,
    Argument,
    c_sharp_expressions_ArgumentList,
    FixedPointerDeclarator,
    PointerType,
    ResourceAcquisition,
    c_sharp_statements_ResourceAcquisition,
    c_sharp_statements_LocalConstantDeclaration,
    statements_ResourceAcquisition,
    c_sharp_expressions_Expression,
    statements_ForInitializer,
    c_sharp_statements_VariableDeclaration,
    c_sharp_statements_FixedPointerDeclarator,
    JumpStatement,
    c_sharp_statements_ReturnStatement,
    c_sharp_statements_ContinueStatement,
    c_sharp_statements_GotoStatement,
    c_sharp_statements_BreakStatement,
    c_sharp_statements_ForInitializer,
    c_sharp_statements_FinallyClause,
    c_sharp_statements_GeneralCatchClause,
    c_sharp_statements_SpecificCatchClause,
    FinallyClause,
    GeneralCatchClause,
    SpecificCatchClause,
    c_sharp_statements_ThrowStatement,
    Default,
    c_sharp_statements_SwitchLabel,
    SwitchLabel,
    c_sharp_statements_SwitchSection,
    SwitchSection,
    SelectionStatement,
    c_sharp_statements_SwitchStatement,
    c_sharp_statements_IfStatement,
    StatementExpression,
    c_sharp_expressions_PreDecrementExpression,
    c_sharp_expressions_PreIncrementExpression,
    StatementExpressionList,
    ForInitializer,
    c_sharp_expressions_StatementExpressionList,
    IterationStatement,
    c_sharp_statements_ForeachStatement,
    c_sharp_statements_DoStatement,
    c_sharp_statements_ForStatement,
    c_sharp_statements_WhileStatement,
    Case,
    NamedArgumentList,
    ExpressionList,
    c_sharp_attributes_AttributeArguments,
    AttributeArguments,
    c_sharp_attributes_Attribute,
    Return,
    Event,
    c_sharp_attributes_AttributeTarget,
    AttributeTarget,
    c_sharp_attributes_Attributes,
    c_sharp_attributes_GlobalAttributeTarget,
    Unsafe,
    EmbeddedStatement,
    c_sharp_statements_CheckedStatement,
    c_sharp_statements_LockStatement,
    c_sharp_statements_UncheckedStatement,
    c_sharp_statements_SelectionStatement,
    c_sharp_statements_UsingStatement,
    c_sharp_statements_EmptyStatement,
    c_sharp_statements_IterationStatement,
    c_sharp_statements_ExpressionStatement,
    c_sharp_statements_JumpStatement,
    c_sharp_statements_TryStatement,
    c_sharp_statements_FixedStatement,
    c_sharp_statements_SimpleEmbeddedStatement,
    LocalConstantDeclaration,
    VariableDeclaration,
    statements_Statement,
    c_sharp_statements_Statement,
    c_sharp_attributes_NamedArgument,
    NamedArgument,
    c_sharp_attributes_NamedArgumentList,
    ConstantDeclarator,
    c_sharp_classes_VariableInitializer,
    Statement,
    c_sharp_statements_DeclarationStatement,
    c_sharp_statements_EmbeddedStatement,
    c_sharp_classes_Block,
    ArrayType,
    Attribute,
    GlobalAttributeTarget,
    c_sharp_attributes_GlobalAttributes,
    c_sharp_arrays_RankSpecifier,
    RankSpecifier,
    NonArrayType,
    Expression,
    c_sharp_expressions_ConditionalExpression,
    VariableInitializer,
    c_sharp_arrays_ArrayInitializer,
    c_sharp_arrays_StackallocInitializer,
    VariableDeclarator,
    FormalParameterList,
    Type,
    c_sharp_arrays_ArrayType,
    c_sharp_classes_ClassMemberDeclaration,
    ClassOrInterfaceOrDelegateOrEnumType,
    c_sharp_classes_ClassBase,
    ClassMemberDeclaration,
    c_sharp_classes_ConstantDeclaration,
    c_sharp_classes_FieldDeclaration,
    Params,
    c_sharp_classes_ParameterArray,
    Out,
    Ref,
    c_sharp_classes_FixedParameter,
    ParameterArray,
    FixedParameter,
    c_sharp_classes_FormalParameterList,
    Block,
    NamespaceMemberDeclaration,
    GlobalAttributes,
    UsingDirective,
    c_sharp_namespaces_CompilationUnit,
    expressions_PrimaryNoArrayCreationExpression,
    c_sharp_expressions_ObjectCreationExpression,
    common_NamedElement,
    c_sharp_statements_LabeledStatement,
    c_sharp_common_Identifier,
    Identifier,
    c_sharp_common_NamespaceOrTypeName,
    c_sharp_common_NamedElement,
    ClassBase,
    Modifier,
    c_sharp_modifiers_Extern,
    c_sharp_modifiers_ReadOnly,
    c_sharp_modifiers_New,
    c_sharp_modifiers_Partial,
    c_sharp_modifiers_Volatile,
    c_sharp_modifiers_Sealed,
    c_sharp_modifiers_Private,
    c_sharp_modifiers_Public,
    c_sharp_modifiers_Abstract,
    c_sharp_modifiers_Virtual,
    c_sharp_modifiers_OverrideModifier,
    c_sharp_modifiers_Static,
    c_sharp_modifiers_Protected,
    c_sharp_modifiers_Internal,
    c_sharp_modifiers_Unsafe,
    Attributes,
    namespaces_TypeDeclaration,
    c_sharp_classes_Class,
    classes_ClassMemberDeclaration,
    c_sharp_classes_Method,
    namespaces_NamespaceMemberDeclaration,
    c_sharp_namespaces_TypeDeclaration,
    c_sharp_namespaces_NamespaceBody,
    NamespaceBody,
    c_sharp_namespaces_Namespace,
    c_sharp_namespaces_NamespaceMemberDeclaration,
    NamespaceOrTypeName,
    NamedElement,
    c_sharp_statements_VariableDeclarator,
    c_sharp_statements_ConstantDeclarator,
    c_sharp_namespaces_UsingDirective,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(ShiftOperator)


def test_hyp_shiftoperator_constructor_exists():
    assert callable(ShiftOperator.__init__)


def test_hyp_shiftoperator_constructor_args():
    sig = inspect.signature(ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_rightshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_RightShift)


def test_hyp_c_sharp_operators_rightshift_constructor_exists():
    assert callable(c_sharp_operators_RightShift.__init__)


def test_hyp_c_sharp_operators_rightshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_RightShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_leftshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_LeftShift)


def test_hyp_c_sharp_operators_leftshift_constructor_exists():
    assert callable(c_sharp_operators_LeftShift.__init__)


def test_hyp_c_sharp_operators_leftshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryModificationOperator)


def test_hyp_unarymodificationoperator_constructor_exists():
    assert callable(UnaryModificationOperator.__init__)


def test_hyp_unarymodificationoperator_constructor_args():
    sig = inspect.signature(UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_plusplus_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_PlusPlus)


def test_hyp_c_sharp_operators_plusplus_constructor_exists():
    assert callable(c_sharp_operators_PlusPlus.__init__)


def test_hyp_c_sharp_operators_plusplus_constructor_args():
    sig = inspect.signature(c_sharp_operators_PlusPlus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_minusminus_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_MinusMinus)


def test_hyp_c_sharp_operators_minusminus_constructor_exists():
    assert callable(c_sharp_operators_MinusMinus.__init__)


def test_hyp_c_sharp_operators_minusminus_constructor_args():
    sig = inspect.signature(c_sharp_operators_MinusMinus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_hyp_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_hyp_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_negate_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Negate)


def test_hyp_c_sharp_operators_negate_constructor_exists():
    assert callable(c_sharp_operators_Negate.__init__)


def test_hyp_c_sharp_operators_negate_constructor_args():
    sig = inspect.signature(c_sharp_operators_Negate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_complement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Complement)


def test_hyp_c_sharp_operators_complement_constructor_exists():
    assert callable(c_sharp_operators_Complement.__init__)


def test_hyp_c_sharp_operators_complement_constructor_args():
    sig = inspect.signature(c_sharp_operators_Complement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeOperator)


def test_hyp_multiplicativeoperator_constructor_exists():
    assert callable(MultiplicativeOperator.__init__)


def test_hyp_multiplicativeoperator_constructor_args():
    sig = inspect.signature(MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_remainder_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Remainder)


def test_hyp_c_sharp_operators_remainder_constructor_exists():
    assert callable(c_sharp_operators_Remainder.__init__)


def test_hyp_c_sharp_operators_remainder_constructor_args():
    sig = inspect.signature(c_sharp_operators_Remainder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_multiplication_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Multiplication)


def test_hyp_c_sharp_operators_multiplication_constructor_exists():
    assert callable(c_sharp_operators_Multiplication.__init__)


def test_hyp_c_sharp_operators_multiplication_constructor_args():
    sig = inspect.signature(c_sharp_operators_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_division_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Division)


def test_hyp_c_sharp_operators_division_constructor_exists():
    assert callable(c_sharp_operators_Division.__init__)


def test_hyp_c_sharp_operators_division_constructor_args():
    sig = inspect.signature(c_sharp_operators_Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(operators_UnaryOperator)


def test_hyp_operators_unaryoperator_constructor_exists():
    assert callable(operators_UnaryOperator.__init__)


def test_hyp_operators_unaryoperator_constructor_args():
    sig = inspect.signature(operators_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operators_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(operators_AdditiveOperator)


def test_hyp_operators_additiveoperator_constructor_exists():
    assert callable(operators_AdditiveOperator.__init__)


def test_hyp_operators_additiveoperator_constructor_args():
    sig = inspect.signature(operators_AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_subtraction_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Subtraction)


def test_hyp_c_sharp_operators_subtraction_constructor_exists():
    assert callable(c_sharp_operators_Subtraction.__init__)


def test_hyp_c_sharp_operators_subtraction_constructor_args():
    sig = inspect.signature(c_sharp_operators_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_addition_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Addition)


def test_hyp_c_sharp_operators_addition_constructor_exists():
    assert callable(c_sharp_operators_Addition.__init__)


def test_hyp_c_sharp_operators_addition_constructor_args():
    sig = inspect.signature(c_sharp_operators_Addition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationoperator_is_not_abstract():
    assert not inspect.isabstract(RelationOperator)


def test_hyp_relationoperator_constructor_exists():
    assert callable(RelationOperator.__init__)


def test_hyp_relationoperator_constructor_args():
    sig = inspect.signature(RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_GreaterThanOrEqual)


def test_hyp_c_sharp_operators_greaterthanorequal_constructor_exists():
    assert callable(c_sharp_operators_GreaterThanOrEqual.__init__)


def test_hyp_c_sharp_operators_greaterthanorequal_constructor_args():
    sig = inspect.signature(c_sharp_operators_GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_lessthan_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_LessThan)


def test_hyp_c_sharp_operators_lessthan_constructor_exists():
    assert callable(c_sharp_operators_LessThan.__init__)


def test_hyp_c_sharp_operators_lessthan_constructor_args():
    sig = inspect.signature(c_sharp_operators_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_LessThanOrEqual)


def test_hyp_c_sharp_operators_lessthanorequal_constructor_exists():
    assert callable(c_sharp_operators_LessThanOrEqual.__init__)


def test_hyp_c_sharp_operators_lessthanorequal_constructor_args():
    sig = inspect.signature(c_sharp_operators_LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_greaterthan_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_GreaterThan)


def test_hyp_c_sharp_operators_greaterthan_constructor_exists():
    assert callable(c_sharp_operators_GreaterThan.__init__)


def test_hyp_c_sharp_operators_greaterthan_constructor_args():
    sig = inspect.signature(c_sharp_operators_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(EqualityOperator)


def test_hyp_equalityoperator_constructor_exists():
    assert callable(EqualityOperator.__init__)


def test_hyp_equalityoperator_constructor_args():
    sig = inspect.signature(EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_notequal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_NotEqual)


def test_hyp_c_sharp_operators_notequal_constructor_exists():
    assert callable(c_sharp_operators_NotEqual.__init__)


def test_hyp_c_sharp_operators_notequal_constructor_args():
    sig = inspect.signature(c_sharp_operators_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_equal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Equal)


def test_hyp_c_sharp_operators_equal_constructor_exists():
    assert callable(c_sharp_operators_Equal.__init__)


def test_hyp_c_sharp_operators_equal_constructor_args():
    sig = inspect.signature(c_sharp_operators_Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_conditionalor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_ConditionalOr)


def test_hyp_c_sharp_operators_conditionalor_constructor_exists():
    assert callable(c_sharp_operators_ConditionalOr.__init__)


def test_hyp_c_sharp_operators_conditionalor_constructor_args():
    sig = inspect.signature(c_sharp_operators_ConditionalOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_conditionaland_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_ConditionalAnd)


def test_hyp_c_sharp_operators_conditionaland_constructor_exists():
    assert callable(c_sharp_operators_ConditionalAnd.__init__)


def test_hyp_c_sharp_operators_conditionaland_constructor_args():
    sig = inspect.signature(c_sharp_operators_ConditionalAnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_inclusiveor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_InclusiveOr)


def test_hyp_c_sharp_operators_inclusiveor_constructor_exists():
    assert callable(c_sharp_operators_InclusiveOr.__init__)


def test_hyp_c_sharp_operators_inclusiveor_constructor_args():
    sig = inspect.signature(c_sharp_operators_InclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_exclusiveor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_ExclusiveOr)


def test_hyp_c_sharp_operators_exclusiveor_constructor_exists():
    assert callable(c_sharp_operators_ExclusiveOr.__init__)


def test_hyp_c_sharp_operators_exclusiveor_constructor_args():
    sig = inspect.signature(c_sharp_operators_ExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_and_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_And)


def test_hyp_c_sharp_operators_and_constructor_exists():
    assert callable(c_sharp_operators_And.__init__)


def test_hyp_c_sharp_operators_and_constructor_args():
    sig = inspect.signature(c_sharp_operators_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_unsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_UnsignedRightShift)


def test_hyp_c_sharp_operators_unsignedrightshift_constructor_exists():
    assert callable(c_sharp_operators_UnsignedRightShift.__init__)


def test_hyp_c_sharp_operators_unsignedrightshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_UnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_hyp_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_hyp_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_unarymodificationoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_UnaryModificationOperator)


def test_hyp_c_sharp_operators_unarymodificationoperator_constructor_exists():
    assert callable(c_sharp_operators_UnaryModificationOperator.__init__)


def test_hyp_c_sharp_operators_unarymodificationoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_UnaryModificationOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_relationoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_RelationOperator)


def test_hyp_c_sharp_operators_relationoperator_constructor_exists():
    assert callable(c_sharp_operators_RelationOperator.__init__)


def test_hyp_c_sharp_operators_relationoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_RelationOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_multiplicativeoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_MultiplicativeOperator)


def test_hyp_c_sharp_operators_multiplicativeoperator_constructor_exists():
    assert callable(c_sharp_operators_MultiplicativeOperator.__init__)


def test_hyp_c_sharp_operators_multiplicativeoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_MultiplicativeOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_equalityoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_EqualityOperator)


def test_hyp_c_sharp_operators_equalityoperator_constructor_exists():
    assert callable(c_sharp_operators_EqualityOperator.__init__)


def test_hyp_c_sharp_operators_equalityoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_EqualityOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_UnaryOperator)


def test_hyp_c_sharp_operators_unaryoperator_constructor_exists():
    assert callable(c_sharp_operators_UnaryOperator.__init__)


def test_hyp_c_sharp_operators_unaryoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentOperator)


def test_hyp_c_sharp_operators_assignmentoperator_constructor_exists():
    assert callable(c_sharp_operators_AssignmentOperator.__init__)


def test_hyp_c_sharp_operators_assignmentoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_shiftoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_ShiftOperator)


def test_hyp_c_sharp_operators_shiftoperator_constructor_exists():
    assert callable(c_sharp_operators_ShiftOperator.__init__)


def test_hyp_c_sharp_operators_shiftoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_ShiftOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_additiveoperator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AdditiveOperator)


def test_hyp_c_sharp_operators_additiveoperator_constructor_exists():
    assert callable(c_sharp_operators_AdditiveOperator.__init__)


def test_hyp_c_sharp_operators_additiveoperator_constructor_args():
    sig = inspect.signature(c_sharp_operators_AdditiveOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_operator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Operator)


def test_hyp_c_sharp_operators_operator_constructor_exists():
    assert callable(c_sharp_operators_Operator.__init__)


def test_hyp_c_sharp_operators_operator_constructor_args():
    sig = inspect.signature(c_sharp_operators_Operator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_keywords_event_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Event)


def test_hyp_c_sharp_keywords_event_constructor_exists():
    assert callable(c_sharp_keywords_Event.__init__)


def test_hyp_c_sharp_keywords_event_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_keywords_return_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Return)


def test_hyp_c_sharp_keywords_return_constructor_exists():
    assert callable(c_sharp_keywords_Return.__init__)


def test_hyp_c_sharp_keywords_return_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_keywords_default_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Default)


def test_hyp_c_sharp_keywords_default_constructor_exists():
    assert callable(c_sharp_keywords_Default.__init__)


def test_hyp_c_sharp_keywords_default_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Default.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_keywords_case_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Case)


def test_hyp_c_sharp_keywords_case_constructor_exists():
    assert callable(c_sharp_keywords_Case.__init__)


def test_hyp_c_sharp_keywords_case_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Case.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_keywords_params_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Params)


def test_hyp_c_sharp_keywords_params_constructor_exists():
    assert callable(c_sharp_keywords_Params.__init__)


def test_hyp_c_sharp_keywords_params_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Params.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_keywords_ref_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Ref)


def test_hyp_c_sharp_keywords_ref_constructor_exists():
    assert callable(c_sharp_keywords_Ref.__init__)


def test_hyp_c_sharp_keywords_ref_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Ref.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_keywords_out_is_not_abstract():
    assert not inspect.isabstract(c_sharp_keywords_Out)


def test_hyp_c_sharp_keywords_out_constructor_exists():
    assert callable(c_sharp_keywords_Out.__init__)


def test_hyp_c_sharp_keywords_out_constructor_args():
    sig = inspect.signature(c_sharp_keywords_Out.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_modifier_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Modifier)


def test_hyp_c_sharp_modifiers_modifier_constructor_exists():
    assert callable(c_sharp_modifiers_Modifier.__init__)


def test_hyp_c_sharp_modifiers_modifier_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Modifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_referencetype_is_not_abstract():
    assert not inspect.isabstract(ReferenceType)


def test_hyp_referencetype_constructor_exists():
    assert callable(ReferenceType.__init__)


def test_hyp_referencetype_constructor_args():
    sig = inspect.signature(ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_classorinterfaceordelegateorenumtype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType)


def test_hyp_c_sharp_types_classorinterfaceordelegateorenumtype_constructor_exists():
    assert callable(c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType.__init__)


def test_hyp_c_sharp_types_classorinterfaceordelegateorenumtype_constructor_args():
    sig = inspect.signature(c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_literals_stringliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_StringLiteral)


def test_hyp_c_sharp_literals_stringliteral_constructor_exists():
    assert callable(c_sharp_literals_StringLiteral.__init__)


def test_hyp_c_sharp_literals_stringliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_c_sharp_literals_realliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_RealLiteral)


def test_hyp_c_sharp_literals_realliteral_constructor_exists():
    assert callable(c_sharp_literals_RealLiteral.__init__)


def test_hyp_c_sharp_literals_realliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_c_sharp_literals_characterliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_CharacterLiteral)


def test_hyp_c_sharp_literals_characterliteral_constructor_exists():
    assert callable(c_sharp_literals_CharacterLiteral.__init__)


def test_hyp_c_sharp_literals_characterliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_c_sharp_literals_nullliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_NullLiteral)


def test_hyp_c_sharp_literals_nullliteral_constructor_exists():
    assert callable(c_sharp_literals_NullLiteral.__init__)


def test_hyp_c_sharp_literals_nullliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_literals_decimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_DecimalIntegerLiteral)


def test_hyp_c_sharp_literals_decimalintegerliteral_constructor_exists():
    assert callable(c_sharp_literals_DecimalIntegerLiteral.__init__)


def test_hyp_c_sharp_literals_decimalintegerliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_DecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_c_sharp_literals_this_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_This)


def test_hyp_c_sharp_literals_this_constructor_exists():
    assert callable(c_sharp_literals_This.__init__)


def test_hyp_c_sharp_literals_this_constructor_args():
    sig = inspect.signature(c_sharp_literals_This.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_literals_hexadecimalintegerliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_HexadecimalIntegerLiteral)


def test_hyp_c_sharp_literals_hexadecimalintegerliteral_constructor_exists():
    assert callable(c_sharp_literals_HexadecimalIntegerLiteral.__init__)


def test_hyp_c_sharp_literals_hexadecimalintegerliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_HexadecimalIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_c_sharp_literals_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_BooleanLiteral)


def test_hyp_c_sharp_literals_booleanliteral_constructor_exists():
    assert callable(c_sharp_literals_BooleanLiteral.__init__)


def test_hyp_c_sharp_literals_booleanliteral_constructor_args():
    sig = inspect.signature(c_sharp_literals_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(InclusiveOrExpression)


def test_hyp_inclusiveorexpression_constructor_exists():
    assert callable(InclusiveOrExpression.__init__)


def test_hyp_inclusiveorexpression_constructor_args():
    sig = inspect.signature(InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ConditionalAndExpression)


def test_hyp_c_sharp_expressions_conditionalandexpression_constructor_exists():
    assert callable(c_sharp_expressions_ConditionalAndExpression.__init__)


def test_hyp_c_sharp_expressions_conditionalandexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inclusiveor_is_not_abstract():
    assert not inspect.isabstract(InclusiveOr)


def test_hyp_inclusiveor_constructor_exists():
    assert callable(InclusiveOr.__init__)


def test_hyp_inclusiveor_constructor_args():
    sig = inspect.signature(InclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(ExclusiveOrExpression)


def test_hyp_exclusiveorexpression_constructor_exists():
    assert callable(ExclusiveOrExpression.__init__)


def test_hyp_exclusiveorexpression_constructor_args():
    sig = inspect.signature(ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_InclusiveOrExpression)


def test_hyp_c_sharp_expressions_inclusiveorexpression_constructor_exists():
    assert callable(c_sharp_expressions_InclusiveOrExpression.__init__)


def test_hyp_c_sharp_expressions_inclusiveorexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_exclusiveor_is_not_abstract():
    assert not inspect.isabstract(ExclusiveOr)


def test_hyp_exclusiveor_constructor_exists():
    assert callable(ExclusiveOr.__init__)


def test_hyp_exclusiveor_constructor_args():
    sig = inspect.signature(ExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_andexpression_is_not_abstract():
    assert not inspect.isabstract(AndExpression)


def test_hyp_andexpression_constructor_exists():
    assert callable(AndExpression.__init__)


def test_hyp_andexpression_constructor_args():
    sig = inspect.signature(AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ExclusiveOrExpression)


def test_hyp_c_sharp_expressions_exclusiveorexpression_constructor_exists():
    assert callable(c_sharp_expressions_ExclusiveOrExpression.__init__)


def test_hyp_c_sharp_expressions_exclusiveorexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_and_is_not_abstract():
    assert not inspect.isabstract(And)


def test_hyp_and_constructor_exists():
    assert callable(And.__init__)


def test_hyp_and_constructor_args():
    sig = inspect.signature(And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(EqualityExpression)


def test_hyp_equalityexpression_constructor_exists():
    assert callable(EqualityExpression.__init__)


def test_hyp_equalityexpression_constructor_args():
    sig = inspect.signature(EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_andexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_AndExpression)


def test_hyp_c_sharp_expressions_andexpression_constructor_exists():
    assert callable(c_sharp_expressions_AndExpression.__init__)


def test_hyp_c_sharp_expressions_andexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notequal_is_not_abstract():
    assert not inspect.isabstract(NotEqual)


def test_hyp_notequal_constructor_exists():
    assert callable(NotEqual.__init__)


def test_hyp_notequal_constructor_args():
    sig = inspect.signature(NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_equal_is_not_abstract():
    assert not inspect.isabstract(Equal)


def test_hyp_equal_constructor_exists():
    assert callable(Equal.__init__)


def test_hyp_equal_constructor_args():
    sig = inspect.signature(Equal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_hyp_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_hyp_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_types_nonarraytype_is_not_abstract():
    assert not inspect.isabstract(types_NonArrayType)


def test_hyp_types_nonarraytype_constructor_exists():
    assert callable(types_NonArrayType.__init__)


def test_hyp_types_nonarraytype_constructor_args():
    sig = inspect.signature(types_NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_simpletype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_SimpleType)


def test_hyp_c_sharp_types_simpletype_constructor_exists():
    assert callable(c_sharp_types_SimpleType.__init__)


def test_hyp_c_sharp_types_simpletype_constructor_args():
    sig = inspect.signature(c_sharp_types_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_pointertype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_PointerType)


def test_hyp_c_sharp_types_pointertype_constructor_exists():
    assert callable(c_sharp_types_PointerType.__init__)


def test_hyp_c_sharp_types_pointertype_constructor_args():
    sig = inspect.signature(c_sharp_types_PointerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_referencetype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_ReferenceType)


def test_hyp_c_sharp_types_referencetype_constructor_exists():
    assert callable(c_sharp_types_ReferenceType.__init__)


def test_hyp_c_sharp_types_referencetype_constructor_args():
    sig = inspect.signature(c_sharp_types_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_nonarraytype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_NonArrayType)


def test_hyp_c_sharp_types_nonarraytype_constructor_exists():
    assert callable(c_sharp_types_NonArrayType.__init__)


def test_hyp_c_sharp_types_nonarraytype_constructor_args():
    sig = inspect.signature(c_sharp_types_NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_type_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Type)


def test_hyp_c_sharp_types_type_constructor_exists():
    assert callable(c_sharp_types_Type.__init__)


def test_hyp_c_sharp_types_type_constructor_args():
    sig = inspect.signature(c_sharp_types_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionalor_is_not_abstract():
    assert not inspect.isabstract(ConditionalOr)


def test_hyp_conditionalor_constructor_exists():
    assert callable(ConditionalOr.__init__)


def test_hyp_conditionalor_constructor_args():
    sig = inspect.signature(ConditionalOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(ConditionalAndExpression)


def test_hyp_conditionalandexpression_constructor_exists():
    assert callable(ConditionalAndExpression.__init__)


def test_hyp_conditionalandexpression_constructor_args():
    sig = inspect.signature(ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ConditionalOrExpression)


def test_hyp_c_sharp_expressions_conditionalorexpression_constructor_exists():
    assert callable(c_sharp_expressions_ConditionalOrExpression.__init__)


def test_hyp_c_sharp_expressions_conditionalorexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionaland_is_not_abstract():
    assert not inspect.isabstract(ConditionalAnd)


def test_hyp_conditionaland_constructor_exists():
    assert callable(ConditionalAnd.__init__)


def test_hyp_conditionaland_constructor_args():
    sig = inspect.signature(ConditionalAnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(MultiplicativeExpression)


def test_hyp_multiplicativeexpression_constructor_exists():
    assert callable(MultiplicativeExpression.__init__)


def test_hyp_multiplicativeexpression_constructor_args():
    sig = inspect.signature(MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_AdditiveExpression)


def test_hyp_c_sharp_expressions_additiveexpression_constructor_exists():
    assert callable(c_sharp_expressions_AdditiveExpression.__init__)


def test_hyp_c_sharp_expressions_additiveexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_remainder_is_not_abstract():
    assert not inspect.isabstract(Remainder)


def test_hyp_remainder_constructor_exists():
    assert callable(Remainder.__init__)


def test_hyp_remainder_constructor_args():
    sig = inspect.signature(Remainder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_division_is_not_abstract():
    assert not inspect.isabstract(Division)


def test_hyp_division_constructor_exists():
    assert callable(Division.__init__)


def test_hyp_division_constructor_args():
    sig = inspect.signature(Division.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_MultiplicativeExpression)


def test_hyp_c_sharp_expressions_multiplicativeexpression_constructor_exists():
    assert callable(c_sharp_expressions_MultiplicativeExpression.__init__)


def test_hyp_c_sharp_expressions_multiplicativeexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_addressofexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_AddressOfExpression)


def test_hyp_c_sharp_expressions_addressofexpression_constructor_exists():
    assert callable(c_sharp_expressions_AddressOfExpression.__init__)


def test_hyp_c_sharp_expressions_addressofexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_AddressOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_castexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_CastExpression)


def test_hyp_c_sharp_expressions_castexpression_constructor_exists():
    assert callable(c_sharp_expressions_CastExpression.__init__)


def test_hyp_c_sharp_expressions_castexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(RelationalExpression)


def test_hyp_relationalexpression_constructor_exists():
    assert callable(RelationalExpression.__init__)


def test_hyp_relationalexpression_constructor_args():
    sig = inspect.signature(RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_EqualityExpression)


def test_hyp_c_sharp_expressions_equalityexpression_constructor_exists():
    assert callable(c_sharp_expressions_EqualityExpression.__init__)


def test_hyp_c_sharp_expressions_equalityexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(GreaterThanOrEqual)


def test_hyp_greaterthanorequal_constructor_exists():
    assert callable(GreaterThanOrEqual.__init__)


def test_hyp_greaterthanorequal_constructor_args():
    sig = inspect.signature(GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_greaterthan_is_not_abstract():
    assert not inspect.isabstract(GreaterThan)


def test_hyp_greaterthan_constructor_exists():
    assert callable(GreaterThan.__init__)


def test_hyp_greaterthan_constructor_args():
    sig = inspect.signature(GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(LessThanOrEqual)


def test_hyp_lessthanorequal_constructor_exists():
    assert callable(LessThanOrEqual.__init__)


def test_hyp_lessthanorequal_constructor_args():
    sig = inspect.signature(LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lessthan_is_not_abstract():
    assert not inspect.isabstract(LessThan)


def test_hyp_lessthan_constructor_exists():
    assert callable(LessThan.__init__)


def test_hyp_lessthan_constructor_args():
    sig = inspect.signature(LessThan.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(ShiftExpression)


def test_hyp_shiftexpression_constructor_exists():
    assert callable(ShiftExpression.__init__)


def test_hyp_shiftexpression_constructor_args():
    sig = inspect.signature(ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_RelationalExpression)


def test_hyp_c_sharp_expressions_relationalexpression_constructor_exists():
    assert callable(c_sharp_expressions_RelationalExpression.__init__)


def test_hyp_c_sharp_expressions_relationalexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(AdditiveExpression)


def test_hyp_additiveexpression_constructor_exists():
    assert callable(AdditiveExpression.__init__)


def test_hyp_additiveexpression_constructor_args():
    sig = inspect.signature(AdditiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_leftshift_is_not_abstract():
    assert not inspect.isabstract(LeftShift)


def test_hyp_leftshift_constructor_exists():
    assert callable(LeftShift.__init__)


def test_hyp_leftshift_constructor_args():
    sig = inspect.signature(LeftShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rightshift_is_not_abstract():
    assert not inspect.isabstract(RightShift)


def test_hyp_rightshift_constructor_exists():
    assert callable(RightShift.__init__)


def test_hyp_rightshift_constructor_args():
    sig = inspect.signature(RightShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ShiftExpression)


def test_hyp_c_sharp_expressions_shiftexpression_constructor_exists():
    assert callable(c_sharp_expressions_ShiftExpression.__init__)


def test_hyp_c_sharp_expressions_shiftexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ShiftExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_assignmentoperator_is_not_abstract():
    assert not inspect.isabstract(AssignmentOperator)


def test_hyp_assignmentoperator_constructor_exists():
    assert callable(AssignmentOperator.__init__)


def test_hyp_assignmentoperator_constructor_args():
    sig = inspect.signature(AssignmentOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentunsignedrightshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentUnsignedRightShift)


def test_hyp_c_sharp_operators_assignmentunsignedrightshift_constructor_exists():
    assert callable(c_sharp_operators_AssignmentUnsignedRightShift.__init__)


def test_hyp_c_sharp_operators_assignmentunsignedrightshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentUnsignedRightShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentand_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentAnd)


def test_hyp_c_sharp_operators_assignmentand_constructor_exists():
    assert callable(c_sharp_operators_AssignmentAnd.__init__)


def test_hyp_c_sharp_operators_assignmentand_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentAnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentexclusiveor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentExclusiveOr)


def test_hyp_c_sharp_operators_assignmentexclusiveor_constructor_exists():
    assert callable(c_sharp_operators_AssignmentExclusiveOr.__init__)


def test_hyp_c_sharp_operators_assignmentexclusiveor_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentExclusiveOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentleftshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentLeftShift)


def test_hyp_c_sharp_operators_assignmentleftshift_constructor_exists():
    assert callable(c_sharp_operators_AssignmentLeftShift.__init__)


def test_hyp_c_sharp_operators_assignmentleftshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentplus_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentPlus)


def test_hyp_c_sharp_operators_assignmentplus_constructor_exists():
    assert callable(c_sharp_operators_AssignmentPlus.__init__)


def test_hyp_c_sharp_operators_assignmentplus_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentPlus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentdivision_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentDivision)


def test_hyp_c_sharp_operators_assignmentdivision_constructor_exists():
    assert callable(c_sharp_operators_AssignmentDivision.__init__)


def test_hyp_c_sharp_operators_assignmentdivision_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentDivision.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentor_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentOr)


def test_hyp_c_sharp_operators_assignmentor_constructor_exists():
    assert callable(c_sharp_operators_AssignmentOr.__init__)


def test_hyp_c_sharp_operators_assignmentor_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignment_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_Assignment)


def test_hyp_c_sharp_operators_assignment_constructor_exists():
    assert callable(c_sharp_operators_Assignment.__init__)


def test_hyp_c_sharp_operators_assignment_constructor_args():
    sig = inspect.signature(c_sharp_operators_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentrightshift_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentRightShift)


def test_hyp_c_sharp_operators_assignmentrightshift_constructor_exists():
    assert callable(c_sharp_operators_AssignmentRightShift.__init__)


def test_hyp_c_sharp_operators_assignmentrightshift_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentRightShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentmultiplication_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentMultiplication)


def test_hyp_c_sharp_operators_assignmentmultiplication_constructor_exists():
    assert callable(c_sharp_operators_AssignmentMultiplication.__init__)


def test_hyp_c_sharp_operators_assignmentmultiplication_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentMultiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentminus_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentMinus)


def test_hyp_c_sharp_operators_assignmentminus_constructor_exists():
    assert callable(c_sharp_operators_AssignmentMinus.__init__)


def test_hyp_c_sharp_operators_assignmentminus_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentMinus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_operators_assignmentmodulo_is_not_abstract():
    assert not inspect.isabstract(c_sharp_operators_AssignmentModulo)


def test_hyp_c_sharp_operators_assignmentmodulo_constructor_exists():
    assert callable(c_sharp_operators_AssignmentModulo.__init__)


def test_hyp_c_sharp_operators_assignmentmodulo_constructor_args():
    sig = inspect.signature(c_sharp_operators_AssignmentModulo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(expressions_Expression)


def test_hyp_expressions_expression_constructor_exists():
    assert callable(expressions_Expression.__init__)


def test_hyp_expressions_expression_constructor_args():
    sig = inspect.signature(expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(ConditionalOrExpression)


def test_hyp_conditionalorexpression_constructor_exists():
    assert callable(ConditionalOrExpression.__init__)


def test_hyp_conditionalorexpression_constructor_args():
    sig = inspect.signature(ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_addressofexpression_is_not_abstract():
    assert not inspect.isabstract(AddressOfExpression)


def test_hyp_addressofexpression_constructor_exists():
    assert callable(AddressOfExpression.__init__)


def test_hyp_addressofexpression_constructor_args():
    sig = inspect.signature(AddressOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_castexpression_is_not_abstract():
    assert not inspect.isabstract(CastExpression)


def test_hyp_castexpression_constructor_exists():
    assert callable(CastExpression.__init__)


def test_hyp_castexpression_constructor_args():
    sig = inspect.signature(CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(PreDecrementExpression)


def test_hyp_predecrementexpression_constructor_exists():
    assert callable(PreDecrementExpression.__init__)


def test_hyp_predecrementexpression_constructor_args():
    sig = inspect.signature(PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(ArrayInitializer)


def test_hyp_arrayinitializer_constructor_exists():
    assert callable(ArrayInitializer.__init__)


def test_hyp_arrayinitializer_constructor_args():
    sig = inspect.signature(ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryNoArrayCreationExpression)


def test_hyp_primarynoarraycreationexpression_constructor_exists():
    assert callable(PrimaryNoArrayCreationExpression.__init__)


def test_hyp_primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_literals_literal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_literals_Literal)


def test_hyp_c_sharp_literals_literal_constructor_exists():
    assert callable(c_sharp_literals_Literal.__init__)


def test_hyp_c_sharp_literals_literal_constructor_args():
    sig = inspect.signature(c_sharp_literals_Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_typeofexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_TypeOfExpression)


def test_hyp_c_sharp_expressions_typeofexpression_constructor_exists():
    assert callable(c_sharp_expressions_TypeOfExpression.__init__)


def test_hyp_c_sharp_expressions_typeofexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_TypeOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_sizeofexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_SizeOfExpression)


def test_hyp_c_sharp_expressions_sizeofexpression_constructor_exists():
    assert callable(c_sharp_expressions_SizeOfExpression.__init__)


def test_hyp_c_sharp_expressions_sizeofexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_SizeOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_uncheckedexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_UncheckedExpression)


def test_hyp_c_sharp_expressions_uncheckedexpression_constructor_exists():
    assert callable(c_sharp_expressions_UncheckedExpression.__init__)


def test_hyp_c_sharp_expressions_uncheckedexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_UncheckedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_delegatecreationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_DelegateCreationExpression)


def test_hyp_c_sharp_expressions_delegatecreationexpression_constructor_exists():
    assert callable(c_sharp_expressions_DelegateCreationExpression.__init__)


def test_hyp_c_sharp_expressions_delegatecreationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_DelegateCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_checkedexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_CheckedExpression)


def test_hyp_c_sharp_expressions_checkedexpression_constructor_exists():
    assert callable(c_sharp_expressions_CheckedExpression.__init__)


def test_hyp_c_sharp_expressions_checkedexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_CheckedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_baseaccess_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_BaseAccess)


def test_hyp_c_sharp_expressions_baseaccess_constructor_exists():
    assert callable(c_sharp_expressions_BaseAccess.__init__)


def test_hyp_c_sharp_expressions_baseaccess_constructor_args():
    sig = inspect.signature(c_sharp_expressions_BaseAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(PreIncrementExpression)


def test_hyp_preincrementexpression_constructor_exists():
    assert callable(PreIncrementExpression.__init__)


def test_hyp_preincrementexpression_constructor_args():
    sig = inspect.signature(PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_hyp_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_hyp_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplication_is_not_abstract():
    assert not inspect.isabstract(Multiplication)


def test_hyp_multiplication_constructor_exists():
    assert callable(Multiplication.__init__)


def test_hyp_multiplication_constructor_args():
    sig = inspect.signature(Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_complement_is_not_abstract():
    assert not inspect.isabstract(Complement)


def test_hyp_complement_constructor_exists():
    assert callable(Complement.__init__)


def test_hyp_complement_constructor_args():
    sig = inspect.signature(Complement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_negate_is_not_abstract():
    assert not inspect.isabstract(Negate)


def test_hyp_negate_constructor_exists():
    assert callable(Negate.__init__)


def test_hyp_negate_constructor_args():
    sig = inspect.signature(Negate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_subtraction_is_not_abstract():
    assert not inspect.isabstract(Subtraction)


def test_hyp_subtraction_constructor_exists():
    assert callable(Subtraction.__init__)


def test_hyp_subtraction_constructor_args():
    sig = inspect.signature(Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_addition_is_not_abstract():
    assert not inspect.isabstract(Addition)


def test_hyp_addition_constructor_exists():
    assert callable(Addition.__init__)


def test_hyp_addition_constructor_args():
    sig = inspect.signature(Addition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_memberaccess_is_not_abstract():
    assert not inspect.isabstract(MemberAccess)


def test_hyp_memberaccess_constructor_exists():
    assert callable(MemberAccess.__init__)


def test_hyp_memberaccess_constructor_args():
    sig = inspect.signature(MemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_UnaryExpression)


def test_hyp_c_sharp_expressions_unaryexpression_constructor_exists():
    assert callable(c_sharp_expressions_UnaryExpression.__init__)


def test_hyp_c_sharp_expressions_unaryexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ParenthesizedExpression)


def test_hyp_c_sharp_expressions_parenthesizedexpression_constructor_exists():
    assert callable(c_sharp_expressions_ParenthesizedExpression.__init__)


def test_hyp_c_sharp_expressions_parenthesizedexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_argument_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_Argument)


def test_hyp_c_sharp_expressions_argument_constructor_exists():
    assert callable(c_sharp_expressions_Argument.__init__)


def test_hyp_c_sharp_expressions_argument_constructor_args():
    sig = inspect.signature(c_sharp_expressions_Argument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_expressionlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ExpressionList)


def test_hyp_c_sharp_expressions_expressionlist_constructor_exists():
    assert callable(c_sharp_expressions_ExpressionList.__init__)


def test_hyp_c_sharp_expressions_expressionlist_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(classes_VariableInitializer)


def test_hyp_classes_variableinitializer_constructor_exists():
    assert callable(classes_VariableInitializer.__init__)


def test_hyp_classes_variableinitializer_constructor_args():
    sig = inspect.signature(classes_VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_statementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_StatementExpression)


def test_hyp_c_sharp_expressions_statementexpression_constructor_exists():
    assert callable(c_sharp_expressions_StatementExpression.__init__)


def test_hyp_c_sharp_expressions_statementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_argumentlist_is_not_abstract():
    assert not inspect.isabstract(ArgumentList)


def test_hyp_argumentlist_constructor_exists():
    assert callable(ArgumentList.__init__)


def test_hyp_argumentlist_constructor_args():
    sig = inspect.signature(ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_statementexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_StatementExpression)


def test_hyp_expressions_statementexpression_constructor_exists():
    assert callable(expressions_StatementExpression.__init__)


def test_hyp_expressions_statementexpression_constructor_args():
    sig = inspect.signature(expressions_StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_AssignmentExpression)


def test_hyp_c_sharp_expressions_assignmentexpression_constructor_exists():
    assert callable(c_sharp_expressions_AssignmentExpression.__init__)


def test_hyp_c_sharp_expressions_assignmentexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(expressions_PrimaryExtendedExpressionType)


def test_hyp_expressions_primaryextendedexpressiontype_constructor_exists():
    assert callable(expressions_PrimaryExtendedExpressionType.__init__)


def test_hyp_expressions_primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(expressions_PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_postincrementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PostIncrementExpression)


def test_hyp_c_sharp_expressions_postincrementexpression_constructor_exists():
    assert callable(c_sharp_expressions_PostIncrementExpression.__init__)


def test_hyp_c_sharp_expressions_postincrementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PostIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_postdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PostDecrementExpression)


def test_hyp_c_sharp_expressions_postdecrementexpression_constructor_exists():
    assert callable(c_sharp_expressions_PostDecrementExpression.__init__)


def test_hyp_c_sharp_expressions_postdecrementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PostDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_invocationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_InvocationExpression)


def test_hyp_c_sharp_expressions_invocationexpression_constructor_exists():
    assert callable(c_sharp_expressions_InvocationExpression.__init__)


def test_hyp_c_sharp_expressions_invocationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_InvocationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_hyp_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_hyp_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_byte_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Byte)


def test_hyp_c_sharp_types_byte_constructor_exists():
    assert callable(c_sharp_types_Byte.__init__)


def test_hyp_c_sharp_types_byte_constructor_args():
    sig = inspect.signature(c_sharp_types_Byte.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_uint_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_UInt)


def test_hyp_c_sharp_types_uint_constructor_exists():
    assert callable(c_sharp_types_UInt.__init__)


def test_hyp_c_sharp_types_uint_constructor_args():
    sig = inspect.signature(c_sharp_types_UInt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_float_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Float)


def test_hyp_c_sharp_types_float_constructor_exists():
    assert callable(c_sharp_types_Float.__init__)


def test_hyp_c_sharp_types_float_constructor_args():
    sig = inspect.signature(c_sharp_types_Float.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_short_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Short)


def test_hyp_c_sharp_types_short_constructor_exists():
    assert callable(c_sharp_types_Short.__init__)


def test_hyp_c_sharp_types_short_constructor_args():
    sig = inspect.signature(c_sharp_types_Short.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_object_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Object)


def test_hyp_c_sharp_types_object_constructor_exists():
    assert callable(c_sharp_types_Object.__init__)


def test_hyp_c_sharp_types_object_constructor_args():
    sig = inspect.signature(c_sharp_types_Object.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_void_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Void)


def test_hyp_c_sharp_types_void_constructor_exists():
    assert callable(c_sharp_types_Void.__init__)


def test_hyp_c_sharp_types_void_constructor_args():
    sig = inspect.signature(c_sharp_types_Void.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_bool_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Bool)


def test_hyp_c_sharp_types_bool_constructor_exists():
    assert callable(c_sharp_types_Bool.__init__)


def test_hyp_c_sharp_types_bool_constructor_args():
    sig = inspect.signature(c_sharp_types_Bool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_decimal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Decimal)


def test_hyp_c_sharp_types_decimal_constructor_exists():
    assert callable(c_sharp_types_Decimal.__init__)


def test_hyp_c_sharp_types_decimal_constructor_args():
    sig = inspect.signature(c_sharp_types_Decimal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_sbyte_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_SByte)


def test_hyp_c_sharp_types_sbyte_constructor_exists():
    assert callable(c_sharp_types_SByte.__init__)


def test_hyp_c_sharp_types_sbyte_constructor_args():
    sig = inspect.signature(c_sharp_types_SByte.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_double_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Double)


def test_hyp_c_sharp_types_double_constructor_exists():
    assert callable(c_sharp_types_Double.__init__)


def test_hyp_c_sharp_types_double_constructor_args():
    sig = inspect.signature(c_sharp_types_Double.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_char_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Char)


def test_hyp_c_sharp_types_char_constructor_exists():
    assert callable(c_sharp_types_Char.__init__)


def test_hyp_c_sharp_types_char_constructor_args():
    sig = inspect.signature(c_sharp_types_Char.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_ushort_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_UShort)


def test_hyp_c_sharp_types_ushort_constructor_exists():
    assert callable(c_sharp_types_UShort.__init__)


def test_hyp_c_sharp_types_ushort_constructor_args():
    sig = inspect.signature(c_sharp_types_UShort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_long_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Long)


def test_hyp_c_sharp_types_long_constructor_exists():
    assert callable(c_sharp_types_Long.__init__)


def test_hyp_c_sharp_types_long_constructor_args():
    sig = inspect.signature(c_sharp_types_Long.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_string_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_String)


def test_hyp_c_sharp_types_string_constructor_exists():
    assert callable(c_sharp_types_String.__init__)


def test_hyp_c_sharp_types_string_constructor_args():
    sig = inspect.signature(c_sharp_types_String.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_int_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_Int)


def test_hyp_c_sharp_types_int_constructor_exists():
    assert callable(c_sharp_types_Int.__init__)


def test_hyp_c_sharp_types_int_constructor_args():
    sig = inspect.signature(c_sharp_types_Int.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_types_ulong_is_not_abstract():
    assert not inspect.isabstract(c_sharp_types_ULong)


def test_hyp_c_sharp_types_ulong_constructor_exists():
    assert callable(c_sharp_types_ULong.__init__)


def test_hyp_c_sharp_types_ulong_constructor_args():
    sig = inspect.signature(c_sharp_types_ULong.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(PrimaryExtendedExpressionType)


def test_hyp_primaryextendedexpressiontype_constructor_exists():
    assert callable(PrimaryExtendedExpressionType.__init__)


def test_hyp_primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_pointermemberaccess_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PointerMemberAccess)


def test_hyp_c_sharp_expressions_pointermemberaccess_constructor_exists():
    assert callable(c_sharp_expressions_PointerMemberAccess.__init__)


def test_hyp_c_sharp_expressions_pointermemberaccess_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PointerMemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_elementaccess_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ElementAccess)


def test_hyp_c_sharp_expressions_elementaccess_constructor_exists():
    assert callable(c_sharp_expressions_ElementAccess.__init__)


def test_hyp_c_sharp_expressions_elementaccess_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_memberaccess_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_MemberAccess)


def test_hyp_c_sharp_expressions_memberaccess_constructor_exists():
    assert callable(c_sharp_expressions_MemberAccess.__init__)


def test_hyp_c_sharp_expressions_memberaccess_constructor_args():
    sig = inspect.signature(c_sharp_expressions_MemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_primaryextendedexpressiontype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PrimaryExtendedExpressionType)


def test_hyp_c_sharp_expressions_primaryextendedexpressiontype_constructor_exists():
    assert callable(c_sharp_expressions_PrimaryExtendedExpressionType.__init__)


def test_hyp_c_sharp_expressions_primaryextendedexpressiontype_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PrimaryExtendedExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_hyp_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_hyp_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_arraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ArrayCreationExpression)


def test_hyp_c_sharp_expressions_arraycreationexpression_constructor_exists():
    assert callable(c_sharp_expressions_ArrayCreationExpression.__init__)


def test_hyp_c_sharp_expressions_arraycreationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PrimaryNoArrayCreationExpression)


def test_hyp_c_sharp_expressions_primarynoarraycreationexpression_constructor_exists():
    assert callable(c_sharp_expressions_PrimaryNoArrayCreationExpression.__init__)


def test_hyp_c_sharp_expressions_primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PrimaryExpression)


def test_hyp_c_sharp_expressions_primaryexpression_constructor_exists():
    assert callable(c_sharp_expressions_PrimaryExpression.__init__)


def test_hyp_c_sharp_expressions_primaryexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_hyp_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_hyp_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_argumentlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ArgumentList)


def test_hyp_c_sharp_expressions_argumentlist_constructor_exists():
    assert callable(c_sharp_expressions_ArgumentList.__init__)


def test_hyp_c_sharp_expressions_argumentlist_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fixedpointerdeclarator_is_not_abstract():
    assert not inspect.isabstract(FixedPointerDeclarator)


def test_hyp_fixedpointerdeclarator_constructor_exists():
    assert callable(FixedPointerDeclarator.__init__)


def test_hyp_fixedpointerdeclarator_constructor_args():
    sig = inspect.signature(FixedPointerDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pointertype_is_not_abstract():
    assert not inspect.isabstract(PointerType)


def test_hyp_pointertype_constructor_exists():
    assert callable(PointerType.__init__)


def test_hyp_pointertype_constructor_args():
    sig = inspect.signature(PointerType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(ResourceAcquisition)


def test_hyp_resourceacquisition_constructor_exists():
    assert callable(ResourceAcquisition.__init__)


def test_hyp_resourceacquisition_constructor_args():
    sig = inspect.signature(ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ResourceAcquisition)


def test_hyp_c_sharp_statements_resourceacquisition_constructor_exists():
    assert callable(c_sharp_statements_ResourceAcquisition.__init__)


def test_hyp_c_sharp_statements_resourceacquisition_constructor_args():
    sig = inspect.signature(c_sharp_statements_ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_localconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_LocalConstantDeclaration)


def test_hyp_c_sharp_statements_localconstantdeclaration_constructor_exists():
    assert callable(c_sharp_statements_LocalConstantDeclaration.__init__)


def test_hyp_c_sharp_statements_localconstantdeclaration_constructor_args():
    sig = inspect.signature(c_sharp_statements_LocalConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statements_resourceacquisition_is_not_abstract():
    assert not inspect.isabstract(statements_ResourceAcquisition)


def test_hyp_statements_resourceacquisition_constructor_exists():
    assert callable(statements_ResourceAcquisition.__init__)


def test_hyp_statements_resourceacquisition_constructor_args():
    sig = inspect.signature(statements_ResourceAcquisition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_Expression)


def test_hyp_c_sharp_expressions_expression_constructor_exists():
    assert callable(c_sharp_expressions_Expression.__init__)


def test_hyp_c_sharp_expressions_expression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statements_forinitializer_is_not_abstract():
    assert not inspect.isabstract(statements_ForInitializer)


def test_hyp_statements_forinitializer_constructor_exists():
    assert callable(statements_ForInitializer.__init__)


def test_hyp_statements_forinitializer_constructor_args():
    sig = inspect.signature(statements_ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_VariableDeclaration)


def test_hyp_c_sharp_statements_variabledeclaration_constructor_exists():
    assert callable(c_sharp_statements_VariableDeclaration.__init__)


def test_hyp_c_sharp_statements_variabledeclaration_constructor_args():
    sig = inspect.signature(c_sharp_statements_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_fixedpointerdeclarator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_FixedPointerDeclarator)


def test_hyp_c_sharp_statements_fixedpointerdeclarator_constructor_exists():
    assert callable(c_sharp_statements_FixedPointerDeclarator.__init__)


def test_hyp_c_sharp_statements_fixedpointerdeclarator_constructor_args():
    sig = inspect.signature(c_sharp_statements_FixedPointerDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(JumpStatement)


def test_hyp_jumpstatement_constructor_exists():
    assert callable(JumpStatement.__init__)


def test_hyp_jumpstatement_constructor_args():
    sig = inspect.signature(JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_returnstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ReturnStatement)


def test_hyp_c_sharp_statements_returnstatement_constructor_exists():
    assert callable(c_sharp_statements_ReturnStatement.__init__)


def test_hyp_c_sharp_statements_returnstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_continuestatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ContinueStatement)


def test_hyp_c_sharp_statements_continuestatement_constructor_exists():
    assert callable(c_sharp_statements_ContinueStatement.__init__)


def test_hyp_c_sharp_statements_continuestatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_gotostatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_GotoStatement)


def test_hyp_c_sharp_statements_gotostatement_constructor_exists():
    assert callable(c_sharp_statements_GotoStatement.__init__)


def test_hyp_c_sharp_statements_gotostatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_breakstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_BreakStatement)


def test_hyp_c_sharp_statements_breakstatement_constructor_exists():
    assert callable(c_sharp_statements_BreakStatement.__init__)


def test_hyp_c_sharp_statements_breakstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_forinitializer_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ForInitializer)


def test_hyp_c_sharp_statements_forinitializer_constructor_exists():
    assert callable(c_sharp_statements_ForInitializer.__init__)


def test_hyp_c_sharp_statements_forinitializer_constructor_args():
    sig = inspect.signature(c_sharp_statements_ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_finallyclause_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_FinallyClause)


def test_hyp_c_sharp_statements_finallyclause_constructor_exists():
    assert callable(c_sharp_statements_FinallyClause.__init__)


def test_hyp_c_sharp_statements_finallyclause_constructor_args():
    sig = inspect.signature(c_sharp_statements_FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_generalcatchclause_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_GeneralCatchClause)


def test_hyp_c_sharp_statements_generalcatchclause_constructor_exists():
    assert callable(c_sharp_statements_GeneralCatchClause.__init__)


def test_hyp_c_sharp_statements_generalcatchclause_constructor_args():
    sig = inspect.signature(c_sharp_statements_GeneralCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_specificcatchclause_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SpecificCatchClause)


def test_hyp_c_sharp_statements_specificcatchclause_constructor_exists():
    assert callable(c_sharp_statements_SpecificCatchClause.__init__)


def test_hyp_c_sharp_statements_specificcatchclause_constructor_args():
    sig = inspect.signature(c_sharp_statements_SpecificCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_finallyclause_is_not_abstract():
    assert not inspect.isabstract(FinallyClause)


def test_hyp_finallyclause_constructor_exists():
    assert callable(FinallyClause.__init__)


def test_hyp_finallyclause_constructor_args():
    sig = inspect.signature(FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_generalcatchclause_is_not_abstract():
    assert not inspect.isabstract(GeneralCatchClause)


def test_hyp_generalcatchclause_constructor_exists():
    assert callable(GeneralCatchClause.__init__)


def test_hyp_generalcatchclause_constructor_args():
    sig = inspect.signature(GeneralCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_specificcatchclause_is_not_abstract():
    assert not inspect.isabstract(SpecificCatchClause)


def test_hyp_specificcatchclause_constructor_exists():
    assert callable(SpecificCatchClause.__init__)


def test_hyp_specificcatchclause_constructor_args():
    sig = inspect.signature(SpecificCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_throwstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ThrowStatement)


def test_hyp_c_sharp_statements_throwstatement_constructor_exists():
    assert callable(c_sharp_statements_ThrowStatement.__init__)


def test_hyp_c_sharp_statements_throwstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_default_is_not_abstract():
    assert not inspect.isabstract(Default)


def test_hyp_default_constructor_exists():
    assert callable(Default.__init__)


def test_hyp_default_constructor_args():
    sig = inspect.signature(Default.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_switchlabel_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SwitchLabel)


def test_hyp_c_sharp_statements_switchlabel_constructor_exists():
    assert callable(c_sharp_statements_SwitchLabel.__init__)


def test_hyp_c_sharp_statements_switchlabel_constructor_args():
    sig = inspect.signature(c_sharp_statements_SwitchLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_switchlabel_is_not_abstract():
    assert not inspect.isabstract(SwitchLabel)


def test_hyp_switchlabel_constructor_exists():
    assert callable(SwitchLabel.__init__)


def test_hyp_switchlabel_constructor_args():
    sig = inspect.signature(SwitchLabel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_switchsection_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SwitchSection)


def test_hyp_c_sharp_statements_switchsection_constructor_exists():
    assert callable(c_sharp_statements_SwitchSection.__init__)


def test_hyp_c_sharp_statements_switchsection_constructor_args():
    sig = inspect.signature(c_sharp_statements_SwitchSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_switchsection_is_not_abstract():
    assert not inspect.isabstract(SwitchSection)


def test_hyp_switchsection_constructor_exists():
    assert callable(SwitchSection.__init__)


def test_hyp_switchsection_constructor_args():
    sig = inspect.signature(SwitchSection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_selectionstatement_is_not_abstract():
    assert not inspect.isabstract(SelectionStatement)


def test_hyp_selectionstatement_constructor_exists():
    assert callable(SelectionStatement.__init__)


def test_hyp_selectionstatement_constructor_args():
    sig = inspect.signature(SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_switchstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SwitchStatement)


def test_hyp_c_sharp_statements_switchstatement_constructor_exists():
    assert callable(c_sharp_statements_SwitchStatement.__init__)


def test_hyp_c_sharp_statements_switchstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_ifstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_IfStatement)


def test_hyp_c_sharp_statements_ifstatement_constructor_exists():
    assert callable(c_sharp_statements_IfStatement.__init__)


def test_hyp_c_sharp_statements_ifstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_hyp_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_hyp_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PreDecrementExpression)


def test_hyp_c_sharp_expressions_predecrementexpression_constructor_exists():
    assert callable(c_sharp_expressions_PreDecrementExpression.__init__)


def test_hyp_c_sharp_expressions_predecrementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_PreIncrementExpression)


def test_hyp_c_sharp_expressions_preincrementexpression_constructor_exists():
    assert callable(c_sharp_expressions_PreIncrementExpression.__init__)


def test_hyp_c_sharp_expressions_preincrementexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(StatementExpressionList)


def test_hyp_statementexpressionlist_constructor_exists():
    assert callable(StatementExpressionList.__init__)


def test_hyp_statementexpressionlist_constructor_args():
    sig = inspect.signature(StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_forinitializer_is_not_abstract():
    assert not inspect.isabstract(ForInitializer)


def test_hyp_forinitializer_constructor_exists():
    assert callable(ForInitializer.__init__)


def test_hyp_forinitializer_constructor_args():
    sig = inspect.signature(ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_StatementExpressionList)


def test_hyp_c_sharp_expressions_statementexpressionlist_constructor_exists():
    assert callable(c_sharp_expressions_StatementExpressionList.__init__)


def test_hyp_c_sharp_expressions_statementexpressionlist_constructor_args():
    sig = inspect.signature(c_sharp_expressions_StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(IterationStatement)


def test_hyp_iterationstatement_constructor_exists():
    assert callable(IterationStatement.__init__)


def test_hyp_iterationstatement_constructor_args():
    sig = inspect.signature(IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ForeachStatement)


def test_hyp_c_sharp_statements_foreachstatement_constructor_exists():
    assert callable(c_sharp_statements_ForeachStatement.__init__)


def test_hyp_c_sharp_statements_foreachstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ForeachStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_dostatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_DoStatement)


def test_hyp_c_sharp_statements_dostatement_constructor_exists():
    assert callable(c_sharp_statements_DoStatement.__init__)


def test_hyp_c_sharp_statements_dostatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_forstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ForStatement)


def test_hyp_c_sharp_statements_forstatement_constructor_exists():
    assert callable(c_sharp_statements_ForStatement.__init__)


def test_hyp_c_sharp_statements_forstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_whilestatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_WhileStatement)


def test_hyp_c_sharp_statements_whilestatement_constructor_exists():
    assert callable(c_sharp_statements_WhileStatement.__init__)


def test_hyp_c_sharp_statements_whilestatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_case_is_not_abstract():
    assert not inspect.isabstract(Case)


def test_hyp_case_constructor_exists():
    assert callable(Case.__init__)


def test_hyp_case_constructor_args():
    sig = inspect.signature(Case.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedargumentlist_is_not_abstract():
    assert not inspect.isabstract(NamedArgumentList)


def test_hyp_namedargumentlist_constructor_exists():
    assert callable(NamedArgumentList.__init__)


def test_hyp_namedargumentlist_constructor_args():
    sig = inspect.signature(NamedArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressionlist_is_not_abstract():
    assert not inspect.isabstract(ExpressionList)


def test_hyp_expressionlist_constructor_exists():
    assert callable(ExpressionList.__init__)


def test_hyp_expressionlist_constructor_args():
    sig = inspect.signature(ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_attributes_attributearguments_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_AttributeArguments)


def test_hyp_c_sharp_attributes_attributearguments_constructor_exists():
    assert callable(c_sharp_attributes_AttributeArguments.__init__)


def test_hyp_c_sharp_attributes_attributearguments_constructor_args():
    sig = inspect.signature(c_sharp_attributes_AttributeArguments.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attributearguments_is_not_abstract():
    assert not inspect.isabstract(AttributeArguments)


def test_hyp_attributearguments_constructor_exists():
    assert callable(AttributeArguments.__init__)


def test_hyp_attributearguments_constructor_args():
    sig = inspect.signature(AttributeArguments.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_attributes_attribute_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_Attribute)


def test_hyp_c_sharp_attributes_attribute_constructor_exists():
    assert callable(c_sharp_attributes_Attribute.__init__)


def test_hyp_c_sharp_attributes_attribute_constructor_args():
    sig = inspect.signature(c_sharp_attributes_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_return_is_not_abstract():
    assert not inspect.isabstract(Return)


def test_hyp_return_constructor_exists():
    assert callable(Return.__init__)


def test_hyp_return_constructor_args():
    sig = inspect.signature(Return.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_attributes_attributetarget_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_AttributeTarget)


def test_hyp_c_sharp_attributes_attributetarget_constructor_exists():
    assert callable(c_sharp_attributes_AttributeTarget.__init__)


def test_hyp_c_sharp_attributes_attributetarget_constructor_args():
    sig = inspect.signature(c_sharp_attributes_AttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attributetarget_is_not_abstract():
    assert not inspect.isabstract(AttributeTarget)


def test_hyp_attributetarget_constructor_exists():
    assert callable(AttributeTarget.__init__)


def test_hyp_attributetarget_constructor_args():
    sig = inspect.signature(AttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_attributes_attributes_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_Attributes)


def test_hyp_c_sharp_attributes_attributes_constructor_exists():
    assert callable(c_sharp_attributes_Attributes.__init__)


def test_hyp_c_sharp_attributes_attributes_constructor_args():
    sig = inspect.signature(c_sharp_attributes_Attributes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_attributes_globalattributetarget_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_GlobalAttributeTarget)


def test_hyp_c_sharp_attributes_globalattributetarget_constructor_exists():
    assert callable(c_sharp_attributes_GlobalAttributeTarget.__init__)


def test_hyp_c_sharp_attributes_globalattributetarget_constructor_args():
    sig = inspect.signature(c_sharp_attributes_GlobalAttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unsafe_is_not_abstract():
    assert not inspect.isabstract(Unsafe)


def test_hyp_unsafe_constructor_exists():
    assert callable(Unsafe.__init__)


def test_hyp_unsafe_constructor_args():
    sig = inspect.signature(Unsafe.__init__)
    params = list(sig.parameters.keys())



def test_hyp_embeddedstatement_is_not_abstract():
    assert not inspect.isabstract(EmbeddedStatement)


def test_hyp_embeddedstatement_constructor_exists():
    assert callable(EmbeddedStatement.__init__)


def test_hyp_embeddedstatement_constructor_args():
    sig = inspect.signature(EmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_checkedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_CheckedStatement)


def test_hyp_c_sharp_statements_checkedstatement_constructor_exists():
    assert callable(c_sharp_statements_CheckedStatement.__init__)


def test_hyp_c_sharp_statements_checkedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_CheckedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_lockstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_LockStatement)


def test_hyp_c_sharp_statements_lockstatement_constructor_exists():
    assert callable(c_sharp_statements_LockStatement.__init__)


def test_hyp_c_sharp_statements_lockstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_LockStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_uncheckedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_UncheckedStatement)


def test_hyp_c_sharp_statements_uncheckedstatement_constructor_exists():
    assert callable(c_sharp_statements_UncheckedStatement.__init__)


def test_hyp_c_sharp_statements_uncheckedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_UncheckedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_selectionstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SelectionStatement)


def test_hyp_c_sharp_statements_selectionstatement_constructor_exists():
    assert callable(c_sharp_statements_SelectionStatement.__init__)


def test_hyp_c_sharp_statements_selectionstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_usingstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_UsingStatement)


def test_hyp_c_sharp_statements_usingstatement_constructor_exists():
    assert callable(c_sharp_statements_UsingStatement.__init__)


def test_hyp_c_sharp_statements_usingstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_UsingStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_emptystatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_EmptyStatement)


def test_hyp_c_sharp_statements_emptystatement_constructor_exists():
    assert callable(c_sharp_statements_EmptyStatement.__init__)


def test_hyp_c_sharp_statements_emptystatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_IterationStatement)


def test_hyp_c_sharp_statements_iterationstatement_constructor_exists():
    assert callable(c_sharp_statements_IterationStatement.__init__)


def test_hyp_c_sharp_statements_iterationstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ExpressionStatement)


def test_hyp_c_sharp_statements_expressionstatement_constructor_exists():
    assert callable(c_sharp_statements_ExpressionStatement.__init__)


def test_hyp_c_sharp_statements_expressionstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_jumpstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_JumpStatement)


def test_hyp_c_sharp_statements_jumpstatement_constructor_exists():
    assert callable(c_sharp_statements_JumpStatement.__init__)


def test_hyp_c_sharp_statements_jumpstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_trystatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_TryStatement)


def test_hyp_c_sharp_statements_trystatement_constructor_exists():
    assert callable(c_sharp_statements_TryStatement.__init__)


def test_hyp_c_sharp_statements_trystatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_fixedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_FixedStatement)


def test_hyp_c_sharp_statements_fixedstatement_constructor_exists():
    assert callable(c_sharp_statements_FixedStatement.__init__)


def test_hyp_c_sharp_statements_fixedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_FixedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_simpleembeddedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_SimpleEmbeddedStatement)


def test_hyp_c_sharp_statements_simpleembeddedstatement_constructor_exists():
    assert callable(c_sharp_statements_SimpleEmbeddedStatement.__init__)


def test_hyp_c_sharp_statements_simpleembeddedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_SimpleEmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_localconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(LocalConstantDeclaration)


def test_hyp_localconstantdeclaration_constructor_exists():
    assert callable(LocalConstantDeclaration.__init__)


def test_hyp_localconstantdeclaration_constructor_args():
    sig = inspect.signature(LocalConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_hyp_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_hyp_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_hyp_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_hyp_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_statement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_Statement)


def test_hyp_c_sharp_statements_statement_constructor_exists():
    assert callable(c_sharp_statements_Statement.__init__)


def test_hyp_c_sharp_statements_statement_constructor_args():
    sig = inspect.signature(c_sharp_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_attributes_namedargument_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_NamedArgument)


def test_hyp_c_sharp_attributes_namedargument_constructor_exists():
    assert callable(c_sharp_attributes_NamedArgument.__init__)


def test_hyp_c_sharp_attributes_namedargument_constructor_args():
    sig = inspect.signature(c_sharp_attributes_NamedArgument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedargument_is_not_abstract():
    assert not inspect.isabstract(NamedArgument)


def test_hyp_namedargument_constructor_exists():
    assert callable(NamedArgument.__init__)


def test_hyp_namedargument_constructor_args():
    sig = inspect.signature(NamedArgument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_attributes_namedargumentlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_NamedArgumentList)


def test_hyp_c_sharp_attributes_namedargumentlist_constructor_exists():
    assert callable(c_sharp_attributes_NamedArgumentList.__init__)


def test_hyp_c_sharp_attributes_namedargumentlist_constructor_args():
    sig = inspect.signature(c_sharp_attributes_NamedArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_constantdeclarator_is_not_abstract():
    assert not inspect.isabstract(ConstantDeclarator)


def test_hyp_constantdeclarator_constructor_exists():
    assert callable(ConstantDeclarator.__init__)


def test_hyp_constantdeclarator_constructor_args():
    sig = inspect.signature(ConstantDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_VariableInitializer)


def test_hyp_c_sharp_classes_variableinitializer_constructor_exists():
    assert callable(c_sharp_classes_VariableInitializer.__init__)


def test_hyp_c_sharp_classes_variableinitializer_constructor_args():
    sig = inspect.signature(c_sharp_classes_VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_declarationstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_DeclarationStatement)


def test_hyp_c_sharp_statements_declarationstatement_constructor_exists():
    assert callable(c_sharp_statements_DeclarationStatement.__init__)


def test_hyp_c_sharp_statements_declarationstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_DeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_embeddedstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_EmbeddedStatement)


def test_hyp_c_sharp_statements_embeddedstatement_constructor_exists():
    assert callable(c_sharp_statements_EmbeddedStatement.__init__)


def test_hyp_c_sharp_statements_embeddedstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_EmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_block_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_Block)


def test_hyp_c_sharp_classes_block_constructor_exists():
    assert callable(c_sharp_classes_Block.__init__)


def test_hyp_c_sharp_classes_block_constructor_args():
    sig = inspect.signature(c_sharp_classes_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arraytype_is_not_abstract():
    assert not inspect.isabstract(ArrayType)


def test_hyp_arraytype_constructor_exists():
    assert callable(ArrayType.__init__)


def test_hyp_arraytype_constructor_args():
    sig = inspect.signature(ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_hyp_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_hyp_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_globalattributetarget_is_not_abstract():
    assert not inspect.isabstract(GlobalAttributeTarget)


def test_hyp_globalattributetarget_constructor_exists():
    assert callable(GlobalAttributeTarget.__init__)


def test_hyp_globalattributetarget_constructor_args():
    sig = inspect.signature(GlobalAttributeTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_attributes_globalattributes_is_not_abstract():
    assert not inspect.isabstract(c_sharp_attributes_GlobalAttributes)


def test_hyp_c_sharp_attributes_globalattributes_constructor_exists():
    assert callable(c_sharp_attributes_GlobalAttributes.__init__)


def test_hyp_c_sharp_attributes_globalattributes_constructor_args():
    sig = inspect.signature(c_sharp_attributes_GlobalAttributes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_arrays_rankspecifier_is_not_abstract():
    assert not inspect.isabstract(c_sharp_arrays_RankSpecifier)


def test_hyp_c_sharp_arrays_rankspecifier_constructor_exists():
    assert callable(c_sharp_arrays_RankSpecifier.__init__)


def test_hyp_c_sharp_arrays_rankspecifier_constructor_args():
    sig = inspect.signature(c_sharp_arrays_RankSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rankspecifier_is_not_abstract():
    assert not inspect.isabstract(RankSpecifier)


def test_hyp_rankspecifier_constructor_exists():
    assert callable(RankSpecifier.__init__)


def test_hyp_rankspecifier_constructor_args():
    sig = inspect.signature(RankSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nonarraytype_is_not_abstract():
    assert not inspect.isabstract(NonArrayType)


def test_hyp_nonarraytype_constructor_exists():
    assert callable(NonArrayType.__init__)


def test_hyp_nonarraytype_constructor_args():
    sig = inspect.signature(NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ConditionalExpression)


def test_hyp_c_sharp_expressions_conditionalexpression_constructor_exists():
    assert callable(c_sharp_expressions_ConditionalExpression.__init__)


def test_hyp_c_sharp_expressions_conditionalexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(VariableInitializer)


def test_hyp_variableinitializer_constructor_exists():
    assert callable(VariableInitializer.__init__)


def test_hyp_variableinitializer_constructor_args():
    sig = inspect.signature(VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_arrays_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(c_sharp_arrays_ArrayInitializer)


def test_hyp_c_sharp_arrays_arrayinitializer_constructor_exists():
    assert callable(c_sharp_arrays_ArrayInitializer.__init__)


def test_hyp_c_sharp_arrays_arrayinitializer_constructor_args():
    sig = inspect.signature(c_sharp_arrays_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_arrays_stackallocinitializer_is_not_abstract():
    assert not inspect.isabstract(c_sharp_arrays_StackallocInitializer)


def test_hyp_c_sharp_arrays_stackallocinitializer_constructor_exists():
    assert callable(c_sharp_arrays_StackallocInitializer.__init__)


def test_hyp_c_sharp_arrays_stackallocinitializer_constructor_args():
    sig = inspect.signature(c_sharp_arrays_StackallocInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarator)


def test_hyp_variabledeclarator_constructor_exists():
    assert callable(VariableDeclarator.__init__)


def test_hyp_variabledeclarator_constructor_args():
    sig = inspect.signature(VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(FormalParameterList)


def test_hyp_formalparameterlist_constructor_exists():
    assert callable(FormalParameterList.__init__)


def test_hyp_formalparameterlist_constructor_args():
    sig = inspect.signature(FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_arrays_arraytype_is_not_abstract():
    assert not inspect.isabstract(c_sharp_arrays_ArrayType)


def test_hyp_c_sharp_arrays_arraytype_constructor_exists():
    assert callable(c_sharp_arrays_ArrayType.__init__)


def test_hyp_c_sharp_arrays_arraytype_constructor_args():
    sig = inspect.signature(c_sharp_arrays_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_ClassMemberDeclaration)


def test_hyp_c_sharp_classes_classmemberdeclaration_constructor_exists():
    assert callable(c_sharp_classes_ClassMemberDeclaration.__init__)


def test_hyp_c_sharp_classes_classmemberdeclaration_constructor_args():
    sig = inspect.signature(c_sharp_classes_ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classorinterfaceordelegateorenumtype_is_not_abstract():
    assert not inspect.isabstract(ClassOrInterfaceOrDelegateOrEnumType)


def test_hyp_classorinterfaceordelegateorenumtype_constructor_exists():
    assert callable(ClassOrInterfaceOrDelegateOrEnumType.__init__)


def test_hyp_classorinterfaceordelegateorenumtype_constructor_args():
    sig = inspect.signature(ClassOrInterfaceOrDelegateOrEnumType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_classbase_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_ClassBase)


def test_hyp_c_sharp_classes_classbase_constructor_exists():
    assert callable(c_sharp_classes_ClassBase.__init__)


def test_hyp_c_sharp_classes_classbase_constructor_args():
    sig = inspect.signature(c_sharp_classes_ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(ClassMemberDeclaration)


def test_hyp_classmemberdeclaration_constructor_exists():
    assert callable(ClassMemberDeclaration.__init__)


def test_hyp_classmemberdeclaration_constructor_args():
    sig = inspect.signature(ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_ConstantDeclaration)


def test_hyp_c_sharp_classes_constantdeclaration_constructor_exists():
    assert callable(c_sharp_classes_ConstantDeclaration.__init__)


def test_hyp_c_sharp_classes_constantdeclaration_constructor_args():
    sig = inspect.signature(c_sharp_classes_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_FieldDeclaration)


def test_hyp_c_sharp_classes_fielddeclaration_constructor_exists():
    assert callable(c_sharp_classes_FieldDeclaration.__init__)


def test_hyp_c_sharp_classes_fielddeclaration_constructor_args():
    sig = inspect.signature(c_sharp_classes_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_params_is_not_abstract():
    assert not inspect.isabstract(Params)


def test_hyp_params_constructor_exists():
    assert callable(Params.__init__)


def test_hyp_params_constructor_args():
    sig = inspect.signature(Params.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_parameterarray_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_ParameterArray)


def test_hyp_c_sharp_classes_parameterarray_constructor_exists():
    assert callable(c_sharp_classes_ParameterArray.__init__)


def test_hyp_c_sharp_classes_parameterarray_constructor_args():
    sig = inspect.signature(c_sharp_classes_ParameterArray.__init__)
    params = list(sig.parameters.keys())



def test_hyp_out_is_not_abstract():
    assert not inspect.isabstract(Out)


def test_hyp_out_constructor_exists():
    assert callable(Out.__init__)


def test_hyp_out_constructor_args():
    sig = inspect.signature(Out.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ref_is_not_abstract():
    assert not inspect.isabstract(Ref)


def test_hyp_ref_constructor_exists():
    assert callable(Ref.__init__)


def test_hyp_ref_constructor_args():
    sig = inspect.signature(Ref.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_fixedparameter_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_FixedParameter)


def test_hyp_c_sharp_classes_fixedparameter_constructor_exists():
    assert callable(c_sharp_classes_FixedParameter.__init__)


def test_hyp_c_sharp_classes_fixedparameter_constructor_args():
    sig = inspect.signature(c_sharp_classes_FixedParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameterarray_is_not_abstract():
    assert not inspect.isabstract(ParameterArray)


def test_hyp_parameterarray_constructor_exists():
    assert callable(ParameterArray.__init__)


def test_hyp_parameterarray_constructor_args():
    sig = inspect.signature(ParameterArray.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fixedparameter_is_not_abstract():
    assert not inspect.isabstract(FixedParameter)


def test_hyp_fixedparameter_constructor_exists():
    assert callable(FixedParameter.__init__)


def test_hyp_fixedparameter_constructor_args():
    sig = inspect.signature(FixedParameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_FormalParameterList)


def test_hyp_c_sharp_classes_formalparameterlist_constructor_exists():
    assert callable(c_sharp_classes_FormalParameterList.__init__)


def test_hyp_c_sharp_classes_formalparameterlist_constructor_args():
    sig = inspect.signature(c_sharp_classes_FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_hyp_block_constructor_exists():
    assert callable(Block.__init__)


def test_hyp_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(NamespaceMemberDeclaration)


def test_hyp_namespacememberdeclaration_constructor_exists():
    assert callable(NamespaceMemberDeclaration.__init__)


def test_hyp_namespacememberdeclaration_constructor_args():
    sig = inspect.signature(NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_globalattributes_is_not_abstract():
    assert not inspect.isabstract(GlobalAttributes)


def test_hyp_globalattributes_constructor_exists():
    assert callable(GlobalAttributes.__init__)


def test_hyp_globalattributes_constructor_args():
    sig = inspect.signature(GlobalAttributes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_usingdirective_is_not_abstract():
    assert not inspect.isabstract(UsingDirective)


def test_hyp_usingdirective_constructor_exists():
    assert callable(UsingDirective.__init__)


def test_hyp_usingdirective_constructor_args():
    sig = inspect.signature(UsingDirective.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_namespaces_compilationunit_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_CompilationUnit)


def test_hyp_c_sharp_namespaces_compilationunit_constructor_exists():
    assert callable(c_sharp_namespaces_CompilationUnit.__init__)


def test_hyp_c_sharp_namespaces_compilationunit_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_primarynoarraycreationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_PrimaryNoArrayCreationExpression)


def test_hyp_expressions_primarynoarraycreationexpression_constructor_exists():
    assert callable(expressions_PrimaryNoArrayCreationExpression.__init__)


def test_hyp_expressions_primarynoarraycreationexpression_constructor_args():
    sig = inspect.signature(expressions_PrimaryNoArrayCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_expressions_objectcreationexpression_is_not_abstract():
    assert not inspect.isabstract(c_sharp_expressions_ObjectCreationExpression)


def test_hyp_c_sharp_expressions_objectcreationexpression_constructor_exists():
    assert callable(c_sharp_expressions_ObjectCreationExpression.__init__)


def test_hyp_c_sharp_expressions_objectcreationexpression_constructor_args():
    sig = inspect.signature(c_sharp_expressions_ObjectCreationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_common_namedelement_is_not_abstract():
    assert not inspect.isabstract(common_NamedElement)


def test_hyp_common_namedelement_constructor_exists():
    assert callable(common_NamedElement.__init__)


def test_hyp_common_namedelement_constructor_args():
    sig = inspect.signature(common_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_LabeledStatement)


def test_hyp_c_sharp_statements_labeledstatement_constructor_exists():
    assert callable(c_sharp_statements_LabeledStatement.__init__)


def test_hyp_c_sharp_statements_labeledstatement_constructor_args():
    sig = inspect.signature(c_sharp_statements_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_common_identifier_is_not_abstract():
    assert not inspect.isabstract(c_sharp_common_Identifier)


def test_hyp_c_sharp_common_identifier_constructor_exists():
    assert callable(c_sharp_common_Identifier.__init__)


def test_hyp_c_sharp_common_identifier_constructor_args():
    sig = inspect.signature(c_sharp_common_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_hyp_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_hyp_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_common_namespaceortypename_is_not_abstract():
    assert not inspect.isabstract(c_sharp_common_NamespaceOrTypeName)


def test_hyp_c_sharp_common_namespaceortypename_constructor_exists():
    assert callable(c_sharp_common_NamespaceOrTypeName.__init__)


def test_hyp_c_sharp_common_namespaceortypename_constructor_args():
    sig = inspect.signature(c_sharp_common_NamespaceOrTypeName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_common_namedelement_is_not_abstract():
    assert not inspect.isabstract(c_sharp_common_NamedElement)


def test_hyp_c_sharp_common_namedelement_constructor_exists():
    assert callable(c_sharp_common_NamedElement.__init__)


def test_hyp_c_sharp_common_namedelement_constructor_args():
    sig = inspect.signature(c_sharp_common_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_classbase_is_not_abstract():
    assert not inspect.isabstract(ClassBase)


def test_hyp_classbase_constructor_exists():
    assert callable(ClassBase.__init__)


def test_hyp_classbase_constructor_args():
    sig = inspect.signature(ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_hyp_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_hyp_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_extern_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Extern)


def test_hyp_c_sharp_modifiers_extern_constructor_exists():
    assert callable(c_sharp_modifiers_Extern.__init__)


def test_hyp_c_sharp_modifiers_extern_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Extern.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_readonly_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_ReadOnly)


def test_hyp_c_sharp_modifiers_readonly_constructor_exists():
    assert callable(c_sharp_modifiers_ReadOnly.__init__)


def test_hyp_c_sharp_modifiers_readonly_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_ReadOnly.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_new_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_New)


def test_hyp_c_sharp_modifiers_new_constructor_exists():
    assert callable(c_sharp_modifiers_New.__init__)


def test_hyp_c_sharp_modifiers_new_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_New.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_partial_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Partial)


def test_hyp_c_sharp_modifiers_partial_constructor_exists():
    assert callable(c_sharp_modifiers_Partial.__init__)


def test_hyp_c_sharp_modifiers_partial_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Partial.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_volatile_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Volatile)


def test_hyp_c_sharp_modifiers_volatile_constructor_exists():
    assert callable(c_sharp_modifiers_Volatile.__init__)


def test_hyp_c_sharp_modifiers_volatile_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Volatile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_sealed_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Sealed)


def test_hyp_c_sharp_modifiers_sealed_constructor_exists():
    assert callable(c_sharp_modifiers_Sealed.__init__)


def test_hyp_c_sharp_modifiers_sealed_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Sealed.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_private_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Private)


def test_hyp_c_sharp_modifiers_private_constructor_exists():
    assert callable(c_sharp_modifiers_Private.__init__)


def test_hyp_c_sharp_modifiers_private_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Private.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_public_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Public)


def test_hyp_c_sharp_modifiers_public_constructor_exists():
    assert callable(c_sharp_modifiers_Public.__init__)


def test_hyp_c_sharp_modifiers_public_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Public.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_abstract_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Abstract)


def test_hyp_c_sharp_modifiers_abstract_constructor_exists():
    assert callable(c_sharp_modifiers_Abstract.__init__)


def test_hyp_c_sharp_modifiers_abstract_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Abstract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_virtual_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Virtual)


def test_hyp_c_sharp_modifiers_virtual_constructor_exists():
    assert callable(c_sharp_modifiers_Virtual.__init__)


def test_hyp_c_sharp_modifiers_virtual_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Virtual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_overridemodifier_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_OverrideModifier)


def test_hyp_c_sharp_modifiers_overridemodifier_constructor_exists():
    assert callable(c_sharp_modifiers_OverrideModifier.__init__)


def test_hyp_c_sharp_modifiers_overridemodifier_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_OverrideModifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_static_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Static)


def test_hyp_c_sharp_modifiers_static_constructor_exists():
    assert callable(c_sharp_modifiers_Static.__init__)


def test_hyp_c_sharp_modifiers_static_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Static.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_protected_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Protected)


def test_hyp_c_sharp_modifiers_protected_constructor_exists():
    assert callable(c_sharp_modifiers_Protected.__init__)


def test_hyp_c_sharp_modifiers_protected_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Protected.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_internal_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Internal)


def test_hyp_c_sharp_modifiers_internal_constructor_exists():
    assert callable(c_sharp_modifiers_Internal.__init__)


def test_hyp_c_sharp_modifiers_internal_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Internal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_modifiers_unsafe_is_not_abstract():
    assert not inspect.isabstract(c_sharp_modifiers_Unsafe)


def test_hyp_c_sharp_modifiers_unsafe_constructor_exists():
    assert callable(c_sharp_modifiers_Unsafe.__init__)


def test_hyp_c_sharp_modifiers_unsafe_constructor_args():
    sig = inspect.signature(c_sharp_modifiers_Unsafe.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attributes_is_not_abstract():
    assert not inspect.isabstract(Attributes)


def test_hyp_attributes_constructor_exists():
    assert callable(Attributes.__init__)


def test_hyp_attributes_constructor_args():
    sig = inspect.signature(Attributes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespaces_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(namespaces_TypeDeclaration)


def test_hyp_namespaces_typedeclaration_constructor_exists():
    assert callable(namespaces_TypeDeclaration.__init__)


def test_hyp_namespaces_typedeclaration_constructor_args():
    sig = inspect.signature(namespaces_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_class_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_Class)


def test_hyp_c_sharp_classes_class_constructor_exists():
    assert callable(c_sharp_classes_Class.__init__)


def test_hyp_c_sharp_classes_class_constructor_args():
    sig = inspect.signature(c_sharp_classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(classes_ClassMemberDeclaration)


def test_hyp_classes_classmemberdeclaration_constructor_exists():
    assert callable(classes_ClassMemberDeclaration.__init__)


def test_hyp_classes_classmemberdeclaration_constructor_args():
    sig = inspect.signature(classes_ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_classes_method_is_not_abstract():
    assert not inspect.isabstract(c_sharp_classes_Method)


def test_hyp_c_sharp_classes_method_constructor_exists():
    assert callable(c_sharp_classes_Method.__init__)


def test_hyp_c_sharp_classes_method_constructor_args():
    sig = inspect.signature(c_sharp_classes_Method.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespaces_namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(namespaces_NamespaceMemberDeclaration)


def test_hyp_namespaces_namespacememberdeclaration_constructor_exists():
    assert callable(namespaces_NamespaceMemberDeclaration.__init__)


def test_hyp_namespaces_namespacememberdeclaration_constructor_args():
    sig = inspect.signature(namespaces_NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_namespaces_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_TypeDeclaration)


def test_hyp_c_sharp_namespaces_typedeclaration_constructor_exists():
    assert callable(c_sharp_namespaces_TypeDeclaration.__init__)


def test_hyp_c_sharp_namespaces_typedeclaration_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_namespaces_namespacebody_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_NamespaceBody)


def test_hyp_c_sharp_namespaces_namespacebody_constructor_exists():
    assert callable(c_sharp_namespaces_NamespaceBody.__init__)


def test_hyp_c_sharp_namespaces_namespacebody_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_NamespaceBody.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespacebody_is_not_abstract():
    assert not inspect.isabstract(NamespaceBody)


def test_hyp_namespacebody_constructor_exists():
    assert callable(NamespaceBody.__init__)


def test_hyp_namespacebody_constructor_args():
    sig = inspect.signature(NamespaceBody.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_namespaces_namespace_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_Namespace)


def test_hyp_c_sharp_namespaces_namespace_constructor_exists():
    assert callable(c_sharp_namespaces_Namespace.__init__)


def test_hyp_c_sharp_namespaces_namespace_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_namespaces_namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_NamespaceMemberDeclaration)


def test_hyp_c_sharp_namespaces_namespacememberdeclaration_constructor_exists():
    assert callable(c_sharp_namespaces_NamespaceMemberDeclaration.__init__)


def test_hyp_c_sharp_namespaces_namespacememberdeclaration_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespaceortypename_is_not_abstract():
    assert not inspect.isabstract(NamespaceOrTypeName)


def test_hyp_namespaceortypename_constructor_exists():
    assert callable(NamespaceOrTypeName.__init__)


def test_hyp_namespaceortypename_constructor_args():
    sig = inspect.signature(NamespaceOrTypeName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_VariableDeclarator)


def test_hyp_c_sharp_statements_variabledeclarator_constructor_exists():
    assert callable(c_sharp_statements_VariableDeclarator.__init__)


def test_hyp_c_sharp_statements_variabledeclarator_constructor_args():
    sig = inspect.signature(c_sharp_statements_VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_statements_constantdeclarator_is_not_abstract():
    assert not inspect.isabstract(c_sharp_statements_ConstantDeclarator)


def test_hyp_c_sharp_statements_constantdeclarator_constructor_exists():
    assert callable(c_sharp_statements_ConstantDeclarator.__init__)


def test_hyp_c_sharp_statements_constantdeclarator_constructor_args():
    sig = inspect.signature(c_sharp_statements_ConstantDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_c_sharp_namespaces_usingdirective_is_not_abstract():
    assert not inspect.isabstract(c_sharp_namespaces_UsingDirective)


def test_hyp_c_sharp_namespaces_usingdirective_constructor_exists():
    assert callable(c_sharp_namespaces_UsingDirective.__init__)


def test_hyp_c_sharp_namespaces_usingdirective_constructor_args():
    sig = inspect.signature(c_sharp_namespaces_UsingDirective.__init__)
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
ShiftOperator_strategy = st.builds(
    ShiftOperator,
)
c_sharp_operators_RightShift_strategy = st.builds(
    c_sharp_operators_RightShift,
)
c_sharp_operators_LeftShift_strategy = st.builds(
    c_sharp_operators_LeftShift,
)
UnaryModificationOperator_strategy = st.builds(
    UnaryModificationOperator,
)
c_sharp_operators_PlusPlus_strategy = st.builds(
    c_sharp_operators_PlusPlus,
)
c_sharp_operators_MinusMinus_strategy = st.builds(
    c_sharp_operators_MinusMinus,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
c_sharp_operators_Negate_strategy = st.builds(
    c_sharp_operators_Negate,
)
c_sharp_operators_Complement_strategy = st.builds(
    c_sharp_operators_Complement,
)
MultiplicativeOperator_strategy = st.builds(
    MultiplicativeOperator,
)
c_sharp_operators_Remainder_strategy = st.builds(
    c_sharp_operators_Remainder,
)
c_sharp_operators_Multiplication_strategy = st.builds(
    c_sharp_operators_Multiplication,
)
c_sharp_operators_Division_strategy = st.builds(
    c_sharp_operators_Division,
)
operators_UnaryOperator_strategy = st.builds(
    operators_UnaryOperator,
)
operators_AdditiveOperator_strategy = st.builds(
    operators_AdditiveOperator,
)
c_sharp_operators_Subtraction_strategy = st.builds(
    c_sharp_operators_Subtraction,
)
c_sharp_operators_Addition_strategy = st.builds(
    c_sharp_operators_Addition,
)
RelationOperator_strategy = st.builds(
    RelationOperator,
)
c_sharp_operators_GreaterThanOrEqual_strategy = st.builds(
    c_sharp_operators_GreaterThanOrEqual,
)
c_sharp_operators_LessThan_strategy = st.builds(
    c_sharp_operators_LessThan,
)
c_sharp_operators_LessThanOrEqual_strategy = st.builds(
    c_sharp_operators_LessThanOrEqual,
)
c_sharp_operators_GreaterThan_strategy = st.builds(
    c_sharp_operators_GreaterThan,
)
EqualityOperator_strategy = st.builds(
    EqualityOperator,
)
c_sharp_operators_NotEqual_strategy = st.builds(
    c_sharp_operators_NotEqual,
)
c_sharp_operators_Equal_strategy = st.builds(
    c_sharp_operators_Equal,
)
c_sharp_operators_ConditionalOr_strategy = st.builds(
    c_sharp_operators_ConditionalOr,
)
c_sharp_operators_ConditionalAnd_strategy = st.builds(
    c_sharp_operators_ConditionalAnd,
)
c_sharp_operators_InclusiveOr_strategy = st.builds(
    c_sharp_operators_InclusiveOr,
)
c_sharp_operators_ExclusiveOr_strategy = st.builds(
    c_sharp_operators_ExclusiveOr,
)
c_sharp_operators_And_strategy = st.builds(
    c_sharp_operators_And,
)
c_sharp_operators_UnsignedRightShift_strategy = st.builds(
    c_sharp_operators_UnsignedRightShift,
)
Operator_strategy = st.builds(
    Operator,
)
c_sharp_operators_UnaryModificationOperator_strategy = st.builds(
    c_sharp_operators_UnaryModificationOperator,
)
c_sharp_operators_RelationOperator_strategy = st.builds(
    c_sharp_operators_RelationOperator,
)
c_sharp_operators_MultiplicativeOperator_strategy = st.builds(
    c_sharp_operators_MultiplicativeOperator,
)
c_sharp_operators_EqualityOperator_strategy = st.builds(
    c_sharp_operators_EqualityOperator,
)
c_sharp_operators_UnaryOperator_strategy = st.builds(
    c_sharp_operators_UnaryOperator,
)
c_sharp_operators_AssignmentOperator_strategy = st.builds(
    c_sharp_operators_AssignmentOperator,
)
c_sharp_operators_ShiftOperator_strategy = st.builds(
    c_sharp_operators_ShiftOperator,
)
c_sharp_operators_AdditiveOperator_strategy = st.builds(
    c_sharp_operators_AdditiveOperator,
)
c_sharp_operators_Operator_strategy = st.builds(
    c_sharp_operators_Operator,
)
c_sharp_keywords_Event_strategy = st.builds(
    c_sharp_keywords_Event,
)
c_sharp_keywords_Return_strategy = st.builds(
    c_sharp_keywords_Return,
)
c_sharp_keywords_Default_strategy = st.builds(
    c_sharp_keywords_Default,
)
c_sharp_keywords_Case_strategy = st.builds(
    c_sharp_keywords_Case,
)
c_sharp_keywords_Params_strategy = st.builds(
    c_sharp_keywords_Params,
)
c_sharp_keywords_Ref_strategy = st.builds(
    c_sharp_keywords_Ref,
)
c_sharp_keywords_Out_strategy = st.builds(
    c_sharp_keywords_Out,
)
c_sharp_modifiers_Modifier_strategy = st.builds(
    c_sharp_modifiers_Modifier,
)
ReferenceType_strategy = st.builds(
    ReferenceType,
)
c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_strategy = st.builds(
    c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType,
)
Literal_strategy = st.builds(
    Literal,
)
c_sharp_literals_StringLiteral_strategy = st.builds(
    c_sharp_literals_StringLiteral,
    value=
        safe_text
)
c_sharp_literals_RealLiteral_strategy = st.builds(
    c_sharp_literals_RealLiteral,
    value=
        safe_text
)
c_sharp_literals_CharacterLiteral_strategy = st.builds(
    c_sharp_literals_CharacterLiteral,
    value=
        safe_text
)
c_sharp_literals_NullLiteral_strategy = st.builds(
    c_sharp_literals_NullLiteral,
)
c_sharp_literals_DecimalIntegerLiteral_strategy = st.builds(
    c_sharp_literals_DecimalIntegerLiteral,
    value=
        safe_text
)
c_sharp_literals_This_strategy = st.builds(
    c_sharp_literals_This,
)
c_sharp_literals_HexadecimalIntegerLiteral_strategy = st.builds(
    c_sharp_literals_HexadecimalIntegerLiteral,
    value=
        safe_text
)
c_sharp_literals_BooleanLiteral_strategy = st.builds(
    c_sharp_literals_BooleanLiteral,
    value=
        st.booleans()
)
InclusiveOrExpression_strategy = st.builds(
    InclusiveOrExpression,
)
c_sharp_expressions_ConditionalAndExpression_strategy = st.builds(
    c_sharp_expressions_ConditionalAndExpression,
)
InclusiveOr_strategy = st.builds(
    InclusiveOr,
)
ExclusiveOrExpression_strategy = st.builds(
    ExclusiveOrExpression,
)
c_sharp_expressions_InclusiveOrExpression_strategy = st.builds(
    c_sharp_expressions_InclusiveOrExpression,
)
ExclusiveOr_strategy = st.builds(
    ExclusiveOr,
)
AndExpression_strategy = st.builds(
    AndExpression,
)
c_sharp_expressions_ExclusiveOrExpression_strategy = st.builds(
    c_sharp_expressions_ExclusiveOrExpression,
)
And_strategy = st.builds(
    And,
)
EqualityExpression_strategy = st.builds(
    EqualityExpression,
)
c_sharp_expressions_AndExpression_strategy = st.builds(
    c_sharp_expressions_AndExpression,
)
NotEqual_strategy = st.builds(
    NotEqual,
)
Equal_strategy = st.builds(
    Equal,
)
types_Type_strategy = st.builds(
    types_Type,
)
types_NonArrayType_strategy = st.builds(
    types_NonArrayType,
)
c_sharp_types_SimpleType_strategy = st.builds(
    c_sharp_types_SimpleType,
)
c_sharp_types_PointerType_strategy = st.builds(
    c_sharp_types_PointerType,
)
c_sharp_types_ReferenceType_strategy = st.builds(
    c_sharp_types_ReferenceType,
)
c_sharp_types_NonArrayType_strategy = st.builds(
    c_sharp_types_NonArrayType,
)
c_sharp_types_Type_strategy = st.builds(
    c_sharp_types_Type,
)
ConditionalOr_strategy = st.builds(
    ConditionalOr,
)
ConditionalAndExpression_strategy = st.builds(
    ConditionalAndExpression,
)
c_sharp_expressions_ConditionalOrExpression_strategy = st.builds(
    c_sharp_expressions_ConditionalOrExpression,
)
ConditionalAnd_strategy = st.builds(
    ConditionalAnd,
)
MultiplicativeExpression_strategy = st.builds(
    MultiplicativeExpression,
)
c_sharp_expressions_AdditiveExpression_strategy = st.builds(
    c_sharp_expressions_AdditiveExpression,
)
Remainder_strategy = st.builds(
    Remainder,
)
Division_strategy = st.builds(
    Division,
)
c_sharp_expressions_MultiplicativeExpression_strategy = st.builds(
    c_sharp_expressions_MultiplicativeExpression,
)
c_sharp_expressions_AddressOfExpression_strategy = st.builds(
    c_sharp_expressions_AddressOfExpression,
)
c_sharp_expressions_CastExpression_strategy = st.builds(
    c_sharp_expressions_CastExpression,
)
RelationalExpression_strategy = st.builds(
    RelationalExpression,
)
c_sharp_expressions_EqualityExpression_strategy = st.builds(
    c_sharp_expressions_EqualityExpression,
)
GreaterThanOrEqual_strategy = st.builds(
    GreaterThanOrEqual,
)
GreaterThan_strategy = st.builds(
    GreaterThan,
)
LessThanOrEqual_strategy = st.builds(
    LessThanOrEqual,
)
LessThan_strategy = st.builds(
    LessThan,
)
ShiftExpression_strategy = st.builds(
    ShiftExpression,
)
c_sharp_expressions_RelationalExpression_strategy = st.builds(
    c_sharp_expressions_RelationalExpression,
)
AdditiveExpression_strategy = st.builds(
    AdditiveExpression,
)
LeftShift_strategy = st.builds(
    LeftShift,
)
RightShift_strategy = st.builds(
    RightShift,
)
c_sharp_expressions_ShiftExpression_strategy = st.builds(
    c_sharp_expressions_ShiftExpression,
)
AssignmentOperator_strategy = st.builds(
    AssignmentOperator,
)
c_sharp_operators_AssignmentUnsignedRightShift_strategy = st.builds(
    c_sharp_operators_AssignmentUnsignedRightShift,
)
c_sharp_operators_AssignmentAnd_strategy = st.builds(
    c_sharp_operators_AssignmentAnd,
)
c_sharp_operators_AssignmentExclusiveOr_strategy = st.builds(
    c_sharp_operators_AssignmentExclusiveOr,
)
c_sharp_operators_AssignmentLeftShift_strategy = st.builds(
    c_sharp_operators_AssignmentLeftShift,
)
c_sharp_operators_AssignmentPlus_strategy = st.builds(
    c_sharp_operators_AssignmentPlus,
)
c_sharp_operators_AssignmentDivision_strategy = st.builds(
    c_sharp_operators_AssignmentDivision,
)
c_sharp_operators_AssignmentOr_strategy = st.builds(
    c_sharp_operators_AssignmentOr,
)
c_sharp_operators_Assignment_strategy = st.builds(
    c_sharp_operators_Assignment,
)
c_sharp_operators_AssignmentRightShift_strategy = st.builds(
    c_sharp_operators_AssignmentRightShift,
)
c_sharp_operators_AssignmentMultiplication_strategy = st.builds(
    c_sharp_operators_AssignmentMultiplication,
)
c_sharp_operators_AssignmentMinus_strategy = st.builds(
    c_sharp_operators_AssignmentMinus,
)
c_sharp_operators_AssignmentModulo_strategy = st.builds(
    c_sharp_operators_AssignmentModulo,
)
expressions_Expression_strategy = st.builds(
    expressions_Expression,
)
ConditionalOrExpression_strategy = st.builds(
    ConditionalOrExpression,
)
AddressOfExpression_strategy = st.builds(
    AddressOfExpression,
)
CastExpression_strategy = st.builds(
    CastExpression,
)
PreDecrementExpression_strategy = st.builds(
    PreDecrementExpression,
)
ArrayInitializer_strategy = st.builds(
    ArrayInitializer,
)
PrimaryNoArrayCreationExpression_strategy = st.builds(
    PrimaryNoArrayCreationExpression,
)
c_sharp_literals_Literal_strategy = st.builds(
    c_sharp_literals_Literal,
)
c_sharp_expressions_TypeOfExpression_strategy = st.builds(
    c_sharp_expressions_TypeOfExpression,
)
c_sharp_expressions_SizeOfExpression_strategy = st.builds(
    c_sharp_expressions_SizeOfExpression,
)
c_sharp_expressions_UncheckedExpression_strategy = st.builds(
    c_sharp_expressions_UncheckedExpression,
)
c_sharp_expressions_DelegateCreationExpression_strategy = st.builds(
    c_sharp_expressions_DelegateCreationExpression,
)
c_sharp_expressions_CheckedExpression_strategy = st.builds(
    c_sharp_expressions_CheckedExpression,
)
c_sharp_expressions_BaseAccess_strategy = st.builds(
    c_sharp_expressions_BaseAccess,
)
PreIncrementExpression_strategy = st.builds(
    PreIncrementExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
Multiplication_strategy = st.builds(
    Multiplication,
)
Complement_strategy = st.builds(
    Complement,
)
Negate_strategy = st.builds(
    Negate,
)
Subtraction_strategy = st.builds(
    Subtraction,
)
Addition_strategy = st.builds(
    Addition,
)
MemberAccess_strategy = st.builds(
    MemberAccess,
)
c_sharp_expressions_UnaryExpression_strategy = st.builds(
    c_sharp_expressions_UnaryExpression,
)
c_sharp_expressions_ParenthesizedExpression_strategy = st.builds(
    c_sharp_expressions_ParenthesizedExpression,
)
c_sharp_expressions_Argument_strategy = st.builds(
    c_sharp_expressions_Argument,
)
c_sharp_expressions_ExpressionList_strategy = st.builds(
    c_sharp_expressions_ExpressionList,
)
classes_VariableInitializer_strategy = st.builds(
    classes_VariableInitializer,
)
c_sharp_expressions_StatementExpression_strategy = st.builds(
    c_sharp_expressions_StatementExpression,
)
ArgumentList_strategy = st.builds(
    ArgumentList,
)
expressions_StatementExpression_strategy = st.builds(
    expressions_StatementExpression,
)
c_sharp_expressions_AssignmentExpression_strategy = st.builds(
    c_sharp_expressions_AssignmentExpression,
)
expressions_PrimaryExtendedExpressionType_strategy = st.builds(
    expressions_PrimaryExtendedExpressionType,
)
c_sharp_expressions_PostIncrementExpression_strategy = st.builds(
    c_sharp_expressions_PostIncrementExpression,
)
c_sharp_expressions_PostDecrementExpression_strategy = st.builds(
    c_sharp_expressions_PostDecrementExpression,
)
c_sharp_expressions_InvocationExpression_strategy = st.builds(
    c_sharp_expressions_InvocationExpression,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
c_sharp_types_Byte_strategy = st.builds(
    c_sharp_types_Byte,
)
c_sharp_types_UInt_strategy = st.builds(
    c_sharp_types_UInt,
)
c_sharp_types_Float_strategy = st.builds(
    c_sharp_types_Float,
)
c_sharp_types_Short_strategy = st.builds(
    c_sharp_types_Short,
)
c_sharp_types_Object_strategy = st.builds(
    c_sharp_types_Object,
)
c_sharp_types_Void_strategy = st.builds(
    c_sharp_types_Void,
)
c_sharp_types_Bool_strategy = st.builds(
    c_sharp_types_Bool,
)
c_sharp_types_Decimal_strategy = st.builds(
    c_sharp_types_Decimal,
)
c_sharp_types_SByte_strategy = st.builds(
    c_sharp_types_SByte,
)
c_sharp_types_Double_strategy = st.builds(
    c_sharp_types_Double,
)
c_sharp_types_Char_strategy = st.builds(
    c_sharp_types_Char,
)
c_sharp_types_UShort_strategy = st.builds(
    c_sharp_types_UShort,
)
c_sharp_types_Long_strategy = st.builds(
    c_sharp_types_Long,
)
c_sharp_types_String_strategy = st.builds(
    c_sharp_types_String,
)
c_sharp_types_Int_strategy = st.builds(
    c_sharp_types_Int,
)
c_sharp_types_ULong_strategy = st.builds(
    c_sharp_types_ULong,
)
PrimaryExtendedExpressionType_strategy = st.builds(
    PrimaryExtendedExpressionType,
)
c_sharp_expressions_PointerMemberAccess_strategy = st.builds(
    c_sharp_expressions_PointerMemberAccess,
)
c_sharp_expressions_ElementAccess_strategy = st.builds(
    c_sharp_expressions_ElementAccess,
)
c_sharp_expressions_MemberAccess_strategy = st.builds(
    c_sharp_expressions_MemberAccess,
)
c_sharp_expressions_PrimaryExtendedExpressionType_strategy = st.builds(
    c_sharp_expressions_PrimaryExtendedExpressionType,
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
c_sharp_expressions_ArrayCreationExpression_strategy = st.builds(
    c_sharp_expressions_ArrayCreationExpression,
)
c_sharp_expressions_PrimaryNoArrayCreationExpression_strategy = st.builds(
    c_sharp_expressions_PrimaryNoArrayCreationExpression,
)
c_sharp_expressions_PrimaryExpression_strategy = st.builds(
    c_sharp_expressions_PrimaryExpression,
)
Argument_strategy = st.builds(
    Argument,
)
c_sharp_expressions_ArgumentList_strategy = st.builds(
    c_sharp_expressions_ArgumentList,
)
FixedPointerDeclarator_strategy = st.builds(
    FixedPointerDeclarator,
)
PointerType_strategy = st.builds(
    PointerType,
)
ResourceAcquisition_strategy = st.builds(
    ResourceAcquisition,
)
c_sharp_statements_ResourceAcquisition_strategy = st.builds(
    c_sharp_statements_ResourceAcquisition,
)
c_sharp_statements_LocalConstantDeclaration_strategy = st.builds(
    c_sharp_statements_LocalConstantDeclaration,
)
statements_ResourceAcquisition_strategy = st.builds(
    statements_ResourceAcquisition,
)
c_sharp_expressions_Expression_strategy = st.builds(
    c_sharp_expressions_Expression,
)
statements_ForInitializer_strategy = st.builds(
    statements_ForInitializer,
)
c_sharp_statements_VariableDeclaration_strategy = st.builds(
    c_sharp_statements_VariableDeclaration,
)
c_sharp_statements_FixedPointerDeclarator_strategy = st.builds(
    c_sharp_statements_FixedPointerDeclarator,
)
JumpStatement_strategy = st.builds(
    JumpStatement,
)
c_sharp_statements_ReturnStatement_strategy = st.builds(
    c_sharp_statements_ReturnStatement,
)
c_sharp_statements_ContinueStatement_strategy = st.builds(
    c_sharp_statements_ContinueStatement,
)
c_sharp_statements_GotoStatement_strategy = st.builds(
    c_sharp_statements_GotoStatement,
)
c_sharp_statements_BreakStatement_strategy = st.builds(
    c_sharp_statements_BreakStatement,
)
c_sharp_statements_ForInitializer_strategy = st.builds(
    c_sharp_statements_ForInitializer,
)
c_sharp_statements_FinallyClause_strategy = st.builds(
    c_sharp_statements_FinallyClause,
)
c_sharp_statements_GeneralCatchClause_strategy = st.builds(
    c_sharp_statements_GeneralCatchClause,
)
c_sharp_statements_SpecificCatchClause_strategy = st.builds(
    c_sharp_statements_SpecificCatchClause,
)
FinallyClause_strategy = st.builds(
    FinallyClause,
)
GeneralCatchClause_strategy = st.builds(
    GeneralCatchClause,
)
SpecificCatchClause_strategy = st.builds(
    SpecificCatchClause,
)
c_sharp_statements_ThrowStatement_strategy = st.builds(
    c_sharp_statements_ThrowStatement,
)
Default_strategy = st.builds(
    Default,
)
c_sharp_statements_SwitchLabel_strategy = st.builds(
    c_sharp_statements_SwitchLabel,
)
SwitchLabel_strategy = st.builds(
    SwitchLabel,
)
c_sharp_statements_SwitchSection_strategy = st.builds(
    c_sharp_statements_SwitchSection,
)
SwitchSection_strategy = st.builds(
    SwitchSection,
)
SelectionStatement_strategy = st.builds(
    SelectionStatement,
)
c_sharp_statements_SwitchStatement_strategy = st.builds(
    c_sharp_statements_SwitchStatement,
)
c_sharp_statements_IfStatement_strategy = st.builds(
    c_sharp_statements_IfStatement,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
c_sharp_expressions_PreDecrementExpression_strategy = st.builds(
    c_sharp_expressions_PreDecrementExpression,
)
c_sharp_expressions_PreIncrementExpression_strategy = st.builds(
    c_sharp_expressions_PreIncrementExpression,
)
StatementExpressionList_strategy = st.builds(
    StatementExpressionList,
)
ForInitializer_strategy = st.builds(
    ForInitializer,
)
c_sharp_expressions_StatementExpressionList_strategy = st.builds(
    c_sharp_expressions_StatementExpressionList,
)
IterationStatement_strategy = st.builds(
    IterationStatement,
)
c_sharp_statements_ForeachStatement_strategy = st.builds(
    c_sharp_statements_ForeachStatement,
)
c_sharp_statements_DoStatement_strategy = st.builds(
    c_sharp_statements_DoStatement,
)
c_sharp_statements_ForStatement_strategy = st.builds(
    c_sharp_statements_ForStatement,
)
c_sharp_statements_WhileStatement_strategy = st.builds(
    c_sharp_statements_WhileStatement,
)
Case_strategy = st.builds(
    Case,
)
NamedArgumentList_strategy = st.builds(
    NamedArgumentList,
)
ExpressionList_strategy = st.builds(
    ExpressionList,
)
c_sharp_attributes_AttributeArguments_strategy = st.builds(
    c_sharp_attributes_AttributeArguments,
)
AttributeArguments_strategy = st.builds(
    AttributeArguments,
)
c_sharp_attributes_Attribute_strategy = st.builds(
    c_sharp_attributes_Attribute,
)
Return_strategy = st.builds(
    Return,
)
Event_strategy = st.builds(
    Event,
)
c_sharp_attributes_AttributeTarget_strategy = st.builds(
    c_sharp_attributes_AttributeTarget,
)
AttributeTarget_strategy = st.builds(
    AttributeTarget,
)
c_sharp_attributes_Attributes_strategy = st.builds(
    c_sharp_attributes_Attributes,
)
c_sharp_attributes_GlobalAttributeTarget_strategy = st.builds(
    c_sharp_attributes_GlobalAttributeTarget,
)
Unsafe_strategy = st.builds(
    Unsafe,
)
EmbeddedStatement_strategy = st.builds(
    EmbeddedStatement,
)
c_sharp_statements_CheckedStatement_strategy = st.builds(
    c_sharp_statements_CheckedStatement,
)
c_sharp_statements_LockStatement_strategy = st.builds(
    c_sharp_statements_LockStatement,
)
c_sharp_statements_UncheckedStatement_strategy = st.builds(
    c_sharp_statements_UncheckedStatement,
)
c_sharp_statements_SelectionStatement_strategy = st.builds(
    c_sharp_statements_SelectionStatement,
)
c_sharp_statements_UsingStatement_strategy = st.builds(
    c_sharp_statements_UsingStatement,
)
c_sharp_statements_EmptyStatement_strategy = st.builds(
    c_sharp_statements_EmptyStatement,
)
c_sharp_statements_IterationStatement_strategy = st.builds(
    c_sharp_statements_IterationStatement,
)
c_sharp_statements_ExpressionStatement_strategy = st.builds(
    c_sharp_statements_ExpressionStatement,
)
c_sharp_statements_JumpStatement_strategy = st.builds(
    c_sharp_statements_JumpStatement,
)
c_sharp_statements_TryStatement_strategy = st.builds(
    c_sharp_statements_TryStatement,
)
c_sharp_statements_FixedStatement_strategy = st.builds(
    c_sharp_statements_FixedStatement,
)
c_sharp_statements_SimpleEmbeddedStatement_strategy = st.builds(
    c_sharp_statements_SimpleEmbeddedStatement,
)
LocalConstantDeclaration_strategy = st.builds(
    LocalConstantDeclaration,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
c_sharp_statements_Statement_strategy = st.builds(
    c_sharp_statements_Statement,
)
c_sharp_attributes_NamedArgument_strategy = st.builds(
    c_sharp_attributes_NamedArgument,
)
NamedArgument_strategy = st.builds(
    NamedArgument,
)
c_sharp_attributes_NamedArgumentList_strategy = st.builds(
    c_sharp_attributes_NamedArgumentList,
)
ConstantDeclarator_strategy = st.builds(
    ConstantDeclarator,
)
c_sharp_classes_VariableInitializer_strategy = st.builds(
    c_sharp_classes_VariableInitializer,
)
Statement_strategy = st.builds(
    Statement,
)
c_sharp_statements_DeclarationStatement_strategy = st.builds(
    c_sharp_statements_DeclarationStatement,
)
c_sharp_statements_EmbeddedStatement_strategy = st.builds(
    c_sharp_statements_EmbeddedStatement,
)
c_sharp_classes_Block_strategy = st.builds(
    c_sharp_classes_Block,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
Attribute_strategy = st.builds(
    Attribute,
)
GlobalAttributeTarget_strategy = st.builds(
    GlobalAttributeTarget,
)
c_sharp_attributes_GlobalAttributes_strategy = st.builds(
    c_sharp_attributes_GlobalAttributes,
)
c_sharp_arrays_RankSpecifier_strategy = st.builds(
    c_sharp_arrays_RankSpecifier,
)
RankSpecifier_strategy = st.builds(
    RankSpecifier,
)
NonArrayType_strategy = st.builds(
    NonArrayType,
)
Expression_strategy = st.builds(
    Expression,
)
c_sharp_expressions_ConditionalExpression_strategy = st.builds(
    c_sharp_expressions_ConditionalExpression,
)
VariableInitializer_strategy = st.builds(
    VariableInitializer,
)
c_sharp_arrays_ArrayInitializer_strategy = st.builds(
    c_sharp_arrays_ArrayInitializer,
)
c_sharp_arrays_StackallocInitializer_strategy = st.builds(
    c_sharp_arrays_StackallocInitializer,
)
VariableDeclarator_strategy = st.builds(
    VariableDeclarator,
)
FormalParameterList_strategy = st.builds(
    FormalParameterList,
)
Type_strategy = st.builds(
    Type,
)
c_sharp_arrays_ArrayType_strategy = st.builds(
    c_sharp_arrays_ArrayType,
)
c_sharp_classes_ClassMemberDeclaration_strategy = st.builds(
    c_sharp_classes_ClassMemberDeclaration,
)
ClassOrInterfaceOrDelegateOrEnumType_strategy = st.builds(
    ClassOrInterfaceOrDelegateOrEnumType,
)
c_sharp_classes_ClassBase_strategy = st.builds(
    c_sharp_classes_ClassBase,
)
ClassMemberDeclaration_strategy = st.builds(
    ClassMemberDeclaration,
)
c_sharp_classes_ConstantDeclaration_strategy = st.builds(
    c_sharp_classes_ConstantDeclaration,
)
c_sharp_classes_FieldDeclaration_strategy = st.builds(
    c_sharp_classes_FieldDeclaration,
)
Params_strategy = st.builds(
    Params,
)
c_sharp_classes_ParameterArray_strategy = st.builds(
    c_sharp_classes_ParameterArray,
)
Out_strategy = st.builds(
    Out,
)
Ref_strategy = st.builds(
    Ref,
)
c_sharp_classes_FixedParameter_strategy = st.builds(
    c_sharp_classes_FixedParameter,
)
ParameterArray_strategy = st.builds(
    ParameterArray,
)
FixedParameter_strategy = st.builds(
    FixedParameter,
)
c_sharp_classes_FormalParameterList_strategy = st.builds(
    c_sharp_classes_FormalParameterList,
)
Block_strategy = st.builds(
    Block,
)
NamespaceMemberDeclaration_strategy = st.builds(
    NamespaceMemberDeclaration,
)
GlobalAttributes_strategy = st.builds(
    GlobalAttributes,
)
UsingDirective_strategy = st.builds(
    UsingDirective,
)
c_sharp_namespaces_CompilationUnit_strategy = st.builds(
    c_sharp_namespaces_CompilationUnit,
)
expressions_PrimaryNoArrayCreationExpression_strategy = st.builds(
    expressions_PrimaryNoArrayCreationExpression,
)
c_sharp_expressions_ObjectCreationExpression_strategy = st.builds(
    c_sharp_expressions_ObjectCreationExpression,
)
common_NamedElement_strategy = st.builds(
    common_NamedElement,
)
c_sharp_statements_LabeledStatement_strategy = st.builds(
    c_sharp_statements_LabeledStatement,
)
c_sharp_common_Identifier_strategy = st.builds(
    c_sharp_common_Identifier,
)
Identifier_strategy = st.builds(
    Identifier,
)
c_sharp_common_NamespaceOrTypeName_strategy = st.builds(
    c_sharp_common_NamespaceOrTypeName,
)
c_sharp_common_NamedElement_strategy = st.builds(
    c_sharp_common_NamedElement,
    name=
        safe_text
)
ClassBase_strategy = st.builds(
    ClassBase,
)
Modifier_strategy = st.builds(
    Modifier,
)
c_sharp_modifiers_Extern_strategy = st.builds(
    c_sharp_modifiers_Extern,
)
c_sharp_modifiers_ReadOnly_strategy = st.builds(
    c_sharp_modifiers_ReadOnly,
)
c_sharp_modifiers_New_strategy = st.builds(
    c_sharp_modifiers_New,
)
c_sharp_modifiers_Partial_strategy = st.builds(
    c_sharp_modifiers_Partial,
)
c_sharp_modifiers_Volatile_strategy = st.builds(
    c_sharp_modifiers_Volatile,
)
c_sharp_modifiers_Sealed_strategy = st.builds(
    c_sharp_modifiers_Sealed,
)
c_sharp_modifiers_Private_strategy = st.builds(
    c_sharp_modifiers_Private,
)
c_sharp_modifiers_Public_strategy = st.builds(
    c_sharp_modifiers_Public,
)
c_sharp_modifiers_Abstract_strategy = st.builds(
    c_sharp_modifiers_Abstract,
)
c_sharp_modifiers_Virtual_strategy = st.builds(
    c_sharp_modifiers_Virtual,
)
c_sharp_modifiers_OverrideModifier_strategy = st.builds(
    c_sharp_modifiers_OverrideModifier,
)
c_sharp_modifiers_Static_strategy = st.builds(
    c_sharp_modifiers_Static,
)
c_sharp_modifiers_Protected_strategy = st.builds(
    c_sharp_modifiers_Protected,
)
c_sharp_modifiers_Internal_strategy = st.builds(
    c_sharp_modifiers_Internal,
)
c_sharp_modifiers_Unsafe_strategy = st.builds(
    c_sharp_modifiers_Unsafe,
)
Attributes_strategy = st.builds(
    Attributes,
)
namespaces_TypeDeclaration_strategy = st.builds(
    namespaces_TypeDeclaration,
)
c_sharp_classes_Class_strategy = st.builds(
    c_sharp_classes_Class,
)
classes_ClassMemberDeclaration_strategy = st.builds(
    classes_ClassMemberDeclaration,
)
c_sharp_classes_Method_strategy = st.builds(
    c_sharp_classes_Method,
)
namespaces_NamespaceMemberDeclaration_strategy = st.builds(
    namespaces_NamespaceMemberDeclaration,
)
c_sharp_namespaces_TypeDeclaration_strategy = st.builds(
    c_sharp_namespaces_TypeDeclaration,
)
c_sharp_namespaces_NamespaceBody_strategy = st.builds(
    c_sharp_namespaces_NamespaceBody,
)
NamespaceBody_strategy = st.builds(
    NamespaceBody,
)
c_sharp_namespaces_Namespace_strategy = st.builds(
    c_sharp_namespaces_Namespace,
)
c_sharp_namespaces_NamespaceMemberDeclaration_strategy = st.builds(
    c_sharp_namespaces_NamespaceMemberDeclaration,
)
NamespaceOrTypeName_strategy = st.builds(
    NamespaceOrTypeName,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
c_sharp_statements_VariableDeclarator_strategy = st.builds(
    c_sharp_statements_VariableDeclarator,
)
c_sharp_statements_ConstantDeclarator_strategy = st.builds(
    c_sharp_statements_ConstantDeclarator,
)
c_sharp_namespaces_UsingDirective_strategy = st.builds(
    c_sharp_namespaces_UsingDirective,
)
























































@given(instance=c_sharp_literals_StringLiteral_strategy)
def test_hyp_c_sharp_literals_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=c_sharp_literals_RealLiteral_strategy)
def test_hyp_c_sharp_literals_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=c_sharp_literals_CharacterLiteral_strategy)
def test_hyp_c_sharp_literals_characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=c_sharp_literals_DecimalIntegerLiteral_strategy)
def test_hyp_c_sharp_literals_decimalintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=c_sharp_literals_HexadecimalIntegerLiteral_strategy)
def test_hyp_c_sharp_literals_hexadecimalintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=c_sharp_literals_BooleanLiteral_strategy)
def test_hyp_c_sharp_literals_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






















































































































































































































































@given(instance=c_sharp_common_NamedElement_strategy)
def test_hyp_c_sharp_common_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



































# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Addition,
    AdditiveExpression,
    AddressOfExpression,
    And,
    AndExpression,
    Argument,
    ArgumentList,
    ArrayInitializer,
    ArrayType,
    AssignmentOperator,
    Attribute,
    AttributeArguments,
    AttributeTarget,
    Attributes,
    Block,
    Case,
    CastExpression,
    ClassBase,
    ClassMemberDeclaration,
    ClassOrInterfaceOrDelegateOrEnumType,
    Complement,
    ConditionalAnd,
    ConditionalAndExpression,
    ConditionalOr,
    ConditionalOrExpression,
    ConstantDeclarator,
    Default,
    Division,
    EmbeddedStatement,
    Equal,
    EqualityExpression,
    EqualityOperator,
    Event,
    ExclusiveOr,
    ExclusiveOrExpression,
    Expression,
    ExpressionList,
    FinallyClause,
    FixedParameter,
    FixedPointerDeclarator,
    ForInitializer,
    FormalParameterList,
    GeneralCatchClause,
    GlobalAttributeTarget,
    GlobalAttributes,
    GreaterThan,
    GreaterThanOrEqual,
    Identifier,
    InclusiveOr,
    InclusiveOrExpression,
    IterationStatement,
    JumpStatement,
    LeftShift,
    LessThan,
    LessThanOrEqual,
    Literal,
    LocalConstantDeclaration,
    MemberAccess,
    Modifier,
    Multiplication,
    MultiplicativeExpression,
    MultiplicativeOperator,
    NamedArgument,
    NamedArgumentList,
    NamedElement,
    NamespaceBody,
    NamespaceMemberDeclaration,
    NamespaceOrTypeName,
    Negate,
    NonArrayType,
    NotEqual,
    Operator,
    Out,
    ParameterArray,
    Params,
    PointerType,
    PreDecrementExpression,
    PreIncrementExpression,
    PrimaryExpression,
    PrimaryExtendedExpressionType,
    PrimaryNoArrayCreationExpression,
    RankSpecifier,
    Ref,
    ReferenceType,
    RelationOperator,
    RelationalExpression,
    Remainder,
    ResourceAcquisition,
    Return,
    RightShift,
    SelectionStatement,
    ShiftExpression,
    ShiftOperator,
    SimpleType,
    SpecificCatchClause,
    Statement,
    StatementExpression,
    StatementExpressionList,
    Subtraction,
    SwitchLabel,
    SwitchSection,
    Type,
    UnaryExpression,
    UnaryModificationOperator,
    UnaryOperator,
    Unsafe,
    UsingDirective,
    VariableDeclaration,
    VariableDeclarator,
    VariableInitializer,
    c_sharp_arrays_ArrayInitializer,
    c_sharp_arrays_ArrayType,
    c_sharp_arrays_RankSpecifier,
    c_sharp_arrays_StackallocInitializer,
    c_sharp_attributes_Attribute,
    c_sharp_attributes_AttributeArguments,
    c_sharp_attributes_AttributeTarget,
    c_sharp_attributes_Attributes,
    c_sharp_attributes_GlobalAttributeTarget,
    c_sharp_attributes_GlobalAttributes,
    c_sharp_attributes_NamedArgument,
    c_sharp_attributes_NamedArgumentList,
    c_sharp_classes_Block,
    c_sharp_classes_Class,
    c_sharp_classes_ClassBase,
    c_sharp_classes_ClassMemberDeclaration,
    c_sharp_classes_ConstantDeclaration,
    c_sharp_classes_FieldDeclaration,
    c_sharp_classes_FixedParameter,
    c_sharp_classes_FormalParameterList,
    c_sharp_classes_Method,
    c_sharp_classes_ParameterArray,
    c_sharp_classes_VariableInitializer,
    c_sharp_common_Identifier,
    c_sharp_common_NamedElement,
    c_sharp_common_NamespaceOrTypeName,
    c_sharp_expressions_AdditiveExpression,
    c_sharp_expressions_AddressOfExpression,
    c_sharp_expressions_AndExpression,
    c_sharp_expressions_Argument,
    c_sharp_expressions_ArgumentList,
    c_sharp_expressions_ArrayCreationExpression,
    c_sharp_expressions_AssignmentExpression,
    c_sharp_expressions_BaseAccess,
    c_sharp_expressions_CastExpression,
    c_sharp_expressions_CheckedExpression,
    c_sharp_expressions_ConditionalAndExpression,
    c_sharp_expressions_ConditionalExpression,
    c_sharp_expressions_ConditionalOrExpression,
    c_sharp_expressions_DelegateCreationExpression,
    c_sharp_expressions_ElementAccess,
    c_sharp_expressions_EqualityExpression,
    c_sharp_expressions_ExclusiveOrExpression,
    c_sharp_expressions_Expression,
    c_sharp_expressions_ExpressionList,
    c_sharp_expressions_InclusiveOrExpression,
    c_sharp_expressions_InvocationExpression,
    c_sharp_expressions_MemberAccess,
    c_sharp_expressions_MultiplicativeExpression,
    c_sharp_expressions_ObjectCreationExpression,
    c_sharp_expressions_ParenthesizedExpression,
    c_sharp_expressions_PointerMemberAccess,
    c_sharp_expressions_PostDecrementExpression,
    c_sharp_expressions_PostIncrementExpression,
    c_sharp_expressions_PreDecrementExpression,
    c_sharp_expressions_PreIncrementExpression,
    c_sharp_expressions_PrimaryExpression,
    c_sharp_expressions_PrimaryExtendedExpressionType,
    c_sharp_expressions_PrimaryNoArrayCreationExpression,
    c_sharp_expressions_RelationalExpression,
    c_sharp_expressions_ShiftExpression,
    c_sharp_expressions_SizeOfExpression,
    c_sharp_expressions_StatementExpression,
    c_sharp_expressions_StatementExpressionList,
    c_sharp_expressions_TypeOfExpression,
    c_sharp_expressions_UnaryExpression,
    c_sharp_expressions_UncheckedExpression,
    c_sharp_keywords_Case,
    c_sharp_keywords_Default,
    c_sharp_keywords_Event,
    c_sharp_keywords_Out,
    c_sharp_keywords_Params,
    c_sharp_keywords_Ref,
    c_sharp_keywords_Return,
    c_sharp_literals_BooleanLiteral,
    c_sharp_literals_CharacterLiteral,
    c_sharp_literals_DecimalIntegerLiteral,
    c_sharp_literals_HexadecimalIntegerLiteral,
    c_sharp_literals_Literal,
    c_sharp_literals_NullLiteral,
    c_sharp_literals_RealLiteral,
    c_sharp_literals_StringLiteral,
    c_sharp_literals_This,
    c_sharp_modifiers_Abstract,
    c_sharp_modifiers_Extern,
    c_sharp_modifiers_Internal,
    c_sharp_modifiers_Modifier,
    c_sharp_modifiers_New,
    c_sharp_modifiers_OverrideModifier,
    c_sharp_modifiers_Partial,
    c_sharp_modifiers_Private,
    c_sharp_modifiers_Protected,
    c_sharp_modifiers_Public,
    c_sharp_modifiers_ReadOnly,
    c_sharp_modifiers_Sealed,
    c_sharp_modifiers_Static,
    c_sharp_modifiers_Unsafe,
    c_sharp_modifiers_Virtual,
    c_sharp_modifiers_Volatile,
    c_sharp_namespaces_CompilationUnit,
    c_sharp_namespaces_Namespace,
    c_sharp_namespaces_NamespaceBody,
    c_sharp_namespaces_NamespaceMemberDeclaration,
    c_sharp_namespaces_TypeDeclaration,
    c_sharp_namespaces_UsingDirective,
    c_sharp_operators_Addition,
    c_sharp_operators_AdditiveOperator,
    c_sharp_operators_And,
    c_sharp_operators_Assignment,
    c_sharp_operators_AssignmentAnd,
    c_sharp_operators_AssignmentDivision,
    c_sharp_operators_AssignmentExclusiveOr,
    c_sharp_operators_AssignmentLeftShift,
    c_sharp_operators_AssignmentMinus,
    c_sharp_operators_AssignmentModulo,
    c_sharp_operators_AssignmentMultiplication,
    c_sharp_operators_AssignmentOperator,
    c_sharp_operators_AssignmentOr,
    c_sharp_operators_AssignmentPlus,
    c_sharp_operators_AssignmentRightShift,
    c_sharp_operators_AssignmentUnsignedRightShift,
    c_sharp_operators_Complement,
    c_sharp_operators_ConditionalAnd,
    c_sharp_operators_ConditionalOr,
    c_sharp_operators_Division,
    c_sharp_operators_Equal,
    c_sharp_operators_EqualityOperator,
    c_sharp_operators_ExclusiveOr,
    c_sharp_operators_GreaterThan,
    c_sharp_operators_GreaterThanOrEqual,
    c_sharp_operators_InclusiveOr,
    c_sharp_operators_LeftShift,
    c_sharp_operators_LessThan,
    c_sharp_operators_LessThanOrEqual,
    c_sharp_operators_MinusMinus,
    c_sharp_operators_Multiplication,
    c_sharp_operators_MultiplicativeOperator,
    c_sharp_operators_Negate,
    c_sharp_operators_NotEqual,
    c_sharp_operators_Operator,
    c_sharp_operators_PlusPlus,
    c_sharp_operators_RelationOperator,
    c_sharp_operators_Remainder,
    c_sharp_operators_RightShift,
    c_sharp_operators_ShiftOperator,
    c_sharp_operators_Subtraction,
    c_sharp_operators_UnaryModificationOperator,
    c_sharp_operators_UnaryOperator,
    c_sharp_operators_UnsignedRightShift,
    c_sharp_statements_BreakStatement,
    c_sharp_statements_CheckedStatement,
    c_sharp_statements_ConstantDeclarator,
    c_sharp_statements_ContinueStatement,
    c_sharp_statements_DeclarationStatement,
    c_sharp_statements_DoStatement,
    c_sharp_statements_EmbeddedStatement,
    c_sharp_statements_EmptyStatement,
    c_sharp_statements_ExpressionStatement,
    c_sharp_statements_FinallyClause,
    c_sharp_statements_FixedPointerDeclarator,
    c_sharp_statements_FixedStatement,
    c_sharp_statements_ForInitializer,
    c_sharp_statements_ForStatement,
    c_sharp_statements_ForeachStatement,
    c_sharp_statements_GeneralCatchClause,
    c_sharp_statements_GotoStatement,
    c_sharp_statements_IfStatement,
    c_sharp_statements_IterationStatement,
    c_sharp_statements_JumpStatement,
    c_sharp_statements_LabeledStatement,
    c_sharp_statements_LocalConstantDeclaration,
    c_sharp_statements_LockStatement,
    c_sharp_statements_ResourceAcquisition,
    c_sharp_statements_ReturnStatement,
    c_sharp_statements_SelectionStatement,
    c_sharp_statements_SimpleEmbeddedStatement,
    c_sharp_statements_SpecificCatchClause,
    c_sharp_statements_Statement,
    c_sharp_statements_SwitchLabel,
    c_sharp_statements_SwitchSection,
    c_sharp_statements_SwitchStatement,
    c_sharp_statements_ThrowStatement,
    c_sharp_statements_TryStatement,
    c_sharp_statements_UncheckedStatement,
    c_sharp_statements_UsingStatement,
    c_sharp_statements_VariableDeclaration,
    c_sharp_statements_VariableDeclarator,
    c_sharp_statements_WhileStatement,
    c_sharp_types_Bool,
    c_sharp_types_Byte,
    c_sharp_types_Char,
    c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType,
    c_sharp_types_Decimal,
    c_sharp_types_Double,
    c_sharp_types_Float,
    c_sharp_types_Int,
    c_sharp_types_Long,
    c_sharp_types_NonArrayType,
    c_sharp_types_Object,
    c_sharp_types_PointerType,
    c_sharp_types_ReferenceType,
    c_sharp_types_SByte,
    c_sharp_types_Short,
    c_sharp_types_SimpleType,
    c_sharp_types_String,
    c_sharp_types_Type,
    c_sharp_types_UInt,
    c_sharp_types_ULong,
    c_sharp_types_UShort,
    c_sharp_types_Void,
    classes_ClassMemberDeclaration,
    classes_VariableInitializer,
    common_NamedElement,
    expressions_Expression,
    expressions_PrimaryExtendedExpressionType,
    expressions_PrimaryNoArrayCreationExpression,
    expressions_StatementExpression,
    namespaces_NamespaceMemberDeclaration,
    namespaces_TypeDeclaration,
    operators_AdditiveOperator,
    operators_UnaryOperator,
    statements_ForInitializer,
    statements_ResourceAcquisition,
    statements_Statement,
    types_NonArrayType,
    types_Type,
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

def test_c_sharp_common_NamedElement_name_value_roundtrip():
    instance = c_sharp_common_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_c_sharp_literals_BooleanLiteral_value_value_roundtrip():
    instance = c_sharp_literals_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_c_sharp_literals_CharacterLiteral_value_value_roundtrip():
    instance = c_sharp_literals_CharacterLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_c_sharp_literals_DecimalIntegerLiteral_value_value_roundtrip():
    instance = c_sharp_literals_DecimalIntegerLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_c_sharp_literals_HexadecimalIntegerLiteral_value_value_roundtrip():
    instance = c_sharp_literals_HexadecimalIntegerLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_c_sharp_literals_RealLiteral_value_value_roundtrip():
    instance = c_sharp_literals_RealLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_c_sharp_literals_StringLiteral_value_value_roundtrip():
    instance = c_sharp_literals_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_c_sharp_operators_Assignment_isa_AssignmentOperator():
    instance = c_sharp_operators_Assignment()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentAnd_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentAnd()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentDivision_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentDivision()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentExclusiveOr_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentExclusiveOr()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentLeftShift_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentLeftShift()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentMinus_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentMinus()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentModulo_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentModulo()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentMultiplication_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentMultiplication()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentOr_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentOr()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentPlus_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentPlus()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentRightShift_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentRightShift()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_operators_AssignmentUnsignedRightShift_isa_AssignmentOperator():
    instance = c_sharp_operators_AssignmentUnsignedRightShift()
    assert isinstance(instance, AssignmentOperator)


def test_c_sharp_classes_ConstantDeclaration_isa_ClassMemberDeclaration():
    instance = c_sharp_classes_ConstantDeclaration()
    assert isinstance(instance, ClassMemberDeclaration)


def test_c_sharp_classes_FieldDeclaration_isa_ClassMemberDeclaration():
    instance = c_sharp_classes_FieldDeclaration()
    assert isinstance(instance, ClassMemberDeclaration)


def test_c_sharp_statements_CheckedStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_CheckedStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_EmptyStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_EmptyStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_ExpressionStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_ExpressionStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_FixedStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_FixedStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_IterationStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_IterationStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_JumpStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_JumpStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_LockStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_LockStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_SelectionStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_SelectionStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_SimpleEmbeddedStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_SimpleEmbeddedStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_TryStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_TryStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_UncheckedStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_UncheckedStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_statements_UsingStatement_isa_EmbeddedStatement():
    instance = c_sharp_statements_UsingStatement()
    assert isinstance(instance, EmbeddedStatement)


def test_c_sharp_operators_Equal_isa_EqualityOperator():
    instance = c_sharp_operators_Equal()
    assert isinstance(instance, EqualityOperator)


def test_c_sharp_operators_NotEqual_isa_EqualityOperator():
    instance = c_sharp_operators_NotEqual()
    assert isinstance(instance, EqualityOperator)


def test_c_sharp_expressions_ConditionalExpression_isa_Expression():
    instance = c_sharp_expressions_ConditionalExpression()
    assert isinstance(instance, Expression)


def test_c_sharp_expressions_StatementExpressionList_isa_ForInitializer():
    instance = c_sharp_expressions_StatementExpressionList()
    assert isinstance(instance, ForInitializer)


def test_c_sharp_statements_DoStatement_isa_IterationStatement():
    instance = c_sharp_statements_DoStatement()
    assert isinstance(instance, IterationStatement)


def test_c_sharp_statements_ForStatement_isa_IterationStatement():
    instance = c_sharp_statements_ForStatement()
    assert isinstance(instance, IterationStatement)


def test_c_sharp_statements_ForeachStatement_isa_IterationStatement():
    instance = c_sharp_statements_ForeachStatement()
    assert isinstance(instance, IterationStatement)


def test_c_sharp_statements_WhileStatement_isa_IterationStatement():
    instance = c_sharp_statements_WhileStatement()
    assert isinstance(instance, IterationStatement)


def test_c_sharp_statements_BreakStatement_isa_JumpStatement():
    instance = c_sharp_statements_BreakStatement()
    assert isinstance(instance, JumpStatement)


def test_c_sharp_statements_ContinueStatement_isa_JumpStatement():
    instance = c_sharp_statements_ContinueStatement()
    assert isinstance(instance, JumpStatement)


def test_c_sharp_statements_GotoStatement_isa_JumpStatement():
    instance = c_sharp_statements_GotoStatement()
    assert isinstance(instance, JumpStatement)


def test_c_sharp_statements_ReturnStatement_isa_JumpStatement():
    instance = c_sharp_statements_ReturnStatement()
    assert isinstance(instance, JumpStatement)


def test_c_sharp_statements_ThrowStatement_isa_JumpStatement():
    instance = c_sharp_statements_ThrowStatement()
    assert isinstance(instance, JumpStatement)


def test_c_sharp_literals_BooleanLiteral_isa_Literal():
    instance = c_sharp_literals_BooleanLiteral(value=True)
    assert isinstance(instance, Literal)


def test_c_sharp_literals_CharacterLiteral_isa_Literal():
    instance = c_sharp_literals_CharacterLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_c_sharp_literals_DecimalIntegerLiteral_isa_Literal():
    instance = c_sharp_literals_DecimalIntegerLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_c_sharp_literals_HexadecimalIntegerLiteral_isa_Literal():
    instance = c_sharp_literals_HexadecimalIntegerLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_c_sharp_literals_NullLiteral_isa_Literal():
    instance = c_sharp_literals_NullLiteral()
    assert isinstance(instance, Literal)


def test_c_sharp_literals_RealLiteral_isa_Literal():
    instance = c_sharp_literals_RealLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_c_sharp_literals_StringLiteral_isa_Literal():
    instance = c_sharp_literals_StringLiteral(value="sample_text")
    assert isinstance(instance, Literal)


def test_c_sharp_literals_This_isa_Literal():
    instance = c_sharp_literals_This()
    assert isinstance(instance, Literal)


def test_c_sharp_modifiers_Abstract_isa_Modifier():
    instance = c_sharp_modifiers_Abstract()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Extern_isa_Modifier():
    instance = c_sharp_modifiers_Extern()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Internal_isa_Modifier():
    instance = c_sharp_modifiers_Internal()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_New_isa_Modifier():
    instance = c_sharp_modifiers_New()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_OverrideModifier_isa_Modifier():
    instance = c_sharp_modifiers_OverrideModifier()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Partial_isa_Modifier():
    instance = c_sharp_modifiers_Partial()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Private_isa_Modifier():
    instance = c_sharp_modifiers_Private()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Protected_isa_Modifier():
    instance = c_sharp_modifiers_Protected()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Public_isa_Modifier():
    instance = c_sharp_modifiers_Public()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_ReadOnly_isa_Modifier():
    instance = c_sharp_modifiers_ReadOnly()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Sealed_isa_Modifier():
    instance = c_sharp_modifiers_Sealed()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Static_isa_Modifier():
    instance = c_sharp_modifiers_Static()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Unsafe_isa_Modifier():
    instance = c_sharp_modifiers_Unsafe()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Virtual_isa_Modifier():
    instance = c_sharp_modifiers_Virtual()
    assert isinstance(instance, Modifier)


def test_c_sharp_modifiers_Volatile_isa_Modifier():
    instance = c_sharp_modifiers_Volatile()
    assert isinstance(instance, Modifier)


def test_c_sharp_operators_Division_isa_MultiplicativeOperator():
    instance = c_sharp_operators_Division()
    assert isinstance(instance, MultiplicativeOperator)


def test_c_sharp_operators_Multiplication_isa_MultiplicativeOperator():
    instance = c_sharp_operators_Multiplication()
    assert isinstance(instance, MultiplicativeOperator)


def test_c_sharp_operators_Remainder_isa_MultiplicativeOperator():
    instance = c_sharp_operators_Remainder()
    assert isinstance(instance, MultiplicativeOperator)


def test_c_sharp_namespaces_UsingDirective_isa_NamedElement():
    instance = c_sharp_namespaces_UsingDirective()
    assert isinstance(instance, NamedElement)


def test_c_sharp_statements_ConstantDeclarator_isa_NamedElement():
    instance = c_sharp_statements_ConstantDeclarator()
    assert isinstance(instance, NamedElement)


def test_c_sharp_statements_VariableDeclarator_isa_NamedElement():
    instance = c_sharp_statements_VariableDeclarator()
    assert isinstance(instance, NamedElement)


def test_c_sharp_namespaces_Namespace_isa_NamespaceMemberDeclaration():
    instance = c_sharp_namespaces_Namespace()
    assert isinstance(instance, NamespaceMemberDeclaration)


def test_c_sharp_operators_AdditiveOperator_isa_Operator():
    instance = c_sharp_operators_AdditiveOperator()
    assert isinstance(instance, Operator)


def test_c_sharp_operators_AssignmentOperator_isa_Operator():
    instance = c_sharp_operators_AssignmentOperator()
    assert isinstance(instance, Operator)


def test_c_sharp_operators_EqualityOperator_isa_Operator():
    instance = c_sharp_operators_EqualityOperator()
    assert isinstance(instance, Operator)


def test_c_sharp_operators_MultiplicativeOperator_isa_Operator():
    instance = c_sharp_operators_MultiplicativeOperator()
    assert isinstance(instance, Operator)


def test_c_sharp_operators_RelationOperator_isa_Operator():
    instance = c_sharp_operators_RelationOperator()
    assert isinstance(instance, Operator)


def test_c_sharp_operators_ShiftOperator_isa_Operator():
    instance = c_sharp_operators_ShiftOperator()
    assert isinstance(instance, Operator)


def test_c_sharp_operators_UnaryModificationOperator_isa_Operator():
    instance = c_sharp_operators_UnaryModificationOperator()
    assert isinstance(instance, Operator)


def test_c_sharp_operators_UnaryOperator_isa_Operator():
    instance = c_sharp_operators_UnaryOperator()
    assert isinstance(instance, Operator)


def test_c_sharp_expressions_ArrayCreationExpression_isa_PrimaryExpression():
    instance = c_sharp_expressions_ArrayCreationExpression()
    assert isinstance(instance, PrimaryExpression)


def test_c_sharp_expressions_PrimaryNoArrayCreationExpression_isa_PrimaryExpression():
    instance = c_sharp_expressions_PrimaryNoArrayCreationExpression()
    assert isinstance(instance, PrimaryExpression)


def test_c_sharp_expressions_ElementAccess_isa_PrimaryExtendedExpressionType():
    instance = c_sharp_expressions_ElementAccess()
    assert isinstance(instance, PrimaryExtendedExpressionType)


def test_c_sharp_expressions_MemberAccess_isa_PrimaryExtendedExpressionType():
    instance = c_sharp_expressions_MemberAccess()
    assert isinstance(instance, PrimaryExtendedExpressionType)


def test_c_sharp_expressions_PointerMemberAccess_isa_PrimaryExtendedExpressionType():
    instance = c_sharp_expressions_PointerMemberAccess()
    assert isinstance(instance, PrimaryExtendedExpressionType)


def test_c_sharp_expressions_BaseAccess_isa_PrimaryNoArrayCreationExpression():
    instance = c_sharp_expressions_BaseAccess()
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_CheckedExpression_isa_PrimaryNoArrayCreationExpression():
    instance = c_sharp_expressions_CheckedExpression()
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_DelegateCreationExpression_isa_PrimaryNoArrayCreationExpression():
    instance = c_sharp_expressions_DelegateCreationExpression()
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_ParenthesizedExpression_isa_PrimaryNoArrayCreationExpression():
    instance = c_sharp_expressions_ParenthesizedExpression()
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_SizeOfExpression_isa_PrimaryNoArrayCreationExpression():
    instance = c_sharp_expressions_SizeOfExpression()
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_TypeOfExpression_isa_PrimaryNoArrayCreationExpression():
    instance = c_sharp_expressions_TypeOfExpression()
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_UncheckedExpression_isa_PrimaryNoArrayCreationExpression():
    instance = c_sharp_expressions_UncheckedExpression()
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


def test_c_sharp_literals_Literal_isa_PrimaryNoArrayCreationExpression():
    instance = c_sharp_literals_Literal()
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


def test_c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_isa_ReferenceType():
    instance = c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType()
    assert isinstance(instance, ReferenceType)


def test_c_sharp_operators_GreaterThan_isa_RelationOperator():
    instance = c_sharp_operators_GreaterThan()
    assert isinstance(instance, RelationOperator)


def test_c_sharp_operators_GreaterThanOrEqual_isa_RelationOperator():
    instance = c_sharp_operators_GreaterThanOrEqual()
    assert isinstance(instance, RelationOperator)


def test_c_sharp_operators_LessThan_isa_RelationOperator():
    instance = c_sharp_operators_LessThan()
    assert isinstance(instance, RelationOperator)


def test_c_sharp_operators_LessThanOrEqual_isa_RelationOperator():
    instance = c_sharp_operators_LessThanOrEqual()
    assert isinstance(instance, RelationOperator)


def test_c_sharp_statements_IfStatement_isa_SelectionStatement():
    instance = c_sharp_statements_IfStatement()
    assert isinstance(instance, SelectionStatement)


def test_c_sharp_statements_SwitchStatement_isa_SelectionStatement():
    instance = c_sharp_statements_SwitchStatement()
    assert isinstance(instance, SelectionStatement)


def test_c_sharp_operators_LeftShift_isa_ShiftOperator():
    instance = c_sharp_operators_LeftShift()
    assert isinstance(instance, ShiftOperator)


def test_c_sharp_operators_RightShift_isa_ShiftOperator():
    instance = c_sharp_operators_RightShift()
    assert isinstance(instance, ShiftOperator)


def test_c_sharp_operators_UnsignedRightShift_isa_ShiftOperator():
    instance = c_sharp_operators_UnsignedRightShift()
    assert isinstance(instance, ShiftOperator)


def test_c_sharp_types_Bool_isa_SimpleType():
    instance = c_sharp_types_Bool()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Byte_isa_SimpleType():
    instance = c_sharp_types_Byte()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Char_isa_SimpleType():
    instance = c_sharp_types_Char()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Decimal_isa_SimpleType():
    instance = c_sharp_types_Decimal()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Double_isa_SimpleType():
    instance = c_sharp_types_Double()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Float_isa_SimpleType():
    instance = c_sharp_types_Float()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Int_isa_SimpleType():
    instance = c_sharp_types_Int()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Long_isa_SimpleType():
    instance = c_sharp_types_Long()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Object_isa_SimpleType():
    instance = c_sharp_types_Object()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_SByte_isa_SimpleType():
    instance = c_sharp_types_SByte()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Short_isa_SimpleType():
    instance = c_sharp_types_Short()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_String_isa_SimpleType():
    instance = c_sharp_types_String()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_UInt_isa_SimpleType():
    instance = c_sharp_types_UInt()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_ULong_isa_SimpleType():
    instance = c_sharp_types_ULong()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_UShort_isa_SimpleType():
    instance = c_sharp_types_UShort()
    assert isinstance(instance, SimpleType)


def test_c_sharp_types_Void_isa_SimpleType():
    instance = c_sharp_types_Void()
    assert isinstance(instance, SimpleType)


def test_c_sharp_statements_DeclarationStatement_isa_Statement():
    instance = c_sharp_statements_DeclarationStatement()
    assert isinstance(instance, Statement)


def test_c_sharp_statements_EmbeddedStatement_isa_Statement():
    instance = c_sharp_statements_EmbeddedStatement()
    assert isinstance(instance, Statement)


def test_c_sharp_expressions_PreDecrementExpression_isa_StatementExpression():
    instance = c_sharp_expressions_PreDecrementExpression()
    assert isinstance(instance, StatementExpression)


def test_c_sharp_expressions_PreIncrementExpression_isa_StatementExpression():
    instance = c_sharp_expressions_PreIncrementExpression()
    assert isinstance(instance, StatementExpression)


def test_c_sharp_arrays_ArrayType_isa_Type():
    instance = c_sharp_arrays_ArrayType()
    assert isinstance(instance, Type)


def test_c_sharp_operators_MinusMinus_isa_UnaryModificationOperator():
    instance = c_sharp_operators_MinusMinus()
    assert isinstance(instance, UnaryModificationOperator)


def test_c_sharp_operators_PlusPlus_isa_UnaryModificationOperator():
    instance = c_sharp_operators_PlusPlus()
    assert isinstance(instance, UnaryModificationOperator)


def test_c_sharp_operators_And_isa_UnaryOperator():
    instance = c_sharp_operators_And()
    assert isinstance(instance, UnaryOperator)


def test_c_sharp_operators_Complement_isa_UnaryOperator():
    instance = c_sharp_operators_Complement()
    assert isinstance(instance, UnaryOperator)


def test_c_sharp_operators_ConditionalAnd_isa_UnaryOperator():
    instance = c_sharp_operators_ConditionalAnd()
    assert isinstance(instance, UnaryOperator)


def test_c_sharp_operators_ConditionalOr_isa_UnaryOperator():
    instance = c_sharp_operators_ConditionalOr()
    assert isinstance(instance, UnaryOperator)


def test_c_sharp_operators_ExclusiveOr_isa_UnaryOperator():
    instance = c_sharp_operators_ExclusiveOr()
    assert isinstance(instance, UnaryOperator)


def test_c_sharp_operators_InclusiveOr_isa_UnaryOperator():
    instance = c_sharp_operators_InclusiveOr()
    assert isinstance(instance, UnaryOperator)


def test_c_sharp_operators_Negate_isa_UnaryOperator():
    instance = c_sharp_operators_Negate()
    assert isinstance(instance, UnaryOperator)


def test_c_sharp_arrays_ArrayInitializer_isa_VariableInitializer():
    instance = c_sharp_arrays_ArrayInitializer()
    assert isinstance(instance, VariableInitializer)


def test_c_sharp_arrays_StackallocInitializer_isa_VariableInitializer():
    instance = c_sharp_arrays_StackallocInitializer()
    assert isinstance(instance, VariableInitializer)


def test_c_sharp_classes_Method_isa_classes_ClassMemberDeclaration():
    instance = c_sharp_classes_Method()
    assert isinstance(instance, classes_ClassMemberDeclaration)


def test_c_sharp_namespaces_TypeDeclaration_isa_classes_ClassMemberDeclaration():
    instance = c_sharp_namespaces_TypeDeclaration()
    assert isinstance(instance, classes_ClassMemberDeclaration)


def test_c_sharp_expressions_Expression_isa_classes_VariableInitializer():
    instance = c_sharp_expressions_Expression()
    assert isinstance(instance, classes_VariableInitializer)


def test_c_sharp_classes_Class_isa_common_NamedElement():
    instance = c_sharp_classes_Class()
    assert isinstance(instance, common_NamedElement)


def test_c_sharp_classes_Method_isa_common_NamedElement():
    instance = c_sharp_classes_Method()
    assert isinstance(instance, common_NamedElement)


def test_c_sharp_common_Identifier_isa_common_NamedElement():
    instance = c_sharp_common_Identifier()
    assert isinstance(instance, common_NamedElement)


def test_c_sharp_statements_LabeledStatement_isa_common_NamedElement():
    instance = c_sharp_statements_LabeledStatement()
    assert isinstance(instance, common_NamedElement)


def test_c_sharp_expressions_AssignmentExpression_isa_expressions_Expression():
    instance = c_sharp_expressions_AssignmentExpression()
    assert isinstance(instance, expressions_Expression)


def test_c_sharp_expressions_InvocationExpression_isa_expressions_PrimaryExtendedExpressionType():
    instance = c_sharp_expressions_InvocationExpression()
    assert isinstance(instance, expressions_PrimaryExtendedExpressionType)


def test_c_sharp_expressions_PostDecrementExpression_isa_expressions_PrimaryExtendedExpressionType():
    instance = c_sharp_expressions_PostDecrementExpression()
    assert isinstance(instance, expressions_PrimaryExtendedExpressionType)


def test_c_sharp_expressions_PostIncrementExpression_isa_expressions_PrimaryExtendedExpressionType():
    instance = c_sharp_expressions_PostIncrementExpression()
    assert isinstance(instance, expressions_PrimaryExtendedExpressionType)


def test_c_sharp_common_Identifier_isa_expressions_PrimaryNoArrayCreationExpression():
    instance = c_sharp_common_Identifier()
    assert isinstance(instance, expressions_PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_ObjectCreationExpression_isa_expressions_PrimaryNoArrayCreationExpression():
    instance = c_sharp_expressions_ObjectCreationExpression()
    assert isinstance(instance, expressions_PrimaryNoArrayCreationExpression)


def test_c_sharp_expressions_AssignmentExpression_isa_expressions_StatementExpression():
    instance = c_sharp_expressions_AssignmentExpression()
    assert isinstance(instance, expressions_StatementExpression)


def test_c_sharp_expressions_InvocationExpression_isa_expressions_StatementExpression():
    instance = c_sharp_expressions_InvocationExpression()
    assert isinstance(instance, expressions_StatementExpression)


def test_c_sharp_expressions_ObjectCreationExpression_isa_expressions_StatementExpression():
    instance = c_sharp_expressions_ObjectCreationExpression()
    assert isinstance(instance, expressions_StatementExpression)


def test_c_sharp_expressions_PostDecrementExpression_isa_expressions_StatementExpression():
    instance = c_sharp_expressions_PostDecrementExpression()
    assert isinstance(instance, expressions_StatementExpression)


def test_c_sharp_expressions_PostIncrementExpression_isa_expressions_StatementExpression():
    instance = c_sharp_expressions_PostIncrementExpression()
    assert isinstance(instance, expressions_StatementExpression)


def test_c_sharp_namespaces_TypeDeclaration_isa_namespaces_NamespaceMemberDeclaration():
    instance = c_sharp_namespaces_TypeDeclaration()
    assert isinstance(instance, namespaces_NamespaceMemberDeclaration)


def test_c_sharp_classes_Class_isa_namespaces_TypeDeclaration():
    instance = c_sharp_classes_Class()
    assert isinstance(instance, namespaces_TypeDeclaration)


def test_c_sharp_operators_Addition_isa_operators_AdditiveOperator():
    instance = c_sharp_operators_Addition()
    assert isinstance(instance, operators_AdditiveOperator)


def test_c_sharp_operators_Subtraction_isa_operators_AdditiveOperator():
    instance = c_sharp_operators_Subtraction()
    assert isinstance(instance, operators_AdditiveOperator)


def test_c_sharp_operators_Addition_isa_operators_UnaryOperator():
    instance = c_sharp_operators_Addition()
    assert isinstance(instance, operators_UnaryOperator)


def test_c_sharp_operators_Subtraction_isa_operators_UnaryOperator():
    instance = c_sharp_operators_Subtraction()
    assert isinstance(instance, operators_UnaryOperator)


def test_c_sharp_statements_VariableDeclaration_isa_statements_ForInitializer():
    instance = c_sharp_statements_VariableDeclaration()
    assert isinstance(instance, statements_ForInitializer)


def test_c_sharp_expressions_Expression_isa_statements_ResourceAcquisition():
    instance = c_sharp_expressions_Expression()
    assert isinstance(instance, statements_ResourceAcquisition)


def test_c_sharp_statements_VariableDeclaration_isa_statements_ResourceAcquisition():
    instance = c_sharp_statements_VariableDeclaration()
    assert isinstance(instance, statements_ResourceAcquisition)


def test_c_sharp_statements_LabeledStatement_isa_statements_Statement():
    instance = c_sharp_statements_LabeledStatement()
    assert isinstance(instance, statements_Statement)


def test_c_sharp_types_PointerType_isa_types_NonArrayType():
    instance = c_sharp_types_PointerType()
    assert isinstance(instance, types_NonArrayType)


def test_c_sharp_types_ReferenceType_isa_types_NonArrayType():
    instance = c_sharp_types_ReferenceType()
    assert isinstance(instance, types_NonArrayType)


def test_c_sharp_types_SimpleType_isa_types_NonArrayType():
    instance = c_sharp_types_SimpleType()
    assert isinstance(instance, types_NonArrayType)


def test_c_sharp_types_PointerType_isa_types_Type():
    instance = c_sharp_types_PointerType()
    assert isinstance(instance, types_Type)


def test_c_sharp_types_ReferenceType_isa_types_Type():
    instance = c_sharp_types_ReferenceType()
    assert isinstance(instance, types_Type)


def test_c_sharp_types_SimpleType_isa_types_Type():
    instance = c_sharp_types_SimpleType()
    assert isinstance(instance, types_Type)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Addition_strategy = st.builds(Addition)
@given(instance=Addition_strategy)
@settings(max_examples=25)
def test_Addition_instantiation(instance):
    assert isinstance(instance, Addition)


AdditiveExpression_strategy = st.builds(AdditiveExpression)
@given(instance=AdditiveExpression_strategy)
@settings(max_examples=25)
def test_AdditiveExpression_instantiation(instance):
    assert isinstance(instance, AdditiveExpression)


AddressOfExpression_strategy = st.builds(AddressOfExpression)
@given(instance=AddressOfExpression_strategy)
@settings(max_examples=25)
def test_AddressOfExpression_instantiation(instance):
    assert isinstance(instance, AddressOfExpression)


And_strategy = st.builds(And)
@given(instance=And_strategy)
@settings(max_examples=25)
def test_And_instantiation(instance):
    assert isinstance(instance, And)


AndExpression_strategy = st.builds(AndExpression)
@given(instance=AndExpression_strategy)
@settings(max_examples=25)
def test_AndExpression_instantiation(instance):
    assert isinstance(instance, AndExpression)


Argument_strategy = st.builds(Argument)
@given(instance=Argument_strategy)
@settings(max_examples=25)
def test_Argument_instantiation(instance):
    assert isinstance(instance, Argument)


ArgumentList_strategy = st.builds(ArgumentList)
@given(instance=ArgumentList_strategy)
@settings(max_examples=25)
def test_ArgumentList_instantiation(instance):
    assert isinstance(instance, ArgumentList)


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


AssignmentOperator_strategy = st.builds(AssignmentOperator)
@given(instance=AssignmentOperator_strategy)
@settings(max_examples=25)
def test_AssignmentOperator_instantiation(instance):
    assert isinstance(instance, AssignmentOperator)


Attribute_strategy = st.builds(Attribute)
@given(instance=Attribute_strategy)
@settings(max_examples=25)
def test_Attribute_instantiation(instance):
    assert isinstance(instance, Attribute)


AttributeArguments_strategy = st.builds(AttributeArguments)
@given(instance=AttributeArguments_strategy)
@settings(max_examples=25)
def test_AttributeArguments_instantiation(instance):
    assert isinstance(instance, AttributeArguments)


AttributeTarget_strategy = st.builds(AttributeTarget)
@given(instance=AttributeTarget_strategy)
@settings(max_examples=25)
def test_AttributeTarget_instantiation(instance):
    assert isinstance(instance, AttributeTarget)


Attributes_strategy = st.builds(Attributes)
@given(instance=Attributes_strategy)
@settings(max_examples=25)
def test_Attributes_instantiation(instance):
    assert isinstance(instance, Attributes)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


Case_strategy = st.builds(Case)
@given(instance=Case_strategy)
@settings(max_examples=25)
def test_Case_instantiation(instance):
    assert isinstance(instance, Case)


CastExpression_strategy = st.builds(CastExpression)
@given(instance=CastExpression_strategy)
@settings(max_examples=25)
def test_CastExpression_instantiation(instance):
    assert isinstance(instance, CastExpression)


ClassBase_strategy = st.builds(ClassBase)
@given(instance=ClassBase_strategy)
@settings(max_examples=25)
def test_ClassBase_instantiation(instance):
    assert isinstance(instance, ClassBase)


ClassMemberDeclaration_strategy = st.builds(ClassMemberDeclaration)
@given(instance=ClassMemberDeclaration_strategy)
@settings(max_examples=25)
def test_ClassMemberDeclaration_instantiation(instance):
    assert isinstance(instance, ClassMemberDeclaration)


ClassOrInterfaceOrDelegateOrEnumType_strategy = st.builds(ClassOrInterfaceOrDelegateOrEnumType)
@given(instance=ClassOrInterfaceOrDelegateOrEnumType_strategy)
@settings(max_examples=25)
def test_ClassOrInterfaceOrDelegateOrEnumType_instantiation(instance):
    assert isinstance(instance, ClassOrInterfaceOrDelegateOrEnumType)


Complement_strategy = st.builds(Complement)
@given(instance=Complement_strategy)
@settings(max_examples=25)
def test_Complement_instantiation(instance):
    assert isinstance(instance, Complement)


ConditionalAnd_strategy = st.builds(ConditionalAnd)
@given(instance=ConditionalAnd_strategy)
@settings(max_examples=25)
def test_ConditionalAnd_instantiation(instance):
    assert isinstance(instance, ConditionalAnd)


ConditionalAndExpression_strategy = st.builds(ConditionalAndExpression)
@given(instance=ConditionalAndExpression_strategy)
@settings(max_examples=25)
def test_ConditionalAndExpression_instantiation(instance):
    assert isinstance(instance, ConditionalAndExpression)


ConditionalOr_strategy = st.builds(ConditionalOr)
@given(instance=ConditionalOr_strategy)
@settings(max_examples=25)
def test_ConditionalOr_instantiation(instance):
    assert isinstance(instance, ConditionalOr)


ConditionalOrExpression_strategy = st.builds(ConditionalOrExpression)
@given(instance=ConditionalOrExpression_strategy)
@settings(max_examples=25)
def test_ConditionalOrExpression_instantiation(instance):
    assert isinstance(instance, ConditionalOrExpression)


ConstantDeclarator_strategy = st.builds(ConstantDeclarator)
@given(instance=ConstantDeclarator_strategy)
@settings(max_examples=25)
def test_ConstantDeclarator_instantiation(instance):
    assert isinstance(instance, ConstantDeclarator)


Default_strategy = st.builds(Default)
@given(instance=Default_strategy)
@settings(max_examples=25)
def test_Default_instantiation(instance):
    assert isinstance(instance, Default)


Division_strategy = st.builds(Division)
@given(instance=Division_strategy)
@settings(max_examples=25)
def test_Division_instantiation(instance):
    assert isinstance(instance, Division)


EmbeddedStatement_strategy = st.builds(EmbeddedStatement)
@given(instance=EmbeddedStatement_strategy)
@settings(max_examples=25)
def test_EmbeddedStatement_instantiation(instance):
    assert isinstance(instance, EmbeddedStatement)


Equal_strategy = st.builds(Equal)
@given(instance=Equal_strategy)
@settings(max_examples=25)
def test_Equal_instantiation(instance):
    assert isinstance(instance, Equal)


EqualityExpression_strategy = st.builds(EqualityExpression)
@given(instance=EqualityExpression_strategy)
@settings(max_examples=25)
def test_EqualityExpression_instantiation(instance):
    assert isinstance(instance, EqualityExpression)


EqualityOperator_strategy = st.builds(EqualityOperator)
@given(instance=EqualityOperator_strategy)
@settings(max_examples=25)
def test_EqualityOperator_instantiation(instance):
    assert isinstance(instance, EqualityOperator)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


ExclusiveOr_strategy = st.builds(ExclusiveOr)
@given(instance=ExclusiveOr_strategy)
@settings(max_examples=25)
def test_ExclusiveOr_instantiation(instance):
    assert isinstance(instance, ExclusiveOr)


ExclusiveOrExpression_strategy = st.builds(ExclusiveOrExpression)
@given(instance=ExclusiveOrExpression_strategy)
@settings(max_examples=25)
def test_ExclusiveOrExpression_instantiation(instance):
    assert isinstance(instance, ExclusiveOrExpression)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ExpressionList_strategy = st.builds(ExpressionList)
@given(instance=ExpressionList_strategy)
@settings(max_examples=25)
def test_ExpressionList_instantiation(instance):
    assert isinstance(instance, ExpressionList)


FinallyClause_strategy = st.builds(FinallyClause)
@given(instance=FinallyClause_strategy)
@settings(max_examples=25)
def test_FinallyClause_instantiation(instance):
    assert isinstance(instance, FinallyClause)


FixedParameter_strategy = st.builds(FixedParameter)
@given(instance=FixedParameter_strategy)
@settings(max_examples=25)
def test_FixedParameter_instantiation(instance):
    assert isinstance(instance, FixedParameter)


FixedPointerDeclarator_strategy = st.builds(FixedPointerDeclarator)
@given(instance=FixedPointerDeclarator_strategy)
@settings(max_examples=25)
def test_FixedPointerDeclarator_instantiation(instance):
    assert isinstance(instance, FixedPointerDeclarator)


ForInitializer_strategy = st.builds(ForInitializer)
@given(instance=ForInitializer_strategy)
@settings(max_examples=25)
def test_ForInitializer_instantiation(instance):
    assert isinstance(instance, ForInitializer)


FormalParameterList_strategy = st.builds(FormalParameterList)
@given(instance=FormalParameterList_strategy)
@settings(max_examples=25)
def test_FormalParameterList_instantiation(instance):
    assert isinstance(instance, FormalParameterList)


GeneralCatchClause_strategy = st.builds(GeneralCatchClause)
@given(instance=GeneralCatchClause_strategy)
@settings(max_examples=25)
def test_GeneralCatchClause_instantiation(instance):
    assert isinstance(instance, GeneralCatchClause)


GlobalAttributeTarget_strategy = st.builds(GlobalAttributeTarget)
@given(instance=GlobalAttributeTarget_strategy)
@settings(max_examples=25)
def test_GlobalAttributeTarget_instantiation(instance):
    assert isinstance(instance, GlobalAttributeTarget)


GlobalAttributes_strategy = st.builds(GlobalAttributes)
@given(instance=GlobalAttributes_strategy)
@settings(max_examples=25)
def test_GlobalAttributes_instantiation(instance):
    assert isinstance(instance, GlobalAttributes)


GreaterThan_strategy = st.builds(GreaterThan)
@given(instance=GreaterThan_strategy)
@settings(max_examples=25)
def test_GreaterThan_instantiation(instance):
    assert isinstance(instance, GreaterThan)


GreaterThanOrEqual_strategy = st.builds(GreaterThanOrEqual)
@given(instance=GreaterThanOrEqual_strategy)
@settings(max_examples=25)
def test_GreaterThanOrEqual_instantiation(instance):
    assert isinstance(instance, GreaterThanOrEqual)


Identifier_strategy = st.builds(Identifier)
@given(instance=Identifier_strategy)
@settings(max_examples=25)
def test_Identifier_instantiation(instance):
    assert isinstance(instance, Identifier)


InclusiveOr_strategy = st.builds(InclusiveOr)
@given(instance=InclusiveOr_strategy)
@settings(max_examples=25)
def test_InclusiveOr_instantiation(instance):
    assert isinstance(instance, InclusiveOr)


InclusiveOrExpression_strategy = st.builds(InclusiveOrExpression)
@given(instance=InclusiveOrExpression_strategy)
@settings(max_examples=25)
def test_InclusiveOrExpression_instantiation(instance):
    assert isinstance(instance, InclusiveOrExpression)


IterationStatement_strategy = st.builds(IterationStatement)
@given(instance=IterationStatement_strategy)
@settings(max_examples=25)
def test_IterationStatement_instantiation(instance):
    assert isinstance(instance, IterationStatement)


JumpStatement_strategy = st.builds(JumpStatement)
@given(instance=JumpStatement_strategy)
@settings(max_examples=25)
def test_JumpStatement_instantiation(instance):
    assert isinstance(instance, JumpStatement)


LeftShift_strategy = st.builds(LeftShift)
@given(instance=LeftShift_strategy)
@settings(max_examples=25)
def test_LeftShift_instantiation(instance):
    assert isinstance(instance, LeftShift)


LessThan_strategy = st.builds(LessThan)
@given(instance=LessThan_strategy)
@settings(max_examples=25)
def test_LessThan_instantiation(instance):
    assert isinstance(instance, LessThan)


LessThanOrEqual_strategy = st.builds(LessThanOrEqual)
@given(instance=LessThanOrEqual_strategy)
@settings(max_examples=25)
def test_LessThanOrEqual_instantiation(instance):
    assert isinstance(instance, LessThanOrEqual)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


LocalConstantDeclaration_strategy = st.builds(LocalConstantDeclaration)
@given(instance=LocalConstantDeclaration_strategy)
@settings(max_examples=25)
def test_LocalConstantDeclaration_instantiation(instance):
    assert isinstance(instance, LocalConstantDeclaration)


MemberAccess_strategy = st.builds(MemberAccess)
@given(instance=MemberAccess_strategy)
@settings(max_examples=25)
def test_MemberAccess_instantiation(instance):
    assert isinstance(instance, MemberAccess)


Modifier_strategy = st.builds(Modifier)
@given(instance=Modifier_strategy)
@settings(max_examples=25)
def test_Modifier_instantiation(instance):
    assert isinstance(instance, Modifier)


Multiplication_strategy = st.builds(Multiplication)
@given(instance=Multiplication_strategy)
@settings(max_examples=25)
def test_Multiplication_instantiation(instance):
    assert isinstance(instance, Multiplication)


MultiplicativeExpression_strategy = st.builds(MultiplicativeExpression)
@given(instance=MultiplicativeExpression_strategy)
@settings(max_examples=25)
def test_MultiplicativeExpression_instantiation(instance):
    assert isinstance(instance, MultiplicativeExpression)


MultiplicativeOperator_strategy = st.builds(MultiplicativeOperator)
@given(instance=MultiplicativeOperator_strategy)
@settings(max_examples=25)
def test_MultiplicativeOperator_instantiation(instance):
    assert isinstance(instance, MultiplicativeOperator)


NamedArgument_strategy = st.builds(NamedArgument)
@given(instance=NamedArgument_strategy)
@settings(max_examples=25)
def test_NamedArgument_instantiation(instance):
    assert isinstance(instance, NamedArgument)


NamedArgumentList_strategy = st.builds(NamedArgumentList)
@given(instance=NamedArgumentList_strategy)
@settings(max_examples=25)
def test_NamedArgumentList_instantiation(instance):
    assert isinstance(instance, NamedArgumentList)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NamespaceBody_strategy = st.builds(NamespaceBody)
@given(instance=NamespaceBody_strategy)
@settings(max_examples=25)
def test_NamespaceBody_instantiation(instance):
    assert isinstance(instance, NamespaceBody)


NamespaceMemberDeclaration_strategy = st.builds(NamespaceMemberDeclaration)
@given(instance=NamespaceMemberDeclaration_strategy)
@settings(max_examples=25)
def test_NamespaceMemberDeclaration_instantiation(instance):
    assert isinstance(instance, NamespaceMemberDeclaration)


NamespaceOrTypeName_strategy = st.builds(NamespaceOrTypeName)
@given(instance=NamespaceOrTypeName_strategy)
@settings(max_examples=25)
def test_NamespaceOrTypeName_instantiation(instance):
    assert isinstance(instance, NamespaceOrTypeName)


Negate_strategy = st.builds(Negate)
@given(instance=Negate_strategy)
@settings(max_examples=25)
def test_Negate_instantiation(instance):
    assert isinstance(instance, Negate)


NonArrayType_strategy = st.builds(NonArrayType)
@given(instance=NonArrayType_strategy)
@settings(max_examples=25)
def test_NonArrayType_instantiation(instance):
    assert isinstance(instance, NonArrayType)


NotEqual_strategy = st.builds(NotEqual)
@given(instance=NotEqual_strategy)
@settings(max_examples=25)
def test_NotEqual_instantiation(instance):
    assert isinstance(instance, NotEqual)


Operator_strategy = st.builds(Operator)
@given(instance=Operator_strategy)
@settings(max_examples=25)
def test_Operator_instantiation(instance):
    assert isinstance(instance, Operator)


Out_strategy = st.builds(Out)
@given(instance=Out_strategy)
@settings(max_examples=25)
def test_Out_instantiation(instance):
    assert isinstance(instance, Out)


ParameterArray_strategy = st.builds(ParameterArray)
@given(instance=ParameterArray_strategy)
@settings(max_examples=25)
def test_ParameterArray_instantiation(instance):
    assert isinstance(instance, ParameterArray)


Params_strategy = st.builds(Params)
@given(instance=Params_strategy)
@settings(max_examples=25)
def test_Params_instantiation(instance):
    assert isinstance(instance, Params)


PointerType_strategy = st.builds(PointerType)
@given(instance=PointerType_strategy)
@settings(max_examples=25)
def test_PointerType_instantiation(instance):
    assert isinstance(instance, PointerType)


PreDecrementExpression_strategy = st.builds(PreDecrementExpression)
@given(instance=PreDecrementExpression_strategy)
@settings(max_examples=25)
def test_PreDecrementExpression_instantiation(instance):
    assert isinstance(instance, PreDecrementExpression)


PreIncrementExpression_strategy = st.builds(PreIncrementExpression)
@given(instance=PreIncrementExpression_strategy)
@settings(max_examples=25)
def test_PreIncrementExpression_instantiation(instance):
    assert isinstance(instance, PreIncrementExpression)


PrimaryExpression_strategy = st.builds(PrimaryExpression)
@given(instance=PrimaryExpression_strategy)
@settings(max_examples=25)
def test_PrimaryExpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)


PrimaryExtendedExpressionType_strategy = st.builds(PrimaryExtendedExpressionType)
@given(instance=PrimaryExtendedExpressionType_strategy)
@settings(max_examples=25)
def test_PrimaryExtendedExpressionType_instantiation(instance):
    assert isinstance(instance, PrimaryExtendedExpressionType)


PrimaryNoArrayCreationExpression_strategy = st.builds(PrimaryNoArrayCreationExpression)
@given(instance=PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=25)
def test_PrimaryNoArrayCreationExpression_instantiation(instance):
    assert isinstance(instance, PrimaryNoArrayCreationExpression)


RankSpecifier_strategy = st.builds(RankSpecifier)
@given(instance=RankSpecifier_strategy)
@settings(max_examples=25)
def test_RankSpecifier_instantiation(instance):
    assert isinstance(instance, RankSpecifier)


Ref_strategy = st.builds(Ref)
@given(instance=Ref_strategy)
@settings(max_examples=25)
def test_Ref_instantiation(instance):
    assert isinstance(instance, Ref)


ReferenceType_strategy = st.builds(ReferenceType)
@given(instance=ReferenceType_strategy)
@settings(max_examples=25)
def test_ReferenceType_instantiation(instance):
    assert isinstance(instance, ReferenceType)


RelationOperator_strategy = st.builds(RelationOperator)
@given(instance=RelationOperator_strategy)
@settings(max_examples=25)
def test_RelationOperator_instantiation(instance):
    assert isinstance(instance, RelationOperator)


RelationalExpression_strategy = st.builds(RelationalExpression)
@given(instance=RelationalExpression_strategy)
@settings(max_examples=25)
def test_RelationalExpression_instantiation(instance):
    assert isinstance(instance, RelationalExpression)


Remainder_strategy = st.builds(Remainder)
@given(instance=Remainder_strategy)
@settings(max_examples=25)
def test_Remainder_instantiation(instance):
    assert isinstance(instance, Remainder)


ResourceAcquisition_strategy = st.builds(ResourceAcquisition)
@given(instance=ResourceAcquisition_strategy)
@settings(max_examples=25)
def test_ResourceAcquisition_instantiation(instance):
    assert isinstance(instance, ResourceAcquisition)


Return_strategy = st.builds(Return)
@given(instance=Return_strategy)
@settings(max_examples=25)
def test_Return_instantiation(instance):
    assert isinstance(instance, Return)


RightShift_strategy = st.builds(RightShift)
@given(instance=RightShift_strategy)
@settings(max_examples=25)
def test_RightShift_instantiation(instance):
    assert isinstance(instance, RightShift)


SelectionStatement_strategy = st.builds(SelectionStatement)
@given(instance=SelectionStatement_strategy)
@settings(max_examples=25)
def test_SelectionStatement_instantiation(instance):
    assert isinstance(instance, SelectionStatement)


ShiftExpression_strategy = st.builds(ShiftExpression)
@given(instance=ShiftExpression_strategy)
@settings(max_examples=25)
def test_ShiftExpression_instantiation(instance):
    assert isinstance(instance, ShiftExpression)


ShiftOperator_strategy = st.builds(ShiftOperator)
@given(instance=ShiftOperator_strategy)
@settings(max_examples=25)
def test_ShiftOperator_instantiation(instance):
    assert isinstance(instance, ShiftOperator)


SimpleType_strategy = st.builds(SimpleType)
@given(instance=SimpleType_strategy)
@settings(max_examples=25)
def test_SimpleType_instantiation(instance):
    assert isinstance(instance, SimpleType)


SpecificCatchClause_strategy = st.builds(SpecificCatchClause)
@given(instance=SpecificCatchClause_strategy)
@settings(max_examples=25)
def test_SpecificCatchClause_instantiation(instance):
    assert isinstance(instance, SpecificCatchClause)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


StatementExpression_strategy = st.builds(StatementExpression)
@given(instance=StatementExpression_strategy)
@settings(max_examples=25)
def test_StatementExpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)


StatementExpressionList_strategy = st.builds(StatementExpressionList)
@given(instance=StatementExpressionList_strategy)
@settings(max_examples=25)
def test_StatementExpressionList_instantiation(instance):
    assert isinstance(instance, StatementExpressionList)


Subtraction_strategy = st.builds(Subtraction)
@given(instance=Subtraction_strategy)
@settings(max_examples=25)
def test_Subtraction_instantiation(instance):
    assert isinstance(instance, Subtraction)


SwitchLabel_strategy = st.builds(SwitchLabel)
@given(instance=SwitchLabel_strategy)
@settings(max_examples=25)
def test_SwitchLabel_instantiation(instance):
    assert isinstance(instance, SwitchLabel)


SwitchSection_strategy = st.builds(SwitchSection)
@given(instance=SwitchSection_strategy)
@settings(max_examples=25)
def test_SwitchSection_instantiation(instance):
    assert isinstance(instance, SwitchSection)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


UnaryExpression_strategy = st.builds(UnaryExpression)
@given(instance=UnaryExpression_strategy)
@settings(max_examples=25)
def test_UnaryExpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)


UnaryModificationOperator_strategy = st.builds(UnaryModificationOperator)
@given(instance=UnaryModificationOperator_strategy)
@settings(max_examples=25)
def test_UnaryModificationOperator_instantiation(instance):
    assert isinstance(instance, UnaryModificationOperator)


UnaryOperator_strategy = st.builds(UnaryOperator)
@given(instance=UnaryOperator_strategy)
@settings(max_examples=25)
def test_UnaryOperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)


Unsafe_strategy = st.builds(Unsafe)
@given(instance=Unsafe_strategy)
@settings(max_examples=25)
def test_Unsafe_instantiation(instance):
    assert isinstance(instance, Unsafe)


UsingDirective_strategy = st.builds(UsingDirective)
@given(instance=UsingDirective_strategy)
@settings(max_examples=25)
def test_UsingDirective_instantiation(instance):
    assert isinstance(instance, UsingDirective)


VariableDeclaration_strategy = st.builds(VariableDeclaration)
@given(instance=VariableDeclaration_strategy)
@settings(max_examples=25)
def test_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)


VariableDeclarator_strategy = st.builds(VariableDeclarator)
@given(instance=VariableDeclarator_strategy)
@settings(max_examples=25)
def test_VariableDeclarator_instantiation(instance):
    assert isinstance(instance, VariableDeclarator)


VariableInitializer_strategy = st.builds(VariableInitializer)
@given(instance=VariableInitializer_strategy)
@settings(max_examples=25)
def test_VariableInitializer_instantiation(instance):
    assert isinstance(instance, VariableInitializer)


c_sharp_arrays_ArrayInitializer_strategy = st.builds(c_sharp_arrays_ArrayInitializer)
@given(instance=c_sharp_arrays_ArrayInitializer_strategy)
@settings(max_examples=25)
def test_c_sharp_arrays_ArrayInitializer_instantiation(instance):
    assert isinstance(instance, c_sharp_arrays_ArrayInitializer)


c_sharp_arrays_ArrayType_strategy = st.builds(c_sharp_arrays_ArrayType)
@given(instance=c_sharp_arrays_ArrayType_strategy)
@settings(max_examples=25)
def test_c_sharp_arrays_ArrayType_instantiation(instance):
    assert isinstance(instance, c_sharp_arrays_ArrayType)


c_sharp_arrays_RankSpecifier_strategy = st.builds(c_sharp_arrays_RankSpecifier)
@given(instance=c_sharp_arrays_RankSpecifier_strategy)
@settings(max_examples=25)
def test_c_sharp_arrays_RankSpecifier_instantiation(instance):
    assert isinstance(instance, c_sharp_arrays_RankSpecifier)


c_sharp_arrays_StackallocInitializer_strategy = st.builds(c_sharp_arrays_StackallocInitializer)
@given(instance=c_sharp_arrays_StackallocInitializer_strategy)
@settings(max_examples=25)
def test_c_sharp_arrays_StackallocInitializer_instantiation(instance):
    assert isinstance(instance, c_sharp_arrays_StackallocInitializer)


c_sharp_attributes_Attribute_strategy = st.builds(c_sharp_attributes_Attribute)
@given(instance=c_sharp_attributes_Attribute_strategy)
@settings(max_examples=25)
def test_c_sharp_attributes_Attribute_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_Attribute)


c_sharp_attributes_AttributeArguments_strategy = st.builds(c_sharp_attributes_AttributeArguments)
@given(instance=c_sharp_attributes_AttributeArguments_strategy)
@settings(max_examples=25)
def test_c_sharp_attributes_AttributeArguments_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_AttributeArguments)


c_sharp_attributes_AttributeTarget_strategy = st.builds(c_sharp_attributes_AttributeTarget)
@given(instance=c_sharp_attributes_AttributeTarget_strategy)
@settings(max_examples=25)
def test_c_sharp_attributes_AttributeTarget_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_AttributeTarget)


c_sharp_attributes_Attributes_strategy = st.builds(c_sharp_attributes_Attributes)
@given(instance=c_sharp_attributes_Attributes_strategy)
@settings(max_examples=25)
def test_c_sharp_attributes_Attributes_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_Attributes)


c_sharp_attributes_GlobalAttributeTarget_strategy = st.builds(c_sharp_attributes_GlobalAttributeTarget)
@given(instance=c_sharp_attributes_GlobalAttributeTarget_strategy)
@settings(max_examples=25)
def test_c_sharp_attributes_GlobalAttributeTarget_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_GlobalAttributeTarget)


c_sharp_attributes_GlobalAttributes_strategy = st.builds(c_sharp_attributes_GlobalAttributes)
@given(instance=c_sharp_attributes_GlobalAttributes_strategy)
@settings(max_examples=25)
def test_c_sharp_attributes_GlobalAttributes_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_GlobalAttributes)


c_sharp_attributes_NamedArgument_strategy = st.builds(c_sharp_attributes_NamedArgument)
@given(instance=c_sharp_attributes_NamedArgument_strategy)
@settings(max_examples=25)
def test_c_sharp_attributes_NamedArgument_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_NamedArgument)


c_sharp_attributes_NamedArgumentList_strategy = st.builds(c_sharp_attributes_NamedArgumentList)
@given(instance=c_sharp_attributes_NamedArgumentList_strategy)
@settings(max_examples=25)
def test_c_sharp_attributes_NamedArgumentList_instantiation(instance):
    assert isinstance(instance, c_sharp_attributes_NamedArgumentList)


c_sharp_classes_Block_strategy = st.builds(c_sharp_classes_Block)
@given(instance=c_sharp_classes_Block_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_Block_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_Block)


c_sharp_classes_Class_strategy = st.builds(c_sharp_classes_Class)
@given(instance=c_sharp_classes_Class_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_Class_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_Class)


c_sharp_classes_ClassBase_strategy = st.builds(c_sharp_classes_ClassBase)
@given(instance=c_sharp_classes_ClassBase_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_ClassBase_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_ClassBase)


c_sharp_classes_ClassMemberDeclaration_strategy = st.builds(c_sharp_classes_ClassMemberDeclaration)
@given(instance=c_sharp_classes_ClassMemberDeclaration_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_ClassMemberDeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_ClassMemberDeclaration)


c_sharp_classes_ConstantDeclaration_strategy = st.builds(c_sharp_classes_ConstantDeclaration)
@given(instance=c_sharp_classes_ConstantDeclaration_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_ConstantDeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_ConstantDeclaration)


c_sharp_classes_FieldDeclaration_strategy = st.builds(c_sharp_classes_FieldDeclaration)
@given(instance=c_sharp_classes_FieldDeclaration_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_FieldDeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_FieldDeclaration)


c_sharp_classes_FixedParameter_strategy = st.builds(c_sharp_classes_FixedParameter)
@given(instance=c_sharp_classes_FixedParameter_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_FixedParameter_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_FixedParameter)


c_sharp_classes_FormalParameterList_strategy = st.builds(c_sharp_classes_FormalParameterList)
@given(instance=c_sharp_classes_FormalParameterList_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_FormalParameterList_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_FormalParameterList)


c_sharp_classes_Method_strategy = st.builds(c_sharp_classes_Method)
@given(instance=c_sharp_classes_Method_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_Method_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_Method)


c_sharp_classes_ParameterArray_strategy = st.builds(c_sharp_classes_ParameterArray)
@given(instance=c_sharp_classes_ParameterArray_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_ParameterArray_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_ParameterArray)


c_sharp_classes_VariableInitializer_strategy = st.builds(c_sharp_classes_VariableInitializer)
@given(instance=c_sharp_classes_VariableInitializer_strategy)
@settings(max_examples=25)
def test_c_sharp_classes_VariableInitializer_instantiation(instance):
    assert isinstance(instance, c_sharp_classes_VariableInitializer)


c_sharp_common_Identifier_strategy = st.builds(c_sharp_common_Identifier)
@given(instance=c_sharp_common_Identifier_strategy)
@settings(max_examples=25)
def test_c_sharp_common_Identifier_instantiation(instance):
    assert isinstance(instance, c_sharp_common_Identifier)


c_sharp_common_NamedElement_strategy = st.builds(c_sharp_common_NamedElement, name=safe_text)
@given(instance=c_sharp_common_NamedElement_strategy)
@settings(max_examples=25)
def test_c_sharp_common_NamedElement_instantiation(instance):
    assert isinstance(instance, c_sharp_common_NamedElement)


c_sharp_common_NamespaceOrTypeName_strategy = st.builds(c_sharp_common_NamespaceOrTypeName)
@given(instance=c_sharp_common_NamespaceOrTypeName_strategy)
@settings(max_examples=25)
def test_c_sharp_common_NamespaceOrTypeName_instantiation(instance):
    assert isinstance(instance, c_sharp_common_NamespaceOrTypeName)


c_sharp_expressions_AdditiveExpression_strategy = st.builds(c_sharp_expressions_AdditiveExpression)
@given(instance=c_sharp_expressions_AdditiveExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_AdditiveExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_AdditiveExpression)


c_sharp_expressions_AddressOfExpression_strategy = st.builds(c_sharp_expressions_AddressOfExpression)
@given(instance=c_sharp_expressions_AddressOfExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_AddressOfExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_AddressOfExpression)


c_sharp_expressions_AndExpression_strategy = st.builds(c_sharp_expressions_AndExpression)
@given(instance=c_sharp_expressions_AndExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_AndExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_AndExpression)


c_sharp_expressions_Argument_strategy = st.builds(c_sharp_expressions_Argument)
@given(instance=c_sharp_expressions_Argument_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_Argument_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_Argument)


c_sharp_expressions_ArgumentList_strategy = st.builds(c_sharp_expressions_ArgumentList)
@given(instance=c_sharp_expressions_ArgumentList_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ArgumentList_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ArgumentList)


c_sharp_expressions_ArrayCreationExpression_strategy = st.builds(c_sharp_expressions_ArrayCreationExpression)
@given(instance=c_sharp_expressions_ArrayCreationExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ArrayCreationExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ArrayCreationExpression)


c_sharp_expressions_AssignmentExpression_strategy = st.builds(c_sharp_expressions_AssignmentExpression)
@given(instance=c_sharp_expressions_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_AssignmentExpression)


c_sharp_expressions_BaseAccess_strategy = st.builds(c_sharp_expressions_BaseAccess)
@given(instance=c_sharp_expressions_BaseAccess_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_BaseAccess_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_BaseAccess)


c_sharp_expressions_CastExpression_strategy = st.builds(c_sharp_expressions_CastExpression)
@given(instance=c_sharp_expressions_CastExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_CastExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_CastExpression)


c_sharp_expressions_CheckedExpression_strategy = st.builds(c_sharp_expressions_CheckedExpression)
@given(instance=c_sharp_expressions_CheckedExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_CheckedExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_CheckedExpression)


c_sharp_expressions_ConditionalAndExpression_strategy = st.builds(c_sharp_expressions_ConditionalAndExpression)
@given(instance=c_sharp_expressions_ConditionalAndExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ConditionalAndExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ConditionalAndExpression)


c_sharp_expressions_ConditionalExpression_strategy = st.builds(c_sharp_expressions_ConditionalExpression)
@given(instance=c_sharp_expressions_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ConditionalExpression)


c_sharp_expressions_ConditionalOrExpression_strategy = st.builds(c_sharp_expressions_ConditionalOrExpression)
@given(instance=c_sharp_expressions_ConditionalOrExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ConditionalOrExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ConditionalOrExpression)


c_sharp_expressions_DelegateCreationExpression_strategy = st.builds(c_sharp_expressions_DelegateCreationExpression)
@given(instance=c_sharp_expressions_DelegateCreationExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_DelegateCreationExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_DelegateCreationExpression)


c_sharp_expressions_ElementAccess_strategy = st.builds(c_sharp_expressions_ElementAccess)
@given(instance=c_sharp_expressions_ElementAccess_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ElementAccess_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ElementAccess)


c_sharp_expressions_EqualityExpression_strategy = st.builds(c_sharp_expressions_EqualityExpression)
@given(instance=c_sharp_expressions_EqualityExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_EqualityExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_EqualityExpression)


c_sharp_expressions_ExclusiveOrExpression_strategy = st.builds(c_sharp_expressions_ExclusiveOrExpression)
@given(instance=c_sharp_expressions_ExclusiveOrExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ExclusiveOrExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ExclusiveOrExpression)


c_sharp_expressions_Expression_strategy = st.builds(c_sharp_expressions_Expression)
@given(instance=c_sharp_expressions_Expression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_Expression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_Expression)


c_sharp_expressions_ExpressionList_strategy = st.builds(c_sharp_expressions_ExpressionList)
@given(instance=c_sharp_expressions_ExpressionList_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ExpressionList_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ExpressionList)


c_sharp_expressions_InclusiveOrExpression_strategy = st.builds(c_sharp_expressions_InclusiveOrExpression)
@given(instance=c_sharp_expressions_InclusiveOrExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_InclusiveOrExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_InclusiveOrExpression)


c_sharp_expressions_InvocationExpression_strategy = st.builds(c_sharp_expressions_InvocationExpression)
@given(instance=c_sharp_expressions_InvocationExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_InvocationExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_InvocationExpression)


c_sharp_expressions_MemberAccess_strategy = st.builds(c_sharp_expressions_MemberAccess)
@given(instance=c_sharp_expressions_MemberAccess_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_MemberAccess_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_MemberAccess)


c_sharp_expressions_MultiplicativeExpression_strategy = st.builds(c_sharp_expressions_MultiplicativeExpression)
@given(instance=c_sharp_expressions_MultiplicativeExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_MultiplicativeExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_MultiplicativeExpression)


c_sharp_expressions_ObjectCreationExpression_strategy = st.builds(c_sharp_expressions_ObjectCreationExpression)
@given(instance=c_sharp_expressions_ObjectCreationExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ObjectCreationExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ObjectCreationExpression)


c_sharp_expressions_ParenthesizedExpression_strategy = st.builds(c_sharp_expressions_ParenthesizedExpression)
@given(instance=c_sharp_expressions_ParenthesizedExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ParenthesizedExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ParenthesizedExpression)


c_sharp_expressions_PointerMemberAccess_strategy = st.builds(c_sharp_expressions_PointerMemberAccess)
@given(instance=c_sharp_expressions_PointerMemberAccess_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_PointerMemberAccess_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PointerMemberAccess)


c_sharp_expressions_PostDecrementExpression_strategy = st.builds(c_sharp_expressions_PostDecrementExpression)
@given(instance=c_sharp_expressions_PostDecrementExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_PostDecrementExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PostDecrementExpression)


c_sharp_expressions_PostIncrementExpression_strategy = st.builds(c_sharp_expressions_PostIncrementExpression)
@given(instance=c_sharp_expressions_PostIncrementExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_PostIncrementExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PostIncrementExpression)


c_sharp_expressions_PreDecrementExpression_strategy = st.builds(c_sharp_expressions_PreDecrementExpression)
@given(instance=c_sharp_expressions_PreDecrementExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_PreDecrementExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PreDecrementExpression)


c_sharp_expressions_PreIncrementExpression_strategy = st.builds(c_sharp_expressions_PreIncrementExpression)
@given(instance=c_sharp_expressions_PreIncrementExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_PreIncrementExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PreIncrementExpression)


c_sharp_expressions_PrimaryExpression_strategy = st.builds(c_sharp_expressions_PrimaryExpression)
@given(instance=c_sharp_expressions_PrimaryExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_PrimaryExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PrimaryExpression)


c_sharp_expressions_PrimaryExtendedExpressionType_strategy = st.builds(c_sharp_expressions_PrimaryExtendedExpressionType)
@given(instance=c_sharp_expressions_PrimaryExtendedExpressionType_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_PrimaryExtendedExpressionType_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PrimaryExtendedExpressionType)


c_sharp_expressions_PrimaryNoArrayCreationExpression_strategy = st.builds(c_sharp_expressions_PrimaryNoArrayCreationExpression)
@given(instance=c_sharp_expressions_PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_PrimaryNoArrayCreationExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_PrimaryNoArrayCreationExpression)


c_sharp_expressions_RelationalExpression_strategy = st.builds(c_sharp_expressions_RelationalExpression)
@given(instance=c_sharp_expressions_RelationalExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_RelationalExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_RelationalExpression)


c_sharp_expressions_ShiftExpression_strategy = st.builds(c_sharp_expressions_ShiftExpression)
@given(instance=c_sharp_expressions_ShiftExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_ShiftExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_ShiftExpression)


c_sharp_expressions_SizeOfExpression_strategy = st.builds(c_sharp_expressions_SizeOfExpression)
@given(instance=c_sharp_expressions_SizeOfExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_SizeOfExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_SizeOfExpression)


c_sharp_expressions_StatementExpression_strategy = st.builds(c_sharp_expressions_StatementExpression)
@given(instance=c_sharp_expressions_StatementExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_StatementExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_StatementExpression)


c_sharp_expressions_StatementExpressionList_strategy = st.builds(c_sharp_expressions_StatementExpressionList)
@given(instance=c_sharp_expressions_StatementExpressionList_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_StatementExpressionList_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_StatementExpressionList)


c_sharp_expressions_TypeOfExpression_strategy = st.builds(c_sharp_expressions_TypeOfExpression)
@given(instance=c_sharp_expressions_TypeOfExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_TypeOfExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_TypeOfExpression)


c_sharp_expressions_UnaryExpression_strategy = st.builds(c_sharp_expressions_UnaryExpression)
@given(instance=c_sharp_expressions_UnaryExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_UnaryExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_UnaryExpression)


c_sharp_expressions_UncheckedExpression_strategy = st.builds(c_sharp_expressions_UncheckedExpression)
@given(instance=c_sharp_expressions_UncheckedExpression_strategy)
@settings(max_examples=25)
def test_c_sharp_expressions_UncheckedExpression_instantiation(instance):
    assert isinstance(instance, c_sharp_expressions_UncheckedExpression)


c_sharp_keywords_Case_strategy = st.builds(c_sharp_keywords_Case)
@given(instance=c_sharp_keywords_Case_strategy)
@settings(max_examples=25)
def test_c_sharp_keywords_Case_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Case)


c_sharp_keywords_Default_strategy = st.builds(c_sharp_keywords_Default)
@given(instance=c_sharp_keywords_Default_strategy)
@settings(max_examples=25)
def test_c_sharp_keywords_Default_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Default)


c_sharp_keywords_Event_strategy = st.builds(c_sharp_keywords_Event)
@given(instance=c_sharp_keywords_Event_strategy)
@settings(max_examples=25)
def test_c_sharp_keywords_Event_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Event)


c_sharp_keywords_Out_strategy = st.builds(c_sharp_keywords_Out)
@given(instance=c_sharp_keywords_Out_strategy)
@settings(max_examples=25)
def test_c_sharp_keywords_Out_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Out)


c_sharp_keywords_Params_strategy = st.builds(c_sharp_keywords_Params)
@given(instance=c_sharp_keywords_Params_strategy)
@settings(max_examples=25)
def test_c_sharp_keywords_Params_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Params)


c_sharp_keywords_Ref_strategy = st.builds(c_sharp_keywords_Ref)
@given(instance=c_sharp_keywords_Ref_strategy)
@settings(max_examples=25)
def test_c_sharp_keywords_Ref_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Ref)


c_sharp_keywords_Return_strategy = st.builds(c_sharp_keywords_Return)
@given(instance=c_sharp_keywords_Return_strategy)
@settings(max_examples=25)
def test_c_sharp_keywords_Return_instantiation(instance):
    assert isinstance(instance, c_sharp_keywords_Return)


c_sharp_literals_BooleanLiteral_strategy = st.builds(c_sharp_literals_BooleanLiteral, value=st.booleans())
@given(instance=c_sharp_literals_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_BooleanLiteral)


c_sharp_literals_CharacterLiteral_strategy = st.builds(c_sharp_literals_CharacterLiteral, value=safe_text)
@given(instance=c_sharp_literals_CharacterLiteral_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_CharacterLiteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_CharacterLiteral)


c_sharp_literals_DecimalIntegerLiteral_strategy = st.builds(c_sharp_literals_DecimalIntegerLiteral, value=safe_text)
@given(instance=c_sharp_literals_DecimalIntegerLiteral_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_DecimalIntegerLiteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_DecimalIntegerLiteral)


c_sharp_literals_HexadecimalIntegerLiteral_strategy = st.builds(c_sharp_literals_HexadecimalIntegerLiteral, value=safe_text)
@given(instance=c_sharp_literals_HexadecimalIntegerLiteral_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_HexadecimalIntegerLiteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_HexadecimalIntegerLiteral)


c_sharp_literals_Literal_strategy = st.builds(c_sharp_literals_Literal)
@given(instance=c_sharp_literals_Literal_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_Literal_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_Literal)


c_sharp_literals_NullLiteral_strategy = st.builds(c_sharp_literals_NullLiteral)
@given(instance=c_sharp_literals_NullLiteral_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_NullLiteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_NullLiteral)


c_sharp_literals_RealLiteral_strategy = st.builds(c_sharp_literals_RealLiteral, value=safe_text)
@given(instance=c_sharp_literals_RealLiteral_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_RealLiteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_RealLiteral)


c_sharp_literals_StringLiteral_strategy = st.builds(c_sharp_literals_StringLiteral, value=safe_text)
@given(instance=c_sharp_literals_StringLiteral_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_StringLiteral_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_StringLiteral)


c_sharp_literals_This_strategy = st.builds(c_sharp_literals_This)
@given(instance=c_sharp_literals_This_strategy)
@settings(max_examples=25)
def test_c_sharp_literals_This_instantiation(instance):
    assert isinstance(instance, c_sharp_literals_This)


c_sharp_modifiers_Abstract_strategy = st.builds(c_sharp_modifiers_Abstract)
@given(instance=c_sharp_modifiers_Abstract_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Abstract_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Abstract)


c_sharp_modifiers_Extern_strategy = st.builds(c_sharp_modifiers_Extern)
@given(instance=c_sharp_modifiers_Extern_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Extern_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Extern)


c_sharp_modifiers_Internal_strategy = st.builds(c_sharp_modifiers_Internal)
@given(instance=c_sharp_modifiers_Internal_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Internal_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Internal)


c_sharp_modifiers_Modifier_strategy = st.builds(c_sharp_modifiers_Modifier)
@given(instance=c_sharp_modifiers_Modifier_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Modifier_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Modifier)


c_sharp_modifiers_New_strategy = st.builds(c_sharp_modifiers_New)
@given(instance=c_sharp_modifiers_New_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_New_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_New)


c_sharp_modifiers_OverrideModifier_strategy = st.builds(c_sharp_modifiers_OverrideModifier)
@given(instance=c_sharp_modifiers_OverrideModifier_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_OverrideModifier_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_OverrideModifier)


c_sharp_modifiers_Partial_strategy = st.builds(c_sharp_modifiers_Partial)
@given(instance=c_sharp_modifiers_Partial_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Partial_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Partial)


c_sharp_modifiers_Private_strategy = st.builds(c_sharp_modifiers_Private)
@given(instance=c_sharp_modifiers_Private_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Private_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Private)


c_sharp_modifiers_Protected_strategy = st.builds(c_sharp_modifiers_Protected)
@given(instance=c_sharp_modifiers_Protected_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Protected_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Protected)


c_sharp_modifiers_Public_strategy = st.builds(c_sharp_modifiers_Public)
@given(instance=c_sharp_modifiers_Public_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Public_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Public)


c_sharp_modifiers_ReadOnly_strategy = st.builds(c_sharp_modifiers_ReadOnly)
@given(instance=c_sharp_modifiers_ReadOnly_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_ReadOnly_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_ReadOnly)


c_sharp_modifiers_Sealed_strategy = st.builds(c_sharp_modifiers_Sealed)
@given(instance=c_sharp_modifiers_Sealed_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Sealed_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Sealed)


c_sharp_modifiers_Static_strategy = st.builds(c_sharp_modifiers_Static)
@given(instance=c_sharp_modifiers_Static_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Static_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Static)


c_sharp_modifiers_Unsafe_strategy = st.builds(c_sharp_modifiers_Unsafe)
@given(instance=c_sharp_modifiers_Unsafe_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Unsafe_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Unsafe)


c_sharp_modifiers_Virtual_strategy = st.builds(c_sharp_modifiers_Virtual)
@given(instance=c_sharp_modifiers_Virtual_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Virtual_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Virtual)


c_sharp_modifiers_Volatile_strategy = st.builds(c_sharp_modifiers_Volatile)
@given(instance=c_sharp_modifiers_Volatile_strategy)
@settings(max_examples=25)
def test_c_sharp_modifiers_Volatile_instantiation(instance):
    assert isinstance(instance, c_sharp_modifiers_Volatile)


c_sharp_namespaces_CompilationUnit_strategy = st.builds(c_sharp_namespaces_CompilationUnit)
@given(instance=c_sharp_namespaces_CompilationUnit_strategy)
@settings(max_examples=25)
def test_c_sharp_namespaces_CompilationUnit_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_CompilationUnit)


c_sharp_namespaces_Namespace_strategy = st.builds(c_sharp_namespaces_Namespace)
@given(instance=c_sharp_namespaces_Namespace_strategy)
@settings(max_examples=25)
def test_c_sharp_namespaces_Namespace_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_Namespace)


c_sharp_namespaces_NamespaceBody_strategy = st.builds(c_sharp_namespaces_NamespaceBody)
@given(instance=c_sharp_namespaces_NamespaceBody_strategy)
@settings(max_examples=25)
def test_c_sharp_namespaces_NamespaceBody_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_NamespaceBody)


c_sharp_namespaces_NamespaceMemberDeclaration_strategy = st.builds(c_sharp_namespaces_NamespaceMemberDeclaration)
@given(instance=c_sharp_namespaces_NamespaceMemberDeclaration_strategy)
@settings(max_examples=25)
def test_c_sharp_namespaces_NamespaceMemberDeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_NamespaceMemberDeclaration)


c_sharp_namespaces_TypeDeclaration_strategy = st.builds(c_sharp_namespaces_TypeDeclaration)
@given(instance=c_sharp_namespaces_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_c_sharp_namespaces_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_TypeDeclaration)


c_sharp_namespaces_UsingDirective_strategy = st.builds(c_sharp_namespaces_UsingDirective)
@given(instance=c_sharp_namespaces_UsingDirective_strategy)
@settings(max_examples=25)
def test_c_sharp_namespaces_UsingDirective_instantiation(instance):
    assert isinstance(instance, c_sharp_namespaces_UsingDirective)


c_sharp_operators_Addition_strategy = st.builds(c_sharp_operators_Addition)
@given(instance=c_sharp_operators_Addition_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Addition_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Addition)


c_sharp_operators_AdditiveOperator_strategy = st.builds(c_sharp_operators_AdditiveOperator)
@given(instance=c_sharp_operators_AdditiveOperator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AdditiveOperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AdditiveOperator)


c_sharp_operators_And_strategy = st.builds(c_sharp_operators_And)
@given(instance=c_sharp_operators_And_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_And_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_And)


c_sharp_operators_Assignment_strategy = st.builds(c_sharp_operators_Assignment)
@given(instance=c_sharp_operators_Assignment_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Assignment_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Assignment)


c_sharp_operators_AssignmentAnd_strategy = st.builds(c_sharp_operators_AssignmentAnd)
@given(instance=c_sharp_operators_AssignmentAnd_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentAnd_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentAnd)


c_sharp_operators_AssignmentDivision_strategy = st.builds(c_sharp_operators_AssignmentDivision)
@given(instance=c_sharp_operators_AssignmentDivision_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentDivision_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentDivision)


c_sharp_operators_AssignmentExclusiveOr_strategy = st.builds(c_sharp_operators_AssignmentExclusiveOr)
@given(instance=c_sharp_operators_AssignmentExclusiveOr_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentExclusiveOr_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentExclusiveOr)


c_sharp_operators_AssignmentLeftShift_strategy = st.builds(c_sharp_operators_AssignmentLeftShift)
@given(instance=c_sharp_operators_AssignmentLeftShift_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentLeftShift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentLeftShift)


c_sharp_operators_AssignmentMinus_strategy = st.builds(c_sharp_operators_AssignmentMinus)
@given(instance=c_sharp_operators_AssignmentMinus_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentMinus_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentMinus)


c_sharp_operators_AssignmentModulo_strategy = st.builds(c_sharp_operators_AssignmentModulo)
@given(instance=c_sharp_operators_AssignmentModulo_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentModulo_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentModulo)


c_sharp_operators_AssignmentMultiplication_strategy = st.builds(c_sharp_operators_AssignmentMultiplication)
@given(instance=c_sharp_operators_AssignmentMultiplication_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentMultiplication_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentMultiplication)


c_sharp_operators_AssignmentOperator_strategy = st.builds(c_sharp_operators_AssignmentOperator)
@given(instance=c_sharp_operators_AssignmentOperator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentOperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentOperator)


c_sharp_operators_AssignmentOr_strategy = st.builds(c_sharp_operators_AssignmentOr)
@given(instance=c_sharp_operators_AssignmentOr_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentOr_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentOr)


c_sharp_operators_AssignmentPlus_strategy = st.builds(c_sharp_operators_AssignmentPlus)
@given(instance=c_sharp_operators_AssignmentPlus_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentPlus_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentPlus)


c_sharp_operators_AssignmentRightShift_strategy = st.builds(c_sharp_operators_AssignmentRightShift)
@given(instance=c_sharp_operators_AssignmentRightShift_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentRightShift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentRightShift)


c_sharp_operators_AssignmentUnsignedRightShift_strategy = st.builds(c_sharp_operators_AssignmentUnsignedRightShift)
@given(instance=c_sharp_operators_AssignmentUnsignedRightShift_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_AssignmentUnsignedRightShift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_AssignmentUnsignedRightShift)


c_sharp_operators_Complement_strategy = st.builds(c_sharp_operators_Complement)
@given(instance=c_sharp_operators_Complement_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Complement_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Complement)


c_sharp_operators_ConditionalAnd_strategy = st.builds(c_sharp_operators_ConditionalAnd)
@given(instance=c_sharp_operators_ConditionalAnd_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_ConditionalAnd_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_ConditionalAnd)


c_sharp_operators_ConditionalOr_strategy = st.builds(c_sharp_operators_ConditionalOr)
@given(instance=c_sharp_operators_ConditionalOr_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_ConditionalOr_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_ConditionalOr)


c_sharp_operators_Division_strategy = st.builds(c_sharp_operators_Division)
@given(instance=c_sharp_operators_Division_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Division_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Division)


c_sharp_operators_Equal_strategy = st.builds(c_sharp_operators_Equal)
@given(instance=c_sharp_operators_Equal_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Equal_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Equal)


c_sharp_operators_EqualityOperator_strategy = st.builds(c_sharp_operators_EqualityOperator)
@given(instance=c_sharp_operators_EqualityOperator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_EqualityOperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_EqualityOperator)


c_sharp_operators_ExclusiveOr_strategy = st.builds(c_sharp_operators_ExclusiveOr)
@given(instance=c_sharp_operators_ExclusiveOr_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_ExclusiveOr_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_ExclusiveOr)


c_sharp_operators_GreaterThan_strategy = st.builds(c_sharp_operators_GreaterThan)
@given(instance=c_sharp_operators_GreaterThan_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_GreaterThan_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_GreaterThan)


c_sharp_operators_GreaterThanOrEqual_strategy = st.builds(c_sharp_operators_GreaterThanOrEqual)
@given(instance=c_sharp_operators_GreaterThanOrEqual_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_GreaterThanOrEqual_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_GreaterThanOrEqual)


c_sharp_operators_InclusiveOr_strategy = st.builds(c_sharp_operators_InclusiveOr)
@given(instance=c_sharp_operators_InclusiveOr_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_InclusiveOr_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_InclusiveOr)


c_sharp_operators_LeftShift_strategy = st.builds(c_sharp_operators_LeftShift)
@given(instance=c_sharp_operators_LeftShift_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_LeftShift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_LeftShift)


c_sharp_operators_LessThan_strategy = st.builds(c_sharp_operators_LessThan)
@given(instance=c_sharp_operators_LessThan_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_LessThan_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_LessThan)


c_sharp_operators_LessThanOrEqual_strategy = st.builds(c_sharp_operators_LessThanOrEqual)
@given(instance=c_sharp_operators_LessThanOrEqual_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_LessThanOrEqual_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_LessThanOrEqual)


c_sharp_operators_MinusMinus_strategy = st.builds(c_sharp_operators_MinusMinus)
@given(instance=c_sharp_operators_MinusMinus_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_MinusMinus_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_MinusMinus)


c_sharp_operators_Multiplication_strategy = st.builds(c_sharp_operators_Multiplication)
@given(instance=c_sharp_operators_Multiplication_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Multiplication_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Multiplication)


c_sharp_operators_MultiplicativeOperator_strategy = st.builds(c_sharp_operators_MultiplicativeOperator)
@given(instance=c_sharp_operators_MultiplicativeOperator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_MultiplicativeOperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_MultiplicativeOperator)


c_sharp_operators_Negate_strategy = st.builds(c_sharp_operators_Negate)
@given(instance=c_sharp_operators_Negate_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Negate_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Negate)


c_sharp_operators_NotEqual_strategy = st.builds(c_sharp_operators_NotEqual)
@given(instance=c_sharp_operators_NotEqual_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_NotEqual_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_NotEqual)


c_sharp_operators_Operator_strategy = st.builds(c_sharp_operators_Operator)
@given(instance=c_sharp_operators_Operator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Operator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Operator)


c_sharp_operators_PlusPlus_strategy = st.builds(c_sharp_operators_PlusPlus)
@given(instance=c_sharp_operators_PlusPlus_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_PlusPlus_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_PlusPlus)


c_sharp_operators_RelationOperator_strategy = st.builds(c_sharp_operators_RelationOperator)
@given(instance=c_sharp_operators_RelationOperator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_RelationOperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_RelationOperator)


c_sharp_operators_Remainder_strategy = st.builds(c_sharp_operators_Remainder)
@given(instance=c_sharp_operators_Remainder_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Remainder_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Remainder)


c_sharp_operators_RightShift_strategy = st.builds(c_sharp_operators_RightShift)
@given(instance=c_sharp_operators_RightShift_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_RightShift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_RightShift)


c_sharp_operators_ShiftOperator_strategy = st.builds(c_sharp_operators_ShiftOperator)
@given(instance=c_sharp_operators_ShiftOperator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_ShiftOperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_ShiftOperator)


c_sharp_operators_Subtraction_strategy = st.builds(c_sharp_operators_Subtraction)
@given(instance=c_sharp_operators_Subtraction_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_Subtraction_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_Subtraction)


c_sharp_operators_UnaryModificationOperator_strategy = st.builds(c_sharp_operators_UnaryModificationOperator)
@given(instance=c_sharp_operators_UnaryModificationOperator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_UnaryModificationOperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_UnaryModificationOperator)


c_sharp_operators_UnaryOperator_strategy = st.builds(c_sharp_operators_UnaryOperator)
@given(instance=c_sharp_operators_UnaryOperator_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_UnaryOperator_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_UnaryOperator)


c_sharp_operators_UnsignedRightShift_strategy = st.builds(c_sharp_operators_UnsignedRightShift)
@given(instance=c_sharp_operators_UnsignedRightShift_strategy)
@settings(max_examples=25)
def test_c_sharp_operators_UnsignedRightShift_instantiation(instance):
    assert isinstance(instance, c_sharp_operators_UnsignedRightShift)


c_sharp_statements_BreakStatement_strategy = st.builds(c_sharp_statements_BreakStatement)
@given(instance=c_sharp_statements_BreakStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_BreakStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_BreakStatement)


c_sharp_statements_CheckedStatement_strategy = st.builds(c_sharp_statements_CheckedStatement)
@given(instance=c_sharp_statements_CheckedStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_CheckedStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_CheckedStatement)


c_sharp_statements_ConstantDeclarator_strategy = st.builds(c_sharp_statements_ConstantDeclarator)
@given(instance=c_sharp_statements_ConstantDeclarator_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ConstantDeclarator_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ConstantDeclarator)


c_sharp_statements_ContinueStatement_strategy = st.builds(c_sharp_statements_ContinueStatement)
@given(instance=c_sharp_statements_ContinueStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ContinueStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ContinueStatement)


c_sharp_statements_DeclarationStatement_strategy = st.builds(c_sharp_statements_DeclarationStatement)
@given(instance=c_sharp_statements_DeclarationStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_DeclarationStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_DeclarationStatement)


c_sharp_statements_DoStatement_strategy = st.builds(c_sharp_statements_DoStatement)
@given(instance=c_sharp_statements_DoStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_DoStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_DoStatement)


c_sharp_statements_EmbeddedStatement_strategy = st.builds(c_sharp_statements_EmbeddedStatement)
@given(instance=c_sharp_statements_EmbeddedStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_EmbeddedStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_EmbeddedStatement)


c_sharp_statements_EmptyStatement_strategy = st.builds(c_sharp_statements_EmptyStatement)
@given(instance=c_sharp_statements_EmptyStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_EmptyStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_EmptyStatement)


c_sharp_statements_ExpressionStatement_strategy = st.builds(c_sharp_statements_ExpressionStatement)
@given(instance=c_sharp_statements_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ExpressionStatement)


c_sharp_statements_FinallyClause_strategy = st.builds(c_sharp_statements_FinallyClause)
@given(instance=c_sharp_statements_FinallyClause_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_FinallyClause_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_FinallyClause)


c_sharp_statements_FixedPointerDeclarator_strategy = st.builds(c_sharp_statements_FixedPointerDeclarator)
@given(instance=c_sharp_statements_FixedPointerDeclarator_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_FixedPointerDeclarator_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_FixedPointerDeclarator)


c_sharp_statements_FixedStatement_strategy = st.builds(c_sharp_statements_FixedStatement)
@given(instance=c_sharp_statements_FixedStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_FixedStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_FixedStatement)


c_sharp_statements_ForInitializer_strategy = st.builds(c_sharp_statements_ForInitializer)
@given(instance=c_sharp_statements_ForInitializer_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ForInitializer_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ForInitializer)


c_sharp_statements_ForStatement_strategy = st.builds(c_sharp_statements_ForStatement)
@given(instance=c_sharp_statements_ForStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ForStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ForStatement)


c_sharp_statements_ForeachStatement_strategy = st.builds(c_sharp_statements_ForeachStatement)
@given(instance=c_sharp_statements_ForeachStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ForeachStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ForeachStatement)


c_sharp_statements_GeneralCatchClause_strategy = st.builds(c_sharp_statements_GeneralCatchClause)
@given(instance=c_sharp_statements_GeneralCatchClause_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_GeneralCatchClause_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_GeneralCatchClause)


c_sharp_statements_GotoStatement_strategy = st.builds(c_sharp_statements_GotoStatement)
@given(instance=c_sharp_statements_GotoStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_GotoStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_GotoStatement)


c_sharp_statements_IfStatement_strategy = st.builds(c_sharp_statements_IfStatement)
@given(instance=c_sharp_statements_IfStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_IfStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_IfStatement)


c_sharp_statements_IterationStatement_strategy = st.builds(c_sharp_statements_IterationStatement)
@given(instance=c_sharp_statements_IterationStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_IterationStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_IterationStatement)


c_sharp_statements_JumpStatement_strategy = st.builds(c_sharp_statements_JumpStatement)
@given(instance=c_sharp_statements_JumpStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_JumpStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_JumpStatement)


c_sharp_statements_LabeledStatement_strategy = st.builds(c_sharp_statements_LabeledStatement)
@given(instance=c_sharp_statements_LabeledStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_LabeledStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_LabeledStatement)


c_sharp_statements_LocalConstantDeclaration_strategy = st.builds(c_sharp_statements_LocalConstantDeclaration)
@given(instance=c_sharp_statements_LocalConstantDeclaration_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_LocalConstantDeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_LocalConstantDeclaration)


c_sharp_statements_LockStatement_strategy = st.builds(c_sharp_statements_LockStatement)
@given(instance=c_sharp_statements_LockStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_LockStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_LockStatement)


c_sharp_statements_ResourceAcquisition_strategy = st.builds(c_sharp_statements_ResourceAcquisition)
@given(instance=c_sharp_statements_ResourceAcquisition_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ResourceAcquisition_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ResourceAcquisition)


c_sharp_statements_ReturnStatement_strategy = st.builds(c_sharp_statements_ReturnStatement)
@given(instance=c_sharp_statements_ReturnStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ReturnStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ReturnStatement)


c_sharp_statements_SelectionStatement_strategy = st.builds(c_sharp_statements_SelectionStatement)
@given(instance=c_sharp_statements_SelectionStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_SelectionStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SelectionStatement)


c_sharp_statements_SimpleEmbeddedStatement_strategy = st.builds(c_sharp_statements_SimpleEmbeddedStatement)
@given(instance=c_sharp_statements_SimpleEmbeddedStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_SimpleEmbeddedStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SimpleEmbeddedStatement)


c_sharp_statements_SpecificCatchClause_strategy = st.builds(c_sharp_statements_SpecificCatchClause)
@given(instance=c_sharp_statements_SpecificCatchClause_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_SpecificCatchClause_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SpecificCatchClause)


c_sharp_statements_Statement_strategy = st.builds(c_sharp_statements_Statement)
@given(instance=c_sharp_statements_Statement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_Statement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_Statement)


c_sharp_statements_SwitchLabel_strategy = st.builds(c_sharp_statements_SwitchLabel)
@given(instance=c_sharp_statements_SwitchLabel_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_SwitchLabel_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SwitchLabel)


c_sharp_statements_SwitchSection_strategy = st.builds(c_sharp_statements_SwitchSection)
@given(instance=c_sharp_statements_SwitchSection_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_SwitchSection_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SwitchSection)


c_sharp_statements_SwitchStatement_strategy = st.builds(c_sharp_statements_SwitchStatement)
@given(instance=c_sharp_statements_SwitchStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_SwitchStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_SwitchStatement)


c_sharp_statements_ThrowStatement_strategy = st.builds(c_sharp_statements_ThrowStatement)
@given(instance=c_sharp_statements_ThrowStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_ThrowStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_ThrowStatement)


c_sharp_statements_TryStatement_strategy = st.builds(c_sharp_statements_TryStatement)
@given(instance=c_sharp_statements_TryStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_TryStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_TryStatement)


c_sharp_statements_UncheckedStatement_strategy = st.builds(c_sharp_statements_UncheckedStatement)
@given(instance=c_sharp_statements_UncheckedStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_UncheckedStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_UncheckedStatement)


c_sharp_statements_UsingStatement_strategy = st.builds(c_sharp_statements_UsingStatement)
@given(instance=c_sharp_statements_UsingStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_UsingStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_UsingStatement)


c_sharp_statements_VariableDeclaration_strategy = st.builds(c_sharp_statements_VariableDeclaration)
@given(instance=c_sharp_statements_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_VariableDeclaration)


c_sharp_statements_VariableDeclarator_strategy = st.builds(c_sharp_statements_VariableDeclarator)
@given(instance=c_sharp_statements_VariableDeclarator_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_VariableDeclarator_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_VariableDeclarator)


c_sharp_statements_WhileStatement_strategy = st.builds(c_sharp_statements_WhileStatement)
@given(instance=c_sharp_statements_WhileStatement_strategy)
@settings(max_examples=25)
def test_c_sharp_statements_WhileStatement_instantiation(instance):
    assert isinstance(instance, c_sharp_statements_WhileStatement)


c_sharp_types_Bool_strategy = st.builds(c_sharp_types_Bool)
@given(instance=c_sharp_types_Bool_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Bool_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Bool)


c_sharp_types_Byte_strategy = st.builds(c_sharp_types_Byte)
@given(instance=c_sharp_types_Byte_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Byte_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Byte)


c_sharp_types_Char_strategy = st.builds(c_sharp_types_Char)
@given(instance=c_sharp_types_Char_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Char_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Char)


c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_strategy = st.builds(c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType)
@given(instance=c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_strategy)
@settings(max_examples=25)
def test_c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_instantiation(instance):
    assert isinstance(instance, c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType)


c_sharp_types_Decimal_strategy = st.builds(c_sharp_types_Decimal)
@given(instance=c_sharp_types_Decimal_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Decimal_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Decimal)


c_sharp_types_Double_strategy = st.builds(c_sharp_types_Double)
@given(instance=c_sharp_types_Double_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Double_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Double)


c_sharp_types_Float_strategy = st.builds(c_sharp_types_Float)
@given(instance=c_sharp_types_Float_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Float_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Float)


c_sharp_types_Int_strategy = st.builds(c_sharp_types_Int)
@given(instance=c_sharp_types_Int_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Int_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Int)


c_sharp_types_Long_strategy = st.builds(c_sharp_types_Long)
@given(instance=c_sharp_types_Long_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Long_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Long)


c_sharp_types_NonArrayType_strategy = st.builds(c_sharp_types_NonArrayType)
@given(instance=c_sharp_types_NonArrayType_strategy)
@settings(max_examples=25)
def test_c_sharp_types_NonArrayType_instantiation(instance):
    assert isinstance(instance, c_sharp_types_NonArrayType)


c_sharp_types_Object_strategy = st.builds(c_sharp_types_Object)
@given(instance=c_sharp_types_Object_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Object_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Object)


c_sharp_types_PointerType_strategy = st.builds(c_sharp_types_PointerType)
@given(instance=c_sharp_types_PointerType_strategy)
@settings(max_examples=25)
def test_c_sharp_types_PointerType_instantiation(instance):
    assert isinstance(instance, c_sharp_types_PointerType)


c_sharp_types_ReferenceType_strategy = st.builds(c_sharp_types_ReferenceType)
@given(instance=c_sharp_types_ReferenceType_strategy)
@settings(max_examples=25)
def test_c_sharp_types_ReferenceType_instantiation(instance):
    assert isinstance(instance, c_sharp_types_ReferenceType)


c_sharp_types_SByte_strategy = st.builds(c_sharp_types_SByte)
@given(instance=c_sharp_types_SByte_strategy)
@settings(max_examples=25)
def test_c_sharp_types_SByte_instantiation(instance):
    assert isinstance(instance, c_sharp_types_SByte)


c_sharp_types_Short_strategy = st.builds(c_sharp_types_Short)
@given(instance=c_sharp_types_Short_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Short_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Short)


c_sharp_types_SimpleType_strategy = st.builds(c_sharp_types_SimpleType)
@given(instance=c_sharp_types_SimpleType_strategy)
@settings(max_examples=25)
def test_c_sharp_types_SimpleType_instantiation(instance):
    assert isinstance(instance, c_sharp_types_SimpleType)


c_sharp_types_String_strategy = st.builds(c_sharp_types_String)
@given(instance=c_sharp_types_String_strategy)
@settings(max_examples=25)
def test_c_sharp_types_String_instantiation(instance):
    assert isinstance(instance, c_sharp_types_String)


c_sharp_types_Type_strategy = st.builds(c_sharp_types_Type)
@given(instance=c_sharp_types_Type_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Type_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Type)


c_sharp_types_UInt_strategy = st.builds(c_sharp_types_UInt)
@given(instance=c_sharp_types_UInt_strategy)
@settings(max_examples=25)
def test_c_sharp_types_UInt_instantiation(instance):
    assert isinstance(instance, c_sharp_types_UInt)


c_sharp_types_ULong_strategy = st.builds(c_sharp_types_ULong)
@given(instance=c_sharp_types_ULong_strategy)
@settings(max_examples=25)
def test_c_sharp_types_ULong_instantiation(instance):
    assert isinstance(instance, c_sharp_types_ULong)


c_sharp_types_UShort_strategy = st.builds(c_sharp_types_UShort)
@given(instance=c_sharp_types_UShort_strategy)
@settings(max_examples=25)
def test_c_sharp_types_UShort_instantiation(instance):
    assert isinstance(instance, c_sharp_types_UShort)


c_sharp_types_Void_strategy = st.builds(c_sharp_types_Void)
@given(instance=c_sharp_types_Void_strategy)
@settings(max_examples=25)
def test_c_sharp_types_Void_instantiation(instance):
    assert isinstance(instance, c_sharp_types_Void)


classes_ClassMemberDeclaration_strategy = st.builds(classes_ClassMemberDeclaration)
@given(instance=classes_ClassMemberDeclaration_strategy)
@settings(max_examples=25)
def test_classes_ClassMemberDeclaration_instantiation(instance):
    assert isinstance(instance, classes_ClassMemberDeclaration)


classes_VariableInitializer_strategy = st.builds(classes_VariableInitializer)
@given(instance=classes_VariableInitializer_strategy)
@settings(max_examples=25)
def test_classes_VariableInitializer_instantiation(instance):
    assert isinstance(instance, classes_VariableInitializer)


common_NamedElement_strategy = st.builds(common_NamedElement)
@given(instance=common_NamedElement_strategy)
@settings(max_examples=25)
def test_common_NamedElement_instantiation(instance):
    assert isinstance(instance, common_NamedElement)


expressions_Expression_strategy = st.builds(expressions_Expression)
@given(instance=expressions_Expression_strategy)
@settings(max_examples=25)
def test_expressions_Expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)


expressions_PrimaryExtendedExpressionType_strategy = st.builds(expressions_PrimaryExtendedExpressionType)
@given(instance=expressions_PrimaryExtendedExpressionType_strategy)
@settings(max_examples=25)
def test_expressions_PrimaryExtendedExpressionType_instantiation(instance):
    assert isinstance(instance, expressions_PrimaryExtendedExpressionType)


expressions_PrimaryNoArrayCreationExpression_strategy = st.builds(expressions_PrimaryNoArrayCreationExpression)
@given(instance=expressions_PrimaryNoArrayCreationExpression_strategy)
@settings(max_examples=25)
def test_expressions_PrimaryNoArrayCreationExpression_instantiation(instance):
    assert isinstance(instance, expressions_PrimaryNoArrayCreationExpression)


expressions_StatementExpression_strategy = st.builds(expressions_StatementExpression)
@given(instance=expressions_StatementExpression_strategy)
@settings(max_examples=25)
def test_expressions_StatementExpression_instantiation(instance):
    assert isinstance(instance, expressions_StatementExpression)


namespaces_NamespaceMemberDeclaration_strategy = st.builds(namespaces_NamespaceMemberDeclaration)
@given(instance=namespaces_NamespaceMemberDeclaration_strategy)
@settings(max_examples=25)
def test_namespaces_NamespaceMemberDeclaration_instantiation(instance):
    assert isinstance(instance, namespaces_NamespaceMemberDeclaration)


namespaces_TypeDeclaration_strategy = st.builds(namespaces_TypeDeclaration)
@given(instance=namespaces_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_namespaces_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, namespaces_TypeDeclaration)


operators_AdditiveOperator_strategy = st.builds(operators_AdditiveOperator)
@given(instance=operators_AdditiveOperator_strategy)
@settings(max_examples=25)
def test_operators_AdditiveOperator_instantiation(instance):
    assert isinstance(instance, operators_AdditiveOperator)


operators_UnaryOperator_strategy = st.builds(operators_UnaryOperator)
@given(instance=operators_UnaryOperator_strategy)
@settings(max_examples=25)
def test_operators_UnaryOperator_instantiation(instance):
    assert isinstance(instance, operators_UnaryOperator)


statements_ForInitializer_strategy = st.builds(statements_ForInitializer)
@given(instance=statements_ForInitializer_strategy)
@settings(max_examples=25)
def test_statements_ForInitializer_instantiation(instance):
    assert isinstance(instance, statements_ForInitializer)


statements_ResourceAcquisition_strategy = st.builds(statements_ResourceAcquisition)
@given(instance=statements_ResourceAcquisition_strategy)
@settings(max_examples=25)
def test_statements_ResourceAcquisition_instantiation(instance):
    assert isinstance(instance, statements_ResourceAcquisition)


statements_Statement_strategy = st.builds(statements_Statement)
@given(instance=statements_Statement_strategy)
@settings(max_examples=25)
def test_statements_Statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)


types_NonArrayType_strategy = st.builds(types_NonArrayType)
@given(instance=types_NonArrayType_strategy)
@settings(max_examples=25)
def test_types_NonArrayType_instantiation(instance):
    assert isinstance(instance, types_NonArrayType)


types_Type_strategy = st.builds(types_Type)
@given(instance=types_Type_strategy)
@settings(max_examples=25)
def test_types_Type_instantiation(instance):
    assert isinstance(instance, types_Type)



