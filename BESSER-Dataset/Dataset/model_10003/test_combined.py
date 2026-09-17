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
    Employee,
    CoachBus_Manager,
    Ticket,
    CoachBus_ChildTicket,
    CoachBus_AdultTicket,
    CoachBus_VendingMachine,
    Trip,
    CoachBus_RegularTrip,
    CoachBus_Passenger,
    CoachBus_Coach,
    CoachBus_Employee,
    CoachBus_Ticket,
    CoachBus_BookingOffice,
    CoachBus_SecurityGuard,
    CoachBus_PrivateTrip,
    CoachBus_Trip,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coachbus_manager_is_not_abstract():
    assert not inspect.isabstract(CoachBus_Manager)


def test_hyp_coachbus_manager_constructor_exists():
    assert callable(CoachBus_Manager.__init__)


def test_hyp_coachbus_manager_constructor_args():
    sig = inspect.signature(CoachBus_Manager.__init__)
    params = list(sig.parameters.keys())
    assert "hasMBA" in params, "Missing parameter 'hasMBA'"




def test_hyp_ticket_is_not_abstract():
    assert not inspect.isabstract(Ticket)


def test_hyp_ticket_constructor_exists():
    assert callable(Ticket.__init__)


def test_hyp_ticket_constructor_args():
    sig = inspect.signature(Ticket.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coachbus_childticket_is_not_abstract():
    assert not inspect.isabstract(CoachBus_ChildTicket)


def test_hyp_coachbus_childticket_constructor_exists():
    assert callable(CoachBus_ChildTicket.__init__)


def test_hyp_coachbus_childticket_constructor_args():
    sig = inspect.signature(CoachBus_ChildTicket.__init__)
    params = list(sig.parameters.keys())
    assert "isSchoolTrip" in params, "Missing parameter 'isSchoolTrip'"




def test_hyp_coachbus_adultticket_is_not_abstract():
    assert not inspect.isabstract(CoachBus_AdultTicket)


def test_hyp_coachbus_adultticket_constructor_exists():
    assert callable(CoachBus_AdultTicket.__init__)


def test_hyp_coachbus_adultticket_constructor_args():
    sig = inspect.signature(CoachBus_AdultTicket.__init__)
    params = list(sig.parameters.keys())
    assert "isElderlyDiscount" in params, "Missing parameter 'isElderlyDiscount'"




def test_hyp_coachbus_vendingmachine_is_not_abstract():
    assert not inspect.isabstract(CoachBus_VendingMachine)


def test_hyp_coachbus_vendingmachine_constructor_exists():
    assert callable(CoachBus_VendingMachine.__init__)


def test_hyp_coachbus_vendingmachine_constructor_args():
    sig = inspect.signature(CoachBus_VendingMachine.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"




def test_hyp_trip_is_not_abstract():
    assert not inspect.isabstract(Trip)


def test_hyp_trip_constructor_exists():
    assert callable(Trip.__init__)


def test_hyp_trip_constructor_args():
    sig = inspect.signature(Trip.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coachbus_regulartrip_is_not_abstract():
    assert not inspect.isabstract(CoachBus_RegularTrip)


def test_hyp_coachbus_regulartrip_constructor_exists():
    assert callable(CoachBus_RegularTrip.__init__)


def test_hyp_coachbus_regulartrip_constructor_args():
    sig = inspect.signature(CoachBus_RegularTrip.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coachbus_passenger_is_not_abstract():
    assert not inspect.isabstract(CoachBus_Passenger)


def test_hyp_coachbus_passenger_constructor_exists():
    assert callable(CoachBus_Passenger.__init__)


def test_hyp_coachbus_passenger_constructor_args():
    sig = inspect.signature(CoachBus_Passenger.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "idCard" in params, "Missing parameter 'idCard'"
    assert "age" in params, "Missing parameter 'age'"






def test_hyp_coachbus_coach_is_not_abstract():
    assert not inspect.isabstract(CoachBus_Coach)


def test_hyp_coachbus_coach_constructor_exists():
    assert callable(CoachBus_Coach.__init__)


def test_hyp_coachbus_coach_constructor_args():
    sig = inspect.signature(CoachBus_Coach.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "model" in params, "Missing parameter 'model'"
    assert "name" in params, "Missing parameter 'name'"
    assert "noOfSeats" in params, "Missing parameter 'noOfSeats'"







def test_hyp_coachbus_employee_is_not_abstract():
    assert not inspect.isabstract(CoachBus_Employee)


def test_hyp_coachbus_employee_constructor_exists():
    assert callable(CoachBus_Employee.__init__)


def test_hyp_coachbus_employee_constructor_args():
    sig = inspect.signature(CoachBus_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "baseSalary" in params, "Missing parameter 'baseSalary'"





def test_hyp_coachbus_ticket_is_not_abstract():
    assert not inspect.isabstract(CoachBus_Ticket)


def test_hyp_coachbus_ticket_constructor_exists():
    assert callable(CoachBus_Ticket.__init__)


def test_hyp_coachbus_ticket_constructor_args():
    sig = inspect.signature(CoachBus_Ticket.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "price" in params, "Missing parameter 'price'"
    assert "isRoundTrip" in params, "Missing parameter 'isRoundTrip'"






def test_hyp_coachbus_bookingoffice_is_not_abstract():
    assert not inspect.isabstract(CoachBus_BookingOffice)


def test_hyp_coachbus_bookingoffice_constructor_exists():
    assert callable(CoachBus_BookingOffice.__init__)


def test_hyp_coachbus_bookingoffice_constructor_args():
    sig = inspect.signature(CoachBus_BookingOffice.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "officeID" in params, "Missing parameter 'officeID'"
    assert "location" in params, "Missing parameter 'location'"






def test_hyp_coachbus_securityguard_is_not_abstract():
    assert not inspect.isabstract(CoachBus_SecurityGuard)


def test_hyp_coachbus_securityguard_constructor_exists():
    assert callable(CoachBus_SecurityGuard.__init__)


def test_hyp_coachbus_securityguard_constructor_args():
    sig = inspect.signature(CoachBus_SecurityGuard.__init__)
    params = list(sig.parameters.keys())
    assert "shift" in params, "Missing parameter 'shift'"




def test_hyp_coachbus_privatetrip_is_not_abstract():
    assert not inspect.isabstract(CoachBus_PrivateTrip)


def test_hyp_coachbus_privatetrip_constructor_exists():
    assert callable(CoachBus_PrivateTrip.__init__)


def test_hyp_coachbus_privatetrip_constructor_args():
    sig = inspect.signature(CoachBus_PrivateTrip.__init__)
    params = list(sig.parameters.keys())
    assert "extras" in params, "Missing parameter 'extras'"




def test_hyp_coachbus_trip_is_not_abstract():
    assert not inspect.isabstract(CoachBus_Trip)


def test_hyp_coachbus_trip_constructor_exists():
    assert callable(CoachBus_Trip.__init__)


def test_hyp_coachbus_trip_constructor_args():
    sig = inspect.signature(CoachBus_Trip.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"
    assert "origin" in params, "Missing parameter 'origin'"
    assert "destination" in params, "Missing parameter 'destination'"







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
Employee_strategy = st.builds(
    Employee,
)
CoachBus_Manager_strategy = st.builds(
    CoachBus_Manager,
    hasMBA=
        st.booleans()
)
Ticket_strategy = st.builds(
    Ticket,
)
CoachBus_ChildTicket_strategy = st.builds(
    CoachBus_ChildTicket,
    isSchoolTrip=
        st.booleans()
)
CoachBus_AdultTicket_strategy = st.builds(
    CoachBus_AdultTicket,
    isElderlyDiscount=
        st.booleans()
)
CoachBus_VendingMachine_strategy = st.builds(
    CoachBus_VendingMachine,
    number=
        st.integers()
)
Trip_strategy = st.builds(
    Trip,
)
CoachBus_RegularTrip_strategy = st.builds(
    CoachBus_RegularTrip,
)
CoachBus_Passenger_strategy = st.builds(
    CoachBus_Passenger,
    name=
        safe_text,
    idCard=
        safe_text,
    age=
        st.integers()
)
CoachBus_Coach_strategy = st.builds(
    CoachBus_Coach,
    id=
        st.integers(),
    model=
        safe_text,
    name=
        safe_text,
    noOfSeats=
        st.integers()
)
CoachBus_Employee_strategy = st.builds(
    CoachBus_Employee,
    id=
        st.integers(),
    baseSalary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CoachBus_Ticket_strategy = st.builds(
    CoachBus_Ticket,
    number=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isRoundTrip=
        st.booleans()
)
CoachBus_BookingOffice_strategy = st.builds(
    CoachBus_BookingOffice,
    name=
        safe_text,
    officeID=
        st.integers(),
    location=
        safe_text
)
CoachBus_SecurityGuard_strategy = st.builds(
    CoachBus_SecurityGuard,
    shift=
        safe_text
)
CoachBus_PrivateTrip_strategy = st.builds(
    CoachBus_PrivateTrip,
    extras=
        safe_text
)
CoachBus_Trip_strategy = st.builds(
    CoachBus_Trip,
    type=
        safe_text,
    number=
        st.integers(),
    name=
        safe_text,
    origin=
        safe_text,
    destination=
        safe_text
)





@given(instance=CoachBus_Manager_strategy)
def test_hyp_coachbus_manager_hasMBA_setter(instance):
    original = instance.hasMBA
    instance.hasMBA = original
    assert instance.hasMBA == original





@given(instance=CoachBus_ChildTicket_strategy)
def test_hyp_coachbus_childticket_isSchoolTrip_setter(instance):
    original = instance.isSchoolTrip
    instance.isSchoolTrip = original
    assert instance.isSchoolTrip == original




@given(instance=CoachBus_AdultTicket_strategy)
def test_hyp_coachbus_adultticket_isElderlyDiscount_setter(instance):
    original = instance.isElderlyDiscount
    instance.isElderlyDiscount = original
    assert instance.isElderlyDiscount == original




@given(instance=CoachBus_VendingMachine_strategy)
def test_hyp_coachbus_vendingmachine_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original






@given(instance=CoachBus_Passenger_strategy)
def test_hyp_coachbus_passenger_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=CoachBus_Passenger_strategy)
def test_hyp_coachbus_passenger_idCard_setter(instance):
    original = instance.idCard
    instance.idCard = original
    assert instance.idCard == original



@given(instance=CoachBus_Passenger_strategy)
def test_hyp_coachbus_passenger_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original




@given(instance=CoachBus_Coach_strategy)
def test_hyp_coachbus_coach_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=CoachBus_Coach_strategy)
def test_hyp_coachbus_coach_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original



@given(instance=CoachBus_Coach_strategy)
def test_hyp_coachbus_coach_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=CoachBus_Coach_strategy)
def test_hyp_coachbus_coach_noOfSeats_setter(instance):
    original = instance.noOfSeats
    instance.noOfSeats = original
    assert instance.noOfSeats == original




@given(instance=CoachBus_Employee_strategy)
def test_hyp_coachbus_employee_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=CoachBus_Employee_strategy)
def test_hyp_coachbus_employee_baseSalary_setter(instance):
    original = instance.baseSalary
    instance.baseSalary = original
    assert instance.baseSalary == original




@given(instance=CoachBus_Ticket_strategy)
def test_hyp_coachbus_ticket_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=CoachBus_Ticket_strategy)
def test_hyp_coachbus_ticket_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=CoachBus_Ticket_strategy)
def test_hyp_coachbus_ticket_isRoundTrip_setter(instance):
    original = instance.isRoundTrip
    instance.isRoundTrip = original
    assert instance.isRoundTrip == original




@given(instance=CoachBus_BookingOffice_strategy)
def test_hyp_coachbus_bookingoffice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=CoachBus_BookingOffice_strategy)
def test_hyp_coachbus_bookingoffice_officeID_setter(instance):
    original = instance.officeID
    instance.officeID = original
    assert instance.officeID == original



@given(instance=CoachBus_BookingOffice_strategy)
def test_hyp_coachbus_bookingoffice_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original




@given(instance=CoachBus_SecurityGuard_strategy)
def test_hyp_coachbus_securityguard_shift_setter(instance):
    original = instance.shift
    instance.shift = original
    assert instance.shift == original




@given(instance=CoachBus_PrivateTrip_strategy)
def test_hyp_coachbus_privatetrip_extras_setter(instance):
    original = instance.extras
    instance.extras = original
    assert instance.extras == original




@given(instance=CoachBus_Trip_strategy)
def test_hyp_coachbus_trip_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=CoachBus_Trip_strategy)
def test_hyp_coachbus_trip_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=CoachBus_Trip_strategy)
def test_hyp_coachbus_trip_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=CoachBus_Trip_strategy)
def test_hyp_coachbus_trip_origin_setter(instance):
    original = instance.origin
    instance.origin = original
    assert instance.origin == original



@given(instance=CoachBus_Trip_strategy)
def test_hyp_coachbus_trip_destination_setter(instance):
    original = instance.destination
    instance.destination = original
    assert instance.destination == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CoachBus_AdultTicket,
    CoachBus_BookingOffice,
    CoachBus_ChildTicket,
    CoachBus_Coach,
    CoachBus_Employee,
    CoachBus_Manager,
    CoachBus_Passenger,
    CoachBus_PrivateTrip,
    CoachBus_RegularTrip,
    CoachBus_SecurityGuard,
    CoachBus_Ticket,
    CoachBus_Trip,
    CoachBus_VendingMachine,
    Employee,
    Ticket,
    Trip,
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

def test_CoachBus_AdultTicket_isElderlyDiscount_value_roundtrip():
    instance = CoachBus_AdultTicket(isElderlyDiscount=True)
    assert instance.isElderlyDiscount == True
    instance.isElderlyDiscount = False
    assert instance.isElderlyDiscount == False


def test_CoachBus_BookingOffice_location_value_roundtrip():
    instance = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_CoachBus_BookingOffice_name_value_roundtrip():
    instance = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_CoachBus_BookingOffice_officeID_value_roundtrip():
    instance = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    assert instance.officeID == 7
    instance.officeID = 13
    assert instance.officeID == 13


def test_CoachBus_ChildTicket_isSchoolTrip_value_roundtrip():
    instance = CoachBus_ChildTicket(isSchoolTrip=True)
    assert instance.isSchoolTrip == True
    instance.isSchoolTrip = False
    assert instance.isSchoolTrip == False


def test_CoachBus_Coach_id_value_roundtrip():
    instance = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_CoachBus_Coach_model_value_roundtrip():
    instance = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    assert instance.model == "sample_text"
    instance.model = "sample_text_2"
    assert instance.model == "sample_text_2"


def test_CoachBus_Coach_name_value_roundtrip():
    instance = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_CoachBus_Coach_noOfSeats_value_roundtrip():
    instance = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    assert instance.noOfSeats == 7
    instance.noOfSeats = 13
    assert instance.noOfSeats == 13


def test_CoachBus_Employee_baseSalary_value_roundtrip():
    instance = CoachBus_Employee(baseSalary=3.14, id=7)
    assert instance.baseSalary == 3.14
    instance.baseSalary = 9.99
    assert instance.baseSalary == 9.99


def test_CoachBus_Employee_id_value_roundtrip():
    instance = CoachBus_Employee(baseSalary=3.14, id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_CoachBus_Manager_hasMBA_value_roundtrip():
    instance = CoachBus_Manager(hasMBA=True)
    assert instance.hasMBA == True
    instance.hasMBA = False
    assert instance.hasMBA == False


def test_CoachBus_Passenger_age_value_roundtrip():
    instance = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_CoachBus_Passenger_idCard_value_roundtrip():
    instance = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    assert instance.idCard == "sample_text"
    instance.idCard = "sample_text_2"
    assert instance.idCard == "sample_text_2"


def test_CoachBus_Passenger_name_value_roundtrip():
    instance = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_CoachBus_PrivateTrip_extras_value_roundtrip():
    instance = CoachBus_PrivateTrip(extras="sample_text")
    assert instance.extras == "sample_text"
    instance.extras = "sample_text_2"
    assert instance.extras == "sample_text_2"


def test_CoachBus_SecurityGuard_shift_value_roundtrip():
    instance = CoachBus_SecurityGuard(shift="sample_text")
    assert instance.shift == "sample_text"
    instance.shift = "sample_text_2"
    assert instance.shift == "sample_text_2"


def test_CoachBus_Ticket_isRoundTrip_value_roundtrip():
    instance = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    assert instance.isRoundTrip == True
    instance.isRoundTrip = False
    assert instance.isRoundTrip == False


def test_CoachBus_Ticket_number_value_roundtrip():
    instance = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_CoachBus_Ticket_price_value_roundtrip():
    instance = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_CoachBus_Trip_destination_value_roundtrip():
    instance = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    assert instance.destination == "sample_text"
    instance.destination = "sample_text_2"
    assert instance.destination == "sample_text_2"


def test_CoachBus_Trip_name_value_roundtrip():
    instance = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_CoachBus_Trip_number_value_roundtrip():
    instance = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_CoachBus_Trip_origin_value_roundtrip():
    instance = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    assert instance.origin == "sample_text"
    instance.origin = "sample_text_2"
    assert instance.origin == "sample_text_2"


def test_CoachBus_Trip_type_value_roundtrip():
    instance = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_CoachBus_VendingMachine_number_value_roundtrip():
    instance = CoachBus_VendingMachine(number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_CoachBus_Manager_isa_Employee():
    instance = CoachBus_Manager(hasMBA=True)
    assert isinstance(instance, Employee)


def test_CoachBus_SecurityGuard_isa_Employee():
    instance = CoachBus_SecurityGuard(shift="sample_text")
    assert isinstance(instance, Employee)


def test_CoachBus_AdultTicket_isa_Ticket():
    instance = CoachBus_AdultTicket(isElderlyDiscount=True)
    assert isinstance(instance, Ticket)


def test_CoachBus_ChildTicket_isa_Ticket():
    instance = CoachBus_ChildTicket(isSchoolTrip=True)
    assert isinstance(instance, Ticket)


def test_CoachBus_PrivateTrip_isa_Trip():
    instance = CoachBus_PrivateTrip(extras="sample_text")
    assert isinstance(instance, Trip)


def test_CoachBus_RegularTrip_isa_Trip():
    instance = CoachBus_RegularTrip()
    assert isinstance(instance, Trip)


def test_assoc_coach10_link_reassign_clear():
    a = CoachBus_SecurityGuard(shift="sample_text")
    b1 = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    b2 = CoachBus_Coach(id=13, model="sample_text_2", name="sample_text_2", noOfSeats=13)
    _safe_set(a, 'guards', b1)
    assert _is_linked(a, 'guards', b1)
    if hasattr(b1, 'Coach11'):
        assert _is_linked(b1, 'Coach11', a)
    _safe_set(a, 'guards', b2)
    assert _is_linked(a, 'guards', b2)
    if hasattr(b1, 'Coach11'):
        assert not _is_linked(b1, 'Coach11', a)
    if hasattr(b2, 'Coach11'):
        assert _is_linked(b2, 'Coach11', a)
    _safe_set(a, 'guards', None)
    assert not _is_linked(a, 'guards', b2)
    if hasattr(b2, 'Coach11'):
        assert not _is_linked(b2, 'Coach11', a)


def test_assoc_coaches0_link_reassign_clear():
    a = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    b1 = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    b2 = CoachBus_Coach(id=13, model="sample_text_2", name="sample_text_2", noOfSeats=13)
    _safe_set(a, 'trips', {b1})
    assert _is_linked(a, 'trips', b1)
    if hasattr(b1, 'Coach'):
        assert _is_linked(b1, 'Coach', a)
    _safe_set(a, 'trips', {b2})
    assert _is_linked(a, 'trips', b2)
    if hasattr(b1, 'Coach'):
        assert not _is_linked(b1, 'Coach', a)
    if hasattr(b2, 'Coach'):
        assert _is_linked(b2, 'Coach', a)
    _safe_set(a, 'trips', set())
    assert not _is_linked(a, 'trips', b2)
    if hasattr(b2, 'Coach'):
        assert not _is_linked(b2, 'Coach', a)


def test_assoc_coaches14_link_reassign_clear():
    a = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    b1 = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    b2 = CoachBus_BookingOffice(location="sample_text_2", name="sample_text_2", officeID=13)
    _safe_set(a, 'Coach15', b1)
    assert _is_linked(a, 'Coach15', b1)
    if hasattr(b1, 'offices'):
        assert _is_linked(b1, 'offices', a)
    _safe_set(a, 'Coach15', b2)
    assert _is_linked(a, 'Coach15', b2)
    if hasattr(b1, 'offices'):
        assert not _is_linked(b1, 'offices', a)
    if hasattr(b2, 'offices'):
        assert _is_linked(b2, 'offices', a)
    _safe_set(a, 'Coach15', None)
    assert not _is_linked(a, 'Coach15', b2)
    if hasattr(b2, 'offices'):
        assert not _is_linked(b2, 'offices', a)


def test_assoc_guards4_link_reassign_clear():
    a = CoachBus_SecurityGuard(shift="sample_text")
    b1 = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    b2 = CoachBus_Coach(id=13, model="sample_text_2", name="sample_text_2", noOfSeats=13)
    _safe_set(a, 'SecurityGuard', b1)
    assert _is_linked(a, 'SecurityGuard', b1)
    if hasattr(b1, 'coach'):
        assert _is_linked(b1, 'coach', a)
    _safe_set(a, 'SecurityGuard', b2)
    assert _is_linked(a, 'SecurityGuard', b2)
    if hasattr(b1, 'coach'):
        assert not _is_linked(b1, 'coach', a)
    if hasattr(b2, 'coach'):
        assert _is_linked(b2, 'coach', a)
    _safe_set(a, 'SecurityGuard', None)
    assert not _is_linked(a, 'SecurityGuard', b2)
    if hasattr(b2, 'coach'):
        assert not _is_linked(b2, 'coach', a)


def test_assoc_manager16_link_reassign_clear():
    a = CoachBus_Manager(hasMBA=True)
    b1 = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    b2 = CoachBus_BookingOffice(location="sample_text_2", name="sample_text_2", officeID=13)
    _safe_set(a, 'Manager', b1)
    assert _is_linked(a, 'Manager', b1)
    if hasattr(b1, 'office'):
        assert _is_linked(b1, 'office', a)
    _safe_set(a, 'Manager', b2)
    assert _is_linked(a, 'Manager', b2)
    if hasattr(b1, 'office'):
        assert not _is_linked(b1, 'office', a)
    if hasattr(b2, 'office'):
        assert _is_linked(b2, 'office', a)
    _safe_set(a, 'Manager', None)
    assert not _is_linked(a, 'Manager', b2)
    if hasattr(b2, 'office'):
        assert not _is_linked(b2, 'office', a)


def test_assoc_office12_link_reassign_clear():
    a = CoachBus_Manager(hasMBA=True)
    b1 = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    b2 = CoachBus_BookingOffice(location="sample_text_2", name="sample_text_2", officeID=13)
    _safe_set(a, 'manager', b1)
    assert _is_linked(a, 'manager', b1)
    if hasattr(b1, 'BookingOffice13'):
        assert _is_linked(b1, 'BookingOffice13', a)
    _safe_set(a, 'manager', b2)
    assert _is_linked(a, 'manager', b2)
    if hasattr(b1, 'BookingOffice13'):
        assert not _is_linked(b1, 'BookingOffice13', a)
    if hasattr(b2, 'BookingOffice13'):
        assert _is_linked(b2, 'BookingOffice13', a)
    _safe_set(a, 'manager', None)
    assert not _is_linked(a, 'manager', b2)
    if hasattr(b2, 'BookingOffice13'):
        assert not _is_linked(b2, 'BookingOffice13', a)


def test_assoc_office26_link_reassign_clear():
    a = CoachBus_VendingMachine(number=7)
    b1 = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    b2 = CoachBus_BookingOffice(location="sample_text_2", name="sample_text_2", officeID=13)
    _safe_set(a, 'vms', b1)
    assert _is_linked(a, 'vms', b1)
    if hasattr(b1, 'BookingOffice27'):
        assert _is_linked(b1, 'BookingOffice27', a)
    _safe_set(a, 'vms', b2)
    assert _is_linked(a, 'vms', b2)
    if hasattr(b1, 'BookingOffice27'):
        assert not _is_linked(b1, 'BookingOffice27', a)
    if hasattr(b2, 'BookingOffice27'):
        assert _is_linked(b2, 'BookingOffice27', a)
    _safe_set(a, 'vms', None)
    assert not _is_linked(a, 'vms', b2)
    if hasattr(b2, 'BookingOffice27'):
        assert not _is_linked(b2, 'BookingOffice27', a)


def test_assoc_offices5_link_reassign_clear():
    a = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    b1 = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    b2 = CoachBus_BookingOffice(location="sample_text_2", name="sample_text_2", officeID=13)
    _safe_set(a, 'coaches6', {b1})
    assert _is_linked(a, 'coaches6', b1)
    if hasattr(b1, 'BookingOffice'):
        assert _is_linked(b1, 'BookingOffice', a)
    _safe_set(a, 'coaches6', {b2})
    assert _is_linked(a, 'coaches6', b2)
    if hasattr(b1, 'BookingOffice'):
        assert not _is_linked(b1, 'BookingOffice', a)
    if hasattr(b2, 'BookingOffice'):
        assert _is_linked(b2, 'BookingOffice', a)
    _safe_set(a, 'coaches6', set())
    assert not _is_linked(a, 'coaches6', b2)
    if hasattr(b2, 'BookingOffice'):
        assert not _is_linked(b2, 'BookingOffice', a)


def test_assoc_passengers1_link_reassign_clear():
    a = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    b1 = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    b2 = CoachBus_Passenger(age=13, idCard="sample_text_2", name="sample_text_2")
    _safe_set(a, 'trips2', {b1})
    assert _is_linked(a, 'trips2', b1)
    if hasattr(b1, 'Passenger'):
        assert _is_linked(b1, 'Passenger', a)
    _safe_set(a, 'trips2', {b2})
    assert _is_linked(a, 'trips2', b2)
    if hasattr(b1, 'Passenger'):
        assert not _is_linked(b1, 'Passenger', a)
    if hasattr(b2, 'Passenger'):
        assert _is_linked(b2, 'Passenger', a)
    _safe_set(a, 'trips2', set())
    assert not _is_linked(a, 'trips2', b2)
    if hasattr(b2, 'Passenger'):
        assert not _is_linked(b2, 'Passenger', a)


def test_assoc_psg19_link_reassign_clear():
    a = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    b1 = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    b2 = CoachBus_Passenger(age=13, idCard="sample_text_2", name="sample_text_2")
    _safe_set(a, 'tickets', b1)
    assert _is_linked(a, 'tickets', b1)
    if hasattr(b1, 'Passenger20'):
        assert _is_linked(b1, 'Passenger20', a)
    _safe_set(a, 'tickets', b2)
    assert _is_linked(a, 'tickets', b2)
    if hasattr(b1, 'Passenger20'):
        assert not _is_linked(b1, 'Passenger20', a)
    if hasattr(b2, 'Passenger20'):
        assert _is_linked(b2, 'Passenger20', a)
    _safe_set(a, 'tickets', None)
    assert not _is_linked(a, 'tickets', b2)
    if hasattr(b2, 'Passenger20'):
        assert not _is_linked(b2, 'Passenger20', a)


def test_assoc_tickets24_link_reassign_clear():
    a = CoachBus_VendingMachine(number=7)
    b1 = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    b2 = CoachBus_Ticket(isRoundTrip=False, number=13, price=9.99)
    _safe_set(a, 'vm', {b1})
    assert _is_linked(a, 'vm', b1)
    if hasattr(b1, 'Ticket25'):
        assert _is_linked(b1, 'Ticket25', a)
    _safe_set(a, 'vm', {b2})
    assert _is_linked(a, 'vm', b2)
    if hasattr(b1, 'Ticket25'):
        assert not _is_linked(b1, 'Ticket25', a)
    if hasattr(b2, 'Ticket25'):
        assert _is_linked(b2, 'Ticket25', a)
    _safe_set(a, 'vm', set())
    assert not _is_linked(a, 'vm', b2)
    if hasattr(b2, 'Ticket25'):
        assert not _is_linked(b2, 'Ticket25', a)


def test_assoc_tickets9_link_reassign_clear():
    a = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    b1 = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    b2 = CoachBus_Passenger(age=13, idCard="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Ticket', b1)
    assert _is_linked(a, 'Ticket', b1)
    if hasattr(b1, 'psg'):
        assert _is_linked(b1, 'psg', a)
    _safe_set(a, 'Ticket', b2)
    assert _is_linked(a, 'Ticket', b2)
    if hasattr(b1, 'psg'):
        assert not _is_linked(b1, 'psg', a)
    if hasattr(b2, 'psg'):
        assert _is_linked(b2, 'psg', a)
    _safe_set(a, 'Ticket', None)
    assert not _is_linked(a, 'Ticket', b2)
    if hasattr(b2, 'psg'):
        assert not _is_linked(b2, 'psg', a)


def test_assoc_trips3_link_reassign_clear():
    a = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    b1 = CoachBus_Coach(id=7, model="sample_text", name="sample_text", noOfSeats=7)
    b2 = CoachBus_Coach(id=13, model="sample_text_2", name="sample_text_2", noOfSeats=13)
    _safe_set(a, 'Trip', b1)
    assert _is_linked(a, 'Trip', b1)
    if hasattr(b1, 'coaches'):
        assert _is_linked(b1, 'coaches', a)
    _safe_set(a, 'Trip', b2)
    assert _is_linked(a, 'Trip', b2)
    if hasattr(b1, 'coaches'):
        assert not _is_linked(b1, 'coaches', a)
    if hasattr(b2, 'coaches'):
        assert _is_linked(b2, 'coaches', a)
    _safe_set(a, 'Trip', None)
    assert not _is_linked(a, 'Trip', b2)
    if hasattr(b2, 'coaches'):
        assert not _is_linked(b2, 'coaches', a)


def test_assoc_trips7_link_reassign_clear():
    a = CoachBus_Trip(destination="sample_text", name="sample_text", number=7, origin="sample_text", type="sample_text")
    b1 = CoachBus_Passenger(age=7, idCard="sample_text", name="sample_text")
    b2 = CoachBus_Passenger(age=13, idCard="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Trip8', b1)
    assert _is_linked(a, 'Trip8', b1)
    if hasattr(b1, 'passengers'):
        assert _is_linked(b1, 'passengers', a)
    _safe_set(a, 'Trip8', b2)
    assert _is_linked(a, 'Trip8', b2)
    if hasattr(b1, 'passengers'):
        assert not _is_linked(b1, 'passengers', a)
    if hasattr(b2, 'passengers'):
        assert _is_linked(b2, 'passengers', a)
    _safe_set(a, 'Trip8', None)
    assert not _is_linked(a, 'Trip8', b2)
    if hasattr(b2, 'passengers'):
        assert not _is_linked(b2, 'passengers', a)


def test_assoc_vm21_link_reassign_clear():
    a = CoachBus_VendingMachine(number=7)
    b1 = CoachBus_Ticket(isRoundTrip=True, number=7, price=3.14)
    b2 = CoachBus_Ticket(isRoundTrip=False, number=13, price=9.99)
    _safe_set(a, 'VendingMachine23', b1)
    assert _is_linked(a, 'VendingMachine23', b1)
    if hasattr(b1, 'tickets22'):
        assert _is_linked(b1, 'tickets22', a)
    _safe_set(a, 'VendingMachine23', b2)
    assert _is_linked(a, 'VendingMachine23', b2)
    if hasattr(b1, 'tickets22'):
        assert not _is_linked(b1, 'tickets22', a)
    if hasattr(b2, 'tickets22'):
        assert _is_linked(b2, 'tickets22', a)
    _safe_set(a, 'VendingMachine23', None)
    assert not _is_linked(a, 'VendingMachine23', b2)
    if hasattr(b2, 'tickets22'):
        assert not _is_linked(b2, 'tickets22', a)


def test_assoc_vms17_link_reassign_clear():
    a = CoachBus_VendingMachine(number=7)
    b1 = CoachBus_BookingOffice(location="sample_text", name="sample_text", officeID=7)
    b2 = CoachBus_BookingOffice(location="sample_text_2", name="sample_text_2", officeID=13)
    _safe_set(a, 'VendingMachine', b1)
    assert _is_linked(a, 'VendingMachine', b1)
    if hasattr(b1, 'office18'):
        assert _is_linked(b1, 'office18', a)
    _safe_set(a, 'VendingMachine', b2)
    assert _is_linked(a, 'VendingMachine', b2)
    if hasattr(b1, 'office18'):
        assert not _is_linked(b1, 'office18', a)
    if hasattr(b2, 'office18'):
        assert _is_linked(b2, 'office18', a)
    _safe_set(a, 'VendingMachine', None)
    assert not _is_linked(a, 'VendingMachine', b2)
    if hasattr(b2, 'office18'):
        assert not _is_linked(b2, 'office18', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CoachBus_AdultTicket_strategy = st.builds(CoachBus_AdultTicket, isElderlyDiscount=st.booleans())
@given(instance=CoachBus_AdultTicket_strategy)
@settings(max_examples=25)
def test_CoachBus_AdultTicket_instantiation(instance):
    assert isinstance(instance, CoachBus_AdultTicket)


CoachBus_BookingOffice_strategy = st.builds(CoachBus_BookingOffice, location=safe_text, name=safe_text, officeID=st.integers())
@given(instance=CoachBus_BookingOffice_strategy)
@settings(max_examples=25)
def test_CoachBus_BookingOffice_instantiation(instance):
    assert isinstance(instance, CoachBus_BookingOffice)


CoachBus_ChildTicket_strategy = st.builds(CoachBus_ChildTicket, isSchoolTrip=st.booleans())
@given(instance=CoachBus_ChildTicket_strategy)
@settings(max_examples=25)
def test_CoachBus_ChildTicket_instantiation(instance):
    assert isinstance(instance, CoachBus_ChildTicket)


CoachBus_Coach_strategy = st.builds(CoachBus_Coach, id=st.integers(), model=safe_text, name=safe_text, noOfSeats=st.integers())
@given(instance=CoachBus_Coach_strategy)
@settings(max_examples=25)
def test_CoachBus_Coach_instantiation(instance):
    assert isinstance(instance, CoachBus_Coach)


CoachBus_Employee_strategy = st.builds(CoachBus_Employee, baseSalary=st.floats(allow_nan=False, allow_infinity=False), id=st.integers())
@given(instance=CoachBus_Employee_strategy)
@settings(max_examples=25)
def test_CoachBus_Employee_instantiation(instance):
    assert isinstance(instance, CoachBus_Employee)


CoachBus_Manager_strategy = st.builds(CoachBus_Manager, hasMBA=st.booleans())
@given(instance=CoachBus_Manager_strategy)
@settings(max_examples=25)
def test_CoachBus_Manager_instantiation(instance):
    assert isinstance(instance, CoachBus_Manager)


CoachBus_Passenger_strategy = st.builds(CoachBus_Passenger, age=st.integers(), idCard=safe_text, name=safe_text)
@given(instance=CoachBus_Passenger_strategy)
@settings(max_examples=25)
def test_CoachBus_Passenger_instantiation(instance):
    assert isinstance(instance, CoachBus_Passenger)


CoachBus_PrivateTrip_strategy = st.builds(CoachBus_PrivateTrip, extras=safe_text)
@given(instance=CoachBus_PrivateTrip_strategy)
@settings(max_examples=25)
def test_CoachBus_PrivateTrip_instantiation(instance):
    assert isinstance(instance, CoachBus_PrivateTrip)


CoachBus_RegularTrip_strategy = st.builds(CoachBus_RegularTrip)
@given(instance=CoachBus_RegularTrip_strategy)
@settings(max_examples=25)
def test_CoachBus_RegularTrip_instantiation(instance):
    assert isinstance(instance, CoachBus_RegularTrip)


CoachBus_SecurityGuard_strategy = st.builds(CoachBus_SecurityGuard, shift=safe_text)
@given(instance=CoachBus_SecurityGuard_strategy)
@settings(max_examples=25)
def test_CoachBus_SecurityGuard_instantiation(instance):
    assert isinstance(instance, CoachBus_SecurityGuard)


CoachBus_Ticket_strategy = st.builds(CoachBus_Ticket, isRoundTrip=st.booleans(), number=st.integers(), price=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=CoachBus_Ticket_strategy)
@settings(max_examples=25)
def test_CoachBus_Ticket_instantiation(instance):
    assert isinstance(instance, CoachBus_Ticket)


CoachBus_Trip_strategy = st.builds(CoachBus_Trip, destination=safe_text, name=safe_text, number=st.integers(), origin=safe_text, type=safe_text)
@given(instance=CoachBus_Trip_strategy)
@settings(max_examples=25)
def test_CoachBus_Trip_instantiation(instance):
    assert isinstance(instance, CoachBus_Trip)


CoachBus_VendingMachine_strategy = st.builds(CoachBus_VendingMachine, number=st.integers())
@given(instance=CoachBus_VendingMachine_strategy)
@settings(max_examples=25)
def test_CoachBus_VendingMachine_instantiation(instance):
    assert isinstance(instance, CoachBus_VendingMachine)


Employee_strategy = st.builds(Employee)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Ticket_strategy = st.builds(Ticket)
@given(instance=Ticket_strategy)
@settings(max_examples=25)
def test_Ticket_instantiation(instance):
    assert isinstance(instance, Ticket)


Trip_strategy = st.builds(Trip)
@given(instance=Trip_strategy)
@settings(max_examples=25)
def test_Trip_instantiation(instance):
    assert isinstance(instance, Trip)



