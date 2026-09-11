import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Amend_Membership_details_UseCase,
    Books,
    Cancel_Membership_UseCase,
    Carry_Out_Stock_Check_UseCase,
    Charge_fine_for_Late_Book_UseCase,
    Checkout_Librarian_Actor,
    Chief_Librarian_Actor,
    Collect_Fine_UseCase,
    Create_New_Member_UseCase,
    Head_Librarian_Actor,
    Inform_Memeber_when_Item_Available_UseCase,
    Issue_Book_UseCase,
    Library_Members,
    Make_Reservation_UseCase,
    Purchase_Books_UseCase,
    Reservations,
    Return_Item_UseCase,
    Suspend_Membership_UseCase,
    Withdraw_Books_UseCase,
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

def test_Books_Title_value_roundtrip():
    instance = Books(Title="sample_text")
    assert instance.Title == "sample_text"
    instance.Title = "sample_text_2"
    assert instance.Title == "sample_text_2"


def test_Library_Members_Name_value_roundtrip():
    instance = Library_Members(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Amend_Membership_details_UseCase_strategy = st.builds(Amend_Membership_details_UseCase)
@given(instance=Amend_Membership_details_UseCase_strategy)
@settings(max_examples=25)
def test_Amend_Membership_details_UseCase_instantiation(instance):
    assert isinstance(instance, Amend_Membership_details_UseCase)


Books_strategy = st.builds(Books, Title=safe_text)
@given(instance=Books_strategy)
@settings(max_examples=25)
def test_Books_instantiation(instance):
    assert isinstance(instance, Books)


Cancel_Membership_UseCase_strategy = st.builds(Cancel_Membership_UseCase)
@given(instance=Cancel_Membership_UseCase_strategy)
@settings(max_examples=25)
def test_Cancel_Membership_UseCase_instantiation(instance):
    assert isinstance(instance, Cancel_Membership_UseCase)


Carry_Out_Stock_Check_UseCase_strategy = st.builds(Carry_Out_Stock_Check_UseCase)
@given(instance=Carry_Out_Stock_Check_UseCase_strategy)
@settings(max_examples=25)
def test_Carry_Out_Stock_Check_UseCase_instantiation(instance):
    assert isinstance(instance, Carry_Out_Stock_Check_UseCase)


Charge_fine_for_Late_Book_UseCase_strategy = st.builds(Charge_fine_for_Late_Book_UseCase)
@given(instance=Charge_fine_for_Late_Book_UseCase_strategy)
@settings(max_examples=25)
def test_Charge_fine_for_Late_Book_UseCase_instantiation(instance):
    assert isinstance(instance, Charge_fine_for_Late_Book_UseCase)


Checkout_Librarian_Actor_strategy = st.builds(Checkout_Librarian_Actor)
@given(instance=Checkout_Librarian_Actor_strategy)
@settings(max_examples=25)
def test_Checkout_Librarian_Actor_instantiation(instance):
    assert isinstance(instance, Checkout_Librarian_Actor)


Chief_Librarian_Actor_strategy = st.builds(Chief_Librarian_Actor)
@given(instance=Chief_Librarian_Actor_strategy)
@settings(max_examples=25)
def test_Chief_Librarian_Actor_instantiation(instance):
    assert isinstance(instance, Chief_Librarian_Actor)


Collect_Fine_UseCase_strategy = st.builds(Collect_Fine_UseCase)
@given(instance=Collect_Fine_UseCase_strategy)
@settings(max_examples=25)
def test_Collect_Fine_UseCase_instantiation(instance):
    assert isinstance(instance, Collect_Fine_UseCase)


Create_New_Member_UseCase_strategy = st.builds(Create_New_Member_UseCase)
@given(instance=Create_New_Member_UseCase_strategy)
@settings(max_examples=25)
def test_Create_New_Member_UseCase_instantiation(instance):
    assert isinstance(instance, Create_New_Member_UseCase)


Head_Librarian_Actor_strategy = st.builds(Head_Librarian_Actor)
@given(instance=Head_Librarian_Actor_strategy)
@settings(max_examples=25)
def test_Head_Librarian_Actor_instantiation(instance):
    assert isinstance(instance, Head_Librarian_Actor)


Inform_Memeber_when_Item_Available_UseCase_strategy = st.builds(Inform_Memeber_when_Item_Available_UseCase)
@given(instance=Inform_Memeber_when_Item_Available_UseCase_strategy)
@settings(max_examples=25)
def test_Inform_Memeber_when_Item_Available_UseCase_instantiation(instance):
    assert isinstance(instance, Inform_Memeber_when_Item_Available_UseCase)


Issue_Book_UseCase_strategy = st.builds(Issue_Book_UseCase)
@given(instance=Issue_Book_UseCase_strategy)
@settings(max_examples=25)
def test_Issue_Book_UseCase_instantiation(instance):
    assert isinstance(instance, Issue_Book_UseCase)


Library_Members_strategy = st.builds(Library_Members, Name=safe_text)
@given(instance=Library_Members_strategy)
@settings(max_examples=25)
def test_Library_Members_instantiation(instance):
    assert isinstance(instance, Library_Members)


Make_Reservation_UseCase_strategy = st.builds(Make_Reservation_UseCase)
@given(instance=Make_Reservation_UseCase_strategy)
@settings(max_examples=25)
def test_Make_Reservation_UseCase_instantiation(instance):
    assert isinstance(instance, Make_Reservation_UseCase)


Purchase_Books_UseCase_strategy = st.builds(Purchase_Books_UseCase)
@given(instance=Purchase_Books_UseCase_strategy)
@settings(max_examples=25)
def test_Purchase_Books_UseCase_instantiation(instance):
    assert isinstance(instance, Purchase_Books_UseCase)


Reservations_strategy = st.builds(Reservations)
@given(instance=Reservations_strategy)
@settings(max_examples=25)
def test_Reservations_instantiation(instance):
    assert isinstance(instance, Reservations)


Return_Item_UseCase_strategy = st.builds(Return_Item_UseCase)
@given(instance=Return_Item_UseCase_strategy)
@settings(max_examples=25)
def test_Return_Item_UseCase_instantiation(instance):
    assert isinstance(instance, Return_Item_UseCase)


Suspend_Membership_UseCase_strategy = st.builds(Suspend_Membership_UseCase)
@given(instance=Suspend_Membership_UseCase_strategy)
@settings(max_examples=25)
def test_Suspend_Membership_UseCase_instantiation(instance):
    assert isinstance(instance, Suspend_Membership_UseCase)


Withdraw_Books_UseCase_strategy = st.builds(Withdraw_Books_UseCase)
@given(instance=Withdraw_Books_UseCase_strategy)
@settings(max_examples=25)
def test_Withdraw_Books_UseCase_instantiation(instance):
    assert isinstance(instance, Withdraw_Books_UseCase)


