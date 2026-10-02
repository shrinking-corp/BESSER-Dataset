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
    Backend_CodePack_BankComponent,
    Booking,
    CheckInHandler,
    CodePack_Backend_CheckInHandler,
    CodePack_Backend_CustomerHandler,
    CodePack_Backend_ManagementHandler,
    CodePack_Backend_ReceptionHandler,
    CodePack_CheckInMachine,
    CodePack_DataBank,
    CodePack_DataModels_Bill,
    CodePack_DataModels_Booking,
    CodePack_DataModels_Customer,
    CodePack_DataModels_ExtraService,
    CodePack_DataModels_Guest,
    CodePack_DataModels_PaymentData,
    CodePack_DataModels_Room,
    CodePack_DataModels_RoomBooked,
    CodePack_DataModels_RoomType,
    CodePack_DataModels_ServiceType,
    CodePack_DataModels_StaffMember,
    CodePack_DataModels_StaffRole,
    CodePack_IBookings,
    CodePack_ICheckIn,
    CodePack_IManagement,
    CodePack_IReceptionOperations_rename_required,
    CodePack_IStaffAdmin,
    CodePack_IStaffAuthentication,
    CodePack_IUserAccount,
    CodePack_Shared_ContactData,
    CodePack_StaffGUI,
    CodePack_UserGUI,
    Customer,
    CustomerHandler,
    ExtraService,
    Guest,
    IBookings,
    ICheckIn,
    IManagement,
    IReceptionOperations_rename_required,
    IStaffAdmin,
    IStaffAuthentication,
    IUserAccount,
    ManagementHandler,
    PaymentData,
    ReceptionHandler,
    Room,
    RoomBooked,
    RoomType,
    ServiceType,
    StaffMember,
    StaffRole,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_5 = python_code_.CodePack_DataModels_Bill(booking_id=-2358, total_price=881.55)
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)


def test_1():
    python_code_.CodePack_CheckInMachine()


def test_2():
    python_code_.CodePack_UserGUI()


def test_3():
    python_code_.CodePack_StaffGUI(CodePack_StaffGUI=None)


def test_4():
    var_60 = python_code_.CodePack_StaffGUI(CodePack_StaffGUI=-3136.66)
    assert isinstance(var_60, python_code_.CodePack_StaffGUI)


def test_5():
    python_code_.CodePack_IUserAccount()


def test_6():
    var_0 = python_code_.CodePack_IManagement()
    var_1 = var_0.updateRoomType(CodePack_roomType=[])
    var_2 = -4064.3
    var_3 = python_code_.CodePack_DataModels_ServiceType(
        description=var_0, type_name=var_1, price=var_2
    )
    var_4 = python_code_.CodePack_IStaffAdmin()
    var_5 = var_4.updateStaffAccount(CodePack_account=var_0)
    var_6 = python_code_.CodePack_IUserAccount()
    var_7 = var_6.updateCustomerPwd(
        CodePack_customer_id=var_3, CodePack_pwd_old=(), CodePack_pwd_new=var_5
    )
    var_8 = var_0.removeServiceType(CodePack_serviceType=var_1)
    var_6.registerCustomer(
        CodePack_date_of_birth=False,
        CodePack_password=var_7,
        CodePack_phone_no=var_0,
        CodePack_last_name=True,
        CodePack_e_mail=var_0,
        CodePack_first_name=var_2,
    )
    var_10 = var_0.removeServiceType(CodePack_serviceType=[4100, "{\tb\t", "_Ip-%\nU7"])
    var_11 = python_code_.StaffMember
    var_12 = python_code_.CodePack_DataModels_ServiceType(
        description=var_10,
        type_name=var_11,
        price=[";+-V\x0cpb7W4[\r", "qB|}JJ\tKN^Yg(r"],
    )
    var_13 = python_code_.CodePack_IBookings()
    var_13.createBooking(
        CodePack_number_of_guests=var_13,
        CodePack_payment_data=var_2,
        CodePack_date_check_out=var_12,
        CodePack_contact_data={
            ">&QwX*Ywf<y=t",
            "ReceptionHandler-_CodePack_DataModels_RoomBooked__CodePack_DataModels_RoomBooked",
            2079,
        },
        CodePack_date_check_in=-1349.95,
        CodePack_services=var_8,
        CodePack_rooms=var_11,
    )
    var_4.removeStaffAccount(CodePack_account=var_11)
    var_16 = ""
    var_17 = -3884
    python_code_.CodePack_DataModels_Guest(name=var_16, booking_id=var_17)
    var_13.getBookingsForCustomer(CodePack_customer_id=-1)


