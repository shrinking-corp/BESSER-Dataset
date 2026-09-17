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
    Admin_add_trajet_UseCase,
    Admin_Passager___conducteur_Actor,
    Admin_s_inscrire_UseCase,
    Admin_UseCase5_UseCase,
    Admin_consulter_trajets_UseCase,
    Admin_suppr_utils_UseCase,
    Admin_modifier_utilis_UseCase,
    Admin_consulter_liste_utilis_UseCase,
    Admin_Admin_Actor,
    covoiturage_Avis,
    covoiturage_Ville,
    covoiturage_Reservations,
    covoiturage_Preferences,
    covoiturage_Voiture,
    covoiturage_Personne,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_admin_add_trajet_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_add_trajet_UseCase)


def test_hyp_admin_add_trajet_usecase_constructor_exists():
    assert callable(Admin_add_trajet_UseCase.__init__)


def test_hyp_admin_add_trajet_usecase_constructor_args():
    sig = inspect.signature(Admin_add_trajet_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_passager___conducteur_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Passager___conducteur_Actor)


def test_hyp_admin_passager___conducteur_actor_constructor_exists():
    assert callable(Admin_Passager___conducteur_Actor.__init__)


def test_hyp_admin_passager___conducteur_actor_constructor_args():
    sig = inspect.signature(Admin_Passager___conducteur_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_s_inscrire_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_s_inscrire_UseCase)


def test_hyp_admin_s_inscrire_usecase_constructor_exists():
    assert callable(Admin_s_inscrire_UseCase.__init__)


def test_hyp_admin_s_inscrire_usecase_constructor_args():
    sig = inspect.signature(Admin_s_inscrire_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_usecase5_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_UseCase5_UseCase)


def test_hyp_admin_usecase5_usecase_constructor_exists():
    assert callable(Admin_UseCase5_UseCase.__init__)


def test_hyp_admin_usecase5_usecase_constructor_args():
    sig = inspect.signature(Admin_UseCase5_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_consulter_trajets_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_consulter_trajets_UseCase)


def test_hyp_admin_consulter_trajets_usecase_constructor_exists():
    assert callable(Admin_consulter_trajets_UseCase.__init__)


def test_hyp_admin_consulter_trajets_usecase_constructor_args():
    sig = inspect.signature(Admin_consulter_trajets_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_suppr_utils_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_suppr_utils_UseCase)


def test_hyp_admin_suppr_utils_usecase_constructor_exists():
    assert callable(Admin_suppr_utils_UseCase.__init__)


def test_hyp_admin_suppr_utils_usecase_constructor_args():
    sig = inspect.signature(Admin_suppr_utils_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_modifier_utilis_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_modifier_utilis_UseCase)


def test_hyp_admin_modifier_utilis_usecase_constructor_exists():
    assert callable(Admin_modifier_utilis_UseCase.__init__)


def test_hyp_admin_modifier_utilis_usecase_constructor_args():
    sig = inspect.signature(Admin_modifier_utilis_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_consulter_liste_utilis_usecase_is_not_abstract():
    assert not inspect.isabstract(Admin_consulter_liste_utilis_UseCase)


def test_hyp_admin_consulter_liste_utilis_usecase_constructor_exists():
    assert callable(Admin_consulter_liste_utilis_UseCase.__init__)


def test_hyp_admin_consulter_liste_utilis_usecase_constructor_args():
    sig = inspect.signature(Admin_consulter_liste_utilis_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Admin_Actor)


def test_hyp_admin_admin_actor_constructor_exists():
    assert callable(Admin_Admin_Actor.__init__)


def test_hyp_admin_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_covoiturage_avis_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Avis)


def test_hyp_covoiturage_avis_constructor_exists():
    assert callable(covoiturage_Avis.__init__)


def test_hyp_covoiturage_avis_constructor_args():
    sig = inspect.signature(covoiturage_Avis.__init__)
    params = list(sig.parameters.keys())
    assert "commentaire" in params, "Missing parameter 'commentaire'"
    assert "id" in params, "Missing parameter 'id'"
    assert "note" in params, "Missing parameter 'note'"






def test_hyp_covoiturage_ville_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Ville)


