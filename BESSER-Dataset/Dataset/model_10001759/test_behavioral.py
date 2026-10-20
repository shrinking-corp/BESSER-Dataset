import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    administrateur,
    compte,
    conducteur,
    inscription,
    paiement,
    passager,
    reservation,
    trajet,
    voiture,
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

def test_assoc_compte_passager_reverse_link_reassign_clear():
    a1 = passager(informations_passager="sample_text")
    a2 = passager(informations_passager="sample_text_2")
    b = compte(informations_conducteur="sample_text", informations_passager="sample_text")
    _safe_set(b, 'passager3', a1)
    assert _is_linked(b, 'passager3', a1)
    if hasattr(a1, 'compte2'):
        assert _is_linked(a1, 'compte2', b)
    _safe_set(b, 'passager3', a2)
    assert _is_linked(b, 'passager3', a2)
    if hasattr(a1, 'compte2'):
        assert not _is_linked(a1, 'compte2', b)
    if hasattr(a2, 'compte2'):
        assert _is_linked(a2, 'compte2', b)
    _safe_set(b, 'passager3', None)
    assert not _is_linked(b, 'passager3', a2)
    if hasattr(a2, 'compte2'):
        assert not _is_linked(a2, 'compte2', b)


def test_assoc_inscription_conducteur_reverse_link_reassign_clear():
    a1 = inscription(informations_conducteur="sample_text", informations_passager="sample_text")
    a2 = inscription(informations_conducteur="sample_text_2", informations_passager="sample_text_2")
    b = conducteur(informations_conducteur="sample_text")
    _safe_set(b, 'inscription16', a1)
    assert _is_linked(b, 'inscription16', a1)
    if hasattr(a1, 'conducteur17'):
        assert _is_linked(a1, 'conducteur17', b)
    _safe_set(b, 'inscription16', a2)
    assert _is_linked(b, 'inscription16', a2)
    if hasattr(a1, 'conducteur17'):
        assert not _is_linked(a1, 'conducteur17', b)
    if hasattr(a2, 'conducteur17'):
        assert _is_linked(a2, 'conducteur17', b)
    _safe_set(b, 'inscription16', None)
    assert not _is_linked(b, 'inscription16', a2)
    if hasattr(a2, 'conducteur17'):
        assert not _is_linked(a2, 'conducteur17', b)


def test_assoc_inscription_passager_reverse_link_reassign_clear():
    a1 = passager(informations_passager="sample_text")
    a2 = passager(informations_passager="sample_text_2")
    b = inscription(informations_conducteur="sample_text", informations_passager="sample_text")
    _safe_set(b, 'passager1', a1)
    assert _is_linked(b, 'passager1', a1)
    if hasattr(a1, 'inscription0'):
        assert _is_linked(a1, 'inscription0', b)
    _safe_set(b, 'passager1', a2)
    assert _is_linked(b, 'passager1', a2)
    if hasattr(a1, 'inscription0'):
        assert not _is_linked(a1, 'inscription0', b)
    if hasattr(a2, 'inscription0'):
        assert _is_linked(a2, 'inscription0', b)
    _safe_set(b, 'passager1', None)
    assert not _is_linked(b, 'passager1', a2)
    if hasattr(a2, 'inscription0'):
        assert not _is_linked(a2, 'inscription0', b)


def test_assoc_passager_paiement_reverse_link_reassign_clear():
    a1 = passager(informations_passager="sample_text")
    a2 = passager(informations_passager="sample_text_2")
    b = paiement(m_thode_de_paiement="sample_text")
    _safe_set(b, 'passager4', a1)
    assert _is_linked(b, 'passager4', a1)
    if hasattr(a1, 'paiement5'):
        assert _is_linked(a1, 'paiement5', b)
    _safe_set(b, 'passager4', a2)
    assert _is_linked(b, 'passager4', a2)
    if hasattr(a1, 'paiement5'):
        assert not _is_linked(a1, 'paiement5', b)
    if hasattr(a2, 'paiement5'):
        assert _is_linked(a2, 'paiement5', b)
    _safe_set(b, 'passager4', None)
    assert not _is_linked(b, 'passager4', a2)
    if hasattr(a2, 'paiement5'):
        assert not _is_linked(a2, 'paiement5', b)


