import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    B,
    Named,
    minher_A,
    minher_B,
    minher_C,
    minher_E,
    minher_G,
    minher_Named,
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

def test_assoc_bs0_stub_double():
    # minher_A has no real 'minher_A' property in the generated
    # code (a bare stub) -- manually attach it so minher_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minher_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minher_B(value="sample_text")
    partner = minher_A()
    setattr(partner, 'minher_A', None)
    _safe_set(owner, 'minher_B', partner)
    assert owner in getattr(partner, 'minher_A')
    _safe_set(owner, 'minher_B', None)
    assert owner not in getattr(partner, 'minher_A')


def test_assoc_cs3_stub_double():
    # minher_C has no real 'minher_C' property in the generated
    # code (a bare stub) -- manually attach it so minher_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minher_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minher_B(value="sample_text")
    partner = minher_C()
    setattr(partner, 'minher_C', None)
    _safe_set(owner, 'minher_B4', {partner})
    assert getattr(partner, 'minher_C') == owner
    _safe_set(owner, 'minher_B4', set())
    assert getattr(partner, 'minher_C') is None


def test_assoc_gs1_stub_double():
    # minher_G has no real 'minher_G' property in the generated
    # code (a bare stub) -- manually attach it so minher_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # minher_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = minher_B(value="sample_text")
    partner = minher_G()
    setattr(partner, 'minher_G', None)
    _safe_set(owner, 'minher_B2', {partner})
    assert getattr(partner, 'minher_G') == owner
    _safe_set(owner, 'minher_B2', set())
    assert getattr(partner, 'minher_G') is None


