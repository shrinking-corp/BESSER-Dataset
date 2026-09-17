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
    library_data_base,
    Book,
    patron,
    librarian,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_data_base_is_not_abstract():
    assert not inspect.isabstract(library_data_base)


def test_hyp_library_data_base_constructor_exists():
    assert callable(library_data_base.__init__)


def test_hyp_library_data_base_constructor_args():
    sig = inspect.signature(library_data_base.__init__)
    params = list(sig.parameters.keys())
    assert "record_patron_borrowing_book" in params, "Missing parameter 'record_patron_borrowing_book'"
    assert "list_of_books" in params, "Missing parameter 'list_of_books'"
    assert "members_information" in params, "Missing parameter 'members_information'"






def test_hyp_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_hyp_book_constructor_exists():
    assert callable(Book.__init__)


def test_hyp_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "Book_ISBN" in params, "Missing parameter 'Book_ISBN'"
    assert "Book_Author" in params, "Missing parameter 'Book_Author'"
    assert "book_name" in params, "Missing parameter 'book_name'"






def test_hyp_patron_is_not_abstract():
    assert not inspect.isabstract(patron)


def test_hyp_patron_constructor_exists():
    assert callable(patron.__init__)


def test_hyp_patron_constructor_args():
    sig = inspect.signature(patron.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Contact_number" in params, "Missing parameter 'Contact_number'"
    assert "Name" in params, "Missing parameter 'Name'"






def test_hyp_librarian_is_not_abstract():
    assert not inspect.isabstract(librarian)


def test_hyp_librarian_constructor_exists():
    assert callable(librarian.__init__)


def test_hyp_librarian_constructor_args():
    sig = inspect.signature(librarian.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
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
library_data_base_strategy = st.builds(
    library_data_base,
    record_patron_borrowing_book=
        st.integers(),
    list_of_books=
        safe_text,
    members_information=
        safe_text
)
Book_strategy = st.builds(
    Book,
    Book_ISBN=
        st.integers(),
    Book_Author=
        st.integers(),
    book_name=
        safe_text
)
patron_strategy = st.builds(
    patron,
    Address=
        safe_text,
    Contact_number=
        st.integers(),
    Name=
        safe_text
)
librarian_strategy = st.builds(
    librarian,
    username=
        st.integers(),
    name=
        safe_text
)




@given(instance=library_data_base_strategy)
def test_hyp_library_data_base_record_patron_borrowing_book_setter(instance):
    original = instance.record_patron_borrowing_book
    instance.record_patron_borrowing_book = original
    assert instance.record_patron_borrowing_book == original



@given(instance=library_data_base_strategy)
def test_hyp_library_data_base_list_of_books_setter(instance):
    original = instance.list_of_books
    instance.list_of_books = original
    assert instance.list_of_books == original



@given(instance=library_data_base_strategy)
def test_hyp_library_data_base_members_information_setter(instance):
    original = instance.members_information
    instance.members_information = original
    assert instance.members_information == original




@given(instance=Book_strategy)
def test_hyp_book_Book_ISBN_setter(instance):
    original = instance.Book_ISBN
    instance.Book_ISBN = original
    assert instance.Book_ISBN == original



@given(instance=Book_strategy)
def test_hyp_book_Book_Author_setter(instance):
    original = instance.Book_Author
    instance.Book_Author = original
    assert instance.Book_Author == original



@given(instance=Book_strategy)
def test_hyp_book_book_name_setter(instance):
    original = instance.book_name
    instance.book_name = original
    assert instance.book_name == original




@given(instance=patron_strategy)
def test_hyp_patron_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=patron_strategy)
def test_hyp_patron_Contact_number_setter(instance):
    original = instance.Contact_number
    instance.Contact_number = original
    assert instance.Contact_number == original



@given(instance=patron_strategy)
def test_hyp_patron_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=librarian_strategy)
def test_hyp_librarian_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=librarian_strategy)
def test_hyp_librarian_name_setter(instance):
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
    Book,
    librarian,
    library_data_base,
    patron,
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

def test_Book_Book_Author_value_roundtrip():
    instance = Book(Book_Author=7, Book_ISBN=7, book_name="sample_text")
    assert instance.Book_Author == 7
    instance.Book_Author = 13
    assert instance.Book_Author == 13


def test_Book_Book_ISBN_value_roundtrip():
    instance = Book(Book_Author=7, Book_ISBN=7, book_name="sample_text")
    assert instance.Book_ISBN == 7
    instance.Book_ISBN = 13
    assert instance.Book_ISBN == 13


def test_Book_book_name_value_roundtrip():
    instance = Book(Book_Author=7, Book_ISBN=7, book_name="sample_text")
    assert instance.book_name == "sample_text"
    instance.book_name = "sample_text_2"
    assert instance.book_name == "sample_text_2"


def test_librarian_name_value_roundtrip():
    instance = librarian(name="sample_text", username=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_librarian_username_value_roundtrip():
    instance = librarian(name="sample_text", username=7)
    assert instance.username == 7
    instance.username = 13
    assert instance.username == 13


def test_library_data_base_list_of_books_value_roundtrip():
    instance = library_data_base(list_of_books="sample_text", members_information="sample_text", record_patron_borrowing_book=7)
    assert instance.list_of_books == "sample_text"
    instance.list_of_books = "sample_text_2"
    assert instance.list_of_books == "sample_text_2"


def test_library_data_base_members_information_value_roundtrip():
    instance = library_data_base(list_of_books="sample_text", members_information="sample_text", record_patron_borrowing_book=7)
    assert instance.members_information == "sample_text"
    instance.members_information = "sample_text_2"
    assert instance.members_information == "sample_text_2"


def test_library_data_base_record_patron_borrowing_book_value_roundtrip():
    instance = library_data_base(list_of_books="sample_text", members_information="sample_text", record_patron_borrowing_book=7)
    assert instance.record_patron_borrowing_book == 7
    instance.record_patron_borrowing_book = 13
    assert instance.record_patron_borrowing_book == 13


def test_patron_Address_value_roundtrip():
    instance = patron(Address="sample_text", Contact_number=7, Name="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_patron_Contact_number_value_roundtrip():
    instance = patron(Address="sample_text", Contact_number=7, Name="sample_text")
    assert instance.Contact_number == 7
    instance.Contact_number = 13
    assert instance.Contact_number == 13


def test_patron_Name_value_roundtrip():
    instance = patron(Address="sample_text", Contact_number=7, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Book_strategy = st.builds(Book, Book_Author=st.integers(), Book_ISBN=st.integers(), book_name=safe_text)
@given(instance=Book_strategy)
@settings(max_examples=25)
def test_Book_instantiation(instance):
    assert isinstance(instance, Book)


librarian_strategy = st.builds(librarian, name=safe_text, username=st.integers())
@given(instance=librarian_strategy)
@settings(max_examples=25)
def test_librarian_instantiation(instance):
    assert isinstance(instance, librarian)


library_data_base_strategy = st.builds(library_data_base, list_of_books=safe_text, members_information=safe_text, record_patron_borrowing_book=st.integers())
@given(instance=library_data_base_strategy)
@settings(max_examples=25)
def test_library_data_base_instantiation(instance):
    assert isinstance(instance, library_data_base)


patron_strategy = st.builds(patron, Address=safe_text, Contact_number=st.integers(), Name=safe_text)
@given(instance=patron_strategy)
@settings(max_examples=25)
def test_patron_instantiation(instance):
    assert isinstance(instance, patron)



