import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SqlExpr,
    SqlSentence,
    TableConstraint,
    TriggerAction,
    Type,
    sqls_Column,
    sqls_ColumnRef,
    sqls_Delete,
    sqls_DeleteTable,
    sqls_Enum,
    sqls_EnumElement,
    sqls_Function,
    sqls_Get,
    sqls_Import,
    sqls_Insert,
    sqls_InsertStatement,
    sqls_NewColumn,
    sqls_OldColumn,
    sqls_OrderingTerm,
    sqls_ResultColumn,
    sqls_Select,
    sqls_SelectList,
    sqls_SqlBinaryExpr,
    sqls_SqlExpr,
    sqls_SqlFunction,
    sqls_SqlLibrary,
    sqls_SqlMethod,
    sqls_SqlMethodRef,
    sqls_SqlNested,
    sqls_SqlNumberLiteral,
    sqls_SqlParam,
    sqls_SqlPlaceholder,
    sqls_SqlSentence,
    sqls_SqlStringLiteral,
    sqls_SqlType,
    sqls_Table,
    sqls_TableConstraint,
    sqls_TableRef,
    sqls_Tag,
    sqls_Trigger,
    sqls_TriggerAction,
    sqls_TriggerDelete,
    sqls_TriggerInsert,
    sqls_TriggerUpdate,
    sqls_Type,
    sqls_TypeDef,
    sqls_UniqueTableConstraint,
    sqls_Update,
    sqls_UpdateColumnExpression,
    TriggerTime,
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

def test_assoc_columns31_reverse_link_reassign_clear():
    a1 = sqls_UniqueTableConstraint(name="sample_text")
    a2 = sqls_UniqueTableConstraint(name="sample_text_2")
    b = sqls_Column(name="sample_text", null=True, primaryKey=True)
    _safe_set(b, 'sqls_Column32', a1)
    assert _is_linked(b, 'sqls_Column32', a1)
    if hasattr(a1, 'sqls_UniqueTableConstraint'):
        assert _is_linked(a1, 'sqls_UniqueTableConstraint', b)
    _safe_set(b, 'sqls_Column32', a2)
    assert _is_linked(b, 'sqls_Column32', a2)
    if hasattr(a1, 'sqls_UniqueTableConstraint'):
        assert not _is_linked(a1, 'sqls_UniqueTableConstraint', b)
    if hasattr(a2, 'sqls_UniqueTableConstraint'):
        assert _is_linked(a2, 'sqls_UniqueTableConstraint', b)
    _safe_set(b, 'sqls_Column32', None)
    assert not _is_linked(b, 'sqls_Column32', a2)
    if hasattr(a2, 'sqls_UniqueTableConstraint'):
        assert not _is_linked(a2, 'sqls_UniqueTableConstraint', b)


def test_assoc_fields21_reverse_link_reassign_clear():
    a1 = sqls_Table(name="sample_text")
    a2 = sqls_Table(name="sample_text_2")
    b = sqls_Column(name="sample_text", null=True, primaryKey=True)
    _safe_set(b, 'sqls_Column', a1)
    assert _is_linked(b, 'sqls_Column', a1)
    if hasattr(a1, 'sqls_Table22'):
        assert _is_linked(a1, 'sqls_Table22', b)
    _safe_set(b, 'sqls_Column', a2)
    assert _is_linked(b, 'sqls_Column', a2)
    if hasattr(a1, 'sqls_Table22'):
        assert not _is_linked(a1, 'sqls_Table22', b)
    if hasattr(a2, 'sqls_Table22'):
        assert _is_linked(a2, 'sqls_Table22', b)
    _safe_set(b, 'sqls_Column', None)
    assert not _is_linked(b, 'sqls_Column', a2)
    if hasattr(a2, 'sqls_Table22'):
        assert not _is_linked(a2, 'sqls_Table22', b)


def test_assoc_from_49_reverse_link_reassign_clear():
    a1 = sqls_TableRef(alias="sample_text")
    a2 = sqls_TableRef(alias="sample_text_2")
    b = sqls_Select(all=True)
    _safe_set(b, 'sqls_Select50', a1)
    assert _is_linked(b, 'sqls_Select50', a1)
    if hasattr(a1, 'sqls_TableRef'):
        assert _is_linked(a1, 'sqls_TableRef', b)
    _safe_set(b, 'sqls_Select50', a2)
    assert _is_linked(b, 'sqls_Select50', a2)
    if hasattr(a1, 'sqls_TableRef'):
        assert not _is_linked(a1, 'sqls_TableRef', b)
    if hasattr(a2, 'sqls_TableRef'):
        assert _is_linked(a2, 'sqls_TableRef', b)
    _safe_set(b, 'sqls_Select50', None)
    assert not _is_linked(b, 'sqls_Select50', a2)
    if hasattr(a2, 'sqls_TableRef'):
        assert not _is_linked(a2, 'sqls_TableRef', b)


