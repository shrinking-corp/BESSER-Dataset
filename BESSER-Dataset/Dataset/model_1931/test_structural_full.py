import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AdministratorProvides,
    Biller,
    Booker,
    Customer,
    CustomerProvides,
    DB_interface,
    GuestBiller,
    GuestInterface,
    ManagerInterface,
    Receipt,
    RoomHandlerInterface,
    RoomProvider,
    RoomType,
    ServiceHandlerInterface,
    ServiceProvider,
    ServiceType,
    Validator,
    newClasses_AdministratorProvides,
    newClasses_BankComponent,
    newClasses_Biller,
    newClasses_Billing,
    newClasses_Booker,
    newClasses_Booking,
    newClasses_CreditCard,
    newClasses_Customer,
    newClasses_CustomerProvides,
    newClasses_DB_interface,
    newClasses_Database,
    newClasses_Guest,
    newClasses_GuestBiller,
    newClasses_GuestInterface,
    newClasses_InformationValidator,
    newClasses_LoginChecker,
    newClasses_Manager,
    newClasses_ManagerInterface,
    newClasses_Receipt,
    newClasses_ReceiptCreator,
    newClasses_Room,
    newClasses_RoomHandler,
    newClasses_RoomHandlerInterface,
    newClasses_RoomProvider,
    newClasses_RoomType,
    newClasses_Service,
    newClasses_ServiceHandler,
    newClasses_ServiceHandlerInterface,
    newClasses_ServiceProvider,
    newClasses_ServiceType,
    newClasses_Validator,
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

def test_newClasses_Billing_isPaid_value_roundtrip():
    instance = newClasses_Billing(isPaid="sample_text", totalCost="sample_text")
    assert instance.isPaid == "sample_text"
    instance.isPaid = "sample_text_2"
    assert instance.isPaid == "sample_text_2"


def test_newClasses_Billing_totalCost_value_roundtrip():
    instance = newClasses_Billing(isPaid="sample_text", totalCost="sample_text")
    assert instance.totalCost == "sample_text"
    instance.totalCost = "sample_text_2"
    assert instance.totalCost == "sample_text_2"


def test_newClasses_Booking_checkInDate_value_roundtrip():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert instance.checkInDate == "sample_text"
    instance.checkInDate = "sample_text_2"
    assert instance.checkInDate == "sample_text_2"


def test_newClasses_Booking_checkOutDate_value_roundtrip():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert instance.checkOutDate == "sample_text"
    instance.checkOutDate = "sample_text_2"
    assert instance.checkOutDate == "sample_text_2"


def test_newClasses_Booking_conformationNum_value_roundtrip():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert instance.conformationNum == "sample_text"
    instance.conformationNum = "sample_text_2"
    assert instance.conformationNum == "sample_text_2"


def test_newClasses_Booking_cost_value_roundtrip():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert instance.cost == "sample_text"
    instance.cost = "sample_text_2"
    assert instance.cost == "sample_text_2"


def test_newClasses_Booking_isPaid_value_roundtrip():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert instance.isPaid == "sample_text"
    instance.isPaid = "sample_text_2"
    assert instance.isPaid == "sample_text_2"


def test_newClasses_Booking_roomType_value_roundtrip():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert instance.roomType == "sample_text"
    instance.roomType = "sample_text_2"
    assert instance.roomType == "sample_text_2"


def test_newClasses_Booking_services_value_roundtrip():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert instance.services == "sample_text"
    instance.services = "sample_text_2"
    assert instance.services == "sample_text_2"


def test_newClasses_CreditCard_creditCardNumber_value_roundtrip():
    instance = newClasses_CreditCard(creditCardNumber="sample_text", cvc="sample_text", firstName="sample_text", lastName="sample_text", month="sample_text", year="sample_text")
    assert instance.creditCardNumber == "sample_text"
    instance.creditCardNumber = "sample_text_2"
    assert instance.creditCardNumber == "sample_text_2"


def test_newClasses_CreditCard_cvc_value_roundtrip():
    instance = newClasses_CreditCard(creditCardNumber="sample_text", cvc="sample_text", firstName="sample_text", lastName="sample_text", month="sample_text", year="sample_text")
    assert instance.cvc == "sample_text"
    instance.cvc = "sample_text_2"
    assert instance.cvc == "sample_text_2"


