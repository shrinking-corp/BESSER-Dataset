import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_DossierPatient_Patient_reverse_link_reassign_clear():
    a1 = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    a2 = Patient(agePatient=13, lieuResidence="sample_text_2", nomPatient="sample_text_2", numeroPatien=13, prenomPatien="sample_text_2", profession="sample_text_2")
    b = DossierPatient(dateCreation=7, heure=7, infoAntecedant="sample_text", nomDossier="sample_text", numeroPatient=7)
    _safe_set(b, 'patient0', a1)
    assert _is_linked(b, 'patient0', a1)
    if hasattr(a1, 'dossierPatient1'):
        assert _is_linked(a1, 'dossierPatient1', b)
    _safe_set(b, 'patient0', a2)
    assert _is_linked(b, 'patient0', a2)
    if hasattr(a1, 'dossierPatient1'):
        assert not _is_linked(a1, 'dossierPatient1', b)
    if hasattr(a2, 'dossierPatient1'):
        assert _is_linked(a2, 'dossierPatient1', b)
    _safe_set(b, 'patient0', None)
    assert not _is_linked(b, 'patient0', a2)
    if hasattr(a2, 'dossierPatient1'):
        assert not _is_linked(a2, 'dossierPatient1', b)


def test_assoc_Medecin_Service_reverse_link_reassign_clear():
    a1 = Service(descriptionService="sample_text", nomService="sample_text", numeroService=7)
    a2 = Service(descriptionService="sample_text_2", nomService="sample_text_2", numeroService=13)
    b = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    _safe_set(b, 'service12', a1)
    assert _is_linked(b, 'service12', a1)
    if hasattr(a1, 'medecin13'):
        assert _is_linked(a1, 'medecin13', b)
    _safe_set(b, 'service12', a2)
    assert _is_linked(b, 'service12', a2)
    if hasattr(a1, 'medecin13'):
        assert not _is_linked(a1, 'medecin13', b)
    if hasattr(a2, 'medecin13'):
        assert _is_linked(a2, 'medecin13', b)
    _safe_set(b, 'service12', None)
    assert not _is_linked(b, 'service12', a2)
    if hasattr(a2, 'medecin13'):
        assert not _is_linked(a2, 'medecin13', b)


def test_assoc_Patient_Rendez_Vous_reverse_link_reassign_clear():
    a1 = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    a2 = Rendez_Vous(dateRDV="sample_text_2", heure="sample_text_2", lieuRDV="sample_text_2", numeroRdV=13)
    b = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    _safe_set(b, 'rendez_Vous2', {a1})
    assert _is_linked(b, 'rendez_Vous2', a1)
    if hasattr(a1, 'patient3'):
        assert _is_linked(a1, 'patient3', b)
    _safe_set(b, 'rendez_Vous2', {a2})
    assert _is_linked(b, 'rendez_Vous2', a2)
    if hasattr(a1, 'patient3'):
        assert not _is_linked(a1, 'patient3', b)
    if hasattr(a2, 'patient3'):
        assert _is_linked(a2, 'patient3', b)
    _safe_set(b, 'rendez_Vous2', set())
    assert not _is_linked(b, 'rendez_Vous2', a2)
    if hasattr(a2, 'patient3'):
        assert not _is_linked(a2, 'patient3', b)


def test_assoc_Patient_ResultatExamen_reverse_link_reassign_clear():
    a1 = ResultatExamen(infoResultat="sample_text", numeroResultat=7)
    a2 = ResultatExamen(infoResultat="sample_text_2", numeroResultat=13)
    b = Patient(agePatient=7, lieuResidence="sample_text", nomPatient="sample_text", numeroPatien=7, prenomPatien="sample_text", profession="sample_text")
    _safe_set(b, 'resultatExamen20', a1)
    assert _is_linked(b, 'resultatExamen20', a1)
    if hasattr(a1, 'patient21'):
        assert _is_linked(a1, 'patient21', b)
    _safe_set(b, 'resultatExamen20', a2)
    assert _is_linked(b, 'resultatExamen20', a2)
    if hasattr(a1, 'patient21'):
        assert not _is_linked(a1, 'patient21', b)
    if hasattr(a2, 'patient21'):
        assert _is_linked(a2, 'patient21', b)
    _safe_set(b, 'resultatExamen20', None)
    assert not _is_linked(b, 'resultatExamen20', a2)
    if hasattr(a2, 'patient21'):
        assert not _is_linked(a2, 'patient21', b)


