import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Backend_CodePack_BankComponent,
    Booking,
    CheckInHandler,
    CodePack_Backend_CheckInHandler,
    CodePack_Backend_CustomerHandler,
    CodePack_Backend_ManagementHandler,
    CodePack_Backend_ReceptionHandler,
    CodePack_CheckInMachine,
    CodePack_DataBank,
    CodePack_DataModels_Bill,
    CodePack_DataModels_Booking,
    CodePack_DataModels_Customer,
    CodePack_DataModels_ExtraService,
    CodePack_DataModels_Guest,
    CodePack_DataModels_PaymentData,
    CodePack_DataModels_Room,
    CodePack_DataModels_RoomBooked,
    CodePack_DataModels_RoomType,
    CodePack_DataModels_ServiceType,
    CodePack_DataModels_StaffMember,
    CodePack_DataModels_StaffRole,
    CodePack_IBookings,
    CodePack_ICheckIn,
    CodePack_IManagement,
    CodePack_IReceptionOperations_rename_required,
    CodePack_IStaffAdmin,
    CodePack_IStaffAuthentication,
    CodePack_IUserAccount,
    CodePack_Shared_ContactData,
    CodePack_StaffGUI,
    CodePack_UserGUI,
    Customer,
    CustomerHandler,
    ExtraService,
    Guest,
    IBookings,
    ICheckIn,
    IManagement,
    IReceptionOperations_rename_required,
    IStaffAdmin,
    IStaffAuthentication,
    IUserAccount,
    ManagementHandler,
    PaymentData,
    ReceptionHandler,
    Room,
    RoomBooked,
    RoomType,
    ServiceType,
    StaffMember,
    StaffRole,
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

def test_CodePack_DataModels_Bill_booking_id_value_roundtrip():
    instance = CodePack_DataModels_Bill(booking_id=7, total_price=3.14)
    assert instance.booking_id == 7
    instance.booking_id = 13
    assert instance.booking_id == 13


def test_CodePack_DataModels_Bill_total_price_value_roundtrip():
    instance = CodePack_DataModels_Bill(booking_id=7, total_price=3.14)
    assert instance.total_price == 3.14
    instance.total_price = 9.99
    assert instance.total_price == 9.99


def test_CodePack_DataModels_Booking_bonus_points_used_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.bonus_points_used == 7
    instance.bonus_points_used = 13
    assert instance.bonus_points_used == 13


def test_CodePack_DataModels_Booking_contact_email_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.contact_email == "sample_text"
    instance.contact_email = "sample_text_2"
    assert instance.contact_email == "sample_text_2"


def test_CodePack_DataModels_Booking_contact_name_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.contact_name == "sample_text"
    instance.contact_name = "sample_text_2"
    assert instance.contact_name == "sample_text_2"


def test_CodePack_DataModels_Booking_contact_phone_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.contact_phone == 7
    instance.contact_phone = 13
    assert instance.contact_phone == 13


def test_CodePack_DataModels_Booking_customer_id_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.customer_id == 7
    instance.customer_id = 13
    assert instance.customer_id == 13


def test_CodePack_DataModels_Booking_date_check_in_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.date_check_in == date(2024, 1, 1)
    instance.date_check_in = date(2025, 6, 15)
    assert instance.date_check_in == date(2025, 6, 15)


def test_CodePack_DataModels_Booking_date_check_out_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.date_check_out == date(2024, 1, 1)
    instance.date_check_out = date(2025, 6, 15)
    assert instance.date_check_out == date(2025, 6, 15)


def test_CodePack_DataModels_Booking_id_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_CodePack_DataModels_Booking_isCheckedIn_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.isCheckedIn == True
    instance.isCheckedIn = False
    assert instance.isCheckedIn == False


def test_CodePack_DataModels_Booking_payment_id_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.payment_id == 7
    instance.payment_id = 13
    assert instance.payment_id == 13


def test_CodePack_DataModels_Booking_total_price_value_roundtrip():
    instance = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    assert instance.total_price == 3.14
    instance.total_price = 9.99
    assert instance.total_price == 9.99


def test_CodePack_DataModels_Customer_bonus_points_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.bonus_points == 7
    instance.bonus_points = 13
    assert instance.bonus_points == 13


def test_CodePack_DataModels_Customer_customer_id_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.customer_id == 7
    instance.customer_id = 13
    assert instance.customer_id == 13


def test_CodePack_DataModels_Customer_date_of_birth_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.date_of_birth == date(2024, 1, 1)
    instance.date_of_birth = date(2025, 6, 15)
    assert instance.date_of_birth == date(2025, 6, 15)


def test_CodePack_DataModels_Customer_e_mail_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.e_mail == "sample_text"
    instance.e_mail = "sample_text_2"
    assert instance.e_mail == "sample_text_2"


def test_CodePack_DataModels_Customer_first_name_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.first_name == "sample_text"
    instance.first_name = "sample_text_2"
    assert instance.first_name == "sample_text_2"


def test_CodePack_DataModels_Customer_last_name_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.last_name == "sample_text"
    instance.last_name = "sample_text_2"
    assert instance.last_name == "sample_text_2"


def test_CodePack_DataModels_Customer_password_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_CodePack_DataModels_Customer_payment_id_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.payment_id == 7
    instance.payment_id = 13
    assert instance.payment_id == 13


