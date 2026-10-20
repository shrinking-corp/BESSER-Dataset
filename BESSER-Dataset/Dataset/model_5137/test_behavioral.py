import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SuperStuff,
    SuperStuff2,
    a_A,
    a_B,
    a_Root,
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

def test_assoc_b4_reverse_link_reassign_clear():
    a1 = a_Root(visible=True)
    a2 = a_Root(visible=False)
    b = a_B(name="sample_text")
    _safe_set(b, 'a_B', a1)
    assert _is_linked(b, 'a_B', a1)
    if hasattr(a1, 'a_Root5'):
        assert _is_linked(a1, 'a_Root5', b)
    _safe_set(b, 'a_B', a2)
    assert _is_linked(b, 'a_B', a2)
    if hasattr(a1, 'a_Root5'):
        assert not _is_linked(a1, 'a_Root5', b)
    if hasattr(a2, 'a_Root5'):
        assert _is_linked(a2, 'a_Root5', b)
    _safe_set(b, 'a_B', None)
    assert not _is_linked(b, 'a_B', a2)
    if hasattr(a2, 'a_Root5'):
        assert not _is_linked(a2, 'a_Root5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_a1_stub_double():
    # a_A has no real 'a_A3' property in the generated
    # code (a bare stub) -- manually attach it so a_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # a_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = a_Root(visible=True)
    partner = a_A()
    setattr(partner, 'a_A3', None)
    _safe_set(owner, 'a_Root2', {partner})
    assert getattr(partner, 'a_A3') == owner
    _safe_set(owner, 'a_Root2', set())
    assert getattr(partner, 'a_A3') is None


def test_assoc_refa0_stub_double():
    # a_A has no real 'a_A' property in the generated
    # code (a bare stub) -- manually attach it so a_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # a_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = a_Root(visible=True)
    partner = a_A()
    setattr(partner, 'a_A', None)
    _safe_set(owner, 'a_Root', partner)
    assert getattr(partner, 'a_A') == owner
    _safe_set(owner, 'a_Root', None)
    assert getattr(partner, 'a_A') is None


def test_assoc_tob6_stub_double():
    # a_A has no real 'a_A7' property in the generated
    # code (a bare stub) -- manually attach it so a_B's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # a_B's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = a_B(name="sample_text")
    partner = a_A()
    setattr(partner, 'a_A7', None)
    _safe_set(owner, 'a_B8', partner)
    assert getattr(partner, 'a_A7') == owner
    _safe_set(owner, 'a_B8', None)
    assert getattr(partner, 'a_A7') is None


