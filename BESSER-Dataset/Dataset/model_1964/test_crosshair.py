from python_code import atem_Aid

def test_atem_Aid___init__():
    assert atem_Aid.__init__(atem_Aid(''), '') == None


from python_code import atem_All

def test_atem_All___init__():
    assert atem_All.__init__(atem_All(True), False) == None


from python_code import atem_Break

def test_atem_Break___init__():
    assert atem_Break.__init__(atem_Break(''), '') == None


from python_code import atem_DOL

def test_atem_DOL___init__():
    assert atem_DOL.__init__(atem_DOL(True), False) == None


from python_code import atem_DOM

def test_atem_DOM___init__():
    assert atem_DOM.__init__(atem_DOM(True), False) == None


from python_code import atem_DOP

def test_atem_DOP___init__():
    assert atem_DOP.__init__(atem_DOP(True), False) == None


from python_code import atem_DOWN

def test_atem_DOWN___init__():
    assert atem_DOWN.__init__(atem_DOWN(True), False) == None


from python_code import atem_DOWT

def test_atem_DOWT___init__():
    assert atem_DOWT.__init__(atem_DOWT(True), False) == None


from python_code import atem_Date

def test_atem_Date___init__():
    assert atem_Date.__init__(atem_Date(0, 0, 0), 0, 0, 0) == None


from python_code import atem_DateRange

def test_atem_DateRange___init__():
    assert atem_DateRange.__init__(atem_DateRange(0, 0), 0, 0) == None


from python_code import atem_DateSet

def test_atem_DateSet___init__():
    assert atem_DateSet.__init__(atem_DateSet(0), 0) == None


from python_code import atem_DayNameRange

def test_atem_DayNameRange___init__():
    assert atem_DayNameRange.__init__(atem_DayNameRange('', '\x00'), '\x00\x00', '') == None


from python_code import atem_DayNameSet

def test_atem_DayNameSet___init__():
    assert atem_DayNameSet.__init__(atem_DayNameSet(''), '') == None


from python_code import atem_DayRange

def test_atem_DayRange___init__():
    assert atem_DayRange.__init__(atem_DayRange(0, 0), 0, 0) == None


from python_code import atem_DaySet

def test_atem_DaySet___init__():
    assert atem_DaySet.__init__(atem_DaySet(0), 0) == None


from python_code import atem_EOW

def test_atem_EOW___init__():
    assert atem_EOW.__init__(atem_EOW(True), False) == None


from python_code import atem_GenDate

def test_atem_GenDate___init__():
    assert atem_GenDate.__init__(atem_GenDate(True), False) == None


from python_code import atem_GenYear

def test_atem_GenYear___init__():
    assert atem_GenYear.__init__(atem_GenYear(True), False) == None


from python_code import atem_HeaderFooterCommemoration

def test_atem_HeaderFooterCommemoration___init__():
    assert atem_HeaderFooterCommemoration.__init__(atem_HeaderFooterCommemoration(True), False) == None


from python_code import atem_HeaderFooterDate

def test_atem_HeaderFooterDate___init__():
    assert atem_HeaderFooterDate.__init__(atem_HeaderFooterDate(False, '\x00'), False, '\x00') == None


from python_code import atem_HeaderFooterLookup

def test_atem_HeaderFooterLookup___init__():
    assert atem_HeaderFooterLookup.__init__(atem_HeaderFooterLookup('', atem_HeaderFooterLookup=set()), '', atem_HeaderFooterLookup=set()) == None


from python_code import atem_HeaderFooterPageNumber

def test_atem_HeaderFooterPageNumber___init__():
    assert atem_HeaderFooterPageNumber.__init__(atem_HeaderFooterPageNumber(True), False) == None


from python_code import atem_HeaderFooterText

def test_atem_HeaderFooterText___init__():
    assert atem_HeaderFooterText.__init__(atem_HeaderFooterText(''), '') == None


from python_code import atem_HeaderFooterTitle

def test_atem_HeaderFooterTitle___init__():
    assert atem_HeaderFooterTitle.__init__(atem_HeaderFooterTitle(True), False) == None


from python_code import atem_Info

def test_atem_Info___init__():
    assert atem_Info.__init__(atem_Info('', atem_Info=set()), '', atem_Info=set()) == None


from python_code import atem_LitBook

def test_atem_LitBook___init__():
    assert atem_LitBook.__init__(atem_LitBook(''), '') == None


from python_code import atem_Definition
from python_code import atem_Lookup

def test_atem_Lookup___init__():
    assert atem_Lookup.__init__(atem_Lookup(False, False, '', False, '', atem_Lookup=atem_Definition()), True, False, '', False, '', atem_Lookup=atem_Definition()) == None


from python_code import atem_MCD

def test_atem_MCD___init__():
    assert atem_MCD.__init__(atem_MCD(True), False) == None


from python_code import atem_MOW

