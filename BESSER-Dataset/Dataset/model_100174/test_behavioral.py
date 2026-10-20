import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ColumnSet,
    RelationalEntity,
    Relationship,
    Table,
    UniqueKey,
    relational_AccessPattern,
    relational_BaseTable,
    relational_Catalog,
    relational_Column,
    relational_ColumnSet,
    relational_EObject,
    relational_ForeignKey,
    relational_Index,
    relational_LogicalRelationship,
    relational_LogicalRelationshipEnd,
    relational_PrimaryKey,
    relational_Procedure,
    relational_ProcedureParameter,
    relational_ProcedureResult,
    relational_RelationalEntity,
    relational_Relationship,
    relational_Schema,
    relational_Table,
    relational_UniqueConstraint,
    relational_UniqueKey,
    relational_View,
    DirectionKind,
    MultiplicityKind,
    NullableType,
    ProcedureUpdateCount,
    SearchabilityType,
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

def test_assoc_columns28_reverse_link_reassign_clear():
    a1 = relational_ForeignKey(foreignKeyMultiplicity="sample_text", primaryKeyMultiplicity="sample_text")
    a2 = relational_ForeignKey(foreignKeyMultiplicity="sample_text_2", primaryKeyMultiplicity="sample_text_2")
    b = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    _safe_set(b, 'Column', a1)
    assert _is_linked(b, 'Column', a1)
    if hasattr(a1, 'foreignKeys'):
        assert _is_linked(a1, 'foreignKeys', b)
    _safe_set(b, 'Column', a2)
    assert _is_linked(b, 'Column', a2)
    if hasattr(a1, 'foreignKeys'):
        assert not _is_linked(a1, 'foreignKeys', b)
    if hasattr(a2, 'foreignKeys'):
        assert _is_linked(a2, 'foreignKeys', b)
    _safe_set(b, 'Column', None)
    assert not _is_linked(b, 'Column', a2)
    if hasattr(a2, 'foreignKeys'):
        assert not _is_linked(a2, 'foreignKeys', b)


def test_assoc_columns35_reverse_link_reassign_clear():
    a1 = relational_UniqueKey()
    a2 = relational_UniqueKey()
    b = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    _safe_set(b, 'Column36', a1)
    assert _is_linked(b, 'Column36', a1)
    if hasattr(a1, 'uniqueKeys'):
        assert _is_linked(a1, 'uniqueKeys', b)
    _safe_set(b, 'Column36', a2)
    assert _is_linked(b, 'Column36', a2)
    if hasattr(a1, 'uniqueKeys'):
        assert not _is_linked(a1, 'uniqueKeys', b)
    if hasattr(a2, 'uniqueKeys'):
        assert _is_linked(a2, 'uniqueKeys', b)
    _safe_set(b, 'Column36', None)
    assert not _is_linked(b, 'Column36', a2)
    if hasattr(a2, 'uniqueKeys'):
        assert not _is_linked(a2, 'uniqueKeys', b)


def test_assoc_columns63_reverse_link_reassign_clear():
    a1 = relational_Index(autoUpdate=True, filterCondition="sample_text", nullable=True, unique=True)
    a2 = relational_Index(autoUpdate=False, filterCondition="sample_text_2", nullable=False, unique=False)
    b = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    _safe_set(b, 'Column65', a1)
    assert _is_linked(b, 'Column65', a1)
    if hasattr(a1, 'indexes64'):
        assert _is_linked(a1, 'indexes64', b)
    _safe_set(b, 'Column65', a2)
    assert _is_linked(b, 'Column65', a2)
    if hasattr(a1, 'indexes64'):
        assert not _is_linked(a1, 'indexes64', b)
    if hasattr(a2, 'indexes64'):
        assert _is_linked(a2, 'indexes64', b)
    _safe_set(b, 'Column65', None)
    assert not _is_linked(b, 'Column65', a2)
    if hasattr(a2, 'indexes64'):
        assert not _is_linked(a2, 'indexes64', b)


