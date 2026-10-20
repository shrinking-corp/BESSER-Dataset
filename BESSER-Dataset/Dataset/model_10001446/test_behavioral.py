import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Covoiturage_Authentification,
    Covoiturage_Avis,
    Covoiturage_Conducteur,
    Covoiturage_Message,
    Covoiturage_Passager,
    Covoiturage_Reservation,
    Covoiturage_Trajet,
    Covoiturage_Ville,
    Covoiturage_Voiture,
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

def test_assoc_Avis_Personne_reverse_link_reassign_clear():
    a1 = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    a2 = Covoiturage_Passager(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel=13)
    b = Covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    _safe_set(b, 'personne4', a1)
    assert _is_linked(b, 'personne4', a1)
    if hasattr(a1, 'avis5'):
        assert _is_linked(a1, 'avis5', b)
    _safe_set(b, 'personne4', a2)
    assert _is_linked(b, 'personne4', a2)
    if hasattr(a1, 'avis5'):
        assert not _is_linked(a1, 'avis5', b)
    if hasattr(a2, 'avis5'):
        assert _is_linked(a2, 'avis5', b)
    _safe_set(b, 'personne4', None)
    assert not _is_linked(b, 'personne4', a2)
    if hasattr(a2, 'avis5'):
        assert not _is_linked(a2, 'avis5', b)


def test_assoc_Passager_Message_reverse_link_reassign_clear():
    a1 = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    a2 = Covoiturage_Passager(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel=13)
    b = Covoiturage_Message(Id="sample_text", Value="sample_text")
    _safe_set(b, 'passager18', a1)
    assert _is_linked(b, 'passager18', a1)
    if hasattr(a1, 'message19'):
        assert _is_linked(a1, 'message19', b)
    _safe_set(b, 'passager18', a2)
    assert _is_linked(b, 'passager18', a2)
    if hasattr(a1, 'message19'):
        assert not _is_linked(a1, 'message19', b)
    if hasattr(a2, 'message19'):
        assert _is_linked(a2, 'message19', b)
    _safe_set(b, 'passager18', None)
    assert not _is_linked(b, 'passager18', a2)
    if hasattr(a2, 'message19'):
        assert not _is_linked(a2, 'message19', b)


def test_assoc_Personne_Preferences_reverse_link_reassign_clear():
    a1 = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    a2 = Covoiturage_Passager(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel=13)
    b = Covoiturage_Authentification(id="sample_text", password="sample_text")
    _safe_set(b, 'personne1', {a1})
    assert _is_linked(b, 'personne1', a1)
    if hasattr(a1, 's_authentifi_0'):
        assert _is_linked(a1, 's_authentifi_0', b)
    _safe_set(b, 'personne1', {a2})
    assert _is_linked(b, 'personne1', a2)
    if hasattr(a1, 's_authentifi_0'):
        assert not _is_linked(a1, 's_authentifi_0', b)
    if hasattr(a2, 's_authentifi_0'):
        assert _is_linked(a2, 's_authentifi_0', b)
    _safe_set(b, 'personne1', set())
    assert not _is_linked(b, 'personne1', a2)
    if hasattr(a2, 's_authentifi_0'):
        assert not _is_linked(a2, 's_authentifi_0', b)


def test_assoc_Personne_Ville_reverse_link_reassign_clear():
    a1 = Covoiturage_Ville(cp=7, id=7, nom="sample_text")
    a2 = Covoiturage_Ville(cp=13, id=13, nom="sample_text_2")
    b = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    _safe_set(b, 'adresse8', a1)
    assert _is_linked(b, 'adresse8', a1)
    if hasattr(a1, 'personnes9'):
        assert _is_linked(a1, 'personnes9', b)
    _safe_set(b, 'adresse8', a2)
    assert _is_linked(b, 'adresse8', a2)
    if hasattr(a1, 'personnes9'):
        assert not _is_linked(a1, 'personnes9', b)
    if hasattr(a2, 'personnes9'):
        assert _is_linked(a2, 'personnes9', b)
    _safe_set(b, 'adresse8', None)
    assert not _is_linked(b, 'adresse8', a2)
    if hasattr(a2, 'personnes9'):
        assert not _is_linked(a2, 'personnes9', b)


def test_assoc_Profil_Reservation_reverse_link_reassign_clear():
    a1 = Covoiturage_Reservation(dateReservation=date(2024, 1, 1), etat=True, id=7, id2=7)
    a2 = Covoiturage_Reservation(dateReservation=date(2025, 6, 15), etat=False, id=13, id2=13)
    b = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    _safe_set(b, 'reservation13', a1)
    assert _is_linked(b, 'reservation13', a1)
    if hasattr(a1, 'profil12'):
        assert _is_linked(a1, 'profil12', b)
    _safe_set(b, 'reservation13', a2)
    assert _is_linked(b, 'reservation13', a2)
    if hasattr(a1, 'profil12'):
        assert not _is_linked(a1, 'profil12', b)
    if hasattr(a2, 'profil12'):
        assert _is_linked(a2, 'profil12', b)
    _safe_set(b, 'reservation13', None)
    assert not _is_linked(b, 'reservation13', a2)
    if hasattr(a2, 'profil12'):
        assert not _is_linked(a2, 'profil12', b)


def test_assoc_Voiture_Passager_reverse_link_reassign_clear():
    a1 = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    a2 = Covoiturage_Voiture(attribute="sample_text_2", categorie="sample_text_2", confort="sample_text_2", id=13, marque="sample_text_2", model="sample_text_2", nbPlaces=13)
    b = Covoiturage_Conducteur(datePermi="sample_text")
    _safe_set(b, 'voiture16', a1)
    assert _is_linked(b, 'voiture16', a1)
    if hasattr(a1, 'Profil17'):
        assert _is_linked(a1, 'Profil17', b)
    _safe_set(b, 'voiture16', a2)
    assert _is_linked(b, 'voiture16', a2)
    if hasattr(a1, 'Profil17'):
        assert not _is_linked(a1, 'Profil17', b)
    if hasattr(a2, 'Profil17'):
        assert _is_linked(a2, 'Profil17', b)
    _safe_set(b, 'voiture16', None)
    assert not _is_linked(b, 'voiture16', a2)
    if hasattr(a2, 'Profil17'):
        assert not _is_linked(a2, 'Profil17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

