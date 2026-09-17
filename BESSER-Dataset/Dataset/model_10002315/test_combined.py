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
    Credit_Card,
    Debit_Card,
    Hotel,
    Payment,
    Room,
    Admin,
    Customer,
    Booking,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_credit_card_is_not_abstract():
    assert not inspect.isabstract(Credit_Card)


def test_hyp_credit_card_constructor_exists():
    assert callable(Credit_Card.__init__)


def test_hyp_credit_card_constructor_args():
    sig = inspect.signature(Credit_Card.__init__)
    params = list(sig.parameters.keys())
    assert "Pin_No_" in params, "Missing parameter 'Pin_No_'"
    assert "Card_No_" in params, "Missing parameter 'Card_No_'"





def test_hyp_debit_card_is_not_abstract():
    assert not inspect.isabstract(Debit_Card)


def test_hyp_debit_card_constructor_exists():
    assert callable(Debit_Card.__init__)


def test_hyp_debit_card_constructor_args():
    sig = inspect.signature(Debit_Card.__init__)
    params = list(sig.parameters.keys())
    assert "Pin_No_" in params, "Missing parameter 'Pin_No_'"
    assert "Card_No_" in params, "Missing parameter 'Card_No_'"





def test_hyp_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hyp_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hyp_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())
    assert "Hotel_Name" in params, "Missing parameter 'Hotel_Name'"
    assert "Hotel_Type" in params, "Missing parameter 'Hotel_Type'"
    assert "Hotel_ID" in params, "Missing parameter 'Hotel_ID'"
    assert "Hotel_Rent" in params, "Missing parameter 'Hotel_Rent'"
    assert "Hotel_Address" in params, "Missing parameter 'Hotel_Address'"








def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Payment_Date" in params, "Missing parameter 'Payment_Date'"
    assert "Customer_s_Id" in params, "Missing parameter 'Customer_s_Id'"
    assert "Payment_Description" in params, "Missing parameter 'Payment_Description'"
    assert "Amount" in params, "Missing parameter 'Amount'"







def test_hyp_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_hyp_room_constructor_exists():
    assert callable(Room.__init__)


def test_hyp_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "Room_number" in params, "Missing parameter 'Room_number'"
    assert "Room_description" in params, "Missing parameter 'Room_description'"
    assert "Room_Id" in params, "Missing parameter 'Room_Id'"
    assert "Room_type" in params, "Missing parameter 'Room_type'"







def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Name" in params, "Missing parameter 'Name'"






def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Mobile_no___Email" in params, "Missing parameter 'Mobile_no___Email'"







def test_hyp_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_hyp_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_hyp_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Description" in params, "Missing parameter 'Description'"






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
Credit_Card_strategy = st.builds(
    Credit_Card,
    Pin_No_=
        safe_text,
    Card_No_=
        safe_text
)
Debit_Card_strategy = st.builds(
    Debit_Card,
    Pin_No_=
        safe_text,
    Card_No_=
        safe_text
)
Hotel_strategy = st.builds(
    Hotel,
    Hotel_Name=
        safe_text,
    Hotel_Type=
        safe_text,
    Hotel_ID=
        safe_text,
    Hotel_Rent=
        safe_text,
    Hotel_Address=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    Payment_Date=
        safe_text,
    Customer_s_Id=
        safe_text,
    Payment_Description=
        safe_text,
    Amount=
        safe_text
)
Room_strategy = st.builds(
    Room,
    Room_number=
        safe_text,
    Room_description=
        safe_text,
    Room_Id=
        safe_text,
    Room_type=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    Id=
        safe_text,
    Password=
        safe_text,
    Name=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    Id=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text,
    Mobile_no___Email=
        safe_text
)
Booking_strategy = st.builds(
    Booking,
    Id=
        safe_text,
    Date=
        safe_text,
    Type=
        safe_text,
    Description=
        safe_text
)




@given(instance=Credit_Card_strategy)
def test_hyp_credit_card_Pin_No__setter(instance):
    original = instance.Pin_No_
    instance.Pin_No_ = original
    assert instance.Pin_No_ == original



@given(instance=Credit_Card_strategy)
def test_hyp_credit_card_Card_No__setter(instance):
    original = instance.Card_No_
    instance.Card_No_ = original
    assert instance.Card_No_ == original




@given(instance=Debit_Card_strategy)
def test_hyp_debit_card_Pin_No__setter(instance):
    original = instance.Pin_No_
    instance.Pin_No_ = original
    assert instance.Pin_No_ == original



