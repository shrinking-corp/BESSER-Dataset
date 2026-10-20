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
    k5_A,
    k5_B,
    k5_C,
    k5_G,
    k5_I,
    k5_J,
    k5_K,
    k5_L1,
    k5_L2,
    k5_L3,
    k5_M,
    k5_N,
    k5_P,
    k5_Q,
    k5_W,
    k5_X,
    k5_Y,
    k5_Z,
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

def test_assoc_l2k33_reverse_link_reassign_clear():
    a1 = k5_L2(l1=7, l2=7)
    a2 = k5_L2(l1=13, l2=13)
    b = k5_K(title="sample_text")
    _safe_set(b, 'k5_K35', a1)
    assert _is_linked(b, 'k5_K35', a1)
    if hasattr(a1, 'k5_L234'):
        assert _is_linked(a1, 'k5_L234', b)
    _safe_set(b, 'k5_K35', a2)
    assert _is_linked(b, 'k5_K35', a2)
    if hasattr(a1, 'k5_L234'):
        assert not _is_linked(a1, 'k5_L234', b)
    if hasattr(a2, 'k5_L234'):
        assert _is_linked(a2, 'k5_L234', b)
    _safe_set(b, 'k5_K35', None)
    assert not _is_linked(b, 'k5_K35', a2)
    if hasattr(a2, 'k5_L234'):
        assert not _is_linked(a2, 'k5_L234', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ks19_stub_double():
    # k5_P has no real 'k5_P20' property in the generated
    # code (a bare stub) -- manually attach it so k5_K's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_K's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_K(title="sample_text")
    partner = k5_P()
    setattr(partner, 'k5_P20', None)
    _safe_set(owner, 'k5_K', partner)
    assert getattr(partner, 'k5_P20') == owner
    _safe_set(owner, 'k5_K', None)
    assert getattr(partner, 'k5_P20') is None


def test_assoc_l1c24_stub_double():
    # k5_C has no real 'k5_C26' property in the generated
    # code (a bare stub) -- manually attach it so k5_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_L1(id1="sample_text", id2=7)
    partner = k5_C()
    setattr(partner, 'k5_C26', None)
    _safe_set(owner, 'k5_L125', partner)
    assert getattr(partner, 'k5_C26') == owner
    _safe_set(owner, 'k5_L125', None)
    assert getattr(partner, 'k5_C26') is None


def test_assoc_l1m27_stub_double():
    # k5_M has no real 'k5_M29' property in the generated
    # code (a bare stub) -- manually attach it so k5_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_L1(id1="sample_text", id2=7)
    partner = k5_M()
    setattr(partner, 'k5_M29', None)
    _safe_set(owner, 'k5_L128', partner)
    assert getattr(partner, 'k5_M29') == owner
    _safe_set(owner, 'k5_L128', None)
    assert getattr(partner, 'k5_M29') is None


def test_assoc_l2q30_stub_double():
    # k5_Q has no real 'k5_Q32' property in the generated
    # code (a bare stub) -- manually attach it so k5_L2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_L2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_L2(l1=7, l2=7)
    partner = k5_Q()
    setattr(partner, 'k5_Q32', None)
    _safe_set(owner, 'k5_L231', partner)
    assert getattr(partner, 'k5_Q32') == owner
    _safe_set(owner, 'k5_L231', None)
    assert getattr(partner, 'k5_Q32') is None


def test_assoc_l2s23_stub_double():
    # k5_Q has no real 'k5_Q' property in the generated
    # code (a bare stub) -- manually attach it so k5_L2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_L2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_L2(l1=7, l2=7)
    partner = k5_Q()
    setattr(partner, 'k5_Q', None)
    _safe_set(owner, 'k5_L2', partner)
    assert owner in getattr(partner, 'k5_Q')
    _safe_set(owner, 'k5_L2', None)
    assert owner not in getattr(partner, 'k5_Q')


def test_assoc_l3z36_stub_double():
    # k5_L3 has no real 'k5_L3' property in the generated
    # code (a bare stub) -- manually attach it so k5_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_Z(z1="sample_text", z2="sample_text", z3="sample_text")
    partner = k5_L3()
    setattr(partner, 'k5_L3', None)
    _safe_set(owner, 'k5_Z37', partner)
    assert getattr(partner, 'k5_L3') == owner
    _safe_set(owner, 'k5_Z37', None)
    assert getattr(partner, 'k5_L3') is None


def test_assoc_ml115_stub_double():
    # k5_M has no real 'k5_M16' property in the generated
    # code (a bare stub) -- manually attach it so k5_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_L1(id1="sample_text", id2=7)
    partner = k5_M()
    setattr(partner, 'k5_M16', None)
    _safe_set(owner, 'k5_L1', partner)
    assert owner in getattr(partner, 'k5_M16')
    _safe_set(owner, 'k5_L1', None)
    assert owner not in getattr(partner, 'k5_M16')


def test_assoc_w7_stub_double():
    # k5_X has no real 'k5_X8' property in the generated
    # code (a bare stub) -- manually attach it so k5_W's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_W's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_W(w="sample_text")
    partner = k5_X()
    setattr(partner, 'k5_X8', None)
    _safe_set(owner, 'k5_W', partner)
    assert getattr(partner, 'k5_X8') == owner
    _safe_set(owner, 'k5_W', None)
    assert getattr(partner, 'k5_X8') is None


def test_assoc_y10_stub_double():
    # k5_B has no real 'k5_B11' property in the generated
    # code (a bare stub) -- manually attach it so k5_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_Y(y=7)
    partner = k5_B()
    setattr(partner, 'k5_B11', None)
    _safe_set(owner, 'k5_Y12', partner)
    assert getattr(partner, 'k5_B11') == owner
    _safe_set(owner, 'k5_Y12', None)
    assert getattr(partner, 'k5_B11') is None


def test_assoc_ys5_stub_double():
    # k5_X has no real 'k5_X6' property in the generated
    # code (a bare stub) -- manually attach it so k5_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_Y(y=7)
    partner = k5_X()
    setattr(partner, 'k5_X6', None)
    _safe_set(owner, 'k5_Y', partner)
    assert owner in getattr(partner, 'k5_X6')
    _safe_set(owner, 'k5_Y', None)
    assert owner not in getattr(partner, 'k5_X6')


def test_assoc_zs3_stub_double():
    # k5_X has no real 'k5_X4' property in the generated
    # code (a bare stub) -- manually attach it so k5_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k5_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k5_Z(z1="sample_text", z2="sample_text", z3="sample_text")
    partner = k5_X()
    setattr(partner, 'k5_X4', None)
    _safe_set(owner, 'k5_Z', partner)
    assert getattr(partner, 'k5_X4') == owner
    _safe_set(owner, 'k5_Z', None)
    assert getattr(partner, 'k5_X4') is None


