from python_code import CheckInHandler
from python_code import CodePack_CheckInMachine

def test_CodePack_CheckInMachine___init__():
    assert CodePack_CheckInMachine.__init__(CodePack_CheckInMachine(CodePack_CheckInMachine=CheckInHandler()), CodePack_CheckInMachine=CheckInHandler()) == None

def test_CodePack_CheckInMachine_startUI():
    assert CodePack_CheckInMachine.startUI(CodePack_CheckInMachine(CodePack_CheckInMachine=CheckInHandler())) == None

from python_code import CodePack_DataModels_Bill

def test_CodePack_DataModels_Bill___init__():
    assert CodePack_DataModels_Bill.__init__(CodePack_DataModels_Bill(0, 0.0, CodePack_DataModels_Bill=set(), CodePack_DataModels_Bill31=set()), 0, 0.0, CodePack_DataModels_Bill=set(), CodePack_DataModels_Bill31=set()) == None

from python_code import CodePack_DataModels_Booking
from python_code import Room

def test_CodePack_DataModels_Booking___init__():
    assert CodePack_DataModels_Booking.__init__(CodePack_DataModels_Booking(0, datetime.date(1, 1, 1), datetime.date(1, 1, 1), False, 0.0, '', 0, '', 0, 0, 0, CodePack_DataModels_Booking=Room()), 0, datetime.date(1, 1, 1), datetime.date(1, 1, 1), False, 0.0, '', 0, '', 0, 0, 0, CodePack_DataModels_Booking=Room()) == None

from python_code import CodePack_DataModels_Customer

def test_CodePack_DataModels_Customer___init__():
    assert CodePack_DataModels_Customer.__init__(CodePack_DataModels_Customer('', datetime.date(1, 1, 1), 0, '', '', 0, 0, 0, ''), '', datetime.date(1, 1, 1), 0, '', '', 0, 0, 0, '') == None

from python_code import CodePack_DataModels_ExtraService

def test_CodePack_DataModels_ExtraService___init__():
    assert CodePack_DataModels_ExtraService.__init__(CodePack_DataModels_ExtraService(datetime.date(1, 1, 2), datetime.date(1, 1, 1), 0, 0.0, ''), datetime.date(1, 1, 1), datetime.date(1, 1, 1), 0, 0.0, '') == None

from python_code import CodePack_DataModels_Guest

def test_CodePack_DataModels_Guest___init__():
    assert CodePack_DataModels_Guest.__init__(CodePack_DataModels_Guest('', 0), '', 0) == None

from python_code import CodePack_DataModels_PaymentData

def test_CodePack_DataModels_PaymentData___init__():
    assert CodePack_DataModels_PaymentData.__init__(CodePack_DataModels_PaymentData('', '', 0, 0, '', '', 0), '', '\x00', 0, 0, '', '', 0) == None

from python_code import CodePack_DataModels_Room

def test_CodePack_DataModels_Room___init__():
    assert CodePack_DataModels_Room.__init__(CodePack_DataModels_Room(0, '\x00', False, ''), 0, '', False, '') == None

from python_code import Booking
from python_code import CodePack_DataModels_RoomBooked

def test_CodePack_DataModels_RoomBooked___init__():
    assert CodePack_DataModels_RoomBooked.__init__(CodePack_DataModels_RoomBooked(0, 0, datetime.date(1, 1, 1), datetime.date(1, 1, 1), CodePack_DataModels_RoomBooked=Booking()), 0, 0, datetime.date(1, 1, 1), datetime.date(1, 1, 1), CodePack_DataModels_RoomBooked=Booking()) == None

from python_code import CodePack_DataModels_RoomType

def test_CodePack_DataModels_RoomType___init__():
    assert CodePack_DataModels_RoomType.__init__(CodePack_DataModels_RoomType('', 0, 0.0, ''), '', 0, 0.0, '') == None

from python_code import CodePack_DataModels_ServiceType

def test_CodePack_DataModels_ServiceType___init__():
    assert CodePack_DataModels_ServiceType.__init__(CodePack_DataModels_ServiceType('', '', 0.0), '', '', 0.0) == None

from python_code import CodePack_DataModels_StaffMember

def test_CodePack_DataModels_StaffMember___init__():
    assert CodePack_DataModels_StaffMember.__init__(CodePack_DataModels_StaffMember('', '', '', '', 0, ''), '', '', '', '', 0, '') == None

from python_code import CodePack_DataModels_StaffRole

def test_CodePack_DataModels_StaffRole___init__():
    assert CodePack_DataModels_StaffRole.__init__(CodePack_DataModels_StaffRole('', False, False, False, False), '', False, False, False, False) == None

from python_code import CodePack_IBookings

def test_CodePack_IBookings___init__():
    assert CodePack_IBookings.__init__(CodePack_IBookings()) == None

def test_CodePack_IBookings_getBookingForId():
    assert CodePack_IBookings.getBookingForId(CodePack_IBookings(), '') == None

def test_CodePack_IBookings_isRoomAvailable():
    assert CodePack_IBookings.isRoomAvailable(CodePack_IBookings(), '', '', '') == None

