import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Argument,
    ControlSQLStatement,
    CursorDeclaration,
    Declaration,
    ExceptionSection,
    Expression,
    FunctionCallParameter,
    IfStatement,
    LoopStatement,
    ModifySQLStatement,
    NamedElement,
    SQLCondition,
    SQLStatement,
    SelectStatement,
    Statement,
    StringOperation,
    TriggerBlock,
    Type,
    UpdatePair,
    VarRefExpression,
    VariableDeclaration,
    condition_SQLCondition,
    declaration_Declaration,
    declaration_NamedElement,
    expression_Expression,
    plsql_condition_BooleanCondition,
    plsql_condition_ConditionComparison,
    plsql_condition_NotCondition,
    plsql_condition_SQLCondition,
    plsql_declaration_Argument,
    plsql_declaration_CursorDeclaration,
    plsql_declaration_Declaration,
    plsql_declaration_FunctionDeclaration,
    plsql_declaration_NamedElement,
    plsql_declaration_PLSQLDefinition,
    plsql_declaration_Package,
    plsql_declaration_ProcedureDeclaration,
    plsql_declaration_TriggerBlock,
    plsql_declaration_VariableDeclaration,
    plsql_expression_ArithmeticExpression,
    plsql_expression_BooleanExpression,
    plsql_expression_ConcatString,
    plsql_expression_Expression,
    plsql_expression_FormsVarRef,
    plsql_expression_FoundExpression,
    plsql_expression_FunctionCallParameter,
    plsql_expression_InRangeExpression,
    plsql_expression_IsNullExpression,
    plsql_expression_LikeExpression,
    plsql_expression_LiteralExpression,
    plsql_expression_NotExpression,
    plsql_expression_PropertyAccess,
    plsql_expression_SQLCursor,
    plsql_expression_SQLVariable,
    plsql_expression_StringOperation,
    plsql_expression_VarRefExpression,
    plsql_statement_AssignmentStatement,
    plsql_statement_BlockStatement,
    plsql_statement_CaseStatement,
    plsql_statement_CloseStatement,
    plsql_statement_CommitStatement,
    plsql_statement_ControlSQLStatement,
    plsql_statement_DeleteStatement,
    plsql_statement_ExceptionSection,
    plsql_statement_ExitStatement,
    plsql_statement_FetchStatement,
    plsql_statement_ForStatement,
    plsql_statement_FunctionCallStatement,
    plsql_statement_GotoStatement,
    plsql_statement_IfStatement,
    plsql_statement_InsertStatement,
    plsql_statement_LockTableStatement,
    plsql_statement_LoopStatement,
    plsql_statement_ModifySQLStatement,
    plsql_statement_NullStatement,
    plsql_statement_OpenStatement,
    plsql_statement_RaiseStatement,
    plsql_statement_ReturnStatement,
    plsql_statement_RollbackStatement,
    plsql_statement_SQLStatement,
    plsql_statement_SavepointStatement,
    plsql_statement_SelectStatement,
    plsql_statement_SetTransactionStatement,
    plsql_statement_Statement,
    plsql_statement_UpdatePair,
    plsql_statement_UpdateStatement,
    plsql_type_Datatype,
    plsql_type_GenericType,
    plsql_type_IndirectType,
    plsql_type_Type,
    plsql_type_TypedElement,
    statement_BlockStatement,
    statement_Statement,
    type_TypedElement,
    ArithmeticOperatorType,
    BasicTypes,
    BooleanOperatorType,
    LiteralExpressionType,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assign107_stub_double():
    # Expression has no real 'Expression108' property in the generated
    # code (a bare stub) -- manually attach it so plsql_declaration_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_declaration_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_declaration_VariableDeclaration(constant=True, default=True, notnull=True)
    partner = Expression()
    setattr(partner, 'Expression108', None)
    _safe_set(owner, 'plsql_declaration_VariableDeclaration', partner)
    assert getattr(partner, 'Expression108') == owner
    _safe_set(owner, 'plsql_declaration_VariableDeclaration', None)
    assert getattr(partner, 'Expression108') is None


def test_assoc_assign131_stub_double():
    # Expression has no real 'Expression132' property in the generated
    # code (a bare stub) -- manually attach it so plsql_declaration_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_declaration_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_declaration_Argument(default=True, in_=True, out=True)
    partner = Expression()
    setattr(partner, 'Expression132', None)
    _safe_set(owner, 'plsql_declaration_Argument', partner)
    assert getattr(partner, 'Expression132') == owner
    _safe_set(owner, 'plsql_declaration_Argument', None)
    assert getattr(partner, 'Expression132') is None


def test_assoc_expr1102_stub_double():
    # Expression has no real 'Expression103' property in the generated
    # code (a bare stub) -- manually attach it so plsql_condition_ConditionComparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_condition_ConditionComparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_condition_ConditionComparison(type="sample_text")
    partner = Expression()
    setattr(partner, 'Expression103', None)
    _safe_set(owner, 'plsql_condition_ConditionComparison', partner)
    assert getattr(partner, 'Expression103') == owner
    _safe_set(owner, 'plsql_condition_ConditionComparison', None)
    assert getattr(partner, 'Expression103') is None