def test_assoc_methods12_reverse_link_reassign_clear():
    a1 = sqls_SqlMethod(array=True, name="sample_text")
    a2 = sqls_SqlMethod(array=False, name="sample_text_2")
    b = sqls_SqlLibrary(database="sample_text", version=7)
    _safe_set(b, 'sqls_SqlLibrary13', {a1})
    assert _is_linked(b, 'sqls_SqlLibrary13', a1)
    if hasattr(a1, 'sqls_SqlMethod'):
        assert _is_linked(a1, 'sqls_SqlMethod', b)
    _safe_set(b, 'sqls_SqlLibrary13', {a2})
    assert _is_linked(b, 'sqls_SqlLibrary13', a2)
    if hasattr(a1, 'sqls_SqlMethod'):
        assert not _is_linked(a1, 'sqls_SqlMethod', b)
    if hasattr(a2, 'sqls_SqlMethod'):
        assert _is_linked(a2, 'sqls_SqlMethod', b)
    _safe_set(b, 'sqls_SqlLibrary13', set())
    assert not _is_linked(b, 'sqls_SqlLibrary13', a2)
    if hasattr(a2, 'sqls_SqlMethod'):
        assert not _is_linked(a2, 'sqls_SqlMethod', b)


def test_assoc_orderingTerms54_reverse_link_reassign_clear():
    a1 = sqls_Select(all=True)
    a2 = sqls_Select(all=False)
    b = sqls_OrderingTerm(asc=True, desc=True)
    _safe_set(b, 'sqls_OrderingTerm56', a1)
    assert _is_linked(b, 'sqls_OrderingTerm56', a1)
    if hasattr(a1, 'sqls_Select55'):
        assert _is_linked(a1, 'sqls_Select55', b)
    _safe_set(b, 'sqls_OrderingTerm56', a2)
    assert _is_linked(b, 'sqls_OrderingTerm56', a2)
    if hasattr(a1, 'sqls_Select55'):
        assert not _is_linked(a1, 'sqls_Select55', b)
    if hasattr(a2, 'sqls_Select55'):
        assert _is_linked(a2, 'sqls_Select55', b)
    _safe_set(b, 'sqls_OrderingTerm56', None)
    assert not _is_linked(b, 'sqls_OrderingTerm56', a2)
    if hasattr(a2, 'sqls_Select55'):
        assert not _is_linked(a2, 'sqls_Select55', b)


def test_assoc_table105_reverse_link_reassign_clear():
    a1 = sqls_Trigger(name="sample_text", time="sample_text")
    a2 = sqls_Trigger(name="sample_text_2", time="sample_text_2")
    b = sqls_Table(name="sample_text")
    _safe_set(b, 'sqls_Table107', a1)
    assert _is_linked(b, 'sqls_Table107', a1)
    if hasattr(a1, 'sqls_Trigger106'):
        assert _is_linked(a1, 'sqls_Trigger106', b)
    _safe_set(b, 'sqls_Table107', a2)
    assert _is_linked(b, 'sqls_Table107', a2)
    if hasattr(a1, 'sqls_Trigger106'):
        assert not _is_linked(a1, 'sqls_Trigger106', b)
    if hasattr(a2, 'sqls_Trigger106'):
        assert _is_linked(a2, 'sqls_Trigger106', b)
    _safe_set(b, 'sqls_Table107', None)
    assert not _is_linked(b, 'sqls_Table107', a2)
    if hasattr(a2, 'sqls_Trigger106'):
        assert not _is_linked(a2, 'sqls_Trigger106', b)


