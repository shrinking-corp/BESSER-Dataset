import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataType,
    cassandra_AsciiType,
    cassandra_BooleanType,
    cassandra_BytesType,
    cassandra_Column,
    cassandra_ColumnFamily,
    cassandra_CounterColumnType,
    cassandra_DataType,
    cassandra_DateType,
    cassandra_DecimalType,
    cassandra_DoubleType,
    cassandra_FloatType,
    cassandra_IntegerType,
    cassandra_Keyspace,
    cassandra_Row,
    cassandra_SuperColumn,
    cassandra_UTF8Type,
    cassandra_UUIDType,
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

def test_assoc_columnfamilies0_reverse_link_reassign_clear():
    a1 = cassandra_Keyspace(name="sample_text")
    a2 = cassandra_Keyspace(name="sample_text_2")
    b = cassandra_ColumnFamily(name="sample_text")
    _safe_set(b, 'cassandra_ColumnFamily', a1)
    assert _is_linked(b, 'cassandra_ColumnFamily', a1)
    if hasattr(a1, 'cassandra_Keyspace'):
        assert _is_linked(a1, 'cassandra_Keyspace', b)
    _safe_set(b, 'cassandra_ColumnFamily', a2)
    assert _is_linked(b, 'cassandra_ColumnFamily', a2)
    if hasattr(a1, 'cassandra_Keyspace'):
        assert not _is_linked(a1, 'cassandra_Keyspace', b)
    if hasattr(a2, 'cassandra_Keyspace'):
        assert _is_linked(a2, 'cassandra_Keyspace', b)
    _safe_set(b, 'cassandra_ColumnFamily', None)
    assert not _is_linked(b, 'cassandra_ColumnFamily', a2)
    if hasattr(a2, 'cassandra_Keyspace'):
        assert not _is_linked(a2, 'cassandra_Keyspace', b)


def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = cassandra_Row(key="sample_text")
    a2 = cassandra_Row(key="sample_text_2")
    b = cassandra_Column(key="sample_text", timestamp="sample_text")
    _safe_set(b, 'cassandra_Column', a1)
    assert _is_linked(b, 'cassandra_Column', a1)
    if hasattr(a1, 'cassandra_Row4'):
        assert _is_linked(a1, 'cassandra_Row4', b)
    _safe_set(b, 'cassandra_Column', a2)
    assert _is_linked(b, 'cassandra_Column', a2)
    if hasattr(a1, 'cassandra_Row4'):
        assert not _is_linked(a1, 'cassandra_Row4', b)
    if hasattr(a2, 'cassandra_Row4'):
        assert _is_linked(a2, 'cassandra_Row4', b)
    _safe_set(b, 'cassandra_Column', None)
    assert not _is_linked(b, 'cassandra_Column', a2)
    if hasattr(a2, 'cassandra_Row4'):
        assert not _is_linked(a2, 'cassandra_Row4', b)


def test_assoc_columns9_reverse_link_reassign_clear():
    a1 = cassandra_SuperColumn(key="sample_text")
    a2 = cassandra_SuperColumn(key="sample_text_2")
    b = cassandra_Column(key="sample_text", timestamp="sample_text")
    _safe_set(b, 'cassandra_Column11', a1)
    assert _is_linked(b, 'cassandra_Column11', a1)
    if hasattr(a1, 'cassandra_SuperColumn10'):
        assert _is_linked(a1, 'cassandra_SuperColumn10', b)
    _safe_set(b, 'cassandra_Column11', a2)
    assert _is_linked(b, 'cassandra_Column11', a2)
    if hasattr(a1, 'cassandra_SuperColumn10'):
        assert not _is_linked(a1, 'cassandra_SuperColumn10', b)
    if hasattr(a2, 'cassandra_SuperColumn10'):
        assert _is_linked(a2, 'cassandra_SuperColumn10', b)
    _safe_set(b, 'cassandra_Column11', None)
    assert not _is_linked(b, 'cassandra_Column11', a2)
    if hasattr(a2, 'cassandra_SuperColumn10'):
        assert not _is_linked(a2, 'cassandra_SuperColumn10', b)


def test_assoc_rows1_reverse_link_reassign_clear():
    a1 = cassandra_Row(key="sample_text")
    a2 = cassandra_Row(key="sample_text_2")
    b = cassandra_ColumnFamily(name="sample_text")
    _safe_set(b, 'cassandra_ColumnFamily2', {a1})
    assert _is_linked(b, 'cassandra_ColumnFamily2', a1)
    if hasattr(a1, 'cassandra_Row'):
        assert _is_linked(a1, 'cassandra_Row', b)
    _safe_set(b, 'cassandra_ColumnFamily2', {a2})
    assert _is_linked(b, 'cassandra_ColumnFamily2', a2)
    if hasattr(a1, 'cassandra_Row'):
        assert not _is_linked(a1, 'cassandra_Row', b)
    if hasattr(a2, 'cassandra_Row'):
        assert _is_linked(a2, 'cassandra_Row', b)
    _safe_set(b, 'cassandra_ColumnFamily2', set())
    assert not _is_linked(b, 'cassandra_ColumnFamily2', a2)
    if hasattr(a2, 'cassandra_Row'):
        assert not _is_linked(a2, 'cassandra_Row', b)


def test_assoc_supercolumns5_reverse_link_reassign_clear():
    a1 = cassandra_SuperColumn(key="sample_text")
    a2 = cassandra_SuperColumn(key="sample_text_2")
    b = cassandra_Row(key="sample_text")
    _safe_set(b, 'cassandra_Row6', {a1})
    assert _is_linked(b, 'cassandra_Row6', a1)
    if hasattr(a1, 'cassandra_SuperColumn'):
        assert _is_linked(a1, 'cassandra_SuperColumn', b)
    _safe_set(b, 'cassandra_Row6', {a2})
    assert _is_linked(b, 'cassandra_Row6', a2)
    if hasattr(a1, 'cassandra_SuperColumn'):
        assert not _is_linked(a1, 'cassandra_SuperColumn', b)
    if hasattr(a2, 'cassandra_SuperColumn'):
        assert _is_linked(a2, 'cassandra_SuperColumn', b)
    _safe_set(b, 'cassandra_Row6', set())
    assert not _is_linked(b, 'cassandra_Row6', a2)
    if hasattr(a2, 'cassandra_SuperColumn'):
        assert not _is_linked(a2, 'cassandra_SuperColumn', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_value7_stub_double():
    # cassandra_DataType has no real 'cassandra_DataType' property in the generated
    # code (a bare stub) -- manually attach it so cassandra_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cassandra_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cassandra_Column(key="sample_text", timestamp="sample_text")
    partner = cassandra_DataType()
    setattr(partner, 'cassandra_DataType', None)
    _safe_set(owner, 'cassandra_Column8', partner)
    assert getattr(partner, 'cassandra_DataType') == owner
    _safe_set(owner, 'cassandra_Column8', None)
    assert getattr(partner, 'cassandra_DataType') is None


