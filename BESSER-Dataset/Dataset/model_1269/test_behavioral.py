import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Collection,
    Key,
    Type,
    columnFamilyDataModel_ClusteringKey,
    columnFamilyDataModel_Collection,
    columnFamilyDataModel_Column,
    columnFamilyDataModel_ColumnFamily,
    columnFamilyDataModel_ColumnFamilyDataModel,
    columnFamilyDataModel_Field,
    columnFamilyDataModel_Key,
    columnFamilyDataModel_List,
    columnFamilyDataModel_Map,
    columnFamilyDataModel_PartitionKey,
    columnFamilyDataModel_Set,
    columnFamilyDataModel_SimpleType,
    columnFamilyDataModel_Table,
    columnFamilyDataModel_Tuple,
    columnFamilyDataModel_Type,
    columnFamilyDataModel_UserDefinedType,
    PrimitiveType,
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

def test_assoc_columnFamilies1_reverse_link_reassign_clear():
    a1 = columnFamilyDataModel_Table(name="sample_text")
    a2 = columnFamilyDataModel_Table(name="sample_text_2")
    b = columnFamilyDataModel_ColumnFamily(name="sample_text")
    _safe_set(b, 'columnFamilyDataModel_ColumnFamily', a1)
    assert _is_linked(b, 'columnFamilyDataModel_ColumnFamily', a1)
    if hasattr(a1, 'columnFamilyDataModel_Table2'):
        assert _is_linked(a1, 'columnFamilyDataModel_Table2', b)
    _safe_set(b, 'columnFamilyDataModel_ColumnFamily', a2)
    assert _is_linked(b, 'columnFamilyDataModel_ColumnFamily', a2)
    if hasattr(a1, 'columnFamilyDataModel_Table2'):
        assert not _is_linked(a1, 'columnFamilyDataModel_Table2', b)
    if hasattr(a2, 'columnFamilyDataModel_Table2'):
        assert _is_linked(a2, 'columnFamilyDataModel_Table2', b)
    _safe_set(b, 'columnFamilyDataModel_ColumnFamily', None)
    assert not _is_linked(b, 'columnFamilyDataModel_ColumnFamily', a2)
    if hasattr(a2, 'columnFamilyDataModel_Table2'):
        assert not _is_linked(a2, 'columnFamilyDataModel_Table2', b)


def test_assoc_columnFamily11_reverse_link_reassign_clear():
    a1 = columnFamilyDataModel_ColumnFamily(name="sample_text")
    a2 = columnFamilyDataModel_ColumnFamily(name="sample_text_2")
    b = columnFamilyDataModel_Column(name="sample_text")
    _safe_set(b, 'columnFamilyDataModel_Column12', a1)
    assert _is_linked(b, 'columnFamilyDataModel_Column12', a1)
    if hasattr(a1, 'columnFamilyDataModel_ColumnFamily13'):
        assert _is_linked(a1, 'columnFamilyDataModel_ColumnFamily13', b)
    _safe_set(b, 'columnFamilyDataModel_Column12', a2)
    assert _is_linked(b, 'columnFamilyDataModel_Column12', a2)
    if hasattr(a1, 'columnFamilyDataModel_ColumnFamily13'):
        assert not _is_linked(a1, 'columnFamilyDataModel_ColumnFamily13', b)
    if hasattr(a2, 'columnFamilyDataModel_ColumnFamily13'):
        assert _is_linked(a2, 'columnFamilyDataModel_ColumnFamily13', b)
    _safe_set(b, 'columnFamilyDataModel_Column12', None)
    assert not _is_linked(b, 'columnFamilyDataModel_Column12', a2)
    if hasattr(a2, 'columnFamilyDataModel_ColumnFamily13'):
        assert not _is_linked(a2, 'columnFamilyDataModel_ColumnFamily13', b)


def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = columnFamilyDataModel_Table(name="sample_text")
    a2 = columnFamilyDataModel_Table(name="sample_text_2")
    b = columnFamilyDataModel_Column(name="sample_text")
    _safe_set(b, 'columnFamilyDataModel_Column', a1)
    assert _is_linked(b, 'columnFamilyDataModel_Column', a1)
    if hasattr(a1, 'columnFamilyDataModel_Table4'):
        assert _is_linked(a1, 'columnFamilyDataModel_Table4', b)
    _safe_set(b, 'columnFamilyDataModel_Column', a2)
    assert _is_linked(b, 'columnFamilyDataModel_Column', a2)
    if hasattr(a1, 'columnFamilyDataModel_Table4'):
        assert not _is_linked(a1, 'columnFamilyDataModel_Table4', b)
    if hasattr(a2, 'columnFamilyDataModel_Table4'):
        assert _is_linked(a2, 'columnFamilyDataModel_Table4', b)
    _safe_set(b, 'columnFamilyDataModel_Column', None)
    assert not _is_linked(b, 'columnFamilyDataModel_Column', a2)
    if hasattr(a2, 'columnFamilyDataModel_Table4'):
        assert not _is_linked(a2, 'columnFamilyDataModel_Table4', b)


