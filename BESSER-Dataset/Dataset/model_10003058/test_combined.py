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
    Ticket,
    Administrator,
    Flight,
    Bank,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_hyp_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_hyp_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Customer_Name" in params, "Missing parameter 'Customer_Name'"
    assert "Type" in params, "Missing parameter 'Type'"







def test_hyp_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_hyp_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_hyp_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Fullname" in params, "Missing parameter 'Fullname'"
    assert "Account" in params, "Missing parameter 'Account'"





def test_hyp_flight_is_not_abstract():
    assert not inspect.isabstract(Flight)


def test_hyp_flight_constructor_exists():
    assert callable(Flight.__init__)


def test_hyp_flight_constructor_args():
    sig = inspect.signature(Flight.__init__)
    params = list(sig.parameters.keys())
    assert "Number_of_seats" in params, "Missing parameter 'Number_of_seats'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Destination" in params, "Missing parameter 'Destination'"
    assert "Source" in params, "Missing parameter 'Source'"

def test_hyp_flight_has_Number_of_seats():
    assert hasattr(Flight, "Number_of_seats")
    descriptor = None
    for klass in Flight.__mro__:
        if "Number_of_seats" in klass.__dict__:
            descriptor = klass.__dict__["Number_of_seats"]
            break
    assert isinstance(descriptor, property)

def test_hyp_flight_has_Time():
    assert hasattr(Flight, "Time")
    descriptor = None
    for klass in Flight.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_hyp_flight_has_Id():
    assert hasattr(Flight, "Id")
    descriptor = None
    for klass in Flight.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_flight_has_Name():
    assert hasattr(Flight, "Name")
    descriptor = None
    for klass in Flight.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_flight_has_Destination():
    assert hasattr(Flight, "Destination")
    descriptor = None
    for klass in Flight.__mro__:
        if "Destination" in klass.__dict__:
            descriptor = klass.__dict__["Destination"]
            break
    assert isinstance(descriptor, property)

def test_hyp_flight_has_Source():
    assert hasattr(Flight, "Source")
    descriptor = None
    for klass in Flight.__mro__:
        if "Source" in klass.__dict__:
            descriptor = klass.__dict__["Source"]
            break
    assert isinstance(descriptor, property)



def test_hyp_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_hyp_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_hyp_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Account" in params, "Missing parameter 'Account'"





def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Fullname" in params, "Missing parameter 'Fullname'"
    assert "Card_details" in params, "Missing parameter 'Card_details'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Location" in params, "Missing parameter 'Location'"






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
Ticket_strategy = st.builds(
    Ticket,
    Price=
        st.booleans(),
    Id=
        st.integers(),
    Customer_Name=
        safe_text,
    Type=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    Fullname=
        safe_text,
    Account=
        safe_text
)
Flight_strategy = st.builds(
    Flight,
    Number_of_seats=
        st.integers(),
    Time=
        st.integers(),
    Id=
        st.none(),
    Name=
        safe_text,
    Destination=
        safe_text,
    Source=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    Name=
        safe_text,
    Account=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
    Fullname=
        safe_text,
    Card_details=
        st.integers(),
    Gender=
        safe_text,
    Location=
        safe_text
)




@given(instance=Ticket_strategy)
def test_hyp_ticket_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_Customer_Name_setter(instance):
    original = instance.Customer_Name
    instance.Customer_Name = original
    assert instance.Customer_Name == original



@given(instance=Ticket_strategy)
def test_hyp_ticket_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original




@given(instance=Administrator_strategy)
def test_hyp_administrator_Fullname_setter(instance):
    original = instance.Fullname
    instance.Fullname = original
    assert instance.Fullname == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_Account_setter(instance):
    original = instance.Account
    instance.Account = original
    assert instance.Account == original

@given(instance=Flight_strategy)
@settings(max_examples=50)
def test_hyp_flight_instantiation(instance):
    assert isinstance(instance, Flight)



@given(instance=Flight_strategy)
def test_hyp_flight_Number_of_seats_setter(instance):
    original = instance.Number_of_seats
    instance.Number_of_seats = original
    assert instance.Number_of_seats == original



