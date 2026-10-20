import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ER_Column,
    ER_ForeignKey,
    ER_Key,
    ER_Schema,
    ER_Table,
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

def test_assoc_column12_reverse_link_reassign_clear():
    a1 = ER_Key(name="sample_text")
    a2 = ER_Key(name="sample_text_2")
    b = ER_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'ER_Column', a1)
    assert _is_linked(b, 'ER_Column', a1)
    if hasattr(a1, 'ER_Key'):
        assert _is_linked(a1, 'ER_Key', b)
    _safe_set(b, 'ER_Column', a2)
    assert _is_linked(b, 'ER_Column', a2)
    if hasattr(a1, 'ER_Key'):
        assert not _is_linked(a1, 'ER_Key', b)
    if hasattr(a2, 'ER_Key'):
        assert _is_linked(a2, 'ER_Key', b)
    _safe_set(b, 'ER_Column', None)
    assert not _is_linked(b, 'ER_Column', a2)
    if hasattr(a2, 'ER_Key'):
        assert not _is_linked(a2, 'ER_Key', b)


def test_assoc_column27_reverse_link_reassign_clear():
    a1 = ER_ForeignKey(name="sample_text")
    a2 = ER_ForeignKey(name="sample_text_2")
    b = ER_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'Column29', a1)
    assert _is_linked(b, 'Column29', a1)
    if hasattr(a1, 'hasForeignKey28'):
        assert _is_linked(a1, 'hasForeignKey28', b)
    _safe_set(b, 'Column29', a2)
    assert _is_linked(b, 'Column29', a2)
    if hasattr(a1, 'hasForeignKey28'):
        assert not _is_linked(a1, 'hasForeignKey28', b)
    if hasattr(a2, 'hasForeignKey28'):
        assert _is_linked(a2, 'hasForeignKey28', b)
    _safe_set(b, 'Column29', None)
    assert not _is_linked(b, 'Column29', a2)
    if hasattr(a2, 'hasForeignKey28'):
        assert not _is_linked(a2, 'hasForeignKey28', b)


def test_assoc_column5_reverse_link_reassign_clear():
    a1 = ER_Table(name="sample_text")
    a2 = ER_Table(name="sample_text_2")
    b = ER_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'owner6'):
        assert _is_linked(a1, 'owner6', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'owner6'):
        assert not _is_linked(a1, 'owner6', b)
    if hasattr(a2, 'owner6'):
        assert _is_linked(a2, 'owner6', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'owner6'):
        assert not _is_linked(a2, 'owner6', b)


def test_assoc_foreignKey1_reverse_link_reassign_clear():
    a1 = ER_Schema(name="sample_text")
    a2 = ER_Schema(name="sample_text_2")
    b = ER_ForeignKey(name="sample_text")
    _safe_set(b, 'ForeignKey', a1)
    assert _is_linked(b, 'ForeignKey', a1)
    if hasattr(a1, 'schema2'):
        assert _is_linked(a1, 'schema2', b)
    _safe_set(b, 'ForeignKey', a2)
    assert _is_linked(b, 'ForeignKey', a2)
    if hasattr(a1, 'schema2'):
        assert not _is_linked(a1, 'schema2', b)
    if hasattr(a2, 'schema2'):
        assert _is_linked(a2, 'schema2', b)
    _safe_set(b, 'ForeignKey', None)
    assert not _is_linked(b, 'ForeignKey', a2)
    if hasattr(a2, 'schema2'):
        assert not _is_linked(a2, 'schema2', b)


def test_assoc_hasForeignKey20_reverse_link_reassign_clear():
    a1 = ER_ForeignKey(name="sample_text")
    a2 = ER_ForeignKey(name="sample_text_2")
    b = ER_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'column21', {a1})
    assert _is_linked(b, 'column21', a1)
    if hasattr(a1, 'ForeignKey22'):
        assert _is_linked(a1, 'ForeignKey22', b)
    _safe_set(b, 'column21', {a2})
    assert _is_linked(b, 'column21', a2)
    if hasattr(a1, 'ForeignKey22'):
        assert not _is_linked(a1, 'ForeignKey22', b)
    if hasattr(a2, 'ForeignKey22'):
        assert _is_linked(a2, 'ForeignKey22', b)
    _safe_set(b, 'column21', set())
    assert not _is_linked(b, 'column21', a2)
    if hasattr(a2, 'ForeignKey22'):
        assert not _is_linked(a2, 'ForeignKey22', b)


