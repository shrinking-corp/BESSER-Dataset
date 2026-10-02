#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    Account,
    Bill,
    Booking,
    Classes_mdsdAccount_Account,
    Classes_mdsdAccount_AccountController,
    Classes_mdsdAccount_BookingToAccount,
    Classes_mdsdAccount_CustomerAccount,
    Classes_mdsdAccount_Pet,
    Classes_mdsdAdmin_Admin,
    Classes_mdsdAdmin_AdminController,
    Classes_mdsdAdmin_BookingToAdmin,
    Classes_mdsdAdmin_HotelStaff,
    Classes_mdsdAdmin_Room,
    Classes_mdsdAdmin_Staff,
    Classes_mdsdBilling_Bill,
    Classes_mdsdBilling_BillingController,
    Classes_mdsdBilling_BookingToBill,
    Classes_mdsdBilling_CustomerBilling,
    Classes_mdsdBilling_StaffBilling,
    Classes_mdsdBilling_Transaction,
    Classes_mdsdBooking_Booking,
    Classes_mdsdBooking_BookingController,
    Classes_mdsdBooking_Meal,
    Classes_mdsdBooking_Service,
    Classes_mdsdBooking_StaffBooking,
    Classes_mdsdBooking_UserBooking,
    HotelStaff,
    Meal,
    Pet,
    Room,
    Service,
    Transaction,
    abstractmethod,
    date,
    datetime,
    mdsdAccount_BookingToAccount,
    mdsdAccount_CustomerAccount,
    mdsdAdmin_Admin,
    mdsdAdmin_BookingToAdmin,
    mdsdAdmin_Staff,
    mdsdBilling_BookingToBill,
    mdsdBilling_CustomerBilling,
    mdsdBilling_StaffBilling,
    mdsdBooking_StaffBooking,
    mdsdBooking_UserBooking,
    time,
)


def test_0():
    var_41 = python_code_.Classes_mdsdAccount_Account(
        accountID='"v=f_\t@',
        password="Pet:_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController4:Room",
        name="n$2`<#c}Qb5",
        email="t( Z\x0c:Yns;h8'",
        isLoggedIn=False,
    )
    assert isinstance(var_41, python_code_.Classes_mdsdAccount_Account)


def test_1():
    var_6 = python_code_.Classes_mdsdBilling_Bill(
        isPaid=True, ID="mnvBw\rQQjs0\n>RE\tt}"
    )
    assert isinstance(var_6, python_code_.Classes_mdsdBilling_Bill)


def test_2():
    python_code_.HotelStaff()


def test_3():
    python_code_.Classes_mdsdAccount_CustomerAccount()


def test_4():
    python_code_.Classes_mdsdBooking_UserBooking()
    python_code_.Classes_mdsdBilling_StaffBilling()
    var_2 = python_code_.Classes_mdsdAccount_CustomerAccount()
    var_3 = python_code_.Room
    var_2.removePet(
        Classes_type={},
        Classes_accountID=var_3,
        Classes_name=b"\x9b\x9f:\x94}\xa8G\x06\xf0<\x86",
    )


def test_5():
    var_0 = python_code_.Service()
    var_1 = python_code_.Classes_mdsdAdmin_Staff()
    var_1.staffLogin(Classes_password=[-4223.79, 2285], Classes_ssn=var_0)
    var_3 = python_code_.Classes_mdsdAdmin_Room
    var_4 = python_code_.Classes_mdsdAccount_Account(
        accountID=",",
        password="y.|&X9HJ`,8G$uxc27",
        name="Pe\t",
        email="Dy3g\\n8T6jif_\\",
        isLoggedIn=True,
    )
    assert isinstance(var_4, python_code_.Classes_mdsdAccount_Account)
    var_6 = python_code_.Classes_mdsdAccount_BookingToAccount()
    var_6.getAccount(Classes_email=var_3)
    var_8 = python_code_.Classes_mdsdAccount_CustomerAccount()
    var_8.createAccount(
        Classes_customerName=-4086.73,
        Classes_password=var_6,
        Classes_customerEmail=True,
    )
    var_10 = "Booking-Room-_Classes_mdsdAdmin_AdminController__Classes_mdsdAdmin_AdminController11"
    var_11 = -1972
    python_code_.Classes_mdsdAdmin_Room(type=var_10, status=var_10, number=var_11)
    var_14 = python_code_.HotelStaff()
    var_16 = lambda *args, **kwargs: 3
    var_20 = python_code_.Classes_mdsdAdmin_Admin()
    var_20.modifyStaff(Classes_SSN=var_16, Classes_newRank=var_0, Classes_newName=-1)
    var_26 = python_code_.Classes_mdsdBilling_Bill(isPaid=False, ID=var_14)
    assert isinstance(var_26, python_code_.Classes_mdsdBilling_Bill)
    var_26.getTotalAmount()
    python_code_.Classes_mdsdBilling_StaffBilling()
    var_6.isUserLoggedIn(Classes_accountId=var_14)


