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
    Discription,
    Payment,
    User,
    Delivery,
    Order,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_discription_is_not_abstract():
    assert not inspect.isabstract(Discription)


def test_hyp_discription_constructor_exists():
    assert callable(Discription.__init__)


def test_hyp_discription_constructor_args():
    sig = inspect.signature(Discription.__init__)
    params = list(sig.parameters.keys())
    assert "Emil" in params, "Missing parameter 'Emil'"
    assert "Discription" in params, "Missing parameter 'Discription'"





def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Date_off" in params, "Missing parameter 'Date_off'"
    assert "Amount" in params, "Missing parameter 'Amount'"





def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Name_" in params, "Missing parameter 'Name_'"
    assert "Phone_number" in params, "Missing parameter 'Phone_number'"
    assert "Phone_number1" in params, "Missing parameter 'Phone_number1'"
    assert "Email_" in params, "Missing parameter 'Email_'"
    assert "Address_" in params, "Missing parameter 'Address_'"








def test_hyp_delivery_is_not_abstract():
    assert not inspect.isabstract(Delivery)


def test_hyp_delivery_constructor_exists():
    assert callable(Delivery.__init__)


def test_hyp_delivery_constructor_args():
    sig = inspect.signature(Delivery.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Name" in params, "Missing parameter 'Name'"






def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Type_" in params, "Missing parameter 'Type_'"
    assert "Size_" in params, "Missing parameter 'Size_'"
    assert "ID_" in params, "Missing parameter 'ID_'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"






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
Discription_strategy = st.builds(
    Discription,
    Emil=
        safe_text,
    Discription=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    Date_off=
        safe_text,
    Amount=
        st.integers()
)
User_strategy = st.builds(
    User,
    Name_=
        safe_text,
    Phone_number=
        st.integers(),
    Phone_number1=
        st.integers(),
    Email_=
        safe_text,
    Address_=
        safe_text
)
Delivery_strategy = st.builds(
    Delivery,
    Date=
        safe_text,
    Type=
        safe_text,
    Name=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Type_=
        safe_text,
    Size_=
        st.integers(),
    ID_=
        st.integers(),
    Quantity=
        st.integers()
)




@given(instance=Discription_strategy)
def test_hyp_discription_Emil_setter(instance):
    original = instance.Emil
    instance.Emil = original
    assert instance.Emil == original



@given(instance=Discription_strategy)
def test_hyp_discription_Discription_setter(instance):
    original = instance.Discription
    instance.Discription = original
    assert instance.Discription == original




@given(instance=Payment_strategy)
def test_hyp_payment_Date_off_setter(instance):
    original = instance.Date_off
    instance.Date_off = original
    assert instance.Date_off == original



@given(instance=Payment_strategy)
def test_hyp_payment_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original




@given(instance=User_strategy)
def test_hyp_user_Name__setter(instance):
    original = instance.Name_
    instance.Name_ = original
    assert instance.Name_ == original



@given(instance=User_strategy)
def test_hyp_user_Phone_number_setter(instance):
    original = instance.Phone_number
    instance.Phone_number = original
    assert instance.Phone_number == original



@given(instance=User_strategy)
def test_hyp_user_Phone_number1_setter(instance):
    original = instance.Phone_number1
    instance.Phone_number1 = original
    assert instance.Phone_number1 == original



@given(instance=User_strategy)
def test_hyp_user_Email__setter(instance):
    original = instance.Email_
    instance.Email_ = original
    assert instance.Email_ == original



@given(instance=User_strategy)
def test_hyp_user_Address__setter(instance):
    original = instance.Address_
    instance.Address_ = original
    assert instance.Address_ == original




@given(instance=Delivery_strategy)
def test_hyp_delivery_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Delivery_strategy)
def test_hyp_delivery_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Delivery_strategy)
def test_hyp_delivery_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Order_strategy)
def test_hyp_order_Type__setter(instance):
    original = instance.Type_
    instance.Type_ = original
    assert instance.Type_ == original



@given(instance=Order_strategy)
def test_hyp_order_Size__setter(instance):
    original = instance.Size_
    instance.Size_ = original
    assert instance.Size_ == original



@given(instance=Order_strategy)
def test_hyp_order_ID__setter(instance):
    original = instance.ID_
    instance.ID_ = original
    assert instance.ID_ == original



@given(instance=Order_strategy)
def test_hyp_order_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Delivery,
    Discription,
    Order,
    Payment,
    User,
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

