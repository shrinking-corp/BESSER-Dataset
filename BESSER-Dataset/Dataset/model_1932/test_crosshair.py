from python_code import se_bankcomponents_IAdministratorProvides

def test_se_bankcomponents_IAdministratorProvides___init__():
    assert se_bankcomponents_IAdministratorProvides.__init__(se_bankcomponents_IAdministratorProvides()) == None

def test_se_bankcomponents_IAdministratorProvides_addCreditCard():
    assert se_bankcomponents_IAdministratorProvides.addCreditCard(se_bankcomponents_IAdministratorProvides(), '', '', '', '', '', '') == None

def test_se_bankcomponents_IAdministratorProvides_getBalance():
    assert se_bankcomponents_IAdministratorProvides.getBalance(se_bankcomponents_IAdministratorProvides(), '', '', '', '', '', '') == None

def test_se_bankcomponents_IAdministratorProvides_removeCreditCard():
    assert se_bankcomponents_IAdministratorProvides.removeCreditCard(se_bankcomponents_IAdministratorProvides(), '', '', '', '', '', '') == None

def test_se_bankcomponents_IAdministratorProvides_makeDeposit():
    assert se_bankcomponents_IAdministratorProvides.makeDeposit(se_bankcomponents_IAdministratorProvides(), '', '', '', '', '', '', '') == None


from python_code import se_bankcomponents_ICustomerProvides

def test_se_bankcomponents_ICustomerProvides___init__():
    assert se_bankcomponents_ICustomerProvides.__init__(se_bankcomponents_ICustomerProvides()) == None

def test_se_bankcomponents_ICustomerProvides_makePayment():
    assert se_bankcomponents_ICustomerProvides.makePayment(se_bankcomponents_ICustomerProvides(), '', '', '', '', '', '', '') == None

def test_se_bankcomponents_ICustomerProvides_isCreditCardValid():
    assert se_bankcomponents_ICustomerProvides.isCreditCardValid(se_bankcomponents_ICustomerProvides(), '', '', '', '', '', '') == None


from python_code import hotelsystem_RoomReservation
from python_code import se_hotelsystem_Bill

def test_se_hotelsystem_Bill___init__():
    assert se_hotelsystem_Bill.__init__(se_hotelsystem_Bill(0.0, 0, se_hotelsystem_Bill=hotelsystem_RoomReservation()), 0.0, 0, se_hotelsystem_Bill=hotelsystem_RoomReservation()) == None


from python_code import hotelsystem_IRoomHandler
from python_code import hotelsystem_PaymentHandler
from python_code import se_actor_Receptionist
from python_code import se_hotelsystem_BookingHandler

def test_se_hotelsystem_BookingHandler___init__():
    assert se_hotelsystem_BookingHandler.__init__(se_hotelsystem_BookingHandler(0, 0, se_hotelsystem_BookingHandler=set(), se_hotelsystem_BookingHandler2=hotelsystem_PaymentHandler(), se_hotelsystem_BookingHandler4=hotelsystem_IRoomHandler(), hotelsystem_IHotelReceptionistProvides=se_actor_Receptionist(), hotelsystem_IHotelCustomerProvides=se_actor_Receptionist()), 0, 0, se_hotelsystem_BookingHandler=set(), se_hotelsystem_BookingHandler2=hotelsystem_PaymentHandler(), se_hotelsystem_BookingHandler4=hotelsystem_IRoomHandler(), hotelsystem_IHotelReceptionistProvides=se_actor_Receptionist(), hotelsystem_IHotelCustomerProvides=se_actor_Receptionist()) == None

def test_se_hotelsystem_BookingHandler_isFree():
    assert se_hotelsystem_BookingHandler.isFree(se_hotelsystem_BookingHandler(0, 0, se_hotelsystem_BookingHandler=set(), se_hotelsystem_BookingHandler2=hotelsystem_PaymentHandler(), se_hotelsystem_BookingHandler4=hotelsystem_IRoomHandler(), hotelsystem_IHotelReceptionistProvides=se_actor_Receptionist(), hotelsystem_IHotelCustomerProvides=se_actor_Receptionist()), '', 0, '') == None