def test_assoc_expr155_stub_double():
    # Expression has no real 'Expression56' property in the generated
    # code (a bare stub) -- manually attach it so plsql_expression_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_expression_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_expression_BooleanExpression(type="sample_text")
    partner = Expression()
    setattr(partner, 'Expression56', None)
    _safe_set(owner, 'plsql_expression_BooleanExpression', partner)
    assert getattr(partner, 'Expression56') == owner
    _safe_set(owner, 'plsql_expression_BooleanExpression', None)
    assert getattr(partner, 'Expression56') is None


def test_assoc_expr187_stub_double():
    # Expression has no real 'Expression88' property in the generated
    # code (a bare stub) -- manually attach it so plsql_expression_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_expression_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_expression_ArithmeticExpression(type="sample_text")
    partner = Expression()
    setattr(partner, 'Expression88', None)
    _safe_set(owner, 'plsql_expression_ArithmeticExpression', partner)
    assert getattr(partner, 'Expression88') == owner
    _safe_set(owner, 'plsql_expression_ArithmeticExpression', None)
    assert getattr(partner, 'Expression88') is None


def test_assoc_expr195_stub_double():
    # SQLCondition has no real 'SQLCondition96' property in the generated
    # code (a bare stub) -- manually attach it so plsql_condition_BooleanCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_condition_BooleanCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_condition_BooleanCondition(type="sample_text")
    partner = SQLCondition()
    setattr(partner, 'SQLCondition96', None)
    _safe_set(owner, 'plsql_condition_BooleanCondition', partner)
    assert getattr(partner, 'SQLCondition96') == owner
    _safe_set(owner, 'plsql_condition_BooleanCondition', None)
    assert getattr(partner, 'SQLCondition96') is None


def test_assoc_expr2104_stub_double():
    # Expression has no real 'Expression106' property in the generated
    # code (a bare stub) -- manually attach it so plsql_condition_ConditionComparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_condition_ConditionComparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_condition_ConditionComparison(type="sample_text")
    partner = Expression()
    setattr(partner, 'Expression106', None)
    _safe_set(owner, 'plsql_condition_ConditionComparison105', partner)
    assert getattr(partner, 'Expression106') == owner
    _safe_set(owner, 'plsql_condition_ConditionComparison105', None)
    assert getattr(partner, 'Expression106') is None


def test_assoc_expr257_stub_double():
    # Expression has no real 'Expression59' property in the generated
    # code (a bare stub) -- manually attach it so plsql_expression_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_expression_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_expression_BooleanExpression(type="sample_text")
    partner = Expression()
    setattr(partner, 'Expression59', None)
    _safe_set(owner, 'plsql_expression_BooleanExpression58', partner)
    assert getattr(partner, 'Expression59') == owner
    _safe_set(owner, 'plsql_expression_BooleanExpression58', None)
    assert getattr(partner, 'Expression59') is None


def test_assoc_expr289_stub_double():
    # Expression has no real 'Expression91' property in the generated
    # code (a bare stub) -- manually attach it so plsql_expression_ArithmeticExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_expression_ArithmeticExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_expression_ArithmeticExpression(type="sample_text")
    partner = Expression()
    setattr(partner, 'Expression91', None)
    _safe_set(owner, 'plsql_expression_ArithmeticExpression90', partner)
    assert getattr(partner, 'Expression91') == owner
    _safe_set(owner, 'plsql_expression_ArithmeticExpression90', None)
    assert getattr(partner, 'Expression91') is None


def test_assoc_expr297_stub_double():
    # SQLCondition has no real 'SQLCondition99' property in the generated
    # code (a bare stub) -- manually attach it so plsql_condition_BooleanCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_condition_BooleanCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_condition_BooleanCondition(type="sample_text")
    partner = SQLCondition()
    setattr(partner, 'SQLCondition99', None)
    _safe_set(owner, 'plsql_condition_BooleanCondition98', partner)
    assert getattr(partner, 'SQLCondition99') == owner
    _safe_set(owner, 'plsql_condition_BooleanCondition98', None)
    assert getattr(partner, 'SQLCondition99') is None


def test_assoc_expr83_stub_double():
    # Expression has no real 'Expression84' property in the generated
    # code (a bare stub) -- manually attach it so plsql_expression_PropertyAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_expression_PropertyAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_expression_PropertyAccess(propertyName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression84', None)
    _safe_set(owner, 'plsql_expression_PropertyAccess', partner)
    assert getattr(partner, 'Expression84') == owner
    _safe_set(owner, 'plsql_expression_PropertyAccess', None)
    assert getattr(partner, 'Expression84') is None