def test_7():
    var_0 = (
        lambda *args, **kwargs: "_CodePack_UserGUI__CodePack_UserGUI _CodePack_StaffGUI__CodePack_StaffGUI CustomerHandler _CodePack_DataModels_Bill__CodePack_DataModels_Bill31"
    )
    python_code_.CodePack_DataModels_Guest(name=var_0, booking_id=var_0)
    var_2 = python_code_.CodePack_IManagement()
    var_2.getServiceTypes()
    var_4 = python_code_.CodePack_IStaffAuthentication()
    var_4.login(CodePack_password=var_0, CodePack_e_mail=var_0)


def test_8():
    var_0 = python_code_.CodePack_IStaffAdmin()
    var_1 = "CheckInHandler.Booking"
    var_2 = -1162
    var_3 = python_code_.CodePack_IStaffAdmin
    var_4 = python_code_.CodePack_DataModels_PaymentData(
        cc_number=(),
        cc_ccv=var_1,
        cc_month=var_2,
        cc_year=var_0,
        cc_first_name=var_3,
        cc_last_name=var_3,
        id=var_2,
    )
    var_5 = python_code_.CodePack_DataModels_StaffMember(
        full_name=var_2,
        email={"s[]uu?vv@r>#np": True, "Room34": "!14cM", "&%Me\x0b": True},
        password=var_1,
        pers_no=var_4,
        phone_no=var_3,
        role_name=var_1,
    )
    var_6 = python_code_.CodePack_Backend_CustomerHandler()
    var_7 = python_code_.CodePack_IBookings()
    var_7.createBookingForCustomer(
        CodePack_date_check_out=var_5,
        CodePack_number_of_guests={},
        CodePack_date_check_in=var_0,
        CodePack_bonus_points_used=var_6,
        CodePack_customer_id=(717.39, 965.22, 0),
        CodePack_rooms=[False, -1928.23, -3655.14],
        CodePack_services=var_3,
    )


def test_9():
    python_code_.CodePack_IBookings()
    var_3 = ""
    var_4 = "O#.4`C'+u_\x0cr,wL{z%"
    python_code_.CodePack_DataModels_PaymentData(
        cc_number=var_3,
        cc_ccv=complex(737.92, -2301.252),
        cc_month=b"e\xaf\xf9\xf8",
        cc_year={},
        cc_first_name=var_4,
        cc_last_name=var_3,
        id=set(),
    )


def test_10():
    var_0 = python_code_.IBookings()
    var_1 = python_code_.CodePack_IManagement()
    var_2 = python_code_.CodePack_DataModels_StaffMember
    var_3 = lambda *args, **kwargs: 1008
    var_1.addRoomType(
        CodePack_name=var_2,
        CodePack_description=var_2,
        CodePack_rate=var_2,
        CodePack_max_guests=var_3,
    )
    var_6 = python_code_.CodePack_IBookings()
    var_6.updateRoomForBooking(
        CodePack_booking_id=-1920, CodePack_old_room=var_1, CodePack_new_room=var_0
    )
    var_8 = python_code_.CodePack_IStaffAdmin()
    var_1.updateServiceType(CodePack_serviceType=var_2)
    var_13 = "~9U4{KB+mRn#023Q4P"
    python_code_.CodePack_DataModels_Room(
        number={}, description=("Room", True), isAvailable=var_8, room_type=var_13
    )


def test_11():
    python_code_.CodePack_ICheckIn()


def test_12():
    var_65 = -1647
    var_66 = python_code_.CodePack_DataModels_ExtraService
    python_code_.CodePack_DataModels_RoomBooked(
        room_number=2269, booking_id=var_65, date_start=None, date_end=None
    )
    var_69 = python_code_.CodePack_ICheckIn()
    var_69.assignGuestToBooking(CodePack_guest_name={}, CodePack_booking_id=var_66)