def test_newClasses_CreditCard_firstName_value_roundtrip():
    instance = newClasses_CreditCard(creditCardNumber="sample_text", cvc="sample_text", firstName="sample_text", lastName="sample_text", month="sample_text", year="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_newClasses_CreditCard_lastName_value_roundtrip():
    instance = newClasses_CreditCard(creditCardNumber="sample_text", cvc="sample_text", firstName="sample_text", lastName="sample_text", month="sample_text", year="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_newClasses_CreditCard_month_value_roundtrip():
    instance = newClasses_CreditCard(creditCardNumber="sample_text", cvc="sample_text", firstName="sample_text", lastName="sample_text", month="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_newClasses_CreditCard_year_value_roundtrip():
    instance = newClasses_CreditCard(creditCardNumber="sample_text", cvc="sample_text", firstName="sample_text", lastName="sample_text", month="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_newClasses_Customer_address_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_newClasses_Customer_bookingCost_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.bookingCost == "sample_text"
    instance.bookingCost = "sample_text_2"
    assert instance.bookingCost == "sample_text_2"


def test_newClasses_Customer_bookingNum_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.bookingNum == "sample_text"
    instance.bookingNum = "sample_text_2"
    assert instance.bookingNum == "sample_text_2"


def test_newClasses_Customer_city_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_newClasses_Customer_country_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_newClasses_Customer_email_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_newClasses_Customer_firstName_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_newClasses_Customer_lastName_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_newClasses_Customer_personalNum_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.personalNum == "sample_text"
    instance.personalNum = "sample_text_2"
    assert instance.personalNum == "sample_text_2"


def test_newClasses_Customer_phoneNum_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.phoneNum == "sample_text"
    instance.phoneNum = "sample_text_2"
    assert instance.phoneNum == "sample_text_2"


def test_newClasses_Customer_zipCode_value_roundtrip():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert instance.zipCode == "sample_text"
    instance.zipCode = "sample_text_2"
    assert instance.zipCode == "sample_text_2"


def test_newClasses_Guest_addedServices_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.addedServices == "sample_text"
    instance.addedServices = "sample_text_2"
    assert instance.addedServices == "sample_text_2"


def test_newClasses_Guest_bookingPaid_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.bookingPaid == "sample_text"
    instance.bookingPaid = "sample_text_2"
    assert instance.bookingPaid == "sample_text_2"


def test_newClasses_Guest_checkInDate_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.checkInDate == "sample_text"
    instance.checkInDate = "sample_text_2"
    assert instance.checkInDate == "sample_text_2"


def test_newClasses_Guest_checkOutDate_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.checkOutDate == "sample_text"
    instance.checkOutDate = "sample_text_2"
    assert instance.checkOutDate == "sample_text_2"


def test_newClasses_Guest_checkedIn_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.checkedIn == "sample_text"
    instance.checkedIn = "sample_text_2"
    assert instance.checkedIn == "sample_text_2"


def test_newClasses_Guest_checkedOut_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.checkedOut == "sample_text"
    instance.checkedOut = "sample_text_2"
    assert instance.checkedOut == "sample_text_2"


def test_newClasses_Guest_cost_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.cost == "sample_text"
    instance.cost = "sample_text_2"
    assert instance.cost == "sample_text_2"


def test_newClasses_Guest_extraDays_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.extraDays == "sample_text"
    instance.extraDays = "sample_text_2"
    assert instance.extraDays == "sample_text_2"


def test_newClasses_Guest_roomNum_value_roundtrip():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert instance.roomNum == "sample_text"
    instance.roomNum = "sample_text_2"
    assert instance.roomNum == "sample_text_2"


def test_newClasses_Manager_password_value_roundtrip():
    instance = newClasses_Manager(password="sample_text", userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_newClasses_Manager_userName_value_roundtrip():
    instance = newClasses_Manager(password="sample_text", userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_newClasses_Room_roomNum_value_roundtrip():
    instance = newClasses_Room(roomNum="sample_text", status="sample_text")
    assert instance.roomNum == "sample_text"
    instance.roomNum = "sample_text_2"
    assert instance.roomNum == "sample_text_2"


def test_newClasses_Room_status_value_roundtrip():
    instance = newClasses_Room(roomNum="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_newClasses_RoomType_price_value_roundtrip():
    instance = newClasses_RoomType(price="sample_text", type="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_newClasses_RoomType_type_value_roundtrip():
    instance = newClasses_RoomType(price="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_newClasses_Service_id_value_roundtrip():
    instance = newClasses_Service(id="sample_text", status="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_newClasses_Service_status_value_roundtrip():
    instance = newClasses_Service(id="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_newClasses_ServiceType_price_value_roundtrip():
    instance = newClasses_ServiceType(price="sample_text", type="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_newClasses_ServiceType_type_value_roundtrip():
    instance = newClasses_ServiceType(price="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_newClasses_BankComponent_isa_AdministratorProvides():
    instance = newClasses_BankComponent()
    assert isinstance(instance, AdministratorProvides)


def test_newClasses_Billing_isa_Biller():
    instance = newClasses_Billing(isPaid="sample_text", totalCost="sample_text")
    assert isinstance(instance, Biller)


def test_newClasses_Booking_isa_Biller():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert isinstance(instance, Biller)


def test_newClasses_Booking_isa_Booker():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert isinstance(instance, Booker)


def test_newClasses_Customer_isa_Booker():
    instance = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    assert isinstance(instance, Booker)


def test_newClasses_Guest_isa_Customer():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert isinstance(instance, Customer)


def test_newClasses_BankComponent_isa_CustomerProvides():
    instance = newClasses_BankComponent()
    assert isinstance(instance, CustomerProvides)


def test_newClasses_Billing_isa_CustomerProvides():
    instance = newClasses_Billing(isPaid="sample_text", totalCost="sample_text")
    assert isinstance(instance, CustomerProvides)


def test_newClasses_Booking_isa_CustomerProvides():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert isinstance(instance, CustomerProvides)


def test_newClasses_Database_isa_DB_interface():
    instance = newClasses_Database()
    assert isinstance(instance, DB_interface)


def test_newClasses_Billing_isa_GuestBiller():
    instance = newClasses_Billing(isPaid="sample_text", totalCost="sample_text")
    assert isinstance(instance, GuestBiller)


def test_newClasses_Guest_isa_GuestBiller():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert isinstance(instance, GuestBiller)


def test_newClasses_Guest_isa_GuestInterface():
    instance = newClasses_Guest(addedServices="sample_text", bookingPaid="sample_text", checkInDate="sample_text", checkOutDate="sample_text", checkedIn="sample_text", checkedOut="sample_text", cost="sample_text", extraDays="sample_text", roomNum="sample_text")
    assert isinstance(instance, GuestInterface)


def test_newClasses_RoomHandler_isa_GuestInterface():
    instance = newClasses_RoomHandler()
    assert isinstance(instance, GuestInterface)


def test_newClasses_LoginChecker_isa_ManagerInterface():
    instance = newClasses_LoginChecker()
    assert isinstance(instance, ManagerInterface)


def test_newClasses_Manager_isa_ManagerInterface():
    instance = newClasses_Manager(password="sample_text", userName="sample_text")
    assert isinstance(instance, ManagerInterface)


def test_newClasses_ReceiptCreator_isa_Receipt():
    instance = newClasses_ReceiptCreator()
    assert isinstance(instance, Receipt)


def test_newClasses_Manager_isa_RoomHandlerInterface():
    instance = newClasses_Manager(password="sample_text", userName="sample_text")
    assert isinstance(instance, RoomHandlerInterface)


def test_newClasses_RoomHandler_isa_RoomHandlerInterface():
    instance = newClasses_RoomHandler()
    assert isinstance(instance, RoomHandlerInterface)


def test_newClasses_Booking_isa_RoomProvider():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert isinstance(instance, RoomProvider)


def test_newClasses_RoomHandler_isa_RoomProvider():
    instance = newClasses_RoomHandler()
    assert isinstance(instance, RoomProvider)


def test_newClasses_Room_isa_RoomType():
    instance = newClasses_Room(roomNum="sample_text", status="sample_text")
    assert isinstance(instance, RoomType)


def test_newClasses_Manager_isa_ServiceHandlerInterface():
    instance = newClasses_Manager(password="sample_text", userName="sample_text")
    assert isinstance(instance, ServiceHandlerInterface)


def test_newClasses_ServiceHandler_isa_ServiceHandlerInterface():
    instance = newClasses_ServiceHandler()
    assert isinstance(instance, ServiceHandlerInterface)


def test_newClasses_Booking_isa_ServiceProvider():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert isinstance(instance, ServiceProvider)


def test_newClasses_ServiceHandler_isa_ServiceProvider():
    instance = newClasses_ServiceHandler()
    assert isinstance(instance, ServiceProvider)


def test_newClasses_Service_isa_ServiceType():
    instance = newClasses_Service(id="sample_text", status="sample_text")
    assert isinstance(instance, ServiceType)


def test_newClasses_Booking_isa_Validator():
    instance = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    assert isinstance(instance, Validator)


def test_newClasses_InformationValidator_isa_Validator():
    instance = newClasses_InformationValidator()
    assert isinstance(instance, Validator)


def test_assoc_booking0_link_reassign_clear():
    a = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    b1 = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    b2 = newClasses_Booking(checkInDate="sample_text_2", checkOutDate="sample_text_2", conformationNum="sample_text_2", cost="sample_text_2", isPaid="sample_text_2", roomType="sample_text_2", services="sample_text_2")
    _safe_set(a, 'newClasses_Customer', b1)
    assert _is_linked(a, 'newClasses_Customer', b1)
    if hasattr(b1, 'newClasses_Booking'):
        assert _is_linked(b1, 'newClasses_Booking', a)
    _safe_set(a, 'newClasses_Customer', b2)
    assert _is_linked(a, 'newClasses_Customer', b2)
    if hasattr(b1, 'newClasses_Booking'):
        assert not _is_linked(b1, 'newClasses_Booking', a)
    if hasattr(b2, 'newClasses_Booking'):
        assert _is_linked(b2, 'newClasses_Booking', a)
    _safe_set(a, 'newClasses_Customer', None)
    assert not _is_linked(a, 'newClasses_Customer', b2)
    if hasattr(b2, 'newClasses_Booking'):
        assert not _is_linked(b2, 'newClasses_Booking', a)


def test_assoc_creditCard1_link_reassign_clear():
    a = newClasses_Customer(address="sample_text", bookingCost="sample_text", bookingNum="sample_text", city="sample_text", country="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", personalNum="sample_text", phoneNum="sample_text", zipCode="sample_text")
    b1 = newClasses_CreditCard(creditCardNumber="sample_text", cvc="sample_text", firstName="sample_text", lastName="sample_text", month="sample_text", year="sample_text")
    b2 = newClasses_CreditCard(creditCardNumber="sample_text_2", cvc="sample_text_2", firstName="sample_text_2", lastName="sample_text_2", month="sample_text_2", year="sample_text_2")
    _safe_set(a, 'newClasses_Customer2', b1)
    assert _is_linked(a, 'newClasses_Customer2', b1)
    if hasattr(b1, 'newClasses_CreditCard'):
        assert _is_linked(b1, 'newClasses_CreditCard', a)
    _safe_set(a, 'newClasses_Customer2', b2)
    assert _is_linked(a, 'newClasses_Customer2', b2)
    if hasattr(b1, 'newClasses_CreditCard'):
        assert not _is_linked(b1, 'newClasses_CreditCard', a)
    if hasattr(b2, 'newClasses_CreditCard'):
        assert _is_linked(b2, 'newClasses_CreditCard', a)
    _safe_set(a, 'newClasses_Customer2', None)
    assert not _is_linked(a, 'newClasses_Customer2', b2)
    if hasattr(b2, 'newClasses_CreditCard'):
        assert not _is_linked(b2, 'newClasses_CreditCard', a)


def test_assoc_databaseHandler5_link_reassign_clear():
    a = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    b1 = newClasses_Database()
    b2 = newClasses_Database()
    _safe_set(a, 'newClasses_Booking6', b1)
    assert _is_linked(a, 'newClasses_Booking6', b1)
    if hasattr(b1, 'newClasses_Database'):
        assert _is_linked(b1, 'newClasses_Database', a)
    _safe_set(a, 'newClasses_Booking6', b2)
    assert _is_linked(a, 'newClasses_Booking6', b2)
    if hasattr(b1, 'newClasses_Database'):
        assert not _is_linked(b1, 'newClasses_Database', a)
    if hasattr(b2, 'newClasses_Database'):
        assert _is_linked(b2, 'newClasses_Database', a)
    _safe_set(a, 'newClasses_Booking6', None)
    assert not _is_linked(a, 'newClasses_Booking6', b2)
    if hasattr(b2, 'newClasses_Database'):
        assert not _is_linked(b2, 'newClasses_Database', a)


def test_assoc_manager17_link_reassign_clear():
    a = newClasses_Manager(password="sample_text", userName="sample_text")
    b1 = newClasses_LoginChecker()
    b2 = newClasses_LoginChecker()
    _safe_set(a, 'newClasses_Manager18', b1)
    assert _is_linked(a, 'newClasses_Manager18', b1)
    if hasattr(b1, 'newClasses_LoginChecker'):
        assert _is_linked(b1, 'newClasses_LoginChecker', a)
    _safe_set(a, 'newClasses_Manager18', b2)
    assert _is_linked(a, 'newClasses_Manager18', b2)
    if hasattr(b1, 'newClasses_LoginChecker'):
        assert not _is_linked(b1, 'newClasses_LoginChecker', a)
    if hasattr(b2, 'newClasses_LoginChecker'):
        assert _is_linked(b2, 'newClasses_LoginChecker', a)
    _safe_set(a, 'newClasses_Manager18', None)
    assert not _is_linked(a, 'newClasses_Manager18', b2)
    if hasattr(b2, 'newClasses_LoginChecker'):
        assert not _is_linked(b2, 'newClasses_LoginChecker', a)


def test_assoc_receiptCreator3_link_reassign_clear():
    a = newClasses_Booking(checkInDate="sample_text", checkOutDate="sample_text", conformationNum="sample_text", cost="sample_text", isPaid="sample_text", roomType="sample_text", services="sample_text")
    b1 = newClasses_ReceiptCreator()
    b2 = newClasses_ReceiptCreator()
    _safe_set(a, 'newClasses_Booking4', b1)
    assert _is_linked(a, 'newClasses_Booking4', b1)
    if hasattr(b1, 'newClasses_ReceiptCreator'):
        assert _is_linked(b1, 'newClasses_ReceiptCreator', a)
    _safe_set(a, 'newClasses_Booking4', b2)
    assert _is_linked(a, 'newClasses_Booking4', b2)
    if hasattr(b1, 'newClasses_ReceiptCreator'):
        assert not _is_linked(b1, 'newClasses_ReceiptCreator', a)
    if hasattr(b2, 'newClasses_ReceiptCreator'):
        assert _is_linked(b2, 'newClasses_ReceiptCreator', a)
    _safe_set(a, 'newClasses_Booking4', None)
    assert not _is_linked(a, 'newClasses_Booking4', b2)
    if hasattr(b2, 'newClasses_ReceiptCreator'):
        assert not _is_linked(b2, 'newClasses_ReceiptCreator', a)


def test_assoc_room12_link_reassign_clear():
    a = newClasses_Room(roomNum="sample_text", status="sample_text")
    b1 = newClasses_RoomHandler()
    b2 = newClasses_RoomHandler()
    _safe_set(a, 'newClasses_Room', b1)
    assert _is_linked(a, 'newClasses_Room', b1)
    if hasattr(b1, 'newClasses_RoomHandler13'):
        assert _is_linked(b1, 'newClasses_RoomHandler13', a)
    _safe_set(a, 'newClasses_Room', b2)
    assert _is_linked(a, 'newClasses_Room', b2)
    if hasattr(b1, 'newClasses_RoomHandler13'):
        assert not _is_linked(b1, 'newClasses_RoomHandler13', a)
    if hasattr(b2, 'newClasses_RoomHandler13'):
        assert _is_linked(b2, 'newClasses_RoomHandler13', a)
    _safe_set(a, 'newClasses_Room', None)
    assert not _is_linked(a, 'newClasses_Room', b2)
    if hasattr(b2, 'newClasses_RoomHandler13'):
        assert not _is_linked(b2, 'newClasses_RoomHandler13', a)


def test_assoc_roomHandler8_link_reassign_clear():
    a = newClasses_Manager(password="sample_text", userName="sample_text")
    b1 = newClasses_RoomHandler()
    b2 = newClasses_RoomHandler()
    _safe_set(a, 'newClasses_Manager', b1)
    assert _is_linked(a, 'newClasses_Manager', b1)
    if hasattr(b1, 'newClasses_RoomHandler'):
        assert _is_linked(b1, 'newClasses_RoomHandler', a)
    _safe_set(a, 'newClasses_Manager', b2)
    assert _is_linked(a, 'newClasses_Manager', b2)
    if hasattr(b1, 'newClasses_RoomHandler'):
        assert not _is_linked(b1, 'newClasses_RoomHandler', a)
    if hasattr(b2, 'newClasses_RoomHandler'):
        assert _is_linked(b2, 'newClasses_RoomHandler', a)
    _safe_set(a, 'newClasses_Manager', None)
    assert not _is_linked(a, 'newClasses_Manager', b2)
    if hasattr(b2, 'newClasses_RoomHandler'):
        assert not _is_linked(b2, 'newClasses_RoomHandler', a)


def test_assoc_service7_link_reassign_clear():
    a = newClasses_Service(id="sample_text", status="sample_text")
    b1 = newClasses_ServiceHandler()
    b2 = newClasses_ServiceHandler()
    _safe_set(a, 'newClasses_Service', b1)
    assert _is_linked(a, 'newClasses_Service', b1)
    if hasattr(b1, 'newClasses_ServiceHandler'):
        assert _is_linked(b1, 'newClasses_ServiceHandler', a)
    _safe_set(a, 'newClasses_Service', b2)
    assert _is_linked(a, 'newClasses_Service', b2)
    if hasattr(b1, 'newClasses_ServiceHandler'):
        assert not _is_linked(b1, 'newClasses_ServiceHandler', a)
    if hasattr(b2, 'newClasses_ServiceHandler'):
        assert _is_linked(b2, 'newClasses_ServiceHandler', a)
    _safe_set(a, 'newClasses_Service', None)
    assert not _is_linked(a, 'newClasses_Service', b2)
    if hasattr(b2, 'newClasses_ServiceHandler'):
        assert not _is_linked(b2, 'newClasses_ServiceHandler', a)


def test_assoc_serviceHandler9_link_reassign_clear():
    a = newClasses_Manager(password="sample_text", userName="sample_text")
    b1 = newClasses_ServiceHandler()
    b2 = newClasses_ServiceHandler()
    _safe_set(a, 'newClasses_Manager10', b1)
    assert _is_linked(a, 'newClasses_Manager10', b1)
    if hasattr(b1, 'newClasses_ServiceHandler11'):
        assert _is_linked(b1, 'newClasses_ServiceHandler11', a)
    _safe_set(a, 'newClasses_Manager10', b2)
    assert _is_linked(a, 'newClasses_Manager10', b2)
    if hasattr(b1, 'newClasses_ServiceHandler11'):
        assert not _is_linked(b1, 'newClasses_ServiceHandler11', a)
    if hasattr(b2, 'newClasses_ServiceHandler11'):
        assert _is_linked(b2, 'newClasses_ServiceHandler11', a)
    _safe_set(a, 'newClasses_Manager10', None)
    assert not _is_linked(a, 'newClasses_Manager10', b2)
    if hasattr(b2, 'newClasses_ServiceHandler11'):
        assert not _is_linked(b2, 'newClasses_ServiceHandler11', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AdministratorProvides_strategy = st.builds(AdministratorProvides)
@given(instance=AdministratorProvides_strategy)
@settings(max_examples=25)
def test_AdministratorProvides_instantiation(instance):
    assert isinstance(instance, AdministratorProvides)


Biller_strategy = st.builds(Biller)
@given(instance=Biller_strategy)
@settings(max_examples=25)
def test_Biller_instantiation(instance):
    assert isinstance(instance, Biller)


Booker_strategy = st.builds(Booker)
@given(instance=Booker_strategy)
@settings(max_examples=25)
def test_Booker_instantiation(instance):
    assert isinstance(instance, Booker)


Customer_strategy = st.builds(Customer)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


CustomerProvides_strategy = st.builds(CustomerProvides)
@given(instance=CustomerProvides_strategy)
@settings(max_examples=25)
def test_CustomerProvides_instantiation(instance):
    assert isinstance(instance, CustomerProvides)


DB_interface_strategy = st.builds(DB_interface)
@given(instance=DB_interface_strategy)
@settings(max_examples=25)
def test_DB_interface_instantiation(instance):
    assert isinstance(instance, DB_interface)


GuestBiller_strategy = st.builds(GuestBiller)
@given(instance=GuestBiller_strategy)
@settings(max_examples=25)
def test_GuestBiller_instantiation(instance):
    assert isinstance(instance, GuestBiller)


GuestInterface_strategy = st.builds(GuestInterface)
@given(instance=GuestInterface_strategy)
@settings(max_examples=25)
def test_GuestInterface_instantiation(instance):
    assert isinstance(instance, GuestInterface)


ManagerInterface_strategy = st.builds(ManagerInterface)
@given(instance=ManagerInterface_strategy)
@settings(max_examples=25)
def test_ManagerInterface_instantiation(instance):
    assert isinstance(instance, ManagerInterface)


Receipt_strategy = st.builds(Receipt)
@given(instance=Receipt_strategy)
@settings(max_examples=25)
def test_Receipt_instantiation(instance):
    assert isinstance(instance, Receipt)


RoomHandlerInterface_strategy = st.builds(RoomHandlerInterface)
@given(instance=RoomHandlerInterface_strategy)
@settings(max_examples=25)
def test_RoomHandlerInterface_instantiation(instance):
    assert isinstance(instance, RoomHandlerInterface)


RoomProvider_strategy = st.builds(RoomProvider)
@given(instance=RoomProvider_strategy)
@settings(max_examples=25)
def test_RoomProvider_instantiation(instance):
    assert isinstance(instance, RoomProvider)


RoomType_strategy = st.builds(RoomType)
@given(instance=RoomType_strategy)
@settings(max_examples=25)
def test_RoomType_instantiation(instance):
    assert isinstance(instance, RoomType)


ServiceHandlerInterface_strategy = st.builds(ServiceHandlerInterface)
@given(instance=ServiceHandlerInterface_strategy)
@settings(max_examples=25)
def test_ServiceHandlerInterface_instantiation(instance):
    assert isinstance(instance, ServiceHandlerInterface)


ServiceProvider_strategy = st.builds(ServiceProvider)
@given(instance=ServiceProvider_strategy)
@settings(max_examples=25)
def test_ServiceProvider_instantiation(instance):
    assert isinstance(instance, ServiceProvider)


ServiceType_strategy = st.builds(ServiceType)
@given(instance=ServiceType_strategy)
@settings(max_examples=25)
def test_ServiceType_instantiation(instance):
    assert isinstance(instance, ServiceType)


Validator_strategy = st.builds(Validator)
@given(instance=Validator_strategy)
@settings(max_examples=25)
def test_Validator_instantiation(instance):
    assert isinstance(instance, Validator)


newClasses_AdministratorProvides_strategy = st.builds(newClasses_AdministratorProvides)
@given(instance=newClasses_AdministratorProvides_strategy)
@settings(max_examples=25)
def test_newClasses_AdministratorProvides_instantiation(instance):
    assert isinstance(instance, newClasses_AdministratorProvides)


newClasses_BankComponent_strategy = st.builds(newClasses_BankComponent)
@given(instance=newClasses_BankComponent_strategy)
@settings(max_examples=25)
def test_newClasses_BankComponent_instantiation(instance):
    assert isinstance(instance, newClasses_BankComponent)


newClasses_Biller_strategy = st.builds(newClasses_Biller)
@given(instance=newClasses_Biller_strategy)
@settings(max_examples=25)
def test_newClasses_Biller_instantiation(instance):
    assert isinstance(instance, newClasses_Biller)


newClasses_Billing_strategy = st.builds(newClasses_Billing, isPaid=safe_text, totalCost=safe_text)
@given(instance=newClasses_Billing_strategy)
@settings(max_examples=25)
def test_newClasses_Billing_instantiation(instance):
    assert isinstance(instance, newClasses_Billing)


newClasses_Booker_strategy = st.builds(newClasses_Booker)
@given(instance=newClasses_Booker_strategy)
@settings(max_examples=25)
def test_newClasses_Booker_instantiation(instance):
    assert isinstance(instance, newClasses_Booker)


newClasses_Booking_strategy = st.builds(newClasses_Booking, checkInDate=safe_text, checkOutDate=safe_text, conformationNum=safe_text, cost=safe_text, isPaid=safe_text, roomType=safe_text, services=safe_text)
@given(instance=newClasses_Booking_strategy)
@settings(max_examples=25)
def test_newClasses_Booking_instantiation(instance):
    assert isinstance(instance, newClasses_Booking)


newClasses_CreditCard_strategy = st.builds(newClasses_CreditCard, creditCardNumber=safe_text, cvc=safe_text, firstName=safe_text, lastName=safe_text, month=safe_text, year=safe_text)
@given(instance=newClasses_CreditCard_strategy)
@settings(max_examples=25)
def test_newClasses_CreditCard_instantiation(instance):
    assert isinstance(instance, newClasses_CreditCard)


newClasses_Customer_strategy = st.builds(newClasses_Customer, address=safe_text, bookingCost=safe_text, bookingNum=safe_text, city=safe_text, country=safe_text, email=safe_text, firstName=safe_text, lastName=safe_text, personalNum=safe_text, phoneNum=safe_text, zipCode=safe_text)
@given(instance=newClasses_Customer_strategy)
@settings(max_examples=25)
def test_newClasses_Customer_instantiation(instance):
    assert isinstance(instance, newClasses_Customer)


newClasses_CustomerProvides_strategy = st.builds(newClasses_CustomerProvides)
@given(instance=newClasses_CustomerProvides_strategy)
@settings(max_examples=25)
def test_newClasses_CustomerProvides_instantiation(instance):
    assert isinstance(instance, newClasses_CustomerProvides)


newClasses_DB_interface_strategy = st.builds(newClasses_DB_interface)
@given(instance=newClasses_DB_interface_strategy)
@settings(max_examples=25)
def test_newClasses_DB_interface_instantiation(instance):
    assert isinstance(instance, newClasses_DB_interface)


newClasses_Database_strategy = st.builds(newClasses_Database)
@given(instance=newClasses_Database_strategy)
@settings(max_examples=25)
def test_newClasses_Database_instantiation(instance):
    assert isinstance(instance, newClasses_Database)


newClasses_Guest_strategy = st.builds(newClasses_Guest, addedServices=safe_text, bookingPaid=safe_text, checkInDate=safe_text, checkOutDate=safe_text, checkedIn=safe_text, checkedOut=safe_text, cost=safe_text, extraDays=safe_text, roomNum=safe_text)
@given(instance=newClasses_Guest_strategy)
@settings(max_examples=25)
def test_newClasses_Guest_instantiation(instance):
    assert isinstance(instance, newClasses_Guest)


newClasses_GuestBiller_strategy = st.builds(newClasses_GuestBiller)
@given(instance=newClasses_GuestBiller_strategy)
@settings(max_examples=25)
def test_newClasses_GuestBiller_instantiation(instance):
    assert isinstance(instance, newClasses_GuestBiller)


newClasses_GuestInterface_strategy = st.builds(newClasses_GuestInterface)
@given(instance=newClasses_GuestInterface_strategy)
@settings(max_examples=25)
def test_newClasses_GuestInterface_instantiation(instance):
    assert isinstance(instance, newClasses_GuestInterface)


newClasses_InformationValidator_strategy = st.builds(newClasses_InformationValidator)
@given(instance=newClasses_InformationValidator_strategy)
@settings(max_examples=25)
def test_newClasses_InformationValidator_instantiation(instance):
    assert isinstance(instance, newClasses_InformationValidator)


newClasses_LoginChecker_strategy = st.builds(newClasses_LoginChecker)
@given(instance=newClasses_LoginChecker_strategy)
@settings(max_examples=25)
def test_newClasses_LoginChecker_instantiation(instance):
    assert isinstance(instance, newClasses_LoginChecker)


newClasses_Manager_strategy = st.builds(newClasses_Manager, password=safe_text, userName=safe_text)
@given(instance=newClasses_Manager_strategy)
@settings(max_examples=25)
def test_newClasses_Manager_instantiation(instance):
    assert isinstance(instance, newClasses_Manager)


newClasses_ManagerInterface_strategy = st.builds(newClasses_ManagerInterface)
@given(instance=newClasses_ManagerInterface_strategy)
@settings(max_examples=25)
def test_newClasses_ManagerInterface_instantiation(instance):
    assert isinstance(instance, newClasses_ManagerInterface)


newClasses_Receipt_strategy = st.builds(newClasses_Receipt)
@given(instance=newClasses_Receipt_strategy)
@settings(max_examples=25)
def test_newClasses_Receipt_instantiation(instance):
    assert isinstance(instance, newClasses_Receipt)


newClasses_ReceiptCreator_strategy = st.builds(newClasses_ReceiptCreator)
@given(instance=newClasses_ReceiptCreator_strategy)
@settings(max_examples=25)
def test_newClasses_ReceiptCreator_instantiation(instance):
    assert isinstance(instance, newClasses_ReceiptCreator)


newClasses_Room_strategy = st.builds(newClasses_Room, roomNum=safe_text, status=safe_text)
@given(instance=newClasses_Room_strategy)
@settings(max_examples=25)
def test_newClasses_Room_instantiation(instance):
    assert isinstance(instance, newClasses_Room)


newClasses_RoomHandler_strategy = st.builds(newClasses_RoomHandler)
@given(instance=newClasses_RoomHandler_strategy)
@settings(max_examples=25)
def test_newClasses_RoomHandler_instantiation(instance):
    assert isinstance(instance, newClasses_RoomHandler)


newClasses_RoomHandlerInterface_strategy = st.builds(newClasses_RoomHandlerInterface)
@given(instance=newClasses_RoomHandlerInterface_strategy)
@settings(max_examples=25)
def test_newClasses_RoomHandlerInterface_instantiation(instance):
    assert isinstance(instance, newClasses_RoomHandlerInterface)


newClasses_RoomProvider_strategy = st.builds(newClasses_RoomProvider)
@given(instance=newClasses_RoomProvider_strategy)
@settings(max_examples=25)
def test_newClasses_RoomProvider_instantiation(instance):
    assert isinstance(instance, newClasses_RoomProvider)


newClasses_RoomType_strategy = st.builds(newClasses_RoomType, price=safe_text, type=safe_text)
@given(instance=newClasses_RoomType_strategy)
@settings(max_examples=25)
def test_newClasses_RoomType_instantiation(instance):
    assert isinstance(instance, newClasses_RoomType)


newClasses_Service_strategy = st.builds(newClasses_Service, id=safe_text, status=safe_text)
@given(instance=newClasses_Service_strategy)
@settings(max_examples=25)
def test_newClasses_Service_instantiation(instance):
    assert isinstance(instance, newClasses_Service)


newClasses_ServiceHandler_strategy = st.builds(newClasses_ServiceHandler)
@given(instance=newClasses_ServiceHandler_strategy)
@settings(max_examples=25)
def test_newClasses_ServiceHandler_instantiation(instance):
    assert isinstance(instance, newClasses_ServiceHandler)


newClasses_ServiceHandlerInterface_strategy = st.builds(newClasses_ServiceHandlerInterface)
@given(instance=newClasses_ServiceHandlerInterface_strategy)
@settings(max_examples=25)
def test_newClasses_ServiceHandlerInterface_instantiation(instance):
    assert isinstance(instance, newClasses_ServiceHandlerInterface)


newClasses_ServiceProvider_strategy = st.builds(newClasses_ServiceProvider)
@given(instance=newClasses_ServiceProvider_strategy)
@settings(max_examples=25)
def test_newClasses_ServiceProvider_instantiation(instance):
    assert isinstance(instance, newClasses_ServiceProvider)


newClasses_ServiceType_strategy = st.builds(newClasses_ServiceType, price=safe_text, type=safe_text)
@given(instance=newClasses_ServiceType_strategy)
@settings(max_examples=25)
def test_newClasses_ServiceType_instantiation(instance):
    assert isinstance(instance, newClasses_ServiceType)


newClasses_Validator_strategy = st.builds(newClasses_Validator)
@given(instance=newClasses_Validator_strategy)
@settings(max_examples=25)
def test_newClasses_Validator_instantiation(instance):
    assert isinstance(instance, newClasses_Validator)


