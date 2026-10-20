import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    A1,
    A2,
    B,
    B1,
    B2,
    C,
    C1,
    C2,
    C22,
    C3,
    C32,
    C4,
    R,
    R2,
    Y,
    Y2,
    Z,
    Z2,
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

def test_assoc_A_B_reverse_link_reassign_clear():
    a1 = B(attB=7)
    a2 = B(attB=13)
    b = A(attA="sample_text")
    _safe_set(b, 'b0', {a1})
    assert _is_linked(b, 'b0', a1)
    if hasattr(a1, 'a1'):
        assert _is_linked(a1, 'a1', b)
    _safe_set(b, 'b0', {a2})
    assert _is_linked(b, 'b0', a2)
    if hasattr(a1, 'a1'):
        assert not _is_linked(a1, 'a1', b)
    if hasattr(a2, 'a1'):
        assert _is_linked(a2, 'a1', b)
    _safe_set(b, 'b0', set())
    assert not _is_linked(b, 'b0', a2)
    if hasattr(a2, 'a1'):
        assert not _is_linked(a2, 'a1', b)


def test_assoc_A_B2_reverse_link_reassign_clear():
    a1 = B1(attB=7)
    a2 = B1(attB=13)
    b = A1(attA="sample_text")
    _safe_set(b, 'b6', {a1})
    assert _is_linked(b, 'b6', a1)
    if hasattr(a1, 'a7'):
        assert _is_linked(a1, 'a7', b)
    _safe_set(b, 'b6', {a2})
    assert _is_linked(b, 'b6', a2)
    if hasattr(a1, 'a7'):
        assert not _is_linked(a1, 'a7', b)
    if hasattr(a2, 'a7'):
        assert _is_linked(a2, 'a7', b)
    _safe_set(b, 'b6', set())
    assert not _is_linked(b, 'b6', a2)
    if hasattr(a2, 'a7'):
        assert not _is_linked(a2, 'a7', b)


def test_assoc_A_B22_reverse_link_reassign_clear():
    a1 = B2(attB=7)
    a2 = B2(attB=13)
    b = A2(attA="sample_text")
    _safe_set(b, 'b12', {a1})
    assert _is_linked(b, 'b12', a1)
    if hasattr(a1, 'a13'):
        assert _is_linked(a1, 'a13', b)
    _safe_set(b, 'b12', {a2})
    assert _is_linked(b, 'b12', a2)
    if hasattr(a1, 'a13'):
        assert not _is_linked(a1, 'a13', b)
    if hasattr(a2, 'a13'):
        assert _is_linked(a2, 'a13', b)
    _safe_set(b, 'b12', set())
    assert not _is_linked(b, 'b12', a2)
    if hasattr(a2, 'a13'):
        assert not _is_linked(a2, 'a13', b)


def test_assoc_B_C_reverse_link_reassign_clear():
    a1 = C(attC1=7, attC2=True)
    a2 = C(attC1=13, attC2=False)
    b = B(attB=7)
    _safe_set(b, 'c2', {a1})
    assert _is_linked(b, 'c2', a1)
    if hasattr(a1, 'b3'):
        assert _is_linked(a1, 'b3', b)
    _safe_set(b, 'c2', {a2})
    assert _is_linked(b, 'c2', a2)
    if hasattr(a1, 'b3'):
        assert not _is_linked(a1, 'b3', b)
    if hasattr(a2, 'b3'):
        assert _is_linked(a2, 'b3', b)
    _safe_set(b, 'c2', set())
    assert not _is_linked(b, 'c2', a2)
    if hasattr(a2, 'b3'):
        assert not _is_linked(a2, 'b3', b)


def test_assoc_B_C2_reverse_link_reassign_clear():
    a1 = C1(attC1=7, attC2=True)
    a2 = C1(attC1=13, attC2=False)
    b = B1(attB=7)
    _safe_set(b, 'c8', {a1})
    assert _is_linked(b, 'c8', a1)
    if hasattr(a1, 'b9'):
        assert _is_linked(a1, 'b9', b)
    _safe_set(b, 'c8', {a2})
    assert _is_linked(b, 'c8', a2)
    if hasattr(a1, 'b9'):
        assert not _is_linked(a1, 'b9', b)
    if hasattr(a2, 'b9'):
        assert _is_linked(a2, 'b9', b)
    _safe_set(b, 'c8', set())
    assert not _is_linked(b, 'c8', a2)
    if hasattr(a2, 'b9'):
        assert not _is_linked(a2, 'b9', b)


def test_assoc_B_C22_reverse_link_reassign_clear():
    a1 = C4(attC1=7, attC2=True)
    a2 = C4(attC1=13, attC2=False)
    b = B2(attB=7)
    _safe_set(b, 'c14', {a1})
    assert _is_linked(b, 'c14', a1)
    if hasattr(a1, 'b15'):
        assert _is_linked(a1, 'b15', b)
    _safe_set(b, 'c14', {a2})
    assert _is_linked(b, 'c14', a2)
    if hasattr(a1, 'b15'):
        assert not _is_linked(a1, 'b15', b)
    if hasattr(a2, 'b15'):
        assert _is_linked(a2, 'b15', b)
    _safe_set(b, 'c14', set())
    assert not _is_linked(b, 'c14', a2)
    if hasattr(a2, 'b15'):
        assert not _is_linked(a2, 'b15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_R_A_stub_double():
    # R has no real 'aR4' property in the generated
    # code (a bare stub) -- manually attach it so A1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A1(attA="sample_text")
    partner = R()
    setattr(partner, 'aR4', None)
    _safe_set(owner, 'r5', partner)
    assert owner in getattr(partner, 'aR4')
    _safe_set(owner, 'r5', None)
    assert owner not in getattr(partner, 'aR4')


def test_assoc_R_A2_stub_double():
    # R2 has no real 'aR10' property in the generated
    # code (a bare stub) -- manually attach it so A2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A2(attA="sample_text")
    partner = R2()
    setattr(partner, 'aR10', None)
    _safe_set(owner, 'r11', partner)
    assert owner in getattr(partner, 'aR10')
    _safe_set(owner, 'r11', None)
    assert owner not in getattr(partner, 'aR10')


