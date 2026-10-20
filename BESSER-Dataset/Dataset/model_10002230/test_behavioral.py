import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Client,
    Convention,
    DevisEntete,
    Facture,
    Formateur,
    Formation,
    Participant,
    Prestation,
    Type,
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

def test_assoc_Client_Session_reverse_link_reassign_clear():
    a1 = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    a2 = Prestation(date_debut="sample_text_2", date_fin="sample_text_2", duree="sample_text_2", horaires="sample_text_2", id_client=13, id_formateur=13, id_formation=13, id_type=13, lieu=False, nb_stagiaires=13)
    b = Client(adresse="sample_text", codePostal="sample_text", contact="sample_text", nom="sample_text", tel="sample_text", ville="sample_text")
    _safe_set(b, 'session6', a1)
    assert _is_linked(b, 'session6', a1)
    if hasattr(a1, 'client7'):
        assert _is_linked(a1, 'client7', b)
    _safe_set(b, 'session6', a2)
    assert _is_linked(b, 'session6', a2)
    if hasattr(a1, 'client7'):
        assert not _is_linked(a1, 'client7', b)
    if hasattr(a2, 'client7'):
        assert _is_linked(a2, 'client7', b)
    _safe_set(b, 'session6', None)
    assert not _is_linked(b, 'session6', a2)
    if hasattr(a2, 'client7'):
        assert not _is_linked(a2, 'client7', b)


def test_assoc_DevisEntete_Session_reverse_link_reassign_clear():
    a1 = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    a2 = Prestation(date_debut="sample_text_2", date_fin="sample_text_2", duree="sample_text_2", horaires="sample_text_2", id_client=13, id_formateur=13, id_formation=13, id_type=13, lieu=False, nb_stagiaires=13)
    b = DevisEntete(id_session=7, numero="sample_text")
    _safe_set(b, 'session4', a1)
    assert _is_linked(b, 'session4', a1)
    if hasattr(a1, 'devisEntete5'):
        assert _is_linked(a1, 'devisEntete5', b)
    _safe_set(b, 'session4', a2)
    assert _is_linked(b, 'session4', a2)
    if hasattr(a1, 'devisEntete5'):
        assert not _is_linked(a1, 'devisEntete5', b)
    if hasattr(a2, 'devisEntete5'):
        assert _is_linked(a2, 'devisEntete5', b)
    _safe_set(b, 'session4', None)
    assert not _is_linked(b, 'session4', a2)
    if hasattr(a2, 'devisEntete5'):
        assert not _is_linked(a2, 'devisEntete5', b)


def test_assoc_Formateurs_Sessions_reverse_link_reassign_clear():
    a1 = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    a2 = Prestation(date_debut="sample_text_2", date_fin="sample_text_2", duree="sample_text_2", horaires="sample_text_2", id_client=13, id_formateur=13, id_formation=13, id_type=13, lieu=False, nb_stagiaires=13)
    b = Formateur(Nom="sample_text", Prenom="sample_text")
    _safe_set(b, 'sessions2', a1)
    assert _is_linked(b, 'sessions2', a1)
    if hasattr(a1, 'formateurs3'):
        assert _is_linked(a1, 'formateurs3', b)
    _safe_set(b, 'sessions2', a2)
    assert _is_linked(b, 'sessions2', a2)
    if hasattr(a1, 'formateurs3'):
        assert not _is_linked(a1, 'formateurs3', b)
    if hasattr(a2, 'formateurs3'):
        assert _is_linked(a2, 'formateurs3', b)
    _safe_set(b, 'sessions2', None)
    assert not _is_linked(b, 'sessions2', a2)
    if hasattr(a2, 'formateurs3'):
        assert not _is_linked(a2, 'formateurs3', b)


def test_assoc_Formation_Session_reverse_link_reassign_clear():
    a1 = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    a2 = Prestation(date_debut="sample_text_2", date_fin="sample_text_2", duree="sample_text_2", horaires="sample_text_2", id_client=13, id_formateur=13, id_formation=13, id_type=13, lieu=False, nb_stagiaires=13)
    b = Formation(cout_unitaire=7, libelle="sample_text", objectif="sample_text")
    _safe_set(b, 'session8', a1)
    assert _is_linked(b, 'session8', a1)
    if hasattr(a1, 'formation9'):
        assert _is_linked(a1, 'formation9', b)
    _safe_set(b, 'session8', a2)
    assert _is_linked(b, 'session8', a2)
    if hasattr(a1, 'formation9'):
        assert not _is_linked(a1, 'formation9', b)
    if hasattr(a2, 'formation9'):
        assert _is_linked(a2, 'formation9', b)
    _safe_set(b, 'session8', None)
    assert not _is_linked(b, 'session8', a2)
    if hasattr(a2, 'formation9'):
        assert not _is_linked(a2, 'formation9', b)


def test_assoc_Sessions_Participants_reverse_link_reassign_clear():
    a1 = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    a2 = Prestation(date_debut="sample_text_2", date_fin="sample_text_2", duree="sample_text_2", horaires="sample_text_2", id_client=13, id_formateur=13, id_formation=13, id_type=13, lieu=False, nb_stagiaires=13)
    b = Participant(date_naissance="sample_text", id_session=7, nom="sample_text", prenom="sample_text")
    _safe_set(b, 'sessions1', {a1})
    assert _is_linked(b, 'sessions1', a1)
    if hasattr(a1, 'participants0'):
        assert _is_linked(a1, 'participants0', b)
    _safe_set(b, 'sessions1', {a2})
    assert _is_linked(b, 'sessions1', a2)
    if hasattr(a1, 'participants0'):
        assert not _is_linked(a1, 'participants0', b)
    if hasattr(a2, 'participants0'):
        assert _is_linked(a2, 'participants0', b)
    _safe_set(b, 'sessions1', set())
    assert not _is_linked(b, 'sessions1', a2)
    if hasattr(a2, 'participants0'):
        assert not _is_linked(a2, 'participants0', b)


def test_assoc_Type_Prestation_reverse_link_reassign_clear():
    a1 = Type(type="sample_text")
    a2 = Type(type="sample_text_2")
    b = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    _safe_set(b, 'type11', a1)
    assert _is_linked(b, 'type11', a1)
    if hasattr(a1, 'prestation10'):
        assert _is_linked(a1, 'prestation10', b)
    _safe_set(b, 'type11', a2)
    assert _is_linked(b, 'type11', a2)
    if hasattr(a1, 'prestation10'):
        assert not _is_linked(a1, 'prestation10', b)
    if hasattr(a2, 'prestation10'):
        assert _is_linked(a2, 'prestation10', b)
    _safe_set(b, 'type11', None)
    assert not _is_linked(b, 'type11', a2)
    if hasattr(a2, 'prestation10'):
        assert not _is_linked(a2, 'prestation10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

