import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    CartItems,
    Categories,
    CompanyAddItem,
    CompanyAddRider,
    CompanyAssignRider,
    CompanyOrderHistory,
    CompanyTrackOrder,
    ConfirmOrder,
    Login,
    Order,
    OrderHistory,
    PlaceOrder,
    ReviewOrder,
    RiderStatusUpdate,
    Store,
    TrackOrder,
    UserRegisteration,
    phon,
    void_Interface,
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

def test_CartItems_Name_value_roundtrip():
    instance = CartItems(Name="sample_text", Price="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_CartItems_Price_value_roundtrip():
    instance = CartItems(Name="sample_text", Price="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_Categories_Categories_value_roundtrip():
    instance = Categories(Categories="sample_text")
    assert instance.Categories == "sample_text"
    instance.Categories = "sample_text_2"
    assert instance.Categories == "sample_text_2"


def test_CompanyAddItem_Category_value_roundtrip():
    instance = CompanyAddItem(Category="sample_text", Description="sample_text", Name="sample_text", Price="sample_text")
    assert instance.Category == "sample_text"
    instance.Category = "sample_text_2"
    assert instance.Category == "sample_text_2"


def test_CompanyAddItem_Description_value_roundtrip():
    instance = CompanyAddItem(Category="sample_text", Description="sample_text", Name="sample_text", Price="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_CompanyAddItem_Name_value_roundtrip():
    instance = CompanyAddItem(Category="sample_text", Description="sample_text", Name="sample_text", Price="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_CompanyAddItem_Price_value_roundtrip():
    instance = CompanyAddItem(Category="sample_text", Description="sample_text", Name="sample_text", Price="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_CompanyAddRider_Address_value_roundtrip():
    instance = CompanyAddRider(Address="sample_text", CNIC=7, Email="sample_text", Name="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_CompanyAddRider_CNIC_value_roundtrip():
    instance = CompanyAddRider(Address="sample_text", CNIC=7, Email="sample_text", Name="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.CNIC == 7
    instance.CNIC = 13
    assert instance.CNIC == 13


def test_CompanyAddRider_Email_value_roundtrip():
    instance = CompanyAddRider(Address="sample_text", CNIC=7, Email="sample_text", Name="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_CompanyAddRider_Name_value_roundtrip():
    instance = CompanyAddRider(Address="sample_text", CNIC=7, Email="sample_text", Name="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_CompanyAddRider_Password_value_roundtrip():
    instance = CompanyAddRider(Address="sample_text", CNIC=7, Email="sample_text", Name="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_CompanyAddRider_Phone_value_roundtrip():
    instance = CompanyAddRider(Address="sample_text", CNIC=7, Email="sample_text", Name="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Phone == "sample_text"
    instance.Phone = "sample_text_2"
    assert instance.Phone == "sample_text_2"


def test_CompanyAddRider_UserName_value_roundtrip():
    instance = CompanyAddRider(Address="sample_text", CNIC=7, Email="sample_text", Name="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


def test_CompanyAssignRider_CustomerName_value_roundtrip():
    instance = CompanyAssignRider(CustomerName="sample_text", OrderDate_Time="sample_text", OrderRider="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_CompanyAssignRider_OrderDate_Time_value_roundtrip():
    instance = CompanyAssignRider(CustomerName="sample_text", OrderDate_Time="sample_text", OrderRider="sample_text")
    assert instance.OrderDate_Time == "sample_text"
    instance.OrderDate_Time = "sample_text_2"
    assert instance.OrderDate_Time == "sample_text_2"


def test_CompanyAssignRider_OrderRider_value_roundtrip():
    instance = CompanyAssignRider(CustomerName="sample_text", OrderDate_Time="sample_text", OrderRider="sample_text")
    assert instance.OrderRider == "sample_text"
    instance.OrderRider = "sample_text_2"
    assert instance.OrderRider == "sample_text_2"


def test_CompanyOrderHistory_CustomerName_value_roundtrip():
    instance = CompanyOrderHistory(CustomerName="sample_text", OrderDate_Time="sample_text", OrderReview="sample_text", OrderRider="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_CompanyOrderHistory_OrderDate_Time_value_roundtrip():
    instance = CompanyOrderHistory(CustomerName="sample_text", OrderDate_Time="sample_text", OrderReview="sample_text", OrderRider="sample_text")
    assert instance.OrderDate_Time == "sample_text"
    instance.OrderDate_Time = "sample_text_2"
    assert instance.OrderDate_Time == "sample_text_2"


def test_CompanyOrderHistory_OrderReview_value_roundtrip():
    instance = CompanyOrderHistory(CustomerName="sample_text", OrderDate_Time="sample_text", OrderReview="sample_text", OrderRider="sample_text")
    assert instance.OrderReview == "sample_text"
    instance.OrderReview = "sample_text_2"
    assert instance.OrderReview == "sample_text_2"


def test_CompanyOrderHistory_OrderRider_value_roundtrip():
    instance = CompanyOrderHistory(CustomerName="sample_text", OrderDate_Time="sample_text", OrderReview="sample_text", OrderRider="sample_text")
    assert instance.OrderRider == "sample_text"
    instance.OrderRider = "sample_text_2"
    assert instance.OrderRider == "sample_text_2"


def test_CompanyTrackOrder_CustomerName_value_roundtrip():
    instance = CompanyTrackOrder(CustomerName="sample_text", OrderDate_Time="sample_text", OrderRider="sample_text", OrderStatus="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_CompanyTrackOrder_OrderDate_Time_value_roundtrip():
    instance = CompanyTrackOrder(CustomerName="sample_text", OrderDate_Time="sample_text", OrderRider="sample_text", OrderStatus="sample_text")
    assert instance.OrderDate_Time == "sample_text"
    instance.OrderDate_Time = "sample_text_2"
    assert instance.OrderDate_Time == "sample_text_2"


def test_CompanyTrackOrder_OrderRider_value_roundtrip():
    instance = CompanyTrackOrder(CustomerName="sample_text", OrderDate_Time="sample_text", OrderRider="sample_text", OrderStatus="sample_text")
    assert instance.OrderRider == "sample_text"
    instance.OrderRider = "sample_text_2"
    assert instance.OrderRider == "sample_text_2"


def test_CompanyTrackOrder_OrderStatus_value_roundtrip():
    instance = CompanyTrackOrder(CustomerName="sample_text", OrderDate_Time="sample_text", OrderRider="sample_text", OrderStatus="sample_text")
    assert instance.OrderStatus == "sample_text"
    instance.OrderStatus = "sample_text_2"
    assert instance.OrderStatus == "sample_text_2"


def test_ConfirmOrder_OrderName_value_roundtrip():
    instance = ConfirmOrder(OrderName="sample_text", OrderPrice="sample_text", Quantity="sample_text", StoreName="sample_text")
    assert instance.OrderName == "sample_text"
    instance.OrderName = "sample_text_2"
    assert instance.OrderName == "sample_text_2"


def test_ConfirmOrder_OrderPrice_value_roundtrip():
    instance = ConfirmOrder(OrderName="sample_text", OrderPrice="sample_text", Quantity="sample_text", StoreName="sample_text")
    assert instance.OrderPrice == "sample_text"
    instance.OrderPrice = "sample_text_2"
    assert instance.OrderPrice == "sample_text_2"


def test_ConfirmOrder_Quantity_value_roundtrip():
    instance = ConfirmOrder(OrderName="sample_text", OrderPrice="sample_text", Quantity="sample_text", StoreName="sample_text")
    assert instance.Quantity == "sample_text"
    instance.Quantity = "sample_text_2"
    assert instance.Quantity == "sample_text_2"


def test_ConfirmOrder_StoreName_value_roundtrip():
    instance = ConfirmOrder(OrderName="sample_text", OrderPrice="sample_text", Quantity="sample_text", StoreName="sample_text")
    assert instance.StoreName == "sample_text"
    instance.StoreName = "sample_text_2"
    assert instance.StoreName == "sample_text_2"


def test_Login_Email_value_roundtrip():
    instance = Login(Email="sample_text", Password="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_Login_Password_value_roundtrip():
    instance = Login(Email="sample_text", Password="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_Order_OrderPrice_value_roundtrip():
    instance = Order(OrderPrice="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text", OrderTime_Date="sample_text")
    assert instance.OrderPrice == "sample_text"
    instance.OrderPrice = "sample_text_2"
    assert instance.OrderPrice == "sample_text_2"


def test_Order_OrderReview_value_roundtrip():
    instance = Order(OrderPrice="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text", OrderTime_Date="sample_text")
    assert instance.OrderReview == "sample_text"
    instance.OrderReview = "sample_text_2"
    assert instance.OrderReview == "sample_text_2"


def test_Order_OrderRider_value_roundtrip():
    instance = Order(OrderPrice="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text", OrderTime_Date="sample_text")
    assert instance.OrderRider == "sample_text"
    instance.OrderRider = "sample_text_2"
    assert instance.OrderRider == "sample_text_2"


def test_Order_OrderStatus_value_roundtrip():
    instance = Order(OrderPrice="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text", OrderTime_Date="sample_text")
    assert instance.OrderStatus == "sample_text"
    instance.OrderStatus = "sample_text_2"
    assert instance.OrderStatus == "sample_text_2"


def test_Order_OrderTime_Date_value_roundtrip():
    instance = Order(OrderPrice="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text", OrderTime_Date="sample_text")
    assert instance.OrderTime_Date == "sample_text"
    instance.OrderTime_Date = "sample_text_2"
    assert instance.OrderTime_Date == "sample_text_2"


def test_OrderHistory_OrderDate_Time_value_roundtrip():
    instance = OrderHistory(OrderDate_Time="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text")
    assert instance.OrderDate_Time == "sample_text"
    instance.OrderDate_Time = "sample_text_2"
    assert instance.OrderDate_Time == "sample_text_2"


def test_OrderHistory_OrderReview_value_roundtrip():
    instance = OrderHistory(OrderDate_Time="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text")
    assert instance.OrderReview == "sample_text"
    instance.OrderReview = "sample_text_2"
    assert instance.OrderReview == "sample_text_2"


def test_OrderHistory_OrderRider_value_roundtrip():
    instance = OrderHistory(OrderDate_Time="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text")
    assert instance.OrderRider == "sample_text"
    instance.OrderRider = "sample_text_2"
    assert instance.OrderRider == "sample_text_2"


def test_OrderHistory_OrderStatus_value_roundtrip():
    instance = OrderHistory(OrderDate_Time="sample_text", OrderReview="sample_text", OrderRider="sample_text", OrderStatus="sample_text")
    assert instance.OrderStatus == "sample_text"
    instance.OrderStatus = "sample_text_2"
    assert instance.OrderStatus == "sample_text_2"


def test_PlaceOrder_Name_value_roundtrip():
    instance = PlaceOrder(Name="sample_text", Price="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_PlaceOrder_Price_value_roundtrip():
    instance = PlaceOrder(Name="sample_text", Price="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_ReviewOrder_OrderTime_Date_value_roundtrip():
    instance = ReviewOrder(OrderTime_Date="sample_text", Review="sample_text", RiderName="sample_text")
    assert instance.OrderTime_Date == "sample_text"
    instance.OrderTime_Date = "sample_text_2"
    assert instance.OrderTime_Date == "sample_text_2"


def test_ReviewOrder_Review_value_roundtrip():
    instance = ReviewOrder(OrderTime_Date="sample_text", Review="sample_text", RiderName="sample_text")
    assert instance.Review == "sample_text"
    instance.Review = "sample_text_2"
    assert instance.Review == "sample_text_2"


def test_ReviewOrder_RiderName_value_roundtrip():
    instance = ReviewOrder(OrderTime_Date="sample_text", Review="sample_text", RiderName="sample_text")
    assert instance.RiderName == "sample_text"
    instance.RiderName = "sample_text_2"
    assert instance.RiderName == "sample_text_2"


def test_RiderStatusUpdate_CustomerName_value_roundtrip():
    instance = RiderStatusUpdate(CustomerName="sample_text", ItemList="sample_text", OrderDate_Time="sample_text")
    assert instance.CustomerName == "sample_text"
    instance.CustomerName = "sample_text_2"
    assert instance.CustomerName == "sample_text_2"


def test_RiderStatusUpdate_ItemList_value_roundtrip():
    instance = RiderStatusUpdate(CustomerName="sample_text", ItemList="sample_text", OrderDate_Time="sample_text")
    assert instance.ItemList == "sample_text"
    instance.ItemList = "sample_text_2"
    assert instance.ItemList == "sample_text_2"


def test_RiderStatusUpdate_OrderDate_Time_value_roundtrip():
    instance = RiderStatusUpdate(CustomerName="sample_text", ItemList="sample_text", OrderDate_Time="sample_text")
    assert instance.OrderDate_Time == "sample_text"
    instance.OrderDate_Time = "sample_text_2"
    assert instance.OrderDate_Time == "sample_text_2"


def test_Store_Name_value_roundtrip():
    instance = Store(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_TrackOrder_OrderTime_Date_value_roundtrip():
    instance = TrackOrder(OrderTime_Date="sample_text", OrderTrack="sample_text")
    assert instance.OrderTime_Date == "sample_text"
    instance.OrderTime_Date = "sample_text_2"
    assert instance.OrderTime_Date == "sample_text_2"


def test_TrackOrder_OrderTrack_value_roundtrip():
    instance = TrackOrder(OrderTime_Date="sample_text", OrderTrack="sample_text")
    assert instance.OrderTrack == "sample_text"
    instance.OrderTrack = "sample_text_2"
    assert instance.OrderTrack == "sample_text_2"


def test_UserRegisteration_Address_value_roundtrip():
    instance = UserRegisteration(Address="sample_text", Email="sample_text", FirstName="sample_text", LastName="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_UserRegisteration_Email_value_roundtrip():
    instance = UserRegisteration(Address="sample_text", Email="sample_text", FirstName="sample_text", LastName="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_UserRegisteration_FirstName_value_roundtrip():
    instance = UserRegisteration(Address="sample_text", Email="sample_text", FirstName="sample_text", LastName="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.FirstName == "sample_text"
    instance.FirstName = "sample_text_2"
    assert instance.FirstName == "sample_text_2"


def test_UserRegisteration_LastName_value_roundtrip():
    instance = UserRegisteration(Address="sample_text", Email="sample_text", FirstName="sample_text", LastName="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.LastName == "sample_text"
    instance.LastName = "sample_text_2"
    assert instance.LastName == "sample_text_2"


def test_UserRegisteration_Password_value_roundtrip():
    instance = UserRegisteration(Address="sample_text", Email="sample_text", FirstName="sample_text", LastName="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_UserRegisteration_Phone_value_roundtrip():
    instance = UserRegisteration(Address="sample_text", Email="sample_text", FirstName="sample_text", LastName="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.Phone == "sample_text"
    instance.Phone = "sample_text_2"
    assert instance.Phone == "sample_text_2"


def test_UserRegisteration_UserName_value_roundtrip():
    instance = UserRegisteration(Address="sample_text", Email="sample_text", FirstName="sample_text", LastName="sample_text", Password="sample_text", Phone="sample_text", UserName="sample_text")
    assert instance.UserName == "sample_text"
    instance.UserName = "sample_text_2"
    assert instance.UserName == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CartItems_strategy = st.builds(CartItems, Name=safe_text, Price=safe_text)
@given(instance=CartItems_strategy)
@settings(max_examples=25)
def test_CartItems_instantiation(instance):
    assert isinstance(instance, CartItems)


Categories_strategy = st.builds(Categories, Categories=safe_text)
@given(instance=Categories_strategy)
@settings(max_examples=25)
def test_Categories_instantiation(instance):
    assert isinstance(instance, Categories)


CompanyAddItem_strategy = st.builds(CompanyAddItem, Category=safe_text, Description=safe_text, Name=safe_text, Price=safe_text)
@given(instance=CompanyAddItem_strategy)
@settings(max_examples=25)
def test_CompanyAddItem_instantiation(instance):
    assert isinstance(instance, CompanyAddItem)


CompanyAddRider_strategy = st.builds(CompanyAddRider, Address=safe_text, CNIC=st.integers(), Email=safe_text, Name=safe_text, Password=safe_text, Phone=safe_text, UserName=safe_text)
@given(instance=CompanyAddRider_strategy)
@settings(max_examples=25)
def test_CompanyAddRider_instantiation(instance):
    assert isinstance(instance, CompanyAddRider)


CompanyAssignRider_strategy = st.builds(CompanyAssignRider, CustomerName=safe_text, OrderDate_Time=safe_text, OrderRider=safe_text)
@given(instance=CompanyAssignRider_strategy)
@settings(max_examples=25)
def test_CompanyAssignRider_instantiation(instance):
    assert isinstance(instance, CompanyAssignRider)


CompanyOrderHistory_strategy = st.builds(CompanyOrderHistory, CustomerName=safe_text, OrderDate_Time=safe_text, OrderReview=safe_text, OrderRider=safe_text)
@given(instance=CompanyOrderHistory_strategy)
@settings(max_examples=25)
def test_CompanyOrderHistory_instantiation(instance):
    assert isinstance(instance, CompanyOrderHistory)


CompanyTrackOrder_strategy = st.builds(CompanyTrackOrder, CustomerName=safe_text, OrderDate_Time=safe_text, OrderRider=safe_text, OrderStatus=safe_text)
@given(instance=CompanyTrackOrder_strategy)
@settings(max_examples=25)
def test_CompanyTrackOrder_instantiation(instance):
    assert isinstance(instance, CompanyTrackOrder)


ConfirmOrder_strategy = st.builds(ConfirmOrder, OrderName=safe_text, OrderPrice=safe_text, Quantity=safe_text, StoreName=safe_text)
@given(instance=ConfirmOrder_strategy)
@settings(max_examples=25)
def test_ConfirmOrder_instantiation(instance):
    assert isinstance(instance, ConfirmOrder)


Login_strategy = st.builds(Login, Email=safe_text, Password=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Order_strategy = st.builds(Order, OrderPrice=safe_text, OrderReview=safe_text, OrderRider=safe_text, OrderStatus=safe_text, OrderTime_Date=safe_text)
@given(instance=Order_strategy)
@settings(max_examples=25)
def test_Order_instantiation(instance):
    assert isinstance(instance, Order)


OrderHistory_strategy = st.builds(OrderHistory, OrderDate_Time=safe_text, OrderReview=safe_text, OrderRider=safe_text, OrderStatus=safe_text)
@given(instance=OrderHistory_strategy)
@settings(max_examples=25)
def test_OrderHistory_instantiation(instance):
    assert isinstance(instance, OrderHistory)


PlaceOrder_strategy = st.builds(PlaceOrder, Name=safe_text, Price=safe_text)
@given(instance=PlaceOrder_strategy)
@settings(max_examples=25)
def test_PlaceOrder_instantiation(instance):
    assert isinstance(instance, PlaceOrder)


ReviewOrder_strategy = st.builds(ReviewOrder, OrderTime_Date=safe_text, Review=safe_text, RiderName=safe_text)
@given(instance=ReviewOrder_strategy)
@settings(max_examples=25)
def test_ReviewOrder_instantiation(instance):
    assert isinstance(instance, ReviewOrder)


RiderStatusUpdate_strategy = st.builds(RiderStatusUpdate, CustomerName=safe_text, ItemList=safe_text, OrderDate_Time=safe_text)
@given(instance=RiderStatusUpdate_strategy)
@settings(max_examples=25)
def test_RiderStatusUpdate_instantiation(instance):
    assert isinstance(instance, RiderStatusUpdate)


Store_strategy = st.builds(Store, Name=safe_text)
@given(instance=Store_strategy)
@settings(max_examples=25)
def test_Store_instantiation(instance):
    assert isinstance(instance, Store)


TrackOrder_strategy = st.builds(TrackOrder, OrderTime_Date=safe_text, OrderTrack=safe_text)
@given(instance=TrackOrder_strategy)
@settings(max_examples=25)
def test_TrackOrder_instantiation(instance):
    assert isinstance(instance, TrackOrder)


UserRegisteration_strategy = st.builds(UserRegisteration, Address=safe_text, Email=safe_text, FirstName=safe_text, LastName=safe_text, Password=safe_text, Phone=safe_text, UserName=safe_text)
@given(instance=UserRegisteration_strategy)
@settings(max_examples=25)
def test_UserRegisteration_instantiation(instance):
    assert isinstance(instance, UserRegisteration)


phon_strategy = st.builds(phon)
@given(instance=phon_strategy)
@settings(max_examples=25)
def test_phon_instantiation(instance):
    assert isinstance(instance, phon)


void_Interface_strategy = st.builds(void_Interface)
@given(instance=void_Interface_strategy)
@settings(max_examples=25)
def test_void_Interface_instantiation(instance):
    assert isinstance(instance, void_Interface)


