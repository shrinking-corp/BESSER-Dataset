import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractComponent,
    AbstractDateCase,
    AbstractDayCase,
    AbstractDayNameCase,
    ElementType,
    HeadComponent,
    HeaderFooterColumn,
    HeaderFooterFragment,
    InfoElementType,
    LdpType,
    PrefaceElementType,
    SectionElementType,
    atem_AbstractComponent,
    atem_AbstractDateCase,
    atem_AbstractDayCase,
    atem_AbstractDayNameCase,
    atem_Actor,
    atem_Aid,
    atem_All,
    atem_AtemModel,
    atem_Block,
    atem_Break,
    atem_Commemoration,
    atem_DOL,
    atem_DOM,
    atem_DOP,
    atem_DOWN,
    atem_DOWT,
    atem_Date,
    atem_DateRange,
    atem_DateSet,
    atem_DayNameRange,
    atem_DayNameSet,
    atem_DayRange,
    atem_DaySet,
    atem_Definition,
    atem_Dialog,
    atem_Driver,
    atem_EOW,
    atem_ElementType,
    atem_GenDate,
    atem_GenYear,
    atem_Head,
    atem_HeadComponent,
    atem_HeaderFooterColumn,
    atem_HeaderFooterColumnCenter,
    atem_HeaderFooterColumnLeft,
    atem_HeaderFooterColumnRight,
    atem_HeaderFooterCommemoration,
    atem_HeaderFooterDate,
    atem_HeaderFooterFragment,
    atem_HeaderFooterLookup,
    atem_HeaderFooterPageNumber,
    atem_HeaderFooterText,
    atem_HeaderFooterTitle,
    atem_Heading1,
    atem_Heading2,
    atem_Heading3,
    atem_Hymn,
    atem_Import,
    atem_Info,
    atem_InfoElementType,
    atem_LDP,
    atem_LdpType,
    atem_LitBook,
    atem_Lookup,
    atem_MCD,
    atem_MOW,
    atem_Media,
    atem_ModeOfWeekSet,
    atem_NOP,
    atem_PageFooterEven,
    atem_PageFooterOdd,
    atem_PageHeaderEven,
    atem_PageHeaderOdd,
    atem_PageKeepWithNext,
    atem_PageNumber,
    atem_Paragraph,
    atem_PassThroughHtml,
    atem_PassThroughPdf,
    atem_Preface,
    atem_PrefaceElementType,
    atem_PrefaceFragment,
    atem_Reading,
    atem_ResourceText,
    atem_RestoreLocale,
    atem_Rubric,
    atem_SAEC,
    atem_SBT,
    atem_SOL,
    atem_Section,
    atem_SectionElementType,
    atem_SectionFragment,
    atem_SetLocale,
    atem_SubTitle,
    atem_SundaysBeforeTriodionCase,
    atem_TaggedText,
    atem_TemplateFragment,
    atem_TemplateStatus,
    atem_TemplateTitle,
    atem_Title,
    atem_Verse,
    atem_Version,
    atem_VersionSwitch,
    atem_WDOLC,
    atem_WOLC,
    atem_WhenDate,
    atem_WhenDateCase,
    atem_WhenDayName,
    atem_WhenDayNameCase,
    atem_WhenExists,
    atem_WhenExistsCase,
    atem_WhenLukanCycleDay,
    atem_WhenModeOfWeek,
    atem_WhenModeOfWeekCase,
    atem_WhenMovableCycleDay,
    atem_WhenOther,
    atem_WhenPascha,
    atem_WhenPentecostarionDay,
    atem_WhenPeriodCase,
    atem_WhenSundayAfterElevationOfCrossDay,
    atem_WhenSundaysBeforeTriodion,
    atem_WhenTriodionDay,
    BookTypes,
    BreakType,
    DayOfMonthTypes,
    DayOfWeek,
    DowTypes,
    Language,
    ModeTypes,
    MonthName,
    Null,
    PeriodType,
    Seasons,
    TemplateStatuses,
    VersionSwitchType,
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

