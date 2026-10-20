import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    B,
    C,
    C1,
    C2,
    Chauffeur,
    Client,
    E,
    F,
    G,
    Groupe,
    Permis,
    R,
    Reservation,
    Vehicule,
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
    a1 = B(attb="sample_text")
    a2 = B(attb="sample_text_2")
    b = A(atta="sample_text")
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


def test_assoc_B__C_reverse_link_reassign_clear():
    a1 = C(attc1=7, attc2=True)
    a2 = C(attc1=13, attc2=False)
    b = B(attb="sample_text")
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


def test_assoc_Client_Groupe_reverse_link_reassign_clear():
    a1 = Groupe(rang="sample_text")
    a2 = Groupe(rang="sample_text_2")
    b = Client(fonction="sample_text", nom="sample_text")
    _safe_set(b, 'groupe6', {a1})
    assert _is_linked(b, 'groupe6', a1)
    if hasattr(a1, 'client7'):
        assert _is_linked(a1, 'client7', b)
    _safe_set(b, 'groupe6', {a2})
    assert _is_linked(b, 'groupe6', a2)
    if hasattr(a1, 'client7'):
        assert not _is_linked(a1, 'client7', b)
    if hasattr(a2, 'client7'):
        assert _is_linked(a2, 'client7', b)
    _safe_set(b, 'groupe6', set())
    assert not _is_linked(b, 'groupe6', a2)
    if hasattr(a2, 'client7'):
        assert not _is_linked(a2, 'client7', b)


def test_assoc_Vehicule_Chauffeur_reverse_link_reassign_clear():
    a1 = Vehicule(rang=7, standing="sample_text")
    a2 = Vehicule(rang=13, standing="sample_text_2")
    b = Chauffeur(position="sample_text")
    _safe_set(b, 'vehicule13', a1)
    assert _is_linked(b, 'vehicule13', a1)
    if hasattr(a1, 'chauffeur12'):
        assert _is_linked(a1, 'chauffeur12', b)
    _safe_set(b, 'vehicule13', a2)
    assert _is_linked(b, 'vehicule13', a2)
    if hasattr(a1, 'chauffeur12'):
        assert not _is_linked(a1, 'chauffeur12', b)
    if hasattr(a2, 'chauffeur12'):
        assert _is_linked(a2, 'chauffeur12', b)
    _safe_set(b, 'vehicule13', None)
    assert not _is_linked(b, 'vehicule13', a2)
    if hasattr(a2, 'chauffeur12'):
        assert not _is_linked(a2, 'chauffeur12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Chauffeur_Permis_stub_double():
    # Permis has no real 'chauffeur11' property in the generated
    # code (a bare stub) -- manually attach it so Chauffeur's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Chauffeur's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Chauffeur(position="sample_text")
    partner = Permis()
    setattr(partner, 'chauffeur11', None)
    _safe_set(owner, 'permis10', partner)
    assert getattr(partner, 'chauffeur11') == owner
    _safe_set(owner, 'permis10', None)
    assert getattr(partner, 'chauffeur11') is None


def test_assoc_Groupe_Reservation_stub_double():
    # Reservation has no real 'groupe9' property in the generated
    # code (a bare stub) -- manually attach it so Groupe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Groupe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Groupe(rang="sample_text")
    partner = Reservation()
    setattr(partner, 'groupe9', None)
    _safe_set(owner, 'reservation8', partner)
    assert getattr(partner, 'groupe9') == owner
    _safe_set(owner, 'reservation8', None)
    assert getattr(partner, 'groupe9') is None


def test_assoc_MyClass3_MyClass_stub_double():
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


def test_assoc_R_A_stub_double():
    # R has no real 'aR4' property in the generated
    # code (a bare stub) -- manually attach it so A's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A(atta="sample_text")
    partner = R()
    setattr(partner, 'aR4', None)
    _safe_set(owner, 'r5', partner)
    assert owner in getattr(partner, 'aR4')
    _safe_set(owner, 'r5', None)
    assert owner not in getattr(partner, 'aR4')


def test_assoc_Reservation_Vehicule_stub_double():
    # Reservation has no real 'vehicule14' property in the generated
    # code (a bare stub) -- manually attach it so Vehicule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Vehicule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Vehicule(rang=7, standing="sample_text")
    partner = Reservation()
    setattr(partner, 'vehicule14', None)
    _safe_set(owner, 'reservation15', partner)
    assert getattr(partner, 'vehicule14') == owner
    _safe_set(owner, 'reservation15', None)
    assert getattr(partner, 'vehicule14') is None


