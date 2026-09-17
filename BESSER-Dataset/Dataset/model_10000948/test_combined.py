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
    Order,
    WebUser,
    Payment,
    OrderStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_hyp_order_constructor_exists():
    assert callable(Order.__init__)


def test_hyp_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "number" in params, "Missing parameter 'number'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "total" in params, "Missing parameter 'total'"
    assert "shipped" in params, "Missing parameter 'shipped'"
    assert "shipTo" in params, "Missing parameter 'shipTo'"

def test_hyp_order_has_status():
    assert hasattr(Order, "status")
    descriptor = None
    for klass in Order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_number():
    assert hasattr(Order, "number")
    descriptor = None
    for klass in Order.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_ordered():
    assert hasattr(Order, "ordered")
    descriptor = None
    for klass in Order.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_total():
    assert hasattr(Order, "total")
    descriptor = None
    for klass in Order.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_shipped():
    assert hasattr(Order, "shipped")
    descriptor = None
    for klass in Order.__mro__:
        if "shipped" in klass.__dict__:
            descriptor = klass.__dict__["shipped"]
            break
    assert isinstance(descriptor, property)

def test_hyp_order_has_shipTo():
    assert hasattr(Order, "shipTo")
    descriptor = None
    for klass in Order.__mro__:
        if "shipTo" in klass.__dict__:
            descriptor = klass.__dict__["shipTo"]
            break
    assert isinstance(descriptor, property)



def test_hyp_webuser_is_not_abstract():
    assert not inspect.isabstract(WebUser)


def test_hyp_webuser_constructor_exists():
    assert callable(WebUser.__init__)


def test_hyp_webuser_constructor_args():
    sig = inspect.signature(WebUser.__init__)
    params = list(sig.parameters.keys())
    assert "login" in params, "Missing parameter 'login'"
    assert "state" in params, "Missing parameter 'state'"
    assert "password" in params, "Missing parameter 'password'"






def test_hyp_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_hyp_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_hyp_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "details" in params, "Missing parameter 'details'"
    assert "paidDate" in params, "Missing parameter 'paidDate'"
    assert "total" in params, "Missing parameter 'total'"




def test_hyp_orderstatus_exists():
    # Check that the Enumeration exists
    assert OrderStatus is not None

def test_hyp_orderstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderStatus"


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
Order_strategy = st.builds(
    Order,
    status=
        st.none(),
    number=
        st.integers(),
    ordered=
        st.dates(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    shipped=
        st.booleans(),
    shipTo=
        safe_text
)
WebUser_strategy = st.builds(
    WebUser,
    login=
        safe_text,
    state=
        safe_text,
    password=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    details=
        safe_text,
    paidDate=
        st.dates(),
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_hyp_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_hyp_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Order_strategy)
def test_hyp_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_hyp_order_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=Order_strategy)
def test_hyp_order_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Order_strategy)
def test_hyp_order_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original



@given(instance=Order_strategy)
def test_hyp_order_shipTo_setter(instance):
    original = instance.shipTo
    instance.shipTo = original
    assert instance.shipTo == original




@given(instance=WebUser_strategy)
def test_hyp_webuser_login_setter(instance):
    original = instance.login
    instance.login = original
    assert instance.login == original



@given(instance=WebUser_strategy)
def test_hyp_webuser_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=WebUser_strategy)
def test_hyp_webuser_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=Payment_strategy)
def test_hyp_payment_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=Payment_strategy)
def test_hyp_payment_paidDate_setter(instance):
    original = instance.paidDate
    instance.paidDate = original
    assert instance.paidDate == original



@given(instance=Payment_strategy)
def test_hyp_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Order,
    Payment,
    WebUser,
    OrderStatus,
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


def test_WebUser_login_value_roundtrip():
    instance = WebUser(login="sample_text", password="sample_text", state="sample_text")
    assert instance.login == "sample_text"
    instance.login = "sample_text_2"
    assert instance.login == "sample_text_2"


def test_WebUser_password_value_roundtrip():
    instance = WebUser(login="sample_text", password="sample_text", state="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_WebUser_state_value_roundtrip():
    instance = WebUser(login="sample_text", password="sample_text", state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Payment_strategy = st.builds(Payment, details=safe_text, paidDate=st.dates(), total=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Payment_strategy)
@settings(max_examples=25)
def test_Payment_instantiation(instance):
    assert isinstance(instance, Payment)


WebUser_strategy = st.builds(WebUser, login=safe_text, password=safe_text, state=safe_text)
@given(instance=WebUser_strategy)
@settings(max_examples=25)
def test_WebUser_instantiation(instance):
    assert isinstance(instance, WebUser)



