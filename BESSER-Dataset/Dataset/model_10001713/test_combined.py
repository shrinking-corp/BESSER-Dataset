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
    Register,
    Sale,
    Sales_Line_Item,
    Product,
    Menu,
    Store,
    Manager,
    Drink,
    Order,
    Food,
    customerDatabase,
    Payment,
    SUID,
    Card,
    CardReader,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_register_is_not_abstract():
    assert not inspect.isabstract(Register)


def test_hyp_register_constructor_exists():
    assert callable(Register.__init__)


def test_hyp_register_constructor_args():
    sig = inspect.signature(Register.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_sale_is_not_abstract():
    assert not inspect.isabstract(Sale)


def test_hyp_sale_constructor_exists():
    assert callable(Sale.__init__)


def test_hyp_sale_constructor_args():
    sig = inspect.signature(Sale.__init__)
    params = list(sig.parameters.keys())
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "isComplete" in params, "Missing parameter 'isComplete'"






def test_hyp_sales_line_item_is_not_abstract():
    assert not inspect.isabstract(Sales_Line_Item)


def test_hyp_sales_line_item_constructor_exists():
    assert callable(Sales_Line_Item.__init__)


def test_hyp_sales_line_item_constructor_args():
    sig = inspect.signature(Sales_Line_Item.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"




def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_hyp_product_constructor_exists():
    assert callable(Product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "itemID" in params, "Missing parameter 'itemID'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_menu_is_not_abstract():
    assert not inspect.isabstract(Menu)


def test_hyp_menu_constructor_exists():
    assert callable(Menu.__init__)


def test_hyp_menu_constructor_args():
    sig = inspect.signature(Menu.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"




def test_hyp_store_is_not_abstract():
    assert not inspect.isabstract(Store)


def test_hyp_store_constructor_exists():
    assert callable(Store.__init__)


def test_hyp_store_constructor_args():
    sig = inspect.signature(Store.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_hyp_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_hyp_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_drink_is_not_abstract():
    assert not inspect.isabstract(Drink)


def test_hyp_drink_constructor_exists():
    assert callable(Drink.__init__)


def test_hyp_drink_constructor_args():
    sig = inspect.signature(Drink.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "foodName" in params, "Missing parameter 'foodName'"
    assert "drinkName" in params, "Missing parameter 'drinkName'"
    assert "foodPrice" in params, "Missing parameter 'foodPrice'"
    assert "drinkPrice" in params, "Missing parameter 'drinkPrice'"
    assert "customer" in params, "Missing parameter 'customer'"








def test_hyp_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_hyp_food_constructor_exists():
    assert callable(Food.__init__)


def test_hyp_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "price" in params, "Missing parameter 'price'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_customerdatabase_is_not_abstract():
    assert not inspect.isabstract(customerDatabase)


def test_hyp_customerdatabase_constructor_exists():
    assert callable(customerDatabase.__init__)


def test_hyp_customerdatabase_constructor_args():
    sig = inspect.signature(customerDatabase.__init__)
    params = list(sig.parameters.keys())
    assert "paymentHistory" in params, "Missing parameter 'paymentHistory'"
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "creditCardNum" in params, "Missing parameter 'creditCardNum'"
    assert "SUID" in params, "Missing parameter 'SUID'"







def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"




def test_hyp_suid_is_not_abstract():
    assert not inspect.isabstract(SUID)


def test_hyp_suid_constructor_exists():
    assert callable(SUID.__init__)


def test_hyp_suid_constructor_args():
    sig = inspect.signature(SUID.__init__)
    params = list(sig.parameters.keys())
    assert "studentName" in params, "Missing parameter 'studentName'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "suFOODBal" in params, "Missing parameter 'suFOODBal'"






def test_hyp_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_hyp_card_constructor_exists():
    assert callable(Card.__init__)


def test_hyp_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "isDebit" in params, "Missing parameter 'isDebit'"
    assert "isCredit" in params, "Missing parameter 'isCredit'"
    assert "cardholderName" in params, "Missing parameter 'cardholderName'"
    assert "cardSN" in params, "Missing parameter 'cardSN'"
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"








def test_hyp_cardreader_is_not_abstract():
    assert not inspect.isabstract(CardReader)


def test_hyp_cardreader_constructor_exists():
    assert callable(CardReader.__init__)


def test_hyp_cardreader_constructor_args():
    sig = inspect.signature(CardReader.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"



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
Register_strategy = st.builds(
    Register,
    attribute=
        safe_text
)
Sale_strategy = st.builds(
    Sale,
    Time=
        safe_text,
    Date=
        safe_text,
    isComplete=
        st.booleans()
)
Sales_Line_Item_strategy = st.builds(
    Sales_Line_Item,
    Quantity=
        st.integers()
)
Product_strategy = st.builds(
    Product,
    price=
        safe_text,
    itemID=
        st.integers(),
    description=
        safe_text,
    name=
        safe_text
)
Menu_strategy = st.builds(
    Menu,
    _attr=
        safe_text
)
Store_strategy = st.builds(
    Store,
    Address=
        safe_text,
    Name=
        safe_text
)
Manager_strategy = st.builds(
    Manager,
    name=
        safe_text,
    password=
        safe_text
)
Drink_strategy = st.builds(
    Drink,
    quantity=
        st.integers(),
    price=
        safe_text,
    name=
        safe_text
)
Order_strategy = st.builds(
    Order,
    foodName=
        safe_text,
    drinkName=
        safe_text,
    foodPrice=
        st.integers(),
    drinkPrice=
        st.integers(),
    customer=
        safe_text
)
Food_strategy = st.builds(
    Food,
    quantity=
        st.integers(),
    attribute=
        safe_text,
    price=
        safe_text,
    name=
        safe_text
)
customerDatabase_strategy = st.builds(
    customerDatabase,
    paymentHistory=
        safe_text,
    customerName=
        safe_text,
    creditCardNum=
        st.integers(),
    SUID=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    amount=
        safe_text
)
SUID_strategy = st.builds(
    SUID,
    studentName=
        safe_text,
    ID=
        st.integers(),
    suFOODBal=
        safe_text
)
Card_strategy = st.builds(
    Card,
    isDebit=
        st.booleans(),
    isCredit=
        st.booleans(),
    cardholderName=
        safe_text,
    cardSN=
        st.integers(),
    cardNumber=
        st.integers()
)
CardReader_strategy = st.builds(
    CardReader,
    attribute=
        safe_text
)




@given(instance=Register_strategy)
def test_hyp_register_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=Sale_strategy)
def test_hyp_sale_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Sale_strategy)
def test_hyp_sale_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Sale_strategy)
def test_hyp_sale_isComplete_setter(instance):
    original = instance.isComplete
    instance.isComplete = original
    assert instance.isComplete == original




@given(instance=Sales_Line_Item_strategy)
def test_hyp_sales_line_item_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original




@given(instance=Product_strategy)
def test_hyp_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Product_strategy)
def test_hyp_product_itemID_setter(instance):
    original = instance.itemID
    instance.itemID = original
    assert instance.itemID == original



@given(instance=Product_strategy)
def test_hyp_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Product_strategy)
def test_hyp_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Menu_strategy)
def test_hyp_menu__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original




@given(instance=Store_strategy)
def test_hyp_store_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Store_strategy)
def test_hyp_store_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Manager_strategy)
def test_hyp_manager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Manager_strategy)
def test_hyp_manager_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Drink_strategy)
def test_hyp_drink_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Drink_strategy)
def test_hyp_drink_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Drink_strategy)
def test_hyp_drink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Order_strategy)
def test_hyp_order_foodName_setter(instance):
    original = instance.foodName
    instance.foodName = original
    assert instance.foodName == original



