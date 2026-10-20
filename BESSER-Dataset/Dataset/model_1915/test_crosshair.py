from python_code import se_bookingSystem_AbstractEvent

def test_se_bookingSystem_AbstractEvent___init__():
    assert se_bookingSystem_AbstractEvent.__init__(se_bookingSystem_AbstractEvent('', '', 0), '\x00', '', 0) == None


from python_code import se_bookingSystem_Booking

def test_se_bookingSystem_Booking___init__():
    assert se_bookingSystem_Booking.__init__(se_bookingSystem_Booking(0, '', '', '', '\x00', se_bookingSystem_Booking=set(), se_bookingSystem_Booking10=set()), 0, '', '', '', '', se_bookingSystem_Booking=set(), se_bookingSystem_Booking10=set()) == None


from python_code import roomManager_IHotelRoomProvider
from python_code import se_bookingSystem_BookingSystem
from python_code import se_roomManager_RoomManager

def test_se_bookingSystem_BookingSystem___init__():
    assert se_bookingSystem_BookingSystem.__init__(se_bookingSystem_BookingSystem(0, se_bookingSystem_BookingSystem=set(), se_bookingSystem_BookingSystem2=set(), se_bookingSystem_BookingSystem4=se_roomManager_RoomManager(), se_bookingSystem_BookingSystem6=set()), 0, se_bookingSystem_BookingSystem=set(), se_bookingSystem_BookingSystem2=set(), se_bookingSystem_BookingSystem4=roomManager_IHotelRoomProvider(), se_bookingSystem_BookingSystem6=set()) == None


from python_code import se_bookingSystem_FreeRoomTypesDTO

def test_se_bookingSystem_FreeRoomTypesDTO___init__():
    assert se_bookingSystem_FreeRoomTypesDTO.__init__(se_bookingSystem_FreeRoomTypesDTO('', 0, 0.0, 0), '', 0, 0.0, 0) == None


from python_code import se_bookingSystem_IBooking

def test_se_bookingSystem_IBooking___init__():
    assert se_bookingSystem_IBooking.__init__(se_bookingSystem_IBooking()) == None

def test_se_bookingSystem_IBooking_setEndDate():
    assert se_bookingSystem_IBooking.setEndDate(se_bookingSystem_IBooking(), '') == None

def test_se_bookingSystem_IBooking_checkInRoom():
    assert se_bookingSystem_IBooking.checkInRoom(se_bookingSystem_IBooking(), '') == None

def test_se_bookingSystem_IBooking_getStartDate():
    assert se_bookingSystem_IBooking.getStartDate(se_bookingSystem_IBooking()) == None

def test_se_bookingSystem_IBooking_getEndDate():
    assert se_bookingSystem_IBooking.getEndDate(se_bookingSystem_IBooking()) == None

def test_se_bookingSystem_IBooking_addRoom():
    assert se_bookingSystem_IBooking.addRoom(se_bookingSystem_IBooking(), '') == None

def test_se_bookingSystem_IBooking_setRooms():
    assert se_bookingSystem_IBooking.setRooms(se_bookingSystem_IBooking(), '') == None

def test_se_bookingSystem_IBooking_checkOutRoom():
    assert se_bookingSystem_IBooking.checkOutRoom(se_bookingSystem_IBooking(), '') == None

def test_se_bookingSystem_IBooking_getRooms():
    assert se_bookingSystem_IBooking.getRooms(se_bookingSystem_IBooking()) == None

def test_se_bookingSystem_IBooking_setStartDate():
    assert se_bookingSystem_IBooking.setStartDate(se_bookingSystem_IBooking(), '') == None

def test_se_bookingSystem_IBooking_getLastName():
    assert se_bookingSystem_IBooking.getLastName(se_bookingSystem_IBooking()) == None

def test_se_bookingSystem_IBooking_getFirstName():
    assert se_bookingSystem_IBooking.getFirstName(se_bookingSystem_IBooking()) == None

def test_se_bookingSystem_IBooking_getID():
    assert se_bookingSystem_IBooking.getID(se_bookingSystem_IBooking()) == None

