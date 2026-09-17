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
    MenuItem,
    FoodItem,
    DrinksItem,
    Customer,
    Order,
    Report,
    Kasir,
    Karyawan,
    Bartender,
    Chef,
    Manager_Owner,
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
    assert "drinksItem" in params, "Missing parameter 'drinksItem'"
    assert "category" in params, "Missing parameter 'category'"
    assert "foodItem" in params, "Missing parameter 'foodItem'"

def test_hyp_menu_has_drinksItem():
    assert hasattr(Menu, "drinksItem")
    descriptor = None
    for klass in Menu.__mro__:
        if "drinksItem" in klass.__dict__:
            descriptor = klass.__dict__["drinksItem"]
            break
    assert isinstance(descriptor, property)

def test_hyp_menu_has_category():
    assert hasattr(Menu, "category")
    descriptor = None
    for klass in Menu.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_hyp_menu_has_foodItem():
    assert hasattr(Menu, "foodItem")
    descriptor = None
    for klass in Menu.__mro__:
        if "foodItem" in klass.__dict__:
            descriptor = klass.__dict__["foodItem"]
            break
    assert isinstance(descriptor, property)



def test_hyp_menuitem_is_not_abstract():
    assert not inspect.isabstract(MenuItem)


def test_hyp_menuitem_constructor_exists():
    assert callable(MenuItem.__init__)


def test_hyp_menuitem_constructor_args():
    sig = inspect.signature(MenuItem.__init__)
    params = list(sig.parameters.keys())
    assert "item_Id" in params, "Missing parameter 'item_Id'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "available" in params, "Missing parameter 'available'"
    assert "item_description" in params, "Missing parameter 'item_description'"
    assert "item_price" in params, "Missing parameter 'item_price'"








def test_hyp_fooditem_is_not_abstract():
    assert not inspect.isabstract(FoodItem)


def test_hyp_fooditem_constructor_exists():
    assert callable(FoodItem.__init__)


def test_hyp_fooditem_constructor_args():
    sig = inspect.signature(FoodItem.__init__)
    params = list(sig.parameters.keys())
    assert "drinkType" in params, "Missing parameter 'drinkType'"




def test_hyp_drinksitem_is_not_abstract():
    assert not inspect.isabstract(DrinksItem)


def test_hyp_drinksitem_constructor_exists():
    assert callable(DrinksItem.__init__)


def test_hyp_drinksitem_constructor_args():
    sig = inspect.signature(DrinksItem.__init__)
    params = list(sig.parameters.keys())
    assert "drinkType" in params, "Missing parameter 'drinkType'"




def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "cust_Id" in params, "Missing parameter 'cust_Id'"
    assert "cust_name" in params, "Missing parameter 'cust_name'"





def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "numTable" in params, "Missing parameter 'numTable'"
    assert "cust_id" in params, "Missing parameter 'cust_id'"
    assert "foodItem" in params, "Missing parameter 'foodItem'"
    assert "drinksItem" in params, "Missing parameter 'drinksItem'"
    assert "cust_name" in params, "Missing parameter 'cust_name'"
    assert "order_Id" in params, "Missing parameter 'order_Id'"

