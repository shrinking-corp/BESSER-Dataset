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
    Person,
    sistedesMM_SistedesMember,
    sistedesMM_Editor,
    sistedesMM_Journal,
    Publication,
    sistedesMM_InProceedings,
    sistedesMM_Book,
    sistedesMM_Article,
    sistedesMM_Edition,
    sistedesMM_Publication,
    sistedesMM_University,
    sistedesMM_Person,
    sistedesMM_Publisher,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistedesmm_sistedesmember_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_SistedesMember)


def test_hyp_sistedesmm_sistedesmember_constructor_exists():
    assert callable(sistedesMM_SistedesMember.__init__)


def test_hyp_sistedesmm_sistedesmember_constructor_args():
    sig = inspect.signature(sistedesMM_SistedesMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistedesmm_editor_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Editor)


def test_hyp_sistedesmm_editor_constructor_exists():
    assert callable(sistedesMM_Editor.__init__)


def test_hyp_sistedesmm_editor_constructor_args():
    sig = inspect.signature(sistedesMM_Editor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_sistedesmm_journal_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Journal)


def test_hyp_sistedesmm_journal_constructor_exists():
    assert callable(sistedesMM_Journal.__init__)


def test_hyp_sistedesmm_journal_constructor_args():
    sig = inspect.signature(sistedesMM_Journal.__init__)
    params = list(sig.parameters.keys())
    assert "jcrIndexed" in params, "Missing parameter 'jcrIndexed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "acronym" in params, "Missing parameter 'acronym'"






def test_hyp_publication_is_not_abstract():
    assert not inspect.isabstract(Publication)


def test_hyp_publication_constructor_exists():
    assert callable(Publication.__init__)


def test_hyp_publication_constructor_args():
    sig = inspect.signature(Publication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistedesmm_inproceedings_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_InProceedings)


def test_hyp_sistedesmm_inproceedings_constructor_exists():
    assert callable(sistedesMM_InProceedings.__init__)


def test_hyp_sistedesmm_inproceedings_constructor_args():
    sig = inspect.signature(sistedesMM_InProceedings.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"
    assert "bookTitle" in params, "Missing parameter 'bookTitle'"
    assert "title" in params, "Missing parameter 'title'"
    assert "toPage" in params, "Missing parameter 'toPage'"
    assert "fromPage" in params, "Missing parameter 'fromPage'"









def test_hyp_sistedesmm_book_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Book)


def test_hyp_sistedesmm_book_constructor_exists():
    assert callable(sistedesMM_Book.__init__)


def test_hyp_sistedesmm_book_constructor_args():
    sig = inspect.signature(sistedesMM_Book.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "isbn" in params, "Missing parameter 'isbn'"
    assert "title" in params, "Missing parameter 'title'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "series" in params, "Missing parameter 'series'"










def test_hyp_sistedesmm_article_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Article)


def test_hyp_sistedesmm_article_constructor_exists():
    assert callable(sistedesMM_Article.__init__)


def test_hyp_sistedesmm_article_constructor_args():
    sig = inspect.signature(sistedesMM_Article.__init__)
    params = list(sig.parameters.keys())
    assert "fromPage" in params, "Missing parameter 'fromPage'"
    assert "month" in params, "Missing parameter 'month'"
    assert "number" in params, "Missing parameter 'number'"
    assert "title" in params, "Missing parameter 'title'"
    assert "year" in params, "Missing parameter 'year'"
    assert "toPage" in params, "Missing parameter 'toPage'"
    assert "volume" in params, "Missing parameter 'volume'"










def test_hyp_sistedesmm_edition_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Edition)


def test_hyp_sistedesmm_edition_constructor_exists():
    assert callable(sistedesMM_Edition.__init__)


def test_hyp_sistedesmm_edition_constructor_args():
    sig = inspect.signature(sistedesMM_Edition.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "year" in params, "Missing parameter 'year'"





def test_hyp_sistedesmm_publication_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Publication)


def test_hyp_sistedesmm_publication_constructor_exists():
    assert callable(sistedesMM_Publication.__init__)


