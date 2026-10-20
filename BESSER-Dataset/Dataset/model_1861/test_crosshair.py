from python_code import HotelManagementClassDiagram_BookingController

def test_HotelManagementClassDiagram_BookingController___init__():
    assert HotelManagementClassDiagram_BookingController.__init__(HotelManagementClassDiagram_BookingController()) == None

def test_HotelManagementClassDiagram_BookingController_updateBooking():
    assert HotelManagementClassDiagram_BookingController.updateBooking(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_checkOut():
    assert HotelManagementClassDiagram_BookingController.checkOut(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_sendConfirmation():
    assert HotelManagementClassDiagram_BookingController.sendConfirmation(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_checkIn():
    assert HotelManagementClassDiagram_BookingController.checkIn(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_getBooking():
    assert HotelManagementClassDiagram_BookingController.getBooking(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_createKeyCard():
    assert HotelManagementClassDiagram_BookingController.createKeyCard(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_saveCustomer():
    assert HotelManagementClassDiagram_BookingController.saveCustomer(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_searchAvailableRoomTypes():
    assert HotelManagementClassDiagram_BookingController.searchAvailableRoomTypes(HotelManagementClassDiagram_BookingController(), '', '', '', '') == None

def test_HotelManagementClassDiagram_BookingController_findCustomer():
    assert HotelManagementClassDiagram_BookingController.findCustomer(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_createBooking():
    assert HotelManagementClassDiagram_BookingController.createBooking(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_assignRoom():
    assert HotelManagementClassDiagram_BookingController.assignRoom(HotelManagementClassDiagram_BookingController(), '') == None

def test_HotelManagementClassDiagram_BookingController_confirm():
    assert HotelManagementClassDiagram_BookingController.confirm(HotelManagementClassDiagram_BookingController(), '') == None


from python_code import HotelManagementClassDiagram_Hotel

def test_HotelManagementClassDiagram_Hotel___init__():
    assert HotelManagementClassDiagram_Hotel.__init__(HotelManagementClassDiagram_Hotel('', '', 0.0), '', '', 0.0) == None

def test_HotelManagementClassDiagram_Hotel_getBookingController():
    assert HotelManagementClassDiagram_Hotel.getBookingController(HotelManagementClassDiagram_Hotel('', '', 0.0)) == None

def test_HotelManagementClassDiagram_Hotel_getMaintenanceController():
    assert HotelManagementClassDiagram_Hotel.getMaintenanceController(HotelManagementClassDiagram_Hotel('', '', 0.0)) == None

def test_HotelManagementClassDiagram_Hotel_authenticate():
    assert HotelManagementClassDiagram_Hotel.authenticate(HotelManagementClassDiagram_Hotel('', '', 0.0), 0, 0) == None

def test_HotelManagementClassDiagram_Hotel_getManagementController():
    assert HotelManagementClassDiagram_Hotel.getManagementController(HotelManagementClassDiagram_Hotel('', '', 0.0)) == None


from python_code import HotelManagementClassDiagram_ManagementController

def test_HotelManagementClassDiagram_ManagementController___init__():
    assert HotelManagementClassDiagram_ManagementController.__init__(HotelManagementClassDiagram_ManagementController()) == None

def test_HotelManagementClassDiagram_ManagementController_registerDiscount():
    assert HotelManagementClassDiagram_ManagementController.registerDiscount(HotelManagementClassDiagram_ManagementController(), '') == None

def test_HotelManagementClassDiagram_ManagementController_updateRoom():
    assert HotelManagementClassDiagram_ManagementController.updateRoom(HotelManagementClassDiagram_ManagementController(), '') == None

def test_HotelManagementClassDiagram_ManagementController_updateAddon():
    assert HotelManagementClassDiagram_ManagementController.updateAddon(HotelManagementClassDiagram_ManagementController(), '') == None

def test_HotelManagementClassDiagram_ManagementController_registerRoom():
    assert HotelManagementClassDiagram_ManagementController.registerRoom(HotelManagementClassDiagram_ManagementController(), '') == None

def test_HotelManagementClassDiagram_ManagementController_registerAddon():
    assert HotelManagementClassDiagram_ManagementController.registerAddon(HotelManagementClassDiagram_ManagementController(), '') == None

def test_HotelManagementClassDiagram_ManagementController_setDateSpecificPrices():
    assert HotelManagementClassDiagram_ManagementController.setDateSpecificPrices(HotelManagementClassDiagram_ManagementController(), '', '', '', '') == None

def test_HotelManagementClassDiagram_ManagementController_modifyBooking():
    assert HotelManagementClassDiagram_ManagementController.modifyBooking(HotelManagementClassDiagram_ManagementController(), '') == None


from python_code import HotelManagementClassDiagram_Person

def test_HotelManagementClassDiagram_Person___init__():
    assert HotelManagementClassDiagram_Person.__init__(HotelManagementClassDiagram_Person('', '', '', '', '\x00', '', '', '', ''), '', '', '', '', '', '\x00', '', '', '') == None

