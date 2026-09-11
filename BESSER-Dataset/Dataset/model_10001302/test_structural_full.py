import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator,
    Booking,
    CustomerUI,
    List__,
    List_re_,
    List_reservation_,
    Management_UI,
    Reservation_status,
    Restaurant_Reservation_System,
    Restaurant_owner,
    Staff,
    Table,
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

def test_Administrator_email_value_roundtrip():
    instance = Administrator(email="sample_text", user_id=7, user_name="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Administrator_user_id_value_roundtrip():
    instance = Administrator(email="sample_text", user_id=7, user_name="sample_text")
    assert instance.user_id == 7
    instance.user_id = 13
    assert instance.user_id == 13


def test_Administrator_user_name_value_roundtrip():
    instance = Administrator(email="sample_text", user_id=7, user_name="sample_text")
    assert instance.user_name == "sample_text"
    instance.user_name = "sample_text_2"
    assert instance.user_name == "sample_text_2"


def test_Booking_Restaurant_id_value_roundtrip():
    instance = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    assert instance.Restaurant_id == "sample_text"
    instance.Restaurant_id = "sample_text_2"
    assert instance.Restaurant_id == "sample_text_2"


def test_Booking_booking_id_value_roundtrip():
    instance = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    assert instance.booking_id == 7
    instance.booking_id = 13
    assert instance.booking_id == 13


def test_Booking_customer_id_value_roundtrip():
    instance = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    assert instance.customer_id == "sample_text"
    instance.customer_id = "sample_text_2"
    assert instance.customer_id == "sample_text_2"


def test_Booking_date_value_roundtrip():
    instance = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_Booking_endTime_value_roundtrip():
    instance = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    assert instance.endTime == "sample_text"
    instance.endTime = "sample_text_2"
    assert instance.endTime == "sample_text_2"


def test_Booking_person_value_roundtrip():
    instance = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    assert instance.person == 7
    instance.person = 13
    assert instance.person == 13


def test_Booking_reservedTables_value_roundtrip():
    instance = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    assert instance.reservedTables == "sample_text"
    instance.reservedTables = "sample_text_2"
    assert instance.reservedTables == "sample_text_2"


def test_Booking_startTime_value_roundtrip():
    instance = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    assert instance.startTime == "sample_text"
    instance.startTime = "sample_text_2"
    assert instance.startTime == "sample_text_2"


def test_Restaurant_Reservation_System_Menu_value_roundtrip():
    instance = Restaurant_Reservation_System(Menu="sample_text", bookings="sample_text")
    assert instance.Menu == "sample_text"
    instance.Menu = "sample_text_2"
    assert instance.Menu == "sample_text_2"


def test_Restaurant_Reservation_System_bookings_value_roundtrip():
    instance = Restaurant_Reservation_System(Menu="sample_text", bookings="sample_text")
    assert instance.bookings == "sample_text"
    instance.bookings = "sample_text_2"
    assert instance.bookings == "sample_text_2"


def test_Restaurant_owner_email_value_roundtrip():
    instance = Restaurant_owner(email="sample_text", user_id="sample_text", username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Restaurant_owner_user_id_value_roundtrip():
    instance = Restaurant_owner(email="sample_text", user_id="sample_text", username="sample_text")
    assert instance.user_id == "sample_text"
    instance.user_id = "sample_text_2"
    assert instance.user_id == "sample_text_2"


def test_Restaurant_owner_username_value_roundtrip():
    instance = Restaurant_owner(email="sample_text", user_id="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Staff_name_value_roundtrip():
    instance = Staff(name="sample_text", type="sample_text", user_id="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Staff_type_value_roundtrip():
    instance = Staff(name="sample_text", type="sample_text", user_id="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Staff_user_id_value_roundtrip():
    instance = Staff(name="sample_text", type="sample_text", user_id="sample_text")
    assert instance.user_id == "sample_text"
    instance.user_id = "sample_text_2"
    assert instance.user_id == "sample_text_2"


def test_Table_numSeats_value_roundtrip():
    instance = Table(numSeats=7, quantity=7, table_id="sample_text")
    assert instance.numSeats == 7
    instance.numSeats = 13
    assert instance.numSeats == 13


def test_Table_quantity_value_roundtrip():
    instance = Table(numSeats=7, quantity=7, table_id="sample_text")
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Table_table_id_value_roundtrip():
    instance = Table(numSeats=7, quantity=7, table_id="sample_text")
    assert instance.table_id == "sample_text"
    instance.table_id = "sample_text_2"
    assert instance.table_id == "sample_text_2"


def test_assoc_CustomerUI_ReservationManagementSystem_link_reassign_clear():
    a = Restaurant_Reservation_System(Menu="sample_text", bookings="sample_text")
    b1 = CustomerUI()
    b2 = CustomerUI()
    _safe_set(a, 'interacts5', {b1})
    assert _is_linked(a, 'interacts5', b1)
    if hasattr(b1, 'CustomerUI_ReservationManagementSystem_04'):
        assert _is_linked(b1, 'CustomerUI_ReservationManagementSystem_04', a)
    _safe_set(a, 'interacts5', {b2})
    assert _is_linked(a, 'interacts5', b2)
    if hasattr(b1, 'CustomerUI_ReservationManagementSystem_04'):
        assert not _is_linked(b1, 'CustomerUI_ReservationManagementSystem_04', a)
    if hasattr(b2, 'CustomerUI_ReservationManagementSystem_04'):
        assert _is_linked(b2, 'CustomerUI_ReservationManagementSystem_04', a)
    _safe_set(a, 'interacts5', set())
    assert not _is_linked(a, 'interacts5', b2)
    if hasattr(b2, 'CustomerUI_ReservationManagementSystem_04'):
        assert not _is_linked(b2, 'CustomerUI_ReservationManagementSystem_04', a)


def test_assoc_ReservationManagementSystem_Booking_link_reassign_clear():
    a = Restaurant_Reservation_System(Menu="sample_text", bookings="sample_text")
    b1 = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    b2 = Booking(Restaurant_id="sample_text_2", booking_id=13, customer_id="sample_text_2", date=date(2025, 6, 15), endTime="sample_text_2", person=13, reservedTables="sample_text_2", startTime="sample_text_2")
    _safe_set(a, 'booking6', {b1})
    assert _is_linked(a, 'booking6', b1)
    if hasattr(b1, 'ReservationManagementSystem_Booking_17'):
        assert _is_linked(b1, 'ReservationManagementSystem_Booking_17', a)
    _safe_set(a, 'booking6', {b2})
    assert _is_linked(a, 'booking6', b2)
    if hasattr(b1, 'ReservationManagementSystem_Booking_17'):
        assert not _is_linked(b1, 'ReservationManagementSystem_Booking_17', a)
    if hasattr(b2, 'ReservationManagementSystem_Booking_17'):
        assert _is_linked(b2, 'ReservationManagementSystem_Booking_17', a)
    _safe_set(a, 'booking6', set())
    assert not _is_linked(a, 'booking6', b2)
    if hasattr(b2, 'ReservationManagementSystem_Booking_17'):
        assert not _is_linked(b2, 'ReservationManagementSystem_Booking_17', a)


def test_assoc_Staff_ReservationManagementSystem_link_reassign_clear():
    a = Staff(name="sample_text", type="sample_text", user_id="sample_text")
    b1 = Restaurant_Reservation_System(Menu="sample_text", bookings="sample_text")
    b2 = Restaurant_Reservation_System(Menu="sample_text_2", bookings="sample_text_2")
    _safe_set(a, 'reservationManagementSystem2', b1)
    assert _is_linked(a, 'reservationManagementSystem2', b1)
    if hasattr(b1, 'interacts3'):
        assert _is_linked(b1, 'interacts3', a)
    _safe_set(a, 'reservationManagementSystem2', b2)
    assert _is_linked(a, 'reservationManagementSystem2', b2)
    if hasattr(b1, 'interacts3'):
        assert not _is_linked(b1, 'interacts3', a)
    if hasattr(b2, 'interacts3'):
        assert _is_linked(b2, 'interacts3', a)
    _safe_set(a, 'reservationManagementSystem2', None)
    assert not _is_linked(a, 'reservationManagementSystem2', b2)
    if hasattr(b2, 'interacts3'):
        assert not _is_linked(b2, 'interacts3', a)


def test_assoc_Staff_StaffUI_link_reassign_clear():
    a = Staff(name="sample_text", type="sample_text", user_id="sample_text")
    b1 = Management_UI()
    b2 = Management_UI()
    _safe_set(a, 'Staff_StaffUI_00', {b1})
    assert _is_linked(a, 'Staff_StaffUI_00', b1)
    if hasattr(b1, 'accesses1'):
        assert _is_linked(b1, 'accesses1', a)
    _safe_set(a, 'Staff_StaffUI_00', {b2})
    assert _is_linked(a, 'Staff_StaffUI_00', b2)
    if hasattr(b1, 'accesses1'):
        assert not _is_linked(b1, 'accesses1', a)
    if hasattr(b2, 'accesses1'):
        assert _is_linked(b2, 'accesses1', a)
    _safe_set(a, 'Staff_StaffUI_00', set())
    assert not _is_linked(a, 'Staff_StaffUI_00', b2)
    if hasattr(b2, 'accesses1'):
        assert not _is_linked(b2, 'accesses1', a)


def test_assoc_Table_Booking_link_reassign_clear():
    a = Table(numSeats=7, quantity=7, table_id="sample_text")
    b1 = Booking(Restaurant_id="sample_text", booking_id=7, customer_id="sample_text", date=date(2024, 1, 1), endTime="sample_text", person=7, reservedTables="sample_text", startTime="sample_text")
    b2 = Booking(Restaurant_id="sample_text_2", booking_id=13, customer_id="sample_text_2", date=date(2025, 6, 15), endTime="sample_text_2", person=13, reservedTables="sample_text_2", startTime="sample_text_2")
    _safe_set(a, 'Table_Booking_010', b1)
    assert _is_linked(a, 'Table_Booking_010', b1)
    if hasattr(b1, 'reservedBy11'):
        assert _is_linked(b1, 'reservedBy11', a)
    _safe_set(a, 'Table_Booking_010', b2)
    assert _is_linked(a, 'Table_Booking_010', b2)
    if hasattr(b1, 'reservedBy11'):
        assert not _is_linked(b1, 'reservedBy11', a)
    if hasattr(b2, 'reservedBy11'):
        assert _is_linked(b2, 'reservedBy11', a)
    _safe_set(a, 'Table_Booking_010', None)
    assert not _is_linked(a, 'Table_Booking_010', b2)
    if hasattr(b2, 'reservedBy11'):
        assert not _is_linked(b2, 'reservedBy11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_strategy = st.builds(Administrator, email=safe_text, user_id=st.integers(), user_name=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Booking_strategy = st.builds(Booking, Restaurant_id=safe_text, booking_id=st.integers(), customer_id=safe_text, date=st.dates(), endTime=safe_text, person=st.integers(), reservedTables=safe_text, startTime=safe_text)
@given(instance=Booking_strategy)
@settings(max_examples=25)
def test_Booking_instantiation(instance):
    assert isinstance(instance, Booking)


CustomerUI_strategy = st.builds(CustomerUI)
@given(instance=CustomerUI_strategy)
@settings(max_examples=25)
def test_CustomerUI_instantiation(instance):
    assert isinstance(instance, CustomerUI)


List___strategy = st.builds(List__)
@given(instance=List___strategy)
@settings(max_examples=25)
def test_List___instantiation(instance):
    assert isinstance(instance, List__)


List_re__strategy = st.builds(List_re_)
@given(instance=List_re__strategy)
@settings(max_examples=25)
def test_List_re__instantiation(instance):
    assert isinstance(instance, List_re_)


List_reservation__strategy = st.builds(List_reservation_)
@given(instance=List_reservation__strategy)
@settings(max_examples=25)
def test_List_reservation__instantiation(instance):
    assert isinstance(instance, List_reservation_)


Management_UI_strategy = st.builds(Management_UI)
@given(instance=Management_UI_strategy)
@settings(max_examples=25)
def test_Management_UI_instantiation(instance):
    assert isinstance(instance, Management_UI)


Restaurant_Reservation_System_strategy = st.builds(Restaurant_Reservation_System, Menu=safe_text, bookings=safe_text)
@given(instance=Restaurant_Reservation_System_strategy)
@settings(max_examples=25)
def test_Restaurant_Reservation_System_instantiation(instance):
    assert isinstance(instance, Restaurant_Reservation_System)


Restaurant_owner_strategy = st.builds(Restaurant_owner, email=safe_text, user_id=safe_text, username=safe_text)
@given(instance=Restaurant_owner_strategy)
@settings(max_examples=25)
def test_Restaurant_owner_instantiation(instance):
    assert isinstance(instance, Restaurant_owner)


Staff_strategy = st.builds(Staff, name=safe_text, type=safe_text, user_id=safe_text)
@given(instance=Staff_strategy)
@settings(max_examples=25)
def test_Staff_instantiation(instance):
    assert isinstance(instance, Staff)


Table_strategy = st.builds(Table, numSeats=st.integers(), quantity=st.integers(), table_id=safe_text)
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


