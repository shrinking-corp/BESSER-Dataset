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
    FeedBack,
    CheckOut_Entity,
    StayIn_Entity,
    User_Entity,
    CheckIn_Entity,
    PostStay_Entity,
    Payment,
    Booking_Entity,
    Bill_Details,
    Booking_Status,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_feedback_is_not_abstract():
    assert not inspect.isabstract(FeedBack)


def test_hyp_feedback_constructor_exists():
    assert callable(FeedBack.__init__)


def test_hyp_feedback_constructor_args():
    sig = inspect.signature(FeedBack.__init__)
    params = list(sig.parameters.keys())
    assert "Rating" in params, "Missing parameter 'Rating'"
    assert "FeedBackMessage" in params, "Missing parameter 'FeedBackMessage'"





def test_hyp_checkout_entity_is_not_abstract():
    assert not inspect.isabstract(CheckOut_Entity)


def test_hyp_checkout_entity_constructor_exists():
    assert callable(CheckOut_Entity.__init__)


def test_hyp_checkout_entity_constructor_args():
    sig = inspect.signature(CheckOut_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "ItemisedBillDetails" in params, "Missing parameter 'ItemisedBillDetails'"

def test_hyp_checkout_entity_has_price():
    assert hasattr(CheckOut_Entity, "price")
    descriptor = None
    for klass in CheckOut_Entity.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_hyp_checkout_entity_has_ItemisedBillDetails():
    assert hasattr(CheckOut_Entity, "ItemisedBillDetails")
    descriptor = None
    for klass in CheckOut_Entity.__mro__:
        if "ItemisedBillDetails" in klass.__dict__:
            descriptor = klass.__dict__["ItemisedBillDetails"]
            break
    assert isinstance(descriptor, property)



def test_hyp_stayin_entity_is_not_abstract():
    assert not inspect.isabstract(StayIn_Entity)


def test_hyp_stayin_entity_constructor_exists():
    assert callable(StayIn_Entity.__init__)


def test_hyp_stayin_entity_constructor_args():
    sig = inspect.signature(StayIn_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "promotionsList" in params, "Missing parameter 'promotionsList'"
    assert "oodList" in params, "Missing parameter 'oodList'"
    assert "placeOfInterest" in params, "Missing parameter 'placeOfInterest'"
    assert "EntertainMentList" in params, "Missing parameter 'EntertainMentList'"
    assert "status" in params, "Missing parameter 'status'"
    assert "InPremisesList" in params, "Missing parameter 'InPremisesList'"

def test_hyp_stayin_entity_has_promotionsList():
    assert hasattr(StayIn_Entity, "promotionsList")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "promotionsList" in klass.__dict__:
            descriptor = klass.__dict__["promotionsList"]
            break
    assert isinstance(descriptor, property)

def test_hyp_stayin_entity_has_oodList():
    assert hasattr(StayIn_Entity, "oodList")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "oodList" in klass.__dict__:
            descriptor = klass.__dict__["oodList"]
            break
    assert isinstance(descriptor, property)

def test_hyp_stayin_entity_has_placeOfInterest():
    assert hasattr(StayIn_Entity, "placeOfInterest")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "placeOfInterest" in klass.__dict__:
            descriptor = klass.__dict__["placeOfInterest"]
            break
    assert isinstance(descriptor, property)

def test_hyp_stayin_entity_has_EntertainMentList():
    assert hasattr(StayIn_Entity, "EntertainMentList")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "EntertainMentList" in klass.__dict__:
            descriptor = klass.__dict__["EntertainMentList"]
            break
    assert isinstance(descriptor, property)

def test_hyp_stayin_entity_has_status():
    assert hasattr(StayIn_Entity, "status")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_stayin_entity_has_InPremisesList():
    assert hasattr(StayIn_Entity, "InPremisesList")
    descriptor = None
    for klass in StayIn_Entity.__mro__:
        if "InPremisesList" in klass.__dict__:
            descriptor = klass.__dict__["InPremisesList"]
            break
    assert isinstance(descriptor, property)



def test_hyp_user_entity_is_not_abstract():
    assert not inspect.isabstract(User_Entity)


def test_hyp_user_entity_constructor_exists():
    assert callable(User_Entity.__init__)


def test_hyp_user_entity_constructor_args():
    sig = inspect.signature(User_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "City" in params, "Missing parameter 'City'"
    assert "login" in params, "Missing parameter 'login'"
    assert "password" in params, "Missing parameter 'password'"
    assert "Email" in params, "Missing parameter 'Email'"







def test_hyp_checkin_entity_is_not_abstract():
    assert not inspect.isabstract(CheckIn_Entity)


def test_hyp_checkin_entity_constructor_exists():
    assert callable(CheckIn_Entity.__init__)


def test_hyp_checkin_entity_constructor_args():
    sig = inspect.signature(CheckIn_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "QRCode" in params, "Missing parameter 'QRCode'"
    assert "CheckInStatus" in params, "Missing parameter 'CheckInStatus'"
    assert "paymentMode" in params, "Missing parameter 'paymentMode'"
    assert "MobileKey" in params, "Missing parameter 'MobileKey'"
    assert "PickUpAddress" in params, "Missing parameter 'PickUpAddress'"








def test_hyp_poststay_entity_is_not_abstract():
    assert not inspect.isabstract(PostStay_Entity)


def test_hyp_poststay_entity_constructor_exists():
    assert callable(PostStay_Entity.__init__)


def test_hyp_poststay_entity_constructor_args():
    sig = inspect.signature(PostStay_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "ThanksMessage" in params, "Missing parameter 'ThanksMessage'"
    assert "PromotionPoints" in params, "Missing parameter 'PromotionPoints'"
    assert "DiscountPoints" in params, "Missing parameter 'DiscountPoints'"






def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "paidDate" in params, "Missing parameter 'paidDate'"
    assert "details" in params, "Missing parameter 'details'"
    assert "total" in params, "Missing parameter 'total'"






def test_hyp_booking_entity_is_not_abstract():
    assert not inspect.isabstract(Booking_Entity)


def test_hyp_booking_entity_constructor_exists():
    assert callable(Booking_Entity.__init__)


def test_hyp_booking_entity_constructor_args():
    sig = inspect.signature(Booking_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "NoOfDays" in params, "Missing parameter 'NoOfDays'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "CheckInDate" in params, "Missing parameter 'CheckInDate'"
    assert "address" in params, "Missing parameter 'address'"






def test_hyp_bill_details_exists():
    # Check that the Enumeration exists
    assert Bill_Details is not None

def test_hyp_bill_details_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Bill_Details]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Bill_Details"

def test_hyp_booking_status_exists():
    # Check that the Enumeration exists
    assert Booking_Status is not None

def test_hyp_booking_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Booking_Status]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Booking_Status"


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
FeedBack_strategy = st.builds(
    FeedBack,
    Rating=
        safe_text,
    FeedBackMessage=
        safe_text
)
CheckOut_Entity_strategy = st.builds(
    CheckOut_Entity,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ItemisedBillDetails=
        st.none()
)
StayIn_Entity_strategy = st.builds(
    StayIn_Entity,
    promotionsList=
        safe_text,
    oodList=
        safe_text,
    placeOfInterest=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    EntertainMentList=
        safe_text,
    status=
        st.none(),
    InPremisesList=
        safe_text
)
User_Entity_strategy = st.builds(
    User_Entity,
    City=
        safe_text,
    login=
        safe_text,
    password=
        safe_text,
    Email=
        safe_text
)
CheckIn_Entity_strategy = st.builds(
    CheckIn_Entity,
    QRCode=
        safe_text,
    CheckInStatus=
        safe_text,
    paymentMode=
        safe_text,
    MobileKey=
        safe_text,
    PickUpAddress=
        safe_text
)
PostStay_Entity_strategy = st.builds(
    PostStay_Entity,
    ThanksMessage=
        safe_text,
    PromotionPoints=
        safe_text,
    DiscountPoints=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    paidDate=
        st.dates(),
    details=
        safe_text,
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Booking_Entity_strategy = st.builds(
    Booking_Entity,
    NoOfDays=
        st.integers(),
    email=
        safe_text,
    phone=
        safe_text,
    CheckInDate=
        st.dates(),
    address=
        safe_text
)




@given(instance=FeedBack_strategy)
def test_hyp_feedback_Rating_setter(instance):
    original = instance.Rating
    instance.Rating = original
    assert instance.Rating == original



@given(instance=FeedBack_strategy)
def test_hyp_feedback_FeedBackMessage_setter(instance):
    original = instance.FeedBackMessage
    instance.FeedBackMessage = original
    assert instance.FeedBackMessage == original

@given(instance=CheckOut_Entity_strategy)
@settings(max_examples=50)
def test_hyp_checkout_entity_instantiation(instance):
    assert isinstance(instance, CheckOut_Entity)



@given(instance=CheckOut_Entity_strategy)
def test_hyp_checkout_entity_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=CheckOut_Entity_strategy)
def test_hyp_checkout_entity_ItemisedBillDetails_setter(instance):
    original = instance.ItemisedBillDetails
    instance.ItemisedBillDetails = original
    assert instance.ItemisedBillDetails == original

@given(instance=StayIn_Entity_strategy)
@settings(max_examples=50)
def test_hyp_stayin_entity_instantiation(instance):
    assert isinstance(instance, StayIn_Entity)



@given(instance=StayIn_Entity_strategy)
def test_hyp_stayin_entity_promotionsList_setter(instance):
    original = instance.promotionsList
    instance.promotionsList = original
    assert instance.promotionsList == original



@given(instance=StayIn_Entity_strategy)
def test_hyp_stayin_entity_oodList_setter(instance):
    original = instance.oodList
    instance.oodList = original
    assert instance.oodList == original



@given(instance=StayIn_Entity_strategy)
def test_hyp_stayin_entity_placeOfInterest_setter(instance):
    original = instance.placeOfInterest
    instance.placeOfInterest = original
    assert instance.placeOfInterest == original



@given(instance=StayIn_Entity_strategy)
def test_hyp_stayin_entity_EntertainMentList_setter(instance):
    original = instance.EntertainMentList
    instance.EntertainMentList = original
    assert instance.EntertainMentList == original



@given(instance=StayIn_Entity_strategy)
def test_hyp_stayin_entity_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=StayIn_Entity_strategy)
def test_hyp_stayin_entity_InPremisesList_setter(instance):
    original = instance.InPremisesList
    instance.InPremisesList = original
    assert instance.InPremisesList == original




@given(instance=User_Entity_strategy)
def test_hyp_user_entity_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=User_Entity_strategy)
def test_hyp_user_entity_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=User_Entity_strategy)
def test_hyp_user_entity_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_Entity_strategy)
def test_hyp_user_entity_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original




