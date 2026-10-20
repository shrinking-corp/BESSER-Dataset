from python_code import Classes_AdministratorProvides

def test_Classes_AdministratorProvides___init__():
    assert Classes_AdministratorProvides.__init__(Classes_AdministratorProvides()) == None

def test_Classes_AdministratorProvides_makeDeposit():
    assert Classes_AdministratorProvides.makeDeposit(Classes_AdministratorProvides(), '', '', '', '', '', '', '') == None

def test_Classes_AdministratorProvides_addCreditCard():
    assert Classes_AdministratorProvides.addCreditCard(Classes_AdministratorProvides(), '', '', '', '', '', '') == None

def test_Classes_AdministratorProvides_getBalance():
    assert Classes_AdministratorProvides.getBalance(Classes_AdministratorProvides(), '', '', '', '', '', '') == None

def test_Classes_AdministratorProvides_removeCreditCard():
    assert Classes_AdministratorProvides.removeCreditCard(Classes_AdministratorProvides(), '', '', '', '', '', '') == None


import datetime as _ch_datetime
from python_code import Classes_Bill
from python_code import Classes_Charge

def test_Classes_Charge___init__():
    assert Classes_Charge.__init__(Classes_Charge(0, _ch_datetime.date(1, 1, 2), '', Classes_Charge=Classes_Bill()), 0, _ch_datetime.date(1, 1, 2), '', Classes_Charge=Classes_Bill()) == None


from python_code import Classes_CustomerProvides
from python_code import Classes_IFinanceImpl

def test_Classes_CustomerProvides___init__():
    assert Classes_CustomerProvides.__init__(Classes_CustomerProvides(Classes_CustomerProvides=Classes_IFinanceImpl()), Classes_CustomerProvides=Classes_IFinanceImpl()) == None

def test_Classes_CustomerProvides_makePayment():
    assert Classes_CustomerProvides.makePayment(Classes_CustomerProvides(Classes_CustomerProvides=Classes_IFinanceImpl()), '', '', '', '', '', '', '') == None

def test_Classes_CustomerProvides_isCreditCardValid():
    assert Classes_CustomerProvides.isCreditCardValid(Classes_CustomerProvides(Classes_CustomerProvides=Classes_IFinanceImpl()), '', '', '', '', '', '') == None


from python_code import Classes_IBookingManagement

def test_Classes_IBookingManagement___init__():
    assert Classes_IBookingManagement.__init__(Classes_IBookingManagement()) == None

def test_Classes_IBookingManagement_updateBooking():
    assert Classes_IBookingManagement.updateBooking(Classes_IBookingManagement(), '', '', '', '', '') == None

def test_Classes_IBookingManagement_confirmBooking():
    assert Classes_IBookingManagement.confirmBooking(Classes_IBookingManagement(), '') == None

def test_Classes_IBookingManagement_sendConfirmation():
    assert Classes_IBookingManagement.sendConfirmation(Classes_IBookingManagement(), '', '') == None

def test_Classes_IBookingManagement_createPendingBooking():
    assert Classes_IBookingManagement.createPendingBooking(Classes_IBookingManagement(), '', '', '') == None

def test_Classes_IBookingManagement_cancelBooking():
    assert Classes_IBookingManagement.cancelBooking(Classes_IBookingManagement(), '') == None

def test_Classes_IBookingManagement_addRoomPending():
    assert Classes_IBookingManagement.addRoomPending(Classes_IBookingManagement(), '', '') == None

def test_Classes_IBookingManagement_getRoomsOfBooking():
    assert Classes_IBookingManagement.getRoomsOfBooking(Classes_IBookingManagement(), '') == None

def test_Classes_IBookingManagement_addCustomerInformationToBooking():
    assert Classes_IBookingManagement.addCustomerInformationToBooking(Classes_IBookingManagement(), '', '', '', '', '') == None

def test_Classes_IBookingManagement_searchRoom():
    assert Classes_IBookingManagement.searchRoom(Classes_IBookingManagement(), '', '', '', '', '') == None

def test_Classes_IBookingManagement_addExtraCharge():
    assert Classes_IBookingManagement.addExtraCharge(Classes_IBookingManagement(), '', '', '') == None


from python_code import Classes_IFinance

def test_Classes_IFinance___init__():
    assert Classes_IFinance.__init__(Classes_IFinance()) == None

def test_Classes_IFinance_payBill():
    assert Classes_IFinance.payBill(Classes_IFinance(), '', '', '', '', '', '', '', '') == None

def test_Classes_IFinance_calculatePayment():
    assert Classes_IFinance.calculatePayment(Classes_IFinance(), '') == None

def test_Classes_IFinance_bankSendInvoice():
    assert Classes_IFinance.bankSendInvoice(Classes_IFinance()) == None


from python_code import Classes_IHotelManager

def test_Classes_IHotelManager___init__():
    assert Classes_IHotelManager.__init__(Classes_IHotelManager()) == None

def test_Classes_IHotelManager_getStaffMemberPhoneNumber():
    assert Classes_IHotelManager.getStaffMemberPhoneNumber(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_isValidUsername():
    assert Classes_IHotelManager.isValidUsername(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_getStaffMemberEmail():
    assert Classes_IHotelManager.getStaffMemberEmail(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_getStaffMemberFirstName():
    assert Classes_IHotelManager.getStaffMemberFirstName(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_logout():
    assert Classes_IHotelManager.logout(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_addStaffMember():
    assert Classes_IHotelManager.addStaffMember(Classes_IHotelManager(), '', '', '', '', '', '', '', '', '') == None

def test_Classes_IHotelManager_checkOut():
    assert Classes_IHotelManager.checkOut(Classes_IHotelManager(), '', '') == None

def test_Classes_IHotelManager_isStaffMemberAdmin():
    assert Classes_IHotelManager.isStaffMemberAdmin(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_changeStatusOfRoom():
    assert Classes_IHotelManager.changeStatusOfRoom(Classes_IHotelManager(), '', '', '') == None

def test_Classes_IHotelManager_login():
    assert Classes_IHotelManager.login(Classes_IHotelManager(), '', '') == None

def test_Classes_IHotelManager_getStaffMemberLastName():
    assert Classes_IHotelManager.getStaffMemberLastName(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_isStaffMemberLoggedIn():
    assert Classes_IHotelManager.isStaffMemberLoggedIn(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_isPasswordSecure():
    assert Classes_IHotelManager.isPasswordSecure(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_checkInBooking():
    assert Classes_IHotelManager.checkInBooking(Classes_IHotelManager(), '', '') == None

def test_Classes_IHotelManager_getStaffMemberAddress():
    assert Classes_IHotelManager.getStaffMemberAddress(Classes_IHotelManager(), '') == None

def test_Classes_IHotelManager_getStaffMemberPassword():
    assert Classes_IHotelManager.getStaffMemberPassword(Classes_IHotelManager(), '') == None


from python_code import Classes_IPerson

def test_Classes_IPerson___init__():
    assert Classes_IPerson.__init__(Classes_IPerson('', '', '', '', ''), '', '', '', '', '') == None


from python_code import Classes_IHotelManagerImpl
from python_code import Classes_StaffMember

def test_Classes_StaffMember___init__():
    assert Classes_StaffMember.__init__(Classes_StaffMember('\x00\x00', '', '', True, Classes_StaffMember=Classes_IHotelManagerImpl()), '', '', '', False, Classes_StaffMember=Classes_IHotelManagerImpl()) == None