def test_13():
    var_0 = python_code_.CodePack_StaffGUI(CodePack_StaffGUI=None)
    var_0.startUI()
    var_2 = python_code_.CodePack_UserGUI()
    var_2.startUI()
    var_4 = python_code_.CodePack_CheckInMachine()
    var_4.startUI()
    var_6 = python_code_.CodePack_IManagement()
    var_7 = python_code_.IStaffAdmin
    var_6.addRoomType(
        CodePack_name=complex(-3511.1394, -5501.22),
        CodePack_description=complex(-2069.253, 704.9933),
        CodePack_rate={
            "!*\x0bz#": "_CodePack_StaffGUI__CodePack_StaffGUI2,Room34,_CodePack_StaffGUI__CodePack_StaffGUI,ReceptionHandler",
            "r7tD;XRg- &{h\x0bzzT": False,
        },
        CodePack_max_guests=var_7,
    )
    var_9 = python_code_.CodePack_IReceptionOperations_rename_required()
    var_9.generateBill(CodePack_booking_id=var_6)


def test_14():
    var_0 = python_code_.StaffMember
    var_1 = python_code_.CodePack_StaffGUI(CodePack_StaffGUI=var_0)
    var_1.startUI()
    python_code_.CodePack_IUserAccount()
    python_code_.CodePack_CheckInMachine()


def test_15():
    python_code_.CodePack_IStaffAuthentication()


def test_16():
    var_0 = python_code_.CodePack_IStaffAdmin()
    var_1 = var_0.updateStaffAccount(CodePack_account=var_0)
    var_2 = python_code_.CodePack_IBookings()
    var_3 = var_2.createBookingForCustomer(
        CodePack_date_check_out=var_1,
        CodePack_number_of_guests=var_0,
        CodePack_date_check_in=var_1,
        CodePack_bonus_points_used=var_2,
        CodePack_customer_id=var_0,
        CodePack_rooms="QOCg(ezF.UhSgRn",
        CodePack_services=(False, -2898.37),
    )
    var_4 = list
    var_5 = 2
    var_6 = ""
    var_7 = 3744
    python_code_.CodePack_DataModels_PaymentData(
        cc_number=var_4,
        cc_ccv=var_3,
        cc_month=var_5,
        cc_year=var_5,
        cc_first_name=var_4,
        cc_last_name=var_6,
        id=var_7,
    )
    var_9 = python_code_.CodePack_UserGUI()
    var_9.startUI()
    var_12 = python_code_.CodePack_IUserAccount()
    var_2.getAvailableServices()
    var_17 = python_code_.CodePack_ICheckIn()
    var_17.assignGuestToBooking(CodePack_guest_name=var_6, CodePack_booking_id=var_12)
    var_20 = python_code_.CodePack_IStaffAuthentication()
    var_20.getRoleForStaff(CodePack_pers_no={})
    var_49 = -502
    var_50 = 129.08
    var_51 = python_code_.CodePack_IManagement()
    var_52 = var_51.getRoom(CodePack_number=var_51)
    var_53 = python_code_.CodePack_DataModels_Bill(
        booking_id=var_49, total_price=var_50, CodePack_DataModels_Bill31=var_52
    )
    assert isinstance(var_53, python_code_.CodePack_DataModels_Bill)
    var_0.removeStaffRole(CodePack_role=3592)
    var_0.getAllStaffAccounts()


def test_17():
    python_code_.CodePack_IManagement()


def test_18():
    var_0 = python_code_.CodePack_IBookings()
    var_1 = var_0.createBooking(
        CodePack_number_of_guests="",
        CodePack_payment_data=var_0,
        CodePack_date_check_out=var_0,
        CodePack_contact_data={"D8g,Wn1\tf'- \"k]I2"},
        CodePack_date_check_in=var_0,
        CodePack_services={
            'bXEU\nSWXkn:-\x0cWUcE6"': "_CodePack_DataModels_Booking__CodePack_DataModels_Booking"
        },
        CodePack_rooms=var_0,
    )
    python_code_.CodePack_ICheckIn()
    var_3 = -1593
    var_4 = -3061.48
    var_5 = python_code_.CodePack_DataModels_Bill(booking_id=var_3, total_price=var_4)
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)
    var_0.updateTimeForBooking(
        CodePack_booking_id=var_0,
        CodePack_new_check_in=var_3,
        CodePack_new_check_out=var_4,
    )
    var_0.getPaymentForBooking(CodePack_booking_id=var_1)
    python_code_.CodePack_IUserAccount()
    var_49 = python_code_.CodePack_IManagement()
    var_49.removeServiceType(CodePack_serviceType=var_0)


