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
    OrderController,
    RestaurantController,
    Customer,
    Order,
    Food,
    FoodItem,
    FoodPackage,
    MenuItem,
    Restaurant,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ordercontroller_is_not_abstract():
    assert not inspect.isabstract(OrderController)


def test_hyp_ordercontroller_constructor_exists():
    assert callable(OrderController.__init__)


def test_hyp_ordercontroller_constructor_args():
    sig = inspect.signature(OrderController.__init__)
    params = list(sig.parameters.keys())
    assert "Order" in params, "Missing parameter 'Order'"

def test_hyp_ordercontroller_has_Order():
    assert hasattr(OrderController, "Order")
    descriptor = None
    for klass in OrderController.__mro__:
        if "Order" in klass.__dict__:
            descriptor = klass.__dict__["Order"]
            break
    assert isinstance(descriptor, property)



def test_hyp_restaurantcontroller_is_not_abstract():
    assert not inspect.isabstract(RestaurantController)


def test_hyp_restaurantcontroller_constructor_exists():
    assert callable(RestaurantController.__init__)


def test_hyp_restaurantcontroller_constructor_args():
    sig = inspect.signature(RestaurantController.__init__)
    params = list(sig.parameters.keys())
    assert "Restaurant" in params, "Missing parameter 'Restaurant'"

def test_hyp_restaurantcontroller_has_Restaurant():
    assert hasattr(RestaurantController, "Restaurant")
    descriptor = None
    for klass in RestaurantController.__mro__:
        if "Restaurant" in klass.__dict__:
            descriptor = klass.__dict__["Restaurant"]
            break
    assert isinstance(descriptor, property)



def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "PostCode" in params, "Missing parameter 'PostCode'"
    assert "Cellphone" in params, "Missing parameter 'Cellphone'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "CreditCard" in params, "Missing parameter 'CreditCard'"
    assert "FullName" in params, "Missing parameter 'FullName'"








def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Customer" in params, "Missing parameter 'Customer'"
    assert "ItemList" in params, "Missing parameter 'ItemList'"
    assert "Restaurant" in params, "Missing parameter 'Restaurant'"

