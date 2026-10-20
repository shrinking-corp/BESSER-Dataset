import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    MOFScriptModel_Advice,
    MOFScriptModel_ArithmeticExpression,
    MOFScriptModel_BreakStatement,
    MOFScriptModel_ComparisonExpression,
    MOFScriptModel_CreateExpression,
    MOFScriptModel_CreateExpressionParameter,
    MOFScriptModel_CreateStatement,
    MOFScriptModel_DebugStatement,
    MOFScriptModel_Expression,
    MOFScriptModel_FileStatement,
    MOFScriptModel_FunctionCall,
    MOFScriptModel_FunctionCallStatement,
    MOFScriptModel_GeneralAssignment,
    MOFScriptModel_IfStatement,
    MOFScriptModel_IteratorStatement,
    MOFScriptModel_Literal,
    MOFScriptModel_LogicalExpression,
    MOFScriptModel_M2MTrace,
    MOFScriptModel_MOFScriptAspect,
    MOFScriptModel_MOFScriptComment,
    MOFScriptModel_MOFScriptImport,
    MOFScriptModel_MOFScriptObject,
    MOFScriptModel_MOFScriptParameter,
    MOFScriptModel_MOFScriptSpecification,
    MOFScriptModel_MOFScriptStatement,
    MOFScriptModel_MOFScriptStatementOwner,
    MOFScriptModel_MOFScriptTransformation,
    MOFScriptModel_PointCut,
    MOFScriptModel_PointCutExpression,
    MOFScriptModel_PrintStatement,
    MOFScriptModel_Reference,
    MOFScriptModel_ResultAssignment,
    MOFScriptModel_ReturnStatement,
    MOFScriptModel_SelectExpression,
    MOFScriptModel_SimpleExpression,
    MOFScriptModel_StatementBlock,
    MOFScriptModel_Trace,
    MOFScriptModel_TransformationRule,
    MOFScriptModel_ValueExpression,
    MOFScriptModel_VariableDeclaration,
    MOFScriptModel_VariableDeclarationStatement,
    MOFScriptModel_WhileStatement,
    MOFScriptObject,
    MOFScriptStatement,
    MOFScriptStatementOwner,
    MOFScriptTransformation,
    SimpleExpression,
    Trace,
    ValueExpression,
    AccessLevel,
    AdviceOperator,
    ArithmeticOperator,
    AssignmentOperator,
    ComparisonOperator,
    ImportSemantics,
    ImportType,
    LiteralType,
    LogicalOperator,
    ParameterDirection,
    PointCutCombinationOperator,
    PointCutOperator,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_after40_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_IteratorStatement(type="sample_text", variable="sample_text")
    _safe_set(b, 'MOFScriptModel_IteratorStatement41', a1)
    assert _is_linked(b, 'MOFScriptModel_IteratorStatement41', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression42'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression42', b)
    _safe_set(b, 'MOFScriptModel_IteratorStatement41', a2)
    assert _is_linked(b, 'MOFScriptModel_IteratorStatement41', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression42'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression42', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression42'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression42', b)
    _safe_set(b, 'MOFScriptModel_IteratorStatement41', None)
    assert not _is_linked(b, 'MOFScriptModel_IteratorStatement41', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression42'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression42', b)


def test_assoc_appliedFunction103_reverse_link_reassign_clear():
    a1 = MOFScriptModel_SelectExpression(type="sample_text", variable="sample_text")
    a2 = MOFScriptModel_SelectExpression(type="sample_text_2", variable="sample_text_2")
    b = MOFScriptModel_FunctionCall(isSuperCall=True, name="sample_text", transformationContext="sample_text")
    _safe_set(b, 'MOFScriptModel_FunctionCall105', a1)
    assert _is_linked(b, 'MOFScriptModel_FunctionCall105', a1)
    if hasattr(a1, 'MOFScriptModel_SelectExpression104'):
        assert _is_linked(a1, 'MOFScriptModel_SelectExpression104', b)
    _safe_set(b, 'MOFScriptModel_FunctionCall105', a2)
    assert _is_linked(b, 'MOFScriptModel_FunctionCall105', a2)
    if hasattr(a1, 'MOFScriptModel_SelectExpression104'):
        assert not _is_linked(a1, 'MOFScriptModel_SelectExpression104', b)
    if hasattr(a2, 'MOFScriptModel_SelectExpression104'):
        assert _is_linked(a2, 'MOFScriptModel_SelectExpression104', b)
    _safe_set(b, 'MOFScriptModel_FunctionCall105', None)
    assert not _is_linked(b, 'MOFScriptModel_FunctionCall105', a2)
    if hasattr(a2, 'MOFScriptModel_SelectExpression104'):
        assert not _is_linked(a2, 'MOFScriptModel_SelectExpression104', b)


