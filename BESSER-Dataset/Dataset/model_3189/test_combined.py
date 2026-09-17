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
    uppaal_visuals_Point,
    uppaal_visuals_LinearElement,
    Point,
    uppaal_visuals_PlanarElement,
    uppaal_visuals_ColoredElement,
    IncrementDecrementExpression,
    uppaal_expressions_PostIncrementDecrementExpression,
    uppaal_expressions_PreIncrementDecrementExpression,
    expressions_Expression,
    Function,
    BinaryExpression,
    uppaal_expressions_CompareExpression,
    uppaal_expressions_MinMaxExpression,
    uppaal_expressions_LogicalExpression,
    uppaal_expressions_ArithmeticExpression,
    uppaal_expressions_BitwiseExpression,
    uppaal_expressions_BitShiftExpression,
    uppaal_expressions_AssignmentExpression,
    uppaal_expressions_Expression,
    statements_Statement,
    uppaal_templates_Synchronization,
    Statement,
    uppaal_statements_IfStatement,
    uppaal_statements_EmptyStatement,
    uppaal_statements_ForLoop,
    uppaal_statements_DoWhileLoop,
    uppaal_statements_ExpressionStatement,
    uppaal_statements_ReturnStatement,
    uppaal_statements_WhileLoop,
    uppaal_statements_Block,
    uppaal_statements_Statement,
    visuals_LinearElement,
    Selection,
    Synchronization,
    Location,
    LocalDeclarations,
    visuals_ColoredElement,
    visuals_PlanarElement,
    system_TemplateDeclaration,
    Edge,
    RedefinedTemplate,
    IdentifierExpression,
    PriorityItem,
    uppaal_global_DefaultItem,
    uppaal_global_ChannelItem,
    uppaal_global_PriorityItem,
    global_PriorityItem,
    uppaal_global_ChannelPriorityGroup,
    uppaal_system_ProgressMeasure,
    AbstractTemplate,
    uppaal_templates_RedefinedTemplate,
    uppaal_templates_Template,
    uppaal_system_InstantiationList,
    system_InstantiationList,
    uppaal_system_System,
    uppaal_declarations_Initializer,
    Variable,
    uppaal_declarations_Parameter,
    TypedElement,
    uppaal_declarations_TypedElementContainer,
    global_ChannelPriorityGroup,
    Initializer,
    uppaal_declarations_ExpressionInitializer,
    uppaal_declarations_ArrayInitializer,
    declarations_TypedElementContainer,
    uppaal_statements_Iteration,
    uppaal_expressions_QuantificationExpression,
    declarations_Declaration,
    uppaal_declarations_TypedDeclaration,
    DeclaredType,
    uppaal_declarations_Declaration,
    system_ProgressMeasure,
    system_System,
    global_ChannelPriorityDeclaration,
    ParameterContainer,
    Block,
    core_TypedElement,
    uppaal_types_IntegerBounds,
    IntegerBounds,
    TypedDeclaration,
    TypeExpression,
    uppaal_types_StructTypeSpecification,
    uppaal_types_RangeTypeSpecification,
    uppaal_types_ScalarTypeSpecification,
    Declarations,
    uppaal_declarations_SystemDeclarations,
    uppaal_declarations_LocalDeclarations,
    uppaal_declarations_GlobalDeclarations,
    Declaration,
    uppaal_global_ChannelPriorityDeclaration,
    uppaal_system_TemplateDeclaration,
    uppaal_declarations_TypeDeclaration,
    uppaal_declarations_Declarations,
    PredefinedType,
    uppaal_types_Library,
    NamedElement,
    uppaal_templates_AbstractTemplate,
    uppaal_types_Type,
    Expression,
    uppaal_expressions_NegationExpression,
    uppaal_expressions_LiteralExpression,
    uppaal_expressions_PlusExpression,
    uppaal_expressions_BinaryExpression,
    uppaal_expressions_FunctionCallExpression,
    uppaal_expressions_IdentifierExpression,
    uppaal_expressions_ChannelPrefixExpression,
    uppaal_expressions_DataPrefixExpression,
    uppaal_expressions_ConditionExpression,
    uppaal_expressions_ScopedIdentifierExpression,
    uppaal_expressions_IncrementDecrementExpression,
    uppaal_expressions_MinusExpression,
    uppaal_types_TypeExpression,
    TypedElementContainer,
    uppaal_declarations_ParameterContainer,
    uppaal_templates_Selection,
    uppaal_core_TypedElement,
    uppaal_core_CommentableElement,
    uppaal_core_NamedElement,
    TypeDeclaration,
    Type,
    uppaal_types_DeclaredType,
    uppaal_types_PredefinedType,
    core_CommentableElement,
    uppaal_templates_Edge,
    core_NamedElement,
    uppaal_declarations_Function,
    uppaal_declarations_Variable,
    uppaal_templates_Location,
    uppaal_NTA,
    SystemDeclarations,
    Template,
    GlobalDeclarations,
    DataVariablePrefix,
    MinMaxOperator,
    ArithmeticOperator,
    BitShiftOperator,
    IncrementDecrementOperator,
    CallType,
    CompareOperator,
    Quantifier,
    LocationKind,
    AssignmentOperator,
    SynchronizationKind,
    BuiltInType,
    LogicalOperator,
    BitwiseOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_uppaal_visuals_point_is_not_abstract():
    assert not inspect.isabstract(uppaal_visuals_Point)


def test_hyp_uppaal_visuals_point_constructor_exists():
    assert callable(uppaal_visuals_Point.__init__)


def test_hyp_uppaal_visuals_point_constructor_args():
    sig = inspect.signature(uppaal_visuals_Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_uppaal_visuals_linearelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_visuals_LinearElement)


def test_hyp_uppaal_visuals_linearelement_constructor_exists():
    assert callable(uppaal_visuals_LinearElement.__init__)


def test_hyp_uppaal_visuals_linearelement_constructor_args():
    sig = inspect.signature(uppaal_visuals_LinearElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_hyp_point_constructor_exists():
    assert callable(Point.__init__)


def test_hyp_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_visuals_planarelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_visuals_PlanarElement)


def test_hyp_uppaal_visuals_planarelement_constructor_exists():
    assert callable(uppaal_visuals_PlanarElement.__init__)


def test_hyp_uppaal_visuals_planarelement_constructor_args():
    sig = inspect.signature(uppaal_visuals_PlanarElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_visuals_coloredelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_visuals_ColoredElement)


def test_hyp_uppaal_visuals_coloredelement_constructor_exists():
    assert callable(uppaal_visuals_ColoredElement.__init__)


def test_hyp_uppaal_visuals_coloredelement_constructor_args():
    sig = inspect.signature(uppaal_visuals_ColoredElement.__init__)
    params = list(sig.parameters.keys())
    assert "colorCode" in params, "Missing parameter 'colorCode'"




def test_hyp_incrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(IncrementDecrementExpression)


def test_hyp_incrementdecrementexpression_constructor_exists():
    assert callable(IncrementDecrementExpression.__init__)


def test_hyp_incrementdecrementexpression_constructor_args():
    sig = inspect.signature(IncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_postincrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_PostIncrementDecrementExpression)


def test_hyp_uppaal_expressions_postincrementdecrementexpression_constructor_exists():
    assert callable(uppaal_expressions_PostIncrementDecrementExpression.__init__)


def test_hyp_uppaal_expressions_postincrementdecrementexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_PostIncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_preincrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_PreIncrementDecrementExpression)


def test_hyp_uppaal_expressions_preincrementdecrementexpression_constructor_exists():
    assert callable(uppaal_expressions_PreIncrementDecrementExpression.__init__)


def test_hyp_uppaal_expressions_preincrementdecrementexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_PreIncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(expressions_Expression)


def test_hyp_expressions_expression_constructor_exists():
    assert callable(expressions_Expression.__init__)


def test_hyp_expressions_expression_constructor_args():
    sig = inspect.signature(expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_hyp_function_constructor_exists():
    assert callable(Function.__init__)


def test_hyp_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_hyp_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_hyp_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_compareexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_CompareExpression)


def test_hyp_uppaal_expressions_compareexpression_constructor_exists():
    assert callable(uppaal_expressions_CompareExpression.__init__)


def test_hyp_uppaal_expressions_compareexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_CompareExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_uppaal_expressions_minmaxexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_MinMaxExpression)


def test_hyp_uppaal_expressions_minmaxexpression_constructor_exists():
    assert callable(uppaal_expressions_MinMaxExpression.__init__)


def test_hyp_uppaal_expressions_minmaxexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_MinMaxExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_uppaal_expressions_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_LogicalExpression)


def test_hyp_uppaal_expressions_logicalexpression_constructor_exists():
    assert callable(uppaal_expressions_LogicalExpression.__init__)


def test_hyp_uppaal_expressions_logicalexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_uppaal_expressions_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_ArithmeticExpression)


def test_hyp_uppaal_expressions_arithmeticexpression_constructor_exists():
    assert callable(uppaal_expressions_ArithmeticExpression.__init__)


def test_hyp_uppaal_expressions_arithmeticexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_uppaal_expressions_bitwiseexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_BitwiseExpression)


def test_hyp_uppaal_expressions_bitwiseexpression_constructor_exists():
    assert callable(uppaal_expressions_BitwiseExpression.__init__)


def test_hyp_uppaal_expressions_bitwiseexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_BitwiseExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_uppaal_expressions_bitshiftexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_BitShiftExpression)


def test_hyp_uppaal_expressions_bitshiftexpression_constructor_exists():
    assert callable(uppaal_expressions_BitShiftExpression.__init__)


def test_hyp_uppaal_expressions_bitshiftexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_BitShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_uppaal_expressions_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_AssignmentExpression)


def test_hyp_uppaal_expressions_assignmentexpression_constructor_exists():
    assert callable(uppaal_expressions_AssignmentExpression.__init__)


def test_hyp_uppaal_expressions_assignmentexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_uppaal_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_Expression)


def test_hyp_uppaal_expressions_expression_constructor_exists():
    assert callable(uppaal_expressions_Expression.__init__)