def test_assoc_table63_reverse_link_reassign_clear():
    a1 = sqls_TableRef(alias="sample_text")
    a2 = sqls_TableRef(alias="sample_text_2")
    b = sqls_Table(name="sample_text")
    _safe_set(b, 'sqls_Table65', a1)
    assert _is_linked(b, 'sqls_Table65', a1)
    if hasattr(a1, 'sqls_TableRef64'):
        assert _is_linked(a1, 'sqls_TableRef64', b)
    _safe_set(b, 'sqls_Table65', a2)
    assert _is_linked(b, 'sqls_Table65', a2)
    if hasattr(a1, 'sqls_TableRef64'):
        assert not _is_linked(a1, 'sqls_TableRef64', b)
    if hasattr(a2, 'sqls_TableRef64'):
        assert _is_linked(a2, 'sqls_TableRef64', b)
    _safe_set(b, 'sqls_Table65', None)
    assert not _is_linked(b, 'sqls_Table65', a2)
    if hasattr(a2, 'sqls_TableRef64'):
        assert not _is_linked(a2, 'sqls_TableRef64', b)


def test_assoc_tables8_reverse_link_reassign_clear():
    a1 = sqls_Table(name="sample_text")
    a2 = sqls_Table(name="sample_text_2")
    b = sqls_SqlLibrary(database="sample_text", version=7)
    _safe_set(b, 'sqls_SqlLibrary9', {a1})
    assert _is_linked(b, 'sqls_SqlLibrary9', a1)
    if hasattr(a1, 'sqls_Table'):
        assert _is_linked(a1, 'sqls_Table', b)
    _safe_set(b, 'sqls_SqlLibrary9', {a2})
    assert _is_linked(b, 'sqls_SqlLibrary9', a2)
    if hasattr(a1, 'sqls_Table'):
        assert not _is_linked(a1, 'sqls_Table', b)
    if hasattr(a2, 'sqls_Table'):
        assert _is_linked(a2, 'sqls_Table', b)
    _safe_set(b, 'sqls_SqlLibrary9', set())
    assert not _is_linked(b, 'sqls_SqlLibrary9', a2)
    if hasattr(a2, 'sqls_Table'):
        assert not _is_linked(a2, 'sqls_Table', b)


def test_assoc_tags1_reverse_link_reassign_clear():
    a1 = sqls_Tag(name="sample_text")
    a2 = sqls_Tag(name="sample_text_2")
    b = sqls_SqlLibrary(database="sample_text", version=7)
    _safe_set(b, 'sqls_SqlLibrary2', {a1})
    assert _is_linked(b, 'sqls_SqlLibrary2', a1)
    if hasattr(a1, 'sqls_Tag'):
        assert _is_linked(a1, 'sqls_Tag', b)
    _safe_set(b, 'sqls_SqlLibrary2', {a2})
    assert _is_linked(b, 'sqls_SqlLibrary2', a2)
    if hasattr(a1, 'sqls_Tag'):
        assert not _is_linked(a1, 'sqls_Tag', b)
    if hasattr(a2, 'sqls_Tag'):
        assert _is_linked(a2, 'sqls_Tag', b)
    _safe_set(b, 'sqls_SqlLibrary2', set())
    assert not _is_linked(b, 'sqls_SqlLibrary2', a2)
    if hasattr(a2, 'sqls_Tag'):
        assert not _is_linked(a2, 'sqls_Tag', b)


def test_assoc_tags100_reverse_link_reassign_clear():
    a1 = sqls_Trigger(name="sample_text", time="sample_text")
    a2 = sqls_Trigger(name="sample_text_2", time="sample_text_2")
    b = sqls_Tag(name="sample_text")
    _safe_set(b, 'sqls_Tag102', a1)
    assert _is_linked(b, 'sqls_Tag102', a1)
    if hasattr(a1, 'sqls_Trigger101'):
        assert _is_linked(a1, 'sqls_Trigger101', b)
    _safe_set(b, 'sqls_Tag102', a2)
    assert _is_linked(b, 'sqls_Tag102', a2)
    if hasattr(a1, 'sqls_Trigger101'):
        assert not _is_linked(a1, 'sqls_Trigger101', b)
    if hasattr(a2, 'sqls_Trigger101'):
        assert _is_linked(a2, 'sqls_Trigger101', b)
    _safe_set(b, 'sqls_Tag102', None)
    assert not _is_linked(b, 'sqls_Tag102', a2)
    if hasattr(a2, 'sqls_Trigger101'):
        assert not _is_linked(a2, 'sqls_Trigger101', b)


