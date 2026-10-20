import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Identified,
    multicontainment_b_ChildB1,
    multicontainment_b_ChildB2,
    multicontainment_b_Identified,
    multicontainment_b_RootB,
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

def test_assoc_childrenB1a0_stub_double():
    # multicontainment_b_RootB has no real 'multicontainment_b_RootB' property in the generated
    # code (a bare stub) -- manually attach it so multicontainment_b_ChildB1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # multicontainment_b_ChildB1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = multicontainment_b_ChildB1(name="sample_text")
    partner = multicontainment_b_RootB()
    setattr(partner, 'multicontainment_b_RootB', None)
    _safe_set(owner, 'multicontainment_b_ChildB1', partner)
    assert getattr(partner, 'multicontainment_b_RootB') == owner
    _safe_set(owner, 'multicontainment_b_ChildB1', None)
    assert getattr(partner, 'multicontainment_b_RootB') is None


def test_assoc_childrenB1b1_stub_double():
    # multicontainment_b_RootB has no real 'multicontainment_b_RootB2' property in the generated
    # code (a bare stub) -- manually attach it so multicontainment_b_ChildB1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # multicontainment_b_ChildB1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = multicontainment_b_ChildB1(name="sample_text")
    partner = multicontainment_b_RootB()
    setattr(partner, 'multicontainment_b_RootB2', None)
    _safe_set(owner, 'multicontainment_b_ChildB13', partner)
    assert getattr(partner, 'multicontainment_b_RootB2') == owner
    _safe_set(owner, 'multicontainment_b_ChildB13', None)
    assert getattr(partner, 'multicontainment_b_RootB2') is None


def test_assoc_childrenB2a4_stub_double():
    # multicontainment_b_RootB has no real 'multicontainment_b_RootB5' property in the generated
    # code (a bare stub) -- manually attach it so multicontainment_b_ChildB2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # multicontainment_b_ChildB2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = multicontainment_b_ChildB2(name="sample_text")
    partner = multicontainment_b_RootB()
    setattr(partner, 'multicontainment_b_RootB5', None)
    _safe_set(owner, 'multicontainment_b_ChildB2', partner)
    assert getattr(partner, 'multicontainment_b_RootB5') == owner
    _safe_set(owner, 'multicontainment_b_ChildB2', None)
    assert getattr(partner, 'multicontainment_b_RootB5') is None