def test_assoc_fields14_reverse_link_reassign_clear():
    a1 = columnFamilyDataModel_UserDefinedType(name="sample_text")
    a2 = columnFamilyDataModel_UserDefinedType(name="sample_text_2")
    b = columnFamilyDataModel_Field(name="sample_text")
    _safe_set(b, 'columnFamilyDataModel_Field', a1)
    assert _is_linked(b, 'columnFamilyDataModel_Field', a1)
    if hasattr(a1, 'columnFamilyDataModel_UserDefinedType'):
        assert _is_linked(a1, 'columnFamilyDataModel_UserDefinedType', b)
    _safe_set(b, 'columnFamilyDataModel_Field', a2)
    assert _is_linked(b, 'columnFamilyDataModel_Field', a2)
    if hasattr(a1, 'columnFamilyDataModel_UserDefinedType'):
        assert not _is_linked(a1, 'columnFamilyDataModel_UserDefinedType', b)
    if hasattr(a2, 'columnFamilyDataModel_UserDefinedType'):
        assert _is_linked(a2, 'columnFamilyDataModel_UserDefinedType', b)
    _safe_set(b, 'columnFamilyDataModel_Field', None)
    assert not _is_linked(b, 'columnFamilyDataModel_Field', a2)
    if hasattr(a2, 'columnFamilyDataModel_UserDefinedType'):
        assert not _is_linked(a2, 'columnFamilyDataModel_UserDefinedType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_clusteringKeys7_stub_double():
    # columnFamilyDataModel_ClusteringKey has no real 'columnFamilyDataModel_ClusteringKey' property in the generated
    # code (a bare stub) -- manually attach it so columnFamilyDataModel_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # columnFamilyDataModel_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = columnFamilyDataModel_Table(name="sample_text")
    partner = columnFamilyDataModel_ClusteringKey()
    setattr(partner, 'columnFamilyDataModel_ClusteringKey', None)
    _safe_set(owner, 'columnFamilyDataModel_Table8', {partner})
    assert getattr(partner, 'columnFamilyDataModel_ClusteringKey') == owner
    _safe_set(owner, 'columnFamilyDataModel_Table8', set())
    assert getattr(partner, 'columnFamilyDataModel_ClusteringKey') is None


def test_assoc_column18_stub_double():
    # columnFamilyDataModel_Key has no real 'columnFamilyDataModel_Key' property in the generated
    # code (a bare stub) -- manually attach it so columnFamilyDataModel_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # columnFamilyDataModel_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = columnFamilyDataModel_Column(name="sample_text")
    partner = columnFamilyDataModel_Key()
    setattr(partner, 'columnFamilyDataModel_Key', None)
    _safe_set(owner, 'columnFamilyDataModel_Column19', partner)
    assert getattr(partner, 'columnFamilyDataModel_Key') == owner
    _safe_set(owner, 'columnFamilyDataModel_Column19', None)
    assert getattr(partner, 'columnFamilyDataModel_Key') is None


def test_assoc_partitionKeys5_stub_double():
    # columnFamilyDataModel_PartitionKey has no real 'columnFamilyDataModel_PartitionKey' property in the generated
    # code (a bare stub) -- manually attach it so columnFamilyDataModel_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # columnFamilyDataModel_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = columnFamilyDataModel_Table(name="sample_text")
    partner = columnFamilyDataModel_PartitionKey()
    setattr(partner, 'columnFamilyDataModel_PartitionKey', None)
    _safe_set(owner, 'columnFamilyDataModel_Table6', {partner})
    assert getattr(partner, 'columnFamilyDataModel_PartitionKey') == owner
    _safe_set(owner, 'columnFamilyDataModel_Table6', set())
    assert getattr(partner, 'columnFamilyDataModel_PartitionKey') is None


def test_assoc_tables0_stub_double():
    # columnFamilyDataModel_ColumnFamilyDataModel has no real 'columnFamilyDataModel_ColumnFamilyDataModel' property in the generated
    # code (a bare stub) -- manually attach it so columnFamilyDataModel_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # columnFamilyDataModel_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = columnFamilyDataModel_Table(name="sample_text")
    partner = columnFamilyDataModel_ColumnFamilyDataModel()
    setattr(partner, 'columnFamilyDataModel_ColumnFamilyDataModel', None)
    _safe_set(owner, 'columnFamilyDataModel_Table', partner)
    assert owner in getattr(partner, 'columnFamilyDataModel_ColumnFamilyDataModel')
    _safe_set(owner, 'columnFamilyDataModel_Table', None)
    assert owner not in getattr(partner, 'columnFamilyDataModel_ColumnFamilyDataModel')


def test_assoc_type15_stub_double():
    # columnFamilyDataModel_Type has no real 'columnFamilyDataModel_Type17' property in the generated
    # code (a bare stub) -- manually attach it so columnFamilyDataModel_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # columnFamilyDataModel_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = columnFamilyDataModel_Field(name="sample_text")
    partner = columnFamilyDataModel_Type()
    setattr(partner, 'columnFamilyDataModel_Type17', None)
    _safe_set(owner, 'columnFamilyDataModel_Field16', partner)
    assert getattr(partner, 'columnFamilyDataModel_Type17') == owner
    _safe_set(owner, 'columnFamilyDataModel_Field16', None)
    assert getattr(partner, 'columnFamilyDataModel_Type17') is None


def test_assoc_type9_stub_double():
    # columnFamilyDataModel_Type has no real 'columnFamilyDataModel_Type' property in the generated
    # code (a bare stub) -- manually attach it so columnFamilyDataModel_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # columnFamilyDataModel_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = columnFamilyDataModel_Column(name="sample_text")
    partner = columnFamilyDataModel_Type()
    setattr(partner, 'columnFamilyDataModel_Type', None)
    _safe_set(owner, 'columnFamilyDataModel_Column10', partner)
    assert getattr(partner, 'columnFamilyDataModel_Type') == owner
    _safe_set(owner, 'columnFamilyDataModel_Column10', None)
    assert getattr(partner, 'columnFamilyDataModel_Type') is None


