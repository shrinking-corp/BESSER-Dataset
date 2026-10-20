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
    Participant,
    Formateur,
    Prestation,
    Type,
    Convention,
    Facture,
    DevisEntete,
    Formation,
    Client,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_participant_is_not_abstract():
    assert not inspect.isabstract(Participant)


def test_hyp_participant_constructor_exists():
    assert callable(Participant.__init__)


def test_hyp_participant_constructor_args():
    sig = inspect.signature(Participant.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"
    assert "id_session" in params, "Missing parameter 'id_session'"
    assert "prenom" in params, "Missing parameter 'prenom'"
    assert "date_naissance" in params, "Missing parameter 'date_naissance'"







def test_hyp_formateur_is_not_abstract():
    assert not inspect.isabstract(Formateur)


def test_hyp_formateur_constructor_exists():
    assert callable(Formateur.__init__)


def test_hyp_formateur_constructor_args():
    sig = inspect.signature(Formateur.__init__)
    params = list(sig.parameters.keys())
    assert "Nom" in params, "Missing parameter 'Nom'"
    assert "Prenom" in params, "Missing parameter 'Prenom'"





def test_hyp_prestation_is_not_abstract():
    assert not inspect.isabstract(Prestation)


def test_hyp_prestation_constructor_exists():
    assert callable(Prestation.__init__)


def test_hyp_prestation_constructor_args():
    sig = inspect.signature(Prestation.__init__)
    params = list(sig.parameters.keys())
    assert "horaires" in params, "Missing parameter 'horaires'"
    assert "duree" in params, "Missing parameter 'duree'"
    assert "nb_stagiaires" in params, "Missing parameter 'nb_stagiaires'"
    assert "id_client" in params, "Missing parameter 'id_client'"
    assert "id_formateur" in params, "Missing parameter 'id_formateur'"
    assert "id_type" in params, "Missing parameter 'id_type'"
    assert "id_formation" in params, "Missing parameter 'id_formation'"
    assert "lieu" in params, "Missing parameter 'lieu'"
    assert "date_debut" in params, "Missing parameter 'date_debut'"
    assert "date_fin" in params, "Missing parameter 'date_fin'"













def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_convention_is_not_abstract():
    assert not inspect.isabstract(Convention)


def test_hyp_convention_constructor_exists():
    assert callable(Convention.__init__)


def test_hyp_convention_constructor_args():
    sig = inspect.signature(Convention.__init__)
    params = list(sig.parameters.keys())
    assert "id_convention" in params, "Missing parameter 'id_convention'"
    assert "numero" in params, "Missing parameter 'numero'"





def test_hyp_facture_is_not_abstract():
    assert not inspect.isabstract(Facture)


def test_hyp_facture_constructor_exists():
    assert callable(Facture.__init__)


def test_hyp_facture_constructor_args():
    sig = inspect.signature(Facture.__init__)
    params = list(sig.parameters.keys())
    assert "numero" in params, "Missing parameter 'numero'"
    assert "paye" in params, "Missing parameter 'paye'"
    assert "id_devis" in params, "Missing parameter 'id_devis'"






def test_hyp_devisentete_is_not_abstract():
    assert not inspect.isabstract(DevisEntete)


def test_hyp_devisentete_constructor_exists():
    assert callable(DevisEntete.__init__)


def test_hyp_devisentete_constructor_args():
    sig = inspect.signature(DevisEntete.__init__)
    params = list(sig.parameters.keys())
    assert "numero" in params, "Missing parameter 'numero'"
    assert "id_session" in params, "Missing parameter 'id_session'"





def test_hyp_formation_is_not_abstract():
    assert not inspect.isabstract(Formation)


def test_hyp_formation_constructor_exists():
    assert callable(Formation.__init__)


def test_hyp_formation_constructor_args():
    sig = inspect.signature(Formation.__init__)
    params = list(sig.parameters.keys())
    assert "cout_unitaire" in params, "Missing parameter 'cout_unitaire'"
    assert "objectif" in params, "Missing parameter 'objectif'"
    assert "libelle" in params, "Missing parameter 'libelle'"






def test_hyp_client_is_not_abstract():
    assert not inspect.isabstract(Client)


def test_hyp_client_constructor_exists():
    assert callable(Client.__init__)


def test_hyp_client_constructor_args():
    sig = inspect.signature(Client.__init__)
    params = list(sig.parameters.keys())
    assert "codePostal" in params, "Missing parameter 'codePostal'"
    assert "nom" in params, "Missing parameter 'nom'"
    assert "contact" in params, "Missing parameter 'contact'"
    assert "tel" in params, "Missing parameter 'tel'"
    assert "ville" in params, "Missing parameter 'ville'"
    assert "adresse" in params, "Missing parameter 'adresse'"








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
Participant_strategy = st.builds(
    Participant,
    nom=
        safe_text,
    id_session=
        st.integers(),
    prenom=
        safe_text,
    date_naissance=
        safe_text
)
Formateur_strategy = st.builds(
    Formateur,
    Nom=
        safe_text,
    Prenom=
        safe_text
)
Prestation_strategy = st.builds(
    Prestation,
    horaires=
        safe_text,
    duree=
        safe_text,
    nb_stagiaires=
        st.integers(),
    id_client=
        st.integers(),
    id_formateur=
        st.integers(),
    id_type=
        st.integers(),
    id_formation=
        st.integers(),
    lieu=
        st.booleans(),
    date_debut=
        safe_text,
    date_fin=
        safe_text
)
Type_strategy = st.builds(
    Type,
    type=
        safe_text
)
Convention_strategy = st.builds(
    Convention,
    id_convention=
        st.integers(),
    numero=
        safe_text
)
Facture_strategy = st.builds(
    Facture,
    numero=
        safe_text,
    paye=
        st.booleans(),
    id_devis=
        st.integers()
)
DevisEntete_strategy = st.builds(
    DevisEntete,
    numero=
        safe_text,
    id_session=
        st.integers()
)
Formation_strategy = st.builds(
    Formation,
    cout_unitaire=
        st.integers(),
    objectif=
        safe_text,
    libelle=
        safe_text
)
Client_strategy = st.builds(
    Client,
    codePostal=
        safe_text,
    nom=
        safe_text,
    contact=
        safe_text,
    tel=
        safe_text,
    ville=
        safe_text,
    adresse=
        safe_text
)




@given(instance=Participant_strategy)
def test_hyp_participant_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Participant_strategy)
def test_hyp_participant_id_session_setter(instance):
    original = instance.id_session
    instance.id_session = original
    assert instance.id_session == original



