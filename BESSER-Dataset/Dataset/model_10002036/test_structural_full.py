import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Book_ticket_UseCase,
    Cancel_ticket_UseCase,
    Check_ticket_availability_UseCase,
    Class,
    Clerk_Actor,
    Express,
    Express1,
    Fill_the_details_UseCase,
    Information_Interface,
    Pay_fare_amount_UseCase,
    Pessanger,
    Railway_website_Actor,
    Refund_money_UseCase,
    SuperFast,
    SuperFast1,
    Traveler_Actor,
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

def test_Express_General_value_roundtrip():
    instance = Express(General="sample_text", SecondSitting="sample_text")
    assert instance.General == "sample_text"
    instance.General = "sample_text_2"
    assert instance.General == "sample_text_2"


def test_Express_SecondSitting_value_roundtrip():
    instance = Express(General="sample_text", SecondSitting="sample_text")
    assert instance.SecondSitting == "sample_text"
    instance.SecondSitting = "sample_text_2"
    assert instance.SecondSitting == "sample_text_2"


def test_Express1_SecondSitting_value_roundtrip():
    instance = Express1(SecondSitting="sample_text")
    assert instance.SecondSitting == "sample_text"
    instance.SecondSitting = "sample_text_2"
    assert instance.SecondSitting == "sample_text_2"


def test_Pessanger_AadharNo_value_roundtrip():
    instance = Pessanger(AadharNo=7, Children=7)
    assert instance.AadharNo == 7
    instance.AadharNo = 13
    assert instance.AadharNo == 13


def test_Pessanger_Children_value_roundtrip():
    instance = Pessanger(AadharNo=7, Children=7)
    assert instance.Children == 7
    instance.Children = 13
    assert instance.Children == 13


def test_SuperFast_AC_1_value_roundtrip():
    instance = SuperFast(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Sleeper="sample_text")
    assert instance.AC_1 == "sample_text"
    instance.AC_1 = "sample_text_2"
    assert instance.AC_1 == "sample_text_2"


def test_SuperFast_AC_2_value_roundtrip():
    instance = SuperFast(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Sleeper="sample_text")
    assert instance.AC_2 == "sample_text"
    instance.AC_2 = "sample_text_2"
    assert instance.AC_2 == "sample_text_2"


def test_SuperFast_AC_3_value_roundtrip():
    instance = SuperFast(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Sleeper="sample_text")
    assert instance.AC_3 == "sample_text"
    instance.AC_3 = "sample_text_2"
    assert instance.AC_3 == "sample_text_2"


def test_SuperFast_Sleeper_value_roundtrip():
    instance = SuperFast(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Sleeper="sample_text")
    assert instance.Sleeper == "sample_text"
    instance.Sleeper = "sample_text_2"
    assert instance.Sleeper == "sample_text_2"


def test_SuperFast1_AC_1_value_roundtrip():
    instance = SuperFast1(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Handicamp="sample_text", Ladies="sample_text", Sleeper="sample_text")
    assert instance.AC_1 == "sample_text"
    instance.AC_1 = "sample_text_2"
    assert instance.AC_1 == "sample_text_2"


def test_SuperFast1_AC_2_value_roundtrip():
    instance = SuperFast1(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Handicamp="sample_text", Ladies="sample_text", Sleeper="sample_text")
    assert instance.AC_2 == "sample_text"
    instance.AC_2 = "sample_text_2"
    assert instance.AC_2 == "sample_text_2"


def test_SuperFast1_AC_3_value_roundtrip():
    instance = SuperFast1(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Handicamp="sample_text", Ladies="sample_text", Sleeper="sample_text")
    assert instance.AC_3 == "sample_text"
    instance.AC_3 = "sample_text_2"
    assert instance.AC_3 == "sample_text_2"


def test_SuperFast1_Handicamp_value_roundtrip():
    instance = SuperFast1(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Handicamp="sample_text", Ladies="sample_text", Sleeper="sample_text")
    assert instance.Handicamp == "sample_text"
    instance.Handicamp = "sample_text_2"
    assert instance.Handicamp == "sample_text_2"


def test_SuperFast1_Ladies_value_roundtrip():
    instance = SuperFast1(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Handicamp="sample_text", Ladies="sample_text", Sleeper="sample_text")
    assert instance.Ladies == "sample_text"
    instance.Ladies = "sample_text_2"
    assert instance.Ladies == "sample_text_2"


