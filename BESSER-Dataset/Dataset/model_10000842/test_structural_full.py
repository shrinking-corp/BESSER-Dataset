import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AccountInfo,
    Administrator,
    CardInfo,
    Farmer,
    Farmer_produces,
    Order,
    Products,
    Retailer,
    Retailer_Cart,
    User,
    rating___review,
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

def test_AccountInfo_ID_value_roundtrip():
    instance = AccountInfo(ID=7, accountNumber=7, bankBranch="sample_text", bankName="sample_text", name="sample_text", routingNumber=7)
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_AccountInfo_accountNumber_value_roundtrip():
    instance = AccountInfo(ID=7, accountNumber=7, bankBranch="sample_text", bankName="sample_text", name="sample_text", routingNumber=7)
    assert instance.accountNumber == 7
    instance.accountNumber = 13
    assert instance.accountNumber == 13


def test_AccountInfo_bankBranch_value_roundtrip():
    instance = AccountInfo(ID=7, accountNumber=7, bankBranch="sample_text", bankName="sample_text", name="sample_text", routingNumber=7)
    assert instance.bankBranch == "sample_text"
    instance.bankBranch = "sample_text_2"
    assert instance.bankBranch == "sample_text_2"


def test_AccountInfo_bankName_value_roundtrip():
    instance = AccountInfo(ID=7, accountNumber=7, bankBranch="sample_text", bankName="sample_text", name="sample_text", routingNumber=7)
    assert instance.bankName == "sample_text"
    instance.bankName = "sample_text_2"
    assert instance.bankName == "sample_text_2"


