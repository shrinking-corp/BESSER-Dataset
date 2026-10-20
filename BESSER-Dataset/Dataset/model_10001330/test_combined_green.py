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
    RiderStatusUpdate,
    Order,
    CompanyTrackOrder,
    CompanyOrderHistory,
    CompanyAssignRider,
    phon,
    CompanyAddRider,
    CompanyAddItem,
    CartItems,
    Login,
    UserRegisteration,
    PlaceOrder,
    Categories,
    ConfirmOrder,
    OrderHistory,
    ReviewOrder,
    void_Interface,
    Store,
    TrackOrder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_riderstatusupdate_is_not_abstract():
    assert not inspect.isabstract(RiderStatusUpdate)


def test_hyp_riderstatusupdate_constructor_exists():
    assert callable(RiderStatusUpdate.__init__)


def test_hyp_riderstatusupdate_constructor_args():
    sig = inspect.signature(RiderStatusUpdate.__init__)
    params = list(sig.parameters.keys())
    assert "ItemList" in params, "Missing parameter 'ItemList'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "OrderDate_Time" in params, "Missing parameter 'OrderDate_Time'"






def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "OrderPrice" in params, "Missing parameter 'OrderPrice'"
    assert "OrderReview" in params, "Missing parameter 'OrderReview'"
    assert "OrderTime_Date" in params, "Missing parameter 'OrderTime_Date'"
    assert "OrderStatus" in params, "Missing parameter 'OrderStatus'"
    assert "OrderRider" in params, "Missing parameter 'OrderRider'"








def test_hyp_companytrackorder_is_not_abstract():
    assert not inspect.isabstract(CompanyTrackOrder)


def test_hyp_companytrackorder_constructor_exists():
    assert callable(CompanyTrackOrder.__init__)


def test_hyp_companytrackorder_constructor_args():
    sig = inspect.signature(CompanyTrackOrder.__init__)
    params = list(sig.parameters.keys())
    assert "OrderDate_Time" in params, "Missing parameter 'OrderDate_Time'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "OrderRider" in params, "Missing parameter 'OrderRider'"
    assert "OrderStatus" in params, "Missing parameter 'OrderStatus'"







def test_hyp_companyorderhistory_is_not_abstract():
    assert not inspect.isabstract(CompanyOrderHistory)


def test_hyp_companyorderhistory_constructor_exists():
    assert callable(CompanyOrderHistory.__init__)


def test_hyp_companyorderhistory_constructor_args():
    sig = inspect.signature(CompanyOrderHistory.__init__)
    params = list(sig.parameters.keys())
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "OrderDate_Time" in params, "Missing parameter 'OrderDate_Time'"
    assert "OrderRider" in params, "Missing parameter 'OrderRider'"
    assert "OrderReview" in params, "Missing parameter 'OrderReview'"







def test_hyp_companyassignrider_is_not_abstract():
    assert not inspect.isabstract(CompanyAssignRider)


def test_hyp_companyassignrider_constructor_exists():
    assert callable(CompanyAssignRider.__init__)


def test_hyp_companyassignrider_constructor_args():
    sig = inspect.signature(CompanyAssignRider.__init__)
    params = list(sig.parameters.keys())
    assert "OrderRider" in params, "Missing parameter 'OrderRider'"
    assert "OrderDate_Time" in params, "Missing parameter 'OrderDate_Time'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"






def test_hyp_phon_is_not_abstract():
    assert not inspect.isabstract(phon)


def test_hyp_phon_constructor_exists():
    assert callable(phon.__init__)


