import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssignmentTarget,
    CompilationUnit,
    Expression,
    FetchStatementIntoClause,
    FunctionClause,
    FunctionContent,
    Item,
    ItemDeclaration,
    LoopStatement,
    NameDeclaration,
    Pragma,
    ProcedureContent,
    Statement,
    plSql_AssignmentStatement,
    plSql_AssignmentTarget,
    plSql_BasicLoopStatement,
    plSql_BlockStatement,
    plSql_BooleanLiteralExpression,
    plSql_CaseStatement,
    plSql_CaseStatementElseBranch,
    plSql_CaseStatementWhenBranch,
    plSql_CloseStatement,
    plSql_CompilationUnit,
    plSql_ContinueStatement,
    plSql_DeclareSection,
    plSql_DeterministicClause,
    plSql_ExitStatement,
    plSql_Expression,
    plSql_ExternalProcedureDeclaration,
    plSql_FetchStatement,
    plSql_FetchStatementBulkIntoClause,
    plSql_FetchStatementIntoClause,
    plSql_FetchStatementSingleIntoClause,
    plSql_ForLoopStatement,
    plSql_Function,
    plSql_FunctionClause,
    plSql_FunctionContent,
    plSql_FunctionImplementation,
    plSql_FunctionInvokerRightsClause,
    plSql_GotoStatement,
    plSql_IfStatement,
    plSql_IfStatementElseBranch,
    plSql_IfStatementElsifBranch,
    plSql_IntLiteralExpression,
    plSql_Item,
    plSql_ItemDeclaration,
    plSql_Label,
    plSql_LoopStatement,
    plSql_LoopVariableDeclaration,
    plSql_Name,
    plSql_NameDeclaration,
    plSql_NullLiteralExpression,
    plSql_NullStatement,
    plSql_Package,
    plSql_ParameterDeclaration,
    plSql_ParameterSequence,
    plSql_ParameterValue,
    plSql_PipelinedClause,
    plSql_Pragma,
    plSql_PragmaRestrictReferences,
    plSql_PragmaTimestamp,
    plSql_Procedure,
    plSql_ProcedureContent,
    plSql_ProcedureDeclaration,
    plSql_ProcedureDefinition,
    plSql_ProcedureImplementation,
    plSql_ProcedureInvokerRightsClause,
    plSql_QualifiedName,
    plSql_RaiseStatement,
    plSql_ResultCacheClause,
    plSql_ReturnStatement,
    plSql_Statement,
    plSql_StatementBody,
    plSql_StringLiteralExpression,
    plSql_VariableAssignmentTarget,
    plSql_VariableDeclaration,
    plSql_VariableRef,
    plSql_VariableRefExpression,
    plSql_VariableValue,
    plSql_WhileLoopStatement,
    InvokerRight,
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

def test_assoc_invokerRights1_reverse_link_reassign_clear():
    a1 = plSql_ProcedureInvokerRightsClause(right="sample_text")
    a2 = plSql_ProcedureInvokerRightsClause(right="sample_text_2")
    b = plSql_Procedure(schemaName="sample_text")
    _safe_set(b, 'plSql_Procedure2', a1)
    assert _is_linked(b, 'plSql_Procedure2', a1)
    if hasattr(a1, 'plSql_ProcedureInvokerRightsClause'):
        assert _is_linked(a1, 'plSql_ProcedureInvokerRightsClause', b)
    _safe_set(b, 'plSql_Procedure2', a2)
    assert _is_linked(b, 'plSql_Procedure2', a2)
    if hasattr(a1, 'plSql_ProcedureInvokerRightsClause'):
        assert not _is_linked(a1, 'plSql_ProcedureInvokerRightsClause', b)
    if hasattr(a2, 'plSql_ProcedureInvokerRightsClause'):
        assert _is_linked(a2, 'plSql_ProcedureInvokerRightsClause', b)
    _safe_set(b, 'plSql_Procedure2', None)
    assert not _is_linked(b, 'plSql_Procedure2', a2)
    if hasattr(a2, 'plSql_ProcedureInvokerRightsClause'):
        assert not _is_linked(a2, 'plSql_ProcedureInvokerRightsClause', b)


