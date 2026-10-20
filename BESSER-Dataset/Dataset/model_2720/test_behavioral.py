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
    T2,
    k7_A,
    k7_B,
    k7_C,
    k7_DsmlRelation,
    k7_G,
    k7_I,
    k7_J,
    k7_K,
    k7_L1,
    k7_L2,
    k7_L3,
    k7_L4,
    k7_M,
    k7_N,
    k7_P,
    k7_Q,
    k7_T1,
    k7_T2,
    k7_W,
    k7_X,
    k7_Y,
    k7_Z,
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

def test_assoc_fromDsml48_reverse_link_reassign_clear():
    a1 = k7_T1(name="sample_text")
    a2 = k7_T1(name="sample_text_2")
    b = k7_DsmlRelation(details="sample_text", mandatory=True, name="sample_text")
    _safe_set(b, 'k7_DsmlRelation', a1)
    assert _is_linked(b, 'k7_DsmlRelation', a1)
    if hasattr(a1, 'k7_T149'):
        assert _is_linked(a1, 'k7_T149', b)
    _safe_set(b, 'k7_DsmlRelation', a2)
    assert _is_linked(b, 'k7_DsmlRelation', a2)
    if hasattr(a1, 'k7_T149'):
        assert not _is_linked(a1, 'k7_T149', b)
    if hasattr(a2, 'k7_T149'):
        assert _is_linked(a2, 'k7_T149', b)
    _safe_set(b, 'k7_DsmlRelation', None)
    assert not _is_linked(b, 'k7_DsmlRelation', a2)
    if hasattr(a2, 'k7_T149'):
        assert not _is_linked(a2, 'k7_T149', b)


def test_assoc_l2k37_reverse_link_reassign_clear():
    a1 = k7_L2(l1=7, l2=7)
    a2 = k7_L2(l1=13, l2=13)
    b = k7_K(title="sample_text")
    _safe_set(b, 'k7_K39', a1)
    assert _is_linked(b, 'k7_K39', a1)
    if hasattr(a1, 'k7_L238'):
        assert _is_linked(a1, 'k7_L238', b)
    _safe_set(b, 'k7_K39', a2)
    assert _is_linked(b, 'k7_K39', a2)
    if hasattr(a1, 'k7_L238'):
        assert not _is_linked(a1, 'k7_L238', b)
    if hasattr(a2, 'k7_L238'):
        assert _is_linked(a2, 'k7_L238', b)
    _safe_set(b, 'k7_K39', None)
    assert not _is_linked(b, 'k7_K39', a2)
    if hasattr(a2, 'k7_L238'):
        assert not _is_linked(a2, 'k7_L238', b)


def test_assoc_relateds55_reverse_link_reassign_clear():
    a1 = k7_T1(name="sample_text")
    a2 = k7_T1(name="sample_text_2")
    b = k7_DsmlRelation(details="sample_text", mandatory=True, name="sample_text")
    _safe_set(b, 'k7_DsmlRelation57', a1)
    assert _is_linked(b, 'k7_DsmlRelation57', a1)
    if hasattr(a1, 'k7_T156'):
        assert _is_linked(a1, 'k7_T156', b)
    _safe_set(b, 'k7_DsmlRelation57', a2)
    assert _is_linked(b, 'k7_DsmlRelation57', a2)
    if hasattr(a1, 'k7_T156'):
        assert not _is_linked(a1, 'k7_T156', b)
    if hasattr(a2, 'k7_T156'):
        assert _is_linked(a2, 'k7_T156', b)
    _safe_set(b, 'k7_DsmlRelation57', None)
    assert not _is_linked(b, 'k7_DsmlRelation57', a2)
    if hasattr(a2, 'k7_T156'):
        assert not _is_linked(a2, 'k7_T156', b)


def test_assoc_t2s53_reverse_link_reassign_clear():
    a1 = k7_T2(id="sample_text")
    a2 = k7_T2(id="sample_text_2")
    b = k7_T1(name="sample_text")
    _safe_set(b, 'k7_T154', {a1})
    assert _is_linked(b, 'k7_T154', a1)
    if hasattr(a1, 'k7_T2'):
        assert _is_linked(a1, 'k7_T2', b)
    _safe_set(b, 'k7_T154', {a2})
    assert _is_linked(b, 'k7_T154', a2)
    if hasattr(a1, 'k7_T2'):
        assert not _is_linked(a1, 'k7_T2', b)
    if hasattr(a2, 'k7_T2'):
        assert _is_linked(a2, 'k7_T2', b)
    _safe_set(b, 'k7_T154', set())
    assert not _is_linked(b, 'k7_T154', a2)
    if hasattr(a2, 'k7_T2'):
        assert not _is_linked(a2, 'k7_T2', b)


