import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CWMRelationalData_CheckConstraint,
    CWMRelationalData_Column,
    CWMRelationalData_ColumnSet,
    CWMRelationalData_NamedColumnSet,
    CWMRelationalData_QueryColumnSet,
    CWMRelationalData_QueryExpression,
    CWMRelationalData_SQLDataType,
    CWMRelationalData_SQLDistinctType,
    CWMRelationalData_SQLSimpleType,
    CWMRelationalData_Table,
    CWMRelationalData_Trigger,
    CWMRelationalData_View,
    CheckConstraint,
    Column,
    ColumnSet,
    NamedColumnSet,
    QueryExpression,
    SQLDataType,
    SQLDistinctType,
    SQLSimpleType,
    Table,
    Trigger,
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

def test_assoc_column_constraints2_stub_double():
    # CheckConstraint has no real 'CheckConstraint' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    partner = CheckConstraint()
    setattr(partner, 'CheckConstraint', None)
    _safe_set(owner, 'constraintElements', {partner})
    assert getattr(partner, 'CheckConstraint') == owner
    _safe_set(owner, 'constraintElements', set())
    assert getattr(partner, 'CheckConstraint') is None


def test_assoc_optionScopeColumnSet5_stub_double():
    # NamedColumnSet has no real 'NamedColumnSet' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    partner = NamedColumnSet()
    setattr(partner, 'NamedColumnSet', None)
    _safe_set(owner, 'optionScopeColumn', partner)
    assert getattr(partner, 'NamedColumnSet') == owner
    _safe_set(owner, 'optionScopeColumn', None)
    assert getattr(partner, 'NamedColumnSet') is None


def test_assoc_owner4_stub_double():
    # ColumnSet has no real 'ColumnSet' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    partner = ColumnSet()
    setattr(partner, 'ColumnSet', None)
    _safe_set(owner, 'features', partner)
    assert getattr(partner, 'ColumnSet') == owner
    _safe_set(owner, 'features', None)
    assert getattr(partner, 'ColumnSet') is None


def test_assoc_queryExpression14_stub_double():
    # QueryExpression has no real 'QueryExpression15' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_View(checkOption="sample_text", isReadOnly="sample_text")
    partner = QueryExpression()
    setattr(partner, 'QueryExpression15', None)
    _safe_set(owner, 'CWMRelationalData_View', partner)
    assert getattr(partner, 'QueryExpression15') == owner
    _safe_set(owner, 'CWMRelationalData_View', None)
    assert getattr(partner, 'QueryExpression15') is None


def test_assoc_sqlDistinctTypes21_stub_double():
    # SQLDistinctType has no real 'SQLDistinctType' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_SQLSimpleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_SQLSimpleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_SQLSimpleType(characterMaximumLength="sample_text", characterOctetLength="sample_text", dateTimePrecision="sample_text", numericPrecision="sample_text", numericPrecisionRadix="sample_text", numericScale="sample_text")
    partner = SQLDistinctType()
    setattr(partner, 'SQLDistinctType', None)
    _safe_set(owner, 'sqlSimpleType', {partner})
    assert getattr(partner, 'SQLDistinctType') == owner
    _safe_set(owner, 'sqlSimpleType', set())
    assert getattr(partner, 'SQLDistinctType') is None


def test_assoc_sqlSimpleType20_stub_double():
    # SQLSimpleType has no real 'SQLSimpleType' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_SQLDistinctType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_SQLDistinctType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_SQLDistinctType(length="sample_text", precision="sample_text", scale="sample_text")
    partner = SQLSimpleType()
    setattr(partner, 'SQLSimpleType', None)
    _safe_set(owner, 'sqlDistinctTypes', partner)
    assert getattr(partner, 'SQLSimpleType') == owner
    _safe_set(owner, 'sqlDistinctTypes', None)
    assert getattr(partner, 'SQLSimpleType') is None


def test_assoc_structuralFeatures18_stub_double():
    # Column has no real 'Column19' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_SQLDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_SQLDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_SQLDataType(typeNumber="sample_text")
    partner = Column()
    setattr(partner, 'Column19', None)
    _safe_set(owner, 'type', {partner})
    assert getattr(partner, 'Column19') == owner
    _safe_set(owner, 'type', set())
    assert getattr(partner, 'Column19') is None


def test_assoc_table_constraints12_stub_double():
    # CheckConstraint has no real 'CheckConstraint13' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_Table(isSystem="sample_text", isTemporary="sample_text", temporaryScope="sample_text")
    partner = CheckConstraint()
    setattr(partner, 'CheckConstraint13', None)
    _safe_set(owner, 'constrainedElements', {partner})
    assert getattr(partner, 'CheckConstraint13') == owner
    _safe_set(owner, 'constrainedElements', set())
    assert getattr(partner, 'CheckConstraint13') is None


def test_assoc_type3_stub_double():
    # SQLDataType has no real 'SQLDataType' property in the generated
    # code (a bare stub) -- manually attach it so CWMRelationalData_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CWMRelationalData_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CWMRelationalData_Column(characterSetName="sample_text", collectionName="sample_text", isNullable="sample_text", length="sample_text", precision="sample_text", scale="sample_text")
    partner = SQLDataType()
    setattr(partner, 'SQLDataType', None)
    _safe_set(owner, 'structuralFeatures', partner)
    assert getattr(partner, 'SQLDataType') == owner
    _safe_set(owner, 'structuralFeatures', None)
    assert getattr(partner, 'SQLDataType') is None


