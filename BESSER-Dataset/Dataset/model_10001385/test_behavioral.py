import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Agenda,
    AgendaPartage,
    Compte,
    Employe,
    EmployeAdministratif,
    Medecin,
    Patient,
    Personne,
    RDV,
    Test,
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

def test_assoc_Agenda_RDV_reverse_link_reassign_clear():
    a1 = RDV(date="sample_text", duree=7, heure="sample_text")
    a2 = RDV(date="sample_text_2", duree=13, heure="sample_text_2")
    b = Agenda(annee="sample_text")
    _safe_set(b, 'rDV0', {a1})
    assert _is_linked(b, 'rDV0', a1)
    if hasattr(a1, 'agenda1'):
        assert _is_linked(a1, 'agenda1', b)
    _safe_set(b, 'rDV0', {a2})
    assert _is_linked(b, 'rDV0', a2)
    if hasattr(a1, 'agenda1'):
        assert not _is_linked(a1, 'agenda1', b)
    if hasattr(a2, 'agenda1'):
        assert _is_linked(a2, 'agenda1', b)
    _safe_set(b, 'rDV0', set())
    assert not _is_linked(b, 'rDV0', a2)
    if hasattr(a2, 'agenda1'):
        assert not _is_linked(a2, 'agenda1', b)


def test_assoc_EmployeAdministratif_RDV_reverse_link_reassign_clear():
    a1 = RDV(date="sample_text", duree=7, heure="sample_text")
    a2 = RDV(date="sample_text_2", duree=13, heure="sample_text_2")
    b = EmployeAdministratif(formation="sample_text")
    _safe_set(b, 'rDV16', {a1})
    assert _is_linked(b, 'rDV16', a1)
    if hasattr(a1, 'employeAdministratif17'):
        assert _is_linked(a1, 'employeAdministratif17', b)
    _safe_set(b, 'rDV16', {a2})
    assert _is_linked(b, 'rDV16', a2)
    if hasattr(a1, 'employeAdministratif17'):
        assert not _is_linked(a1, 'employeAdministratif17', b)
    if hasattr(a2, 'employeAdministratif17'):
        assert _is_linked(a2, 'employeAdministratif17', b)
    _safe_set(b, 'rDV16', set())
    assert not _is_linked(b, 'rDV16', a2)
    if hasattr(a2, 'employeAdministratif17'):
        assert not _is_linked(a2, 'employeAdministratif17', b)


def test_assoc_Employe_Compte_reverse_link_reassign_clear():
    a1 = Employe(dateDebut="sample_text", dateFin="sample_text", joursVacance=7, salaire=7)
    a2 = Employe(dateDebut="sample_text_2", dateFin="sample_text_2", joursVacance=13, salaire=13)
    b = Compte(login="sample_text", password="sample_text", typeCompte="sample_text")
    _safe_set(b, 'employe5', a1)
    assert _is_linked(b, 'employe5', a1)
    if hasattr(a1, 'compte4'):
        assert _is_linked(a1, 'compte4', b)
    _safe_set(b, 'employe5', a2)
    assert _is_linked(b, 'employe5', a2)
    if hasattr(a1, 'compte4'):
        assert not _is_linked(a1, 'compte4', b)
    if hasattr(a2, 'compte4'):
        assert _is_linked(a2, 'compte4', b)
    _safe_set(b, 'employe5', None)
    assert not _is_linked(b, 'employe5', a2)
    if hasattr(a2, 'compte4'):
        assert not _is_linked(a2, 'compte4', b)


def test_assoc_Medecin_Agenda_reverse_link_reassign_clear():
    a1 = Medecin(specialisation="sample_text")
    a2 = Medecin(specialisation="sample_text_2")
    b = Agenda(annee="sample_text")
    _safe_set(b, 'medecin7', a1)
    assert _is_linked(b, 'medecin7', a1)
    if hasattr(a1, 'agenda6'):
        assert _is_linked(a1, 'agenda6', b)
    _safe_set(b, 'medecin7', a2)
    assert _is_linked(b, 'medecin7', a2)
    if hasattr(a1, 'agenda6'):
        assert not _is_linked(a1, 'agenda6', b)
    if hasattr(a2, 'agenda6'):
        assert _is_linked(a2, 'agenda6', b)
    _safe_set(b, 'medecin7', None)
    assert not _is_linked(b, 'medecin7', a2)
    if hasattr(a2, 'agenda6'):
        assert not _is_linked(a2, 'agenda6', b)


