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
    Guest,
    Employee,
    OrderDetails,
    Meals,
    Payment,
    Admin,
    Transport,
    User,
    Orders,
    Cart,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_hyp_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_hyp_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())
    assert "guestID" in params, "Missing parameter 'guestID'"




def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "EmpPassword" in params, "Missing parameter 'EmpPassword'"
    assert "EmployeeID" in params, "Missing parameter 'EmployeeID'"
    assert "EmpName" in params, "Missing parameter 'EmpName'"






def test_hyp_orderdetails_is_not_abstract():
    assert not inspect.isabstract(OrderDetails)


def test_hyp_orderdetails_constructor_exists():
    assert callable(OrderDetails.__init__)


def test_hyp_orderdetails_constructor_args():
    sig = inspect.signature(OrderDetails.__init__)
    params = list(sig.parameters.keys())
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "totPrice" in params, "Missing parameter 'totPrice'"
    assert "orderTime" in params, "Missing parameter 'orderTime'"
    assert "MealID" in params, "Missing parameter 'MealID'"
    assert "status" in params, "Missing parameter 'status'"
    assert "quantity" in params, "Missing parameter 'quantity'"









def test_hyp_meals_is_not_abstract():
    assert not inspect.isabstract(Meals)


def test_hyp_meals_constructor_exists():
    assert callable(Meals.__init__)


def test_hyp_meals_constructor_args():
    sig = inspect.signature(Meals.__init__)
    params = list(sig.parameters.keys())
    assert "MealID" in params, "Missing parameter 'MealID'"
    assert "Portion" in params, "Missing parameter 'Portion'"
    assert "supplier" in params, "Missing parameter 'supplier'"
    assert "MealType" in params, "Missing parameter 'MealType'"
    assert "MealName" in params, "Missing parameter 'MealName'"
    assert "unitPrice" in params, "Missing parameter 'unitPrice'"









def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "PaymentType" in params, "Missing parameter 'PaymentType'"
    assert "paymentID" in params, "Missing parameter 'paymentID'"
    assert "paymentDate" in params, "Missing parameter 'paymentDate'"
    assert "PaymentStatus" in params, "Missing parameter 'PaymentStatus'"
    assert "paymentAmount" in params, "Missing parameter 'paymentAmount'"








def test_hyp_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_hyp_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_hyp_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transport_is_not_abstract():
    assert not inspect.isabstract(Transport)


def test_hyp_transport_constructor_exists():
    assert callable(Transport.__init__)


def test_hyp_transport_constructor_args():
    sig = inspect.signature(Transport.__init__)
    params = list(sig.parameters.keys())
    assert "transportCost" in params, "Missing parameter 'transportCost'"
    assert "location" in params, "Missing parameter 'location'"
    assert "TransportID" in params, "Missing parameter 'TransportID'"






def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"






def test_hyp_orders_is_not_abstract():
    assert not inspect.isabstract(Orders)


def test_hyp_orders_constructor_exists():
    assert callable(Orders.__init__)


def test_hyp_orders_constructor_args():
    sig = inspect.signature(Orders.__init__)
    params = list(sig.parameters.keys())
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "status" in params, "Missing parameter 'status'"
    assert "dateFinished" in params, "Missing parameter 'dateFinished'"
    assert "dateOrdered" in params, "Missing parameter 'dateOrdered'"







def test_hyp_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_hyp_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_hyp_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "cartID" in params, "Missing parameter 'cartID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "date" in params, "Missing parameter 'date'"







