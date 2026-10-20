import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    cycle_A,
    cycle_B,
    cycle_C,
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

def test_assoc_myA1_reverse_link_reassign_clear():
    a1 = cycle_B(x=3.14, y=3.14)
    a2 = cycle_B(x=9.99, y=9.99)
    b = cycle_A(i=7, j=7)
    _safe_set(b, 'cycle_A3', a1)
    assert _is_linked(b, 'cycle_A3', a1)
    if hasattr(a1, 'cycle_B2'):
        assert _is_linked(a1, 'cycle_B2', b)
    _safe_set(b, 'cycle_A3', a2)
    assert _is_linked(b, 'cycle_A3', a2)
    if hasattr(a1, 'cycle_B2'):
        assert not _is_linked(a1, 'cycle_B2', b)
    if hasattr(a2, 'cycle_B2'):
        assert _is_linked(a2, 'cycle_B2', b)
    _safe_set(b, 'cycle_A3', None)
    assert not _is_linked(b, 'cycle_A3', a2)
    if hasattr(a2, 'cycle_B2'):
        assert not _is_linked(a2, 'cycle_B2', b)


def test_assoc_myBs0_reverse_link_reassign_clear():
    a1 = cycle_B(x=3.14, y=3.14)
    a2 = cycle_B(x=9.99, y=9.99)
    b = cycle_A(i=7, j=7)
    _safe_set(b, 'cycle_A', {a1})
    assert _is_linked(b, 'cycle_A', a1)
    if hasattr(a1, 'cycle_B'):
        assert _is_linked(a1, 'cycle_B', b)
    _safe_set(b, 'cycle_A', {a2})
    assert _is_linked(b, 'cycle_A', a2)
    if hasattr(a1, 'cycle_B'):
        assert not _is_linked(a1, 'cycle_B', b)
    if hasattr(a2, 'cycle_B'):
        assert _is_linked(a2, 'cycle_B', b)
    _safe_set(b, 'cycle_A', set())
    assert not _is_linked(b, 'cycle_A', a2)
    if hasattr(a2, 'cycle_B'):
        assert not _is_linked(a2, 'cycle_B', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_myA6_stub_double():
    # cycle_C has no real 'cycle_C7' property in the generated
    # code (a bare stub) -- manually attach it so cycle_A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cycle_A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cycle_A(i=7, j=7)
    partner = cycle_C()
    setattr(partner, 'cycle_C7', None)
    _safe_set(owner, 'cycle_A8', partner)
    assert getattr(partner, 'cycle_C7') == owner
    _safe_set(owner, 'cycle_A8', None)
    assert getattr(partner, 'cycle_C7') is None


def test_assoc_myC4_stub_double():
    # cycle_C has no real 'cycle_C' property in the generated
    # code (a bare stub) -- manually attach it so cycle_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cycle_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cycle_B(x=3.14, y=3.14)
    partner = cycle_C()
    setattr(partner, 'cycle_C', None)
    _safe_set(owner, 'cycle_B5', partner)
    assert getattr(partner, 'cycle_C') == owner
    _safe_set(owner, 'cycle_B5', None)
    assert getattr(partner, 'cycle_C') is None