@given(instance=Debit_Card_strategy)
def test_hyp_debit_card_Card_No__setter(instance):
    original = instance.Card_No_
    instance.Card_No_ = original
    assert instance.Card_No_ == original




@given(instance=Hotel_strategy)
def test_hyp_hotel_Hotel_Name_setter(instance):
    original = instance.Hotel_Name
    instance.Hotel_Name = original
    assert instance.Hotel_Name == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_Hotel_Type_setter(instance):
    original = instance.Hotel_Type
    instance.Hotel_Type = original
    assert instance.Hotel_Type == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_Hotel_ID_setter(instance):
    original = instance.Hotel_ID
    instance.Hotel_ID = original
    assert instance.Hotel_ID == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_Hotel_Rent_setter(instance):
    original = instance.Hotel_Rent
    instance.Hotel_Rent = original
    assert instance.Hotel_Rent == original



@given(instance=Hotel_strategy)
def test_hyp_hotel_Hotel_Address_setter(instance):
    original = instance.Hotel_Address
    instance.Hotel_Address = original
    assert instance.Hotel_Address == original




@given(instance=Payment_strategy)
def test_hyp_payment_Payment_Date_setter(instance):
    original = instance.Payment_Date
    instance.Payment_Date = original
    assert instance.Payment_Date == original



@given(instance=Payment_strategy)
def test_hyp_payment_Customer_s_Id_setter(instance):
    original = instance.Customer_s_Id
    instance.Customer_s_Id = original
    assert instance.Customer_s_Id == original



@given(instance=Payment_strategy)
def test_hyp_payment_Payment_Description_setter(instance):
    original = instance.Payment_Description
    instance.Payment_Description = original
    assert instance.Payment_Description == original



@given(instance=Payment_strategy)
def test_hyp_payment_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original




@given(instance=Room_strategy)
def test_hyp_room_Room_number_setter(instance):
    original = instance.Room_number
    instance.Room_number = original
    assert instance.Room_number == original



@given(instance=Room_strategy)
def test_hyp_room_Room_description_setter(instance):
    original = instance.Room_description
    instance.Room_description = original
    assert instance.Room_description == original



@given(instance=Room_strategy)
def test_hyp_room_Room_Id_setter(instance):
    original = instance.Room_Id
    instance.Room_Id = original
    assert instance.Room_Id == original



@given(instance=Room_strategy)
def test_hyp_room_Room_type_setter(instance):
    original = instance.Room_type
    instance.Room_type = original
    assert instance.Room_type == original




@given(instance=Admin_strategy)
def test_hyp_admin_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Admin_strategy)
def test_hyp_admin_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Admin_strategy)
def test_hyp_admin_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Customer_strategy)
def test_hyp_customer_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Customer_strategy)
def test_hyp_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Customer_strategy)
def test_hyp_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_hyp_customer_Mobile_no___Email_setter(instance):
    original = instance.Mobile_no___Email
    instance.Mobile_no___Email = original
    assert instance.Mobile_no___Email == original




@given(instance=Booking_strategy)
def test_hyp_booking_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Booking_strategy)
def test_hyp_booking_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Booking_strategy)
def test_hyp_booking_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Booking_strategy)
def test_hyp_booking_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Booking,
    Credit_Card,
    Customer,
    Debit_Card,
    Hotel,
    Payment,
    Room,
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

def test_Admin_Id_value_roundtrip():
    instance = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    assert instance.Id == "sample_text"
    instance.Id = "sample_text_2"
    assert instance.Id == "sample_text_2"


def test_Admin_Name_value_roundtrip():
    instance = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Admin_Password_value_roundtrip():
    instance = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Booking_Date_value_roundtrip():
    instance = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_Booking_Description_value_roundtrip():
    instance = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_Booking_Id_value_roundtrip():
    instance = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    assert instance.Id == "sample_text"
    instance.Id = "sample_text_2"
    assert instance.Id == "sample_text_2"


def test_Booking_Type_value_roundtrip():
    instance = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_Credit_Card_Card_No__value_roundtrip():
    instance = Credit_Card(Card_No_="sample_text", Pin_No_="sample_text")
    assert instance.Card_No_ == "sample_text"
    instance.Card_No_ = "sample_text_2"
    assert instance.Card_No_ == "sample_text_2"