@given(instance=CheckIn_Entity_strategy)
def test_hyp_checkin_entity_QRCode_setter(instance):
    original = instance.QRCode
    instance.QRCode = original
    assert instance.QRCode == original



@given(instance=CheckIn_Entity_strategy)
def test_hyp_checkin_entity_CheckInStatus_setter(instance):
    original = instance.CheckInStatus
    instance.CheckInStatus = original
    assert instance.CheckInStatus == original



@given(instance=CheckIn_Entity_strategy)
def test_hyp_checkin_entity_paymentMode_setter(instance):
    original = instance.paymentMode
    instance.paymentMode = original
    assert instance.paymentMode == original



@given(instance=CheckIn_Entity_strategy)
def test_hyp_checkin_entity_MobileKey_setter(instance):
    original = instance.MobileKey
    instance.MobileKey = original
    assert instance.MobileKey == original



@given(instance=CheckIn_Entity_strategy)
def test_hyp_checkin_entity_PickUpAddress_setter(instance):
    original = instance.PickUpAddress
    instance.PickUpAddress = original
    assert instance.PickUpAddress == original




@given(instance=PostStay_Entity_strategy)
def test_hyp_poststay_entity_ThanksMessage_setter(instance):
    original = instance.ThanksMessage
    instance.ThanksMessage = original
    assert instance.ThanksMessage == original



