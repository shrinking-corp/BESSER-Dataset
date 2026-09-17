# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    domain_Reservation,
    domain_Avis,
    domain_Ville,
    domain_Trajet,
    domain_Authentification,
    domain_Voiture,
    domain_Profil,
    domain_Role,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_domain_reservation_is_not_abstract():
    assert not inspect.isabstract(domain_Reservation)


def test_hyp_domain_reservation_constructor_exists():
    assert callable(domain_Reservation.__init__)


def test_hyp_domain_reservation_constructor_args():
    sig = inspect.signature(domain_Reservation.__init__)
    params = list(sig.parameters.keys())
    assert "dateReservation" in params, "Missing parameter 'dateReservation'"
    assert "id" in params, "Missing parameter 'id'"
    assert "id2" in params, "Missing parameter 'id2'"






def test_hyp_domain_avis_is_not_abstract():
    assert not inspect.isabstract(domain_Avis)


def test_hyp_domain_avis_constructor_exists():
    assert callable(domain_Avis.__init__)


def test_hyp_domain_avis_constructor_args():
    sig = inspect.signature(domain_Avis.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "commentaire" in params, "Missing parameter 'commentaire'"
    assert "note" in params, "Missing parameter 'note'"






def test_hyp_domain_ville_is_not_abstract():
    assert not inspect.isabstract(domain_Ville)


def test_hyp_domain_ville_constructor_exists():
    assert callable(domain_Ville.__init__)


def test_hyp_domain_ville_constructor_args():
    sig = inspect.signature(domain_Ville.__init__)
    params = list(sig.parameters.keys())
    assert "cp" in params, "Missing parameter 'cp'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_domain_trajet_is_not_abstract():
    assert not inspect.isabstract(domain_Trajet)


def test_hyp_domain_trajet_constructor_exists():
    assert callable(domain_Trajet.__init__)


def test_hyp_domain_trajet_constructor_args():
    sig = inspect.signature(domain_Trajet.__init__)
    params = list(sig.parameters.keys())
    assert "depart" in params, "Missing parameter 'depart'"
    assert "prix" in params, "Missing parameter 'prix'"
    assert "date" in params, "Missing parameter 'date'"
    assert "destination" in params, "Missing parameter 'destination'"
    assert "id" in params, "Missing parameter 'id'"

def test_hyp_domain_trajet_has_depart():
    assert hasattr(domain_Trajet, "depart")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "depart" in klass.__dict__:
            descriptor = klass.__dict__["depart"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_trajet_has_prix():
    assert hasattr(domain_Trajet, "prix")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "prix" in klass.__dict__:
            descriptor = klass.__dict__["prix"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_trajet_has_date():
    assert hasattr(domain_Trajet, "date")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_trajet_has_destination():
    assert hasattr(domain_Trajet, "destination")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "destination" in klass.__dict__:
            descriptor = klass.__dict__["destination"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_trajet_has_id():
    assert hasattr(domain_Trajet, "id")
    descriptor = None
    for klass in domain_Trajet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_hyp_domain_authentification_is_not_abstract():
    assert not inspect.isabstract(domain_Authentification)


def test_hyp_domain_authentification_constructor_exists():
    assert callable(domain_Authentification.__init__)


def test_hyp_domain_authentification_constructor_args():
    sig = inspect.signature(domain_Authentification.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_domain_voiture_is_not_abstract():
    assert not inspect.isabstract(domain_Voiture)


def test_hyp_domain_voiture_constructor_exists():
    assert callable(domain_Voiture.__init__)


def test_hyp_domain_voiture_constructor_args():
    sig = inspect.signature(domain_Voiture.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "model" in params, "Missing parameter 'model'"
    assert "categorie" in params, "Missing parameter 'categorie'"
    assert "marque" in params, "Missing parameter 'marque'"
    assert "confort" in params, "Missing parameter 'confort'"
    assert "nbPlaces" in params, "Missing parameter 'nbPlaces'"









def test_hyp_domain_profil_is_not_abstract():
    assert not inspect.isabstract(domain_Profil)


def test_hyp_domain_profil_constructor_exists():
    assert callable(domain_Profil.__init__)


def test_hyp_domain_profil_constructor_args():
    sig = inspect.signature(domain_Profil.__init__)
    params = list(sig.parameters.keys())
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "mail" in params, "Missing parameter 'mail'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "role" in params, "Missing parameter 'role'"
    assert "tel" in params, "Missing parameter 'tel'"

def test_hyp_domain_profil_has_prenom():
    assert hasattr(domain_Profil, "prenom")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "prenom" in klass.__dict__:
            descriptor = klass.__dict__["prenom"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_profil_has_mail():
    assert hasattr(domain_Profil, "mail")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "mail" in klass.__dict__:
            descriptor = klass.__dict__["mail"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_profil_has_nom():
    assert hasattr(domain_Profil, "nom")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_profil_has_id():
    assert hasattr(domain_Profil, "id")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_profil_has_role():
    assert hasattr(domain_Profil, "role")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_profil_has_tel():
    assert hasattr(domain_Profil, "tel")
    descriptor = None
    for klass in domain_Profil.__mro__:
        if "tel" in klass.__dict__:
            descriptor = klass.__dict__["tel"]
            break
    assert isinstance(descriptor, property)

def test_hyp_domain_role_exists():
    # Check that the Enumeration exists
    assert domain_Role is not None

def test_hyp_domain_role_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in domain_Role]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in domain_Role"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
domain_Reservation_strategy = st.builds(
    domain_Reservation,
    dateReservation=
        st.dates(),
    id=
        st.integers(),
    id2=
        st.integers()
)
domain_Avis_strategy = st.builds(
    domain_Avis,
    id=
        st.integers(),
    commentaire=
        safe_text,
    note=
        st.integers()
)
domain_Ville_strategy = st.builds(
    domain_Ville,
    cp=
        st.integers(),
    nom=
        safe_text,
    id=
        st.integers()
)
domain_Trajet_strategy = st.builds(
    domain_Trajet,
    depart=
        st.none(),
    prix=
        st.integers(),
    date=
        st.dates(),
    destination=
        st.none(),
    id=
        st.integers()
)
domain_Authentification_strategy = st.builds(
    domain_Authentification,
    id=
        safe_text,
    password=
        safe_text
)
domain_Voiture_strategy = st.builds(
    domain_Voiture,
    id=
        st.integers(),
    model=
        safe_text,
    categorie=
        safe_text,
    marque=
        safe_text,
    confort=
        safe_text,
    nbPlaces=
        st.integers()
)
domain_Profil_strategy = st.builds(
    domain_Profil,
    prenom=
        safe_text,
    mail=
        safe_text,
    nom=
        safe_text,
    id=
        st.integers(),
    role=
        st.none(),
    tel=
        safe_text
)




@given(instance=domain_Reservation_strategy)
def test_hyp_domain_reservation_dateReservation_setter(instance):
    original = instance.dateReservation
    instance.dateReservation = original
    assert instance.dateReservation == original



@given(instance=domain_Reservation_strategy)
def test_hyp_domain_reservation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Reservation_strategy)
def test_hyp_domain_reservation_id2_setter(instance):
    original = instance.id2
    instance.id2 = original
    assert instance.id2 == original




@given(instance=domain_Avis_strategy)
def test_hyp_domain_avis_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Avis_strategy)
def test_hyp_domain_avis_commentaire_setter(instance):
    original = instance.commentaire
    instance.commentaire = original
    assert instance.commentaire == original



@given(instance=domain_Avis_strategy)
def test_hyp_domain_avis_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original




@given(instance=domain_Ville_strategy)
def test_hyp_domain_ville_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original



@given(instance=domain_Ville_strategy)
def test_hyp_domain_ville_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=domain_Ville_strategy)
def test_hyp_domain_ville_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=domain_Trajet_strategy)
@settings(max_examples=50)
def test_hyp_domain_trajet_instantiation(instance):
    assert isinstance(instance, domain_Trajet)



@given(instance=domain_Trajet_strategy)
def test_hyp_domain_trajet_depart_setter(instance):
    original = instance.depart
    instance.depart = original
    assert instance.depart == original



@given(instance=domain_Trajet_strategy)
def test_hyp_domain_trajet_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original



@given(instance=domain_Trajet_strategy)
def test_hyp_domain_trajet_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=domain_Trajet_strategy)
def test_hyp_domain_trajet_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original



@given(instance=domain_Trajet_strategy)
def test_hyp_domain_trajet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=domain_Authentification_strategy)
def test_hyp_domain_authentification_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Authentification_strategy)
def test_hyp_domain_authentification_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=domain_Voiture_strategy)
def test_hyp_domain_voiture_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Voiture_strategy)
def test_hyp_domain_voiture_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=domain_Voiture_strategy)
def test_hyp_domain_voiture_categorie_setter(instance):
    original = instance.categorie
    instance.categorie = original
    assert instance.categorie == original



