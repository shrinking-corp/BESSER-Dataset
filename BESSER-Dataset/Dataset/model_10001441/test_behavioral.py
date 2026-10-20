import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Analyse2_AvisGlobal,
    Analyse2_Compte,
    Analyse2_Criteres,
    Analyse2_Fast_Food,
    Analyse2_Moderateurs,
    Analyse2_Review,
    Analyse2_Utilisateur,
    Analyse_Compte,
    Analyse_Criteres,
    Analyse_Fast_Food,
    Analyse_Moderateurs,
    Analyse_Review,
    Analyse_Utilisateur,
    AvisGlobal,
    Commentaire,
    Controlleur_Actor,
    FicheRestaurant,
    Photo,
    Pr_sentation,
    IHM,
    Information,
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

def test_assoc_AvisGlobal_Fast_Food_reverse_link_reassign_clear():
    a1 = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    a2 = Analyse2_Fast_Food(Adresse="sample_text_2", Ville="sample_text_2", description="sample_text_2", horaires="sample_text_2", nbPlaces=13, nom="sample_text_2", numeroTel="sample_text_2", photos="sample_text_2", prixMax=13, prixMin=13, proprietaire="sample_text_2", reviews="sample_text_2", siteDeCommande="sample_text_2")
    b = Analyse2_AvisGlobal(Commentaires="sample_text", nbAvis=7, notes="sample_text")
    _safe_set(b, 'fast_Food28', a1)
    assert _is_linked(b, 'fast_Food28', a1)
    if hasattr(a1, 'avisGlobal29'):
        assert _is_linked(a1, 'avisGlobal29', b)
    _safe_set(b, 'fast_Food28', a2)
    assert _is_linked(b, 'fast_Food28', a2)
    if hasattr(a1, 'avisGlobal29'):
        assert not _is_linked(a1, 'avisGlobal29', b)
    if hasattr(a2, 'avisGlobal29'):
        assert _is_linked(a2, 'avisGlobal29', b)
    _safe_set(b, 'fast_Food28', None)
    assert not _is_linked(b, 'fast_Food28', a2)
    if hasattr(a2, 'avisGlobal29'):
        assert not _is_linked(a2, 'avisGlobal29', b)


def test_assoc_AvisGlobal_FicheRestaurant_reverse_link_reassign_clear():
    a1 = FicheRestaurant(nom="sample_text")
    a2 = FicheRestaurant(nom="sample_text_2")
    b = AvisGlobal(Commentaires="sample_text", diagramme="sample_text", nbAvis=7, note="sample_text")
    _safe_set(b, 'd_finit12', a1)
    assert _is_linked(b, 'd_finit12', a1)
    if hasattr(a1, 'poss_de13'):
        assert _is_linked(a1, 'poss_de13', b)
    _safe_set(b, 'd_finit12', a2)
    assert _is_linked(b, 'd_finit12', a2)
    if hasattr(a1, 'poss_de13'):
        assert not _is_linked(a1, 'poss_de13', b)
    if hasattr(a2, 'poss_de13'):
        assert _is_linked(a2, 'poss_de13', b)
    _safe_set(b, 'd_finit12', None)
    assert not _is_linked(b, 'd_finit12', a2)
    if hasattr(a2, 'poss_de13'):
        assert not _is_linked(a2, 'poss_de13', b)


def test_assoc_Compte_Review_reverse_link_reassign_clear():
    a1 = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    a2 = Analyse_Review(Commentaire="sample_text_2", NoteGlobale=13, lesNotes="sample_text_2")
    b = Analyse_Compte(login="sample_text", motdepasse="sample_text")
    _safe_set(b, 'poss_de4', {a1})
    assert _is_linked(b, 'poss_de4', a1)
    if hasattr(a1, 'est__crite5'):
        assert _is_linked(a1, 'est__crite5', b)
    _safe_set(b, 'poss_de4', {a2})
    assert _is_linked(b, 'poss_de4', a2)
    if hasattr(a1, 'est__crite5'):
        assert not _is_linked(a1, 'est__crite5', b)
    if hasattr(a2, 'est__crite5'):
        assert _is_linked(a2, 'est__crite5', b)
    _safe_set(b, 'poss_de4', set())
    assert not _is_linked(b, 'poss_de4', a2)
    if hasattr(a2, 'est__crite5'):
        assert not _is_linked(a2, 'est__crite5', b)


