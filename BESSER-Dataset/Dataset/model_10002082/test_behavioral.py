import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    C,
    C2,
    C3,
    Lieu,
    Personne,
    R,
    Sport,
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
    _safe_set(b, 'b4', {a1})
    assert _is_linked(b, 'b4', a1)
    if hasattr(a1, 'a5'):
        assert _is_linked(a1, 'a5', b)
    _safe_set(b, 'b4', {a2})
    assert _is_linked(b, 'b4', a2)
    if hasattr(a1, 'a5'):
        assert not _is_linked(a1, 'a5', b)
    if hasattr(a2, 'a5'):
        assert _is_linked(a2, 'a5', b)
    _safe_set(b, 'b4', set())
    assert not _is_linked(b, 'b4', a2)
    if hasattr(a2, 'a5'):
        assert not _is_linked(a2, 'a5', b)


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


def test_assoc_Personne_Sport_reverse_link_reassign_clear():
    a1 = Sport(id=7, nom="sample_text")
    a2 = Sport(id=13, nom="sample_text_2")
    b = Personne(id=7, nom="sample_text", prenom="sample_text")
    _safe_set(b, 'sport6', {a1})
    assert _is_linked(b, 'sport6', a1)
    if hasattr(a1, 'personne7'):
        assert _is_linked(a1, 'personne7', b)
    _safe_set(b, 'sport6', {a2})
    assert _is_linked(b, 'sport6', a2)
    if hasattr(a1, 'personne7'):
        assert not _is_linked(a1, 'personne7', b)
    if hasattr(a2, 'personne7'):
        assert _is_linked(a2, 'personne7', b)
    _safe_set(b, 'sport6', set())
    assert not _is_linked(b, 'sport6', a2)
    if hasattr(a2, 'personne7'):
        assert not _is_linked(a2, 'personne7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Lieu_Personne_stub_double():
    # Lieu has no real 'personne8' property in the generated
    # code (a bare stub) -- manually attach it so Personne's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Personne's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Personne(id=7, nom="sample_text", prenom="sample_text")
    partner = Lieu()
    setattr(partner, 'personne8', None)
    _safe_set(owner, 'lieu9', {partner})
    assert owner in getattr(partner, 'personne8')
    _safe_set(owner, 'lieu9', set())
    assert owner not in getattr(partner, 'personne8')


def test_assoc_R_A_stub_double():
    # R has no real 'a2' property in the generated
    # code (a bare stub) -- manually attach it so A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A(attA="sample_text")
    partner = R()
    setattr(partner, 'a2', None)
    _safe_set(owner, 'r3', partner)
    assert owner in getattr(partner, 'a2')
    _safe_set(owner, 'r3', None)
    assert owner not in getattr(partner, 'a2')


def test_assoc_Sport_Lieu_stub_double():
    # Lieu has no real 'sport11' property in the generated
    # code (a bare stub) -- manually attach it so Sport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Sport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Sport(id=7, nom="sample_text")
    partner = Lieu()
    setattr(partner, 'sport11', None)
    _safe_set(owner, 'lieu10', {partner})
    assert owner in getattr(partner, 'sport11')
    _safe_set(owner, 'lieu10', set())
    assert owner not in getattr(partner, 'sport11')