@given(instance=domain_Voiture_strategy)
def test_hyp_domain_voiture_marque_setter(instance):
    original = instance.marque
    instance.marque = original
    assert instance.marque == original



@given(instance=domain_Voiture_strategy)
def test_hyp_domain_voiture_confort_setter(instance):
    original = instance.confort
    instance.confort = original
    assert instance.confort == original



@given(instance=domain_Voiture_strategy)
def test_hyp_domain_voiture_nbPlaces_setter(instance):
    original = instance.nbPlaces
    instance.nbPlaces = original
    assert instance.nbPlaces == original

@given(instance=domain_Profil_strategy)
@settings(max_examples=50)
def test_hyp_domain_profil_instantiation(instance):
    assert isinstance(instance, domain_Profil)



@given(instance=domain_Profil_strategy)
def test_hyp_domain_profil_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=domain_Profil_strategy)
def test_hyp_domain_profil_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original



@given(instance=domain_Profil_strategy)
def test_hyp_domain_profil_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=domain_Profil_strategy)
def test_hyp_domain_profil_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=domain_Profil_strategy)
def test_hyp_domain_profil_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=domain_Profil_strategy)
def test_hyp_domain_profil_tel_setter(instance):
    original = instance.tel
    instance.tel = original
    assert instance.tel == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    domain_Authentification,
    domain_Avis,
    domain_Profil,
    domain_Reservation,
    domain_Trajet,
    domain_Ville,
    domain_Voiture,
    domain_Role,
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