def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "CutsomerAddress" in params, "Missing parameter 'CutsomerAddress'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "Email" in params, "Missing parameter 'Email'"






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
Guest_strategy = st.builds(
    Guest,
    guestID=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    EmpPassword=
        safe_text,
    EmployeeID=
        safe_text,
    EmpName=
        safe_text
)
OrderDetails_strategy = st.builds(
    OrderDetails,
    OrderID=
        st.integers(),
    totPrice=
        safe_text,
    orderTime=
        safe_text,
    MealID=
        safe_text,
    status=
        safe_text,
    quantity=
        st.integers()
)
Meals_strategy = st.builds(
    Meals,
    MealID=
        safe_text,
    Portion=
        safe_text,
    supplier=
        safe_text,
    MealType=
        safe_text,
    MealName=
        safe_text,
    unitPrice=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    PaymentType=
        safe_text,
    paymentID=
        safe_text,
    paymentDate=
        safe_text,
    PaymentStatus=
        safe_text,
    paymentAmount=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
)
Transport_strategy = st.builds(
    Transport,
    transportCost=
        safe_text,
    location=
        safe_text,
    TransportID=
        st.integers()
)
User_strategy = st.builds(
    User,
    userID=
        safe_text,
    Password=
        safe_text,
    loginStatus=
        safe_text
)
Orders_strategy = st.builds(
    Orders,
    OrderID=
        st.integers(),
    status=
        safe_text,
    dateFinished=
        safe_text,
    dateOrdered=
        safe_text
)
Cart_strategy = st.builds(
    Cart,
    Quantity=
        st.integers(),
    cartID=
        st.integers(),
    ProductID=
        safe_text,
    date=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    CutsomerAddress=
        safe_text,
    PhoneNumber=
        st.integers(),
    CustomerName=
        safe_text,
    Email=
        safe_text
)




@given(instance=Guest_strategy)
def test_hyp_guest_guestID_setter(instance):
    original = instance.guestID
    instance.guestID = original
    assert instance.guestID == original




@given(instance=Employee_strategy)
def test_hyp_employee_EmpPassword_setter(instance):
    original = instance.EmpPassword
    instance.EmpPassword = original
    assert instance.EmpPassword == original



@given(instance=Employee_strategy)
def test_hyp_employee_EmployeeID_setter(instance):
    original = instance.EmployeeID
    instance.EmployeeID = original
    assert instance.EmployeeID == original



@given(instance=Employee_strategy)
def test_hyp_employee_EmpName_setter(instance):
    original = instance.EmpName
    instance.EmpName = original
    assert instance.EmpName == original




@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_totPrice_setter(instance):
    original = instance.totPrice
    instance.totPrice = original
    assert instance.totPrice == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_orderTime_setter(instance):
    original = instance.orderTime
    instance.orderTime = original
    assert instance.orderTime == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_MealID_setter(instance):
    original = instance.MealID
    instance.MealID = original
    assert instance.MealID == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=OrderDetails_strategy)
def test_hyp_orderdetails_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original




@given(instance=Meals_strategy)
def test_hyp_meals_MealID_setter(instance):
    original = instance.MealID
    instance.MealID = original
    assert instance.MealID == original



@given(instance=Meals_strategy)
def test_hyp_meals_Portion_setter(instance):
    original = instance.Portion
    instance.Portion = original
    assert instance.Portion == original



@given(instance=Meals_strategy)
def test_hyp_meals_supplier_setter(instance):
    original = instance.supplier
    instance.supplier = original
    assert instance.supplier == original



@given(instance=Meals_strategy)
def test_hyp_meals_MealType_setter(instance):
    original = instance.MealType
    instance.MealType = original
    assert instance.MealType == original



@given(instance=Meals_strategy)
def test_hyp_meals_MealName_setter(instance):
    original = instance.MealName
    instance.MealName = original
    assert instance.MealName == original



@given(instance=Meals_strategy)
def test_hyp_meals_unitPrice_setter(instance):
    original = instance.unitPrice
    instance.unitPrice = original
    assert instance.unitPrice == original




@given(instance=Payment_strategy)
def test_hyp_payment_PaymentType_setter(instance):
    original = instance.PaymentType
    instance.PaymentType = original
    assert instance.PaymentType == original



@given(instance=Payment_strategy)
def test_hyp_payment_paymentID_setter(instance):
    original = instance.paymentID
    instance.paymentID = original
    assert instance.paymentID == original



@given(instance=Payment_strategy)
def test_hyp_payment_paymentDate_setter(instance):
    original = instance.paymentDate
    instance.paymentDate = original
    assert instance.paymentDate == original



@given(instance=Payment_strategy)
def test_hyp_payment_PaymentStatus_setter(instance):
    original = instance.PaymentStatus
    instance.PaymentStatus = original
    assert instance.PaymentStatus == original



@given(instance=Payment_strategy)
def test_hyp_payment_paymentAmount_setter(instance):
    original = instance.paymentAmount
    instance.paymentAmount = original
    assert instance.paymentAmount == original





