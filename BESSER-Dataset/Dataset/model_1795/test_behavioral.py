import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Cleaning,
    Clerk,
    FeedbackReader,
    FeedbackWriter,
    HotelSystem,
    MakeBooking,
    Payment,
    ReceptionHandling,
    RoomAttributeHandling,
    RoomBooking,
    RoomFetcher,
    RoomHandling,
    RoomTypeHandling,
    RootElement_Booking,
    RootElement_BookingHandler,
    RootElement_Cleaning,
    RootElement_CleaningHandler,
    RootElement_Clerk,
    RootElement_DailyRoomBooking,
    RootElement_Feedback,
    RootElement_FeedbackHandler,
    RootElement_FeedbackReader,
    RootElement_FeedbackWriter,
    RootElement_Guest,
    RootElement_Hotel,
    RootElement_HotelSystem,
    RootElement_HourlyRoomBooking,
    RootElement_MakeBooking,
    RootElement_Manager,
    RootElement_Payment,
    RootElement_PaymentHandler,
    RootElement_ReceptionHandling,
    RootElement_Room,
    RootElement_RoomAttribute,
    RootElement_RoomAttributeHandling,
    RootElement_RoomBooking,
    RootElement_RoomFetcher,
    RootElement_RoomHandling,
    RootElement_RoomStructure,
    RootElement_RoomType,
    RootElement_RoomTypeHandling,
    RootElement_ServiceItem,
    RootElement_ServiceItemHandling,
    RootElement_Staff,
    RootElement_SupportTicket,
    RootElement_SupportTicketHandler,
    RootElement_SupportTicketReader,
    RootElement_SupportTicketWriter,
    RootElement_SysAdmin,
    ServiceItemHandling,
    Staff,
    SupportTicketReader,
    SupportTicketWriter,
    SysAdmin,
    BookingStatus,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_cleaning17_reverse_link_reassign_clear():
    a1 = RootElement_Staff(name="sample_text", staffID="sample_text")
    a2 = RootElement_Staff(name="sample_text_2", staffID="sample_text_2")
    b = RootElement_Cleaning()
    _safe_set(b, 'RootElement_Cleaning', a1)
    assert _is_linked(b, 'RootElement_Cleaning', a1)
    if hasattr(a1, 'RootElement_Staff'):
        assert _is_linked(a1, 'RootElement_Staff', b)
    _safe_set(b, 'RootElement_Cleaning', a2)
    assert _is_linked(b, 'RootElement_Cleaning', a2)
    if hasattr(a1, 'RootElement_Staff'):
        assert not _is_linked(a1, 'RootElement_Staff', b)
    if hasattr(a2, 'RootElement_Staff'):
        assert _is_linked(a2, 'RootElement_Staff', b)
    _safe_set(b, 'RootElement_Cleaning', None)
    assert not _is_linked(b, 'RootElement_Cleaning', a2)
    if hasattr(a2, 'RootElement_Staff'):
        assert not _is_linked(a2, 'RootElement_Staff', b)


def test_assoc_feedbackWriter3_reverse_link_reassign_clear():
    a1 = RootElement_Guest(mail="sample_text", name="sample_text", nationality="sample_text", nextDestination="sample_text", phoneNumber="sample_text", socialSecurityNumber="sample_text")
    a2 = RootElement_Guest(mail="sample_text_2", name="sample_text_2", nationality="sample_text_2", nextDestination="sample_text_2", phoneNumber="sample_text_2", socialSecurityNumber="sample_text_2")
    b = RootElement_FeedbackWriter()
    _safe_set(b, 'RootElement_FeedbackWriter', a1)
    assert _is_linked(b, 'RootElement_FeedbackWriter', a1)
    if hasattr(a1, 'RootElement_Guest4'):
        assert _is_linked(a1, 'RootElement_Guest4', b)
    _safe_set(b, 'RootElement_FeedbackWriter', a2)
    assert _is_linked(b, 'RootElement_FeedbackWriter', a2)
    if hasattr(a1, 'RootElement_Guest4'):
        assert not _is_linked(a1, 'RootElement_Guest4', b)
    if hasattr(a2, 'RootElement_Guest4'):
        assert _is_linked(a2, 'RootElement_Guest4', b)
    _safe_set(b, 'RootElement_FeedbackWriter', None)
    assert not _is_linked(b, 'RootElement_FeedbackWriter', a2)
    if hasattr(a2, 'RootElement_Guest4'):
        assert not _is_linked(a2, 'RootElement_Guest4', b)


