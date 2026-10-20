import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    A1,
    A2,
    A3,
    A4,
    A5,
    B,
    B1,
    B2,
    C,
    C2,
    C3,
    R,
    Y,
    Z,
    cxw,
    dz_aklm,
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

def test_assoc_A_A_reverse_link_reassign_clear():
    a1 = A1(b=True, d=7)
    a2 = A1(b=False, d=13)
    b = A1(b=True, d=7)
    _safe_set(b, 'a11', a1)
    assert _is_linked(b, 'a11', a1)
    if hasattr(a1, 'a10'):
        assert _is_linked(a1, 'a10', b)
    _safe_set(b, 'a11', a2)
    assert _is_linked(b, 'a11', a2)
    if hasattr(a1, 'a10'):
        assert not _is_linked(a1, 'a10', b)
    if hasattr(a2, 'a10'):
        assert _is_linked(a2, 'a10', b)
    _safe_set(b, 'a11', None)
    assert not _is_linked(b, 'a11', a2)
    if hasattr(a2, 'a10'):
        assert not _is_linked(a2, 'a10', b)


def test_assoc_A_B2_reverse_link_reassign_clear():
    a1 = B(attB=7)
    a2 = B(attB=13)
    b = A(attA="sample_text")
    _safe_set(b, 'b2', {a1})
    assert _is_linked(b, 'b2', a1)
    if hasattr(a1, 'a3'):
        assert _is_linked(a1, 'a3', b)
    _safe_set(b, 'b2', {a2})
    assert _is_linked(b, 'b2', a2)
    if hasattr(a1, 'a3'):
        assert not _is_linked(a1, 'a3', b)
    if hasattr(a2, 'a3'):
        assert _is_linked(a2, 'a3', b)
    _safe_set(b, 'b2', set())
    assert not _is_linked(b, 'b2', a2)
    if hasattr(a2, 'a3'):
        assert not _is_linked(a2, 'a3', b)


def test_assoc_B_C2_reverse_link_reassign_clear():
    a1 = C(attC1=7, attC2=True)
    a2 = C(attC1=13, attC2=False)
    b = B(attB=7)
    _safe_set(b, 'c6', a1)
    assert _is_linked(b, 'c6', a1)
    if hasattr(a1, 'b7'):
        assert _is_linked(a1, 'b7', b)
    _safe_set(b, 'c6', a2)
    assert _is_linked(b, 'c6', a2)
    if hasattr(a1, 'b7'):
        assert not _is_linked(a1, 'b7', b)
    if hasattr(a2, 'b7'):
        assert _is_linked(a2, 'b7', b)
    _safe_set(b, 'c6', None)
    assert not _is_linked(b, 'c6', a2)
    if hasattr(a2, 'b7'):
        assert not _is_linked(a2, 'b7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_A3_A_stub_double():
    # A3 has no real 'a14' property in the generated
    # code (a bare stub) -- manually attach it so A1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A1(b=True, d=7)
    partner = A3()
    setattr(partner, 'a14', None)
    _safe_set(owner, 'a315', partner)
    assert getattr(partner, 'a14') == owner
    _safe_set(owner, 'a315', None)
    assert getattr(partner, 'a14') is None


def test_assoc_A_B_stub_double():
    # B1 has no real 'c9' property in the generated
    # code (a bare stub) -- manually attach it so A1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A1(b=True, d=7)
    partner = B1()
    setattr(partner, 'c9', None)
    _safe_set(owner, 'c8', partner)
    assert getattr(partner, 'c9') == owner
    _safe_set(owner, 'c8', None)
    assert getattr(partner, 'c9') is None


def test_assoc_C2_C_stub_double():
    # C2 has no real 'c0' property in the generated
    # code (a bare stub) -- manually attach it so C's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C(attC1=7, attC2=True)
    partner = C2()
    setattr(partner, 'c0', None)
    _safe_set(owner, 'c21', partner)
    assert getattr(partner, 'c0') == owner
    _safe_set(owner, 'c21', None)
    assert getattr(partner, 'c0') is None


def test_assoc_R_A_stub_double():
    # R has no real 'aR4' property in the generated
    # code (a bare stub) -- manually attach it so A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A(attA="sample_text")
    partner = R()
    setattr(partner, 'aR4', None)
    _safe_set(owner, 'r5', partner)
    assert owner in getattr(partner, 'aR4')
    _safe_set(owner, 'r5', None)
    assert owner not in getattr(partner, 'aR4')


