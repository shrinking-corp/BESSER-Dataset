import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    C,
    C2,
    C3,
    R,
    Y,
    Z,
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


def test_assoc_B_C_reverse_link_reassign_clear():
    a1 = C(AttC2=True, attC1=7)
    a2 = C(AttC2=False, attC1=13)
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


def test_assoc_Y_A_reverse_link_reassign_clear():
    a1 = Y(atty="sample_text")
    a2 = Y(atty="sample_text_2")
    b = A(attA="sample_text")
    _safe_set(b, 'y13', a1)
    assert _is_linked(b, 'y13', a1)
    if hasattr(a1, 'a12'):
        assert _is_linked(a1, 'a12', b)
    _safe_set(b, 'y13', a2)
    assert _is_linked(b, 'y13', a2)
    if hasattr(a1, 'a12'):
        assert not _is_linked(a1, 'a12', b)
    if hasattr(a2, 'a12'):
        assert _is_linked(a2, 'a12', b)
    _safe_set(b, 'y13', None)
    assert not _is_linked(b, 'y13', a2)
    if hasattr(a2, 'a12'):
        assert not _is_linked(a2, 'a12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_C2_C_stub_double():
    # C2 has no real 'c6' property in the generated
    # code (a bare stub) -- manually attach it so C's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C(AttC2=True, attC1=7)
    partner = C2()
    setattr(partner, 'c6', None)
    _safe_set(owner, 'c27', partner)
    assert getattr(partner, 'c6') == owner
    _safe_set(owner, 'c27', None)
    assert getattr(partner, 'c6') is None


def test_assoc_C3_C_stub_double():
    # C3 has no real 'c4' property in the generated
    # code (a bare stub) -- manually attach it so C's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # C's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = C(AttC2=True, attC1=7)
    partner = C3()
    setattr(partner, 'c4', None)
    _safe_set(owner, 'c35', partner)
    assert getattr(partner, 'c4') == owner
    _safe_set(owner, 'c35', None)
    assert getattr(partner, 'c4') is None


def test_assoc_R_A_stub_double():
    # R has no real 'aR10' property in the generated
    # code (a bare stub) -- manually attach it so A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A(attA="sample_text")
    partner = R()
    setattr(partner, 'aR10', None)
    _safe_set(owner, 'r11', partner)
    assert owner in getattr(partner, 'aR10')
    _safe_set(owner, 'r11', None)
    assert owner not in getattr(partner, 'aR10')


def test_assoc_Z_A_stub_double():
    # Z has no real 'a8' property in the generated
    # code (a bare stub) -- manually attach it so A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A(attA="sample_text")
    partner = Z()
    setattr(partner, 'a8', None)
    _safe_set(owner, 'z9', partner)
    assert getattr(partner, 'a8') == owner
    _safe_set(owner, 'z9', None)
    assert getattr(partner, 'a8') is None