def test_se_hotelsystem_BookingHandler_getBookingById():
    assert se_hotelsystem_BookingHandler.getBookingById(se_hotelsystem_BookingHandler(0, 0, se_hotelsystem_BookingHandler=set(), se_hotelsystem_BookingHandler2=hotelsystem_PaymentHandler(), se_hotelsystem_BookingHandler4=hotelsystem_IRoomHandler(), hotelsystem_IHotelReceptionistProvides=se_actor_Receptionist(), hotelsystem_IHotelCustomerProvides=se_actor_Receptionist()), '') == None


from python_code import se_hotelsystem_Customer

def test_se_hotelsystem_Customer___init__():
    assert se_hotelsystem_Customer.__init__(se_hotelsystem_Customer('', '\x00'), '\x00\x00', '') == None


from python_code import se_hotelsystem_FreeRoomTypesDTO

def test_se_hotelsystem_FreeRoomTypesDTO___init__():
    assert se_hotelsystem_FreeRoomTypesDTO.__init__(se_hotelsystem_FreeRoomTypesDTO('', 0, 0.0, 0), '', 0, 0.0, 0) == None


from python_code import se_hotelsystem_IHotelAdministratorProvides

def test_se_hotelsystem_IHotelAdministratorProvides___init__():
    assert se_hotelsystem_IHotelAdministratorProvides.__init__(se_hotelsystem_IHotelAdministratorProvides()) == None

def test_se_hotelsystem_IHotelAdministratorProvides_blockRoom():
    assert se_hotelsystem_IHotelAdministratorProvides.blockRoom(se_hotelsystem_IHotelAdministratorProvides(), '') == None

def test_se_hotelsystem_IHotelAdministratorProvides_unblockRoom():
    assert se_hotelsystem_IHotelAdministratorProvides.unblockRoom(se_hotelsystem_IHotelAdministratorProvides(), '') == None

def test_se_hotelsystem_IHotelAdministratorProvides_addRoom():
    assert se_hotelsystem_IHotelAdministratorProvides.addRoom(se_hotelsystem_IHotelAdministratorProvides(), '', '') == None

def test_se_hotelsystem_IHotelAdministratorProvides_removeRoom():
    assert se_hotelsystem_IHotelAdministratorProvides.removeRoom(se_hotelsystem_IHotelAdministratorProvides(), '') == None

def test_se_hotelsystem_IHotelAdministratorProvides_changeRoomType():
    assert se_hotelsystem_IHotelAdministratorProvides.changeRoomType(se_hotelsystem_IHotelAdministratorProvides(), '', '') == None

def test_se_hotelsystem_IHotelAdministratorProvides_editRoomType():
    assert se_hotelsystem_IHotelAdministratorProvides.editRoomType(se_hotelsystem_IHotelAdministratorProvides(), '', '', '', '') == None

def test_se_hotelsystem_IHotelAdministratorProvides_addRoomType():
    assert se_hotelsystem_IHotelAdministratorProvides.addRoomType(se_hotelsystem_IHotelAdministratorProvides(), '', '', '', '') == None

def test_se_hotelsystem_IHotelAdministratorProvides_removeRoomType():
    assert se_hotelsystem_IHotelAdministratorProvides.removeRoomType(se_hotelsystem_IHotelAdministratorProvides(), '') == None


from python_code import se_hotelsystem_IHotelCustomerProvides

def test_se_hotelsystem_IHotelCustomerProvides___init__():
    assert se_hotelsystem_IHotelCustomerProvides.__init__(se_hotelsystem_IHotelCustomerProvides()) == None

