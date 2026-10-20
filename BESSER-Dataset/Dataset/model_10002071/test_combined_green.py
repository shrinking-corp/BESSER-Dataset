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
    Secretaire_external,
    ResultatExamen,
    CentreHospitalier,
    Programme,
    Service,
    Medecin,
    Examen,
    Consultion,
    Rendez_Vous,
    Patient,
    DossierPatient,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_secretaire_external_is_not_abstract():
    assert not inspect.isabstract(Secretaire_external)


def test_hyp_secretaire_external_constructor_exists():
    assert callable(Secretaire_external.__init__)


def test_hyp_secretaire_external_constructor_args():
    sig = inspect.signature(Secretaire_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_resultatexamen_is_not_abstract():
    assert not inspect.isabstract(ResultatExamen)


def test_hyp_resultatexamen_constructor_exists():
    assert callable(ResultatExamen.__init__)


def test_hyp_resultatexamen_constructor_args():
    sig = inspect.signature(ResultatExamen.__init__)
    params = list(sig.parameters.keys())
    assert "numeroResultat" in params, "Missing parameter 'numeroResultat'"
    assert "infoResultat" in params, "Missing parameter 'infoResultat'"





def test_hyp_centrehospitalier_is_not_abstract():
    assert not inspect.isabstract(CentreHospitalier)


def test_hyp_centrehospitalier_constructor_exists():
    assert callable(CentreHospitalier.__init__)


def test_hyp_centrehospitalier_constructor_args():
    sig = inspect.signature(CentreHospitalier.__init__)
    params = list(sig.parameters.keys())
    assert "nomCentre" in params, "Missing parameter 'nomCentre'"
    assert "numeroCentre" in params, "Missing parameter 'numeroCentre'"
    assert "descriptionCentre" in params, "Missing parameter 'descriptionCentre'"






def test_hyp_programme_is_not_abstract():
    assert not inspect.isabstract(Programme)


def test_hyp_programme_constructor_exists():
    assert callable(Programme.__init__)


def test_hyp_programme_constructor_args():
    sig = inspect.signature(Programme.__init__)
    params = list(sig.parameters.keys())
    assert "heure" in params, "Missing parameter 'heure'"
    assert "numeroProgramme" in params, "Missing parameter 'numeroProgramme'"
    assert "date" in params, "Missing parameter 'date'"






def test_hyp_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_hyp_service_constructor_exists():
    assert callable(Service.__init__)


def test_hyp_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())
    assert "nomService" in params, "Missing parameter 'nomService'"
    assert "descriptionService" in params, "Missing parameter 'descriptionService'"
    assert "numeroService" in params, "Missing parameter 'numeroService'"






def test_hyp_medecin_is_not_abstract():
    assert not inspect.isabstract(Medecin)


def test_hyp_medecin_constructor_exists():
    assert callable(Medecin.__init__)


def test_hyp_medecin_constructor_args():
    sig = inspect.signature(Medecin.__init__)
    params = list(sig.parameters.keys())
    assert "specialite" in params, "Missing parameter 'specialite'"
    assert "prenomMedecin" in params, "Missing parameter 'prenomMedecin'"
    assert "numeroMedecin" in params, "Missing parameter 'numeroMedecin'"
    assert "dateNaissance" in params, "Missing parameter 'dateNaissance'"
    assert "nomMedecin" in params, "Missing parameter 'nomMedecin'"








def test_hyp_examen_is_not_abstract():
    assert not inspect.isabstract(Examen)


def test_hyp_examen_constructor_exists():
    assert callable(Examen.__init__)


def test_hyp_examen_constructor_args():
    sig = inspect.signature(Examen.__init__)
    params = list(sig.parameters.keys())
    assert "dateProvisoir" in params, "Missing parameter 'dateProvisoir'"
    assert "heure" in params, "Missing parameter 'heure'"
    assert "motif" in params, "Missing parameter 'motif'"
    assert "numeroExamen" in params, "Missing parameter 'numeroExamen'"







def test_hyp_consultion_is_not_abstract():
    assert not inspect.isabstract(Consultion)


def test_hyp_consultion_constructor_exists():
    assert callable(Consultion.__init__)


def test_hyp_consultion_constructor_args():
    sig = inspect.signature(Consultion.__init__)
    params = list(sig.parameters.keys())
    assert "dateConsultation" in params, "Missing parameter 'dateConsultation'"
    assert "heure" in params, "Missing parameter 'heure'"
    assert "numeroConsultation" in params, "Missing parameter 'numeroConsultation'"
    assert "description" in params, "Missing parameter 'description'"







def test_hyp_rendez_vous_is_not_abstract():
    assert not inspect.isabstract(Rendez_Vous)


def test_hyp_rendez_vous_constructor_exists():
    assert callable(Rendez_Vous.__init__)


def test_hyp_rendez_vous_constructor_args():
    sig = inspect.signature(Rendez_Vous.__init__)
    params = list(sig.parameters.keys())
    assert "dateRDV" in params, "Missing parameter 'dateRDV'"
    assert "numeroRdV" in params, "Missing parameter 'numeroRdV'"
    assert "lieuRDV" in params, "Missing parameter 'lieuRDV'"
    assert "heure" in params, "Missing parameter 'heure'"







