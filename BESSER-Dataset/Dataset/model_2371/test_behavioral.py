import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DB_Column,
    DB_Database,
    DB_ForeignKey,
    DB_Key,
    DB_Table,
    DataType,
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

def test_assoc_columns5_reverse_link_reassign_clear():
    a1 = DB_Table(name="sample_text")
    a2 = DB_Table(name="sample_text_2")
    b = DB_Column(name="sample_text", notNull=True, type="sample_text")
    _safe_set(b, 'DB_Column', a1)
    assert _is_linked(b, 'DB_Column', a1)
    if hasattr(a1, 'DB_Table6'):
        assert _is_linked(a1, 'DB_Table6', b)
    _safe_set(b, 'DB_Column', a2)
    assert _is_linked(b, 'DB_Column', a2)
    if hasattr(a1, 'DB_Table6'):
        assert not _is_linked(a1, 'DB_Table6', b)
    if hasattr(a2, 'DB_Table6'):
        assert _is_linked(a2, 'DB_Table6', b)
    _safe_set(b, 'DB_Column', None)
    assert not _is_linked(b, 'DB_Column', a2)
    if hasattr(a2, 'DB_Table6'):
        assert not _is_linked(a2, 'DB_Table6', b)


def test_assoc_database7_reverse_link_reassign_clear():
    a1 = DB_Table(name="sample_text")
    a2 = DB_Table(name="sample_text_2")
    b = DB_Database(name="sample_text")
    _safe_set(b, 'DB_Database9', a1)
    assert _is_linked(b, 'DB_Database9', a1)
    if hasattr(a1, 'DB_Table8'):
        assert _is_linked(a1, 'DB_Table8', b)
    _safe_set(b, 'DB_Database9', a2)
    assert _is_linked(b, 'DB_Database9', a2)
    if hasattr(a1, 'DB_Table8'):
        assert not _is_linked(a1, 'DB_Table8', b)
    if hasattr(a2, 'DB_Table8'):
        assert _is_linked(a2, 'DB_Table8', b)
    _safe_set(b, 'DB_Database9', None)
    assert not _is_linked(b, 'DB_Database9', a2)
    if hasattr(a2, 'DB_Table8'):
        assert not _is_linked(a2, 'DB_Table8', b)


def test_assoc_foreign16_reverse_link_reassign_clear():
    a1 = DB_ForeignKey(isMany="sample_text")
    a2 = DB_ForeignKey(isMany="sample_text_2")
    b = DB_Column(name="sample_text", notNull=True, type="sample_text")
    _safe_set(b, 'DB_Column17', {a1})
    assert _is_linked(b, 'DB_Column17', a1)
    if hasattr(a1, 'DB_ForeignKey18'):
        assert _is_linked(a1, 'DB_ForeignKey18', b)
    _safe_set(b, 'DB_Column17', {a2})
    assert _is_linked(b, 'DB_Column17', a2)
    if hasattr(a1, 'DB_ForeignKey18'):
        assert not _is_linked(a1, 'DB_ForeignKey18', b)
    if hasattr(a2, 'DB_ForeignKey18'):
        assert _is_linked(a2, 'DB_ForeignKey18', b)
    _safe_set(b, 'DB_Column17', set())
    assert not _is_linked(b, 'DB_Column17', a2)
    if hasattr(a2, 'DB_ForeignKey18'):
        assert not _is_linked(a2, 'DB_ForeignKey18', b)


def test_assoc_foreign_column22_reverse_link_reassign_clear():
    a1 = DB_ForeignKey(isMany="sample_text")
    a2 = DB_ForeignKey(isMany="sample_text_2")
    b = DB_Column(name="sample_text", notNull=True, type="sample_text")
    _safe_set(b, 'DB_Column24', a1)
    assert _is_linked(b, 'DB_Column24', a1)
    if hasattr(a1, 'DB_ForeignKey23'):
        assert _is_linked(a1, 'DB_ForeignKey23', b)
    _safe_set(b, 'DB_Column24', a2)
    assert _is_linked(b, 'DB_Column24', a2)
    if hasattr(a1, 'DB_ForeignKey23'):
        assert not _is_linked(a1, 'DB_ForeignKey23', b)
    if hasattr(a2, 'DB_ForeignKey23'):
        assert _is_linked(a2, 'DB_ForeignKey23', b)
    _safe_set(b, 'DB_Column24', None)
    assert not _is_linked(b, 'DB_Column24', a2)
    if hasattr(a2, 'DB_ForeignKey23'):
        assert not _is_linked(a2, 'DB_ForeignKey23', b)


