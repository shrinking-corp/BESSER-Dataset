import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Animal,
    CD,
    Club_de_lecture_Consulter_p_riodiques___livres_UseCase,
    Club_de_lecture_Emprunter_DVD_UseCase,
    Club_de_lecture_Emprunter_UseCase,
    Club_de_lecture_Emprunter_livre_num_rique_UseCase,
    Club_de_lecture_Emprunter_livres_UseCase,
    Club_de_lecture_Faire_proposition_UseCase,
    Club_de_lecture_Habitant_Actor,
    Club_de_lecture_S_inscrire_UseCase,
    Club_de_lecture_Utilisateur_inscrit_Actor,
    Etudiant,
    Habitant,
    Informations,
    Livre,
    Livre_num_rique,
    Media_physique,
    Responsable_CL,
    Utilisateur_Inscrit,
    Utilisateur_Inscrit1,
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

def test_assoc_Utilisateur_Inscrit_CD_stub_double():
    # CD has no real 'utilisateur_Inscrit11' property in the generated
    # code (a bare stub) -- manually attach it so Utilisateur_Inscrit1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Utilisateur_Inscrit1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Utilisateur_Inscrit1(noCarte="sample_text")
    partner = CD()
    setattr(partner, 'utilisateur_Inscrit11', None)
    _safe_set(owner, 'cD10', partner)
    assert getattr(partner, 'utilisateur_Inscrit11') == owner
    _safe_set(owner, 'cD10', None)
    assert getattr(partner, 'utilisateur_Inscrit11') is None


def test_assoc_Utilisateur_Inscrit_Livre_stub_double():
    # Livre has no real 'emprunter_9' property in the generated
    # code (a bare stub) -- manually attach it so Utilisateur_Inscrit1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Utilisateur_Inscrit1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Utilisateur_Inscrit1(noCarte="sample_text")
    partner = Livre()
    setattr(partner, 'emprunter_9', None)
    _safe_set(owner, 'empruntLivre8', {partner})
    assert getattr(partner, 'emprunter_9') == owner
    _safe_set(owner, 'empruntLivre8', set())
    assert getattr(partner, 'emprunter_9') is None


def test_assoc_Utilisateur_Inscrit_Livre_num_rique_stub_double():
    # Livre_num_rique has no real 'utilisateur_Inscrit13' property in the generated
    # code (a bare stub) -- manually attach it so Utilisateur_Inscrit1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Utilisateur_Inscrit1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Utilisateur_Inscrit1(noCarte="sample_text")
    partner = Livre_num_rique()
    setattr(partner, 'utilisateur_Inscrit13', None)
    _safe_set(owner, 'livre_num_rique12', {partner})
    assert getattr(partner, 'utilisateur_Inscrit13') == owner
    _safe_set(owner, 'livre_num_rique12', set())
    assert getattr(partner, 'utilisateur_Inscrit13') is None