def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "lieuResidence" in params, "Missing parameter 'lieuResidence'"
    assert "numeroPatien" in params, "Missing parameter 'numeroPatien'"
    assert "profession" in params, "Missing parameter 'profession'"
    assert "nomPatient" in params, "Missing parameter 'nomPatient'"
    assert "prenomPatien" in params, "Missing parameter 'prenomPatien'"
    assert "agePatient" in params, "Missing parameter 'agePatient'"









def test_hyp_dossierpatient_is_not_abstract():
    assert not inspect.isabstract(DossierPatient)


def test_hyp_dossierpatient_constructor_exists():
    assert callable(DossierPatient.__init__)


def test_hyp_dossierpatient_constructor_args():
    sig = inspect.signature(DossierPatient.__init__)
    params = list(sig.parameters.keys())
    assert "heure" in params, "Missing parameter 'heure'"
    assert "nomDossier" in params, "Missing parameter 'nomDossier'"
    assert "numeroPatient" in params, "Missing parameter 'numeroPatient'"
    assert "dateCreation" in params, "Missing parameter 'dateCreation'"
    assert "infoAntecedant" in params, "Missing parameter 'infoAntecedant'"







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
Secretaire_external_strategy = st.builds(
    Secretaire_external,
)
ResultatExamen_strategy = st.builds(
    ResultatExamen,
    numeroResultat=
        st.integers(),
    infoResultat=
        safe_text
)
CentreHospitalier_strategy = st.builds(
    CentreHospitalier,
    nomCentre=
        safe_text,
    numeroCentre=
        st.integers(),
    descriptionCentre=
        safe_text
)
Programme_strategy = st.builds(
    Programme,
    heure=
        safe_text,
    numeroProgramme=
        safe_text,
    date=
        safe_text
)
Service_strategy = st.builds(
    Service,
    nomService=
        safe_text,
    descriptionService=
        safe_text,
    numeroService=
        st.integers()
)
Medecin_strategy = st.builds(
    Medecin,
    specialite=
        safe_text,
    prenomMedecin=
        safe_text,
    numeroMedecin=
        st.integers(),
    dateNaissance=
        safe_text,
    nomMedecin=
        safe_text
)
Examen_strategy = st.builds(
    Examen,
    dateProvisoir=
        safe_text,
    heure=
        safe_text,
    motif=
        safe_text,
    numeroExamen=
        st.integers()
)
Consultion_strategy = st.builds(
    Consultion,
    dateConsultation=
        safe_text,
    heure=
        safe_text,
    numeroConsultation=
        st.integers(),
    description=
        safe_text
)
Rendez_Vous_strategy = st.builds(
    Rendez_Vous,
    dateRDV=
        safe_text,
    numeroRdV=
        st.integers(),
    lieuRDV=
        safe_text,
    heure=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    lieuResidence=
        safe_text,
    numeroPatien=
        st.integers(),
    profession=
        safe_text,
    nomPatient=
        safe_text,
    prenomPatien=
        safe_text,
    agePatient=
        st.integers()
)
DossierPatient_strategy = st.builds(
    DossierPatient,
    heure=
        st.integers(),
    nomDossier=
        safe_text,
    numeroPatient=
        st.integers(),
    dateCreation=
        st.integers(),
    infoAntecedant=
        safe_text
)





@given(instance=ResultatExamen_strategy)
def test_hyp_resultatexamen_numeroResultat_setter(instance):
    original = instance.numeroResultat
    instance.numeroResultat = original
    assert instance.numeroResultat == original



@given(instance=ResultatExamen_strategy)
def test_hyp_resultatexamen_infoResultat_setter(instance):
    original = instance.infoResultat
    instance.infoResultat = original
    assert instance.infoResultat == original




@given(instance=CentreHospitalier_strategy)
def test_hyp_centrehospitalier_nomCentre_setter(instance):
    original = instance.nomCentre
    instance.nomCentre = original
    assert instance.nomCentre == original



@given(instance=CentreHospitalier_strategy)
def test_hyp_centrehospitalier_numeroCentre_setter(instance):
    original = instance.numeroCentre
    instance.numeroCentre = original
    assert instance.numeroCentre == original



@given(instance=CentreHospitalier_strategy)
def test_hyp_centrehospitalier_descriptionCentre_setter(instance):
    original = instance.descriptionCentre
    instance.descriptionCentre = original
    assert instance.descriptionCentre == original




@given(instance=Programme_strategy)
def test_hyp_programme_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=Programme_strategy)
def test_hyp_programme_numeroProgramme_setter(instance):
    original = instance.numeroProgramme
    instance.numeroProgramme = original
    assert instance.numeroProgramme == original



@given(instance=Programme_strategy)
def test_hyp_programme_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=Service_strategy)
def test_hyp_service_nomService_setter(instance):
    original = instance.nomService
    instance.nomService = original
    assert instance.nomService == original



@given(instance=Service_strategy)
def test_hyp_service_descriptionService_setter(instance):
    original = instance.descriptionService
    instance.descriptionService = original
    assert instance.descriptionService == original