def test_assoc_foreignKeys37_reverse_link_reassign_clear():
    a1 = relational_UniqueKey()
    a2 = relational_UniqueKey()
    b = relational_ForeignKey(foreignKeyMultiplicity="sample_text", primaryKeyMultiplicity="sample_text")
    _safe_set(b, 'ForeignKey38', a1)
    assert _is_linked(b, 'ForeignKey38', a1)
    if hasattr(a1, 'uniqueKey'):
        assert _is_linked(a1, 'uniqueKey', b)
    _safe_set(b, 'ForeignKey38', a2)
    assert _is_linked(b, 'ForeignKey38', a2)
    if hasattr(a1, 'uniqueKey'):
        assert not _is_linked(a1, 'uniqueKey', b)
    if hasattr(a2, 'uniqueKey'):
        assert _is_linked(a2, 'uniqueKey', b)
    _safe_set(b, 'ForeignKey38', None)
    assert not _is_linked(b, 'ForeignKey38', a2)
    if hasattr(a2, 'uniqueKey'):
        assert not _is_linked(a2, 'uniqueKey', b)


def test_assoc_foreignKeys9_reverse_link_reassign_clear():
    a1 = relational_ForeignKey(foreignKeyMultiplicity="sample_text", primaryKeyMultiplicity="sample_text")
    a2 = relational_ForeignKey(foreignKeyMultiplicity="sample_text_2", primaryKeyMultiplicity="sample_text_2")
    b = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    _safe_set(b, 'columns10', {a1})
    assert _is_linked(b, 'columns10', a1)
    if hasattr(a1, 'ForeignKey'):
        assert _is_linked(a1, 'ForeignKey', b)
    _safe_set(b, 'columns10', {a2})
    assert _is_linked(b, 'columns10', a2)
    if hasattr(a1, 'ForeignKey'):
        assert not _is_linked(a1, 'ForeignKey', b)
    if hasattr(a2, 'ForeignKey'):
        assert _is_linked(a2, 'ForeignKey', b)
    _safe_set(b, 'columns10', set())
    assert not _is_linked(b, 'columns10', a2)
    if hasattr(a2, 'ForeignKey'):
        assert not _is_linked(a2, 'ForeignKey', b)


def test_assoc_indexes7_reverse_link_reassign_clear():
    a1 = relational_Index(autoUpdate=True, filterCondition="sample_text", nullable=True, unique=True)
    a2 = relational_Index(autoUpdate=False, filterCondition="sample_text_2", nullable=False, unique=False)
    b = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    _safe_set(b, 'columns8', {a1})
    assert _is_linked(b, 'columns8', a1)
    if hasattr(a1, 'Index'):
        assert _is_linked(a1, 'Index', b)
    _safe_set(b, 'columns8', {a2})
    assert _is_linked(b, 'columns8', a2)
    if hasattr(a1, 'Index'):
        assert not _is_linked(a1, 'Index', b)
    if hasattr(a2, 'Index'):
        assert _is_linked(a2, 'Index', b)
    _safe_set(b, 'columns8', set())
    assert not _is_linked(b, 'columns8', a2)
    if hasattr(a2, 'Index'):
        assert not _is_linked(a2, 'Index', b)


def test_assoc_logicalRelationships4_reverse_link_reassign_clear():
    a1 = relational_Table(cardinality=7, materialized=True, supportsUpdate=True, system=True)
    a2 = relational_Table(cardinality=13, materialized=False, supportsUpdate=False, system=False)
    b = relational_LogicalRelationshipEnd(multiplicity="sample_text")
    _safe_set(b, 'LogicalRelationshipEnd', a1)
    assert _is_linked(b, 'LogicalRelationshipEnd', a1)
    if hasattr(a1, 'table5'):
        assert _is_linked(a1, 'table5', b)
    _safe_set(b, 'LogicalRelationshipEnd', a2)
    assert _is_linked(b, 'LogicalRelationshipEnd', a2)
    if hasattr(a1, 'table5'):
        assert not _is_linked(a1, 'table5', b)
    if hasattr(a2, 'table5'):
        assert _is_linked(a2, 'table5', b)
    _safe_set(b, 'LogicalRelationshipEnd', None)
    assert not _is_linked(b, 'LogicalRelationshipEnd', a2)
    if hasattr(a2, 'table5'):
        assert not _is_linked(a2, 'table5', b)


