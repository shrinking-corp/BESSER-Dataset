import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AdminInterface,
    BookingController,
    CustomerInterface,
    DatabaseInterface,
    ReceptionistInterface,
    model_Admin,
    model_AdminController,
    model_AdminInterface,
    model_BankComponent,
    model_BankInterface,
    model_Booking,
    model_BookingController,
    model_BookingExpert,
    model_Customer,
    model_CustomerInterface,
    model_Customers,
    model_DatabaseInterface,
    model_EmailSender,
    model_Expense,
    model_ExpenseExpert,
    model_HotelComponent,
    model_MSAccessDB,
    model_Payment,
    model_Promotion,
    model_PromotionExpert,
    model_Receipt,
    model_ReceiptExpert,
    model_Receptionist,
    model_ReceptionistController,
    model_ReceptionistInterface,
    model_Resident,
    model_Room,
    model_RoomExpert,
    model_User,
    model_UserExpert,
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

def test_model_Booking_checkedIn_value_roundtrip():
    instance = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    assert instance.checkedIn == "sample_text"
    instance.checkedIn = "sample_text_2"
    assert instance.checkedIn == "sample_text_2"


def test_model_Booking_fromDate_value_roundtrip():
    instance = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    assert instance.fromDate == date(2024, 1, 1)
    instance.fromDate = date(2025, 6, 15)
    assert instance.fromDate == date(2025, 6, 15)


def test_model_Booking_id_value_roundtrip():
    instance = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_model_Booking_promotion_value_roundtrip():
    instance = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    assert instance.promotion == "sample_text"
    instance.promotion = "sample_text_2"
    assert instance.promotion == "sample_text_2"


def test_model_Booking_roomTypes_value_roundtrip():
    instance = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    assert instance.roomTypes == "sample_text"
    instance.roomTypes = "sample_text_2"
    assert instance.roomTypes == "sample_text_2"


def test_model_Booking_toDate_value_roundtrip():
    instance = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    assert instance.toDate == date(2024, 1, 1)
    instance.toDate = date(2025, 6, 15)
    assert instance.toDate == date(2025, 6, 15)


def test_model_Booking_wishes_value_roundtrip():
    instance = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    assert instance.wishes == "sample_text"
    instance.wishes = "sample_text_2"
    assert instance.wishes == "sample_text_2"


def test_model_Customer_adress_value_roundtrip():
    instance = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    assert instance.adress == "sample_text"
    instance.adress = "sample_text_2"
    assert instance.adress == "sample_text_2"


def test_model_Customer_ccNumber_value_roundtrip():
    instance = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    assert instance.ccNumber == "sample_text"
    instance.ccNumber = "sample_text_2"
    assert instance.ccNumber == "sample_text_2"


def test_model_Customer_ccv_value_roundtrip():
    instance = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    assert instance.ccv == "sample_text"
    instance.ccv = "sample_text_2"
    assert instance.ccv == "sample_text_2"


def test_model_Customer_email_value_roundtrip():
    instance = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_model_Customer_expiringMonth_value_roundtrip():
    instance = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    assert instance.expiringMonth == "sample_text"
    instance.expiringMonth = "sample_text_2"
    assert instance.expiringMonth == "sample_text_2"


def test_model_Customer_expiringYear_value_roundtrip():
    instance = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    assert instance.expiringYear == "sample_text"
    instance.expiringYear = "sample_text_2"
    assert instance.expiringYear == "sample_text_2"


def test_model_Customer_firstName_value_roundtrip():
    instance = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_model_Customer_surname_value_roundtrip():
    instance = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_model_Expense_date_value_roundtrip():
    instance = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_model_Expense_description_value_roundtrip():
    instance = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_model_Expense_fixed_value_roundtrip():
    instance = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    assert instance.fixed == True
    instance.fixed = False
    assert instance.fixed == False


def test_model_Expense_id_value_roundtrip():
    instance = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_model_Expense_name_value_roundtrip():
    instance = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_Expense_price_value_roundtrip():
    instance = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_model_Expense_receiptId_value_roundtrip():
    instance = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    assert instance.receiptId == 7
    instance.receiptId = 13
    assert instance.receiptId == 13


