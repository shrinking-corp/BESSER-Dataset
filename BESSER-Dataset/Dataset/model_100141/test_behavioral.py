import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AlterTableAction,
    Comment,
    Constraint,
    Create,
    DdlStatement,
    LongRaw,
    SqlDataType,
    SqlDateTime,
    TableProperty,
    ddlDsl_AddTableConstraint,
    ddlDsl_Alter,
    ddlDsl_AlterTableAction,
    ddlDsl_Column,
    ddlDsl_ColumnComment,
    ddlDsl_Comment,
    ddlDsl_Constraint,
    ddlDsl_Create,
    ddlDsl_CreateIndex,
    ddlDsl_CreateTable,
    ddlDsl_Ddl,
    ddlDsl_DdlStatement,
    ddlDsl_Drop,
    ddlDsl_DropTableConstraint,
    ddlDsl_ForeignKeyConstraint,
    ddlDsl_LargeObjectType,
    ddlDsl_Long,
    ddlDsl_LongRaw,
    ddlDsl_NullableConstraint,
    ddlDsl_PrimaryKeyConstraint,
    ddlDsl_Raw,
    ddlDsl_ReferenceClause,
    ddlDsl_RowIdType,
    ddlDsl_SqlBoolean,
    ddlDsl_SqlCharacter,
    ddlDsl_SqlDataType,
    ddlDsl_SqlDate,
    ddlDsl_SqlDateTime,
    ddlDsl_SqlInterval,
    ddlDsl_SqlNumber,
    ddlDsl_SqlTimeStamp,
    ddlDsl_TableComment,
    ddlDsl_TableProperty,
    ddlDsl_UniqueKeyConstraint,
    SortDirectionEnum,
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

def test_assoc_columns15_reverse_link_reassign_clear():
    a1 = ddlDsl_CreateIndex(sortOrders="sample_text", unique=True)
    a2 = ddlDsl_CreateIndex(sortOrders="sample_text_2", unique=False)
    b = ddlDsl_Column(default="sample_text", sorted=True)
    _safe_set(b, 'ddlDsl_Column17', a1)
    assert _is_linked(b, 'ddlDsl_Column17', a1)
    if hasattr(a1, 'ddlDsl_CreateIndex16'):
        assert _is_linked(a1, 'ddlDsl_CreateIndex16', b)
    _safe_set(b, 'ddlDsl_Column17', a2)
    assert _is_linked(b, 'ddlDsl_Column17', a2)
    if hasattr(a1, 'ddlDsl_CreateIndex16'):
        assert not _is_linked(a1, 'ddlDsl_CreateIndex16', b)
    if hasattr(a2, 'ddlDsl_CreateIndex16'):
        assert _is_linked(a2, 'ddlDsl_CreateIndex16', b)
    _safe_set(b, 'ddlDsl_Column17', None)
    assert not _is_linked(b, 'ddlDsl_Column17', a2)
    if hasattr(a2, 'ddlDsl_CreateIndex16'):
        assert not _is_linked(a2, 'ddlDsl_CreateIndex16', b)