def test_se_bookingSystem_IBooking_getCheckedInRooms():
    assert se_bookingSystem_IBooking.getCheckedInRooms(se_bookingSystem_IBooking()) == None


from python_code import se_bookingSystem_IEvent

def test_se_bookingSystem_IEvent___init__():
    assert se_bookingSystem_IEvent.__init__(se_bookingSystem_IEvent()) == None

def test_se_bookingSystem_IEvent_getType():
    assert se_bookingSystem_IEvent.getType(se_bookingSystem_IEvent()) == None

def test_se_bookingSystem_IEvent_getTimestamp():
    assert se_bookingSystem_IEvent.getTimestamp(se_bookingSystem_IEvent()) == None

def test_se_bookingSystem_IEvent_getBookingId():
    assert se_bookingSystem_IEvent.getBookingId(se_bookingSystem_IEvent()) == None


from python_code import se_bookingSystem_IHotelBookingManager

def test_se_bookingSystem_IHotelBookingManager___init__():
    assert se_bookingSystem_IHotelBookingManager.__init__(se_bookingSystem_IHotelBookingManager()) == None

def test_se_bookingSystem_IHotelBookingManager_editBookingRooms():
    assert se_bookingSystem_IHotelBookingManager.editBookingRooms(se_bookingSystem_IHotelBookingManager(), '', '', '') == None

def test_se_bookingSystem_IHotelBookingManager_listBooking():
    assert se_bookingSystem_IHotelBookingManager.listBooking(se_bookingSystem_IHotelBookingManager()) == None

def test_se_bookingSystem_IHotelBookingManager_cancelBooking():
    assert se_bookingSystem_IHotelBookingManager.cancelBooking(se_bookingSystem_IHotelBookingManager(), '') == None

def test_se_bookingSystem_IHotelBookingManager_listCheckouts():
    assert se_bookingSystem_IHotelBookingManager.listCheckouts(se_bookingSystem_IHotelBookingManager(), '', '') == None

def test_se_bookingSystem_IHotelBookingManager_addExtraCostToRoom():
    assert se_bookingSystem_IHotelBookingManager.addExtraCostToRoom(se_bookingSystem_IHotelBookingManager(), '', '', '', '') == None

def test_se_bookingSystem_IHotelBookingManager_editBookingPeriod():
    assert se_bookingSystem_IHotelBookingManager.editBookingPeriod(se_bookingSystem_IHotelBookingManager(), '', '', '') == None

def test_se_bookingSystem_IHotelBookingManager_listOccupiedRooms():
    assert se_bookingSystem_IHotelBookingManager.listOccupiedRooms(se_bookingSystem_IHotelBookingManager(), '') == None

def test_se_bookingSystem_IHotelBookingManager_listCheckins():
    assert se_bookingSystem_IHotelBookingManager.listCheckins(se_bookingSystem_IHotelBookingManager(), '', '') == None

def test_se_bookingSystem_IHotelBookingManager_initiateCheckin():
    assert se_bookingSystem_IHotelBookingManager.initiateCheckin(se_bookingSystem_IHotelBookingManager(), '') == None


from python_code import se_bookingSystem_IHotelCustomerProvides

def test_se_bookingSystem_IHotelCustomerProvides___init__():
    assert se_bookingSystem_IHotelCustomerProvides.__init__(se_bookingSystem_IHotelCustomerProvides()) == None

def test_se_bookingSystem_IHotelCustomerProvides_initiateRoomCheckout():
    assert se_bookingSystem_IHotelCustomerProvides.initiateRoomCheckout(se_bookingSystem_IHotelCustomerProvides(), '', '') == None

def test_se_bookingSystem_IHotelCustomerProvides_payRoomDuringCheckout():
    assert se_bookingSystem_IHotelCustomerProvides.payRoomDuringCheckout(se_bookingSystem_IHotelCustomerProvides(), '', '', '', '', '', '', '') == None

def test_se_bookingSystem_IHotelCustomerProvides_payDuringCheckout():
    assert se_bookingSystem_IHotelCustomerProvides.payDuringCheckout(se_bookingSystem_IHotelCustomerProvides(), '', '', '', '', '', '') == None

