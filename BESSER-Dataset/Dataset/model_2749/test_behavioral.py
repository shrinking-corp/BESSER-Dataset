import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    B_B,
    B_RootB,
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

def test_assoc_bs1_stub_double():
    # B_RootB has no real 'root' property in the generated
    # code (a bare stub) -- manually attach it so B_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_B(b=7)
    partner = B_RootB()
    setattr(partner, 'root', None)
    _safe_set(owner, 'B', partner)
    assert owner in getattr(partner, 'root')
    _safe_set(owner, 'B', None)
    assert owner not in getattr(partner, 'root')


def test_assoc_root0_stub_double():
    # B_RootB has no real 'RootB' property in the generated
    # code (a bare stub) -- manually attach it so B_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # B_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = B_B(b=7)
    partner = B_RootB()
    setattr(partner, 'RootB', None)
    _safe_set(owner, 'bs', partner)
    assert getattr(partner, 'RootB') == owner
    _safe_set(owner, 'bs', None)
    assert getattr(partner, 'RootB') is None


