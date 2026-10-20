from python_code import newClasses_AdministratorProvides

def test_newClasses_AdministratorProvides___init__():
    assert newClasses_AdministratorProvides.__init__(newClasses_AdministratorProvides()) == None

def test_newClasses_AdministratorProvides_getBalance():
    assert newClasses_AdministratorProvides.getBalance(newClasses_AdministratorProvides(), '', '', '', '', '', '') == None

def test_newClasses_AdministratorProvides_removeCreditCard():
    assert newClasses_AdministratorProvides.removeCreditCard(newClasses_AdministratorProvides(), '', '', '', '', '', '') == None

def test_newClasses_AdministratorProvides_makeDeposit():
    assert newClasses_AdministratorProvides.makeDeposit(newClasses_AdministratorProvides(), '', '', '', '', '', '', '') == None

def test_newClasses_AdministratorProvides_addCreditCard():
    assert newClasses_AdministratorProvides.addCreditCard(newClasses_AdministratorProvides(), '', '', '', '', '', '') == None


from python_code import newClasses_Biller

def test_newClasses_Biller___init__():
    assert newClasses_Biller.__init__(newClasses_Biller()) == None

def test_newClasses_Biller_pay():
    assert newClasses_Biller.pay(newClasses_Biller(), '', '', '', '', '', '', '', '', '', '') == None

def test_newClasses_Biller_calculateBill():
    assert newClasses_Biller.calculateBill(newClasses_Biller(), '', '', '', '') == None

def test_newClasses_Biller_calculateCost():
    assert newClasses_Biller.calculateCost(newClasses_Biller(), '', '', '', '') == None


from python_code import newClasses_Billing

def test_newClasses_Billing___init__():
    assert newClasses_Billing.__init__(newClasses_Billing('', '\x00'), '\x00\x00', '') == None


from python_code import newClasses_Booker

def test_newClasses_Booker___init__():
    assert newClasses_Booker.__init__(newClasses_Booker()) == None

def test_newClasses_Booker_cancelBooking():
    assert newClasses_Booker.cancelBooking(newClasses_Booker(), '') == None

def test_newClasses_Booker_createBooking():
    assert newClasses_Booker.createBooking(newClasses_Booker(), '', '', '', '') == None

def test_newClasses_Booker_reBook():
    assert newClasses_Booker.reBook(newClasses_Booker(), '', '', '', '', '') == None

def test_newClasses_Booker_generateConfirmNum():
    assert newClasses_Booker.generateConfirmNum(newClasses_Booker()) == None


from python_code import newClasses_CustomerProvides

def test_newClasses_CustomerProvides___init__():
    assert newClasses_CustomerProvides.__init__(newClasses_CustomerProvides()) == None

def test_newClasses_CustomerProvides_makePayment():
    assert newClasses_CustomerProvides.makePayment(newClasses_CustomerProvides(), '', '', '', '', '', '', '') == None

def test_newClasses_CustomerProvides_isCreditCardValid():
    assert newClasses_CustomerProvides.isCreditCardValid(newClasses_CustomerProvides(), '', '', '', '', '', '') == None


from python_code import newClasses_DB_interface

def test_newClasses_DB_interface___init__():
    assert newClasses_DB_interface.__init__(newClasses_DB_interface()) == None

def test_newClasses_DB_interface_storeCustomer():
    assert newClasses_DB_interface.storeCustomer(newClasses_DB_interface(), '') == None

def test_newClasses_DB_interface_registerCustomerPayment():
    assert newClasses_DB_interface.registerCustomerPayment(newClasses_DB_interface(), '', '') == None

def test_newClasses_DB_interface_connect():
    assert newClasses_DB_interface.connect(newClasses_DB_interface()) == None

def test_newClasses_DB_interface_storeBooking():
    assert newClasses_DB_interface.storeBooking(newClasses_DB_interface(), '') == None

def test_newClasses_DB_interface_storeGuest():
    assert newClasses_DB_interface.storeGuest(newClasses_DB_interface(), '') == None

def test_newClasses_DB_interface_registerGuestPayment():
    assert newClasses_DB_interface.registerGuestPayment(newClasses_DB_interface(), '', '') == None


from python_code import newClasses_Guest

def test_newClasses_Guest___init__():
    assert newClasses_Guest.__init__(newClasses_Guest('', '', '', '', '\x00', '', '', '', ''), '', '', '', '', '', '\x00', '', '', '') == None


from python_code import newClasses_GuestBiller

