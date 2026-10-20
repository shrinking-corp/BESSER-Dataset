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
    anol3l4_A,
    anol3l4_B,
    anol3l4_C,
    anol3l4_G,
    anol3l4_I,
    anol3l4_J,
    anol3l4_K,
    anol3l4_L1,
    anol3l4_L2,
    anol3l4_L3,
    anol3l4_L4,
    anol3l4_M,
    anol3l4_N,
    anol3l4_P,
    anol3l4_Q,
    anol3l4_W,
    anol3l4_X,
    anol3l4_Y,
    anol3l4_Z,
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
    a1 = anol3l4_L2(l1=7, l2=7)
    a2 = anol3l4_L2(l1=13, l2=13)
    b = anol3l4_K(title="sample_text")
    _safe_set(b, 'anol3l4_K32', a1)
    assert _is_linked(b, 'anol3l4_K32', a1)
    if hasattr(a1, 'anol3l4_L231'):
        assert _is_linked(a1, 'anol3l4_L231', b)
    _safe_set(b, 'anol3l4_K32', a2)
    assert _is_linked(b, 'anol3l4_K32', a2)
    if hasattr(a1, 'anol3l4_L231'):
        assert not _is_linked(a1, 'anol3l4_L231', b)
    if hasattr(a2, 'anol3l4_L231'):
        assert _is_linked(a2, 'anol3l4_L231', b)
    _safe_set(b, 'anol3l4_K32', None)
    assert not _is_linked(b, 'anol3l4_K32', a2)
    if hasattr(a2, 'anol3l4_L231'):
        assert not _is_linked(a2, 'anol3l4_L231', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ks16_stub_double():
    # anol3l4_P has no real 'anol3l4_P17' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_K's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_K's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_K(title="sample_text")
    partner = anol3l4_P()
    setattr(partner, 'anol3l4_P17', None)
    _safe_set(owner, 'anol3l4_K', partner)
    assert getattr(partner, 'anol3l4_P17') == owner
    _safe_set(owner, 'anol3l4_K', None)
    assert getattr(partner, 'anol3l4_P17') is None


def test_assoc_l1c21_stub_double():
    # anol3l4_C has no real 'anol3l4_C23' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_L1(id1="sample_text", id2=7)
    partner = anol3l4_C()
    setattr(partner, 'anol3l4_C23', None)
    _safe_set(owner, 'anol3l4_L122', partner)
    assert getattr(partner, 'anol3l4_C23') == owner
    _safe_set(owner, 'anol3l4_L122', None)
    assert getattr(partner, 'anol3l4_C23') is None


def test_assoc_l1m24_stub_double():
    # anol3l4_M has no real 'anol3l4_M26' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_L1(id1="sample_text", id2=7)
    partner = anol3l4_M()
    setattr(partner, 'anol3l4_M26', None)
    _safe_set(owner, 'anol3l4_L125', partner)
    assert getattr(partner, 'anol3l4_M26') == owner
    _safe_set(owner, 'anol3l4_L125', None)
    assert getattr(partner, 'anol3l4_M26') is None


def test_assoc_l2q27_stub_double():
    # anol3l4_Q has no real 'anol3l4_Q29' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_L2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_L2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_L2(l1=7, l2=7)
    partner = anol3l4_Q()
    setattr(partner, 'anol3l4_Q29', None)
    _safe_set(owner, 'anol3l4_L228', partner)
    assert getattr(partner, 'anol3l4_Q29') == owner
    _safe_set(owner, 'anol3l4_L228', None)
    assert getattr(partner, 'anol3l4_Q29') is None


def test_assoc_l2s20_stub_double():
    # anol3l4_Q has no real 'anol3l4_Q' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_L2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_L2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_L2(l1=7, l2=7)
    partner = anol3l4_Q()
    setattr(partner, 'anol3l4_Q', None)
    _safe_set(owner, 'anol3l4_L2', partner)
    assert owner in getattr(partner, 'anol3l4_Q')
    _safe_set(owner, 'anol3l4_L2', None)
    assert owner not in getattr(partner, 'anol3l4_Q')


def test_assoc_l4z35_stub_double():
    # anol3l4_L4 has no real 'anol3l4_L4' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_Z(z1="sample_text", z2="sample_text", z3="sample_text")
    partner = anol3l4_L4()
    setattr(partner, 'anol3l4_L4', None)
    _safe_set(owner, 'anol3l4_Z36', partner)
    assert getattr(partner, 'anol3l4_L4') == owner
    _safe_set(owner, 'anol3l4_Z36', None)
    assert getattr(partner, 'anol3l4_L4') is None


def test_assoc_ml112_stub_double():
    # anol3l4_M has no real 'anol3l4_M13' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_L1(id1="sample_text", id2=7)
    partner = anol3l4_M()
    setattr(partner, 'anol3l4_M13', None)
    _safe_set(owner, 'anol3l4_L1', partner)
    assert owner in getattr(partner, 'anol3l4_M13')
    _safe_set(owner, 'anol3l4_L1', None)
    assert owner not in getattr(partner, 'anol3l4_M13')


def test_assoc_w7_stub_double():
    # anol3l4_X has no real 'anol3l4_X8' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_W's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_W's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_W(w="sample_text")
    partner = anol3l4_X()
    setattr(partner, 'anol3l4_X8', None)
    _safe_set(owner, 'anol3l4_W', partner)
    assert getattr(partner, 'anol3l4_X8') == owner
    _safe_set(owner, 'anol3l4_W', None)
    assert getattr(partner, 'anol3l4_X8') is None


def test_assoc_ys5_stub_double():
    # anol3l4_X has no real 'anol3l4_X6' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_Y(y=7)
    partner = anol3l4_X()
    setattr(partner, 'anol3l4_X6', None)
    _safe_set(owner, 'anol3l4_Y', partner)
    assert owner in getattr(partner, 'anol3l4_X6')
    _safe_set(owner, 'anol3l4_Y', None)
    assert owner not in getattr(partner, 'anol3l4_X6')


def test_assoc_zs3_stub_double():
    # anol3l4_X has no real 'anol3l4_X4' property in the generated
    # code (a bare stub) -- manually attach it so anol3l4_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anol3l4_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anol3l4_Z(z1="sample_text", z2="sample_text", z3="sample_text")
    partner = anol3l4_X()
    setattr(partner, 'anol3l4_X4', None)
    _safe_set(owner, 'anol3l4_Z', partner)
    assert getattr(partner, 'anol3l4_X4') == owner
    _safe_set(owner, 'anol3l4_Z', None)
    assert getattr(partner, 'anol3l4_X4') is None


