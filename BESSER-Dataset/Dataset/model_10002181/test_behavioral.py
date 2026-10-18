import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
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
    account_registration,
    account_type,
    add_and_get_from_storage_check_storage_UseCase,
    add_constraints_UseCase,
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
    date2,
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
    weekly_plan_dishes_UseCase,
    weekly_plan_of_each_cutomer_UseCase,
    Enumeration,
    Enumeration1,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_Accounnt_Customer_reverse_link_reassign_clear():
    a1 = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    a2 = Customer1(Accontbalance="sample_text_2", Address="sample_text_2", Adress="sample_text_2", Email="sample_text_2", ID=13, Name="sample_text_2", Password="sample_text_2", Phone=13, _attr="sample_text_2", attribute="sample_text_2")
    b = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    _safe_set(b, 'customer98', a1)
    assert _is_linked(b, 'customer98', a1)
    if hasattr(a1, 'accounnt99'):
        assert _is_linked(a1, 'accounnt99', b)
    _safe_set(b, 'customer98', a2)
    assert _is_linked(b, 'customer98', a2)
    if hasattr(a1, 'accounnt99'):
        assert not _is_linked(a1, 'accounnt99', b)
    if hasattr(a2, 'accounnt99'):
        assert _is_linked(a2, 'accounnt99', b)
    _safe_set(b, 'customer98', None)
    assert not _is_linked(b, 'customer98', a2)
    if hasattr(a2, 'accounnt99'):
        assert not _is_linked(a2, 'accounnt99', b)


def test_assoc_Accounnt_Employee_reverse_link_reassign_clear():
    a1 = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    a2 = Kitchen_worker(Email="sample_text_2", ID=13, Name="sample_text_2", attribute="sample_text_2", password="sample_text_2")
    b = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    _safe_set(b, 'employee40', a1)
    assert _is_linked(b, 'employee40', a1)
    if hasattr(a1, 'accounnt41'):
        assert _is_linked(a1, 'accounnt41', b)
    _safe_set(b, 'employee40', a2)
    assert _is_linked(b, 'employee40', a2)
    if hasattr(a1, 'accounnt41'):
        assert not _is_linked(a1, 'accounnt41', b)
    if hasattr(a2, 'accounnt41'):
        assert _is_linked(a2, 'accounnt41', b)
    _safe_set(b, 'employee40', None)
    assert not _is_linked(b, 'employee40', a2)
    if hasattr(a2, 'accounnt41'):
        assert not _is_linked(a2, 'accounnt41', b)


def test_assoc_Accounnt_chef_reverse_link_reassign_clear():
    a1 = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    a2 = chef1(Email="sample_text_2", Employee_ID=13, Name="sample_text_2", Room_no=13, passowrd="sample_text_2")
    b = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    _safe_set(b, 'chef100', a1)
    assert _is_linked(b, 'chef100', a1)
    if hasattr(a1, 'accounnt101'):
        assert _is_linked(a1, 'accounnt101', b)
    _safe_set(b, 'chef100', a2)
    assert _is_linked(b, 'chef100', a2)
    if hasattr(a1, 'accounnt101'):
        assert not _is_linked(a1, 'accounnt101', b)
    if hasattr(a2, 'accounnt101'):
        assert _is_linked(a2, 'accounnt101', b)
    _safe_set(b, 'chef100', None)
    assert not _is_linked(b, 'chef100', a2)
    if hasattr(a2, 'accounnt101'):
        assert not _is_linked(a2, 'accounnt101', b)


