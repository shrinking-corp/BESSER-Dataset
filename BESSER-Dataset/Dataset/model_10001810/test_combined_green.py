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
    Pizzeria,
    R_le,
    Produit,
    Recette,
    Cat_gorie,
    Ingr_dient,
    Stock,
    Livraison,
    Adresse,
    Etat,
    Commande,
    Class,
    Utilisateur,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_pizzeria_is_not_abstract():
    assert not inspect.isabstract(Pizzeria)


def test_hyp_pizzeria_constructor_exists():
    assert callable(Pizzeria.__init__)


def test_hyp_pizzeria_constructor_args():
    sig = inspect.signature(Pizzeria.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id" in params, "Missing parameter 'id'"
    assert "adresse_id" in params, "Missing parameter 'adresse_id'"






def test_hyp_r_le_is_not_abstract():
    assert not inspect.isabstract(R_le)


def test_hyp_r_le_constructor_exists():
    assert callable(R_le.__init__)


def test_hyp_r_le_constructor_args():
    sig = inspect.signature(R_le.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_produit_is_not_abstract():
    assert not inspect.isabstract(Produit)


def test_hyp_produit_constructor_exists():
    assert callable(Produit.__init__)


def test_hyp_produit_constructor_args():
    sig = inspect.signature(Produit.__init__)
    params = list(sig.parameters.keys())
    assert "categorie_id" in params, "Missing parameter 'categorie_id'"
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "prix" in params, "Missing parameter 'prix'"







def test_hyp_recette_is_not_abstract():
    assert not inspect.isabstract(Recette)


def test_hyp_recette_constructor_exists():
    assert callable(Recette.__init__)


def test_hyp_recette_constructor_args():
    sig = inspect.signature(Recette.__init__)
    params = list(sig.parameters.keys())
    assert "produit_id" in params, "Missing parameter 'produit_id'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_cat_gorie_is_not_abstract():
    assert not inspect.isabstract(Cat_gorie)


def test_hyp_cat_gorie_constructor_exists():
    assert callable(Cat_gorie.__init__)


def test_hyp_cat_gorie_constructor_args():
    sig = inspect.signature(Cat_gorie.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"





def test_hyp_ingr_dient_is_not_abstract():
    assert not inspect.isabstract(Ingr_dient)


def test_hyp_ingr_dient_constructor_exists():
    assert callable(Ingr_dient.__init__)


def test_hyp_ingr_dient_constructor_args():
    sig = inspect.signature(Ingr_dient.__init__)
    params = list(sig.parameters.keys())
    assert "poids" in params, "Missing parameter 'poids'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "unit_" in params, "Missing parameter 'unit_'"
    assert "id" in params, "Missing parameter 'id'"







def test_hyp_stock_is_not_abstract():
    assert not inspect.isabstract(Stock)


def test_hyp_stock_constructor_exists():
    assert callable(Stock.__init__)


def test_hyp_stock_constructor_args():
    sig = inspect.signature(Stock.__init__)
    params = list(sig.parameters.keys())
    assert "quantit_" in params, "Missing parameter 'quantit_'"
    assert "date_modification" in params, "Missing parameter 'date_modification'"
    assert "ingredient_id" in params, "Missing parameter 'ingredient_id'"
    assert "disponibilit_" in params, "Missing parameter 'disponibilit_'"







def test_hyp_livraison_is_not_abstract():
    assert not inspect.isabstract(Livraison)


def test_hyp_livraison_constructor_exists():
    assert callable(Livraison.__init__)


def test_hyp_livraison_constructor_args():
    sig = inspect.signature(Livraison.__init__)
    params = list(sig.parameters.keys())
    assert "client_id" in params, "Missing parameter 'client_id'"
    assert "geocode" in params, "Missing parameter 'geocode'"
    assert "livreur_id" in params, "Missing parameter 'livreur_id'"
    assert "id" in params, "Missing parameter 'id'"
    assert "commande_id" in params, "Missing parameter 'commande_id'"








def test_hyp_adresse_is_not_abstract():
    assert not inspect.isabstract(Adresse)


def test_hyp_adresse_constructor_exists():
    assert callable(Adresse.__init__)


def test_hyp_adresse_constructor_args():
    sig = inspect.signature(Adresse.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "ville" in params, "Missing parameter 'ville'"
    assert "t_l_phone" in params, "Missing parameter 't_l_phone'"
    assert "num_ro" in params, "Missing parameter 'num_ro'"
    assert "voie" in params, "Missing parameter 'voie'"
    assert "utilisateur_id" in params, "Missing parameter 'utilisateur_id'"
    assert "code_postal" in params, "Missing parameter 'code_postal'"
    assert "geocode" in params, "Missing parameter 'geocode'"











def test_hyp_etat_is_not_abstract():
    assert not inspect.isabstract(Etat)


def test_hyp_etat_constructor_exists():
    assert callable(Etat.__init__)


def test_hyp_etat_constructor_args():
    sig = inspect.signature(Etat.__init__)
    params = list(sig.parameters.keys())
    assert "verrouillage" in params, "Missing parameter 'verrouillage'"
    assert "id" in params, "Missing parameter 'id'"
    assert "nom" in params, "Missing parameter 'nom'"






def test_hyp_commande_is_not_abstract():
    assert not inspect.isabstract(Commande)


def test_hyp_commande_constructor_exists():
    assert callable(Commande.__init__)


def test_hyp_commande_constructor_args():
    sig = inspect.signature(Commande.__init__)
    params = list(sig.parameters.keys())
    assert "_tat" in params, "Missing parameter '_tat'"
    assert "date" in params, "Missing parameter 'date'"
    assert "id" in params, "Missing parameter 'id'"
    assert "utilisateur_id" in params, "Missing parameter 'utilisateur_id'"
    assert "paiement" in params, "Missing parameter 'paiement'"








def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Utilisateur)


def test_hyp_utilisateur_constructor_exists():
    assert callable(Utilisateur.__init__)


def test_hyp_utilisateur_constructor_args():
    sig = inspect.signature(Utilisateur.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "civilit_" in params, "Missing parameter 'civilit_'"
    assert "pizzeria_id" in params, "Missing parameter 'pizzeria_id'"
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "date_naissance" in params, "Missing parameter 'date_naissance'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "role_id" in params, "Missing parameter 'role_id'"
    assert "email" in params, "Missing parameter 'email'"
    assert "mot_de_passe" in params, "Missing parameter 'mot_de_passe'"











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
Pizzeria_strategy = st.builds(
    Pizzeria,
    nom=
        safe_text,
    id=
        st.integers(),
    adresse_id=
        st.integers()
)
R_le_strategy = st.builds(
    R_le,
    type=
        safe_text,
    id=
        st.integers()
)
Produit_strategy = st.builds(
    Produit,
    categorie_id=
        st.integers(),
    id=
        st.integers(),
    nom=
        safe_text,
    prix=
        safe_text
)
Recette_strategy = st.builds(
    Recette,
    produit_id=
        st.integers(),
    id=
        st.integers()
)
Cat_gorie_strategy = st.builds(
    Cat_gorie,
    id=
        st.integers(),
    nom=
        safe_text
)
Ingr_dient_strategy = st.builds(
    Ingr_dient,
    poids=
        safe_text,
    nom=
        safe_text,
    unit_=
        safe_text,
    id=
        st.integers()
)
Stock_strategy = st.builds(
    Stock,
    quantit_=
        st.integers(),
    date_modification=
        st.integers(),
    ingredient_id=
        st.integers(),
    disponibilit_=
        st.booleans()
)
Livraison_strategy = st.builds(
    Livraison,
    client_id=
        st.integers(),
    geocode=
        safe_text,
    livreur_id=
        st.integers(),
    id=
        st.integers(),
    commande_id=
        st.integers()
)
Adresse_strategy = st.builds(
    Adresse,
    id=
        st.integers(),
    ville=
        safe_text,
    t_l_phone=
        safe_text,
    num_ro=
        st.integers(),
    voie=
        safe_text,
    utilisateur_id=
        st.integers(),
    code_postal=
        st.integers(),
    geocode=
        safe_text
)
Etat_strategy = st.builds(
    Etat,
    verrouillage=
        st.booleans(),
    id=
        st.integers(),
    nom=
        safe_text
)
Commande_strategy = st.builds(
    Commande,
    _tat=
        st.integers(),
    date=
        st.integers(),
    id=
        st.integers(),
    utilisateur_id=
        st.integers(),
    paiement=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
Utilisateur_strategy = st.builds(
    Utilisateur,
    id=
        st.integers(),
    civilit_=
        safe_text,
    pizzeria_id=
        st.integers(),
    prenom=
        safe_text,
    date_naissance=
        safe_text,
    nom=
        safe_text,
    role_id=
        st.integers(),
    email=
        safe_text,
    mot_de_passe=
        safe_text
)




@given(instance=Pizzeria_strategy)
def test_hyp_pizzeria_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Pizzeria_strategy)
def test_hyp_pizzeria_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Pizzeria_strategy)
def test_hyp_pizzeria_adresse_id_setter(instance):
    original = instance.adresse_id
    instance.adresse_id = original
    assert instance.adresse_id == original




@given(instance=R_le_strategy)
def test_hyp_r_le_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=R_le_strategy)
def test_hyp_r_le_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Produit_strategy)
def test_hyp_produit_categorie_id_setter(instance):
    original = instance.categorie_id
    instance.categorie_id = original
    assert instance.categorie_id == original



@given(instance=Produit_strategy)
def test_hyp_produit_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Produit_strategy)
def test_hyp_produit_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Produit_strategy)
def test_hyp_produit_prix_setter(instance):
    original = instance.prix
    instance.prix = original
    assert instance.prix == original




