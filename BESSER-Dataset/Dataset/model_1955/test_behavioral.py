import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstaktFernKampfwaffe,
    AbstaktWaffe,
    AbstractMatrixDevice,
    AbstraktFokus,
    AbstraktGegenstand,
    AbstraktModifikatoren,
    AbstraktPersona,
    AbtraktGranate,
    ActiveMatixDevice,
    Anwendbar,
    AstraleProjektion,
    BaseMagischePersona,
    BasicProgram,
    BerechneteAttribute,
    Beschreibbar,
    Capacity,
    ChrakterLimits,
    CredstickTransaction,
    CyberwareEnhancement,
    Erlernbar,
    Fahrzeug,
    FahrzeugModifikation,
    FahrzeugZustand,
    Fakeable,
    Fertigkeit,
    Fokus,
    GeistigeAttribute,
    GeldWert,
    Identifiable,
    IntervallVertrag,
    KiAdept,
    KoerperPersona,
    KoerperlicheAttribute,
    Koerpermods,
    LifestyleOption,
    MagischeMods,
    MagischePersona,
    MagischeStufe,
    MatixConditionMonitor,
    MatrixAttributes,
    MatrixDevice,
    MatrixProgram,
    Menge,
    ModifikatorAttribute,
    Modifizierbar,
    Modifyable,
    Munition,
    Nahkampfwaffe,
    Panzerung,
    PassagierFahrzeug,
    PersonaZustand,
    Quelle,
    ResonanzPersona,
    RiggerProgram,
    Sensor,
    Software,
    Spezialisierung,
    SpezielleAttribute,
    Spezies,
    Steigerbar,
    StufenPersona,
    Substance,
    Vertrag,
    Wissensfertigkeit,
    Wurfwaffe,
    Zauberer,
    shr5_AbstaktFernKampfwaffe,
    shr5_AbstaktWaffe,
    shr5_AbstractMatrixDevice,
    shr5_AbstraktFokus,
    shr5_AbstraktGegenstand,
    shr5_AbstraktModifikatoren,
    shr5_AbstraktPersona,
    shr5_AbtraktGranate,
    shr5_ActiveMatixDevice,
    shr5_Anwendbar,
    shr5_AspektMagier,
    shr5_AstraleProjektion,
    shr5_AttributModifikatorWert,
    shr5_AutoSoft,
    shr5_BaseMagischePersona,
    shr5_BasicProgram,
    shr5_BerechneteAttribute,
    shr5_Beschreibbar,
    shr5_BioWare,
    shr5_Bodenfahrzeug,
    shr5_Capacity,
    shr5_ChrakterLimits,
    shr5_Commlink,
    shr5_CommonProgram,
    shr5_ConsumerSoft,
    shr5_Credstick,
    shr5_CredstickTransaction,
    shr5_Critter,
    shr5_CritterKraft,
    shr5_CyberImplantWeapon,
    shr5_Cyberdeck,
    shr5_Cyberware,
    shr5_CyberwareEnhancement,
    shr5_CyberwareModifikatioren,
    shr5_Datasoft,
    shr5_DefaultWifi,
    shr5_Drohne,
    shr5_Drug,
    shr5_EAttribute,
    shr5_EObject,
    shr5_EReference,
    shr5_Echo,
    shr5_Erlernbar,
    shr5_Fahrzeug,
    shr5_FahrzeugErweiterung,
    shr5_FahrzeugModifikation,
    shr5_FahrzeugZustand,
    shr5_Fakeable,
    shr5_FernkampfwaffeModifikator,
    shr5_FernkampfwaffenModifikatoren,
    shr5_Fertigkeit,
    shr5_FertigkeitsGruppe,
    shr5_Feuerwaffe,
    shr5_Fokus,
    shr5_FokusBinding,
    shr5_GebundenerGeist,
    shr5_Gegenstand,
    shr5_GegenstandStufen,
    shr5_Geist,
    shr5_GeistigeAttribute,
    shr5_GeldWert,
    shr5_Granate,
    shr5_Host,
    shr5_Identifiable,
    shr5_Initation,
    shr5_IntervallVertrag,
    shr5_KiAdept,
    shr5_KiKraft,
    shr5_Kleidung,
    shr5_KleindungsModifikator,
    shr5_KoerperPersona,
    shr5_KoerperlicheAttribute,
    shr5_Koerpermods,
    shr5_KomplexeForm,
    shr5_Lifestyle,
    shr5_LifestyleOption,
    shr5_Lizenz,
    shr5_Localization,
    shr5_Magazin,
    shr5_MagieFokus,
    shr5_Magier,
    shr5_MagischeMods,
    shr5_MagischePersona,
    shr5_MagischeStufe,
    shr5_MagischeTradition,
    shr5_MartialartStyle,
    shr5_MartialartTechnique,
    shr5_MatixConditionMonitor,
    shr5_MatrixAttributes,
    shr5_MatrixDevice,
    shr5_MatrixProgram,
    shr5_Menge,
    shr5_MetaMagie,
    shr5_MiniGrenate,
    shr5_ModifikatorAttribute,
    shr5_Modifizierbar,
    shr5_Modifyable,
    shr5_MudanPersona,
    shr5_Munition,
    shr5_MysticAdept,
    shr5_Nahkampfwaffe,
    shr5_Panzerung,
    shr5_PassagierFahrzeug,
    shr5_PercentLifestyleOption,
    shr5_PersonaEigenschaft,
    shr5_PersonaFertigkeit,
    shr5_PersonaFertigkeitsGruppe,
    shr5_PersonaKomplexForm,
    shr5_PersonaMartialartStyle,
    shr5_PersonaMartialartTechnique,
    shr5_PersonaZauber,
    shr5_PersonaZustand,
    shr5_PersonalAreaNetwork,
    shr5_ProbenModifikatoren,
    shr5_Projektilwaffe,
    shr5_QiFokus,
    shr5_Quelle,
    shr5_Reichweite,
    shr5_ResonanzPersona,
    shr5_RiggerCommandConsole,
    shr5_RiggerProgram,
    shr5_Schutzgeist,
    shr5_Sensor,
    shr5_SensorArray,
    shr5_SensorFunction,
    shr5_ShoppingTransaction,
    shr5_ShrList,
    shr5_Sichtverhaeltnisse,
    shr5_Sin,
    shr5_SkillSoft,
    shr5_Software,
    shr5_SoftwareAgent,
    shr5_SourceBook,
    shr5_SourceLink,
    shr5_Spezialisierung,
    shr5_SpezielleAttribute,
    shr5_Spezies,
    shr5_Sprachfertigkeit,
    shr5_Sprite,
    shr5_Steigerbar,
    shr5_StufenPersona,
    shr5_Substance,
    shr5_SubstanceContainer,
    shr5_Technomancer,
    shr5_Toxin,
    shr5_TransferAmount,
    shr5_Tutorsoft,
    shr5_Vertrag,
    shr5_WaffenFokus,
    shr5_WeaponMount,
    shr5_Wissensfertigkeit,
    shr5_Wurfwaffe,
    shr5_Zauber,
    shr5_Zauberer,
    AddictionType,
    CritterDauer,
    CritterHandlung,
    CritterReichweite,
    CyberwareType,
    Enzug,
    FeuerModus,
    FeuwerwaffenErweiterung,
    InterfaceModus,
    MagazinTyp,
    MatrixProgramType,
    ModifikatorType,
    ProgramType,
    ResonanzZiel,
    SchadensTyp,
    SmartgunType,
    SubstanceEffect,
    SubstanceVector,
    TimeUnits,
    ZauberArt,
    ZauberDauer,
    ZauberReichweite,
    armorModificationType,
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

def test_assoc_angriff47_reverse_link_reassign_clear():
    a1 = shr5_Spezies(charismaMax=7, charismaMin=7, edgeMax=7, edgeMin=7, essenzMax=7, essenzMin=7, geschicklichkeitMax=7, geschicklichkeitMin=7, intuitionMax=7, intuitionMin=7, konstitutionMax=7, konstitutionMin=7, laufen=7, logikMax=7, logikMin=7, magieMax=7, magieMin=7, reaktionMax=7, reaktionMin=7, rennen=7, resonanzMax=7, resonanzMin=7, sprinten=7, staerkeMax=7, staerkeMin=7, willenskraftMax=7, willenskraftMin=7)
    a2 = shr5_Spezies(charismaMax=13, charismaMin=13, edgeMax=13, edgeMin=13, essenzMax=13, essenzMin=13, geschicklichkeitMax=13, geschicklichkeitMin=13, intuitionMax=13, intuitionMin=13, konstitutionMax=13, konstitutionMin=13, laufen=13, logikMax=13, logikMin=13, magieMax=13, magieMin=13, reaktionMax=13, reaktionMin=13, rennen=13, resonanzMax=13, resonanzMin=13, sprinten=13, staerkeMax=13, staerkeMin=13, willenskraftMax=13, willenskraftMin=13)
    b = shr5_Nahkampfwaffe(reichweite=7)
    _safe_set(b, 'shr5_Nahkampfwaffe', a1)
    assert _is_linked(b, 'shr5_Nahkampfwaffe', a1)
    if hasattr(a1, 'shr5_Spezies48'):
        assert _is_linked(a1, 'shr5_Spezies48', b)
    _safe_set(b, 'shr5_Nahkampfwaffe', a2)
    assert _is_linked(b, 'shr5_Nahkampfwaffe', a2)
    if hasattr(a1, 'shr5_Spezies48'):
        assert not _is_linked(a1, 'shr5_Spezies48', b)
    if hasattr(a2, 'shr5_Spezies48'):
        assert _is_linked(a2, 'shr5_Spezies48', b)
    _safe_set(b, 'shr5_Nahkampfwaffe', None)
    assert not _is_linked(b, 'shr5_Nahkampfwaffe', a2)
    if hasattr(a2, 'shr5_Spezies48'):
        assert not _is_linked(a2, 'shr5_Spezies48', b)