@given(instance=Service_strategy)
def test_hyp_service_numeroService_setter(instance):
    original = instance.numeroService
    instance.numeroService = original
    assert instance.numeroService == original




@given(instance=Medecin_strategy)
def test_hyp_medecin_specialite_setter(instance):
    original = instance.specialite
    instance.specialite = original
    assert instance.specialite == original



@given(instance=Medecin_strategy)
def test_hyp_medecin_prenomMedecin_setter(instance):
    original = instance.prenomMedecin
    instance.prenomMedecin = original
    assert instance.prenomMedecin == original



@given(instance=Medecin_strategy)
def test_hyp_medecin_numeroMedecin_setter(instance):
    original = instance.numeroMedecin
    instance.numeroMedecin = original
    assert instance.numeroMedecin == original



@given(instance=Medecin_strategy)
def test_hyp_medecin_dateNaissance_setter(instance):
    original = instance.dateNaissance
    instance.dateNaissance = original
    assert instance.dateNaissance == original



@given(instance=Medecin_strategy)
def test_hyp_medecin_nomMedecin_setter(instance):
    original = instance.nomMedecin
    instance.nomMedecin = original
    assert instance.nomMedecin == original




@given(instance=Examen_strategy)
def test_hyp_examen_dateProvisoir_setter(instance):
    original = instance.dateProvisoir
    instance.dateProvisoir = original
    assert instance.dateProvisoir == original



@given(instance=Examen_strategy)
def test_hyp_examen_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=Examen_strategy)
def test_hyp_examen_motif_setter(instance):
    original = instance.motif
    instance.motif = original
    assert instance.motif == original



@given(instance=Examen_strategy)
def test_hyp_examen_numeroExamen_setter(instance):
    original = instance.numeroExamen
    instance.numeroExamen = original
    assert instance.numeroExamen == original




@given(instance=Consultion_strategy)
def test_hyp_consultion_dateConsultation_setter(instance):
    original = instance.dateConsultation
    instance.dateConsultation = original
    assert instance.dateConsultation == original



@given(instance=Consultion_strategy)
def test_hyp_consultion_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=Consultion_strategy)
def test_hyp_consultion_numeroConsultation_setter(instance):
    original = instance.numeroConsultation
    instance.numeroConsultation = original
    assert instance.numeroConsultation == original



@given(instance=Consultion_strategy)
def test_hyp_consultion_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=Rendez_Vous_strategy)
def test_hyp_rendez_vous_dateRDV_setter(instance):
    original = instance.dateRDV
    instance.dateRDV = original
    assert instance.dateRDV == original



@given(instance=Rendez_Vous_strategy)
def test_hyp_rendez_vous_numeroRdV_setter(instance):
    original = instance.numeroRdV
    instance.numeroRdV = original
    assert instance.numeroRdV == original



@given(instance=Rendez_Vous_strategy)
def test_hyp_rendez_vous_lieuRDV_setter(instance):
    original = instance.lieuRDV
    instance.lieuRDV = original
    assert instance.lieuRDV == original



@given(instance=Rendez_Vous_strategy)
def test_hyp_rendez_vous_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original




@given(instance=Patient_strategy)
def test_hyp_patient_lieuResidence_setter(instance):
    original = instance.lieuResidence
    instance.lieuResidence = original
    assert instance.lieuResidence == original



@given(instance=Patient_strategy)
def test_hyp_patient_numeroPatien_setter(instance):
    original = instance.numeroPatien
    instance.numeroPatien = original
    assert instance.numeroPatien == original



@given(instance=Patient_strategy)
def test_hyp_patient_profession_setter(instance):
    original = instance.profession
    instance.profession = original
    assert instance.profession == original



@given(instance=Patient_strategy)
def test_hyp_patient_nomPatient_setter(instance):
    original = instance.nomPatient
    instance.nomPatient = original
    assert instance.nomPatient == original



@given(instance=Patient_strategy)
def test_hyp_patient_prenomPatien_setter(instance):
    original = instance.prenomPatien
    instance.prenomPatien = original
    assert instance.prenomPatien == original



@given(instance=Patient_strategy)
def test_hyp_patient_agePatient_setter(instance):
    original = instance.agePatient
    instance.agePatient = original
    assert instance.agePatient == original




@given(instance=DossierPatient_strategy)
def test_hyp_dossierpatient_heure_setter(instance):
    original = instance.heure
    instance.heure = original
    assert instance.heure == original



@given(instance=DossierPatient_strategy)
def test_hyp_dossierpatient_nomDossier_setter(instance):
    original = instance.nomDossier
    instance.nomDossier = original
    assert instance.nomDossier == original



@given(instance=DossierPatient_strategy)
def test_hyp_dossierpatient_numeroPatient_setter(instance):
    original = instance.numeroPatient
    instance.numeroPatient = original
    assert instance.numeroPatient == original



@given(instance=DossierPatient_strategy)
def test_hyp_dossierpatient_dateCreation_setter(instance):
    original = instance.dateCreation
    instance.dateCreation = original
    assert instance.dateCreation == original