def test_newClasses_GuestBiller___init__():
    assert newClasses_GuestBiller.__init__(newClasses_GuestBiller()) == None

def test_newClasses_GuestBiller_checkOut():
    assert newClasses_GuestBiller.checkOut(newClasses_GuestBiller(), '', '', '', '', '', '', '', '', '') == None

def test_newClasses_GuestBiller_addServiceToBill():
    assert newClasses_GuestBiller.addServiceToBill(newClasses_GuestBiller(), '', '') == None


from python_code import newClasses_GuestInterface

def test_newClasses_GuestInterface___init__():
    assert newClasses_GuestInterface.__init__(newClasses_GuestInterface()) == None

def test_newClasses_GuestInterface_checkIn():
    assert newClasses_GuestInterface.checkIn(newClasses_GuestInterface(), '', '') == None

def test_newClasses_GuestInterface_changeRoom():
    assert newClasses_GuestInterface.changeRoom(newClasses_GuestInterface(), '', '', '') == None

def test_newClasses_GuestInterface_extendStay():
    assert newClasses_GuestInterface.extendStay(newClasses_GuestInterface(), '', '', '') == None


from python_code import newClasses_LoginChecker
from python_code import newClasses_Manager
from python_code import newClasses_RoomHandler
from python_code import newClasses_ServiceHandler

def test_newClasses_Manager___init__():
    assert newClasses_Manager.__init__(newClasses_Manager('', '\x00', newClasses_Manager=newClasses_RoomHandler(), newClasses_Manager10=newClasses_ServiceHandler(), newClasses_Manager18=newClasses_LoginChecker()), '\x00\x00', '', newClasses_Manager=newClasses_RoomHandler(), newClasses_Manager10=newClasses_ServiceHandler(), newClasses_Manager18=newClasses_LoginChecker()) == None


from python_code import newClasses_ManagerInterface

def test_newClasses_ManagerInterface___init__():
    assert newClasses_ManagerInterface.__init__(newClasses_ManagerInterface()) == None

def test_newClasses_ManagerInterface_validateLogin():
    assert newClasses_ManagerInterface.validateLogin(newClasses_ManagerInterface(), '', '') == None

def test_newClasses_ManagerInterface_SessionData():
    assert newClasses_ManagerInterface.SessionData(newClasses_ManagerInterface()) == None

def test_newClasses_ManagerInterface_login():
    assert newClasses_ManagerInterface.login(newClasses_ManagerInterface(), '', '') == None

def test_newClasses_ManagerInterface_logout():
    assert newClasses_ManagerInterface.logout(newClasses_ManagerInterface()) == None


from python_code import newClasses_Receipt

def test_newClasses_Receipt___init__():
    assert newClasses_Receipt.__init__(newClasses_Receipt()) == None

def test_newClasses_Receipt_createGuestReceipt():
    assert newClasses_Receipt.createGuestReceipt(newClasses_Receipt(), '', '', '') == None

def test_newClasses_Receipt_createCustomerReceipt():
    assert newClasses_Receipt.createCustomerReceipt(newClasses_Receipt(), '', '', '') == None


from python_code import newClasses_Room
from python_code import newClasses_RoomHandler

def test_newClasses_Room___init__():
    assert newClasses_Room.__init__(newClasses_Room('', '\x00', newClasses_Room=newClasses_RoomHandler()), '\x00\x00', '', newClasses_Room=newClasses_RoomHandler()) == None


from python_code import newClasses_RoomHandlerInterface

def test_newClasses_RoomHandlerInterface___init__():
    assert newClasses_RoomHandlerInterface.__init__(newClasses_RoomHandlerInterface()) == None

def test_newClasses_RoomHandlerInterface_addRoom():
    assert newClasses_RoomHandlerInterface.addRoom(newClasses_RoomHandlerInterface(), '', '', '') == None

def test_newClasses_RoomHandlerInterface_changeRoomType():
    assert newClasses_RoomHandlerInterface.changeRoomType(newClasses_RoomHandlerInterface(), '', '') == None

def test_newClasses_RoomHandlerInterface_changeRoomPrice():
    assert newClasses_RoomHandlerInterface.changeRoomPrice(newClasses_RoomHandlerInterface(), '', '') == None

def test_newClasses_RoomHandlerInterface_removeRoom():
    assert newClasses_RoomHandlerInterface.removeRoom(newClasses_RoomHandlerInterface(), '') == None


from python_code import newClasses_RoomProvider

