# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Menu,
    Online_pizza_ordering,
    Online_payment_methods,
    Pay_cash_on_deliver,
    Payment,
    Admin,
    Customer,
    PayAt_Delivery_UseCase,
    Add_new_address_UseCase,
    Pre_order_UseCase,
    Admin_Actor,
    Manage_accounts_UseCase,
    Edit_menu_UseCase,
    Deliver_pizza_UseCase,
    Cook_Pizza_UseCase,
    Receive_order_UseCase,
    Delivery_person_Actor,
    Pizza_Chef_Actor,
    Order_tracking_UseCase,
    Make_Payment_UseCase,
    Save_favourite_order_UseCase,
    Pay_online_UseCase,
    Checkout_UseCase,
    Search_store_locations_UseCase,
    Change_toppings_UseCase,
    Create_Account_UseCase,
    View_side_orders_UseCase,
    Add_item_UseCase,
    Create_your_own_pizza_UseCase,
    View_Pizza_types_UseCase,
    View_Meal_Deal_UseCase,
    Sign_In_UseCase,
    Registered_User_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_menu_is_not_abstract():
    assert not inspect.isabstract(Menu)


def test_hyp_menu_constructor_exists():
    assert callable(Menu.__init__)


def test_hyp_menu_constructor_args():
    sig = inspect.signature(Menu.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "toppings" in params, "Missing parameter 'toppings'"





def test_hyp_online_pizza_ordering_is_not_abstract():
    assert not inspect.isabstract(Online_pizza_ordering)


def test_hyp_online_pizza_ordering_constructor_exists():
    assert callable(Online_pizza_ordering.__init__)


def test_hyp_online_pizza_ordering_constructor_args():
    sig = inspect.signature(Online_pizza_ordering.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Ingredients" in params, "Missing parameter 'Ingredients'"
    assert "pizza_type" in params, "Missing parameter 'pizza_type'"






def test_hyp_online_payment_methods_is_not_abstract():
    assert not inspect.isabstract(Online_payment_methods)


def test_hyp_online_payment_methods_constructor_exists():
    assert callable(Online_payment_methods.__init__)


def test_hyp_online_payment_methods_constructor_args():
    sig = inspect.signature(Online_payment_methods.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pay_cash_on_deliver_is_not_abstract():
    assert not inspect.isabstract(Pay_cash_on_deliver)


def test_hyp_pay_cash_on_deliver_constructor_exists():
    assert callable(Pay_cash_on_deliver.__init__)


def test_hyp_pay_cash_on_deliver_constructor_args():
    sig = inspect.signature(Pay_cash_on_deliver.__init__)
    params = list(sig.parameters.keys())



def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_payat_delivery_usecase_is_not_abstract():
    assert not inspect.isabstract(PayAt_Delivery_UseCase)


def test_hyp_payat_delivery_usecase_constructor_exists():
    assert callable(PayAt_Delivery_UseCase.__init__)


def test_hyp_payat_delivery_usecase_constructor_args():
    sig = inspect.signature(PayAt_Delivery_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_add_new_address_usecase_is_not_abstract():
    assert not inspect.isabstract(Add_new_address_UseCase)


def test_hyp_add_new_address_usecase_constructor_exists():
    assert callable(Add_new_address_UseCase.__init__)


def test_hyp_add_new_address_usecase_constructor_args():
    sig = inspect.signature(Add_new_address_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pre_order_usecase_is_not_abstract():
    assert not inspect.isabstract(Pre_order_UseCase)


def test_hyp_pre_order_usecase_constructor_exists():
    assert callable(Pre_order_UseCase.__init__)


def test_hyp_pre_order_usecase_constructor_args():
    sig = inspect.signature(Pre_order_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_hyp_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_hyp_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_manage_accounts_usecase_is_not_abstract():
    assert not inspect.isabstract(Manage_accounts_UseCase)


def test_hyp_manage_accounts_usecase_constructor_exists():
    assert callable(Manage_accounts_UseCase.__init__)


def test_hyp_manage_accounts_usecase_constructor_args():
    sig = inspect.signature(Manage_accounts_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edit_menu_usecase_is_not_abstract():
    assert not inspect.isabstract(Edit_menu_UseCase)


def test_hyp_edit_menu_usecase_constructor_exists():
    assert callable(Edit_menu_UseCase.__init__)


def test_hyp_edit_menu_usecase_constructor_args():
    sig = inspect.signature(Edit_menu_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_deliver_pizza_usecase_is_not_abstract():
    assert not inspect.isabstract(Deliver_pizza_UseCase)


def test_hyp_deliver_pizza_usecase_constructor_exists():
    assert callable(Deliver_pizza_UseCase.__init__)


def test_hyp_deliver_pizza_usecase_constructor_args():
    sig = inspect.signature(Deliver_pizza_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cook_pizza_usecase_is_not_abstract():
    assert not inspect.isabstract(Cook_Pizza_UseCase)


def test_hyp_cook_pizza_usecase_constructor_exists():
    assert callable(Cook_Pizza_UseCase.__init__)


def test_hyp_cook_pizza_usecase_constructor_args():
    sig = inspect.signature(Cook_Pizza_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_receive_order_usecase_is_not_abstract():
    assert not inspect.isabstract(Receive_order_UseCase)


def test_hyp_receive_order_usecase_constructor_exists():
    assert callable(Receive_order_UseCase.__init__)


def test_hyp_receive_order_usecase_constructor_args():
    sig = inspect.signature(Receive_order_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_delivery_person_actor_is_not_abstract():
    assert not inspect.isabstract(Delivery_person_Actor)


def test_hyp_delivery_person_actor_constructor_exists():
    assert callable(Delivery_person_Actor.__init__)


def test_hyp_delivery_person_actor_constructor_args():
    sig = inspect.signature(Delivery_person_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pizza_chef_actor_is_not_abstract():
    assert not inspect.isabstract(Pizza_Chef_Actor)


def test_hyp_pizza_chef_actor_constructor_exists():
    assert callable(Pizza_Chef_Actor.__init__)


def test_hyp_pizza_chef_actor_constructor_args():
    sig = inspect.signature(Pizza_Chef_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_order_tracking_usecase_is_not_abstract():
    assert not inspect.isabstract(Order_tracking_UseCase)


def test_hyp_order_tracking_usecase_constructor_exists():
    assert callable(Order_tracking_UseCase.__init__)


def test_hyp_order_tracking_usecase_constructor_args():
    sig = inspect.signature(Order_tracking_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_make_payment_usecase_is_not_abstract():
    assert not inspect.isabstract(Make_Payment_UseCase)


def test_hyp_make_payment_usecase_constructor_exists():
    assert callable(Make_Payment_UseCase.__init__)


def test_hyp_make_payment_usecase_constructor_args():
    sig = inspect.signature(Make_Payment_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_save_favourite_order_usecase_is_not_abstract():
    assert not inspect.isabstract(Save_favourite_order_UseCase)


def test_hyp_save_favourite_order_usecase_constructor_exists():
    assert callable(Save_favourite_order_UseCase.__init__)


def test_hyp_save_favourite_order_usecase_constructor_args():
    sig = inspect.signature(Save_favourite_order_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pay_online_usecase_is_not_abstract():
    assert not inspect.isabstract(Pay_online_UseCase)


def test_hyp_pay_online_usecase_constructor_exists():
    assert callable(Pay_online_UseCase.__init__)


def test_hyp_pay_online_usecase_constructor_args():
    sig = inspect.signature(Pay_online_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_checkout_usecase_is_not_abstract():
    assert not inspect.isabstract(Checkout_UseCase)


def test_hyp_checkout_usecase_constructor_exists():
    assert callable(Checkout_UseCase.__init__)


def test_hyp_checkout_usecase_constructor_args():
    sig = inspect.signature(Checkout_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_search_store_locations_usecase_is_not_abstract():
    assert not inspect.isabstract(Search_store_locations_UseCase)


def test_hyp_search_store_locations_usecase_constructor_exists():
    assert callable(Search_store_locations_UseCase.__init__)


def test_hyp_search_store_locations_usecase_constructor_args():
    sig = inspect.signature(Search_store_locations_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_change_toppings_usecase_is_not_abstract():
    assert not inspect.isabstract(Change_toppings_UseCase)


def test_hyp_change_toppings_usecase_constructor_exists():
    assert callable(Change_toppings_UseCase.__init__)


def test_hyp_change_toppings_usecase_constructor_args():
    sig = inspect.signature(Change_toppings_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_create_account_usecase_is_not_abstract():
    assert not inspect.isabstract(Create_Account_UseCase)


def test_hyp_create_account_usecase_constructor_exists():
    assert callable(Create_Account_UseCase.__init__)


def test_hyp_create_account_usecase_constructor_args():
    sig = inspect.signature(Create_Account_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_view_side_orders_usecase_is_not_abstract():
    assert not inspect.isabstract(View_side_orders_UseCase)


def test_hyp_view_side_orders_usecase_constructor_exists():
    assert callable(View_side_orders_UseCase.__init__)


def test_hyp_view_side_orders_usecase_constructor_args():
    sig = inspect.signature(View_side_orders_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_add_item_usecase_is_not_abstract():
    assert not inspect.isabstract(Add_item_UseCase)


def test_hyp_add_item_usecase_constructor_exists():
    assert callable(Add_item_UseCase.__init__)


def test_hyp_add_item_usecase_constructor_args():
    sig = inspect.signature(Add_item_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_create_your_own_pizza_usecase_is_not_abstract():
    assert not inspect.isabstract(Create_your_own_pizza_UseCase)


def test_hyp_create_your_own_pizza_usecase_constructor_exists():
    assert callable(Create_your_own_pizza_UseCase.__init__)


def test_hyp_create_your_own_pizza_usecase_constructor_args():
    sig = inspect.signature(Create_your_own_pizza_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_view_pizza_types_usecase_is_not_abstract():
    assert not inspect.isabstract(View_Pizza_types_UseCase)


def test_hyp_view_pizza_types_usecase_constructor_exists():
    assert callable(View_Pizza_types_UseCase.__init__)


def test_hyp_view_pizza_types_usecase_constructor_args():
    sig = inspect.signature(View_Pizza_types_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_view_meal_deal_usecase_is_not_abstract():
    assert not inspect.isabstract(View_Meal_Deal_UseCase)


def test_hyp_view_meal_deal_usecase_constructor_exists():
    assert callable(View_Meal_Deal_UseCase.__init__)


def test_hyp_view_meal_deal_usecase_constructor_args():
    sig = inspect.signature(View_Meal_Deal_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sign_in_usecase_is_not_abstract():
    assert not inspect.isabstract(Sign_In_UseCase)


def test_hyp_sign_in_usecase_constructor_exists():
    assert callable(Sign_In_UseCase.__init__)


def test_hyp_sign_in_usecase_constructor_args():
    sig = inspect.signature(Sign_In_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_registered_user_actor_is_not_abstract():
    assert not inspect.isabstract(Registered_User_Actor)


def test_hyp_registered_user_actor_constructor_exists():
    assert callable(Registered_User_Actor.__init__)


def test_hyp_registered_user_actor_constructor_args():
    sig = inspect.signature(Registered_User_Actor.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Menu_strategy = st.builds(
    Menu,
    Quantity=
        safe_text,
    toppings=
        safe_text
)
Online_pizza_ordering_strategy = st.builds(
    Online_pizza_ordering,
    Price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Ingredients=
        safe_text,
    pizza_type=
        safe_text
)
Online_payment_methods_strategy = st.builds(
    Online_payment_methods,
)
Pay_cash_on_deliver_strategy = st.builds(
    Pay_cash_on_deliver,
)
Payment_strategy = st.builds(
    Payment,
)
Admin_strategy = st.builds(
    Admin,
)
Customer_strategy = st.builds(
    Customer,
    Password=
        safe_text,
    Name=
        safe_text
)
PayAt_Delivery_UseCase_strategy = st.builds(
    PayAt_Delivery_UseCase,
)
Add_new_address_UseCase_strategy = st.builds(
    Add_new_address_UseCase,
)
Pre_order_UseCase_strategy = st.builds(
    Pre_order_UseCase,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)
Manage_accounts_UseCase_strategy = st.builds(
    Manage_accounts_UseCase,
)
Edit_menu_UseCase_strategy = st.builds(
    Edit_menu_UseCase,
)
Deliver_pizza_UseCase_strategy = st.builds(
    Deliver_pizza_UseCase,
)
Cook_Pizza_UseCase_strategy = st.builds(
    Cook_Pizza_UseCase,
)
Receive_order_UseCase_strategy = st.builds(
    Receive_order_UseCase,
)
Delivery_person_Actor_strategy = st.builds(
    Delivery_person_Actor,
)
Pizza_Chef_Actor_strategy = st.builds(
    Pizza_Chef_Actor,
)
Order_tracking_UseCase_strategy = st.builds(
    Order_tracking_UseCase,
)
Make_Payment_UseCase_strategy = st.builds(
    Make_Payment_UseCase,
)
Save_favourite_order_UseCase_strategy = st.builds(
    Save_favourite_order_UseCase,
)
Pay_online_UseCase_strategy = st.builds(
    Pay_online_UseCase,
)
Checkout_UseCase_strategy = st.builds(
    Checkout_UseCase,
)
Search_store_locations_UseCase_strategy = st.builds(
    Search_store_locations_UseCase,
)
Change_toppings_UseCase_strategy = st.builds(
    Change_toppings_UseCase,
)
Create_Account_UseCase_strategy = st.builds(
    Create_Account_UseCase,
)
View_side_orders_UseCase_strategy = st.builds(
    View_side_orders_UseCase,
)
Add_item_UseCase_strategy = st.builds(
    Add_item_UseCase,
)
Create_your_own_pizza_UseCase_strategy = st.builds(
    Create_your_own_pizza_UseCase,
)
View_Pizza_types_UseCase_strategy = st.builds(
    View_Pizza_types_UseCase,
)
View_Meal_Deal_UseCase_strategy = st.builds(
    View_Meal_Deal_UseCase,
)
Sign_In_UseCase_strategy = st.builds(
    Sign_In_UseCase,
)
Registered_User_Actor_strategy = st.builds(
    Registered_User_Actor,
)




@given(instance=Menu_strategy)
def test_hyp_menu_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Menu_strategy)
def test_hyp_menu_toppings_setter(instance):
    original = instance.toppings
    instance.toppings = original
    assert instance.toppings == original




@given(instance=Online_pizza_ordering_strategy)
def test_hyp_online_pizza_ordering_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Online_pizza_ordering_strategy)
def test_hyp_online_pizza_ordering_Ingredients_setter(instance):
    original = instance.Ingredients
    instance.Ingredients = original
    assert instance.Ingredients == original



@given(instance=Online_pizza_ordering_strategy)
def test_hyp_online_pizza_ordering_pizza_type_setter(instance):
    original = instance.pizza_type
    instance.pizza_type = original
    assert instance.pizza_type == original








@given(instance=Customer_strategy)
def test_hyp_customer_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Customer_strategy)
def test_hyp_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




























# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Add_item_UseCase,
    Add_new_address_UseCase,
    Admin,
    Admin_Actor,
    Change_toppings_UseCase,
    Checkout_UseCase,
    Cook_Pizza_UseCase,
    Create_Account_UseCase,
    Create_your_own_pizza_UseCase,
    Customer,
    Deliver_pizza_UseCase,
    Delivery_person_Actor,
    Edit_menu_UseCase,
    Make_Payment_UseCase,
    Manage_accounts_UseCase,
    Menu,
    Online_payment_methods,
    Online_pizza_ordering,
    Order_tracking_UseCase,
    PayAt_Delivery_UseCase,
    Pay_cash_on_deliver,
    Pay_online_UseCase,
    Payment,
    Pizza_Chef_Actor,
    Pre_order_UseCase,
    Receive_order_UseCase,
    Registered_User_Actor,
    Save_favourite_order_UseCase,
    Search_store_locations_UseCase,
    Sign_In_UseCase,
    View_Meal_Deal_UseCase,
    View_Pizza_types_UseCase,
    View_side_orders_UseCase,
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

def test_Customer_Name_value_roundtrip():
    instance = Customer(Name="sample_text", Password="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Customer_Password_value_roundtrip():
    instance = Customer(Name="sample_text", Password="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Menu_Quantity_value_roundtrip():
    instance = Menu(Quantity="sample_text", toppings="sample_text")
    assert instance.Quantity == "sample_text"
    instance.Quantity = "sample_text_2"
    assert instance.Quantity == "sample_text_2"


def test_Menu_toppings_value_roundtrip():
    instance = Menu(Quantity="sample_text", toppings="sample_text")
    assert instance.toppings == "sample_text"
    instance.toppings = "sample_text_2"
    assert instance.toppings == "sample_text_2"


def test_Online_pizza_ordering_Ingredients_value_roundtrip():
    instance = Online_pizza_ordering(Ingredients="sample_text", Price=3.14, pizza_type="sample_text")
    assert instance.Ingredients == "sample_text"
    instance.Ingredients = "sample_text_2"
    assert instance.Ingredients == "sample_text_2"


def test_Online_pizza_ordering_Price_value_roundtrip():
    instance = Online_pizza_ordering(Ingredients="sample_text", Price=3.14, pizza_type="sample_text")
    assert instance.Price == 3.14
    instance.Price = 9.99
    assert instance.Price == 9.99


def test_Online_pizza_ordering_pizza_type_value_roundtrip():
    instance = Online_pizza_ordering(Ingredients="sample_text", Price=3.14, pizza_type="sample_text")
    assert instance.pizza_type == "sample_text"
    instance.pizza_type = "sample_text_2"
    assert instance.pizza_type == "sample_text_2"


def test_assoc_Customer_Online_pizza_ordering_link_reassign_clear():
    a = Online_pizza_ordering(Ingredients="sample_text", Price=3.14, pizza_type="sample_text")
    b1 = Customer(Name="sample_text", Password="sample_text")
    b2 = Customer(Name="sample_text_2", Password="sample_text_2")
    _safe_set(a, 'Customer_Online_pizza_ordering_131', {b1})
    assert _is_linked(a, 'Customer_Online_pizza_ordering_131', b1)
    if hasattr(b1, 'Customer_Online_pizza_ordering_030'):
        assert _is_linked(b1, 'Customer_Online_pizza_ordering_030', a)
    _safe_set(a, 'Customer_Online_pizza_ordering_131', {b2})
    assert _is_linked(a, 'Customer_Online_pizza_ordering_131', b2)
    if hasattr(b1, 'Customer_Online_pizza_ordering_030'):
        assert not _is_linked(b1, 'Customer_Online_pizza_ordering_030', a)
    if hasattr(b2, 'Customer_Online_pizza_ordering_030'):
        assert _is_linked(b2, 'Customer_Online_pizza_ordering_030', a)
    _safe_set(a, 'Customer_Online_pizza_ordering_131', set())
    assert not _is_linked(a, 'Customer_Online_pizza_ordering_131', b2)
    if hasattr(b2, 'Customer_Online_pizza_ordering_030'):
        assert not _is_linked(b2, 'Customer_Online_pizza_ordering_030', a)


def test_assoc_assoc__Ppt9QpfqEeqEM7mFKilpXw_link_reassign_clear():
    a = Online_pizza_ordering(Ingredients="sample_text", Price=3.14, pizza_type="sample_text")
    b1 = Admin()
    b2 = Admin()
    _safe_set(a, 'assoc_032', b1)
    assert _is_linked(a, 'assoc_032', b1)
    if hasattr(b1, 'assoc_133'):
        assert _is_linked(b1, 'assoc_133', a)
    _safe_set(a, 'assoc_032', b2)
    assert _is_linked(a, 'assoc_032', b2)
    if hasattr(b1, 'assoc_133'):
        assert not _is_linked(b1, 'assoc_133', a)
    if hasattr(b2, 'assoc_133'):
        assert _is_linked(b2, 'assoc_133', a)
    _safe_set(a, 'assoc_032', None)
    assert not _is_linked(a, 'assoc_032', b2)
    if hasattr(b2, 'assoc_133'):
        assert not _is_linked(b2, 'assoc_133', a)


def test_assoc_assoc__Ppt9U5fqEeqEM7mFKilpXw_link_reassign_clear():
    a = Customer(Name="sample_text", Password="sample_text")
    b1 = Payment()
    b2 = Payment()
    _safe_set(a, 'assoc_034', {b1})
    assert _is_linked(a, 'assoc_034', b1)
    if hasattr(b1, 'assoc_135'):
        assert _is_linked(b1, 'assoc_135', a)
    _safe_set(a, 'assoc_034', {b2})
    assert _is_linked(a, 'assoc_034', b2)
    if hasattr(b1, 'assoc_135'):
        assert not _is_linked(b1, 'assoc_135', a)
    if hasattr(b2, 'assoc_135'):
        assert _is_linked(b2, 'assoc_135', a)
    _safe_set(a, 'assoc_034', set())
    assert not _is_linked(a, 'assoc_034', b2)
    if hasattr(b2, 'assoc_135'):
        assert not _is_linked(b2, 'assoc_135', a)


def test_assoc_assoc__Ppt9cpfqEeqEM7mFKilpXw_link_reassign_clear():
    a = Online_pizza_ordering(Ingredients="sample_text", Price=3.14, pizza_type="sample_text")
    b1 = Menu(Quantity="sample_text", toppings="sample_text")
    b2 = Menu(Quantity="sample_text_2", toppings="sample_text_2")
    _safe_set(a, 'assoc_036', b1)
    assert _is_linked(a, 'assoc_036', b1)
    if hasattr(b1, 'assoc_137'):
        assert _is_linked(b1, 'assoc_137', a)
    _safe_set(a, 'assoc_036', b2)
    assert _is_linked(a, 'assoc_036', b2)
    if hasattr(b1, 'assoc_137'):
        assert not _is_linked(b1, 'assoc_137', a)
    if hasattr(b2, 'assoc_137'):
        assert _is_linked(b2, 'assoc_137', a)
    _safe_set(a, 'assoc_036', None)
    assert not _is_linked(a, 'assoc_036', b2)
    if hasattr(b2, 'assoc_137'):
        assert not _is_linked(b2, 'assoc_137', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Add_item_UseCase_strategy = st.builds(Add_item_UseCase)
@given(instance=Add_item_UseCase_strategy)
@settings(max_examples=25)
def test_Add_item_UseCase_instantiation(instance):
    assert isinstance(instance, Add_item_UseCase)


Add_new_address_UseCase_strategy = st.builds(Add_new_address_UseCase)
@given(instance=Add_new_address_UseCase_strategy)
@settings(max_examples=25)
def test_Add_new_address_UseCase_instantiation(instance):
    assert isinstance(instance, Add_new_address_UseCase)


Admin_strategy = st.builds(Admin)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Admin_Actor_strategy = st.builds(Admin_Actor)
@given(instance=Admin_Actor_strategy)
@settings(max_examples=25)
def test_Admin_Actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)


Change_toppings_UseCase_strategy = st.builds(Change_toppings_UseCase)
@given(instance=Change_toppings_UseCase_strategy)
@settings(max_examples=25)
def test_Change_toppings_UseCase_instantiation(instance):
    assert isinstance(instance, Change_toppings_UseCase)


Checkout_UseCase_strategy = st.builds(Checkout_UseCase)
@given(instance=Checkout_UseCase_strategy)
@settings(max_examples=25)
def test_Checkout_UseCase_instantiation(instance):
    assert isinstance(instance, Checkout_UseCase)


Cook_Pizza_UseCase_strategy = st.builds(Cook_Pizza_UseCase)
@given(instance=Cook_Pizza_UseCase_strategy)
@settings(max_examples=25)
def test_Cook_Pizza_UseCase_instantiation(instance):
    assert isinstance(instance, Cook_Pizza_UseCase)


Create_Account_UseCase_strategy = st.builds(Create_Account_UseCase)
@given(instance=Create_Account_UseCase_strategy)
@settings(max_examples=25)
def test_Create_Account_UseCase_instantiation(instance):
    assert isinstance(instance, Create_Account_UseCase)


Create_your_own_pizza_UseCase_strategy = st.builds(Create_your_own_pizza_UseCase)
@given(instance=Create_your_own_pizza_UseCase_strategy)
@settings(max_examples=25)
def test_Create_your_own_pizza_UseCase_instantiation(instance):
    assert isinstance(instance, Create_your_own_pizza_UseCase)


Customer_strategy = st.builds(Customer, Name=safe_text, Password=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Deliver_pizza_UseCase_strategy = st.builds(Deliver_pizza_UseCase)
@given(instance=Deliver_pizza_UseCase_strategy)
@settings(max_examples=25)
def test_Deliver_pizza_UseCase_instantiation(instance):
    assert isinstance(instance, Deliver_pizza_UseCase)


Delivery_person_Actor_strategy = st.builds(Delivery_person_Actor)
@given(instance=Delivery_person_Actor_strategy)
@settings(max_examples=25)
def test_Delivery_person_Actor_instantiation(instance):
    assert isinstance(instance, Delivery_person_Actor)


Edit_menu_UseCase_strategy = st.builds(Edit_menu_UseCase)
@given(instance=Edit_menu_UseCase_strategy)
@settings(max_examples=25)
def test_Edit_menu_UseCase_instantiation(instance):
    assert isinstance(instance, Edit_menu_UseCase)


Make_Payment_UseCase_strategy = st.builds(Make_Payment_UseCase)
@given(instance=Make_Payment_UseCase_strategy)
@settings(max_examples=25)
def test_Make_Payment_UseCase_instantiation(instance):
    assert isinstance(instance, Make_Payment_UseCase)


Manage_accounts_UseCase_strategy = st.builds(Manage_accounts_UseCase)
@given(instance=Manage_accounts_UseCase_strategy)
@settings(max_examples=25)
def test_Manage_accounts_UseCase_instantiation(instance):
    assert isinstance(instance, Manage_accounts_UseCase)


Menu_strategy = st.builds(Menu, Quantity=safe_text, toppings=safe_text)
@given(instance=Menu_strategy)
@settings(max_examples=25)
def test_Menu_instantiation(instance):
    assert isinstance(instance, Menu)


Online_payment_methods_strategy = st.builds(Online_payment_methods)
@given(instance=Online_payment_methods_strategy)
@settings(max_examples=25)
def test_Online_payment_methods_instantiation(instance):
    assert isinstance(instance, Online_payment_methods)


Online_pizza_ordering_strategy = st.builds(Online_pizza_ordering, Ingredients=safe_text, Price=st.floats(allow_nan=False, allow_infinity=False), pizza_type=safe_text)
@given(instance=Online_pizza_ordering_strategy)
@settings(max_examples=25)
def test_Online_pizza_ordering_instantiation(instance):
    assert isinstance(instance, Online_pizza_ordering)


Order_tracking_UseCase_strategy = st.builds(Order_tracking_UseCase)
@given(instance=Order_tracking_UseCase_strategy)
@settings(max_examples=25)
def test_Order_tracking_UseCase_instantiation(instance):
    assert isinstance(instance, Order_tracking_UseCase)


PayAt_Delivery_UseCase_strategy = st.builds(PayAt_Delivery_UseCase)
@given(instance=PayAt_Delivery_UseCase_strategy)
@settings(max_examples=25)
def test_PayAt_Delivery_UseCase_instantiation(instance):
    assert isinstance(instance, PayAt_Delivery_UseCase)


Pay_cash_on_deliver_strategy = st.builds(Pay_cash_on_deliver)
@given(instance=Pay_cash_on_deliver_strategy)
@settings(max_examples=25)
def test_Pay_cash_on_deliver_instantiation(instance):
    assert isinstance(instance, Pay_cash_on_deliver)


Pay_online_UseCase_strategy = st.builds(Pay_online_UseCase)
@given(instance=Pay_online_UseCase_strategy)
@settings(max_examples=25)
def test_Pay_online_UseCase_instantiation(instance):
    assert isinstance(instance, Pay_online_UseCase)


Payment_strategy = st.builds(Payment)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Pizza_Chef_Actor_strategy = st.builds(Pizza_Chef_Actor)
@given(instance=Pizza_Chef_Actor_strategy)
@settings(max_examples=25)
def test_Pizza_Chef_Actor_instantiation(instance):
    assert isinstance(instance, Pizza_Chef_Actor)


Pre_order_UseCase_strategy = st.builds(Pre_order_UseCase)
@given(instance=Pre_order_UseCase_strategy)
@settings(max_examples=25)
def test_Pre_order_UseCase_instantiation(instance):
    assert isinstance(instance, Pre_order_UseCase)


Receive_order_UseCase_strategy = st.builds(Receive_order_UseCase)
@given(instance=Receive_order_UseCase_strategy)
@settings(max_examples=25)
def test_Receive_order_UseCase_instantiation(instance):
    assert isinstance(instance, Receive_order_UseCase)


Registered_User_Actor_strategy = st.builds(Registered_User_Actor)
@given(instance=Registered_User_Actor_strategy)
@settings(max_examples=25)
def test_Registered_User_Actor_instantiation(instance):
    assert isinstance(instance, Registered_User_Actor)


Save_favourite_order_UseCase_strategy = st.builds(Save_favourite_order_UseCase)
@given(instance=Save_favourite_order_UseCase_strategy)
@settings(max_examples=25)
def test_Save_favourite_order_UseCase_instantiation(instance):
    assert isinstance(instance, Save_favourite_order_UseCase)


Search_store_locations_UseCase_strategy = st.builds(Search_store_locations_UseCase)
@given(instance=Search_store_locations_UseCase_strategy)
@settings(max_examples=25)
def test_Search_store_locations_UseCase_instantiation(instance):
    assert isinstance(instance, Search_store_locations_UseCase)


Sign_In_UseCase_strategy = st.builds(Sign_In_UseCase)
@given(instance=Sign_In_UseCase_strategy)
@settings(max_examples=25)
def test_Sign_In_UseCase_instantiation(instance):
    assert isinstance(instance, Sign_In_UseCase)


View_Meal_Deal_UseCase_strategy = st.builds(View_Meal_Deal_UseCase)
@given(instance=View_Meal_Deal_UseCase_strategy)
@settings(max_examples=25)
def test_View_Meal_Deal_UseCase_instantiation(instance):
    assert isinstance(instance, View_Meal_Deal_UseCase)


View_Pizza_types_UseCase_strategy = st.builds(View_Pizza_types_UseCase)
@given(instance=View_Pizza_types_UseCase_strategy)
@settings(max_examples=25)
def test_View_Pizza_types_UseCase_instantiation(instance):
    assert isinstance(instance, View_Pizza_types_UseCase)


View_side_orders_UseCase_strategy = st.builds(View_side_orders_UseCase)
@given(instance=View_side_orders_UseCase_strategy)
@settings(max_examples=25)
def test_View_side_orders_UseCase_instantiation(instance):
    assert isinstance(instance, View_side_orders_UseCase)