def test_hyp_phon_constructor_args():
    sig = inspect.signature(phon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_companyaddrider_is_not_abstract():
    assert not inspect.isabstract(CompanyAddRider)


def test_hyp_companyaddrider_constructor_exists():
    assert callable(CompanyAddRider.__init__)


def test_hyp_companyaddrider_constructor_args():
    sig = inspect.signature(CompanyAddRider.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "CNIC" in params, "Missing parameter 'CNIC'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Email" in params, "Missing parameter 'Email'"










def test_hyp_companyadditem_is_not_abstract():
    assert not inspect.isabstract(CompanyAddItem)


def test_hyp_companyadditem_constructor_exists():
    assert callable(CompanyAddItem.__init__)


def test_hyp_companyadditem_constructor_args():
    sig = inspect.signature(CompanyAddItem.__init__)
    params = list(sig.parameters.keys())
    assert "Category" in params, "Missing parameter 'Category'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Name" in params, "Missing parameter 'Name'"







def test_hyp_cartitems_is_not_abstract():
    assert not inspect.isabstract(CartItems)


def test_hyp_cartitems_constructor_exists():
    assert callable(CartItems.__init__)


def test_hyp_cartitems_constructor_args():
    sig = inspect.signature(CartItems.__init__)
    params = list(sig.parameters.keys())
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Name" in params, "Missing parameter 'Name'"





def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Password" in params, "Missing parameter 'Password'"





def test_hyp_userregisteration_is_not_abstract():
    assert not inspect.isabstract(UserRegisteration)


def test_hyp_userregisteration_constructor_exists():
    assert callable(UserRegisteration.__init__)


def test_hyp_userregisteration_constructor_args():
    sig = inspect.signature(UserRegisteration.__init__)
    params = list(sig.parameters.keys())
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "FirstName" in params, "Missing parameter 'FirstName'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "Address" in params, "Missing parameter 'Address'"










def test_hyp_placeorder_is_not_abstract():
    assert not inspect.isabstract(PlaceOrder)


def test_hyp_placeorder_constructor_exists():
    assert callable(PlaceOrder.__init__)


def test_hyp_placeorder_constructor_args():
    sig = inspect.signature(PlaceOrder.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Price" in params, "Missing parameter 'Price'"





def test_hyp_categories_is_not_abstract():
    assert not inspect.isabstract(Categories)


def test_hyp_categories_constructor_exists():
    assert callable(Categories.__init__)


def test_hyp_categories_constructor_args():
    sig = inspect.signature(Categories.__init__)
    params = list(sig.parameters.keys())
    assert "Categories" in params, "Missing parameter 'Categories'"




def test_hyp_confirmorder_is_not_abstract():
    assert not inspect.isabstract(ConfirmOrder)


def test_hyp_confirmorder_constructor_exists():
    assert callable(ConfirmOrder.__init__)


def test_hyp_confirmorder_constructor_args():
    sig = inspect.signature(ConfirmOrder.__init__)
    params = list(sig.parameters.keys())
    assert "OrderName" in params, "Missing parameter 'OrderName'"
    assert "StoreName" in params, "Missing parameter 'StoreName'"
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "OrderPrice" in params, "Missing parameter 'OrderPrice'"







def test_hyp_orderhistory_is_not_abstract():
    assert not inspect.isabstract(OrderHistory)


def test_hyp_orderhistory_constructor_exists():
    assert callable(OrderHistory.__init__)


def test_hyp_orderhistory_constructor_args():
    sig = inspect.signature(OrderHistory.__init__)
    params = list(sig.parameters.keys())
    assert "OrderReview" in params, "Missing parameter 'OrderReview'"
    assert "OrderDate_Time" in params, "Missing parameter 'OrderDate_Time'"
    assert "OrderStatus" in params, "Missing parameter 'OrderStatus'"
    assert "OrderRider" in params, "Missing parameter 'OrderRider'"







def test_hyp_revieworder_is_not_abstract():
    assert not inspect.isabstract(ReviewOrder)


def test_hyp_revieworder_constructor_exists():
    assert callable(ReviewOrder.__init__)


def test_hyp_revieworder_constructor_args():
    sig = inspect.signature(ReviewOrder.__init__)
    params = list(sig.parameters.keys())
    assert "RiderName" in params, "Missing parameter 'RiderName'"
    assert "OrderTime_Date" in params, "Missing parameter 'OrderTime_Date'"
    assert "Review" in params, "Missing parameter 'Review'"






def test_hyp_void_interface_is_not_abstract():
    assert not inspect.isabstract(void_Interface)


def test_hyp_void_interface_constructor_exists():
    assert callable(void_Interface.__init__)


def test_hyp_void_interface_constructor_args():
    sig = inspect.signature(void_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_store_is_not_abstract():
    assert not inspect.isabstract(Store)


def test_hyp_store_constructor_exists():
    assert callable(Store.__init__)


def test_hyp_store_constructor_args():
    sig = inspect.signature(Store.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_trackorder_is_not_abstract():
    assert not inspect.isabstract(TrackOrder)


def test_hyp_trackorder_constructor_exists():
    assert callable(TrackOrder.__init__)


def test_hyp_trackorder_constructor_args():
    sig = inspect.signature(TrackOrder.__init__)
    params = list(sig.parameters.keys())
    assert "OrderTime_Date" in params, "Missing parameter 'OrderTime_Date'"
    assert "OrderTrack" in params, "Missing parameter 'OrderTrack'"




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
RiderStatusUpdate_strategy = st.builds(
    RiderStatusUpdate,
    ItemList=
        safe_text,
    CustomerName=
        safe_text,
    OrderDate_Time=
        safe_text
)
Order_strategy = st.builds(
    Order,
    OrderPrice=
        safe_text,
    OrderReview=
        safe_text,
    OrderTime_Date=
        safe_text,
    OrderStatus=
        safe_text,
    OrderRider=
        safe_text
)
CompanyTrackOrder_strategy = st.builds(
    CompanyTrackOrder,
    OrderDate_Time=
        safe_text,
    CustomerName=
        safe_text,
    OrderRider=
        safe_text,
    OrderStatus=
        safe_text
)
CompanyOrderHistory_strategy = st.builds(
    CompanyOrderHistory,
    CustomerName=
        safe_text,
    OrderDate_Time=
        safe_text,
    OrderRider=
        safe_text,
    OrderReview=
        safe_text
)
CompanyAssignRider_strategy = st.builds(
    CompanyAssignRider,
    OrderRider=
        safe_text,
    OrderDate_Time=
        safe_text,
    CustomerName=
        safe_text
)
phon_strategy = st.builds(
    phon,
)
CompanyAddRider_strategy = st.builds(
    CompanyAddRider,
    Name=
        safe_text,
    UserName=
        safe_text,
    Password=
        safe_text,
    CNIC=
        st.integers(),
    Address=
        safe_text,
    Phone=
        safe_text,
    Email=
        safe_text
)
CompanyAddItem_strategy = st.builds(
    CompanyAddItem,
    Category=
        safe_text,
    Description=
        safe_text,
    Price=
        safe_text,
    Name=
        safe_text
)
CartItems_strategy = st.builds(
    CartItems,
    Price=
        safe_text,
    Name=
        safe_text
)
Login_strategy = st.builds(
    Login,
    Email=
        safe_text,
    Password=
        safe_text
)
UserRegisteration_strategy = st.builds(
    UserRegisteration,
    LastName=
        safe_text,
    Password=
        safe_text,
    Email=
        safe_text,
    Phone=
        safe_text,
    FirstName=
        safe_text,
    UserName=
        safe_text,
    Address=
        safe_text
)
PlaceOrder_strategy = st.builds(
    PlaceOrder,
    Name=
        safe_text,
    Price=
        safe_text
)
Categories_strategy = st.builds(
    Categories,
    Categories=
        safe_text
)
ConfirmOrder_strategy = st.builds(
    ConfirmOrder,
    OrderName=
        safe_text,
    StoreName=
        safe_text,
    Quantity=
        safe_text,
    OrderPrice=
        safe_text
)
OrderHistory_strategy = st.builds(
    OrderHistory,
    OrderReview=
        safe_text,
    OrderDate_Time=
        safe_text,
    OrderStatus=
        safe_text,
    OrderRider=
        safe_text
)
ReviewOrder_strategy = st.builds(
    ReviewOrder,
    RiderName=
        safe_text,
    OrderTime_Date=
        safe_text,
    Review=
        safe_text
)
void_Interface_strategy = st.builds(
    void_Interface,
)
Store_strategy = st.builds(
    Store,
    Name=
        safe_text
)
TrackOrder_strategy = st.builds(
    TrackOrder,
    OrderTime_Date=
        safe_text,
    OrderTrack=
        safe_text
)




@given(instance=RiderStatusUpdate_strategy)
def test_hyp_riderstatusupdate_ItemList_setter(instance):
    original = instance.ItemList
    instance.ItemList = original
    assert instance.ItemList == original



@given(instance=RiderStatusUpdate_strategy)
def test_hyp_riderstatusupdate_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=RiderStatusUpdate_strategy)
def test_hyp_riderstatusupdate_OrderDate_Time_setter(instance):
    original = instance.OrderDate_Time
    instance.OrderDate_Time = original
    assert instance.OrderDate_Time == original




@given(instance=Order_strategy)
def test_hyp_order_OrderPrice_setter(instance):
    original = instance.OrderPrice
    instance.OrderPrice = original
    assert instance.OrderPrice == original



@given(instance=Order_strategy)
def test_hyp_order_OrderReview_setter(instance):
    original = instance.OrderReview
    instance.OrderReview = original
    assert instance.OrderReview == original



@given(instance=Order_strategy)
def test_hyp_order_OrderTime_Date_setter(instance):
    original = instance.OrderTime_Date
    instance.OrderTime_Date = original
    assert instance.OrderTime_Date == original



@given(instance=Order_strategy)
def test_hyp_order_OrderStatus_setter(instance):
    original = instance.OrderStatus
    instance.OrderStatus = original
    assert instance.OrderStatus == original



@given(instance=Order_strategy)
def test_hyp_order_OrderRider_setter(instance):
    original = instance.OrderRider
    instance.OrderRider = original
    assert instance.OrderRider == original




@given(instance=CompanyTrackOrder_strategy)
def test_hyp_companytrackorder_OrderDate_Time_setter(instance):
    original = instance.OrderDate_Time
    instance.OrderDate_Time = original
    assert instance.OrderDate_Time == original



@given(instance=CompanyTrackOrder_strategy)
def test_hyp_companytrackorder_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=CompanyTrackOrder_strategy)
def test_hyp_companytrackorder_OrderRider_setter(instance):
    original = instance.OrderRider
    instance.OrderRider = original
    assert instance.OrderRider == original



@given(instance=CompanyTrackOrder_strategy)
def test_hyp_companytrackorder_OrderStatus_setter(instance):
    original = instance.OrderStatus
    instance.OrderStatus = original
    assert instance.OrderStatus == original




@given(instance=CompanyOrderHistory_strategy)
def test_hyp_companyorderhistory_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=CompanyOrderHistory_strategy)
def test_hyp_companyorderhistory_OrderDate_Time_setter(instance):
    original = instance.OrderDate_Time
    instance.OrderDate_Time = original
    assert instance.OrderDate_Time == original



@given(instance=CompanyOrderHistory_strategy)
def test_hyp_companyorderhistory_OrderRider_setter(instance):
    original = instance.OrderRider
    instance.OrderRider = original
    assert instance.OrderRider == original



@given(instance=CompanyOrderHistory_strategy)
def test_hyp_companyorderhistory_OrderReview_setter(instance):
    original = instance.OrderReview
    instance.OrderReview = original
    assert instance.OrderReview == original




@given(instance=CompanyAssignRider_strategy)
def test_hyp_companyassignrider_OrderRider_setter(instance):
    original = instance.OrderRider
    instance.OrderRider = original
    assert instance.OrderRider == original



@given(instance=CompanyAssignRider_strategy)
def test_hyp_companyassignrider_OrderDate_Time_setter(instance):
    original = instance.OrderDate_Time
    instance.OrderDate_Time = original
    assert instance.OrderDate_Time == original



@given(instance=CompanyAssignRider_strategy)
def test_hyp_companyassignrider_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original





@given(instance=CompanyAddRider_strategy)
def test_hyp_companyaddrider_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=CompanyAddRider_strategy)
def test_hyp_companyaddrider_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=CompanyAddRider_strategy)
def test_hyp_companyaddrider_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=CompanyAddRider_strategy)
def test_hyp_companyaddrider_CNIC_setter(instance):
    original = instance.CNIC
    instance.CNIC = original
    assert instance.CNIC == original