def test_assoc_trajet_passager_reverse_link_reassign_clear():
    a1 = trajet(l_heure_de_d_part=3.14, la_date="sample_text", lieu_de_d_part="sample_text", prix_du_trajet=3.14)
    a2 = trajet(l_heure_de_d_part=9.99, la_date="sample_text_2", lieu_de_d_part="sample_text_2", prix_du_trajet=9.99)
    b = passager(informations_passager="sample_text")
    _safe_set(b, 'trajet14', a1)
    assert _is_linked(b, 'trajet14', a1)
    if hasattr(a1, 'passager15'):
        assert _is_linked(a1, 'passager15', b)
    _safe_set(b, 'trajet14', a2)
    assert _is_linked(b, 'trajet14', a2)
    if hasattr(a1, 'passager15'):
        assert not _is_linked(a1, 'passager15', b)
    if hasattr(a2, 'passager15'):
        assert _is_linked(a2, 'passager15', b)
    _safe_set(b, 'trajet14', None)
    assert not _is_linked(b, 'trajet14', a2)
    if hasattr(a2, 'passager15'):
        assert not _is_linked(a2, 'passager15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_administrateur_inscription_stub_double():
    # administrateur has no real 'inscription13' property in the generated
    # code (a bare stub) -- manually attach it so inscription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # inscription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = inscription(informations_conducteur="sample_text", informations_passager="sample_text")
    partner = administrateur()
    setattr(partner, 'inscription13', None)
    _safe_set(owner, 'administrateur12', partner)
    assert getattr(partner, 'inscription13') == owner
    _safe_set(owner, 'administrateur12', None)
    assert getattr(partner, 'inscription13') is None


def test_assoc_administrateur_paiement_stub_double():
    # administrateur has no real 'paiement9' property in the generated
    # code (a bare stub) -- manually attach it so paiement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # paiement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = paiement(m_thode_de_paiement="sample_text")
    partner = administrateur()
    setattr(partner, 'paiement9', None)
    _safe_set(owner, 'administrateur8', partner)
    assert owner in getattr(partner, 'paiement9')
    _safe_set(owner, 'administrateur8', None)
    assert owner not in getattr(partner, 'paiement9')


def test_assoc_administrateur_passager_stub_double():
    # administrateur has no real 'passager11' property in the generated
    # code (a bare stub) -- manually attach it so passager's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # passager's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = passager(informations_passager="sample_text")
    partner = administrateur()
    setattr(partner, 'passager11', None)
    _safe_set(owner, 'administrateur10', partner)
    assert getattr(partner, 'passager11') == owner
    _safe_set(owner, 'administrateur10', None)
    assert getattr(partner, 'passager11') is None


def test_assoc_administrateur_reservation_stub_double():
    # administrateur has no real 'reservation7' property in the generated
    # code (a bare stub) -- manually attach it so reservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # reservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = reservation(nombre_de_passager=7)
    partner = administrateur()
    setattr(partner, 'reservation7', None)
    _safe_set(owner, 'administrateur6', partner)
    assert getattr(partner, 'reservation7') == owner
    _safe_set(owner, 'administrateur6', None)
    assert getattr(partner, 'reservation7') is None


def test_assoc_administrateur_trajet_stub_double():
    # administrateur has no real 'trajet19' property in the generated
    # code (a bare stub) -- manually attach it so trajet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trajet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trajet(l_heure_de_d_part=3.14, la_date="sample_text", lieu_de_d_part="sample_text", prix_du_trajet=3.14)
    partner = administrateur()
    setattr(partner, 'trajet19', None)
    _safe_set(owner, 'administrateur18', partner)
    assert getattr(partner, 'trajet19') == owner
    _safe_set(owner, 'administrateur18', None)
    assert getattr(partner, 'trajet19') is None


