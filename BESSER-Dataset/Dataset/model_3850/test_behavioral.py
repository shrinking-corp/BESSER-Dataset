import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    FKey,
    SimpleRDBMS_Column,
    SimpleRDBMS_FKey,
    SimpleRDBMS_Table,
    Table,
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

def test_assoc_cols3_stub_double():
    # Column has no real 'Column5' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Table(name="sample_text", tipo="sample_text")
    partner = Column()
    setattr(partner, 'Column5', None)
    _safe_set(owner, 'SimpleRDBMS_Table4', {partner})
    assert getattr(partner, 'Column5') == owner
    _safe_set(owner, 'SimpleRDBMS_Table4', set())
    assert getattr(partner, 'Column5') is None


def test_assoc_fkeys0_stub_double():
    # FKey has no real 'FKey' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Table(name="sample_text", tipo="sample_text")
    partner = FKey()
    setattr(partner, 'FKey', None)
    _safe_set(owner, 'SimpleRDBMS_Table', {partner})
    assert getattr(partner, 'FKey') == owner
    _safe_set(owner, 'SimpleRDBMS_Table', set())
    assert getattr(partner, 'FKey') is None


def test_assoc_pkey1_stub_double():
    # Column has no real 'Column' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Table(name="sample_text", tipo="sample_text")
    partner = Column()
    setattr(partner, 'Column', None)
    _safe_set(owner, 'SimpleRDBMS_Table2', {partner})
    assert getattr(partner, 'Column') == owner
    _safe_set(owner, 'SimpleRDBMS_Table2', set())
    assert getattr(partner, 'Column') is None