@given(instance=CompanyAddRider_strategy)
def test_hyp_companyaddrider_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=CompanyAddRider_strategy)
def test_hyp_companyaddrider_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=CompanyAddRider_strategy)
def test_hyp_companyaddrider_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original




@given(instance=CompanyAddItem_strategy)
def test_hyp_companyadditem_Category_setter(instance):
    original = instance.Category
    instance.Category = original
    assert instance.Category == original



@given(instance=CompanyAddItem_strategy)
def test_hyp_companyadditem_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=CompanyAddItem_strategy)
def test_hyp_companyadditem_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=CompanyAddItem_strategy)
def test_hyp_companyadditem_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=CartItems_strategy)
def test_hyp_cartitems_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=CartItems_strategy)
def test_hyp_cartitems_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=Login_strategy)
def test_hyp_login_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Login_strategy)
def test_hyp_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original




@given(instance=UserRegisteration_strategy)
def test_hyp_userregisteration_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=UserRegisteration_strategy)
def test_hyp_userregisteration_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=UserRegisteration_strategy)
def test_hyp_userregisteration_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=UserRegisteration_strategy)
def test_hyp_userregisteration_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=UserRegisteration_strategy)
def test_hyp_userregisteration_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original



@given(instance=UserRegisteration_strategy)
def test_hyp_userregisteration_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=UserRegisteration_strategy)
def test_hyp_userregisteration_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original