def test_6():
    var_30 = python_code_.Classes_mdsdBooking_UserBooking()
    var_33 = python_code_.Classes_mdsdAdmin_Admin()
    var_52 = "_Classes_mdsdAccount_Account__Classes_mdsdAccount_Account"
    python_code_.Classes_mdsdAdmin_Room(
        type=("64vtG",),
        status=var_52,
        number=[
            2796,
            "_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController4",
            "'mKgLhjVM",
        ],
    )
    var_51 = python_code_.Classes_mdsdBooking_BookingController()
    assert isinstance(var_51, python_code_.Classes_mdsdBooking_BookingController)
    var_33.removeRoom(Classes_number=var_30)
    var_38 = python_code_.mdsdAccount_BookingToAccount
    var_39 = python_code_.Pet()
    var_41 = '07"o'
    python_code_.Classes_mdsdAccount_Pet(name=var_38, type=var_41)
    var_46 = python_code_.Classes_mdsdAccount_CustomerAccount()
    var_46.logout(Classes_accountId=var_39)


def test_7():
    var_0 = python_code_.Classes_mdsdBilling_StaffBilling()
    var_1 = lambda *args, **kwargs: []
    var_0.printReceipt(Classes_billID=var_1)
    var_3 = python_code_.Classes_mdsdBooking_Service(description=[], price=[])
    var_7 = python_code_.Classes_mdsdBilling_Bill(isPaid=var_1, ID=var_3)
    assert isinstance(var_7, python_code_.Classes_mdsdBilling_Bill)
    var_7.getTotalAmount()
    var_10 = python_code_.mdsdBooking_UserBooking()
    var_39 = python_code_.Classes_mdsdAdmin_AdminController()
    assert isinstance(var_39, python_code_.Classes_mdsdAdmin_AdminController)
    var_57 = python_code_.Classes_mdsdAccount_BookingToAccount()
    var_57.getAccount(Classes_email=var_1)
    var_59 = "~l'!r$UH^"
    python_code_.Classes_mdsdAccount_Pet(name=var_59, type=var_10)


def test_8():
    python_code_.Classes_mdsdAdmin_Staff()


def test_9():
    var_0 = python_code_.Service()
    var_1 = python_code_.Classes_mdsdAdmin_Staff()
    var_1.staffLogin(Classes_password=[-4223.79, 2285], Classes_ssn=var_0)
    var_3 = python_code_.Classes_mdsdAdmin_Room
    var_4 = python_code_.Classes_mdsdAccount_Account(
        accountID=var_3,
        password=var_0,
        name=(-287.07, "Booking-Room", 4068.9),
        email={},
        isLoggedIn=var_0,
    )
    assert isinstance(var_4, python_code_.Classes_mdsdAccount_Account)
    var_6 = python_code_.Classes_mdsdAccount_BookingToAccount()
    var_6.getAccount(Classes_email=var_3)
    python_code_.Classes_mdsdAccount_CustomerAccount()
    python_code_.Classes_mdsdBooking_UserBooking()
    var_56 = python_code_.Classes_mdsdAdmin_AdminController()
    assert isinstance(var_56, python_code_.Classes_mdsdAdmin_AdminController)
    var_58 = python_code_.mdsdBooking_UserBooking()
    var_59 = python_code_.Classes_mdsdBooking_BookingController(
        Classes_mdsdBooking_BookingController={var_56, var_58}
    )
    assert isinstance(var_59, python_code_.Classes_mdsdBooking_BookingController)
    var_60 = float
    var_59.getBookingList(Classes_email=var_60)


def test_10():
    python_code_.Classes_mdsdAdmin_Admin()