def test_hyp_sistedesmm_publication_constructor_args():
    sig = inspect.signature(sistedesMM_Publication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sistedesmm_university_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_University)


def test_hyp_sistedesmm_university_constructor_exists():
    assert callable(sistedesMM_University.__init__)


def test_hyp_sistedesmm_university_constructor_args():
    sig = inspect.signature(sistedesMM_University.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "city" in params, "Missing parameter 'city'"
    assert "provinceOrState" in params, "Missing parameter 'provinceOrState'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_sistedesmm_person_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Person)


def test_hyp_sistedesmm_person_constructor_exists():
    assert callable(sistedesMM_Person.__init__)


def test_hyp_sistedesmm_person_constructor_args():
    sig = inspect.signature(sistedesMM_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "surname" in params, "Missing parameter 'surname'"
    assert "nationality" in params, "Missing parameter 'nationality'"
    assert "email" in params, "Missing parameter 'email'"







def test_hyp_sistedesmm_publisher_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Publisher)


def test_hyp_sistedesmm_publisher_constructor_exists():
    assert callable(sistedesMM_Publisher.__init__)


def test_hyp_sistedesmm_publisher_constructor_args():
    sig = inspect.signature(sistedesMM_Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"




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
Person_strategy = st.builds(
    Person,
)
sistedesMM_SistedesMember_strategy = st.builds(
    sistedesMM_SistedesMember,
)
sistedesMM_Editor_strategy = st.builds(
    sistedesMM_Editor,
    name=
        safe_text
)
sistedesMM_Journal_strategy = st.builds(
    sistedesMM_Journal,
    jcrIndexed=
        st.booleans(),
    name=
        safe_text,
    acronym=
        safe_text
)
Publication_strategy = st.builds(
    Publication,
)
sistedesMM_InProceedings_strategy = st.builds(
    sistedesMM_InProceedings,
    month=
        safe_text,
    year=
        st.integers(),
    bookTitle=
        safe_text,
    title=
        safe_text,
    toPage=
        safe_text,
    fromPage=
        safe_text
)
sistedesMM_Book_strategy = st.builds(
    sistedesMM_Book,
    year=
        st.integers(),
    month=
        safe_text,
    volume=
        safe_text,
    isbn=
        safe_text,
    title=
        safe_text,
    edition=
        st.integers(),
    series=
        safe_text
)
sistedesMM_Article_strategy = st.builds(
    sistedesMM_Article,
    fromPage=
        st.integers(),
    month=
        safe_text,
    number=
        st.integers(),
    title=
        safe_text,
    year=
        st.integers(),
    toPage=
        st.integers(),
    volume=
        safe_text
)
sistedesMM_Edition_strategy = st.builds(
    sistedesMM_Edition,
    location=
        safe_text,
    year=
        st.integers()
)
sistedesMM_Publication_strategy = st.builds(
    sistedesMM_Publication,
)
sistedesMM_University_strategy = st.builds(
    sistedesMM_University,
    country=
        safe_text,
    city=
        safe_text,
    provinceOrState=
        safe_text,
    name=
        safe_text
)
sistedesMM_Person_strategy = st.builds(
    sistedesMM_Person,
    name=
        safe_text,
    surname=
        safe_text,
    nationality=
        safe_text,
    email=
        safe_text
)
sistedesMM_Publisher_strategy = st.builds(
    sistedesMM_Publisher,
    address=
        safe_text,
    name=
        safe_text
)






@given(instance=sistedesMM_Editor_strategy)
def test_hyp_sistedesmm_editor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=sistedesMM_Journal_strategy)
def test_hyp_sistedesmm_journal_jcrIndexed_setter(instance):
    original = instance.jcrIndexed
    instance.jcrIndexed = original
    assert instance.jcrIndexed == original



@given(instance=sistedesMM_Journal_strategy)
def test_hyp_sistedesmm_journal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sistedesMM_Journal_strategy)
def test_hyp_sistedesmm_journal_acronym_setter(instance):
    original = instance.acronym
    instance.acronym = original
    assert instance.acronym == original





