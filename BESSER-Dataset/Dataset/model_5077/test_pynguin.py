#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    CarRental2_Branch,
    CarRental2_Car,
    CarRental2_CarGroup,
    CarRental2_Check,
    CarRental2_Customer,
    CarRental2_Employee,
    CarRental2_Person,
    CarRental2_Rental,
    CarRental2_ServiceDepot,
    Person,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="c&.psY5iQc${|",
        Offers_CarGroup={False, False, "4O!\nQPlLA"},
        CarGroup=None,
        Classification_CarGroup={508, "o.%"},
        Reservation_CarGroup=set(),
        CarGroup26=None,
        CarGroup29=None,
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)


def test_1():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="^}G3|-", CarGroup15=None, CarGroup=None, Quality_CarGroup_role_higher=None
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)


@pytest.mark.xfail(strict=True)
def test_2():
    var_2 = "_CarRental2_BFranch__Branch!\r"
    var_36 = python_code_.CarRental2_CarGroup(
        kind=var_2, CarGroup15=var_2, Quality_CarGroup_role_higher=None
    )
    assert isinstance(var_36, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_CarGroup(
        kind=var_2,
        CarGroup15=var_2,
        Quality_CarGroup_role_higher=var_36,
        Quality_CarGroup_role_lower=var_36,
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_3 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    var_8 = "1WhCd"
    var_9 = lambda *args, **kwargs: 2
    var_10 = python_code_.CarRental2_Car(id=var_3, Car17=var_9, Car=(), Fleet_Car=var_9)
    var_11 = var_10.description()
    var_12 = python_code_.CarRental2_CarGroup(kind=var_8, Offers_CarGroup=var_11)
    assert isinstance(var_12, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_Rental(
        fromDate=var_8, untilDate=var_3, Reservation_Rental=var_12, Rental=var_3
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_2 = "_CarRental2_BFranch__Branch!9"
    var_36 = python_code_.CarRental2_CarGroup(
        kind=var_2, CarGroup15=var_2, Reservation_CarGroup=set(), CarGroup29=None
    )
    assert isinstance(var_36, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_CarGroup(
        kind="Fs Ey$9#$cXw",
        Reservation_CarGroup={3293.33, var_36, "\x0b\x0bU42>CHw:SW2d4(/"},
        Quality_CarGroup_role_higher=None,
        Quality_CarGroup_role_lower=var_36,
    )


def test_5():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="^}G3|-", CarGroup15=None, CarGroup=None, Quality_CarGroup_role_higher=None
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)
    var_42 = {var_28}
    var_43 = python_code_.CarRental2_Branch(
        location=0, Branch13=var_42, Offers_Branch=var_42, Provider_Branch=None
    )
    assert isinstance(var_43, python_code_.CarRental2_Branch)
    var_43.rentalsForDate()
    var_48 = python_code_.CarRental2_Car(id=None, Car=var_43)
    assert isinstance(var_48, python_code_.CarRental2_Car)
    var_51 = var_48.description()
    var_52 = python_code_.CarRental2_CarGroup(
        kind=(False, False, 'zh8#Jy"m>pGl2Z{]'),
        CarGroup=var_43,
        Classification_CarGroup=var_51,
        Reservation_CarGroup=var_42,
        CarGroup29={
            "IQ\x0b": "Quality_CarGroup_role_higher-_CarRental2_Branch__Branch13-Branch31-Car21",
            ".$`": -144,
        },
        Quality_CarGroup_role_lower=-1337,
        CarGroup33=set(),
    )
    assert isinstance(var_52, python_code_.CarRental2_CarGroup)


def test_6():
    python_code_.CarRental2_Car(id="", Car17=None, Assignment_Car=None)


def test_7():
    var_3 = "^\nEK@GL"
    python_code_.CarRental2_Car(
        id="6*N_/", Car21=None, Classification_Car=var_3, Assignment_Car=None
    )


@pytest.mark.xfail(strict=True)
def test_8():
    var_17 = python_code_.CarRental2_Check(
        description="_CarRental2_CarGroup__Reservation_CarGroup"
    )
    var_19 = "LJu)Y,_taj~"
    var_20 = set
    var_21 = python_code_.CarRental2_Car(id=var_19, Car17=var_17, Car21=var_20)
    var_22 = var_21.description()
    python_code_.CarRental2_Branch(
        location=var_19, Fleet_Branch=var_19, Offers_Branch=var_22, Branch31=var_21
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_3 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    var_7 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    var_8 = python_code_.CarRental2_Car(id=var_7, Car=[2])
    python_code_.CarRental2_Rental(
        fromDate=var_3,
        untilDate=var_3,
        Reservation_Rental=var_3,
        Assignment_Rental=var_8,
    )


def test_10():
    var_19 = ""
    python_code_.CarRental2_Car(id=var_19, Car17=var_19)
    var_25 = python_code_.CarRental2_Branch(location=var_19, Branch3=var_19)
    assert var_25.Branch3 == ""


def test_11():
    var_3 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Re>ntal__Rental"
    var_17 = 0
    var_18 = python_code_.CarRental2_Employee(
        salary=var_17, Management_Employee_role_manager=var_3
    )
    assert isinstance(var_18, python_code_.CarRental2_Employee)
    python_code_.CarRental2_Branch(
        location=var_3,
        Branch3=None,
        Management_Branch_role_managedBranch=var_18,
        Employment_Branch_role_employer={var_18},
        Provider_Branch=set(),
    )
    assert isinstance(var_18.Employee, python_code_.CarRental2_Branch)
    python_code_.CarRental2_Employee(salary=-1789)


def test_12():
    var_3 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    var_7 = python_code_.CarRental2_Branch(location=var_3, Branch3=var_3)
    assert (
        var_7.Branch3
        == "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    )


def test_13():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="CarRental2_Employee Booking_Customer",
        CarGroup15=None,
        Offers_CarGroup=set(),
        CarGroup=None,
        Reservation_CarGroup={False, "I"},
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)
    var_35 = python_code_.CarRental2_Branch(
        location=b"\x99\xb0p*:",
        Branch19=var_28,
        Fleet_Branch=["%{)S:3|D/1\tQ", 2522.53, "\\R&}z"],
    )
    assert isinstance(var_35, python_code_.CarRental2_Branch)


@pytest.mark.xfail(strict=True)
def test_14():
    var_1 = b"y\xdb\xc5^\x83"
    var_2 = "_CarRental2_Branch__Branch19"
    var_17 = python_code_.CarRental2_Branch(location=var_2, Provider_Branch=var_1)
    python_code_.CarRental2_Employee(
        salary="Management_Branch_role_managedBranch-Employment_Employee_role_employee-_CarRental2_Branch__Offers_Branch-_CarRental2_Branch__Provider_Branch",
        Management_Employee_role_manager=complex(-1073.8722598, 3631.3),
        Employment_Employee_role_employee=var_17,
        Employee6=var_17,
    )
    assert isinstance(var_17.Branch3, python_code_.CarRental2_Employee)


def test_15():
    var_2 = "_CarRental2_Branch__Branch19"
    var_3 = 0
    var_4 = python_code_.CarRental2_Employee(
        salary=var_3,
        Employment_Employee_role_employee={"Branch13": -2252.09},
        Employee6=complex(2984.3847019, -2005.2),
    )
    assert isinstance(var_4, python_code_.CarRental2_Employee)
    python_code_.CarRental2_Branch(
        location=var_2,
        Branch3=None,
        Management_Branch_role_managedBranch=var_4,
        Employment_Branch_role_employer={var_4},
        Provider_Branch=set(),
    )


def test_16():
    var_34 = python_code_.CarRental2_Rental(
        fromDate="x3C5k",
        untilDate=[],
        Reservation_Rental=[],
        Rental35=complex(1208.93, -389.5),
    )
    assert var_34.Reservation_Rental == []


def test_17():
    var_31 = 0
    var_32 = python_code_.CarRental2_Employee(salary=var_31)
    assert isinstance(var_32, python_code_.CarRental2_Employee)
    var_33 = var_32.raiseSalary()
    python_code_.CarRental2_Rental(fromDate=var_31, untilDate=var_33, Rental10=1487)


def test_18():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="^}G3|-", CarGroup15=None, CarGroup=None, Quality_CarGroup_role_higher=None
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)
    var_40 = python_code_.CarRental2_Rental(
        fromDate="_CarRental2_Branch__Branch Employment_Branch_role_employer Quality_CarGroup_role_higher",
        untilDate="1D4{3'kR,\\xg;g,v",
        Booking_Rental=var_28,
        Rental23=var_28,
        Rental35=var_28,
    )
    assert isinstance(var_40, python_code_.CarRental2_Rental)
    python_code_.CarRental2_Check(description="\x0cX")


@pytest.mark.xfail(strict=True)
def test_19():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="Booking_Rental", CarGroup15=None, Quality_CarGroup_role_lower=None
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)
    var_34 = python_code_.CarRental2_Employee
    var_45 = "Nz}2%|2"
    var_46 = python_code_.CarRental2_Customer(address=var_45)
    assert isinstance(var_46, python_code_.CarRental2_Customer)
    python_code_.CarRental2_Rental(
        fromDate=var_45,
        untilDate=var_45,
        Provider_Rental=var_34,
        Reservation_Rental=var_28,
        Rental23=var_28,
    )


def test_20():
    var_10 = object
    var_15 = "Nz}2%|2"
    var_16 = python_code_.CarRental2_Customer(address=var_15)
    assert isinstance(var_16, python_code_.CarRental2_Customer)
    python_code_.CarRental2_Rental(
        fromDate=var_10,
        untilDate=3,
        Reservation_Rental=var_10,
        Assignment_Rental=(2,),
        Rental=var_16,
    )


def test_21():
    var_0 = "Q\t-i%=c1/Ms"
    python_code_.CarRental2_Rental(fromDate=var_0, untilDate=var_0, Rental23=-700.81)
    var_2 = python_code_.CarRental2_Employee(salary=None)
    assert isinstance(var_2, python_code_.CarRental2_Employee)
    var_3 = "_CarRental2_Rental__Rental Customer"
    python_code_.CarRental2_Check(description=var_3)


def test_22():
    var_39 = python_code_.CarRental2_Employee(salary=-1789)
    assert isinstance(var_39, python_code_.CarRental2_Employee)


def test_23():
    var_0 = -792
    var_1 = python_code_.CarRental2_Employee(
        salary=var_0,
        Management_Employee_role_manager=var_0,
        Employee="N16",
        Employee6=var_0,
    )
    assert isinstance(var_1, python_code_.CarRental2_Employee)
    var_2 = "Q$x;7\x0bzF;x2I,BMi!"
    python_code_.CarRental2_Car(id=var_2, Car=[2])


def test_24():
    var_3 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Re>ntal__Rental"
    var_17 = -1
    var_18 = python_code_.CarRental2_Employee(
        salary=var_17,
        Employment_Employee_role_employee={"Branch13": -2252.09},
        Employee6=complex(2984.3847019, -2005.2),
    )
    assert isinstance(var_18, python_code_.CarRental2_Employee)
    python_code_.CarRental2_Branch(
        location=var_3,
        Branch3=None,
        Management_Branch_role_managedBranch=var_18,
        Employment_Branch_role_employer={var_18},
        Provider_Branch=set(),
    )
    python_code_.CarRental2_Employee(salary=-1789)


def test_25():
    var_0 = -2337
    var_1 = python_code_.CarRental2_Employee(salary=var_0)
    assert isinstance(var_1, python_code_.CarRental2_Employee)


def test_26():
    var_3 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    var_7 = python_code_.CarRental2_Customer(address=var_3)
    assert isinstance(var_7, python_code_.CarRental2_Customer)


def test_27():
    python_code_.CarRental2_Check(
        description="_CarRental2_CarGroup__Reservation_CarGroup"
    )


def test_28():
    python_code_.CarRental2_ServiceDepot(location=-1427.98)


def test_29():
    var_19 = ""
    var_20 = python_code_.CarRental2_Car(id=var_19, Car17=var_19)
    var_21 = var_20.description()
    var_22 = python_code_.CarRental2_Branch(
        location="Booking_Customer",
        Branch13=complex(-921.01, -2319.334),
        Offers_Branch=var_21,
        Branch31=None,
    )
    var_22.rentalsForDate()


def test_30():
    var_0 = -2337
    var_1 = python_code_.CarRental2_Employee(salary=var_0)
    assert isinstance(var_1, python_code_.CarRental2_Employee)
    var_1.raiseSalary()


def test_31():
    var_2 = "_CarRental2_Branch__Branch19"
    var_14 = object
    python_code_.CarRental2_Car(
        id=var_2, Car17=var_14, Assignment_Car={"-": 2604.72, "!BT\rm": -1213.84}
    )
    var_16 = python_code_.CarRental2_Person(
        firstname=False, lastname=b"]\xfe(\xe8@\x02\x89", age=var_14, isMarried=var_14
    )
    assert isinstance(var_16, python_code_.CarRental2_Person)


def test_32():
    python_code_.CarRental2_Check(description=2577)
    var_75 = lambda *args, **kwargs: "Lf`"
    var_77 = "H2Vo[6>H|(/v"
    var_87 = "_CarRental2_Employee__Employment_Employee_role_employee_CarRental2_CarGroup__CarGroup_CarRental2_Car__CarCustomer"
    var_88 = python_code_.CarRental2_Person(
        firstname=var_87, lastname=var_77, age=788, isMarried=True
    )
    assert isinstance(var_88, python_code_.CarRental2_Person)
    var_89 = var_88.fullname()
    var_90 = python_code_.CarRental2_CarGroup(
        kind=True, Offers_CarGroup=var_89, Quality_CarGroup_role_lower=var_75
    )
    assert isinstance(var_90, python_code_.CarRental2_CarGroup)


@pytest.mark.xfail(strict=True)
def test_33():
    var_11 = "Er0* \n?"
    var_12 = python_code_.CarRental2_CarGroup(kind=var_11, CarGroup26=False)
    assert isinstance(var_12, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_Rental(
        fromDate=var_11,
        untilDate=(2452, 2949.34),
        Provider_Rental=b"R\xdc\x94\x82vd\xc0\xde-\x01\x9b\xe3|\xd8b",
        Reservation_Rental=var_12,
        Rental35=var_12,
    )


@pytest.mark.xfail(strict=True)
def test_34():
    var_2 = "_CarRental2_BFranch__Branch!9"
    var_36 = python_code_.CarRental2_CarGroup(
        kind=var_2,
        Offers_CarGroup=set(),
        CarGroup=var_2,
        Classification_CarGroup=set(),
        Reservation_CarGroup=set(),
        Quality_CarGroup_role_higher=None,
        CarGroup29=var_2,
        Quality_CarGroup_role_lower=var_2,
    )
    assert isinstance(var_36, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_CarGroup(
        kind="Fs Ey$9#$cXw",
        Reservation_CarGroup={3293.33, var_36, "\x0b\x0bU42>CHw:SW2d4(/"},
        Quality_CarGroup_role_higher=None,
        Quality_CarGroup_role_lower=var_36,
    )


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = "_CarRental2_Car__Car21-_CarRental2_Car__Car"
    var_1 = python_code_.CarRental2_Car(id=var_0)
    python_code_.CarRental2_ServiceDepot(location=var_0)
    var_3 = python_code_.CarRental2_CarGroup
    var_4 = python_code_.CarRental2_Customer(address=var_3)
    assert isinstance(var_4, python_code_.CarRental2_Customer)
    python_code_.CarRental2_Check(description=var_0)
    var_6 = '&\t"'
    var_7 = True
    var_8 = python_code_.CarRental2_Person(
        firstname=var_1, lastname=var_6, age=False, isMarried=var_7
    )
    assert isinstance(var_8, python_code_.CarRental2_Person)
    var_8.fullname()
    python_code_.CarRental2_Branch(
        location=var_6,
        Management_Branch_role_managedBranch="",
        Employment_Branch_role_employer=var_3,
        Offers_Branch=var_8,
    )


@pytest.mark.xfail(strict=True)
def test_36():
    var_1 = 2
    var_2 = "_CarRental2_Branch__Branch19"
    var_3 = 0
    var_4 = python_code_.CarRental2_Employee(
        salary=var_3,
        Employment_Employee_role_employee={"Branch13": -2252.09},
        Employee6=complex(2984.3847019, -2005.2),
    )
    assert isinstance(var_4, python_code_.CarRental2_Employee)
    var_5 = var_4.raiseSalary()
    python_code_.CarRental2_Branch(
        location=var_2,
        Branch3=var_4,
        Employment_Branch_role_employer=var_5,
        Fleet_Branch=complex(1325.89, 789.9),
        Provider_Branch=var_1,
    )


def test_37():
    var_30 = 0
    var_31 = python_code_.CarRental2_Employee(
        salary=var_30,
        Employment_Employee_role_employee={"Branch13": -2252.09},
        Employee6=complex(2984.3847019, -2005.2),
    )
    assert isinstance(var_31, python_code_.CarRental2_Employee)
    var_31.raiseSalary()


def test_38():
    var_0 = "Rental23._CarRental2_Customer__Booking_Customer._CarRental2_CarGroup__Classification_CarGroup"
    python_code_.CarRental2_ServiceDepot(location=var_0)
    var_2 = lambda *args, **kwargs: "Lf`"
    var_3 = python_code_.CarRental2_Employee(
        salary=var_2, Management_Employee_role_manager=None, Employee=var_2
    )
    assert isinstance(
        python_code_.CarRental2_Employee.Employee, python_code_.CarRental2_Branch
    )
    var_4 = "H2Vo[6>H|(/v"
    var_5 = var_3.raiseSalary()
    python_code_.CarRental2_Branch(
        location=var_4,
        Management_Branch_role_managedBranch=var_3,
        Employment_Branch_role_employer={"#CIrzP!E/kZ`h=C6"},
        Fleet_Branch=var_5,
        Branch31=var_2,
    )


def test_39():
    var_34 = lambda *args, **kwargs: [True, True, True]
    python_code_.CarRental2_Car(id="Booking_Rental", Car=var_34, Assignment_Car=var_34)


def test_40():
    var_3 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    python_code_.CarRental2_Car(id=var_3, Car=[2])


@pytest.mark.xfail(strict=True)
def test_41():
    var_3 = 0
    var_4 = python_code_.CarRental2_Employee(
        salary=var_3,
        Employment_Employee_role_employee={"Branch13": -2252.09},
        Employee6=complex(2984.3847019, -2005.2),
    )
    assert isinstance(var_4, python_code_.CarRental2_Employee)
    python_code_.CarRental2_Branch(
        location=(),
        Branch=var_4,
        Offers_Branch=3061.19,
        Provider_Branch=b"\x1a\xe9\r\x98AyL\xf584@\xac \xdf\xbaF\x19c\xa9",
    )


def test_42():
    var_0 = "_CarRental2_Car_CCar21-_CarRental2_Car__Car"
    var_1 = python_code_.CarRental2_Car(id=var_0)
    var_44 = python_code_.CarRental2_Employee
    var_48 = python_code_.CarRental2_CarGroup(kind=var_1)
    assert isinstance(var_48, python_code_.CarRental2_CarGroup)
    var_50 = var_1.description()
    var_51 = python_code_.CarRental2_Branch(
        location=var_0,
        Branch19=var_48,
        Branch={"92w%": "~HmziG0aM;9} "},
        Management_Branch_role_managedBranch=var_44,
        Employment_Branch_role_employer=var_50,
    )
    assert isinstance(var_51, python_code_.CarRental2_Branch)


@pytest.mark.xfail(strict=True)
def test_43():
    var_2 = "_CarRental2_BFranch__Branch!9"
    var_35 = "_CarRental2_EmpQoyee__Management_Employee_role_manager-Rental10-_CarRental2_Branch__Branch13-Management_Branch_role_managedBranch"
    var_36 = python_code_.CarRental2_CarGroup(
        kind=var_35, Reservation_CarGroup=var_2, Quality_CarGroup_role_higher=set()
    )
    assert isinstance(var_36, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_CarGroup(
        kind=var_35,
        CarGroup=var_2,
        Reservation_CarGroup={
            3665.1,
            "Management_Employee_role_manager _CarRental2_CarGroup__Quality_CarGroup_role_higher",
        },
        CarGroup29=var_36,
        Quality_CarGroup_role_lower=None,
    )


@pytest.mark.xfail(strict=True)
def test_44():
    var_8 = python_code_.Person()
    var_12 = "tU`^T7%#=="
    var_13 = python_code_.CarRental2_Rental(
        fromDate=var_12,
        untilDate=var_12,
        Assignment_Rental=-2887.64,
        Rental10=var_8,
        Rental35=var_8,
    )
    var_14 = "\n[\x0bH8Vpw~*Ff\n0"
    var_15 = python_code_.CarRental2_Customer(address=var_13)
    assert isinstance(var_15, python_code_.CarRental2_Customer)
    python_code_.CarRental2_Rental(
        fromDate=var_12,
        untilDate=var_14,
        Booking_Rental=var_15,
        Assignment_Rental=(True, 624.84, 320.54),
        Rental35=None,
    )


@pytest.mark.xfail(strict=True)
def test_45():
    python_code_.CarRental2_Check(description=complex(330.509, 1380.72555))
    var_2 = python_code_.CarRental2_Customer(address={391, -267, True})
    assert isinstance(var_2, python_code_.CarRental2_Customer)
    var_35 = python_code_.Person()
    python_code_.CarRental2_ServiceDepot(
        location=[
            1729,
            "%G90]bkv#d%pU;",
            "CarRental2_Customer-_CarRental2_Car__Car21-_CarRental2_CarGroup__CarGroup33-_CarRental2_CarGroup__CarGroup26",
        ]
    )
    var_58 = "_CarRental2_Rental__Assignment_Rental"
    var_59 = python_code_.CarRental2_Rental(
        fromDate=var_35, untilDate=var_58, Booking_Rental=var_35, Rental35=var_58
    )
    python_code_.CarRental2_Customer(address=var_58, Customer=var_59)


def test_46():
    var_28 = python_code_.CarRental2_CarGroup(kind=None, CarGroup33={-890, 159})
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)


def test_47():
    var_0 = abs
    python_code_.CarRental2_ServiceDepot(location=var_0)
    var_2 = "Er0* \n?T"
    var_5 = 2
    var_25 = python_code_.CarRental2_Customer(
        address="56", Booking_Customer={"P=usYT5!2V~Yu:nIqO,", var_5}
    )
    assert isinstance(var_25, python_code_.CarRental2_Customer)
    var_35 = dict
    var_36 = python_code_.CarRental2_Person(
        firstname=var_2, lastname=var_35, age=set(), isMarried=var_35
    )
    assert isinstance(var_36, python_code_.CarRental2_Person)


def test_48():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="?ijdg$",
        CarGroup15=None,
        Quality_CarGroup_role_higher=None,
        Quality_CarGroup_role_lower=None,
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)
    var_29 = {var_28}
    var_31 = python_code_.CarRental2_Branch(
        location=0, Branch13=var_29, Offers_Branch=var_29, Provider_Branch=None
    )
    assert isinstance(var_31, python_code_.CarRental2_Branch)
    var_31.rentalsForDate()


@pytest.mark.xfail(strict=True)
def test_49():
    var_2 = "_CarRental2_Branch__Branch19"
    var_3 = 0
    var_4 = python_code_.CarRental2_Employee(
        salary=var_3,
        Employment_Employee_role_employee={"Branch13": -2252.09},
        Employee6=complex(2984.3847019, -2005.2),
    )
    assert isinstance(var_4, python_code_.CarRental2_Employee)
    python_code_.CarRental2_Branch(
        location=var_2,
        Branch19=var_3,
        Branch=var_4,
        Branch3=var_4,
        Employment_Branch_role_employer={False, False},
        Branch31=None,
    )


@pytest.mark.xfail(strict=True)
def test_50():
    var_2 = "_CarRental2_BFranc_h__Branch!9"
    var_38 = lambda *args, **kwargs: False
    var_39 = python_code_.CarRental2_Customer(address=var_38, Customer=var_38)
    assert isinstance(var_39, python_code_.CarRental2_Customer)
    python_code_.CarRental2_Rental(
        fromDate=var_38,
        untilDate=var_38,
        Booking_Rental=complex(-158.13433, -1353.782),
        Rental=var_39,
        Rental10=var_2,
    )
    var_41 = python_code_.CarRental2_Employee(
        salary=complex(78.0, 45.5),
        Management_Employee_role_manager={
            "_CarRental2_Car__Car21Branch_CarRental2_Rental__Provider_RentalCarRental2_Employee"
        },
    )
    assert isinstance(var_41, python_code_.CarRental2_Employee)
    var_42 = python_code_.CarRental2_CarGroup(kind=var_2, CarGroup=())
    assert isinstance(var_42, python_code_.CarRental2_CarGroup)
    var_43 = python_code_.CarRental2_Car(id=var_2, Car17=None, Car21=var_42)
    assert isinstance(var_43, python_code_.CarRental2_Car)
    python_code_.CarRental2_Branch(
        location=var_2,
        Branch=var_41,
        Branch3=var_2,
        Employment_Branch_role_employer=var_38,
        Branch31=var_43,
    )


def test_51():
    var_3 = "_*^+dK_*"
    python_code_.CarRental2_Car(id="\r8", Car21=var_3, Assignment_Car=None)


@pytest.mark.xfail(strict=True)
def test_52():
    var_1 = b"y\xdb\xc5^\x83"
    var_2 = "_CarRental2_Branch__Branch19"
    var_20 = "+N1&nJ>=VY+e"
    var_21 = hash
    var_22 = python_code_.CarRental2_Car(
        id=True,
        Car21=var_21,
        Fleet_Car=complex(1693.379607, -2281.388764),
        Classification_Car=var_21,
        Assignment_Car=False,
    )
    python_code_.CarRental2_Rental(
        fromDate=var_1,
        untilDate=var_20,
        Provider_Rental=1040,
        Rental=var_2,
        Rental35=var_22,
    )


@pytest.mark.xfail(strict=True)
def test_53():
    var_0 = abs
    var_1 = python_code_.CarRental2_ServiceDepot(location=var_0)
    var_28 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    var_29 = python_code_.CarRental2_Car(
        id=var_28, Fleet_Car=var_0, Classification_Car=None
    )
    python_code_.CarRental2_Rental(
        fromDate="Classification_Car", untilDate=var_28, Booking_Rental=None
    )
    var_42 = "-.5e"
    var_43 = python_code_.CarRental2_Person(
        firstname=var_42,
        lastname={1174.58, -94.59},
        age=var_1,
        isMarried=complex(-358.0349, -1451.83334),
    )
    assert isinstance(var_43, python_code_.CarRental2_Person)
    var_29.description()
    var_32 = "K?^11\n32_7xlf(1^"
    python_code_.CarRental2_Branch(location=var_32, Branch31=var_29)


@pytest.mark.xfail(strict=True)
def test_54():
    var_34 = lambda *args, **kwargs: [True, True, True]
    var_48 = python_code_.CarRental2_Customer(address="9")
    assert isinstance(var_48, python_code_.CarRental2_Customer)
    var_49 = set()
    var_50 = "Branch13"
    var_51 = python_code_.CarRental2_Car(id=var_34, Car=-2179.83, Assignment_Car=var_34)
    python_code_.CarRental2_Rental(
        fromDate=var_50, untilDate=[], Reservation_Rental=var_49, Rental35=var_51
    )


@pytest.mark.xfail(strict=True)
def test_55():
    var_3 = bool
    var_17 = ":Wte;F_h{' _agr"
    var_18 = python_code_.CarRental2_Employee(salary=1840)
    assert isinstance(var_18, python_code_.CarRental2_Employee)
    assert isinstance(
        python_code_.CarRental2_Employee.Employee, python_code_.CarRental2_Branch
    )
    var_19 = var_18.raiseSalary()
    var_20 = python_code_.CarRental2_CarGroup(
        kind=var_17, CarGroup15=var_3, CarGroup=[-2248.57], CarGroup26=var_19
    )
    assert isinstance(var_20, python_code_.CarRental2_CarGroup)
    var_32 = "Branch13"
    var_33 = python_code_.CarRental2_Customer(address=var_32)
    assert isinstance(var_33, python_code_.CarRental2_Customer)
    python_code_.CarRental2_Rental(
        fromDate=var_32, untilDate=-1266.52, Reservation_Rental=var_20, Rental=var_33
    )


@pytest.mark.xfail(strict=True)
def test_56():
    var_12 = bool
    var_13 = "_CarRental2_Rental__Reservation_Rental"
    var_14 = python_code_.CarRental2_Car(
        id=var_13, Car17=var_12, Assignment_Car={"-": 2604.72, "!BT\rm": -1213.84}
    )
    var_16 = python_code_.CarRental2_Employee(salary=1840)
    assert isinstance(var_16, python_code_.CarRental2_Employee)
    var_16.raiseSalary()
    var_25 = "{Rc]"
    python_code_.CarRental2_Rental(
        fromDate=var_25,
        untilDate=var_25,
        Reservation_Rental=var_25,
        Assignment_Rental=var_14,
    )


@pytest.mark.xfail(strict=True)
def test_57():
    var_33 = "cKj>u"
    var_34 = python_code_.CarRental2_Branch(
        location=var_33,
        Branch13=None,
        Employment_Branch_role_employer=(-870.43,),
        Branch31={'zN"([K&*': 730},
    )
    var_34.rentalsForDate()
    python_code_.CarRental2_Car(id=var_33, Fleet_Car=var_34, Classification_Car=var_34)


@pytest.mark.xfail(strict=True)
def test_58():
    var_2 = "_CarRental2_BFranc_h__Branch!9"
    var_38 = lambda *args, **kwargs: False
    var_39 = python_code_.CarRental2_Customer(address=var_38, Customer=var_38)
    assert isinstance(var_39, python_code_.CarRental2_Customer)
    python_code_.CarRental2_Rental(
        fromDate=var_38,
        untilDate=var_38,
        Booking_Rental=complex(-158.13433, -1353.782),
        Rental=var_39,
        Rental10=var_2,
    )
    var_41 = python_code_.CarRental2_Employee(
        salary=complex(78.0, 45.5),
        Management_Employee_role_manager={
            "_CarRental2_Car__Car21Branch_CarRental2_Rental__Provider_RentalCarRental2_Employee"
        },
    )
    assert isinstance(var_41, python_code_.CarRental2_Employee)
    var_42 = python_code_.CarRental2_CarGroup(kind=var_2, CarGroup=())
    assert isinstance(var_42, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_Car(id=var_2, Classification_Car=var_42)


@pytest.mark.xfail(strict=True)
def test_59():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="^}G3|-", CarGroup15=None, CarGroup=None, Quality_CarGroup_role_higher=None
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)
    var_33 = False
    var_35 = python_code_.CarRental2_Branch(
        location=b"\x99\xb0p*:",
        Branch19=var_28,
        Fleet_Branch=["%{)S:3|D/1\tQ", 2522.53, "\\R&}z"],
    )
    assert isinstance(var_35, python_code_.CarRental2_Branch)
    var_35.rentalsForDate()
    python_code_.CarRental2_Rental(
        fromDate=var_33,
        untilDate=var_33,
        Provider_Rental=var_35,
        Rental=b"\x04\x1f\x13\xef\xde\x9bh[C\xdf",
        Rental23=var_28,
    )


def test_60():
    var_2 = "_CarRental2_Branch__Branch19"
    var_3 = 1
    var_4 = python_code_.CarRental2_Employee(
        salary=var_3,
        Employment_Employee_role_employee={"Branch13": -2252.09},
        Employee6=complex(2984.3847019, -2005.2),
    )
    assert isinstance(var_4, python_code_.CarRental2_Employee)
    var_8 = python_code_.CarRental2_Branch(
        location=var_2,
        Branch3=None,
        Management_Branch_role_managedBranch=var_4,
        Employment_Branch_role_employer={var_4},
        Provider_Branch=set(),
    )
    python_code_.CarRental2_Employee(salary=False, Employee=var_8)


@pytest.mark.xfail(strict=True)
def test_61():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="CarRental2_Employee Booking_Customer",
        CarGroup15=None,
        Offers_CarGroup=set(),
        CarGroup=None,
        Reservation_CarGroup={False, "I"},
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)
    var_35 = python_code_.CarRental2_Branch(
        location=b"\x99\xb0p*:",
        Branch19=var_28,
        Fleet_Branch=["%{)S:3|D/1\tQ", 2522.53, "\\R&}z"],
    )
    assert isinstance(var_35, python_code_.CarRental2_Branch)
    var_42 = python_code_.CarRental2_Employee(salary=-1789)
    assert isinstance(var_42, python_code_.CarRental2_Employee)
    var_43 = "_CarRental2_Rental__Provider_Rental,_CarRental2_Rental__Rental23"
    python_code_.CarRental2_Car(id=var_43, Classification_Car=var_28)


def test_62():
    var_17 = python_code_.CarRental2_Check(
        description="_CarRental2_CarGroup__Reservation_CarGroup"
    )
    var_19 = "LJu)Y,_taj~"
    var_24 = python_code_.CarRental2_Branch(location=var_19, Branch3=var_19)
    assert var_24.Branch3 == "LJu)Y,_taj~"
    var_25 = "Eh]e_#Z"
    var_26 = python_code_.CarRental2_Rental(
        fromDate=var_17,
        untilDate=var_25,
        Provider_Rental=[False, "7bW2r2h\x0bg~Zmi)+:", 190.7],
        Reservation_Rental={2237, "+'BMvI", 3853.98},
        Rental=None,
        Rental10=var_24,
    )
    assert var_26.Reservation_Rental == {"+'BMvI", 3853.98, 2237}


@pytest.mark.xfail(strict=True)
def test_63():
    var_28 = python_code_.CarRental2_CarGroup(
        kind="CarRental2_Employee Booking_Customer",
        CarGroup15=None,
        Offers_CarGroup=set(),
        CarGroup=None,
        Reservation_CarGroup={False, "I"},
    )
    assert isinstance(var_28, python_code_.CarRental2_CarGroup)
    var_35 = python_code_.CarRental2_Branch(
        location=b"\x99\xb0p*:",
        Branch19=var_28,
        Fleet_Branch=["%{)S:3|D/1\tQ", 2522.53, "\\R&}z"],
    )
    assert isinstance(var_35, python_code_.CarRental2_Branch)
    var_42 = python_code_.CarRental2_Employee(salary=-1789)
    assert isinstance(var_42, python_code_.CarRental2_Employee)
    var_43 = "N"
    var_44 = bool
    python_code_.CarRental2_Car(
        id=var_43,
        Car17=var_44,
        Car=var_35,
        Car21=var_28,
        Fleet_Car=var_35,
        Classification_Car=var_28,
    )


@pytest.mark.xfail(strict=True)
def test_64():
    var_11 = "UIP5q7.QQA7,"
    var_12 = len
    var_13 = "P8P'VM"
    var_14 = python_code_.CarRental2_Rental(
        fromDate=var_12, untilDate=var_13, Reservation_Rental=var_11, Rental=var_13
    )
    assert var_14.Reservation_Rental == "UIP5q7.QQA7,"
    var_15 = 2854
    var_17 = python_code_.CarRental2_Branch(
        location=var_13,
        Management_Branch_role_managedBranch=var_13,
        Offers_Branch=var_13,
    )
    var_18 = python_code_.CarRental2_CarGroup(
        kind=2715,
        CarGroup15=var_15,
        CarGroup=var_17,
        Quality_CarGroup_role_higher=var_12,
    )
    assert isinstance(var_18, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_CarGroup(
        kind=var_12, Reservation_CarGroup=[], CarGroup26=var_18, CarGroup33=var_11
    )


@pytest.mark.xfail(strict=True)
def test_65():
    var_0 = python_code_.CarRental2_Check
    var_1 = 'XxzH.d"0</uk?\x0c]6Vq'
    var_2 = python_code_.CarRental2_Employee(
        salary=var_1, Employee=var_1, Employee6=None
    )
    assert isinstance(var_2, python_code_.CarRental2_Employee)
    var_2.raiseSalary()
    var_4 = "0jiQmp_xs!>"
    var_5 = "K68d"
    var_6 = python_code_.CarRental2_Customer(address=var_5)
    assert isinstance(var_6, python_code_.CarRental2_Customer)
    var_7 = python_code_.CarRental2_Rental(
        fromDate=var_1,
        untilDate=var_4,
        Booking_Rental=var_0,
        Provider_Rental=complex(-976.3473374, 3725.65094),
        Rental=var_6,
    )
    var_8 = python_code_.CarRental2_CarGroup(
        kind=var_4, CarGroup=complex(2501.13018, -1415.0)
    )
    assert isinstance(var_8, python_code_.CarRental2_CarGroup)
    var_9 = python_code_.CarRental2_Car(
        id={}, Car17=None, Car21=var_8, Assignment_Car=var_0
    )
    assert isinstance(var_9, python_code_.CarRental2_Car)
    var_10 = var_9.description()
    python_code_.CarRental2_Branch(
        location=var_0,
        Branch13=var_7,
        Branch3=var_2,
        Fleet_Branch=var_10,
        Offers_Branch=complex(-2833.7956, -1328.35543),
        Branch31=var_9,
    )


def test_66():
    var_14 = "Fp}tt,hR\x0bY(}\\G"
    var_18 = "\x0cgUeK?L"
    var_19 = "_CarRental2_Branch__Branch3"
    var_20 = python_code_.CarRental2_CarGroup(kind=var_19, Offers_CarGroup=var_18)
    assert isinstance(var_20, python_code_.CarRental2_CarGroup)
    var_23 = python_code_.CarRental2_Branch(
        location=var_14, Branch19=var_20, Offers_Branch=(1948.46, "4\x0b40E")
    )
    assert isinstance(var_23, python_code_.CarRental2_Branch)


@pytest.mark.xfail(strict=True)
def test_67():
    var_3 = "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    var_7 = python_code_.CarRental2_Branch(location=var_3, Branch3=var_3)
    assert (
        var_7.Branch3
        == "_CarRental2_Rental__Assignment_Rental-_CarRental2_Rental__Rental"
    )
    var_8 = float
    var_9 = lambda *args, **kwargs: True
    var_10 = " ?a^"
    var_11 = var_7.rentalsForDate()
    var_12 = python_code_.CarRental2_CarGroup(
        kind=var_10,
        CarGroup15=var_8,
        CarGroup=None,
        Reservation_CarGroup=var_11,
        Quality_CarGroup_role_higher=-427.16,
        Quality_CarGroup_role_lower=var_9,
        CarGroup33=var_8,
    )
    assert isinstance(var_12, python_code_.CarRental2_CarGroup)
    python_code_.CarRental2_Car(id=var_10, Car21=var_8, Classification_Car=var_12)
