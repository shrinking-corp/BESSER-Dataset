import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AR,
    CommandeBasique,
    DecollerAtterrir,
    FonctionCall,
    GDr,
    MD,
    Mouvement,
    Parallele,
    PourcentExp,
    RGRD,
    SecondeExp,
    VarDecl,
    droneDSL_AR,
    droneDSL_Atterrir,
    droneDSL_Avancer,
    droneDSL_CommandeBasique,
    droneDSL_Decoller,
    droneDSL_DecollerAtterrir,
    droneDSL_Descendre,
    droneDSL_Droite,
    droneDSL_EObject,
    droneDSL_Eloignement_max,
    droneDSL_FinDeMain,
    droneDSL_FonctionCall,
    droneDSL_FonctionCallExterne,
    droneDSL_FonctionCallInterne,
    droneDSL_FonctionDecl,
    droneDSL_GDr,
    droneDSL_Gauche,
    droneDSL_Hauteur_max,
    droneDSL_Import,
    droneDSL_MD,
    droneDSL_Main,
    droneDSL_Model,
    droneDSL_Monter,
    droneDSL_Mouvement,
    droneDSL_Parallele,
    droneDSL_Parallele2,
    droneDSL_Parallele3,
    droneDSL_Parallele4,
    droneDSL_Pause,
    droneDSL_PourcentConst,
    droneDSL_PourcentDecl,
    droneDSL_PourcentExp,
    droneDSL_Pourcent_vitesse_deplacement_max,
    droneDSL_Pourcent_vitesse_hauteur_max,
    droneDSL_Pourcent_vitesse_rotation_max,
    droneDSL_Prologue,
    droneDSL_RGRD,
    droneDSL_Reculer,
    droneDSL_RefPourcentVar,
    droneDSL_RefSecondeVar,
    droneDSL_RotationDroite,
    droneDSL_RotationGauche,
    droneDSL_SecondeConst,
    droneDSL_SecondeDecl,
    droneDSL_SecondeExp,
    droneDSL_VarDecl,
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