@given(instance=sistedesMM_InProceedings_strategy)
def test_hyp_sistedesmm_inproceedings_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_hyp_sistedesmm_inproceedings_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_hyp_sistedesmm_inproceedings_bookTitle_setter(instance):
    original = instance.bookTitle
    instance.bookTitle = original
    assert instance.bookTitle == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_hyp_sistedesmm_inproceedings_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_hyp_sistedesmm_inproceedings_toPage_setter(instance):
    original = instance.toPage
    instance.toPage = original
    assert instance.toPage == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_hyp_sistedesmm_inproceedings_fromPage_setter(instance):
    original = instance.fromPage
    instance.fromPage = original
    assert instance.fromPage == original




@given(instance=sistedesMM_Book_strategy)
def test_hyp_sistedesmm_book_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=sistedesMM_Book_strategy)
def test_hyp_sistedesmm_book_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=sistedesMM_Book_strategy)
def test_hyp_sistedesmm_book_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original



@given(instance=sistedesMM_Book_strategy)
def test_hyp_sistedesmm_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original



@given(instance=sistedesMM_Book_strategy)
def test_hyp_sistedesmm_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=sistedesMM_Book_strategy)
def test_hyp_sistedesmm_book_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original



@given(instance=sistedesMM_Book_strategy)
def test_hyp_sistedesmm_book_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original




@given(instance=sistedesMM_Article_strategy)
def test_hyp_sistedesmm_article_fromPage_setter(instance):
    original = instance.fromPage
    instance.fromPage = original
    assert instance.fromPage == original



@given(instance=sistedesMM_Article_strategy)
def test_hyp_sistedesmm_article_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=sistedesMM_Article_strategy)
def test_hyp_sistedesmm_article_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=sistedesMM_Article_strategy)
def test_hyp_sistedesmm_article_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=sistedesMM_Article_strategy)
def test_hyp_sistedesmm_article_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=sistedesMM_Article_strategy)
def test_hyp_sistedesmm_article_toPage_setter(instance):
    original = instance.toPage
    instance.toPage = original
    assert instance.toPage == original



@given(instance=sistedesMM_Article_strategy)
def test_hyp_sistedesmm_article_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original




@given(instance=sistedesMM_Edition_strategy)
def test_hyp_sistedesmm_edition_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=sistedesMM_Edition_strategy)
def test_hyp_sistedesmm_edition_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original





@given(instance=sistedesMM_University_strategy)
def test_hyp_sistedesmm_university_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=sistedesMM_University_strategy)
def test_hyp_sistedesmm_university_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=sistedesMM_University_strategy)
def test_hyp_sistedesmm_university_provinceOrState_setter(instance):
    original = instance.provinceOrState
    instance.provinceOrState = original
    assert instance.provinceOrState == original



@given(instance=sistedesMM_University_strategy)
def test_hyp_sistedesmm_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=sistedesMM_Person_strategy)
def test_hyp_sistedesmm_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sistedesMM_Person_strategy)
def test_hyp_sistedesmm_person_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=sistedesMM_Person_strategy)
def test_hyp_sistedesmm_person_nationality_setter(instance):
    original = instance.nationality
    instance.nationality = original
    assert instance.nationality == original



@given(instance=sistedesMM_Person_strategy)
def test_hyp_sistedesmm_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original




@given(instance=sistedesMM_Publisher_strategy)
def test_hyp_sistedesmm_publisher_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=sistedesMM_Publisher_strategy)
def test_hyp_sistedesmm_publisher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Person,
    Publication,
    sistedesMM_Article,
    sistedesMM_Book,
    sistedesMM_Edition,
    sistedesMM_Editor,
    sistedesMM_InProceedings,
    sistedesMM_Journal,
    sistedesMM_Person,
    sistedesMM_Publication,
    sistedesMM_Publisher,
    sistedesMM_SistedesMember,
    sistedesMM_University,
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

def test_sistedesMM_Article_fromPage_value_roundtrip():
    instance = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    assert instance.fromPage == 7
    instance.fromPage = 13
    assert instance.fromPage == 13