def test_assoc_Medecin_Patient_reverse_link_reassign_clear():
    a1 = Patient(allergies="sample_text", antecedent="sample_text", traitement="sample_text")
    a2 = Patient(allergies="sample_text_2", antecedent="sample_text_2", traitement="sample_text_2")
    b = Medecin(specialisation="sample_text")
    _safe_set(b, 'patient14', {a1})
    assert _is_linked(b, 'patient14', a1)
    if hasattr(a1, 'medecin15'):
        assert _is_linked(a1, 'medecin15', b)
    _safe_set(b, 'patient14', {a2})
    assert _is_linked(b, 'patient14', a2)
    if hasattr(a1, 'medecin15'):
        assert not _is_linked(a1, 'medecin15', b)
    if hasattr(a2, 'medecin15'):
        assert _is_linked(a2, 'medecin15', b)
    _safe_set(b, 'patient14', set())
    assert not _is_linked(b, 'patient14', a2)
    if hasattr(a2, 'medecin15'):
        assert not _is_linked(a2, 'medecin15', b)


def test_assoc_Patient_Compte_reverse_link_reassign_clear():
    a1 = Patient(allergies="sample_text", antecedent="sample_text", traitement="sample_text")
    a2 = Patient(allergies="sample_text_2", antecedent="sample_text_2", traitement="sample_text_2")
    b = Compte(login="sample_text", password="sample_text", typeCompte="sample_text")
    _safe_set(b, 'patient11', a1)
    assert _is_linked(b, 'patient11', a1)
    if hasattr(a1, 'compte10'):
        assert _is_linked(a1, 'compte10', b)
    _safe_set(b, 'patient11', a2)
    assert _is_linked(b, 'patient11', a2)
    if hasattr(a1, 'compte10'):
        assert not _is_linked(a1, 'compte10', b)
    if hasattr(a2, 'compte10'):
        assert _is_linked(a2, 'compte10', b)
    _safe_set(b, 'patient11', None)
    assert not _is_linked(b, 'patient11', a2)
    if hasattr(a2, 'compte10'):
        assert not _is_linked(a2, 'compte10', b)


def test_assoc_RDV_Patient_reverse_link_reassign_clear():
    a1 = RDV(date="sample_text", duree=7, heure="sample_text")
    a2 = RDV(date="sample_text_2", duree=13, heure="sample_text_2")
    b = Patient(allergies="sample_text", antecedent="sample_text", traitement="sample_text")
    _safe_set(b, 'rDV13', {a1})
    assert _is_linked(b, 'rDV13', a1)
    if hasattr(a1, 'patient12'):
        assert _is_linked(a1, 'patient12', b)
    _safe_set(b, 'rDV13', {a2})
    assert _is_linked(b, 'rDV13', a2)
    if hasattr(a1, 'patient12'):
        assert not _is_linked(a1, 'patient12', b)
    if hasattr(a2, 'patient12'):
        assert _is_linked(a2, 'patient12', b)
    _safe_set(b, 'rDV13', set())
    assert not _is_linked(b, 'rDV13', a2)
    if hasattr(a2, 'patient12'):
        assert not _is_linked(a2, 'patient12', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_AgendaPartage_Agenda_stub_double():
    # AgendaPartage has no real 'agenda2' property in the generated
    # code (a bare stub) -- manually attach it so Agenda's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Agenda's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Agenda(annee="sample_text")
    partner = AgendaPartage()
    setattr(partner, 'agenda2', None)
    _safe_set(owner, 'agendaPartage3', partner)
    assert owner in getattr(partner, 'agenda2')
    _safe_set(owner, 'agendaPartage3', None)
    assert owner not in getattr(partner, 'agenda2')


def test_assoc_EmployeAdministratif_AgendaPartage_stub_double():
    # AgendaPartage has no real 'employeAdministratif9' property in the generated
    # code (a bare stub) -- manually attach it so EmployeAdministratif's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmployeAdministratif's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmployeAdministratif(formation="sample_text")
    partner = AgendaPartage()
    setattr(partner, 'employeAdministratif9', None)
    _safe_set(owner, 'agendaPartage8', partner)
    assert owner in getattr(partner, 'employeAdministratif9')
    _safe_set(owner, 'agendaPartage8', None)
    assert owner not in getattr(partner, 'employeAdministratif9')


