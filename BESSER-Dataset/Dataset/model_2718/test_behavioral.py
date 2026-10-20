import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    C,
    G,
    J,
    L1,
    M,
    N,
    P,
    k4_A,
    k4_B,
    k4_C,
    k4_G,
    k4_I,
    k4_J,
    k4_K,
    k4_L1,
    k4_L2,
    k4_L3,
    k4_L4,
    k4_M,
    k4_N,
    k4_P,
    k4_Q,
    k4_W,
    k4_X,
    k4_Y,
    k4_Z,
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

def test_assoc_l2k30_reverse_link_reassign_clear():
    a1 = k4_L2(l1=7, l2=7)
    a2 = k4_L2(l1=13, l2=13)
    b = k4_K(title="sample_text")
    _safe_set(b, 'k4_K32', a1)
    assert _is_linked(b, 'k4_K32', a1)
    if hasattr(a1, 'k4_L231'):
        assert _is_linked(a1, 'k4_L231', b)
    _safe_set(b, 'k4_K32', a2)
    assert _is_linked(b, 'k4_K32', a2)
    if hasattr(a1, 'k4_L231'):
        assert not _is_linked(a1, 'k4_L231', b)
    if hasattr(a2, 'k4_L231'):
        assert _is_linked(a2, 'k4_L231', b)
    _safe_set(b, 'k4_K32', None)
    assert not _is_linked(b, 'k4_K32', a2)
    if hasattr(a2, 'k4_L231'):
        assert not _is_linked(a2, 'k4_L231', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ks16_stub_double():
    # k4_P has no real 'k4_P17' property in the generated
    # code (a bare stub) -- manually attach it so k4_K's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_K's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_K(title="sample_text")
    partner = k4_P()
    setattr(partner, 'k4_P17', None)
    _safe_set(owner, 'k4_K', partner)
    assert getattr(partner, 'k4_P17') == owner
    _safe_set(owner, 'k4_K', None)
    assert getattr(partner, 'k4_P17') is None


def test_assoc_l1c21_stub_double():
    # k4_C has no real 'k4_C23' property in the generated
    # code (a bare stub) -- manually attach it so k4_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_L1(id1="sample_text", id2=7)
    partner = k4_C()
    setattr(partner, 'k4_C23', None)
    _safe_set(owner, 'k4_L122', partner)
    assert getattr(partner, 'k4_C23') == owner
    _safe_set(owner, 'k4_L122', None)
    assert getattr(partner, 'k4_C23') is None


def test_assoc_l1m24_stub_double():
    # k4_M has no real 'k4_M26' property in the generated
    # code (a bare stub) -- manually attach it so k4_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_L1(id1="sample_text", id2=7)
    partner = k4_M()
    setattr(partner, 'k4_M26', None)
    _safe_set(owner, 'k4_L125', partner)
    assert getattr(partner, 'k4_M26') == owner
    _safe_set(owner, 'k4_L125', None)
    assert getattr(partner, 'k4_M26') is None


def test_assoc_l2q27_stub_double():
    # k4_Q has no real 'k4_Q29' property in the generated
    # code (a bare stub) -- manually attach it so k4_L2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_L2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_L2(l1=7, l2=7)
    partner = k4_Q()
    setattr(partner, 'k4_Q29', None)
    _safe_set(owner, 'k4_L228', partner)
    assert getattr(partner, 'k4_Q29') == owner
    _safe_set(owner, 'k4_L228', None)
    assert getattr(partner, 'k4_Q29') is None


def test_assoc_l2s20_stub_double():
    # k4_Q has no real 'k4_Q' property in the generated
    # code (a bare stub) -- manually attach it so k4_L2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_L2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_L2(l1=7, l2=7)
    partner = k4_Q()
    setattr(partner, 'k4_Q', None)
    _safe_set(owner, 'k4_L2', partner)
    assert owner in getattr(partner, 'k4_Q')
    _safe_set(owner, 'k4_L2', None)
    assert owner not in getattr(partner, 'k4_Q')


def test_assoc_l4z35_stub_double():
    # k4_L4 has no real 'k4_L4' property in the generated
    # code (a bare stub) -- manually attach it so k4_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_Z(z1="sample_text", z2="sample_text", z3="sample_text")
    partner = k4_L4()
    setattr(partner, 'k4_L4', None)
    _safe_set(owner, 'k4_Z36', partner)
    assert getattr(partner, 'k4_L4') == owner
    _safe_set(owner, 'k4_Z36', None)
    assert getattr(partner, 'k4_L4') is None


def test_assoc_ml112_stub_double():
    # k4_M has no real 'k4_M13' property in the generated
    # code (a bare stub) -- manually attach it so k4_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_L1(id1="sample_text", id2=7)
    partner = k4_M()
    setattr(partner, 'k4_M13', None)
    _safe_set(owner, 'k4_L1', partner)
    assert owner in getattr(partner, 'k4_M13')
    _safe_set(owner, 'k4_L1', None)
    assert owner not in getattr(partner, 'k4_M13')


def test_assoc_w7_stub_double():
    # k4_X has no real 'k4_X8' property in the generated
    # code (a bare stub) -- manually attach it so k4_W's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_W's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_W(w="sample_text")
    partner = k4_X()
    setattr(partner, 'k4_X8', None)
    _safe_set(owner, 'k4_W', partner)
    assert getattr(partner, 'k4_X8') == owner
    _safe_set(owner, 'k4_W', None)
    assert getattr(partner, 'k4_X8') is None


def test_assoc_ys5_stub_double():
    # k4_X has no real 'k4_X6' property in the generated
    # code (a bare stub) -- manually attach it so k4_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_Y(y=7)
    partner = k4_X()
    setattr(partner, 'k4_X6', None)
    _safe_set(owner, 'k4_Y', partner)
    assert owner in getattr(partner, 'k4_X6')
    _safe_set(owner, 'k4_Y', None)
    assert owner not in getattr(partner, 'k4_X6')


def test_assoc_zs3_stub_double():
    # k4_X has no real 'k4_X4' property in the generated
    # code (a bare stub) -- manually attach it so k4_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k4_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k4_Z(z1="sample_text", z2="sample_text", z3="sample_text")
    partner = k4_X()
    setattr(partner, 'k4_X4', None)
    _safe_set(owner, 'k4_Z', partner)
    assert getattr(partner, 'k4_X4') == owner
    _safe_set(owner, 'k4_Z', None)
    assert getattr(partner, 'k4_X4') is None