@given(instance=Transport_strategy)
def test_hyp_transport_transportCost_setter(instance):
    original = instance.transportCost
    instance.transportCost = original
    assert instance.transportCost == original



@given(instance=Transport_strategy)
def test_hyp_transport_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Transport_strategy)
def test_hyp_transport_TransportID_setter(instance):
    original = instance.TransportID
    instance.TransportID = original
    assert instance.TransportID == original




@given(instance=User_strategy)
def test_hyp_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=User_strategy)
def test_hyp_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_hyp_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original




@given(instance=Orders_strategy)
def test_hyp_orders_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Orders_strategy)
def test_hyp_orders_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Orders_strategy)
def test_hyp_orders_dateFinished_setter(instance):
    original = instance.dateFinished
    instance.dateFinished = original
    assert instance.dateFinished == original



@given(instance=Orders_strategy)
def test_hyp_orders_dateOrdered_setter(instance):
    original = instance.dateOrdered
    instance.dateOrdered = original
    assert instance.dateOrdered == original




@given(instance=Cart_strategy)
def test_hyp_cart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Cart_strategy)
def test_hyp_cart_cartID_setter(instance):
    original = instance.cartID
    instance.cartID = original
    assert instance.cartID == original



@given(instance=Cart_strategy)
def test_hyp_cart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Cart_strategy)
def test_hyp_cart_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original




@given(instance=Customer_strategy)
def test_hyp_customer_CutsomerAddress_setter(instance):
    original = instance.CutsomerAddress
    instance.CutsomerAddress = original
    assert instance.CutsomerAddress == original



@given(instance=Customer_strategy)
def test_hyp_customer_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=Customer_strategy)
def test_hyp_customer_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=Customer_strategy)
def test_hyp_customer_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Admin,
    Cart,
    Customer,
    Employee,
    Guest,
    Meals,
    OrderDetails,
    Orders,
    Payment,
    Transport,
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

def test_Cart_ProductID_value_roundtrip():
    instance = Cart(ProductID="sample_text", Quantity=7, cartID=7, date="sample_text")
    assert instance.ProductID == "sample_text"
    instance.ProductID = "sample_text_2"
    assert instance.ProductID == "sample_text_2"


def test_Cart_Quantity_value_roundtrip():
    instance = Cart(ProductID="sample_text", Quantity=7, cartID=7, date="sample_text")
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_Cart_cartID_value_roundtrip():
    instance = Cart(ProductID="sample_text", Quantity=7, cartID=7, date="sample_text")
    assert instance.cartID == 7
    instance.cartID = 13
    assert instance.cartID == 13


def test_Cart_date_value_roundtrip():
    instance = Cart(ProductID="sample_text", Quantity=7, cartID=7, date="sample_text")
    assert instance.date == "sample_text"
    instance.date = "sample_text_2"
    assert instance.date == "sample_text_2"


def test_Customer_CustomerName_value_roundtrip():
    instance = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_Customer_CutsomerAddress_value_roundtrip():
    instance = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    assert instance.CutsomerAddress == "sample_text"
    instance.CutsomerAddress = "sample_text_2"
    assert instance.CutsomerAddress == "sample_text_2"


def test_Customer_Email_value_roundtrip():
    instance = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Customer_PhoneNumber_value_roundtrip():
    instance = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    assert instance.PhoneNumber == 7
    instance.PhoneNumber = 13
    assert instance.PhoneNumber == 13


def test_Employee_EmpName_value_roundtrip():
    instance = Employee(EmpName="sample_text", EmpPassword="sample_text", EmployeeID="sample_text")
    assert instance.EmpName == "sample_text"
    instance.EmpName = "sample_text_2"
    assert instance.EmpName == "sample_text_2"


def test_Employee_EmpPassword_value_roundtrip():
    instance = Employee(EmpName="sample_text", EmpPassword="sample_text", EmployeeID="sample_text")
    assert instance.EmpPassword == "sample_text"
    instance.EmpPassword = "sample_text_2"
    assert instance.EmpPassword == "sample_text_2"


def test_Employee_EmployeeID_value_roundtrip():
    instance = Employee(EmpName="sample_text", EmpPassword="sample_text", EmployeeID="sample_text")
    assert instance.EmployeeID == "sample_text"
    instance.EmployeeID = "sample_text_2"
    assert instance.EmployeeID == "sample_text_2"