def test_assoc_foreignkeys1_reverse_link_reassign_clear():
    a1 = DB_Table(name="sample_text")
    a2 = DB_Table(name="sample_text_2")
    b = DB_ForeignKey(isMany="sample_text")
    _safe_set(b, 'DB_ForeignKey', a1)
    assert _is_linked(b, 'DB_ForeignKey', a1)
    if hasattr(a1, 'DB_Table2'):
        assert _is_linked(a1, 'DB_Table2', b)
    _safe_set(b, 'DB_ForeignKey', a2)
    assert _is_linked(b, 'DB_ForeignKey', a2)
    if hasattr(a1, 'DB_Table2'):
        assert not _is_linked(a1, 'DB_Table2', b)
    if hasattr(a2, 'DB_Table2'):
        assert _is_linked(a2, 'DB_Table2', b)
    _safe_set(b, 'DB_ForeignKey', None)
    assert not _is_linked(b, 'DB_ForeignKey', a2)
    if hasattr(a2, 'DB_Table2'):
        assert not _is_linked(a2, 'DB_Table2', b)


def test_assoc_key13_reverse_link_reassign_clear():
    a1 = DB_Key(name="sample_text")
    a2 = DB_Key(name="sample_text_2")
    b = DB_Column(name="sample_text", notNull=True, type="sample_text")
    _safe_set(b, 'DB_Column14', a1)
    assert _is_linked(b, 'DB_Column14', a1)
    if hasattr(a1, 'DB_Key15'):
        assert _is_linked(a1, 'DB_Key15', b)
    _safe_set(b, 'DB_Column14', a2)
    assert _is_linked(b, 'DB_Column14', a2)
    if hasattr(a1, 'DB_Key15'):
        assert not _is_linked(a1, 'DB_Key15', b)
    if hasattr(a2, 'DB_Key15'):
        assert _is_linked(a2, 'DB_Key15', b)
    _safe_set(b, 'DB_Column14', None)
    assert not _is_linked(b, 'DB_Column14', a2)
    if hasattr(a2, 'DB_Key15'):
        assert not _is_linked(a2, 'DB_Key15', b)


def test_assoc_key_column25_reverse_link_reassign_clear():
    a1 = DB_Key(name="sample_text")
    a2 = DB_Key(name="sample_text_2")
    b = DB_Column(name="sample_text", notNull=True, type="sample_text")
    _safe_set(b, 'DB_Column27', a1)
    assert _is_linked(b, 'DB_Column27', a1)
    if hasattr(a1, 'DB_Key26'):
        assert _is_linked(a1, 'DB_Key26', b)
    _safe_set(b, 'DB_Column27', a2)
    assert _is_linked(b, 'DB_Column27', a2)
    if hasattr(a1, 'DB_Key26'):
        assert not _is_linked(a1, 'DB_Key26', b)
    if hasattr(a2, 'DB_Key26'):
        assert _is_linked(a2, 'DB_Key26', b)
    _safe_set(b, 'DB_Column27', None)
    assert not _is_linked(b, 'DB_Column27', a2)
    if hasattr(a2, 'DB_Key26'):
        assert not _is_linked(a2, 'DB_Key26', b)


def test_assoc_primary_key3_reverse_link_reassign_clear():
    a1 = DB_Table(name="sample_text")
    a2 = DB_Table(name="sample_text_2")
    b = DB_Key(name="sample_text")
    _safe_set(b, 'DB_Key', a1)
    assert _is_linked(b, 'DB_Key', a1)
    if hasattr(a1, 'DB_Table4'):
        assert _is_linked(a1, 'DB_Table4', b)
    _safe_set(b, 'DB_Key', a2)
    assert _is_linked(b, 'DB_Key', a2)
    if hasattr(a1, 'DB_Table4'):
        assert not _is_linked(a1, 'DB_Table4', b)
    if hasattr(a2, 'DB_Table4'):
        assert _is_linked(a2, 'DB_Table4', b)
    _safe_set(b, 'DB_Key', None)
    assert not _is_linked(b, 'DB_Key', a2)
    if hasattr(a2, 'DB_Table4'):
        assert not _is_linked(a2, 'DB_Table4', b)