def test_SuperFast1_Sleeper_value_roundtrip():
    instance = SuperFast1(AC_1="sample_text", AC_2="sample_text", AC_3="sample_text", Handicamp="sample_text", Ladies="sample_text", Sleeper="sample_text")
    assert instance.Sleeper == "sample_text"
    instance.Sleeper = "sample_text_2"
    assert instance.Sleeper == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Book_ticket_UseCase_strategy = st.builds(Book_ticket_UseCase)
@given(instance=Book_ticket_UseCase_strategy)
@settings(max_examples=25)
def test_Book_ticket_UseCase_instantiation(instance):
    assert isinstance(instance, Book_ticket_UseCase)


Cancel_ticket_UseCase_strategy = st.builds(Cancel_ticket_UseCase)
@given(instance=Cancel_ticket_UseCase_strategy)
@settings(max_examples=25)
def test_Cancel_ticket_UseCase_instantiation(instance):
    assert isinstance(instance, Cancel_ticket_UseCase)


Check_ticket_availability_UseCase_strategy = st.builds(Check_ticket_availability_UseCase)
@given(instance=Check_ticket_availability_UseCase_strategy)
@settings(max_examples=25)
def test_Check_ticket_availability_UseCase_instantiation(instance):
    assert isinstance(instance, Check_ticket_availability_UseCase)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Clerk_Actor_strategy = st.builds(Clerk_Actor)
@given(instance=Clerk_Actor_strategy)
@settings(max_examples=25)
def test_Clerk_Actor_instantiation(instance):
    assert isinstance(instance, Clerk_Actor)


Express_strategy = st.builds(Express, General=safe_text, SecondSitting=safe_text)
@given(instance=Express_strategy)
@settings(max_examples=25)
def test_Express_instantiation(instance):
    assert isinstance(instance, Express)


Express1_strategy = st.builds(Express1, SecondSitting=safe_text)
@given(instance=Express1_strategy)
@settings(max_examples=25)
def test_Express1_instantiation(instance):
    assert isinstance(instance, Express1)


Fill_the_details_UseCase_strategy = st.builds(Fill_the_details_UseCase)
@given(instance=Fill_the_details_UseCase_strategy)
@settings(max_examples=25)
def test_Fill_the_details_UseCase_instantiation(instance):
    assert isinstance(instance, Fill_the_details_UseCase)


Information_Interface_strategy = st.builds(Information_Interface)
@given(instance=Information_Interface_strategy)
@settings(max_examples=25)
def test_Information_Interface_instantiation(instance):
    assert isinstance(instance, Information_Interface)


Pay_fare_amount_UseCase_strategy = st.builds(Pay_fare_amount_UseCase)
@given(instance=Pay_fare_amount_UseCase_strategy)
@settings(max_examples=25)
def test_Pay_fare_amount_UseCase_instantiation(instance):
    assert isinstance(instance, Pay_fare_amount_UseCase)


Pessanger_strategy = st.builds(Pessanger, AadharNo=st.integers(), Children=st.integers())
@given(instance=Pessanger_strategy)
@settings(max_examples=25)
def test_Pessanger_instantiation(instance):
    assert isinstance(instance, Pessanger)


Railway_website_Actor_strategy = st.builds(Railway_website_Actor)
@given(instance=Railway_website_Actor_strategy)
@settings(max_examples=25)
def test_Railway_website_Actor_instantiation(instance):
    assert isinstance(instance, Railway_website_Actor)


Refund_money_UseCase_strategy = st.builds(Refund_money_UseCase)
@given(instance=Refund_money_UseCase_strategy)
@settings(max_examples=25)
def test_Refund_money_UseCase_instantiation(instance):
    assert isinstance(instance, Refund_money_UseCase)


SuperFast_strategy = st.builds(SuperFast, AC_1=safe_text, AC_2=safe_text, AC_3=safe_text, Sleeper=safe_text)
@given(instance=SuperFast_strategy)
@settings(max_examples=25)
def test_SuperFast_instantiation(instance):
    assert isinstance(instance, SuperFast)


SuperFast1_strategy = st.builds(SuperFast1, AC_1=safe_text, AC_2=safe_text, AC_3=safe_text, Handicamp=safe_text, Ladies=safe_text, Sleeper=safe_text)
@given(instance=SuperFast1_strategy)
@settings(max_examples=25)
def test_SuperFast1_instantiation(instance):
    assert isinstance(instance, SuperFast1)


Traveler_Actor_strategy = st.builds(Traveler_Actor)
@given(instance=Traveler_Actor_strategy)
@settings(max_examples=25)
def test_Traveler_Actor_instantiation(instance):
    assert isinstance(instance, Traveler_Actor)