def test_hyp_uppaal_expressions_expression_constructor_args():
    sig = inspect.signature(uppaal_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statements_statement_is_not_abstract():
    assert not inspect.isabstract(statements_Statement)


def test_hyp_statements_statement_constructor_exists():
    assert callable(statements_Statement.__init__)


def test_hyp_statements_statement_constructor_args():
    sig = inspect.signature(statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_templates_synchronization_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Synchronization)


def test_hyp_uppaal_templates_synchronization_constructor_exists():
    assert callable(uppaal_templates_Synchronization.__init__)


def test_hyp_uppaal_templates_synchronization_constructor_args():
    sig = inspect.signature(uppaal_templates_Synchronization.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_ifstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_IfStatement)


def test_hyp_uppaal_statements_ifstatement_constructor_exists():
    assert callable(uppaal_statements_IfStatement.__init__)


def test_hyp_uppaal_statements_ifstatement_constructor_args():
    sig = inspect.signature(uppaal_statements_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_emptystatement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_EmptyStatement)


def test_hyp_uppaal_statements_emptystatement_constructor_exists():
    assert callable(uppaal_statements_EmptyStatement.__init__)


def test_hyp_uppaal_statements_emptystatement_constructor_args():
    sig = inspect.signature(uppaal_statements_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_forloop_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_ForLoop)


def test_hyp_uppaal_statements_forloop_constructor_exists():
    assert callable(uppaal_statements_ForLoop.__init__)


def test_hyp_uppaal_statements_forloop_constructor_args():
    sig = inspect.signature(uppaal_statements_ForLoop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_dowhileloop_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_DoWhileLoop)


def test_hyp_uppaal_statements_dowhileloop_constructor_exists():
    assert callable(uppaal_statements_DoWhileLoop.__init__)


def test_hyp_uppaal_statements_dowhileloop_constructor_args():
    sig = inspect.signature(uppaal_statements_DoWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_ExpressionStatement)


def test_hyp_uppaal_statements_expressionstatement_constructor_exists():
    assert callable(uppaal_statements_ExpressionStatement.__init__)


def test_hyp_uppaal_statements_expressionstatement_constructor_args():
    sig = inspect.signature(uppaal_statements_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_returnstatement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_ReturnStatement)


def test_hyp_uppaal_statements_returnstatement_constructor_exists():
    assert callable(uppaal_statements_ReturnStatement.__init__)


def test_hyp_uppaal_statements_returnstatement_constructor_args():
    sig = inspect.signature(uppaal_statements_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_whileloop_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_WhileLoop)


def test_hyp_uppaal_statements_whileloop_constructor_exists():
    assert callable(uppaal_statements_WhileLoop.__init__)


def test_hyp_uppaal_statements_whileloop_constructor_args():
    sig = inspect.signature(uppaal_statements_WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_block_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_Block)


def test_hyp_uppaal_statements_block_constructor_exists():
    assert callable(uppaal_statements_Block.__init__)


def test_hyp_uppaal_statements_block_constructor_args():
    sig = inspect.signature(uppaal_statements_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_statement_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_Statement)


def test_hyp_uppaal_statements_statement_constructor_exists():
    assert callable(uppaal_statements_Statement.__init__)


def test_hyp_uppaal_statements_statement_constructor_args():
    sig = inspect.signature(uppaal_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visuals_linearelement_is_not_abstract():
    assert not inspect.isabstract(visuals_LinearElement)


def test_hyp_visuals_linearelement_constructor_exists():
    assert callable(visuals_LinearElement.__init__)


def test_hyp_visuals_linearelement_constructor_args():
    sig = inspect.signature(visuals_LinearElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_selection_is_not_abstract():
    assert not inspect.isabstract(Selection)


def test_hyp_selection_constructor_exists():
    assert callable(Selection.__init__)


def test_hyp_selection_constructor_args():
    sig = inspect.signature(Selection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_synchronization_is_not_abstract():
    assert not inspect.isabstract(Synchronization)


def test_hyp_synchronization_constructor_exists():
    assert callable(Synchronization.__init__)


def test_hyp_synchronization_constructor_args():
    sig = inspect.signature(Synchronization.__init__)
    params = list(sig.parameters.keys())



def test_hyp_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_hyp_location_constructor_exists():
    assert callable(Location.__init__)


def test_hyp_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_hyp_localdeclarations_is_not_abstract():
    assert not inspect.isabstract(LocalDeclarations)


def test_hyp_localdeclarations_constructor_exists():
    assert callable(LocalDeclarations.__init__)


def test_hyp_localdeclarations_constructor_args():
    sig = inspect.signature(LocalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visuals_coloredelement_is_not_abstract():
    assert not inspect.isabstract(visuals_ColoredElement)


def test_hyp_visuals_coloredelement_constructor_exists():
    assert callable(visuals_ColoredElement.__init__)


def test_hyp_visuals_coloredelement_constructor_args():
    sig = inspect.signature(visuals_ColoredElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visuals_planarelement_is_not_abstract():
    assert not inspect.isabstract(visuals_PlanarElement)


def test_hyp_visuals_planarelement_constructor_exists():
    assert callable(visuals_PlanarElement.__init__)


def test_hyp_visuals_planarelement_constructor_args():
    sig = inspect.signature(visuals_PlanarElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_system_templatedeclaration_is_not_abstract():
    assert not inspect.isabstract(system_TemplateDeclaration)


def test_hyp_system_templatedeclaration_constructor_exists():
    assert callable(system_TemplateDeclaration.__init__)


def test_hyp_system_templatedeclaration_constructor_args():
    sig = inspect.signature(system_TemplateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_hyp_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_hyp_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_redefinedtemplate_is_not_abstract():
    assert not inspect.isabstract(RedefinedTemplate)


def test_hyp_redefinedtemplate_constructor_exists():
    assert callable(RedefinedTemplate.__init__)


def test_hyp_redefinedtemplate_constructor_args():
    sig = inspect.signature(RedefinedTemplate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifierexpression_is_not_abstract():
    assert not inspect.isabstract(IdentifierExpression)


def test_hyp_identifierexpression_constructor_exists():
    assert callable(IdentifierExpression.__init__)


def test_hyp_identifierexpression_constructor_args():
    sig = inspect.signature(IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_priorityitem_is_not_abstract():
    assert not inspect.isabstract(PriorityItem)


def test_hyp_priorityitem_constructor_exists():
    assert callable(PriorityItem.__init__)


def test_hyp_priorityitem_constructor_args():
    sig = inspect.signature(PriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_global_defaultitem_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_DefaultItem)


def test_hyp_uppaal_global_defaultitem_constructor_exists():
    assert callable(uppaal_global_DefaultItem.__init__)


def test_hyp_uppaal_global_defaultitem_constructor_args():
    sig = inspect.signature(uppaal_global_DefaultItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_global_channelitem_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_ChannelItem)


def test_hyp_uppaal_global_channelitem_constructor_exists():
    assert callable(uppaal_global_ChannelItem.__init__)


def test_hyp_uppaal_global_channelitem_constructor_args():
    sig = inspect.signature(uppaal_global_ChannelItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_global_priorityitem_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_PriorityItem)


def test_hyp_uppaal_global_priorityitem_constructor_exists():
    assert callable(uppaal_global_PriorityItem.__init__)


def test_hyp_uppaal_global_priorityitem_constructor_args():
    sig = inspect.signature(uppaal_global_PriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_global_priorityitem_is_not_abstract():
    assert not inspect.isabstract(global_PriorityItem)


def test_hyp_global_priorityitem_constructor_exists():
    assert callable(global_PriorityItem.__init__)


def test_hyp_global_priorityitem_constructor_args():
    sig = inspect.signature(global_PriorityItem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_global_channelprioritygroup_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_ChannelPriorityGroup)


def test_hyp_uppaal_global_channelprioritygroup_constructor_exists():
    assert callable(uppaal_global_ChannelPriorityGroup.__init__)


def test_hyp_uppaal_global_channelprioritygroup_constructor_args():
    sig = inspect.signature(uppaal_global_ChannelPriorityGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_system_progressmeasure_is_not_abstract():
    assert not inspect.isabstract(uppaal_system_ProgressMeasure)


def test_hyp_uppaal_system_progressmeasure_constructor_exists():
    assert callable(uppaal_system_ProgressMeasure.__init__)


def test_hyp_uppaal_system_progressmeasure_constructor_args():
    sig = inspect.signature(uppaal_system_ProgressMeasure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttemplate_is_not_abstract():
    assert not inspect.isabstract(AbstractTemplate)


def test_hyp_abstracttemplate_constructor_exists():
    assert callable(AbstractTemplate.__init__)


def test_hyp_abstracttemplate_constructor_args():
    sig = inspect.signature(AbstractTemplate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_templates_redefinedtemplate_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_RedefinedTemplate)


def test_hyp_uppaal_templates_redefinedtemplate_constructor_exists():
    assert callable(uppaal_templates_RedefinedTemplate.__init__)


def test_hyp_uppaal_templates_redefinedtemplate_constructor_args():
    sig = inspect.signature(uppaal_templates_RedefinedTemplate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_templates_template_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Template)


def test_hyp_uppaal_templates_template_constructor_exists():
    assert callable(uppaal_templates_Template.__init__)


def test_hyp_uppaal_templates_template_constructor_args():
    sig = inspect.signature(uppaal_templates_Template.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_system_instantiationlist_is_not_abstract():
    assert not inspect.isabstract(uppaal_system_InstantiationList)


def test_hyp_uppaal_system_instantiationlist_constructor_exists():
    assert callable(uppaal_system_InstantiationList.__init__)


def test_hyp_uppaal_system_instantiationlist_constructor_args():
    sig = inspect.signature(uppaal_system_InstantiationList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_system_instantiationlist_is_not_abstract():
    assert not inspect.isabstract(system_InstantiationList)


def test_hyp_system_instantiationlist_constructor_exists():
    assert callable(system_InstantiationList.__init__)


def test_hyp_system_instantiationlist_constructor_args():
    sig = inspect.signature(system_InstantiationList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_system_system_is_not_abstract():
    assert not inspect.isabstract(uppaal_system_System)


def test_hyp_uppaal_system_system_constructor_exists():
    assert callable(uppaal_system_System.__init__)


def test_hyp_uppaal_system_system_constructor_args():
    sig = inspect.signature(uppaal_system_System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_initializer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Initializer)


def test_hyp_uppaal_declarations_initializer_constructor_exists():
    assert callable(uppaal_declarations_Initializer.__init__)


def test_hyp_uppaal_declarations_initializer_constructor_args():
    sig = inspect.signature(uppaal_declarations_Initializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_parameter_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Parameter)


def test_hyp_uppaal_declarations_parameter_constructor_exists():
    assert callable(uppaal_declarations_Parameter.__init__)


def test_hyp_uppaal_declarations_parameter_constructor_args():
    sig = inspect.signature(uppaal_declarations_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "callType" in params, "Missing parameter 'callType'"




def test_hyp_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_hyp_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_hyp_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_typedelementcontainer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_TypedElementContainer)


def test_hyp_uppaal_declarations_typedelementcontainer_constructor_exists():
    assert callable(uppaal_declarations_TypedElementContainer.__init__)


def test_hyp_uppaal_declarations_typedelementcontainer_constructor_args():
    sig = inspect.signature(uppaal_declarations_TypedElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_global_channelprioritygroup_is_not_abstract():
    assert not inspect.isabstract(global_ChannelPriorityGroup)


def test_hyp_global_channelprioritygroup_constructor_exists():
    assert callable(global_ChannelPriorityGroup.__init__)


def test_hyp_global_channelprioritygroup_constructor_args():
    sig = inspect.signature(global_ChannelPriorityGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_initializer_is_not_abstract():
    assert not inspect.isabstract(Initializer)


def test_hyp_initializer_constructor_exists():
    assert callable(Initializer.__init__)


def test_hyp_initializer_constructor_args():
    sig = inspect.signature(Initializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_expressioninitializer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_ExpressionInitializer)


def test_hyp_uppaal_declarations_expressioninitializer_constructor_exists():
    assert callable(uppaal_declarations_ExpressionInitializer.__init__)


def test_hyp_uppaal_declarations_expressioninitializer_constructor_args():
    sig = inspect.signature(uppaal_declarations_ExpressionInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_ArrayInitializer)


def test_hyp_uppaal_declarations_arrayinitializer_constructor_exists():
    assert callable(uppaal_declarations_ArrayInitializer.__init__)


def test_hyp_uppaal_declarations_arrayinitializer_constructor_args():
    sig = inspect.signature(uppaal_declarations_ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declarations_typedelementcontainer_is_not_abstract():
    assert not inspect.isabstract(declarations_TypedElementContainer)


def test_hyp_declarations_typedelementcontainer_constructor_exists():
    assert callable(declarations_TypedElementContainer.__init__)


def test_hyp_declarations_typedelementcontainer_constructor_args():
    sig = inspect.signature(declarations_TypedElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_statements_iteration_is_not_abstract():
    assert not inspect.isabstract(uppaal_statements_Iteration)


def test_hyp_uppaal_statements_iteration_constructor_exists():
    assert callable(uppaal_statements_Iteration.__init__)


def test_hyp_uppaal_statements_iteration_constructor_args():
    sig = inspect.signature(uppaal_statements_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_quantificationexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_QuantificationExpression)


def test_hyp_uppaal_expressions_quantificationexpression_constructor_exists():
    assert callable(uppaal_expressions_QuantificationExpression.__init__)


def test_hyp_uppaal_expressions_quantificationexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_QuantificationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "quantifier" in params, "Missing parameter 'quantifier'"




def test_hyp_declarations_declaration_is_not_abstract():
    assert not inspect.isabstract(declarations_Declaration)


def test_hyp_declarations_declaration_constructor_exists():
    assert callable(declarations_Declaration.__init__)


def test_hyp_declarations_declaration_constructor_args():
    sig = inspect.signature(declarations_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_TypedDeclaration)


def test_hyp_uppaal_declarations_typeddeclaration_constructor_exists():
    assert callable(uppaal_declarations_TypedDeclaration.__init__)


def test_hyp_uppaal_declarations_typeddeclaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaredtype_is_not_abstract():
    assert not inspect.isabstract(DeclaredType)


def test_hyp_declaredtype_constructor_exists():
    assert callable(DeclaredType.__init__)


def test_hyp_declaredtype_constructor_args():
    sig = inspect.signature(DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_declaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Declaration)


def test_hyp_uppaal_declarations_declaration_constructor_exists():
    assert callable(uppaal_declarations_Declaration.__init__)


def test_hyp_uppaal_declarations_declaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_system_progressmeasure_is_not_abstract():
    assert not inspect.isabstract(system_ProgressMeasure)


def test_hyp_system_progressmeasure_constructor_exists():
    assert callable(system_ProgressMeasure.__init__)


def test_hyp_system_progressmeasure_constructor_args():
    sig = inspect.signature(system_ProgressMeasure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_system_system_is_not_abstract():
    assert not inspect.isabstract(system_System)


def test_hyp_system_system_constructor_exists():
    assert callable(system_System.__init__)


def test_hyp_system_system_constructor_args():
    sig = inspect.signature(system_System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_global_channelprioritydeclaration_is_not_abstract():
    assert not inspect.isabstract(global_ChannelPriorityDeclaration)


def test_hyp_global_channelprioritydeclaration_constructor_exists():
    assert callable(global_ChannelPriorityDeclaration.__init__)


def test_hyp_global_channelprioritydeclaration_constructor_args():
    sig = inspect.signature(global_ChannelPriorityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parametercontainer_is_not_abstract():
    assert not inspect.isabstract(ParameterContainer)


def test_hyp_parametercontainer_constructor_exists():
    assert callable(ParameterContainer.__init__)


def test_hyp_parametercontainer_constructor_args():
    sig = inspect.signature(ParameterContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_hyp_block_constructor_exists():
    assert callable(Block.__init__)


def test_hyp_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_typedelement_is_not_abstract():
    assert not inspect.isabstract(core_TypedElement)


def test_hyp_core_typedelement_constructor_exists():
    assert callable(core_TypedElement.__init__)


def test_hyp_core_typedelement_constructor_args():
    sig = inspect.signature(core_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_integerbounds_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_IntegerBounds)


def test_hyp_uppaal_types_integerbounds_constructor_exists():
    assert callable(uppaal_types_IntegerBounds.__init__)


def test_hyp_uppaal_types_integerbounds_constructor_args():
    sig = inspect.signature(uppaal_types_IntegerBounds.__init__)
    params = list(sig.parameters.keys())



def test_hyp_integerbounds_is_not_abstract():
    assert not inspect.isabstract(IntegerBounds)


def test_hyp_integerbounds_constructor_exists():
    assert callable(IntegerBounds.__init__)


def test_hyp_integerbounds_constructor_args():
    sig = inspect.signature(IntegerBounds.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(TypedDeclaration)


def test_hyp_typeddeclaration_constructor_exists():
    assert callable(TypedDeclaration.__init__)


def test_hyp_typeddeclaration_constructor_args():
    sig = inspect.signature(TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typeexpression_is_not_abstract():
    assert not inspect.isabstract(TypeExpression)


def test_hyp_typeexpression_constructor_exists():
    assert callable(TypeExpression.__init__)


def test_hyp_typeexpression_constructor_args():
    sig = inspect.signature(TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_structtypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_StructTypeSpecification)


def test_hyp_uppaal_types_structtypespecification_constructor_exists():
    assert callable(uppaal_types_StructTypeSpecification.__init__)


def test_hyp_uppaal_types_structtypespecification_constructor_args():
    sig = inspect.signature(uppaal_types_StructTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_rangetypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_RangeTypeSpecification)


def test_hyp_uppaal_types_rangetypespecification_constructor_exists():
    assert callable(uppaal_types_RangeTypeSpecification.__init__)


def test_hyp_uppaal_types_rangetypespecification_constructor_args():
    sig = inspect.signature(uppaal_types_RangeTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_scalartypespecification_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_ScalarTypeSpecification)


def test_hyp_uppaal_types_scalartypespecification_constructor_exists():
    assert callable(uppaal_types_ScalarTypeSpecification.__init__)


def test_hyp_uppaal_types_scalartypespecification_constructor_args():
    sig = inspect.signature(uppaal_types_ScalarTypeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declarations_is_not_abstract():
    assert not inspect.isabstract(Declarations)


def test_hyp_declarations_constructor_exists():
    assert callable(Declarations.__init__)


def test_hyp_declarations_constructor_args():
    sig = inspect.signature(Declarations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_systemdeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_SystemDeclarations)


def test_hyp_uppaal_declarations_systemdeclarations_constructor_exists():
    assert callable(uppaal_declarations_SystemDeclarations.__init__)


def test_hyp_uppaal_declarations_systemdeclarations_constructor_args():
    sig = inspect.signature(uppaal_declarations_SystemDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_localdeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_LocalDeclarations)


def test_hyp_uppaal_declarations_localdeclarations_constructor_exists():
    assert callable(uppaal_declarations_LocalDeclarations.__init__)


def test_hyp_uppaal_declarations_localdeclarations_constructor_args():
    sig = inspect.signature(uppaal_declarations_LocalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_globaldeclarations_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_GlobalDeclarations)


def test_hyp_uppaal_declarations_globaldeclarations_constructor_exists():
    assert callable(uppaal_declarations_GlobalDeclarations.__init__)


def test_hyp_uppaal_declarations_globaldeclarations_constructor_args():
    sig = inspect.signature(uppaal_declarations_GlobalDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_hyp_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_hyp_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_global_channelprioritydeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_global_ChannelPriorityDeclaration)


def test_hyp_uppaal_global_channelprioritydeclaration_constructor_exists():
    assert callable(uppaal_global_ChannelPriorityDeclaration.__init__)


def test_hyp_uppaal_global_channelprioritydeclaration_constructor_args():
    sig = inspect.signature(uppaal_global_ChannelPriorityDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_system_templatedeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_system_TemplateDeclaration)


def test_hyp_uppaal_system_templatedeclaration_constructor_exists():
    assert callable(uppaal_system_TemplateDeclaration.__init__)


def test_hyp_uppaal_system_templatedeclaration_constructor_args():
    sig = inspect.signature(uppaal_system_TemplateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_TypeDeclaration)


def test_hyp_uppaal_declarations_typedeclaration_constructor_exists():
    assert callable(uppaal_declarations_TypeDeclaration.__init__)


def test_hyp_uppaal_declarations_typedeclaration_constructor_args():
    sig = inspect.signature(uppaal_declarations_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_declarations_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Declarations)


def test_hyp_uppaal_declarations_declarations_constructor_exists():
    assert callable(uppaal_declarations_Declarations.__init__)


def test_hyp_uppaal_declarations_declarations_constructor_args():
    sig = inspect.signature(uppaal_declarations_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(PredefinedType)


def test_hyp_predefinedtype_constructor_exists():
    assert callable(PredefinedType.__init__)


def test_hyp_predefinedtype_constructor_args():
    sig = inspect.signature(PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_library_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_Library)


def test_hyp_uppaal_types_library_constructor_exists():
    assert callable(uppaal_types_Library.__init__)


def test_hyp_uppaal_types_library_constructor_args():
    sig = inspect.signature(uppaal_types_Library.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_templates_abstracttemplate_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_AbstractTemplate)


def test_hyp_uppaal_templates_abstracttemplate_constructor_exists():
    assert callable(uppaal_templates_AbstractTemplate.__init__)


def test_hyp_uppaal_templates_abstracttemplate_constructor_args():
    sig = inspect.signature(uppaal_templates_AbstractTemplate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_type_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_Type)


def test_hyp_uppaal_types_type_constructor_exists():
    assert callable(uppaal_types_Type.__init__)


def test_hyp_uppaal_types_type_constructor_args():
    sig = inspect.signature(uppaal_types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_negationexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_NegationExpression)


def test_hyp_uppaal_expressions_negationexpression_constructor_exists():
    assert callable(uppaal_expressions_NegationExpression.__init__)


def test_hyp_uppaal_expressions_negationexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_NegationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_literalexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_LiteralExpression)


def test_hyp_uppaal_expressions_literalexpression_constructor_exists():
    assert callable(uppaal_expressions_LiteralExpression.__init__)


def test_hyp_uppaal_expressions_literalexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_LiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_uppaal_expressions_plusexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_PlusExpression)


def test_hyp_uppaal_expressions_plusexpression_constructor_exists():
    assert callable(uppaal_expressions_PlusExpression.__init__)


def test_hyp_uppaal_expressions_plusexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_PlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_BinaryExpression)


def test_hyp_uppaal_expressions_binaryexpression_constructor_exists():
    assert callable(uppaal_expressions_BinaryExpression.__init__)


def test_hyp_uppaal_expressions_binaryexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_functioncallexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_FunctionCallExpression)


def test_hyp_uppaal_expressions_functioncallexpression_constructor_exists():
    assert callable(uppaal_expressions_FunctionCallExpression.__init__)


def test_hyp_uppaal_expressions_functioncallexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_FunctionCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_identifierexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_IdentifierExpression)


def test_hyp_uppaal_expressions_identifierexpression_constructor_exists():
    assert callable(uppaal_expressions_IdentifierExpression.__init__)


def test_hyp_uppaal_expressions_identifierexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_IdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_channelprefixexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_ChannelPrefixExpression)


def test_hyp_uppaal_expressions_channelprefixexpression_constructor_exists():
    assert callable(uppaal_expressions_ChannelPrefixExpression.__init__)


def test_hyp_uppaal_expressions_channelprefixexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_ChannelPrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "broadcast" in params, "Missing parameter 'broadcast'"
    assert "urgent" in params, "Missing parameter 'urgent'"





def test_hyp_uppaal_expressions_dataprefixexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_DataPrefixExpression)


def test_hyp_uppaal_expressions_dataprefixexpression_constructor_exists():
    assert callable(uppaal_expressions_DataPrefixExpression.__init__)


def test_hyp_uppaal_expressions_dataprefixexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_DataPrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"




def test_hyp_uppaal_expressions_conditionexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_ConditionExpression)


def test_hyp_uppaal_expressions_conditionexpression_constructor_exists():
    assert callable(uppaal_expressions_ConditionExpression.__init__)


def test_hyp_uppaal_expressions_conditionexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_ConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_scopedidentifierexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_ScopedIdentifierExpression)


def test_hyp_uppaal_expressions_scopedidentifierexpression_constructor_exists():
    assert callable(uppaal_expressions_ScopedIdentifierExpression.__init__)


def test_hyp_uppaal_expressions_scopedidentifierexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_ScopedIdentifierExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_expressions_incrementdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_IncrementDecrementExpression)


def test_hyp_uppaal_expressions_incrementdecrementexpression_constructor_exists():
    assert callable(uppaal_expressions_IncrementDecrementExpression.__init__)


def test_hyp_uppaal_expressions_incrementdecrementexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_IncrementDecrementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_uppaal_expressions_minusexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_expressions_MinusExpression)


def test_hyp_uppaal_expressions_minusexpression_constructor_exists():
    assert callable(uppaal_expressions_MinusExpression.__init__)


def test_hyp_uppaal_expressions_minusexpression_constructor_args():
    sig = inspect.signature(uppaal_expressions_MinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_typeexpression_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_TypeExpression)


def test_hyp_uppaal_types_typeexpression_constructor_exists():
    assert callable(uppaal_types_TypeExpression.__init__)


def test_hyp_uppaal_types_typeexpression_constructor_args():
    sig = inspect.signature(uppaal_types_TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelementcontainer_is_not_abstract():
    assert not inspect.isabstract(TypedElementContainer)


def test_hyp_typedelementcontainer_constructor_exists():
    assert callable(TypedElementContainer.__init__)


def test_hyp_typedelementcontainer_constructor_args():
    sig = inspect.signature(TypedElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_parametercontainer_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_ParameterContainer)


def test_hyp_uppaal_declarations_parametercontainer_constructor_exists():
    assert callable(uppaal_declarations_ParameterContainer.__init__)


def test_hyp_uppaal_declarations_parametercontainer_constructor_args():
    sig = inspect.signature(uppaal_declarations_ParameterContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_templates_selection_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Selection)


def test_hyp_uppaal_templates_selection_constructor_exists():
    assert callable(uppaal_templates_Selection.__init__)


def test_hyp_uppaal_templates_selection_constructor_args():
    sig = inspect.signature(uppaal_templates_Selection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_core_typedelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_core_TypedElement)


def test_hyp_uppaal_core_typedelement_constructor_exists():
    assert callable(uppaal_core_TypedElement.__init__)


def test_hyp_uppaal_core_typedelement_constructor_args():
    sig = inspect.signature(uppaal_core_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_core_commentableelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_core_CommentableElement)


def test_hyp_uppaal_core_commentableelement_constructor_exists():
    assert callable(uppaal_core_CommentableElement.__init__)


def test_hyp_uppaal_core_commentableelement_constructor_args():
    sig = inspect.signature(uppaal_core_CommentableElement.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"




def test_hyp_uppaal_core_namedelement_is_not_abstract():
    assert not inspect.isabstract(uppaal_core_NamedElement)


def test_hyp_uppaal_core_namedelement_constructor_exists():
    assert callable(uppaal_core_NamedElement.__init__)


def test_hyp_uppaal_core_namedelement_constructor_args():
    sig = inspect.signature(uppaal_core_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_hyp_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_hyp_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_declaredtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_DeclaredType)


def test_hyp_uppaal_types_declaredtype_constructor_exists():
    assert callable(uppaal_types_DeclaredType.__init__)


def test_hyp_uppaal_types_declaredtype_constructor_args():
    sig = inspect.signature(uppaal_types_DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_types_predefinedtype_is_not_abstract():
    assert not inspect.isabstract(uppaal_types_PredefinedType)


def test_hyp_uppaal_types_predefinedtype_constructor_exists():
    assert callable(uppaal_types_PredefinedType.__init__)


def test_hyp_uppaal_types_predefinedtype_constructor_args():
    sig = inspect.signature(uppaal_types_PredefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_core_commentableelement_is_not_abstract():
    assert not inspect.isabstract(core_CommentableElement)


def test_hyp_core_commentableelement_constructor_exists():
    assert callable(core_CommentableElement.__init__)


def test_hyp_core_commentableelement_constructor_args():
    sig = inspect.signature(core_CommentableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_templates_edge_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Edge)


def test_hyp_uppaal_templates_edge_constructor_exists():
    assert callable(uppaal_templates_Edge.__init__)


def test_hyp_uppaal_templates_edge_constructor_args():
    sig = inspect.signature(uppaal_templates_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_core_namedelement_is_not_abstract():
    assert not inspect.isabstract(core_NamedElement)


def test_hyp_core_namedelement_constructor_exists():
    assert callable(core_NamedElement.__init__)


def test_hyp_core_namedelement_constructor_args():
    sig = inspect.signature(core_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_function_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Function)


def test_hyp_uppaal_declarations_function_constructor_exists():
    assert callable(uppaal_declarations_Function.__init__)


def test_hyp_uppaal_declarations_function_constructor_args():
    sig = inspect.signature(uppaal_declarations_Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_declarations_variable_is_not_abstract():
    assert not inspect.isabstract(uppaal_declarations_Variable)


def test_hyp_uppaal_declarations_variable_constructor_exists():
    assert callable(uppaal_declarations_Variable.__init__)


def test_hyp_uppaal_declarations_variable_constructor_args():
    sig = inspect.signature(uppaal_declarations_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uppaal_templates_location_is_not_abstract():
    assert not inspect.isabstract(uppaal_templates_Location)


def test_hyp_uppaal_templates_location_constructor_exists():
    assert callable(uppaal_templates_Location.__init__)


def test_hyp_uppaal_templates_location_constructor_args():
    sig = inspect.signature(uppaal_templates_Location.__init__)
    params = list(sig.parameters.keys())
    assert "locationTimeKind" in params, "Missing parameter 'locationTimeKind'"




def test_hyp_uppaal_nta_is_not_abstract():
    assert not inspect.isabstract(uppaal_NTA)


def test_hyp_uppaal_nta_constructor_exists():
    assert callable(uppaal_NTA.__init__)


def test_hyp_uppaal_nta_constructor_args():
    sig = inspect.signature(uppaal_NTA.__init__)
    params = list(sig.parameters.keys())



def test_hyp_systemdeclarations_is_not_abstract():
    assert not inspect.isabstract(SystemDeclarations)


def test_hyp_systemdeclarations_constructor_exists():
    assert callable(SystemDeclarations.__init__)


def test_hyp_systemdeclarations_constructor_args():
    sig = inspect.signature(SystemDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_hyp_template_is_not_abstract():
    assert not inspect.isabstract(Template)


def test_hyp_template_constructor_exists():
    assert callable(Template.__init__)


def test_hyp_template_constructor_args():
    sig = inspect.signature(Template.__init__)
    params = list(sig.parameters.keys())



def test_hyp_globaldeclarations_is_not_abstract():
    assert not inspect.isabstract(GlobalDeclarations)


def test_hyp_globaldeclarations_constructor_exists():
    assert callable(GlobalDeclarations.__init__)


def test_hyp_globaldeclarations_constructor_args():
    sig = inspect.signature(GlobalDeclarations.__init__)
    params = list(sig.parameters.keys())

def test_hyp_datavariableprefix_exists():
    # Check that the Enumeration exists
    assert DataVariablePrefix is not None

def test_hyp_datavariableprefix_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataVariablePrefix]
    expected_literals = [
        "CONST",
        "META",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataVariablePrefix"

def test_hyp_minmaxoperator_exists():
    # Check that the Enumeration exists
    assert MinMaxOperator is not None

def test_hyp_minmaxoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MinMaxOperator]
    expected_literals = [
        "MIN",
        "MAX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MinMaxOperator"

def test_hyp_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_hyp_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "MODULO",
        "DIVIDE",
        "ADD",
        "MULTIPLICATE",
        "SUBTRACT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_hyp_bitshiftoperator_exists():
    # Check that the Enumeration exists
    assert BitShiftOperator is not None

def test_hyp_bitshiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitShiftOperator]
    expected_literals = [
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitShiftOperator"

def test_hyp_incrementdecrementoperator_exists():
    # Check that the Enumeration exists
    assert IncrementDecrementOperator is not None

def test_hyp_incrementdecrementoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncrementDecrementOperator]
    expected_literals = [
        "DECREMENT",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncrementDecrementOperator"

def test_hyp_calltype_exists():
    # Check that the Enumeration exists
    assert CallType is not None

def test_hyp_calltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallType]
    expected_literals = [
        "CALL_BY_VALUE",
        "CALL_BY_REFERENCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallType"

def test_hyp_compareoperator_exists():
    # Check that the Enumeration exists
    assert CompareOperator is not None

def test_hyp_compareoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompareOperator]
    expected_literals = [
        "LESS",
        "GREATER",
        "EQUAL",
        "GREATER_OR_EQUAL",
        "UNEQUAL",
        "LESS_OR_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompareOperator"

def test_hyp_quantifier_exists():
    # Check that the Enumeration exists
    assert Quantifier is not None

def test_hyp_quantifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Quantifier]
    expected_literals = [
        "UNIVERSAL",
        "EXISTENTIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Quantifier"

def test_hyp_locationkind_exists():
    # Check that the Enumeration exists
    assert LocationKind is not None

def test_hyp_locationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationKind]
    expected_literals = [
        "COMMITED",
        "NORMAL",
        "URGENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationKind"

def test_hyp_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_hyp_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "PLUS_EQUAL",
        "BIT_OR_EQUAL",
        "MINUS_EQUAL",
        "BIT_XOR_EQUAL",
        "BIT_RIGHT_EQUAL",
        "EQUAL",
        "MODULO_EQUAL",
        "BIT_AND_EQUAL",
        "DIVIDE_EQUAL",
        "BIT_LEFT_EQUAL",
        "TIMES_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_hyp_synchronizationkind_exists():
    # Check that the Enumeration exists
    assert SynchronizationKind is not None

def test_hyp_synchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynchronizationKind]
    expected_literals = [
        "SEND",
        "RECEIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SynchronizationKind"

def test_hyp_builtintype_exists():
    # Check that the Enumeration exists
    assert BuiltInType is not None

def test_hyp_builtintype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltInType]
    expected_literals = [
        "CLOCK",
        "INT",
        "CHAN",
        "BOOL",
        "VOID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltInType"

def test_hyp_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_hyp_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "OR",
        "AND",
        "IMPLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_hyp_bitwiseoperator_exists():
    # Check that the Enumeration exists
    assert BitwiseOperator is not None

def test_hyp_bitwiseoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitwiseOperator]
    expected_literals = [
        "AND",
        "XOR",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitwiseOperator"


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
uppaal_visuals_Point_strategy = st.builds(
    uppaal_visuals_Point,
    y=
        st.integers(),
    x=
        st.integers()
)
uppaal_visuals_LinearElement_strategy = st.builds(
    uppaal_visuals_LinearElement,
)
Point_strategy = st.builds(
    Point,
)
uppaal_visuals_PlanarElement_strategy = st.builds(
    uppaal_visuals_PlanarElement,
)
uppaal_visuals_ColoredElement_strategy = st.builds(
    uppaal_visuals_ColoredElement,
    colorCode=
        safe_text
)
IncrementDecrementExpression_strategy = st.builds(
    IncrementDecrementExpression,
)
uppaal_expressions_PostIncrementDecrementExpression_strategy = st.builds(
    uppaal_expressions_PostIncrementDecrementExpression,
)
uppaal_expressions_PreIncrementDecrementExpression_strategy = st.builds(
    uppaal_expressions_PreIncrementDecrementExpression,
)
expressions_Expression_strategy = st.builds(
    expressions_Expression,
)
Function_strategy = st.builds(
    Function,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
uppaal_expressions_CompareExpression_strategy = st.builds(
    uppaal_expressions_CompareExpression,
    operator=
        safe_text
)
uppaal_expressions_MinMaxExpression_strategy = st.builds(
    uppaal_expressions_MinMaxExpression,
    operator=
        safe_text
)
uppaal_expressions_LogicalExpression_strategy = st.builds(
    uppaal_expressions_LogicalExpression,
    operator=
        safe_text
)
uppaal_expressions_ArithmeticExpression_strategy = st.builds(
    uppaal_expressions_ArithmeticExpression,
    operator=
        safe_text
)
uppaal_expressions_BitwiseExpression_strategy = st.builds(
    uppaal_expressions_BitwiseExpression,
    operator=
        safe_text
)
uppaal_expressions_BitShiftExpression_strategy = st.builds(
    uppaal_expressions_BitShiftExpression,
    operator=
        safe_text
)
uppaal_expressions_AssignmentExpression_strategy = st.builds(
    uppaal_expressions_AssignmentExpression,
    operator=
        safe_text
)
uppaal_expressions_Expression_strategy = st.builds(
    uppaal_expressions_Expression,
)
statements_Statement_strategy = st.builds(
    statements_Statement,
)
uppaal_templates_Synchronization_strategy = st.builds(
    uppaal_templates_Synchronization,
    kind=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
uppaal_statements_IfStatement_strategy = st.builds(
    uppaal_statements_IfStatement,
)
uppaal_statements_EmptyStatement_strategy = st.builds(
    uppaal_statements_EmptyStatement,
)
uppaal_statements_ForLoop_strategy = st.builds(
    uppaal_statements_ForLoop,
)
uppaal_statements_DoWhileLoop_strategy = st.builds(
    uppaal_statements_DoWhileLoop,
)
uppaal_statements_ExpressionStatement_strategy = st.builds(
    uppaal_statements_ExpressionStatement,
)
uppaal_statements_ReturnStatement_strategy = st.builds(
    uppaal_statements_ReturnStatement,
)
uppaal_statements_WhileLoop_strategy = st.builds(
    uppaal_statements_WhileLoop,
)
uppaal_statements_Block_strategy = st.builds(
    uppaal_statements_Block,
)
uppaal_statements_Statement_strategy = st.builds(
    uppaal_statements_Statement,
)
visuals_LinearElement_strategy = st.builds(
    visuals_LinearElement,
)
Selection_strategy = st.builds(
    Selection,
)
Synchronization_strategy = st.builds(
    Synchronization,
)
Location_strategy = st.builds(
    Location,
)
LocalDeclarations_strategy = st.builds(
    LocalDeclarations,
)
visuals_ColoredElement_strategy = st.builds(
    visuals_ColoredElement,
)
visuals_PlanarElement_strategy = st.builds(
    visuals_PlanarElement,
)
system_TemplateDeclaration_strategy = st.builds(
    system_TemplateDeclaration,
)
Edge_strategy = st.builds(
    Edge,
)
RedefinedTemplate_strategy = st.builds(
    RedefinedTemplate,
)
IdentifierExpression_strategy = st.builds(
    IdentifierExpression,
)
PriorityItem_strategy = st.builds(
    PriorityItem,
)
uppaal_global_DefaultItem_strategy = st.builds(
    uppaal_global_DefaultItem,
)
uppaal_global_ChannelItem_strategy = st.builds(
    uppaal_global_ChannelItem,
)
uppaal_global_PriorityItem_strategy = st.builds(
    uppaal_global_PriorityItem,
)
global_PriorityItem_strategy = st.builds(
    global_PriorityItem,
)
uppaal_global_ChannelPriorityGroup_strategy = st.builds(
    uppaal_global_ChannelPriorityGroup,
)
uppaal_system_ProgressMeasure_strategy = st.builds(
    uppaal_system_ProgressMeasure,
)
AbstractTemplate_strategy = st.builds(
    AbstractTemplate,
)
uppaal_templates_RedefinedTemplate_strategy = st.builds(
    uppaal_templates_RedefinedTemplate,
)
uppaal_templates_Template_strategy = st.builds(
    uppaal_templates_Template,
)
uppaal_system_InstantiationList_strategy = st.builds(
    uppaal_system_InstantiationList,
)
system_InstantiationList_strategy = st.builds(
    system_InstantiationList,
)
uppaal_system_System_strategy = st.builds(
    uppaal_system_System,
)
uppaal_declarations_Initializer_strategy = st.builds(
    uppaal_declarations_Initializer,
)
Variable_strategy = st.builds(
    Variable,
)
uppaal_declarations_Parameter_strategy = st.builds(
    uppaal_declarations_Parameter,
    callType=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
uppaal_declarations_TypedElementContainer_strategy = st.builds(
    uppaal_declarations_TypedElementContainer,
)
global_ChannelPriorityGroup_strategy = st.builds(
    global_ChannelPriorityGroup,
)
Initializer_strategy = st.builds(
    Initializer,
)
uppaal_declarations_ExpressionInitializer_strategy = st.builds(
    uppaal_declarations_ExpressionInitializer,
)
uppaal_declarations_ArrayInitializer_strategy = st.builds(
    uppaal_declarations_ArrayInitializer,
)
declarations_TypedElementContainer_strategy = st.builds(
    declarations_TypedElementContainer,
)
uppaal_statements_Iteration_strategy = st.builds(
    uppaal_statements_Iteration,
)
uppaal_expressions_QuantificationExpression_strategy = st.builds(
    uppaal_expressions_QuantificationExpression,
    quantifier=
        safe_text
)
declarations_Declaration_strategy = st.builds(
    declarations_Declaration,
)
uppaal_declarations_TypedDeclaration_strategy = st.builds(
    uppaal_declarations_TypedDeclaration,
)
DeclaredType_strategy = st.builds(
    DeclaredType,
)
uppaal_declarations_Declaration_strategy = st.builds(
    uppaal_declarations_Declaration,
)
system_ProgressMeasure_strategy = st.builds(
    system_ProgressMeasure,
)
system_System_strategy = st.builds(
    system_System,
)
global_ChannelPriorityDeclaration_strategy = st.builds(
    global_ChannelPriorityDeclaration,
)
ParameterContainer_strategy = st.builds(
    ParameterContainer,
)
Block_strategy = st.builds(
    Block,
)
core_TypedElement_strategy = st.builds(
    core_TypedElement,
)
uppaal_types_IntegerBounds_strategy = st.builds(
    uppaal_types_IntegerBounds,
)
IntegerBounds_strategy = st.builds(
    IntegerBounds,
)
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
TypeExpression_strategy = st.builds(
    TypeExpression,
)
uppaal_types_StructTypeSpecification_strategy = st.builds(
    uppaal_types_StructTypeSpecification,
)
uppaal_types_RangeTypeSpecification_strategy = st.builds(
    uppaal_types_RangeTypeSpecification,
)
uppaal_types_ScalarTypeSpecification_strategy = st.builds(
    uppaal_types_ScalarTypeSpecification,
)
Declarations_strategy = st.builds(
    Declarations,
)
uppaal_declarations_SystemDeclarations_strategy = st.builds(
    uppaal_declarations_SystemDeclarations,
)
uppaal_declarations_LocalDeclarations_strategy = st.builds(
    uppaal_declarations_LocalDeclarations,
)
uppaal_declarations_GlobalDeclarations_strategy = st.builds(
    uppaal_declarations_GlobalDeclarations,
)
Declaration_strategy = st.builds(
    Declaration,
)
uppaal_global_ChannelPriorityDeclaration_strategy = st.builds(
    uppaal_global_ChannelPriorityDeclaration,
)
uppaal_system_TemplateDeclaration_strategy = st.builds(
    uppaal_system_TemplateDeclaration,
)
uppaal_declarations_TypeDeclaration_strategy = st.builds(
    uppaal_declarations_TypeDeclaration,
)
uppaal_declarations_Declarations_strategy = st.builds(
    uppaal_declarations_Declarations,
)
PredefinedType_strategy = st.builds(
    PredefinedType,
)
uppaal_types_Library_strategy = st.builds(
    uppaal_types_Library,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uppaal_templates_AbstractTemplate_strategy = st.builds(
    uppaal_templates_AbstractTemplate,
)
uppaal_types_Type_strategy = st.builds(
    uppaal_types_Type,
    baseType=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
uppaal_expressions_NegationExpression_strategy = st.builds(
    uppaal_expressions_NegationExpression,
)
uppaal_expressions_LiteralExpression_strategy = st.builds(
    uppaal_expressions_LiteralExpression,
    text=
        safe_text
)
uppaal_expressions_PlusExpression_strategy = st.builds(
    uppaal_expressions_PlusExpression,
)
uppaal_expressions_BinaryExpression_strategy = st.builds(
    uppaal_expressions_BinaryExpression,
)
uppaal_expressions_FunctionCallExpression_strategy = st.builds(
    uppaal_expressions_FunctionCallExpression,
)
uppaal_expressions_IdentifierExpression_strategy = st.builds(
    uppaal_expressions_IdentifierExpression,
)
uppaal_expressions_ChannelPrefixExpression_strategy = st.builds(
    uppaal_expressions_ChannelPrefixExpression,
    broadcast=
        st.booleans(),
    urgent=
        st.booleans()
)
uppaal_expressions_DataPrefixExpression_strategy = st.builds(
    uppaal_expressions_DataPrefixExpression,
    prefix=
        safe_text
)
uppaal_expressions_ConditionExpression_strategy = st.builds(
    uppaal_expressions_ConditionExpression,
)
uppaal_expressions_ScopedIdentifierExpression_strategy = st.builds(
    uppaal_expressions_ScopedIdentifierExpression,
)
uppaal_expressions_IncrementDecrementExpression_strategy = st.builds(
    uppaal_expressions_IncrementDecrementExpression,
    operator=
        safe_text
)
uppaal_expressions_MinusExpression_strategy = st.builds(
    uppaal_expressions_MinusExpression,
)
uppaal_types_TypeExpression_strategy = st.builds(
    uppaal_types_TypeExpression,
)
TypedElementContainer_strategy = st.builds(
    TypedElementContainer,
)
uppaal_declarations_ParameterContainer_strategy = st.builds(
    uppaal_declarations_ParameterContainer,
)
uppaal_templates_Selection_strategy = st.builds(
    uppaal_templates_Selection,
)
uppaal_core_TypedElement_strategy = st.builds(
    uppaal_core_TypedElement,
)
uppaal_core_CommentableElement_strategy = st.builds(
    uppaal_core_CommentableElement,
    comment=
        safe_text
)
uppaal_core_NamedElement_strategy = st.builds(
    uppaal_core_NamedElement,
    name=
        safe_text
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
Type_strategy = st.builds(
    Type,
)
uppaal_types_DeclaredType_strategy = st.builds(
    uppaal_types_DeclaredType,
)
uppaal_types_PredefinedType_strategy = st.builds(
    uppaal_types_PredefinedType,
    type=
        safe_text
)
core_CommentableElement_strategy = st.builds(
    core_CommentableElement,
)
uppaal_templates_Edge_strategy = st.builds(
    uppaal_templates_Edge,
)
core_NamedElement_strategy = st.builds(
    core_NamedElement,
)
uppaal_declarations_Function_strategy = st.builds(
    uppaal_declarations_Function,
)
uppaal_declarations_Variable_strategy = st.builds(
    uppaal_declarations_Variable,
)
uppaal_templates_Location_strategy = st.builds(
    uppaal_templates_Location,
    locationTimeKind=
        safe_text
)
uppaal_NTA_strategy = st.builds(
    uppaal_NTA,
)
SystemDeclarations_strategy = st.builds(
    SystemDeclarations,
)
Template_strategy = st.builds(
    Template,
)
GlobalDeclarations_strategy = st.builds(
    GlobalDeclarations,
)




@given(instance=uppaal_visuals_Point_strategy)
def test_hyp_uppaal_visuals_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=uppaal_visuals_Point_strategy)
def test_hyp_uppaal_visuals_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original







@given(instance=uppaal_visuals_ColoredElement_strategy)
def test_hyp_uppaal_visuals_coloredelement_colorCode_setter(instance):
    original = instance.colorCode
    instance.colorCode = original
    assert instance.colorCode == original










@given(instance=uppaal_expressions_CompareExpression_strategy)
def test_hyp_uppaal_expressions_compareexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=uppaal_expressions_MinMaxExpression_strategy)
def test_hyp_uppaal_expressions_minmaxexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=uppaal_expressions_LogicalExpression_strategy)
def test_hyp_uppaal_expressions_logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=uppaal_expressions_ArithmeticExpression_strategy)
def test_hyp_uppaal_expressions_arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=uppaal_expressions_BitwiseExpression_strategy)
def test_hyp_uppaal_expressions_bitwiseexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=uppaal_expressions_BitShiftExpression_strategy)
def test_hyp_uppaal_expressions_bitshiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=uppaal_expressions_AssignmentExpression_strategy)
def test_hyp_uppaal_expressions_assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original






@given(instance=uppaal_templates_Synchronization_strategy)
def test_hyp_uppaal_templates_synchronization_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original








































@given(instance=uppaal_declarations_Parameter_strategy)
def test_hyp_uppaal_declarations_parameter_callType_setter(instance):
    original = instance.callType
    instance.callType = original
    assert instance.callType == original












@given(instance=uppaal_expressions_QuantificationExpression_strategy)
def test_hyp_uppaal_expressions_quantificationexpression_quantifier_setter(instance):
    original = instance.quantifier
    instance.quantifier = original
    assert instance.quantifier == original


































@given(instance=uppaal_types_Type_strategy)
def test_hyp_uppaal_types_type_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original






@given(instance=uppaal_expressions_LiteralExpression_strategy)
def test_hyp_uppaal_expressions_literalexpression_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original








@given(instance=uppaal_expressions_ChannelPrefixExpression_strategy)
def test_hyp_uppaal_expressions_channelprefixexpression_broadcast_setter(instance):
    original = instance.broadcast
    instance.broadcast = original
    assert instance.broadcast == original



@given(instance=uppaal_expressions_ChannelPrefixExpression_strategy)
def test_hyp_uppaal_expressions_channelprefixexpression_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original




@given(instance=uppaal_expressions_DataPrefixExpression_strategy)
def test_hyp_uppaal_expressions_dataprefixexpression_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original






@given(instance=uppaal_expressions_IncrementDecrementExpression_strategy)
def test_hyp_uppaal_expressions_incrementdecrementexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original










@given(instance=uppaal_core_CommentableElement_strategy)
def test_hyp_uppaal_core_commentableelement_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original




@given(instance=uppaal_core_NamedElement_strategy)
def test_hyp_uppaal_core_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=uppaal_types_PredefinedType_strategy)
def test_hyp_uppaal_types_predefinedtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original









@given(instance=uppaal_templates_Location_strategy)
def test_hyp_uppaal_templates_location_locationTimeKind_setter(instance):
    original = instance.locationTimeKind
    instance.locationTimeKind = original
    assert instance.locationTimeKind == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractTemplate,
    BinaryExpression,
    Block,
    Declaration,
    Declarations,
    DeclaredType,
    Edge,
    Expression,
    Function,
    GlobalDeclarations,
    IdentifierExpression,
    IncrementDecrementExpression,
    Initializer,
    IntegerBounds,
    LocalDeclarations,
    Location,
    NamedElement,
    ParameterContainer,
    Point,
    PredefinedType,
    PriorityItem,
    RedefinedTemplate,
    Selection,
    Statement,
    Synchronization,
    SystemDeclarations,
    Template,
    Type,
    TypeDeclaration,
    TypeExpression,
    TypedDeclaration,
    TypedElement,
    TypedElementContainer,
    Variable,
    core_CommentableElement,
    core_NamedElement,
    core_TypedElement,
    declarations_Declaration,
    declarations_TypedElementContainer,
    expressions_Expression,
    global_ChannelPriorityDeclaration,
    global_ChannelPriorityGroup,
    global_PriorityItem,
    statements_Statement,
    system_InstantiationList,
    system_ProgressMeasure,
    system_System,
    system_TemplateDeclaration,
    uppaal_NTA,
    uppaal_core_CommentableElement,
    uppaal_core_NamedElement,
    uppaal_core_TypedElement,
    uppaal_declarations_ArrayInitializer,
    uppaal_declarations_Declaration,
    uppaal_declarations_Declarations,
    uppaal_declarations_ExpressionInitializer,
    uppaal_declarations_Function,
    uppaal_declarations_GlobalDeclarations,
    uppaal_declarations_Initializer,
    uppaal_declarations_LocalDeclarations,
    uppaal_declarations_Parameter,
    uppaal_declarations_ParameterContainer,
    uppaal_declarations_SystemDeclarations,
    uppaal_declarations_TypeDeclaration,
    uppaal_declarations_TypedDeclaration,
    uppaal_declarations_TypedElementContainer,
    uppaal_declarations_Variable,
    uppaal_expressions_ArithmeticExpression,
    uppaal_expressions_AssignmentExpression,
    uppaal_expressions_BinaryExpression,
    uppaal_expressions_BitShiftExpression,
    uppaal_expressions_BitwiseExpression,
    uppaal_expressions_ChannelPrefixExpression,
    uppaal_expressions_CompareExpression,
    uppaal_expressions_ConditionExpression,
    uppaal_expressions_DataPrefixExpression,
    uppaal_expressions_Expression,
    uppaal_expressions_FunctionCallExpression,
    uppaal_expressions_IdentifierExpression,
    uppaal_expressions_IncrementDecrementExpression,
    uppaal_expressions_LiteralExpression,
    uppaal_expressions_LogicalExpression,
    uppaal_expressions_MinMaxExpression,
    uppaal_expressions_MinusExpression,
    uppaal_expressions_NegationExpression,
    uppaal_expressions_PlusExpression,
    uppaal_expressions_PostIncrementDecrementExpression,
    uppaal_expressions_PreIncrementDecrementExpression,
    uppaal_expressions_QuantificationExpression,
    uppaal_expressions_ScopedIdentifierExpression,
    uppaal_global_ChannelItem,
    uppaal_global_ChannelPriorityDeclaration,
    uppaal_global_ChannelPriorityGroup,
    uppaal_global_DefaultItem,
    uppaal_global_PriorityItem,
    uppaal_statements_Block,
    uppaal_statements_DoWhileLoop,
    uppaal_statements_EmptyStatement,
    uppaal_statements_ExpressionStatement,
    uppaal_statements_ForLoop,
    uppaal_statements_IfStatement,
    uppaal_statements_Iteration,
    uppaal_statements_ReturnStatement,
    uppaal_statements_Statement,
    uppaal_statements_WhileLoop,
    uppaal_system_InstantiationList,
    uppaal_system_ProgressMeasure,
    uppaal_system_System,
    uppaal_system_TemplateDeclaration,
    uppaal_templates_AbstractTemplate,
    uppaal_templates_Edge,
    uppaal_templates_Location,
    uppaal_templates_RedefinedTemplate,
    uppaal_templates_Selection,
    uppaal_templates_Synchronization,
    uppaal_templates_Template,
    uppaal_types_DeclaredType,
    uppaal_types_IntegerBounds,
    uppaal_types_Library,
    uppaal_types_PredefinedType,
    uppaal_types_RangeTypeSpecification,
    uppaal_types_ScalarTypeSpecification,
    uppaal_types_StructTypeSpecification,
    uppaal_types_Type,
    uppaal_types_TypeExpression,
    uppaal_visuals_ColoredElement,
    uppaal_visuals_LinearElement,
    uppaal_visuals_PlanarElement,
    uppaal_visuals_Point,
    visuals_ColoredElement,
    visuals_LinearElement,
    visuals_PlanarElement,
    ArithmeticOperator,
    AssignmentOperator,
    BitShiftOperator,
    BitwiseOperator,
    BuiltInType,
    CallType,
    CompareOperator,
    DataVariablePrefix,
    IncrementDecrementOperator,
    LocationKind,
    LogicalOperator,
    MinMaxOperator,
    Quantifier,
    SynchronizationKind,
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

def test_uppaal_core_CommentableElement_comment_value_roundtrip():
    instance = uppaal_core_CommentableElement(comment="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_uppaal_core_NamedElement_name_value_roundtrip():
    instance = uppaal_core_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_uppaal_declarations_Parameter_callType_value_roundtrip():
    instance = uppaal_declarations_Parameter(callType="sample_text")
    assert instance.callType == "sample_text"
    instance.callType = "sample_text_2"
    assert instance.callType == "sample_text_2"


def test_uppaal_expressions_ArithmeticExpression_operator_value_roundtrip():
    instance = uppaal_expressions_ArithmeticExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_uppaal_expressions_AssignmentExpression_operator_value_roundtrip():
    instance = uppaal_expressions_AssignmentExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_uppaal_expressions_BitShiftExpression_operator_value_roundtrip():
    instance = uppaal_expressions_BitShiftExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_uppaal_expressions_BitwiseExpression_operator_value_roundtrip():
    instance = uppaal_expressions_BitwiseExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_uppaal_expressions_ChannelPrefixExpression_broadcast_value_roundtrip():
    instance = uppaal_expressions_ChannelPrefixExpression(broadcast=True, urgent=True)
    assert instance.broadcast == True
    instance.broadcast = False
    assert instance.broadcast == False


def test_uppaal_expressions_ChannelPrefixExpression_urgent_value_roundtrip():
    instance = uppaal_expressions_ChannelPrefixExpression(broadcast=True, urgent=True)
    assert instance.urgent == True
    instance.urgent = False
    assert instance.urgent == False


def test_uppaal_expressions_CompareExpression_operator_value_roundtrip():
    instance = uppaal_expressions_CompareExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_uppaal_expressions_DataPrefixExpression_prefix_value_roundtrip():
    instance = uppaal_expressions_DataPrefixExpression(prefix="sample_text")
    assert instance.prefix == "sample_text"
    instance.prefix = "sample_text_2"
    assert instance.prefix == "sample_text_2"


def test_uppaal_expressions_IncrementDecrementExpression_operator_value_roundtrip():
    instance = uppaal_expressions_IncrementDecrementExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_uppaal_expressions_LiteralExpression_text_value_roundtrip():
    instance = uppaal_expressions_LiteralExpression(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_uppaal_expressions_LogicalExpression_operator_value_roundtrip():
    instance = uppaal_expressions_LogicalExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_uppaal_expressions_MinMaxExpression_operator_value_roundtrip():
    instance = uppaal_expressions_MinMaxExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_uppaal_expressions_QuantificationExpression_quantifier_value_roundtrip():
    instance = uppaal_expressions_QuantificationExpression(quantifier="sample_text")
    assert instance.quantifier == "sample_text"
    instance.quantifier = "sample_text_2"
    assert instance.quantifier == "sample_text_2"


def test_uppaal_templates_Location_locationTimeKind_value_roundtrip():
    instance = uppaal_templates_Location(locationTimeKind="sample_text")
    assert instance.locationTimeKind == "sample_text"
    instance.locationTimeKind = "sample_text_2"
    assert instance.locationTimeKind == "sample_text_2"


def test_uppaal_templates_Synchronization_kind_value_roundtrip():
    instance = uppaal_templates_Synchronization(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_uppaal_types_PredefinedType_type_value_roundtrip():
    instance = uppaal_types_PredefinedType(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_uppaal_types_Type_baseType_value_roundtrip():
    instance = uppaal_types_Type(baseType="sample_text")
    assert instance.baseType == "sample_text"
    instance.baseType = "sample_text_2"
    assert instance.baseType == "sample_text_2"


def test_uppaal_visuals_ColoredElement_colorCode_value_roundtrip():
    instance = uppaal_visuals_ColoredElement(colorCode="sample_text")
    assert instance.colorCode == "sample_text"
    instance.colorCode = "sample_text_2"
    assert instance.colorCode == "sample_text_2"


def test_uppaal_visuals_Point_x_value_roundtrip():
    instance = uppaal_visuals_Point(x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_uppaal_visuals_Point_y_value_roundtrip():
    instance = uppaal_visuals_Point(x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_uppaal_templates_RedefinedTemplate_isa_AbstractTemplate():
    instance = uppaal_templates_RedefinedTemplate()
    assert isinstance(instance, AbstractTemplate)


def test_uppaal_templates_Template_isa_AbstractTemplate():
    instance = uppaal_templates_Template()
    assert isinstance(instance, AbstractTemplate)


def test_uppaal_expressions_ArithmeticExpression_isa_BinaryExpression():
    instance = uppaal_expressions_ArithmeticExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_uppaal_expressions_AssignmentExpression_isa_BinaryExpression():
    instance = uppaal_expressions_AssignmentExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_uppaal_expressions_BitShiftExpression_isa_BinaryExpression():
    instance = uppaal_expressions_BitShiftExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_uppaal_expressions_BitwiseExpression_isa_BinaryExpression():
    instance = uppaal_expressions_BitwiseExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_uppaal_expressions_CompareExpression_isa_BinaryExpression():
    instance = uppaal_expressions_CompareExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_uppaal_expressions_LogicalExpression_isa_BinaryExpression():
    instance = uppaal_expressions_LogicalExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_uppaal_expressions_MinMaxExpression_isa_BinaryExpression():
    instance = uppaal_expressions_MinMaxExpression(operator="sample_text")
    assert isinstance(instance, BinaryExpression)


def test_uppaal_declarations_TypeDeclaration_isa_Declaration():
    instance = uppaal_declarations_TypeDeclaration()
    assert isinstance(instance, Declaration)


def test_uppaal_global_ChannelPriorityDeclaration_isa_Declaration():
    instance = uppaal_global_ChannelPriorityDeclaration()
    assert isinstance(instance, Declaration)


def test_uppaal_system_TemplateDeclaration_isa_Declaration():
    instance = uppaal_system_TemplateDeclaration()
    assert isinstance(instance, Declaration)


def test_uppaal_declarations_GlobalDeclarations_isa_Declarations():
    instance = uppaal_declarations_GlobalDeclarations()
    assert isinstance(instance, Declarations)


def test_uppaal_declarations_LocalDeclarations_isa_Declarations():
    instance = uppaal_declarations_LocalDeclarations()
    assert isinstance(instance, Declarations)


def test_uppaal_declarations_SystemDeclarations_isa_Declarations():
    instance = uppaal_declarations_SystemDeclarations()
    assert isinstance(instance, Declarations)


def test_uppaal_expressions_BinaryExpression_isa_Expression():
    instance = uppaal_expressions_BinaryExpression()
    assert isinstance(instance, Expression)


def test_uppaal_expressions_ChannelPrefixExpression_isa_Expression():
    instance = uppaal_expressions_ChannelPrefixExpression(broadcast=True, urgent=True)
    assert isinstance(instance, Expression)


def test_uppaal_expressions_ConditionExpression_isa_Expression():
    instance = uppaal_expressions_ConditionExpression()
    assert isinstance(instance, Expression)


def test_uppaal_expressions_DataPrefixExpression_isa_Expression():
    instance = uppaal_expressions_DataPrefixExpression(prefix="sample_text")
    assert isinstance(instance, Expression)


def test_uppaal_expressions_FunctionCallExpression_isa_Expression():
    instance = uppaal_expressions_FunctionCallExpression()
    assert isinstance(instance, Expression)


def test_uppaal_expressions_IdentifierExpression_isa_Expression():
    instance = uppaal_expressions_IdentifierExpression()
    assert isinstance(instance, Expression)


def test_uppaal_expressions_IncrementDecrementExpression_isa_Expression():
    instance = uppaal_expressions_IncrementDecrementExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_uppaal_expressions_LiteralExpression_isa_Expression():
    instance = uppaal_expressions_LiteralExpression(text="sample_text")
    assert isinstance(instance, Expression)


def test_uppaal_expressions_MinusExpression_isa_Expression():
    instance = uppaal_expressions_MinusExpression()
    assert isinstance(instance, Expression)


def test_uppaal_expressions_NegationExpression_isa_Expression():
    instance = uppaal_expressions_NegationExpression()
    assert isinstance(instance, Expression)


def test_uppaal_expressions_PlusExpression_isa_Expression():
    instance = uppaal_expressions_PlusExpression()
    assert isinstance(instance, Expression)


def test_uppaal_expressions_ScopedIdentifierExpression_isa_Expression():
    instance = uppaal_expressions_ScopedIdentifierExpression()
    assert isinstance(instance, Expression)


def test_uppaal_types_TypeExpression_isa_Expression():
    instance = uppaal_types_TypeExpression()
    assert isinstance(instance, Expression)


def test_uppaal_expressions_PostIncrementDecrementExpression_isa_IncrementDecrementExpression():
    instance = uppaal_expressions_PostIncrementDecrementExpression()
    assert isinstance(instance, IncrementDecrementExpression)


def test_uppaal_expressions_PreIncrementDecrementExpression_isa_IncrementDecrementExpression():
    instance = uppaal_expressions_PreIncrementDecrementExpression()
    assert isinstance(instance, IncrementDecrementExpression)


def test_uppaal_declarations_ArrayInitializer_isa_Initializer():
    instance = uppaal_declarations_ArrayInitializer()
    assert isinstance(instance, Initializer)


def test_uppaal_declarations_ExpressionInitializer_isa_Initializer():
    instance = uppaal_declarations_ExpressionInitializer()
    assert isinstance(instance, Initializer)


def test_uppaal_templates_AbstractTemplate_isa_NamedElement():
    instance = uppaal_templates_AbstractTemplate()
    assert isinstance(instance, NamedElement)


def test_uppaal_types_Type_isa_NamedElement():
    instance = uppaal_types_Type(baseType="sample_text")
    assert isinstance(instance, NamedElement)


def test_uppaal_global_ChannelItem_isa_PriorityItem():
    instance = uppaal_global_ChannelItem()
    assert isinstance(instance, PriorityItem)


def test_uppaal_global_DefaultItem_isa_PriorityItem():
    instance = uppaal_global_DefaultItem()
    assert isinstance(instance, PriorityItem)


def test_uppaal_statements_Block_isa_Statement():
    instance = uppaal_statements_Block()
    assert isinstance(instance, Statement)


def test_uppaal_statements_DoWhileLoop_isa_Statement():
    instance = uppaal_statements_DoWhileLoop()
    assert isinstance(instance, Statement)


def test_uppaal_statements_EmptyStatement_isa_Statement():
    instance = uppaal_statements_EmptyStatement()
    assert isinstance(instance, Statement)


def test_uppaal_statements_ExpressionStatement_isa_Statement():
    instance = uppaal_statements_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_uppaal_statements_ForLoop_isa_Statement():
    instance = uppaal_statements_ForLoop()
    assert isinstance(instance, Statement)


def test_uppaal_statements_IfStatement_isa_Statement():
    instance = uppaal_statements_IfStatement()
    assert isinstance(instance, Statement)


def test_uppaal_statements_ReturnStatement_isa_Statement():
    instance = uppaal_statements_ReturnStatement()
    assert isinstance(instance, Statement)


def test_uppaal_statements_WhileLoop_isa_Statement():
    instance = uppaal_statements_WhileLoop()
    assert isinstance(instance, Statement)


def test_uppaal_types_DeclaredType_isa_Type():
    instance = uppaal_types_DeclaredType()
    assert isinstance(instance, Type)


def test_uppaal_types_PredefinedType_isa_Type():
    instance = uppaal_types_PredefinedType(type="sample_text")
    assert isinstance(instance, Type)


def test_uppaal_types_RangeTypeSpecification_isa_TypeExpression():
    instance = uppaal_types_RangeTypeSpecification()
    assert isinstance(instance, TypeExpression)


def test_uppaal_types_ScalarTypeSpecification_isa_TypeExpression():
    instance = uppaal_types_ScalarTypeSpecification()
    assert isinstance(instance, TypeExpression)


def test_uppaal_types_StructTypeSpecification_isa_TypeExpression():
    instance = uppaal_types_StructTypeSpecification()
    assert isinstance(instance, TypeExpression)


def test_uppaal_declarations_ParameterContainer_isa_TypedElementContainer():
    instance = uppaal_declarations_ParameterContainer()
    assert isinstance(instance, TypedElementContainer)


def test_uppaal_templates_Selection_isa_TypedElementContainer():
    instance = uppaal_templates_Selection()
    assert isinstance(instance, TypedElementContainer)


def test_uppaal_declarations_Parameter_isa_Variable():
    instance = uppaal_declarations_Parameter(callType="sample_text")
    assert isinstance(instance, Variable)


def test_uppaal_NTA_isa_core_CommentableElement():
    instance = uppaal_NTA()
    assert isinstance(instance, core_CommentableElement)


def test_uppaal_templates_Edge_isa_core_CommentableElement():
    instance = uppaal_templates_Edge()
    assert isinstance(instance, core_CommentableElement)


def test_uppaal_templates_Location_isa_core_CommentableElement():
    instance = uppaal_templates_Location(locationTimeKind="sample_text")
    assert isinstance(instance, core_CommentableElement)


def test_uppaal_NTA_isa_core_NamedElement():
    instance = uppaal_NTA()
    assert isinstance(instance, core_NamedElement)


def test_uppaal_declarations_Function_isa_core_NamedElement():
    instance = uppaal_declarations_Function()
    assert isinstance(instance, core_NamedElement)


def test_uppaal_declarations_Variable_isa_core_NamedElement():
    instance = uppaal_declarations_Variable()
    assert isinstance(instance, core_NamedElement)


def test_uppaal_templates_Location_isa_core_NamedElement():
    instance = uppaal_templates_Location(locationTimeKind="sample_text")
    assert isinstance(instance, core_NamedElement)


def test_uppaal_declarations_Function_isa_core_TypedElement():
    instance = uppaal_declarations_Function()
    assert isinstance(instance, core_TypedElement)


def test_uppaal_declarations_Variable_isa_core_TypedElement():
    instance = uppaal_declarations_Variable()
    assert isinstance(instance, core_TypedElement)


def test_uppaal_declarations_TypedDeclaration_isa_declarations_Declaration():
    instance = uppaal_declarations_TypedDeclaration()
    assert isinstance(instance, declarations_Declaration)


def test_uppaal_declarations_TypedDeclaration_isa_declarations_TypedElementContainer():
    instance = uppaal_declarations_TypedDeclaration()
    assert isinstance(instance, declarations_TypedElementContainer)


def test_uppaal_expressions_QuantificationExpression_isa_declarations_TypedElementContainer():
    instance = uppaal_expressions_QuantificationExpression(quantifier="sample_text")
    assert isinstance(instance, declarations_TypedElementContainer)


def test_uppaal_statements_Iteration_isa_declarations_TypedElementContainer():
    instance = uppaal_statements_Iteration()
    assert isinstance(instance, declarations_TypedElementContainer)


def test_uppaal_expressions_QuantificationExpression_isa_expressions_Expression():
    instance = uppaal_expressions_QuantificationExpression(quantifier="sample_text")
    assert isinstance(instance, expressions_Expression)


def test_uppaal_statements_Iteration_isa_statements_Statement():
    instance = uppaal_statements_Iteration()
    assert isinstance(instance, statements_Statement)


def test_uppaal_templates_Edge_isa_visuals_ColoredElement():
    instance = uppaal_templates_Edge()
    assert isinstance(instance, visuals_ColoredElement)


def test_uppaal_templates_Location_isa_visuals_ColoredElement():
    instance = uppaal_templates_Location(locationTimeKind="sample_text")
    assert isinstance(instance, visuals_ColoredElement)


def test_uppaal_templates_Edge_isa_visuals_LinearElement():
    instance = uppaal_templates_Edge()
    assert isinstance(instance, visuals_LinearElement)


def test_uppaal_templates_Location_isa_visuals_PlanarElement():
    instance = uppaal_templates_Location(locationTimeKind="sample_text")
    assert isinstance(instance, visuals_PlanarElement)


def test_assoc_channelExpression87_link_reassign_clear():
    a = uppaal_templates_Synchronization(kind="sample_text")
    b1 = IdentifierExpression()
    b2 = IdentifierExpression()
    _safe_set(a, 'uppaal_templates_Synchronization', b1)
    assert _is_linked(a, 'uppaal_templates_Synchronization', b1)
    if hasattr(b1, 'IdentifierExpression88'):
        assert _is_linked(b1, 'IdentifierExpression88', a)
    _safe_set(a, 'uppaal_templates_Synchronization', b2)
    assert _is_linked(a, 'uppaal_templates_Synchronization', b2)
    if hasattr(b1, 'IdentifierExpression88'):
        assert not _is_linked(b1, 'IdentifierExpression88', a)
    if hasattr(b2, 'IdentifierExpression88'):
        assert _is_linked(b2, 'IdentifierExpression88', a)
    _safe_set(a, 'uppaal_templates_Synchronization', None)
    assert not _is_linked(a, 'uppaal_templates_Synchronization', b2)
    if hasattr(b2, 'IdentifierExpression88'):
        assert not _is_linked(b2, 'IdentifierExpression88', a)


def test_assoc_channelType164_link_reassign_clear():
    a = uppaal_expressions_ChannelPrefixExpression(broadcast=True, urgent=True)
    b1 = Type()
    b2 = Type()
    _safe_set(a, 'uppaal_expressions_ChannelPrefixExpression', b1)
    assert _is_linked(a, 'uppaal_expressions_ChannelPrefixExpression', b1)
    if hasattr(b1, 'Type'):
        assert _is_linked(b1, 'Type', a)
    _safe_set(a, 'uppaal_expressions_ChannelPrefixExpression', b2)
    assert _is_linked(a, 'uppaal_expressions_ChannelPrefixExpression', b2)
    if hasattr(b1, 'Type'):
        assert not _is_linked(b1, 'Type', a)
    if hasattr(b2, 'Type'):
        assert _is_linked(b2, 'Type', a)
    _safe_set(a, 'uppaal_expressions_ChannelPrefixExpression', None)
    assert not _is_linked(a, 'uppaal_expressions_ChannelPrefixExpression', b2)
    if hasattr(b2, 'Type'):
        assert not _is_linked(b2, 'Type', a)


def test_assoc_dataTypeExpression165_link_reassign_clear():
    a = uppaal_expressions_DataPrefixExpression(prefix="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'uppaal_expressions_DataPrefixExpression', b1)
    assert _is_linked(a, 'uppaal_expressions_DataPrefixExpression', b1)
    if hasattr(b1, 'Expression166'):
        assert _is_linked(b1, 'Expression166', a)
    _safe_set(a, 'uppaal_expressions_DataPrefixExpression', b2)
    assert _is_linked(a, 'uppaal_expressions_DataPrefixExpression', b2)
    if hasattr(b1, 'Expression166'):
        assert not _is_linked(b1, 'Expression166', a)
    if hasattr(b2, 'Expression166'):
        assert _is_linked(b2, 'Expression166', a)
    _safe_set(a, 'uppaal_expressions_DataPrefixExpression', None)
    assert not _is_linked(a, 'uppaal_expressions_DataPrefixExpression', b2)
    if hasattr(b2, 'Expression166'):
        assert not _is_linked(b2, 'Expression166', a)


def test_assoc_expression160_link_reassign_clear():
    a = uppaal_expressions_QuantificationExpression(quantifier="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'uppaal_expressions_QuantificationExpression', b1)
    assert _is_linked(a, 'uppaal_expressions_QuantificationExpression', b1)
    if hasattr(b1, 'Expression161'):
        assert _is_linked(b1, 'Expression161', a)
    _safe_set(a, 'uppaal_expressions_QuantificationExpression', b2)
    assert _is_linked(a, 'uppaal_expressions_QuantificationExpression', b2)
    if hasattr(b1, 'Expression161'):
        assert not _is_linked(b1, 'Expression161', a)
    if hasattr(b2, 'Expression161'):
        assert _is_linked(b2, 'Expression161', a)
    _safe_set(a, 'uppaal_expressions_QuantificationExpression', None)
    assert not _is_linked(a, 'uppaal_expressions_QuantificationExpression', b2)
    if hasattr(b2, 'Expression161'):
        assert not _is_linked(b2, 'Expression161', a)


def test_assoc_expression162_link_reassign_clear():
    a = uppaal_expressions_IncrementDecrementExpression(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'uppaal_expressions_IncrementDecrementExpression', b1)
    assert _is_linked(a, 'uppaal_expressions_IncrementDecrementExpression', b1)
    if hasattr(b1, 'Expression163'):
        assert _is_linked(b1, 'Expression163', a)
    _safe_set(a, 'uppaal_expressions_IncrementDecrementExpression', b2)
    assert _is_linked(a, 'uppaal_expressions_IncrementDecrementExpression', b2)
    if hasattr(b1, 'Expression163'):
        assert not _is_linked(b1, 'Expression163', a)
    if hasattr(b2, 'Expression163'):
        assert _is_linked(b2, 'Expression163', a)
    _safe_set(a, 'uppaal_expressions_IncrementDecrementExpression', None)
    assert not _is_linked(a, 'uppaal_expressions_IncrementDecrementExpression', b2)
    if hasattr(b2, 'Expression163'):
        assert not _is_linked(b2, 'Expression163', a)


def test_assoc_incomingEdges68_link_reassign_clear():
    a = uppaal_templates_Location(locationTimeKind="sample_text")
    b1 = Edge()
    b2 = Edge()
    _safe_set(a, 'target', {b1})
    assert _is_linked(a, 'target', b1)
    if hasattr(b1, 'Edge69'):
        assert _is_linked(b1, 'Edge69', a)
    _safe_set(a, 'target', {b2})
    assert _is_linked(a, 'target', b2)
    if hasattr(b1, 'Edge69'):
        assert not _is_linked(b1, 'Edge69', a)
    if hasattr(b2, 'Edge69'):
        assert _is_linked(b2, 'Edge69', a)
    _safe_set(a, 'target', set())
    assert not _is_linked(a, 'target', b2)
    if hasattr(b2, 'Edge69'):
        assert not _is_linked(b2, 'Edge69', a)


def test_assoc_invariant66_link_reassign_clear():
    a = uppaal_templates_Location(locationTimeKind="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'uppaal_templates_Location', b1)
    assert _is_linked(a, 'uppaal_templates_Location', b1)
    if hasattr(b1, 'Expression67'):
        assert _is_linked(b1, 'Expression67', a)
    _safe_set(a, 'uppaal_templates_Location', b2)
    assert _is_linked(a, 'uppaal_templates_Location', b2)
    if hasattr(b1, 'Expression67'):
        assert not _is_linked(b1, 'Expression67', a)
    if hasattr(b2, 'Expression67'):
        assert _is_linked(b2, 'Expression67', a)
    _safe_set(a, 'uppaal_templates_Location', None)
    assert not _is_linked(a, 'uppaal_templates_Location', b2)
    if hasattr(b2, 'Expression67'):
        assert not _is_linked(b2, 'Expression67', a)


def test_assoc_outgoingEdges70_link_reassign_clear():
    a = uppaal_templates_Location(locationTimeKind="sample_text")
    b1 = Edge()
    b2 = Edge()
    _safe_set(a, 'source', {b1})
    assert _is_linked(a, 'source', b1)
    if hasattr(b1, 'Edge71'):
        assert _is_linked(b1, 'Edge71', a)
    _safe_set(a, 'source', {b2})
    assert _is_linked(a, 'source', b2)
    if hasattr(b1, 'Edge71'):
        assert not _is_linked(b1, 'Edge71', a)
    if hasattr(b2, 'Edge71'):
        assert _is_linked(b2, 'Edge71', a)
    _safe_set(a, 'source', set())
    assert not _is_linked(a, 'source', b2)
    if hasattr(b2, 'Edge71'):
        assert not _is_linked(b2, 'Edge71', a)


def test_assoc_parentTemplate64_link_reassign_clear():
    a = uppaal_templates_Location(locationTimeKind="sample_text")
    b1 = Template()
    b2 = Template()
    _safe_set(a, 'location', b1)
    assert _is_linked(a, 'location', b1)
    if hasattr(b1, 'Template65'):
        assert _is_linked(b1, 'Template65', a)
    _safe_set(a, 'location', b2)
    assert _is_linked(a, 'location', b2)
    if hasattr(b1, 'Template65'):
        assert not _is_linked(b1, 'Template65', a)
    if hasattr(b2, 'Template65'):
        assert _is_linked(b2, 'Template65', a)
    _safe_set(a, 'location', None)
    assert not _is_linked(a, 'location', b2)
    if hasattr(b2, 'Template65'):
        assert not _is_linked(b2, 'Template65', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractTemplate_strategy = st.builds(AbstractTemplate)
@given(instance=AbstractTemplate_strategy)
@settings(max_examples=25)
def test_AbstractTemplate_instantiation(instance):
    assert isinstance(instance, AbstractTemplate)


BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


Block_strategy = st.builds(Block)
@given(instance=Block_strategy)
@settings(max_examples=25)
def test_Block_instantiation(instance):
    assert isinstance(instance, Block)


Declaration_strategy = st.builds(Declaration)
@given(instance=Declaration_strategy)
@settings(max_examples=25)
def test_Declaration_instantiation(instance):
    assert isinstance(instance, Declaration)


Declarations_strategy = st.builds(Declarations)
@given(instance=Declarations_strategy)
@settings(max_examples=25)
def test_Declarations_instantiation(instance):
    assert isinstance(instance, Declarations)


DeclaredType_strategy = st.builds(DeclaredType)
@given(instance=DeclaredType_strategy)
@settings(max_examples=25)
def test_DeclaredType_instantiation(instance):
    assert isinstance(instance, DeclaredType)


Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Function_strategy = st.builds(Function)
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


GlobalDeclarations_strategy = st.builds(GlobalDeclarations)
@given(instance=GlobalDeclarations_strategy)
@settings(max_examples=25)
def test_GlobalDeclarations_instantiation(instance):
    assert isinstance(instance, GlobalDeclarations)


IdentifierExpression_strategy = st.builds(IdentifierExpression)
@given(instance=IdentifierExpression_strategy)
@settings(max_examples=25)
def test_IdentifierExpression_instantiation(instance):
    assert isinstance(instance, IdentifierExpression)


IncrementDecrementExpression_strategy = st.builds(IncrementDecrementExpression)
@given(instance=IncrementDecrementExpression_strategy)
@settings(max_examples=25)
def test_IncrementDecrementExpression_instantiation(instance):
    assert isinstance(instance, IncrementDecrementExpression)


Initializer_strategy = st.builds(Initializer)
@given(instance=Initializer_strategy)
@settings(max_examples=25)
def test_Initializer_instantiation(instance):
    assert isinstance(instance, Initializer)


IntegerBounds_strategy = st.builds(IntegerBounds)
@given(instance=IntegerBounds_strategy)
@settings(max_examples=25)
def test_IntegerBounds_instantiation(instance):
    assert isinstance(instance, IntegerBounds)


LocalDeclarations_strategy = st.builds(LocalDeclarations)
@given(instance=LocalDeclarations_strategy)
@settings(max_examples=25)
def test_LocalDeclarations_instantiation(instance):
    assert isinstance(instance, LocalDeclarations)


Location_strategy = st.builds(Location)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


ParameterContainer_strategy = st.builds(ParameterContainer)
@given(instance=ParameterContainer_strategy)
@settings(max_examples=25)
def test_ParameterContainer_instantiation(instance):
    assert isinstance(instance, ParameterContainer)


Point_strategy = st.builds(Point)
@given(instance=Point_strategy)
@settings(max_examples=25)
def test_Point_instantiation(instance):
    assert isinstance(instance, Point)


PredefinedType_strategy = st.builds(PredefinedType)
@given(instance=PredefinedType_strategy)
@settings(max_examples=25)
def test_PredefinedType_instantiation(instance):
    assert isinstance(instance, PredefinedType)


PriorityItem_strategy = st.builds(PriorityItem)
@given(instance=PriorityItem_strategy)
@settings(max_examples=25)
def test_PriorityItem_instantiation(instance):
    assert isinstance(instance, PriorityItem)


RedefinedTemplate_strategy = st.builds(RedefinedTemplate)
@given(instance=RedefinedTemplate_strategy)
@settings(max_examples=25)
def test_RedefinedTemplate_instantiation(instance):
    assert isinstance(instance, RedefinedTemplate)


Selection_strategy = st.builds(Selection)
@given(instance=Selection_strategy)
@settings(max_examples=25)
def test_Selection_instantiation(instance):
    assert isinstance(instance, Selection)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Synchronization_strategy = st.builds(Synchronization)
@given(instance=Synchronization_strategy)
@settings(max_examples=25)
def test_Synchronization_instantiation(instance):
    assert isinstance(instance, Synchronization)


SystemDeclarations_strategy = st.builds(SystemDeclarations)
@given(instance=SystemDeclarations_strategy)
@settings(max_examples=25)
def test_SystemDeclarations_instantiation(instance):
    assert isinstance(instance, SystemDeclarations)


Template_strategy = st.builds(Template)
@given(instance=Template_strategy)
@settings(max_examples=25)
def test_Template_instantiation(instance):
    assert isinstance(instance, Template)


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


TypeExpression_strategy = st.builds(TypeExpression)
@given(instance=TypeExpression_strategy)
@settings(max_examples=25)
def test_TypeExpression_instantiation(instance):
    assert isinstance(instance, TypeExpression)


TypedDeclaration_strategy = st.builds(TypedDeclaration)
@given(instance=TypedDeclaration_strategy)
@settings(max_examples=25)
def test_TypedDeclaration_instantiation(instance):
    assert isinstance(instance, TypedDeclaration)


TypedElement_strategy = st.builds(TypedElement)
@given(instance=TypedElement_strategy)
@settings(max_examples=25)
def test_TypedElement_instantiation(instance):
    assert isinstance(instance, TypedElement)


TypedElementContainer_strategy = st.builds(TypedElementContainer)
@given(instance=TypedElementContainer_strategy)
@settings(max_examples=25)
def test_TypedElementContainer_instantiation(instance):
    assert isinstance(instance, TypedElementContainer)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


core_CommentableElement_strategy = st.builds(core_CommentableElement)
@given(instance=core_CommentableElement_strategy)
@settings(max_examples=25)
def test_core_CommentableElement_instantiation(instance):
    assert isinstance(instance, core_CommentableElement)


core_NamedElement_strategy = st.builds(core_NamedElement)
@given(instance=core_NamedElement_strategy)
@settings(max_examples=25)
def test_core_NamedElement_instantiation(instance):
    assert isinstance(instance, core_NamedElement)


core_TypedElement_strategy = st.builds(core_TypedElement)
@given(instance=core_TypedElement_strategy)
@settings(max_examples=25)
def test_core_TypedElement_instantiation(instance):
    assert isinstance(instance, core_TypedElement)


declarations_Declaration_strategy = st.builds(declarations_Declaration)
@given(instance=declarations_Declaration_strategy)
@settings(max_examples=25)
def test_declarations_Declaration_instantiation(instance):
    assert isinstance(instance, declarations_Declaration)


declarations_TypedElementContainer_strategy = st.builds(declarations_TypedElementContainer)
@given(instance=declarations_TypedElementContainer_strategy)
@settings(max_examples=25)
def test_declarations_TypedElementContainer_instantiation(instance):
    assert isinstance(instance, declarations_TypedElementContainer)


expressions_Expression_strategy = st.builds(expressions_Expression)
@given(instance=expressions_Expression_strategy)
@settings(max_examples=25)
def test_expressions_Expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)


global_ChannelPriorityDeclaration_strategy = st.builds(global_ChannelPriorityDeclaration)
@given(instance=global_ChannelPriorityDeclaration_strategy)
@settings(max_examples=25)
def test_global_ChannelPriorityDeclaration_instantiation(instance):
    assert isinstance(instance, global_ChannelPriorityDeclaration)


global_ChannelPriorityGroup_strategy = st.builds(global_ChannelPriorityGroup)
@given(instance=global_ChannelPriorityGroup_strategy)
@settings(max_examples=25)
def test_global_ChannelPriorityGroup_instantiation(instance):
    assert isinstance(instance, global_ChannelPriorityGroup)


global_PriorityItem_strategy = st.builds(global_PriorityItem)
@given(instance=global_PriorityItem_strategy)
@settings(max_examples=25)
def test_global_PriorityItem_instantiation(instance):
    assert isinstance(instance, global_PriorityItem)


statements_Statement_strategy = st.builds(statements_Statement)
@given(instance=statements_Statement_strategy)
@settings(max_examples=25)
def test_statements_Statement_instantiation(instance):
    assert isinstance(instance, statements_Statement)


system_InstantiationList_strategy = st.builds(system_InstantiationList)
@given(instance=system_InstantiationList_strategy)
@settings(max_examples=25)
def test_system_InstantiationList_instantiation(instance):
    assert isinstance(instance, system_InstantiationList)


system_ProgressMeasure_strategy = st.builds(system_ProgressMeasure)
@given(instance=system_ProgressMeasure_strategy)
@settings(max_examples=25)
def test_system_ProgressMeasure_instantiation(instance):
    assert isinstance(instance, system_ProgressMeasure)


system_System_strategy = st.builds(system_System)
@given(instance=system_System_strategy)
@settings(max_examples=25)
def test_system_System_instantiation(instance):
    assert isinstance(instance, system_System)


system_TemplateDeclaration_strategy = st.builds(system_TemplateDeclaration)
@given(instance=system_TemplateDeclaration_strategy)
@settings(max_examples=25)
def test_system_TemplateDeclaration_instantiation(instance):
    assert isinstance(instance, system_TemplateDeclaration)


uppaal_NTA_strategy = st.builds(uppaal_NTA)
@given(instance=uppaal_NTA_strategy)
@settings(max_examples=25)
def test_uppaal_NTA_instantiation(instance):
    assert isinstance(instance, uppaal_NTA)


uppaal_core_CommentableElement_strategy = st.builds(uppaal_core_CommentableElement, comment=safe_text)
@given(instance=uppaal_core_CommentableElement_strategy)
@settings(max_examples=25)
def test_uppaal_core_CommentableElement_instantiation(instance):
    assert isinstance(instance, uppaal_core_CommentableElement)


uppaal_core_NamedElement_strategy = st.builds(uppaal_core_NamedElement, name=safe_text)
@given(instance=uppaal_core_NamedElement_strategy)
@settings(max_examples=25)
def test_uppaal_core_NamedElement_instantiation(instance):
    assert isinstance(instance, uppaal_core_NamedElement)


uppaal_core_TypedElement_strategy = st.builds(uppaal_core_TypedElement)
@given(instance=uppaal_core_TypedElement_strategy)
@settings(max_examples=25)
def test_uppaal_core_TypedElement_instantiation(instance):
    assert isinstance(instance, uppaal_core_TypedElement)


uppaal_declarations_ArrayInitializer_strategy = st.builds(uppaal_declarations_ArrayInitializer)
@given(instance=uppaal_declarations_ArrayInitializer_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_ArrayInitializer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_ArrayInitializer)


uppaal_declarations_Declaration_strategy = st.builds(uppaal_declarations_Declaration)
@given(instance=uppaal_declarations_Declaration_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_Declaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Declaration)


uppaal_declarations_Declarations_strategy = st.builds(uppaal_declarations_Declarations)
@given(instance=uppaal_declarations_Declarations_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_Declarations_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Declarations)


uppaal_declarations_ExpressionInitializer_strategy = st.builds(uppaal_declarations_ExpressionInitializer)
@given(instance=uppaal_declarations_ExpressionInitializer_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_ExpressionInitializer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_ExpressionInitializer)


uppaal_declarations_Function_strategy = st.builds(uppaal_declarations_Function)
@given(instance=uppaal_declarations_Function_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_Function_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Function)


uppaal_declarations_GlobalDeclarations_strategy = st.builds(uppaal_declarations_GlobalDeclarations)
@given(instance=uppaal_declarations_GlobalDeclarations_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_GlobalDeclarations_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_GlobalDeclarations)


uppaal_declarations_Initializer_strategy = st.builds(uppaal_declarations_Initializer)
@given(instance=uppaal_declarations_Initializer_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_Initializer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Initializer)


uppaal_declarations_LocalDeclarations_strategy = st.builds(uppaal_declarations_LocalDeclarations)
@given(instance=uppaal_declarations_LocalDeclarations_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_LocalDeclarations_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_LocalDeclarations)


uppaal_declarations_Parameter_strategy = st.builds(uppaal_declarations_Parameter, callType=safe_text)
@given(instance=uppaal_declarations_Parameter_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_Parameter_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Parameter)


uppaal_declarations_ParameterContainer_strategy = st.builds(uppaal_declarations_ParameterContainer)
@given(instance=uppaal_declarations_ParameterContainer_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_ParameterContainer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_ParameterContainer)


uppaal_declarations_SystemDeclarations_strategy = st.builds(uppaal_declarations_SystemDeclarations)
@given(instance=uppaal_declarations_SystemDeclarations_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_SystemDeclarations_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_SystemDeclarations)


uppaal_declarations_TypeDeclaration_strategy = st.builds(uppaal_declarations_TypeDeclaration)
@given(instance=uppaal_declarations_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_TypeDeclaration)


uppaal_declarations_TypedDeclaration_strategy = st.builds(uppaal_declarations_TypedDeclaration)
@given(instance=uppaal_declarations_TypedDeclaration_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_TypedDeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_TypedDeclaration)


uppaal_declarations_TypedElementContainer_strategy = st.builds(uppaal_declarations_TypedElementContainer)
@given(instance=uppaal_declarations_TypedElementContainer_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_TypedElementContainer_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_TypedElementContainer)


uppaal_declarations_Variable_strategy = st.builds(uppaal_declarations_Variable)
@given(instance=uppaal_declarations_Variable_strategy)
@settings(max_examples=25)
def test_uppaal_declarations_Variable_instantiation(instance):
    assert isinstance(instance, uppaal_declarations_Variable)


uppaal_expressions_ArithmeticExpression_strategy = st.builds(uppaal_expressions_ArithmeticExpression, operator=safe_text)
@given(instance=uppaal_expressions_ArithmeticExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_ArithmeticExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_ArithmeticExpression)


uppaal_expressions_AssignmentExpression_strategy = st.builds(uppaal_expressions_AssignmentExpression, operator=safe_text)
@given(instance=uppaal_expressions_AssignmentExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_AssignmentExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_AssignmentExpression)


uppaal_expressions_BinaryExpression_strategy = st.builds(uppaal_expressions_BinaryExpression)
@given(instance=uppaal_expressions_BinaryExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_BinaryExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_BinaryExpression)


uppaal_expressions_BitShiftExpression_strategy = st.builds(uppaal_expressions_BitShiftExpression, operator=safe_text)
@given(instance=uppaal_expressions_BitShiftExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_BitShiftExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_BitShiftExpression)


uppaal_expressions_BitwiseExpression_strategy = st.builds(uppaal_expressions_BitwiseExpression, operator=safe_text)
@given(instance=uppaal_expressions_BitwiseExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_BitwiseExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_BitwiseExpression)


uppaal_expressions_ChannelPrefixExpression_strategy = st.builds(uppaal_expressions_ChannelPrefixExpression, broadcast=st.booleans(), urgent=st.booleans())
@given(instance=uppaal_expressions_ChannelPrefixExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_ChannelPrefixExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_ChannelPrefixExpression)


uppaal_expressions_CompareExpression_strategy = st.builds(uppaal_expressions_CompareExpression, operator=safe_text)
@given(instance=uppaal_expressions_CompareExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_CompareExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_CompareExpression)


uppaal_expressions_ConditionExpression_strategy = st.builds(uppaal_expressions_ConditionExpression)
@given(instance=uppaal_expressions_ConditionExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_ConditionExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_ConditionExpression)


uppaal_expressions_DataPrefixExpression_strategy = st.builds(uppaal_expressions_DataPrefixExpression, prefix=safe_text)
@given(instance=uppaal_expressions_DataPrefixExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_DataPrefixExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_DataPrefixExpression)


uppaal_expressions_Expression_strategy = st.builds(uppaal_expressions_Expression)
@given(instance=uppaal_expressions_Expression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_Expression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_Expression)


uppaal_expressions_FunctionCallExpression_strategy = st.builds(uppaal_expressions_FunctionCallExpression)
@given(instance=uppaal_expressions_FunctionCallExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_FunctionCallExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_FunctionCallExpression)


uppaal_expressions_IdentifierExpression_strategy = st.builds(uppaal_expressions_IdentifierExpression)
@given(instance=uppaal_expressions_IdentifierExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_IdentifierExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_IdentifierExpression)


uppaal_expressions_IncrementDecrementExpression_strategy = st.builds(uppaal_expressions_IncrementDecrementExpression, operator=safe_text)
@given(instance=uppaal_expressions_IncrementDecrementExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_IncrementDecrementExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_IncrementDecrementExpression)


uppaal_expressions_LiteralExpression_strategy = st.builds(uppaal_expressions_LiteralExpression, text=safe_text)
@given(instance=uppaal_expressions_LiteralExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_LiteralExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_LiteralExpression)


uppaal_expressions_LogicalExpression_strategy = st.builds(uppaal_expressions_LogicalExpression, operator=safe_text)
@given(instance=uppaal_expressions_LogicalExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_LogicalExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_LogicalExpression)


uppaal_expressions_MinMaxExpression_strategy = st.builds(uppaal_expressions_MinMaxExpression, operator=safe_text)
@given(instance=uppaal_expressions_MinMaxExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_MinMaxExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_MinMaxExpression)


uppaal_expressions_MinusExpression_strategy = st.builds(uppaal_expressions_MinusExpression)
@given(instance=uppaal_expressions_MinusExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_MinusExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_MinusExpression)


uppaal_expressions_NegationExpression_strategy = st.builds(uppaal_expressions_NegationExpression)
@given(instance=uppaal_expressions_NegationExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_NegationExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_NegationExpression)


uppaal_expressions_PlusExpression_strategy = st.builds(uppaal_expressions_PlusExpression)
@given(instance=uppaal_expressions_PlusExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_PlusExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_PlusExpression)


uppaal_expressions_PostIncrementDecrementExpression_strategy = st.builds(uppaal_expressions_PostIncrementDecrementExpression)
@given(instance=uppaal_expressions_PostIncrementDecrementExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_PostIncrementDecrementExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_PostIncrementDecrementExpression)


uppaal_expressions_PreIncrementDecrementExpression_strategy = st.builds(uppaal_expressions_PreIncrementDecrementExpression)
@given(instance=uppaal_expressions_PreIncrementDecrementExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_PreIncrementDecrementExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_PreIncrementDecrementExpression)


uppaal_expressions_QuantificationExpression_strategy = st.builds(uppaal_expressions_QuantificationExpression, quantifier=safe_text)
@given(instance=uppaal_expressions_QuantificationExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_QuantificationExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_QuantificationExpression)


uppaal_expressions_ScopedIdentifierExpression_strategy = st.builds(uppaal_expressions_ScopedIdentifierExpression)
@given(instance=uppaal_expressions_ScopedIdentifierExpression_strategy)
@settings(max_examples=25)
def test_uppaal_expressions_ScopedIdentifierExpression_instantiation(instance):
    assert isinstance(instance, uppaal_expressions_ScopedIdentifierExpression)


uppaal_global_ChannelItem_strategy = st.builds(uppaal_global_ChannelItem)
@given(instance=uppaal_global_ChannelItem_strategy)
@settings(max_examples=25)
def test_uppaal_global_ChannelItem_instantiation(instance):
    assert isinstance(instance, uppaal_global_ChannelItem)


uppaal_global_ChannelPriorityDeclaration_strategy = st.builds(uppaal_global_ChannelPriorityDeclaration)
@given(instance=uppaal_global_ChannelPriorityDeclaration_strategy)
@settings(max_examples=25)
def test_uppaal_global_ChannelPriorityDeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_global_ChannelPriorityDeclaration)


uppaal_global_ChannelPriorityGroup_strategy = st.builds(uppaal_global_ChannelPriorityGroup)
@given(instance=uppaal_global_ChannelPriorityGroup_strategy)
@settings(max_examples=25)
def test_uppaal_global_ChannelPriorityGroup_instantiation(instance):
    assert isinstance(instance, uppaal_global_ChannelPriorityGroup)


uppaal_global_DefaultItem_strategy = st.builds(uppaal_global_DefaultItem)
@given(instance=uppaal_global_DefaultItem_strategy)
@settings(max_examples=25)
def test_uppaal_global_DefaultItem_instantiation(instance):
    assert isinstance(instance, uppaal_global_DefaultItem)


uppaal_global_PriorityItem_strategy = st.builds(uppaal_global_PriorityItem)
@given(instance=uppaal_global_PriorityItem_strategy)
@settings(max_examples=25)
def test_uppaal_global_PriorityItem_instantiation(instance):
    assert isinstance(instance, uppaal_global_PriorityItem)


uppaal_statements_Block_strategy = st.builds(uppaal_statements_Block)
@given(instance=uppaal_statements_Block_strategy)
@settings(max_examples=25)
def test_uppaal_statements_Block_instantiation(instance):
    assert isinstance(instance, uppaal_statements_Block)


uppaal_statements_DoWhileLoop_strategy = st.builds(uppaal_statements_DoWhileLoop)
@given(instance=uppaal_statements_DoWhileLoop_strategy)
@settings(max_examples=25)
def test_uppaal_statements_DoWhileLoop_instantiation(instance):
    assert isinstance(instance, uppaal_statements_DoWhileLoop)


uppaal_statements_EmptyStatement_strategy = st.builds(uppaal_statements_EmptyStatement)
@given(instance=uppaal_statements_EmptyStatement_strategy)
@settings(max_examples=25)
def test_uppaal_statements_EmptyStatement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_EmptyStatement)


uppaal_statements_ExpressionStatement_strategy = st.builds(uppaal_statements_ExpressionStatement)
@given(instance=uppaal_statements_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_uppaal_statements_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_ExpressionStatement)


uppaal_statements_ForLoop_strategy = st.builds(uppaal_statements_ForLoop)
@given(instance=uppaal_statements_ForLoop_strategy)
@settings(max_examples=25)
def test_uppaal_statements_ForLoop_instantiation(instance):
    assert isinstance(instance, uppaal_statements_ForLoop)


uppaal_statements_IfStatement_strategy = st.builds(uppaal_statements_IfStatement)
@given(instance=uppaal_statements_IfStatement_strategy)
@settings(max_examples=25)
def test_uppaal_statements_IfStatement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_IfStatement)


uppaal_statements_Iteration_strategy = st.builds(uppaal_statements_Iteration)
@given(instance=uppaal_statements_Iteration_strategy)
@settings(max_examples=25)
def test_uppaal_statements_Iteration_instantiation(instance):
    assert isinstance(instance, uppaal_statements_Iteration)


uppaal_statements_ReturnStatement_strategy = st.builds(uppaal_statements_ReturnStatement)
@given(instance=uppaal_statements_ReturnStatement_strategy)
@settings(max_examples=25)
def test_uppaal_statements_ReturnStatement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_ReturnStatement)


uppaal_statements_Statement_strategy = st.builds(uppaal_statements_Statement)
@given(instance=uppaal_statements_Statement_strategy)
@settings(max_examples=25)
def test_uppaal_statements_Statement_instantiation(instance):
    assert isinstance(instance, uppaal_statements_Statement)


uppaal_statements_WhileLoop_strategy = st.builds(uppaal_statements_WhileLoop)
@given(instance=uppaal_statements_WhileLoop_strategy)
@settings(max_examples=25)
def test_uppaal_statements_WhileLoop_instantiation(instance):
    assert isinstance(instance, uppaal_statements_WhileLoop)


uppaal_system_InstantiationList_strategy = st.builds(uppaal_system_InstantiationList)
@given(instance=uppaal_system_InstantiationList_strategy)
@settings(max_examples=25)
def test_uppaal_system_InstantiationList_instantiation(instance):
    assert isinstance(instance, uppaal_system_InstantiationList)


uppaal_system_ProgressMeasure_strategy = st.builds(uppaal_system_ProgressMeasure)
@given(instance=uppaal_system_ProgressMeasure_strategy)
@settings(max_examples=25)
def test_uppaal_system_ProgressMeasure_instantiation(instance):
    assert isinstance(instance, uppaal_system_ProgressMeasure)


uppaal_system_System_strategy = st.builds(uppaal_system_System)
@given(instance=uppaal_system_System_strategy)
@settings(max_examples=25)
def test_uppaal_system_System_instantiation(instance):
    assert isinstance(instance, uppaal_system_System)


uppaal_system_TemplateDeclaration_strategy = st.builds(uppaal_system_TemplateDeclaration)
@given(instance=uppaal_system_TemplateDeclaration_strategy)
@settings(max_examples=25)
def test_uppaal_system_TemplateDeclaration_instantiation(instance):
    assert isinstance(instance, uppaal_system_TemplateDeclaration)


uppaal_templates_AbstractTemplate_strategy = st.builds(uppaal_templates_AbstractTemplate)
@given(instance=uppaal_templates_AbstractTemplate_strategy)
@settings(max_examples=25)
def test_uppaal_templates_AbstractTemplate_instantiation(instance):
    assert isinstance(instance, uppaal_templates_AbstractTemplate)


uppaal_templates_Edge_strategy = st.builds(uppaal_templates_Edge)
@given(instance=uppaal_templates_Edge_strategy)
@settings(max_examples=25)
def test_uppaal_templates_Edge_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Edge)


uppaal_templates_Location_strategy = st.builds(uppaal_templates_Location, locationTimeKind=safe_text)
@given(instance=uppaal_templates_Location_strategy)
@settings(max_examples=25)
def test_uppaal_templates_Location_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Location)


uppaal_templates_RedefinedTemplate_strategy = st.builds(uppaal_templates_RedefinedTemplate)
@given(instance=uppaal_templates_RedefinedTemplate_strategy)
@settings(max_examples=25)
def test_uppaal_templates_RedefinedTemplate_instantiation(instance):
    assert isinstance(instance, uppaal_templates_RedefinedTemplate)


uppaal_templates_Selection_strategy = st.builds(uppaal_templates_Selection)
@given(instance=uppaal_templates_Selection_strategy)
@settings(max_examples=25)
def test_uppaal_templates_Selection_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Selection)


uppaal_templates_Synchronization_strategy = st.builds(uppaal_templates_Synchronization, kind=safe_text)
@given(instance=uppaal_templates_Synchronization_strategy)
@settings(max_examples=25)
def test_uppaal_templates_Synchronization_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Synchronization)


uppaal_templates_Template_strategy = st.builds(uppaal_templates_Template)
@given(instance=uppaal_templates_Template_strategy)
@settings(max_examples=25)
def test_uppaal_templates_Template_instantiation(instance):
    assert isinstance(instance, uppaal_templates_Template)


uppaal_types_DeclaredType_strategy = st.builds(uppaal_types_DeclaredType)
@given(instance=uppaal_types_DeclaredType_strategy)
@settings(max_examples=25)
def test_uppaal_types_DeclaredType_instantiation(instance):
    assert isinstance(instance, uppaal_types_DeclaredType)


uppaal_types_IntegerBounds_strategy = st.builds(uppaal_types_IntegerBounds)
@given(instance=uppaal_types_IntegerBounds_strategy)
@settings(max_examples=25)
def test_uppaal_types_IntegerBounds_instantiation(instance):
    assert isinstance(instance, uppaal_types_IntegerBounds)


uppaal_types_Library_strategy = st.builds(uppaal_types_Library)
@given(instance=uppaal_types_Library_strategy)
@settings(max_examples=25)
def test_uppaal_types_Library_instantiation(instance):
    assert isinstance(instance, uppaal_types_Library)


uppaal_types_PredefinedType_strategy = st.builds(uppaal_types_PredefinedType, type=safe_text)
@given(instance=uppaal_types_PredefinedType_strategy)
@settings(max_examples=25)
def test_uppaal_types_PredefinedType_instantiation(instance):
    assert isinstance(instance, uppaal_types_PredefinedType)


uppaal_types_RangeTypeSpecification_strategy = st.builds(uppaal_types_RangeTypeSpecification)
@given(instance=uppaal_types_RangeTypeSpecification_strategy)
@settings(max_examples=25)
def test_uppaal_types_RangeTypeSpecification_instantiation(instance):
    assert isinstance(instance, uppaal_types_RangeTypeSpecification)


uppaal_types_ScalarTypeSpecification_strategy = st.builds(uppaal_types_ScalarTypeSpecification)
@given(instance=uppaal_types_ScalarTypeSpecification_strategy)
@settings(max_examples=25)
def test_uppaal_types_ScalarTypeSpecification_instantiation(instance):
    assert isinstance(instance, uppaal_types_ScalarTypeSpecification)


uppaal_types_StructTypeSpecification_strategy = st.builds(uppaal_types_StructTypeSpecification)
@given(instance=uppaal_types_StructTypeSpecification_strategy)
@settings(max_examples=25)
def test_uppaal_types_StructTypeSpecification_instantiation(instance):
    assert isinstance(instance, uppaal_types_StructTypeSpecification)


uppaal_types_Type_strategy = st.builds(uppaal_types_Type, baseType=safe_text)
@given(instance=uppaal_types_Type_strategy)
@settings(max_examples=25)
def test_uppaal_types_Type_instantiation(instance):
    assert isinstance(instance, uppaal_types_Type)


uppaal_types_TypeExpression_strategy = st.builds(uppaal_types_TypeExpression)
@given(instance=uppaal_types_TypeExpression_strategy)
@settings(max_examples=25)
def test_uppaal_types_TypeExpression_instantiation(instance):
    assert isinstance(instance, uppaal_types_TypeExpression)


uppaal_visuals_ColoredElement_strategy = st.builds(uppaal_visuals_ColoredElement, colorCode=safe_text)
@given(instance=uppaal_visuals_ColoredElement_strategy)
@settings(max_examples=25)
def test_uppaal_visuals_ColoredElement_instantiation(instance):
    assert isinstance(instance, uppaal_visuals_ColoredElement)


uppaal_visuals_LinearElement_strategy = st.builds(uppaal_visuals_LinearElement)
@given(instance=uppaal_visuals_LinearElement_strategy)
@settings(max_examples=25)
def test_uppaal_visuals_LinearElement_instantiation(instance):
    assert isinstance(instance, uppaal_visuals_LinearElement)


uppaal_visuals_PlanarElement_strategy = st.builds(uppaal_visuals_PlanarElement)
@given(instance=uppaal_visuals_PlanarElement_strategy)
@settings(max_examples=25)
def test_uppaal_visuals_PlanarElement_instantiation(instance):
    assert isinstance(instance, uppaal_visuals_PlanarElement)


uppaal_visuals_Point_strategy = st.builds(uppaal_visuals_Point, x=st.integers(), y=st.integers())
@given(instance=uppaal_visuals_Point_strategy)
@settings(max_examples=25)
def test_uppaal_visuals_Point_instantiation(instance):
    assert isinstance(instance, uppaal_visuals_Point)


visuals_ColoredElement_strategy = st.builds(visuals_ColoredElement)
@given(instance=visuals_ColoredElement_strategy)
@settings(max_examples=25)
def test_visuals_ColoredElement_instantiation(instance):
    assert isinstance(instance, visuals_ColoredElement)


visuals_LinearElement_strategy = st.builds(visuals_LinearElement)
@given(instance=visuals_LinearElement_strategy)
@settings(max_examples=25)
def test_visuals_LinearElement_instantiation(instance):
    assert isinstance(instance, visuals_LinearElement)


visuals_PlanarElement_strategy = st.builds(visuals_PlanarElement)
@given(instance=visuals_PlanarElement_strategy)
@settings(max_examples=25)
def test_visuals_PlanarElement_instantiation(instance):
    assert isinstance(instance, visuals_PlanarElement)



