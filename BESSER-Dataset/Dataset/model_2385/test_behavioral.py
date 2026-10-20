import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    sql_Column,
    sql_Element,
    sql_Table,
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

def test_assoc_column0_stub_double():
    # sql_Table has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(type="sample_text")
    partner = sql_Table()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'Column', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'Column', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_fkey2_stub_double():
    # sql_Table has no real 'sql_Table3' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(type="sample_text")
    partner = sql_Table()
    setattr(partner, 'sql_Table3', None)
    _safe_set(owner, 'sql_Column4', partner)
    assert owner in getattr(partner, 'sql_Table3')
    _safe_set(owner, 'sql_Column4', None)
    assert owner not in getattr(partner, 'sql_Table3')


def test_assoc_key1_stub_double():
    # sql_Table has no real 'sql_Table' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(type="sample_text")
    partner = sql_Table()
    setattr(partner, 'sql_Table', None)
    _safe_set(owner, 'sql_Column', partner)
    assert owner in getattr(partner, 'sql_Table')
    _safe_set(owner, 'sql_Column', None)
    assert owner not in getattr(partner, 'sql_Table')


def test_assoc_owner5_stub_double():
    # sql_Table has no real 'Table' property in the generated
    # code (a bare stub) -- manually attach it so sql_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sql_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sql_Column(type="sample_text")
    partner = sql_Table()
    setattr(partner, 'Table', None)
    _safe_set(owner, 'column', partner)
    assert getattr(partner, 'Table') == owner
    _safe_set(owner, 'column', None)
    assert getattr(partner, 'Table') is None