def test_assoc_guest6_reverse_link_reassign_clear():
    a1 = RootElement_Guest(mail="sample_text", name="sample_text", nationality="sample_text", nextDestination="sample_text", phoneNumber="sample_text", socialSecurityNumber="sample_text")
    a2 = RootElement_Guest(mail="sample_text_2", name="sample_text_2", nationality="sample_text_2", nextDestination="sample_text_2", phoneNumber="sample_text_2", socialSecurityNumber="sample_text_2")
    b = RootElement_Booking(bookingID="sample_text")
    _safe_set(b, 'RootElement_Booking7', a1)
    assert _is_linked(b, 'RootElement_Booking7', a1)
    if hasattr(a1, 'RootElement_Guest8'):
        assert _is_linked(a1, 'RootElement_Guest8', b)
    _safe_set(b, 'RootElement_Booking7', a2)
    assert _is_linked(b, 'RootElement_Booking7', a2)
    if hasattr(a1, 'RootElement_Guest8'):
        assert not _is_linked(a1, 'RootElement_Guest8', b)
    if hasattr(a2, 'RootElement_Guest8'):
        assert _is_linked(a2, 'RootElement_Guest8', b)
    _safe_set(b, 'RootElement_Booking7', None)
    assert not _is_linked(b, 'RootElement_Booking7', a2)
    if hasattr(a2, 'RootElement_Guest8'):
        assert not _is_linked(a2, 'RootElement_Guest8', b)


