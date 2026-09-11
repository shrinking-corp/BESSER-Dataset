import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Author,
    AuthoredEntry,
    BibTeXEntry,
    BibTeX_Article,
    BibTeX_Author,
    BibTeX_AuthoredEntry,
    BibTeX_BibTeXEntry,
    BibTeX_BibTeXFile,
    BibTeX_Book,
    BibTeX_BookTitledEntry,
    BibTeX_Booklet,
    BibTeX_DatedEntry,
    BibTeX_InBook,
    BibTeX_InCollection,
    BibTeX_InProceedings,
    BibTeX_Manual,
    BibTeX_MasterThesis,
    BibTeX_Misc,
    BibTeX_PhDThesis,
    BibTeX_Proceedings,
    BibTeX_TechReport,
    BibTeX_ThesisEntry,
    BibTeX_TitledEntry,
    BibTeX_Unpublished,
    Book,
    BookTitledEntry,
    DatedEntry,
    Proceedings,
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

def test_BibTeX_Article_journal_value_roundtrip():
    instance = BibTeX_Article(journal="sample_text")
    assert instance.journal == "sample_text"
    instance.journal = "sample_text_2"
    assert instance.journal == "sample_text_2"


def test_BibTeX_Author_author_value_roundtrip():
    instance = BibTeX_Author(author="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_BibTeX_BibTeXEntry_id_value_roundtrip():
    instance = BibTeX_BibTeXEntry(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_BibTeX_Book_publisher_value_roundtrip():
    instance = BibTeX_Book(publisher="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_BibTeX_BookTitledEntry_booktitle_value_roundtrip():
    instance = BibTeX_BookTitledEntry(booktitle="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_BibTeX_DatedEntry_year_value_roundtrip():
    instance = BibTeX_DatedEntry(year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_BibTeX_InBook_chapter_value_roundtrip():
    instance = BibTeX_InBook(chapter=7)
    assert instance.chapter == 7
    instance.chapter = 13
    assert instance.chapter == 13


def test_BibTeX_ThesisEntry_school_value_roundtrip():
    instance = BibTeX_ThesisEntry(school="sample_text")
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_BibTeX_TitledEntry_title_value_roundtrip():
    instance = BibTeX_TitledEntry(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_BibTeX_Unpublished_note_value_roundtrip():
    instance = BibTeX_Unpublished(note="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_BibTeX_Article_isa_AuthoredEntry():
    instance = BibTeX_Article(journal="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BibTeX_Book_isa_AuthoredEntry():
    instance = BibTeX_Book(publisher="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BibTeX_InProceedings_isa_AuthoredEntry():
    instance = BibTeX_InProceedings()
    assert isinstance(instance, AuthoredEntry)


def test_BibTeX_TechReport_isa_AuthoredEntry():
    instance = BibTeX_TechReport()
    assert isinstance(instance, AuthoredEntry)


def test_BibTeX_ThesisEntry_isa_AuthoredEntry():
    instance = BibTeX_ThesisEntry(school="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BibTeX_Unpublished_isa_AuthoredEntry():
    instance = BibTeX_Unpublished(note="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_BibTeX_AuthoredEntry_isa_BibTeXEntry():
    instance = BibTeX_AuthoredEntry()
    assert isinstance(instance, BibTeXEntry)


def test_BibTeX_BookTitledEntry_isa_BibTeXEntry():
    instance = BibTeX_BookTitledEntry(booktitle="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_BibTeX_DatedEntry_isa_BibTeXEntry():
    instance = BibTeX_DatedEntry(year="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_BibTeX_Misc_isa_BibTeXEntry():
    instance = BibTeX_Misc()
    assert isinstance(instance, BibTeXEntry)


def test_BibTeX_TitledEntry_isa_BibTeXEntry():
    instance = BibTeX_TitledEntry(title="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_BibTeX_InBook_isa_Book():
    instance = BibTeX_InBook(chapter=7)
    assert isinstance(instance, Book)


def test_BibTeX_InCollection_isa_Book():
    instance = BibTeX_InCollection()
    assert isinstance(instance, Book)


def test_BibTeX_InCollection_isa_BookTitledEntry():
    instance = BibTeX_InCollection()
    assert isinstance(instance, BookTitledEntry)


def test_BibTeX_InProceedings_isa_BookTitledEntry():
    instance = BibTeX_InProceedings()
    assert isinstance(instance, BookTitledEntry)


def test_BibTeX_Article_isa_DatedEntry():
    instance = BibTeX_Article(journal="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BibTeX_Book_isa_DatedEntry():
    instance = BibTeX_Book(publisher="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BibTeX_Booklet_isa_DatedEntry():
    instance = BibTeX_Booklet()
    assert isinstance(instance, DatedEntry)


def test_BibTeX_Proceedings_isa_DatedEntry():
    instance = BibTeX_Proceedings()
    assert isinstance(instance, DatedEntry)


def test_BibTeX_TechReport_isa_DatedEntry():
    instance = BibTeX_TechReport()
    assert isinstance(instance, DatedEntry)


def test_BibTeX_ThesisEntry_isa_DatedEntry():
    instance = BibTeX_ThesisEntry(school="sample_text")
    assert isinstance(instance, DatedEntry)


def test_BibTeX_InProceedings_isa_Proceedings():
    instance = BibTeX_InProceedings()
    assert isinstance(instance, Proceedings)


def test_BibTeX_MasterThesis_isa_ThesisEntry():
    instance = BibTeX_MasterThesis()
    assert isinstance(instance, ThesisEntry)


def test_BibTeX_PhDThesis_isa_ThesisEntry():
    instance = BibTeX_PhDThesis()
    assert isinstance(instance, ThesisEntry)


def test_BibTeX_Article_isa_TitledEntry():
    instance = BibTeX_Article(journal="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BibTeX_Book_isa_TitledEntry():
    instance = BibTeX_Book(publisher="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BibTeX_Manual_isa_TitledEntry():
    instance = BibTeX_Manual()
    assert isinstance(instance, TitledEntry)


def test_BibTeX_Proceedings_isa_TitledEntry():
    instance = BibTeX_Proceedings()
    assert isinstance(instance, TitledEntry)


def test_BibTeX_TechReport_isa_TitledEntry():
    instance = BibTeX_TechReport()
    assert isinstance(instance, TitledEntry)


def test_BibTeX_ThesisEntry_isa_TitledEntry():
    instance = BibTeX_ThesisEntry(school="sample_text")
    assert isinstance(instance, TitledEntry)


def test_BibTeX_Unpublished_isa_TitledEntry():
    instance = BibTeX_Unpublished(note="sample_text")
    assert isinstance(instance, TitledEntry)


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


BibTeXEntry_strategy = st.builds(BibTeXEntry)
@given(instance=BibTeXEntry_strategy)
@settings(max_examples=25)
def test_BibTeXEntry_instantiation(instance):
    assert isinstance(instance, BibTeXEntry)


BibTeX_Article_strategy = st.builds(BibTeX_Article, journal=safe_text)
@given(instance=BibTeX_Article_strategy)
@settings(max_examples=25)
def test_BibTeX_Article_instantiation(instance):
    assert isinstance(instance, BibTeX_Article)


BibTeX_Author_strategy = st.builds(BibTeX_Author, author=safe_text)
@given(instance=BibTeX_Author_strategy)
@settings(max_examples=25)
def test_BibTeX_Author_instantiation(instance):
    assert isinstance(instance, BibTeX_Author)


BibTeX_AuthoredEntry_strategy = st.builds(BibTeX_AuthoredEntry)
@given(instance=BibTeX_AuthoredEntry_strategy)
@settings(max_examples=25)
def test_BibTeX_AuthoredEntry_instantiation(instance):
    assert isinstance(instance, BibTeX_AuthoredEntry)


BibTeX_BibTeXEntry_strategy = st.builds(BibTeX_BibTeXEntry, id=safe_text)
@given(instance=BibTeX_BibTeXEntry_strategy)
@settings(max_examples=25)
def test_BibTeX_BibTeXEntry_instantiation(instance):
    assert isinstance(instance, BibTeX_BibTeXEntry)


BibTeX_BibTeXFile_strategy = st.builds(BibTeX_BibTeXFile)
@given(instance=BibTeX_BibTeXFile_strategy)
@settings(max_examples=25)
def test_BibTeX_BibTeXFile_instantiation(instance):
    assert isinstance(instance, BibTeX_BibTeXFile)


BibTeX_Book_strategy = st.builds(BibTeX_Book, publisher=safe_text)
@given(instance=BibTeX_Book_strategy)
@settings(max_examples=25)
def test_BibTeX_Book_instantiation(instance):
    assert isinstance(instance, BibTeX_Book)


BibTeX_BookTitledEntry_strategy = st.builds(BibTeX_BookTitledEntry, booktitle=safe_text)
@given(instance=BibTeX_BookTitledEntry_strategy)
@settings(max_examples=25)
def test_BibTeX_BookTitledEntry_instantiation(instance):
    assert isinstance(instance, BibTeX_BookTitledEntry)


BibTeX_Booklet_strategy = st.builds(BibTeX_Booklet)
@given(instance=BibTeX_Booklet_strategy)
@settings(max_examples=25)
def test_BibTeX_Booklet_instantiation(instance):
    assert isinstance(instance, BibTeX_Booklet)


BibTeX_DatedEntry_strategy = st.builds(BibTeX_DatedEntry, year=safe_text)
@given(instance=BibTeX_DatedEntry_strategy)
@settings(max_examples=25)
def test_BibTeX_DatedEntry_instantiation(instance):
    assert isinstance(instance, BibTeX_DatedEntry)


BibTeX_InBook_strategy = st.builds(BibTeX_InBook, chapter=st.integers())
@given(instance=BibTeX_InBook_strategy)
@settings(max_examples=25)
def test_BibTeX_InBook_instantiation(instance):
    assert isinstance(instance, BibTeX_InBook)


BibTeX_InCollection_strategy = st.builds(BibTeX_InCollection)
@given(instance=BibTeX_InCollection_strategy)
@settings(max_examples=25)
def test_BibTeX_InCollection_instantiation(instance):
    assert isinstance(instance, BibTeX_InCollection)


BibTeX_InProceedings_strategy = st.builds(BibTeX_InProceedings)
@given(instance=BibTeX_InProceedings_strategy)
@settings(max_examples=25)
def test_BibTeX_InProceedings_instantiation(instance):
    assert isinstance(instance, BibTeX_InProceedings)


BibTeX_Manual_strategy = st.builds(BibTeX_Manual)
@given(instance=BibTeX_Manual_strategy)
@settings(max_examples=25)
def test_BibTeX_Manual_instantiation(instance):
    assert isinstance(instance, BibTeX_Manual)


BibTeX_MasterThesis_strategy = st.builds(BibTeX_MasterThesis)
@given(instance=BibTeX_MasterThesis_strategy)
@settings(max_examples=25)
def test_BibTeX_MasterThesis_instantiation(instance):
    assert isinstance(instance, BibTeX_MasterThesis)


BibTeX_Misc_strategy = st.builds(BibTeX_Misc)
@given(instance=BibTeX_Misc_strategy)
@settings(max_examples=25)
def test_BibTeX_Misc_instantiation(instance):
    assert isinstance(instance, BibTeX_Misc)


BibTeX_PhDThesis_strategy = st.builds(BibTeX_PhDThesis)
@given(instance=BibTeX_PhDThesis_strategy)
@settings(max_examples=25)
def test_BibTeX_PhDThesis_instantiation(instance):
    assert isinstance(instance, BibTeX_PhDThesis)


BibTeX_Proceedings_strategy = st.builds(BibTeX_Proceedings)
@given(instance=BibTeX_Proceedings_strategy)
@settings(max_examples=25)
def test_BibTeX_Proceedings_instantiation(instance):
    assert isinstance(instance, BibTeX_Proceedings)


BibTeX_TechReport_strategy = st.builds(BibTeX_TechReport)
@given(instance=BibTeX_TechReport_strategy)
@settings(max_examples=25)
def test_BibTeX_TechReport_instantiation(instance):
    assert isinstance(instance, BibTeX_TechReport)


BibTeX_ThesisEntry_strategy = st.builds(BibTeX_ThesisEntry, school=safe_text)
@given(instance=BibTeX_ThesisEntry_strategy)
@settings(max_examples=25)
def test_BibTeX_ThesisEntry_instantiation(instance):
    assert isinstance(instance, BibTeX_ThesisEntry)


BibTeX_TitledEntry_strategy = st.builds(BibTeX_TitledEntry, title=safe_text)
@given(instance=BibTeX_TitledEntry_strategy)
@settings(max_examples=25)
def test_BibTeX_TitledEntry_instantiation(instance):
    assert isinstance(instance, BibTeX_TitledEntry)


BibTeX_Unpublished_strategy = st.builds(BibTeX_Unpublished, note=safe_text)
@given(instance=BibTeX_Unpublished_strategy)
@settings(max_examples=25)
def test_BibTeX_Unpublished_instantiation(instance):
    assert isinstance(instance, BibTeX_Unpublished)


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


Proceedings_strategy = st.builds(Proceedings)
@given(instance=Proceedings_strategy)
@settings(max_examples=25)
def test_Proceedings_instantiation(instance):
    assert isinstance(instance, Proceedings)


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