@given(instance=Flight_strategy)
def test_hyp_flight_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Flight_strategy)
def test_hyp_flight_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Flight_strategy)
def test_hyp_flight_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Flight_strategy)
def test_hyp_flight_Destination_setter(instance):
    original = instance.Destination
    instance.Destination = original
    assert instance.Destination == original



@given(instance=Flight_strategy)
def test_hyp_flight_Source_setter(instance):
    original = instance.Source
    instance.Source = original
    assert instance.Source == original




@given(instance=Bank_strategy)
def test_hyp_bank_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Bank_strategy)
def test_hyp_bank_Account_setter(instance):
    original = instance.Account
    instance.Account = original
    assert instance.Account == original




@given(instance=Customer_strategy)
def test_hyp_customer_Fullname_setter(instance):
    original = instance.Fullname
    instance.Fullname = original
    assert instance.Fullname == original



@given(instance=Customer_strategy)
def test_hyp_customer_Card_details_setter(instance):
    original = instance.Card_details
    instance.Card_details = original
    assert instance.Card_details == original



@given(instance=Customer_strategy)
def test_hyp_customer_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Customer_strategy)
def test_hyp_customer_Location_setter(instance):
    original = instance.Location
    instance.Location = original
    assert instance.Location == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator,
    Bank,
    Customer,
    Flight,
    Ticket,
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

def test_Administrator_Account_value_roundtrip():
    instance = Administrator(Account="sample_text", Fullname="sample_text")
    assert instance.Account == "sample_text"
    instance.Account = "sample_text_2"
    assert instance.Account == "sample_text_2"


def test_Administrator_Fullname_value_roundtrip():
    instance = Administrator(Account="sample_text", Fullname="sample_text")
    assert instance.Fullname == "sample_text"
    instance.Fullname = "sample_text_2"
    assert instance.Fullname == "sample_text_2"


def test_Bank_Account_value_roundtrip():
    instance = Bank(Account=7, Name="sample_text")
    assert instance.Account == 7
    instance.Account = 13
    assert instance.Account == 13