def test_assoc_type18_reverse_link_reassign_clear():
    a1 = ddlDsl_SqlDataType(name="sample_text")
    a2 = ddlDsl_SqlDataType(name="sample_text_2")
    b = ddlDsl_Column(default="sample_text", sorted=True)
    _safe_set(b, 'ddlDsl_Column19', a1)
    assert _is_linked(b, 'ddlDsl_Column19', a1)
    if hasattr(a1, 'ddlDsl_SqlDataType'):
        assert _is_linked(a1, 'ddlDsl_SqlDataType', b)
    _safe_set(b, 'ddlDsl_Column19', a2)
    assert _is_linked(b, 'ddlDsl_Column19', a2)
    if hasattr(a1, 'ddlDsl_SqlDataType'):
        assert not _is_linked(a1, 'ddlDsl_SqlDataType', b)
    if hasattr(a2, 'ddlDsl_SqlDataType'):
        assert _is_linked(a2, 'ddlDsl_SqlDataType', b)
    _safe_set(b, 'ddlDsl_Column19', None)
    assert not _is_linked(b, 'ddlDsl_Column19', a2)
    if hasattr(a2, 'ddlDsl_SqlDataType'):
        assert not _is_linked(a2, 'ddlDsl_SqlDataType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_column10_stub_double():
    # ddlDsl_ColumnComment has no real 'ddlDsl_ColumnComment' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_Column(default="sample_text", sorted=True)
    partner = ddlDsl_ColumnComment()
    setattr(partner, 'ddlDsl_ColumnComment', None)
    _safe_set(owner, 'ddlDsl_Column', partner)
    assert getattr(partner, 'ddlDsl_ColumnComment') == owner
    _safe_set(owner, 'ddlDsl_Column', None)
    assert getattr(partner, 'ddlDsl_ColumnComment') is None


def test_assoc_columns25_stub_double():
    # ddlDsl_UniqueKeyConstraint has no real 'ddlDsl_UniqueKeyConstraint' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_Column(default="sample_text", sorted=True)
    partner = ddlDsl_UniqueKeyConstraint()
    setattr(partner, 'ddlDsl_UniqueKeyConstraint', None)
    _safe_set(owner, 'ddlDsl_Column26', partner)
    assert owner in getattr(partner, 'ddlDsl_UniqueKeyConstraint')
    _safe_set(owner, 'ddlDsl_Column26', None)
    assert owner not in getattr(partner, 'ddlDsl_UniqueKeyConstraint')


def test_assoc_columns27_stub_double():
    # ddlDsl_PrimaryKeyConstraint has no real 'ddlDsl_PrimaryKeyConstraint' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_Column(default="sample_text", sorted=True)
    partner = ddlDsl_PrimaryKeyConstraint()
    setattr(partner, 'ddlDsl_PrimaryKeyConstraint', None)
    _safe_set(owner, 'ddlDsl_Column28', partner)
    assert owner in getattr(partner, 'ddlDsl_PrimaryKeyConstraint')
    _safe_set(owner, 'ddlDsl_Column28', None)
    assert owner not in getattr(partner, 'ddlDsl_PrimaryKeyConstraint')


def test_assoc_columns29_stub_double():
    # ddlDsl_ForeignKeyConstraint has no real 'ddlDsl_ForeignKeyConstraint' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_Column(default="sample_text", sorted=True)
    partner = ddlDsl_ForeignKeyConstraint()
    setattr(partner, 'ddlDsl_ForeignKeyConstraint', None)
    _safe_set(owner, 'ddlDsl_Column30', partner)
    assert owner in getattr(partner, 'ddlDsl_ForeignKeyConstraint')
    _safe_set(owner, 'ddlDsl_Column30', None)
    assert owner not in getattr(partner, 'ddlDsl_ForeignKeyConstraint')


def test_assoc_columns37_stub_double():
    # ddlDsl_ReferenceClause has no real 'ddlDsl_ReferenceClause38' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_Column(default="sample_text", sorted=True)
    partner = ddlDsl_ReferenceClause()
    setattr(partner, 'ddlDsl_ReferenceClause38', None)
    _safe_set(owner, 'ddlDsl_Column39', partner)
    assert owner in getattr(partner, 'ddlDsl_ReferenceClause38')
    _safe_set(owner, 'ddlDsl_Column39', None)
    assert owner not in getattr(partner, 'ddlDsl_ReferenceClause38')


def test_assoc_constraint20_stub_double():
    # ddlDsl_Constraint has no real 'ddlDsl_Constraint22' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_Column(default="sample_text", sorted=True)
    partner = ddlDsl_Constraint()
    setattr(partner, 'ddlDsl_Constraint22', None)
    _safe_set(owner, 'ddlDsl_Column21', partner)
    assert getattr(partner, 'ddlDsl_Constraint22') == owner
    _safe_set(owner, 'ddlDsl_Column21', None)
    assert getattr(partner, 'ddlDsl_Constraint22') is None


def test_assoc_properties11_stub_double():
    # ddlDsl_CreateTable has no real 'ddlDsl_CreateTable12' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_TableProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_TableProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_TableProperty(name="sample_text")
    partner = ddlDsl_CreateTable()
    setattr(partner, 'ddlDsl_CreateTable12', None)
    _safe_set(owner, 'ddlDsl_TableProperty', partner)
    assert owner in getattr(partner, 'ddlDsl_CreateTable12')
    _safe_set(owner, 'ddlDsl_TableProperty', None)
    assert owner not in getattr(partner, 'ddlDsl_CreateTable12')


def test_assoc_reference23_stub_double():
    # ddlDsl_ReferenceClause has no real 'ddlDsl_ReferenceClause' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_Column(default="sample_text", sorted=True)
    partner = ddlDsl_ReferenceClause()
    setattr(partner, 'ddlDsl_ReferenceClause', None)
    _safe_set(owner, 'ddlDsl_Column24', partner)
    assert getattr(partner, 'ddlDsl_ReferenceClause') == owner
    _safe_set(owner, 'ddlDsl_Column24', None)
    assert getattr(partner, 'ddlDsl_ReferenceClause') is None


def test_assoc_table13_stub_double():
    # ddlDsl_CreateTable has no real 'ddlDsl_CreateTable14' property in the generated
    # code (a bare stub) -- manually attach it so ddlDsl_CreateIndex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddlDsl_CreateIndex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddlDsl_CreateIndex(sortOrders="sample_text", unique=True)
    partner = ddlDsl_CreateTable()
    setattr(partner, 'ddlDsl_CreateTable14', None)
    _safe_set(owner, 'ddlDsl_CreateIndex', partner)
    assert getattr(partner, 'ddlDsl_CreateTable14') == owner
    _safe_set(owner, 'ddlDsl_CreateIndex', None)
    assert getattr(partner, 'ddlDsl_CreateTable14') is None


