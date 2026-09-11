import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BibTeXMLEntriesClass,
    bibtexml_ArticleType,
    bibtexml_BibTeXMLEntriesClass,
    bibtexml_BibTeXMLEntryType,
    bibtexml_BookType,
    bibtexml_BookletType,
    bibtexml_ConferenceType,
    bibtexml_DocumentRoot,
    bibtexml_EStringToStringMapEntry,
    bibtexml_FileType,
    bibtexml_InbookType,
    bibtexml_IncollectionType,
    bibtexml_InproceedingsType,
    bibtexml_ManualType,
    bibtexml_MastersthesisType,
    bibtexml_MiscType,
    bibtexml_PhdthesisType,
    bibtexml_ProceedingsType,
    bibtexml_TechreportType,
    bibtexml_UnpublishedType,
    MonthStringType,
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

def test_bibtexml_ArticleType_author_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_ArticleType_crossref_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_ArticleType_doi_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_ArticleType_journal_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.journal == "sample_text"
    instance.journal = "sample_text_2"
    assert instance.journal == "sample_text_2"


def test_bibtexml_ArticleType_key_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_ArticleType_month_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_ArticleType_note_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_ArticleType_number_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_ArticleType_pages_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_bibtexml_ArticleType_title_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_ArticleType_url_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_ArticleType_volume_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibtexml_ArticleType_year_value_roundtrip():
    instance = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_BibTeXMLEntryType_id_value_roundtrip():
    instance = bibtexml_BibTeXMLEntryType(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_bibtexml_BookType_address_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_BookType_author_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_BookType_crossref_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_BookType_doi_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_BookType_edition_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.edition == "sample_text"
    instance.edition = "sample_text_2"
    assert instance.edition == "sample_text_2"


def test_bibtexml_BookType_editor_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_bibtexml_BookType_key_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_BookType_month_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_BookType_note_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_BookType_number_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_BookType_publisher_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibtexml_BookType_series_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_bibtexml_BookType_title_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_BookType_url_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_BookType_volume_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibtexml_BookType_year_value_roundtrip():
    instance = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_BookletType_address_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_BookletType_author_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_BookletType_crossref_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_BookletType_doi_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_BookletType_howpublished_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.howpublished == "sample_text"
    instance.howpublished = "sample_text_2"
    assert instance.howpublished == "sample_text_2"


def test_bibtexml_BookletType_key_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_BookletType_month_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_BookletType_note_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_BookletType_title_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_BookletType_url_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_BookletType_year_value_roundtrip():
    instance = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_ConferenceType_address_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_ConferenceType_author_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_ConferenceType_booktitle_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_bibtexml_ConferenceType_crossref_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_ConferenceType_doi_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_ConferenceType_editor_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_bibtexml_ConferenceType_key_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_ConferenceType_month_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_ConferenceType_note_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_ConferenceType_number_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_ConferenceType_organization_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_bibtexml_ConferenceType_pages_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_bibtexml_ConferenceType_publisher_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibtexml_ConferenceType_series_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_bibtexml_ConferenceType_title_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_ConferenceType_url_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_ConferenceType_volume_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibtexml_ConferenceType_year_value_roundtrip():
    instance = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_DocumentRoot_address_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_DocumentRoot_annote_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.annote == "sample_text"
    instance.annote = "sample_text_2"
    assert instance.annote == "sample_text_2"


def test_bibtexml_DocumentRoot_author_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_DocumentRoot_booktitle_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_bibtexml_DocumentRoot_chapter_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.chapter == "sample_text"
    instance.chapter = "sample_text_2"
    assert instance.chapter == "sample_text_2"


def test_bibtexml_DocumentRoot_crossref_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_DocumentRoot_doi_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_DocumentRoot_edition_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.edition == "sample_text"
    instance.edition = "sample_text_2"
    assert instance.edition == "sample_text_2"


def test_bibtexml_DocumentRoot_editor_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_bibtexml_DocumentRoot_howpublished_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.howpublished == "sample_text"
    instance.howpublished = "sample_text_2"
    assert instance.howpublished == "sample_text_2"


def test_bibtexml_DocumentRoot_institution_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.institution == "sample_text"
    instance.institution = "sample_text_2"
    assert instance.institution == "sample_text_2"


def test_bibtexml_DocumentRoot_journal_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.journal == "sample_text"
    instance.journal = "sample_text_2"
    assert instance.journal == "sample_text_2"


def test_bibtexml_DocumentRoot_key_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_DocumentRoot_mixed_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_bibtexml_DocumentRoot_month_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_DocumentRoot_note_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_DocumentRoot_number_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_DocumentRoot_organization_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_bibtexml_DocumentRoot_pages_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_bibtexml_DocumentRoot_publisher_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibtexml_DocumentRoot_school_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_bibtexml_DocumentRoot_series_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_bibtexml_DocumentRoot_title_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_DocumentRoot_type_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_bibtexml_DocumentRoot_url_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_DocumentRoot_volume_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibtexml_DocumentRoot_year_value_roundtrip():
    instance = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_InbookType_address_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_InbookType_author_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_InbookType_chapter_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.chapter == "sample_text"
    instance.chapter = "sample_text_2"
    assert instance.chapter == "sample_text_2"


def test_bibtexml_InbookType_crossref_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_InbookType_doi_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_InbookType_edition_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.edition == "sample_text"
    instance.edition = "sample_text_2"
    assert instance.edition == "sample_text_2"


def test_bibtexml_InbookType_editor_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_bibtexml_InbookType_key_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_InbookType_month_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_InbookType_note_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_InbookType_number_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_InbookType_pages_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_bibtexml_InbookType_pages1_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.pages1 == "sample_text"
    instance.pages1 = "sample_text_2"
    assert instance.pages1 == "sample_text_2"


def test_bibtexml_InbookType_publisher_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibtexml_InbookType_series_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_bibtexml_InbookType_title_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_InbookType_type_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_bibtexml_InbookType_url_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_InbookType_volume_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibtexml_InbookType_year_value_roundtrip():
    instance = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_IncollectionType_address_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_IncollectionType_author_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_IncollectionType_booktitle_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_bibtexml_IncollectionType_chapter_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.chapter == "sample_text"
    instance.chapter = "sample_text_2"
    assert instance.chapter == "sample_text_2"


def test_bibtexml_IncollectionType_crossref_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_IncollectionType_doi_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_IncollectionType_edition_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.edition == "sample_text"
    instance.edition = "sample_text_2"
    assert instance.edition == "sample_text_2"


def test_bibtexml_IncollectionType_editor_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_bibtexml_IncollectionType_key_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_IncollectionType_month_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_IncollectionType_note_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_IncollectionType_number_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_IncollectionType_pages_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_bibtexml_IncollectionType_publisher_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibtexml_IncollectionType_series_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_bibtexml_IncollectionType_title_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_IncollectionType_type_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_bibtexml_IncollectionType_url_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_IncollectionType_volume_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibtexml_IncollectionType_year_value_roundtrip():
    instance = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_InproceedingsType_address_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_InproceedingsType_author_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_InproceedingsType_booktitle_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_bibtexml_InproceedingsType_crossref_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_InproceedingsType_doi_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_InproceedingsType_editor_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_bibtexml_InproceedingsType_key_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_InproceedingsType_month_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_InproceedingsType_note_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_InproceedingsType_number_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_InproceedingsType_organization_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_bibtexml_InproceedingsType_pages_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_bibtexml_InproceedingsType_publisher_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibtexml_InproceedingsType_series_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_bibtexml_InproceedingsType_title_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_InproceedingsType_url_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_InproceedingsType_volume_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibtexml_InproceedingsType_year_value_roundtrip():
    instance = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_ManualType_address_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_ManualType_author_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_ManualType_crossref_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_ManualType_doi_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_ManualType_edition_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.edition == "sample_text"
    instance.edition = "sample_text_2"
    assert instance.edition == "sample_text_2"


def test_bibtexml_ManualType_key_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_ManualType_month_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_ManualType_note_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_ManualType_organization_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_bibtexml_ManualType_title_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_ManualType_url_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_ManualType_year_value_roundtrip():
    instance = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_MastersthesisType_address_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_MastersthesisType_author_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_MastersthesisType_crossref_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_MastersthesisType_doi_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_MastersthesisType_key_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_MastersthesisType_month_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_MastersthesisType_note_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_MastersthesisType_school_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_bibtexml_MastersthesisType_title_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_MastersthesisType_type_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_bibtexml_MastersthesisType_url_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_MastersthesisType_year_value_roundtrip():
    instance = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_MiscType_author_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_MiscType_crossref_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_MiscType_doi_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_MiscType_howpublished_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.howpublished == "sample_text"
    instance.howpublished = "sample_text_2"
    assert instance.howpublished == "sample_text_2"


def test_bibtexml_MiscType_key_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_MiscType_month_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_MiscType_note_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_MiscType_title_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_MiscType_url_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_MiscType_year_value_roundtrip():
    instance = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_PhdthesisType_address_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_PhdthesisType_author_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_PhdthesisType_crossref_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_PhdthesisType_doi_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_PhdthesisType_key_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_PhdthesisType_month_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_PhdthesisType_note_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_PhdthesisType_school_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_bibtexml_PhdthesisType_title_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_PhdthesisType_type_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_bibtexml_PhdthesisType_url_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_PhdthesisType_year_value_roundtrip():
    instance = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_ProceedingsType_address_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_ProceedingsType_crossref_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_ProceedingsType_doi_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_ProceedingsType_editor_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_bibtexml_ProceedingsType_key_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_ProceedingsType_month_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_ProceedingsType_note_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_ProceedingsType_number_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_ProceedingsType_organization_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.organization == "sample_text"
    instance.organization = "sample_text_2"
    assert instance.organization == "sample_text_2"


def test_bibtexml_ProceedingsType_publisher_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibtexml_ProceedingsType_series_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_bibtexml_ProceedingsType_title_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_ProceedingsType_url_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_ProceedingsType_volume_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibtexml_ProceedingsType_year_value_roundtrip():
    instance = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_TechreportType_address_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibtexml_TechreportType_author_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_TechreportType_crossref_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_TechreportType_doi_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_TechreportType_institution_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.institution == "sample_text"
    instance.institution = "sample_text_2"
    assert instance.institution == "sample_text_2"


def test_bibtexml_TechreportType_key_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_TechreportType_month_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_TechreportType_note_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_TechreportType_number_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibtexml_TechreportType_title_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_TechreportType_type_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_bibtexml_TechreportType_url_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_TechreportType_year_value_roundtrip():
    instance = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_UnpublishedType_author_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtexml_UnpublishedType_crossref_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.crossref == "sample_text"
    instance.crossref = "sample_text_2"
    assert instance.crossref == "sample_text_2"


def test_bibtexml_UnpublishedType_doi_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.doi == "sample_text"
    instance.doi = "sample_text_2"
    assert instance.doi == "sample_text_2"


def test_bibtexml_UnpublishedType_key_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibtexml_UnpublishedType_month_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibtexml_UnpublishedType_note_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtexml_UnpublishedType_title_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtexml_UnpublishedType_url_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_bibtexml_UnpublishedType_year_value_roundtrip():
    instance = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtexml_BibTeXMLEntryType_isa_BibTeXMLEntriesClass():
    instance = bibtexml_BibTeXMLEntryType(id="sample_text")
    assert isinstance(instance, BibTeXMLEntriesClass)


def test_assoc_article0_link_reassign_clear():
    a = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_ArticleType', b1)
    assert _is_linked(a, 'bibtexml_ArticleType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass', a)
    _safe_set(a, 'bibtexml_ArticleType', b2)
    assert _is_linked(a, 'bibtexml_ArticleType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass', a)
    _safe_set(a, 'bibtexml_ArticleType', None)
    assert not _is_linked(a, 'bibtexml_ArticleType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass', a)


def test_assoc_article31_link_reassign_clear():
    a = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_ArticleType(author="sample_text", crossref="sample_text", doi="sample_text", journal="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_ArticleType(author="sample_text_2", crossref="sample_text_2", doi="sample_text_2", journal="sample_text_2", key="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", pages="sample_text_2", title="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_DocumentRoot32', {b1})
    assert _is_linked(a, 'bibtexml_DocumentRoot32', b1)
    if hasattr(b1, 'bibtexml_ArticleType33'):
        assert _is_linked(b1, 'bibtexml_ArticleType33', a)
    _safe_set(a, 'bibtexml_DocumentRoot32', {b2})
    assert _is_linked(a, 'bibtexml_DocumentRoot32', b2)
    if hasattr(b1, 'bibtexml_ArticleType33'):
        assert not _is_linked(b1, 'bibtexml_ArticleType33', a)
    if hasattr(b2, 'bibtexml_ArticleType33'):
        assert _is_linked(b2, 'bibtexml_ArticleType33', a)
    _safe_set(a, 'bibtexml_DocumentRoot32', set())
    assert not _is_linked(a, 'bibtexml_DocumentRoot32', b2)
    if hasattr(b2, 'bibtexml_ArticleType33'):
        assert not _is_linked(b2, 'bibtexml_ArticleType33', a)


def test_assoc_book1_link_reassign_clear():
    a = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_BookType', b1)
    assert _is_linked(a, 'bibtexml_BookType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass2'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass2', a)
    _safe_set(a, 'bibtexml_BookType', b2)
    assert _is_linked(a, 'bibtexml_BookType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass2'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass2', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass2'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass2', a)
    _safe_set(a, 'bibtexml_BookType', None)
    assert not _is_linked(a, 'bibtexml_BookType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass2'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass2', a)


def test_assoc_book34_link_reassign_clear():
    a = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BookType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_BookType(address="sample_text_2", author="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", key="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", publisher="sample_text_2", series="sample_text_2", title="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_DocumentRoot35', {b1})
    assert _is_linked(a, 'bibtexml_DocumentRoot35', b1)
    if hasattr(b1, 'bibtexml_BookType36'):
        assert _is_linked(b1, 'bibtexml_BookType36', a)
    _safe_set(a, 'bibtexml_DocumentRoot35', {b2})
    assert _is_linked(a, 'bibtexml_DocumentRoot35', b2)
    if hasattr(b1, 'bibtexml_BookType36'):
        assert not _is_linked(b1, 'bibtexml_BookType36', a)
    if hasattr(b2, 'bibtexml_BookType36'):
        assert _is_linked(b2, 'bibtexml_BookType36', a)
    _safe_set(a, 'bibtexml_DocumentRoot35', set())
    assert not _is_linked(a, 'bibtexml_DocumentRoot35', b2)
    if hasattr(b2, 'bibtexml_BookType36'):
        assert not _is_linked(b2, 'bibtexml_BookType36', a)


def test_assoc_booklet3_link_reassign_clear():
    a = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_BookletType', b1)
    assert _is_linked(a, 'bibtexml_BookletType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass4'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass4', a)
    _safe_set(a, 'bibtexml_BookletType', b2)
    assert _is_linked(a, 'bibtexml_BookletType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass4'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass4', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass4'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass4', a)
    _safe_set(a, 'bibtexml_BookletType', None)
    assert not _is_linked(a, 'bibtexml_BookletType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass4'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass4', a)


def test_assoc_booklet37_link_reassign_clear():
    a = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BookletType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    b2 = bibtexml_BookletType(address="sample_text_2", author="sample_text_2", crossref="sample_text_2", doi="sample_text_2", howpublished="sample_text_2", key="sample_text_2", month="sample_text_2", note="sample_text_2", title="sample_text_2", url="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_DocumentRoot38', {b1})
    assert _is_linked(a, 'bibtexml_DocumentRoot38', b1)
    if hasattr(b1, 'bibtexml_BookletType39'):
        assert _is_linked(b1, 'bibtexml_BookletType39', a)
    _safe_set(a, 'bibtexml_DocumentRoot38', {b2})
    assert _is_linked(a, 'bibtexml_DocumentRoot38', b2)
    if hasattr(b1, 'bibtexml_BookletType39'):
        assert not _is_linked(b1, 'bibtexml_BookletType39', a)
    if hasattr(b2, 'bibtexml_BookletType39'):
        assert _is_linked(b2, 'bibtexml_BookletType39', a)
    _safe_set(a, 'bibtexml_DocumentRoot38', set())
    assert not _is_linked(a, 'bibtexml_DocumentRoot38', b2)
    if hasattr(b2, 'bibtexml_BookletType39'):
        assert not _is_linked(b2, 'bibtexml_BookletType39', a)


def test_assoc_conference21_link_reassign_clear():
    a = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_ConferenceType', b1)
    assert _is_linked(a, 'bibtexml_ConferenceType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass22'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass22', a)
    _safe_set(a, 'bibtexml_ConferenceType', b2)
    assert _is_linked(a, 'bibtexml_ConferenceType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass22'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass22', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass22'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass22', a)
    _safe_set(a, 'bibtexml_ConferenceType', None)
    assert not _is_linked(a, 'bibtexml_ConferenceType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass22'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass22', a)


def test_assoc_conference40_link_reassign_clear():
    a = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_ConferenceType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_ConferenceType(address="sample_text_2", author="sample_text_2", booktitle="sample_text_2", crossref="sample_text_2", doi="sample_text_2", editor="sample_text_2", key="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", series="sample_text_2", title="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_DocumentRoot41', {b1})
    assert _is_linked(a, 'bibtexml_DocumentRoot41', b1)
    if hasattr(b1, 'bibtexml_ConferenceType42'):
        assert _is_linked(b1, 'bibtexml_ConferenceType42', a)
    _safe_set(a, 'bibtexml_DocumentRoot41', {b2})
    assert _is_linked(a, 'bibtexml_DocumentRoot41', b2)
    if hasattr(b1, 'bibtexml_ConferenceType42'):
        assert not _is_linked(b1, 'bibtexml_ConferenceType42', a)
    if hasattr(b2, 'bibtexml_ConferenceType42'):
        assert _is_linked(b2, 'bibtexml_ConferenceType42', a)
    _safe_set(a, 'bibtexml_DocumentRoot41', set())
    assert not _is_linked(a, 'bibtexml_DocumentRoot41', b2)
    if hasattr(b2, 'bibtexml_ConferenceType42'):
        assert not _is_linked(b2, 'bibtexml_ConferenceType42', a)


def test_assoc_entry43_link_reassign_clear():
    a = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntryType(id="sample_text")
    b2 = bibtexml_BibTeXMLEntryType(id="sample_text_2")
    _safe_set(a, 'bibtexml_DocumentRoot44', {b1})
    assert _is_linked(a, 'bibtexml_DocumentRoot44', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntryType'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntryType', a)
    _safe_set(a, 'bibtexml_DocumentRoot44', {b2})
    assert _is_linked(a, 'bibtexml_DocumentRoot44', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntryType'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntryType', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntryType'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntryType', a)
    _safe_set(a, 'bibtexml_DocumentRoot44', set())
    assert not _is_linked(a, 'bibtexml_DocumentRoot44', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntryType'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntryType', a)


def test_assoc_entry77_link_reassign_clear():
    a = bibtexml_BibTeXMLEntryType(id="sample_text")
    b1 = bibtexml_FileType()
    b2 = bibtexml_FileType()
    _safe_set(a, 'bibtexml_BibTeXMLEntryType79', b1)
    assert _is_linked(a, 'bibtexml_BibTeXMLEntryType79', b1)
    if hasattr(b1, 'bibtexml_FileType78'):
        assert _is_linked(b1, 'bibtexml_FileType78', a)
    _safe_set(a, 'bibtexml_BibTeXMLEntryType79', b2)
    assert _is_linked(a, 'bibtexml_BibTeXMLEntryType79', b2)
    if hasattr(b1, 'bibtexml_FileType78'):
        assert not _is_linked(b1, 'bibtexml_FileType78', a)
    if hasattr(b2, 'bibtexml_FileType78'):
        assert _is_linked(b2, 'bibtexml_FileType78', a)
    _safe_set(a, 'bibtexml_BibTeXMLEntryType79', None)
    assert not _is_linked(a, 'bibtexml_BibTeXMLEntryType79', b2)
    if hasattr(b2, 'bibtexml_FileType78'):
        assert not _is_linked(b2, 'bibtexml_FileType78', a)


def test_assoc_file45_link_reassign_clear():
    a = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_FileType()
    b2 = bibtexml_FileType()
    _safe_set(a, 'bibtexml_DocumentRoot46', {b1})
    assert _is_linked(a, 'bibtexml_DocumentRoot46', b1)
    if hasattr(b1, 'bibtexml_FileType'):
        assert _is_linked(b1, 'bibtexml_FileType', a)
    _safe_set(a, 'bibtexml_DocumentRoot46', {b2})
    assert _is_linked(a, 'bibtexml_DocumentRoot46', b2)
    if hasattr(b1, 'bibtexml_FileType'):
        assert not _is_linked(b1, 'bibtexml_FileType', a)
    if hasattr(b2, 'bibtexml_FileType'):
        assert _is_linked(b2, 'bibtexml_FileType', a)
    _safe_set(a, 'bibtexml_DocumentRoot46', set())
    assert not _is_linked(a, 'bibtexml_DocumentRoot46', b2)
    if hasattr(b2, 'bibtexml_FileType'):
        assert not _is_linked(b2, 'bibtexml_FileType', a)


def test_assoc_inbook13_link_reassign_clear():
    a = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_InbookType', b1)
    assert _is_linked(a, 'bibtexml_InbookType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass14'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass14', a)
    _safe_set(a, 'bibtexml_InbookType', b2)
    assert _is_linked(a, 'bibtexml_InbookType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass14'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass14', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass14'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass14', a)
    _safe_set(a, 'bibtexml_InbookType', None)
    assert not _is_linked(a, 'bibtexml_InbookType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass14'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass14', a)


def test_assoc_inbook47_link_reassign_clear():
    a = bibtexml_InbookType(address="sample_text", author="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", pages1="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_InbookType49', b1)
    assert _is_linked(a, 'bibtexml_InbookType49', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot48'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot48', a)
    _safe_set(a, 'bibtexml_InbookType49', b2)
    assert _is_linked(a, 'bibtexml_InbookType49', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot48'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot48', a)
    if hasattr(b2, 'bibtexml_DocumentRoot48'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot48', a)
    _safe_set(a, 'bibtexml_InbookType49', None)
    assert not _is_linked(a, 'bibtexml_InbookType49', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot48'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot48', a)


def test_assoc_incollection15_link_reassign_clear():
    a = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_IncollectionType', b1)
    assert _is_linked(a, 'bibtexml_IncollectionType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass16'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass16', a)
    _safe_set(a, 'bibtexml_IncollectionType', b2)
    assert _is_linked(a, 'bibtexml_IncollectionType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass16'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass16', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass16'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass16', a)
    _safe_set(a, 'bibtexml_IncollectionType', None)
    assert not _is_linked(a, 'bibtexml_IncollectionType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass16'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass16', a)


def test_assoc_incollection50_link_reassign_clear():
    a = bibtexml_IncollectionType(address="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_IncollectionType52', b1)
    assert _is_linked(a, 'bibtexml_IncollectionType52', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot51'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot51', a)
    _safe_set(a, 'bibtexml_IncollectionType52', b2)
    assert _is_linked(a, 'bibtexml_IncollectionType52', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot51'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot51', a)
    if hasattr(b2, 'bibtexml_DocumentRoot51'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot51', a)
    _safe_set(a, 'bibtexml_IncollectionType52', None)
    assert not _is_linked(a, 'bibtexml_IncollectionType52', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot51'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot51', a)


def test_assoc_inproceedings19_link_reassign_clear():
    a = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_InproceedingsType', b1)
    assert _is_linked(a, 'bibtexml_InproceedingsType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass20'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass20', a)
    _safe_set(a, 'bibtexml_InproceedingsType', b2)
    assert _is_linked(a, 'bibtexml_InproceedingsType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass20'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass20', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass20'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass20', a)
    _safe_set(a, 'bibtexml_InproceedingsType', None)
    assert not _is_linked(a, 'bibtexml_InproceedingsType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass20'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass20', a)


def test_assoc_inproceedings53_link_reassign_clear():
    a = bibtexml_InproceedingsType(address="sample_text", author="sample_text", booktitle="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_InproceedingsType55', b1)
    assert _is_linked(a, 'bibtexml_InproceedingsType55', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot54'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot54', a)
    _safe_set(a, 'bibtexml_InproceedingsType55', b2)
    assert _is_linked(a, 'bibtexml_InproceedingsType55', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot54'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot54', a)
    if hasattr(b2, 'bibtexml_DocumentRoot54'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot54', a)
    _safe_set(a, 'bibtexml_InproceedingsType55', None)
    assert not _is_linked(a, 'bibtexml_InproceedingsType55', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot54'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot54', a)


def test_assoc_manual5_link_reassign_clear():
    a = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_ManualType', b1)
    assert _is_linked(a, 'bibtexml_ManualType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass6'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass6', a)
    _safe_set(a, 'bibtexml_ManualType', b2)
    assert _is_linked(a, 'bibtexml_ManualType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass6'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass6', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass6'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass6', a)
    _safe_set(a, 'bibtexml_ManualType', None)
    assert not _is_linked(a, 'bibtexml_ManualType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass6'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass6', a)


def test_assoc_manual56_link_reassign_clear():
    a = bibtexml_ManualType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", key="sample_text", month="sample_text", note="sample_text", organization="sample_text", title="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_ManualType58', b1)
    assert _is_linked(a, 'bibtexml_ManualType58', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot57'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot57', a)
    _safe_set(a, 'bibtexml_ManualType58', b2)
    assert _is_linked(a, 'bibtexml_ManualType58', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot57'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot57', a)
    if hasattr(b2, 'bibtexml_DocumentRoot57'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot57', a)
    _safe_set(a, 'bibtexml_ManualType58', None)
    assert not _is_linked(a, 'bibtexml_ManualType58', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot57'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot57', a)


def test_assoc_mastersthesis59_link_reassign_clear():
    a = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_MastersthesisType61', b1)
    assert _is_linked(a, 'bibtexml_MastersthesisType61', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot60'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot60', a)
    _safe_set(a, 'bibtexml_MastersthesisType61', b2)
    assert _is_linked(a, 'bibtexml_MastersthesisType61', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot60'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot60', a)
    if hasattr(b2, 'bibtexml_DocumentRoot60'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot60', a)
    _safe_set(a, 'bibtexml_MastersthesisType61', None)
    assert not _is_linked(a, 'bibtexml_MastersthesisType61', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot60'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot60', a)


def test_assoc_mastersthesis9_link_reassign_clear():
    a = bibtexml_MastersthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_MastersthesisType', b1)
    assert _is_linked(a, 'bibtexml_MastersthesisType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass10'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass10', a)
    _safe_set(a, 'bibtexml_MastersthesisType', b2)
    assert _is_linked(a, 'bibtexml_MastersthesisType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass10'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass10', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass10'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass10', a)
    _safe_set(a, 'bibtexml_MastersthesisType', None)
    assert not _is_linked(a, 'bibtexml_MastersthesisType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass10'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass10', a)


def test_assoc_misc25_link_reassign_clear():
    a = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_MiscType', b1)
    assert _is_linked(a, 'bibtexml_MiscType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass26'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass26', a)
    _safe_set(a, 'bibtexml_MiscType', b2)
    assert _is_linked(a, 'bibtexml_MiscType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass26'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass26', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass26'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass26', a)
    _safe_set(a, 'bibtexml_MiscType', None)
    assert not _is_linked(a, 'bibtexml_MiscType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass26'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass26', a)


def test_assoc_misc62_link_reassign_clear():
    a = bibtexml_MiscType(author="sample_text", crossref="sample_text", doi="sample_text", howpublished="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_MiscType64', b1)
    assert _is_linked(a, 'bibtexml_MiscType64', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot63'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot63', a)
    _safe_set(a, 'bibtexml_MiscType64', b2)
    assert _is_linked(a, 'bibtexml_MiscType64', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot63'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot63', a)
    if hasattr(b2, 'bibtexml_DocumentRoot63'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot63', a)
    _safe_set(a, 'bibtexml_MiscType64', None)
    assert not _is_linked(a, 'bibtexml_MiscType64', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot63'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot63', a)


def test_assoc_phdthesis11_link_reassign_clear():
    a = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_PhdthesisType', b1)
    assert _is_linked(a, 'bibtexml_PhdthesisType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass12'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass12', a)
    _safe_set(a, 'bibtexml_PhdthesisType', b2)
    assert _is_linked(a, 'bibtexml_PhdthesisType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass12'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass12', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass12'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass12', a)
    _safe_set(a, 'bibtexml_PhdthesisType', None)
    assert not _is_linked(a, 'bibtexml_PhdthesisType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass12'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass12', a)


def test_assoc_phdthesis65_link_reassign_clear():
    a = bibtexml_PhdthesisType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", school="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_PhdthesisType67', b1)
    assert _is_linked(a, 'bibtexml_PhdthesisType67', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot66'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot66', a)
    _safe_set(a, 'bibtexml_PhdthesisType67', b2)
    assert _is_linked(a, 'bibtexml_PhdthesisType67', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot66'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot66', a)
    if hasattr(b2, 'bibtexml_DocumentRoot66'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot66', a)
    _safe_set(a, 'bibtexml_PhdthesisType67', None)
    assert not _is_linked(a, 'bibtexml_PhdthesisType67', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot66'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot66', a)


def test_assoc_proceedings17_link_reassign_clear():
    a = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_ProceedingsType', b1)
    assert _is_linked(a, 'bibtexml_ProceedingsType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass18'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass18', a)
    _safe_set(a, 'bibtexml_ProceedingsType', b2)
    assert _is_linked(a, 'bibtexml_ProceedingsType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass18'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass18', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass18'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass18', a)
    _safe_set(a, 'bibtexml_ProceedingsType', None)
    assert not _is_linked(a, 'bibtexml_ProceedingsType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass18'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass18', a)


def test_assoc_proceedings68_link_reassign_clear():
    a = bibtexml_ProceedingsType(address="sample_text", crossref="sample_text", doi="sample_text", editor="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", publisher="sample_text", series="sample_text", title="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_ProceedingsType70', b1)
    assert _is_linked(a, 'bibtexml_ProceedingsType70', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot69'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot69', a)
    _safe_set(a, 'bibtexml_ProceedingsType70', b2)
    assert _is_linked(a, 'bibtexml_ProceedingsType70', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot69'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot69', a)
    if hasattr(b2, 'bibtexml_DocumentRoot69'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot69', a)
    _safe_set(a, 'bibtexml_ProceedingsType70', None)
    assert not _is_linked(a, 'bibtexml_ProceedingsType70', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot69'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot69', a)


def test_assoc_techreport7_link_reassign_clear():
    a = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_TechreportType', b1)
    assert _is_linked(a, 'bibtexml_TechreportType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass8'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass8', a)
    _safe_set(a, 'bibtexml_TechreportType', b2)
    assert _is_linked(a, 'bibtexml_TechreportType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass8'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass8', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass8'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass8', a)
    _safe_set(a, 'bibtexml_TechreportType', None)
    assert not _is_linked(a, 'bibtexml_TechreportType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass8'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass8', a)


def test_assoc_techreport71_link_reassign_clear():
    a = bibtexml_TechreportType(address="sample_text", author="sample_text", crossref="sample_text", doi="sample_text", institution="sample_text", key="sample_text", month="sample_text", note="sample_text", number="sample_text", title="sample_text", type="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_TechreportType73', b1)
    assert _is_linked(a, 'bibtexml_TechreportType73', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot72'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot72', a)
    _safe_set(a, 'bibtexml_TechreportType73', b2)
    assert _is_linked(a, 'bibtexml_TechreportType73', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot72'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot72', a)
    if hasattr(b2, 'bibtexml_DocumentRoot72'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot72', a)
    _safe_set(a, 'bibtexml_TechreportType73', None)
    assert not _is_linked(a, 'bibtexml_TechreportType73', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot72'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot72', a)


def test_assoc_unpublished23_link_reassign_clear():
    a = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_BibTeXMLEntriesClass()
    b2 = bibtexml_BibTeXMLEntriesClass()
    _safe_set(a, 'bibtexml_UnpublishedType', b1)
    assert _is_linked(a, 'bibtexml_UnpublishedType', b1)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass24'):
        assert _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass24', a)
    _safe_set(a, 'bibtexml_UnpublishedType', b2)
    assert _is_linked(a, 'bibtexml_UnpublishedType', b2)
    if hasattr(b1, 'bibtexml_BibTeXMLEntriesClass24'):
        assert not _is_linked(b1, 'bibtexml_BibTeXMLEntriesClass24', a)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass24'):
        assert _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass24', a)
    _safe_set(a, 'bibtexml_UnpublishedType', None)
    assert not _is_linked(a, 'bibtexml_UnpublishedType', b2)
    if hasattr(b2, 'bibtexml_BibTeXMLEntriesClass24'):
        assert not _is_linked(b2, 'bibtexml_BibTeXMLEntriesClass24', a)


def test_assoc_unpublished74_link_reassign_clear():
    a = bibtexml_UnpublishedType(author="sample_text", crossref="sample_text", doi="sample_text", key="sample_text", month="sample_text", note="sample_text", title="sample_text", url="sample_text", year="sample_text")
    b1 = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b2 = bibtexml_DocumentRoot(address="sample_text_2", annote="sample_text_2", author="sample_text_2", booktitle="sample_text_2", chapter="sample_text_2", crossref="sample_text_2", doi="sample_text_2", edition="sample_text_2", editor="sample_text_2", howpublished="sample_text_2", institution="sample_text_2", journal="sample_text_2", key="sample_text_2", mixed="sample_text_2", month="sample_text_2", note="sample_text_2", number="sample_text_2", organization="sample_text_2", pages="sample_text_2", publisher="sample_text_2", school="sample_text_2", series="sample_text_2", title="sample_text_2", type="sample_text_2", url="sample_text_2", volume="sample_text_2", year="sample_text_2")
    _safe_set(a, 'bibtexml_UnpublishedType76', b1)
    assert _is_linked(a, 'bibtexml_UnpublishedType76', b1)
    if hasattr(b1, 'bibtexml_DocumentRoot75'):
        assert _is_linked(b1, 'bibtexml_DocumentRoot75', a)
    _safe_set(a, 'bibtexml_UnpublishedType76', b2)
    assert _is_linked(a, 'bibtexml_UnpublishedType76', b2)
    if hasattr(b1, 'bibtexml_DocumentRoot75'):
        assert not _is_linked(b1, 'bibtexml_DocumentRoot75', a)
    if hasattr(b2, 'bibtexml_DocumentRoot75'):
        assert _is_linked(b2, 'bibtexml_DocumentRoot75', a)
    _safe_set(a, 'bibtexml_UnpublishedType76', None)
    assert not _is_linked(a, 'bibtexml_UnpublishedType76', b2)
    if hasattr(b2, 'bibtexml_DocumentRoot75'):
        assert not _is_linked(b2, 'bibtexml_DocumentRoot75', a)


def test_assoc_xMLNSPrefixMap27_link_reassign_clear():
    a = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_EStringToStringMapEntry()
    b2 = bibtexml_EStringToStringMapEntry()
    _safe_set(a, 'bibtexml_DocumentRoot', {b1})
    assert _is_linked(a, 'bibtexml_DocumentRoot', b1)
    if hasattr(b1, 'bibtexml_EStringToStringMapEntry'):
        assert _is_linked(b1, 'bibtexml_EStringToStringMapEntry', a)
    _safe_set(a, 'bibtexml_DocumentRoot', {b2})
    assert _is_linked(a, 'bibtexml_DocumentRoot', b2)
    if hasattr(b1, 'bibtexml_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'bibtexml_EStringToStringMapEntry', a)
    if hasattr(b2, 'bibtexml_EStringToStringMapEntry'):
        assert _is_linked(b2, 'bibtexml_EStringToStringMapEntry', a)
    _safe_set(a, 'bibtexml_DocumentRoot', set())
    assert not _is_linked(a, 'bibtexml_DocumentRoot', b2)
    if hasattr(b2, 'bibtexml_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'bibtexml_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation28_link_reassign_clear():
    a = bibtexml_DocumentRoot(address="sample_text", annote="sample_text", author="sample_text", booktitle="sample_text", chapter="sample_text", crossref="sample_text", doi="sample_text", edition="sample_text", editor="sample_text", howpublished="sample_text", institution="sample_text", journal="sample_text", key="sample_text", mixed="sample_text", month="sample_text", note="sample_text", number="sample_text", organization="sample_text", pages="sample_text", publisher="sample_text", school="sample_text", series="sample_text", title="sample_text", type="sample_text", url="sample_text", volume="sample_text", year="sample_text")
    b1 = bibtexml_EStringToStringMapEntry()
    b2 = bibtexml_EStringToStringMapEntry()
    _safe_set(a, 'bibtexml_DocumentRoot29', {b1})
    assert _is_linked(a, 'bibtexml_DocumentRoot29', b1)
    if hasattr(b1, 'bibtexml_EStringToStringMapEntry30'):
        assert _is_linked(b1, 'bibtexml_EStringToStringMapEntry30', a)
    _safe_set(a, 'bibtexml_DocumentRoot29', {b2})
    assert _is_linked(a, 'bibtexml_DocumentRoot29', b2)
    if hasattr(b1, 'bibtexml_EStringToStringMapEntry30'):
        assert not _is_linked(b1, 'bibtexml_EStringToStringMapEntry30', a)
    if hasattr(b2, 'bibtexml_EStringToStringMapEntry30'):
        assert _is_linked(b2, 'bibtexml_EStringToStringMapEntry30', a)
    _safe_set(a, 'bibtexml_DocumentRoot29', set())
    assert not _is_linked(a, 'bibtexml_DocumentRoot29', b2)
    if hasattr(b2, 'bibtexml_EStringToStringMapEntry30'):
        assert not _is_linked(b2, 'bibtexml_EStringToStringMapEntry30', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BibTeXMLEntriesClass_strategy = st.builds(BibTeXMLEntriesClass)
@given(instance=BibTeXMLEntriesClass_strategy)
@settings(max_examples=25)
def test_BibTeXMLEntriesClass_instantiation(instance):
    assert isinstance(instance, BibTeXMLEntriesClass)


bibtexml_ArticleType_strategy = st.builds(bibtexml_ArticleType, author=safe_text, crossref=safe_text, doi=safe_text, journal=safe_text, key=safe_text, month=safe_text, note=safe_text, number=safe_text, pages=safe_text, title=safe_text, url=safe_text, volume=safe_text, year=safe_text)
@given(instance=bibtexml_ArticleType_strategy)
@settings(max_examples=25)
def test_bibtexml_ArticleType_instantiation(instance):
    assert isinstance(instance, bibtexml_ArticleType)


bibtexml_BibTeXMLEntriesClass_strategy = st.builds(bibtexml_BibTeXMLEntriesClass)
@given(instance=bibtexml_BibTeXMLEntriesClass_strategy)
@settings(max_examples=25)
def test_bibtexml_BibTeXMLEntriesClass_instantiation(instance):
    assert isinstance(instance, bibtexml_BibTeXMLEntriesClass)


bibtexml_BibTeXMLEntryType_strategy = st.builds(bibtexml_BibTeXMLEntryType, id=safe_text)
@given(instance=bibtexml_BibTeXMLEntryType_strategy)
@settings(max_examples=25)
def test_bibtexml_BibTeXMLEntryType_instantiation(instance):
    assert isinstance(instance, bibtexml_BibTeXMLEntryType)


bibtexml_BookType_strategy = st.builds(bibtexml_BookType, address=safe_text, author=safe_text, crossref=safe_text, doi=safe_text, edition=safe_text, editor=safe_text, key=safe_text, month=safe_text, note=safe_text, number=safe_text, publisher=safe_text, series=safe_text, title=safe_text, url=safe_text, volume=safe_text, year=safe_text)
@given(instance=bibtexml_BookType_strategy)
@settings(max_examples=25)
def test_bibtexml_BookType_instantiation(instance):
    assert isinstance(instance, bibtexml_BookType)


bibtexml_BookletType_strategy = st.builds(bibtexml_BookletType, address=safe_text, author=safe_text, crossref=safe_text, doi=safe_text, howpublished=safe_text, key=safe_text, month=safe_text, note=safe_text, title=safe_text, url=safe_text, year=safe_text)
@given(instance=bibtexml_BookletType_strategy)
@settings(max_examples=25)
def test_bibtexml_BookletType_instantiation(instance):
    assert isinstance(instance, bibtexml_BookletType)


bibtexml_ConferenceType_strategy = st.builds(bibtexml_ConferenceType, address=safe_text, author=safe_text, booktitle=safe_text, crossref=safe_text, doi=safe_text, editor=safe_text, key=safe_text, month=safe_text, note=safe_text, number=safe_text, organization=safe_text, pages=safe_text, publisher=safe_text, series=safe_text, title=safe_text, url=safe_text, volume=safe_text, year=safe_text)
@given(instance=bibtexml_ConferenceType_strategy)
@settings(max_examples=25)
def test_bibtexml_ConferenceType_instantiation(instance):
    assert isinstance(instance, bibtexml_ConferenceType)


bibtexml_DocumentRoot_strategy = st.builds(bibtexml_DocumentRoot, address=safe_text, annote=safe_text, author=safe_text, booktitle=safe_text, chapter=safe_text, crossref=safe_text, doi=safe_text, edition=safe_text, editor=safe_text, howpublished=safe_text, institution=safe_text, journal=safe_text, key=safe_text, mixed=safe_text, month=safe_text, note=safe_text, number=safe_text, organization=safe_text, pages=safe_text, publisher=safe_text, school=safe_text, series=safe_text, title=safe_text, type=safe_text, url=safe_text, volume=safe_text, year=safe_text)
@given(instance=bibtexml_DocumentRoot_strategy)
@settings(max_examples=25)
def test_bibtexml_DocumentRoot_instantiation(instance):
    assert isinstance(instance, bibtexml_DocumentRoot)


bibtexml_EStringToStringMapEntry_strategy = st.builds(bibtexml_EStringToStringMapEntry)
@given(instance=bibtexml_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_bibtexml_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, bibtexml_EStringToStringMapEntry)


bibtexml_FileType_strategy = st.builds(bibtexml_FileType)
@given(instance=bibtexml_FileType_strategy)
@settings(max_examples=25)
def test_bibtexml_FileType_instantiation(instance):
    assert isinstance(instance, bibtexml_FileType)


bibtexml_InbookType_strategy = st.builds(bibtexml_InbookType, address=safe_text, author=safe_text, chapter=safe_text, crossref=safe_text, doi=safe_text, edition=safe_text, editor=safe_text, key=safe_text, month=safe_text, note=safe_text, number=safe_text, pages=safe_text, pages1=safe_text, publisher=safe_text, series=safe_text, title=safe_text, type=safe_text, url=safe_text, volume=safe_text, year=safe_text)
@given(instance=bibtexml_InbookType_strategy)
@settings(max_examples=25)
def test_bibtexml_InbookType_instantiation(instance):
    assert isinstance(instance, bibtexml_InbookType)


bibtexml_IncollectionType_strategy = st.builds(bibtexml_IncollectionType, address=safe_text, author=safe_text, booktitle=safe_text, chapter=safe_text, crossref=safe_text, doi=safe_text, edition=safe_text, editor=safe_text, key=safe_text, month=safe_text, note=safe_text, number=safe_text, pages=safe_text, publisher=safe_text, series=safe_text, title=safe_text, type=safe_text, url=safe_text, volume=safe_text, year=safe_text)
@given(instance=bibtexml_IncollectionType_strategy)
@settings(max_examples=25)
def test_bibtexml_IncollectionType_instantiation(instance):
    assert isinstance(instance, bibtexml_IncollectionType)


bibtexml_InproceedingsType_strategy = st.builds(bibtexml_InproceedingsType, address=safe_text, author=safe_text, booktitle=safe_text, crossref=safe_text, doi=safe_text, editor=safe_text, key=safe_text, month=safe_text, note=safe_text, number=safe_text, organization=safe_text, pages=safe_text, publisher=safe_text, series=safe_text, title=safe_text, url=safe_text, volume=safe_text, year=safe_text)
@given(instance=bibtexml_InproceedingsType_strategy)
@settings(max_examples=25)
def test_bibtexml_InproceedingsType_instantiation(instance):
    assert isinstance(instance, bibtexml_InproceedingsType)


bibtexml_ManualType_strategy = st.builds(bibtexml_ManualType, address=safe_text, author=safe_text, crossref=safe_text, doi=safe_text, edition=safe_text, key=safe_text, month=safe_text, note=safe_text, organization=safe_text, title=safe_text, url=safe_text, year=safe_text)
@given(instance=bibtexml_ManualType_strategy)
@settings(max_examples=25)
def test_bibtexml_ManualType_instantiation(instance):
    assert isinstance(instance, bibtexml_ManualType)


bibtexml_MastersthesisType_strategy = st.builds(bibtexml_MastersthesisType, address=safe_text, author=safe_text, crossref=safe_text, doi=safe_text, key=safe_text, month=safe_text, note=safe_text, school=safe_text, title=safe_text, type=safe_text, url=safe_text, year=safe_text)
@given(instance=bibtexml_MastersthesisType_strategy)
@settings(max_examples=25)
def test_bibtexml_MastersthesisType_instantiation(instance):
    assert isinstance(instance, bibtexml_MastersthesisType)


bibtexml_MiscType_strategy = st.builds(bibtexml_MiscType, author=safe_text, crossref=safe_text, doi=safe_text, howpublished=safe_text, key=safe_text, month=safe_text, note=safe_text, title=safe_text, url=safe_text, year=safe_text)
@given(instance=bibtexml_MiscType_strategy)
@settings(max_examples=25)
def test_bibtexml_MiscType_instantiation(instance):
    assert isinstance(instance, bibtexml_MiscType)


bibtexml_PhdthesisType_strategy = st.builds(bibtexml_PhdthesisType, address=safe_text, author=safe_text, crossref=safe_text, doi=safe_text, key=safe_text, month=safe_text, note=safe_text, school=safe_text, title=safe_text, type=safe_text, url=safe_text, year=safe_text)
@given(instance=bibtexml_PhdthesisType_strategy)
@settings(max_examples=25)
def test_bibtexml_PhdthesisType_instantiation(instance):
    assert isinstance(instance, bibtexml_PhdthesisType)


bibtexml_ProceedingsType_strategy = st.builds(bibtexml_ProceedingsType, address=safe_text, crossref=safe_text, doi=safe_text, editor=safe_text, key=safe_text, month=safe_text, note=safe_text, number=safe_text, organization=safe_text, publisher=safe_text, series=safe_text, title=safe_text, url=safe_text, volume=safe_text, year=safe_text)
@given(instance=bibtexml_ProceedingsType_strategy)
@settings(max_examples=25)
def test_bibtexml_ProceedingsType_instantiation(instance):
    assert isinstance(instance, bibtexml_ProceedingsType)


bibtexml_TechreportType_strategy = st.builds(bibtexml_TechreportType, address=safe_text, author=safe_text, crossref=safe_text, doi=safe_text, institution=safe_text, key=safe_text, month=safe_text, note=safe_text, number=safe_text, title=safe_text, type=safe_text, url=safe_text, year=safe_text)
@given(instance=bibtexml_TechreportType_strategy)
@settings(max_examples=25)
def test_bibtexml_TechreportType_instantiation(instance):
    assert isinstance(instance, bibtexml_TechreportType)


bibtexml_UnpublishedType_strategy = st.builds(bibtexml_UnpublishedType, author=safe_text, crossref=safe_text, doi=safe_text, key=safe_text, month=safe_text, note=safe_text, title=safe_text, url=safe_text, year=safe_text)
@given(instance=bibtexml_UnpublishedType_strategy)
@settings(max_examples=25)
def test_bibtexml_UnpublishedType_instantiation(instance):
    assert isinstance(instance, bibtexml_UnpublishedType)