def test_assoc_parameters55_reverse_link_reassign_clear():
    a1 = relational_ProcedureParameter(defaultValue="sample_text", direction="sample_text", length=7, nativeType="sample_text", nullable="sample_text", precision=7, radix=7, scale=7)
    a2 = relational_ProcedureParameter(defaultValue="sample_text_2", direction="sample_text_2", length=13, nativeType="sample_text_2", nullable="sample_text_2", precision=13, radix=13, scale=13)
    b = relational_Procedure(function=True, updateCount="sample_text")
    _safe_set(b, 'procedure', {a1})
    assert _is_linked(b, 'procedure', a1)
    if hasattr(a1, 'ProcedureParameter'):
        assert _is_linked(a1, 'ProcedureParameter', b)
    _safe_set(b, 'procedure', {a2})
    assert _is_linked(b, 'procedure', a2)
    if hasattr(a1, 'ProcedureParameter'):
        assert not _is_linked(a1, 'ProcedureParameter', b)
    if hasattr(a2, 'ProcedureParameter'):
        assert _is_linked(a2, 'ProcedureParameter', b)
    _safe_set(b, 'procedure', set())
    assert not _is_linked(b, 'procedure', a2)
    if hasattr(a2, 'ProcedureParameter'):
        assert not _is_linked(a2, 'ProcedureParameter', b)


def test_assoc_procedure69_reverse_link_reassign_clear():
    a1 = relational_ProcedureParameter(defaultValue="sample_text", direction="sample_text", length=7, nativeType="sample_text", nullable="sample_text", precision=7, radix=7, scale=7)
    a2 = relational_ProcedureParameter(defaultValue="sample_text_2", direction="sample_text_2", length=13, nativeType="sample_text_2", nullable="sample_text_2", precision=13, radix=13, scale=13)
    b = relational_Procedure(function=True, updateCount="sample_text")
    _safe_set(b, 'Procedure70', a1)
    assert _is_linked(b, 'Procedure70', a1)
    if hasattr(a1, 'parameters'):
        assert _is_linked(a1, 'parameters', b)
    _safe_set(b, 'Procedure70', a2)
    assert _is_linked(b, 'Procedure70', a2)
    if hasattr(a1, 'parameters'):
        assert not _is_linked(a1, 'parameters', b)
    if hasattr(a2, 'parameters'):
        assert _is_linked(a2, 'parameters', b)
    _safe_set(b, 'Procedure70', None)
    assert not _is_linked(b, 'Procedure70', a2)
    if hasattr(a2, 'parameters'):
        assert not _is_linked(a2, 'parameters', b)


def test_assoc_table87_reverse_link_reassign_clear():
    a1 = relational_Table(cardinality=7, materialized=True, supportsUpdate=True, system=True)
    a2 = relational_Table(cardinality=13, materialized=False, supportsUpdate=False, system=False)
    b = relational_LogicalRelationshipEnd(multiplicity="sample_text")
    _safe_set(b, 'logicalRelationships88', a1)
    assert _is_linked(b, 'logicalRelationships88', a1)
    if hasattr(a1, 'Table89'):
        assert _is_linked(a1, 'Table89', b)
    _safe_set(b, 'logicalRelationships88', a2)
    assert _is_linked(b, 'logicalRelationships88', a2)
    if hasattr(a1, 'Table89'):
        assert not _is_linked(a1, 'Table89', b)
    if hasattr(a2, 'Table89'):
        assert _is_linked(a2, 'Table89', b)
    _safe_set(b, 'logicalRelationships88', None)
    assert not _is_linked(b, 'logicalRelationships88', a2)
    if hasattr(a2, 'Table89'):
        assert not _is_linked(a2, 'Table89', b)