def test_se_bookingSystem_IHotelCustomerProvides_addRoomToBooking():
    assert se_bookingSystem_IHotelCustomerProvides.addRoomToBooking(se_bookingSystem_IHotelCustomerProvides(), '', '') == None

def test_se_bookingSystem_IHotelCustomerProvides_confirmBooking():
    assert se_bookingSystem_IHotelCustomerProvides.confirmBooking(se_bookingSystem_IHotelCustomerProvides(), '') == None

def test_se_bookingSystem_IHotelCustomerProvides_initiateBooking():
    assert se_bookingSystem_IHotelCustomerProvides.initiateBooking(se_bookingSystem_IHotelCustomerProvides(), '', '', '', '') == None

def test_se_bookingSystem_IHotelCustomerProvides_initiateCheckout():
    assert se_bookingSystem_IHotelCustomerProvides.initiateCheckout(se_bookingSystem_IHotelCustomerProvides(), '') == None

def test_se_bookingSystem_IHotelCustomerProvides_getFreeRooms():
    assert se_bookingSystem_IHotelCustomerProvides.getFreeRooms(se_bookingSystem_IHotelCustomerProvides(), '', '', '') == None

def test_se_bookingSystem_IHotelCustomerProvides_checkInRoom():
    assert se_bookingSystem_IHotelCustomerProvides.checkInRoom(se_bookingSystem_IHotelCustomerProvides(), '', '') == None


from python_code import se_roomManager_IHotelRoomManager

def test_se_roomManager_IHotelRoomManager___init__():
    assert se_roomManager_IHotelRoomManager.__init__(se_roomManager_IHotelRoomManager()) == None

def test_se_roomManager_IHotelRoomManager_removeRoom():
    assert se_roomManager_IHotelRoomManager.removeRoom(se_roomManager_IHotelRoomManager(), '') == None

def test_se_roomManager_IHotelRoomManager_addRoom():
    assert se_roomManager_IHotelRoomManager.addRoom(se_roomManager_IHotelRoomManager(), '', '') == None

def test_se_roomManager_IHotelRoomManager_changeRoomType():
    assert se_roomManager_IHotelRoomManager.changeRoomType(se_roomManager_IHotelRoomManager(), '', '') == None

def test_se_roomManager_IHotelRoomManager_addRoomType():
    assert se_roomManager_IHotelRoomManager.addRoomType(se_roomManager_IHotelRoomManager(), '', '', '', '') == None

def test_se_roomManager_IHotelRoomManager_blockRoom():
    assert se_roomManager_IHotelRoomManager.blockRoom(se_roomManager_IHotelRoomManager(), '') == None

def test_se_roomManager_IHotelRoomManager_unblockRoom():
    assert se_roomManager_IHotelRoomManager.unblockRoom(se_roomManager_IHotelRoomManager(), '') == None

def test_se_roomManager_IHotelRoomManager_updateRoomType():
    assert se_roomManager_IHotelRoomManager.updateRoomType(se_roomManager_IHotelRoomManager(), '', '', '', '', '') == None

def test_se_roomManager_IHotelRoomManager_removeRoomType():
    assert se_roomManager_IHotelRoomManager.removeRoomType(se_roomManager_IHotelRoomManager(), '') == None

def test_se_roomManager_IHotelRoomManager_getRoomTypes():
    assert se_roomManager_IHotelRoomManager.getRoomTypes(se_roomManager_IHotelRoomManager()) == None


from python_code import se_roomManager_IHotelRoomProvider

def test_se_roomManager_IHotelRoomProvider___init__():
    assert se_roomManager_IHotelRoomProvider.__init__(se_roomManager_IHotelRoomProvider()) == None

def test_se_roomManager_IHotelRoomProvider_getRooms():
    assert se_roomManager_IHotelRoomProvider.getRooms(se_roomManager_IHotelRoomProvider()) == None


from python_code import se_roomManager_IHotelStartupProvies

def test_se_roomManager_IHotelStartupProvies___init__():
    assert se_roomManager_IHotelStartupProvies.__init__(se_roomManager_IHotelStartupProvies()) == None

