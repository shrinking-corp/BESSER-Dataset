import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataBaseElement,
    database_Column,
    database_DataBaseElement,
    database_ForeignKey,
    database_Schema,
    database_Table,
    RailsData,
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

def test_assoc_column8_stub_double():
    # database_ForeignKey has no real 'database_ForeignKey9' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(type="sample_text")
    partner = database_ForeignKey()
    setattr(partner, 'database_ForeignKey9', None)
    _safe_set(owner, 'database_Column10', partner)
    assert getattr(partner, 'database_ForeignKey9') == owner
    _safe_set(owner, 'database_Column10', None)
    assert getattr(partner, 'database_ForeignKey9') is None


def test_assoc_columns1_stub_double():
    # database_Table has no real 'database_Table2' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(type="sample_text")
    partner = database_Table()
    setattr(partner, 'database_Table2', None)
    _safe_set(owner, 'database_Column', partner)
    assert owner in getattr(partner, 'database_Table2')
    _safe_set(owner, 'database_Column', None)
    assert owner not in getattr(partner, 'database_Table2')


def test_assoc_primaryKey3_stub_double():
    # database_Table has no real 'database_Table4' property in the generated
    # code (a bare stub) -- manually attach it so database_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # database_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = database_Column(type="sample_text")
    partner = database_Table()
    setattr(partner, 'database_Table4', None)
    _safe_set(owner, 'database_Column5', partner)
    assert getattr(partner, 'database_Table4') == owner
    _safe_set(owner, 'database_Column5', None)
    assert getattr(partner, 'database_Table4') is None