def test_CodePack_IBookings_sendComfimationMail():
    assert CodePack_IBookings.sendComfimationMail(CodePack_IBookings(), '') == None

def test_CodePack_IBookings_getAvailableServices():
    assert CodePack_IBookings.getAvailableServices(CodePack_IBookings()) == None

def test_CodePack_IBookings_getAvailableRooms():
    assert CodePack_IBookings.getAvailableRooms(CodePack_IBookings(), '', '') == None

def test_CodePack_IBookings_updateTimeForBooking():
    assert CodePack_IBookings.updateTimeForBooking(CodePack_IBookings(), '', '', '') == None

def test_CodePack_IBookings_updateRoomForBooking():
    assert CodePack_IBookings.updateRoomForBooking(CodePack_IBookings(), '', '', '') == None

def test_CodePack_IBookings_updateServiceForBooking():
    assert CodePack_IBookings.updateServiceForBooking(CodePack_IBookings(), '', '') == None

def test_CodePack_IBookings_createBookingForCustomer():
    assert CodePack_IBookings.createBookingForCustomer(CodePack_IBookings(), '', '', '', '', '', '', '') == None

def test_CodePack_IBookings_createBooking():
    assert CodePack_IBookings.createBooking(CodePack_IBookings(), '', '', '', '', '', '', '') == None

def test_CodePack_IBookings_getBookingsForCustomer():
    assert CodePack_IBookings.getBookingsForCustomer(CodePack_IBookings(), '') == None

def test_CodePack_IBookings_cancelBooking():
    assert CodePack_IBookings.cancelBooking(CodePack_IBookings(), '') == None

def test_CodePack_IBookings_getPaymentForBooking():
    assert CodePack_IBookings.getPaymentForBooking(CodePack_IBookings(), '') == None

from python_code import CodePack_ICheckIn

def test_CodePack_ICheckIn___init__():
    assert CodePack_ICheckIn.__init__(CodePack_ICheckIn()) == None

def test_CodePack_ICheckIn_validateBooking():
    assert CodePack_ICheckIn.validateBooking(CodePack_ICheckIn(), '') == None

def test_CodePack_ICheckIn_assignGuestToBooking():
    assert CodePack_ICheckIn.assignGuestToBooking(CodePack_ICheckIn(), '', '') == None

from python_code import CodePack_IManagement

def test_CodePack_IManagement___init__():
    assert CodePack_IManagement.__init__(CodePack_IManagement()) == None

def test_CodePack_IManagement_getServiceTypes():
    assert CodePack_IManagement.getServiceTypes(CodePack_IManagement()) == None

def test_CodePack_IManagement_removeRoomType():
    assert CodePack_IManagement.removeRoomType(CodePack_IManagement(), '') == None

def test_CodePack_IManagement_removeServiceType():
    assert CodePack_IManagement.removeServiceType(CodePack_IManagement(), '') == None

def test_CodePack_IManagement_removeRoom():
    assert CodePack_IManagement.removeRoom(CodePack_IManagement(), '') == None

def test_CodePack_IManagement_getRoom():
    assert CodePack_IManagement.getRoom(CodePack_IManagement(), '') == None

def test_CodePack_IManagement_getRoomTypes():
    assert CodePack_IManagement.getRoomTypes(CodePack_IManagement()) == None

def test_CodePack_IManagement_updateServiceType():
    assert CodePack_IManagement.updateServiceType(CodePack_IManagement(), '') == None

def test_CodePack_IManagement_addRoom():
    assert CodePack_IManagement.addRoom(CodePack_IManagement(), '', '', '', '') == None

def test_CodePack_IManagement_getAllRooms():
    assert CodePack_IManagement.getAllRooms(CodePack_IManagement()) == None

def test_CodePack_IManagement_addRoomType():
    assert CodePack_IManagement.addRoomType(CodePack_IManagement(), '', '', '', '') == None

def test_CodePack_IManagement_updateRoom():
    assert CodePack_IManagement.updateRoom(CodePack_IManagement(), '') == None

def test_CodePack_IManagement_updateRoomType():
    assert CodePack_IManagement.updateRoomType(CodePack_IManagement(), '') == None

from python_code import CodePack_IReceptionOperations_rename_required

def test_CodePack_IReceptionOperations_rename_required___init__():
    assert CodePack_IReceptionOperations_rename_required.__init__(CodePack_IReceptionOperations_rename_required()) == None

def test_CodePack_IReceptionOperations_rename_required_isCheckedIn():
    assert CodePack_IReceptionOperations_rename_required.isCheckedIn(CodePack_IReceptionOperations_rename_required(), '') == None

def test_CodePack_IReceptionOperations_rename_required_generateReceipt():
    assert CodePack_IReceptionOperations_rename_required.generateReceipt(CodePack_IReceptionOperations_rename_required(), '') == None

def test_CodePack_IReceptionOperations_rename_required_generateBill():
    assert CodePack_IReceptionOperations_rename_required.generateBill(CodePack_IReceptionOperations_rename_required(), '') == None

from python_code import CodePack_IStaffAdmin

