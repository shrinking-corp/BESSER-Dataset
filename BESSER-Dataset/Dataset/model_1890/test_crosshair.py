from python_code import Classes_mdsdAccount_Account

def test_Classes_mdsdAccount_Account___init__():
    assert Classes_mdsdAccount_Account.__init__(Classes_mdsdAccount_Account('', '', '', '', False, Classes_mdsdAccount_Account=set()), '', '', '', '\x00', False, Classes_mdsdAccount_Account=set()) == None

from python_code import Classes_mdsdAccount_BookingToAccount

def test_Classes_mdsdAccount_BookingToAccount___init__():
    assert Classes_mdsdAccount_BookingToAccount.__init__(Classes_mdsdAccount_BookingToAccount()) == None

def test_Classes_mdsdAccount_BookingToAccount_getAccount():
    assert Classes_mdsdAccount_BookingToAccount.getAccount(Classes_mdsdAccount_BookingToAccount(), '') == None

def test_Classes_mdsdAccount_BookingToAccount_isUserLoggedIn():
    assert Classes_mdsdAccount_BookingToAccount.isUserLoggedIn(Classes_mdsdAccount_BookingToAccount(), '') == None

from python_code import Classes_mdsdAccount_CustomerAccount

def test_Classes_mdsdAccount_CustomerAccount___init__():
    assert Classes_mdsdAccount_CustomerAccount.__init__(Classes_mdsdAccount_CustomerAccount()) == None

def test_Classes_mdsdAccount_CustomerAccount_removePet():
    assert Classes_mdsdAccount_CustomerAccount.removePet(Classes_mdsdAccount_CustomerAccount(), '', '', '') == None

def test_Classes_mdsdAccount_CustomerAccount_createAccount():
    assert Classes_mdsdAccount_CustomerAccount.createAccount(Classes_mdsdAccount_CustomerAccount(), '', '', '') == None

def test_Classes_mdsdAccount_CustomerAccount_logout():
    assert Classes_mdsdAccount_CustomerAccount.logout(Classes_mdsdAccount_CustomerAccount(), '') == None

def test_Classes_mdsdAccount_CustomerAccount_addPet():
    assert Classes_mdsdAccount_CustomerAccount.addPet(Classes_mdsdAccount_CustomerAccount(), '', '', '') == None

def test_Classes_mdsdAccount_CustomerAccount_login():
    assert Classes_mdsdAccount_CustomerAccount.login(Classes_mdsdAccount_CustomerAccount(), '', '') == None

from python_code import Classes_mdsdAccount_Pet

def test_Classes_mdsdAccount_Pet___init__():
    assert Classes_mdsdAccount_Pet.__init__(Classes_mdsdAccount_Pet('', '\x00'), '\x00\x00', '') == None

from python_code import Classes_mdsdAdmin_Admin

def test_Classes_mdsdAdmin_Admin___init__():
    assert Classes_mdsdAdmin_Admin.__init__(Classes_mdsdAdmin_Admin()) == None

def test_Classes_mdsdAdmin_Admin_createStaff():
    assert Classes_mdsdAdmin_Admin.createStaff(Classes_mdsdAdmin_Admin(), '', '', '', '') == None

def test_Classes_mdsdAdmin_Admin_removeRoom():
    assert Classes_mdsdAdmin_Admin.removeRoom(Classes_mdsdAdmin_Admin(), '') == None

def test_Classes_mdsdAdmin_Admin_addRoom():
    assert Classes_mdsdAdmin_Admin.addRoom(Classes_mdsdAdmin_Admin(), '', '', '') == None

def test_Classes_mdsdAdmin_Admin_removeStaff():
    assert Classes_mdsdAdmin_Admin.removeStaff(Classes_mdsdAdmin_Admin(), '') == None

def test_Classes_mdsdAdmin_Admin_modifyStaff():
    assert Classes_mdsdAdmin_Admin.modifyStaff(Classes_mdsdAdmin_Admin(), '', '', '') == None

from python_code import Classes_mdsdAdmin_AdminController

def test_Classes_mdsdAdmin_AdminController___init__():
    assert Classes_mdsdAdmin_AdminController.__init__(Classes_mdsdAdmin_AdminController(Classes_mdsdAdmin_AdminController=set(), Classes_mdsdAdmin_AdminController11=set()), Classes_mdsdAdmin_AdminController=set(), Classes_mdsdAdmin_AdminController11=set()) == None

