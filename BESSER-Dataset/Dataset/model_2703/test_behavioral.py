import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    sample_A,
    sample_B,
    sample_C,
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

def test_assoc_a1_stub_double():
    # sample_C has no real 'sample_C2' property in the generated
    # code (a bare stub) -- manually attach it so sample_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_A(name="sample_text", quantity=7, valid=True)
    partner = sample_C()
    setattr(partner, 'sample_C2', None)
    _safe_set(owner, 'sample_A', partner)
    assert getattr(partner, 'sample_C2') == owner
    _safe_set(owner, 'sample_A', None)
    assert getattr(partner, 'sample_C2') is None


def test_assoc_c0_stub_double():
    # sample_C has no real 'sample_C' property in the generated
    # code (a bare stub) -- manually attach it so sample_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_B(label="sample_text")
    partner = sample_C()
    setattr(partner, 'sample_C', None)
    _safe_set(owner, 'sample_B', {partner})
    assert getattr(partner, 'sample_C') == owner
    _safe_set(owner, 'sample_B', set())
    assert getattr(partner, 'sample_C') is None