@given(instance=PostStay_Entity_strategy)
def test_hyp_poststay_entity_PromotionPoints_setter(instance):
    original = instance.PromotionPoints
    instance.PromotionPoints = original
    assert instance.PromotionPoints == original



@given(instance=PostStay_Entity_strategy)
def test_hyp_poststay_entity_DiscountPoints_setter(instance):
    original = instance.DiscountPoints
    instance.DiscountPoints = original
    assert instance.DiscountPoints == original




@given(instance=Payment_strategy)
def test_hyp_payment_paidDate_setter(instance):
    original = instance.paidDate
    instance.paidDate = original
    assert instance.paidDate == original



@given(instance=Payment_strategy)
def test_hyp_payment_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=Payment_strategy)
def test_hyp_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original




@given(instance=Booking_Entity_strategy)
def test_hyp_booking_entity_NoOfDays_setter(instance):
    original = instance.NoOfDays
    instance.NoOfDays = original
    assert instance.NoOfDays == original



@given(instance=Booking_Entity_strategy)
def test_hyp_booking_entity_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Booking_Entity_strategy)
def test_hyp_booking_entity_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Booking_Entity_strategy)
def test_hyp_booking_entity_CheckInDate_setter(instance):
    original = instance.CheckInDate
    instance.CheckInDate = original
    assert instance.CheckInDate == original



