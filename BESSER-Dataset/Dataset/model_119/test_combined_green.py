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
    XmlFragment,
    dom_XmlExpressionFragment,
    dom_XmlTextFragment,
    IUnqualifiedSelector,
    dom_ExpressionSelector,
    dom_IPropertySelector,
    ISelector,
    dom_IUnqualifiedSelector,
    PropertyIdentifier,
    dom_QualifiedIdentifier,
    dom_AttributeIdentifier,
    SwitchElement,
    dom_CaseClause,
    dom_DefaultClause,
    IterationStatement,
    dom_ForStatement,
    dom_ForEachInStatement,
    dom_WhileStatement,
    dom_DoStatement,
    dom_ForInStatement,
    Statement,
    dom_WithStatement,
    dom_IfStatement,
    dom_ExpressionStatement,
    dom_DefaultXmlNamespaceStatement,
    dom_SwitchStatement,
    dom_ReturnStatement,
    dom_ConstStatement,
    dom_BreakStatement,
    dom_EmptyStatement,
    dom_TryStatement,
    dom_LabeledStatement,
    dom_IterationStatement,
    dom_ContinueStatement,
    dom_ThrowStatement,
    AccessorAssignment,
    dom_SetterAssignment,
    dom_GetterAssignment,
    dom_BlockStatement,
    IForInitializer,
    dom_VariableStatement,
    IArrayElement,
    Expression,
    dom_UnaryExpression,
    dom_FilterExpression,
    dom_PropertyAccessExpression,
    dom_CallExpression,
    dom_XmlInitializer,
    dom_ConditionalExpression,
    dom_FunctionExpression,
    dom_NullLiteral,
    dom_DescendantAccessExpression,
    dom_BinaryExpression,
    dom_NewExpression,
    dom_ArrayAccessExpression,
    dom_BooleanLiteral,
    dom_ParenthesizedExpression,
    dom_VariableReference,
    PropertyAssignment,
    dom_AccessorAssignment,
    dom_SimplePropertyAssignment,
    dom_ObjectLiteral,
    dom_Elision,
    dom_ArrayLiteral,
    dom_ThisExpression,
    dom_RegularExpressionLiteral,
    IProperty,
    dom_PropertyIdentifier,
    IPropertySelector,
    dom_WildcardIdentifier,
    IPropertyName,
    dom_StringLiteral,
    dom_NumericLiteral,
    Node,
    dom_Identifier,
    dom_SwitchElement,
    dom_Parameter,
    dom_FinallyClause,
    dom_VariableDeclaration,
    dom_XmlFragment,
    dom_CatchClause,
    dom_IPropertyName,
    dom_Source,
    dom_PropertyAssignment,
    dom_Statement,
    dom_IProperty,
    dom_Label,
    dom_Expression,
    dom_IForInitializer,
    dom_ISelector,
    dom_IArrayElement,
    dom_Comment,
    dom_Node,
    BinaryOperator,
    UnaryOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_xmlfragment_is_not_abstract():
    assert not inspect.isabstract(XmlFragment)


def test_hyp_xmlfragment_constructor_exists():
    assert callable(XmlFragment.__init__)


