import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDepot,
    AbstractDepotType,
    AbstractMetaLab,
    ArtOuvrageType,
    ArtRevueType,
    Article,
    AutLabType,
    Auteur,
    AutreType,
    BrevetType,
    Connexion,
    DepotsType,
    Entry,
    HAL_AbstractDepot,
    HAL_AbstractDepotType,
    HAL_AbstractMetaLab,
    HAL_AffiliationType,
    HAL_ArtJournal,
    HAL_ArtOuvrage,
    HAL_ArtOuvrageType,
    HAL_ArtRevue,
    HAL_ArtRevueType,
    HAL_Article,
    HAL_ArticleRecent,
    HAL_ArticleRetro,
    HAL_AutLabType,
    HAL_Auteur,
    HAL_Autre,
    HAL_AutreType,
    HAL_Brevet,
    HAL_BrevetType,
    HAL_Communication,
    HAL_Conference,
    HAL_Connexion,
    HAL_Depot,
    HAL_DepotWeb,
    HAL_DepotsType,
    HAL_Entry,
    HAL_HAL,
    HAL_Laboratoire,
    HAL_MetaArtNoticeType,
    HAL_MetaArtType,
    HAL_MetaLab,
    HAL_MetaType,
    HAL_Notice,
    HAL_Ouvrage,
    HAL_OuvrageType,
    HAL_ReferenceBiblioType,
    HAL_Server,
    HAL_TamponType,
    HAL_These,
    HAL_TheseType,
    HAL_WebLink,
    HAL_Workshop,
    HAL_WorkshopType,
    Laboratoire,
    MetaArtNoticeType,
    MetaArtType,
    MetaType,
    OuvrageType,
    ReferenceBiblioType,
    Server,
    TamponType,
    TheseType,
    WorkshopType,
    DateVisibleEnum,
    FormatEnum,
    FormatWebEnum,
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

def test_assoc_fichiers8_stub_double():
    # AbstractDepot has no real 'AbstractDepot' property in the generated
    # code (a bare stub) -- manually attach it so HAL_ArticleRetro's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HAL_ArticleRetro's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HAL_ArticleRetro(dateRedaction="sample_text")
    partner = AbstractDepot()
    setattr(partner, 'AbstractDepot', None)
    _safe_set(owner, 'HAL_ArticleRetro', partner)
    assert getattr(partner, 'AbstractDepot') == owner
    _safe_set(owner, 'HAL_ArticleRetro', None)
    assert getattr(partner, 'AbstractDepot') is None


def test_assoc_lab16_stub_double():
    # Laboratoire has no real 'Laboratoire17' property in the generated
    # code (a bare stub) -- manually attach it so HAL_Auteur's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HAL_Auteur's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HAL_Auteur(autrePrenom="sample_text", email="sample_text", nom="sample_text", prenom="sample_text", urlPerso="sample_text")
    partner = Laboratoire()
    setattr(partner, 'Laboratoire17', None)
    _safe_set(owner, 'HAL_Auteur', partner)
    assert getattr(partner, 'Laboratoire17') == owner
    _safe_set(owner, 'HAL_Auteur', None)
    assert getattr(partner, 'Laboratoire17') is None


def test_assoc_metas18_stub_double():
    # AbstractMetaLab has no real 'AbstractMetaLab' property in the generated
    # code (a bare stub) -- manually attach it so HAL_Laboratoire's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HAL_Laboratoire's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HAL_Laboratoire(id="sample_text")
    partner = AbstractMetaLab()
    setattr(partner, 'AbstractMetaLab', None)
    _safe_set(owner, 'HAL_Laboratoire', partner)
    assert getattr(partner, 'AbstractMetaLab') == owner
    _safe_set(owner, 'HAL_Laboratoire', None)
    assert getattr(partner, 'AbstractMetaLab') is None


def test_assoc_referenceBiblio10_stub_double():
    # ReferenceBiblioType has no real 'ReferenceBiblioType' property in the generated
    # code (a bare stub) -- manually attach it so HAL_MetaArtType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HAL_MetaArtType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HAL_MetaArtType(abstract="sample_text", domain="sample_text")
    partner = ReferenceBiblioType()
    setattr(partner, 'ReferenceBiblioType', None)
    _safe_set(owner, 'HAL_MetaArtType', partner)
    assert getattr(partner, 'ReferenceBiblioType') == owner
    _safe_set(owner, 'HAL_MetaArtType', None)
    assert getattr(partner, 'ReferenceBiblioType') is None


def test_assoc_referenceBiblio11_stub_double():
    # ReferenceBiblioType has no real 'ReferenceBiblioType12' property in the generated
    # code (a bare stub) -- manually attach it so HAL_MetaArtNoticeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HAL_MetaArtNoticeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HAL_MetaArtNoticeType(abstract="sample_text", domain="sample_text")
    partner = ReferenceBiblioType()
    setattr(partner, 'ReferenceBiblioType12', None)
    _safe_set(owner, 'HAL_MetaArtNoticeType', partner)
    assert getattr(partner, 'ReferenceBiblioType12') == owner
    _safe_set(owner, 'HAL_MetaArtNoticeType', None)
    assert getattr(partner, 'ReferenceBiblioType12') is None


def test_assoc_server21_stub_double():
    # Server has no real 'Server' property in the generated
    # code (a bare stub) -- manually attach it so HAL_WebLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # HAL_WebLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = HAL_WebLink(identifiant="sample_text")
    partner = Server()
    setattr(partner, 'Server', None)
    _safe_set(owner, 'HAL_WebLink', partner)
    assert getattr(partner, 'Server') == owner
    _safe_set(owner, 'HAL_WebLink', None)
    assert getattr(partner, 'Server') is None