def test_CodePack_IStaffAdmin___init__():
    assert CodePack_IStaffAdmin.__init__(CodePack_IStaffAdmin()) == None

def test_CodePack_IStaffAdmin_getStaffRoles():
    assert CodePack_IStaffAdmin.getStaffRoles(CodePack_IStaffAdmin()) == None

def test_CodePack_IStaffAdmin_removeStaffRole():
    assert CodePack_IStaffAdmin.removeStaffRole(CodePack_IStaffAdmin(), '') == None

def test_CodePack_IStaffAdmin_updateStaffRole():
    assert CodePack_IStaffAdmin.updateStaffRole(CodePack_IStaffAdmin(), '') == None

def test_CodePack_IStaffAdmin_updateStaffAccount():
    assert CodePack_IStaffAdmin.updateStaffAccount(CodePack_IStaffAdmin(), '') == None

def test_CodePack_IStaffAdmin_getStaffAccount():
    assert CodePack_IStaffAdmin.getStaffAccount(CodePack_IStaffAdmin(), '') == None

def test_CodePack_IStaffAdmin_removeStaffAccount():
    assert CodePack_IStaffAdmin.removeStaffAccount(CodePack_IStaffAdmin(), '') == None

def test_CodePack_IStaffAdmin_getAllStaffAccounts():
    assert CodePack_IStaffAdmin.getAllStaffAccounts(CodePack_IStaffAdmin()) == None

def test_CodePack_IStaffAdmin_registerStaffAccount():
    assert CodePack_IStaffAdmin.registerStaffAccount(CodePack_IStaffAdmin(), '', '', '', '', '') == None

def test_CodePack_IStaffAdmin_addStaffRole():
    assert CodePack_IStaffAdmin.addStaffRole(CodePack_IStaffAdmin(), '', '', '', '', '') == None

from python_code import CodePack_IStaffAuthentication

def test_CodePack_IStaffAuthentication___init__():
    assert CodePack_IStaffAuthentication.__init__(CodePack_IStaffAuthentication()) == None

def test_CodePack_IStaffAuthentication_getRoleForStaff():
    assert CodePack_IStaffAuthentication.getRoleForStaff(CodePack_IStaffAuthentication(), '') == None

def test_CodePack_IStaffAuthentication_login():
    assert CodePack_IStaffAuthentication.login(CodePack_IStaffAuthentication(), '', '') == None

from python_code import CodePack_IUserAccount

def test_CodePack_IUserAccount___init__():
    assert CodePack_IUserAccount.__init__(CodePack_IUserAccount()) == None

def test_CodePack_IUserAccount_updateCustomerInfo():
    assert CodePack_IUserAccount.updateCustomerInfo(CodePack_IUserAccount(), '', '', '') == None

def test_CodePack_IUserAccount_updateCustomerPwd():
    assert CodePack_IUserAccount.updateCustomerPwd(CodePack_IUserAccount(), '', '', '') == None

def test_CodePack_IUserAccount_getCustomerInfo():
    assert CodePack_IUserAccount.getCustomerInfo(CodePack_IUserAccount(), '') == None

def test_CodePack_IUserAccount_isEmailAvailable():
    assert CodePack_IUserAccount.isEmailAvailable(CodePack_IUserAccount(), '') == None

def test_CodePack_IUserAccount_updateCustomerCC():
    assert CodePack_IUserAccount.updateCustomerCC(CodePack_IUserAccount(), '', '', '', '', '', '', '') == None

def test_CodePack_IUserAccount_login():
    assert CodePack_IUserAccount.login(CodePack_IUserAccount(), '', '') == None

def test_CodePack_IUserAccount_registerCustomer():
    assert CodePack_IUserAccount.registerCustomer(CodePack_IUserAccount(), '', '', '', '', '', '') == None

from python_code import CodePack_Shared_ContactData

def test_CodePack_Shared_ContactData___init__():
    assert CodePack_Shared_ContactData.__init__(CodePack_Shared_ContactData('', '', 0), '\x00', '', 0) == None

from python_code import CodePack_StaffGUI
from python_code import ManagementHandler
from python_code import ReceptionHandler

def test_CodePack_StaffGUI___init__():
    assert CodePack_StaffGUI.__init__(CodePack_StaffGUI(CodePack_StaffGUI=ManagementHandler(), CodePack_StaffGUI2=ReceptionHandler()), CodePack_StaffGUI=ManagementHandler(), CodePack_StaffGUI2=ReceptionHandler()) == None

def test_CodePack_StaffGUI_startUI():
    assert CodePack_StaffGUI.startUI(CodePack_StaffGUI(CodePack_StaffGUI=ManagementHandler(), CodePack_StaffGUI2=ReceptionHandler())) == None

from python_code import CodePack_UserGUI
from python_code import CustomerHandler

def test_CodePack_UserGUI___init__():
    assert CodePack_UserGUI.__init__(CodePack_UserGUI(CodePack_UserGUI=CustomerHandler()), CodePack_UserGUI=CustomerHandler()) == None

def test_CodePack_UserGUI_startUI():
    assert CodePack_UserGUI.startUI(CodePack_UserGUI(CodePack_UserGUI=CustomerHandler())) == None