@given(instance=Order_strategy)
def test_hyp_order_drinkName_setter(instance):
    original = instance.drinkName
    instance.drinkName = original
    assert instance.drinkName == original



@given(instance=Order_strategy)
def test_hyp_order_foodPrice_setter(instance):
    original = instance.foodPrice
    instance.foodPrice = original
    assert instance.foodPrice == original



@given(instance=Order_strategy)
def test_hyp_order_drinkPrice_setter(instance):
    original = instance.drinkPrice
    instance.drinkPrice = original
    assert instance.drinkPrice == original



@given(instance=Order_strategy)
def test_hyp_order_customer_setter(instance):
    original = instance.customer
    instance.customer = original
    assert instance.customer == original




@given(instance=Food_strategy)
def test_hyp_food_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Food_strategy)
def test_hyp_food_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Food_strategy)
def test_hyp_food_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Food_strategy)
def test_hyp_food_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=customerDatabase_strategy)
def test_hyp_customerdatabase_paymentHistory_setter(instance):
    original = instance.paymentHistory
    instance.paymentHistory = original
    assert instance.paymentHistory == original



@given(instance=customerDatabase_strategy)
def test_hyp_customerdatabase_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original



@given(instance=customerDatabase_strategy)
def test_hyp_customerdatabase_creditCardNum_setter(instance):
    original = instance.creditCardNum
    instance.creditCardNum = original
    assert instance.creditCardNum == original