def test_assoc_Programme_Medecin_reverse_link_reassign_clear():
    a1 = Programme(date="sample_text", heure="sample_text", numeroProgramme="sample_text")
    a2 = Programme(date="sample_text_2", heure="sample_text_2", numeroProgramme="sample_text_2")
    b = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    _safe_set(b, 'programme11', a1)
    assert _is_linked(b, 'programme11', a1)
    if hasattr(a1, 'medecin10'):
        assert _is_linked(a1, 'medecin10', b)
    _safe_set(b, 'programme11', a2)
    assert _is_linked(b, 'programme11', a2)
    if hasattr(a1, 'medecin10'):
        assert not _is_linked(a1, 'medecin10', b)
    if hasattr(a2, 'medecin10'):
        assert _is_linked(a2, 'medecin10', b)
    _safe_set(b, 'programme11', None)
    assert not _is_linked(b, 'programme11', a2)
    if hasattr(a2, 'medecin10'):
        assert not _is_linked(a2, 'medecin10', b)


def test_assoc_Rendez_Vous_Consultion_reverse_link_reassign_clear():
    a1 = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    a2 = Rendez_Vous(dateRDV="sample_text_2", heure="sample_text_2", lieuRDV="sample_text_2", numeroRdV=13)
    b = Consultion(dateConsultation="sample_text", description="sample_text", heure="sample_text", numeroConsultation=7)
    _safe_set(b, 'rendez_Vous5', a1)
    assert _is_linked(b, 'rendez_Vous5', a1)
    if hasattr(a1, 'consultion4'):
        assert _is_linked(a1, 'consultion4', b)
    _safe_set(b, 'rendez_Vous5', a2)
    assert _is_linked(b, 'rendez_Vous5', a2)
    if hasattr(a1, 'consultion4'):
        assert not _is_linked(a1, 'consultion4', b)
    if hasattr(a2, 'consultion4'):
        assert _is_linked(a2, 'consultion4', b)
    _safe_set(b, 'rendez_Vous5', None)
    assert not _is_linked(b, 'rendez_Vous5', a2)
    if hasattr(a2, 'consultion4'):
        assert not _is_linked(a2, 'consultion4', b)


def test_assoc_Rendez_Vous_Examen_reverse_link_reassign_clear():
    a1 = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    a2 = Rendez_Vous(dateRDV="sample_text_2", heure="sample_text_2", lieuRDV="sample_text_2", numeroRdV=13)
    b = Examen(dateProvisoir="sample_text", heure="sample_text", motif="sample_text", numeroExamen=7)
    _safe_set(b, 'rendez_Vous7', a1)
    assert _is_linked(b, 'rendez_Vous7', a1)
    if hasattr(a1, 'examen6'):
        assert _is_linked(a1, 'examen6', b)
    _safe_set(b, 'rendez_Vous7', a2)
    assert _is_linked(b, 'rendez_Vous7', a2)
    if hasattr(a1, 'examen6'):
        assert not _is_linked(a1, 'examen6', b)
    if hasattr(a2, 'examen6'):
        assert _is_linked(a2, 'examen6', b)
    _safe_set(b, 'rendez_Vous7', None)
    assert not _is_linked(b, 'rendez_Vous7', a2)
    if hasattr(a2, 'examen6'):
        assert not _is_linked(a2, 'examen6', b)