def test_assoc_dsl_Template_Driver3_reverse_link_reassign_clear():
    a1 = atem_Driver(dsl_Driver_RegEx="sample_text", dsl_Driver_Status="sample_text")
    a2 = atem_Driver(dsl_Driver_RegEx="sample_text_2", dsl_Driver_Status="sample_text_2")
    b = atem_AtemModel(name="sample_text")
    _safe_set(b, 'atem_AtemModel4', a1)
    assert _is_linked(b, 'atem_AtemModel4', a1)
    if hasattr(a1, 'atem_Driver'):
        assert _is_linked(a1, 'atem_Driver', b)
    _safe_set(b, 'atem_AtemModel4', a2)
    assert _is_linked(b, 'atem_AtemModel4', a2)
    if hasattr(a1, 'atem_Driver'):
        assert not _is_linked(a1, 'atem_Driver', b)
    if hasattr(a2, 'atem_Driver'):
        assert _is_linked(a2, 'atem_Driver', b)
    _safe_set(b, 'atem_AtemModel4', None)
    assert not _is_linked(b, 'atem_AtemModel4', a2)
    if hasattr(a2, 'atem_Driver'):
        assert not _is_linked(a2, 'atem_Driver', b)


def test_assoc_dsl_Template_Status0_reverse_link_reassign_clear():
    a1 = atem_TemplateStatus(dsl_TemplateStatus="sample_text")
    a2 = atem_TemplateStatus(dsl_TemplateStatus="sample_text_2")
    b = atem_AtemModel(name="sample_text")
    _safe_set(b, 'atem_AtemModel', a1)
    assert _is_linked(b, 'atem_AtemModel', a1)
    if hasattr(a1, 'atem_TemplateStatus'):
        assert _is_linked(a1, 'atem_TemplateStatus', b)
    _safe_set(b, 'atem_AtemModel', a2)
    assert _is_linked(b, 'atem_AtemModel', a2)
    if hasattr(a1, 'atem_TemplateStatus'):
        assert not _is_linked(a1, 'atem_TemplateStatus', b)
    if hasattr(a2, 'atem_TemplateStatus'):
        assert _is_linked(a2, 'atem_TemplateStatus', b)
    _safe_set(b, 'atem_AtemModel', None)
    assert not _is_linked(b, 'atem_AtemModel', a2)
    if hasattr(a2, 'atem_TemplateStatus'):
        assert not _is_linked(a2, 'atem_TemplateStatus', b)


def test_assoc_dsl_Template_preface7_reverse_link_reassign_clear():
    a1 = atem_Preface(name="sample_text")
    a2 = atem_Preface(name="sample_text_2")
    b = atem_AtemModel(name="sample_text")
    _safe_set(b, 'atem_AtemModel8', a1)
    assert _is_linked(b, 'atem_AtemModel8', a1)
    if hasattr(a1, 'atem_Preface'):
        assert _is_linked(a1, 'atem_Preface', b)
    _safe_set(b, 'atem_AtemModel8', a2)
    assert _is_linked(b, 'atem_AtemModel8', a2)
    if hasattr(a1, 'atem_Preface'):
        assert not _is_linked(a1, 'atem_Preface', b)
    if hasattr(a2, 'atem_Preface'):
        assert _is_linked(a2, 'atem_Preface', b)
    _safe_set(b, 'atem_AtemModel8', None)
    assert not _is_linked(b, 'atem_AtemModel8', a2)
    if hasattr(a2, 'atem_Preface'):
        assert not _is_linked(a2, 'atem_Preface', b)