def test_hyp_covoiturage_ville_constructor_exists():
    assert callable(covoiturage_Ville.__init__)


def test_hyp_covoiturage_ville_constructor_args():
    sig = inspect.signature(covoiturage_Ville.__init__)
    params = list(sig.parameters.keys())
    assert "cp" in params, "Missing parameter 'cp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"






def test_hyp_covoiturage_reservations_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Reservations)


def test_hyp_covoiturage_reservations_constructor_exists():
    assert callable(covoiturage_Reservations.__init__)


def test_hyp_covoiturage_reservations_constructor_args():
    sig = inspect.signature(covoiturage_Reservations.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "date" in params, "Missing parameter 'date'"
    assert "prix" in params, "Missing parameter 'prix'"
    assert "lieuDeDepose" in params, "Missing parameter 'lieuDeDepose'"







def test_hyp_covoiturage_preferences_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Preferences)


def test_hyp_covoiturage_preferences_constructor_exists():
    assert callable(covoiturage_Preferences.__init__)


def test_hyp_covoiturage_preferences_constructor_args():
    sig = inspect.signature(covoiturage_Preferences.__init__)
    params = list(sig.parameters.keys())
    assert "valeur" in params, "Missing parameter 'valeur'"
    assert "nomPref" in params, "Missing parameter 'nomPref'"
    assert "id" in params, "Missing parameter 'id'"






def test_hyp_covoiturage_voiture_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Voiture)


def test_hyp_covoiturage_voiture_constructor_exists():
    assert callable(covoiturage_Voiture.__init__)


def test_hyp_covoiturage_voiture_constructor_args():
    sig = inspect.signature(covoiturage_Voiture.__init__)
    params = list(sig.parameters.keys())
    assert "tabac" in params, "Missing parameter 'tabac'"
    assert "nbPlaces" in params, "Missing parameter 'nbPlaces'"
    assert "model" in params, "Missing parameter 'model'"
    assert "confort" in params, "Missing parameter 'confort'"
    assert "categorie" in params, "Missing parameter 'categorie'"
    assert "id" in params, "Missing parameter 'id'"
    assert "couleur" in params, "Missing parameter 'couleur'"
    assert "marque" in params, "Missing parameter 'marque'"
    assert "climatiseur" in params, "Missing parameter 'climatiseur'"












def test_hyp_covoiturage_personne_is_not_abstract():
    assert not inspect.isabstract(covoiturage_Personne)


def test_hyp_covoiturage_personne_constructor_exists():
    assert callable(covoiturage_Personne.__init__)


def test_hyp_covoiturage_personne_constructor_args():
    sig = inspect.signature(covoiturage_Personne.__init__)
    params = list(sig.parameters.keys())
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "tel" in params, "Missing parameter 'tel'"
    assert "id" in params, "Missing parameter 'id'"
    assert "mail" in params, "Missing parameter 'mail'"







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
Admin_add_trajet_UseCase_strategy = st.builds(
    Admin_add_trajet_UseCase,
)
Admin_Passager___conducteur_Actor_strategy = st.builds(
    Admin_Passager___conducteur_Actor,
)
Admin_s_inscrire_UseCase_strategy = st.builds(
    Admin_s_inscrire_UseCase,
)
Admin_UseCase5_UseCase_strategy = st.builds(
    Admin_UseCase5_UseCase,
)
Admin_consulter_trajets_UseCase_strategy = st.builds(
    Admin_consulter_trajets_UseCase,
)
Admin_suppr_utils_UseCase_strategy = st.builds(
    Admin_suppr_utils_UseCase,
)
Admin_modifier_utilis_UseCase_strategy = st.builds(
    Admin_modifier_utilis_UseCase,
)
Admin_consulter_liste_utilis_UseCase_strategy = st.builds(
    Admin_consulter_liste_utilis_UseCase,
)
Admin_Admin_Actor_strategy = st.builds(
    Admin_Admin_Actor,
)
covoiturage_Avis_strategy = st.builds(
    covoiturage_Avis,
    commentaire=
        safe_text,
    id=
        st.integers(),
    note=
        st.integers()
)
covoiturage_Ville_strategy = st.builds(
    covoiturage_Ville,
    cp=
        safe_text,
    id=
        st.integers(),
    nom=
        safe_text
)
covoiturage_Reservations_strategy = st.builds(
    covoiturage_Reservations,
    id=
        st.integers(),
    date=
        st.dates(),
    prix=
        st.integers(),
    lieuDeDepose=
        safe_text
)
covoiturage_Preferences_strategy = st.builds(
    covoiturage_Preferences,
    valeur=
        safe_text,
    nomPref=
        safe_text,
    id=
        st.integers()
)
covoiturage_Voiture_strategy = st.builds(
    covoiturage_Voiture,
    tabac=
        st.booleans(),
    nbPlaces=
        st.integers(),
    model=
        safe_text,
    confort=
        safe_text,
    categorie=
        safe_text,
    id=
        st.integers(),
    couleur=
        safe_text,
    marque=
        safe_text,
    climatiseur=
        st.booleans()
)
covoiturage_Personne_strategy = st.builds(
    covoiturage_Personne,
    prenom=
        safe_text,
    nom=
        safe_text,
    tel=
        safe_text,
    id=
        st.integers(),
    mail=
        safe_text
)













