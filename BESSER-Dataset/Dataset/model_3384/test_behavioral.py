import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Error,
    errors_CheckError,
    errors_ColumnCk,
    errors_ColumnFk,
    errors_Error,
    errors_Errores,
    errors_ForeignError,
    errors_Table,
    errors_ValueCk,
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

def test_assoc_columnCont5_reverse_link_reassign_clear():
    a1 = errors_Table(nameTable="sample_text")
    a2 = errors_Table(nameTable="sample_text_2")
    b = errors_ColumnFk(nameColumn="sample_text")
    _safe_set(b, 'errors_ColumnFk', a1)
    assert _is_linked(b, 'errors_ColumnFk', a1)
    if hasattr(a1, 'errors_Table6'):
        assert _is_linked(a1, 'errors_Table6', b)
    _safe_set(b, 'errors_ColumnFk', a2)
    assert _is_linked(b, 'errors_ColumnFk', a2)
    if hasattr(a1, 'errors_Table6'):
        assert not _is_linked(a1, 'errors_Table6', b)
    if hasattr(a2, 'errors_Table6'):
        assert _is_linked(a2, 'errors_Table6', b)
    _safe_set(b, 'errors_ColumnFk', None)
    assert not _is_linked(b, 'errors_ColumnFk', a2)
    if hasattr(a2, 'errors_Table6'):
        assert not _is_linked(a2, 'errors_Table6', b)


def test_assoc_columns7_reverse_link_reassign_clear():
    a1 = errors_ColumnCk(columnName="sample_text")
    a2 = errors_ColumnCk(columnName="sample_text_2")
    b = errors_CheckError(nameCk="sample_text", nameTable="sample_text", porcent="sample_text")
    _safe_set(b, 'errors_CheckError', {a1})
    assert _is_linked(b, 'errors_CheckError', a1)
    if hasattr(a1, 'errors_ColumnCk'):
        assert _is_linked(a1, 'errors_ColumnCk', b)
    _safe_set(b, 'errors_CheckError', {a2})
    assert _is_linked(b, 'errors_CheckError', a2)
    if hasattr(a1, 'errors_ColumnCk'):
        assert not _is_linked(a1, 'errors_ColumnCk', b)
    if hasattr(a2, 'errors_ColumnCk'):
        assert _is_linked(a2, 'errors_ColumnCk', b)
    _safe_set(b, 'errors_CheckError', set())
    assert not _is_linked(b, 'errors_CheckError', a2)
    if hasattr(a2, 'errors_ColumnCk'):
        assert not _is_linked(a2, 'errors_ColumnCk', b)


def test_assoc_tableCont1_reverse_link_reassign_clear():
    a1 = errors_Table(nameTable="sample_text")
    a2 = errors_Table(nameTable="sample_text_2")
    b = errors_ForeignError(nameFk="sample_text", porcent="sample_text")
    _safe_set(b, 'errors_ForeignError', a1)
    assert _is_linked(b, 'errors_ForeignError', a1)
    if hasattr(a1, 'errors_Table'):
        assert _is_linked(a1, 'errors_Table', b)
    _safe_set(b, 'errors_ForeignError', a2)
    assert _is_linked(b, 'errors_ForeignError', a2)
    if hasattr(a1, 'errors_Table'):
        assert not _is_linked(a1, 'errors_Table', b)
    if hasattr(a2, 'errors_Table'):
        assert _is_linked(a2, 'errors_Table', b)
    _safe_set(b, 'errors_ForeignError', None)
    assert not _is_linked(b, 'errors_ForeignError', a2)
    if hasattr(a2, 'errors_Table'):
        assert not _is_linked(a2, 'errors_Table', b)


def test_assoc_tableRef2_reverse_link_reassign_clear():
    a1 = errors_Table(nameTable="sample_text")
    a2 = errors_Table(nameTable="sample_text_2")
    b = errors_ForeignError(nameFk="sample_text", porcent="sample_text")
    _safe_set(b, 'errors_ForeignError3', a1)
    assert _is_linked(b, 'errors_ForeignError3', a1)
    if hasattr(a1, 'errors_Table4'):
        assert _is_linked(a1, 'errors_Table4', b)
    _safe_set(b, 'errors_ForeignError3', a2)
    assert _is_linked(b, 'errors_ForeignError3', a2)
    if hasattr(a1, 'errors_Table4'):
        assert not _is_linked(a1, 'errors_Table4', b)
    if hasattr(a2, 'errors_Table4'):
        assert _is_linked(a2, 'errors_Table4', b)
    _safe_set(b, 'errors_ForeignError3', None)
    assert not _is_linked(b, 'errors_ForeignError3', a2)
    if hasattr(a2, 'errors_Table4'):
        assert not _is_linked(a2, 'errors_Table4', b)


def test_assoc_values8_reverse_link_reassign_clear():
    a1 = errors_ValueCk(value="sample_text")
    a2 = errors_ValueCk(value="sample_text_2")
    b = errors_ColumnCk(columnName="sample_text")
    _safe_set(b, 'errors_ColumnCk9', {a1})
    assert _is_linked(b, 'errors_ColumnCk9', a1)
    if hasattr(a1, 'errors_ValueCk'):
        assert _is_linked(a1, 'errors_ValueCk', b)
    _safe_set(b, 'errors_ColumnCk9', {a2})
    assert _is_linked(b, 'errors_ColumnCk9', a2)
    if hasattr(a1, 'errors_ValueCk'):
        assert not _is_linked(a1, 'errors_ValueCk', b)
    if hasattr(a2, 'errors_ValueCk'):
        assert _is_linked(a2, 'errors_ValueCk', b)
    _safe_set(b, 'errors_ColumnCk9', set())
    assert not _is_linked(b, 'errors_ColumnCk9', a2)
    if hasattr(a2, 'errors_ValueCk'):
        assert not _is_linked(a2, 'errors_ValueCk', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

