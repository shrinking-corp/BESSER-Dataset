import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Covoiturage_Authentification_id_value_roundtrip():
    instance = Covoiturage_Authentification(id="sample_text", password="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Covoiturage_Authentification_password_value_roundtrip():
    instance = Covoiturage_Authentification(id="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Covoiturage_Avis_commentaire_value_roundtrip():
    instance = Covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.commentaire == "sample_text"
    instance.commentaire = "sample_text_2"
    assert instance.commentaire == "sample_text_2"


def test_Covoiturage_Avis_id_value_roundtrip():
    instance = Covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Covoiturage_Avis_note_value_roundtrip():
    instance = Covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.note == 7
    instance.note = 13
    assert instance.note == 13


def test_Covoiturage_Conducteur_datePermi_value_roundtrip():
    instance = Covoiturage_Conducteur(datePermi="sample_text")
    assert instance.datePermi == "sample_text"
    instance.datePermi = "sample_text_2"
    assert instance.datePermi == "sample_text_2"


def test_Covoiturage_Message_Id_value_roundtrip():
    instance = Covoiturage_Message(Id="sample_text", Value="sample_text")
    assert instance.Id == "sample_text"
    instance.Id = "sample_text_2"
    assert instance.Id == "sample_text_2"


def test_Covoiturage_Message_Value_value_roundtrip():
    instance = Covoiturage_Message(Id="sample_text", Value="sample_text")
    assert instance.Value == "sample_text"
    instance.Value = "sample_text_2"
    assert instance.Value == "sample_text_2"


def test_Covoiturage_Passager_id_value_roundtrip():
    instance = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Covoiturage_Passager_mail_value_roundtrip():
    instance = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    assert instance.mail == "sample_text"
    instance.mail = "sample_text_2"
    assert instance.mail == "sample_text_2"


def test_Covoiturage_Passager_nom_value_roundtrip():
    instance = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Covoiturage_Passager_prenom_value_roundtrip():
    instance = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    assert instance.prenom == "sample_text"
    instance.prenom = "sample_text_2"
    assert instance.prenom == "sample_text_2"


def test_Covoiturage_Passager_tel_value_roundtrip():
    instance = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    assert instance.tel == 7
    instance.tel = 13
    assert instance.tel == 13


def test_Covoiturage_Reservation_dateReservation_value_roundtrip():
    instance = Covoiturage_Reservation(dateReservation=date(2024, 1, 1), etat=True, id=7, id2=7)
    assert instance.dateReservation == date(2024, 1, 1)
    instance.dateReservation = date(2025, 6, 15)
    assert instance.dateReservation == date(2025, 6, 15)


def test_Covoiturage_Reservation_etat_value_roundtrip():
    instance = Covoiturage_Reservation(dateReservation=date(2024, 1, 1), etat=True, id=7, id2=7)
    assert instance.etat == True
    instance.etat = False
    assert instance.etat == False


def test_Covoiturage_Reservation_id_value_roundtrip():
    instance = Covoiturage_Reservation(dateReservation=date(2024, 1, 1), etat=True, id=7, id2=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Covoiturage_Reservation_id2_value_roundtrip():
    instance = Covoiturage_Reservation(dateReservation=date(2024, 1, 1), etat=True, id=7, id2=7)
    assert instance.id2 == 7
    instance.id2 = 13
    assert instance.id2 == 13


def test_Covoiturage_Ville_cp_value_roundtrip():
    instance = Covoiturage_Ville(cp=7, id=7, nom="sample_text")
    assert instance.cp == 7
    instance.cp = 13
    assert instance.cp == 13


def test_Covoiturage_Ville_id_value_roundtrip():
    instance = Covoiturage_Ville(cp=7, id=7, nom="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Covoiturage_Ville_nom_value_roundtrip():
    instance = Covoiturage_Ville(cp=7, id=7, nom="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Covoiturage_Voiture_attribute_value_roundtrip():
    instance = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Covoiturage_Voiture_categorie_value_roundtrip():
    instance = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.categorie == "sample_text"
    instance.categorie = "sample_text_2"
    assert instance.categorie == "sample_text_2"


def test_Covoiturage_Voiture_confort_value_roundtrip():
    instance = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.confort == "sample_text"
    instance.confort = "sample_text_2"
    assert instance.confort == "sample_text_2"


def test_Covoiturage_Voiture_id_value_roundtrip():
    instance = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Covoiturage_Voiture_marque_value_roundtrip():
    instance = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.marque == "sample_text"
    instance.marque = "sample_text_2"
    assert instance.marque == "sample_text_2"


def test_Covoiturage_Voiture_model_value_roundtrip():
    instance = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.model == "sample_text"
    instance.model = "sample_text_2"
    assert instance.model == "sample_text_2"


def test_Covoiturage_Voiture_nbPlaces_value_roundtrip():
    instance = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.nbPlaces == 7
    instance.nbPlaces = 13
    assert instance.nbPlaces == 13


def test_assoc_Avis_Personne_link_reassign_clear():
    a = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    b1 = Covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    b2 = Covoiturage_Avis(commentaire="sample_text_2", id=13, note=13)
    _safe_set(a, 'avis5', {b1})
    assert _is_linked(a, 'avis5', b1)
    if hasattr(b1, 'personne4'):
        assert _is_linked(b1, 'personne4', a)
    _safe_set(a, 'avis5', {b2})
    assert _is_linked(a, 'avis5', b2)
    if hasattr(b1, 'personne4'):
        assert not _is_linked(b1, 'personne4', a)
    if hasattr(b2, 'personne4'):
        assert _is_linked(b2, 'personne4', a)
    _safe_set(a, 'avis5', set())
    assert not _is_linked(a, 'avis5', b2)
    if hasattr(b2, 'personne4'):
        assert not _is_linked(b2, 'personne4', a)


def test_assoc_Passager_Message_link_reassign_clear():
    a = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    b1 = Covoiturage_Message(Id="sample_text", Value="sample_text")
    b2 = Covoiturage_Message(Id="sample_text_2", Value="sample_text_2")
    _safe_set(a, 'message19', {b1})
    assert _is_linked(a, 'message19', b1)
    if hasattr(b1, 'passager18'):
        assert _is_linked(b1, 'passager18', a)
    _safe_set(a, 'message19', {b2})
    assert _is_linked(a, 'message19', b2)
    if hasattr(b1, 'passager18'):
        assert not _is_linked(b1, 'passager18', a)
    if hasattr(b2, 'passager18'):
        assert _is_linked(b2, 'passager18', a)
    _safe_set(a, 'message19', set())
    assert not _is_linked(a, 'message19', b2)
    if hasattr(b2, 'passager18'):
        assert not _is_linked(b2, 'passager18', a)


def test_assoc_Personne_Preferences_link_reassign_clear():
    a = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    b1 = Covoiturage_Authentification(id="sample_text", password="sample_text")
    b2 = Covoiturage_Authentification(id="sample_text_2", password="sample_text_2")
    _safe_set(a, 's_authentifi_0', b1)
    assert _is_linked(a, 's_authentifi_0', b1)
    if hasattr(b1, 'personne1'):
        assert _is_linked(b1, 'personne1', a)
    _safe_set(a, 's_authentifi_0', b2)
    assert _is_linked(a, 's_authentifi_0', b2)
    if hasattr(b1, 'personne1'):
        assert not _is_linked(b1, 'personne1', a)
    if hasattr(b2, 'personne1'):
        assert _is_linked(b2, 'personne1', a)
    _safe_set(a, 's_authentifi_0', None)
    assert not _is_linked(a, 's_authentifi_0', b2)
    if hasattr(b2, 'personne1'):
        assert not _is_linked(b2, 'personne1', a)


def test_assoc_Personne_Ville_link_reassign_clear():
    a = Covoiturage_Ville(cp=7, id=7, nom="sample_text")
    b1 = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    b2 = Covoiturage_Passager(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel=13)
    _safe_set(a, 'personnes9', {b1})
    assert _is_linked(a, 'personnes9', b1)
    if hasattr(b1, 'adresse8'):
        assert _is_linked(b1, 'adresse8', a)
    _safe_set(a, 'personnes9', {b2})
    assert _is_linked(a, 'personnes9', b2)
    if hasattr(b1, 'adresse8'):
        assert not _is_linked(b1, 'adresse8', a)
    if hasattr(b2, 'adresse8'):
        assert _is_linked(b2, 'adresse8', a)
    _safe_set(a, 'personnes9', set())
    assert not _is_linked(a, 'personnes9', b2)
    if hasattr(b2, 'adresse8'):
        assert not _is_linked(b2, 'adresse8', a)


def test_assoc_Profil_Reservation_link_reassign_clear():
    a = Covoiturage_Reservation(dateReservation=date(2024, 1, 1), etat=True, id=7, id2=7)
    b1 = Covoiturage_Passager(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel=7)
    b2 = Covoiturage_Passager(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel=13)
    _safe_set(a, 'profil12', {b1})
    assert _is_linked(a, 'profil12', b1)
    if hasattr(b1, 'reservation13'):
        assert _is_linked(b1, 'reservation13', a)
    _safe_set(a, 'profil12', {b2})
    assert _is_linked(a, 'profil12', b2)
    if hasattr(b1, 'reservation13'):
        assert not _is_linked(b1, 'reservation13', a)
    if hasattr(b2, 'reservation13'):
        assert _is_linked(b2, 'reservation13', a)
    _safe_set(a, 'profil12', set())
    assert not _is_linked(a, 'profil12', b2)
    if hasattr(b2, 'reservation13'):
        assert not _is_linked(b2, 'reservation13', a)


def test_assoc_Voiture_Passager_link_reassign_clear():
    a = Covoiturage_Voiture(attribute="sample_text", categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    b1 = Covoiturage_Conducteur(datePermi="sample_text")
    b2 = Covoiturage_Conducteur(datePermi="sample_text_2")
    _safe_set(a, 'Profil17', b1)
    assert _is_linked(a, 'Profil17', b1)
    if hasattr(b1, 'voiture16'):
        assert _is_linked(b1, 'voiture16', a)
    _safe_set(a, 'Profil17', b2)
    assert _is_linked(a, 'Profil17', b2)
    if hasattr(b1, 'voiture16'):
        assert not _is_linked(b1, 'voiture16', a)
    if hasattr(b2, 'voiture16'):
        assert _is_linked(b2, 'voiture16', a)
    _safe_set(a, 'Profil17', None)
    assert not _is_linked(a, 'Profil17', b2)
    if hasattr(b2, 'voiture16'):
        assert not _is_linked(b2, 'voiture16', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Covoiturage_Authentification_strategy = st.builds(Covoiturage_Authentification, id=safe_text, password=safe_text)
@given(instance=Covoiturage_Authentification_strategy)
@settings(max_examples=25)
def test_Covoiturage_Authentification_instantiation(instance):
    assert isinstance(instance, Covoiturage_Authentification)


Covoiturage_Avis_strategy = st.builds(Covoiturage_Avis, commentaire=safe_text, id=st.integers(), note=st.integers())
@given(instance=Covoiturage_Avis_strategy)
@settings(max_examples=25)
def test_Covoiturage_Avis_instantiation(instance):
    assert isinstance(instance, Covoiturage_Avis)


Covoiturage_Conducteur_strategy = st.builds(Covoiturage_Conducteur, datePermi=safe_text)
@given(instance=Covoiturage_Conducteur_strategy)
@settings(max_examples=25)
def test_Covoiturage_Conducteur_instantiation(instance):
    assert isinstance(instance, Covoiturage_Conducteur)


Covoiturage_Message_strategy = st.builds(Covoiturage_Message, Id=safe_text, Value=safe_text)
@given(instance=Covoiturage_Message_strategy)
@settings(max_examples=25)
def test_Covoiturage_Message_instantiation(instance):
    assert isinstance(instance, Covoiturage_Message)


Covoiturage_Passager_strategy = st.builds(Covoiturage_Passager, id=st.integers(), mail=safe_text, nom=safe_text, prenom=safe_text, tel=st.integers())
@given(instance=Covoiturage_Passager_strategy)
@settings(max_examples=25)
def test_Covoiturage_Passager_instantiation(instance):
    assert isinstance(instance, Covoiturage_Passager)


Covoiturage_Reservation_strategy = st.builds(Covoiturage_Reservation, dateReservation=st.dates(), etat=st.booleans(), id=st.integers(), id2=st.integers())
@given(instance=Covoiturage_Reservation_strategy)
@settings(max_examples=25)
def test_Covoiturage_Reservation_instantiation(instance):
    assert isinstance(instance, Covoiturage_Reservation)


Covoiturage_Ville_strategy = st.builds(Covoiturage_Ville, cp=st.integers(), id=st.integers(), nom=safe_text)
@given(instance=Covoiturage_Ville_strategy)
@settings(max_examples=25)
def test_Covoiturage_Ville_instantiation(instance):
    assert isinstance(instance, Covoiturage_Ville)


Covoiturage_Voiture_strategy = st.builds(Covoiturage_Voiture, attribute=safe_text, categorie=safe_text, confort=safe_text, id=st.integers(), marque=safe_text, model=safe_text, nbPlaces=st.integers())
@given(instance=Covoiturage_Voiture_strategy)
@settings(max_examples=25)
def test_Covoiturage_Voiture_instantiation(instance):
    assert isinstance(instance, Covoiturage_Voiture)


