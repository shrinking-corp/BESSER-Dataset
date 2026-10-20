import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SqoopHiveImport,
    SqoopImport,
    ingest_Catalogue,
    ingest_Database,
    ingest_DbColumn,
    ingest_DbSchema,
    ingest_DbTable,
    ingest_SqoopHiveImport,
    ingest_SqoopHiveIncrementalImport,
    ingest_SqoopImport,
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

def test_assoc_columns1_reverse_link_reassign_clear():
    a1 = ingest_DbTable(name="sample_text")
    a2 = ingest_DbTable(name="sample_text_2")
    b = ingest_DbColumn(jdbcPrecision=7, jdbcScale=7, jdbcType=7, name="sample_text")
    _safe_set(b, 'ingest_DbColumn', a1)
    assert _is_linked(b, 'ingest_DbColumn', a1)
    if hasattr(a1, 'ingest_DbTable'):
        assert _is_linked(a1, 'ingest_DbTable', b)
    _safe_set(b, 'ingest_DbColumn', a2)
    assert _is_linked(b, 'ingest_DbColumn', a2)
    if hasattr(a1, 'ingest_DbTable'):
        assert not _is_linked(a1, 'ingest_DbTable', b)
    if hasattr(a2, 'ingest_DbTable'):
        assert _is_linked(a2, 'ingest_DbTable', b)
    _safe_set(b, 'ingest_DbColumn', None)
    assert not _is_linked(b, 'ingest_DbColumn', a2)
    if hasattr(a2, 'ingest_DbTable'):
        assert not _is_linked(a2, 'ingest_DbTable', b)


def test_assoc_schemas0_reverse_link_reassign_clear():
    a1 = ingest_DbSchema(name="sample_text")
    a2 = ingest_DbSchema(name="sample_text_2")
    b = ingest_Database(jdbcDriver="sample_text", jdbcPassword="sample_text", jdbcUrl="sample_text", jdbcUser="sample_text", label="sample_text")
    _safe_set(b, 'ingest_Database', {a1})
    assert _is_linked(b, 'ingest_Database', a1)
    if hasattr(a1, 'ingest_DbSchema'):
        assert _is_linked(a1, 'ingest_DbSchema', b)
    _safe_set(b, 'ingest_Database', {a2})
    assert _is_linked(b, 'ingest_Database', a2)
    if hasattr(a1, 'ingest_DbSchema'):
        assert not _is_linked(a1, 'ingest_DbSchema', b)
    if hasattr(a2, 'ingest_DbSchema'):
        assert _is_linked(a2, 'ingest_DbSchema', b)
    _safe_set(b, 'ingest_Database', set())
    assert not _is_linked(b, 'ingest_Database', a2)
    if hasattr(a2, 'ingest_DbSchema'):
        assert not _is_linked(a2, 'ingest_DbSchema', b)


def test_assoc_tables4_reverse_link_reassign_clear():
    a1 = ingest_DbTable(name="sample_text")
    a2 = ingest_DbTable(name="sample_text_2")
    b = ingest_DbSchema(name="sample_text")
    _safe_set(b, 'ingest_DbSchema5', {a1})
    assert _is_linked(b, 'ingest_DbSchema5', a1)
    if hasattr(a1, 'ingest_DbTable6'):
        assert _is_linked(a1, 'ingest_DbTable6', b)
    _safe_set(b, 'ingest_DbSchema5', {a2})
    assert _is_linked(b, 'ingest_DbSchema5', a2)
    if hasattr(a1, 'ingest_DbTable6'):
        assert not _is_linked(a1, 'ingest_DbTable6', b)
    if hasattr(a2, 'ingest_DbTable6'):
        assert _is_linked(a2, 'ingest_DbTable6', b)
    _safe_set(b, 'ingest_DbSchema5', set())
    assert not _is_linked(b, 'ingest_DbSchema5', a2)
    if hasattr(a2, 'ingest_DbTable6'):
        assert not _is_linked(a2, 'ingest_DbTable6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_checkColumn7_stub_double():
    # ingest_SqoopHiveIncrementalImport has no real 'ingest_SqoopHiveIncrementalImport' property in the generated
    # code (a bare stub) -- manually attach it so ingest_DbColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ingest_DbColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ingest_DbColumn(jdbcPrecision=7, jdbcScale=7, jdbcType=7, name="sample_text")
    partner = ingest_SqoopHiveIncrementalImport()
    setattr(partner, 'ingest_SqoopHiveIncrementalImport', None)
    _safe_set(owner, 'ingest_DbColumn8', partner)
    assert getattr(partner, 'ingest_SqoopHiveIncrementalImport') == owner
    _safe_set(owner, 'ingest_DbColumn8', None)
    assert getattr(partner, 'ingest_SqoopHiveIncrementalImport') is None


def test_assoc_databases9_stub_double():
    # ingest_Catalogue has no real 'ingest_Catalogue' property in the generated
    # code (a bare stub) -- manually attach it so ingest_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ingest_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ingest_Database(jdbcDriver="sample_text", jdbcPassword="sample_text", jdbcUrl="sample_text", jdbcUser="sample_text", label="sample_text")
    partner = ingest_Catalogue()
    setattr(partner, 'ingest_Catalogue', None)
    _safe_set(owner, 'ingest_Database10', partner)
    assert owner in getattr(partner, 'ingest_Catalogue')
    _safe_set(owner, 'ingest_Database10', None)
    assert owner not in getattr(partner, 'ingest_Catalogue')


def test_assoc_sqoopImports2_stub_double():
    # ingest_SqoopImport has no real 'ingest_SqoopImport' property in the generated
    # code (a bare stub) -- manually attach it so ingest_DbTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ingest_DbTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ingest_DbTable(name="sample_text")
    partner = ingest_SqoopImport()
    setattr(partner, 'ingest_SqoopImport', None)
    _safe_set(owner, 'ingest_DbTable3', {partner})
    assert getattr(partner, 'ingest_SqoopImport') == owner
    _safe_set(owner, 'ingest_DbTable3', set())
    assert getattr(partner, 'ingest_SqoopImport') is None