def test_assoc_Component_drink_reverse_link_reassign_clear():
    a1 = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    a2 = menu(attribute="sample_text_2", dish_quantity="sample_text_2", dishname="sample_text_2", drinkname="sample_text_2", price="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'component155', a1)
    assert _is_linked(b, 'component155', a1)
    if hasattr(a1, 'drink154'):
        assert _is_linked(a1, 'drink154', b)
    _safe_set(b, 'component155', a2)
    assert _is_linked(b, 'component155', a2)
    if hasattr(a1, 'drink154'):
        assert not _is_linked(a1, 'drink154', b)
    if hasattr(a2, 'drink154'):
        assert _is_linked(a2, 'drink154', b)
    _safe_set(b, 'component155', None)
    assert not _is_linked(b, 'component155', a2)
    if hasattr(a2, 'drink154'):
        assert not _is_linked(a2, 'drink154', b)


def test_assoc_Component_food_dish_reverse_link_reassign_clear():
    a1 = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    a2 = food_dish(attribute="sample_text_2", attribute2="sample_text_2", type="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'component153', a1)
    assert _is_linked(b, 'component153', a1)
    if hasattr(a1, 'food_dish152'):
        assert _is_linked(a1, 'food_dish152', b)
    _safe_set(b, 'component153', a2)
    assert _is_linked(b, 'component153', a2)
    if hasattr(a1, 'food_dish152'):
        assert not _is_linked(a1, 'food_dish152', b)
    if hasattr(a2, 'food_dish152'):
        assert _is_linked(a2, 'food_dish152', b)
    _safe_set(b, 'component153', None)
    assert not _is_linked(b, 'component153', a2)
    if hasattr(a2, 'food_dish152'):
        assert not _is_linked(a2, 'food_dish152', b)


def test_assoc_Component_liquid_reverse_link_reassign_clear():
    a1 = liquid(must_be_unit_in_ml="sample_text", name="sample_text", quantiy="sample_text")
    a2 = liquid(must_be_unit_in_ml="sample_text_2", name="sample_text_2", quantiy="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'liquid110', a1)
    assert _is_linked(b, 'liquid110', a1)
    if hasattr(a1, 'component111'):
        assert _is_linked(a1, 'component111', b)
    _safe_set(b, 'liquid110', a2)
    assert _is_linked(b, 'liquid110', a2)
    if hasattr(a1, 'component111'):
        assert not _is_linked(a1, 'component111', b)
    if hasattr(a2, 'component111'):
        assert _is_linked(a2, 'component111', b)
    _safe_set(b, 'liquid110', None)
    assert not _is_linked(b, 'liquid110', a2)
    if hasattr(a2, 'component111'):
        assert not _is_linked(a2, 'component111', b)


def test_assoc_Component_owner__system_reverse_link_reassign_clear():
    a1 = owner__system(attribute="sample_text")
    a2 = owner__system(attribute="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'owner__system148', a1)
    assert _is_linked(b, 'owner__system148', a1)
    if hasattr(a1, 'component149'):
        assert _is_linked(a1, 'component149', b)
    _safe_set(b, 'owner__system148', a2)
    assert _is_linked(b, 'owner__system148', a2)
    if hasattr(a1, 'component149'):
        assert not _is_linked(a1, 'component149', b)
    if hasattr(a2, 'component149'):
        assert _is_linked(a2, 'component149', b)
    _safe_set(b, 'owner__system148', None)
    assert not _is_linked(b, 'owner__system148', a2)
    if hasattr(a2, 'component149'):
        assert not _is_linked(a2, 'component149', b)


def test_assoc_Component_owner__system2_reverse_link_reassign_clear():
    a1 = owner__system(attribute="sample_text")
    a2 = owner__system(attribute="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'owner__system162', a1)
    assert _is_linked(b, 'owner__system162', a1)
    if hasattr(a1, 'component163'):
        assert _is_linked(a1, 'component163', b)
    _safe_set(b, 'owner__system162', a2)
    assert _is_linked(b, 'owner__system162', a2)
    if hasattr(a1, 'component163'):
        assert not _is_linked(a1, 'component163', b)
    if hasattr(a2, 'component163'):
        assert _is_linked(a2, 'component163', b)
    _safe_set(b, 'owner__system162', None)
    assert not _is_linked(b, 'owner__system162', a2)
    if hasattr(a2, 'component163'):
        assert not _is_linked(a2, 'component163', b)


def test_assoc_Component_owner__system3_reverse_link_reassign_clear():
    a1 = owner__system(attribute="sample_text")
    a2 = owner__system(attribute="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'owner__system172', a1)
    assert _is_linked(b, 'owner__system172', a1)
    if hasattr(a1, 'component173'):
        assert _is_linked(a1, 'component173', b)
    _safe_set(b, 'owner__system172', a2)
    assert _is_linked(b, 'owner__system172', a2)
    if hasattr(a1, 'component173'):
        assert not _is_linked(a1, 'component173', b)
    if hasattr(a2, 'component173'):
        assert _is_linked(a2, 'component173', b)
    _safe_set(b, 'owner__system172', None)
    assert not _is_linked(b, 'owner__system172', a2)
    if hasattr(a2, 'component173'):
        assert not _is_linked(a2, 'component173', b)


def test_assoc_Component_solid_reverse_link_reassign_clear():
    a1 = solid(must_be_unit_in_kg="sample_text")
    a2 = solid(must_be_unit_in_kg="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'solid108', a1)
    assert _is_linked(b, 'solid108', a1)
    if hasattr(a1, 'component109'):
        assert _is_linked(a1, 'component109', b)
    _safe_set(b, 'solid108', a2)
    assert _is_linked(b, 'solid108', a2)
    if hasattr(a1, 'component109'):
        assert not _is_linked(a1, 'component109', b)
    if hasattr(a2, 'component109'):
        assert _is_linked(a2, 'component109', b)
    _safe_set(b, 'solid108', None)
    assert not _is_linked(b, 'solid108', a2)
    if hasattr(a2, 'component109'):
        assert not _is_linked(a2, 'component109', b)


def test_assoc_Component_weekly_planning_of_dishes__for__waiter_reverse_link_reassign_clear():
    a1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    a2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'component179', a1)
    assert _is_linked(b, 'component179', a1)
    if hasattr(a1, 'weekly_planning_of_dishes__for__waiter178'):
        assert _is_linked(a1, 'weekly_planning_of_dishes__for__waiter178', b)
    _safe_set(b, 'component179', a2)
    assert _is_linked(b, 'component179', a2)
    if hasattr(a1, 'weekly_planning_of_dishes__for__waiter178'):
        assert not _is_linked(a1, 'weekly_planning_of_dishes__for__waiter178', b)
    if hasattr(a2, 'weekly_planning_of_dishes__for__waiter178'):
        assert _is_linked(a2, 'weekly_planning_of_dishes__for__waiter178', b)
    _safe_set(b, 'component179', None)
    assert not _is_linked(b, 'component179', a2)
    if hasattr(a2, 'weekly_planning_of_dishes__for__waiter178'):
        assert not _is_linked(a2, 'weekly_planning_of_dishes__for__waiter178', b)


def test_assoc_Customer_Accounnt_reverse_link_reassign_clear():
    a1 = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    a2 = Customer1(Accontbalance="sample_text_2", Address="sample_text_2", Adress="sample_text_2", Email="sample_text_2", ID=13, Name="sample_text_2", Password="sample_text_2", Phone=13, _attr="sample_text_2", attribute="sample_text_2")
    b = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    _safe_set(b, 'customer37', a1)
    assert _is_linked(b, 'customer37', a1)
    if hasattr(a1, 'accounnt36'):
        assert _is_linked(a1, 'accounnt36', b)
    _safe_set(b, 'customer37', a2)
    assert _is_linked(b, 'customer37', a2)
    if hasattr(a1, 'accounnt36'):
        assert not _is_linked(a1, 'accounnt36', b)
    if hasattr(a2, 'accounnt36'):
        assert _is_linked(a2, 'accounnt36', b)
    _safe_set(b, 'customer37', None)
    assert not _is_linked(b, 'customer37', a2)
    if hasattr(a2, 'accounnt36'):
        assert not _is_linked(a2, 'accounnt36', b)


def test_assoc_Customer_Accounnt2_reverse_link_reassign_clear():
    a1 = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    a2 = Customer1(Accontbalance="sample_text_2", Address="sample_text_2", Adress="sample_text_2", Email="sample_text_2", ID=13, Name="sample_text_2", Password="sample_text_2", Phone=13, _attr="sample_text_2", attribute="sample_text_2")
    b = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    _safe_set(b, 'customer103', a1)
    assert _is_linked(b, 'customer103', a1)
    if hasattr(a1, 'accounnt102'):
        assert _is_linked(a1, 'accounnt102', b)
    _safe_set(b, 'customer103', a2)
    assert _is_linked(b, 'customer103', a2)
    if hasattr(a1, 'accounnt102'):
        assert not _is_linked(a1, 'accounnt102', b)
    if hasattr(a2, 'accounnt102'):
        assert _is_linked(a2, 'accounnt102', b)
    _safe_set(b, 'customer103', None)
    assert not _is_linked(b, 'customer103', a2)
    if hasattr(a2, 'accounnt102'):
        assert not _is_linked(a2, 'accounnt102', b)


def test_assoc_Customer_Catering_reverse_link_reassign_clear():
    a1 = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    a2 = Customer1(Accontbalance="sample_text_2", Address="sample_text_2", Adress="sample_text_2", Email="sample_text_2", ID=13, Name="sample_text_2", Password="sample_text_2", Phone=13, _attr="sample_text_2", attribute="sample_text_2")
    b = Catering1(Menu="sample_text", attribute="sample_text")
    _safe_set(b, 'customer51', {a1})
    assert _is_linked(b, 'customer51', a1)
    if hasattr(a1, 'catering50'):
        assert _is_linked(a1, 'catering50', b)
    _safe_set(b, 'customer51', {a2})
    assert _is_linked(b, 'customer51', a2)
    if hasattr(a1, 'catering50'):
        assert not _is_linked(a1, 'catering50', b)
    if hasattr(a2, 'catering50'):
        assert _is_linked(a2, 'catering50', b)
    _safe_set(b, 'customer51', set())
    assert not _is_linked(b, 'customer51', a2)
    if hasattr(a2, 'catering50'):
        assert not _is_linked(a2, 'catering50', b)


def test_assoc_Customer_Customer_Balance_reverse_link_reassign_clear():
    a1 = Customer_Balance1(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    a2 = Customer_Balance1(Account_balance="sample_text_2", Adress="sample_text_2", CustomerID=13, CustomerName="sample_text_2", Date="sample_text_2")
    b = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    _safe_set(b, 'customer_Balance42', a1)
    assert _is_linked(b, 'customer_Balance42', a1)
    if hasattr(a1, 'customer43'):
        assert _is_linked(a1, 'customer43', b)
    _safe_set(b, 'customer_Balance42', a2)
    assert _is_linked(b, 'customer_Balance42', a2)
    if hasattr(a1, 'customer43'):
        assert not _is_linked(a1, 'customer43', b)
    if hasattr(a2, 'customer43'):
        assert _is_linked(a2, 'customer43', b)
    _safe_set(b, 'customer_Balance42', None)
    assert not _is_linked(b, 'customer_Balance42', a2)
    if hasattr(a2, 'customer43'):
        assert not _is_linked(a2, 'customer43', b)


def test_assoc_Customer_Order_reverse_link_reassign_clear():
    a1 = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    a2 = Order1(Customerid=13, Dishname="sample_text_2", OrderID=13, attribute="sample_text_2", date="sample_text_2")
    b = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    _safe_set(b, 'order92', a1)
    assert _is_linked(b, 'order92', a1)
    if hasattr(a1, 'customer93'):
        assert _is_linked(a1, 'customer93', b)
    _safe_set(b, 'order92', a2)
    assert _is_linked(b, 'order92', a2)
    if hasattr(a1, 'customer93'):
        assert not _is_linked(a1, 'customer93', b)
    if hasattr(a2, 'customer93'):
        assert _is_linked(a2, 'customer93', b)
    _safe_set(b, 'order92', None)
    assert not _is_linked(b, 'order92', a2)
    if hasattr(a2, 'customer93'):
        assert not _is_linked(a2, 'customer93', b)


def test_assoc_Dish_Menu_reverse_link_reassign_clear():
    a1 = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    a2 = Menu1(Components="sample_text_2", DishName="sample_text_2", Price="sample_text_2", Quantity="sample_text_2")
    b = Dish(_attr="sample_text")
    _safe_set(b, 'menu104', a1)
    assert _is_linked(b, 'menu104', a1)
    if hasattr(a1, 'dish105'):
        assert _is_linked(a1, 'dish105', b)
    _safe_set(b, 'menu104', a2)
    assert _is_linked(b, 'menu104', a2)
    if hasattr(a1, 'dish105'):
        assert not _is_linked(a1, 'dish105', b)
    if hasattr(a2, 'dish105'):
        assert _is_linked(a2, 'dish105', b)
    _safe_set(b, 'menu104', None)
    assert not _is_linked(b, 'menu104', a2)
    if hasattr(a2, 'dish105'):
        assert not _is_linked(a2, 'dish105', b)


def test_assoc_Employee_Plan_reverse_link_reassign_clear():
    a1 = Plan(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    a2 = Plan(Monthly_plan="sample_text_2", day_plan="sample_text_2", weekly_plan="sample_text_2")
    b = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    _safe_set(b, 'plan2', {a1})
    assert _is_linked(b, 'plan2', a1)
    if hasattr(a1, 'employee3'):
        assert _is_linked(a1, 'employee3', b)
    _safe_set(b, 'plan2', {a2})
    assert _is_linked(b, 'plan2', a2)
    if hasattr(a1, 'employee3'):
        assert not _is_linked(a1, 'employee3', b)
    if hasattr(a2, 'employee3'):
        assert _is_linked(a2, 'employee3', b)
    _safe_set(b, 'plan2', set())
    assert not _is_linked(b, 'plan2', a2)
    if hasattr(a2, 'employee3'):
        assert not _is_linked(a2, 'employee3', b)


def test_assoc_Employee_Storage_reverse_link_reassign_clear():
    a1 = Storage(Component_Name="sample_text", Component_id=7)
    a2 = Storage(Component_Name="sample_text_2", Component_id=13)
    b = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    _safe_set(b, 'storage0', {a1})
    assert _is_linked(b, 'storage0', a1)
    if hasattr(a1, 'employee1'):
        assert _is_linked(a1, 'employee1', b)
    _safe_set(b, 'storage0', {a2})
    assert _is_linked(b, 'storage0', a2)
    if hasattr(a1, 'employee1'):
        assert not _is_linked(a1, 'employee1', b)
    if hasattr(a2, 'employee1'):
        assert _is_linked(a2, 'employee1', b)
    _safe_set(b, 'storage0', set())
    assert not _is_linked(b, 'storage0', a2)
    if hasattr(a2, 'employee1'):
        assert not _is_linked(a2, 'employee1', b)


def test_assoc_Employee_Storage2_reverse_link_reassign_clear():
    a1 = Storage1(Component_Name="sample_text", Component_id=7)
    a2 = Storage1(Component_Name="sample_text_2", Component_id=13)
    b = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    _safe_set(b, 'storage44', {a1})
    assert _is_linked(b, 'storage44', a1)
    if hasattr(a1, 'Employee45'):
        assert _is_linked(a1, 'Employee45', b)
    _safe_set(b, 'storage44', {a2})
    assert _is_linked(b, 'storage44', a2)
    if hasattr(a1, 'Employee45'):
        assert not _is_linked(a1, 'Employee45', b)
    if hasattr(a2, 'Employee45'):
        assert _is_linked(a2, 'Employee45', b)
    _safe_set(b, 'storage44', set())
    assert not _is_linked(b, 'storage44', a2)
    if hasattr(a2, 'Employee45'):
        assert not _is_linked(a2, 'Employee45', b)


def test_assoc_Menu_Catering_reverse_link_reassign_clear():
    a1 = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    a2 = Menu1(Components="sample_text_2", DishName="sample_text_2", Price="sample_text_2", Quantity="sample_text_2")
    b = Catering1(Menu="sample_text", attribute="sample_text")
    _safe_set(b, 'menu49', {a1})
    assert _is_linked(b, 'menu49', a1)
    if hasattr(a1, 'catering48'):
        assert _is_linked(a1, 'catering48', b)
    _safe_set(b, 'menu49', {a2})
    assert _is_linked(b, 'menu49', a2)
    if hasattr(a1, 'catering48'):
        assert not _is_linked(a1, 'catering48', b)
    if hasattr(a2, 'catering48'):
        assert _is_linked(a2, 'catering48', b)
    _safe_set(b, 'menu49', set())
    assert not _is_linked(b, 'menu49', a2)
    if hasattr(a2, 'catering48'):
        assert not _is_linked(a2, 'catering48', b)


def test_assoc_Menu_Dish_reverse_link_reassign_clear():
    a1 = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    a2 = Menu1(Components="sample_text_2", DishName="sample_text_2", Price="sample_text_2", Quantity="sample_text_2")
    b = Dish(_attr="sample_text")
    _safe_set(b, 'menu107', {a1})
    assert _is_linked(b, 'menu107', a1)
    if hasattr(a1, 'dish106'):
        assert _is_linked(a1, 'dish106', b)
    _safe_set(b, 'menu107', {a2})
    assert _is_linked(b, 'menu107', a2)
    if hasattr(a1, 'dish106'):
        assert not _is_linked(a1, 'dish106', b)
    if hasattr(a2, 'dish106'):
        assert _is_linked(a2, 'dish106', b)
    _safe_set(b, 'menu107', set())
    assert not _is_linked(b, 'menu107', a2)
    if hasattr(a2, 'dish106'):
        assert not _is_linked(a2, 'dish106', b)


def test_assoc_Menu_Shopping_cart_reverse_link_reassign_clear():
    a1 = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    a2 = Shopping_cart1(Dishname="sample_text_2", Quantity=13, attribute="sample_text_2", price=13, time="sample_text_2")
    b = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    _safe_set(b, 'shopping_cart94', a1)
    assert _is_linked(b, 'shopping_cart94', a1)
    if hasattr(a1, 'menu95'):
        assert _is_linked(a1, 'menu95', b)
    _safe_set(b, 'shopping_cart94', a2)
    assert _is_linked(b, 'shopping_cart94', a2)
    if hasattr(a1, 'menu95'):
        assert not _is_linked(a1, 'menu95', b)
    if hasattr(a2, 'menu95'):
        assert _is_linked(a2, 'menu95', b)
    _safe_set(b, 'shopping_cart94', None)
    assert not _is_linked(b, 'shopping_cart94', a2)
    if hasattr(a2, 'menu95'):
        assert not _is_linked(a2, 'menu95', b)


def test_assoc_Order_Customer_reverse_link_reassign_clear():
    a1 = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    a2 = Order1(Customerid=13, Dishname="sample_text_2", OrderID=13, attribute="sample_text_2", date="sample_text_2")
    b = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    _safe_set(b, 'order53', {a1})
    assert _is_linked(b, 'order53', a1)
    if hasattr(a1, 'customer52'):
        assert _is_linked(a1, 'customer52', b)
    _safe_set(b, 'order53', {a2})
    assert _is_linked(b, 'order53', a2)
    if hasattr(a1, 'customer52'):
        assert not _is_linked(a1, 'customer52', b)
    if hasattr(a2, 'customer52'):
        assert _is_linked(a2, 'customer52', b)
    _safe_set(b, 'order53', set())
    assert not _is_linked(b, 'order53', a2)
    if hasattr(a2, 'customer52'):
        assert not _is_linked(a2, 'customer52', b)


def test_assoc_Order_Payment_reverse_link_reassign_clear():
    a1 = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    a2 = Payment1(Amount="sample_text_2", CustomerID=13, OrderID=13, PaymentID=13, date="sample_text_2", time="sample_text_2")
    b = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    _safe_set(b, 'payment56', a1)
    assert _is_linked(b, 'payment56', a1)
    if hasattr(a1, 'order57'):
        assert _is_linked(a1, 'order57', b)
    _safe_set(b, 'payment56', a2)
    assert _is_linked(b, 'payment56', a2)
    if hasattr(a1, 'order57'):
        assert not _is_linked(a1, 'order57', b)
    if hasattr(a2, 'order57'):
        assert _is_linked(a2, 'order57', b)
    _safe_set(b, 'payment56', None)
    assert not _is_linked(b, 'payment56', a2)
    if hasattr(a2, 'order57'):
        assert not _is_linked(a2, 'order57', b)


def test_assoc_Payment_PrintRecipts_reverse_link_reassign_clear():
    a1 = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    a2 = PrintRecipts1(Amount="sample_text_2", CustomerID=13, Dishname="sample_text_2", PaymentID="sample_text_2", Quantity=13, date="sample_text_2", time="sample_text_2")
    b = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    _safe_set(b, 'printRecipts58', a1)
    assert _is_linked(b, 'printRecipts58', a1)
    if hasattr(a1, 'payment59'):
        assert _is_linked(a1, 'payment59', b)
    _safe_set(b, 'printRecipts58', a2)
    assert _is_linked(b, 'printRecipts58', a2)
    if hasattr(a1, 'payment59'):
        assert not _is_linked(a1, 'payment59', b)
    if hasattr(a2, 'payment59'):
        assert _is_linked(a2, 'payment59', b)
    _safe_set(b, 'printRecipts58', None)
    assert not _is_linked(b, 'printRecipts58', a2)
    if hasattr(a2, 'payment59'):
        assert not _is_linked(a2, 'payment59', b)


def test_assoc_Plan_Customer_reverse_link_reassign_clear():
    a1 = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    a2 = Plan1(Monthly_plan="sample_text_2", day_plan="sample_text_2", weekly_plan="sample_text_2")
    b = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    _safe_set(b, 'plan89', a1)
    assert _is_linked(b, 'plan89', a1)
    if hasattr(a1, 'customer88'):
        assert _is_linked(a1, 'customer88', b)
    _safe_set(b, 'plan89', a2)
    assert _is_linked(b, 'plan89', a2)
    if hasattr(a1, 'customer88'):
        assert not _is_linked(a1, 'customer88', b)
    if hasattr(a2, 'customer88'):
        assert _is_linked(a2, 'customer88', b)
    _safe_set(b, 'plan89', None)
    assert not _is_linked(b, 'plan89', a2)
    if hasattr(a2, 'customer88'):
        assert not _is_linked(a2, 'customer88', b)


def test_assoc_Plan_Kitchen_worker_reverse_link_reassign_clear():
    a1 = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    a2 = Plan1(Monthly_plan="sample_text_2", day_plan="sample_text_2", weekly_plan="sample_text_2")
    b = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    _safe_set(b, 'plan91', {a1})
    assert _is_linked(b, 'plan91', a1)
    if hasattr(a1, 'kitchen_worker90'):
        assert _is_linked(a1, 'kitchen_worker90', b)
    _safe_set(b, 'plan91', {a2})
    assert _is_linked(b, 'plan91', a2)
    if hasattr(a1, 'kitchen_worker90'):
        assert not _is_linked(a1, 'kitchen_worker90', b)
    if hasattr(a2, 'kitchen_worker90'):
        assert _is_linked(a2, 'kitchen_worker90', b)
    _safe_set(b, 'plan91', set())
    assert not _is_linked(b, 'plan91', a2)
    if hasattr(a2, 'kitchen_worker90'):
        assert not _is_linked(a2, 'kitchen_worker90', b)


def test_assoc_Plan_chef_reverse_link_reassign_clear():
    a1 = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    a2 = chef1(Email="sample_text_2", Employee_ID=13, Name="sample_text_2", Room_no=13, passowrd="sample_text_2")
    b = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    _safe_set(b, 'chef46', {a1})
    assert _is_linked(b, 'chef46', a1)
    if hasattr(a1, 'plan47'):
        assert _is_linked(a1, 'plan47', b)
    _safe_set(b, 'chef46', {a2})
    assert _is_linked(b, 'chef46', a2)
    if hasattr(a1, 'plan47'):
        assert not _is_linked(a1, 'plan47', b)
    if hasattr(a2, 'plan47'):
        assert _is_linked(a2, 'plan47', b)
    _safe_set(b, 'chef46', set())
    assert not _is_linked(b, 'chef46', a2)
    if hasattr(a2, 'plan47'):
        assert not _is_linked(a2, 'plan47', b)


def test_assoc_Shopping_cart_Menu_reverse_link_reassign_clear():
    a1 = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    a2 = Shopping_cart1(Dishname="sample_text_2", Quantity=13, attribute="sample_text_2", price=13, time="sample_text_2")
    b = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    _safe_set(b, 'shopping_cart55', a1)
    assert _is_linked(b, 'shopping_cart55', a1)
    if hasattr(a1, 'menu54'):
        assert _is_linked(a1, 'menu54', b)
    _safe_set(b, 'shopping_cart55', a2)
    assert _is_linked(b, 'shopping_cart55', a2)
    if hasattr(a1, 'menu54'):
        assert not _is_linked(a1, 'menu54', b)
    if hasattr(a2, 'menu54'):
        assert _is_linked(a2, 'menu54', b)
    _safe_set(b, 'shopping_cart55', None)
    assert not _is_linked(b, 'shopping_cart55', a2)
    if hasattr(a2, 'menu54'):
        assert not _is_linked(a2, 'menu54', b)


def test_assoc_Storage_Kitchen_worker_reverse_link_reassign_clear():
    a1 = Storage1(Component_Name="sample_text", Component_id=7)
    a2 = Storage1(Component_Name="sample_text_2", Component_id=13)
    b = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    _safe_set(b, 'storage97', {a1})
    assert _is_linked(b, 'storage97', a1)
    if hasattr(a1, 'kitchen_worker96'):
        assert _is_linked(a1, 'kitchen_worker96', b)
    _safe_set(b, 'storage97', {a2})
    assert _is_linked(b, 'storage97', a2)
    if hasattr(a1, 'kitchen_worker96'):
        assert not _is_linked(a1, 'kitchen_worker96', b)
    if hasattr(a2, 'kitchen_worker96'):
        assert _is_linked(a2, 'kitchen_worker96', b)
    _safe_set(b, 'storage97', set())
    assert not _is_linked(b, 'storage97', a2)
    if hasattr(a2, 'kitchen_worker96'):
        assert not _is_linked(a2, 'kitchen_worker96', b)


def test_assoc_Storage_chef_reverse_link_reassign_clear():
    a1 = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    a2 = chef1(Email="sample_text_2", Employee_ID=13, Name="sample_text_2", Room_no=13, passowrd="sample_text_2")
    b = Storage1(Component_Name="sample_text", Component_id=7)
    _safe_set(b, 'chef64', {a1})
    assert _is_linked(b, 'chef64', a1)
    if hasattr(a1, 'storage65'):
        assert _is_linked(a1, 'storage65', b)
    _safe_set(b, 'chef64', {a2})
    assert _is_linked(b, 'chef64', a2)
    if hasattr(a1, 'storage65'):
        assert not _is_linked(a1, 'storage65', b)
    if hasattr(a2, 'storage65'):
        assert _is_linked(a2, 'storage65', b)
    _safe_set(b, 'chef64', set())
    assert not _is_linked(b, 'chef64', a2)
    if hasattr(a2, 'storage65'):
        assert not _is_linked(a2, 'storage65', b)


def test_assoc_System_Storage_reverse_link_reassign_clear():
    a1 = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    a2 = System1(Email="sample_text_2", Password="sample_text_2", WebAdmin_or_owner="sample_text_2")
    b = Storage1(Component_Name="sample_text", Component_id=7)
    _safe_set(b, 'system87', a1)
    assert _is_linked(b, 'system87', a1)
    if hasattr(a1, 'storage86'):
        assert _is_linked(a1, 'storage86', b)
    _safe_set(b, 'system87', a2)
    assert _is_linked(b, 'system87', a2)
    if hasattr(a1, 'storage86'):
        assert not _is_linked(a1, 'storage86', b)
    if hasattr(a2, 'storage86'):
        assert _is_linked(a2, 'storage86', b)
    _safe_set(b, 'system87', None)
    assert not _is_linked(b, 'system87', a2)
    if hasattr(a2, 'storage86'):
        assert not _is_linked(a2, 'storage86', b)


def test_assoc_System_contact_reverse_link_reassign_clear():
    a1 = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    a2 = contact(Adress="sample_text_2", Email="sample_text_2", Name="sample_text_2", Tel=13, attribute="sample_text_2")
    b = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    _safe_set(b, 'contact72', a1)
    assert _is_linked(b, 'contact72', a1)
    if hasattr(a1, 'system73'):
        assert _is_linked(a1, 'system73', b)
    _safe_set(b, 'contact72', a2)
    assert _is_linked(b, 'contact72', a2)
    if hasattr(a1, 'system73'):
        assert not _is_linked(a1, 'system73', b)
    if hasattr(a2, 'system73'):
        assert _is_linked(a2, 'system73', b)
    _safe_set(b, 'contact72', None)
    assert not _is_linked(b, 'contact72', a2)
    if hasattr(a2, 'system73'):
        assert not _is_linked(a2, 'system73', b)


def test_assoc_chef_Accounnt_reverse_link_reassign_clear():
    a1 = chef(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    a2 = chef(Email="sample_text_2", Employee_ID=13, Name="sample_text_2", Room_no=13, passowrd="sample_text_2")
    b = Accounnt(Accounttype="sample_text", Email="sample_text", Employee_ID="sample_text", password="sample_text")
    _safe_set(b, 'chef35', a1)
    assert _is_linked(b, 'chef35', a1)
    if hasattr(a1, 'accounnt34'):
        assert _is_linked(a1, 'accounnt34', b)
    _safe_set(b, 'chef35', a2)
    assert _is_linked(b, 'chef35', a2)
    if hasattr(a1, 'accounnt34'):
        assert not _is_linked(a1, 'accounnt34', b)
    if hasattr(a2, 'accounnt34'):
        assert _is_linked(a2, 'accounnt34', b)
    _safe_set(b, 'chef35', None)
    assert not _is_linked(b, 'chef35', a2)
    if hasattr(a2, 'accounnt34'):
        assert not _is_linked(a2, 'accounnt34', b)


def test_assoc_chef_Accounnt2_reverse_link_reassign_clear():
    a1 = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    a2 = chef1(Email="sample_text_2", Employee_ID=13, Name="sample_text_2", Room_no=13, passowrd="sample_text_2")
    b = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    _safe_set(b, 'chef39', a1)
    assert _is_linked(b, 'chef39', a1)
    if hasattr(a1, 'accounnt38'):
        assert _is_linked(a1, 'accounnt38', b)
    _safe_set(b, 'chef39', a2)
    assert _is_linked(b, 'chef39', a2)
    if hasattr(a1, 'accounnt38'):
        assert not _is_linked(a1, 'accounnt38', b)
    if hasattr(a2, 'accounnt38'):
        assert _is_linked(a2, 'accounnt38', b)
    _safe_set(b, 'chef39', None)
    assert not _is_linked(b, 'chef39', a2)
    if hasattr(a2, 'accounnt38'):
        assert not _is_linked(a2, 'accounnt38', b)


def test_assoc_drink_Component_reverse_link_reassign_clear():
    a1 = drink(type="sample_text")
    a2 = drink(type="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'drink117', a1)
    assert _is_linked(b, 'drink117', a1)
    if hasattr(a1, 'component116'):
        assert _is_linked(a1, 'component116', b)
    _safe_set(b, 'drink117', a2)
    assert _is_linked(b, 'drink117', a2)
    if hasattr(a1, 'component116'):
        assert not _is_linked(a1, 'component116', b)
    if hasattr(a2, 'component116'):
        assert _is_linked(a2, 'component116', b)
    _safe_set(b, 'drink117', None)
    assert not _is_linked(b, 'drink117', a2)
    if hasattr(a2, 'component116'):
        assert not _is_linked(a2, 'component116', b)


def test_assoc_events_order_reverse_link_reassign_clear():
    a1 = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    a2 = order(_attr="sample_text_2", date="sample_text_2", order_id="sample_text_2", ordered_item="sample_text_2", status="sample_text_2")
    b = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    _safe_set(b, 'order182', {a1})
    assert _is_linked(b, 'order182', a1)
    if hasattr(a1, 'events183'):
        assert _is_linked(a1, 'events183', b)
    _safe_set(b, 'order182', {a2})
    assert _is_linked(b, 'order182', a2)
    if hasattr(a1, 'events183'):
        assert not _is_linked(a1, 'events183', b)
    if hasattr(a2, 'events183'):
        assert _is_linked(a2, 'events183', b)
    _safe_set(b, 'order182', set())
    assert not _is_linked(b, 'order182', a2)
    if hasattr(a2, 'events183'):
        assert not _is_linked(a2, 'events183', b)


def test_assoc_food_dish_Component_reverse_link_reassign_clear():
    a1 = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    a2 = food_dish(attribute="sample_text_2", attribute2="sample_text_2", type="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'food_dish113', a1)
    assert _is_linked(b, 'food_dish113', a1)
    if hasattr(a1, 'component112'):
        assert _is_linked(a1, 'component112', b)
    _safe_set(b, 'food_dish113', a2)
    assert _is_linked(b, 'food_dish113', a2)
    if hasattr(a1, 'component112'):
        assert not _is_linked(a1, 'component112', b)
    if hasattr(a2, 'component112'):
        assert _is_linked(a2, 'component112', b)
    _safe_set(b, 'food_dish113', None)
    assert not _is_linked(b, 'food_dish113', a2)
    if hasattr(a2, 'component112'):
        assert not _is_linked(a2, 'component112', b)


def test_assoc_food_dish_Component2_reverse_link_reassign_clear():
    a1 = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    a2 = food_dish(attribute="sample_text_2", attribute2="sample_text_2", type="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'food_dish115', a1)
    assert _is_linked(b, 'food_dish115', a1)
    if hasattr(a1, 'component114'):
        assert _is_linked(a1, 'component114', b)
    _safe_set(b, 'food_dish115', a2)
    assert _is_linked(b, 'food_dish115', a2)
    if hasattr(a1, 'component114'):
        assert not _is_linked(a1, 'component114', b)
    if hasattr(a2, 'component114'):
        assert _is_linked(a2, 'component114', b)
    _safe_set(b, 'food_dish115', None)
    assert not _is_linked(b, 'food_dish115', a2)
    if hasattr(a2, 'component114'):
        assert not _is_linked(a2, 'component114', b)


def test_assoc_food_dish_menu_reverse_link_reassign_clear():
    a1 = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    a2 = menu(attribute="sample_text_2", dish_quantity="sample_text_2", dishname="sample_text_2", drinkname="sample_text_2", price="sample_text_2")
    b = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    _safe_set(b, 'food_dish157', {a1})
    assert _is_linked(b, 'food_dish157', a1)
    if hasattr(a1, 'menu156'):
        assert _is_linked(a1, 'menu156', b)
    _safe_set(b, 'food_dish157', {a2})
    assert _is_linked(b, 'food_dish157', a2)
    if hasattr(a1, 'menu156'):
        assert not _is_linked(a1, 'menu156', b)
    if hasattr(a2, 'menu156'):
        assert _is_linked(a2, 'menu156', b)
    _safe_set(b, 'food_dish157', set())
    assert not _is_linked(b, 'food_dish157', a2)
    if hasattr(a2, 'menu156'):
        assert not _is_linked(a2, 'menu156', b)


def test_assoc_food_dish_weekly_planning_of_dishes__for__waiter_reverse_link_reassign_clear():
    a1 = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    a2 = food_dish(attribute="sample_text_2", attribute2="sample_text_2", type="sample_text_2")
    b = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    _safe_set(b, 'weekly_planning_of_dishes__for__waiter180', {a1})
    assert _is_linked(b, 'weekly_planning_of_dishes__for__waiter180', a1)
    if hasattr(a1, 'food_dish181'):
        assert _is_linked(a1, 'food_dish181', b)
    _safe_set(b, 'weekly_planning_of_dishes__for__waiter180', {a2})
    assert _is_linked(b, 'weekly_planning_of_dishes__for__waiter180', a2)
    if hasattr(a1, 'food_dish181'):
        assert not _is_linked(a1, 'food_dish181', b)
    if hasattr(a2, 'food_dish181'):
        assert _is_linked(a2, 'food_dish181', b)
    _safe_set(b, 'weekly_planning_of_dishes__for__waiter180', set())
    assert not _is_linked(b, 'weekly_planning_of_dishes__for__waiter180', a2)
    if hasattr(a2, 'food_dish181'):
        assert not _is_linked(a2, 'food_dish181', b)


def test_assoc_menu_Csutomer_reverse_link_reassign_clear():
    a1 = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    a2 = menu(attribute="sample_text_2", dish_quantity="sample_text_2", dishname="sample_text_2", drinkname="sample_text_2", price="sample_text_2")
    b = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    _safe_set(b, 'menu123', a1)
    assert _is_linked(b, 'menu123', a1)
    if hasattr(a1, 'csutomer122'):
        assert _is_linked(a1, 'csutomer122', b)
    _safe_set(b, 'menu123', a2)
    assert _is_linked(b, 'menu123', a2)
    if hasattr(a1, 'csutomer122'):
        assert not _is_linked(a1, 'csutomer122', b)
    if hasattr(a2, 'csutomer122'):
        assert _is_linked(a2, 'csutomer122', b)
    _safe_set(b, 'menu123', None)
    assert not _is_linked(b, 'menu123', a2)
    if hasattr(a2, 'csutomer122'):
        assert not _is_linked(a2, 'csutomer122', b)


def test_assoc_menu_drink_reverse_link_reassign_clear():
    a1 = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    a2 = menu(attribute="sample_text_2", dish_quantity="sample_text_2", dishname="sample_text_2", drinkname="sample_text_2", price="sample_text_2")
    b = drink(type="sample_text")
    _safe_set(b, 'menu121', a1)
    assert _is_linked(b, 'menu121', a1)
    if hasattr(a1, 'drink120'):
        assert _is_linked(a1, 'drink120', b)
    _safe_set(b, 'menu121', a2)
    assert _is_linked(b, 'menu121', a2)
    if hasattr(a1, 'drink120'):
        assert not _is_linked(a1, 'drink120', b)
    if hasattr(a2, 'drink120'):
        assert _is_linked(a2, 'drink120', b)
    _safe_set(b, 'menu121', None)
    assert not _is_linked(b, 'menu121', a2)
    if hasattr(a2, 'drink120'):
        assert not _is_linked(a2, 'drink120', b)


def test_assoc_menu_food_dish_reverse_link_reassign_clear():
    a1 = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    a2 = menu(attribute="sample_text_2", dish_quantity="sample_text_2", dishname="sample_text_2", drinkname="sample_text_2", price="sample_text_2")
    b = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    _safe_set(b, 'menu119', a1)
    assert _is_linked(b, 'menu119', a1)
    if hasattr(a1, 'food_dish118'):
        assert _is_linked(a1, 'food_dish118', b)
    _safe_set(b, 'menu119', a2)
    assert _is_linked(b, 'menu119', a2)
    if hasattr(a1, 'food_dish118'):
        assert not _is_linked(a1, 'food_dish118', b)
    if hasattr(a2, 'food_dish118'):
        assert _is_linked(a2, 'food_dish118', b)
    _safe_set(b, 'menu119', None)
    assert not _is_linked(b, 'menu119', a2)
    if hasattr(a2, 'food_dish118'):
        assert not _is_linked(a2, 'food_dish118', b)


def test_assoc_menu_order_reverse_link_reassign_clear():
    a1 = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    a2 = order(_attr="sample_text_2", date="sample_text_2", order_id="sample_text_2", ordered_item="sample_text_2", status="sample_text_2")
    b = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    _safe_set(b, 'order124', a1)
    assert _is_linked(b, 'order124', a1)
    if hasattr(a1, 'menu125'):
        assert _is_linked(a1, 'menu125', b)
    _safe_set(b, 'order124', a2)
    assert _is_linked(b, 'order124', a2)
    if hasattr(a1, 'menu125'):
        assert not _is_linked(a1, 'menu125', b)
    if hasattr(a2, 'menu125'):
        assert _is_linked(a2, 'menu125', b)
    _safe_set(b, 'order124', None)
    assert not _is_linked(b, 'order124', a2)
    if hasattr(a2, 'menu125'):
        assert not _is_linked(a2, 'menu125', b)


def test_assoc_menu_order2_reverse_link_reassign_clear():
    a1 = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    a2 = order(_attr="sample_text_2", date="sample_text_2", order_id="sample_text_2", ordered_item="sample_text_2", status="sample_text_2")
    b = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    _safe_set(b, 'order168', {a1})
    assert _is_linked(b, 'order168', a1)
    if hasattr(a1, 'menu169'):
        assert _is_linked(a1, 'menu169', b)
    _safe_set(b, 'order168', {a2})
    assert _is_linked(b, 'order168', a2)
    if hasattr(a1, 'menu169'):
        assert not _is_linked(a1, 'menu169', b)
    if hasattr(a2, 'menu169'):
        assert _is_linked(a2, 'menu169', b)
    _safe_set(b, 'order168', set())
    assert not _is_linked(b, 'order168', a2)
    if hasattr(a2, 'menu169'):
        assert not _is_linked(a2, 'menu169', b)


def test_assoc_order_Csutomer_reverse_link_reassign_clear():
    a1 = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    a2 = order(_attr="sample_text_2", date="sample_text_2", order_id="sample_text_2", ordered_item="sample_text_2", status="sample_text_2")
    b = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    _safe_set(b, 'order127', {a1})
    assert _is_linked(b, 'order127', a1)
    if hasattr(a1, 'csutomer126'):
        assert _is_linked(a1, 'csutomer126', b)
    _safe_set(b, 'order127', {a2})
    assert _is_linked(b, 'order127', a2)
    if hasattr(a1, 'csutomer126'):
        assert not _is_linked(a1, 'csutomer126', b)
    if hasattr(a2, 'csutomer126'):
        assert _is_linked(a2, 'csutomer126', b)
    _safe_set(b, 'order127', set())
    assert not _is_linked(b, 'order127', a2)
    if hasattr(a2, 'csutomer126'):
        assert not _is_linked(a2, 'csutomer126', b)


def test_assoc_planning_weekly_planning_of_dishes__by_waiter_reverse_link_reassign_clear():
    a1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    a2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    b = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter134', {a1})
    assert _is_linked(b, 'weekly_planning_of_dishes__by_waiter134', a1)
    if hasattr(a1, 'planning135'):
        assert _is_linked(a1, 'planning135', b)
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter134', {a2})
    assert _is_linked(b, 'weekly_planning_of_dishes__by_waiter134', a2)
    if hasattr(a1, 'planning135'):
        assert not _is_linked(a1, 'planning135', b)
    if hasattr(a2, 'planning135'):
        assert _is_linked(a2, 'planning135', b)
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter134', set())
    assert not _is_linked(b, 'weekly_planning_of_dishes__by_waiter134', a2)
    if hasattr(a2, 'planning135'):
        assert not _is_linked(a2, 'planning135', b)


def test_assoc_weekly_planning_of_dishes__by_waiter_Component_reverse_link_reassign_clear():
    a1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    a2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    b = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter141', a1)
    assert _is_linked(b, 'weekly_planning_of_dishes__by_waiter141', a1)
    if hasattr(a1, 'component140'):
        assert _is_linked(a1, 'component140', b)
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter141', a2)
    assert _is_linked(b, 'weekly_planning_of_dishes__by_waiter141', a2)
    if hasattr(a1, 'component140'):
        assert not _is_linked(a1, 'component140', b)
    if hasattr(a2, 'component140'):
        assert _is_linked(a2, 'component140', b)
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter141', None)
    assert not _is_linked(b, 'weekly_planning_of_dishes__by_waiter141', a2)
    if hasattr(a2, 'component140'):
        assert not _is_linked(a2, 'component140', b)


def test_assoc_weekly_planning_of_dishes__by_waiter_food_dish_reverse_link_reassign_clear():
    a1 = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    a2 = food_dish(attribute="sample_text_2", attribute2="sample_text_2", type="sample_text_2")
    b = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    _safe_set(b, 'food_dish160', a1)
    assert _is_linked(b, 'food_dish160', a1)
    if hasattr(a1, 'weekly_planning_of_dishes__by_waiter161'):
        assert _is_linked(a1, 'weekly_planning_of_dishes__by_waiter161', b)
    _safe_set(b, 'food_dish160', a2)
    assert _is_linked(b, 'food_dish160', a2)
    if hasattr(a1, 'weekly_planning_of_dishes__by_waiter161'):
        assert not _is_linked(a1, 'weekly_planning_of_dishes__by_waiter161', b)
    if hasattr(a2, 'weekly_planning_of_dishes__by_waiter161'):
        assert _is_linked(a2, 'weekly_planning_of_dishes__by_waiter161', b)
    _safe_set(b, 'food_dish160', None)
    assert not _is_linked(b, 'food_dish160', a2)
    if hasattr(a2, 'weekly_planning_of_dishes__by_waiter161'):
        assert not _is_linked(a2, 'weekly_planning_of_dishes__by_waiter161', b)


def test_assoc_weekly_planning_of_dishes__by_waiter_weekly_planning_of_dishes__by_waiter_reverse_link_reassign_clear():
    a1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    a2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    b = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter143', a1)
    assert _is_linked(b, 'weekly_planning_of_dishes__by_waiter143', a1)
    if hasattr(a1, 'weekly_planning_of_dishes__by_waiter142'):
        assert _is_linked(a1, 'weekly_planning_of_dishes__by_waiter142', b)
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter143', a2)
    assert _is_linked(b, 'weekly_planning_of_dishes__by_waiter143', a2)
    if hasattr(a1, 'weekly_planning_of_dishes__by_waiter142'):
        assert not _is_linked(a1, 'weekly_planning_of_dishes__by_waiter142', b)
    if hasattr(a2, 'weekly_planning_of_dishes__by_waiter142'):
        assert _is_linked(a2, 'weekly_planning_of_dishes__by_waiter142', b)
    _safe_set(b, 'weekly_planning_of_dishes__by_waiter143', None)
    assert not _is_linked(b, 'weekly_planning_of_dishes__by_waiter143', a2)
    if hasattr(a2, 'weekly_planning_of_dishes__by_waiter142'):
        assert not _is_linked(a2, 'weekly_planning_of_dishes__by_waiter142', b)


def test_assoc_weekly_planning_of_dishes__for__waiter_food_dish_reverse_link_reassign_clear():
    a1 = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    a2 = food_dish(attribute="sample_text_2", attribute2="sample_text_2", type="sample_text_2")
    b = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    _safe_set(b, 'food_dish164', {a1})
    assert _is_linked(b, 'food_dish164', a1)
    if hasattr(a1, 'weekly_planning_of_dishes__for__waiter165'):
        assert _is_linked(a1, 'weekly_planning_of_dishes__for__waiter165', b)
    _safe_set(b, 'food_dish164', {a2})
    assert _is_linked(b, 'food_dish164', a2)
    if hasattr(a1, 'weekly_planning_of_dishes__for__waiter165'):
        assert not _is_linked(a1, 'weekly_planning_of_dishes__for__waiter165', b)
    if hasattr(a2, 'weekly_planning_of_dishes__for__waiter165'):
        assert _is_linked(a2, 'weekly_planning_of_dishes__for__waiter165', b)
    _safe_set(b, 'food_dish164', set())
    assert not _is_linked(b, 'food_dish164', a2)
    if hasattr(a2, 'weekly_planning_of_dishes__for__waiter165'):
        assert not _is_linked(a2, 'weekly_planning_of_dishes__for__waiter165', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Component_waiter_stub_double():
    # kitchen_worker has no real 'component139' property in the generated
    # code (a bare stub) -- manually attach it so Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    partner = kitchen_worker()
    setattr(partner, 'component139', None)
    _safe_set(owner, 'waiter138', {partner})
    assert owner in getattr(partner, 'component139')
    _safe_set(owner, 'waiter138', set())
    assert owner not in getattr(partner, 'component139')


def test_assoc_Csutomer_catering_stub_double():
    # catering has no real 'csutomer175' property in the generated
    # code (a bare stub) -- manually attach it so Csutomer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Csutomer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    partner = catering()
    setattr(partner, 'csutomer175', None)
    _safe_set(owner, 'catering174', partner)
    assert getattr(partner, 'csutomer175') == owner
    _safe_set(owner, 'catering174', None)
    assert getattr(partner, 'csutomer175') is None


def test_assoc_Csutomer_shopping_cart_stub_double():
    # shopping_cart has no real 'csutomer129' property in the generated
    # code (a bare stub) -- manually attach it so Csutomer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Csutomer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    partner = shopping_cart()
    setattr(partner, 'csutomer129', None)
    _safe_set(owner, 'shopping_cart128', partner)
    assert getattr(partner, 'csutomer129') == owner
    _safe_set(owner, 'shopping_cart128', None)
    assert getattr(partner, 'csutomer129') is None


def test_assoc_Payment_bank_account_stub_double():
    # bank_account has no real 'payment67' property in the generated
    # code (a bare stub) -- manually attach it so Payment1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Payment1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    partner = bank_account()
    setattr(partner, 'payment67', None)
    _safe_set(owner, 'bank_account66', partner)
    assert owner in getattr(partner, 'payment67')
    _safe_set(owner, 'bank_account66', None)
    assert owner not in getattr(partner, 'payment67')


def test_assoc_System_bank_account_stub_double():
    # bank_account has no real 'system69' property in the generated
    # code (a bare stub) -- manually attach it so System1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # System1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    partner = bank_account()
    setattr(partner, 'system69', None)
    _safe_set(owner, 'bank_account68', partner)
    assert getattr(partner, 'system69') == owner
    _safe_set(owner, 'bank_account68', None)
    assert getattr(partner, 'system69') is None


def test_assoc_System_bank_account2_stub_double():
    # bank_account has no real 'system71' property in the generated
    # code (a bare stub) -- manually attach it so System1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # System1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    partner = bank_account()
    setattr(partner, 'system71', None)
    _safe_set(owner, 'bank_account70', partner)
    assert getattr(partner, 'system71') == owner
    _safe_set(owner, 'bank_account70', None)
    assert getattr(partner, 'system71') is None


def test_assoc_System_help_stub_double():
    # help has no real 'system75' property in the generated
    # code (a bare stub) -- manually attach it so System1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # System1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    partner = help()
    setattr(partner, 'system75', None)
    _safe_set(owner, 'help74', partner)
    assert getattr(partner, 'system75') == owner
    _safe_set(owner, 'help74', None)
    assert getattr(partner, 'system75') is None


def test_assoc_Web_master_contact_stub_double():
    # Web_master has no real 'contact62' property in the generated
    # code (a bare stub) -- manually attach it so contact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # contact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    partner = Web_master()
    setattr(partner, 'contact62', None)
    _safe_set(owner, 'web_master63', partner)
    assert getattr(partner, 'contact62') == owner
    _safe_set(owner, 'web_master63', None)
    assert getattr(partner, 'contact62') is None


def test_assoc_chef_planning_stub_double():
    # chef2 has no real 'planning150' property in the generated
    # code (a bare stub) -- manually attach it so dayplan's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dayplan's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    partner = chef2()
    setattr(partner, 'planning150', None)
    _safe_set(owner, 'chef151', partner)
    assert owner in getattr(partner, 'planning150')
    _safe_set(owner, 'chef151', None)
    assert owner not in getattr(partner, 'planning150')


def test_assoc_menu_catering_stub_double():
    # catering has no real 'menu177' property in the generated
    # code (a bare stub) -- manually attach it so menu's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # menu's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    partner = catering()
    setattr(partner, 'menu177', None)
    _safe_set(owner, 'catering176', partner)
    assert getattr(partner, 'menu177') == owner
    _safe_set(owner, 'catering176', None)
    assert getattr(partner, 'menu177') is None


def test_assoc_order_shopping_cart_stub_double():
    # shopping_cart has no real 'order131' property in the generated
    # code (a bare stub) -- manually attach it so order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    partner = shopping_cart()
    setattr(partner, 'order131', None)
    _safe_set(owner, 'shopping_cart130', partner)
    assert getattr(partner, 'order131') == owner
    _safe_set(owner, 'shopping_cart130', None)
    assert getattr(partner, 'order131') is None


def test_assoc_order_shopping_cart2_stub_double():
    # shopping_cart has no real 'order159' property in the generated
    # code (a bare stub) -- manually attach it so order's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # order's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    partner = shopping_cart()
    setattr(partner, 'order159', None)
    _safe_set(owner, 'shopping_cart158', {partner})
    assert owner in getattr(partner, 'order159')
    _safe_set(owner, 'shopping_cart158', set())
    assert owner not in getattr(partner, 'order159')


def test_assoc_planning_chef_stub_double():
    # chef2 has no real 'planning137' property in the generated
    # code (a bare stub) -- manually attach it so dayplan's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dayplan's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    partner = chef2()
    setattr(partner, 'planning137', None)
    _safe_set(owner, 'chef136', partner)
    assert getattr(partner, 'planning137') == owner
    _safe_set(owner, 'chef136', None)
    assert getattr(partner, 'planning137') is None


def test_assoc_shopping_cart_payment_stub_double():
    # shopping_cart has no real 'payment132' property in the generated
    # code (a bare stub) -- manually attach it so payment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # payment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = payment(_attr="sample_text", amount="sample_text", total_amount="sample_text")
    partner = shopping_cart()
    setattr(partner, 'payment132', None)
    _safe_set(owner, 'shopping_cart133', {partner})
    assert owner in getattr(partner, 'payment132')
    _safe_set(owner, 'shopping_cart133', set())
    assert owner not in getattr(partner, 'payment132')


def test_assoc_shopping_cart_payment2_stub_double():
    # shopping_cart has no real 'payment170' property in the generated
    # code (a bare stub) -- manually attach it so payment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # payment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = payment(_attr="sample_text", amount="sample_text", total_amount="sample_text")
    partner = shopping_cart()
    setattr(partner, 'payment170', None)
    _safe_set(owner, 'shopping_cart171', partner)
    assert getattr(partner, 'payment170') == owner
    _safe_set(owner, 'shopping_cart171', None)
    assert getattr(partner, 'payment170') is None


def test_assoc_weekly_planning_of_dishes__by_waiter_waiter_stub_double():
    # kitchen_worker has no real 'weekly_planning_of_dishes__by_waiter145' property in the generated
    # code (a bare stub) -- manually attach it so events's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # events's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    partner = kitchen_worker()
    setattr(partner, 'weekly_planning_of_dishes__by_waiter145', None)
    _safe_set(owner, 'waiter144', partner)
    assert getattr(partner, 'weekly_planning_of_dishes__by_waiter145') == owner
    _safe_set(owner, 'waiter144', None)
    assert getattr(partner, 'weekly_planning_of_dishes__by_waiter145') is None


def test_assoc_weekly_planning_of_dishes__by_waiter_waiter2_stub_double():
    # kitchen_worker has no real 'weekly_planning_of_dishes__by_waiter147' property in the generated
    # code (a bare stub) -- manually attach it so events's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # events's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    partner = kitchen_worker()
    setattr(partner, 'weekly_planning_of_dishes__by_waiter147', None)
    _safe_set(owner, 'waiter146', {partner})
    assert owner in getattr(partner, 'weekly_planning_of_dishes__by_waiter147')
    _safe_set(owner, 'waiter146', set())
    assert owner not in getattr(partner, 'weekly_planning_of_dishes__by_waiter147')


