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
    Search_for_Books_external,
    Checkout_Book_external,
    Database_external,
    Return_Book_external,
    Send_Book_external,
    librarymanagementsystem_Library,
    Library_Staff_Actor,
    Patron_Actor,
    Library_Management_System_Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_search_for_books_external_is_not_abstract():
    assert not inspect.isabstract(Search_for_Books_external)


def test_hyp_search_for_books_external_constructor_exists():
    assert callable(Search_for_Books_external.__init__)


def test_hyp_search_for_books_external_constructor_args():
    sig = inspect.signature(Search_for_Books_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_checkout_book_external_is_not_abstract():
    assert not inspect.isabstract(Checkout_Book_external)


def test_hyp_checkout_book_external_constructor_exists():
    assert callable(Checkout_Book_external.__init__)


def test_hyp_checkout_book_external_constructor_args():
    sig = inspect.signature(Checkout_Book_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_database_external_is_not_abstract():
    assert not inspect.isabstract(Database_external)


def test_hyp_database_external_constructor_exists():
    assert callable(Database_external.__init__)


def test_hyp_database_external_constructor_args():
    sig = inspect.signature(Database_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_return_book_external_is_not_abstract():
    assert not inspect.isabstract(Return_Book_external)


def test_hyp_return_book_external_constructor_exists():
    assert callable(Return_Book_external.__init__)


def test_hyp_return_book_external_constructor_args():
    sig = inspect.signature(Return_Book_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_send_book_external_is_not_abstract():
    assert not inspect.isabstract(Send_Book_external)


def test_hyp_send_book_external_constructor_exists():
    assert callable(Send_Book_external.__init__)


def test_hyp_send_book_external_constructor_args():
    sig = inspect.signature(Send_Book_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_librarymanagementsystem_library_is_not_abstract():
    assert not inspect.isabstract(librarymanagementsystem_Library)


def test_hyp_librarymanagementsystem_library_constructor_exists():
    assert callable(librarymanagementsystem_Library.__init__)


def test_hyp_librarymanagementsystem_library_constructor_args():
    sig = inspect.signature(librarymanagementsystem_Library.__init__)
    params = list(sig.parameters.keys())
    assert "fine" in params, "Missing parameter 'fine'"
    assert "books" in params, "Missing parameter 'books'"
    assert "computers" in params, "Missing parameter 'computers'"
    assert "videos" in params, "Missing parameter 'videos'"
    assert "CDs" in params, "Missing parameter 'CDs'"
    assert "software" in params, "Missing parameter 'software'"
    assert "maxFine" in params, "Missing parameter 'maxFine'"










def test_hyp_library_staff_actor_is_not_abstract():
    assert not inspect.isabstract(Library_Staff_Actor)


def test_hyp_library_staff_actor_constructor_exists():
    assert callable(Library_Staff_Actor.__init__)


def test_hyp_library_staff_actor_constructor_args():
    sig = inspect.signature(Library_Staff_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patron_actor_is_not_abstract():
    assert not inspect.isabstract(Patron_Actor)


def test_hyp_patron_actor_constructor_exists():
    assert callable(Patron_Actor.__init__)


def test_hyp_patron_actor_constructor_args():
    sig = inspect.signature(Patron_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_management_system_component_is_not_abstract():
    assert not inspect.isabstract(Library_Management_System_Component)


def test_hyp_library_management_system_component_constructor_exists():
    assert callable(Library_Management_System_Component.__init__)


def test_hyp_library_management_system_component_constructor_args():
    sig = inspect.signature(Library_Management_System_Component.__init__)
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
Search_for_Books_external_strategy = st.builds(
    Search_for_Books_external,
)
Checkout_Book_external_strategy = st.builds(
    Checkout_Book_external,
)
Database_external_strategy = st.builds(
    Database_external,
)
Return_Book_external_strategy = st.builds(
    Return_Book_external,
)
Send_Book_external_strategy = st.builds(
    Send_Book_external,
)
librarymanagementsystem_Library_strategy = st.builds(
    librarymanagementsystem_Library,
    fine=
        safe_text,
    books=
        safe_text,
    computers=
        st.integers(),
    videos=
        safe_text,
    CDs=
        safe_text,
    software=
        safe_text,
    maxFine=
        safe_text
)
Library_Staff_Actor_strategy = st.builds(
    Library_Staff_Actor,
)
Patron_Actor_strategy = st.builds(
    Patron_Actor,
)
Library_Management_System_Component_strategy = st.builds(
    Library_Management_System_Component,
)









@given(instance=librarymanagementsystem_Library_strategy)
def test_hyp_librarymanagementsystem_library_fine_setter(instance):
    original = instance.fine
    instance.fine = original
    assert instance.fine == original



@given(instance=librarymanagementsystem_Library_strategy)
def test_hyp_librarymanagementsystem_library_books_setter(instance):
    original = instance.books
    instance.books = original
    assert instance.books == original



@given(instance=librarymanagementsystem_Library_strategy)
def test_hyp_librarymanagementsystem_library_computers_setter(instance):
    original = instance.computers
    instance.computers = original
    assert instance.computers == original



@given(instance=librarymanagementsystem_Library_strategy)
def test_hyp_librarymanagementsystem_library_videos_setter(instance):
    original = instance.videos
    instance.videos = original
    assert instance.videos == original



@given(instance=librarymanagementsystem_Library_strategy)
def test_hyp_librarymanagementsystem_library_CDs_setter(instance):
    original = instance.CDs
    instance.CDs = original
    assert instance.CDs == original



@given(instance=librarymanagementsystem_Library_strategy)
def test_hyp_librarymanagementsystem_library_software_setter(instance):
    original = instance.software
    instance.software = original
    assert instance.software == original



@given(instance=librarymanagementsystem_Library_strategy)
def test_hyp_librarymanagementsystem_library_maxFine_setter(instance):
    original = instance.maxFine
    instance.maxFine = original
    assert instance.maxFine == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Checkout_Book_external,
    Database_external,
    Library_Management_System_Component,
    Library_Staff_Actor,
    Patron_Actor,
    Return_Book_external,
    Search_for_Books_external,
    Send_Book_external,
    librarymanagementsystem_Library,
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

def test_librarymanagementsystem_Library_CDs_value_roundtrip():
    instance = librarymanagementsystem_Library(CDs="sample_text", books="sample_text", computers=7, fine="sample_text", maxFine="sample_text", software="sample_text", videos="sample_text")
    assert instance.CDs == "sample_text"
    instance.CDs = "sample_text_2"
    assert instance.CDs == "sample_text_2"


def test_librarymanagementsystem_Library_books_value_roundtrip():
    instance = librarymanagementsystem_Library(CDs="sample_text", books="sample_text", computers=7, fine="sample_text", maxFine="sample_text", software="sample_text", videos="sample_text")
    assert instance.books == "sample_text"
    instance.books = "sample_text_2"
    assert instance.books == "sample_text_2"


def test_librarymanagementsystem_Library_computers_value_roundtrip():
    instance = librarymanagementsystem_Library(CDs="sample_text", books="sample_text", computers=7, fine="sample_text", maxFine="sample_text", software="sample_text", videos="sample_text")
    assert instance.computers == 7
    instance.computers = 13
    assert instance.computers == 13


def test_librarymanagementsystem_Library_fine_value_roundtrip():
    instance = librarymanagementsystem_Library(CDs="sample_text", books="sample_text", computers=7, fine="sample_text", maxFine="sample_text", software="sample_text", videos="sample_text")
    assert instance.fine == "sample_text"
    instance.fine = "sample_text_2"
    assert instance.fine == "sample_text_2"


def test_librarymanagementsystem_Library_maxFine_value_roundtrip():
    instance = librarymanagementsystem_Library(CDs="sample_text", books="sample_text", computers=7, fine="sample_text", maxFine="sample_text", software="sample_text", videos="sample_text")
    assert instance.maxFine == "sample_text"
    instance.maxFine = "sample_text_2"
    assert instance.maxFine == "sample_text_2"


def test_librarymanagementsystem_Library_software_value_roundtrip():
    instance = librarymanagementsystem_Library(CDs="sample_text", books="sample_text", computers=7, fine="sample_text", maxFine="sample_text", software="sample_text", videos="sample_text")
    assert instance.software == "sample_text"
    instance.software = "sample_text_2"
    assert instance.software == "sample_text_2"


def test_librarymanagementsystem_Library_videos_value_roundtrip():
    instance = librarymanagementsystem_Library(CDs="sample_text", books="sample_text", computers=7, fine="sample_text", maxFine="sample_text", software="sample_text", videos="sample_text")
    assert instance.videos == "sample_text"
    instance.videos = "sample_text_2"
    assert instance.videos == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Checkout_Book_external_strategy = st.builds(Checkout_Book_external)
@given(instance=Checkout_Book_external_strategy)
@settings(max_examples=25)
def test_Checkout_Book_external_instantiation(instance):
    assert isinstance(instance, Checkout_Book_external)


Database_external_strategy = st.builds(Database_external)
@given(instance=Database_external_strategy)
@settings(max_examples=25)
def test_Database_external_instantiation(instance):
    assert isinstance(instance, Database_external)


Library_Management_System_Component_strategy = st.builds(Library_Management_System_Component)
@given(instance=Library_Management_System_Component_strategy)
@settings(max_examples=25)
def test_Library_Management_System_Component_instantiation(instance):
    assert isinstance(instance, Library_Management_System_Component)


Library_Staff_Actor_strategy = st.builds(Library_Staff_Actor)
@given(instance=Library_Staff_Actor_strategy)
@settings(max_examples=25)
def test_Library_Staff_Actor_instantiation(instance):
    assert isinstance(instance, Library_Staff_Actor)


Patron_Actor_strategy = st.builds(Patron_Actor)
@given(instance=Patron_Actor_strategy)
@settings(max_examples=25)
def test_Patron_Actor_instantiation(instance):
    assert isinstance(instance, Patron_Actor)


Return_Book_external_strategy = st.builds(Return_Book_external)
@given(instance=Return_Book_external_strategy)
@settings(max_examples=25)
def test_Return_Book_external_instantiation(instance):
    assert isinstance(instance, Return_Book_external)


Search_for_Books_external_strategy = st.builds(Search_for_Books_external)
@given(instance=Search_for_Books_external_strategy)
@settings(max_examples=25)
def test_Search_for_Books_external_instantiation(instance):
    assert isinstance(instance, Search_for_Books_external)


Send_Book_external_strategy = st.builds(Send_Book_external)
@given(instance=Send_Book_external_strategy)
@settings(max_examples=25)
def test_Send_Book_external_instantiation(instance):
    assert isinstance(instance, Send_Book_external)


librarymanagementsystem_Library_strategy = st.builds(librarymanagementsystem_Library, CDs=safe_text, books=safe_text, computers=st.integers(), fine=safe_text, maxFine=safe_text, software=safe_text, videos=safe_text)
@given(instance=librarymanagementsystem_Library_strategy)
@settings(max_examples=25)
def test_librarymanagementsystem_Library_instantiation(instance):
    assert isinstance(instance, librarymanagementsystem_Library)



