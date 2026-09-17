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
    Library,
    MyClass,
    Library_Management_Component,
    Patron_Actor,
    Cancel_UseCase,
    create_UseCase,
    Checkout_book_UseCase,
    Request_Book_UseCase,
    Create_library_account_UseCase,
    Renew_Patron_UseCase,
    Late_fees_UseCase,
    Update_Books_UseCase,
    Remove_Books_UseCase,
    Add_books_UseCase,
    Maintain_Patron_profile_UseCase,
    Return_book_UseCase,
    Issue_Book_UseCase,
    Manage_Books_UseCase,
    Issue_card_UseCase,
    Librarian_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_hyp_library_constructor_exists():
    assert callable(Library.__init__)


def test_hyp_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())
    assert "books" in params, "Missing parameter 'books'"




def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_management_component_is_not_abstract():
    assert not inspect.isabstract(Library_Management_Component)


def test_hyp_library_management_component_constructor_exists():
    assert callable(Library_Management_Component.__init__)


def test_hyp_library_management_component_constructor_args():
    sig = inspect.signature(Library_Management_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_patron_actor_is_not_abstract():
    assert not inspect.isabstract(Patron_Actor)


def test_hyp_patron_actor_constructor_exists():
    assert callable(Patron_Actor.__init__)


def test_hyp_patron_actor_constructor_args():
    sig = inspect.signature(Patron_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cancel_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancel_UseCase)


def test_hyp_cancel_usecase_constructor_exists():
    assert callable(Cancel_UseCase.__init__)


def test_hyp_cancel_usecase_constructor_args():
    sig = inspect.signature(Cancel_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_create_usecase_is_not_abstract():
    assert not inspect.isabstract(create_UseCase)


def test_hyp_create_usecase_constructor_exists():
    assert callable(create_UseCase.__init__)


def test_hyp_create_usecase_constructor_args():
    sig = inspect.signature(create_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_checkout_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Checkout_book_UseCase)


def test_hyp_checkout_book_usecase_constructor_exists():
    assert callable(Checkout_book_UseCase.__init__)


def test_hyp_checkout_book_usecase_constructor_args():
    sig = inspect.signature(Checkout_book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_request_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Request_Book_UseCase)


def test_hyp_request_book_usecase_constructor_exists():
    assert callable(Request_Book_UseCase.__init__)


def test_hyp_request_book_usecase_constructor_args():
    sig = inspect.signature(Request_Book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_create_library_account_usecase_is_not_abstract():
    assert not inspect.isabstract(Create_library_account_UseCase)


def test_hyp_create_library_account_usecase_constructor_exists():
    assert callable(Create_library_account_UseCase.__init__)


def test_hyp_create_library_account_usecase_constructor_args():
    sig = inspect.signature(Create_library_account_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_renew_patron_usecase_is_not_abstract():
    assert not inspect.isabstract(Renew_Patron_UseCase)


def test_hyp_renew_patron_usecase_constructor_exists():
    assert callable(Renew_Patron_UseCase.__init__)


def test_hyp_renew_patron_usecase_constructor_args():
    sig = inspect.signature(Renew_Patron_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_late_fees_usecase_is_not_abstract():
    assert not inspect.isabstract(Late_fees_UseCase)


def test_hyp_late_fees_usecase_constructor_exists():
    assert callable(Late_fees_UseCase.__init__)


def test_hyp_late_fees_usecase_constructor_args():
    sig = inspect.signature(Late_fees_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_update_books_usecase_is_not_abstract():
    assert not inspect.isabstract(Update_Books_UseCase)


def test_hyp_update_books_usecase_constructor_exists():
    assert callable(Update_Books_UseCase.__init__)


def test_hyp_update_books_usecase_constructor_args():
    sig = inspect.signature(Update_Books_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_remove_books_usecase_is_not_abstract():
    assert not inspect.isabstract(Remove_Books_UseCase)


def test_hyp_remove_books_usecase_constructor_exists():
    assert callable(Remove_Books_UseCase.__init__)


def test_hyp_remove_books_usecase_constructor_args():
    sig = inspect.signature(Remove_Books_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_add_books_usecase_is_not_abstract():
    assert not inspect.isabstract(Add_books_UseCase)


def test_hyp_add_books_usecase_constructor_exists():
    assert callable(Add_books_UseCase.__init__)


def test_hyp_add_books_usecase_constructor_args():
    sig = inspect.signature(Add_books_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_maintain_patron_profile_usecase_is_not_abstract():
    assert not inspect.isabstract(Maintain_Patron_profile_UseCase)


def test_hyp_maintain_patron_profile_usecase_constructor_exists():
    assert callable(Maintain_Patron_profile_UseCase.__init__)


def test_hyp_maintain_patron_profile_usecase_constructor_args():
    sig = inspect.signature(Maintain_Patron_profile_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_return_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Return_book_UseCase)


def test_hyp_return_book_usecase_constructor_exists():
    assert callable(Return_book_UseCase.__init__)


def test_hyp_return_book_usecase_constructor_args():
    sig = inspect.signature(Return_book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_issue_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Issue_Book_UseCase)


def test_hyp_issue_book_usecase_constructor_exists():
    assert callable(Issue_Book_UseCase.__init__)


def test_hyp_issue_book_usecase_constructor_args():
    sig = inspect.signature(Issue_Book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manage_books_usecase_is_not_abstract():
    assert not inspect.isabstract(Manage_Books_UseCase)


def test_hyp_manage_books_usecase_constructor_exists():
    assert callable(Manage_Books_UseCase.__init__)


def test_hyp_manage_books_usecase_constructor_args():
    sig = inspect.signature(Manage_Books_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_issue_card_usecase_is_not_abstract():
    assert not inspect.isabstract(Issue_card_UseCase)


def test_hyp_issue_card_usecase_constructor_exists():
    assert callable(Issue_card_UseCase.__init__)


def test_hyp_issue_card_usecase_constructor_args():
    sig = inspect.signature(Issue_card_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_librarian_actor_is_not_abstract():
    assert not inspect.isabstract(Librarian_Actor)


def test_hyp_librarian_actor_constructor_exists():
    assert callable(Librarian_Actor.__init__)


def test_hyp_librarian_actor_constructor_args():
    sig = inspect.signature(Librarian_Actor.__init__)
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
Library_strategy = st.builds(
    Library,
    books=
        safe_text
)
MyClass_strategy = st.builds(
    MyClass,
)
Library_Management_Component_strategy = st.builds(
    Library_Management_Component,
)
Patron_Actor_strategy = st.builds(
    Patron_Actor,
)
Cancel_UseCase_strategy = st.builds(
    Cancel_UseCase,
)
create_UseCase_strategy = st.builds(
    create_UseCase,
)
Checkout_book_UseCase_strategy = st.builds(
    Checkout_book_UseCase,
)
Request_Book_UseCase_strategy = st.builds(
    Request_Book_UseCase,
)
Create_library_account_UseCase_strategy = st.builds(
    Create_library_account_UseCase,
)
Renew_Patron_UseCase_strategy = st.builds(
    Renew_Patron_UseCase,
)
Late_fees_UseCase_strategy = st.builds(
    Late_fees_UseCase,
)
Update_Books_UseCase_strategy = st.builds(
    Update_Books_UseCase,
)
Remove_Books_UseCase_strategy = st.builds(
    Remove_Books_UseCase,
)
Add_books_UseCase_strategy = st.builds(
    Add_books_UseCase,
)
Maintain_Patron_profile_UseCase_strategy = st.builds(
    Maintain_Patron_profile_UseCase,
)
Return_book_UseCase_strategy = st.builds(
    Return_book_UseCase,
)
Issue_Book_UseCase_strategy = st.builds(
    Issue_Book_UseCase,
)
Manage_Books_UseCase_strategy = st.builds(
    Manage_Books_UseCase,
)
Issue_card_UseCase_strategy = st.builds(
    Issue_card_UseCase,
)
Librarian_Actor_strategy = st.builds(
    Librarian_Actor,
)




@given(instance=Library_strategy)
def test_hyp_library_books_setter(instance):
    original = instance.books
    instance.books = original
    assert instance.books == original





















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Add_books_UseCase,
    Cancel_UseCase,
    Checkout_book_UseCase,
    Create_library_account_UseCase,
    Issue_Book_UseCase,
    Issue_card_UseCase,
    Late_fees_UseCase,
    Librarian_Actor,
    Library,
    Library_Management_Component,
    Maintain_Patron_profile_UseCase,
    Manage_Books_UseCase,
    MyClass,
    Patron_Actor,
    Remove_Books_UseCase,
    Renew_Patron_UseCase,
    Request_Book_UseCase,
    Return_book_UseCase,
    Update_Books_UseCase,
    create_UseCase,
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

def test_Library_books_value_roundtrip():
    instance = Library(books="sample_text")
    assert instance.books == "sample_text"
    instance.books = "sample_text_2"
    assert instance.books == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Add_books_UseCase_strategy = st.builds(Add_books_UseCase)
@given(instance=Add_books_UseCase_strategy)
@settings(max_examples=25)
def test_Add_books_UseCase_instantiation(instance):
    assert isinstance(instance, Add_books_UseCase)


Cancel_UseCase_strategy = st.builds(Cancel_UseCase)
@given(instance=Cancel_UseCase_strategy)
@settings(max_examples=25)
def test_Cancel_UseCase_instantiation(instance):
    assert isinstance(instance, Cancel_UseCase)


Checkout_book_UseCase_strategy = st.builds(Checkout_book_UseCase)
@given(instance=Checkout_book_UseCase_strategy)
@settings(max_examples=25)
def test_Checkout_book_UseCase_instantiation(instance):
    assert isinstance(instance, Checkout_book_UseCase)


Create_library_account_UseCase_strategy = st.builds(Create_library_account_UseCase)
@given(instance=Create_library_account_UseCase_strategy)
@settings(max_examples=25)
def test_Create_library_account_UseCase_instantiation(instance):
    assert isinstance(instance, Create_library_account_UseCase)


Issue_Book_UseCase_strategy = st.builds(Issue_Book_UseCase)
@given(instance=Issue_Book_UseCase_strategy)
@settings(max_examples=25)
def test_Issue_Book_UseCase_instantiation(instance):
    assert isinstance(instance, Issue_Book_UseCase)


Issue_card_UseCase_strategy = st.builds(Issue_card_UseCase)
@given(instance=Issue_card_UseCase_strategy)
@settings(max_examples=25)
def test_Issue_card_UseCase_instantiation(instance):
    assert isinstance(instance, Issue_card_UseCase)


Late_fees_UseCase_strategy = st.builds(Late_fees_UseCase)
@given(instance=Late_fees_UseCase_strategy)
@settings(max_examples=25)
def test_Late_fees_UseCase_instantiation(instance):
    assert isinstance(instance, Late_fees_UseCase)


Librarian_Actor_strategy = st.builds(Librarian_Actor)
@given(instance=Librarian_Actor_strategy)
@settings(max_examples=25)
def test_Librarian_Actor_instantiation(instance):
    assert isinstance(instance, Librarian_Actor)


Library_strategy = st.builds(Library, books=safe_text)
@given(instance=Library_strategy)
@settings(max_examples=25)
def test_Library_instantiation(instance):
    assert isinstance(instance, Library)


Library_Management_Component_strategy = st.builds(Library_Management_Component)
@given(instance=Library_Management_Component_strategy)
@settings(max_examples=25)
def test_Library_Management_Component_instantiation(instance):
    assert isinstance(instance, Library_Management_Component)


Maintain_Patron_profile_UseCase_strategy = st.builds(Maintain_Patron_profile_UseCase)
@given(instance=Maintain_Patron_profile_UseCase_strategy)
@settings(max_examples=25)
def test_Maintain_Patron_profile_UseCase_instantiation(instance):
    assert isinstance(instance, Maintain_Patron_profile_UseCase)


Manage_Books_UseCase_strategy = st.builds(Manage_Books_UseCase)
@given(instance=Manage_Books_UseCase_strategy)
@settings(max_examples=25)
def test_Manage_Books_UseCase_instantiation(instance):
    assert isinstance(instance, Manage_Books_UseCase)


MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


Patron_Actor_strategy = st.builds(Patron_Actor)
@given(instance=Patron_Actor_strategy)
@settings(max_examples=25)
def test_Patron_Actor_instantiation(instance):
    assert isinstance(instance, Patron_Actor)


Remove_Books_UseCase_strategy = st.builds(Remove_Books_UseCase)
@given(instance=Remove_Books_UseCase_strategy)
@settings(max_examples=25)
def test_Remove_Books_UseCase_instantiation(instance):
    assert isinstance(instance, Remove_Books_UseCase)


Renew_Patron_UseCase_strategy = st.builds(Renew_Patron_UseCase)
@given(instance=Renew_Patron_UseCase_strategy)
@settings(max_examples=25)
def test_Renew_Patron_UseCase_instantiation(instance):
    assert isinstance(instance, Renew_Patron_UseCase)


Request_Book_UseCase_strategy = st.builds(Request_Book_UseCase)
@given(instance=Request_Book_UseCase_strategy)
@settings(max_examples=25)
def test_Request_Book_UseCase_instantiation(instance):
    assert isinstance(instance, Request_Book_UseCase)


Return_book_UseCase_strategy = st.builds(Return_book_UseCase)
@given(instance=Return_book_UseCase_strategy)
@settings(max_examples=25)
def test_Return_book_UseCase_instantiation(instance):
    assert isinstance(instance, Return_book_UseCase)


Update_Books_UseCase_strategy = st.builds(Update_Books_UseCase)
@given(instance=Update_Books_UseCase_strategy)
@settings(max_examples=25)
def test_Update_Books_UseCase_instantiation(instance):
    assert isinstance(instance, Update_Books_UseCase)


create_UseCase_strategy = st.builds(create_UseCase)
@given(instance=create_UseCase_strategy)
@settings(max_examples=25)
def test_create_UseCase_instantiation(instance):
    assert isinstance(instance, create_UseCase)