def test_11():
    var_30 = python_code_.Classes_mdsdBooking_UserBooking()
    var_33 = python_code_.Classes_mdsdAdmin_Admin()
    var_52 = "_Classes_mdsdAccount_Account__Classes_mdsdAccount_Account"
    python_code_.Classes_mdsdAdmin_Room(
        type=("64vtG",),
        status=var_52,
        number=[
            2796,
            "_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController4",
            "'mKgLhjVM",
        ],
    )
    var_51 = python_code_.Classes_mdsdBooking_BookingController()
    assert isinstance(var_51, python_code_.Classes_mdsdBooking_BookingController)
    var_33.removeRoom(Classes_number=var_30)
    var_55 = python_code_.Classes_mdsdAdmin_BookingToAdmin()
    var_56 = python_code_.Classes_mdsdAdmin_Admin()
    var_55.getPetTypes()
    python_code_.Classes_mdsdAccount_BookingToAccount()
    var_61 = -2914.13
    var_62 = "_~b"
    var_63 = True
    var_64 = python_code_.Classes_mdsdAccount_Account(
        accountID=var_62,
        password=complex(1040.8362679, 1867.84),
        name=584.49,
        email=var_61,
        isLoggedIn=var_63,
    )
    assert isinstance(var_64, python_code_.Classes_mdsdAccount_Account)
    var_56.createStaff(
        Classes_rank=var_55,
        Classes_name=-1986,
        Classes_SSN=(False, "IpyX,", 2077.38),
        Classes_password=False,
    )


def test_12():
    var_0 = python_code_.Classes_mdsdBilling_StaffBilling()
    var_1 = lambda *args, **kwargs: []
    var_0.printReceipt(Classes_billID=var_1)
    python_code_.Classes_mdsdBooking_Service(description=[], price=[])
    python_code_.Classes_mdsdBooking_StaffBooking()
    var_12 = python_code_.Classes_mdsdBooking_UserBooking()
    var_12.cancelBooking(Classes_bookingId=True)
    var_14 = python_code_.Classes_mdsdAdmin_Admin()
    var_15 = var_14.addRoom(
        Classes_type=var_1, Classes_status=var_1, Classes_room=[True, False]
    )
    var_16 = -1811.44
    python_code_.Classes_mdsdBilling_Transaction(description=var_15, price=var_16)
    var_21 = python_code_.Classes_mdsdBilling_BookingToBill()
    var_21.addTransaction(
        Classes_booking=3575,
        Classes_description=complex(-1551.0, -1031.8),
        Classes_amount=1030,
    )
    var_38 = python_code_.Classes_mdsdBooking_UserBooking()
    var_38.modifyBooking(Classes_bookingId=-1503)
    python_code_.Classes_mdsdAdmin_Staff()
    var_46 = False
    var_47 = python_code_.Classes_mdsdBilling_Bill(isPaid=var_46, ID=())
    assert isinstance(var_47, python_code_.Classes_mdsdBilling_Bill)


def test_13():
    var_1 = python_code_.Classes_mdsdBooking_UserBooking()
    var_2 = hash
    var_1.enterService(Classes_service=var_1, Classes_bookingId=var_2)
    var_4 = python_code_.Classes_mdsdAdmin_Admin()
    var_5 = var_4.removeStaff(Classes_SSN=var_4)
    var_6 = python_code_.Classes_mdsdBooking_BookingController(
        Classes_mdsdBooking_BookingController=var_5
    )
    assert isinstance(var_6, python_code_.Classes_mdsdBooking_BookingController)
    python_code_.Classes_mdsdBilling_StaffBilling()
    python_code_.Classes_mdsdAccount_CustomerAccount()


def test_14():
    var_0 = python_code_.Classes_mdsdBooking_StaffBooking()
    var_0.checkOut(Classes_rooms=var_0, Classes_bills=var_0, Classes_bookingID=var_0)
    var_2 = python_code_.Classes_mdsdBilling_StaffBilling()
    var_2.printReceipt(Classes_billID=var_0)
    var_5 = "G2xXvEP9d+Wri"
    var_6 = -1586.2
    var_7 = python_code_.Classes_mdsdBooking_Meal(
        foodType=var_5, schedule=[], amountOfFood=var_6, price="z`~_/\nT!"
    )
    var_8 = python_code_.Classes_mdsdAdmin_Admin()
    var_8.modifyStaff(
        Classes_SSN=var_7, Classes_newRank=(-77.83, False, 394), Classes_newName=var_7
    )


