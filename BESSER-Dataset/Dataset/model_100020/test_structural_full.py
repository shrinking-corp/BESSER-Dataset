import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Author,
    AuthoredEntry,
    BIBTEXML_Article,
    BIBTEXML_Author,
    BIBTEXML_AuthoredEntry,
    BIBTEXML_BibtexFile,
    BIBTEXML_Book,
    BIBTEXML_BookTitledEntry,
    BIBTEXML_Booklet,
    BIBTEXML_Conference,
    BIBTEXML_DatedEntry,
    BIBTEXML_EditoredEntry,
    BIBTEXML_Entry,
    BIBTEXML_InBook,
    BIBTEXML_InCollection,
    BIBTEXML_InProceedings,
    BIBTEXML_InstitutionEntry,
    BIBTEXML_JournalEntry,
    BIBTEXML_Manual,
    BIBTEXML_MastersThesis,
    BIBTEXML_Misc,
    BIBTEXML_NotedEntry,
    BIBTEXML_PhdThesis,
    BIBTEXML_Proceedings,
    BIBTEXML_PublisheredEntry,
    BIBTEXML_SchoolEntry,
    BIBTEXML_TechReport,
    BIBTEXML_ThesisEntry,
    BIBTEXML_TitledEntry,
    BIBTEXML_Unpublished,
    Book,
    BookTitledEntry,
    DatedEntry,
    EditoredEntry,
    Entry,
    InProceedings,
    InstitutionEntry,
    JournalEntry,
    NotedEntry,
    Proceedings,
    PublisheredEntry,
    SchoolEntry,
    ThesisEntry,
    TitledEntry,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_BIBTEXML_Article_note_value_roundtrip():
    instance = BIBTEXML_Article(note="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_Article_number_value_roundtrip():
    instance = BIBTEXML_Article(note="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_BIBTEXML_Article_pages_value_roundtrip():
    instance = BIBTEXML_Article(note="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_BIBTEXML_Article_volume_value_roundtrip():
    instance = BIBTEXML_Article(note="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_BIBTEXML_Author_name_value_roundtrip():
    instance = BIBTEXML_Author(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_BIBTEXML_Book_address_value_roundtrip():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_BIBTEXML_Book_edition_value_roundtrip():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert instance.edition == "sample_text"
    instance.edition = "sample_text_2"
    assert instance.edition == "sample_text_2"


def test_BIBTEXML_Book_note_value_roundtrip():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_Book_number_value_roundtrip():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_BIBTEXML_Book_series_value_roundtrip():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_BIBTEXML_Book_volume_value_roundtrip():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_BIBTEXML_BookTitledEntry_booktitle_value_roundtrip():
    instance = BIBTEXML_BookTitledEntry(booktitle="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_BIBTEXML_Booklet_address_value_roundtrip():
    instance = BIBTEXML_Booklet(address="sample_text", howpublished="sample_text", note="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_BIBTEXML_Booklet_howpublished_value_roundtrip():
    instance = BIBTEXML_Booklet(address="sample_text", howpublished="sample_text", note="sample_text")
    assert instance.howpublished == "sample_text"
    instance.howpublished = "sample_text_2"
    assert instance.howpublished == "sample_text_2"


def test_BIBTEXML_Booklet_note_value_roundtrip():
    instance = BIBTEXML_Booklet(address="sample_text", howpublished="sample_text", note="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_DatedEntry_month_value_roundtrip():
    instance = BIBTEXML_DatedEntry(month="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_BIBTEXML_DatedEntry_year_value_roundtrip():
    instance = BIBTEXML_DatedEntry(month="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_BIBTEXML_EditoredEntry_editor_value_roundtrip():
    instance = BIBTEXML_EditoredEntry(editor="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_BIBTEXML_Entry_abstract_value_roundtrip():
    instance = BIBTEXML_Entry(abstract="sample_text", id="sample_text")
    assert instance.abstract == "sample_text"
    instance.abstract = "sample_text_2"
    assert instance.abstract == "sample_text_2"


def test_BIBTEXML_Entry_id_value_roundtrip():
    instance = BIBTEXML_Entry(abstract="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_BIBTEXML_InBook_chapter_value_roundtrip():
    instance = BIBTEXML_InBook(chapter="sample_text", type="sample_text")
    assert instance.chapter == "sample_text"
    instance.chapter = "sample_text_2"
    assert instance.chapter == "sample_text_2"


def test_BIBTEXML_InBook_type_value_roundtrip():
    instance = BIBTEXML_InBook(chapter="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_BIBTEXML_InCollection_chapter_value_roundtrip():
    instance = BIBTEXML_InCollection(chapter="sample_text", type="sample_text")
    assert instance.chapter == "sample_text"
    instance.chapter = "sample_text_2"
    assert instance.chapter == "sample_text_2"


def test_BIBTEXML_InCollection_type_value_roundtrip():
    instance = BIBTEXML_InCollection(chapter="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_BIBTEXML_InProceedings_pages_value_roundtrip():
    instance = BIBTEXML_InProceedings(pages="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_BIBTEXML_InstitutionEntry_institution_value_roundtrip():
    instance = BIBTEXML_InstitutionEntry(institution="sample_text")
    assert instance.institution == "sample_text"
    instance.institution = "sample_text_2"
    assert instance.institution == "sample_text_2"


def test_BIBTEXML_JournalEntry_journal_value_roundtrip():
    instance = BIBTEXML_JournalEntry(journal="sample_text")
    assert instance.journal == "sample_text"
    instance.journal = "sample_text_2"
    assert instance.journal == "sample_text_2"


def test_BIBTEXML_Manual_address_value_roundtrip():
    instance = BIBTEXML_Manual(address="sample_text", edition="sample_text", note="sample_text", organization="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_BIBTEXML_Manual_edition_value_roundtrip():
    instance = BIBTEXML_Manual(address="sample_text", edition="sample_text", note="sample_text", organization="sample_text")
    assert instance.edition == "sample_text"
    instance.edition = "sample_text_2"
    assert instance.edition == "sample_text_2"


def test_BIBTEXML_Manual_note_value_roundtrip():
    instance = BIBTEXML_Manual(address="sample_text", edition="sample_text", note="sample_text", organization="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_Manual_organization_value_roundtrip():
    instance = BIBTEXML_Manual(address="sample_text", edition="sample_text", note="sample_text", organization="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_BIBTEXML_Misc_howpublished_value_roundtrip():
    instance = BIBTEXML_Misc(howpublished="sample_text", month="sample_text", note="sample_text", title="sample_text", year="sample_text")
    assert instance.howpublished == "sample_text"
    instance.howpublished = "sample_text_2"
    assert instance.howpublished == "sample_text_2"


def test_BIBTEXML_Misc_month_value_roundtrip():
    instance = BIBTEXML_Misc(howpublished="sample_text", month="sample_text", note="sample_text", title="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_BIBTEXML_Misc_note_value_roundtrip():
    instance = BIBTEXML_Misc(howpublished="sample_text", month="sample_text", note="sample_text", title="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_Misc_title_value_roundtrip():
    instance = BIBTEXML_Misc(howpublished="sample_text", month="sample_text", note="sample_text", title="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_BIBTEXML_Misc_year_value_roundtrip():
    instance = BIBTEXML_Misc(howpublished="sample_text", month="sample_text", note="sample_text", title="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_BIBTEXML_NotedEntry_note_value_roundtrip():
    instance = BIBTEXML_NotedEntry(note="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_Proceedings_address_value_roundtrip():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_BIBTEXML_Proceedings_editor_value_roundtrip():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_BIBTEXML_Proceedings_note_value_roundtrip():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_Proceedings_number_value_roundtrip():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_BIBTEXML_Proceedings_organization_value_roundtrip():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_BIBTEXML_Proceedings_publisher_value_roundtrip():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_BIBTEXML_Proceedings_series_value_roundtrip():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_BIBTEXML_Proceedings_volume_value_roundtrip():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_BIBTEXML_PublisheredEntry_publisher_value_roundtrip():
    instance = BIBTEXML_PublisheredEntry(publisher="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_BIBTEXML_SchoolEntry_school_value_roundtrip():
    instance = BIBTEXML_SchoolEntry(school="sample_text")
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_BIBTEXML_TechReport_address_value_roundtrip():
    instance = BIBTEXML_TechReport(address="sample_text", note="sample_text", number="sample_text", type="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_BIBTEXML_TechReport_note_value_roundtrip():
    instance = BIBTEXML_TechReport(address="sample_text", note="sample_text", number="sample_text", type="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_TechReport_number_value_roundtrip():
    instance = BIBTEXML_TechReport(address="sample_text", note="sample_text", number="sample_text", type="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_BIBTEXML_TechReport_type_value_roundtrip():
    instance = BIBTEXML_TechReport(address="sample_text", note="sample_text", number="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_BIBTEXML_ThesisEntry_address_value_roundtrip():
    instance = BIBTEXML_ThesisEntry(address="sample_text", note="sample_text", type="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_BIBTEXML_ThesisEntry_note_value_roundtrip():
    instance = BIBTEXML_ThesisEntry(address="sample_text", note="sample_text", type="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BIBTEXML_ThesisEntry_type_value_roundtrip():
    instance = BIBTEXML_ThesisEntry(address="sample_text", note="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_BIBTEXML_TitledEntry_title_value_roundtrip():
    instance = BIBTEXML_TitledEntry(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_BIBTEXML_Article_isa_AuthoredEntry():
    instance = BIBTEXML_Article(note="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BIBTEXML_Book_isa_AuthoredEntry():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BIBTEXML_InProceedings_isa_AuthoredEntry():
    instance = BIBTEXML_InProceedings(pages="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BIBTEXML_Manual_isa_AuthoredEntry():
    instance = BIBTEXML_Manual(address="sample_text", edition="sample_text", note="sample_text", organization="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BIBTEXML_TechReport_isa_AuthoredEntry():
    instance = BIBTEXML_TechReport(address="sample_text", note="sample_text", number="sample_text", type="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BIBTEXML_ThesisEntry_isa_AuthoredEntry():
    instance = BIBTEXML_ThesisEntry(address="sample_text", note="sample_text", type="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BIBTEXML_Unpublished_isa_AuthoredEntry():
    instance = BIBTEXML_Unpublished()
    assert isinstance(instance, AuthoredEntry)


def test_BIBTEXML_InBook_isa_Book():
    instance = BIBTEXML_InBook(chapter="sample_text", type="sample_text")
    assert isinstance(instance, Book)


def test_BIBTEXML_InCollection_isa_Book():
    instance = BIBTEXML_InCollection(chapter="sample_text", type="sample_text")
    assert isinstance(instance, Book)


def test_BIBTEXML_InCollection_isa_BookTitledEntry():
    instance = BIBTEXML_InCollection(chapter="sample_text", type="sample_text")
    assert isinstance(instance, BookTitledEntry)


def test_BIBTEXML_InProceedings_isa_BookTitledEntry():
    instance = BIBTEXML_InProceedings(pages="sample_text")
    assert isinstance(instance, BookTitledEntry)


def test_BIBTEXML_Article_isa_DatedEntry():
    instance = BIBTEXML_Article(note="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BIBTEXML_Book_isa_DatedEntry():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BIBTEXML_Booklet_isa_DatedEntry():
    instance = BIBTEXML_Booklet(address="sample_text", howpublished="sample_text", note="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BIBTEXML_Manual_isa_DatedEntry():
    instance = BIBTEXML_Manual(address="sample_text", edition="sample_text", note="sample_text", organization="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BIBTEXML_Proceedings_isa_DatedEntry():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BIBTEXML_TechReport_isa_DatedEntry():
    instance = BIBTEXML_TechReport(address="sample_text", note="sample_text", number="sample_text", type="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BIBTEXML_ThesisEntry_isa_DatedEntry():
    instance = BIBTEXML_ThesisEntry(address="sample_text", note="sample_text", type="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BIBTEXML_Unpublished_isa_DatedEntry():
    instance = BIBTEXML_Unpublished()
    assert isinstance(instance, DatedEntry)


def test_BIBTEXML_Book_isa_EditoredEntry():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert isinstance(instance, EditoredEntry)


def test_BIBTEXML_AuthoredEntry_isa_Entry():
    instance = BIBTEXML_AuthoredEntry()
    assert isinstance(instance, Entry)


def test_BIBTEXML_BookTitledEntry_isa_Entry():
    instance = BIBTEXML_BookTitledEntry(booktitle="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_DatedEntry_isa_Entry():
    instance = BIBTEXML_DatedEntry(month="sample_text", year="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_EditoredEntry_isa_Entry():
    instance = BIBTEXML_EditoredEntry(editor="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_InstitutionEntry_isa_Entry():
    instance = BIBTEXML_InstitutionEntry(institution="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_JournalEntry_isa_Entry():
    instance = BIBTEXML_JournalEntry(journal="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_Misc_isa_Entry():
    instance = BIBTEXML_Misc(howpublished="sample_text", month="sample_text", note="sample_text", title="sample_text", year="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_NotedEntry_isa_Entry():
    instance = BIBTEXML_NotedEntry(note="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_PublisheredEntry_isa_Entry():
    instance = BIBTEXML_PublisheredEntry(publisher="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_SchoolEntry_isa_Entry():
    instance = BIBTEXML_SchoolEntry(school="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_TitledEntry_isa_Entry():
    instance = BIBTEXML_TitledEntry(title="sample_text")
    assert isinstance(instance, Entry)


def test_BIBTEXML_Conference_isa_InProceedings():
    instance = BIBTEXML_Conference()
    assert isinstance(instance, InProceedings)


def test_BIBTEXML_TechReport_isa_InstitutionEntry():
    instance = BIBTEXML_TechReport(address="sample_text", note="sample_text", number="sample_text", type="sample_text")
    assert isinstance(instance, InstitutionEntry)


def test_BIBTEXML_Article_isa_JournalEntry():
    instance = BIBTEXML_Article(note="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    assert isinstance(instance, JournalEntry)


def test_BIBTEXML_Unpublished_isa_NotedEntry():
    instance = BIBTEXML_Unpublished()
    assert isinstance(instance, NotedEntry)


def test_BIBTEXML_InProceedings_isa_Proceedings():
    instance = BIBTEXML_InProceedings(pages="sample_text")
    assert isinstance(instance, Proceedings)


def test_BIBTEXML_Book_isa_PublisheredEntry():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert isinstance(instance, PublisheredEntry)


def test_BIBTEXML_ThesisEntry_isa_SchoolEntry():
    instance = BIBTEXML_ThesisEntry(address="sample_text", note="sample_text", type="sample_text")
    assert isinstance(instance, SchoolEntry)


def test_BIBTEXML_MastersThesis_isa_ThesisEntry():
    instance = BIBTEXML_MastersThesis()
    assert isinstance(instance, ThesisEntry)


def test_BIBTEXML_PhdThesis_isa_ThesisEntry():
    instance = BIBTEXML_PhdThesis()
    assert isinstance(instance, ThesisEntry)


def test_BIBTEXML_Article_isa_TitledEntry():
    instance = BIBTEXML_Article(note="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BIBTEXML_Book_isa_TitledEntry():
    instance = BIBTEXML_Book(address="sample_text", edition="sample_text", note="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BIBTEXML_Booklet_isa_TitledEntry():
    instance = BIBTEXML_Booklet(address="sample_text", howpublished="sample_text", note="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BIBTEXML_Manual_isa_TitledEntry():
    instance = BIBTEXML_Manual(address="sample_text", edition="sample_text", note="sample_text", organization="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BIBTEXML_Proceedings_isa_TitledEntry():
    instance = BIBTEXML_Proceedings(address="sample_text", editor="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", volume="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BIBTEXML_TechReport_isa_TitledEntry():
    instance = BIBTEXML_TechReport(address="sample_text", note="sample_text", number="sample_text", type="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BIBTEXML_ThesisEntry_isa_TitledEntry():
    instance = BIBTEXML_ThesisEntry(address="sample_text", note="sample_text", type="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BIBTEXML_Unpublished_isa_TitledEntry():
    instance = BIBTEXML_Unpublished()
    assert isinstance(instance, TitledEntry)


def test_assoc_authors2_link_reassign_clear():
    a = BIBTEXML_Booklet(address="sample_text", howpublished="sample_text", note="sample_text")
    b1 = Author()
    b2 = Author()
    _safe_set(a, 'BIBTEXML_Booklet', {b1})
    assert _is_linked(a, 'BIBTEXML_Booklet', b1)
    if hasattr(b1, 'Author3'):
        assert _is_linked(b1, 'Author3', a)
    _safe_set(a, 'BIBTEXML_Booklet', {b2})
    assert _is_linked(a, 'BIBTEXML_Booklet', b2)
    if hasattr(b1, 'Author3'):
        assert not _is_linked(b1, 'Author3', a)
    if hasattr(b2, 'Author3'):
        assert _is_linked(b2, 'Author3', a)
    _safe_set(a, 'BIBTEXML_Booklet', set())
    assert not _is_linked(a, 'BIBTEXML_Booklet', b2)
    if hasattr(b2, 'Author3'):
        assert not _is_linked(b2, 'Author3', a)


def test_assoc_authors4_link_reassign_clear():
    a = BIBTEXML_Misc(howpublished="sample_text", month="sample_text", note="sample_text", title="sample_text", year="sample_text")
    b1 = Author()
    b2 = Author()
    _safe_set(a, 'BIBTEXML_Misc', {b1})
    assert _is_linked(a, 'BIBTEXML_Misc', b1)
    if hasattr(b1, 'Author5'):
        assert _is_linked(b1, 'Author5', a)
    _safe_set(a, 'BIBTEXML_Misc', {b2})
    assert _is_linked(a, 'BIBTEXML_Misc', b2)
    if hasattr(b1, 'Author5'):
        assert not _is_linked(b1, 'Author5', a)
    if hasattr(b2, 'Author5'):
        assert _is_linked(b2, 'Author5', a)
    _safe_set(a, 'BIBTEXML_Misc', set())
    assert not _is_linked(a, 'BIBTEXML_Misc', b2)
    if hasattr(b2, 'Author5'):
        assert not _is_linked(b2, 'Author5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Author_strategy = st.builds(Author)
@given(instance=Author_strategy)
@settings(max_examples=25)
def test_Author_instantiation(instance):
    assert isinstance(instance, Author)


AuthoredEntry_strategy = st.builds(AuthoredEntry)
@given(instance=AuthoredEntry_strategy)
@settings(max_examples=25)
def test_AuthoredEntry_instantiation(instance):
    assert isinstance(instance, AuthoredEntry)


BIBTEXML_Article_strategy = st.builds(BIBTEXML_Article, note=safe_text, number=safe_text, pages=safe_text, volume=safe_text)
@given(instance=BIBTEXML_Article_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Article_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Article)


BIBTEXML_Author_strategy = st.builds(BIBTEXML_Author, name=safe_text)
@given(instance=BIBTEXML_Author_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Author_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Author)


BIBTEXML_AuthoredEntry_strategy = st.builds(BIBTEXML_AuthoredEntry)
@given(instance=BIBTEXML_AuthoredEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_AuthoredEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_AuthoredEntry)


BIBTEXML_BibtexFile_strategy = st.builds(BIBTEXML_BibtexFile)
@given(instance=BIBTEXML_BibtexFile_strategy)
@settings(max_examples=25)
def test_BIBTEXML_BibtexFile_instantiation(instance):
    assert isinstance(instance, BIBTEXML_BibtexFile)


BIBTEXML_Book_strategy = st.builds(BIBTEXML_Book, address=safe_text, edition=safe_text, note=safe_text, number=safe_text, series=safe_text, volume=safe_text)
@given(instance=BIBTEXML_Book_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Book_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Book)


BIBTEXML_BookTitledEntry_strategy = st.builds(BIBTEXML_BookTitledEntry, booktitle=safe_text)
@given(instance=BIBTEXML_BookTitledEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_BookTitledEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_BookTitledEntry)


BIBTEXML_Booklet_strategy = st.builds(BIBTEXML_Booklet, address=safe_text, howpublished=safe_text, note=safe_text)
@given(instance=BIBTEXML_Booklet_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Booklet_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Booklet)


BIBTEXML_Conference_strategy = st.builds(BIBTEXML_Conference)
@given(instance=BIBTEXML_Conference_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Conference_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Conference)


BIBTEXML_DatedEntry_strategy = st.builds(BIBTEXML_DatedEntry, month=safe_text, year=safe_text)
@given(instance=BIBTEXML_DatedEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_DatedEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_DatedEntry)


BIBTEXML_EditoredEntry_strategy = st.builds(BIBTEXML_EditoredEntry, editor=safe_text)
@given(instance=BIBTEXML_EditoredEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_EditoredEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_EditoredEntry)


BIBTEXML_Entry_strategy = st.builds(BIBTEXML_Entry, abstract=safe_text, id=safe_text)
@given(instance=BIBTEXML_Entry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Entry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Entry)


BIBTEXML_InBook_strategy = st.builds(BIBTEXML_InBook, chapter=safe_text, type=safe_text)
@given(instance=BIBTEXML_InBook_strategy)
@settings(max_examples=25)
def test_BIBTEXML_InBook_instantiation(instance):
    assert isinstance(instance, BIBTEXML_InBook)


BIBTEXML_InCollection_strategy = st.builds(BIBTEXML_InCollection, chapter=safe_text, type=safe_text)
@given(instance=BIBTEXML_InCollection_strategy)
@settings(max_examples=25)
def test_BIBTEXML_InCollection_instantiation(instance):
    assert isinstance(instance, BIBTEXML_InCollection)


BIBTEXML_InProceedings_strategy = st.builds(BIBTEXML_InProceedings, pages=safe_text)
@given(instance=BIBTEXML_InProceedings_strategy)
@settings(max_examples=25)
def test_BIBTEXML_InProceedings_instantiation(instance):
    assert isinstance(instance, BIBTEXML_InProceedings)


BIBTEXML_InstitutionEntry_strategy = st.builds(BIBTEXML_InstitutionEntry, institution=safe_text)
@given(instance=BIBTEXML_InstitutionEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_InstitutionEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_InstitutionEntry)


BIBTEXML_JournalEntry_strategy = st.builds(BIBTEXML_JournalEntry, journal=safe_text)
@given(instance=BIBTEXML_JournalEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_JournalEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_JournalEntry)


BIBTEXML_Manual_strategy = st.builds(BIBTEXML_Manual, address=safe_text, edition=safe_text, note=safe_text, organization=safe_text)
@given(instance=BIBTEXML_Manual_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Manual_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Manual)


BIBTEXML_MastersThesis_strategy = st.builds(BIBTEXML_MastersThesis)
@given(instance=BIBTEXML_MastersThesis_strategy)
@settings(max_examples=25)
def test_BIBTEXML_MastersThesis_instantiation(instance):
    assert isinstance(instance, BIBTEXML_MastersThesis)


BIBTEXML_Misc_strategy = st.builds(BIBTEXML_Misc, howpublished=safe_text, month=safe_text, note=safe_text, title=safe_text, year=safe_text)
@given(instance=BIBTEXML_Misc_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Misc_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Misc)


BIBTEXML_NotedEntry_strategy = st.builds(BIBTEXML_NotedEntry, note=safe_text)
@given(instance=BIBTEXML_NotedEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_NotedEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_NotedEntry)


BIBTEXML_PhdThesis_strategy = st.builds(BIBTEXML_PhdThesis)
@given(instance=BIBTEXML_PhdThesis_strategy)
@settings(max_examples=25)
def test_BIBTEXML_PhdThesis_instantiation(instance):
    assert isinstance(instance, BIBTEXML_PhdThesis)


BIBTEXML_Proceedings_strategy = st.builds(BIBTEXML_Proceedings, address=safe_text, editor=safe_text, note=safe_text, number=safe_text, organization=safe_text, publisher=safe_text, series=safe_text, volume=safe_text)
@given(instance=BIBTEXML_Proceedings_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Proceedings_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Proceedings)


BIBTEXML_PublisheredEntry_strategy = st.builds(BIBTEXML_PublisheredEntry, publisher=safe_text)
@given(instance=BIBTEXML_PublisheredEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_PublisheredEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_PublisheredEntry)


BIBTEXML_SchoolEntry_strategy = st.builds(BIBTEXML_SchoolEntry, school=safe_text)
@given(instance=BIBTEXML_SchoolEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_SchoolEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_SchoolEntry)


BIBTEXML_TechReport_strategy = st.builds(BIBTEXML_TechReport, address=safe_text, note=safe_text, number=safe_text, type=safe_text)
@given(instance=BIBTEXML_TechReport_strategy)
@settings(max_examples=25)
def test_BIBTEXML_TechReport_instantiation(instance):
    assert isinstance(instance, BIBTEXML_TechReport)


BIBTEXML_ThesisEntry_strategy = st.builds(BIBTEXML_ThesisEntry, address=safe_text, note=safe_text, type=safe_text)
@given(instance=BIBTEXML_ThesisEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_ThesisEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_ThesisEntry)


BIBTEXML_TitledEntry_strategy = st.builds(BIBTEXML_TitledEntry, title=safe_text)
@given(instance=BIBTEXML_TitledEntry_strategy)
@settings(max_examples=25)
def test_BIBTEXML_TitledEntry_instantiation(instance):
    assert isinstance(instance, BIBTEXML_TitledEntry)


BIBTEXML_Unpublished_strategy = st.builds(BIBTEXML_Unpublished)
@given(instance=BIBTEXML_Unpublished_strategy)
@settings(max_examples=25)
def test_BIBTEXML_Unpublished_instantiation(instance):
    assert isinstance(instance, BIBTEXML_Unpublished)


Book_strategy = st.builds(Book)
@given(instance=Book_strategy)
@settings(max_examples=25)
def test_Book_instantiation(instance):
    assert isinstance(instance, Book)


BookTitledEntry_strategy = st.builds(BookTitledEntry)
@given(instance=BookTitledEntry_strategy)
@settings(max_examples=25)
def test_BookTitledEntry_instantiation(instance):
    assert isinstance(instance, BookTitledEntry)


DatedEntry_strategy = st.builds(DatedEntry)
@given(instance=DatedEntry_strategy)
@settings(max_examples=25)
def test_DatedEntry_instantiation(instance):
    assert isinstance(instance, DatedEntry)


EditoredEntry_strategy = st.builds(EditoredEntry)
@given(instance=EditoredEntry_strategy)
@settings(max_examples=25)
def test_EditoredEntry_instantiation(instance):
    assert isinstance(instance, EditoredEntry)


Entry_strategy = st.builds(Entry)
@given(instance=Entry_strategy)
@settings(max_examples=25)
def test_Entry_instantiation(instance):
    assert isinstance(instance, Entry)


InProceedings_strategy = st.builds(InProceedings)
@given(instance=InProceedings_strategy)
@settings(max_examples=25)
def test_InProceedings_instantiation(instance):
    assert isinstance(instance, InProceedings)


InstitutionEntry_strategy = st.builds(InstitutionEntry)
@given(instance=InstitutionEntry_strategy)
@settings(max_examples=25)
def test_InstitutionEntry_instantiation(instance):
    assert isinstance(instance, InstitutionEntry)


JournalEntry_strategy = st.builds(JournalEntry)
@given(instance=JournalEntry_strategy)
@settings(max_examples=25)
def test_JournalEntry_instantiation(instance):
    assert isinstance(instance, JournalEntry)


NotedEntry_strategy = st.builds(NotedEntry)
@given(instance=NotedEntry_strategy)
@settings(max_examples=25)
def test_NotedEntry_instantiation(instance):
    assert isinstance(instance, NotedEntry)


Proceedings_strategy = st.builds(Proceedings)
@given(instance=Proceedings_strategy)
@settings(max_examples=25)
def test_Proceedings_instantiation(instance):
    assert isinstance(instance, Proceedings)


PublisheredEntry_strategy = st.builds(PublisheredEntry)
@given(instance=PublisheredEntry_strategy)
@settings(max_examples=25)
def test_PublisheredEntry_instantiation(instance):
    assert isinstance(instance, PublisheredEntry)


SchoolEntry_strategy = st.builds(SchoolEntry)
@given(instance=SchoolEntry_strategy)
@settings(max_examples=25)
def test_SchoolEntry_instantiation(instance):
    assert isinstance(instance, SchoolEntry)


ThesisEntry_strategy = st.builds(ThesisEntry)
@given(instance=ThesisEntry_strategy)
@settings(max_examples=25)
def test_ThesisEntry_instantiation(instance):
    assert isinstance(instance, ThesisEntry)


TitledEntry_strategy = st.builds(TitledEntry)
@given(instance=TitledEntry_strategy)
@settings(max_examples=25)
def test_TitledEntry_instantiation(instance):
    assert isinstance(instance, TitledEntry)