def test_se_hotelsystem_IHotelCustomerProvides_addRoomToBooking():
    assert se_hotelsystem_IHotelCustomerProvides.addRoomToBooking(se_hotelsystem_IHotelCustomerProvides(), '', '') == None

def test_se_hotelsystem_IHotelCustomerProvides_getFreeRooms():
    assert se_hotelsystem_IHotelCustomerProvides.getFreeRooms(se_hotelsystem_IHotelCustomerProvides(), '', '', '') == None

def test_se_hotelsystem_IHotelCustomerProvides_confirmBooking():
    assert se_hotelsystem_IHotelCustomerProvides.confirmBooking(se_hotelsystem_IHotelCustomerProvides(), '') == None

def test_se_hotelsystem_IHotelCustomerProvides_payDuringCheckout():
    assert se_hotelsystem_IHotelCustomerProvides.payDuringCheckout(se_hotelsystem_IHotelCustomerProvides(), '', '', '', '', '', '') == None

def test_se_hotelsystem_IHotelCustomerProvides_payRoomDuringCheckout():
    assert se_hotelsystem_IHotelCustomerProvides.payRoomDuringCheckout(se_hotelsystem_IHotelCustomerProvides(), '', '', '', '', '', '', '') == None

def test_se_hotelsystem_IHotelCustomerProvides_initiateRoomCheckout():
    assert se_hotelsystem_IHotelCustomerProvides.initiateRoomCheckout(se_hotelsystem_IHotelCustomerProvides(), '', '') == None

def test_se_hotelsystem_IHotelCustomerProvides_checkInRoom():
    assert se_hotelsystem_IHotelCustomerProvides.checkInRoom(se_hotelsystem_IHotelCustomerProvides(), '', '') == None

def test_se_hotelsystem_IHotelCustomerProvides_initiateBooking():
    assert se_hotelsystem_IHotelCustomerProvides.initiateBooking(se_hotelsystem_IHotelCustomerProvides(), '', '', '', '') == None

def test_se_hotelsystem_IHotelCustomerProvides_initiateCheckout():
    assert se_hotelsystem_IHotelCustomerProvides.initiateCheckout(se_hotelsystem_IHotelCustomerProvides(), '') == None


from python_code import se_hotelsystem_IHotelReceptionistProvides

def test_se_hotelsystem_IHotelReceptionistProvides___init__():
    assert se_hotelsystem_IHotelReceptionistProvides.__init__(se_hotelsystem_IHotelReceptionistProvides()) == None