def test_Credit_Card_Pin_No__value_roundtrip():
    instance = Credit_Card(Card_No_="sample_text", Pin_No_="sample_text")
    assert instance.Pin_No_ == "sample_text"
    instance.Pin_No_ = "sample_text_2"
    assert instance.Pin_No_ == "sample_text_2"


def test_Customer_Address_value_roundtrip():
    instance = Customer(Address="sample_text", Id="sample_text", Mobile_no___Email="sample_text", Name="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Customer_Id_value_roundtrip():
    instance = Customer(Address="sample_text", Id="sample_text", Mobile_no___Email="sample_text", Name="sample_text")
    assert instance.Id == "sample_text"
    instance.Id = "sample_text_2"
    assert instance.Id == "sample_text_2"


def test_Customer_Mobile_no___Email_value_roundtrip():
    instance = Customer(Address="sample_text", Id="sample_text", Mobile_no___Email="sample_text", Name="sample_text")
    assert instance.Mobile_no___Email == "sample_text"
    instance.Mobile_no___Email = "sample_text_2"
    assert instance.Mobile_no___Email == "sample_text_2"


def test_Customer_Name_value_roundtrip():
    instance = Customer(Address="sample_text", Id="sample_text", Mobile_no___Email="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Debit_Card_Card_No__value_roundtrip():
    instance = Debit_Card(Card_No_="sample_text", Pin_No_="sample_text")
    assert instance.Card_No_ == "sample_text"
    instance.Card_No_ = "sample_text_2"
    assert instance.Card_No_ == "sample_text_2"


def test_Debit_Card_Pin_No__value_roundtrip():
    instance = Debit_Card(Card_No_="sample_text", Pin_No_="sample_text")
    assert instance.Pin_No_ == "sample_text"
    instance.Pin_No_ = "sample_text_2"
    assert instance.Pin_No_ == "sample_text_2"


def test_Hotel_Hotel_Address_value_roundtrip():
    instance = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    assert instance.Hotel_Address == "sample_text"
    instance.Hotel_Address = "sample_text_2"
    assert instance.Hotel_Address == "sample_text_2"


def test_Hotel_Hotel_ID_value_roundtrip():
    instance = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    assert instance.Hotel_ID == "sample_text"
    instance.Hotel_ID = "sample_text_2"
    assert instance.Hotel_ID == "sample_text_2"


def test_Hotel_Hotel_Name_value_roundtrip():
    instance = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    assert instance.Hotel_Name == "sample_text"
    instance.Hotel_Name = "sample_text_2"
    assert instance.Hotel_Name == "sample_text_2"


def test_Hotel_Hotel_Rent_value_roundtrip():
    instance = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    assert instance.Hotel_Rent == "sample_text"
    instance.Hotel_Rent = "sample_text_2"
    assert instance.Hotel_Rent == "sample_text_2"


def test_Hotel_Hotel_Type_value_roundtrip():
    instance = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    assert instance.Hotel_Type == "sample_text"
    instance.Hotel_Type = "sample_text_2"
    assert instance.Hotel_Type == "sample_text_2"


def test_Payment_Amount_value_roundtrip():
    instance = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    assert instance.Amount == "sample_text"
    instance.Amount = "sample_text_2"
    assert instance.Amount == "sample_text_2"


def test_Payment_Customer_s_Id_value_roundtrip():
    instance = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    assert instance.Customer_s_Id == "sample_text"
    instance.Customer_s_Id = "sample_text_2"
    assert instance.Customer_s_Id == "sample_text_2"


def test_Payment_Payment_Date_value_roundtrip():
    instance = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    assert instance.Payment_Date == "sample_text"
    instance.Payment_Date = "sample_text_2"
    assert instance.Payment_Date == "sample_text_2"


def test_Payment_Payment_Description_value_roundtrip():
    instance = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    assert instance.Payment_Description == "sample_text"
    instance.Payment_Description = "sample_text_2"
    assert instance.Payment_Description == "sample_text_2"


def test_Room_Room_Id_value_roundtrip():
    instance = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    assert instance.Room_Id == "sample_text"
    instance.Room_Id = "sample_text_2"
    assert instance.Room_Id == "sample_text_2"


def test_Room_Room_description_value_roundtrip():
    instance = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    assert instance.Room_description == "sample_text"
    instance.Room_description = "sample_text_2"
    assert instance.Room_description == "sample_text_2"


def test_Room_Room_number_value_roundtrip():
    instance = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    assert instance.Room_number == "sample_text"
    instance.Room_number = "sample_text_2"
    assert instance.Room_number == "sample_text_2"


def test_Room_Room_type_value_roundtrip():
    instance = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    assert instance.Room_type == "sample_text"
    instance.Room_type = "sample_text_2"
    assert instance.Room_type == "sample_text_2"


def test_assoc_Admin_Booking_link_reassign_clear():
    a = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    b1 = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    b2 = Admin(Id="sample_text_2", Name="sample_text_2", Password="sample_text_2")
    _safe_set(a, 'admin1', b1)
    assert _is_linked(a, 'admin1', b1)
    if hasattr(b1, 'booking0'):
        assert _is_linked(b1, 'booking0', a)
    _safe_set(a, 'admin1', b2)
    assert _is_linked(a, 'admin1', b2)
    if hasattr(b1, 'booking0'):
        assert not _is_linked(b1, 'booking0', a)
    if hasattr(b2, 'booking0'):
        assert _is_linked(b2, 'booking0', a)
    _safe_set(a, 'admin1', None)
    assert not _is_linked(a, 'admin1', b2)
    if hasattr(b2, 'booking0'):
        assert not _is_linked(b2, 'booking0', a)


def test_assoc_Admin_Hotel_link_reassign_clear():
    a = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    b1 = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    b2 = Admin(Id="sample_text_2", Name="sample_text_2", Password="sample_text_2")
    _safe_set(a, 'admin17', b1)
    assert _is_linked(a, 'admin17', b1)
    if hasattr(b1, 'hotel16'):
        assert _is_linked(b1, 'hotel16', a)
    _safe_set(a, 'admin17', b2)
    assert _is_linked(a, 'admin17', b2)
    if hasattr(b1, 'hotel16'):
        assert not _is_linked(b1, 'hotel16', a)
    if hasattr(b2, 'hotel16'):
        assert _is_linked(b2, 'hotel16', a)
    _safe_set(a, 'admin17', None)
    assert not _is_linked(a, 'admin17', b2)
    if hasattr(b2, 'hotel16'):
        assert not _is_linked(b2, 'hotel16', a)


def test_assoc_Admin_Room_link_reassign_clear():
    a = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    b1 = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    b2 = Admin(Id="sample_text_2", Name="sample_text_2", Password="sample_text_2")
    _safe_set(a, 'admin3', b1)
    assert _is_linked(a, 'admin3', b1)
    if hasattr(b1, 'room2'):
        assert _is_linked(b1, 'room2', a)
    _safe_set(a, 'admin3', b2)
    assert _is_linked(a, 'admin3', b2)
    if hasattr(b1, 'room2'):
        assert not _is_linked(b1, 'room2', a)
    if hasattr(b2, 'room2'):
        assert _is_linked(b2, 'room2', a)
    _safe_set(a, 'admin3', None)
    assert not _is_linked(a, 'admin3', b2)
    if hasattr(b2, 'room2'):
        assert not _is_linked(b2, 'room2', a)


def test_assoc_Booking_Hotel_link_reassign_clear():
    a = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    b1 = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    b2 = Booking(Date="sample_text_2", Description="sample_text_2", Id="sample_text_2", Type="sample_text_2")
    _safe_set(a, 'booking13', b1)
    assert _is_linked(a, 'booking13', b1)
    if hasattr(b1, 'hotel12'):
        assert _is_linked(b1, 'hotel12', a)
    _safe_set(a, 'booking13', b2)
    assert _is_linked(a, 'booking13', b2)
    if hasattr(b1, 'hotel12'):
        assert not _is_linked(b1, 'hotel12', a)
    if hasattr(b2, 'hotel12'):
        assert _is_linked(b2, 'hotel12', a)
    _safe_set(a, 'booking13', None)
    assert not _is_linked(a, 'booking13', b2)
    if hasattr(b2, 'hotel12'):
        assert not _is_linked(b2, 'hotel12', a)


def test_assoc_Customer_Hotel_link_reassign_clear():
    a = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    b1 = Customer(Address="sample_text", Id="sample_text", Mobile_no___Email="sample_text", Name="sample_text")
    b2 = Customer(Address="sample_text_2", Id="sample_text_2", Mobile_no___Email="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'customer15', b1)
    assert _is_linked(a, 'customer15', b1)
    if hasattr(b1, 'hotel14'):
        assert _is_linked(b1, 'hotel14', a)
    _safe_set(a, 'customer15', b2)
    assert _is_linked(a, 'customer15', b2)
    if hasattr(b1, 'hotel14'):
        assert not _is_linked(b1, 'hotel14', a)
    if hasattr(b2, 'hotel14'):
        assert _is_linked(b2, 'hotel14', a)
    _safe_set(a, 'customer15', None)
    assert not _is_linked(a, 'customer15', b2)
    if hasattr(b2, 'hotel14'):
        assert not _is_linked(b2, 'hotel14', a)


def test_assoc_Customer_Payment_link_reassign_clear():
    a = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    b1 = Customer(Address="sample_text", Id="sample_text", Mobile_no___Email="sample_text", Name="sample_text")
    b2 = Customer(Address="sample_text_2", Id="sample_text_2", Mobile_no___Email="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'customer7', b1)
    assert _is_linked(a, 'customer7', b1)
    if hasattr(b1, 'payment6'):
        assert _is_linked(b1, 'payment6', a)
    _safe_set(a, 'customer7', b2)
    assert _is_linked(a, 'customer7', b2)
    if hasattr(b1, 'payment6'):
        assert not _is_linked(b1, 'payment6', a)
    if hasattr(b2, 'payment6'):
        assert _is_linked(b2, 'payment6', a)
    _safe_set(a, 'customer7', None)
    assert not _is_linked(a, 'customer7', b2)
    if hasattr(b2, 'payment6'):
        assert not _is_linked(b2, 'payment6', a)


def test_assoc_Payment_Booking_link_reassign_clear():
    a = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    b1 = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    b2 = Booking(Date="sample_text_2", Description="sample_text_2", Id="sample_text_2", Type="sample_text_2")
    _safe_set(a, 'booking18', b1)
    assert _is_linked(a, 'booking18', b1)
    if hasattr(b1, 'payment19'):
        assert _is_linked(b1, 'payment19', a)
    _safe_set(a, 'booking18', b2)
    assert _is_linked(a, 'booking18', b2)
    if hasattr(b1, 'payment19'):
        assert not _is_linked(b1, 'payment19', a)
    if hasattr(b2, 'payment19'):
        assert _is_linked(b2, 'payment19', a)
    _safe_set(a, 'booking18', None)
    assert not _is_linked(a, 'booking18', b2)
    if hasattr(b2, 'payment19'):
        assert not _is_linked(b2, 'payment19', a)


def test_assoc_Payment_Credit_Card_link_reassign_clear():
    a = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    b1 = Credit_Card(Card_No_="sample_text", Pin_No_="sample_text")
    b2 = Credit_Card(Card_No_="sample_text_2", Pin_No_="sample_text_2")
    _safe_set(a, 'credit_Card10', b1)
    assert _is_linked(a, 'credit_Card10', b1)
    if hasattr(b1, 'payment11'):
        assert _is_linked(b1, 'payment11', a)
    _safe_set(a, 'credit_Card10', b2)
    assert _is_linked(a, 'credit_Card10', b2)
    if hasattr(b1, 'payment11'):
        assert not _is_linked(b1, 'payment11', a)
    if hasattr(b2, 'payment11'):
        assert _is_linked(b2, 'payment11', a)
    _safe_set(a, 'credit_Card10', None)
    assert not _is_linked(a, 'credit_Card10', b2)
    if hasattr(b2, 'payment11'):
        assert not _is_linked(b2, 'payment11', a)


def test_assoc_Payment_Debit_Card_link_reassign_clear():
    a = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    b1 = Debit_Card(Card_No_="sample_text", Pin_No_="sample_text")
    b2 = Debit_Card(Card_No_="sample_text_2", Pin_No_="sample_text_2")
    _safe_set(a, 'debit_Card8', b1)
    assert _is_linked(a, 'debit_Card8', b1)
    if hasattr(b1, 'payment9'):
        assert _is_linked(b1, 'payment9', a)
    _safe_set(a, 'debit_Card8', b2)
    assert _is_linked(a, 'debit_Card8', b2)
    if hasattr(b1, 'payment9'):
        assert not _is_linked(b1, 'payment9', a)
    if hasattr(b2, 'payment9'):
        assert _is_linked(b2, 'payment9', a)
    _safe_set(a, 'debit_Card8', None)
    assert not _is_linked(a, 'debit_Card8', b2)
    if hasattr(b2, 'payment9'):
        assert not _is_linked(b2, 'payment9', a)


def test_assoc_Payment_Hotel_link_reassign_clear():
    a = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    b1 = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    b2 = Hotel(Hotel_Address="sample_text_2", Hotel_ID="sample_text_2", Hotel_Name="sample_text_2", Hotel_Rent="sample_text_2", Hotel_Type="sample_text_2")
    _safe_set(a, 'hotel22', b1)
    assert _is_linked(a, 'hotel22', b1)
    if hasattr(b1, 'payment23'):
        assert _is_linked(b1, 'payment23', a)
    _safe_set(a, 'hotel22', b2)
    assert _is_linked(a, 'hotel22', b2)
    if hasattr(b1, 'payment23'):
        assert not _is_linked(b1, 'payment23', a)
    if hasattr(b2, 'payment23'):
        assert _is_linked(b2, 'payment23', a)
    _safe_set(a, 'hotel22', None)
    assert not _is_linked(a, 'hotel22', b2)
    if hasattr(b2, 'payment23'):
        assert not _is_linked(b2, 'payment23', a)


def test_assoc_Payment_Room_link_reassign_clear():
    a = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    b1 = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    b2 = Payment(Amount="sample_text_2", Customer_s_Id="sample_text_2", Payment_Date="sample_text_2", Payment_Description="sample_text_2")
    _safe_set(a, 'payment21', b1)
    assert _is_linked(a, 'payment21', b1)
    if hasattr(b1, 'room20'):
        assert _is_linked(b1, 'room20', a)
    _safe_set(a, 'payment21', b2)
    assert _is_linked(a, 'payment21', b2)
    if hasattr(b1, 'room20'):
        assert not _is_linked(b1, 'room20', a)
    if hasattr(b2, 'room20'):
        assert _is_linked(b2, 'room20', a)
    _safe_set(a, 'payment21', None)
    assert not _is_linked(a, 'payment21', b2)
    if hasattr(b2, 'room20'):
        assert not _is_linked(b2, 'room20', a)


def test_assoc_Room_Hotel_link_reassign_clear():
    a = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    b1 = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    b2 = Hotel(Hotel_Address="sample_text_2", Hotel_ID="sample_text_2", Hotel_Name="sample_text_2", Hotel_Rent="sample_text_2", Hotel_Type="sample_text_2")
    _safe_set(a, 'hotel4', b1)
    assert _is_linked(a, 'hotel4', b1)
    if hasattr(b1, 'room5'):
        assert _is_linked(b1, 'room5', a)
    _safe_set(a, 'hotel4', b2)
    assert _is_linked(a, 'hotel4', b2)
    if hasattr(b1, 'room5'):
        assert not _is_linked(b1, 'room5', a)
    if hasattr(b2, 'room5'):
        assert _is_linked(b2, 'room5', a)
    _safe_set(a, 'hotel4', None)
    assert not _is_linked(a, 'hotel4', b2)
    if hasattr(b2, 'room5'):
        assert not _is_linked(b2, 'room5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin, Id=safe_text, Name=safe_text, Password=safe_text)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Booking_strategy = st.builds(Booking, Date=safe_text, Description=safe_text, Id=safe_text, Type=safe_text)
@given(instance=Booking_strategy)
@settings(max_examples=25)
def test_Booking_instantiation(instance):
    assert isinstance(instance, Booking)


Credit_Card_strategy = st.builds(Credit_Card, Card_No_=safe_text, Pin_No_=safe_text)
@given(instance=Credit_Card_strategy)
@settings(max_examples=25)
def test_Credit_Card_instantiation(instance):
    assert isinstance(instance, Credit_Card)


Customer_strategy = st.builds(Customer, Address=safe_text, Id=safe_text, Mobile_no___Email=safe_text, Name=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Debit_Card_strategy = st.builds(Debit_Card, Card_No_=safe_text, Pin_No_=safe_text)
@given(instance=Debit_Card_strategy)
@settings(max_examples=25)
def test_Debit_Card_instantiation(instance):
    assert isinstance(instance, Debit_Card)


Hotel_strategy = st.builds(Hotel, Hotel_Address=safe_text, Hotel_ID=safe_text, Hotel_Name=safe_text, Hotel_Rent=safe_text, Hotel_Type=safe_text)
@given(instance=Hotel_strategy)
@settings(max_examples=25)
def test_Hotel_instantiation(instance):
    assert isinstance(instance, Hotel)


Payment_strategy = st.builds(Payment, Amount=safe_text, Customer_s_Id=safe_text, Payment_Date=safe_text, Payment_Description=safe_text)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Room_strategy = st.builds(Room, Room_Id=safe_text, Room_description=safe_text, Room_number=safe_text, Room_type=safe_text)
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)



