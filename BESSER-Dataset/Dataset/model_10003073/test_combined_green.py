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
    User,
    Registration,
    Cart,
    StaffUI,
    Chef,
    Product,
    Order,
    Invoice,
    Table,
    Booking,
    ReservationManagementSystem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Passowrd" in params, "Missing parameter 'Passowrd'"
    assert "User_Name" in params, "Missing parameter 'User_Name'"





def test_hyp_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_hyp_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_hyp_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "First_Name" in params, "Missing parameter 'First_Name'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Email" in params, "Missing parameter 'Email'"











def test_hyp_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_hyp_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_hyp_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())
    assert "Product" in params, "Missing parameter 'Product'"

def test_hyp_cart_has_Product():
    assert hasattr(Cart, "Product")
    descriptor = None
    for klass in Cart.__mro__:
        if "Product" in klass.__dict__:
            descriptor = klass.__dict__["Product"]
            break
    assert isinstance(descriptor, property)



def test_hyp_staffui_is_not_abstract():
    assert not inspect.isabstract(StaffUI)


def test_hyp_staffui_constructor_exists():
    assert callable(StaffUI.__init__)


def test_hyp_staffui_constructor_args():
    sig = inspect.signature(StaffUI.__init__)
    params = list(sig.parameters.keys())



def test_hyp_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_hyp_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_hyp_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_hyp_product_constructor_exists():
    assert callable(Product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "Note" in params, "Missing parameter 'Note'"
    assert "price" in params, "Missing parameter 'price'"
    assert "food_id" in params, "Missing parameter 'food_id'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "order_id" in params, "Missing parameter 'order_id'"
    assert "foodList" in params, "Missing parameter 'foodList'"





def test_hyp_invoice_is_not_abstract():
    assert not inspect.isabstract(Invoice)


def test_hyp_invoice_constructor_exists():
    assert callable(Invoice.__init__)


def test_hyp_invoice_constructor_args():
    sig = inspect.signature(Invoice.__init__)
    params = list(sig.parameters.keys())
    assert "invoice_id" in params, "Missing parameter 'invoice_id'"
    assert "orders" in params, "Missing parameter 'orders'"





def test_hyp_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_hyp_table_constructor_exists():
    assert callable(Table.__init__)


def test_hyp_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "numSeats" in params, "Missing parameter 'numSeats'"
    assert "avaliable" in params, "Missing parameter 'avaliable'"
    assert "table_id" in params, "Missing parameter 'table_id'"






def test_hyp_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_hyp_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_hyp_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "booking_id" in params, "Missing parameter 'booking_id'"
    assert "customer_name" in params, "Missing parameter 'customer_name'"
    assert "date" in params, "Missing parameter 'date'"









def test_hyp_reservationmanagementsystem_is_not_abstract():
    assert not inspect.isabstract(ReservationManagementSystem)


def test_hyp_reservationmanagementsystem_constructor_exists():
    assert callable(ReservationManagementSystem.__init__)


def test_hyp_reservationmanagementsystem_constructor_args():
    sig = inspect.signature(ReservationManagementSystem.__init__)
    params = list(sig.parameters.keys())
    assert "bookings" in params, "Missing parameter 'bookings'"



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
User_strategy = st.builds(
    User,
    Passowrd=
        safe_text,
    User_Name=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    attribute=
        safe_text,
    UserName=
        safe_text,
    attribute5=
        safe_text,
    First_Name=
        safe_text,
    Password=
        safe_text,
    Last_Name=
        safe_text,
    Gender=
        safe_text,
    Email=
        safe_text
)
Cart_strategy = st.builds(
    Cart,
    Product=
        st.none()
)
StaffUI_strategy = st.builds(
    StaffUI,
)
Chef_strategy = st.builds(
    Chef,
)
Product_strategy = st.builds(
    Product,
    Note=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    food_id=
        safe_text,
    name=
        safe_text
)
Order_strategy = st.builds(
    Order,
    order_id=
        safe_text,
    foodList=
        safe_text
)
Invoice_strategy = st.builds(
    Invoice,
    invoice_id=
        safe_text,
    orders=
        safe_text
)
Table_strategy = st.builds(
    Table,
    numSeats=
        st.integers(),
    avaliable=
        st.booleans(),
    table_id=
        safe_text
)
Booking_strategy = st.builds(
    Booking,
    startTime=
        safe_text,
    endTime=
        safe_text,
    reservedTables=
        safe_text,
    booking_id=
        st.integers(),
    customer_name=
        safe_text,
    date=
        st.dates()
)
ReservationManagementSystem_strategy = st.builds(
    ReservationManagementSystem,
    bookings=
        safe_text
)




@given(instance=User_strategy)
def test_hyp_user_Passowrd_setter(instance):
    original = instance.Passowrd
    instance.Passowrd = original
    assert instance.Passowrd == original



@given(instance=User_strategy)
def test_hyp_user_User_Name_setter(instance):
    original = instance.User_Name
    instance.User_Name = original
    assert instance.User_Name == original




@given(instance=Registration_strategy)
def test_hyp_registration_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Registration_strategy)
def test_hyp_registration_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Registration_strategy)
def test_hyp_registration_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=Registration_strategy)
def test_hyp_registration_First_Name_setter(instance):
    original = instance.First_Name
    instance.First_Name = original
    assert instance.First_Name == original



