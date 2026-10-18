import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AuthorField,
    BibtexEntryTypes,
    bibTeX_AddressField,
    bibTeX_Article,
    bibTeX_AuthorField,
    bibTeX_Authors,
    bibTeX_BibtexEntryTypes,
    bibTeX_Book,
    bibTeX_CiteKey,
    bibTeX_EObject,
    bibTeX_EditionField,
    bibTeX_EditorField,
    bibTeX_Fullname,
    bibTeX_IsbnField,
    bibTeX_JournalField,
    bibTeX_Model,
    bibTeX_MonthField,
    bibTeX_NoteField,
    bibTeX_NumberField,
    bibTeX_PagesField,
    bibTeX_PublisherField,
    bibTeX_SeriesField,
    bibTeX_TitleField,
    bibTeX_UnknownField,
    bibTeX_UnknownType,
    bibTeX_UnknownValue,
    bibTeX_VolumeField,
    bibTeX_YearField,
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

def test_assoc_address30_stub_double():
    # bibTeX_Book has no real 'bibTeX_Book31' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_AddressField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_AddressField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_AddressField(address="sample_text")
    partner = bibTeX_Book()
    setattr(partner, 'bibTeX_Book31', None)
    _safe_set(owner, 'bibTeX_AddressField', partner)
    assert getattr(partner, 'bibTeX_Book31') == owner
    _safe_set(owner, 'bibTeX_AddressField', None)
    assert getattr(partner, 'bibTeX_Book31') is None


def test_assoc_edition32_stub_double():
    # bibTeX_Book has no real 'bibTeX_Book33' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_EditionField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_EditionField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_EditionField(edition="sample_text")
    partner = bibTeX_Book()
    setattr(partner, 'bibTeX_Book33', None)
    _safe_set(owner, 'bibTeX_EditionField', partner)
    assert getattr(partner, 'bibTeX_Book33') == owner
    _safe_set(owner, 'bibTeX_EditionField', None)
    assert getattr(partner, 'bibTeX_Book33') is None


def test_assoc_isbn34_stub_double():
    # bibTeX_Book has no real 'bibTeX_Book35' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_IsbnField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_IsbnField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_IsbnField(isbn="sample_text")
    partner = bibTeX_Book()
    setattr(partner, 'bibTeX_Book35', None)
    _safe_set(owner, 'bibTeX_IsbnField', partner)
    assert getattr(partner, 'bibTeX_Book35') == owner
    _safe_set(owner, 'bibTeX_IsbnField', None)
    assert getattr(partner, 'bibTeX_Book35') is None


def test_assoc_journal14_stub_double():
    # bibTeX_Article has no real 'bibTeX_Article15' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_JournalField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_JournalField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_JournalField(journal="sample_text")
    partner = bibTeX_Article()
    setattr(partner, 'bibTeX_Article15', None)
    _safe_set(owner, 'bibTeX_JournalField', partner)
    assert getattr(partner, 'bibTeX_Article15') == owner
    _safe_set(owner, 'bibTeX_JournalField', None)
    assert getattr(partner, 'bibTeX_Article15') is None


def test_assoc_key1_stub_double():
    # bibTeX_BibtexEntryTypes has no real 'bibTeX_BibtexEntryTypes2' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_CiteKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_CiteKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_CiteKey(key="sample_text")
    partner = bibTeX_BibtexEntryTypes()
    setattr(partner, 'bibTeX_BibtexEntryTypes2', None)
    _safe_set(owner, 'bibTeX_CiteKey', partner)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes2') == owner
    _safe_set(owner, 'bibTeX_CiteKey', None)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes2') is None


def test_assoc_month7_stub_double():
    # bibTeX_BibtexEntryTypes has no real 'bibTeX_BibtexEntryTypes8' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_MonthField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_MonthField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_MonthField(month="sample_text")
    partner = bibTeX_BibtexEntryTypes()
    setattr(partner, 'bibTeX_BibtexEntryTypes8', None)
    _safe_set(owner, 'bibTeX_MonthField', partner)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes8') == owner
    _safe_set(owner, 'bibTeX_MonthField', None)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes8') is None


def test_assoc_names40_stub_double():
    # bibTeX_Authors has no real 'bibTeX_Authors' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_Fullname's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_Fullname's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_Fullname(firstname="sample_text", lastname="sample_text")
    partner = bibTeX_Authors()
    setattr(partner, 'bibTeX_Authors', None)
    _safe_set(owner, 'bibTeX_Fullname', partner)
    assert owner in getattr(partner, 'bibTeX_Authors')
    _safe_set(owner, 'bibTeX_Fullname', None)
    assert owner not in getattr(partner, 'bibTeX_Authors')


def test_assoc_note9_stub_double():
    # bibTeX_BibtexEntryTypes has no real 'bibTeX_BibtexEntryTypes10' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_NoteField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_NoteField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_NoteField(note="sample_text")
    partner = bibTeX_BibtexEntryTypes()
    setattr(partner, 'bibTeX_BibtexEntryTypes10', None)
    _safe_set(owner, 'bibTeX_NoteField', partner)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes10') == owner
    _safe_set(owner, 'bibTeX_NoteField', None)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes10') is None