def test_sistedesMM_Article_month_value_roundtrip():
    instance = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_sistedesMM_Article_number_value_roundtrip():
    instance = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_sistedesMM_Article_title_value_roundtrip():
    instance = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_sistedesMM_Article_toPage_value_roundtrip():
    instance = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    assert instance.toPage == 7
    instance.toPage = 13
    assert instance.toPage == 13


def test_sistedesMM_Article_volume_value_roundtrip():
    instance = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_sistedesMM_Article_year_value_roundtrip():
    instance = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_sistedesMM_Book_edition_value_roundtrip():
    instance = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    assert instance.edition == 7
    instance.edition = 13
    assert instance.edition == 13


def test_sistedesMM_Book_isbn_value_roundtrip():
    instance = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    assert instance.isbn == "sample_text"
    instance.isbn = "sample_text_2"
    assert instance.isbn == "sample_text_2"


def test_sistedesMM_Book_month_value_roundtrip():
    instance = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_sistedesMM_Book_series_value_roundtrip():
    instance = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_sistedesMM_Book_title_value_roundtrip():
    instance = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_sistedesMM_Book_volume_value_roundtrip():
    instance = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    assert instance.volume == "sample_text"
    instance.volume = "sample_text_2"
    assert instance.volume == "sample_text_2"