def test_19():
    var_1 = "CheckInHandler.Booking"
    python_code_.CodePack_IBookings()
    var_10 = python_code_.CodePack_IStaffAdmin()
    var_11 = var_10.updateStaffRole(CodePack_role=var_1)
    var_13 = python_code_.CodePack_IManagement()
    var_13.removeServiceType(CodePack_serviceType=var_11)
    python_code_.CodePack_IUserAccount()
    var_15 = lambda *args, **kwargs: []
    var_13.addRoomType(
        CodePack_name=5725,
        CodePack_description=-32.67,
        CodePack_rate=var_15,
        CodePack_max_guests=var_1,
    )
    var_13.updateRoomType(CodePack_roomType=var_15)


def test_20():
    python_code_.CodePack_IStaffAdmin()


def test_21():
    var_0 = python_code_.CodePack_IStaffAdmin()
    var_0.updateStaffAccount(CodePack_account=var_0)
    python_code_.CodePack_IBookings()
    var_4 = list
    var_6 = ""
    python_code_.CodePack_UserGUI()
    var_12 = python_code_.CodePack_IUserAccount()
    python_code_.CodePack_CheckInMachine()
    var_12.login(CodePack_e_mail=var_4, CodePack_password=var_6)
    var_0.getStaffAccount(CodePack_pers_no=var_4)


def test_22():
    var_0 = python_code_.CodePack_IManagement()
    var_1 = python_code_.PaymentData()
    var_3 = python_code_.CodePack_IUserAccount()
    var_4 = python_code_.CodePack_Backend_CheckInHandler
    var_3.updateCustomerCC(
        CodePack_cc_month="9\\ItjvP#=UzF7]-w+@",
        CodePack_name_last=var_3,
        CodePack_customer_id=var_1,
        CodePack_cc_year=var_1,
        CodePack_cc_ccv=var_4,
        CodePack_name_first=var_0,
        CodePack_cc_number=set(),
    )
    var_6 = python_code_.CodePack_ICheckIn()
    var_6.validateBooking(CodePack_booking_id=var_3)
    var_8 = python_code_.IReceptionOperations_rename_required()
    var_9 = python_code_.CodePack_IBookings()
    var_9.updateRoomForBooking(
        CodePack_booking_id=var_0, CodePack_old_room=var_4, CodePack_new_room=var_4
    )
    var_3.isEmailAvailable(CodePack_e_mail=var_4)
    var_9.isRoomAvailable(
        CodePack_date_end=2378.33, CodePack_room_number=var_3, CodePack_date_start=var_8
    )
    var_14 = "_CodePack_DataModels_Bill__CodePack_DataModels_Bill31"
    var_15 = 2
    python_code_.CodePack_DataModels_Guest(name=var_14, booking_id=var_15)
    var_19 = python_code_.CodePack_IStaffAdmin()
    var_19.removeStaffAccount(CodePack_account=[1287, -151, "Booking"])
    var_0.updateRoom(CodePack_room=(-1, 2506, 2426))


def test_23():
    var_0 = python_code_.CodePack_Backend_CustomerHandler()
    var_1 = python_code_.CodePack_IStaffAdmin()
    var_1.registerStaffAccount(
        CodePack_pers_no="0L0*gl",
        CodePack_email=var_1,
        CodePack_phone_no=var_0,
        CodePack_name={1751, 1831.63, True},
        CodePack_role_name=complex(1460.12, 3101.752),
    )
    var_3 = python_code_.CodePack_IBookings()
    var_3.getPaymentForBooking(CodePack_booking_id=())