def test_Classes_mdsdAdmin_AdminController_isLoggedIn():
    assert Classes_mdsdAdmin_AdminController.isLoggedIn(Classes_mdsdAdmin_AdminController(Classes_mdsdAdmin_AdminController=set(), Classes_mdsdAdmin_AdminController11=set()), 0) == None

from python_code import Classes_mdsdAdmin_BookingToAdmin

def test_Classes_mdsdAdmin_BookingToAdmin___init__():
    assert Classes_mdsdAdmin_BookingToAdmin.__init__(Classes_mdsdAdmin_BookingToAdmin()) == None

def test_Classes_mdsdAdmin_BookingToAdmin_getPetTypes():
    assert Classes_mdsdAdmin_BookingToAdmin.getPetTypes(Classes_mdsdAdmin_BookingToAdmin()) == None

from python_code import Classes_mdsdAdmin_HotelStaff

def test_Classes_mdsdAdmin_HotelStaff___init__():
    assert Classes_mdsdAdmin_HotelStaff.__init__(Classes_mdsdAdmin_HotelStaff('', 0, '', False, ''), '', 0, '', False, '') == None

from python_code import Classes_mdsdAdmin_Room

def test_Classes_mdsdAdmin_Room___init__():
    assert Classes_mdsdAdmin_Room.__init__(Classes_mdsdAdmin_Room('', '', 0), '\x00', '', 0) == None

from python_code import Classes_mdsdAdmin_Staff

def test_Classes_mdsdAdmin_Staff___init__():
    assert Classes_mdsdAdmin_Staff.__init__(Classes_mdsdAdmin_Staff()) == None

def test_Classes_mdsdAdmin_Staff_staffLogin():
    assert Classes_mdsdAdmin_Staff.staffLogin(Classes_mdsdAdmin_Staff(), '', '') == None

def test_Classes_mdsdAdmin_Staff_staffLogout():
    assert Classes_mdsdAdmin_Staff.staffLogout(Classes_mdsdAdmin_Staff(), '') == None

def test_Classes_mdsdAdmin_Staff_changeRoomStatus():
    assert Classes_mdsdAdmin_Staff.changeRoomStatus(Classes_mdsdAdmin_Staff(), '', '') == None

from python_code import Classes_mdsdBilling_Bill

def test_Classes_mdsdBilling_Bill___init__():
    assert Classes_mdsdBilling_Bill.__init__(Classes_mdsdBilling_Bill(False, '\x00', Classes_mdsdBilling_Bill=set()), False, '', Classes_mdsdBilling_Bill=set()) == None

def test_Classes_mdsdBilling_Bill_getTotalAmount():
    assert Classes_mdsdBilling_Bill.getTotalAmount(Classes_mdsdBilling_Bill(False, '\x00', Classes_mdsdBilling_Bill=set())) == None

from python_code import Classes_mdsdBilling_BookingToBill

def test_Classes_mdsdBilling_BookingToBill___init__():
    assert Classes_mdsdBilling_BookingToBill.__init__(Classes_mdsdBilling_BookingToBill()) == None

def test_Classes_mdsdBilling_BookingToBill_addTransaction():
    assert Classes_mdsdBilling_BookingToBill.addTransaction(Classes_mdsdBilling_BookingToBill(), '', '', '') == None

from python_code import Classes_mdsdBilling_StaffBilling

def test_Classes_mdsdBilling_StaffBilling___init__():
    assert Classes_mdsdBilling_StaffBilling.__init__(Classes_mdsdBilling_StaffBilling()) == None

def test_Classes_mdsdBilling_StaffBilling_modifyBill():
    assert Classes_mdsdBilling_StaffBilling.modifyBill(Classes_mdsdBilling_StaffBilling(), '', '', '') == None

def test_Classes_mdsdBilling_StaffBilling_printReceipt():
    assert Classes_mdsdBilling_StaffBilling.printReceipt(Classes_mdsdBilling_StaffBilling(), '') == None

def test_Classes_mdsdBilling_StaffBilling_isPaid():
    assert Classes_mdsdBilling_StaffBilling.isPaid(Classes_mdsdBilling_StaffBilling(), '') == None

def test_Classes_mdsdBilling_StaffBilling_giveRefund():
    assert Classes_mdsdBilling_StaffBilling.giveRefund(Classes_mdsdBilling_StaffBilling(), '', '') == None

from python_code import Classes_mdsdBilling_Transaction

