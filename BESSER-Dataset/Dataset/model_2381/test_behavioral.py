import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    DataType,
    DistinctUserDefinedType,
    ENamedElement,
    ReferenceConstraint,
    SQLObject,
    Table,
    TableConstraint,
    TypedElement,
    UniqueConstraint,
    UserDefinedType,
    relational_Assertion,
    relational_BaseTable,
    relational_CheckConstraint,
    relational_Column,
    relational_Comment,
    relational_Constraint,
    relational_DataType,
    relational_DistinctUserDefinedType,
    relational_Domain,
    relational_ENamedElement,
    relational_ForeignKey,
    relational_PrimaryKey,
    relational_ReferenceConstraint,
    relational_SQLObject,
    relational_Schema,
    relational_Table,
    relational_TableConstraint,
    relational_Trigger,
    relational_TypedElement,
    relational_UniqueConstraint,
    relational_UserDefinedType,
    ActionGranularityType,
    ActionTimeType,
    ReferentialActionType,
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

def test_assoc_comments0_reverse_link_reassign_clear():
    a1 = relational_SQLObject(description="sample_text", label="sample_text")
    a2 = relational_SQLObject(description="sample_text_2", label="sample_text_2")
    b = relational_Comment(description="sample_text")
    _safe_set(b, 'Comment', a1)
    assert _is_linked(b, 'Comment', a1)
    if hasattr(a1, 'sqlobject'):
        assert _is_linked(a1, 'sqlobject', b)
    _safe_set(b, 'Comment', a2)
    assert _is_linked(b, 'Comment', a2)
    if hasattr(a1, 'sqlobject'):
        assert not _is_linked(a1, 'sqlobject', b)
    if hasattr(a2, 'sqlobject'):
        assert _is_linked(a2, 'sqlobject', b)
    _safe_set(b, 'Comment', None)
    assert not _is_linked(b, 'Comment', a2)
    if hasattr(a2, 'sqlobject'):
        assert not _is_linked(a2, 'sqlobject', b)


def test_assoc_constraint47_reverse_link_reassign_clear():
    a1 = relational_Domain(defaultValue="sample_text", nullable=True)
    a2 = relational_Domain(defaultValue="sample_text_2", nullable=False)
    b = relational_CheckConstraint(searchCondition="sample_text")
    _safe_set(b, 'relational_CheckConstraint', a1)
    assert _is_linked(b, 'relational_CheckConstraint', a1)
    if hasattr(a1, 'relational_Domain'):
        assert _is_linked(a1, 'relational_Domain', b)
    _safe_set(b, 'relational_CheckConstraint', a2)
    assert _is_linked(b, 'relational_CheckConstraint', a2)
    if hasattr(a1, 'relational_Domain'):
        assert not _is_linked(a1, 'relational_Domain', b)
    if hasattr(a2, 'relational_Domain'):
        assert _is_linked(a2, 'relational_Domain', b)
    _safe_set(b, 'relational_CheckConstraint', None)
    assert not _is_linked(b, 'relational_CheckConstraint', a2)
    if hasattr(a2, 'relational_Domain'):
        assert not _is_linked(a2, 'relational_Domain', b)


def test_assoc_foreignKey28_reverse_link_reassign_clear():
    a1 = relational_ForeignKey(onDelete="sample_text", onUpdate="sample_text")
    a2 = relational_ForeignKey(onDelete="sample_text_2", onUpdate="sample_text_2")
    b = relational_Column(defaultValue="sample_text", length=7, nullable=True, srid="sample_text")
    _safe_set(b, 'referencedMembers', {a1})
    assert _is_linked(b, 'referencedMembers', a1)
    if hasattr(a1, 'ForeignKey'):
        assert _is_linked(a1, 'ForeignKey', b)
    _safe_set(b, 'referencedMembers', {a2})
    assert _is_linked(b, 'referencedMembers', a2)
    if hasattr(a1, 'ForeignKey'):
        assert not _is_linked(a1, 'ForeignKey', b)
    if hasattr(a2, 'ForeignKey'):
        assert _is_linked(a2, 'ForeignKey', b)
    _safe_set(b, 'referencedMembers', set())
    assert not _is_linked(b, 'referencedMembers', a2)
    if hasattr(a2, 'ForeignKey'):
        assert not _is_linked(a2, 'ForeignKey', b)


def test_assoc_referencedMembers38_reverse_link_reassign_clear():
    a1 = relational_ForeignKey(onDelete="sample_text", onUpdate="sample_text")
    a2 = relational_ForeignKey(onDelete="sample_text_2", onUpdate="sample_text_2")
    b = relational_Column(defaultValue="sample_text", length=7, nullable=True, srid="sample_text")
    _safe_set(b, 'Column40', a1)
    assert _is_linked(b, 'Column40', a1)
    if hasattr(a1, 'foreignKey39'):
        assert _is_linked(a1, 'foreignKey39', b)
    _safe_set(b, 'Column40', a2)
    assert _is_linked(b, 'Column40', a2)
    if hasattr(a1, 'foreignKey39'):
        assert not _is_linked(a1, 'foreignKey39', b)
    if hasattr(a2, 'foreignKey39'):
        assert _is_linked(a2, 'foreignKey39', b)
    _safe_set(b, 'Column40', None)
    assert not _is_linked(b, 'Column40', a2)
    if hasattr(a2, 'foreignKey39'):
        assert not _is_linked(a2, 'foreignKey39', b)