def test_24():
    var_0 = python_code_.CodePack_IBookings()
    var_1 = var_0.createBooking(
        CodePack_number_of_guests="",
        CodePack_payment_data=var_0,
        CodePack_date_check_out=var_0,
        CodePack_contact_data={"D8g,Wn1\tf'- \"k]I2"},
        CodePack_date_check_in=var_0,
        CodePack_services={
            'bXEU\nSWXkn:-\x0cWUcE6"': "_CodePack_DataModels_Booking__CodePack_DataModels_Booking"
        },
        CodePack_rooms=var_0,
    )
    var_2 = python_code_.CodePack_ICheckIn()
    var_3 = -1593
    var_4 = -3061.48
    var_5 = python_code_.CodePack_DataModels_Bill(booking_id=var_3, total_price=var_4)
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)
    var_6 = "_CodePack_DataModels_Booking__CodePack_DataModels_Booking-CustomerHandler-ExtraService-_CodePack_DataModels_RoomBooked__CodePack_DataModels_RoomBooked"
    var_7 = "cfqhQO"
    python_code_.CodePack_DataModels_PaymentData(
        cc_number=complex(310.0, -460.7),
        cc_ccv={
            "ReceptionHandler": '[tB8"',
            "ExtraService32": -4126,
            "_CodePack_UserGUI__CodePack_UserGUI ReceptionHandler": 642,
        },
        cc_month=var_3,
        cc_year=var_3,
        cc_first_name=var_6,
        cc_last_name=var_7,
        id=var_1,
    )
    var_9 = var_0.createBooking(
        CodePack_number_of_guests=var_4,
        CodePack_payment_data=True,
        CodePack_date_check_out=False,
        CodePack_contact_data=None,
        CodePack_date_check_in=var_4,
        CodePack_services=var_2,
        CodePack_rooms={"f<'Wq^,<+5 ,]#e(E"},
    )
    var_0.updateTimeForBooking(
        CodePack_booking_id=var_0,
        CodePack_new_check_in=var_3,
        CodePack_new_check_out=var_4,
    )
    var_0.getPaymentForBooking(CodePack_booking_id=var_1)
    var_13 = python_code_.CodePack_IUserAccount()
    var_13.updateCustomerInfo(
        CodePack_phone_no=var_13, CodePack_customer_id=var_9, CodePack_e_mail=1
    )


def test_25():
    var_0 = python_code_.StaffMember
    var_1 = python_code_.CodePack_StaffGUI(CodePack_StaffGUI=var_0)
    var_1.startUI()
    var_4 = python_code_.CodePack_IUserAccount()
    var_4.updateCustomerCC(
        CodePack_cc_month=False,
        CodePack_name_last=var_4,
        CodePack_customer_id=set(),
        CodePack_cc_year=2138.96,
        CodePack_cc_ccv=var_0,
        CodePack_name_first=var_0,
        CodePack_cc_number=[True],
    )
    var_4.getCustomerInfo(CodePack_customer_id={False})
    python_code_.CodePack_IBookings()
    var_36 = python_code_.CodePack_IUserAccount()
    var_36.isEmailAvailable(CodePack_e_mail=False)


def test_26():
    var_3 = python_code_.CodePack_IUserAccount()
    var_3.isEmailAvailable(CodePack_e_mail=False)


def test_27():
    python_code_.CodePack_IBookings()
    var_58 = python_code_.StaffMember()
    var_59 = python_code_.CodePack_UserGUI(CodePack_UserGUI=var_58)
    var_63 = python_code_.CodePack_IUserAccount()
    python_code_.CodePack_CheckInMachine()
    var_65 = list
    var_63.updateCustomerCC(
        CodePack_cc_month=var_59,
        CodePack_name_last=var_65,
        CodePack_customer_id=var_58,
        CodePack_cc_year={},
        CodePack_cc_ccv=var_65,
        CodePack_name_first=var_65,
        CodePack_cc_number=var_65,
    )


def test_28():
    python_code_.CodePack_IBookings()


def test_29():
    var_0 = python_code_.CodePack_IBookings()
    var_1 = lambda *args, **kwargs: []
    var_0.updateRoomForBooking(
        CodePack_booking_id=var_1, CodePack_old_room=var_1, CodePack_new_room=var_1
    )
    var_3 = python_code_.CodePack_IUserAccount()
    var_3.isEmailAvailable(CodePack_e_mail=False)