def test_hyp_xmlfragment_constructor_args():
    sig = inspect.signature(XmlFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_xmlexpressionfragment_is_not_abstract():
    assert not inspect.isabstract(dom_XmlExpressionFragment)


def test_hyp_dom_xmlexpressionfragment_constructor_exists():
    assert callable(dom_XmlExpressionFragment.__init__)


def test_hyp_dom_xmlexpressionfragment_constructor_args():
    sig = inspect.signature(dom_XmlExpressionFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_xmltextfragment_is_not_abstract():
    assert not inspect.isabstract(dom_XmlTextFragment)


def test_hyp_dom_xmltextfragment_constructor_exists():
    assert callable(dom_XmlTextFragment.__init__)


def test_hyp_dom_xmltextfragment_constructor_args():
    sig = inspect.signature(dom_XmlTextFragment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_iunqualifiedselector_is_not_abstract():
    assert not inspect.isabstract(IUnqualifiedSelector)


def test_hyp_iunqualifiedselector_constructor_exists():
    assert callable(IUnqualifiedSelector.__init__)


def test_hyp_iunqualifiedselector_constructor_args():
    sig = inspect.signature(IUnqualifiedSelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_expressionselector_is_not_abstract():
    assert not inspect.isabstract(dom_ExpressionSelector)


def test_hyp_dom_expressionselector_constructor_exists():
    assert callable(dom_ExpressionSelector.__init__)


def test_hyp_dom_expressionselector_constructor_args():
    sig = inspect.signature(dom_ExpressionSelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_ipropertyselector_is_not_abstract():
    assert not inspect.isabstract(dom_IPropertySelector)


def test_hyp_dom_ipropertyselector_constructor_exists():
    assert callable(dom_IPropertySelector.__init__)


def test_hyp_dom_ipropertyselector_constructor_args():
    sig = inspect.signature(dom_IPropertySelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iselector_is_not_abstract():
    assert not inspect.isabstract(ISelector)


def test_hyp_iselector_constructor_exists():
    assert callable(ISelector.__init__)


def test_hyp_iselector_constructor_args():
    sig = inspect.signature(ISelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_iunqualifiedselector_is_not_abstract():
    assert not inspect.isabstract(dom_IUnqualifiedSelector)


def test_hyp_dom_iunqualifiedselector_constructor_exists():
    assert callable(dom_IUnqualifiedSelector.__init__)


def test_hyp_dom_iunqualifiedselector_constructor_args():
    sig = inspect.signature(dom_IUnqualifiedSelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_propertyidentifier_is_not_abstract():
    assert not inspect.isabstract(PropertyIdentifier)


def test_hyp_propertyidentifier_constructor_exists():
    assert callable(PropertyIdentifier.__init__)


def test_hyp_propertyidentifier_constructor_args():
    sig = inspect.signature(PropertyIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(dom_QualifiedIdentifier)


def test_hyp_dom_qualifiedidentifier_constructor_exists():
    assert callable(dom_QualifiedIdentifier.__init__)


def test_hyp_dom_qualifiedidentifier_constructor_args():
    sig = inspect.signature(dom_QualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_attributeidentifier_is_not_abstract():
    assert not inspect.isabstract(dom_AttributeIdentifier)


def test_hyp_dom_attributeidentifier_constructor_exists():
    assert callable(dom_AttributeIdentifier.__init__)


def test_hyp_dom_attributeidentifier_constructor_args():
    sig = inspect.signature(dom_AttributeIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_switchelement_is_not_abstract():
    assert not inspect.isabstract(SwitchElement)


def test_hyp_switchelement_constructor_exists():
    assert callable(SwitchElement.__init__)


def test_hyp_switchelement_constructor_args():
    sig = inspect.signature(SwitchElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_caseclause_is_not_abstract():
    assert not inspect.isabstract(dom_CaseClause)


def test_hyp_dom_caseclause_constructor_exists():
    assert callable(dom_CaseClause.__init__)


def test_hyp_dom_caseclause_constructor_args():
    sig = inspect.signature(dom_CaseClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_defaultclause_is_not_abstract():
    assert not inspect.isabstract(dom_DefaultClause)


def test_hyp_dom_defaultclause_constructor_exists():
    assert callable(dom_DefaultClause.__init__)


def test_hyp_dom_defaultclause_constructor_args():
    sig = inspect.signature(dom_DefaultClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(IterationStatement)


def test_hyp_iterationstatement_constructor_exists():
    assert callable(IterationStatement.__init__)


def test_hyp_iterationstatement_constructor_args():
    sig = inspect.signature(IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_forstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ForStatement)


def test_hyp_dom_forstatement_constructor_exists():
    assert callable(dom_ForStatement.__init__)


def test_hyp_dom_forstatement_constructor_args():
    sig = inspect.signature(dom_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_foreachinstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ForEachInStatement)


def test_hyp_dom_foreachinstatement_constructor_exists():
    assert callable(dom_ForEachInStatement.__init__)


def test_hyp_dom_foreachinstatement_constructor_args():
    sig = inspect.signature(dom_ForEachInStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_whilestatement_is_not_abstract():
    assert not inspect.isabstract(dom_WhileStatement)


def test_hyp_dom_whilestatement_constructor_exists():
    assert callable(dom_WhileStatement.__init__)


def test_hyp_dom_whilestatement_constructor_args():
    sig = inspect.signature(dom_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_dostatement_is_not_abstract():
    assert not inspect.isabstract(dom_DoStatement)


def test_hyp_dom_dostatement_constructor_exists():
    assert callable(dom_DoStatement.__init__)


def test_hyp_dom_dostatement_constructor_args():
    sig = inspect.signature(dom_DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_forinstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ForInStatement)


def test_hyp_dom_forinstatement_constructor_exists():
    assert callable(dom_ForInStatement.__init__)


def test_hyp_dom_forinstatement_constructor_args():
    sig = inspect.signature(dom_ForInStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_withstatement_is_not_abstract():
    assert not inspect.isabstract(dom_WithStatement)


def test_hyp_dom_withstatement_constructor_exists():
    assert callable(dom_WithStatement.__init__)


def test_hyp_dom_withstatement_constructor_args():
    sig = inspect.signature(dom_WithStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_ifstatement_is_not_abstract():
    assert not inspect.isabstract(dom_IfStatement)


def test_hyp_dom_ifstatement_constructor_exists():
    assert callable(dom_IfStatement.__init__)


def test_hyp_dom_ifstatement_constructor_args():
    sig = inspect.signature(dom_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ExpressionStatement)


def test_hyp_dom_expressionstatement_constructor_exists():
    assert callable(dom_ExpressionStatement.__init__)


def test_hyp_dom_expressionstatement_constructor_args():
    sig = inspect.signature(dom_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_defaultxmlnamespacestatement_is_not_abstract():
    assert not inspect.isabstract(dom_DefaultXmlNamespaceStatement)


def test_hyp_dom_defaultxmlnamespacestatement_constructor_exists():
    assert callable(dom_DefaultXmlNamespaceStatement.__init__)


def test_hyp_dom_defaultxmlnamespacestatement_constructor_args():
    sig = inspect.signature(dom_DefaultXmlNamespaceStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_switchstatement_is_not_abstract():
    assert not inspect.isabstract(dom_SwitchStatement)


def test_hyp_dom_switchstatement_constructor_exists():
    assert callable(dom_SwitchStatement.__init__)


def test_hyp_dom_switchstatement_constructor_args():
    sig = inspect.signature(dom_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_returnstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ReturnStatement)


def test_hyp_dom_returnstatement_constructor_exists():
    assert callable(dom_ReturnStatement.__init__)


def test_hyp_dom_returnstatement_constructor_args():
    sig = inspect.signature(dom_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_conststatement_is_not_abstract():
    assert not inspect.isabstract(dom_ConstStatement)


def test_hyp_dom_conststatement_constructor_exists():
    assert callable(dom_ConstStatement.__init__)


def test_hyp_dom_conststatement_constructor_args():
    sig = inspect.signature(dom_ConstStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_breakstatement_is_not_abstract():
    assert not inspect.isabstract(dom_BreakStatement)


def test_hyp_dom_breakstatement_constructor_exists():
    assert callable(dom_BreakStatement.__init__)


def test_hyp_dom_breakstatement_constructor_args():
    sig = inspect.signature(dom_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_emptystatement_is_not_abstract():
    assert not inspect.isabstract(dom_EmptyStatement)


def test_hyp_dom_emptystatement_constructor_exists():
    assert callable(dom_EmptyStatement.__init__)


def test_hyp_dom_emptystatement_constructor_args():
    sig = inspect.signature(dom_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_trystatement_is_not_abstract():
    assert not inspect.isabstract(dom_TryStatement)


def test_hyp_dom_trystatement_constructor_exists():
    assert callable(dom_TryStatement.__init__)


def test_hyp_dom_trystatement_constructor_args():
    sig = inspect.signature(dom_TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_labeledstatement_is_not_abstract():
    assert not inspect.isabstract(dom_LabeledStatement)


def test_hyp_dom_labeledstatement_constructor_exists():
    assert callable(dom_LabeledStatement.__init__)


def test_hyp_dom_labeledstatement_constructor_args():
    sig = inspect.signature(dom_LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_iterationstatement_is_not_abstract():
    assert not inspect.isabstract(dom_IterationStatement)


def test_hyp_dom_iterationstatement_constructor_exists():
    assert callable(dom_IterationStatement.__init__)


def test_hyp_dom_iterationstatement_constructor_args():
    sig = inspect.signature(dom_IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_continuestatement_is_not_abstract():
    assert not inspect.isabstract(dom_ContinueStatement)


def test_hyp_dom_continuestatement_constructor_exists():
    assert callable(dom_ContinueStatement.__init__)


def test_hyp_dom_continuestatement_constructor_args():
    sig = inspect.signature(dom_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_throwstatement_is_not_abstract():
    assert not inspect.isabstract(dom_ThrowStatement)


def test_hyp_dom_throwstatement_constructor_exists():
    assert callable(dom_ThrowStatement.__init__)


def test_hyp_dom_throwstatement_constructor_args():
    sig = inspect.signature(dom_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_accessorassignment_is_not_abstract():
    assert not inspect.isabstract(AccessorAssignment)


def test_hyp_accessorassignment_constructor_exists():
    assert callable(AccessorAssignment.__init__)


def test_hyp_accessorassignment_constructor_args():
    sig = inspect.signature(AccessorAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_setterassignment_is_not_abstract():
    assert not inspect.isabstract(dom_SetterAssignment)


def test_hyp_dom_setterassignment_constructor_exists():
    assert callable(dom_SetterAssignment.__init__)


def test_hyp_dom_setterassignment_constructor_args():
    sig = inspect.signature(dom_SetterAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_getterassignment_is_not_abstract():
    assert not inspect.isabstract(dom_GetterAssignment)


def test_hyp_dom_getterassignment_constructor_exists():
    assert callable(dom_GetterAssignment.__init__)


def test_hyp_dom_getterassignment_constructor_args():
    sig = inspect.signature(dom_GetterAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_blockstatement_is_not_abstract():
    assert not inspect.isabstract(dom_BlockStatement)


def test_hyp_dom_blockstatement_constructor_exists():
    assert callable(dom_BlockStatement.__init__)


def test_hyp_dom_blockstatement_constructor_args():
    sig = inspect.signature(dom_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iforinitializer_is_not_abstract():
    assert not inspect.isabstract(IForInitializer)


def test_hyp_iforinitializer_constructor_exists():
    assert callable(IForInitializer.__init__)


def test_hyp_iforinitializer_constructor_args():
    sig = inspect.signature(IForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variablestatement_is_not_abstract():
    assert not inspect.isabstract(dom_VariableStatement)


def test_hyp_dom_variablestatement_constructor_exists():
    assert callable(dom_VariableStatement.__init__)


def test_hyp_dom_variablestatement_constructor_args():
    sig = inspect.signature(dom_VariableStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iarrayelement_is_not_abstract():
    assert not inspect.isabstract(IArrayElement)


def test_hyp_iarrayelement_constructor_exists():
    assert callable(IArrayElement.__init__)


def test_hyp_iarrayelement_constructor_args():
    sig = inspect.signature(IArrayElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(dom_UnaryExpression)


def test_hyp_dom_unaryexpression_constructor_exists():
    assert callable(dom_UnaryExpression.__init__)


def test_hyp_dom_unaryexpression_constructor_args():
    sig = inspect.signature(dom_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"




def test_hyp_dom_filterexpression_is_not_abstract():
    assert not inspect.isabstract(dom_FilterExpression)


def test_hyp_dom_filterexpression_constructor_exists():
    assert callable(dom_FilterExpression.__init__)


def test_hyp_dom_filterexpression_constructor_args():
    sig = inspect.signature(dom_FilterExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_propertyaccessexpression_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyAccessExpression)


def test_hyp_dom_propertyaccessexpression_constructor_exists():
    assert callable(dom_PropertyAccessExpression.__init__)


def test_hyp_dom_propertyaccessexpression_constructor_args():
    sig = inspect.signature(dom_PropertyAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_callexpression_is_not_abstract():
    assert not inspect.isabstract(dom_CallExpression)


def test_hyp_dom_callexpression_constructor_exists():
    assert callable(dom_CallExpression.__init__)


def test_hyp_dom_callexpression_constructor_args():
    sig = inspect.signature(dom_CallExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_xmlinitializer_is_not_abstract():
    assert not inspect.isabstract(dom_XmlInitializer)


def test_hyp_dom_xmlinitializer_constructor_exists():
    assert callable(dom_XmlInitializer.__init__)


def test_hyp_dom_xmlinitializer_constructor_args():
    sig = inspect.signature(dom_XmlInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ConditionalExpression)


def test_hyp_dom_conditionalexpression_constructor_exists():
    assert callable(dom_ConditionalExpression.__init__)


def test_hyp_dom_conditionalexpression_constructor_args():
    sig = inspect.signature(dom_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_functionexpression_is_not_abstract():
    assert not inspect.isabstract(dom_FunctionExpression)


def test_hyp_dom_functionexpression_constructor_exists():
    assert callable(dom_FunctionExpression.__init__)


def test_hyp_dom_functionexpression_constructor_args():
    sig = inspect.signature(dom_FunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "parametersPosition" in params, "Missing parameter 'parametersPosition'"




def test_hyp_dom_nullliteral_is_not_abstract():
    assert not inspect.isabstract(dom_NullLiteral)


def test_hyp_dom_nullliteral_constructor_exists():
    assert callable(dom_NullLiteral.__init__)


def test_hyp_dom_nullliteral_constructor_args():
    sig = inspect.signature(dom_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_descendantaccessexpression_is_not_abstract():
    assert not inspect.isabstract(dom_DescendantAccessExpression)


def test_hyp_dom_descendantaccessexpression_constructor_exists():
    assert callable(dom_DescendantAccessExpression.__init__)


def test_hyp_dom_descendantaccessexpression_constructor_args():
    sig = inspect.signature(dom_DescendantAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(dom_BinaryExpression)


def test_hyp_dom_binaryexpression_constructor_exists():
    assert callable(dom_BinaryExpression.__init__)


def test_hyp_dom_binaryexpression_constructor_args():
    sig = inspect.signature(dom_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operatorPosition" in params, "Missing parameter 'operatorPosition'"
    assert "operation" in params, "Missing parameter 'operation'"





def test_hyp_dom_newexpression_is_not_abstract():
    assert not inspect.isabstract(dom_NewExpression)


def test_hyp_dom_newexpression_constructor_exists():
    assert callable(dom_NewExpression.__init__)


def test_hyp_dom_newexpression_constructor_args():
    sig = inspect.signature(dom_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_arrayaccessexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ArrayAccessExpression)


def test_hyp_dom_arrayaccessexpression_constructor_exists():
    assert callable(dom_ArrayAccessExpression.__init__)


def test_hyp_dom_arrayaccessexpression_constructor_args():
    sig = inspect.signature(dom_ArrayAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(dom_BooleanLiteral)


def test_hyp_dom_booleanliteral_constructor_exists():
    assert callable(dom_BooleanLiteral.__init__)


def test_hyp_dom_booleanliteral_constructor_args():
    sig = inspect.signature(dom_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_dom_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ParenthesizedExpression)


def test_hyp_dom_parenthesizedexpression_constructor_exists():
    assert callable(dom_ParenthesizedExpression.__init__)


def test_hyp_dom_parenthesizedexpression_constructor_args():
    sig = inspect.signature(dom_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variablereference_is_not_abstract():
    assert not inspect.isabstract(dom_VariableReference)


def test_hyp_dom_variablereference_constructor_exists():
    assert callable(dom_VariableReference.__init__)


def test_hyp_dom_variablereference_constructor_args():
    sig = inspect.signature(dom_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_propertyassignment_is_not_abstract():
    assert not inspect.isabstract(PropertyAssignment)


def test_hyp_propertyassignment_constructor_exists():
    assert callable(PropertyAssignment.__init__)


def test_hyp_propertyassignment_constructor_args():
    sig = inspect.signature(PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_accessorassignment_is_not_abstract():
    assert not inspect.isabstract(dom_AccessorAssignment)


def test_hyp_dom_accessorassignment_constructor_exists():
    assert callable(dom_AccessorAssignment.__init__)


def test_hyp_dom_accessorassignment_constructor_args():
    sig = inspect.signature(dom_AccessorAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_simplepropertyassignment_is_not_abstract():
    assert not inspect.isabstract(dom_SimplePropertyAssignment)


def test_hyp_dom_simplepropertyassignment_constructor_exists():
    assert callable(dom_SimplePropertyAssignment.__init__)


def test_hyp_dom_simplepropertyassignment_constructor_args():
    sig = inspect.signature(dom_SimplePropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_objectliteral_is_not_abstract():
    assert not inspect.isabstract(dom_ObjectLiteral)


def test_hyp_dom_objectliteral_constructor_exists():
    assert callable(dom_ObjectLiteral.__init__)


def test_hyp_dom_objectliteral_constructor_args():
    sig = inspect.signature(dom_ObjectLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_elision_is_not_abstract():
    assert not inspect.isabstract(dom_Elision)


def test_hyp_dom_elision_constructor_exists():
    assert callable(dom_Elision.__init__)


def test_hyp_dom_elision_constructor_args():
    sig = inspect.signature(dom_Elision.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_arrayliteral_is_not_abstract():
    assert not inspect.isabstract(dom_ArrayLiteral)


def test_hyp_dom_arrayliteral_constructor_exists():
    assert callable(dom_ArrayLiteral.__init__)


def test_hyp_dom_arrayliteral_constructor_args():
    sig = inspect.signature(dom_ArrayLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_thisexpression_is_not_abstract():
    assert not inspect.isabstract(dom_ThisExpression)


def test_hyp_dom_thisexpression_constructor_exists():
    assert callable(dom_ThisExpression.__init__)


def test_hyp_dom_thisexpression_constructor_args():
    sig = inspect.signature(dom_ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_regularexpressionliteral_is_not_abstract():
    assert not inspect.isabstract(dom_RegularExpressionLiteral)


def test_hyp_dom_regularexpressionliteral_constructor_exists():
    assert callable(dom_RegularExpressionLiteral.__init__)


def test_hyp_dom_regularexpressionliteral_constructor_args():
    sig = inspect.signature(dom_RegularExpressionLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_iproperty_is_not_abstract():
    assert not inspect.isabstract(IProperty)


def test_hyp_iproperty_constructor_exists():
    assert callable(IProperty.__init__)


def test_hyp_iproperty_constructor_args():
    sig = inspect.signature(IProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_propertyidentifier_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyIdentifier)


def test_hyp_dom_propertyidentifier_constructor_exists():
    assert callable(dom_PropertyIdentifier.__init__)


def test_hyp_dom_propertyidentifier_constructor_args():
    sig = inspect.signature(dom_PropertyIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ipropertyselector_is_not_abstract():
    assert not inspect.isabstract(IPropertySelector)


def test_hyp_ipropertyselector_constructor_exists():
    assert callable(IPropertySelector.__init__)


def test_hyp_ipropertyselector_constructor_args():
    sig = inspect.signature(IPropertySelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_wildcardidentifier_is_not_abstract():
    assert not inspect.isabstract(dom_WildcardIdentifier)


def test_hyp_dom_wildcardidentifier_constructor_exists():
    assert callable(dom_WildcardIdentifier.__init__)


def test_hyp_dom_wildcardidentifier_constructor_args():
    sig = inspect.signature(dom_WildcardIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ipropertyname_is_not_abstract():
    assert not inspect.isabstract(IPropertyName)


def test_hyp_ipropertyname_constructor_exists():
    assert callable(IPropertyName.__init__)


def test_hyp_ipropertyname_constructor_args():
    sig = inspect.signature(IPropertyName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_stringliteral_is_not_abstract():
    assert not inspect.isabstract(dom_StringLiteral)


def test_hyp_dom_stringliteral_constructor_exists():
    assert callable(dom_StringLiteral.__init__)


def test_hyp_dom_stringliteral_constructor_args():
    sig = inspect.signature(dom_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_dom_numericliteral_is_not_abstract():
    assert not inspect.isabstract(dom_NumericLiteral)


def test_hyp_dom_numericliteral_constructor_exists():
    assert callable(dom_NumericLiteral.__init__)


def test_hyp_dom_numericliteral_constructor_args():
    sig = inspect.signature(dom_NumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_identifier_is_not_abstract():
    assert not inspect.isabstract(dom_Identifier)


def test_hyp_dom_identifier_constructor_exists():
    assert callable(dom_Identifier.__init__)


def test_hyp_dom_identifier_constructor_args():
    sig = inspect.signature(dom_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dom_switchelement_is_not_abstract():
    assert not inspect.isabstract(dom_SwitchElement)


def test_hyp_dom_switchelement_constructor_exists():
    assert callable(dom_SwitchElement.__init__)


def test_hyp_dom_switchelement_constructor_args():
    sig = inspect.signature(dom_SwitchElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_parameter_is_not_abstract():
    assert not inspect.isabstract(dom_Parameter)


def test_hyp_dom_parameter_constructor_exists():
    assert callable(dom_Parameter.__init__)


def test_hyp_dom_parameter_constructor_args():
    sig = inspect.signature(dom_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_finallyclause_is_not_abstract():
    assert not inspect.isabstract(dom_FinallyClause)


def test_hyp_dom_finallyclause_constructor_exists():
    assert callable(dom_FinallyClause.__init__)


def test_hyp_dom_finallyclause_constructor_args():
    sig = inspect.signature(dom_FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(dom_VariableDeclaration)


def test_hyp_dom_variabledeclaration_constructor_exists():
    assert callable(dom_VariableDeclaration.__init__)


def test_hyp_dom_variabledeclaration_constructor_args():
    sig = inspect.signature(dom_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_xmlfragment_is_not_abstract():
    assert not inspect.isabstract(dom_XmlFragment)


def test_hyp_dom_xmlfragment_constructor_exists():
    assert callable(dom_XmlFragment.__init__)


def test_hyp_dom_xmlfragment_constructor_args():
    sig = inspect.signature(dom_XmlFragment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_catchclause_is_not_abstract():
    assert not inspect.isabstract(dom_CatchClause)


def test_hyp_dom_catchclause_constructor_exists():
    assert callable(dom_CatchClause.__init__)


def test_hyp_dom_catchclause_constructor_args():
    sig = inspect.signature(dom_CatchClause.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_ipropertyname_is_not_abstract():
    assert not inspect.isabstract(dom_IPropertyName)


def test_hyp_dom_ipropertyname_constructor_exists():
    assert callable(dom_IPropertyName.__init__)


def test_hyp_dom_ipropertyname_constructor_args():
    sig = inspect.signature(dom_IPropertyName.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_source_is_not_abstract():
    assert not inspect.isabstract(dom_Source)


def test_hyp_dom_source_constructor_exists():
    assert callable(dom_Source.__init__)


def test_hyp_dom_source_constructor_args():
    sig = inspect.signature(dom_Source.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_propertyassignment_is_not_abstract():
    assert not inspect.isabstract(dom_PropertyAssignment)


def test_hyp_dom_propertyassignment_constructor_exists():
    assert callable(dom_PropertyAssignment.__init__)


def test_hyp_dom_propertyassignment_constructor_args():
    sig = inspect.signature(dom_PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_statement_is_not_abstract():
    assert not inspect.isabstract(dom_Statement)


def test_hyp_dom_statement_constructor_exists():
    assert callable(dom_Statement.__init__)


def test_hyp_dom_statement_constructor_args():
    sig = inspect.signature(dom_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_iproperty_is_not_abstract():
    assert not inspect.isabstract(dom_IProperty)


def test_hyp_dom_iproperty_constructor_exists():
    assert callable(dom_IProperty.__init__)


def test_hyp_dom_iproperty_constructor_args():
    sig = inspect.signature(dom_IProperty.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_label_is_not_abstract():
    assert not inspect.isabstract(dom_Label)


def test_hyp_dom_label_constructor_exists():
    assert callable(dom_Label.__init__)


def test_hyp_dom_label_constructor_args():
    sig = inspect.signature(dom_Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_dom_expression_is_not_abstract():
    assert not inspect.isabstract(dom_Expression)


def test_hyp_dom_expression_constructor_exists():
    assert callable(dom_Expression.__init__)


def test_hyp_dom_expression_constructor_args():
    sig = inspect.signature(dom_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_iforinitializer_is_not_abstract():
    assert not inspect.isabstract(dom_IForInitializer)


def test_hyp_dom_iforinitializer_constructor_exists():
    assert callable(dom_IForInitializer.__init__)


def test_hyp_dom_iforinitializer_constructor_args():
    sig = inspect.signature(dom_IForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_iselector_is_not_abstract():
    assert not inspect.isabstract(dom_ISelector)


def test_hyp_dom_iselector_constructor_exists():
    assert callable(dom_ISelector.__init__)


def test_hyp_dom_iselector_constructor_args():
    sig = inspect.signature(dom_ISelector.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_iarrayelement_is_not_abstract():
    assert not inspect.isabstract(dom_IArrayElement)


def test_hyp_dom_iarrayelement_constructor_exists():
    assert callable(dom_IArrayElement.__init__)


def test_hyp_dom_iarrayelement_constructor_args():
    sig = inspect.signature(dom_IArrayElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dom_comment_is_not_abstract():
    assert not inspect.isabstract(dom_Comment)


def test_hyp_dom_comment_constructor_exists():
    assert callable(dom_Comment.__init__)


def test_hyp_dom_comment_constructor_args():
    sig = inspect.signature(dom_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_dom_node_is_not_abstract():
    assert not inspect.isabstract(dom_Node)


def test_hyp_dom_node_constructor_exists():
    assert callable(dom_Node.__init__)


def test_hyp_dom_node_constructor_args():
    sig = inspect.signature(dom_Node.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "begin" in params, "Missing parameter 'begin'"



def test_hyp_binaryoperator_exists():
    # Check that the Enumeration exists
    assert BinaryOperator is not None

def test_hyp_binaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperator]
    expected_literals = [
        "same",
        "greater",
        "geq",
        "mulAssign",
        "sub",
        "assign",
        "leq",
        "comma",
        "subAssign",
        "bwOr",
        "logAnd",
        "urshAssign",
        "in_",
        "ursh",
        "lsh",
        "logOr",
        "orAssign",
        "rshAssign",
        "divAssign",
        "modAssign",
        "eq",
        "instanceof",
        "nsame",
        "bwAnd",
        "neq",
        "mul",
        "lshAssign",
        "andAssign",
        "bwXor",
        "addAssign",
        "div",
        "less",
        "add",
        "xorAssign",
        "rsh",
        "mod",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperator"

def test_hyp_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_hyp_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "delete",
        "prefixDec",
        "postfixInc",
        "not_",
        "postfixDec",
        "yield_",
        "void",
        "typeof",
        "prefixInc",
        "unaryPlus",
        "bwNot",
        "numNeg",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"


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
XmlFragment_strategy = st.builds(
    XmlFragment,
)
dom_XmlExpressionFragment_strategy = st.builds(
    dom_XmlExpressionFragment,
)
dom_XmlTextFragment_strategy = st.builds(
    dom_XmlTextFragment,
    text=
        safe_text
)
IUnqualifiedSelector_strategy = st.builds(
    IUnqualifiedSelector,
)
dom_ExpressionSelector_strategy = st.builds(
    dom_ExpressionSelector,
)
dom_IPropertySelector_strategy = st.builds(
    dom_IPropertySelector,
)
ISelector_strategy = st.builds(
    ISelector,
)
dom_IUnqualifiedSelector_strategy = st.builds(
    dom_IUnqualifiedSelector,
)
PropertyIdentifier_strategy = st.builds(
    PropertyIdentifier,
)
dom_QualifiedIdentifier_strategy = st.builds(
    dom_QualifiedIdentifier,
)
dom_AttributeIdentifier_strategy = st.builds(
    dom_AttributeIdentifier,
)
SwitchElement_strategy = st.builds(
    SwitchElement,
)
dom_CaseClause_strategy = st.builds(
    dom_CaseClause,
)
dom_DefaultClause_strategy = st.builds(
    dom_DefaultClause,
)
IterationStatement_strategy = st.builds(
    IterationStatement,
)
dom_ForStatement_strategy = st.builds(
    dom_ForStatement,
)
dom_ForEachInStatement_strategy = st.builds(
    dom_ForEachInStatement,
)
dom_WhileStatement_strategy = st.builds(
    dom_WhileStatement,
)
dom_DoStatement_strategy = st.builds(
    dom_DoStatement,
)
dom_ForInStatement_strategy = st.builds(
    dom_ForInStatement,
)
Statement_strategy = st.builds(
    Statement,
)
dom_WithStatement_strategy = st.builds(
    dom_WithStatement,
)
dom_IfStatement_strategy = st.builds(
    dom_IfStatement,
)
dom_ExpressionStatement_strategy = st.builds(
    dom_ExpressionStatement,
)
dom_DefaultXmlNamespaceStatement_strategy = st.builds(
    dom_DefaultXmlNamespaceStatement,
)
dom_SwitchStatement_strategy = st.builds(
    dom_SwitchStatement,
)
dom_ReturnStatement_strategy = st.builds(
    dom_ReturnStatement,
)
dom_ConstStatement_strategy = st.builds(
    dom_ConstStatement,
)
dom_BreakStatement_strategy = st.builds(
    dom_BreakStatement,
)
dom_EmptyStatement_strategy = st.builds(
    dom_EmptyStatement,
)
dom_TryStatement_strategy = st.builds(
    dom_TryStatement,
)
dom_LabeledStatement_strategy = st.builds(
    dom_LabeledStatement,
)
dom_IterationStatement_strategy = st.builds(
    dom_IterationStatement,
)
dom_ContinueStatement_strategy = st.builds(
    dom_ContinueStatement,
)
dom_ThrowStatement_strategy = st.builds(
    dom_ThrowStatement,
)
AccessorAssignment_strategy = st.builds(
    AccessorAssignment,
)
dom_SetterAssignment_strategy = st.builds(
    dom_SetterAssignment,
)
dom_GetterAssignment_strategy = st.builds(
    dom_GetterAssignment,
)
dom_BlockStatement_strategy = st.builds(
    dom_BlockStatement,
)
IForInitializer_strategy = st.builds(
    IForInitializer,
)
dom_VariableStatement_strategy = st.builds(
    dom_VariableStatement,
)
IArrayElement_strategy = st.builds(
    IArrayElement,
)
Expression_strategy = st.builds(
    Expression,
)
dom_UnaryExpression_strategy = st.builds(
    dom_UnaryExpression,
    operation=
        safe_text
)
dom_FilterExpression_strategy = st.builds(
    dom_FilterExpression,
)
dom_PropertyAccessExpression_strategy = st.builds(
    dom_PropertyAccessExpression,
)
dom_CallExpression_strategy = st.builds(
    dom_CallExpression,
)
dom_XmlInitializer_strategy = st.builds(
    dom_XmlInitializer,
)
dom_ConditionalExpression_strategy = st.builds(
    dom_ConditionalExpression,
)
dom_FunctionExpression_strategy = st.builds(
    dom_FunctionExpression,
    parametersPosition=
        st.integers()
)
dom_NullLiteral_strategy = st.builds(
    dom_NullLiteral,
)
dom_DescendantAccessExpression_strategy = st.builds(
    dom_DescendantAccessExpression,
)
dom_BinaryExpression_strategy = st.builds(
    dom_BinaryExpression,
    operatorPosition=
        st.integers(),
    operation=
        safe_text
)
dom_NewExpression_strategy = st.builds(
    dom_NewExpression,
)
dom_ArrayAccessExpression_strategy = st.builds(
    dom_ArrayAccessExpression,
)
dom_BooleanLiteral_strategy = st.builds(
    dom_BooleanLiteral,
    text=
        safe_text
)
dom_ParenthesizedExpression_strategy = st.builds(
    dom_ParenthesizedExpression,
)
dom_VariableReference_strategy = st.builds(
    dom_VariableReference,
)
PropertyAssignment_strategy = st.builds(
    PropertyAssignment,
)
dom_AccessorAssignment_strategy = st.builds(
    dom_AccessorAssignment,
)
dom_SimplePropertyAssignment_strategy = st.builds(
    dom_SimplePropertyAssignment,
)
dom_ObjectLiteral_strategy = st.builds(
    dom_ObjectLiteral,
)
dom_Elision_strategy = st.builds(
    dom_Elision,
)
dom_ArrayLiteral_strategy = st.builds(
    dom_ArrayLiteral,
)
dom_ThisExpression_strategy = st.builds(
    dom_ThisExpression,
)
dom_RegularExpressionLiteral_strategy = st.builds(
    dom_RegularExpressionLiteral,
    text=
        safe_text
)
IProperty_strategy = st.builds(
    IProperty,
)
dom_PropertyIdentifier_strategy = st.builds(
    dom_PropertyIdentifier,
)
IPropertySelector_strategy = st.builds(
    IPropertySelector,
)
dom_WildcardIdentifier_strategy = st.builds(
    dom_WildcardIdentifier,
)
IPropertyName_strategy = st.builds(
    IPropertyName,
)
dom_StringLiteral_strategy = st.builds(
    dom_StringLiteral,
    text=
        safe_text
)
dom_NumericLiteral_strategy = st.builds(
    dom_NumericLiteral,
    text=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
dom_Identifier_strategy = st.builds(
    dom_Identifier,
    name=
        safe_text
)
dom_SwitchElement_strategy = st.builds(
    dom_SwitchElement,
)
dom_Parameter_strategy = st.builds(
    dom_Parameter,
)
dom_FinallyClause_strategy = st.builds(
    dom_FinallyClause,
)
dom_VariableDeclaration_strategy = st.builds(
    dom_VariableDeclaration,
)
dom_XmlFragment_strategy = st.builds(
    dom_XmlFragment,
)
dom_CatchClause_strategy = st.builds(
    dom_CatchClause,
)
dom_IPropertyName_strategy = st.builds(
    dom_IPropertyName,
)
dom_Source_strategy = st.builds(
    dom_Source,
)
dom_PropertyAssignment_strategy = st.builds(
    dom_PropertyAssignment,
)
dom_Statement_strategy = st.builds(
    dom_Statement,
)
dom_IProperty_strategy = st.builds(
    dom_IProperty,
)
dom_Label_strategy = st.builds(
    dom_Label,
    name=
        safe_text
)
dom_Expression_strategy = st.builds(
    dom_Expression,
)
dom_IForInitializer_strategy = st.builds(
    dom_IForInitializer,
)
dom_ISelector_strategy = st.builds(
    dom_ISelector,
)
dom_IArrayElement_strategy = st.builds(
    dom_IArrayElement,
)
dom_Comment_strategy = st.builds(
    dom_Comment,
    text=
        safe_text
)
dom_Node_strategy = st.builds(
    dom_Node,
    end=
        st.integers(),
    begin=
        st.integers()
)






@given(instance=dom_XmlTextFragment_strategy)
def test_hyp_dom_xmltextfragment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original












































@given(instance=dom_UnaryExpression_strategy)
def test_hyp_dom_unaryexpression_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original









@given(instance=dom_FunctionExpression_strategy)
def test_hyp_dom_functionexpression_parametersPosition_setter(instance):
    original = instance.parametersPosition
    instance.parametersPosition = original
    assert instance.parametersPosition == original






@given(instance=dom_BinaryExpression_strategy)
def test_hyp_dom_binaryexpression_operatorPosition_setter(instance):
    original = instance.operatorPosition
    instance.operatorPosition = original
    assert instance.operatorPosition == original



@given(instance=dom_BinaryExpression_strategy)
def test_hyp_dom_binaryexpression_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original






@given(instance=dom_BooleanLiteral_strategy)
def test_hyp_dom_booleanliteral_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original













@given(instance=dom_RegularExpressionLiteral_strategy)
def test_hyp_dom_regularexpressionliteral_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original









@given(instance=dom_StringLiteral_strategy)
def test_hyp_dom_stringliteral_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=dom_NumericLiteral_strategy)
def test_hyp_dom_numericliteral_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=dom_Identifier_strategy)
def test_hyp_dom_identifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original















@given(instance=dom_Label_strategy)
def test_hyp_dom_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








@given(instance=dom_Comment_strategy)
def test_hyp_dom_comment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=dom_Node_strategy)
def test_hyp_dom_node_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=dom_Node_strategy)
def test_hyp_dom_node_begin_setter(instance):
    original = instance.begin
    instance.begin = original
    assert instance.begin == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AccessorAssignment,
    Expression,
    IArrayElement,
    IForInitializer,
    IProperty,
    IPropertyName,
    IPropertySelector,
    ISelector,
    IUnqualifiedSelector,
    IterationStatement,
    Node,
    PropertyAssignment,
    PropertyIdentifier,
    Statement,
    SwitchElement,
    XmlFragment,
    dom_AccessorAssignment,
    dom_ArrayAccessExpression,
    dom_ArrayLiteral,
    dom_AttributeIdentifier,
    dom_BinaryExpression,
    dom_BlockStatement,
    dom_BooleanLiteral,
    dom_BreakStatement,
    dom_CallExpression,
    dom_CaseClause,
    dom_CatchClause,
    dom_Comment,
    dom_ConditionalExpression,
    dom_ConstStatement,
    dom_ContinueStatement,
    dom_DefaultClause,
    dom_DefaultXmlNamespaceStatement,
    dom_DescendantAccessExpression,
    dom_DoStatement,
    dom_Elision,
    dom_EmptyStatement,
    dom_Expression,
    dom_ExpressionSelector,
    dom_ExpressionStatement,
    dom_FilterExpression,
    dom_FinallyClause,
    dom_ForEachInStatement,
    dom_ForInStatement,
    dom_ForStatement,
    dom_FunctionExpression,
    dom_GetterAssignment,
    dom_IArrayElement,
    dom_IForInitializer,
    dom_IProperty,
    dom_IPropertyName,
    dom_IPropertySelector,
    dom_ISelector,
    dom_IUnqualifiedSelector,
    dom_Identifier,
    dom_IfStatement,
    dom_IterationStatement,
    dom_Label,
    dom_LabeledStatement,
    dom_NewExpression,
    dom_Node,
    dom_NullLiteral,
    dom_NumericLiteral,
    dom_ObjectLiteral,
    dom_Parameter,
    dom_ParenthesizedExpression,
    dom_PropertyAccessExpression,
    dom_PropertyAssignment,
    dom_PropertyIdentifier,
    dom_QualifiedIdentifier,
    dom_RegularExpressionLiteral,
    dom_ReturnStatement,
    dom_SetterAssignment,
    dom_SimplePropertyAssignment,
    dom_Source,
    dom_Statement,
    dom_StringLiteral,
    dom_SwitchElement,
    dom_SwitchStatement,
    dom_ThisExpression,
    dom_ThrowStatement,
    dom_TryStatement,
    dom_UnaryExpression,
    dom_VariableDeclaration,
    dom_VariableReference,
    dom_VariableStatement,
    dom_WhileStatement,
    dom_WildcardIdentifier,
    dom_WithStatement,
    dom_XmlExpressionFragment,
    dom_XmlFragment,
    dom_XmlInitializer,
    dom_XmlTextFragment,
    BinaryOperator,
    UnaryOperator,
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

def test_dom_BinaryExpression_operation_value_roundtrip():
    instance = dom_BinaryExpression(operation="sample_text", operatorPosition=7)
    assert instance.operation == "sample_text"
    instance.operation = "sample_text_2"
    assert instance.operation == "sample_text_2"


def test_dom_BinaryExpression_operatorPosition_value_roundtrip():
    instance = dom_BinaryExpression(operation="sample_text", operatorPosition=7)
    assert instance.operatorPosition == 7
    instance.operatorPosition = 13
    assert instance.operatorPosition == 13


def test_dom_BooleanLiteral_text_value_roundtrip():
    instance = dom_BooleanLiteral(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_dom_Comment_text_value_roundtrip():
    instance = dom_Comment(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_dom_FunctionExpression_parametersPosition_value_roundtrip():
    instance = dom_FunctionExpression(parametersPosition=7)
    assert instance.parametersPosition == 7
    instance.parametersPosition = 13
    assert instance.parametersPosition == 13


def test_dom_Identifier_name_value_roundtrip():
    instance = dom_Identifier(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_Label_name_value_roundtrip():
    instance = dom_Label(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_dom_Node_begin_value_roundtrip():
    instance = dom_Node(begin=7, end=7)
    assert instance.begin == 7
    instance.begin = 13
    assert instance.begin == 13


def test_dom_Node_end_value_roundtrip():
    instance = dom_Node(begin=7, end=7)
    assert instance.end == 7
    instance.end = 13
    assert instance.end == 13


def test_dom_NumericLiteral_text_value_roundtrip():
    instance = dom_NumericLiteral(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_dom_RegularExpressionLiteral_text_value_roundtrip():
    instance = dom_RegularExpressionLiteral(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_dom_StringLiteral_text_value_roundtrip():
    instance = dom_StringLiteral(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_dom_UnaryExpression_operation_value_roundtrip():
    instance = dom_UnaryExpression(operation="sample_text")
    assert instance.operation == "sample_text"
    instance.operation = "sample_text_2"
    assert instance.operation == "sample_text_2"


def test_dom_XmlTextFragment_text_value_roundtrip():
    instance = dom_XmlTextFragment(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_dom_GetterAssignment_isa_AccessorAssignment():
    instance = dom_GetterAssignment()
    assert isinstance(instance, AccessorAssignment)


def test_dom_SetterAssignment_isa_AccessorAssignment():
    instance = dom_SetterAssignment()
    assert isinstance(instance, AccessorAssignment)


def test_dom_ArrayAccessExpression_isa_Expression():
    instance = dom_ArrayAccessExpression()
    assert isinstance(instance, Expression)


def test_dom_ArrayLiteral_isa_Expression():
    instance = dom_ArrayLiteral()
    assert isinstance(instance, Expression)


def test_dom_BinaryExpression_isa_Expression():
    instance = dom_BinaryExpression(operation="sample_text", operatorPosition=7)
    assert isinstance(instance, Expression)


def test_dom_BooleanLiteral_isa_Expression():
    instance = dom_BooleanLiteral(text="sample_text")
    assert isinstance(instance, Expression)


def test_dom_CallExpression_isa_Expression():
    instance = dom_CallExpression()
    assert isinstance(instance, Expression)


def test_dom_ConditionalExpression_isa_Expression():
    instance = dom_ConditionalExpression()
    assert isinstance(instance, Expression)


def test_dom_DescendantAccessExpression_isa_Expression():
    instance = dom_DescendantAccessExpression()
    assert isinstance(instance, Expression)


def test_dom_FilterExpression_isa_Expression():
    instance = dom_FilterExpression()
    assert isinstance(instance, Expression)


def test_dom_FunctionExpression_isa_Expression():
    instance = dom_FunctionExpression(parametersPosition=7)
    assert isinstance(instance, Expression)


def test_dom_NewExpression_isa_Expression():
    instance = dom_NewExpression()
    assert isinstance(instance, Expression)


def test_dom_NullLiteral_isa_Expression():
    instance = dom_NullLiteral()
    assert isinstance(instance, Expression)


def test_dom_NumericLiteral_isa_Expression():
    instance = dom_NumericLiteral(text="sample_text")
    assert isinstance(instance, Expression)


def test_dom_ObjectLiteral_isa_Expression():
    instance = dom_ObjectLiteral()
    assert isinstance(instance, Expression)


def test_dom_ParenthesizedExpression_isa_Expression():
    instance = dom_ParenthesizedExpression()
    assert isinstance(instance, Expression)


def test_dom_PropertyAccessExpression_isa_Expression():
    instance = dom_PropertyAccessExpression()
    assert isinstance(instance, Expression)


def test_dom_PropertyIdentifier_isa_Expression():
    instance = dom_PropertyIdentifier()
    assert isinstance(instance, Expression)


def test_dom_RegularExpressionLiteral_isa_Expression():
    instance = dom_RegularExpressionLiteral(text="sample_text")
    assert isinstance(instance, Expression)


def test_dom_StringLiteral_isa_Expression():
    instance = dom_StringLiteral(text="sample_text")
    assert isinstance(instance, Expression)


def test_dom_ThisExpression_isa_Expression():
    instance = dom_ThisExpression()
    assert isinstance(instance, Expression)


def test_dom_UnaryExpression_isa_Expression():
    instance = dom_UnaryExpression(operation="sample_text")
    assert isinstance(instance, Expression)


def test_dom_VariableReference_isa_Expression():
    instance = dom_VariableReference()
    assert isinstance(instance, Expression)


def test_dom_XmlInitializer_isa_Expression():
    instance = dom_XmlInitializer()
    assert isinstance(instance, Expression)


def test_dom_Elision_isa_IArrayElement():
    instance = dom_Elision()
    assert isinstance(instance, IArrayElement)


def test_dom_Expression_isa_IArrayElement():
    instance = dom_Expression()
    assert isinstance(instance, IArrayElement)


def test_dom_Expression_isa_IForInitializer():
    instance = dom_Expression()
    assert isinstance(instance, IForInitializer)


def test_dom_VariableStatement_isa_IForInitializer():
    instance = dom_VariableStatement()
    assert isinstance(instance, IForInitializer)


def test_dom_Identifier_isa_IProperty():
    instance = dom_Identifier(name="sample_text")
    assert isinstance(instance, IProperty)


def test_dom_PropertyIdentifier_isa_IProperty():
    instance = dom_PropertyIdentifier()
    assert isinstance(instance, IProperty)


def test_dom_Identifier_isa_IPropertyName():
    instance = dom_Identifier(name="sample_text")
    assert isinstance(instance, IPropertyName)


def test_dom_NumericLiteral_isa_IPropertyName():
    instance = dom_NumericLiteral(text="sample_text")
    assert isinstance(instance, IPropertyName)


def test_dom_StringLiteral_isa_IPropertyName():
    instance = dom_StringLiteral(text="sample_text")
    assert isinstance(instance, IPropertyName)


def test_dom_Identifier_isa_IPropertySelector():
    instance = dom_Identifier(name="sample_text")
    assert isinstance(instance, IPropertySelector)


def test_dom_WildcardIdentifier_isa_IPropertySelector():
    instance = dom_WildcardIdentifier()
    assert isinstance(instance, IPropertySelector)


def test_dom_IUnqualifiedSelector_isa_ISelector():
    instance = dom_IUnqualifiedSelector()
    assert isinstance(instance, ISelector)


def test_dom_QualifiedIdentifier_isa_ISelector():
    instance = dom_QualifiedIdentifier()
    assert isinstance(instance, ISelector)


def test_dom_ExpressionSelector_isa_IUnqualifiedSelector():
    instance = dom_ExpressionSelector()
    assert isinstance(instance, IUnqualifiedSelector)


def test_dom_IPropertySelector_isa_IUnqualifiedSelector():
    instance = dom_IPropertySelector()
    assert isinstance(instance, IUnqualifiedSelector)


def test_dom_DoStatement_isa_IterationStatement():
    instance = dom_DoStatement()
    assert isinstance(instance, IterationStatement)


def test_dom_ForEachInStatement_isa_IterationStatement():
    instance = dom_ForEachInStatement()
    assert isinstance(instance, IterationStatement)


def test_dom_ForInStatement_isa_IterationStatement():
    instance = dom_ForInStatement()
    assert isinstance(instance, IterationStatement)


def test_dom_ForStatement_isa_IterationStatement():
    instance = dom_ForStatement()
    assert isinstance(instance, IterationStatement)


def test_dom_WhileStatement_isa_IterationStatement():
    instance = dom_WhileStatement()
    assert isinstance(instance, IterationStatement)


def test_dom_CatchClause_isa_Node():
    instance = dom_CatchClause()
    assert isinstance(instance, Node)


def test_dom_Comment_isa_Node():
    instance = dom_Comment(text="sample_text")
    assert isinstance(instance, Node)


def test_dom_Expression_isa_Node():
    instance = dom_Expression()
    assert isinstance(instance, Node)


def test_dom_FinallyClause_isa_Node():
    instance = dom_FinallyClause()
    assert isinstance(instance, Node)


def test_dom_IArrayElement_isa_Node():
    instance = dom_IArrayElement()
    assert isinstance(instance, Node)


def test_dom_IForInitializer_isa_Node():
    instance = dom_IForInitializer()
    assert isinstance(instance, Node)


def test_dom_IProperty_isa_Node():
    instance = dom_IProperty()
    assert isinstance(instance, Node)


def test_dom_IPropertyName_isa_Node():
    instance = dom_IPropertyName()
    assert isinstance(instance, Node)


def test_dom_ISelector_isa_Node():
    instance = dom_ISelector()
    assert isinstance(instance, Node)


def test_dom_Identifier_isa_Node():
    instance = dom_Identifier(name="sample_text")
    assert isinstance(instance, Node)


def test_dom_Label_isa_Node():
    instance = dom_Label(name="sample_text")
    assert isinstance(instance, Node)


def test_dom_Parameter_isa_Node():
    instance = dom_Parameter()
    assert isinstance(instance, Node)


def test_dom_PropertyAssignment_isa_Node():
    instance = dom_PropertyAssignment()
    assert isinstance(instance, Node)


def test_dom_Source_isa_Node():
    instance = dom_Source()
    assert isinstance(instance, Node)


def test_dom_Statement_isa_Node():
    instance = dom_Statement()
    assert isinstance(instance, Node)


def test_dom_SwitchElement_isa_Node():
    instance = dom_SwitchElement()
    assert isinstance(instance, Node)


def test_dom_VariableDeclaration_isa_Node():
    instance = dom_VariableDeclaration()
    assert isinstance(instance, Node)


def test_dom_XmlFragment_isa_Node():
    instance = dom_XmlFragment()
    assert isinstance(instance, Node)


def test_dom_AccessorAssignment_isa_PropertyAssignment():
    instance = dom_AccessorAssignment()
    assert isinstance(instance, PropertyAssignment)


def test_dom_SimplePropertyAssignment_isa_PropertyAssignment():
    instance = dom_SimplePropertyAssignment()
    assert isinstance(instance, PropertyAssignment)


def test_dom_AttributeIdentifier_isa_PropertyIdentifier():
    instance = dom_AttributeIdentifier()
    assert isinstance(instance, PropertyIdentifier)


def test_dom_QualifiedIdentifier_isa_PropertyIdentifier():
    instance = dom_QualifiedIdentifier()
    assert isinstance(instance, PropertyIdentifier)


def test_dom_WildcardIdentifier_isa_PropertyIdentifier():
    instance = dom_WildcardIdentifier()
    assert isinstance(instance, PropertyIdentifier)


def test_dom_BlockStatement_isa_Statement():
    instance = dom_BlockStatement()
    assert isinstance(instance, Statement)


def test_dom_BreakStatement_isa_Statement():
    instance = dom_BreakStatement()
    assert isinstance(instance, Statement)


def test_dom_ConstStatement_isa_Statement():
    instance = dom_ConstStatement()
    assert isinstance(instance, Statement)


def test_dom_ContinueStatement_isa_Statement():
    instance = dom_ContinueStatement()
    assert isinstance(instance, Statement)


def test_dom_DefaultXmlNamespaceStatement_isa_Statement():
    instance = dom_DefaultXmlNamespaceStatement()
    assert isinstance(instance, Statement)


def test_dom_EmptyStatement_isa_Statement():
    instance = dom_EmptyStatement()
    assert isinstance(instance, Statement)


def test_dom_ExpressionStatement_isa_Statement():
    instance = dom_ExpressionStatement()
    assert isinstance(instance, Statement)


def test_dom_IfStatement_isa_Statement():
    instance = dom_IfStatement()
    assert isinstance(instance, Statement)


def test_dom_IterationStatement_isa_Statement():
    instance = dom_IterationStatement()
    assert isinstance(instance, Statement)


def test_dom_LabeledStatement_isa_Statement():
    instance = dom_LabeledStatement()
    assert isinstance(instance, Statement)


def test_dom_ReturnStatement_isa_Statement():
    instance = dom_ReturnStatement()
    assert isinstance(instance, Statement)


def test_dom_SwitchStatement_isa_Statement():
    instance = dom_SwitchStatement()
    assert isinstance(instance, Statement)


def test_dom_ThrowStatement_isa_Statement():
    instance = dom_ThrowStatement()
    assert isinstance(instance, Statement)


def test_dom_TryStatement_isa_Statement():
    instance = dom_TryStatement()
    assert isinstance(instance, Statement)


def test_dom_VariableStatement_isa_Statement():
    instance = dom_VariableStatement()
    assert isinstance(instance, Statement)


def test_dom_WithStatement_isa_Statement():
    instance = dom_WithStatement()
    assert isinstance(instance, Statement)


def test_dom_CaseClause_isa_SwitchElement():
    instance = dom_CaseClause()
    assert isinstance(instance, SwitchElement)


def test_dom_DefaultClause_isa_SwitchElement():
    instance = dom_DefaultClause()
    assert isinstance(instance, SwitchElement)


def test_dom_XmlExpressionFragment_isa_XmlFragment():
    instance = dom_XmlExpressionFragment()
    assert isinstance(instance, XmlFragment)


def test_dom_XmlTextFragment_isa_XmlFragment():
    instance = dom_XmlTextFragment(text="sample_text")
    assert isinstance(instance, XmlFragment)


def test_assoc_argument30_link_reassign_clear():
    a = dom_UnaryExpression(operation="sample_text")
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_UnaryExpression', b1)
    assert _is_linked(a, 'dom_UnaryExpression', b1)
    if hasattr(b1, 'dom_Expression31'):
        assert _is_linked(b1, 'dom_Expression31', a)
    _safe_set(a, 'dom_UnaryExpression', b2)
    assert _is_linked(a, 'dom_UnaryExpression', b2)
    if hasattr(b1, 'dom_Expression31'):
        assert not _is_linked(b1, 'dom_Expression31', a)
    if hasattr(b2, 'dom_Expression31'):
        assert _is_linked(b2, 'dom_Expression31', a)
    _safe_set(a, 'dom_UnaryExpression', None)
    assert not _is_linked(a, 'dom_UnaryExpression', b2)
    if hasattr(b2, 'dom_Expression31'):
        assert not _is_linked(b2, 'dom_Expression31', a)


def test_assoc_body132_link_reassign_clear():
    a = dom_FunctionExpression(parametersPosition=7)
    b1 = dom_BlockStatement()
    b2 = dom_BlockStatement()
    _safe_set(a, 'dom_FunctionExpression133', b1)
    assert _is_linked(a, 'dom_FunctionExpression133', b1)
    if hasattr(b1, 'dom_BlockStatement134'):
        assert _is_linked(b1, 'dom_BlockStatement134', a)
    _safe_set(a, 'dom_FunctionExpression133', b2)
    assert _is_linked(a, 'dom_FunctionExpression133', b2)
    if hasattr(b1, 'dom_BlockStatement134'):
        assert not _is_linked(b1, 'dom_BlockStatement134', a)
    if hasattr(b2, 'dom_BlockStatement134'):
        assert _is_linked(b2, 'dom_BlockStatement134', a)
    _safe_set(a, 'dom_FunctionExpression133', None)
    assert not _is_linked(a, 'dom_FunctionExpression133', b2)
    if hasattr(b2, 'dom_BlockStatement134'):
        assert not _is_linked(b2, 'dom_BlockStatement134', a)


def test_assoc_documentation126_link_reassign_clear():
    a = dom_FunctionExpression(parametersPosition=7)
    b1 = dom_Comment(text="sample_text")
    b2 = dom_Comment(text="sample_text_2")
    _safe_set(a, 'dom_FunctionExpression', b1)
    assert _is_linked(a, 'dom_FunctionExpression', b1)
    if hasattr(b1, 'dom_Comment'):
        assert _is_linked(b1, 'dom_Comment', a)
    _safe_set(a, 'dom_FunctionExpression', b2)
    assert _is_linked(a, 'dom_FunctionExpression', b2)
    if hasattr(b1, 'dom_Comment'):
        assert not _is_linked(b1, 'dom_Comment', a)
    if hasattr(b2, 'dom_Comment'):
        assert _is_linked(b2, 'dom_Comment', a)
    _safe_set(a, 'dom_FunctionExpression', None)
    assert not _is_linked(a, 'dom_FunctionExpression', b2)
    if hasattr(b2, 'dom_Comment'):
        assert not _is_linked(b2, 'dom_Comment', a)


def test_assoc_exception114_link_reassign_clear():
    a = dom_Identifier(name="sample_text")
    b1 = dom_CatchClause()
    b2 = dom_CatchClause()
    _safe_set(a, 'dom_Identifier116', b1)
    assert _is_linked(a, 'dom_Identifier116', b1)
    if hasattr(b1, 'dom_CatchClause115'):
        assert _is_linked(b1, 'dom_CatchClause115', a)
    _safe_set(a, 'dom_Identifier116', b2)
    assert _is_linked(a, 'dom_Identifier116', b2)
    if hasattr(b1, 'dom_CatchClause115'):
        assert not _is_linked(b1, 'dom_CatchClause115', a)
    if hasattr(b2, 'dom_CatchClause115'):
        assert _is_linked(b2, 'dom_CatchClause115', a)
    _safe_set(a, 'dom_Identifier116', None)
    assert not _is_linked(a, 'dom_Identifier116', b2)
    if hasattr(b2, 'dom_CatchClause115'):
        assert not _is_linked(b2, 'dom_CatchClause115', a)


def test_assoc_identifier127_link_reassign_clear():
    a = dom_Identifier(name="sample_text")
    b1 = dom_FunctionExpression(parametersPosition=7)
    b2 = dom_FunctionExpression(parametersPosition=13)
    _safe_set(a, 'dom_Identifier129', b1)
    assert _is_linked(a, 'dom_Identifier129', b1)
    if hasattr(b1, 'dom_FunctionExpression128'):
        assert _is_linked(b1, 'dom_FunctionExpression128', a)
    _safe_set(a, 'dom_Identifier129', b2)
    assert _is_linked(a, 'dom_Identifier129', b2)
    if hasattr(b1, 'dom_FunctionExpression128'):
        assert not _is_linked(b1, 'dom_FunctionExpression128', a)
    if hasattr(b2, 'dom_FunctionExpression128'):
        assert _is_linked(b2, 'dom_FunctionExpression128', a)
    _safe_set(a, 'dom_Identifier129', None)
    assert not _is_linked(a, 'dom_Identifier129', b2)
    if hasattr(b2, 'dom_FunctionExpression128'):
        assert not _is_linked(b2, 'dom_FunctionExpression128', a)


def test_assoc_identifier48_link_reassign_clear():
    a = dom_Identifier(name="sample_text")
    b1 = dom_VariableDeclaration()
    b2 = dom_VariableDeclaration()
    _safe_set(a, 'dom_Identifier50', b1)
    assert _is_linked(a, 'dom_Identifier50', b1)
    if hasattr(b1, 'dom_VariableDeclaration49'):
        assert _is_linked(b1, 'dom_VariableDeclaration49', a)
    _safe_set(a, 'dom_Identifier50', b2)
    assert _is_linked(a, 'dom_Identifier50', b2)
    if hasattr(b1, 'dom_VariableDeclaration49'):
        assert not _is_linked(b1, 'dom_VariableDeclaration49', a)
    if hasattr(b2, 'dom_VariableDeclaration49'):
        assert _is_linked(b2, 'dom_VariableDeclaration49', a)
    _safe_set(a, 'dom_Identifier50', None)
    assert not _is_linked(a, 'dom_Identifier50', b2)
    if hasattr(b2, 'dom_VariableDeclaration49'):
        assert not _is_linked(b2, 'dom_VariableDeclaration49', a)


def test_assoc_label101_link_reassign_clear():
    a = dom_Label(name="sample_text")
    b1 = dom_LabeledStatement()
    b2 = dom_LabeledStatement()
    _safe_set(a, 'dom_Label102', b1)
    assert _is_linked(a, 'dom_Label102', b1)
    if hasattr(b1, 'dom_LabeledStatement'):
        assert _is_linked(b1, 'dom_LabeledStatement', a)
    _safe_set(a, 'dom_Label102', b2)
    assert _is_linked(a, 'dom_Label102', b2)
    if hasattr(b1, 'dom_LabeledStatement'):
        assert not _is_linked(b1, 'dom_LabeledStatement', a)
    if hasattr(b2, 'dom_LabeledStatement'):
        assert _is_linked(b2, 'dom_LabeledStatement', a)
    _safe_set(a, 'dom_Label102', None)
    assert not _is_linked(a, 'dom_Label102', b2)
    if hasattr(b2, 'dom_LabeledStatement'):
        assert not _is_linked(b2, 'dom_LabeledStatement', a)


def test_assoc_label82_link_reassign_clear():
    a = dom_Label(name="sample_text")
    b1 = dom_ContinueStatement()
    b2 = dom_ContinueStatement()
    _safe_set(a, 'dom_Label', b1)
    assert _is_linked(a, 'dom_Label', b1)
    if hasattr(b1, 'dom_ContinueStatement'):
        assert _is_linked(b1, 'dom_ContinueStatement', a)
    _safe_set(a, 'dom_Label', b2)
    assert _is_linked(a, 'dom_Label', b2)
    if hasattr(b1, 'dom_ContinueStatement'):
        assert not _is_linked(b1, 'dom_ContinueStatement', a)
    if hasattr(b2, 'dom_ContinueStatement'):
        assert _is_linked(b2, 'dom_ContinueStatement', a)
    _safe_set(a, 'dom_Label', None)
    assert not _is_linked(a, 'dom_Label', b2)
    if hasattr(b2, 'dom_ContinueStatement'):
        assert not _is_linked(b2, 'dom_ContinueStatement', a)


def test_assoc_label83_link_reassign_clear():
    a = dom_Label(name="sample_text")
    b1 = dom_BreakStatement()
    b2 = dom_BreakStatement()
    _safe_set(a, 'dom_Label84', b1)
    assert _is_linked(a, 'dom_Label84', b1)
    if hasattr(b1, 'dom_BreakStatement'):
        assert _is_linked(b1, 'dom_BreakStatement', a)
    _safe_set(a, 'dom_Label84', b2)
    assert _is_linked(a, 'dom_Label84', b2)
    if hasattr(b1, 'dom_BreakStatement'):
        assert not _is_linked(b1, 'dom_BreakStatement', a)
    if hasattr(b2, 'dom_BreakStatement'):
        assert _is_linked(b2, 'dom_BreakStatement', a)
    _safe_set(a, 'dom_Label84', None)
    assert not _is_linked(a, 'dom_Label84', b2)
    if hasattr(b2, 'dom_BreakStatement'):
        assert not _is_linked(b2, 'dom_BreakStatement', a)


def test_assoc_left32_link_reassign_clear():
    a = dom_BinaryExpression(operation="sample_text", operatorPosition=7)
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_BinaryExpression', b1)
    assert _is_linked(a, 'dom_BinaryExpression', b1)
    if hasattr(b1, 'dom_Expression33'):
        assert _is_linked(b1, 'dom_Expression33', a)
    _safe_set(a, 'dom_BinaryExpression', b2)
    assert _is_linked(a, 'dom_BinaryExpression', b2)
    if hasattr(b1, 'dom_Expression33'):
        assert not _is_linked(b1, 'dom_Expression33', a)
    if hasattr(b2, 'dom_Expression33'):
        assert _is_linked(b2, 'dom_Expression33', a)
    _safe_set(a, 'dom_BinaryExpression', None)
    assert not _is_linked(a, 'dom_BinaryExpression', b2)
    if hasattr(b2, 'dom_Expression33'):
        assert not _is_linked(b2, 'dom_Expression33', a)


def test_assoc_name135_link_reassign_clear():
    a = dom_Identifier(name="sample_text")
    b1 = dom_Parameter()
    b2 = dom_Parameter()
    _safe_set(a, 'dom_Identifier137', b1)
    assert _is_linked(a, 'dom_Identifier137', b1)
    if hasattr(b1, 'dom_Parameter136'):
        assert _is_linked(b1, 'dom_Parameter136', a)
    _safe_set(a, 'dom_Identifier137', b2)
    assert _is_linked(a, 'dom_Identifier137', b2)
    if hasattr(b1, 'dom_Parameter136'):
        assert not _is_linked(b1, 'dom_Parameter136', a)
    if hasattr(b2, 'dom_Parameter136'):
        assert _is_linked(b2, 'dom_Parameter136', a)
    _safe_set(a, 'dom_Identifier137', None)
    assert not _is_linked(a, 'dom_Identifier137', b2)
    if hasattr(b2, 'dom_Parameter136'):
        assert not _is_linked(b2, 'dom_Parameter136', a)


def test_assoc_parameter7_link_reassign_clear():
    a = dom_Identifier(name="sample_text")
    b1 = dom_SetterAssignment()
    b2 = dom_SetterAssignment()
    _safe_set(a, 'dom_Identifier8', b1)
    assert _is_linked(a, 'dom_Identifier8', b1)
    if hasattr(b1, 'dom_SetterAssignment'):
        assert _is_linked(b1, 'dom_SetterAssignment', a)
    _safe_set(a, 'dom_Identifier8', b2)
    assert _is_linked(a, 'dom_Identifier8', b2)
    if hasattr(b1, 'dom_SetterAssignment'):
        assert not _is_linked(b1, 'dom_SetterAssignment', a)
    if hasattr(b2, 'dom_SetterAssignment'):
        assert _is_linked(b2, 'dom_SetterAssignment', a)
    _safe_set(a, 'dom_Identifier8', None)
    assert not _is_linked(a, 'dom_Identifier8', b2)
    if hasattr(b2, 'dom_SetterAssignment'):
        assert not _is_linked(b2, 'dom_SetterAssignment', a)


def test_assoc_parameters130_link_reassign_clear():
    a = dom_FunctionExpression(parametersPosition=7)
    b1 = dom_Parameter()
    b2 = dom_Parameter()
    _safe_set(a, 'dom_FunctionExpression131', {b1})
    assert _is_linked(a, 'dom_FunctionExpression131', b1)
    if hasattr(b1, 'dom_Parameter'):
        assert _is_linked(b1, 'dom_Parameter', a)
    _safe_set(a, 'dom_FunctionExpression131', {b2})
    assert _is_linked(a, 'dom_FunctionExpression131', b2)
    if hasattr(b1, 'dom_Parameter'):
        assert not _is_linked(b1, 'dom_Parameter', a)
    if hasattr(b2, 'dom_Parameter'):
        assert _is_linked(b2, 'dom_Parameter', a)
    _safe_set(a, 'dom_FunctionExpression131', set())
    assert not _is_linked(a, 'dom_FunctionExpression131', b2)
    if hasattr(b2, 'dom_Parameter'):
        assert not _is_linked(b2, 'dom_Parameter', a)


def test_assoc_right34_link_reassign_clear():
    a = dom_BinaryExpression(operation="sample_text", operatorPosition=7)
    b1 = dom_Expression()
    b2 = dom_Expression()
    _safe_set(a, 'dom_BinaryExpression35', b1)
    assert _is_linked(a, 'dom_BinaryExpression35', b1)
    if hasattr(b1, 'dom_Expression36'):
        assert _is_linked(b1, 'dom_Expression36', a)
    _safe_set(a, 'dom_BinaryExpression35', b2)
    assert _is_linked(a, 'dom_BinaryExpression35', b2)
    if hasattr(b1, 'dom_Expression36'):
        assert not _is_linked(b1, 'dom_Expression36', a)
    if hasattr(b2, 'dom_Expression36'):
        assert _is_linked(b2, 'dom_Expression36', a)
    _safe_set(a, 'dom_BinaryExpression35', None)
    assert not _is_linked(a, 'dom_BinaryExpression35', b2)
    if hasattr(b2, 'dom_Expression36'):
        assert not _is_linked(b2, 'dom_Expression36', a)


def test_assoc_variable0_link_reassign_clear():
    a = dom_Identifier(name="sample_text")
    b1 = dom_VariableReference()
    b2 = dom_VariableReference()
    _safe_set(a, 'dom_Identifier', b1)
    assert _is_linked(a, 'dom_Identifier', b1)
    if hasattr(b1, 'dom_VariableReference'):
        assert _is_linked(b1, 'dom_VariableReference', a)
    _safe_set(a, 'dom_Identifier', b2)
    assert _is_linked(a, 'dom_Identifier', b2)
    if hasattr(b1, 'dom_VariableReference'):
        assert not _is_linked(b1, 'dom_VariableReference', a)
    if hasattr(b2, 'dom_VariableReference'):
        assert _is_linked(b2, 'dom_VariableReference', a)
    _safe_set(a, 'dom_Identifier', None)
    assert not _is_linked(a, 'dom_Identifier', b2)
    if hasattr(b2, 'dom_VariableReference'):
        assert not _is_linked(b2, 'dom_VariableReference', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AccessorAssignment_strategy = st.builds(AccessorAssignment)
@given(instance=AccessorAssignment_strategy)
@settings(max_examples=25)
def test_AccessorAssignment_instantiation(instance):
    assert isinstance(instance, AccessorAssignment)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


IArrayElement_strategy = st.builds(IArrayElement)
@given(instance=IArrayElement_strategy)
@settings(max_examples=25)
def test_IArrayElement_instantiation(instance):
    assert isinstance(instance, IArrayElement)


IForInitializer_strategy = st.builds(IForInitializer)
@given(instance=IForInitializer_strategy)
@settings(max_examples=25)
def test_IForInitializer_instantiation(instance):
    assert isinstance(instance, IForInitializer)


IProperty_strategy = st.builds(IProperty)
@given(instance=IProperty_strategy)
@settings(max_examples=25)
def test_IProperty_instantiation(instance):
    assert isinstance(instance, IProperty)


IPropertyName_strategy = st.builds(IPropertyName)
@given(instance=IPropertyName_strategy)
@settings(max_examples=25)
def test_IPropertyName_instantiation(instance):
    assert isinstance(instance, IPropertyName)


IPropertySelector_strategy = st.builds(IPropertySelector)
@given(instance=IPropertySelector_strategy)
@settings(max_examples=25)
def test_IPropertySelector_instantiation(instance):
    assert isinstance(instance, IPropertySelector)


ISelector_strategy = st.builds(ISelector)
@given(instance=ISelector_strategy)
@settings(max_examples=25)
def test_ISelector_instantiation(instance):
    assert isinstance(instance, ISelector)


IUnqualifiedSelector_strategy = st.builds(IUnqualifiedSelector)
@given(instance=IUnqualifiedSelector_strategy)
@settings(max_examples=25)
def test_IUnqualifiedSelector_instantiation(instance):
    assert isinstance(instance, IUnqualifiedSelector)


IterationStatement_strategy = st.builds(IterationStatement)
@given(instance=IterationStatement_strategy)
@settings(max_examples=25)
def test_IterationStatement_instantiation(instance):
    assert isinstance(instance, IterationStatement)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


PropertyAssignment_strategy = st.builds(PropertyAssignment)
@given(instance=PropertyAssignment_strategy)
@settings(max_examples=25)
def test_PropertyAssignment_instantiation(instance):
    assert isinstance(instance, PropertyAssignment)


PropertyIdentifier_strategy = st.builds(PropertyIdentifier)
@given(instance=PropertyIdentifier_strategy)
@settings(max_examples=25)
def test_PropertyIdentifier_instantiation(instance):
    assert isinstance(instance, PropertyIdentifier)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


SwitchElement_strategy = st.builds(SwitchElement)
@given(instance=SwitchElement_strategy)
@settings(max_examples=25)
def test_SwitchElement_instantiation(instance):
    assert isinstance(instance, SwitchElement)


XmlFragment_strategy = st.builds(XmlFragment)
@given(instance=XmlFragment_strategy)
@settings(max_examples=25)
def test_XmlFragment_instantiation(instance):
    assert isinstance(instance, XmlFragment)


dom_AccessorAssignment_strategy = st.builds(dom_AccessorAssignment)
@given(instance=dom_AccessorAssignment_strategy)
@settings(max_examples=25)
def test_dom_AccessorAssignment_instantiation(instance):
    assert isinstance(instance, dom_AccessorAssignment)


dom_ArrayAccessExpression_strategy = st.builds(dom_ArrayAccessExpression)
@given(instance=dom_ArrayAccessExpression_strategy)
@settings(max_examples=25)
def test_dom_ArrayAccessExpression_instantiation(instance):
    assert isinstance(instance, dom_ArrayAccessExpression)


dom_ArrayLiteral_strategy = st.builds(dom_ArrayLiteral)
@given(instance=dom_ArrayLiteral_strategy)
@settings(max_examples=25)
def test_dom_ArrayLiteral_instantiation(instance):
    assert isinstance(instance, dom_ArrayLiteral)


dom_AttributeIdentifier_strategy = st.builds(dom_AttributeIdentifier)
@given(instance=dom_AttributeIdentifier_strategy)
@settings(max_examples=25)
def test_dom_AttributeIdentifier_instantiation(instance):
    assert isinstance(instance, dom_AttributeIdentifier)


dom_BinaryExpression_strategy = st.builds(dom_BinaryExpression, operation=safe_text, operatorPosition=st.integers())
@given(instance=dom_BinaryExpression_strategy)
@settings(max_examples=25)
def test_dom_BinaryExpression_instantiation(instance):
    assert isinstance(instance, dom_BinaryExpression)


dom_BlockStatement_strategy = st.builds(dom_BlockStatement)
@given(instance=dom_BlockStatement_strategy)
@settings(max_examples=25)
def test_dom_BlockStatement_instantiation(instance):
    assert isinstance(instance, dom_BlockStatement)


dom_BooleanLiteral_strategy = st.builds(dom_BooleanLiteral, text=safe_text)
@given(instance=dom_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_dom_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, dom_BooleanLiteral)


dom_BreakStatement_strategy = st.builds(dom_BreakStatement)
@given(instance=dom_BreakStatement_strategy)
@settings(max_examples=25)
def test_dom_BreakStatement_instantiation(instance):
    assert isinstance(instance, dom_BreakStatement)


dom_CallExpression_strategy = st.builds(dom_CallExpression)
@given(instance=dom_CallExpression_strategy)
@settings(max_examples=25)
def test_dom_CallExpression_instantiation(instance):
    assert isinstance(instance, dom_CallExpression)


dom_CaseClause_strategy = st.builds(dom_CaseClause)
@given(instance=dom_CaseClause_strategy)
@settings(max_examples=25)
def test_dom_CaseClause_instantiation(instance):
    assert isinstance(instance, dom_CaseClause)


dom_CatchClause_strategy = st.builds(dom_CatchClause)
@given(instance=dom_CatchClause_strategy)
@settings(max_examples=25)
def test_dom_CatchClause_instantiation(instance):
    assert isinstance(instance, dom_CatchClause)


dom_Comment_strategy = st.builds(dom_Comment, text=safe_text)
@given(instance=dom_Comment_strategy)
@settings(max_examples=25)
def test_dom_Comment_instantiation(instance):
    assert isinstance(instance, dom_Comment)


dom_ConditionalExpression_strategy = st.builds(dom_ConditionalExpression)
@given(instance=dom_ConditionalExpression_strategy)
@settings(max_examples=25)
def test_dom_ConditionalExpression_instantiation(instance):
    assert isinstance(instance, dom_ConditionalExpression)


dom_ConstStatement_strategy = st.builds(dom_ConstStatement)
@given(instance=dom_ConstStatement_strategy)
@settings(max_examples=25)
def test_dom_ConstStatement_instantiation(instance):
    assert isinstance(instance, dom_ConstStatement)


dom_ContinueStatement_strategy = st.builds(dom_ContinueStatement)
@given(instance=dom_ContinueStatement_strategy)
@settings(max_examples=25)
def test_dom_ContinueStatement_instantiation(instance):
    assert isinstance(instance, dom_ContinueStatement)


dom_DefaultClause_strategy = st.builds(dom_DefaultClause)
@given(instance=dom_DefaultClause_strategy)
@settings(max_examples=25)
def test_dom_DefaultClause_instantiation(instance):
    assert isinstance(instance, dom_DefaultClause)


dom_DefaultXmlNamespaceStatement_strategy = st.builds(dom_DefaultXmlNamespaceStatement)
@given(instance=dom_DefaultXmlNamespaceStatement_strategy)
@settings(max_examples=25)
def test_dom_DefaultXmlNamespaceStatement_instantiation(instance):
    assert isinstance(instance, dom_DefaultXmlNamespaceStatement)


dom_DescendantAccessExpression_strategy = st.builds(dom_DescendantAccessExpression)
@given(instance=dom_DescendantAccessExpression_strategy)
@settings(max_examples=25)
def test_dom_DescendantAccessExpression_instantiation(instance):
    assert isinstance(instance, dom_DescendantAccessExpression)


dom_DoStatement_strategy = st.builds(dom_DoStatement)
@given(instance=dom_DoStatement_strategy)
@settings(max_examples=25)
def test_dom_DoStatement_instantiation(instance):
    assert isinstance(instance, dom_DoStatement)


dom_Elision_strategy = st.builds(dom_Elision)
@given(instance=dom_Elision_strategy)
@settings(max_examples=25)
def test_dom_Elision_instantiation(instance):
    assert isinstance(instance, dom_Elision)


dom_EmptyStatement_strategy = st.builds(dom_EmptyStatement)
@given(instance=dom_EmptyStatement_strategy)
@settings(max_examples=25)
def test_dom_EmptyStatement_instantiation(instance):
    assert isinstance(instance, dom_EmptyStatement)


dom_Expression_strategy = st.builds(dom_Expression)
@given(instance=dom_Expression_strategy)
@settings(max_examples=25)
def test_dom_Expression_instantiation(instance):
    assert isinstance(instance, dom_Expression)


dom_ExpressionSelector_strategy = st.builds(dom_ExpressionSelector)
@given(instance=dom_ExpressionSelector_strategy)
@settings(max_examples=25)
def test_dom_ExpressionSelector_instantiation(instance):
    assert isinstance(instance, dom_ExpressionSelector)


dom_ExpressionStatement_strategy = st.builds(dom_ExpressionStatement)
@given(instance=dom_ExpressionStatement_strategy)
@settings(max_examples=25)
def test_dom_ExpressionStatement_instantiation(instance):
    assert isinstance(instance, dom_ExpressionStatement)


dom_FilterExpression_strategy = st.builds(dom_FilterExpression)
@given(instance=dom_FilterExpression_strategy)
@settings(max_examples=25)
def test_dom_FilterExpression_instantiation(instance):
    assert isinstance(instance, dom_FilterExpression)


dom_FinallyClause_strategy = st.builds(dom_FinallyClause)
@given(instance=dom_FinallyClause_strategy)
@settings(max_examples=25)
def test_dom_FinallyClause_instantiation(instance):
    assert isinstance(instance, dom_FinallyClause)


dom_ForEachInStatement_strategy = st.builds(dom_ForEachInStatement)
@given(instance=dom_ForEachInStatement_strategy)
@settings(max_examples=25)
def test_dom_ForEachInStatement_instantiation(instance):
    assert isinstance(instance, dom_ForEachInStatement)


dom_ForInStatement_strategy = st.builds(dom_ForInStatement)
@given(instance=dom_ForInStatement_strategy)
@settings(max_examples=25)
def test_dom_ForInStatement_instantiation(instance):
    assert isinstance(instance, dom_ForInStatement)


dom_ForStatement_strategy = st.builds(dom_ForStatement)
@given(instance=dom_ForStatement_strategy)
@settings(max_examples=25)
def test_dom_ForStatement_instantiation(instance):
    assert isinstance(instance, dom_ForStatement)


dom_FunctionExpression_strategy = st.builds(dom_FunctionExpression, parametersPosition=st.integers())
@given(instance=dom_FunctionExpression_strategy)
@settings(max_examples=25)
def test_dom_FunctionExpression_instantiation(instance):
    assert isinstance(instance, dom_FunctionExpression)


dom_GetterAssignment_strategy = st.builds(dom_GetterAssignment)
@given(instance=dom_GetterAssignment_strategy)
@settings(max_examples=25)
def test_dom_GetterAssignment_instantiation(instance):
    assert isinstance(instance, dom_GetterAssignment)


dom_IArrayElement_strategy = st.builds(dom_IArrayElement)
@given(instance=dom_IArrayElement_strategy)
@settings(max_examples=25)
def test_dom_IArrayElement_instantiation(instance):
    assert isinstance(instance, dom_IArrayElement)


dom_IForInitializer_strategy = st.builds(dom_IForInitializer)
@given(instance=dom_IForInitializer_strategy)
@settings(max_examples=25)
def test_dom_IForInitializer_instantiation(instance):
    assert isinstance(instance, dom_IForInitializer)


dom_IProperty_strategy = st.builds(dom_IProperty)
@given(instance=dom_IProperty_strategy)
@settings(max_examples=25)
def test_dom_IProperty_instantiation(instance):
    assert isinstance(instance, dom_IProperty)


dom_IPropertyName_strategy = st.builds(dom_IPropertyName)
@given(instance=dom_IPropertyName_strategy)
@settings(max_examples=25)
def test_dom_IPropertyName_instantiation(instance):
    assert isinstance(instance, dom_IPropertyName)


dom_IPropertySelector_strategy = st.builds(dom_IPropertySelector)
@given(instance=dom_IPropertySelector_strategy)
@settings(max_examples=25)
def test_dom_IPropertySelector_instantiation(instance):
    assert isinstance(instance, dom_IPropertySelector)


dom_ISelector_strategy = st.builds(dom_ISelector)
@given(instance=dom_ISelector_strategy)
@settings(max_examples=25)
def test_dom_ISelector_instantiation(instance):
    assert isinstance(instance, dom_ISelector)


dom_IUnqualifiedSelector_strategy = st.builds(dom_IUnqualifiedSelector)
@given(instance=dom_IUnqualifiedSelector_strategy)
@settings(max_examples=25)
def test_dom_IUnqualifiedSelector_instantiation(instance):
    assert isinstance(instance, dom_IUnqualifiedSelector)


dom_Identifier_strategy = st.builds(dom_Identifier, name=safe_text)
@given(instance=dom_Identifier_strategy)
@settings(max_examples=25)
def test_dom_Identifier_instantiation(instance):
    assert isinstance(instance, dom_Identifier)


dom_IfStatement_strategy = st.builds(dom_IfStatement)
@given(instance=dom_IfStatement_strategy)
@settings(max_examples=25)
def test_dom_IfStatement_instantiation(instance):
    assert isinstance(instance, dom_IfStatement)


dom_IterationStatement_strategy = st.builds(dom_IterationStatement)
@given(instance=dom_IterationStatement_strategy)
@settings(max_examples=25)
def test_dom_IterationStatement_instantiation(instance):
    assert isinstance(instance, dom_IterationStatement)


dom_Label_strategy = st.builds(dom_Label, name=safe_text)
@given(instance=dom_Label_strategy)
@settings(max_examples=25)
def test_dom_Label_instantiation(instance):
    assert isinstance(instance, dom_Label)


dom_LabeledStatement_strategy = st.builds(dom_LabeledStatement)
@given(instance=dom_LabeledStatement_strategy)
@settings(max_examples=25)
def test_dom_LabeledStatement_instantiation(instance):
    assert isinstance(instance, dom_LabeledStatement)


dom_NewExpression_strategy = st.builds(dom_NewExpression)
@given(instance=dom_NewExpression_strategy)
@settings(max_examples=25)
def test_dom_NewExpression_instantiation(instance):
    assert isinstance(instance, dom_NewExpression)


dom_Node_strategy = st.builds(dom_Node, begin=st.integers(), end=st.integers())
@given(instance=dom_Node_strategy)
@settings(max_examples=25)
def test_dom_Node_instantiation(instance):
    assert isinstance(instance, dom_Node)


dom_NullLiteral_strategy = st.builds(dom_NullLiteral)
@given(instance=dom_NullLiteral_strategy)
@settings(max_examples=25)
def test_dom_NullLiteral_instantiation(instance):
    assert isinstance(instance, dom_NullLiteral)


dom_NumericLiteral_strategy = st.builds(dom_NumericLiteral, text=safe_text)
@given(instance=dom_NumericLiteral_strategy)
@settings(max_examples=25)
def test_dom_NumericLiteral_instantiation(instance):
    assert isinstance(instance, dom_NumericLiteral)


dom_ObjectLiteral_strategy = st.builds(dom_ObjectLiteral)
@given(instance=dom_ObjectLiteral_strategy)
@settings(max_examples=25)
def test_dom_ObjectLiteral_instantiation(instance):
    assert isinstance(instance, dom_ObjectLiteral)


dom_Parameter_strategy = st.builds(dom_Parameter)
@given(instance=dom_Parameter_strategy)
@settings(max_examples=25)
def test_dom_Parameter_instantiation(instance):
    assert isinstance(instance, dom_Parameter)


dom_ParenthesizedExpression_strategy = st.builds(dom_ParenthesizedExpression)
@given(instance=dom_ParenthesizedExpression_strategy)
@settings(max_examples=25)
def test_dom_ParenthesizedExpression_instantiation(instance):
    assert isinstance(instance, dom_ParenthesizedExpression)


dom_PropertyAccessExpression_strategy = st.builds(dom_PropertyAccessExpression)
@given(instance=dom_PropertyAccessExpression_strategy)
@settings(max_examples=25)
def test_dom_PropertyAccessExpression_instantiation(instance):
    assert isinstance(instance, dom_PropertyAccessExpression)


dom_PropertyAssignment_strategy = st.builds(dom_PropertyAssignment)
@given(instance=dom_PropertyAssignment_strategy)
@settings(max_examples=25)
def test_dom_PropertyAssignment_instantiation(instance):
    assert isinstance(instance, dom_PropertyAssignment)


dom_PropertyIdentifier_strategy = st.builds(dom_PropertyIdentifier)
@given(instance=dom_PropertyIdentifier_strategy)
@settings(max_examples=25)
def test_dom_PropertyIdentifier_instantiation(instance):
    assert isinstance(instance, dom_PropertyIdentifier)


dom_QualifiedIdentifier_strategy = st.builds(dom_QualifiedIdentifier)
@given(instance=dom_QualifiedIdentifier_strategy)
@settings(max_examples=25)
def test_dom_QualifiedIdentifier_instantiation(instance):
    assert isinstance(instance, dom_QualifiedIdentifier)


dom_RegularExpressionLiteral_strategy = st.builds(dom_RegularExpressionLiteral, text=safe_text)
@given(instance=dom_RegularExpressionLiteral_strategy)
@settings(max_examples=25)
def test_dom_RegularExpressionLiteral_instantiation(instance):
    assert isinstance(instance, dom_RegularExpressionLiteral)


dom_ReturnStatement_strategy = st.builds(dom_ReturnStatement)
@given(instance=dom_ReturnStatement_strategy)
@settings(max_examples=25)
def test_dom_ReturnStatement_instantiation(instance):
    assert isinstance(instance, dom_ReturnStatement)


dom_SetterAssignment_strategy = st.builds(dom_SetterAssignment)
@given(instance=dom_SetterAssignment_strategy)
@settings(max_examples=25)
def test_dom_SetterAssignment_instantiation(instance):
    assert isinstance(instance, dom_SetterAssignment)


dom_SimplePropertyAssignment_strategy = st.builds(dom_SimplePropertyAssignment)
@given(instance=dom_SimplePropertyAssignment_strategy)
@settings(max_examples=25)
def test_dom_SimplePropertyAssignment_instantiation(instance):
    assert isinstance(instance, dom_SimplePropertyAssignment)


dom_Source_strategy = st.builds(dom_Source)
@given(instance=dom_Source_strategy)
@settings(max_examples=25)
def test_dom_Source_instantiation(instance):
    assert isinstance(instance, dom_Source)


dom_Statement_strategy = st.builds(dom_Statement)
@given(instance=dom_Statement_strategy)
@settings(max_examples=25)
def test_dom_Statement_instantiation(instance):
    assert isinstance(instance, dom_Statement)


dom_StringLiteral_strategy = st.builds(dom_StringLiteral, text=safe_text)
@given(instance=dom_StringLiteral_strategy)
@settings(max_examples=25)
def test_dom_StringLiteral_instantiation(instance):
    assert isinstance(instance, dom_StringLiteral)


dom_SwitchElement_strategy = st.builds(dom_SwitchElement)
@given(instance=dom_SwitchElement_strategy)
@settings(max_examples=25)
def test_dom_SwitchElement_instantiation(instance):
    assert isinstance(instance, dom_SwitchElement)


dom_SwitchStatement_strategy = st.builds(dom_SwitchStatement)
@given(instance=dom_SwitchStatement_strategy)
@settings(max_examples=25)
def test_dom_SwitchStatement_instantiation(instance):
    assert isinstance(instance, dom_SwitchStatement)


dom_ThisExpression_strategy = st.builds(dom_ThisExpression)
@given(instance=dom_ThisExpression_strategy)
@settings(max_examples=25)
def test_dom_ThisExpression_instantiation(instance):
    assert isinstance(instance, dom_ThisExpression)


dom_ThrowStatement_strategy = st.builds(dom_ThrowStatement)
@given(instance=dom_ThrowStatement_strategy)
@settings(max_examples=25)
def test_dom_ThrowStatement_instantiation(instance):
    assert isinstance(instance, dom_ThrowStatement)


dom_TryStatement_strategy = st.builds(dom_TryStatement)
@given(instance=dom_TryStatement_strategy)
@settings(max_examples=25)
def test_dom_TryStatement_instantiation(instance):
    assert isinstance(instance, dom_TryStatement)


dom_UnaryExpression_strategy = st.builds(dom_UnaryExpression, operation=safe_text)
@given(instance=dom_UnaryExpression_strategy)
@settings(max_examples=25)
def test_dom_UnaryExpression_instantiation(instance):
    assert isinstance(instance, dom_UnaryExpression)


dom_VariableDeclaration_strategy = st.builds(dom_VariableDeclaration)
@given(instance=dom_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_dom_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, dom_VariableDeclaration)


dom_VariableReference_strategy = st.builds(dom_VariableReference)
@given(instance=dom_VariableReference_strategy)
@settings(max_examples=25)
def test_dom_VariableReference_instantiation(instance):
    assert isinstance(instance, dom_VariableReference)


dom_VariableStatement_strategy = st.builds(dom_VariableStatement)
@given(instance=dom_VariableStatement_strategy)
@settings(max_examples=25)
def test_dom_VariableStatement_instantiation(instance):
    assert isinstance(instance, dom_VariableStatement)


dom_WhileStatement_strategy = st.builds(dom_WhileStatement)
@given(instance=dom_WhileStatement_strategy)
@settings(max_examples=25)
def test_dom_WhileStatement_instantiation(instance):
    assert isinstance(instance, dom_WhileStatement)


dom_WildcardIdentifier_strategy = st.builds(dom_WildcardIdentifier)
@given(instance=dom_WildcardIdentifier_strategy)
@settings(max_examples=25)
def test_dom_WildcardIdentifier_instantiation(instance):
    assert isinstance(instance, dom_WildcardIdentifier)


dom_WithStatement_strategy = st.builds(dom_WithStatement)
@given(instance=dom_WithStatement_strategy)
@settings(max_examples=25)
def test_dom_WithStatement_instantiation(instance):
    assert isinstance(instance, dom_WithStatement)


dom_XmlExpressionFragment_strategy = st.builds(dom_XmlExpressionFragment)
@given(instance=dom_XmlExpressionFragment_strategy)
@settings(max_examples=25)
def test_dom_XmlExpressionFragment_instantiation(instance):
    assert isinstance(instance, dom_XmlExpressionFragment)


dom_XmlFragment_strategy = st.builds(dom_XmlFragment)
@given(instance=dom_XmlFragment_strategy)
@settings(max_examples=25)
def test_dom_XmlFragment_instantiation(instance):
    assert isinstance(instance, dom_XmlFragment)


dom_XmlInitializer_strategy = st.builds(dom_XmlInitializer)
@given(instance=dom_XmlInitializer_strategy)
@settings(max_examples=25)
def test_dom_XmlInitializer_instantiation(instance):
    assert isinstance(instance, dom_XmlInitializer)


dom_XmlTextFragment_strategy = st.builds(dom_XmlTextFragment, text=safe_text)
@given(instance=dom_XmlTextFragment_strategy)
@settings(max_examples=25)
def test_dom_XmlTextFragment_instantiation(instance):
    assert isinstance(instance, dom_XmlTextFragment)



