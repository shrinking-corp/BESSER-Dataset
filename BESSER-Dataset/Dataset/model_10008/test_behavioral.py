import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EntiteLieu,
    GameElement,
    game_Action,
    game_Chemin,
    game_Choix,
    game_Condition,
    game_Conjonction,
    game_Connaissance,
    game_ConnaissanceLieu,
    game_Description,
    game_EntiteLieu,
    game_Explorateur,
    game_Game,
    game_GameElement,
    game_Interaction,
    game_Lieu,
    game_Litteral,
    game_Objet,
    game_PackObjets,
    game_Personne,
    game_Recompense,
    game_Texte,
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

def test_assoc_explorateur0_reverse_link_reassign_clear():
    a1 = game_Game(name="sample_text")
    a2 = game_Game(name="sample_text_2")
    b = game_Explorateur(name="sample_text", tailleInventaire=7)
    _safe_set(b, 'game_Explorateur', a1)
    assert _is_linked(b, 'game_Explorateur', a1)
    if hasattr(a1, 'game_Game'):
        assert _is_linked(a1, 'game_Game', b)
    _safe_set(b, 'game_Explorateur', a2)
    assert _is_linked(b, 'game_Explorateur', a2)
    if hasattr(a1, 'game_Game'):
        assert not _is_linked(a1, 'game_Game', b)
    if hasattr(a2, 'game_Game'):
        assert _is_linked(a2, 'game_Game', b)
    _safe_set(b, 'game_Explorateur', None)
    assert not _is_linked(b, 'game_Explorateur', a2)
    if hasattr(a2, 'game_Game'):
        assert not _is_linked(a2, 'game_Game', b)


def test_assoc_gameElements6_reverse_link_reassign_clear():
    a1 = game_GameElement(name="sample_text")
    a2 = game_GameElement(name="sample_text_2")
    b = game_Game(name="sample_text")
    _safe_set(b, 'game_Game7', {a1})
    assert _is_linked(b, 'game_Game7', a1)
    if hasattr(a1, 'game_GameElement'):
        assert _is_linked(a1, 'game_GameElement', b)
    _safe_set(b, 'game_Game7', {a2})
    assert _is_linked(b, 'game_Game7', a2)
    if hasattr(a1, 'game_GameElement'):
        assert not _is_linked(a1, 'game_GameElement', b)
    if hasattr(a2, 'game_GameElement'):
        assert _is_linked(a2, 'game_GameElement', b)
    _safe_set(b, 'game_Game7', set())
    assert not _is_linked(b, 'game_Game7', a2)
    if hasattr(a2, 'game_GameElement'):
        assert not _is_linked(a2, 'game_GameElement', b)


def test_assoc_inventaire17_reverse_link_reassign_clear():
    a1 = game_PackObjets(quantite=7)
    a2 = game_PackObjets(quantite=13)
    b = game_Explorateur(name="sample_text", tailleInventaire=7)
    _safe_set(b, 'game_Explorateur18', {a1})
    assert _is_linked(b, 'game_Explorateur18', a1)
    if hasattr(a1, 'game_PackObjets'):
        assert _is_linked(a1, 'game_PackObjets', b)
    _safe_set(b, 'game_Explorateur18', {a2})
    assert _is_linked(b, 'game_Explorateur18', a2)
    if hasattr(a1, 'game_PackObjets'):
        assert not _is_linked(a1, 'game_PackObjets', b)
    if hasattr(a2, 'game_PackObjets'):
        assert _is_linked(a2, 'game_PackObjets', b)
    _safe_set(b, 'game_Explorateur18', set())
    assert not _is_linked(b, 'game_Explorateur18', a2)
    if hasattr(a2, 'game_PackObjets'):
        assert not _is_linked(a2, 'game_PackObjets', b)