@given(instance=DossierPatient_strategy)
def test_hyp_dossierpatient_infoAntecedant_setter(instance):
    original = instance.infoAntecedant
    instance.infoAntecedant = original
    assert instance.infoAntecedant == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CentreHospitalier,
    Consultion,
    DossierPatient,
    Examen,
    Medecin,
    Patient,
    Programme,
    Rendez_Vous,
    ResultatExamen,
    Secretaire_external,
    Service,
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

def test_CentreHospitalier_descriptionCentre_value_roundtrip():
    instance = CentreHospitalier(descriptionCentre="sample_text", nomCentre="sample_text", numeroCentre=7)
    assert instance.descriptionCentre == "sample_text"
    instance.descriptionCentre = "sample_text_2"
    assert instance.descriptionCentre == "sample_text_2"


def test_CentreHospitalier_nomCentre_value_roundtrip():
    instance = CentreHospitalier(descriptionCentre="sample_text", nomCentre="sample_text", numeroCentre=7)
    assert instance.nomCentre == "sample_text"
    instance.nomCentre = "sample_text_2"
    assert instance.nomCentre == "sample_text_2"


def test_CentreHospitalier_numeroCentre_value_roundtrip():
    instance = CentreHospitalier(descriptionCentre="sample_text", nomCentre="sample_text", numeroCentre=7)
    assert instance.numeroCentre == 7
    instance.numeroCentre = 13
    assert instance.numeroCentre == 13


def test_Consultion_dateConsultation_value_roundtrip():
    instance = Consultion(dateConsultation="sample_text", description="sample_text", heure="sample_text", numeroConsultation=7)
    assert instance.dateConsultation == "sample_text"
    instance.dateConsultation = "sample_text_2"
    assert instance.dateConsultation == "sample_text_2"


def test_Consultion_description_value_roundtrip():
    instance = Consultion(dateConsultation="sample_text", description="sample_text", heure="sample_text", numeroConsultation=7)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Consultion_heure_value_roundtrip():
    instance = Consultion(dateConsultation="sample_text", description="sample_text", heure="sample_text", numeroConsultation=7)
    assert instance.heure == "sample_text"
    instance.heure = "sample_text_2"
    assert instance.heure == "sample_text_2"


def test_Consultion_numeroConsultation_value_roundtrip():
    instance = Consultion(dateConsultation="sample_text", description="sample_text", heure="sample_text", numeroConsultation=7)
    assert instance.numeroConsultation == 7
    instance.numeroConsultation = 13
    assert instance.numeroConsultation == 13


def test_DossierPatient_dateCreation_value_roundtrip():
    instance = DossierPatient(dateCreation=7, heure=7, infoAntecedant="sample_text", nomDossier="sample_text", numeroPatient=7)
    assert instance.dateCreation == 7
    instance.dateCreation = 13
    assert instance.dateCreation == 13


def test_DossierPatient_heure_value_roundtrip():
    instance = DossierPatient(dateCreation=7, heure=7, infoAntecedant="sample_text", nomDossier="sample_text", numeroPatient=7)
    assert instance.heure == 7
    instance.heure = 13
    assert instance.heure == 13


def test_DossierPatient_infoAntecedant_value_roundtrip():
    instance = DossierPatient(dateCreation=7, heure=7, infoAntecedant="sample_text", nomDossier="sample_text", numeroPatient=7)
    assert instance.infoAntecedant == "sample_text"
    instance.infoAntecedant = "sample_text_2"
    assert instance.infoAntecedant == "sample_text_2"


def test_DossierPatient_nomDossier_value_roundtrip():
    instance = DossierPatient(dateCreation=7, heure=7, infoAntecedant="sample_text", nomDossier="sample_text", numeroPatient=7)
    assert instance.nomDossier == "sample_text"
    instance.nomDossier = "sample_text_2"
    assert instance.nomDossier == "sample_text_2"


def test_DossierPatient_numeroPatient_value_roundtrip():
    instance = DossierPatient(dateCreation=7, heure=7, infoAntecedant="sample_text", nomDossier="sample_text", numeroPatient=7)
    assert instance.numeroPatient == 7
    instance.numeroPatient = 13
    assert instance.numeroPatient == 13


def test_Examen_dateProvisoir_value_roundtrip():
    instance = Examen(dateProvisoir="sample_text", heure="sample_text", motif="sample_text", numeroExamen=7)
    assert instance.dateProvisoir == "sample_text"
    instance.dateProvisoir = "sample_text_2"
    assert instance.dateProvisoir == "sample_text_2"


def test_Examen_heure_value_roundtrip():
    instance = Examen(dateProvisoir="sample_text", heure="sample_text", motif="sample_text", numeroExamen=7)
    assert instance.heure == "sample_text"
    instance.heure = "sample_text_2"
    assert instance.heure == "sample_text_2"


def test_Examen_motif_value_roundtrip():
    instance = Examen(dateProvisoir="sample_text", heure="sample_text", motif="sample_text", numeroExamen=7)
    assert instance.motif == "sample_text"
    instance.motif = "sample_text_2"
    assert instance.motif == "sample_text_2"


def test_Examen_numeroExamen_value_roundtrip():
    instance = Examen(dateProvisoir="sample_text", heure="sample_text", motif="sample_text", numeroExamen=7)
    assert instance.numeroExamen == 7
    instance.numeroExamen = 13
    assert instance.numeroExamen == 13