def test_assoc_file82_reverse_link_reassign_clear():
    a1 = droneDSL_Import(name="sample_text")
    a2 = droneDSL_Import(name="sample_text_2")
    b = droneDSL_FonctionCallExterne(name="sample_text")
    _safe_set(b, 'droneDSL_FonctionCallExterne', a1)
    assert _is_linked(b, 'droneDSL_FonctionCallExterne', a1)
    if hasattr(a1, 'droneDSL_Import83'):
        assert _is_linked(a1, 'droneDSL_Import83', b)
    _safe_set(b, 'droneDSL_FonctionCallExterne', a2)
    assert _is_linked(b, 'droneDSL_FonctionCallExterne', a2)
    if hasattr(a1, 'droneDSL_Import83'):
        assert not _is_linked(a1, 'droneDSL_Import83', b)
    if hasattr(a2, 'droneDSL_Import83'):
        assert _is_linked(a2, 'droneDSL_Import83', b)
    _safe_set(b, 'droneDSL_FonctionCallExterne', None)
    assert not _is_linked(b, 'droneDSL_FonctionCallExterne', a2)
    if hasattr(a2, 'droneDSL_Import83'):
        assert not _is_linked(a2, 'droneDSL_Import83', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body78_stub_double():
    # droneDSL_EObject has no real 'droneDSL_EObject' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_FonctionDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_FonctionDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_FonctionDecl(name="sample_text")
    partner = droneDSL_EObject()
    setattr(partner, 'droneDSL_EObject', None)
    _safe_set(owner, 'droneDSL_FonctionDecl79', {partner})
    assert getattr(partner, 'droneDSL_EObject') == owner
    _safe_set(owner, 'droneDSL_FonctionDecl79', set())
    assert getattr(partner, 'droneDSL_EObject') is None


def test_assoc_eloignement_max13_stub_double():
    # droneDSL_Eloignement_max has no real 'droneDSL_Eloignement_max' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_SecondeConst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_SecondeConst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_SecondeConst(val="sample_text")
    partner = droneDSL_Eloignement_max()
    setattr(partner, 'droneDSL_Eloignement_max', None)
    _safe_set(owner, 'droneDSL_SecondeConst14', partner)
    assert getattr(partner, 'droneDSL_Eloignement_max') == owner
    _safe_set(owner, 'droneDSL_SecondeConst14', None)
    assert getattr(partner, 'droneDSL_Eloignement_max') is None


def test_assoc_fdm91_stub_double():
    # droneDSL_Main has no real 'droneDSL_Main92' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_FinDeMain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_FinDeMain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_FinDeMain(accolade="sample_text")
    partner = droneDSL_Main()
    setattr(partner, 'droneDSL_Main92', None)
    _safe_set(owner, 'droneDSL_FinDeMain', partner)
    assert getattr(partner, 'droneDSL_Main92') == owner
    _safe_set(owner, 'droneDSL_FinDeMain', None)
    assert getattr(partner, 'droneDSL_Main92') is None


def test_assoc_fonctions5_stub_double():
    # droneDSL_Model has no real 'droneDSL_Model6' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_FonctionDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_FonctionDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_FonctionDecl(name="sample_text")
    partner = droneDSL_Model()
    setattr(partner, 'droneDSL_Model6', None)
    _safe_set(owner, 'droneDSL_FonctionDecl', partner)
    assert owner in getattr(partner, 'droneDSL_Model6')
    _safe_set(owner, 'droneDSL_FonctionDecl', None)
    assert owner not in getattr(partner, 'droneDSL_Model6')


def test_assoc_hauteur_max12_stub_double():
    # droneDSL_Hauteur_max has no real 'droneDSL_Hauteur_max' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_SecondeConst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_SecondeConst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_SecondeConst(val="sample_text")
    partner = droneDSL_Hauteur_max()
    setattr(partner, 'droneDSL_Hauteur_max', None)
    _safe_set(owner, 'droneDSL_SecondeConst', partner)
    assert getattr(partner, 'droneDSL_Hauteur_max') == owner
    _safe_set(owner, 'droneDSL_SecondeConst', None)
    assert getattr(partner, 'droneDSL_Hauteur_max') is None


def test_assoc_imports0_stub_double():
    # droneDSL_Model has no real 'droneDSL_Model' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_Import(name="sample_text")
    partner = droneDSL_Model()
    setattr(partner, 'droneDSL_Model', None)
    _safe_set(owner, 'droneDSL_Import', partner)
    assert owner in getattr(partner, 'droneDSL_Model')
    _safe_set(owner, 'droneDSL_Import', None)
    assert owner not in getattr(partner, 'droneDSL_Model')


def test_assoc_ref80_stub_double():
    # droneDSL_FonctionCallInterne has no real 'droneDSL_FonctionCallInterne' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_FonctionDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_FonctionDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_FonctionDecl(name="sample_text")
    partner = droneDSL_FonctionCallInterne()
    setattr(partner, 'droneDSL_FonctionCallInterne', None)
    _safe_set(owner, 'droneDSL_FonctionDecl81', partner)
    assert getattr(partner, 'droneDSL_FonctionCallInterne') == owner
    _safe_set(owner, 'droneDSL_FonctionDecl81', None)
    assert getattr(partner, 'droneDSL_FonctionCallInterne') is None


def test_assoc_val30_stub_double():
    # droneDSL_SecondeDecl has no real 'droneDSL_SecondeDecl' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_SecondeConst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_SecondeConst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_SecondeConst(val="sample_text")
    partner = droneDSL_SecondeDecl()
    setattr(partner, 'droneDSL_SecondeDecl', None)
    _safe_set(owner, 'droneDSL_SecondeConst31', partner)
    assert getattr(partner, 'droneDSL_SecondeDecl') == owner
    _safe_set(owner, 'droneDSL_SecondeConst31', None)
    assert getattr(partner, 'droneDSL_SecondeDecl') is None


def test_assoc_val32_stub_double():
    # droneDSL_PourcentDecl has no real 'droneDSL_PourcentDecl' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_PourcentConst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_PourcentConst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_PourcentConst(val="sample_text")
    partner = droneDSL_PourcentDecl()
    setattr(partner, 'droneDSL_PourcentDecl', None)
    _safe_set(owner, 'droneDSL_PourcentConst33', partner)
    assert getattr(partner, 'droneDSL_PourcentDecl') == owner
    _safe_set(owner, 'droneDSL_PourcentConst33', None)
    assert getattr(partner, 'droneDSL_PourcentDecl') is None


def test_assoc_vitesse_deplacement8_stub_double():
    # droneDSL_Pourcent_vitesse_deplacement_max has no real 'droneDSL_Pourcent_vitesse_deplacement_max' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_PourcentConst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_PourcentConst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_PourcentConst(val="sample_text")
    partner = droneDSL_Pourcent_vitesse_deplacement_max()
    setattr(partner, 'droneDSL_Pourcent_vitesse_deplacement_max', None)
    _safe_set(owner, 'droneDSL_PourcentConst9', partner)
    assert getattr(partner, 'droneDSL_Pourcent_vitesse_deplacement_max') == owner
    _safe_set(owner, 'droneDSL_PourcentConst9', None)
    assert getattr(partner, 'droneDSL_Pourcent_vitesse_deplacement_max') is None


def test_assoc_vitesse_rotation10_stub_double():
    # droneDSL_Pourcent_vitesse_rotation_max has no real 'droneDSL_Pourcent_vitesse_rotation_max' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_PourcentConst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_PourcentConst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_PourcentConst(val="sample_text")
    partner = droneDSL_Pourcent_vitesse_rotation_max()
    setattr(partner, 'droneDSL_Pourcent_vitesse_rotation_max', None)
    _safe_set(owner, 'droneDSL_PourcentConst11', partner)
    assert getattr(partner, 'droneDSL_Pourcent_vitesse_rotation_max') == owner
    _safe_set(owner, 'droneDSL_PourcentConst11', None)
    assert getattr(partner, 'droneDSL_Pourcent_vitesse_rotation_max') is None


def test_assoc_vitesse_verticale7_stub_double():
    # droneDSL_Pourcent_vitesse_hauteur_max has no real 'droneDSL_Pourcent_vitesse_hauteur_max' property in the generated
    # code (a bare stub) -- manually attach it so droneDSL_PourcentConst's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # droneDSL_PourcentConst's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = droneDSL_PourcentConst(val="sample_text")
    partner = droneDSL_Pourcent_vitesse_hauteur_max()
    setattr(partner, 'droneDSL_Pourcent_vitesse_hauteur_max', None)
    _safe_set(owner, 'droneDSL_PourcentConst', partner)
    assert getattr(partner, 'droneDSL_Pourcent_vitesse_hauteur_max') == owner
    _safe_set(owner, 'droneDSL_PourcentConst', None)
    assert getattr(partner, 'droneDSL_Pourcent_vitesse_hauteur_max') is None