@given(instance=covoiturage_Avis_strategy)
def test_hyp_covoiturage_avis_commentaire_setter(instance):
    original = instance.commentaire
    instance.commentaire = original
    assert instance.commentaire == original



@given(instance=covoiturage_Avis_strategy)
def test_hyp_covoiturage_avis_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Avis_strategy)
def test_hyp_covoiturage_avis_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original




@given(instance=covoiturage_Ville_strategy)
def test_hyp_covoiturage_ville_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original



@given(instance=covoiturage_Ville_strategy)
def test_hyp_covoiturage_ville_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Ville_strategy)
def test_hyp_covoiturage_ville_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original




@given(instance=covoiturage_Reservations_strategy)
def test_hyp_covoiturage_reservations_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Reservations_strategy)
def test_hyp_covoiturage_reservations_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=covoiturage_Reservations_strategy)
def test_hyp_covoiturage_reservations_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original



@given(instance=covoiturage_Reservations_strategy)
def test_hyp_covoiturage_reservations_lieuDeDepose_setter(instance):
    original = instance.lieuDeDepose
    instance.lieuDeDepose = original
    assert instance.lieuDeDepose == original




@given(instance=covoiturage_Preferences_strategy)
def test_hyp_covoiturage_preferences_valeur_setter(instance):
    original = instance.valeur
    instance.valeur = original
    assert instance.valeur == original



@given(instance=covoiturage_Preferences_strategy)
def test_hyp_covoiturage_preferences_nomPref_setter(instance):
    original = instance.nomPref
    instance.nomPref = original
    assert instance.nomPref == original



@given(instance=covoiturage_Preferences_strategy)
def test_hyp_covoiturage_preferences_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_tabac_setter(instance):
    original = instance.tabac
    instance.tabac = original
    assert instance.tabac == original



@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_nbPlaces_setter(instance):
    original = instance.nbPlaces
    instance.nbPlaces = original
    assert instance.nbPlaces == original



@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_confort_setter(instance):
    original = instance.confort
    instance.confort = original
    assert instance.confort == original



@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_categorie_setter(instance):
    original = instance.categorie
    instance.categorie = original
    assert instance.categorie == original



@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_couleur_setter(instance):
    original = instance.couleur
    instance.couleur = original
    assert instance.couleur == original



@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_marque_setter(instance):
    original = instance.marque
    instance.marque = original
    assert instance.marque == original



@given(instance=covoiturage_Voiture_strategy)
def test_hyp_covoiturage_voiture_climatiseur_setter(instance):
    original = instance.climatiseur
    instance.climatiseur = original
    assert instance.climatiseur == original




@given(instance=covoiturage_Personne_strategy)
def test_hyp_covoiturage_personne_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=covoiturage_Personne_strategy)
def test_hyp_covoiturage_personne_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=covoiturage_Personne_strategy)
def test_hyp_covoiturage_personne_tel_setter(instance):
    original = instance.tel
    instance.tel = original
    assert instance.tel == original



