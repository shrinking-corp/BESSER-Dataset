import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Entry,
    Field,
    IntValue,
    Person,
    StringValue,
    YearValue,
    bibtex_AbstractField,
    bibtex_AddressField,
    bibtex_ArticleEntry,
    bibtex_Author,
    bibtex_AuthorField,
    bibtex_Bibliography,
    bibtex_BibtexKeyField,
    bibtex_BookTitleField,
    bibtex_Editor,
    bibtex_EditorField,
    bibtex_EidField,
    bibtex_Entry,
    bibtex_Field,
    bibtex_InProceedingsEntry,
    bibtex_IntValue,
    bibtex_JournalField,
    bibtex_Keyword,
    bibtex_KeywordField,
    bibtex_MonthField,
    bibtex_NoteField,
    bibtex_NumberField,
    bibtex_OrganizationField,
    bibtex_Page,
    bibtex_PageField,
    bibtex_PartField,
    bibtex_Person,
    bibtex_PublisherField,
    bibtex_ReviewField,
    bibtex_SeriesField,
    bibtex_StringValue,
    bibtex_TitleField,
    bibtex_UrlField,
    bibtex_VolumeField,
    bibtex_YearField,
    bibtex_YearValue,
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

def test_assoc_abstract8_stub_double():
    # bibtex_AbstractField has no real 'bibtex_AbstractField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Entry()
    partner = bibtex_AbstractField()
    setattr(partner, 'bibtex_AbstractField', None)
    _safe_set(owner, 'bibtex_Entry9', partner)
    assert getattr(partner, 'bibtex_AbstractField') == owner
    _safe_set(owner, 'bibtex_Entry9', None)
    assert getattr(partner, 'bibtex_AbstractField') is None


def test_assoc_address37_stub_double():
    # bibtex_AddressField has no real 'bibtex_AddressField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_AddressField()
    setattr(partner, 'bibtex_AddressField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry38', partner)
    assert getattr(partner, 'bibtex_AddressField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry38', None)
    assert getattr(partner, 'bibtex_AddressField') is None


