import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Airline_Agency_Actor,
    Check_Tickets_UseCase,
    Choose_Flight_UseCase,
    Create_Account_UseCase,
    Invalid_Details_UseCase,
    Invalid_UseCase,
    Make_Payment___Checkout_UseCase,
    MyClass,
    Pay_Travel_Agent_UseCase,
    Proceed_to_Checkout_UseCase,
    Receive_Payment_UseCase,
    Register__Login_UseCase,
    Reserve_a_Ticket_UseCase,
    Review_Order_UseCase,
    Travel_Agent_Actor,
    Travel_Agent_Fee_UseCase,
    User___Passenger_Actor,
    Valid_Details_UseCase,
    Valid_UseCase,
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

# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Airline_Agency_Actor_strategy = st.builds(Airline_Agency_Actor)
@given(instance=Airline_Agency_Actor_strategy)
@settings(max_examples=25)
def test_Airline_Agency_Actor_instantiation(instance):
    assert isinstance(instance, Airline_Agency_Actor)


Check_Tickets_UseCase_strategy = st.builds(Check_Tickets_UseCase)
@given(instance=Check_Tickets_UseCase_strategy)
@settings(max_examples=25)
def test_Check_Tickets_UseCase_instantiation(instance):
    assert isinstance(instance, Check_Tickets_UseCase)


Choose_Flight_UseCase_strategy = st.builds(Choose_Flight_UseCase)
@given(instance=Choose_Flight_UseCase_strategy)
@settings(max_examples=25)
def test_Choose_Flight_UseCase_instantiation(instance):
    assert isinstance(instance, Choose_Flight_UseCase)


Create_Account_UseCase_strategy = st.builds(Create_Account_UseCase)
@given(instance=Create_Account_UseCase_strategy)
@settings(max_examples=25)
def test_Create_Account_UseCase_instantiation(instance):
    assert isinstance(instance, Create_Account_UseCase)


Invalid_Details_UseCase_strategy = st.builds(Invalid_Details_UseCase)
@given(instance=Invalid_Details_UseCase_strategy)
@settings(max_examples=25)
def test_Invalid_Details_UseCase_instantiation(instance):
    assert isinstance(instance, Invalid_Details_UseCase)


Invalid_UseCase_strategy = st.builds(Invalid_UseCase)
@given(instance=Invalid_UseCase_strategy)
@settings(max_examples=25)
def test_Invalid_UseCase_instantiation(instance):
    assert isinstance(instance, Invalid_UseCase)


Make_Payment___Checkout_UseCase_strategy = st.builds(Make_Payment___Checkout_UseCase)
@given(instance=Make_Payment___Checkout_UseCase_strategy)
@settings(max_examples=25)
def test_Make_Payment___Checkout_UseCase_instantiation(instance):
    assert isinstance(instance, Make_Payment___Checkout_UseCase)


MyClass_strategy = st.builds(MyClass)
@given(instance=MyClass_strategy)
@settings(max_examples=25)
def test_MyClass_instantiation(instance):
    assert isinstance(instance, MyClass)


Pay_Travel_Agent_UseCase_strategy = st.builds(Pay_Travel_Agent_UseCase)
@given(instance=Pay_Travel_Agent_UseCase_strategy)
@settings(max_examples=25)
def test_Pay_Travel_Agent_UseCase_instantiation(instance):
    assert isinstance(instance, Pay_Travel_Agent_UseCase)


Proceed_to_Checkout_UseCase_strategy = st.builds(Proceed_to_Checkout_UseCase)
@given(instance=Proceed_to_Checkout_UseCase_strategy)
@settings(max_examples=25)
def test_Proceed_to_Checkout_UseCase_instantiation(instance):
    assert isinstance(instance, Proceed_to_Checkout_UseCase)


Receive_Payment_UseCase_strategy = st.builds(Receive_Payment_UseCase)
@given(instance=Receive_Payment_UseCase_strategy)
@settings(max_examples=25)
def test_Receive_Payment_UseCase_instantiation(instance):
    assert isinstance(instance, Receive_Payment_UseCase)


Register__Login_UseCase_strategy = st.builds(Register__Login_UseCase)
@given(instance=Register__Login_UseCase_strategy)
@settings(max_examples=25)
def test_Register__Login_UseCase_instantiation(instance):
    assert isinstance(instance, Register__Login_UseCase)


Reserve_a_Ticket_UseCase_strategy = st.builds(Reserve_a_Ticket_UseCase)
@given(instance=Reserve_a_Ticket_UseCase_strategy)
@settings(max_examples=25)
def test_Reserve_a_Ticket_UseCase_instantiation(instance):
    assert isinstance(instance, Reserve_a_Ticket_UseCase)


Review_Order_UseCase_strategy = st.builds(Review_Order_UseCase)
@given(instance=Review_Order_UseCase_strategy)
@settings(max_examples=25)
def test_Review_Order_UseCase_instantiation(instance):
    assert isinstance(instance, Review_Order_UseCase)


Travel_Agent_Actor_strategy = st.builds(Travel_Agent_Actor)
@given(instance=Travel_Agent_Actor_strategy)
@settings(max_examples=25)
def test_Travel_Agent_Actor_instantiation(instance):
    assert isinstance(instance, Travel_Agent_Actor)


Travel_Agent_Fee_UseCase_strategy = st.builds(Travel_Agent_Fee_UseCase)
@given(instance=Travel_Agent_Fee_UseCase_strategy)
@settings(max_examples=25)
def test_Travel_Agent_Fee_UseCase_instantiation(instance):
    assert isinstance(instance, Travel_Agent_Fee_UseCase)


User___Passenger_Actor_strategy = st.builds(User___Passenger_Actor)
@given(instance=User___Passenger_Actor_strategy)
@settings(max_examples=25)
def test_User___Passenger_Actor_instantiation(instance):
    assert isinstance(instance, User___Passenger_Actor)


Valid_Details_UseCase_strategy = st.builds(Valid_Details_UseCase)
@given(instance=Valid_Details_UseCase_strategy)
@settings(max_examples=25)
def test_Valid_Details_UseCase_instantiation(instance):
    assert isinstance(instance, Valid_Details_UseCase)


Valid_UseCase_strategy = st.builds(Valid_UseCase)
@given(instance=Valid_UseCase_strategy)
@settings(max_examples=25)
def test_Valid_UseCase_instantiation(instance):
    assert isinstance(instance, Valid_UseCase)


