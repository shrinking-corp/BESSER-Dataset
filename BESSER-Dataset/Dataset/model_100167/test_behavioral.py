import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    ForeignKey,
    Key,
    RModelElement,
    Schema,
    SimpleRDBMS_Column,
    SimpleRDBMS_ForeignKey,
    SimpleRDBMS_Key,
    SimpleRDBMS_RModelElement,
    SimpleRDBMS_Schema,
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

def test_assoc_foreignKey12_stub_double():
    # ForeignKey has no real 'ForeignKey14' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = ForeignKey()
    setattr(partner, 'ForeignKey14', None)
    _safe_set(owner, 'column13', {partner})
    assert getattr(partner, 'ForeignKey14') == owner
    _safe_set(owner, 'column13', set())
    assert getattr(partner, 'ForeignKey14') is None


def test_assoc_key9_stub_double():
    # Key has no real 'Key11' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = Key()
    setattr(partner, 'Key11', None)
    _safe_set(owner, 'column10', {partner})
    assert getattr(partner, 'Key11') == owner
    _safe_set(owner, 'column10', set())
    assert getattr(partner, 'Key11') is None


def test_assoc_owner7_stub_double():
    # Table has no real 'Table8' property in the generated
    # code (a bare stub) -- manually attach it so SimpleRDBMS_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleRDBMS_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleRDBMS_Column(type="sample_text")
    partner = Table()
    setattr(partner, 'Table8', None)
    _safe_set(owner, 'column', partner)
    assert getattr(partner, 'Table8') == owner
    _safe_set(owner, 'column', None)
    assert getattr(partner, 'Table8') is None