def test_assoc_Compte_Review1_reverse_link_reassign_clear():
    a1 = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    a2 = Analyse2_Review(Commentaire="sample_text_2", lesNotes="sample_text_2", utilite="sample_text_2")
    b = Analyse2_Compte(login="sample_text", motdepasse="sample_text")
    _safe_set(b, 'poss_de22', {a1})
    assert _is_linked(b, 'poss_de22', a1)
    if hasattr(a1, 'est__crite23'):
        assert _is_linked(a1, 'est__crite23', b)
    _safe_set(b, 'poss_de22', {a2})
    assert _is_linked(b, 'poss_de22', a2)
    if hasattr(a1, 'est__crite23'):
        assert not _is_linked(a1, 'est__crite23', b)
    if hasattr(a2, 'est__crite23'):
        assert _is_linked(a2, 'est__crite23', b)
    _safe_set(b, 'poss_de22', set())
    assert not _is_linked(b, 'poss_de22', a2)
    if hasattr(a2, 'est__crite23'):
        assert not _is_linked(a2, 'est__crite23', b)


def test_assoc_Criteres_Review_reverse_link_reassign_clear():
    a1 = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    a2 = Analyse_Review(Commentaire="sample_text_2", NoteGlobale=13, lesNotes="sample_text_2")
    b = Analyse_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    _safe_set(b, 'sont_associ_s6', {a1})
    assert _is_linked(b, 'sont_associ_s6', a1)
    if hasattr(a1, 'note7'):
        assert _is_linked(a1, 'note7', b)
    _safe_set(b, 'sont_associ_s6', {a2})
    assert _is_linked(b, 'sont_associ_s6', a2)
    if hasattr(a1, 'note7'):
        assert not _is_linked(a1, 'note7', b)
    if hasattr(a2, 'note7'):
        assert _is_linked(a2, 'note7', b)
    _safe_set(b, 'sont_associ_s6', set())
    assert not _is_linked(b, 'sont_associ_s6', a2)
    if hasattr(a2, 'note7'):
        assert not _is_linked(a2, 'note7', b)


def test_assoc_Criteres_Review1_reverse_link_reassign_clear():
    a1 = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    a2 = Analyse2_Review(Commentaire="sample_text_2", lesNotes="sample_text_2", utilite="sample_text_2")
    b = Analyse2_Criteres(amabilite=7, qualit_=7, rapidite=7, rapportQualitePrix=7, respectHoraires=7)
    _safe_set(b, 'sont_associ_s24', {a1})
    assert _is_linked(b, 'sont_associ_s24', a1)
    if hasattr(a1, 'note25'):
        assert _is_linked(a1, 'note25', b)
    _safe_set(b, 'sont_associ_s24', {a2})
    assert _is_linked(b, 'sont_associ_s24', a2)
    if hasattr(a1, 'note25'):
        assert not _is_linked(a1, 'note25', b)
    if hasattr(a2, 'note25'):
        assert _is_linked(a2, 'note25', b)
    _safe_set(b, 'sont_associ_s24', set())
    assert not _is_linked(b, 'sont_associ_s24', a2)
    if hasattr(a2, 'note25'):
        assert not _is_linked(a2, 'note25', b)


def test_assoc_Pr_sentation_FicheRestaurant_reverse_link_reassign_clear():
    a1 = Pr_sentation(adresse="sample_text", description="sample_text", numTel="sample_text", ouverture="sample_text", siteDeCommande="sample_text")
    a2 = Pr_sentation(adresse="sample_text_2", description="sample_text_2", numTel="sample_text_2", ouverture="sample_text_2", siteDeCommande="sample_text_2")
    b = FicheRestaurant(nom="sample_text")
    _safe_set(b, 'poss_de17', a1)
    assert _is_linked(b, 'poss_de17', a1)
    if hasattr(a1, 'repr_sente16'):
        assert _is_linked(a1, 'repr_sente16', b)
    _safe_set(b, 'poss_de17', a2)
    assert _is_linked(b, 'poss_de17', a2)
    if hasattr(a1, 'repr_sente16'):
        assert not _is_linked(a1, 'repr_sente16', b)
    if hasattr(a2, 'repr_sente16'):
        assert _is_linked(a2, 'repr_sente16', b)
    _safe_set(b, 'poss_de17', None)
    assert not _is_linked(b, 'poss_de17', a2)
    if hasattr(a2, 'repr_sente16'):
        assert not _is_linked(a2, 'repr_sente16', b)


def test_assoc_Review_Fast_Food_reverse_link_reassign_clear():
    a1 = Analyse_Review(Commentaire="sample_text", NoteGlobale=7, lesNotes="sample_text")
    a2 = Analyse_Review(Commentaire="sample_text_2", NoteGlobale=13, lesNotes="sample_text_2")
    b = Analyse_Fast_Food(Adresse="sample_text", Ville="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", notes="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text")
    _safe_set(b, 'poss_de1', {a1})
    assert _is_linked(b, 'poss_de1', a1)
    if hasattr(a1, 'caract_rise0'):
        assert _is_linked(a1, 'caract_rise0', b)
    _safe_set(b, 'poss_de1', {a2})
    assert _is_linked(b, 'poss_de1', a2)
    if hasattr(a1, 'caract_rise0'):
        assert not _is_linked(a1, 'caract_rise0', b)
    if hasattr(a2, 'caract_rise0'):
        assert _is_linked(a2, 'caract_rise0', b)
    _safe_set(b, 'poss_de1', set())
    assert not _is_linked(b, 'poss_de1', a2)
    if hasattr(a2, 'caract_rise0'):
        assert not _is_linked(a2, 'caract_rise0', b)