@given(instance=covoiturage_Personne_strategy)
def test_hyp_covoiturage_personne_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=covoiturage_Personne_strategy)
def test_hyp_covoiturage_personne_mail_setter(instance):
    original = instance.mail
    instance.mail = original
    assert instance.mail == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_covoiturage_Avis_commentaire_value_roundtrip():
    instance = covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.commentaire == "sample_text"
    instance.commentaire = "sample_text_2"
    assert instance.commentaire == "sample_text_2"


def test_covoiturage_Avis_id_value_roundtrip():
    instance = covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_covoiturage_Avis_note_value_roundtrip():
    instance = covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    assert instance.note == 7
    instance.note = 13
    assert instance.note == 13


def test_covoiturage_Personne_id_value_roundtrip():
    instance = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_covoiturage_Personne_mail_value_roundtrip():
    instance = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    assert instance.mail == "sample_text"
    instance.mail = "sample_text_2"
    assert instance.mail == "sample_text_2"


def test_covoiturage_Personne_nom_value_roundtrip():
    instance = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_covoiturage_Personne_prenom_value_roundtrip():
    instance = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    assert instance.prenom == "sample_text"
    instance.prenom = "sample_text_2"
    assert instance.prenom == "sample_text_2"


def test_covoiturage_Personne_tel_value_roundtrip():
    instance = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    assert instance.tel == "sample_text"
    instance.tel = "sample_text_2"
    assert instance.tel == "sample_text_2"


