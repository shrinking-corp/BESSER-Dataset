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
    Accounnt,
    Accounnt1,
    Account,
    Account1,
    Account_for_employee,
    Catering,
    Catering1,
    Chef,
    Component,
    Csutomer,
    Customer,
    Customer1,
    Customer_Balance,
    Customer_Balance1,
    Dish,
    Employee,
    Employee1,
    Employee_Actor,
    Enum,
    Enumeration,
    Enumeration1,
    Generate_payment_cheque_employes_UseCase,
    Kitchen_worker,
    Menu,
    Menu1,
    Order,
    Order1,
    Owner,
    Owner1,
    Owner2,
    Payment,
    Payment1,
    Plan,
    Plan1,
    PrintRecipts,
    PrintRecipts1,
    Shopping_cart,
    Shopping_cart1,
    Storage,
    Storage1,
    System,
    System1,
    UseCase_UseCase,
    Waiter,
    Web_master,
    abstractmethod,
    account_registration,
    account_type,
    add_and_get_from_storage_check_storage_UseCase,
    add_constraints_UseCase,
    annotations,
    bank_account,
    catering,
    check_bank_account_for_payments_UseCase,
    chef,
    chef1,
    chef2,
    chef_Actor,
    contact,
    create_invoice_UseCase,
    customer_Actor,
    customer_account,
    daily_weekly_monthly_plan_UseCase,
    date,
    date2,
    datetime,
    dayplan,
    drink,
    events,
    food_dish,
    help,
    kitchen_worker,
    liquid,
    list_of_outdated_components_UseCase,
    menu,
    order,
    order_catering_service_UseCase,
    order_missing_components_UseCase,
    owner_System_Actor,
    owner__system,
    payment,
    payorder_UseCase,
    prepration_plan_dishes_UseCase,
    select_from_menu_UseCase,
    shopping_cart,
    sign_up_login_logout_UseCase,
    solid,
    solid1,
    time,
    weekly_plan_dishes_UseCase,
    weekly_plan_of_each_cutomer_UseCase,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = "w1\x0cg.\\=_W"
    var_1 = 3
    var_2 = "weekly_planning_of_dishes__by_waiter145_menu__drink120"
    var_3 = 775
    var_4 = python_code_.chef1(
        Name=None,
        Employee_ID=var_1,
        Email=None,
        passowrd=var_2,
        Room_no=var_3,
        plan47=var_2,
    )
    var_5 = -1423
    var_6 = 150
    var_7 = python_code_.chef1(
        Name=var_0,
        Employee_ID=var_5,
        Email=b'r:\xcc\xf3"\xd4\xc5hp\xe3',
        passowrd=var_2,
        Room_no=var_6,
    )
    var_8 = {var_4, var_7, var_4}
    python_code_.Plan1(
        weekly_plan={}, Monthly_plan=var_0, day_plan={}, chef46=var_8, customer88=var_1
    )
    var_10 = python_code_.date2()
    python_code_.Customer_Balance(
        CustomerID=var_5,
        CustomerName=b"\x07\xc8\x9c\x92\xb4\x9a\xa1",
        Adress=var_0,
        Date=var_2,
        Account_balance=var_1,
    )
    var_14 = python_code_.Plan1(weekly_plan=var_8, Monthly_plan=var_2, day_plan=var_8)
    var_15 = "order127"
    var_16 = "TDSO.E8c`L#pvi^nI"
    python_code_.Customer_Balance1(
        Account_balance=var_2,
        CustomerID=var_7,
        CustomerName=var_15,
        Adress=var_1,
        Date=var_16,
    )
    var_18 = python_code_.Menu
    python_code_.System1(WebAdmin_or_owner=var_18, Email=var_2, Password=var_3)
    var_20 = "$2\x0cMe9g3 N'lI!^[(&"
    python_code_.owner__system(attribute=var_20)
    python_code_.owner__system(attribute=var_20, component149=var_10)
    var_24 = "&vHq$PvQ"
    var_25 = "Accounnt1,Component,_events__planning135"
    var_26 = -1033
    var_27 = "X|v)BbO{\rxz3+l{"
    python_code_.Customer1(
        Name=False,
        ID=set(),
        Address=var_14,
        Email=var_24,
        Password=var_25,
        Accontbalance=var_18,
        Phone=var_26,
        attribute=var_27,
        _attr=(819.36, 'QHxVh&\t"\\hZ^'),
        Adress=var_24,
        order53=var_8,
        plan89=var_14,
        accounnt99=var_18,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_0 = "`SC"
    python_code_.contact(
        Name={-491},
        Adress=complex(-684.44668, 1533.1),
        Email=[-685],
        Tel=False,
        attribute=var_0,
    )
    var_3 = "component179"
    var_4 = 'zb"RmX\t]'
    python_code_.Account1(
        Name=var_0,
        id=var_0,
        email=var_3,
        password=var_3,
        _attr=var_4,
        attribute=-1080.5,
    )
    var_6 = lambda *args, **kwargs: "_Component__component155"
    python_code_.Catering(Menu=False, attribute=var_6)
    var_8 = python_code_.shopping_cart()
    var_9 = python_code_.shopping_cart()
    var_10 = {var_8, var_9}
    var_11 = python_code_.payment(
        amount=b"(t\x01\x85NI\xbb\x16\xec\xd8\xcf\x16\x9e\xb4\xc4w9\xad",
        _attr=var_6,
        total_amount=var_6,
        shopping_cart133=var_10,
    )
    assert isinstance(var_11, python_code_.payment)
    var_12 = python_code_.kitchen_worker()
    var_14 = python_code_.catering()
    var_15 = "weekly_planning_of_dishes__by_waiter147Shopping_cart1_Accounnt1__customer103bank_account"
    python_code_.payment(amount=var_10, _attr=var_15, total_amount=var_3)
    var_18 = "_events__weekly_planning_of_dishes__for__waiter178-dish106"
    var_19 = ""
    var_20 = python_code_.events(
        get_employee_name=var_19,
        duration=b"\x99\x0ecQ\xa4\xa8\xb5\x8c\xbcHMVJ\xd3",
        attribute=var_0,
        catering_location=var_0,
        weekly_planning_of_dishes__for__waiter178=var_10,
    )
    assert isinstance(var_20, python_code_.events)
    python_code_.Component(
        ID=var_12,
        Name=var_15,
        Type=var_15,
        Storage_or_sehlf=var_18,
        Expiry_date=var_3,
        attribute=var_14,
        weekly_planning_of_dishes__by_waiter141=var_20,
    )


@pytest.mark.xfail(strict=True)
def test_2():
    var_2 = "_Customer1__customer_Balance42 _Menu1__catering48"
    var_3 = ":LT4>0.|2"
    var_4 = "\tP4+0>c1DJ"
    var_5 = python_code_.Plan
    python_code_.events(
        get_employee_name=var_2,
        duration=var_3,
        attribute=["owner__system"],
        catering_location=var_4,
        planning135=-109,
        food_dish164=var_5,
        order182=[1, 1964.67, "$od{qko?-$0t"],
    )


@pytest.mark.xfail(strict=True)
def test_3():
    var_0 = python_code_.food_dish
    var_1 = "_order__menu125"
    var_2 = ")ku&L"
    var_3 = -2121
    var_4 = python_code_.Web_master()
    var_5 = python_code_.contact(
        Name=var_0,
        Adress=var_1,
        Email=var_2,
        Tel=var_3,
        attribute=var_3,
        web_master63=var_4,
    )
    var_6 = -1
    var_7 = "_Component__owner__system162,_Csutomer__catering174,_food_dish__component112,_Menu1__dish106"
    var_8 = python_code_.Order(
        OrderID=complex(-3850.326, 3070.205159),
        Customerid=var_6,
        Dishname=complex(-2607.0, 572.5258),
        attribute=var_2,
        date=var_7,
    )
    var_10 = "P"
    var_11 = python_code_.contact(
        Name=var_2, Adress=var_7, Email=var_7, Tel=var_8, attribute=var_10
    )
    python_code_.solid(must_be_unit_in_kg=var_0)
    python_code_.Plan1(weekly_plan=var_1, Monthly_plan=None, day_plan=None)
    var_17 = python_code_.catering()
    python_code_.solid1(
        name=var_17,
        weight__kg_=var_7,
        pieces=b"\x98}BPj\xc1ux\xdf\xc0\xd4\xf9{\xfdWx",
        state=var_1,
    )
    var_20 = 'J\nu%"7\nyPaEjmh,s'
    var_21 = "events"
    var_22 = "payment56_Menu1__shopping_cart94"
    var_23 = python_code_.Storage1(Component_id=var_5, Component_Name=var_22)
    python_code_.System1(
        WebAdmin_or_owner=var_3,
        Email=var_20,
        Password=var_21,
        contact72=var_11,
        storage86=var_23,
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_1 = 1934
    var_2 = "ho@"
    var_3 = "Hl;}r0#Kjg(("
    var_4 = python_code_.Payment(
        PaymentID=var_1,
        Amount=var_2,
        OrderID=var_2,
        CustomerID=var_2,
        date=var_2,
        time=var_3,
    )
    var_6 = python_code_.menu
    python_code_.account_type(
        name=var_4,
        id=var_6,
        email=complex(3064.3, -1910.78341),
        password="`A;C_q'\"dmRQ;?E",
        _attr=var_4,
    )
    var_8 = python_code_.order_catering_service_UseCase()
    python_code_.Dish(_attr=var_8, menu107=complex(-5299.8488647, -778.479694))


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "d*Ql\x0cPI^Z\x0bIwC("
    var_1 = 2
    var_2 = "gyt%#V*m/\x0bOp"
    var_3 = python_code_.check_bank_account_for_payments_UseCase
    python_code_.Shopping_cart1(
        Dishname=var_0,
        price="_Csutomer__catering174",
        Quantity=var_1,
        time=var_2,
        attribute=var_3,
        menu54=var_3,
    )
    var_5 = -476
    var_6 = "NpV6A"
    python_code_.PrintRecipts1(
        PaymentID=var_2,
        CustomerID=var_0,
        Amount="_Plan1__customer88",
        Dishname=var_0,
        Quantity=var_5,
        time=var_6,
        date=var_1,
        payment59=var_5,
    )
    var_8 = python_code_.chef2()
    var_10 = 0
    var_11 = "nRJK1"
    python_code_.solid1(name=var_2, weight__kg_=var_1, pieces=var_10, state=var_11)
    python_code_.Catering(Menu=var_6, attribute=var_2)
    var_14 = "N"
    var_15 = python_code_.Dish(_attr=var_3, menu104=var_6)
    python_code_.Menu1(
        DishName=complex(3315.1, 2050.7038532),
        Price=var_8,
        Quantity=False,
        Components=var_14,
        dish105=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = "zV0Ma\x0b@h-;lP'1"
    var_1 = python_code_.Owner1
    var_2 = python_code_.Shopping_cart1(
        Dishname=None,
        price=-2132.54,
        Quantity=[False, False, False],
        time=var_0,
        attribute=var_1,
    )
    python_code_.Employee(
        Email=var_0,
        password=False,
        attribute=(-141, -977, 1727.35),
        ID=[],
        Name=var_2,
        storage0=True,
        plan2=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = 'x"ML@W{Em'
    var_1 = python_code_.date2
    python_code_.Account_for_employee(
        name=var_0,
        id=var_0,
        email=var_0,
        password=var_0,
        getaccount=var_0,
        attribute=var_1,
    )
    var_4 = -1133
    var_5 = python_code_.Storage1(Component_id=var_4, Component_Name=var_0, chef64=())
    python_code_.System1(
        WebAdmin_or_owner=var_0, Email=var_0, Password=var_0, storage86=var_5
    )


def test_8():
    var_0 = lambda *args, **kwargs: -1
    var_1 = "_Component__owner__system148:events:component139:food_dish181"
    var_2 = ".R@\n"
    python_code_.Customer_Balance(
        CustomerID=var_0,
        CustomerName=var_1,
        Adress=True,
        Date=None,
        Account_balance=var_2,
    )
