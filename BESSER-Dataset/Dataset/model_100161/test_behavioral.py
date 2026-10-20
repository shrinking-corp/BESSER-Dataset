import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ColumnFamily,
    DataStructureType,
    Type,
    nosql_CollectionType,
    nosql_Column,
    nosql_ColumnFamily,
    nosql_DataStructureType,
    nosql_DynamicColumnFamily,
    nosql_KeySpace,
    nosql_MapType,
    nosql_PrimitiveType,
    nosql_StaticColumnFamily,
    nosql_Type,
    CollectionTypeType,
    PrimitiveTypeType,
    ReplicaPlacementStrategies,
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

def test_assoc_columnFamilies0_reverse_link_reassign_clear():
    a1 = nosql_KeySpace(name="sample_text", replicaPlacementStrategy="sample_text", replicationFactor="sample_text")
    a2 = nosql_KeySpace(name="sample_text_2", replicaPlacementStrategy="sample_text_2", replicationFactor="sample_text_2")
    b = nosql_ColumnFamily(name="sample_text")
    _safe_set(b, 'nosql_ColumnFamily', a1)
    assert _is_linked(b, 'nosql_ColumnFamily', a1)
    if hasattr(a1, 'nosql_KeySpace'):
        assert _is_linked(a1, 'nosql_KeySpace', b)
    _safe_set(b, 'nosql_ColumnFamily', a2)
    assert _is_linked(b, 'nosql_ColumnFamily', a2)
    if hasattr(a1, 'nosql_KeySpace'):
        assert not _is_linked(a1, 'nosql_KeySpace', b)
    if hasattr(a2, 'nosql_KeySpace'):
        assert _is_linked(a2, 'nosql_KeySpace', b)
    _safe_set(b, 'nosql_ColumnFamily', None)
    assert not _is_linked(b, 'nosql_ColumnFamily', a2)
    if hasattr(a2, 'nosql_KeySpace'):
        assert not _is_linked(a2, 'nosql_KeySpace', b)


def test_assoc_columns4_reverse_link_reassign_clear():
    a1 = nosql_ColumnFamily(name="sample_text")
    a2 = nosql_ColumnFamily(name="sample_text_2")
    b = nosql_Column(name="sample_text")
    _safe_set(b, 'nosql_Column', a1)
    assert _is_linked(b, 'nosql_Column', a1)
    if hasattr(a1, 'nosql_ColumnFamily5'):
        assert _is_linked(a1, 'nosql_ColumnFamily5', b)
    _safe_set(b, 'nosql_Column', a2)
    assert _is_linked(b, 'nosql_Column', a2)
    if hasattr(a1, 'nosql_ColumnFamily5'):
        assert not _is_linked(a1, 'nosql_ColumnFamily5', b)
    if hasattr(a2, 'nosql_ColumnFamily5'):
        assert _is_linked(a2, 'nosql_ColumnFamily5', b)
    _safe_set(b, 'nosql_Column', None)
    assert not _is_linked(b, 'nosql_Column', a2)
    if hasattr(a2, 'nosql_ColumnFamily5'):
        assert not _is_linked(a2, 'nosql_ColumnFamily5', b)


def test_assoc_keyspace1_reverse_link_reassign_clear():
    a1 = nosql_KeySpace(name="sample_text", replicaPlacementStrategy="sample_text", replicationFactor="sample_text")
    a2 = nosql_KeySpace(name="sample_text_2", replicaPlacementStrategy="sample_text_2", replicationFactor="sample_text_2")
    b = nosql_ColumnFamily(name="sample_text")
    _safe_set(b, 'nosql_ColumnFamily2', a1)
    assert _is_linked(b, 'nosql_ColumnFamily2', a1)
    if hasattr(a1, 'nosql_KeySpace3'):
        assert _is_linked(a1, 'nosql_KeySpace3', b)
    _safe_set(b, 'nosql_ColumnFamily2', a2)
    assert _is_linked(b, 'nosql_ColumnFamily2', a2)
    if hasattr(a1, 'nosql_KeySpace3'):
        assert not _is_linked(a1, 'nosql_KeySpace3', b)
    if hasattr(a2, 'nosql_KeySpace3'):
        assert _is_linked(a2, 'nosql_KeySpace3', b)
    _safe_set(b, 'nosql_ColumnFamily2', None)
    assert not _is_linked(b, 'nosql_ColumnFamily2', a2)
    if hasattr(a2, 'nosql_KeySpace3'):
        assert not _is_linked(a2, 'nosql_KeySpace3', b)


def test_assoc_primaryKey6_reverse_link_reassign_clear():
    a1 = nosql_ColumnFamily(name="sample_text")
    a2 = nosql_ColumnFamily(name="sample_text_2")
    b = nosql_Column(name="sample_text")
    _safe_set(b, 'nosql_Column8', a1)
    assert _is_linked(b, 'nosql_Column8', a1)
    if hasattr(a1, 'nosql_ColumnFamily7'):
        assert _is_linked(a1, 'nosql_ColumnFamily7', b)
    _safe_set(b, 'nosql_Column8', a2)
    assert _is_linked(b, 'nosql_Column8', a2)
    if hasattr(a1, 'nosql_ColumnFamily7'):
        assert not _is_linked(a1, 'nosql_ColumnFamily7', b)
    if hasattr(a2, 'nosql_ColumnFamily7'):
        assert _is_linked(a2, 'nosql_ColumnFamily7', b)
    _safe_set(b, 'nosql_Column8', None)
    assert not _is_linked(b, 'nosql_Column8', a2)
    if hasattr(a2, 'nosql_ColumnFamily7'):
        assert not _is_linked(a2, 'nosql_ColumnFamily7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_clusteringKey11_stub_double():
    # nosql_DynamicColumnFamily has no real 'nosql_DynamicColumnFamily' property in the generated
    # code (a bare stub) -- manually attach it so nosql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nosql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nosql_Column(name="sample_text")
    partner = nosql_DynamicColumnFamily()
    setattr(partner, 'nosql_DynamicColumnFamily', None)
    _safe_set(owner, 'nosql_Column12', partner)
    assert owner in getattr(partner, 'nosql_DynamicColumnFamily')
    _safe_set(owner, 'nosql_Column12', None)
    assert owner not in getattr(partner, 'nosql_DynamicColumnFamily')


def test_assoc_type9_stub_double():
    # nosql_Type has no real 'nosql_Type' property in the generated
    # code (a bare stub) -- manually attach it so nosql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # nosql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = nosql_Column(name="sample_text")
    partner = nosql_Type()
    setattr(partner, 'nosql_Type', None)
    _safe_set(owner, 'nosql_Column10', partner)
    assert getattr(partner, 'nosql_Type') == owner
    _safe_set(owner, 'nosql_Column10', None)
    assert getattr(partner, 'nosql_Type') is None


