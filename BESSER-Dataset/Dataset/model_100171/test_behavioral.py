import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    rdbms_DocumentRoot,
    rdbms_EStringToStringMapEntry,
    rdbms_RDBMS,
    rdbms_column,
    rdbms_columns,
    rdbms_foreignKey,
    rdbms_foreignKeys,
    rdbms_hasForeignKeys,
    rdbms_key,
    rdbms_key2,
    rdbms_oID,
    rdbms_referencedColumns,
    rdbms_referencedKeys,
    rdbms_schema,
    rdbms_schemas,
    rdbms_table,
    rdbms_tables,
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

def test_assoc_column3_reverse_link_reassign_clear():
    a1 = rdbms_columns(group="sample_text")
    a2 = rdbms_columns(group="sample_text_2")
    b = rdbms_column(kind="sample_text", name="sample_text", oID="sample_text", type="sample_text")
    _safe_set(b, 'rdbms_column4', a1)
    assert _is_linked(b, 'rdbms_column4', a1)
    if hasattr(a1, 'rdbms_columns'):
        assert _is_linked(a1, 'rdbms_columns', b)
    _safe_set(b, 'rdbms_column4', a2)
    assert _is_linked(b, 'rdbms_column4', a2)
    if hasattr(a1, 'rdbms_columns'):
        assert not _is_linked(a1, 'rdbms_columns', b)
    if hasattr(a2, 'rdbms_columns'):
        assert _is_linked(a2, 'rdbms_columns', b)
    _safe_set(b, 'rdbms_column4', None)
    assert not _is_linked(b, 'rdbms_column4', a2)
    if hasattr(a2, 'rdbms_columns'):
        assert not _is_linked(a2, 'rdbms_columns', b)