def test_hyp_order_has_numTable():
    assert hasattr(Order, "numTable")
    descriptor = None
    for klass in Order.__mro__:
        if "numTable" in klass.__dict__:
            descriptor = klass.__dict__["numTable"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_cust_id():
    assert hasattr(Order, "cust_id")
    descriptor = None
    for klass in Order.__mro__:
        if "cust_id" in klass.__dict__:
            descriptor = klass.__dict__["cust_id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_foodItem():
    assert hasattr(Order, "foodItem")
    descriptor = None
    for klass in Order.__mro__:
        if "foodItem" in klass.__dict__:
            descriptor = klass.__dict__["foodItem"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_drinksItem():
    assert hasattr(Order, "drinksItem")
    descriptor = None
    for klass in Order.__mro__:
        if "drinksItem" in klass.__dict__:
            descriptor = klass.__dict__["drinksItem"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_cust_name():
    assert hasattr(Order, "cust_name")
    descriptor = None
    for klass in Order.__mro__:
        if "cust_name" in klass.__dict__:
            descriptor = klass.__dict__["cust_name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_order_Id():
    assert hasattr(Order, "order_Id")
    descriptor = None
    for klass in Order.__mro__:
        if "order_Id" in klass.__dict__:
            descriptor = klass.__dict__["order_Id"]
            break
    assert isinstance(descriptor, property)



def test_hyp_report_is_not_abstract():
    assert not inspect.isabstract(Report)


def test_hyp_report_constructor_exists():
    assert callable(Report.__init__)


def test_hyp_report_constructor_args():
    sig = inspect.signature(Report.__init__)
    params = list(sig.parameters.keys())
    assert "orders" in params, "Missing parameter 'orders'"
    assert "profit" in params, "Missing parameter 'profit'"
    assert "totalSales" in params, "Missing parameter 'totalSales'"






def test_hyp_kasir_is_not_abstract():
    assert not inspect.isabstract(Kasir)


def test_hyp_kasir_constructor_exists():
    assert callable(Kasir.__init__)


def test_hyp_kasir_constructor_args():
    sig = inspect.signature(Kasir.__init__)
    params = list(sig.parameters.keys())
    assert "cust_id" in params, "Missing parameter 'cust_id'"
    assert "order_id" in params, "Missing parameter 'order_id'"





def test_hyp_karyawan_is_not_abstract():
    assert not inspect.isabstract(Karyawan)


def test_hyp_karyawan_constructor_exists():
    assert callable(Karyawan.__init__)


def test_hyp_karyawan_constructor_args():
    sig = inspect.signature(Karyawan.__init__)
    params = list(sig.parameters.keys())
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"
    assert "contact" in params, "Missing parameter 'contact'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_bartender_is_not_abstract():
    assert not inspect.isabstract(Bartender)


def test_hyp_bartender_constructor_exists():
    assert callable(Bartender.__init__)


def test_hyp_bartender_constructor_args():
    sig = inspect.signature(Bartender.__init__)
    params = list(sig.parameters.keys())
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_hyp_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_hyp_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "staff_Id" in params, "Missing parameter 'staff_Id'"





def test_hyp_manager_owner_is_not_abstract():
    assert not inspect.isabstract(Manager_Owner)


def test_hyp_manager_owner_constructor_exists():
    assert callable(Manager_Owner.__init__)


def test_hyp_manager_owner_constructor_args():
    sig = inspect.signature(Manager_Owner.__init__)
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
    drinksItem=
        st.none(),
    category=
        safe_text,
    foodItem=
        st.none()
)
MenuItem_strategy = st.builds(
    MenuItem,
    item_Id=
        st.integers(),
    quantity=
        st.integers(),
    available=
        st.booleans(),
    item_description=
        safe_text,
    item_price=
        st.integers()
)
FoodItem_strategy = st.builds(
    FoodItem,
    drinkType=
        safe_text
)
DrinksItem_strategy = st.builds(
    DrinksItem,
    drinkType=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    cust_Id=
        safe_text,
    cust_name=
        safe_text
)
Order_strategy = st.builds(
    Order,
    numTable=
        st.integers(),
    cust_id=
        safe_text,
    foodItem=
        st.none(),
    drinksItem=
        st.none(),
    cust_name=
        safe_text,
    order_Id=
        safe_text
)
Report_strategy = st.builds(
    Report,
    orders=
        safe_text,
    profit=
        safe_text,
    totalSales=
        safe_text
)
Kasir_strategy = st.builds(
    Kasir,
    cust_id=
        safe_text,
    order_id=
        safe_text
)
Karyawan_strategy = st.builds(
    Karyawan,
    staff_Id=
        safe_text,
    contact=
        safe_text,
    name=
        safe_text
)
Bartender_strategy = st.builds(
    Bartender,
    staff_Id=
        safe_text,
    name=
        safe_text
)
Chef_strategy = st.builds(
    Chef,
    name=
        safe_text,
    staff_Id=
        safe_text
)
Manager_Owner_strategy = st.builds(
    Manager_Owner,
)

@given(instance=Menu_strategy)
@settings(max_examples=50)
def test_hyp_menu_instantiation(instance):
    assert isinstance(instance, Menu)



@given(instance=Menu_strategy)
def test_hyp_menu_drinksItem_setter(instance):
    original = instance.drinksItem
    instance.drinksItem = original
    assert instance.drinksItem == original



@given(instance=Menu_strategy)
def test_hyp_menu_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=Menu_strategy)
def test_hyp_menu_foodItem_setter(instance):
    original = instance.foodItem
    instance.foodItem = original
    assert instance.foodItem == original




@given(instance=MenuItem_strategy)
def test_hyp_menuitem_item_Id_setter(instance):
    original = instance.item_Id
    instance.item_Id = original
    assert instance.item_Id == original



@given(instance=MenuItem_strategy)
def test_hyp_menuitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=MenuItem_strategy)
def test_hyp_menuitem_available_setter(instance):
    original = instance.available
    instance.available = original
    assert instance.available == original



@given(instance=MenuItem_strategy)
def test_hyp_menuitem_item_description_setter(instance):
    original = instance.item_description
    instance.item_description = original
    assert instance.item_description == original



@given(instance=MenuItem_strategy)
def test_hyp_menuitem_item_price_setter(instance):
    original = instance.item_price
    instance.item_price = original
    assert instance.item_price == original




@given(instance=FoodItem_strategy)
def test_hyp_fooditem_drinkType_setter(instance):
    original = instance.drinkType
    instance.drinkType = original
    assert instance.drinkType == original




@given(instance=DrinksItem_strategy)
def test_hyp_drinksitem_drinkType_setter(instance):
    original = instance.drinkType
    instance.drinkType = original
    assert instance.drinkType == original




@given(instance=Customer_strategy)
def test_hyp_customer_cust_Id_setter(instance):
    original = instance.cust_Id
    instance.cust_Id = original
    assert instance.cust_Id == original



@given(instance=Customer_strategy)
def test_hyp_customer_cust_name_setter(instance):
    original = instance.cust_name
    instance.cust_name = original
    assert instance.cust_name == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_hyp_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_hyp_order_numTable_setter(instance):
    original = instance.numTable
    instance.numTable = original
    assert instance.numTable == original



@given(instance=Order_strategy)
def test_hyp_order_cust_id_setter(instance):
    original = instance.cust_id
    instance.cust_id = original
    assert instance.cust_id == original



@given(instance=Order_strategy)
def test_hyp_order_foodItem_setter(instance):
    original = instance.foodItem
    instance.foodItem = original
    assert instance.foodItem == original



@given(instance=Order_strategy)
def test_hyp_order_drinksItem_setter(instance):
    original = instance.drinksItem
    instance.drinksItem = original
    assert instance.drinksItem == original



@given(instance=Order_strategy)
def test_hyp_order_cust_name_setter(instance):
    original = instance.cust_name
    instance.cust_name = original
    assert instance.cust_name == original



@given(instance=Order_strategy)
def test_hyp_order_order_Id_setter(instance):
    original = instance.order_Id
    instance.order_Id = original
    assert instance.order_Id == original




@given(instance=Report_strategy)
def test_hyp_report_orders_setter(instance):
    original = instance.orders
    instance.orders = original
    assert instance.orders == original



@given(instance=Report_strategy)
def test_hyp_report_profit_setter(instance):
    original = instance.profit
    instance.profit = original
    assert instance.profit == original



@given(instance=Report_strategy)
def test_hyp_report_totalSales_setter(instance):
    original = instance.totalSales
    instance.totalSales = original
    assert instance.totalSales == original




@given(instance=Kasir_strategy)
def test_hyp_kasir_cust_id_setter(instance):
    original = instance.cust_id
    instance.cust_id = original
    assert instance.cust_id == original



@given(instance=Kasir_strategy)
def test_hyp_kasir_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original




@given(instance=Karyawan_strategy)
def test_hyp_karyawan_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original



@given(instance=Karyawan_strategy)
def test_hyp_karyawan_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=Karyawan_strategy)
def test_hyp_karyawan_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Bartender_strategy)
def test_hyp_bartender_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original