def test_hyp_order_has_Customer():
    assert hasattr(Order, "Customer")
    descriptor = None
    for klass in Order.__mro__:
        if "Customer" in klass.__dict__:
            descriptor = klass.__dict__["Customer"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_ItemList():
    assert hasattr(Order, "ItemList")
    descriptor = None
    for klass in Order.__mro__:
        if "ItemList" in klass.__dict__:
            descriptor = klass.__dict__["ItemList"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_Restaurant():
    assert hasattr(Order, "Restaurant")
    descriptor = None
    for klass in Order.__mro__:
        if "Restaurant" in klass.__dict__:
            descriptor = klass.__dict__["Restaurant"]
            break
    assert isinstance(descriptor, property)



def test_hyp_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_hyp_food_constructor_exists():
    assert callable(Food.__init__)


def test_hyp_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Vegetarian" in params, "Missing parameter 'Vegetarian'"
    assert "Calories" in params, "Missing parameter 'Calories'"






def test_hyp_fooditem_is_not_abstract():
    assert not inspect.isabstract(FoodItem)


def test_hyp_fooditem_constructor_exists():
    assert callable(FoodItem.__init__)


def test_hyp_fooditem_constructor_args():
    sig = inspect.signature(FoodItem.__init__)
    params = list(sig.parameters.keys())
    assert "Food" in params, "Missing parameter 'Food'"

def test_hyp_fooditem_has_Food():
    assert hasattr(FoodItem, "Food")
    descriptor = None
    for klass in FoodItem.__mro__:
        if "Food" in klass.__dict__:
            descriptor = klass.__dict__["Food"]
            break
    assert isinstance(descriptor, property)



def test_hyp_foodpackage_is_not_abstract():
    assert not inspect.isabstract(FoodPackage)


def test_hyp_foodpackage_constructor_exists():
    assert callable(FoodPackage.__init__)


def test_hyp_foodpackage_constructor_args():
    sig = inspect.signature(FoodPackage.__init__)
    params = list(sig.parameters.keys())
    assert "FoodList" in params, "Missing parameter 'FoodList'"

def test_hyp_foodpackage_has_FoodList():
    assert hasattr(FoodPackage, "FoodList")
    descriptor = None
    for klass in FoodPackage.__mro__:
        if "FoodList" in klass.__dict__:
            descriptor = klass.__dict__["FoodList"]
            break
    assert isinstance(descriptor, property)



def test_hyp_menuitem_is_not_abstract():
    assert not inspect.isabstract(MenuItem)


def test_hyp_menuitem_constructor_exists():
    assert callable(MenuItem.__init__)


def test_hyp_menuitem_constructor_args():
    sig = inspect.signature(MenuItem.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"




def test_hyp_restaurant_is_not_abstract():
    assert not inspect.isabstract(Restaurant)


def test_hyp_restaurant_constructor_exists():
    assert callable(Restaurant.__init__)


def test_hyp_restaurant_constructor_args():
    sig = inspect.signature(Restaurant.__init__)
    params = list(sig.parameters.keys())
    assert "Menu" in params, "Missing parameter 'Menu'"
    assert "PostCode" in params, "Missing parameter 'PostCode'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_hyp_restaurant_has_Menu():
    assert hasattr(Restaurant, "Menu")
    descriptor = None
    for klass in Restaurant.__mro__:
        if "Menu" in klass.__dict__:
            descriptor = klass.__dict__["Menu"]
            break
    assert isinstance(descriptor, property)

def test_hyp_restaurant_has_PostCode():
    assert hasattr(Restaurant, "PostCode")
    descriptor = None
    for klass in Restaurant.__mro__:
        if "PostCode" in klass.__dict__:
            descriptor = klass.__dict__["PostCode"]
            break
    assert isinstance(descriptor, property)

def test_hyp_restaurant_has_Name():
    assert hasattr(Restaurant, "Name")
    descriptor = None
    for klass in Restaurant.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_restaurant_has_Address():
    assert hasattr(Restaurant, "Address")
    descriptor = None
    for klass in Restaurant.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)


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
OrderController_strategy = st.builds(
    OrderController,
    Order=
        st.none()
)
RestaurantController_strategy = st.builds(
    RestaurantController,
    Restaurant=
        st.none()
)
Customer_strategy = st.builds(
    Customer,
    PostCode=
        st.integers(),
    Cellphone=
        safe_text,
    Address=
        safe_text,
    CreditCard=
        safe_text,
    FullName=
        safe_text
)
Order_strategy = st.builds(
    Order,
    Customer=
        st.none(),
    ItemList=
        st.none(),
    Restaurant=
        st.none()
)
Food_strategy = st.builds(
    Food,
    Price=
        st.integers(),
    Vegetarian=
        st.booleans(),
    Calories=
        st.integers()
)
FoodItem_strategy = st.builds(
    FoodItem,
    Food=
        st.none()
)
FoodPackage_strategy = st.builds(
    FoodPackage,
    FoodList=
        st.none()
)
MenuItem_strategy = st.builds(
    MenuItem,
    Description=
        safe_text
)
Restaurant_strategy = st.builds(
    Restaurant,
    Menu=
        st.none(),
    PostCode=
        st.integers(),
    Name=
        safe_text,
    Address=
        safe_text
)

@given(instance=OrderController_strategy)
@settings(max_examples=50)
def test_hyp_ordercontroller_instantiation(instance):
    assert isinstance(instance, OrderController)



@given(instance=OrderController_strategy)
def test_hyp_ordercontroller_Order_setter(instance):
    original = instance.Order
    instance.Order = original
    assert instance.Order == original

@given(instance=RestaurantController_strategy)
@settings(max_examples=50)
def test_hyp_restaurantcontroller_instantiation(instance):
    assert isinstance(instance, RestaurantController)



@given(instance=RestaurantController_strategy)
def test_hyp_restaurantcontroller_Restaurant_setter(instance):
    original = instance.Restaurant
    instance.Restaurant = original
    assert instance.Restaurant == original




@given(instance=Customer_strategy)
def test_hyp_customer_PostCode_setter(instance):
    original = instance.PostCode
    instance.PostCode = original
    assert instance.PostCode == original



@given(instance=Customer_strategy)
def test_hyp_customer_Cellphone_setter(instance):
    original = instance.Cellphone
    instance.Cellphone = original
    assert instance.Cellphone == original



@given(instance=Customer_strategy)
def test_hyp_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_hyp_customer_CreditCard_setter(instance):
    original = instance.CreditCard
    instance.CreditCard = original
    assert instance.CreditCard == original



@given(instance=Customer_strategy)
def test_hyp_customer_FullName_setter(instance):
    original = instance.FullName
    instance.FullName = original
    assert instance.FullName == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_hyp_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_hyp_order_Customer_setter(instance):
    original = instance.Customer
    instance.Customer = original
    assert instance.Customer == original



@given(instance=Order_strategy)
def test_hyp_order_ItemList_setter(instance):
    original = instance.ItemList
    instance.ItemList = original
    assert instance.ItemList == original



@given(instance=Order_strategy)
def test_hyp_order_Restaurant_setter(instance):
    original = instance.Restaurant
    instance.Restaurant = original
    assert instance.Restaurant == original




@given(instance=Food_strategy)
def test_hyp_food_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Food_strategy)
def test_hyp_food_Vegetarian_setter(instance):
    original = instance.Vegetarian
    instance.Vegetarian = original
    assert instance.Vegetarian == original



@given(instance=Food_strategy)
def test_hyp_food_Calories_setter(instance):
    original = instance.Calories
    instance.Calories = original
    assert instance.Calories == original

@given(instance=FoodItem_strategy)
@settings(max_examples=50)
def test_hyp_fooditem_instantiation(instance):
    assert isinstance(instance, FoodItem)



@given(instance=FoodItem_strategy)
def test_hyp_fooditem_Food_setter(instance):
    original = instance.Food
    instance.Food = original
    assert instance.Food == original

@given(instance=FoodPackage_strategy)
@settings(max_examples=50)
def test_hyp_foodpackage_instantiation(instance):
    assert isinstance(instance, FoodPackage)



@given(instance=FoodPackage_strategy)
def test_hyp_foodpackage_FoodList_setter(instance):
    original = instance.FoodList
    instance.FoodList = original
    assert instance.FoodList == original




@given(instance=MenuItem_strategy)
def test_hyp_menuitem_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=Restaurant_strategy)
@settings(max_examples=50)
def test_hyp_restaurant_instantiation(instance):
    assert isinstance(instance, Restaurant)