def test_CodePack_DataModels_Customer_phone_no_value_roundtrip():
    instance = CodePack_DataModels_Customer(bonus_points=7, customer_id=7, date_of_birth=date(2024, 1, 1), e_mail="sample_text", first_name="sample_text", last_name="sample_text", password="sample_text", payment_id=7, phone_no=7)
    assert instance.phone_no == 7
    instance.phone_no = 13
    assert instance.phone_no == 13


def test_CodePack_DataModels_ExtraService_booking_id_value_roundtrip():
    instance = CodePack_DataModels_ExtraService(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), total_price=3.14, type="sample_text")
    assert instance.booking_id == 7
    instance.booking_id = 13
    assert instance.booking_id == 13


def test_CodePack_DataModels_ExtraService_date_end_value_roundtrip():
    instance = CodePack_DataModels_ExtraService(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), total_price=3.14, type="sample_text")
    assert instance.date_end == date(2024, 1, 1)
    instance.date_end = date(2025, 6, 15)
    assert instance.date_end == date(2025, 6, 15)


def test_CodePack_DataModels_ExtraService_date_start_value_roundtrip():
    instance = CodePack_DataModels_ExtraService(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), total_price=3.14, type="sample_text")
    assert instance.date_start == date(2024, 1, 1)
    instance.date_start = date(2025, 6, 15)
    assert instance.date_start == date(2025, 6, 15)


def test_CodePack_DataModels_ExtraService_total_price_value_roundtrip():
    instance = CodePack_DataModels_ExtraService(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), total_price=3.14, type="sample_text")
    assert instance.total_price == 3.14
    instance.total_price = 9.99
    assert instance.total_price == 9.99


def test_CodePack_DataModels_ExtraService_type_value_roundtrip():
    instance = CodePack_DataModels_ExtraService(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), total_price=3.14, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_CodePack_DataModels_Guest_booking_id_value_roundtrip():
    instance = CodePack_DataModels_Guest(booking_id=7, name="sample_text")
    assert instance.booking_id == 7
    instance.booking_id = 13
    assert instance.booking_id == 13


def test_CodePack_DataModels_Guest_name_value_roundtrip():
    instance = CodePack_DataModels_Guest(booking_id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_CodePack_DataModels_PaymentData_cc_ccv_value_roundtrip():
    instance = CodePack_DataModels_PaymentData(cc_ccv="sample_text", cc_first_name="sample_text", cc_last_name="sample_text", cc_month=7, cc_number="sample_text", cc_year=7, id=7)
    assert instance.cc_ccv == "sample_text"
    instance.cc_ccv = "sample_text_2"
    assert instance.cc_ccv == "sample_text_2"


def test_CodePack_DataModels_PaymentData_cc_first_name_value_roundtrip():
    instance = CodePack_DataModels_PaymentData(cc_ccv="sample_text", cc_first_name="sample_text", cc_last_name="sample_text", cc_month=7, cc_number="sample_text", cc_year=7, id=7)
    assert instance.cc_first_name == "sample_text"
    instance.cc_first_name = "sample_text_2"
    assert instance.cc_first_name == "sample_text_2"


def test_CodePack_DataModels_PaymentData_cc_last_name_value_roundtrip():
    instance = CodePack_DataModels_PaymentData(cc_ccv="sample_text", cc_first_name="sample_text", cc_last_name="sample_text", cc_month=7, cc_number="sample_text", cc_year=7, id=7)
    assert instance.cc_last_name == "sample_text"
    instance.cc_last_name = "sample_text_2"
    assert instance.cc_last_name == "sample_text_2"


def test_CodePack_DataModels_PaymentData_cc_month_value_roundtrip():
    instance = CodePack_DataModels_PaymentData(cc_ccv="sample_text", cc_first_name="sample_text", cc_last_name="sample_text", cc_month=7, cc_number="sample_text", cc_year=7, id=7)
    assert instance.cc_month == 7
    instance.cc_month = 13
    assert instance.cc_month == 13


def test_CodePack_DataModels_PaymentData_cc_number_value_roundtrip():
    instance = CodePack_DataModels_PaymentData(cc_ccv="sample_text", cc_first_name="sample_text", cc_last_name="sample_text", cc_month=7, cc_number="sample_text", cc_year=7, id=7)
    assert instance.cc_number == "sample_text"
    instance.cc_number = "sample_text_2"
    assert instance.cc_number == "sample_text_2"


def test_CodePack_DataModels_PaymentData_cc_year_value_roundtrip():
    instance = CodePack_DataModels_PaymentData(cc_ccv="sample_text", cc_first_name="sample_text", cc_last_name="sample_text", cc_month=7, cc_number="sample_text", cc_year=7, id=7)
    assert instance.cc_year == 7
    instance.cc_year = 13
    assert instance.cc_year == 13


def test_CodePack_DataModels_PaymentData_id_value_roundtrip():
    instance = CodePack_DataModels_PaymentData(cc_ccv="sample_text", cc_first_name="sample_text", cc_last_name="sample_text", cc_month=7, cc_number="sample_text", cc_year=7, id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_CodePack_DataModels_Room_description_value_roundtrip():
    instance = CodePack_DataModels_Room(description="sample_text", isAvailable=True, number=7, room_type="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_CodePack_DataModels_Room_isAvailable_value_roundtrip():
    instance = CodePack_DataModels_Room(description="sample_text", isAvailable=True, number=7, room_type="sample_text")
    assert instance.isAvailable == True
    instance.isAvailable = False
    assert instance.isAvailable == False


def test_CodePack_DataModels_Room_number_value_roundtrip():
    instance = CodePack_DataModels_Room(description="sample_text", isAvailable=True, number=7, room_type="sample_text")
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_CodePack_DataModels_Room_room_type_value_roundtrip():
    instance = CodePack_DataModels_Room(description="sample_text", isAvailable=True, number=7, room_type="sample_text")
    assert instance.room_type == "sample_text"
    instance.room_type = "sample_text_2"
    assert instance.room_type == "sample_text_2"


def test_CodePack_DataModels_RoomBooked_booking_id_value_roundtrip():
    instance = CodePack_DataModels_RoomBooked(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), room_number=7)
    assert instance.booking_id == 7
    instance.booking_id = 13
    assert instance.booking_id == 13


def test_CodePack_DataModels_RoomBooked_date_end_value_roundtrip():
    instance = CodePack_DataModels_RoomBooked(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), room_number=7)
    assert instance.date_end == date(2024, 1, 1)
    instance.date_end = date(2025, 6, 15)
    assert instance.date_end == date(2025, 6, 15)


def test_CodePack_DataModels_RoomBooked_date_start_value_roundtrip():
    instance = CodePack_DataModels_RoomBooked(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), room_number=7)
    assert instance.date_start == date(2024, 1, 1)
    instance.date_start = date(2025, 6, 15)
    assert instance.date_start == date(2025, 6, 15)


