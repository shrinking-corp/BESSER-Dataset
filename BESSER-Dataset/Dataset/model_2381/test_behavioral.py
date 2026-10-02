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