def test_30():
    var_0 = python_code_.CodePack_IBookings()
    var_0.createBooking(
        CodePack_number_of_guests="",
        CodePack_payment_data=var_0,
        CodePack_date_check_out=var_0,
        CodePack_contact_data={"D8g,Wn1\tf'- \"k]I2"},
        CodePack_date_check_in=var_0,
        CodePack_services={
            'bXEU\nSWXkn:-\x0cWUcE6"': "_CodePack_DataModels_Booking__CodePack_DataModels_Booking"
        },
        CodePack_rooms=var_0,
    )
    python_code_.CodePack_ICheckIn()
    var_3 = -1593
    var_4 = -3061.48
    var_5 = python_code_.CodePack_DataModels_Bill(
        booking_id=var_3,
        total_price=1743.9,
        CodePack_DataModels_Bill={False},
        CodePack_DataModels_Bill31={var_4, var_4, var_0},
    )
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)
    python_code_.CodePack_IUserAccount()
    var_54 = python_code_.CodePack_CheckInMachine()
    var_54.startUI()


def test_31():
    var_1 = python_code_.CodePack_IManagement()
    var_1.getAllRooms()


def test_32():
    var_5 = python_code_.CodePack_DataModels_Bill(
        booking_id=-1438, total_price=1965.8, CodePack_DataModels_Bill=set()
    )
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)


def test_33():
    var_5 = python_code_.CodePack_DataModels_Bill(
        booking_id=3,
        total_price=2489.2,
        CodePack_DataModels_Bill=set(),
        CodePack_DataModels_Bill31=set(),
    )
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)


def test_34():
    python_code_.CodePack_IUserAccount()
    var_7 = python_code_.CodePack_CheckInMachine()
    var_7.startUI()


def test_35():
    var_0 = -2046
    var_1 = -631.02
    var_2 = python_code_.CodePack_DataModels_Bill(
        booking_id=var_0, total_price=var_1, CodePack_DataModels_Bill31=None
    )
    assert isinstance(var_2, python_code_.CodePack_DataModels_Bill)
    var_3 = -1855
    var_4 = set
    python_code_.CodePack_DataModels_RoomBooked(
        room_number=var_0, booking_id=var_3, date_start=var_4, date_end=var_4
    )
    var_6 = python_code_.CodePack_IManagement()
    var_6.removeRoom(CodePack_number=var_4)


def test_36():
    var_48 = python_code_.CodePack_IReceptionOperations_rename_required()
    var_48.isCheckedIn(CodePack_booking_id=None)
    python_code_.CodePack_IStaffAuthentication()


def test_37():
    var_0 = python_code_.CodePack_IBookings()
    var_0.createBooking(
        CodePack_number_of_guests="",
        CodePack_payment_data=var_0,
        CodePack_date_check_out=var_0,
        CodePack_contact_data={"D8g,Wn1\tf'- \"k]I2"},
        CodePack_date_check_in=var_0,
        CodePack_services={
            'bXEU\nSWXkn:-\x0cWUcE6"': "_CodePack_DataModels_Booking__CodePack_DataModels_Booking"
        },
        CodePack_rooms=var_0,
    )
    var_57 = lambda *args, **kwargs: "_CodePack_StaffGUI__CodePack_StaffGUI2"
    var_62 = python_code_.CodePack_IReceptionOperations_rename_required()
    var_62.generateReceipt(CodePack_bill=965.12)
    var_64 = python_code_.CodePack_ICheckIn()
    var_64.assignGuestToBooking(CodePack_guest_name=var_57, CodePack_booking_id=-1300)
    var_0.sendComfimationMail(CodePack_booking=complex(933.0134445, -760.05))


def test_38():
    python_code_.CodePack_IBookings()
    python_code_.CodePack_ICheckIn()
    var_68 = ""
    python_code_.CodePack_UserGUI()
    var_72 = python_code_.CodePack_IUserAccount()
    python_code_.CodePack_CheckInMachine()
    var_74 = python_code_.CodePack_Backend_CustomerHandler
    var_72.login(CodePack_e_mail=var_74, CodePack_password=var_68)


def test_39():
    var_0 = python_code_.StaffMember
    python_code_.CodePack_StaffGUI(CodePack_StaffGUI=var_0)
    python_code_.CodePack_IUserAccount()
    var_39 = python_code_.CodePack_CheckInMachine()
    python_code_.CodePack_IReceptionOperations_rename_required()
    python_code_.CodePack_IStaffAdmin()
    var_44 = python_code_.CodePack_IBookings()
    var_44.getAvailableRooms(CodePack_date_end=var_0, CodePack_date_start=var_39)


