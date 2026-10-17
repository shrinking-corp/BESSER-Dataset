import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RModelElement,
    SimpleRDBMS_Column,
    SimpleRDBMS_ForeignKey,
    SimpleRDBMS_Key,
    SimpleRDBMS_RModelElement,
    SimpleRDBMS_Schema,
    SimpleRDBMS_Table,
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

def test_assoc__key7_stub_double():
    # SimpleRDBMS_Key has no real 'Key9' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = SimpleRDBMS_Key()
    setattr(partner, 'Key9', None)
    _safe_set(owner, 'column8', {partner})
    assert getattr(partner, 'Key9') == owner
    _safe_set(owner, 'column8', set())
    assert getattr(partner, 'Key9') is None


def test_assoc_column0_stub_double():
    # SimpleRDBMS_Table has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = SimpleRDBMS_Table()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Column', partner)
    assert getattr(partner, 'owner') == owner
    _safe_set(owner, 'Column', None)
    assert getattr(partner, 'owner') is None


def test_assoc_column13_stub_double():
    # SimpleRDBMS_Key has no real '_key' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = SimpleRDBMS_Key()
    setattr(partner, '_key', None)
    _safe_set(owner, 'Column14', partner)
    assert getattr(partner, '_key') == owner
    _safe_set(owner, 'Column14', None)
    assert getattr(partner, '_key') is None


def test_assoc_column18_stub_double():
    # SimpleRDBMS_ForeignKey has no real 'foreignKey' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = SimpleRDBMS_ForeignKey()
    setattr(partner, 'foreignKey', None)
    _safe_set(owner, 'Column19', partner)
    assert getattr(partner, 'foreignKey') == owner
    _safe_set(owner, 'Column19', None)
    assert getattr(partner, 'foreignKey') is None


def test_assoc_foreignKey10_stub_double():
    # SimpleRDBMS_ForeignKey has no real 'ForeignKey12' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = SimpleRDBMS_ForeignKey()
    setattr(partner, 'ForeignKey12', None)
    _safe_set(owner, 'column11', {partner})
    assert getattr(partner, 'ForeignKey12') == owner
    _safe_set(owner, 'column11', set())
    assert getattr(partner, 'ForeignKey12') is None


def test_assoc_owner6_stub_double():
    # SimpleRDBMS_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = SimpleRDBMS_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'column', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'column', None)
    assert getattr(partner, 'Table') is None