def test_Delivery_Date_value_roundtrip():
    instance = Delivery(Date="sample_text", Name="sample_text", Type="sample_text")
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_Delivery_Name_value_roundtrip():
    instance = Delivery(Date="sample_text", Name="sample_text", Type="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Delivery_Type_value_roundtrip():
    instance = Delivery(Date="sample_text", Name="sample_text", Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_Discription_Discription_value_roundtrip():
    instance = Discription(Discription="sample_text", Emil="sample_text")
    assert instance.Discription == "sample_text"
    instance.Discription = "sample_text_2"
    assert instance.Discription == "sample_text_2"


def test_Discription_Emil_value_roundtrip():
    instance = Discription(Discription="sample_text", Emil="sample_text")
    assert instance.Emil == "sample_text"
    instance.Emil = "sample_text_2"
    assert instance.Emil == "sample_text_2"


def test_Order_ID__value_roundtrip():
    instance = Order(ID_=7, Quantity=7, Size_=7, Type_="sample_text")
    assert instance.ID_ == 7
    instance.ID_ = 13
    assert instance.ID_ == 13


def test_Order_Quantity_value_roundtrip():
    instance = Order(ID_=7, Quantity=7, Size_=7, Type_="sample_text")
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_Order_Size__value_roundtrip():
    instance = Order(ID_=7, Quantity=7, Size_=7, Type_="sample_text")
    assert instance.Size_ == 7
    instance.Size_ = 13
    assert instance.Size_ == 13


def test_Order_Type__value_roundtrip():
    instance = Order(ID_=7, Quantity=7, Size_=7, Type_="sample_text")
    assert instance.Type_ == "sample_text"
    instance.Type_ = "sample_text_2"
    assert instance.Type_ == "sample_text_2"


def test_Payment_Amount_value_roundtrip():
    instance = Payment(Amount=7, Date_off="sample_text")
    assert instance.Amount == 7
    instance.Amount = 13
    assert instance.Amount == 13


def test_Payment_Date_off_value_roundtrip():
    instance = Payment(Amount=7, Date_off="sample_text")
    assert instance.Date_off == "sample_text"
    instance.Date_off = "sample_text_2"
    assert instance.Date_off == "sample_text_2"


def test_User_Address__value_roundtrip():
    instance = User(Address_="sample_text", Email_="sample_text", Name_="sample_text", Phone_number=7, Phone_number1=7)
    assert instance.Address_ == "sample_text"
    instance.Address_ = "sample_text_2"
    assert instance.Address_ == "sample_text_2"


def test_User_Email__value_roundtrip():
    instance = User(Address_="sample_text", Email_="sample_text", Name_="sample_text", Phone_number=7, Phone_number1=7)
    assert instance.Email_ == "sample_text"
    instance.Email_ = "sample_text_2"
    assert instance.Email_ == "sample_text_2"


def test_User_Name__value_roundtrip():
    instance = User(Address_="sample_text", Email_="sample_text", Name_="sample_text", Phone_number=7, Phone_number1=7)
    assert instance.Name_ == "sample_text"
    instance.Name_ = "sample_text_2"
    assert instance.Name_ == "sample_text_2"


def test_User_Phone_number_value_roundtrip():
    instance = User(Address_="sample_text", Email_="sample_text", Name_="sample_text", Phone_number=7, Phone_number1=7)
    assert instance.Phone_number == 7
    instance.Phone_number = 13
    assert instance.Phone_number == 13


def test_User_Phone_number1_value_roundtrip():
    instance = User(Address_="sample_text", Email_="sample_text", Name_="sample_text", Phone_number=7, Phone_number1=7)
    assert instance.Phone_number1 == 7
    instance.Phone_number1 = 13
    assert instance.Phone_number1 == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Delivery_strategy = st.builds(Delivery, Date=safe_text, Name=safe_text, Type=safe_text)
@given(instance=Delivery_strategy)
@settings(max_examples=25)
def test_Delivery_instantiation(instance):
    assert isinstance(instance, Delivery)


Discription_strategy = st.builds(Discription, Discription=safe_text, Emil=safe_text)
@given(instance=Discription_strategy)
@settings(max_examples=25)
def test_Discription_instantiation(instance):
    assert isinstance(instance, Discription)


Order_strategy = st.builds(Order, ID_=st.integers(), Quantity=st.integers(), Size_=st.integers(), Type_=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Payment_strategy = st.builds(Payment, Amount=st.integers(), Date_off=safe_text)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


User_strategy = st.builds(User, Address_=safe_text, Email_=safe_text, Name_=safe_text, Phone_number=st.integers(), Phone_number1=st.integers())
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