def test_40():
    var_0 = python_code_.CodePack_IBookings()
    python_code_.CodePack_ICheckIn()
    var_3 = -1593
    var_4 = -3061.48
    var_5 = python_code_.CodePack_DataModels_Bill(
        booking_id=var_3,
        total_price=1743.9,
        CodePack_DataModels_Bill={False},
        CodePack_DataModels_Bill31={var_4, var_4, var_0},
    )
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)
    var_57 = python_code_.CodePack_IManagement()
    var_57.updateRoom(CodePack_room=complex(-1141.1240862, 2522.6))


def test_41():
    python_code_.CodePack_ICheckIn()
    var_68 = "N"
    var_69 = 3744
    python_code_.CodePack_UserGUI()
    var_72 = python_code_.CodePack_IUserAccount()
    python_code_.CodePack_CheckInMachine()
    var_74 = python_code_.CodePack_Backend_CustomerHandler
    var_72.login(CodePack_e_mail=var_74, CodePack_password=var_68)
    var_77 = python_code_.CodePack_IBookings()
    var_77.getBookingForId(CodePack_booking_id=var_69)
    var_79 = python_code_.CodePack_IStaffAdmin()
    var_79.getStaffAccount(CodePack_pers_no=178.52)


def test_42():
    var_58 = python_code_.StaffMember()
    python_code_.CodePack_UserGUI(CodePack_UserGUI=var_58)


def test_43():
    python_code_.CodePack_IUserAccount()
    var_5 = python_code_.CodePack_IManagement()
    var_5.removeRoomType(CodePack_type_name=var_5)


def test_44():
    python_code_.CodePack_IUserAccount()
    python_code_.CodePack_CheckInMachine()
    var_8 = python_code_.CodePack_IBookings()
    var_8.updateServiceForBooking(
        CodePack_old_service_id=b"\x8f\x14\xb1",
        CodePack_new_service="Room_CodePack_StaffGUI__CodePack_StaffGUI2",
    )


def test_45():
    var_6 = python_code_.CodePack_IUserAccount()
    var_6.isEmailAvailable(CodePack_e_mail=False)
    var_10 = python_code_.CodePack_IBookings()
    var_10.cancelBooking(
        CodePack_booking_id="_CodePack_StaffGUI__CodePack_StaffGUI_CodePack_DataModels_Booking__CodePack_DataModels_Booking_CodePack_CheckInMachine__CodePack_CheckInMachine_CodePack_DataModels_Bill__CodePack_DataModels_Bill31"
    )


def test_46():
    var_5 = python_code_.CodePack_DataModels_Bill(booking_id=0, total_price=-438.15)
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)
    var_57 = python_code_.CodePack_CheckInMachine()
    var_58 = 0
    var_59 = "crQ^fvr0JY"
    var_60 = 1468
    var_61 = -2506
    var_62 = lambda *args, **kwargs: False
    python_code_.CodePack_DataModels_Customer(
        password=complex(-173.29822, 1604.79),
        date_of_birth=var_57,
        bonus_points=var_58,
        e_mail=var_59,
        first_name=var_59,
        phone_no=var_60,
        customer_id=var_61,
        payment_id=var_58,
        last_name=var_62,
    )
    python_code_.CodePack_IUserAccount()


def test_47():
    python_code_.CodePack_Shared_ContactData(
        full_name="_CodePack_StaffGUI__CodePack_StaffGUI2-_CodePack_StaffGUI__CodePack_StaffGUI-CheckInHandler",
        e_mail="rJ|5O?}Dv<6bNe\nh%",
        phone_no=0,
    )


def test_48():
    var_10 = python_code_.CodePack_IManagement()
    var_10.getRoomTypes()


def test_49():
    var_5 = python_code_.CodePack_DataModels_Bill(booking_id=0, total_price=-438.15)
    assert isinstance(var_5, python_code_.CodePack_DataModels_Bill)
    python_code_.CodePack_CheckInMachine()
    var_59 = lambda *args, **kwargs: "Room"
    var_60 = -1199
    var_61 = "1Gh`zh.'?c"
    python_code_.CodePack_DataModels_ExtraService(
        date_start=var_5,
        date_end=var_59,
        booking_id=var_60,
        total_price="5_ k",
        type=var_61,
    )