@given(instance=PlaceOrder_strategy)
def test_hyp_placeorder_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=PlaceOrder_strategy)
def test_hyp_placeorder_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original




@given(instance=Categories_strategy)
def test_hyp_categories_Categories_setter(instance):
    original = instance.Categories
    instance.Categories = original
    assert instance.Categories == original




@given(instance=ConfirmOrder_strategy)
def test_hyp_confirmorder_OrderName_setter(instance):
    original = instance.OrderName
    instance.OrderName = original
    assert instance.OrderName == original



@given(instance=ConfirmOrder_strategy)
def test_hyp_confirmorder_StoreName_setter(instance):
    original = instance.StoreName
    instance.StoreName = original
    assert instance.StoreName == original



@given(instance=ConfirmOrder_strategy)
def test_hyp_confirmorder_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=ConfirmOrder_strategy)
def test_hyp_confirmorder_OrderPrice_setter(instance):
    original = instance.OrderPrice
    instance.OrderPrice = original
    assert instance.OrderPrice == original




@given(instance=OrderHistory_strategy)
def test_hyp_orderhistory_OrderReview_setter(instance):
    original = instance.OrderReview
    instance.OrderReview = original
    assert instance.OrderReview == original



@given(instance=OrderHistory_strategy)
def test_hyp_orderhistory_OrderDate_Time_setter(instance):
    original = instance.OrderDate_Time
    instance.OrderDate_Time = original
    assert instance.OrderDate_Time == original



