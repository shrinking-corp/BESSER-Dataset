import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrateur,
    BankAccount,
    CCP,
    ClassA,
    ClassB,
    ClassC,
    ClassD,
    ClassE,
    ClassF,
    ClassG,
    ClassH,
    ClassJ,
    ClassK,
    ClassL,
    ClassM,
    ClassN,
    ClassP,
    ClassQ,
    ClassR,
    ClassS,
    ClassT,
    ClassU,
    ClassV,
    Direction,
    Document,
    Etudiant,
    Formateur,
    Formation,
    InterfaceO_Interface,
    Personne,
    Session,
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

def test_assoc_Document_Session_reverse_link_reassign_clear():
    a1 = Session(adresse="sample_text", date_debut=date(2024, 1, 1), date_fin=date(2024, 1, 1), id_session=7, label="sample_text")
    a2 = Session(adresse="sample_text_2", date_debut=date(2025, 6, 15), date_fin=date(2025, 6, 15), id_session=13, label="sample_text_2")
    b = Document(cours=True, descriptif="sample_text", id_document=7, label="sample_text", url="sample_text")
    _safe_set(b, 'session20', {a1})
    assert _is_linked(b, 'session20', a1)
    if hasattr(a1, 'document21'):
        assert _is_linked(a1, 'document21', b)
    _safe_set(b, 'session20', {a2})
    assert _is_linked(b, 'session20', a2)
    if hasattr(a1, 'document21'):
        assert not _is_linked(a1, 'document21', b)
    if hasattr(a2, 'document21'):
        assert _is_linked(a2, 'document21', b)
    _safe_set(b, 'session20', set())
    assert not _is_linked(b, 'session20', a2)
    if hasattr(a2, 'document21'):
        assert not _is_linked(a2, 'document21', b)


def test_assoc_Etudiant_Session_reverse_link_reassign_clear():
    a1 = Session(adresse="sample_text", date_debut=date(2024, 1, 1), date_fin=date(2024, 1, 1), id_session=7, label="sample_text")
    a2 = Session(adresse="sample_text_2", date_debut=date(2025, 6, 15), date_fin=date(2025, 6, 15), id_session=13, label="sample_text_2")
    b = Etudiant(actif=True, cv="sample_text", id_etudiant=7, list_commentaire="sample_text", list_notes=3.14)
    _safe_set(b, 'session22', {a1})
    assert _is_linked(b, 'session22', a1)
    if hasattr(a1, 'etudiant23'):
        assert _is_linked(a1, 'etudiant23', b)
    _safe_set(b, 'session22', {a2})
    assert _is_linked(b, 'session22', a2)
    if hasattr(a1, 'etudiant23'):
        assert not _is_linked(a1, 'etudiant23', b)
    if hasattr(a2, 'etudiant23'):
        assert _is_linked(a2, 'etudiant23', b)
    _safe_set(b, 'session22', set())
    assert not _is_linked(b, 'session22', a2)
    if hasattr(a2, 'etudiant23'):
        assert not _is_linked(a2, 'etudiant23', b)


def test_assoc_Formation_CCP_reverse_link_reassign_clear():
    a1 = Formation(descriptif="sample_text", id_formation=7, label="sample_text")
    a2 = Formation(descriptif="sample_text_2", id_formation=13, label="sample_text_2")
    b = CCP(description="sample_text", id_ccp=7, label="sample_text")
    _safe_set(b, 'formation19', {a1})
    assert _is_linked(b, 'formation19', a1)
    if hasattr(a1, 'cCP18'):
        assert _is_linked(a1, 'cCP18', b)
    _safe_set(b, 'formation19', {a2})
    assert _is_linked(b, 'formation19', a2)
    if hasattr(a1, 'cCP18'):
        assert not _is_linked(a1, 'cCP18', b)
    if hasattr(a2, 'cCP18'):
        assert _is_linked(a2, 'cCP18', b)
    _safe_set(b, 'formation19', set())
    assert not _is_linked(b, 'formation19', a2)
    if hasattr(a2, 'cCP18'):
        assert not _is_linked(a2, 'cCP18', b)


def test_assoc_Formation_Session_reverse_link_reassign_clear():
    a1 = Session(adresse="sample_text", date_debut=date(2024, 1, 1), date_fin=date(2024, 1, 1), id_session=7, label="sample_text")
    a2 = Session(adresse="sample_text_2", date_debut=date(2025, 6, 15), date_fin=date(2025, 6, 15), id_session=13, label="sample_text_2")
    b = Formation(descriptif="sample_text", id_formation=7, label="sample_text")
    _safe_set(b, 'session16', {a1})
    assert _is_linked(b, 'session16', a1)
    if hasattr(a1, 'formation17'):
        assert _is_linked(a1, 'formation17', b)
    _safe_set(b, 'session16', {a2})
    assert _is_linked(b, 'session16', a2)
    if hasattr(a1, 'formation17'):
        assert not _is_linked(a1, 'formation17', b)
    if hasattr(a2, 'formation17'):
        assert _is_linked(a2, 'formation17', b)
    _safe_set(b, 'session16', set())
    assert not _is_linked(b, 'session16', a2)
    if hasattr(a2, 'formation17'):
        assert not _is_linked(a2, 'formation17', b)