def test_newClasses_RoomProvider___init__():
    assert newClasses_RoomProvider.__init__(newClasses_RoomProvider()) == None

def test_newClasses_RoomProvider_checkAvalibility():
    assert newClasses_RoomProvider.checkAvalibility(newClasses_RoomProvider(), '', '', '') == None

def test_newClasses_RoomProvider_setAvalibility():
    assert newClasses_RoomProvider.setAvalibility(newClasses_RoomProvider(), '', '', '', '') == None

def test_newClasses_RoomProvider_dateChecker():
    assert newClasses_RoomProvider.dateChecker(newClasses_RoomProvider(), '', '', '', '') == None


from python_code import newClasses_RoomType

def test_newClasses_RoomType___init__():
    assert newClasses_RoomType.__init__(newClasses_RoomType('', '\x00'), '\x00\x00', '') == None


from python_code import newClasses_Service
from python_code import newClasses_ServiceHandler

def test_newClasses_Service___init__():
    assert newClasses_Service.__init__(newClasses_Service('', '\x00', newClasses_Service=newClasses_ServiceHandler()), '\x00\x00', '', newClasses_Service=newClasses_ServiceHandler()) == None


from python_code import newClasses_ServiceHandlerInterface

def test_newClasses_ServiceHandlerInterface___init__():
    assert newClasses_ServiceHandlerInterface.__init__(newClasses_ServiceHandlerInterface()) == None

def test_newClasses_ServiceHandlerInterface_removeService():
    assert newClasses_ServiceHandlerInterface.removeService(newClasses_ServiceHandlerInterface(), '') == None

def test_newClasses_ServiceHandlerInterface_addService():
    assert newClasses_ServiceHandlerInterface.addService(newClasses_ServiceHandlerInterface(), '', '', '') == None

def test_newClasses_ServiceHandlerInterface_changeServicePrice():
    assert newClasses_ServiceHandlerInterface.changeServicePrice(newClasses_ServiceHandlerInterface(), '', '') == None

def test_newClasses_ServiceHandlerInterface_changeServiceType():
    assert newClasses_ServiceHandlerInterface.changeServiceType(newClasses_ServiceHandlerInterface(), '', '') == None


from python_code import newClasses_ServiceProvider

def test_newClasses_ServiceProvider___init__():
    assert newClasses_ServiceProvider.__init__(newClasses_ServiceProvider()) == None

def test_newClasses_ServiceProvider_setAvalibility():
    assert newClasses_ServiceProvider.setAvalibility(newClasses_ServiceProvider(), '', '') == None

def test_newClasses_ServiceProvider_checkAvalibility():
    assert newClasses_ServiceProvider.checkAvalibility(newClasses_ServiceProvider(), '', '', '') == None


from python_code import newClasses_ServiceType

def test_newClasses_ServiceType___init__():
    assert newClasses_ServiceType.__init__(newClasses_ServiceType('', '\x00'), '\x00\x00', '') == None


from python_code import newClasses_Validator

def test_newClasses_Validator___init__():
    assert newClasses_Validator.__init__(newClasses_Validator()) == None

def test_newClasses_Validator_checkAgeRestriction():
    assert newClasses_Validator.checkAgeRestriction(newClasses_Validator(), '') == None

def test_newClasses_Validator_validateDates():
    assert newClasses_Validator.validateDates(newClasses_Validator(), '', '') == None

def test_newClasses_Validator_validatePersonalNum():
    assert newClasses_Validator.validatePersonalNum(newClasses_Validator(), '') == None

def test_newClasses_Validator_validateEmail():
    assert newClasses_Validator.validateEmail(newClasses_Validator(), '') == None

def test_newClasses_Validator_validateAddress():
    assert newClasses_Validator.validateAddress(newClasses_Validator(), '', '', '', '') == None

def test_newClasses_Validator_checkAge():
    assert newClasses_Validator.checkAge(newClasses_Validator(), '', '', '') == None

def test_newClasses_Validator_checkDateOrder():
    assert newClasses_Validator.checkDateOrder(newClasses_Validator(), '', '') == None

def test_newClasses_Validator_validatePhoneNum():
    assert newClasses_Validator.validatePhoneNum(newClasses_Validator(), '') == None

def test_newClasses_Validator_validateNames():
    assert newClasses_Validator.validateNames(newClasses_Validator(), '', '') == None

def test_newClasses_Validator_validateConfirmationNum():
    assert newClasses_Validator.validateConfirmationNum(newClasses_Validator(), '') == None

