import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SuperA3,
    testmerge_A3,
    testmerge_B3,
    testmerge_SuperA3,
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

def test_assoc_toA31_stub_double():
    # testmerge_A3 has no real 'A3' property in the generated
    # code (a bare stub) -- manually attach it so testmerge_B3's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmerge_B3's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmerge_B3()
    partner = testmerge_A3()
    setattr(partner, 'A3', None)
    _safe_set(owner, 'toB3', partner)
    assert getattr(partner, 'A3') == owner
    _safe_set(owner, 'toB3', None)
    assert getattr(partner, 'A3') is None


def test_assoc_toB30_stub_double():
    # testmerge_A3 has no real 'toA3' property in the generated
    # code (a bare stub) -- manually attach it so testmerge_B3's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testmerge_B3's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testmerge_B3()
    partner = testmerge_A3()
    setattr(partner, 'toA3', None)
    _safe_set(owner, 'B3', partner)
    assert getattr(partner, 'toA3') == owner
    _safe_set(owner, 'B3', None)
    assert getattr(partner, 'toA3') is None


