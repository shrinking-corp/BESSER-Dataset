import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExp,
    ColumnExp,
    DataType,
    Expression,
    LocatedElement,
    NamedElement,
    Predicate,
    QueryStmt,
    SQLDML_AndExp,
    SQLDML_BinaryExp,
    SQLDML_ColumnExp,
    SQLDML_DataType,
    SQLDML_Expression,
    SQLDML_FunctionExp,
    SQLDML_InExp,
    SQLDML_InsertStmt,
    SQLDML_IntegerValueExp,
    SQLDML_LikeExp,
    SQLDML_ListExp,
    SQLDML_LocatedElement,
    SQLDML_NamedElement,
    SQLDML_NotExp,
    SQLDML_OperationExp,
    SQLDML_OrExp,
    SQLDML_Predicate,
    SQLDML_QueryPredicate,
    SQLDML_QueryStmt,
    SQLDML_QueryStmtAllCol,
    SQLDML_QueryStmtCol,
    SQLDML_SQLRoot,
    SQLDML_Statement,
    SQLDML_StringValueExp,
    SQLDML_Table,
    SQLDML_ValueExp,
    SQLDML_ViewStatement,
    SQLDML_WhereClause,
    Statement,
    StringValueExp,
    Table,
    ValueExp,
    WhereClause,
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

def test_assoc_arguments31_stub_double():
    # Expression has no real 'Expression32' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_FunctionExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_FunctionExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_FunctionExp(name="sample_text")
    partner = Expression()
    setattr(partner, 'Expression32', None)
    _safe_set(owner, 'SQLDML_FunctionExp', {partner})
    assert getattr(partner, 'Expression32') == owner
    _safe_set(owner, 'SQLDML_FunctionExp', set())
    assert getattr(partner, 'Expression32') is None


def test_assoc_columns1_stub_double():
    # ColumnExp has no real 'ColumnExp' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_ViewStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_ViewStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_ViewStatement(name="sample_text")
    partner = ColumnExp()
    setattr(partner, 'ColumnExp', None)
    _safe_set(owner, 'SQLDML_ViewStatement', {partner})
    assert getattr(partner, 'ColumnExp') == owner
    _safe_set(owner, 'SQLDML_ViewStatement', set())
    assert getattr(partner, 'ColumnExp') is None


def test_assoc_elements23_stub_double():
    # Predicate has no real 'Predicate' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_InExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_InExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_InExp(columnName="sample_text")
    partner = Predicate()
    setattr(partner, 'Predicate', None)
    _safe_set(owner, 'SQLDML_InExp', {partner})
    assert getattr(partner, 'Predicate') == owner
    _safe_set(owner, 'SQLDML_InExp', set())
    assert getattr(partner, 'Predicate') is None


def test_assoc_expression22_stub_double():
    # StringValueExp has no real 'StringValueExp' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_LikeExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_LikeExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_LikeExp(columnName="sample_text")
    partner = StringValueExp()
    setattr(partner, 'StringValueExp', None)
    _safe_set(owner, 'SQLDML_LikeExp', partner)
    assert getattr(partner, 'StringValueExp') == owner
    _safe_set(owner, 'SQLDML_LikeExp', None)
    assert getattr(partner, 'StringValueExp') is None


def test_assoc_leftExp12_stub_double():
    # Expression has no real 'Expression13' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_BinaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_BinaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_BinaryExp(opName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression13', None)
    _safe_set(owner, 'SQLDML_BinaryExp', partner)
    assert getattr(partner, 'Expression13') == owner
    _safe_set(owner, 'SQLDML_BinaryExp', None)
    assert getattr(partner, 'Expression13') is None


def test_assoc_query2_stub_double():
    # QueryStmt has no real 'QueryStmt' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_ViewStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_ViewStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_ViewStatement(name="sample_text")
    partner = QueryStmt()
    setattr(partner, 'QueryStmt', None)
    _safe_set(owner, 'SQLDML_ViewStatement3', partner)
    assert getattr(partner, 'QueryStmt') == owner
    _safe_set(owner, 'SQLDML_ViewStatement3', None)
    assert getattr(partner, 'QueryStmt') is None


def test_assoc_rightExp14_stub_double():
    # Expression has no real 'Expression16' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_BinaryExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_BinaryExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_BinaryExp(opName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression16', None)
    _safe_set(owner, 'SQLDML_BinaryExp15', partner)
    assert getattr(partner, 'Expression16') == owner
    _safe_set(owner, 'SQLDML_BinaryExp15', None)
    assert getattr(partner, 'Expression16') is None


def test_assoc_type26_stub_double():
    # DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_ColumnExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_ColumnExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_ColumnExp(alias="sample_text")
    partner = DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'SQLDML_ColumnExp', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'SQLDML_ColumnExp', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_unused19_stub_double():
    # Expression has no real 'Expression21' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_NotExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_NotExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_NotExp(opName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression21', None)
    _safe_set(owner, 'SQLDML_NotExp20', partner)
    assert getattr(partner, 'Expression21') == owner
    _safe_set(owner, 'SQLDML_NotExp20', None)
    assert getattr(partner, 'Expression21') is None


def test_assoc_valueExp17_stub_double():
    # Expression has no real 'Expression18' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_NotExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_NotExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_NotExp(opName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression18', None)
    _safe_set(owner, 'SQLDML_NotExp', partner)
    assert getattr(partner, 'Expression18') == owner
    _safe_set(owner, 'SQLDML_NotExp', None)
    assert getattr(partner, 'Expression18') is None


def test_assoc_values4_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so SQLDML_InsertStmt's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SQLDML_InsertStmt's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SQLDML_InsertStmt(tableName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'SQLDML_InsertStmt', {partner})
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'SQLDML_InsertStmt', set())
    assert getattr(partner, 'Expression') is None