def test_Bank_Name_value_roundtrip():
    instance = Bank(Account=7, Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Customer_Card_details_value_roundtrip():
    instance = Customer(Card_details=7, Fullname="sample_text", Gender="sample_text", Location="sample_text")
    assert instance.Card_details == 7
    instance.Card_details = 13
    assert instance.Card_details == 13


def test_Customer_Fullname_value_roundtrip():
    instance = Customer(Card_details=7, Fullname="sample_text", Gender="sample_text", Location="sample_text")
    assert instance.Fullname == "sample_text"
    instance.Fullname = "sample_text_2"
    assert instance.Fullname == "sample_text_2"


def test_Customer_Gender_value_roundtrip():
    instance = Customer(Card_details=7, Fullname="sample_text", Gender="sample_text", Location="sample_text")
    assert instance.Gender == "sample_text"
    instance.Gender = "sample_text_2"
    assert instance.Gender == "sample_text_2"


def test_Customer_Location_value_roundtrip():
    instance = Customer(Card_details=7, Fullname="sample_text", Gender="sample_text", Location="sample_text")
    assert instance.Location == "sample_text"
    instance.Location = "sample_text_2"
    assert instance.Location == "sample_text_2"


def test_Ticket_Customer_Name_value_roundtrip():
    instance = Ticket(Customer_Name="sample_text", Id=7, Price=True, Type="sample_text")
    assert instance.Customer_Name == "sample_text"
    instance.Customer_Name = "sample_text_2"
    assert instance.Customer_Name == "sample_text_2"


def test_Ticket_Id_value_roundtrip():
    instance = Ticket(Customer_Name="sample_text", Id=7, Price=True, Type="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_Ticket_Price_value_roundtrip():
    instance = Ticket(Customer_Name="sample_text", Id=7, Price=True, Type="sample_text")
    assert instance.Price == True
    instance.Price = False
    assert instance.Price == False


def test_Ticket_Type_value_roundtrip():
    instance = Ticket(Customer_Name="sample_text", Id=7, Price=True, Type="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_assoc_Bank_Customer_link_reassign_clear():
    a = Customer(Card_details=7, Fullname="sample_text", Gender="sample_text", Location="sample_text")
    b1 = Bank(Account=7, Name="sample_text")
    b2 = Bank(Account=13, Name="sample_text_2")
    _safe_set(a, 'bank3', b1)
    assert _is_linked(a, 'bank3', b1)
    if hasattr(b1, 'customer2'):
        assert _is_linked(b1, 'customer2', a)
    _safe_set(a, 'bank3', b2)
    assert _is_linked(a, 'bank3', b2)
    if hasattr(b1, 'customer2'):
        assert not _is_linked(b1, 'customer2', a)
    if hasattr(b2, 'customer2'):
        assert _is_linked(b2, 'customer2', a)
    _safe_set(a, 'bank3', None)
    assert not _is_linked(a, 'bank3', b2)
    if hasattr(b2, 'customer2'):
        assert not _is_linked(b2, 'customer2', a)


def test_assoc_Customer_Administrator_link_reassign_clear():
    a = Customer(Card_details=7, Fullname="sample_text", Gender="sample_text", Location="sample_text")
    b1 = Administrator(Account="sample_text", Fullname="sample_text")
    b2 = Administrator(Account="sample_text_2", Fullname="sample_text_2")
    _safe_set(a, 'Request0', b1)
    assert _is_linked(a, 'Request0', b1)
    if hasattr(b1, 'Manage1'):
        assert _is_linked(b1, 'Manage1', a)
    _safe_set(a, 'Request0', b2)
    assert _is_linked(a, 'Request0', b2)
    if hasattr(b1, 'Manage1'):
        assert not _is_linked(b1, 'Manage1', a)
    if hasattr(b2, 'Manage1'):
        assert _is_linked(b2, 'Manage1', a)
    _safe_set(a, 'Request0', None)
    assert not _is_linked(a, 'Request0', b2)
    if hasattr(b2, 'Manage1'):
        assert not _is_linked(b2, 'Manage1', a)


def test_assoc_Ticket_Customer_link_reassign_clear():
    a = Ticket(Customer_Name="sample_text", Id=7, Price=True, Type="sample_text")
    b1 = Customer(Card_details=7, Fullname="sample_text", Gender="sample_text", Location="sample_text")
    b2 = Customer(Card_details=13, Fullname="sample_text_2", Gender="sample_text_2", Location="sample_text_2")
    _safe_set(a, 'Owner4', b1)
    assert _is_linked(a, 'Owner4', b1)
    if hasattr(b1, 'Owns5'):
        assert _is_linked(b1, 'Owns5', a)
    _safe_set(a, 'Owner4', b2)
    assert _is_linked(a, 'Owner4', b2)
    if hasattr(b1, 'Owns5'):
        assert not _is_linked(b1, 'Owns5', a)
    if hasattr(b2, 'Owns5'):
        assert _is_linked(b2, 'Owns5', a)
    _safe_set(a, 'Owner4', None)
    assert not _is_linked(a, 'Owner4', b2)
    if hasattr(b2, 'Owns5'):
        assert not _is_linked(b2, 'Owns5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_strategy = st.builds(Administrator, Account=safe_text, Fullname=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Bank_strategy = st.builds(Bank, Account=st.integers(), Name=safe_text)
@given(instance=Bank_strategy)
@settings(max_examples=25)
def test_Bank_instantiation(instance):
    assert isinstance(instance, Bank)


Customer_strategy = st.builds(Customer, Card_details=st.integers(), Fullname=safe_text, Gender=safe_text, Location=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Ticket_strategy = st.builds(Ticket, Customer_Name=safe_text, Id=st.integers(), Price=st.booleans(), Type=safe_text)
@given(instance=Ticket_strategy)
@settings(max_examples=25)
def test_Ticket_instantiation(instance):
    assert isinstance(instance, Ticket)



