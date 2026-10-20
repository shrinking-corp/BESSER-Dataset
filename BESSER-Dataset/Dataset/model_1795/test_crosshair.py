from python_code import RootElement_DailyRoomBooking

def test_RootElement_DailyRoomBooking___init__():
    assert RootElement_DailyRoomBooking.__init__(RootElement_DailyRoomBooking(''), '') == None


from python_code import RootElement_Feedback
from python_code import RootElement_FeedbackHandler

def test_RootElement_Feedback___init__():
    assert RootElement_Feedback.__init__(RootElement_Feedback('', '', '\x00\x00', RootElement_Feedback=RootElement_FeedbackHandler()), '', '', '', RootElement_Feedback=RootElement_FeedbackHandler()) == None


from python_code import RootElement_FeedbackReader
from python_code import RootElement_Manager

def test_RootElement_FeedbackReader___init__():
    assert RootElement_FeedbackReader.__init__(RootElement_FeedbackReader(RootElement_FeedbackReader=RootElement_Manager()), RootElement_FeedbackReader=RootElement_Manager()) == None

def test_RootElement_FeedbackReader_getUnreadFeedback():
    assert RootElement_FeedbackReader.getUnreadFeedback(RootElement_FeedbackReader(RootElement_FeedbackReader=RootElement_Manager())) == None

def test_RootElement_FeedbackReader_getAllFeedback():
    assert RootElement_FeedbackReader.getAllFeedback(RootElement_FeedbackReader(RootElement_FeedbackReader=RootElement_Manager())) == None


from python_code import RootElement_HotelSystem

def test_RootElement_HotelSystem___init__():
    assert RootElement_HotelSystem.__init__(RootElement_HotelSystem()) == None

def test_RootElement_HotelSystem_getNationality():
    assert RootElement_HotelSystem.getNationality(RootElement_HotelSystem()) == None

def test_RootElement_HotelSystem_getStaff():
    assert RootElement_HotelSystem.getStaff(RootElement_HotelSystem(), '') == None

def test_RootElement_HotelSystem_getName():
    assert RootElement_HotelSystem.getName(RootElement_HotelSystem()) == None

def test_RootElement_HotelSystem_getManager():
    assert RootElement_HotelSystem.getManager(RootElement_HotelSystem(), '') == None

def test_RootElement_HotelSystem_getSystemAdministrator():
    assert RootElement_HotelSystem.getSystemAdministrator(RootElement_HotelSystem()) == None

def test_RootElement_HotelSystem_getGuest():
    assert RootElement_HotelSystem.getGuest(RootElement_HotelSystem()) == None

def test_RootElement_HotelSystem_getClerk():
    assert RootElement_HotelSystem.getClerk(RootElement_HotelSystem(), '') == None


from python_code import RootElement_Clerk
from python_code import RootElement_Payment

def test_RootElement_Payment___init__():
    assert RootElement_Payment.__init__(RootElement_Payment(RootElement_Payment=RootElement_Clerk()), RootElement_Payment=RootElement_Clerk()) == None

def test_RootElement_Payment_verifyCreditCard():
    assert RootElement_Payment.verifyCreditCard(RootElement_Payment(RootElement_Payment=RootElement_Clerk()), '') == None

def test_RootElement_Payment_debitCard():
    assert RootElement_Payment.debitCard(RootElement_Payment(RootElement_Payment=RootElement_Clerk()), '', '') == None


from python_code import RootElement_Clerk
from python_code import RootElement_ReceptionHandling

def test_RootElement_ReceptionHandling___init__():
    assert RootElement_ReceptionHandling.__init__(RootElement_ReceptionHandling(RootElement_ReceptionHandling=RootElement_Clerk()), RootElement_ReceptionHandling=RootElement_Clerk()) == None

def test_RootElement_ReceptionHandling_findActiveBooking():
    assert RootElement_ReceptionHandling.findActiveBooking(RootElement_ReceptionHandling(RootElement_ReceptionHandling=RootElement_Clerk()), '') == None

def test_RootElement_ReceptionHandling_findBookings():
    assert RootElement_ReceptionHandling.findBookings(RootElement_ReceptionHandling(RootElement_ReceptionHandling=RootElement_Clerk()), '') == None

def test_RootElement_ReceptionHandling_checkIn():
    assert RootElement_ReceptionHandling.checkIn(RootElement_ReceptionHandling(RootElement_ReceptionHandling=RootElement_Clerk()), '') == None

def test_RootElement_ReceptionHandling_checkOut():
    assert RootElement_ReceptionHandling.checkOut(RootElement_ReceptionHandling(RootElement_ReceptionHandling=RootElement_Clerk()), '') == None


from python_code import RootElement_RoomAttributeHandling

def test_RootElement_RoomAttributeHandling___init__():
    assert RootElement_RoomAttributeHandling.__init__(RootElement_RoomAttributeHandling()) == None

def test_RootElement_RoomAttributeHandling_editRoomAttribute():
    assert RootElement_RoomAttributeHandling.editRoomAttribute(RootElement_RoomAttributeHandling(), '', '', '') == None

def test_RootElement_RoomAttributeHandling_removeRoomAttribute():
    assert RootElement_RoomAttributeHandling.removeRoomAttribute(RootElement_RoomAttributeHandling(), '') == None

def test_RootElement_RoomAttributeHandling_addRoomAttribute():
    assert RootElement_RoomAttributeHandling.addRoomAttribute(RootElement_RoomAttributeHandling(), '', '') == None

def test_RootElement_RoomAttributeHandling_findRoomAttribute():
    assert RootElement_RoomAttributeHandling.findRoomAttribute(RootElement_RoomAttributeHandling(), '') == None