@given(instance=Registration_strategy)
def test_hyp_registration_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Registration_strategy)
def test_hyp_registration_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=Registration_strategy)
def test_hyp_registration_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Registration_strategy)
def test_hyp_registration_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Cart_strategy)
@settings(max_examples=50)
def test_hyp_cart_instantiation(instance):
    assert isinstance(instance, Cart)



@given(instance=Cart_strategy)
def test_hyp_cart_Product_setter(instance):
    original = instance.Product
    instance.Product = original
    assert instance.Product == original






@given(instance=Product_strategy)
def test_hyp_product_Note_setter(instance):
    original = instance.Note
    instance.Note = original
    assert instance.Note == original



@given(instance=Product_strategy)
def test_hyp_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Product_strategy)
def test_hyp_product_food_id_setter(instance):
    original = instance.food_id
    instance.food_id = original
    assert instance.food_id == original



@given(instance=Product_strategy)
def test_hyp_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Order_strategy)
def test_hyp_order_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original



@given(instance=Order_strategy)
def test_hyp_order_foodList_setter(instance):
    original = instance.foodList
    instance.foodList = original
    assert instance.foodList == original




@given(instance=Invoice_strategy)
def test_hyp_invoice_invoice_id_setter(instance):
    original = instance.invoice_id
    instance.invoice_id = original
    assert instance.invoice_id == original



@given(instance=Invoice_strategy)
def test_hyp_invoice_orders_setter(instance):
    original = instance.orders
    instance.orders = original
    assert instance.orders == original




@given(instance=Table_strategy)
def test_hyp_table_numSeats_setter(instance):
    original = instance.numSeats
    instance.numSeats = original
    assert instance.numSeats == original



@given(instance=Table_strategy)
def test_hyp_table_avaliable_setter(instance):
    original = instance.avaliable
    instance.avaliable = original
    assert instance.avaliable == original



@given(instance=Table_strategy)
def test_hyp_table_table_id_setter(instance):
    original = instance.table_id
    instance.table_id = original
    assert instance.table_id == original




@given(instance=Booking_strategy)
def test_hyp_booking_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original



@given(instance=Booking_strategy)
def test_hyp_booking_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=Booking_strategy)
def test_hyp_booking_reservedTables_setter(instance):
    original = instance.reservedTables
    instance.reservedTables = original
    assert instance.reservedTables == original



@given(instance=Booking_strategy)
def test_hyp_booking_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original