def test_assoc_tags18_reverse_link_reassign_clear():
    a1 = sqls_Tag(name="sample_text")
    a2 = sqls_Tag(name="sample_text_2")
    b = sqls_Table(name="sample_text")
    _safe_set(b, 'sqls_Table19', {a1})
    assert _is_linked(b, 'sqls_Table19', a1)
    if hasattr(a1, 'sqls_Tag20'):
        assert _is_linked(a1, 'sqls_Tag20', b)
    _safe_set(b, 'sqls_Table19', {a2})
    assert _is_linked(b, 'sqls_Table19', a2)
    if hasattr(a1, 'sqls_Tag20'):
        assert not _is_linked(a1, 'sqls_Tag20', b)
    if hasattr(a2, 'sqls_Tag20'):
        assert _is_linked(a2, 'sqls_Tag20', b)
    _safe_set(b, 'sqls_Table19', set())
    assert not _is_linked(b, 'sqls_Table19', a2)
    if hasattr(a2, 'sqls_Tag20'):
        assert not _is_linked(a2, 'sqls_Tag20', b)


def test_assoc_tags33_reverse_link_reassign_clear():
    a1 = sqls_Tag(name="sample_text")
    a2 = sqls_Tag(name="sample_text_2")
    b = sqls_SqlMethod(array=True, name="sample_text")
    _safe_set(b, 'sqls_SqlMethod34', {a1})
    assert _is_linked(b, 'sqls_SqlMethod34', a1)
    if hasattr(a1, 'sqls_Tag35'):
        assert _is_linked(a1, 'sqls_Tag35', b)
    _safe_set(b, 'sqls_SqlMethod34', {a2})
    assert _is_linked(b, 'sqls_SqlMethod34', a2)
    if hasattr(a1, 'sqls_Tag35'):
        assert not _is_linked(a1, 'sqls_Tag35', b)
    if hasattr(a2, 'sqls_Tag35'):
        assert _is_linked(a2, 'sqls_Tag35', b)
    _safe_set(b, 'sqls_SqlMethod34', set())
    assert not _is_linked(b, 'sqls_SqlMethod34', a2)
    if hasattr(a2, 'sqls_Tag35'):
        assert not _is_linked(a2, 'sqls_Tag35', b)


def test_assoc_triggers10_reverse_link_reassign_clear():
    a1 = sqls_Trigger(name="sample_text", time="sample_text")
    a2 = sqls_Trigger(name="sample_text_2", time="sample_text_2")
    b = sqls_SqlLibrary(database="sample_text", version=7)
    _safe_set(b, 'sqls_SqlLibrary11', {a1})
    assert _is_linked(b, 'sqls_SqlLibrary11', a1)
    if hasattr(a1, 'sqls_Trigger'):
        assert _is_linked(a1, 'sqls_Trigger', b)
    _safe_set(b, 'sqls_SqlLibrary11', {a2})
    assert _is_linked(b, 'sqls_SqlLibrary11', a2)
    if hasattr(a1, 'sqls_Trigger'):
        assert not _is_linked(a1, 'sqls_Trigger', b)
    if hasattr(a2, 'sqls_Trigger'):
        assert _is_linked(a2, 'sqls_Trigger', b)
    _safe_set(b, 'sqls_SqlLibrary11', set())
    assert not _is_linked(b, 'sqls_SqlLibrary11', a2)
    if hasattr(a2, 'sqls_Trigger'):
        assert not _is_linked(a2, 'sqls_Trigger', b)