def test_se_roomManager_IHotelStartupProvies_startup():
    assert se_roomManager_IHotelStartupProvies.startup(se_roomManager_IHotelStartupProvies(), '') == None


from python_code import se_roomManager_IRoom

def test_se_roomManager_IRoom___init__():
    assert se_roomManager_IRoom.__init__(se_roomManager_IRoom()) == None

def test_se_roomManager_IRoom_getRoomNumber():
    assert se_roomManager_IRoom.getRoomNumber(se_roomManager_IRoom()) == None

def test_se_roomManager_IRoom_setOccupied():
    assert se_roomManager_IRoom.setOccupied(se_roomManager_IRoom(), '') == None

def test_se_roomManager_IRoom_getExtraCostDescription():
    assert se_roomManager_IRoom.getExtraCostDescription(se_roomManager_IRoom()) == None

def test_se_roomManager_IRoom_addExtraCost():
    assert se_roomManager_IRoom.addExtraCost(se_roomManager_IRoom(), '') == None

def test_se_roomManager_IRoom_isBlocked():
    assert se_roomManager_IRoom.isBlocked(se_roomManager_IRoom()) == None

def test_se_roomManager_IRoom_setExtraCostDescription():
    assert se_roomManager_IRoom.setExtraCostDescription(se_roomManager_IRoom(), '') == None

def test_se_roomManager_IRoom_getExtraCostPrice():
    assert se_roomManager_IRoom.getExtraCostPrice(se_roomManager_IRoom()) == None

def test_se_roomManager_IRoom_setRoomType():
    assert se_roomManager_IRoom.setRoomType(se_roomManager_IRoom(), '') == None

def test_se_roomManager_IRoom_setIsBlocked():
    assert se_roomManager_IRoom.setIsBlocked(se_roomManager_IRoom(), '') == None

def test_se_roomManager_IRoom_getRoomType():
    assert se_roomManager_IRoom.getRoomType(se_roomManager_IRoom()) == None

def test_se_roomManager_IRoom_isOccupied():
    assert se_roomManager_IRoom.isOccupied(se_roomManager_IRoom()) == None


from python_code import se_roomManager_IRoomType

def test_se_roomManager_IRoomType___init__():
    assert se_roomManager_IRoomType.__init__(se_roomManager_IRoomType()) == None

def test_se_roomManager_IRoomType_getNumberOfBeds():
    assert se_roomManager_IRoomType.getNumberOfBeds(se_roomManager_IRoomType()) == None

def test_se_roomManager_IRoomType_getDescription():
    assert se_roomManager_IRoomType.getDescription(se_roomManager_IRoomType()) == None

def test_se_roomManager_IRoomType_getPrice():
    assert se_roomManager_IRoomType.getPrice(se_roomManager_IRoomType()) == None

def test_se_roomManager_IRoomType_setDescription():
    assert se_roomManager_IRoomType.setDescription(se_roomManager_IRoomType(), '') == None

def test_se_roomManager_IRoomType_getName():
    assert se_roomManager_IRoomType.getName(se_roomManager_IRoomType()) == None

def test_se_roomManager_IRoomType_setPrice():
    assert se_roomManager_IRoomType.setPrice(se_roomManager_IRoomType(), '') == None

def test_se_roomManager_IRoomType_setName():
    assert se_roomManager_IRoomType.setName(se_roomManager_IRoomType(), '') == None

def test_se_roomManager_IRoomType_setNumberOfBeds():
    assert se_roomManager_IRoomType.setNumberOfBeds(se_roomManager_IRoomType(), '') == None


from python_code import roomManager_IRoomType
from python_code import se_roomManager_Room

def test_se_roomManager_Room___init__():
    assert se_roomManager_Room.__init__(se_roomManager_Room(0, False, '', 0.0, False, se_roomManager_Room=roomManager_IRoomType()), 0, False, '', 0.0, False, se_roomManager_Room=roomManager_IRoomType()) == None


from python_code import se_roomManager_RoomType

def test_se_roomManager_RoomType___init__():
    assert se_roomManager_RoomType.__init__(se_roomManager_RoomType('', 0.0, '', 0), '', 0.0, '', 0) == None