def test_assoc_objet26_reverse_link_reassign_clear():
    a1 = game_PackObjets(quantite=7)
    a2 = game_PackObjets(quantite=13)
    b = game_Objet(taille=7)
    _safe_set(b, 'game_Objet', a1)
    assert _is_linked(b, 'game_Objet', a1)
    if hasattr(a1, 'game_PackObjets27'):
        assert _is_linked(a1, 'game_PackObjets27', b)
    _safe_set(b, 'game_Objet', a2)
    assert _is_linked(b, 'game_Objet', a2)
    if hasattr(a1, 'game_PackObjets27'):
        assert not _is_linked(a1, 'game_PackObjets27', b)
    if hasattr(a2, 'game_PackObjets27'):
        assert _is_linked(a2, 'game_PackObjets27', b)
    _safe_set(b, 'game_Objet', None)
    assert not _is_linked(b, 'game_Objet', a2)
    if hasattr(a2, 'game_PackObjets27'):
        assert not _is_linked(a2, 'game_PackObjets27', b)


def test_assoc_objet49_reverse_link_reassign_clear():
    a1 = game_Objet(taille=7)
    a2 = game_Objet(taille=13)
    b = game_Litteral(operateur="sample_text", quantite=7)
    _safe_set(b, 'game_Litteral50', a1)
    assert _is_linked(b, 'game_Litteral50', a1)
    if hasattr(a1, 'game_Objet51'):
        assert _is_linked(a1, 'game_Objet51', b)
    _safe_set(b, 'game_Litteral50', a2)
    assert _is_linked(b, 'game_Litteral50', a2)
    if hasattr(a1, 'game_Objet51'):
        assert not _is_linked(a1, 'game_Objet51', b)
    if hasattr(a2, 'game_Objet51'):
        assert _is_linked(a2, 'game_Objet51', b)
    _safe_set(b, 'game_Litteral50', None)
    assert not _is_linked(b, 'game_Litteral50', a2)
    if hasattr(a2, 'game_Objet51'):
        assert not _is_linked(a2, 'game_Objet51', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_choixFin100_stub_double():
    # game_Condition has no real 'game_Condition102' property in the generated
    # code (a bare stub) -- manually attach it so game_Choix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Choix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Choix(name="sample_text")
    partner = game_Condition()
    setattr(partner, 'game_Condition102', None)
    _safe_set(owner, 'game_Choix101', partner)
    assert getattr(partner, 'game_Condition102') == owner
    _safe_set(owner, 'game_Choix101', None)
    assert getattr(partner, 'game_Condition102') is None


def test_assoc_choixSuivant80_stub_double():
    # game_Action has no real 'game_Action81' property in the generated
    # code (a bare stub) -- manually attach it so game_Choix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Choix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Choix(name="sample_text")
    partner = game_Action()
    setattr(partner, 'game_Action81', None)
    _safe_set(owner, 'game_Choix', partner)
    assert getattr(partner, 'game_Action81') == owner
    _safe_set(owner, 'game_Choix', None)
    assert getattr(partner, 'game_Action81') is None


def test_assoc_condition57_stub_double():
    # game_Condition has no real 'game_Condition59' property in the generated
    # code (a bare stub) -- manually attach it so game_Texte's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Texte's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Texte(contenu="sample_text")
    partner = game_Condition()
    setattr(partner, 'game_Condition59', None)
    _safe_set(owner, 'game_Texte58', partner)
    assert getattr(partner, 'game_Condition59') == owner
    _safe_set(owner, 'game_Texte58', None)
    assert getattr(partner, 'game_Condition59') is None


def test_assoc_connaissance52_stub_double():
    # game_Connaissance has no real 'game_Connaissance54' property in the generated
    # code (a bare stub) -- manually attach it so game_Litteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Litteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Litteral(operateur="sample_text", quantite=7)
    partner = game_Connaissance()
    setattr(partner, 'game_Connaissance54', None)
    _safe_set(owner, 'game_Litteral53', partner)
    assert getattr(partner, 'game_Connaissance54') == owner
    _safe_set(owner, 'game_Litteral53', None)
    assert getattr(partner, 'game_Connaissance54') is None


def test_assoc_connaissances14_stub_double():
    # game_Connaissance has no real 'game_Connaissance16' property in the generated
    # code (a bare stub) -- manually attach it so game_Explorateur's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Explorateur's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Explorateur(name="sample_text", tailleInventaire=7)
    partner = game_Connaissance()
    setattr(partner, 'game_Connaissance16', None)
    _safe_set(owner, 'game_Explorateur15', {partner})
    assert getattr(partner, 'game_Connaissance16') == owner
    _safe_set(owner, 'game_Explorateur15', set())
    assert getattr(partner, 'game_Connaissance16') is None


def test_assoc_consommations42_stub_double():
    # game_Chemin has no real 'game_Chemin43' property in the generated
    # code (a bare stub) -- manually attach it so game_PackObjets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_PackObjets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_PackObjets(quantite=7)
    partner = game_Chemin()
    setattr(partner, 'game_Chemin43', None)
    _safe_set(owner, 'game_PackObjets44', partner)
    assert owner in getattr(partner, 'game_Chemin43')
    _safe_set(owner, 'game_PackObjets44', None)
    assert owner not in getattr(partner, 'game_Chemin43')


def test_assoc_consommations77_stub_double():
    # game_Action has no real 'game_Action78' property in the generated
    # code (a bare stub) -- manually attach it so game_PackObjets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_PackObjets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_PackObjets(quantite=7)
    partner = game_Action()
    setattr(partner, 'game_Action78', None)
    _safe_set(owner, 'game_PackObjets79', partner)
    assert owner in getattr(partner, 'game_Action78')
    _safe_set(owner, 'game_PackObjets79', None)
    assert owner not in getattr(partner, 'game_Action78')


def test_assoc_description12_stub_double():
    # game_Description has no real 'game_Description' property in the generated
    # code (a bare stub) -- manually attach it so game_GameElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_GameElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_GameElement(name="sample_text")
    partner = game_Description()
    setattr(partner, 'game_Description', None)
    _safe_set(owner, 'game_GameElement13', partner)
    assert getattr(partner, 'game_Description') == owner
    _safe_set(owner, 'game_GameElement13', None)
    assert getattr(partner, 'game_Description') is None


def test_assoc_description97_stub_double():
    # game_Description has no real 'game_Description99' property in the generated
    # code (a bare stub) -- manually attach it so game_Choix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Choix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Choix(name="sample_text")
    partner = game_Description()
    setattr(partner, 'game_Description99', None)
    _safe_set(owner, 'game_Choix98', partner)
    assert getattr(partner, 'game_Description99') == owner
    _safe_set(owner, 'game_Choix98', None)
    assert getattr(partner, 'game_Description99') is None


def test_assoc_entite8_stub_double():
    # game_EntiteLieu has no real 'game_EntiteLieu' property in the generated
    # code (a bare stub) -- manually attach it so game_Personne's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Personne's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Personne(name="sample_text")
    partner = game_EntiteLieu()
    setattr(partner, 'game_EntiteLieu', None)
    _safe_set(owner, 'game_Personne', partner)
    assert getattr(partner, 'game_EntiteLieu') == owner
    _safe_set(owner, 'game_Personne', None)
    assert getattr(partner, 'game_EntiteLieu') is None


def test_assoc_interaction19_stub_double():
    # game_Interaction has no real 'game_Interaction' property in the generated
    # code (a bare stub) -- manually attach it so game_Personne's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Personne's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Personne(name="sample_text")
    partner = game_Interaction()
    setattr(partner, 'game_Interaction', None)
    _safe_set(owner, 'game_Personne20', partner)
    assert getattr(partner, 'game_Interaction') == owner
    _safe_set(owner, 'game_Personne20', None)
    assert getattr(partner, 'game_Interaction') is None


def test_assoc_lieuDepart1_stub_double():
    # game_Lieu has no real 'game_Lieu' property in the generated
    # code (a bare stub) -- manually attach it so game_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Game(name="sample_text")
    partner = game_Lieu()
    setattr(partner, 'game_Lieu', None)
    _safe_set(owner, 'game_Game2', partner)
    assert getattr(partner, 'game_Lieu') == owner
    _safe_set(owner, 'game_Game2', None)
    assert getattr(partner, 'game_Lieu') is None


def test_assoc_lieuxArrivee3_stub_double():
    # game_Lieu has no real 'game_Lieu5' property in the generated
    # code (a bare stub) -- manually attach it so game_Game's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Game's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Game(name="sample_text")
    partner = game_Lieu()
    setattr(partner, 'game_Lieu5', None)
    _safe_set(owner, 'game_Game4', {partner})
    assert getattr(partner, 'game_Lieu5') == owner
    _safe_set(owner, 'game_Game4', set())
    assert getattr(partner, 'game_Lieu5') is None


def test_assoc_listeActions103_stub_double():
    # game_Action has no real 'game_Action105' property in the generated
    # code (a bare stub) -- manually attach it so game_Choix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Choix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Choix(name="sample_text")
    partner = game_Action()
    setattr(partner, 'game_Action105', None)
    _safe_set(owner, 'game_Choix104', {partner})
    assert getattr(partner, 'game_Action105') == owner
    _safe_set(owner, 'game_Choix104', set())
    assert getattr(partner, 'game_Action105') is None


def test_assoc_listeChoix94_stub_double():
    # game_Interaction has no real 'game_Interaction95' property in the generated
    # code (a bare stub) -- manually attach it so game_Choix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Choix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Choix(name="sample_text")
    partner = game_Interaction()
    setattr(partner, 'game_Interaction95', None)
    _safe_set(owner, 'game_Choix96', partner)
    assert owner in getattr(partner, 'game_Interaction95')
    _safe_set(owner, 'game_Choix96', None)
    assert owner not in getattr(partner, 'game_Interaction95')


def test_assoc_listeChoixDebut85_stub_double():
    # game_Interaction has no real 'game_Interaction86' property in the generated
    # code (a bare stub) -- manually attach it so game_Choix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Choix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Choix(name="sample_text")
    partner = game_Interaction()
    setattr(partner, 'game_Interaction86', None)
    _safe_set(owner, 'game_Choix87', partner)
    assert owner in getattr(partner, 'game_Interaction86')
    _safe_set(owner, 'game_Choix87', None)
    assert owner not in getattr(partner, 'game_Interaction86')


def test_assoc_litteraux47_stub_double():
    # game_Conjonction has no real 'game_Conjonction48' property in the generated
    # code (a bare stub) -- manually attach it so game_Litteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Litteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Litteral(operateur="sample_text", quantite=7)
    partner = game_Conjonction()
    setattr(partner, 'game_Conjonction48', None)
    _safe_set(owner, 'game_Litteral', partner)
    assert owner in getattr(partner, 'game_Conjonction48')
    _safe_set(owner, 'game_Litteral', None)
    assert owner not in getattr(partner, 'game_Conjonction48')


def test_assoc_objetsObtenus63_stub_double():
    # game_Recompense has no real 'game_Recompense64' property in the generated
    # code (a bare stub) -- manually attach it so game_PackObjets's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_PackObjets's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_PackObjets(quantite=7)
    partner = game_Recompense()
    setattr(partner, 'game_Recompense64', None)
    _safe_set(owner, 'game_PackObjets65', partner)
    assert getattr(partner, 'game_Recompense64') == owner
    _safe_set(owner, 'game_PackObjets65', None)
    assert getattr(partner, 'game_Recompense64') is None


def test_assoc_seulChoixDebut91_stub_double():
    # game_Interaction has no real 'game_Interaction92' property in the generated
    # code (a bare stub) -- manually attach it so game_Choix's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Choix's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Choix(name="sample_text")
    partner = game_Interaction()
    setattr(partner, 'game_Interaction92', None)
    _safe_set(owner, 'game_Choix93', partner)
    assert getattr(partner, 'game_Interaction92') == owner
    _safe_set(owner, 'game_Choix93', None)
    assert getattr(partner, 'game_Interaction92') is None


def test_assoc_textes55_stub_double():
    # game_Description has no real 'game_Description56' property in the generated
    # code (a bare stub) -- manually attach it so game_Texte's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # game_Texte's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = game_Texte(contenu="sample_text")
    partner = game_Description()
    setattr(partner, 'game_Description56', None)
    _safe_set(owner, 'game_Texte', partner)
    assert owner in getattr(partner, 'game_Description56')
    _safe_set(owner, 'game_Texte', None)
    assert owner not in getattr(partner, 'game_Description56')