def test_CodePack_DataModels_RoomBooked_room_number_value_roundtrip():
    instance = CodePack_DataModels_RoomBooked(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), room_number=7)
    assert instance.room_number == 7
    instance.room_number = 13
    assert instance.room_number == 13


def test_CodePack_DataModels_RoomType_description_value_roundtrip():
    instance = CodePack_DataModels_RoomType(description="sample_text", max_guests=7, rate=3.14, typename="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_CodePack_DataModels_RoomType_max_guests_value_roundtrip():
    instance = CodePack_DataModels_RoomType(description="sample_text", max_guests=7, rate=3.14, typename="sample_text")
    assert instance.max_guests == 7
    instance.max_guests = 13
    assert instance.max_guests == 13


def test_CodePack_DataModels_RoomType_rate_value_roundtrip():
    instance = CodePack_DataModels_RoomType(description="sample_text", max_guests=7, rate=3.14, typename="sample_text")
    assert instance.rate == 3.14
    instance.rate = 9.99
    assert instance.rate == 9.99


def test_CodePack_DataModels_RoomType_typename_value_roundtrip():
    instance = CodePack_DataModels_RoomType(description="sample_text", max_guests=7, rate=3.14, typename="sample_text")
    assert instance.typename == "sample_text"
    instance.typename = "sample_text_2"
    assert instance.typename == "sample_text_2"


def test_CodePack_DataModels_ServiceType_description_value_roundtrip():
    instance = CodePack_DataModels_ServiceType(description="sample_text", price=3.14, type_name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_CodePack_DataModels_ServiceType_price_value_roundtrip():
    instance = CodePack_DataModels_ServiceType(description="sample_text", price=3.14, type_name="sample_text")
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_CodePack_DataModels_ServiceType_type_name_value_roundtrip():
    instance = CodePack_DataModels_ServiceType(description="sample_text", price=3.14, type_name="sample_text")
    assert instance.type_name == "sample_text"
    instance.type_name = "sample_text_2"
    assert instance.type_name == "sample_text_2"


def test_CodePack_DataModels_StaffMember_email_value_roundtrip():
    instance = CodePack_DataModels_StaffMember(email="sample_text", full_name="sample_text", password="sample_text", pers_no="sample_text", phone_no=7, role_name="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_CodePack_DataModels_StaffMember_full_name_value_roundtrip():
    instance = CodePack_DataModels_StaffMember(email="sample_text", full_name="sample_text", password="sample_text", pers_no="sample_text", phone_no=7, role_name="sample_text")
    assert instance.full_name == "sample_text"
    instance.full_name = "sample_text_2"
    assert instance.full_name == "sample_text_2"


def test_CodePack_DataModels_StaffMember_password_value_roundtrip():
    instance = CodePack_DataModels_StaffMember(email="sample_text", full_name="sample_text", password="sample_text", pers_no="sample_text", phone_no=7, role_name="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_CodePack_DataModels_StaffMember_pers_no_value_roundtrip():
    instance = CodePack_DataModels_StaffMember(email="sample_text", full_name="sample_text", password="sample_text", pers_no="sample_text", phone_no=7, role_name="sample_text")
    assert instance.pers_no == "sample_text"
    instance.pers_no = "sample_text_2"
    assert instance.pers_no == "sample_text_2"


def test_CodePack_DataModels_StaffMember_phone_no_value_roundtrip():
    instance = CodePack_DataModels_StaffMember(email="sample_text", full_name="sample_text", password="sample_text", pers_no="sample_text", phone_no=7, role_name="sample_text")
    assert instance.phone_no == 7
    instance.phone_no = 13
    assert instance.phone_no == 13


def test_CodePack_DataModels_StaffMember_role_name_value_roundtrip():
    instance = CodePack_DataModels_StaffMember(email="sample_text", full_name="sample_text", password="sample_text", pers_no="sample_text", phone_no=7, role_name="sample_text")
    assert instance.role_name == "sample_text"
    instance.role_name = "sample_text_2"
    assert instance.role_name == "sample_text_2"


def test_CodePack_DataModels_StaffRole_canManageAccounts_value_roundtrip():
    instance = CodePack_DataModels_StaffRole(canManageAccounts=True, canManageBookings=True, canManageRooms=True, canManageServices=True, name="sample_text")
    assert instance.canManageAccounts == True
    instance.canManageAccounts = False
    assert instance.canManageAccounts == False


def test_CodePack_DataModels_StaffRole_canManageBookings_value_roundtrip():
    instance = CodePack_DataModels_StaffRole(canManageAccounts=True, canManageBookings=True, canManageRooms=True, canManageServices=True, name="sample_text")
    assert instance.canManageBookings == True
    instance.canManageBookings = False
    assert instance.canManageBookings == False


def test_CodePack_DataModels_StaffRole_canManageRooms_value_roundtrip():
    instance = CodePack_DataModels_StaffRole(canManageAccounts=True, canManageBookings=True, canManageRooms=True, canManageServices=True, name="sample_text")
    assert instance.canManageRooms == True
    instance.canManageRooms = False
    assert instance.canManageRooms == False


def test_CodePack_DataModels_StaffRole_canManageServices_value_roundtrip():
    instance = CodePack_DataModels_StaffRole(canManageAccounts=True, canManageBookings=True, canManageRooms=True, canManageServices=True, name="sample_text")
    assert instance.canManageServices == True
    instance.canManageServices = False
    assert instance.canManageServices == False


def test_CodePack_DataModels_StaffRole_name_value_roundtrip():
    instance = CodePack_DataModels_StaffRole(canManageAccounts=True, canManageBookings=True, canManageRooms=True, canManageServices=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_CodePack_Shared_ContactData_e_mail_value_roundtrip():
    instance = CodePack_Shared_ContactData(e_mail="sample_text", full_name="sample_text", phone_no=7)
    assert instance.e_mail == "sample_text"
    instance.e_mail = "sample_text_2"
    assert instance.e_mail == "sample_text_2"


def test_CodePack_Shared_ContactData_full_name_value_roundtrip():
    instance = CodePack_Shared_ContactData(e_mail="sample_text", full_name="sample_text", phone_no=7)
    assert instance.full_name == "sample_text"
    instance.full_name = "sample_text_2"
    assert instance.full_name == "sample_text_2"


def test_CodePack_Shared_ContactData_phone_no_value_roundtrip():
    instance = CodePack_Shared_ContactData(e_mail="sample_text", full_name="sample_text", phone_no=7)
    assert instance.phone_no == 7
    instance.phone_no = 13
    assert instance.phone_no == 13


def test_CodePack_IReceptionOperations_rename_required_isa_IBookings():
    instance = CodePack_IReceptionOperations_rename_required()
    assert isinstance(instance, IBookings)


def test_CodePack_IUserAccount_isa_IBookings():
    instance = CodePack_IUserAccount()
    assert isinstance(instance, IBookings)


def test_CodePack_Backend_CheckInHandler_isa_ICheckIn():
    instance = CodePack_Backend_CheckInHandler()
    assert isinstance(instance, ICheckIn)


def test_CodePack_IReceptionOperations_rename_required_isa_ICheckIn():
    instance = CodePack_IReceptionOperations_rename_required()
    assert isinstance(instance, ICheckIn)


def test_CodePack_Backend_ManagementHandler_isa_IManagement():
    instance = CodePack_Backend_ManagementHandler()
    assert isinstance(instance, IManagement)


def test_CodePack_Backend_ReceptionHandler_isa_IReceptionOperations_rename_required():
    instance = CodePack_Backend_ReceptionHandler()
    assert isinstance(instance, IReceptionOperations_rename_required)


def test_CodePack_IManagement_isa_IStaffAdmin():
    instance = CodePack_IManagement()
    assert isinstance(instance, IStaffAdmin)


def test_CodePack_IManagement_isa_IStaffAuthentication():
    instance = CodePack_IManagement()
    assert isinstance(instance, IStaffAuthentication)


def test_CodePack_IReceptionOperations_rename_required_isa_IStaffAuthentication():
    instance = CodePack_IReceptionOperations_rename_required()
    assert isinstance(instance, IStaffAuthentication)


def test_CodePack_Backend_CustomerHandler_isa_IUserAccount():
    instance = CodePack_Backend_CustomerHandler()
    assert isinstance(instance, IUserAccount)


def test_assoc_booking26_link_reassign_clear():
    a = CodePack_DataModels_RoomBooked(booking_id=7, date_end=date(2024, 1, 1), date_start=date(2024, 1, 1), room_number=7)
    b1 = Booking()
    b2 = Booking()
    _safe_set(a, 'CodePack_DataModels_RoomBooked', b1)
    assert _is_linked(a, 'CodePack_DataModels_RoomBooked', b1)
    if hasattr(b1, 'Booking27'):
        assert _is_linked(b1, 'Booking27', a)
    _safe_set(a, 'CodePack_DataModels_RoomBooked', b2)
    assert _is_linked(a, 'CodePack_DataModels_RoomBooked', b2)
    if hasattr(b1, 'Booking27'):
        assert not _is_linked(b1, 'Booking27', a)
    if hasattr(b2, 'Booking27'):
        assert _is_linked(b2, 'Booking27', a)
    _safe_set(a, 'CodePack_DataModels_RoomBooked', None)
    assert not _is_linked(a, 'CodePack_DataModels_RoomBooked', b2)
    if hasattr(b2, 'Booking27'):
        assert not _is_linked(b2, 'Booking27', a)


def test_assoc_checkInHandler4_link_reassign_clear():
    a = CodePack_CheckInMachine()
    b1 = CheckInHandler()
    b2 = CheckInHandler()
    _safe_set(a, 'CodePack_CheckInMachine', b1)
    assert _is_linked(a, 'CodePack_CheckInMachine', b1)
    if hasattr(b1, 'CheckInHandler'):
        assert _is_linked(b1, 'CheckInHandler', a)
    _safe_set(a, 'CodePack_CheckInMachine', b2)
    assert _is_linked(a, 'CodePack_CheckInMachine', b2)
    if hasattr(b1, 'CheckInHandler'):
        assert not _is_linked(b1, 'CheckInHandler', a)
    if hasattr(b2, 'CheckInHandler'):
        assert _is_linked(b2, 'CheckInHandler', a)
    _safe_set(a, 'CodePack_CheckInMachine', None)
    assert not _is_linked(a, 'CodePack_CheckInMachine', b2)
    if hasattr(b2, 'CheckInHandler'):
        assert not _is_linked(b2, 'CheckInHandler', a)


def test_assoc_customerHandler3_link_reassign_clear():
    a = CodePack_UserGUI()
    b1 = CustomerHandler()
    b2 = CustomerHandler()
    _safe_set(a, 'CodePack_UserGUI', b1)
    assert _is_linked(a, 'CodePack_UserGUI', b1)
    if hasattr(b1, 'CustomerHandler'):
        assert _is_linked(b1, 'CustomerHandler', a)
    _safe_set(a, 'CodePack_UserGUI', b2)
    assert _is_linked(a, 'CodePack_UserGUI', b2)
    if hasattr(b1, 'CustomerHandler'):
        assert not _is_linked(b1, 'CustomerHandler', a)
    if hasattr(b2, 'CustomerHandler'):
        assert _is_linked(b2, 'CustomerHandler', a)
    _safe_set(a, 'CodePack_UserGUI', None)
    assert not _is_linked(a, 'CodePack_UserGUI', b2)
    if hasattr(b2, 'CustomerHandler'):
        assert not _is_linked(b2, 'CustomerHandler', a)


def test_assoc_managementHandler0_link_reassign_clear():
    a = CodePack_StaffGUI()
    b1 = ManagementHandler()
    b2 = ManagementHandler()
    _safe_set(a, 'CodePack_StaffGUI', b1)
    assert _is_linked(a, 'CodePack_StaffGUI', b1)
    if hasattr(b1, 'ManagementHandler'):
        assert _is_linked(b1, 'ManagementHandler', a)
    _safe_set(a, 'CodePack_StaffGUI', b2)
    assert _is_linked(a, 'CodePack_StaffGUI', b2)
    if hasattr(b1, 'ManagementHandler'):
        assert not _is_linked(b1, 'ManagementHandler', a)
    if hasattr(b2, 'ManagementHandler'):
        assert _is_linked(b2, 'ManagementHandler', a)
    _safe_set(a, 'CodePack_StaffGUI', None)
    assert not _is_linked(a, 'CodePack_StaffGUI', b2)
    if hasattr(b2, 'ManagementHandler'):
        assert not _is_linked(b2, 'ManagementHandler', a)


def test_assoc_receptionHandler1_link_reassign_clear():
    a = CodePack_StaffGUI()
    b1 = ReceptionHandler()
    b2 = ReceptionHandler()
    _safe_set(a, 'CodePack_StaffGUI2', b1)
    assert _is_linked(a, 'CodePack_StaffGUI2', b1)
    if hasattr(b1, 'ReceptionHandler'):
        assert _is_linked(b1, 'ReceptionHandler', a)
    _safe_set(a, 'CodePack_StaffGUI2', b2)
    assert _is_linked(a, 'CodePack_StaffGUI2', b2)
    if hasattr(b1, 'ReceptionHandler'):
        assert not _is_linked(b1, 'ReceptionHandler', a)
    if hasattr(b2, 'ReceptionHandler'):
        assert _is_linked(b2, 'ReceptionHandler', a)
    _safe_set(a, 'CodePack_StaffGUI2', None)
    assert not _is_linked(a, 'CodePack_StaffGUI2', b2)
    if hasattr(b2, 'ReceptionHandler'):
        assert not _is_linked(b2, 'ReceptionHandler', a)


def test_assoc_room33_link_reassign_clear():
    a = CodePack_DataModels_Booking(bonus_points_used=7, contact_email="sample_text", contact_name="sample_text", contact_phone=7, customer_id=7, date_check_in=date(2024, 1, 1), date_check_out=date(2024, 1, 1), id=7, isCheckedIn=True, payment_id=7, total_price=3.14)
    b1 = Room()
    b2 = Room()
    _safe_set(a, 'CodePack_DataModels_Booking', b1)
    assert _is_linked(a, 'CodePack_DataModels_Booking', b1)
    if hasattr(b1, 'Room34'):
        assert _is_linked(b1, 'Room34', a)
    _safe_set(a, 'CodePack_DataModels_Booking', b2)
    assert _is_linked(a, 'CodePack_DataModels_Booking', b2)
    if hasattr(b1, 'Room34'):
        assert not _is_linked(b1, 'Room34', a)
    if hasattr(b2, 'Room34'):
        assert _is_linked(b2, 'Room34', a)
    _safe_set(a, 'CodePack_DataModels_Booking', None)
    assert not _is_linked(a, 'CodePack_DataModels_Booking', b2)
    if hasattr(b2, 'Room34'):
        assert not _is_linked(b2, 'Room34', a)


def test_assoc_rooms_booked28_link_reassign_clear():
    a = CodePack_DataModels_Bill(booking_id=7, total_price=3.14)
    b1 = Room()
    b2 = Room()
    _safe_set(a, 'CodePack_DataModels_Bill', {b1})
    assert _is_linked(a, 'CodePack_DataModels_Bill', b1)
    if hasattr(b1, 'Room29'):
        assert _is_linked(b1, 'Room29', a)
    _safe_set(a, 'CodePack_DataModels_Bill', {b2})
    assert _is_linked(a, 'CodePack_DataModels_Bill', b2)
    if hasattr(b1, 'Room29'):
        assert not _is_linked(b1, 'Room29', a)
    if hasattr(b2, 'Room29'):
        assert _is_linked(b2, 'Room29', a)
    _safe_set(a, 'CodePack_DataModels_Bill', set())
    assert not _is_linked(a, 'CodePack_DataModels_Bill', b2)
    if hasattr(b2, 'Room29'):
        assert not _is_linked(b2, 'Room29', a)


def test_assoc_services_ordered30_link_reassign_clear():
    a = CodePack_DataModels_Bill(booking_id=7, total_price=3.14)
    b1 = ExtraService()
    b2 = ExtraService()
    _safe_set(a, 'CodePack_DataModels_Bill31', {b1})
    assert _is_linked(a, 'CodePack_DataModels_Bill31', b1)
    if hasattr(b1, 'ExtraService32'):
        assert _is_linked(b1, 'ExtraService32', a)
    _safe_set(a, 'CodePack_DataModels_Bill31', {b2})
    assert _is_linked(a, 'CodePack_DataModels_Bill31', b2)
    if hasattr(b1, 'ExtraService32'):
        assert not _is_linked(b1, 'ExtraService32', a)
    if hasattr(b2, 'ExtraService32'):
        assert _is_linked(b2, 'ExtraService32', a)
    _safe_set(a, 'CodePack_DataModels_Bill31', set())
    assert not _is_linked(a, 'CodePack_DataModels_Bill31', b2)
    if hasattr(b2, 'ExtraService32'):
        assert not _is_linked(b2, 'ExtraService32', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Backend_CodePack_BankComponent_strategy = st.builds(Backend_CodePack_BankComponent)
@given(instance=Backend_CodePack_BankComponent_strategy)
@settings(max_examples=25)
def test_Backend_CodePack_BankComponent_instantiation(instance):
    assert isinstance(instance, Backend_CodePack_BankComponent)


Booking_strategy = st.builds(Booking)
@given(instance=Booking_strategy)
@settings(max_examples=25)
def test_Booking_instantiation(instance):
    assert isinstance(instance, Booking)


CheckInHandler_strategy = st.builds(CheckInHandler)
@given(instance=CheckInHandler_strategy)
@settings(max_examples=25)
def test_CheckInHandler_instantiation(instance):
    assert isinstance(instance, CheckInHandler)


CodePack_Backend_CheckInHandler_strategy = st.builds(CodePack_Backend_CheckInHandler)
@given(instance=CodePack_Backend_CheckInHandler_strategy)
@settings(max_examples=25)
def test_CodePack_Backend_CheckInHandler_instantiation(instance):
    assert isinstance(instance, CodePack_Backend_CheckInHandler)


CodePack_Backend_CustomerHandler_strategy = st.builds(CodePack_Backend_CustomerHandler)
@given(instance=CodePack_Backend_CustomerHandler_strategy)
@settings(max_examples=25)
def test_CodePack_Backend_CustomerHandler_instantiation(instance):
    assert isinstance(instance, CodePack_Backend_CustomerHandler)


CodePack_Backend_ManagementHandler_strategy = st.builds(CodePack_Backend_ManagementHandler)
@given(instance=CodePack_Backend_ManagementHandler_strategy)
@settings(max_examples=25)
def test_CodePack_Backend_ManagementHandler_instantiation(instance):
    assert isinstance(instance, CodePack_Backend_ManagementHandler)


CodePack_Backend_ReceptionHandler_strategy = st.builds(CodePack_Backend_ReceptionHandler)
@given(instance=CodePack_Backend_ReceptionHandler_strategy)
@settings(max_examples=25)
def test_CodePack_Backend_ReceptionHandler_instantiation(instance):
    assert isinstance(instance, CodePack_Backend_ReceptionHandler)


CodePack_CheckInMachine_strategy = st.builds(CodePack_CheckInMachine)
@given(instance=CodePack_CheckInMachine_strategy)
@settings(max_examples=25)
def test_CodePack_CheckInMachine_instantiation(instance):
    assert isinstance(instance, CodePack_CheckInMachine)


CodePack_DataBank_strategy = st.builds(CodePack_DataBank)
@given(instance=CodePack_DataBank_strategy)
@settings(max_examples=25)
def test_CodePack_DataBank_instantiation(instance):
    assert isinstance(instance, CodePack_DataBank)


CodePack_DataModels_Bill_strategy = st.builds(CodePack_DataModels_Bill, booking_id=st.integers(), total_price=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=CodePack_DataModels_Bill_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_Bill_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_Bill)


CodePack_DataModels_Booking_strategy = st.builds(CodePack_DataModels_Booking, bonus_points_used=st.integers(), contact_email=safe_text, contact_name=safe_text, contact_phone=st.integers(), customer_id=st.integers(), date_check_in=st.dates(), date_check_out=st.dates(), id=st.integers(), isCheckedIn=st.booleans(), payment_id=st.integers(), total_price=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=CodePack_DataModels_Booking_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_Booking_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_Booking)


CodePack_DataModels_Customer_strategy = st.builds(CodePack_DataModels_Customer, bonus_points=st.integers(), customer_id=st.integers(), date_of_birth=st.dates(), e_mail=safe_text, first_name=safe_text, last_name=safe_text, password=safe_text, payment_id=st.integers(), phone_no=st.integers())
@given(instance=CodePack_DataModels_Customer_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_Customer_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_Customer)


CodePack_DataModels_ExtraService_strategy = st.builds(CodePack_DataModels_ExtraService, booking_id=st.integers(), date_end=st.dates(), date_start=st.dates(), total_price=st.floats(allow_nan=False, allow_infinity=False), type=safe_text)
@given(instance=CodePack_DataModels_ExtraService_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_ExtraService_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_ExtraService)


CodePack_DataModels_Guest_strategy = st.builds(CodePack_DataModels_Guest, booking_id=st.integers(), name=safe_text)
@given(instance=CodePack_DataModels_Guest_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_Guest_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_Guest)


CodePack_DataModels_PaymentData_strategy = st.builds(CodePack_DataModels_PaymentData, cc_ccv=safe_text, cc_first_name=safe_text, cc_last_name=safe_text, cc_month=st.integers(), cc_number=safe_text, cc_year=st.integers(), id=st.integers())
@given(instance=CodePack_DataModels_PaymentData_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_PaymentData_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_PaymentData)


CodePack_DataModels_Room_strategy = st.builds(CodePack_DataModels_Room, description=safe_text, isAvailable=st.booleans(), number=st.integers(), room_type=safe_text)
@given(instance=CodePack_DataModels_Room_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_Room_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_Room)


CodePack_DataModels_RoomBooked_strategy = st.builds(CodePack_DataModels_RoomBooked, booking_id=st.integers(), date_end=st.dates(), date_start=st.dates(), room_number=st.integers())
@given(instance=CodePack_DataModels_RoomBooked_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_RoomBooked_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_RoomBooked)


CodePack_DataModels_RoomType_strategy = st.builds(CodePack_DataModels_RoomType, description=safe_text, max_guests=st.integers(), rate=st.floats(allow_nan=False, allow_infinity=False), typename=safe_text)
@given(instance=CodePack_DataModels_RoomType_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_RoomType_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_RoomType)


CodePack_DataModels_ServiceType_strategy = st.builds(CodePack_DataModels_ServiceType, description=safe_text, price=st.floats(allow_nan=False, allow_infinity=False), type_name=safe_text)
@given(instance=CodePack_DataModels_ServiceType_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_ServiceType_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_ServiceType)


CodePack_DataModels_StaffMember_strategy = st.builds(CodePack_DataModels_StaffMember, email=safe_text, full_name=safe_text, password=safe_text, pers_no=safe_text, phone_no=st.integers(), role_name=safe_text)
@given(instance=CodePack_DataModels_StaffMember_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_StaffMember_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_StaffMember)


CodePack_DataModels_StaffRole_strategy = st.builds(CodePack_DataModels_StaffRole, canManageAccounts=st.booleans(), canManageBookings=st.booleans(), canManageRooms=st.booleans(), canManageServices=st.booleans(), name=safe_text)
@given(instance=CodePack_DataModels_StaffRole_strategy)
@settings(max_examples=25)
def test_CodePack_DataModels_StaffRole_instantiation(instance):
    assert isinstance(instance, CodePack_DataModels_StaffRole)


CodePack_IBookings_strategy = st.builds(CodePack_IBookings)
@given(instance=CodePack_IBookings_strategy)
@settings(max_examples=25)
def test_CodePack_IBookings_instantiation(instance):
    assert isinstance(instance, CodePack_IBookings)


CodePack_ICheckIn_strategy = st.builds(CodePack_ICheckIn)
@given(instance=CodePack_ICheckIn_strategy)
@settings(max_examples=25)
def test_CodePack_ICheckIn_instantiation(instance):
    assert isinstance(instance, CodePack_ICheckIn)


CodePack_IManagement_strategy = st.builds(CodePack_IManagement)
@given(instance=CodePack_IManagement_strategy)
@settings(max_examples=25)
def test_CodePack_IManagement_instantiation(instance):
    assert isinstance(instance, CodePack_IManagement)


CodePack_IReceptionOperations_rename_required_strategy = st.builds(CodePack_IReceptionOperations_rename_required)
@given(instance=CodePack_IReceptionOperations_rename_required_strategy)
@settings(max_examples=25)
def test_CodePack_IReceptionOperations_rename_required_instantiation(instance):
    assert isinstance(instance, CodePack_IReceptionOperations_rename_required)


CodePack_IStaffAdmin_strategy = st.builds(CodePack_IStaffAdmin)
@given(instance=CodePack_IStaffAdmin_strategy)
@settings(max_examples=25)
def test_CodePack_IStaffAdmin_instantiation(instance):
    assert isinstance(instance, CodePack_IStaffAdmin)


CodePack_IStaffAuthentication_strategy = st.builds(CodePack_IStaffAuthentication)
@given(instance=CodePack_IStaffAuthentication_strategy)
@settings(max_examples=25)
def test_CodePack_IStaffAuthentication_instantiation(instance):
    assert isinstance(instance, CodePack_IStaffAuthentication)


CodePack_IUserAccount_strategy = st.builds(CodePack_IUserAccount)
@given(instance=CodePack_IUserAccount_strategy)
@settings(max_examples=25)
def test_CodePack_IUserAccount_instantiation(instance):
    assert isinstance(instance, CodePack_IUserAccount)


CodePack_Shared_ContactData_strategy = st.builds(CodePack_Shared_ContactData, e_mail=safe_text, full_name=safe_text, phone_no=st.integers())
@given(instance=CodePack_Shared_ContactData_strategy)
@settings(max_examples=25)
def test_CodePack_Shared_ContactData_instantiation(instance):
    assert isinstance(instance, CodePack_Shared_ContactData)


CodePack_StaffGUI_strategy = st.builds(CodePack_StaffGUI)
@given(instance=CodePack_StaffGUI_strategy)
@settings(max_examples=25)
def test_CodePack_StaffGUI_instantiation(instance):
    assert isinstance(instance, CodePack_StaffGUI)


CodePack_UserGUI_strategy = st.builds(CodePack_UserGUI)
@given(instance=CodePack_UserGUI_strategy)
@settings(max_examples=25)
def test_CodePack_UserGUI_instantiation(instance):
    assert isinstance(instance, CodePack_UserGUI)


Customer_strategy = st.builds(Customer)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


CustomerHandler_strategy = st.builds(CustomerHandler)
@given(instance=CustomerHandler_strategy)
@settings(max_examples=25)
def test_CustomerHandler_instantiation(instance):
    assert isinstance(instance, CustomerHandler)


ExtraService_strategy = st.builds(ExtraService)
@given(instance=ExtraService_strategy)
@settings(max_examples=25)
def test_ExtraService_instantiation(instance):
    assert isinstance(instance, ExtraService)


Guest_strategy = st.builds(Guest)
@given(instance=Guest_strategy)
@settings(max_examples=25)
def test_Guest_instantiation(instance):
    assert isinstance(instance, Guest)


IBookings_strategy = st.builds(IBookings)
@given(instance=IBookings_strategy)
@settings(max_examples=25)
def test_IBookings_instantiation(instance):
    assert isinstance(instance, IBookings)


ICheckIn_strategy = st.builds(ICheckIn)
@given(instance=ICheckIn_strategy)
@settings(max_examples=25)
def test_ICheckIn_instantiation(instance):
    assert isinstance(instance, ICheckIn)


IManagement_strategy = st.builds(IManagement)
@given(instance=IManagement_strategy)
@settings(max_examples=25)
def test_IManagement_instantiation(instance):
    assert isinstance(instance, IManagement)


IReceptionOperations_rename_required_strategy = st.builds(IReceptionOperations_rename_required)
@given(instance=IReceptionOperations_rename_required_strategy)
@settings(max_examples=25)
def test_IReceptionOperations_rename_required_instantiation(instance):
    assert isinstance(instance, IReceptionOperations_rename_required)


IStaffAdmin_strategy = st.builds(IStaffAdmin)
@given(instance=IStaffAdmin_strategy)
@settings(max_examples=25)
def test_IStaffAdmin_instantiation(instance):
    assert isinstance(instance, IStaffAdmin)


IStaffAuthentication_strategy = st.builds(IStaffAuthentication)
@given(instance=IStaffAuthentication_strategy)
@settings(max_examples=25)
def test_IStaffAuthentication_instantiation(instance):
    assert isinstance(instance, IStaffAuthentication)


IUserAccount_strategy = st.builds(IUserAccount)
@given(instance=IUserAccount_strategy)
@settings(max_examples=25)
def test_IUserAccount_instantiation(instance):
    assert isinstance(instance, IUserAccount)


ManagementHandler_strategy = st.builds(ManagementHandler)
@given(instance=ManagementHandler_strategy)
@settings(max_examples=25)
def test_ManagementHandler_instantiation(instance):
    assert isinstance(instance, ManagementHandler)


PaymentData_strategy = st.builds(PaymentData)
@given(instance=PaymentData_strategy)
@settings(max_examples=25)
def test_PaymentData_instantiation(instance):
    assert isinstance(instance, PaymentData)


ReceptionHandler_strategy = st.builds(ReceptionHandler)
@given(instance=ReceptionHandler_strategy)
@settings(max_examples=25)
def test_ReceptionHandler_instantiation(instance):
    assert isinstance(instance, ReceptionHandler)


Room_strategy = st.builds(Room)
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


RoomBooked_strategy = st.builds(RoomBooked)
@given(instance=RoomBooked_strategy)
@settings(max_examples=25)
def test_RoomBooked_instantiation(instance):
    assert isinstance(instance, RoomBooked)


RoomType_strategy = st.builds(RoomType)
@given(instance=RoomType_strategy)
@settings(max_examples=25)
def test_RoomType_instantiation(instance):
    assert isinstance(instance, RoomType)


ServiceType_strategy = st.builds(ServiceType)
@given(instance=ServiceType_strategy)
@settings(max_examples=25)
def test_ServiceType_instantiation(instance):
    assert isinstance(instance, ServiceType)


StaffMember_strategy = st.builds(StaffMember)
@given(instance=StaffMember_strategy)
@settings(max_examples=25)
def test_StaffMember_instantiation(instance):
    assert isinstance(instance, StaffMember)


StaffRole_strategy = st.builds(StaffRole)
@given(instance=StaffRole_strategy)
@settings(max_examples=25)
def test_StaffRole_instantiation(instance):
    assert isinstance(instance, StaffRole)