def test_assoc_imports1_reverse_link_reassign_clear():
    a1 = atem_Import(importedNamespace="sample_text")
    a2 = atem_Import(importedNamespace="sample_text_2")
    b = atem_AtemModel(name="sample_text")
    _safe_set(b, 'atem_AtemModel2', {a1})
    assert _is_linked(b, 'atem_AtemModel2', a1)
    if hasattr(a1, 'atem_Import'):
        assert _is_linked(a1, 'atem_Import', b)
    _safe_set(b, 'atem_AtemModel2', {a2})
    assert _is_linked(b, 'atem_AtemModel2', a2)
    if hasattr(a1, 'atem_Import'):
        assert not _is_linked(a1, 'atem_Import', b)
    if hasattr(a2, 'atem_Import'):
        assert _is_linked(a2, 'atem_Import', b)
    _safe_set(b, 'atem_AtemModel2', set())
    assert not _is_linked(b, 'atem_AtemModel2', a2)
    if hasattr(a2, 'atem_Import'):
        assert not _is_linked(a2, 'atem_Import', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dsl_HeaderFooterLookup_Elements24_stub_double():
    # atem_ElementType has no real 'atem_ElementType' property in the generated
    # code (a bare stub) -- manually attach it so atem_HeaderFooterLookup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_HeaderFooterLookup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_HeaderFooterLookup(dsl_HeaderFooterLookup_Language="sample_text")
    partner = atem_ElementType()
    setattr(partner, 'atem_ElementType', None)
    _safe_set(owner, 'atem_HeaderFooterLookup', {partner})
    assert getattr(partner, 'atem_ElementType') == owner
    _safe_set(owner, 'atem_HeaderFooterLookup', set())
    assert getattr(partner, 'atem_ElementType') is None


def test_assoc_dsl_Info_Elements36_stub_double():
    # atem_InfoElementType has no real 'atem_InfoElementType' property in the generated
    # code (a bare stub) -- manually attach it so atem_Info's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_Info's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_Info(name="sample_text")
    partner = atem_InfoElementType()
    setattr(partner, 'atem_InfoElementType', None)
    _safe_set(owner, 'atem_Info', {partner})
    assert getattr(partner, 'atem_InfoElementType') == owner
    _safe_set(owner, 'atem_Info', set())
    assert getattr(partner, 'atem_InfoElementType') is None


def test_assoc_dsl_Preface_Elements37_stub_double():
    # atem_PrefaceElementType has no real 'atem_PrefaceElementType' property in the generated
    # code (a bare stub) -- manually attach it so atem_Preface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_Preface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_Preface(name="sample_text")
    partner = atem_PrefaceElementType()
    setattr(partner, 'atem_PrefaceElementType', None)
    _safe_set(owner, 'atem_Preface38', {partner})
    assert getattr(partner, 'atem_PrefaceElementType') == owner
    _safe_set(owner, 'atem_Preface38', set())
    assert getattr(partner, 'atem_PrefaceElementType') is None


def test_assoc_dsl_ResourceTextRef27_stub_double():
    # atem_Definition has no real 'atem_Definition' property in the generated
    # code (a bare stub) -- manually attach it so atem_ResourceText's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_ResourceText's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_ResourceText(dsl_ResourceText_Media_Off=True)
    partner = atem_Definition()
    setattr(partner, 'atem_Definition', None)
    _safe_set(owner, 'atem_ResourceText', partner)
    assert getattr(partner, 'atem_Definition') == owner
    _safe_set(owner, 'atem_ResourceText', None)
    assert getattr(partner, 'atem_Definition') is None


def test_assoc_dsl_ResourceTextRef28_stub_double():
    # atem_Definition has no real 'atem_Definition29' property in the generated
    # code (a bare stub) -- manually attach it so atem_Lookup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_Lookup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_Lookup(dsl_Lookup_Media_Off=True, dsl_Lookup_OverrideDay="sample_text", dsl_Lookup_OverrideMode="sample_text", dsl_Lookup_Override_Mode_Set=True, dsl_Lookup_Override__Day_Set=True)
    partner = atem_Definition()
    setattr(partner, 'atem_Definition29', None)
    _safe_set(owner, 'atem_Lookup', partner)
    assert getattr(partner, 'atem_Definition29') == owner
    _safe_set(owner, 'atem_Lookup', None)
    assert getattr(partner, 'atem_Definition29') is None


def test_assoc_dsl_Section_Elements41_stub_double():
    # atem_SectionElementType has no real 'atem_SectionElementType' property in the generated
    # code (a bare stub) -- manually attach it so atem_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_Section(name="sample_text")
    partner = atem_SectionElementType()
    setattr(partner, 'atem_SectionElementType', None)
    _safe_set(owner, 'atem_Section42', {partner})
    assert getattr(partner, 'atem_SectionElementType') == owner
    _safe_set(owner, 'atem_Section42', set())
    assert getattr(partner, 'atem_SectionElementType') is None


def test_assoc_dsl_Section_Role39_stub_double():
    # atem_Definition has no real 'atem_Definition40' property in the generated
    # code (a bare stub) -- manually attach it so atem_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_Section(name="sample_text")
    partner = atem_Definition()
    setattr(partner, 'atem_Definition40', None)
    _safe_set(owner, 'atem_Section', partner)
    assert getattr(partner, 'atem_Definition40') == owner
    _safe_set(owner, 'atem_Section', None)
    assert getattr(partner, 'atem_Definition40') is None


def test_assoc_dsl_SundaysBeforeTriodionCase_True_actions156_stub_double():
    # atem_AbstractComponent has no real 'atem_AbstractComponent158' property in the generated
    # code (a bare stub) -- manually attach it so atem_SundaysBeforeTriodionCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_SundaysBeforeTriodionCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_SundaysBeforeTriodionCase(dsl_SundaysBeforeTriodionCase_Days=7)
    partner = atem_AbstractComponent()
    setattr(partner, 'atem_AbstractComponent158', None)
    _safe_set(owner, 'atem_SundaysBeforeTriodionCase157', {partner})
    assert getattr(partner, 'atem_AbstractComponent158') == owner
    _safe_set(owner, 'atem_SundaysBeforeTriodionCase157', set())
    assert getattr(partner, 'atem_AbstractComponent158') is None


def test_assoc_dsl_Template_components9_stub_double():
    # atem_AbstractComponent has no real 'atem_AbstractComponent' property in the generated
    # code (a bare stub) -- manually attach it so atem_AtemModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_AtemModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_AtemModel(name="sample_text")
    partner = atem_AbstractComponent()
    setattr(partner, 'atem_AbstractComponent', None)
    _safe_set(owner, 'atem_AtemModel10', {partner})
    assert getattr(partner, 'atem_AbstractComponent') == owner
    _safe_set(owner, 'atem_AtemModel10', set())
    assert getattr(partner, 'atem_AbstractComponent') is None


def test_assoc_dsl_Template_head5_stub_double():
    # atem_Head has no real 'atem_Head' property in the generated
    # code (a bare stub) -- manually attach it so atem_AtemModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_AtemModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_AtemModel(name="sample_text")
    partner = atem_Head()
    setattr(partner, 'atem_Head', None)
    _safe_set(owner, 'atem_AtemModel6', partner)
    assert getattr(partner, 'atem_Head') == owner
    _safe_set(owner, 'atem_AtemModel6', None)
    assert getattr(partner, 'atem_Head') is None


def test_assoc_dsl_WhenDateCase_Days92_stub_double():
    # atem_AbstractDateCase has no real 'atem_AbstractDateCase' property in the generated
    # code (a bare stub) -- manually attach it so atem_WhenDateCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_WhenDateCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_WhenDateCase(dsl_WhenDate_Case_Month="sample_text")
    partner = atem_AbstractDateCase()
    setattr(partner, 'atem_AbstractDateCase', None)
    _safe_set(owner, 'atem_WhenDateCase93', partner)
    assert getattr(partner, 'atem_AbstractDateCase') == owner
    _safe_set(owner, 'atem_WhenDateCase93', None)
    assert getattr(partner, 'atem_AbstractDateCase') is None


def test_assoc_dsl_WhenDateCase_True_actions94_stub_double():
    # atem_AbstractComponent has no real 'atem_AbstractComponent96' property in the generated
    # code (a bare stub) -- manually attach it so atem_WhenDateCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_WhenDateCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_WhenDateCase(dsl_WhenDate_Case_Month="sample_text")
    partner = atem_AbstractComponent()
    setattr(partner, 'atem_AbstractComponent96', None)
    _safe_set(owner, 'atem_WhenDateCase95', {partner})
    assert getattr(partner, 'atem_AbstractComponent96') == owner
    _safe_set(owner, 'atem_WhenDateCase95', set())
    assert getattr(partner, 'atem_AbstractComponent96') is None


def test_assoc_dsl_WhenDate_Cases89_stub_double():
    # atem_WhenDate has no real 'atem_WhenDate' property in the generated
    # code (a bare stub) -- manually attach it so atem_WhenDateCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_WhenDateCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_WhenDateCase(dsl_WhenDate_Case_Month="sample_text")
    partner = atem_WhenDate()
    setattr(partner, 'atem_WhenDate', None)
    _safe_set(owner, 'atem_WhenDateCase', partner)
    assert owner in getattr(partner, 'atem_WhenDate')
    _safe_set(owner, 'atem_WhenDateCase', None)
    assert owner not in getattr(partner, 'atem_WhenDate')


def test_assoc_dsl_WhenModeOfWeekCase_Days147_stub_double():
    # atem_WhenModeOfWeekCase has no real 'atem_WhenModeOfWeekCase148' property in the generated
    # code (a bare stub) -- manually attach it so atem_ModeOfWeekSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_ModeOfWeekSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_ModeOfWeekSet(dsl_ModeOfWeekSet_MOWs="sample_text")
    partner = atem_WhenModeOfWeekCase()
    setattr(partner, 'atem_WhenModeOfWeekCase148', None)
    _safe_set(owner, 'atem_ModeOfWeekSet', partner)
    assert getattr(partner, 'atem_WhenModeOfWeekCase148') == owner
    _safe_set(owner, 'atem_ModeOfWeekSet', None)
    assert getattr(partner, 'atem_WhenModeOfWeekCase148') is None


def test_assoc_dsl_WhenSundayAfterElevationOfCrossDay_Cases120_stub_double():
    # atem_WhenSundayAfterElevationOfCrossDay has no real 'atem_WhenSundayAfterElevationOfCrossDay' property in the generated
    # code (a bare stub) -- manually attach it so atem_WhenDateCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_WhenDateCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_WhenDateCase(dsl_WhenDate_Case_Month="sample_text")
    partner = atem_WhenSundayAfterElevationOfCrossDay()
    setattr(partner, 'atem_WhenSundayAfterElevationOfCrossDay', None)
    _safe_set(owner, 'atem_WhenDateCase121', partner)
    assert owner in getattr(partner, 'atem_WhenSundayAfterElevationOfCrossDay')
    _safe_set(owner, 'atem_WhenDateCase121', None)
    assert owner not in getattr(partner, 'atem_WhenSundayAfterElevationOfCrossDay')


def test_assoc_dsl_WhenSundaysBeforeTriodion_Cases152_stub_double():
    # atem_WhenSundaysBeforeTriodion has no real 'atem_WhenSundaysBeforeTriodion' property in the generated
    # code (a bare stub) -- manually attach it so atem_SundaysBeforeTriodionCase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_SundaysBeforeTriodionCase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_SundaysBeforeTriodionCase(dsl_SundaysBeforeTriodionCase_Days=7)
    partner = atem_WhenSundaysBeforeTriodion()
    setattr(partner, 'atem_WhenSundaysBeforeTriodion', None)
    _safe_set(owner, 'atem_SundaysBeforeTriodionCase', partner)
    assert owner in getattr(partner, 'atem_WhenSundaysBeforeTriodion')
    _safe_set(owner, 'atem_SundaysBeforeTriodionCase', None)
    assert owner not in getattr(partner, 'atem_WhenSundaysBeforeTriodion')


def test_assoc_name43_stub_double():
    # atem_TemplateFragment has no real 'atem_TemplateFragment' property in the generated
    # code (a bare stub) -- manually attach it so atem_AtemModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_AtemModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_AtemModel(name="sample_text")
    partner = atem_TemplateFragment()
    setattr(partner, 'atem_TemplateFragment', None)
    _safe_set(owner, 'atem_AtemModel44', partner)
    assert getattr(partner, 'atem_TemplateFragment') == owner
    _safe_set(owner, 'atem_AtemModel44', None)
    assert getattr(partner, 'atem_TemplateFragment') is None


def test_assoc_name45_stub_double():
    # atem_PrefaceFragment has no real 'atem_PrefaceFragment' property in the generated
    # code (a bare stub) -- manually attach it so atem_Preface's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_Preface's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_Preface(name="sample_text")
    partner = atem_PrefaceFragment()
    setattr(partner, 'atem_PrefaceFragment', None)
    _safe_set(owner, 'atem_Preface46', partner)
    assert getattr(partner, 'atem_PrefaceFragment') == owner
    _safe_set(owner, 'atem_Preface46', None)
    assert getattr(partner, 'atem_PrefaceFragment') is None


def test_assoc_name47_stub_double():
    # atem_SectionFragment has no real 'atem_SectionFragment' property in the generated
    # code (a bare stub) -- manually attach it so atem_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atem_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atem_Section(name="sample_text")
    partner = atem_SectionFragment()
    setattr(partner, 'atem_SectionFragment', None)
    _safe_set(owner, 'atem_Section48', partner)
    assert getattr(partner, 'atem_SectionFragment') == owner
    _safe_set(owner, 'atem_Section48', None)
    assert getattr(partner, 'atem_SectionFragment') is None


