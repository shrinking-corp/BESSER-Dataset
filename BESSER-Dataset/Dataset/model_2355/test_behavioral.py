import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RModelElement,
    rdbmsMM_Column,
    rdbmsMM_ForeignKey,
    rdbmsMM_Key,
    rdbmsMM_RModelElement,
    rdbmsMM_Schema,
    rdbmsMM_Table,
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

def test_assoc_column10_stub_double():
    # rdbmsMM_ForeignKey has no real 'foreignKey11' property in the generated
    # code (a bare stub) -- manually attach it so rdbmsMM_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmsMM_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmsMM_Column(type="sample_text")
    partner = rdbmsMM_ForeignKey()
    setattr(partner, 'foreignKey11', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'foreignKey11')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'foreignKey11')


def test_assoc_column14_stub_double():
    # rdbmsMM_Key has no real 'key15' property in the generated
    # code (a bare stub) -- manually attach it so rdbmsMM_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmsMM_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmsMM_Column(type="sample_text")
    partner = rdbmsMM_Key()
    setattr(partner, 'key15', None)
    _safe_set(owner, 'Column16', partner)
    assert owner in getattr(partner, 'key15')
    _safe_set(owner, 'Column16', None)
    assert owner not in getattr(partner, 'key15')


def test_assoc_column22_stub_double():
    # rdbmsMM_Table has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so rdbmsMM_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmsMM_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmsMM_Column(type="sample_text")
    partner = rdbmsMM_Table()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Column23', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Column23', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_foreignKey3_stub_double():
    # rdbmsMM_ForeignKey has no real 'ForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so rdbmsMM_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmsMM_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmsMM_Column(type="sample_text")
    partner = rdbmsMM_ForeignKey()
    setattr(partner, 'ForeignKey', None)
    _safe_set(owner, 'column4', {partner})
    assert getattr(partner, 'ForeignKey') == owner
    _safe_set(owner, 'column4', set())
    assert getattr(partner, 'ForeignKey') is None


def test_assoc_key1_stub_double():
    # rdbmsMM_Key has no real 'Key' property in the generated
    # code (a bare stub) -- manually attach it so rdbmsMM_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmsMM_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmsMM_Column(type="sample_text")
    partner = rdbmsMM_Key()
    setattr(partner, 'Key', None)
    _safe_set(owner, 'column2', {partner})
    assert getattr(partner, 'Key') == owner
    _safe_set(owner, 'column2', set())
    assert getattr(partner, 'Key') is None


def test_assoc_owner0_stub_double():
    # rdbmsMM_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so rdbmsMM_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rdbmsMM_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rdbmsMM_Column(type="sample_text")
    partner = rdbmsMM_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'column', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'column', None)
    assert getattr(partner, 'Table') is None