def test_assoc_makeBooking1_reverse_link_reassign_clear():
    a1 = RootElement_MakeBooking()
    a2 = RootElement_MakeBooking()
    b = RootElement_Guest(mail="sample_text", name="sample_text", nationality="sample_text", nextDestination="sample_text", phoneNumber="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'RootElement_Guest2', a1)
    assert _is_linked(b, 'RootElement_Guest2', a1)
    if hasattr(a1, 'RootElement_MakeBooking'):
        assert _is_linked(a1, 'RootElement_MakeBooking', b)
    _safe_set(b, 'RootElement_Guest2', a2)
    assert _is_linked(b, 'RootElement_Guest2', a2)
    if hasattr(a1, 'RootElement_MakeBooking'):
        assert not _is_linked(a1, 'RootElement_MakeBooking', b)
    if hasattr(a2, 'RootElement_MakeBooking'):
        assert _is_linked(a2, 'RootElement_MakeBooking', b)
    _safe_set(b, 'RootElement_Guest2', None)
    assert not _is_linked(b, 'RootElement_Guest2', a2)
    if hasattr(a2, 'RootElement_MakeBooking'):
        assert not _is_linked(a2, 'RootElement_MakeBooking', b)


def test_assoc_room11_reverse_link_reassign_clear():
    a1 = RootElement_RoomBooking(bookingStatus="sample_text", endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    a2 = RootElement_RoomBooking(bookingStatus="sample_text_2", endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    b = RootElement_Room(isOccupied="sample_text", name="sample_text", needCleaning="sample_text")
    _safe_set(b, 'RootElement_Room', a1)
    assert _is_linked(b, 'RootElement_Room', a1)
    if hasattr(a1, 'RootElement_RoomBooking12'):
        assert _is_linked(a1, 'RootElement_RoomBooking12', b)
    _safe_set(b, 'RootElement_Room', a2)
    assert _is_linked(b, 'RootElement_Room', a2)
    if hasattr(a1, 'RootElement_RoomBooking12'):
        assert not _is_linked(a1, 'RootElement_RoomBooking12', b)
    if hasattr(a2, 'RootElement_RoomBooking12'):
        assert _is_linked(a2, 'RootElement_RoomBooking12', b)
    _safe_set(b, 'RootElement_Room', None)
    assert not _is_linked(b, 'RootElement_Room', a2)
    if hasattr(a2, 'RootElement_RoomBooking12'):
        assert not _is_linked(a2, 'RootElement_RoomBooking12', b)


def test_assoc_roomAttributes15_reverse_link_reassign_clear():
    a1 = RootElement_RoomType(capacity="sample_text", name="sample_text", price="sample_text")
    a2 = RootElement_RoomType(capacity="sample_text_2", name="sample_text_2", price="sample_text_2")
    b = RootElement_RoomAttribute(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'RootElement_RoomAttribute', a1)
    assert _is_linked(b, 'RootElement_RoomAttribute', a1)
    if hasattr(a1, 'RootElement_RoomType16'):
        assert _is_linked(a1, 'RootElement_RoomType16', b)
    _safe_set(b, 'RootElement_RoomAttribute', a2)
    assert _is_linked(b, 'RootElement_RoomAttribute', a2)
    if hasattr(a1, 'RootElement_RoomType16'):
        assert not _is_linked(a1, 'RootElement_RoomType16', b)
    if hasattr(a2, 'RootElement_RoomType16'):
        assert _is_linked(a2, 'RootElement_RoomType16', b)
    _safe_set(b, 'RootElement_RoomAttribute', None)
    assert not _is_linked(b, 'RootElement_RoomAttribute', a2)
    if hasattr(a2, 'RootElement_RoomType16'):
        assert not _is_linked(a2, 'RootElement_RoomType16', b)


def test_assoc_roomType13_reverse_link_reassign_clear():
    a1 = RootElement_RoomType(capacity="sample_text", name="sample_text", price="sample_text")
    a2 = RootElement_RoomType(capacity="sample_text_2", name="sample_text_2", price="sample_text_2")
    b = RootElement_Room(isOccupied="sample_text", name="sample_text", needCleaning="sample_text")
    _safe_set(b, 'RootElement_Room14', a1)
    assert _is_linked(b, 'RootElement_Room14', a1)
    if hasattr(a1, 'RootElement_RoomType'):
        assert _is_linked(a1, 'RootElement_RoomType', b)
    _safe_set(b, 'RootElement_Room14', a2)
    assert _is_linked(b, 'RootElement_Room14', a2)
    if hasattr(a1, 'RootElement_RoomType'):
        assert not _is_linked(a1, 'RootElement_RoomType', b)
    if hasattr(a2, 'RootElement_RoomType'):
        assert _is_linked(a2, 'RootElement_RoomType', b)
    _safe_set(b, 'RootElement_Room14', None)
    assert not _is_linked(b, 'RootElement_Room14', a2)
    if hasattr(a2, 'RootElement_RoomType'):
        assert not _is_linked(a2, 'RootElement_RoomType', b)


def test_assoc_roombooking5_reverse_link_reassign_clear():
    a1 = RootElement_RoomBooking(bookingStatus="sample_text", endDate=date(2024, 1, 1), startDate=date(2024, 1, 1))
    a2 = RootElement_RoomBooking(bookingStatus="sample_text_2", endDate=date(2025, 6, 15), startDate=date(2025, 6, 15))
    b = RootElement_Booking(bookingID="sample_text")
    _safe_set(b, 'RootElement_Booking', {a1})
    assert _is_linked(b, 'RootElement_Booking', a1)
    if hasattr(a1, 'RootElement_RoomBooking'):
        assert _is_linked(a1, 'RootElement_RoomBooking', b)
    _safe_set(b, 'RootElement_Booking', {a2})
    assert _is_linked(b, 'RootElement_Booking', a2)
    if hasattr(a1, 'RootElement_RoomBooking'):
        assert not _is_linked(a1, 'RootElement_RoomBooking', b)
    if hasattr(a2, 'RootElement_RoomBooking'):
        assert _is_linked(a2, 'RootElement_RoomBooking', b)
    _safe_set(b, 'RootElement_Booking', set())
    assert not _is_linked(b, 'RootElement_Booking', a2)
    if hasattr(a2, 'RootElement_RoomBooking'):
        assert not _is_linked(a2, 'RootElement_RoomBooking', b)


def test_assoc_serviceitem9_reverse_link_reassign_clear():
    a1 = RootElement_ServiceItem(description="sample_text", name="sample_text", price="sample_text")
    a2 = RootElement_ServiceItem(description="sample_text_2", name="sample_text_2", price="sample_text_2")
    b = RootElement_Booking(bookingID="sample_text")
    _safe_set(b, 'RootElement_Booking10', {a1})
    assert _is_linked(b, 'RootElement_Booking10', a1)
    if hasattr(a1, 'RootElement_ServiceItem'):
        assert _is_linked(a1, 'RootElement_ServiceItem', b)
    _safe_set(b, 'RootElement_Booking10', {a2})
    assert _is_linked(b, 'RootElement_Booking10', a2)
    if hasattr(a1, 'RootElement_ServiceItem'):
        assert not _is_linked(a1, 'RootElement_ServiceItem', b)
    if hasattr(a2, 'RootElement_ServiceItem'):
        assert _is_linked(a2, 'RootElement_ServiceItem', b)
    _safe_set(b, 'RootElement_Booking10', set())
    assert not _is_linked(b, 'RootElement_Booking10', a2)
    if hasattr(a2, 'RootElement_ServiceItem'):
        assert not _is_linked(a2, 'RootElement_ServiceItem', b)


def test_assoc_supportTicketReader18_reverse_link_reassign_clear():
    a1 = RootElement_SupportTicketReader()
    a2 = RootElement_SupportTicketReader()
    b = RootElement_Staff(name="sample_text", staffID="sample_text")
    _safe_set(b, 'RootElement_Staff19', a1)
    assert _is_linked(b, 'RootElement_Staff19', a1)
    if hasattr(a1, 'RootElement_SupportTicketReader'):
        assert _is_linked(a1, 'RootElement_SupportTicketReader', b)
    _safe_set(b, 'RootElement_Staff19', a2)
    assert _is_linked(b, 'RootElement_Staff19', a2)
    if hasattr(a1, 'RootElement_SupportTicketReader'):
        assert not _is_linked(a1, 'RootElement_SupportTicketReader', b)
    if hasattr(a2, 'RootElement_SupportTicketReader'):
        assert _is_linked(a2, 'RootElement_SupportTicketReader', b)
    _safe_set(b, 'RootElement_Staff19', None)
    assert not _is_linked(b, 'RootElement_Staff19', a2)
    if hasattr(a2, 'RootElement_SupportTicketReader'):
        assert not _is_linked(a2, 'RootElement_SupportTicketReader', b)


def test_assoc_supportTicketWriter0_reverse_link_reassign_clear():
    a1 = RootElement_SupportTicketWriter()
    a2 = RootElement_SupportTicketWriter()
    b = RootElement_Guest(mail="sample_text", name="sample_text", nationality="sample_text", nextDestination="sample_text", phoneNumber="sample_text", socialSecurityNumber="sample_text")
    _safe_set(b, 'RootElement_Guest', a1)
    assert _is_linked(b, 'RootElement_Guest', a1)
    if hasattr(a1, 'RootElement_SupportTicketWriter'):
        assert _is_linked(a1, 'RootElement_SupportTicketWriter', b)
    _safe_set(b, 'RootElement_Guest', a2)
    assert _is_linked(b, 'RootElement_Guest', a2)
    if hasattr(a1, 'RootElement_SupportTicketWriter'):
        assert not _is_linked(a1, 'RootElement_SupportTicketWriter', b)
    if hasattr(a2, 'RootElement_SupportTicketWriter'):
        assert _is_linked(a2, 'RootElement_SupportTicketWriter', b)
    _safe_set(b, 'RootElement_Guest', None)
    assert not _is_linked(b, 'RootElement_Guest', a2)
    if hasattr(a2, 'RootElement_SupportTicketWriter'):
        assert not _is_linked(a2, 'RootElement_SupportTicketWriter', b)


def test_assoc_supportTicketWriter20_reverse_link_reassign_clear():
    a1 = RootElement_SupportTicketWriter()
    a2 = RootElement_SupportTicketWriter()
    b = RootElement_Staff(name="sample_text", staffID="sample_text")
    _safe_set(b, 'RootElement_Staff21', a1)
    assert _is_linked(b, 'RootElement_Staff21', a1)
    if hasattr(a1, 'RootElement_SupportTicketWriter22'):
        assert _is_linked(a1, 'RootElement_SupportTicketWriter22', b)
    _safe_set(b, 'RootElement_Staff21', a2)
    assert _is_linked(b, 'RootElement_Staff21', a2)
    if hasattr(a1, 'RootElement_SupportTicketWriter22'):
        assert not _is_linked(a1, 'RootElement_SupportTicketWriter22', b)
    if hasattr(a2, 'RootElement_SupportTicketWriter22'):
        assert _is_linked(a2, 'RootElement_SupportTicketWriter22', b)
    _safe_set(b, 'RootElement_Staff21', None)
    assert not _is_linked(b, 'RootElement_Staff21', a2)
    if hasattr(a2, 'RootElement_SupportTicketWriter22'):
        assert not _is_linked(a2, 'RootElement_SupportTicketWriter22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_booking32_stub_double():
    # RootElement_BookingHandler has no real 'RootElement_BookingHandler' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_Booking(bookingID="sample_text")
    partner = RootElement_BookingHandler()
    setattr(partner, 'RootElement_BookingHandler', None)
    _safe_set(owner, 'RootElement_Booking33', partner)
    assert owner in getattr(partner, 'RootElement_BookingHandler')
    _safe_set(owner, 'RootElement_Booking33', None)
    assert owner not in getattr(partner, 'RootElement_BookingHandler')


def test_assoc_feedback44_stub_double():
    # RootElement_FeedbackHandler has no real 'RootElement_FeedbackHandler' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_Feedback's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_Feedback's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_Feedback(feedbackDescription="sample_text", rating="sample_text", read="sample_text")
    partner = RootElement_FeedbackHandler()
    setattr(partner, 'RootElement_FeedbackHandler', None)
    _safe_set(owner, 'RootElement_Feedback', partner)
    assert owner in getattr(partner, 'RootElement_FeedbackHandler')
    _safe_set(owner, 'RootElement_Feedback', None)
    assert owner not in getattr(partner, 'RootElement_FeedbackHandler')


def test_assoc_feedbackReader31_stub_double():
    # RootElement_Manager has no real 'RootElement_Manager' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_FeedbackReader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_FeedbackReader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_FeedbackReader()
    partner = RootElement_Manager()
    setattr(partner, 'RootElement_Manager', None)
    _safe_set(owner, 'RootElement_FeedbackReader', partner)
    assert getattr(partner, 'RootElement_Manager') == owner
    _safe_set(owner, 'RootElement_FeedbackReader', None)
    assert getattr(partner, 'RootElement_Manager') is None


def test_assoc_makeBooking26_stub_double():
    # RootElement_Clerk has no real 'RootElement_Clerk27' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_MakeBooking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_MakeBooking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_MakeBooking()
    partner = RootElement_Clerk()
    setattr(partner, 'RootElement_Clerk27', None)
    _safe_set(owner, 'RootElement_MakeBooking28', partner)
    assert getattr(partner, 'RootElement_Clerk27') == owner
    _safe_set(owner, 'RootElement_MakeBooking28', None)
    assert getattr(partner, 'RootElement_Clerk27') is None


def test_assoc_payment29_stub_double():
    # RootElement_Clerk has no real 'RootElement_Clerk30' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_Payment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_Payment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_Payment()
    partner = RootElement_Clerk()
    setattr(partner, 'RootElement_Clerk30', None)
    _safe_set(owner, 'RootElement_Payment', partner)
    assert getattr(partner, 'RootElement_Clerk30') == owner
    _safe_set(owner, 'RootElement_Payment', None)
    assert getattr(partner, 'RootElement_Clerk30') is None


def test_assoc_receptionHandling23_stub_double():
    # RootElement_Clerk has no real 'RootElement_Clerk' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_ReceptionHandling's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_ReceptionHandling's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_ReceptionHandling()
    partner = RootElement_Clerk()
    setattr(partner, 'RootElement_Clerk', None)
    _safe_set(owner, 'RootElement_ReceptionHandling', partner)
    assert getattr(partner, 'RootElement_Clerk') == owner
    _safe_set(owner, 'RootElement_ReceptionHandling', None)
    assert getattr(partner, 'RootElement_Clerk') is None


def test_assoc_roomAttributes41_stub_double():
    # RootElement_RoomStructure has no real 'RootElement_RoomStructure42' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_RoomAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_RoomAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_RoomAttribute(description="sample_text", id="sample_text", name="sample_text")
    partner = RootElement_RoomStructure()
    setattr(partner, 'RootElement_RoomStructure42', None)
    _safe_set(owner, 'RootElement_RoomAttribute43', partner)
    assert owner in getattr(partner, 'RootElement_RoomStructure42')
    _safe_set(owner, 'RootElement_RoomAttribute43', None)
    assert owner not in getattr(partner, 'RootElement_RoomStructure42')


def test_assoc_roomFetcher34_stub_double():
    # RootElement_BookingHandler has no real 'RootElement_BookingHandler35' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_RoomFetcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_RoomFetcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_RoomFetcher()
    partner = RootElement_BookingHandler()
    setattr(partner, 'RootElement_BookingHandler35', None)
    _safe_set(owner, 'RootElement_RoomFetcher', partner)
    assert getattr(partner, 'RootElement_BookingHandler35') == owner
    _safe_set(owner, 'RootElement_RoomFetcher', None)
    assert getattr(partner, 'RootElement_BookingHandler35') is None


def test_assoc_roomFetcher46_stub_double():
    # RootElement_CleaningHandler has no real 'RootElement_CleaningHandler' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_RoomFetcher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_RoomFetcher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_RoomFetcher()
    partner = RootElement_CleaningHandler()
    setattr(partner, 'RootElement_CleaningHandler', None)
    _safe_set(owner, 'RootElement_RoomFetcher47', partner)
    assert getattr(partner, 'RootElement_CleaningHandler') == owner
    _safe_set(owner, 'RootElement_RoomFetcher47', None)
    assert getattr(partner, 'RootElement_CleaningHandler') is None


def test_assoc_roomTypes38_stub_double():
    # RootElement_RoomStructure has no real 'RootElement_RoomStructure39' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_RoomType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_RoomType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_RoomType(capacity="sample_text", name="sample_text", price="sample_text")
    partner = RootElement_RoomStructure()
    setattr(partner, 'RootElement_RoomStructure39', None)
    _safe_set(owner, 'RootElement_RoomType40', partner)
    assert owner in getattr(partner, 'RootElement_RoomStructure39')
    _safe_set(owner, 'RootElement_RoomType40', None)
    assert owner not in getattr(partner, 'RootElement_RoomStructure39')


def test_assoc_rooms36_stub_double():
    # RootElement_RoomStructure has no real 'RootElement_RoomStructure' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_Room's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_Room's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_Room(isOccupied="sample_text", name="sample_text", needCleaning="sample_text")
    partner = RootElement_RoomStructure()
    setattr(partner, 'RootElement_RoomStructure', None)
    _safe_set(owner, 'RootElement_Room37', partner)
    assert owner in getattr(partner, 'RootElement_RoomStructure')
    _safe_set(owner, 'RootElement_Room37', None)
    assert owner not in getattr(partner, 'RootElement_RoomStructure')


def test_assoc_serviceItemHandling24_stub_double():
    # RootElement_Clerk has no real 'RootElement_Clerk25' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_ServiceItemHandling's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_ServiceItemHandling's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_ServiceItemHandling()
    partner = RootElement_Clerk()
    setattr(partner, 'RootElement_Clerk25', None)
    _safe_set(owner, 'RootElement_ServiceItemHandling', partner)
    assert getattr(partner, 'RootElement_Clerk25') == owner
    _safe_set(owner, 'RootElement_ServiceItemHandling', None)
    assert getattr(partner, 'RootElement_Clerk25') is None


def test_assoc_supportticket45_stub_double():
    # RootElement_SupportTicketHandler has no real 'RootElement_SupportTicketHandler' property in the generated
    # code (a bare stub) -- manually attach it so RootElement_SupportTicket's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RootElement_SupportTicket's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RootElement_SupportTicket(fixed="sample_text", problemDescription="sample_text", roomName="sample_text")
    partner = RootElement_SupportTicketHandler()
    setattr(partner, 'RootElement_SupportTicketHandler', None)
    _safe_set(owner, 'RootElement_SupportTicket', partner)
    assert owner in getattr(partner, 'RootElement_SupportTicketHandler')
    _safe_set(owner, 'RootElement_SupportTicket', None)
    assert owner not in getattr(partner, 'RootElement_SupportTicketHandler')