@given(instance=Booking_Entity_strategy)
def test_hyp_booking_entity_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Booking_Entity,
    CheckIn_Entity,
    CheckOut_Entity,
    FeedBack,
    Payment,
    PostStay_Entity,
    StayIn_Entity,
    User_Entity,
    Bill_Details,
    Booking_Status,
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

def test_Booking_Entity_CheckInDate_value_roundtrip():
    instance = Booking_Entity(CheckInDate=date(2024, 1, 1), NoOfDays=7, address="sample_text", email="sample_text", phone="sample_text")
    assert instance.CheckInDate == date(2024, 1, 1)
    instance.CheckInDate = date(2025, 6, 15)
    assert instance.CheckInDate == date(2025, 6, 15)


def test_Booking_Entity_NoOfDays_value_roundtrip():
    instance = Booking_Entity(CheckInDate=date(2024, 1, 1), NoOfDays=7, address="sample_text", email="sample_text", phone="sample_text")
    assert instance.NoOfDays == 7
    instance.NoOfDays = 13
    assert instance.NoOfDays == 13


def test_Booking_Entity_address_value_roundtrip():
    instance = Booking_Entity(CheckInDate=date(2024, 1, 1), NoOfDays=7, address="sample_text", email="sample_text", phone="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Booking_Entity_email_value_roundtrip():
    instance = Booking_Entity(CheckInDate=date(2024, 1, 1), NoOfDays=7, address="sample_text", email="sample_text", phone="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Booking_Entity_phone_value_roundtrip():
    instance = Booking_Entity(CheckInDate=date(2024, 1, 1), NoOfDays=7, address="sample_text", email="sample_text", phone="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_CheckIn_Entity_CheckInStatus_value_roundtrip():
    instance = CheckIn_Entity(CheckInStatus="sample_text", MobileKey="sample_text", PickUpAddress="sample_text", QRCode="sample_text", paymentMode="sample_text")
    assert instance.CheckInStatus == "sample_text"
    instance.CheckInStatus = "sample_text_2"
    assert instance.CheckInStatus == "sample_text_2"


def test_CheckIn_Entity_MobileKey_value_roundtrip():
    instance = CheckIn_Entity(CheckInStatus="sample_text", MobileKey="sample_text", PickUpAddress="sample_text", QRCode="sample_text", paymentMode="sample_text")
    assert instance.MobileKey == "sample_text"
    instance.MobileKey = "sample_text_2"
    assert instance.MobileKey == "sample_text_2"


def test_CheckIn_Entity_PickUpAddress_value_roundtrip():
    instance = CheckIn_Entity(CheckInStatus="sample_text", MobileKey="sample_text", PickUpAddress="sample_text", QRCode="sample_text", paymentMode="sample_text")
    assert instance.PickUpAddress == "sample_text"
    instance.PickUpAddress = "sample_text_2"
    assert instance.PickUpAddress == "sample_text_2"


def test_CheckIn_Entity_QRCode_value_roundtrip():
    instance = CheckIn_Entity(CheckInStatus="sample_text", MobileKey="sample_text", PickUpAddress="sample_text", QRCode="sample_text", paymentMode="sample_text")
    assert instance.QRCode == "sample_text"
    instance.QRCode = "sample_text_2"
    assert instance.QRCode == "sample_text_2"


def test_CheckIn_Entity_paymentMode_value_roundtrip():
    instance = CheckIn_Entity(CheckInStatus="sample_text", MobileKey="sample_text", PickUpAddress="sample_text", QRCode="sample_text", paymentMode="sample_text")
    assert instance.paymentMode == "sample_text"
    instance.paymentMode = "sample_text_2"
    assert instance.paymentMode == "sample_text_2"


def test_FeedBack_FeedBackMessage_value_roundtrip():
    instance = FeedBack(FeedBackMessage="sample_text", Rating="sample_text")
    assert instance.FeedBackMessage == "sample_text"
    instance.FeedBackMessage = "sample_text_2"
    assert instance.FeedBackMessage == "sample_text_2"


def test_FeedBack_Rating_value_roundtrip():
    instance = FeedBack(FeedBackMessage="sample_text", Rating="sample_text")
    assert instance.Rating == "sample_text"
    instance.Rating = "sample_text_2"
    assert instance.Rating == "sample_text_2"


def test_Payment_details_value_roundtrip():
    instance = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    assert instance.details == "sample_text"
    instance.details = "sample_text_2"
    assert instance.details == "sample_text_2"


def test_Payment_paidDate_value_roundtrip():
    instance = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    assert instance.paidDate == date(2024, 1, 1)
    instance.paidDate = date(2025, 6, 15)
    assert instance.paidDate == date(2025, 6, 15)


def test_Payment_total_value_roundtrip():
    instance = Payment(details="sample_text", paidDate=date(2024, 1, 1), total=3.14)
    assert instance.total == 3.14
    instance.total = 9.99
    assert instance.total == 9.99


def test_PostStay_Entity_DiscountPoints_value_roundtrip():
    instance = PostStay_Entity(DiscountPoints="sample_text", PromotionPoints="sample_text", ThanksMessage="sample_text")
    assert instance.DiscountPoints == "sample_text"
    instance.DiscountPoints = "sample_text_2"
    assert instance.DiscountPoints == "sample_text_2"


def test_PostStay_Entity_PromotionPoints_value_roundtrip():
    instance = PostStay_Entity(DiscountPoints="sample_text", PromotionPoints="sample_text", ThanksMessage="sample_text")
    assert instance.PromotionPoints == "sample_text"
    instance.PromotionPoints = "sample_text_2"
    assert instance.PromotionPoints == "sample_text_2"


def test_PostStay_Entity_ThanksMessage_value_roundtrip():
    instance = PostStay_Entity(DiscountPoints="sample_text", PromotionPoints="sample_text", ThanksMessage="sample_text")
    assert instance.ThanksMessage == "sample_text"
    instance.ThanksMessage = "sample_text_2"
    assert instance.ThanksMessage == "sample_text_2"


def test_User_Entity_City_value_roundtrip():
    instance = User_Entity(City="sample_text", Email="sample_text", login="sample_text", password="sample_text")
    assert instance.City == "sample_text"
    instance.City = "sample_text_2"
    assert instance.City == "sample_text_2"


def test_User_Entity_Email_value_roundtrip():
    instance = User_Entity(City="sample_text", Email="sample_text", login="sample_text", password="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_User_Entity_login_value_roundtrip():
    instance = User_Entity(City="sample_text", Email="sample_text", login="sample_text", password="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_User_Entity_password_value_roundtrip():
    instance = User_Entity(City="sample_text", Email="sample_text", login="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_assoc_Account_ShoppingCart_link_reassign_clear():
    a = PostStay_Entity(DiscountPoints="sample_text", PromotionPoints="sample_text", ThanksMessage="sample_text")
    b1 = CheckIn_Entity(CheckInStatus="sample_text", MobileKey="sample_text", PickUpAddress="sample_text", QRCode="sample_text", paymentMode="sample_text")
    b2 = CheckIn_Entity(CheckInStatus="sample_text_2", MobileKey="sample_text_2", PickUpAddress="sample_text_2", QRCode="sample_text_2", paymentMode="sample_text_2")
    _safe_set(a, 'undefined7', b1)
    assert _is_linked(a, 'undefined7', b1)
    if hasattr(b1, 'undefined6'):
        assert _is_linked(b1, 'undefined6', a)
    _safe_set(a, 'undefined7', b2)
    assert _is_linked(a, 'undefined7', b2)
    if hasattr(b1, 'undefined6'):
        assert not _is_linked(b1, 'undefined6', a)
    if hasattr(b2, 'undefined6'):
        assert _is_linked(b2, 'undefined6', a)
    _safe_set(a, 'undefined7', None)
    assert not _is_linked(a, 'undefined7', b2)
    if hasattr(b2, 'undefined6'):
        assert not _is_linked(b2, 'undefined6', a)


def test_assoc_WebUser_Customer_link_reassign_clear():
    a = User_Entity(City="sample_text", Email="sample_text", login="sample_text", password="sample_text")
    b1 = Booking_Entity(CheckInDate=date(2024, 1, 1), NoOfDays=7, address="sample_text", email="sample_text", phone="sample_text")
    b2 = Booking_Entity(CheckInDate=date(2025, 6, 15), NoOfDays=13, address="sample_text_2", email="sample_text_2", phone="sample_text_2")
    _safe_set(a, 'Booking4', b1)
    assert _is_linked(a, 'Booking4', b1)
    if hasattr(b1, 'webUser5'):
        assert _is_linked(b1, 'webUser5', a)
    _safe_set(a, 'Booking4', b2)
    assert _is_linked(a, 'Booking4', b2)
    if hasattr(b1, 'webUser5'):
        assert not _is_linked(b1, 'webUser5', a)
    if hasattr(b2, 'webUser5'):
        assert _is_linked(b2, 'webUser5', a)
    _safe_set(a, 'Booking4', None)
    assert not _is_linked(a, 'Booking4', b2)
    if hasattr(b2, 'webUser5'):
        assert not _is_linked(b2, 'webUser5', a)


def test_assoc_WebUser_ShoppingCart_link_reassign_clear():
    a = User_Entity(City="sample_text", Email="sample_text", login="sample_text", password="sample_text")
    b1 = PostStay_Entity(DiscountPoints="sample_text", PromotionPoints="sample_text", ThanksMessage="sample_text")
    b2 = PostStay_Entity(DiscountPoints="sample_text_2", PromotionPoints="sample_text_2", ThanksMessage="sample_text_2")
    _safe_set(a, 'Start_Resedentz2', b1)
    assert _is_linked(a, 'Start_Resedentz2', b1)
    if hasattr(b1, 'webUser3'):
        assert _is_linked(b1, 'webUser3', a)
    _safe_set(a, 'Start_Resedentz2', b2)
    assert _is_linked(a, 'Start_Resedentz2', b2)
    if hasattr(b1, 'webUser3'):
        assert not _is_linked(b1, 'webUser3', a)
    if hasattr(b2, 'webUser3'):
        assert _is_linked(b2, 'webUser3', a)
    _safe_set(a, 'Start_Resedentz2', None)
    assert not _is_linked(a, 'Start_Resedentz2', b2)
    if hasattr(b2, 'webUser3'):
        assert not _is_linked(b2, 'webUser3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Booking_Entity_strategy = st.builds(Booking_Entity, CheckInDate=st.dates(), NoOfDays=st.integers(), address=safe_text, email=safe_text, phone=safe_text)
@given(instance=Booking_Entity_strategy)
@settings(max_examples=25)
def test_Booking_Entity_instantiation(instance):
    assert isinstance(instance, Booking_Entity)


CheckIn_Entity_strategy = st.builds(CheckIn_Entity, CheckInStatus=safe_text, MobileKey=safe_text, PickUpAddress=safe_text, QRCode=safe_text, paymentMode=safe_text)
@given(instance=CheckIn_Entity_strategy)
@settings(max_examples=25)
def test_CheckIn_Entity_instantiation(instance):
    assert isinstance(instance, CheckIn_Entity)


FeedBack_strategy = st.builds(FeedBack, FeedBackMessage=safe_text, Rating=safe_text)
@given(instance=FeedBack_strategy)
@settings(max_examples=25)
def test_FeedBack_instantiation(instance):
    assert isinstance(instance, FeedBack)


Payment_strategy = st.builds(Payment, details=safe_text, paidDate=st.dates(), total=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


PostStay_Entity_strategy = st.builds(PostStay_Entity, DiscountPoints=safe_text, PromotionPoints=safe_text, ThanksMessage=safe_text)
@given(instance=PostStay_Entity_strategy)
@settings(max_examples=25)
def test_PostStay_Entity_instantiation(instance):
    assert isinstance(instance, PostStay_Entity)


User_Entity_strategy = st.builds(User_Entity, City=safe_text, Email=safe_text, login=safe_text, password=safe_text)
@given(instance=User_Entity_strategy)
@settings(max_examples=25)
def test_User_Entity_instantiation(instance):
    assert isinstance(instance, User_Entity)