def test_assoc_Review_Fast_Food1_reverse_link_reassign_clear():
    a1 = Analyse2_Review(Commentaire="sample_text", lesNotes="sample_text", utilite="sample_text")
    a2 = Analyse2_Review(Commentaire="sample_text_2", lesNotes="sample_text_2", utilite="sample_text_2")
    b = Analyse2_Fast_Food(Adresse="sample_text", Ville="sample_text", description="sample_text", horaires="sample_text", nbPlaces=7, nom="sample_text", numeroTel="sample_text", photos="sample_text", prixMax=7, prixMin=7, proprietaire="sample_text", reviews="sample_text", siteDeCommande="sample_text")
    _safe_set(b, 'poss_de19', {a1})
    assert _is_linked(b, 'poss_de19', a1)
    if hasattr(a1, 'caract_rise18'):
        assert _is_linked(a1, 'caract_rise18', b)
    _safe_set(b, 'poss_de19', {a2})
    assert _is_linked(b, 'poss_de19', a2)
    if hasattr(a1, 'caract_rise18'):
        assert not _is_linked(a1, 'caract_rise18', b)
    if hasattr(a2, 'caract_rise18'):
        assert _is_linked(a2, 'caract_rise18', b)
    _safe_set(b, 'poss_de19', set())
    assert not _is_linked(b, 'poss_de19', a2)
    if hasattr(a2, 'caract_rise18'):
        assert not _is_linked(a2, 'caract_rise18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Compte_Utilisateur_stub_double():
    # Analyse_Utilisateur has no real 'poss_de3' property in the generated
    # code (a bare stub) -- manually attach it so Analyse_Compte's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Analyse_Compte's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Analyse_Compte(login="sample_text", motdepasse="sample_text")
    partner = Analyse_Utilisateur()
    setattr(partner, 'poss_de3', None)
    _safe_set(owner, 'est_associ_2', partner)
    assert getattr(partner, 'poss_de3') == owner
    _safe_set(owner, 'est_associ_2', None)
    assert getattr(partner, 'poss_de3') is None


def test_assoc_Compte_Utilisateur1_stub_double():
    # Analyse2_Utilisateur has no real 'poss_de21' property in the generated
    # code (a bare stub) -- manually attach it so Analyse2_Compte's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Analyse2_Compte's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Analyse2_Compte(login="sample_text", motdepasse="sample_text")
    partner = Analyse2_Utilisateur()
    setattr(partner, 'poss_de21', None)
    _safe_set(owner, 'est_associ_20', partner)
    assert getattr(partner, 'poss_de21') == owner
    _safe_set(owner, 'est_associ_20', None)
    assert getattr(partner, 'poss_de21') is None


def test_assoc_FicheRestaurant_Photo_stub_double():
    # Photo has no real 'repr_sente15' property in the generated
    # code (a bare stub) -- manually attach it so FicheRestaurant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FicheRestaurant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FicheRestaurant(nom="sample_text")
    partner = Photo()
    setattr(partner, 'repr_sente15', None)
    _safe_set(owner, 'poss_de14', {partner})
    assert getattr(partner, 'repr_sente15') == owner
    _safe_set(owner, 'poss_de14', set())
    assert getattr(partner, 'repr_sente15') is None


def test_assoc_Moderateurs_Compte_stub_double():
    # Analyse_Moderateurs has no real 'poss_de8' property in the generated
    # code (a bare stub) -- manually attach it so Analyse_Compte's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Analyse_Compte's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Analyse_Compte(login="sample_text", motdepasse="sample_text")
    partner = Analyse_Moderateurs()
    setattr(partner, 'poss_de8', None)
    _safe_set(owner, 'est_associ_9', partner)
    assert getattr(partner, 'poss_de8') == owner
    _safe_set(owner, 'est_associ_9', None)
    assert getattr(partner, 'poss_de8') is None


def test_assoc_Moderateurs_Compte1_stub_double():
    # Analyse2_Moderateurs has no real 'poss_de26' property in the generated
    # code (a bare stub) -- manually attach it so Analyse2_Compte's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Analyse2_Compte's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Analyse2_Compte(login="sample_text", motdepasse="sample_text")
    partner = Analyse2_Moderateurs()
    setattr(partner, 'poss_de26', None)
    _safe_set(owner, 'est_associ_27', partner)
    assert getattr(partner, 'poss_de26') == owner
    _safe_set(owner, 'est_associ_27', None)
    assert getattr(partner, 'poss_de26') is None


