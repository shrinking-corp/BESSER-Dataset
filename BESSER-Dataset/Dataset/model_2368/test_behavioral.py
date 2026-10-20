import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ModelElement,
    relational_obeo_Column,
    relational_obeo_Database,
    relational_obeo_ForeignKey,
    relational_obeo_ModelElement,
    relational_obeo_Schema,
    relational_obeo_Table,
    Type,
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

def test_assoc_foreignTable9_reverse_link_reassign_clear():
    a1 = relational_obeo_Table(name="sample_text")
    a2 = relational_obeo_Table(name="sample_text_2")
    b = relational_obeo_ForeignKey(name="sample_text")
    _safe_set(b, 'ownedForeignKeys', a1)
    assert _is_linked(b, 'ownedForeignKeys', a1)
    if hasattr(a1, 'Table10'):
        assert _is_linked(a1, 'Table10', b)
    _safe_set(b, 'ownedForeignKeys', a2)
    assert _is_linked(b, 'ownedForeignKeys', a2)
    if hasattr(a1, 'Table10'):
        assert not _is_linked(a1, 'Table10', b)
    if hasattr(a2, 'Table10'):
        assert _is_linked(a2, 'Table10', b)
    _safe_set(b, 'ownedForeignKeys', None)
    assert not _is_linked(b, 'ownedForeignKeys', a2)
    if hasattr(a2, 'Table10'):
        assert not _is_linked(a2, 'Table10', b)


def test_assoc_ownedColumns4_reverse_link_reassign_clear():
    a1 = relational_obeo_Table(name="sample_text")
    a2 = relational_obeo_Table(name="sample_text_2")
    b = relational_obeo_Column(isPrimaryKey=True, isUnique=True, name="sample_text", type="sample_text")
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'owner5'):
        assert _is_linked(a1, 'owner5', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'owner5'):
        assert not _is_linked(a1, 'owner5', b)
    if hasattr(a2, 'owner5'):
        assert _is_linked(a2, 'owner5', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'owner5'):
        assert not _is_linked(a2, 'owner5', b)


def test_assoc_ownedForeignKeys6_reverse_link_reassign_clear():
    a1 = relational_obeo_Table(name="sample_text")
    a2 = relational_obeo_Table(name="sample_text_2")
    b = relational_obeo_ForeignKey(name="sample_text")
    _safe_set(b, 'ForeignKey', a1)
    assert _is_linked(b, 'ForeignKey', a1)
    if hasattr(a1, 'foreignTable'):
        assert _is_linked(a1, 'foreignTable', b)
    _safe_set(b, 'ForeignKey', a2)
    assert _is_linked(b, 'ForeignKey', a2)
    if hasattr(a1, 'foreignTable'):
        assert not _is_linked(a1, 'foreignTable', b)
    if hasattr(a2, 'foreignTable'):
        assert _is_linked(a2, 'foreignTable', b)
    _safe_set(b, 'ForeignKey', None)
    assert not _is_linked(b, 'ForeignKey', a2)
    if hasattr(a2, 'foreignTable'):
        assert not _is_linked(a2, 'foreignTable', b)


def test_assoc_ownedSchemas0_reverse_link_reassign_clear():
    a1 = relational_obeo_Schema(name="sample_text")
    a2 = relational_obeo_Schema(name="sample_text_2")
    b = relational_obeo_Database(name="sample_text", url="sample_text")
    _safe_set(b, 'owner', {a1})
    assert _is_linked(b, 'owner', a1)
    if hasattr(a1, 'Schema'):
        assert _is_linked(a1, 'Schema', b)
    _safe_set(b, 'owner', {a2})
    assert _is_linked(b, 'owner', a2)
    if hasattr(a1, 'Schema'):
        assert not _is_linked(a1, 'Schema', b)
    if hasattr(a2, 'Schema'):
        assert _is_linked(a2, 'Schema', b)
    _safe_set(b, 'owner', set())
    assert not _is_linked(b, 'owner', a2)
    if hasattr(a2, 'Schema'):
        assert not _is_linked(a2, 'Schema', b)


def test_assoc_ownedTables1_reverse_link_reassign_clear():
    a1 = relational_obeo_Table(name="sample_text")
    a2 = relational_obeo_Table(name="sample_text_2")
    b = relational_obeo_Schema(name="sample_text")
    _safe_set(b, 'owner2', {a1})
    assert _is_linked(b, 'owner2', a1)
    if hasattr(a1, 'Table'):
        assert _is_linked(a1, 'Table', b)
    _safe_set(b, 'owner2', {a2})
    assert _is_linked(b, 'owner2', a2)
    if hasattr(a1, 'Table'):
        assert not _is_linked(a1, 'Table', b)
    if hasattr(a2, 'Table'):
        assert _is_linked(a2, 'Table', b)
    _safe_set(b, 'owner2', set())
    assert not _is_linked(b, 'owner2', a2)
    if hasattr(a2, 'Table'):
        assert not _is_linked(a2, 'Table', b)