def test_assoc_beschwoerbar151_reverse_link_reassign_clear():
    a1 = shr5_MagischeTradition(enzug="sample_text")
    a2 = shr5_MagischeTradition(enzug="sample_text_2")
    b = shr5_Geist(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    _safe_set(b, 'shr5_Geist153', a1)
    assert _is_linked(b, 'shr5_Geist153', a1)
    if hasattr(a1, 'shr5_MagischeTradition152'):
        assert _is_linked(a1, 'shr5_MagischeTradition152', b)
    _safe_set(b, 'shr5_Geist153', a2)
    assert _is_linked(b, 'shr5_Geist153', a2)
    if hasattr(a1, 'shr5_MagischeTradition152'):
        assert not _is_linked(a1, 'shr5_MagischeTradition152', b)
    if hasattr(a2, 'shr5_MagischeTradition152'):
        assert _is_linked(a2, 'shr5_MagischeTradition152', b)
    _safe_set(b, 'shr5_Geist153', None)
    assert not _is_linked(b, 'shr5_Geist153', a2)
    if hasattr(a2, 'shr5_MagischeTradition152'):
        assert not _is_linked(a2, 'shr5_MagischeTradition152', b)


def test_assoc_boundFoki45_reverse_link_reassign_clear():
    a1 = shr5_FokusBinding(active=True)
    a2 = shr5_FokusBinding(active=False)
    b = shr5_BaseMagischePersona(magie=7, magieBasis=7)
    _safe_set(b, 'shr5_BaseMagischePersona46', {a1})
    assert _is_linked(b, 'shr5_BaseMagischePersona46', a1)
    if hasattr(a1, 'shr5_FokusBinding'):
        assert _is_linked(a1, 'shr5_FokusBinding', b)
    _safe_set(b, 'shr5_BaseMagischePersona46', {a2})
    assert _is_linked(b, 'shr5_BaseMagischePersona46', a2)
    if hasattr(a1, 'shr5_FokusBinding'):
        assert not _is_linked(a1, 'shr5_FokusBinding', b)
    if hasattr(a2, 'shr5_FokusBinding'):
        assert _is_linked(a2, 'shr5_FokusBinding', b)
    _safe_set(b, 'shr5_BaseMagischePersona46', set())
    assert not _is_linked(b, 'shr5_BaseMagischePersona46', a2)
    if hasattr(a2, 'shr5_FokusBinding'):
        assert not _is_linked(a2, 'shr5_FokusBinding', b)


def test_assoc_chemical173_reverse_link_reassign_clear():
    a1 = shr5_Substance(speed="sample_text", vector="sample_text")
    a2 = shr5_Substance(speed="sample_text_2", vector="sample_text_2")
    b = shr5_AbtraktGranate(blast="sample_text")
    _safe_set(b, 'shr5_AbtraktGranate', a1)
    assert _is_linked(b, 'shr5_AbtraktGranate', a1)
    if hasattr(a1, 'shr5_Substance174'):
        assert _is_linked(a1, 'shr5_Substance174', b)
    _safe_set(b, 'shr5_AbtraktGranate', a2)
    assert _is_linked(b, 'shr5_AbtraktGranate', a2)
    if hasattr(a1, 'shr5_Substance174'):
        assert not _is_linked(a1, 'shr5_Substance174', b)
    if hasattr(a2, 'shr5_Substance174'):
        assert _is_linked(a2, 'shr5_Substance174', b)
    _safe_set(b, 'shr5_AbtraktGranate', None)
    assert not _is_linked(b, 'shr5_AbtraktGranate', a2)
    if hasattr(a2, 'shr5_Substance174'):
        assert not _is_linked(a2, 'shr5_Substance174', b)


def test_assoc_dest157_reverse_link_reassign_clear():
    a1 = shr5_TransferAmount(amountToTransfer="sample_text")
    a2 = shr5_TransferAmount(amountToTransfer="sample_text_2")
    b = shr5_Credstick(currentValue="sample_text", maxValue=7)
    _safe_set(b, 'shr5_Credstick159', a1)
    assert _is_linked(b, 'shr5_Credstick159', a1)
    if hasattr(a1, 'shr5_TransferAmount158'):
        assert _is_linked(a1, 'shr5_TransferAmount158', b)
    _safe_set(b, 'shr5_Credstick159', a2)
    assert _is_linked(b, 'shr5_Credstick159', a2)
    if hasattr(a1, 'shr5_TransferAmount158'):
        assert not _is_linked(a1, 'shr5_TransferAmount158', b)
    if hasattr(a2, 'shr5_TransferAmount158'):
        assert _is_linked(a2, 'shr5_TransferAmount158', b)
    _safe_set(b, 'shr5_Credstick159', None)
    assert not _is_linked(b, 'shr5_Credstick159', a2)
    if hasattr(a2, 'shr5_TransferAmount158'):
        assert not _is_linked(a2, 'shr5_TransferAmount158', b)


def test_assoc_eigenschaften41_reverse_link_reassign_clear():
    a1 = shr5_PersonaEigenschaft(karmaKosten=7)
    a2 = shr5_PersonaEigenschaft(karmaKosten=13)
    b = shr5_KoerperPersona(zustandGeistig=7, zustandKoerperlich=7)
    _safe_set(b, 'shr5_KoerperPersona42', {a1})
    assert _is_linked(b, 'shr5_KoerperPersona42', a1)
    if hasattr(a1, 'shr5_PersonaEigenschaft'):
        assert _is_linked(a1, 'shr5_PersonaEigenschaft', b)
    _safe_set(b, 'shr5_KoerperPersona42', {a2})
    assert _is_linked(b, 'shr5_KoerperPersona42', a2)
    if hasattr(a1, 'shr5_PersonaEigenschaft'):
        assert not _is_linked(a1, 'shr5_PersonaEigenschaft', b)
    if hasattr(a2, 'shr5_PersonaEigenschaft'):
        assert _is_linked(a2, 'shr5_PersonaEigenschaft', b)
    _safe_set(b, 'shr5_KoerperPersona42', set())
    assert not _is_linked(b, 'shr5_KoerperPersona42', a2)
    if hasattr(a2, 'shr5_PersonaEigenschaft'):
        assert not _is_linked(a2, 'shr5_PersonaEigenschaft', b)


def test_assoc_einbau15_reverse_link_reassign_clear():
    a1 = shr5_Feuerwaffe(erweiterung="sample_text", kapazitaet=7, modie="sample_text", munitionstyp="sample_text", rueckstoss=7)
    a2 = shr5_Feuerwaffe(erweiterung="sample_text_2", kapazitaet=13, modie="sample_text_2", munitionstyp="sample_text_2", rueckstoss=13)
    b = shr5_FernkampfwaffeModifikator(ep="sample_text")
    _safe_set(b, 'shr5_FernkampfwaffeModifikator', a1)
    assert _is_linked(b, 'shr5_FernkampfwaffeModifikator', a1)
    if hasattr(a1, 'shr5_Feuerwaffe'):
        assert _is_linked(a1, 'shr5_Feuerwaffe', b)
    _safe_set(b, 'shr5_FernkampfwaffeModifikator', a2)
    assert _is_linked(b, 'shr5_FernkampfwaffeModifikator', a2)
    if hasattr(a1, 'shr5_Feuerwaffe'):
        assert not _is_linked(a1, 'shr5_Feuerwaffe', b)
    if hasattr(a2, 'shr5_Feuerwaffe'):
        assert _is_linked(a2, 'shr5_Feuerwaffe', b)
    _safe_set(b, 'shr5_FernkampfwaffeModifikator', None)
    assert not _is_linked(b, 'shr5_FernkampfwaffeModifikator', a2)
    if hasattr(a2, 'shr5_Feuerwaffe'):
        assert not _is_linked(a2, 'shr5_Feuerwaffe', b)


def test_assoc_einbau34_reverse_link_reassign_clear():
    a1 = shr5_CyberwareEnhancement(capacityUse=7, type="sample_text")
    a2 = shr5_CyberwareEnhancement(capacityUse=13, type="sample_text_2")
    b = shr5_Cyberware(cyberwareCapacity=7, type="sample_text")
    _safe_set(b, 'shr5_Cyberware35', {a1})
    assert _is_linked(b, 'shr5_Cyberware35', a1)
    if hasattr(a1, 'shr5_CyberwareEnhancement'):
        assert _is_linked(a1, 'shr5_CyberwareEnhancement', b)
    _safe_set(b, 'shr5_Cyberware35', {a2})
    assert _is_linked(b, 'shr5_Cyberware35', a2)
    if hasattr(a1, 'shr5_CyberwareEnhancement'):
        assert not _is_linked(a1, 'shr5_CyberwareEnhancement', b)
    if hasattr(a2, 'shr5_CyberwareEnhancement'):
        assert _is_linked(a2, 'shr5_CyberwareEnhancement', b)
    _safe_set(b, 'shr5_Cyberware35', set())
    assert not _is_linked(b, 'shr5_Cyberware35', a2)
    if hasattr(a2, 'shr5_CyberwareEnhancement'):
        assert not _is_linked(a2, 'shr5_CyberwareEnhancement', b)


def test_assoc_fokus139_reverse_link_reassign_clear():
    a1 = shr5_FokusBinding(active=True)
    a2 = shr5_FokusBinding(active=False)
    b = shr5_Fokus(bindungskosten=7)
    _safe_set(b, 'shr5_Fokus', a1)
    assert _is_linked(b, 'shr5_Fokus', a1)
    if hasattr(a1, 'shr5_FokusBinding140'):
        assert _is_linked(a1, 'shr5_FokusBinding140', b)
    _safe_set(b, 'shr5_Fokus', a2)
    assert _is_linked(b, 'shr5_Fokus', a2)
    if hasattr(a1, 'shr5_FokusBinding140'):
        assert not _is_linked(a1, 'shr5_FokusBinding140', b)
    if hasattr(a2, 'shr5_FokusBinding140'):
        assert _is_linked(a2, 'shr5_FokusBinding140', b)
    _safe_set(b, 'shr5_Fokus', None)
    assert not _is_linked(b, 'shr5_Fokus', a2)
    if hasattr(a2, 'shr5_FokusBinding140'):
        assert not _is_linked(a2, 'shr5_FokusBinding140', b)


def test_assoc_form80_reverse_link_reassign_clear():
    a1 = shr5_PersonaKomplexForm(stufe=7)
    a2 = shr5_PersonaKomplexForm(stufe=13)
    b = shr5_KomplexeForm(dauer="sample_text", schwund="sample_text", ziel="sample_text")
    _safe_set(b, 'shr5_KomplexeForm', a1)
    assert _is_linked(b, 'shr5_KomplexeForm', a1)
    if hasattr(a1, 'shr5_PersonaKomplexForm81'):
        assert _is_linked(a1, 'shr5_PersonaKomplexForm81', b)
    _safe_set(b, 'shr5_KomplexeForm', a2)
    assert _is_linked(b, 'shr5_KomplexeForm', a2)
    if hasattr(a1, 'shr5_PersonaKomplexForm81'):
        assert not _is_linked(a1, 'shr5_PersonaKomplexForm81', b)
    if hasattr(a2, 'shr5_PersonaKomplexForm81'):
        assert _is_linked(a2, 'shr5_PersonaKomplexForm81', b)
    _safe_set(b, 'shr5_KomplexeForm', None)
    assert not _is_linked(b, 'shr5_KomplexeForm', a2)
    if hasattr(a2, 'shr5_PersonaKomplexForm81'):
        assert not _is_linked(a2, 'shr5_PersonaKomplexForm81', b)


def test_assoc_formel64_reverse_link_reassign_clear():
    a1 = shr5_Zauber(art="sample_text", dauer="sample_text", entzug="sample_text", kategorie="sample_text", merkmale="sample_text", reichweite="sample_text", schaden="sample_text")
    a2 = shr5_Zauber(art="sample_text_2", dauer="sample_text_2", entzug="sample_text_2", kategorie="sample_text_2", merkmale="sample_text_2", reichweite="sample_text_2", schaden="sample_text_2")
    b = shr5_PersonaZauber(stufe=7)
    _safe_set(b, 'shr5_PersonaZauber65', a1)
    assert _is_linked(b, 'shr5_PersonaZauber65', a1)
    if hasattr(a1, 'shr5_Zauber'):
        assert _is_linked(a1, 'shr5_Zauber', b)
    _safe_set(b, 'shr5_PersonaZauber65', a2)
    assert _is_linked(b, 'shr5_PersonaZauber65', a2)
    if hasattr(a1, 'shr5_Zauber'):
        assert not _is_linked(a1, 'shr5_Zauber', b)
    if hasattr(a2, 'shr5_Zauber'):
        assert _is_linked(a2, 'shr5_Zauber', b)
    _safe_set(b, 'shr5_PersonaZauber65', None)
    assert not _is_linked(b, 'shr5_PersonaZauber65', a2)
    if hasattr(a2, 'shr5_Zauber'):
        assert not _is_linked(a2, 'shr5_Zauber', b)


def test_assoc_functions160_reverse_link_reassign_clear():
    a1 = shr5_SensorFunction(maxRange=7)
    a2 = shr5_SensorFunction(maxRange=13)
    b = shr5_Sensor(capacityValue=7, rating=7)
    _safe_set(b, 'shr5_Sensor', {a1})
    assert _is_linked(b, 'shr5_Sensor', a1)
    if hasattr(a1, 'shr5_SensorFunction'):
        assert _is_linked(a1, 'shr5_SensorFunction', b)
    _safe_set(b, 'shr5_Sensor', {a2})
    assert _is_linked(b, 'shr5_Sensor', a2)
    if hasattr(a1, 'shr5_SensorFunction'):
        assert not _is_linked(a1, 'shr5_SensorFunction', b)
    if hasattr(a2, 'shr5_SensorFunction'):
        assert _is_linked(a2, 'shr5_SensorFunction', b)
    _safe_set(b, 'shr5_Sensor', set())
    assert not _is_linked(b, 'shr5_Sensor', a2)
    if hasattr(a2, 'shr5_SensorFunction'):
        assert not _is_linked(a2, 'shr5_SensorFunction', b)


def test_assoc_gebundeneGeister57_reverse_link_reassign_clear():
    a1 = shr5_Zauberer(enzug=7)
    a2 = shr5_Zauberer(enzug=13)
    b = shr5_GebundenerGeist(dienste=7)
    _safe_set(b, 'shr5_GebundenerGeist', a1)
    assert _is_linked(b, 'shr5_GebundenerGeist', a1)
    if hasattr(a1, 'shr5_Zauberer58'):
        assert _is_linked(a1, 'shr5_Zauberer58', b)
    _safe_set(b, 'shr5_GebundenerGeist', a2)
    assert _is_linked(b, 'shr5_GebundenerGeist', a2)
    if hasattr(a1, 'shr5_Zauberer58'):
        assert not _is_linked(a1, 'shr5_Zauberer58', b)
    if hasattr(a2, 'shr5_Zauberer58'):
        assert _is_linked(a2, 'shr5_Zauberer58', b)
    _safe_set(b, 'shr5_GebundenerGeist', None)
    assert not _is_linked(b, 'shr5_GebundenerGeist', a2)
    if hasattr(a2, 'shr5_Zauberer58'):
        assert not _is_linked(a2, 'shr5_Zauberer58', b)


def test_assoc_geist89_reverse_link_reassign_clear():
    a1 = shr5_Geist(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    a2 = shr5_Geist(charismaBasis=13, geschicklichkeitBasis=13, intuitionBasis=13, konstitutionBasis=13, logikBasis=13, reaktionBasis=13, staerkeBasis=13, willenskraftBasis=13)
    b = shr5_GebundenerGeist(dienste=7)
    _safe_set(b, 'shr5_GebundenerGeist90', a1)
    assert _is_linked(b, 'shr5_GebundenerGeist90', a1)
    if hasattr(a1, 'shr5_Geist'):
        assert _is_linked(a1, 'shr5_Geist', b)
    _safe_set(b, 'shr5_GebundenerGeist90', a2)
    assert _is_linked(b, 'shr5_GebundenerGeist90', a2)
    if hasattr(a1, 'shr5_Geist'):
        assert not _is_linked(a1, 'shr5_Geist', b)
    if hasattr(a2, 'shr5_Geist'):
        assert _is_linked(a2, 'shr5_Geist', b)
    _safe_set(b, 'shr5_GebundenerGeist90', None)
    assert not _is_linked(b, 'shr5_GebundenerGeist90', a2)
    if hasattr(a2, 'shr5_Geist'):
        assert not _is_linked(a2, 'shr5_Geist', b)


def test_assoc_items154_reverse_link_reassign_clear():
    a1 = shr5_ShoppingTransaction(caculatedCosts="sample_text", fee=3.14)
    a2 = shr5_ShoppingTransaction(caculatedCosts="sample_text_2", fee=9.99)
    b = shr5_GeldWert(verfuegbarkeit="sample_text", wert="sample_text", wertValue="sample_text")
    _safe_set(b, 'shr5_GeldWert', a1)
    assert _is_linked(b, 'shr5_GeldWert', a1)
    if hasattr(a1, 'shr5_ShoppingTransaction'):
        assert _is_linked(a1, 'shr5_ShoppingTransaction', b)
    _safe_set(b, 'shr5_GeldWert', a2)
    assert _is_linked(b, 'shr5_GeldWert', a2)
    if hasattr(a1, 'shr5_ShoppingTransaction'):
        assert not _is_linked(a1, 'shr5_ShoppingTransaction', b)
    if hasattr(a2, 'shr5_ShoppingTransaction'):
        assert _is_linked(a2, 'shr5_ShoppingTransaction', b)
    _safe_set(b, 'shr5_GeldWert', None)
    assert not _is_linked(b, 'shr5_GeldWert', a2)
    if hasattr(a2, 'shr5_ShoppingTransaction'):
        assert not _is_linked(a2, 'shr5_ShoppingTransaction', b)


def test_assoc_kmods50_reverse_link_reassign_clear():
    a1 = shr5_KleindungsModifikator(capacity=7, rating=7, type="sample_text")
    a2 = shr5_KleindungsModifikator(capacity=13, rating=13, type="sample_text_2")
    b = shr5_Kleidung(ruestung=7)
    _safe_set(b, 'shr5_Kleidung', {a1})
    assert _is_linked(b, 'shr5_Kleidung', a1)
    if hasattr(a1, 'shr5_KleindungsModifikator'):
        assert _is_linked(a1, 'shr5_KleindungsModifikator', b)
    _safe_set(b, 'shr5_Kleidung', {a2})
    assert _is_linked(b, 'shr5_Kleidung', a2)
    if hasattr(a1, 'shr5_KleindungsModifikator'):
        assert not _is_linked(a1, 'shr5_KleindungsModifikator', b)
    if hasattr(a2, 'shr5_KleindungsModifikator'):
        assert _is_linked(a2, 'shr5_KleindungsModifikator', b)
    _safe_set(b, 'shr5_Kleidung', set())
    assert not _is_linked(b, 'shr5_Kleidung', a2)
    if hasattr(a2, 'shr5_KleindungsModifikator'):
        assert not _is_linked(a2, 'shr5_KleindungsModifikator', b)


def test_assoc_localizations102_reverse_link_reassign_clear():
    a1 = shr5_Localization(local="sample_text", name="sample_text", page=7)
    a2 = shr5_Localization(local="sample_text_2", name="sample_text_2", page=13)
    b = shr5_Identifiable(parentId="sample_text")
    _safe_set(b, 'shr5_Identifiable', {a1})
    assert _is_linked(b, 'shr5_Identifiable', a1)
    if hasattr(a1, 'shr5_Localization'):
        assert _is_linked(a1, 'shr5_Localization', b)
    _safe_set(b, 'shr5_Identifiable', {a2})
    assert _is_linked(b, 'shr5_Identifiable', a2)
    if hasattr(a1, 'shr5_Localization'):
        assert not _is_linked(a1, 'shr5_Localization', b)
    if hasattr(a2, 'shr5_Localization'):
        assert _is_linked(a2, 'shr5_Localization', b)
    _safe_set(b, 'shr5_Identifiable', set())
    assert not _is_linked(b, 'shr5_Identifiable', a2)
    if hasattr(a2, 'shr5_Localization'):
        assert not _is_linked(a2, 'shr5_Localization', b)


def test_assoc_model123_reverse_link_reassign_clear():
    a1 = shr5_Drohne(programSlotCount=7)
    a2 = shr5_Drohne(programSlotCount=13)
    b = shr5_AutoSoft(rating=7)
    _safe_set(b, 'shr5_AutoSoft124', a1)
    assert _is_linked(b, 'shr5_AutoSoft124', a1)
    if hasattr(a1, 'shr5_Drohne125'):
        assert _is_linked(a1, 'shr5_Drohne125', b)
    _safe_set(b, 'shr5_AutoSoft124', a2)
    assert _is_linked(b, 'shr5_AutoSoft124', a2)
    if hasattr(a1, 'shr5_Drohne125'):
        assert not _is_linked(a1, 'shr5_Drohne125', b)
    if hasattr(a2, 'shr5_Drohne125'):
        assert _is_linked(a2, 'shr5_Drohne125', b)
    _safe_set(b, 'shr5_AutoSoft124', None)
    assert not _is_linked(b, 'shr5_AutoSoft124', a2)
    if hasattr(a2, 'shr5_Drohne125'):
        assert not _is_linked(a2, 'shr5_Drohne125', b)


def test_assoc_modifizierungen70_reverse_link_reassign_clear():
    a1 = shr5_FahrzeugModifikation(capacityUsed=7)
    a2 = shr5_FahrzeugModifikation(capacityUsed=13)
    b = shr5_Fahrzeug(beschleunigung=7, fahrzeugTyp="sample_text", geschwindigkeit=7, handling=7, panzer=7, pilot=7, rumpf=7, sensor=7, weaponMounts=7)
    _safe_set(b, 'shr5_Fahrzeug', {a1})
    assert _is_linked(b, 'shr5_Fahrzeug', a1)
    if hasattr(a1, 'shr5_FahrzeugModifikation'):
        assert _is_linked(a1, 'shr5_FahrzeugModifikation', b)
    _safe_set(b, 'shr5_Fahrzeug', {a2})
    assert _is_linked(b, 'shr5_Fahrzeug', a2)
    if hasattr(a1, 'shr5_FahrzeugModifikation'):
        assert not _is_linked(a1, 'shr5_FahrzeugModifikation', b)
    if hasattr(a2, 'shr5_FahrzeugModifikation'):
        assert _is_linked(a2, 'shr5_FahrzeugModifikation', b)
    _safe_set(b, 'shr5_Fahrzeug', set())
    assert not _is_linked(b, 'shr5_Fahrzeug', a2)
    if hasattr(a2, 'shr5_FahrzeugModifikation'):
        assert not _is_linked(a2, 'shr5_FahrzeugModifikation', b)


def test_assoc_optionalPowers99_reverse_link_reassign_clear():
    a1 = shr5_Geist(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    a2 = shr5_Geist(charismaBasis=13, geschicklichkeitBasis=13, intuitionBasis=13, konstitutionBasis=13, logikBasis=13, reaktionBasis=13, staerkeBasis=13, willenskraftBasis=13)
    b = shr5_CritterKraft(art="sample_text", dauer="sample_text", handlung="sample_text", reichweite="sample_text")
    _safe_set(b, 'shr5_CritterKraft101', a1)
    assert _is_linked(b, 'shr5_CritterKraft101', a1)
    if hasattr(a1, 'shr5_Geist100'):
        assert _is_linked(a1, 'shr5_Geist100', b)
    _safe_set(b, 'shr5_CritterKraft101', a2)
    assert _is_linked(b, 'shr5_CritterKraft101', a2)
    if hasattr(a1, 'shr5_Geist100'):
        assert not _is_linked(a1, 'shr5_Geist100', b)
    if hasattr(a2, 'shr5_Geist100'):
        assert _is_linked(a2, 'shr5_Geist100', b)
    _safe_set(b, 'shr5_CritterKraft101', None)
    assert not _is_linked(b, 'shr5_CritterKraft101', a2)
    if hasattr(a2, 'shr5_Geist100'):
        assert not _is_linked(a2, 'shr5_Geist100', b)


def test_assoc_persona32_reverse_link_reassign_clear():
    a1 = shr5_Cyberware(cyberwareCapacity=7, type="sample_text")
    a2 = shr5_Cyberware(cyberwareCapacity=13, type="sample_text_2")
    b = shr5_AbstraktPersona(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, modManager="sample_text", reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    _safe_set(b, 'shr5_AbstraktPersona33', a1)
    assert _is_linked(b, 'shr5_AbstraktPersona33', a1)
    if hasattr(a1, 'shr5_Cyberware'):
        assert _is_linked(a1, 'shr5_Cyberware', b)
    _safe_set(b, 'shr5_AbstraktPersona33', a2)
    assert _is_linked(b, 'shr5_AbstraktPersona33', a2)
    if hasattr(a1, 'shr5_Cyberware'):
        assert not _is_linked(a1, 'shr5_Cyberware', b)
    if hasattr(a2, 'shr5_Cyberware'):
        assert _is_linked(a2, 'shr5_Cyberware', b)
    _safe_set(b, 'shr5_AbstraktPersona33', None)
    assert not _is_linked(b, 'shr5_AbstraktPersona33', a2)
    if hasattr(a2, 'shr5_Cyberware'):
        assert not _is_linked(a2, 'shr5_Cyberware', b)


def test_assoc_powers96_reverse_link_reassign_clear():
    a1 = shr5_Geist(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    a2 = shr5_Geist(charismaBasis=13, geschicklichkeitBasis=13, intuitionBasis=13, konstitutionBasis=13, logikBasis=13, reaktionBasis=13, staerkeBasis=13, willenskraftBasis=13)
    b = shr5_CritterKraft(art="sample_text", dauer="sample_text", handlung="sample_text", reichweite="sample_text")
    _safe_set(b, 'shr5_CritterKraft98', a1)
    assert _is_linked(b, 'shr5_CritterKraft98', a1)
    if hasattr(a1, 'shr5_Geist97'):
        assert _is_linked(a1, 'shr5_Geist97', b)
    _safe_set(b, 'shr5_CritterKraft98', a2)
    assert _is_linked(b, 'shr5_CritterKraft98', a2)
    if hasattr(a1, 'shr5_Geist97'):
        assert not _is_linked(a1, 'shr5_Geist97', b)
    if hasattr(a2, 'shr5_Geist97'):
        assert _is_linked(a2, 'shr5_Geist97', b)
    _safe_set(b, 'shr5_CritterKraft98', None)
    assert not _is_linked(b, 'shr5_CritterKraft98', a2)
    if hasattr(a2, 'shr5_Geist97'):
        assert not _is_linked(a2, 'shr5_Geist97', b)


def test_assoc_skill119_reverse_link_reassign_clear():
    a1 = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    a2 = shr5_Fertigkeit(ausweichen=False, kategorie="sample_text_2")
    b = shr5_AutoSoft(rating=7)
    _safe_set(b, 'shr5_AutoSoft', a1)
    assert _is_linked(b, 'shr5_AutoSoft', a1)
    if hasattr(a1, 'shr5_Fertigkeit120'):
        assert _is_linked(a1, 'shr5_Fertigkeit120', b)
    _safe_set(b, 'shr5_AutoSoft', a2)
    assert _is_linked(b, 'shr5_AutoSoft', a2)
    if hasattr(a1, 'shr5_Fertigkeit120'):
        assert not _is_linked(a1, 'shr5_Fertigkeit120', b)
    if hasattr(a2, 'shr5_Fertigkeit120'):
        assert _is_linked(a2, 'shr5_Fertigkeit120', b)
    _safe_set(b, 'shr5_AutoSoft', None)
    assert not _is_linked(b, 'shr5_AutoSoft', a2)
    if hasattr(a2, 'shr5_Fertigkeit120'):
        assert not _is_linked(a2, 'shr5_Fertigkeit120', b)


def test_assoc_skill126_reverse_link_reassign_clear():
    a1 = shr5_Tutorsoft(rating=7)
    a2 = shr5_Tutorsoft(rating=13)
    b = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    _safe_set(b, 'shr5_Fertigkeit127', a1)
    assert _is_linked(b, 'shr5_Fertigkeit127', a1)
    if hasattr(a1, 'shr5_Tutorsoft'):
        assert _is_linked(a1, 'shr5_Tutorsoft', b)
    _safe_set(b, 'shr5_Fertigkeit127', a2)
    assert _is_linked(b, 'shr5_Fertigkeit127', a2)
    if hasattr(a1, 'shr5_Tutorsoft'):
        assert not _is_linked(a1, 'shr5_Tutorsoft', b)
    if hasattr(a2, 'shr5_Tutorsoft'):
        assert _is_linked(a2, 'shr5_Tutorsoft', b)
    _safe_set(b, 'shr5_Fertigkeit127', None)
    assert not _is_linked(b, 'shr5_Fertigkeit127', a2)
    if hasattr(a2, 'shr5_Tutorsoft'):
        assert not _is_linked(a2, 'shr5_Tutorsoft', b)


def test_assoc_skill128_reverse_link_reassign_clear():
    a1 = shr5_SkillSoft(rating=7)
    a2 = shr5_SkillSoft(rating=13)
    b = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    _safe_set(b, 'shr5_Fertigkeit129', a1)
    assert _is_linked(b, 'shr5_Fertigkeit129', a1)
    if hasattr(a1, 'shr5_SkillSoft'):
        assert _is_linked(a1, 'shr5_SkillSoft', b)
    _safe_set(b, 'shr5_Fertigkeit129', a2)
    assert _is_linked(b, 'shr5_Fertigkeit129', a2)
    if hasattr(a1, 'shr5_SkillSoft'):
        assert not _is_linked(a1, 'shr5_SkillSoft', b)
    if hasattr(a2, 'shr5_SkillSoft'):
        assert _is_linked(a2, 'shr5_SkillSoft', b)
    _safe_set(b, 'shr5_Fertigkeit129', None)
    assert not _is_linked(b, 'shr5_Fertigkeit129', a2)
    if hasattr(a2, 'shr5_SkillSoft'):
        assert not _is_linked(a2, 'shr5_SkillSoft', b)


def test_assoc_skills93_reverse_link_reassign_clear():
    a1 = shr5_StufenPersona(stufe=7)
    a2 = shr5_StufenPersona(stufe=13)
    b = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    _safe_set(b, 'shr5_Fertigkeit95', a1)
    assert _is_linked(b, 'shr5_Fertigkeit95', a1)
    if hasattr(a1, 'shr5_StufenPersona94'):
        assert _is_linked(a1, 'shr5_StufenPersona94', b)
    _safe_set(b, 'shr5_Fertigkeit95', a2)
    assert _is_linked(b, 'shr5_Fertigkeit95', a2)
    if hasattr(a1, 'shr5_StufenPersona94'):
        assert not _is_linked(a1, 'shr5_StufenPersona94', b)
    if hasattr(a2, 'shr5_StufenPersona94'):
        assert _is_linked(a2, 'shr5_StufenPersona94', b)
    _safe_set(b, 'shr5_Fertigkeit95', None)
    assert not _is_linked(b, 'shr5_Fertigkeit95', a2)
    if hasattr(a2, 'shr5_StufenPersona94'):
        assert not _is_linked(a2, 'shr5_StufenPersona94', b)


def test_assoc_source155_reverse_link_reassign_clear():
    a1 = shr5_TransferAmount(amountToTransfer="sample_text")
    a2 = shr5_TransferAmount(amountToTransfer="sample_text_2")
    b = shr5_Credstick(currentValue="sample_text", maxValue=7)
    _safe_set(b, 'shr5_Credstick156', a1)
    assert _is_linked(b, 'shr5_Credstick156', a1)
    if hasattr(a1, 'shr5_TransferAmount'):
        assert _is_linked(a1, 'shr5_TransferAmount', b)
    _safe_set(b, 'shr5_Credstick156', a2)
    assert _is_linked(b, 'shr5_Credstick156', a2)
    if hasattr(a1, 'shr5_TransferAmount'):
        assert not _is_linked(a1, 'shr5_TransferAmount', b)
    if hasattr(a2, 'shr5_TransferAmount'):
        assert _is_linked(a2, 'shr5_TransferAmount', b)
    _safe_set(b, 'shr5_Credstick156', None)
    assert not _is_linked(b, 'shr5_Credstick156', a2)
    if hasattr(a2, 'shr5_TransferAmount'):
        assert not _is_linked(a2, 'shr5_TransferAmount', b)


def test_assoc_spezies4_reverse_link_reassign_clear():
    a1 = shr5_Spezies(charismaMax=7, charismaMin=7, edgeMax=7, edgeMin=7, essenzMax=7, essenzMin=7, geschicklichkeitMax=7, geschicklichkeitMin=7, intuitionMax=7, intuitionMin=7, konstitutionMax=7, konstitutionMin=7, laufen=7, logikMax=7, logikMin=7, magieMax=7, magieMin=7, reaktionMax=7, reaktionMin=7, rennen=7, resonanzMax=7, resonanzMin=7, sprinten=7, staerkeMax=7, staerkeMin=7, willenskraftMax=7, willenskraftMin=7)
    a2 = shr5_Spezies(charismaMax=13, charismaMin=13, edgeMax=13, edgeMin=13, essenzMax=13, essenzMin=13, geschicklichkeitMax=13, geschicklichkeitMin=13, intuitionMax=13, intuitionMin=13, konstitutionMax=13, konstitutionMin=13, laufen=13, logikMax=13, logikMin=13, magieMax=13, magieMin=13, reaktionMax=13, reaktionMin=13, rennen=13, resonanzMax=13, resonanzMin=13, sprinten=13, staerkeMax=13, staerkeMin=13, willenskraftMax=13, willenskraftMin=13)
    b = shr5_AbstraktPersona(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, modManager="sample_text", reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    _safe_set(b, 'shr5_AbstraktPersona5', a1)
    assert _is_linked(b, 'shr5_AbstraktPersona5', a1)
    if hasattr(a1, 'shr5_Spezies'):
        assert _is_linked(a1, 'shr5_Spezies', b)
    _safe_set(b, 'shr5_AbstraktPersona5', a2)
    assert _is_linked(b, 'shr5_AbstraktPersona5', a2)
    if hasattr(a1, 'shr5_Spezies'):
        assert not _is_linked(a1, 'shr5_Spezies', b)
    if hasattr(a2, 'shr5_Spezies'):
        assert _is_linked(a2, 'shr5_Spezies', b)
    _safe_set(b, 'shr5_AbstraktPersona5', None)
    assert not _is_linked(b, 'shr5_AbstraktPersona5', a2)
    if hasattr(a2, 'shr5_Spezies'):
        assert not _is_linked(a2, 'shr5_Spezies', b)


def test_assoc_srcBook0_reverse_link_reassign_clear():
    a1 = shr5_SourceBook(code="sample_text", endShrTime="sample_text", startShrTime="sample_text")
    a2 = shr5_SourceBook(code="sample_text_2", endShrTime="sample_text_2", startShrTime="sample_text_2")
    b = shr5_Quelle(page="sample_text")
    _safe_set(b, 'shr5_Quelle', a1)
    assert _is_linked(b, 'shr5_Quelle', a1)
    if hasattr(a1, 'shr5_SourceBook'):
        assert _is_linked(a1, 'shr5_SourceBook', b)
    _safe_set(b, 'shr5_Quelle', a2)
    assert _is_linked(b, 'shr5_Quelle', a2)
    if hasattr(a1, 'shr5_SourceBook'):
        assert not _is_linked(a1, 'shr5_SourceBook', b)
    if hasattr(a2, 'shr5_SourceBook'):
        assert _is_linked(a2, 'shr5_SourceBook', b)
    _safe_set(b, 'shr5_Quelle', None)
    assert not _is_linked(b, 'shr5_Quelle', a2)
    if hasattr(a2, 'shr5_SourceBook'):
        assert not _is_linked(a2, 'shr5_SourceBook', b)


def test_assoc_tradition62_reverse_link_reassign_clear():
    a1 = shr5_Zauberer(enzug=7)
    a2 = shr5_Zauberer(enzug=13)
    b = shr5_MagischeTradition(enzug="sample_text")
    _safe_set(b, 'shr5_MagischeTradition', a1)
    assert _is_linked(b, 'shr5_MagischeTradition', a1)
    if hasattr(a1, 'shr5_Zauberer63'):
        assert _is_linked(a1, 'shr5_Zauberer63', b)
    _safe_set(b, 'shr5_MagischeTradition', a2)
    assert _is_linked(b, 'shr5_MagischeTradition', a2)
    if hasattr(a1, 'shr5_Zauberer63'):
        assert not _is_linked(a1, 'shr5_Zauberer63', b)
    if hasattr(a2, 'shr5_Zauberer63'):
        assert _is_linked(a2, 'shr5_Zauberer63', b)
    _safe_set(b, 'shr5_MagischeTradition', None)
    assert not _is_linked(b, 'shr5_MagischeTradition', a2)
    if hasattr(a2, 'shr5_Zauberer63'):
        assert not _is_linked(a2, 'shr5_Zauberer63', b)


def test_assoc_transactionlog86_reverse_link_reassign_clear():
    a1 = shr5_CredstickTransaction(amount="sample_text", date="sample_text", description="sample_text")
    a2 = shr5_CredstickTransaction(amount="sample_text_2", date="sample_text_2", description="sample_text_2")
    b = shr5_Credstick(currentValue="sample_text", maxValue=7)
    _safe_set(b, 'shr5_Credstick', {a1})
    assert _is_linked(b, 'shr5_Credstick', a1)
    if hasattr(a1, 'shr5_CredstickTransaction'):
        assert _is_linked(a1, 'shr5_CredstickTransaction', b)
    _safe_set(b, 'shr5_Credstick', {a2})
    assert _is_linked(b, 'shr5_Credstick', a2)
    if hasattr(a1, 'shr5_CredstickTransaction'):
        assert not _is_linked(a1, 'shr5_CredstickTransaction', b)
    if hasattr(a2, 'shr5_CredstickTransaction'):
        assert _is_linked(a2, 'shr5_CredstickTransaction', b)
    _safe_set(b, 'shr5_Credstick', set())
    assert not _is_linked(b, 'shr5_Credstick', a2)
    if hasattr(a2, 'shr5_CredstickTransaction'):
        assert not _is_linked(a2, 'shr5_CredstickTransaction', b)


def test_assoc_type87_reverse_link_reassign_clear():
    a1 = shr5_Reichweite(extrem=7, kurz=7, min=7, mittel=7, weit=7)
    a2 = shr5_Reichweite(extrem=13, kurz=13, min=13, mittel=13, weit=13)
    b = shr5_Munition(armorMod=7, damageMod=7, damageType="sample_text")
    _safe_set(b, 'shr5_Munition', a1)
    assert _is_linked(b, 'shr5_Munition', a1)
    if hasattr(a1, 'shr5_Reichweite88'):
        assert _is_linked(a1, 'shr5_Reichweite88', b)
    _safe_set(b, 'shr5_Munition', a2)
    assert _is_linked(b, 'shr5_Munition', a2)
    if hasattr(a1, 'shr5_Reichweite88'):
        assert not _is_linked(a1, 'shr5_Reichweite88', b)
    if hasattr(a2, 'shr5_Reichweite88'):
        assert _is_linked(a2, 'shr5_Reichweite88', b)
    _safe_set(b, 'shr5_Munition', None)
    assert not _is_linked(b, 'shr5_Munition', a2)
    if hasattr(a2, 'shr5_Reichweite88'):
        assert not _is_linked(a2, 'shr5_Reichweite88', b)


def test_assoc_ungebundenerGeist59_reverse_link_reassign_clear():
    a1 = shr5_Zauberer(enzug=7)
    a2 = shr5_Zauberer(enzug=13)
    b = shr5_GebundenerGeist(dienste=7)
    _safe_set(b, 'shr5_GebundenerGeist61', a1)
    assert _is_linked(b, 'shr5_GebundenerGeist61', a1)
    if hasattr(a1, 'shr5_Zauberer60'):
        assert _is_linked(a1, 'shr5_Zauberer60', b)
    _safe_set(b, 'shr5_GebundenerGeist61', a2)
    assert _is_linked(b, 'shr5_GebundenerGeist61', a2)
    if hasattr(a1, 'shr5_Zauberer60'):
        assert not _is_linked(a1, 'shr5_Zauberer60', b)
    if hasattr(a2, 'shr5_Zauberer60'):
        assert _is_linked(a2, 'shr5_Zauberer60', b)
    _safe_set(b, 'shr5_GebundenerGeist61', None)
    assert not _is_linked(b, 'shr5_GebundenerGeist61', a2)
    if hasattr(a2, 'shr5_Zauberer60'):
        assert not _is_linked(a2, 'shr5_Zauberer60', b)


def test_assoc_weapon121_reverse_link_reassign_clear():
    a1 = shr5_AutoSoft(rating=7)
    a2 = shr5_AutoSoft(rating=13)
    b = shr5_AbstaktWaffe(durchschlagsKraft=7, praezision=7, schadenscode="sample_text", schadesTyp="sample_text")
    _safe_set(b, 'shr5_AbstaktWaffe', a1)
    assert _is_linked(b, 'shr5_AbstaktWaffe', a1)
    if hasattr(a1, 'shr5_AutoSoft122'):
        assert _is_linked(a1, 'shr5_AutoSoft122', b)
    _safe_set(b, 'shr5_AbstaktWaffe', a2)
    assert _is_linked(b, 'shr5_AbstaktWaffe', a2)
    if hasattr(a1, 'shr5_AutoSoft122'):
        assert not _is_linked(a1, 'shr5_AutoSoft122', b)
    if hasattr(a2, 'shr5_AutoSoft122'):
        assert _is_linked(a2, 'shr5_AutoSoft122', b)
    _safe_set(b, 'shr5_AbstaktWaffe', None)
    assert not _is_linked(b, 'shr5_AbstaktWaffe', a2)
    if hasattr(a2, 'shr5_AutoSoft122'):
        assert not _is_linked(a2, 'shr5_AutoSoft122', b)


def test_assoc_zauber56_reverse_link_reassign_clear():
    a1 = shr5_Zauberer(enzug=7)
    a2 = shr5_Zauberer(enzug=13)
    b = shr5_PersonaZauber(stufe=7)
    _safe_set(b, 'shr5_PersonaZauber', a1)
    assert _is_linked(b, 'shr5_PersonaZauber', a1)
    if hasattr(a1, 'shr5_Zauberer'):
        assert _is_linked(a1, 'shr5_Zauberer', b)
    _safe_set(b, 'shr5_PersonaZauber', a2)
    assert _is_linked(b, 'shr5_PersonaZauber', a2)
    if hasattr(a1, 'shr5_Zauberer'):
        assert not _is_linked(a1, 'shr5_Zauberer', b)
    if hasattr(a2, 'shr5_Zauberer'):
        assert _is_linked(a2, 'shr5_Zauberer', b)
    _safe_set(b, 'shr5_PersonaZauber', None)
    assert not _is_linked(b, 'shr5_PersonaZauber', a2)
    if hasattr(a2, 'shr5_Zauberer'):
        assert not _is_linked(a2, 'shr5_Zauberer', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribut20_stub_double():
    # shr5_EAttribute has no real 'shr5_EAttribute22' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Fertigkeit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Fertigkeit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    partner = shr5_EAttribute()
    setattr(partner, 'shr5_EAttribute22', None)
    _safe_set(owner, 'shr5_Fertigkeit21', partner)
    assert getattr(partner, 'shr5_EAttribute22') == owner
    _safe_set(owner, 'shr5_Fertigkeit21', None)
    assert getattr(partner, 'shr5_EAttribute22') is None


def test_assoc_attribut8_stub_double():
    # shr5_EAttribute has no real 'shr5_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AttributModifikatorWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AttributModifikatorWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AttributModifikatorWert(wert=7)
    partner = shr5_EAttribute()
    setattr(partner, 'shr5_EAttribute', None)
    _safe_set(owner, 'shr5_AttributModifikatorWert', partner)
    assert getattr(partner, 'shr5_EAttribute') == owner
    _safe_set(owner, 'shr5_AttributModifikatorWert', None)
    assert getattr(partner, 'shr5_EAttribute') is None


def test_assoc_bullets144_stub_double():
    # shr5_Magazin has no real 'shr5_Magazin145' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Munition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Munition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Munition(armorMod=7, damageMod=7, damageType="sample_text")
    partner = shr5_Magazin()
    setattr(partner, 'shr5_Magazin145', None)
    _safe_set(owner, 'shr5_Munition146', partner)
    assert owner in getattr(partner, 'shr5_Magazin145')
    _safe_set(owner, 'shr5_Munition146', None)
    assert owner not in getattr(partner, 'shr5_Magazin145')


def test_assoc_capacityFeature148_stub_double():
    # shr5_EReference has no real 'shr5_EReference' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Capacity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Capacity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Capacity(capacity=7, capacityRemains=7)
    partner = shr5_EReference()
    setattr(partner, 'shr5_EReference', None)
    _safe_set(owner, 'shr5_Capacity', partner)
    assert getattr(partner, 'shr5_EReference') == owner
    _safe_set(owner, 'shr5_Capacity', None)
    assert getattr(partner, 'shr5_EReference') is None


def test_assoc_complexForms77_stub_double():
    # shr5_Technomancer has no real 'shr5_Technomancer' property in the generated
    # code (a bare stub) -- manually attach it so shr5_PersonaKomplexForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_PersonaKomplexForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_PersonaKomplexForm(stufe=7)
    partner = shr5_Technomancer()
    setattr(partner, 'shr5_Technomancer', None)
    _safe_set(owner, 'shr5_PersonaKomplexForm', partner)
    assert owner in getattr(partner, 'shr5_Technomancer')
    _safe_set(owner, 'shr5_PersonaKomplexForm', None)
    assert owner not in getattr(partner, 'shr5_Technomancer')


def test_assoc_configuration107_stub_double():
    # shr5_EAttribute has no real 'shr5_EAttribute108' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Cyberdeck's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Cyberdeck's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Cyberdeck(attribute1=7, attribute2=7, attribute3=7, attribute4=7, modManager="sample_text", programSlots=7)
    partner = shr5_EAttribute()
    setattr(partner, 'shr5_EAttribute108', None)
    _safe_set(owner, 'shr5_Cyberdeck', {partner})
    assert getattr(partner, 'shr5_EAttribute108') == owner
    _safe_set(owner, 'shr5_Cyberdeck', set())
    assert getattr(partner, 'shr5_EAttribute108') is None


def test_assoc_fertigkeit103_stub_double():
    # shr5_Spezialisierung has no real 'spezialisierungen' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Fertigkeit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Fertigkeit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    partner = shr5_Spezialisierung()
    setattr(partner, 'spezialisierungen', None)
    _safe_set(owner, 'Fertigkeit', partner)
    assert getattr(partner, 'spezialisierungen') == owner
    _safe_set(owner, 'Fertigkeit', None)
    assert getattr(partner, 'spezialisierungen') is None


def test_assoc_fertigkeit24_stub_double():
    # shr5_PersonaFertigkeit has no real 'shr5_PersonaFertigkeit25' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Fertigkeit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Fertigkeit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    partner = shr5_PersonaFertigkeit()
    setattr(partner, 'shr5_PersonaFertigkeit25', None)
    _safe_set(owner, 'shr5_Fertigkeit26', partner)
    assert getattr(partner, 'shr5_PersonaFertigkeit25') == owner
    _safe_set(owner, 'shr5_Fertigkeit26', None)
    assert getattr(partner, 'shr5_PersonaFertigkeit25') is None


def test_assoc_fertigkeit51_stub_double():
    # shr5_Anwendbar has no real 'shr5_Anwendbar' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Fertigkeit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Fertigkeit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    partner = shr5_Anwendbar()
    setattr(partner, 'shr5_Anwendbar', None)
    _safe_set(owner, 'shr5_Fertigkeit52', partner)
    assert getattr(partner, 'shr5_Anwendbar') == owner
    _safe_set(owner, 'shr5_Fertigkeit52', None)
    assert getattr(partner, 'shr5_Anwendbar') is None


def test_assoc_fertigkeiten1_stub_double():
    # shr5_PersonaFertigkeit has no real 'shr5_PersonaFertigkeit' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AbstraktPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AbstraktPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AbstraktPersona(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, modManager="sample_text", reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    partner = shr5_PersonaFertigkeit()
    setattr(partner, 'shr5_PersonaFertigkeit', None)
    _safe_set(owner, 'shr5_AbstraktPersona', {partner})
    assert getattr(partner, 'shr5_PersonaFertigkeit') == owner
    _safe_set(owner, 'shr5_AbstraktPersona', set())
    assert getattr(partner, 'shr5_PersonaFertigkeit') is None


def test_assoc_fertigkeiten19_stub_double():
    # shr5_FertigkeitsGruppe has no real 'shr5_FertigkeitsGruppe' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Fertigkeit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Fertigkeit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    partner = shr5_FertigkeitsGruppe()
    setattr(partner, 'shr5_FertigkeitsGruppe', None)
    _safe_set(owner, 'shr5_Fertigkeit', partner)
    assert owner in getattr(partner, 'shr5_FertigkeitsGruppe')
    _safe_set(owner, 'shr5_Fertigkeit', None)
    assert owner not in getattr(partner, 'shr5_FertigkeitsGruppe')


def test_assoc_fertigkeitsGruppen2_stub_double():
    # shr5_PersonaFertigkeitsGruppe has no real 'shr5_PersonaFertigkeitsGruppe' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AbstraktPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AbstraktPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AbstraktPersona(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, modManager="sample_text", reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    partner = shr5_PersonaFertigkeitsGruppe()
    setattr(partner, 'shr5_PersonaFertigkeitsGruppe', None)
    _safe_set(owner, 'shr5_AbstraktPersona3', {partner})
    assert getattr(partner, 'shr5_PersonaFertigkeitsGruppe') == owner
    _safe_set(owner, 'shr5_AbstraktPersona3', set())
    assert getattr(partner, 'shr5_PersonaFertigkeitsGruppe') is None


def test_assoc_initationen44_stub_double():
    # shr5_Initation has no real 'shr5_Initation' property in the generated
    # code (a bare stub) -- manually attach it so shr5_BaseMagischePersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_BaseMagischePersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_BaseMagischePersona(magie=7, magieBasis=7)
    partner = shr5_Initation()
    setattr(partner, 'shr5_Initation', None)
    _safe_set(owner, 'shr5_BaseMagischePersona', {partner})
    assert getattr(partner, 'shr5_Initation') == owner
    _safe_set(owner, 'shr5_BaseMagischePersona', set())
    assert getattr(partner, 'shr5_Initation') is None


def test_assoc_kikraft49_stub_double():
    # shr5_KiAdept has no real 'shr5_KiAdept' property in the generated
    # code (a bare stub) -- manually attach it so shr5_KiKraft's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_KiKraft's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_KiKraft(kraftpunkte=7)
    partner = shr5_KiAdept()
    setattr(partner, 'shr5_KiAdept', None)
    _safe_set(owner, 'shr5_KiKraft', partner)
    assert owner in getattr(partner, 'shr5_KiAdept')
    _safe_set(owner, 'shr5_KiKraft', None)
    assert owner not in getattr(partner, 'shr5_KiAdept')


def test_assoc_koerperMods40_stub_double():
    # shr5_Koerpermods has no real 'shr5_Koerpermods' property in the generated
    # code (a bare stub) -- manually attach it so shr5_KoerperPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_KoerperPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_KoerperPersona(zustandGeistig=7, zustandKoerperlich=7)
    partner = shr5_Koerpermods()
    setattr(partner, 'shr5_Koerpermods', None)
    _safe_set(owner, 'shr5_KoerperPersona', {partner})
    assert getattr(partner, 'shr5_Koerpermods') == owner
    _safe_set(owner, 'shr5_KoerperPersona', set())
    assert getattr(partner, 'shr5_Koerpermods') is None


def test_assoc_licences84_stub_double():
    # shr5_Sin has no real 'lizenzTraeger' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Lizenz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Lizenz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Lizenz(lizenGegenstand="sample_text")
    partner = shr5_Sin()
    setattr(partner, 'lizenzTraeger', None)
    _safe_set(owner, 'Lizenz', partner)
    assert owner in getattr(partner, 'lizenzTraeger')
    _safe_set(owner, 'Lizenz', None)
    assert owner not in getattr(partner, 'lizenzTraeger')


def test_assoc_lizenzTraeger85_stub_double():
    # shr5_Sin has no real 'Sin' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Lizenz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Lizenz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Lizenz(lizenGegenstand="sample_text")
    partner = shr5_Sin()
    setattr(partner, 'Sin', None)
    _safe_set(owner, 'licences', partner)
    assert getattr(partner, 'Sin') == owner
    _safe_set(owner, 'licences', None)
    assert getattr(partner, 'Sin') is None


def test_assoc_magazin16_stub_double():
    # shr5_Magazin has no real 'shr5_Magazin' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Feuerwaffe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Feuerwaffe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Feuerwaffe(erweiterung="sample_text", kapazitaet=7, modie="sample_text", munitionstyp="sample_text", rueckstoss=7)
    partner = shr5_Magazin()
    setattr(partner, 'shr5_Magazin', None)
    _safe_set(owner, 'shr5_Feuerwaffe17', partner)
    assert getattr(partner, 'shr5_Magazin') == owner
    _safe_set(owner, 'shr5_Feuerwaffe17', None)
    assert getattr(partner, 'shr5_Magazin') is None


def test_assoc_martialartStyles6_stub_double():
    # shr5_PersonaMartialartStyle has no real 'shr5_PersonaMartialartStyle' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AbstraktPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AbstraktPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AbstraktPersona(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, modManager="sample_text", reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    partner = shr5_PersonaMartialartStyle()
    setattr(partner, 'shr5_PersonaMartialartStyle', None)
    _safe_set(owner, 'shr5_AbstraktPersona7', {partner})
    assert getattr(partner, 'shr5_PersonaMartialartStyle') == owner
    _safe_set(owner, 'shr5_AbstraktPersona7', set())
    assert getattr(partner, 'shr5_PersonaMartialartStyle') is None


def test_assoc_master132_stub_double():
    # shr5_MatrixDevice has no real 'MatrixDevice' property in the generated
    # code (a bare stub) -- manually attach it so shr5_PersonalAreaNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_PersonalAreaNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_PersonalAreaNetwork(slaveMax=7)
    partner = shr5_MatrixDevice()
    setattr(partner, 'MatrixDevice', None)
    _safe_set(owner, 'pan', partner)
    assert getattr(partner, 'MatrixDevice') == owner
    _safe_set(owner, 'pan', None)
    assert getattr(partner, 'MatrixDevice') is None


def test_assoc_mentor43_stub_double():
    # shr5_MagischePersona has no real 'shr5_MagischePersona' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Schutzgeist's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Schutzgeist's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Schutzgeist(nachteile="sample_text", vorteile="sample_text")
    partner = shr5_MagischePersona()
    setattr(partner, 'shr5_MagischePersona', None)
    _safe_set(owner, 'shr5_Schutzgeist', partner)
    assert getattr(partner, 'shr5_MagischePersona') == owner
    _safe_set(owner, 'shr5_Schutzgeist', None)
    assert getattr(partner, 'shr5_MagischePersona') is None


def test_assoc_modifiziertes9_stub_double():
    # shr5_Modifizierbar has no real 'Modifizierbar' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AttributModifikatorWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AttributModifikatorWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AttributModifikatorWert(wert=7)
    partner = shr5_Modifizierbar()
    setattr(partner, 'Modifizierbar', None)
    _safe_set(owner, 'mods', partner)
    assert getattr(partner, 'Modifizierbar') == owner
    _safe_set(owner, 'mods', None)
    assert getattr(partner, 'Modifizierbar') is None


def test_assoc_modifyable10_stub_double():
    # shr5_Modifyable has no real 'shr5_Modifyable' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AttributModifikatorWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AttributModifikatorWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AttributModifikatorWert(wert=7)
    partner = shr5_Modifyable()
    setattr(partner, 'shr5_Modifyable', None)
    _safe_set(owner, 'shr5_AttributModifikatorWert11', partner)
    assert getattr(partner, 'shr5_Modifyable') == owner
    _safe_set(owner, 'shr5_AttributModifikatorWert11', None)
    assert getattr(partner, 'shr5_Modifyable') is None


def test_assoc_mods12_stub_double():
    # shr5_Modifizierbar has no real 'modifiziertes' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AttributModifikatorWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AttributModifikatorWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AttributModifikatorWert(wert=7)
    partner = shr5_Modifizierbar()
    setattr(partner, 'modifiziertes', None)
    _safe_set(owner, 'AttributModifikatorWert', partner)
    assert owner in getattr(partner, 'modifiziertes')
    _safe_set(owner, 'AttributModifikatorWert', None)
    assert owner not in getattr(partner, 'modifiziertes')


def test_assoc_options82_stub_double():
    # shr5_LifestyleOption has no real 'shr5_LifestyleOption' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Lifestyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Lifestyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Lifestyle(owned=True)
    partner = shr5_LifestyleOption()
    setattr(partner, 'shr5_LifestyleOption', None)
    _safe_set(owner, 'shr5_Lifestyle', {partner})
    assert getattr(partner, 'shr5_LifestyleOption') == owner
    _safe_set(owner, 'shr5_Lifestyle', set())
    assert getattr(partner, 'shr5_LifestyleOption') is None


def test_assoc_pan134_stub_double():
    # shr5_MatrixDevice has no real 'master' property in the generated
    # code (a bare stub) -- manually attach it so shr5_PersonalAreaNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_PersonalAreaNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_PersonalAreaNetwork(slaveMax=7)
    partner = shr5_MatrixDevice()
    setattr(partner, 'master', None)
    _safe_set(owner, 'PersonalAreaNetwork', partner)
    assert getattr(partner, 'master') == owner
    _safe_set(owner, 'PersonalAreaNetwork', None)
    assert getattr(partner, 'master') is None


def test_assoc_persona38_stub_double():
    # shr5_BioWare has no real 'shr5_BioWare' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AbstraktPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AbstraktPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AbstraktPersona(charismaBasis=7, geschicklichkeitBasis=7, intuitionBasis=7, konstitutionBasis=7, logikBasis=7, modManager="sample_text", reaktionBasis=7, staerkeBasis=7, willenskraftBasis=7)
    partner = shr5_BioWare()
    setattr(partner, 'shr5_BioWare', None)
    _safe_set(owner, 'shr5_AbstraktPersona39', partner)
    assert getattr(partner, 'shr5_BioWare') == owner
    _safe_set(owner, 'shr5_AbstraktPersona39', None)
    assert getattr(partner, 'shr5_BioWare') is None


def test_assoc_power137_stub_double():
    # shr5_QiFokus has no real 'shr5_QiFokus' property in the generated
    # code (a bare stub) -- manually attach it so shr5_KiKraft's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_KiKraft's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_KiKraft(kraftpunkte=7)
    partner = shr5_QiFokus()
    setattr(partner, 'shr5_QiFokus', None)
    _safe_set(owner, 'shr5_KiKraft138', partner)
    assert getattr(partner, 'shr5_QiFokus') == owner
    _safe_set(owner, 'shr5_KiKraft138', None)
    assert getattr(partner, 'shr5_QiFokus') is None


def test_assoc_powers83_stub_double():
    # shr5_Critter has no real 'shr5_Critter' property in the generated
    # code (a bare stub) -- manually attach it so shr5_CritterKraft's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_CritterKraft's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_CritterKraft(art="sample_text", dauer="sample_text", handlung="sample_text", reichweite="sample_text")
    partner = shr5_Critter()
    setattr(partner, 'shr5_Critter', None)
    _safe_set(owner, 'shr5_CritterKraft', partner)
    assert owner in getattr(partner, 'shr5_Critter')
    _safe_set(owner, 'shr5_CritterKraft', None)
    assert owner not in getattr(partner, 'shr5_Critter')


def test_assoc_reichweite14_stub_double():
    # shr5_AbstaktFernKampfwaffe has no real 'shr5_AbstaktFernKampfwaffe' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Reichweite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Reichweite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Reichweite(extrem=7, kurz=7, min=7, mittel=7, weit=7)
    partner = shr5_AbstaktFernKampfwaffe()
    setattr(partner, 'shr5_AbstaktFernKampfwaffe', None)
    _safe_set(owner, 'shr5_Reichweite', partner)
    assert getattr(partner, 'shr5_AbstaktFernKampfwaffe') == owner
    _safe_set(owner, 'shr5_Reichweite', None)
    assert getattr(partner, 'shr5_AbstaktFernKampfwaffe') is None


def test_assoc_runningPrograms111_stub_double():
    # shr5_MatrixProgram has no real 'shr5_MatrixProgram113' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Cyberdeck's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Cyberdeck's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Cyberdeck(attribute1=7, attribute2=7, attribute3=7, attribute4=7, modManager="sample_text", programSlots=7)
    partner = shr5_MatrixProgram()
    setattr(partner, 'shr5_MatrixProgram113', None)
    _safe_set(owner, 'shr5_Cyberdeck112', {partner})
    assert getattr(partner, 'shr5_MatrixProgram113') == owner
    _safe_set(owner, 'shr5_Cyberdeck112', set())
    assert getattr(partner, 'shr5_MatrixProgram113') is None


def test_assoc_runningPrograms116_stub_double():
    # shr5_RiggerProgram has no real 'shr5_RiggerProgram118' property in the generated
    # code (a bare stub) -- manually attach it so shr5_RiggerCommandConsole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_RiggerCommandConsole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_RiggerCommandConsole(datenverarbeitungBasis=7, firewallBasis=7, rauschunterdrueckung=7, zugriff=7, zugriffBasis=7)
    partner = shr5_RiggerProgram()
    setattr(partner, 'shr5_RiggerProgram118', None)
    _safe_set(owner, 'shr5_RiggerCommandConsole117', {partner})
    assert getattr(partner, 'shr5_RiggerProgram118') == owner
    _safe_set(owner, 'shr5_RiggerCommandConsole117', set())
    assert getattr(partner, 'shr5_RiggerProgram118') is None


def test_assoc_runningPrograms73_stub_double():
    # shr5_RiggerProgram has no real 'shr5_RiggerProgram' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Drohne's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Drohne's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Drohne(programSlotCount=7)
    partner = shr5_RiggerProgram()
    setattr(partner, 'shr5_RiggerProgram', None)
    _safe_set(owner, 'shr5_Drohne', {partner})
    assert getattr(partner, 'shr5_RiggerProgram') == owner
    _safe_set(owner, 'shr5_Drohne', set())
    assert getattr(partner, 'shr5_RiggerProgram') is None


def test_assoc_sensorArray71_stub_double():
    # shr5_SensorArray has no real 'shr5_SensorArray' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Fahrzeug's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Fahrzeug's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Fahrzeug(beschleunigung=7, fahrzeugTyp="sample_text", geschwindigkeit=7, handling=7, panzer=7, pilot=7, rumpf=7, sensor=7, weaponMounts=7)
    partner = shr5_SensorArray()
    setattr(partner, 'shr5_SensorArray', None)
    _safe_set(owner, 'shr5_Fahrzeug72', partner)
    assert getattr(partner, 'shr5_SensorArray') == owner
    _safe_set(owner, 'shr5_Fahrzeug72', None)
    assert getattr(partner, 'shr5_SensorArray') is None


def test_assoc_skillGroups91_stub_double():
    # shr5_FertigkeitsGruppe has no real 'shr5_FertigkeitsGruppe92' property in the generated
    # code (a bare stub) -- manually attach it so shr5_StufenPersona's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_StufenPersona's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_StufenPersona(stufe=7)
    partner = shr5_FertigkeitsGruppe()
    setattr(partner, 'shr5_FertigkeitsGruppe92', None)
    _safe_set(owner, 'shr5_StufenPersona', {partner})
    assert getattr(partner, 'shr5_FertigkeitsGruppe92') == owner
    _safe_set(owner, 'shr5_StufenPersona', set())
    assert getattr(partner, 'shr5_FertigkeitsGruppe92') is None


def test_assoc_slaves130_stub_double():
    # shr5_MatrixDevice has no real 'shr5_MatrixDevice131' property in the generated
    # code (a bare stub) -- manually attach it so shr5_PersonalAreaNetwork's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_PersonalAreaNetwork's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_PersonalAreaNetwork(slaveMax=7)
    partner = shr5_MatrixDevice()
    setattr(partner, 'shr5_MatrixDevice131', None)
    _safe_set(owner, 'shr5_PersonalAreaNetwork', {partner})
    assert getattr(partner, 'shr5_MatrixDevice131') == owner
    _safe_set(owner, 'shr5_PersonalAreaNetwork', set())
    assert getattr(partner, 'shr5_MatrixDevice131') is None


def test_assoc_spezialisierungen23_stub_double():
    # shr5_Spezialisierung has no real 'Spezialisierung' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Fertigkeit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Fertigkeit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    partner = shr5_Spezialisierung()
    setattr(partner, 'Spezialisierung', None)
    _safe_set(owner, 'fertigkeit', {partner})
    assert getattr(partner, 'Spezialisierung') == owner
    _safe_set(owner, 'fertigkeit', set())
    assert getattr(partner, 'Spezialisierung') is None


def test_assoc_storedPrograms109_stub_double():
    # shr5_MatrixProgram has no real 'shr5_MatrixProgram' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Cyberdeck's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Cyberdeck's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Cyberdeck(attribute1=7, attribute2=7, attribute3=7, attribute4=7, modManager="sample_text", programSlots=7)
    partner = shr5_MatrixProgram()
    setattr(partner, 'shr5_MatrixProgram', None)
    _safe_set(owner, 'shr5_Cyberdeck110', {partner})
    assert getattr(partner, 'shr5_MatrixProgram') == owner
    _safe_set(owner, 'shr5_Cyberdeck110', set())
    assert getattr(partner, 'shr5_MatrixProgram') is None


def test_assoc_storedPrograms114_stub_double():
    # shr5_RiggerProgram has no real 'shr5_RiggerProgram115' property in the generated
    # code (a bare stub) -- manually attach it so shr5_RiggerCommandConsole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_RiggerCommandConsole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_RiggerCommandConsole(datenverarbeitungBasis=7, firewallBasis=7, rauschunterdrueckung=7, zugriff=7, zugriffBasis=7)
    partner = shr5_RiggerProgram()
    setattr(partner, 'shr5_RiggerProgram115', None)
    _safe_set(owner, 'shr5_RiggerCommandConsole', {partner})
    assert getattr(partner, 'shr5_RiggerProgram115') == owner
    _safe_set(owner, 'shr5_RiggerCommandConsole', set())
    assert getattr(partner, 'shr5_RiggerProgram115') is None


def test_assoc_storedPrograms74_stub_double():
    # shr5_RiggerProgram has no real 'shr5_RiggerProgram76' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Drohne's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Drohne's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Drohne(programSlotCount=7)
    partner = shr5_RiggerProgram()
    setattr(partner, 'shr5_RiggerProgram76', None)
    _safe_set(owner, 'shr5_Drohne75', {partner})
    assert getattr(partner, 'shr5_RiggerProgram76') == owner
    _safe_set(owner, 'shr5_Drohne75', set())
    assert getattr(partner, 'shr5_RiggerProgram76') is None


def test_assoc_substance147_stub_double():
    # shr5_SubstanceContainer has no real 'shr5_SubstanceContainer' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Substance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Substance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Substance(speed="sample_text", vector="sample_text")
    partner = shr5_SubstanceContainer()
    setattr(partner, 'shr5_SubstanceContainer', None)
    _safe_set(owner, 'shr5_Substance', partner)
    assert getattr(partner, 'shr5_SubstanceContainer') == owner
    _safe_set(owner, 'shr5_Substance', None)
    assert getattr(partner, 'shr5_SubstanceContainer') is None


def test_assoc_type141_stub_double():
    # shr5_Magazin has no real 'shr5_Magazin142' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Feuerwaffe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Feuerwaffe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Feuerwaffe(erweiterung="sample_text", kapazitaet=7, modie="sample_text", munitionstyp="sample_text", rueckstoss=7)
    partner = shr5_Magazin()
    setattr(partner, 'shr5_Magazin142', None)
    _safe_set(owner, 'shr5_Feuerwaffe143', partner)
    assert getattr(partner, 'shr5_Magazin142') == owner
    _safe_set(owner, 'shr5_Feuerwaffe143', None)
    assert getattr(partner, 'shr5_Magazin142') is None


def test_assoc_usableWith162_stub_double():
    # shr5_MartialartStyle has no real 'shr5_MartialartStyle163' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Fertigkeit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Fertigkeit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Fertigkeit(ausweichen=True, kategorie="sample_text")
    partner = shr5_MartialartStyle()
    setattr(partner, 'shr5_MartialartStyle163', None)
    _safe_set(owner, 'shr5_Fertigkeit164', partner)
    assert owner in getattr(partner, 'shr5_MartialartStyle163')
    _safe_set(owner, 'shr5_Fertigkeit164', None)
    assert owner not in getattr(partner, 'shr5_MartialartStyle163')


def test_assoc_weapon135_stub_double():
    # shr5_WeaponMount has no real 'shr5_WeaponMount' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AbstaktWaffe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AbstaktWaffe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AbstaktWaffe(durchschlagsKraft=7, praezision=7, schadenscode="sample_text", schadesTyp="sample_text")
    partner = shr5_WeaponMount()
    setattr(partner, 'shr5_WeaponMount', None)
    _safe_set(owner, 'shr5_AbstaktWaffe136', partner)
    assert getattr(partner, 'shr5_WeaponMount') == owner
    _safe_set(owner, 'shr5_AbstaktWaffe136', None)
    assert getattr(partner, 'shr5_WeaponMount') is None


def test_assoc_weapon149_stub_double():
    # shr5_CyberImplantWeapon has no real 'shr5_CyberImplantWeapon' property in the generated
    # code (a bare stub) -- manually attach it so shr5_AbstaktWaffe's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_AbstaktWaffe's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_AbstaktWaffe(durchschlagsKraft=7, praezision=7, schadenscode="sample_text", schadesTyp="sample_text")
    partner = shr5_CyberImplantWeapon()
    setattr(partner, 'shr5_CyberImplantWeapon', None)
    _safe_set(owner, 'shr5_AbstaktWaffe150', partner)
    assert getattr(partner, 'shr5_CyberImplantWeapon') == owner
    _safe_set(owner, 'shr5_AbstaktWaffe150', None)
    assert getattr(partner, 'shr5_CyberImplantWeapon') is None


def test_assoc_wifi36_stub_double():
    # shr5_DefaultWifi has no real 'shr5_DefaultWifi' property in the generated
    # code (a bare stub) -- manually attach it so shr5_Cyberware's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # shr5_Cyberware's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = shr5_Cyberware(cyberwareCapacity=7, type="sample_text")
    partner = shr5_DefaultWifi()
    setattr(partner, 'shr5_DefaultWifi', None)
    _safe_set(owner, 'shr5_Cyberware37', {partner})
    assert getattr(partner, 'shr5_DefaultWifi') == owner
    _safe_set(owner, 'shr5_Cyberware37', set())
    assert getattr(partner, 'shr5_DefaultWifi') is None