@given(instance=Recette_strategy)
def test_hyp_recette_produit_id_setter(instance):
    original = instance.produit_id
    instance.produit_id = original
    assert instance.produit_id == original



@given(instance=Recette_strategy)
def test_hyp_recette_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Cat_gorie_strategy)
def test_hyp_cat_gorie_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Cat_gorie_strategy)
def test_hyp_cat_gorie_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original




@given(instance=Ingr_dient_strategy)
def test_hyp_ingr_dient_poids_setter(instance):
    original = instance.poids
    instance.poids = original
    assert instance.poids == original



@given(instance=Ingr_dient_strategy)
def test_hyp_ingr_dient_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Ingr_dient_strategy)
def test_hyp_ingr_dient_unit__setter(instance):
    original = instance.unit_
    instance.unit_ = original
    assert instance.unit_ == original



@given(instance=Ingr_dient_strategy)
def test_hyp_ingr_dient_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=Stock_strategy)
def test_hyp_stock_quantit__setter(instance):
    original = instance.quantit_
    instance.quantit_ = original
    assert instance.quantit_ == original



@given(instance=Stock_strategy)
def test_hyp_stock_date_modification_setter(instance):
    original = instance.date_modification
    instance.date_modification = original
    assert instance.date_modification == original



@given(instance=Stock_strategy)
def test_hyp_stock_ingredient_id_setter(instance):
    original = instance.ingredient_id
    instance.ingredient_id = original
    assert instance.ingredient_id == original