def test_RootElement_RoomAttributeHandling_getAllRoomAttributes():
    assert RootElement_RoomAttributeHandling.getAllRoomAttributes(RootElement_RoomAttributeHandling()) == None


from python_code import RootElement_BookingHandler
from python_code import RootElement_CleaningHandler
from python_code import RootElement_RoomFetcher

def test_RootElement_RoomFetcher___init__():
    assert RootElement_RoomFetcher.__init__(RootElement_RoomFetcher(RootElement_RoomFetcher=RootElement_BookingHandler(), RootElement_RoomFetcher47=RootElement_CleaningHandler()), RootElement_RoomFetcher=RootElement_BookingHandler(), RootElement_RoomFetcher47=RootElement_CleaningHandler()) == None

def test_RootElement_RoomFetcher_getBookableRooms():
    assert RootElement_RoomFetcher.getBookableRooms(RootElement_RoomFetcher(RootElement_RoomFetcher=RootElement_BookingHandler(), RootElement_RoomFetcher47=RootElement_CleaningHandler())) == None

def test_RootElement_RoomFetcher_getAllCleanableRooms():
    assert RootElement_RoomFetcher.getAllCleanableRooms(RootElement_RoomFetcher(RootElement_RoomFetcher=RootElement_BookingHandler(), RootElement_RoomFetcher47=RootElement_CleaningHandler())) == None

def test_RootElement_RoomFetcher_getAvailableRooms():
    assert RootElement_RoomFetcher.getAvailableRooms(RootElement_RoomFetcher(RootElement_RoomFetcher=RootElement_BookingHandler(), RootElement_RoomFetcher47=RootElement_CleaningHandler())) == None


from python_code import RootElement_RoomHandling

def test_RootElement_RoomHandling___init__():
    assert RootElement_RoomHandling.__init__(RootElement_RoomHandling()) == None

def test_RootElement_RoomHandling_findRoom():
    assert RootElement_RoomHandling.findRoom(RootElement_RoomHandling(), '') == None

def test_RootElement_RoomHandling_removeRoom():
    assert RootElement_RoomHandling.removeRoom(RootElement_RoomHandling(), '') == None

def test_RootElement_RoomHandling_getAllRooms():
    assert RootElement_RoomHandling.getAllRooms(RootElement_RoomHandling()) == None

def test_RootElement_RoomHandling_addRoom():
    assert RootElement_RoomHandling.addRoom(RootElement_RoomHandling(), '', '') == None

def test_RootElement_RoomHandling_editRoom():
    assert RootElement_RoomHandling.editRoom(RootElement_RoomHandling(), '', '', '') == None


from python_code import RootElement_RoomTypeHandling

def test_RootElement_RoomTypeHandling___init__():
    assert RootElement_RoomTypeHandling.__init__(RootElement_RoomTypeHandling()) == None

def test_RootElement_RoomTypeHandling_editRoomType():
    assert RootElement_RoomTypeHandling.editRoomType(RootElement_RoomTypeHandling(), '', '', '', '') == None

def test_RootElement_RoomTypeHandling_removeAttributeFromRoomType():
    assert RootElement_RoomTypeHandling.removeAttributeFromRoomType(RootElement_RoomTypeHandling(), '', '') == None

def test_RootElement_RoomTypeHandling_addAttributeToRoomType():
    assert RootElement_RoomTypeHandling.addAttributeToRoomType(RootElement_RoomTypeHandling(), '', '') == None

def test_RootElement_RoomTypeHandling_removeRoomType():
    assert RootElement_RoomTypeHandling.removeRoomType(RootElement_RoomTypeHandling(), '') == None

def test_RootElement_RoomTypeHandling_findRoomType():
    assert RootElement_RoomTypeHandling.findRoomType(RootElement_RoomTypeHandling(), '') == None

def test_RootElement_RoomTypeHandling_getAllRoomTypes():
    assert RootElement_RoomTypeHandling.getAllRoomTypes(RootElement_RoomTypeHandling()) == None

def test_RootElement_RoomTypeHandling_addRoomType():
    assert RootElement_RoomTypeHandling.addRoomType(RootElement_RoomTypeHandling(), '', '', '') == None


from python_code import RootElement_Clerk
from python_code import RootElement_ServiceItemHandling

def test_RootElement_ServiceItemHandling___init__():
    assert RootElement_ServiceItemHandling.__init__(RootElement_ServiceItemHandling(RootElement_ServiceItemHandling=RootElement_Clerk()), RootElement_ServiceItemHandling=RootElement_Clerk()) == None

def test_RootElement_ServiceItemHandling_findAllServiceItems():
    assert RootElement_ServiceItemHandling.findAllServiceItems(RootElement_ServiceItemHandling(RootElement_ServiceItemHandling=RootElement_Clerk()), '') == None

def test_RootElement_ServiceItemHandling_addServiceItem():
    assert RootElement_ServiceItemHandling.addServiceItem(RootElement_ServiceItemHandling(RootElement_ServiceItemHandling=RootElement_Clerk()), '', '', '', '') == None

def test_RootElement_ServiceItemHandling_removeServiceItem():
    assert RootElement_ServiceItemHandling.removeServiceItem(RootElement_ServiceItemHandling(RootElement_ServiceItemHandling=RootElement_Clerk()), '', '') == None


from python_code import RootElement_SupportTicket
from python_code import RootElement_SupportTicketHandler

def test_RootElement_SupportTicket___init__():
    assert RootElement_SupportTicket.__init__(RootElement_SupportTicket('', '', '\x00\x00', RootElement_SupportTicket=RootElement_SupportTicketHandler()), '', '', '', RootElement_SupportTicket=RootElement_SupportTicketHandler()) == None