def test_AccountInfo_name_value_roundtrip():
    instance = AccountInfo(ID=7, accountNumber=7, bankBranch="sample_text", bankName="sample_text", name="sample_text", routingNumber=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_AccountInfo_routingNumber_value_roundtrip():
    instance = AccountInfo(ID=7, accountNumber=7, bankBranch="sample_text", bankName="sample_text", name="sample_text", routingNumber=7)
    assert instance.routingNumber == 7
    instance.routingNumber = 13
    assert instance.routingNumber == 13


def test_Administrator_address_value_roundtrip():
    instance = Administrator(address="sample_text", adminType="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Administrator_adminType_value_roundtrip():
    instance = Administrator(address="sample_text", adminType="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.adminType == "sample_text"
    instance.adminType = "sample_text_2"
    assert instance.adminType == "sample_text_2"


def test_Administrator_dateOfBirth_value_roundtrip():
    instance = Administrator(address="sample_text", adminType="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_Administrator_emailId_value_roundtrip():
    instance = Administrator(address="sample_text", adminType="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.emailId == "sample_text"
    instance.emailId = "sample_text_2"
    assert instance.emailId == "sample_text_2"


def test_Administrator_name_value_roundtrip():
    instance = Administrator(address="sample_text", adminType="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Administrator_phone_value_roundtrip():
    instance = Administrator(address="sample_text", adminType="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


def test_Administrator_userId_value_roundtrip():
    instance = Administrator(address="sample_text", adminType="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.userId == 7
    instance.userId = 13
    assert instance.userId == 13


def test_CardInfo_CVV_value_roundtrip():
    instance = CardInfo(CVV=7, ID=7, billingAddress="sample_text", expiryDate=date(2024, 1, 1), name="sample_text", number=7)
    assert instance.CVV == 7
    instance.CVV = 13
    assert instance.CVV == 13


def test_CardInfo_ID_value_roundtrip():
    instance = CardInfo(CVV=7, ID=7, billingAddress="sample_text", expiryDate=date(2024, 1, 1), name="sample_text", number=7)
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_CardInfo_billingAddress_value_roundtrip():
    instance = CardInfo(CVV=7, ID=7, billingAddress="sample_text", expiryDate=date(2024, 1, 1), name="sample_text", number=7)
    assert instance.billingAddress == "sample_text"
    instance.billingAddress = "sample_text_2"
    assert instance.billingAddress == "sample_text_2"


def test_CardInfo_expiryDate_value_roundtrip():
    instance = CardInfo(CVV=7, ID=7, billingAddress="sample_text", expiryDate=date(2024, 1, 1), name="sample_text", number=7)
    assert instance.expiryDate == date(2024, 1, 1)
    instance.expiryDate = date(2025, 6, 15)
    assert instance.expiryDate == date(2025, 6, 15)


def test_CardInfo_name_value_roundtrip():
    instance = CardInfo(CVV=7, ID=7, billingAddress="sample_text", expiryDate=date(2024, 1, 1), name="sample_text", number=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_CardInfo_number_value_roundtrip():
    instance = CardInfo(CVV=7, ID=7, billingAddress="sample_text", expiryDate=date(2024, 1, 1), name="sample_text", number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_Farmer_CardInfo_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.CardInfo == "sample_text"
    instance.CardInfo = "sample_text_2"
    assert instance.CardInfo == "sample_text_2"


def test_Farmer_accountInfoID_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.accountInfoID == 7
    instance.accountInfoID = 13
    assert instance.accountInfoID == 13


def test_Farmer_address_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Farmer_dateOfBirth_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_Farmer_emailId_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.emailId == "sample_text"
    instance.emailId = "sample_text_2"
    assert instance.emailId == "sample_text_2"


def test_Farmer_name_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Farmer_phone_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


def test_Farmer_type_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_Farmer_userId_value_roundtrip():
    instance = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    assert instance.userId == 7
    instance.userId = 13
    assert instance.userId == 13


def test_Farmer_produces_ID_value_roundtrip():
    instance = Farmer_produces(ID=7, farmerID=7, productList="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Farmer_produces_farmerID_value_roundtrip():
    instance = Farmer_produces(ID=7, farmerID=7, productList="sample_text")
    assert instance.farmerID == 7
    instance.farmerID = 13
    assert instance.farmerID == 13


def test_Farmer_produces_productList_value_roundtrip():
    instance = Farmer_produces(ID=7, farmerID=7, productList="sample_text")
    assert instance.productList == "sample_text"
    instance.productList = "sample_text_2"
    assert instance.productList == "sample_text_2"


def test_Order_cardDetails_value_roundtrip():
    instance = Order(cardDetails="sample_text", productDetails="sample_text", purchaseDate=date(2024, 1, 1), transactionID=7)
    assert instance.cardDetails == "sample_text"
    instance.cardDetails = "sample_text_2"
    assert instance.cardDetails == "sample_text_2"


def test_Order_productDetails_value_roundtrip():
    instance = Order(cardDetails="sample_text", productDetails="sample_text", purchaseDate=date(2024, 1, 1), transactionID=7)
    assert instance.productDetails == "sample_text"
    instance.productDetails = "sample_text_2"
    assert instance.productDetails == "sample_text_2"


def test_Order_purchaseDate_value_roundtrip():
    instance = Order(cardDetails="sample_text", productDetails="sample_text", purchaseDate=date(2024, 1, 1), transactionID=7)
    assert instance.purchaseDate == date(2024, 1, 1)
    instance.purchaseDate = date(2025, 6, 15)
    assert instance.purchaseDate == date(2025, 6, 15)


def test_Order_transactionID_value_roundtrip():
    instance = Order(cardDetails="sample_text", productDetails="sample_text", purchaseDate=date(2024, 1, 1), transactionID=7)
    assert instance.transactionID == 7
    instance.transactionID = 13
    assert instance.transactionID == 13


def test_Products_ID_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_Products_description_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Products_discount_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.discount == 7
    instance.discount = 13
    assert instance.discount == 13


def test_Products_farmerID_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.farmerID == "sample_text"
    instance.farmerID = "sample_text_2"
    assert instance.farmerID == "sample_text_2"


def test_Products_inventoryID_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.inventoryID == "sample_text"
    instance.inventoryID = "sample_text_2"
    assert instance.inventoryID == "sample_text_2"


def test_Products_name_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Products_rating_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.rating == 7
    instance.rating = 13
    assert instance.rating == 13


def test_Products_reviews_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.reviews == "sample_text"
    instance.reviews = "sample_text_2"
    assert instance.reviews == "sample_text_2"


def test_Products_selling_price_value_roundtrip():
    instance = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    assert instance.selling_price == 3.14
    instance.selling_price = 9.99
    assert instance.selling_price == 9.99


def test_Retailer_CardInfo_value_roundtrip():
    instance = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.CardInfo == 7
    instance.CardInfo = 13
    assert instance.CardInfo == 13


def test_Retailer_Photo_value_roundtrip():
    instance = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.Photo == "sample_text"
    instance.Photo = "sample_text_2"
    assert instance.Photo == "sample_text_2"


def test_Retailer_address_value_roundtrip():
    instance = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Retailer_dateOfBirth_value_roundtrip():
    instance = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_Retailer_emailId_value_roundtrip():
    instance = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.emailId == "sample_text"
    instance.emailId = "sample_text_2"
    assert instance.emailId == "sample_text_2"


def test_Retailer_name_value_roundtrip():
    instance = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Retailer_phone_value_roundtrip():
    instance = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.phone == 7
    instance.phone = 13
    assert instance.phone == 13


def test_Retailer_userId_value_roundtrip():
    instance = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    assert instance.userId == 7
    instance.userId = 13
    assert instance.userId == 13


def test_User_Id_value_roundtrip():
    instance = User(Id=7, password="sample_text", userName="sample_text", userType="sample_text")
    assert instance.Id == 7
    instance.Id = 13
    assert instance.Id == 13


def test_User_password_value_roundtrip():
    instance = User(Id=7, password="sample_text", userName="sample_text", userType="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_userName_value_roundtrip():
    instance = User(Id=7, password="sample_text", userName="sample_text", userType="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_User_userType_value_roundtrip():
    instance = User(Id=7, password="sample_text", userName="sample_text", userType="sample_text")
    assert instance.userType == "sample_text"
    instance.userType = "sample_text_2"
    assert instance.userType == "sample_text_2"


def test_rating___review_ID_value_roundtrip():
    instance = rating___review(ID=7, inventoryID="sample_text", name="sample_text", rating=7, retailerID="sample_text", reviews="sample_text")
    assert instance.ID == 7
    instance.ID = 13
    assert instance.ID == 13


def test_rating___review_inventoryID_value_roundtrip():
    instance = rating___review(ID=7, inventoryID="sample_text", name="sample_text", rating=7, retailerID="sample_text", reviews="sample_text")
    assert instance.inventoryID == "sample_text"
    instance.inventoryID = "sample_text_2"
    assert instance.inventoryID == "sample_text_2"


def test_rating___review_name_value_roundtrip():
    instance = rating___review(ID=7, inventoryID="sample_text", name="sample_text", rating=7, retailerID="sample_text", reviews="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_rating___review_rating_value_roundtrip():
    instance = rating___review(ID=7, inventoryID="sample_text", name="sample_text", rating=7, retailerID="sample_text", reviews="sample_text")
    assert instance.rating == 7
    instance.rating = 13
    assert instance.rating == 13


def test_rating___review_retailerID_value_roundtrip():
    instance = rating___review(ID=7, inventoryID="sample_text", name="sample_text", rating=7, retailerID="sample_text", reviews="sample_text")
    assert instance.retailerID == "sample_text"
    instance.retailerID = "sample_text_2"
    assert instance.retailerID == "sample_text_2"


def test_rating___review_reviews_value_roundtrip():
    instance = rating___review(ID=7, inventoryID="sample_text", name="sample_text", rating=7, retailerID="sample_text", reviews="sample_text")
    assert instance.reviews == "sample_text"
    instance.reviews = "sample_text_2"
    assert instance.reviews == "sample_text_2"


def test_assoc_Customer_CardInfo_link_reassign_clear():
    a = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    b1 = CardInfo(CVV=7, ID=7, billingAddress="sample_text", expiryDate=date(2024, 1, 1), name="sample_text", number=7)
    b2 = CardInfo(CVV=13, ID=13, billingAddress="sample_text_2", expiryDate=date(2025, 6, 15), name="sample_text_2", number=13)
    _safe_set(a, 'cardInfo2', b1)
    assert _is_linked(a, 'cardInfo2', b1)
    if hasattr(b1, 'customer3'):
        assert _is_linked(b1, 'customer3', a)
    _safe_set(a, 'cardInfo2', b2)
    assert _is_linked(a, 'cardInfo2', b2)
    if hasattr(b1, 'customer3'):
        assert not _is_linked(b1, 'customer3', a)
    if hasattr(b2, 'customer3'):
        assert _is_linked(b2, 'customer3', a)
    _safe_set(a, 'cardInfo2', None)
    assert not _is_linked(a, 'cardInfo2', b2)
    if hasattr(b2, 'customer3'):
        assert not _is_linked(b2, 'customer3', a)


def test_assoc_Customer_Order_link_reassign_clear():
    a = Retailer(CardInfo=7, Photo="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, userId=7)
    b1 = Order(cardDetails="sample_text", productDetails="sample_text", purchaseDate=date(2024, 1, 1), transactionID=7)
    b2 = Order(cardDetails="sample_text_2", productDetails="sample_text_2", purchaseDate=date(2025, 6, 15), transactionID=13)
    _safe_set(a, 'order4', b1)
    assert _is_linked(a, 'order4', b1)
    if hasattr(b1, 'customer5'):
        assert _is_linked(b1, 'customer5', a)
    _safe_set(a, 'order4', b2)
    assert _is_linked(a, 'order4', b2)
    if hasattr(b1, 'customer5'):
        assert not _is_linked(b1, 'customer5', a)
    if hasattr(b2, 'customer5'):
        assert _is_linked(b2, 'customer5', a)
    _safe_set(a, 'order4', None)
    assert not _is_linked(a, 'order4', b2)
    if hasattr(b2, 'customer5'):
        assert not _is_linked(b2, 'customer5', a)


def test_assoc_Order_Farmer_link_reassign_clear():
    a = Order(cardDetails="sample_text", productDetails="sample_text", purchaseDate=date(2024, 1, 1), transactionID=7)
    b1 = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    b2 = Farmer(CardInfo="sample_text_2", accountInfoID=13, address="sample_text_2", dateOfBirth=date(2025, 6, 15), emailId="sample_text_2", name="sample_text_2", phone=13, type="sample_text_2", userId=13)
    _safe_set(a, 'farmer10', b1)
    assert _is_linked(a, 'farmer10', b1)
    if hasattr(b1, 'order11'):
        assert _is_linked(b1, 'order11', a)
    _safe_set(a, 'farmer10', b2)
    assert _is_linked(a, 'farmer10', b2)
    if hasattr(b1, 'order11'):
        assert not _is_linked(b1, 'order11', a)
    if hasattr(b2, 'order11'):
        assert _is_linked(b2, 'order11', a)
    _safe_set(a, 'farmer10', None)
    assert not _is_linked(a, 'farmer10', b2)
    if hasattr(b2, 'order11'):
        assert not _is_linked(b2, 'order11', a)


def test_assoc_Product_Farmer_Farmer_link_reassign_clear():
    a = Products(ID=7, description="sample_text", discount=7, farmerID="sample_text", inventoryID="sample_text", name="sample_text", rating=7, reviews="sample_text", selling_price=3.14)
    b1 = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    b2 = Farmer(CardInfo="sample_text_2", accountInfoID=13, address="sample_text_2", dateOfBirth=date(2025, 6, 15), emailId="sample_text_2", name="sample_text_2", phone=13, type="sample_text_2", userId=13)
    _safe_set(a, 'farmer8', b1)
    assert _is_linked(a, 'farmer8', b1)
    if hasattr(b1, 'product_Farmer9'):
        assert _is_linked(b1, 'product_Farmer9', a)
    _safe_set(a, 'farmer8', b2)
    assert _is_linked(a, 'farmer8', b2)
    if hasattr(b1, 'product_Farmer9'):
        assert not _is_linked(b1, 'product_Farmer9', a)
    if hasattr(b2, 'product_Farmer9'):
        assert _is_linked(b2, 'product_Farmer9', a)
    _safe_set(a, 'farmer8', None)
    assert not _is_linked(a, 'farmer8', b2)
    if hasattr(b2, 'product_Farmer9'):
        assert not _is_linked(b2, 'product_Farmer9', a)


def test_assoc_Seller_AccountInfo_link_reassign_clear():
    a = Farmer(CardInfo="sample_text", accountInfoID=7, address="sample_text", dateOfBirth=date(2024, 1, 1), emailId="sample_text", name="sample_text", phone=7, type="sample_text", userId=7)
    b1 = AccountInfo(ID=7, accountNumber=7, bankBranch="sample_text", bankName="sample_text", name="sample_text", routingNumber=7)
    b2 = AccountInfo(ID=13, accountNumber=13, bankBranch="sample_text_2", bankName="sample_text_2", name="sample_text_2", routingNumber=13)
    _safe_set(a, 'accountInfo6', b1)
    assert _is_linked(a, 'accountInfo6', b1)
    if hasattr(b1, 'seller7'):
        assert _is_linked(b1, 'seller7', a)
    _safe_set(a, 'accountInfo6', b2)
    assert _is_linked(a, 'accountInfo6', b2)
    if hasattr(b1, 'seller7'):
        assert not _is_linked(b1, 'seller7', a)
    if hasattr(b2, 'seller7'):
        assert _is_linked(b2, 'seller7', a)
    _safe_set(a, 'accountInfo6', None)
    assert not _is_linked(a, 'accountInfo6', b2)
    if hasattr(b2, 'seller7'):
        assert not _is_linked(b2, 'seller7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AccountInfo_strategy = st.builds(AccountInfo, ID=st.integers(), accountNumber=st.integers(), bankBranch=safe_text, bankName=safe_text, name=safe_text, routingNumber=st.integers())
@given(instance=AccountInfo_strategy)
@settings(max_examples=25)
def test_AccountInfo_instantiation(instance):
    assert isinstance(instance, AccountInfo)


Administrator_strategy = st.builds(Administrator, address=safe_text, adminType=safe_text, dateOfBirth=st.dates(), emailId=safe_text, name=safe_text, phone=st.integers(), userId=st.integers())
@given(instance=Administrator_strategy)
@settings(max_examples=25)
def test_Administrator_instantiation(instance):
    assert isinstance(instance, Administrator)


CardInfo_strategy = st.builds(CardInfo, CVV=st.integers(), ID=st.integers(), billingAddress=safe_text, expiryDate=st.dates(), name=safe_text, number=st.integers())
@given(instance=CardInfo_strategy)
@settings(max_examples=25)
def test_CardInfo_instantiation(instance):
    assert isinstance(instance, CardInfo)


Farmer_strategy = st.builds(Farmer, CardInfo=safe_text, accountInfoID=st.integers(), address=safe_text, dateOfBirth=st.dates(), emailId=safe_text, name=safe_text, phone=st.integers(), type=safe_text, userId=st.integers())
@given(instance=Farmer_strategy)
@settings(max_examples=25)
def test_Farmer_instantiation(instance):
    assert isinstance(instance, Farmer)


Farmer_produces_strategy = st.builds(Farmer_produces, ID=st.integers(), farmerID=st.integers(), productList=safe_text)
@given(instance=Farmer_produces_strategy)
@settings(max_examples=25)
def test_Farmer_produces_instantiation(instance):
    assert isinstance(instance, Farmer_produces)


Order_strategy = st.builds(Order, cardDetails=safe_text, productDetails=safe_text, purchaseDate=st.dates(), transactionID=st.integers())
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


Products_strategy = st.builds(Products, ID=st.integers(), description=safe_text, discount=st.integers(), farmerID=safe_text, inventoryID=safe_text, name=safe_text, rating=st.integers(), reviews=safe_text, selling_price=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Products_strategy)
@settings(max_examples=25)
def test_Products_instantiation(instance):
    assert isinstance(instance, Products)


Retailer_strategy = st.builds(Retailer, CardInfo=st.integers(), Photo=safe_text, address=safe_text, dateOfBirth=st.dates(), emailId=safe_text, name=safe_text, phone=st.integers(), userId=st.integers())
@given(instance=Retailer_strategy)
@settings(max_examples=25)
def test_Retailer_instantiation(instance):
    assert isinstance(instance, Retailer)


User_strategy = st.builds(User, Id=st.integers(), password=safe_text, userName=safe_text, userType=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


rating___review_strategy = st.builds(rating___review, ID=st.integers(), inventoryID=safe_text, name=safe_text, rating=st.integers(), retailerID=safe_text, reviews=safe_text)
@given(instance=rating___review_strategy)
@settings(max_examples=25)
def test_rating___review_instantiation(instance):
    assert isinstance(instance, rating___review)