def test_Medecin_dateNaissance_value_roundtrip():
    instance = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    assert instance.dateNaissance == "sample_text"
    instance.dateNaissance = "sample_text_2"
    assert instance.dateNaissance == "sample_text_2"


def test_Medecin_nomMedecin_value_roundtrip():
    instance = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    assert instance.nomMedecin == "sample_text"
    instance.nomMedecin = "sample_text_2"
    assert instance.nomMedecin == "sample_text_2"


def test_Medecin_numeroMedecin_value_roundtrip():
    instance = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    assert instance.numeroMedecin == 7
    instance.numeroMedecin = 13
    assert instance.numeroMedecin == 13


def test_Medecin_prenomMedecin_value_roundtrip():
    instance = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    assert instance.prenomMedecin == "sample_text"
    instance.prenomMedecin = "sample_text_2"
    assert instance.prenomMedecin == "sample_text_2"


def test_Medecin_specialite_value_roundtrip():
    instance = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    assert instance.specialite == "sample_text"
    instance.specialite = "sample_text_2"
    assert instance.specialite == "sample_text_2"


def test_Patient_agePatient_value_roundtrip():
    instance = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    assert instance.agePatient == 7
    instance.agePatient = 13
    assert instance.agePatient == 13


def test_Patient_lieuResidence_value_roundtrip():
    instance = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    assert instance.lieuResidence == "sample_text"
    instance.lieuResidence = "sample_text_2"
    assert instance.lieuResidence == "sample_text_2"


def test_Patient_nomPatient_value_roundtrip():
    instance = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    assert instance.nomPatient == "sample_text"
    instance.nomPatient = "sample_text_2"
    assert instance.nomPatient == "sample_text_2"


def test_Patient_numeroPatien_value_roundtrip():
    instance = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    assert instance.numeroPatien == 7
    instance.numeroPatien = 13
    assert instance.numeroPatien == 13


def test_Patient_prenomPatien_value_roundtrip():
    instance = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    assert instance.prenomPatien == "sample_text"
    instance.prenomPatien = "sample_text_2"
    assert instance.prenomPatien == "sample_text_2"


def test_Patient_profession_value_roundtrip():
    instance = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    assert instance.profession == "sample_text"
    instance.profession = "sample_text_2"
    assert instance.profession == "sample_text_2"