def test_15():
    python_code_.Classes_mdsdAccount_BookingToAccount()


def test_16():
    var_18 = python_code_.Classes_mdsdBooking_StaffBooking()
    var_19 = lambda *args, **kwargs: -2414
    var_18.checkIn(Classes_rooms=var_19, Classes_bookingID=set())
    python_code_.Classes_mdsdAdmin_Admin()
    var_30 = python_code_.Classes_mdsdAccount_BookingToAccount()
    var_30.getAccount(Classes_email=var_19)
    var_33 = -2914.13
    var_35 = "_~b"
    var_36 = True
    var_37 = python_code_.Classes_mdsdAccount_Account(
        accountID=var_35,
        password=complex(1040.8362679, 1867.84),
        name=584.49,
        email=var_33,
        isLoggedIn=var_36,
    )
    assert isinstance(var_37, python_code_.Classes_mdsdAccount_Account)
    var_39 = python_code_.Classes_mdsdBooking_UserBooking()
    var_39.modifyBooking(
        Classes_bookingId=b"\xf9\xda\tM$Iy\xd0\xd3\x07\xc0\xae@\xba\x013\xfd\x95:"
    )


def test_17():
    python_code_.Classes_mdsdBooking_StaffBooking()


def test_18():
    var_0 = python_code_.Classes_mdsdBooking_UserBooking()
    var_1 = python_code_.mdsdBilling_CustomerBilling
    var_0.enterDatesOfStay(
        Classes_stayTo=var_0,
        Classes_stayFrom=var_0,
        Classes_petType=None,
        Classes_rooms=var_1,
    )
    var_3 = python_code_.Classes_mdsdBilling_BillingController()
    var_4 = python_code_.Classes_mdsdBooking_StaffBooking()
    var_4.addNewService(Classes_description=var_3, Classes_price=False)


def test_19():
    python_code_.Classes_mdsdBooking_Service(
        description="_Classes_mdsdAdmin_AdminController__Classes_mdsdAdmin_AdminController:_Classes_mdsdAccount_Account__Classes_mdsdAccount_Account",
        price=1521.58,
    )


def test_20():
    python_code_.Classes_mdsdBilling_BookingToBill()


def test_21():
    python_code_.Classes_mdsdBilling_StaffBilling()


def test_22():
    var_0 = False
    var_1 = len
    var_2 = python_code_.Classes_mdsdBilling_Bill(isPaid=var_0, ID=var_1)
    assert isinstance(var_2, python_code_.Classes_mdsdBilling_Bill)
    var_4 = python_code_.Classes_mdsdBilling_StaffBilling()
    var_4.modifyBill(
        Classes_transaction=var_1, Classes_billID=var_0, Classes_newPrice=var_1
    )


def test_23():
    var_0 = python_code_.Classes_mdsdBooking_StaffBooking()
    var_0.checkOut(Classes_rooms=var_0, Classes_bills=var_0, Classes_bookingID=var_0)
    var_2 = python_code_.Classes_mdsdBilling_StaffBilling()
    var_2.printReceipt(Classes_billID=var_0)
    var_5 = "G2xXvEP9d+Wri"
    var_6 = -1586.22
    var_7 = python_code_.Classes_mdsdBooking_Meal(
        foodType=var_5, schedule=[], amountOfFood=var_6, price="z`~_/\nT!"
    )
    var_8 = python_code_.Classes_mdsdAdmin_Admin()
    var_8.modifyStaff(
        Classes_SSN=var_7, Classes_newRank=(-77.83, False, 394), Classes_newName=var_7
    )


def test_24():
    var_0 = python_code_.Classes_mdsdBilling_StaffBilling()
    var_1 = var_0.isPaid(Classes_billID=275.98)
    var_2 = python_code_.Classes_mdsdBooking_StaffBooking()
    var_3 = lambda *args, **kwargs: -2414
    var_2.checkIn(Classes_rooms=var_3, Classes_bookingID=set())
    var_0.modifyBill(
        Classes_transaction=var_1, Classes_billID=False, Classes_newPrice={}
    )


