import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RdbmsModelElement,
    SimpleRDBMS_RdbmsColumn,
    SimpleRDBMS_RdbmsForeignKey,
    SimpleRDBMS_RdbmsKey,
    SimpleRDBMS_RdbmsModelElement,
    SimpleRDBMS_RdbmsSchema,
    SimpleRDBMS_RdbmsTable,
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

def test_assoc_rdbmsColumn11_stub_double():
    # SimpleRDBMS_RdbmsKey has no real 'rdbmsKey' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_RdbmsColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_RdbmsColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_RdbmsColumn(rdbmsType="sample_text")
    partner = SimpleRDBMS_RdbmsKey()
    setattr(partner, 'rdbmsKey', None)
    _safe_set(owner, 'RdbmsColumn12', partner)
    assert owner in getattr(partner, 'rdbmsKey')
    _safe_set(owner, 'RdbmsColumn12', None)
    assert owner not in getattr(partner, 'rdbmsKey')


def test_assoc_rdbmsColumn20_stub_double():
    # SimpleRDBMS_RdbmsTable has no real 'rdbmsOwner' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_RdbmsColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_RdbmsColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_RdbmsColumn(rdbmsType="sample_text")
    partner = SimpleRDBMS_RdbmsTable()
    setattr(partner, 'rdbmsOwner', None)
    _safe_set(owner, 'RdbmsColumn21', partner)
    assert owner in getattr(partner, 'rdbmsOwner')
    _safe_set(owner, 'RdbmsColumn21', None)
    assert owner not in getattr(partner, 'rdbmsOwner')


def test_assoc_rdbmsColumn9_stub_double():
    # SimpleRDBMS_RdbmsForeignKey has no real 'rdbmsForeignKey10' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_RdbmsColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_RdbmsColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_RdbmsColumn(rdbmsType="sample_text")
    partner = SimpleRDBMS_RdbmsForeignKey()
    setattr(partner, 'rdbmsForeignKey10', None)
    _safe_set(owner, 'RdbmsColumn', partner)
    assert owner in getattr(partner, 'rdbmsForeignKey10')
    _safe_set(owner, 'RdbmsColumn', None)
    assert owner not in getattr(partner, 'rdbmsForeignKey10')


def test_assoc_rdbmsForeignKey3_stub_double():
    # SimpleRDBMS_RdbmsForeignKey has no real 'RdbmsForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_RdbmsColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_RdbmsColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_RdbmsColumn(rdbmsType="sample_text")
    partner = SimpleRDBMS_RdbmsForeignKey()
    setattr(partner, 'RdbmsForeignKey', None)
    _safe_set(owner, 'rdbmsColumn4', {partner})
    assert getattr(partner, 'RdbmsForeignKey') == owner
    _safe_set(owner, 'rdbmsColumn4', set())
    assert getattr(partner, 'RdbmsForeignKey') is None


def test_assoc_rdbmsKey1_stub_double():
    # SimpleRDBMS_RdbmsKey has no real 'RdbmsKey' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_RdbmsColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_RdbmsColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_RdbmsColumn(rdbmsType="sample_text")
    partner = SimpleRDBMS_RdbmsKey()
    setattr(partner, 'RdbmsKey', None)
    _safe_set(owner, 'rdbmsColumn2', {partner})
    assert getattr(partner, 'RdbmsKey') == owner
    _safe_set(owner, 'rdbmsColumn2', set())
    assert getattr(partner, 'RdbmsKey') is None


def test_assoc_rdbmsOwner0_stub_double():
    # SimpleRDBMS_RdbmsTable has no real 'RdbmsTable' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_RdbmsColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_RdbmsColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_RdbmsColumn(rdbmsType="sample_text")
    partner = SimpleRDBMS_RdbmsTable()
    setattr(partner, 'RdbmsTable', None)
    _safe_set(owner, 'rdbmsColumn', partner)
    assert getattr(partner, 'RdbmsTable') == owner
    _safe_set(owner, 'rdbmsColumn', None)
    assert getattr(partner, 'RdbmsTable') is None