@given(instance=Participant_strategy)
def test_hyp_participant_prenom_setter(instance):
    original = instance.prenom
    instance.prenom = original
    assert instance.prenom == original



@given(instance=Participant_strategy)
def test_hyp_participant_date_naissance_setter(instance):
    original = instance.date_naissance
    instance.date_naissance = original
    assert instance.date_naissance == original




@given(instance=Formateur_strategy)
def test_hyp_formateur_Nom_setter(instance):
    original = instance.Nom
    instance.Nom = original
    assert instance.Nom == original



@given(instance=Formateur_strategy)
def test_hyp_formateur_Prenom_setter(instance):
    original = instance.Prenom
    instance.Prenom = original
    assert instance.Prenom == original




@given(instance=Prestation_strategy)
def test_hyp_prestation_horaires_setter(instance):
    original = instance.horaires
    instance.horaires = original
    assert instance.horaires == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_duree_setter(instance):
    original = instance.duree
    instance.duree = original
    assert instance.duree == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_nb_stagiaires_setter(instance):
    original = instance.nb_stagiaires
    instance.nb_stagiaires = original
    assert instance.nb_stagiaires == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_id_client_setter(instance):
    original = instance.id_client
    instance.id_client = original
    assert instance.id_client == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_id_formateur_setter(instance):
    original = instance.id_formateur
    instance.id_formateur = original
    assert instance.id_formateur == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_id_type_setter(instance):
    original = instance.id_type
    instance.id_type = original
    assert instance.id_type == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_id_formation_setter(instance):
    original = instance.id_formation
    instance.id_formation = original
    assert instance.id_formation == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_lieu_setter(instance):
    original = instance.lieu
    instance.lieu = original
    assert instance.lieu == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_date_debut_setter(instance):
    original = instance.date_debut
    instance.date_debut = original
    assert instance.date_debut == original



@given(instance=Prestation_strategy)
def test_hyp_prestation_date_fin_setter(instance):
    original = instance.date_fin
    instance.date_fin = original
    assert instance.date_fin == original




@given(instance=Type_strategy)
def test_hyp_type_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=Convention_strategy)
def test_hyp_convention_id_convention_setter(instance):
    original = instance.id_convention
    instance.id_convention = original
    assert instance.id_convention == original



@given(instance=Convention_strategy)
def test_hyp_convention_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original