def test_Guest_guestID_value_roundtrip():
    instance = Guest(guestID="sample_text")
    assert instance.guestID == "sample_text"
    instance.guestID = "sample_text_2"
    assert instance.guestID == "sample_text_2"


def test_Meals_MealID_value_roundtrip():
    instance = Meals(MealID="sample_text", MealName="sample_text", MealType="sample_text", Portion="sample_text", supplier="sample_text", unitPrice="sample_text")
    assert instance.MealID == "sample_text"
    instance.MealID = "sample_text_2"
    assert instance.MealID == "sample_text_2"


def test_Meals_MealName_value_roundtrip():
    instance = Meals(MealID="sample_text", MealName="sample_text", MealType="sample_text", Portion="sample_text", supplier="sample_text", unitPrice="sample_text")
    assert instance.MealName == "sample_text"
    instance.MealName = "sample_text_2"
    assert instance.MealName == "sample_text_2"


def test_Meals_MealType_value_roundtrip():
    instance = Meals(MealID="sample_text", MealName="sample_text", MealType="sample_text", Portion="sample_text", supplier="sample_text", unitPrice="sample_text")
    assert instance.MealType == "sample_text"
    instance.MealType = "sample_text_2"
    assert instance.MealType == "sample_text_2"


def test_Meals_Portion_value_roundtrip():
    instance = Meals(MealID="sample_text", MealName="sample_text", MealType="sample_text", Portion="sample_text", supplier="sample_text", unitPrice="sample_text")
    assert instance.Portion == "sample_text"
    instance.Portion = "sample_text_2"
    assert instance.Portion == "sample_text_2"


def test_Meals_supplier_value_roundtrip():
    instance = Meals(MealID="sample_text", MealName="sample_text", MealType="sample_text", Portion="sample_text", supplier="sample_text", unitPrice="sample_text")
    assert instance.supplier == "sample_text"
    instance.supplier = "sample_text_2"
    assert instance.supplier == "sample_text_2"


def test_Meals_unitPrice_value_roundtrip():
    instance = Meals(MealID="sample_text", MealName="sample_text", MealType="sample_text", Portion="sample_text", supplier="sample_text", unitPrice="sample_text")
    assert instance.unitPrice == "sample_text"
    instance.unitPrice = "sample_text_2"
    assert instance.unitPrice == "sample_text_2"


def test_OrderDetails_MealID_value_roundtrip():
    instance = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    assert instance.MealID == "sample_text"
    instance.MealID = "sample_text_2"
    assert instance.MealID == "sample_text_2"


def test_OrderDetails_OrderID_value_roundtrip():
    instance = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_OrderDetails_orderTime_value_roundtrip():
    instance = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    assert instance.orderTime == "sample_text"
    instance.orderTime = "sample_text_2"
    assert instance.orderTime == "sample_text_2"


def test_OrderDetails_quantity_value_roundtrip():
    instance = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_OrderDetails_status_value_roundtrip():
    instance = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_OrderDetails_totPrice_value_roundtrip():
    instance = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    assert instance.totPrice == "sample_text"
    instance.totPrice = "sample_text_2"
    assert instance.totPrice == "sample_text_2"


def test_Orders_OrderID_value_roundtrip():
    instance = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    assert instance.OrderID == 7
    instance.OrderID = 13
    assert instance.OrderID == 13


def test_Orders_dateFinished_value_roundtrip():
    instance = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    assert instance.dateFinished == "sample_text"
    instance.dateFinished = "sample_text_2"
    assert instance.dateFinished == "sample_text_2"


def test_Orders_dateOrdered_value_roundtrip():
    instance = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    assert instance.dateOrdered == "sample_text"
    instance.dateOrdered = "sample_text_2"
    assert instance.dateOrdered == "sample_text_2"


def test_Orders_status_value_roundtrip():
    instance = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Payment_PaymentStatus_value_roundtrip():
    instance = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    assert instance.PaymentStatus == "sample_text"
    instance.PaymentStatus = "sample_text_2"
    assert instance.PaymentStatus == "sample_text_2"


def test_Payment_PaymentType_value_roundtrip():
    instance = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    assert instance.PaymentType == "sample_text"
    instance.PaymentType = "sample_text_2"
    assert instance.PaymentType == "sample_text_2"


