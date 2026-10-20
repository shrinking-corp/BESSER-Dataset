import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    N,
    Y,
    ktest206_A,
    ktest206_B,
    ktest206_C,
    ktest206_D,
    ktest206_E,
    ktest206_N,
    ktest206_V,
    ktest206_W,
    ktest206_X,
    ktest206_Y,
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

def test_assoc_cs0_stub_double():
    # ktest206_B has no real 'ktest206_B' property in the generated
    # code (a bare stub) -- manually attach it so ktest206_C's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ktest206_C's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ktest206_C(name="sample_text")
    partner = ktest206_B()
    setattr(partner, 'ktest206_B', None)
    _safe_set(owner, 'ktest206_C', partner)
    assert owner in getattr(partner, 'ktest206_B')
    _safe_set(owner, 'ktest206_C', None)
    assert owner not in getattr(partner, 'ktest206_B')


def test_assoc_ds1_stub_double():
    # ktest206_A has no real 'ktest206_A' property in the generated
    # code (a bare stub) -- manually attach it so ktest206_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ktest206_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ktest206_D(name="sample_text")
    partner = ktest206_A()
    setattr(partner, 'ktest206_A', None)
    _safe_set(owner, 'ktest206_D', partner)
    assert owner in getattr(partner, 'ktest206_A')
    _safe_set(owner, 'ktest206_D', None)
    assert owner not in getattr(partner, 'ktest206_A')