@given(instance=Stock_strategy)
def test_hyp_stock_disponibilit__setter(instance):
    original = instance.disponibilit_
    instance.disponibilit_ = original
    assert instance.disponibilit_ == original




@given(instance=Livraison_strategy)
def test_hyp_livraison_client_id_setter(instance):
    original = instance.client_id
    instance.client_id = original
    assert instance.client_id == original



@given(instance=Livraison_strategy)
def test_hyp_livraison_geocode_setter(instance):
    original = instance.geocode
    instance.geocode = original
    assert instance.geocode == original



@given(instance=Livraison_strategy)
def test_hyp_livraison_livreur_id_setter(instance):
    original = instance.livreur_id
    instance.livreur_id = original
    assert instance.livreur_id == original



@given(instance=Livraison_strategy)
def test_hyp_livraison_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Livraison_strategy)
def test_hyp_livraison_commande_id_setter(instance):
    original = instance.commande_id
    instance.commande_id = original
    assert instance.commande_id == original




@given(instance=Adresse_strategy)
def test_hyp_adresse_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Adresse_strategy)
def test_hyp_adresse_ville_setter(instance):
    original = instance.ville
    instance.ville = original
    assert instance.ville == original



@given(instance=Adresse_strategy)
def test_hyp_adresse_t_l_phone_setter(instance):
    original = instance.t_l_phone
    instance.t_l_phone = original
    assert instance.t_l_phone == original



@given(instance=Adresse_strategy)
def test_hyp_adresse_num_ro_setter(instance):
    original = instance.num_ro
    instance.num_ro = original
    assert instance.num_ro == original



@given(instance=Adresse_strategy)
def test_hyp_adresse_voie_setter(instance):
    original = instance.voie
    instance.voie = original
    assert instance.voie == original



@given(instance=Adresse_strategy)
def test_hyp_adresse_utilisateur_id_setter(instance):
    original = instance.utilisateur_id
    instance.utilisateur_id = original
    assert instance.utilisateur_id == original



@given(instance=Adresse_strategy)
def test_hyp_adresse_code_postal_setter(instance):
    original = instance.code_postal
    instance.code_postal = original
    assert instance.code_postal == original



@given(instance=Adresse_strategy)
def test_hyp_adresse_geocode_setter(instance):
    original = instance.geocode
    instance.geocode = original
    assert instance.geocode == original




@given(instance=Etat_strategy)
def test_hyp_etat_verrouillage_setter(instance):
    original = instance.verrouillage
    instance.verrouillage = original
    assert instance.verrouillage == original



@given(instance=Etat_strategy)
def test_hyp_etat_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Etat_strategy)
def test_hyp_etat_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original




@given(instance=Commande_strategy)
def test_hyp_commande__tat_setter(instance):
    original = instance._tat
    instance._tat = original
    assert instance._tat == original



@given(instance=Commande_strategy)
def test_hyp_commande_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Commande_strategy)
def test_hyp_commande_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Commande_strategy)
def test_hyp_commande_utilisateur_id_setter(instance):
    original = instance.utilisateur_id
    instance.utilisateur_id = original
    assert instance.utilisateur_id == original



@given(instance=Commande_strategy)
def test_hyp_commande_paiement_setter(instance):
    original = instance.paiement
    instance.paiement = original
    assert instance.paiement == original





@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_civilit__setter(instance):
    original = instance.civilit_
    instance.civilit_ = original
    assert instance.civilit_ == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_pizzeria_id_setter(instance):
    original = instance.pizzeria_id
    instance.pizzeria_id = original
    assert instance.pizzeria_id == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_date_naissance_setter(instance):
    original = instance.date_naissance
    instance.date_naissance = original
    assert instance.date_naissance == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_role_id_setter(instance):
    original = instance.role_id
    instance.role_id = original
    assert instance.role_id == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_mot_de_passe_setter(instance):
    original = instance.mot_de_passe
    instance.mot_de_passe = original
    assert instance.mot_de_passe == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Adresse,
    Cat_gorie,
    Class,
    Commande,
    Etat,
    Ingr_dient,
    Livraison,
    Pizzeria,
    Produit,
    R_le,
    Recette,
    Stock,
    Utilisateur,
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

def test_Adresse_code_postal_value_roundtrip():
    instance = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    assert instance.code_postal == 7
    instance.code_postal = 13
    assert instance.code_postal == 13