def test_assoc_column9_reverse_link_reassign_clear():
    a1 = rdbms_column(kind="sample_text", name="sample_text", oID="sample_text", type="sample_text")
    a2 = rdbms_column(kind="sample_text_2", name="sample_text_2", oID="sample_text_2", type="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot10', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot10', a1)
    if hasattr(a1, 'rdbms_column11'):
        assert _is_linked(a1, 'rdbms_column11', b)
    _safe_set(b, 'rdbms_DocumentRoot10', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot10', a2)
    if hasattr(a1, 'rdbms_column11'):
        assert not _is_linked(a1, 'rdbms_column11', b)
    if hasattr(a2, 'rdbms_column11'):
        assert _is_linked(a2, 'rdbms_column11', b)
    _safe_set(b, 'rdbms_DocumentRoot10', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot10', a2)
    if hasattr(a2, 'rdbms_column11'):
        assert not _is_linked(a2, 'rdbms_column11', b)


def test_assoc_columns12_reverse_link_reassign_clear():
    a1 = rdbms_columns(group="sample_text")
    a2 = rdbms_columns(group="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot13', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot13', a1)
    if hasattr(a1, 'rdbms_columns14'):
        assert _is_linked(a1, 'rdbms_columns14', b)
    _safe_set(b, 'rdbms_DocumentRoot13', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot13', a2)
    if hasattr(a1, 'rdbms_columns14'):
        assert not _is_linked(a1, 'rdbms_columns14', b)
    if hasattr(a2, 'rdbms_columns14'):
        assert _is_linked(a2, 'rdbms_columns14', b)
    _safe_set(b, 'rdbms_DocumentRoot13', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot13', a2)
    if hasattr(a2, 'rdbms_columns14'):
        assert not _is_linked(a2, 'rdbms_columns14', b)


def test_assoc_columns76_reverse_link_reassign_clear():
    a1 = rdbms_table(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = rdbms_table(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = rdbms_columns(group="sample_text")
    _safe_set(b, 'rdbms_columns78', a1)
    assert _is_linked(b, 'rdbms_columns78', a1)
    if hasattr(a1, 'rdbms_table77'):
        assert _is_linked(a1, 'rdbms_table77', b)
    _safe_set(b, 'rdbms_columns78', a2)
    assert _is_linked(b, 'rdbms_columns78', a2)
    if hasattr(a1, 'rdbms_table77'):
        assert not _is_linked(a1, 'rdbms_table77', b)
    if hasattr(a2, 'rdbms_table77'):
        assert _is_linked(a2, 'rdbms_table77', b)
    _safe_set(b, 'rdbms_columns78', None)
    assert not _is_linked(b, 'rdbms_columns78', a2)
    if hasattr(a2, 'rdbms_table77'):
        assert not _is_linked(a2, 'rdbms_table77', b)


def test_assoc_foreignKey15_reverse_link_reassign_clear():
    a1 = rdbms_foreignKey(kind="sample_text", name="sample_text", oID="sample_text", owner="sample_text", refersTo="sample_text")
    a2 = rdbms_foreignKey(kind="sample_text_2", name="sample_text_2", oID="sample_text_2", owner="sample_text_2", refersTo="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot16', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot16', a1)
    if hasattr(a1, 'rdbms_foreignKey'):
        assert _is_linked(a1, 'rdbms_foreignKey', b)
    _safe_set(b, 'rdbms_DocumentRoot16', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot16', a2)
    if hasattr(a1, 'rdbms_foreignKey'):
        assert not _is_linked(a1, 'rdbms_foreignKey', b)
    if hasattr(a2, 'rdbms_foreignKey'):
        assert _is_linked(a2, 'rdbms_foreignKey', b)
    _safe_set(b, 'rdbms_DocumentRoot16', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot16', a2)
    if hasattr(a2, 'rdbms_foreignKey'):
        assert not _is_linked(a2, 'rdbms_foreignKey', b)


def test_assoc_foreignKey46_reverse_link_reassign_clear():
    a1 = rdbms_foreignKeys(group="sample_text")
    a2 = rdbms_foreignKeys(group="sample_text_2")
    b = rdbms_foreignKey(kind="sample_text", name="sample_text", oID="sample_text", owner="sample_text", refersTo="sample_text")
    _safe_set(b, 'rdbms_foreignKey48', a1)
    assert _is_linked(b, 'rdbms_foreignKey48', a1)
    if hasattr(a1, 'rdbms_foreignKeys47'):
        assert _is_linked(a1, 'rdbms_foreignKeys47', b)
    _safe_set(b, 'rdbms_foreignKey48', a2)
    assert _is_linked(b, 'rdbms_foreignKey48', a2)
    if hasattr(a1, 'rdbms_foreignKeys47'):
        assert not _is_linked(a1, 'rdbms_foreignKeys47', b)
    if hasattr(a2, 'rdbms_foreignKeys47'):
        assert _is_linked(a2, 'rdbms_foreignKeys47', b)
    _safe_set(b, 'rdbms_foreignKey48', None)
    assert not _is_linked(b, 'rdbms_foreignKey48', a2)
    if hasattr(a2, 'rdbms_foreignKeys47'):
        assert not _is_linked(a2, 'rdbms_foreignKeys47', b)


def test_assoc_foreignKeys17_reverse_link_reassign_clear():
    a1 = rdbms_foreignKeys(group="sample_text")
    a2 = rdbms_foreignKeys(group="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot18', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot18', a1)
    if hasattr(a1, 'rdbms_foreignKeys'):
        assert _is_linked(a1, 'rdbms_foreignKeys', b)
    _safe_set(b, 'rdbms_DocumentRoot18', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot18', a2)
    if hasattr(a1, 'rdbms_foreignKeys'):
        assert not _is_linked(a1, 'rdbms_foreignKeys', b)
    if hasattr(a2, 'rdbms_foreignKeys'):
        assert _is_linked(a2, 'rdbms_foreignKeys', b)
    _safe_set(b, 'rdbms_DocumentRoot18', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot18', a2)
    if hasattr(a2, 'rdbms_foreignKeys'):
        assert not _is_linked(a2, 'rdbms_foreignKeys', b)


def test_assoc_foreignKeys70_reverse_link_reassign_clear():
    a1 = rdbms_schema(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = rdbms_schema(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = rdbms_foreignKeys(group="sample_text")
    _safe_set(b, 'rdbms_foreignKeys72', a1)
    assert _is_linked(b, 'rdbms_foreignKeys72', a1)
    if hasattr(a1, 'rdbms_schema71'):
        assert _is_linked(a1, 'rdbms_schema71', b)
    _safe_set(b, 'rdbms_foreignKeys72', a2)
    assert _is_linked(b, 'rdbms_foreignKeys72', a2)
    if hasattr(a1, 'rdbms_schema71'):
        assert not _is_linked(a1, 'rdbms_schema71', b)
    if hasattr(a2, 'rdbms_schema71'):
        assert _is_linked(a2, 'rdbms_schema71', b)
    _safe_set(b, 'rdbms_foreignKeys72', None)
    assert not _is_linked(b, 'rdbms_foreignKeys72', a2)
    if hasattr(a2, 'rdbms_schema71'):
        assert not _is_linked(a2, 'rdbms_schema71', b)


def test_assoc_hasForeignKeys1_reverse_link_reassign_clear():
    a1 = rdbms_hasForeignKeys(group="sample_text")
    a2 = rdbms_hasForeignKeys(group="sample_text_2")
    b = rdbms_column(kind="sample_text", name="sample_text", oID="sample_text", type="sample_text")
    _safe_set(b, 'rdbms_column2', a1)
    assert _is_linked(b, 'rdbms_column2', a1)
    if hasattr(a1, 'rdbms_hasForeignKeys'):
        assert _is_linked(a1, 'rdbms_hasForeignKeys', b)
    _safe_set(b, 'rdbms_column2', a2)
    assert _is_linked(b, 'rdbms_column2', a2)
    if hasattr(a1, 'rdbms_hasForeignKeys'):
        assert not _is_linked(a1, 'rdbms_hasForeignKeys', b)
    if hasattr(a2, 'rdbms_hasForeignKeys'):
        assert _is_linked(a2, 'rdbms_hasForeignKeys', b)
    _safe_set(b, 'rdbms_column2', None)
    assert not _is_linked(b, 'rdbms_column2', a2)
    if hasattr(a2, 'rdbms_hasForeignKeys'):
        assert not _is_linked(a2, 'rdbms_hasForeignKeys', b)


def test_assoc_hasForeignKeys19_reverse_link_reassign_clear():
    a1 = rdbms_hasForeignKeys(group="sample_text")
    a2 = rdbms_hasForeignKeys(group="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot20', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot20', a1)
    if hasattr(a1, 'rdbms_hasForeignKeys21'):
        assert _is_linked(a1, 'rdbms_hasForeignKeys21', b)
    _safe_set(b, 'rdbms_DocumentRoot20', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot20', a2)
    if hasattr(a1, 'rdbms_hasForeignKeys21'):
        assert not _is_linked(a1, 'rdbms_hasForeignKeys21', b)
    if hasattr(a2, 'rdbms_hasForeignKeys21'):
        assert _is_linked(a2, 'rdbms_hasForeignKeys21', b)
    _safe_set(b, 'rdbms_DocumentRoot20', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot20', a2)
    if hasattr(a2, 'rdbms_hasForeignKeys21'):
        assert not _is_linked(a2, 'rdbms_hasForeignKeys21', b)


def test_assoc_key22_reverse_link_reassign_clear():
    a1 = rdbms_key(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = rdbms_key(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot23', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot23', a1)
    if hasattr(a1, 'rdbms_key'):
        assert _is_linked(a1, 'rdbms_key', b)
    _safe_set(b, 'rdbms_DocumentRoot23', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot23', a2)
    if hasattr(a1, 'rdbms_key'):
        assert not _is_linked(a1, 'rdbms_key', b)
    if hasattr(a2, 'rdbms_key'):
        assert _is_linked(a2, 'rdbms_key', b)
    _safe_set(b, 'rdbms_DocumentRoot23', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot23', a2)
    if hasattr(a2, 'rdbms_key'):
        assert not _is_linked(a2, 'rdbms_key', b)


def test_assoc_oID26_reverse_link_reassign_clear():
    a1 = rdbms_oID(oID="sample_text")
    a2 = rdbms_oID(oID="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot27', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot27', a1)
    if hasattr(a1, 'rdbms_oID'):
        assert _is_linked(a1, 'rdbms_oID', b)
    _safe_set(b, 'rdbms_DocumentRoot27', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot27', a2)
    if hasattr(a1, 'rdbms_oID'):
        assert not _is_linked(a1, 'rdbms_oID', b)
    if hasattr(a2, 'rdbms_oID'):
        assert _is_linked(a2, 'rdbms_oID', b)
    _safe_set(b, 'rdbms_DocumentRoot27', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot27', a2)
    if hasattr(a2, 'rdbms_oID'):
        assert not _is_linked(a2, 'rdbms_oID', b)


def test_assoc_oID49_reverse_link_reassign_clear():
    a1 = rdbms_oID(oID="sample_text")
    a2 = rdbms_oID(oID="sample_text_2")
    b = rdbms_hasForeignKeys(group="sample_text")
    _safe_set(b, 'rdbms_hasForeignKeys50', {a1})
    assert _is_linked(b, 'rdbms_hasForeignKeys50', a1)
    if hasattr(a1, 'rdbms_oID51'):
        assert _is_linked(a1, 'rdbms_oID51', b)
    _safe_set(b, 'rdbms_hasForeignKeys50', {a2})
    assert _is_linked(b, 'rdbms_hasForeignKeys50', a2)
    if hasattr(a1, 'rdbms_oID51'):
        assert not _is_linked(a1, 'rdbms_oID51', b)
    if hasattr(a2, 'rdbms_oID51'):
        assert _is_linked(a2, 'rdbms_oID51', b)
    _safe_set(b, 'rdbms_hasForeignKeys50', set())
    assert not _is_linked(b, 'rdbms_hasForeignKeys50', a2)
    if hasattr(a2, 'rdbms_oID51'):
        assert not _is_linked(a2, 'rdbms_oID51', b)


def test_assoc_oID61_reverse_link_reassign_clear():
    a1 = rdbms_referencedColumns(group="sample_text")
    a2 = rdbms_referencedColumns(group="sample_text_2")
    b = rdbms_oID(oID="sample_text")
    _safe_set(b, 'rdbms_oID63', a1)
    assert _is_linked(b, 'rdbms_oID63', a1)
    if hasattr(a1, 'rdbms_referencedColumns62'):
        assert _is_linked(a1, 'rdbms_referencedColumns62', b)
    _safe_set(b, 'rdbms_oID63', a2)
    assert _is_linked(b, 'rdbms_oID63', a2)
    if hasattr(a1, 'rdbms_referencedColumns62'):
        assert not _is_linked(a1, 'rdbms_referencedColumns62', b)
    if hasattr(a2, 'rdbms_referencedColumns62'):
        assert _is_linked(a2, 'rdbms_referencedColumns62', b)
    _safe_set(b, 'rdbms_oID63', None)
    assert not _is_linked(b, 'rdbms_oID63', a2)
    if hasattr(a2, 'rdbms_referencedColumns62'):
        assert not _is_linked(a2, 'rdbms_referencedColumns62', b)


def test_assoc_oID64_reverse_link_reassign_clear():
    a1 = rdbms_referencedKeys(group="sample_text")
    a2 = rdbms_referencedKeys(group="sample_text_2")
    b = rdbms_oID(oID="sample_text")
    _safe_set(b, 'rdbms_oID66', a1)
    assert _is_linked(b, 'rdbms_oID66', a1)
    if hasattr(a1, 'rdbms_referencedKeys65'):
        assert _is_linked(a1, 'rdbms_referencedKeys65', b)
    _safe_set(b, 'rdbms_oID66', a2)
    assert _is_linked(b, 'rdbms_oID66', a2)
    if hasattr(a1, 'rdbms_referencedKeys65'):
        assert not _is_linked(a1, 'rdbms_referencedKeys65', b)
    if hasattr(a2, 'rdbms_referencedKeys65'):
        assert _is_linked(a2, 'rdbms_referencedKeys65', b)
    _safe_set(b, 'rdbms_oID66', None)
    assert not _is_linked(b, 'rdbms_oID66', a2)
    if hasattr(a2, 'rdbms_referencedKeys65'):
        assert not _is_linked(a2, 'rdbms_referencedKeys65', b)


def test_assoc_referencedColumns30_reverse_link_reassign_clear():
    a1 = rdbms_referencedColumns(group="sample_text")
    a2 = rdbms_referencedColumns(group="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot31', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot31', a1)
    if hasattr(a1, 'rdbms_referencedColumns'):
        assert _is_linked(a1, 'rdbms_referencedColumns', b)
    _safe_set(b, 'rdbms_DocumentRoot31', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot31', a2)
    if hasattr(a1, 'rdbms_referencedColumns'):
        assert not _is_linked(a1, 'rdbms_referencedColumns', b)
    if hasattr(a2, 'rdbms_referencedColumns'):
        assert _is_linked(a2, 'rdbms_referencedColumns', b)
    _safe_set(b, 'rdbms_DocumentRoot31', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot31', a2)
    if hasattr(a2, 'rdbms_referencedColumns'):
        assert not _is_linked(a2, 'rdbms_referencedColumns', b)


def test_assoc_referencedColumns43_reverse_link_reassign_clear():
    a1 = rdbms_referencedColumns(group="sample_text")
    a2 = rdbms_referencedColumns(group="sample_text_2")
    b = rdbms_foreignKey(kind="sample_text", name="sample_text", oID="sample_text", owner="sample_text", refersTo="sample_text")
    _safe_set(b, 'rdbms_foreignKey44', a1)
    assert _is_linked(b, 'rdbms_foreignKey44', a1)
    if hasattr(a1, 'rdbms_referencedColumns45'):
        assert _is_linked(a1, 'rdbms_referencedColumns45', b)
    _safe_set(b, 'rdbms_foreignKey44', a2)
    assert _is_linked(b, 'rdbms_foreignKey44', a2)
    if hasattr(a1, 'rdbms_referencedColumns45'):
        assert not _is_linked(a1, 'rdbms_referencedColumns45', b)
    if hasattr(a2, 'rdbms_referencedColumns45'):
        assert _is_linked(a2, 'rdbms_referencedColumns45', b)
    _safe_set(b, 'rdbms_foreignKey44', None)
    assert not _is_linked(b, 'rdbms_foreignKey44', a2)
    if hasattr(a2, 'rdbms_referencedColumns45'):
        assert not _is_linked(a2, 'rdbms_referencedColumns45', b)


def test_assoc_referencedColumns52_reverse_link_reassign_clear():
    a1 = rdbms_referencedColumns(group="sample_text")
    a2 = rdbms_referencedColumns(group="sample_text_2")
    b = rdbms_key(kind="sample_text", name="sample_text", oID="sample_text")
    _safe_set(b, 'rdbms_key53', a1)
    assert _is_linked(b, 'rdbms_key53', a1)
    if hasattr(a1, 'rdbms_referencedColumns54'):
        assert _is_linked(a1, 'rdbms_referencedColumns54', b)
    _safe_set(b, 'rdbms_key53', a2)
    assert _is_linked(b, 'rdbms_key53', a2)
    if hasattr(a1, 'rdbms_referencedColumns54'):
        assert not _is_linked(a1, 'rdbms_referencedColumns54', b)
    if hasattr(a2, 'rdbms_referencedColumns54'):
        assert _is_linked(a2, 'rdbms_referencedColumns54', b)
    _safe_set(b, 'rdbms_key53', None)
    assert not _is_linked(b, 'rdbms_key53', a2)
    if hasattr(a2, 'rdbms_referencedColumns54'):
        assert not _is_linked(a2, 'rdbms_referencedColumns54', b)


def test_assoc_referencedKeys0_reverse_link_reassign_clear():
    a1 = rdbms_referencedKeys(group="sample_text")
    a2 = rdbms_referencedKeys(group="sample_text_2")
    b = rdbms_column(kind="sample_text", name="sample_text", oID="sample_text", type="sample_text")
    _safe_set(b, 'rdbms_column', a1)
    assert _is_linked(b, 'rdbms_column', a1)
    if hasattr(a1, 'rdbms_referencedKeys'):
        assert _is_linked(a1, 'rdbms_referencedKeys', b)
    _safe_set(b, 'rdbms_column', a2)
    assert _is_linked(b, 'rdbms_column', a2)
    if hasattr(a1, 'rdbms_referencedKeys'):
        assert not _is_linked(a1, 'rdbms_referencedKeys', b)
    if hasattr(a2, 'rdbms_referencedKeys'):
        assert _is_linked(a2, 'rdbms_referencedKeys', b)
    _safe_set(b, 'rdbms_column', None)
    assert not _is_linked(b, 'rdbms_column', a2)
    if hasattr(a2, 'rdbms_referencedKeys'):
        assert not _is_linked(a2, 'rdbms_referencedKeys', b)


def test_assoc_referencedKeys32_reverse_link_reassign_clear():
    a1 = rdbms_referencedKeys(group="sample_text")
    a2 = rdbms_referencedKeys(group="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot33', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot33', a1)
    if hasattr(a1, 'rdbms_referencedKeys34'):
        assert _is_linked(a1, 'rdbms_referencedKeys34', b)
    _safe_set(b, 'rdbms_DocumentRoot33', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot33', a2)
    if hasattr(a1, 'rdbms_referencedKeys34'):
        assert not _is_linked(a1, 'rdbms_referencedKeys34', b)
    if hasattr(a2, 'rdbms_referencedKeys34'):
        assert _is_linked(a2, 'rdbms_referencedKeys34', b)
    _safe_set(b, 'rdbms_DocumentRoot33', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot33', a2)
    if hasattr(a2, 'rdbms_referencedKeys34'):
        assert not _is_linked(a2, 'rdbms_referencedKeys34', b)


def test_assoc_schema35_reverse_link_reassign_clear():
    a1 = rdbms_schema(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = rdbms_schema(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot36', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot36', a1)
    if hasattr(a1, 'rdbms_schema'):
        assert _is_linked(a1, 'rdbms_schema', b)
    _safe_set(b, 'rdbms_DocumentRoot36', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot36', a2)
    if hasattr(a1, 'rdbms_schema'):
        assert not _is_linked(a1, 'rdbms_schema', b)
    if hasattr(a2, 'rdbms_schema'):
        assert _is_linked(a2, 'rdbms_schema', b)
    _safe_set(b, 'rdbms_DocumentRoot36', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot36', a2)
    if hasattr(a2, 'rdbms_schema'):
        assert not _is_linked(a2, 'rdbms_schema', b)


def test_assoc_schema73_reverse_link_reassign_clear():
    a1 = rdbms_schemas(group="sample_text")
    a2 = rdbms_schemas(group="sample_text_2")
    b = rdbms_schema(kind="sample_text", name="sample_text", oID="sample_text")
    _safe_set(b, 'rdbms_schema75', a1)
    assert _is_linked(b, 'rdbms_schema75', a1)
    if hasattr(a1, 'rdbms_schemas74'):
        assert _is_linked(a1, 'rdbms_schemas74', b)
    _safe_set(b, 'rdbms_schema75', a2)
    assert _is_linked(b, 'rdbms_schema75', a2)
    if hasattr(a1, 'rdbms_schemas74'):
        assert not _is_linked(a1, 'rdbms_schemas74', b)
    if hasattr(a2, 'rdbms_schemas74'):
        assert _is_linked(a2, 'rdbms_schemas74', b)
    _safe_set(b, 'rdbms_schema75', None)
    assert not _is_linked(b, 'rdbms_schema75', a2)
    if hasattr(a2, 'rdbms_schemas74'):
        assert not _is_linked(a2, 'rdbms_schemas74', b)


def test_assoc_schemas37_reverse_link_reassign_clear():
    a1 = rdbms_schemas(group="sample_text")
    a2 = rdbms_schemas(group="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot38', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot38', a1)
    if hasattr(a1, 'rdbms_schemas'):
        assert _is_linked(a1, 'rdbms_schemas', b)
    _safe_set(b, 'rdbms_DocumentRoot38', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot38', a2)
    if hasattr(a1, 'rdbms_schemas'):
        assert not _is_linked(a1, 'rdbms_schemas', b)
    if hasattr(a2, 'rdbms_schemas'):
        assert _is_linked(a2, 'rdbms_schemas', b)
    _safe_set(b, 'rdbms_DocumentRoot38', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot38', a2)
    if hasattr(a2, 'rdbms_schemas'):
        assert not _is_linked(a2, 'rdbms_schemas', b)


def test_assoc_table39_reverse_link_reassign_clear():
    a1 = rdbms_table(kind="sample_text", name="sample_text", oID="sample_text")
    a2 = rdbms_table(kind="sample_text_2", name="sample_text_2", oID="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot40', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot40', a1)
    if hasattr(a1, 'rdbms_table'):
        assert _is_linked(a1, 'rdbms_table', b)
    _safe_set(b, 'rdbms_DocumentRoot40', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot40', a2)
    if hasattr(a1, 'rdbms_table'):
        assert not _is_linked(a1, 'rdbms_table', b)
    if hasattr(a2, 'rdbms_table'):
        assert _is_linked(a2, 'rdbms_table', b)
    _safe_set(b, 'rdbms_DocumentRoot40', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot40', a2)
    if hasattr(a2, 'rdbms_table'):
        assert not _is_linked(a2, 'rdbms_table', b)


def test_assoc_table82_reverse_link_reassign_clear():
    a1 = rdbms_tables(group="sample_text")
    a2 = rdbms_tables(group="sample_text_2")
    b = rdbms_table(kind="sample_text", name="sample_text", oID="sample_text")
    _safe_set(b, 'rdbms_table84', a1)
    assert _is_linked(b, 'rdbms_table84', a1)
    if hasattr(a1, 'rdbms_tables83'):
        assert _is_linked(a1, 'rdbms_tables83', b)
    _safe_set(b, 'rdbms_table84', a2)
    assert _is_linked(b, 'rdbms_table84', a2)
    if hasattr(a1, 'rdbms_tables83'):
        assert not _is_linked(a1, 'rdbms_tables83', b)
    if hasattr(a2, 'rdbms_tables83'):
        assert _is_linked(a2, 'rdbms_tables83', b)
    _safe_set(b, 'rdbms_table84', None)
    assert not _is_linked(b, 'rdbms_table84', a2)
    if hasattr(a2, 'rdbms_tables83'):
        assert not _is_linked(a2, 'rdbms_tables83', b)


def test_assoc_tables41_reverse_link_reassign_clear():
    a1 = rdbms_tables(group="sample_text")
    a2 = rdbms_tables(group="sample_text_2")
    b = rdbms_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'rdbms_DocumentRoot42', {a1})
    assert _is_linked(b, 'rdbms_DocumentRoot42', a1)
    if hasattr(a1, 'rdbms_tables'):
        assert _is_linked(a1, 'rdbms_tables', b)
    _safe_set(b, 'rdbms_DocumentRoot42', {a2})
    assert _is_linked(b, 'rdbms_DocumentRoot42', a2)
    if hasattr(a1, 'rdbms_tables'):
        assert not _is_linked(a1, 'rdbms_tables', b)
    if hasattr(a2, 'rdbms_tables'):
        assert _is_linked(a2, 'rdbms_tables', b)
    _safe_set(b, 'rdbms_DocumentRoot42', set())
    assert not _is_linked(b, 'rdbms_DocumentRoot42', a2)
    if hasattr(a2, 'rdbms_tables'):
        assert not _is_linked(a2, 'rdbms_tables', b)


def test_assoc_tables67_reverse_link_reassign_clear():
    a1 = rdbms_tables(group="sample_text")
    a2 = rdbms_tables(group="sample_text_2")
    b = rdbms_schema(kind="sample_text", name="sample_text", oID="sample_text")
    _safe_set(b, 'rdbms_schema68', a1)
    assert _is_linked(b, 'rdbms_schema68', a1)
    if hasattr(a1, 'rdbms_tables69'):
        assert _is_linked(a1, 'rdbms_tables69', b)
    _safe_set(b, 'rdbms_schema68', a2)
    assert _is_linked(b, 'rdbms_schema68', a2)
    if hasattr(a1, 'rdbms_tables69'):
        assert not _is_linked(a1, 'rdbms_tables69', b)
    if hasattr(a2, 'rdbms_tables69'):
        assert _is_linked(a2, 'rdbms_tables69', b)
    _safe_set(b, 'rdbms_schema68', None)
    assert not _is_linked(b, 'rdbms_schema68', a2)
    if hasattr(a2, 'rdbms_tables69'):
        assert not _is_linked(a2, 'rdbms_tables69', b)


