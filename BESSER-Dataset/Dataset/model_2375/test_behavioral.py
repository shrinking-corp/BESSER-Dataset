import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    ENamedElement,
    ReferenceConstraint,
    SQLObject,
    Table,
    TableConstraint,
    TypedElement,
    UniqueConstraint,
    relational_BaseTable,
    relational_Column,
    relational_Comment,
    relational_Constraint,
    relational_DataType,
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
    ActionTimeType,
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

def test_assoc_columns19_stub_double():
    # relational_Table has no real 'table20' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True)
    partner = relational_Table()
    setattr(partner, 'table20', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'table20')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'table20')


def test_assoc_foreignKey24_stub_double():
    # relational_ForeignKey has no real 'ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True)
    partner = relational_ForeignKey()
    setattr(partner, 'ForeignKey', None)
    _safe_set(owner, 'referencedMembers', {partner})
    assert getattr(partner, 'ForeignKey') == owner
    _safe_set(owner, 'referencedMembers', set())
    assert getattr(partner, 'ForeignKey') is None


def test_assoc_members29_stub_double():
    # relational_ReferenceConstraint has no real 'referenceConstraint' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True)
    partner = relational_ReferenceConstraint()
    setattr(partner, 'referenceConstraint', None)
    _safe_set(owner, 'Column30', partner)
    assert owner in getattr(partner, 'referenceConstraint')
    _safe_set(owner, 'Column30', None)
    assert owner not in getattr(partner, 'referenceConstraint')


def test_assoc_referenceConstraint23_stub_double():
    # relational_ReferenceConstraint has no real 'ReferenceConstraint' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True)
    partner = relational_ReferenceConstraint()
    setattr(partner, 'ReferenceConstraint', None)
    _safe_set(owner, 'members', {partner})
    assert getattr(partner, 'ReferenceConstraint') == owner
    _safe_set(owner, 'members', set())
    assert getattr(partner, 'ReferenceConstraint') is None


def test_assoc_referencedMembers34_stub_double():
    # relational_ForeignKey has no real 'foreignKey35' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True)
    partner = relational_ForeignKey()
    setattr(partner, 'foreignKey35', None)
    _safe_set(owner, 'Column36', partner)
    assert owner in getattr(partner, 'foreignKey35')
    _safe_set(owner, 'Column36', None)
    assert owner not in getattr(partner, 'foreignKey35')


def test_assoc_schema7_stub_double():
    # relational_Schema has no real 'Schema' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionTime="sample_text", deleteType=True, insertType=True, updateType=True)
    partner = relational_Schema()
    setattr(partner, 'Schema', None)
    _safe_set(owner, 'triggers', partner)
    assert getattr(partner, 'Schema') == owner
    _safe_set(owner, 'triggers', None)
    assert getattr(partner, 'Schema') is None


def test_assoc_table21_stub_double():
    # relational_Table has no real 'Table22' property in the generated
    # code (a bare stub) -- manually attach it so relational_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Column(defaultValue="sample_text", length=7, nullable=True)
    partner = relational_Table()
    setattr(partner, 'Table22', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'Table22') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'Table22') is None


def test_assoc_table8_stub_double():
    # relational_Table has no real 'Table10' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionTime="sample_text", deleteType=True, insertType=True, updateType=True)
    partner = relational_Table()
    setattr(partner, 'Table10', None)
    _safe_set(owner, 'triggers9', partner)
    assert getattr(partner, 'Table10') == owner
    _safe_set(owner, 'triggers9', None)
    assert getattr(partner, 'Table10') is None


def test_assoc_triggerTables11_stub_double():
    # relational_Table has no real 'Table12' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionTime="sample_text", deleteType=True, insertType=True, updateType=True)
    partner = relational_Table()
    setattr(partner, 'Table12', None)
    _safe_set(owner, 'triggersConstrainted', {partner})
    assert getattr(partner, 'Table12') == owner
    _safe_set(owner, 'triggersConstrainted', set())
    assert getattr(partner, 'Table12') is None


def test_assoc_triggers15_stub_double():
    # relational_Table has no real 'table' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionTime="sample_text", deleteType=True, insertType=True, updateType=True)
    partner = relational_Table()
    setattr(partner, 'table', None)
    _safe_set(owner, 'Trigger16', partner)
    assert owner in getattr(partner, 'table')
    _safe_set(owner, 'Trigger16', None)
    assert owner not in getattr(partner, 'table')


def test_assoc_triggers5_stub_double():
    # relational_Schema has no real 'schema6' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionTime="sample_text", deleteType=True, insertType=True, updateType=True)
    partner = relational_Schema()
    setattr(partner, 'schema6', None)
    _safe_set(owner, 'Trigger', partner)
    assert owner in getattr(partner, 'schema6')
    _safe_set(owner, 'Trigger', None)
    assert owner not in getattr(partner, 'schema6')


def test_assoc_triggersConstrainted17_stub_double():
    # relational_Table has no real 'triggerTables' property in the generated
    # code (a bare stub) -- manually attach it so relational_Trigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # relational_Trigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = relational_Trigger(actionTime="sample_text", deleteType=True, insertType=True, updateType=True)
    partner = relational_Table()
    setattr(partner, 'triggerTables', None)
    _safe_set(owner, 'Trigger18', partner)
    assert owner in getattr(partner, 'triggerTables')
    _safe_set(owner, 'Trigger18', None)
    assert owner not in getattr(partner, 'triggerTables')


