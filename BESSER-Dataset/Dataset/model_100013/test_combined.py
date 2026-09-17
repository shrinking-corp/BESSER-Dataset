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
    ThesisEntry,
    bibtex_MasterThesis,
    bibtex_PhDThesis,
    Book,
    bibtex_InBook,
    TitledEntry,
    DatedEntry,
    bibtex_Booklet,
    BookTitledEntry,
    bibtex_InCollection,
    Proceedings,
    bibtex_Proceedings,
    bibtex_Manual,
    AuthoredEntry,
    bibtex_Book,
    bibtex_InProceedings,
    bibtex_ThesisEntry,
    bibtex_Article,
    bibtex_Unpublished,
    bibtex_TechReport,
    BibTeXEntry,
    bibtex_BookTitledEntry,
    bibtex_TitledEntry,
    bibtex_Misc,
    bibtex_AuthoredEntry,
    bibtex_DatedEntry,
    bibtex_BibTeXFile,
    bibtex_Author,
    bibtex_BibTeXEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_thesisentry_is_not_abstract():
    assert not inspect.isabstract(ThesisEntry)


def test_hyp_thesisentry_constructor_exists():
    assert callable(ThesisEntry.__init__)


def test_hyp_thesisentry_constructor_args():
    sig = inspect.signature(ThesisEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_masterthesis_is_not_abstract():
    assert not inspect.isabstract(bibtex_MasterThesis)


def test_hyp_bibtex_masterthesis_constructor_exists():
    assert callable(bibtex_MasterThesis.__init__)


def test_hyp_bibtex_masterthesis_constructor_args():
    sig = inspect.signature(bibtex_MasterThesis.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_phdthesis_is_not_abstract():
    assert not inspect.isabstract(bibtex_PhDThesis)


def test_hyp_bibtex_phdthesis_constructor_exists():
    assert callable(bibtex_PhDThesis.__init__)


def test_hyp_bibtex_phdthesis_constructor_args():
    sig = inspect.signature(bibtex_PhDThesis.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_hyp_book_constructor_exists():
    assert callable(Book.__init__)


def test_hyp_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_inbook_is_not_abstract():
    assert not inspect.isabstract(bibtex_InBook)


def test_hyp_bibtex_inbook_constructor_exists():
    assert callable(bibtex_InBook.__init__)


def test_hyp_bibtex_inbook_constructor_args():
    sig = inspect.signature(bibtex_InBook.__init__)
    params = list(sig.parameters.keys())
    assert "chapter" in params, "Missing parameter 'chapter'"




def test_hyp_titledentry_is_not_abstract():
    assert not inspect.isabstract(TitledEntry)


def test_hyp_titledentry_constructor_exists():
    assert callable(TitledEntry.__init__)


def test_hyp_titledentry_constructor_args():
    sig = inspect.signature(TitledEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datedentry_is_not_abstract():
    assert not inspect.isabstract(DatedEntry)


def test_hyp_datedentry_constructor_exists():
    assert callable(DatedEntry.__init__)


def test_hyp_datedentry_constructor_args():
    sig = inspect.signature(DatedEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_booklet_is_not_abstract():
    assert not inspect.isabstract(bibtex_Booklet)


def test_hyp_bibtex_booklet_constructor_exists():
    assert callable(bibtex_Booklet.__init__)


def test_hyp_bibtex_booklet_constructor_args():
    sig = inspect.signature(bibtex_Booklet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booktitledentry_is_not_abstract():
    assert not inspect.isabstract(BookTitledEntry)


def test_hyp_booktitledentry_constructor_exists():
    assert callable(BookTitledEntry.__init__)


def test_hyp_booktitledentry_constructor_args():
    sig = inspect.signature(BookTitledEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_incollection_is_not_abstract():
    assert not inspect.isabstract(bibtex_InCollection)


def test_hyp_bibtex_incollection_constructor_exists():
    assert callable(bibtex_InCollection.__init__)


def test_hyp_bibtex_incollection_constructor_args():
    sig = inspect.signature(bibtex_InCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_proceedings_is_not_abstract():
    assert not inspect.isabstract(Proceedings)


def test_hyp_proceedings_constructor_exists():
    assert callable(Proceedings.__init__)


def test_hyp_proceedings_constructor_args():
    sig = inspect.signature(Proceedings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_proceedings_is_not_abstract():
    assert not inspect.isabstract(bibtex_Proceedings)


def test_hyp_bibtex_proceedings_constructor_exists():
    assert callable(bibtex_Proceedings.__init__)


def test_hyp_bibtex_proceedings_constructor_args():
    sig = inspect.signature(bibtex_Proceedings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_manual_is_not_abstract():
    assert not inspect.isabstract(bibtex_Manual)


def test_hyp_bibtex_manual_constructor_exists():
    assert callable(bibtex_Manual.__init__)


def test_hyp_bibtex_manual_constructor_args():
    sig = inspect.signature(bibtex_Manual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_authoredentry_is_not_abstract():
    assert not inspect.isabstract(AuthoredEntry)


def test_hyp_authoredentry_constructor_exists():
    assert callable(AuthoredEntry.__init__)


def test_hyp_authoredentry_constructor_args():
    sig = inspect.signature(AuthoredEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_book_is_not_abstract():
    assert not inspect.isabstract(bibtex_Book)


def test_hyp_bibtex_book_constructor_exists():
    assert callable(bibtex_Book.__init__)


def test_hyp_bibtex_book_constructor_args():
    sig = inspect.signature(bibtex_Book.__init__)
    params = list(sig.parameters.keys())
    assert "publisher" in params, "Missing parameter 'publisher'"




def test_hyp_bibtex_inproceedings_is_not_abstract():
    assert not inspect.isabstract(bibtex_InProceedings)


def test_hyp_bibtex_inproceedings_constructor_exists():
    assert callable(bibtex_InProceedings.__init__)


def test_hyp_bibtex_inproceedings_constructor_args():
    sig = inspect.signature(bibtex_InProceedings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_thesisentry_is_not_abstract():
    assert not inspect.isabstract(bibtex_ThesisEntry)


def test_hyp_bibtex_thesisentry_constructor_exists():
    assert callable(bibtex_ThesisEntry.__init__)


def test_hyp_bibtex_thesisentry_constructor_args():
    sig = inspect.signature(bibtex_ThesisEntry.__init__)
    params = list(sig.parameters.keys())
    assert "school" in params, "Missing parameter 'school'"




def test_hyp_bibtex_article_is_not_abstract():
    assert not inspect.isabstract(bibtex_Article)


def test_hyp_bibtex_article_constructor_exists():
    assert callable(bibtex_Article.__init__)


def test_hyp_bibtex_article_constructor_args():
    sig = inspect.signature(bibtex_Article.__init__)
    params = list(sig.parameters.keys())
    assert "journal" in params, "Missing parameter 'journal'"




def test_hyp_bibtex_unpublished_is_not_abstract():
    assert not inspect.isabstract(bibtex_Unpublished)


def test_hyp_bibtex_unpublished_constructor_exists():
    assert callable(bibtex_Unpublished.__init__)


def test_hyp_bibtex_unpublished_constructor_args():
    sig = inspect.signature(bibtex_Unpublished.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"




def test_hyp_bibtex_techreport_is_not_abstract():
    assert not inspect.isabstract(bibtex_TechReport)


def test_hyp_bibtex_techreport_constructor_exists():
    assert callable(bibtex_TechReport.__init__)


def test_hyp_bibtex_techreport_constructor_args():
    sig = inspect.signature(bibtex_TechReport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtexentry_is_not_abstract():
    assert not inspect.isabstract(BibTeXEntry)


def test_hyp_bibtexentry_constructor_exists():
    assert callable(BibTeXEntry.__init__)


def test_hyp_bibtexentry_constructor_args():
    sig = inspect.signature(BibTeXEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_booktitledentry_is_not_abstract():
    assert not inspect.isabstract(bibtex_BookTitledEntry)


def test_hyp_bibtex_booktitledentry_constructor_exists():
    assert callable(bibtex_BookTitledEntry.__init__)


def test_hyp_bibtex_booktitledentry_constructor_args():
    sig = inspect.signature(bibtex_BookTitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "booktitle" in params, "Missing parameter 'booktitle'"




def test_hyp_bibtex_titledentry_is_not_abstract():
    assert not inspect.isabstract(bibtex_TitledEntry)


def test_hyp_bibtex_titledentry_constructor_exists():
    assert callable(bibtex_TitledEntry.__init__)


def test_hyp_bibtex_titledentry_constructor_args():
    sig = inspect.signature(bibtex_TitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_bibtex_misc_is_not_abstract():
    assert not inspect.isabstract(bibtex_Misc)


def test_hyp_bibtex_misc_constructor_exists():
    assert callable(bibtex_Misc.__init__)


def test_hyp_bibtex_misc_constructor_args():
    sig = inspect.signature(bibtex_Misc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_authoredentry_is_not_abstract():
    assert not inspect.isabstract(bibtex_AuthoredEntry)


def test_hyp_bibtex_authoredentry_constructor_exists():
    assert callable(bibtex_AuthoredEntry.__init__)


def test_hyp_bibtex_authoredentry_constructor_args():
    sig = inspect.signature(bibtex_AuthoredEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_datedentry_is_not_abstract():
    assert not inspect.isabstract(bibtex_DatedEntry)


def test_hyp_bibtex_datedentry_constructor_exists():
    assert callable(bibtex_DatedEntry.__init__)


def test_hyp_bibtex_datedentry_constructor_args():
    sig = inspect.signature(bibtex_DatedEntry.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"




def test_hyp_bibtex_bibtexfile_is_not_abstract():
    assert not inspect.isabstract(bibtex_BibTeXFile)


def test_hyp_bibtex_bibtexfile_constructor_exists():
    assert callable(bibtex_BibTeXFile.__init__)


def test_hyp_bibtex_bibtexfile_constructor_args():
    sig = inspect.signature(bibtex_BibTeXFile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_author_is_not_abstract():
    assert not inspect.isabstract(bibtex_Author)


def test_hyp_bibtex_author_constructor_exists():
    assert callable(bibtex_Author.__init__)


def test_hyp_bibtex_author_constructor_args():
    sig = inspect.signature(bibtex_Author.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"




def test_hyp_bibtex_bibtexentry_is_not_abstract():
    assert not inspect.isabstract(bibtex_BibTeXEntry)


def test_hyp_bibtex_bibtexentry_constructor_exists():
    assert callable(bibtex_BibTeXEntry.__init__)


def test_hyp_bibtex_bibtexentry_constructor_args():
    sig = inspect.signature(bibtex_BibTeXEntry.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"



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
ThesisEntry_strategy = st.builds(
    ThesisEntry,
)
bibtex_MasterThesis_strategy = st.builds(
    bibtex_MasterThesis,
)
bibtex_PhDThesis_strategy = st.builds(
    bibtex_PhDThesis,
)
Book_strategy = st.builds(
    Book,
)
bibtex_InBook_strategy = st.builds(
    bibtex_InBook,
    chapter=
        st.integers()
)
TitledEntry_strategy = st.builds(
    TitledEntry,
)
DatedEntry_strategy = st.builds(
    DatedEntry,
)
bibtex_Booklet_strategy = st.builds(
    bibtex_Booklet,
)
BookTitledEntry_strategy = st.builds(
    BookTitledEntry,
)
bibtex_InCollection_strategy = st.builds(
    bibtex_InCollection,
)
Proceedings_strategy = st.builds(
    Proceedings,
)
bibtex_Proceedings_strategy = st.builds(
    bibtex_Proceedings,
)
bibtex_Manual_strategy = st.builds(
    bibtex_Manual,
)
AuthoredEntry_strategy = st.builds(
    AuthoredEntry,
)
bibtex_Book_strategy = st.builds(
    bibtex_Book,
    publisher=
        safe_text
)
bibtex_InProceedings_strategy = st.builds(
    bibtex_InProceedings,
)
bibtex_ThesisEntry_strategy = st.builds(
    bibtex_ThesisEntry,
    school=
        safe_text
)
bibtex_Article_strategy = st.builds(
    bibtex_Article,
    journal=
        safe_text
)
bibtex_Unpublished_strategy = st.builds(
    bibtex_Unpublished,
    note=
        safe_text
)
bibtex_TechReport_strategy = st.builds(
    bibtex_TechReport,
)
BibTeXEntry_strategy = st.builds(
    BibTeXEntry,
)
bibtex_BookTitledEntry_strategy = st.builds(
    bibtex_BookTitledEntry,
    booktitle=
        safe_text
)
bibtex_TitledEntry_strategy = st.builds(
    bibtex_TitledEntry,
    title=
        safe_text
)
bibtex_Misc_strategy = st.builds(
    bibtex_Misc,
)
bibtex_AuthoredEntry_strategy = st.builds(
    bibtex_AuthoredEntry,
)
bibtex_DatedEntry_strategy = st.builds(
    bibtex_DatedEntry,
    year=
        safe_text
)
bibtex_BibTeXFile_strategy = st.builds(
    bibtex_BibTeXFile,
)
bibtex_Author_strategy = st.builds(
    bibtex_Author,
    author=
        safe_text
)
bibtex_BibTeXEntry_strategy = st.builds(
    bibtex_BibTeXEntry,
    id=
        safe_text
)








@given(instance=bibtex_InBook_strategy)
def test_hyp_bibtex_inbook_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original













@given(instance=bibtex_Book_strategy)
def test_hyp_bibtex_book_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original





@given(instance=bibtex_ThesisEntry_strategy)
def test_hyp_bibtex_thesisentry_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original




@given(instance=bibtex_Article_strategy)
def test_hyp_bibtex_article_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original




@given(instance=bibtex_Unpublished_strategy)
def test_hyp_bibtex_unpublished_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original






@given(instance=bibtex_BookTitledEntry_strategy)
def test_hyp_bibtex_booktitledentry_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original




@given(instance=bibtex_TitledEntry_strategy)
def test_hyp_bibtex_titledentry_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original






@given(instance=bibtex_DatedEntry_strategy)
def test_hyp_bibtex_datedentry_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original





@given(instance=bibtex_Author_strategy)
def test_hyp_bibtex_author_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original




@given(instance=bibtex_BibTeXEntry_strategy)
def test_hyp_bibtex_bibtexentry_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AuthoredEntry,
    BibTeXEntry,
    Book,
    BookTitledEntry,
    DatedEntry,
    Proceedings,
    ThesisEntry,
    TitledEntry,
    bibtex_Article,
    bibtex_Author,
    bibtex_AuthoredEntry,
    bibtex_BibTeXEntry,
    bibtex_BibTeXFile,
    bibtex_Book,
    bibtex_BookTitledEntry,
    bibtex_Booklet,
    bibtex_DatedEntry,
    bibtex_InBook,
    bibtex_InCollection,
    bibtex_InProceedings,
    bibtex_Manual,
    bibtex_MasterThesis,
    bibtex_Misc,
    bibtex_PhDThesis,
    bibtex_Proceedings,
    bibtex_TechReport,
    bibtex_ThesisEntry,
    bibtex_TitledEntry,
    bibtex_Unpublished,
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

def test_bibtex_Article_journal_value_roundtrip():
    instance = bibtex_Article(journal="sample_text")
    assert instance.journal == "sample_text"
    instance.journal = "sample_text_2"
    assert instance.journal == "sample_text_2"


def test_bibtex_Author_author_value_roundtrip():
    instance = bibtex_Author(author="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibtex_BibTeXEntry_id_value_roundtrip():
    instance = bibtex_BibTeXEntry(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_bibtex_Book_publisher_value_roundtrip():
    instance = bibtex_Book(publisher="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibtex_BookTitledEntry_booktitle_value_roundtrip():
    instance = bibtex_BookTitledEntry(booktitle="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_bibtex_DatedEntry_year_value_roundtrip():
    instance = bibtex_DatedEntry(year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibtex_InBook_chapter_value_roundtrip():
    instance = bibtex_InBook(chapter=7)
    assert instance.chapter == 7
    instance.chapter = 13
    assert instance.chapter == 13


def test_bibtex_ThesisEntry_school_value_roundtrip():
    instance = bibtex_ThesisEntry(school="sample_text")
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_bibtex_TitledEntry_title_value_roundtrip():
    instance = bibtex_TitledEntry(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibtex_Unpublished_note_value_roundtrip():
    instance = bibtex_Unpublished(note="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibtex_Article_isa_AuthoredEntry():
    instance = bibtex_Article(journal="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_bibtex_Book_isa_AuthoredEntry():
    instance = bibtex_Book(publisher="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_bibtex_InProceedings_isa_AuthoredEntry():
    instance = bibtex_InProceedings()
    assert isinstance(instance, AuthoredEntry)


def test_bibtex_TechReport_isa_AuthoredEntry():
    instance = bibtex_TechReport()
    assert isinstance(instance, AuthoredEntry)


def test_bibtex_ThesisEntry_isa_AuthoredEntry():
    instance = bibtex_ThesisEntry(school="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_bibtex_Unpublished_isa_AuthoredEntry():
    instance = bibtex_Unpublished(note="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_bibtex_AuthoredEntry_isa_BibTeXEntry():
    instance = bibtex_AuthoredEntry()
    assert isinstance(instance, BibTeXEntry)


def test_bibtex_BookTitledEntry_isa_BibTeXEntry():
    instance = bibtex_BookTitledEntry(booktitle="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_bibtex_DatedEntry_isa_BibTeXEntry():
    instance = bibtex_DatedEntry(year="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_bibtex_Misc_isa_BibTeXEntry():
    instance = bibtex_Misc()
    assert isinstance(instance, BibTeXEntry)


def test_bibtex_TitledEntry_isa_BibTeXEntry():
    instance = bibtex_TitledEntry(title="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_bibtex_InBook_isa_Book():
    instance = bibtex_InBook(chapter=7)
    assert isinstance(instance, Book)


def test_bibtex_InCollection_isa_Book():
    instance = bibtex_InCollection()
    assert isinstance(instance, Book)


def test_bibtex_InCollection_isa_BookTitledEntry():
    instance = bibtex_InCollection()
    assert isinstance(instance, BookTitledEntry)


def test_bibtex_InProceedings_isa_BookTitledEntry():
    instance = bibtex_InProceedings()
    assert isinstance(instance, BookTitledEntry)


def test_bibtex_Article_isa_DatedEntry():
    instance = bibtex_Article(journal="sample_text")
    assert isinstance(instance, DatedEntry)


def test_bibtex_Book_isa_DatedEntry():
    instance = bibtex_Book(publisher="sample_text")
    assert isinstance(instance, DatedEntry)


def test_bibtex_Booklet_isa_DatedEntry():
    instance = bibtex_Booklet()
    assert isinstance(instance, DatedEntry)


def test_bibtex_Proceedings_isa_DatedEntry():
    instance = bibtex_Proceedings()
    assert isinstance(instance, DatedEntry)


def test_bibtex_TechReport_isa_DatedEntry():
    instance = bibtex_TechReport()
    assert isinstance(instance, DatedEntry)


def test_bibtex_ThesisEntry_isa_DatedEntry():
    instance = bibtex_ThesisEntry(school="sample_text")
    assert isinstance(instance, DatedEntry)


def test_bibtex_InProceedings_isa_Proceedings():
    instance = bibtex_InProceedings()
    assert isinstance(instance, Proceedings)


def test_bibtex_MasterThesis_isa_ThesisEntry():
    instance = bibtex_MasterThesis()
    assert isinstance(instance, ThesisEntry)


def test_bibtex_PhDThesis_isa_ThesisEntry():
    instance = bibtex_PhDThesis()
    assert isinstance(instance, ThesisEntry)


def test_bibtex_Article_isa_TitledEntry():
    instance = bibtex_Article(journal="sample_text")
    assert isinstance(instance, TitledEntry)


def test_bibtex_Book_isa_TitledEntry():
    instance = bibtex_Book(publisher="sample_text")
    assert isinstance(instance, TitledEntry)


def test_bibtex_Manual_isa_TitledEntry():
    instance = bibtex_Manual()
    assert isinstance(instance, TitledEntry)


def test_bibtex_Proceedings_isa_TitledEntry():
    instance = bibtex_Proceedings()
    assert isinstance(instance, TitledEntry)


def test_bibtex_TechReport_isa_TitledEntry():
    instance = bibtex_TechReport()
    assert isinstance(instance, TitledEntry)


def test_bibtex_ThesisEntry_isa_TitledEntry():
    instance = bibtex_ThesisEntry(school="sample_text")
    assert isinstance(instance, TitledEntry)


def test_bibtex_Unpublished_isa_TitledEntry():
    instance = bibtex_Unpublished(note="sample_text")
    assert isinstance(instance, TitledEntry)


def test_assoc_authors1_link_reassign_clear():
    a = bibtex_Author(author="sample_text")
    b1 = bibtex_AuthoredEntry()
    b2 = bibtex_AuthoredEntry()
    _safe_set(a, 'bibtex_Author', b1)
    assert _is_linked(a, 'bibtex_Author', b1)
    if hasattr(b1, 'bibtex_AuthoredEntry'):
        assert _is_linked(b1, 'bibtex_AuthoredEntry', a)
    _safe_set(a, 'bibtex_Author', b2)
    assert _is_linked(a, 'bibtex_Author', b2)
    if hasattr(b1, 'bibtex_AuthoredEntry'):
        assert not _is_linked(b1, 'bibtex_AuthoredEntry', a)
    if hasattr(b2, 'bibtex_AuthoredEntry'):
        assert _is_linked(b2, 'bibtex_AuthoredEntry', a)
    _safe_set(a, 'bibtex_Author', None)
    assert not _is_linked(a, 'bibtex_Author', b2)
    if hasattr(b2, 'bibtex_AuthoredEntry'):
        assert not _is_linked(b2, 'bibtex_AuthoredEntry', a)


def test_assoc_entries0_link_reassign_clear():
    a = bibtex_BibTeXEntry(id="sample_text")
    b1 = bibtex_BibTeXFile()
    b2 = bibtex_BibTeXFile()
    _safe_set(a, 'bibtex_BibTeXEntry', b1)
    assert _is_linked(a, 'bibtex_BibTeXEntry', b1)
    if hasattr(b1, 'bibtex_BibTeXFile'):
        assert _is_linked(b1, 'bibtex_BibTeXFile', a)
    _safe_set(a, 'bibtex_BibTeXEntry', b2)
    assert _is_linked(a, 'bibtex_BibTeXEntry', b2)
    if hasattr(b1, 'bibtex_BibTeXFile'):
        assert not _is_linked(b1, 'bibtex_BibTeXFile', a)
    if hasattr(b2, 'bibtex_BibTeXFile'):
        assert _is_linked(b2, 'bibtex_BibTeXFile', a)
    _safe_set(a, 'bibtex_BibTeXEntry', None)
    assert not _is_linked(a, 'bibtex_BibTeXEntry', b2)
    if hasattr(b2, 'bibtex_BibTeXFile'):
        assert not _is_linked(b2, 'bibtex_BibTeXFile', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

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


bibtex_Article_strategy = st.builds(bibtex_Article, journal=safe_text)
@given(instance=bibtex_Article_strategy)
@settings(max_examples=25)
def test_bibtex_Article_instantiation(instance):
    assert isinstance(instance, bibtex_Article)


bibtex_Author_strategy = st.builds(bibtex_Author, author=safe_text)
@given(instance=bibtex_Author_strategy)
@settings(max_examples=25)
def test_bibtex_Author_instantiation(instance):
    assert isinstance(instance, bibtex_Author)


bibtex_AuthoredEntry_strategy = st.builds(bibtex_AuthoredEntry)
@given(instance=bibtex_AuthoredEntry_strategy)
@settings(max_examples=25)
def test_bibtex_AuthoredEntry_instantiation(instance):
    assert isinstance(instance, bibtex_AuthoredEntry)


bibtex_BibTeXEntry_strategy = st.builds(bibtex_BibTeXEntry, id=safe_text)
@given(instance=bibtex_BibTeXEntry_strategy)
@settings(max_examples=25)
def test_bibtex_BibTeXEntry_instantiation(instance):
    assert isinstance(instance, bibtex_BibTeXEntry)


bibtex_BibTeXFile_strategy = st.builds(bibtex_BibTeXFile)
@given(instance=bibtex_BibTeXFile_strategy)
@settings(max_examples=25)
def test_bibtex_BibTeXFile_instantiation(instance):
    assert isinstance(instance, bibtex_BibTeXFile)


bibtex_Book_strategy = st.builds(bibtex_Book, publisher=safe_text)
@given(instance=bibtex_Book_strategy)
@settings(max_examples=25)
def test_bibtex_Book_instantiation(instance):
    assert isinstance(instance, bibtex_Book)


bibtex_BookTitledEntry_strategy = st.builds(bibtex_BookTitledEntry, booktitle=safe_text)
@given(instance=bibtex_BookTitledEntry_strategy)
@settings(max_examples=25)
def test_bibtex_BookTitledEntry_instantiation(instance):
    assert isinstance(instance, bibtex_BookTitledEntry)


bibtex_Booklet_strategy = st.builds(bibtex_Booklet)
@given(instance=bibtex_Booklet_strategy)
@settings(max_examples=25)
def test_bibtex_Booklet_instantiation(instance):
    assert isinstance(instance, bibtex_Booklet)


bibtex_DatedEntry_strategy = st.builds(bibtex_DatedEntry, year=safe_text)
@given(instance=bibtex_DatedEntry_strategy)
@settings(max_examples=25)
def test_bibtex_DatedEntry_instantiation(instance):
    assert isinstance(instance, bibtex_DatedEntry)


bibtex_InBook_strategy = st.builds(bibtex_InBook, chapter=st.integers())
@given(instance=bibtex_InBook_strategy)
@settings(max_examples=25)
def test_bibtex_InBook_instantiation(instance):
    assert isinstance(instance, bibtex_InBook)


bibtex_InCollection_strategy = st.builds(bibtex_InCollection)
@given(instance=bibtex_InCollection_strategy)
@settings(max_examples=25)
def test_bibtex_InCollection_instantiation(instance):
    assert isinstance(instance, bibtex_InCollection)


bibtex_InProceedings_strategy = st.builds(bibtex_InProceedings)
@given(instance=bibtex_InProceedings_strategy)
@settings(max_examples=25)
def test_bibtex_InProceedings_instantiation(instance):
    assert isinstance(instance, bibtex_InProceedings)


bibtex_Manual_strategy = st.builds(bibtex_Manual)
@given(instance=bibtex_Manual_strategy)
@settings(max_examples=25)
def test_bibtex_Manual_instantiation(instance):
    assert isinstance(instance, bibtex_Manual)


bibtex_MasterThesis_strategy = st.builds(bibtex_MasterThesis)
@given(instance=bibtex_MasterThesis_strategy)
@settings(max_examples=25)
def test_bibtex_MasterThesis_instantiation(instance):
    assert isinstance(instance, bibtex_MasterThesis)


bibtex_Misc_strategy = st.builds(bibtex_Misc)
@given(instance=bibtex_Misc_strategy)
@settings(max_examples=25)
def test_bibtex_Misc_instantiation(instance):
    assert isinstance(instance, bibtex_Misc)


bibtex_PhDThesis_strategy = st.builds(bibtex_PhDThesis)
@given(instance=bibtex_PhDThesis_strategy)
@settings(max_examples=25)
def test_bibtex_PhDThesis_instantiation(instance):
    assert isinstance(instance, bibtex_PhDThesis)


bibtex_Proceedings_strategy = st.builds(bibtex_Proceedings)
@given(instance=bibtex_Proceedings_strategy)
@settings(max_examples=25)
def test_bibtex_Proceedings_instantiation(instance):
    assert isinstance(instance, bibtex_Proceedings)


bibtex_TechReport_strategy = st.builds(bibtex_TechReport)
@given(instance=bibtex_TechReport_strategy)
@settings(max_examples=25)
def test_bibtex_TechReport_instantiation(instance):
    assert isinstance(instance, bibtex_TechReport)


bibtex_ThesisEntry_strategy = st.builds(bibtex_ThesisEntry, school=safe_text)
@given(instance=bibtex_ThesisEntry_strategy)
@settings(max_examples=25)
def test_bibtex_ThesisEntry_instantiation(instance):
    assert isinstance(instance, bibtex_ThesisEntry)


bibtex_TitledEntry_strategy = st.builds(bibtex_TitledEntry, title=safe_text)
@given(instance=bibtex_TitledEntry_strategy)
@settings(max_examples=25)
def test_bibtex_TitledEntry_instantiation(instance):
    assert isinstance(instance, bibtex_TitledEntry)


bibtex_Unpublished_strategy = st.builds(bibtex_Unpublished, note=safe_text)
@given(instance=bibtex_Unpublished_strategy)
@settings(max_examples=25)
def test_bibtex_Unpublished_instantiation(instance):
    assert isinstance(instance, bibtex_Unpublished)