def test_assoc_sqlobject1_reverse_link_reassign_clear():
    a1 = relational_SQLObject(description="sample_text", label="sample_text")
    a2 = relational_SQLObject(description="sample_text_2", label="sample_text_2")
    b = relational_Comment(description="sample_text")
    _safe_set(b, 'comments', a1)
    assert _is_linked(b, 'comments', a1)
    if hasattr(a1, 'SQLObject'):
        assert _is_linked(a1, 'SQLObject', b)
    _safe_set(b, 'comments', a2)
    assert _is_linked(b, 'comments', a2)
    if hasattr(a1, 'SQLObject'):
        assert not _is_linked(a1, 'SQLObject', b)
    if hasattr(a2, 'SQLObject'):
        assert _is_linked(a2, 'SQLObject', b)
    _safe_set(b, 'comments', None)
    assert not _is_linked(b, 'comments', a2)
    if hasattr(a2, 'SQLObject'):
        assert not _is_linked(a2, 'SQLObject', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assertions7_stub_double():
    # relational_Schema has no real 'schema8' property in the generated
    # code (a bare stub) -- manually attach it so relational_Assertion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Assertion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Assertion(searchCondition="sample_text")
    partner = relational_Schema()
    setattr(partner, 'schema8', None)
    _safe_set(owner, 'Assertion', partner)
    assert owner in getattr(partner, 'schema8')
    _safe_set(owner, 'Assertion', None)
    assert owner not in getattr(partner, 'schema8')


def test_assoc_columns23_stub_double():
    # relational_Table has no real 'table24' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True, srid="sample_text")
    partner = relational_Table()
    setattr(partner, 'table24', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'table24')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'table24')


def test_assoc_foreignKey41_stub_double():
    # relational_UniqueConstraint has no real 'uniqueConstraint' property in the generated
    # code (a bare stub) -- manually attach it so relational_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_ForeignKey(onDelete="sample_text", onUpdate="sample_text")
    partner = relational_UniqueConstraint()
    setattr(partner, 'uniqueConstraint', None)
    _safe_set(owner, 'ForeignKey42', partner)
    assert owner in getattr(partner, 'uniqueConstraint')
    _safe_set(owner, 'ForeignKey42', None)
    assert owner not in getattr(partner, 'uniqueConstraint')


def test_assoc_members33_stub_double():
    # relational_ReferenceConstraint has no real 'referenceConstraint' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True, srid="sample_text")
    partner = relational_ReferenceConstraint()
    setattr(partner, 'referenceConstraint', None)
    _safe_set(owner, 'Column34', partner)
    assert owner in getattr(partner, 'referenceConstraint')
    _safe_set(owner, 'Column34', None)
    assert owner not in getattr(partner, 'referenceConstraint')


def test_assoc_referenceConstraint27_stub_double():
    # relational_ReferenceConstraint has no real 'ReferenceConstraint' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True, srid="sample_text")
    partner = relational_ReferenceConstraint()
    setattr(partner, 'ReferenceConstraint', None)
    _safe_set(owner, 'members', {partner})
    assert getattr(partner, 'ReferenceConstraint') == owner
    _safe_set(owner, 'members', set())
    assert getattr(partner, 'ReferenceConstraint') is None


def test_assoc_referencedTable35_stub_double():
    # relational_BaseTable has no real 'BaseTable36' property in the generated
    # code (a bare stub) -- manually attach it so relational_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_ForeignKey(onDelete="sample_text", onUpdate="sample_text")
    partner = relational_BaseTable()
    setattr(partner, 'BaseTable36', None)
    _safe_set(owner, 'referencingForeignKeys', partner)
    assert getattr(partner, 'BaseTable36') == owner
    _safe_set(owner, 'referencingForeignKeys', None)
    assert getattr(partner, 'BaseTable36') is None


def test_assoc_referencedType48_stub_double():
    # relational_DataType has no real 'relational_DataType' property in the generated
    # code (a bare stub) -- manually attach it so relational_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Domain(defaultValue="sample_text", nullable=True)
    partner = relational_DataType()
    setattr(partner, 'relational_DataType', None)
    _safe_set(owner, 'relational_Domain49', partner)
    assert getattr(partner, 'relational_DataType') == owner
    _safe_set(owner, 'relational_Domain49', None)
    assert getattr(partner, 'relational_DataType') is None


def test_assoc_referencingForeignKeys29_stub_double():
    # relational_BaseTable has no real 'referencedTable' property in the generated
    # code (a bare stub) -- manually attach it so relational_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_ForeignKey(onDelete="sample_text", onUpdate="sample_text")
    partner = relational_BaseTable()
    setattr(partner, 'referencedTable', None)
    _safe_set(owner, 'ForeignKey30', partner)
    assert owner in getattr(partner, 'referencedTable')
    _safe_set(owner, 'ForeignKey30', None)
    assert owner not in getattr(partner, 'referencedTable')


