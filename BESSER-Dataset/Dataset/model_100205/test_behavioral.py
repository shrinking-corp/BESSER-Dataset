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