def test_25():
    var_0 = python_code_.Classes_mdsdAdmin_Admin()
    var_1 = python_code_.Classes_mdsdBooking_Meal
    var_0.modifyStaff(
        Classes_SSN=False,
        Classes_newRank=b"B\x8f|\xd5b\x1d\xce1\x8f\x99\xde\xa0\xe9",
        Classes_newName=var_1,
    )
    var_3 = python_code_.Classes_mdsdAccount_CustomerAccount()
    var_3.removePet(
        Classes_type=complex(184.9, -770.32),
        Classes_accountID=[],
        Classes_name=complex(-4261.958, -26.7),
    )
    var_6 = python_code_.Classes_mdsdBilling_StaffBilling()
    var_6.giveRefund(Classes_billId={}, Classes_transaction={})


def test_26():
    python_code_.Classes_mdsdBooking_UserBooking()


def test_27():
    var_0 = python_code_.Classes_mdsdBooking_UserBooking()
    var_0.enterCustomerInfo(
        Classes_rooms=var_0,
        Classes_customerName=3119,
        Classes_customerEmail=812.2,
        Classes_petName=var_0,
        Classes_booking=var_0,
    )


def test_28():
    var_0 = python_code_.mdsdBooking_UserBooking()
    var_1 = python_code_.Classes_mdsdAccount_AccountController()
    var_2 = python_code_.Classes_mdsdBooking_UserBooking()
    var_3 = var_2.enterMealInfo(
        Classes_bookingId=b"\xc2o\x81\xc0",
        Classes_foodType=var_1,
        Classes_schedule=var_0,
        Classes_amountOfFood=var_1,
        Classes_price=complex(3252.0, 2751.0430777),
    )
    var_4 = "_Classes_mdsdBilling_Bill__Classes_mdsdBilling_Bill.HotelStaff._Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController.HotelStaff"
    python_code_.Classes_mdsdAdmin_Room(type=(), status=var_4, number=var_3)
    var_7 = python_code_.Classes_mdsdAdmin_Admin()
    var_7.removeRoom(Classes_number=var_2)
    var_12 = python_code_.mdsdAccount_BookingToAccount
    var_2.enterCustomerInfo(
        Classes_rooms=var_12,
        Classes_customerName=var_12,
        Classes_customerEmail=var_0,
        Classes_petName=True,
        Classes_booking=[2324, True, 5506],
    )
    var_16 = '07"o'
    python_code_.Classes_mdsdAccount_Pet(name=var_12, type=var_16)


def test_29():
    python_code_.Classes_mdsdBilling_Transaction(
        description=complex(-899.5, 769.1), price=-65
    )


def test_30():
    python_code_.Classes_mdsdBooking_UserBooking()
    python_code_.Classes_mdsdAdmin_Admin()
    var_14 = False
    var_15 = "oxl\x0c"
    var_16 = python_code_.Classes_mdsdBilling_Bill(isPaid=var_14, ID=var_15)
    assert isinstance(var_16, python_code_.Classes_mdsdBilling_Bill)
    var_16.getTotalAmount()


def test_31():
    var_40 = python_code_.Classes_mdsdAdmin_AdminController()
    assert isinstance(var_40, python_code_.Classes_mdsdAdmin_AdminController)


def test_32():
    var_3 = python_code_.Classes_mdsdBooking_BookingController()
    assert isinstance(var_3, python_code_.Classes_mdsdBooking_BookingController)


def test_33():
    var_44 = python_code_.Classes_mdsdBooking_BookingController(
        Classes_mdsdBooking_BookingController4=set()
    )
    assert isinstance(var_44, python_code_.Classes_mdsdBooking_BookingController)


def test_34():
    python_code_.Classes_mdsdAdmin_BookingToAdmin()


def test_35():
    var_18 = python_code_.Classes_mdsdBooking_StaffBooking()
    var_19 = lambda *args, **kwargs: -2414
    var_18.checkIn(Classes_rooms=var_19, Classes_bookingID=set())
    var_26 = python_code_.Classes_mdsdAdmin_BookingToAdmin()
    var_27 = python_code_.Classes_mdsdAdmin_Admin()
    var_26.getPetTypes()
    var_30 = python_code_.Classes_mdsdAccount_BookingToAccount()
    var_30.getAccount(Classes_email=var_19)
    var_33 = -2914.13
    var_35 = "_~b"
    var_36 = True
    var_37 = python_code_.Classes_mdsdAccount_Account(
        accountID=var_35,
        password=complex(1040.8362679, 1867.84),
        name=584.49,
        email=var_33,
        isLoggedIn=var_36,
    )
    assert isinstance(var_37, python_code_.Classes_mdsdAccount_Account)
    var_27.createStaff(
        Classes_rank=var_26,
        Classes_name=-1986,
        Classes_SSN=(False, "IpyX,", 2077.38),
        Classes_password=False,
    )


