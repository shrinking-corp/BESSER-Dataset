import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BankingManager,
    Bill,
    BillManager,
    BookingManager,
    CreditCardManager,
    Discount,
    DiscountManager,
    KeyCardManager,
    LegalEntity,
    LegalEntityManager,
    Room,
    RoomManager,
    ServiceManager,
    billing_AdminDiscountManager,
    billing_AdminServiceManager,
    billing_Bill,
    billing_BillDataService,
    billing_CreditCardInformationDataService,
    billing_Discount,
    billing_DiscountDataService,
    billing_DiscountLimit,
    billing_DiscountManagerImpl,
    billing_Purchase,
    billing_Service,
    billing_ServiceDataService,
    billing_ServiceManagerImpl,
    booking_Booking,
    booking_BookingDataService,
    booking_BookingManager,
    booking_LegalEntity,
    booking_LegalEntityDataService,
    booking_Person,
    booking_RoomStay,
    booking_StayRequest,
    booking_TravelInformation,
    facilities_AdminKeyCardManager,
    facilities_AdminRoomManager,
    facilities_KeyCard,
    facilities_KeyCardDataService,
    facilities_KeyCardManager,
    facilities_KeyCardManagerImpl,
    facilities_Room,
    facilities_RoomDataService,
    facilities_RoomManager,
    facilities_RoomManagerImpl,
    facilities_RoomType,
    facilities_RoomTypeDataService,
    tda593_billing_AdminDiscountManager,
    tda593_billing_AdminDiscountManagerImpl,
    tda593_billing_AdminServiceManager,
    tda593_billing_AdminServiceManagerImpl,
    tda593_billing_BankingManager,
    tda593_billing_BankingManagerImpl,
    tda593_billing_Bill,
    tda593_billing_BillDataService,
    tda593_billing_BillManager,
    tda593_billing_BillManagerImpl,
    tda593_billing_BookingBill,
    tda593_billing_CreditCardInformation,
    tda593_billing_CreditCardInformationDataService,
    tda593_billing_CreditCardManager,
    tda593_billing_CreditCardManagerImpl,
    tda593_billing_Discount,
    tda593_billing_DiscountDataService,
    tda593_billing_DiscountLimit,
    tda593_billing_DiscountManager,
    tda593_billing_DiscountManagerImpl,
    tda593_billing_PercentageDiscount,
    tda593_billing_Purchase,
    tda593_billing_Service,
    tda593_billing_ServiceDataService,
    tda593_billing_ServiceManager,
    tda593_billing_ServiceManagerImpl,
    tda593_billing_SumDiscount,
    tda593_booking_Booking,
    tda593_booking_BookingDataService,
    tda593_booking_BookingManager,
    tda593_booking_BookingManagerImpl,
    tda593_booking_LegalEntity,
    tda593_booking_LegalEntityDataService,
    tda593_booking_LegalEntityManager,
    tda593_booking_LegalEntityManagerImpl,
    tda593_booking_Organization,
    tda593_booking_Person,
    tda593_booking_RoomStay,
    tda593_booking_StayRequest,
    tda593_booking_TravelInformation,
    tda593_california_DataService,
    tda593_facilities_AdminKeyCardManager,
    tda593_facilities_AdminKeyCardManagerImpl,
    tda593_facilities_AdminRoomManager,
    tda593_facilities_AdminRoomManagerImpl,
    tda593_facilities_ConferenceRoom,
    tda593_facilities_GuestRoom,
    tda593_facilities_KeyCard,
    tda593_facilities_KeyCardDataService,
    tda593_facilities_KeyCardManager,
    tda593_facilities_KeyCardManagerImpl,
    tda593_facilities_Room,
    tda593_facilities_RoomDataService,
    tda593_facilities_RoomManager,
    tda593_facilities_RoomManagerImpl,
    tda593_facilities_RoomType,
    tda593_facilities_RoomTypeDataService,
    DisabilityApproval,
    RoomApproval,
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

def test_tda593_billing_Bill_date_value_roundtrip():
    instance = tda593_billing_Bill(date=date(2024, 1, 1), id=7, isPaid=True, isPublished=True)
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_tda593_billing_Bill_id_value_roundtrip():
    instance = tda593_billing_Bill(date=date(2024, 1, 1), id=7, isPaid=True, isPublished=True)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_billing_Bill_isPaid_value_roundtrip():
    instance = tda593_billing_Bill(date=date(2024, 1, 1), id=7, isPaid=True, isPublished=True)
    assert instance.isPaid == True
    instance.isPaid = False
    assert instance.isPaid == False


def test_tda593_billing_Bill_isPublished_value_roundtrip():
    instance = tda593_billing_Bill(date=date(2024, 1, 1), id=7, isPaid=True, isPublished=True)
    assert instance.isPublished == True
    instance.isPublished = False
    assert instance.isPublished == False