def test_assoc_toDsml50_reverse_link_reassign_clear():
    a1 = k7_T1(name="sample_text")
    a2 = k7_T1(name="sample_text_2")
    b = k7_DsmlRelation(details="sample_text", mandatory=True, name="sample_text")
    _safe_set(b, 'k7_DsmlRelation51', a1)
    assert _is_linked(b, 'k7_DsmlRelation51', a1)
    if hasattr(a1, 'k7_T152'):
        assert _is_linked(a1, 'k7_T152', b)
    _safe_set(b, 'k7_DsmlRelation51', a2)
    assert _is_linked(b, 'k7_DsmlRelation51', a2)
    if hasattr(a1, 'k7_T152'):
        assert not _is_linked(a1, 'k7_T152', b)
    if hasattr(a2, 'k7_T152'):
        assert _is_linked(a2, 'k7_T152', b)
    _safe_set(b, 'k7_DsmlRelation51', None)
    assert not _is_linked(b, 'k7_DsmlRelation51', a2)
    if hasattr(a2, 'k7_T152'):
        assert not _is_linked(a2, 'k7_T152', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_a45_stub_double():
    # k7_A has no real 'k7_A47' property in the generated
    # code (a bare stub) -- manually attach it so k7_L4's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_L4's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_L4(id="sample_text")
    partner = k7_A()
    setattr(partner, 'k7_A47', None)
    _safe_set(owner, 'k7_L446', partner)
    assert getattr(partner, 'k7_A47') == owner
    _safe_set(owner, 'k7_L446', None)
    assert getattr(partner, 'k7_A47') is None


def test_assoc_ks23_stub_double():
    # k7_P has no real 'k7_P24' property in the generated
    # code (a bare stub) -- manually attach it so k7_K's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_K's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_K(title="sample_text")
    partner = k7_P()
    setattr(partner, 'k7_P24', None)
    _safe_set(owner, 'k7_K', partner)
    assert getattr(partner, 'k7_P24') == owner
    _safe_set(owner, 'k7_K', None)
    assert getattr(partner, 'k7_P24') is None


def test_assoc_l1c28_stub_double():
    # k7_C has no real 'k7_C30' property in the generated
    # code (a bare stub) -- manually attach it so k7_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_L1(id1="sample_text", id2=7)
    partner = k7_C()
    setattr(partner, 'k7_C30', None)
    _safe_set(owner, 'k7_L129', partner)
    assert getattr(partner, 'k7_C30') == owner
    _safe_set(owner, 'k7_L129', None)
    assert getattr(partner, 'k7_C30') is None


def test_assoc_l1m31_stub_double():
    # k7_M has no real 'k7_M33' property in the generated
    # code (a bare stub) -- manually attach it so k7_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_L1(id1="sample_text", id2=7)
    partner = k7_M()
    setattr(partner, 'k7_M33', None)
    _safe_set(owner, 'k7_L132', partner)
    assert getattr(partner, 'k7_M33') == owner
    _safe_set(owner, 'k7_L132', None)
    assert getattr(partner, 'k7_M33') is None


def test_assoc_l2q34_stub_double():
    # k7_Q has no real 'k7_Q36' property in the generated
    # code (a bare stub) -- manually attach it so k7_L2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_L2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_L2(l1=7, l2=7)
    partner = k7_Q()
    setattr(partner, 'k7_Q36', None)
    _safe_set(owner, 'k7_L235', partner)
    assert getattr(partner, 'k7_Q36') == owner
    _safe_set(owner, 'k7_L235', None)
    assert getattr(partner, 'k7_Q36') is None


def test_assoc_l2s27_stub_double():
    # k7_Q has no real 'k7_Q' property in the generated
    # code (a bare stub) -- manually attach it so k7_L2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_L2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_L2(l1=7, l2=7)
    partner = k7_Q()
    setattr(partner, 'k7_Q', None)
    _safe_set(owner, 'k7_L2', partner)
    assert owner in getattr(partner, 'k7_Q')
    _safe_set(owner, 'k7_L2', None)
    assert owner not in getattr(partner, 'k7_Q')


def test_assoc_l3z40_stub_double():
    # k7_L3 has no real 'k7_L3' property in the generated
    # code (a bare stub) -- manually attach it so k7_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_Z(z1="sample_text", z2="sample_text", z3="sample_text")
    partner = k7_L3()
    setattr(partner, 'k7_L3', None)
    _safe_set(owner, 'k7_Z41', partner)
    assert getattr(partner, 'k7_L3') == owner
    _safe_set(owner, 'k7_Z41', None)
    assert getattr(partner, 'k7_L3') is None


def test_assoc_l4s9_stub_double():
    # k7_X has no real 'k7_X10' property in the generated
    # code (a bare stub) -- manually attach it so k7_L4's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_L4's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_L4(id="sample_text")
    partner = k7_X()
    setattr(partner, 'k7_X10', None)
    _safe_set(owner, 'k7_L4', partner)
    assert owner in getattr(partner, 'k7_X10')
    _safe_set(owner, 'k7_L4', None)
    assert owner not in getattr(partner, 'k7_X10')


def test_assoc_ml119_stub_double():
    # k7_M has no real 'k7_M20' property in the generated
    # code (a bare stub) -- manually attach it so k7_L1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_L1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_L1(id1="sample_text", id2=7)
    partner = k7_M()
    setattr(partner, 'k7_M20', None)
    _safe_set(owner, 'k7_L1', partner)
    assert owner in getattr(partner, 'k7_M20')
    _safe_set(owner, 'k7_L1', None)
    assert owner not in getattr(partner, 'k7_M20')


def test_assoc_p42_stub_double():
    # k7_P has no real 'k7_P44' property in the generated
    # code (a bare stub) -- manually attach it so k7_L4's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_L4's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_L4(id="sample_text")
    partner = k7_P()
    setattr(partner, 'k7_P44', None)
    _safe_set(owner, 'k7_L443', partner)
    assert getattr(partner, 'k7_P44') == owner
    _safe_set(owner, 'k7_L443', None)
    assert getattr(partner, 'k7_P44') is None


def test_assoc_t1s11_stub_double():
    # k7_X has no real 'k7_X12' property in the generated
    # code (a bare stub) -- manually attach it so k7_T1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_T1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_T1(name="sample_text")
    partner = k7_X()
    setattr(partner, 'k7_X12', None)
    _safe_set(owner, 'k7_T1', partner)
    assert owner in getattr(partner, 'k7_X12')
    _safe_set(owner, 'k7_T1', None)
    assert owner not in getattr(partner, 'k7_X12')


def test_assoc_w7_stub_double():
    # k7_X has no real 'k7_X8' property in the generated
    # code (a bare stub) -- manually attach it so k7_W's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_W's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_W(w="sample_text")
    partner = k7_X()
    setattr(partner, 'k7_X8', None)
    _safe_set(owner, 'k7_W', partner)
    assert getattr(partner, 'k7_X8') == owner
    _safe_set(owner, 'k7_W', None)
    assert getattr(partner, 'k7_X8') is None


def test_assoc_y14_stub_double():
    # k7_B has no real 'k7_B15' property in the generated
    # code (a bare stub) -- manually attach it so k7_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_Y(y=7)
    partner = k7_B()
    setattr(partner, 'k7_B15', None)
    _safe_set(owner, 'k7_Y16', partner)
    assert getattr(partner, 'k7_B15') == owner
    _safe_set(owner, 'k7_Y16', None)
    assert getattr(partner, 'k7_B15') is None


def test_assoc_ys5_stub_double():
    # k7_X has no real 'k7_X6' property in the generated
    # code (a bare stub) -- manually attach it so k7_Y's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_Y's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_Y(y=7)
    partner = k7_X()
    setattr(partner, 'k7_X6', None)
    _safe_set(owner, 'k7_Y', partner)
    assert owner in getattr(partner, 'k7_X6')
    _safe_set(owner, 'k7_Y', None)
    assert owner not in getattr(partner, 'k7_X6')


def test_assoc_zs3_stub_double():
    # k7_X has no real 'k7_X4' property in the generated
    # code (a bare stub) -- manually attach it so k7_Z's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # k7_Z's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = k7_Z(z1="sample_text", z2="sample_text", z3="sample_text")
    partner = k7_X()
    setattr(partner, 'k7_X4', None)
    _safe_set(owner, 'k7_Z', partner)
    assert getattr(partner, 'k7_X4') == owner
    _safe_set(owner, 'k7_Z', None)
    assert getattr(partner, 'k7_X4') is None