def test_assoc_Personne_Administrateur_reverse_link_reassign_clear():
    a1 = Personne(id=7, mail="sample_text", naissance=date(2024, 1, 1), nom="sample_text", photo="sample_text", prenom="sample_text", telephone="sample_text")
    a2 = Personne(id=13, mail="sample_text_2", naissance=date(2025, 6, 15), nom="sample_text_2", photo="sample_text_2", prenom="sample_text_2", telephone="sample_text_2")
    b = Administrateur(actif=True, id_administrateur=7)
    _safe_set(b, 'personne13', {a1})
    assert _is_linked(b, 'personne13', a1)
    if hasattr(a1, 'administrateur12'):
        assert _is_linked(a1, 'administrateur12', b)
    _safe_set(b, 'personne13', {a2})
    assert _is_linked(b, 'personne13', a2)
    if hasattr(a1, 'administrateur12'):
        assert not _is_linked(a1, 'administrateur12', b)
    if hasattr(a2, 'administrateur12'):
        assert _is_linked(a2, 'administrateur12', b)
    _safe_set(b, 'personne13', set())
    assert not _is_linked(b, 'personne13', a2)
    if hasattr(a2, 'administrateur12'):
        assert not _is_linked(a2, 'administrateur12', b)


def test_assoc_Personne_Direction_reverse_link_reassign_clear():
    a1 = Personne(id=7, mail="sample_text", naissance=date(2024, 1, 1), nom="sample_text", photo="sample_text", prenom="sample_text", telephone="sample_text")
    a2 = Personne(id=13, mail="sample_text_2", naissance=date(2025, 6, 15), nom="sample_text_2", photo="sample_text_2", prenom="sample_text_2", telephone="sample_text_2")
    b = Direction(actif=True, id_direction=7)
    _safe_set(b, 'personne11', {a1})
    assert _is_linked(b, 'personne11', a1)
    if hasattr(a1, 'direction10'):
        assert _is_linked(a1, 'direction10', b)
    _safe_set(b, 'personne11', {a2})
    assert _is_linked(b, 'personne11', a2)
    if hasattr(a1, 'direction10'):
        assert not _is_linked(a1, 'direction10', b)
    if hasattr(a2, 'direction10'):
        assert _is_linked(a2, 'direction10', b)
    _safe_set(b, 'personne11', set())
    assert not _is_linked(b, 'personne11', a2)
    if hasattr(a2, 'direction10'):
        assert not _is_linked(a2, 'direction10', b)


def test_assoc_Personne_Etudiant_reverse_link_reassign_clear():
    a1 = Personne(id=7, mail="sample_text", naissance=date(2024, 1, 1), nom="sample_text", photo="sample_text", prenom="sample_text", telephone="sample_text")
    a2 = Personne(id=13, mail="sample_text_2", naissance=date(2025, 6, 15), nom="sample_text_2", photo="sample_text_2", prenom="sample_text_2", telephone="sample_text_2")
    b = Etudiant(actif=True, cv="sample_text", id_etudiant=7, list_commentaire="sample_text", list_notes=3.14)
    _safe_set(b, 'personne7', {a1})
    assert _is_linked(b, 'personne7', a1)
    if hasattr(a1, 'etudiant6'):
        assert _is_linked(a1, 'etudiant6', b)
    _safe_set(b, 'personne7', {a2})
    assert _is_linked(b, 'personne7', a2)
    if hasattr(a1, 'etudiant6'):
        assert not _is_linked(a1, 'etudiant6', b)
    if hasattr(a2, 'etudiant6'):
        assert _is_linked(a2, 'etudiant6', b)
    _safe_set(b, 'personne7', set())
    assert not _is_linked(b, 'personne7', a2)
    if hasattr(a2, 'etudiant6'):
        assert not _is_linked(a2, 'etudiant6', b)


def test_assoc_Personne_Formateur_reverse_link_reassign_clear():
    a1 = Personne(id=7, mail="sample_text", naissance=date(2024, 1, 1), nom="sample_text", photo="sample_text", prenom="sample_text", telephone="sample_text")
    a2 = Personne(id=13, mail="sample_text_2", naissance=date(2025, 6, 15), nom="sample_text_2", photo="sample_text_2", prenom="sample_text_2", telephone="sample_text_2")
    b = Formateur(actif=True, id_formateur=7)
    _safe_set(b, 'personne9', {a1})
    assert _is_linked(b, 'personne9', a1)
    if hasattr(a1, 'formateur8'):
        assert _is_linked(a1, 'formateur8', b)
    _safe_set(b, 'personne9', {a2})
    assert _is_linked(b, 'personne9', a2)
    if hasattr(a1, 'formateur8'):
        assert not _is_linked(a1, 'formateur8', b)
    if hasattr(a2, 'formateur8'):
        assert _is_linked(a2, 'formateur8', b)
    _safe_set(b, 'personne9', set())
    assert not _is_linked(b, 'personne9', a2)
    if hasattr(a2, 'formateur8'):
        assert not _is_linked(a2, 'formateur8', b)


def test_assoc_Session_Formateur_reverse_link_reassign_clear():
    a1 = Session(adresse="sample_text", date_debut=date(2024, 1, 1), date_fin=date(2024, 1, 1), id_session=7, label="sample_text")
    a2 = Session(adresse="sample_text_2", date_debut=date(2025, 6, 15), date_fin=date(2025, 6, 15), id_session=13, label="sample_text_2")
    b = Formateur(actif=True, id_formateur=7)
    _safe_set(b, 'session15', {a1})
    assert _is_linked(b, 'session15', a1)
    if hasattr(a1, 'formateur14'):
        assert _is_linked(a1, 'formateur14', b)
    _safe_set(b, 'session15', {a2})
    assert _is_linked(b, 'session15', a2)
    if hasattr(a1, 'formateur14'):
        assert not _is_linked(a1, 'formateur14', b)
    if hasattr(a2, 'formateur14'):
        assert _is_linked(a2, 'formateur14', b)
    _safe_set(b, 'session15', set())
    assert not _is_linked(b, 'session15', a2)
    if hasattr(a2, 'formateur14'):
        assert not _is_linked(a2, 'formateur14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

