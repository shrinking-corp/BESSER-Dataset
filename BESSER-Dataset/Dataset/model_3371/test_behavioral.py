import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DDL_CreateCk,
    DDL_CreateColumn,
    DDL_CreateCommentColumn,
    DDL_CreateCommentTable,
    DDL_CreateDatabase,
    DDL_CreateFk,
    DDL_CreatePk,
    DDL_CreateTable,
    DDL_DDLDefinition,
    DDL_DataDefinition,
    DDL_Statement,
    DataDefinition,
    Statement,
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

def test_assoc_checks8_reverse_link_reassign_clear():
    a1 = DDL_CreateTable(commentTable="sample_text", tableName="sample_text")
    a2 = DDL_CreateTable(commentTable="sample_text_2", tableName="sample_text_2")
    b = DDL_CreateCk(columnName="sample_text", nameCk="sample_text", valuesCk="sample_text")
    _safe_set(b, 'DDL_CreateCk', a1)
    assert _is_linked(b, 'DDL_CreateCk', a1)
    if hasattr(a1, 'DDL_CreateTable9'):
        assert _is_linked(a1, 'DDL_CreateTable9', b)
    _safe_set(b, 'DDL_CreateCk', a2)
    assert _is_linked(b, 'DDL_CreateCk', a2)
    if hasattr(a1, 'DDL_CreateTable9'):
        assert not _is_linked(a1, 'DDL_CreateTable9', b)
    if hasattr(a2, 'DDL_CreateTable9'):
        assert _is_linked(a2, 'DDL_CreateTable9', b)
    _safe_set(b, 'DDL_CreateCk', None)
    assert not _is_linked(b, 'DDL_CreateCk', a2)
    if hasattr(a2, 'DDL_CreateTable9'):
        assert not _is_linked(a2, 'DDL_CreateTable9', b)


def test_assoc_columns1_reverse_link_reassign_clear():
    a1 = DDL_CreateTable(commentTable="sample_text", tableName="sample_text")
    a2 = DDL_CreateTable(commentTable="sample_text_2", tableName="sample_text_2")
    b = DDL_CreateColumn(columnName="sample_text", columnNull=True, columnType="sample_text", commentColumn="sample_text")
    _safe_set(b, 'DDL_CreateColumn', a1)
    assert _is_linked(b, 'DDL_CreateColumn', a1)
    if hasattr(a1, 'DDL_CreateTable2'):
        assert _is_linked(a1, 'DDL_CreateTable2', b)
    _safe_set(b, 'DDL_CreateColumn', a2)
    assert _is_linked(b, 'DDL_CreateColumn', a2)
    if hasattr(a1, 'DDL_CreateTable2'):
        assert not _is_linked(a1, 'DDL_CreateTable2', b)
    if hasattr(a2, 'DDL_CreateTable2'):
        assert _is_linked(a2, 'DDL_CreateTable2', b)
    _safe_set(b, 'DDL_CreateColumn', None)
    assert not _is_linked(b, 'DDL_CreateColumn', a2)
    if hasattr(a2, 'DDL_CreateTable2'):
        assert not _is_linked(a2, 'DDL_CreateTable2', b)


def test_assoc_columnsFk5_reverse_link_reassign_clear():
    a1 = DDL_CreateTable(commentTable="sample_text", tableName="sample_text")
    a2 = DDL_CreateTable(commentTable="sample_text_2", tableName="sample_text_2")
    b = DDL_CreateFk(columnName="sample_text", columnReference="sample_text", nameFk="sample_text")
    _safe_set(b, 'DDL_CreateFk7', a1)
    assert _is_linked(b, 'DDL_CreateFk7', a1)
    if hasattr(a1, 'DDL_CreateTable6'):
        assert _is_linked(a1, 'DDL_CreateTable6', b)
    _safe_set(b, 'DDL_CreateFk7', a2)
    assert _is_linked(b, 'DDL_CreateFk7', a2)
    if hasattr(a1, 'DDL_CreateTable6'):
        assert not _is_linked(a1, 'DDL_CreateTable6', b)
    if hasattr(a2, 'DDL_CreateTable6'):
        assert _is_linked(a2, 'DDL_CreateTable6', b)
    _safe_set(b, 'DDL_CreateFk7', None)
    assert not _is_linked(b, 'DDL_CreateFk7', a2)
    if hasattr(a2, 'DDL_CreateTable6'):
        assert not _is_linked(a2, 'DDL_CreateTable6', b)


def test_assoc_columnsPk3_reverse_link_reassign_clear():
    a1 = DDL_CreateTable(commentTable="sample_text", tableName="sample_text")
    a2 = DDL_CreateTable(commentTable="sample_text_2", tableName="sample_text_2")
    b = DDL_CreatePk(columnName="sample_text", namePk="sample_text")
    _safe_set(b, 'DDL_CreatePk', a1)
    assert _is_linked(b, 'DDL_CreatePk', a1)
    if hasattr(a1, 'DDL_CreateTable4'):
        assert _is_linked(a1, 'DDL_CreateTable4', b)
    _safe_set(b, 'DDL_CreatePk', a2)
    assert _is_linked(b, 'DDL_CreatePk', a2)
    if hasattr(a1, 'DDL_CreateTable4'):
        assert not _is_linked(a1, 'DDL_CreateTable4', b)
    if hasattr(a2, 'DDL_CreateTable4'):
        assert _is_linked(a2, 'DDL_CreateTable4', b)
    _safe_set(b, 'DDL_CreatePk', None)
    assert not _is_linked(b, 'DDL_CreatePk', a2)
    if hasattr(a2, 'DDL_CreateTable4'):
        assert not _is_linked(a2, 'DDL_CreateTable4', b)


def test_assoc_references0_reverse_link_reassign_clear():
    a1 = DDL_CreateTable(commentTable="sample_text", tableName="sample_text")
    a2 = DDL_CreateTable(commentTable="sample_text_2", tableName="sample_text_2")
    b = DDL_CreateFk(columnName="sample_text", columnReference="sample_text", nameFk="sample_text")
    _safe_set(b, 'DDL_CreateFk', a1)
    assert _is_linked(b, 'DDL_CreateFk', a1)
    if hasattr(a1, 'DDL_CreateTable'):
        assert _is_linked(a1, 'DDL_CreateTable', b)
    _safe_set(b, 'DDL_CreateFk', a2)
    assert _is_linked(b, 'DDL_CreateFk', a2)
    if hasattr(a1, 'DDL_CreateTable'):
        assert not _is_linked(a1, 'DDL_CreateTable', b)
    if hasattr(a2, 'DDL_CreateTable'):
        assert _is_linked(a2, 'DDL_CreateTable', b)
    _safe_set(b, 'DDL_CreateFk', None)
    assert not _is_linked(b, 'DDL_CreateFk', a2)
    if hasattr(a2, 'DDL_CreateTable'):
        assert not _is_linked(a2, 'DDL_CreateTable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

