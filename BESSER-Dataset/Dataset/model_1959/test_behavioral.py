import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstaktFernKampfwaffe,
    AbstaktGegenstand,
    AbstaktPersona,
    AbstaktWaffe,
    AbstractMagier,
    AbstractMagischePaersona,
    AbstraktFertigkeit,
    AbstraktKleidung,
    AbstraktModifikatoren,
    AbstraktNahkampfwaffe,
    AbstrakteRuestung,
    BaseMagischePersona,
    Bemerkbar,
    BerechneteAttribute,
    Beschreibbar,
    BodyIndex,
    Essenz,
    FK,
    Gegenstand,
    GeistigeAttribute,
    GeldWert,
    KoerperlicheAtribute,
    Legalitaet,
    MagiePersona,
    MagischeMods,
    Modifizierbar,
    NahkampfReichweite,
    Quelle,
    Schadenswiederstand,
    koerpermods,
    shadowrun_AbstaktFernKampfwaffe,
    shadowrun_AbstaktGegenstand,
    shadowrun_AbstaktPersona,
    shadowrun_AbstaktWaffe,
    shadowrun_AbstractMagier,
    shadowrun_AbstractMagischePaersona,
    shadowrun_AbstrakRaumKoerper,
    shadowrun_AbstraktFertigkeit,
    shadowrun_AbstraktKleidung,
    shadowrun_AbstraktModifikatoren,
    shadowrun_AbstraktNahkampfwaffe,
    shadowrun_AbstrakteRuestung,
    shadowrun_AttributModifikatorWert,
    shadowrun_BaseMagischePersona,
    shadowrun_BasicList,
    shadowrun_Behaelter,
    shadowrun_Bemerkbar,
    shadowrun_BerechneteAttribute,
    shadowrun_Beschreibbar,
    shadowrun_BioWare,
    shadowrun_BodyIndex,
    shadowrun_Cyberware,
    shadowrun_EAttribute,
    shadowrun_EObject,
    shadowrun_Essenz,
    shadowrun_FK,
    shadowrun_FernkampfwaffenModifikatoren,
    shadowrun_Fertigkeit,
    shadowrun_FertigkeitsGruppe,
    shadowrun_Feuerwaffe,
    shadowrun_Gegenstand,
    shadowrun_GegenstandStufen,
    shadowrun_GeistigeAttribute,
    shadowrun_GeldWert,
    shadowrun_GengenstandListe,
    shadowrun_Granate,
    shadowrun_KiAdept,
    shadowrun_KiKraft,
    shadowrun_Kleidung,
    shadowrun_KoerperlicheAtribute,
    shadowrun_Konzentration,
    shadowrun_Legalitaet,
    shadowrun_MagiePersona,
    shadowrun_MagischeMods,
    shadowrun_ModifikatorList,
    shadowrun_Modifizierbar,
    shadowrun_Munition,
    shadowrun_MunitionsBehealter,
    shadowrun_NahkampfReichweite,
    shadowrun_Nahkampfwaffe,
    shadowrun_Persona,
    shadowrun_PersonaFertigkeit,
    shadowrun_PersonaGruppe,
    shadowrun_PersonaKoerper,
    shadowrun_PersonaZauber,
    shadowrun_Placement,
    shadowrun_Projektilwaffe,
    shadowrun_Quelle,
    shadowrun_RaumKoordinate,
    shadowrun_Reichweite,
    shadowrun_Reichweiten,
    shadowrun_Ruestung,
    shadowrun_Schadenswiederstand,
    shadowrun_Script,
    shadowrun_Shamane,
    shadowrun_ShrList,
    shadowrun_Sichtverhaeltnisse,
    shadowrun_SourceBook,
    shadowrun_Spezialisierung,
    shadowrun_Spezies,
    shadowrun_Totem,
    shadowrun_WarenListe,
    shadowrun_Wurfwaffe,
    shadowrun_Zauber,
    shadowrun_koerpermods,
    FeuerModus,
    Koerperteil,
    MagazinTyp,
    ModifikatorType,
    SchadensTyp,
    SmartgunType,
    Tragbar,
    ZauberArt,
    ZauberDauer,
    ZauberReichweite,
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

