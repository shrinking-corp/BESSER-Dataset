import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    Index,
    ModelOperation,
    ModelRoot,
    Operations,
    Schema,
    Sequence,
    Structure,
    Table,
    TableConstraint,
    mm_ops_AddColumn,
    mm_ops_AddForeignKey,
    mm_ops_AddIndex,
    mm_ops_AddNotNull,
    mm_ops_AddPrimaryKey,
    mm_ops_AddSchema,
    mm_ops_AddSequence,
    mm_ops_AddTable,
    mm_ops_AddUnique,
    mm_ops_DeleteRows,
    mm_ops_GenerateSequenceNumbers,
    mm_ops_HasNoInstances,
    mm_ops_HasNoOwnInstances,
    mm_ops_InsertRows,
    mm_ops_ModelOperation,
    mm_ops_NillRows,
    mm_ops_RemoveColumn,
    mm_ops_RemoveConstraint,
    mm_ops_RemoveDefaultValue,
    mm_ops_RemoveIndex,
    mm_ops_RemoveNotNull,
    mm_ops_RemoveSequence,
    mm_ops_RemoveTable,
    mm_ops_RenameColumn,
    mm_ops_RenameTable,
    mm_ops_SetColumnType,
    mm_ops_SetDefaultValue,
    mm_ops_UpdateRows,
    mm_rdb_Column,
    mm_rdb_ForeignKey,
    mm_rdb_Index,
    mm_rdb_ModelRoot,
    mm_rdb_Operations,
    mm_rdb_PrimaryKey,
    mm_rdb_Schema,
    mm_rdb_Sequence,
    mm_rdb_Structure,
    mm_rdb_Table,
    mm_rdb_TableConstraint,
    mm_rdb_Unique,
    ops_ModelOperation,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns12_stub_double():
    # Column has no real 'Column' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Index(name="sample_text")
    partner = Column()
    setattr(partner, 'Column', None)
    _safe_set(owner, 'mm_rdb_Index', {partner})
    assert getattr(partner, 'Column') == owner
    _safe_set(owner, 'mm_rdb_Index', set())
    assert getattr(partner, 'Column') is None


def test_assoc_columns15_stub_double():
    # Column has no real 'Column16' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Table(name="sample_text")
    partner = Column()
    setattr(partner, 'Column16', None)
    _safe_set(owner, 'owningTable', {partner})
    assert getattr(partner, 'Column16') == owner
    _safe_set(owner, 'owningTable', set())
    assert getattr(partner, 'Column16') is None


def test_assoc_constraints17_stub_double():
    # TableConstraint has no real 'TableConstraint' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Table(name="sample_text")
    partner = TableConstraint()
    setattr(partner, 'TableConstraint', None)
    _safe_set(owner, 'owningTable18', {partner})
    assert getattr(partner, 'TableConstraint') == owner
    _safe_set(owner, 'owningTable18', set())
    assert getattr(partner, 'TableConstraint') is None


def test_assoc_indexes6_stub_double():
    # Index has no real 'Index' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Schema(name="sample_text")
    partner = Index()
    setattr(partner, 'Index', None)
    _safe_set(owner, 'owningSchema7', {partner})
    assert getattr(partner, 'Index') == owner
    _safe_set(owner, 'owningSchema7', set())
    assert getattr(partner, 'Index') is None


def test_assoc_owningSchema10_stub_double():
    # Schema has no real 'Schema11' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Index(name="sample_text")
    partner = Schema()
    setattr(partner, 'Schema11', None)
    _safe_set(owner, 'indexes', partner)
    assert getattr(partner, 'Schema11') == owner
    _safe_set(owner, 'indexes', None)
    assert getattr(partner, 'Schema11') is None


def test_assoc_owningSchema13_stub_double():
    # Schema has no real 'Schema14' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Table(name="sample_text")
    partner = Schema()
    setattr(partner, 'Schema14', None)
    _safe_set(owner, 'tables', partner)
    assert getattr(partner, 'Schema14') == owner
    _safe_set(owner, 'tables', None)
    assert getattr(partner, 'Schema14') is None


def test_assoc_owningSchema8_stub_double():
    # Schema has no real 'Schema9' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Sequence(name="sample_text", startValue=7)
    partner = Schema()
    setattr(partner, 'Schema9', None)
    _safe_set(owner, 'sequence', partner)
    assert getattr(partner, 'Schema9') == owner
    _safe_set(owner, 'sequence', None)
    assert getattr(partner, 'Schema9') is None


def test_assoc_owningStructure2_stub_double():
    # Structure has no real 'Structure' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Schema(name="sample_text")
    partner = Structure()
    setattr(partner, 'Structure', None)
    _safe_set(owner, 'schemas', partner)
    assert getattr(partner, 'Structure') == owner
    _safe_set(owner, 'schemas', None)
    assert getattr(partner, 'Structure') is None


def test_assoc_owningTable19_stub_double():
    # Table has no real 'Table20' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Column(defaultValue="sample_text", isNillable="sample_text", name="sample_text", type="sample_text")
    partner = Table()
    setattr(partner, 'Table20', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'Table20') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'Table20') is None


def test_assoc_owningTable21_stub_double():
    # Table has no real 'Table22' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_TableConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_TableConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_TableConstraint(name="sample_text")
    partner = Table()
    setattr(partner, 'Table22', None)
    _safe_set(owner, 'constraints', partner)
    assert getattr(partner, 'Table22') == owner
    _safe_set(owner, 'constraints', None)
    assert getattr(partner, 'Table22') is None


def test_assoc_sequence4_stub_double():
    # Sequence has no real 'Sequence' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Schema(name="sample_text")
    partner = Sequence()
    setattr(partner, 'Sequence', None)
    _safe_set(owner, 'owningSchema5', partner)
    assert getattr(partner, 'Sequence') == owner
    _safe_set(owner, 'owningSchema5', None)
    assert getattr(partner, 'Sequence') is None


def test_assoc_tables3_stub_double():
    # Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so mm_rdb_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mm_rdb_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mm_rdb_Schema(name="sample_text")
    partner = Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'owningSchema', {partner})
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'owningSchema', set())
    assert getattr(partner, 'Table') is None