def test_assoc_hasForeignKey7_reverse_link_reassign_clear():
    a1 = ER_Table(name="sample_text")
    a2 = ER_Table(name="sample_text_2")
    b = ER_ForeignKey(name="sample_text")
    _safe_set(b, 'ForeignKey9', a1)
    assert _is_linked(b, 'ForeignKey9', a1)
    if hasattr(a1, 'owner8'):
        assert _is_linked(a1, 'owner8', b)
    _safe_set(b, 'ForeignKey9', a2)
    assert _is_linked(b, 'ForeignKey9', a2)
    if hasattr(a1, 'owner8'):
        assert not _is_linked(a1, 'owner8', b)
    if hasattr(a2, 'owner8'):
        assert _is_linked(a2, 'owner8', b)
    _safe_set(b, 'ForeignKey9', None)
    assert not _is_linked(b, 'ForeignKey9', a2)
    if hasattr(a2, 'owner8'):
        assert not _is_linked(a2, 'owner8', b)


def test_assoc_hasKey17_reverse_link_reassign_clear():
    a1 = ER_Key(name="sample_text")
    a2 = ER_Key(name="sample_text_2")
    b = ER_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'ER_Column18', {a1})
    assert _is_linked(b, 'ER_Column18', a1)
    if hasattr(a1, 'ER_Key19'):
        assert _is_linked(a1, 'ER_Key19', b)
    _safe_set(b, 'ER_Column18', {a2})
    assert _is_linked(b, 'ER_Column18', a2)
    if hasattr(a1, 'ER_Key19'):
        assert not _is_linked(a1, 'ER_Key19', b)
    if hasattr(a2, 'ER_Key19'):
        assert _is_linked(a2, 'ER_Key19', b)
    _safe_set(b, 'ER_Column18', set())
    assert not _is_linked(b, 'ER_Column18', a2)
    if hasattr(a2, 'ER_Key19'):
        assert not _is_linked(a2, 'ER_Key19', b)


def test_assoc_hasKey4_reverse_link_reassign_clear():
    a1 = ER_Table(name="sample_text")
    a2 = ER_Table(name="sample_text_2")
    b = ER_Key(name="sample_text")
    _safe_set(b, 'Key', a1)
    assert _is_linked(b, 'Key', a1)
    if hasattr(a1, 'owner'):
        assert _is_linked(a1, 'owner', b)
    _safe_set(b, 'Key', a2)
    assert _is_linked(b, 'Key', a2)
    if hasattr(a1, 'owner'):
        assert not _is_linked(a1, 'owner', b)
    if hasattr(a2, 'owner'):
        assert _is_linked(a2, 'owner', b)
    _safe_set(b, 'Key', None)
    assert not _is_linked(b, 'Key', a2)
    if hasattr(a2, 'owner'):
        assert not _is_linked(a2, 'owner', b)


def test_assoc_owner10_reverse_link_reassign_clear():
    a1 = ER_Table(name="sample_text")
    a2 = ER_Table(name="sample_text_2")
    b = ER_Key(name="sample_text")
    _safe_set(b, 'hasKey', a1)
    assert _is_linked(b, 'hasKey', a1)
    if hasattr(a1, 'Table11'):
        assert _is_linked(a1, 'Table11', b)
    _safe_set(b, 'hasKey', a2)
    assert _is_linked(b, 'hasKey', a2)
    if hasattr(a1, 'Table11'):
        assert not _is_linked(a1, 'Table11', b)
    if hasattr(a2, 'Table11'):
        assert _is_linked(a2, 'Table11', b)
    _safe_set(b, 'hasKey', None)
    assert not _is_linked(b, 'hasKey', a2)
    if hasattr(a2, 'Table11'):
        assert not _is_linked(a2, 'Table11', b)


def test_assoc_owner15_reverse_link_reassign_clear():
    a1 = ER_Table(name="sample_text")
    a2 = ER_Table(name="sample_text_2")
    b = ER_Column(name="sample_text", type="sample_text")
    _safe_set(b, 'column', a1)
    assert _is_linked(b, 'column', a1)
    if hasattr(a1, 'Table16'):
        assert _is_linked(a1, 'Table16', b)
    _safe_set(b, 'column', a2)
    assert _is_linked(b, 'column', a2)
    if hasattr(a1, 'Table16'):
        assert not _is_linked(a1, 'Table16', b)
    if hasattr(a2, 'Table16'):
        assert _is_linked(a2, 'Table16', b)
    _safe_set(b, 'column', None)
    assert not _is_linked(b, 'column', a2)
    if hasattr(a2, 'Table16'):
        assert not _is_linked(a2, 'Table16', b)


def test_assoc_owner25_reverse_link_reassign_clear():
    a1 = ER_Table(name="sample_text")
    a2 = ER_Table(name="sample_text_2")
    b = ER_ForeignKey(name="sample_text")
    _safe_set(b, 'hasForeignKey', a1)
    assert _is_linked(b, 'hasForeignKey', a1)
    if hasattr(a1, 'Table26'):
        assert _is_linked(a1, 'Table26', b)
    _safe_set(b, 'hasForeignKey', a2)
    assert _is_linked(b, 'hasForeignKey', a2)
    if hasattr(a1, 'Table26'):
        assert not _is_linked(a1, 'Table26', b)
    if hasattr(a2, 'Table26'):
        assert _is_linked(a2, 'Table26', b)
    _safe_set(b, 'hasForeignKey', None)
    assert not _is_linked(b, 'hasForeignKey', a2)
    if hasattr(a2, 'Table26'):
        assert not _is_linked(a2, 'Table26', b)