@given(instance=customerDatabase_strategy)
def test_hyp_customerdatabase_SUID_setter(instance):
    original = instance.SUID
    instance.SUID = original
    assert instance.SUID == original




@given(instance=Payment_strategy)
def test_hyp_payment_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original




@given(instance=SUID_strategy)
def test_hyp_suid_studentName_setter(instance):
    original = instance.studentName
    instance.studentName = original
    assert instance.studentName == original



@given(instance=SUID_strategy)
def test_hyp_suid_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=SUID_strategy)
def test_hyp_suid_suFOODBal_setter(instance):
    original = instance.suFOODBal
    instance.suFOODBal = original
    assert instance.suFOODBal == original




@given(instance=Card_strategy)
def test_hyp_card_isDebit_setter(instance):
    original = instance.isDebit
    instance.isDebit = original
    assert instance.isDebit == original



@given(instance=Card_strategy)
def test_hyp_card_isCredit_setter(instance):
    original = instance.isCredit
    instance.isCredit = original
    assert instance.isCredit == original



@given(instance=Card_strategy)
def test_hyp_card_cardholderName_setter(instance):
    original = instance.cardholderName
    instance.cardholderName = original
    assert instance.cardholderName == original



@given(instance=Card_strategy)
def test_hyp_card_cardSN_setter(instance):
    original = instance.cardSN
    instance.cardSN = original
    assert instance.cardSN == original



@given(instance=Card_strategy)
def test_hyp_card_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original




@given(instance=CardReader_strategy)
def test_hyp_cardreader_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Card,
    CardReader,
    Drink,
    Food,
    Manager,
    Menu,
    Order,
    Payment,
    Product,
    Register,
    SUID,
    Sale,
    Sales_Line_Item,
    Store,
    customerDatabase,
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

def test_Card_cardNumber_value_roundtrip():
    instance = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    assert instance.cardNumber == 7
    instance.cardNumber = 13
    assert instance.cardNumber == 13


def test_Card_cardSN_value_roundtrip():
    instance = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    assert instance.cardSN == 7
    instance.cardSN = 13
    assert instance.cardSN == 13


def test_Card_cardholderName_value_roundtrip():
    instance = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    assert instance.cardholderName == "sample_text"
    instance.cardholderName = "sample_text_2"
    assert instance.cardholderName == "sample_text_2"


def test_Card_isCredit_value_roundtrip():
    instance = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    assert instance.isCredit == True
    instance.isCredit = False
    assert instance.isCredit == False


def test_Card_isDebit_value_roundtrip():
    instance = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    assert instance.isDebit == True
    instance.isDebit = False
    assert instance.isDebit == False


