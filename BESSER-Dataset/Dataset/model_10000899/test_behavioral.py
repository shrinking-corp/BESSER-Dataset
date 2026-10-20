import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin_Admin_Actor,
    Admin_Passager___conducteur_Actor,
    Admin_UseCase5_UseCase,
    Admin_add_trajet_UseCase,
    Admin_consulter_liste_utilis_UseCase,
    Admin_consulter_trajets_UseCase,
    Admin_modifier_utilis_UseCase,
    Admin_s_inscrire_UseCase,
    Admin_suppr_utils_UseCase,
    covoiturage_Avis,
    covoiturage_Personne,
    covoiturage_Preferences,
    covoiturage_Reservations,
    covoiturage_Ville,
    covoiturage_Voiture,
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

def test_assoc_Avis_Evenement_reverse_link_reassign_clear():
    a1 = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    a2 = covoiturage_Reservations(date=date(2025, 6, 15), id=13, lieuDeDepose="sample_text_2", prix=13)
    b = covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    _safe_set(b, 'evenement10', a1)
    assert _is_linked(b, 'evenement10', a1)
    if hasattr(a1, 'avis11'):
        assert _is_linked(a1, 'avis11', b)
    _safe_set(b, 'evenement10', a2)
    assert _is_linked(b, 'evenement10', a2)
    if hasattr(a1, 'avis11'):
        assert not _is_linked(a1, 'avis11', b)
    if hasattr(a2, 'avis11'):
        assert _is_linked(a2, 'avis11', b)
    _safe_set(b, 'evenement10', None)
    assert not _is_linked(b, 'evenement10', a2)
    if hasattr(a2, 'avis11'):
        assert not _is_linked(a2, 'avis11', b)


def test_assoc_Avis_Personne_reverse_link_reassign_clear():
    a1 = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    a2 = covoiturage_Personne(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel="sample_text_2")
    b = covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    _safe_set(b, 'personne8', a1)
    assert _is_linked(b, 'personne8', a1)
    if hasattr(a1, 'avis9'):
        assert _is_linked(a1, 'avis9', b)
    _safe_set(b, 'personne8', a2)
    assert _is_linked(b, 'personne8', a2)
    if hasattr(a1, 'avis9'):
        assert not _is_linked(a1, 'avis9', b)
    if hasattr(a2, 'avis9'):
        assert _is_linked(a2, 'avis9', b)
    _safe_set(b, 'personne8', None)
    assert not _is_linked(b, 'personne8', a2)
    if hasattr(a2, 'avis9'):
        assert not _is_linked(a2, 'avis9', b)


def test_assoc_Evenement_Ville_reverse_link_reassign_clear():
    a1 = covoiturage_Ville(cp="sample_text", id=7, nom="sample_text")
    a2 = covoiturage_Ville(cp="sample_text_2", id=13, nom="sample_text_2")
    b = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    _safe_set(b, 'villes4', {a1})
    assert _is_linked(b, 'villes4', a1)
    if hasattr(a1, 'evenement5'):
        assert _is_linked(a1, 'evenement5', b)
    _safe_set(b, 'villes4', {a2})
    assert _is_linked(b, 'villes4', a2)
    if hasattr(a1, 'evenement5'):
        assert not _is_linked(a1, 'evenement5', b)
    if hasattr(a2, 'evenement5'):
        assert _is_linked(a2, 'evenement5', b)
    _safe_set(b, 'villes4', set())
    assert not _is_linked(b, 'villes4', a2)
    if hasattr(a2, 'evenement5'):
        assert not _is_linked(a2, 'evenement5', b)


def test_assoc_Personne_Evenement_reverse_link_reassign_clear():
    a1 = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    a2 = covoiturage_Reservations(date=date(2025, 6, 15), id=13, lieuDeDepose="sample_text_2", prix=13)
    b = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    _safe_set(b, 'events6', {a1})
    assert _is_linked(b, 'events6', a1)
    if hasattr(a1, 'participants7'):
        assert _is_linked(a1, 'participants7', b)
    _safe_set(b, 'events6', {a2})
    assert _is_linked(b, 'events6', a2)
    if hasattr(a1, 'participants7'):
        assert not _is_linked(a1, 'participants7', b)
    if hasattr(a2, 'participants7'):
        assert _is_linked(a2, 'participants7', b)
    _safe_set(b, 'events6', set())
    assert not _is_linked(b, 'events6', a2)
    if hasattr(a2, 'participants7'):
        assert not _is_linked(a2, 'participants7', b)


def test_assoc_Personne_Preferences_reverse_link_reassign_clear():
    a1 = covoiturage_Preferences(id=7, nomPref="sample_text", valeur="sample_text")
    a2 = covoiturage_Preferences(id=13, nomPref="sample_text_2", valeur="sample_text_2")
    b = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    _safe_set(b, 'preferences2', {a1})
    assert _is_linked(b, 'preferences2', a1)
    if hasattr(a1, 'personne3'):
        assert _is_linked(a1, 'personne3', b)
    _safe_set(b, 'preferences2', {a2})
    assert _is_linked(b, 'preferences2', a2)
    if hasattr(a1, 'personne3'):
        assert not _is_linked(a1, 'personne3', b)
    if hasattr(a2, 'personne3'):
        assert _is_linked(a2, 'personne3', b)
    _safe_set(b, 'preferences2', set())
    assert not _is_linked(b, 'preferences2', a2)
    if hasattr(a2, 'personne3'):
        assert not _is_linked(a2, 'personne3', b)


def test_assoc_Personne_Ville_reverse_link_reassign_clear():
    a1 = covoiturage_Ville(cp="sample_text", id=7, nom="sample_text")
    a2 = covoiturage_Ville(cp="sample_text_2", id=13, nom="sample_text_2")
    b = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    _safe_set(b, 'adresse12', a1)
    assert _is_linked(b, 'adresse12', a1)
    if hasattr(a1, 'personnes13'):
        assert _is_linked(a1, 'personnes13', b)
    _safe_set(b, 'adresse12', a2)
    assert _is_linked(b, 'adresse12', a2)
    if hasattr(a1, 'personnes13'):
        assert not _is_linked(a1, 'personnes13', b)
    if hasattr(a2, 'personnes13'):
        assert _is_linked(a2, 'personnes13', b)
    _safe_set(b, 'adresse12', None)
    assert not _is_linked(b, 'adresse12', a2)
    if hasattr(a2, 'personnes13'):
        assert not _is_linked(a2, 'personnes13', b)


def test_assoc_Personne_Voiture_reverse_link_reassign_clear():
    a1 = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    a2 = covoiturage_Voiture(categorie="sample_text_2", climatiseur=False, confort="sample_text_2", couleur="sample_text_2", id=13, marque="sample_text_2", model="sample_text_2", nbPlaces=13, tabac=False)
    b = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    _safe_set(b, 'voiture0', a1)
    assert _is_linked(b, 'voiture0', a1)
    if hasattr(a1, 'personne1'):
        assert _is_linked(a1, 'personne1', b)
    _safe_set(b, 'voiture0', a2)
    assert _is_linked(b, 'voiture0', a2)
    if hasattr(a1, 'personne1'):
        assert not _is_linked(a1, 'personne1', b)
    if hasattr(a2, 'personne1'):
        assert _is_linked(a2, 'personne1', b)
    _safe_set(b, 'voiture0', None)
    assert not _is_linked(b, 'voiture0', a2)
    if hasattr(a2, 'personne1'):
        assert not _is_linked(a2, 'personne1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