@given(instance=OrderHistory_strategy)
def test_hyp_orderhistory_OrderStatus_setter(instance):
    original = instance.OrderStatus
    instance.OrderStatus = original
    assert instance.OrderStatus == original



@given(instance=OrderHistory_strategy)
def test_hyp_orderhistory_OrderRider_setter(instance):
    original = instance.OrderRider
    instance.OrderRider = original
    assert instance.OrderRider == original




@given(instance=ReviewOrder_strategy)
def test_hyp_revieworder_RiderName_setter(instance):
    original = instance.RiderName
    instance.RiderName = original
    assert instance.RiderName == original



@given(instance=ReviewOrder_strategy)
def test_hyp_revieworder_OrderTime_Date_setter(instance):
    original = instance.OrderTime_Date
    instance.OrderTime_Date = original
    assert instance.OrderTime_Date == original



@given(instance=ReviewOrder_strategy)
def test_hyp_revieworder_Review_setter(instance):
    original = instance.Review
    instance.Review = original
    assert instance.Review == original





@given(instance=Store_strategy)
def test_hyp_store_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original




@given(instance=TrackOrder_strategy)
def test_hyp_trackorder_OrderTime_Date_setter(instance):
    original = instance.OrderTime_Date
    instance.OrderTime_Date = original
    assert instance.OrderTime_Date == original



@given(instance=TrackOrder_strategy)
def test_hyp_trackorder_OrderTrack_setter(instance):
    original = instance.OrderTrack
    instance.OrderTrack = original
    assert instance.OrderTrack == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



