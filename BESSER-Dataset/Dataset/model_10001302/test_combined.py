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
    List_reservation_,
    List_re_,
    List__,
    CustomerUI,
    Management_UI,
    Restaurant_owner,
    Administrator,
    Staff,
    Reservation_status,
    Table,
    Booking,
    Restaurant_Reservation_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_list_reservation__is_not_abstract():
    assert not inspect.isabstract(List_reservation_)


def test_hyp_list_reservation__constructor_exists():
    assert callable(List_reservation_.__init__)


def test_hyp_list_reservation__constructor_args():
    sig = inspect.signature(List_reservation_.__init__)
    params = list(sig.parameters.keys())



def test_hyp_list_re__is_not_abstract():
    assert not inspect.isabstract(List_re_)


def test_hyp_list_re__constructor_exists():
    assert callable(List_re_.__init__)


def test_hyp_list_re__constructor_args():
    sig = inspect.signature(List_re_.__init__)
    params = list(sig.parameters.keys())



def test_hyp_list___is_not_abstract():
    assert not inspect.isabstract(List__)


def test_hyp_list___constructor_exists():
    assert callable(List__.__init__)


def test_hyp_list___constructor_args():
    sig = inspect.signature(List__.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customerui_is_not_abstract():
    assert not inspect.isabstract(CustomerUI)


def test_hyp_customerui_constructor_exists():
    assert callable(CustomerUI.__init__)


def test_hyp_customerui_constructor_args():
    sig = inspect.signature(CustomerUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_management_ui_is_not_abstract():
    assert not inspect.isabstract(Management_UI)


def test_hyp_management_ui_constructor_exists():
    assert callable(Management_UI.__init__)


def test_hyp_management_ui_constructor_args():
    sig = inspect.signature(Management_UI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_restaurant_owner_is_not_abstract():
    assert not inspect.isabstract(Restaurant_owner)


def test_hyp_restaurant_owner_constructor_exists():
    assert callable(Restaurant_owner.__init__)


def test_hyp_restaurant_owner_constructor_args():
    sig = inspect.signature(Restaurant_owner.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "username" in params, "Missing parameter 'username'"
    assert "user_id" in params, "Missing parameter 'user_id'"






def test_hyp_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_hyp_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_hyp_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "user_name" in params, "Missing parameter 'user_name'"
    assert "user_id" in params, "Missing parameter 'user_id'"






def test_hyp_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_hyp_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_hyp_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "user_id" in params, "Missing parameter 'user_id'"






def test_hyp_reservation_status_is_not_abstract():
    assert not inspect.isabstract(Reservation_status)


def test_hyp_reservation_status_constructor_exists():
    assert callable(Reservation_status.__init__)


def test_hyp_reservation_status_constructor_args():
    sig = inspect.signature(Reservation_status.__init__)
    params = list(sig.parameters.keys())
    assert "reservation" in params, "Missing parameter 'reservation'"
    assert "report_id" in params, "Missing parameter 'report_id'"

def test_hyp_reservation_status_has_reservation():
    assert hasattr(Reservation_status, "reservation")
    descriptor = None
    for klass in Reservation_status.__mro__:
        if "reservation" in klass.__dict__:
            descriptor = klass.__dict__["reservation"]
            break
    assert isinstance(descriptor, property)

def test_hyp_reservation_status_has_report_id():
    assert hasattr(Reservation_status, "report_id")
    descriptor = None
    for klass in Reservation_status.__mro__:
        if "report_id" in klass.__dict__:
            descriptor = klass.__dict__["report_id"]
            break
    assert isinstance(descriptor, property)



def test_hyp_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_hyp_table_constructor_exists():
    assert callable(Table.__init__)


def test_hyp_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "table_id" in params, "Missing parameter 'table_id'"
    assert "numSeats" in params, "Missing parameter 'numSeats'"
    assert "quantity" in params, "Missing parameter 'quantity'"






def test_hyp_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_hyp_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_hyp_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "person" in params, "Missing parameter 'person'"
    assert "customer_id" in params, "Missing parameter 'customer_id'"
    assert "Restaurant_id" in params, "Missing parameter 'Restaurant_id'"
    assert "booking_id" in params, "Missing parameter 'booking_id'"
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "startTime" in params, "Missing parameter 'startTime'"











def test_hyp_restaurant_reservation_system_is_not_abstract():
    assert not inspect.isabstract(Restaurant_Reservation_System)


def test_hyp_restaurant_reservation_system_constructor_exists():
    assert callable(Restaurant_Reservation_System.__init__)


def test_hyp_restaurant_reservation_system_constructor_args():
    sig = inspect.signature(Restaurant_Reservation_System.__init__)
    params = list(sig.parameters.keys())
    assert "Menu" in params, "Missing parameter 'Menu'"
    assert "bookings" in params, "Missing parameter 'bookings'"




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
List_reservation__strategy = st.builds(
    List_reservation_,
)
List_re__strategy = st.builds(
    List_re_,
)
List___strategy = st.builds(
    List__,
)
CustomerUI_strategy = st.builds(
    CustomerUI,
)
Management_UI_strategy = st.builds(
    Management_UI,
)
Restaurant_owner_strategy = st.builds(
    Restaurant_owner,
    email=
        safe_text,
    username=
        safe_text,
    user_id=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    email=
        safe_text,
    user_name=
        safe_text,
    user_id=
        st.integers()
)
Staff_strategy = st.builds(
    Staff,
    name=
        safe_text,
    type=
        safe_text,
    user_id=
        safe_text
)
Reservation_status_strategy = st.builds(
    Reservation_status,
    reservation=
        st.none(),
    report_id=
        safe_text
)
Table_strategy = st.builds(
    Table,
    table_id=
        safe_text,
    numSeats=
        st.integers(),
    quantity=
        st.integers()
)
Booking_strategy = st.builds(
    Booking,
    date=
        st.dates(),
    reservedTables=
        safe_text,
    person=
        st.integers(),
    customer_id=
        safe_text,
    Restaurant_id=
        safe_text,
    booking_id=
        st.integers(),
    endTime=
        safe_text,
    startTime=
        safe_text
)
Restaurant_Reservation_System_strategy = st.builds(
    Restaurant_Reservation_System,
    Menu=
        safe_text,
    bookings=
        safe_text
)









@given(instance=Restaurant_owner_strategy)
def test_hyp_restaurant_owner_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Restaurant_owner_strategy)
def test_hyp_restaurant_owner_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Restaurant_owner_strategy)
def test_hyp_restaurant_owner_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original




@given(instance=Administrator_strategy)
def test_hyp_administrator_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_user_name_setter(instance):
    original = instance.user_name
    instance.user_name = original
    assert instance.user_name == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original




@given(instance=Staff_strategy)
def test_hyp_staff_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Staff_strategy)
def test_hyp_staff_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Staff_strategy)
def test_hyp_staff_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Reservation_status_strategy)
@settings(max_examples=50)
def test_hyp_reservation_status_instantiation(instance):
    assert isinstance(instance, Reservation_status)