def test_36():
    python_code_.Classes_mdsdBooking_Meal(
        foodType=set(),
        schedule=";[Q4_(*7&^I+D",
        amountOfFood=127.22,
        price={"hAMmQIf": 376, "6\\bW": True},
    )


def test_37():
    python_code_.Classes_mdsdBooking_StaffBooking()
    python_code_.Classes_mdsdAdmin_BookingToAdmin()
    python_code_.Classes_mdsdBooking_UserBooking()
    var_41 = python_code_.Classes_mdsdAdmin_AdminController()
    assert isinstance(var_41, python_code_.Classes_mdsdAdmin_AdminController)
    var_43 = python_code_.mdsdBooking_UserBooking()
    var_44 = python_code_.Classes_mdsdBooking_BookingController(
        Classes_mdsdBooking_BookingController={var_41, var_43}
    )
    assert isinstance(var_44, python_code_.Classes_mdsdBooking_BookingController)
    var_45 = float
    var_44.getBookingList(Classes_email=var_45)


def test_38():
    var_41 = python_code_.Classes_mdsdAccount_Account(
        accountID='"v=f_\t@',
        password="Pet:_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController4:Room",
        name="n$2`<#c}Qb5",
        email="t( Z\x0c:Yns;h8'",
        isLoggedIn=False,
    )
    assert isinstance(var_41, python_code_.Classes_mdsdAccount_Account)
    var_42 = python_code_.Bill()
    var_43 = python_code_.Classes_mdsdAccount_CustomerAccount()
    var_44 = var_43.addPet(
        Classes_name=var_42, Classes_type=None, Classes_accountID=var_42
    )
    var_45 = python_code_.Classes_mdsdAdmin_AdminController(
        Classes_mdsdAdmin_AdminController=var_44
    )
    assert isinstance(var_45, python_code_.Classes_mdsdAdmin_AdminController)
    var_45.isLoggedIn(Classes_ssn=-1254)


def test_39():
    var_0 = python_code_.HotelStaff()
    var_1 = python_code_.Classes_mdsdAccount_BookingToAccount()
    var_1.isUserLoggedIn(Classes_accountId=var_0)


def test_40():
    var_3 = python_code_.Classes_mdsdBooking_BookingController(
        Classes_mdsdBooking_BookingController={-3343, -2986.69, "[~^Y.-"}
    )
    assert isinstance(var_3, python_code_.Classes_mdsdBooking_BookingController)


def test_41():
    var_1 = python_code_.Classes_mdsdBooking_UserBooking()
    var_2 = hash
    var_1.enterService(Classes_service=var_1, Classes_bookingId=var_2)


def test_42():
    var_0 = python_code_.Classes_mdsdBilling_StaffBilling()
    var_1 = lambda *args, **kwargs: []
    var_0.printReceipt(Classes_billID=var_1)
    var_3 = python_code_.Classes_mdsdBooking_Service(description=[], price=[])
    python_code_.Classes_mdsdBooking_StaffBooking()
    var_7 = python_code_.Classes_mdsdBilling_Bill(isPaid=var_1, ID=var_3)
    assert isinstance(var_7, python_code_.Classes_mdsdBilling_Bill)
    var_7.getTotalAmount()
    python_code_.Classes_mdsdBooking_UserBooking()
    var_39 = python_code_.Classes_mdsdAdmin_AdminController()
    assert isinstance(var_39, python_code_.Classes_mdsdAdmin_AdminController)
    var_58 = python_code_.Classes_mdsdAdmin_Staff()
    var_58.staffLogout(Classes_ssn=None)


def test_43():
    var_40 = python_code_.Classes_mdsdAdmin_AdminController(
        Classes_mdsdAdmin_AdminController=set()
    )
    assert isinstance(var_40, python_code_.Classes_mdsdAdmin_AdminController)


def test_44():
    var_6 = python_code_.Classes_mdsdBilling_Bill(
        isPaid=True, ID="A", Classes_mdsdBilling_Bill=set()
    )
    assert isinstance(var_6, python_code_.Classes_mdsdBilling_Bill)