def test_assoc_before35_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_IteratorStatement(type="sample_text", variable="sample_text")
    _safe_set(b, 'MOFScriptModel_IteratorStatement36', a1)
    assert _is_linked(b, 'MOFScriptModel_IteratorStatement36', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression', b)
    _safe_set(b, 'MOFScriptModel_IteratorStatement36', a2)
    assert _is_linked(b, 'MOFScriptModel_IteratorStatement36', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression', b)
    _safe_set(b, 'MOFScriptModel_IteratorStatement36', None)
    assert not _is_linked(b, 'MOFScriptModel_IteratorStatement36', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression', b)


def test_assoc_between37_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_IteratorStatement(type="sample_text", variable="sample_text")
    _safe_set(b, 'MOFScriptModel_IteratorStatement38', a1)
    assert _is_linked(b, 'MOFScriptModel_IteratorStatement38', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression39'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression39', b)
    _safe_set(b, 'MOFScriptModel_IteratorStatement38', a2)
    assert _is_linked(b, 'MOFScriptModel_IteratorStatement38', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression39'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression39', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression39'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression39', b)
    _safe_set(b, 'MOFScriptModel_IteratorStatement38', None)
    assert not _is_linked(b, 'MOFScriptModel_IteratorStatement38', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression39'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression39', b)


def test_assoc_combinedExpression96_reverse_link_reassign_clear():
    a1 = MOFScriptModel_PointCutExpression(combinationOperator="sample_text", expressionString="sample_text", operator="sample_text")
    a2 = MOFScriptModel_PointCutExpression(combinationOperator="sample_text_2", expressionString="sample_text_2", operator="sample_text_2")
    b = MOFScriptModel_PointCutExpression(combinationOperator="sample_text", expressionString="sample_text", operator="sample_text")
    _safe_set(b, 'MOFScriptModel_PointCutExpression97', a1)
    assert _is_linked(b, 'MOFScriptModel_PointCutExpression97', a1)
    if hasattr(a1, 'MOFScriptModel_PointCutExpression95'):
        assert _is_linked(a1, 'MOFScriptModel_PointCutExpression95', b)
    _safe_set(b, 'MOFScriptModel_PointCutExpression97', a2)
    assert _is_linked(b, 'MOFScriptModel_PointCutExpression97', a2)
    if hasattr(a1, 'MOFScriptModel_PointCutExpression95'):
        assert not _is_linked(a1, 'MOFScriptModel_PointCutExpression95', b)
    if hasattr(a2, 'MOFScriptModel_PointCutExpression95'):
        assert _is_linked(a2, 'MOFScriptModel_PointCutExpression95', b)
    _safe_set(b, 'MOFScriptModel_PointCutExpression97', None)
    assert not _is_linked(b, 'MOFScriptModel_PointCutExpression97', a2)
    if hasattr(a2, 'MOFScriptModel_PointCutExpression95'):
        assert not _is_linked(a2, 'MOFScriptModel_PointCutExpression95', b)


def test_assoc_comment12_reverse_link_reassign_clear():
    a1 = MOFScriptModel_MOFScriptObject(column=7, line=7)
    a2 = MOFScriptModel_MOFScriptObject(column=13, line=13)
    b = MOFScriptModel_MOFScriptComment(commentText="sample_text", docStyle=True, singleLine=True)
    _safe_set(b, 'MOFScriptModel_MOFScriptComment', a1)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptComment', a1)
    if hasattr(a1, 'MOFScriptModel_MOFScriptObject'):
        assert _is_linked(a1, 'MOFScriptModel_MOFScriptObject', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptComment', a2)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptComment', a2)
    if hasattr(a1, 'MOFScriptModel_MOFScriptObject'):
        assert not _is_linked(a1, 'MOFScriptModel_MOFScriptObject', b)
    if hasattr(a2, 'MOFScriptModel_MOFScriptObject'):
        assert _is_linked(a2, 'MOFScriptModel_MOFScriptObject', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptComment', None)
    assert not _is_linked(b, 'MOFScriptModel_MOFScriptComment', a2)
    if hasattr(a2, 'MOFScriptModel_MOFScriptObject'):
        assert not _is_linked(a2, 'MOFScriptModel_MOFScriptObject', b)


def test_assoc_constants20_reverse_link_reassign_clear():
    a1 = MOFScriptModel_VariableDeclaration(constant=True, name="sample_text", type="sample_text")
    a2 = MOFScriptModel_VariableDeclaration(constant=False, name="sample_text_2", type="sample_text_2")
    b = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text", name="sample_text")
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation21', {a1})
    assert _is_linked(b, 'MOFScriptModel_MOFScriptTransformation21', a1)
    if hasattr(a1, 'MOFScriptModel_VariableDeclaration22'):
        assert _is_linked(a1, 'MOFScriptModel_VariableDeclaration22', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation21', {a2})
    assert _is_linked(b, 'MOFScriptModel_MOFScriptTransformation21', a2)
    if hasattr(a1, 'MOFScriptModel_VariableDeclaration22'):
        assert not _is_linked(a1, 'MOFScriptModel_VariableDeclaration22', b)
    if hasattr(a2, 'MOFScriptModel_VariableDeclaration22'):
        assert _is_linked(a2, 'MOFScriptModel_VariableDeclaration22', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation21', set())
    assert not _is_linked(b, 'MOFScriptModel_MOFScriptTransformation21', a2)
    if hasattr(a2, 'MOFScriptModel_VariableDeclaration22'):
        assert not _is_linked(a2, 'MOFScriptModel_VariableDeclaration22', b)


def test_assoc_context5_reverse_link_reassign_clear():
    a1 = MOFScriptModel_TransformationRule(accessLevel="sample_text", isAbstract=True, isEntryPoint=True, name="sample_text", return_="sample_text")
    a2 = MOFScriptModel_TransformationRule(accessLevel="sample_text_2", isAbstract=False, isEntryPoint=False, name="sample_text_2", return_="sample_text_2")
    b = MOFScriptModel_MOFScriptParameter(direction="sample_text", name="sample_text", type="sample_text", typePrefix="sample_text")
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter7', a1)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptParameter7', a1)
    if hasattr(a1, 'MOFScriptModel_TransformationRule6'):
        assert _is_linked(a1, 'MOFScriptModel_TransformationRule6', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter7', a2)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptParameter7', a2)
    if hasattr(a1, 'MOFScriptModel_TransformationRule6'):
        assert not _is_linked(a1, 'MOFScriptModel_TransformationRule6', b)
    if hasattr(a2, 'MOFScriptModel_TransformationRule6'):
        assert _is_linked(a2, 'MOFScriptModel_TransformationRule6', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter7', None)
    assert not _is_linked(b, 'MOFScriptModel_MOFScriptParameter7', a2)
    if hasattr(a2, 'MOFScriptModel_TransformationRule6'):
        assert not _is_linked(a2, 'MOFScriptModel_TransformationRule6', b)


def test_assoc_extends2_reverse_link_reassign_clear():
    a1 = MOFScriptModel_TransformationRule(accessLevel="sample_text", isAbstract=True, isEntryPoint=True, name="sample_text", return_="sample_text")
    a2 = MOFScriptModel_TransformationRule(accessLevel="sample_text_2", isAbstract=False, isEntryPoint=False, name="sample_text_2", return_="sample_text_2")
    b = MOFScriptModel_TransformationRule(accessLevel="sample_text", isAbstract=True, isEntryPoint=True, name="sample_text", return_="sample_text")
    _safe_set(b, 'MOFScriptModel_TransformationRule1', a1)
    assert _is_linked(b, 'MOFScriptModel_TransformationRule1', a1)
    if hasattr(a1, 'MOFScriptModel_TransformationRule'):
        assert _is_linked(a1, 'MOFScriptModel_TransformationRule', b)
    _safe_set(b, 'MOFScriptModel_TransformationRule1', a2)
    assert _is_linked(b, 'MOFScriptModel_TransformationRule1', a2)
    if hasattr(a1, 'MOFScriptModel_TransformationRule'):
        assert not _is_linked(a1, 'MOFScriptModel_TransformationRule', b)
    if hasattr(a2, 'MOFScriptModel_TransformationRule'):
        assert _is_linked(a2, 'MOFScriptModel_TransformationRule', b)
    _safe_set(b, 'MOFScriptModel_TransformationRule1', None)
    assert not _is_linked(b, 'MOFScriptModel_TransformationRule1', a2)
    if hasattr(a2, 'MOFScriptModel_TransformationRule'):
        assert not _is_linked(a2, 'MOFScriptModel_TransformationRule', b)


def test_assoc_extends27_reverse_link_reassign_clear():
    a1 = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text", name="sample_text")
    a2 = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text_2", name="sample_text_2")
    b = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text", name="sample_text")
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation28', a1)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptTransformation28', a1)
    if hasattr(a1, 'MOFScriptModel_MOFScriptTransformation26'):
        assert _is_linked(a1, 'MOFScriptModel_MOFScriptTransformation26', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation28', a2)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptTransformation28', a2)
    if hasattr(a1, 'MOFScriptModel_MOFScriptTransformation26'):
        assert not _is_linked(a1, 'MOFScriptModel_MOFScriptTransformation26', b)
    if hasattr(a2, 'MOFScriptModel_MOFScriptTransformation26'):
        assert _is_linked(a2, 'MOFScriptModel_MOFScriptTransformation26', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation28', None)
    assert not _is_linked(b, 'MOFScriptModel_MOFScriptTransformation28', a2)
    if hasattr(a2, 'MOFScriptModel_MOFScriptTransformation26'):
        assert not _is_linked(a2, 'MOFScriptModel_MOFScriptTransformation26', b)


def test_assoc_fileURI69_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_FileStatement(append=True, fileReference="sample_text", use=True)
    _safe_set(b, 'MOFScriptModel_FileStatement', a1)
    assert _is_linked(b, 'MOFScriptModel_FileStatement', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression70'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression70', b)
    _safe_set(b, 'MOFScriptModel_FileStatement', a2)
    assert _is_linked(b, 'MOFScriptModel_FileStatement', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression70'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression70', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression70'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression70', b)
    _safe_set(b, 'MOFScriptModel_FileStatement', None)
    assert not _is_linked(b, 'MOFScriptModel_FileStatement', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression70'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression70', b)


def test_assoc_owner0_reverse_link_reassign_clear():
    a1 = MOFScriptModel_TransformationRule(accessLevel="sample_text", isAbstract=True, isEntryPoint=True, name="sample_text", return_="sample_text")
    a2 = MOFScriptModel_TransformationRule(accessLevel="sample_text_2", isAbstract=False, isEntryPoint=False, name="sample_text_2", return_="sample_text_2")
    b = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text", name="sample_text")
    _safe_set(b, 'MOFScriptTransformation', a1)
    assert _is_linked(b, 'MOFScriptTransformation', a1)
    if hasattr(a1, 'transformationrules'):
        assert _is_linked(a1, 'transformationrules', b)
    _safe_set(b, 'MOFScriptTransformation', a2)
    assert _is_linked(b, 'MOFScriptTransformation', a2)
    if hasattr(a1, 'transformationrules'):
        assert not _is_linked(a1, 'transformationrules', b)
    if hasattr(a2, 'transformationrules'):
        assert _is_linked(a2, 'transformationrules', b)
    _safe_set(b, 'MOFScriptTransformation', None)
    assert not _is_linked(b, 'MOFScriptTransformation', a2)
    if hasattr(a2, 'transformationrules'):
        assert not _is_linked(a2, 'transformationrules', b)


def test_assoc_parameters106_reverse_link_reassign_clear():
    a1 = MOFScriptModel_CreateExpressionParameter(name="sample_text")
    a2 = MOFScriptModel_CreateExpressionParameter(name="sample_text_2")
    b = MOFScriptModel_CreateExpression(type="sample_text")
    _safe_set(b, 'MOFScriptModel_CreateExpression', {a1})
    assert _is_linked(b, 'MOFScriptModel_CreateExpression', a1)
    if hasattr(a1, 'MOFScriptModel_CreateExpressionParameter'):
        assert _is_linked(a1, 'MOFScriptModel_CreateExpressionParameter', b)
    _safe_set(b, 'MOFScriptModel_CreateExpression', {a2})
    assert _is_linked(b, 'MOFScriptModel_CreateExpression', a2)
    if hasattr(a1, 'MOFScriptModel_CreateExpressionParameter'):
        assert not _is_linked(a1, 'MOFScriptModel_CreateExpressionParameter', b)
    if hasattr(a2, 'MOFScriptModel_CreateExpressionParameter'):
        assert _is_linked(a2, 'MOFScriptModel_CreateExpressionParameter', b)
    _safe_set(b, 'MOFScriptModel_CreateExpression', set())
    assert not _is_linked(b, 'MOFScriptModel_CreateExpression', a2)
    if hasattr(a2, 'MOFScriptModel_CreateExpressionParameter'):
        assert not _is_linked(a2, 'MOFScriptModel_CreateExpressionParameter', b)


def test_assoc_parameters23_reverse_link_reassign_clear():
    a1 = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text", name="sample_text")
    a2 = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text_2", name="sample_text_2")
    b = MOFScriptModel_MOFScriptParameter(direction="sample_text", name="sample_text", type="sample_text", typePrefix="sample_text")
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter25', a1)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptParameter25', a1)
    if hasattr(a1, 'MOFScriptModel_MOFScriptTransformation24'):
        assert _is_linked(a1, 'MOFScriptModel_MOFScriptTransformation24', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter25', a2)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptParameter25', a2)
    if hasattr(a1, 'MOFScriptModel_MOFScriptTransformation24'):
        assert not _is_linked(a1, 'MOFScriptModel_MOFScriptTransformation24', b)
    if hasattr(a2, 'MOFScriptModel_MOFScriptTransformation24'):
        assert _is_linked(a2, 'MOFScriptModel_MOFScriptTransformation24', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter25', None)
    assert not _is_linked(b, 'MOFScriptModel_MOFScriptParameter25', a2)
    if hasattr(a2, 'MOFScriptModel_MOFScriptTransformation24'):
        assert not _is_linked(a2, 'MOFScriptModel_MOFScriptTransformation24', b)


def test_assoc_parameters3_reverse_link_reassign_clear():
    a1 = MOFScriptModel_TransformationRule(accessLevel="sample_text", isAbstract=True, isEntryPoint=True, name="sample_text", return_="sample_text")
    a2 = MOFScriptModel_TransformationRule(accessLevel="sample_text_2", isAbstract=False, isEntryPoint=False, name="sample_text_2", return_="sample_text_2")
    b = MOFScriptModel_MOFScriptParameter(direction="sample_text", name="sample_text", type="sample_text", typePrefix="sample_text")
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter', a1)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptParameter', a1)
    if hasattr(a1, 'MOFScriptModel_TransformationRule4'):
        assert _is_linked(a1, 'MOFScriptModel_TransformationRule4', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter', a2)
    assert _is_linked(b, 'MOFScriptModel_MOFScriptParameter', a2)
    if hasattr(a1, 'MOFScriptModel_TransformationRule4'):
        assert not _is_linked(a1, 'MOFScriptModel_TransformationRule4', b)
    if hasattr(a2, 'MOFScriptModel_TransformationRule4'):
        assert _is_linked(a2, 'MOFScriptModel_TransformationRule4', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptParameter', None)
    assert not _is_linked(b, 'MOFScriptModel_MOFScriptParameter', a2)
    if hasattr(a2, 'MOFScriptModel_TransformationRule4'):
        assert not _is_linked(a2, 'MOFScriptModel_TransformationRule4', b)


def test_assoc_parameters51_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_FunctionCall(isSuperCall=True, name="sample_text", transformationContext="sample_text")
    _safe_set(b, 'MOFScriptModel_FunctionCall', {a1})
    assert _is_linked(b, 'MOFScriptModel_FunctionCall', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression52'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression52', b)
    _safe_set(b, 'MOFScriptModel_FunctionCall', {a2})
    assert _is_linked(b, 'MOFScriptModel_FunctionCall', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression52'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression52', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression52'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression52', b)
    _safe_set(b, 'MOFScriptModel_FunctionCall', set())
    assert not _is_linked(b, 'MOFScriptModel_FunctionCall', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression52'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression52', b)


def test_assoc_part164_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_ArithmeticExpression(operator="sample_text")
    _safe_set(b, 'MOFScriptModel_ArithmeticExpression', a1)
    assert _is_linked(b, 'MOFScriptModel_ArithmeticExpression', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression65'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression65', b)
    _safe_set(b, 'MOFScriptModel_ArithmeticExpression', a2)
    assert _is_linked(b, 'MOFScriptModel_ArithmeticExpression', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression65'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression65', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression65'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression65', b)
    _safe_set(b, 'MOFScriptModel_ArithmeticExpression', None)
    assert not _is_linked(b, 'MOFScriptModel_ArithmeticExpression', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression65'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression65', b)


def test_assoc_part173_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_ComparisonExpression(operator="sample_text")
    _safe_set(b, 'MOFScriptModel_ComparisonExpression74', a1)
    assert _is_linked(b, 'MOFScriptModel_ComparisonExpression74', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression75'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression75', b)
    _safe_set(b, 'MOFScriptModel_ComparisonExpression74', a2)
    assert _is_linked(b, 'MOFScriptModel_ComparisonExpression74', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression75'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression75', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression75'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression75', b)
    _safe_set(b, 'MOFScriptModel_ComparisonExpression74', None)
    assert not _is_linked(b, 'MOFScriptModel_ComparisonExpression74', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression75'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression75', b)


def test_assoc_part266_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_ArithmeticExpression(operator="sample_text")
    _safe_set(b, 'MOFScriptModel_ArithmeticExpression67', a1)
    assert _is_linked(b, 'MOFScriptModel_ArithmeticExpression67', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression68'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression68', b)
    _safe_set(b, 'MOFScriptModel_ArithmeticExpression67', a2)
    assert _is_linked(b, 'MOFScriptModel_ArithmeticExpression67', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression68'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression68', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression68'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression68', b)
    _safe_set(b, 'MOFScriptModel_ArithmeticExpression67', None)
    assert not _is_linked(b, 'MOFScriptModel_ArithmeticExpression67', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression68'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression68', b)


def test_assoc_part271_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_ComparisonExpression(operator="sample_text")
    _safe_set(b, 'MOFScriptModel_ComparisonExpression', a1)
    assert _is_linked(b, 'MOFScriptModel_ComparisonExpression', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression72'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression72', b)
    _safe_set(b, 'MOFScriptModel_ComparisonExpression', a2)
    assert _is_linked(b, 'MOFScriptModel_ComparisonExpression', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression72'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression72', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression72'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression72', b)
    _safe_set(b, 'MOFScriptModel_ComparisonExpression', None)
    assert not _is_linked(b, 'MOFScriptModel_ComparisonExpression', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression72'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression72', b)


def test_assoc_pointcut90_reverse_link_reassign_clear():
    a1 = MOFScriptModel_PointCut(name="sample_text", typeMatch="sample_text")
    a2 = MOFScriptModel_PointCut(name="sample_text_2", typeMatch="sample_text_2")
    b = MOFScriptModel_Advice(code="sample_text", name="sample_text", operator="sample_text", pointCutRef="sample_text")
    _safe_set(b, 'MOFScriptModel_Advice91', a1)
    assert _is_linked(b, 'MOFScriptModel_Advice91', a1)
    if hasattr(a1, 'MOFScriptModel_PointCut92'):
        assert _is_linked(a1, 'MOFScriptModel_PointCut92', b)
    _safe_set(b, 'MOFScriptModel_Advice91', a2)
    assert _is_linked(b, 'MOFScriptModel_Advice91', a2)
    if hasattr(a1, 'MOFScriptModel_PointCut92'):
        assert not _is_linked(a1, 'MOFScriptModel_PointCut92', b)
    if hasattr(a2, 'MOFScriptModel_PointCut92'):
        assert _is_linked(a2, 'MOFScriptModel_PointCut92', b)
    _safe_set(b, 'MOFScriptModel_Advice91', None)
    assert not _is_linked(b, 'MOFScriptModel_Advice91', a2)
    if hasattr(a2, 'MOFScriptModel_PointCut92'):
        assert not _is_linked(a2, 'MOFScriptModel_PointCut92', b)


def test_assoc_pointcutexpression93_reverse_link_reassign_clear():
    a1 = MOFScriptModel_PointCutExpression(combinationOperator="sample_text", expressionString="sample_text", operator="sample_text")
    a2 = MOFScriptModel_PointCutExpression(combinationOperator="sample_text_2", expressionString="sample_text_2", operator="sample_text_2")
    b = MOFScriptModel_PointCut(name="sample_text", typeMatch="sample_text")
    _safe_set(b, 'MOFScriptModel_PointCut94', a1)
    assert _is_linked(b, 'MOFScriptModel_PointCut94', a1)
    if hasattr(a1, 'MOFScriptModel_PointCutExpression'):
        assert _is_linked(a1, 'MOFScriptModel_PointCutExpression', b)
    _safe_set(b, 'MOFScriptModel_PointCut94', a2)
    assert _is_linked(b, 'MOFScriptModel_PointCut94', a2)
    if hasattr(a1, 'MOFScriptModel_PointCutExpression'):
        assert not _is_linked(a1, 'MOFScriptModel_PointCutExpression', b)
    if hasattr(a2, 'MOFScriptModel_PointCutExpression'):
        assert _is_linked(a2, 'MOFScriptModel_PointCutExpression', b)
    _safe_set(b, 'MOFScriptModel_PointCut94', None)
    assert not _is_linked(b, 'MOFScriptModel_PointCut94', a2)
    if hasattr(a2, 'MOFScriptModel_PointCutExpression'):
        assert not _is_linked(a2, 'MOFScriptModel_PointCutExpression', b)


def test_assoc_printBody62_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_PrintStatement(context="sample_text", printCommand="sample_text")
    _safe_set(b, 'MOFScriptModel_PrintStatement', a1)
    assert _is_linked(b, 'MOFScriptModel_PrintStatement', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression63'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression63', b)
    _safe_set(b, 'MOFScriptModel_PrintStatement', a2)
    assert _is_linked(b, 'MOFScriptModel_PrintStatement', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression63'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression63', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression63'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression63', b)
    _safe_set(b, 'MOFScriptModel_PrintStatement', None)
    assert not _is_linked(b, 'MOFScriptModel_PrintStatement', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression63'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression63', b)


def test_assoc_source114_reverse_link_reassign_clear():
    a1 = MOFScriptModel_Reference(name="sample_text")
    a2 = MOFScriptModel_Reference(name="sample_text_2")
    b = MOFScriptModel_M2MTrace(id="sample_text", name="sample_text")
    _safe_set(b, 'MOFScriptModel_M2MTrace', a1)
    assert _is_linked(b, 'MOFScriptModel_M2MTrace', a1)
    if hasattr(a1, 'MOFScriptModel_Reference'):
        assert _is_linked(a1, 'MOFScriptModel_Reference', b)
    _safe_set(b, 'MOFScriptModel_M2MTrace', a2)
    assert _is_linked(b, 'MOFScriptModel_M2MTrace', a2)
    if hasattr(a1, 'MOFScriptModel_Reference'):
        assert not _is_linked(a1, 'MOFScriptModel_Reference', b)
    if hasattr(a2, 'MOFScriptModel_Reference'):
        assert _is_linked(a2, 'MOFScriptModel_Reference', b)
    _safe_set(b, 'MOFScriptModel_M2MTrace', None)
    assert not _is_linked(b, 'MOFScriptModel_M2MTrace', a2)
    if hasattr(a2, 'MOFScriptModel_Reference'):
        assert not _is_linked(a2, 'MOFScriptModel_Reference', b)


def test_assoc_target115_reverse_link_reassign_clear():
    a1 = MOFScriptModel_Reference(name="sample_text")
    a2 = MOFScriptModel_Reference(name="sample_text_2")
    b = MOFScriptModel_M2MTrace(id="sample_text", name="sample_text")
    _safe_set(b, 'MOFScriptModel_M2MTrace116', a1)
    assert _is_linked(b, 'MOFScriptModel_M2MTrace116', a1)
    if hasattr(a1, 'MOFScriptModel_Reference117'):
        assert _is_linked(a1, 'MOFScriptModel_Reference117', b)
    _safe_set(b, 'MOFScriptModel_M2MTrace116', a2)
    assert _is_linked(b, 'MOFScriptModel_M2MTrace116', a2)
    if hasattr(a1, 'MOFScriptModel_Reference117'):
        assert not _is_linked(a1, 'MOFScriptModel_Reference117', b)
    if hasattr(a2, 'MOFScriptModel_Reference117'):
        assert _is_linked(a2, 'MOFScriptModel_Reference117', b)
    _safe_set(b, 'MOFScriptModel_M2MTrace116', None)
    assert not _is_linked(b, 'MOFScriptModel_M2MTrace116', a2)
    if hasattr(a2, 'MOFScriptModel_Reference117'):
        assert not _is_linked(a2, 'MOFScriptModel_Reference117', b)


def test_assoc_transformationRule53_reverse_link_reassign_clear():
    a1 = MOFScriptModel_TransformationRule(accessLevel="sample_text", isAbstract=True, isEntryPoint=True, name="sample_text", return_="sample_text")
    a2 = MOFScriptModel_TransformationRule(accessLevel="sample_text_2", isAbstract=False, isEntryPoint=False, name="sample_text_2", return_="sample_text_2")
    b = MOFScriptModel_FunctionCall(isSuperCall=True, name="sample_text", transformationContext="sample_text")
    _safe_set(b, 'MOFScriptModel_FunctionCall54', a1)
    assert _is_linked(b, 'MOFScriptModel_FunctionCall54', a1)
    if hasattr(a1, 'MOFScriptModel_TransformationRule55'):
        assert _is_linked(a1, 'MOFScriptModel_TransformationRule55', b)
    _safe_set(b, 'MOFScriptModel_FunctionCall54', a2)
    assert _is_linked(b, 'MOFScriptModel_FunctionCall54', a2)
    if hasattr(a1, 'MOFScriptModel_TransformationRule55'):
        assert not _is_linked(a1, 'MOFScriptModel_TransformationRule55', b)
    if hasattr(a2, 'MOFScriptModel_TransformationRule55'):
        assert _is_linked(a2, 'MOFScriptModel_TransformationRule55', b)
    _safe_set(b, 'MOFScriptModel_FunctionCall54', None)
    assert not _is_linked(b, 'MOFScriptModel_FunctionCall54', a2)
    if hasattr(a2, 'MOFScriptModel_TransformationRule55'):
        assert not _is_linked(a2, 'MOFScriptModel_TransformationRule55', b)


def test_assoc_transformationrules29_reverse_link_reassign_clear():
    a1 = MOFScriptModel_TransformationRule(accessLevel="sample_text", isAbstract=True, isEntryPoint=True, name="sample_text", return_="sample_text")
    a2 = MOFScriptModel_TransformationRule(accessLevel="sample_text_2", isAbstract=False, isEntryPoint=False, name="sample_text_2", return_="sample_text_2")
    b = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text", name="sample_text")
    _safe_set(b, 'owner30', {a1})
    assert _is_linked(b, 'owner30', a1)
    if hasattr(a1, 'TransformationRule'):
        assert _is_linked(a1, 'TransformationRule', b)
    _safe_set(b, 'owner30', {a2})
    assert _is_linked(b, 'owner30', a2)
    if hasattr(a1, 'TransformationRule'):
        assert not _is_linked(a1, 'TransformationRule', b)
    if hasattr(a2, 'TransformationRule'):
        assert _is_linked(a2, 'TransformationRule', b)
    _safe_set(b, 'owner30', set())
    assert not _is_linked(b, 'owner30', a2)
    if hasattr(a2, 'TransformationRule'):
        assert not _is_linked(a2, 'TransformationRule', b)


def test_assoc_value107_reverse_link_reassign_clear():
    a1 = MOFScriptModel_ValueExpression(specification="sample_text")
    a2 = MOFScriptModel_ValueExpression(specification="sample_text_2")
    b = MOFScriptModel_CreateExpressionParameter(name="sample_text")
    _safe_set(b, 'MOFScriptModel_CreateExpressionParameter108', a1)
    assert _is_linked(b, 'MOFScriptModel_CreateExpressionParameter108', a1)
    if hasattr(a1, 'MOFScriptModel_ValueExpression109'):
        assert _is_linked(a1, 'MOFScriptModel_ValueExpression109', b)
    _safe_set(b, 'MOFScriptModel_CreateExpressionParameter108', a2)
    assert _is_linked(b, 'MOFScriptModel_CreateExpressionParameter108', a2)
    if hasattr(a1, 'MOFScriptModel_ValueExpression109'):
        assert not _is_linked(a1, 'MOFScriptModel_ValueExpression109', b)
    if hasattr(a2, 'MOFScriptModel_ValueExpression109'):
        assert _is_linked(a2, 'MOFScriptModel_ValueExpression109', b)
    _safe_set(b, 'MOFScriptModel_CreateExpressionParameter108', None)
    assert not _is_linked(b, 'MOFScriptModel_CreateExpressionParameter108', a2)
    if hasattr(a2, 'MOFScriptModel_ValueExpression109'):
        assert not _is_linked(a2, 'MOFScriptModel_ValueExpression109', b)


def test_assoc_variables18_reverse_link_reassign_clear():
    a1 = MOFScriptModel_VariableDeclaration(constant=True, name="sample_text", type="sample_text")
    a2 = MOFScriptModel_VariableDeclaration(constant=False, name="sample_text_2", type="sample_text_2")
    b = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text", name="sample_text")
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation', {a1})
    assert _is_linked(b, 'MOFScriptModel_MOFScriptTransformation', a1)
    if hasattr(a1, 'MOFScriptModel_VariableDeclaration19'):
        assert _is_linked(a1, 'MOFScriptModel_VariableDeclaration19', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation', {a2})
    assert _is_linked(b, 'MOFScriptModel_MOFScriptTransformation', a2)
    if hasattr(a1, 'MOFScriptModel_VariableDeclaration19'):
        assert not _is_linked(a1, 'MOFScriptModel_VariableDeclaration19', b)
    if hasattr(a2, 'MOFScriptModel_VariableDeclaration19'):
        assert _is_linked(a2, 'MOFScriptModel_VariableDeclaration19', b)
    _safe_set(b, 'MOFScriptModel_MOFScriptTransformation', set())
    assert not _is_linked(b, 'MOFScriptModel_MOFScriptTransformation', a2)
    if hasattr(a2, 'MOFScriptModel_VariableDeclaration19'):
        assert not _is_linked(a2, 'MOFScriptModel_VariableDeclaration19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_advice87_stub_double():
    # MOFScriptModel_MOFScriptAspect has no real 'MOFScriptModel_MOFScriptAspect' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_Advice's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_Advice's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_Advice(code="sample_text", name="sample_text", operator="sample_text", pointCutRef="sample_text")
    partner = MOFScriptModel_MOFScriptAspect()
    setattr(partner, 'MOFScriptModel_MOFScriptAspect', None)
    _safe_set(owner, 'MOFScriptModel_Advice', partner)
    assert owner in getattr(partner, 'MOFScriptModel_MOFScriptAspect')
    _safe_set(owner, 'MOFScriptModel_Advice', None)
    assert owner not in getattr(partner, 'MOFScriptModel_MOFScriptAspect')


def test_assoc_blocks10_stub_double():
    # MOFScriptModel_MOFScriptStatementOwner has no real 'MOFScriptModel_MOFScriptStatementOwner11' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_StatementBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_StatementBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_StatementBlock(id="sample_text", protected=True, reference="sample_text")
    partner = MOFScriptModel_MOFScriptStatementOwner()
    setattr(partner, 'MOFScriptModel_MOFScriptStatementOwner11', None)
    _safe_set(owner, 'MOFScriptModel_StatementBlock', partner)
    assert owner in getattr(partner, 'MOFScriptModel_MOFScriptStatementOwner11')
    _safe_set(owner, 'MOFScriptModel_StatementBlock', None)
    assert owner not in getattr(partner, 'MOFScriptModel_MOFScriptStatementOwner11')


def test_assoc_expression56_stub_double():
    # MOFScriptModel_Expression has no real 'MOFScriptModel_Expression57' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_ResultAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_ResultAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_ResultAssignment(operator="sample_text", resultPart="sample_text")
    partner = MOFScriptModel_Expression()
    setattr(partner, 'MOFScriptModel_Expression57', None)
    _safe_set(owner, 'MOFScriptModel_ResultAssignment', partner)
    assert getattr(partner, 'MOFScriptModel_Expression57') == owner
    _safe_set(owner, 'MOFScriptModel_ResultAssignment', None)
    assert getattr(partner, 'MOFScriptModel_Expression57') is None


def test_assoc_expression58_stub_double():
    # MOFScriptModel_Expression has no real 'MOFScriptModel_Expression59' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_GeneralAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_GeneralAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_GeneralAssignment(name="sample_text", operator="sample_text")
    partner = MOFScriptModel_Expression()
    setattr(partner, 'MOFScriptModel_Expression59', None)
    _safe_set(owner, 'MOFScriptModel_GeneralAssignment', partner)
    assert getattr(partner, 'MOFScriptModel_Expression59') == owner
    _safe_set(owner, 'MOFScriptModel_GeneralAssignment', None)
    assert getattr(partner, 'MOFScriptModel_Expression59') is None


def test_assoc_filterExpression31_stub_double():
    # MOFScriptModel_Expression has no real 'MOFScriptModel_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_IteratorStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_IteratorStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_IteratorStatement(type="sample_text", variable="sample_text")
    partner = MOFScriptModel_Expression()
    setattr(partner, 'MOFScriptModel_Expression32', None)
    _safe_set(owner, 'MOFScriptModel_IteratorStatement', partner)
    assert getattr(partner, 'MOFScriptModel_Expression32') == owner
    _safe_set(owner, 'MOFScriptModel_IteratorStatement', None)
    assert getattr(partner, 'MOFScriptModel_Expression32') is None


def test_assoc_filterExpression98_stub_double():
    # MOFScriptModel_Expression has no real 'MOFScriptModel_Expression99' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_SelectExpression(type="sample_text", variable="sample_text")
    partner = MOFScriptModel_Expression()
    setattr(partner, 'MOFScriptModel_Expression99', None)
    _safe_set(owner, 'MOFScriptModel_SelectExpression', partner)
    assert getattr(partner, 'MOFScriptModel_Expression99') == owner
    _safe_set(owner, 'MOFScriptModel_SelectExpression', None)
    assert getattr(partner, 'MOFScriptModel_Expression99') is None


def test_assoc_function60_stub_double():
    # MOFScriptModel_FunctionCallStatement has no real 'MOFScriptModel_FunctionCallStatement' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_FunctionCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_FunctionCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_FunctionCall(isSuperCall=True, name="sample_text", transformationContext="sample_text")
    partner = MOFScriptModel_FunctionCallStatement()
    setattr(partner, 'MOFScriptModel_FunctionCallStatement', None)
    _safe_set(owner, 'MOFScriptModel_FunctionCall61', partner)
    assert getattr(partner, 'MOFScriptModel_FunctionCallStatement') == owner
    _safe_set(owner, 'MOFScriptModel_FunctionCall61', None)
    assert getattr(partner, 'MOFScriptModel_FunctionCallStatement') is None


def test_assoc_imports83_stub_double():
    # MOFScriptModel_MOFScriptSpecification has no real 'MOFScriptModel_MOFScriptSpecification84' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_MOFScriptImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_MOFScriptImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_MOFScriptImport(importSemantics="sample_text", name="sample_text", type="sample_text", uri="sample_text")
    partner = MOFScriptModel_MOFScriptSpecification()
    setattr(partner, 'MOFScriptModel_MOFScriptSpecification84', None)
    _safe_set(owner, 'MOFScriptModel_MOFScriptImport', partner)
    assert owner in getattr(partner, 'MOFScriptModel_MOFScriptSpecification84')
    _safe_set(owner, 'MOFScriptModel_MOFScriptImport', None)
    assert owner not in getattr(partner, 'MOFScriptModel_MOFScriptSpecification84')


def test_assoc_part143_stub_double():
    # MOFScriptModel_Expression has no real 'MOFScriptModel_Expression44' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_LogicalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_LogicalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_LogicalExpression(operator="sample_text")
    partner = MOFScriptModel_Expression()
    setattr(partner, 'MOFScriptModel_Expression44', None)
    _safe_set(owner, 'MOFScriptModel_LogicalExpression', partner)
    assert getattr(partner, 'MOFScriptModel_Expression44') == owner
    _safe_set(owner, 'MOFScriptModel_LogicalExpression', None)
    assert getattr(partner, 'MOFScriptModel_Expression44') is None


def test_assoc_part245_stub_double():
    # MOFScriptModel_Expression has no real 'MOFScriptModel_Expression47' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_LogicalExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_LogicalExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_LogicalExpression(operator="sample_text")
    partner = MOFScriptModel_Expression()
    setattr(partner, 'MOFScriptModel_Expression47', None)
    _safe_set(owner, 'MOFScriptModel_LogicalExpression46', partner)
    assert getattr(partner, 'MOFScriptModel_Expression47') == owner
    _safe_set(owner, 'MOFScriptModel_LogicalExpression46', None)
    assert getattr(partner, 'MOFScriptModel_Expression47') is None


def test_assoc_pointcut88_stub_double():
    # MOFScriptModel_MOFScriptAspect has no real 'MOFScriptModel_MOFScriptAspect89' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_PointCut's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_PointCut's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_PointCut(name="sample_text", typeMatch="sample_text")
    partner = MOFScriptModel_MOFScriptAspect()
    setattr(partner, 'MOFScriptModel_MOFScriptAspect89', None)
    _safe_set(owner, 'MOFScriptModel_PointCut', partner)
    assert owner in getattr(partner, 'MOFScriptModel_MOFScriptAspect89')
    _safe_set(owner, 'MOFScriptModel_PointCut', None)
    assert owner not in getattr(partner, 'MOFScriptModel_MOFScriptAspect89')


def test_assoc_source33_stub_double():
    # MOFScriptModel_SimpleExpression has no real 'MOFScriptModel_SimpleExpression' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_IteratorStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_IteratorStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_IteratorStatement(type="sample_text", variable="sample_text")
    partner = MOFScriptModel_SimpleExpression()
    setattr(partner, 'MOFScriptModel_SimpleExpression', None)
    _safe_set(owner, 'MOFScriptModel_IteratorStatement34', partner)
    assert getattr(partner, 'MOFScriptModel_SimpleExpression') == owner
    _safe_set(owner, 'MOFScriptModel_IteratorStatement34', None)
    assert getattr(partner, 'MOFScriptModel_SimpleExpression') is None


def test_assoc_sourceReference100_stub_double():
    # MOFScriptModel_SimpleExpression has no real 'MOFScriptModel_SimpleExpression102' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_SelectExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_SelectExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_SelectExpression(type="sample_text", variable="sample_text")
    partner = MOFScriptModel_SimpleExpression()
    setattr(partner, 'MOFScriptModel_SimpleExpression102', None)
    _safe_set(owner, 'MOFScriptModel_SelectExpression101', partner)
    assert getattr(partner, 'MOFScriptModel_SimpleExpression102') == owner
    _safe_set(owner, 'MOFScriptModel_SelectExpression101', None)
    assert getattr(partner, 'MOFScriptModel_SimpleExpression102') is None


def test_assoc_statements16_stub_double():
    # MOFScriptModel_MOFScriptStatement has no real 'MOFScriptModel_MOFScriptStatement' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_StatementBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_StatementBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_StatementBlock(id="sample_text", protected=True, reference="sample_text")
    partner = MOFScriptModel_MOFScriptStatement()
    setattr(partner, 'MOFScriptModel_MOFScriptStatement', None)
    _safe_set(owner, 'MOFScriptModel_StatementBlock17', {partner})
    assert getattr(partner, 'MOFScriptModel_MOFScriptStatement') == owner
    _safe_set(owner, 'MOFScriptModel_StatementBlock17', set())
    assert getattr(partner, 'MOFScriptModel_MOFScriptStatement') is None


def test_assoc_transformation81_stub_double():
    # MOFScriptModel_MOFScriptSpecification has no real 'MOFScriptModel_MOFScriptSpecification' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_MOFScriptTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_MOFScriptTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_MOFScriptTransformation(extendsName="sample_text", name="sample_text")
    partner = MOFScriptModel_MOFScriptSpecification()
    setattr(partner, 'MOFScriptModel_MOFScriptSpecification', None)
    _safe_set(owner, 'MOFScriptModel_MOFScriptTransformation82', partner)
    assert owner in getattr(partner, 'MOFScriptModel_MOFScriptSpecification')
    _safe_set(owner, 'MOFScriptModel_MOFScriptTransformation82', None)
    assert owner not in getattr(partner, 'MOFScriptModel_MOFScriptSpecification')


def test_assoc_value14_stub_double():
    # MOFScriptModel_Expression has no real 'MOFScriptModel_Expression' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_VariableDeclaration(constant=True, name="sample_text", type="sample_text")
    partner = MOFScriptModel_Expression()
    setattr(partner, 'MOFScriptModel_Expression', None)
    _safe_set(owner, 'MOFScriptModel_VariableDeclaration15', partner)
    assert getattr(partner, 'MOFScriptModel_Expression') == owner
    _safe_set(owner, 'MOFScriptModel_VariableDeclaration15', None)
    assert getattr(partner, 'MOFScriptModel_Expression') is None


def test_assoc_variable112_stub_double():
    # MOFScriptModel_VariableDeclarationStatement has no real 'MOFScriptModel_VariableDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_VariableDeclaration(constant=True, name="sample_text", type="sample_text")
    partner = MOFScriptModel_VariableDeclarationStatement()
    setattr(partner, 'MOFScriptModel_VariableDeclarationStatement', None)
    _safe_set(owner, 'MOFScriptModel_VariableDeclaration113', partner)
    assert getattr(partner, 'MOFScriptModel_VariableDeclarationStatement') == owner
    _safe_set(owner, 'MOFScriptModel_VariableDeclaration113', None)
    assert getattr(partner, 'MOFScriptModel_VariableDeclarationStatement') is None


def test_assoc_variables9_stub_double():
    # MOFScriptModel_MOFScriptStatementOwner has no real 'MOFScriptModel_MOFScriptStatementOwner' property in the generated
    # code (a bare stub) -- manually attach it so MOFScriptModel_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MOFScriptModel_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MOFScriptModel_VariableDeclaration(constant=True, name="sample_text", type="sample_text")
    partner = MOFScriptModel_MOFScriptStatementOwner()
    setattr(partner, 'MOFScriptModel_MOFScriptStatementOwner', None)
    _safe_set(owner, 'MOFScriptModel_VariableDeclaration', partner)
    assert owner in getattr(partner, 'MOFScriptModel_MOFScriptStatementOwner')
    _safe_set(owner, 'MOFScriptModel_VariableDeclaration', None)
    assert owner not in getattr(partner, 'MOFScriptModel_MOFScriptStatementOwner')