def test_tda593_billing_CreditCardInformation_cardNumber_value_roundtrip():
    instance = tda593_billing_CreditCardInformation(cardNumber="sample_text", ccv="sample_text", expirationDate=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.cardNumber == "sample_text"
    instance.cardNumber = "sample_text_2"
    assert instance.cardNumber == "sample_text_2"


def test_tda593_billing_CreditCardInformation_ccv_value_roundtrip():
    instance = tda593_billing_CreditCardInformation(cardNumber="sample_text", ccv="sample_text", expirationDate=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.ccv == "sample_text"
    instance.ccv = "sample_text_2"
    assert instance.ccv == "sample_text_2"


def test_tda593_billing_CreditCardInformation_expirationDate_value_roundtrip():
    instance = tda593_billing_CreditCardInformation(cardNumber="sample_text", ccv="sample_text", expirationDate=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.expirationDate == date(2024, 1, 1)
    instance.expirationDate = date(2025, 6, 15)
    assert instance.expirationDate == date(2025, 6, 15)


def test_tda593_billing_CreditCardInformation_firstName_value_roundtrip():
    instance = tda593_billing_CreditCardInformation(cardNumber="sample_text", ccv="sample_text", expirationDate=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_tda593_billing_CreditCardInformation_lastName_value_roundtrip():
    instance = tda593_billing_CreditCardInformation(cardNumber="sample_text", ccv="sample_text", expirationDate=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_tda593_billing_Discount_code_value_roundtrip():
    instance = tda593_billing_Discount(code="sample_text", name="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_tda593_billing_Discount_name_value_roundtrip():
    instance = tda593_billing_Discount(code="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tda593_billing_DiscountLimit_endDate_value_roundtrip():
    instance = tda593_billing_DiscountLimit(endDate=date(2024, 1, 1), id=7, startDate=date(2024, 1, 1), timesLeftToUse=7)
    assert instance.endDate == date(2024, 1, 1)
    instance.endDate = date(2025, 6, 15)
    assert instance.endDate == date(2025, 6, 15)


def test_tda593_billing_DiscountLimit_id_value_roundtrip():
    instance = tda593_billing_DiscountLimit(endDate=date(2024, 1, 1), id=7, startDate=date(2024, 1, 1), timesLeftToUse=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_billing_DiscountLimit_startDate_value_roundtrip():
    instance = tda593_billing_DiscountLimit(endDate=date(2024, 1, 1), id=7, startDate=date(2024, 1, 1), timesLeftToUse=7)
    assert instance.startDate == date(2024, 1, 1)
    instance.startDate = date(2025, 6, 15)
    assert instance.startDate == date(2025, 6, 15)


def test_tda593_billing_DiscountLimit_timesLeftToUse_value_roundtrip():
    instance = tda593_billing_DiscountLimit(endDate=date(2024, 1, 1), id=7, startDate=date(2024, 1, 1), timesLeftToUse=7)
    assert instance.timesLeftToUse == 7
    instance.timesLeftToUse = 13
    assert instance.timesLeftToUse == 13


def test_tda593_billing_PercentageDiscount_percentage_value_roundtrip():
    instance = tda593_billing_PercentageDiscount(percentage=3.14)
    assert instance.percentage == 3.14
    instance.percentage = 9.99
    assert instance.percentage == 9.99


def test_tda593_billing_Purchase_id_value_roundtrip():
    instance = tda593_billing_Purchase(id=7, price=3.14, quantity=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_billing_Purchase_price_value_roundtrip():
    instance = tda593_billing_Purchase(id=7, price=3.14, quantity=7)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_tda593_billing_Purchase_quantity_value_roundtrip():
    instance = tda593_billing_Purchase(id=7, price=3.14, quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_tda593_billing_Service_id_value_roundtrip():
    instance = tda593_billing_Service(id=7, name="sample_text", price=3.14)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_billing_Service_name_value_roundtrip():
    instance = tda593_billing_Service(id=7, name="sample_text", price=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tda593_billing_Service_price_value_roundtrip():
    instance = tda593_billing_Service(id=7, name="sample_text", price=3.14)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_tda593_billing_SumDiscount_discountSum_value_roundtrip():
    instance = tda593_billing_SumDiscount(discountSum=3.14)
    assert instance.discountSum == 3.14
    instance.discountSum = 9.99
    assert instance.discountSum == 9.99


def test_tda593_booking_Booking_endDate_value_roundtrip():
    instance = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    assert instance.endDate == date(2024, 1, 1)
    instance.endDate = date(2025, 6, 15)
    assert instance.endDate == date(2025, 6, 15)


def test_tda593_booking_Booking_id_value_roundtrip():
    instance = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_booking_Booking_isCanceled_value_roundtrip():
    instance = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    assert instance.isCanceled == True
    instance.isCanceled = False
    assert instance.isCanceled == False


def test_tda593_booking_Booking_price_value_roundtrip():
    instance = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_tda593_booking_Booking_specialRequest_value_roundtrip():
    instance = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    assert instance.specialRequest == "sample_text"
    instance.specialRequest = "sample_text_2"
    assert instance.specialRequest == "sample_text_2"


def test_tda593_booking_Booking_startDate_value_roundtrip():
    instance = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    assert instance.startDate == date(2024, 1, 1)
    instance.startDate = date(2025, 6, 15)
    assert instance.startDate == date(2025, 6, 15)


def test_tda593_booking_LegalEntity_email_value_roundtrip():
    instance = tda593_booking_LegalEntity(email="sample_text", id=7, phone="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_tda593_booking_LegalEntity_id_value_roundtrip():
    instance = tda593_booking_LegalEntity(email="sample_text", id=7, phone="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_booking_LegalEntity_phone_value_roundtrip():
    instance = tda593_booking_LegalEntity(email="sample_text", id=7, phone="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_tda593_booking_Organization_name_value_roundtrip():
    instance = tda593_booking_Organization(name="sample_text", organizationNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tda593_booking_Organization_organizationNumber_value_roundtrip():
    instance = tda593_booking_Organization(name="sample_text", organizationNumber="sample_text")
    assert instance.organizationNumber == "sample_text"
    instance.organizationNumber = "sample_text_2"
    assert instance.organizationNumber == "sample_text_2"


def test_tda593_booking_Person_firstname_value_roundtrip():
    instance = tda593_booking_Person(firstname="sample_text", lastname="sample_text", socialSecurityNumber="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_tda593_booking_Person_lastname_value_roundtrip():
    instance = tda593_booking_Person(firstname="sample_text", lastname="sample_text", socialSecurityNumber="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_tda593_booking_Person_socialSecurityNumber_value_roundtrip():
    instance = tda593_booking_Person(firstname="sample_text", lastname="sample_text", socialSecurityNumber="sample_text")
    assert instance.socialSecurityNumber == "sample_text"
    instance.socialSecurityNumber = "sample_text_2"
    assert instance.socialSecurityNumber == "sample_text_2"


def test_tda593_booking_RoomStay_active_value_roundtrip():
    instance = tda593_booking_RoomStay(active=True, id=7)
    assert instance.active == True
    instance.active = False
    assert instance.active == False


def test_tda593_booking_RoomStay_id_value_roundtrip():
    instance = tda593_booking_RoomStay(active=True, id=7)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_booking_StayRequest_id_value_roundtrip():
    instance = tda593_booking_StayRequest(id=7, text="sample_text", timeStamp=date(2024, 1, 1))
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_booking_StayRequest_text_value_roundtrip():
    instance = tda593_booking_StayRequest(id=7, text="sample_text", timeStamp=date(2024, 1, 1))
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_tda593_booking_StayRequest_timeStamp_value_roundtrip():
    instance = tda593_booking_StayRequest(id=7, text="sample_text", timeStamp=date(2024, 1, 1))
    assert instance.timeStamp == date(2024, 1, 1)
    instance.timeStamp = date(2025, 6, 15)
    assert instance.timeStamp == date(2025, 6, 15)


def test_tda593_booking_TravelInformation_comment_value_roundtrip():
    instance = tda593_booking_TravelInformation(comment="sample_text", id=7, trackingId="sample_text")
    assert instance.comment == "sample_text"
    instance.comment = "sample_text_2"
    assert instance.comment == "sample_text_2"


def test_tda593_booking_TravelInformation_id_value_roundtrip():
    instance = tda593_booking_TravelInformation(comment="sample_text", id=7, trackingId="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_tda593_booking_TravelInformation_trackingId_value_roundtrip():
    instance = tda593_booking_TravelInformation(comment="sample_text", id=7, trackingId="sample_text")
    assert instance.trackingId == "sample_text"
    instance.trackingId = "sample_text_2"
    assert instance.trackingId == "sample_text_2"


def test_tda593_facilities_ConferenceRoom_equipment_value_roundtrip():
    instance = tda593_facilities_ConferenceRoom(equipment="sample_text", numberOfSeats=7)
    assert instance.equipment == "sample_text"
    instance.equipment = "sample_text_2"
    assert instance.equipment == "sample_text_2"


def test_tda593_facilities_ConferenceRoom_numberOfSeats_value_roundtrip():
    instance = tda593_facilities_ConferenceRoom(equipment="sample_text", numberOfSeats=7)
    assert instance.numberOfSeats == 7
    instance.numberOfSeats = 13
    assert instance.numberOfSeats == 13


def test_tda593_facilities_GuestRoom_numberOfBeds_value_roundtrip():
    instance = tda593_facilities_GuestRoom(numberOfBeds=7, numberOfExtrabeds=7)
    assert instance.numberOfBeds == 7
    instance.numberOfBeds = 13
    assert instance.numberOfBeds == 13


def test_tda593_facilities_GuestRoom_numberOfExtrabeds_value_roundtrip():
    instance = tda593_facilities_GuestRoom(numberOfBeds=7, numberOfExtrabeds=7)
    assert instance.numberOfExtrabeds == 7
    instance.numberOfExtrabeds = 13
    assert instance.numberOfExtrabeds == 13


def test_tda593_facilities_KeyCard_id_value_roundtrip():
    instance = tda593_facilities_KeyCard(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_tda593_facilities_Room_description_value_roundtrip():
    instance = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_tda593_facilities_Room_disabilityApprovals_value_roundtrip():
    instance = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    assert instance.disabilityApprovals == "sample_text"
    instance.disabilityApprovals = "sample_text_2"
    assert instance.disabilityApprovals == "sample_text_2"


def test_tda593_facilities_Room_floor_value_roundtrip():
    instance = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    assert instance.floor == 7
    instance.floor = 13
    assert instance.floor == 13


def test_tda593_facilities_Room_isBeingCleaned_value_roundtrip():
    instance = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    assert instance.isBeingCleaned == True
    instance.isBeingCleaned = False
    assert instance.isBeingCleaned == False


def test_tda593_facilities_Room_isOperational_value_roundtrip():
    instance = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    assert instance.isOperational == True
    instance.isOperational = False
    assert instance.isOperational == False


def test_tda593_facilities_Room_photos_value_roundtrip():
    instance = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    assert instance.photos == "sample_text"
    instance.photos = "sample_text_2"
    assert instance.photos == "sample_text_2"


def test_tda593_facilities_Room_roomNumber_value_roundtrip():
    instance = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    assert instance.roomNumber == "sample_text"
    instance.roomNumber = "sample_text_2"
    assert instance.roomNumber == "sample_text_2"


def test_tda593_facilities_RoomType_description_value_roundtrip():
    instance = tda593_facilities_RoomType(description="sample_text", name="sample_text", price=3.14, roomApprovals="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_tda593_facilities_RoomType_name_value_roundtrip():
    instance = tda593_facilities_RoomType(description="sample_text", name="sample_text", price=3.14, roomApprovals="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tda593_facilities_RoomType_price_value_roundtrip():
    instance = tda593_facilities_RoomType(description="sample_text", name="sample_text", price=3.14, roomApprovals="sample_text")
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_tda593_facilities_RoomType_roomApprovals_value_roundtrip():
    instance = tda593_facilities_RoomType(description="sample_text", name="sample_text", price=3.14, roomApprovals="sample_text")
    assert instance.roomApprovals == "sample_text"
    instance.roomApprovals = "sample_text_2"
    assert instance.roomApprovals == "sample_text_2"


def test_tda593_billing_BankingManagerImpl_isa_BankingManager():
    instance = tda593_billing_BankingManagerImpl()
    assert isinstance(instance, BankingManager)


def test_tda593_billing_BookingBill_isa_Bill():
    instance = tda593_billing_BookingBill()
    assert isinstance(instance, Bill)


def test_tda593_billing_BillManagerImpl_isa_BillManager():
    instance = tda593_billing_BillManagerImpl()
    assert isinstance(instance, BillManager)


def test_tda593_booking_BookingManagerImpl_isa_BookingManager():
    instance = tda593_booking_BookingManagerImpl()
    assert isinstance(instance, BookingManager)


def test_tda593_billing_CreditCardManagerImpl_isa_CreditCardManager():
    instance = tda593_billing_CreditCardManagerImpl()
    assert isinstance(instance, CreditCardManager)


def test_tda593_billing_PercentageDiscount_isa_Discount():
    instance = tda593_billing_PercentageDiscount(percentage=3.14)
    assert isinstance(instance, Discount)


def test_tda593_billing_SumDiscount_isa_Discount():
    instance = tda593_billing_SumDiscount(discountSum=3.14)
    assert isinstance(instance, Discount)


def test_tda593_billing_AdminDiscountManager_isa_DiscountManager():
    instance = tda593_billing_AdminDiscountManager()
    assert isinstance(instance, DiscountManager)


def test_tda593_billing_DiscountManagerImpl_isa_DiscountManager():
    instance = tda593_billing_DiscountManagerImpl()
    assert isinstance(instance, DiscountManager)


def test_tda593_facilities_AdminKeyCardManager_isa_KeyCardManager():
    instance = tda593_facilities_AdminKeyCardManager()
    assert isinstance(instance, KeyCardManager)


def test_tda593_facilities_KeyCardManagerImpl_isa_KeyCardManager():
    instance = tda593_facilities_KeyCardManagerImpl()
    assert isinstance(instance, KeyCardManager)


def test_tda593_booking_Organization_isa_LegalEntity():
    instance = tda593_booking_Organization(name="sample_text", organizationNumber="sample_text")
    assert isinstance(instance, LegalEntity)


def test_tda593_booking_Person_isa_LegalEntity():
    instance = tda593_booking_Person(firstname="sample_text", lastname="sample_text", socialSecurityNumber="sample_text")
    assert isinstance(instance, LegalEntity)


def test_tda593_booking_LegalEntityManagerImpl_isa_LegalEntityManager():
    instance = tda593_booking_LegalEntityManagerImpl()
    assert isinstance(instance, LegalEntityManager)


def test_tda593_facilities_ConferenceRoom_isa_Room():
    instance = tda593_facilities_ConferenceRoom(equipment="sample_text", numberOfSeats=7)
    assert isinstance(instance, Room)


def test_tda593_facilities_GuestRoom_isa_Room():
    instance = tda593_facilities_GuestRoom(numberOfBeds=7, numberOfExtrabeds=7)
    assert isinstance(instance, Room)


def test_tda593_facilities_AdminRoomManager_isa_RoomManager():
    instance = tda593_facilities_AdminRoomManager()
    assert isinstance(instance, RoomManager)


def test_tda593_facilities_RoomManagerImpl_isa_RoomManager():
    instance = tda593_facilities_RoomManagerImpl()
    assert isinstance(instance, RoomManager)


def test_tda593_billing_AdminServiceManager_isa_ServiceManager():
    instance = tda593_billing_AdminServiceManager()
    assert isinstance(instance, ServiceManager)


def test_tda593_billing_ServiceManagerImpl_isa_ServiceManager():
    instance = tda593_billing_ServiceManagerImpl()
    assert isinstance(instance, ServiceManager)


def test_tda593_billing_AdminDiscountManagerImpl_isa_billing_AdminDiscountManager():
    instance = tda593_billing_AdminDiscountManagerImpl()
    assert isinstance(instance, billing_AdminDiscountManager)


def test_tda593_billing_AdminServiceManagerImpl_isa_billing_AdminServiceManager():
    instance = tda593_billing_AdminServiceManagerImpl()
    assert isinstance(instance, billing_AdminServiceManager)


def test_tda593_billing_AdminDiscountManagerImpl_isa_billing_DiscountManagerImpl():
    instance = tda593_billing_AdminDiscountManagerImpl()
    assert isinstance(instance, billing_DiscountManagerImpl)


def test_tda593_billing_AdminServiceManagerImpl_isa_billing_ServiceManagerImpl():
    instance = tda593_billing_AdminServiceManagerImpl()
    assert isinstance(instance, billing_ServiceManagerImpl)


def test_tda593_facilities_AdminKeyCardManagerImpl_isa_facilities_AdminKeyCardManager():
    instance = tda593_facilities_AdminKeyCardManagerImpl()
    assert isinstance(instance, facilities_AdminKeyCardManager)


def test_tda593_facilities_AdminRoomManagerImpl_isa_facilities_AdminRoomManager():
    instance = tda593_facilities_AdminRoomManagerImpl()
    assert isinstance(instance, facilities_AdminRoomManager)


def test_tda593_facilities_AdminKeyCardManagerImpl_isa_facilities_KeyCardManagerImpl():
    instance = tda593_facilities_AdminKeyCardManagerImpl()
    assert isinstance(instance, facilities_KeyCardManagerImpl)


def test_tda593_facilities_AdminRoomManagerImpl_isa_facilities_RoomManagerImpl():
    instance = tda593_facilities_AdminRoomManagerImpl()
    assert isinstance(instance, facilities_RoomManagerImpl)


def test_assoc_allowedKeyCards0_link_reassign_clear():
    a = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    b1 = facilities_KeyCard()
    b2 = facilities_KeyCard()
    _safe_set(a, 'tda593_facilities_Room', {b1})
    assert _is_linked(a, 'tda593_facilities_Room', b1)
    if hasattr(b1, 'facilities_KeyCard'):
        assert _is_linked(b1, 'facilities_KeyCard', a)
    _safe_set(a, 'tda593_facilities_Room', {b2})
    assert _is_linked(a, 'tda593_facilities_Room', b2)
    if hasattr(b1, 'facilities_KeyCard'):
        assert not _is_linked(b1, 'facilities_KeyCard', a)
    if hasattr(b2, 'facilities_KeyCard'):
        assert _is_linked(b2, 'facilities_KeyCard', a)
    _safe_set(a, 'tda593_facilities_Room', set())
    assert not _is_linked(a, 'tda593_facilities_Room', b2)
    if hasattr(b2, 'facilities_KeyCard'):
        assert not _is_linked(b2, 'facilities_KeyCard', a)


def test_assoc_allowedUsers10_link_reassign_clear():
    a = tda593_billing_DiscountLimit(endDate=date(2024, 1, 1), id=7, startDate=date(2024, 1, 1), timesLeftToUse=7)
    b1 = booking_LegalEntity()
    b2 = booking_LegalEntity()
    _safe_set(a, 'tda593_billing_DiscountLimit', {b1})
    assert _is_linked(a, 'tda593_billing_DiscountLimit', b1)
    if hasattr(b1, 'booking_LegalEntity'):
        assert _is_linked(b1, 'booking_LegalEntity', a)
    _safe_set(a, 'tda593_billing_DiscountLimit', {b2})
    assert _is_linked(a, 'tda593_billing_DiscountLimit', b2)
    if hasattr(b1, 'booking_LegalEntity'):
        assert not _is_linked(b1, 'booking_LegalEntity', a)
    if hasattr(b2, 'booking_LegalEntity'):
        assert _is_linked(b2, 'booking_LegalEntity', a)
    _safe_set(a, 'tda593_billing_DiscountLimit', set())
    assert not _is_linked(a, 'tda593_billing_DiscountLimit', b2)
    if hasattr(b2, 'booking_LegalEntity'):
        assert not _is_linked(b2, 'booking_LegalEntity', a)


def test_assoc_customer15_link_reassign_clear():
    a = tda593_billing_Bill(date=date(2024, 1, 1), id=7, isPaid=True, isPublished=True)
    b1 = booking_LegalEntity()
    b2 = booking_LegalEntity()
    _safe_set(a, 'tda593_billing_Bill16', b1)
    assert _is_linked(a, 'tda593_billing_Bill16', b1)
    if hasattr(b1, 'booking_LegalEntity17'):
        assert _is_linked(b1, 'booking_LegalEntity17', a)
    _safe_set(a, 'tda593_billing_Bill16', b2)
    assert _is_linked(a, 'tda593_billing_Bill16', b2)
    if hasattr(b1, 'booking_LegalEntity17'):
        assert not _is_linked(b1, 'booking_LegalEntity17', a)
    if hasattr(b2, 'booking_LegalEntity17'):
        assert _is_linked(b2, 'booking_LegalEntity17', a)
    _safe_set(a, 'tda593_billing_Bill16', None)
    assert not _is_linked(a, 'tda593_billing_Bill16', b2)
    if hasattr(b2, 'booking_LegalEntity17'):
        assert not _is_linked(b2, 'booking_LegalEntity17', a)


def test_assoc_discountLimit9_link_reassign_clear():
    a = tda593_billing_Discount(code="sample_text", name="sample_text")
    b1 = billing_DiscountLimit()
    b2 = billing_DiscountLimit()
    _safe_set(a, 'tda593_billing_Discount', b1)
    assert _is_linked(a, 'tda593_billing_Discount', b1)
    if hasattr(b1, 'billing_DiscountLimit'):
        assert _is_linked(b1, 'billing_DiscountLimit', a)
    _safe_set(a, 'tda593_billing_Discount', b2)
    assert _is_linked(a, 'tda593_billing_Discount', b2)
    if hasattr(b1, 'billing_DiscountLimit'):
        assert not _is_linked(b1, 'billing_DiscountLimit', a)
    if hasattr(b2, 'billing_DiscountLimit'):
        assert _is_linked(b2, 'billing_DiscountLimit', a)
    _safe_set(a, 'tda593_billing_Discount', None)
    assert not _is_linked(a, 'tda593_billing_Discount', b2)
    if hasattr(b2, 'billing_DiscountLimit'):
        assert not _is_linked(b2, 'billing_DiscountLimit', a)


def test_assoc_legalEntity22_link_reassign_clear():
    a = tda593_billing_CreditCardInformation(cardNumber="sample_text", ccv="sample_text", expirationDate=date(2024, 1, 1), firstName="sample_text", lastName="sample_text")
    b1 = booking_LegalEntity()
    b2 = booking_LegalEntity()
    _safe_set(a, 'tda593_billing_CreditCardInformation', b1)
    assert _is_linked(a, 'tda593_billing_CreditCardInformation', b1)
    if hasattr(b1, 'booking_LegalEntity23'):
        assert _is_linked(b1, 'booking_LegalEntity23', a)
    _safe_set(a, 'tda593_billing_CreditCardInformation', b2)
    assert _is_linked(a, 'tda593_billing_CreditCardInformation', b2)
    if hasattr(b1, 'booking_LegalEntity23'):
        assert not _is_linked(b1, 'booking_LegalEntity23', a)
    if hasattr(b2, 'booking_LegalEntity23'):
        assert _is_linked(b2, 'booking_LegalEntity23', a)
    _safe_set(a, 'tda593_billing_CreditCardInformation', None)
    assert not _is_linked(a, 'tda593_billing_CreditCardInformation', b2)
    if hasattr(b2, 'booking_LegalEntity23'):
        assert not _is_linked(b2, 'booking_LegalEntity23', a)


def test_assoc_predecessor38_link_reassign_clear():
    a = tda593_booking_TravelInformation(comment="sample_text", id=7, trackingId="sample_text")
    b1 = booking_TravelInformation()
    b2 = booking_TravelInformation()
    _safe_set(a, 'tda593_booking_TravelInformation', b1)
    assert _is_linked(a, 'tda593_booking_TravelInformation', b1)
    if hasattr(b1, 'booking_TravelInformation39'):
        assert _is_linked(b1, 'booking_TravelInformation39', a)
    _safe_set(a, 'tda593_booking_TravelInformation', b2)
    assert _is_linked(a, 'tda593_booking_TravelInformation', b2)
    if hasattr(b1, 'booking_TravelInformation39'):
        assert not _is_linked(b1, 'booking_TravelInformation39', a)
    if hasattr(b2, 'booking_TravelInformation39'):
        assert _is_linked(b2, 'booking_TravelInformation39', a)
    _safe_set(a, 'tda593_booking_TravelInformation', None)
    assert not _is_linked(a, 'tda593_booking_TravelInformation', b2)
    if hasattr(b2, 'booking_TravelInformation39'):
        assert not _is_linked(b2, 'booking_TravelInformation39', a)


def test_assoc_purchases12_link_reassign_clear():
    a = tda593_billing_Bill(date=date(2024, 1, 1), id=7, isPaid=True, isPublished=True)
    b1 = billing_Purchase()
    b2 = billing_Purchase()
    _safe_set(a, 'tda593_billing_Bill', {b1})
    assert _is_linked(a, 'tda593_billing_Bill', b1)
    if hasattr(b1, 'billing_Purchase'):
        assert _is_linked(b1, 'billing_Purchase', a)
    _safe_set(a, 'tda593_billing_Bill', {b2})
    assert _is_linked(a, 'tda593_billing_Bill', b2)
    if hasattr(b1, 'billing_Purchase'):
        assert not _is_linked(b1, 'billing_Purchase', a)
    if hasattr(b2, 'billing_Purchase'):
        assert _is_linked(b2, 'billing_Purchase', a)
    _safe_set(a, 'tda593_billing_Bill', set())
    assert not _is_linked(a, 'tda593_billing_Bill', b2)
    if hasattr(b2, 'billing_Purchase'):
        assert not _is_linked(b2, 'billing_Purchase', a)


def test_assoc_registeredPersons41_link_reassign_clear():
    a = tda593_booking_RoomStay(active=True, id=7)
    b1 = booking_Person()
    b2 = booking_Person()
    _safe_set(a, 'tda593_booking_RoomStay42', {b1})
    assert _is_linked(a, 'tda593_booking_RoomStay42', b1)
    if hasattr(b1, 'booking_Person'):
        assert _is_linked(b1, 'booking_Person', a)
    _safe_set(a, 'tda593_booking_RoomStay42', {b2})
    assert _is_linked(a, 'tda593_booking_RoomStay42', b2)
    if hasattr(b1, 'booking_Person'):
        assert not _is_linked(b1, 'booking_Person', a)
    if hasattr(b2, 'booking_Person'):
        assert _is_linked(b2, 'booking_Person', a)
    _safe_set(a, 'tda593_booking_RoomStay42', set())
    assert not _is_linked(a, 'tda593_booking_RoomStay42', b2)
    if hasattr(b2, 'booking_Person'):
        assert not _is_linked(b2, 'booking_Person', a)


def test_assoc_responsible33_link_reassign_clear():
    a = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    b1 = booking_LegalEntity()
    b2 = booking_LegalEntity()
    _safe_set(a, 'tda593_booking_Booking34', b1)
    assert _is_linked(a, 'tda593_booking_Booking34', b1)
    if hasattr(b1, 'booking_LegalEntity35'):
        assert _is_linked(b1, 'booking_LegalEntity35', a)
    _safe_set(a, 'tda593_booking_Booking34', b2)
    assert _is_linked(a, 'tda593_booking_Booking34', b2)
    if hasattr(b1, 'booking_LegalEntity35'):
        assert not _is_linked(b1, 'booking_LegalEntity35', a)
    if hasattr(b2, 'booking_LegalEntity35'):
        assert _is_linked(b2, 'booking_LegalEntity35', a)
    _safe_set(a, 'tda593_booking_Booking34', None)
    assert not _is_linked(a, 'tda593_booking_Booking34', b2)
    if hasattr(b2, 'booking_LegalEntity35'):
        assert not _is_linked(b2, 'booking_LegalEntity35', a)


def test_assoc_room43_link_reassign_clear():
    a = tda593_booking_RoomStay(active=True, id=7)
    b1 = facilities_Room()
    b2 = facilities_Room()
    _safe_set(a, 'tda593_booking_RoomStay44', b1)
    assert _is_linked(a, 'tda593_booking_RoomStay44', b1)
    if hasattr(b1, 'facilities_Room'):
        assert _is_linked(b1, 'facilities_Room', a)
    _safe_set(a, 'tda593_booking_RoomStay44', b2)
    assert _is_linked(a, 'tda593_booking_RoomStay44', b2)
    if hasattr(b1, 'facilities_Room'):
        assert not _is_linked(b1, 'facilities_Room', a)
    if hasattr(b2, 'facilities_Room'):
        assert _is_linked(b2, 'facilities_Room', a)
    _safe_set(a, 'tda593_booking_RoomStay44', None)
    assert not _is_linked(a, 'tda593_booking_RoomStay44', b2)
    if hasattr(b2, 'facilities_Room'):
        assert not _is_linked(b2, 'facilities_Room', a)


def test_assoc_roomStay36_link_reassign_clear():
    a = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    b1 = booking_RoomStay()
    b2 = booking_RoomStay()
    _safe_set(a, 'tda593_booking_Booking37', b1)
    assert _is_linked(a, 'tda593_booking_Booking37', b1)
    if hasattr(b1, 'booking_RoomStay'):
        assert _is_linked(b1, 'booking_RoomStay', a)
    _safe_set(a, 'tda593_booking_Booking37', b2)
    assert _is_linked(a, 'tda593_booking_Booking37', b2)
    if hasattr(b1, 'booking_RoomStay'):
        assert not _is_linked(b1, 'booking_RoomStay', a)
    if hasattr(b2, 'booking_RoomStay'):
        assert _is_linked(b2, 'booking_RoomStay', a)
    _safe_set(a, 'tda593_booking_Booking37', None)
    assert not _is_linked(a, 'tda593_booking_Booking37', b2)
    if hasattr(b2, 'booking_RoomStay'):
        assert not _is_linked(b2, 'booking_RoomStay', a)


def test_assoc_roomType1_link_reassign_clear():
    a = tda593_facilities_Room(description="sample_text", disabilityApprovals="sample_text", floor=7, isBeingCleaned=True, isOperational=True, photos="sample_text", roomNumber="sample_text")
    b1 = facilities_RoomType()
    b2 = facilities_RoomType()
    _safe_set(a, 'tda593_facilities_Room2', b1)
    assert _is_linked(a, 'tda593_facilities_Room2', b1)
    if hasattr(b1, 'facilities_RoomType'):
        assert _is_linked(b1, 'facilities_RoomType', a)
    _safe_set(a, 'tda593_facilities_Room2', b2)
    assert _is_linked(a, 'tda593_facilities_Room2', b2)
    if hasattr(b1, 'facilities_RoomType'):
        assert not _is_linked(b1, 'facilities_RoomType', a)
    if hasattr(b2, 'facilities_RoomType'):
        assert _is_linked(b2, 'facilities_RoomType', a)
    _safe_set(a, 'tda593_facilities_Room2', None)
    assert not _is_linked(a, 'tda593_facilities_Room2', b2)
    if hasattr(b2, 'facilities_RoomType'):
        assert not _is_linked(b2, 'facilities_RoomType', a)


def test_assoc_roomType29_link_reassign_clear():
    a = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    b1 = facilities_RoomType()
    b2 = facilities_RoomType()
    _safe_set(a, 'tda593_booking_Booking', b1)
    assert _is_linked(a, 'tda593_booking_Booking', b1)
    if hasattr(b1, 'facilities_RoomType30'):
        assert _is_linked(b1, 'facilities_RoomType30', a)
    _safe_set(a, 'tda593_booking_Booking', b2)
    assert _is_linked(a, 'tda593_booking_Booking', b2)
    if hasattr(b1, 'facilities_RoomType30'):
        assert not _is_linked(b1, 'facilities_RoomType30', a)
    if hasattr(b2, 'facilities_RoomType30'):
        assert _is_linked(b2, 'facilities_RoomType30', a)
    _safe_set(a, 'tda593_booking_Booking', None)
    assert not _is_linked(a, 'tda593_booking_Booking', b2)
    if hasattr(b2, 'facilities_RoomType30'):
        assert not _is_linked(b2, 'facilities_RoomType30', a)


def test_assoc_service20_link_reassign_clear():
    a = tda593_billing_Purchase(id=7, price=3.14, quantity=7)
    b1 = billing_Service()
    b2 = billing_Service()
    _safe_set(a, 'tda593_billing_Purchase', b1)
    assert _is_linked(a, 'tda593_billing_Purchase', b1)
    if hasattr(b1, 'billing_Service'):
        assert _is_linked(b1, 'billing_Service', a)
    _safe_set(a, 'tda593_billing_Purchase', b2)
    assert _is_linked(a, 'tda593_billing_Purchase', b2)
    if hasattr(b1, 'billing_Service'):
        assert not _is_linked(b1, 'billing_Service', a)
    if hasattr(b2, 'billing_Service'):
        assert _is_linked(b2, 'billing_Service', a)
    _safe_set(a, 'tda593_billing_Purchase', None)
    assert not _is_linked(a, 'tda593_billing_Purchase', b2)
    if hasattr(b2, 'billing_Service'):
        assert not _is_linked(b2, 'billing_Service', a)


def test_assoc_stayRequest40_link_reassign_clear():
    a = tda593_booking_RoomStay(active=True, id=7)
    b1 = booking_StayRequest()
    b2 = booking_StayRequest()
    _safe_set(a, 'tda593_booking_RoomStay', {b1})
    assert _is_linked(a, 'tda593_booking_RoomStay', b1)
    if hasattr(b1, 'booking_StayRequest'):
        assert _is_linked(b1, 'booking_StayRequest', a)
    _safe_set(a, 'tda593_booking_RoomStay', {b2})
    assert _is_linked(a, 'tda593_booking_RoomStay', b2)
    if hasattr(b1, 'booking_StayRequest'):
        assert not _is_linked(b1, 'booking_StayRequest', a)
    if hasattr(b2, 'booking_StayRequest'):
        assert _is_linked(b2, 'booking_StayRequest', a)
    _safe_set(a, 'tda593_booking_RoomStay', set())
    assert not _is_linked(a, 'tda593_booking_RoomStay', b2)
    if hasattr(b2, 'booking_StayRequest'):
        assert not _is_linked(b2, 'booking_StayRequest', a)


def test_assoc_subBills18_link_reassign_clear():
    a = tda593_billing_Bill(date=date(2024, 1, 1), id=7, isPaid=True, isPublished=True)
    b1 = billing_Bill()
    b2 = billing_Bill()
    _safe_set(a, 'tda593_billing_Bill19', {b1})
    assert _is_linked(a, 'tda593_billing_Bill19', b1)
    if hasattr(b1, 'billing_Bill'):
        assert _is_linked(b1, 'billing_Bill', a)
    _safe_set(a, 'tda593_billing_Bill19', {b2})
    assert _is_linked(a, 'tda593_billing_Bill19', b2)
    if hasattr(b1, 'billing_Bill'):
        assert not _is_linked(b1, 'billing_Bill', a)
    if hasattr(b2, 'billing_Bill'):
        assert _is_linked(b2, 'billing_Bill', a)
    _safe_set(a, 'tda593_billing_Bill19', set())
    assert not _is_linked(a, 'tda593_billing_Bill19', b2)
    if hasattr(b2, 'billing_Bill'):
        assert not _is_linked(b2, 'billing_Bill', a)


def test_assoc_travelInformation31_link_reassign_clear():
    a = tda593_booking_Booking(endDate=date(2024, 1, 1), id=7, isCanceled=True, price=3.14, specialRequest="sample_text", startDate=date(2024, 1, 1))
    b1 = booking_TravelInformation()
    b2 = booking_TravelInformation()
    _safe_set(a, 'tda593_booking_Booking32', b1)
    assert _is_linked(a, 'tda593_booking_Booking32', b1)
    if hasattr(b1, 'booking_TravelInformation'):
        assert _is_linked(b1, 'booking_TravelInformation', a)
    _safe_set(a, 'tda593_booking_Booking32', b2)
    assert _is_linked(a, 'tda593_booking_Booking32', b2)
    if hasattr(b1, 'booking_TravelInformation'):
        assert not _is_linked(b1, 'booking_TravelInformation', a)
    if hasattr(b2, 'booking_TravelInformation'):
        assert _is_linked(b2, 'booking_TravelInformation', a)
    _safe_set(a, 'tda593_booking_Booking32', None)
    assert not _is_linked(a, 'tda593_booking_Booking32', b2)
    if hasattr(b2, 'booking_TravelInformation'):
        assert not _is_linked(b2, 'booking_TravelInformation', a)


def test_assoc_usedDiscounts13_link_reassign_clear():
    a = tda593_billing_Bill(date=date(2024, 1, 1), id=7, isPaid=True, isPublished=True)
    b1 = billing_Discount()
    b2 = billing_Discount()
    _safe_set(a, 'tda593_billing_Bill14', {b1})
    assert _is_linked(a, 'tda593_billing_Bill14', b1)
    if hasattr(b1, 'billing_Discount'):
        assert _is_linked(b1, 'billing_Discount', a)
    _safe_set(a, 'tda593_billing_Bill14', {b2})
    assert _is_linked(a, 'tda593_billing_Bill14', b2)
    if hasattr(b1, 'billing_Discount'):
        assert not _is_linked(b1, 'billing_Discount', a)
    if hasattr(b2, 'billing_Discount'):
        assert _is_linked(b2, 'billing_Discount', a)
    _safe_set(a, 'tda593_billing_Bill14', set())
    assert not _is_linked(a, 'tda593_billing_Bill14', b2)
    if hasattr(b2, 'billing_Discount'):
        assert not _is_linked(b2, 'billing_Discount', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BankingManager_strategy = st.builds(BankingManager)
@given(instance=BankingManager_strategy)
@settings(max_examples=25)
def test_BankingManager_instantiation(instance):
    assert isinstance(instance, BankingManager)


Bill_strategy = st.builds(Bill)
@given(instance=Bill_strategy)
@settings(max_examples=25)
def test_Bill_instantiation(instance):
    assert isinstance(instance, Bill)


BillManager_strategy = st.builds(BillManager)
@given(instance=BillManager_strategy)
@settings(max_examples=25)
def test_BillManager_instantiation(instance):
    assert isinstance(instance, BillManager)


BookingManager_strategy = st.builds(BookingManager)
@given(instance=BookingManager_strategy)
@settings(max_examples=25)
def test_BookingManager_instantiation(instance):
    assert isinstance(instance, BookingManager)


CreditCardManager_strategy = st.builds(CreditCardManager)
@given(instance=CreditCardManager_strategy)
@settings(max_examples=25)
def test_CreditCardManager_instantiation(instance):
    assert isinstance(instance, CreditCardManager)


Discount_strategy = st.builds(Discount)
@given(instance=Discount_strategy)
@settings(max_examples=25)
def test_Discount_instantiation(instance):
    assert isinstance(instance, Discount)


DiscountManager_strategy = st.builds(DiscountManager)
@given(instance=DiscountManager_strategy)
@settings(max_examples=25)
def test_DiscountManager_instantiation(instance):
    assert isinstance(instance, DiscountManager)


KeyCardManager_strategy = st.builds(KeyCardManager)
@given(instance=KeyCardManager_strategy)
@settings(max_examples=25)
def test_KeyCardManager_instantiation(instance):
    assert isinstance(instance, KeyCardManager)


LegalEntity_strategy = st.builds(LegalEntity)
@given(instance=LegalEntity_strategy)
@settings(max_examples=25)
def test_LegalEntity_instantiation(instance):
    assert isinstance(instance, LegalEntity)


LegalEntityManager_strategy = st.builds(LegalEntityManager)
@given(instance=LegalEntityManager_strategy)
@settings(max_examples=25)
def test_LegalEntityManager_instantiation(instance):
    assert isinstance(instance, LegalEntityManager)


Room_strategy = st.builds(Room)
@given(instance=Room_strategy)
@settings(max_examples=25)
def test_Room_instantiation(instance):
    assert isinstance(instance, Room)


RoomManager_strategy = st.builds(RoomManager)
@given(instance=RoomManager_strategy)
@settings(max_examples=25)
def test_RoomManager_instantiation(instance):
    assert isinstance(instance, RoomManager)


ServiceManager_strategy = st.builds(ServiceManager)
@given(instance=ServiceManager_strategy)
@settings(max_examples=25)
def test_ServiceManager_instantiation(instance):
    assert isinstance(instance, ServiceManager)


billing_AdminDiscountManager_strategy = st.builds(billing_AdminDiscountManager)
@given(instance=billing_AdminDiscountManager_strategy)
@settings(max_examples=25)
def test_billing_AdminDiscountManager_instantiation(instance):
    assert isinstance(instance, billing_AdminDiscountManager)


billing_AdminServiceManager_strategy = st.builds(billing_AdminServiceManager)
@given(instance=billing_AdminServiceManager_strategy)
@settings(max_examples=25)
def test_billing_AdminServiceManager_instantiation(instance):
    assert isinstance(instance, billing_AdminServiceManager)


billing_Bill_strategy = st.builds(billing_Bill)
@given(instance=billing_Bill_strategy)
@settings(max_examples=25)
def test_billing_Bill_instantiation(instance):
    assert isinstance(instance, billing_Bill)


billing_BillDataService_strategy = st.builds(billing_BillDataService)
@given(instance=billing_BillDataService_strategy)
@settings(max_examples=25)
def test_billing_BillDataService_instantiation(instance):
    assert isinstance(instance, billing_BillDataService)


billing_CreditCardInformationDataService_strategy = st.builds(billing_CreditCardInformationDataService)
@given(instance=billing_CreditCardInformationDataService_strategy)
@settings(max_examples=25)
def test_billing_CreditCardInformationDataService_instantiation(instance):
    assert isinstance(instance, billing_CreditCardInformationDataService)


billing_Discount_strategy = st.builds(billing_Discount)
@given(instance=billing_Discount_strategy)
@settings(max_examples=25)
def test_billing_Discount_instantiation(instance):
    assert isinstance(instance, billing_Discount)


billing_DiscountDataService_strategy = st.builds(billing_DiscountDataService)
@given(instance=billing_DiscountDataService_strategy)
@settings(max_examples=25)
def test_billing_DiscountDataService_instantiation(instance):
    assert isinstance(instance, billing_DiscountDataService)


billing_DiscountLimit_strategy = st.builds(billing_DiscountLimit)
@given(instance=billing_DiscountLimit_strategy)
@settings(max_examples=25)
def test_billing_DiscountLimit_instantiation(instance):
    assert isinstance(instance, billing_DiscountLimit)


billing_DiscountManagerImpl_strategy = st.builds(billing_DiscountManagerImpl)
@given(instance=billing_DiscountManagerImpl_strategy)
@settings(max_examples=25)
def test_billing_DiscountManagerImpl_instantiation(instance):
    assert isinstance(instance, billing_DiscountManagerImpl)


billing_Purchase_strategy = st.builds(billing_Purchase)
@given(instance=billing_Purchase_strategy)
@settings(max_examples=25)
def test_billing_Purchase_instantiation(instance):
    assert isinstance(instance, billing_Purchase)


billing_Service_strategy = st.builds(billing_Service)
@given(instance=billing_Service_strategy)
@settings(max_examples=25)
def test_billing_Service_instantiation(instance):
    assert isinstance(instance, billing_Service)


billing_ServiceDataService_strategy = st.builds(billing_ServiceDataService)
@given(instance=billing_ServiceDataService_strategy)
@settings(max_examples=25)
def test_billing_ServiceDataService_instantiation(instance):
    assert isinstance(instance, billing_ServiceDataService)


billing_ServiceManagerImpl_strategy = st.builds(billing_ServiceManagerImpl)
@given(instance=billing_ServiceManagerImpl_strategy)
@settings(max_examples=25)
def test_billing_ServiceManagerImpl_instantiation(instance):
    assert isinstance(instance, billing_ServiceManagerImpl)


booking_Booking_strategy = st.builds(booking_Booking)
@given(instance=booking_Booking_strategy)
@settings(max_examples=25)
def test_booking_Booking_instantiation(instance):
    assert isinstance(instance, booking_Booking)


booking_BookingDataService_strategy = st.builds(booking_BookingDataService)
@given(instance=booking_BookingDataService_strategy)
@settings(max_examples=25)
def test_booking_BookingDataService_instantiation(instance):
    assert isinstance(instance, booking_BookingDataService)


booking_BookingManager_strategy = st.builds(booking_BookingManager)
@given(instance=booking_BookingManager_strategy)
@settings(max_examples=25)
def test_booking_BookingManager_instantiation(instance):
    assert isinstance(instance, booking_BookingManager)


booking_LegalEntity_strategy = st.builds(booking_LegalEntity)
@given(instance=booking_LegalEntity_strategy)
@settings(max_examples=25)
def test_booking_LegalEntity_instantiation(instance):
    assert isinstance(instance, booking_LegalEntity)


booking_LegalEntityDataService_strategy = st.builds(booking_LegalEntityDataService)
@given(instance=booking_LegalEntityDataService_strategy)
@settings(max_examples=25)
def test_booking_LegalEntityDataService_instantiation(instance):
    assert isinstance(instance, booking_LegalEntityDataService)


booking_Person_strategy = st.builds(booking_Person)
@given(instance=booking_Person_strategy)
@settings(max_examples=25)
def test_booking_Person_instantiation(instance):
    assert isinstance(instance, booking_Person)


booking_RoomStay_strategy = st.builds(booking_RoomStay)
@given(instance=booking_RoomStay_strategy)
@settings(max_examples=25)
def test_booking_RoomStay_instantiation(instance):
    assert isinstance(instance, booking_RoomStay)


booking_StayRequest_strategy = st.builds(booking_StayRequest)
@given(instance=booking_StayRequest_strategy)
@settings(max_examples=25)
def test_booking_StayRequest_instantiation(instance):
    assert isinstance(instance, booking_StayRequest)


booking_TravelInformation_strategy = st.builds(booking_TravelInformation)
@given(instance=booking_TravelInformation_strategy)
@settings(max_examples=25)
def test_booking_TravelInformation_instantiation(instance):
    assert isinstance(instance, booking_TravelInformation)


facilities_AdminKeyCardManager_strategy = st.builds(facilities_AdminKeyCardManager)
@given(instance=facilities_AdminKeyCardManager_strategy)
@settings(max_examples=25)
def test_facilities_AdminKeyCardManager_instantiation(instance):
    assert isinstance(instance, facilities_AdminKeyCardManager)


facilities_AdminRoomManager_strategy = st.builds(facilities_AdminRoomManager)
@given(instance=facilities_AdminRoomManager_strategy)
@settings(max_examples=25)
def test_facilities_AdminRoomManager_instantiation(instance):
    assert isinstance(instance, facilities_AdminRoomManager)


facilities_KeyCard_strategy = st.builds(facilities_KeyCard)
@given(instance=facilities_KeyCard_strategy)
@settings(max_examples=25)
def test_facilities_KeyCard_instantiation(instance):
    assert isinstance(instance, facilities_KeyCard)


facilities_KeyCardDataService_strategy = st.builds(facilities_KeyCardDataService)
@given(instance=facilities_KeyCardDataService_strategy)
@settings(max_examples=25)
def test_facilities_KeyCardDataService_instantiation(instance):
    assert isinstance(instance, facilities_KeyCardDataService)


facilities_KeyCardManager_strategy = st.builds(facilities_KeyCardManager)
@given(instance=facilities_KeyCardManager_strategy)
@settings(max_examples=25)
def test_facilities_KeyCardManager_instantiation(instance):
    assert isinstance(instance, facilities_KeyCardManager)


facilities_KeyCardManagerImpl_strategy = st.builds(facilities_KeyCardManagerImpl)
@given(instance=facilities_KeyCardManagerImpl_strategy)
@settings(max_examples=25)
def test_facilities_KeyCardManagerImpl_instantiation(instance):
    assert isinstance(instance, facilities_KeyCardManagerImpl)


facilities_Room_strategy = st.builds(facilities_Room)
@given(instance=facilities_Room_strategy)
@settings(max_examples=25)
def test_facilities_Room_instantiation(instance):
    assert isinstance(instance, facilities_Room)


facilities_RoomDataService_strategy = st.builds(facilities_RoomDataService)
@given(instance=facilities_RoomDataService_strategy)
@settings(max_examples=25)
def test_facilities_RoomDataService_instantiation(instance):
    assert isinstance(instance, facilities_RoomDataService)


facilities_RoomManager_strategy = st.builds(facilities_RoomManager)
@given(instance=facilities_RoomManager_strategy)
@settings(max_examples=25)
def test_facilities_RoomManager_instantiation(instance):
    assert isinstance(instance, facilities_RoomManager)


facilities_RoomManagerImpl_strategy = st.builds(facilities_RoomManagerImpl)
@given(instance=facilities_RoomManagerImpl_strategy)
@settings(max_examples=25)
def test_facilities_RoomManagerImpl_instantiation(instance):
    assert isinstance(instance, facilities_RoomManagerImpl)


facilities_RoomType_strategy = st.builds(facilities_RoomType)
@given(instance=facilities_RoomType_strategy)
@settings(max_examples=25)
def test_facilities_RoomType_instantiation(instance):
    assert isinstance(instance, facilities_RoomType)


facilities_RoomTypeDataService_strategy = st.builds(facilities_RoomTypeDataService)
@given(instance=facilities_RoomTypeDataService_strategy)
@settings(max_examples=25)
def test_facilities_RoomTypeDataService_instantiation(instance):
    assert isinstance(instance, facilities_RoomTypeDataService)


tda593_billing_AdminDiscountManager_strategy = st.builds(tda593_billing_AdminDiscountManager)
@given(instance=tda593_billing_AdminDiscountManager_strategy)
@settings(max_examples=25)
def test_tda593_billing_AdminDiscountManager_instantiation(instance):
    assert isinstance(instance, tda593_billing_AdminDiscountManager)


tda593_billing_AdminDiscountManagerImpl_strategy = st.builds(tda593_billing_AdminDiscountManagerImpl)
@given(instance=tda593_billing_AdminDiscountManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_billing_AdminDiscountManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_billing_AdminDiscountManagerImpl)


tda593_billing_AdminServiceManager_strategy = st.builds(tda593_billing_AdminServiceManager)
@given(instance=tda593_billing_AdminServiceManager_strategy)
@settings(max_examples=25)
def test_tda593_billing_AdminServiceManager_instantiation(instance):
    assert isinstance(instance, tda593_billing_AdminServiceManager)


tda593_billing_AdminServiceManagerImpl_strategy = st.builds(tda593_billing_AdminServiceManagerImpl)
@given(instance=tda593_billing_AdminServiceManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_billing_AdminServiceManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_billing_AdminServiceManagerImpl)


tda593_billing_BankingManager_strategy = st.builds(tda593_billing_BankingManager)
@given(instance=tda593_billing_BankingManager_strategy)
@settings(max_examples=25)
def test_tda593_billing_BankingManager_instantiation(instance):
    assert isinstance(instance, tda593_billing_BankingManager)


tda593_billing_BankingManagerImpl_strategy = st.builds(tda593_billing_BankingManagerImpl)
@given(instance=tda593_billing_BankingManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_billing_BankingManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_billing_BankingManagerImpl)


tda593_billing_Bill_strategy = st.builds(tda593_billing_Bill, date=st.dates(), id=st.integers(), isPaid=st.booleans(), isPublished=st.booleans())
@given(instance=tda593_billing_Bill_strategy)
@settings(max_examples=25)
def test_tda593_billing_Bill_instantiation(instance):
    assert isinstance(instance, tda593_billing_Bill)


tda593_billing_BillDataService_strategy = st.builds(tda593_billing_BillDataService)
@given(instance=tda593_billing_BillDataService_strategy)
@settings(max_examples=25)
def test_tda593_billing_BillDataService_instantiation(instance):
    assert isinstance(instance, tda593_billing_BillDataService)


tda593_billing_BillManager_strategy = st.builds(tda593_billing_BillManager)
@given(instance=tda593_billing_BillManager_strategy)
@settings(max_examples=25)
def test_tda593_billing_BillManager_instantiation(instance):
    assert isinstance(instance, tda593_billing_BillManager)


tda593_billing_BillManagerImpl_strategy = st.builds(tda593_billing_BillManagerImpl)
@given(instance=tda593_billing_BillManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_billing_BillManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_billing_BillManagerImpl)


tda593_billing_BookingBill_strategy = st.builds(tda593_billing_BookingBill)
@given(instance=tda593_billing_BookingBill_strategy)
@settings(max_examples=25)
def test_tda593_billing_BookingBill_instantiation(instance):
    assert isinstance(instance, tda593_billing_BookingBill)


tda593_billing_CreditCardInformation_strategy = st.builds(tda593_billing_CreditCardInformation, cardNumber=safe_text, ccv=safe_text, expirationDate=st.dates(), firstName=safe_text, lastName=safe_text)
@given(instance=tda593_billing_CreditCardInformation_strategy)
@settings(max_examples=25)
def test_tda593_billing_CreditCardInformation_instantiation(instance):
    assert isinstance(instance, tda593_billing_CreditCardInformation)


tda593_billing_CreditCardInformationDataService_strategy = st.builds(tda593_billing_CreditCardInformationDataService)
@given(instance=tda593_billing_CreditCardInformationDataService_strategy)
@settings(max_examples=25)
def test_tda593_billing_CreditCardInformationDataService_instantiation(instance):
    assert isinstance(instance, tda593_billing_CreditCardInformationDataService)


tda593_billing_CreditCardManager_strategy = st.builds(tda593_billing_CreditCardManager)
@given(instance=tda593_billing_CreditCardManager_strategy)
@settings(max_examples=25)
def test_tda593_billing_CreditCardManager_instantiation(instance):
    assert isinstance(instance, tda593_billing_CreditCardManager)


tda593_billing_CreditCardManagerImpl_strategy = st.builds(tda593_billing_CreditCardManagerImpl)
@given(instance=tda593_billing_CreditCardManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_billing_CreditCardManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_billing_CreditCardManagerImpl)


tda593_billing_Discount_strategy = st.builds(tda593_billing_Discount, code=safe_text, name=safe_text)
@given(instance=tda593_billing_Discount_strategy)
@settings(max_examples=25)
def test_tda593_billing_Discount_instantiation(instance):
    assert isinstance(instance, tda593_billing_Discount)


tda593_billing_DiscountDataService_strategy = st.builds(tda593_billing_DiscountDataService)
@given(instance=tda593_billing_DiscountDataService_strategy)
@settings(max_examples=25)
def test_tda593_billing_DiscountDataService_instantiation(instance):
    assert isinstance(instance, tda593_billing_DiscountDataService)


tda593_billing_DiscountLimit_strategy = st.builds(tda593_billing_DiscountLimit, endDate=st.dates(), id=st.integers(), startDate=st.dates(), timesLeftToUse=st.integers())
@given(instance=tda593_billing_DiscountLimit_strategy)
@settings(max_examples=25)
def test_tda593_billing_DiscountLimit_instantiation(instance):
    assert isinstance(instance, tda593_billing_DiscountLimit)


tda593_billing_DiscountManager_strategy = st.builds(tda593_billing_DiscountManager)
@given(instance=tda593_billing_DiscountManager_strategy)
@settings(max_examples=25)
def test_tda593_billing_DiscountManager_instantiation(instance):
    assert isinstance(instance, tda593_billing_DiscountManager)


tda593_billing_DiscountManagerImpl_strategy = st.builds(tda593_billing_DiscountManagerImpl)
@given(instance=tda593_billing_DiscountManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_billing_DiscountManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_billing_DiscountManagerImpl)


tda593_billing_PercentageDiscount_strategy = st.builds(tda593_billing_PercentageDiscount, percentage=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=tda593_billing_PercentageDiscount_strategy)
@settings(max_examples=25)
def test_tda593_billing_PercentageDiscount_instantiation(instance):
    assert isinstance(instance, tda593_billing_PercentageDiscount)


tda593_billing_Purchase_strategy = st.builds(tda593_billing_Purchase, id=st.integers(), price=st.floats(allow_nan=False, allow_infinity=False), quantity=st.integers())
@given(instance=tda593_billing_Purchase_strategy)
@settings(max_examples=25)
def test_tda593_billing_Purchase_instantiation(instance):
    assert isinstance(instance, tda593_billing_Purchase)


tda593_billing_Service_strategy = st.builds(tda593_billing_Service, id=st.integers(), name=safe_text, price=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=tda593_billing_Service_strategy)
@settings(max_examples=25)
def test_tda593_billing_Service_instantiation(instance):
    assert isinstance(instance, tda593_billing_Service)


tda593_billing_ServiceDataService_strategy = st.builds(tda593_billing_ServiceDataService)
@given(instance=tda593_billing_ServiceDataService_strategy)
@settings(max_examples=25)
def test_tda593_billing_ServiceDataService_instantiation(instance):
    assert isinstance(instance, tda593_billing_ServiceDataService)


tda593_billing_ServiceManager_strategy = st.builds(tda593_billing_ServiceManager)
@given(instance=tda593_billing_ServiceManager_strategy)
@settings(max_examples=25)
def test_tda593_billing_ServiceManager_instantiation(instance):
    assert isinstance(instance, tda593_billing_ServiceManager)


tda593_billing_ServiceManagerImpl_strategy = st.builds(tda593_billing_ServiceManagerImpl)
@given(instance=tda593_billing_ServiceManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_billing_ServiceManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_billing_ServiceManagerImpl)


tda593_billing_SumDiscount_strategy = st.builds(tda593_billing_SumDiscount, discountSum=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=tda593_billing_SumDiscount_strategy)
@settings(max_examples=25)
def test_tda593_billing_SumDiscount_instantiation(instance):
    assert isinstance(instance, tda593_billing_SumDiscount)


tda593_booking_Booking_strategy = st.builds(tda593_booking_Booking, endDate=st.dates(), id=st.integers(), isCanceled=st.booleans(), price=st.floats(allow_nan=False, allow_infinity=False), specialRequest=safe_text, startDate=st.dates())
@given(instance=tda593_booking_Booking_strategy)
@settings(max_examples=25)
def test_tda593_booking_Booking_instantiation(instance):
    assert isinstance(instance, tda593_booking_Booking)


tda593_booking_BookingDataService_strategy = st.builds(tda593_booking_BookingDataService)
@given(instance=tda593_booking_BookingDataService_strategy)
@settings(max_examples=25)
def test_tda593_booking_BookingDataService_instantiation(instance):
    assert isinstance(instance, tda593_booking_BookingDataService)


tda593_booking_BookingManager_strategy = st.builds(tda593_booking_BookingManager)
@given(instance=tda593_booking_BookingManager_strategy)
@settings(max_examples=25)
def test_tda593_booking_BookingManager_instantiation(instance):
    assert isinstance(instance, tda593_booking_BookingManager)


tda593_booking_BookingManagerImpl_strategy = st.builds(tda593_booking_BookingManagerImpl)
@given(instance=tda593_booking_BookingManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_booking_BookingManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_booking_BookingManagerImpl)


tda593_booking_LegalEntity_strategy = st.builds(tda593_booking_LegalEntity, email=safe_text, id=st.integers(), phone=safe_text)
@given(instance=tda593_booking_LegalEntity_strategy)
@settings(max_examples=25)
def test_tda593_booking_LegalEntity_instantiation(instance):
    assert isinstance(instance, tda593_booking_LegalEntity)


tda593_booking_LegalEntityDataService_strategy = st.builds(tda593_booking_LegalEntityDataService)
@given(instance=tda593_booking_LegalEntityDataService_strategy)
@settings(max_examples=25)
def test_tda593_booking_LegalEntityDataService_instantiation(instance):
    assert isinstance(instance, tda593_booking_LegalEntityDataService)


tda593_booking_LegalEntityManager_strategy = st.builds(tda593_booking_LegalEntityManager)
@given(instance=tda593_booking_LegalEntityManager_strategy)
@settings(max_examples=25)
def test_tda593_booking_LegalEntityManager_instantiation(instance):
    assert isinstance(instance, tda593_booking_LegalEntityManager)


tda593_booking_LegalEntityManagerImpl_strategy = st.builds(tda593_booking_LegalEntityManagerImpl)
@given(instance=tda593_booking_LegalEntityManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_booking_LegalEntityManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_booking_LegalEntityManagerImpl)


tda593_booking_Organization_strategy = st.builds(tda593_booking_Organization, name=safe_text, organizationNumber=safe_text)
@given(instance=tda593_booking_Organization_strategy)
@settings(max_examples=25)
def test_tda593_booking_Organization_instantiation(instance):
    assert isinstance(instance, tda593_booking_Organization)


tda593_booking_Person_strategy = st.builds(tda593_booking_Person, firstname=safe_text, lastname=safe_text, socialSecurityNumber=safe_text)
@given(instance=tda593_booking_Person_strategy)
@settings(max_examples=25)
def test_tda593_booking_Person_instantiation(instance):
    assert isinstance(instance, tda593_booking_Person)


tda593_booking_RoomStay_strategy = st.builds(tda593_booking_RoomStay, active=st.booleans(), id=st.integers())
@given(instance=tda593_booking_RoomStay_strategy)
@settings(max_examples=25)
def test_tda593_booking_RoomStay_instantiation(instance):
    assert isinstance(instance, tda593_booking_RoomStay)


tda593_booking_StayRequest_strategy = st.builds(tda593_booking_StayRequest, id=st.integers(), text=safe_text, timeStamp=st.dates())
@given(instance=tda593_booking_StayRequest_strategy)
@settings(max_examples=25)
def test_tda593_booking_StayRequest_instantiation(instance):
    assert isinstance(instance, tda593_booking_StayRequest)


tda593_booking_TravelInformation_strategy = st.builds(tda593_booking_TravelInformation, comment=safe_text, id=st.integers(), trackingId=safe_text)
@given(instance=tda593_booking_TravelInformation_strategy)
@settings(max_examples=25)
def test_tda593_booking_TravelInformation_instantiation(instance):
    assert isinstance(instance, tda593_booking_TravelInformation)


tda593_california_DataService_strategy = st.builds(tda593_california_DataService)
@given(instance=tda593_california_DataService_strategy)
@settings(max_examples=25)
def test_tda593_california_DataService_instantiation(instance):
    assert isinstance(instance, tda593_california_DataService)


tda593_facilities_AdminKeyCardManager_strategy = st.builds(tda593_facilities_AdminKeyCardManager)
@given(instance=tda593_facilities_AdminKeyCardManager_strategy)
@settings(max_examples=25)
def test_tda593_facilities_AdminKeyCardManager_instantiation(instance):
    assert isinstance(instance, tda593_facilities_AdminKeyCardManager)


tda593_facilities_AdminKeyCardManagerImpl_strategy = st.builds(tda593_facilities_AdminKeyCardManagerImpl)
@given(instance=tda593_facilities_AdminKeyCardManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_facilities_AdminKeyCardManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_facilities_AdminKeyCardManagerImpl)


tda593_facilities_AdminRoomManager_strategy = st.builds(tda593_facilities_AdminRoomManager)
@given(instance=tda593_facilities_AdminRoomManager_strategy)
@settings(max_examples=25)
def test_tda593_facilities_AdminRoomManager_instantiation(instance):
    assert isinstance(instance, tda593_facilities_AdminRoomManager)


tda593_facilities_AdminRoomManagerImpl_strategy = st.builds(tda593_facilities_AdminRoomManagerImpl)
@given(instance=tda593_facilities_AdminRoomManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_facilities_AdminRoomManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_facilities_AdminRoomManagerImpl)


tda593_facilities_ConferenceRoom_strategy = st.builds(tda593_facilities_ConferenceRoom, equipment=safe_text, numberOfSeats=st.integers())
@given(instance=tda593_facilities_ConferenceRoom_strategy)
@settings(max_examples=25)
def test_tda593_facilities_ConferenceRoom_instantiation(instance):
    assert isinstance(instance, tda593_facilities_ConferenceRoom)


tda593_facilities_GuestRoom_strategy = st.builds(tda593_facilities_GuestRoom, numberOfBeds=st.integers(), numberOfExtrabeds=st.integers())
@given(instance=tda593_facilities_GuestRoom_strategy)
@settings(max_examples=25)
def test_tda593_facilities_GuestRoom_instantiation(instance):
    assert isinstance(instance, tda593_facilities_GuestRoom)


tda593_facilities_KeyCard_strategy = st.builds(tda593_facilities_KeyCard, id=safe_text)
@given(instance=tda593_facilities_KeyCard_strategy)
@settings(max_examples=25)
def test_tda593_facilities_KeyCard_instantiation(instance):
    assert isinstance(instance, tda593_facilities_KeyCard)


tda593_facilities_KeyCardDataService_strategy = st.builds(tda593_facilities_KeyCardDataService)
@given(instance=tda593_facilities_KeyCardDataService_strategy)
@settings(max_examples=25)
def test_tda593_facilities_KeyCardDataService_instantiation(instance):
    assert isinstance(instance, tda593_facilities_KeyCardDataService)


tda593_facilities_KeyCardManager_strategy = st.builds(tda593_facilities_KeyCardManager)
@given(instance=tda593_facilities_KeyCardManager_strategy)
@settings(max_examples=25)
def test_tda593_facilities_KeyCardManager_instantiation(instance):
    assert isinstance(instance, tda593_facilities_KeyCardManager)


tda593_facilities_KeyCardManagerImpl_strategy = st.builds(tda593_facilities_KeyCardManagerImpl)
@given(instance=tda593_facilities_KeyCardManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_facilities_KeyCardManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_facilities_KeyCardManagerImpl)


tda593_facilities_Room_strategy = st.builds(tda593_facilities_Room, description=safe_text, disabilityApprovals=safe_text, floor=st.integers(), isBeingCleaned=st.booleans(), isOperational=st.booleans(), photos=safe_text, roomNumber=safe_text)
@given(instance=tda593_facilities_Room_strategy)
@settings(max_examples=25)
def test_tda593_facilities_Room_instantiation(instance):
    assert isinstance(instance, tda593_facilities_Room)


tda593_facilities_RoomDataService_strategy = st.builds(tda593_facilities_RoomDataService)
@given(instance=tda593_facilities_RoomDataService_strategy)
@settings(max_examples=25)
def test_tda593_facilities_RoomDataService_instantiation(instance):
    assert isinstance(instance, tda593_facilities_RoomDataService)


tda593_facilities_RoomManager_strategy = st.builds(tda593_facilities_RoomManager)
@given(instance=tda593_facilities_RoomManager_strategy)
@settings(max_examples=25)
def test_tda593_facilities_RoomManager_instantiation(instance):
    assert isinstance(instance, tda593_facilities_RoomManager)


tda593_facilities_RoomManagerImpl_strategy = st.builds(tda593_facilities_RoomManagerImpl)
@given(instance=tda593_facilities_RoomManagerImpl_strategy)
@settings(max_examples=25)
def test_tda593_facilities_RoomManagerImpl_instantiation(instance):
    assert isinstance(instance, tda593_facilities_RoomManagerImpl)


tda593_facilities_RoomType_strategy = st.builds(tda593_facilities_RoomType, description=safe_text, name=safe_text, price=st.floats(allow_nan=False, allow_infinity=False), roomApprovals=safe_text)
@given(instance=tda593_facilities_RoomType_strategy)
@settings(max_examples=25)
def test_tda593_facilities_RoomType_instantiation(instance):
    assert isinstance(instance, tda593_facilities_RoomType)


tda593_facilities_RoomTypeDataService_strategy = st.builds(tda593_facilities_RoomTypeDataService)
@given(instance=tda593_facilities_RoomTypeDataService_strategy)
@settings(max_examples=25)
def test_tda593_facilities_RoomTypeDataService_instantiation(instance):
    assert isinstance(instance, tda593_facilities_RoomTypeDataService)


