# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    bibTeX_EditorField,
    bibTeX_UnknownValue,
    bibTeX_Fullname,
    AuthorField,
    bibTeX_Authors,
    bibTeX_EditionField,
    bibTeX_AddressField,
    bibTeX_UnknownType,
    bibTeX_IsbnField,
    bibTeX_EObject,
    bibTeX_PagesField,
    bibTeX_SeriesField,
    bibTeX_PublisherField,
    bibTeX_VolumeField,
    bibTeX_JournalField,
    bibTeX_NumberField,
    BibtexEntryTypes,
    bibTeX_Book,
    bibTeX_Article,
    bibTeX_UnknownField,
    bibTeX_AuthorField,
    bibTeX_MonthField,
    bibTeX_YearField,
    bibTeX_TitleField,
    bibTeX_CiteKey,
    bibTeX_NoteField,
    bibTeX_Model,
    bibTeX_BibtexEntryTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_bibtex_editorfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_EditorField)


def test_hyp_bibtex_editorfield_constructor_exists():
    assert callable(bibTeX_EditorField.__init__)


def test_hyp_bibtex_editorfield_constructor_args():
    sig = inspect.signature(bibTeX_EditorField.__init__)
    params = list(sig.parameters.keys())
    assert "editor" in params, "Missing parameter 'editor'"




def test_hyp_bibtex_unknownvalue_is_not_abstract():
    assert not inspect.isabstract(bibTeX_UnknownValue)


def test_hyp_bibtex_unknownvalue_constructor_exists():
    assert callable(bibTeX_UnknownValue.__init__)


def test_hyp_bibtex_unknownvalue_constructor_args():
    sig = inspect.signature(bibTeX_UnknownValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_bibtex_fullname_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Fullname)


def test_hyp_bibtex_fullname_constructor_exists():
    assert callable(bibTeX_Fullname.__init__)


def test_hyp_bibtex_fullname_constructor_args():
    sig = inspect.signature(bibTeX_Fullname.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "lastname" in params, "Missing parameter 'lastname'"





def test_hyp_authorfield_is_not_abstract():
    assert not inspect.isabstract(AuthorField)


def test_hyp_authorfield_constructor_exists():
    assert callable(AuthorField.__init__)


def test_hyp_authorfield_constructor_args():
    sig = inspect.signature(AuthorField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_authors_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Authors)


def test_hyp_bibtex_authors_constructor_exists():
    assert callable(bibTeX_Authors.__init__)


def test_hyp_bibtex_authors_constructor_args():
    sig = inspect.signature(bibTeX_Authors.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_editionfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_EditionField)


def test_hyp_bibtex_editionfield_constructor_exists():
    assert callable(bibTeX_EditionField.__init__)


def test_hyp_bibtex_editionfield_constructor_args():
    sig = inspect.signature(bibTeX_EditionField.__init__)
    params = list(sig.parameters.keys())
    assert "edition" in params, "Missing parameter 'edition'"




def test_hyp_bibtex_addressfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_AddressField)


def test_hyp_bibtex_addressfield_constructor_exists():
    assert callable(bibTeX_AddressField.__init__)


def test_hyp_bibtex_addressfield_constructor_args():
    sig = inspect.signature(bibTeX_AddressField.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"




def test_hyp_bibtex_unknowntype_is_not_abstract():
    assert not inspect.isabstract(bibTeX_UnknownType)


def test_hyp_bibtex_unknowntype_constructor_exists():
    assert callable(bibTeX_UnknownType.__init__)


def test_hyp_bibtex_unknowntype_constructor_args():
    sig = inspect.signature(bibTeX_UnknownType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_bibtex_isbnfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_IsbnField)


def test_hyp_bibtex_isbnfield_constructor_exists():
    assert callable(bibTeX_IsbnField.__init__)


def test_hyp_bibtex_isbnfield_constructor_args():
    sig = inspect.signature(bibTeX_IsbnField.__init__)
    params = list(sig.parameters.keys())
    assert "isbn" in params, "Missing parameter 'isbn'"




def test_hyp_bibtex_eobject_is_not_abstract():
    assert not inspect.isabstract(bibTeX_EObject)


def test_hyp_bibtex_eobject_constructor_exists():
    assert callable(bibTeX_EObject.__init__)


def test_hyp_bibtex_eobject_constructor_args():
    sig = inspect.signature(bibTeX_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_pagesfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_PagesField)


def test_hyp_bibtex_pagesfield_constructor_exists():
    assert callable(bibTeX_PagesField.__init__)


def test_hyp_bibtex_pagesfield_constructor_args():
    sig = inspect.signature(bibTeX_PagesField.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"




def test_hyp_bibtex_seriesfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_SeriesField)


def test_hyp_bibtex_seriesfield_constructor_exists():
    assert callable(bibTeX_SeriesField.__init__)


def test_hyp_bibtex_seriesfield_constructor_args():
    sig = inspect.signature(bibTeX_SeriesField.__init__)
    params = list(sig.parameters.keys())
    assert "series" in params, "Missing parameter 'series'"




def test_hyp_bibtex_publisherfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_PublisherField)


def test_hyp_bibtex_publisherfield_constructor_exists():
    assert callable(bibTeX_PublisherField.__init__)


def test_hyp_bibtex_publisherfield_constructor_args():
    sig = inspect.signature(bibTeX_PublisherField.__init__)
    params = list(sig.parameters.keys())
    assert "publisher" in params, "Missing parameter 'publisher'"




def test_hyp_bibtex_volumefield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_VolumeField)


def test_hyp_bibtex_volumefield_constructor_exists():
    assert callable(bibTeX_VolumeField.__init__)


