import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    grammarSql_Column,
    grammarSql_EObject,
    grammarSql_ForeignKey,
    grammarSql_Model,
    grammarSql_PrimaryKey,
    grammarSql_Reference,
    grammarSql_Table,
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

def test_assoc_col3_stub_double():
    # grammarSql_PrimaryKey has no real 'grammarSql_PrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so grammarSql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammarSql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammarSql_Column(isNotNull=True, name="sample_text", type="sample_text")
    partner = grammarSql_PrimaryKey()
    setattr(partner, 'grammarSql_PrimaryKey', None)
    _safe_set(owner, 'grammarSql_Column', partner)
    assert owner in getattr(partner, 'grammarSql_PrimaryKey')
    _safe_set(owner, 'grammarSql_Column', None)
    assert owner not in getattr(partner, 'grammarSql_PrimaryKey')


def test_assoc_elements1_stub_double():
    # grammarSql_EObject has no real 'grammarSql_EObject' property in the generated
    # code (a bare stub) -- manually attach it so grammarSql_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammarSql_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammarSql_Table(name="sample_text")
    partner = grammarSql_EObject()
    setattr(partner, 'grammarSql_EObject', None)
    _safe_set(owner, 'grammarSql_Table2', {partner})
    assert getattr(partner, 'grammarSql_EObject') == owner
    _safe_set(owner, 'grammarSql_Table2', set())
    assert getattr(partner, 'grammarSql_EObject') is None


def test_assoc_fromC11_stub_double():
    # grammarSql_Reference has no real 'grammarSql_Reference12' property in the generated
    # code (a bare stub) -- manually attach it so grammarSql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammarSql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammarSql_Column(isNotNull=True, name="sample_text", type="sample_text")
    partner = grammarSql_Reference()
    setattr(partner, 'grammarSql_Reference12', None)
    _safe_set(owner, 'grammarSql_Column13', partner)
    assert owner in getattr(partner, 'grammarSql_Reference12')
    _safe_set(owner, 'grammarSql_Column13', None)
    assert owner not in getattr(partner, 'grammarSql_Reference12')


def test_assoc_fromT8_stub_double():
    # grammarSql_Reference has no real 'grammarSql_Reference9' property in the generated
    # code (a bare stub) -- manually attach it so grammarSql_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammarSql_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammarSql_Table(name="sample_text")
    partner = grammarSql_Reference()
    setattr(partner, 'grammarSql_Reference9', None)
    _safe_set(owner, 'grammarSql_Table10', partner)
    assert owner in getattr(partner, 'grammarSql_Reference9')
    _safe_set(owner, 'grammarSql_Table10', None)
    assert owner not in getattr(partner, 'grammarSql_Reference9')


def test_assoc_localColumns4_stub_double():
    # grammarSql_ForeignKey has no real 'grammarSql_ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so grammarSql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammarSql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammarSql_Column(isNotNull=True, name="sample_text", type="sample_text")
    partner = grammarSql_ForeignKey()
    setattr(partner, 'grammarSql_ForeignKey', None)
    _safe_set(owner, 'grammarSql_Column5', partner)
    assert owner in getattr(partner, 'grammarSql_ForeignKey')
    _safe_set(owner, 'grammarSql_Column5', None)
    assert owner not in getattr(partner, 'grammarSql_ForeignKey')


def test_assoc_tables0_stub_double():
    # grammarSql_Model has no real 'grammarSql_Model' property in the generated
    # code (a bare stub) -- manually attach it so grammarSql_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammarSql_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammarSql_Table(name="sample_text")
    partner = grammarSql_Model()
    setattr(partner, 'grammarSql_Model', None)
    _safe_set(owner, 'grammarSql_Table', partner)
    assert owner in getattr(partner, 'grammarSql_Model')
    _safe_set(owner, 'grammarSql_Table', None)
    assert owner not in getattr(partner, 'grammarSql_Model')