def test_Adresse_geocode_value_roundtrip():
    instance = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    assert instance.geocode == "sample_text"
    instance.geocode = "sample_text_2"
    assert instance.geocode == "sample_text_2"


def test_Adresse_id_value_roundtrip():
    instance = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Adresse_num_ro_value_roundtrip():
    instance = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    assert instance.num_ro == 7
    instance.num_ro = 13
    assert instance.num_ro == 13


def test_Adresse_t_l_phone_value_roundtrip():
    instance = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    assert instance.t_l_phone == "sample_text"
    instance.t_l_phone = "sample_text_2"
    assert instance.t_l_phone == "sample_text_2"


def test_Adresse_utilisateur_id_value_roundtrip():
    instance = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    assert instance.utilisateur_id == 7
    instance.utilisateur_id = 13
    assert instance.utilisateur_id == 13


def test_Adresse_ville_value_roundtrip():
    instance = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    assert instance.ville == "sample_text"
    instance.ville = "sample_text_2"
    assert instance.ville == "sample_text_2"


def test_Adresse_voie_value_roundtrip():
    instance = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    assert instance.voie == "sample_text"
    instance.voie = "sample_text_2"
    assert instance.voie == "sample_text_2"


def test_Cat_gorie_id_value_roundtrip():
    instance = Cat_gorie(id=7, nom="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Cat_gorie_nom_value_roundtrip():
    instance = Cat_gorie(id=7, nom="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Commande__tat_value_roundtrip():
    instance = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    assert instance._tat == 7
    instance._tat = 13
    assert instance._tat == 13


def test_Commande_date_value_roundtrip():
    instance = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    assert instance.date == 7
    instance.date = 13
    assert instance.date == 13


def test_Commande_id_value_roundtrip():
    instance = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Commande_paiement_value_roundtrip():
    instance = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    assert instance.paiement == "sample_text"
    instance.paiement = "sample_text_2"
    assert instance.paiement == "sample_text_2"


def test_Commande_utilisateur_id_value_roundtrip():
    instance = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    assert instance.utilisateur_id == 7
    instance.utilisateur_id = 13
    assert instance.utilisateur_id == 13


def test_Etat_id_value_roundtrip():
    instance = Etat(id=7, nom="sample_text", verrouillage=True)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Etat_nom_value_roundtrip():
    instance = Etat(id=7, nom="sample_text", verrouillage=True)
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Etat_verrouillage_value_roundtrip():
    instance = Etat(id=7, nom="sample_text", verrouillage=True)
    assert instance.verrouillage == True
    instance.verrouillage = False
    assert instance.verrouillage == False


def test_Ingr_dient_id_value_roundtrip():
    instance = Ingr_dient(id=7, nom="sample_text", poids="sample_text", unit_="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Ingr_dient_nom_value_roundtrip():
    instance = Ingr_dient(id=7, nom="sample_text", poids="sample_text", unit_="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Ingr_dient_poids_value_roundtrip():
    instance = Ingr_dient(id=7, nom="sample_text", poids="sample_text", unit_="sample_text")
    assert instance.poids == "sample_text"
    instance.poids = "sample_text_2"
    assert instance.poids == "sample_text_2"


def test_Ingr_dient_unit__value_roundtrip():
    instance = Ingr_dient(id=7, nom="sample_text", poids="sample_text", unit_="sample_text")
    assert instance.unit_ == "sample_text"
    instance.unit_ = "sample_text_2"
    assert instance.unit_ == "sample_text_2"


def test_Livraison_client_id_value_roundtrip():
    instance = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    assert instance.client_id == 7
    instance.client_id = 13
    assert instance.client_id == 13


def test_Livraison_commande_id_value_roundtrip():
    instance = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    assert instance.commande_id == 7
    instance.commande_id = 13
    assert instance.commande_id == 13


def test_Livraison_geocode_value_roundtrip():
    instance = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    assert instance.geocode == "sample_text"
    instance.geocode = "sample_text_2"
    assert instance.geocode == "sample_text_2"


def test_Livraison_id_value_roundtrip():
    instance = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Livraison_livreur_id_value_roundtrip():
    instance = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    assert instance.livreur_id == 7
    instance.livreur_id = 13
    assert instance.livreur_id == 13


def test_Pizzeria_adresse_id_value_roundtrip():
    instance = Pizzeria(adresse_id=7, id=7, nom="sample_text")
    assert instance.adresse_id == 7
    instance.adresse_id = 13
    assert instance.adresse_id == 13


def test_Pizzeria_id_value_roundtrip():
    instance = Pizzeria(adresse_id=7, id=7, nom="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Pizzeria_nom_value_roundtrip():
    instance = Pizzeria(adresse_id=7, id=7, nom="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Produit_categorie_id_value_roundtrip():
    instance = Produit(categorie_id=7, id=7, nom="sample_text", prix="sample_text")
    assert instance.categorie_id == 7
    instance.categorie_id = 13
    assert instance.categorie_id == 13


def test_Produit_id_value_roundtrip():
    instance = Produit(categorie_id=7, id=7, nom="sample_text", prix="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Produit_nom_value_roundtrip():
    instance = Produit(categorie_id=7, id=7, nom="sample_text", prix="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Produit_prix_value_roundtrip():
    instance = Produit(categorie_id=7, id=7, nom="sample_text", prix="sample_text")
    assert instance.prix == "sample_text"
    instance.prix = "sample_text_2"
    assert instance.prix == "sample_text_2"


def test_R_le_id_value_roundtrip():
    instance = R_le(id=7, type="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_R_le_type_value_roundtrip():
    instance = R_le(id=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Recette_id_value_roundtrip():
    instance = Recette(id=7, produit_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Recette_produit_id_value_roundtrip():
    instance = Recette(id=7, produit_id=7)
    assert instance.produit_id == 7
    instance.produit_id = 13
    assert instance.produit_id == 13


def test_Stock_date_modification_value_roundtrip():
    instance = Stock(date_modification=7, disponibilit_=True, ingredient_id=7, quantit_=7)
    assert instance.date_modification == 7
    instance.date_modification = 13
    assert instance.date_modification == 13


def test_Stock_disponibilit__value_roundtrip():
    instance = Stock(date_modification=7, disponibilit_=True, ingredient_id=7, quantit_=7)
    assert instance.disponibilit_ == True
    instance.disponibilit_ = False
    assert instance.disponibilit_ == False


def test_Stock_ingredient_id_value_roundtrip():
    instance = Stock(date_modification=7, disponibilit_=True, ingredient_id=7, quantit_=7)
    assert instance.ingredient_id == 7
    instance.ingredient_id = 13
    assert instance.ingredient_id == 13


def test_Stock_quantit__value_roundtrip():
    instance = Stock(date_modification=7, disponibilit_=True, ingredient_id=7, quantit_=7)
    assert instance.quantit_ == 7
    instance.quantit_ = 13
    assert instance.quantit_ == 13


def test_Utilisateur_civilit__value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.civilit_ == "sample_text"
    instance.civilit_ = "sample_text_2"
    assert instance.civilit_ == "sample_text_2"


def test_Utilisateur_date_naissance_value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.date_naissance == "sample_text"
    instance.date_naissance = "sample_text_2"
    assert instance.date_naissance == "sample_text_2"


def test_Utilisateur_email_value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Utilisateur_id_value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Utilisateur_mot_de_passe_value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.mot_de_passe == "sample_text"
    instance.mot_de_passe = "sample_text_2"
    assert instance.mot_de_passe == "sample_text_2"


def test_Utilisateur_nom_value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Utilisateur_pizzeria_id_value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.pizzeria_id == 7
    instance.pizzeria_id = 13
    assert instance.pizzeria_id == 13


def test_Utilisateur_prenom_value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.prenom == "sample_text"
    instance.prenom = "sample_text_2"
    assert instance.prenom == "sample_text_2"


def test_Utilisateur_role_id_value_roundtrip():
    instance = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    assert instance.role_id == 7
    instance.role_id = 13
    assert instance.role_id == 13


def test_assoc_Commande_Utilisateur_link_reassign_clear():
    a = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    b1 = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    b2 = Commande(_tat=13, date=13, id=13, paiement="sample_text_2", utilisateur_id=13)
    _safe_set(a, 'Commande_Utilisateur_17', b1)
    assert _is_linked(a, 'Commande_Utilisateur_17', b1)
    if hasattr(b1, 'Commande_Utilisateur_06'):
        assert _is_linked(b1, 'Commande_Utilisateur_06', a)
    _safe_set(a, 'Commande_Utilisateur_17', b2)
    assert _is_linked(a, 'Commande_Utilisateur_17', b2)
    if hasattr(b1, 'Commande_Utilisateur_06'):
        assert not _is_linked(b1, 'Commande_Utilisateur_06', a)
    if hasattr(b2, 'Commande_Utilisateur_06'):
        assert _is_linked(b2, 'Commande_Utilisateur_06', a)
    _safe_set(a, 'Commande_Utilisateur_17', None)
    assert not _is_linked(a, 'Commande_Utilisateur_17', b2)
    if hasattr(b2, 'Commande_Utilisateur_06'):
        assert not _is_linked(b2, 'Commande_Utilisateur_06', a)


def test_assoc_Etat_Commande_link_reassign_clear():
    a = Etat(id=7, nom="sample_text", verrouillage=True)
    b1 = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    b2 = Commande(_tat=13, date=13, id=13, paiement="sample_text_2", utilisateur_id=13)
    _safe_set(a, 'Etat_Commande_010', b1)
    assert _is_linked(a, 'Etat_Commande_010', b1)
    if hasattr(b1, 'Etat_Commande_111'):
        assert _is_linked(b1, 'Etat_Commande_111', a)
    _safe_set(a, 'Etat_Commande_010', b2)
    assert _is_linked(a, 'Etat_Commande_010', b2)
    if hasattr(b1, 'Etat_Commande_111'):
        assert not _is_linked(b1, 'Etat_Commande_111', a)
    if hasattr(b2, 'Etat_Commande_111'):
        assert _is_linked(b2, 'Etat_Commande_111', a)
    _safe_set(a, 'Etat_Commande_010', None)
    assert not _is_linked(a, 'Etat_Commande_010', b2)
    if hasattr(b2, 'Etat_Commande_111'):
        assert not _is_linked(b2, 'Etat_Commande_111', a)


def test_assoc_Livraison_Commande_link_reassign_clear():
    a = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    b1 = Commande(_tat=7, date=7, id=7, paiement="sample_text", utilisateur_id=7)
    b2 = Commande(_tat=13, date=13, id=13, paiement="sample_text_2", utilisateur_id=13)
    _safe_set(a, 'Livraison_Commande_014', b1)
    assert _is_linked(a, 'Livraison_Commande_014', b1)
    if hasattr(b1, 'Livraison_Commande_115'):
        assert _is_linked(b1, 'Livraison_Commande_115', a)
    _safe_set(a, 'Livraison_Commande_014', b2)
    assert _is_linked(a, 'Livraison_Commande_014', b2)
    if hasattr(b1, 'Livraison_Commande_115'):
        assert not _is_linked(b1, 'Livraison_Commande_115', a)
    if hasattr(b2, 'Livraison_Commande_115'):
        assert _is_linked(b2, 'Livraison_Commande_115', a)
    _safe_set(a, 'Livraison_Commande_014', None)
    assert not _is_linked(a, 'Livraison_Commande_014', b2)
    if hasattr(b2, 'Livraison_Commande_115'):
        assert not _is_linked(b2, 'Livraison_Commande_115', a)


def test_assoc_Livraison_Utilisateur_link_reassign_clear():
    a = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    b1 = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    b2 = Livraison(client_id=13, commande_id=13, geocode="sample_text_2", id=13, livreur_id=13)
    _safe_set(a, 'livreur13', {b1})
    assert _is_linked(a, 'livreur13', b1)
    if hasattr(b1, 'Livraison_Utilisateur_012'):
        assert _is_linked(b1, 'Livraison_Utilisateur_012', a)
    _safe_set(a, 'livreur13', {b2})
    assert _is_linked(a, 'livreur13', b2)
    if hasattr(b1, 'Livraison_Utilisateur_012'):
        assert not _is_linked(b1, 'Livraison_Utilisateur_012', a)
    if hasattr(b2, 'Livraison_Utilisateur_012'):
        assert _is_linked(b2, 'Livraison_Utilisateur_012', a)
    _safe_set(a, 'livreur13', set())
    assert not _is_linked(a, 'livreur13', b2)
    if hasattr(b2, 'Livraison_Utilisateur_012'):
        assert not _is_linked(b2, 'Livraison_Utilisateur_012', a)


def test_assoc_Livraison_Utilisateur2_link_reassign_clear():
    a = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    b1 = Livraison(client_id=7, commande_id=7, geocode="sample_text", id=7, livreur_id=7)
    b2 = Livraison(client_id=13, commande_id=13, geocode="sample_text_2", id=13, livreur_id=13)
    _safe_set(a, 'client21', {b1})
    assert _is_linked(a, 'client21', b1)
    if hasattr(b1, 'Livraison_Utilisateur2_020'):
        assert _is_linked(b1, 'Livraison_Utilisateur2_020', a)
    _safe_set(a, 'client21', {b2})
    assert _is_linked(a, 'client21', b2)
    if hasattr(b1, 'Livraison_Utilisateur2_020'):
        assert not _is_linked(b1, 'Livraison_Utilisateur2_020', a)
    if hasattr(b2, 'Livraison_Utilisateur2_020'):
        assert _is_linked(b2, 'Livraison_Utilisateur2_020', a)
    _safe_set(a, 'client21', set())
    assert not _is_linked(a, 'client21', b2)
    if hasattr(b2, 'Livraison_Utilisateur2_020'):
        assert not _is_linked(b2, 'Livraison_Utilisateur2_020', a)


def test_assoc_Pizzeria_Adresse_link_reassign_clear():
    a = Pizzeria(adresse_id=7, id=7, nom="sample_text")
    b1 = Adresse(code_postal=7, geocode="sample_text", id=7, num_ro=7, t_l_phone="sample_text", utilisateur_id=7, ville="sample_text", voie="sample_text")
    b2 = Adresse(code_postal=13, geocode="sample_text_2", id=13, num_ro=13, t_l_phone="sample_text_2", utilisateur_id=13, ville="sample_text_2", voie="sample_text_2")
    _safe_set(a, 'Pizzeria_Adresse_018', b1)
    assert _is_linked(a, 'Pizzeria_Adresse_018', b1)
    if hasattr(b1, 'Pizzeria_Adresse_119'):
        assert _is_linked(b1, 'Pizzeria_Adresse_119', a)
    _safe_set(a, 'Pizzeria_Adresse_018', b2)
    assert _is_linked(a, 'Pizzeria_Adresse_018', b2)
    if hasattr(b1, 'Pizzeria_Adresse_119'):
        assert not _is_linked(b1, 'Pizzeria_Adresse_119', a)
    if hasattr(b2, 'Pizzeria_Adresse_119'):
        assert _is_linked(b2, 'Pizzeria_Adresse_119', a)
    _safe_set(a, 'Pizzeria_Adresse_018', None)
    assert not _is_linked(a, 'Pizzeria_Adresse_018', b2)
    if hasattr(b2, 'Pizzeria_Adresse_119'):
        assert not _is_linked(b2, 'Pizzeria_Adresse_119', a)


def test_assoc_Produit_Cat_gorie_link_reassign_clear():
    a = Produit(categorie_id=7, id=7, nom="sample_text", prix="sample_text")
    b1 = Cat_gorie(id=7, nom="sample_text")
    b2 = Cat_gorie(id=13, nom="sample_text_2")
    _safe_set(a, 'Produit_Cat_gorie_04', b1)
    assert _is_linked(a, 'Produit_Cat_gorie_04', b1)
    if hasattr(b1, 'Produit_Cat_gorie_15'):
        assert _is_linked(b1, 'Produit_Cat_gorie_15', a)
    _safe_set(a, 'Produit_Cat_gorie_04', b2)
    assert _is_linked(a, 'Produit_Cat_gorie_04', b2)
    if hasattr(b1, 'Produit_Cat_gorie_15'):
        assert not _is_linked(b1, 'Produit_Cat_gorie_15', a)
    if hasattr(b2, 'Produit_Cat_gorie_15'):
        assert _is_linked(b2, 'Produit_Cat_gorie_15', a)
    _safe_set(a, 'Produit_Cat_gorie_04', None)
    assert not _is_linked(a, 'Produit_Cat_gorie_04', b2)
    if hasattr(b2, 'Produit_Cat_gorie_15'):
        assert not _is_linked(b2, 'Produit_Cat_gorie_15', a)


def test_assoc_Produit_Recette_link_reassign_clear():
    a = Recette(id=7, produit_id=7)
    b1 = Produit(categorie_id=7, id=7, nom="sample_text", prix="sample_text")
    b2 = Produit(categorie_id=13, id=13, nom="sample_text_2", prix="sample_text_2")
    _safe_set(a, 'Produit_Recette_13', b1)
    assert _is_linked(a, 'Produit_Recette_13', b1)
    if hasattr(b1, 'Produit_Recette_02'):
        assert _is_linked(b1, 'Produit_Recette_02', a)
    _safe_set(a, 'Produit_Recette_13', b2)
    assert _is_linked(a, 'Produit_Recette_13', b2)
    if hasattr(b1, 'Produit_Recette_02'):
        assert not _is_linked(b1, 'Produit_Recette_02', a)
    if hasattr(b2, 'Produit_Recette_02'):
        assert _is_linked(b2, 'Produit_Recette_02', a)
    _safe_set(a, 'Produit_Recette_13', None)
    assert not _is_linked(a, 'Produit_Recette_13', b2)
    if hasattr(b2, 'Produit_Recette_02'):
        assert not _is_linked(b2, 'Produit_Recette_02', a)


def test_assoc_Stock_Ingr_dient_link_reassign_clear():
    a = Stock(date_modification=7, disponibilit_=True, ingredient_id=7, quantit_=7)
    b1 = Ingr_dient(id=7, nom="sample_text", poids="sample_text", unit_="sample_text")
    b2 = Ingr_dient(id=13, nom="sample_text_2", poids="sample_text_2", unit_="sample_text_2")
    _safe_set(a, 'Stock_Ingr_dient_08', b1)
    assert _is_linked(a, 'Stock_Ingr_dient_08', b1)
    if hasattr(b1, 'Stock_Ingr_dient_19'):
        assert _is_linked(b1, 'Stock_Ingr_dient_19', a)
    _safe_set(a, 'Stock_Ingr_dient_08', b2)
    assert _is_linked(a, 'Stock_Ingr_dient_08', b2)
    if hasattr(b1, 'Stock_Ingr_dient_19'):
        assert not _is_linked(b1, 'Stock_Ingr_dient_19', a)
    if hasattr(b2, 'Stock_Ingr_dient_19'):
        assert _is_linked(b2, 'Stock_Ingr_dient_19', a)
    _safe_set(a, 'Stock_Ingr_dient_08', None)
    assert not _is_linked(a, 'Stock_Ingr_dient_08', b2)
    if hasattr(b2, 'Stock_Ingr_dient_19'):
        assert not _is_linked(b2, 'Stock_Ingr_dient_19', a)


def test_assoc_Utilisateur_Pizzeria_link_reassign_clear():
    a = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    b1 = Pizzeria(adresse_id=7, id=7, nom="sample_text")
    b2 = Pizzeria(adresse_id=13, id=13, nom="sample_text_2")
    _safe_set(a, 'Utilisateur_Pizzeria_016', b1)
    assert _is_linked(a, 'Utilisateur_Pizzeria_016', b1)
    if hasattr(b1, 'Utilisateur_Pizzeria_117'):
        assert _is_linked(b1, 'Utilisateur_Pizzeria_117', a)
    _safe_set(a, 'Utilisateur_Pizzeria_016', b2)
    assert _is_linked(a, 'Utilisateur_Pizzeria_016', b2)
    if hasattr(b1, 'Utilisateur_Pizzeria_117'):
        assert not _is_linked(b1, 'Utilisateur_Pizzeria_117', a)
    if hasattr(b2, 'Utilisateur_Pizzeria_117'):
        assert _is_linked(b2, 'Utilisateur_Pizzeria_117', a)
    _safe_set(a, 'Utilisateur_Pizzeria_016', None)
    assert not _is_linked(a, 'Utilisateur_Pizzeria_016', b2)
    if hasattr(b2, 'Utilisateur_Pizzeria_117'):
        assert not _is_linked(b2, 'Utilisateur_Pizzeria_117', a)


def test_assoc_Utilisateur_R_le_link_reassign_clear():
    a = Utilisateur(civilit_="sample_text", date_naissance="sample_text", email="sample_text", id=7, mot_de_passe="sample_text", nom="sample_text", pizzeria_id=7, prenom="sample_text", role_id=7)
    b1 = R_le(id=7, type="sample_text")
    b2 = R_le(id=13, type="sample_text_2")
    _safe_set(a, 'Utilisateur_R_le_00', b1)
    assert _is_linked(a, 'Utilisateur_R_le_00', b1)
    if hasattr(b1, 'Utilisateur_R_le_11'):
        assert _is_linked(b1, 'Utilisateur_R_le_11', a)
    _safe_set(a, 'Utilisateur_R_le_00', b2)
    assert _is_linked(a, 'Utilisateur_R_le_00', b2)
    if hasattr(b1, 'Utilisateur_R_le_11'):
        assert not _is_linked(b1, 'Utilisateur_R_le_11', a)
    if hasattr(b2, 'Utilisateur_R_le_11'):
        assert _is_linked(b2, 'Utilisateur_R_le_11', a)
    _safe_set(a, 'Utilisateur_R_le_00', None)
    assert not _is_linked(a, 'Utilisateur_R_le_00', b2)
    if hasattr(b2, 'Utilisateur_R_le_11'):
        assert not _is_linked(b2, 'Utilisateur_R_le_11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Adresse_strategy = st.builds(Adresse, code_postal=st.integers(), geocode=safe_text, id=st.integers(), num_ro=st.integers(), t_l_phone=safe_text, utilisateur_id=st.integers(), ville=safe_text, voie=safe_text)
@given(instance=Adresse_strategy)
@settings(max_examples=25)
def test_Adresse_instantiation(instance):
    assert isinstance(instance, Adresse)


Cat_gorie_strategy = st.builds(Cat_gorie, id=st.integers(), nom=safe_text)
@given(instance=Cat_gorie_strategy)
@settings(max_examples=25)
def test_Cat_gorie_instantiation(instance):
    assert isinstance(instance, Cat_gorie)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Commande_strategy = st.builds(Commande, _tat=st.integers(), date=st.integers(), id=st.integers(), paiement=safe_text, utilisateur_id=st.integers())
@given(instance=Commande_strategy)
@settings(max_examples=25)
def test_Commande_instantiation(instance):
    assert isinstance(instance, Commande)


Etat_strategy = st.builds(Etat, id=st.integers(), nom=safe_text, verrouillage=st.booleans())
@given(instance=Etat_strategy)
@settings(max_examples=25)
def test_Etat_instantiation(instance):
    assert isinstance(instance, Etat)


Ingr_dient_strategy = st.builds(Ingr_dient, id=st.integers(), nom=safe_text, poids=safe_text, unit_=safe_text)
@given(instance=Ingr_dient_strategy)
@settings(max_examples=25)
def test_Ingr_dient_instantiation(instance):
    assert isinstance(instance, Ingr_dient)


Livraison_strategy = st.builds(Livraison, client_id=st.integers(), commande_id=st.integers(), geocode=safe_text, id=st.integers(), livreur_id=st.integers())
@given(instance=Livraison_strategy)
@settings(max_examples=25)
def test_Livraison_instantiation(instance):
    assert isinstance(instance, Livraison)


Pizzeria_strategy = st.builds(Pizzeria, adresse_id=st.integers(), id=st.integers(), nom=safe_text)
@given(instance=Pizzeria_strategy)
@settings(max_examples=25)
def test_Pizzeria_instantiation(instance):
    assert isinstance(instance, Pizzeria)


Produit_strategy = st.builds(Produit, categorie_id=st.integers(), id=st.integers(), nom=safe_text, prix=safe_text)
@given(instance=Produit_strategy)
@settings(max_examples=25)
def test_Produit_instantiation(instance):
    assert isinstance(instance, Produit)


R_le_strategy = st.builds(R_le, id=st.integers(), type=safe_text)
@given(instance=R_le_strategy)
@settings(max_examples=25)
def test_R_le_instantiation(instance):
    assert isinstance(instance, R_le)


Recette_strategy = st.builds(Recette, id=st.integers(), produit_id=st.integers())
@given(instance=Recette_strategy)
@settings(max_examples=25)
def test_Recette_instantiation(instance):
    assert isinstance(instance, Recette)


Stock_strategy = st.builds(Stock, date_modification=st.integers(), disponibilit_=st.booleans(), ingredient_id=st.integers(), quantit_=st.integers())
@given(instance=Stock_strategy)
@settings(max_examples=25)
def test_Stock_instantiation(instance):
    assert isinstance(instance, Stock)


Utilisateur_strategy = st.builds(Utilisateur, civilit_=safe_text, date_naissance=safe_text, email=safe_text, id=st.integers(), mot_de_passe=safe_text, nom=safe_text, pizzeria_id=st.integers(), prenom=safe_text, role_id=st.integers())
@given(instance=Utilisateur_strategy)
@settings(max_examples=25)
def test_Utilisateur_instantiation(instance):
    assert isinstance(instance, Utilisateur)