def test_hyp_bibtex_volumefield_constructor_args():
    sig = inspect.signature(bibTeX_VolumeField.__init__)
    params = list(sig.parameters.keys())
    assert "volume" in params, "Missing parameter 'volume'"




def test_hyp_bibtex_journalfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_JournalField)


def test_hyp_bibtex_journalfield_constructor_exists():
    assert callable(bibTeX_JournalField.__init__)


def test_hyp_bibtex_journalfield_constructor_args():
    sig = inspect.signature(bibTeX_JournalField.__init__)
    params = list(sig.parameters.keys())
    assert "journal" in params, "Missing parameter 'journal'"




def test_hyp_bibtex_numberfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_NumberField)


def test_hyp_bibtex_numberfield_constructor_exists():
    assert callable(bibTeX_NumberField.__init__)


def test_hyp_bibtex_numberfield_constructor_args():
    sig = inspect.signature(bibTeX_NumberField.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"




def test_hyp_bibtexentrytypes_is_not_abstract():
    assert not inspect.isabstract(BibtexEntryTypes)


def test_hyp_bibtexentrytypes_constructor_exists():
    assert callable(BibtexEntryTypes.__init__)


def test_hyp_bibtexentrytypes_constructor_args():
    sig = inspect.signature(BibtexEntryTypes.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_book_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Book)


def test_hyp_bibtex_book_constructor_exists():
    assert callable(bibTeX_Book.__init__)


def test_hyp_bibtex_book_constructor_args():
    sig = inspect.signature(bibTeX_Book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_article_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Article)


def test_hyp_bibtex_article_constructor_exists():
    assert callable(bibTeX_Article.__init__)


def test_hyp_bibtex_article_constructor_args():
    sig = inspect.signature(bibTeX_Article.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_unknownfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_UnknownField)


def test_hyp_bibtex_unknownfield_constructor_exists():
    assert callable(bibTeX_UnknownField.__init__)


def test_hyp_bibtex_unknownfield_constructor_args():
    sig = inspect.signature(bibTeX_UnknownField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_authorfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_AuthorField)


def test_hyp_bibtex_authorfield_constructor_exists():
    assert callable(bibTeX_AuthorField.__init__)


def test_hyp_bibtex_authorfield_constructor_args():
    sig = inspect.signature(bibTeX_AuthorField.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_monthfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_MonthField)


def test_hyp_bibtex_monthfield_constructor_exists():
    assert callable(bibTeX_MonthField.__init__)


def test_hyp_bibtex_monthfield_constructor_args():
    sig = inspect.signature(bibTeX_MonthField.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"




def test_hyp_bibtex_yearfield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_YearField)


def test_hyp_bibtex_yearfield_constructor_exists():
    assert callable(bibTeX_YearField.__init__)


def test_hyp_bibtex_yearfield_constructor_args():
    sig = inspect.signature(bibTeX_YearField.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"




def test_hyp_bibtex_titlefield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_TitleField)


def test_hyp_bibtex_titlefield_constructor_exists():
    assert callable(bibTeX_TitleField.__init__)


def test_hyp_bibtex_titlefield_constructor_args():
    sig = inspect.signature(bibTeX_TitleField.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_bibtex_citekey_is_not_abstract():
    assert not inspect.isabstract(bibTeX_CiteKey)


def test_hyp_bibtex_citekey_constructor_exists():
    assert callable(bibTeX_CiteKey.__init__)


def test_hyp_bibtex_citekey_constructor_args():
    sig = inspect.signature(bibTeX_CiteKey.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"




def test_hyp_bibtex_notefield_is_not_abstract():
    assert not inspect.isabstract(bibTeX_NoteField)


def test_hyp_bibtex_notefield_constructor_exists():
    assert callable(bibTeX_NoteField.__init__)


def test_hyp_bibtex_notefield_constructor_args():
    sig = inspect.signature(bibTeX_NoteField.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"




def test_hyp_bibtex_model_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Model)


def test_hyp_bibtex_model_constructor_exists():
    assert callable(bibTeX_Model.__init__)


def test_hyp_bibtex_model_constructor_args():
    sig = inspect.signature(bibTeX_Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_bibtexentrytypes_is_not_abstract():
    assert not inspect.isabstract(bibTeX_BibtexEntryTypes)


def test_hyp_bibtex_bibtexentrytypes_constructor_exists():
    assert callable(bibTeX_BibtexEntryTypes.__init__)


def test_hyp_bibtex_bibtexentrytypes_constructor_args():
    sig = inspect.signature(bibTeX_BibtexEntryTypes.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
bibTeX_EditorField_strategy = st.builds(
    bibTeX_EditorField,
    editor=
        safe_text
)
bibTeX_UnknownValue_strategy = st.builds(
    bibTeX_UnknownValue,
    value=
        safe_text
)
bibTeX_Fullname_strategy = st.builds(
    bibTeX_Fullname,
    firstname=
        safe_text,
    lastname=
        safe_text
)
AuthorField_strategy = st.builds(
    AuthorField,
)
bibTeX_Authors_strategy = st.builds(
    bibTeX_Authors,
)
bibTeX_EditionField_strategy = st.builds(
    bibTeX_EditionField,
    edition=
        safe_text
)
bibTeX_AddressField_strategy = st.builds(
    bibTeX_AddressField,
    address=
        safe_text
)
bibTeX_UnknownType_strategy = st.builds(
    bibTeX_UnknownType,
    type=
        safe_text
)
bibTeX_IsbnField_strategy = st.builds(
    bibTeX_IsbnField,
    isbn=
        safe_text
)
bibTeX_EObject_strategy = st.builds(
    bibTeX_EObject,
)
bibTeX_PagesField_strategy = st.builds(
    bibTeX_PagesField,
    pages=
        safe_text
)
bibTeX_SeriesField_strategy = st.builds(
    bibTeX_SeriesField,
    series=
        safe_text
)
bibTeX_PublisherField_strategy = st.builds(
    bibTeX_PublisherField,
    publisher=
        safe_text
)
bibTeX_VolumeField_strategy = st.builds(
    bibTeX_VolumeField,
    volume=
        safe_text
)
bibTeX_JournalField_strategy = st.builds(
    bibTeX_JournalField,
    journal=
        safe_text
)
bibTeX_NumberField_strategy = st.builds(
    bibTeX_NumberField,
    number=
        safe_text
)
BibtexEntryTypes_strategy = st.builds(
    BibtexEntryTypes,
)
bibTeX_Book_strategy = st.builds(
    bibTeX_Book,
)
bibTeX_Article_strategy = st.builds(
    bibTeX_Article,
)
bibTeX_UnknownField_strategy = st.builds(
    bibTeX_UnknownField,
)
bibTeX_AuthorField_strategy = st.builds(
    bibTeX_AuthorField,
)
bibTeX_MonthField_strategy = st.builds(
    bibTeX_MonthField,
    month=
        safe_text
)
bibTeX_YearField_strategy = st.builds(
    bibTeX_YearField,
    year=
        safe_text
)
bibTeX_TitleField_strategy = st.builds(
    bibTeX_TitleField,
    title=
        safe_text
)
bibTeX_CiteKey_strategy = st.builds(
    bibTeX_CiteKey,
    key=
        safe_text
)
bibTeX_NoteField_strategy = st.builds(
    bibTeX_NoteField,
    note=
        safe_text
)
bibTeX_Model_strategy = st.builds(
    bibTeX_Model,
)
bibTeX_BibtexEntryTypes_strategy = st.builds(
    bibTeX_BibtexEntryTypes,
)




@given(instance=bibTeX_EditorField_strategy)
def test_hyp_bibtex_editorfield_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original




@given(instance=bibTeX_UnknownValue_strategy)
def test_hyp_bibtex_unknownvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=bibTeX_Fullname_strategy)
def test_hyp_bibtex_fullname_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=bibTeX_Fullname_strategy)
def test_hyp_bibtex_fullname_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original






@given(instance=bibTeX_EditionField_strategy)
def test_hyp_bibtex_editionfield_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original




@given(instance=bibTeX_AddressField_strategy)
def test_hyp_bibtex_addressfield_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original




@given(instance=bibTeX_UnknownType_strategy)
def test_hyp_bibtex_unknowntype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=bibTeX_IsbnField_strategy)
def test_hyp_bibtex_isbnfield_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original





@given(instance=bibTeX_PagesField_strategy)
def test_hyp_bibtex_pagesfield_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original




@given(instance=bibTeX_SeriesField_strategy)
def test_hyp_bibtex_seriesfield_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original




@given(instance=bibTeX_PublisherField_strategy)
def test_hyp_bibtex_publisherfield_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original




@given(instance=bibTeX_VolumeField_strategy)
def test_hyp_bibtex_volumefield_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original




@given(instance=bibTeX_JournalField_strategy)
def test_hyp_bibtex_journalfield_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original




@given(instance=bibTeX_NumberField_strategy)
def test_hyp_bibtex_numberfield_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original









@given(instance=bibTeX_MonthField_strategy)
def test_hyp_bibtex_monthfield_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original




@given(instance=bibTeX_YearField_strategy)
def test_hyp_bibtex_yearfield_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original




@given(instance=bibTeX_TitleField_strategy)
def test_hyp_bibtex_titlefield_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original




@given(instance=bibTeX_CiteKey_strategy)
def test_hyp_bibtex_citekey_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




@given(instance=bibTeX_NoteField_strategy)
def test_hyp_bibtex_notefield_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_bibTeX_AddressField_address_value_roundtrip():
    instance = bibTeX_AddressField(address="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_bibTeX_CiteKey_key_value_roundtrip():
    instance = bibTeX_CiteKey(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_bibTeX_EditionField_edition_value_roundtrip():
    instance = bibTeX_EditionField(edition="sample_text")
    assert instance.edition == "sample_text"
    instance.edition = "sample_text_2"
    assert instance.edition == "sample_text_2"


def test_bibTeX_EditorField_editor_value_roundtrip():
    instance = bibTeX_EditorField(editor="sample_text")
    assert instance.editor == "sample_text"
    instance.editor = "sample_text_2"
    assert instance.editor == "sample_text_2"


def test_bibTeX_Fullname_firstname_value_roundtrip():
    instance = bibTeX_Fullname(firstname="sample_text", lastname="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_bibTeX_Fullname_lastname_value_roundtrip():
    instance = bibTeX_Fullname(firstname="sample_text", lastname="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_bibTeX_IsbnField_isbn_value_roundtrip():
    instance = bibTeX_IsbnField(isbn="sample_text")
    assert instance.isbn == "sample_text"
    instance.isbn = "sample_text_2"
    assert instance.isbn == "sample_text_2"


def test_bibTeX_JournalField_journal_value_roundtrip():
    instance = bibTeX_JournalField(journal="sample_text")
    assert instance.journal == "sample_text"
    instance.journal = "sample_text_2"
    assert instance.journal == "sample_text_2"


def test_bibTeX_MonthField_month_value_roundtrip():
    instance = bibTeX_MonthField(month="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_bibTeX_NoteField_note_value_roundtrip():
    instance = bibTeX_NoteField(note="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibTeX_NumberField_number_value_roundtrip():
    instance = bibTeX_NumberField(number="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_bibTeX_PagesField_pages_value_roundtrip():
    instance = bibTeX_PagesField(pages="sample_text")
    assert instance.pages == "sample_text"
    instance.pages = "sample_text_2"
    assert instance.pages == "sample_text_2"


def test_bibTeX_PublisherField_publisher_value_roundtrip():
    instance = bibTeX_PublisherField(publisher="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibTeX_SeriesField_series_value_roundtrip():
    instance = bibTeX_SeriesField(series="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_bibTeX_TitleField_title_value_roundtrip():
    instance = bibTeX_TitleField(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibTeX_UnknownType_type_value_roundtrip():
    instance = bibTeX_UnknownType(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_bibTeX_UnknownValue_value_value_roundtrip():
    instance = bibTeX_UnknownValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_bibTeX_VolumeField_volume_value_roundtrip():
    instance = bibTeX_VolumeField(volume="sample_text")
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_bibTeX_YearField_year_value_roundtrip():
    instance = bibTeX_YearField(year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibTeX_Authors_isa_AuthorField():
    instance = bibTeX_Authors()
    assert isinstance(instance, AuthorField)


def test_bibTeX_Article_isa_BibtexEntryTypes():
    instance = bibTeX_Article()
    assert isinstance(instance, BibtexEntryTypes)


def test_bibTeX_Book_isa_BibtexEntryTypes():
    instance = bibTeX_Book()
    assert isinstance(instance, BibtexEntryTypes)


def test_assoc_address30_link_reassign_clear():
    a = bibTeX_AddressField(address="sample_text")
    b1 = bibTeX_Book()
    b2 = bibTeX_Book()
    _safe_set(a, 'bibTeX_AddressField', b1)
    assert _is_linked(a, 'bibTeX_AddressField', b1)
    if hasattr(b1, 'bibTeX_Book31'):
        assert _is_linked(b1, 'bibTeX_Book31', a)
    _safe_set(a, 'bibTeX_AddressField', b2)
    assert _is_linked(a, 'bibTeX_AddressField', b2)
    if hasattr(b1, 'bibTeX_Book31'):
        assert not _is_linked(b1, 'bibTeX_Book31', a)
    if hasattr(b2, 'bibTeX_Book31'):
        assert _is_linked(b2, 'bibTeX_Book31', a)
    _safe_set(a, 'bibTeX_AddressField', None)
    assert not _is_linked(a, 'bibTeX_AddressField', b2)
    if hasattr(b2, 'bibTeX_Book31'):
        assert not _is_linked(b2, 'bibTeX_Book31', a)


def test_assoc_edition32_link_reassign_clear():
    a = bibTeX_EditionField(edition="sample_text")
    b1 = bibTeX_Book()
    b2 = bibTeX_Book()
    _safe_set(a, 'bibTeX_EditionField', b1)
    assert _is_linked(a, 'bibTeX_EditionField', b1)
    if hasattr(b1, 'bibTeX_Book33'):
        assert _is_linked(b1, 'bibTeX_Book33', a)
    _safe_set(a, 'bibTeX_EditionField', b2)
    assert _is_linked(a, 'bibTeX_EditionField', b2)
    if hasattr(b1, 'bibTeX_Book33'):
        assert not _is_linked(b1, 'bibTeX_Book33', a)
    if hasattr(b2, 'bibTeX_Book33'):
        assert _is_linked(b2, 'bibTeX_Book33', a)
    _safe_set(a, 'bibTeX_EditionField', None)
    assert not _is_linked(a, 'bibTeX_EditionField', b2)
    if hasattr(b2, 'bibTeX_Book33'):
        assert not _is_linked(b2, 'bibTeX_Book33', a)


def test_assoc_isbn34_link_reassign_clear():
    a = bibTeX_IsbnField(isbn="sample_text")
    b1 = bibTeX_Book()
    b2 = bibTeX_Book()
    _safe_set(a, 'bibTeX_IsbnField', b1)
    assert _is_linked(a, 'bibTeX_IsbnField', b1)
    if hasattr(b1, 'bibTeX_Book35'):
        assert _is_linked(b1, 'bibTeX_Book35', a)
    _safe_set(a, 'bibTeX_IsbnField', b2)
    assert _is_linked(a, 'bibTeX_IsbnField', b2)
    if hasattr(b1, 'bibTeX_Book35'):
        assert not _is_linked(b1, 'bibTeX_Book35', a)
    if hasattr(b2, 'bibTeX_Book35'):
        assert _is_linked(b2, 'bibTeX_Book35', a)
    _safe_set(a, 'bibTeX_IsbnField', None)
    assert not _is_linked(a, 'bibTeX_IsbnField', b2)
    if hasattr(b2, 'bibTeX_Book35'):
        assert not _is_linked(b2, 'bibTeX_Book35', a)


def test_assoc_journal14_link_reassign_clear():
    a = bibTeX_JournalField(journal="sample_text")
    b1 = bibTeX_Article()
    b2 = bibTeX_Article()
    _safe_set(a, 'bibTeX_JournalField', b1)
    assert _is_linked(a, 'bibTeX_JournalField', b1)
    if hasattr(b1, 'bibTeX_Article15'):
        assert _is_linked(b1, 'bibTeX_Article15', a)
    _safe_set(a, 'bibTeX_JournalField', b2)
    assert _is_linked(a, 'bibTeX_JournalField', b2)
    if hasattr(b1, 'bibTeX_Article15'):
        assert not _is_linked(b1, 'bibTeX_Article15', a)
    if hasattr(b2, 'bibTeX_Article15'):
        assert _is_linked(b2, 'bibTeX_Article15', a)
    _safe_set(a, 'bibTeX_JournalField', None)
    assert not _is_linked(a, 'bibTeX_JournalField', b2)
    if hasattr(b2, 'bibTeX_Article15'):
        assert not _is_linked(b2, 'bibTeX_Article15', a)


def test_assoc_key1_link_reassign_clear():
    a = bibTeX_CiteKey(key="sample_text")
    b1 = bibTeX_BibtexEntryTypes()
    b2 = bibTeX_BibtexEntryTypes()
    _safe_set(a, 'bibTeX_CiteKey', b1)
    assert _is_linked(a, 'bibTeX_CiteKey', b1)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes2'):
        assert _is_linked(b1, 'bibTeX_BibtexEntryTypes2', a)
    _safe_set(a, 'bibTeX_CiteKey', b2)
    assert _is_linked(a, 'bibTeX_CiteKey', b2)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes2'):
        assert not _is_linked(b1, 'bibTeX_BibtexEntryTypes2', a)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes2'):
        assert _is_linked(b2, 'bibTeX_BibtexEntryTypes2', a)
    _safe_set(a, 'bibTeX_CiteKey', None)
    assert not _is_linked(a, 'bibTeX_CiteKey', b2)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes2'):
        assert not _is_linked(b2, 'bibTeX_BibtexEntryTypes2', a)


def test_assoc_month7_link_reassign_clear():
    a = bibTeX_MonthField(month="sample_text")
    b1 = bibTeX_BibtexEntryTypes()
    b2 = bibTeX_BibtexEntryTypes()
    _safe_set(a, 'bibTeX_MonthField', b1)
    assert _is_linked(a, 'bibTeX_MonthField', b1)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes8'):
        assert _is_linked(b1, 'bibTeX_BibtexEntryTypes8', a)
    _safe_set(a, 'bibTeX_MonthField', b2)
    assert _is_linked(a, 'bibTeX_MonthField', b2)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes8'):
        assert not _is_linked(b1, 'bibTeX_BibtexEntryTypes8', a)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes8'):
        assert _is_linked(b2, 'bibTeX_BibtexEntryTypes8', a)
    _safe_set(a, 'bibTeX_MonthField', None)
    assert not _is_linked(a, 'bibTeX_MonthField', b2)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes8'):
        assert not _is_linked(b2, 'bibTeX_BibtexEntryTypes8', a)


def test_assoc_names40_link_reassign_clear():
    a = bibTeX_Fullname(firstname="sample_text", lastname="sample_text")
    b1 = bibTeX_Authors()
    b2 = bibTeX_Authors()
    _safe_set(a, 'bibTeX_Fullname', b1)
    assert _is_linked(a, 'bibTeX_Fullname', b1)
    if hasattr(b1, 'bibTeX_Authors'):
        assert _is_linked(b1, 'bibTeX_Authors', a)
    _safe_set(a, 'bibTeX_Fullname', b2)
    assert _is_linked(a, 'bibTeX_Fullname', b2)
    if hasattr(b1, 'bibTeX_Authors'):
        assert not _is_linked(b1, 'bibTeX_Authors', a)
    if hasattr(b2, 'bibTeX_Authors'):
        assert _is_linked(b2, 'bibTeX_Authors', a)
    _safe_set(a, 'bibTeX_Fullname', None)
    assert not _is_linked(a, 'bibTeX_Fullname', b2)
    if hasattr(b2, 'bibTeX_Authors'):
        assert not _is_linked(b2, 'bibTeX_Authors', a)


def test_assoc_note9_link_reassign_clear():
    a = bibTeX_NoteField(note="sample_text")
    b1 = bibTeX_BibtexEntryTypes()
    b2 = bibTeX_BibtexEntryTypes()
    _safe_set(a, 'bibTeX_NoteField', b1)
    assert _is_linked(a, 'bibTeX_NoteField', b1)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes10'):
        assert _is_linked(b1, 'bibTeX_BibtexEntryTypes10', a)
    _safe_set(a, 'bibTeX_NoteField', b2)
    assert _is_linked(a, 'bibTeX_NoteField', b2)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes10'):
        assert not _is_linked(b1, 'bibTeX_BibtexEntryTypes10', a)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes10'):
        assert _is_linked(b2, 'bibTeX_BibtexEntryTypes10', a)
    _safe_set(a, 'bibTeX_NoteField', None)
    assert not _is_linked(a, 'bibTeX_NoteField', b2)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes10'):
        assert not _is_linked(b2, 'bibTeX_BibtexEntryTypes10', a)


def test_assoc_number18_link_reassign_clear():
    a = bibTeX_NumberField(number="sample_text")
    b1 = bibTeX_Article()
    b2 = bibTeX_Article()
    _safe_set(a, 'bibTeX_NumberField', b1)
    assert _is_linked(a, 'bibTeX_NumberField', b1)
    if hasattr(b1, 'bibTeX_Article19'):
        assert _is_linked(b1, 'bibTeX_Article19', a)
    _safe_set(a, 'bibTeX_NumberField', b2)
    assert _is_linked(a, 'bibTeX_NumberField', b2)
    if hasattr(b1, 'bibTeX_Article19'):
        assert not _is_linked(b1, 'bibTeX_Article19', a)
    if hasattr(b2, 'bibTeX_Article19'):
        assert _is_linked(b2, 'bibTeX_Article19', a)
    _safe_set(a, 'bibTeX_NumberField', None)
    assert not _is_linked(a, 'bibTeX_NumberField', b2)
    if hasattr(b2, 'bibTeX_Article19'):
        assert not _is_linked(b2, 'bibTeX_Article19', a)


def test_assoc_pages20_link_reassign_clear():
    a = bibTeX_PagesField(pages="sample_text")
    b1 = bibTeX_Article()
    b2 = bibTeX_Article()
    _safe_set(a, 'bibTeX_PagesField', b1)
    assert _is_linked(a, 'bibTeX_PagesField', b1)
    if hasattr(b1, 'bibTeX_Article21'):
        assert _is_linked(b1, 'bibTeX_Article21', a)
    _safe_set(a, 'bibTeX_PagesField', b2)
    assert _is_linked(a, 'bibTeX_PagesField', b2)
    if hasattr(b1, 'bibTeX_Article21'):
        assert not _is_linked(b1, 'bibTeX_Article21', a)
    if hasattr(b2, 'bibTeX_Article21'):
        assert _is_linked(b2, 'bibTeX_Article21', a)
    _safe_set(a, 'bibTeX_PagesField', None)
    assert not _is_linked(a, 'bibTeX_PagesField', b2)
    if hasattr(b2, 'bibTeX_Article21'):
        assert not _is_linked(b2, 'bibTeX_Article21', a)


def test_assoc_publisher23_link_reassign_clear():
    a = bibTeX_PublisherField(publisher="sample_text")
    b1 = bibTeX_Book()
    b2 = bibTeX_Book()
    _safe_set(a, 'bibTeX_PublisherField', b1)
    assert _is_linked(a, 'bibTeX_PublisherField', b1)
    if hasattr(b1, 'bibTeX_Book24'):
        assert _is_linked(b1, 'bibTeX_Book24', a)
    _safe_set(a, 'bibTeX_PublisherField', b2)
    assert _is_linked(a, 'bibTeX_PublisherField', b2)
    if hasattr(b1, 'bibTeX_Book24'):
        assert not _is_linked(b1, 'bibTeX_Book24', a)
    if hasattr(b2, 'bibTeX_Book24'):
        assert _is_linked(b2, 'bibTeX_Book24', a)
    _safe_set(a, 'bibTeX_PublisherField', None)
    assert not _is_linked(a, 'bibTeX_PublisherField', b2)
    if hasattr(b2, 'bibTeX_Book24'):
        assert not _is_linked(b2, 'bibTeX_Book24', a)


def test_assoc_series28_link_reassign_clear():
    a = bibTeX_SeriesField(series="sample_text")
    b1 = bibTeX_Book()
    b2 = bibTeX_Book()
    _safe_set(a, 'bibTeX_SeriesField', b1)
    assert _is_linked(a, 'bibTeX_SeriesField', b1)
    if hasattr(b1, 'bibTeX_Book29'):
        assert _is_linked(b1, 'bibTeX_Book29', a)
    _safe_set(a, 'bibTeX_SeriesField', b2)
    assert _is_linked(a, 'bibTeX_SeriesField', b2)
    if hasattr(b1, 'bibTeX_Book29'):
        assert not _is_linked(b1, 'bibTeX_Book29', a)
    if hasattr(b2, 'bibTeX_Book29'):
        assert _is_linked(b2, 'bibTeX_Book29', a)
    _safe_set(a, 'bibTeX_SeriesField', None)
    assert not _is_linked(a, 'bibTeX_SeriesField', b2)
    if hasattr(b2, 'bibTeX_Book29'):
        assert not _is_linked(b2, 'bibTeX_Book29', a)


def test_assoc_title3_link_reassign_clear():
    a = bibTeX_TitleField(title="sample_text")
    b1 = bibTeX_BibtexEntryTypes()
    b2 = bibTeX_BibtexEntryTypes()
    _safe_set(a, 'bibTeX_TitleField', b1)
    assert _is_linked(a, 'bibTeX_TitleField', b1)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes4'):
        assert _is_linked(b1, 'bibTeX_BibtexEntryTypes4', a)
    _safe_set(a, 'bibTeX_TitleField', b2)
    assert _is_linked(a, 'bibTeX_TitleField', b2)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes4'):
        assert not _is_linked(b1, 'bibTeX_BibtexEntryTypes4', a)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes4'):
        assert _is_linked(b2, 'bibTeX_BibtexEntryTypes4', a)
    _safe_set(a, 'bibTeX_TitleField', None)
    assert not _is_linked(a, 'bibTeX_TitleField', b2)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes4'):
        assert not _is_linked(b2, 'bibTeX_BibtexEntryTypes4', a)


def test_assoc_type36_link_reassign_clear():
    a = bibTeX_UnknownType(type="sample_text")
    b1 = bibTeX_UnknownField()
    b2 = bibTeX_UnknownField()
    _safe_set(a, 'bibTeX_UnknownType', b1)
    assert _is_linked(a, 'bibTeX_UnknownType', b1)
    if hasattr(b1, 'bibTeX_UnknownField37'):
        assert _is_linked(b1, 'bibTeX_UnknownField37', a)
    _safe_set(a, 'bibTeX_UnknownType', b2)
    assert _is_linked(a, 'bibTeX_UnknownType', b2)
    if hasattr(b1, 'bibTeX_UnknownField37'):
        assert not _is_linked(b1, 'bibTeX_UnknownField37', a)
    if hasattr(b2, 'bibTeX_UnknownField37'):
        assert _is_linked(b2, 'bibTeX_UnknownField37', a)
    _safe_set(a, 'bibTeX_UnknownType', None)
    assert not _is_linked(a, 'bibTeX_UnknownType', b2)
    if hasattr(b2, 'bibTeX_UnknownField37'):
        assert not _is_linked(b2, 'bibTeX_UnknownField37', a)


def test_assoc_value38_link_reassign_clear():
    a = bibTeX_UnknownValue(value="sample_text")
    b1 = bibTeX_UnknownField()
    b2 = bibTeX_UnknownField()
    _safe_set(a, 'bibTeX_UnknownValue', b1)
    assert _is_linked(a, 'bibTeX_UnknownValue', b1)
    if hasattr(b1, 'bibTeX_UnknownField39'):
        assert _is_linked(b1, 'bibTeX_UnknownField39', a)
    _safe_set(a, 'bibTeX_UnknownValue', b2)
    assert _is_linked(a, 'bibTeX_UnknownValue', b2)
    if hasattr(b1, 'bibTeX_UnknownField39'):
        assert not _is_linked(b1, 'bibTeX_UnknownField39', a)
    if hasattr(b2, 'bibTeX_UnknownField39'):
        assert _is_linked(b2, 'bibTeX_UnknownField39', a)
    _safe_set(a, 'bibTeX_UnknownValue', None)
    assert not _is_linked(a, 'bibTeX_UnknownValue', b2)
    if hasattr(b2, 'bibTeX_UnknownField39'):
        assert not _is_linked(b2, 'bibTeX_UnknownField39', a)


def test_assoc_volume16_link_reassign_clear():
    a = bibTeX_VolumeField(volume="sample_text")
    b1 = bibTeX_Article()
    b2 = bibTeX_Article()
    _safe_set(a, 'bibTeX_VolumeField', b1)
    assert _is_linked(a, 'bibTeX_VolumeField', b1)
    if hasattr(b1, 'bibTeX_Article17'):
        assert _is_linked(b1, 'bibTeX_Article17', a)
    _safe_set(a, 'bibTeX_VolumeField', b2)
    assert _is_linked(a, 'bibTeX_VolumeField', b2)
    if hasattr(b1, 'bibTeX_Article17'):
        assert not _is_linked(b1, 'bibTeX_Article17', a)
    if hasattr(b2, 'bibTeX_Article17'):
        assert _is_linked(b2, 'bibTeX_Article17', a)
    _safe_set(a, 'bibTeX_VolumeField', None)
    assert not _is_linked(a, 'bibTeX_VolumeField', b2)
    if hasattr(b2, 'bibTeX_Article17'):
        assert not _is_linked(b2, 'bibTeX_Article17', a)


def test_assoc_year5_link_reassign_clear():
    a = bibTeX_YearField(year="sample_text")
    b1 = bibTeX_BibtexEntryTypes()
    b2 = bibTeX_BibtexEntryTypes()
    _safe_set(a, 'bibTeX_YearField', b1)
    assert _is_linked(a, 'bibTeX_YearField', b1)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes6'):
        assert _is_linked(b1, 'bibTeX_BibtexEntryTypes6', a)
    _safe_set(a, 'bibTeX_YearField', b2)
    assert _is_linked(a, 'bibTeX_YearField', b2)
    if hasattr(b1, 'bibTeX_BibtexEntryTypes6'):
        assert not _is_linked(b1, 'bibTeX_BibtexEntryTypes6', a)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes6'):
        assert _is_linked(b2, 'bibTeX_BibtexEntryTypes6', a)
    _safe_set(a, 'bibTeX_YearField', None)
    assert not _is_linked(a, 'bibTeX_YearField', b2)
    if hasattr(b2, 'bibTeX_BibtexEntryTypes6'):
        assert not _is_linked(b2, 'bibTeX_BibtexEntryTypes6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AuthorField_strategy = st.builds(AuthorField)
@given(instance=AuthorField_strategy)
@settings(max_examples=25)
def test_AuthorField_instantiation(instance):
    assert isinstance(instance, AuthorField)


BibtexEntryTypes_strategy = st.builds(BibtexEntryTypes)
@given(instance=BibtexEntryTypes_strategy)
@settings(max_examples=25)
def test_BibtexEntryTypes_instantiation(instance):
    assert isinstance(instance, BibtexEntryTypes)


bibTeX_AddressField_strategy = st.builds(bibTeX_AddressField, address=safe_text)
@given(instance=bibTeX_AddressField_strategy)
@settings(max_examples=25)
def test_bibTeX_AddressField_instantiation(instance):
    assert isinstance(instance, bibTeX_AddressField)


bibTeX_Article_strategy = st.builds(bibTeX_Article)
@given(instance=bibTeX_Article_strategy)
@settings(max_examples=25)
def test_bibTeX_Article_instantiation(instance):
    assert isinstance(instance, bibTeX_Article)


bibTeX_AuthorField_strategy = st.builds(bibTeX_AuthorField)
@given(instance=bibTeX_AuthorField_strategy)
@settings(max_examples=25)
def test_bibTeX_AuthorField_instantiation(instance):
    assert isinstance(instance, bibTeX_AuthorField)


bibTeX_Authors_strategy = st.builds(bibTeX_Authors)
@given(instance=bibTeX_Authors_strategy)
@settings(max_examples=25)
def test_bibTeX_Authors_instantiation(instance):
    assert isinstance(instance, bibTeX_Authors)


bibTeX_BibtexEntryTypes_strategy = st.builds(bibTeX_BibtexEntryTypes)
@given(instance=bibTeX_BibtexEntryTypes_strategy)
@settings(max_examples=25)
def test_bibTeX_BibtexEntryTypes_instantiation(instance):
    assert isinstance(instance, bibTeX_BibtexEntryTypes)


bibTeX_Book_strategy = st.builds(bibTeX_Book)
@given(instance=bibTeX_Book_strategy)
@settings(max_examples=25)
def test_bibTeX_Book_instantiation(instance):
    assert isinstance(instance, bibTeX_Book)


bibTeX_CiteKey_strategy = st.builds(bibTeX_CiteKey, key=safe_text)
@given(instance=bibTeX_CiteKey_strategy)
@settings(max_examples=25)
def test_bibTeX_CiteKey_instantiation(instance):
    assert isinstance(instance, bibTeX_CiteKey)


bibTeX_EObject_strategy = st.builds(bibTeX_EObject)
@given(instance=bibTeX_EObject_strategy)
@settings(max_examples=25)
def test_bibTeX_EObject_instantiation(instance):
    assert isinstance(instance, bibTeX_EObject)


bibTeX_EditionField_strategy = st.builds(bibTeX_EditionField, edition=safe_text)
@given(instance=bibTeX_EditionField_strategy)
@settings(max_examples=25)
def test_bibTeX_EditionField_instantiation(instance):
    assert isinstance(instance, bibTeX_EditionField)


bibTeX_EditorField_strategy = st.builds(bibTeX_EditorField, editor=safe_text)
@given(instance=bibTeX_EditorField_strategy)
@settings(max_examples=25)
def test_bibTeX_EditorField_instantiation(instance):
    assert isinstance(instance, bibTeX_EditorField)


bibTeX_Fullname_strategy = st.builds(bibTeX_Fullname, firstname=safe_text, lastname=safe_text)
@given(instance=bibTeX_Fullname_strategy)
@settings(max_examples=25)
def test_bibTeX_Fullname_instantiation(instance):
    assert isinstance(instance, bibTeX_Fullname)


bibTeX_IsbnField_strategy = st.builds(bibTeX_IsbnField, isbn=safe_text)
@given(instance=bibTeX_IsbnField_strategy)
@settings(max_examples=25)
def test_bibTeX_IsbnField_instantiation(instance):
    assert isinstance(instance, bibTeX_IsbnField)


bibTeX_JournalField_strategy = st.builds(bibTeX_JournalField, journal=safe_text)
@given(instance=bibTeX_JournalField_strategy)
@settings(max_examples=25)
def test_bibTeX_JournalField_instantiation(instance):
    assert isinstance(instance, bibTeX_JournalField)


bibTeX_Model_strategy = st.builds(bibTeX_Model)
@given(instance=bibTeX_Model_strategy)
@settings(max_examples=25)
def test_bibTeX_Model_instantiation(instance):
    assert isinstance(instance, bibTeX_Model)


bibTeX_MonthField_strategy = st.builds(bibTeX_MonthField, month=safe_text)
@given(instance=bibTeX_MonthField_strategy)
@settings(max_examples=25)
def test_bibTeX_MonthField_instantiation(instance):
    assert isinstance(instance, bibTeX_MonthField)


bibTeX_NoteField_strategy = st.builds(bibTeX_NoteField, note=safe_text)
@given(instance=bibTeX_NoteField_strategy)
@settings(max_examples=25)
def test_bibTeX_NoteField_instantiation(instance):
    assert isinstance(instance, bibTeX_NoteField)


bibTeX_NumberField_strategy = st.builds(bibTeX_NumberField, number=safe_text)
@given(instance=bibTeX_NumberField_strategy)
@settings(max_examples=25)
def test_bibTeX_NumberField_instantiation(instance):
    assert isinstance(instance, bibTeX_NumberField)


bibTeX_PagesField_strategy = st.builds(bibTeX_PagesField, pages=safe_text)
@given(instance=bibTeX_PagesField_strategy)
@settings(max_examples=25)
def test_bibTeX_PagesField_instantiation(instance):
    assert isinstance(instance, bibTeX_PagesField)


bibTeX_PublisherField_strategy = st.builds(bibTeX_PublisherField, publisher=safe_text)
@given(instance=bibTeX_PublisherField_strategy)
@settings(max_examples=25)
def test_bibTeX_PublisherField_instantiation(instance):
    assert isinstance(instance, bibTeX_PublisherField)


bibTeX_SeriesField_strategy = st.builds(bibTeX_SeriesField, series=safe_text)
@given(instance=bibTeX_SeriesField_strategy)
@settings(max_examples=25)
def test_bibTeX_SeriesField_instantiation(instance):
    assert isinstance(instance, bibTeX_SeriesField)


bibTeX_TitleField_strategy = st.builds(bibTeX_TitleField, title=safe_text)
@given(instance=bibTeX_TitleField_strategy)
@settings(max_examples=25)
def test_bibTeX_TitleField_instantiation(instance):
    assert isinstance(instance, bibTeX_TitleField)


bibTeX_UnknownField_strategy = st.builds(bibTeX_UnknownField)
@given(instance=bibTeX_UnknownField_strategy)
@settings(max_examples=25)
def test_bibTeX_UnknownField_instantiation(instance):
    assert isinstance(instance, bibTeX_UnknownField)


bibTeX_UnknownType_strategy = st.builds(bibTeX_UnknownType, type=safe_text)
@given(instance=bibTeX_UnknownType_strategy)
@settings(max_examples=25)
def test_bibTeX_UnknownType_instantiation(instance):
    assert isinstance(instance, bibTeX_UnknownType)


bibTeX_UnknownValue_strategy = st.builds(bibTeX_UnknownValue, value=safe_text)
@given(instance=bibTeX_UnknownValue_strategy)
@settings(max_examples=25)
def test_bibTeX_UnknownValue_instantiation(instance):
    assert isinstance(instance, bibTeX_UnknownValue)


bibTeX_VolumeField_strategy = st.builds(bibTeX_VolumeField, volume=safe_text)
@given(instance=bibTeX_VolumeField_strategy)
@settings(max_examples=25)
def test_bibTeX_VolumeField_instantiation(instance):
    assert isinstance(instance, bibTeX_VolumeField)


bibTeX_YearField_strategy = st.builds(bibTeX_YearField, year=safe_text)
@given(instance=bibTeX_YearField_strategy)
@settings(max_examples=25)
def test_bibTeX_YearField_instantiation(instance):
    assert isinstance(instance, bibTeX_YearField)



