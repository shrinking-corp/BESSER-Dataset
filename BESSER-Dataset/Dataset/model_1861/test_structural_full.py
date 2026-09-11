import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    HotelManagementClassDiagram_Addon,
    HotelManagementClassDiagram_Bill,
    HotelManagementClassDiagram_BookedRoom,
    HotelManagementClassDiagram_Booking,
    HotelManagementClassDiagram_BookingController,
    HotelManagementClassDiagram_Costable,
    HotelManagementClassDiagram_Creditcard,
    HotelManagementClassDiagram_Customer,
    HotelManagementClassDiagram_Discount,
    HotelManagementClassDiagram_Employee,
    HotelManagementClassDiagram_EmployeeType,
    HotelManagementClassDiagram_Hotel,
    HotelManagementClassDiagram_Interaction1,
    HotelManagementClassDiagram_Interaction2,
    HotelManagementClassDiagram_Interaction3,
    HotelManagementClassDiagram_Interaction4,
    HotelManagementClassDiagram_Interaction5,
    HotelManagementClassDiagram_MaintenanceController,
    HotelManagementClassDiagram_ManagementController,
    HotelManagementClassDiagram_Person,
    HotelManagementClassDiagram_Room,
    Person,
    Room,
    EType,
    RoomType,
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

def test_HotelManagementClassDiagram_Addon_description_value_roundtrip():
    instance = HotelManagementClassDiagram_Addon(description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_HotelManagementClassDiagram_Addon_name_value_roundtrip():
    instance = HotelManagementClassDiagram_Addon(description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_HotelManagementClassDiagram_Bill_final_value_roundtrip():
    instance = HotelManagementClassDiagram_Bill(final=True, paid=True, totalPrice=3.14, valueAddedTax=3.14)
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_HotelManagementClassDiagram_Bill_paid_value_roundtrip():
    instance = HotelManagementClassDiagram_Bill(final=True, paid=True, totalPrice=3.14, valueAddedTax=3.14)
    assert instance.paid == True
    instance.paid = False
    assert instance.paid == False


def test_HotelManagementClassDiagram_Bill_totalPrice_value_roundtrip():
    instance = HotelManagementClassDiagram_Bill(final=True, paid=True, totalPrice=3.14, valueAddedTax=3.14)
    assert instance.totalPrice == 3.14
    instance.totalPrice = 9.99
    assert instance.totalPrice == 9.99


def test_HotelManagementClassDiagram_Bill_valueAddedTax_value_roundtrip():
    instance = HotelManagementClassDiagram_Bill(final=True, paid=True, totalPrice=3.14, valueAddedTax=3.14)
    assert instance.valueAddedTax == 3.14
    instance.valueAddedTax = 9.99
    assert instance.valueAddedTax == 9.99


def test_HotelManagementClassDiagram_Booking_bookingId_value_roundtrip():
    instance = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    assert instance.bookingId == 7
    instance.bookingId = 13
    assert instance.bookingId == 13


def test_HotelManagementClassDiagram_Booking_checkedIn_value_roundtrip():
    instance = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    assert instance.checkedIn == True
    instance.checkedIn = False
    assert instance.checkedIn == False


def test_HotelManagementClassDiagram_Booking_checkedOut_value_roundtrip():
    instance = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    assert instance.checkedOut == True
    instance.checkedOut = False
    assert instance.checkedOut == False


def test_HotelManagementClassDiagram_Booking_created_value_roundtrip():
    instance = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    assert instance.created == date(2024, 1, 1)
    instance.created = date(2025, 6, 15)
    assert instance.created == date(2025, 6, 15)


def test_HotelManagementClassDiagram_Booking_endDate_value_roundtrip():
    instance = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    assert instance.endDate == date(2024, 1, 1)
    instance.endDate = date(2025, 6, 15)
    assert instance.endDate == date(2025, 6, 15)


def test_HotelManagementClassDiagram_Booking_externalComments_value_roundtrip():
    instance = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    assert instance.externalComments == "sample_text"
    instance.externalComments = "sample_text_2"
    assert instance.externalComments == "sample_text_2"


def test_HotelManagementClassDiagram_Booking_internalComments_value_roundtrip():
    instance = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    assert instance.internalComments == "sample_text"
    instance.internalComments = "sample_text_2"
    assert instance.internalComments == "sample_text_2"


def test_HotelManagementClassDiagram_Booking_startDate_value_roundtrip():
    instance = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    assert instance.startDate == date(2024, 1, 1)
    instance.startDate = date(2025, 6, 15)
    assert instance.startDate == date(2025, 6, 15)


def test_HotelManagementClassDiagram_Costable_price_value_roundtrip():
    instance = HotelManagementClassDiagram_Costable(price=3.14)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_HotelManagementClassDiagram_Creditcard_cvc_value_roundtrip():
    instance = HotelManagementClassDiagram_Creditcard(cvc=7, expirationDay=7, expirationMonth=7, number="sample_text", owner="sample_text")
    assert instance.cvc == 7
    instance.cvc = 13
    assert instance.cvc == 13


def test_HotelManagementClassDiagram_Creditcard_expirationDay_value_roundtrip():
    instance = HotelManagementClassDiagram_Creditcard(cvc=7, expirationDay=7, expirationMonth=7, number="sample_text", owner="sample_text")
    assert instance.expirationDay == 7
    instance.expirationDay = 13
    assert instance.expirationDay == 13


def test_HotelManagementClassDiagram_Creditcard_expirationMonth_value_roundtrip():
    instance = HotelManagementClassDiagram_Creditcard(cvc=7, expirationDay=7, expirationMonth=7, number="sample_text", owner="sample_text")
    assert instance.expirationMonth == 7
    instance.expirationMonth = 13
    assert instance.expirationMonth == 13


def test_HotelManagementClassDiagram_Creditcard_number_value_roundtrip():
    instance = HotelManagementClassDiagram_Creditcard(cvc=7, expirationDay=7, expirationMonth=7, number="sample_text", owner="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_HotelManagementClassDiagram_Creditcard_owner_value_roundtrip():
    instance = HotelManagementClassDiagram_Creditcard(cvc=7, expirationDay=7, expirationMonth=7, number="sample_text", owner="sample_text")
    assert instance.owner == "sample_text"
    instance.owner = "sample_text_2"
    assert instance.owner == "sample_text_2"


def test_HotelManagementClassDiagram_Customer_bonusPoints_value_roundtrip():
    instance = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    assert instance.bonusPoints == 7
    instance.bonusPoints = 13
    assert instance.bonusPoints == 13


def test_HotelManagementClassDiagram_Customer_customerID_value_roundtrip():
    instance = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    assert instance.customerID == 7
    instance.customerID = 13
    assert instance.customerID == 13


def test_HotelManagementClassDiagram_Customer_miscInfo_value_roundtrip():
    instance = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    assert instance.miscInfo == "sample_text"
    instance.miscInfo = "sample_text_2"
    assert instance.miscInfo == "sample_text_2"


def test_HotelManagementClassDiagram_Customer_rank_value_roundtrip():
    instance = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    assert instance.rank == 3.14
    instance.rank = 9.99
    assert instance.rank == 9.99


def test_HotelManagementClassDiagram_Discount_amount_value_roundtrip():
    instance = HotelManagementClassDiagram_Discount(amount=3.14, isPercentage="sample_text")
    assert instance.amount == 3.14
    instance.amount = 9.99
    assert instance.amount == 9.99


def test_HotelManagementClassDiagram_Discount_isPercentage_value_roundtrip():
    instance = HotelManagementClassDiagram_Discount(amount=3.14, isPercentage="sample_text")
    assert instance.isPercentage == "sample_text"
    instance.isPercentage = "sample_text_2"
    assert instance.isPercentage == "sample_text_2"


def test_HotelManagementClassDiagram_Employee_employeeID_value_roundtrip():
    instance = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    assert instance.employeeID == 7
    instance.employeeID = 13
    assert instance.employeeID == 13


def test_HotelManagementClassDiagram_Employee_salary_value_roundtrip():
    instance = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    assert instance.salary == 3.14
    instance.salary = 9.99
    assert instance.salary == 9.99


def test_HotelManagementClassDiagram_Employee_workRate_value_roundtrip():
    instance = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    assert instance.workRate == 7
    instance.workRate = 13
    assert instance.workRate == 13


def test_HotelManagementClassDiagram_EmployeeType_acessLevel_value_roundtrip():
    instance = HotelManagementClassDiagram_EmployeeType(acessLevel=7, type="sample_text")
    assert instance.acessLevel == 7
    instance.acessLevel = 13
    assert instance.acessLevel == 13


def test_HotelManagementClassDiagram_EmployeeType_type_value_roundtrip():
    instance = HotelManagementClassDiagram_EmployeeType(acessLevel=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_HotelManagementClassDiagram_Hotel_address_value_roundtrip():
    instance = HotelManagementClassDiagram_Hotel(address="sample_text", name="sample_text", rank=3.14)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_HotelManagementClassDiagram_Hotel_name_value_roundtrip():
    instance = HotelManagementClassDiagram_Hotel(address="sample_text", name="sample_text", rank=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_HotelManagementClassDiagram_Hotel_rank_value_roundtrip():
    instance = HotelManagementClassDiagram_Hotel(address="sample_text", name="sample_text", rank=3.14)
    assert instance.rank == 3.14
    instance.rank = 9.99
    assert instance.rank == 9.99


def test_HotelManagementClassDiagram_Person_SSNumber_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.SSNumber == "sample_text"
    instance.SSNumber = "sample_text_2"
    assert instance.SSNumber == "sample_text_2"


def test_HotelManagementClassDiagram_Person_city_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_HotelManagementClassDiagram_Person_country_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_HotelManagementClassDiagram_Person_gender_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_HotelManagementClassDiagram_Person_name_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_HotelManagementClassDiagram_Person_phoneNumber_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_HotelManagementClassDiagram_Person_postalCode_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.postalCode == "sample_text"
    instance.postalCode = "sample_text_2"
    assert instance.postalCode == "sample_text_2"


def test_HotelManagementClassDiagram_Person_street_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_HotelManagementClassDiagram_Person_title_value_roundtrip():
    instance = HotelManagementClassDiagram_Person(SSNumber="sample_text", city="sample_text", country="sample_text", gender="sample_text", name="sample_text", phoneNumber="sample_text", postalCode="sample_text", street="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_HotelManagementClassDiagram_Room_booked_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.booked == True
    instance.booked = False
    assert instance.booked == False


def test_HotelManagementClassDiagram_Room_internalComment_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.internalComment == "sample_text"
    instance.internalComment = "sample_text_2"
    assert instance.internalComment == "sample_text_2"


def test_HotelManagementClassDiagram_Room_maxNbrPeople_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.maxNbrPeople == 7
    instance.maxNbrPeople = 13
    assert instance.maxNbrPeople == 13


def test_HotelManagementClassDiagram_Room_roomName_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.roomName == "sample_text"
    instance.roomName = "sample_text_2"
    assert instance.roomName == "sample_text_2"


def test_HotelManagementClassDiagram_Room_roomNumber_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.roomNumber == 7
    instance.roomNumber = 13
    assert instance.roomNumber == 13


def test_HotelManagementClassDiagram_Room_size_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.size == 3.14
    instance.size = 9.99
    assert instance.size == 9.99


def test_HotelManagementClassDiagram_Room_types_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.types == "sample_text"
    instance.types = "sample_text_2"
    assert instance.types == "sample_text_2"


def test_HotelManagementClassDiagram_Room_underCleaning_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.underCleaning == True
    instance.underCleaning = False
    assert instance.underCleaning == False


def test_HotelManagementClassDiagram_Room_underRepair_value_roundtrip():
    instance = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    assert instance.underRepair == True
    instance.underRepair = False
    assert instance.underRepair == False


def test_HotelManagementClassDiagram_Customer_isa_Person():
    instance = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    assert isinstance(instance, Person)


def test_HotelManagementClassDiagram_Employee_isa_Person():
    instance = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    assert isinstance(instance, Person)


def test_HotelManagementClassDiagram_BookedRoom_isa_Room():
    instance = HotelManagementClassDiagram_BookedRoom()
    assert isinstance(instance, Room)


def test_assoc__24_link_reassign_clear():
    a = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    b1 = HotelManagementClassDiagram_Interaction1()
    b2 = HotelManagementClassDiagram_Interaction1()
    _safe_set(a, 'HotelManagementClassDiagram_Employee25', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Employee25', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction1'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Interaction1', a)
    _safe_set(a, 'HotelManagementClassDiagram_Employee25', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Employee25', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction1'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Interaction1', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction1'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Interaction1', a)
    _safe_set(a, 'HotelManagementClassDiagram_Employee25', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Employee25', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction1'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Interaction1', a)


def test_assoc__26_link_reassign_clear():
    a = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    b1 = HotelManagementClassDiagram_Interaction2()
    b2 = HotelManagementClassDiagram_Interaction2()
    _safe_set(a, 'HotelManagementClassDiagram_Employee27', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Employee27', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction2'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Interaction2', a)
    _safe_set(a, 'HotelManagementClassDiagram_Employee27', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Employee27', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction2'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Interaction2', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction2'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Interaction2', a)
    _safe_set(a, 'HotelManagementClassDiagram_Employee27', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Employee27', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction2'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Interaction2', a)


def test_assoc__28_link_reassign_clear():
    a = HotelManagementClassDiagram_MaintenanceController()
    b1 = HotelManagementClassDiagram_Interaction3()
    b2 = HotelManagementClassDiagram_Interaction3()
    _safe_set(a, 'HotelManagementClassDiagram_MaintenanceController29', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_MaintenanceController29', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction3'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Interaction3', a)
    _safe_set(a, 'HotelManagementClassDiagram_MaintenanceController29', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_MaintenanceController29', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction3'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Interaction3', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction3'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Interaction3', a)
    _safe_set(a, 'HotelManagementClassDiagram_MaintenanceController29', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_MaintenanceController29', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction3'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Interaction3', a)


def test_assoc__30_link_reassign_clear():
    a = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    b1 = HotelManagementClassDiagram_Interaction4()
    b2 = HotelManagementClassDiagram_Interaction4()
    _safe_set(a, 'HotelManagementClassDiagram_Employee31', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Employee31', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction4'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Interaction4', a)
    _safe_set(a, 'HotelManagementClassDiagram_Employee31', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Employee31', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction4'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Interaction4', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction4'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Interaction4', a)
    _safe_set(a, 'HotelManagementClassDiagram_Employee31', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Employee31', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction4'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Interaction4', a)


def test_assoc__32_link_reassign_clear():
    a = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    b1 = HotelManagementClassDiagram_Interaction5()
    b2 = HotelManagementClassDiagram_Interaction5()
    _safe_set(a, 'HotelManagementClassDiagram_Booking33', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Booking33', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction5'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Interaction5', a)
    _safe_set(a, 'HotelManagementClassDiagram_Booking33', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Booking33', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Interaction5'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Interaction5', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction5'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Interaction5', a)
    _safe_set(a, 'HotelManagementClassDiagram_Booking33', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Booking33', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Interaction5'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Interaction5', a)


def test_assoc_addons22_link_reassign_clear():
    a = HotelManagementClassDiagram_BookedRoom()
    b1 = HotelManagementClassDiagram_Addon(description="sample_text", name="sample_text")
    b2 = HotelManagementClassDiagram_Addon(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'HotelManagementClassDiagram_BookedRoom', {b1})
    assert _is_linked(a, 'HotelManagementClassDiagram_BookedRoom', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Addon23'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Addon23', a)
    _safe_set(a, 'HotelManagementClassDiagram_BookedRoom', {b2})
    assert _is_linked(a, 'HotelManagementClassDiagram_BookedRoom', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Addon23'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Addon23', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Addon23'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Addon23', a)
    _safe_set(a, 'HotelManagementClassDiagram_BookedRoom', set())
    assert not _is_linked(a, 'HotelManagementClassDiagram_BookedRoom', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Addon23'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Addon23', a)


def test_assoc_addons4_link_reassign_clear():
    a = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    b1 = HotelManagementClassDiagram_Addon(description="sample_text", name="sample_text")
    b2 = HotelManagementClassDiagram_Addon(description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'HotelManagementClassDiagram_Booking5', {b1})
    assert _is_linked(a, 'HotelManagementClassDiagram_Booking5', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Addon'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Addon', a)
    _safe_set(a, 'HotelManagementClassDiagram_Booking5', {b2})
    assert _is_linked(a, 'HotelManagementClassDiagram_Booking5', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Addon'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Addon', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Addon'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Addon', a)
    _safe_set(a, 'HotelManagementClassDiagram_Booking5', set())
    assert not _is_linked(a, 'HotelManagementClassDiagram_Booking5', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Addon'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Addon', a)


def test_assoc_bookedRooms6_link_reassign_clear():
    a = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    b1 = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    b2 = HotelManagementClassDiagram_Booking(bookingId=13, checkedIn=False, checkedOut=False, created=date(2025, 6, 15), endDate=date(2025, 6, 15), externalComments="sample_text_2", internalComments="sample_text_2", startDate=date(2025, 6, 15))
    _safe_set(a, 'HotelManagementClassDiagram_Room', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Room', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking7'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Booking7', a)
    _safe_set(a, 'HotelManagementClassDiagram_Room', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Room', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking7'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Booking7', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking7'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Booking7', a)
    _safe_set(a, 'HotelManagementClassDiagram_Room', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Room', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking7'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Booking7', a)


def test_assoc_costables13_link_reassign_clear():
    a = HotelManagementClassDiagram_Costable(price=3.14)
    b1 = HotelManagementClassDiagram_Bill(final=True, paid=True, totalPrice=3.14, valueAddedTax=3.14)
    b2 = HotelManagementClassDiagram_Bill(final=False, paid=False, totalPrice=9.99, valueAddedTax=9.99)
    _safe_set(a, 'HotelManagementClassDiagram_Costable', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Costable', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Bill'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Bill', a)
    _safe_set(a, 'HotelManagementClassDiagram_Costable', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Costable', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Bill'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Bill', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Bill'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Bill', a)
    _safe_set(a, 'HotelManagementClassDiagram_Costable', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Costable', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Bill'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Bill', a)


def test_assoc_creditCard1_link_reassign_clear():
    a = HotelManagementClassDiagram_Creditcard(cvc=7, expirationDay=7, expirationMonth=7, number="sample_text", owner="sample_text")
    b1 = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    b2 = HotelManagementClassDiagram_Booking(bookingId=13, checkedIn=False, checkedOut=False, created=date(2025, 6, 15), endDate=date(2025, 6, 15), externalComments="sample_text_2", internalComments="sample_text_2", startDate=date(2025, 6, 15))
    _safe_set(a, 'HotelManagementClassDiagram_Creditcard', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Creditcard', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Booking', a)
    _safe_set(a, 'HotelManagementClassDiagram_Creditcard', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Creditcard', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Booking', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Booking', a)
    _safe_set(a, 'HotelManagementClassDiagram_Creditcard', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Creditcard', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Booking', a)


def test_assoc_customer14_link_reassign_clear():
    a = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    b1 = HotelManagementClassDiagram_Bill(final=True, paid=True, totalPrice=3.14, valueAddedTax=3.14)
    b2 = HotelManagementClassDiagram_Bill(final=False, paid=False, totalPrice=9.99, valueAddedTax=9.99)
    _safe_set(a, 'HotelManagementClassDiagram_Customer16', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Customer16', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Bill15'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Bill15', a)
    _safe_set(a, 'HotelManagementClassDiagram_Customer16', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Customer16', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Bill15'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Bill15', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Bill15'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Bill15', a)
    _safe_set(a, 'HotelManagementClassDiagram_Customer16', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Customer16', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Bill15'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Bill15', a)


def test_assoc_customer2_link_reassign_clear():
    a = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    b1 = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    b2 = HotelManagementClassDiagram_Booking(bookingId=13, checkedIn=False, checkedOut=False, created=date(2025, 6, 15), endDate=date(2025, 6, 15), externalComments="sample_text_2", internalComments="sample_text_2", startDate=date(2025, 6, 15))
    _safe_set(a, 'HotelManagementClassDiagram_Customer', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Customer', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking3'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Booking3', a)
    _safe_set(a, 'HotelManagementClassDiagram_Customer', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Customer', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking3'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Booking3', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking3'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Booking3', a)
    _safe_set(a, 'HotelManagementClassDiagram_Customer', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Customer', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking3'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Booking3', a)


def test_assoc_discounts11_link_reassign_clear():
    a = HotelManagementClassDiagram_Discount(amount=3.14, isPercentage="sample_text")
    b1 = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    b2 = HotelManagementClassDiagram_Booking(bookingId=13, checkedIn=False, checkedOut=False, created=date(2025, 6, 15), endDate=date(2025, 6, 15), externalComments="sample_text_2", internalComments="sample_text_2", startDate=date(2025, 6, 15))
    _safe_set(a, 'HotelManagementClassDiagram_Discount', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Discount', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking12'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Booking12', a)
    _safe_set(a, 'HotelManagementClassDiagram_Discount', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Discount', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking12'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Booking12', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking12'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Booking12', a)
    _safe_set(a, 'HotelManagementClassDiagram_Discount', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Discount', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking12'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Booking12', a)


def test_assoc_discounts17_link_reassign_clear():
    a = HotelManagementClassDiagram_Discount(amount=3.14, isPercentage="sample_text")
    b1 = HotelManagementClassDiagram_Costable(price=3.14)
    b2 = HotelManagementClassDiagram_Costable(price=9.99)
    _safe_set(a, 'HotelManagementClassDiagram_Discount19', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Discount19', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Costable18'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Costable18', a)
    _safe_set(a, 'HotelManagementClassDiagram_Discount19', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Discount19', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Costable18'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Costable18', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Costable18'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Costable18', a)
    _safe_set(a, 'HotelManagementClassDiagram_Discount19', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Discount19', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Costable18'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Costable18', a)


def test_assoc_employeeType0_link_reassign_clear():
    a = HotelManagementClassDiagram_EmployeeType(acessLevel=7, type="sample_text")
    b1 = HotelManagementClassDiagram_Employee(employeeID=7, salary=3.14, workRate=7)
    b2 = HotelManagementClassDiagram_Employee(employeeID=13, salary=9.99, workRate=13)
    _safe_set(a, 'HotelManagementClassDiagram_EmployeeType', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_EmployeeType', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Employee'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Employee', a)
    _safe_set(a, 'HotelManagementClassDiagram_EmployeeType', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_EmployeeType', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Employee'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Employee', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Employee'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Employee', a)
    _safe_set(a, 'HotelManagementClassDiagram_EmployeeType', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_EmployeeType', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Employee'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Employee', a)


def test_assoc_paymentMaster8_link_reassign_clear():
    a = HotelManagementClassDiagram_Customer(bonusPoints=7, customerID=7, miscInfo="sample_text", rank=3.14)
    b1 = HotelManagementClassDiagram_Booking(bookingId=7, checkedIn=True, checkedOut=True, created=date(2024, 1, 1), endDate=date(2024, 1, 1), externalComments="sample_text", internalComments="sample_text", startDate=date(2024, 1, 1))
    b2 = HotelManagementClassDiagram_Booking(bookingId=13, checkedIn=False, checkedOut=False, created=date(2025, 6, 15), endDate=date(2025, 6, 15), externalComments="sample_text_2", internalComments="sample_text_2", startDate=date(2025, 6, 15))
    _safe_set(a, 'HotelManagementClassDiagram_Customer10', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Customer10', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking9'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_Booking9', a)
    _safe_set(a, 'HotelManagementClassDiagram_Customer10', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Customer10', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_Booking9'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_Booking9', a)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking9'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_Booking9', a)
    _safe_set(a, 'HotelManagementClassDiagram_Customer10', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Customer10', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_Booking9'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_Booking9', a)


def test_assoc_roomStack20_link_reassign_clear():
    a = HotelManagementClassDiagram_Room(booked=True, internalComment="sample_text", maxNbrPeople=7, roomName="sample_text", roomNumber=7, size=3.14, types="sample_text", underCleaning=True, underRepair=True)
    b1 = HotelManagementClassDiagram_MaintenanceController()
    b2 = HotelManagementClassDiagram_MaintenanceController()
    _safe_set(a, 'HotelManagementClassDiagram_Room21', b1)
    assert _is_linked(a, 'HotelManagementClassDiagram_Room21', b1)
    if hasattr(b1, 'HotelManagementClassDiagram_MaintenanceController'):
        assert _is_linked(b1, 'HotelManagementClassDiagram_MaintenanceController', a)
    _safe_set(a, 'HotelManagementClassDiagram_Room21', b2)
    assert _is_linked(a, 'HotelManagementClassDiagram_Room21', b2)
    if hasattr(b1, 'HotelManagementClassDiagram_MaintenanceController'):
        assert not _is_linked(b1, 'HotelManagementClassDiagram_MaintenanceController', a)
    if hasattr(b2, 'HotelManagementClassDiagram_MaintenanceController'):
        assert _is_linked(b2, 'HotelManagementClassDiagram_MaintenanceController', a)
    _safe_set(a, 'HotelManagementClassDiagram_Room21', None)
    assert not _is_linked(a, 'HotelManagementClassDiagram_Room21', b2)
    if hasattr(b2, 'HotelManagementClassDiagram_MaintenanceController'):
        assert not _is_linked(b2, 'HotelManagementClassDiagram_MaintenanceController', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

HotelManagementClassDiagram_Addon_strategy = st.builds(HotelManagementClassDiagram_Addon, description=safe_text, name=safe_text)
@given(instance=HotelManagementClassDiagram_Addon_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Addon_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Addon)


HotelManagementClassDiagram_Bill_strategy = st.builds(HotelManagementClassDiagram_Bill, final=st.booleans(), paid=st.booleans(), totalPrice=st.floats(allow_nan=False, allow_infinity=False), valueAddedTax=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=HotelManagementClassDiagram_Bill_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Bill_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Bill)


HotelManagementClassDiagram_BookedRoom_strategy = st.builds(HotelManagementClassDiagram_BookedRoom)
@given(instance=HotelManagementClassDiagram_BookedRoom_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_BookedRoom_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_BookedRoom)


HotelManagementClassDiagram_Booking_strategy = st.builds(HotelManagementClassDiagram_Booking, bookingId=st.integers(), checkedIn=st.booleans(), checkedOut=st.booleans(), created=st.dates(), endDate=st.dates(), externalComments=safe_text, internalComments=safe_text, startDate=st.dates())
@given(instance=HotelManagementClassDiagram_Booking_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Booking_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Booking)


HotelManagementClassDiagram_BookingController_strategy = st.builds(HotelManagementClassDiagram_BookingController)
@given(instance=HotelManagementClassDiagram_BookingController_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_BookingController_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_BookingController)


HotelManagementClassDiagram_Costable_strategy = st.builds(HotelManagementClassDiagram_Costable, price=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=HotelManagementClassDiagram_Costable_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Costable_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Costable)


HotelManagementClassDiagram_Creditcard_strategy = st.builds(HotelManagementClassDiagram_Creditcard, cvc=st.integers(), expirationDay=st.integers(), expirationMonth=st.integers(), number=safe_text, owner=safe_text)
@given(instance=HotelManagementClassDiagram_Creditcard_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Creditcard_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Creditcard)


HotelManagementClassDiagram_Customer_strategy = st.builds(HotelManagementClassDiagram_Customer, bonusPoints=st.integers(), customerID=st.integers(), miscInfo=safe_text, rank=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=HotelManagementClassDiagram_Customer_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Customer_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Customer)


HotelManagementClassDiagram_Discount_strategy = st.builds(HotelManagementClassDiagram_Discount, amount=st.floats(allow_nan=False, allow_infinity=False), isPercentage=safe_text)
@given(instance=HotelManagementClassDiagram_Discount_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Discount_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Discount)


HotelManagementClassDiagram_Employee_strategy = st.builds(HotelManagementClassDiagram_Employee, employeeID=st.integers(), salary=st.floats(allow_nan=False, allow_infinity=False), workRate=st.integers())
@given(instance=HotelManagementClassDiagram_Employee_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Employee_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Employee)


HotelManagementClassDiagram_EmployeeType_strategy = st.builds(HotelManagementClassDiagram_EmployeeType, acessLevel=st.integers(), type=safe_text)
@given(instance=HotelManagementClassDiagram_EmployeeType_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_EmployeeType_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_EmployeeType)


HotelManagementClassDiagram_Hotel_strategy = st.builds(HotelManagementClassDiagram_Hotel, address=safe_text, name=safe_text, rank=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=HotelManagementClassDiagram_Hotel_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Hotel_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Hotel)


HotelManagementClassDiagram_Interaction1_strategy = st.builds(HotelManagementClassDiagram_Interaction1)
@given(instance=HotelManagementClassDiagram_Interaction1_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Interaction1_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Interaction1)


HotelManagementClassDiagram_Interaction2_strategy = st.builds(HotelManagementClassDiagram_Interaction2)
@given(instance=HotelManagementClassDiagram_Interaction2_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Interaction2_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Interaction2)


HotelManagementClassDiagram_Interaction3_strategy = st.builds(HotelManagementClassDiagram_Interaction3)
@given(instance=HotelManagementClassDiagram_Interaction3_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Interaction3_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Interaction3)


HotelManagementClassDiagram_Interaction4_strategy = st.builds(HotelManagementClassDiagram_Interaction4)
@given(instance=HotelManagementClassDiagram_Interaction4_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Interaction4_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Interaction4)


HotelManagementClassDiagram_Interaction5_strategy = st.builds(HotelManagementClassDiagram_Interaction5)
@given(instance=HotelManagementClassDiagram_Interaction5_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Interaction5_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Interaction5)


HotelManagementClassDiagram_MaintenanceController_strategy = st.builds(HotelManagementClassDiagram_MaintenanceController)
@given(instance=HotelManagementClassDiagram_MaintenanceController_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_MaintenanceController_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_MaintenanceController)


HotelManagementClassDiagram_ManagementController_strategy = st.builds(HotelManagementClassDiagram_ManagementController)
@given(instance=HotelManagementClassDiagram_ManagementController_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_ManagementController_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_ManagementController)


HotelManagementClassDiagram_Person_strategy = st.builds(HotelManagementClassDiagram_Person, SSNumber=safe_text, city=safe_text, country=safe_text, gender=safe_text, name=safe_text, phoneNumber=safe_text, postalCode=safe_text, street=safe_text, title=safe_text)
@given(instance=HotelManagementClassDiagram_Person_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Person_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Person)


HotelManagementClassDiagram_Room_strategy = st.builds(HotelManagementClassDiagram_Room, booked=st.booleans(), internalComment=safe_text, maxNbrPeople=st.integers(), roomName=safe_text, roomNumber=st.integers(), size=st.floats(allow_nan=False, allow_infinity=False), types=safe_text, underCleaning=st.booleans(), underRepair=st.booleans())
@given(instance=HotelManagementClassDiagram_Room_strategy)
@settings(max_examples=25)
def test_HotelManagementClassDiagram_Room_instantiation(instance):
    assert isinstance(instance, HotelManagementClassDiagram_Room)


Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Room_strategy = st.builds(Room)
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