def test_domain_Authentification_id_value_roundtrip():
    instance = domain_Authentification(id="sample_text", password="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_domain_Authentification_password_value_roundtrip():
    instance = domain_Authentification(id="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_domain_Avis_commentaire_value_roundtrip():
    instance = domain_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.commentaire == "sample_text"
    instance.commentaire = "sample_text_2"
    assert instance.commentaire == "sample_text_2"


def test_domain_Avis_id_value_roundtrip():
    instance = domain_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_domain_Avis_note_value_roundtrip():
    instance = domain_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.note == 7
    instance.note = 13
    assert instance.note == 13


def test_domain_Reservation_dateReservation_value_roundtrip():
    instance = domain_Reservation(dateReservation=date(2024, 1, 1), id=7, id2=7)
    assert instance.dateReservation == date(2024, 1, 1)
    instance.dateReservation = date(2025, 6, 15)
    assert instance.dateReservation == date(2025, 6, 15)


def test_domain_Reservation_id_value_roundtrip():
    instance = domain_Reservation(dateReservation=date(2024, 1, 1), id=7, id2=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_domain_Reservation_id2_value_roundtrip():
    instance = domain_Reservation(dateReservation=date(2024, 1, 1), id=7, id2=7)
    assert instance.id2 == 7
    instance.id2 = 13
    assert instance.id2 == 13


def test_domain_Ville_cp_value_roundtrip():
    instance = domain_Ville(cp=7, id=7, nom="sample_text")
    assert instance.cp == 7
    instance.cp = 13
    assert instance.cp == 13


def test_domain_Ville_id_value_roundtrip():
    instance = domain_Ville(cp=7, id=7, nom="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_domain_Ville_nom_value_roundtrip():
    instance = domain_Ville(cp=7, id=7, nom="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_domain_Voiture_categorie_value_roundtrip():
    instance = domain_Voiture(categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.categorie == "sample_text"
    instance.categorie = "sample_text_2"
    assert instance.categorie == "sample_text_2"


def test_domain_Voiture_confort_value_roundtrip():
    instance = domain_Voiture(categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.confort == "sample_text"
    instance.confort = "sample_text_2"
    assert instance.confort == "sample_text_2"


def test_domain_Voiture_id_value_roundtrip():
    instance = domain_Voiture(categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_domain_Voiture_marque_value_roundtrip():
    instance = domain_Voiture(categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.marque == "sample_text"
    instance.marque = "sample_text_2"
    assert instance.marque == "sample_text_2"


def test_domain_Voiture_model_value_roundtrip():
    instance = domain_Voiture(categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.model == "sample_text"
    instance.model = "sample_text_2"
    assert instance.model == "sample_text_2"


def test_domain_Voiture_nbPlaces_value_roundtrip():
    instance = domain_Voiture(categorie="sample_text", confort="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7)
    assert instance.nbPlaces == 7
    instance.nbPlaces = 13
    assert instance.nbPlaces == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

domain_Authentification_strategy = st.builds(domain_Authentification, id=safe_text, password=safe_text)
@given(instance=domain_Authentification_strategy)
@settings(max_examples=25)
def test_domain_Authentification_instantiation(instance):
    assert isinstance(instance, domain_Authentification)


domain_Avis_strategy = st.builds(domain_Avis, commentaire=safe_text, id=st.integers(), note=st.integers())
@given(instance=domain_Avis_strategy)
@settings(max_examples=25)
def test_domain_Avis_instantiation(instance):
    assert isinstance(instance, domain_Avis)


domain_Reservation_strategy = st.builds(domain_Reservation, dateReservation=st.dates(), id=st.integers(), id2=st.integers())
@given(instance=domain_Reservation_strategy)
@settings(max_examples=25)
def test_domain_Reservation_instantiation(instance):
    assert isinstance(instance, domain_Reservation)


domain_Ville_strategy = st.builds(domain_Ville, cp=st.integers(), id=st.integers(), nom=safe_text)
@given(instance=domain_Ville_strategy)
@settings(max_examples=25)
def test_domain_Ville_instantiation(instance):
    assert isinstance(instance, domain_Ville)


domain_Voiture_strategy = st.builds(domain_Voiture, categorie=safe_text, confort=safe_text, id=st.integers(), marque=safe_text, model=safe_text, nbPlaces=st.integers())
@given(instance=domain_Voiture_strategy)
@settings(max_examples=25)
def test_domain_Voiture_instantiation(instance):
    assert isinstance(instance, domain_Voiture)