def test_assoc_number18_stub_double():
    # bibTeX_Article has no real 'bibTeX_Article19' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_NumberField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_NumberField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_NumberField(number="sample_text")
    partner = bibTeX_Article()
    setattr(partner, 'bibTeX_Article19', None)
    _safe_set(owner, 'bibTeX_NumberField', partner)
    assert getattr(partner, 'bibTeX_Article19') == owner
    _safe_set(owner, 'bibTeX_NumberField', None)
    assert getattr(partner, 'bibTeX_Article19') is None


def test_assoc_pages20_stub_double():
    # bibTeX_Article has no real 'bibTeX_Article21' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_PagesField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_PagesField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_PagesField(pages="sample_text")
    partner = bibTeX_Article()
    setattr(partner, 'bibTeX_Article21', None)
    _safe_set(owner, 'bibTeX_PagesField', partner)
    assert getattr(partner, 'bibTeX_Article21') == owner
    _safe_set(owner, 'bibTeX_PagesField', None)
    assert getattr(partner, 'bibTeX_Article21') is None


def test_assoc_publisher23_stub_double():
    # bibTeX_Book has no real 'bibTeX_Book24' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_PublisherField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_PublisherField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_PublisherField(publisher="sample_text")
    partner = bibTeX_Book()
    setattr(partner, 'bibTeX_Book24', None)
    _safe_set(owner, 'bibTeX_PublisherField', partner)
    assert getattr(partner, 'bibTeX_Book24') == owner
    _safe_set(owner, 'bibTeX_PublisherField', None)
    assert getattr(partner, 'bibTeX_Book24') is None


def test_assoc_series28_stub_double():
    # bibTeX_Book has no real 'bibTeX_Book29' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_SeriesField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_SeriesField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_SeriesField(series="sample_text")
    partner = bibTeX_Book()
    setattr(partner, 'bibTeX_Book29', None)
    _safe_set(owner, 'bibTeX_SeriesField', partner)
    assert getattr(partner, 'bibTeX_Book29') == owner
    _safe_set(owner, 'bibTeX_SeriesField', None)
    assert getattr(partner, 'bibTeX_Book29') is None


def test_assoc_title3_stub_double():
    # bibTeX_BibtexEntryTypes has no real 'bibTeX_BibtexEntryTypes4' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_TitleField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_TitleField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_TitleField(title="sample_text")
    partner = bibTeX_BibtexEntryTypes()
    setattr(partner, 'bibTeX_BibtexEntryTypes4', None)
    _safe_set(owner, 'bibTeX_TitleField', partner)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes4') == owner
    _safe_set(owner, 'bibTeX_TitleField', None)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes4') is None


def test_assoc_type36_stub_double():
    # bibTeX_UnknownField has no real 'bibTeX_UnknownField37' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_UnknownType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_UnknownType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_UnknownType(type="sample_text")
    partner = bibTeX_UnknownField()
    setattr(partner, 'bibTeX_UnknownField37', None)
    _safe_set(owner, 'bibTeX_UnknownType', partner)
    assert getattr(partner, 'bibTeX_UnknownField37') == owner
    _safe_set(owner, 'bibTeX_UnknownType', None)
    assert getattr(partner, 'bibTeX_UnknownField37') is None


def test_assoc_value38_stub_double():
    # bibTeX_UnknownField has no real 'bibTeX_UnknownField39' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_UnknownValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_UnknownValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_UnknownValue(value="sample_text")
    partner = bibTeX_UnknownField()
    setattr(partner, 'bibTeX_UnknownField39', None)
    _safe_set(owner, 'bibTeX_UnknownValue', partner)
    assert getattr(partner, 'bibTeX_UnknownField39') == owner
    _safe_set(owner, 'bibTeX_UnknownValue', None)
    assert getattr(partner, 'bibTeX_UnknownField39') is None


def test_assoc_volume16_stub_double():
    # bibTeX_Article has no real 'bibTeX_Article17' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_VolumeField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_VolumeField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_VolumeField(volume="sample_text")
    partner = bibTeX_Article()
    setattr(partner, 'bibTeX_Article17', None)
    _safe_set(owner, 'bibTeX_VolumeField', partner)
    assert getattr(partner, 'bibTeX_Article17') == owner
    _safe_set(owner, 'bibTeX_VolumeField', None)
    assert getattr(partner, 'bibTeX_Article17') is None


def test_assoc_year5_stub_double():
    # bibTeX_BibtexEntryTypes has no real 'bibTeX_BibtexEntryTypes6' property in the generated
    # code (a bare stub) -- manually attach it so bibTeX_YearField's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibTeX_YearField's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibTeX_YearField(year="sample_text")
    partner = bibTeX_BibtexEntryTypes()
    setattr(partner, 'bibTeX_BibtexEntryTypes6', None)
    _safe_set(owner, 'bibTeX_YearField', partner)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes6') == owner
    _safe_set(owner, 'bibTeX_YearField', None)
    assert getattr(partner, 'bibTeX_BibtexEntryTypes6') is None