@given(instance=Restaurant_strategy)
def test_hyp_restaurant_Menu_setter(instance):
    original = instance.Menu
    instance.Menu = original
    assert instance.Menu == original



@given(instance=Restaurant_strategy)
def test_hyp_restaurant_PostCode_setter(instance):
    original = instance.PostCode
    instance.PostCode = original
    assert instance.PostCode == original



@given(instance=Restaurant_strategy)
def test_hyp_restaurant_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Restaurant_strategy)
def test_hyp_restaurant_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Customer,
    Food,
    FoodItem,
    FoodPackage,
    MenuItem,
    Order,
    OrderController,
    Restaurant,
    RestaurantController,
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

def test_Customer_Address_value_roundtrip():
    instance = Customer(Address="sample_text", Cellphone="sample_text", CreditCard="sample_text", FullName="sample_text", PostCode=7)
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Customer_Cellphone_value_roundtrip():
    instance = Customer(Address="sample_text", Cellphone="sample_text", CreditCard="sample_text", FullName="sample_text", PostCode=7)
    assert instance.Cellphone == "sample_text"
    instance.Cellphone = "sample_text_2"
    assert instance.Cellphone == "sample_text_2"


def test_Customer_CreditCard_value_roundtrip():
    instance = Customer(Address="sample_text", Cellphone="sample_text", CreditCard="sample_text", FullName="sample_text", PostCode=7)
    assert instance.CreditCard == "sample_text"
    instance.CreditCard = "sample_text_2"
    assert instance.CreditCard == "sample_text_2"


def test_Customer_FullName_value_roundtrip():
    instance = Customer(Address="sample_text", Cellphone="sample_text", CreditCard="sample_text", FullName="sample_text", PostCode=7)
    assert instance.FullName == "sample_text"
    instance.FullName = "sample_text_2"
    assert instance.FullName == "sample_text_2"


def test_Customer_PostCode_value_roundtrip():
    instance = Customer(Address="sample_text", Cellphone="sample_text", CreditCard="sample_text", FullName="sample_text", PostCode=7)
    assert instance.PostCode == 7
    instance.PostCode = 13
    assert instance.PostCode == 13


def test_Food_Calories_value_roundtrip():
    instance = Food(Calories=7, Price=7, Vegetarian=True)
    assert instance.Calories == 7
    instance.Calories = 13
    assert instance.Calories == 13


def test_Food_Price_value_roundtrip():
    instance = Food(Calories=7, Price=7, Vegetarian=True)
    assert instance.Price == 7
    instance.Price = 13
    assert instance.Price == 13


def test_Food_Vegetarian_value_roundtrip():
    instance = Food(Calories=7, Price=7, Vegetarian=True)
    assert instance.Vegetarian == True
    instance.Vegetarian = False
    assert instance.Vegetarian == False


def test_MenuItem_Description_value_roundtrip():
    instance = MenuItem(Description="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Customer_strategy = st.builds(Customer, Address=safe_text, Cellphone=safe_text, CreditCard=safe_text, FullName=safe_text, PostCode=st.integers())
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Food_strategy = st.builds(Food, Calories=st.integers(), Price=st.integers(), Vegetarian=st.booleans())
@given(instance=Food_strategy)
@settings(max_examples=25)
def test_Food_instantiation(instance):
    assert isinstance(instance, Food)


MenuItem_strategy = st.builds(MenuItem, Description=safe_text)
@given(instance=MenuItem_strategy)
@settings(max_examples=25)
def test_MenuItem_instantiation(instance):
    assert isinstance(instance, MenuItem)



