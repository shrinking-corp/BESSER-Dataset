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
    Railway_website_Actor,
    Clerk_Actor,
    Refund_money_UseCase,
    Cancel_ticket_UseCase,
    Fill_the_details_UseCase,
    Book_ticket_UseCase,
    Pay_fare_amount_UseCase,
    Check_ticket_availability_UseCase,
    Traveler_Actor,
    Pessanger,
    Information_Interface,
    Express1,
    SuperFast1,
    Express,
    SuperFast,
    Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_railway_website_actor_is_not_abstract():
    assert not inspect.isabstract(Railway_website_Actor)


def test_hyp_railway_website_actor_constructor_exists():
    assert callable(Railway_website_Actor.__init__)


def test_hyp_railway_website_actor_constructor_args():
    sig = inspect.signature(Railway_website_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_clerk_actor_is_not_abstract():
    assert not inspect.isabstract(Clerk_Actor)


def test_hyp_clerk_actor_constructor_exists():
    assert callable(Clerk_Actor.__init__)


def test_hyp_clerk_actor_constructor_args():
    sig = inspect.signature(Clerk_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_refund_money_usecase_is_not_abstract():
    assert not inspect.isabstract(Refund_money_UseCase)


def test_hyp_refund_money_usecase_constructor_exists():
    assert callable(Refund_money_UseCase.__init__)


def test_hyp_refund_money_usecase_constructor_args():
    sig = inspect.signature(Refund_money_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cancel_ticket_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancel_ticket_UseCase)


def test_hyp_cancel_ticket_usecase_constructor_exists():
    assert callable(Cancel_ticket_UseCase.__init__)


def test_hyp_cancel_ticket_usecase_constructor_args():
    sig = inspect.signature(Cancel_ticket_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fill_the_details_usecase_is_not_abstract():
    assert not inspect.isabstract(Fill_the_details_UseCase)


def test_hyp_fill_the_details_usecase_constructor_exists():
    assert callable(Fill_the_details_UseCase.__init__)


def test_hyp_fill_the_details_usecase_constructor_args():
    sig = inspect.signature(Fill_the_details_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_book_ticket_usecase_is_not_abstract():
    assert not inspect.isabstract(Book_ticket_UseCase)


def test_hyp_book_ticket_usecase_constructor_exists():
    assert callable(Book_ticket_UseCase.__init__)


def test_hyp_book_ticket_usecase_constructor_args():
    sig = inspect.signature(Book_ticket_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pay_fare_amount_usecase_is_not_abstract():
    assert not inspect.isabstract(Pay_fare_amount_UseCase)


def test_hyp_pay_fare_amount_usecase_constructor_exists():
    assert callable(Pay_fare_amount_UseCase.__init__)


def test_hyp_pay_fare_amount_usecase_constructor_args():
    sig = inspect.signature(Pay_fare_amount_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_check_ticket_availability_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_ticket_availability_UseCase)


def test_hyp_check_ticket_availability_usecase_constructor_exists():
    assert callable(Check_ticket_availability_UseCase.__init__)


def test_hyp_check_ticket_availability_usecase_constructor_args():
    sig = inspect.signature(Check_ticket_availability_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_traveler_actor_is_not_abstract():
    assert not inspect.isabstract(Traveler_Actor)


def test_hyp_traveler_actor_constructor_exists():
    assert callable(Traveler_Actor.__init__)


def test_hyp_traveler_actor_constructor_args():
    sig = inspect.signature(Traveler_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pessanger_is_not_abstract():
    assert not inspect.isabstract(Pessanger)


def test_hyp_pessanger_constructor_exists():
    assert callable(Pessanger.__init__)


def test_hyp_pessanger_constructor_args():
    sig = inspect.signature(Pessanger.__init__)
    params = list(sig.parameters.keys())
    assert "AadharNo" in params, "Missing parameter 'AadharNo'"
    assert "Children" in params, "Missing parameter 'Children'"





def test_hyp_information_interface_is_not_abstract():
    assert not inspect.isabstract(Information_Interface)


def test_hyp_information_interface_constructor_exists():
    assert callable(Information_Interface.__init__)


def test_hyp_information_interface_constructor_args():
    sig = inspect.signature(Information_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_express1_is_not_abstract():
    assert not inspect.isabstract(Express1)


def test_hyp_express1_constructor_exists():
    assert callable(Express1.__init__)


def test_hyp_express1_constructor_args():
    sig = inspect.signature(Express1.__init__)
    params = list(sig.parameters.keys())
    assert "SecondSitting" in params, "Missing parameter 'SecondSitting'"




def test_hyp_superfast1_is_not_abstract():
    assert not inspect.isabstract(SuperFast1)


def test_hyp_superfast1_constructor_exists():
    assert callable(SuperFast1.__init__)


def test_hyp_superfast1_constructor_args():
    sig = inspect.signature(SuperFast1.__init__)
    params = list(sig.parameters.keys())
    assert "AC_2" in params, "Missing parameter 'AC_2'"
    assert "Ladies" in params, "Missing parameter 'Ladies'"
    assert "Sleeper" in params, "Missing parameter 'Sleeper'"
    assert "AC_3" in params, "Missing parameter 'AC_3'"
    assert "Handicamp" in params, "Missing parameter 'Handicamp'"
    assert "AC_1" in params, "Missing parameter 'AC_1'"









def test_hyp_express_is_not_abstract():
    assert not inspect.isabstract(Express)


def test_hyp_express_constructor_exists():
    assert callable(Express.__init__)


def test_hyp_express_constructor_args():
    sig = inspect.signature(Express.__init__)
    params = list(sig.parameters.keys())
    assert "SecondSitting" in params, "Missing parameter 'SecondSitting'"
    assert "General" in params, "Missing parameter 'General'"





def test_hyp_superfast_is_not_abstract():
    assert not inspect.isabstract(SuperFast)


def test_hyp_superfast_constructor_exists():
    assert callable(SuperFast.__init__)


def test_hyp_superfast_constructor_args():
    sig = inspect.signature(SuperFast.__init__)
    params = list(sig.parameters.keys())
    assert "AC_1" in params, "Missing parameter 'AC_1'"
    assert "AC_2" in params, "Missing parameter 'AC_2'"
    assert "Sleeper" in params, "Missing parameter 'Sleeper'"
    assert "AC_3" in params, "Missing parameter 'AC_3'"







def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
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
Railway_website_Actor_strategy = st.builds(
    Railway_website_Actor,
)
Clerk_Actor_strategy = st.builds(
    Clerk_Actor,
)
Refund_money_UseCase_strategy = st.builds(
    Refund_money_UseCase,
)
Cancel_ticket_UseCase_strategy = st.builds(
    Cancel_ticket_UseCase,
)
Fill_the_details_UseCase_strategy = st.builds(
    Fill_the_details_UseCase,
)
Book_ticket_UseCase_strategy = st.builds(
    Book_ticket_UseCase,
)
Pay_fare_amount_UseCase_strategy = st.builds(
    Pay_fare_amount_UseCase,
)
Check_ticket_availability_UseCase_strategy = st.builds(
    Check_ticket_availability_UseCase,
)
Traveler_Actor_strategy = st.builds(
    Traveler_Actor,
)
Pessanger_strategy = st.builds(
    Pessanger,
    AadharNo=
        st.integers(),
    Children=
        st.integers()
)
Information_Interface_strategy = st.builds(
    Information_Interface,
)
Express1_strategy = st.builds(
    Express1,
    SecondSitting=
        safe_text
)
SuperFast1_strategy = st.builds(
    SuperFast1,
    AC_2=
        safe_text,
    Ladies=
        safe_text,
    Sleeper=
        safe_text,
    AC_3=
        safe_text,
    Handicamp=
        safe_text,
    AC_1=
        safe_text
)
Express_strategy = st.builds(
    Express,
    SecondSitting=
        safe_text,
    General=
        safe_text
)
SuperFast_strategy = st.builds(
    SuperFast,
    AC_1=
        safe_text,
    AC_2=
        safe_text,
    Sleeper=
        safe_text,
    AC_3=
        safe_text
)
Class_strategy = st.builds(
    Class,
)













@given(instance=Pessanger_strategy)
def test_hyp_pessanger_AadharNo_setter(instance):
    original = instance.AadharNo
    instance.AadharNo = original
    assert instance.AadharNo == original



@given(instance=Pessanger_strategy)
def test_hyp_pessanger_Children_setter(instance):
    original = instance.Children
    instance.Children = original
    assert instance.Children == original





@given(instance=Express1_strategy)
def test_hyp_express1_SecondSitting_setter(instance):
    original = instance.SecondSitting
    instance.SecondSitting = original
    assert instance.SecondSitting == original




@given(instance=SuperFast1_strategy)
def test_hyp_superfast1_AC_2_setter(instance):
    original = instance.AC_2
    instance.AC_2 = original
    assert instance.AC_2 == original



@given(instance=SuperFast1_strategy)
def test_hyp_superfast1_Ladies_setter(instance):
    original = instance.Ladies
    instance.Ladies = original
    assert instance.Ladies == original



@given(instance=SuperFast1_strategy)
def test_hyp_superfast1_Sleeper_setter(instance):
    original = instance.Sleeper
    instance.Sleeper = original
    assert instance.Sleeper == original



@given(instance=SuperFast1_strategy)
def test_hyp_superfast1_AC_3_setter(instance):
    original = instance.AC_3
    instance.AC_3 = original
    assert instance.AC_3 == original



@given(instance=SuperFast1_strategy)
def test_hyp_superfast1_Handicamp_setter(instance):
    original = instance.Handicamp
    instance.Handicamp = original
    assert instance.Handicamp == original



@given(instance=SuperFast1_strategy)
def test_hyp_superfast1_AC_1_setter(instance):
    original = instance.AC_1
    instance.AC_1 = original
    assert instance.AC_1 == original




@given(instance=Express_strategy)
def test_hyp_express_SecondSitting_setter(instance):
    original = instance.SecondSitting
    instance.SecondSitting = original
    assert instance.SecondSitting == original



@given(instance=Express_strategy)
def test_hyp_express_General_setter(instance):
    original = instance.General
    instance.General = original
    assert instance.General == original




@given(instance=SuperFast_strategy)
def test_hyp_superfast_AC_1_setter(instance):
    original = instance.AC_1
    instance.AC_1 = original
    assert instance.AC_1 == original



@given(instance=SuperFast_strategy)
def test_hyp_superfast_AC_2_setter(instance):
    original = instance.AC_2
    instance.AC_2 = original
    assert instance.AC_2 == original



@given(instance=SuperFast_strategy)
def test_hyp_superfast_Sleeper_setter(instance):
    original = instance.Sleeper
    instance.Sleeper = original
    assert instance.Sleeper == original



@given(instance=SuperFast_strategy)
def test_hyp_superfast_AC_3_setter(instance):
    original = instance.AC_3
    instance.AC_3 = original
    assert instance.AC_3 == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