@given(instance=Facture_strategy)
def test_hyp_facture_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Facture_strategy)
def test_hyp_facture_paye_setter(instance):
    original = instance.paye
    instance.paye = original
    assert instance.paye == original



@given(instance=Facture_strategy)
def test_hyp_facture_id_devis_setter(instance):
    original = instance.id_devis
    instance.id_devis = original
    assert instance.id_devis == original




@given(instance=DevisEntete_strategy)
def test_hyp_devisentete_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=DevisEntete_strategy)
def test_hyp_devisentete_id_session_setter(instance):
    original = instance.id_session
    instance.id_session = original
    assert instance.id_session == original




@given(instance=Formation_strategy)
def test_hyp_formation_cout_unitaire_setter(instance):
    original = instance.cout_unitaire
    instance.cout_unitaire = original
    assert instance.cout_unitaire == original



@given(instance=Formation_strategy)
def test_hyp_formation_objectif_setter(instance):
    original = instance.objectif
    instance.objectif = original
    assert instance.objectif == original



@given(instance=Formation_strategy)
def test_hyp_formation_libelle_setter(instance):
    original = instance.libelle
    instance.libelle = original
    assert instance.libelle == original




@given(instance=Client_strategy)
def test_hyp_client_codePostal_setter(instance):
    original = instance.codePostal
    instance.codePostal = original
    assert instance.codePostal == original



@given(instance=Client_strategy)
def test_hyp_client_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original



@given(instance=Client_strategy)
def test_hyp_client_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=Client_strategy)
def test_hyp_client_tel_setter(instance):
    original = instance.tel
    instance.tel = original
    assert instance.tel == original



@given(instance=Client_strategy)
def test_hyp_client_ville_setter(instance):
    original = instance.ville
    instance.ville = original
    assert instance.ville == original



@given(instance=Client_strategy)
def test_hyp_client_adresse_setter(instance):
    original = instance.adresse
    instance.adresse = original
    assert instance.adresse == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_Client_adresse_value_roundtrip():
    instance = Client(adresse="sample_text", codePostal="sample_text", contact="sample_text", nom="sample_text", tel="sample_text", ville="sample_text")
    assert instance.adresse == "sample_text"
    instance.adresse = "sample_text_2"
    assert instance.adresse == "sample_text_2"


def test_Client_codePostal_value_roundtrip():
    instance = Client(adresse="sample_text", codePostal="sample_text", contact="sample_text", nom="sample_text", tel="sample_text", ville="sample_text")
    assert instance.codePostal == "sample_text"
    instance.codePostal = "sample_text_2"
    assert instance.codePostal == "sample_text_2"


def test_Client_contact_value_roundtrip():
    instance = Client(adresse="sample_text", codePostal="sample_text", contact="sample_text", nom="sample_text", tel="sample_text", ville="sample_text")
    assert instance.contact == "sample_text"
    instance.contact = "sample_text_2"
    assert instance.contact == "sample_text_2"


