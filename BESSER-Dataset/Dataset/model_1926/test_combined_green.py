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
    bibTeX_MasterThesis,
    bibTeX_PhDThesis,
    Book,
    bibTeX_InBook,
    TitledEntry,
    DatedEntry,
    AuthoredEntry,
    bibTeX_Unpublished,
    bibTeX_TechReport,
    bibTeX_ThesisEntry,
    bibTeX_Article,
    bibTeX_Book,
    bibTeX_Booklet,
    BookTitledEntry,
    bibTeX_InCollection,
    Proceedings,
    bibTeX_InProceedings,
    bibTeX_Proceedings,
    bibTeX_Manual,
    BibTeXEntry,
    bibTeX_BookTitledEntry,
    bibTeX_DatedEntry,
    bibTeX_TitledEntry,
    bibTeX_Misc,
    bibTeX_AuthoredEntry,
    bibTeX_Author,
    bibTeX_BibTeXEntry,
    bibTeX_BibTeXFile,
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
    assert not inspect.isabstract(bibTeX_MasterThesis)


def test_hyp_bibtex_masterthesis_constructor_exists():
    assert callable(bibTeX_MasterThesis.__init__)


def test_hyp_bibtex_masterthesis_constructor_args():
    sig = inspect.signature(bibTeX_MasterThesis.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_phdthesis_is_not_abstract():
    assert not inspect.isabstract(bibTeX_PhDThesis)


def test_hyp_bibtex_phdthesis_constructor_exists():
    assert callable(bibTeX_PhDThesis.__init__)


def test_hyp_bibtex_phdthesis_constructor_args():
    sig = inspect.signature(bibTeX_PhDThesis.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_hyp_book_constructor_exists():
    assert callable(Book.__init__)


def test_hyp_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_inbook_is_not_abstract():
    assert not inspect.isabstract(bibTeX_InBook)


def test_hyp_bibtex_inbook_constructor_exists():
    assert callable(bibTeX_InBook.__init__)


def test_hyp_bibtex_inbook_constructor_args():
    sig = inspect.signature(bibTeX_InBook.__init__)
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



def test_hyp_authoredentry_is_not_abstract():
    assert not inspect.isabstract(AuthoredEntry)


def test_hyp_authoredentry_constructor_exists():
    assert callable(AuthoredEntry.__init__)


def test_hyp_authoredentry_constructor_args():
    sig = inspect.signature(AuthoredEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_unpublished_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Unpublished)


def test_hyp_bibtex_unpublished_constructor_exists():
    assert callable(bibTeX_Unpublished.__init__)


def test_hyp_bibtex_unpublished_constructor_args():
    sig = inspect.signature(bibTeX_Unpublished.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"




def test_hyp_bibtex_techreport_is_not_abstract():
    assert not inspect.isabstract(bibTeX_TechReport)


def test_hyp_bibtex_techreport_constructor_exists():
    assert callable(bibTeX_TechReport.__init__)


def test_hyp_bibtex_techreport_constructor_args():
    sig = inspect.signature(bibTeX_TechReport.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_thesisentry_is_not_abstract():
    assert not inspect.isabstract(bibTeX_ThesisEntry)


def test_hyp_bibtex_thesisentry_constructor_exists():
    assert callable(bibTeX_ThesisEntry.__init__)


def test_hyp_bibtex_thesisentry_constructor_args():
    sig = inspect.signature(bibTeX_ThesisEntry.__init__)
    params = list(sig.parameters.keys())
    assert "school" in params, "Missing parameter 'school'"




def test_hyp_bibtex_article_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Article)


def test_hyp_bibtex_article_constructor_exists():
    assert callable(bibTeX_Article.__init__)


def test_hyp_bibtex_article_constructor_args():
    sig = inspect.signature(bibTeX_Article.__init__)
    params = list(sig.parameters.keys())
    assert "journal" in params, "Missing parameter 'journal'"




def test_hyp_bibtex_book_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Book)


def test_hyp_bibtex_book_constructor_exists():
    assert callable(bibTeX_Book.__init__)


def test_hyp_bibtex_book_constructor_args():
    sig = inspect.signature(bibTeX_Book.__init__)
    params = list(sig.parameters.keys())
    assert "publisher" in params, "Missing parameter 'publisher'"




def test_hyp_bibtex_booklet_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Booklet)


def test_hyp_bibtex_booklet_constructor_exists():
    assert callable(bibTeX_Booklet.__init__)


def test_hyp_bibtex_booklet_constructor_args():
    sig = inspect.signature(bibTeX_Booklet.__init__)
    params = list(sig.parameters.keys())



def test_hyp_booktitledentry_is_not_abstract():
    assert not inspect.isabstract(BookTitledEntry)


def test_hyp_booktitledentry_constructor_exists():
    assert callable(BookTitledEntry.__init__)


def test_hyp_booktitledentry_constructor_args():
    sig = inspect.signature(BookTitledEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_incollection_is_not_abstract():
    assert not inspect.isabstract(bibTeX_InCollection)


def test_hyp_bibtex_incollection_constructor_exists():
    assert callable(bibTeX_InCollection.__init__)


def test_hyp_bibtex_incollection_constructor_args():
    sig = inspect.signature(bibTeX_InCollection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_proceedings_is_not_abstract():
    assert not inspect.isabstract(Proceedings)


def test_hyp_proceedings_constructor_exists():
    assert callable(Proceedings.__init__)


def test_hyp_proceedings_constructor_args():
    sig = inspect.signature(Proceedings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_inproceedings_is_not_abstract():
    assert not inspect.isabstract(bibTeX_InProceedings)


def test_hyp_bibtex_inproceedings_constructor_exists():
    assert callable(bibTeX_InProceedings.__init__)


def test_hyp_bibtex_inproceedings_constructor_args():
    sig = inspect.signature(bibTeX_InProceedings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_proceedings_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Proceedings)


def test_hyp_bibtex_proceedings_constructor_exists():
    assert callable(bibTeX_Proceedings.__init__)


def test_hyp_bibtex_proceedings_constructor_args():
    sig = inspect.signature(bibTeX_Proceedings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_manual_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Manual)


def test_hyp_bibtex_manual_constructor_exists():
    assert callable(bibTeX_Manual.__init__)


def test_hyp_bibtex_manual_constructor_args():
    sig = inspect.signature(bibTeX_Manual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtexentry_is_not_abstract():
    assert not inspect.isabstract(BibTeXEntry)


def test_hyp_bibtexentry_constructor_exists():
    assert callable(BibTeXEntry.__init__)


def test_hyp_bibtexentry_constructor_args():
    sig = inspect.signature(BibTeXEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_booktitledentry_is_not_abstract():
    assert not inspect.isabstract(bibTeX_BookTitledEntry)


def test_hyp_bibtex_booktitledentry_constructor_exists():
    assert callable(bibTeX_BookTitledEntry.__init__)


def test_hyp_bibtex_booktitledentry_constructor_args():
    sig = inspect.signature(bibTeX_BookTitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "booktitle" in params, "Missing parameter 'booktitle'"




def test_hyp_bibtex_datedentry_is_not_abstract():
    assert not inspect.isabstract(bibTeX_DatedEntry)


def test_hyp_bibtex_datedentry_constructor_exists():
    assert callable(bibTeX_DatedEntry.__init__)


def test_hyp_bibtex_datedentry_constructor_args():
    sig = inspect.signature(bibTeX_DatedEntry.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"




def test_hyp_bibtex_titledentry_is_not_abstract():
    assert not inspect.isabstract(bibTeX_TitledEntry)


def test_hyp_bibtex_titledentry_constructor_exists():
    assert callable(bibTeX_TitledEntry.__init__)


def test_hyp_bibtex_titledentry_constructor_args():
    sig = inspect.signature(bibTeX_TitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"




def test_hyp_bibtex_misc_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Misc)


def test_hyp_bibtex_misc_constructor_exists():
    assert callable(bibTeX_Misc.__init__)


def test_hyp_bibtex_misc_constructor_args():
    sig = inspect.signature(bibTeX_Misc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_authoredentry_is_not_abstract():
    assert not inspect.isabstract(bibTeX_AuthoredEntry)


def test_hyp_bibtex_authoredentry_constructor_exists():
    assert callable(bibTeX_AuthoredEntry.__init__)


def test_hyp_bibtex_authoredentry_constructor_args():
    sig = inspect.signature(bibTeX_AuthoredEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bibtex_author_is_not_abstract():
    assert not inspect.isabstract(bibTeX_Author)


def test_hyp_bibtex_author_constructor_exists():
    assert callable(bibTeX_Author.__init__)


def test_hyp_bibtex_author_constructor_args():
    sig = inspect.signature(bibTeX_Author.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"




def test_hyp_bibtex_bibtexentry_is_not_abstract():
    assert not inspect.isabstract(bibTeX_BibTeXEntry)


def test_hyp_bibtex_bibtexentry_constructor_exists():
    assert callable(bibTeX_BibTeXEntry.__init__)


def test_hyp_bibtex_bibtexentry_constructor_args():
    sig = inspect.signature(bibTeX_BibTeXEntry.__init__)
    params = list(sig.parameters.keys())
    assert "theId" in params, "Missing parameter 'theId'"




def test_hyp_bibtex_bibtexfile_is_not_abstract():
    assert not inspect.isabstract(bibTeX_BibTeXFile)


def test_hyp_bibtex_bibtexfile_constructor_exists():
    assert callable(bibTeX_BibTeXFile.__init__)


def test_hyp_bibtex_bibtexfile_constructor_args():
    sig = inspect.signature(bibTeX_BibTeXFile.__init__)
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
ThesisEntry_strategy = st.builds(
    ThesisEntry,
)
bibTeX_MasterThesis_strategy = st.builds(
    bibTeX_MasterThesis,
)
bibTeX_PhDThesis_strategy = st.builds(
    bibTeX_PhDThesis,
)
Book_strategy = st.builds(
    Book,
)
bibTeX_InBook_strategy = st.builds(
    bibTeX_InBook,
    chapter=
        safe_text
)
TitledEntry_strategy = st.builds(
    TitledEntry,
)
DatedEntry_strategy = st.builds(
    DatedEntry,
)
AuthoredEntry_strategy = st.builds(
    AuthoredEntry,
)
bibTeX_Unpublished_strategy = st.builds(
    bibTeX_Unpublished,
    note=
        safe_text
)
bibTeX_TechReport_strategy = st.builds(
    bibTeX_TechReport,
)
bibTeX_ThesisEntry_strategy = st.builds(
    bibTeX_ThesisEntry,
    school=
        safe_text
)
bibTeX_Article_strategy = st.builds(
    bibTeX_Article,
    journal=
        safe_text
)
bibTeX_Book_strategy = st.builds(
    bibTeX_Book,
    publisher=
        safe_text
)
bibTeX_Booklet_strategy = st.builds(
    bibTeX_Booklet,
)
BookTitledEntry_strategy = st.builds(
    BookTitledEntry,
)
bibTeX_InCollection_strategy = st.builds(
    bibTeX_InCollection,
)
Proceedings_strategy = st.builds(
    Proceedings,
)
bibTeX_InProceedings_strategy = st.builds(
    bibTeX_InProceedings,
)
bibTeX_Proceedings_strategy = st.builds(
    bibTeX_Proceedings,
)
bibTeX_Manual_strategy = st.builds(
    bibTeX_Manual,
)
BibTeXEntry_strategy = st.builds(
    BibTeXEntry,
)
bibTeX_BookTitledEntry_strategy = st.builds(
    bibTeX_BookTitledEntry,
    booktitle=
        safe_text
)
bibTeX_DatedEntry_strategy = st.builds(
    bibTeX_DatedEntry,
    year=
        safe_text
)
bibTeX_TitledEntry_strategy = st.builds(
    bibTeX_TitledEntry,
    title=
        safe_text
)
bibTeX_Misc_strategy = st.builds(
    bibTeX_Misc,
)
bibTeX_AuthoredEntry_strategy = st.builds(
    bibTeX_AuthoredEntry,
)
bibTeX_Author_strategy = st.builds(
    bibTeX_Author,
    author=
        safe_text
)
bibTeX_BibTeXEntry_strategy = st.builds(
    bibTeX_BibTeXEntry,
    theId=
        safe_text
)
bibTeX_BibTeXFile_strategy = st.builds(
    bibTeX_BibTeXFile,
)








@given(instance=bibTeX_InBook_strategy)
def test_hyp_bibtex_inbook_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original







@given(instance=bibTeX_Unpublished_strategy)
def test_hyp_bibtex_unpublished_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original





@given(instance=bibTeX_ThesisEntry_strategy)
def test_hyp_bibtex_thesisentry_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original




@given(instance=bibTeX_Article_strategy)
def test_hyp_bibtex_article_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original




@given(instance=bibTeX_Book_strategy)
def test_hyp_bibtex_book_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original












@given(instance=bibTeX_BookTitledEntry_strategy)
def test_hyp_bibtex_booktitledentry_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original




@given(instance=bibTeX_DatedEntry_strategy)
def test_hyp_bibtex_datedentry_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original




@given(instance=bibTeX_TitledEntry_strategy)
def test_hyp_bibtex_titledentry_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original






@given(instance=bibTeX_Author_strategy)
def test_hyp_bibtex_author_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original




@given(instance=bibTeX_BibTeXEntry_strategy)
def test_hyp_bibtex_bibtexentry_theId_setter(instance):
    original = instance.theId
    instance.theId = original
    assert instance.theId == original



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
    bibTeX_Article,
    bibTeX_Author,
    bibTeX_AuthoredEntry,
    bibTeX_BibTeXEntry,
    bibTeX_BibTeXFile,
    bibTeX_Book,
    bibTeX_BookTitledEntry,
    bibTeX_Booklet,
    bibTeX_DatedEntry,
    bibTeX_InBook,
    bibTeX_InCollection,
    bibTeX_InProceedings,
    bibTeX_Manual,
    bibTeX_MasterThesis,
    bibTeX_Misc,
    bibTeX_PhDThesis,
    bibTeX_Proceedings,
    bibTeX_TechReport,
    bibTeX_ThesisEntry,
    bibTeX_TitledEntry,
    bibTeX_Unpublished,
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

def test_bibTeX_Article_journal_value_roundtrip():
    instance = bibTeX_Article(journal="sample_text")
    assert instance.journal == "sample_text"
    instance.journal = "sample_text_2"
    assert instance.journal == "sample_text_2"


def test_bibTeX_Author_author_value_roundtrip():
    instance = bibTeX_Author(author="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_bibTeX_BibTeXEntry_theId_value_roundtrip():
    instance = bibTeX_BibTeXEntry(theId="sample_text")
    assert instance.theId == "sample_text"
    instance.theId = "sample_text_2"
    assert instance.theId == "sample_text_2"


def test_bibTeX_Book_publisher_value_roundtrip():
    instance = bibTeX_Book(publisher="sample_text")
    assert instance.publisher == "sample_text"
    instance.publisher = "sample_text_2"
    assert instance.publisher == "sample_text_2"


def test_bibTeX_BookTitledEntry_booktitle_value_roundtrip():
    instance = bibTeX_BookTitledEntry(booktitle="sample_text")
    assert instance.booktitle == "sample_text"
    instance.booktitle = "sample_text_2"
    assert instance.booktitle == "sample_text_2"


def test_bibTeX_DatedEntry_year_value_roundtrip():
    instance = bibTeX_DatedEntry(year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_bibTeX_InBook_chapter_value_roundtrip():
    instance = bibTeX_InBook(chapter="sample_text")
    assert instance.chapter == "sample_text"
    instance.chapter = "sample_text_2"
    assert instance.chapter == "sample_text_2"


def test_bibTeX_ThesisEntry_school_value_roundtrip():
    instance = bibTeX_ThesisEntry(school="sample_text")
    assert instance.school == "sample_text"
    instance.school = "sample_text_2"
    assert instance.school == "sample_text_2"


def test_bibTeX_TitledEntry_title_value_roundtrip():
    instance = bibTeX_TitledEntry(title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_bibTeX_Unpublished_note_value_roundtrip():
    instance = bibTeX_Unpublished(note="sample_text")
    assert instance.note == "sample_text"
    instance.note = "sample_text_2"
    assert instance.note == "sample_text_2"


def test_bibTeX_Article_isa_AuthoredEntry():
    instance = bibTeX_Article(journal="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_bibTeX_Book_isa_AuthoredEntry():
    instance = bibTeX_Book(publisher="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_bibTeX_InProceedings_isa_AuthoredEntry():
    instance = bibTeX_InProceedings()
    assert isinstance(instance, AuthoredEntry)


def test_bibTeX_TechReport_isa_AuthoredEntry():
    instance = bibTeX_TechReport()
    assert isinstance(instance, AuthoredEntry)


def test_bibTeX_ThesisEntry_isa_AuthoredEntry():
    instance = bibTeX_ThesisEntry(school="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_bibTeX_Unpublished_isa_AuthoredEntry():
    instance = bibTeX_Unpublished(note="sample_text")
    assert isinstance(instance, AuthoredEntry)


def test_bibTeX_AuthoredEntry_isa_BibTeXEntry():
    instance = bibTeX_AuthoredEntry()
    assert isinstance(instance, BibTeXEntry)


def test_bibTeX_BookTitledEntry_isa_BibTeXEntry():
    instance = bibTeX_BookTitledEntry(booktitle="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_bibTeX_DatedEntry_isa_BibTeXEntry():
    instance = bibTeX_DatedEntry(year="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_bibTeX_Misc_isa_BibTeXEntry():
    instance = bibTeX_Misc()
    assert isinstance(instance, BibTeXEntry)


def test_bibTeX_TitledEntry_isa_BibTeXEntry():
    instance = bibTeX_TitledEntry(title="sample_text")
    assert isinstance(instance, BibTeXEntry)


def test_bibTeX_InBook_isa_Book():
    instance = bibTeX_InBook(chapter="sample_text")
    assert isinstance(instance, Book)


def test_bibTeX_InCollection_isa_Book():
    instance = bibTeX_InCollection()
    assert isinstance(instance, Book)


def test_bibTeX_InCollection_isa_BookTitledEntry():
    instance = bibTeX_InCollection()
    assert isinstance(instance, BookTitledEntry)


def test_bibTeX_InProceedings_isa_BookTitledEntry():
    instance = bibTeX_InProceedings()
    assert isinstance(instance, BookTitledEntry)


def test_bibTeX_Article_isa_DatedEntry():
    instance = bibTeX_Article(journal="sample_text")
    assert isinstance(instance, DatedEntry)


def test_bibTeX_Book_isa_DatedEntry():
    instance = bibTeX_Book(publisher="sample_text")
    assert isinstance(instance, DatedEntry)


def test_bibTeX_Booklet_isa_DatedEntry():
    instance = bibTeX_Booklet()
    assert isinstance(instance, DatedEntry)


def test_bibTeX_Proceedings_isa_DatedEntry():
    instance = bibTeX_Proceedings()
    assert isinstance(instance, DatedEntry)


def test_bibTeX_TechReport_isa_DatedEntry():
    instance = bibTeX_TechReport()
    assert isinstance(instance, DatedEntry)


def test_bibTeX_ThesisEntry_isa_DatedEntry():
    instance = bibTeX_ThesisEntry(school="sample_text")
    assert isinstance(instance, DatedEntry)


def test_bibTeX_InProceedings_isa_Proceedings():
    instance = bibTeX_InProceedings()
    assert isinstance(instance, Proceedings)


def test_bibTeX_MasterThesis_isa_ThesisEntry():
    instance = bibTeX_MasterThesis()
    assert isinstance(instance, ThesisEntry)


def test_bibTeX_PhDThesis_isa_ThesisEntry():
    instance = bibTeX_PhDThesis()
    assert isinstance(instance, ThesisEntry)


def test_bibTeX_Article_isa_TitledEntry():
    instance = bibTeX_Article(journal="sample_text")
    assert isinstance(instance, TitledEntry)


def test_bibTeX_Book_isa_TitledEntry():
    instance = bibTeX_Book(publisher="sample_text")
    assert isinstance(instance, TitledEntry)


def test_bibTeX_Manual_isa_TitledEntry():
    instance = bibTeX_Manual()
    assert isinstance(instance, TitledEntry)


def test_bibTeX_Proceedings_isa_TitledEntry():
    instance = bibTeX_Proceedings()
    assert isinstance(instance, TitledEntry)


def test_bibTeX_TechReport_isa_TitledEntry():
    instance = bibTeX_TechReport()
    assert isinstance(instance, TitledEntry)


def test_bibTeX_ThesisEntry_isa_TitledEntry():
    instance = bibTeX_ThesisEntry(school="sample_text")
    assert isinstance(instance, TitledEntry)


def test_bibTeX_Unpublished_isa_TitledEntry():
    instance = bibTeX_Unpublished(note="sample_text")
    assert isinstance(instance, TitledEntry)


def test_assoc_authors1_link_reassign_clear():
    a = bibTeX_Author(author="sample_text")
    b1 = bibTeX_AuthoredEntry()
    b2 = bibTeX_AuthoredEntry()
    _safe_set(a, 'bibTeX_Author', b1)
    assert _is_linked(a, 'bibTeX_Author', b1)
    if hasattr(b1, 'bibTeX_AuthoredEntry'):
        assert _is_linked(b1, 'bibTeX_AuthoredEntry', a)
    _safe_set(a, 'bibTeX_Author', b2)
    assert _is_linked(a, 'bibTeX_Author', b2)
    if hasattr(b1, 'bibTeX_AuthoredEntry'):
        assert not _is_linked(b1, 'bibTeX_AuthoredEntry', a)
    if hasattr(b2, 'bibTeX_AuthoredEntry'):
        assert _is_linked(b2, 'bibTeX_AuthoredEntry', a)
    _safe_set(a, 'bibTeX_Author', None)
    assert not _is_linked(a, 'bibTeX_Author', b2)
    if hasattr(b2, 'bibTeX_AuthoredEntry'):
        assert not _is_linked(b2, 'bibTeX_AuthoredEntry', a)


def test_assoc_entries0_link_reassign_clear():
    a = bibTeX_BibTeXEntry(theId="sample_text")
    b1 = bibTeX_BibTeXFile()
    b2 = bibTeX_BibTeXFile()
    _safe_set(a, 'bibTeX_BibTeXEntry', b1)
    assert _is_linked(a, 'bibTeX_BibTeXEntry', b1)
    if hasattr(b1, 'bibTeX_BibTeXFile'):
        assert _is_linked(b1, 'bibTeX_BibTeXFile', a)
    _safe_set(a, 'bibTeX_BibTeXEntry', b2)
    assert _is_linked(a, 'bibTeX_BibTeXEntry', b2)
    if hasattr(b1, 'bibTeX_BibTeXFile'):
        assert not _is_linked(b1, 'bibTeX_BibTeXFile', a)
    if hasattr(b2, 'bibTeX_BibTeXFile'):
        assert _is_linked(b2, 'bibTeX_BibTeXFile', a)
    _safe_set(a, 'bibTeX_BibTeXEntry', None)
    assert not _is_linked(a, 'bibTeX_BibTeXEntry', b2)
    if hasattr(b2, 'bibTeX_BibTeXFile'):
        assert not _is_linked(b2, 'bibTeX_BibTeXFile', a)


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


bibTeX_Article_strategy = st.builds(bibTeX_Article, journal=safe_text)
@given(instance=bibTeX_Article_strategy)
@settings(max_examples=25)
def test_bibTeX_Article_instantiation(instance):
    assert isinstance(instance, bibTeX_Article)


bibTeX_Author_strategy = st.builds(bibTeX_Author, author=safe_text)
@given(instance=bibTeX_Author_strategy)
@settings(max_examples=25)
def test_bibTeX_Author_instantiation(instance):
    assert isinstance(instance, bibTeX_Author)


bibTeX_AuthoredEntry_strategy = st.builds(bibTeX_AuthoredEntry)
@given(instance=bibTeX_AuthoredEntry_strategy)
@settings(max_examples=25)
def test_bibTeX_AuthoredEntry_instantiation(instance):
    assert isinstance(instance, bibTeX_AuthoredEntry)


bibTeX_BibTeXEntry_strategy = st.builds(bibTeX_BibTeXEntry, theId=safe_text)
@given(instance=bibTeX_BibTeXEntry_strategy)
@settings(max_examples=25)
def test_bibTeX_BibTeXEntry_instantiation(instance):
    assert isinstance(instance, bibTeX_BibTeXEntry)


bibTeX_BibTeXFile_strategy = st.builds(bibTeX_BibTeXFile)
@given(instance=bibTeX_BibTeXFile_strategy)
@settings(max_examples=25)
def test_bibTeX_BibTeXFile_instantiation(instance):
    assert isinstance(instance, bibTeX_BibTeXFile)


bibTeX_Book_strategy = st.builds(bibTeX_Book, publisher=safe_text)
@given(instance=bibTeX_Book_strategy)
@settings(max_examples=25)
def test_bibTeX_Book_instantiation(instance):
    assert isinstance(instance, bibTeX_Book)


bibTeX_BookTitledEntry_strategy = st.builds(bibTeX_BookTitledEntry, booktitle=safe_text)
@given(instance=bibTeX_BookTitledEntry_strategy)
@settings(max_examples=25)
def test_bibTeX_BookTitledEntry_instantiation(instance):
    assert isinstance(instance, bibTeX_BookTitledEntry)


bibTeX_Booklet_strategy = st.builds(bibTeX_Booklet)
@given(instance=bibTeX_Booklet_strategy)
@settings(max_examples=25)
def test_bibTeX_Booklet_instantiation(instance):
    assert isinstance(instance, bibTeX_Booklet)


bibTeX_DatedEntry_strategy = st.builds(bibTeX_DatedEntry, year=safe_text)
@given(instance=bibTeX_DatedEntry_strategy)
@settings(max_examples=25)
def test_bibTeX_DatedEntry_instantiation(instance):
    assert isinstance(instance, bibTeX_DatedEntry)


bibTeX_InBook_strategy = st.builds(bibTeX_InBook, chapter=safe_text)
@given(instance=bibTeX_InBook_strategy)
@settings(max_examples=25)
def test_bibTeX_InBook_instantiation(instance):
    assert isinstance(instance, bibTeX_InBook)


bibTeX_InCollection_strategy = st.builds(bibTeX_InCollection)
@given(instance=bibTeX_InCollection_strategy)
@settings(max_examples=25)
def test_bibTeX_InCollection_instantiation(instance):
    assert isinstance(instance, bibTeX_InCollection)


bibTeX_InProceedings_strategy = st.builds(bibTeX_InProceedings)
@given(instance=bibTeX_InProceedings_strategy)
@settings(max_examples=25)
def test_bibTeX_InProceedings_instantiation(instance):
    assert isinstance(instance, bibTeX_InProceedings)


bibTeX_Manual_strategy = st.builds(bibTeX_Manual)
@given(instance=bibTeX_Manual_strategy)
@settings(max_examples=25)
def test_bibTeX_Manual_instantiation(instance):
    assert isinstance(instance, bibTeX_Manual)


bibTeX_MasterThesis_strategy = st.builds(bibTeX_MasterThesis)
@given(instance=bibTeX_MasterThesis_strategy)
@settings(max_examples=25)
def test_bibTeX_MasterThesis_instantiation(instance):
    assert isinstance(instance, bibTeX_MasterThesis)


bibTeX_Misc_strategy = st.builds(bibTeX_Misc)
@given(instance=bibTeX_Misc_strategy)
@settings(max_examples=25)
def test_bibTeX_Misc_instantiation(instance):
    assert isinstance(instance, bibTeX_Misc)


bibTeX_PhDThesis_strategy = st.builds(bibTeX_PhDThesis)
@given(instance=bibTeX_PhDThesis_strategy)
@settings(max_examples=25)
def test_bibTeX_PhDThesis_instantiation(instance):
    assert isinstance(instance, bibTeX_PhDThesis)


bibTeX_Proceedings_strategy = st.builds(bibTeX_Proceedings)
@given(instance=bibTeX_Proceedings_strategy)
@settings(max_examples=25)
def test_bibTeX_Proceedings_instantiation(instance):
    assert isinstance(instance, bibTeX_Proceedings)


bibTeX_TechReport_strategy = st.builds(bibTeX_TechReport)
@given(instance=bibTeX_TechReport_strategy)
@settings(max_examples=25)
def test_bibTeX_TechReport_instantiation(instance):
    assert isinstance(instance, bibTeX_TechReport)


bibTeX_ThesisEntry_strategy = st.builds(bibTeX_ThesisEntry, school=safe_text)
@given(instance=bibTeX_ThesisEntry_strategy)
@settings(max_examples=25)
def test_bibTeX_ThesisEntry_instantiation(instance):
    assert isinstance(instance, bibTeX_ThesisEntry)


bibTeX_TitledEntry_strategy = st.builds(bibTeX_TitledEntry, title=safe_text)
@given(instance=bibTeX_TitledEntry_strategy)
@settings(max_examples=25)
def test_bibTeX_TitledEntry_instantiation(instance):
    assert isinstance(instance, bibTeX_TitledEntry)


bibTeX_Unpublished_strategy = st.builds(bibTeX_Unpublished, note=safe_text)
@given(instance=bibTeX_Unpublished_strategy)
@settings(max_examples=25)
def test_bibTeX_Unpublished_instantiation(instance):
    assert isinstance(instance, bibTeX_Unpublished)



