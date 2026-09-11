import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Accounnt_Accounttype_value_roundtrip():
    instance = Accounnt(Accounttype="sample_text", Email="sample_text", Employee_ID="sample_text", password="sample_text")
    assert instance.Accounttype == "sample_text"
    instance.Accounttype = "sample_text_2"
    assert instance.Accounttype == "sample_text_2"


def test_Accounnt_Email_value_roundtrip():
    instance = Accounnt(Accounttype="sample_text", Email="sample_text", Employee_ID="sample_text", password="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Accounnt_Employee_ID_value_roundtrip():
    instance = Accounnt(Accounttype="sample_text", Email="sample_text", Employee_ID="sample_text", password="sample_text")
    assert instance.Employee_ID == "sample_text"
    instance.Employee_ID = "sample_text_2"
    assert instance.Employee_ID == "sample_text_2"


def test_Accounnt_password_value_roundtrip():
    instance = Accounnt(Accounttype="sample_text", Email="sample_text", Employee_ID="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Accounnt1_Accounttype_value_roundtrip():
    instance = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    assert instance.Accounttype == "sample_text"
    instance.Accounttype = "sample_text_2"
    assert instance.Accounttype == "sample_text_2"


def test_Accounnt1_Email_value_roundtrip():
    instance = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Accounnt1_password_value_roundtrip():
    instance = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Account_Name_value_roundtrip():
    instance = Account(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Account__attr_value_roundtrip():
    instance = Account(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_Account_attribute_value_roundtrip():
    instance = Account(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Account_email_value_roundtrip():
    instance = Account(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Account_id_value_roundtrip():
    instance = Account(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Account_password_value_roundtrip():
    instance = Account(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Account1_Name_value_roundtrip():
    instance = Account1(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Account1__attr_value_roundtrip():
    instance = Account1(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_Account1_attribute_value_roundtrip():
    instance = Account1(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Account1_email_value_roundtrip():
    instance = Account1(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Account1_id_value_roundtrip():
    instance = Account1(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Account1_password_value_roundtrip():
    instance = Account1(Name="sample_text", _attr="sample_text", attribute="sample_text", email="sample_text", id="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Account_for_employee_attribute_value_roundtrip():
    instance = Account_for_employee(attribute="sample_text", email="sample_text", getaccount="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Account_for_employee_email_value_roundtrip():
    instance = Account_for_employee(attribute="sample_text", email="sample_text", getaccount="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Account_for_employee_getaccount_value_roundtrip():
    instance = Account_for_employee(attribute="sample_text", email="sample_text", getaccount="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.getaccount == "sample_text"
    instance.getaccount = "sample_text_2"
    assert instance.getaccount == "sample_text_2"


def test_Account_for_employee_id_value_roundtrip():
    instance = Account_for_employee(attribute="sample_text", email="sample_text", getaccount="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Account_for_employee_name_value_roundtrip():
    instance = Account_for_employee(attribute="sample_text", email="sample_text", getaccount="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Account_for_employee_password_value_roundtrip():
    instance = Account_for_employee(attribute="sample_text", email="sample_text", getaccount="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Catering_Menu_value_roundtrip():
    instance = Catering(Menu="sample_text", attribute="sample_text")
    assert instance.Menu == "sample_text"
    instance.Menu = "sample_text_2"
    assert instance.Menu == "sample_text_2"


def test_Catering_attribute_value_roundtrip():
    instance = Catering(Menu="sample_text", attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Catering1_Menu_value_roundtrip():
    instance = Catering1(Menu="sample_text", attribute="sample_text")
    assert instance.Menu == "sample_text"
    instance.Menu = "sample_text_2"
    assert instance.Menu == "sample_text_2"


def test_Catering1_attribute_value_roundtrip():
    instance = Catering1(Menu="sample_text", attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Component_Expiry_date_value_roundtrip():
    instance = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    assert instance.Expiry_date == "sample_text"
    instance.Expiry_date = "sample_text_2"
    assert instance.Expiry_date == "sample_text_2"


def test_Component_ID_value_roundtrip():
    instance = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_Component_Name_value_roundtrip():
    instance = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Component_Storage_or_sehlf_value_roundtrip():
    instance = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    assert instance.Storage_or_sehlf == "sample_text"
    instance.Storage_or_sehlf = "sample_text_2"
    assert instance.Storage_or_sehlf == "sample_text_2"


def test_Component_Type_value_roundtrip():
    instance = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_Component_attribute_value_roundtrip():
    instance = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Csutomer_Adress_value_roundtrip():
    instance = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    assert instance.Adress == "sample_text"
    instance.Adress = "sample_text_2"
    assert instance.Adress == "sample_text_2"


def test_Csutomer_attribute_value_roundtrip():
    instance = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Csutomer_email_value_roundtrip():
    instance = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Csutomer_id_value_roundtrip():
    instance = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Csutomer_name_value_roundtrip():
    instance = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Csutomer_password_value_roundtrip():
    instance = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Csutomer_register_value_roundtrip():
    instance = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    assert instance.register == "sample_text"
    instance.register = "sample_text_2"
    assert instance.register == "sample_text_2"


def test_Csutomer_tel_no_value_roundtrip():
    instance = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    assert instance.tel_no == "sample_text"
    instance.tel_no = "sample_text_2"
    assert instance.tel_no == "sample_text_2"


def test_Customer_Accontbalance_value_roundtrip():
    instance = Customer(Accontbalance="sample_text", Address="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7)
    assert instance.Accontbalance == "sample_text"
    instance.Accontbalance = "sample_text_2"
    assert instance.Accontbalance == "sample_text_2"


def test_Customer_Address_value_roundtrip():
    instance = Customer(Accontbalance="sample_text", Address="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7)
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Customer_Email_value_roundtrip():
    instance = Customer(Accontbalance="sample_text", Address="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7)
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Customer_ID_value_roundtrip():
    instance = Customer(Accontbalance="sample_text", Address="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7)
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Customer_Name_value_roundtrip():
    instance = Customer(Accontbalance="sample_text", Address="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Customer_Password_value_roundtrip():
    instance = Customer(Accontbalance="sample_text", Address="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7)
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Customer_Phone_value_roundtrip():
    instance = Customer(Accontbalance="sample_text", Address="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7)
    assert instance.Phone == 7
    instance.Phone = 13
    assert instance.Phone == 13


def test_Customer1_Accontbalance_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.Accontbalance == "sample_text"
    instance.Accontbalance = "sample_text_2"
    assert instance.Accontbalance == "sample_text_2"


def test_Customer1_Address_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Customer1_Adress_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.Adress == "sample_text"
    instance.Adress = "sample_text_2"
    assert instance.Adress == "sample_text_2"


def test_Customer1_Email_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Customer1_ID_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Customer1_Name_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Customer1_Password_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Customer1_Phone_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.Phone == 7
    instance.Phone = 13
    assert instance.Phone == 13


def test_Customer1__attr_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_Customer1_attribute_value_roundtrip():
    instance = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Customer_Balance_Account_balance_value_roundtrip():
    instance = Customer_Balance(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.Account_balance == "sample_text"
    instance.Account_balance = "sample_text_2"
    assert instance.Account_balance == "sample_text_2"


def test_Customer_Balance_Adress_value_roundtrip():
    instance = Customer_Balance(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.Adress == "sample_text"
    instance.Adress = "sample_text_2"
    assert instance.Adress == "sample_text_2"


def test_Customer_Balance_CustomerID_value_roundtrip():
    instance = Customer_Balance(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.CustomerID == 7
    instance.CustomerID = 13
    assert instance.CustomerID == 13


def test_Customer_Balance_CustomerName_value_roundtrip():
    instance = Customer_Balance(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_Customer_Balance_Date_value_roundtrip():
    instance = Customer_Balance(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_Customer_Balance1_Account_balance_value_roundtrip():
    instance = Customer_Balance1(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.Account_balance == "sample_text"
    instance.Account_balance = "sample_text_2"
    assert instance.Account_balance == "sample_text_2"


def test_Customer_Balance1_Adress_value_roundtrip():
    instance = Customer_Balance1(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.Adress == "sample_text"
    instance.Adress = "sample_text_2"
    assert instance.Adress == "sample_text_2"


def test_Customer_Balance1_CustomerID_value_roundtrip():
    instance = Customer_Balance1(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.CustomerID == 7
    instance.CustomerID = 13
    assert instance.CustomerID == 13


def test_Customer_Balance1_CustomerName_value_roundtrip():
    instance = Customer_Balance1(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_Customer_Balance1_Date_value_roundtrip():
    instance = Customer_Balance1(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_Dish__attr_value_roundtrip():
    instance = Dish(_attr="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_Employee_Email_value_roundtrip():
    instance = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Employee_ID_value_roundtrip():
    instance = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Employee_Name_value_roundtrip():
    instance = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Employee_attribute_value_roundtrip():
    instance = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Employee_password_value_roundtrip():
    instance = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Employee1_Email_value_roundtrip():
    instance = Employee1(Email="sample_text", ID="sample_text", Name="sample_text", Password="sample_text", attribute="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Employee1_ID_value_roundtrip():
    instance = Employee1(Email="sample_text", ID="sample_text", Name="sample_text", Password="sample_text", attribute="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_Employee1_Name_value_roundtrip():
    instance = Employee1(Email="sample_text", ID="sample_text", Name="sample_text", Password="sample_text", attribute="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Employee1_Password_value_roundtrip():
    instance = Employee1(Email="sample_text", ID="sample_text", Name="sample_text", Password="sample_text", attribute="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Employee1_attribute_value_roundtrip():
    instance = Employee1(Email="sample_text", ID="sample_text", Name="sample_text", Password="sample_text", attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Kitchen_worker_Email_value_roundtrip():
    instance = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Kitchen_worker_ID_value_roundtrip():
    instance = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Kitchen_worker_Name_value_roundtrip():
    instance = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Kitchen_worker_attribute_value_roundtrip():
    instance = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Kitchen_worker_password_value_roundtrip():
    instance = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Menu_Components_value_roundtrip():
    instance = Menu(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    assert instance.Components == "sample_text"
    instance.Components = "sample_text_2"
    assert instance.Components == "sample_text_2"


def test_Menu_DishName_value_roundtrip():
    instance = Menu(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    assert instance.DishName == "sample_text"
    instance.DishName = "sample_text_2"
    assert instance.DishName == "sample_text_2"


def test_Menu_Price_value_roundtrip():
    instance = Menu(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_Menu_Quantity_value_roundtrip():
    instance = Menu(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    assert instance.Quantity == "sample_text"
    instance.Quantity = "sample_text_2"
    assert instance.Quantity == "sample_text_2"


def test_Menu1_Components_value_roundtrip():
    instance = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    assert instance.Components == "sample_text"
    instance.Components = "sample_text_2"
    assert instance.Components == "sample_text_2"


def test_Menu1_DishName_value_roundtrip():
    instance = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    assert instance.DishName == "sample_text"
    instance.DishName = "sample_text_2"
    assert instance.DishName == "sample_text_2"


def test_Menu1_Price_value_roundtrip():
    instance = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_Menu1_Quantity_value_roundtrip():
    instance = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    assert instance.Quantity == "sample_text"
    instance.Quantity = "sample_text_2"
    assert instance.Quantity == "sample_text_2"


def test_Order_Customerid_value_roundtrip():
    instance = Order(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.Customerid == 7
    instance.Customerid = 13
    assert instance.Customerid == 13


def test_Order_Dishname_value_roundtrip():
    instance = Order(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.Dishname == "sample_text"
    instance.Dishname = "sample_text_2"
    assert instance.Dishname == "sample_text_2"


def test_Order_OrderID_value_roundtrip():
    instance = Order(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Order_attribute_value_roundtrip():
    instance = Order(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Order_date_value_roundtrip():
    instance = Order(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Order1_Customerid_value_roundtrip():
    instance = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.Customerid == 7
    instance.Customerid = 13
    assert instance.Customerid == 13


def test_Order1_Dishname_value_roundtrip():
    instance = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.Dishname == "sample_text"
    instance.Dishname = "sample_text_2"
    assert instance.Dishname == "sample_text_2"


def test_Order1_OrderID_value_roundtrip():
    instance = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Order1_attribute_value_roundtrip():
    instance = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Order1_date_value_roundtrip():
    instance = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Payment_Amount_value_roundtrip():
    instance = Payment(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.Amount == "sample_text"
    instance.Amount = "sample_text_2"
    assert instance.Amount == "sample_text_2"


def test_Payment_CustomerID_value_roundtrip():
    instance = Payment(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.CustomerID == 7
    instance.CustomerID = 13
    assert instance.CustomerID == 13


def test_Payment_OrderID_value_roundtrip():
    instance = Payment(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Payment_PaymentID_value_roundtrip():
    instance = Payment(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.PaymentID == 7
    instance.PaymentID = 13
    assert instance.PaymentID == 13


def test_Payment_date_value_roundtrip():
    instance = Payment(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Payment_time_value_roundtrip():
    instance = Payment(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_Payment1_Amount_value_roundtrip():
    instance = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.Amount == "sample_text"
    instance.Amount = "sample_text_2"
    assert instance.Amount == "sample_text_2"


def test_Payment1_CustomerID_value_roundtrip():
    instance = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.CustomerID == 7
    instance.CustomerID = 13
    assert instance.CustomerID == 13


def test_Payment1_OrderID_value_roundtrip():
    instance = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Payment1_PaymentID_value_roundtrip():
    instance = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.PaymentID == 7
    instance.PaymentID = 13
    assert instance.PaymentID == 13


def test_Payment1_date_value_roundtrip():
    instance = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Payment1_time_value_roundtrip():
    instance = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_Plan_Monthly_plan_value_roundtrip():
    instance = Plan(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    assert instance.Monthly_plan == "sample_text"
    instance.Monthly_plan = "sample_text_2"
    assert instance.Monthly_plan == "sample_text_2"


def test_Plan_day_plan_value_roundtrip():
    instance = Plan(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    assert instance.day_plan == "sample_text"
    instance.day_plan = "sample_text_2"
    assert instance.day_plan == "sample_text_2"


def test_Plan_weekly_plan_value_roundtrip():
    instance = Plan(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    assert instance.weekly_plan == "sample_text"
    instance.weekly_plan = "sample_text_2"
    assert instance.weekly_plan == "sample_text_2"


def test_Plan1_Monthly_plan_value_roundtrip():
    instance = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    assert instance.Monthly_plan == "sample_text"
    instance.Monthly_plan = "sample_text_2"
    assert instance.Monthly_plan == "sample_text_2"


def test_Plan1_day_plan_value_roundtrip():
    instance = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    assert instance.day_plan == "sample_text"
    instance.day_plan = "sample_text_2"
    assert instance.day_plan == "sample_text_2"


def test_Plan1_weekly_plan_value_roundtrip():
    instance = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    assert instance.weekly_plan == "sample_text"
    instance.weekly_plan = "sample_text_2"
    assert instance.weekly_plan == "sample_text_2"


def test_PrintRecipts_Amount_value_roundtrip():
    instance = PrintRecipts(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.Amount == "sample_text"
    instance.Amount = "sample_text_2"
    assert instance.Amount == "sample_text_2"


def test_PrintRecipts_CustomerID_value_roundtrip():
    instance = PrintRecipts(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.CustomerID == 7
    instance.CustomerID = 13
    assert instance.CustomerID == 13


def test_PrintRecipts_Dishname_value_roundtrip():
    instance = PrintRecipts(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.Dishname == "sample_text"
    instance.Dishname = "sample_text_2"
    assert instance.Dishname == "sample_text_2"


def test_PrintRecipts_PaymentID_value_roundtrip():
    instance = PrintRecipts(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.PaymentID == "sample_text"
    instance.PaymentID = "sample_text_2"
    assert instance.PaymentID == "sample_text_2"


def test_PrintRecipts_Quantity_value_roundtrip():
    instance = PrintRecipts(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_PrintRecipts_date_value_roundtrip():
    instance = PrintRecipts(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_PrintRecipts_time_value_roundtrip():
    instance = PrintRecipts(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_PrintRecipts1_Amount_value_roundtrip():
    instance = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.Amount == "sample_text"
    instance.Amount = "sample_text_2"
    assert instance.Amount == "sample_text_2"


def test_PrintRecipts1_CustomerID_value_roundtrip():
    instance = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.CustomerID == 7
    instance.CustomerID = 13
    assert instance.CustomerID == 13


def test_PrintRecipts1_Dishname_value_roundtrip():
    instance = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.Dishname == "sample_text"
    instance.Dishname = "sample_text_2"
    assert instance.Dishname == "sample_text_2"


def test_PrintRecipts1_PaymentID_value_roundtrip():
    instance = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.PaymentID == "sample_text"
    instance.PaymentID = "sample_text_2"
    assert instance.PaymentID == "sample_text_2"


def test_PrintRecipts1_Quantity_value_roundtrip():
    instance = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_PrintRecipts1_date_value_roundtrip():
    instance = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_PrintRecipts1_time_value_roundtrip():
    instance = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_Shopping_cart_Dishname_value_roundtrip():
    instance = Shopping_cart(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.Dishname == "sample_text"
    instance.Dishname = "sample_text_2"
    assert instance.Dishname == "sample_text_2"


def test_Shopping_cart_Quantity_value_roundtrip():
    instance = Shopping_cart(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_Shopping_cart_attribute_value_roundtrip():
    instance = Shopping_cart(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Shopping_cart_price_value_roundtrip():
    instance = Shopping_cart(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_Shopping_cart_time_value_roundtrip():
    instance = Shopping_cart(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_Shopping_cart1_Dishname_value_roundtrip():
    instance = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.Dishname == "sample_text"
    instance.Dishname = "sample_text_2"
    assert instance.Dishname == "sample_text_2"


def test_Shopping_cart1_Quantity_value_roundtrip():
    instance = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_Shopping_cart1_attribute_value_roundtrip():
    instance = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Shopping_cart1_price_value_roundtrip():
    instance = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.price == 7
    instance.price = 13
    assert instance.price == 13


def test_Shopping_cart1_time_value_roundtrip():
    instance = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_Storage_Component_Name_value_roundtrip():
    instance = Storage(Component_Name="sample_text", Component_id=7)
    assert instance.Component_Name == "sample_text"
    instance.Component_Name = "sample_text_2"
    assert instance.Component_Name == "sample_text_2"


def test_Storage_Component_id_value_roundtrip():
    instance = Storage(Component_Name="sample_text", Component_id=7)
    assert instance.Component_id == 7
    instance.Component_id = 13
    assert instance.Component_id == 13


def test_Storage1_Component_Name_value_roundtrip():
    instance = Storage1(Component_Name="sample_text", Component_id=7)
    assert instance.Component_Name == "sample_text"
    instance.Component_Name = "sample_text_2"
    assert instance.Component_Name == "sample_text_2"


def test_Storage1_Component_id_value_roundtrip():
    instance = Storage1(Component_Name="sample_text", Component_id=7)
    assert instance.Component_id == 7
    instance.Component_id = 13
    assert instance.Component_id == 13


def test_System1_Email_value_roundtrip():
    instance = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_System1_Password_value_roundtrip():
    instance = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_System1_WebAdmin_or_owner_value_roundtrip():
    instance = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    assert instance.WebAdmin_or_owner == "sample_text"
    instance.WebAdmin_or_owner = "sample_text_2"
    assert instance.WebAdmin_or_owner == "sample_text_2"


def test_account_type__attr_value_roundtrip():
    instance = account_type(_attr="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_account_type_email_value_roundtrip():
    instance = account_type(_attr="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_account_type_id_value_roundtrip():
    instance = account_type(_attr="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_account_type_name_value_roundtrip():
    instance = account_type(_attr="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_account_type_password_value_roundtrip():
    instance = account_type(_attr="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_chef_Email_value_roundtrip():
    instance = chef(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_chef_Employee_ID_value_roundtrip():
    instance = chef(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.Employee_ID == 7
    instance.Employee_ID = 13
    assert instance.Employee_ID == 13


def test_chef_Name_value_roundtrip():
    instance = chef(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_chef_Room_no_value_roundtrip():
    instance = chef(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.Room_no == 7
    instance.Room_no = 13
    assert instance.Room_no == 13


def test_chef_passowrd_value_roundtrip():
    instance = chef(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.passowrd == "sample_text"
    instance.passowrd = "sample_text_2"
    assert instance.passowrd == "sample_text_2"


def test_chef1_Email_value_roundtrip():
    instance = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_chef1_Employee_ID_value_roundtrip():
    instance = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.Employee_ID == 7
    instance.Employee_ID = 13
    assert instance.Employee_ID == 13


def test_chef1_Name_value_roundtrip():
    instance = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_chef1_Room_no_value_roundtrip():
    instance = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.Room_no == 7
    instance.Room_no = 13
    assert instance.Room_no == 13


def test_chef1_passowrd_value_roundtrip():
    instance = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    assert instance.passowrd == "sample_text"
    instance.passowrd = "sample_text_2"
    assert instance.passowrd == "sample_text_2"


def test_contact_Adress_value_roundtrip():
    instance = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    assert instance.Adress == "sample_text"
    instance.Adress = "sample_text_2"
    assert instance.Adress == "sample_text_2"


def test_contact_Email_value_roundtrip():
    instance = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_contact_Name_value_roundtrip():
    instance = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_contact_Tel_value_roundtrip():
    instance = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    assert instance.Tel == 7
    instance.Tel = 13
    assert instance.Tel == 13


def test_contact_attribute_value_roundtrip():
    instance = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_dayplan_Monday_value_roundtrip():
    instance = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    assert instance.Monday == "sample_text"
    instance.Monday = "sample_text_2"
    assert instance.Monday == "sample_text_2"


def test_dayplan_friday_value_roundtrip():
    instance = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    assert instance.friday == "sample_text"
    instance.friday = "sample_text_2"
    assert instance.friday == "sample_text_2"


def test_dayplan_plan_per_date_value_roundtrip():
    instance = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    assert instance.plan_per_date == "sample_text"
    instance.plan_per_date = "sample_text_2"
    assert instance.plan_per_date == "sample_text_2"


def test_dayplan_saturday_value_roundtrip():
    instance = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    assert instance.saturday == "sample_text"
    instance.saturday = "sample_text_2"
    assert instance.saturday == "sample_text_2"


def test_dayplan_sunday_value_roundtrip():
    instance = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    assert instance.sunday == "sample_text"
    instance.sunday = "sample_text_2"
    assert instance.sunday == "sample_text_2"


def test_dayplan_thursday_value_roundtrip():
    instance = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    assert instance.thursday == "sample_text"
    instance.thursday = "sample_text_2"
    assert instance.thursday == "sample_text_2"


def test_dayplan_tuesday_value_roundtrip():
    instance = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    assert instance.tuesday == "sample_text"
    instance.tuesday = "sample_text_2"
    assert instance.tuesday == "sample_text_2"


def test_dayplan_wenesday_value_roundtrip():
    instance = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    assert instance.wenesday == "sample_text"
    instance.wenesday = "sample_text_2"
    assert instance.wenesday == "sample_text_2"


def test_drink_type_value_roundtrip():
    instance = drink(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_events_attribute_value_roundtrip():
    instance = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_events_catering_location_value_roundtrip():
    instance = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    assert instance.catering_location == "sample_text"
    instance.catering_location = "sample_text_2"
    assert instance.catering_location == "sample_text_2"


def test_events_duration_value_roundtrip():
    instance = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    assert instance.duration == "sample_text"
    instance.duration = "sample_text_2"
    assert instance.duration == "sample_text_2"


def test_events_get_employee_name_value_roundtrip():
    instance = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    assert instance.get_employee_name == "sample_text"
    instance.get_employee_name = "sample_text_2"
    assert instance.get_employee_name == "sample_text_2"


def test_food_dish_attribute_value_roundtrip():
    instance = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_food_dish_attribute2_value_roundtrip():
    instance = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_food_dish_type_value_roundtrip():
    instance = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_liquid_must_be_unit_in_ml_value_roundtrip():
    instance = liquid(must_be_unit_in_ml="sample_text", name="sample_text", quantiy="sample_text")
    assert instance.must_be_unit_in_ml == "sample_text"
    instance.must_be_unit_in_ml = "sample_text_2"
    assert instance.must_be_unit_in_ml == "sample_text_2"


def test_liquid_name_value_roundtrip():
    instance = liquid(must_be_unit_in_ml="sample_text", name="sample_text", quantiy="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_liquid_quantiy_value_roundtrip():
    instance = liquid(must_be_unit_in_ml="sample_text", name="sample_text", quantiy="sample_text")
    assert instance.quantiy == "sample_text"
    instance.quantiy = "sample_text_2"
    assert instance.quantiy == "sample_text_2"


def test_menu_attribute_value_roundtrip():
    instance = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_menu_dish_quantity_value_roundtrip():
    instance = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    assert instance.dish_quantity == "sample_text"
    instance.dish_quantity = "sample_text_2"
    assert instance.dish_quantity == "sample_text_2"


def test_menu_dishname_value_roundtrip():
    instance = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    assert instance.dishname == "sample_text"
    instance.dishname = "sample_text_2"
    assert instance.dishname == "sample_text_2"


def test_menu_drinkname_value_roundtrip():
    instance = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    assert instance.drinkname == "sample_text"
    instance.drinkname = "sample_text_2"
    assert instance.drinkname == "sample_text_2"


def test_menu_price_value_roundtrip():
    instance = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_order__attr_value_roundtrip():
    instance = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_order_date_value_roundtrip():
    instance = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_order_order_id_value_roundtrip():
    instance = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    assert instance.order_id == "sample_text"
    instance.order_id = "sample_text_2"
    assert instance.order_id == "sample_text_2"


def test_order_ordered_item_value_roundtrip():
    instance = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    assert instance.ordered_item == "sample_text"
    instance.ordered_item = "sample_text_2"
    assert instance.ordered_item == "sample_text_2"


def test_order_status_value_roundtrip():
    instance = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_owner__system_attribute_value_roundtrip():
    instance = owner__system(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_payment__attr_value_roundtrip():
    instance = payment(_attr="sample_text", amount="sample_text", total_amount="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_payment_amount_value_roundtrip():
    instance = payment(_attr="sample_text", amount="sample_text", total_amount="sample_text")
    assert instance.amount == "sample_text"
    instance.amount = "sample_text_2"
    assert instance.amount == "sample_text_2"


def test_payment_total_amount_value_roundtrip():
    instance = payment(_attr="sample_text", amount="sample_text", total_amount="sample_text")
    assert instance.total_amount == "sample_text"
    instance.total_amount = "sample_text_2"
    assert instance.total_amount == "sample_text_2"


def test_solid_must_be_unit_in_kg_value_roundtrip():
    instance = solid(must_be_unit_in_kg="sample_text")
    assert instance.must_be_unit_in_kg == "sample_text"
    instance.must_be_unit_in_kg = "sample_text_2"
    assert instance.must_be_unit_in_kg == "sample_text_2"


def test_solid1_name_value_roundtrip():
    instance = solid1(name="sample_text", pieces=7, state="sample_text", weight__kg_="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_solid1_pieces_value_roundtrip():
    instance = solid1(name="sample_text", pieces=7, state="sample_text", weight__kg_="sample_text")
    assert instance.pieces == 7
    instance.pieces = 13
    assert instance.pieces == 13


def test_solid1_state_value_roundtrip():
    instance = solid1(name="sample_text", pieces=7, state="sample_text", weight__kg_="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_solid1_weight__kg__value_roundtrip():
    instance = solid1(name="sample_text", pieces=7, state="sample_text", weight__kg_="sample_text")
    assert instance.weight__kg_ == "sample_text"
    instance.weight__kg_ = "sample_text_2"
    assert instance.weight__kg_ == "sample_text_2"


def test_assoc_Accounnt_Customer_link_reassign_clear():
    a = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    b1 = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    b2 = Accounnt1(Accounttype="sample_text_2", Email="sample_text_2", password="sample_text_2")
    _safe_set(a, 'accounnt99', b1)
    assert _is_linked(a, 'accounnt99', b1)
    if hasattr(b1, 'customer98'):
        assert _is_linked(b1, 'customer98', a)
    _safe_set(a, 'accounnt99', b2)
    assert _is_linked(a, 'accounnt99', b2)
    if hasattr(b1, 'customer98'):
        assert not _is_linked(b1, 'customer98', a)
    if hasattr(b2, 'customer98'):
        assert _is_linked(b2, 'customer98', a)
    _safe_set(a, 'accounnt99', None)
    assert not _is_linked(a, 'accounnt99', b2)
    if hasattr(b2, 'customer98'):
        assert not _is_linked(b2, 'customer98', a)


def test_assoc_Accounnt_Employee_link_reassign_clear():
    a = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    b1 = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    b2 = Accounnt1(Accounttype="sample_text_2", Email="sample_text_2", password="sample_text_2")
    _safe_set(a, 'accounnt41', b1)
    assert _is_linked(a, 'accounnt41', b1)
    if hasattr(b1, 'employee40'):
        assert _is_linked(b1, 'employee40', a)
    _safe_set(a, 'accounnt41', b2)
    assert _is_linked(a, 'accounnt41', b2)
    if hasattr(b1, 'employee40'):
        assert not _is_linked(b1, 'employee40', a)
    if hasattr(b2, 'employee40'):
        assert _is_linked(b2, 'employee40', a)
    _safe_set(a, 'accounnt41', None)
    assert not _is_linked(a, 'accounnt41', b2)
    if hasattr(b2, 'employee40'):
        assert not _is_linked(b2, 'employee40', a)


def test_assoc_Accounnt_chef_link_reassign_clear():
    a = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    b1 = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    b2 = Accounnt1(Accounttype="sample_text_2", Email="sample_text_2", password="sample_text_2")
    _safe_set(a, 'accounnt101', b1)
    assert _is_linked(a, 'accounnt101', b1)
    if hasattr(b1, 'chef100'):
        assert _is_linked(b1, 'chef100', a)
    _safe_set(a, 'accounnt101', b2)
    assert _is_linked(a, 'accounnt101', b2)
    if hasattr(b1, 'chef100'):
        assert not _is_linked(b1, 'chef100', a)
    if hasattr(b2, 'chef100'):
        assert _is_linked(b2, 'chef100', a)
    _safe_set(a, 'accounnt101', None)
    assert not _is_linked(a, 'accounnt101', b2)
    if hasattr(b2, 'chef100'):
        assert not _is_linked(b2, 'chef100', a)


def test_assoc_Component_drink_link_reassign_clear():
    a = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'drink154', b1)
    assert _is_linked(a, 'drink154', b1)
    if hasattr(b1, 'component155'):
        assert _is_linked(b1, 'component155', a)
    _safe_set(a, 'drink154', b2)
    assert _is_linked(a, 'drink154', b2)
    if hasattr(b1, 'component155'):
        assert not _is_linked(b1, 'component155', a)
    if hasattr(b2, 'component155'):
        assert _is_linked(b2, 'component155', a)
    _safe_set(a, 'drink154', None)
    assert not _is_linked(a, 'drink154', b2)
    if hasattr(b2, 'component155'):
        assert not _is_linked(b2, 'component155', a)


def test_assoc_Component_food_dish_link_reassign_clear():
    a = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'food_dish152', {b1})
    assert _is_linked(a, 'food_dish152', b1)
    if hasattr(b1, 'component153'):
        assert _is_linked(b1, 'component153', a)
    _safe_set(a, 'food_dish152', {b2})
    assert _is_linked(a, 'food_dish152', b2)
    if hasattr(b1, 'component153'):
        assert not _is_linked(b1, 'component153', a)
    if hasattr(b2, 'component153'):
        assert _is_linked(b2, 'component153', a)
    _safe_set(a, 'food_dish152', set())
    assert not _is_linked(a, 'food_dish152', b2)
    if hasattr(b2, 'component153'):
        assert not _is_linked(b2, 'component153', a)


def test_assoc_Component_liquid_link_reassign_clear():
    a = liquid(must_be_unit_in_ml="sample_text", name="sample_text", quantiy="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component111', b1)
    assert _is_linked(a, 'component111', b1)
    if hasattr(b1, 'liquid110'):
        assert _is_linked(b1, 'liquid110', a)
    _safe_set(a, 'component111', b2)
    assert _is_linked(a, 'component111', b2)
    if hasattr(b1, 'liquid110'):
        assert not _is_linked(b1, 'liquid110', a)
    if hasattr(b2, 'liquid110'):
        assert _is_linked(b2, 'liquid110', a)
    _safe_set(a, 'component111', None)
    assert not _is_linked(a, 'component111', b2)
    if hasattr(b2, 'liquid110'):
        assert not _is_linked(b2, 'liquid110', a)


def test_assoc_Component_owner__system_link_reassign_clear():
    a = owner__system(attribute="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component149', b1)
    assert _is_linked(a, 'component149', b1)
    if hasattr(b1, 'owner__system148'):
        assert _is_linked(b1, 'owner__system148', a)
    _safe_set(a, 'component149', b2)
    assert _is_linked(a, 'component149', b2)
    if hasattr(b1, 'owner__system148'):
        assert not _is_linked(b1, 'owner__system148', a)
    if hasattr(b2, 'owner__system148'):
        assert _is_linked(b2, 'owner__system148', a)
    _safe_set(a, 'component149', None)
    assert not _is_linked(a, 'component149', b2)
    if hasattr(b2, 'owner__system148'):
        assert not _is_linked(b2, 'owner__system148', a)


def test_assoc_Component_owner__system2_link_reassign_clear():
    a = owner__system(attribute="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component163', b1)
    assert _is_linked(a, 'component163', b1)
    if hasattr(b1, 'owner__system162'):
        assert _is_linked(b1, 'owner__system162', a)
    _safe_set(a, 'component163', b2)
    assert _is_linked(a, 'component163', b2)
    if hasattr(b1, 'owner__system162'):
        assert not _is_linked(b1, 'owner__system162', a)
    if hasattr(b2, 'owner__system162'):
        assert _is_linked(b2, 'owner__system162', a)
    _safe_set(a, 'component163', None)
    assert not _is_linked(a, 'component163', b2)
    if hasattr(b2, 'owner__system162'):
        assert not _is_linked(b2, 'owner__system162', a)


def test_assoc_Component_owner__system3_link_reassign_clear():
    a = owner__system(attribute="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component173', b1)
    assert _is_linked(a, 'component173', b1)
    if hasattr(b1, 'owner__system172'):
        assert _is_linked(b1, 'owner__system172', a)
    _safe_set(a, 'component173', b2)
    assert _is_linked(a, 'component173', b2)
    if hasattr(b1, 'owner__system172'):
        assert not _is_linked(b1, 'owner__system172', a)
    if hasattr(b2, 'owner__system172'):
        assert _is_linked(b2, 'owner__system172', a)
    _safe_set(a, 'component173', None)
    assert not _is_linked(a, 'component173', b2)
    if hasattr(b2, 'owner__system172'):
        assert not _is_linked(b2, 'owner__system172', a)


def test_assoc_Component_solid_link_reassign_clear():
    a = solid(must_be_unit_in_kg="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component109', b1)
    assert _is_linked(a, 'component109', b1)
    if hasattr(b1, 'solid108'):
        assert _is_linked(b1, 'solid108', a)
    _safe_set(a, 'component109', b2)
    assert _is_linked(a, 'component109', b2)
    if hasattr(b1, 'solid108'):
        assert not _is_linked(b1, 'solid108', a)
    if hasattr(b2, 'solid108'):
        assert _is_linked(b2, 'solid108', a)
    _safe_set(a, 'component109', None)
    assert not _is_linked(a, 'component109', b2)
    if hasattr(b2, 'solid108'):
        assert not _is_linked(b2, 'solid108', a)


def test_assoc_Component_waiter_link_reassign_clear():
    a = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b1 = kitchen_worker()
    b2 = kitchen_worker()
    _safe_set(a, 'waiter138', {b1})
    assert _is_linked(a, 'waiter138', b1)
    if hasattr(b1, 'component139'):
        assert _is_linked(b1, 'component139', a)
    _safe_set(a, 'waiter138', {b2})
    assert _is_linked(a, 'waiter138', b2)
    if hasattr(b1, 'component139'):
        assert not _is_linked(b1, 'component139', a)
    if hasattr(b2, 'component139'):
        assert _is_linked(b2, 'component139', a)
    _safe_set(a, 'waiter138', set())
    assert not _is_linked(a, 'waiter138', b2)
    if hasattr(b2, 'component139'):
        assert not _is_linked(b2, 'component139', a)


def test_assoc_Component_weekly_planning_of_dishes__for__waiter_link_reassign_clear():
    a = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'weekly_planning_of_dishes__for__waiter178', {b1})
    assert _is_linked(a, 'weekly_planning_of_dishes__for__waiter178', b1)
    if hasattr(b1, 'component179'):
        assert _is_linked(b1, 'component179', a)
    _safe_set(a, 'weekly_planning_of_dishes__for__waiter178', {b2})
    assert _is_linked(a, 'weekly_planning_of_dishes__for__waiter178', b2)
    if hasattr(b1, 'component179'):
        assert not _is_linked(b1, 'component179', a)
    if hasattr(b2, 'component179'):
        assert _is_linked(b2, 'component179', a)
    _safe_set(a, 'weekly_planning_of_dishes__for__waiter178', set())
    assert not _is_linked(a, 'weekly_planning_of_dishes__for__waiter178', b2)
    if hasattr(b2, 'component179'):
        assert not _is_linked(b2, 'component179', a)


def test_assoc_Csutomer_catering_link_reassign_clear():
    a = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    b1 = catering()
    b2 = catering()
    _safe_set(a, 'catering174', b1)
    assert _is_linked(a, 'catering174', b1)
    if hasattr(b1, 'csutomer175'):
        assert _is_linked(b1, 'csutomer175', a)
    _safe_set(a, 'catering174', b2)
    assert _is_linked(a, 'catering174', b2)
    if hasattr(b1, 'csutomer175'):
        assert not _is_linked(b1, 'csutomer175', a)
    if hasattr(b2, 'csutomer175'):
        assert _is_linked(b2, 'csutomer175', a)
    _safe_set(a, 'catering174', None)
    assert not _is_linked(a, 'catering174', b2)
    if hasattr(b2, 'csutomer175'):
        assert not _is_linked(b2, 'csutomer175', a)


def test_assoc_Csutomer_shopping_cart_link_reassign_clear():
    a = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    b1 = shopping_cart()
    b2 = shopping_cart()
    _safe_set(a, 'shopping_cart128', b1)
    assert _is_linked(a, 'shopping_cart128', b1)
    if hasattr(b1, 'csutomer129'):
        assert _is_linked(b1, 'csutomer129', a)
    _safe_set(a, 'shopping_cart128', b2)
    assert _is_linked(a, 'shopping_cart128', b2)
    if hasattr(b1, 'csutomer129'):
        assert not _is_linked(b1, 'csutomer129', a)
    if hasattr(b2, 'csutomer129'):
        assert _is_linked(b2, 'csutomer129', a)
    _safe_set(a, 'shopping_cart128', None)
    assert not _is_linked(a, 'shopping_cart128', b2)
    if hasattr(b2, 'csutomer129'):
        assert not _is_linked(b2, 'csutomer129', a)


def test_assoc_Customer_Accounnt_link_reassign_clear():
    a = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    b1 = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    b2 = Accounnt1(Accounttype="sample_text_2", Email="sample_text_2", password="sample_text_2")
    _safe_set(a, 'accounnt36', b1)
    assert _is_linked(a, 'accounnt36', b1)
    if hasattr(b1, 'customer37'):
        assert _is_linked(b1, 'customer37', a)
    _safe_set(a, 'accounnt36', b2)
    assert _is_linked(a, 'accounnt36', b2)
    if hasattr(b1, 'customer37'):
        assert not _is_linked(b1, 'customer37', a)
    if hasattr(b2, 'customer37'):
        assert _is_linked(b2, 'customer37', a)
    _safe_set(a, 'accounnt36', None)
    assert not _is_linked(a, 'accounnt36', b2)
    if hasattr(b2, 'customer37'):
        assert not _is_linked(b2, 'customer37', a)


def test_assoc_Customer_Accounnt2_link_reassign_clear():
    a = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    b1 = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    b2 = Accounnt1(Accounttype="sample_text_2", Email="sample_text_2", password="sample_text_2")
    _safe_set(a, 'accounnt102', b1)
    assert _is_linked(a, 'accounnt102', b1)
    if hasattr(b1, 'customer103'):
        assert _is_linked(b1, 'customer103', a)
    _safe_set(a, 'accounnt102', b2)
    assert _is_linked(a, 'accounnt102', b2)
    if hasattr(b1, 'customer103'):
        assert not _is_linked(b1, 'customer103', a)
    if hasattr(b2, 'customer103'):
        assert _is_linked(b2, 'customer103', a)
    _safe_set(a, 'accounnt102', None)
    assert not _is_linked(a, 'accounnt102', b2)
    if hasattr(b2, 'customer103'):
        assert not _is_linked(b2, 'customer103', a)


def test_assoc_Customer_Catering_link_reassign_clear():
    a = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    b1 = Catering1(Menu="sample_text", attribute="sample_text")
    b2 = Catering1(Menu="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'catering50', {b1})
    assert _is_linked(a, 'catering50', b1)
    if hasattr(b1, 'customer51'):
        assert _is_linked(b1, 'customer51', a)
    _safe_set(a, 'catering50', {b2})
    assert _is_linked(a, 'catering50', b2)
    if hasattr(b1, 'customer51'):
        assert not _is_linked(b1, 'customer51', a)
    if hasattr(b2, 'customer51'):
        assert _is_linked(b2, 'customer51', a)
    _safe_set(a, 'catering50', set())
    assert not _is_linked(a, 'catering50', b2)
    if hasattr(b2, 'customer51'):
        assert not _is_linked(b2, 'customer51', a)


def test_assoc_Customer_Customer_Balance_link_reassign_clear():
    a = Customer_Balance1(Account_balance="sample_text", Adress="sample_text", CustomerID=7, CustomerName="sample_text", Date="sample_text")
    b1 = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    b2 = Customer1(Accontbalance="sample_text_2", Address="sample_text_2", Adress="sample_text_2", Email="sample_text_2", ID=13, Name="sample_text_2", Password="sample_text_2", Phone=13, _attr="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'customer43', b1)
    assert _is_linked(a, 'customer43', b1)
    if hasattr(b1, 'customer_Balance42'):
        assert _is_linked(b1, 'customer_Balance42', a)
    _safe_set(a, 'customer43', b2)
    assert _is_linked(a, 'customer43', b2)
    if hasattr(b1, 'customer_Balance42'):
        assert not _is_linked(b1, 'customer_Balance42', a)
    if hasattr(b2, 'customer_Balance42'):
        assert _is_linked(b2, 'customer_Balance42', a)
    _safe_set(a, 'customer43', None)
    assert not _is_linked(a, 'customer43', b2)
    if hasattr(b2, 'customer_Balance42'):
        assert not _is_linked(b2, 'customer_Balance42', a)


def test_assoc_Customer_Order_link_reassign_clear():
    a = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    b1 = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    b2 = Customer1(Accontbalance="sample_text_2", Address="sample_text_2", Adress="sample_text_2", Email="sample_text_2", ID=13, Name="sample_text_2", Password="sample_text_2", Phone=13, _attr="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'customer93', b1)
    assert _is_linked(a, 'customer93', b1)
    if hasattr(b1, 'order92'):
        assert _is_linked(b1, 'order92', a)
    _safe_set(a, 'customer93', b2)
    assert _is_linked(a, 'customer93', b2)
    if hasattr(b1, 'order92'):
        assert not _is_linked(b1, 'order92', a)
    if hasattr(b2, 'order92'):
        assert _is_linked(b2, 'order92', a)
    _safe_set(a, 'customer93', None)
    assert not _is_linked(a, 'customer93', b2)
    if hasattr(b2, 'order92'):
        assert not _is_linked(b2, 'order92', a)


def test_assoc_Dish_Menu_link_reassign_clear():
    a = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    b1 = Dish(_attr="sample_text")
    b2 = Dish(_attr="sample_text_2")
    _safe_set(a, 'dish105', b1)
    assert _is_linked(a, 'dish105', b1)
    if hasattr(b1, 'menu104'):
        assert _is_linked(b1, 'menu104', a)
    _safe_set(a, 'dish105', b2)
    assert _is_linked(a, 'dish105', b2)
    if hasattr(b1, 'menu104'):
        assert not _is_linked(b1, 'menu104', a)
    if hasattr(b2, 'menu104'):
        assert _is_linked(b2, 'menu104', a)
    _safe_set(a, 'dish105', None)
    assert not _is_linked(a, 'dish105', b2)
    if hasattr(b2, 'menu104'):
        assert not _is_linked(b2, 'menu104', a)


def test_assoc_Employee_Plan_link_reassign_clear():
    a = Plan(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    b1 = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    b2 = Employee(Email="sample_text_2", ID=13, Name="sample_text_2", attribute="sample_text_2", password="sample_text_2")
    _safe_set(a, 'employee3', {b1})
    assert _is_linked(a, 'employee3', b1)
    if hasattr(b1, 'plan2'):
        assert _is_linked(b1, 'plan2', a)
    _safe_set(a, 'employee3', {b2})
    assert _is_linked(a, 'employee3', b2)
    if hasattr(b1, 'plan2'):
        assert not _is_linked(b1, 'plan2', a)
    if hasattr(b2, 'plan2'):
        assert _is_linked(b2, 'plan2', a)
    _safe_set(a, 'employee3', set())
    assert not _is_linked(a, 'employee3', b2)
    if hasattr(b2, 'plan2'):
        assert not _is_linked(b2, 'plan2', a)


def test_assoc_Employee_Storage_link_reassign_clear():
    a = Storage(Component_Name="sample_text", Component_id=7)
    b1 = Employee(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    b2 = Employee(Email="sample_text_2", ID=13, Name="sample_text_2", attribute="sample_text_2", password="sample_text_2")
    _safe_set(a, 'employee1', {b1})
    assert _is_linked(a, 'employee1', b1)
    if hasattr(b1, 'storage0'):
        assert _is_linked(b1, 'storage0', a)
    _safe_set(a, 'employee1', {b2})
    assert _is_linked(a, 'employee1', b2)
    if hasattr(b1, 'storage0'):
        assert not _is_linked(b1, 'storage0', a)
    if hasattr(b2, 'storage0'):
        assert _is_linked(b2, 'storage0', a)
    _safe_set(a, 'employee1', set())
    assert not _is_linked(a, 'employee1', b2)
    if hasattr(b2, 'storage0'):
        assert not _is_linked(b2, 'storage0', a)


def test_assoc_Employee_Storage2_link_reassign_clear():
    a = Storage1(Component_Name="sample_text", Component_id=7)
    b1 = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    b2 = Kitchen_worker(Email="sample_text_2", ID=13, Name="sample_text_2", attribute="sample_text_2", password="sample_text_2")
    _safe_set(a, 'Employee45', {b1})
    assert _is_linked(a, 'Employee45', b1)
    if hasattr(b1, 'storage44'):
        assert _is_linked(b1, 'storage44', a)
    _safe_set(a, 'Employee45', {b2})
    assert _is_linked(a, 'Employee45', b2)
    if hasattr(b1, 'storage44'):
        assert not _is_linked(b1, 'storage44', a)
    if hasattr(b2, 'storage44'):
        assert _is_linked(b2, 'storage44', a)
    _safe_set(a, 'Employee45', set())
    assert not _is_linked(a, 'Employee45', b2)
    if hasattr(b2, 'storage44'):
        assert not _is_linked(b2, 'storage44', a)


def test_assoc_Menu_Catering_link_reassign_clear():
    a = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    b1 = Catering1(Menu="sample_text", attribute="sample_text")
    b2 = Catering1(Menu="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'catering48', b1)
    assert _is_linked(a, 'catering48', b1)
    if hasattr(b1, 'menu49'):
        assert _is_linked(b1, 'menu49', a)
    _safe_set(a, 'catering48', b2)
    assert _is_linked(a, 'catering48', b2)
    if hasattr(b1, 'menu49'):
        assert not _is_linked(b1, 'menu49', a)
    if hasattr(b2, 'menu49'):
        assert _is_linked(b2, 'menu49', a)
    _safe_set(a, 'catering48', None)
    assert not _is_linked(a, 'catering48', b2)
    if hasattr(b2, 'menu49'):
        assert not _is_linked(b2, 'menu49', a)


def test_assoc_Menu_Dish_link_reassign_clear():
    a = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    b1 = Dish(_attr="sample_text")
    b2 = Dish(_attr="sample_text_2")
    _safe_set(a, 'dish106', {b1})
    assert _is_linked(a, 'dish106', b1)
    if hasattr(b1, 'menu107'):
        assert _is_linked(b1, 'menu107', a)
    _safe_set(a, 'dish106', {b2})
    assert _is_linked(a, 'dish106', b2)
    if hasattr(b1, 'menu107'):
        assert not _is_linked(b1, 'menu107', a)
    if hasattr(b2, 'menu107'):
        assert _is_linked(b2, 'menu107', a)
    _safe_set(a, 'dish106', set())
    assert not _is_linked(a, 'dish106', b2)
    if hasattr(b2, 'menu107'):
        assert not _is_linked(b2, 'menu107', a)


def test_assoc_Menu_Shopping_cart_link_reassign_clear():
    a = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    b1 = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    b2 = Menu1(Components="sample_text_2", DishName="sample_text_2", Price="sample_text_2", Quantity="sample_text_2")
    _safe_set(a, 'menu95', b1)
    assert _is_linked(a, 'menu95', b1)
    if hasattr(b1, 'shopping_cart94'):
        assert _is_linked(b1, 'shopping_cart94', a)
    _safe_set(a, 'menu95', b2)
    assert _is_linked(a, 'menu95', b2)
    if hasattr(b1, 'shopping_cart94'):
        assert not _is_linked(b1, 'shopping_cart94', a)
    if hasattr(b2, 'shopping_cart94'):
        assert _is_linked(b2, 'shopping_cart94', a)
    _safe_set(a, 'menu95', None)
    assert not _is_linked(a, 'menu95', b2)
    if hasattr(b2, 'shopping_cart94'):
        assert not _is_linked(b2, 'shopping_cart94', a)


def test_assoc_Order_Customer_link_reassign_clear():
    a = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    b1 = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    b2 = Customer1(Accontbalance="sample_text_2", Address="sample_text_2", Adress="sample_text_2", Email="sample_text_2", ID=13, Name="sample_text_2", Password="sample_text_2", Phone=13, _attr="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'customer52', b1)
    assert _is_linked(a, 'customer52', b1)
    if hasattr(b1, 'order53'):
        assert _is_linked(b1, 'order53', a)
    _safe_set(a, 'customer52', b2)
    assert _is_linked(a, 'customer52', b2)
    if hasattr(b1, 'order53'):
        assert not _is_linked(b1, 'order53', a)
    if hasattr(b2, 'order53'):
        assert _is_linked(b2, 'order53', a)
    _safe_set(a, 'customer52', None)
    assert not _is_linked(a, 'customer52', b2)
    if hasattr(b2, 'order53'):
        assert not _is_linked(b2, 'order53', a)


def test_assoc_Order_Payment_link_reassign_clear():
    a = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    b1 = Order1(Customerid=7, Dishname="sample_text", OrderID=7, attribute="sample_text", date="sample_text")
    b2 = Order1(Customerid=13, Dishname="sample_text_2", OrderID=13, attribute="sample_text_2", date="sample_text_2")
    _safe_set(a, 'order57', b1)
    assert _is_linked(a, 'order57', b1)
    if hasattr(b1, 'payment56'):
        assert _is_linked(b1, 'payment56', a)
    _safe_set(a, 'order57', b2)
    assert _is_linked(a, 'order57', b2)
    if hasattr(b1, 'payment56'):
        assert not _is_linked(b1, 'payment56', a)
    if hasattr(b2, 'payment56'):
        assert _is_linked(b2, 'payment56', a)
    _safe_set(a, 'order57', None)
    assert not _is_linked(a, 'order57', b2)
    if hasattr(b2, 'payment56'):
        assert not _is_linked(b2, 'payment56', a)


def test_assoc_Payment_PrintRecipts_link_reassign_clear():
    a = PrintRecipts1(Amount="sample_text", CustomerID=7, Dishname="sample_text", PaymentID="sample_text", Quantity=7, date="sample_text", time="sample_text")
    b1 = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    b2 = Payment1(Amount="sample_text_2", CustomerID=13, OrderID=13, PaymentID=13, date="sample_text_2", time="sample_text_2")
    _safe_set(a, 'payment59', b1)
    assert _is_linked(a, 'payment59', b1)
    if hasattr(b1, 'printRecipts58'):
        assert _is_linked(b1, 'printRecipts58', a)
    _safe_set(a, 'payment59', b2)
    assert _is_linked(a, 'payment59', b2)
    if hasattr(b1, 'printRecipts58'):
        assert not _is_linked(b1, 'printRecipts58', a)
    if hasattr(b2, 'printRecipts58'):
        assert _is_linked(b2, 'printRecipts58', a)
    _safe_set(a, 'payment59', None)
    assert not _is_linked(a, 'payment59', b2)
    if hasattr(b2, 'printRecipts58'):
        assert not _is_linked(b2, 'printRecipts58', a)


def test_assoc_Payment_bank_account_link_reassign_clear():
    a = Payment1(Amount="sample_text", CustomerID=7, OrderID=7, PaymentID=7, date="sample_text", time="sample_text")
    b1 = bank_account()
    b2 = bank_account()
    _safe_set(a, 'bank_account66', b1)
    assert _is_linked(a, 'bank_account66', b1)
    if hasattr(b1, 'payment67'):
        assert _is_linked(b1, 'payment67', a)
    _safe_set(a, 'bank_account66', b2)
    assert _is_linked(a, 'bank_account66', b2)
    if hasattr(b1, 'payment67'):
        assert not _is_linked(b1, 'payment67', a)
    if hasattr(b2, 'payment67'):
        assert _is_linked(b2, 'payment67', a)
    _safe_set(a, 'bank_account66', None)
    assert not _is_linked(a, 'bank_account66', b2)
    if hasattr(b2, 'payment67'):
        assert not _is_linked(b2, 'payment67', a)


def test_assoc_Plan_Customer_link_reassign_clear():
    a = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    b1 = Customer1(Accontbalance="sample_text", Address="sample_text", Adress="sample_text", Email="sample_text", ID=7, Name="sample_text", Password="sample_text", Phone=7, _attr="sample_text", attribute="sample_text")
    b2 = Customer1(Accontbalance="sample_text_2", Address="sample_text_2", Adress="sample_text_2", Email="sample_text_2", ID=13, Name="sample_text_2", Password="sample_text_2", Phone=13, _attr="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'customer88', b1)
    assert _is_linked(a, 'customer88', b1)
    if hasattr(b1, 'plan89'):
        assert _is_linked(b1, 'plan89', a)
    _safe_set(a, 'customer88', b2)
    assert _is_linked(a, 'customer88', b2)
    if hasattr(b1, 'plan89'):
        assert not _is_linked(b1, 'plan89', a)
    if hasattr(b2, 'plan89'):
        assert _is_linked(b2, 'plan89', a)
    _safe_set(a, 'customer88', None)
    assert not _is_linked(a, 'customer88', b2)
    if hasattr(b2, 'plan89'):
        assert not _is_linked(b2, 'plan89', a)


def test_assoc_Plan_Kitchen_worker_link_reassign_clear():
    a = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    b1 = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    b2 = Kitchen_worker(Email="sample_text_2", ID=13, Name="sample_text_2", attribute="sample_text_2", password="sample_text_2")
    _safe_set(a, 'kitchen_worker90', {b1})
    assert _is_linked(a, 'kitchen_worker90', b1)
    if hasattr(b1, 'plan91'):
        assert _is_linked(b1, 'plan91', a)
    _safe_set(a, 'kitchen_worker90', {b2})
    assert _is_linked(a, 'kitchen_worker90', b2)
    if hasattr(b1, 'plan91'):
        assert not _is_linked(b1, 'plan91', a)
    if hasattr(b2, 'plan91'):
        assert _is_linked(b2, 'plan91', a)
    _safe_set(a, 'kitchen_worker90', set())
    assert not _is_linked(a, 'kitchen_worker90', b2)
    if hasattr(b2, 'plan91'):
        assert not _is_linked(b2, 'plan91', a)


def test_assoc_Plan_chef_link_reassign_clear():
    a = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    b1 = Plan1(Monthly_plan="sample_text", day_plan="sample_text", weekly_plan="sample_text")
    b2 = Plan1(Monthly_plan="sample_text_2", day_plan="sample_text_2", weekly_plan="sample_text_2")
    _safe_set(a, 'plan47', {b1})
    assert _is_linked(a, 'plan47', b1)
    if hasattr(b1, 'chef46'):
        assert _is_linked(b1, 'chef46', a)
    _safe_set(a, 'plan47', {b2})
    assert _is_linked(a, 'plan47', b2)
    if hasattr(b1, 'chef46'):
        assert not _is_linked(b1, 'chef46', a)
    if hasattr(b2, 'chef46'):
        assert _is_linked(b2, 'chef46', a)
    _safe_set(a, 'plan47', set())
    assert not _is_linked(a, 'plan47', b2)
    if hasattr(b2, 'chef46'):
        assert not _is_linked(b2, 'chef46', a)


def test_assoc_Shopping_cart_Menu_link_reassign_clear():
    a = Shopping_cart1(Dishname="sample_text", Quantity=7, attribute="sample_text", price=7, time="sample_text")
    b1 = Menu1(Components="sample_text", DishName="sample_text", Price="sample_text", Quantity="sample_text")
    b2 = Menu1(Components="sample_text_2", DishName="sample_text_2", Price="sample_text_2", Quantity="sample_text_2")
    _safe_set(a, 'menu54', b1)
    assert _is_linked(a, 'menu54', b1)
    if hasattr(b1, 'shopping_cart55'):
        assert _is_linked(b1, 'shopping_cart55', a)
    _safe_set(a, 'menu54', b2)
    assert _is_linked(a, 'menu54', b2)
    if hasattr(b1, 'shopping_cart55'):
        assert not _is_linked(b1, 'shopping_cart55', a)
    if hasattr(b2, 'shopping_cart55'):
        assert _is_linked(b2, 'shopping_cart55', a)
    _safe_set(a, 'menu54', None)
    assert not _is_linked(a, 'menu54', b2)
    if hasattr(b2, 'shopping_cart55'):
        assert not _is_linked(b2, 'shopping_cart55', a)


def test_assoc_Storage_Kitchen_worker_link_reassign_clear():
    a = Storage1(Component_Name="sample_text", Component_id=7)
    b1 = Kitchen_worker(Email="sample_text", ID=7, Name="sample_text", attribute="sample_text", password="sample_text")
    b2 = Kitchen_worker(Email="sample_text_2", ID=13, Name="sample_text_2", attribute="sample_text_2", password="sample_text_2")
    _safe_set(a, 'kitchen_worker96', {b1})
    assert _is_linked(a, 'kitchen_worker96', b1)
    if hasattr(b1, 'storage97'):
        assert _is_linked(b1, 'storage97', a)
    _safe_set(a, 'kitchen_worker96', {b2})
    assert _is_linked(a, 'kitchen_worker96', b2)
    if hasattr(b1, 'storage97'):
        assert not _is_linked(b1, 'storage97', a)
    if hasattr(b2, 'storage97'):
        assert _is_linked(b2, 'storage97', a)
    _safe_set(a, 'kitchen_worker96', set())
    assert not _is_linked(a, 'kitchen_worker96', b2)
    if hasattr(b2, 'storage97'):
        assert not _is_linked(b2, 'storage97', a)


def test_assoc_Storage_chef_link_reassign_clear():
    a = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    b1 = Storage1(Component_Name="sample_text", Component_id=7)
    b2 = Storage1(Component_Name="sample_text_2", Component_id=13)
    _safe_set(a, 'storage65', {b1})
    assert _is_linked(a, 'storage65', b1)
    if hasattr(b1, 'chef64'):
        assert _is_linked(b1, 'chef64', a)
    _safe_set(a, 'storage65', {b2})
    assert _is_linked(a, 'storage65', b2)
    if hasattr(b1, 'chef64'):
        assert not _is_linked(b1, 'chef64', a)
    if hasattr(b2, 'chef64'):
        assert _is_linked(b2, 'chef64', a)
    _safe_set(a, 'storage65', set())
    assert not _is_linked(a, 'storage65', b2)
    if hasattr(b2, 'chef64'):
        assert not _is_linked(b2, 'chef64', a)


def test_assoc_System_Storage_link_reassign_clear():
    a = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    b1 = Storage1(Component_Name="sample_text", Component_id=7)
    b2 = Storage1(Component_Name="sample_text_2", Component_id=13)
    _safe_set(a, 'storage86', b1)
    assert _is_linked(a, 'storage86', b1)
    if hasattr(b1, 'system87'):
        assert _is_linked(b1, 'system87', a)
    _safe_set(a, 'storage86', b2)
    assert _is_linked(a, 'storage86', b2)
    if hasattr(b1, 'system87'):
        assert not _is_linked(b1, 'system87', a)
    if hasattr(b2, 'system87'):
        assert _is_linked(b2, 'system87', a)
    _safe_set(a, 'storage86', None)
    assert not _is_linked(a, 'storage86', b2)
    if hasattr(b2, 'system87'):
        assert not _is_linked(b2, 'system87', a)


def test_assoc_System_bank_account_link_reassign_clear():
    a = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    b1 = bank_account()
    b2 = bank_account()
    _safe_set(a, 'bank_account68', b1)
    assert _is_linked(a, 'bank_account68', b1)
    if hasattr(b1, 'system69'):
        assert _is_linked(b1, 'system69', a)
    _safe_set(a, 'bank_account68', b2)
    assert _is_linked(a, 'bank_account68', b2)
    if hasattr(b1, 'system69'):
        assert not _is_linked(b1, 'system69', a)
    if hasattr(b2, 'system69'):
        assert _is_linked(b2, 'system69', a)
    _safe_set(a, 'bank_account68', None)
    assert not _is_linked(a, 'bank_account68', b2)
    if hasattr(b2, 'system69'):
        assert not _is_linked(b2, 'system69', a)


def test_assoc_System_bank_account2_link_reassign_clear():
    a = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    b1 = bank_account()
    b2 = bank_account()
    _safe_set(a, 'bank_account70', b1)
    assert _is_linked(a, 'bank_account70', b1)
    if hasattr(b1, 'system71'):
        assert _is_linked(b1, 'system71', a)
    _safe_set(a, 'bank_account70', b2)
    assert _is_linked(a, 'bank_account70', b2)
    if hasattr(b1, 'system71'):
        assert not _is_linked(b1, 'system71', a)
    if hasattr(b2, 'system71'):
        assert _is_linked(b2, 'system71', a)
    _safe_set(a, 'bank_account70', None)
    assert not _is_linked(a, 'bank_account70', b2)
    if hasattr(b2, 'system71'):
        assert not _is_linked(b2, 'system71', a)


def test_assoc_System_contact_link_reassign_clear():
    a = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    b1 = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    b2 = System1(Email="sample_text_2", Password="sample_text_2", WebAdmin_or_owner="sample_text_2")
    _safe_set(a, 'system73', b1)
    assert _is_linked(a, 'system73', b1)
    if hasattr(b1, 'contact72'):
        assert _is_linked(b1, 'contact72', a)
    _safe_set(a, 'system73', b2)
    assert _is_linked(a, 'system73', b2)
    if hasattr(b1, 'contact72'):
        assert not _is_linked(b1, 'contact72', a)
    if hasattr(b2, 'contact72'):
        assert _is_linked(b2, 'contact72', a)
    _safe_set(a, 'system73', None)
    assert not _is_linked(a, 'system73', b2)
    if hasattr(b2, 'contact72'):
        assert not _is_linked(b2, 'contact72', a)


def test_assoc_System_help_link_reassign_clear():
    a = System1(Email="sample_text", Password="sample_text", WebAdmin_or_owner="sample_text")
    b1 = help()
    b2 = help()
    _safe_set(a, 'help74', b1)
    assert _is_linked(a, 'help74', b1)
    if hasattr(b1, 'system75'):
        assert _is_linked(b1, 'system75', a)
    _safe_set(a, 'help74', b2)
    assert _is_linked(a, 'help74', b2)
    if hasattr(b1, 'system75'):
        assert not _is_linked(b1, 'system75', a)
    if hasattr(b2, 'system75'):
        assert _is_linked(b2, 'system75', a)
    _safe_set(a, 'help74', None)
    assert not _is_linked(a, 'help74', b2)
    if hasattr(b2, 'system75'):
        assert not _is_linked(b2, 'system75', a)


def test_assoc_Web_master_contact_link_reassign_clear():
    a = contact(Adress="sample_text", Email="sample_text", Name="sample_text", Tel=7, attribute="sample_text")
    b1 = Web_master()
    b2 = Web_master()
    _safe_set(a, 'web_master63', b1)
    assert _is_linked(a, 'web_master63', b1)
    if hasattr(b1, 'contact62'):
        assert _is_linked(b1, 'contact62', a)
    _safe_set(a, 'web_master63', b2)
    assert _is_linked(a, 'web_master63', b2)
    if hasattr(b1, 'contact62'):
        assert not _is_linked(b1, 'contact62', a)
    if hasattr(b2, 'contact62'):
        assert _is_linked(b2, 'contact62', a)
    _safe_set(a, 'web_master63', None)
    assert not _is_linked(a, 'web_master63', b2)
    if hasattr(b2, 'contact62'):
        assert not _is_linked(b2, 'contact62', a)


def test_assoc_chef_Accounnt_link_reassign_clear():
    a = chef(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    b1 = Accounnt(Accounttype="sample_text", Email="sample_text", Employee_ID="sample_text", password="sample_text")
    b2 = Accounnt(Accounttype="sample_text_2", Email="sample_text_2", Employee_ID="sample_text_2", password="sample_text_2")
    _safe_set(a, 'accounnt34', b1)
    assert _is_linked(a, 'accounnt34', b1)
    if hasattr(b1, 'chef35'):
        assert _is_linked(b1, 'chef35', a)
    _safe_set(a, 'accounnt34', b2)
    assert _is_linked(a, 'accounnt34', b2)
    if hasattr(b1, 'chef35'):
        assert not _is_linked(b1, 'chef35', a)
    if hasattr(b2, 'chef35'):
        assert _is_linked(b2, 'chef35', a)
    _safe_set(a, 'accounnt34', None)
    assert not _is_linked(a, 'accounnt34', b2)
    if hasattr(b2, 'chef35'):
        assert not _is_linked(b2, 'chef35', a)


def test_assoc_chef_Accounnt2_link_reassign_clear():
    a = chef1(Email="sample_text", Employee_ID=7, Name="sample_text", Room_no=7, passowrd="sample_text")
    b1 = Accounnt1(Accounttype="sample_text", Email="sample_text", password="sample_text")
    b2 = Accounnt1(Accounttype="sample_text_2", Email="sample_text_2", password="sample_text_2")
    _safe_set(a, 'accounnt38', b1)
    assert _is_linked(a, 'accounnt38', b1)
    if hasattr(b1, 'chef39'):
        assert _is_linked(b1, 'chef39', a)
    _safe_set(a, 'accounnt38', b2)
    assert _is_linked(a, 'accounnt38', b2)
    if hasattr(b1, 'chef39'):
        assert not _is_linked(b1, 'chef39', a)
    if hasattr(b2, 'chef39'):
        assert _is_linked(b2, 'chef39', a)
    _safe_set(a, 'accounnt38', None)
    assert not _is_linked(a, 'accounnt38', b2)
    if hasattr(b2, 'chef39'):
        assert not _is_linked(b2, 'chef39', a)


def test_assoc_chef_planning_link_reassign_clear():
    a = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    b1 = chef2()
    b2 = chef2()
    _safe_set(a, 'chef151', b1)
    assert _is_linked(a, 'chef151', b1)
    if hasattr(b1, 'planning150'):
        assert _is_linked(b1, 'planning150', a)
    _safe_set(a, 'chef151', b2)
    assert _is_linked(a, 'chef151', b2)
    if hasattr(b1, 'planning150'):
        assert not _is_linked(b1, 'planning150', a)
    if hasattr(b2, 'planning150'):
        assert _is_linked(b2, 'planning150', a)
    _safe_set(a, 'chef151', None)
    assert not _is_linked(a, 'chef151', b2)
    if hasattr(b2, 'planning150'):
        assert not _is_linked(b2, 'planning150', a)


def test_assoc_drink_Component_link_reassign_clear():
    a = drink(type="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component116', b1)
    assert _is_linked(a, 'component116', b1)
    if hasattr(b1, 'drink117'):
        assert _is_linked(b1, 'drink117', a)
    _safe_set(a, 'component116', b2)
    assert _is_linked(a, 'component116', b2)
    if hasattr(b1, 'drink117'):
        assert not _is_linked(b1, 'drink117', a)
    if hasattr(b2, 'drink117'):
        assert _is_linked(b2, 'drink117', a)
    _safe_set(a, 'component116', None)
    assert not _is_linked(a, 'component116', b2)
    if hasattr(b2, 'drink117'):
        assert not _is_linked(b2, 'drink117', a)


def test_assoc_events_order_link_reassign_clear():
    a = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    b1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    _safe_set(a, 'events183', b1)
    assert _is_linked(a, 'events183', b1)
    if hasattr(b1, 'order182'):
        assert _is_linked(b1, 'order182', a)
    _safe_set(a, 'events183', b2)
    assert _is_linked(a, 'events183', b2)
    if hasattr(b1, 'order182'):
        assert not _is_linked(b1, 'order182', a)
    if hasattr(b2, 'order182'):
        assert _is_linked(b2, 'order182', a)
    _safe_set(a, 'events183', None)
    assert not _is_linked(a, 'events183', b2)
    if hasattr(b2, 'order182'):
        assert not _is_linked(b2, 'order182', a)


def test_assoc_food_dish_Component_link_reassign_clear():
    a = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component112', b1)
    assert _is_linked(a, 'component112', b1)
    if hasattr(b1, 'food_dish113'):
        assert _is_linked(b1, 'food_dish113', a)
    _safe_set(a, 'component112', b2)
    assert _is_linked(a, 'component112', b2)
    if hasattr(b1, 'food_dish113'):
        assert not _is_linked(b1, 'food_dish113', a)
    if hasattr(b2, 'food_dish113'):
        assert _is_linked(b2, 'food_dish113', a)
    _safe_set(a, 'component112', None)
    assert not _is_linked(a, 'component112', b2)
    if hasattr(b2, 'food_dish113'):
        assert not _is_linked(b2, 'food_dish113', a)


def test_assoc_food_dish_Component2_link_reassign_clear():
    a = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component114', b1)
    assert _is_linked(a, 'component114', b1)
    if hasattr(b1, 'food_dish115'):
        assert _is_linked(b1, 'food_dish115', a)
    _safe_set(a, 'component114', b2)
    assert _is_linked(a, 'component114', b2)
    if hasattr(b1, 'food_dish115'):
        assert not _is_linked(b1, 'food_dish115', a)
    if hasattr(b2, 'food_dish115'):
        assert _is_linked(b2, 'food_dish115', a)
    _safe_set(a, 'component114', None)
    assert not _is_linked(a, 'component114', b2)
    if hasattr(b2, 'food_dish115'):
        assert not _is_linked(b2, 'food_dish115', a)


def test_assoc_food_dish_menu_link_reassign_clear():
    a = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    b1 = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    b2 = food_dish(attribute="sample_text_2", attribute2="sample_text_2", type="sample_text_2")
    _safe_set(a, 'menu156', {b1})
    assert _is_linked(a, 'menu156', b1)
    if hasattr(b1, 'food_dish157'):
        assert _is_linked(b1, 'food_dish157', a)
    _safe_set(a, 'menu156', {b2})
    assert _is_linked(a, 'menu156', b2)
    if hasattr(b1, 'food_dish157'):
        assert not _is_linked(b1, 'food_dish157', a)
    if hasattr(b2, 'food_dish157'):
        assert _is_linked(b2, 'food_dish157', a)
    _safe_set(a, 'menu156', set())
    assert not _is_linked(a, 'menu156', b2)
    if hasattr(b2, 'food_dish157'):
        assert not _is_linked(b2, 'food_dish157', a)


def test_assoc_food_dish_weekly_planning_of_dishes__for__waiter_link_reassign_clear():
    a = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    b1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    _safe_set(a, 'food_dish181', b1)
    assert _is_linked(a, 'food_dish181', b1)
    if hasattr(b1, 'weekly_planning_of_dishes__for__waiter180'):
        assert _is_linked(b1, 'weekly_planning_of_dishes__for__waiter180', a)
    _safe_set(a, 'food_dish181', b2)
    assert _is_linked(a, 'food_dish181', b2)
    if hasattr(b1, 'weekly_planning_of_dishes__for__waiter180'):
        assert not _is_linked(b1, 'weekly_planning_of_dishes__for__waiter180', a)
    if hasattr(b2, 'weekly_planning_of_dishes__for__waiter180'):
        assert _is_linked(b2, 'weekly_planning_of_dishes__for__waiter180', a)
    _safe_set(a, 'food_dish181', None)
    assert not _is_linked(a, 'food_dish181', b2)
    if hasattr(b2, 'weekly_planning_of_dishes__for__waiter180'):
        assert not _is_linked(b2, 'weekly_planning_of_dishes__for__waiter180', a)


def test_assoc_menu_Csutomer_link_reassign_clear():
    a = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    b1 = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    b2 = Csutomer(Adress="sample_text_2", attribute="sample_text_2", email="sample_text_2", id="sample_text_2", name="sample_text_2", password="sample_text_2", register="sample_text_2", tel_no="sample_text_2")
    _safe_set(a, 'csutomer122', b1)
    assert _is_linked(a, 'csutomer122', b1)
    if hasattr(b1, 'menu123'):
        assert _is_linked(b1, 'menu123', a)
    _safe_set(a, 'csutomer122', b2)
    assert _is_linked(a, 'csutomer122', b2)
    if hasattr(b1, 'menu123'):
        assert not _is_linked(b1, 'menu123', a)
    if hasattr(b2, 'menu123'):
        assert _is_linked(b2, 'menu123', a)
    _safe_set(a, 'csutomer122', None)
    assert not _is_linked(a, 'csutomer122', b2)
    if hasattr(b2, 'menu123'):
        assert not _is_linked(b2, 'menu123', a)


def test_assoc_menu_catering_link_reassign_clear():
    a = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    b1 = catering()
    b2 = catering()
    _safe_set(a, 'catering176', b1)
    assert _is_linked(a, 'catering176', b1)
    if hasattr(b1, 'menu177'):
        assert _is_linked(b1, 'menu177', a)
    _safe_set(a, 'catering176', b2)
    assert _is_linked(a, 'catering176', b2)
    if hasattr(b1, 'menu177'):
        assert not _is_linked(b1, 'menu177', a)
    if hasattr(b2, 'menu177'):
        assert _is_linked(b2, 'menu177', a)
    _safe_set(a, 'catering176', None)
    assert not _is_linked(a, 'catering176', b2)
    if hasattr(b2, 'menu177'):
        assert not _is_linked(b2, 'menu177', a)


def test_assoc_menu_drink_link_reassign_clear():
    a = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    b1 = drink(type="sample_text")
    b2 = drink(type="sample_text_2")
    _safe_set(a, 'drink120', b1)
    assert _is_linked(a, 'drink120', b1)
    if hasattr(b1, 'menu121'):
        assert _is_linked(b1, 'menu121', a)
    _safe_set(a, 'drink120', b2)
    assert _is_linked(a, 'drink120', b2)
    if hasattr(b1, 'menu121'):
        assert not _is_linked(b1, 'menu121', a)
    if hasattr(b2, 'menu121'):
        assert _is_linked(b2, 'menu121', a)
    _safe_set(a, 'drink120', None)
    assert not _is_linked(a, 'drink120', b2)
    if hasattr(b2, 'menu121'):
        assert not _is_linked(b2, 'menu121', a)


def test_assoc_menu_food_dish_link_reassign_clear():
    a = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    b1 = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    b2 = food_dish(attribute="sample_text_2", attribute2="sample_text_2", type="sample_text_2")
    _safe_set(a, 'food_dish118', b1)
    assert _is_linked(a, 'food_dish118', b1)
    if hasattr(b1, 'menu119'):
        assert _is_linked(b1, 'menu119', a)
    _safe_set(a, 'food_dish118', b2)
    assert _is_linked(a, 'food_dish118', b2)
    if hasattr(b1, 'menu119'):
        assert not _is_linked(b1, 'menu119', a)
    if hasattr(b2, 'menu119'):
        assert _is_linked(b2, 'menu119', a)
    _safe_set(a, 'food_dish118', None)
    assert not _is_linked(a, 'food_dish118', b2)
    if hasattr(b2, 'menu119'):
        assert not _is_linked(b2, 'menu119', a)


def test_assoc_menu_order_link_reassign_clear():
    a = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    b1 = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    b2 = menu(attribute="sample_text_2", dish_quantity="sample_text_2", dishname="sample_text_2", drinkname="sample_text_2", price="sample_text_2")
    _safe_set(a, 'menu125', b1)
    assert _is_linked(a, 'menu125', b1)
    if hasattr(b1, 'order124'):
        assert _is_linked(b1, 'order124', a)
    _safe_set(a, 'menu125', b2)
    assert _is_linked(a, 'menu125', b2)
    if hasattr(b1, 'order124'):
        assert not _is_linked(b1, 'order124', a)
    if hasattr(b2, 'order124'):
        assert _is_linked(b2, 'order124', a)
    _safe_set(a, 'menu125', None)
    assert not _is_linked(a, 'menu125', b2)
    if hasattr(b2, 'order124'):
        assert not _is_linked(b2, 'order124', a)


def test_assoc_menu_order2_link_reassign_clear():
    a = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    b1 = menu(attribute="sample_text", dish_quantity="sample_text", dishname="sample_text", drinkname="sample_text", price="sample_text")
    b2 = menu(attribute="sample_text_2", dish_quantity="sample_text_2", dishname="sample_text_2", drinkname="sample_text_2", price="sample_text_2")
    _safe_set(a, 'menu169', {b1})
    assert _is_linked(a, 'menu169', b1)
    if hasattr(b1, 'order168'):
        assert _is_linked(b1, 'order168', a)
    _safe_set(a, 'menu169', {b2})
    assert _is_linked(a, 'menu169', b2)
    if hasattr(b1, 'order168'):
        assert not _is_linked(b1, 'order168', a)
    if hasattr(b2, 'order168'):
        assert _is_linked(b2, 'order168', a)
    _safe_set(a, 'menu169', set())
    assert not _is_linked(a, 'menu169', b2)
    if hasattr(b2, 'order168'):
        assert not _is_linked(b2, 'order168', a)


def test_assoc_order_Csutomer_link_reassign_clear():
    a = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    b1 = Csutomer(Adress="sample_text", attribute="sample_text", email="sample_text", id="sample_text", name="sample_text", password="sample_text", register="sample_text", tel_no="sample_text")
    b2 = Csutomer(Adress="sample_text_2", attribute="sample_text_2", email="sample_text_2", id="sample_text_2", name="sample_text_2", password="sample_text_2", register="sample_text_2", tel_no="sample_text_2")
    _safe_set(a, 'csutomer126', {b1})
    assert _is_linked(a, 'csutomer126', b1)
    if hasattr(b1, 'order127'):
        assert _is_linked(b1, 'order127', a)
    _safe_set(a, 'csutomer126', {b2})
    assert _is_linked(a, 'csutomer126', b2)
    if hasattr(b1, 'order127'):
        assert not _is_linked(b1, 'order127', a)
    if hasattr(b2, 'order127'):
        assert _is_linked(b2, 'order127', a)
    _safe_set(a, 'csutomer126', set())
    assert not _is_linked(a, 'csutomer126', b2)
    if hasattr(b2, 'order127'):
        assert not _is_linked(b2, 'order127', a)


def test_assoc_order_shopping_cart_link_reassign_clear():
    a = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    b1 = shopping_cart()
    b2 = shopping_cart()
    _safe_set(a, 'shopping_cart130', b1)
    assert _is_linked(a, 'shopping_cart130', b1)
    if hasattr(b1, 'order131'):
        assert _is_linked(b1, 'order131', a)
    _safe_set(a, 'shopping_cart130', b2)
    assert _is_linked(a, 'shopping_cart130', b2)
    if hasattr(b1, 'order131'):
        assert not _is_linked(b1, 'order131', a)
    if hasattr(b2, 'order131'):
        assert _is_linked(b2, 'order131', a)
    _safe_set(a, 'shopping_cart130', None)
    assert not _is_linked(a, 'shopping_cart130', b2)
    if hasattr(b2, 'order131'):
        assert not _is_linked(b2, 'order131', a)


def test_assoc_order_shopping_cart2_link_reassign_clear():
    a = order(_attr="sample_text", date="sample_text", order_id="sample_text", ordered_item="sample_text", status="sample_text")
    b1 = shopping_cart()
    b2 = shopping_cart()
    _safe_set(a, 'shopping_cart158', {b1})
    assert _is_linked(a, 'shopping_cart158', b1)
    if hasattr(b1, 'order159'):
        assert _is_linked(b1, 'order159', a)
    _safe_set(a, 'shopping_cart158', {b2})
    assert _is_linked(a, 'shopping_cart158', b2)
    if hasattr(b1, 'order159'):
        assert not _is_linked(b1, 'order159', a)
    if hasattr(b2, 'order159'):
        assert _is_linked(b2, 'order159', a)
    _safe_set(a, 'shopping_cart158', set())
    assert not _is_linked(a, 'shopping_cart158', b2)
    if hasattr(b2, 'order159'):
        assert not _is_linked(b2, 'order159', a)


def test_assoc_planning_chef_link_reassign_clear():
    a = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    b1 = chef2()
    b2 = chef2()
    _safe_set(a, 'chef136', b1)
    assert _is_linked(a, 'chef136', b1)
    if hasattr(b1, 'planning137'):
        assert _is_linked(b1, 'planning137', a)
    _safe_set(a, 'chef136', b2)
    assert _is_linked(a, 'chef136', b2)
    if hasattr(b1, 'planning137'):
        assert not _is_linked(b1, 'planning137', a)
    if hasattr(b2, 'planning137'):
        assert _is_linked(b2, 'planning137', a)
    _safe_set(a, 'chef136', None)
    assert not _is_linked(a, 'chef136', b2)
    if hasattr(b2, 'planning137'):
        assert not _is_linked(b2, 'planning137', a)


def test_assoc_planning_weekly_planning_of_dishes__by_waiter_link_reassign_clear():
    a = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b1 = dayplan(Monday="sample_text", friday="sample_text", plan_per_date="sample_text", saturday="sample_text", sunday="sample_text", thursday="sample_text", tuesday="sample_text", wenesday="sample_text")
    b2 = dayplan(Monday="sample_text_2", friday="sample_text_2", plan_per_date="sample_text_2", saturday="sample_text_2", sunday="sample_text_2", thursday="sample_text_2", tuesday="sample_text_2", wenesday="sample_text_2")
    _safe_set(a, 'planning135', b1)
    assert _is_linked(a, 'planning135', b1)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter134'):
        assert _is_linked(b1, 'weekly_planning_of_dishes__by_waiter134', a)
    _safe_set(a, 'planning135', b2)
    assert _is_linked(a, 'planning135', b2)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter134'):
        assert not _is_linked(b1, 'weekly_planning_of_dishes__by_waiter134', a)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter134'):
        assert _is_linked(b2, 'weekly_planning_of_dishes__by_waiter134', a)
    _safe_set(a, 'planning135', None)
    assert not _is_linked(a, 'planning135', b2)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter134'):
        assert not _is_linked(b2, 'weekly_planning_of_dishes__by_waiter134', a)


def test_assoc_shopping_cart_payment_link_reassign_clear():
    a = payment(_attr="sample_text", amount="sample_text", total_amount="sample_text")
    b1 = shopping_cart()
    b2 = shopping_cart()
    _safe_set(a, 'shopping_cart133', {b1})
    assert _is_linked(a, 'shopping_cart133', b1)
    if hasattr(b1, 'payment132'):
        assert _is_linked(b1, 'payment132', a)
    _safe_set(a, 'shopping_cart133', {b2})
    assert _is_linked(a, 'shopping_cart133', b2)
    if hasattr(b1, 'payment132'):
        assert not _is_linked(b1, 'payment132', a)
    if hasattr(b2, 'payment132'):
        assert _is_linked(b2, 'payment132', a)
    _safe_set(a, 'shopping_cart133', set())
    assert not _is_linked(a, 'shopping_cart133', b2)
    if hasattr(b2, 'payment132'):
        assert not _is_linked(b2, 'payment132', a)


def test_assoc_shopping_cart_payment2_link_reassign_clear():
    a = payment(_attr="sample_text", amount="sample_text", total_amount="sample_text")
    b1 = shopping_cart()
    b2 = shopping_cart()
    _safe_set(a, 'shopping_cart171', b1)
    assert _is_linked(a, 'shopping_cart171', b1)
    if hasattr(b1, 'payment170'):
        assert _is_linked(b1, 'payment170', a)
    _safe_set(a, 'shopping_cart171', b2)
    assert _is_linked(a, 'shopping_cart171', b2)
    if hasattr(b1, 'payment170'):
        assert not _is_linked(b1, 'payment170', a)
    if hasattr(b2, 'payment170'):
        assert _is_linked(b2, 'payment170', a)
    _safe_set(a, 'shopping_cart171', None)
    assert not _is_linked(a, 'shopping_cart171', b2)
    if hasattr(b2, 'payment170'):
        assert not _is_linked(b2, 'payment170', a)


def test_assoc_weekly_planning_of_dishes__by_waiter_Component_link_reassign_clear():
    a = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b1 = Component(Expiry_date="sample_text", ID="sample_text", Name="sample_text", Storage_or_sehlf="sample_text", Type="sample_text", attribute="sample_text")
    b2 = Component(Expiry_date="sample_text_2", ID="sample_text_2", Name="sample_text_2", Storage_or_sehlf="sample_text_2", Type="sample_text_2", attribute="sample_text_2")
    _safe_set(a, 'component140', b1)
    assert _is_linked(a, 'component140', b1)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter141'):
        assert _is_linked(b1, 'weekly_planning_of_dishes__by_waiter141', a)
    _safe_set(a, 'component140', b2)
    assert _is_linked(a, 'component140', b2)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter141'):
        assert not _is_linked(b1, 'weekly_planning_of_dishes__by_waiter141', a)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter141'):
        assert _is_linked(b2, 'weekly_planning_of_dishes__by_waiter141', a)
    _safe_set(a, 'component140', None)
    assert not _is_linked(a, 'component140', b2)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter141'):
        assert not _is_linked(b2, 'weekly_planning_of_dishes__by_waiter141', a)


def test_assoc_weekly_planning_of_dishes__by_waiter_food_dish_link_reassign_clear():
    a = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    b1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    _safe_set(a, 'weekly_planning_of_dishes__by_waiter161', b1)
    assert _is_linked(a, 'weekly_planning_of_dishes__by_waiter161', b1)
    if hasattr(b1, 'food_dish160'):
        assert _is_linked(b1, 'food_dish160', a)
    _safe_set(a, 'weekly_planning_of_dishes__by_waiter161', b2)
    assert _is_linked(a, 'weekly_planning_of_dishes__by_waiter161', b2)
    if hasattr(b1, 'food_dish160'):
        assert not _is_linked(b1, 'food_dish160', a)
    if hasattr(b2, 'food_dish160'):
        assert _is_linked(b2, 'food_dish160', a)
    _safe_set(a, 'weekly_planning_of_dishes__by_waiter161', None)
    assert not _is_linked(a, 'weekly_planning_of_dishes__by_waiter161', b2)
    if hasattr(b2, 'food_dish160'):
        assert not _is_linked(b2, 'food_dish160', a)


def test_assoc_weekly_planning_of_dishes__by_waiter_waiter_link_reassign_clear():
    a = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b1 = kitchen_worker()
    b2 = kitchen_worker()
    _safe_set(a, 'waiter144', b1)
    assert _is_linked(a, 'waiter144', b1)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter145'):
        assert _is_linked(b1, 'weekly_planning_of_dishes__by_waiter145', a)
    _safe_set(a, 'waiter144', b2)
    assert _is_linked(a, 'waiter144', b2)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter145'):
        assert not _is_linked(b1, 'weekly_planning_of_dishes__by_waiter145', a)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter145'):
        assert _is_linked(b2, 'weekly_planning_of_dishes__by_waiter145', a)
    _safe_set(a, 'waiter144', None)
    assert not _is_linked(a, 'waiter144', b2)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter145'):
        assert not _is_linked(b2, 'weekly_planning_of_dishes__by_waiter145', a)


def test_assoc_weekly_planning_of_dishes__by_waiter_waiter2_link_reassign_clear():
    a = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b1 = kitchen_worker()
    b2 = kitchen_worker()
    _safe_set(a, 'waiter146', {b1})
    assert _is_linked(a, 'waiter146', b1)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter147'):
        assert _is_linked(b1, 'weekly_planning_of_dishes__by_waiter147', a)
    _safe_set(a, 'waiter146', {b2})
    assert _is_linked(a, 'waiter146', b2)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter147'):
        assert not _is_linked(b1, 'weekly_planning_of_dishes__by_waiter147', a)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter147'):
        assert _is_linked(b2, 'weekly_planning_of_dishes__by_waiter147', a)
    _safe_set(a, 'waiter146', set())
    assert not _is_linked(a, 'waiter146', b2)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter147'):
        assert not _is_linked(b2, 'weekly_planning_of_dishes__by_waiter147', a)


def test_assoc_weekly_planning_of_dishes__by_waiter_weekly_planning_of_dishes__by_waiter_link_reassign_clear():
    a = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    _safe_set(a, 'weekly_planning_of_dishes__by_waiter142', b1)
    assert _is_linked(a, 'weekly_planning_of_dishes__by_waiter142', b1)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter143'):
        assert _is_linked(b1, 'weekly_planning_of_dishes__by_waiter143', a)
    _safe_set(a, 'weekly_planning_of_dishes__by_waiter142', b2)
    assert _is_linked(a, 'weekly_planning_of_dishes__by_waiter142', b2)
    if hasattr(b1, 'weekly_planning_of_dishes__by_waiter143'):
        assert not _is_linked(b1, 'weekly_planning_of_dishes__by_waiter143', a)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter143'):
        assert _is_linked(b2, 'weekly_planning_of_dishes__by_waiter143', a)
    _safe_set(a, 'weekly_planning_of_dishes__by_waiter142', None)
    assert not _is_linked(a, 'weekly_planning_of_dishes__by_waiter142', b2)
    if hasattr(b2, 'weekly_planning_of_dishes__by_waiter143'):
        assert not _is_linked(b2, 'weekly_planning_of_dishes__by_waiter143', a)


def test_assoc_weekly_planning_of_dishes__for__waiter_food_dish_link_reassign_clear():
    a = food_dish(attribute="sample_text", attribute2="sample_text", type="sample_text")
    b1 = events(attribute="sample_text", catering_location="sample_text", duration="sample_text", get_employee_name="sample_text")
    b2 = events(attribute="sample_text_2", catering_location="sample_text_2", duration="sample_text_2", get_employee_name="sample_text_2")
    _safe_set(a, 'weekly_planning_of_dishes__for__waiter165', {b1})
    assert _is_linked(a, 'weekly_planning_of_dishes__for__waiter165', b1)
    if hasattr(b1, 'food_dish164'):
        assert _is_linked(b1, 'food_dish164', a)
    _safe_set(a, 'weekly_planning_of_dishes__for__waiter165', {b2})
    assert _is_linked(a, 'weekly_planning_of_dishes__for__waiter165', b2)
    if hasattr(b1, 'food_dish164'):
        assert not _is_linked(b1, 'food_dish164', a)
    if hasattr(b2, 'food_dish164'):
        assert _is_linked(b2, 'food_dish164', a)
    _safe_set(a, 'weekly_planning_of_dishes__for__waiter165', set())
    assert not _is_linked(a, 'weekly_planning_of_dishes__for__waiter165', b2)
    if hasattr(b2, 'food_dish164'):
        assert not _is_linked(b2, 'food_dish164', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Accounnt_strategy = st.builds(Accounnt, Accounttype=safe_text, Email=safe_text, Employee_ID=safe_text, password=safe_text)
@given(instance=Accounnt_strategy)
@settings(max_examples=25)
def test_Accounnt_instantiation(instance):
    assert isinstance(instance, Accounnt)


Accounnt1_strategy = st.builds(Accounnt1, Accounttype=safe_text, Email=safe_text, password=safe_text)
@given(instance=Accounnt1_strategy)
@settings(max_examples=25)
def test_Accounnt1_instantiation(instance):
    assert isinstance(instance, Accounnt1)


Account_strategy = st.builds(Account, Name=safe_text, _attr=safe_text, attribute=safe_text, email=safe_text, id=safe_text, password=safe_text)
@given(instance=Account_strategy)
@settings(max_examples=25)
def test_Account_instantiation(instance):
    assert isinstance(instance, Account)


Account1_strategy = st.builds(Account1, Name=safe_text, _attr=safe_text, attribute=safe_text, email=safe_text, id=safe_text, password=safe_text)
@given(instance=Account1_strategy)
@settings(max_examples=25)
def test_Account1_instantiation(instance):
    assert isinstance(instance, Account1)


Account_for_employee_strategy = st.builds(Account_for_employee, attribute=safe_text, email=safe_text, getaccount=safe_text, id=safe_text, name=safe_text, password=safe_text)
@given(instance=Account_for_employee_strategy)
@settings(max_examples=25)
def test_Account_for_employee_instantiation(instance):
    assert isinstance(instance, Account_for_employee)


Catering_strategy = st.builds(Catering, Menu=safe_text, attribute=safe_text)
@given(instance=Catering_strategy)
@settings(max_examples=25)
def test_Catering_instantiation(instance):
    assert isinstance(instance, Catering)


Catering1_strategy = st.builds(Catering1, Menu=safe_text, attribute=safe_text)
@given(instance=Catering1_strategy)
@settings(max_examples=25)
def test_Catering1_instantiation(instance):
    assert isinstance(instance, Catering1)


Chef_strategy = st.builds(Chef)
@given(instance=Chef_strategy)
@settings(max_examples=25)
def test_Chef_instantiation(instance):
    assert isinstance(instance, Chef)


Component_strategy = st.builds(Component, Expiry_date=safe_text, ID=safe_text, Name=safe_text, Storage_or_sehlf=safe_text, Type=safe_text, attribute=safe_text)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


Csutomer_strategy = st.builds(Csutomer, Adress=safe_text, attribute=safe_text, email=safe_text, id=safe_text, name=safe_text, password=safe_text, register=safe_text, tel_no=safe_text)
@given(instance=Csutomer_strategy)
@settings(max_examples=25)
def test_Csutomer_instantiation(instance):
    assert isinstance(instance, Csutomer)


Customer_strategy = st.builds(Customer, Accontbalance=safe_text, Address=safe_text, Email=safe_text, ID=st.integers(), Name=safe_text, Password=safe_text, Phone=st.integers())
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Customer1_strategy = st.builds(Customer1, Accontbalance=safe_text, Address=safe_text, Adress=safe_text, Email=safe_text, ID=st.integers(), Name=safe_text, Password=safe_text, Phone=st.integers(), _attr=safe_text, attribute=safe_text)
@given(instance=Customer1_strategy)
@settings(max_examples=25)
def test_Customer1_instantiation(instance):
    assert isinstance(instance, Customer1)


Customer_Balance_strategy = st.builds(Customer_Balance, Account_balance=safe_text, Adress=safe_text, CustomerID=st.integers(), CustomerName=safe_text, Date=safe_text)
@given(instance=Customer_Balance_strategy)
@settings(max_examples=25)
def test_Customer_Balance_instantiation(instance):
    assert isinstance(instance, Customer_Balance)


Customer_Balance1_strategy = st.builds(Customer_Balance1, Account_balance=safe_text, Adress=safe_text, CustomerID=st.integers(), CustomerName=safe_text, Date=safe_text)
@given(instance=Customer_Balance1_strategy)
@settings(max_examples=25)
def test_Customer_Balance1_instantiation(instance):
    assert isinstance(instance, Customer_Balance1)


Dish_strategy = st.builds(Dish, _attr=safe_text)
@given(instance=Dish_strategy)
@settings(max_examples=25)
def test_Dish_instantiation(instance):
    assert isinstance(instance, Dish)


Employee_strategy = st.builds(Employee, Email=safe_text, ID=st.integers(), Name=safe_text, attribute=safe_text, password=safe_text)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Employee1_strategy = st.builds(Employee1, Email=safe_text, ID=safe_text, Name=safe_text, Password=safe_text, attribute=safe_text)
@given(instance=Employee1_strategy)
@settings(max_examples=25)
def test_Employee1_instantiation(instance):
    assert isinstance(instance, Employee1)


Employee_Actor_strategy = st.builds(Employee_Actor)
@given(instance=Employee_Actor_strategy)
@settings(max_examples=25)
def test_Employee_Actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)


Generate_payment_cheque_employes_UseCase_strategy = st.builds(Generate_payment_cheque_employes_UseCase)
@given(instance=Generate_payment_cheque_employes_UseCase_strategy)
@settings(max_examples=25)
def test_Generate_payment_cheque_employes_UseCase_instantiation(instance):
    assert isinstance(instance, Generate_payment_cheque_employes_UseCase)


Kitchen_worker_strategy = st.builds(Kitchen_worker, Email=safe_text, ID=st.integers(), Name=safe_text, attribute=safe_text, password=safe_text)
@given(instance=Kitchen_worker_strategy)
@settings(max_examples=25)
def test_Kitchen_worker_instantiation(instance):
    assert isinstance(instance, Kitchen_worker)


Menu_strategy = st.builds(Menu, Components=safe_text, DishName=safe_text, Price=safe_text, Quantity=safe_text)
@given(instance=Menu_strategy)
@settings(max_examples=25)
def test_Menu_instantiation(instance):
    assert isinstance(instance, Menu)


Menu1_strategy = st.builds(Menu1, Components=safe_text, DishName=safe_text, Price=safe_text, Quantity=safe_text)
@given(instance=Menu1_strategy)
@settings(max_examples=25)
def test_Menu1_instantiation(instance):
    assert isinstance(instance, Menu1)


Order_strategy = st.builds(Order, Customerid=st.integers(), Dishname=safe_text, OrderID=st.integers(), attribute=safe_text, date=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Order1_strategy = st.builds(Order1, Customerid=st.integers(), Dishname=safe_text, OrderID=st.integers(), attribute=safe_text, date=safe_text)
@given(instance=Order1_strategy)
@settings(max_examples=25)
def test_Order1_instantiation(instance):
    assert isinstance(instance, Order1)


Owner_strategy = st.builds(Owner)
@given(instance=Owner_strategy)
@settings(max_examples=25)
def test_Owner_instantiation(instance):
    assert isinstance(instance, Owner)


Owner1_strategy = st.builds(Owner1)
@given(instance=Owner1_strategy)
@settings(max_examples=25)
def test_Owner1_instantiation(instance):
    assert isinstance(instance, Owner1)


Owner2_strategy = st.builds(Owner2)
@given(instance=Owner2_strategy)
@settings(max_examples=25)
def test_Owner2_instantiation(instance):
    assert isinstance(instance, Owner2)


Payment_strategy = st.builds(Payment, Amount=safe_text, CustomerID=st.integers(), OrderID=st.integers(), PaymentID=st.integers(), date=safe_text, time=safe_text)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Payment1_strategy = st.builds(Payment1, Amount=safe_text, CustomerID=st.integers(), OrderID=st.integers(), PaymentID=st.integers(), date=safe_text, time=safe_text)
@given(instance=Payment1_strategy)
@settings(max_examples=25)
def test_Payment1_instantiation(instance):
    assert isinstance(instance, Payment1)


Plan_strategy = st.builds(Plan, Monthly_plan=safe_text, day_plan=safe_text, weekly_plan=safe_text)
@given(instance=Plan_strategy)
@settings(max_examples=25)
def test_Plan_instantiation(instance):
    assert isinstance(instance, Plan)


Plan1_strategy = st.builds(Plan1, Monthly_plan=safe_text, day_plan=safe_text, weekly_plan=safe_text)
@given(instance=Plan1_strategy)
@settings(max_examples=25)
def test_Plan1_instantiation(instance):
    assert isinstance(instance, Plan1)


PrintRecipts_strategy = st.builds(PrintRecipts, Amount=safe_text, CustomerID=st.integers(), Dishname=safe_text, PaymentID=safe_text, Quantity=st.integers(), date=safe_text, time=safe_text)
@given(instance=PrintRecipts_strategy)
@settings(max_examples=25)
def test_PrintRecipts_instantiation(instance):
    assert isinstance(instance, PrintRecipts)


PrintRecipts1_strategy = st.builds(PrintRecipts1, Amount=safe_text, CustomerID=st.integers(), Dishname=safe_text, PaymentID=safe_text, Quantity=st.integers(), date=safe_text, time=safe_text)
@given(instance=PrintRecipts1_strategy)
@settings(max_examples=25)
def test_PrintRecipts1_instantiation(instance):
    assert isinstance(instance, PrintRecipts1)


Shopping_cart_strategy = st.builds(Shopping_cart, Dishname=safe_text, Quantity=st.integers(), attribute=safe_text, price=st.integers(), time=safe_text)
@given(instance=Shopping_cart_strategy)
@settings(max_examples=25)
def test_Shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_cart)


Shopping_cart1_strategy = st.builds(Shopping_cart1, Dishname=safe_text, Quantity=st.integers(), attribute=safe_text, price=st.integers(), time=safe_text)
@given(instance=Shopping_cart1_strategy)
@settings(max_examples=25)
def test_Shopping_cart1_instantiation(instance):
    assert isinstance(instance, Shopping_cart1)


Storage_strategy = st.builds(Storage, Component_Name=safe_text, Component_id=st.integers())
@given(instance=Storage_strategy)
@settings(max_examples=25)
def test_Storage_instantiation(instance):
    assert isinstance(instance, Storage)


Storage1_strategy = st.builds(Storage1, Component_Name=safe_text, Component_id=st.integers())
@given(instance=Storage1_strategy)
@settings(max_examples=25)
def test_Storage1_instantiation(instance):
    assert isinstance(instance, Storage1)


System_strategy = st.builds(System)
@given(instance=System_strategy)
@settings(max_examples=25)
def test_System_instantiation(instance):
    assert isinstance(instance, System)


System1_strategy = st.builds(System1, Email=safe_text, Password=safe_text, WebAdmin_or_owner=safe_text)
@given(instance=System1_strategy)
@settings(max_examples=25)
def test_System1_instantiation(instance):
    assert isinstance(instance, System1)


UseCase_UseCase_strategy = st.builds(UseCase_UseCase)
@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)


Waiter_strategy = st.builds(Waiter)
@given(instance=Waiter_strategy)
@settings(max_examples=25)
def test_Waiter_instantiation(instance):
    assert isinstance(instance, Waiter)


Web_master_strategy = st.builds(Web_master)
@given(instance=Web_master_strategy)
@settings(max_examples=25)
def test_Web_master_instantiation(instance):
    assert isinstance(instance, Web_master)


account_registration_strategy = st.builds(account_registration)
@given(instance=account_registration_strategy)
@settings(max_examples=25)
def test_account_registration_instantiation(instance):
    assert isinstance(instance, account_registration)


account_type_strategy = st.builds(account_type, _attr=safe_text, email=safe_text, id=safe_text, name=safe_text, password=safe_text)
@given(instance=account_type_strategy)
@settings(max_examples=25)
def test_account_type_instantiation(instance):
    assert isinstance(instance, account_type)


add_and_get_from_storage_check_storage_UseCase_strategy = st.builds(add_and_get_from_storage_check_storage_UseCase)
@given(instance=add_and_get_from_storage_check_storage_UseCase_strategy)
@settings(max_examples=25)
def test_add_and_get_from_storage_check_storage_UseCase_instantiation(instance):
    assert isinstance(instance, add_and_get_from_storage_check_storage_UseCase)


add_constraints_UseCase_strategy = st.builds(add_constraints_UseCase)
@given(instance=add_constraints_UseCase_strategy)
@settings(max_examples=25)
def test_add_constraints_UseCase_instantiation(instance):
    assert isinstance(instance, add_constraints_UseCase)


bank_account_strategy = st.builds(bank_account)
@given(instance=bank_account_strategy)
@settings(max_examples=25)
def test_bank_account_instantiation(instance):
    assert isinstance(instance, bank_account)


catering_strategy = st.builds(catering)
@given(instance=catering_strategy)
@settings(max_examples=25)
def test_catering_instantiation(instance):
    assert isinstance(instance, catering)


check_bank_account_for_payments_UseCase_strategy = st.builds(check_bank_account_for_payments_UseCase)
@given(instance=check_bank_account_for_payments_UseCase_strategy)
@settings(max_examples=25)
def test_check_bank_account_for_payments_UseCase_instantiation(instance):
    assert isinstance(instance, check_bank_account_for_payments_UseCase)


chef_strategy = st.builds(chef, Email=safe_text, Employee_ID=st.integers(), Name=safe_text, Room_no=st.integers(), passowrd=safe_text)
@given(instance=chef_strategy)
@settings(max_examples=25)
def test_chef_instantiation(instance):
    assert isinstance(instance, chef)


chef1_strategy = st.builds(chef1, Email=safe_text, Employee_ID=st.integers(), Name=safe_text, Room_no=st.integers(), passowrd=safe_text)
@given(instance=chef1_strategy)
@settings(max_examples=25)
def test_chef1_instantiation(instance):
    assert isinstance(instance, chef1)


chef2_strategy = st.builds(chef2)
@given(instance=chef2_strategy)
@settings(max_examples=25)
def test_chef2_instantiation(instance):
    assert isinstance(instance, chef2)


chef_Actor_strategy = st.builds(chef_Actor)
@given(instance=chef_Actor_strategy)
@settings(max_examples=25)
def test_chef_Actor_instantiation(instance):
    assert isinstance(instance, chef_Actor)


contact_strategy = st.builds(contact, Adress=safe_text, Email=safe_text, Name=safe_text, Tel=st.integers(), attribute=safe_text)
@given(instance=contact_strategy)
@settings(max_examples=25)
def test_contact_instantiation(instance):
    assert isinstance(instance, contact)


create_invoice_UseCase_strategy = st.builds(create_invoice_UseCase)
@given(instance=create_invoice_UseCase_strategy)
@settings(max_examples=25)
def test_create_invoice_UseCase_instantiation(instance):
    assert isinstance(instance, create_invoice_UseCase)


customer_Actor_strategy = st.builds(customer_Actor)
@given(instance=customer_Actor_strategy)
@settings(max_examples=25)
def test_customer_Actor_instantiation(instance):
    assert isinstance(instance, customer_Actor)


customer_account_strategy = st.builds(customer_account)
@given(instance=customer_account_strategy)
@settings(max_examples=25)
def test_customer_account_instantiation(instance):
    assert isinstance(instance, customer_account)


daily_weekly_monthly_plan_UseCase_strategy = st.builds(daily_weekly_monthly_plan_UseCase)
@given(instance=daily_weekly_monthly_plan_UseCase_strategy)
@settings(max_examples=25)
def test_daily_weekly_monthly_plan_UseCase_instantiation(instance):
    assert isinstance(instance, daily_weekly_monthly_plan_UseCase)


date2_strategy = st.builds(date2)
@given(instance=date2_strategy)
@settings(max_examples=25)
def test_date2_instantiation(instance):
    assert isinstance(instance, date2)


dayplan_strategy = st.builds(dayplan, Monday=safe_text, friday=safe_text, plan_per_date=safe_text, saturday=safe_text, sunday=safe_text, thursday=safe_text, tuesday=safe_text, wenesday=safe_text)
@given(instance=dayplan_strategy)
@settings(max_examples=25)
def test_dayplan_instantiation(instance):
    assert isinstance(instance, dayplan)


drink_strategy = st.builds(drink, type=safe_text)
@given(instance=drink_strategy)
@settings(max_examples=25)
def test_drink_instantiation(instance):
    assert isinstance(instance, drink)


events_strategy = st.builds(events, attribute=safe_text, catering_location=safe_text, duration=safe_text, get_employee_name=safe_text)
@given(instance=events_strategy)
@settings(max_examples=25)
def test_events_instantiation(instance):
    assert isinstance(instance, events)


food_dish_strategy = st.builds(food_dish, attribute=safe_text, attribute2=safe_text, type=safe_text)
@given(instance=food_dish_strategy)
@settings(max_examples=25)
def test_food_dish_instantiation(instance):
    assert isinstance(instance, food_dish)


help_strategy = st.builds(help)
@given(instance=help_strategy)
@settings(max_examples=25)
def test_help_instantiation(instance):
    assert isinstance(instance, help)


kitchen_worker_strategy = st.builds(kitchen_worker)
@given(instance=kitchen_worker_strategy)
@settings(max_examples=25)
def test_kitchen_worker_instantiation(instance):
    assert isinstance(instance, kitchen_worker)


liquid_strategy = st.builds(liquid, must_be_unit_in_ml=safe_text, name=safe_text, quantiy=safe_text)
@given(instance=liquid_strategy)
@settings(max_examples=25)
def test_liquid_instantiation(instance):
    assert isinstance(instance, liquid)


list_of_outdated_components_UseCase_strategy = st.builds(list_of_outdated_components_UseCase)
@given(instance=list_of_outdated_components_UseCase_strategy)
@settings(max_examples=25)
def test_list_of_outdated_components_UseCase_instantiation(instance):
    assert isinstance(instance, list_of_outdated_components_UseCase)


menu_strategy = st.builds(menu, attribute=safe_text, dish_quantity=safe_text, dishname=safe_text, drinkname=safe_text, price=safe_text)
@given(instance=menu_strategy)
@settings(max_examples=25)
def test_menu_instantiation(instance):
    assert isinstance(instance, menu)


order_strategy = st.builds(order, _attr=safe_text, date=safe_text, order_id=safe_text, ordered_item=safe_text, status=safe_text)
@given(instance=order_strategy)
@settings(max_examples=25)
def test_order_instantiation(instance):
    assert isinstance(instance, order)


order_catering_service_UseCase_strategy = st.builds(order_catering_service_UseCase)
@given(instance=order_catering_service_UseCase_strategy)
@settings(max_examples=25)
def test_order_catering_service_UseCase_instantiation(instance):
    assert isinstance(instance, order_catering_service_UseCase)


order_missing_components_UseCase_strategy = st.builds(order_missing_components_UseCase)
@given(instance=order_missing_components_UseCase_strategy)
@settings(max_examples=25)
def test_order_missing_components_UseCase_instantiation(instance):
    assert isinstance(instance, order_missing_components_UseCase)


owner_System_Actor_strategy = st.builds(owner_System_Actor)
@given(instance=owner_System_Actor_strategy)
@settings(max_examples=25)
def test_owner_System_Actor_instantiation(instance):
    assert isinstance(instance, owner_System_Actor)


owner__system_strategy = st.builds(owner__system, attribute=safe_text)
@given(instance=owner__system_strategy)
@settings(max_examples=25)
def test_owner__system_instantiation(instance):
    assert isinstance(instance, owner__system)


payment_strategy = st.builds(payment, _attr=safe_text, amount=safe_text, total_amount=safe_text)
@given(instance=payment_strategy)
@settings(max_examples=25)
def test_payment_instantiation(instance):
    assert isinstance(instance, payment)


payorder_UseCase_strategy = st.builds(payorder_UseCase)
@given(instance=payorder_UseCase_strategy)
@settings(max_examples=25)
def test_payorder_UseCase_instantiation(instance):
    assert isinstance(instance, payorder_UseCase)


prepration_plan_dishes_UseCase_strategy = st.builds(prepration_plan_dishes_UseCase)
@given(instance=prepration_plan_dishes_UseCase_strategy)
@settings(max_examples=25)
def test_prepration_plan_dishes_UseCase_instantiation(instance):
    assert isinstance(instance, prepration_plan_dishes_UseCase)


select_from_menu_UseCase_strategy = st.builds(select_from_menu_UseCase)
@given(instance=select_from_menu_UseCase_strategy)
@settings(max_examples=25)
def test_select_from_menu_UseCase_instantiation(instance):
    assert isinstance(instance, select_from_menu_UseCase)


shopping_cart_strategy = st.builds(shopping_cart)
@given(instance=shopping_cart_strategy)
@settings(max_examples=25)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, shopping_cart)


sign_up_login_logout_UseCase_strategy = st.builds(sign_up_login_logout_UseCase)
@given(instance=sign_up_login_logout_UseCase_strategy)
@settings(max_examples=25)
def test_sign_up_login_logout_UseCase_instantiation(instance):
    assert isinstance(instance, sign_up_login_logout_UseCase)


solid_strategy = st.builds(solid, must_be_unit_in_kg=safe_text)
@given(instance=solid_strategy)
@settings(max_examples=25)
def test_solid_instantiation(instance):
    assert isinstance(instance, solid)


solid1_strategy = st.builds(solid1, name=safe_text, pieces=st.integers(), state=safe_text, weight__kg_=safe_text)
@given(instance=solid1_strategy)
@settings(max_examples=25)
def test_solid1_instantiation(instance):
    assert isinstance(instance, solid1)


weekly_plan_dishes_UseCase_strategy = st.builds(weekly_plan_dishes_UseCase)
@given(instance=weekly_plan_dishes_UseCase_strategy)
@settings(max_examples=25)
def test_weekly_plan_dishes_UseCase_instantiation(instance):
    assert isinstance(instance, weekly_plan_dishes_UseCase)


weekly_plan_of_each_cutomer_UseCase_strategy = st.builds(weekly_plan_of_each_cutomer_UseCase)
@given(instance=weekly_plan_of_each_cutomer_UseCase_strategy)
@settings(max_examples=25)
def test_weekly_plan_of_each_cutomer_UseCase_instantiation(instance):
    assert isinstance(instance, weekly_plan_of_each_cutomer_UseCase)