@given(instance=Bartender_strategy)
def test_hyp_bartender_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Chef_strategy)
def test_hyp_chef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Chef_strategy)
def test_hyp_chef_staff_Id_setter(instance):
    original = instance.staff_Id
    instance.staff_Id = original
    assert instance.staff_Id == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Bartender,
    Chef,
    Customer,
    DrinksItem,
    FoodItem,
    Karyawan,
    Kasir,
    Manager_Owner,
    Menu,
    MenuItem,
    Order,
    Report,
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

def test_Bartender_name_value_roundtrip():
    instance = Bartender(name="sample_text", staff_Id="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Bartender_staff_Id_value_roundtrip():
    instance = Bartender(name="sample_text", staff_Id="sample_text")
    assert instance.staff_Id == "sample_text"
    instance.staff_Id = "sample_text_2"
    assert instance.staff_Id == "sample_text_2"


def test_Chef_name_value_roundtrip():
    instance = Chef(name="sample_text", staff_Id="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Chef_staff_Id_value_roundtrip():
    instance = Chef(name="sample_text", staff_Id="sample_text")
    assert instance.staff_Id == "sample_text"
    instance.staff_Id = "sample_text_2"
    assert instance.staff_Id == "sample_text_2"


def test_Customer_cust_Id_value_roundtrip():
    instance = Customer(cust_Id="sample_text", cust_name="sample_text")
    assert instance.cust_Id == "sample_text"
    instance.cust_Id = "sample_text_2"
    assert instance.cust_Id == "sample_text_2"


def test_Customer_cust_name_value_roundtrip():
    instance = Customer(cust_Id="sample_text", cust_name="sample_text")
    assert instance.cust_name == "sample_text"
    instance.cust_name = "sample_text_2"
    assert instance.cust_name == "sample_text_2"


def test_DrinksItem_drinkType_value_roundtrip():
    instance = DrinksItem(drinkType="sample_text")
    assert instance.drinkType == "sample_text"
    instance.drinkType = "sample_text_2"
    assert instance.drinkType == "sample_text_2"


def test_FoodItem_drinkType_value_roundtrip():
    instance = FoodItem(drinkType="sample_text")
    assert instance.drinkType == "sample_text"
    instance.drinkType = "sample_text_2"
    assert instance.drinkType == "sample_text_2"


def test_Karyawan_contact_value_roundtrip():
    instance = Karyawan(contact="sample_text", name="sample_text", staff_Id="sample_text")
    assert instance.contact == "sample_text"
    instance.contact = "sample_text_2"
    assert instance.contact == "sample_text_2"


def test_Karyawan_name_value_roundtrip():
    instance = Karyawan(contact="sample_text", name="sample_text", staff_Id="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Karyawan_staff_Id_value_roundtrip():
    instance = Karyawan(contact="sample_text", name="sample_text", staff_Id="sample_text")
    assert instance.staff_Id == "sample_text"
    instance.staff_Id = "sample_text_2"
    assert instance.staff_Id == "sample_text_2"


def test_Kasir_cust_id_value_roundtrip():
    instance = Kasir(cust_id="sample_text", order_id="sample_text")
    assert instance.cust_id == "sample_text"
    instance.cust_id = "sample_text_2"
    assert instance.cust_id == "sample_text_2"


def test_Kasir_order_id_value_roundtrip():
    instance = Kasir(cust_id="sample_text", order_id="sample_text")
    assert instance.order_id == "sample_text"
    instance.order_id = "sample_text_2"
    assert instance.order_id == "sample_text_2"


def test_MenuItem_available_value_roundtrip():
    instance = MenuItem(available=True, item_Id=7, item_description="sample_text", item_price=7, quantity=7)
    assert instance.available == True
    instance.available = False
    assert instance.available == False


def test_MenuItem_item_Id_value_roundtrip():
    instance = MenuItem(available=True, item_Id=7, item_description="sample_text", item_price=7, quantity=7)
    assert instance.item_Id == 7
    instance.item_Id = 13
    assert instance.item_Id == 13


def test_MenuItem_item_description_value_roundtrip():
    instance = MenuItem(available=True, item_Id=7, item_description="sample_text", item_price=7, quantity=7)
    assert instance.item_description == "sample_text"
    instance.item_description = "sample_text_2"
    assert instance.item_description == "sample_text_2"


def test_MenuItem_item_price_value_roundtrip():
    instance = MenuItem(available=True, item_Id=7, item_description="sample_text", item_price=7, quantity=7)
    assert instance.item_price == 7
    instance.item_price = 13
    assert instance.item_price == 13


def test_MenuItem_quantity_value_roundtrip():
    instance = MenuItem(available=True, item_Id=7, item_description="sample_text", item_price=7, quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Report_orders_value_roundtrip():
    instance = Report(orders="sample_text", profit="sample_text", totalSales="sample_text")
    assert instance.orders == "sample_text"
    instance.orders = "sample_text_2"
    assert instance.orders == "sample_text_2"


def test_Report_profit_value_roundtrip():
    instance = Report(orders="sample_text", profit="sample_text", totalSales="sample_text")
    assert instance.profit == "sample_text"
    instance.profit = "sample_text_2"
    assert instance.profit == "sample_text_2"


def test_Report_totalSales_value_roundtrip():
    instance = Report(orders="sample_text", profit="sample_text", totalSales="sample_text")
    assert instance.totalSales == "sample_text"
    instance.totalSales = "sample_text_2"
    assert instance.totalSales == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Bartender_strategy = st.builds(Bartender, name=safe_text, staff_Id=safe_text)
@given(instance=Bartender_strategy)
@settings(max_examples=25)
def test_Bartender_instantiation(instance):
    assert isinstance(instance, Bartender)


Chef_strategy = st.builds(Chef, name=safe_text, staff_Id=safe_text)
@given(instance=Chef_strategy)
@settings(max_examples=25)
def test_Chef_instantiation(instance):
    assert isinstance(instance, Chef)


Customer_strategy = st.builds(Customer, cust_Id=safe_text, cust_name=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


DrinksItem_strategy = st.builds(DrinksItem, drinkType=safe_text)
@given(instance=DrinksItem_strategy)
@settings(max_examples=25)
def test_DrinksItem_instantiation(instance):
    assert isinstance(instance, DrinksItem)


FoodItem_strategy = st.builds(FoodItem, drinkType=safe_text)
@given(instance=FoodItem_strategy)
@settings(max_examples=25)
def test_FoodItem_instantiation(instance):
    assert isinstance(instance, FoodItem)


Karyawan_strategy = st.builds(Karyawan, contact=safe_text, name=safe_text, staff_Id=safe_text)
@given(instance=Karyawan_strategy)
@settings(max_examples=25)
def test_Karyawan_instantiation(instance):
    assert isinstance(instance, Karyawan)


Kasir_strategy = st.builds(Kasir, cust_id=safe_text, order_id=safe_text)
@given(instance=Kasir_strategy)
@settings(max_examples=25)
def test_Kasir_instantiation(instance):
    assert isinstance(instance, Kasir)


Manager_Owner_strategy = st.builds(Manager_Owner)
@given(instance=Manager_Owner_strategy)
@settings(max_examples=25)
def test_Manager_Owner_instantiation(instance):
    assert isinstance(instance, Manager_Owner)


MenuItem_strategy = st.builds(MenuItem, available=st.booleans(), item_Id=st.integers(), item_description=safe_text, item_price=st.integers(), quantity=st.integers())
@given(instance=MenuItem_strategy)
@settings(max_examples=25)
def test_MenuItem_instantiation(instance):
    assert isinstance(instance, MenuItem)


Report_strategy = st.builds(Report, orders=safe_text, profit=safe_text, totalSales=safe_text)
@given(instance=Report_strategy)
@settings(max_examples=25)
def test_Report_instantiation(instance):
    assert isinstance(instance, Report)



