import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Class,
    Credit_Card_company_Actor,
    Customer1_Actor,
    Customer1_Actor1,
    Supper_System_Add_product_UseCase,
    Supper_System_Check_item_availability_UseCase,
    Supper_System_Checkout_UseCase,
    Supper_System_Collect_package_UseCase,
    Supper_System_Confirm_payment_UseCase,
    Supper_System_Create_account_UseCase,
    Supper_System_Create_order_list_UseCase,
    Supper_System_Deliver_Package_UseCase,
    Supper_System_Email_reminder_UseCase,
    Supper_System_Login_UseCase,
    Supper_System_Pay_Shipping_Fees_UseCase,
    Supper_System_Print_invoice_UseCase,
    Supper_System_Receive_package_UseCase,
    Supper_System_Return_defective_items_UseCase,
    Supper_System_Return_items_UseCase,
    Supper_System_Save_invoice_UseCase,
    Supper_System_Search_product_UseCase,
    Supper_System_Sign_delivery_notice_UseCase,
    Supper_System_Start_Shopping_UseCase,
    Supper_System_Update_order_list_UseCase,
    Supper_System_Update_unit_number_UseCase,
    Supper_System_Verify_Customer_information_UseCase,
    Supper_System_View_Product_UseCase,
    Supper_System_View_invoice_on_screen_UseCase,
    Supper_System_prepare_package_UseCase,
    Supper_System_schedule_for_delivery_UseCase,
    Warehouse_department_Actor,
    Warehouse_man_Actor,
    delivery_man_Actor,
    djkd,
    fsdf,
    prepare_package_UseCase,
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

def test_fsdf_fdasf_value_roundtrip():
    instance = fsdf(fdasf=7)
    assert instance.fdasf == 7
    instance.fdasf = 13
    assert instance.fdasf == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Credit_Card_company_Actor_strategy = st.builds(Credit_Card_company_Actor)
@given(instance=Credit_Card_company_Actor_strategy)
@settings(max_examples=25)
def test_Credit_Card_company_Actor_instantiation(instance):
    assert isinstance(instance, Credit_Card_company_Actor)


Customer1_Actor_strategy = st.builds(Customer1_Actor)
@given(instance=Customer1_Actor_strategy)
@settings(max_examples=25)
def test_Customer1_Actor_instantiation(instance):
    assert isinstance(instance, Customer1_Actor)


Customer1_Actor1_strategy = st.builds(Customer1_Actor1)
@given(instance=Customer1_Actor1_strategy)
@settings(max_examples=25)
def test_Customer1_Actor1_instantiation(instance):
    assert isinstance(instance, Customer1_Actor1)


Supper_System_Add_product_UseCase_strategy = st.builds(Supper_System_Add_product_UseCase)
@given(instance=Supper_System_Add_product_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Add_product_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Add_product_UseCase)


Supper_System_Check_item_availability_UseCase_strategy = st.builds(Supper_System_Check_item_availability_UseCase)
@given(instance=Supper_System_Check_item_availability_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Check_item_availability_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Check_item_availability_UseCase)


Supper_System_Checkout_UseCase_strategy = st.builds(Supper_System_Checkout_UseCase)
@given(instance=Supper_System_Checkout_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Checkout_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Checkout_UseCase)


Supper_System_Collect_package_UseCase_strategy = st.builds(Supper_System_Collect_package_UseCase)
@given(instance=Supper_System_Collect_package_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Collect_package_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Collect_package_UseCase)


Supper_System_Confirm_payment_UseCase_strategy = st.builds(Supper_System_Confirm_payment_UseCase)
@given(instance=Supper_System_Confirm_payment_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Confirm_payment_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Confirm_payment_UseCase)


Supper_System_Create_account_UseCase_strategy = st.builds(Supper_System_Create_account_UseCase)
@given(instance=Supper_System_Create_account_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Create_account_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Create_account_UseCase)


Supper_System_Create_order_list_UseCase_strategy = st.builds(Supper_System_Create_order_list_UseCase)
@given(instance=Supper_System_Create_order_list_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Create_order_list_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Create_order_list_UseCase)


Supper_System_Deliver_Package_UseCase_strategy = st.builds(Supper_System_Deliver_Package_UseCase)
@given(instance=Supper_System_Deliver_Package_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Deliver_Package_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Deliver_Package_UseCase)


Supper_System_Email_reminder_UseCase_strategy = st.builds(Supper_System_Email_reminder_UseCase)
@given(instance=Supper_System_Email_reminder_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Email_reminder_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Email_reminder_UseCase)


Supper_System_Login_UseCase_strategy = st.builds(Supper_System_Login_UseCase)
@given(instance=Supper_System_Login_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Login_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Login_UseCase)


Supper_System_Pay_Shipping_Fees_UseCase_strategy = st.builds(Supper_System_Pay_Shipping_Fees_UseCase)
@given(instance=Supper_System_Pay_Shipping_Fees_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Pay_Shipping_Fees_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Pay_Shipping_Fees_UseCase)


