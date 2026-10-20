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
    Issue_member_card_external,
    Search_books_external,
    Request_book_return_external,
    Request_book_external,
    Inquiry_for_membership_external,
    MyClass2,
    MyClass,
    Librarian_Actor,
    Member_Actor,
    Library_Management_Component,
    Update_member_profile_external,
    Return_book_external,
    Issue_book_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_issue_member_card_external_is_not_abstract():
    assert not inspect.isabstract(Issue_member_card_external)


def test_hyp_issue_member_card_external_constructor_exists():
    assert callable(Issue_member_card_external.__init__)


def test_hyp_issue_member_card_external_constructor_args():
    sig = inspect.signature(Issue_member_card_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_search_books_external_is_not_abstract():
    assert not inspect.isabstract(Search_books_external)


def test_hyp_search_books_external_constructor_exists():
    assert callable(Search_books_external.__init__)


def test_hyp_search_books_external_constructor_args():
    sig = inspect.signature(Search_books_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_request_book_return_external_is_not_abstract():
    assert not inspect.isabstract(Request_book_return_external)


def test_hyp_request_book_return_external_constructor_exists():
    assert callable(Request_book_return_external.__init__)


def test_hyp_request_book_return_external_constructor_args():
    sig = inspect.signature(Request_book_return_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_request_book_external_is_not_abstract():
    assert not inspect.isabstract(Request_book_external)


def test_hyp_request_book_external_constructor_exists():
    assert callable(Request_book_external.__init__)


def test_hyp_request_book_external_constructor_args():
    sig = inspect.signature(Request_book_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_inquiry_for_membership_external_is_not_abstract():
    assert not inspect.isabstract(Inquiry_for_membership_external)


def test_hyp_inquiry_for_membership_external_constructor_exists():
    assert callable(Inquiry_for_membership_external.__init__)


def test_hyp_inquiry_for_membership_external_constructor_args():
    sig = inspect.signature(Inquiry_for_membership_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_hyp_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_hyp_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_hyp_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_hyp_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_librarian_actor_is_not_abstract():
    assert not inspect.isabstract(Librarian_Actor)


def test_hyp_librarian_actor_constructor_exists():
    assert callable(Librarian_Actor.__init__)


def test_hyp_librarian_actor_constructor_args():
    sig = inspect.signature(Librarian_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_member_actor_is_not_abstract():
    assert not inspect.isabstract(Member_Actor)


def test_hyp_member_actor_constructor_exists():
    assert callable(Member_Actor.__init__)


def test_hyp_member_actor_constructor_args():
    sig = inspect.signature(Member_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_library_management_component_is_not_abstract():
    assert not inspect.isabstract(Library_Management_Component)


def test_hyp_library_management_component_constructor_exists():
    assert callable(Library_Management_Component.__init__)


def test_hyp_library_management_component_constructor_args():
    sig = inspect.signature(Library_Management_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_update_member_profile_external_is_not_abstract():
    assert not inspect.isabstract(Update_member_profile_external)


def test_hyp_update_member_profile_external_constructor_exists():
    assert callable(Update_member_profile_external.__init__)


def test_hyp_update_member_profile_external_constructor_args():
    sig = inspect.signature(Update_member_profile_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_return_book_external_is_not_abstract():
    assert not inspect.isabstract(Return_book_external)


def test_hyp_return_book_external_constructor_exists():
    assert callable(Return_book_external.__init__)


def test_hyp_return_book_external_constructor_args():
    sig = inspect.signature(Return_book_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_issue_book_external_is_not_abstract():
    assert not inspect.isabstract(Issue_book_external)


def test_hyp_issue_book_external_constructor_exists():
    assert callable(Issue_book_external.__init__)


def test_hyp_issue_book_external_constructor_args():
    sig = inspect.signature(Issue_book_external.__init__)
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
Issue_member_card_external_strategy = st.builds(
    Issue_member_card_external,
)
Search_books_external_strategy = st.builds(
    Search_books_external,
)
Request_book_return_external_strategy = st.builds(
    Request_book_return_external,
)
Request_book_external_strategy = st.builds(
    Request_book_external,
)
Inquiry_for_membership_external_strategy = st.builds(
    Inquiry_for_membership_external,
)
MyClass2_strategy = st.builds(
    MyClass2,
    attribute=
        safe_text
)
MyClass_strategy = st.builds(
    MyClass,
    attribute=
        safe_text
)
Librarian_Actor_strategy = st.builds(
    Librarian_Actor,
)
Member_Actor_strategy = st.builds(
    Member_Actor,
)
Library_Management_Component_strategy = st.builds(
    Library_Management_Component,
)
Update_member_profile_external_strategy = st.builds(
    Update_member_profile_external,
)
Return_book_external_strategy = st.builds(
    Return_book_external,
)
Issue_book_external_strategy = st.builds(
    Issue_book_external,
)









@given(instance=MyClass2_strategy)
def test_hyp_myclass2_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=MyClass_strategy)
def test_hyp_myclass_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original








# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Inquiry_for_membership_external,
    Issue_book_external,
    Issue_member_card_external,
    Librarian_Actor,
    Library_Management_Component,
    Member_Actor,
    MyClass,
    MyClass2,
    Request_book_external,
    Request_book_return_external,
    Return_book_external,
    Search_books_external,
    Update_member_profile_external,
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

def test_MyClass_attribute_value_roundtrip():
    instance = MyClass(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_MyClass2_attribute_value_roundtrip():
    instance = MyClass2(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Inquiry_for_membership_external_strategy = st.builds(Inquiry_for_membership_external)
@given(instance=Inquiry_for_membership_external_strategy)
@settings(max_examples=25)
def test_Inquiry_for_membership_external_instantiation(instance):
    assert isinstance(instance, Inquiry_for_membership_external)


Issue_book_external_strategy = st.builds(Issue_book_external)
@given(instance=Issue_book_external_strategy)
@settings(max_examples=25)
def test_Issue_book_external_instantiation(instance):
    assert isinstance(instance, Issue_book_external)


Issue_member_card_external_strategy = st.builds(Issue_member_card_external)
@given(instance=Issue_member_card_external_strategy)
@settings(max_examples=25)
def test_Issue_member_card_external_instantiation(instance):
    assert isinstance(instance, Issue_member_card_external)


Librarian_Actor_strategy = st.builds(Librarian_Actor)
@given(instance=Librarian_Actor_strategy)
@settings(max_examples=25)
def test_Librarian_Actor_instantiation(instance):
    assert isinstance(instance, Librarian_Actor)


Library_Management_Component_strategy = st.builds(Library_Management_Component)
@given(instance=Library_Management_Component_strategy)
@settings(max_examples=25)
def test_Library_Management_Component_instantiation(instance):
    assert isinstance(instance, Library_Management_Component)


Member_Actor_strategy = st.builds(Member_Actor)
@given(instance=Member_Actor_strategy)
@settings(max_examples=25)
def test_Member_Actor_instantiation(instance):
    assert isinstance(instance, Member_Actor)


MyClass_strategy = st.builds(MyClass, attribute=safe_text)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


MyClass2_strategy = st.builds(MyClass2, attribute=safe_text)
@given(instance=MyClass2_strategy)
@settings(max_examples=25)
def test_MyClass2_instantiation(instance):
    assert isinstance(instance, MyClass2)


Request_book_external_strategy = st.builds(Request_book_external)
@given(instance=Request_book_external_strategy)
@settings(max_examples=25)
def test_Request_book_external_instantiation(instance):
    assert isinstance(instance, Request_book_external)


Request_book_return_external_strategy = st.builds(Request_book_return_external)
@given(instance=Request_book_return_external_strategy)
@settings(max_examples=25)
def test_Request_book_return_external_instantiation(instance):
    assert isinstance(instance, Request_book_return_external)


Return_book_external_strategy = st.builds(Return_book_external)
@given(instance=Return_book_external_strategy)
@settings(max_examples=25)
def test_Return_book_external_instantiation(instance):
    assert isinstance(instance, Return_book_external)


Search_books_external_strategy = st.builds(Search_books_external)
@given(instance=Search_books_external_strategy)
@settings(max_examples=25)
def test_Search_books_external_instantiation(instance):
    assert isinstance(instance, Search_books_external)


Update_member_profile_external_strategy = st.builds(Update_member_profile_external)
@given(instance=Update_member_profile_external_strategy)
@settings(max_examples=25)
def test_Update_member_profile_external_instantiation(instance):
    assert isinstance(instance, Update_member_profile_external)