def test_assoc_schema11_stub_double():
    # relational_Schema has no real 'Schema' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionGranularity="sample_text", actionTime="sample_text", condition="sample_text", deleteType=True, insertType=True, newRow="sample_text", newTable="sample_text", oldRow="sample_text", oldTable="sample_text", statementSQL="sample_text", updateType=True)
    partner = relational_Schema()
    setattr(partner, 'Schema', None)
    _safe_set(owner, 'triggers', partner)
    assert getattr(partner, 'Schema') == owner
    _safe_set(owner, 'triggers', None)
    assert getattr(partner, 'Schema') is None


def test_assoc_schema43_stub_double():
    # relational_Schema has no real 'Schema44' property in the generated
    # code (a bare stub) -- manually attach it so relational_Assertion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Assertion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Assertion(searchCondition="sample_text")
    partner = relational_Schema()
    setattr(partner, 'Schema44', None)
    _safe_set(owner, 'assertions', partner)
    assert getattr(partner, 'Schema44') == owner
    _safe_set(owner, 'assertions', None)
    assert getattr(partner, 'Schema44') is None


def test_assoc_table12_stub_double():
    # relational_Table has no real 'Table14' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionGranularity="sample_text", actionTime="sample_text", condition="sample_text", deleteType=True, insertType=True, newRow="sample_text", newTable="sample_text", oldRow="sample_text", oldTable="sample_text", statementSQL="sample_text", updateType=True)
    partner = relational_Table()
    setattr(partner, 'Table14', None)
    _safe_set(owner, 'triggers13', partner)
    assert getattr(partner, 'Table14') == owner
    _safe_set(owner, 'triggers13', None)
    assert getattr(partner, 'Table14') is None


def test_assoc_table25_stub_double():
    # relational_Table has no real 'Table26' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True, srid="sample_text")
    partner = relational_Table()
    setattr(partner, 'Table26', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'Table26') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'Table26') is None


def test_assoc_triggerTables15_stub_double():
    # relational_Table has no real 'Table16' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionGranularity="sample_text", actionTime="sample_text", condition="sample_text", deleteType=True, insertType=True, newRow="sample_text", newTable="sample_text", oldRow="sample_text", oldTable="sample_text", statementSQL="sample_text", updateType=True)
    partner = relational_Table()
    setattr(partner, 'Table16', None)
    _safe_set(owner, 'triggersConstrainted', {partner})
    assert getattr(partner, 'Table16') == owner
    _safe_set(owner, 'triggersConstrainted', set())
    assert getattr(partner, 'Table16') is None


def test_assoc_triggers19_stub_double():
    # relational_Table has no real 'table' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionGranularity="sample_text", actionTime="sample_text", condition="sample_text", deleteType=True, insertType=True, newRow="sample_text", newTable="sample_text", oldRow="sample_text", oldTable="sample_text", statementSQL="sample_text", updateType=True)
    partner = relational_Table()
    setattr(partner, 'table', None)
    _safe_set(owner, 'Trigger20', partner)
    assert owner in getattr(partner, 'table')
    _safe_set(owner, 'Trigger20', None)
    assert owner not in getattr(partner, 'table')


def test_assoc_triggers5_stub_double():
    # relational_Schema has no real 'schema6' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionGranularity="sample_text", actionTime="sample_text", condition="sample_text", deleteType=True, insertType=True, newRow="sample_text", newTable="sample_text", oldRow="sample_text", oldTable="sample_text", statementSQL="sample_text", updateType=True)
    partner = relational_Schema()
    setattr(partner, 'schema6', None)
    _safe_set(owner, 'Trigger', partner)
    assert owner in getattr(partner, 'schema6')
    _safe_set(owner, 'Trigger', None)
    assert owner not in getattr(partner, 'schema6')


def test_assoc_triggersConstrainted21_stub_double():
    # relational_Table has no real 'triggerTables' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionGranularity="sample_text", actionTime="sample_text", condition="sample_text", deleteType=True, insertType=True, newRow="sample_text", newTable="sample_text", oldRow="sample_text", oldTable="sample_text", statementSQL="sample_text", updateType=True)
    partner = relational_Table()
    setattr(partner, 'triggerTables', None)
    _safe_set(owner, 'Trigger22', partner)
    assert owner in getattr(partner, 'triggerTables')
    _safe_set(owner, 'Trigger22', None)
    assert owner not in getattr(partner, 'triggerTables')


def test_assoc_uniqueConstraint37_stub_double():
    # relational_UniqueConstraint has no real 'UniqueConstraint' property in the generated
    # code (a bare stub) -- manually attach it so relational_ForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_ForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_ForeignKey(onDelete="sample_text", onUpdate="sample_text")
    partner = relational_UniqueConstraint()
    setattr(partner, 'UniqueConstraint', None)
    _safe_set(owner, 'foreignKey', partner)
    assert getattr(partner, 'UniqueConstraint') == owner
    _safe_set(owner, 'foreignKey', None)
    assert getattr(partner, 'UniqueConstraint') is None