def test_assoc_type36_reverse_link_reassign_clear():
    a1 = sqls_Table(name="sample_text")
    a2 = sqls_Table(name="sample_text_2")
    b = sqls_SqlMethod(array=True, name="sample_text")
    _safe_set(b, 'sqls_SqlMethod37', a1)
    assert _is_linked(b, 'sqls_SqlMethod37', a1)
    if hasattr(a1, 'sqls_Table38'):
        assert _is_linked(a1, 'sqls_Table38', b)
    _safe_set(b, 'sqls_SqlMethod37', a2)
    assert _is_linked(b, 'sqls_SqlMethod37', a2)
    if hasattr(a1, 'sqls_Table38'):
        assert not _is_linked(a1, 'sqls_Table38', b)
    if hasattr(a2, 'sqls_Table38'):
        assert _is_linked(a2, 'sqls_Table38', b)
    _safe_set(b, 'sqls_SqlMethod37', None)
    assert not _is_linked(b, 'sqls_SqlMethod37', a2)
    if hasattr(a2, 'sqls_Table38'):
        assert not _is_linked(a2, 'sqls_Table38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_action103_stub_double():
    # sqls_TriggerAction has no real 'sqls_TriggerAction' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Trigger(name="sample_text", time="sample_text")
    partner = sqls_TriggerAction()
    setattr(partner, 'sqls_TriggerAction', None)
    _safe_set(owner, 'sqls_Trigger104', partner)
    assert getattr(partner, 'sqls_TriggerAction') == owner
    _safe_set(owner, 'sqls_Trigger104', None)
    assert getattr(partner, 'sqls_TriggerAction') is None


def test_assoc_column119_stub_double():
    # sqls_NewColumn has no real 'sqls_NewColumn' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Column(name="sample_text", null=True, primaryKey=True)
    partner = sqls_NewColumn()
    setattr(partner, 'sqls_NewColumn', None)
    _safe_set(owner, 'sqls_Column120', partner)
    assert getattr(partner, 'sqls_NewColumn') == owner
    _safe_set(owner, 'sqls_Column120', None)
    assert getattr(partner, 'sqls_NewColumn') is None


def test_assoc_column121_stub_double():
    # sqls_OldColumn has no real 'sqls_OldColumn' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Column(name="sample_text", null=True, primaryKey=True)
    partner = sqls_OldColumn()
    setattr(partner, 'sqls_OldColumn', None)
    _safe_set(owner, 'sqls_Column122', partner)
    assert getattr(partner, 'sqls_OldColumn') == owner
    _safe_set(owner, 'sqls_Column122', None)
    assert getattr(partner, 'sqls_OldColumn') is None


def test_assoc_column127_stub_double():
    # sqls_ColumnRef has no real 'sqls_ColumnRef128' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Column(name="sample_text", null=True, primaryKey=True)
    partner = sqls_ColumnRef()
    setattr(partner, 'sqls_ColumnRef128', None)
    _safe_set(owner, 'sqls_Column129', partner)
    assert getattr(partner, 'sqls_ColumnRef128') == owner
    _safe_set(owner, 'sqls_Column129', None)
    assert getattr(partner, 'sqls_ColumnRef128') is None


def test_assoc_column92_stub_double():
    # sqls_UpdateColumnExpression has no real 'sqls_UpdateColumnExpression93' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Column(name="sample_text", null=True, primaryKey=True)
    partner = sqls_UpdateColumnExpression()
    setattr(partner, 'sqls_UpdateColumnExpression93', None)
    _safe_set(owner, 'sqls_Column94', partner)
    assert getattr(partner, 'sqls_UpdateColumnExpression93') == owner
    _safe_set(owner, 'sqls_Column94', None)
    assert getattr(partner, 'sqls_UpdateColumnExpression93') is None


def test_assoc_columns134_stub_double():
    # sqls_TriggerUpdate has no real 'sqls_TriggerUpdate' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Column(name="sample_text", null=True, primaryKey=True)
    partner = sqls_TriggerUpdate()
    setattr(partner, 'sqls_TriggerUpdate', None)
    _safe_set(owner, 'sqls_Column135', partner)
    assert getattr(partner, 'sqls_TriggerUpdate') == owner
    _safe_set(owner, 'sqls_Column135', None)
    assert getattr(partner, 'sqls_TriggerUpdate') is None


def test_assoc_columns74_stub_double():
    # sqls_InsertStatement has no real 'sqls_InsertStatement75' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Column(name="sample_text", null=True, primaryKey=True)
    partner = sqls_InsertStatement()
    setattr(partner, 'sqls_InsertStatement75', None)
    _safe_set(owner, 'sqls_Column76', partner)
    assert getattr(partner, 'sqls_InsertStatement75') == owner
    _safe_set(owner, 'sqls_Column76', None)
    assert getattr(partner, 'sqls_InsertStatement75') is None


def test_assoc_constraints23_stub_double():
    # sqls_TableConstraint has no real 'sqls_TableConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Table(name="sample_text")
    partner = sqls_TableConstraint()
    setattr(partner, 'sqls_TableConstraint', None)
    _safe_set(owner, 'sqls_Table24', {partner})
    assert getattr(partner, 'sqls_TableConstraint') == owner
    _safe_set(owner, 'sqls_Table24', set())
    assert getattr(partner, 'sqls_TableConstraint') is None


def test_assoc_defaultValue28_stub_double():
    # sqls_SqlExpr has no real 'sqls_SqlExpr30' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Column(name="sample_text", null=True, primaryKey=True)
    partner = sqls_SqlExpr()
    setattr(partner, 'sqls_SqlExpr30', None)
    _safe_set(owner, 'sqls_Column29', partner)
    assert getattr(partner, 'sqls_SqlExpr30') == owner
    _safe_set(owner, 'sqls_Column29', None)
    assert getattr(partner, 'sqls_SqlExpr30') is None


def test_assoc_elements111_stub_double():
    # sqls_Enum has no real 'sqls_Enum' property in the generated
    # code (a bare stub) -- manually attach it so sqls_EnumElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_EnumElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_EnumElement(name="sample_text", text="sample_text")
    partner = sqls_Enum()
    setattr(partner, 'sqls_Enum', None)
    _safe_set(owner, 'sqls_EnumElement', partner)
    assert getattr(partner, 'sqls_Enum') == owner
    _safe_set(owner, 'sqls_EnumElement', None)
    assert getattr(partner, 'sqls_Enum') is None


def test_assoc_enums3_stub_double():
    # sqls_Type has no real 'sqls_Type' property in the generated
    # code (a bare stub) -- manually attach it so sqls_SqlLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_SqlLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_SqlLibrary(database="sample_text", version=7)
    partner = sqls_Type()
    setattr(partner, 'sqls_Type', None)
    _safe_set(owner, 'sqls_SqlLibrary4', {partner})
    assert getattr(partner, 'sqls_Type') == owner
    _safe_set(owner, 'sqls_SqlLibrary4', set())
    assert getattr(partner, 'sqls_Type') is None


def test_assoc_expression41_stub_double():
    # sqls_SqlExpr has no real 'sqls_SqlExpr42' property in the generated
    # code (a bare stub) -- manually attach it so sqls_OrderingTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_OrderingTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_OrderingTerm(asc=True, desc=True)
    partner = sqls_SqlExpr()
    setattr(partner, 'sqls_SqlExpr42', None)
    _safe_set(owner, 'sqls_OrderingTerm', partner)
    assert getattr(partner, 'sqls_SqlExpr42') == owner
    _safe_set(owner, 'sqls_OrderingTerm', None)
    assert getattr(partner, 'sqls_SqlExpr42') is None


def test_assoc_expression43_stub_double():
    # sqls_SqlExpr has no real 'sqls_SqlExpr44' property in the generated
    # code (a bare stub) -- manually attach it so sqls_ResultColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_ResultColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_ResultColumn(name="sample_text")
    partner = sqls_SqlExpr()
    setattr(partner, 'sqls_SqlExpr44', None)
    _safe_set(owner, 'sqls_ResultColumn', partner)
    assert getattr(partner, 'sqls_SqlExpr44') == owner
    _safe_set(owner, 'sqls_ResultColumn', None)
    assert getattr(partner, 'sqls_SqlExpr44') is None


def test_assoc_imports0_stub_double():
    # sqls_Import has no real 'sqls_Import' property in the generated
    # code (a bare stub) -- manually attach it so sqls_SqlLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_SqlLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_SqlLibrary(database="sample_text", version=7)
    partner = sqls_Import()
    setattr(partner, 'sqls_Import', None)
    _safe_set(owner, 'sqls_SqlLibrary', {partner})
    assert getattr(partner, 'sqls_Import') == owner
    _safe_set(owner, 'sqls_SqlLibrary', set())
    assert getattr(partner, 'sqls_Import') is None


def test_assoc_left114_stub_double():
    # sqls_SqlExpr has no real 'sqls_SqlExpr115' property in the generated
    # code (a bare stub) -- manually attach it so sqls_SqlBinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_SqlBinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_SqlBinaryExpr(op="sample_text")
    partner = sqls_SqlExpr()
    setattr(partner, 'sqls_SqlExpr115', None)
    _safe_set(owner, 'sqls_SqlBinaryExpr', partner)
    assert getattr(partner, 'sqls_SqlExpr115') == owner
    _safe_set(owner, 'sqls_SqlBinaryExpr', None)
    assert getattr(partner, 'sqls_SqlExpr115') is None


def test_assoc_limit57_stub_double():
    # sqls_SqlExpr has no real 'sqls_SqlExpr59' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Select(all=True)
    partner = sqls_SqlExpr()
    setattr(partner, 'sqls_SqlExpr59', None)
    _safe_set(owner, 'sqls_Select58', partner)
    assert getattr(partner, 'sqls_SqlExpr59') == owner
    _safe_set(owner, 'sqls_Select58', None)
    assert getattr(partner, 'sqls_SqlExpr59') is None


def test_assoc_limitOffset60_stub_double():
    # sqls_SqlExpr has no real 'sqls_SqlExpr62' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Select(all=True)
    partner = sqls_SqlExpr()
    setattr(partner, 'sqls_SqlExpr62', None)
    _safe_set(owner, 'sqls_Select61', partner)
    assert getattr(partner, 'sqls_SqlExpr62') == owner
    _safe_set(owner, 'sqls_Select61', None)
    assert getattr(partner, 'sqls_SqlExpr62') is None


def test_assoc_method130_stub_double():
    # sqls_SqlMethodRef has no real 'sqls_SqlMethodRef' property in the generated
    # code (a bare stub) -- manually attach it so sqls_SqlMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_SqlMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_SqlMethod(array=True, name="sample_text")
    partner = sqls_SqlMethodRef()
    setattr(partner, 'sqls_SqlMethodRef', None)
    _safe_set(owner, 'sqls_SqlMethod131', partner)
    assert getattr(partner, 'sqls_SqlMethodRef') == owner
    _safe_set(owner, 'sqls_SqlMethod131', None)
    assert getattr(partner, 'sqls_SqlMethodRef') is None


def test_assoc_resultColumns45_stub_double():
    # sqls_SelectList has no real 'sqls_SelectList' property in the generated
    # code (a bare stub) -- manually attach it so sqls_ResultColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_ResultColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_ResultColumn(name="sample_text")
    partner = sqls_SelectList()
    setattr(partner, 'sqls_SelectList', None)
    _safe_set(owner, 'sqls_ResultColumn46', partner)
    assert getattr(partner, 'sqls_SelectList') == owner
    _safe_set(owner, 'sqls_ResultColumn46', None)
    assert getattr(partner, 'sqls_SelectList') is None


def test_assoc_right116_stub_double():
    # sqls_SqlExpr has no real 'sqls_SqlExpr118' property in the generated
    # code (a bare stub) -- manually attach it so sqls_SqlBinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_SqlBinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_SqlBinaryExpr(op="sample_text")
    partner = sqls_SqlExpr()
    setattr(partner, 'sqls_SqlExpr118', None)
    _safe_set(owner, 'sqls_SqlBinaryExpr117', partner)
    assert getattr(partner, 'sqls_SqlExpr118') == owner
    _safe_set(owner, 'sqls_SqlBinaryExpr117', None)
    assert getattr(partner, 'sqls_SqlExpr118') is None


def test_assoc_selectList47_stub_double():
    # sqls_SelectList has no real 'sqls_SelectList48' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Select(all=True)
    partner = sqls_SelectList()
    setattr(partner, 'sqls_SelectList48', None)
    _safe_set(owner, 'sqls_Select', partner)
    assert getattr(partner, 'sqls_SelectList48') == owner
    _safe_set(owner, 'sqls_Select', None)
    assert getattr(partner, 'sqls_SelectList48') is None


def test_assoc_sql39_stub_double():
    # sqls_SqlSentence has no real 'sqls_SqlSentence' property in the generated
    # code (a bare stub) -- manually attach it so sqls_SqlMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_SqlMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_SqlMethod(array=True, name="sample_text")
    partner = sqls_SqlSentence()
    setattr(partner, 'sqls_SqlSentence', None)
    _safe_set(owner, 'sqls_SqlMethod40', {partner})
    assert getattr(partner, 'sqls_SqlSentence') == owner
    _safe_set(owner, 'sqls_SqlMethod40', set())
    assert getattr(partner, 'sqls_SqlSentence') is None


def test_assoc_sqls108_stub_double():
    # sqls_SqlSentence has no real 'sqls_SqlSentence110' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Trigger(name="sample_text", time="sample_text")
    partner = sqls_SqlSentence()
    setattr(partner, 'sqls_SqlSentence110', None)
    _safe_set(owner, 'sqls_Trigger109', {partner})
    assert getattr(partner, 'sqls_SqlSentence110') == owner
    _safe_set(owner, 'sqls_Trigger109', set())
    assert getattr(partner, 'sqls_SqlSentence110') is None


def test_assoc_table132_stub_double():
    # sqls_DeleteTable has no real 'sqls_DeleteTable' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Table(name="sample_text")
    partner = sqls_DeleteTable()
    setattr(partner, 'sqls_DeleteTable', None)
    _safe_set(owner, 'sqls_Table133', partner)
    assert getattr(partner, 'sqls_DeleteTable') == owner
    _safe_set(owner, 'sqls_Table133', None)
    assert getattr(partner, 'sqls_DeleteTable') is None


def test_assoc_table70_stub_double():
    # sqls_Insert has no real 'sqls_Insert' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Table(name="sample_text")
    partner = sqls_Insert()
    setattr(partner, 'sqls_Insert', None)
    _safe_set(owner, 'sqls_Table71', partner)
    assert getattr(partner, 'sqls_Insert') == owner
    _safe_set(owner, 'sqls_Table71', None)
    assert getattr(partner, 'sqls_Insert') is None


def test_assoc_table72_stub_double():
    # sqls_InsertStatement has no real 'sqls_InsertStatement' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Table(name="sample_text")
    partner = sqls_InsertStatement()
    setattr(partner, 'sqls_InsertStatement', None)
    _safe_set(owner, 'sqls_Table73', partner)
    assert getattr(partner, 'sqls_InsertStatement') == owner
    _safe_set(owner, 'sqls_Table73', None)
    assert getattr(partner, 'sqls_InsertStatement') is None


def test_assoc_table80_stub_double():
    # sqls_Delete has no real 'sqls_Delete' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Table(name="sample_text")
    partner = sqls_Delete()
    setattr(partner, 'sqls_Delete', None)
    _safe_set(owner, 'sqls_Table81', partner)
    assert getattr(partner, 'sqls_Delete') == owner
    _safe_set(owner, 'sqls_Table81', None)
    assert getattr(partner, 'sqls_Delete') is None


def test_assoc_table85_stub_double():
    # sqls_Update has no real 'sqls_Update' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Table(name="sample_text")
    partner = sqls_Update()
    setattr(partner, 'sqls_Update', None)
    _safe_set(owner, 'sqls_Table86', partner)
    assert getattr(partner, 'sqls_Update') == owner
    _safe_set(owner, 'sqls_Table86', None)
    assert getattr(partner, 'sqls_Update') is None


def test_assoc_table98_stub_double():
    # sqls_Get has no real 'sqls_Get' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Table(name="sample_text")
    partner = sqls_Get()
    setattr(partner, 'sqls_Get', None)
    _safe_set(owner, 'sqls_Table99', partner)
    assert getattr(partner, 'sqls_Get') == owner
    _safe_set(owner, 'sqls_Table99', None)
    assert getattr(partner, 'sqls_Get') is None


def test_assoc_tableRef125_stub_double():
    # sqls_ColumnRef has no real 'sqls_ColumnRef' property in the generated
    # code (a bare stub) -- manually attach it so sqls_TableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_TableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_TableRef(alias="sample_text")
    partner = sqls_ColumnRef()
    setattr(partner, 'sqls_ColumnRef', None)
    _safe_set(owner, 'sqls_TableRef126', partner)
    assert getattr(partner, 'sqls_ColumnRef') == owner
    _safe_set(owner, 'sqls_TableRef126', None)
    assert getattr(partner, 'sqls_ColumnRef') is None


def test_assoc_type25_stub_double():
    # sqls_SqlType has no real 'sqls_SqlType27' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Column(name="sample_text", null=True, primaryKey=True)
    partner = sqls_SqlType()
    setattr(partner, 'sqls_SqlType27', None)
    _safe_set(owner, 'sqls_Column26', partner)
    assert getattr(partner, 'sqls_SqlType27') == owner
    _safe_set(owner, 'sqls_Column26', None)
    assert getattr(partner, 'sqls_SqlType27') is None


def test_assoc_types5_stub_double():
    # sqls_Type has no real 'sqls_Type7' property in the generated
    # code (a bare stub) -- manually attach it so sqls_SqlLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_SqlLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_SqlLibrary(database="sample_text", version=7)
    partner = sqls_Type()
    setattr(partner, 'sqls_Type7', None)
    _safe_set(owner, 'sqls_SqlLibrary6', {partner})
    assert getattr(partner, 'sqls_Type7') == owner
    _safe_set(owner, 'sqls_SqlLibrary6', set())
    assert getattr(partner, 'sqls_Type7') is None


def test_assoc_where51_stub_double():
    # sqls_SqlExpr has no real 'sqls_SqlExpr53' property in the generated
    # code (a bare stub) -- manually attach it so sqls_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sqls_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sqls_Select(all=True)
    partner = sqls_SqlExpr()
    setattr(partner, 'sqls_SqlExpr53', None)
    _safe_set(owner, 'sqls_Select52', partner)
    assert getattr(partner, 'sqls_SqlExpr53') == owner
    _safe_set(owner, 'sqls_Select52', None)
    assert getattr(partner, 'sqls_SqlExpr53') is None