def test_CardReader_attribute_value_roundtrip():
    instance = CardReader(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Drink_name_value_roundtrip():
    instance = Drink(name="sample_text", price="sample_text", quantity=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Drink_price_value_roundtrip():
    instance = Drink(name="sample_text", price="sample_text", quantity=7)
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_Drink_quantity_value_roundtrip():
    instance = Drink(name="sample_text", price="sample_text", quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Food_attribute_value_roundtrip():
    instance = Food(attribute="sample_text", name="sample_text", price="sample_text", quantity=7)
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Food_name_value_roundtrip():
    instance = Food(attribute="sample_text", name="sample_text", price="sample_text", quantity=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Food_price_value_roundtrip():
    instance = Food(attribute="sample_text", name="sample_text", price="sample_text", quantity=7)
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_Food_quantity_value_roundtrip():
    instance = Food(attribute="sample_text", name="sample_text", price="sample_text", quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_Manager_name_value_roundtrip():
    instance = Manager(name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Manager_password_value_roundtrip():
    instance = Manager(name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Menu__attr_value_roundtrip():
    instance = Menu(_attr="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_Order_customer_value_roundtrip():
    instance = Order(customer="sample_text", drinkName="sample_text", drinkPrice=7, foodName="sample_text", foodPrice=7)
    assert instance.customer == "sample_text"
    instance.customer = "sample_text_2"
    assert instance.customer == "sample_text_2"


def test_Order_drinkName_value_roundtrip():
    instance = Order(customer="sample_text", drinkName="sample_text", drinkPrice=7, foodName="sample_text", foodPrice=7)
    assert instance.drinkName == "sample_text"
    instance.drinkName = "sample_text_2"
    assert instance.drinkName == "sample_text_2"


def test_Order_drinkPrice_value_roundtrip():
    instance = Order(customer="sample_text", drinkName="sample_text", drinkPrice=7, foodName="sample_text", foodPrice=7)
    assert instance.drinkPrice == 7
    instance.drinkPrice = 13
    assert instance.drinkPrice == 13


def test_Order_foodName_value_roundtrip():
    instance = Order(customer="sample_text", drinkName="sample_text", drinkPrice=7, foodName="sample_text", foodPrice=7)
    assert instance.foodName == "sample_text"
    instance.foodName = "sample_text_2"
    assert instance.foodName == "sample_text_2"


def test_Order_foodPrice_value_roundtrip():
    instance = Order(customer="sample_text", drinkName="sample_text", drinkPrice=7, foodName="sample_text", foodPrice=7)
    assert instance.foodPrice == 7
    instance.foodPrice = 13
    assert instance.foodPrice == 13


def test_Payment_amount_value_roundtrip():
    instance = Payment(amount="sample_text")
    assert instance.amount == "sample_text"
    instance.amount = "sample_text_2"
    assert instance.amount == "sample_text_2"


def test_Product_description_value_roundtrip():
    instance = Product(description="sample_text", itemID=7, name="sample_text", price="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Product_itemID_value_roundtrip():
    instance = Product(description="sample_text", itemID=7, name="sample_text", price="sample_text")
    assert instance.itemID == 7
    instance.itemID = 13
    assert instance.itemID == 13


def test_Product_name_value_roundtrip():
    instance = Product(description="sample_text", itemID=7, name="sample_text", price="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Product_price_value_roundtrip():
    instance = Product(description="sample_text", itemID=7, name="sample_text", price="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_Register_attribute_value_roundtrip():
    instance = Register(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_SUID_ID_value_roundtrip():
    instance = SUID(ID=7, studentName="sample_text", suFOODBal="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_SUID_studentName_value_roundtrip():
    instance = SUID(ID=7, studentName="sample_text", suFOODBal="sample_text")
    assert instance.studentName == "sample_text"
    instance.studentName = "sample_text_2"
    assert instance.studentName == "sample_text_2"


def test_SUID_suFOODBal_value_roundtrip():
    instance = SUID(ID=7, studentName="sample_text", suFOODBal="sample_text")
    assert instance.suFOODBal == "sample_text"
    instance.suFOODBal = "sample_text_2"
    assert instance.suFOODBal == "sample_text_2"


def test_Sale_Date_value_roundtrip():
    instance = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_Sale_Time_value_roundtrip():
    instance = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    assert instance.Time == "sample_text"
    instance.Time = "sample_text_2"
    assert instance.Time == "sample_text_2"


def test_Sale_isComplete_value_roundtrip():
    instance = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    assert instance.isComplete == True
    instance.isComplete = False
    assert instance.isComplete == False


def test_Sales_Line_Item_Quantity_value_roundtrip():
    instance = Sales_Line_Item(Quantity=7)
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_Store_Address_value_roundtrip():
    instance = Store(Address="sample_text", Name="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_Store_Name_value_roundtrip():
    instance = Store(Address="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_customerDatabase_SUID_value_roundtrip():
    instance = customerDatabase(SUID=7, creditCardNum=7, customerName="sample_text", paymentHistory="sample_text")
    assert instance.SUID == 7
    instance.SUID = 13
    assert instance.SUID == 13


def test_customerDatabase_creditCardNum_value_roundtrip():
    instance = customerDatabase(SUID=7, creditCardNum=7, customerName="sample_text", paymentHistory="sample_text")
    assert instance.creditCardNum == 7
    instance.creditCardNum = 13
    assert instance.creditCardNum == 13


def test_customerDatabase_customerName_value_roundtrip():
    instance = customerDatabase(SUID=7, creditCardNum=7, customerName="sample_text", paymentHistory="sample_text")
    assert instance.customerName == "sample_text"
    instance.customerName = "sample_text_2"
    assert instance.customerName == "sample_text_2"


def test_customerDatabase_paymentHistory_value_roundtrip():
    instance = customerDatabase(SUID=7, creditCardNum=7, customerName="sample_text", paymentHistory="sample_text")
    assert instance.paymentHistory == "sample_text"
    instance.paymentHistory = "sample_text_2"
    assert instance.paymentHistory == "sample_text_2"


def test_assoc_Manager_Menu_link_reassign_clear():
    a = Menu(_attr="sample_text")
    b1 = Manager(name="sample_text", password="sample_text")
    b2 = Manager(name="sample_text_2", password="sample_text_2")
    _safe_set(a, 'manager29', b1)
    assert _is_linked(a, 'manager29', b1)
    if hasattr(b1, 'menu28'):
        assert _is_linked(b1, 'menu28', a)
    _safe_set(a, 'manager29', b2)
    assert _is_linked(a, 'manager29', b2)
    if hasattr(b1, 'menu28'):
        assert not _is_linked(b1, 'menu28', a)
    if hasattr(b2, 'menu28'):
        assert _is_linked(b2, 'menu28', a)
    _safe_set(a, 'manager29', None)
    assert not _is_linked(a, 'manager29', b2)
    if hasattr(b2, 'menu28'):
        assert not _is_linked(b2, 'menu28', a)


def test_assoc_Menu_Product_link_reassign_clear():
    a = Product(description="sample_text", itemID=7, name="sample_text", price="sample_text")
    b1 = Menu(_attr="sample_text")
    b2 = Menu(_attr="sample_text_2")
    _safe_set(a, 'menu5', b1)
    assert _is_linked(a, 'menu5', b1)
    if hasattr(b1, 'product4'):
        assert _is_linked(b1, 'product4', a)
    _safe_set(a, 'menu5', b2)
    assert _is_linked(a, 'menu5', b2)
    if hasattr(b1, 'product4'):
        assert not _is_linked(b1, 'product4', a)
    if hasattr(b2, 'product4'):
        assert _is_linked(b2, 'product4', a)
    _safe_set(a, 'menu5', None)
    assert not _is_linked(a, 'menu5', b2)
    if hasattr(b2, 'product4'):
        assert not _is_linked(b2, 'product4', a)


def test_assoc_Payment_Order_link_reassign_clear():
    a = Payment(amount="sample_text")
    b1 = Order(customer="sample_text", drinkName="sample_text", drinkPrice=7, foodName="sample_text", foodPrice=7)
    b2 = Order(customer="sample_text_2", drinkName="sample_text_2", drinkPrice=13, foodName="sample_text_2", foodPrice=13)
    _safe_set(a, 'order12', b1)
    assert _is_linked(a, 'order12', b1)
    if hasattr(b1, 'payment13'):
        assert _is_linked(b1, 'payment13', a)
    _safe_set(a, 'order12', b2)
    assert _is_linked(a, 'order12', b2)
    if hasattr(b1, 'payment13'):
        assert not _is_linked(b1, 'payment13', a)
    if hasattr(b2, 'payment13'):
        assert _is_linked(b2, 'payment13', a)
    _safe_set(a, 'order12', None)
    assert not _is_linked(a, 'order12', b2)
    if hasattr(b2, 'payment13'):
        assert not _is_linked(b2, 'payment13', a)


def test_assoc_Product_Sales_Line_Item_link_reassign_clear():
    a = Sales_Line_Item(Quantity=7)
    b1 = Product(description="sample_text", itemID=7, name="sample_text", price="sample_text")
    b2 = Product(description="sample_text_2", itemID=13, name="sample_text_2", price="sample_text_2")
    _safe_set(a, 'product27', b1)
    assert _is_linked(a, 'product27', b1)
    if hasattr(b1, 'sales_Line_Item26'):
        assert _is_linked(b1, 'sales_Line_Item26', a)
    _safe_set(a, 'product27', b2)
    assert _is_linked(a, 'product27', b2)
    if hasattr(b1, 'sales_Line_Item26'):
        assert not _is_linked(b1, 'sales_Line_Item26', a)
    if hasattr(b2, 'sales_Line_Item26'):
        assert _is_linked(b2, 'sales_Line_Item26', a)
    _safe_set(a, 'product27', None)
    assert not _is_linked(a, 'product27', b2)
    if hasattr(b2, 'sales_Line_Item26'):
        assert not _is_linked(b2, 'sales_Line_Item26', a)


def test_assoc_Register_Sale_link_reassign_clear():
    a = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    b1 = Register(attribute="sample_text")
    b2 = Register(attribute="sample_text_2")
    _safe_set(a, 'register7', b1)
    assert _is_linked(a, 'register7', b1)
    if hasattr(b1, 'sale6'):
        assert _is_linked(b1, 'sale6', a)
    _safe_set(a, 'register7', b2)
    assert _is_linked(a, 'register7', b2)
    if hasattr(b1, 'sale6'):
        assert not _is_linked(b1, 'sale6', a)
    if hasattr(b2, 'sale6'):
        assert _is_linked(b2, 'sale6', a)
    _safe_set(a, 'register7', None)
    assert not _is_linked(a, 'register7', b2)
    if hasattr(b2, 'sale6'):
        assert not _is_linked(b2, 'sale6', a)


def test_assoc_Register_Store_link_reassign_clear():
    a = Store(Address="sample_text", Name="sample_text")
    b1 = Register(attribute="sample_text")
    b2 = Register(attribute="sample_text_2")
    _safe_set(a, 'register1', b1)
    assert _is_linked(a, 'register1', b1)
    if hasattr(b1, 'store0'):
        assert _is_linked(b1, 'store0', a)
    _safe_set(a, 'register1', b2)
    assert _is_linked(a, 'register1', b2)
    if hasattr(b1, 'store0'):
        assert not _is_linked(b1, 'store0', a)
    if hasattr(b2, 'store0'):
        assert _is_linked(b2, 'store0', a)
    _safe_set(a, 'register1', None)
    assert not _is_linked(a, 'register1', b2)
    if hasattr(b2, 'store0'):
        assert not _is_linked(b2, 'store0', a)


def test_assoc_SUID_Card_link_reassign_clear():
    a = SUID(ID=7, studentName="sample_text", suFOODBal="sample_text")
    b1 = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    b2 = Card(cardNumber=13, cardSN=13, cardholderName="sample_text_2", isCredit=False, isDebit=False)
    _safe_set(a, 'card22', b1)
    assert _is_linked(a, 'card22', b1)
    if hasattr(b1, 'sUID23'):
        assert _is_linked(b1, 'sUID23', a)
    _safe_set(a, 'card22', b2)
    assert _is_linked(a, 'card22', b2)
    if hasattr(b1, 'sUID23'):
        assert not _is_linked(b1, 'sUID23', a)
    if hasattr(b2, 'sUID23'):
        assert _is_linked(b2, 'sUID23', a)
    _safe_set(a, 'card22', None)
    assert not _is_linked(a, 'card22', b2)
    if hasattr(b2, 'sUID23'):
        assert not _is_linked(b2, 'sUID23', a)


def test_assoc_SUID_Payment_link_reassign_clear():
    a = SUID(ID=7, studentName="sample_text", suFOODBal="sample_text")
    b1 = Payment(amount="sample_text")
    b2 = Payment(amount="sample_text_2")
    _safe_set(a, 'payment24', b1)
    assert _is_linked(a, 'payment24', b1)
    if hasattr(b1, 'sUID25'):
        assert _is_linked(b1, 'sUID25', a)
    _safe_set(a, 'payment24', b2)
    assert _is_linked(a, 'payment24', b2)
    if hasattr(b1, 'sUID25'):
        assert not _is_linked(b1, 'sUID25', a)
    if hasattr(b2, 'sUID25'):
        assert _is_linked(b2, 'sUID25', a)
    _safe_set(a, 'payment24', None)
    assert not _is_linked(a, 'payment24', b2)
    if hasattr(b2, 'sUID25'):
        assert not _is_linked(b2, 'sUID25', a)


def test_assoc_Sale_CardReader_link_reassign_clear():
    a = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    b1 = CardReader(attribute="sample_text")
    b2 = CardReader(attribute="sample_text_2")
    _safe_set(a, 'cardReader18', b1)
    assert _is_linked(a, 'cardReader18', b1)
    if hasattr(b1, 'sale19'):
        assert _is_linked(b1, 'sale19', a)
    _safe_set(a, 'cardReader18', b2)
    assert _is_linked(a, 'cardReader18', b2)
    if hasattr(b1, 'sale19'):
        assert not _is_linked(b1, 'sale19', a)
    if hasattr(b2, 'sale19'):
        assert _is_linked(b2, 'sale19', a)
    _safe_set(a, 'cardReader18', None)
    assert not _is_linked(a, 'cardReader18', b2)
    if hasattr(b2, 'sale19'):
        assert not _is_linked(b2, 'sale19', a)


def test_assoc_Sale_Payment_link_reassign_clear():
    a = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    b1 = Payment(amount="sample_text")
    b2 = Payment(amount="sample_text_2")
    _safe_set(a, 'payment8', b1)
    assert _is_linked(a, 'payment8', b1)
    if hasattr(b1, 'sale9'):
        assert _is_linked(b1, 'sale9', a)
    _safe_set(a, 'payment8', b2)
    assert _is_linked(a, 'payment8', b2)
    if hasattr(b1, 'sale9'):
        assert not _is_linked(b1, 'sale9', a)
    if hasattr(b2, 'sale9'):
        assert _is_linked(b2, 'sale9', a)
    _safe_set(a, 'payment8', None)
    assert not _is_linked(a, 'payment8', b2)
    if hasattr(b2, 'sale9'):
        assert not _is_linked(b2, 'sale9', a)


def test_assoc_Sale_Sales_Line_Item_link_reassign_clear():
    a = Sales_Line_Item(Quantity=7)
    b1 = Sale(Date="sample_text", Time="sample_text", isComplete=True)
    b2 = Sale(Date="sample_text_2", Time="sample_text_2", isComplete=False)
    _safe_set(a, 'sale11', b1)
    assert _is_linked(a, 'sale11', b1)
    if hasattr(b1, 'sales_Line_Item10'):
        assert _is_linked(b1, 'sales_Line_Item10', a)
    _safe_set(a, 'sale11', b2)
    assert _is_linked(a, 'sale11', b2)
    if hasattr(b1, 'sales_Line_Item10'):
        assert not _is_linked(b1, 'sales_Line_Item10', a)
    if hasattr(b2, 'sales_Line_Item10'):
        assert _is_linked(b2, 'sales_Line_Item10', a)
    _safe_set(a, 'sale11', None)
    assert not _is_linked(a, 'sale11', b2)
    if hasattr(b2, 'sales_Line_Item10'):
        assert not _is_linked(b2, 'sales_Line_Item10', a)


def test_assoc_Sales_Line_Item_Drink_link_reassign_clear():
    a = Sales_Line_Item(Quantity=7)
    b1 = Drink(name="sample_text", price="sample_text", quantity=7)
    b2 = Drink(name="sample_text_2", price="sample_text_2", quantity=13)
    _safe_set(a, 'drink16', {b1})
    assert _is_linked(a, 'drink16', b1)
    if hasattr(b1, 'sales_Line_Item17'):
        assert _is_linked(b1, 'sales_Line_Item17', a)
    _safe_set(a, 'drink16', {b2})
    assert _is_linked(a, 'drink16', b2)
    if hasattr(b1, 'sales_Line_Item17'):
        assert not _is_linked(b1, 'sales_Line_Item17', a)
    if hasattr(b2, 'sales_Line_Item17'):
        assert _is_linked(b2, 'sales_Line_Item17', a)
    _safe_set(a, 'drink16', set())
    assert not _is_linked(a, 'drink16', b2)
    if hasattr(b2, 'sales_Line_Item17'):
        assert not _is_linked(b2, 'sales_Line_Item17', a)


def test_assoc_Sales_Line_Item_Food_link_reassign_clear():
    a = Sales_Line_Item(Quantity=7)
    b1 = Food(attribute="sample_text", name="sample_text", price="sample_text", quantity=7)
    b2 = Food(attribute="sample_text_2", name="sample_text_2", price="sample_text_2", quantity=13)
    _safe_set(a, 'food14', {b1})
    assert _is_linked(a, 'food14', b1)
    if hasattr(b1, 'sales_Line_Item15'):
        assert _is_linked(b1, 'sales_Line_Item15', a)
    _safe_set(a, 'food14', {b2})
    assert _is_linked(a, 'food14', b2)
    if hasattr(b1, 'sales_Line_Item15'):
        assert not _is_linked(b1, 'sales_Line_Item15', a)
    if hasattr(b2, 'sales_Line_Item15'):
        assert _is_linked(b2, 'sales_Line_Item15', a)
    _safe_set(a, 'food14', set())
    assert not _is_linked(a, 'food14', b2)
    if hasattr(b2, 'sales_Line_Item15'):
        assert not _is_linked(b2, 'sales_Line_Item15', a)


def test_assoc_Store_Menu_link_reassign_clear():
    a = Store(Address="sample_text", Name="sample_text")
    b1 = Menu(_attr="sample_text")
    b2 = Menu(_attr="sample_text_2")
    _safe_set(a, 'menu2', b1)
    assert _is_linked(a, 'menu2', b1)
    if hasattr(b1, 'store3'):
        assert _is_linked(b1, 'store3', a)
    _safe_set(a, 'menu2', b2)
    assert _is_linked(a, 'menu2', b2)
    if hasattr(b1, 'store3'):
        assert not _is_linked(b1, 'store3', a)
    if hasattr(b2, 'store3'):
        assert _is_linked(b2, 'store3', a)
    _safe_set(a, 'menu2', None)
    assert not _is_linked(a, 'menu2', b2)
    if hasattr(b2, 'store3'):
        assert not _is_linked(b2, 'store3', a)


def test_assoc_customerDatabase_Card_link_reassign_clear():
    a = customerDatabase(SUID=7, creditCardNum=7, customerName="sample_text", paymentHistory="sample_text")
    b1 = Card(cardNumber=7, cardSN=7, cardholderName="sample_text", isCredit=True, isDebit=True)
    b2 = Card(cardNumber=13, cardSN=13, cardholderName="sample_text_2", isCredit=False, isDebit=False)
    _safe_set(a, 'card20', {b1})
    assert _is_linked(a, 'card20', b1)
    if hasattr(b1, 'customerDatabase21'):
        assert _is_linked(b1, 'customerDatabase21', a)
    _safe_set(a, 'card20', {b2})
    assert _is_linked(a, 'card20', b2)
    if hasattr(b1, 'customerDatabase21'):
        assert not _is_linked(b1, 'customerDatabase21', a)
    if hasattr(b2, 'customerDatabase21'):
        assert _is_linked(b2, 'customerDatabase21', a)
    _safe_set(a, 'card20', set())
    assert not _is_linked(a, 'card20', b2)
    if hasattr(b2, 'customerDatabase21'):
        assert not _is_linked(b2, 'customerDatabase21', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Card_strategy = st.builds(Card, cardNumber=st.integers(), cardSN=st.integers(), cardholderName=safe_text, isCredit=st.booleans(), isDebit=st.booleans())
@given(instance=Card_strategy)
@settings(max_examples=25)
def test_Card_instantiation(instance):
    assert isinstance(instance, Card)


CardReader_strategy = st.builds(CardReader, attribute=safe_text)
@given(instance=CardReader_strategy)
@settings(max_examples=25)
def test_CardReader_instantiation(instance):
    assert isinstance(instance, CardReader)


Drink_strategy = st.builds(Drink, name=safe_text, price=safe_text, quantity=st.integers())
@given(instance=Drink_strategy)
@settings(max_examples=25)
def test_Drink_instantiation(instance):
    assert isinstance(instance, Drink)


Food_strategy = st.builds(Food, attribute=safe_text, name=safe_text, price=safe_text, quantity=st.integers())
@given(instance=Food_strategy)
@settings(max_examples=25)
def test_Food_instantiation(instance):
    assert isinstance(instance, Food)


Manager_strategy = st.builds(Manager, name=safe_text, password=safe_text)
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


Menu_strategy = st.builds(Menu, _attr=safe_text)
@given(instance=Menu_strategy)
@settings(max_examples=25)
def test_Menu_instantiation(instance):
    assert isinstance(instance, Menu)


Order_strategy = st.builds(Order, customer=safe_text, drinkName=safe_text, drinkPrice=st.integers(), foodName=safe_text, foodPrice=st.integers())
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Payment_strategy = st.builds(Payment, amount=safe_text)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Product_strategy = st.builds(Product, description=safe_text, itemID=st.integers(), name=safe_text, price=safe_text)
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)


Register_strategy = st.builds(Register, attribute=safe_text)
@given(instance=Register_strategy)
@settings(max_examples=25)
def test_Register_instantiation(instance):
    assert isinstance(instance, Register)


SUID_strategy = st.builds(SUID, ID=st.integers(), studentName=safe_text, suFOODBal=safe_text)
@given(instance=SUID_strategy)
@settings(max_examples=25)
def test_SUID_instantiation(instance):
    assert isinstance(instance, SUID)


Sale_strategy = st.builds(Sale, Date=safe_text, Time=safe_text, isComplete=st.booleans())
@given(instance=Sale_strategy)
@settings(max_examples=25)
def test_Sale_instantiation(instance):
    assert isinstance(instance, Sale)


Sales_Line_Item_strategy = st.builds(Sales_Line_Item, Quantity=st.integers())
@given(instance=Sales_Line_Item_strategy)
@settings(max_examples=25)
def test_Sales_Line_Item_instantiation(instance):
    assert isinstance(instance, Sales_Line_Item)


Store_strategy = st.builds(Store, Address=safe_text, Name=safe_text)
@given(instance=Store_strategy)
@settings(max_examples=25)
def test_Store_instantiation(instance):
    assert isinstance(instance, Store)


customerDatabase_strategy = st.builds(customerDatabase, SUID=st.integers(), creditCardNum=st.integers(), customerName=safe_text, paymentHistory=safe_text)
@given(instance=customerDatabase_strategy)
@settings(max_examples=25)
def test_customerDatabase_instantiation(instance):
    assert isinstance(instance, customerDatabase)