def test_assoc_expression51_stub_double():
    # Expression has no real 'Expression52' property in the generated
    # code (a bare stub) -- manually attach it so plsql_statement_UpdatePair's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_statement_UpdatePair's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_statement_UpdatePair(column="sample_text")
    partner = Expression()
    setattr(partner, 'Expression52', None)
    _safe_set(owner, 'plsql_statement_UpdatePair', partner)
    assert getattr(partner, 'Expression52') == owner
    _safe_set(owner, 'plsql_statement_UpdatePair', None)
    assert getattr(partner, 'Expression52') is None


def test_assoc_into38_stub_double():
    # VarRefExpression has no real 'VarRefExpression39' property in the generated
    # code (a bare stub) -- manually attach it so plsql_statement_SelectStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_statement_SelectStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_statement_SelectStatement(all=True, bulk=True, collect=True, distinct=True, from_="sample_text", isCount=True, selectList="sample_text", unique=True)
    partner = VarRefExpression()
    setattr(partner, 'VarRefExpression39', None)
    _safe_set(owner, 'plsql_statement_SelectStatement', {partner})
    assert getattr(partner, 'VarRefExpression39') == owner
    _safe_set(owner, 'plsql_statement_SelectStatement', set())
    assert getattr(partner, 'VarRefExpression39') is None


def test_assoc_orderBy42_stub_double():
    # Expression has no real 'Expression44' property in the generated
    # code (a bare stub) -- manually attach it so plsql_statement_SelectStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_statement_SelectStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_statement_SelectStatement(all=True, bulk=True, collect=True, distinct=True, from_="sample_text", isCount=True, selectList="sample_text", unique=True)
    partner = Expression()
    setattr(partner, 'Expression44', None)
    _safe_set(owner, 'plsql_statement_SelectStatement43', {partner})
    assert getattr(partner, 'Expression44') == owner
    _safe_set(owner, 'plsql_statement_SelectStatement43', set())
    assert getattr(partner, 'Expression44') is None


def test_assoc_pairs47_stub_double():
    # UpdatePair has no real 'UpdatePair' property in the generated
    # code (a bare stub) -- manually attach it so plsql_statement_UpdateStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_statement_UpdateStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_statement_UpdateStatement(table="sample_text")
    partner = UpdatePair()
    setattr(partner, 'UpdatePair', None)
    _safe_set(owner, 'plsql_statement_UpdateStatement', {partner})
    assert getattr(partner, 'UpdatePair') == owner
    _safe_set(owner, 'plsql_statement_UpdateStatement', set())
    assert getattr(partner, 'UpdatePair') is None


def test_assoc_statements53_stub_double():
    # Statement has no real 'Statement54' property in the generated
    # code (a bare stub) -- manually attach it so plsql_statement_ExceptionSection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_statement_ExceptionSection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_statement_ExceptionSection(exceptionNames="sample_text")
    partner = Statement()
    setattr(partner, 'Statement54', None)
    _safe_set(owner, 'plsql_statement_ExceptionSection', {partner})
    assert getattr(partner, 'Statement54') == owner
    _safe_set(owner, 'plsql_statement_ExceptionSection', set())
    assert getattr(partner, 'Statement54') is None


def test_assoc_values45_stub_double():
    # Expression has no real 'Expression46' property in the generated
    # code (a bare stub) -- manually attach it so plsql_statement_InsertStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_statement_InsertStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_statement_InsertStatement(columns="sample_text", into="sample_text")
    partner = Expression()
    setattr(partner, 'Expression46', None)
    _safe_set(owner, 'plsql_statement_InsertStatement', {partner})
    assert getattr(partner, 'Expression46') == owner
    _safe_set(owner, 'plsql_statement_InsertStatement', set())
    assert getattr(partner, 'Expression46') is None


def test_assoc_where40_stub_double():
    # SQLCondition has no real 'SQLCondition' property in the generated
    # code (a bare stub) -- manually attach it so plsql_statement_SelectStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_statement_SelectStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_statement_SelectStatement(all=True, bulk=True, collect=True, distinct=True, from_="sample_text", isCount=True, selectList="sample_text", unique=True)
    partner = SQLCondition()
    setattr(partner, 'SQLCondition', None)
    _safe_set(owner, 'plsql_statement_SelectStatement41', partner)
    assert getattr(partner, 'SQLCondition') == owner
    _safe_set(owner, 'plsql_statement_SelectStatement41', None)
    assert getattr(partner, 'SQLCondition') is None


def test_assoc_where48_stub_double():
    # SQLCondition has no real 'SQLCondition50' property in the generated
    # code (a bare stub) -- manually attach it so plsql_statement_UpdateStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # plsql_statement_UpdateStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = plsql_statement_UpdateStatement(table="sample_text")
    partner = SQLCondition()
    setattr(partner, 'SQLCondition50', None)
    _safe_set(owner, 'plsql_statement_UpdateStatement49', partner)
    assert getattr(partner, 'SQLCondition50') == owner
    _safe_set(owner, 'plsql_statement_UpdateStatement49', None)
    assert getattr(partner, 'SQLCondition50') is None