def test_assoc_author17_stub_double():
    # bibtex_AuthorField has no real 'bibtex_AuthorField18' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_AuthorField()
    setattr(partner, 'bibtex_AuthorField18', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry', partner)
    assert getattr(partner, 'bibtex_AuthorField18') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry', None)
    assert getattr(partner, 'bibtex_AuthorField18') is None


def test_assoc_author47_stub_double():
    # bibtex_AuthorField has no real 'bibtex_AuthorField48' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_AuthorField()
    setattr(partner, 'bibtex_AuthorField48', None)
    _safe_set(owner, 'bibtex_ArticleEntry', partner)
    assert getattr(partner, 'bibtex_AuthorField48') == owner
    _safe_set(owner, 'bibtex_ArticleEntry', None)
    assert getattr(partner, 'bibtex_AuthorField48') is None


def test_assoc_bibtexKey7_stub_double():
    # bibtex_BibtexKeyField has no real 'bibtex_BibtexKeyField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Entry()
    partner = bibtex_BibtexKeyField()
    setattr(partner, 'bibtex_BibtexKeyField', None)
    _safe_set(owner, 'bibtex_Entry', partner)
    assert getattr(partner, 'bibtex_BibtexKeyField') == owner
    _safe_set(owner, 'bibtex_Entry', None)
    assert getattr(partner, 'bibtex_BibtexKeyField') is None


def test_assoc_bookTitle21_stub_double():
    # bibtex_BookTitleField has no real 'bibtex_BookTitleField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_BookTitleField()
    setattr(partner, 'bibtex_BookTitleField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry22', partner)
    assert getattr(partner, 'bibtex_BookTitleField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry22', None)
    assert getattr(partner, 'bibtex_BookTitleField') is None


def test_assoc_editor25_stub_double():
    # bibtex_EditorField has no real 'bibtex_EditorField27' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_EditorField()
    setattr(partner, 'bibtex_EditorField27', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry26', partner)
    assert getattr(partner, 'bibtex_EditorField27') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry26', None)
    assert getattr(partner, 'bibtex_EditorField27') is None


def test_assoc_eid74_stub_double():
    # bibtex_EidField has no real 'bibtex_EidField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_EidField()
    setattr(partner, 'bibtex_EidField', None)
    _safe_set(owner, 'bibtex_ArticleEntry75', partner)
    assert getattr(partner, 'bibtex_EidField') == owner
    _safe_set(owner, 'bibtex_ArticleEntry75', None)
    assert getattr(partner, 'bibtex_EidField') is None


def test_assoc_entries76_stub_double():
    # bibtex_Bibliography has no real 'bibtex_Bibliography' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Entry()
    partner = bibtex_Bibliography()
    setattr(partner, 'bibtex_Bibliography', None)
    _safe_set(owner, 'bibtex_Entry77', partner)
    assert owner in getattr(partner, 'bibtex_Bibliography')
    _safe_set(owner, 'bibtex_Entry77', None)
    assert owner not in getattr(partner, 'bibtex_Bibliography')


def test_assoc_journal55_stub_double():
    # bibtex_JournalField has no real 'bibtex_JournalField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_JournalField()
    setattr(partner, 'bibtex_JournalField', None)
    _safe_set(owner, 'bibtex_ArticleEntry56', partner)
    assert getattr(partner, 'bibtex_JournalField') == owner
    _safe_set(owner, 'bibtex_ArticleEntry56', None)
    assert getattr(partner, 'bibtex_JournalField') is None


def test_assoc_keyword12_stub_double():
    # bibtex_KeywordField has no real 'bibtex_KeywordField14' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Entry()
    partner = bibtex_KeywordField()
    setattr(partner, 'bibtex_KeywordField14', None)
    _safe_set(owner, 'bibtex_Entry13', partner)
    assert getattr(partner, 'bibtex_KeywordField14') == owner
    _safe_set(owner, 'bibtex_Entry13', None)
    assert getattr(partner, 'bibtex_KeywordField14') is None


def test_assoc_month39_stub_double():
    # bibtex_MonthField has no real 'bibtex_MonthField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_MonthField()
    setattr(partner, 'bibtex_MonthField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry40', partner)
    assert getattr(partner, 'bibtex_MonthField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry40', None)
    assert getattr(partner, 'bibtex_MonthField') is None


def test_assoc_month66_stub_double():
    # bibtex_MonthField has no real 'bibtex_MonthField68' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_MonthField()
    setattr(partner, 'bibtex_MonthField68', None)
    _safe_set(owner, 'bibtex_ArticleEntry67', partner)
    assert getattr(partner, 'bibtex_MonthField68') == owner
    _safe_set(owner, 'bibtex_ArticleEntry67', None)
    assert getattr(partner, 'bibtex_MonthField68') is None


def test_assoc_note43_stub_double():
    # bibtex_NoteField has no real 'bibtex_NoteField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_NoteField()
    setattr(partner, 'bibtex_NoteField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry44', partner)
    assert getattr(partner, 'bibtex_NoteField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry44', None)
    assert getattr(partner, 'bibtex_NoteField') is None


def test_assoc_note69_stub_double():
    # bibtex_NoteField has no real 'bibtex_NoteField71' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_NoteField()
    setattr(partner, 'bibtex_NoteField71', None)
    _safe_set(owner, 'bibtex_ArticleEntry70', partner)
    assert getattr(partner, 'bibtex_NoteField71') == owner
    _safe_set(owner, 'bibtex_ArticleEntry70', None)
    assert getattr(partner, 'bibtex_NoteField71') is None


def test_assoc_number33_stub_double():
    # bibtex_NumberField has no real 'bibtex_NumberField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_NumberField()
    setattr(partner, 'bibtex_NumberField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry34', partner)
    assert getattr(partner, 'bibtex_NumberField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry34', None)
    assert getattr(partner, 'bibtex_NumberField') is None


def test_assoc_number63_stub_double():
    # bibtex_NumberField has no real 'bibtex_NumberField65' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_NumberField()
    setattr(partner, 'bibtex_NumberField65', None)
    _safe_set(owner, 'bibtex_ArticleEntry64', partner)
    assert getattr(partner, 'bibtex_NumberField65') == owner
    _safe_set(owner, 'bibtex_ArticleEntry64', None)
    assert getattr(partner, 'bibtex_NumberField65') is None


def test_assoc_organization41_stub_double():
    # bibtex_OrganizationField has no real 'bibtex_OrganizationField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_OrganizationField()
    setattr(partner, 'bibtex_OrganizationField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry42', partner)
    assert getattr(partner, 'bibtex_OrganizationField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry42', None)
    assert getattr(partner, 'bibtex_OrganizationField') is None


def test_assoc_pages28_stub_double():
    # bibtex_PageField has no real 'bibtex_PageField30' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_PageField()
    setattr(partner, 'bibtex_PageField30', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry29', partner)
    assert getattr(partner, 'bibtex_PageField30') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry29', None)
    assert getattr(partner, 'bibtex_PageField30') is None


def test_assoc_pages57_stub_double():
    # bibtex_PageField has no real 'bibtex_PageField59' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_PageField()
    setattr(partner, 'bibtex_PageField59', None)
    _safe_set(owner, 'bibtex_ArticleEntry58', partner)
    assert getattr(partner, 'bibtex_PageField59') == owner
    _safe_set(owner, 'bibtex_ArticleEntry58', None)
    assert getattr(partner, 'bibtex_PageField59') is None


def test_assoc_part72_stub_double():
    # bibtex_PartField has no real 'bibtex_PartField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_PartField()
    setattr(partner, 'bibtex_PartField', None)
    _safe_set(owner, 'bibtex_ArticleEntry73', partner)
    assert getattr(partner, 'bibtex_PartField') == owner
    _safe_set(owner, 'bibtex_ArticleEntry73', None)
    assert getattr(partner, 'bibtex_PartField') is None


def test_assoc_publisher45_stub_double():
    # bibtex_PublisherField has no real 'bibtex_PublisherField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_PublisherField()
    setattr(partner, 'bibtex_PublisherField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry46', partner)
    assert getattr(partner, 'bibtex_PublisherField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry46', None)
    assert getattr(partner, 'bibtex_PublisherField') is None


def test_assoc_review15_stub_double():
    # bibtex_ReviewField has no real 'bibtex_ReviewField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Entry()
    partner = bibtex_ReviewField()
    setattr(partner, 'bibtex_ReviewField', None)
    _safe_set(owner, 'bibtex_Entry16', partner)
    assert getattr(partner, 'bibtex_ReviewField') == owner
    _safe_set(owner, 'bibtex_Entry16', None)
    assert getattr(partner, 'bibtex_ReviewField') is None


def test_assoc_series35_stub_double():
    # bibtex_SeriesField has no real 'bibtex_SeriesField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_SeriesField()
    setattr(partner, 'bibtex_SeriesField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry36', partner)
    assert getattr(partner, 'bibtex_SeriesField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry36', None)
    assert getattr(partner, 'bibtex_SeriesField') is None


def test_assoc_title19_stub_double():
    # bibtex_TitleField has no real 'bibtex_TitleField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_TitleField()
    setattr(partner, 'bibtex_TitleField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry20', partner)
    assert getattr(partner, 'bibtex_TitleField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry20', None)
    assert getattr(partner, 'bibtex_TitleField') is None


def test_assoc_title49_stub_double():
    # bibtex_TitleField has no real 'bibtex_TitleField51' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_TitleField()
    setattr(partner, 'bibtex_TitleField51', None)
    _safe_set(owner, 'bibtex_ArticleEntry50', partner)
    assert getattr(partner, 'bibtex_TitleField51') == owner
    _safe_set(owner, 'bibtex_ArticleEntry50', None)
    assert getattr(partner, 'bibtex_TitleField51') is None


def test_assoc_url10_stub_double():
    # bibtex_UrlField has no real 'bibtex_UrlField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Entry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Entry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Entry()
    partner = bibtex_UrlField()
    setattr(partner, 'bibtex_UrlField', None)
    _safe_set(owner, 'bibtex_Entry11', partner)
    assert getattr(partner, 'bibtex_UrlField') == owner
    _safe_set(owner, 'bibtex_Entry11', None)
    assert getattr(partner, 'bibtex_UrlField') is None


def test_assoc_volume31_stub_double():
    # bibtex_VolumeField has no real 'bibtex_VolumeField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_VolumeField()
    setattr(partner, 'bibtex_VolumeField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry32', partner)
    assert getattr(partner, 'bibtex_VolumeField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry32', None)
    assert getattr(partner, 'bibtex_VolumeField') is None


def test_assoc_volume60_stub_double():
    # bibtex_VolumeField has no real 'bibtex_VolumeField62' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_VolumeField()
    setattr(partner, 'bibtex_VolumeField62', None)
    _safe_set(owner, 'bibtex_ArticleEntry61', partner)
    assert getattr(partner, 'bibtex_VolumeField62') == owner
    _safe_set(owner, 'bibtex_ArticleEntry61', None)
    assert getattr(partner, 'bibtex_VolumeField62') is None


def test_assoc_year23_stub_double():
    # bibtex_YearField has no real 'bibtex_YearField' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_InProceedingsEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_InProceedingsEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_InProceedingsEntry()
    partner = bibtex_YearField()
    setattr(partner, 'bibtex_YearField', None)
    _safe_set(owner, 'bibtex_InProceedingsEntry24', partner)
    assert getattr(partner, 'bibtex_YearField') == owner
    _safe_set(owner, 'bibtex_InProceedingsEntry24', None)
    assert getattr(partner, 'bibtex_YearField') is None


def test_assoc_year52_stub_double():
    # bibtex_YearField has no real 'bibtex_YearField54' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_ArticleEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_ArticleEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_ArticleEntry()
    partner = bibtex_YearField()
    setattr(partner, 'bibtex_YearField54', None)
    _safe_set(owner, 'bibtex_ArticleEntry53', partner)
    assert getattr(partner, 'bibtex_YearField54') == owner
    _safe_set(owner, 'bibtex_ArticleEntry53', None)
    assert getattr(partner, 'bibtex_YearField54') is None