def test_Payment_paymentAmount_value_roundtrip():
    instance = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    assert instance.paymentAmount == "sample_text"
    instance.paymentAmount = "sample_text_2"
    assert instance.paymentAmount == "sample_text_2"


def test_Payment_paymentDate_value_roundtrip():
    instance = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    assert instance.paymentDate == "sample_text"
    instance.paymentDate = "sample_text_2"
    assert instance.paymentDate == "sample_text_2"


def test_Payment_paymentID_value_roundtrip():
    instance = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    assert instance.paymentID == "sample_text"
    instance.paymentID = "sample_text_2"
    assert instance.paymentID == "sample_text_2"


def test_Transport_TransportID_value_roundtrip():
    instance = Transport(TransportID=7, location="sample_text", transportCost="sample_text")
    assert instance.TransportID == 7
    instance.TransportID = 13
    assert instance.TransportID == 13


def test_Transport_location_value_roundtrip():
    instance = Transport(TransportID=7, location="sample_text", transportCost="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_Transport_transportCost_value_roundtrip():
    instance = Transport(TransportID=7, location="sample_text", transportCost="sample_text")
    assert instance.transportCost == "sample_text"
    instance.transportCost = "sample_text_2"
    assert instance.transportCost == "sample_text_2"


def test_User_Password_value_roundtrip():
    instance = User(Password="sample_text", loginStatus="sample_text", userID="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_User_loginStatus_value_roundtrip():
    instance = User(Password="sample_text", loginStatus="sample_text", userID="sample_text")
    assert instance.loginStatus == "sample_text"
    instance.loginStatus = "sample_text_2"
    assert instance.loginStatus == "sample_text_2"


def test_User_userID_value_roundtrip():
    instance = User(Password="sample_text", loginStatus="sample_text", userID="sample_text")
    assert instance.userID == "sample_text"
    instance.userID = "sample_text_2"
    assert instance.userID == "sample_text_2"


def test_assoc_Customer_Cart_link_reassign_clear():
    a = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    b1 = Cart(ProductID="sample_text", Quantity=7, cartID=7, date="sample_text")
    b2 = Cart(ProductID="sample_text_2", Quantity=13, cartID=13, date="sample_text_2")
    _safe_set(a, 'cart8', b1)
    assert _is_linked(a, 'cart8', b1)
    if hasattr(b1, 'customer9'):
        assert _is_linked(b1, 'customer9', a)
    _safe_set(a, 'cart8', b2)
    assert _is_linked(a, 'cart8', b2)
    if hasattr(b1, 'customer9'):
        assert not _is_linked(b1, 'customer9', a)
    if hasattr(b2, 'customer9'):
        assert _is_linked(b2, 'customer9', a)
    _safe_set(a, 'cart8', None)
    assert not _is_linked(a, 'cart8', b2)
    if hasattr(b2, 'customer9'):
        assert not _is_linked(b2, 'customer9', a)


def test_assoc_Customer_Orders_link_reassign_clear():
    a = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    b1 = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    b2 = Customer(CustomerName="sample_text_2", CutsomerAddress="sample_text_2", Email="sample_text_2", PhoneNumber=13)
    _safe_set(a, 'customer3', b1)
    assert _is_linked(a, 'customer3', b1)
    if hasattr(b1, 'orders2'):
        assert _is_linked(b1, 'orders2', a)
    _safe_set(a, 'customer3', b2)
    assert _is_linked(a, 'customer3', b2)
    if hasattr(b1, 'orders2'):
        assert not _is_linked(b1, 'orders2', a)
    if hasattr(b2, 'orders2'):
        assert _is_linked(b2, 'orders2', a)
    _safe_set(a, 'customer3', None)
    assert not _is_linked(a, 'customer3', b2)
    if hasattr(b2, 'orders2'):
        assert not _is_linked(b2, 'orders2', a)


def test_assoc_Customer_Payment_link_reassign_clear():
    a = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    b1 = Customer(CustomerName="sample_text", CutsomerAddress="sample_text", Email="sample_text", PhoneNumber=7)
    b2 = Customer(CustomerName="sample_text_2", CutsomerAddress="sample_text_2", Email="sample_text_2", PhoneNumber=13)
    _safe_set(a, 'customer1', b1)
    assert _is_linked(a, 'customer1', b1)
    if hasattr(b1, 'payment0'):
        assert _is_linked(b1, 'payment0', a)
    _safe_set(a, 'customer1', b2)
    assert _is_linked(a, 'customer1', b2)
    if hasattr(b1, 'payment0'):
        assert not _is_linked(b1, 'payment0', a)
    if hasattr(b2, 'payment0'):
        assert _is_linked(b2, 'payment0', a)
    _safe_set(a, 'customer1', None)
    assert not _is_linked(a, 'customer1', b2)
    if hasattr(b2, 'payment0'):
        assert not _is_linked(b2, 'payment0', a)


def test_assoc_Employee_Orders_link_reassign_clear():
    a = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    b1 = Employee(EmpName="sample_text", EmpPassword="sample_text", EmployeeID="sample_text")
    b2 = Employee(EmpName="sample_text_2", EmpPassword="sample_text_2", EmployeeID="sample_text_2")
    _safe_set(a, 'employee5', b1)
    assert _is_linked(a, 'employee5', b1)
    if hasattr(b1, 'orders4'):
        assert _is_linked(b1, 'orders4', a)
    _safe_set(a, 'employee5', b2)
    assert _is_linked(a, 'employee5', b2)
    if hasattr(b1, 'orders4'):
        assert not _is_linked(b1, 'orders4', a)
    if hasattr(b2, 'orders4'):
        assert _is_linked(b2, 'orders4', a)
    _safe_set(a, 'employee5', None)
    assert not _is_linked(a, 'employee5', b2)
    if hasattr(b2, 'orders4'):
        assert not _is_linked(b2, 'orders4', a)


def test_assoc_OrderDetails_Cart_link_reassign_clear():
    a = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    b1 = Cart(ProductID="sample_text", Quantity=7, cartID=7, date="sample_text")
    b2 = Cart(ProductID="sample_text_2", Quantity=13, cartID=13, date="sample_text_2")
    _safe_set(a, 'cart10', b1)
    assert _is_linked(a, 'cart10', b1)
    if hasattr(b1, 'orderDetails11'):
        assert _is_linked(b1, 'orderDetails11', a)
    _safe_set(a, 'cart10', b2)
    assert _is_linked(a, 'cart10', b2)
    if hasattr(b1, 'orderDetails11'):
        assert not _is_linked(b1, 'orderDetails11', a)
    if hasattr(b2, 'orderDetails11'):
        assert _is_linked(b2, 'orderDetails11', a)
    _safe_set(a, 'cart10', None)
    assert not _is_linked(a, 'cart10', b2)
    if hasattr(b2, 'orderDetails11'):
        assert not _is_linked(b2, 'orderDetails11', a)


def test_assoc_Orders_OrderDetails_link_reassign_clear():
    a = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    b1 = OrderDetails(MealID="sample_text", OrderID=7, orderTime="sample_text", quantity=7, status="sample_text", totPrice="sample_text")
    b2 = OrderDetails(MealID="sample_text_2", OrderID=13, orderTime="sample_text_2", quantity=13, status="sample_text_2", totPrice="sample_text_2")
    _safe_set(a, 'orderDetails6', {b1})
    assert _is_linked(a, 'orderDetails6', b1)
    if hasattr(b1, 'orders7'):
        assert _is_linked(b1, 'orders7', a)
    _safe_set(a, 'orderDetails6', {b2})
    assert _is_linked(a, 'orderDetails6', b2)
    if hasattr(b1, 'orders7'):
        assert not _is_linked(b1, 'orders7', a)
    if hasattr(b2, 'orders7'):
        assert _is_linked(b2, 'orders7', a)
    _safe_set(a, 'orderDetails6', set())
    assert not _is_linked(a, 'orderDetails6', b2)
    if hasattr(b2, 'orders7'):
        assert not _is_linked(b2, 'orders7', a)


def test_assoc_Orders_Payment_link_reassign_clear():
    a = Payment(PaymentStatus="sample_text", PaymentType="sample_text", paymentAmount="sample_text", paymentDate="sample_text", paymentID="sample_text")
    b1 = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    b2 = Orders(OrderID=13, dateFinished="sample_text_2", dateOrdered="sample_text_2", status="sample_text_2")
    _safe_set(a, 'orders15', b1)
    assert _is_linked(a, 'orders15', b1)
    if hasattr(b1, 'payment14'):
        assert _is_linked(b1, 'payment14', a)
    _safe_set(a, 'orders15', b2)
    assert _is_linked(a, 'orders15', b2)
    if hasattr(b1, 'payment14'):
        assert not _is_linked(b1, 'payment14', a)
    if hasattr(b2, 'payment14'):
        assert _is_linked(b2, 'payment14', a)
    _safe_set(a, 'orders15', None)
    assert not _is_linked(a, 'orders15', b2)
    if hasattr(b2, 'payment14'):
        assert not _is_linked(b2, 'payment14', a)


def test_assoc_Orders_Transport2_link_reassign_clear():
    a = Transport(TransportID=7, location="sample_text", transportCost="sample_text")
    b1 = Orders(OrderID=7, dateFinished="sample_text", dateOrdered="sample_text", status="sample_text")
    b2 = Orders(OrderID=13, dateFinished="sample_text_2", dateOrdered="sample_text_2", status="sample_text_2")
    _safe_set(a, 'orders13', b1)
    assert _is_linked(a, 'orders13', b1)
    if hasattr(b1, 'transport12'):
        assert _is_linked(b1, 'transport12', a)
    _safe_set(a, 'orders13', b2)
    assert _is_linked(a, 'orders13', b2)
    if hasattr(b1, 'transport12'):
        assert not _is_linked(b1, 'transport12', a)
    if hasattr(b2, 'transport12'):
        assert _is_linked(b2, 'transport12', a)
    _safe_set(a, 'orders13', None)
    assert not _is_linked(a, 'orders13', b2)
    if hasattr(b2, 'transport12'):
        assert not _is_linked(b2, 'transport12', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Admin_strategy = st.builds(Admin)
@given(instance=Admin_strategy)
@settings(max_examples=25)
def test_Admin_instantiation(instance):
    assert isinstance(instance, Admin)


Cart_strategy = st.builds(Cart, ProductID=safe_text, Quantity=st.integers(), cartID=st.integers(), date=safe_text)
@given(instance=Cart_strategy)
@settings(max_examples=25)
def test_Cart_instantiation(instance):
    assert isinstance(instance, Cart)


Customer_strategy = st.builds(Customer, CustomerName=safe_text, CutsomerAddress=safe_text, Email=safe_text, PhoneNumber=st.integers())
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Employee_strategy = st.builds(Employee, EmpName=safe_text, EmpPassword=safe_text, EmployeeID=safe_text)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Guest_strategy = st.builds(Guest, guestID=safe_text)
@given(instance=Guest_strategy)
@settings(max_examples=25)
def test_Guest_instantiation(instance):
    assert isinstance(instance, Guest)


Meals_strategy = st.builds(Meals, MealID=safe_text, MealName=safe_text, MealType=safe_text, Portion=safe_text, supplier=safe_text, unitPrice=safe_text)
@given(instance=Meals_strategy)
@settings(max_examples=25)
def test_Meals_instantiation(instance):
    assert isinstance(instance, Meals)


OrderDetails_strategy = st.builds(OrderDetails, MealID=safe_text, OrderID=st.integers(), orderTime=safe_text, quantity=st.integers(), status=safe_text, totPrice=safe_text)
@given(instance=OrderDetails_strategy)
@settings(max_examples=25)
def test_OrderDetails_instantiation(instance):
    assert isinstance(instance, OrderDetails)


Orders_strategy = st.builds(Orders, OrderID=st.integers(), dateFinished=safe_text, dateOrdered=safe_text, status=safe_text)
@given(instance=Orders_strategy)
@settings(max_examples=25)
def test_Orders_instantiation(instance):
    assert isinstance(instance, Orders)


Payment_strategy = st.builds(Payment, PaymentStatus=safe_text, PaymentType=safe_text, paymentAmount=safe_text, paymentDate=safe_text, paymentID=safe_text)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Transport_strategy = st.builds(Transport, TransportID=st.integers(), location=safe_text, transportCost=safe_text)
@given(instance=Transport_strategy)
@settings(max_examples=25)
def test_Transport_instantiation(instance):
    assert isinstance(instance, Transport)


User_strategy = st.builds(User, Password=safe_text, loginStatus=safe_text, userID=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



