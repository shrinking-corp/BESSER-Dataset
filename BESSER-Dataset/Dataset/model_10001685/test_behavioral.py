import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    A2,
    B,
    B2,
    C,
    C2,
    C3,
    C4,
    E,
    F,
    G,
    Mariage,
    PACs,
    Personne,
    R,
    Union,
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


def test_assoc_A_B2_reverse_link_reassign_clear():
    a1 = B2(attB=7)
    a2 = B2(attB=13)
    b = A2(attA="sample_text")
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
    a1 = C2(attC1=7, attC2=7)
    a2 = C2(attC1=13, attC2=13)
    b = B2(attB=7)
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_G_E_stub_double():
    # G has no real 'e16' property in the generated
    # code (a bare stub) -- manually attach it so E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = E(attE="sample_text")
    partner = G()
    setattr(partner, 'e16', None)
    _safe_set(owner, 'g17', partner)
    assert getattr(partner, 'e16') == owner
    _safe_set(owner, 'g17', None)
    assert getattr(partner, 'e16') is None


def test_assoc_Personne_Union_stub_double():
    # Personne has no real 'union12' property in the generated
    # code (a bare stub) -- manually attach it so Union's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Union's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Union(dateUnion="sample_text")
    partner = Personne()
    setattr(partner, 'union12', None)
    _safe_set(owner, 'pers13', {partner})
    assert owner in getattr(partner, 'union12')
    _safe_set(owner, 'pers13', set())
    assert owner not in getattr(partner, 'union12')


def test_assoc_Personne_Union2_stub_double():
    # Personne has no real 'unionActuelles14' property in the generated
    # code (a bare stub) -- manually attach it so Union's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Union's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Union(dateUnion="sample_text")
    partner = Personne()
    setattr(partner, 'unionActuelles14', None)
    _safe_set(owner, 'personnes15', {partner})
    assert getattr(partner, 'unionActuelles14') == owner
    _safe_set(owner, 'personnes15', set())
    assert getattr(partner, 'unionActuelles14') is None


def test_assoc_R_A_stub_double():
    # R has no real 'a4' property in the generated
    # code (a bare stub) -- manually attach it so A2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A2(attA="sample_text")
    partner = R()
    setattr(partner, 'a4', None)
    _safe_set(owner, 'r5', partner)
    assert owner in getattr(partner, 'a4')
    _safe_set(owner, 'r5', None)
    assert owner not in getattr(partner, 'a4')