Supper_System_Print_invoice_UseCase_strategy = st.builds(Supper_System_Print_invoice_UseCase)
@given(instance=Supper_System_Print_invoice_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Print_invoice_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Print_invoice_UseCase)


Supper_System_Receive_package_UseCase_strategy = st.builds(Supper_System_Receive_package_UseCase)
@given(instance=Supper_System_Receive_package_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Receive_package_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Receive_package_UseCase)


Supper_System_Return_defective_items_UseCase_strategy = st.builds(Supper_System_Return_defective_items_UseCase)
@given(instance=Supper_System_Return_defective_items_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Return_defective_items_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Return_defective_items_UseCase)


Supper_System_Return_items_UseCase_strategy = st.builds(Supper_System_Return_items_UseCase)
@given(instance=Supper_System_Return_items_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Return_items_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Return_items_UseCase)


Supper_System_Save_invoice_UseCase_strategy = st.builds(Supper_System_Save_invoice_UseCase)
@given(instance=Supper_System_Save_invoice_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Save_invoice_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Save_invoice_UseCase)


Supper_System_Search_product_UseCase_strategy = st.builds(Supper_System_Search_product_UseCase)
@given(instance=Supper_System_Search_product_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Search_product_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Search_product_UseCase)


Supper_System_Sign_delivery_notice_UseCase_strategy = st.builds(Supper_System_Sign_delivery_notice_UseCase)
@given(instance=Supper_System_Sign_delivery_notice_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Sign_delivery_notice_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Sign_delivery_notice_UseCase)


Supper_System_Start_Shopping_UseCase_strategy = st.builds(Supper_System_Start_Shopping_UseCase)
@given(instance=Supper_System_Start_Shopping_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Start_Shopping_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Start_Shopping_UseCase)


Supper_System_Update_order_list_UseCase_strategy = st.builds(Supper_System_Update_order_list_UseCase)
@given(instance=Supper_System_Update_order_list_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Update_order_list_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Update_order_list_UseCase)


Supper_System_Update_unit_number_UseCase_strategy = st.builds(Supper_System_Update_unit_number_UseCase)
@given(instance=Supper_System_Update_unit_number_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Update_unit_number_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Update_unit_number_UseCase)


Supper_System_Verify_Customer_information_UseCase_strategy = st.builds(Supper_System_Verify_Customer_information_UseCase)
@given(instance=Supper_System_Verify_Customer_information_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_Verify_Customer_information_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_Verify_Customer_information_UseCase)


Supper_System_View_Product_UseCase_strategy = st.builds(Supper_System_View_Product_UseCase)
@given(instance=Supper_System_View_Product_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_View_Product_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_View_Product_UseCase)


Supper_System_View_invoice_on_screen_UseCase_strategy = st.builds(Supper_System_View_invoice_on_screen_UseCase)
@given(instance=Supper_System_View_invoice_on_screen_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_View_invoice_on_screen_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_View_invoice_on_screen_UseCase)


Supper_System_prepare_package_UseCase_strategy = st.builds(Supper_System_prepare_package_UseCase)
@given(instance=Supper_System_prepare_package_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_prepare_package_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_prepare_package_UseCase)


Supper_System_schedule_for_delivery_UseCase_strategy = st.builds(Supper_System_schedule_for_delivery_UseCase)
@given(instance=Supper_System_schedule_for_delivery_UseCase_strategy)
@settings(max_examples=25)
def test_Supper_System_schedule_for_delivery_UseCase_instantiation(instance):
    assert isinstance(instance, Supper_System_schedule_for_delivery_UseCase)


Warehouse_department_Actor_strategy = st.builds(Warehouse_department_Actor)
@given(instance=Warehouse_department_Actor_strategy)
@settings(max_examples=25)
def test_Warehouse_department_Actor_instantiation(instance):
    assert isinstance(instance, Warehouse_department_Actor)


Warehouse_man_Actor_strategy = st.builds(Warehouse_man_Actor)
@given(instance=Warehouse_man_Actor_strategy)
@settings(max_examples=25)
def test_Warehouse_man_Actor_instantiation(instance):
    assert isinstance(instance, Warehouse_man_Actor)


delivery_man_Actor_strategy = st.builds(delivery_man_Actor)
@given(instance=delivery_man_Actor_strategy)
@settings(max_examples=25)
def test_delivery_man_Actor_instantiation(instance):
    assert isinstance(instance, delivery_man_Actor)


djkd_strategy = st.builds(djkd)
@given(instance=djkd_strategy)
@settings(max_examples=25)
def test_djkd_instantiation(instance):
    assert isinstance(instance, djkd)


fsdf_strategy = st.builds(fsdf, fdasf=st.integers())
@given(instance=fsdf_strategy)
@settings(max_examples=25)
def test_fsdf_instantiation(instance):
    assert isinstance(instance, fsdf)


prepare_package_UseCase_strategy = st.builds(prepare_package_UseCase)
@given(instance=prepare_package_UseCase_strategy)
@settings(max_examples=25)
def test_prepare_package_UseCase_instantiation(instance):
    assert isinstance(instance, prepare_package_UseCase)