def test_Classes_mdsdBilling_Transaction___init__():
    assert Classes_mdsdBilling_Transaction.__init__(Classes_mdsdBilling_Transaction('\x00', 0.0), '', 0.0) == None

from python_code import Classes_mdsdBooking_Booking
from python_code import Meal

def test_Classes_mdsdBooking_Booking___init__():
    assert Classes_mdsdBooking_Booking.__init__(Classes_mdsdBooking_Booking(0, datetime.date(1, 1, 1), datetime.date(1, 1, 2), '', '', '', '', '', False, False, Classes_mdsdBooking_Booking8=Meal(), Classes_mdsdBooking_Booking=set()), 0, datetime.date(1, 1, 1), datetime.date(1, 1, 1), '\x00', '', '', '', '', False, False, Classes_mdsdBooking_Booking8=Meal(), Classes_mdsdBooking_Booking=set()) == None

from python_code import Classes_mdsdBooking_BookingController

def test_Classes_mdsdBooking_BookingController___init__():
    assert Classes_mdsdBooking_BookingController.__init__(Classes_mdsdBooking_BookingController(Classes_mdsdBooking_BookingController=set(), Classes_mdsdBooking_BookingController4=set()), Classes_mdsdBooking_BookingController=set(), Classes_mdsdBooking_BookingController4=set()) == None

def test_Classes_mdsdBooking_BookingController_getBookingList():
    assert Classes_mdsdBooking_BookingController.getBookingList(Classes_mdsdBooking_BookingController(Classes_mdsdBooking_BookingController=set(), Classes_mdsdBooking_BookingController4=set()), 0) == None

from python_code import Classes_mdsdBooking_Meal

def test_Classes_mdsdBooking_Meal___init__():
    assert Classes_mdsdBooking_Meal.__init__(Classes_mdsdBooking_Meal('', '\x00', 0.0, 0.0), '', '', 0.0, 0.0) == None

from python_code import Classes_mdsdBooking_Service

def test_Classes_mdsdBooking_Service___init__():
    assert Classes_mdsdBooking_Service.__init__(Classes_mdsdBooking_Service('\x00', 0.0), '', 0.0) == None

from python_code import Classes_mdsdBooking_StaffBooking

def test_Classes_mdsdBooking_StaffBooking___init__():
    assert Classes_mdsdBooking_StaffBooking.__init__(Classes_mdsdBooking_StaffBooking()) == None

def test_Classes_mdsdBooking_StaffBooking_checkIn():
    assert Classes_mdsdBooking_StaffBooking.checkIn(Classes_mdsdBooking_StaffBooking(), '', '') == None

def test_Classes_mdsdBooking_StaffBooking_checkOut():
    assert Classes_mdsdBooking_StaffBooking.checkOut(Classes_mdsdBooking_StaffBooking(), '', '', '') == None

def test_Classes_mdsdBooking_StaffBooking_addNewService():
    assert Classes_mdsdBooking_StaffBooking.addNewService(Classes_mdsdBooking_StaffBooking(), '', '') == None

from python_code import Classes_mdsdBooking_UserBooking

def test_Classes_mdsdBooking_UserBooking___init__():
    assert Classes_mdsdBooking_UserBooking.__init__(Classes_mdsdBooking_UserBooking()) == None

def test_Classes_mdsdBooking_UserBooking_enterCustomerInfo():
    assert Classes_mdsdBooking_UserBooking.enterCustomerInfo(Classes_mdsdBooking_UserBooking(), '', '', '', '', '') == None

def test_Classes_mdsdBooking_UserBooking_enterDatesOfStay():
    assert Classes_mdsdBooking_UserBooking.enterDatesOfStay(Classes_mdsdBooking_UserBooking(), '', '', '', '') == None

def test_Classes_mdsdBooking_UserBooking_cancelBooking():
    assert Classes_mdsdBooking_UserBooking.cancelBooking(Classes_mdsdBooking_UserBooking(), '') == None

def test_Classes_mdsdBooking_UserBooking_enterMealInfo():
    assert Classes_mdsdBooking_UserBooking.enterMealInfo(Classes_mdsdBooking_UserBooking(), '', '', '', '', '') == None

def test_Classes_mdsdBooking_UserBooking_enterService():
    assert Classes_mdsdBooking_UserBooking.enterService(Classes_mdsdBooking_UserBooking(), '', '') == None

def test_Classes_mdsdBooking_UserBooking_modifyBooking():
    assert Classes_mdsdBooking_UserBooking.modifyBooking(Classes_mdsdBooking_UserBooking(), '') == None
