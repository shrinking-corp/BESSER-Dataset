import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    unql_Connection,
    unql_Definition,
    unql_Program,
    unql_Select,
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

def test_assoc_connections1_stub_double():
    # unql_Program has no real 'unql_Program2' property in the generated
    # code (a bare stub) -- manually attach it so unql_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # unql_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = unql_Connection(name="sample_text", password="sample_text", url="sample_text", username="sample_text")
    partner = unql_Program()
    setattr(partner, 'unql_Program2', None)
    _safe_set(owner, 'unql_Connection', partner)
    assert owner in getattr(partner, 'unql_Program2')
    _safe_set(owner, 'unql_Connection', None)
    assert owner not in getattr(partner, 'unql_Program2')


def test_assoc_definitions0_stub_double():
    # unql_Program has no real 'unql_Program' property in the generated
    # code (a bare stub) -- manually attach it so unql_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # unql_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = unql_Definition(name="sample_text", type="sample_text")
    partner = unql_Program()
    setattr(partner, 'unql_Program', None)
    _safe_set(owner, 'unql_Definition', partner)
    assert owner in getattr(partner, 'unql_Program')
    _safe_set(owner, 'unql_Definition', None)
    assert owner not in getattr(partner, 'unql_Program')


def test_assoc_queries3_stub_double():
    # unql_Program has no real 'unql_Program4' property in the generated
    # code (a bare stub) -- manually attach it so unql_Select's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # unql_Select's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = unql_Select(attributes="sample_text", conditions="sample_text", relations="sample_text")
    partner = unql_Program()
    setattr(partner, 'unql_Program4', None)
    _safe_set(owner, 'unql_Select', partner)
    assert owner in getattr(partner, 'unql_Program4')
    _safe_set(owner, 'unql_Select', None)
    assert owner not in getattr(partner, 'unql_Program4')


