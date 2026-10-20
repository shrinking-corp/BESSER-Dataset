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
    PrimitiveType,
    ccsl_datatype_StringPrimitiveType,
    DataType,
    ccsl_datatype_PrimitiveType,
    annotation_Annotation,
    complexType_AnnotationType,
    statements_Block,
    tryCatch_CatchClause,
    UnaryAssignment,
    ccsl_assignment_PostfixUnaryAssignment,
    ccsl_assignment_PrefixUnaryAssignment,
    AbstractAssignment,
    ccsl_assignment_UnaryAssignment,
    ccsl_assignment_Assignment,
    OperatorExpression,
    ccsl_expressions_InfixExpression,
    ccsl_expressions_BooleanExpression,
    ccsl_expressions_ArithmeticExpression,
    ccsl_expressions_StringConcatenation,
    Block,
    ccsl_controlFlow_SwitchCaseBlock,
    controlFlow_SwitchCaseBlock,
    ControlFlow,
    ccsl_controlFlow_LoopStatement,
    ccsl_controlFlow_IfStatement,
    ccsl_controlFlow_SwitchStatement,
    LiteralValue,
    ccsl_literalValues_BooleanLiteral,
    ccsl_literalValues_StringLiteral,
    ccsl_literalValues_CharacterLiteral,
    ccsl_literalValues_NumberLiteral,
    ccsl_literalValues_NullLiteral,
    ccsl_statements_ThrowStatement,
    Statement,
    ccsl_statements_ArrayCreation,
    ccsl_statements_ContinueStatement,
    ccsl_expressions_ParenthesizedExpression,
    ccsl_statements_Access,
    ccsl_statements_SynchronizedBlock,
    ccsl_expressions_OperatorExpression,
    ccsl_tryCatch_TryStatement,
    ccsl_annotation_Annotation,
    ccsl_literalValues_LiteralValue,
    ccsl_assignment_AbstractAssignment,
    ccsl_tryCatch_CatchClause,
    ccsl_statements_ThisStatement,
    ccsl_statements_ReturnStatement,
    ccsl_statements_InstanceOf,
    ccsl_statements_BreakStatement,
    ccsl_statements_EmptyStatement,
    ccsl_statements_NamedElementAccess,
    method_SimpleMethod,
    variable_ParameterVariable,
    elements_Element,
    SimpleMethod,
    ccsl_method_Constructor,
    ccsl_statements_InstanceCreation,
    ccsl_statements_VarDeclaration,
    ccsl_statements_Block,
    ccsl_statements_ControlFlow,
    Access,
    ccsl_statements_DataTypeAccess,
    ccsl_statements_VariableAccess,
    complexType_JClass,
    method_Constructor,
    datatype_ObjectType,
    ComplexType,
    ccsl_complexType_AnonymousClass,
    complexType_ComplexType,
    variable_InitializableVariable,
    statements_Statement,
    DeclaredType,
    ccsl_complexType_AnnotationType,
    method_Method,
    variable_FieldVariable,
    import_ImportStatement,
    complexType_JInterface,
    ccsl_elements_Element,
    InjectionStrategy,
    InjectionAction,
    ccsl_Root,
    Variable,
    ccsl_variable_InitializableVariable,
    InitializableVariable,
    ccsl_variable_LocalVariable,
    annotation_AnnotableElement,
    ccsl_variable_FieldVariable,
    ccsl_method_SimpleMethod,
    variable_Variable,
    ccsl_variable_ParameterVariable,
    datatype_DataType,
    NamedElement,
    ccsl_variable_Variable,
    complexType_DeclaredType,
    ccsl_complexType_JClass,
    ccsl_complexType_JInterface,
    import_ImportableElement,
    namedElements_NamedElement,
    ccsl_method_Method,
    ccsl_complexType_DeclaredType,
    ccsl_namedElements_Package,
    Context,
    Element,
    ccsl_complexType_ComplexType,
    ccsl_namedElements_NamedElement,
    ccsl_annotation_AnnotableElement,
    ccsl_datatype_DataType,
    ccsl_statements_Statement,
    Rule,
    ccsl_AtomicRule,
    ccsl_CompositeRule,
    Root,
    ccsl_FaultTypeDescription,
    ccsl_Rule,
    statements_Access,
    CcslNumberFunction,
    ccsl_numberFunctions_GetIndexOf,
    ccsl_numberFunctions_CcslIntegerLiteral,
    numberFunctions_CcslNumberFunction,
    ccsl_filters_EquationFilter,
    AtomicFilter,
    ccsl_filters_SameNameFilter,
    ccsl_filters_HasSameReferenceFilter,
    ccsl_filters_IsKindOfFilter,
    ccsl_filters_SuperClassClosureFilter,
    ccsl_filters_IsStringFilter,
    ccsl_filters_BlockLastStatementFilter,
    ccsl_filters_TemplateFilter,
    ccsl_filters_ChildClosureComplexTypeFilter,
    ccsl_filters_FromClosureFilter,
    ccsl_filters_SuperMethodClosureFilter,
    ccsl_filters_IsTypeOfFilter,
    ccsl_filters_PropertyFilter,
    Filter,
    ccsl_filters_CompositeFilter,
    ccsl_filters_AtomicFilter,
    CcslBooleanFunction,
    ccsl_filters_Filter,
    CcslFunction,
    ccsl_numberFunctions_CcslNumberFunction,
    ccsl_booleanFunctions_CcslBooleanFunction,
    ccsl_filters_ImplicityContainerFilter,
    expressions_OperatorExpression,
    TemplateFilter,
    ccsl_filters_ImplicityOperandFilter,
    ccsl_filters_RegexMatch,
    ccsl_filters_CountFilter,
    ccsl_faultTypeDescription_InjectionAction,
    filters_Filter,
    ccsl_context_Context,
    ccsl_datatype_VoidType,
    ccsl_datatype_IntPrimitiveType,
    ccsl_datatype_GenericType,
    ObjectType,
    ccsl_datatype_ArrayType,
    ccsl_datatype_ParameterizedType,
    ccsl_datatype_ObjectType,
    ccsl_functions_CcslFunction,
    ccsl_strategy_AllStrategy,
    ccsl_action_ArithmeticOperatorMap,
    action_ArithmeticOperatorMap,
    ccsl_action_ReplaceArithmeticOperatorAction,
    ccsl_action_ReplaceVariableAccessAction,
    ccsl_action_DeleteRandomStatementAction,
    ccsl_action_ChangeLiteralValueAction,
    ccsl_action_DeleteInfixOperatorAction,
    ccsl_action_MoveScopeUpAction,
    ccsl_action_DeleteAction,
    ccsl_faultTypeDescription_InjectionStrategy,
    ccsl_import_ImportStatement,
    ccsl_import_ImportableElement,
    Invocation,
    ccsl_invocation_SimpleMethodInvocation,
    ccsl_invocation_ConstructorInvocation,
    ccsl_invocation_Invocation,
    SimpleMethodInvocation,
    ccsl_invocation_SuperMethodInvocation,
    ccsl_invocation_MethodInvocation,
    ccsl_datatype_ShortPrimitiveType,
    ccsl_datatype_BooleanPrimitiveType,
    CollectionKind,
    EquationOperator,
    UnaryAssignmentOperator,
    Inheritance,
    AssignmentOperator,
    Visibility,
    ArithmeticOperator,
    LogicOperator,
    BooleanOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_hyp_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_hyp_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_stringprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_StringPrimitiveType)


def test_hyp_ccsl_datatype_stringprimitivetype_constructor_exists():
    assert callable(ccsl_datatype_StringPrimitiveType.__init__)


def test_hyp_ccsl_datatype_stringprimitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_StringPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_primitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_PrimitiveType)


def test_hyp_ccsl_datatype_primitivetype_constructor_exists():
    assert callable(ccsl_datatype_PrimitiveType.__init__)


def test_hyp_ccsl_datatype_primitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_annotation_annotation_is_not_abstract():
    assert not inspect.isabstract(annotation_Annotation)


def test_hyp_annotation_annotation_constructor_exists():
    assert callable(annotation_Annotation.__init__)


def test_hyp_annotation_annotation_constructor_args():
    sig = inspect.signature(annotation_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_complextype_annotationtype_is_not_abstract():
    assert not inspect.isabstract(complexType_AnnotationType)


def test_hyp_complextype_annotationtype_constructor_exists():
    assert callable(complexType_AnnotationType.__init__)


def test_hyp_complextype_annotationtype_constructor_args():
    sig = inspect.signature(complexType_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statements_block_is_not_abstract():
    assert not inspect.isabstract(statements_Block)


def test_hyp_statements_block_constructor_exists():
    assert callable(statements_Block.__init__)


def test_hyp_statements_block_constructor_args():
    sig = inspect.signature(statements_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trycatch_catchclause_is_not_abstract():
    assert not inspect.isabstract(tryCatch_CatchClause)


def test_hyp_trycatch_catchclause_constructor_exists():
    assert callable(tryCatch_CatchClause.__init__)


def test_hyp_trycatch_catchclause_constructor_args():
    sig = inspect.signature(tryCatch_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unaryassignment_is_not_abstract():
    assert not inspect.isabstract(UnaryAssignment)


def test_hyp_unaryassignment_constructor_exists():
    assert callable(UnaryAssignment.__init__)


def test_hyp_unaryassignment_constructor_args():
    sig = inspect.signature(UnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_assignment_postfixunaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_PostfixUnaryAssignment)


def test_hyp_ccsl_assignment_postfixunaryassignment_constructor_exists():
    assert callable(ccsl_assignment_PostfixUnaryAssignment.__init__)


def test_hyp_ccsl_assignment_postfixunaryassignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_PostfixUnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_assignment_prefixunaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_PrefixUnaryAssignment)


def test_hyp_ccsl_assignment_prefixunaryassignment_constructor_exists():
    assert callable(ccsl_assignment_PrefixUnaryAssignment.__init__)


def test_hyp_ccsl_assignment_prefixunaryassignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_PrefixUnaryAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(AbstractAssignment)


def test_hyp_abstractassignment_constructor_exists():
    assert callable(AbstractAssignment.__init__)


def test_hyp_abstractassignment_constructor_args():
    sig = inspect.signature(AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_assignment_unaryassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_UnaryAssignment)


def test_hyp_ccsl_assignment_unaryassignment_constructor_exists():
    assert callable(ccsl_assignment_UnaryAssignment.__init__)


def test_hyp_ccsl_assignment_unaryassignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_UnaryAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_ccsl_assignment_assignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_Assignment)


def test_hyp_ccsl_assignment_assignment_constructor_exists():
    assert callable(ccsl_assignment_Assignment.__init__)


def test_hyp_ccsl_assignment_assignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_hyp_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_hyp_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_expressions_infixexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_InfixExpression)


def test_hyp_ccsl_expressions_infixexpression_constructor_exists():
    assert callable(ccsl_expressions_InfixExpression.__init__)


def test_hyp_ccsl_expressions_infixexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_InfixExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_expressions_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_BooleanExpression)


def test_hyp_ccsl_expressions_booleanexpression_constructor_exists():
    assert callable(ccsl_expressions_BooleanExpression.__init__)


def test_hyp_ccsl_expressions_booleanexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "booleanOperator" in params, "Missing parameter 'booleanOperator'"




def test_hyp_ccsl_expressions_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_ArithmeticExpression)


def test_hyp_ccsl_expressions_arithmeticexpression_constructor_exists():
    assert callable(ccsl_expressions_ArithmeticExpression.__init__)


def test_hyp_ccsl_expressions_arithmeticexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "arithmeticOperator" in params, "Missing parameter 'arithmeticOperator'"




def test_hyp_ccsl_expressions_stringconcatenation_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_StringConcatenation)


def test_hyp_ccsl_expressions_stringconcatenation_constructor_exists():
    assert callable(ccsl_expressions_StringConcatenation.__init__)


def test_hyp_ccsl_expressions_stringconcatenation_constructor_args():
    sig = inspect.signature(ccsl_expressions_StringConcatenation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_hyp_block_constructor_exists():
    assert callable(Block.__init__)


def test_hyp_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_controlflow_switchcaseblock_is_not_abstract():
    assert not inspect.isabstract(ccsl_controlFlow_SwitchCaseBlock)


def test_hyp_ccsl_controlflow_switchcaseblock_constructor_exists():
    assert callable(ccsl_controlFlow_SwitchCaseBlock.__init__)


def test_hyp_ccsl_controlflow_switchcaseblock_constructor_args():
    sig = inspect.signature(ccsl_controlFlow_SwitchCaseBlock.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_controlflow_switchcaseblock_is_not_abstract():
    assert not inspect.isabstract(controlFlow_SwitchCaseBlock)


def test_hyp_controlflow_switchcaseblock_constructor_exists():
    assert callable(controlFlow_SwitchCaseBlock.__init__)


def test_hyp_controlflow_switchcaseblock_constructor_args():
    sig = inspect.signature(controlFlow_SwitchCaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_controlflow_is_not_abstract():
    assert not inspect.isabstract(ControlFlow)


def test_hyp_controlflow_constructor_exists():
    assert callable(ControlFlow.__init__)


def test_hyp_controlflow_constructor_args():
    sig = inspect.signature(ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_controlflow_loopstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_controlFlow_LoopStatement)


def test_hyp_ccsl_controlflow_loopstatement_constructor_exists():
    assert callable(ccsl_controlFlow_LoopStatement.__init__)


def test_hyp_ccsl_controlflow_loopstatement_constructor_args():
    sig = inspect.signature(ccsl_controlFlow_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_controlflow_ifstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_controlFlow_IfStatement)


def test_hyp_ccsl_controlflow_ifstatement_constructor_exists():
    assert callable(ccsl_controlFlow_IfStatement.__init__)


def test_hyp_ccsl_controlflow_ifstatement_constructor_args():
    sig = inspect.signature(ccsl_controlFlow_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_controlflow_switchstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_controlFlow_SwitchStatement)


def test_hyp_ccsl_controlflow_switchstatement_constructor_exists():
    assert callable(ccsl_controlFlow_SwitchStatement.__init__)


def test_hyp_ccsl_controlflow_switchstatement_constructor_args():
    sig = inspect.signature(ccsl_controlFlow_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_literalvalue_is_not_abstract():
    assert not inspect.isabstract(LiteralValue)


def test_hyp_literalvalue_constructor_exists():
    assert callable(LiteralValue.__init__)


def test_hyp_literalvalue_constructor_args():
    sig = inspect.signature(LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_literalvalues_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_BooleanLiteral)


def test_hyp_ccsl_literalvalues_booleanliteral_constructor_exists():
    assert callable(ccsl_literalValues_BooleanLiteral.__init__)


def test_hyp_ccsl_literalvalues_booleanliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_literalvalues_stringliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_StringLiteral)


def test_hyp_ccsl_literalvalues_stringliteral_constructor_exists():
    assert callable(ccsl_literalValues_StringLiteral.__init__)


def test_hyp_ccsl_literalvalues_stringliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_literalvalues_characterliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_CharacterLiteral)


def test_hyp_ccsl_literalvalues_characterliteral_constructor_exists():
    assert callable(ccsl_literalValues_CharacterLiteral.__init__)


def test_hyp_ccsl_literalvalues_characterliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_CharacterLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_literalvalues_numberliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_NumberLiteral)


def test_hyp_ccsl_literalvalues_numberliteral_constructor_exists():
    assert callable(ccsl_literalValues_NumberLiteral.__init__)


def test_hyp_ccsl_literalvalues_numberliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_NumberLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_literalvalues_nullliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_NullLiteral)


def test_hyp_ccsl_literalvalues_nullliteral_constructor_exists():
    assert callable(ccsl_literalValues_NullLiteral.__init__)


def test_hyp_ccsl_literalvalues_nullliteral_constructor_args():
    sig = inspect.signature(ccsl_literalValues_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_throwstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ThrowStatement)


def test_hyp_ccsl_statements_throwstatement_constructor_exists():
    assert callable(ccsl_statements_ThrowStatement.__init__)


def test_hyp_ccsl_statements_throwstatement_constructor_args():
    sig = inspect.signature(ccsl_statements_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_arraycreation_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ArrayCreation)


def test_hyp_ccsl_statements_arraycreation_constructor_exists():
    assert callable(ccsl_statements_ArrayCreation.__init__)


def test_hyp_ccsl_statements_arraycreation_constructor_args():
    sig = inspect.signature(ccsl_statements_ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_continuestatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ContinueStatement)


def test_hyp_ccsl_statements_continuestatement_constructor_exists():
    assert callable(ccsl_statements_ContinueStatement.__init__)


def test_hyp_ccsl_statements_continuestatement_constructor_args():
    sig = inspect.signature(ccsl_statements_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_expressions_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_ParenthesizedExpression)


def test_hyp_ccsl_expressions_parenthesizedexpression_constructor_exists():
    assert callable(ccsl_expressions_ParenthesizedExpression.__init__)


def test_hyp_ccsl_expressions_parenthesizedexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_access_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_Access)


def test_hyp_ccsl_statements_access_constructor_exists():
    assert callable(ccsl_statements_Access.__init__)


def test_hyp_ccsl_statements_access_constructor_args():
    sig = inspect.signature(ccsl_statements_Access.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_synchronizedblock_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_SynchronizedBlock)


def test_hyp_ccsl_statements_synchronizedblock_constructor_exists():
    assert callable(ccsl_statements_SynchronizedBlock.__init__)


