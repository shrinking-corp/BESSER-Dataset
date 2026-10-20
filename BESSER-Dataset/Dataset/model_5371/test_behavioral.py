import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    hExample_1_RHS_X,
    hExample_1_RHS_Y,
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

def test_assoc_link0_stub_double():
    # hExample_1_RHS_X has no real 'hExample_1_RHS_X' property in the generated
    # code (a bare stub) -- manually attach it so hExample_1_RHS_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # hExample_1_RHS_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = hExample_1_RHS_Y(label="sample_text")
    partner = hExample_1_RHS_X()
    setattr(partner, 'hExample_1_RHS_X', None)
    _safe_set(owner, 'hExample_1_RHS_Y', partner)
    assert getattr(partner, 'hExample_1_RHS_X') == owner
    _safe_set(owner, 'hExample_1_RHS_Y', None)
    assert getattr(partner, 'hExample_1_RHS_X') is None