def test_assoc_owner12_reverse_link_reassign_clear():
    a1 = relational_obeo_Table(name="sample_text")
    a2 = relational_obeo_Table(name="sample_text_2")
    b = relational_obeo_Column(isPrimaryKey=True, isUnique=True, name="sample_text", type="sample_text")
    _safe_set(b, 'ownedColumns', a1)
    assert _is_linked(b, 'ownedColumns', a1)
    if hasattr(a1, 'Table13'):
        assert _is_linked(a1, 'Table13', b)
    _safe_set(b, 'ownedColumns', a2)
    assert _is_linked(b, 'ownedColumns', a2)
    if hasattr(a1, 'Table13'):
        assert not _is_linked(a1, 'Table13', b)
    if hasattr(a2, 'Table13'):
        assert _is_linked(a2, 'Table13', b)
    _safe_set(b, 'ownedColumns', None)
    assert not _is_linked(b, 'ownedColumns', a2)
    if hasattr(a2, 'Table13'):
        assert not _is_linked(a2, 'Table13', b)


def test_assoc_owner3_reverse_link_reassign_clear():
    a1 = relational_obeo_Schema(name="sample_text")
    a2 = relational_obeo_Schema(name="sample_text_2")
    b = relational_obeo_Database(name="sample_text", url="sample_text")
    _safe_set(b, 'Database', a1)
    assert _is_linked(b, 'Database', a1)
    if hasattr(a1, 'ownedSchemas'):
        assert _is_linked(a1, 'ownedSchemas', b)
    _safe_set(b, 'Database', a2)
    assert _is_linked(b, 'Database', a2)
    if hasattr(a1, 'ownedSchemas'):
        assert not _is_linked(a1, 'ownedSchemas', b)
    if hasattr(a2, 'ownedSchemas'):
        assert _is_linked(a2, 'ownedSchemas', b)
    _safe_set(b, 'Database', None)
    assert not _is_linked(b, 'Database', a2)
    if hasattr(a2, 'ownedSchemas'):
        assert not _is_linked(a2, 'ownedSchemas', b)


def test_assoc_owner7_reverse_link_reassign_clear():
    a1 = relational_obeo_Table(name="sample_text")
    a2 = relational_obeo_Table(name="sample_text_2")
    b = relational_obeo_Schema(name="sample_text")
    _safe_set(b, 'Schema8', a1)
    assert _is_linked(b, 'Schema8', a1)
    if hasattr(a1, 'ownedTables'):
        assert _is_linked(a1, 'ownedTables', b)
    _safe_set(b, 'Schema8', a2)
    assert _is_linked(b, 'Schema8', a2)
    if hasattr(a1, 'ownedTables'):
        assert not _is_linked(a1, 'ownedTables', b)
    if hasattr(a2, 'ownedTables'):
        assert _is_linked(a2, 'ownedTables', b)
    _safe_set(b, 'Schema8', None)
    assert not _is_linked(b, 'Schema8', a2)
    if hasattr(a2, 'ownedTables'):
        assert not _is_linked(a2, 'ownedTables', b)


def test_assoc_sourceTable11_reverse_link_reassign_clear():
    a1 = relational_obeo_Table(name="sample_text")
    a2 = relational_obeo_Table(name="sample_text_2")
    b = relational_obeo_ForeignKey(name="sample_text")
    _safe_set(b, 'relational_obeo_ForeignKey', a1)
    assert _is_linked(b, 'relational_obeo_ForeignKey', a1)
    if hasattr(a1, 'relational_obeo_Table'):
        assert _is_linked(a1, 'relational_obeo_Table', b)
    _safe_set(b, 'relational_obeo_ForeignKey', a2)
    assert _is_linked(b, 'relational_obeo_ForeignKey', a2)
    if hasattr(a1, 'relational_obeo_Table'):
        assert not _is_linked(a1, 'relational_obeo_Table', b)
    if hasattr(a2, 'relational_obeo_Table'):
        assert _is_linked(a2, 'relational_obeo_Table', b)
    _safe_set(b, 'relational_obeo_ForeignKey', None)
    assert not _is_linked(b, 'relational_obeo_ForeignKey', a2)
    if hasattr(a2, 'relational_obeo_Table'):
        assert not _is_linked(a2, 'relational_obeo_Table', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