def test_45():
    python_code_.Classes_mdsdBooking_StaffBooking()
    python_code_.Classes_mdsdAdmin_BookingToAdmin()
    python_code_.Classes_mdsdBooking_UserBooking()
    var_41 = python_code_.Classes_mdsdAdmin_AdminController()
    assert isinstance(var_41, python_code_.Classes_mdsdAdmin_AdminController)
    python_code_.Classes_mdsdAccount_BookingToAccount()
    var_64 = python_code_.Classes_mdsdAdmin_Staff()
    var_64.changeRoomStatus(Classes_roomNumber="==Z?", Classes_status=var_41)


def test_46():
    var_40 = python_code_.Classes_mdsdAdmin_AdminController(
        Classes_mdsdAdmin_AdminController11={True, True}
    )
    assert isinstance(var_40, python_code_.Classes_mdsdAdmin_AdminController)


def test_47():
    var_50 = python_code_.Classes_mdsdBooking_Booking(
        roomNumber=-2476,
        dateFrom=None,
        dateTo=None,
        bill_Id="[> /g\\",
        petName="s/JXH1dW",
        customerName="Transaction",
        customerEmail="",
        bookingId="",
        isCheckedIn=True,
        isCheckedOut=False,
    )
    assert isinstance(var_50, python_code_.Classes_mdsdBooking_Booking)


def test_48():
    python_code_.Classes_mdsdAccount_BookingToAccount()
    var_41 = python_code_.Classes_mdsdAccount_Account(
        accountID="$lU0Z0%+\x0b7K",
        password="_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController4 _Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController4 _Classes_mdsdBooking_Booking__Classes_mdsdBooking_Booking _Classes_mdsdBilling_Bill__Classes_mdsdBilling_Bill",
        name="\tm",
        email="ZSF",
        isLoggedIn=False,
        Classes_mdsdAccount_Account=set(),
    )
    assert isinstance(var_41, python_code_.Classes_mdsdAccount_Account)
    var_43 = python_code_.mdsdAccount_CustomerAccount()
    var_44 = python_code_.Classes_mdsdAccount_CustomerAccount()
    var_44.login(Classes_email=1, Classes_password=var_43)


def test_49():
    var_1 = python_code_.Classes_mdsdBooking_UserBooking()
    python_code_.Classes_mdsdAdmin_Admin()
    python_code_.Classes_mdsdAccount_CustomerAccount()
    var_21 = "Dq0|"
    var_22 = python_code_.Classes_mdsdAdmin_Room
    var_23 = True
    python_code_.Classes_mdsdAdmin_HotelStaff(
        Name=var_21, rank=var_21, SSN=var_22, isLoggedIn=var_23, password=var_1
    )


def test_50():
    var_2 = "r.\x0bTEpbr(~f@"
    var_47 = python_code_.Classes_mdsdBooking_Booking(
        roomNumber=667,
        dateFrom=var_2,
        dateTo=var_2,
        bill_Id="_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController.Service6",
        petName="_Classes_mdsdBooking_Booking__Classes_mdsdBooking_Booking:_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController:Transaction",
        customerName="EE(",
        customerEmail="_Classes_mdsdBilling_Bill__Classes_mdsdBilling_Bill",
        bookingId=var_2,
        isCheckedIn=True,
        isCheckedOut=True,
        Classes_mdsdBooking_Booking8=var_2,
    )
    assert isinstance(var_47, python_code_.Classes_mdsdBooking_Booking)


def test_51():
    var_41 = python_code_.Classes_mdsdAccount_Account(
        accountID='t+S{&"\t',
        password="A\rU4,^9|(_<",
        name="Transaction",
        email='vu(\teL9)a1hd,(i)"',
        isLoggedIn=False,
        Classes_mdsdAccount_Account={2, 2672},
    )
    assert isinstance(var_41, python_code_.Classes_mdsdAccount_Account)


def test_52():
    var_50 = python_code_.Classes_mdsdBooking_Booking(
        roomNumber=189,
        dateFrom=None,
        dateTo=None,
        bill_Id="y\\",
        petName="_Classes_mdsdBooking_Booking__Classes_mdsdBooking_Booking8",
        customerName="5NzihPuhs\\SlO:Jd",
        customerEmail="7g",
        bookingId="_Classes_mdsdBooking_BookingController__Classes_mdsdBooking_BookingController4",
        isCheckedIn=True,
        isCheckedOut=True,
        Classes_mdsdBooking_Booking=set(),
    )
    assert isinstance(var_50, python_code_.Classes_mdsdBooking_Booking)
