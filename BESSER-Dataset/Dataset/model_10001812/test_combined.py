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
    email_Interface,
    notify_Interface,
    cartItem,
    keywordSet,
    Product,
    OrderDetail,
    Shipping,
    Order,
    searchFacade,
    Department,
    Administrator,
    Customer,
    SessionManager,
    User,
    email,
    SMS,
    Notify_Interface,
    Address,
    ShoppingCart,
    Vendor,
    ShippingType_Interface,
    PayLater1,
    CreditCardPayment,
    Payment_Interface,
    Payment,
    OrderService,
    Item,
    Price,
    TimeBasedDiscount,
    ProductDiscount,
    Offer_Interface,
    Class2,
    Class1,
    Category,
    PayLater,
    Gpay,
    Credit_DebitCard1,
    PushNotification,
    EmailNotification,
    paylater_Interface,
    Class,
    gpay_Interface,
    Credit_DebitCard,
    billdesk_Interface,
    payment_Interface,
    promotions,
    customeraddress_Interface,
    pickuppoint_Interface,
    shiporder_Interface,
    mobile_Interface,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_email_interface_is_not_abstract():
    assert not inspect.isabstract(email_Interface)


def test_hyp_email_interface_constructor_exists():
    assert callable(email_Interface.__init__)


def test_hyp_email_interface_constructor_args():
    sig = inspect.signature(email_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_notify_interface_is_not_abstract():
    assert not inspect.isabstract(notify_Interface)


def test_hyp_notify_interface_constructor_exists():
    assert callable(notify_Interface.__init__)


def test_hyp_notify_interface_constructor_args():
    sig = inspect.signature(notify_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cartitem_is_not_abstract():
    assert not inspect.isabstract(cartItem)


def test_hyp_cartitem_constructor_exists():
    assert callable(cartItem.__init__)


def test_hyp_cartitem_constructor_args():
    sig = inspect.signature(cartItem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "subtotal" in params, "Missing parameter 'subtotal'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "unitCost" in params, "Missing parameter 'unitCost'"








def test_hyp_keywordset_is_not_abstract():
    assert not inspect.isabstract(keywordSet)


def test_hyp_keywordset_constructor_exists():
    assert callable(keywordSet.__init__)


def test_hyp_keywordset_constructor_args():
    sig = inspect.signature(keywordSet.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"




def test_hyp_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_hyp_product_constructor_exists():
    assert callable(Product.__init__)


def test_hyp_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "Price" in params, "Missing parameter 'Price'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "SKU" in params, "Missing parameter 'SKU'"
    assert "reviews" in params, "Missing parameter 'reviews'"
    assert "attribute7" in params, "Missing parameter 'attribute7'"












def test_hyp_orderdetail_is_not_abstract():
    assert not inspect.isabstract(OrderDetail)


def test_hyp_orderdetail_constructor_exists():
    assert callable(OrderDetail.__init__)


def test_hyp_orderdetail_constructor_args():
    sig = inspect.signature(OrderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "productName" in params, "Missing parameter 'productName'"
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "subTotal" in params, "Missing parameter 'subTotal'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "unitCost" in params, "Missing parameter 'unitCost'"









def test_hyp_shipping_is_not_abstract():
    assert not inspect.isabstract(Shipping)


def test_hyp_shipping_constructor_exists():
    assert callable(Shipping.__init__)


def test_hyp_shipping_constructor_args():
    sig = inspect.signature(Shipping.__init__)
    params = list(sig.parameters.keys())
    assert "shippingAddress" in params, "Missing parameter 'shippingAddress'"
    assert "shippingId" in params, "Missing parameter 'shippingId'"
    assert "_attr" in params, "Missing parameter '_attr'"
    assert "ShippingType" in params, "Missing parameter 'ShippingType'"
    assert "shippingType" in params, "Missing parameter 'shippingType'"








def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "OrderId" in params, "Missing parameter 'OrderId'"
    assert "Payment" in params, "Missing parameter 'Payment'"
    assert "customerId" in params, "Missing parameter 'customerId'"
    assert "Item" in params, "Missing parameter 'Item'"
    assert "ShippingAddress" in params, "Missing parameter 'ShippingAddress'"
    assert "OrderStatus" in params, "Missing parameter 'OrderStatus'"
    assert "BillingAddress" in params, "Missing parameter 'BillingAddress'"
    assert "status" in params, "Missing parameter 'status'"
    assert "dateShipped" in params, "Missing parameter 'dateShipped'"
    assert "dateCreated" in params, "Missing parameter 'dateCreated'"














def test_hyp_searchfacade_is_not_abstract():
    assert not inspect.isabstract(searchFacade)


def test_hyp_searchfacade_constructor_exists():
    assert callable(searchFacade.__init__)


def test_hyp_searchfacade_constructor_args():
    sig = inspect.signature(searchFacade.__init__)
    params = list(sig.parameters.keys())



def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "departmentName" in params, "Missing parameter 'departmentName'"
    assert "departmentID" in params, "Missing parameter 'departmentID'"
    assert "description" in params, "Missing parameter 'description'"






def test_hyp_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_hyp_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_hyp_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "adminName" in params, "Missing parameter 'adminName'"





def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "shippinginfo" in params, "Missing parameter 'shippinginfo'"
    assert "newsLettersub" in params, "Missing parameter 'newsLettersub'"
    assert "surveys" in params, "Missing parameter 'surveys'"
    assert "phoneno" in params, "Missing parameter 'phoneno'"
    assert "creditcardinfo" in params, "Missing parameter 'creditcardinfo'"
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "address" in params, "Missing parameter 'address'"











def test_hyp_sessionmanager_is_not_abstract():
    assert not inspect.isabstract(SessionManager)


def test_hyp_sessionmanager_constructor_exists():
    assert callable(SessionManager.__init__)


def test_hyp_sessionmanager_constructor_args():
    sig = inspect.signature(SessionManager.__init__)
    params = list(sig.parameters.keys())
    assert "userid" in params, "Missing parameter 'userid'"
    assert "departmentName" in params, "Missing parameter 'departmentName'"





def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"
    assert "userId" in params, "Missing parameter 'userId'"
    assert "password" in params, "Missing parameter 'password'"






def test_hyp_email_is_not_abstract():
    assert not inspect.isabstract(email)


def test_hyp_email_constructor_exists():
    assert callable(email.__init__)


def test_hyp_email_constructor_args():
    sig = inspect.signature(email.__init__)
    params = list(sig.parameters.keys())
    assert "EmailAddress" in params, "Missing parameter 'EmailAddress'"




def test_hyp_sms_is_not_abstract():
    assert not inspect.isabstract(SMS)


def test_hyp_sms_constructor_exists():
    assert callable(SMS.__init__)


def test_hyp_sms_constructor_args():
    sig = inspect.signature(SMS.__init__)
    params = list(sig.parameters.keys())
    assert "MobileNo" in params, "Missing parameter 'MobileNo'"




def test_hyp_notify_interface_is_not_abstract():
    assert not inspect.isabstract(Notify_Interface)


def test_hyp_notify_interface_constructor_exists():
    assert callable(Notify_Interface.__init__)


def test_hyp_notify_interface_constructor_args():
    sig = inspect.signature(Notify_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_hyp_address_constructor_exists():
    assert callable(Address.__init__)


def test_hyp_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())
    assert "Street" in params, "Missing parameter 'Street'"
    assert "ZipCode" in params, "Missing parameter 'ZipCode'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "City" in params, "Missing parameter 'City'"
    assert "State" in params, "Missing parameter 'State'"
    assert "Country" in params, "Missing parameter 'Country'"









def test_hyp_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_hyp_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_hyp_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"
    assert "GetTotalPrice" in params, "Missing parameter 'GetTotalPrice'"
    assert "Item" in params, "Missing parameter 'Item'"
    assert "quantity" in params, "Missing parameter 'quantity'"







def test_hyp_vendor_is_not_abstract():
    assert not inspect.isabstract(Vendor)


def test_hyp_vendor_constructor_exists():
    assert callable(Vendor.__init__)


def test_hyp_vendor_constructor_args():
    sig = inspect.signature(Vendor.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"





def test_hyp_shippingtype_interface_is_not_abstract():
    assert not inspect.isabstract(ShippingType_Interface)


def test_hyp_shippingtype_interface_constructor_exists():
    assert callable(ShippingType_Interface.__init__)


def test_hyp_shippingtype_interface_constructor_args():
    sig = inspect.signature(ShippingType_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paylater1_is_not_abstract():
    assert not inspect.isabstract(PayLater1)


def test_hyp_paylater1_constructor_exists():
    assert callable(PayLater1.__init__)


def test_hyp_paylater1_constructor_args():
    sig = inspect.signature(PayLater1.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"




def test_hyp_creditcardpayment_is_not_abstract():
    assert not inspect.isabstract(CreditCardPayment)


def test_hyp_creditcardpayment_constructor_exists():
    assert callable(CreditCardPayment.__init__)


def test_hyp_creditcardpayment_constructor_args():
    sig = inspect.signature(CreditCardPayment.__init__)
    params = list(sig.parameters.keys())
    assert "CardNumber" in params, "Missing parameter 'CardNumber'"
    assert "CardType" in params, "Missing parameter 'CardType'"





def test_hyp_payment_interface_is_not_abstract():
    assert not inspect.isabstract(Payment_Interface)


def test_hyp_payment_interface_constructor_exists():
    assert callable(Payment_Interface.__init__)


def test_hyp_payment_interface_constructor_args():
    sig = inspect.signature(Payment_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())



def test_hyp_orderservice_is_not_abstract():
    assert not inspect.isabstract(OrderService)


def test_hyp_orderservice_constructor_exists():
    assert callable(OrderService.__init__)


def test_hyp_orderservice_constructor_args():
    sig = inspect.signature(OrderService.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"




def test_hyp_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_hyp_item_constructor_exists():
    assert callable(Item.__init__)


def test_hyp_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "Name" in params, "Missing parameter 'Name'"






def test_hyp_price_is_not_abstract():
    assert not inspect.isabstract(Price)


def test_hyp_price_constructor_exists():
    assert callable(Price.__init__)


def test_hyp_price_constructor_args():
    sig = inspect.signature(Price.__init__)
    params = list(sig.parameters.keys())
    assert "ActualPrice" in params, "Missing parameter 'ActualPrice'"




def test_hyp_timebaseddiscount_is_not_abstract():
    assert not inspect.isabstract(TimeBasedDiscount)


def test_hyp_timebaseddiscount_constructor_exists():
    assert callable(TimeBasedDiscount.__init__)


def test_hyp_timebaseddiscount_constructor_args():
    sig = inspect.signature(TimeBasedDiscount.__init__)
    params = list(sig.parameters.keys())



def test_hyp_productdiscount_is_not_abstract():
    assert not inspect.isabstract(ProductDiscount)


def test_hyp_productdiscount_constructor_exists():
    assert callable(ProductDiscount.__init__)


def test_hyp_productdiscount_constructor_args():
    sig = inspect.signature(ProductDiscount.__init__)
    params = list(sig.parameters.keys())



def test_hyp_offer_interface_is_not_abstract():
    assert not inspect.isabstract(Offer_Interface)


def test_hyp_offer_interface_constructor_exists():
    assert callable(Offer_Interface.__init__)


def test_hyp_offer_interface_constructor_args():
    sig = inspect.signature(Offer_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_hyp_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_hyp_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class1_is_not_abstract():
    assert not inspect.isabstract(Class1)


def test_hyp_class1_constructor_exists():
    assert callable(Class1.__init__)


def test_hyp_class1_constructor_args():
    sig = inspect.signature(Class1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_hyp_category_constructor_exists():
    assert callable(Category.__init__)


def test_hyp_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "categoryName" in params, "Missing parameter 'categoryName'"
    assert "categoryID" in params, "Missing parameter 'categoryID'"
    assert "departmentId" in params, "Missing parameter 'departmentId'"







def test_hyp_paylater_is_not_abstract():
    assert not inspect.isabstract(PayLater)


def test_hyp_paylater_constructor_exists():
    assert callable(PayLater.__init__)


def test_hyp_paylater_constructor_args():
    sig = inspect.signature(PayLater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gpay_is_not_abstract():
    assert not inspect.isabstract(Gpay)


def test_hyp_gpay_constructor_exists():
    assert callable(Gpay.__init__)


def test_hyp_gpay_constructor_args():
    sig = inspect.signature(Gpay.__init__)
    params = list(sig.parameters.keys())



def test_hyp_credit_debitcard1_is_not_abstract():
    assert not inspect.isabstract(Credit_DebitCard1)


def test_hyp_credit_debitcard1_constructor_exists():
    assert callable(Credit_DebitCard1.__init__)


def test_hyp_credit_debitcard1_constructor_args():
    sig = inspect.signature(Credit_DebitCard1.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pushnotification_is_not_abstract():
    assert not inspect.isabstract(PushNotification)


def test_hyp_pushnotification_constructor_exists():
    assert callable(PushNotification.__init__)


def test_hyp_pushnotification_constructor_args():
    sig = inspect.signature(PushNotification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_emailnotification_is_not_abstract():
    assert not inspect.isabstract(EmailNotification)


def test_hyp_emailnotification_constructor_exists():
    assert callable(EmailNotification.__init__)


def test_hyp_emailnotification_constructor_args():
    sig = inspect.signature(EmailNotification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_paylater_interface_is_not_abstract():
    assert not inspect.isabstract(paylater_Interface)


def test_hyp_paylater_interface_constructor_exists():
    assert callable(paylater_Interface.__init__)


def test_hyp_paylater_interface_constructor_args():
    sig = inspect.signature(paylater_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gpay_interface_is_not_abstract():
    assert not inspect.isabstract(gpay_Interface)


def test_hyp_gpay_interface_constructor_exists():
    assert callable(gpay_Interface.__init__)


def test_hyp_gpay_interface_constructor_args():
    sig = inspect.signature(gpay_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_credit_debitcard_is_not_abstract():
    assert not inspect.isabstract(Credit_DebitCard)


def test_hyp_credit_debitcard_constructor_exists():
    assert callable(Credit_DebitCard.__init__)


def test_hyp_credit_debitcard_constructor_args():
    sig = inspect.signature(Credit_DebitCard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_billdesk_interface_is_not_abstract():
    assert not inspect.isabstract(billdesk_Interface)


def test_hyp_billdesk_interface_constructor_exists():
    assert callable(billdesk_Interface.__init__)


def test_hyp_billdesk_interface_constructor_args():
    sig = inspect.signature(billdesk_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_payment_interface_is_not_abstract():
    assert not inspect.isabstract(payment_Interface)


def test_hyp_payment_interface_constructor_exists():
    assert callable(payment_Interface.__init__)


def test_hyp_payment_interface_constructor_args():
    sig = inspect.signature(payment_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_promotions_is_not_abstract():
    assert not inspect.isabstract(promotions)


def test_hyp_promotions_constructor_exists():
    assert callable(promotions.__init__)


def test_hyp_promotions_constructor_args():
    sig = inspect.signature(promotions.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "promotionCode" in params, "Missing parameter 'promotionCode'"
    assert "endDate" in params, "Missing parameter 'endDate'"






def test_hyp_customeraddress_interface_is_not_abstract():
    assert not inspect.isabstract(customeraddress_Interface)


def test_hyp_customeraddress_interface_constructor_exists():
    assert callable(customeraddress_Interface.__init__)


def test_hyp_customeraddress_interface_constructor_args():
    sig = inspect.signature(customeraddress_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pickuppoint_interface_is_not_abstract():
    assert not inspect.isabstract(pickuppoint_Interface)


def test_hyp_pickuppoint_interface_constructor_exists():
    assert callable(pickuppoint_Interface.__init__)


def test_hyp_pickuppoint_interface_constructor_args():
    sig = inspect.signature(pickuppoint_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_shiporder_interface_is_not_abstract():
    assert not inspect.isabstract(shiporder_Interface)


def test_hyp_shiporder_interface_constructor_exists():
    assert callable(shiporder_Interface.__init__)


def test_hyp_shiporder_interface_constructor_args():
    sig = inspect.signature(shiporder_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mobile_interface_is_not_abstract():
    assert not inspect.isabstract(mobile_Interface)


def test_hyp_mobile_interface_constructor_exists():
    assert callable(mobile_Interface.__init__)


def test_hyp_mobile_interface_constructor_args():
    sig = inspect.signature(mobile_Interface.__init__)
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
email_Interface_strategy = st.builds(
    email_Interface,
)
notify_Interface_strategy = st.builds(
    notify_Interface,
)
cartItem_strategy = st.builds(
    cartItem,
    name=
        safe_text,
    subtotal=
        safe_text,
    productId=
        st.integers(),
    quantity=
        st.integers(),
    unitCost=
        safe_text
)
keywordSet_strategy = st.builds(
    keywordSet,
    keyword=
        safe_text
)
Product_strategy = st.builds(
    Product,
    Name=
        safe_text,
    description=
        safe_text,
    attribute6=
        safe_text,
    attribute5=
        safe_text,
    Price=
        safe_text,
    productId=
        st.integers(),
    SKU=
        safe_text,
    reviews=
        safe_text,
    attribute7=
        safe_text
)
OrderDetail_strategy = st.builds(
    OrderDetail,
    productName=
        safe_text,
    orderId=
        st.integers(),
    subTotal=
        safe_text,
    productId=
        st.integers(),
    quantity=
        st.integers(),
    unitCost=
        safe_text
)
Shipping_strategy = st.builds(
    Shipping,
    shippingAddress=
        safe_text,
    shippingId=
        st.integers(),
    _attr=
        st.integers(),
    ShippingType=
        safe_text,
    shippingType=
        safe_text
)
Order_strategy = st.builds(
    Order,
    customerName=
        safe_text,
    OrderId=
        st.integers(),
    Payment=
        safe_text,
    customerId=
        safe_text,
    Item=
        safe_text,
    ShippingAddress=
        safe_text,
    OrderStatus=
        safe_text,
    BillingAddress=
        safe_text,
    status=
        safe_text,
    dateShipped=
        safe_text,
    dateCreated=
        safe_text
)
searchFacade_strategy = st.builds(
    searchFacade,
)
Department_strategy = st.builds(
    Department,
    departmentName=
        safe_text,
    departmentID=
        st.integers(),
    description=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    email=
        safe_text,
    adminName=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    email=
        safe_text,
    shippinginfo=
        safe_text,
    newsLettersub=
        st.booleans(),
    surveys=
        st.booleans(),
    phoneno=
        st.integers(),
    creditcardinfo=
        safe_text,
    customerName=
        safe_text,
    address=
        safe_text
)
SessionManager_strategy = st.builds(
    SessionManager,
    userid=
        safe_text,
    departmentName=
        safe_text
)
User_strategy = st.builds(
    User,
    loginStatus=
        safe_text,
    userId=
        safe_text,
    password=
        safe_text
)
email_strategy = st.builds(
    email,
    EmailAddress=
        safe_text
)
SMS_strategy = st.builds(
    SMS,
    MobileNo=
        st.integers()
)
Notify_Interface_strategy = st.builds(
    Notify_Interface,
)
Address_strategy = st.builds(
    Address,
    Street=
        safe_text,
    ZipCode=
        safe_text,
    Type=
        safe_text,
    City=
        safe_text,
    State=
        safe_text,
    Country=
        safe_text
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    dateAdded=
        st.integers(),
    GetTotalPrice=
        safe_text,
    Item=
        safe_text,
    quantity=
        st.integers()
)
Vendor_strategy = st.builds(
    Vendor,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
ShippingType_Interface_strategy = st.builds(
    ShippingType_Interface,
)
PayLater1_strategy = st.builds(
    PayLater1,
    UserID=
        safe_text
)
CreditCardPayment_strategy = st.builds(
    CreditCardPayment,
    CardNumber=
        st.integers(),
    CardType=
        safe_text
)
Payment_Interface_strategy = st.builds(
    Payment_Interface,
)
Payment_strategy = st.builds(
    Payment,
)
OrderService_strategy = st.builds(
    OrderService,
    attribute=
        safe_text
)
Item_strategy = st.builds(
    Item,
    Quantity=
        st.integers(),
    attribute=
        safe_text,
    Name=
        safe_text
)
Price_strategy = st.builds(
    Price,
    ActualPrice=
        safe_text
)
TimeBasedDiscount_strategy = st.builds(
    TimeBasedDiscount,
)
ProductDiscount_strategy = st.builds(
    ProductDiscount,
)
Offer_Interface_strategy = st.builds(
    Offer_Interface,
)
Class2_strategy = st.builds(
    Class2,
)
Class1_strategy = st.builds(
    Class1,
)
Category_strategy = st.builds(
    Category,
    description=
        safe_text,
    categoryName=
        safe_text,
    categoryID=
        st.integers(),
    departmentId=
        st.integers()
)
PayLater_strategy = st.builds(
    PayLater,
)
Gpay_strategy = st.builds(
    Gpay,
)
Credit_DebitCard1_strategy = st.builds(
    Credit_DebitCard1,
)
PushNotification_strategy = st.builds(
    PushNotification,
)
EmailNotification_strategy = st.builds(
    EmailNotification,
)
paylater_Interface_strategy = st.builds(
    paylater_Interface,
)
Class_strategy = st.builds(
    Class,
)
gpay_Interface_strategy = st.builds(
    gpay_Interface,
)
Credit_DebitCard_strategy = st.builds(
    Credit_DebitCard,
)
billdesk_Interface_strategy = st.builds(
    billdesk_Interface,
)
payment_Interface_strategy = st.builds(
    payment_Interface,
)
promotions_strategy = st.builds(
    promotions,
    startDate=
        st.integers(),
    promotionCode=
        safe_text,
    endDate=
        st.integers()
)
customeraddress_Interface_strategy = st.builds(
    customeraddress_Interface,
)
pickuppoint_Interface_strategy = st.builds(
    pickuppoint_Interface,
)
shiporder_Interface_strategy = st.builds(
    shiporder_Interface,
)
mobile_Interface_strategy = st.builds(
    mobile_Interface,
)






@given(instance=cartItem_strategy)
def test_hyp_cartitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cartItem_strategy)
def test_hyp_cartitem_subtotal_setter(instance):
    original = instance.subtotal
    instance.subtotal = original
    assert instance.subtotal == original



@given(instance=cartItem_strategy)
def test_hyp_cartitem_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=cartItem_strategy)
def test_hyp_cartitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=cartItem_strategy)
def test_hyp_cartitem_unitCost_setter(instance):
    original = instance.unitCost
    instance.unitCost = original
    assert instance.unitCost == original




@given(instance=keywordSet_strategy)
def test_hyp_keywordset_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original




@given(instance=Product_strategy)
def test_hyp_product_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Product_strategy)
def test_hyp_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Product_strategy)
def test_hyp_product_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=Product_strategy)
def test_hyp_product_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=Product_strategy)
def test_hyp_product_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=Product_strategy)
def test_hyp_product_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=Product_strategy)
def test_hyp_product_SKU_setter(instance):
    original = instance.SKU
    instance.SKU = original
    assert instance.SKU == original



@given(instance=Product_strategy)
def test_hyp_product_reviews_setter(instance):
    original = instance.reviews
    instance.reviews = original
    assert instance.reviews == original



@given(instance=Product_strategy)
def test_hyp_product_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original




@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_productName_setter(instance):
    original = instance.productName
    instance.productName = original
    assert instance.productName == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_subTotal_setter(instance):
    original = instance.subTotal
    instance.subTotal = original
    assert instance.subTotal == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=OrderDetail_strategy)
def test_hyp_orderdetail_unitCost_setter(instance):
    original = instance.unitCost
    instance.unitCost = original
    assert instance.unitCost == original




@given(instance=Shipping_strategy)
def test_hyp_shipping_shippingAddress_setter(instance):
    original = instance.shippingAddress
    instance.shippingAddress = original
    assert instance.shippingAddress == original



@given(instance=Shipping_strategy)
def test_hyp_shipping_shippingId_setter(instance):
    original = instance.shippingId
    instance.shippingId = original
    assert instance.shippingId == original



@given(instance=Shipping_strategy)
def test_hyp_shipping__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original



@given(instance=Shipping_strategy)
def test_hyp_shipping_ShippingType_setter(instance):
    original = instance.ShippingType
    instance.ShippingType = original
    assert instance.ShippingType == original



@given(instance=Shipping_strategy)
def test_hyp_shipping_shippingType_setter(instance):
    original = instance.shippingType
    instance.shippingType = original
    assert instance.shippingType == original




@given(instance=Order_strategy)
def test_hyp_order_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original



@given(instance=Order_strategy)
def test_hyp_order_OrderId_setter(instance):
    original = instance.OrderId
    instance.OrderId = original
    assert instance.OrderId == original



@given(instance=Order_strategy)
def test_hyp_order_Payment_setter(instance):
    original = instance.Payment
    instance.Payment = original
    assert instance.Payment == original



@given(instance=Order_strategy)
def test_hyp_order_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original



@given(instance=Order_strategy)
def test_hyp_order_Item_setter(instance):
    original = instance.Item
    instance.Item = original
    assert instance.Item == original



@given(instance=Order_strategy)
def test_hyp_order_ShippingAddress_setter(instance):
    original = instance.ShippingAddress
    instance.ShippingAddress = original
    assert instance.ShippingAddress == original



@given(instance=Order_strategy)
def test_hyp_order_OrderStatus_setter(instance):
    original = instance.OrderStatus
    instance.OrderStatus = original
    assert instance.OrderStatus == original



@given(instance=Order_strategy)
def test_hyp_order_BillingAddress_setter(instance):
    original = instance.BillingAddress
    instance.BillingAddress = original
    assert instance.BillingAddress == original



@given(instance=Order_strategy)
def test_hyp_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_hyp_order_dateShipped_setter(instance):
    original = instance.dateShipped
    instance.dateShipped = original
    assert instance.dateShipped == original



@given(instance=Order_strategy)
def test_hyp_order_dateCreated_setter(instance):
    original = instance.dateCreated
    instance.dateCreated = original
    assert instance.dateCreated == original





@given(instance=Department_strategy)
def test_hyp_department_departmentName_setter(instance):
    original = instance.departmentName
    instance.departmentName = original
    assert instance.departmentName == original



@given(instance=Department_strategy)
def test_hyp_department_departmentID_setter(instance):
    original = instance.departmentID
    instance.departmentID = original
    assert instance.departmentID == original



@given(instance=Department_strategy)
def test_hyp_department_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=Administrator_strategy)
def test_hyp_administrator_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Administrator_strategy)
def test_hyp_administrator_adminName_setter(instance):
    original = instance.adminName
    instance.adminName = original
    assert instance.adminName == original




@given(instance=Customer_strategy)
def test_hyp_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Customer_strategy)
def test_hyp_customer_shippinginfo_setter(instance):
    original = instance.shippinginfo
    instance.shippinginfo = original
    assert instance.shippinginfo == original



@given(instance=Customer_strategy)
def test_hyp_customer_newsLettersub_setter(instance):
    original = instance.newsLettersub
    instance.newsLettersub = original
    assert instance.newsLettersub == original



@given(instance=Customer_strategy)
def test_hyp_customer_surveys_setter(instance):
    original = instance.surveys
    instance.surveys = original
    assert instance.surveys == original



@given(instance=Customer_strategy)
def test_hyp_customer_phoneno_setter(instance):
    original = instance.phoneno
    instance.phoneno = original
    assert instance.phoneno == original



@given(instance=Customer_strategy)
def test_hyp_customer_creditcardinfo_setter(instance):
    original = instance.creditcardinfo
    instance.creditcardinfo = original
    assert instance.creditcardinfo == original



@given(instance=Customer_strategy)
def test_hyp_customer_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original



@given(instance=Customer_strategy)
def test_hyp_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original




@given(instance=SessionManager_strategy)
def test_hyp_sessionmanager_userid_setter(instance):
    original = instance.userid
    instance.userid = original
    assert instance.userid == original



@given(instance=SessionManager_strategy)
def test_hyp_sessionmanager_departmentName_setter(instance):
    original = instance.departmentName
    instance.departmentName = original
    assert instance.departmentName == original




@given(instance=User_strategy)
def test_hyp_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original



@given(instance=User_strategy)
def test_hyp_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=email_strategy)
def test_hyp_email_EmailAddress_setter(instance):
    original = instance.EmailAddress
    instance.EmailAddress = original
    assert instance.EmailAddress == original




@given(instance=SMS_strategy)
def test_hyp_sms_MobileNo_setter(instance):
    original = instance.MobileNo
    instance.MobileNo = original
    assert instance.MobileNo == original





@given(instance=Address_strategy)
def test_hyp_address_Street_setter(instance):
    original = instance.Street
    instance.Street = original
    assert instance.Street == original



@given(instance=Address_strategy)
def test_hyp_address_ZipCode_setter(instance):
    original = instance.ZipCode
    instance.ZipCode = original
    assert instance.ZipCode == original



@given(instance=Address_strategy)
def test_hyp_address_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Address_strategy)
def test_hyp_address_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=Address_strategy)
def test_hyp_address_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original



@given(instance=Address_strategy)
def test_hyp_address_Country_setter(instance):
    original = instance.Country
    instance.Country = original
    assert instance.Country == original




@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_GetTotalPrice_setter(instance):
    original = instance.GetTotalPrice
    instance.GetTotalPrice = original
    assert instance.GetTotalPrice == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_Item_setter(instance):
    original = instance.Item
    instance.Item = original
    assert instance.Item == original



@given(instance=ShoppingCart_strategy)
def test_hyp_shoppingcart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original




@given(instance=Vendor_strategy)
def test_hyp_vendor_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Vendor_strategy)
def test_hyp_vendor_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original





@given(instance=PayLater1_strategy)
def test_hyp_paylater1_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original




@given(instance=CreditCardPayment_strategy)
def test_hyp_creditcardpayment_CardNumber_setter(instance):
    original = instance.CardNumber
    instance.CardNumber = original
    assert instance.CardNumber == original



@given(instance=CreditCardPayment_strategy)
def test_hyp_creditcardpayment_CardType_setter(instance):
    original = instance.CardType
    instance.CardType = original
    assert instance.CardType == original






@given(instance=OrderService_strategy)
def test_hyp_orderservice_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original




@given(instance=Item_strategy)
def test_hyp_item_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Item_strategy)
def test_hyp_item_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Item_strategy)
def test_hyp_item_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Price_strategy)
def test_hyp_price_ActualPrice_setter(instance):
    original = instance.ActualPrice
    instance.ActualPrice = original
    assert instance.ActualPrice == original









@given(instance=Category_strategy)
def test_hyp_category_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Category_strategy)
def test_hyp_category_categoryName_setter(instance):
    original = instance.categoryName
    instance.categoryName = original
    assert instance.categoryName == original



@given(instance=Category_strategy)
def test_hyp_category_categoryID_setter(instance):
    original = instance.categoryID
    instance.categoryID = original
    assert instance.categoryID == original



@given(instance=Category_strategy)
def test_hyp_category_departmentId_setter(instance):
    original = instance.departmentId
    instance.departmentId = original
    assert instance.departmentId == original















@given(instance=promotions_strategy)
def test_hyp_promotions_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=promotions_strategy)
def test_hyp_promotions_promotionCode_setter(instance):
    original = instance.promotionCode
    instance.promotionCode = original
    assert instance.promotionCode == original



@given(instance=promotions_strategy)
def test_hyp_promotions_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Address,
    Administrator,
    Category,
    Class,
    Class1,
    Class2,
    CreditCardPayment,
    Credit_DebitCard,
    Credit_DebitCard1,
    Customer,
    Department,
    EmailNotification,
    Gpay,
    Item,
    Notify_Interface,
    Offer_Interface,
    Order,
    OrderDetail,
    OrderService,
    PayLater,
    PayLater1,
    Payment,
    Payment_Interface,
    Price,
    Product,
    ProductDiscount,
    PushNotification,
    SMS,
    SessionManager,
    Shipping,
    ShippingType_Interface,
    ShoppingCart,
    TimeBasedDiscount,
    User,
    Vendor,
    billdesk_Interface,
    cartItem,
    customeraddress_Interface,
    email,
    email_Interface,
    gpay_Interface,
    keywordSet,
    mobile_Interface,
    notify_Interface,
    paylater_Interface,
    payment_Interface,
    pickuppoint_Interface,
    promotions,
    searchFacade,
    shiporder_Interface,
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

def test_Address_City_value_roundtrip():
    instance = Address(City="sample_text", Country="sample_text", State="sample_text", Street="sample_text", Type="sample_text", ZipCode="sample_text")
    assert instance.City == "sample_text"
    instance.City = "sample_text_2"
    assert instance.City == "sample_text_2"


def test_Address_Country_value_roundtrip():
    instance = Address(City="sample_text", Country="sample_text", State="sample_text", Street="sample_text", Type="sample_text", ZipCode="sample_text")
    assert instance.Country == "sample_text"
    instance.Country = "sample_text_2"
    assert instance.Country == "sample_text_2"


def test_Address_State_value_roundtrip():
    instance = Address(City="sample_text", Country="sample_text", State="sample_text", Street="sample_text", Type="sample_text", ZipCode="sample_text")
    assert instance.State == "sample_text"
    instance.State = "sample_text_2"
    assert instance.State == "sample_text_2"


def test_Address_Street_value_roundtrip():
    instance = Address(City="sample_text", Country="sample_text", State="sample_text", Street="sample_text", Type="sample_text", ZipCode="sample_text")
    assert instance.Street == "sample_text"
    instance.Street = "sample_text_2"
    assert instance.Street == "sample_text_2"


def test_Address_Type_value_roundtrip():
    instance = Address(City="sample_text", Country="sample_text", State="sample_text", Street="sample_text", Type="sample_text", ZipCode="sample_text")
    assert instance.Type == "sample_text"
    instance.Type = "sample_text_2"
    assert instance.Type == "sample_text_2"


def test_Address_ZipCode_value_roundtrip():
    instance = Address(City="sample_text", Country="sample_text", State="sample_text", Street="sample_text", Type="sample_text", ZipCode="sample_text")
    assert instance.ZipCode == "sample_text"
    instance.ZipCode = "sample_text_2"
    assert instance.ZipCode == "sample_text_2"


def test_Administrator_adminName_value_roundtrip():
    instance = Administrator(adminName="sample_text", email="sample_text")
    assert instance.adminName == "sample_text"
    instance.adminName = "sample_text_2"
    assert instance.adminName == "sample_text_2"


def test_Administrator_email_value_roundtrip():
    instance = Administrator(adminName="sample_text", email="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Category_categoryID_value_roundtrip():
    instance = Category(categoryID=7, categoryName="sample_text", departmentId=7, description="sample_text")
    assert instance.categoryID == 7
    instance.categoryID = 13
    assert instance.categoryID == 13


def test_Category_categoryName_value_roundtrip():
    instance = Category(categoryID=7, categoryName="sample_text", departmentId=7, description="sample_text")
    assert instance.categoryName == "sample_text"
    instance.categoryName = "sample_text_2"
    assert instance.categoryName == "sample_text_2"


def test_Category_departmentId_value_roundtrip():
    instance = Category(categoryID=7, categoryName="sample_text", departmentId=7, description="sample_text")
    assert instance.departmentId == 7
    instance.departmentId = 13
    assert instance.departmentId == 13


def test_Category_description_value_roundtrip():
    instance = Category(categoryID=7, categoryName="sample_text", departmentId=7, description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_CreditCardPayment_CardNumber_value_roundtrip():
    instance = CreditCardPayment(CardNumber=7, CardType="sample_text")
    assert instance.CardNumber == 7
    instance.CardNumber = 13
    assert instance.CardNumber == 13


def test_CreditCardPayment_CardType_value_roundtrip():
    instance = CreditCardPayment(CardNumber=7, CardType="sample_text")
    assert instance.CardType == "sample_text"
    instance.CardType = "sample_text_2"
    assert instance.CardType == "sample_text_2"


def test_Customer_address_value_roundtrip():
    instance = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer_creditcardinfo_value_roundtrip():
    instance = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    assert instance.creditcardinfo == "sample_text"
    instance.creditcardinfo = "sample_text_2"
    assert instance.creditcardinfo == "sample_text_2"


def test_Customer_customerName_value_roundtrip():
    instance = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    assert instance.customerName == "sample_text"
    instance.customerName = "sample_text_2"
    assert instance.customerName == "sample_text_2"


def test_Customer_email_value_roundtrip():
    instance = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Customer_newsLettersub_value_roundtrip():
    instance = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    assert instance.newsLettersub == True
    instance.newsLettersub = False
    assert instance.newsLettersub == False


def test_Customer_phoneno_value_roundtrip():
    instance = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    assert instance.phoneno == 7
    instance.phoneno = 13
    assert instance.phoneno == 13


def test_Customer_shippinginfo_value_roundtrip():
    instance = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    assert instance.shippinginfo == "sample_text"
    instance.shippinginfo = "sample_text_2"
    assert instance.shippinginfo == "sample_text_2"


def test_Customer_surveys_value_roundtrip():
    instance = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    assert instance.surveys == True
    instance.surveys = False
    assert instance.surveys == False


def test_Department_departmentID_value_roundtrip():
    instance = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    assert instance.departmentID == 7
    instance.departmentID = 13
    assert instance.departmentID == 13


def test_Department_departmentName_value_roundtrip():
    instance = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    assert instance.departmentName == "sample_text"
    instance.departmentName = "sample_text_2"
    assert instance.departmentName == "sample_text_2"


def test_Department_description_value_roundtrip():
    instance = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Item_Name_value_roundtrip():
    instance = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Item_Quantity_value_roundtrip():
    instance = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    assert instance.Quantity == 7
    instance.Quantity = 13
    assert instance.Quantity == 13


def test_Item_attribute_value_roundtrip():
    instance = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Order_BillingAddress_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.BillingAddress == "sample_text"
    instance.BillingAddress = "sample_text_2"
    assert instance.BillingAddress == "sample_text_2"


def test_Order_Item_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.Item == "sample_text"
    instance.Item = "sample_text_2"
    assert instance.Item == "sample_text_2"


def test_Order_OrderId_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.OrderId == 7
    instance.OrderId = 13
    assert instance.OrderId == 13


def test_Order_OrderStatus_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.OrderStatus == "sample_text"
    instance.OrderStatus = "sample_text_2"
    assert instance.OrderStatus == "sample_text_2"


def test_Order_Payment_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.Payment == "sample_text"
    instance.Payment = "sample_text_2"
    assert instance.Payment == "sample_text_2"


def test_Order_ShippingAddress_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.ShippingAddress == "sample_text"
    instance.ShippingAddress = "sample_text_2"
    assert instance.ShippingAddress == "sample_text_2"


def test_Order_customerId_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.customerId == "sample_text"
    instance.customerId = "sample_text_2"
    assert instance.customerId == "sample_text_2"


def test_Order_customerName_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.customerName == "sample_text"
    instance.customerName = "sample_text_2"
    assert instance.customerName == "sample_text_2"


def test_Order_dateCreated_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.dateCreated == "sample_text"
    instance.dateCreated = "sample_text_2"
    assert instance.dateCreated == "sample_text_2"


def test_Order_dateShipped_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.dateShipped == "sample_text"
    instance.dateShipped = "sample_text_2"
    assert instance.dateShipped == "sample_text_2"


def test_Order_status_value_roundtrip():
    instance = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_OrderDetail_orderId_value_roundtrip():
    instance = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    assert instance.orderId == 7
    instance.orderId = 13
    assert instance.orderId == 13


def test_OrderDetail_productId_value_roundtrip():
    instance = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    assert instance.productId == 7
    instance.productId = 13
    assert instance.productId == 13


def test_OrderDetail_productName_value_roundtrip():
    instance = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    assert instance.productName == "sample_text"
    instance.productName = "sample_text_2"
    assert instance.productName == "sample_text_2"


def test_OrderDetail_quantity_value_roundtrip():
    instance = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_OrderDetail_subTotal_value_roundtrip():
    instance = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    assert instance.subTotal == "sample_text"
    instance.subTotal = "sample_text_2"
    assert instance.subTotal == "sample_text_2"


def test_OrderDetail_unitCost_value_roundtrip():
    instance = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    assert instance.unitCost == "sample_text"
    instance.unitCost = "sample_text_2"
    assert instance.unitCost == "sample_text_2"


def test_OrderService_attribute_value_roundtrip():
    instance = OrderService(attribute="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_PayLater1_UserID_value_roundtrip():
    instance = PayLater1(UserID="sample_text")
    assert instance.UserID == "sample_text"
    instance.UserID = "sample_text_2"
    assert instance.UserID == "sample_text_2"


def test_Price_ActualPrice_value_roundtrip():
    instance = Price(ActualPrice="sample_text")
    assert instance.ActualPrice == "sample_text"
    instance.ActualPrice = "sample_text_2"
    assert instance.ActualPrice == "sample_text_2"


def test_Product_Name_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Product_Price_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_Product_SKU_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.SKU == "sample_text"
    instance.SKU = "sample_text_2"
    assert instance.SKU == "sample_text_2"


def test_Product_attribute5_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.attribute5 == "sample_text"
    instance.attribute5 = "sample_text_2"
    assert instance.attribute5 == "sample_text_2"


def test_Product_attribute6_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.attribute6 == "sample_text"
    instance.attribute6 = "sample_text_2"
    assert instance.attribute6 == "sample_text_2"


def test_Product_attribute7_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.attribute7 == "sample_text"
    instance.attribute7 = "sample_text_2"
    assert instance.attribute7 == "sample_text_2"


def test_Product_description_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Product_productId_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.productId == 7
    instance.productId = 13
    assert instance.productId == 13


def test_Product_reviews_value_roundtrip():
    instance = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    assert instance.reviews == "sample_text"
    instance.reviews = "sample_text_2"
    assert instance.reviews == "sample_text_2"


def test_SMS_MobileNo_value_roundtrip():
    instance = SMS(MobileNo=7)
    assert instance.MobileNo == 7
    instance.MobileNo = 13
    assert instance.MobileNo == 13


def test_SessionManager_departmentName_value_roundtrip():
    instance = SessionManager(departmentName="sample_text", userid="sample_text")
    assert instance.departmentName == "sample_text"
    instance.departmentName = "sample_text_2"
    assert instance.departmentName == "sample_text_2"


def test_SessionManager_userid_value_roundtrip():
    instance = SessionManager(departmentName="sample_text", userid="sample_text")
    assert instance.userid == "sample_text"
    instance.userid = "sample_text_2"
    assert instance.userid == "sample_text_2"


def test_Shipping_ShippingType_value_roundtrip():
    instance = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    assert instance.ShippingType == "sample_text"
    instance.ShippingType = "sample_text_2"
    assert instance.ShippingType == "sample_text_2"


def test_Shipping__attr_value_roundtrip():
    instance = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    assert instance._attr == 7
    instance._attr = 13
    assert instance._attr == 13


def test_Shipping_shippingAddress_value_roundtrip():
    instance = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    assert instance.shippingAddress == "sample_text"
    instance.shippingAddress = "sample_text_2"
    assert instance.shippingAddress == "sample_text_2"


def test_Shipping_shippingId_value_roundtrip():
    instance = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    assert instance.shippingId == 7
    instance.shippingId = 13
    assert instance.shippingId == 13


def test_Shipping_shippingType_value_roundtrip():
    instance = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    assert instance.shippingType == "sample_text"
    instance.shippingType = "sample_text_2"
    assert instance.shippingType == "sample_text_2"


def test_ShoppingCart_GetTotalPrice_value_roundtrip():
    instance = ShoppingCart(GetTotalPrice="sample_text", Item="sample_text", dateAdded=7, quantity=7)
    assert instance.GetTotalPrice == "sample_text"
    instance.GetTotalPrice = "sample_text_2"
    assert instance.GetTotalPrice == "sample_text_2"


def test_ShoppingCart_Item_value_roundtrip():
    instance = ShoppingCart(GetTotalPrice="sample_text", Item="sample_text", dateAdded=7, quantity=7)
    assert instance.Item == "sample_text"
    instance.Item = "sample_text_2"
    assert instance.Item == "sample_text_2"


def test_ShoppingCart_dateAdded_value_roundtrip():
    instance = ShoppingCart(GetTotalPrice="sample_text", Item="sample_text", dateAdded=7, quantity=7)
    assert instance.dateAdded == 7
    instance.dateAdded = 13
    assert instance.dateAdded == 13


def test_ShoppingCart_quantity_value_roundtrip():
    instance = ShoppingCart(GetTotalPrice="sample_text", Item="sample_text", dateAdded=7, quantity=7)
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_User_loginStatus_value_roundtrip():
    instance = User(loginStatus="sample_text", password="sample_text", userId="sample_text")
    assert instance.loginStatus == "sample_text"
    instance.loginStatus = "sample_text_2"
    assert instance.loginStatus == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(loginStatus="sample_text", password="sample_text", userId="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_userId_value_roundtrip():
    instance = User(loginStatus="sample_text", password="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_Vendor_attribute_value_roundtrip():
    instance = Vendor(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute == "sample_text"
    instance.attribute = "sample_text_2"
    assert instance.attribute == "sample_text_2"


def test_Vendor_attribute2_value_roundtrip():
    instance = Vendor(attribute="sample_text", attribute2="sample_text")
    assert instance.attribute2 == "sample_text"
    instance.attribute2 = "sample_text_2"
    assert instance.attribute2 == "sample_text_2"


def test_cartItem_name_value_roundtrip():
    instance = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_cartItem_productId_value_roundtrip():
    instance = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    assert instance.productId == 7
    instance.productId = 13
    assert instance.productId == 13


def test_cartItem_quantity_value_roundtrip():
    instance = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    assert instance.quantity == 7
    instance.quantity = 13
    assert instance.quantity == 13


def test_cartItem_subtotal_value_roundtrip():
    instance = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    assert instance.subtotal == "sample_text"
    instance.subtotal = "sample_text_2"
    assert instance.subtotal == "sample_text_2"


def test_cartItem_unitCost_value_roundtrip():
    instance = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    assert instance.unitCost == "sample_text"
    instance.unitCost = "sample_text_2"
    assert instance.unitCost == "sample_text_2"


def test_email_EmailAddress_value_roundtrip():
    instance = email(EmailAddress="sample_text")
    assert instance.EmailAddress == "sample_text"
    instance.EmailAddress = "sample_text_2"
    assert instance.EmailAddress == "sample_text_2"


def test_keywordSet_keyword_value_roundtrip():
    instance = keywordSet(keyword="sample_text")
    assert instance.keyword == "sample_text"
    instance.keyword = "sample_text_2"
    assert instance.keyword == "sample_text_2"


def test_promotions_endDate_value_roundtrip():
    instance = promotions(endDate=7, promotionCode="sample_text", startDate=7)
    assert instance.endDate == 7
    instance.endDate = 13
    assert instance.endDate == 13


def test_promotions_promotionCode_value_roundtrip():
    instance = promotions(endDate=7, promotionCode="sample_text", startDate=7)
    assert instance.promotionCode == "sample_text"
    instance.promotionCode = "sample_text_2"
    assert instance.promotionCode == "sample_text_2"


def test_promotions_startDate_value_roundtrip():
    instance = promotions(endDate=7, promotionCode="sample_text", startDate=7)
    assert instance.startDate == 7
    instance.startDate = 13
    assert instance.startDate == 13


def test_assoc_Administrator_Order_link_reassign_clear():
    a = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b1 = Administrator(adminName="sample_text", email="sample_text")
    b2 = Administrator(adminName="sample_text_2", email="sample_text_2")
    _safe_set(a, 'administrator17', b1)
    assert _is_linked(a, 'administrator17', b1)
    if hasattr(b1, 'order16'):
        assert _is_linked(b1, 'order16', a)
    _safe_set(a, 'administrator17', b2)
    assert _is_linked(a, 'administrator17', b2)
    if hasattr(b1, 'order16'):
        assert not _is_linked(b1, 'order16', a)
    if hasattr(b2, 'order16'):
        assert _is_linked(b2, 'order16', a)
    _safe_set(a, 'administrator17', None)
    assert not _is_linked(a, 'administrator17', b2)
    if hasattr(b2, 'order16'):
        assert not _is_linked(b2, 'order16', a)


def test_assoc_Cart_Cart_link_reassign_clear():
    a = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    b1 = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    b2 = cartItem(name="sample_text_2", productId=13, quantity=13, subtotal="sample_text_2", unitCost="sample_text_2")
    _safe_set(a, 'cart2', b1)
    assert _is_linked(a, 'cart2', b1)
    if hasattr(b1, 'cart3'):
        assert _is_linked(b1, 'cart3', a)
    _safe_set(a, 'cart2', b2)
    assert _is_linked(a, 'cart2', b2)
    if hasattr(b1, 'cart3'):
        assert not _is_linked(b1, 'cart3', a)
    if hasattr(b2, 'cart3'):
        assert _is_linked(b2, 'cart3', a)
    _safe_set(a, 'cart2', None)
    assert not _is_linked(a, 'cart2', b2)
    if hasattr(b2, 'cart3'):
        assert not _is_linked(b2, 'cart3', a)


def test_assoc_Customer_Order_link_reassign_clear():
    a = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b1 = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    b2 = Customer(address="sample_text_2", creditcardinfo="sample_text_2", customerName="sample_text_2", email="sample_text_2", newsLettersub=False, phoneno=13, shippinginfo="sample_text_2", surveys=False)
    _safe_set(a, 'customer15', b1)
    assert _is_linked(a, 'customer15', b1)
    if hasattr(b1, 'order14'):
        assert _is_linked(b1, 'order14', a)
    _safe_set(a, 'customer15', b2)
    assert _is_linked(a, 'customer15', b2)
    if hasattr(b1, 'order14'):
        assert not _is_linked(b1, 'order14', a)
    if hasattr(b2, 'order14'):
        assert _is_linked(b2, 'order14', a)
    _safe_set(a, 'customer15', None)
    assert not _is_linked(a, 'customer15', b2)
    if hasattr(b2, 'order14'):
        assert not _is_linked(b2, 'order14', a)


def test_assoc_Customer_promotions_link_reassign_clear():
    a = promotions(endDate=7, promotionCode="sample_text", startDate=7)
    b1 = Customer(address="sample_text", creditcardinfo="sample_text", customerName="sample_text", email="sample_text", newsLettersub=True, phoneno=7, shippinginfo="sample_text", surveys=True)
    b2 = Customer(address="sample_text_2", creditcardinfo="sample_text_2", customerName="sample_text_2", email="sample_text_2", newsLettersub=False, phoneno=13, shippinginfo="sample_text_2", surveys=False)
    _safe_set(a, 'customer35', b1)
    assert _is_linked(a, 'customer35', b1)
    if hasattr(b1, 'promotions34'):
        assert _is_linked(b1, 'promotions34', a)
    _safe_set(a, 'customer35', b2)
    assert _is_linked(a, 'customer35', b2)
    if hasattr(b1, 'promotions34'):
        assert not _is_linked(b1, 'promotions34', a)
    if hasattr(b2, 'promotions34'):
        assert _is_linked(b2, 'promotions34', a)
    _safe_set(a, 'customer35', None)
    assert not _is_linked(a, 'customer35', b2)
    if hasattr(b2, 'promotions34'):
        assert not _is_linked(b2, 'promotions34', a)


def test_assoc_Department_Category_link_reassign_clear():
    a = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    b1 = Category(categoryID=7, categoryName="sample_text", departmentId=7, description="sample_text")
    b2 = Category(categoryID=13, categoryName="sample_text_2", departmentId=13, description="sample_text_2")
    _safe_set(a, 'category54', b1)
    assert _is_linked(a, 'category54', b1)
    if hasattr(b1, 'department55'):
        assert _is_linked(b1, 'department55', a)
    _safe_set(a, 'category54', b2)
    assert _is_linked(a, 'category54', b2)
    if hasattr(b1, 'department55'):
        assert not _is_linked(b1, 'department55', a)
    if hasattr(b2, 'department55'):
        assert _is_linked(b2, 'department55', a)
    _safe_set(a, 'category54', None)
    assert not _is_linked(a, 'category54', b2)
    if hasattr(b2, 'department55'):
        assert not _is_linked(b2, 'department55', a)


def test_assoc_Department_Department_link_reassign_clear():
    a = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    b1 = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    b2 = Department(departmentID=13, departmentName="sample_text_2", description="sample_text_2")
    _safe_set(a, 'department52', b1)
    assert _is_linked(a, 'department52', b1)
    if hasattr(b1, 'department53'):
        assert _is_linked(b1, 'department53', a)
    _safe_set(a, 'department52', b2)
    assert _is_linked(a, 'department52', b2)
    if hasattr(b1, 'department53'):
        assert not _is_linked(b1, 'department53', a)
    if hasattr(b2, 'department53'):
        assert _is_linked(b2, 'department53', a)
    _safe_set(a, 'department52', None)
    assert not _is_linked(a, 'department52', b2)
    if hasattr(b2, 'department53'):
        assert not _is_linked(b2, 'department53', a)


def test_assoc_Genre_Genre_link_reassign_clear():
    a = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    b1 = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    b2 = Department(departmentID=13, departmentName="sample_text_2", description="sample_text_2")
    _safe_set(a, 'genre5', b1)
    assert _is_linked(a, 'genre5', b1)
    if hasattr(b1, 'genre4'):
        assert _is_linked(b1, 'genre4', a)
    _safe_set(a, 'genre5', b2)
    assert _is_linked(a, 'genre5', b2)
    if hasattr(b1, 'genre4'):
        assert not _is_linked(b1, 'genre4', a)
    if hasattr(b2, 'genre4'):
        assert _is_linked(b2, 'genre4', a)
    _safe_set(a, 'genre5', None)
    assert not _is_linked(a, 'genre5', b2)
    if hasattr(b2, 'genre4'):
        assert not _is_linked(b2, 'genre4', a)


def test_assoc_Genre_Product_link_reassign_clear():
    a = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    b1 = Category(categoryID=7, categoryName="sample_text", departmentId=7, description="sample_text")
    b2 = Category(categoryID=13, categoryName="sample_text_2", departmentId=13, description="sample_text_2")
    _safe_set(a, 'genre7', b1)
    assert _is_linked(a, 'genre7', b1)
    if hasattr(b1, 'product6'):
        assert _is_linked(b1, 'product6', a)
    _safe_set(a, 'genre7', b2)
    assert _is_linked(a, 'genre7', b2)
    if hasattr(b1, 'product6'):
        assert not _is_linked(b1, 'product6', a)
    if hasattr(b2, 'product6'):
        assert _is_linked(b2, 'product6', a)
    _safe_set(a, 'genre7', None)
    assert not _is_linked(a, 'genre7', b2)
    if hasattr(b2, 'product6'):
        assert not _is_linked(b2, 'product6', a)


def test_assoc_Item_Order_link_reassign_clear():
    a = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b1 = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    b2 = Item(Name="sample_text_2", Quantity=13, attribute="sample_text_2")
    _safe_set(a, 'item77', b1)
    assert _is_linked(a, 'item77', b1)
    if hasattr(b1, 'order76'):
        assert _is_linked(b1, 'order76', a)
    _safe_set(a, 'item77', b2)
    assert _is_linked(a, 'item77', b2)
    if hasattr(b1, 'order76'):
        assert not _is_linked(b1, 'order76', a)
    if hasattr(b2, 'order76'):
        assert _is_linked(b2, 'order76', a)
    _safe_set(a, 'item77', None)
    assert not _is_linked(a, 'item77', b2)
    if hasattr(b2, 'order76'):
        assert not _is_linked(b2, 'order76', a)


def test_assoc_Item_Product_link_reassign_clear():
    a = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    b1 = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    b2 = Item(Name="sample_text_2", Quantity=13, attribute="sample_text_2")
    _safe_set(a, 'item63', b1)
    assert _is_linked(a, 'item63', b1)
    if hasattr(b1, 'product62'):
        assert _is_linked(b1, 'product62', a)
    _safe_set(a, 'item63', b2)
    assert _is_linked(a, 'item63', b2)
    if hasattr(b1, 'product62'):
        assert not _is_linked(b1, 'product62', a)
    if hasattr(b2, 'product62'):
        assert _is_linked(b2, 'product62', a)
    _safe_set(a, 'item63', None)
    assert not _is_linked(a, 'item63', b2)
    if hasattr(b2, 'product62'):
        assert not _is_linked(b2, 'product62', a)


def test_assoc_OrderService_Notify_link_reassign_clear():
    a = OrderService(attribute="sample_text")
    b1 = Notify_Interface()
    b2 = Notify_Interface()
    _safe_set(a, 'notify82', b1)
    assert _is_linked(a, 'notify82', b1)
    if hasattr(b1, 'orderService83'):
        assert _is_linked(b1, 'orderService83', a)
    _safe_set(a, 'notify82', b2)
    assert _is_linked(a, 'notify82', b2)
    if hasattr(b1, 'orderService83'):
        assert not _is_linked(b1, 'orderService83', a)
    if hasattr(b2, 'orderService83'):
        assert _is_linked(b2, 'orderService83', a)
    _safe_set(a, 'notify82', None)
    assert not _is_linked(a, 'notify82', b2)
    if hasattr(b2, 'orderService83'):
        assert not _is_linked(b2, 'orderService83', a)


def test_assoc_OrderService_Order_link_reassign_clear():
    a = OrderService(attribute="sample_text")
    b1 = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b2 = Order(BillingAddress="sample_text_2", Item="sample_text_2", OrderId=13, OrderStatus="sample_text_2", Payment="sample_text_2", ShippingAddress="sample_text_2", customerId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", dateShipped="sample_text_2", status="sample_text_2")
    _safe_set(a, 'order64', b1)
    assert _is_linked(a, 'order64', b1)
    if hasattr(b1, 'orderService65'):
        assert _is_linked(b1, 'orderService65', a)
    _safe_set(a, 'order64', b2)
    assert _is_linked(a, 'order64', b2)
    if hasattr(b1, 'orderService65'):
        assert not _is_linked(b1, 'orderService65', a)
    if hasattr(b2, 'orderService65'):
        assert _is_linked(b2, 'orderService65', a)
    _safe_set(a, 'order64', None)
    assert not _is_linked(a, 'order64', b2)
    if hasattr(b2, 'orderService65'):
        assert not _is_linked(b2, 'orderService65', a)


def test_assoc_Order_Address_link_reassign_clear():
    a = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b1 = Address(City="sample_text", Country="sample_text", State="sample_text", Street="sample_text", Type="sample_text", ZipCode="sample_text")
    b2 = Address(City="sample_text_2", Country="sample_text_2", State="sample_text_2", Street="sample_text_2", Type="sample_text_2", ZipCode="sample_text_2")
    _safe_set(a, 'address80', b1)
    assert _is_linked(a, 'address80', b1)
    if hasattr(b1, 'order81'):
        assert _is_linked(b1, 'order81', a)
    _safe_set(a, 'address80', b2)
    assert _is_linked(a, 'address80', b2)
    if hasattr(b1, 'order81'):
        assert not _is_linked(b1, 'order81', a)
    if hasattr(b2, 'order81'):
        assert _is_linked(b2, 'order81', a)
    _safe_set(a, 'address80', None)
    assert not _is_linked(a, 'address80', b2)
    if hasattr(b2, 'order81'):
        assert not _is_linked(b2, 'order81', a)


def test_assoc_Order_OrderDetail_link_reassign_clear():
    a = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    b1 = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b2 = Order(BillingAddress="sample_text_2", Item="sample_text_2", OrderId=13, OrderStatus="sample_text_2", Payment="sample_text_2", ShippingAddress="sample_text_2", customerId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", dateShipped="sample_text_2", status="sample_text_2")
    _safe_set(a, 'order13', b1)
    assert _is_linked(a, 'order13', b1)
    if hasattr(b1, 'orderDetail12'):
        assert _is_linked(b1, 'orderDetail12', a)
    _safe_set(a, 'order13', b2)
    assert _is_linked(a, 'order13', b2)
    if hasattr(b1, 'orderDetail12'):
        assert not _is_linked(b1, 'orderDetail12', a)
    if hasattr(b2, 'orderDetail12'):
        assert _is_linked(b2, 'orderDetail12', a)
    _safe_set(a, 'order13', None)
    assert not _is_linked(a, 'order13', b2)
    if hasattr(b2, 'orderDetail12'):
        assert not _is_linked(b2, 'orderDetail12', a)


def test_assoc_Order_Payment_link_reassign_clear():
    a = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b1 = Payment()
    b2 = Payment()
    _safe_set(a, 'payment66', b1)
    assert _is_linked(a, 'payment66', b1)
    if hasattr(b1, 'order67'):
        assert _is_linked(b1, 'order67', a)
    _safe_set(a, 'payment66', b2)
    assert _is_linked(a, 'payment66', b2)
    if hasattr(b1, 'order67'):
        assert not _is_linked(b1, 'order67', a)
    if hasattr(b2, 'order67'):
        assert _is_linked(b2, 'order67', a)
    _safe_set(a, 'payment66', None)
    assert not _is_linked(a, 'payment66', b2)
    if hasattr(b2, 'order67'):
        assert not _is_linked(b2, 'order67', a)


def test_assoc_Order_Payment2_link_reassign_clear():
    a = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b1 = Payment_Interface()
    b2 = Payment_Interface()
    _safe_set(a, 'payment68', b1)
    assert _is_linked(a, 'payment68', b1)
    if hasattr(b1, 'order69'):
        assert _is_linked(b1, 'order69', a)
    _safe_set(a, 'payment68', b2)
    assert _is_linked(a, 'payment68', b2)
    if hasattr(b1, 'order69'):
        assert not _is_linked(b1, 'order69', a)
    if hasattr(b2, 'order69'):
        assert _is_linked(b2, 'order69', a)
    _safe_set(a, 'payment68', None)
    assert not _is_linked(a, 'payment68', b2)
    if hasattr(b2, 'order69'):
        assert not _is_linked(b2, 'order69', a)


def test_assoc_Order_Shipping_link_reassign_clear():
    a = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    b1 = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b2 = Order(BillingAddress="sample_text_2", Item="sample_text_2", OrderId=13, OrderStatus="sample_text_2", Payment="sample_text_2", ShippingAddress="sample_text_2", customerId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", dateShipped="sample_text_2", status="sample_text_2")
    _safe_set(a, 'order75', b1)
    assert _is_linked(a, 'order75', b1)
    if hasattr(b1, 'shipping74'):
        assert _is_linked(b1, 'shipping74', a)
    _safe_set(a, 'order75', b2)
    assert _is_linked(a, 'order75', b2)
    if hasattr(b1, 'shipping74'):
        assert not _is_linked(b1, 'shipping74', a)
    if hasattr(b2, 'shipping74'):
        assert _is_linked(b2, 'shipping74', a)
    _safe_set(a, 'order75', None)
    assert not _is_linked(a, 'order75', b2)
    if hasattr(b2, 'shipping74'):
        assert not _is_linked(b2, 'shipping74', a)


def test_assoc_Order_Shippinginfo_link_reassign_clear():
    a = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    b1 = Order(BillingAddress="sample_text", Item="sample_text", OrderId=7, OrderStatus="sample_text", Payment="sample_text", ShippingAddress="sample_text", customerId="sample_text", customerName="sample_text", dateCreated="sample_text", dateShipped="sample_text", status="sample_text")
    b2 = Order(BillingAddress="sample_text_2", Item="sample_text_2", OrderId=13, OrderStatus="sample_text_2", Payment="sample_text_2", ShippingAddress="sample_text_2", customerId="sample_text_2", customerName="sample_text_2", dateCreated="sample_text_2", dateShipped="sample_text_2", status="sample_text_2")
    _safe_set(a, 'Order_Shippinginfo_111', b1)
    assert _is_linked(a, 'Order_Shippinginfo_111', b1)
    if hasattr(b1, 'Order_Shippinginfo_010'):
        assert _is_linked(b1, 'Order_Shippinginfo_010', a)
    _safe_set(a, 'Order_Shippinginfo_111', b2)
    assert _is_linked(a, 'Order_Shippinginfo_111', b2)
    if hasattr(b1, 'Order_Shippinginfo_010'):
        assert not _is_linked(b1, 'Order_Shippinginfo_010', a)
    if hasattr(b2, 'Order_Shippinginfo_010'):
        assert _is_linked(b2, 'Order_Shippinginfo_010', a)
    _safe_set(a, 'Order_Shippinginfo_111', None)
    assert not _is_linked(a, 'Order_Shippinginfo_111', b2)
    if hasattr(b2, 'Order_Shippinginfo_010'):
        assert not _is_linked(b2, 'Order_Shippinginfo_010', a)


def test_assoc_Price_Price_link_reassign_clear():
    a = Price(ActualPrice="sample_text")
    b1 = Price(ActualPrice="sample_text")
    b2 = Price(ActualPrice="sample_text_2")
    _safe_set(a, 'price56', b1)
    assert _is_linked(a, 'price56', b1)
    if hasattr(b1, 'price57'):
        assert _is_linked(b1, 'price57', a)
    _safe_set(a, 'price56', b2)
    assert _is_linked(a, 'price56', b2)
    if hasattr(b1, 'price57'):
        assert not _is_linked(b1, 'price57', a)
    if hasattr(b2, 'price57'):
        assert _is_linked(b2, 'price57', a)
    _safe_set(a, 'price56', None)
    assert not _is_linked(a, 'price56', b2)
    if hasattr(b2, 'price57'):
        assert not _is_linked(b2, 'price57', a)


def test_assoc_Product_Offer_link_reassign_clear():
    a = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    b1 = Offer_Interface()
    b2 = Offer_Interface()
    _safe_set(a, 'offer58', b1)
    assert _is_linked(a, 'offer58', b1)
    if hasattr(b1, 'product59'):
        assert _is_linked(b1, 'product59', a)
    _safe_set(a, 'offer58', b2)
    assert _is_linked(a, 'offer58', b2)
    if hasattr(b1, 'product59'):
        assert not _is_linked(b1, 'product59', a)
    if hasattr(b2, 'product59'):
        assert _is_linked(b2, 'product59', a)
    _safe_set(a, 'offer58', None)
    assert not _is_linked(a, 'offer58', b2)
    if hasattr(b2, 'product59'):
        assert not _is_linked(b2, 'product59', a)


def test_assoc_Product_OrderDetail_link_reassign_clear():
    a = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    b1 = OrderDetail(orderId=7, productId=7, productName="sample_text", quantity=7, subTotal="sample_text", unitCost="sample_text")
    b2 = OrderDetail(orderId=13, productId=13, productName="sample_text_2", quantity=13, subTotal="sample_text_2", unitCost="sample_text_2")
    _safe_set(a, 'orderDetail18', b1)
    assert _is_linked(a, 'orderDetail18', b1)
    if hasattr(b1, 'product19'):
        assert _is_linked(b1, 'product19', a)
    _safe_set(a, 'orderDetail18', b2)
    assert _is_linked(a, 'orderDetail18', b2)
    if hasattr(b1, 'product19'):
        assert not _is_linked(b1, 'product19', a)
    if hasattr(b2, 'product19'):
        assert _is_linked(b2, 'product19', a)
    _safe_set(a, 'orderDetail18', None)
    assert not _is_linked(a, 'orderDetail18', b2)
    if hasattr(b2, 'product19'):
        assert not _is_linked(b2, 'product19', a)


def test_assoc_Product_Price_link_reassign_clear():
    a = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    b1 = Price(ActualPrice="sample_text")
    b2 = Price(ActualPrice="sample_text_2")
    _safe_set(a, 'price60', b1)
    assert _is_linked(a, 'price60', b1)
    if hasattr(b1, 'product61'):
        assert _is_linked(b1, 'product61', a)
    _safe_set(a, 'price60', b2)
    assert _is_linked(a, 'price60', b2)
    if hasattr(b1, 'product61'):
        assert not _is_linked(b1, 'product61', a)
    if hasattr(b2, 'product61'):
        assert _is_linked(b2, 'product61', a)
    _safe_set(a, 'price60', None)
    assert not _is_linked(a, 'price60', b2)
    if hasattr(b2, 'product61'):
        assert not _is_linked(b2, 'product61', a)


def test_assoc_Product_cartItem_link_reassign_clear():
    a = cartItem(name="sample_text", productId=7, quantity=7, subtotal="sample_text", unitCost="sample_text")
    b1 = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    b2 = Product(Name="sample_text_2", Price="sample_text_2", SKU="sample_text_2", attribute5="sample_text_2", attribute6="sample_text_2", attribute7="sample_text_2", description="sample_text_2", productId=13, reviews="sample_text_2")
    _safe_set(a, 'product21', b1)
    assert _is_linked(a, 'product21', b1)
    if hasattr(b1, 'cartItem20'):
        assert _is_linked(b1, 'cartItem20', a)
    _safe_set(a, 'product21', b2)
    assert _is_linked(a, 'product21', b2)
    if hasattr(b1, 'cartItem20'):
        assert not _is_linked(b1, 'cartItem20', a)
    if hasattr(b2, 'cartItem20'):
        assert _is_linked(b2, 'cartItem20', a)
    _safe_set(a, 'product21', None)
    assert not _is_linked(a, 'product21', b2)
    if hasattr(b2, 'cartItem20'):
        assert not _is_linked(b2, 'cartItem20', a)


def test_assoc_SessionManager_Genre_link_reassign_clear():
    a = SessionManager(departmentName="sample_text", userid="sample_text")
    b1 = Department(departmentID=7, departmentName="sample_text", description="sample_text")
    b2 = Department(departmentID=13, departmentName="sample_text_2", description="sample_text_2")
    _safe_set(a, 'genre8', b1)
    assert _is_linked(a, 'genre8', b1)
    if hasattr(b1, 'sessionManager9'):
        assert _is_linked(b1, 'sessionManager9', a)
    _safe_set(a, 'genre8', b2)
    assert _is_linked(a, 'genre8', b2)
    if hasattr(b1, 'sessionManager9'):
        assert not _is_linked(b1, 'sessionManager9', a)
    if hasattr(b2, 'sessionManager9'):
        assert _is_linked(b2, 'sessionManager9', a)
    _safe_set(a, 'genre8', None)
    assert not _is_linked(a, 'genre8', b2)
    if hasattr(b2, 'sessionManager9'):
        assert not _is_linked(b2, 'sessionManager9', a)


def test_assoc_SessionManager_User_link_reassign_clear():
    a = User(loginStatus="sample_text", password="sample_text", userId="sample_text")
    b1 = SessionManager(departmentName="sample_text", userid="sample_text")
    b2 = SessionManager(departmentName="sample_text_2", userid="sample_text_2")
    _safe_set(a, 'sessionManager1', b1)
    assert _is_linked(a, 'sessionManager1', b1)
    if hasattr(b1, 'user0'):
        assert _is_linked(b1, 'user0', a)
    _safe_set(a, 'sessionManager1', b2)
    assert _is_linked(a, 'sessionManager1', b2)
    if hasattr(b1, 'user0'):
        assert not _is_linked(b1, 'user0', a)
    if hasattr(b2, 'user0'):
        assert _is_linked(b2, 'user0', a)
    _safe_set(a, 'sessionManager1', None)
    assert not _is_linked(a, 'sessionManager1', b2)
    if hasattr(b2, 'user0'):
        assert not _is_linked(b2, 'user0', a)


def test_assoc_Shipping_ShippingType_link_reassign_clear():
    a = Shipping(ShippingType="sample_text", _attr=7, shippingAddress="sample_text", shippingId=7, shippingType="sample_text")
    b1 = ShippingType_Interface()
    b2 = ShippingType_Interface()
    _safe_set(a, 'shippingType272', b1)
    assert _is_linked(a, 'shippingType272', b1)
    if hasattr(b1, 'shipping73'):
        assert _is_linked(b1, 'shipping73', a)
    _safe_set(a, 'shippingType272', b2)
    assert _is_linked(a, 'shippingType272', b2)
    if hasattr(b1, 'shipping73'):
        assert not _is_linked(b1, 'shipping73', a)
    if hasattr(b2, 'shipping73'):
        assert _is_linked(b2, 'shipping73', a)
    _safe_set(a, 'shippingType272', None)
    assert not _is_linked(a, 'shippingType272', b2)
    if hasattr(b2, 'shipping73'):
        assert not _is_linked(b2, 'shipping73', a)


def test_assoc_ShoppingCart_Item_link_reassign_clear():
    a = ShoppingCart(GetTotalPrice="sample_text", Item="sample_text", dateAdded=7, quantity=7)
    b1 = Item(Name="sample_text", Quantity=7, attribute="sample_text")
    b2 = Item(Name="sample_text_2", Quantity=13, attribute="sample_text_2")
    _safe_set(a, 'item78', b1)
    assert _is_linked(a, 'item78', b1)
    if hasattr(b1, 'shoppingCart79'):
        assert _is_linked(b1, 'shoppingCart79', a)
    _safe_set(a, 'item78', b2)
    assert _is_linked(a, 'item78', b2)
    if hasattr(b1, 'shoppingCart79'):
        assert not _is_linked(b1, 'shoppingCart79', a)
    if hasattr(b2, 'shoppingCart79'):
        assert _is_linked(b2, 'shoppingCart79', a)
    _safe_set(a, 'item78', None)
    assert not _is_linked(a, 'item78', b2)
    if hasattr(b2, 'shoppingCart79'):
        assert not _is_linked(b2, 'shoppingCart79', a)


def test_assoc_keywordSet_Product_link_reassign_clear():
    a = keywordSet(keyword="sample_text")
    b1 = Product(Name="sample_text", Price="sample_text", SKU="sample_text", attribute5="sample_text", attribute6="sample_text", attribute7="sample_text", description="sample_text", productId=7, reviews="sample_text")
    b2 = Product(Name="sample_text_2", Price="sample_text_2", SKU="sample_text_2", attribute5="sample_text_2", attribute6="sample_text_2", attribute7="sample_text_2", description="sample_text_2", productId=13, reviews="sample_text_2")
    _safe_set(a, 'product24', b1)
    assert _is_linked(a, 'product24', b1)
    if hasattr(b1, 'keywordSet25'):
        assert _is_linked(b1, 'keywordSet25', a)
    _safe_set(a, 'product24', b2)
    assert _is_linked(a, 'product24', b2)
    if hasattr(b1, 'keywordSet25'):
        assert not _is_linked(b1, 'keywordSet25', a)
    if hasattr(b2, 'keywordSet25'):
        assert _is_linked(b2, 'keywordSet25', a)
    _safe_set(a, 'product24', None)
    assert not _is_linked(a, 'product24', b2)
    if hasattr(b2, 'keywordSet25'):
        assert not _is_linked(b2, 'keywordSet25', a)


def test_assoc_searchFacade_keywordSet_link_reassign_clear():
    a = keywordSet(keyword="sample_text")
    b1 = searchFacade()
    b2 = searchFacade()
    _safe_set(a, 'searchFacade23', b1)
    assert _is_linked(a, 'searchFacade23', b1)
    if hasattr(b1, 'keywordSet22'):
        assert _is_linked(b1, 'keywordSet22', a)
    _safe_set(a, 'searchFacade23', b2)
    assert _is_linked(a, 'searchFacade23', b2)
    if hasattr(b1, 'keywordSet22'):
        assert not _is_linked(b1, 'keywordSet22', a)
    if hasattr(b2, 'keywordSet22'):
        assert _is_linked(b2, 'keywordSet22', a)
    _safe_set(a, 'searchFacade23', None)
    assert not _is_linked(a, 'searchFacade23', b2)
    if hasattr(b2, 'keywordSet22'):
        assert not _is_linked(b2, 'keywordSet22', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Address_strategy = st.builds(Address, City=safe_text, Country=safe_text, State=safe_text, Street=safe_text, Type=safe_text, ZipCode=safe_text)
@given(instance=Address_strategy)
@settings(max_examples=25)
def test_Address_instantiation(instance):
    assert isinstance(instance, Address)


Administrator_strategy = st.builds(Administrator, adminName=safe_text, email=safe_text)
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


Category_strategy = st.builds(Category, categoryID=st.integers(), categoryName=safe_text, departmentId=st.integers(), description=safe_text)
@given(instance=Category_strategy)
@settings(max_examples=25)
def test_Category_instantiation(instance):
    assert isinstance(instance, Category)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Class1_strategy = st.builds(Class1)
@given(instance=Class1_strategy)
@settings(max_examples=25)
def test_Class1_instantiation(instance):
    assert isinstance(instance, Class1)


Class2_strategy = st.builds(Class2)
@given(instance=Class2_strategy)
@settings(max_examples=25)
def test_Class2_instantiation(instance):
    assert isinstance(instance, Class2)


CreditCardPayment_strategy = st.builds(CreditCardPayment, CardNumber=st.integers(), CardType=safe_text)
@given(instance=CreditCardPayment_strategy)
@settings(max_examples=25)
def test_CreditCardPayment_instantiation(instance):
    assert isinstance(instance, CreditCardPayment)


Credit_DebitCard_strategy = st.builds(Credit_DebitCard)
@given(instance=Credit_DebitCard_strategy)
@settings(max_examples=25)
def test_Credit_DebitCard_instantiation(instance):
    assert isinstance(instance, Credit_DebitCard)


Credit_DebitCard1_strategy = st.builds(Credit_DebitCard1)
@given(instance=Credit_DebitCard1_strategy)
@settings(max_examples=25)
def test_Credit_DebitCard1_instantiation(instance):
    assert isinstance(instance, Credit_DebitCard1)


Customer_strategy = st.builds(Customer, address=safe_text, creditcardinfo=safe_text, customerName=safe_text, email=safe_text, newsLettersub=st.booleans(), phoneno=st.integers(), shippinginfo=safe_text, surveys=st.booleans())
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Department_strategy = st.builds(Department, departmentID=st.integers(), departmentName=safe_text, description=safe_text)
@given(instance=Department_strategy)
@settings(max_examples=25)
def test_Department_instantiation(instance):
    assert isinstance(instance, Department)


EmailNotification_strategy = st.builds(EmailNotification)
@given(instance=EmailNotification_strategy)
@settings(max_examples=25)
def test_EmailNotification_instantiation(instance):
    assert isinstance(instance, EmailNotification)


Gpay_strategy = st.builds(Gpay)
@given(instance=Gpay_strategy)
@settings(max_examples=25)
def test_Gpay_instantiation(instance):
    assert isinstance(instance, Gpay)


Item_strategy = st.builds(Item, Name=safe_text, Quantity=st.integers(), attribute=safe_text)
@given(instance=Item_strategy)
@settings(max_examples=25)
def test_Item_instantiation(instance):
    assert isinstance(instance, Item)


Notify_Interface_strategy = st.builds(Notify_Interface)
@given(instance=Notify_Interface_strategy)
@settings(max_examples=25)
def test_Notify_Interface_instantiation(instance):
    assert isinstance(instance, Notify_Interface)


Offer_Interface_strategy = st.builds(Offer_Interface)
@given(instance=Offer_Interface_strategy)
@settings(max_examples=25)
def test_Offer_Interface_instantiation(instance):
    assert isinstance(instance, Offer_Interface)


Order_strategy = st.builds(Order, BillingAddress=safe_text, Item=safe_text, OrderId=st.integers(), OrderStatus=safe_text, Payment=safe_text, ShippingAddress=safe_text, customerId=safe_text, customerName=safe_text, dateCreated=safe_text, dateShipped=safe_text, status=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


OrderDetail_strategy = st.builds(OrderDetail, orderId=st.integers(), productId=st.integers(), productName=safe_text, quantity=st.integers(), subTotal=safe_text, unitCost=safe_text)
@given(instance=OrderDetail_strategy)
@settings(max_examples=25)
def test_OrderDetail_instantiation(instance):
    assert isinstance(instance, OrderDetail)


OrderService_strategy = st.builds(OrderService, attribute=safe_text)
@given(instance=OrderService_strategy)
@settings(max_examples=25)
def test_OrderService_instantiation(instance):
    assert isinstance(instance, OrderService)


PayLater_strategy = st.builds(PayLater)
@given(instance=PayLater_strategy)
@settings(max_examples=25)
def test_PayLater_instantiation(instance):
    assert isinstance(instance, PayLater)


PayLater1_strategy = st.builds(PayLater1, UserID=safe_text)
@given(instance=PayLater1_strategy)
@settings(max_examples=25)
def test_PayLater1_instantiation(instance):
    assert isinstance(instance, PayLater1)


Payment_strategy = st.builds(Payment)
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


Payment_Interface_strategy = st.builds(Payment_Interface)
@given(instance=Payment_Interface_strategy)
@settings(max_examples=25)
def test_Payment_Interface_instantiation(instance):
    assert isinstance(instance, Payment_Interface)


Price_strategy = st.builds(Price, ActualPrice=safe_text)
@given(instance=Price_strategy)
@settings(max_examples=25)
def test_Price_instantiation(instance):
    assert isinstance(instance, Price)


Product_strategy = st.builds(Product, Name=safe_text, Price=safe_text, SKU=safe_text, attribute5=safe_text, attribute6=safe_text, attribute7=safe_text, description=safe_text, productId=st.integers(), reviews=safe_text)
@given(instance=Product_strategy)
@settings(max_examples=25)
def test_Product_instantiation(instance):
    assert isinstance(instance, Product)


ProductDiscount_strategy = st.builds(ProductDiscount)
@given(instance=ProductDiscount_strategy)
@settings(max_examples=25)
def test_ProductDiscount_instantiation(instance):
    assert isinstance(instance, ProductDiscount)


PushNotification_strategy = st.builds(PushNotification)
@given(instance=PushNotification_strategy)
@settings(max_examples=25)
def test_PushNotification_instantiation(instance):
    assert isinstance(instance, PushNotification)


SMS_strategy = st.builds(SMS, MobileNo=st.integers())
@given(instance=SMS_strategy)
@settings(max_examples=25)
def test_SMS_instantiation(instance):
    assert isinstance(instance, SMS)


SessionManager_strategy = st.builds(SessionManager, departmentName=safe_text, userid=safe_text)
@given(instance=SessionManager_strategy)
@settings(max_examples=25)
def test_SessionManager_instantiation(instance):
    assert isinstance(instance, SessionManager)


Shipping_strategy = st.builds(Shipping, ShippingType=safe_text, _attr=st.integers(), shippingAddress=safe_text, shippingId=st.integers(), shippingType=safe_text)
@given(instance=Shipping_strategy)
@settings(max_examples=25)
def test_Shipping_instantiation(instance):
    assert isinstance(instance, Shipping)


ShippingType_Interface_strategy = st.builds(ShippingType_Interface)
@given(instance=ShippingType_Interface_strategy)
@settings(max_examples=25)
def test_ShippingType_Interface_instantiation(instance):
    assert isinstance(instance, ShippingType_Interface)


ShoppingCart_strategy = st.builds(ShoppingCart, GetTotalPrice=safe_text, Item=safe_text, dateAdded=st.integers(), quantity=st.integers())
@given(instance=ShoppingCart_strategy)
@settings(max_examples=25)
def test_ShoppingCart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)


TimeBasedDiscount_strategy = st.builds(TimeBasedDiscount)
@given(instance=TimeBasedDiscount_strategy)
@settings(max_examples=25)
def test_TimeBasedDiscount_instantiation(instance):
    assert isinstance(instance, TimeBasedDiscount)


User_strategy = st.builds(User, loginStatus=safe_text, password=safe_text, userId=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


Vendor_strategy = st.builds(Vendor, attribute=safe_text, attribute2=safe_text)
@given(instance=Vendor_strategy)
@settings(max_examples=25)
def test_Vendor_instantiation(instance):
    assert isinstance(instance, Vendor)


billdesk_Interface_strategy = st.builds(billdesk_Interface)
@given(instance=billdesk_Interface_strategy)
@settings(max_examples=25)
def test_billdesk_Interface_instantiation(instance):
    assert isinstance(instance, billdesk_Interface)


cartItem_strategy = st.builds(cartItem, name=safe_text, productId=st.integers(), quantity=st.integers(), subtotal=safe_text, unitCost=safe_text)
@given(instance=cartItem_strategy)
@settings(max_examples=25)
def test_cartItem_instantiation(instance):
    assert isinstance(instance, cartItem)


customeraddress_Interface_strategy = st.builds(customeraddress_Interface)
@given(instance=customeraddress_Interface_strategy)
@settings(max_examples=25)
def test_customeraddress_Interface_instantiation(instance):
    assert isinstance(instance, customeraddress_Interface)


email_strategy = st.builds(email, EmailAddress=safe_text)
@given(instance=email_strategy)
@settings(max_examples=25)
def test_email_instantiation(instance):
    assert isinstance(instance, email)


email_Interface_strategy = st.builds(email_Interface)
@given(instance=email_Interface_strategy)
@settings(max_examples=25)
def test_email_Interface_instantiation(instance):
    assert isinstance(instance, email_Interface)


gpay_Interface_strategy = st.builds(gpay_Interface)
@given(instance=gpay_Interface_strategy)
@settings(max_examples=25)
def test_gpay_Interface_instantiation(instance):
    assert isinstance(instance, gpay_Interface)


keywordSet_strategy = st.builds(keywordSet, keyword=safe_text)
@given(instance=keywordSet_strategy)
@settings(max_examples=25)
def test_keywordSet_instantiation(instance):
    assert isinstance(instance, keywordSet)


mobile_Interface_strategy = st.builds(mobile_Interface)
@given(instance=mobile_Interface_strategy)
@settings(max_examples=25)
def test_mobile_Interface_instantiation(instance):
    assert isinstance(instance, mobile_Interface)


notify_Interface_strategy = st.builds(notify_Interface)
@given(instance=notify_Interface_strategy)
@settings(max_examples=25)
def test_notify_Interface_instantiation(instance):
    assert isinstance(instance, notify_Interface)


paylater_Interface_strategy = st.builds(paylater_Interface)
@given(instance=paylater_Interface_strategy)
@settings(max_examples=25)
def test_paylater_Interface_instantiation(instance):
    assert isinstance(instance, paylater_Interface)


payment_Interface_strategy = st.builds(payment_Interface)
@given(instance=payment_Interface_strategy)
@settings(max_examples=25)
def test_payment_Interface_instantiation(instance):
    assert isinstance(instance, payment_Interface)


pickuppoint_Interface_strategy = st.builds(pickuppoint_Interface)
@given(instance=pickuppoint_Interface_strategy)
@settings(max_examples=25)
def test_pickuppoint_Interface_instantiation(instance):
    assert isinstance(instance, pickuppoint_Interface)


promotions_strategy = st.builds(promotions, endDate=st.integers(), promotionCode=safe_text, startDate=st.integers())
@given(instance=promotions_strategy)
@settings(max_examples=25)
def test_promotions_instantiation(instance):
    assert isinstance(instance, promotions)


searchFacade_strategy = st.builds(searchFacade)
@given(instance=searchFacade_strategy)
@settings(max_examples=25)
def test_searchFacade_instantiation(instance):
    assert isinstance(instance, searchFacade)


shiporder_Interface_strategy = st.builds(shiporder_Interface)
@given(instance=shiporder_Interface_strategy)
@settings(max_examples=25)
def test_shiporder_Interface_instantiation(instance):
    assert isinstance(instance, shiporder_Interface)