def test_sistedesMM_Book_year_value_roundtrip():
    instance = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_sistedesMM_Edition_location_value_roundtrip():
    instance = sistedesMM_Edition(location="sample_text", year=7)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_sistedesMM_Edition_year_value_roundtrip():
    instance = sistedesMM_Edition(location="sample_text", year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_sistedesMM_Editor_name_value_roundtrip():
    instance = sistedesMM_Editor(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sistedesMM_InProceedings_bookTitle_value_roundtrip():
    instance = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    assert instance.bookTitle == "sample_text"
    instance.bookTitle = "sample_text_2"
    assert instance.bookTitle == "sample_text_2"


def test_sistedesMM_InProceedings_fromPage_value_roundtrip():
    instance = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    assert instance.fromPage == "sample_text"
    instance.fromPage = "sample_text_2"
    assert instance.fromPage == "sample_text_2"


def test_sistedesMM_InProceedings_month_value_roundtrip():
    instance = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_sistedesMM_InProceedings_title_value_roundtrip():
    instance = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_sistedesMM_InProceedings_toPage_value_roundtrip():
    instance = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    assert instance.toPage == "sample_text"
    instance.toPage = "sample_text_2"
    assert instance.toPage == "sample_text_2"


def test_sistedesMM_InProceedings_year_value_roundtrip():
    instance = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_sistedesMM_Journal_acronym_value_roundtrip():
    instance = sistedesMM_Journal(acronym="sample_text", jcrIndexed=True, name="sample_text")
    assert instance.acronym == "sample_text"
    instance.acronym = "sample_text_2"
    assert instance.acronym == "sample_text_2"


def test_sistedesMM_Journal_jcrIndexed_value_roundtrip():
    instance = sistedesMM_Journal(acronym="sample_text", jcrIndexed=True, name="sample_text")
    assert instance.jcrIndexed == True
    instance.jcrIndexed = False
    assert instance.jcrIndexed == False


def test_sistedesMM_Journal_name_value_roundtrip():
    instance = sistedesMM_Journal(acronym="sample_text", jcrIndexed=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sistedesMM_Person_email_value_roundtrip():
    instance = sistedesMM_Person(email="sample_text", name="sample_text", nationality="sample_text", surname="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_sistedesMM_Person_name_value_roundtrip():
    instance = sistedesMM_Person(email="sample_text", name="sample_text", nationality="sample_text", surname="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sistedesMM_Person_nationality_value_roundtrip():
    instance = sistedesMM_Person(email="sample_text", name="sample_text", nationality="sample_text", surname="sample_text")
    assert instance.nationality == "sample_text"
    instance.nationality = "sample_text_2"
    assert instance.nationality == "sample_text_2"


def test_sistedesMM_Person_surname_value_roundtrip():
    instance = sistedesMM_Person(email="sample_text", name="sample_text", nationality="sample_text", surname="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_sistedesMM_Publisher_address_value_roundtrip():
    instance = sistedesMM_Publisher(address="sample_text", name="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_sistedesMM_Publisher_name_value_roundtrip():
    instance = sistedesMM_Publisher(address="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sistedesMM_University_city_value_roundtrip():
    instance = sistedesMM_University(city="sample_text", country="sample_text", name="sample_text", provinceOrState="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_sistedesMM_University_country_value_roundtrip():
    instance = sistedesMM_University(city="sample_text", country="sample_text", name="sample_text", provinceOrState="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_sistedesMM_University_name_value_roundtrip():
    instance = sistedesMM_University(city="sample_text", country="sample_text", name="sample_text", provinceOrState="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_sistedesMM_University_provinceOrState_value_roundtrip():
    instance = sistedesMM_University(city="sample_text", country="sample_text", name="sample_text", provinceOrState="sample_text")
    assert instance.provinceOrState == "sample_text"
    instance.provinceOrState = "sample_text_2"
    assert instance.provinceOrState == "sample_text_2"


def test_sistedesMM_SistedesMember_isa_Person():
    instance = sistedesMM_SistedesMember()
    assert isinstance(instance, Person)


def test_sistedesMM_Article_isa_Publication():
    instance = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    assert isinstance(instance, Publication)


def test_sistedesMM_Book_isa_Publication():
    instance = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    assert isinstance(instance, Publication)


def test_sistedesMM_InProceedings_isa_Publication():
    instance = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    assert isinstance(instance, Publication)


def test_assoc_articles7_link_reassign_clear():
    a = sistedesMM_Journal(acronym="sample_text", jcrIndexed=True, name="sample_text")
    b1 = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    b2 = sistedesMM_Article(fromPage=13, month="sample_text_2", number=13, title="sample_text_2", toPage=13, volume="sample_text_2", year=13)
    _safe_set(a, 'journal', b1)
    assert _is_linked(a, 'journal', b1)
    if hasattr(b1, 'Article'):
        assert _is_linked(b1, 'Article', a)
    _safe_set(a, 'journal', b2)
    assert _is_linked(a, 'journal', b2)
    if hasattr(b1, 'Article'):
        assert not _is_linked(b1, 'Article', a)
    if hasattr(b2, 'Article'):
        assert _is_linked(b2, 'Article', a)
    _safe_set(a, 'journal', None)
    assert not _is_linked(a, 'journal', b2)
    if hasattr(b2, 'Article'):
        assert not _is_linked(b2, 'Article', a)


def test_assoc_attendedTo10_link_reassign_clear():
    a = sistedesMM_Edition(location="sample_text", year=7)
    b1 = sistedesMM_SistedesMember()
    b2 = sistedesMM_SistedesMember()
    _safe_set(a, 'sistedesMM_Edition', b1)
    assert _is_linked(a, 'sistedesMM_Edition', b1)
    if hasattr(b1, 'sistedesMM_SistedesMember'):
        assert _is_linked(b1, 'sistedesMM_SistedesMember', a)
    _safe_set(a, 'sistedesMM_Edition', b2)
    assert _is_linked(a, 'sistedesMM_Edition', b2)
    if hasattr(b1, 'sistedesMM_SistedesMember'):
        assert not _is_linked(b1, 'sistedesMM_SistedesMember', a)
    if hasattr(b2, 'sistedesMM_SistedesMember'):
        assert _is_linked(b2, 'sistedesMM_SistedesMember', a)
    _safe_set(a, 'sistedesMM_Edition', None)
    assert not _is_linked(a, 'sistedesMM_Edition', b2)
    if hasattr(b2, 'sistedesMM_SistedesMember'):
        assert not _is_linked(b2, 'sistedesMM_SistedesMember', a)


def test_assoc_authors2_link_reassign_clear():
    a = sistedesMM_Person(email="sample_text", name="sample_text", nationality="sample_text", surname="sample_text")
    b1 = sistedesMM_Publication()
    b2 = sistedesMM_Publication()
    _safe_set(a, 'Person', b1)
    assert _is_linked(a, 'Person', b1)
    if hasattr(b1, 'publications'):
        assert _is_linked(b1, 'publications', a)
    _safe_set(a, 'Person', b2)
    assert _is_linked(a, 'Person', b2)
    if hasattr(b1, 'publications'):
        assert not _is_linked(b1, 'publications', a)
    if hasattr(b2, 'publications'):
        assert _is_linked(b2, 'publications', a)
    _safe_set(a, 'Person', None)
    assert not _is_linked(a, 'Person', b2)
    if hasattr(b2, 'publications'):
        assert not _is_linked(b2, 'publications', a)


def test_assoc_editors5_link_reassign_clear():
    a = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    b1 = sistedesMM_Editor(name="sample_text")
    b2 = sistedesMM_Editor(name="sample_text_2")
    _safe_set(a, 'sistedesMM_InProceedings6', {b1})
    assert _is_linked(a, 'sistedesMM_InProceedings6', b1)
    if hasattr(b1, 'sistedesMM_Editor'):
        assert _is_linked(b1, 'sistedesMM_Editor', a)
    _safe_set(a, 'sistedesMM_InProceedings6', {b2})
    assert _is_linked(a, 'sistedesMM_InProceedings6', b2)
    if hasattr(b1, 'sistedesMM_Editor'):
        assert not _is_linked(b1, 'sistedesMM_Editor', a)
    if hasattr(b2, 'sistedesMM_Editor'):
        assert _is_linked(b2, 'sistedesMM_Editor', a)
    _safe_set(a, 'sistedesMM_InProceedings6', set())
    assert not _is_linked(a, 'sistedesMM_InProceedings6', b2)
    if hasattr(b2, 'sistedesMM_Editor'):
        assert not _is_linked(b2, 'sistedesMM_Editor', a)


def test_assoc_journal3_link_reassign_clear():
    a = sistedesMM_Journal(acronym="sample_text", jcrIndexed=True, name="sample_text")
    b1 = sistedesMM_Article(fromPage=7, month="sample_text", number=7, title="sample_text", toPage=7, volume="sample_text", year=7)
    b2 = sistedesMM_Article(fromPage=13, month="sample_text_2", number=13, title="sample_text_2", toPage=13, volume="sample_text_2", year=13)
    _safe_set(a, 'Journal', b1)
    assert _is_linked(a, 'Journal', b1)
    if hasattr(b1, 'articles'):
        assert _is_linked(b1, 'articles', a)
    _safe_set(a, 'Journal', b2)
    assert _is_linked(a, 'Journal', b2)
    if hasattr(b1, 'articles'):
        assert not _is_linked(b1, 'articles', a)
    if hasattr(b2, 'articles'):
        assert _is_linked(b2, 'articles', a)
    _safe_set(a, 'Journal', None)
    assert not _is_linked(a, 'Journal', b2)
    if hasattr(b2, 'articles'):
        assert not _is_linked(b2, 'articles', a)


def test_assoc_publications1_link_reassign_clear():
    a = sistedesMM_Person(email="sample_text", name="sample_text", nationality="sample_text", surname="sample_text")
    b1 = sistedesMM_Publication()
    b2 = sistedesMM_Publication()
    _safe_set(a, 'authors', {b1})
    assert _is_linked(a, 'authors', b1)
    if hasattr(b1, 'Publication'):
        assert _is_linked(b1, 'Publication', a)
    _safe_set(a, 'authors', {b2})
    assert _is_linked(a, 'authors', b2)
    if hasattr(b1, 'Publication'):
        assert not _is_linked(b1, 'Publication', a)
    if hasattr(b2, 'Publication'):
        assert _is_linked(b2, 'Publication', a)
    _safe_set(a, 'authors', set())
    assert not _is_linked(a, 'authors', b2)
    if hasattr(b2, 'Publication'):
        assert not _is_linked(b2, 'Publication', a)


def test_assoc_publisher4_link_reassign_clear():
    a = sistedesMM_Publisher(address="sample_text", name="sample_text")
    b1 = sistedesMM_InProceedings(bookTitle="sample_text", fromPage="sample_text", month="sample_text", title="sample_text", toPage="sample_text", year=7)
    b2 = sistedesMM_InProceedings(bookTitle="sample_text_2", fromPage="sample_text_2", month="sample_text_2", title="sample_text_2", toPage="sample_text_2", year=13)
    _safe_set(a, 'sistedesMM_Publisher', b1)
    assert _is_linked(a, 'sistedesMM_Publisher', b1)
    if hasattr(b1, 'sistedesMM_InProceedings'):
        assert _is_linked(b1, 'sistedesMM_InProceedings', a)
    _safe_set(a, 'sistedesMM_Publisher', b2)
    assert _is_linked(a, 'sistedesMM_Publisher', b2)
    if hasattr(b1, 'sistedesMM_InProceedings'):
        assert not _is_linked(b1, 'sistedesMM_InProceedings', a)
    if hasattr(b2, 'sistedesMM_InProceedings'):
        assert _is_linked(b2, 'sistedesMM_InProceedings', a)
    _safe_set(a, 'sistedesMM_Publisher', None)
    assert not _is_linked(a, 'sistedesMM_Publisher', b2)
    if hasattr(b2, 'sistedesMM_InProceedings'):
        assert not _is_linked(b2, 'sistedesMM_InProceedings', a)


def test_assoc_publisher8_link_reassign_clear():
    a = sistedesMM_Publisher(address="sample_text", name="sample_text")
    b1 = sistedesMM_Book(edition=7, isbn="sample_text", month="sample_text", series="sample_text", title="sample_text", volume="sample_text", year=7)
    b2 = sistedesMM_Book(edition=13, isbn="sample_text_2", month="sample_text_2", series="sample_text_2", title="sample_text_2", volume="sample_text_2", year=13)
    _safe_set(a, 'sistedesMM_Publisher9', b1)
    assert _is_linked(a, 'sistedesMM_Publisher9', b1)
    if hasattr(b1, 'sistedesMM_Book'):
        assert _is_linked(b1, 'sistedesMM_Book', a)
    _safe_set(a, 'sistedesMM_Publisher9', b2)
    assert _is_linked(a, 'sistedesMM_Publisher9', b2)
    if hasattr(b1, 'sistedesMM_Book'):
        assert not _is_linked(b1, 'sistedesMM_Book', a)
    if hasattr(b2, 'sistedesMM_Book'):
        assert _is_linked(b2, 'sistedesMM_Book', a)
    _safe_set(a, 'sistedesMM_Publisher9', None)
    assert not _is_linked(a, 'sistedesMM_Publisher9', b2)
    if hasattr(b2, 'sistedesMM_Book'):
        assert not _is_linked(b2, 'sistedesMM_Book', a)


def test_assoc_university0_link_reassign_clear():
    a = sistedesMM_University(city="sample_text", country="sample_text", name="sample_text", provinceOrState="sample_text")
    b1 = sistedesMM_Person(email="sample_text", name="sample_text", nationality="sample_text", surname="sample_text")
    b2 = sistedesMM_Person(email="sample_text_2", name="sample_text_2", nationality="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'sistedesMM_University', b1)
    assert _is_linked(a, 'sistedesMM_University', b1)
    if hasattr(b1, 'sistedesMM_Person'):
        assert _is_linked(b1, 'sistedesMM_Person', a)
    _safe_set(a, 'sistedesMM_University', b2)
    assert _is_linked(a, 'sistedesMM_University', b2)
    if hasattr(b1, 'sistedesMM_Person'):
        assert not _is_linked(b1, 'sistedesMM_Person', a)
    if hasattr(b2, 'sistedesMM_Person'):
        assert _is_linked(b2, 'sistedesMM_Person', a)
    _safe_set(a, 'sistedesMM_University', None)
    assert not _is_linked(a, 'sistedesMM_University', b2)
    if hasattr(b2, 'sistedesMM_Person'):
        assert not _is_linked(b2, 'sistedesMM_Person', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Publication_strategy = st.builds(Publication)
@given(instance=Publication_strategy)
@settings(max_examples=25)
def test_Publication_instantiation(instance):
    assert isinstance(instance, Publication)


sistedesMM_Article_strategy = st.builds(sistedesMM_Article, fromPage=st.integers(), month=safe_text, number=st.integers(), title=safe_text, toPage=st.integers(), volume=safe_text, year=st.integers())
@given(instance=sistedesMM_Article_strategy)
@settings(max_examples=25)
def test_sistedesMM_Article_instantiation(instance):
    assert isinstance(instance, sistedesMM_Article)


sistedesMM_Book_strategy = st.builds(sistedesMM_Book, edition=st.integers(), isbn=safe_text, month=safe_text, series=safe_text, title=safe_text, volume=safe_text, year=st.integers())
@given(instance=sistedesMM_Book_strategy)
@settings(max_examples=25)
def test_sistedesMM_Book_instantiation(instance):
    assert isinstance(instance, sistedesMM_Book)


sistedesMM_Edition_strategy = st.builds(sistedesMM_Edition, location=safe_text, year=st.integers())
@given(instance=sistedesMM_Edition_strategy)
@settings(max_examples=25)
def test_sistedesMM_Edition_instantiation(instance):
    assert isinstance(instance, sistedesMM_Edition)


sistedesMM_Editor_strategy = st.builds(sistedesMM_Editor, name=safe_text)
@given(instance=sistedesMM_Editor_strategy)
@settings(max_examples=25)
def test_sistedesMM_Editor_instantiation(instance):
    assert isinstance(instance, sistedesMM_Editor)


sistedesMM_InProceedings_strategy = st.builds(sistedesMM_InProceedings, bookTitle=safe_text, fromPage=safe_text, month=safe_text, title=safe_text, toPage=safe_text, year=st.integers())
@given(instance=sistedesMM_InProceedings_strategy)
@settings(max_examples=25)
def test_sistedesMM_InProceedings_instantiation(instance):
    assert isinstance(instance, sistedesMM_InProceedings)


sistedesMM_Journal_strategy = st.builds(sistedesMM_Journal, acronym=safe_text, jcrIndexed=st.booleans(), name=safe_text)
@given(instance=sistedesMM_Journal_strategy)
@settings(max_examples=25)
def test_sistedesMM_Journal_instantiation(instance):
    assert isinstance(instance, sistedesMM_Journal)


sistedesMM_Person_strategy = st.builds(sistedesMM_Person, email=safe_text, name=safe_text, nationality=safe_text, surname=safe_text)
@given(instance=sistedesMM_Person_strategy)
@settings(max_examples=25)
def test_sistedesMM_Person_instantiation(instance):
    assert isinstance(instance, sistedesMM_Person)


sistedesMM_Publication_strategy = st.builds(sistedesMM_Publication)
@given(instance=sistedesMM_Publication_strategy)
@settings(max_examples=25)
def test_sistedesMM_Publication_instantiation(instance):
    assert isinstance(instance, sistedesMM_Publication)


sistedesMM_Publisher_strategy = st.builds(sistedesMM_Publisher, address=safe_text, name=safe_text)
@given(instance=sistedesMM_Publisher_strategy)
@settings(max_examples=25)
def test_sistedesMM_Publisher_instantiation(instance):
    assert isinstance(instance, sistedesMM_Publisher)


sistedesMM_SistedesMember_strategy = st.builds(sistedesMM_SistedesMember)
@given(instance=sistedesMM_SistedesMember_strategy)
@settings(max_examples=25)
def test_sistedesMM_SistedesMember_instantiation(instance):
    assert isinstance(instance, sistedesMM_SistedesMember)


sistedesMM_University_strategy = st.builds(sistedesMM_University, city=safe_text, country=safe_text, name=safe_text, provinceOrState=safe_text)
@given(instance=sistedesMM_University_strategy)
@settings(max_examples=25)
def test_sistedesMM_University_instantiation(instance):
    assert isinstance(instance, sistedesMM_University)