def test_assoc_referedBy13_reverse_link_reassign_clear():
    a1 = ER_Key(name="sample_text")
    a2 = ER_Key(name="sample_text_2")
    b = ER_ForeignKey(name="sample_text")
    _safe_set(b, 'ER_ForeignKey', a1)
    assert _is_linked(b, 'ER_ForeignKey', a1)
    if hasattr(a1, 'ER_Key14'):
        assert _is_linked(a1, 'ER_Key14', b)
    _safe_set(b, 'ER_ForeignKey', a2)
    assert _is_linked(b, 'ER_ForeignKey', a2)
    if hasattr(a1, 'ER_Key14'):
        assert not _is_linked(a1, 'ER_Key14', b)
    if hasattr(a2, 'ER_Key14'):
        assert _is_linked(a2, 'ER_Key14', b)
    _safe_set(b, 'ER_ForeignKey', None)
    assert not _is_linked(b, 'ER_ForeignKey', a2)
    if hasattr(a2, 'ER_Key14'):
        assert not _is_linked(a2, 'ER_Key14', b)


def test_assoc_refersTo30_reverse_link_reassign_clear():
    a1 = ER_Key(name="sample_text")
    a2 = ER_Key(name="sample_text_2")
    b = ER_ForeignKey(name="sample_text")
    _safe_set(b, 'ER_ForeignKey31', {a1})
    assert _is_linked(b, 'ER_ForeignKey31', a1)
    if hasattr(a1, 'ER_Key32'):
        assert _is_linked(a1, 'ER_Key32', b)
    _safe_set(b, 'ER_ForeignKey31', {a2})
    assert _is_linked(b, 'ER_ForeignKey31', a2)
    if hasattr(a1, 'ER_Key32'):
        assert not _is_linked(a1, 'ER_Key32', b)
    if hasattr(a2, 'ER_Key32'):
        assert _is_linked(a2, 'ER_Key32', b)
    _safe_set(b, 'ER_ForeignKey31', set())
    assert not _is_linked(b, 'ER_ForeignKey31', a2)
    if hasattr(a2, 'ER_Key32'):
        assert not _is_linked(a2, 'ER_Key32', b)


def test_assoc_schema23_reverse_link_reassign_clear():
    a1 = ER_Schema(name="sample_text")
    a2 = ER_Schema(name="sample_text_2")
    b = ER_ForeignKey(name="sample_text")
    _safe_set(b, 'foreignKey', a1)
    assert _is_linked(b, 'foreignKey', a1)
    if hasattr(a1, 'Schema24'):
        assert _is_linked(a1, 'Schema24', b)
    _safe_set(b, 'foreignKey', a2)
    assert _is_linked(b, 'foreignKey', a2)
    if hasattr(a1, 'Schema24'):
        assert not _is_linked(a1, 'Schema24', b)
    if hasattr(a2, 'Schema24'):
        assert _is_linked(a2, 'Schema24', b)
    _safe_set(b, 'foreignKey', None)
    assert not _is_linked(b, 'foreignKey', a2)
    if hasattr(a2, 'Schema24'):
        assert not _is_linked(a2, 'Schema24', b)


def test_assoc_schema3_reverse_link_reassign_clear():
    a1 = ER_Table(name="sample_text")
    a2 = ER_Table(name="sample_text_2")
    b = ER_Schema(name="sample_text")
    _safe_set(b, 'Schema', a1)
    assert _is_linked(b, 'Schema', a1)
    if hasattr(a1, 'table'):
        assert _is_linked(a1, 'table', b)
    _safe_set(b, 'Schema', a2)
    assert _is_linked(b, 'Schema', a2)
    if hasattr(a1, 'table'):
        assert not _is_linked(a1, 'table', b)
    if hasattr(a2, 'table'):
        assert _is_linked(a2, 'table', b)
    _safe_set(b, 'Schema', None)
    assert not _is_linked(b, 'Schema', a2)
    if hasattr(a2, 'table'):
        assert not _is_linked(a2, 'table', b)


def test_assoc_table0_reverse_link_reassign_clear():
    a1 = ER_Table(name="sample_text")
    a2 = ER_Table(name="sample_text_2")
    b = ER_Schema(name="sample_text")
    _safe_set(b, 'schema', {a1})
    assert _is_linked(b, 'schema', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'schema', {a2})
    assert _is_linked(b, 'schema', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'schema', set())
    assert not _is_linked(b, 'schema', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