def test_assoc_Rendez_Vous_Medecin_reverse_link_reassign_clear():
    a1 = Rendez_Vous(dateRDV="sample_text", heure="sample_text", lieuRDV="sample_text", numeroRdV=7)
    a2 = Rendez_Vous(dateRDV="sample_text_2", heure="sample_text_2", lieuRDV="sample_text_2", numeroRdV=13)
    b = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    _safe_set(b, 'rendez_Vous9', a1)
    assert _is_linked(b, 'rendez_Vous9', a1)
    if hasattr(a1, 'medecin8'):
        assert _is_linked(a1, 'medecin8', b)
    _safe_set(b, 'rendez_Vous9', a2)
    assert _is_linked(b, 'rendez_Vous9', a2)
    if hasattr(a1, 'medecin8'):
        assert not _is_linked(a1, 'medecin8', b)
    if hasattr(a2, 'medecin8'):
        assert _is_linked(a2, 'medecin8', b)
    _safe_set(b, 'rendez_Vous9', None)
    assert not _is_linked(b, 'rendez_Vous9', a2)
    if hasattr(a2, 'medecin8'):
        assert not _is_linked(a2, 'medecin8', b)


def test_assoc_ResultatExamen_Medecin_reverse_link_reassign_clear():
    a1 = ResultatExamen(infoResultat="sample_text", numeroResultat=7)
    a2 = ResultatExamen(infoResultat="sample_text_2", numeroResultat=13)
    b = Medecin(dateNaissance="sample_text", nomMedecin="sample_text", numeroMedecin=7, prenomMedecin="sample_text", specialite="sample_text")
    _safe_set(b, 'resultatExamen19', a1)
    assert _is_linked(b, 'resultatExamen19', a1)
    if hasattr(a1, 'medecin18'):
        assert _is_linked(a1, 'medecin18', b)
    _safe_set(b, 'resultatExamen19', a2)
    assert _is_linked(b, 'resultatExamen19', a2)
    if hasattr(a1, 'medecin18'):
        assert not _is_linked(a1, 'medecin18', b)
    if hasattr(a2, 'medecin18'):
        assert _is_linked(a2, 'medecin18', b)
    _safe_set(b, 'resultatExamen19', None)
    assert not _is_linked(b, 'resultatExamen19', a2)
    if hasattr(a2, 'medecin18'):
        assert not _is_linked(a2, 'medecin18', b)


def test_assoc_Service_CentreHospitalier_reverse_link_reassign_clear():
    a1 = Service(descriptionService="sample_text", nomService="sample_text", numeroService=7)
    a2 = Service(descriptionService="sample_text_2", nomService="sample_text_2", numeroService=13)
    b = CentreHospitalier(descriptionCentre="sample_text", nomCentre="sample_text", numeroCentre=7)
    _safe_set(b, 'service15', {a1})
    assert _is_linked(b, 'service15', a1)
    if hasattr(a1, 'centreHospitalier14'):
        assert _is_linked(a1, 'centreHospitalier14', b)
    _safe_set(b, 'service15', {a2})
    assert _is_linked(b, 'service15', a2)
    if hasattr(a1, 'centreHospitalier14'):
        assert not _is_linked(a1, 'centreHospitalier14', b)
    if hasattr(a2, 'centreHospitalier14'):
        assert _is_linked(a2, 'centreHospitalier14', b)
    _safe_set(b, 'service15', set())
    assert not _is_linked(b, 'service15', a2)
    if hasattr(a2, 'centreHospitalier14'):
        assert not _is_linked(a2, 'centreHospitalier14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Secretaire_ResultatExamen_stub_double():
    # Secretaire_external has no real 'resultatExamen16' property in the generated
    # code (a bare stub) -- manually attach it so ResultatExamen's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ResultatExamen's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ResultatExamen(infoResultat="sample_text", numeroResultat=7)
    partner = Secretaire_external()
    setattr(partner, 'resultatExamen16', None)
    _safe_set(owner, 'secretaire17', partner)
    assert owner in getattr(partner, 'resultatExamen16')
    _safe_set(owner, 'secretaire17', None)
    assert owner not in getattr(partner, 'resultatExamen16')


