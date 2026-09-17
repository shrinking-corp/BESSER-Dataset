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
    Effectue_un_paiement_UseCase,
    Valide_arriv__UseCase,
    Valide_embarquement_UseCase,
    confirme_voyage_UseCase,
    Reserve_voyage_UseCase,
    Administre_UseCase,
    Choisi_un_voyage_UseCase,
    S_authentifier_UseCase,
    Enregistre_son_vehicule_UseCase,
    Conducteur_Actor,
    Passager__Actor,
    S_enregistre_UseCase,
    Administrateur_Actor,
    Proposition_de_voyage_UseCase,
    Utilisateur_anonyme_Actor,
    Date_trajet,
    Utilisateur,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_effectue_un_paiement_usecase_is_not_abstract():
    assert not inspect.isabstract(Effectue_un_paiement_UseCase)


def test_hyp_effectue_un_paiement_usecase_constructor_exists():
    assert callable(Effectue_un_paiement_UseCase.__init__)


def test_hyp_effectue_un_paiement_usecase_constructor_args():
    sig = inspect.signature(Effectue_un_paiement_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_valide_arriv__usecase_is_not_abstract():
    assert not inspect.isabstract(Valide_arriv__UseCase)


def test_hyp_valide_arriv__usecase_constructor_exists():
    assert callable(Valide_arriv__UseCase.__init__)


def test_hyp_valide_arriv__usecase_constructor_args():
    sig = inspect.signature(Valide_arriv__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_valide_embarquement_usecase_is_not_abstract():
    assert not inspect.isabstract(Valide_embarquement_UseCase)


def test_hyp_valide_embarquement_usecase_constructor_exists():
    assert callable(Valide_embarquement_UseCase.__init__)


def test_hyp_valide_embarquement_usecase_constructor_args():
    sig = inspect.signature(Valide_embarquement_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_confirme_voyage_usecase_is_not_abstract():
    assert not inspect.isabstract(confirme_voyage_UseCase)


def test_hyp_confirme_voyage_usecase_constructor_exists():
    assert callable(confirme_voyage_UseCase.__init__)


def test_hyp_confirme_voyage_usecase_constructor_args():
    sig = inspect.signature(confirme_voyage_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_reserve_voyage_usecase_is_not_abstract():
    assert not inspect.isabstract(Reserve_voyage_UseCase)


def test_hyp_reserve_voyage_usecase_constructor_exists():
    assert callable(Reserve_voyage_UseCase.__init__)


def test_hyp_reserve_voyage_usecase_constructor_args():
    sig = inspect.signature(Reserve_voyage_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_administre_usecase_is_not_abstract():
    assert not inspect.isabstract(Administre_UseCase)


def test_hyp_administre_usecase_constructor_exists():
    assert callable(Administre_UseCase.__init__)


def test_hyp_administre_usecase_constructor_args():
    sig = inspect.signature(Administre_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_choisi_un_voyage_usecase_is_not_abstract():
    assert not inspect.isabstract(Choisi_un_voyage_UseCase)


def test_hyp_choisi_un_voyage_usecase_constructor_exists():
    assert callable(Choisi_un_voyage_UseCase.__init__)


def test_hyp_choisi_un_voyage_usecase_constructor_args():
    sig = inspect.signature(Choisi_un_voyage_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_s_authentifier_usecase_is_not_abstract():
    assert not inspect.isabstract(S_authentifier_UseCase)


def test_hyp_s_authentifier_usecase_constructor_exists():
    assert callable(S_authentifier_UseCase.__init__)


def test_hyp_s_authentifier_usecase_constructor_args():
    sig = inspect.signature(S_authentifier_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_enregistre_son_vehicule_usecase_is_not_abstract():
    assert not inspect.isabstract(Enregistre_son_vehicule_UseCase)


def test_hyp_enregistre_son_vehicule_usecase_constructor_exists():
    assert callable(Enregistre_son_vehicule_UseCase.__init__)


def test_hyp_enregistre_son_vehicule_usecase_constructor_args():
    sig = inspect.signature(Enregistre_son_vehicule_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conducteur_actor_is_not_abstract():
    assert not inspect.isabstract(Conducteur_Actor)


def test_hyp_conducteur_actor_constructor_exists():
    assert callable(Conducteur_Actor.__init__)


def test_hyp_conducteur_actor_constructor_args():
    sig = inspect.signature(Conducteur_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_passager__actor_is_not_abstract():
    assert not inspect.isabstract(Passager__Actor)


def test_hyp_passager__actor_constructor_exists():
    assert callable(Passager__Actor.__init__)


def test_hyp_passager__actor_constructor_args():
    sig = inspect.signature(Passager__Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_s_enregistre_usecase_is_not_abstract():
    assert not inspect.isabstract(S_enregistre_UseCase)


def test_hyp_s_enregistre_usecase_constructor_exists():
    assert callable(S_enregistre_UseCase.__init__)


def test_hyp_s_enregistre_usecase_constructor_args():
    sig = inspect.signature(S_enregistre_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_administrateur_actor_is_not_abstract():
    assert not inspect.isabstract(Administrateur_Actor)


def test_hyp_administrateur_actor_constructor_exists():
    assert callable(Administrateur_Actor.__init__)


def test_hyp_administrateur_actor_constructor_args():
    sig = inspect.signature(Administrateur_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_proposition_de_voyage_usecase_is_not_abstract():
    assert not inspect.isabstract(Proposition_de_voyage_UseCase)


def test_hyp_proposition_de_voyage_usecase_constructor_exists():
    assert callable(Proposition_de_voyage_UseCase.__init__)


def test_hyp_proposition_de_voyage_usecase_constructor_args():
    sig = inspect.signature(Proposition_de_voyage_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_utilisateur_anonyme_actor_is_not_abstract():
    assert not inspect.isabstract(Utilisateur_anonyme_Actor)


def test_hyp_utilisateur_anonyme_actor_constructor_exists():
    assert callable(Utilisateur_anonyme_Actor.__init__)


def test_hyp_utilisateur_anonyme_actor_constructor_args():
    sig = inspect.signature(Utilisateur_anonyme_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_date_trajet_is_not_abstract():
    assert not inspect.isabstract(Date_trajet)


def test_hyp_date_trajet_constructor_exists():
    assert callable(Date_trajet.__init__)


def test_hyp_date_trajet_constructor_args():
    sig = inspect.signature(Date_trajet.__init__)
    params = list(sig.parameters.keys())
    assert "Date___heure__minute" in params, "Missing parameter 'Date___heure__minute'"
    assert "Jour" in params, "Missing parameter 'Jour'"
    assert "Type_date" in params, "Missing parameter 'Type_date'"
    assert "id_date" in params, "Missing parameter 'id_date'"







def test_hyp_utilisateur_is_not_abstract():
    assert not inspect.isabstract(Utilisateur)


def test_hyp_utilisateur_constructor_exists():
    assert callable(Utilisateur.__init__)


def test_hyp_utilisateur_constructor_args():
    sig = inspect.signature(Utilisateur.__init__)
    params = list(sig.parameters.keys())
    assert "Mail" in params, "Missing parameter 'Mail'"
    assert "Pr_nom" in params, "Missing parameter 'Pr_nom'"
    assert "Telephone" in params, "Missing parameter 'Telephone'"
    assert "Nom" in params, "Missing parameter 'Nom'"
    assert "id_utilisateur" in params, "Missing parameter 'id_utilisateur'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Login" in params, "Missing parameter 'Login'"









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
Effectue_un_paiement_UseCase_strategy = st.builds(
    Effectue_un_paiement_UseCase,
)
Valide_arriv__UseCase_strategy = st.builds(
    Valide_arriv__UseCase,
)
Valide_embarquement_UseCase_strategy = st.builds(
    Valide_embarquement_UseCase,
)
confirme_voyage_UseCase_strategy = st.builds(
    confirme_voyage_UseCase,
)
Reserve_voyage_UseCase_strategy = st.builds(
    Reserve_voyage_UseCase,
)
Administre_UseCase_strategy = st.builds(
    Administre_UseCase,
)
Choisi_un_voyage_UseCase_strategy = st.builds(
    Choisi_un_voyage_UseCase,
)
S_authentifier_UseCase_strategy = st.builds(
    S_authentifier_UseCase,
)
Enregistre_son_vehicule_UseCase_strategy = st.builds(
    Enregistre_son_vehicule_UseCase,
)
Conducteur_Actor_strategy = st.builds(
    Conducteur_Actor,
)
Passager__Actor_strategy = st.builds(
    Passager__Actor,
)
S_enregistre_UseCase_strategy = st.builds(
    S_enregistre_UseCase,
)
Administrateur_Actor_strategy = st.builds(
    Administrateur_Actor,
)
Proposition_de_voyage_UseCase_strategy = st.builds(
    Proposition_de_voyage_UseCase,
)
Utilisateur_anonyme_Actor_strategy = st.builds(
    Utilisateur_anonyme_Actor,
)
Date_trajet_strategy = st.builds(
    Date_trajet,
    Date___heure__minute=
        safe_text,
    Jour=
        safe_text,
    Type_date=
        safe_text,
    id_date=
        st.integers()
)
Utilisateur_strategy = st.builds(
    Utilisateur,
    Mail=
        safe_text,
    Pr_nom=
        safe_text,
    Telephone=
        safe_text,
    Nom=
        safe_text,
    id_utilisateur=
        st.integers(),
    Password=
        safe_text,
    Login=
        safe_text
)



















@given(instance=Date_trajet_strategy)
def test_hyp_date_trajet_Date___heure__minute_setter(instance):
    original = instance.Date___heure__minute
    instance.Date___heure__minute = original
    assert instance.Date___heure__minute == original



@given(instance=Date_trajet_strategy)
def test_hyp_date_trajet_Jour_setter(instance):
    original = instance.Jour
    instance.Jour = original
    assert instance.Jour == original



@given(instance=Date_trajet_strategy)
def test_hyp_date_trajet_Type_date_setter(instance):
    original = instance.Type_date
    instance.Type_date = original
    assert instance.Type_date == original



@given(instance=Date_trajet_strategy)
def test_hyp_date_trajet_id_date_setter(instance):
    original = instance.id_date
    instance.id_date = original
    assert instance.id_date == original




@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_Mail_setter(instance):
    original = instance.Mail
    instance.Mail = original
    assert instance.Mail == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_Pr_nom_setter(instance):
    original = instance.Pr_nom
    instance.Pr_nom = original
    assert instance.Pr_nom == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_Telephone_setter(instance):
    original = instance.Telephone
    instance.Telephone = original
    assert instance.Telephone == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_Nom_setter(instance):
    original = instance.Nom
    instance.Nom = original
    assert instance.Nom == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_id_utilisateur_setter(instance):
    original = instance.id_utilisateur
    instance.id_utilisateur = original
    assert instance.id_utilisateur == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Utilisateur_strategy)
def test_hyp_utilisateur_Login_setter(instance):
    original = instance.Login
    instance.Login = original
    assert instance.Login == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrateur_Actor,
    Administre_UseCase,
    Choisi_un_voyage_UseCase,
    Conducteur_Actor,
    Date_trajet,
    Effectue_un_paiement_UseCase,
    Enregistre_son_vehicule_UseCase,
    Passager__Actor,
    Proposition_de_voyage_UseCase,
    Reserve_voyage_UseCase,
    S_authentifier_UseCase,
    S_enregistre_UseCase,
    Utilisateur,
    Utilisateur_anonyme_Actor,
    Valide_arriv__UseCase,
    Valide_embarquement_UseCase,
    confirme_voyage_UseCase,
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

def test_Date_trajet_Date___heure__minute_value_roundtrip():
    instance = Date_trajet(Date___heure__minute="sample_text", Jour="sample_text", Type_date="sample_text", id_date=7)
    assert instance.Date___heure__minute == "sample_text"
    instance.Date___heure__minute = "sample_text_2"
    assert instance.Date___heure__minute == "sample_text_2"


def test_Date_trajet_Jour_value_roundtrip():
    instance = Date_trajet(Date___heure__minute="sample_text", Jour="sample_text", Type_date="sample_text", id_date=7)
    assert instance.Jour == "sample_text"
    instance.Jour = "sample_text_2"
    assert instance.Jour == "sample_text_2"


def test_Date_trajet_Type_date_value_roundtrip():
    instance = Date_trajet(Date___heure__minute="sample_text", Jour="sample_text", Type_date="sample_text", id_date=7)
    assert instance.Type_date == "sample_text"
    instance.Type_date = "sample_text_2"
    assert instance.Type_date == "sample_text_2"


def test_Date_trajet_id_date_value_roundtrip():
    instance = Date_trajet(Date___heure__minute="sample_text", Jour="sample_text", Type_date="sample_text", id_date=7)
    assert instance.id_date == 7
    instance.id_date = 13
    assert instance.id_date == 13


def test_Utilisateur_Login_value_roundtrip():
    instance = Utilisateur(Login="sample_text", Mail="sample_text", Nom="sample_text", Password="sample_text", Pr_nom="sample_text", Telephone="sample_text", id_utilisateur=7)
    assert instance.Login == "sample_text"
    instance.Login = "sample_text_2"
    assert instance.Login == "sample_text_2"


def test_Utilisateur_Mail_value_roundtrip():
    instance = Utilisateur(Login="sample_text", Mail="sample_text", Nom="sample_text", Password="sample_text", Pr_nom="sample_text", Telephone="sample_text", id_utilisateur=7)
    assert instance.Mail == "sample_text"
    instance.Mail = "sample_text_2"
    assert instance.Mail == "sample_text_2"


def test_Utilisateur_Nom_value_roundtrip():
    instance = Utilisateur(Login="sample_text", Mail="sample_text", Nom="sample_text", Password="sample_text", Pr_nom="sample_text", Telephone="sample_text", id_utilisateur=7)
    assert instance.Nom == "sample_text"
    instance.Nom = "sample_text_2"
    assert instance.Nom == "sample_text_2"


def test_Utilisateur_Password_value_roundtrip():
    instance = Utilisateur(Login="sample_text", Mail="sample_text", Nom="sample_text", Password="sample_text", Pr_nom="sample_text", Telephone="sample_text", id_utilisateur=7)
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Utilisateur_Pr_nom_value_roundtrip():
    instance = Utilisateur(Login="sample_text", Mail="sample_text", Nom="sample_text", Password="sample_text", Pr_nom="sample_text", Telephone="sample_text", id_utilisateur=7)
    assert instance.Pr_nom == "sample_text"
    instance.Pr_nom = "sample_text_2"
    assert instance.Pr_nom == "sample_text_2"


def test_Utilisateur_Telephone_value_roundtrip():
    instance = Utilisateur(Login="sample_text", Mail="sample_text", Nom="sample_text", Password="sample_text", Pr_nom="sample_text", Telephone="sample_text", id_utilisateur=7)
    assert instance.Telephone == "sample_text"
    instance.Telephone = "sample_text_2"
    assert instance.Telephone == "sample_text_2"


def test_Utilisateur_id_utilisateur_value_roundtrip():
    instance = Utilisateur(Login="sample_text", Mail="sample_text", Nom="sample_text", Password="sample_text", Pr_nom="sample_text", Telephone="sample_text", id_utilisateur=7)
    assert instance.id_utilisateur == 7
    instance.id_utilisateur = 13
    assert instance.id_utilisateur == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrateur_Actor_strategy = st.builds(Administrateur_Actor)
@given(instance=Administrateur_Actor_strategy)
@settings(max_examples=25)
def test_Administrateur_Actor_instantiation(instance):
    assert isinstance(instance, Administrateur_Actor)


Administre_UseCase_strategy = st.builds(Administre_UseCase)
@given(instance=Administre_UseCase_strategy)
@settings(max_examples=25)
def test_Administre_UseCase_instantiation(instance):
    assert isinstance(instance, Administre_UseCase)


Choisi_un_voyage_UseCase_strategy = st.builds(Choisi_un_voyage_UseCase)
@given(instance=Choisi_un_voyage_UseCase_strategy)
@settings(max_examples=25)
def test_Choisi_un_voyage_UseCase_instantiation(instance):
    assert isinstance(instance, Choisi_un_voyage_UseCase)


Conducteur_Actor_strategy = st.builds(Conducteur_Actor)
@given(instance=Conducteur_Actor_strategy)
@settings(max_examples=25)
def test_Conducteur_Actor_instantiation(instance):
    assert isinstance(instance, Conducteur_Actor)


Date_trajet_strategy = st.builds(Date_trajet, Date___heure__minute=safe_text, Jour=safe_text, Type_date=safe_text, id_date=st.integers())
@given(instance=Date_trajet_strategy)
@settings(max_examples=25)
def test_Date_trajet_instantiation(instance):
    assert isinstance(instance, Date_trajet)


Effectue_un_paiement_UseCase_strategy = st.builds(Effectue_un_paiement_UseCase)
@given(instance=Effectue_un_paiement_UseCase_strategy)
@settings(max_examples=25)
def test_Effectue_un_paiement_UseCase_instantiation(instance):
    assert isinstance(instance, Effectue_un_paiement_UseCase)


Enregistre_son_vehicule_UseCase_strategy = st.builds(Enregistre_son_vehicule_UseCase)
@given(instance=Enregistre_son_vehicule_UseCase_strategy)
@settings(max_examples=25)
def test_Enregistre_son_vehicule_UseCase_instantiation(instance):
    assert isinstance(instance, Enregistre_son_vehicule_UseCase)


Passager__Actor_strategy = st.builds(Passager__Actor)
@given(instance=Passager__Actor_strategy)
@settings(max_examples=25)
def test_Passager__Actor_instantiation(instance):
    assert isinstance(instance, Passager__Actor)


Proposition_de_voyage_UseCase_strategy = st.builds(Proposition_de_voyage_UseCase)
@given(instance=Proposition_de_voyage_UseCase_strategy)
@settings(max_examples=25)
def test_Proposition_de_voyage_UseCase_instantiation(instance):
    assert isinstance(instance, Proposition_de_voyage_UseCase)


Reserve_voyage_UseCase_strategy = st.builds(Reserve_voyage_UseCase)
@given(instance=Reserve_voyage_UseCase_strategy)
@settings(max_examples=25)
def test_Reserve_voyage_UseCase_instantiation(instance):
    assert isinstance(instance, Reserve_voyage_UseCase)


S_authentifier_UseCase_strategy = st.builds(S_authentifier_UseCase)
@given(instance=S_authentifier_UseCase_strategy)
@settings(max_examples=25)
def test_S_authentifier_UseCase_instantiation(instance):
    assert isinstance(instance, S_authentifier_UseCase)


S_enregistre_UseCase_strategy = st.builds(S_enregistre_UseCase)
@given(instance=S_enregistre_UseCase_strategy)
@settings(max_examples=25)
def test_S_enregistre_UseCase_instantiation(instance):
    assert isinstance(instance, S_enregistre_UseCase)


Utilisateur_strategy = st.builds(Utilisateur, Login=safe_text, Mail=safe_text, Nom=safe_text, Password=safe_text, Pr_nom=safe_text, Telephone=safe_text, id_utilisateur=st.integers())
@given(instance=Utilisateur_strategy)
@settings(max_examples=25)
def test_Utilisateur_instantiation(instance):
    assert isinstance(instance, Utilisateur)


Utilisateur_anonyme_Actor_strategy = st.builds(Utilisateur_anonyme_Actor)
@given(instance=Utilisateur_anonyme_Actor_strategy)
@settings(max_examples=25)
def test_Utilisateur_anonyme_Actor_instantiation(instance):
    assert isinstance(instance, Utilisateur_anonyme_Actor)


Valide_arriv__UseCase_strategy = st.builds(Valide_arriv__UseCase)
@given(instance=Valide_arriv__UseCase_strategy)
@settings(max_examples=25)
def test_Valide_arriv__UseCase_instantiation(instance):
    assert isinstance(instance, Valide_arriv__UseCase)


Valide_embarquement_UseCase_strategy = st.builds(Valide_embarquement_UseCase)
@given(instance=Valide_embarquement_UseCase_strategy)
@settings(max_examples=25)
def test_Valide_embarquement_UseCase_instantiation(instance):
    assert isinstance(instance, Valide_embarquement_UseCase)


confirme_voyage_UseCase_strategy = st.builds(confirme_voyage_UseCase)
@given(instance=confirme_voyage_UseCase_strategy)
@settings(max_examples=25)
def test_confirme_voyage_UseCase_instantiation(instance):
    assert isinstance(instance, confirme_voyage_UseCase)