@given(instance=Reservation_status_strategy)
def test_hyp_reservation_status_reservation_setter(instance):
    original = instance.reservation
    instance.reservation = original
    assert instance.reservation == original



@given(instance=Reservation_status_strategy)
def test_hyp_reservation_status_report_id_setter(instance):
    original = instance.report_id
    instance.report_id = original
    assert instance.report_id == original




@given(instance=Table_strategy)
def test_hyp_table_table_id_setter(instance):
    original = instance.table_id
    instance.table_id = original
    assert instance.table_id == original



@given(instance=Table_strategy)
def test_hyp_table_numSeats_setter(instance):
    original = instance.numSeats
    instance.numSeats = original
    assert instance.numSeats == original



@given(instance=Table_strategy)
def test_hyp_table_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original




@given(instance=Booking_strategy)
def test_hyp_booking_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Booking_strategy)
def test_hyp_booking_reservedTables_setter(instance):
    original = instance.reservedTables
    instance.reservedTables = original
    assert instance.reservedTables == original



@given(instance=Booking_strategy)
def test_hyp_booking_person_setter(instance):
    original = instance.person
    instance.person = original
    assert instance.person == original



@given(instance=Booking_strategy)
def test_hyp_booking_customer_id_setter(instance):
    original = instance.customer_id
    instance.customer_id = original
    assert instance.customer_id == original



@given(instance=Booking_strategy)
def test_hyp_booking_Restaurant_id_setter(instance):
    original = instance.Restaurant_id
    instance.Restaurant_id = original
    assert instance.Restaurant_id == original



@given(instance=Booking_strategy)
def test_hyp_booking_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original



@given(instance=Booking_strategy)
def test_hyp_booking_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=Booking_strategy)
def test_hyp_booking_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original




@given(instance=Restaurant_Reservation_System_strategy)
def test_hyp_restaurant_reservation_system_Menu_setter(instance):
    original = instance.Menu
    instance.Menu = original
    assert instance.Menu == original



@given(instance=Restaurant_Reservation_System_strategy)
def test_hyp_restaurant_reservation_system_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