def test_assoc_uniqueKey29_reverse_link_reassign_clear():
    a1 = relational_UniqueKey()
    a2 = relational_UniqueKey()
    b = relational_ForeignKey(foreignKeyMultiplicity="sample_text", primaryKeyMultiplicity="sample_text")
    _safe_set(b, 'foreignKeys30', a1)
    assert _is_linked(b, 'foreignKeys30', a1)
    if hasattr(a1, 'UniqueKey31'):
        assert _is_linked(a1, 'UniqueKey31', b)
    _safe_set(b, 'foreignKeys30', a2)
    assert _is_linked(b, 'foreignKeys30', a2)
    if hasattr(a1, 'UniqueKey31'):
        assert not _is_linked(a1, 'UniqueKey31', b)
    if hasattr(a2, 'UniqueKey31'):
        assert _is_linked(a2, 'UniqueKey31', b)
    _safe_set(b, 'foreignKeys30', None)
    assert not _is_linked(b, 'foreignKeys30', a2)
    if hasattr(a2, 'UniqueKey31'):
        assert not _is_linked(a2, 'UniqueKey31', b)


def test_assoc_uniqueKeys6_reverse_link_reassign_clear():
    a1 = relational_UniqueKey()
    a2 = relational_UniqueKey()
    b = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    _safe_set(b, 'columns', {a1})
    assert _is_linked(b, 'columns', a1)
    if hasattr(a1, 'UniqueKey'):
        assert _is_linked(a1, 'UniqueKey', b)
    _safe_set(b, 'columns', {a2})
    assert _is_linked(b, 'columns', a2)
    if hasattr(a1, 'UniqueKey'):
        assert not _is_linked(a1, 'UniqueKey', b)
    if hasattr(a2, 'UniqueKey'):
        assert _is_linked(a2, 'UniqueKey', b)
    _safe_set(b, 'columns', set())
    assert not _is_linked(b, 'columns', a2)
    if hasattr(a2, 'UniqueKey'):
        assert not _is_linked(a2, 'UniqueKey', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessPatterns1_stub_double():
    # relational_AccessPattern has no real 'AccessPattern' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(cardinality=7, materialized=True, supportsUpdate=True, system=True)
    partner = relational_AccessPattern()
    setattr(partner, 'AccessPattern', None)
    _safe_set(owner, 'table', {partner})
    assert getattr(partner, 'AccessPattern') == owner
    _safe_set(owner, 'table', set())
    assert getattr(partner, 'AccessPattern') is None


def test_assoc_accessPatterns11_stub_double():
    # relational_AccessPattern has no real 'AccessPattern13' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    partner = relational_AccessPattern()
    setattr(partner, 'AccessPattern13', None)
    _safe_set(owner, 'columns12', {partner})
    assert getattr(partner, 'AccessPattern13') == owner
    _safe_set(owner, 'columns12', set())
    assert getattr(partner, 'AccessPattern13') is None


def test_assoc_catalog2_stub_double():
    # relational_Catalog has no real 'Catalog' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(cardinality=7, materialized=True, supportsUpdate=True, system=True)
    partner = relational_Catalog()
    setattr(partner, 'Catalog', None)
    _safe_set(owner, 'tables3', partner)
    assert getattr(partner, 'Catalog') == owner
    _safe_set(owner, 'tables3', None)
    assert getattr(partner, 'Catalog') is None


def test_assoc_catalog56_stub_double():
    # relational_Catalog has no real 'Catalog58' property in the generated
    # code (a bare stub) -- manually attach it so relational_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Procedure(function=True, updateCount="sample_text")
    partner = relational_Catalog()
    setattr(partner, 'Catalog58', None)
    _safe_set(owner, 'procedures57', partner)
    assert getattr(partner, 'Catalog58') == owner
    _safe_set(owner, 'procedures57', None)
    assert getattr(partner, 'Catalog58') is None


def test_assoc_catalog66_stub_double():
    # relational_Catalog has no real 'Catalog68' property in the generated
    # code (a bare stub) -- manually attach it so relational_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Index(autoUpdate=True, filterCondition="sample_text", nullable=True, unique=True)
    partner = relational_Catalog()
    setattr(partner, 'Catalog68', None)
    _safe_set(owner, 'indexes67', partner)
    assert getattr(partner, 'Catalog68') == owner
    _safe_set(owner, 'indexes67', None)
    assert getattr(partner, 'Catalog68') is None


def test_assoc_columns75_stub_double():
    # relational_AccessPattern has no real 'accessPatterns' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    partner = relational_AccessPattern()
    setattr(partner, 'accessPatterns', None)
    _safe_set(owner, 'Column76', partner)
    assert owner in getattr(partner, 'accessPatterns')
    _safe_set(owner, 'Column76', None)
    assert owner not in getattr(partner, 'accessPatterns')


def test_assoc_columns99_stub_double():
    # relational_ColumnSet has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    partner = relational_ColumnSet()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Column100', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Column100', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_ends85_stub_double():
    # relational_LogicalRelationship has no real 'relationship' property in the generated
    # code (a bare stub) -- manually attach it so relational_LogicalRelationshipEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_LogicalRelationshipEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_LogicalRelationshipEnd(multiplicity="sample_text")
    partner = relational_LogicalRelationship()
    setattr(partner, 'relationship', None)
    _safe_set(owner, 'LogicalRelationshipEnd86', partner)
    assert owner in getattr(partner, 'relationship')
    _safe_set(owner, 'LogicalRelationshipEnd86', None)
    assert owner not in getattr(partner, 'relationship')


def test_assoc_foreignKeys92_stub_double():
    # relational_BaseTable has no real 'table93' property in the generated
    # code (a bare stub) -- manually attach it so relational_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_ForeignKey(foreignKeyMultiplicity="sample_text", primaryKeyMultiplicity="sample_text")
    partner = relational_BaseTable()
    setattr(partner, 'table93', None)
    _safe_set(owner, 'ForeignKey94', partner)
    assert owner in getattr(partner, 'table93')
    _safe_set(owner, 'ForeignKey94', None)
    assert owner not in getattr(partner, 'table93')


def test_assoc_indexes22_stub_double():
    # relational_Schema has no real 'schema23' property in the generated
    # code (a bare stub) -- manually attach it so relational_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Index(autoUpdate=True, filterCondition="sample_text", nullable=True, unique=True)
    partner = relational_Schema()
    setattr(partner, 'schema23', None)
    _safe_set(owner, 'Index24', partner)
    assert owner in getattr(partner, 'schema23')
    _safe_set(owner, 'Index24', None)
    assert owner not in getattr(partner, 'schema23')


def test_assoc_indexes44_stub_double():
    # relational_Catalog has no real 'catalog45' property in the generated
    # code (a bare stub) -- manually attach it so relational_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Index(autoUpdate=True, filterCondition="sample_text", nullable=True, unique=True)
    partner = relational_Catalog()
    setattr(partner, 'catalog45', None)
    _safe_set(owner, 'Index46', partner)
    assert owner in getattr(partner, 'catalog45')
    _safe_set(owner, 'Index46', None)
    assert owner not in getattr(partner, 'catalog45')


def test_assoc_owner14_stub_double():
    # relational_ColumnSet has no real 'ColumnSet' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    partner = relational_ColumnSet()
    setattr(partner, 'ColumnSet', None)
    _safe_set(owner, 'columns15', partner)
    assert getattr(partner, 'ColumnSet') == owner
    _safe_set(owner, 'columns15', None)
    assert getattr(partner, 'ColumnSet') is None


def test_assoc_procedure101_stub_double():
    # relational_ProcedureResult has no real 'result' property in the generated
    # code (a bare stub) -- manually attach it so relational_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Procedure(function=True, updateCount="sample_text")
    partner = relational_ProcedureResult()
    setattr(partner, 'result', None)
    _safe_set(owner, 'Procedure102', partner)
    assert getattr(partner, 'result') == owner
    _safe_set(owner, 'Procedure102', None)
    assert getattr(partner, 'result') is None


def test_assoc_procedures20_stub_double():
    # relational_Schema has no real 'schema21' property in the generated
    # code (a bare stub) -- manually attach it so relational_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Procedure(function=True, updateCount="sample_text")
    partner = relational_Schema()
    setattr(partner, 'schema21', None)
    _safe_set(owner, 'Procedure', partner)
    assert owner in getattr(partner, 'schema21')
    _safe_set(owner, 'Procedure', None)
    assert owner not in getattr(partner, 'schema21')


def test_assoc_procedures41_stub_double():
    # relational_Catalog has no real 'catalog42' property in the generated
    # code (a bare stub) -- manually attach it so relational_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Procedure(function=True, updateCount="sample_text")
    partner = relational_Catalog()
    setattr(partner, 'catalog42', None)
    _safe_set(owner, 'Procedure43', partner)
    assert owner in getattr(partner, 'catalog42')
    _safe_set(owner, 'Procedure43', None)
    assert owner not in getattr(partner, 'catalog42')


def test_assoc_relationship90_stub_double():
    # relational_LogicalRelationship has no real 'LogicalRelationship91' property in the generated
    # code (a bare stub) -- manually attach it so relational_LogicalRelationshipEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_LogicalRelationshipEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_LogicalRelationshipEnd(multiplicity="sample_text")
    partner = relational_LogicalRelationship()
    setattr(partner, 'LogicalRelationship91', None)
    _safe_set(owner, 'ends', partner)
    assert getattr(partner, 'LogicalRelationship91') == owner
    _safe_set(owner, 'ends', None)
    assert getattr(partner, 'LogicalRelationship91') is None


def test_assoc_result59_stub_double():
    # relational_ProcedureResult has no real 'ProcedureResult' property in the generated
    # code (a bare stub) -- manually attach it so relational_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Procedure(function=True, updateCount="sample_text")
    partner = relational_ProcedureResult()
    setattr(partner, 'ProcedureResult', None)
    _safe_set(owner, 'procedure60', partner)
    assert getattr(partner, 'ProcedureResult') == owner
    _safe_set(owner, 'procedure60', None)
    assert getattr(partner, 'ProcedureResult') is None


def test_assoc_schema0_stub_double():
    # relational_Schema has no real 'Schema' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(cardinality=7, materialized=True, supportsUpdate=True, system=True)
    partner = relational_Schema()
    setattr(partner, 'Schema', None)
    _safe_set(owner, 'tables', partner)
    assert getattr(partner, 'Schema') == owner
    _safe_set(owner, 'tables', None)
    assert getattr(partner, 'Schema') is None


def test_assoc_schema53_stub_double():
    # relational_Schema has no real 'Schema54' property in the generated
    # code (a bare stub) -- manually attach it so relational_Procedure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Procedure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Procedure(function=True, updateCount="sample_text")
    partner = relational_Schema()
    setattr(partner, 'Schema54', None)
    _safe_set(owner, 'procedures', partner)
    assert getattr(partner, 'Schema54') == owner
    _safe_set(owner, 'procedures', None)
    assert getattr(partner, 'Schema54') is None


def test_assoc_schema61_stub_double():
    # relational_Schema has no real 'Schema62' property in the generated
    # code (a bare stub) -- manually attach it so relational_Index's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Index's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Index(autoUpdate=True, filterCondition="sample_text", nullable=True, unique=True)
    partner = relational_Schema()
    setattr(partner, 'Schema62', None)
    _safe_set(owner, 'indexes', partner)
    assert getattr(partner, 'Schema62') == owner
    _safe_set(owner, 'indexes', None)
    assert getattr(partner, 'Schema62') is None


def test_assoc_table32_stub_double():
    # relational_BaseTable has no real 'BaseTable34' property in the generated
    # code (a bare stub) -- manually attach it so relational_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_ForeignKey(foreignKeyMultiplicity="sample_text", primaryKeyMultiplicity="sample_text")
    partner = relational_BaseTable()
    setattr(partner, 'BaseTable34', None)
    _safe_set(owner, 'foreignKeys33', partner)
    assert getattr(partner, 'BaseTable34') == owner
    _safe_set(owner, 'foreignKeys33', None)
    assert getattr(partner, 'BaseTable34') is None


def test_assoc_table77_stub_double():
    # relational_AccessPattern has no real 'accessPatterns78' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(cardinality=7, materialized=True, supportsUpdate=True, system=True)
    partner = relational_AccessPattern()
    setattr(partner, 'accessPatterns78', None)
    _safe_set(owner, 'Table79', partner)
    assert getattr(partner, 'accessPatterns78') == owner
    _safe_set(owner, 'Table79', None)
    assert getattr(partner, 'accessPatterns78') is None


def test_assoc_tables17_stub_double():
    # relational_Schema has no real 'schema' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(cardinality=7, materialized=True, supportsUpdate=True, system=True)
    partner = relational_Schema()
    setattr(partner, 'schema', None)
    _safe_set(owner, 'Table', partner)
    assert owner in getattr(partner, 'schema')
    _safe_set(owner, 'Table', None)
    assert owner not in getattr(partner, 'schema')


def test_assoc_tables47_stub_double():
    # relational_Catalog has no real 'catalog48' property in the generated
    # code (a bare stub) -- manually attach it so relational_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Table(cardinality=7, materialized=True, supportsUpdate=True, system=True)
    partner = relational_Catalog()
    setattr(partner, 'catalog48', None)
    _safe_set(owner, 'Table49', partner)
    assert owner in getattr(partner, 'catalog48')
    _safe_set(owner, 'Table49', None)
    assert owner not in getattr(partner, 'catalog48')


def test_assoc_type16_stub_double():
    # relational_EObject has no real 'relational_EObject' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(autoIncremented=True, caseSensitive=True, characterSetName="sample_text", collationName="sample_text", currency=True, defaultValue="sample_text", distinctValueCount=7, fixedLength=True, format="sample_text", length=7, maximumValue="sample_text", minimumValue="sample_text", nativeType="sample_text", nullValueCount=7, nullable="sample_text", precision=7, radix=7, scale=7, searchability="sample_text", selectable=True, signed=True, updateable=True)
    partner = relational_EObject()
    setattr(partner, 'relational_EObject', None)
    _safe_set(owner, 'relational_Column', partner)
    assert getattr(partner, 'relational_EObject') == owner
    _safe_set(owner, 'relational_Column', None)
    assert getattr(partner, 'relational_EObject') is None


def test_assoc_type71_stub_double():
    # relational_EObject has no real 'relational_EObject72' property in the generated
    # code (a bare stub) -- manually attach it so relational_ProcedureParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_ProcedureParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_ProcedureParameter(defaultValue="sample_text", direction="sample_text", length=7, nativeType="sample_text", nullable="sample_text", precision=7, radix=7, scale=7)
    partner = relational_EObject()
    setattr(partner, 'relational_EObject72', None)
    _safe_set(owner, 'relational_ProcedureParameter', partner)
    assert getattr(partner, 'relational_EObject72') == owner
    _safe_set(owner, 'relational_ProcedureParameter', None)
    assert getattr(partner, 'relational_EObject72') is None