def test_atem_MOW___init__():
    assert atem_MOW.__init__(atem_MOW(True), False) == None


from python_code import atem_ModeOfWeekSet
from python_code import atem_WhenModeOfWeekCase

def test_atem_ModeOfWeekSet___init__():
    assert atem_ModeOfWeekSet.__init__(atem_ModeOfWeekSet('', atem_ModeOfWeekSet=atem_WhenModeOfWeekCase()), '', atem_ModeOfWeekSet=atem_WhenModeOfWeekCase()) == None


from python_code import atem_NOP

def test_atem_NOP___init__():
    assert atem_NOP.__init__(atem_NOP(True), False) == None


from python_code import atem_PageKeepWithNext

def test_atem_PageKeepWithNext___init__():
    assert atem_PageKeepWithNext.__init__(atem_PageKeepWithNext(''), '') == None


from python_code import atem_PageNumber

def test_atem_PageNumber___init__():
    assert atem_PageNumber.__init__(atem_PageNumber(0), 0) == None


from python_code import atem_PassThroughHtml

def test_atem_PassThroughHtml___init__():
    assert atem_PassThroughHtml.__init__(atem_PassThroughHtml(''), '') == None


from python_code import atem_PassThroughPdf

def test_atem_PassThroughPdf___init__():
    assert atem_PassThroughPdf.__init__(atem_PassThroughPdf(''), '') == None


from python_code import atem_Definition
from python_code import atem_ResourceText

def test_atem_ResourceText___init__():
    assert atem_ResourceText.__init__(atem_ResourceText(True, atem_ResourceText=atem_Definition()), False, atem_ResourceText=atem_Definition()) == None


from python_code import atem_RestoreLocale

def test_atem_RestoreLocale___init__():
    assert atem_RestoreLocale.__init__(atem_RestoreLocale(True), False) == None


from python_code import atem_SAEC

def test_atem_SAEC___init__():
    assert atem_SAEC.__init__(atem_SAEC(True), False) == None


from python_code import atem_SBT

def test_atem_SBT___init__():
    assert atem_SBT.__init__(atem_SBT(True), False) == None


from python_code import atem_SOL

def test_atem_SOL___init__():
    assert atem_SOL.__init__(atem_SOL(True), False) == None


from python_code import atem_Definition
from python_code import atem_Section
from python_code import atem_SectionFragment

def test_atem_Section___init__():
    assert atem_Section.__init__(atem_Section('', atem_Section=atem_Definition(), atem_Section42=set(), atem_Section48=atem_SectionFragment()), '', atem_Section=atem_Definition(), atem_Section42=set(), atem_Section48=atem_SectionFragment()) == None


from python_code import atem_SetLocale

def test_atem_SetLocale___init__():
    assert atem_SetLocale.__init__(atem_SetLocale('', '\x00'), '\x00\x00', '') == None


from python_code import atem_SundaysBeforeTriodionCase
from python_code import atem_WhenSundaysBeforeTriodion

def test_atem_SundaysBeforeTriodionCase___init__():
    assert atem_SundaysBeforeTriodionCase.__init__(atem_SundaysBeforeTriodionCase(0, atem_SundaysBeforeTriodionCase=atem_WhenSundaysBeforeTriodion(), atem_SundaysBeforeTriodionCase157=set()), 0, atem_SundaysBeforeTriodionCase=atem_WhenSundaysBeforeTriodion(), atem_SundaysBeforeTriodionCase157=set()) == None


from python_code import atem_Version

def test_atem_Version___init__():
    assert atem_Version.__init__(atem_Version(''), '') == None


from python_code import atem_VersionSwitch

def test_atem_VersionSwitch___init__():
    assert atem_VersionSwitch.__init__(atem_VersionSwitch(''), '') == None


from python_code import atem_WDOLC

def test_atem_WDOLC___init__():
    assert atem_WDOLC.__init__(atem_WDOLC(True), False) == None


from python_code import atem_WOLC

def test_atem_WOLC___init__():
    assert atem_WOLC.__init__(atem_WOLC(True), False) == None


from python_code import atem_AbstractDateCase
from python_code import atem_WhenDate
from python_code import atem_WhenDateCase
from python_code import atem_WhenSundayAfterElevationOfCrossDay

def test_atem_WhenDateCase___init__():
    assert atem_WhenDateCase.__init__(atem_WhenDateCase('', atem_WhenDateCase=atem_WhenDate(), atem_WhenDateCase93=atem_AbstractDateCase(), atem_WhenDateCase95=set(), atem_WhenDateCase121=atem_WhenSundayAfterElevationOfCrossDay()), '', atem_WhenDateCase=atem_WhenDate(), atem_WhenDateCase93=atem_AbstractDateCase(), atem_WhenDateCase95=set(), atem_WhenDateCase121=atem_WhenSundayAfterElevationOfCrossDay()) == None

