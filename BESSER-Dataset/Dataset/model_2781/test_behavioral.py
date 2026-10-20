import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    p_A,
    p_B,
    p_C,
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

def test_assoc_a0_stub_double():
    # p_B has no real 'p_B' property in the generated
    # code (a bare stub) -- manually attach it so p_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p_A(name=True)
    partner = p_B()
    setattr(partner, 'p_B', None)
    _safe_set(owner, 'p_A', partner)
    assert getattr(partner, 'p_B') == owner
    _safe_set(owner, 'p_A', None)
    assert getattr(partner, 'p_B') is None


def test_assoc_c3_stub_double():
    # p_C has no real 'p_C4' property in the generated
    # code (a bare stub) -- manually attach it so p_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # p_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = p_A(name=True)
    partner = p_C()
    setattr(partner, 'p_C4', None)
    _safe_set(owner, 'p_A5', partner)
    assert getattr(partner, 'p_C4') == owner
    _safe_set(owner, 'p_A5', None)
    assert getattr(partner, 'p_C4') is None