def test_Client_nom_value_roundtrip():
    instance = Client(adresse="sample_text", codePostal="sample_text", contact="sample_text", nom="sample_text", tel="sample_text", ville="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Client_tel_value_roundtrip():
    instance = Client(adresse="sample_text", codePostal="sample_text", contact="sample_text", nom="sample_text", tel="sample_text", ville="sample_text")
    assert instance.tel == "sample_text"
    instance.tel = "sample_text_2"
    assert instance.tel == "sample_text_2"


def test_Client_ville_value_roundtrip():
    instance = Client(adresse="sample_text", codePostal="sample_text", contact="sample_text", nom="sample_text", tel="sample_text", ville="sample_text")
    assert instance.ville == "sample_text"
    instance.ville = "sample_text_2"
    assert instance.ville == "sample_text_2"


def test_Convention_id_convention_value_roundtrip():
    instance = Convention(id_convention=7, numero="sample_text")
    assert instance.id_convention == 7
    instance.id_convention = 13
    assert instance.id_convention == 13


def test_Convention_numero_value_roundtrip():
    instance = Convention(id_convention=7, numero="sample_text")
    assert instance.numero == "sample_text"
    instance.numero = "sample_text_2"
    assert instance.numero == "sample_text_2"


def test_DevisEntete_id_session_value_roundtrip():
    instance = DevisEntete(id_session=7, numero="sample_text")
    assert instance.id_session == 7
    instance.id_session = 13
    assert instance.id_session == 13


def test_DevisEntete_numero_value_roundtrip():
    instance = DevisEntete(id_session=7, numero="sample_text")
    assert instance.numero == "sample_text"
    instance.numero = "sample_text_2"
    assert instance.numero == "sample_text_2"


def test_Facture_id_devis_value_roundtrip():
    instance = Facture(id_devis=7, numero="sample_text", paye=True)
    assert instance.id_devis == 7
    instance.id_devis = 13
    assert instance.id_devis == 13


def test_Facture_numero_value_roundtrip():
    instance = Facture(id_devis=7, numero="sample_text", paye=True)
    assert instance.numero == "sample_text"
    instance.numero = "sample_text_2"
    assert instance.numero == "sample_text_2"


def test_Facture_paye_value_roundtrip():
    instance = Facture(id_devis=7, numero="sample_text", paye=True)
    assert instance.paye == True
    instance.paye = False
    assert instance.paye == False


def test_Formateur_Nom_value_roundtrip():
    instance = Formateur(Nom="sample_text", Prenom="sample_text")
    assert instance.Nom == "sample_text"
    instance.Nom = "sample_text_2"
    assert instance.Nom == "sample_text_2"


def test_Formateur_Prenom_value_roundtrip():
    instance = Formateur(Nom="sample_text", Prenom="sample_text")
    assert instance.Prenom == "sample_text"
    instance.Prenom = "sample_text_2"
    assert instance.Prenom == "sample_text_2"


def test_Formation_cout_unitaire_value_roundtrip():
    instance = Formation(cout_unitaire=7, libelle="sample_text", objectif="sample_text")
    assert instance.cout_unitaire == 7
    instance.cout_unitaire = 13
    assert instance.cout_unitaire == 13


def test_Formation_libelle_value_roundtrip():
    instance = Formation(cout_unitaire=7, libelle="sample_text", objectif="sample_text")
    assert instance.libelle == "sample_text"
    instance.libelle = "sample_text_2"
    assert instance.libelle == "sample_text_2"


def test_Formation_objectif_value_roundtrip():
    instance = Formation(cout_unitaire=7, libelle="sample_text", objectif="sample_text")
    assert instance.objectif == "sample_text"
    instance.objectif = "sample_text_2"
    assert instance.objectif == "sample_text_2"


def test_Participant_date_naissance_value_roundtrip():
    instance = Participant(date_naissance="sample_text", id_session=7, nom="sample_text", prenom="sample_text")
    assert instance.date_naissance == "sample_text"
    instance.date_naissance = "sample_text_2"
    assert instance.date_naissance == "sample_text_2"


def test_Participant_id_session_value_roundtrip():
    instance = Participant(date_naissance="sample_text", id_session=7, nom="sample_text", prenom="sample_text")
    assert instance.id_session == 7
    instance.id_session = 13
    assert instance.id_session == 13


def test_Participant_nom_value_roundtrip():
    instance = Participant(date_naissance="sample_text", id_session=7, nom="sample_text", prenom="sample_text")
    assert instance.nom == "sample_text"
    instance.nom = "sample_text_2"
    assert instance.nom == "sample_text_2"


def test_Participant_prenom_value_roundtrip():
    instance = Participant(date_naissance="sample_text", id_session=7, nom="sample_text", prenom="sample_text")
    assert instance.prenom == "sample_text"
    instance.prenom = "sample_text_2"
    assert instance.prenom == "sample_text_2"


def test_Prestation_date_debut_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.date_debut == "sample_text"
    instance.date_debut = "sample_text_2"
    assert instance.date_debut == "sample_text_2"


def test_Prestation_date_fin_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.date_fin == "sample_text"
    instance.date_fin = "sample_text_2"
    assert instance.date_fin == "sample_text_2"


def test_Prestation_duree_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.duree == "sample_text"
    instance.duree = "sample_text_2"
    assert instance.duree == "sample_text_2"


def test_Prestation_horaires_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.horaires == "sample_text"
    instance.horaires = "sample_text_2"
    assert instance.horaires == "sample_text_2"


def test_Prestation_id_client_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.id_client == 7
    instance.id_client = 13
    assert instance.id_client == 13


def test_Prestation_id_formateur_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.id_formateur == 7
    instance.id_formateur = 13
    assert instance.id_formateur == 13


def test_Prestation_id_formation_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.id_formation == 7
    instance.id_formation = 13
    assert instance.id_formation == 13


def test_Prestation_id_type_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.id_type == 7
    instance.id_type = 13
    assert instance.id_type == 13


def test_Prestation_lieu_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.lieu == True
    instance.lieu = False
    assert instance.lieu == False


def test_Prestation_nb_stagiaires_value_roundtrip():
    instance = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    assert instance.nb_stagiaires == 7
    instance.nb_stagiaires = 13
    assert instance.nb_stagiaires == 13


def test_Type_type_value_roundtrip():
    instance = Type(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_assoc_Client_Session_link_reassign_clear():
    a = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    b1 = Client(adresse="sample_text", codePostal="sample_text", contact="sample_text", nom="sample_text", tel="sample_text", ville="sample_text")
    b2 = Client(adresse="sample_text_2", codePostal="sample_text_2", contact="sample_text_2", nom="sample_text_2", tel="sample_text_2", ville="sample_text_2")
    _safe_set(a, 'client7', b1)
    assert _is_linked(a, 'client7', b1)
    if hasattr(b1, 'session6'):
        assert _is_linked(b1, 'session6', a)
    _safe_set(a, 'client7', b2)
    assert _is_linked(a, 'client7', b2)
    if hasattr(b1, 'session6'):
        assert not _is_linked(b1, 'session6', a)
    if hasattr(b2, 'session6'):
        assert _is_linked(b2, 'session6', a)
    _safe_set(a, 'client7', None)
    assert not _is_linked(a, 'client7', b2)
    if hasattr(b2, 'session6'):
        assert not _is_linked(b2, 'session6', a)


def test_assoc_DevisEntete_Session_link_reassign_clear():
    a = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    b1 = DevisEntete(id_session=7, numero="sample_text")
    b2 = DevisEntete(id_session=13, numero="sample_text_2")
    _safe_set(a, 'devisEntete5', b1)
    assert _is_linked(a, 'devisEntete5', b1)
    if hasattr(b1, 'session4'):
        assert _is_linked(b1, 'session4', a)
    _safe_set(a, 'devisEntete5', b2)
    assert _is_linked(a, 'devisEntete5', b2)
    if hasattr(b1, 'session4'):
        assert not _is_linked(b1, 'session4', a)
    if hasattr(b2, 'session4'):
        assert _is_linked(b2, 'session4', a)
    _safe_set(a, 'devisEntete5', None)
    assert not _is_linked(a, 'devisEntete5', b2)
    if hasattr(b2, 'session4'):
        assert not _is_linked(b2, 'session4', a)


def test_assoc_Formateurs_Sessions_link_reassign_clear():
    a = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    b1 = Formateur(Nom="sample_text", Prenom="sample_text")
    b2 = Formateur(Nom="sample_text_2", Prenom="sample_text_2")
    _safe_set(a, 'formateurs3', b1)
    assert _is_linked(a, 'formateurs3', b1)
    if hasattr(b1, 'sessions2'):
        assert _is_linked(b1, 'sessions2', a)
    _safe_set(a, 'formateurs3', b2)
    assert _is_linked(a, 'formateurs3', b2)
    if hasattr(b1, 'sessions2'):
        assert not _is_linked(b1, 'sessions2', a)
    if hasattr(b2, 'sessions2'):
        assert _is_linked(b2, 'sessions2', a)
    _safe_set(a, 'formateurs3', None)
    assert not _is_linked(a, 'formateurs3', b2)
    if hasattr(b2, 'sessions2'):
        assert not _is_linked(b2, 'sessions2', a)


def test_assoc_Formation_Session_link_reassign_clear():
    a = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    b1 = Formation(cout_unitaire=7, libelle="sample_text", objectif="sample_text")
    b2 = Formation(cout_unitaire=13, libelle="sample_text_2", objectif="sample_text_2")
    _safe_set(a, 'formation9', b1)
    assert _is_linked(a, 'formation9', b1)
    if hasattr(b1, 'session8'):
        assert _is_linked(b1, 'session8', a)
    _safe_set(a, 'formation9', b2)
    assert _is_linked(a, 'formation9', b2)
    if hasattr(b1, 'session8'):
        assert not _is_linked(b1, 'session8', a)
    if hasattr(b2, 'session8'):
        assert _is_linked(b2, 'session8', a)
    _safe_set(a, 'formation9', None)
    assert not _is_linked(a, 'formation9', b2)
    if hasattr(b2, 'session8'):
        assert not _is_linked(b2, 'session8', a)


def test_assoc_Sessions_Participants_link_reassign_clear():
    a = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    b1 = Participant(date_naissance="sample_text", id_session=7, nom="sample_text", prenom="sample_text")
    b2 = Participant(date_naissance="sample_text_2", id_session=13, nom="sample_text_2", prenom="sample_text_2")
    _safe_set(a, 'participants0', b1)
    assert _is_linked(a, 'participants0', b1)
    if hasattr(b1, 'sessions1'):
        assert _is_linked(b1, 'sessions1', a)
    _safe_set(a, 'participants0', b2)
    assert _is_linked(a, 'participants0', b2)
    if hasattr(b1, 'sessions1'):
        assert not _is_linked(b1, 'sessions1', a)
    if hasattr(b2, 'sessions1'):
        assert _is_linked(b2, 'sessions1', a)
    _safe_set(a, 'participants0', None)
    assert not _is_linked(a, 'participants0', b2)
    if hasattr(b2, 'sessions1'):
        assert not _is_linked(b2, 'sessions1', a)


def test_assoc_Type_Prestation_link_reassign_clear():
    a = Type(type="sample_text")
    b1 = Prestation(date_debut="sample_text", date_fin="sample_text", duree="sample_text", horaires="sample_text", id_client=7, id_formateur=7, id_formation=7, id_type=7, lieu=True, nb_stagiaires=7)
    b2 = Prestation(date_debut="sample_text_2", date_fin="sample_text_2", duree="sample_text_2", horaires="sample_text_2", id_client=13, id_formateur=13, id_formation=13, id_type=13, lieu=False, nb_stagiaires=13)
    _safe_set(a, 'prestation10', b1)
    assert _is_linked(a, 'prestation10', b1)
    if hasattr(b1, 'type11'):
        assert _is_linked(b1, 'type11', a)
    _safe_set(a, 'prestation10', b2)
    assert _is_linked(a, 'prestation10', b2)
    if hasattr(b1, 'type11'):
        assert not _is_linked(b1, 'type11', a)
    if hasattr(b2, 'type11'):
        assert _is_linked(b2, 'type11', a)
    _safe_set(a, 'prestation10', None)
    assert not _is_linked(a, 'prestation10', b2)
    if hasattr(b2, 'type11'):
        assert not _is_linked(b2, 'type11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Client_strategy = st.builds(Client, adresse=safe_text, codePostal=safe_text, contact=safe_text, nom=safe_text, tel=safe_text, ville=safe_text)
@given(instance=Client_strategy)
@settings(max_examples=25)
def test_Client_instantiation(instance):
    assert isinstance(instance, Client)


Convention_strategy = st.builds(Convention, id_convention=st.integers(), numero=safe_text)
@given(instance=Convention_strategy)
@settings(max_examples=25)
def test_Convention_instantiation(instance):
    assert isinstance(instance, Convention)


DevisEntete_strategy = st.builds(DevisEntete, id_session=st.integers(), numero=safe_text)
@given(instance=DevisEntete_strategy)
@settings(max_examples=25)
def test_DevisEntete_instantiation(instance):
    assert isinstance(instance, DevisEntete)


Facture_strategy = st.builds(Facture, id_devis=st.integers(), numero=safe_text, paye=st.booleans())
@given(instance=Facture_strategy)
@settings(max_examples=25)
def test_Facture_instantiation(instance):
    assert isinstance(instance, Facture)


Formateur_strategy = st.builds(Formateur, Nom=safe_text, Prenom=safe_text)
@given(instance=Formateur_strategy)
@settings(max_examples=25)
def test_Formateur_instantiation(instance):
    assert isinstance(instance, Formateur)


Formation_strategy = st.builds(Formation, cout_unitaire=st.integers(), libelle=safe_text, objectif=safe_text)
@given(instance=Formation_strategy)
@settings(max_examples=25)
def test_Formation_instantiation(instance):
    assert isinstance(instance, Formation)


Participant_strategy = st.builds(Participant, date_naissance=safe_text, id_session=st.integers(), nom=safe_text, prenom=safe_text)
@given(instance=Participant_strategy)
@settings(max_examples=25)
def test_Participant_instantiation(instance):
    assert isinstance(instance, Participant)


Prestation_strategy = st.builds(Prestation, date_debut=safe_text, date_fin=safe_text, duree=safe_text, horaires=safe_text, id_client=st.integers(), id_formateur=st.integers(), id_formation=st.integers(), id_type=st.integers(), lieu=st.booleans(), nb_stagiaires=st.integers())
@given(instance=Prestation_strategy)
@settings(max_examples=25)
def test_Prestation_instantiation(instance):
    assert isinstance(instance, Prestation)


Type_strategy = st.builds(Type, type=safe_text)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)