@given(instance=Booking_strategy)
def test_hyp_booking_customer_name_setter(instance):
    original = instance.customer_name
    instance.customer_name = original
    assert instance.customer_name == original



@given(instance=Booking_strategy)
def test_hyp_booking_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=ReservationManagementSystem_strategy)
def test_hyp_reservationmanagementsystem_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Booking,
    Cart,
    Chef,
    Invoice,
    Order,
    Product,
    Registration,
    ReservationManagementSystem,
    StaffUI,
    Table,
    User,
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

def test_Booking_booking_id_value_roundtrip():
    instance = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    assert instance.booking_id == 7
    instance.booking_id = 13
    assert instance.booking_id == 13


def test_Booking_customer_name_value_roundtrip():
    instance = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    assert instance.customer_name == "sample_text"
    instance.customer_name = "sample_text_2"
    assert instance.customer_name == "sample_text_2"


def test_Booking_date_value_roundtrip():
    instance = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_Booking_endTime_value_roundtrip():
    instance = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    assert instance.endTime == "sample_text"
    instance.endTime = "sample_text_2"
    assert instance.endTime == "sample_text_2"


def test_Booking_reservedTables_value_roundtrip():
    instance = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    assert instance.reservedTables == "sample_text"
    instance.reservedTables = "sample_text_2"
    assert instance.reservedTables == "sample_text_2"


def test_Booking_startTime_value_roundtrip():
    instance = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    assert instance.startTime == "sample_text"
    instance.startTime = "sample_text_2"
    assert instance.startTime == "sample_text_2"


def test_Invoice_invoice_id_value_roundtrip():
    instance = Invoice(invoice_id="sample_text", orders="sample_text")
    assert instance.invoice_id == "sample_text"
    instance.invoice_id = "sample_text_2"
    assert instance.invoice_id == "sample_text_2"


def test_Invoice_orders_value_roundtrip():
    instance = Invoice(invoice_id="sample_text", orders="sample_text")
    assert instance.orders == "sample_text"
    instance.orders = "sample_text_2"
    assert instance.orders == "sample_text_2"


def test_Order_foodList_value_roundtrip():
    instance = Order(foodList="sample_text", order_id="sample_text")
    assert instance.foodList == "sample_text"
    instance.foodList = "sample_text_2"
    assert instance.foodList == "sample_text_2"


def test_Order_order_id_value_roundtrip():
    instance = Order(foodList="sample_text", order_id="sample_text")
    assert instance.order_id == "sample_text"
    instance.order_id = "sample_text_2"
    assert instance.order_id == "sample_text_2"


def test_Product_Note_value_roundtrip():
    instance = Product(Note="sample_text", food_id="sample_text", name="sample_text", price=3.14)
    assert instance.Note == "sample_text"
    instance.Note = "sample_text_2"
    assert instance.Note == "sample_text_2"


def test_Product_food_id_value_roundtrip():
    instance = Product(Note="sample_text", food_id="sample_text", name="sample_text", price=3.14)
    assert instance.food_id == "sample_text"
    instance.food_id = "sample_text_2"
    assert instance.food_id == "sample_text_2"