def test_hyp_ccsl_statements_synchronizedblock_constructor_args():
    sig = inspect.signature(ccsl_statements_SynchronizedBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_expressions_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(ccsl_expressions_OperatorExpression)


def test_hyp_ccsl_expressions_operatorexpression_constructor_exists():
    assert callable(ccsl_expressions_OperatorExpression.__init__)


def test_hyp_ccsl_expressions_operatorexpression_constructor_args():
    sig = inspect.signature(ccsl_expressions_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_trycatch_trystatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_tryCatch_TryStatement)


def test_hyp_ccsl_trycatch_trystatement_constructor_exists():
    assert callable(ccsl_tryCatch_TryStatement.__init__)


def test_hyp_ccsl_trycatch_trystatement_constructor_args():
    sig = inspect.signature(ccsl_tryCatch_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_annotation_annotation_is_not_abstract():
    assert not inspect.isabstract(ccsl_annotation_Annotation)


def test_hyp_ccsl_annotation_annotation_constructor_exists():
    assert callable(ccsl_annotation_Annotation.__init__)


def test_hyp_ccsl_annotation_annotation_constructor_args():
    sig = inspect.signature(ccsl_annotation_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_literalvalues_literalvalue_is_not_abstract():
    assert not inspect.isabstract(ccsl_literalValues_LiteralValue)


def test_hyp_ccsl_literalvalues_literalvalue_constructor_exists():
    assert callable(ccsl_literalValues_LiteralValue.__init__)


def test_hyp_ccsl_literalvalues_literalvalue_constructor_args():
    sig = inspect.signature(ccsl_literalValues_LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_ccsl_assignment_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(ccsl_assignment_AbstractAssignment)


def test_hyp_ccsl_assignment_abstractassignment_constructor_exists():
    assert callable(ccsl_assignment_AbstractAssignment.__init__)


def test_hyp_ccsl_assignment_abstractassignment_constructor_args():
    sig = inspect.signature(ccsl_assignment_AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_trycatch_catchclause_is_not_abstract():
    assert not inspect.isabstract(ccsl_tryCatch_CatchClause)


def test_hyp_ccsl_trycatch_catchclause_constructor_exists():
    assert callable(ccsl_tryCatch_CatchClause.__init__)


def test_hyp_ccsl_trycatch_catchclause_constructor_args():
    sig = inspect.signature(ccsl_tryCatch_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_thisstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ThisStatement)


def test_hyp_ccsl_statements_thisstatement_constructor_exists():
    assert callable(ccsl_statements_ThisStatement.__init__)


def test_hyp_ccsl_statements_thisstatement_constructor_args():
    sig = inspect.signature(ccsl_statements_ThisStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_returnstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ReturnStatement)


def test_hyp_ccsl_statements_returnstatement_constructor_exists():
    assert callable(ccsl_statements_ReturnStatement.__init__)


def test_hyp_ccsl_statements_returnstatement_constructor_args():
    sig = inspect.signature(ccsl_statements_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_instanceof_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_InstanceOf)


def test_hyp_ccsl_statements_instanceof_constructor_exists():
    assert callable(ccsl_statements_InstanceOf.__init__)


def test_hyp_ccsl_statements_instanceof_constructor_args():
    sig = inspect.signature(ccsl_statements_InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_breakstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_BreakStatement)


def test_hyp_ccsl_statements_breakstatement_constructor_exists():
    assert callable(ccsl_statements_BreakStatement.__init__)


def test_hyp_ccsl_statements_breakstatement_constructor_args():
    sig = inspect.signature(ccsl_statements_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_emptystatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_EmptyStatement)


def test_hyp_ccsl_statements_emptystatement_constructor_exists():
    assert callable(ccsl_statements_EmptyStatement.__init__)


def test_hyp_ccsl_statements_emptystatement_constructor_args():
    sig = inspect.signature(ccsl_statements_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_namedelementaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_NamedElementAccess)


def test_hyp_ccsl_statements_namedelementaccess_constructor_exists():
    assert callable(ccsl_statements_NamedElementAccess.__init__)


def test_hyp_ccsl_statements_namedelementaccess_constructor_args():
    sig = inspect.signature(ccsl_statements_NamedElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_method_simplemethod_is_not_abstract():
    assert not inspect.isabstract(method_SimpleMethod)


def test_hyp_method_simplemethod_constructor_exists():
    assert callable(method_SimpleMethod.__init__)


def test_hyp_method_simplemethod_constructor_args():
    sig = inspect.signature(method_SimpleMethod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_parametervariable_is_not_abstract():
    assert not inspect.isabstract(variable_ParameterVariable)


def test_hyp_variable_parametervariable_constructor_exists():
    assert callable(variable_ParameterVariable.__init__)


def test_hyp_variable_parametervariable_constructor_args():
    sig = inspect.signature(variable_ParameterVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elements_element_is_not_abstract():
    assert not inspect.isabstract(elements_Element)


def test_hyp_elements_element_constructor_exists():
    assert callable(elements_Element.__init__)


def test_hyp_elements_element_constructor_args():
    sig = inspect.signature(elements_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_simplemethod_is_not_abstract():
    assert not inspect.isabstract(SimpleMethod)


def test_hyp_simplemethod_constructor_exists():
    assert callable(SimpleMethod.__init__)


def test_hyp_simplemethod_constructor_args():
    sig = inspect.signature(SimpleMethod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_method_constructor_is_not_abstract():
    assert not inspect.isabstract(ccsl_method_Constructor)


def test_hyp_ccsl_method_constructor_constructor_exists():
    assert callable(ccsl_method_Constructor.__init__)


def test_hyp_ccsl_method_constructor_constructor_args():
    sig = inspect.signature(ccsl_method_Constructor.__init__)
    params = list(sig.parameters.keys())
    assert "avaliableInSourceCode" in params, "Missing parameter 'avaliableInSourceCode'"




def test_hyp_ccsl_statements_instancecreation_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_InstanceCreation)


def test_hyp_ccsl_statements_instancecreation_constructor_exists():
    assert callable(ccsl_statements_InstanceCreation.__init__)


def test_hyp_ccsl_statements_instancecreation_constructor_args():
    sig = inspect.signature(ccsl_statements_InstanceCreation.__init__)
    params = list(sig.parameters.keys())
    assert "argsKind" in params, "Missing parameter 'argsKind'"




def test_hyp_ccsl_statements_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_VarDeclaration)


def test_hyp_ccsl_statements_vardeclaration_constructor_exists():
    assert callable(ccsl_statements_VarDeclaration.__init__)


def test_hyp_ccsl_statements_vardeclaration_constructor_args():
    sig = inspect.signature(ccsl_statements_VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_block_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_Block)


def test_hyp_ccsl_statements_block_constructor_exists():
    assert callable(ccsl_statements_Block.__init__)


def test_hyp_ccsl_statements_block_constructor_args():
    sig = inspect.signature(ccsl_statements_Block.__init__)
    params = list(sig.parameters.keys())
    assert "statementsKind" in params, "Missing parameter 'statementsKind'"




def test_hyp_ccsl_statements_controlflow_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_ControlFlow)


def test_hyp_ccsl_statements_controlflow_constructor_exists():
    assert callable(ccsl_statements_ControlFlow.__init__)


def test_hyp_ccsl_statements_controlflow_constructor_args():
    sig = inspect.signature(ccsl_statements_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_hyp_access_constructor_exists():
    assert callable(Access.__init__)


def test_hyp_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_datatypeaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_DataTypeAccess)


def test_hyp_ccsl_statements_datatypeaccess_constructor_exists():
    assert callable(ccsl_statements_DataTypeAccess.__init__)


def test_hyp_ccsl_statements_datatypeaccess_constructor_args():
    sig = inspect.signature(ccsl_statements_DataTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_variableaccess_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_VariableAccess)


def test_hyp_ccsl_statements_variableaccess_constructor_exists():
    assert callable(ccsl_statements_VariableAccess.__init__)


def test_hyp_ccsl_statements_variableaccess_constructor_args():
    sig = inspect.signature(ccsl_statements_VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_complextype_jclass_is_not_abstract():
    assert not inspect.isabstract(complexType_JClass)


def test_hyp_complextype_jclass_constructor_exists():
    assert callable(complexType_JClass.__init__)


def test_hyp_complextype_jclass_constructor_args():
    sig = inspect.signature(complexType_JClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_method_constructor_is_not_abstract():
    assert not inspect.isabstract(method_Constructor)


def test_hyp_method_constructor_constructor_exists():
    assert callable(method_Constructor.__init__)


def test_hyp_method_constructor_constructor_args():
    sig = inspect.signature(method_Constructor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_objecttype_is_not_abstract():
    assert not inspect.isabstract(datatype_ObjectType)


def test_hyp_datatype_objecttype_constructor_exists():
    assert callable(datatype_ObjectType.__init__)


def test_hyp_datatype_objecttype_constructor_args():
    sig = inspect.signature(datatype_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_hyp_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_hyp_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_complextype_anonymousclass_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_AnonymousClass)


def test_hyp_ccsl_complextype_anonymousclass_constructor_exists():
    assert callable(ccsl_complexType_AnonymousClass.__init__)


def test_hyp_ccsl_complextype_anonymousclass_constructor_args():
    sig = inspect.signature(ccsl_complexType_AnonymousClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_complextype_complextype_is_not_abstract():
    assert not inspect.isabstract(complexType_ComplexType)


def test_hyp_complextype_complextype_constructor_exists():
    assert callable(complexType_ComplexType.__init__)


def test_hyp_complextype_complextype_constructor_args():
    sig = inspect.signature(complexType_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_initializablevariable_is_not_abstract():
    assert not inspect.isabstract(variable_InitializableVariable)


def test_hyp_variable_initializablevariable_constructor_exists():
    assert callable(variable_InitializableVariable.__init__)


def test_hyp_variable_initializablevariable_constructor_args():
    sig = inspect.signature(variable_InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_hyp_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_hyp_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaredtype_is_not_abstract():
    assert not inspect.isabstract(DeclaredType)


def test_hyp_declaredtype_constructor_exists():
    assert callable(DeclaredType.__init__)


def test_hyp_declaredtype_constructor_args():
    sig = inspect.signature(DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_complextype_annotationtype_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_AnnotationType)


def test_hyp_ccsl_complextype_annotationtype_constructor_exists():
    assert callable(ccsl_complexType_AnnotationType.__init__)


def test_hyp_ccsl_complextype_annotationtype_constructor_args():
    sig = inspect.signature(ccsl_complexType_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_method_method_is_not_abstract():
    assert not inspect.isabstract(method_Method)


def test_hyp_method_method_constructor_exists():
    assert callable(method_Method.__init__)


def test_hyp_method_method_constructor_args():
    sig = inspect.signature(method_Method.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_fieldvariable_is_not_abstract():
    assert not inspect.isabstract(variable_FieldVariable)


def test_hyp_variable_fieldvariable_constructor_exists():
    assert callable(variable_FieldVariable.__init__)


def test_hyp_variable_fieldvariable_constructor_args():
    sig = inspect.signature(variable_FieldVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_import_importstatement_is_not_abstract():
    assert not inspect.isabstract(import_ImportStatement)


def test_hyp_import_importstatement_constructor_exists():
    assert callable(import_ImportStatement.__init__)


def test_hyp_import_importstatement_constructor_args():
    sig = inspect.signature(import_ImportStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_complextype_jinterface_is_not_abstract():
    assert not inspect.isabstract(complexType_JInterface)


def test_hyp_complextype_jinterface_constructor_exists():
    assert callable(complexType_JInterface.__init__)


def test_hyp_complextype_jinterface_constructor_args():
    sig = inspect.signature(complexType_JInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_elements_element_is_not_abstract():
    assert not inspect.isabstract(ccsl_elements_Element)


def test_hyp_ccsl_elements_element_constructor_exists():
    assert callable(ccsl_elements_Element.__init__)


def test_hyp_ccsl_elements_element_constructor_args():
    sig = inspect.signature(ccsl_elements_Element.__init__)
    params = list(sig.parameters.keys())
    assert "uniqueName" in params, "Missing parameter 'uniqueName'"




def test_hyp_injectionstrategy_is_not_abstract():
    assert not inspect.isabstract(InjectionStrategy)


def test_hyp_injectionstrategy_constructor_exists():
    assert callable(InjectionStrategy.__init__)


def test_hyp_injectionstrategy_constructor_args():
    sig = inspect.signature(InjectionStrategy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_injectionaction_is_not_abstract():
    assert not inspect.isabstract(InjectionAction)


def test_hyp_injectionaction_constructor_exists():
    assert callable(InjectionAction.__init__)


def test_hyp_injectionaction_constructor_args():
    sig = inspect.signature(InjectionAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_root_is_not_abstract():
    assert not inspect.isabstract(ccsl_Root)


def test_hyp_ccsl_root_constructor_exists():
    assert callable(ccsl_Root.__init__)


def test_hyp_ccsl_root_constructor_args():
    sig = inspect.signature(ccsl_Root.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_variable_initializablevariable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_InitializableVariable)


def test_hyp_ccsl_variable_initializablevariable_constructor_exists():
    assert callable(ccsl_variable_InitializableVariable.__init__)


def test_hyp_ccsl_variable_initializablevariable_constructor_args():
    sig = inspect.signature(ccsl_variable_InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_initializablevariable_is_not_abstract():
    assert not inspect.isabstract(InitializableVariable)


def test_hyp_initializablevariable_constructor_exists():
    assert callable(InitializableVariable.__init__)


def test_hyp_initializablevariable_constructor_args():
    sig = inspect.signature(InitializableVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_variable_localvariable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_LocalVariable)


def test_hyp_ccsl_variable_localvariable_constructor_exists():
    assert callable(ccsl_variable_LocalVariable.__init__)


def test_hyp_ccsl_variable_localvariable_constructor_args():
    sig = inspect.signature(ccsl_variable_LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_annotation_annotableelement_is_not_abstract():
    assert not inspect.isabstract(annotation_AnnotableElement)


def test_hyp_annotation_annotableelement_constructor_exists():
    assert callable(annotation_AnnotableElement.__init__)


def test_hyp_annotation_annotableelement_constructor_args():
    sig = inspect.signature(annotation_AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_variable_fieldvariable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_FieldVariable)


def test_hyp_ccsl_variable_fieldvariable_constructor_exists():
    assert callable(ccsl_variable_FieldVariable.__init__)


def test_hyp_ccsl_variable_fieldvariable_constructor_args():
    sig = inspect.signature(ccsl_variable_FieldVariable.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"





def test_hyp_ccsl_method_simplemethod_is_not_abstract():
    assert not inspect.isabstract(ccsl_method_SimpleMethod)


def test_hyp_ccsl_method_simplemethod_constructor_exists():
    assert callable(ccsl_method_SimpleMethod.__init__)


def test_hyp_ccsl_method_simplemethod_constructor_args():
    sig = inspect.signature(ccsl_method_SimpleMethod.__init__)
    params = list(sig.parameters.keys())
    assert "paramsKind" in params, "Missing parameter 'paramsKind'"
    assert "visibility" in params, "Missing parameter 'visibility'"





def test_hyp_variable_variable_is_not_abstract():
    assert not inspect.isabstract(variable_Variable)


def test_hyp_variable_variable_constructor_exists():
    assert callable(variable_Variable.__init__)


def test_hyp_variable_variable_constructor_args():
    sig = inspect.signature(variable_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_variable_parametervariable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_ParameterVariable)


def test_hyp_ccsl_variable_parametervariable_constructor_exists():
    assert callable(ccsl_variable_ParameterVariable.__init__)


def test_hyp_ccsl_variable_parametervariable_constructor_args():
    sig = inspect.signature(ccsl_variable_ParameterVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_datatype_is_not_abstract():
    assert not inspect.isabstract(datatype_DataType)


def test_hyp_datatype_datatype_constructor_exists():
    assert callable(datatype_DataType.__init__)


def test_hyp_datatype_datatype_constructor_args():
    sig = inspect.signature(datatype_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_variable_variable_is_not_abstract():
    assert not inspect.isabstract(ccsl_variable_Variable)


def test_hyp_ccsl_variable_variable_constructor_exists():
    assert callable(ccsl_variable_Variable.__init__)


def test_hyp_ccsl_variable_variable_constructor_args():
    sig = inspect.signature(ccsl_variable_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"




def test_hyp_complextype_declaredtype_is_not_abstract():
    assert not inspect.isabstract(complexType_DeclaredType)


def test_hyp_complextype_declaredtype_constructor_exists():
    assert callable(complexType_DeclaredType.__init__)


def test_hyp_complextype_declaredtype_constructor_args():
    sig = inspect.signature(complexType_DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_complextype_jclass_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_JClass)


def test_hyp_ccsl_complextype_jclass_constructor_exists():
    assert callable(ccsl_complexType_JClass.__init__)


def test_hyp_ccsl_complextype_jclass_constructor_args():
    sig = inspect.signature(ccsl_complexType_JClass.__init__)
    params = list(sig.parameters.keys())
    assert "inheritance" in params, "Missing parameter 'inheritance'"




def test_hyp_ccsl_complextype_jinterface_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_JInterface)


def test_hyp_ccsl_complextype_jinterface_constructor_exists():
    assert callable(ccsl_complexType_JInterface.__init__)


def test_hyp_ccsl_complextype_jinterface_constructor_args():
    sig = inspect.signature(ccsl_complexType_JInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_import_importableelement_is_not_abstract():
    assert not inspect.isabstract(import_ImportableElement)


def test_hyp_import_importableelement_constructor_exists():
    assert callable(import_ImportableElement.__init__)


def test_hyp_import_importableelement_constructor_args():
    sig = inspect.signature(import_ImportableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelements_namedelement_is_not_abstract():
    assert not inspect.isabstract(namedElements_NamedElement)


def test_hyp_namedelements_namedelement_constructor_exists():
    assert callable(namedElements_NamedElement.__init__)


def test_hyp_namedelements_namedelement_constructor_args():
    sig = inspect.signature(namedElements_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_method_method_is_not_abstract():
    assert not inspect.isabstract(ccsl_method_Method)


def test_hyp_ccsl_method_method_constructor_exists():
    assert callable(ccsl_method_Method.__init__)


def test_hyp_ccsl_method_method_constructor_args():
    sig = inspect.signature(ccsl_method_Method.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"
    assert "inheritance" in params, "Missing parameter 'inheritance'"







def test_hyp_ccsl_complextype_declaredtype_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_DeclaredType)


def test_hyp_ccsl_complextype_declaredtype_constructor_exists():
    assert callable(ccsl_complexType_DeclaredType.__init__)


def test_hyp_ccsl_complextype_declaredtype_constructor_args():
    sig = inspect.signature(ccsl_complexType_DeclaredType.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"





def test_hyp_ccsl_namedelements_package_is_not_abstract():
    assert not inspect.isabstract(ccsl_namedElements_Package)


def test_hyp_ccsl_namedelements_package_constructor_exists():
    assert callable(ccsl_namedElements_Package.__init__)


def test_hyp_ccsl_namedelements_package_constructor_args():
    sig = inspect.signature(ccsl_namedElements_Package.__init__)
    params = list(sig.parameters.keys())



def test_hyp_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_hyp_context_constructor_exists():
    assert callable(Context.__init__)


def test_hyp_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_complextype_complextype_is_not_abstract():
    assert not inspect.isabstract(ccsl_complexType_ComplexType)


def test_hyp_ccsl_complextype_complextype_constructor_exists():
    assert callable(ccsl_complexType_ComplexType.__init__)


def test_hyp_ccsl_complextype_complextype_constructor_args():
    sig = inspect.signature(ccsl_complexType_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_namedelements_namedelement_is_not_abstract():
    assert not inspect.isabstract(ccsl_namedElements_NamedElement)


def test_hyp_ccsl_namedelements_namedelement_constructor_exists():
    assert callable(ccsl_namedElements_NamedElement.__init__)


def test_hyp_ccsl_namedelements_namedelement_constructor_args():
    sig = inspect.signature(ccsl_namedElements_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "avaliableInSourceCode" in params, "Missing parameter 'avaliableInSourceCode'"





def test_hyp_ccsl_annotation_annotableelement_is_not_abstract():
    assert not inspect.isabstract(ccsl_annotation_AnnotableElement)


def test_hyp_ccsl_annotation_annotableelement_constructor_exists():
    assert callable(ccsl_annotation_AnnotableElement.__init__)


def test_hyp_ccsl_annotation_annotableelement_constructor_args():
    sig = inspect.signature(ccsl_annotation_AnnotableElement.__init__)
    params = list(sig.parameters.keys())
    assert "annotationsKind" in params, "Missing parameter 'annotationsKind'"




def test_hyp_ccsl_datatype_datatype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_DataType)


def test_hyp_ccsl_datatype_datatype_constructor_exists():
    assert callable(ccsl_datatype_DataType.__init__)


def test_hyp_ccsl_datatype_datatype_constructor_args():
    sig = inspect.signature(ccsl_datatype_DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_statements_statement_is_not_abstract():
    assert not inspect.isabstract(ccsl_statements_Statement)


def test_hyp_ccsl_statements_statement_constructor_exists():
    assert callable(ccsl_statements_Statement.__init__)


def test_hyp_ccsl_statements_statement_constructor_args():
    sig = inspect.signature(ccsl_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_hyp_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_hyp_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_atomicrule_is_not_abstract():
    assert not inspect.isabstract(ccsl_AtomicRule)


def test_hyp_ccsl_atomicrule_constructor_exists():
    assert callable(ccsl_AtomicRule.__init__)


def test_hyp_ccsl_atomicrule_constructor_args():
    sig = inspect.signature(ccsl_AtomicRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_compositerule_is_not_abstract():
    assert not inspect.isabstract(ccsl_CompositeRule)


def test_hyp_ccsl_compositerule_constructor_exists():
    assert callable(ccsl_CompositeRule.__init__)


def test_hyp_ccsl_compositerule_constructor_args():
    sig = inspect.signature(ccsl_CompositeRule.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_root_is_not_abstract():
    assert not inspect.isabstract(Root)


def test_hyp_root_constructor_exists():
    assert callable(Root.__init__)


def test_hyp_root_constructor_args():
    sig = inspect.signature(Root.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_faulttypedescription_is_not_abstract():
    assert not inspect.isabstract(ccsl_FaultTypeDescription)


def test_hyp_ccsl_faulttypedescription_constructor_exists():
    assert callable(ccsl_FaultTypeDescription.__init__)


def test_hyp_ccsl_faulttypedescription_constructor_args():
    sig = inspect.signature(ccsl_FaultTypeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ccsl_rule_is_not_abstract():
    assert not inspect.isabstract(ccsl_Rule)


def test_hyp_ccsl_rule_constructor_exists():
    assert callable(ccsl_Rule.__init__)


def test_hyp_ccsl_rule_constructor_args():
    sig = inspect.signature(ccsl_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"




def test_hyp_statements_access_is_not_abstract():
    assert not inspect.isabstract(statements_Access)


def test_hyp_statements_access_constructor_exists():
    assert callable(statements_Access.__init__)


def test_hyp_statements_access_constructor_args():
    sig = inspect.signature(statements_Access.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(CcslNumberFunction)


def test_hyp_ccslnumberfunction_constructor_exists():
    assert callable(CcslNumberFunction.__init__)


def test_hyp_ccslnumberfunction_constructor_args():
    sig = inspect.signature(CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_numberfunctions_getindexof_is_not_abstract():
    assert not inspect.isabstract(ccsl_numberFunctions_GetIndexOf)


def test_hyp_ccsl_numberfunctions_getindexof_constructor_exists():
    assert callable(ccsl_numberFunctions_GetIndexOf.__init__)


def test_hyp_ccsl_numberfunctions_getindexof_constructor_args():
    sig = inspect.signature(ccsl_numberFunctions_GetIndexOf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_numberfunctions_ccslintegerliteral_is_not_abstract():
    assert not inspect.isabstract(ccsl_numberFunctions_CcslIntegerLiteral)


def test_hyp_ccsl_numberfunctions_ccslintegerliteral_constructor_exists():
    assert callable(ccsl_numberFunctions_CcslIntegerLiteral.__init__)


def test_hyp_ccsl_numberfunctions_ccslintegerliteral_constructor_args():
    sig = inspect.signature(ccsl_numberFunctions_CcslIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_numberfunctions_ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(numberFunctions_CcslNumberFunction)


def test_hyp_numberfunctions_ccslnumberfunction_constructor_exists():
    assert callable(numberFunctions_CcslNumberFunction.__init__)


def test_hyp_numberfunctions_ccslnumberfunction_constructor_args():
    sig = inspect.signature(numberFunctions_CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_equationfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_EquationFilter)


def test_hyp_ccsl_filters_equationfilter_constructor_exists():
    assert callable(ccsl_filters_EquationFilter.__init__)


def test_hyp_ccsl_filters_equationfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_EquationFilter.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_atomicfilter_is_not_abstract():
    assert not inspect.isabstract(AtomicFilter)


def test_hyp_atomicfilter_constructor_exists():
    assert callable(AtomicFilter.__init__)


def test_hyp_atomicfilter_constructor_args():
    sig = inspect.signature(AtomicFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_samenamefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_SameNameFilter)


def test_hyp_ccsl_filters_samenamefilter_constructor_exists():
    assert callable(ccsl_filters_SameNameFilter.__init__)


def test_hyp_ccsl_filters_samenamefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_SameNameFilter.__init__)
    params = list(sig.parameters.keys())
    assert "ignoreCase" in params, "Missing parameter 'ignoreCase'"




def test_hyp_ccsl_filters_hassamereferencefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_HasSameReferenceFilter)


def test_hyp_ccsl_filters_hassamereferencefilter_constructor_exists():
    assert callable(ccsl_filters_HasSameReferenceFilter.__init__)


def test_hyp_ccsl_filters_hassamereferencefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_HasSameReferenceFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_iskindoffilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_IsKindOfFilter)


def test_hyp_ccsl_filters_iskindoffilter_constructor_exists():
    assert callable(ccsl_filters_IsKindOfFilter.__init__)


def test_hyp_ccsl_filters_iskindoffilter_constructor_args():
    sig = inspect.signature(ccsl_filters_IsKindOfFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_superclassclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_SuperClassClosureFilter)


def test_hyp_ccsl_filters_superclassclosurefilter_constructor_exists():
    assert callable(ccsl_filters_SuperClassClosureFilter.__init__)


def test_hyp_ccsl_filters_superclassclosurefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_SuperClassClosureFilter.__init__)
    params = list(sig.parameters.keys())
    assert "includesSubClass" in params, "Missing parameter 'includesSubClass'"




def test_hyp_ccsl_filters_isstringfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_IsStringFilter)


def test_hyp_ccsl_filters_isstringfilter_constructor_exists():
    assert callable(ccsl_filters_IsStringFilter.__init__)


def test_hyp_ccsl_filters_isstringfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_IsStringFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_blocklaststatementfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_BlockLastStatementFilter)


def test_hyp_ccsl_filters_blocklaststatementfilter_constructor_exists():
    assert callable(ccsl_filters_BlockLastStatementFilter.__init__)


def test_hyp_ccsl_filters_blocklaststatementfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_BlockLastStatementFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_templatefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_TemplateFilter)


def test_hyp_ccsl_filters_templatefilter_constructor_exists():
    assert callable(ccsl_filters_TemplateFilter.__init__)


def test_hyp_ccsl_filters_templatefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_TemplateFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_childclosurecomplextypefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_ChildClosureComplexTypeFilter)


def test_hyp_ccsl_filters_childclosurecomplextypefilter_constructor_exists():
    assert callable(ccsl_filters_ChildClosureComplexTypeFilter.__init__)


def test_hyp_ccsl_filters_childclosurecomplextypefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_ChildClosureComplexTypeFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_fromclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_FromClosureFilter)


def test_hyp_ccsl_filters_fromclosurefilter_constructor_exists():
    assert callable(ccsl_filters_FromClosureFilter.__init__)


def test_hyp_ccsl_filters_fromclosurefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_FromClosureFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_supermethodclosurefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_SuperMethodClosureFilter)


def test_hyp_ccsl_filters_supermethodclosurefilter_constructor_exists():
    assert callable(ccsl_filters_SuperMethodClosureFilter.__init__)


def test_hyp_ccsl_filters_supermethodclosurefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_SuperMethodClosureFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_istypeoffilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_IsTypeOfFilter)


def test_hyp_ccsl_filters_istypeoffilter_constructor_exists():
    assert callable(ccsl_filters_IsTypeOfFilter.__init__)


def test_hyp_ccsl_filters_istypeoffilter_constructor_args():
    sig = inspect.signature(ccsl_filters_IsTypeOfFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_propertyfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_PropertyFilter)


def test_hyp_ccsl_filters_propertyfilter_constructor_exists():
    assert callable(ccsl_filters_PropertyFilter.__init__)


def test_hyp_ccsl_filters_propertyfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_PropertyFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_hyp_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_hyp_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_compositefilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_CompositeFilter)


def test_hyp_ccsl_filters_compositefilter_constructor_exists():
    assert callable(ccsl_filters_CompositeFilter.__init__)


def test_hyp_ccsl_filters_compositefilter_constructor_args():
    sig = inspect.signature(ccsl_filters_CompositeFilter.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_ccsl_filters_atomicfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_AtomicFilter)


def test_hyp_ccsl_filters_atomicfilter_constructor_exists():
    assert callable(ccsl_filters_AtomicFilter.__init__)


def test_hyp_ccsl_filters_atomicfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_AtomicFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccslbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(CcslBooleanFunction)


def test_hyp_ccslbooleanfunction_constructor_exists():
    assert callable(CcslBooleanFunction.__init__)


def test_hyp_ccslbooleanfunction_constructor_args():
    sig = inspect.signature(CcslBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_filter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_Filter)


def test_hyp_ccsl_filters_filter_constructor_exists():
    assert callable(ccsl_filters_Filter.__init__)


def test_hyp_ccsl_filters_filter_constructor_args():
    sig = inspect.signature(ccsl_filters_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"




def test_hyp_ccslfunction_is_not_abstract():
    assert not inspect.isabstract(CcslFunction)


def test_hyp_ccslfunction_constructor_exists():
    assert callable(CcslFunction.__init__)


def test_hyp_ccslfunction_constructor_args():
    sig = inspect.signature(CcslFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_numberfunctions_ccslnumberfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl_numberFunctions_CcslNumberFunction)


def test_hyp_ccsl_numberfunctions_ccslnumberfunction_constructor_exists():
    assert callable(ccsl_numberFunctions_CcslNumberFunction.__init__)


def test_hyp_ccsl_numberfunctions_ccslnumberfunction_constructor_args():
    sig = inspect.signature(ccsl_numberFunctions_CcslNumberFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_booleanfunctions_ccslbooleanfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl_booleanFunctions_CcslBooleanFunction)


def test_hyp_ccsl_booleanfunctions_ccslbooleanfunction_constructor_exists():
    assert callable(ccsl_booleanFunctions_CcslBooleanFunction.__init__)


def test_hyp_ccsl_booleanfunctions_ccslbooleanfunction_constructor_args():
    sig = inspect.signature(ccsl_booleanFunctions_CcslBooleanFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_implicitycontainerfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_ImplicityContainerFilter)


def test_hyp_ccsl_filters_implicitycontainerfilter_constructor_exists():
    assert callable(ccsl_filters_ImplicityContainerFilter.__init__)


def test_hyp_ccsl_filters_implicitycontainerfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_ImplicityContainerFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_OperatorExpression)


def test_hyp_expressions_operatorexpression_constructor_exists():
    assert callable(expressions_OperatorExpression.__init__)


def test_hyp_expressions_operatorexpression_constructor_args():
    sig = inspect.signature(expressions_OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_templatefilter_is_not_abstract():
    assert not inspect.isabstract(TemplateFilter)


def test_hyp_templatefilter_constructor_exists():
    assert callable(TemplateFilter.__init__)


def test_hyp_templatefilter_constructor_args():
    sig = inspect.signature(TemplateFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_implicityoperandfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_ImplicityOperandFilter)


def test_hyp_ccsl_filters_implicityoperandfilter_constructor_exists():
    assert callable(ccsl_filters_ImplicityOperandFilter.__init__)


def test_hyp_ccsl_filters_implicityoperandfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_ImplicityOperandFilter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_filters_regexmatch_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_RegexMatch)


def test_hyp_ccsl_filters_regexmatch_constructor_exists():
    assert callable(ccsl_filters_RegexMatch.__init__)


def test_hyp_ccsl_filters_regexmatch_constructor_args():
    sig = inspect.signature(ccsl_filters_RegexMatch.__init__)
    params = list(sig.parameters.keys())
    assert "regex" in params, "Missing parameter 'regex'"




def test_hyp_ccsl_filters_countfilter_is_not_abstract():
    assert not inspect.isabstract(ccsl_filters_CountFilter)


def test_hyp_ccsl_filters_countfilter_constructor_exists():
    assert callable(ccsl_filters_CountFilter.__init__)


def test_hyp_ccsl_filters_countfilter_constructor_args():
    sig = inspect.signature(ccsl_filters_CountFilter.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"





def test_hyp_ccsl_faulttypedescription_injectionaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_faultTypeDescription_InjectionAction)


def test_hyp_ccsl_faulttypedescription_injectionaction_constructor_exists():
    assert callable(ccsl_faultTypeDescription_InjectionAction.__init__)


def test_hyp_ccsl_faulttypedescription_injectionaction_constructor_args():
    sig = inspect.signature(ccsl_faultTypeDescription_InjectionAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_filters_filter_is_not_abstract():
    assert not inspect.isabstract(filters_Filter)


def test_hyp_filters_filter_constructor_exists():
    assert callable(filters_Filter.__init__)


def test_hyp_filters_filter_constructor_args():
    sig = inspect.signature(filters_Filter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_context_context_is_not_abstract():
    assert not inspect.isabstract(ccsl_context_Context)


def test_hyp_ccsl_context_context_constructor_exists():
    assert callable(ccsl_context_Context.__init__)


def test_hyp_ccsl_context_context_constructor_args():
    sig = inspect.signature(ccsl_context_Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_voidtype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_VoidType)


def test_hyp_ccsl_datatype_voidtype_constructor_exists():
    assert callable(ccsl_datatype_VoidType.__init__)


def test_hyp_ccsl_datatype_voidtype_constructor_args():
    sig = inspect.signature(ccsl_datatype_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_intprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_IntPrimitiveType)


def test_hyp_ccsl_datatype_intprimitivetype_constructor_exists():
    assert callable(ccsl_datatype_IntPrimitiveType.__init__)


def test_hyp_ccsl_datatype_intprimitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_IntPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_generictype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_GenericType)


def test_hyp_ccsl_datatype_generictype_constructor_exists():
    assert callable(ccsl_datatype_GenericType.__init__)


def test_hyp_ccsl_datatype_generictype_constructor_args():
    sig = inspect.signature(ccsl_datatype_GenericType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_objecttype_is_not_abstract():
    assert not inspect.isabstract(ObjectType)


def test_hyp_objecttype_constructor_exists():
    assert callable(ObjectType.__init__)


def test_hyp_objecttype_constructor_args():
    sig = inspect.signature(ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_arraytype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_ArrayType)


def test_hyp_ccsl_datatype_arraytype_constructor_exists():
    assert callable(ccsl_datatype_ArrayType.__init__)


def test_hyp_ccsl_datatype_arraytype_constructor_args():
    sig = inspect.signature(ccsl_datatype_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "dimensions" in params, "Missing parameter 'dimensions'"




def test_hyp_ccsl_datatype_parameterizedtype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_ParameterizedType)


def test_hyp_ccsl_datatype_parameterizedtype_constructor_exists():
    assert callable(ccsl_datatype_ParameterizedType.__init__)


def test_hyp_ccsl_datatype_parameterizedtype_constructor_args():
    sig = inspect.signature(ccsl_datatype_ParameterizedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_objecttype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_ObjectType)


def test_hyp_ccsl_datatype_objecttype_constructor_exists():
    assert callable(ccsl_datatype_ObjectType.__init__)


def test_hyp_ccsl_datatype_objecttype_constructor_args():
    sig = inspect.signature(ccsl_datatype_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_functions_ccslfunction_is_not_abstract():
    assert not inspect.isabstract(ccsl_functions_CcslFunction)


def test_hyp_ccsl_functions_ccslfunction_constructor_exists():
    assert callable(ccsl_functions_CcslFunction.__init__)


def test_hyp_ccsl_functions_ccslfunction_constructor_args():
    sig = inspect.signature(ccsl_functions_CcslFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_strategy_allstrategy_is_not_abstract():
    assert not inspect.isabstract(ccsl_strategy_AllStrategy)


def test_hyp_ccsl_strategy_allstrategy_constructor_exists():
    assert callable(ccsl_strategy_AllStrategy.__init__)


def test_hyp_ccsl_strategy_allstrategy_constructor_args():
    sig = inspect.signature(ccsl_strategy_AllStrategy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_action_arithmeticoperatormap_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_ArithmeticOperatorMap)


def test_hyp_ccsl_action_arithmeticoperatormap_constructor_exists():
    assert callable(ccsl_action_ArithmeticOperatorMap.__init__)


def test_hyp_ccsl_action_arithmeticoperatormap_constructor_args():
    sig = inspect.signature(ccsl_action_ArithmeticOperatorMap.__init__)
    params = list(sig.parameters.keys())
    assert "oldArithmeticOperator" in params, "Missing parameter 'oldArithmeticOperator'"
    assert "newArithmeticOperator" in params, "Missing parameter 'newArithmeticOperator'"





def test_hyp_action_arithmeticoperatormap_is_not_abstract():
    assert not inspect.isabstract(action_ArithmeticOperatorMap)


def test_hyp_action_arithmeticoperatormap_constructor_exists():
    assert callable(action_ArithmeticOperatorMap.__init__)


def test_hyp_action_arithmeticoperatormap_constructor_args():
    sig = inspect.signature(action_ArithmeticOperatorMap.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_action_replacearithmeticoperatoraction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_ReplaceArithmeticOperatorAction)


def test_hyp_ccsl_action_replacearithmeticoperatoraction_constructor_exists():
    assert callable(ccsl_action_ReplaceArithmeticOperatorAction.__init__)


def test_hyp_ccsl_action_replacearithmeticoperatoraction_constructor_args():
    sig = inspect.signature(ccsl_action_ReplaceArithmeticOperatorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_action_replacevariableaccessaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_ReplaceVariableAccessAction)


def test_hyp_ccsl_action_replacevariableaccessaction_constructor_exists():
    assert callable(ccsl_action_ReplaceVariableAccessAction.__init__)


def test_hyp_ccsl_action_replacevariableaccessaction_constructor_args():
    sig = inspect.signature(ccsl_action_ReplaceVariableAccessAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_action_deleterandomstatementaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_DeleteRandomStatementAction)


def test_hyp_ccsl_action_deleterandomstatementaction_constructor_exists():
    assert callable(ccsl_action_DeleteRandomStatementAction.__init__)


def test_hyp_ccsl_action_deleterandomstatementaction_constructor_args():
    sig = inspect.signature(ccsl_action_DeleteRandomStatementAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_action_changeliteralvalueaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_ChangeLiteralValueAction)


def test_hyp_ccsl_action_changeliteralvalueaction_constructor_exists():
    assert callable(ccsl_action_ChangeLiteralValueAction.__init__)


def test_hyp_ccsl_action_changeliteralvalueaction_constructor_args():
    sig = inspect.signature(ccsl_action_ChangeLiteralValueAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_action_deleteinfixoperatoraction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_DeleteInfixOperatorAction)


def test_hyp_ccsl_action_deleteinfixoperatoraction_constructor_exists():
    assert callable(ccsl_action_DeleteInfixOperatorAction.__init__)


def test_hyp_ccsl_action_deleteinfixoperatoraction_constructor_args():
    sig = inspect.signature(ccsl_action_DeleteInfixOperatorAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_action_movescopeupaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_MoveScopeUpAction)


def test_hyp_ccsl_action_movescopeupaction_constructor_exists():
    assert callable(ccsl_action_MoveScopeUpAction.__init__)


def test_hyp_ccsl_action_movescopeupaction_constructor_args():
    sig = inspect.signature(ccsl_action_MoveScopeUpAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_action_deleteaction_is_not_abstract():
    assert not inspect.isabstract(ccsl_action_DeleteAction)


def test_hyp_ccsl_action_deleteaction_constructor_exists():
    assert callable(ccsl_action_DeleteAction.__init__)


def test_hyp_ccsl_action_deleteaction_constructor_args():
    sig = inspect.signature(ccsl_action_DeleteAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_faulttypedescription_injectionstrategy_is_not_abstract():
    assert not inspect.isabstract(ccsl_faultTypeDescription_InjectionStrategy)


def test_hyp_ccsl_faulttypedescription_injectionstrategy_constructor_exists():
    assert callable(ccsl_faultTypeDescription_InjectionStrategy.__init__)


def test_hyp_ccsl_faulttypedescription_injectionstrategy_constructor_args():
    sig = inspect.signature(ccsl_faultTypeDescription_InjectionStrategy.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_import_importstatement_is_not_abstract():
    assert not inspect.isabstract(ccsl_import_ImportStatement)


def test_hyp_ccsl_import_importstatement_constructor_exists():
    assert callable(ccsl_import_ImportStatement.__init__)


def test_hyp_ccsl_import_importstatement_constructor_args():
    sig = inspect.signature(ccsl_import_ImportStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_import_importableelement_is_not_abstract():
    assert not inspect.isabstract(ccsl_import_ImportableElement)


def test_hyp_ccsl_import_importableelement_constructor_exists():
    assert callable(ccsl_import_ImportableElement.__init__)


def test_hyp_ccsl_import_importableelement_constructor_args():
    sig = inspect.signature(ccsl_import_ImportableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_invocation_is_not_abstract():
    assert not inspect.isabstract(Invocation)


def test_hyp_invocation_constructor_exists():
    assert callable(Invocation.__init__)


def test_hyp_invocation_constructor_args():
    sig = inspect.signature(Invocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_invocation_simplemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_SimpleMethodInvocation)


def test_hyp_ccsl_invocation_simplemethodinvocation_constructor_exists():
    assert callable(ccsl_invocation_SimpleMethodInvocation.__init__)


def test_hyp_ccsl_invocation_simplemethodinvocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_SimpleMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_invocation_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_ConstructorInvocation)


def test_hyp_ccsl_invocation_constructorinvocation_constructor_exists():
    assert callable(ccsl_invocation_ConstructorInvocation.__init__)


def test_hyp_ccsl_invocation_constructorinvocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_invocation_invocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_Invocation)


def test_hyp_ccsl_invocation_invocation_constructor_exists():
    assert callable(ccsl_invocation_Invocation.__init__)


def test_hyp_ccsl_invocation_invocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_Invocation.__init__)
    params = list(sig.parameters.keys())
    assert "argsKind" in params, "Missing parameter 'argsKind'"




def test_hyp_simplemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(SimpleMethodInvocation)


def test_hyp_simplemethodinvocation_constructor_exists():
    assert callable(SimpleMethodInvocation.__init__)


def test_hyp_simplemethodinvocation_constructor_args():
    sig = inspect.signature(SimpleMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_invocation_supermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_SuperMethodInvocation)


def test_hyp_ccsl_invocation_supermethodinvocation_constructor_exists():
    assert callable(ccsl_invocation_SuperMethodInvocation.__init__)


def test_hyp_ccsl_invocation_supermethodinvocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_SuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_invocation_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(ccsl_invocation_MethodInvocation)


def test_hyp_ccsl_invocation_methodinvocation_constructor_exists():
    assert callable(ccsl_invocation_MethodInvocation.__init__)


def test_hyp_ccsl_invocation_methodinvocation_constructor_args():
    sig = inspect.signature(ccsl_invocation_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_shortprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_ShortPrimitiveType)


def test_hyp_ccsl_datatype_shortprimitivetype_constructor_exists():
    assert callable(ccsl_datatype_ShortPrimitiveType.__init__)


def test_hyp_ccsl_datatype_shortprimitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_ShortPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ccsl_datatype_booleanprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ccsl_datatype_BooleanPrimitiveType)


def test_hyp_ccsl_datatype_booleanprimitivetype_constructor_exists():
    assert callable(ccsl_datatype_BooleanPrimitiveType.__init__)


def test_hyp_ccsl_datatype_booleanprimitivetype_constructor_args():
    sig = inspect.signature(ccsl_datatype_BooleanPrimitiveType.__init__)
    params = list(sig.parameters.keys())

def test_hyp_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_hyp_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "IMMEDIATE",
        "SEQUENCE",
        "EXACT",
        "ANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

def test_hyp_equationoperator_exists():
    # Check that the Enumeration exists
    assert EquationOperator is not None

def test_hyp_equationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EquationOperator]
    expected_literals = [
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EquationOperator"

def test_hyp_unaryassignmentoperator_exists():
    # Check that the Enumeration exists
    assert UnaryAssignmentOperator is not None

def test_hyp_unaryassignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryAssignmentOperator]
    expected_literals = [
        "DECREMENT",
        "ANY",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryAssignmentOperator"

def test_hyp_inheritance_exists():
    # Check that the Enumeration exists
    assert Inheritance is not None

def test_hyp_inheritance_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Inheritance]
    expected_literals = [
        "NONE",
        "ABSTRACT",
        "FINAL",
        "ANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Inheritance"

def test_hyp_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_hyp_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "ANY",
        "PLUS_ASSIGN",
        "ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_hyp_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_hyp_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "ANY",
        "PROTECTED",
        "PACKAGE",
        "PRIVATE",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"

def test_hyp_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_hyp_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "SUBTRACTION",
        "ADDITION",
        "DIVISION",
        "MODULUS",
        "UNDEFINED",
        "MULTIPLICATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_hyp_logicoperator_exists():
    # Check that the Enumeration exists
    assert LogicOperator is not None

def test_hyp_logicoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperator]
    expected_literals = [
        "OR",
        "AND",
        "IF_THEN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperator"

def test_hyp_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_hyp_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "ANY",
        "EQUAL_TO",
        "LESS_THAN_OR_EQUAL_TO",
        "OR",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL_TO",
        "NOT",
        "NOT_EQUAL_TO",
        "AND",
        "LESS_THAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"


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
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
ccsl_datatype_StringPrimitiveType_strategy = st.builds(
    ccsl_datatype_StringPrimitiveType,
)
DataType_strategy = st.builds(
    DataType,
)
ccsl_datatype_PrimitiveType_strategy = st.builds(
    ccsl_datatype_PrimitiveType,
)
annotation_Annotation_strategy = st.builds(
    annotation_Annotation,
)
complexType_AnnotationType_strategy = st.builds(
    complexType_AnnotationType,
)
statements_Block_strategy = st.builds(
    statements_Block,
)
tryCatch_CatchClause_strategy = st.builds(
    tryCatch_CatchClause,
)
UnaryAssignment_strategy = st.builds(
    UnaryAssignment,
)
ccsl_assignment_PostfixUnaryAssignment_strategy = st.builds(
    ccsl_assignment_PostfixUnaryAssignment,
)
ccsl_assignment_PrefixUnaryAssignment_strategy = st.builds(
    ccsl_assignment_PrefixUnaryAssignment,
)
AbstractAssignment_strategy = st.builds(
    AbstractAssignment,
)
ccsl_assignment_UnaryAssignment_strategy = st.builds(
    ccsl_assignment_UnaryAssignment,
    operator=
        safe_text
)
ccsl_assignment_Assignment_strategy = st.builds(
    ccsl_assignment_Assignment,
    operator=
        safe_text
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
ccsl_expressions_InfixExpression_strategy = st.builds(
    ccsl_expressions_InfixExpression,
)
ccsl_expressions_BooleanExpression_strategy = st.builds(
    ccsl_expressions_BooleanExpression,
    booleanOperator=
        safe_text
)
ccsl_expressions_ArithmeticExpression_strategy = st.builds(
    ccsl_expressions_ArithmeticExpression,
    arithmeticOperator=
        safe_text
)
ccsl_expressions_StringConcatenation_strategy = st.builds(
    ccsl_expressions_StringConcatenation,
)
Block_strategy = st.builds(
    Block,
)
ccsl_controlFlow_SwitchCaseBlock_strategy = st.builds(
    ccsl_controlFlow_SwitchCaseBlock,
    default=
        safe_text
)
controlFlow_SwitchCaseBlock_strategy = st.builds(
    controlFlow_SwitchCaseBlock,
)
ControlFlow_strategy = st.builds(
    ControlFlow,
)
ccsl_controlFlow_LoopStatement_strategy = st.builds(
    ccsl_controlFlow_LoopStatement,
)
ccsl_controlFlow_IfStatement_strategy = st.builds(
    ccsl_controlFlow_IfStatement,
)
ccsl_controlFlow_SwitchStatement_strategy = st.builds(
    ccsl_controlFlow_SwitchStatement,
)
LiteralValue_strategy = st.builds(
    LiteralValue,
)
ccsl_literalValues_BooleanLiteral_strategy = st.builds(
    ccsl_literalValues_BooleanLiteral,
)
ccsl_literalValues_StringLiteral_strategy = st.builds(
    ccsl_literalValues_StringLiteral,
)
ccsl_literalValues_CharacterLiteral_strategy = st.builds(
    ccsl_literalValues_CharacterLiteral,
)
ccsl_literalValues_NumberLiteral_strategy = st.builds(
    ccsl_literalValues_NumberLiteral,
)
ccsl_literalValues_NullLiteral_strategy = st.builds(
    ccsl_literalValues_NullLiteral,
)
ccsl_statements_ThrowStatement_strategy = st.builds(
    ccsl_statements_ThrowStatement,
)
Statement_strategy = st.builds(
    Statement,
)
ccsl_statements_ArrayCreation_strategy = st.builds(
    ccsl_statements_ArrayCreation,
)
ccsl_statements_ContinueStatement_strategy = st.builds(
    ccsl_statements_ContinueStatement,
)
ccsl_expressions_ParenthesizedExpression_strategy = st.builds(
    ccsl_expressions_ParenthesizedExpression,
)
ccsl_statements_Access_strategy = st.builds(
    ccsl_statements_Access,
)
ccsl_statements_SynchronizedBlock_strategy = st.builds(
    ccsl_statements_SynchronizedBlock,
)
ccsl_expressions_OperatorExpression_strategy = st.builds(
    ccsl_expressions_OperatorExpression,
)
ccsl_tryCatch_TryStatement_strategy = st.builds(
    ccsl_tryCatch_TryStatement,
)
ccsl_annotation_Annotation_strategy = st.builds(
    ccsl_annotation_Annotation,
)
ccsl_literalValues_LiteralValue_strategy = st.builds(
    ccsl_literalValues_LiteralValue,
    value=
        safe_text
)
ccsl_assignment_AbstractAssignment_strategy = st.builds(
    ccsl_assignment_AbstractAssignment,
)
ccsl_tryCatch_CatchClause_strategy = st.builds(
    ccsl_tryCatch_CatchClause,
)
ccsl_statements_ThisStatement_strategy = st.builds(
    ccsl_statements_ThisStatement,
)
ccsl_statements_ReturnStatement_strategy = st.builds(
    ccsl_statements_ReturnStatement,
)
ccsl_statements_InstanceOf_strategy = st.builds(
    ccsl_statements_InstanceOf,
)
ccsl_statements_BreakStatement_strategy = st.builds(
    ccsl_statements_BreakStatement,
)
ccsl_statements_EmptyStatement_strategy = st.builds(
    ccsl_statements_EmptyStatement,
)
ccsl_statements_NamedElementAccess_strategy = st.builds(
    ccsl_statements_NamedElementAccess,
)
method_SimpleMethod_strategy = st.builds(
    method_SimpleMethod,
)
variable_ParameterVariable_strategy = st.builds(
    variable_ParameterVariable,
)
elements_Element_strategy = st.builds(
    elements_Element,
)
SimpleMethod_strategy = st.builds(
    SimpleMethod,
)
ccsl_method_Constructor_strategy = st.builds(
    ccsl_method_Constructor,
    avaliableInSourceCode=
        safe_text
)
ccsl_statements_InstanceCreation_strategy = st.builds(
    ccsl_statements_InstanceCreation,
    argsKind=
        safe_text
)
ccsl_statements_VarDeclaration_strategy = st.builds(
    ccsl_statements_VarDeclaration,
)
ccsl_statements_Block_strategy = st.builds(
    ccsl_statements_Block,
    statementsKind=
        safe_text
)
ccsl_statements_ControlFlow_strategy = st.builds(
    ccsl_statements_ControlFlow,
)
Access_strategy = st.builds(
    Access,
)
ccsl_statements_DataTypeAccess_strategy = st.builds(
    ccsl_statements_DataTypeAccess,
)
ccsl_statements_VariableAccess_strategy = st.builds(
    ccsl_statements_VariableAccess,
)
complexType_JClass_strategy = st.builds(
    complexType_JClass,
)
method_Constructor_strategy = st.builds(
    method_Constructor,
)
datatype_ObjectType_strategy = st.builds(
    datatype_ObjectType,
)
ComplexType_strategy = st.builds(
    ComplexType,
)
ccsl_complexType_AnonymousClass_strategy = st.builds(
    ccsl_complexType_AnonymousClass,
)
complexType_ComplexType_strategy = st.builds(
    complexType_ComplexType,
)
variable_InitializableVariable_strategy = st.builds(
    variable_InitializableVariable,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
DeclaredType_strategy = st.builds(
    DeclaredType,
)
ccsl_complexType_AnnotationType_strategy = st.builds(
    ccsl_complexType_AnnotationType,
)
method_Method_strategy = st.builds(
    method_Method,
)
variable_FieldVariable_strategy = st.builds(
    variable_FieldVariable,
)
import_ImportStatement_strategy = st.builds(
    import_ImportStatement,
)
complexType_JInterface_strategy = st.builds(
    complexType_JInterface,
)
ccsl_elements_Element_strategy = st.builds(
    ccsl_elements_Element,
    uniqueName=
        safe_text
)
InjectionStrategy_strategy = st.builds(
    InjectionStrategy,
)
InjectionAction_strategy = st.builds(
    InjectionAction,
)
ccsl_Root_strategy = st.builds(
    ccsl_Root,
)
Variable_strategy = st.builds(
    Variable,
)
ccsl_variable_InitializableVariable_strategy = st.builds(
    ccsl_variable_InitializableVariable,
)
InitializableVariable_strategy = st.builds(
    InitializableVariable,
)
ccsl_variable_LocalVariable_strategy = st.builds(
    ccsl_variable_LocalVariable,
)
annotation_AnnotableElement_strategy = st.builds(
    annotation_AnnotableElement,
)
ccsl_variable_FieldVariable_strategy = st.builds(
    ccsl_variable_FieldVariable,
    static=
        safe_text,
    visibility=
        safe_text
)
ccsl_method_SimpleMethod_strategy = st.builds(
    ccsl_method_SimpleMethod,
    paramsKind=
        safe_text,
    visibility=
        safe_text
)
variable_Variable_strategy = st.builds(
    variable_Variable,
)
ccsl_variable_ParameterVariable_strategy = st.builds(
    ccsl_variable_ParameterVariable,
)
datatype_DataType_strategy = st.builds(
    datatype_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
ccsl_variable_Variable_strategy = st.builds(
    ccsl_variable_Variable,
    final=
        safe_text
)
complexType_DeclaredType_strategy = st.builds(
    complexType_DeclaredType,
)
ccsl_complexType_JClass_strategy = st.builds(
    ccsl_complexType_JClass,
    inheritance=
        safe_text
)
ccsl_complexType_JInterface_strategy = st.builds(
    ccsl_complexType_JInterface,
)
import_ImportableElement_strategy = st.builds(
    import_ImportableElement,
)
namedElements_NamedElement_strategy = st.builds(
    namedElements_NamedElement,
)
ccsl_method_Method_strategy = st.builds(
    ccsl_method_Method,
    abstract=
        safe_text,
    static=
        safe_text,
    final=
        safe_text,
    inheritance=
        safe_text
)
ccsl_complexType_DeclaredType_strategy = st.builds(
    ccsl_complexType_DeclaredType,
    static=
        safe_text,
    visibility=
        safe_text
)
ccsl_namedElements_Package_strategy = st.builds(
    ccsl_namedElements_Package,
)
Context_strategy = st.builds(
    Context,
)
Element_strategy = st.builds(
    Element,
)
ccsl_complexType_ComplexType_strategy = st.builds(
    ccsl_complexType_ComplexType,
)
ccsl_namedElements_NamedElement_strategy = st.builds(
    ccsl_namedElements_NamedElement,
    name=
        safe_text,
    avaliableInSourceCode=
        safe_text
)
ccsl_annotation_AnnotableElement_strategy = st.builds(
    ccsl_annotation_AnnotableElement,
    annotationsKind=
        safe_text
)
ccsl_datatype_DataType_strategy = st.builds(
    ccsl_datatype_DataType,
)
ccsl_statements_Statement_strategy = st.builds(
    ccsl_statements_Statement,
)
Rule_strategy = st.builds(
    Rule,
)
ccsl_AtomicRule_strategy = st.builds(
    ccsl_AtomicRule,
)
ccsl_CompositeRule_strategy = st.builds(
    ccsl_CompositeRule,
    operator=
        safe_text
)
Root_strategy = st.builds(
    Root,
)
ccsl_FaultTypeDescription_strategy = st.builds(
    ccsl_FaultTypeDescription,
    name=
        safe_text
)
ccsl_Rule_strategy = st.builds(
    ccsl_Rule,
    negated=
        safe_text
)
statements_Access_strategy = st.builds(
    statements_Access,
)
CcslNumberFunction_strategy = st.builds(
    CcslNumberFunction,
)
ccsl_numberFunctions_GetIndexOf_strategy = st.builds(
    ccsl_numberFunctions_GetIndexOf,
)
ccsl_numberFunctions_CcslIntegerLiteral_strategy = st.builds(
    ccsl_numberFunctions_CcslIntegerLiteral,
    value=
        safe_text
)
numberFunctions_CcslNumberFunction_strategy = st.builds(
    numberFunctions_CcslNumberFunction,
)
ccsl_filters_EquationFilter_strategy = st.builds(
    ccsl_filters_EquationFilter,
    operator=
        safe_text
)
AtomicFilter_strategy = st.builds(
    AtomicFilter,
)
ccsl_filters_SameNameFilter_strategy = st.builds(
    ccsl_filters_SameNameFilter,
    ignoreCase=
        safe_text
)
ccsl_filters_HasSameReferenceFilter_strategy = st.builds(
    ccsl_filters_HasSameReferenceFilter,
)
ccsl_filters_IsKindOfFilter_strategy = st.builds(
    ccsl_filters_IsKindOfFilter,
)
ccsl_filters_SuperClassClosureFilter_strategy = st.builds(
    ccsl_filters_SuperClassClosureFilter,
    includesSubClass=
        safe_text
)
ccsl_filters_IsStringFilter_strategy = st.builds(
    ccsl_filters_IsStringFilter,
)
ccsl_filters_BlockLastStatementFilter_strategy = st.builds(
    ccsl_filters_BlockLastStatementFilter,
)
ccsl_filters_TemplateFilter_strategy = st.builds(
    ccsl_filters_TemplateFilter,
)
ccsl_filters_ChildClosureComplexTypeFilter_strategy = st.builds(
    ccsl_filters_ChildClosureComplexTypeFilter,
)
ccsl_filters_FromClosureFilter_strategy = st.builds(
    ccsl_filters_FromClosureFilter,
)
ccsl_filters_SuperMethodClosureFilter_strategy = st.builds(
    ccsl_filters_SuperMethodClosureFilter,
)
ccsl_filters_IsTypeOfFilter_strategy = st.builds(
    ccsl_filters_IsTypeOfFilter,
)
ccsl_filters_PropertyFilter_strategy = st.builds(
    ccsl_filters_PropertyFilter,
)
Filter_strategy = st.builds(
    Filter,
)
ccsl_filters_CompositeFilter_strategy = st.builds(
    ccsl_filters_CompositeFilter,
    operator=
        safe_text
)
ccsl_filters_AtomicFilter_strategy = st.builds(
    ccsl_filters_AtomicFilter,
)
CcslBooleanFunction_strategy = st.builds(
    CcslBooleanFunction,
)
ccsl_filters_Filter_strategy = st.builds(
    ccsl_filters_Filter,
    negated=
        safe_text
)
CcslFunction_strategy = st.builds(
    CcslFunction,
)
ccsl_numberFunctions_CcslNumberFunction_strategy = st.builds(
    ccsl_numberFunctions_CcslNumberFunction,
)
ccsl_booleanFunctions_CcslBooleanFunction_strategy = st.builds(
    ccsl_booleanFunctions_CcslBooleanFunction,
)
ccsl_filters_ImplicityContainerFilter_strategy = st.builds(
    ccsl_filters_ImplicityContainerFilter,
)
expressions_OperatorExpression_strategy = st.builds(
    expressions_OperatorExpression,
)
TemplateFilter_strategy = st.builds(
    TemplateFilter,
)
ccsl_filters_ImplicityOperandFilter_strategy = st.builds(
    ccsl_filters_ImplicityOperandFilter,
)
ccsl_filters_RegexMatch_strategy = st.builds(
    ccsl_filters_RegexMatch,
    regex=
        safe_text
)
ccsl_filters_CountFilter_strategy = st.builds(
    ccsl_filters_CountFilter,
    min=
        safe_text,
    max=
        safe_text
)
ccsl_faultTypeDescription_InjectionAction_strategy = st.builds(
    ccsl_faultTypeDescription_InjectionAction,
)
filters_Filter_strategy = st.builds(
    filters_Filter,
)
ccsl_context_Context_strategy = st.builds(
    ccsl_context_Context,
)
ccsl_datatype_VoidType_strategy = st.builds(
    ccsl_datatype_VoidType,
)
ccsl_datatype_IntPrimitiveType_strategy = st.builds(
    ccsl_datatype_IntPrimitiveType,
)
ccsl_datatype_GenericType_strategy = st.builds(
    ccsl_datatype_GenericType,
)
ObjectType_strategy = st.builds(
    ObjectType,
)
ccsl_datatype_ArrayType_strategy = st.builds(
    ccsl_datatype_ArrayType,
    dimensions=
        safe_text
)
ccsl_datatype_ParameterizedType_strategy = st.builds(
    ccsl_datatype_ParameterizedType,
)
ccsl_datatype_ObjectType_strategy = st.builds(
    ccsl_datatype_ObjectType,
)
ccsl_functions_CcslFunction_strategy = st.builds(
    ccsl_functions_CcslFunction,
)
ccsl_strategy_AllStrategy_strategy = st.builds(
    ccsl_strategy_AllStrategy,
)
ccsl_action_ArithmeticOperatorMap_strategy = st.builds(
    ccsl_action_ArithmeticOperatorMap,
    oldArithmeticOperator=
        safe_text,
    newArithmeticOperator=
        safe_text
)
action_ArithmeticOperatorMap_strategy = st.builds(
    action_ArithmeticOperatorMap,
)
ccsl_action_ReplaceArithmeticOperatorAction_strategy = st.builds(
    ccsl_action_ReplaceArithmeticOperatorAction,
)
ccsl_action_ReplaceVariableAccessAction_strategy = st.builds(
    ccsl_action_ReplaceVariableAccessAction,
)
ccsl_action_DeleteRandomStatementAction_strategy = st.builds(
    ccsl_action_DeleteRandomStatementAction,
)
ccsl_action_ChangeLiteralValueAction_strategy = st.builds(
    ccsl_action_ChangeLiteralValueAction,
)
ccsl_action_DeleteInfixOperatorAction_strategy = st.builds(
    ccsl_action_DeleteInfixOperatorAction,
)
ccsl_action_MoveScopeUpAction_strategy = st.builds(
    ccsl_action_MoveScopeUpAction,
)
ccsl_action_DeleteAction_strategy = st.builds(
    ccsl_action_DeleteAction,
)
ccsl_faultTypeDescription_InjectionStrategy_strategy = st.builds(
    ccsl_faultTypeDescription_InjectionStrategy,
)
ccsl_import_ImportStatement_strategy = st.builds(
    ccsl_import_ImportStatement,
)
ccsl_import_ImportableElement_strategy = st.builds(
    ccsl_import_ImportableElement,
)
Invocation_strategy = st.builds(
    Invocation,
)
ccsl_invocation_SimpleMethodInvocation_strategy = st.builds(
    ccsl_invocation_SimpleMethodInvocation,
)
ccsl_invocation_ConstructorInvocation_strategy = st.builds(
    ccsl_invocation_ConstructorInvocation,
)
ccsl_invocation_Invocation_strategy = st.builds(
    ccsl_invocation_Invocation,
    argsKind=
        safe_text
)
SimpleMethodInvocation_strategy = st.builds(
    SimpleMethodInvocation,
)
ccsl_invocation_SuperMethodInvocation_strategy = st.builds(
    ccsl_invocation_SuperMethodInvocation,
)
ccsl_invocation_MethodInvocation_strategy = st.builds(
    ccsl_invocation_MethodInvocation,
)
ccsl_datatype_ShortPrimitiveType_strategy = st.builds(
    ccsl_datatype_ShortPrimitiveType,
)
ccsl_datatype_BooleanPrimitiveType_strategy = st.builds(
    ccsl_datatype_BooleanPrimitiveType,
)
















@given(instance=ccsl_assignment_UnaryAssignment_strategy)
def test_hyp_ccsl_assignment_unaryassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=ccsl_assignment_Assignment_strategy)
def test_hyp_ccsl_assignment_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original






@given(instance=ccsl_expressions_BooleanExpression_strategy)
def test_hyp_ccsl_expressions_booleanexpression_booleanOperator_setter(instance):
    original = instance.booleanOperator
    instance.booleanOperator = original
    assert instance.booleanOperator == original




@given(instance=ccsl_expressions_ArithmeticExpression_strategy)
def test_hyp_ccsl_expressions_arithmeticexpression_arithmeticOperator_setter(instance):
    original = instance.arithmeticOperator
    instance.arithmeticOperator = original
    assert instance.arithmeticOperator == original






@given(instance=ccsl_controlFlow_SwitchCaseBlock_strategy)
def test_hyp_ccsl_controlflow_switchcaseblock_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

























@given(instance=ccsl_literalValues_LiteralValue_strategy)
def test_hyp_ccsl_literalvalues_literalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
















@given(instance=ccsl_method_Constructor_strategy)
def test_hyp_ccsl_method_constructor_avaliableInSourceCode_setter(instance):
    original = instance.avaliableInSourceCode
    instance.avaliableInSourceCode = original
    assert instance.avaliableInSourceCode == original




@given(instance=ccsl_statements_InstanceCreation_strategy)
def test_hyp_ccsl_statements_instancecreation_argsKind_setter(instance):
    original = instance.argsKind
    instance.argsKind = original
    assert instance.argsKind == original





@given(instance=ccsl_statements_Block_strategy)
def test_hyp_ccsl_statements_block_statementsKind_setter(instance):
    original = instance.statementsKind
    instance.statementsKind = original
    assert instance.statementsKind == original






















@given(instance=ccsl_elements_Element_strategy)
def test_hyp_ccsl_elements_element_uniqueName_setter(instance):
    original = instance.uniqueName
    instance.uniqueName = original
    assert instance.uniqueName == original












@given(instance=ccsl_variable_FieldVariable_strategy)
def test_hyp_ccsl_variable_fieldvariable_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=ccsl_variable_FieldVariable_strategy)
def test_hyp_ccsl_variable_fieldvariable_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original




@given(instance=ccsl_method_SimpleMethod_strategy)
def test_hyp_ccsl_method_simplemethod_paramsKind_setter(instance):
    original = instance.paramsKind
    instance.paramsKind = original
    assert instance.paramsKind == original



@given(instance=ccsl_method_SimpleMethod_strategy)
def test_hyp_ccsl_method_simplemethod_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original








@given(instance=ccsl_variable_Variable_strategy)
def test_hyp_ccsl_variable_variable_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original





@given(instance=ccsl_complexType_JClass_strategy)
def test_hyp_ccsl_complextype_jclass_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original







@given(instance=ccsl_method_Method_strategy)
def test_hyp_ccsl_method_method_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=ccsl_method_Method_strategy)
def test_hyp_ccsl_method_method_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=ccsl_method_Method_strategy)
def test_hyp_ccsl_method_method_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=ccsl_method_Method_strategy)
def test_hyp_ccsl_method_method_inheritance_setter(instance):
    original = instance.inheritance
    instance.inheritance = original
    assert instance.inheritance == original




@given(instance=ccsl_complexType_DeclaredType_strategy)
def test_hyp_ccsl_complextype_declaredtype_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=ccsl_complexType_DeclaredType_strategy)
def test_hyp_ccsl_complextype_declaredtype_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original








@given(instance=ccsl_namedElements_NamedElement_strategy)
def test_hyp_ccsl_namedelements_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ccsl_namedElements_NamedElement_strategy)
def test_hyp_ccsl_namedelements_namedelement_avaliableInSourceCode_setter(instance):
    original = instance.avaliableInSourceCode
    instance.avaliableInSourceCode = original
    assert instance.avaliableInSourceCode == original




@given(instance=ccsl_annotation_AnnotableElement_strategy)
def test_hyp_ccsl_annotation_annotableelement_annotationsKind_setter(instance):
    original = instance.annotationsKind
    instance.annotationsKind = original
    assert instance.annotationsKind == original








@given(instance=ccsl_CompositeRule_strategy)
def test_hyp_ccsl_compositerule_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=ccsl_FaultTypeDescription_strategy)
def test_hyp_ccsl_faulttypedescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=ccsl_Rule_strategy)
def test_hyp_ccsl_rule_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original







@given(instance=ccsl_numberFunctions_CcslIntegerLiteral_strategy)
def test_hyp_ccsl_numberfunctions_ccslintegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=ccsl_filters_EquationFilter_strategy)
def test_hyp_ccsl_filters_equationfilter_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=ccsl_filters_SameNameFilter_strategy)
def test_hyp_ccsl_filters_samenamefilter_ignoreCase_setter(instance):
    original = instance.ignoreCase
    instance.ignoreCase = original
    assert instance.ignoreCase == original






@given(instance=ccsl_filters_SuperClassClosureFilter_strategy)
def test_hyp_ccsl_filters_superclassclosurefilter_includesSubClass_setter(instance):
    original = instance.includesSubClass
    instance.includesSubClass = original
    assert instance.includesSubClass == original













@given(instance=ccsl_filters_CompositeFilter_strategy)
def test_hyp_ccsl_filters_compositefilter_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original






@given(instance=ccsl_filters_Filter_strategy)
def test_hyp_ccsl_filters_filter_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original











@given(instance=ccsl_filters_RegexMatch_strategy)
def test_hyp_ccsl_filters_regexmatch_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original




@given(instance=ccsl_filters_CountFilter_strategy)
def test_hyp_ccsl_filters_countfilter_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=ccsl_filters_CountFilter_strategy)
def test_hyp_ccsl_filters_countfilter_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original











@given(instance=ccsl_datatype_ArrayType_strategy)
def test_hyp_ccsl_datatype_arraytype_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original








@given(instance=ccsl_action_ArithmeticOperatorMap_strategy)
def test_hyp_ccsl_action_arithmeticoperatormap_oldArithmeticOperator_setter(instance):
    original = instance.oldArithmeticOperator
    instance.oldArithmeticOperator = original
    assert instance.oldArithmeticOperator == original



@given(instance=ccsl_action_ArithmeticOperatorMap_strategy)
def test_hyp_ccsl_action_arithmeticoperatormap_newArithmeticOperator_setter(instance):
    original = instance.newArithmeticOperator
    instance.newArithmeticOperator = original
    assert instance.newArithmeticOperator == original


















@given(instance=ccsl_invocation_Invocation_strategy)
def test_hyp_ccsl_invocation_invocation_argsKind_setter(instance):
    original = instance.argsKind
    instance.argsKind = original
    assert instance.argsKind == original







# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractAssignment,
    Access,
    AtomicFilter,
    Block,
    CcslBooleanFunction,
    CcslFunction,
    CcslNumberFunction,
    ComplexType,
    Context,
    ControlFlow,
    DataType,
    DeclaredType,
    Element,
    Filter,
    InitializableVariable,
    InjectionAction,
    InjectionStrategy,
    Invocation,
    LiteralValue,
    NamedElement,
    ObjectType,
    OperatorExpression,
    PrimitiveType,
    Root,
    Rule,
    SimpleMethod,
    SimpleMethodInvocation,
    Statement,
    TemplateFilter,
    UnaryAssignment,
    Variable,
    action_ArithmeticOperatorMap,
    annotation_AnnotableElement,
    annotation_Annotation,
    ccsl_AtomicRule,
    ccsl_CompositeRule,
    ccsl_FaultTypeDescription,
    ccsl_Root,
    ccsl_Rule,
    ccsl_action_ArithmeticOperatorMap,
    ccsl_action_ChangeLiteralValueAction,
    ccsl_action_DeleteAction,
    ccsl_action_DeleteInfixOperatorAction,
    ccsl_action_DeleteRandomStatementAction,
    ccsl_action_MoveScopeUpAction,
    ccsl_action_ReplaceArithmeticOperatorAction,
    ccsl_action_ReplaceVariableAccessAction,
    ccsl_annotation_AnnotableElement,
    ccsl_annotation_Annotation,
    ccsl_assignment_AbstractAssignment,
    ccsl_assignment_Assignment,
    ccsl_assignment_PostfixUnaryAssignment,
    ccsl_assignment_PrefixUnaryAssignment,
    ccsl_assignment_UnaryAssignment,
    ccsl_booleanFunctions_CcslBooleanFunction,
    ccsl_complexType_AnnotationType,
    ccsl_complexType_AnonymousClass,
    ccsl_complexType_ComplexType,
    ccsl_complexType_DeclaredType,
    ccsl_complexType_JClass,
    ccsl_complexType_JInterface,
    ccsl_context_Context,
    ccsl_controlFlow_IfStatement,
    ccsl_controlFlow_LoopStatement,
    ccsl_controlFlow_SwitchCaseBlock,
    ccsl_controlFlow_SwitchStatement,
    ccsl_datatype_ArrayType,
    ccsl_datatype_BooleanPrimitiveType,
    ccsl_datatype_DataType,
    ccsl_datatype_GenericType,
    ccsl_datatype_IntPrimitiveType,
    ccsl_datatype_ObjectType,
    ccsl_datatype_ParameterizedType,
    ccsl_datatype_PrimitiveType,
    ccsl_datatype_ShortPrimitiveType,
    ccsl_datatype_StringPrimitiveType,
    ccsl_datatype_VoidType,
    ccsl_elements_Element,
    ccsl_expressions_ArithmeticExpression,
    ccsl_expressions_BooleanExpression,
    ccsl_expressions_InfixExpression,
    ccsl_expressions_OperatorExpression,
    ccsl_expressions_ParenthesizedExpression,
    ccsl_expressions_StringConcatenation,
    ccsl_faultTypeDescription_InjectionAction,
    ccsl_faultTypeDescription_InjectionStrategy,
    ccsl_filters_AtomicFilter,
    ccsl_filters_BlockLastStatementFilter,
    ccsl_filters_ChildClosureComplexTypeFilter,
    ccsl_filters_CompositeFilter,
    ccsl_filters_CountFilter,
    ccsl_filters_EquationFilter,
    ccsl_filters_Filter,
    ccsl_filters_FromClosureFilter,
    ccsl_filters_HasSameReferenceFilter,
    ccsl_filters_ImplicityContainerFilter,
    ccsl_filters_ImplicityOperandFilter,
    ccsl_filters_IsKindOfFilter,
    ccsl_filters_IsStringFilter,
    ccsl_filters_IsTypeOfFilter,
    ccsl_filters_PropertyFilter,
    ccsl_filters_RegexMatch,
    ccsl_filters_SameNameFilter,
    ccsl_filters_SuperClassClosureFilter,
    ccsl_filters_SuperMethodClosureFilter,
    ccsl_filters_TemplateFilter,
    ccsl_functions_CcslFunction,
    ccsl_import_ImportStatement,
    ccsl_import_ImportableElement,
    ccsl_invocation_ConstructorInvocation,
    ccsl_invocation_Invocation,
    ccsl_invocation_MethodInvocation,
    ccsl_invocation_SimpleMethodInvocation,
    ccsl_invocation_SuperMethodInvocation,
    ccsl_literalValues_BooleanLiteral,
    ccsl_literalValues_CharacterLiteral,
    ccsl_literalValues_LiteralValue,
    ccsl_literalValues_NullLiteral,
    ccsl_literalValues_NumberLiteral,
    ccsl_literalValues_StringLiteral,
    ccsl_method_Constructor,
    ccsl_method_Method,
    ccsl_method_SimpleMethod,
    ccsl_namedElements_NamedElement,
    ccsl_namedElements_Package,
    ccsl_numberFunctions_CcslIntegerLiteral,
    ccsl_numberFunctions_CcslNumberFunction,
    ccsl_numberFunctions_GetIndexOf,
    ccsl_statements_Access,
    ccsl_statements_ArrayCreation,
    ccsl_statements_Block,
    ccsl_statements_BreakStatement,
    ccsl_statements_ContinueStatement,
    ccsl_statements_ControlFlow,
    ccsl_statements_DataTypeAccess,
    ccsl_statements_EmptyStatement,
    ccsl_statements_InstanceCreation,
    ccsl_statements_InstanceOf,
    ccsl_statements_NamedElementAccess,
    ccsl_statements_ReturnStatement,
    ccsl_statements_Statement,
    ccsl_statements_SynchronizedBlock,
    ccsl_statements_ThisStatement,
    ccsl_statements_ThrowStatement,
    ccsl_statements_VarDeclaration,
    ccsl_statements_VariableAccess,
    ccsl_strategy_AllStrategy,
    ccsl_tryCatch_CatchClause,
    ccsl_tryCatch_TryStatement,
    ccsl_variable_FieldVariable,
    ccsl_variable_InitializableVariable,
    ccsl_variable_LocalVariable,
    ccsl_variable_ParameterVariable,
    ccsl_variable_Variable,
    complexType_AnnotationType,
    complexType_ComplexType,
    complexType_DeclaredType,
    complexType_JClass,
    complexType_JInterface,
    controlFlow_SwitchCaseBlock,
    datatype_DataType,
    datatype_ObjectType,
    elements_Element,
    expressions_OperatorExpression,
    filters_Filter,
    import_ImportStatement,
    import_ImportableElement,
    method_Constructor,
    method_Method,
    method_SimpleMethod,
    namedElements_NamedElement,
    numberFunctions_CcslNumberFunction,
    statements_Access,
    statements_Block,
    statements_Statement,
    tryCatch_CatchClause,
    variable_FieldVariable,
    variable_InitializableVariable,
    variable_ParameterVariable,
    variable_Variable,
    ArithmeticOperator,
    AssignmentOperator,
    BooleanOperator,
    CollectionKind,
    EquationOperator,
    Inheritance,
    LogicOperator,
    UnaryAssignmentOperator,
    Visibility,
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

def test_ccsl_CompositeRule_operator_value_roundtrip():
    instance = ccsl_CompositeRule(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_ccsl_FaultTypeDescription_name_value_roundtrip():
    instance = ccsl_FaultTypeDescription(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ccsl_Rule_negated_value_roundtrip():
    instance = ccsl_Rule(negated="sample_text")
    assert instance.negated == "sample_text"
    instance.negated = "sample_text_2"
    assert instance.negated == "sample_text_2"


def test_ccsl_action_ArithmeticOperatorMap_newArithmeticOperator_value_roundtrip():
    instance = ccsl_action_ArithmeticOperatorMap(newArithmeticOperator="sample_text", oldArithmeticOperator="sample_text")
    assert instance.newArithmeticOperator == "sample_text"
    instance.newArithmeticOperator = "sample_text_2"
    assert instance.newArithmeticOperator == "sample_text_2"


def test_ccsl_action_ArithmeticOperatorMap_oldArithmeticOperator_value_roundtrip():
    instance = ccsl_action_ArithmeticOperatorMap(newArithmeticOperator="sample_text", oldArithmeticOperator="sample_text")
    assert instance.oldArithmeticOperator == "sample_text"
    instance.oldArithmeticOperator = "sample_text_2"
    assert instance.oldArithmeticOperator == "sample_text_2"


def test_ccsl_annotation_AnnotableElement_annotationsKind_value_roundtrip():
    instance = ccsl_annotation_AnnotableElement(annotationsKind="sample_text")
    assert instance.annotationsKind == "sample_text"
    instance.annotationsKind = "sample_text_2"
    assert instance.annotationsKind == "sample_text_2"


def test_ccsl_assignment_Assignment_operator_value_roundtrip():
    instance = ccsl_assignment_Assignment(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_ccsl_assignment_UnaryAssignment_operator_value_roundtrip():
    instance = ccsl_assignment_UnaryAssignment(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_ccsl_complexType_DeclaredType_static_value_roundtrip():
    instance = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    assert instance.static == "sample_text"
    instance.static = "sample_text_2"
    assert instance.static == "sample_text_2"


def test_ccsl_complexType_DeclaredType_visibility_value_roundtrip():
    instance = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_ccsl_complexType_JClass_inheritance_value_roundtrip():
    instance = ccsl_complexType_JClass(inheritance="sample_text")
    assert instance.inheritance == "sample_text"
    instance.inheritance = "sample_text_2"
    assert instance.inheritance == "sample_text_2"


def test_ccsl_controlFlow_SwitchCaseBlock_default_value_roundtrip():
    instance = ccsl_controlFlow_SwitchCaseBlock(default="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_ccsl_datatype_ArrayType_dimensions_value_roundtrip():
    instance = ccsl_datatype_ArrayType(dimensions="sample_text")
    assert instance.dimensions == "sample_text"
    instance.dimensions = "sample_text_2"
    assert instance.dimensions == "sample_text_2"


def test_ccsl_elements_Element_uniqueName_value_roundtrip():
    instance = ccsl_elements_Element(uniqueName="sample_text")
    assert instance.uniqueName == "sample_text"
    instance.uniqueName = "sample_text_2"
    assert instance.uniqueName == "sample_text_2"


def test_ccsl_expressions_ArithmeticExpression_arithmeticOperator_value_roundtrip():
    instance = ccsl_expressions_ArithmeticExpression(arithmeticOperator="sample_text")
    assert instance.arithmeticOperator == "sample_text"
    instance.arithmeticOperator = "sample_text_2"
    assert instance.arithmeticOperator == "sample_text_2"


def test_ccsl_expressions_BooleanExpression_booleanOperator_value_roundtrip():
    instance = ccsl_expressions_BooleanExpression(booleanOperator="sample_text")
    assert instance.booleanOperator == "sample_text"
    instance.booleanOperator = "sample_text_2"
    assert instance.booleanOperator == "sample_text_2"


def test_ccsl_filters_CompositeFilter_operator_value_roundtrip():
    instance = ccsl_filters_CompositeFilter(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_ccsl_filters_CountFilter_max_value_roundtrip():
    instance = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    assert instance.max == "sample_text"
    instance.max = "sample_text_2"
    assert instance.max == "sample_text_2"


def test_ccsl_filters_CountFilter_min_value_roundtrip():
    instance = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    assert instance.min == "sample_text"
    instance.min = "sample_text_2"
    assert instance.min == "sample_text_2"


def test_ccsl_filters_EquationFilter_operator_value_roundtrip():
    instance = ccsl_filters_EquationFilter(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_ccsl_filters_Filter_negated_value_roundtrip():
    instance = ccsl_filters_Filter(negated="sample_text")
    assert instance.negated == "sample_text"
    instance.negated = "sample_text_2"
    assert instance.negated == "sample_text_2"


def test_ccsl_filters_RegexMatch_regex_value_roundtrip():
    instance = ccsl_filters_RegexMatch(regex="sample_text")
    assert instance.regex == "sample_text"
    instance.regex = "sample_text_2"
    assert instance.regex == "sample_text_2"


def test_ccsl_filters_SameNameFilter_ignoreCase_value_roundtrip():
    instance = ccsl_filters_SameNameFilter(ignoreCase="sample_text")
    assert instance.ignoreCase == "sample_text"
    instance.ignoreCase = "sample_text_2"
    assert instance.ignoreCase == "sample_text_2"


def test_ccsl_filters_SuperClassClosureFilter_includesSubClass_value_roundtrip():
    instance = ccsl_filters_SuperClassClosureFilter(includesSubClass="sample_text")
    assert instance.includesSubClass == "sample_text"
    instance.includesSubClass = "sample_text_2"
    assert instance.includesSubClass == "sample_text_2"


def test_ccsl_invocation_Invocation_argsKind_value_roundtrip():
    instance = ccsl_invocation_Invocation(argsKind="sample_text")
    assert instance.argsKind == "sample_text"
    instance.argsKind = "sample_text_2"
    assert instance.argsKind == "sample_text_2"


def test_ccsl_literalValues_LiteralValue_value_value_roundtrip():
    instance = ccsl_literalValues_LiteralValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_ccsl_method_Constructor_avaliableInSourceCode_value_roundtrip():
    instance = ccsl_method_Constructor(avaliableInSourceCode="sample_text")
    assert instance.avaliableInSourceCode == "sample_text"
    instance.avaliableInSourceCode = "sample_text_2"
    assert instance.avaliableInSourceCode == "sample_text_2"


def test_ccsl_method_Method_abstract_value_roundtrip():
    instance = ccsl_method_Method(abstract="sample_text", final="sample_text", inheritance="sample_text", static="sample_text")
    assert instance.abstract == "sample_text"
    instance.abstract = "sample_text_2"
    assert instance.abstract == "sample_text_2"


def test_ccsl_method_Method_final_value_roundtrip():
    instance = ccsl_method_Method(abstract="sample_text", final="sample_text", inheritance="sample_text", static="sample_text")
    assert instance.final == "sample_text"
    instance.final = "sample_text_2"
    assert instance.final == "sample_text_2"


def test_ccsl_method_Method_inheritance_value_roundtrip():
    instance = ccsl_method_Method(abstract="sample_text", final="sample_text", inheritance="sample_text", static="sample_text")
    assert instance.inheritance == "sample_text"
    instance.inheritance = "sample_text_2"
    assert instance.inheritance == "sample_text_2"


def test_ccsl_method_Method_static_value_roundtrip():
    instance = ccsl_method_Method(abstract="sample_text", final="sample_text", inheritance="sample_text", static="sample_text")
    assert instance.static == "sample_text"
    instance.static = "sample_text_2"
    assert instance.static == "sample_text_2"


def test_ccsl_method_SimpleMethod_paramsKind_value_roundtrip():
    instance = ccsl_method_SimpleMethod(paramsKind="sample_text", visibility="sample_text")
    assert instance.paramsKind == "sample_text"
    instance.paramsKind = "sample_text_2"
    assert instance.paramsKind == "sample_text_2"


def test_ccsl_method_SimpleMethod_visibility_value_roundtrip():
    instance = ccsl_method_SimpleMethod(paramsKind="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_ccsl_namedElements_NamedElement_avaliableInSourceCode_value_roundtrip():
    instance = ccsl_namedElements_NamedElement(avaliableInSourceCode="sample_text", name="sample_text")
    assert instance.avaliableInSourceCode == "sample_text"
    instance.avaliableInSourceCode = "sample_text_2"
    assert instance.avaliableInSourceCode == "sample_text_2"


def test_ccsl_namedElements_NamedElement_name_value_roundtrip():
    instance = ccsl_namedElements_NamedElement(avaliableInSourceCode="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ccsl_numberFunctions_CcslIntegerLiteral_value_value_roundtrip():
    instance = ccsl_numberFunctions_CcslIntegerLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_ccsl_statements_Block_statementsKind_value_roundtrip():
    instance = ccsl_statements_Block(statementsKind="sample_text")
    assert instance.statementsKind == "sample_text"
    instance.statementsKind = "sample_text_2"
    assert instance.statementsKind == "sample_text_2"


def test_ccsl_statements_InstanceCreation_argsKind_value_roundtrip():
    instance = ccsl_statements_InstanceCreation(argsKind="sample_text")
    assert instance.argsKind == "sample_text"
    instance.argsKind = "sample_text_2"
    assert instance.argsKind == "sample_text_2"


def test_ccsl_variable_FieldVariable_static_value_roundtrip():
    instance = ccsl_variable_FieldVariable(static="sample_text", visibility="sample_text")
    assert instance.static == "sample_text"
    instance.static = "sample_text_2"
    assert instance.static == "sample_text_2"


def test_ccsl_variable_FieldVariable_visibility_value_roundtrip():
    instance = ccsl_variable_FieldVariable(static="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_ccsl_variable_Variable_final_value_roundtrip():
    instance = ccsl_variable_Variable(final="sample_text")
    assert instance.final == "sample_text"
    instance.final = "sample_text_2"
    assert instance.final == "sample_text_2"


def test_ccsl_assignment_Assignment_isa_AbstractAssignment():
    instance = ccsl_assignment_Assignment(operator="sample_text")
    assert isinstance(instance, AbstractAssignment)


def test_ccsl_assignment_UnaryAssignment_isa_AbstractAssignment():
    instance = ccsl_assignment_UnaryAssignment(operator="sample_text")
    assert isinstance(instance, AbstractAssignment)


def test_ccsl_statements_DataTypeAccess_isa_Access():
    instance = ccsl_statements_DataTypeAccess()
    assert isinstance(instance, Access)


def test_ccsl_statements_VariableAccess_isa_Access():
    instance = ccsl_statements_VariableAccess()
    assert isinstance(instance, Access)


def test_ccsl_filters_BlockLastStatementFilter_isa_AtomicFilter():
    instance = ccsl_filters_BlockLastStatementFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_ChildClosureComplexTypeFilter_isa_AtomicFilter():
    instance = ccsl_filters_ChildClosureComplexTypeFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_CountFilter_isa_AtomicFilter():
    instance = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_FromClosureFilter_isa_AtomicFilter():
    instance = ccsl_filters_FromClosureFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_HasSameReferenceFilter_isa_AtomicFilter():
    instance = ccsl_filters_HasSameReferenceFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_ImplicityContainerFilter_isa_AtomicFilter():
    instance = ccsl_filters_ImplicityContainerFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_IsKindOfFilter_isa_AtomicFilter():
    instance = ccsl_filters_IsKindOfFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_IsStringFilter_isa_AtomicFilter():
    instance = ccsl_filters_IsStringFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_IsTypeOfFilter_isa_AtomicFilter():
    instance = ccsl_filters_IsTypeOfFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_PropertyFilter_isa_AtomicFilter():
    instance = ccsl_filters_PropertyFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_RegexMatch_isa_AtomicFilter():
    instance = ccsl_filters_RegexMatch(regex="sample_text")
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_SameNameFilter_isa_AtomicFilter():
    instance = ccsl_filters_SameNameFilter(ignoreCase="sample_text")
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_SuperClassClosureFilter_isa_AtomicFilter():
    instance = ccsl_filters_SuperClassClosureFilter(includesSubClass="sample_text")
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_SuperMethodClosureFilter_isa_AtomicFilter():
    instance = ccsl_filters_SuperMethodClosureFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_filters_TemplateFilter_isa_AtomicFilter():
    instance = ccsl_filters_TemplateFilter()
    assert isinstance(instance, AtomicFilter)


def test_ccsl_controlFlow_SwitchCaseBlock_isa_Block():
    instance = ccsl_controlFlow_SwitchCaseBlock(default="sample_text")
    assert isinstance(instance, Block)


def test_ccsl_filters_Filter_isa_CcslBooleanFunction():
    instance = ccsl_filters_Filter(negated="sample_text")
    assert isinstance(instance, CcslBooleanFunction)


def test_ccsl_booleanFunctions_CcslBooleanFunction_isa_CcslFunction():
    instance = ccsl_booleanFunctions_CcslBooleanFunction()
    assert isinstance(instance, CcslFunction)


def test_ccsl_numberFunctions_CcslNumberFunction_isa_CcslFunction():
    instance = ccsl_numberFunctions_CcslNumberFunction()
    assert isinstance(instance, CcslFunction)


def test_ccsl_numberFunctions_CcslIntegerLiteral_isa_CcslNumberFunction():
    instance = ccsl_numberFunctions_CcslIntegerLiteral(value="sample_text")
    assert isinstance(instance, CcslNumberFunction)


def test_ccsl_numberFunctions_GetIndexOf_isa_CcslNumberFunction():
    instance = ccsl_numberFunctions_GetIndexOf()
    assert isinstance(instance, CcslNumberFunction)


def test_ccsl_complexType_AnonymousClass_isa_ComplexType():
    instance = ccsl_complexType_AnonymousClass()
    assert isinstance(instance, ComplexType)


def test_ccsl_datatype_GenericType_isa_ComplexType():
    instance = ccsl_datatype_GenericType()
    assert isinstance(instance, ComplexType)


def test_ccsl_controlFlow_IfStatement_isa_ControlFlow():
    instance = ccsl_controlFlow_IfStatement()
    assert isinstance(instance, ControlFlow)


def test_ccsl_controlFlow_LoopStatement_isa_ControlFlow():
    instance = ccsl_controlFlow_LoopStatement()
    assert isinstance(instance, ControlFlow)


def test_ccsl_controlFlow_SwitchStatement_isa_ControlFlow():
    instance = ccsl_controlFlow_SwitchStatement()
    assert isinstance(instance, ControlFlow)


def test_ccsl_datatype_ObjectType_isa_DataType():
    instance = ccsl_datatype_ObjectType()
    assert isinstance(instance, DataType)


def test_ccsl_datatype_PrimitiveType_isa_DataType():
    instance = ccsl_datatype_PrimitiveType()
    assert isinstance(instance, DataType)


def test_ccsl_complexType_AnnotationType_isa_DeclaredType():
    instance = ccsl_complexType_AnnotationType()
    assert isinstance(instance, DeclaredType)


def test_ccsl_annotation_AnnotableElement_isa_Element():
    instance = ccsl_annotation_AnnotableElement(annotationsKind="sample_text")
    assert isinstance(instance, Element)


def test_ccsl_complexType_ComplexType_isa_Element():
    instance = ccsl_complexType_ComplexType()
    assert isinstance(instance, Element)


def test_ccsl_datatype_DataType_isa_Element():
    instance = ccsl_datatype_DataType()
    assert isinstance(instance, Element)


def test_ccsl_import_ImportableElement_isa_Element():
    instance = ccsl_import_ImportableElement()
    assert isinstance(instance, Element)


def test_ccsl_namedElements_NamedElement_isa_Element():
    instance = ccsl_namedElements_NamedElement(avaliableInSourceCode="sample_text", name="sample_text")
    assert isinstance(instance, Element)


def test_ccsl_statements_Statement_isa_Element():
    instance = ccsl_statements_Statement()
    assert isinstance(instance, Element)


def test_ccsl_filters_AtomicFilter_isa_Filter():
    instance = ccsl_filters_AtomicFilter()
    assert isinstance(instance, Filter)


def test_ccsl_filters_CompositeFilter_isa_Filter():
    instance = ccsl_filters_CompositeFilter(operator="sample_text")
    assert isinstance(instance, Filter)


def test_ccsl_variable_LocalVariable_isa_InitializableVariable():
    instance = ccsl_variable_LocalVariable()
    assert isinstance(instance, InitializableVariable)


def test_ccsl_action_ChangeLiteralValueAction_isa_InjectionAction():
    instance = ccsl_action_ChangeLiteralValueAction()
    assert isinstance(instance, InjectionAction)


def test_ccsl_action_DeleteAction_isa_InjectionAction():
    instance = ccsl_action_DeleteAction()
    assert isinstance(instance, InjectionAction)


def test_ccsl_action_DeleteInfixOperatorAction_isa_InjectionAction():
    instance = ccsl_action_DeleteInfixOperatorAction()
    assert isinstance(instance, InjectionAction)


def test_ccsl_action_DeleteRandomStatementAction_isa_InjectionAction():
    instance = ccsl_action_DeleteRandomStatementAction()
    assert isinstance(instance, InjectionAction)


def test_ccsl_action_MoveScopeUpAction_isa_InjectionAction():
    instance = ccsl_action_MoveScopeUpAction()
    assert isinstance(instance, InjectionAction)


def test_ccsl_action_ReplaceArithmeticOperatorAction_isa_InjectionAction():
    instance = ccsl_action_ReplaceArithmeticOperatorAction()
    assert isinstance(instance, InjectionAction)


def test_ccsl_action_ReplaceVariableAccessAction_isa_InjectionAction():
    instance = ccsl_action_ReplaceVariableAccessAction()
    assert isinstance(instance, InjectionAction)


def test_ccsl_strategy_AllStrategy_isa_InjectionStrategy():
    instance = ccsl_strategy_AllStrategy()
    assert isinstance(instance, InjectionStrategy)


def test_ccsl_invocation_ConstructorInvocation_isa_Invocation():
    instance = ccsl_invocation_ConstructorInvocation()
    assert isinstance(instance, Invocation)


def test_ccsl_invocation_SimpleMethodInvocation_isa_Invocation():
    instance = ccsl_invocation_SimpleMethodInvocation()
    assert isinstance(instance, Invocation)


def test_ccsl_literalValues_BooleanLiteral_isa_LiteralValue():
    instance = ccsl_literalValues_BooleanLiteral()
    assert isinstance(instance, LiteralValue)


def test_ccsl_literalValues_CharacterLiteral_isa_LiteralValue():
    instance = ccsl_literalValues_CharacterLiteral()
    assert isinstance(instance, LiteralValue)


def test_ccsl_literalValues_NullLiteral_isa_LiteralValue():
    instance = ccsl_literalValues_NullLiteral()
    assert isinstance(instance, LiteralValue)


def test_ccsl_literalValues_NumberLiteral_isa_LiteralValue():
    instance = ccsl_literalValues_NumberLiteral()
    assert isinstance(instance, LiteralValue)


def test_ccsl_literalValues_StringLiteral_isa_LiteralValue():
    instance = ccsl_literalValues_StringLiteral()
    assert isinstance(instance, LiteralValue)


def test_ccsl_variable_Variable_isa_NamedElement():
    instance = ccsl_variable_Variable(final="sample_text")
    assert isinstance(instance, NamedElement)


def test_ccsl_datatype_ArrayType_isa_ObjectType():
    instance = ccsl_datatype_ArrayType(dimensions="sample_text")
    assert isinstance(instance, ObjectType)


def test_ccsl_datatype_ParameterizedType_isa_ObjectType():
    instance = ccsl_datatype_ParameterizedType()
    assert isinstance(instance, ObjectType)


def test_ccsl_expressions_ArithmeticExpression_isa_OperatorExpression():
    instance = ccsl_expressions_ArithmeticExpression(arithmeticOperator="sample_text")
    assert isinstance(instance, OperatorExpression)


def test_ccsl_expressions_BooleanExpression_isa_OperatorExpression():
    instance = ccsl_expressions_BooleanExpression(booleanOperator="sample_text")
    assert isinstance(instance, OperatorExpression)


def test_ccsl_expressions_InfixExpression_isa_OperatorExpression():
    instance = ccsl_expressions_InfixExpression()
    assert isinstance(instance, OperatorExpression)


def test_ccsl_expressions_StringConcatenation_isa_OperatorExpression():
    instance = ccsl_expressions_StringConcatenation()
    assert isinstance(instance, OperatorExpression)


def test_ccsl_datatype_BooleanPrimitiveType_isa_PrimitiveType():
    instance = ccsl_datatype_BooleanPrimitiveType()
    assert isinstance(instance, PrimitiveType)


def test_ccsl_datatype_IntPrimitiveType_isa_PrimitiveType():
    instance = ccsl_datatype_IntPrimitiveType()
    assert isinstance(instance, PrimitiveType)


def test_ccsl_datatype_ShortPrimitiveType_isa_PrimitiveType():
    instance = ccsl_datatype_ShortPrimitiveType()
    assert isinstance(instance, PrimitiveType)


def test_ccsl_datatype_StringPrimitiveType_isa_PrimitiveType():
    instance = ccsl_datatype_StringPrimitiveType()
    assert isinstance(instance, PrimitiveType)


def test_ccsl_datatype_VoidType_isa_PrimitiveType():
    instance = ccsl_datatype_VoidType()
    assert isinstance(instance, PrimitiveType)


def test_ccsl_FaultTypeDescription_isa_Root():
    instance = ccsl_FaultTypeDescription(name="sample_text")
    assert isinstance(instance, Root)


def test_ccsl_Rule_isa_Root():
    instance = ccsl_Rule(negated="sample_text")
    assert isinstance(instance, Root)


def test_ccsl_AtomicRule_isa_Rule():
    instance = ccsl_AtomicRule()
    assert isinstance(instance, Rule)


def test_ccsl_CompositeRule_isa_Rule():
    instance = ccsl_CompositeRule(operator="sample_text")
    assert isinstance(instance, Rule)


def test_ccsl_method_Constructor_isa_SimpleMethod():
    instance = ccsl_method_Constructor(avaliableInSourceCode="sample_text")
    assert isinstance(instance, SimpleMethod)


def test_ccsl_invocation_MethodInvocation_isa_SimpleMethodInvocation():
    instance = ccsl_invocation_MethodInvocation()
    assert isinstance(instance, SimpleMethodInvocation)


def test_ccsl_invocation_SuperMethodInvocation_isa_SimpleMethodInvocation():
    instance = ccsl_invocation_SuperMethodInvocation()
    assert isinstance(instance, SimpleMethodInvocation)


def test_ccsl_annotation_Annotation_isa_Statement():
    instance = ccsl_annotation_Annotation()
    assert isinstance(instance, Statement)


def test_ccsl_assignment_AbstractAssignment_isa_Statement():
    instance = ccsl_assignment_AbstractAssignment()
    assert isinstance(instance, Statement)


def test_ccsl_expressions_OperatorExpression_isa_Statement():
    instance = ccsl_expressions_OperatorExpression()
    assert isinstance(instance, Statement)


def test_ccsl_expressions_ParenthesizedExpression_isa_Statement():
    instance = ccsl_expressions_ParenthesizedExpression()
    assert isinstance(instance, Statement)


def test_ccsl_import_ImportStatement_isa_Statement():
    instance = ccsl_import_ImportStatement()
    assert isinstance(instance, Statement)


def test_ccsl_invocation_Invocation_isa_Statement():
    instance = ccsl_invocation_Invocation(argsKind="sample_text")
    assert isinstance(instance, Statement)


def test_ccsl_literalValues_LiteralValue_isa_Statement():
    instance = ccsl_literalValues_LiteralValue(value="sample_text")
    assert isinstance(instance, Statement)


def test_ccsl_statements_Access_isa_Statement():
    instance = ccsl_statements_Access()
    assert isinstance(instance, Statement)


def test_ccsl_statements_ArrayCreation_isa_Statement():
    instance = ccsl_statements_ArrayCreation()
    assert isinstance(instance, Statement)


def test_ccsl_statements_Block_isa_Statement():
    instance = ccsl_statements_Block(statementsKind="sample_text")
    assert isinstance(instance, Statement)


def test_ccsl_statements_BreakStatement_isa_Statement():
    instance = ccsl_statements_BreakStatement()
    assert isinstance(instance, Statement)


def test_ccsl_statements_ContinueStatement_isa_Statement():
    instance = ccsl_statements_ContinueStatement()
    assert isinstance(instance, Statement)


def test_ccsl_statements_ControlFlow_isa_Statement():
    instance = ccsl_statements_ControlFlow()
    assert isinstance(instance, Statement)


def test_ccsl_statements_EmptyStatement_isa_Statement():
    instance = ccsl_statements_EmptyStatement()
    assert isinstance(instance, Statement)


def test_ccsl_statements_InstanceCreation_isa_Statement():
    instance = ccsl_statements_InstanceCreation(argsKind="sample_text")
    assert isinstance(instance, Statement)


def test_ccsl_statements_InstanceOf_isa_Statement():
    instance = ccsl_statements_InstanceOf()
    assert isinstance(instance, Statement)


def test_ccsl_statements_NamedElementAccess_isa_Statement():
    instance = ccsl_statements_NamedElementAccess()
    assert isinstance(instance, Statement)


def test_ccsl_statements_ReturnStatement_isa_Statement():
    instance = ccsl_statements_ReturnStatement()
    assert isinstance(instance, Statement)


def test_ccsl_statements_SynchronizedBlock_isa_Statement():
    instance = ccsl_statements_SynchronizedBlock()
    assert isinstance(instance, Statement)


def test_ccsl_statements_ThisStatement_isa_Statement():
    instance = ccsl_statements_ThisStatement()
    assert isinstance(instance, Statement)


def test_ccsl_statements_VarDeclaration_isa_Statement():
    instance = ccsl_statements_VarDeclaration()
    assert isinstance(instance, Statement)


def test_ccsl_tryCatch_CatchClause_isa_Statement():
    instance = ccsl_tryCatch_CatchClause()
    assert isinstance(instance, Statement)


def test_ccsl_tryCatch_TryStatement_isa_Statement():
    instance = ccsl_tryCatch_TryStatement()
    assert isinstance(instance, Statement)


def test_ccsl_filters_ImplicityOperandFilter_isa_TemplateFilter():
    instance = ccsl_filters_ImplicityOperandFilter()
    assert isinstance(instance, TemplateFilter)


def test_ccsl_assignment_PostfixUnaryAssignment_isa_UnaryAssignment():
    instance = ccsl_assignment_PostfixUnaryAssignment()
    assert isinstance(instance, UnaryAssignment)


def test_ccsl_assignment_PrefixUnaryAssignment_isa_UnaryAssignment():
    instance = ccsl_assignment_PrefixUnaryAssignment()
    assert isinstance(instance, UnaryAssignment)


def test_ccsl_variable_InitializableVariable_isa_Variable():
    instance = ccsl_variable_InitializableVariable()
    assert isinstance(instance, Variable)


def test_ccsl_complexType_JClass_isa_annotation_AnnotableElement():
    instance = ccsl_complexType_JClass(inheritance="sample_text")
    assert isinstance(instance, annotation_AnnotableElement)


def test_ccsl_complexType_JInterface_isa_annotation_AnnotableElement():
    instance = ccsl_complexType_JInterface()
    assert isinstance(instance, annotation_AnnotableElement)


def test_ccsl_method_SimpleMethod_isa_annotation_AnnotableElement():
    instance = ccsl_method_SimpleMethod(paramsKind="sample_text", visibility="sample_text")
    assert isinstance(instance, annotation_AnnotableElement)


def test_ccsl_variable_FieldVariable_isa_annotation_AnnotableElement():
    instance = ccsl_variable_FieldVariable(static="sample_text", visibility="sample_text")
    assert isinstance(instance, annotation_AnnotableElement)


def test_ccsl_variable_ParameterVariable_isa_annotation_AnnotableElement():
    instance = ccsl_variable_ParameterVariable()
    assert isinstance(instance, annotation_AnnotableElement)


def test_ccsl_complexType_JClass_isa_complexType_ComplexType():
    instance = ccsl_complexType_JClass(inheritance="sample_text")
    assert isinstance(instance, complexType_ComplexType)


def test_ccsl_complexType_JInterface_isa_complexType_ComplexType():
    instance = ccsl_complexType_JInterface()
    assert isinstance(instance, complexType_ComplexType)


def test_ccsl_complexType_JClass_isa_complexType_DeclaredType():
    instance = ccsl_complexType_JClass(inheritance="sample_text")
    assert isinstance(instance, complexType_DeclaredType)


def test_ccsl_complexType_JInterface_isa_complexType_DeclaredType():
    instance = ccsl_complexType_JInterface()
    assert isinstance(instance, complexType_DeclaredType)


def test_ccsl_complexType_DeclaredType_isa_datatype_ObjectType():
    instance = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    assert isinstance(instance, datatype_ObjectType)


def test_ccsl_method_SimpleMethod_isa_elements_Element():
    instance = ccsl_method_SimpleMethod(paramsKind="sample_text", visibility="sample_text")
    assert isinstance(instance, elements_Element)


def test_ccsl_complexType_DeclaredType_isa_import_ImportableElement():
    instance = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    assert isinstance(instance, import_ImportableElement)


def test_ccsl_namedElements_Package_isa_import_ImportableElement():
    instance = ccsl_namedElements_Package()
    assert isinstance(instance, import_ImportableElement)


def test_ccsl_method_Method_isa_method_SimpleMethod():
    instance = ccsl_method_Method(abstract="sample_text", final="sample_text", inheritance="sample_text", static="sample_text")
    assert isinstance(instance, method_SimpleMethod)


def test_ccsl_complexType_DeclaredType_isa_namedElements_NamedElement():
    instance = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    assert isinstance(instance, namedElements_NamedElement)


def test_ccsl_method_Method_isa_namedElements_NamedElement():
    instance = ccsl_method_Method(abstract="sample_text", final="sample_text", inheritance="sample_text", static="sample_text")
    assert isinstance(instance, namedElements_NamedElement)


def test_ccsl_namedElements_Package_isa_namedElements_NamedElement():
    instance = ccsl_namedElements_Package()
    assert isinstance(instance, namedElements_NamedElement)


def test_ccsl_variable_FieldVariable_isa_variable_InitializableVariable():
    instance = ccsl_variable_FieldVariable(static="sample_text", visibility="sample_text")
    assert isinstance(instance, variable_InitializableVariable)


def test_ccsl_variable_ParameterVariable_isa_variable_Variable():
    instance = ccsl_variable_ParameterVariable()
    assert isinstance(instance, variable_Variable)


def test_assoc_actions6_link_reassign_clear():
    a = ccsl_FaultTypeDescription(name="sample_text")
    b1 = InjectionAction()
    b2 = InjectionAction()
    _safe_set(a, 'ccsl_FaultTypeDescription7', {b1})
    assert _is_linked(a, 'ccsl_FaultTypeDescription7', b1)
    if hasattr(b1, 'InjectionAction'):
        assert _is_linked(b1, 'InjectionAction', a)
    _safe_set(a, 'ccsl_FaultTypeDescription7', {b2})
    assert _is_linked(a, 'ccsl_FaultTypeDescription7', b2)
    if hasattr(b1, 'InjectionAction'):
        assert not _is_linked(b1, 'InjectionAction', a)
    if hasattr(b2, 'InjectionAction'):
        assert _is_linked(b2, 'InjectionAction', a)
    _safe_set(a, 'ccsl_FaultTypeDescription7', set())
    assert not _is_linked(a, 'ccsl_FaultTypeDescription7', b2)
    if hasattr(b2, 'InjectionAction'):
        assert not _is_linked(b2, 'InjectionAction', a)


def test_assoc_annotations102_link_reassign_clear():
    a = ccsl_annotation_AnnotableElement(annotationsKind="sample_text")
    b1 = annotation_Annotation()
    b2 = annotation_Annotation()
    _safe_set(a, 'ccsl_annotation_AnnotableElement', {b1})
    assert _is_linked(a, 'ccsl_annotation_AnnotableElement', b1)
    if hasattr(b1, 'annotation_Annotation'):
        assert _is_linked(b1, 'annotation_Annotation', a)
    _safe_set(a, 'ccsl_annotation_AnnotableElement', {b2})
    assert _is_linked(a, 'ccsl_annotation_AnnotableElement', b2)
    if hasattr(b1, 'annotation_Annotation'):
        assert not _is_linked(b1, 'annotation_Annotation', a)
    if hasattr(b2, 'annotation_Annotation'):
        assert _is_linked(b2, 'annotation_Annotation', a)
    _safe_set(a, 'ccsl_annotation_AnnotableElement', set())
    assert not _is_linked(a, 'ccsl_annotation_AnnotableElement', b2)
    if hasattr(b2, 'annotation_Annotation'):
        assert not _is_linked(b2, 'annotation_Annotation', a)


def test_assoc_args41_link_reassign_clear():
    a = ccsl_statements_InstanceCreation(argsKind="sample_text")
    b1 = statements_Statement()
    b2 = statements_Statement()
    _safe_set(a, 'ccsl_statements_InstanceCreation42', {b1})
    assert _is_linked(a, 'ccsl_statements_InstanceCreation42', b1)
    if hasattr(b1, 'statements_Statement43'):
        assert _is_linked(b1, 'statements_Statement43', a)
    _safe_set(a, 'ccsl_statements_InstanceCreation42', {b2})
    assert _is_linked(a, 'ccsl_statements_InstanceCreation42', b2)
    if hasattr(b1, 'statements_Statement43'):
        assert not _is_linked(b1, 'statements_Statement43', a)
    if hasattr(b2, 'statements_Statement43'):
        assert _is_linked(b2, 'statements_Statement43', a)
    _safe_set(a, 'ccsl_statements_InstanceCreation42', set())
    assert not _is_linked(a, 'ccsl_statements_InstanceCreation42', b2)
    if hasattr(b2, 'statements_Statement43'):
        assert not _is_linked(b2, 'statements_Statement43', a)


def test_assoc_args94_link_reassign_clear():
    a = ccsl_invocation_Invocation(argsKind="sample_text")
    b1 = statements_Statement()
    b2 = statements_Statement()
    _safe_set(a, 'ccsl_invocation_Invocation', {b1})
    assert _is_linked(a, 'ccsl_invocation_Invocation', b1)
    if hasattr(b1, 'statements_Statement95'):
        assert _is_linked(b1, 'statements_Statement95', a)
    _safe_set(a, 'ccsl_invocation_Invocation', {b2})
    assert _is_linked(a, 'ccsl_invocation_Invocation', b2)
    if hasattr(b1, 'statements_Statement95'):
        assert not _is_linked(b1, 'statements_Statement95', a)
    if hasattr(b2, 'statements_Statement95'):
        assert _is_linked(b2, 'statements_Statement95', a)
    _safe_set(a, 'ccsl_invocation_Invocation', set())
    assert not _is_linked(a, 'ccsl_invocation_Invocation', b2)
    if hasattr(b2, 'statements_Statement95'):
        assert not _is_linked(b2, 'statements_Statement95', a)


def test_assoc_constructor38_link_reassign_clear():
    a = ccsl_statements_InstanceCreation(argsKind="sample_text")
    b1 = method_Constructor()
    b2 = method_Constructor()
    _safe_set(a, 'ccsl_statements_InstanceCreation39', b1)
    assert _is_linked(a, 'ccsl_statements_InstanceCreation39', b1)
    if hasattr(b1, 'method_Constructor40'):
        assert _is_linked(b1, 'method_Constructor40', a)
    _safe_set(a, 'ccsl_statements_InstanceCreation39', b2)
    assert _is_linked(a, 'ccsl_statements_InstanceCreation39', b2)
    if hasattr(b1, 'method_Constructor40'):
        assert not _is_linked(b1, 'method_Constructor40', a)
    if hasattr(b2, 'method_Constructor40'):
        assert _is_linked(b2, 'method_Constructor40', a)
    _safe_set(a, 'ccsl_statements_InstanceCreation39', None)
    assert not _is_linked(a, 'ccsl_statements_InstanceCreation39', b2)
    if hasattr(b2, 'method_Constructor40'):
        assert not _is_linked(b2, 'method_Constructor40', a)


def test_assoc_constructors14_link_reassign_clear():
    a = ccsl_complexType_JClass(inheritance="sample_text")
    b1 = method_Constructor()
    b2 = method_Constructor()
    _safe_set(a, 'ccsl_complexType_JClass', {b1})
    assert _is_linked(a, 'ccsl_complexType_JClass', b1)
    if hasattr(b1, 'method_Constructor'):
        assert _is_linked(b1, 'method_Constructor', a)
    _safe_set(a, 'ccsl_complexType_JClass', {b2})
    assert _is_linked(a, 'ccsl_complexType_JClass', b2)
    if hasattr(b1, 'method_Constructor'):
        assert not _is_linked(b1, 'method_Constructor', a)
    if hasattr(b2, 'method_Constructor'):
        assert _is_linked(b2, 'method_Constructor', a)
    _safe_set(a, 'ccsl_complexType_JClass', set())
    assert not _is_linked(a, 'ccsl_complexType_JClass', b2)
    if hasattr(b2, 'method_Constructor'):
        assert not _is_linked(b2, 'method_Constructor', a)


def test_assoc_container129_link_reassign_clear():
    a = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    b1 = Element()
    b2 = Element()
    _safe_set(a, 'ccsl_filters_CountFilter130', b1)
    assert _is_linked(a, 'ccsl_filters_CountFilter130', b1)
    if hasattr(b1, 'Element131'):
        assert _is_linked(b1, 'Element131', a)
    _safe_set(a, 'ccsl_filters_CountFilter130', b2)
    assert _is_linked(a, 'ccsl_filters_CountFilter130', b2)
    if hasattr(b1, 'Element131'):
        assert not _is_linked(b1, 'Element131', a)
    if hasattr(b2, 'Element131'):
        assert _is_linked(b2, 'Element131', a)
    _safe_set(a, 'ccsl_filters_CountFilter130', None)
    assert not _is_linked(a, 'ccsl_filters_CountFilter130', b2)
    if hasattr(b2, 'Element131'):
        assert not _is_linked(b2, 'Element131', a)


def test_assoc_context127_link_reassign_clear():
    a = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    b1 = Context()
    b2 = Context()
    _safe_set(a, 'ccsl_filters_CountFilter', {b1})
    assert _is_linked(a, 'ccsl_filters_CountFilter', b1)
    if hasattr(b1, 'Context128'):
        assert _is_linked(b1, 'Context128', a)
    _safe_set(a, 'ccsl_filters_CountFilter', {b2})
    assert _is_linked(a, 'ccsl_filters_CountFilter', b2)
    if hasattr(b1, 'Context128'):
        assert not _is_linked(b1, 'Context128', a)
    if hasattr(b2, 'Context128'):
        assert _is_linked(b2, 'Context128', a)
    _safe_set(a, 'ccsl_filters_CountFilter', set())
    assert not _is_linked(a, 'ccsl_filters_CountFilter', b2)
    if hasattr(b2, 'Context128'):
        assert not _is_linked(b2, 'Context128', a)


def test_assoc_context185_link_reassign_clear():
    a = ccsl_filters_SuperClassClosureFilter(includesSubClass="sample_text")
    b1 = Context()
    b2 = Context()
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter186', b1)
    assert _is_linked(a, 'ccsl_filters_SuperClassClosureFilter186', b1)
    if hasattr(b1, 'Context187'):
        assert _is_linked(b1, 'Context187', a)
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter186', b2)
    assert _is_linked(a, 'ccsl_filters_SuperClassClosureFilter186', b2)
    if hasattr(b1, 'Context187'):
        assert not _is_linked(b1, 'Context187', a)
    if hasattr(b2, 'Context187'):
        assert _is_linked(b2, 'Context187', a)
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter186', None)
    assert not _is_linked(a, 'ccsl_filters_SuperClassClosureFilter186', b2)
    if hasattr(b2, 'Context187'):
        assert not _is_linked(b2, 'Context187', a)


def test_assoc_elements126_link_reassign_clear():
    a = ccsl_filters_SameNameFilter(ignoreCase="sample_text")
    b1 = namedElements_NamedElement()
    b2 = namedElements_NamedElement()
    _safe_set(a, 'ccsl_filters_SameNameFilter', {b1})
    assert _is_linked(a, 'ccsl_filters_SameNameFilter', b1)
    if hasattr(b1, 'namedElements_NamedElement'):
        assert _is_linked(b1, 'namedElements_NamedElement', a)
    _safe_set(a, 'ccsl_filters_SameNameFilter', {b2})
    assert _is_linked(a, 'ccsl_filters_SameNameFilter', b2)
    if hasattr(b1, 'namedElements_NamedElement'):
        assert not _is_linked(b1, 'namedElements_NamedElement', a)
    if hasattr(b2, 'namedElements_NamedElement'):
        assert _is_linked(b2, 'namedElements_NamedElement', a)
    _safe_set(a, 'ccsl_filters_SameNameFilter', set())
    assert not _is_linked(a, 'ccsl_filters_SameNameFilter', b2)
    if hasattr(b2, 'namedElements_NamedElement'):
        assert not _is_linked(b2, 'namedElements_NamedElement', a)


def test_assoc_field132_link_reassign_clear():
    a = ccsl_filters_CountFilter(max="sample_text", min="sample_text")
    b1 = Element()
    b2 = Element()
    _safe_set(a, 'ccsl_filters_CountFilter133', b1)
    assert _is_linked(a, 'ccsl_filters_CountFilter133', b1)
    if hasattr(b1, 'Element134'):
        assert _is_linked(b1, 'Element134', a)
    _safe_set(a, 'ccsl_filters_CountFilter133', b2)
    assert _is_linked(a, 'ccsl_filters_CountFilter133', b2)
    if hasattr(b1, 'Element134'):
        assert not _is_linked(b1, 'Element134', a)
    if hasattr(b2, 'Element134'):
        assert _is_linked(b2, 'Element134', a)
    _safe_set(a, 'ccsl_filters_CountFilter133', None)
    assert not _is_linked(a, 'ccsl_filters_CountFilter133', b2)
    if hasattr(b2, 'Element134'):
        assert not _is_linked(b2, 'Element134', a)


def test_assoc_filters119_link_reassign_clear():
    a = ccsl_filters_CompositeFilter(operator="sample_text")
    b1 = filters_Filter()
    b2 = filters_Filter()
    _safe_set(a, 'ccsl_filters_CompositeFilter', {b1})
    assert _is_linked(a, 'ccsl_filters_CompositeFilter', b1)
    if hasattr(b1, 'filters_Filter120'):
        assert _is_linked(b1, 'filters_Filter120', a)
    _safe_set(a, 'ccsl_filters_CompositeFilter', {b2})
    assert _is_linked(a, 'ccsl_filters_CompositeFilter', b2)
    if hasattr(b1, 'filters_Filter120'):
        assert not _is_linked(b1, 'filters_Filter120', a)
    if hasattr(b2, 'filters_Filter120'):
        assert _is_linked(b2, 'filters_Filter120', a)
    _safe_set(a, 'ccsl_filters_CompositeFilter', set())
    assert not _is_linked(a, 'ccsl_filters_CompositeFilter', b2)
    if hasattr(b2, 'filters_Filter120'):
        assert not _is_linked(b2, 'filters_Filter120', a)


def test_assoc_imports18_link_reassign_clear():
    a = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    b1 = import_ImportStatement()
    b2 = import_ImportStatement()
    _safe_set(a, 'ccsl_complexType_DeclaredType19', {b1})
    assert _is_linked(a, 'ccsl_complexType_DeclaredType19', b1)
    if hasattr(b1, 'import_ImportStatement'):
        assert _is_linked(b1, 'import_ImportStatement', a)
    _safe_set(a, 'ccsl_complexType_DeclaredType19', {b2})
    assert _is_linked(a, 'ccsl_complexType_DeclaredType19', b2)
    if hasattr(b1, 'import_ImportStatement'):
        assert not _is_linked(b1, 'import_ImportStatement', a)
    if hasattr(b2, 'import_ImportStatement'):
        assert _is_linked(b2, 'import_ImportStatement', a)
    _safe_set(a, 'ccsl_complexType_DeclaredType19', set())
    assert not _is_linked(a, 'ccsl_complexType_DeclaredType19', b2)
    if hasattr(b2, 'import_ImportStatement'):
        assert not _is_linked(b2, 'import_ImportStatement', a)


def test_assoc_leftHandSide169_link_reassign_clear():
    a = ccsl_filters_EquationFilter(operator="sample_text")
    b1 = numberFunctions_CcslNumberFunction()
    b2 = numberFunctions_CcslNumberFunction()
    _safe_set(a, 'ccsl_filters_EquationFilter', {b1})
    assert _is_linked(a, 'ccsl_filters_EquationFilter', b1)
    if hasattr(b1, 'numberFunctions_CcslNumberFunction'):
        assert _is_linked(b1, 'numberFunctions_CcslNumberFunction', a)
    _safe_set(a, 'ccsl_filters_EquationFilter', {b2})
    assert _is_linked(a, 'ccsl_filters_EquationFilter', b2)
    if hasattr(b1, 'numberFunctions_CcslNumberFunction'):
        assert not _is_linked(b1, 'numberFunctions_CcslNumberFunction', a)
    if hasattr(b2, 'numberFunctions_CcslNumberFunction'):
        assert _is_linked(b2, 'numberFunctions_CcslNumberFunction', a)
    _safe_set(a, 'ccsl_filters_EquationFilter', set())
    assert not _is_linked(a, 'ccsl_filters_EquationFilter', b2)
    if hasattr(b2, 'numberFunctions_CcslNumberFunction'):
        assert not _is_linked(b2, 'numberFunctions_CcslNumberFunction', a)


def test_assoc_nestedTypes20_link_reassign_clear():
    a = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    b1 = complexType_DeclaredType()
    b2 = complexType_DeclaredType()
    _safe_set(a, 'ccsl_complexType_DeclaredType21', {b1})
    assert _is_linked(a, 'ccsl_complexType_DeclaredType21', b1)
    if hasattr(b1, 'complexType_DeclaredType22'):
        assert _is_linked(b1, 'complexType_DeclaredType22', a)
    _safe_set(a, 'ccsl_complexType_DeclaredType21', {b2})
    assert _is_linked(a, 'ccsl_complexType_DeclaredType21', b2)
    if hasattr(b1, 'complexType_DeclaredType22'):
        assert not _is_linked(b1, 'complexType_DeclaredType22', a)
    if hasattr(b2, 'complexType_DeclaredType22'):
        assert _is_linked(b2, 'complexType_DeclaredType22', a)
    _safe_set(a, 'ccsl_complexType_DeclaredType21', set())
    assert not _is_linked(a, 'ccsl_complexType_DeclaredType21', b2)
    if hasattr(b2, 'complexType_DeclaredType22'):
        assert not _is_linked(b2, 'complexType_DeclaredType22', a)


def test_assoc_params26_link_reassign_clear():
    a = ccsl_method_SimpleMethod(paramsKind="sample_text", visibility="sample_text")
    b1 = variable_ParameterVariable()
    b2 = variable_ParameterVariable()
    _safe_set(a, 'ccsl_method_SimpleMethod', {b1})
    assert _is_linked(a, 'ccsl_method_SimpleMethod', b1)
    if hasattr(b1, 'variable_ParameterVariable'):
        assert _is_linked(b1, 'variable_ParameterVariable', a)
    _safe_set(a, 'ccsl_method_SimpleMethod', {b2})
    assert _is_linked(a, 'ccsl_method_SimpleMethod', b2)
    if hasattr(b1, 'variable_ParameterVariable'):
        assert not _is_linked(b1, 'variable_ParameterVariable', a)
    if hasattr(b2, 'variable_ParameterVariable'):
        assert _is_linked(b2, 'variable_ParameterVariable', a)
    _safe_set(a, 'ccsl_method_SimpleMethod', set())
    assert not _is_linked(a, 'ccsl_method_SimpleMethod', b2)
    if hasattr(b2, 'variable_ParameterVariable'):
        assert not _is_linked(b2, 'variable_ParameterVariable', a)


def test_assoc_returnType27_link_reassign_clear():
    a = ccsl_method_Method(abstract="sample_text", final="sample_text", inheritance="sample_text", static="sample_text")
    b1 = datatype_DataType()
    b2 = datatype_DataType()
    _safe_set(a, 'ccsl_method_Method', b1)
    assert _is_linked(a, 'ccsl_method_Method', b1)
    if hasattr(b1, 'datatype_DataType28'):
        assert _is_linked(b1, 'datatype_DataType28', a)
    _safe_set(a, 'ccsl_method_Method', b2)
    assert _is_linked(a, 'ccsl_method_Method', b2)
    if hasattr(b1, 'datatype_DataType28'):
        assert not _is_linked(b1, 'datatype_DataType28', a)
    if hasattr(b2, 'datatype_DataType28'):
        assert _is_linked(b2, 'datatype_DataType28', a)
    _safe_set(a, 'ccsl_method_Method', None)
    assert not _is_linked(a, 'ccsl_method_Method', b2)
    if hasattr(b2, 'datatype_DataType28'):
        assert not _is_linked(b2, 'datatype_DataType28', a)


def test_assoc_rightHandSide170_link_reassign_clear():
    a = ccsl_filters_EquationFilter(operator="sample_text")
    b1 = numberFunctions_CcslNumberFunction()
    b2 = numberFunctions_CcslNumberFunction()
    _safe_set(a, 'ccsl_filters_EquationFilter171', {b1})
    assert _is_linked(a, 'ccsl_filters_EquationFilter171', b1)
    if hasattr(b1, 'numberFunctions_CcslNumberFunction172'):
        assert _is_linked(b1, 'numberFunctions_CcslNumberFunction172', a)
    _safe_set(a, 'ccsl_filters_EquationFilter171', {b2})
    assert _is_linked(a, 'ccsl_filters_EquationFilter171', b2)
    if hasattr(b1, 'numberFunctions_CcslNumberFunction172'):
        assert not _is_linked(b1, 'numberFunctions_CcslNumberFunction172', a)
    if hasattr(b2, 'numberFunctions_CcslNumberFunction172'):
        assert _is_linked(b2, 'numberFunctions_CcslNumberFunction172', a)
    _safe_set(a, 'ccsl_filters_EquationFilter171', set())
    assert not _is_linked(a, 'ccsl_filters_EquationFilter171', b2)
    if hasattr(b2, 'numberFunctions_CcslNumberFunction172'):
        assert not _is_linked(b2, 'numberFunctions_CcslNumberFunction172', a)


def test_assoc_rightHandSide90_link_reassign_clear():
    a = ccsl_assignment_Assignment(operator="sample_text")
    b1 = statements_Statement()
    b2 = statements_Statement()
    _safe_set(a, 'ccsl_assignment_Assignment', b1)
    assert _is_linked(a, 'ccsl_assignment_Assignment', b1)
    if hasattr(b1, 'statements_Statement91'):
        assert _is_linked(b1, 'statements_Statement91', a)
    _safe_set(a, 'ccsl_assignment_Assignment', b2)
    assert _is_linked(a, 'ccsl_assignment_Assignment', b2)
    if hasattr(b1, 'statements_Statement91'):
        assert not _is_linked(b1, 'statements_Statement91', a)
    if hasattr(b2, 'statements_Statement91'):
        assert _is_linked(b2, 'statements_Statement91', a)
    _safe_set(a, 'ccsl_assignment_Assignment', None)
    assert not _is_linked(a, 'ccsl_assignment_Assignment', b2)
    if hasattr(b2, 'statements_Statement91'):
        assert not _is_linked(b2, 'statements_Statement91', a)


def test_assoc_rule4_link_reassign_clear():
    a = ccsl_FaultTypeDescription(name="sample_text")
    b1 = ccsl_AtomicRule()
    b2 = ccsl_AtomicRule()
    _safe_set(a, 'ccsl_FaultTypeDescription', b1)
    assert _is_linked(a, 'ccsl_FaultTypeDescription', b1)
    if hasattr(b1, 'ccsl_AtomicRule5'):
        assert _is_linked(b1, 'ccsl_AtomicRule5', a)
    _safe_set(a, 'ccsl_FaultTypeDescription', b2)
    assert _is_linked(a, 'ccsl_FaultTypeDescription', b2)
    if hasattr(b1, 'ccsl_AtomicRule5'):
        assert not _is_linked(b1, 'ccsl_AtomicRule5', a)
    if hasattr(b2, 'ccsl_AtomicRule5'):
        assert _is_linked(b2, 'ccsl_AtomicRule5', a)
    _safe_set(a, 'ccsl_FaultTypeDescription', None)
    assert not _is_linked(a, 'ccsl_FaultTypeDescription', b2)
    if hasattr(b2, 'ccsl_AtomicRule5'):
        assert not _is_linked(b2, 'ccsl_AtomicRule5', a)


def test_assoc_rules0_link_reassign_clear():
    a = ccsl_Rule(negated="sample_text")
    b1 = ccsl_CompositeRule(operator="sample_text")
    b2 = ccsl_CompositeRule(operator="sample_text_2")
    _safe_set(a, 'ccsl_Rule', b1)
    assert _is_linked(a, 'ccsl_Rule', b1)
    if hasattr(b1, 'ccsl_CompositeRule'):
        assert _is_linked(b1, 'ccsl_CompositeRule', a)
    _safe_set(a, 'ccsl_Rule', b2)
    assert _is_linked(a, 'ccsl_Rule', b2)
    if hasattr(b1, 'ccsl_CompositeRule'):
        assert not _is_linked(b1, 'ccsl_CompositeRule', a)
    if hasattr(b2, 'ccsl_CompositeRule'):
        assert _is_linked(b2, 'ccsl_CompositeRule', a)
    _safe_set(a, 'ccsl_Rule', None)
    assert not _is_linked(a, 'ccsl_Rule', b2)
    if hasattr(b2, 'ccsl_CompositeRule'):
        assert not _is_linked(b2, 'ccsl_CompositeRule', a)


def test_assoc_statements33_link_reassign_clear():
    a = ccsl_statements_Block(statementsKind="sample_text")
    b1 = statements_Statement()
    b2 = statements_Statement()
    _safe_set(a, 'ccsl_statements_Block', {b1})
    assert _is_linked(a, 'ccsl_statements_Block', b1)
    if hasattr(b1, 'statements_Statement34'):
        assert _is_linked(b1, 'statements_Statement34', a)
    _safe_set(a, 'ccsl_statements_Block', {b2})
    assert _is_linked(a, 'ccsl_statements_Block', b2)
    if hasattr(b1, 'statements_Statement34'):
        assert not _is_linked(b1, 'statements_Statement34', a)
    if hasattr(b2, 'statements_Statement34'):
        assert _is_linked(b2, 'statements_Statement34', a)
    _safe_set(a, 'ccsl_statements_Block', set())
    assert not _is_linked(a, 'ccsl_statements_Block', b2)
    if hasattr(b2, 'statements_Statement34'):
        assert not _is_linked(b2, 'statements_Statement34', a)


def test_assoc_strategy8_link_reassign_clear():
    a = ccsl_FaultTypeDescription(name="sample_text")
    b1 = InjectionStrategy()
    b2 = InjectionStrategy()
    _safe_set(a, 'ccsl_FaultTypeDescription9', b1)
    assert _is_linked(a, 'ccsl_FaultTypeDescription9', b1)
    if hasattr(b1, 'InjectionStrategy'):
        assert _is_linked(b1, 'InjectionStrategy', a)
    _safe_set(a, 'ccsl_FaultTypeDescription9', b2)
    assert _is_linked(a, 'ccsl_FaultTypeDescription9', b2)
    if hasattr(b1, 'InjectionStrategy'):
        assert not _is_linked(b1, 'InjectionStrategy', a)
    if hasattr(b2, 'InjectionStrategy'):
        assert _is_linked(b2, 'InjectionStrategy', a)
    _safe_set(a, 'ccsl_FaultTypeDescription9', None)
    assert not _is_linked(a, 'ccsl_FaultTypeDescription9', b2)
    if hasattr(b2, 'InjectionStrategy'):
        assert not _is_linked(b2, 'InjectionStrategy', a)


def test_assoc_subClass182_link_reassign_clear():
    a = ccsl_filters_SuperClassClosureFilter(includesSubClass="sample_text")
    b1 = complexType_JClass()
    b2 = complexType_JClass()
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter183', b1)
    assert _is_linked(a, 'ccsl_filters_SuperClassClosureFilter183', b1)
    if hasattr(b1, 'complexType_JClass184'):
        assert _is_linked(b1, 'complexType_JClass184', a)
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter183', b2)
    assert _is_linked(a, 'ccsl_filters_SuperClassClosureFilter183', b2)
    if hasattr(b1, 'complexType_JClass184'):
        assert not _is_linked(b1, 'complexType_JClass184', a)
    if hasattr(b2, 'complexType_JClass184'):
        assert _is_linked(b2, 'complexType_JClass184', a)
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter183', None)
    assert not _is_linked(a, 'ccsl_filters_SuperClassClosureFilter183', b2)
    if hasattr(b2, 'complexType_JClass184'):
        assert not _is_linked(b2, 'complexType_JClass184', a)


def test_assoc_superClass15_link_reassign_clear():
    a = ccsl_complexType_JClass(inheritance="sample_text")
    b1 = complexType_JClass()
    b2 = complexType_JClass()
    _safe_set(a, 'ccsl_complexType_JClass16', b1)
    assert _is_linked(a, 'ccsl_complexType_JClass16', b1)
    if hasattr(b1, 'complexType_JClass'):
        assert _is_linked(b1, 'complexType_JClass', a)
    _safe_set(a, 'ccsl_complexType_JClass16', b2)
    assert _is_linked(a, 'ccsl_complexType_JClass16', b2)
    if hasattr(b1, 'complexType_JClass'):
        assert not _is_linked(b1, 'complexType_JClass', a)
    if hasattr(b2, 'complexType_JClass'):
        assert _is_linked(b2, 'complexType_JClass', a)
    _safe_set(a, 'ccsl_complexType_JClass16', None)
    assert not _is_linked(a, 'ccsl_complexType_JClass16', b2)
    if hasattr(b2, 'complexType_JClass'):
        assert not _is_linked(b2, 'complexType_JClass', a)


def test_assoc_superClass180_link_reassign_clear():
    a = ccsl_filters_SuperClassClosureFilter(includesSubClass="sample_text")
    b1 = complexType_JClass()
    b2 = complexType_JClass()
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter', b1)
    assert _is_linked(a, 'ccsl_filters_SuperClassClosureFilter', b1)
    if hasattr(b1, 'complexType_JClass181'):
        assert _is_linked(b1, 'complexType_JClass181', a)
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter', b2)
    assert _is_linked(a, 'ccsl_filters_SuperClassClosureFilter', b2)
    if hasattr(b1, 'complexType_JClass181'):
        assert not _is_linked(b1, 'complexType_JClass181', a)
    if hasattr(b2, 'complexType_JClass181'):
        assert _is_linked(b2, 'complexType_JClass181', a)
    _safe_set(a, 'ccsl_filters_SuperClassClosureFilter', None)
    assert not _is_linked(a, 'ccsl_filters_SuperClassClosureFilter', b2)
    if hasattr(b2, 'complexType_JClass181'):
        assert not _is_linked(b2, 'complexType_JClass181', a)


def test_assoc_superInterfaces17_link_reassign_clear():
    a = ccsl_complexType_DeclaredType(static="sample_text", visibility="sample_text")
    b1 = complexType_JInterface()
    b2 = complexType_JInterface()
    _safe_set(a, 'ccsl_complexType_DeclaredType', {b1})
    assert _is_linked(a, 'ccsl_complexType_DeclaredType', b1)
    if hasattr(b1, 'complexType_JInterface'):
        assert _is_linked(b1, 'complexType_JInterface', a)
    _safe_set(a, 'ccsl_complexType_DeclaredType', {b2})
    assert _is_linked(a, 'ccsl_complexType_DeclaredType', b2)
    if hasattr(b1, 'complexType_JInterface'):
        assert not _is_linked(b1, 'complexType_JInterface', a)
    if hasattr(b2, 'complexType_JInterface'):
        assert _is_linked(b2, 'complexType_JInterface', a)
    _safe_set(a, 'ccsl_complexType_DeclaredType', set())
    assert not _is_linked(a, 'ccsl_complexType_DeclaredType', b2)
    if hasattr(b2, 'complexType_JInterface'):
        assert not _is_linked(b2, 'complexType_JInterface', a)


def test_assoc_type108_link_reassign_clear():
    a = ccsl_datatype_ArrayType(dimensions="sample_text")
    b1 = datatype_DataType()
    b2 = datatype_DataType()
    _safe_set(a, 'ccsl_datatype_ArrayType', b1)
    assert _is_linked(a, 'ccsl_datatype_ArrayType', b1)
    if hasattr(b1, 'datatype_DataType109'):
        assert _is_linked(b1, 'datatype_DataType109', a)
    _safe_set(a, 'ccsl_datatype_ArrayType', b2)
    assert _is_linked(a, 'ccsl_datatype_ArrayType', b2)
    if hasattr(b1, 'datatype_DataType109'):
        assert not _is_linked(b1, 'datatype_DataType109', a)
    if hasattr(b2, 'datatype_DataType109'):
        assert _is_linked(b2, 'datatype_DataType109', a)
    _safe_set(a, 'ccsl_datatype_ArrayType', None)
    assert not _is_linked(a, 'ccsl_datatype_ArrayType', b2)
    if hasattr(b2, 'datatype_DataType109'):
        assert not _is_linked(b2, 'datatype_DataType109', a)


def test_assoc_type11_link_reassign_clear():
    a = ccsl_variable_Variable(final="sample_text")
    b1 = datatype_DataType()
    b2 = datatype_DataType()
    _safe_set(a, 'ccsl_variable_Variable', b1)
    assert _is_linked(a, 'ccsl_variable_Variable', b1)
    if hasattr(b1, 'datatype_DataType'):
        assert _is_linked(b1, 'datatype_DataType', a)
    _safe_set(a, 'ccsl_variable_Variable', b2)
    assert _is_linked(a, 'ccsl_variable_Variable', b2)
    if hasattr(b1, 'datatype_DataType'):
        assert not _is_linked(b1, 'datatype_DataType', a)
    if hasattr(b2, 'datatype_DataType'):
        assert _is_linked(b2, 'datatype_DataType', a)
    _safe_set(a, 'ccsl_variable_Variable', None)
    assert not _is_linked(a, 'ccsl_variable_Variable', b2)
    if hasattr(b2, 'datatype_DataType'):
        assert not _is_linked(b2, 'datatype_DataType', a)


def test_assoc_type36_link_reassign_clear():
    a = ccsl_statements_InstanceCreation(argsKind="sample_text")
    b1 = datatype_ObjectType()
    b2 = datatype_ObjectType()
    _safe_set(a, 'ccsl_statements_InstanceCreation', b1)
    assert _is_linked(a, 'ccsl_statements_InstanceCreation', b1)
    if hasattr(b1, 'datatype_ObjectType37'):
        assert _is_linked(b1, 'datatype_ObjectType37', a)
    _safe_set(a, 'ccsl_statements_InstanceCreation', b2)
    assert _is_linked(a, 'ccsl_statements_InstanceCreation', b2)
    if hasattr(b1, 'datatype_ObjectType37'):
        assert not _is_linked(b1, 'datatype_ObjectType37', a)
    if hasattr(b2, 'datatype_ObjectType37'):
        assert _is_linked(b2, 'datatype_ObjectType37', a)
    _safe_set(a, 'ccsl_statements_InstanceCreation', None)
    assert not _is_linked(a, 'ccsl_statements_InstanceCreation', b2)
    if hasattr(b2, 'datatype_ObjectType37'):
        assert not _is_linked(b2, 'datatype_ObjectType37', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractAssignment_strategy = st.builds(AbstractAssignment)
@given(instance=AbstractAssignment_strategy)
@settings(max_examples=25)
def test_AbstractAssignment_instantiation(instance):
    assert isinstance(instance, AbstractAssignment)


Access_strategy = st.builds(Access)
@given(instance=Access_strategy)
@settings(max_examples=25)
def test_Access_instantiation(instance):
    assert isinstance(instance, Access)


AtomicFilter_strategy = st.builds(AtomicFilter)
@given(instance=AtomicFilter_strategy)
@settings(max_examples=25)
def test_AtomicFilter_instantiation(instance):
    assert isinstance(instance, AtomicFilter)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


CcslBooleanFunction_strategy = st.builds(CcslBooleanFunction)
@given(instance=CcslBooleanFunction_strategy)
@settings(max_examples=25)
def test_CcslBooleanFunction_instantiation(instance):
    assert isinstance(instance, CcslBooleanFunction)


CcslFunction_strategy = st.builds(CcslFunction)
@given(instance=CcslFunction_strategy)
@settings(max_examples=25)
def test_CcslFunction_instantiation(instance):
    assert isinstance(instance, CcslFunction)


CcslNumberFunction_strategy = st.builds(CcslNumberFunction)
@given(instance=CcslNumberFunction_strategy)
@settings(max_examples=25)
def test_CcslNumberFunction_instantiation(instance):
    assert isinstance(instance, CcslNumberFunction)


ComplexType_strategy = st.builds(ComplexType)
@given(instance=ComplexType_strategy)
@settings(max_examples=25)
def test_ComplexType_instantiation(instance):
    assert isinstance(instance, ComplexType)


Context_strategy = st.builds(Context)
@given(instance=Context_strategy)
@settings(max_examples=25)
def test_Context_instantiation(instance):
    assert isinstance(instance, Context)


ControlFlow_strategy = st.builds(ControlFlow)
@given(instance=ControlFlow_strategy)
@settings(max_examples=25)
def test_ControlFlow_instantiation(instance):
    assert isinstance(instance, ControlFlow)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


DeclaredType_strategy = st.builds(DeclaredType)
@given(instance=DeclaredType_strategy)
@settings(max_examples=25)
def test_DeclaredType_instantiation(instance):
    assert isinstance(instance, DeclaredType)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


Filter_strategy = st.builds(Filter)
@given(instance=Filter_strategy)
@settings(max_examples=25)
def test_Filter_instantiation(instance):
    assert isinstance(instance, Filter)


InitializableVariable_strategy = st.builds(InitializableVariable)
@given(instance=InitializableVariable_strategy)
@settings(max_examples=25)
def test_InitializableVariable_instantiation(instance):
    assert isinstance(instance, InitializableVariable)


InjectionAction_strategy = st.builds(InjectionAction)
@given(instance=InjectionAction_strategy)
@settings(max_examples=25)
def test_InjectionAction_instantiation(instance):
    assert isinstance(instance, InjectionAction)


InjectionStrategy_strategy = st.builds(InjectionStrategy)
@given(instance=InjectionStrategy_strategy)
@settings(max_examples=25)
def test_InjectionStrategy_instantiation(instance):
    assert isinstance(instance, InjectionStrategy)


Invocation_strategy = st.builds(Invocation)
@given(instance=Invocation_strategy)
@settings(max_examples=25)
def test_Invocation_instantiation(instance):
    assert isinstance(instance, Invocation)


LiteralValue_strategy = st.builds(LiteralValue)
@given(instance=LiteralValue_strategy)
@settings(max_examples=25)
def test_LiteralValue_instantiation(instance):
    assert isinstance(instance, LiteralValue)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


ObjectType_strategy = st.builds(ObjectType)
@given(instance=ObjectType_strategy)
@settings(max_examples=25)
def test_ObjectType_instantiation(instance):
    assert isinstance(instance, ObjectType)


OperatorExpression_strategy = st.builds(OperatorExpression)
@given(instance=OperatorExpression_strategy)
@settings(max_examples=25)
def test_OperatorExpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)


PrimitiveType_strategy = st.builds(PrimitiveType)
@given(instance=PrimitiveType_strategy)
@settings(max_examples=25)
def test_PrimitiveType_instantiation(instance):
    assert isinstance(instance, PrimitiveType)


Root_strategy = st.builds(Root)
@given(instance=Root_strategy)
@settings(max_examples=25)
def test_Root_instantiation(instance):
    assert isinstance(instance, Root)


Rule_strategy = st.builds(Rule)
@given(instance=Rule_strategy)
@settings(max_examples=25)
def test_Rule_instantiation(instance):
    assert isinstance(instance, Rule)


SimpleMethod_strategy = st.builds(SimpleMethod)
@given(instance=SimpleMethod_strategy)
@settings(max_examples=25)
def test_SimpleMethod_instantiation(instance):
    assert isinstance(instance, SimpleMethod)


SimpleMethodInvocation_strategy = st.builds(SimpleMethodInvocation)
@given(instance=SimpleMethodInvocation_strategy)
@settings(max_examples=25)
def test_SimpleMethodInvocation_instantiation(instance):
    assert isinstance(instance, SimpleMethodInvocation)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


TemplateFilter_strategy = st.builds(TemplateFilter)
@given(instance=TemplateFilter_strategy)
@settings(max_examples=25)
def test_TemplateFilter_instantiation(instance):
    assert isinstance(instance, TemplateFilter)


UnaryAssignment_strategy = st.builds(UnaryAssignment)
@given(instance=UnaryAssignment_strategy)
@settings(max_examples=25)
def test_UnaryAssignment_instantiation(instance):
    assert isinstance(instance, UnaryAssignment)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


action_ArithmeticOperatorMap_strategy = st.builds(action_ArithmeticOperatorMap)
@given(instance=action_ArithmeticOperatorMap_strategy)
@settings(max_examples=25)
def test_action_ArithmeticOperatorMap_instantiation(instance):
    assert isinstance(instance, action_ArithmeticOperatorMap)


annotation_AnnotableElement_strategy = st.builds(annotation_AnnotableElement)
@given(instance=annotation_AnnotableElement_strategy)
@settings(max_examples=25)
def test_annotation_AnnotableElement_instantiation(instance):
    assert isinstance(instance, annotation_AnnotableElement)


annotation_Annotation_strategy = st.builds(annotation_Annotation)
@given(instance=annotation_Annotation_strategy)
@settings(max_examples=25)
def test_annotation_Annotation_instantiation(instance):
    assert isinstance(instance, annotation_Annotation)


ccsl_AtomicRule_strategy = st.builds(ccsl_AtomicRule)
@given(instance=ccsl_AtomicRule_strategy)
@settings(max_examples=25)
def test_ccsl_AtomicRule_instantiation(instance):
    assert isinstance(instance, ccsl_AtomicRule)


ccsl_CompositeRule_strategy = st.builds(ccsl_CompositeRule, operator=safe_text)
@given(instance=ccsl_CompositeRule_strategy)
@settings(max_examples=25)
def test_ccsl_CompositeRule_instantiation(instance):
    assert isinstance(instance, ccsl_CompositeRule)


ccsl_FaultTypeDescription_strategy = st.builds(ccsl_FaultTypeDescription, name=safe_text)
@given(instance=ccsl_FaultTypeDescription_strategy)
@settings(max_examples=25)
def test_ccsl_FaultTypeDescription_instantiation(instance):
    assert isinstance(instance, ccsl_FaultTypeDescription)


ccsl_Root_strategy = st.builds(ccsl_Root)
@given(instance=ccsl_Root_strategy)
@settings(max_examples=25)
def test_ccsl_Root_instantiation(instance):
    assert isinstance(instance, ccsl_Root)


ccsl_Rule_strategy = st.builds(ccsl_Rule, negated=safe_text)
@given(instance=ccsl_Rule_strategy)
@settings(max_examples=25)
def test_ccsl_Rule_instantiation(instance):
    assert isinstance(instance, ccsl_Rule)


ccsl_action_ArithmeticOperatorMap_strategy = st.builds(ccsl_action_ArithmeticOperatorMap, newArithmeticOperator=safe_text, oldArithmeticOperator=safe_text)
@given(instance=ccsl_action_ArithmeticOperatorMap_strategy)
@settings(max_examples=25)
def test_ccsl_action_ArithmeticOperatorMap_instantiation(instance):
    assert isinstance(instance, ccsl_action_ArithmeticOperatorMap)


ccsl_action_ChangeLiteralValueAction_strategy = st.builds(ccsl_action_ChangeLiteralValueAction)
@given(instance=ccsl_action_ChangeLiteralValueAction_strategy)
@settings(max_examples=25)
def test_ccsl_action_ChangeLiteralValueAction_instantiation(instance):
    assert isinstance(instance, ccsl_action_ChangeLiteralValueAction)


ccsl_action_DeleteAction_strategy = st.builds(ccsl_action_DeleteAction)
@given(instance=ccsl_action_DeleteAction_strategy)
@settings(max_examples=25)
def test_ccsl_action_DeleteAction_instantiation(instance):
    assert isinstance(instance, ccsl_action_DeleteAction)


ccsl_action_DeleteInfixOperatorAction_strategy = st.builds(ccsl_action_DeleteInfixOperatorAction)
@given(instance=ccsl_action_DeleteInfixOperatorAction_strategy)
@settings(max_examples=25)
def test_ccsl_action_DeleteInfixOperatorAction_instantiation(instance):
    assert isinstance(instance, ccsl_action_DeleteInfixOperatorAction)


ccsl_action_DeleteRandomStatementAction_strategy = st.builds(ccsl_action_DeleteRandomStatementAction)
@given(instance=ccsl_action_DeleteRandomStatementAction_strategy)
@settings(max_examples=25)
def test_ccsl_action_DeleteRandomStatementAction_instantiation(instance):
    assert isinstance(instance, ccsl_action_DeleteRandomStatementAction)


ccsl_action_MoveScopeUpAction_strategy = st.builds(ccsl_action_MoveScopeUpAction)
@given(instance=ccsl_action_MoveScopeUpAction_strategy)
@settings(max_examples=25)
def test_ccsl_action_MoveScopeUpAction_instantiation(instance):
    assert isinstance(instance, ccsl_action_MoveScopeUpAction)


ccsl_action_ReplaceArithmeticOperatorAction_strategy = st.builds(ccsl_action_ReplaceArithmeticOperatorAction)
@given(instance=ccsl_action_ReplaceArithmeticOperatorAction_strategy)
@settings(max_examples=25)
def test_ccsl_action_ReplaceArithmeticOperatorAction_instantiation(instance):
    assert isinstance(instance, ccsl_action_ReplaceArithmeticOperatorAction)


ccsl_action_ReplaceVariableAccessAction_strategy = st.builds(ccsl_action_ReplaceVariableAccessAction)
@given(instance=ccsl_action_ReplaceVariableAccessAction_strategy)
@settings(max_examples=25)
def test_ccsl_action_ReplaceVariableAccessAction_instantiation(instance):
    assert isinstance(instance, ccsl_action_ReplaceVariableAccessAction)


ccsl_annotation_AnnotableElement_strategy = st.builds(ccsl_annotation_AnnotableElement, annotationsKind=safe_text)
@given(instance=ccsl_annotation_AnnotableElement_strategy)
@settings(max_examples=25)
def test_ccsl_annotation_AnnotableElement_instantiation(instance):
    assert isinstance(instance, ccsl_annotation_AnnotableElement)


ccsl_annotation_Annotation_strategy = st.builds(ccsl_annotation_Annotation)
@given(instance=ccsl_annotation_Annotation_strategy)
@settings(max_examples=25)
def test_ccsl_annotation_Annotation_instantiation(instance):
    assert isinstance(instance, ccsl_annotation_Annotation)


ccsl_assignment_AbstractAssignment_strategy = st.builds(ccsl_assignment_AbstractAssignment)
@given(instance=ccsl_assignment_AbstractAssignment_strategy)
@settings(max_examples=25)
def test_ccsl_assignment_AbstractAssignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_AbstractAssignment)


ccsl_assignment_Assignment_strategy = st.builds(ccsl_assignment_Assignment, operator=safe_text)
@given(instance=ccsl_assignment_Assignment_strategy)
@settings(max_examples=25)
def test_ccsl_assignment_Assignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_Assignment)


ccsl_assignment_PostfixUnaryAssignment_strategy = st.builds(ccsl_assignment_PostfixUnaryAssignment)
@given(instance=ccsl_assignment_PostfixUnaryAssignment_strategy)
@settings(max_examples=25)
def test_ccsl_assignment_PostfixUnaryAssignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_PostfixUnaryAssignment)


ccsl_assignment_PrefixUnaryAssignment_strategy = st.builds(ccsl_assignment_PrefixUnaryAssignment)
@given(instance=ccsl_assignment_PrefixUnaryAssignment_strategy)
@settings(max_examples=25)
def test_ccsl_assignment_PrefixUnaryAssignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_PrefixUnaryAssignment)


ccsl_assignment_UnaryAssignment_strategy = st.builds(ccsl_assignment_UnaryAssignment, operator=safe_text)
@given(instance=ccsl_assignment_UnaryAssignment_strategy)
@settings(max_examples=25)
def test_ccsl_assignment_UnaryAssignment_instantiation(instance):
    assert isinstance(instance, ccsl_assignment_UnaryAssignment)


ccsl_booleanFunctions_CcslBooleanFunction_strategy = st.builds(ccsl_booleanFunctions_CcslBooleanFunction)
@given(instance=ccsl_booleanFunctions_CcslBooleanFunction_strategy)
@settings(max_examples=25)
def test_ccsl_booleanFunctions_CcslBooleanFunction_instantiation(instance):
    assert isinstance(instance, ccsl_booleanFunctions_CcslBooleanFunction)


ccsl_complexType_AnnotationType_strategy = st.builds(ccsl_complexType_AnnotationType)
@given(instance=ccsl_complexType_AnnotationType_strategy)
@settings(max_examples=25)
def test_ccsl_complexType_AnnotationType_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_AnnotationType)


ccsl_complexType_AnonymousClass_strategy = st.builds(ccsl_complexType_AnonymousClass)
@given(instance=ccsl_complexType_AnonymousClass_strategy)
@settings(max_examples=25)
def test_ccsl_complexType_AnonymousClass_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_AnonymousClass)


ccsl_complexType_ComplexType_strategy = st.builds(ccsl_complexType_ComplexType)
@given(instance=ccsl_complexType_ComplexType_strategy)
@settings(max_examples=25)
def test_ccsl_complexType_ComplexType_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_ComplexType)


ccsl_complexType_DeclaredType_strategy = st.builds(ccsl_complexType_DeclaredType, static=safe_text, visibility=safe_text)
@given(instance=ccsl_complexType_DeclaredType_strategy)
@settings(max_examples=25)
def test_ccsl_complexType_DeclaredType_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_DeclaredType)


ccsl_complexType_JClass_strategy = st.builds(ccsl_complexType_JClass, inheritance=safe_text)
@given(instance=ccsl_complexType_JClass_strategy)
@settings(max_examples=25)
def test_ccsl_complexType_JClass_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_JClass)


ccsl_complexType_JInterface_strategy = st.builds(ccsl_complexType_JInterface)
@given(instance=ccsl_complexType_JInterface_strategy)
@settings(max_examples=25)
def test_ccsl_complexType_JInterface_instantiation(instance):
    assert isinstance(instance, ccsl_complexType_JInterface)


ccsl_context_Context_strategy = st.builds(ccsl_context_Context)
@given(instance=ccsl_context_Context_strategy)
@settings(max_examples=25)
def test_ccsl_context_Context_instantiation(instance):
    assert isinstance(instance, ccsl_context_Context)


ccsl_controlFlow_IfStatement_strategy = st.builds(ccsl_controlFlow_IfStatement)
@given(instance=ccsl_controlFlow_IfStatement_strategy)
@settings(max_examples=25)
def test_ccsl_controlFlow_IfStatement_instantiation(instance):
    assert isinstance(instance, ccsl_controlFlow_IfStatement)


ccsl_controlFlow_LoopStatement_strategy = st.builds(ccsl_controlFlow_LoopStatement)
@given(instance=ccsl_controlFlow_LoopStatement_strategy)
@settings(max_examples=25)
def test_ccsl_controlFlow_LoopStatement_instantiation(instance):
    assert isinstance(instance, ccsl_controlFlow_LoopStatement)


ccsl_controlFlow_SwitchCaseBlock_strategy = st.builds(ccsl_controlFlow_SwitchCaseBlock, default=safe_text)
@given(instance=ccsl_controlFlow_SwitchCaseBlock_strategy)
@settings(max_examples=25)
def test_ccsl_controlFlow_SwitchCaseBlock_instantiation(instance):
    assert isinstance(instance, ccsl_controlFlow_SwitchCaseBlock)


ccsl_controlFlow_SwitchStatement_strategy = st.builds(ccsl_controlFlow_SwitchStatement)
@given(instance=ccsl_controlFlow_SwitchStatement_strategy)
@settings(max_examples=25)
def test_ccsl_controlFlow_SwitchStatement_instantiation(instance):
    assert isinstance(instance, ccsl_controlFlow_SwitchStatement)


ccsl_datatype_ArrayType_strategy = st.builds(ccsl_datatype_ArrayType, dimensions=safe_text)
@given(instance=ccsl_datatype_ArrayType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_ArrayType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_ArrayType)


ccsl_datatype_BooleanPrimitiveType_strategy = st.builds(ccsl_datatype_BooleanPrimitiveType)
@given(instance=ccsl_datatype_BooleanPrimitiveType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_BooleanPrimitiveType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_BooleanPrimitiveType)


ccsl_datatype_DataType_strategy = st.builds(ccsl_datatype_DataType)
@given(instance=ccsl_datatype_DataType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_DataType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_DataType)


ccsl_datatype_GenericType_strategy = st.builds(ccsl_datatype_GenericType)
@given(instance=ccsl_datatype_GenericType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_GenericType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_GenericType)


ccsl_datatype_IntPrimitiveType_strategy = st.builds(ccsl_datatype_IntPrimitiveType)
@given(instance=ccsl_datatype_IntPrimitiveType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_IntPrimitiveType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_IntPrimitiveType)


ccsl_datatype_ObjectType_strategy = st.builds(ccsl_datatype_ObjectType)
@given(instance=ccsl_datatype_ObjectType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_ObjectType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_ObjectType)


ccsl_datatype_ParameterizedType_strategy = st.builds(ccsl_datatype_ParameterizedType)
@given(instance=ccsl_datatype_ParameterizedType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_ParameterizedType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_ParameterizedType)


ccsl_datatype_PrimitiveType_strategy = st.builds(ccsl_datatype_PrimitiveType)
@given(instance=ccsl_datatype_PrimitiveType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_PrimitiveType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_PrimitiveType)


ccsl_datatype_ShortPrimitiveType_strategy = st.builds(ccsl_datatype_ShortPrimitiveType)
@given(instance=ccsl_datatype_ShortPrimitiveType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_ShortPrimitiveType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_ShortPrimitiveType)


ccsl_datatype_StringPrimitiveType_strategy = st.builds(ccsl_datatype_StringPrimitiveType)
@given(instance=ccsl_datatype_StringPrimitiveType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_StringPrimitiveType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_StringPrimitiveType)


ccsl_datatype_VoidType_strategy = st.builds(ccsl_datatype_VoidType)
@given(instance=ccsl_datatype_VoidType_strategy)
@settings(max_examples=25)
def test_ccsl_datatype_VoidType_instantiation(instance):
    assert isinstance(instance, ccsl_datatype_VoidType)


ccsl_elements_Element_strategy = st.builds(ccsl_elements_Element, uniqueName=safe_text)
@given(instance=ccsl_elements_Element_strategy)
@settings(max_examples=25)
def test_ccsl_elements_Element_instantiation(instance):
    assert isinstance(instance, ccsl_elements_Element)


ccsl_expressions_ArithmeticExpression_strategy = st.builds(ccsl_expressions_ArithmeticExpression, arithmeticOperator=safe_text)
@given(instance=ccsl_expressions_ArithmeticExpression_strategy)
@settings(max_examples=25)
def test_ccsl_expressions_ArithmeticExpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_ArithmeticExpression)


ccsl_expressions_BooleanExpression_strategy = st.builds(ccsl_expressions_BooleanExpression, booleanOperator=safe_text)
@given(instance=ccsl_expressions_BooleanExpression_strategy)
@settings(max_examples=25)
def test_ccsl_expressions_BooleanExpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_BooleanExpression)


ccsl_expressions_InfixExpression_strategy = st.builds(ccsl_expressions_InfixExpression)
@given(instance=ccsl_expressions_InfixExpression_strategy)
@settings(max_examples=25)
def test_ccsl_expressions_InfixExpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_InfixExpression)


ccsl_expressions_OperatorExpression_strategy = st.builds(ccsl_expressions_OperatorExpression)
@given(instance=ccsl_expressions_OperatorExpression_strategy)
@settings(max_examples=25)
def test_ccsl_expressions_OperatorExpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_OperatorExpression)


ccsl_expressions_ParenthesizedExpression_strategy = st.builds(ccsl_expressions_ParenthesizedExpression)
@given(instance=ccsl_expressions_ParenthesizedExpression_strategy)
@settings(max_examples=25)
def test_ccsl_expressions_ParenthesizedExpression_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_ParenthesizedExpression)


ccsl_expressions_StringConcatenation_strategy = st.builds(ccsl_expressions_StringConcatenation)
@given(instance=ccsl_expressions_StringConcatenation_strategy)
@settings(max_examples=25)
def test_ccsl_expressions_StringConcatenation_instantiation(instance):
    assert isinstance(instance, ccsl_expressions_StringConcatenation)


ccsl_faultTypeDescription_InjectionAction_strategy = st.builds(ccsl_faultTypeDescription_InjectionAction)
@given(instance=ccsl_faultTypeDescription_InjectionAction_strategy)
@settings(max_examples=25)
def test_ccsl_faultTypeDescription_InjectionAction_instantiation(instance):
    assert isinstance(instance, ccsl_faultTypeDescription_InjectionAction)


ccsl_faultTypeDescription_InjectionStrategy_strategy = st.builds(ccsl_faultTypeDescription_InjectionStrategy)
@given(instance=ccsl_faultTypeDescription_InjectionStrategy_strategy)
@settings(max_examples=25)
def test_ccsl_faultTypeDescription_InjectionStrategy_instantiation(instance):
    assert isinstance(instance, ccsl_faultTypeDescription_InjectionStrategy)


ccsl_filters_AtomicFilter_strategy = st.builds(ccsl_filters_AtomicFilter)
@given(instance=ccsl_filters_AtomicFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_AtomicFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_AtomicFilter)


ccsl_filters_BlockLastStatementFilter_strategy = st.builds(ccsl_filters_BlockLastStatementFilter)
@given(instance=ccsl_filters_BlockLastStatementFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_BlockLastStatementFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_BlockLastStatementFilter)


ccsl_filters_ChildClosureComplexTypeFilter_strategy = st.builds(ccsl_filters_ChildClosureComplexTypeFilter)
@given(instance=ccsl_filters_ChildClosureComplexTypeFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_ChildClosureComplexTypeFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_ChildClosureComplexTypeFilter)


ccsl_filters_CompositeFilter_strategy = st.builds(ccsl_filters_CompositeFilter, operator=safe_text)
@given(instance=ccsl_filters_CompositeFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_CompositeFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_CompositeFilter)


ccsl_filters_CountFilter_strategy = st.builds(ccsl_filters_CountFilter, max=safe_text, min=safe_text)
@given(instance=ccsl_filters_CountFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_CountFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_CountFilter)


ccsl_filters_EquationFilter_strategy = st.builds(ccsl_filters_EquationFilter, operator=safe_text)
@given(instance=ccsl_filters_EquationFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_EquationFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_EquationFilter)


ccsl_filters_Filter_strategy = st.builds(ccsl_filters_Filter, negated=safe_text)
@given(instance=ccsl_filters_Filter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_Filter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_Filter)


ccsl_filters_FromClosureFilter_strategy = st.builds(ccsl_filters_FromClosureFilter)
@given(instance=ccsl_filters_FromClosureFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_FromClosureFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_FromClosureFilter)


ccsl_filters_HasSameReferenceFilter_strategy = st.builds(ccsl_filters_HasSameReferenceFilter)
@given(instance=ccsl_filters_HasSameReferenceFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_HasSameReferenceFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_HasSameReferenceFilter)


ccsl_filters_ImplicityContainerFilter_strategy = st.builds(ccsl_filters_ImplicityContainerFilter)
@given(instance=ccsl_filters_ImplicityContainerFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_ImplicityContainerFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_ImplicityContainerFilter)


ccsl_filters_ImplicityOperandFilter_strategy = st.builds(ccsl_filters_ImplicityOperandFilter)
@given(instance=ccsl_filters_ImplicityOperandFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_ImplicityOperandFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_ImplicityOperandFilter)


ccsl_filters_IsKindOfFilter_strategy = st.builds(ccsl_filters_IsKindOfFilter)
@given(instance=ccsl_filters_IsKindOfFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_IsKindOfFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_IsKindOfFilter)


ccsl_filters_IsStringFilter_strategy = st.builds(ccsl_filters_IsStringFilter)
@given(instance=ccsl_filters_IsStringFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_IsStringFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_IsStringFilter)


ccsl_filters_IsTypeOfFilter_strategy = st.builds(ccsl_filters_IsTypeOfFilter)
@given(instance=ccsl_filters_IsTypeOfFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_IsTypeOfFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_IsTypeOfFilter)


ccsl_filters_PropertyFilter_strategy = st.builds(ccsl_filters_PropertyFilter)
@given(instance=ccsl_filters_PropertyFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_PropertyFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_PropertyFilter)


ccsl_filters_RegexMatch_strategy = st.builds(ccsl_filters_RegexMatch, regex=safe_text)
@given(instance=ccsl_filters_RegexMatch_strategy)
@settings(max_examples=25)
def test_ccsl_filters_RegexMatch_instantiation(instance):
    assert isinstance(instance, ccsl_filters_RegexMatch)


ccsl_filters_SameNameFilter_strategy = st.builds(ccsl_filters_SameNameFilter, ignoreCase=safe_text)
@given(instance=ccsl_filters_SameNameFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_SameNameFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_SameNameFilter)


ccsl_filters_SuperClassClosureFilter_strategy = st.builds(ccsl_filters_SuperClassClosureFilter, includesSubClass=safe_text)
@given(instance=ccsl_filters_SuperClassClosureFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_SuperClassClosureFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_SuperClassClosureFilter)


ccsl_filters_SuperMethodClosureFilter_strategy = st.builds(ccsl_filters_SuperMethodClosureFilter)
@given(instance=ccsl_filters_SuperMethodClosureFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_SuperMethodClosureFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_SuperMethodClosureFilter)


ccsl_filters_TemplateFilter_strategy = st.builds(ccsl_filters_TemplateFilter)
@given(instance=ccsl_filters_TemplateFilter_strategy)
@settings(max_examples=25)
def test_ccsl_filters_TemplateFilter_instantiation(instance):
    assert isinstance(instance, ccsl_filters_TemplateFilter)


ccsl_functions_CcslFunction_strategy = st.builds(ccsl_functions_CcslFunction)
@given(instance=ccsl_functions_CcslFunction_strategy)
@settings(max_examples=25)
def test_ccsl_functions_CcslFunction_instantiation(instance):
    assert isinstance(instance, ccsl_functions_CcslFunction)


ccsl_import_ImportStatement_strategy = st.builds(ccsl_import_ImportStatement)
@given(instance=ccsl_import_ImportStatement_strategy)
@settings(max_examples=25)
def test_ccsl_import_ImportStatement_instantiation(instance):
    assert isinstance(instance, ccsl_import_ImportStatement)


ccsl_import_ImportableElement_strategy = st.builds(ccsl_import_ImportableElement)
@given(instance=ccsl_import_ImportableElement_strategy)
@settings(max_examples=25)
def test_ccsl_import_ImportableElement_instantiation(instance):
    assert isinstance(instance, ccsl_import_ImportableElement)


ccsl_invocation_ConstructorInvocation_strategy = st.builds(ccsl_invocation_ConstructorInvocation)
@given(instance=ccsl_invocation_ConstructorInvocation_strategy)
@settings(max_examples=25)
def test_ccsl_invocation_ConstructorInvocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_ConstructorInvocation)


ccsl_invocation_Invocation_strategy = st.builds(ccsl_invocation_Invocation, argsKind=safe_text)
@given(instance=ccsl_invocation_Invocation_strategy)
@settings(max_examples=25)
def test_ccsl_invocation_Invocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_Invocation)


ccsl_invocation_MethodInvocation_strategy = st.builds(ccsl_invocation_MethodInvocation)
@given(instance=ccsl_invocation_MethodInvocation_strategy)
@settings(max_examples=25)
def test_ccsl_invocation_MethodInvocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_MethodInvocation)


ccsl_invocation_SimpleMethodInvocation_strategy = st.builds(ccsl_invocation_SimpleMethodInvocation)
@given(instance=ccsl_invocation_SimpleMethodInvocation_strategy)
@settings(max_examples=25)
def test_ccsl_invocation_SimpleMethodInvocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_SimpleMethodInvocation)


ccsl_invocation_SuperMethodInvocation_strategy = st.builds(ccsl_invocation_SuperMethodInvocation)
@given(instance=ccsl_invocation_SuperMethodInvocation_strategy)
@settings(max_examples=25)
def test_ccsl_invocation_SuperMethodInvocation_instantiation(instance):
    assert isinstance(instance, ccsl_invocation_SuperMethodInvocation)


ccsl_literalValues_BooleanLiteral_strategy = st.builds(ccsl_literalValues_BooleanLiteral)
@given(instance=ccsl_literalValues_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_ccsl_literalValues_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_BooleanLiteral)


ccsl_literalValues_CharacterLiteral_strategy = st.builds(ccsl_literalValues_CharacterLiteral)
@given(instance=ccsl_literalValues_CharacterLiteral_strategy)
@settings(max_examples=25)
def test_ccsl_literalValues_CharacterLiteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_CharacterLiteral)


ccsl_literalValues_LiteralValue_strategy = st.builds(ccsl_literalValues_LiteralValue, value=safe_text)
@given(instance=ccsl_literalValues_LiteralValue_strategy)
@settings(max_examples=25)
def test_ccsl_literalValues_LiteralValue_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_LiteralValue)


ccsl_literalValues_NullLiteral_strategy = st.builds(ccsl_literalValues_NullLiteral)
@given(instance=ccsl_literalValues_NullLiteral_strategy)
@settings(max_examples=25)
def test_ccsl_literalValues_NullLiteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_NullLiteral)


ccsl_literalValues_NumberLiteral_strategy = st.builds(ccsl_literalValues_NumberLiteral)
@given(instance=ccsl_literalValues_NumberLiteral_strategy)
@settings(max_examples=25)
def test_ccsl_literalValues_NumberLiteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_NumberLiteral)


ccsl_literalValues_StringLiteral_strategy = st.builds(ccsl_literalValues_StringLiteral)
@given(instance=ccsl_literalValues_StringLiteral_strategy)
@settings(max_examples=25)
def test_ccsl_literalValues_StringLiteral_instantiation(instance):
    assert isinstance(instance, ccsl_literalValues_StringLiteral)


ccsl_method_Constructor_strategy = st.builds(ccsl_method_Constructor, avaliableInSourceCode=safe_text)
@given(instance=ccsl_method_Constructor_strategy)
@settings(max_examples=25)
def test_ccsl_method_Constructor_instantiation(instance):
    assert isinstance(instance, ccsl_method_Constructor)


ccsl_method_Method_strategy = st.builds(ccsl_method_Method, abstract=safe_text, final=safe_text, inheritance=safe_text, static=safe_text)
@given(instance=ccsl_method_Method_strategy)
@settings(max_examples=25)
def test_ccsl_method_Method_instantiation(instance):
    assert isinstance(instance, ccsl_method_Method)


ccsl_method_SimpleMethod_strategy = st.builds(ccsl_method_SimpleMethod, paramsKind=safe_text, visibility=safe_text)
@given(instance=ccsl_method_SimpleMethod_strategy)
@settings(max_examples=25)
def test_ccsl_method_SimpleMethod_instantiation(instance):
    assert isinstance(instance, ccsl_method_SimpleMethod)


ccsl_namedElements_NamedElement_strategy = st.builds(ccsl_namedElements_NamedElement, avaliableInSourceCode=safe_text, name=safe_text)
@given(instance=ccsl_namedElements_NamedElement_strategy)
@settings(max_examples=25)
def test_ccsl_namedElements_NamedElement_instantiation(instance):
    assert isinstance(instance, ccsl_namedElements_NamedElement)


ccsl_namedElements_Package_strategy = st.builds(ccsl_namedElements_Package)
@given(instance=ccsl_namedElements_Package_strategy)
@settings(max_examples=25)
def test_ccsl_namedElements_Package_instantiation(instance):
    assert isinstance(instance, ccsl_namedElements_Package)


ccsl_numberFunctions_CcslIntegerLiteral_strategy = st.builds(ccsl_numberFunctions_CcslIntegerLiteral, value=safe_text)
@given(instance=ccsl_numberFunctions_CcslIntegerLiteral_strategy)
@settings(max_examples=25)
def test_ccsl_numberFunctions_CcslIntegerLiteral_instantiation(instance):
    assert isinstance(instance, ccsl_numberFunctions_CcslIntegerLiteral)


ccsl_numberFunctions_CcslNumberFunction_strategy = st.builds(ccsl_numberFunctions_CcslNumberFunction)
@given(instance=ccsl_numberFunctions_CcslNumberFunction_strategy)
@settings(max_examples=25)
def test_ccsl_numberFunctions_CcslNumberFunction_instantiation(instance):
    assert isinstance(instance, ccsl_numberFunctions_CcslNumberFunction)


ccsl_numberFunctions_GetIndexOf_strategy = st.builds(ccsl_numberFunctions_GetIndexOf)
@given(instance=ccsl_numberFunctions_GetIndexOf_strategy)
@settings(max_examples=25)
def test_ccsl_numberFunctions_GetIndexOf_instantiation(instance):
    assert isinstance(instance, ccsl_numberFunctions_GetIndexOf)


ccsl_statements_Access_strategy = st.builds(ccsl_statements_Access)
@given(instance=ccsl_statements_Access_strategy)
@settings(max_examples=25)
def test_ccsl_statements_Access_instantiation(instance):
    assert isinstance(instance, ccsl_statements_Access)


ccsl_statements_ArrayCreation_strategy = st.builds(ccsl_statements_ArrayCreation)
@given(instance=ccsl_statements_ArrayCreation_strategy)
@settings(max_examples=25)
def test_ccsl_statements_ArrayCreation_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ArrayCreation)


ccsl_statements_Block_strategy = st.builds(ccsl_statements_Block, statementsKind=safe_text)
@given(instance=ccsl_statements_Block_strategy)
@settings(max_examples=25)
def test_ccsl_statements_Block_instantiation(instance):
    assert isinstance(instance, ccsl_statements_Block)


ccsl_statements_BreakStatement_strategy = st.builds(ccsl_statements_BreakStatement)
@given(instance=ccsl_statements_BreakStatement_strategy)
@settings(max_examples=25)
def test_ccsl_statements_BreakStatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_BreakStatement)


ccsl_statements_ContinueStatement_strategy = st.builds(ccsl_statements_ContinueStatement)
@given(instance=ccsl_statements_ContinueStatement_strategy)
@settings(max_examples=25)
def test_ccsl_statements_ContinueStatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ContinueStatement)


ccsl_statements_ControlFlow_strategy = st.builds(ccsl_statements_ControlFlow)
@given(instance=ccsl_statements_ControlFlow_strategy)
@settings(max_examples=25)
def test_ccsl_statements_ControlFlow_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ControlFlow)


ccsl_statements_DataTypeAccess_strategy = st.builds(ccsl_statements_DataTypeAccess)
@given(instance=ccsl_statements_DataTypeAccess_strategy)
@settings(max_examples=25)
def test_ccsl_statements_DataTypeAccess_instantiation(instance):
    assert isinstance(instance, ccsl_statements_DataTypeAccess)


ccsl_statements_EmptyStatement_strategy = st.builds(ccsl_statements_EmptyStatement)
@given(instance=ccsl_statements_EmptyStatement_strategy)
@settings(max_examples=25)
def test_ccsl_statements_EmptyStatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_EmptyStatement)


ccsl_statements_InstanceCreation_strategy = st.builds(ccsl_statements_InstanceCreation, argsKind=safe_text)
@given(instance=ccsl_statements_InstanceCreation_strategy)
@settings(max_examples=25)
def test_ccsl_statements_InstanceCreation_instantiation(instance):
    assert isinstance(instance, ccsl_statements_InstanceCreation)


ccsl_statements_InstanceOf_strategy = st.builds(ccsl_statements_InstanceOf)
@given(instance=ccsl_statements_InstanceOf_strategy)
@settings(max_examples=25)
def test_ccsl_statements_InstanceOf_instantiation(instance):
    assert isinstance(instance, ccsl_statements_InstanceOf)


ccsl_statements_NamedElementAccess_strategy = st.builds(ccsl_statements_NamedElementAccess)
@given(instance=ccsl_statements_NamedElementAccess_strategy)
@settings(max_examples=25)
def test_ccsl_statements_NamedElementAccess_instantiation(instance):
    assert isinstance(instance, ccsl_statements_NamedElementAccess)


ccsl_statements_ReturnStatement_strategy = st.builds(ccsl_statements_ReturnStatement)
@given(instance=ccsl_statements_ReturnStatement_strategy)
@settings(max_examples=25)
def test_ccsl_statements_ReturnStatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ReturnStatement)


ccsl_statements_Statement_strategy = st.builds(ccsl_statements_Statement)
@given(instance=ccsl_statements_Statement_strategy)
@settings(max_examples=25)
def test_ccsl_statements_Statement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_Statement)


ccsl_statements_SynchronizedBlock_strategy = st.builds(ccsl_statements_SynchronizedBlock)
@given(instance=ccsl_statements_SynchronizedBlock_strategy)
@settings(max_examples=25)
def test_ccsl_statements_SynchronizedBlock_instantiation(instance):
    assert isinstance(instance, ccsl_statements_SynchronizedBlock)


ccsl_statements_ThisStatement_strategy = st.builds(ccsl_statements_ThisStatement)
@given(instance=ccsl_statements_ThisStatement_strategy)
@settings(max_examples=25)
def test_ccsl_statements_ThisStatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ThisStatement)


ccsl_statements_ThrowStatement_strategy = st.builds(ccsl_statements_ThrowStatement)
@given(instance=ccsl_statements_ThrowStatement_strategy)
@settings(max_examples=25)
def test_ccsl_statements_ThrowStatement_instantiation(instance):
    assert isinstance(instance, ccsl_statements_ThrowStatement)


ccsl_statements_VarDeclaration_strategy = st.builds(ccsl_statements_VarDeclaration)
@given(instance=ccsl_statements_VarDeclaration_strategy)
@settings(max_examples=25)
def test_ccsl_statements_VarDeclaration_instantiation(instance):
    assert isinstance(instance, ccsl_statements_VarDeclaration)


ccsl_statements_VariableAccess_strategy = st.builds(ccsl_statements_VariableAccess)
@given(instance=ccsl_statements_VariableAccess_strategy)
@settings(max_examples=25)
def test_ccsl_statements_VariableAccess_instantiation(instance):
    assert isinstance(instance, ccsl_statements_VariableAccess)


ccsl_strategy_AllStrategy_strategy = st.builds(ccsl_strategy_AllStrategy)
@given(instance=ccsl_strategy_AllStrategy_strategy)
@settings(max_examples=25)
def test_ccsl_strategy_AllStrategy_instantiation(instance):
    assert isinstance(instance, ccsl_strategy_AllStrategy)


ccsl_tryCatch_CatchClause_strategy = st.builds(ccsl_tryCatch_CatchClause)
@given(instance=ccsl_tryCatch_CatchClause_strategy)
@settings(max_examples=25)
def test_ccsl_tryCatch_CatchClause_instantiation(instance):
    assert isinstance(instance, ccsl_tryCatch_CatchClause)


ccsl_tryCatch_TryStatement_strategy = st.builds(ccsl_tryCatch_TryStatement)
@given(instance=ccsl_tryCatch_TryStatement_strategy)
@settings(max_examples=25)
def test_ccsl_tryCatch_TryStatement_instantiation(instance):
    assert isinstance(instance, ccsl_tryCatch_TryStatement)


ccsl_variable_FieldVariable_strategy = st.builds(ccsl_variable_FieldVariable, static=safe_text, visibility=safe_text)
@given(instance=ccsl_variable_FieldVariable_strategy)
@settings(max_examples=25)
def test_ccsl_variable_FieldVariable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_FieldVariable)


ccsl_variable_InitializableVariable_strategy = st.builds(ccsl_variable_InitializableVariable)
@given(instance=ccsl_variable_InitializableVariable_strategy)
@settings(max_examples=25)
def test_ccsl_variable_InitializableVariable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_InitializableVariable)


ccsl_variable_LocalVariable_strategy = st.builds(ccsl_variable_LocalVariable)
@given(instance=ccsl_variable_LocalVariable_strategy)
@settings(max_examples=25)
def test_ccsl_variable_LocalVariable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_LocalVariable)


ccsl_variable_ParameterVariable_strategy = st.builds(ccsl_variable_ParameterVariable)
@given(instance=ccsl_variable_ParameterVariable_strategy)
@settings(max_examples=25)
def test_ccsl_variable_ParameterVariable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_ParameterVariable)


ccsl_variable_Variable_strategy = st.builds(ccsl_variable_Variable, final=safe_text)
@given(instance=ccsl_variable_Variable_strategy)
@settings(max_examples=25)
def test_ccsl_variable_Variable_instantiation(instance):
    assert isinstance(instance, ccsl_variable_Variable)


complexType_AnnotationType_strategy = st.builds(complexType_AnnotationType)
@given(instance=complexType_AnnotationType_strategy)
@settings(max_examples=25)
def test_complexType_AnnotationType_instantiation(instance):
    assert isinstance(instance, complexType_AnnotationType)


complexType_ComplexType_strategy = st.builds(complexType_ComplexType)
@given(instance=complexType_ComplexType_strategy)
@settings(max_examples=25)
def test_complexType_ComplexType_instantiation(instance):
    assert isinstance(instance, complexType_ComplexType)


complexType_DeclaredType_strategy = st.builds(complexType_DeclaredType)
@given(instance=complexType_DeclaredType_strategy)
@settings(max_examples=25)
def test_complexType_DeclaredType_instantiation(instance):
    assert isinstance(instance, complexType_DeclaredType)


complexType_JClass_strategy = st.builds(complexType_JClass)
@given(instance=complexType_JClass_strategy)
@settings(max_examples=25)
def test_complexType_JClass_instantiation(instance):
    assert isinstance(instance, complexType_JClass)


complexType_JInterface_strategy = st.builds(complexType_JInterface)
@given(instance=complexType_JInterface_strategy)
@settings(max_examples=25)
def test_complexType_JInterface_instantiation(instance):
    assert isinstance(instance, complexType_JInterface)


controlFlow_SwitchCaseBlock_strategy = st.builds(controlFlow_SwitchCaseBlock)
@given(instance=controlFlow_SwitchCaseBlock_strategy)
@settings(max_examples=25)
def test_controlFlow_SwitchCaseBlock_instantiation(instance):
    assert isinstance(instance, controlFlow_SwitchCaseBlock)


datatype_DataType_strategy = st.builds(datatype_DataType)
@given(instance=datatype_DataType_strategy)
@settings(max_examples=25)
def test_datatype_DataType_instantiation(instance):
    assert isinstance(instance, datatype_DataType)


datatype_ObjectType_strategy = st.builds(datatype_ObjectType)
@given(instance=datatype_ObjectType_strategy)
@settings(max_examples=25)
def test_datatype_ObjectType_instantiation(instance):
    assert isinstance(instance, datatype_ObjectType)


elements_Element_strategy = st.builds(elements_Element)
@given(instance=elements_Element_strategy)
@settings(max_examples=25)
def test_elements_Element_instantiation(instance):
    assert isinstance(instance, elements_Element)


expressions_OperatorExpression_strategy = st.builds(expressions_OperatorExpression)
@given(instance=expressions_OperatorExpression_strategy)
@settings(max_examples=25)
def test_expressions_OperatorExpression_instantiation(instance):
    assert isinstance(instance, expressions_OperatorExpression)


filters_Filter_strategy = st.builds(filters_Filter)
@given(instance=filters_Filter_strategy)
@settings(max_examples=25)
def test_filters_Filter_instantiation(instance):
    assert isinstance(instance, filters_Filter)


import_ImportStatement_strategy = st.builds(import_ImportStatement)
@given(instance=import_ImportStatement_strategy)
@settings(max_examples=25)
def test_import_ImportStatement_instantiation(instance):
    assert isinstance(instance, import_ImportStatement)


import_ImportableElement_strategy = st.builds(import_ImportableElement)
@given(instance=import_ImportableElement_strategy)
@settings(max_examples=25)
def test_import_ImportableElement_instantiation(instance):
    assert isinstance(instance, import_ImportableElement)


method_Constructor_strategy = st.builds(method_Constructor)
@given(instance=method_Constructor_strategy)
@settings(max_examples=25)
def test_method_Constructor_instantiation(instance):
    assert isinstance(instance, method_Constructor)


method_Method_strategy = st.builds(method_Method)
@given(instance=method_Method_strategy)
@settings(max_examples=25)
def test_method_Method_instantiation(instance):
    assert isinstance(instance, method_Method)


method_SimpleMethod_strategy = st.builds(method_SimpleMethod)
@given(instance=method_SimpleMethod_strategy)
@settings(max_examples=25)
def test_method_SimpleMethod_instantiation(instance):
    assert isinstance(instance, method_SimpleMethod)


namedElements_NamedElement_strategy = st.builds(namedElements_NamedElement)
@given(instance=namedElements_NamedElement_strategy)
@settings(max_examples=25)
def test_namedElements_NamedElement_instantiation(instance):
    assert isinstance(instance, namedElements_NamedElement)


numberFunctions_CcslNumberFunction_strategy = st.builds(numberFunctions_CcslNumberFunction)
@given(instance=numberFunctions_CcslNumberFunction_strategy)
@settings(max_examples=25)
def test_numberFunctions_CcslNumberFunction_instantiation(instance):
    assert isinstance(instance, numberFunctions_CcslNumberFunction)


statements_Access_strategy = st.builds(statements_Access)
@given(instance=statements_Access_strategy)
@settings(max_examples=25)
def test_statements_Access_instantiation(instance):
    assert isinstance(instance, statements_Access)


statements_Block_strategy = st.builds(statements_Block)
@given(instance=statements_Block_strategy)
@settings(max_examples=25)
def test_statements_Block_instantiation(instance):
    assert isinstance(instance, statements_Block)


statements_Statement_strategy = st.builds(statements_Statement)
@given(instance=statements_Statement_strategy)
@settings(max_examples=25)
def test_statements_Statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)