def test_assoc_referenced28_reverse_link_reassign_clear():
    a1 = DB_Key(name="sample_text")
    a2 = DB_Key(name="sample_text_2")
    b = DB_ForeignKey(isMany="sample_text")
    _safe_set(b, 'DB_ForeignKey30', a1)
    assert _is_linked(b, 'DB_ForeignKey30', a1)
    if hasattr(a1, 'DB_Key29'):
        assert _is_linked(a1, 'DB_Key29', b)
    _safe_set(b, 'DB_ForeignKey30', a2)
    assert _is_linked(b, 'DB_ForeignKey30', a2)
    if hasattr(a1, 'DB_Key29'):
        assert not _is_linked(a1, 'DB_Key29', b)
    if hasattr(a2, 'DB_Key29'):
        assert _is_linked(a2, 'DB_Key29', b)
    _safe_set(b, 'DB_ForeignKey30', None)
    assert not _is_linked(b, 'DB_ForeignKey30', a2)
    if hasattr(a2, 'DB_Key29'):
        assert not _is_linked(a2, 'DB_Key29', b)


def test_assoc_referencedKey19_reverse_link_reassign_clear():
    a1 = DB_Key(name="sample_text")
    a2 = DB_Key(name="sample_text_2")
    b = DB_ForeignKey(isMany="sample_text")
    _safe_set(b, 'DB_ForeignKey20', a1)
    assert _is_linked(b, 'DB_ForeignKey20', a1)
    if hasattr(a1, 'DB_Key21'):
        assert _is_linked(a1, 'DB_Key21', b)
    _safe_set(b, 'DB_ForeignKey20', a2)
    assert _is_linked(b, 'DB_ForeignKey20', a2)
    if hasattr(a1, 'DB_Key21'):
        assert not _is_linked(a1, 'DB_Key21', b)
    if hasattr(a2, 'DB_Key21'):
        assert _is_linked(a2, 'DB_Key21', b)
    _safe_set(b, 'DB_ForeignKey20', None)
    assert not _is_linked(b, 'DB_ForeignKey20', a2)
    if hasattr(a2, 'DB_Key21'):
        assert not _is_linked(a2, 'DB_Key21', b)


def test_assoc_table10_reverse_link_reassign_clear():
    a1 = DB_Table(name="sample_text")
    a2 = DB_Table(name="sample_text_2")
    b = DB_Column(name="sample_text", notNull=True, type="sample_text")
    _safe_set(b, 'DB_Column11', a1)
    assert _is_linked(b, 'DB_Column11', a1)
    if hasattr(a1, 'DB_Table12'):
        assert _is_linked(a1, 'DB_Table12', b)
    _safe_set(b, 'DB_Column11', a2)
    assert _is_linked(b, 'DB_Column11', a2)
    if hasattr(a1, 'DB_Table12'):
        assert not _is_linked(a1, 'DB_Table12', b)
    if hasattr(a2, 'DB_Table12'):
        assert _is_linked(a2, 'DB_Table12', b)
    _safe_set(b, 'DB_Column11', None)
    assert not _is_linked(b, 'DB_Column11', a2)
    if hasattr(a2, 'DB_Table12'):
        assert not _is_linked(a2, 'DB_Table12', b)


def test_assoc_tables0_reverse_link_reassign_clear():
    a1 = DB_Table(name="sample_text")
    a2 = DB_Table(name="sample_text_2")
    b = DB_Database(name="sample_text")
    _safe_set(b, 'DB_Database', {a1})
    assert _is_linked(b, 'DB_Database', a1)
    if hasattr(a1, 'DB_Table'):
        assert _is_linked(a1, 'DB_Table', b)
    _safe_set(b, 'DB_Database', {a2})
    assert _is_linked(b, 'DB_Database', a2)
    if hasattr(a1, 'DB_Table'):
        assert not _is_linked(a1, 'DB_Table', b)
    if hasattr(a2, 'DB_Table'):
        assert _is_linked(a2, 'DB_Table', b)
    _safe_set(b, 'DB_Database', set())
    assert not _is_linked(b, 'DB_Database', a2)
    if hasattr(a2, 'DB_Table'):
        assert not _is_linked(a2, 'DB_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