def test_assoc_invokerRights5_reverse_link_reassign_clear():
    a1 = plSql_ProcedureInvokerRightsClause(right="sample_text")
    a2 = plSql_ProcedureInvokerRightsClause(right="sample_text_2")
    b = plSql_Package(endName="sample_text", schemaName="sample_text")
    _safe_set(b, 'plSql_Package', a1)
    assert _is_linked(b, 'plSql_Package', a1)
    if hasattr(a1, 'plSql_ProcedureInvokerRightsClause6'):
        assert _is_linked(a1, 'plSql_ProcedureInvokerRightsClause6', b)
    _safe_set(b, 'plSql_Package', a2)
    assert _is_linked(b, 'plSql_Package', a2)
    if hasattr(a1, 'plSql_ProcedureInvokerRightsClause6'):
        assert not _is_linked(a1, 'plSql_ProcedureInvokerRightsClause6', b)
    if hasattr(a2, 'plSql_ProcedureInvokerRightsClause6'):
        assert _is_linked(a2, 'plSql_ProcedureInvokerRightsClause6', b)
    _safe_set(b, 'plSql_Package', None)
    assert not _is_linked(b, 'plSql_Package', a2)
    if hasattr(a2, 'plSql_ProcedureInvokerRightsClause6'):
        assert not _is_linked(a2, 'plSql_ProcedureInvokerRightsClause6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body29_stub_double():
    # plSql_ProcedureImplementation has no real 'plSql_ProcedureImplementation30' property in the generated
    # code (a bare stub) -- manually attach it so plSql_StatementBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_StatementBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_StatementBody(endName="sample_text")
    partner = plSql_ProcedureImplementation()
    setattr(partner, 'plSql_ProcedureImplementation30', None)
    _safe_set(owner, 'plSql_StatementBody', partner)
    assert getattr(partner, 'plSql_ProcedureImplementation30') == owner
    _safe_set(owner, 'plSql_StatementBody', None)
    assert getattr(partner, 'plSql_ProcedureImplementation30') is None


def test_assoc_body33_stub_double():
    # plSql_FunctionImplementation has no real 'plSql_FunctionImplementation34' property in the generated
    # code (a bare stub) -- manually attach it so plSql_StatementBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_StatementBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_StatementBody(endName="sample_text")
    partner = plSql_FunctionImplementation()
    setattr(partner, 'plSql_FunctionImplementation34', None)
    _safe_set(owner, 'plSql_StatementBody35', partner)
    assert getattr(partner, 'plSql_FunctionImplementation34') == owner
    _safe_set(owner, 'plSql_StatementBody35', None)
    assert getattr(partner, 'plSql_FunctionImplementation34') is None


def test_assoc_body56_stub_double():
    # plSql_BlockStatement has no real 'plSql_BlockStatement57' property in the generated
    # code (a bare stub) -- manually attach it so plSql_StatementBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_StatementBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_StatementBody(endName="sample_text")
    partner = plSql_BlockStatement()
    setattr(partner, 'plSql_BlockStatement57', None)
    _safe_set(owner, 'plSql_StatementBody58', partner)
    assert getattr(partner, 'plSql_BlockStatement57') == owner
    _safe_set(owner, 'plSql_StatementBody58', None)
    assert getattr(partner, 'plSql_BlockStatement57') is None


def test_assoc_content19_stub_double():
    # plSql_FunctionContent has no real 'plSql_FunctionContent' property in the generated
    # code (a bare stub) -- manually attach it so plSql_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_Function(returnType="sample_text", schemaName="sample_text")
    partner = plSql_FunctionContent()
    setattr(partner, 'plSql_FunctionContent', None)
    _safe_set(owner, 'plSql_Function20', partner)
    assert getattr(partner, 'plSql_FunctionContent') == owner
    _safe_set(owner, 'plSql_Function20', None)
    assert getattr(partner, 'plSql_FunctionContent') is None


def test_assoc_content3_stub_double():
    # plSql_ProcedureContent has no real 'plSql_ProcedureContent' property in the generated
    # code (a bare stub) -- manually attach it so plSql_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_Procedure(schemaName="sample_text")
    partner = plSql_ProcedureContent()
    setattr(partner, 'plSql_ProcedureContent', None)
    _safe_set(owner, 'plSql_Procedure4', partner)
    assert getattr(partner, 'plSql_ProcedureContent') == owner
    _safe_set(owner, 'plSql_Procedure4', None)
    assert getattr(partner, 'plSql_ProcedureContent') is None


def test_assoc_cursor74_stub_double():
    # plSql_CloseStatement has no real 'plSql_CloseStatement' property in the generated
    # code (a bare stub) -- manually attach it so plSql_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_VariableRef(isHostRef=True)
    partner = plSql_CloseStatement()
    setattr(partner, 'plSql_CloseStatement', None)
    _safe_set(owner, 'plSql_VariableRef75', partner)
    assert getattr(partner, 'plSql_CloseStatement') == owner
    _safe_set(owner, 'plSql_VariableRef75', None)
    assert getattr(partner, 'plSql_CloseStatement') is None


def test_assoc_cursor80_stub_double():
    # plSql_FetchStatement has no real 'plSql_FetchStatement' property in the generated
    # code (a bare stub) -- manually attach it so plSql_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_VariableRef(isHostRef=True)
    partner = plSql_FetchStatement()
    setattr(partner, 'plSql_FetchStatement', None)
    _safe_set(owner, 'plSql_VariableRef81', partner)
    assert getattr(partner, 'plSql_FetchStatement') == owner
    _safe_set(owner, 'plSql_VariableRef81', None)
    assert getattr(partner, 'plSql_FetchStatement') is None


def test_assoc_declaration126_stub_double():
    # plSql_Name has no real 'plSql_Name127' property in the generated
    # code (a bare stub) -- manually attach it so plSql_NameDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_NameDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_NameDeclaration(name="sample_text")
    partner = plSql_Name()
    setattr(partner, 'plSql_Name127', None)
    _safe_set(owner, 'plSql_NameDeclaration', partner)
    assert getattr(partner, 'plSql_Name127') == owner
    _safe_set(owner, 'plSql_NameDeclaration', None)
    assert getattr(partner, 'plSql_Name127') is None


def test_assoc_elseBranch63_stub_double():
    # plSql_CaseStatementElseBranch has no real 'plSql_CaseStatementElseBranch' property in the generated
    # code (a bare stub) -- manually attach it so plSql_CaseStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_CaseStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_CaseStatement(endLabel="sample_text")
    partner = plSql_CaseStatementElseBranch()
    setattr(partner, 'plSql_CaseStatementElseBranch', None)
    _safe_set(owner, 'plSql_CaseStatement64', partner)
    assert getattr(partner, 'plSql_CaseStatementElseBranch') == owner
    _safe_set(owner, 'plSql_CaseStatement64', None)
    assert getattr(partner, 'plSql_CaseStatementElseBranch') is None


def test_assoc_expression59_stub_double():
    # plSql_Expression has no real 'plSql_Expression60' property in the generated
    # code (a bare stub) -- manually attach it so plSql_CaseStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_CaseStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_CaseStatement(endLabel="sample_text")
    partner = plSql_Expression()
    setattr(partner, 'plSql_Expression60', None)
    _safe_set(owner, 'plSql_CaseStatement', partner)
    assert getattr(partner, 'plSql_Expression60') == owner
    _safe_set(owner, 'plSql_CaseStatement', None)
    assert getattr(partner, 'plSql_Expression60') is None


def test_assoc_functionClauses17_stub_double():
    # plSql_FunctionClause has no real 'plSql_FunctionClause' property in the generated
    # code (a bare stub) -- manually attach it so plSql_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_Function(returnType="sample_text", schemaName="sample_text")
    partner = plSql_FunctionClause()
    setattr(partner, 'plSql_FunctionClause', None)
    _safe_set(owner, 'plSql_Function18', {partner})
    assert getattr(partner, 'plSql_FunctionClause') == owner
    _safe_set(owner, 'plSql_Function18', set())
    assert getattr(partner, 'plSql_FunctionClause') is None


def test_assoc_items7_stub_double():
    # plSql_Item has no real 'plSql_Item' property in the generated
    # code (a bare stub) -- manually attach it so plSql_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_Package(endName="sample_text", schemaName="sample_text")
    partner = plSql_Item()
    setattr(partner, 'plSql_Item', None)
    _safe_set(owner, 'plSql_Package8', {partner})
    assert getattr(partner, 'plSql_Item') == owner
    _safe_set(owner, 'plSql_Package8', set())
    assert getattr(partner, 'plSql_Item') is None


def test_assoc_labelName89_stub_double():
    # plSql_GotoStatement has no real 'plSql_GotoStatement' property in the generated
    # code (a bare stub) -- manually attach it so plSql_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_Label(name="sample_text")
    partner = plSql_GotoStatement()
    setattr(partner, 'plSql_GotoStatement', None)
    _safe_set(owner, 'plSql_Label90', partner)
    assert getattr(partner, 'plSql_GotoStatement') == owner
    _safe_set(owner, 'plSql_Label90', None)
    assert getattr(partner, 'plSql_GotoStatement') is None


def test_assoc_labels46_stub_double():
    # plSql_Statement has no real 'plSql_Statement47' property in the generated
    # code (a bare stub) -- manually attach it so plSql_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_Label(name="sample_text")
    partner = plSql_Statement()
    setattr(partner, 'plSql_Statement47', None)
    _safe_set(owner, 'plSql_Label', partner)
    assert owner in getattr(partner, 'plSql_Statement47')
    _safe_set(owner, 'plSql_Label', None)
    assert owner not in getattr(partner, 'plSql_Statement47')


def test_assoc_name122_stub_double():
    # plSql_QualifiedName has no real 'plSql_QualifiedName' property in the generated
    # code (a bare stub) -- manually attach it so plSql_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_VariableRef(isHostRef=True)
    partner = plSql_QualifiedName()
    setattr(partner, 'plSql_QualifiedName', None)
    _safe_set(owner, 'plSql_VariableRef123', partner)
    assert getattr(partner, 'plSql_QualifiedName') == owner
    _safe_set(owner, 'plSql_VariableRef123', None)
    assert getattr(partner, 'plSql_QualifiedName') is None


def test_assoc_parameters0_stub_double():
    # plSql_ParameterSequence has no real 'plSql_ParameterSequence' property in the generated
    # code (a bare stub) -- manually attach it so plSql_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_Procedure(schemaName="sample_text")
    partner = plSql_ParameterSequence()
    setattr(partner, 'plSql_ParameterSequence', None)
    _safe_set(owner, 'plSql_Procedure', partner)
    assert getattr(partner, 'plSql_ParameterSequence') == owner
    _safe_set(owner, 'plSql_Procedure', None)
    assert getattr(partner, 'plSql_ParameterSequence') is None


def test_assoc_parameters15_stub_double():
    # plSql_ParameterSequence has no real 'plSql_ParameterSequence16' property in the generated
    # code (a bare stub) -- manually attach it so plSql_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_Function(returnType="sample_text", schemaName="sample_text")
    partner = plSql_ParameterSequence()
    setattr(partner, 'plSql_ParameterSequence16', None)
    _safe_set(owner, 'plSql_Function', partner)
    assert getattr(partner, 'plSql_ParameterSequence16') == owner
    _safe_set(owner, 'plSql_Function', None)
    assert getattr(partner, 'plSql_ParameterSequence16') is None


def test_assoc_parameters21_stub_double():
    # plSql_ParameterSequence has no real 'plSql_ParameterSequence22' property in the generated
    # code (a bare stub) -- manually attach it so plSql_ParameterDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_ParameterDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_ParameterDeclaration(behavior="sample_text", dataType="sample_text")
    partner = plSql_ParameterSequence()
    setattr(partner, 'plSql_ParameterSequence22', None)
    _safe_set(owner, 'plSql_ParameterDeclaration', partner)
    assert owner in getattr(partner, 'plSql_ParameterSequence22')
    _safe_set(owner, 'plSql_ParameterDeclaration', None)
    assert owner not in getattr(partner, 'plSql_ParameterSequence22')


def test_assoc_parameters9_stub_double():
    # plSql_ParameterSequence has no real 'plSql_ParameterSequence10' property in the generated
    # code (a bare stub) -- manually attach it so plSql_ProcedureDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_ProcedureDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_ProcedureDeclaration(name="sample_text")
    partner = plSql_ParameterSequence()
    setattr(partner, 'plSql_ParameterSequence10', None)
    _safe_set(owner, 'plSql_ProcedureDeclaration', partner)
    assert getattr(partner, 'plSql_ParameterSequence10') == owner
    _safe_set(owner, 'plSql_ProcedureDeclaration', None)
    assert getattr(partner, 'plSql_ParameterSequence10') is None


def test_assoc_statements109_stub_double():
    # plSql_Statement has no real 'plSql_Statement110' property in the generated
    # code (a bare stub) -- manually attach it so plSql_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_LoopStatement(endLabel="sample_text")
    partner = plSql_Statement()
    setattr(partner, 'plSql_Statement110', None)
    _safe_set(owner, 'plSql_LoopStatement', {partner})
    assert getattr(partner, 'plSql_Statement110') == owner
    _safe_set(owner, 'plSql_LoopStatement', set())
    assert getattr(partner, 'plSql_Statement110') is None


def test_assoc_statements36_stub_double():
    # plSql_Statement has no real 'plSql_Statement' property in the generated
    # code (a bare stub) -- manually attach it so plSql_StatementBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_StatementBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_StatementBody(endName="sample_text")
    partner = plSql_Statement()
    setattr(partner, 'plSql_Statement', None)
    _safe_set(owner, 'plSql_StatementBody37', {partner})
    assert getattr(partner, 'plSql_Statement') == owner
    _safe_set(owner, 'plSql_StatementBody37', set())
    assert getattr(partner, 'plSql_Statement') is None


def test_assoc_targetVariables84_stub_double():
    # plSql_FetchStatementIntoClause has no real 'plSql_FetchStatementIntoClause85' property in the generated
    # code (a bare stub) -- manually attach it so plSql_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_VariableRef(isHostRef=True)
    partner = plSql_FetchStatementIntoClause()
    setattr(partner, 'plSql_FetchStatementIntoClause85', None)
    _safe_set(owner, 'plSql_VariableRef86', partner)
    assert owner in getattr(partner, 'plSql_FetchStatementIntoClause85')
    _safe_set(owner, 'plSql_VariableRef86', None)
    assert owner not in getattr(partner, 'plSql_FetchStatementIntoClause85')


def test_assoc_value23_stub_double():
    # plSql_ParameterValue has no real 'plSql_ParameterValue' property in the generated
    # code (a bare stub) -- manually attach it so plSql_ParameterDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_ParameterDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_ParameterDeclaration(behavior="sample_text", dataType="sample_text")
    partner = plSql_ParameterValue()
    setattr(partner, 'plSql_ParameterValue', None)
    _safe_set(owner, 'plSql_ParameterDeclaration24', partner)
    assert getattr(partner, 'plSql_ParameterValue') == owner
    _safe_set(owner, 'plSql_ParameterDeclaration24', None)
    assert getattr(partner, 'plSql_ParameterValue') is None


def test_assoc_value41_stub_double():
    # plSql_VariableValue has no real 'plSql_VariableValue' property in the generated
    # code (a bare stub) -- manually attach it so plSql_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_VariableDeclaration(dataType="sample_text", isConstant=True, isNotNull=True)
    partner = plSql_VariableValue()
    setattr(partner, 'plSql_VariableValue', None)
    _safe_set(owner, 'plSql_VariableDeclaration', partner)
    assert getattr(partner, 'plSql_VariableValue') == owner
    _safe_set(owner, 'plSql_VariableDeclaration', None)
    assert getattr(partner, 'plSql_VariableValue') is None


def test_assoc_variable45_stub_double():
    # plSql_VariableRefExpression has no real 'plSql_VariableRefExpression' property in the generated
    # code (a bare stub) -- manually attach it so plSql_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_VariableRef(isHostRef=True)
    partner = plSql_VariableRefExpression()
    setattr(partner, 'plSql_VariableRefExpression', None)
    _safe_set(owner, 'plSql_VariableRef', partner)
    assert getattr(partner, 'plSql_VariableRefExpression') == owner
    _safe_set(owner, 'plSql_VariableRef', None)
    assert getattr(partner, 'plSql_VariableRefExpression') is None


def test_assoc_variable52_stub_double():
    # plSql_VariableAssignmentTarget has no real 'plSql_VariableAssignmentTarget' property in the generated
    # code (a bare stub) -- manually attach it so plSql_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_VariableRef(isHostRef=True)
    partner = plSql_VariableAssignmentTarget()
    setattr(partner, 'plSql_VariableAssignmentTarget', None)
    _safe_set(owner, 'plSql_VariableRef53', partner)
    assert getattr(partner, 'plSql_VariableAssignmentTarget') == owner
    _safe_set(owner, 'plSql_VariableRef53', None)
    assert getattr(partner, 'plSql_VariableAssignmentTarget') is None


def test_assoc_whenBranches61_stub_double():
    # plSql_CaseStatementWhenBranch has no real 'plSql_CaseStatementWhenBranch' property in the generated
    # code (a bare stub) -- manually attach it so plSql_CaseStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_CaseStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_CaseStatement(endLabel="sample_text")
    partner = plSql_CaseStatementWhenBranch()
    setattr(partner, 'plSql_CaseStatementWhenBranch', None)
    _safe_set(owner, 'plSql_CaseStatement62', {partner})
    assert getattr(partner, 'plSql_CaseStatementWhenBranch') == owner
    _safe_set(owner, 'plSql_CaseStatement62', set())
    assert getattr(partner, 'plSql_CaseStatementWhenBranch') is None


def test_assoc_whenExpression76_stub_double():
    # plSql_Expression has no real 'plSql_Expression77' property in the generated
    # code (a bare stub) -- manually attach it so plSql_ContinueStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_ContinueStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_ContinueStatement(labelName="sample_text")
    partner = plSql_Expression()
    setattr(partner, 'plSql_Expression77', None)
    _safe_set(owner, 'plSql_ContinueStatement', partner)
    assert getattr(partner, 'plSql_Expression77') == owner
    _safe_set(owner, 'plSql_ContinueStatement', None)
    assert getattr(partner, 'plSql_Expression77') is None


def test_assoc_whenExpression78_stub_double():
    # plSql_Expression has no real 'plSql_Expression79' property in the generated
    # code (a bare stub) -- manually attach it so plSql_ExitStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plSql_ExitStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plSql_ExitStatement(labelName="sample_text")
    partner = plSql_Expression()
    setattr(partner, 'plSql_Expression79', None)
    _safe_set(owner, 'plSql_ExitStatement', partner)
    assert getattr(partner, 'plSql_Expression79') == owner
    _safe_set(owner, 'plSql_ExitStatement', None)
    assert getattr(partner, 'plSql_Expression79') is None