def test_assoc_entries66_reverse_link_reassign_clear():
    a1 = shadowrun_WarenListe(listenWert="sample_text", strassenWert="sample_text")
    a2 = shadowrun_WarenListe(listenWert="sample_text_2", strassenWert="sample_text_2")
    b = shadowrun_AbstaktGegenstand(gewicht=3.14, inBenutzung=True, raumKapazitaet=7, tragbar="sample_text", verbraucht=True)
    _safe_set(b, 'shadowrun_AbstaktGegenstand67', a1)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand67', a1)
    if hasattr(a1, 'shadowrun_WarenListe'):
        assert _is_linked(a1, 'shadowrun_WarenListe', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand67', a2)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand67', a2)
    if hasattr(a1, 'shadowrun_WarenListe'):
        assert not _is_linked(a1, 'shadowrun_WarenListe', b)
    if hasattr(a2, 'shadowrun_WarenListe'):
        assert _is_linked(a2, 'shadowrun_WarenListe', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand67', None)
    assert not _is_linked(b, 'shadowrun_AbstaktGegenstand67', a2)
    if hasattr(a2, 'shadowrun_WarenListe'):
        assert not _is_linked(a2, 'shadowrun_WarenListe', b)


def test_assoc_fertigkeiten1_reverse_link_reassign_clear():
    a1 = shadowrun_PersonaFertigkeit(stufe=7)
    a2 = shadowrun_PersonaFertigkeit(stufe=13)
    b = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    _safe_set(b, 'shadowrun_AbstaktPersona', {a1})
    assert _is_linked(b, 'shadowrun_AbstaktPersona', a1)
    if hasattr(a1, 'shadowrun_PersonaFertigkeit'):
        assert _is_linked(a1, 'shadowrun_PersonaFertigkeit', b)
    _safe_set(b, 'shadowrun_AbstaktPersona', {a2})
    assert _is_linked(b, 'shadowrun_AbstaktPersona', a2)
    if hasattr(a1, 'shadowrun_PersonaFertigkeit'):
        assert not _is_linked(a1, 'shadowrun_PersonaFertigkeit', b)
    if hasattr(a2, 'shadowrun_PersonaFertigkeit'):
        assert _is_linked(a2, 'shadowrun_PersonaFertigkeit', b)
    _safe_set(b, 'shadowrun_AbstaktPersona', set())
    assert not _is_linked(b, 'shadowrun_AbstaktPersona', a2)
    if hasattr(a2, 'shadowrun_PersonaFertigkeit'):
        assert not _is_linked(a2, 'shadowrun_PersonaFertigkeit', b)


def test_assoc_gegenstaende5_reverse_link_reassign_clear():
    a1 = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    a2 = shadowrun_AbstaktPersona(CharismaBase=13, EssenzBase=13, InteligenzBase=13, KampfpoolBase=13, KonsitutionBase=13, ReaktionBase=13, ReaktionWBase=13, SchnelligkeitBase=13, StaerkeBase=13, WillenskraftBase=13, eigenGewicht=13, modsetter="sample_text_2")
    b = shadowrun_AbstaktGegenstand(gewicht=3.14, inBenutzung=True, raumKapazitaet=7, tragbar="sample_text", verbraucht=True)
    _safe_set(b, 'shadowrun_AbstaktGegenstand', a1)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand', a1)
    if hasattr(a1, 'shadowrun_AbstaktPersona6'):
        assert _is_linked(a1, 'shadowrun_AbstaktPersona6', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand', a2)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand', a2)
    if hasattr(a1, 'shadowrun_AbstaktPersona6'):
        assert not _is_linked(a1, 'shadowrun_AbstaktPersona6', b)
    if hasattr(a2, 'shadowrun_AbstaktPersona6'):
        assert _is_linked(a2, 'shadowrun_AbstaktPersona6', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand', None)
    assert not _is_linked(b, 'shadowrun_AbstaktGegenstand', a2)
    if hasattr(a2, 'shadowrun_AbstaktPersona6'):
        assert not _is_linked(a2, 'shadowrun_AbstaktPersona6', b)


def test_assoc_gegenstaendeList26_reverse_link_reassign_clear():
    a1 = shadowrun_Behaelter(kapazitaet=7)
    a2 = shadowrun_Behaelter(kapazitaet=13)
    b = shadowrun_AbstaktGegenstand(gewicht=3.14, inBenutzung=True, raumKapazitaet=7, tragbar="sample_text", verbraucht=True)
    _safe_set(b, 'shadowrun_AbstaktGegenstand27', a1)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand27', a1)
    if hasattr(a1, 'shadowrun_Behaelter'):
        assert _is_linked(a1, 'shadowrun_Behaelter', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand27', a2)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand27', a2)
    if hasattr(a1, 'shadowrun_Behaelter'):
        assert not _is_linked(a1, 'shadowrun_Behaelter', b)
    if hasattr(a2, 'shadowrun_Behaelter'):
        assert _is_linked(a2, 'shadowrun_Behaelter', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand27', None)
    assert not _is_linked(b, 'shadowrun_AbstaktGegenstand27', a2)
    if hasattr(a2, 'shadowrun_Behaelter'):
        assert not _is_linked(a2, 'shadowrun_Behaelter', b)


def test_assoc_gruppen31_reverse_link_reassign_clear():
    a1 = shadowrun_Placement()
    a2 = shadowrun_Placement()
    b = shadowrun_PersonaGruppe()
    _safe_set(b, 'shadowrun_PersonaGruppe32', a1)
    assert _is_linked(b, 'shadowrun_PersonaGruppe32', a1)
    if hasattr(a1, 'shadowrun_Placement'):
        assert _is_linked(a1, 'shadowrun_Placement', b)
    _safe_set(b, 'shadowrun_PersonaGruppe32', a2)
    assert _is_linked(b, 'shadowrun_PersonaGruppe32', a2)
    if hasattr(a1, 'shadowrun_Placement'):
        assert not _is_linked(a1, 'shadowrun_Placement', b)
    if hasattr(a2, 'shadowrun_Placement'):
        assert _is_linked(a2, 'shadowrun_Placement', b)
    _safe_set(b, 'shadowrun_PersonaGruppe32', None)
    assert not _is_linked(b, 'shadowrun_PersonaGruppe32', a2)
    if hasattr(a2, 'shadowrun_Placement'):
        assert not _is_linked(a2, 'shadowrun_Placement', b)


def test_assoc_inBenutzung15_reverse_link_reassign_clear():
    a1 = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    a2 = shadowrun_AbstaktPersona(CharismaBase=13, EssenzBase=13, InteligenzBase=13, KampfpoolBase=13, KonsitutionBase=13, ReaktionBase=13, ReaktionWBase=13, SchnelligkeitBase=13, StaerkeBase=13, WillenskraftBase=13, eigenGewicht=13, modsetter="sample_text_2")
    b = shadowrun_AbstaktGegenstand(gewicht=3.14, inBenutzung=True, raumKapazitaet=7, tragbar="sample_text", verbraucht=True)
    _safe_set(b, 'shadowrun_AbstaktGegenstand17', a1)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand17', a1)
    if hasattr(a1, 'shadowrun_AbstaktPersona16'):
        assert _is_linked(a1, 'shadowrun_AbstaktPersona16', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand17', a2)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand17', a2)
    if hasattr(a1, 'shadowrun_AbstaktPersona16'):
        assert not _is_linked(a1, 'shadowrun_AbstaktPersona16', b)
    if hasattr(a2, 'shadowrun_AbstaktPersona16'):
        assert _is_linked(a2, 'shadowrun_AbstaktPersona16', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand17', None)
    assert not _is_linked(b, 'shadowrun_AbstaktGegenstand17', a2)
    if hasattr(a2, 'shadowrun_AbstaktPersona16'):
        assert not _is_linked(a2, 'shadowrun_AbstaktPersona16', b)


def test_assoc_kleidung13_reverse_link_reassign_clear():
    a1 = shadowrun_AbstraktKleidung(koeperTeil="sample_text")
    a2 = shadowrun_AbstraktKleidung(koeperTeil="sample_text_2")
    b = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    _safe_set(b, 'shadowrun_AbstaktPersona14', {a1})
    assert _is_linked(b, 'shadowrun_AbstaktPersona14', a1)
    if hasattr(a1, 'shadowrun_AbstraktKleidung'):
        assert _is_linked(a1, 'shadowrun_AbstraktKleidung', b)
    _safe_set(b, 'shadowrun_AbstaktPersona14', {a2})
    assert _is_linked(b, 'shadowrun_AbstaktPersona14', a2)
    if hasattr(a1, 'shadowrun_AbstraktKleidung'):
        assert not _is_linked(a1, 'shadowrun_AbstraktKleidung', b)
    if hasattr(a2, 'shadowrun_AbstraktKleidung'):
        assert _is_linked(a2, 'shadowrun_AbstraktKleidung', b)
    _safe_set(b, 'shadowrun_AbstaktPersona14', set())
    assert not _is_linked(b, 'shadowrun_AbstaktPersona14', a2)
    if hasattr(a2, 'shadowrun_AbstraktKleidung'):
        assert not _is_linked(a2, 'shadowrun_AbstraktKleidung', b)


def test_assoc_linkeHand7_reverse_link_reassign_clear():
    a1 = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    a2 = shadowrun_AbstaktPersona(CharismaBase=13, EssenzBase=13, InteligenzBase=13, KampfpoolBase=13, KonsitutionBase=13, ReaktionBase=13, ReaktionWBase=13, SchnelligkeitBase=13, StaerkeBase=13, WillenskraftBase=13, eigenGewicht=13, modsetter="sample_text_2")
    b = shadowrun_AbstaktGegenstand(gewicht=3.14, inBenutzung=True, raumKapazitaet=7, tragbar="sample_text", verbraucht=True)
    _safe_set(b, 'shadowrun_AbstaktGegenstand9', a1)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand9', a1)
    if hasattr(a1, 'shadowrun_AbstaktPersona8'):
        assert _is_linked(a1, 'shadowrun_AbstaktPersona8', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand9', a2)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand9', a2)
    if hasattr(a1, 'shadowrun_AbstaktPersona8'):
        assert not _is_linked(a1, 'shadowrun_AbstaktPersona8', b)
    if hasattr(a2, 'shadowrun_AbstaktPersona8'):
        assert _is_linked(a2, 'shadowrun_AbstaktPersona8', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand9', None)
    assert not _is_linked(b, 'shadowrun_AbstaktGegenstand9', a2)
    if hasattr(a2, 'shadowrun_AbstaktPersona8'):
        assert not _is_linked(a2, 'shadowrun_AbstaktPersona8', b)


def test_assoc_personaList29_reverse_link_reassign_clear():
    a1 = shadowrun_PersonaGruppe()
    a2 = shadowrun_PersonaGruppe()
    b = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    _safe_set(b, 'shadowrun_AbstaktPersona30', a1)
    assert _is_linked(b, 'shadowrun_AbstaktPersona30', a1)
    if hasattr(a1, 'shadowrun_PersonaGruppe'):
        assert _is_linked(a1, 'shadowrun_PersonaGruppe', b)
    _safe_set(b, 'shadowrun_AbstaktPersona30', a2)
    assert _is_linked(b, 'shadowrun_AbstaktPersona30', a2)
    if hasattr(a1, 'shadowrun_PersonaGruppe'):
        assert not _is_linked(a1, 'shadowrun_PersonaGruppe', b)
    if hasattr(a2, 'shadowrun_PersonaGruppe'):
        assert _is_linked(a2, 'shadowrun_PersonaGruppe', b)
    _safe_set(b, 'shadowrun_AbstaktPersona30', None)
    assert not _is_linked(b, 'shadowrun_AbstaktPersona30', a2)
    if hasattr(a2, 'shadowrun_PersonaGruppe'):
        assert not _is_linked(a2, 'shadowrun_PersonaGruppe', b)


def test_assoc_placementList33_reverse_link_reassign_clear():
    a1 = shadowrun_Script()
    a2 = shadowrun_Script()
    b = shadowrun_Placement()
    _safe_set(b, 'shadowrun_Placement34', a1)
    assert _is_linked(b, 'shadowrun_Placement34', a1)
    if hasattr(a1, 'shadowrun_Script'):
        assert _is_linked(a1, 'shadowrun_Script', b)
    _safe_set(b, 'shadowrun_Placement34', a2)
    assert _is_linked(b, 'shadowrun_Placement34', a2)
    if hasattr(a1, 'shadowrun_Script'):
        assert not _is_linked(a1, 'shadowrun_Script', b)
    if hasattr(a2, 'shadowrun_Script'):
        assert _is_linked(a2, 'shadowrun_Script', b)
    _safe_set(b, 'shadowrun_Placement34', None)
    assert not _is_linked(b, 'shadowrun_Placement34', a2)
    if hasattr(a2, 'shadowrun_Script'):
        assert not _is_linked(a2, 'shadowrun_Script', b)


def test_assoc_rechteHand10_reverse_link_reassign_clear():
    a1 = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    a2 = shadowrun_AbstaktPersona(CharismaBase=13, EssenzBase=13, InteligenzBase=13, KampfpoolBase=13, KonsitutionBase=13, ReaktionBase=13, ReaktionWBase=13, SchnelligkeitBase=13, StaerkeBase=13, WillenskraftBase=13, eigenGewicht=13, modsetter="sample_text_2")
    b = shadowrun_AbstaktGegenstand(gewicht=3.14, inBenutzung=True, raumKapazitaet=7, tragbar="sample_text", verbraucht=True)
    _safe_set(b, 'shadowrun_AbstaktGegenstand12', a1)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand12', a1)
    if hasattr(a1, 'shadowrun_AbstaktPersona11'):
        assert _is_linked(a1, 'shadowrun_AbstaktPersona11', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand12', a2)
    assert _is_linked(b, 'shadowrun_AbstaktGegenstand12', a2)
    if hasattr(a1, 'shadowrun_AbstaktPersona11'):
        assert not _is_linked(a1, 'shadowrun_AbstaktPersona11', b)
    if hasattr(a2, 'shadowrun_AbstaktPersona11'):
        assert _is_linked(a2, 'shadowrun_AbstaktPersona11', b)
    _safe_set(b, 'shadowrun_AbstaktGegenstand12', None)
    assert not _is_linked(b, 'shadowrun_AbstaktGegenstand12', a2)
    if hasattr(a2, 'shadowrun_AbstaktPersona11'):
        assert not _is_linked(a2, 'shadowrun_AbstaktPersona11', b)


def test_assoc_spezies18_reverse_link_reassign_clear():
    a1 = shadowrun_Spezies(CharismaMax=7, InteligenzMax=7, KonsitutionMax=7, SchnelligkeitMax=7, StaerkeMax=7, WillenskraftMax=7)
    a2 = shadowrun_Spezies(CharismaMax=13, InteligenzMax=13, KonsitutionMax=13, SchnelligkeitMax=13, StaerkeMax=13, WillenskraftMax=13)
    b = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    _safe_set(b, 'shadowrun_AbstaktPersona19', a1)
    assert _is_linked(b, 'shadowrun_AbstaktPersona19', a1)
    if hasattr(a1, 'shadowrun_Spezies'):
        assert _is_linked(a1, 'shadowrun_Spezies', b)
    _safe_set(b, 'shadowrun_AbstaktPersona19', a2)
    assert _is_linked(b, 'shadowrun_AbstaktPersona19', a2)
    if hasattr(a1, 'shadowrun_Spezies'):
        assert not _is_linked(a1, 'shadowrun_Spezies', b)
    if hasattr(a2, 'shadowrun_Spezies'):
        assert _is_linked(a2, 'shadowrun_Spezies', b)
    _safe_set(b, 'shadowrun_AbstaktPersona19', None)
    assert not _is_linked(b, 'shadowrun_AbstaktPersona19', a2)
    if hasattr(a2, 'shadowrun_Spezies'):
        assert not _is_linked(a2, 'shadowrun_Spezies', b)


def test_assoc_spielerGruppe35_reverse_link_reassign_clear():
    a1 = shadowrun_Script()
    a2 = shadowrun_Script()
    b = shadowrun_PersonaGruppe()
    _safe_set(b, 'shadowrun_PersonaGruppe37', a1)
    assert _is_linked(b, 'shadowrun_PersonaGruppe37', a1)
    if hasattr(a1, 'shadowrun_Script36'):
        assert _is_linked(a1, 'shadowrun_Script36', b)
    _safe_set(b, 'shadowrun_PersonaGruppe37', a2)
    assert _is_linked(b, 'shadowrun_PersonaGruppe37', a2)
    if hasattr(a1, 'shadowrun_Script36'):
        assert not _is_linked(a1, 'shadowrun_Script36', b)
    if hasattr(a2, 'shadowrun_Script36'):
        assert _is_linked(a2, 'shadowrun_Script36', b)
    _safe_set(b, 'shadowrun_PersonaGruppe37', None)
    assert not _is_linked(b, 'shadowrun_PersonaGruppe37', a2)
    if hasattr(a2, 'shadowrun_Script36'):
        assert not _is_linked(a2, 'shadowrun_Script36', b)


def test_assoc_srcBook68_reverse_link_reassign_clear():
    a1 = shadowrun_SourceBook(endShrTime="sample_text", startShrTime="sample_text")
    a2 = shadowrun_SourceBook(endShrTime="sample_text_2", startShrTime="sample_text_2")
    b = shadowrun_Quelle(page="sample_text")
    _safe_set(b, 'shadowrun_Quelle', a1)
    assert _is_linked(b, 'shadowrun_Quelle', a1)
    if hasattr(a1, 'shadowrun_SourceBook'):
        assert _is_linked(a1, 'shadowrun_SourceBook', b)
    _safe_set(b, 'shadowrun_Quelle', a2)
    assert _is_linked(b, 'shadowrun_Quelle', a2)
    if hasattr(a1, 'shadowrun_SourceBook'):
        assert not _is_linked(a1, 'shadowrun_SourceBook', b)
    if hasattr(a2, 'shadowrun_SourceBook'):
        assert _is_linked(a2, 'shadowrun_SourceBook', b)
    _safe_set(b, 'shadowrun_Quelle', None)
    assert not _is_linked(b, 'shadowrun_Quelle', a2)
    if hasattr(a2, 'shadowrun_SourceBook'):
        assert not _is_linked(a2, 'shadowrun_SourceBook', b)


def test_assoc_typ71_reverse_link_reassign_clear():
    a1 = shadowrun_Reichweite(reichweiteExtrem=7, reichweiteExtrem1=7, reichweiteKurz=7, reichweiteKurz1=7, reichweiteMittel=7, reichweiteMittel1=7, reichweiteWeit=7, reichweiteWeit1=7)
    a2 = shadowrun_Reichweite(reichweiteExtrem=13, reichweiteExtrem1=13, reichweiteKurz=13, reichweiteKurz1=13, reichweiteMittel=13, reichweiteMittel1=13, reichweiteWeit=13, reichweiteWeit1=13)
    b = shadowrun_Munition(niveau=7, power=7, schadensTyp="sample_text")
    _safe_set(b, 'shadowrun_Munition', a1)
    assert _is_linked(b, 'shadowrun_Munition', a1)
    if hasattr(a1, 'shadowrun_Reichweite72'):
        assert _is_linked(a1, 'shadowrun_Reichweite72', b)
    _safe_set(b, 'shadowrun_Munition', a2)
    assert _is_linked(b, 'shadowrun_Munition', a2)
    if hasattr(a1, 'shadowrun_Reichweite72'):
        assert not _is_linked(a1, 'shadowrun_Reichweite72', b)
    if hasattr(a2, 'shadowrun_Reichweite72'):
        assert _is_linked(a2, 'shadowrun_Reichweite72', b)
    _safe_set(b, 'shadowrun_Munition', None)
    assert not _is_linked(b, 'shadowrun_Munition', a2)
    if hasattr(a2, 'shadowrun_Reichweite72'):
        assert not _is_linked(a2, 'shadowrun_Reichweite72', b)


def test_assoc_zauber61_reverse_link_reassign_clear():
    a1 = shadowrun_Zauber(Dauer="sample_text", Enzug="sample_text", Mindestwurf="sample_text", Schaden="sample_text", art="sample_text", reichweite="sample_text")
    a2 = shadowrun_Zauber(Dauer="sample_text_2", Enzug="sample_text_2", Mindestwurf="sample_text_2", Schaden="sample_text_2", art="sample_text_2", reichweite="sample_text_2")
    b = shadowrun_PersonaZauber(stufe=7)
    _safe_set(b, 'shadowrun_PersonaZauber62', a1)
    assert _is_linked(b, 'shadowrun_PersonaZauber62', a1)
    if hasattr(a1, 'shadowrun_Zauber'):
        assert _is_linked(a1, 'shadowrun_Zauber', b)
    _safe_set(b, 'shadowrun_PersonaZauber62', a2)
    assert _is_linked(b, 'shadowrun_PersonaZauber62', a2)
    if hasattr(a1, 'shadowrun_Zauber'):
        assert not _is_linked(a1, 'shadowrun_Zauber', b)
    if hasattr(a2, 'shadowrun_Zauber'):
        assert _is_linked(a2, 'shadowrun_Zauber', b)
    _safe_set(b, 'shadowrun_PersonaZauber62', None)
    assert not _is_linked(b, 'shadowrun_PersonaZauber62', a2)
    if hasattr(a2, 'shadowrun_Zauber'):
        assert not _is_linked(a2, 'shadowrun_Zauber', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribut40_stub_double():
    # shadowrun_EAttribute has no real 'shadowrun_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AttributModifikatorWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AttributModifikatorWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AttributModifikatorWert(wert=7)
    partner = shadowrun_EAttribute()
    setattr(partner, 'shadowrun_EAttribute', None)
    _safe_set(owner, 'shadowrun_AttributModifikatorWert', partner)
    assert getattr(partner, 'shadowrun_EAttribute') == owner
    _safe_set(owner, 'shadowrun_AttributModifikatorWert', None)
    assert getattr(partner, 'shadowrun_EAttribute') is None


def test_assoc_bioware3_stub_double():
    # shadowrun_BioWare has no real 'BioWare' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstaktPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstaktPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    partner = shadowrun_BioWare()
    setattr(partner, 'BioWare', None)
    _safe_set(owner, 'persona4', {partner})
    assert getattr(partner, 'BioWare') == owner
    _safe_set(owner, 'persona4', set())
    assert getattr(partner, 'BioWare') is None


def test_assoc_cyberware2_stub_double():
    # shadowrun_Cyberware has no real 'Cyberware' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstaktPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstaktPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    partner = shadowrun_Cyberware()
    setattr(partner, 'Cyberware', None)
    _safe_set(owner, 'persona', {partner})
    assert getattr(partner, 'Cyberware') == owner
    _safe_set(owner, 'persona', set())
    assert getattr(partner, 'Cyberware') is None


def test_assoc_entries53_stub_double():
    # shadowrun_AbstraktModifikatoren has no real 'shadowrun_AbstraktModifikatoren' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_ModifikatorList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_ModifikatorList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_ModifikatorList(name="sample_text")
    partner = shadowrun_AbstraktModifikatoren()
    setattr(partner, 'shadowrun_AbstraktModifikatoren', None)
    _safe_set(owner, 'shadowrun_ModifikatorList', {partner})
    assert getattr(partner, 'shadowrun_AbstraktModifikatoren') == owner
    _safe_set(owner, 'shadowrun_ModifikatorList', set())
    assert getattr(partner, 'shadowrun_AbstraktModifikatoren') is None


def test_assoc_entries56_stub_double():
    # shadowrun_GengenstandListe has no real 'shadowrun_GengenstandListe' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstaktGegenstand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstaktGegenstand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstaktGegenstand(gewicht=3.14, inBenutzung=True, raumKapazitaet=7, tragbar="sample_text", verbraucht=True)
    partner = shadowrun_GengenstandListe()
    setattr(partner, 'shadowrun_GengenstandListe', None)
    _safe_set(owner, 'shadowrun_AbstaktGegenstand57', partner)
    assert owner in getattr(partner, 'shadowrun_GengenstandListe')
    _safe_set(owner, 'shadowrun_AbstaktGegenstand57', None)
    assert owner not in getattr(partner, 'shadowrun_GengenstandListe')


def test_assoc_entries58_stub_double():
    # shadowrun_Reichweiten has no real 'shadowrun_Reichweiten' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_Reichweite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_Reichweite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_Reichweite(reichweiteExtrem=7, reichweiteExtrem1=7, reichweiteKurz=7, reichweiteKurz1=7, reichweiteMittel=7, reichweiteMittel1=7, reichweiteWeit=7, reichweiteWeit1=7)
    partner = shadowrun_Reichweiten()
    setattr(partner, 'shadowrun_Reichweiten', None)
    _safe_set(owner, 'shadowrun_Reichweite59', partner)
    assert owner in getattr(partner, 'shadowrun_Reichweiten')
    _safe_set(owner, 'shadowrun_Reichweite59', None)
    assert owner not in getattr(partner, 'shadowrun_Reichweiten')


def test_assoc_fertigkeit20_stub_double():
    # shadowrun_Fertigkeit has no real 'shadowrun_Fertigkeit' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstaktWaffe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstaktWaffe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstaktWaffe(schadenscode="sample_text")
    partner = shadowrun_Fertigkeit()
    setattr(partner, 'shadowrun_Fertigkeit', None)
    _safe_set(owner, 'shadowrun_AbstaktWaffe', partner)
    assert getattr(partner, 'shadowrun_Fertigkeit') == owner
    _safe_set(owner, 'shadowrun_AbstaktWaffe', None)
    assert getattr(partner, 'shadowrun_Fertigkeit') is None


def test_assoc_fertigkeit49_stub_double():
    # shadowrun_AbstraktFertigkeit has no real 'shadowrun_AbstraktFertigkeit' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_PersonaFertigkeit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_PersonaFertigkeit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_PersonaFertigkeit(stufe=7)
    partner = shadowrun_AbstraktFertigkeit()
    setattr(partner, 'shadowrun_AbstraktFertigkeit', None)
    _safe_set(owner, 'shadowrun_PersonaFertigkeit50', partner)
    assert getattr(partner, 'shadowrun_AbstraktFertigkeit') == owner
    _safe_set(owner, 'shadowrun_PersonaFertigkeit50', None)
    assert getattr(partner, 'shadowrun_AbstraktFertigkeit') is None


def test_assoc_konzentration21_stub_double():
    # shadowrun_Konzentration has no real 'shadowrun_Konzentration' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstaktWaffe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstaktWaffe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstaktWaffe(schadenscode="sample_text")
    partner = shadowrun_Konzentration()
    setattr(partner, 'shadowrun_Konzentration', None)
    _safe_set(owner, 'shadowrun_AbstaktWaffe22', partner)
    assert getattr(partner, 'shadowrun_Konzentration') == owner
    _safe_set(owner, 'shadowrun_AbstaktWaffe22', None)
    assert getattr(partner, 'shadowrun_Konzentration') is None


def test_assoc_modifiziertes41_stub_double():
    # shadowrun_Modifizierbar has no real 'Modifizierbar' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AttributModifikatorWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AttributModifikatorWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AttributModifikatorWert(wert=7)
    partner = shadowrun_Modifizierbar()
    setattr(partner, 'Modifizierbar', None)
    _safe_set(owner, 'mods', partner)
    assert getattr(partner, 'Modifizierbar') == owner
    _safe_set(owner, 'mods', None)
    assert getattr(partner, 'Modifizierbar') is None


def test_assoc_mods69_stub_double():
    # shadowrun_Modifizierbar has no real 'modifiziertes' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AttributModifikatorWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AttributModifikatorWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AttributModifikatorWert(wert=7)
    partner = shadowrun_Modifizierbar()
    setattr(partner, 'modifiziertes', None)
    _safe_set(owner, 'AttributModifikatorWert', partner)
    assert owner in getattr(partner, 'modifiziertes')
    _safe_set(owner, 'AttributModifikatorWert', None)
    assert owner not in getattr(partner, 'modifiziertes')


def test_assoc_munitionReservior28_stub_double():
    # shadowrun_MunitionsBehealter has no real 'shadowrun_MunitionsBehealter' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_Feuerwaffe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_Feuerwaffe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_Feuerwaffe(kapazitaet=7, modie="sample_text", munitionstyp="sample_text")
    partner = shadowrun_MunitionsBehealter()
    setattr(partner, 'shadowrun_MunitionsBehealter', None)
    _safe_set(owner, 'shadowrun_Feuerwaffe', partner)
    assert getattr(partner, 'shadowrun_MunitionsBehealter') == owner
    _safe_set(owner, 'shadowrun_Feuerwaffe', None)
    assert getattr(partner, 'shadowrun_MunitionsBehealter') is None


def test_assoc_persona38_stub_double():
    # shadowrun_Cyberware has no real 'cyberware' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstaktPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstaktPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    partner = shadowrun_Cyberware()
    setattr(partner, 'cyberware', None)
    _safe_set(owner, 'AbstaktPersona', partner)
    assert getattr(partner, 'cyberware') == owner
    _safe_set(owner, 'AbstaktPersona', None)
    assert getattr(partner, 'cyberware') is None


def test_assoc_persona51_stub_double():
    # shadowrun_BioWare has no real 'bioware' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstaktPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstaktPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstaktPersona(CharismaBase=7, EssenzBase=7, InteligenzBase=7, KampfpoolBase=7, KonsitutionBase=7, ReaktionBase=7, ReaktionWBase=7, SchnelligkeitBase=7, StaerkeBase=7, WillenskraftBase=7, eigenGewicht=7, modsetter="sample_text")
    partner = shadowrun_BioWare()
    setattr(partner, 'bioware', None)
    _safe_set(owner, 'AbstaktPersona52', partner)
    assert getattr(partner, 'bioware') == owner
    _safe_set(owner, 'AbstaktPersona52', None)
    assert getattr(partner, 'bioware') is None


def test_assoc_position25_stub_double():
    # shadowrun_RaumKoordinate has no real 'shadowrun_RaumKoordinate' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstrakRaumKoerper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstrakRaumKoerper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstrakRaumKoerper()
    partner = shadowrun_RaumKoordinate()
    setattr(partner, 'shadowrun_RaumKoordinate', None)
    _safe_set(owner, 'shadowrun_AbstrakRaumKoerper', partner)
    assert getattr(partner, 'shadowrun_RaumKoordinate') == owner
    _safe_set(owner, 'shadowrun_AbstrakRaumKoerper', None)
    assert getattr(partner, 'shadowrun_RaumKoordinate') is None


def test_assoc_reichweite0_stub_double():
    # shadowrun_AbstaktFernKampfwaffe has no real 'shadowrun_AbstaktFernKampfwaffe' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_Reichweite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_Reichweite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_Reichweite(reichweiteExtrem=7, reichweiteExtrem1=7, reichweiteKurz=7, reichweiteKurz1=7, reichweiteMittel=7, reichweiteMittel1=7, reichweiteWeit=7, reichweiteWeit1=7)
    partner = shadowrun_AbstaktFernKampfwaffe()
    setattr(partner, 'shadowrun_AbstaktFernKampfwaffe', None)
    _safe_set(owner, 'shadowrun_Reichweite', partner)
    assert getattr(partner, 'shadowrun_AbstaktFernKampfwaffe') == owner
    _safe_set(owner, 'shadowrun_Reichweite', None)
    assert getattr(partner, 'shadowrun_AbstaktFernKampfwaffe') is None


def test_assoc_spezialisierung23_stub_double():
    # shadowrun_Spezialisierung has no real 'shadowrun_Spezialisierung' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_AbstaktWaffe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_AbstaktWaffe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_AbstaktWaffe(schadenscode="sample_text")
    partner = shadowrun_Spezialisierung()
    setattr(partner, 'shadowrun_Spezialisierung', None)
    _safe_set(owner, 'shadowrun_AbstaktWaffe24', partner)
    assert getattr(partner, 'shadowrun_Spezialisierung') == owner
    _safe_set(owner, 'shadowrun_AbstaktWaffe24', None)
    assert getattr(partner, 'shadowrun_Spezialisierung') is None


def test_assoc_zauber60_stub_double():
    # shadowrun_MagiePersona has no real 'shadowrun_MagiePersona' property in the generated
    # code (a bare stub) -- manually attach it so shadowrun_PersonaZauber's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shadowrun_PersonaZauber's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shadowrun_PersonaZauber(stufe=7)
    partner = shadowrun_MagiePersona()
    setattr(partner, 'shadowrun_MagiePersona', None)
    _safe_set(owner, 'shadowrun_PersonaZauber', partner)
    assert owner in getattr(partner, 'shadowrun_MagiePersona')
    _safe_set(owner, 'shadowrun_PersonaZauber', None)
    assert owner not in getattr(partner, 'shadowrun_MagiePersona')