def test_se_hotelsystem_IHotelReceptionistProvides_getFreeRoom():
    assert se_hotelsystem_IHotelReceptionistProvides.getFreeRoom(se_hotelsystem_IHotelReceptionistProvides(), '', '', '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_checkIn():
    assert se_hotelsystem_IHotelReceptionistProvides.checkIn(se_hotelsystem_IHotelReceptionistProvides(), '', '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_listFreeRooms():
    assert se_hotelsystem_IHotelReceptionistProvides.listFreeRooms(se_hotelsystem_IHotelReceptionistProvides(), '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_addExtraToRoom():
    assert se_hotelsystem_IHotelReceptionistProvides.addExtraToRoom(se_hotelsystem_IHotelReceptionistProvides(), '', '', '', '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_listCheckins():
    assert se_hotelsystem_IHotelReceptionistProvides.listCheckins(se_hotelsystem_IHotelReceptionistProvides(), '', '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_listOccupiedRooms():
    assert se_hotelsystem_IHotelReceptionistProvides.listOccupiedRooms(se_hotelsystem_IHotelReceptionistProvides(), '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_editBookingTime():
    assert se_hotelsystem_IHotelReceptionistProvides.editBookingTime(se_hotelsystem_IHotelReceptionistProvides(), '', '', '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_listCheckouts():
    assert se_hotelsystem_IHotelReceptionistProvides.listCheckouts(se_hotelsystem_IHotelReceptionistProvides(), '', '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_listBookings():
    assert se_hotelsystem_IHotelReceptionistProvides.listBookings(se_hotelsystem_IHotelReceptionistProvides()) == None

def test_se_hotelsystem_IHotelReceptionistProvides_cancelBooking():
    assert se_hotelsystem_IHotelReceptionistProvides.cancelBooking(se_hotelsystem_IHotelReceptionistProvides(), '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_removeRoomTypeFromBooking():
    assert se_hotelsystem_IHotelReceptionistProvides.removeRoomTypeFromBooking(se_hotelsystem_IHotelReceptionistProvides(), '', '', '') == None

def test_se_hotelsystem_IHotelReceptionistProvides_addRoomTypeToBooking():
    assert se_hotelsystem_IHotelReceptionistProvides.addRoomTypeToBooking(se_hotelsystem_IHotelReceptionistProvides(), '', '', '') == None


from python_code import se_hotelsystem_IHotelStartupProvides

def test_se_hotelsystem_IHotelStartupProvides___init__():
    assert se_hotelsystem_IHotelStartupProvides.__init__(se_hotelsystem_IHotelStartupProvides()) == None

def test_se_hotelsystem_IHotelStartupProvides_startup():
    assert se_hotelsystem_IHotelStartupProvides.startup(se_hotelsystem_IHotelStartupProvides(), '') == None


from python_code import se_hotelsystem_IRoomHandler

def test_se_hotelsystem_IRoomHandler___init__():
    assert se_hotelsystem_IRoomHandler.__init__(se_hotelsystem_IRoomHandler()) == None

def test_se_hotelsystem_IRoomHandler_getAllRoomsByType():
    assert se_hotelsystem_IRoomHandler.getAllRoomsByType(se_hotelsystem_IRoomHandler(), '') == None

def test_se_hotelsystem_IRoomHandler_getAllRooms():
    assert se_hotelsystem_IRoomHandler.getAllRooms(se_hotelsystem_IRoomHandler()) == None

def test_se_hotelsystem_IRoomHandler_getFreeRooms():
    assert se_hotelsystem_IRoomHandler.getFreeRooms(se_hotelsystem_IRoomHandler()) == None

def test_se_hotelsystem_IRoomHandler_getRoomType():
    assert se_hotelsystem_IRoomHandler.getRoomType(se_hotelsystem_IRoomHandler(), '') == None

def test_se_hotelsystem_IRoomHandler_getFreeRoomByType():
    assert se_hotelsystem_IRoomHandler.getFreeRoomByType(se_hotelsystem_IRoomHandler(), '') == None

def test_se_hotelsystem_IRoomHandler_getAllRoomTypes():
    assert se_hotelsystem_IRoomHandler.getAllRoomTypes(se_hotelsystem_IRoomHandler(), '') == None


from python_code import bankcomponents_ICustomerProvides
from python_code import se_hotelsystem_PaymentHandler

def test_se_hotelsystem_PaymentHandler___init__():
    assert se_hotelsystem_PaymentHandler.__init__(se_hotelsystem_PaymentHandler(se_hotelsystem_PaymentHandler=bankcomponents_ICustomerProvides()), se_hotelsystem_PaymentHandler=bankcomponents_ICustomerProvides()) == None

def test_se_hotelsystem_PaymentHandler_payIfCardValid():
    assert se_hotelsystem_PaymentHandler.payIfCardValid(se_hotelsystem_PaymentHandler(se_hotelsystem_PaymentHandler=bankcomponents_ICustomerProvides()), '', '', '', '', '', '', '') == None


from python_code import hotelsystem_RoomType
from python_code import se_hotelsystem_Room

def test_se_hotelsystem_Room___init__():
    assert se_hotelsystem_Room.__init__(se_hotelsystem_Room(False, False, 0, se_hotelsystem_Room=hotelsystem_RoomType()), False, False, 0, se_hotelsystem_Room=hotelsystem_RoomType()) == None


from python_code import se_hotelsystem_RoomExtra

def test_se_hotelsystem_RoomExtra___init__():
    assert se_hotelsystem_RoomExtra.__init__(se_hotelsystem_RoomExtra(0.0, '\x00\x00'), 0.0, '') == None


from python_code import hotelsystem_IRoomHandler
from python_code import hotelsystem_PaymentHandler
from python_code import se_actor_Administrator
from python_code import se_actor_Receptionist
from python_code import se_hotelsystem_BookingHandler
from python_code import se_hotelsystem_RoomHandler

def test_se_hotelsystem_RoomHandler___init__():
    assert se_hotelsystem_RoomHandler.__init__(se_hotelsystem_RoomHandler(se_hotelsystem_RoomHandler=set(), se_hotelsystem_RoomHandler23=set(), hotelsystem_IRoomHandler=se_hotelsystem_BookingHandler(0, 0, se_hotelsystem_BookingHandler=set(), se_hotelsystem_BookingHandler2=hotelsystem_PaymentHandler(), se_hotelsystem_BookingHandler4=hotelsystem_IRoomHandler(), hotelsystem_IHotelReceptionistProvides=se_actor_Receptionist(), hotelsystem_IHotelCustomerProvides=se_actor_Receptionist()), hotelsystem_IHotelAdministratorProvides=se_actor_Administrator()), se_hotelsystem_RoomHandler=set(), se_hotelsystem_RoomHandler23=set(), hotelsystem_IRoomHandler=se_hotelsystem_BookingHandler(0, 0, se_hotelsystem_BookingHandler=set(), se_hotelsystem_BookingHandler2=hotelsystem_PaymentHandler(), se_hotelsystem_BookingHandler4=hotelsystem_IRoomHandler(), hotelsystem_IHotelReceptionistProvides=se_actor_Receptionist(), hotelsystem_IHotelCustomerProvides=se_actor_Receptionist()), hotelsystem_IHotelAdministratorProvides=se_actor_Administrator()) == None

def test_se_hotelsystem_RoomHandler_getRoom():
    assert se_hotelsystem_RoomHandler.getRoom(se_hotelsystem_RoomHandler(se_hotelsystem_RoomHandler=set(), se_hotelsystem_RoomHandler23=set(), hotelsystem_IRoomHandler=se_hotelsystem_BookingHandler(0, 0, se_hotelsystem_BookingHandler=set(), se_hotelsystem_BookingHandler2=hotelsystem_PaymentHandler(), se_hotelsystem_BookingHandler4=hotelsystem_IRoomHandler(), hotelsystem_IHotelReceptionistProvides=se_actor_Receptionist(), hotelsystem_IHotelCustomerProvides=se_actor_Receptionist()), hotelsystem_IHotelAdministratorProvides=se_actor_Administrator()), 0) == None

def test_se_hotelsystem_RoomHandler_initialize():
    assert se_hotelsystem_RoomHandler.initialize(se_hotelsystem_RoomHandler(se_hotelsystem_RoomHandler=set(), se_hotelsystem_RoomHandler23=set(), hotelsystem_IRoomHandler=se_hotelsystem_BookingHandler(0, 0, se_hotelsystem_BookingHandler=set(), se_hotelsystem_BookingHandler2=hotelsystem_PaymentHandler(), se_hotelsystem_BookingHandler4=hotelsystem_IRoomHandler(), hotelsystem_IHotelReceptionistProvides=se_actor_Receptionist(), hotelsystem_IHotelCustomerProvides=se_actor_Receptionist()), hotelsystem_IHotelAdministratorProvides=se_actor_Administrator()), 0) == None


from python_code import se_hotelsystem_RoomType

def test_se_hotelsystem_RoomType___init__():
    assert se_hotelsystem_RoomType.__init__(se_hotelsystem_RoomType('', 0, 0.0, ''), '', 0, 0.0, '') == None

