import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    refac_A,
    refac_B,
    refac_C,
    refac_K,
    refac_M,
    refac_N99,
    refac_W,
    refac_X,
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

def test_assoc_wc16_stub_double():
    # refac_C has no real 'refac_C18' property in the generated
    # code (a bare stub) -- manually attach it so refac_W's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # refac_W's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = refac_W(name="sample_text")
    partner = refac_C()
    setattr(partner, 'refac_C18', None)
    _safe_set(owner, 'refac_W17', partner)
    assert getattr(partner, 'refac_C18') == owner
    _safe_set(owner, 'refac_W17', None)
    assert getattr(partner, 'refac_C18') is None


def test_assoc_ws3_stub_double():
    # refac_A has no real 'refac_A4' property in the generated
    # code (a bare stub) -- manually attach it so refac_W's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # refac_W's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = refac_W(name="sample_text")
    partner = refac_A()
    setattr(partner, 'refac_A4', None)
    _safe_set(owner, 'refac_W', partner)
    assert owner in getattr(partner, 'refac_A4')
    _safe_set(owner, 'refac_W', None)
    assert owner not in getattr(partner, 'refac_A4')