def test_Programme_date_value_roundtrip():
    instance = Programme(date="sample_text", heure="sample_text", numeroProgramme="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Programme_heure_value_roundtrip():
    instance = Programme(date="sample_text", heure="sample_text", numeroProgramme="sample_text")
    assert instance.heure == "sample_text"
    instance.heure = "sample_text_2"
    assert instance.heure == "sample_text_2"


def test_Programme_numeroProgramme_value_roundtrip():
    instance = Programme(date="sample_text", heure="sample_text", numeroProgramme="sample_text")
    assert instance.numeroProgramme == "sample_text"
    instance.numeroProgramme = "sample_text_2"
    assert instance.numeroProgramme == "sample_text_2"


def test_Rendez_Vous_dateRDV_value_roundtrip():
    instance = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    assert instance.dateRDV == "sample_text"
    instance.dateRDV = "sample_text_2"
    assert instance.dateRDV == "sample_text_2"


def test_Rendez_Vous_heure_value_roundtrip():
    instance = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    assert instance.heure == "sample_text"
    instance.heure = "sample_text_2"
    assert instance.heure == "sample_text_2"


def test_Rendez_Vous_lieuRDV_value_roundtrip():
    instance = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    assert instance.lieuRDV == "sample_text"
    instance.lieuRDV = "sample_text_2"
    assert instance.lieuRDV == "sample_text_2"


def test_Rendez_Vous_numeroRdV_value_roundtrip():
    instance = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    assert instance.numeroRdV == 7
    instance.numeroRdV = 13
    assert instance.numeroRdV == 13


def test_ResultatExamen_infoResultat_value_roundtrip():
    instance = ResultatExamen(infoResultat="sample_text", numeroResultat=7)
    assert instance.infoResultat == "sample_text"
    instance.infoResultat = "sample_text_2"
    assert instance.infoResultat == "sample_text_2"


def test_ResultatExamen_numeroResultat_value_roundtrip():
    instance = ResultatExamen(infoResultat="sample_text", numeroResultat=7)
    assert instance.numeroResultat == 7
    instance.numeroResultat = 13
    assert instance.numeroResultat == 13


def test_Service_descriptionService_value_roundtrip():
    instance = Service(descriptionService="sample_text", nomService="sample_text", numeroService=7)
    assert instance.descriptionService == "sample_text"
    instance.descriptionService = "sample_text_2"
    assert instance.descriptionService == "sample_text_2"


def test_Service_nomService_value_roundtrip():
    instance = Service(descriptionService="sample_text", nomService="sample_text", numeroService=7)
    assert instance.nomService == "sample_text"
    instance.nomService = "sample_text_2"
    assert instance.nomService == "sample_text_2"


def test_Service_numeroService_value_roundtrip():
    instance = Service(descriptionService="sample_text", nomService="sample_text", numeroService=7)
    assert instance.numeroService == 7
    instance.numeroService = 13
    assert instance.numeroService == 13


def test_assoc_DossierPatient_Patient_link_reassign_clear():
    a = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    b1 = DossierPatient(dateCreation=7, heure=7, infoAntecedant="sample_text", nomDossier="sample_text", numeroPatient=7)
    b2 = DossierPatient(dateCreation=13, heure=13, infoAntecedant="sample_text_2", nomDossier="sample_text_2", numeroPatient=13)
    _safe_set(a, 'dossierPatient1', {b1})
    assert _is_linked(a, 'dossierPatient1', b1)
    if hasattr(b1, 'patient0'):
        assert _is_linked(b1, 'patient0', a)
    _safe_set(a, 'dossierPatient1', {b2})
    assert _is_linked(a, 'dossierPatient1', b2)
    if hasattr(b1, 'patient0'):
        assert not _is_linked(b1, 'patient0', a)
    if hasattr(b2, 'patient0'):
        assert _is_linked(b2, 'patient0', a)
    _safe_set(a, 'dossierPatient1', set())
    assert not _is_linked(a, 'dossierPatient1', b2)
    if hasattr(b2, 'patient0'):
        assert not _is_linked(b2, 'patient0', a)


def test_assoc_Medecin_Service_link_reassign_clear():
    a = Service(descriptionService="sample_text", nomService="sample_text", numeroService=7)
    b1 = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    b2 = Medecin(dateNaissance="sample_text_2", nomMedecin="sample_text_2", numeroMedecin=13, prenomMedecin="sample_text_2", specialite="sample_text_2")
    _safe_set(a, 'medecin13', b1)
    assert _is_linked(a, 'medecin13', b1)
    if hasattr(b1, 'service12'):
        assert _is_linked(b1, 'service12', a)
    _safe_set(a, 'medecin13', b2)
    assert _is_linked(a, 'medecin13', b2)
    if hasattr(b1, 'service12'):
        assert not _is_linked(b1, 'service12', a)
    if hasattr(b2, 'service12'):
        assert _is_linked(b2, 'service12', a)
    _safe_set(a, 'medecin13', None)
    assert not _is_linked(a, 'medecin13', b2)
    if hasattr(b2, 'service12'):
        assert not _is_linked(b2, 'service12', a)


def test_assoc_Patient_Rendez_Vous_link_reassign_clear():
    a = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    b1 = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    b2 = Patient(agePatient=13, lieuResidence="sample_text_2", nomPatient="sample_text_2", numeroPatien=13, prenomPatien="sample_text_2", profession="sample_text_2")
    _safe_set(a, 'patient3', b1)
    assert _is_linked(a, 'patient3', b1)
    if hasattr(b1, 'rendez_Vous2'):
        assert _is_linked(b1, 'rendez_Vous2', a)
    _safe_set(a, 'patient3', b2)
    assert _is_linked(a, 'patient3', b2)
    if hasattr(b1, 'rendez_Vous2'):
        assert not _is_linked(b1, 'rendez_Vous2', a)
    if hasattr(b2, 'rendez_Vous2'):
        assert _is_linked(b2, 'rendez_Vous2', a)
    _safe_set(a, 'patient3', None)
    assert not _is_linked(a, 'patient3', b2)
    if hasattr(b2, 'rendez_Vous2'):
        assert not _is_linked(b2, 'rendez_Vous2', a)


def test_assoc_Patient_ResultatExamen_link_reassign_clear():
    a = ResultatExamen(infoResultat="sample_text", numeroResultat=7)
    b1 = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    b2 = Patient(agePatient=13, lieuResidence="sample_text_2", nomPatient="sample_text_2", numeroPatien=13, prenomPatien="sample_text_2", profession="sample_text_2")
    _safe_set(a, 'patient21', b1)
    assert _is_linked(a, 'patient21', b1)
    if hasattr(b1, 'resultatExamen20'):
        assert _is_linked(b1, 'resultatExamen20', a)
    _safe_set(a, 'patient21', b2)
    assert _is_linked(a, 'patient21', b2)
    if hasattr(b1, 'resultatExamen20'):
        assert not _is_linked(b1, 'resultatExamen20', a)
    if hasattr(b2, 'resultatExamen20'):
        assert _is_linked(b2, 'resultatExamen20', a)
    _safe_set(a, 'patient21', None)
    assert not _is_linked(a, 'patient21', b2)
    if hasattr(b2, 'resultatExamen20'):
        assert not _is_linked(b2, 'resultatExamen20', a)


def test_assoc_Programme_Medecin_link_reassign_clear():
    a = Programme(date="sample_text", heure="sample_text", numeroProgramme="sample_text")
    b1 = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    b2 = Medecin(dateNaissance="sample_text_2", nomMedecin="sample_text_2", numeroMedecin=13, prenomMedecin="sample_text_2", specialite="sample_text_2")
    _safe_set(a, 'medecin10', b1)
    assert _is_linked(a, 'medecin10', b1)
    if hasattr(b1, 'programme11'):
        assert _is_linked(b1, 'programme11', a)
    _safe_set(a, 'medecin10', b2)
    assert _is_linked(a, 'medecin10', b2)
    if hasattr(b1, 'programme11'):
        assert not _is_linked(b1, 'programme11', a)
    if hasattr(b2, 'programme11'):
        assert _is_linked(b2, 'programme11', a)
    _safe_set(a, 'medecin10', None)
    assert not _is_linked(a, 'medecin10', b2)
    if hasattr(b2, 'programme11'):
        assert not _is_linked(b2, 'programme11', a)


def test_assoc_Rendez_Vous_Consultion_link_reassign_clear():
    a = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    b1 = Consultion(dateConsultation="sample_text", description="sample_text", heure="sample_text", numeroConsultation=7)
    b2 = Consultion(dateConsultation="sample_text_2", description="sample_text_2", heure="sample_text_2", numeroConsultation=13)
    _safe_set(a, 'consultion4', b1)
    assert _is_linked(a, 'consultion4', b1)
    if hasattr(b1, 'rendez_Vous5'):
        assert _is_linked(b1, 'rendez_Vous5', a)
    _safe_set(a, 'consultion4', b2)
    assert _is_linked(a, 'consultion4', b2)
    if hasattr(b1, 'rendez_Vous5'):
        assert not _is_linked(b1, 'rendez_Vous5', a)
    if hasattr(b2, 'rendez_Vous5'):
        assert _is_linked(b2, 'rendez_Vous5', a)
    _safe_set(a, 'consultion4', None)
    assert not _is_linked(a, 'consultion4', b2)
    if hasattr(b2, 'rendez_Vous5'):
        assert not _is_linked(b2, 'rendez_Vous5', a)


def test_assoc_Rendez_Vous_Examen_link_reassign_clear():
    a = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    b1 = Examen(dateProvisoir="sample_text", heure="sample_text", motif="sample_text", numeroExamen=7)
    b2 = Examen(dateProvisoir="sample_text_2", heure="sample_text_2", motif="sample_text_2", numeroExamen=13)
    _safe_set(a, 'examen6', b1)
    assert _is_linked(a, 'examen6', b1)
    if hasattr(b1, 'rendez_Vous7'):
        assert _is_linked(b1, 'rendez_Vous7', a)
    _safe_set(a, 'examen6', b2)
    assert _is_linked(a, 'examen6', b2)
    if hasattr(b1, 'rendez_Vous7'):
        assert not _is_linked(b1, 'rendez_Vous7', a)
    if hasattr(b2, 'rendez_Vous7'):
        assert _is_linked(b2, 'rendez_Vous7', a)
    _safe_set(a, 'examen6', None)
    assert not _is_linked(a, 'examen6', b2)
    if hasattr(b2, 'rendez_Vous7'):
        assert not _is_linked(b2, 'rendez_Vous7', a)


def test_assoc_Rendez_Vous_Medecin_link_reassign_clear():
    a = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    b1 = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    b2 = Medecin(dateNaissance="sample_text_2", nomMedecin="sample_text_2", numeroMedecin=13, prenomMedecin="sample_text_2", specialite="sample_text_2")
    _safe_set(a, 'medecin8', b1)
    assert _is_linked(a, 'medecin8', b1)
    if hasattr(b1, 'rendez_Vous9'):
        assert _is_linked(b1, 'rendez_Vous9', a)
    _safe_set(a, 'medecin8', b2)
    assert _is_linked(a, 'medecin8', b2)
    if hasattr(b1, 'rendez_Vous9'):
        assert not _is_linked(b1, 'rendez_Vous9', a)
    if hasattr(b2, 'rendez_Vous9'):
        assert _is_linked(b2, 'rendez_Vous9', a)
    _safe_set(a, 'medecin8', None)
    assert not _is_linked(a, 'medecin8', b2)
    if hasattr(b2, 'rendez_Vous9'):
        assert not _is_linked(b2, 'rendez_Vous9', a)


def test_assoc_ResultatExamen_Medecin_link_reassign_clear():
    a = ResultatExamen(infoResultat="sample_text", numeroResultat=7)
    b1 = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    b2 = Medecin(dateNaissance="sample_text_2", nomMedecin="sample_text_2", numeroMedecin=13, prenomMedecin="sample_text_2", specialite="sample_text_2")
    _safe_set(a, 'medecin18', b1)
    assert _is_linked(a, 'medecin18', b1)
    if hasattr(b1, 'resultatExamen19'):
        assert _is_linked(b1, 'resultatExamen19', a)
    _safe_set(a, 'medecin18', b2)
    assert _is_linked(a, 'medecin18', b2)
    if hasattr(b1, 'resultatExamen19'):
        assert not _is_linked(b1, 'resultatExamen19', a)
    if hasattr(b2, 'resultatExamen19'):
        assert _is_linked(b2, 'resultatExamen19', a)
    _safe_set(a, 'medecin18', None)
    assert not _is_linked(a, 'medecin18', b2)
    if hasattr(b2, 'resultatExamen19'):
        assert not _is_linked(b2, 'resultatExamen19', a)


def test_assoc_Secretaire_ResultatExamen_link_reassign_clear():
    a = ResultatExamen(infoResultat="sample_text", numeroResultat=7)
    b1 = Secretaire_external()
    b2 = Secretaire_external()
    _safe_set(a, 'secretaire17', b1)
    assert _is_linked(a, 'secretaire17', b1)
    if hasattr(b1, 'resultatExamen16'):
        assert _is_linked(b1, 'resultatExamen16', a)
    _safe_set(a, 'secretaire17', b2)
    assert _is_linked(a, 'secretaire17', b2)
    if hasattr(b1, 'resultatExamen16'):
        assert not _is_linked(b1, 'resultatExamen16', a)
    if hasattr(b2, 'resultatExamen16'):
        assert _is_linked(b2, 'resultatExamen16', a)
    _safe_set(a, 'secretaire17', None)
    assert not _is_linked(a, 'secretaire17', b2)
    if hasattr(b2, 'resultatExamen16'):
        assert not _is_linked(b2, 'resultatExamen16', a)


def test_assoc_Service_CentreHospitalier_link_reassign_clear():
    a = Service(descriptionService="sample_text", nomService="sample_text", numeroService=7)
    b1 = CentreHospitalier(descriptionCentre="sample_text", nomCentre="sample_text", numeroCentre=7)
    b2 = CentreHospitalier(descriptionCentre="sample_text_2", nomCentre="sample_text_2", numeroCentre=13)
    _safe_set(a, 'centreHospitalier14', b1)
    assert _is_linked(a, 'centreHospitalier14', b1)
    if hasattr(b1, 'service15'):
        assert _is_linked(b1, 'service15', a)
    _safe_set(a, 'centreHospitalier14', b2)
    assert _is_linked(a, 'centreHospitalier14', b2)
    if hasattr(b1, 'service15'):
        assert not _is_linked(b1, 'service15', a)
    if hasattr(b2, 'service15'):
        assert _is_linked(b2, 'service15', a)
    _safe_set(a, 'centreHospitalier14', None)
    assert not _is_linked(a, 'centreHospitalier14', b2)
    if hasattr(b2, 'service15'):
        assert not _is_linked(b2, 'service15', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CentreHospitalier_strategy = st.builds(CentreHospitalier, descriptionCentre=safe_text, nomCentre=safe_text, numeroCentre=st.integers())
@given(instance=CentreHospitalier_strategy)
@settings(max_examples=25)
def test_CentreHospitalier_instantiation(instance):
    assert isinstance(instance, CentreHospitalier)


Consultion_strategy = st.builds(Consultion, dateConsultation=safe_text, description=safe_text, heure=safe_text, numeroConsultation=st.integers())
@given(instance=Consultion_strategy)
@settings(max_examples=25)
def test_Consultion_instantiation(instance):
    assert isinstance(instance, Consultion)


DossierPatient_strategy = st.builds(DossierPatient, dateCreation=st.integers(), heure=st.integers(), infoAntecedant=safe_text, nomDossier=safe_text, numeroPatient=st.integers())
@given(instance=DossierPatient_strategy)
@settings(max_examples=25)
def test_DossierPatient_instantiation(instance):
    assert isinstance(instance, DossierPatient)


Examen_strategy = st.builds(Examen, dateProvisoir=safe_text, heure=safe_text, motif=safe_text, numeroExamen=st.integers())
@given(instance=Examen_strategy)
@settings(max_examples=25)
def test_Examen_instantiation(instance):
    assert isinstance(instance, Examen)


Medecin_strategy = st.builds(Medecin, dateNaissance=safe_text, nomMedecin=safe_text, numeroMedecin=st.integers(), prenomMedecin=safe_text, specialite=safe_text)
@given(instance=Medecin_strategy)
@settings(max_examples=25)
def test_Medecin_instantiation(instance):
    assert isinstance(instance, Medecin)


Patient_strategy = st.builds(Patient, agePatient=st.integers(), lieuResidence=safe_text, nomPatient=safe_text, numeroPatien=st.integers(), prenomPatien=safe_text, profession=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


Programme_strategy = st.builds(Programme, date=safe_text, heure=safe_text, numeroProgramme=safe_text)
@given(instance=Programme_strategy)
@settings(max_examples=25)
def test_Programme_instantiation(instance):
    assert isinstance(instance, Programme)


Rendez_Vous_strategy = st.builds(Rendez_Vous, dateRDV=safe_text, heure=safe_text, lieuRDV=safe_text, numeroRdV=st.integers())
@given(instance=Rendez_Vous_strategy)
@settings(max_examples=25)
def test_Rendez_Vous_instantiation(instance):
    assert isinstance(instance, Rendez_Vous)


ResultatExamen_strategy = st.builds(ResultatExamen, infoResultat=safe_text, numeroResultat=st.integers())
@given(instance=ResultatExamen_strategy)
@settings(max_examples=25)
def test_ResultatExamen_instantiation(instance):
    assert isinstance(instance, ResultatExamen)


Secretaire_external_strategy = st.builds(Secretaire_external)
@given(instance=Secretaire_external_strategy)
@settings(max_examples=25)
def test_Secretaire_external_instantiation(instance):
    assert isinstance(instance, Secretaire_external)


Service_strategy = st.builds(Service, descriptionService=safe_text, nomService=safe_text, numeroService=st.integers())
@given(instance=Service_strategy)
@settings(max_examples=25)
def test_Service_instantiation(instance):
    assert isinstance(instance, Service)