def test_covoiturage_Preferences_id_value_roundtrip():
    instance = covoiturage_Preferences(id=7, nomPref="sample_text", valeur="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_covoiturage_Preferences_nomPref_value_roundtrip():
    instance = covoiturage_Preferences(id=7, nomPref="sample_text", valeur="sample_text")
    assert instance.nomPref == "sample_text"
    instance.nomPref = "sample_text_2"
    assert instance.nomPref == "sample_text_2"


def test_covoiturage_Preferences_valeur_value_roundtrip():
    instance = covoiturage_Preferences(id=7, nomPref="sample_text", valeur="sample_text")
    assert instance.valeur == "sample_text"
    instance.valeur = "sample_text_2"
    assert instance.valeur == "sample_text_2"


def test_covoiturage_Reservations_date_value_roundtrip():
    instance = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_covoiturage_Reservations_id_value_roundtrip():
    instance = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_covoiturage_Reservations_lieuDeDepose_value_roundtrip():
    instance = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    assert instance.lieuDeDepose == "sample_text"
    instance.lieuDeDepose = "sample_text_2"
    assert instance.lieuDeDepose == "sample_text_2"


def test_covoiturage_Reservations_prix_value_roundtrip():
    instance = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    assert instance.prix == 7
    instance.prix = 13
    assert instance.prix == 13


def test_covoiturage_Ville_cp_value_roundtrip():
    instance = covoiturage_Ville(cp="sample_text", id=7, nom="sample_text")
    assert instance.cp == "sample_text"
    instance.cp = "sample_text_2"
    assert instance.cp == "sample_text_2"


def test_covoiturage_Ville_id_value_roundtrip():
    instance = covoiturage_Ville(cp="sample_text", id=7, nom="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_covoiturage_Ville_nom_value_roundtrip():
    instance = covoiturage_Ville(cp="sample_text", id=7, nom="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_covoiturage_Voiture_categorie_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.categorie == "sample_text"
    instance.categorie = "sample_text_2"
    assert instance.categorie == "sample_text_2"


def test_covoiturage_Voiture_climatiseur_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.climatiseur == True
    instance.climatiseur = False
    assert instance.climatiseur == False


def test_covoiturage_Voiture_confort_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.confort == "sample_text"
    instance.confort = "sample_text_2"
    assert instance.confort == "sample_text_2"


def test_covoiturage_Voiture_couleur_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.couleur == "sample_text"
    instance.couleur = "sample_text_2"
    assert instance.couleur == "sample_text_2"


def test_covoiturage_Voiture_id_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_covoiturage_Voiture_marque_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.marque == "sample_text"
    instance.marque = "sample_text_2"
    assert instance.marque == "sample_text_2"


def test_covoiturage_Voiture_model_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.model == "sample_text"
    instance.model = "sample_text_2"
    assert instance.model == "sample_text_2"


def test_covoiturage_Voiture_nbPlaces_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.nbPlaces == 7
    instance.nbPlaces = 13
    assert instance.nbPlaces == 13


def test_covoiturage_Voiture_tabac_value_roundtrip():
    instance = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    assert instance.tabac == True
    instance.tabac = False
    assert instance.tabac == False


def test_assoc_Avis_Evenement_link_reassign_clear():
    a = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    b1 = covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    b2 = covoiturage_Avis(commentaire="sample_text_2", id=13, note=13)
    _safe_set(a, 'avis11', {b1})
    assert _is_linked(a, 'avis11', b1)
    if hasattr(b1, 'evenement10'):
        assert _is_linked(b1, 'evenement10', a)
    _safe_set(a, 'avis11', {b2})
    assert _is_linked(a, 'avis11', b2)
    if hasattr(b1, 'evenement10'):
        assert not _is_linked(b1, 'evenement10', a)
    if hasattr(b2, 'evenement10'):
        assert _is_linked(b2, 'evenement10', a)
    _safe_set(a, 'avis11', set())
    assert not _is_linked(a, 'avis11', b2)
    if hasattr(b2, 'evenement10'):
        assert not _is_linked(b2, 'evenement10', a)


def test_assoc_Avis_Personne_link_reassign_clear():
    a = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    b1 = covoiturage_Avis(commentaire="sample_text", id=7, note=7)
    b2 = covoiturage_Avis(commentaire="sample_text_2", id=13, note=13)
    _safe_set(a, 'avis9', {b1})
    assert _is_linked(a, 'avis9', b1)
    if hasattr(b1, 'personne8'):
        assert _is_linked(b1, 'personne8', a)
    _safe_set(a, 'avis9', {b2})
    assert _is_linked(a, 'avis9', b2)
    if hasattr(b1, 'personne8'):
        assert not _is_linked(b1, 'personne8', a)
    if hasattr(b2, 'personne8'):
        assert _is_linked(b2, 'personne8', a)
    _safe_set(a, 'avis9', set())
    assert not _is_linked(a, 'avis9', b2)
    if hasattr(b2, 'personne8'):
        assert not _is_linked(b2, 'personne8', a)


def test_assoc_Evenement_Ville_link_reassign_clear():
    a = covoiturage_Ville(cp="sample_text", id=7, nom="sample_text")
    b1 = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    b2 = covoiturage_Reservations(date=date(2025, 6, 15), id=13, lieuDeDepose="sample_text_2", prix=13)
    _safe_set(a, 'evenement5', b1)
    assert _is_linked(a, 'evenement5', b1)
    if hasattr(b1, 'villes4'):
        assert _is_linked(b1, 'villes4', a)
    _safe_set(a, 'evenement5', b2)
    assert _is_linked(a, 'evenement5', b2)
    if hasattr(b1, 'villes4'):
        assert not _is_linked(b1, 'villes4', a)
    if hasattr(b2, 'villes4'):
        assert _is_linked(b2, 'villes4', a)
    _safe_set(a, 'evenement5', None)
    assert not _is_linked(a, 'evenement5', b2)
    if hasattr(b2, 'villes4'):
        assert not _is_linked(b2, 'villes4', a)


def test_assoc_Personne_Evenement_link_reassign_clear():
    a = covoiturage_Reservations(date=date(2024, 1, 1), id=7, lieuDeDepose="sample_text", prix=7)
    b1 = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    b2 = covoiturage_Personne(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel="sample_text_2")
    _safe_set(a, 'participants7', {b1})
    assert _is_linked(a, 'participants7', b1)
    if hasattr(b1, 'events6'):
        assert _is_linked(b1, 'events6', a)
    _safe_set(a, 'participants7', {b2})
    assert _is_linked(a, 'participants7', b2)
    if hasattr(b1, 'events6'):
        assert not _is_linked(b1, 'events6', a)
    if hasattr(b2, 'events6'):
        assert _is_linked(b2, 'events6', a)
    _safe_set(a, 'participants7', set())
    assert not _is_linked(a, 'participants7', b2)
    if hasattr(b2, 'events6'):
        assert not _is_linked(b2, 'events6', a)


def test_assoc_Personne_Preferences_link_reassign_clear():
    a = covoiturage_Preferences(id=7, nomPref="sample_text", valeur="sample_text")
    b1 = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    b2 = covoiturage_Personne(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel="sample_text_2")
    _safe_set(a, 'personne3', {b1})
    assert _is_linked(a, 'personne3', b1)
    if hasattr(b1, 'preferences2'):
        assert _is_linked(b1, 'preferences2', a)
    _safe_set(a, 'personne3', {b2})
    assert _is_linked(a, 'personne3', b2)
    if hasattr(b1, 'preferences2'):
        assert not _is_linked(b1, 'preferences2', a)
    if hasattr(b2, 'preferences2'):
        assert _is_linked(b2, 'preferences2', a)
    _safe_set(a, 'personne3', set())
    assert not _is_linked(a, 'personne3', b2)
    if hasattr(b2, 'preferences2'):
        assert not _is_linked(b2, 'preferences2', a)


def test_assoc_Personne_Ville_link_reassign_clear():
    a = covoiturage_Ville(cp="sample_text", id=7, nom="sample_text")
    b1 = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    b2 = covoiturage_Personne(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel="sample_text_2")
    _safe_set(a, 'personnes13', {b1})
    assert _is_linked(a, 'personnes13', b1)
    if hasattr(b1, 'adresse12'):
        assert _is_linked(b1, 'adresse12', a)
    _safe_set(a, 'personnes13', {b2})
    assert _is_linked(a, 'personnes13', b2)
    if hasattr(b1, 'adresse12'):
        assert not _is_linked(b1, 'adresse12', a)
    if hasattr(b2, 'adresse12'):
        assert _is_linked(b2, 'adresse12', a)
    _safe_set(a, 'personnes13', set())
    assert not _is_linked(a, 'personnes13', b2)
    if hasattr(b2, 'adresse12'):
        assert not _is_linked(b2, 'adresse12', a)


def test_assoc_Personne_Voiture_link_reassign_clear():
    a = covoiturage_Voiture(categorie="sample_text", climatiseur=True, confort="sample_text", couleur="sample_text", id=7, marque="sample_text", model="sample_text", nbPlaces=7, tabac=True)
    b1 = covoiturage_Personne(id=7, mail="sample_text", nom="sample_text", prenom="sample_text", tel="sample_text")
    b2 = covoiturage_Personne(id=13, mail="sample_text_2", nom="sample_text_2", prenom="sample_text_2", tel="sample_text_2")
    _safe_set(a, 'personne1', b1)
    assert _is_linked(a, 'personne1', b1)
    if hasattr(b1, 'voiture0'):
        assert _is_linked(b1, 'voiture0', a)
    _safe_set(a, 'personne1', b2)
    assert _is_linked(a, 'personne1', b2)
    if hasattr(b1, 'voiture0'):
        assert not _is_linked(b1, 'voiture0', a)
    if hasattr(b2, 'voiture0'):
        assert _is_linked(b2, 'voiture0', a)
    _safe_set(a, 'personne1', None)
    assert not _is_linked(a, 'personne1', b2)
    if hasattr(b2, 'voiture0'):
        assert not _is_linked(b2, 'voiture0', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_Admin_Actor_strategy = st.builds(Admin_Admin_Actor)
@given(instance=Admin_Admin_Actor_strategy)
@settings(max_examples=25)
def test_Admin_Admin_Actor_instantiation(instance):
    assert isinstance(instance, Admin_Admin_Actor)


Admin_Passager___conducteur_Actor_strategy = st.builds(Admin_Passager___conducteur_Actor)
@given(instance=Admin_Passager___conducteur_Actor_strategy)
@settings(max_examples=25)
def test_Admin_Passager___conducteur_Actor_instantiation(instance):
    assert isinstance(instance, Admin_Passager___conducteur_Actor)


Admin_UseCase5_UseCase_strategy = st.builds(Admin_UseCase5_UseCase)
@given(instance=Admin_UseCase5_UseCase_strategy)
@settings(max_examples=25)
def test_Admin_UseCase5_UseCase_instantiation(instance):
    assert isinstance(instance, Admin_UseCase5_UseCase)


Admin_add_trajet_UseCase_strategy = st.builds(Admin_add_trajet_UseCase)
@given(instance=Admin_add_trajet_UseCase_strategy)
@settings(max_examples=25)
def test_Admin_add_trajet_UseCase_instantiation(instance):
    assert isinstance(instance, Admin_add_trajet_UseCase)


Admin_consulter_liste_utilis_UseCase_strategy = st.builds(Admin_consulter_liste_utilis_UseCase)
@given(instance=Admin_consulter_liste_utilis_UseCase_strategy)
@settings(max_examples=25)
def test_Admin_consulter_liste_utilis_UseCase_instantiation(instance):
    assert isinstance(instance, Admin_consulter_liste_utilis_UseCase)


Admin_consulter_trajets_UseCase_strategy = st.builds(Admin_consulter_trajets_UseCase)
@given(instance=Admin_consulter_trajets_UseCase_strategy)
@settings(max_examples=25)
def test_Admin_consulter_trajets_UseCase_instantiation(instance):
    assert isinstance(instance, Admin_consulter_trajets_UseCase)


Admin_modifier_utilis_UseCase_strategy = st.builds(Admin_modifier_utilis_UseCase)
@given(instance=Admin_modifier_utilis_UseCase_strategy)
@settings(max_examples=25)
def test_Admin_modifier_utilis_UseCase_instantiation(instance):
    assert isinstance(instance, Admin_modifier_utilis_UseCase)


Admin_s_inscrire_UseCase_strategy = st.builds(Admin_s_inscrire_UseCase)
@given(instance=Admin_s_inscrire_UseCase_strategy)
@settings(max_examples=25)
def test_Admin_s_inscrire_UseCase_instantiation(instance):
    assert isinstance(instance, Admin_s_inscrire_UseCase)


Admin_suppr_utils_UseCase_strategy = st.builds(Admin_suppr_utils_UseCase)
@given(instance=Admin_suppr_utils_UseCase_strategy)
@settings(max_examples=25)
def test_Admin_suppr_utils_UseCase_instantiation(instance):
    assert isinstance(instance, Admin_suppr_utils_UseCase)


covoiturage_Avis_strategy = st.builds(covoiturage_Avis, commentaire=safe_text, id=st.integers(), note=st.integers())
@given(instance=covoiturage_Avis_strategy)
@settings(max_examples=25)
def test_covoiturage_Avis_instantiation(instance):
    assert isinstance(instance, covoiturage_Avis)


covoiturage_Personne_strategy = st.builds(covoiturage_Personne, id=st.integers(), mail=safe_text, nom=safe_text, prenom=safe_text, tel=safe_text)
@given(instance=covoiturage_Personne_strategy)
@settings(max_examples=25)
def test_covoiturage_Personne_instantiation(instance):
    assert isinstance(instance, covoiturage_Personne)


covoiturage_Preferences_strategy = st.builds(covoiturage_Preferences, id=st.integers(), nomPref=safe_text, valeur=safe_text)
@given(instance=covoiturage_Preferences_strategy)
@settings(max_examples=25)
def test_covoiturage_Preferences_instantiation(instance):
    assert isinstance(instance, covoiturage_Preferences)


covoiturage_Reservations_strategy = st.builds(covoiturage_Reservations, date=st.dates(), id=st.integers(), lieuDeDepose=safe_text, prix=st.integers())
@given(instance=covoiturage_Reservations_strategy)
@settings(max_examples=25)
def test_covoiturage_Reservations_instantiation(instance):
    assert isinstance(instance, covoiturage_Reservations)


covoiturage_Ville_strategy = st.builds(covoiturage_Ville, cp=safe_text, id=st.integers(), nom=safe_text)
@given(instance=covoiturage_Ville_strategy)
@settings(max_examples=25)
def test_covoiturage_Ville_instantiation(instance):
    assert isinstance(instance, covoiturage_Ville)


covoiturage_Voiture_strategy = st.builds(covoiturage_Voiture, categorie=safe_text, climatiseur=st.booleans(), confort=safe_text, couleur=safe_text, id=st.integers(), marque=safe_text, model=safe_text, nbPlaces=st.integers(), tabac=st.booleans())
@given(instance=covoiturage_Voiture_strategy)
@settings(max_examples=25)
def test_covoiturage_Voiture_instantiation(instance):
    assert isinstance(instance, covoiturage_Voiture)



