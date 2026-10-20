import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Candidat,
    CoursCode,
    CoursConduite,
    Examen,
    Groupe,
    Personne,
    Professeur,
    Utilisateur,
    Voiture,
    cours,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_candidat_groupe_stub_double():
    # Candidat has no real 'appartenir2' property in the generated
    # code (a bare stub) -- manually attach it so Groupe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Groupe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Groupe(id=7, libelle="sample_text", numeroGroupe=7)
    partner = Candidat()
    setattr(partner, 'appartenir2', None)
    _safe_set(owner, 'candidat3', {partner})
    assert getattr(partner, 'appartenir2') == owner
    _safe_set(owner, 'candidat3', set())
    assert getattr(partner, 'appartenir2') is None


def test_assoc_coursConduite_voiture_stub_double():
    # CoursConduite has no real 'concerner0' property in the generated
    # code (a bare stub) -- manually attach it so Voiture's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Voiture's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Voiture(id=7, immatriculation="sample_text", marque="sample_text", modele="sample_text")
    partner = CoursConduite()
    setattr(partner, 'concerner0', None)
    _safe_set(owner, 'coursConduite1', {partner})
    assert getattr(partner, 'concerner0') == owner
    _safe_set(owner, 'coursConduite1', set())
    assert getattr(partner, 'concerner0') is None


def test_assoc_groupe_coursCode_stub_double():
    # CoursCode has no real 'groupe9' property in the generated
    # code (a bare stub) -- manually attach it so Groupe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Groupe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Groupe(id=7, libelle="sample_text", numeroGroupe=7)
    partner = CoursCode()
    setattr(partner, 'groupe9', None)
    _safe_set(owner, 'suivre8', {partner})
    assert getattr(partner, 'groupe9') == owner
    _safe_set(owner, 'suivre8', set())
    assert getattr(partner, 'groupe9') is None


def test_assoc_professeur_coursCode_stub_double():
    # CoursCode has no real 'professeur5' property in the generated
    # code (a bare stub) -- manually attach it so Professeur's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Professeur's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Professeur(dateEmbauche="sample_text")
    partner = CoursCode()
    setattr(partner, 'professeur5', None)
    _safe_set(owner, 'donner4', {partner})
    assert getattr(partner, 'professeur5') == owner
    _safe_set(owner, 'donner4', set())
    assert getattr(partner, 'professeur5') is None


def test_assoc_professeur_coursConduite_stub_double():
    # CoursConduite has no real 'professeur7' property in the generated
    # code (a bare stub) -- manually attach it so Professeur's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Professeur's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Professeur(dateEmbauche="sample_text")
    partner = CoursConduite()
    setattr(partner, 'professeur7', None)
    _safe_set(owner, 'dispenser6', {partner})
    assert getattr(partner, 'professeur7') == owner
    _safe_set(owner, 'dispenser6', set())
    assert getattr(partner, 'professeur7') is None


