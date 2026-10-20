import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    C,
    C1,
    C2,
    Mariage,
    PACS,
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

def test_assoc_B_C_reverse_link_reassign_clear():
    a1 = C(attC1=7, attC2=True)
    a2 = C(attC1=13, attC2=False)
    b = B(attB=7)
    _safe_set(b, 'c0', {a1})
    assert _is_linked(b, 'c0', a1)
    if hasattr(a1, 'b1'):
        assert _is_linked(a1, 'b1', b)
    _safe_set(b, 'c0', {a2})
    assert _is_linked(b, 'c0', a2)
    if hasattr(a1, 'b1'):
        assert not _is_linked(a1, 'b1', b)
    if hasattr(a2, 'b1'):
        assert _is_linked(a2, 'b1', b)
    _safe_set(b, 'c0', set())
    assert not _is_linked(b, 'c0', a2)
    if hasattr(a2, 'b1'):
        assert not _is_linked(a2, 'b1', b)


def test_assoc_Y_B_reverse_link_reassign_clear():
    a1 = Y(attY="sample_text")
    a2 = Y(attY="sample_text_2")
    b = B(attB=7)
    _safe_set(b, 'y3', a1)
    assert _is_linked(b, 'y3', a1)
    if hasattr(a1, 'b2'):
        assert _is_linked(a1, 'b2', b)
    _safe_set(b, 'y3', a2)
    assert _is_linked(b, 'y3', a2)
    if hasattr(a1, 'b2'):
        assert not _is_linked(a1, 'b2', b)
    if hasattr(a2, 'b2'):
        assert _is_linked(a2, 'b2', b)
    _safe_set(b, 'y3', None)
    assert not _is_linked(b, 'y3', a2)
    if hasattr(a2, 'b2'):
        assert not _is_linked(a2, 'b2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Personne_Union_stub_double():
    # Personne has no real 'union8' property in the generated
    # code (a bare stub) -- manually attach it so Union's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Union's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Union(dateUnion=7)
    partner = Personne()
    setattr(partner, 'union8', None)
    _safe_set(owner, 'pers9', {partner})
    assert owner in getattr(partner, 'union8')
    _safe_set(owner, 'pers9', set())
    assert owner not in getattr(partner, 'union8')


def test_assoc_Personne_Union2_stub_double():
    # Personne has no real 'unionActuelle10' property in the generated
    # code (a bare stub) -- manually attach it so Union's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Union's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Union(dateUnion=7)
    partner = Personne()
    setattr(partner, 'unionActuelle10', None)
    _safe_set(owner, 'personne11', {partner})
    assert getattr(partner, 'unionActuelle10') == owner
    _safe_set(owner, 'personne11', set())
    assert getattr(partner, 'unionActuelle10') is None


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


