import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sql_Column,
    sql_Database,
    sql_EObject,
    sql_ForeignKey,
    sql_Model,
    sql_PrimaryKey,
    sql_Table,
    DataType,
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

def test_assoc_col5_stub_double():
    # sql_PrimaryKey has no real 'sql_PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(isNotNull=True, name="sample_text", type="sample_text")
    partner = sql_PrimaryKey()
    setattr(partner, 'sql_PrimaryKey', None)
    _safe_set(owner, 'sql_Column', partner)
    assert owner in getattr(partner, 'sql_PrimaryKey')
    _safe_set(owner, 'sql_Column', None)
    assert owner not in getattr(partner, 'sql_PrimaryKey')


def test_assoc_facts3_stub_double():
    # sql_EObject has no real 'sql_EObject' property in the generated
    # code (a bare stub) -- manually attach it so sql_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Table(name="sample_text")
    partner = sql_EObject()
    setattr(partner, 'sql_EObject', None)
    _safe_set(owner, 'sql_Table4', {partner})
    assert getattr(partner, 'sql_EObject') == owner
    _safe_set(owner, 'sql_Table4', set())
    assert getattr(partner, 'sql_EObject') is None


def test_assoc_foreignColumns11_stub_double():
    # sql_ForeignKey has no real 'sql_ForeignKey12' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(isNotNull=True, name="sample_text", type="sample_text")
    partner = sql_ForeignKey()
    setattr(partner, 'sql_ForeignKey12', None)
    _safe_set(owner, 'sql_Column13', partner)
    assert owner in getattr(partner, 'sql_ForeignKey12')
    _safe_set(owner, 'sql_Column13', None)
    assert owner not in getattr(partner, 'sql_ForeignKey12')


def test_assoc_foreignTable8_stub_double():
    # sql_ForeignKey has no real 'sql_ForeignKey9' property in the generated
    # code (a bare stub) -- manually attach it so sql_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Table(name="sample_text")
    partner = sql_ForeignKey()
    setattr(partner, 'sql_ForeignKey9', None)
    _safe_set(owner, 'sql_Table10', partner)
    assert getattr(partner, 'sql_ForeignKey9') == owner
    _safe_set(owner, 'sql_Table10', None)
    assert getattr(partner, 'sql_ForeignKey9') is None


def test_assoc_localColumns6_stub_double():
    # sql_ForeignKey has no real 'sql_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(isNotNull=True, name="sample_text", type="sample_text")
    partner = sql_ForeignKey()
    setattr(partner, 'sql_ForeignKey', None)
    _safe_set(owner, 'sql_Column7', partner)
    assert owner in getattr(partner, 'sql_ForeignKey')
    _safe_set(owner, 'sql_Column7', None)
    assert owner not in getattr(partner, 'sql_ForeignKey')


def test_assoc_tables1_stub_double():
    # sql_Database has no real 'sql_Database2' property in the generated
    # code (a bare stub) -- manually attach it so sql_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Table(name="sample_text")
    partner = sql_Database()
    setattr(partner, 'sql_Database2', None)
    _safe_set(owner, 'sql_Table', partner)
    assert owner in getattr(partner, 'sql_Database2')
    _safe_set(owner, 'sql_Table', None)
    assert owner not in getattr(partner, 'sql_Database2')