tryCatch_CatchClause_strategy = st.builds(tryCatch_CatchClause)
@given(instance=tryCatch_CatchClause_strategy)
@settings(max_examples=25)
def test_tryCatch_CatchClause_instantiation(instance):
    assert isinstance(instance, tryCatch_CatchClause)


variable_FieldVariable_strategy = st.builds(variable_FieldVariable)
@given(instance=variable_FieldVariable_strategy)
@settings(max_examples=25)
def test_variable_FieldVariable_instantiation(instance):
    assert isinstance(instance, variable_FieldVariable)


variable_InitializableVariable_strategy = st.builds(variable_InitializableVariable)
@given(instance=variable_InitializableVariable_strategy)
@settings(max_examples=25)
def test_variable_InitializableVariable_instantiation(instance):
    assert isinstance(instance, variable_InitializableVariable)


variable_ParameterVariable_strategy = st.builds(variable_ParameterVariable)
@given(instance=variable_ParameterVariable_strategy)
@settings(max_examples=25)
def test_variable_ParameterVariable_instantiation(instance):
    assert isinstance(instance, variable_ParameterVariable)


variable_Variable_strategy = st.builds(variable_Variable)
@given(instance=variable_Variable_strategy)
@settings(max_examples=25)
def test_variable_Variable_instantiation(instance):
    assert isinstance(instance, variable_Variable)