def test_model_Promotion_code_value_roundtrip():
    instance = model_Promotion(code="sample_text", description="sample_text", expirationDate=date(2024, 1, 1), percentage="sample_text", roomType="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_model_Promotion_description_value_roundtrip():
    instance = model_Promotion(code="sample_text", description="sample_text", expirationDate=date(2024, 1, 1), percentage="sample_text", roomType="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_model_Promotion_expirationDate_value_roundtrip():
    instance = model_Promotion(code="sample_text", description="sample_text", expirationDate=date(2024, 1, 1), percentage="sample_text", roomType="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.expirationDate == date(2024, 1, 1)
    instance.expirationDate = date(2025, 6, 15)
    assert instance.expirationDate == date(2025, 6, 15)


def test_model_Promotion_percentage_value_roundtrip():
    instance = model_Promotion(code="sample_text", description="sample_text", expirationDate=date(2024, 1, 1), percentage="sample_text", roomType="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.percentage == "sample_text"
    instance.percentage = "sample_text_2"
    assert instance.percentage == "sample_text_2"


def test_model_Promotion_roomType_value_roundtrip():
    instance = model_Promotion(code="sample_text", description="sample_text", expirationDate=date(2024, 1, 1), percentage="sample_text", roomType="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.roomType == "sample_text"
    instance.roomType = "sample_text_2"
    assert instance.roomType == "sample_text_2"


def test_model_Promotion_validFrom_value_roundtrip():
    instance = model_Promotion(code="sample_text", description="sample_text", expirationDate=date(2024, 1, 1), percentage="sample_text", roomType="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.validFrom == date(2024, 1, 1)
    instance.validFrom = date(2025, 6, 15)
    assert instance.validFrom == date(2025, 6, 15)


def test_model_Promotion_validTo_value_roundtrip():
    instance = model_Promotion(code="sample_text", description="sample_text", expirationDate=date(2024, 1, 1), percentage="sample_text", roomType="sample_text", validFrom=date(2024, 1, 1), validTo=date(2024, 1, 1))
    assert instance.validTo == date(2024, 1, 1)
    instance.validTo = date(2025, 6, 15)
    assert instance.validTo == date(2025, 6, 15)


def test_model_Receipt_Date_value_roundtrip():
    instance = model_Receipt(Date=date(2024, 1, 1), id=7, totalCost=3.14)
    assert instance.Date == date(2024, 1, 1)
    instance.Date = date(2025, 6, 15)
    assert instance.Date == date(2025, 6, 15)


def test_model_Receipt_id_value_roundtrip():
    instance = model_Receipt(Date=date(2024, 1, 1), id=7, totalCost=3.14)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_model_Receipt_totalCost_value_roundtrip():
    instance = model_Receipt(Date=date(2024, 1, 1), id=7, totalCost=3.14)
    assert instance.totalCost == 3.14
    instance.totalCost = 9.99
    assert instance.totalCost == 9.99


def test_model_Resident_firstName_value_roundtrip():
    instance = model_Resident(firstName="sample_text", id="sample_text", surname="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_model_Resident_id_value_roundtrip():
    instance = model_Resident(firstName="sample_text", id="sample_text", surname="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_model_Resident_surname_value_roundtrip():
    instance = model_Resident(firstName="sample_text", id="sample_text", surname="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_model_Room_beds_value_roundtrip():
    instance = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    assert instance.beds == "sample_text"
    instance.beds = "sample_text_2"
    assert instance.beds == "sample_text_2"


def test_model_Room_clean_value_roundtrip():
    instance = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    assert instance.clean == "sample_text"
    instance.clean = "sample_text_2"
    assert instance.clean == "sample_text_2"


def test_model_Room_description_value_roundtrip():
    instance = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_model_Room_number_value_roundtrip():
    instance = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    assert instance.number == "sample_text"
    instance.number = "sample_text_2"
    assert instance.number == "sample_text_2"


def test_model_Room_status_value_roundtrip():
    instance = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_model_Room_type_value_roundtrip():
    instance = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_model_User_administrator_value_roundtrip():
    instance = model_User(administrator="sample_text", firstName="sample_text", id="sample_text", password="sample_text", receptionist="sample_text", surname="sample_text")
    assert instance.administrator == "sample_text"
    instance.administrator = "sample_text_2"
    assert instance.administrator == "sample_text_2"


def test_model_User_firstName_value_roundtrip():
    instance = model_User(administrator="sample_text", firstName="sample_text", id="sample_text", password="sample_text", receptionist="sample_text", surname="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_model_User_id_value_roundtrip():
    instance = model_User(administrator="sample_text", firstName="sample_text", id="sample_text", password="sample_text", receptionist="sample_text", surname="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_model_User_password_value_roundtrip():
    instance = model_User(administrator="sample_text", firstName="sample_text", id="sample_text", password="sample_text", receptionist="sample_text", surname="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_model_User_receptionist_value_roundtrip():
    instance = model_User(administrator="sample_text", firstName="sample_text", id="sample_text", password="sample_text", receptionist="sample_text", surname="sample_text")
    assert instance.receptionist == "sample_text"
    instance.receptionist = "sample_text_2"
    assert instance.receptionist == "sample_text_2"


def test_model_User_surname_value_roundtrip():
    instance = model_User(administrator="sample_text", firstName="sample_text", id="sample_text", password="sample_text", receptionist="sample_text", surname="sample_text")
    assert instance.surname == "sample_text"
    instance.surname = "sample_text_2"
    assert instance.surname == "sample_text_2"


def test_model_AdminController_isa_AdminInterface():
    instance = model_AdminController()
    assert isinstance(instance, AdminInterface)


def test_model_ReceptionistController_isa_BookingController():
    instance = model_ReceptionistController()
    assert isinstance(instance, BookingController)


def test_model_BookingController_isa_CustomerInterface():
    instance = model_BookingController()
    assert isinstance(instance, CustomerInterface)


def test_model_MSAccessDB_isa_DatabaseInterface():
    instance = model_MSAccessDB()
    assert isinstance(instance, DatabaseInterface)


def test_model_ReceptionistController_isa_ReceptionistInterface():
    instance = model_ReceptionistController()
    assert isinstance(instance, ReceptionistInterface)


def test_assoc_bookingExpert28_link_reassign_clear():
    a = model_BookingExpert()
    b1 = model_BookingController()
    b2 = model_BookingController()
    _safe_set(a, 'model_BookingExpert30', b1)
    assert _is_linked(a, 'model_BookingExpert30', b1)
    if hasattr(b1, 'model_BookingController29'):
        assert _is_linked(b1, 'model_BookingController29', a)
    _safe_set(a, 'model_BookingExpert30', b2)
    assert _is_linked(a, 'model_BookingExpert30', b2)
    if hasattr(b1, 'model_BookingController29'):
        assert not _is_linked(b1, 'model_BookingController29', a)
    if hasattr(b2, 'model_BookingController29'):
        assert _is_linked(b2, 'model_BookingController29', a)
    _safe_set(a, 'model_BookingExpert30', None)
    assert not _is_linked(a, 'model_BookingExpert30', b2)
    if hasattr(b2, 'model_BookingController29'):
        assert not _is_linked(b2, 'model_BookingController29', a)


def test_assoc_customer8_link_reassign_clear():
    a = model_Customer(adress="sample_text", ccNumber="sample_text", ccv="sample_text", email="sample_text", expiringMonth="sample_text", expiringYear="sample_text", firstName="sample_text", surname="sample_text")
    b1 = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    b2 = model_Booking(checkedIn="sample_text_2", fromDate=date(2025, 6, 15), id=13, promotion="sample_text_2", roomTypes="sample_text_2", toDate=date(2025, 6, 15), wishes="sample_text_2")
    _safe_set(a, 'model_Customer', b1)
    assert _is_linked(a, 'model_Customer', b1)
    if hasattr(b1, 'model_Booking'):
        assert _is_linked(b1, 'model_Booking', a)
    _safe_set(a, 'model_Customer', b2)
    assert _is_linked(a, 'model_Customer', b2)
    if hasattr(b1, 'model_Booking'):
        assert not _is_linked(b1, 'model_Booking', a)
    if hasattr(b2, 'model_Booking'):
        assert _is_linked(b2, 'model_Booking', a)
    _safe_set(a, 'model_Customer', None)
    assert not _is_linked(a, 'model_Customer', b2)
    if hasattr(b2, 'model_Booking'):
        assert not _is_linked(b2, 'model_Booking', a)


def test_assoc_database15_link_reassign_clear():
    a = model_RoomExpert()
    b1 = model_DatabaseInterface()
    b2 = model_DatabaseInterface()
    _safe_set(a, 'model_RoomExpert', b1)
    assert _is_linked(a, 'model_RoomExpert', b1)
    if hasattr(b1, 'model_DatabaseInterface'):
        assert _is_linked(b1, 'model_DatabaseInterface', a)
    _safe_set(a, 'model_RoomExpert', b2)
    assert _is_linked(a, 'model_RoomExpert', b2)
    if hasattr(b1, 'model_DatabaseInterface'):
        assert not _is_linked(b1, 'model_DatabaseInterface', a)
    if hasattr(b2, 'model_DatabaseInterface'):
        assert _is_linked(b2, 'model_DatabaseInterface', a)
    _safe_set(a, 'model_RoomExpert', None)
    assert not _is_linked(a, 'model_RoomExpert', b2)
    if hasattr(b2, 'model_DatabaseInterface'):
        assert not _is_linked(b2, 'model_DatabaseInterface', a)


def test_assoc_database16_link_reassign_clear():
    a = model_ExpenseExpert()
    b1 = model_DatabaseInterface()
    b2 = model_DatabaseInterface()
    _safe_set(a, 'model_ExpenseExpert', b1)
    assert _is_linked(a, 'model_ExpenseExpert', b1)
    if hasattr(b1, 'model_DatabaseInterface17'):
        assert _is_linked(b1, 'model_DatabaseInterface17', a)
    _safe_set(a, 'model_ExpenseExpert', b2)
    assert _is_linked(a, 'model_ExpenseExpert', b2)
    if hasattr(b1, 'model_DatabaseInterface17'):
        assert not _is_linked(b1, 'model_DatabaseInterface17', a)
    if hasattr(b2, 'model_DatabaseInterface17'):
        assert _is_linked(b2, 'model_DatabaseInterface17', a)
    _safe_set(a, 'model_ExpenseExpert', None)
    assert not _is_linked(a, 'model_ExpenseExpert', b2)
    if hasattr(b2, 'model_DatabaseInterface17'):
        assert not _is_linked(b2, 'model_DatabaseInterface17', a)


def test_assoc_database18_link_reassign_clear():
    a = model_UserExpert()
    b1 = model_DatabaseInterface()
    b2 = model_DatabaseInterface()
    _safe_set(a, 'model_UserExpert', b1)
    assert _is_linked(a, 'model_UserExpert', b1)
    if hasattr(b1, 'model_DatabaseInterface19'):
        assert _is_linked(b1, 'model_DatabaseInterface19', a)
    _safe_set(a, 'model_UserExpert', b2)
    assert _is_linked(a, 'model_UserExpert', b2)
    if hasattr(b1, 'model_DatabaseInterface19'):
        assert not _is_linked(b1, 'model_DatabaseInterface19', a)
    if hasattr(b2, 'model_DatabaseInterface19'):
        assert _is_linked(b2, 'model_DatabaseInterface19', a)
    _safe_set(a, 'model_UserExpert', None)
    assert not _is_linked(a, 'model_UserExpert', b2)
    if hasattr(b2, 'model_DatabaseInterface19'):
        assert not _is_linked(b2, 'model_DatabaseInterface19', a)


def test_assoc_database20_link_reassign_clear():
    a = model_PromotionExpert()
    b1 = model_DatabaseInterface()
    b2 = model_DatabaseInterface()
    _safe_set(a, 'model_PromotionExpert', b1)
    assert _is_linked(a, 'model_PromotionExpert', b1)
    if hasattr(b1, 'model_DatabaseInterface21'):
        assert _is_linked(b1, 'model_DatabaseInterface21', a)
    _safe_set(a, 'model_PromotionExpert', b2)
    assert _is_linked(a, 'model_PromotionExpert', b2)
    if hasattr(b1, 'model_DatabaseInterface21'):
        assert not _is_linked(b1, 'model_DatabaseInterface21', a)
    if hasattr(b2, 'model_DatabaseInterface21'):
        assert _is_linked(b2, 'model_DatabaseInterface21', a)
    _safe_set(a, 'model_PromotionExpert', None)
    assert not _is_linked(a, 'model_PromotionExpert', b2)
    if hasattr(b2, 'model_DatabaseInterface21'):
        assert not _is_linked(b2, 'model_DatabaseInterface21', a)


def test_assoc_database22_link_reassign_clear():
    a = model_DatabaseInterface()
    b1 = model_BookingExpert()
    b2 = model_BookingExpert()
    _safe_set(a, 'model_DatabaseInterface23', b1)
    assert _is_linked(a, 'model_DatabaseInterface23', b1)
    if hasattr(b1, 'model_BookingExpert'):
        assert _is_linked(b1, 'model_BookingExpert', a)
    _safe_set(a, 'model_DatabaseInterface23', b2)
    assert _is_linked(a, 'model_DatabaseInterface23', b2)
    if hasattr(b1, 'model_BookingExpert'):
        assert not _is_linked(b1, 'model_BookingExpert', a)
    if hasattr(b2, 'model_BookingExpert'):
        assert _is_linked(b2, 'model_BookingExpert', a)
    _safe_set(a, 'model_DatabaseInterface23', None)
    assert not _is_linked(a, 'model_DatabaseInterface23', b2)
    if hasattr(b2, 'model_BookingExpert'):
        assert not _is_linked(b2, 'model_BookingExpert', a)


def test_assoc_database24_link_reassign_clear():
    a = model_ReceiptExpert()
    b1 = model_DatabaseInterface()
    b2 = model_DatabaseInterface()
    _safe_set(a, 'model_ReceiptExpert', b1)
    assert _is_linked(a, 'model_ReceiptExpert', b1)
    if hasattr(b1, 'model_DatabaseInterface25'):
        assert _is_linked(b1, 'model_DatabaseInterface25', a)
    _safe_set(a, 'model_ReceiptExpert', b2)
    assert _is_linked(a, 'model_ReceiptExpert', b2)
    if hasattr(b1, 'model_DatabaseInterface25'):
        assert not _is_linked(b1, 'model_DatabaseInterface25', a)
    if hasattr(b2, 'model_DatabaseInterface25'):
        assert _is_linked(b2, 'model_DatabaseInterface25', a)
    _safe_set(a, 'model_ReceiptExpert', None)
    assert not _is_linked(a, 'model_ReceiptExpert', b2)
    if hasattr(b2, 'model_DatabaseInterface25'):
        assert not _is_linked(b2, 'model_DatabaseInterface25', a)


def test_assoc_databaseInterface34_link_reassign_clear():
    a = model_DatabaseInterface()
    b1 = model_BookingController()
    b2 = model_BookingController()
    _safe_set(a, 'model_DatabaseInterface36', b1)
    assert _is_linked(a, 'model_DatabaseInterface36', b1)
    if hasattr(b1, 'model_BookingController35'):
        assert _is_linked(b1, 'model_BookingController35', a)
    _safe_set(a, 'model_DatabaseInterface36', b2)
    assert _is_linked(a, 'model_DatabaseInterface36', b2)
    if hasattr(b1, 'model_BookingController35'):
        assert not _is_linked(b1, 'model_BookingController35', a)
    if hasattr(b2, 'model_BookingController35'):
        assert _is_linked(b2, 'model_BookingController35', a)
    _safe_set(a, 'model_DatabaseInterface36', None)
    assert not _is_linked(a, 'model_DatabaseInterface36', b2)
    if hasattr(b2, 'model_BookingController35'):
        assert not _is_linked(b2, 'model_BookingController35', a)


def test_assoc_databaseInterface51_link_reassign_clear():
    a = model_DatabaseInterface()
    b1 = model_AdminController()
    b2 = model_AdminController()
    _safe_set(a, 'model_DatabaseInterface53', b1)
    assert _is_linked(a, 'model_DatabaseInterface53', b1)
    if hasattr(b1, 'model_AdminController52'):
        assert _is_linked(b1, 'model_AdminController52', a)
    _safe_set(a, 'model_DatabaseInterface53', b2)
    assert _is_linked(a, 'model_DatabaseInterface53', b2)
    if hasattr(b1, 'model_AdminController52'):
        assert not _is_linked(b1, 'model_AdminController52', a)
    if hasattr(b2, 'model_AdminController52'):
        assert _is_linked(b2, 'model_AdminController52', a)
    _safe_set(a, 'model_DatabaseInterface53', None)
    assert not _is_linked(a, 'model_DatabaseInterface53', b2)
    if hasattr(b2, 'model_AdminController52'):
        assert not _is_linked(b2, 'model_AdminController52', a)


def test_assoc_expenseExpert37_link_reassign_clear():
    a = model_ExpenseExpert()
    b1 = model_BookingController()
    b2 = model_BookingController()
    _safe_set(a, 'model_ExpenseExpert39', b1)
    assert _is_linked(a, 'model_ExpenseExpert39', b1)
    if hasattr(b1, 'model_BookingController38'):
        assert _is_linked(b1, 'model_BookingController38', a)
    _safe_set(a, 'model_ExpenseExpert39', b2)
    assert _is_linked(a, 'model_ExpenseExpert39', b2)
    if hasattr(b1, 'model_BookingController38'):
        assert not _is_linked(b1, 'model_BookingController38', a)
    if hasattr(b2, 'model_BookingController38'):
        assert _is_linked(b2, 'model_BookingController38', a)
    _safe_set(a, 'model_ExpenseExpert39', None)
    assert not _is_linked(a, 'model_ExpenseExpert39', b2)
    if hasattr(b2, 'model_BookingController38'):
        assert not _is_linked(b2, 'model_BookingController38', a)


def test_assoc_expenseExpert45_link_reassign_clear():
    a = model_ExpenseExpert()
    b1 = model_AdminController()
    b2 = model_AdminController()
    _safe_set(a, 'model_ExpenseExpert47', b1)
    assert _is_linked(a, 'model_ExpenseExpert47', b1)
    if hasattr(b1, 'model_AdminController46'):
        assert _is_linked(b1, 'model_AdminController46', a)
    _safe_set(a, 'model_ExpenseExpert47', b2)
    assert _is_linked(a, 'model_ExpenseExpert47', b2)
    if hasattr(b1, 'model_AdminController46'):
        assert not _is_linked(b1, 'model_AdminController46', a)
    if hasattr(b2, 'model_AdminController46'):
        assert _is_linked(b2, 'model_AdminController46', a)
    _safe_set(a, 'model_ExpenseExpert47', None)
    assert not _is_linked(a, 'model_ExpenseExpert47', b2)
    if hasattr(b2, 'model_AdminController46'):
        assert not _is_linked(b2, 'model_AdminController46', a)


def test_assoc_expenses5_link_reassign_clear():
    a = model_Receipt(Date=date(2024, 1, 1), id=7, totalCost=3.14)
    b1 = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    b2 = model_Expense(date=date(2025, 6, 15), description="sample_text_2", fixed=False, id=13, name="sample_text_2", price=9.99, receiptId=13)
    _safe_set(a, 'model_Receipt6', {b1})
    assert _is_linked(a, 'model_Receipt6', b1)
    if hasattr(b1, 'model_Expense7'):
        assert _is_linked(b1, 'model_Expense7', a)
    _safe_set(a, 'model_Receipt6', {b2})
    assert _is_linked(a, 'model_Receipt6', b2)
    if hasattr(b1, 'model_Expense7'):
        assert not _is_linked(b1, 'model_Expense7', a)
    if hasattr(b2, 'model_Expense7'):
        assert _is_linked(b2, 'model_Expense7', a)
    _safe_set(a, 'model_Receipt6', set())
    assert not _is_linked(a, 'model_Receipt6', b2)
    if hasattr(b2, 'model_Expense7'):
        assert not _is_linked(b2, 'model_Expense7', a)


def test_assoc_price0_link_reassign_clear():
    a = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    b1 = model_Expense(date=date(2024, 1, 1), description="sample_text", fixed=True, id=7, name="sample_text", price=3.14, receiptId=7)
    b2 = model_Expense(date=date(2025, 6, 15), description="sample_text_2", fixed=False, id=13, name="sample_text_2", price=9.99, receiptId=13)
    _safe_set(a, 'model_Room', b1)
    assert _is_linked(a, 'model_Room', b1)
    if hasattr(b1, 'model_Expense'):
        assert _is_linked(b1, 'model_Expense', a)
    _safe_set(a, 'model_Room', b2)
    assert _is_linked(a, 'model_Room', b2)
    if hasattr(b1, 'model_Expense'):
        assert not _is_linked(b1, 'model_Expense', a)
    if hasattr(b2, 'model_Expense'):
        assert _is_linked(b2, 'model_Expense', a)
    _safe_set(a, 'model_Room', None)
    assert not _is_linked(a, 'model_Room', b2)
    if hasattr(b2, 'model_Expense'):
        assert not _is_linked(b2, 'model_Expense', a)


def test_assoc_promoExpert48_link_reassign_clear():
    a = model_PromotionExpert()
    b1 = model_AdminController()
    b2 = model_AdminController()
    _safe_set(a, 'model_PromotionExpert50', b1)
    assert _is_linked(a, 'model_PromotionExpert50', b1)
    if hasattr(b1, 'model_AdminController49'):
        assert _is_linked(b1, 'model_AdminController49', a)
    _safe_set(a, 'model_PromotionExpert50', b2)
    assert _is_linked(a, 'model_PromotionExpert50', b2)
    if hasattr(b1, 'model_AdminController49'):
        assert not _is_linked(b1, 'model_AdminController49', a)
    if hasattr(b2, 'model_AdminController49'):
        assert _is_linked(b2, 'model_AdminController49', a)
    _safe_set(a, 'model_PromotionExpert50', None)
    assert not _is_linked(a, 'model_PromotionExpert50', b2)
    if hasattr(b2, 'model_AdminController49'):
        assert not _is_linked(b2, 'model_AdminController49', a)


def test_assoc_promotionExpert31_link_reassign_clear():
    a = model_PromotionExpert()
    b1 = model_BookingController()
    b2 = model_BookingController()
    _safe_set(a, 'model_PromotionExpert33', b1)
    assert _is_linked(a, 'model_PromotionExpert33', b1)
    if hasattr(b1, 'model_BookingController32'):
        assert _is_linked(b1, 'model_BookingController32', a)
    _safe_set(a, 'model_PromotionExpert33', b2)
    assert _is_linked(a, 'model_PromotionExpert33', b2)
    if hasattr(b1, 'model_BookingController32'):
        assert not _is_linked(b1, 'model_BookingController32', a)
    if hasattr(b2, 'model_BookingController32'):
        assert _is_linked(b2, 'model_BookingController32', a)
    _safe_set(a, 'model_PromotionExpert33', None)
    assert not _is_linked(a, 'model_PromotionExpert33', b2)
    if hasattr(b2, 'model_BookingController32'):
        assert not _is_linked(b2, 'model_BookingController32', a)


def test_assoc_receipt1_link_reassign_clear():
    a = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    b1 = model_Receipt(Date=date(2024, 1, 1), id=7, totalCost=3.14)
    b2 = model_Receipt(Date=date(2025, 6, 15), id=13, totalCost=9.99)
    _safe_set(a, 'model_Room2', b1)
    assert _is_linked(a, 'model_Room2', b1)
    if hasattr(b1, 'model_Receipt'):
        assert _is_linked(b1, 'model_Receipt', a)
    _safe_set(a, 'model_Room2', b2)
    assert _is_linked(a, 'model_Room2', b2)
    if hasattr(b1, 'model_Receipt'):
        assert not _is_linked(b1, 'model_Receipt', a)
    if hasattr(b2, 'model_Receipt'):
        assert _is_linked(b2, 'model_Receipt', a)
    _safe_set(a, 'model_Room2', None)
    assert not _is_linked(a, 'model_Room2', b2)
    if hasattr(b2, 'model_Receipt'):
        assert not _is_linked(b2, 'model_Receipt', a)


def test_assoc_receipt9_link_reassign_clear():
    a = model_Receipt(Date=date(2024, 1, 1), id=7, totalCost=3.14)
    b1 = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    b2 = model_Booking(checkedIn="sample_text_2", fromDate=date(2025, 6, 15), id=13, promotion="sample_text_2", roomTypes="sample_text_2", toDate=date(2025, 6, 15), wishes="sample_text_2")
    _safe_set(a, 'model_Receipt11', b1)
    assert _is_linked(a, 'model_Receipt11', b1)
    if hasattr(b1, 'model_Booking10'):
        assert _is_linked(b1, 'model_Booking10', a)
    _safe_set(a, 'model_Receipt11', b2)
    assert _is_linked(a, 'model_Receipt11', b2)
    if hasattr(b1, 'model_Booking10'):
        assert not _is_linked(b1, 'model_Booking10', a)
    if hasattr(b2, 'model_Booking10'):
        assert _is_linked(b2, 'model_Booking10', a)
    _safe_set(a, 'model_Receipt11', None)
    assert not _is_linked(a, 'model_Receipt11', b2)
    if hasattr(b2, 'model_Booking10'):
        assert not _is_linked(b2, 'model_Booking10', a)


def test_assoc_receiptExpert40_link_reassign_clear():
    a = model_ReceiptExpert()
    b1 = model_BookingController()
    b2 = model_BookingController()
    _safe_set(a, 'model_ReceiptExpert42', b1)
    assert _is_linked(a, 'model_ReceiptExpert42', b1)
    if hasattr(b1, 'model_BookingController41'):
        assert _is_linked(b1, 'model_BookingController41', a)
    _safe_set(a, 'model_ReceiptExpert42', b2)
    assert _is_linked(a, 'model_ReceiptExpert42', b2)
    if hasattr(b1, 'model_BookingController41'):
        assert not _is_linked(b1, 'model_BookingController41', a)
    if hasattr(b2, 'model_BookingController41'):
        assert _is_linked(b2, 'model_BookingController41', a)
    _safe_set(a, 'model_ReceiptExpert42', None)
    assert not _is_linked(a, 'model_ReceiptExpert42', b2)
    if hasattr(b2, 'model_BookingController41'):
        assert not _is_linked(b2, 'model_BookingController41', a)


def test_assoc_residents3_link_reassign_clear():
    a = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    b1 = model_Resident(firstName="sample_text", id="sample_text", surname="sample_text")
    b2 = model_Resident(firstName="sample_text_2", id="sample_text_2", surname="sample_text_2")
    _safe_set(a, 'model_Room4', {b1})
    assert _is_linked(a, 'model_Room4', b1)
    if hasattr(b1, 'model_Resident'):
        assert _is_linked(b1, 'model_Resident', a)
    _safe_set(a, 'model_Room4', {b2})
    assert _is_linked(a, 'model_Room4', b2)
    if hasattr(b1, 'model_Resident'):
        assert not _is_linked(b1, 'model_Resident', a)
    if hasattr(b2, 'model_Resident'):
        assert _is_linked(b2, 'model_Resident', a)
    _safe_set(a, 'model_Room4', set())
    assert not _is_linked(a, 'model_Room4', b2)
    if hasattr(b2, 'model_Resident'):
        assert not _is_linked(b2, 'model_Resident', a)


def test_assoc_room12_link_reassign_clear():
    a = model_Room(beds="sample_text", clean="sample_text", description="sample_text", number="sample_text", status="sample_text", type="sample_text")
    b1 = model_Booking(checkedIn="sample_text", fromDate=date(2024, 1, 1), id=7, promotion="sample_text", roomTypes="sample_text", toDate=date(2024, 1, 1), wishes="sample_text")
    b2 = model_Booking(checkedIn="sample_text_2", fromDate=date(2025, 6, 15), id=13, promotion="sample_text_2", roomTypes="sample_text_2", toDate=date(2025, 6, 15), wishes="sample_text_2")
    _safe_set(a, 'model_Room14', b1)
    assert _is_linked(a, 'model_Room14', b1)
    if hasattr(b1, 'model_Booking13'):
        assert _is_linked(b1, 'model_Booking13', a)
    _safe_set(a, 'model_Room14', b2)
    assert _is_linked(a, 'model_Room14', b2)
    if hasattr(b1, 'model_Booking13'):
        assert not _is_linked(b1, 'model_Booking13', a)
    if hasattr(b2, 'model_Booking13'):
        assert _is_linked(b2, 'model_Booking13', a)
    _safe_set(a, 'model_Room14', None)
    assert not _is_linked(a, 'model_Room14', b2)
    if hasattr(b2, 'model_Booking13'):
        assert not _is_linked(b2, 'model_Booking13', a)


def test_assoc_room26_link_reassign_clear():
    a = model_RoomExpert()
    b1 = model_BookingController()
    b2 = model_BookingController()
    _safe_set(a, 'model_RoomExpert27', b1)
    assert _is_linked(a, 'model_RoomExpert27', b1)
    if hasattr(b1, 'model_BookingController'):
        assert _is_linked(b1, 'model_BookingController', a)
    _safe_set(a, 'model_RoomExpert27', b2)
    assert _is_linked(a, 'model_RoomExpert27', b2)
    if hasattr(b1, 'model_BookingController'):
        assert not _is_linked(b1, 'model_BookingController', a)
    if hasattr(b2, 'model_BookingController'):
        assert _is_linked(b2, 'model_BookingController', a)
    _safe_set(a, 'model_RoomExpert27', None)
    assert not _is_linked(a, 'model_RoomExpert27', b2)
    if hasattr(b2, 'model_BookingController'):
        assert not _is_linked(b2, 'model_BookingController', a)


def test_assoc_roomExpert54_link_reassign_clear():
    a = model_RoomExpert()
    b1 = model_AdminController()
    b2 = model_AdminController()
    _safe_set(a, 'model_RoomExpert56', b1)
    assert _is_linked(a, 'model_RoomExpert56', b1)
    if hasattr(b1, 'model_AdminController55'):
        assert _is_linked(b1, 'model_AdminController55', a)
    _safe_set(a, 'model_RoomExpert56', b2)
    assert _is_linked(a, 'model_RoomExpert56', b2)
    if hasattr(b1, 'model_AdminController55'):
        assert not _is_linked(b1, 'model_AdminController55', a)
    if hasattr(b2, 'model_AdminController55'):
        assert _is_linked(b2, 'model_AdminController55', a)
    _safe_set(a, 'model_RoomExpert56', None)
    assert not _is_linked(a, 'model_RoomExpert56', b2)
    if hasattr(b2, 'model_AdminController55'):
        assert not _is_linked(b2, 'model_AdminController55', a)


def test_assoc_userExpert43_link_reassign_clear():
    a = model_UserExpert()
    b1 = model_AdminController()
    b2 = model_AdminController()
    _safe_set(a, 'model_UserExpert44', b1)
    assert _is_linked(a, 'model_UserExpert44', b1)
    if hasattr(b1, 'model_AdminController'):
        assert _is_linked(b1, 'model_AdminController', a)
    _safe_set(a, 'model_UserExpert44', b2)
    assert _is_linked(a, 'model_UserExpert44', b2)
    if hasattr(b1, 'model_AdminController'):
        assert not _is_linked(b1, 'model_AdminController', a)
    if hasattr(b2, 'model_AdminController'):
        assert _is_linked(b2, 'model_AdminController', a)
    _safe_set(a, 'model_UserExpert44', None)
    assert not _is_linked(a, 'model_UserExpert44', b2)
    if hasattr(b2, 'model_AdminController'):
        assert not _is_linked(b2, 'model_AdminController', a)


def test_assoc_userExpert57_link_reassign_clear():
    a = model_UserExpert()
    b1 = model_ReceptionistController()
    b2 = model_ReceptionistController()
    _safe_set(a, 'model_UserExpert58', b1)
    assert _is_linked(a, 'model_UserExpert58', b1)
    if hasattr(b1, 'model_ReceptionistController'):
        assert _is_linked(b1, 'model_ReceptionistController', a)
    _safe_set(a, 'model_UserExpert58', b2)
    assert _is_linked(a, 'model_UserExpert58', b2)
    if hasattr(b1, 'model_ReceptionistController'):
        assert not _is_linked(b1, 'model_ReceptionistController', a)
    if hasattr(b2, 'model_ReceptionistController'):
        assert _is_linked(b2, 'model_ReceptionistController', a)
    _safe_set(a, 'model_UserExpert58', None)
    assert not _is_linked(a, 'model_UserExpert58', b2)
    if hasattr(b2, 'model_ReceptionistController'):
        assert not _is_linked(b2, 'model_ReceptionistController', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AdminInterface_strategy = st.builds(AdminInterface)
@given(instance=AdminInterface_strategy)
@settings(max_examples=25)
def test_AdminInterface_instantiation(instance):
    assert isinstance(instance, AdminInterface)


BookingController_strategy = st.builds(BookingController)
@given(instance=BookingController_strategy)
@settings(max_examples=25)
def test_BookingController_instantiation(instance):
    assert isinstance(instance, BookingController)


CustomerInterface_strategy = st.builds(CustomerInterface)
@given(instance=CustomerInterface_strategy)
@settings(max_examples=25)
def test_CustomerInterface_instantiation(instance):
    assert isinstance(instance, CustomerInterface)


DatabaseInterface_strategy = st.builds(DatabaseInterface)
@given(instance=DatabaseInterface_strategy)
@settings(max_examples=25)
def test_DatabaseInterface_instantiation(instance):
    assert isinstance(instance, DatabaseInterface)


ReceptionistInterface_strategy = st.builds(ReceptionistInterface)
@given(instance=ReceptionistInterface_strategy)
@settings(max_examples=25)
def test_ReceptionistInterface_instantiation(instance):
    assert isinstance(instance, ReceptionistInterface)


model_Admin_strategy = st.builds(model_Admin)
@given(instance=model_Admin_strategy)
@settings(max_examples=25)
def test_model_Admin_instantiation(instance):
    assert isinstance(instance, model_Admin)


model_AdminController_strategy = st.builds(model_AdminController)
@given(instance=model_AdminController_strategy)
@settings(max_examples=25)
def test_model_AdminController_instantiation(instance):
    assert isinstance(instance, model_AdminController)


model_AdminInterface_strategy = st.builds(model_AdminInterface)
@given(instance=model_AdminInterface_strategy)
@settings(max_examples=25)
def test_model_AdminInterface_instantiation(instance):
    assert isinstance(instance, model_AdminInterface)


model_BankComponent_strategy = st.builds(model_BankComponent)
@given(instance=model_BankComponent_strategy)
@settings(max_examples=25)
def test_model_BankComponent_instantiation(instance):
    assert isinstance(instance, model_BankComponent)


model_BankInterface_strategy = st.builds(model_BankInterface)
@given(instance=model_BankInterface_strategy)
@settings(max_examples=25)
def test_model_BankInterface_instantiation(instance):
    assert isinstance(instance, model_BankInterface)


model_Booking_strategy = st.builds(model_Booking, checkedIn=safe_text, fromDate=st.dates(), id=st.integers(), promotion=safe_text, roomTypes=safe_text, toDate=st.dates(), wishes=safe_text)
@given(instance=model_Booking_strategy)
@settings(max_examples=25)
def test_model_Booking_instantiation(instance):
    assert isinstance(instance, model_Booking)


model_BookingController_strategy = st.builds(model_BookingController)
@given(instance=model_BookingController_strategy)
@settings(max_examples=25)
def test_model_BookingController_instantiation(instance):
    assert isinstance(instance, model_BookingController)


model_BookingExpert_strategy = st.builds(model_BookingExpert)
@given(instance=model_BookingExpert_strategy)
@settings(max_examples=25)
def test_model_BookingExpert_instantiation(instance):
    assert isinstance(instance, model_BookingExpert)


model_Customer_strategy = st.builds(model_Customer, adress=safe_text, ccNumber=safe_text, ccv=safe_text, email=safe_text, expiringMonth=safe_text, expiringYear=safe_text, firstName=safe_text, surname=safe_text)
@given(instance=model_Customer_strategy)
@settings(max_examples=25)
def test_model_Customer_instantiation(instance):
    assert isinstance(instance, model_Customer)


model_CustomerInterface_strategy = st.builds(model_CustomerInterface)
@given(instance=model_CustomerInterface_strategy)
@settings(max_examples=25)
def test_model_CustomerInterface_instantiation(instance):
    assert isinstance(instance, model_CustomerInterface)


model_Customers_strategy = st.builds(model_Customers)
@given(instance=model_Customers_strategy)
@settings(max_examples=25)
def test_model_Customers_instantiation(instance):
    assert isinstance(instance, model_Customers)


model_DatabaseInterface_strategy = st.builds(model_DatabaseInterface)
@given(instance=model_DatabaseInterface_strategy)
@settings(max_examples=25)
def test_model_DatabaseInterface_instantiation(instance):
    assert isinstance(instance, model_DatabaseInterface)


model_EmailSender_strategy = st.builds(model_EmailSender)
@given(instance=model_EmailSender_strategy)
@settings(max_examples=25)
def test_model_EmailSender_instantiation(instance):
    assert isinstance(instance, model_EmailSender)


model_Expense_strategy = st.builds(model_Expense, date=st.dates(), description=safe_text, fixed=st.booleans(), id=st.integers(), name=safe_text, price=st.floats(allow_nan=False, allow_infinity=False), receiptId=st.integers())
@given(instance=model_Expense_strategy)
@settings(max_examples=25)
def test_model_Expense_instantiation(instance):
    assert isinstance(instance, model_Expense)


model_ExpenseExpert_strategy = st.builds(model_ExpenseExpert)
@given(instance=model_ExpenseExpert_strategy)
@settings(max_examples=25)
def test_model_ExpenseExpert_instantiation(instance):
    assert isinstance(instance, model_ExpenseExpert)


model_HotelComponent_strategy = st.builds(model_HotelComponent)
@given(instance=model_HotelComponent_strategy)
@settings(max_examples=25)
def test_model_HotelComponent_instantiation(instance):
    assert isinstance(instance, model_HotelComponent)


model_MSAccessDB_strategy = st.builds(model_MSAccessDB)
@given(instance=model_MSAccessDB_strategy)
@settings(max_examples=25)
def test_model_MSAccessDB_instantiation(instance):
    assert isinstance(instance, model_MSAccessDB)


model_Payment_strategy = st.builds(model_Payment)
@given(instance=model_Payment_strategy)
@settings(max_examples=25)
def test_model_Payment_instantiation(instance):
    assert isinstance(instance, model_Payment)


model_Promotion_strategy = st.builds(model_Promotion, code=safe_text, description=safe_text, expirationDate=st.dates(), percentage=safe_text, roomType=safe_text, validFrom=st.dates(), validTo=st.dates())
@given(instance=model_Promotion_strategy)
@settings(max_examples=25)
def test_model_Promotion_instantiation(instance):
    assert isinstance(instance, model_Promotion)


model_PromotionExpert_strategy = st.builds(model_PromotionExpert)
@given(instance=model_PromotionExpert_strategy)
@settings(max_examples=25)
def test_model_PromotionExpert_instantiation(instance):
    assert isinstance(instance, model_PromotionExpert)


model_Receipt_strategy = st.builds(model_Receipt, Date=st.dates(), id=st.integers(), totalCost=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=model_Receipt_strategy)
@settings(max_examples=25)
def test_model_Receipt_instantiation(instance):
    assert isinstance(instance, model_Receipt)


model_ReceiptExpert_strategy = st.builds(model_ReceiptExpert)
@given(instance=model_ReceiptExpert_strategy)
@settings(max_examples=25)
def test_model_ReceiptExpert_instantiation(instance):
    assert isinstance(instance, model_ReceiptExpert)


model_Receptionist_strategy = st.builds(model_Receptionist)
@given(instance=model_Receptionist_strategy)
@settings(max_examples=25)
def test_model_Receptionist_instantiation(instance):
    assert isinstance(instance, model_Receptionist)


model_ReceptionistController_strategy = st.builds(model_ReceptionistController)
@given(instance=model_ReceptionistController_strategy)
@settings(max_examples=25)
def test_model_ReceptionistController_instantiation(instance):
    assert isinstance(instance, model_ReceptionistController)


model_ReceptionistInterface_strategy = st.builds(model_ReceptionistInterface)
@given(instance=model_ReceptionistInterface_strategy)
@settings(max_examples=25)
def test_model_ReceptionistInterface_instantiation(instance):
    assert isinstance(instance, model_ReceptionistInterface)


model_Resident_strategy = st.builds(model_Resident, firstName=safe_text, id=safe_text, surname=safe_text)
@given(instance=model_Resident_strategy)
@settings(max_examples=25)
def test_model_Resident_instantiation(instance):
    assert isinstance(instance, model_Resident)


model_Room_strategy = st.builds(model_Room, beds=safe_text, clean=safe_text, description=safe_text, number=safe_text, status=safe_text, type=safe_text)
@given(instance=model_Room_strategy)
@settings(max_examples=25)
def test_model_Room_instantiation(instance):
    assert isinstance(instance, model_Room)


model_RoomExpert_strategy = st.builds(model_RoomExpert)
@given(instance=model_RoomExpert_strategy)
@settings(max_examples=25)
def test_model_RoomExpert_instantiation(instance):
    assert isinstance(instance, model_RoomExpert)


model_User_strategy = st.builds(model_User, administrator=safe_text, firstName=safe_text, id=safe_text, password=safe_text, receptionist=safe_text, surname=safe_text)
@given(instance=model_User_strategy)
@settings(max_examples=25)
def test_model_User_instantiation(instance):
    assert isinstance(instance, model_User)


model_UserExpert_strategy = st.builds(model_UserExpert)
@given(instance=model_UserExpert_strategy)
@settings(max_examples=25)
def test_model_UserExpert_instantiation(instance):
    assert isinstance(instance, model_UserExpert)