def test_50():
    var_6 = python_code_.CodePack_IUserAccount()
    var_9 = python_code_.CodePack_IManagement()
    var_10 = python_code_.RoomBooked
    var_9.addRoom(
        CodePack_number=var_9,
        CodePack_type=var_10,
        CodePack_description=True,
        CodePack_isAvailable=var_6,
    )


def test_51():
    python_code_.CodePack_UserGUI(CodePack_UserGUI=None)
    var_64 = python_code_.CodePack_IStaffAdmin()
    var_64.getStaffRoles()


def test_52():
    var_65 = -1634
    var_66 = python_code_.CodePack_DataModels_RoomBooked
    python_code_.CodePack_DataModels_RoomBooked(
        room_number=var_65, booking_id=25, date_start=var_66, date_end=var_65
    )


def test_53():
    var_58 = python_code_.StaffMember()
    var_59 = python_code_.CodePack_UserGUI(CodePack_UserGUI=var_58)
    var_64 = True
    python_code_.CodePack_DataModels_StaffRole(
        name=var_59,
        canManageBookings=var_64,
        canManageRooms=var_64,
        canManageServices={},
        canManageAccounts="Booking",
    )


def test_54():
    var_6 = python_code_.CodePack_IManagement()
    var_10 = python_code_.CodePack_IStaffAdmin()
    var_10.addStaffRole(
        CodePack_canManageAccounts=[True, 2],
        CodePack_canManageRooms=0,
        CodePack_canManageServices=0,
        CodePack_canManageBookings=var_6,
        CodePack_name=var_6,
    )


def test_55():
    var_63 = python_code_.CodePack_CheckInMachine(
        CodePack_CheckInMachine=b"d\xafO\xb1O\xfa[\xbdfx\xe8\xfb"
    )
    assert isinstance(var_63, python_code_.CodePack_CheckInMachine)


def test_56():
    var_58 = python_code_.StaffMember()
    var_59 = python_code_.CodePack_UserGUI(CodePack_UserGUI=var_58)
    var_64 = python_code_.CodePack_ICheckIn()
    var_64.validateBooking(CodePack_booking_id=var_59)


def test_57():
    var_58 = python_code_.StaffMember()
    python_code_.CodePack_StaffGUI(CodePack_StaffGUI=None, CodePack_StaffGUI2=var_58)


def test_58():
    python_code_.CodePack_UserGUI()
    var_65 = -871
    python_code_.CodePack_DataModels_RoomType(
        description=-2852,
        max_guests=var_65,
        rate={"s\rsh\tv5": 227.43},
        typename=b"a\x98",
    )


def test_59():
    var_65 = -1634
    var_66 = python_code_.CodePack_ICheckIn
    python_code_.CodePack_DataModels_RoomBooked(
        room_number=var_65,
        booking_id=var_65,
        date_start=None,
        date_end=var_66,
        CodePack_DataModels_RoomBooked=var_66,
    )


def test_60():
    var_49 = -1881
    python_code_.CodePack_DataModels_Booking(
        id=-2370,
        date_check_in=None,
        date_check_out=None,
        isCheckedIn=False,
        total_price=2300.18,
        contact_name=":+`Y",
        contact_phone=1463,
        contact_email="%Kyq",
        customer_id=var_49,
        payment_id=658,
        bonus_points_used=var_49,
    )


def test_61():
    var_49 = -1893
    var_51 = python_code_.CodePack_DataModels_Booking(
        id=-177,
        date_check_in=var_49,
        date_check_out=None,
        isCheckedIn=True,
        total_price=-2369.21,
        contact_name="JxG\n8Z9X>-3]\x0b<LE",
        contact_phone=var_49,
        contact_email="`\ndF,Lo%CKS9Rw",
        customer_id=var_49,
        payment_id=978,
        bonus_points_used=var_49,
        CodePack_DataModels_Booking=var_49,
    )
    assert isinstance(var_51, python_code_.CodePack_DataModels_Booking)