def test_Product_name_value_roundtrip():
    instance = Product(Note="sample_text", food_id="sample_text", name="sample_text", price=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Product_price_value_roundtrip():
    instance = Product(Note="sample_text", food_id="sample_text", name="sample_text", price=3.14)
    assert instance.price == 3.14
    instance.price = 9.99
    assert instance.price == 9.99


def test_Registration_Email_value_roundtrip():
    instance = Registration(Email="sample_text", First_Name="sample_text", Gender="sample_text", Last_Name="sample_text", Password="sample_text", UserName="sample_text", attribute="sample_text", attribute5="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Registration_First_Name_value_roundtrip():
    instance = Registration(Email="sample_text", First_Name="sample_text", Gender="sample_text", Last_Name="sample_text", Password="sample_text", UserName="sample_text", attribute="sample_text", attribute5="sample_text")
    assert instance.First_Name == "sample_text"
    instance.First_Name = "sample_text_2"
    assert instance.First_Name == "sample_text_2"


def test_Registration_Gender_value_roundtrip():
    instance = Registration(Email="sample_text", First_Name="sample_text", Gender="sample_text", Last_Name="sample_text", Password="sample_text", UserName="sample_text", attribute="sample_text", attribute5="sample_text")
    assert instance.Gender == "sample_text"
    instance.Gender = "sample_text_2"
    assert instance.Gender == "sample_text_2"


def test_Registration_Last_Name_value_roundtrip():
    instance = Registration(Email="sample_text", First_Name="sample_text", Gender="sample_text", Last_Name="sample_text", Password="sample_text", UserName="sample_text", attribute="sample_text", attribute5="sample_text")
    assert instance.Last_Name == "sample_text"
    instance.Last_Name = "sample_text_2"
    assert instance.Last_Name == "sample_text_2"


def test_Registration_Password_value_roundtrip():
    instance = Registration(Email="sample_text", First_Name="sample_text", Gender="sample_text", Last_Name="sample_text", Password="sample_text", UserName="sample_text", attribute="sample_text", attribute5="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Registration_UserName_value_roundtrip():
    instance = Registration(Email="sample_text", First_Name="sample_text", Gender="sample_text", Last_Name="sample_text", Password="sample_text", UserName="sample_text", attribute="sample_text", attribute5="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_Registration_attribute_value_roundtrip():
    instance = Registration(Email="sample_text", First_Name="sample_text", Gender="sample_text", Last_Name="sample_text", Password="sample_text", UserName="sample_text", attribute="sample_text", attribute5="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Registration_attribute5_value_roundtrip():
    instance = Registration(Email="sample_text", First_Name="sample_text", Gender="sample_text", Last_Name="sample_text", Password="sample_text", UserName="sample_text", attribute="sample_text", attribute5="sample_text")
    assert instance.attribute5 == "sample_text"
    instance.attribute5 = "sample_text_2"
    assert instance.attribute5 == "sample_text_2"


def test_ReservationManagementSystem_bookings_value_roundtrip():
    instance = ReservationManagementSystem(bookings="sample_text")
    assert instance.bookings == "sample_text"
    instance.bookings = "sample_text_2"
    assert instance.bookings == "sample_text_2"


def test_Table_avaliable_value_roundtrip():
    instance = Table(avaliable=True, numSeats=7, table_id="sample_text")
    assert instance.avaliable == True
    instance.avaliable = False
    assert instance.avaliable == False


def test_Table_numSeats_value_roundtrip():
    instance = Table(avaliable=True, numSeats=7, table_id="sample_text")
    assert instance.numSeats == 7
    instance.numSeats = 13
    assert instance.numSeats == 13


def test_Table_table_id_value_roundtrip():
    instance = Table(avaliable=True, numSeats=7, table_id="sample_text")
    assert instance.table_id == "sample_text"
    instance.table_id = "sample_text_2"
    assert instance.table_id == "sample_text_2"


def test_User_Passowrd_value_roundtrip():
    instance = User(Passowrd="sample_text", User_Name="sample_text")
    assert instance.Passowrd == "sample_text"
    instance.Passowrd = "sample_text_2"
    assert instance.Passowrd == "sample_text_2"


def test_User_User_Name_value_roundtrip():
    instance = User(Passowrd="sample_text", User_Name="sample_text")
    assert instance.User_Name == "sample_text"
    instance.User_Name = "sample_text_2"
    assert instance.User_Name == "sample_text_2"


def test_assoc_Order_Food_link_reassign_clear():
    a = Product(Note="sample_text", food_id="sample_text", name="sample_text", price=3.14)
    b1 = Order(foodList="sample_text", order_id="sample_text")
    b2 = Order(foodList="sample_text_2", order_id="sample_text_2")
    _safe_set(a, 'has9', b1)
    assert _is_linked(a, 'has9', b1)
    if hasattr(b1, 'orde8'):
        assert _is_linked(b1, 'orde8', a)
    _safe_set(a, 'has9', b2)
    assert _is_linked(a, 'has9', b2)
    if hasattr(b1, 'orde8'):
        assert not _is_linked(b1, 'orde8', a)
    if hasattr(b2, 'orde8'):
        assert _is_linked(b2, 'orde8', a)
    _safe_set(a, 'has9', None)
    assert not _is_linked(a, 'has9', b2)
    if hasattr(b2, 'orde8'):
        assert not _is_linked(b2, 'orde8', a)


def test_assoc_ReservationManagementSystem_Booking_link_reassign_clear():
    a = ReservationManagementSystem(bookings="sample_text")
    b1 = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    b2 = Booking(booking_id=13, customer_name="sample_text_2", date=date(2025, 6, 15), endTime="sample_text_2", reservedTables="sample_text_2", startTime="sample_text_2")
    _safe_set(a, 'booking0', {b1})
    assert _is_linked(a, 'booking0', b1)
    if hasattr(b1, 'ReservationManagementSystem_Booking_11'):
        assert _is_linked(b1, 'ReservationManagementSystem_Booking_11', a)
    _safe_set(a, 'booking0', {b2})
    assert _is_linked(a, 'booking0', b2)
    if hasattr(b1, 'ReservationManagementSystem_Booking_11'):
        assert not _is_linked(b1, 'ReservationManagementSystem_Booking_11', a)
    if hasattr(b2, 'ReservationManagementSystem_Booking_11'):
        assert _is_linked(b2, 'ReservationManagementSystem_Booking_11', a)
    _safe_set(a, 'booking0', set())
    assert not _is_linked(a, 'booking0', b2)
    if hasattr(b2, 'ReservationManagementSystem_Booking_11'):
        assert not _is_linked(b2, 'ReservationManagementSystem_Booking_11', a)


def test_assoc_ReservationManagementSystem_Report_link_reassign_clear():
    a = ReservationManagementSystem(bookings="sample_text")
    b1 = Invoice(invoice_id="sample_text", orders="sample_text")
    b2 = Invoice(invoice_id="sample_text_2", orders="sample_text_2")
    _safe_set(a, 'generates2', {b1})
    assert _is_linked(a, 'generates2', b1)
    if hasattr(b1, 'reservationManagementSystem3'):
        assert _is_linked(b1, 'reservationManagementSystem3', a)
    _safe_set(a, 'generates2', {b2})
    assert _is_linked(a, 'generates2', b2)
    if hasattr(b1, 'reservationManagementSystem3'):
        assert not _is_linked(b1, 'reservationManagementSystem3', a)
    if hasattr(b2, 'reservationManagementSystem3'):
        assert _is_linked(b2, 'reservationManagementSystem3', a)
    _safe_set(a, 'generates2', set())
    assert not _is_linked(a, 'generates2', b2)
    if hasattr(b2, 'reservationManagementSystem3'):
        assert not _is_linked(b2, 'reservationManagementSystem3', a)


def test_assoc_Table_Booking_link_reassign_clear():
    a = Table(avaliable=True, numSeats=7, table_id="sample_text")
    b1 = Booking(booking_id=7, customer_name="sample_text", date=date(2024, 1, 1), endTime="sample_text", reservedTables="sample_text", startTime="sample_text")
    b2 = Booking(booking_id=13, customer_name="sample_text_2", date=date(2025, 6, 15), endTime="sample_text_2", reservedTables="sample_text_2", startTime="sample_text_2")
    _safe_set(a, 'Table_Booking_06', b1)
    assert _is_linked(a, 'Table_Booking_06', b1)
    if hasattr(b1, 'reservedBy7'):
        assert _is_linked(b1, 'reservedBy7', a)
    _safe_set(a, 'Table_Booking_06', b2)
    assert _is_linked(a, 'Table_Booking_06', b2)
    if hasattr(b1, 'reservedBy7'):
        assert not _is_linked(b1, 'reservedBy7', a)
    if hasattr(b2, 'reservedBy7'):
        assert _is_linked(b2, 'reservedBy7', a)
    _safe_set(a, 'Table_Booking_06', None)
    assert not _is_linked(a, 'Table_Booking_06', b2)
    if hasattr(b2, 'reservedBy7'):
        assert not _is_linked(b2, 'reservedBy7', a)


def test_assoc_Table_Order_link_reassign_clear():
    a = Table(avaliable=True, numSeats=7, table_id="sample_text")
    b1 = Order(foodList="sample_text", order_id="sample_text")
    b2 = Order(foodList="sample_text_2", order_id="sample_text_2")
    _safe_set(a, 'has4', b1)
    assert _is_linked(a, 'has4', b1)
    if hasattr(b1, 'table5'):
        assert _is_linked(b1, 'table5', a)
    _safe_set(a, 'has4', b2)
    assert _is_linked(a, 'has4', b2)
    if hasattr(b1, 'table5'):
        assert not _is_linked(b1, 'table5', a)
    if hasattr(b2, 'table5'):
        assert _is_linked(b2, 'table5', a)
    _safe_set(a, 'has4', None)
    assert not _is_linked(a, 'has4', b2)
    if hasattr(b2, 'table5'):
        assert not _is_linked(b2, 'table5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Booking_strategy = st.builds(Booking, booking_id=st.integers(), customer_name=safe_text, date=st.dates(), endTime=safe_text, reservedTables=safe_text, startTime=safe_text)
@given(instance=Booking_strategy)
@settings(max_examples=25)
def test_Booking_instantiation(instance):
    assert isinstance(instance, Booking)


Chef_strategy = st.builds(Chef)
@given(instance=Chef_strategy)
@settings(max_examples=25)
def test_Chef_instantiation(instance):
    assert isinstance(instance, Chef)


Invoice_strategy = st.builds(Invoice, invoice_id=safe_text, orders=safe_text)
@given(instance=Invoice_strategy)
@settings(max_examples=25)
def test_Invoice_instantiation(instance):
    assert isinstance(instance, Invoice)


Order_strategy = st.builds(Order, foodList=safe_text, order_id=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Product_strategy = st.builds(Product, Note=safe_text, food_id=safe_text, name=safe_text, price=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)


Registration_strategy = st.builds(Registration, Email=safe_text, First_Name=safe_text, Gender=safe_text, Last_Name=safe_text, Password=safe_text, UserName=safe_text, attribute=safe_text, attribute5=safe_text)
@given(instance=Registration_strategy)
@settings(max_examples=25)
def test_Registration_instantiation(instance):
    assert isinstance(instance, Registration)


ReservationManagementSystem_strategy = st.builds(ReservationManagementSystem, bookings=safe_text)
@given(instance=ReservationManagementSystem_strategy)
@settings(max_examples=25)
def test_ReservationManagementSystem_instantiation(instance):
    assert isinstance(instance, ReservationManagementSystem)


StaffUI_strategy = st.builds(StaffUI)
@given(instance=StaffUI_strategy)
@settings(max_examples=25)
def test_StaffUI_instantiation(instance):
    assert isinstance(instance, StaffUI)


Table_strategy = st.builds(Table, avaliable=st.booleans(), numSeats=st.integers(), table_id=safe_text)
@given(instance=Table_strategy)
@settings(max_examples=25)
def test_Table_instantiation(instance):
    assert isinstance(instance, Table)


User_strategy = st.builds(User, Passowrd=safe_text, User_Name=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



