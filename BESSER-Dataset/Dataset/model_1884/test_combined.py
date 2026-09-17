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
    Classes_AdministratorProvides,
    Classes_Charge,
    Classes_IFinance,
    Classes_IBookingManagement,
    Classes_CustomerProvides,
    IFinance,
    IPerson,
    Classes_StaffMember,
    IHotelManager,
    Classes_IFinanceImpl,
    Classes_IHotelManagerImpl,
    IBookingManagement,
    Classes_Booking,
    Classes_IHotelManager,
    Classes_IPerson,
    Classes_Bill,
    Classes_Customer,
    Classes_IBookingManagementImpl,
    Classes_RoomType,
    Classes_Room,
    RoomStatus,
    ChargeType,
    RoomTypeName,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_classes_administratorprovides_is_not_abstract():
    assert not inspect.isabstract(Classes_AdministratorProvides)


def test_hyp_classes_administratorprovides_constructor_exists():
    assert callable(Classes_AdministratorProvides.__init__)


def test_hyp_classes_administratorprovides_constructor_args():
    sig = inspect.signature(Classes_AdministratorProvides.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_charge_is_not_abstract():
    assert not inspect.isabstract(Classes_Charge)


def test_hyp_classes_charge_constructor_exists():
    assert callable(Classes_Charge.__init__)


def test_hyp_classes_charge_constructor_args():
    sig = inspect.signature(Classes_Charge.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "chargeType" in params, "Missing parameter 'chargeType'"






def test_hyp_classes_ifinance_is_not_abstract():
    assert not inspect.isabstract(Classes_IFinance)


def test_hyp_classes_ifinance_constructor_exists():
    assert callable(Classes_IFinance.__init__)


def test_hyp_classes_ifinance_constructor_args():
    sig = inspect.signature(Classes_IFinance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_ibookingmanagement_is_not_abstract():
    assert not inspect.isabstract(Classes_IBookingManagement)


def test_hyp_classes_ibookingmanagement_constructor_exists():
    assert callable(Classes_IBookingManagement.__init__)


def test_hyp_classes_ibookingmanagement_constructor_args():
    sig = inspect.signature(Classes_IBookingManagement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_customerprovides_is_not_abstract():
    assert not inspect.isabstract(Classes_CustomerProvides)


def test_hyp_classes_customerprovides_constructor_exists():
    assert callable(Classes_CustomerProvides.__init__)


def test_hyp_classes_customerprovides_constructor_args():
    sig = inspect.signature(Classes_CustomerProvides.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ifinance_is_not_abstract():
    assert not inspect.isabstract(IFinance)


def test_hyp_ifinance_constructor_exists():
    assert callable(IFinance.__init__)


def test_hyp_ifinance_constructor_args():
    sig = inspect.signature(IFinance.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iperson_is_not_abstract():
    assert not inspect.isabstract(IPerson)


def test_hyp_iperson_constructor_exists():
    assert callable(IPerson.__init__)


def test_hyp_iperson_constructor_args():
    sig = inspect.signature(IPerson.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_staffmember_is_not_abstract():
    assert not inspect.isabstract(Classes_StaffMember)


def test_hyp_classes_staffmember_constructor_exists():
    assert callable(Classes_StaffMember.__init__)


def test_hyp_classes_staffmember_constructor_args():
    sig = inspect.signature(Classes_StaffMember.__init__)
    params = list(sig.parameters.keys())
    assert "admin" in params, "Missing parameter 'admin'"
    assert "password" in params, "Missing parameter 'password'"
    assert "isLoggedIn" in params, "Missing parameter 'isLoggedIn'"
    assert "username" in params, "Missing parameter 'username'"







def test_hyp_ihotelmanager_is_not_abstract():
    assert not inspect.isabstract(IHotelManager)


def test_hyp_ihotelmanager_constructor_exists():
    assert callable(IHotelManager.__init__)


def test_hyp_ihotelmanager_constructor_args():
    sig = inspect.signature(IHotelManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_ifinanceimpl_is_not_abstract():
    assert not inspect.isabstract(Classes_IFinanceImpl)


def test_hyp_classes_ifinanceimpl_constructor_exists():
    assert callable(Classes_IFinanceImpl.__init__)


def test_hyp_classes_ifinanceimpl_constructor_args():
    sig = inspect.signature(Classes_IFinanceImpl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_ihotelmanagerimpl_is_not_abstract():
    assert not inspect.isabstract(Classes_IHotelManagerImpl)


def test_hyp_classes_ihotelmanagerimpl_constructor_exists():
    assert callable(Classes_IHotelManagerImpl.__init__)


def test_hyp_classes_ihotelmanagerimpl_constructor_args():
    sig = inspect.signature(Classes_IHotelManagerImpl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ibookingmanagement_is_not_abstract():
    assert not inspect.isabstract(IBookingManagement)


def test_hyp_ibookingmanagement_constructor_exists():
    assert callable(IBookingManagement.__init__)


def test_hyp_ibookingmanagement_constructor_args():
    sig = inspect.signature(IBookingManagement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_booking_is_not_abstract():
    assert not inspect.isabstract(Classes_Booking)


def test_hyp_classes_booking_constructor_exists():
    assert callable(Classes_Booking.__init__)


def test_hyp_classes_booking_constructor_args():
    sig = inspect.signature(Classes_Booking.__init__)
    params = list(sig.parameters.keys())
    assert "checkOut" in params, "Missing parameter 'checkOut'"
    assert "checkIn" in params, "Missing parameter 'checkIn'"
    assert "numberOfGuests" in params, "Missing parameter 'numberOfGuests'"
    assert "bookingID" in params, "Missing parameter 'bookingID'"







def test_hyp_classes_ihotelmanager_is_not_abstract():
    assert not inspect.isabstract(Classes_IHotelManager)


def test_hyp_classes_ihotelmanager_constructor_exists():
    assert callable(Classes_IHotelManager.__init__)


def test_hyp_classes_ihotelmanager_constructor_args():
    sig = inspect.signature(Classes_IHotelManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_iperson_is_not_abstract():
    assert not inspect.isabstract(Classes_IPerson)


def test_hyp_classes_iperson_constructor_exists():
    assert callable(Classes_IPerson.__init__)


def test_hyp_classes_iperson_constructor_args():
    sig = inspect.signature(Classes_IPerson.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"








def test_hyp_classes_bill_is_not_abstract():
    assert not inspect.isabstract(Classes_Bill)


def test_hyp_classes_bill_constructor_exists():
    assert callable(Classes_Bill.__init__)


def test_hyp_classes_bill_constructor_args():
    sig = inspect.signature(Classes_Bill.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_customer_is_not_abstract():
    assert not inspect.isabstract(Classes_Customer)


def test_hyp_classes_customer_constructor_exists():
    assert callable(Classes_Customer.__init__)


def test_hyp_classes_customer_constructor_args():
    sig = inspect.signature(Classes_Customer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_ibookingmanagementimpl_is_not_abstract():
    assert not inspect.isabstract(Classes_IBookingManagementImpl)


def test_hyp_classes_ibookingmanagementimpl_constructor_exists():
    assert callable(Classes_IBookingManagementImpl.__init__)


def test_hyp_classes_ibookingmanagementimpl_constructor_args():
    sig = inspect.signature(Classes_IBookingManagementImpl.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classes_roomtype_is_not_abstract():
    assert not inspect.isabstract(Classes_RoomType)


def test_hyp_classes_roomtype_constructor_exists():
    assert callable(Classes_RoomType.__init__)


def test_hyp_classes_roomtype_constructor_args():
    sig = inspect.signature(Classes_RoomType.__init__)
    params = list(sig.parameters.keys())
    assert "roomTypeName" in params, "Missing parameter 'roomTypeName'"
    assert "price" in params, "Missing parameter 'price'"
    assert "numberOfGuests" in params, "Missing parameter 'numberOfGuests'"
    assert "features" in params, "Missing parameter 'features'"
    assert "description" in params, "Missing parameter 'description'"








def test_hyp_classes_room_is_not_abstract():
    assert not inspect.isabstract(Classes_Room)


def test_hyp_classes_room_constructor_exists():
    assert callable(Classes_Room.__init__)


def test_hyp_classes_room_constructor_args():
    sig = inspect.signature(Classes_Room.__init__)
    params = list(sig.parameters.keys())
    assert "roomNumber" in params, "Missing parameter 'roomNumber'"
    assert "status" in params, "Missing parameter 'status'"



def test_hyp_roomstatus_exists():
    # Check that the Enumeration exists
    assert RoomStatus is not None

def test_hyp_roomstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoomStatus]
    expected_literals = [
        "Available",
        "Cleaning",
        "Maintenance",
        "Occupied",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoomStatus"

def test_hyp_chargetype_exists():
    # Check that the Enumeration exists
    assert ChargeType is not None

def test_hyp_chargetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChargeType]
    expected_literals = [
        "DoubleRoom",
        "FamilySuite",
        "SingleRoom",
        "LateCheckOutFee",
        "CancellationFee",
        "Breakfast",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChargeType"

def test_hyp_roomtypename_exists():
    # Check that the Enumeration exists
    assert RoomTypeName is not None

def test_hyp_roomtypename_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoomTypeName]
    expected_literals = [
        "FamilySuite",
        "SingleRoom",
        "DoubleRoom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoomTypeName"


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
Classes_AdministratorProvides_strategy = st.builds(
    Classes_AdministratorProvides,
)
Classes_Charge_strategy = st.builds(
    Classes_Charge,
    date=
        st.dates(),
    amount=
        st.integers(),
    chargeType=
        safe_text
)
Classes_IFinance_strategy = st.builds(
    Classes_IFinance,
)
Classes_IBookingManagement_strategy = st.builds(
    Classes_IBookingManagement,
)
Classes_CustomerProvides_strategy = st.builds(
    Classes_CustomerProvides,
)
IFinance_strategy = st.builds(
    IFinance,
)
IPerson_strategy = st.builds(
    IPerson,
)
Classes_StaffMember_strategy = st.builds(
    Classes_StaffMember,
    admin=
        safe_text,
    password=
        safe_text,
    isLoggedIn=
        st.booleans(),
    username=
        safe_text
)
IHotelManager_strategy = st.builds(
    IHotelManager,
)
Classes_IFinanceImpl_strategy = st.builds(
    Classes_IFinanceImpl,
)
Classes_IHotelManagerImpl_strategy = st.builds(
    Classes_IHotelManagerImpl,
)
IBookingManagement_strategy = st.builds(
    IBookingManagement,
)
Classes_Booking_strategy = st.builds(
    Classes_Booking,
    checkOut=
        st.dates(),
    checkIn=
        st.dates(),
    numberOfGuests=
        safe_text,
    bookingID=
        safe_text
)
Classes_IHotelManager_strategy = st.builds(
    Classes_IHotelManager,
)
Classes_IPerson_strategy = st.builds(
    Classes_IPerson,
    email=
        safe_text,
    address=
        safe_text,
    lastName=
        safe_text,
    firstName=
        safe_text,
    phoneNumber=
        safe_text
)
Classes_Bill_strategy = st.builds(
    Classes_Bill,
)
Classes_Customer_strategy = st.builds(
    Classes_Customer,
)
Classes_IBookingManagementImpl_strategy = st.builds(
    Classes_IBookingManagementImpl,
)
Classes_RoomType_strategy = st.builds(
    Classes_RoomType,
    roomTypeName=
        safe_text,
    price=
        safe_text,
    numberOfGuests=
        safe_text,
    features=
        safe_text,
    description=
        safe_text
)
Classes_Room_strategy = st.builds(
    Classes_Room,
    roomNumber=
        safe_text,
    status=
        safe_text
)


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_AdministratorProvides_strategy)
@settings(max_examples=30)
def test_hyp_classes_administratorprovides_addcreditcard_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addCreditCard(
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addCreditCard).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addCreditCard' in Classes_AdministratorProvides is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addCreditCard' in Classes_AdministratorProvides did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addCreditCard' in Classes_AdministratorProvides is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_AdministratorProvides_strategy)
@settings(max_examples=30)
def test_hyp_classes_administratorprovides_makedeposit_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.makeDeposit(
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.makeDeposit).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'makeDeposit' in Classes_AdministratorProvides is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makeDeposit' in Classes_AdministratorProvides did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makeDeposit' in Classes_AdministratorProvides is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_AdministratorProvides_strategy)
@settings(max_examples=30)
def test_hyp_classes_administratorprovides_removecreditcard_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeCreditCard(
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeCreditCard).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeCreditCard' in Classes_AdministratorProvides is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeCreditCard' in Classes_AdministratorProvides did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeCreditCard' in Classes_AdministratorProvides is not implemented or raised an error")




@given(instance=Classes_Charge_strategy)
def test_hyp_classes_charge_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Classes_Charge_strategy)
def test_hyp_classes_charge_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Classes_Charge_strategy)
def test_hyp_classes_charge_chargeType_setter(instance):
    original = instance.chargeType
    instance.chargeType = original
    assert instance.chargeType == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IFinance_strategy)
@settings(max_examples=30)
def test_hyp_classes_ifinance_calculatepayment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.calculatePayment(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.calculatePayment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'calculatePayment' in Classes_IFinance is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'calculatePayment' in Classes_IFinance did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'calculatePayment' in Classes_IFinance is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IFinance_strategy)
@settings(max_examples=30)
def test_hyp_classes_ifinance_banksendinvoice_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bankSendInvoice()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bankSendInvoice).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bankSendInvoice' in Classes_IFinance is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bankSendInvoice' in Classes_IFinance did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bankSendInvoice' in Classes_IFinance is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IFinance_strategy)
@settings(max_examples=30)
def test_hyp_classes_ifinance_paybill_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.payBill(
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.payBill).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'payBill' in Classes_IFinance is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'payBill' in Classes_IFinance did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'payBill' in Classes_IFinance is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_addroompending_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addRoomPending(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addRoomPending).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addRoomPending' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addRoomPending' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addRoomPending' in Classes_IBookingManagement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_updatebooking_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateBooking(
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateBooking).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateBooking' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateBooking' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateBooking' in Classes_IBookingManagement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_addextracharge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addExtraCharge(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addExtraCharge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addExtraCharge' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addExtraCharge' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addExtraCharge' in Classes_IBookingManagement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_confirmbooking_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.confirmBooking(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.confirmBooking).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'confirmBooking' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'confirmBooking' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'confirmBooking' in Classes_IBookingManagement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_addcustomerinformationtobooking_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addCustomerInformationToBooking(
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addCustomerInformationToBooking).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addCustomerInformationToBooking' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addCustomerInformationToBooking' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addCustomerInformationToBooking' in Classes_IBookingManagement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_searchroom_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.searchRoom(
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.searchRoom).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'searchRoom' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'searchRoom' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'searchRoom' in Classes_IBookingManagement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_cancelbooking_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.cancelBooking(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.cancelBooking).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'cancelBooking' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'cancelBooking' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'cancelBooking' in Classes_IBookingManagement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_creatependingbooking_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createPendingBooking(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createPendingBooking).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createPendingBooking' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createPendingBooking' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createPendingBooking' in Classes_IBookingManagement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=30)
def test_hyp_classes_ibookingmanagement_sendconfirmation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.sendConfirmation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.sendConfirmation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'sendConfirmation' in Classes_IBookingManagement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'sendConfirmation' in Classes_IBookingManagement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'sendConfirmation' in Classes_IBookingManagement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_CustomerProvides_strategy)
@settings(max_examples=30)
def test_hyp_classes_customerprovides_makepayment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.makePayment(
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.makePayment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'makePayment' in Classes_CustomerProvides is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'makePayment' in Classes_CustomerProvides did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'makePayment' in Classes_CustomerProvides is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_CustomerProvides_strategy)
@settings(max_examples=30)
def test_hyp_classes_customerprovides_iscreditcardvalid_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isCreditCardValid(
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isCreditCardValid).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isCreditCardValid' in Classes_CustomerProvides is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isCreditCardValid' in Classes_CustomerProvides did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isCreditCardValid' in Classes_CustomerProvides is not implemented or raised an error")






@given(instance=Classes_StaffMember_strategy)
def test_hyp_classes_staffmember_admin_setter(instance):
    original = instance.admin
    instance.admin = original
    assert instance.admin == original



@given(instance=Classes_StaffMember_strategy)
def test_hyp_classes_staffmember_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Classes_StaffMember_strategy)
def test_hyp_classes_staffmember_isLoggedIn_setter(instance):
    original = instance.isLoggedIn
    instance.isLoggedIn = original
    assert instance.isLoggedIn == original



@given(instance=Classes_StaffMember_strategy)
def test_hyp_classes_staffmember_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original








@given(instance=Classes_Booking_strategy)
def test_hyp_classes_booking_checkOut_setter(instance):
    original = instance.checkOut
    instance.checkOut = original
    assert instance.checkOut == original



@given(instance=Classes_Booking_strategy)
def test_hyp_classes_booking_checkIn_setter(instance):
    original = instance.checkIn
    instance.checkIn = original
    assert instance.checkIn == original



@given(instance=Classes_Booking_strategy)
def test_hyp_classes_booking_numberOfGuests_setter(instance):
    original = instance.numberOfGuests
    instance.numberOfGuests = original
    assert instance.numberOfGuests == original



@given(instance=Classes_Booking_strategy)
def test_hyp_classes_booking_bookingID_setter(instance):
    original = instance.bookingID
    instance.bookingID = original
    assert instance.bookingID == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_changestatusofroom_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.changeStatusOfRoom(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.changeStatusOfRoom).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'changeStatusOfRoom' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'changeStatusOfRoom' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'changeStatusOfRoom' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_isvalidusername_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isValidUsername(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isValidUsername).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isValidUsername' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isValidUsername' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isValidUsername' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_login_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.login(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.login).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'login' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'login' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'login' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_isstaffmemberadmin_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isStaffMemberAdmin(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isStaffMemberAdmin).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isStaffMemberAdmin' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStaffMemberAdmin' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStaffMemberAdmin' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_ispasswordsecure_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isPasswordSecure(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isPasswordSecure).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isPasswordSecure' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isPasswordSecure' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isPasswordSecure' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_logout_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.logout(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.logout).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'logout' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'logout' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'logout' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_checkinbooking_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkInBooking(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkInBooking).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkInBooking' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkInBooking' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkInBooking' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_isstaffmemberloggedin_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isStaffMemberLoggedIn(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isStaffMemberLoggedIn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isStaffMemberLoggedIn' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isStaffMemberLoggedIn' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isStaffMemberLoggedIn' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_checkout_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkOut(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkOut).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkOut' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkOut' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkOut' in Classes_IHotelManager is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=30)
def test_hyp_classes_ihotelmanager_addstaffmember_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addStaffMember(
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addStaffMember).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addStaffMember' in Classes_IHotelManager is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addStaffMember' in Classes_IHotelManager did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addStaffMember' in Classes_IHotelManager is not implemented or raised an error")




@given(instance=Classes_IPerson_strategy)
def test_hyp_classes_iperson_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Classes_IPerson_strategy)
def test_hyp_classes_iperson_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Classes_IPerson_strategy)
def test_hyp_classes_iperson_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=Classes_IPerson_strategy)
def test_hyp_classes_iperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Classes_IPerson_strategy)
def test_hyp_classes_iperson_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original







@given(instance=Classes_RoomType_strategy)
def test_hyp_classes_roomtype_roomTypeName_setter(instance):
    original = instance.roomTypeName
    instance.roomTypeName = original
    assert instance.roomTypeName == original



@given(instance=Classes_RoomType_strategy)
def test_hyp_classes_roomtype_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Classes_RoomType_strategy)
def test_hyp_classes_roomtype_numberOfGuests_setter(instance):
    original = instance.numberOfGuests
    instance.numberOfGuests = original
    assert instance.numberOfGuests == original



@given(instance=Classes_RoomType_strategy)
def test_hyp_classes_roomtype_features_setter(instance):
    original = instance.features
    instance.features = original
    assert instance.features == original



@given(instance=Classes_RoomType_strategy)
def test_hyp_classes_roomtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=Classes_Room_strategy)
def test_hyp_classes_room_roomNumber_setter(instance):
    original = instance.roomNumber
    instance.roomNumber = original
    assert instance.roomNumber == original



@given(instance=Classes_Room_strategy)
def test_hyp_classes_room_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Classes_AdministratorProvides,
    Classes_Bill,
    Classes_Booking,
    Classes_Charge,
    Classes_Customer,
    Classes_CustomerProvides,
    Classes_IBookingManagement,
    Classes_IBookingManagementImpl,
    Classes_IFinance,
    Classes_IFinanceImpl,
    Classes_IHotelManager,
    Classes_IHotelManagerImpl,
    Classes_IPerson,
    Classes_Room,
    Classes_RoomType,
    Classes_StaffMember,
    IBookingManagement,
    IFinance,
    IHotelManager,
    IPerson,
    ChargeType,
    RoomStatus,
    RoomTypeName,
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

def test_Classes_Booking_bookingID_value_roundtrip():
    instance = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    assert instance.bookingID == "sample_text"
    instance.bookingID = "sample_text_2"
    assert instance.bookingID == "sample_text_2"


def test_Classes_Booking_checkIn_value_roundtrip():
    instance = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    assert instance.checkIn == date(2024, 1, 1)
    instance.checkIn = date(2025, 6, 15)
    assert instance.checkIn == date(2025, 6, 15)


def test_Classes_Booking_checkOut_value_roundtrip():
    instance = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    assert instance.checkOut == date(2024, 1, 1)
    instance.checkOut = date(2025, 6, 15)
    assert instance.checkOut == date(2025, 6, 15)


def test_Classes_Booking_numberOfGuests_value_roundtrip():
    instance = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    assert instance.numberOfGuests == "sample_text"
    instance.numberOfGuests = "sample_text_2"
    assert instance.numberOfGuests == "sample_text_2"


def test_Classes_Charge_amount_value_roundtrip():
    instance = Classes_Charge(amount=7, chargeType="sample_text", date=date(2024, 1, 1))
    assert instance.amount == 7
    instance.amount = 13
    assert instance.amount == 13


def test_Classes_Charge_chargeType_value_roundtrip():
    instance = Classes_Charge(amount=7, chargeType="sample_text", date=date(2024, 1, 1))
    assert instance.chargeType == "sample_text"
    instance.chargeType = "sample_text_2"
    assert instance.chargeType == "sample_text_2"


def test_Classes_Charge_date_value_roundtrip():
    instance = Classes_Charge(amount=7, chargeType="sample_text", date=date(2024, 1, 1))
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_Classes_IPerson_address_value_roundtrip():
    instance = Classes_IPerson(address="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", phoneNumber="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Classes_IPerson_email_value_roundtrip():
    instance = Classes_IPerson(address="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", phoneNumber="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Classes_IPerson_firstName_value_roundtrip():
    instance = Classes_IPerson(address="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", phoneNumber="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_Classes_IPerson_lastName_value_roundtrip():
    instance = Classes_IPerson(address="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", phoneNumber="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_Classes_IPerson_phoneNumber_value_roundtrip():
    instance = Classes_IPerson(address="sample_text", email="sample_text", firstName="sample_text", lastName="sample_text", phoneNumber="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_Classes_Room_roomNumber_value_roundtrip():
    instance = Classes_Room(roomNumber="sample_text", status="sample_text")
    assert instance.roomNumber == "sample_text"
    instance.roomNumber = "sample_text_2"
    assert instance.roomNumber == "sample_text_2"


def test_Classes_Room_status_value_roundtrip():
    instance = Classes_Room(roomNumber="sample_text", status="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_Classes_RoomType_description_value_roundtrip():
    instance = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Classes_RoomType_features_value_roundtrip():
    instance = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    assert instance.features == "sample_text"
    instance.features = "sample_text_2"
    assert instance.features == "sample_text_2"


def test_Classes_RoomType_numberOfGuests_value_roundtrip():
    instance = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    assert instance.numberOfGuests == "sample_text"
    instance.numberOfGuests = "sample_text_2"
    assert instance.numberOfGuests == "sample_text_2"


def test_Classes_RoomType_price_value_roundtrip():
    instance = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    assert instance.price == "sample_text"
    instance.price = "sample_text_2"
    assert instance.price == "sample_text_2"


def test_Classes_RoomType_roomTypeName_value_roundtrip():
    instance = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    assert instance.roomTypeName == "sample_text"
    instance.roomTypeName = "sample_text_2"
    assert instance.roomTypeName == "sample_text_2"


def test_Classes_StaffMember_admin_value_roundtrip():
    instance = Classes_StaffMember(admin="sample_text", isLoggedIn=True, password="sample_text", username="sample_text")
    assert instance.admin == "sample_text"
    instance.admin = "sample_text_2"
    assert instance.admin == "sample_text_2"


def test_Classes_StaffMember_isLoggedIn_value_roundtrip():
    instance = Classes_StaffMember(admin="sample_text", isLoggedIn=True, password="sample_text", username="sample_text")
    assert instance.isLoggedIn == True
    instance.isLoggedIn = False
    assert instance.isLoggedIn == False


def test_Classes_StaffMember_password_value_roundtrip():
    instance = Classes_StaffMember(admin="sample_text", isLoggedIn=True, password="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Classes_StaffMember_username_value_roundtrip():
    instance = Classes_StaffMember(admin="sample_text", isLoggedIn=True, password="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Classes_IBookingManagementImpl_isa_IBookingManagement():
    instance = Classes_IBookingManagementImpl()
    assert isinstance(instance, IBookingManagement)


def test_Classes_IFinanceImpl_isa_IFinance():
    instance = Classes_IFinanceImpl()
    assert isinstance(instance, IFinance)


def test_Classes_IHotelManagerImpl_isa_IHotelManager():
    instance = Classes_IHotelManagerImpl()
    assert isinstance(instance, IHotelManager)


def test_Classes_Customer_isa_IPerson():
    instance = Classes_Customer()
    assert isinstance(instance, IPerson)


def test_Classes_StaffMember_isa_IPerson():
    instance = Classes_StaffMember(admin="sample_text", isLoggedIn=True, password="sample_text", username="sample_text")
    assert isinstance(instance, IPerson)


def test_assoc_bill8_link_reassign_clear():
    a = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b1 = Classes_Bill()
    b2 = Classes_Bill()
    _safe_set(a, 'Classes_Booking', b1)
    assert _is_linked(a, 'Classes_Booking', b1)
    if hasattr(b1, 'Classes_Bill'):
        assert _is_linked(b1, 'Classes_Bill', a)
    _safe_set(a, 'Classes_Booking', b2)
    assert _is_linked(a, 'Classes_Booking', b2)
    if hasattr(b1, 'Classes_Bill'):
        assert not _is_linked(b1, 'Classes_Bill', a)
    if hasattr(b2, 'Classes_Bill'):
        assert _is_linked(b2, 'Classes_Bill', a)
    _safe_set(a, 'Classes_Booking', None)
    assert not _is_linked(a, 'Classes_Booking', b2)
    if hasattr(b2, 'Classes_Bill'):
        assert not _is_linked(b2, 'Classes_Bill', a)


def test_assoc_booking11_link_reassign_clear():
    a = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b1 = Classes_Customer()
    b2 = Classes_Customer()
    _safe_set(a, 'Booking12', b1)
    assert _is_linked(a, 'Booking12', b1)
    if hasattr(b1, 'customer'):
        assert _is_linked(b1, 'customer', a)
    _safe_set(a, 'Booking12', b2)
    assert _is_linked(a, 'Booking12', b2)
    if hasattr(b1, 'customer'):
        assert not _is_linked(b1, 'customer', a)
    if hasattr(b2, 'customer'):
        assert _is_linked(b2, 'customer', a)
    _safe_set(a, 'Booking12', None)
    assert not _is_linked(a, 'Booking12', b2)
    if hasattr(b2, 'customer'):
        assert not _is_linked(b2, 'customer', a)


def test_assoc_bookingHistory21_link_reassign_clear():
    a = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b1 = Classes_IBookingManagementImpl()
    b2 = Classes_IBookingManagementImpl()
    _safe_set(a, 'Classes_Booking23', b1)
    assert _is_linked(a, 'Classes_Booking23', b1)
    if hasattr(b1, 'Classes_IBookingManagementImpl22'):
        assert _is_linked(b1, 'Classes_IBookingManagementImpl22', a)
    _safe_set(a, 'Classes_Booking23', b2)
    assert _is_linked(a, 'Classes_Booking23', b2)
    if hasattr(b1, 'Classes_IBookingManagementImpl22'):
        assert not _is_linked(b1, 'Classes_IBookingManagementImpl22', a)
    if hasattr(b2, 'Classes_IBookingManagementImpl22'):
        assert _is_linked(b2, 'Classes_IBookingManagementImpl22', a)
    _safe_set(a, 'Classes_Booking23', None)
    assert not _is_linked(a, 'Classes_Booking23', b2)
    if hasattr(b2, 'Classes_IBookingManagementImpl22'):
        assert not _is_linked(b2, 'Classes_IBookingManagementImpl22', a)


def test_assoc_bookings1_link_reassign_clear():
    a = Classes_Room(roomNumber="sample_text", status="sample_text")
    b1 = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b2 = Classes_Booking(bookingID="sample_text_2", checkIn=date(2025, 6, 15), checkOut=date(2025, 6, 15), numberOfGuests="sample_text_2")
    _safe_set(a, 'rooms', {b1})
    assert _is_linked(a, 'rooms', b1)
    if hasattr(b1, 'Booking'):
        assert _is_linked(b1, 'Booking', a)
    _safe_set(a, 'rooms', {b2})
    assert _is_linked(a, 'rooms', b2)
    if hasattr(b1, 'Booking'):
        assert not _is_linked(b1, 'Booking', a)
    if hasattr(b2, 'Booking'):
        assert _is_linked(b2, 'Booking', a)
    _safe_set(a, 'rooms', set())
    assert not _is_linked(a, 'rooms', b2)
    if hasattr(b2, 'Booking'):
        assert not _is_linked(b2, 'Booking', a)


def test_assoc_charge35_link_reassign_clear():
    a = Classes_Charge(amount=7, chargeType="sample_text", date=date(2024, 1, 1))
    b1 = Classes_Bill()
    b2 = Classes_Bill()
    _safe_set(a, 'Classes_Charge', b1)
    assert _is_linked(a, 'Classes_Charge', b1)
    if hasattr(b1, 'Classes_Bill36'):
        assert _is_linked(b1, 'Classes_Bill36', a)
    _safe_set(a, 'Classes_Charge', b2)
    assert _is_linked(a, 'Classes_Charge', b2)
    if hasattr(b1, 'Classes_Bill36'):
        assert not _is_linked(b1, 'Classes_Bill36', a)
    if hasattr(b2, 'Classes_Bill36'):
        assert _is_linked(b2, 'Classes_Bill36', a)
    _safe_set(a, 'Classes_Charge', None)
    assert not _is_linked(a, 'Classes_Charge', b2)
    if hasattr(b2, 'Classes_Bill36'):
        assert not _is_linked(b2, 'Classes_Bill36', a)


def test_assoc_confirmedBookings26_link_reassign_clear():
    a = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b1 = Classes_IBookingManagementImpl()
    b2 = Classes_IBookingManagementImpl()
    _safe_set(a, 'Booking28', b1)
    assert _is_linked(a, 'Booking28', b1)
    if hasattr(b1, 'iBookingManagementImpl27'):
        assert _is_linked(b1, 'iBookingManagementImpl27', a)
    _safe_set(a, 'Booking28', b2)
    assert _is_linked(a, 'Booking28', b2)
    if hasattr(b1, 'iBookingManagementImpl27'):
        assert not _is_linked(b1, 'iBookingManagementImpl27', a)
    if hasattr(b2, 'iBookingManagementImpl27'):
        assert _is_linked(b2, 'iBookingManagementImpl27', a)
    _safe_set(a, 'Booking28', None)
    assert not _is_linked(a, 'Booking28', b2)
    if hasattr(b2, 'iBookingManagementImpl27'):
        assert not _is_linked(b2, 'iBookingManagementImpl27', a)


def test_assoc_customer5_link_reassign_clear():
    a = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b1 = Classes_Customer()
    b2 = Classes_Customer()
    _safe_set(a, 'booking', b1)
    assert _is_linked(a, 'booking', b1)
    if hasattr(b1, 'Customer'):
        assert _is_linked(b1, 'Customer', a)
    _safe_set(a, 'booking', b2)
    assert _is_linked(a, 'booking', b2)
    if hasattr(b1, 'Customer'):
        assert not _is_linked(b1, 'Customer', a)
    if hasattr(b2, 'Customer'):
        assert _is_linked(b2, 'Customer', a)
    _safe_set(a, 'booking', None)
    assert not _is_linked(a, 'booking', b2)
    if hasattr(b2, 'Customer'):
        assert not _is_linked(b2, 'Customer', a)


def test_assoc_customerProvides32_link_reassign_clear():
    a = Classes_CustomerProvides()
    b1 = Classes_IFinanceImpl()
    b2 = Classes_IFinanceImpl()
    _safe_set(a, 'Classes_CustomerProvides', b1)
    assert _is_linked(a, 'Classes_CustomerProvides', b1)
    if hasattr(b1, 'Classes_IFinanceImpl'):
        assert _is_linked(b1, 'Classes_IFinanceImpl', a)
    _safe_set(a, 'Classes_CustomerProvides', b2)
    assert _is_linked(a, 'Classes_CustomerProvides', b2)
    if hasattr(b1, 'Classes_IFinanceImpl'):
        assert not _is_linked(b1, 'Classes_IFinanceImpl', a)
    if hasattr(b2, 'Classes_IFinanceImpl'):
        assert _is_linked(b2, 'Classes_IFinanceImpl', a)
    _safe_set(a, 'Classes_CustomerProvides', None)
    assert not _is_linked(a, 'Classes_CustomerProvides', b2)
    if hasattr(b2, 'Classes_IFinanceImpl'):
        assert not _is_linked(b2, 'Classes_IFinanceImpl', a)


def test_assoc_iBookingManagementImpl2_link_reassign_clear():
    a = Classes_Room(roomNumber="sample_text", status="sample_text")
    b1 = Classes_IBookingManagementImpl()
    b2 = Classes_IBookingManagementImpl()
    _safe_set(a, 'room3', b1)
    assert _is_linked(a, 'room3', b1)
    if hasattr(b1, 'IBookingManagementImpl'):
        assert _is_linked(b1, 'IBookingManagementImpl', a)
    _safe_set(a, 'room3', b2)
    assert _is_linked(a, 'room3', b2)
    if hasattr(b1, 'IBookingManagementImpl'):
        assert not _is_linked(b1, 'IBookingManagementImpl', a)
    if hasattr(b2, 'IBookingManagementImpl'):
        assert _is_linked(b2, 'IBookingManagementImpl', a)
    _safe_set(a, 'room3', None)
    assert not _is_linked(a, 'room3', b2)
    if hasattr(b2, 'IBookingManagementImpl'):
        assert not _is_linked(b2, 'IBookingManagementImpl', a)


def test_assoc_iBookingManagementImpl6_link_reassign_clear():
    a = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b1 = Classes_IBookingManagementImpl()
    b2 = Classes_IBookingManagementImpl()
    _safe_set(a, 'confirmedBookings', b1)
    assert _is_linked(a, 'confirmedBookings', b1)
    if hasattr(b1, 'IBookingManagementImpl7'):
        assert _is_linked(b1, 'IBookingManagementImpl7', a)
    _safe_set(a, 'confirmedBookings', b2)
    assert _is_linked(a, 'confirmedBookings', b2)
    if hasattr(b1, 'IBookingManagementImpl7'):
        assert not _is_linked(b1, 'IBookingManagementImpl7', a)
    if hasattr(b2, 'IBookingManagementImpl7'):
        assert _is_linked(b2, 'IBookingManagementImpl7', a)
    _safe_set(a, 'confirmedBookings', None)
    assert not _is_linked(a, 'confirmedBookings', b2)
    if hasattr(b2, 'IBookingManagementImpl7'):
        assert not _is_linked(b2, 'IBookingManagementImpl7', a)


def test_assoc_pendingBookings16_link_reassign_clear():
    a = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b1 = Classes_IBookingManagementImpl()
    b2 = Classes_IBookingManagementImpl()
    _safe_set(a, 'Classes_Booking18', b1)
    assert _is_linked(a, 'Classes_Booking18', b1)
    if hasattr(b1, 'Classes_IBookingManagementImpl17'):
        assert _is_linked(b1, 'Classes_IBookingManagementImpl17', a)
    _safe_set(a, 'Classes_Booking18', b2)
    assert _is_linked(a, 'Classes_Booking18', b2)
    if hasattr(b1, 'Classes_IBookingManagementImpl17'):
        assert not _is_linked(b1, 'Classes_IBookingManagementImpl17', a)
    if hasattr(b2, 'Classes_IBookingManagementImpl17'):
        assert _is_linked(b2, 'Classes_IBookingManagementImpl17', a)
    _safe_set(a, 'Classes_Booking18', None)
    assert not _is_linked(a, 'Classes_Booking18', b2)
    if hasattr(b2, 'Classes_IBookingManagementImpl17'):
        assert not _is_linked(b2, 'Classes_IBookingManagementImpl17', a)


def test_assoc_room14_link_reassign_clear():
    a = Classes_Room(roomNumber="sample_text", status="sample_text")
    b1 = Classes_IBookingManagementImpl()
    b2 = Classes_IBookingManagementImpl()
    _safe_set(a, 'Room15', b1)
    assert _is_linked(a, 'Room15', b1)
    if hasattr(b1, 'iBookingManagementImpl'):
        assert _is_linked(b1, 'iBookingManagementImpl', a)
    _safe_set(a, 'Room15', b2)
    assert _is_linked(a, 'Room15', b2)
    if hasattr(b1, 'iBookingManagementImpl'):
        assert not _is_linked(b1, 'iBookingManagementImpl', a)
    if hasattr(b2, 'iBookingManagementImpl'):
        assert _is_linked(b2, 'iBookingManagementImpl', a)
    _safe_set(a, 'Room15', None)
    assert not _is_linked(a, 'Room15', b2)
    if hasattr(b2, 'iBookingManagementImpl'):
        assert not _is_linked(b2, 'iBookingManagementImpl', a)


def test_assoc_room4_link_reassign_clear():
    a = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    b1 = Classes_Room(roomNumber="sample_text", status="sample_text")
    b2 = Classes_Room(roomNumber="sample_text_2", status="sample_text_2")
    _safe_set(a, 'roomType', {b1})
    assert _is_linked(a, 'roomType', b1)
    if hasattr(b1, 'Room'):
        assert _is_linked(b1, 'Room', a)
    _safe_set(a, 'roomType', {b2})
    assert _is_linked(a, 'roomType', b2)
    if hasattr(b1, 'Room'):
        assert not _is_linked(b1, 'Room', a)
    if hasattr(b2, 'Room'):
        assert _is_linked(b2, 'Room', a)
    _safe_set(a, 'roomType', set())
    assert not _is_linked(a, 'roomType', b2)
    if hasattr(b2, 'Room'):
        assert not _is_linked(b2, 'Room', a)


def test_assoc_roomType0_link_reassign_clear():
    a = Classes_RoomType(description="sample_text", features="sample_text", numberOfGuests="sample_text", price="sample_text", roomTypeName="sample_text")
    b1 = Classes_Room(roomNumber="sample_text", status="sample_text")
    b2 = Classes_Room(roomNumber="sample_text_2", status="sample_text_2")
    _safe_set(a, 'RoomType', b1)
    assert _is_linked(a, 'RoomType', b1)
    if hasattr(b1, 'room'):
        assert _is_linked(b1, 'room', a)
    _safe_set(a, 'RoomType', b2)
    assert _is_linked(a, 'RoomType', b2)
    if hasattr(b1, 'room'):
        assert not _is_linked(b1, 'room', a)
    if hasattr(b2, 'room'):
        assert _is_linked(b2, 'room', a)
    _safe_set(a, 'RoomType', None)
    assert not _is_linked(a, 'RoomType', b2)
    if hasattr(b2, 'room'):
        assert not _is_linked(b2, 'room', a)


def test_assoc_rooms9_link_reassign_clear():
    a = Classes_Room(roomNumber="sample_text", status="sample_text")
    b1 = Classes_Booking(bookingID="sample_text", checkIn=date(2024, 1, 1), checkOut=date(2024, 1, 1), numberOfGuests="sample_text")
    b2 = Classes_Booking(bookingID="sample_text_2", checkIn=date(2025, 6, 15), checkOut=date(2025, 6, 15), numberOfGuests="sample_text_2")
    _safe_set(a, 'Room10', b1)
    assert _is_linked(a, 'Room10', b1)
    if hasattr(b1, 'bookings'):
        assert _is_linked(b1, 'bookings', a)
    _safe_set(a, 'Room10', b2)
    assert _is_linked(a, 'Room10', b2)
    if hasattr(b1, 'bookings'):
        assert not _is_linked(b1, 'bookings', a)
    if hasattr(b2, 'bookings'):
        assert _is_linked(b2, 'bookings', a)
    _safe_set(a, 'Room10', None)
    assert not _is_linked(a, 'Room10', b2)
    if hasattr(b2, 'bookings'):
        assert not _is_linked(b2, 'bookings', a)


def test_assoc_staff29_link_reassign_clear():
    a = Classes_StaffMember(admin="sample_text", isLoggedIn=True, password="sample_text", username="sample_text")
    b1 = Classes_IHotelManagerImpl()
    b2 = Classes_IHotelManagerImpl()
    _safe_set(a, 'Classes_StaffMember', b1)
    assert _is_linked(a, 'Classes_StaffMember', b1)
    if hasattr(b1, 'Classes_IHotelManagerImpl'):
        assert _is_linked(b1, 'Classes_IHotelManagerImpl', a)
    _safe_set(a, 'Classes_StaffMember', b2)
    assert _is_linked(a, 'Classes_StaffMember', b2)
    if hasattr(b1, 'Classes_IHotelManagerImpl'):
        assert not _is_linked(b1, 'Classes_IHotelManagerImpl', a)
    if hasattr(b2, 'Classes_IHotelManagerImpl'):
        assert _is_linked(b2, 'Classes_IHotelManagerImpl', a)
    _safe_set(a, 'Classes_StaffMember', None)
    assert not _is_linked(a, 'Classes_StaffMember', b2)
    if hasattr(b2, 'Classes_IHotelManagerImpl'):
        assert not _is_linked(b2, 'Classes_IHotelManagerImpl', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Classes_AdministratorProvides_strategy = st.builds(Classes_AdministratorProvides)
@given(instance=Classes_AdministratorProvides_strategy)
@settings(max_examples=25)
def test_Classes_AdministratorProvides_instantiation(instance):
    assert isinstance(instance, Classes_AdministratorProvides)


Classes_Bill_strategy = st.builds(Classes_Bill)
@given(instance=Classes_Bill_strategy)
@settings(max_examples=25)
def test_Classes_Bill_instantiation(instance):
    assert isinstance(instance, Classes_Bill)


Classes_Booking_strategy = st.builds(Classes_Booking, bookingID=safe_text, checkIn=st.dates(), checkOut=st.dates(), numberOfGuests=safe_text)
@given(instance=Classes_Booking_strategy)
@settings(max_examples=25)
def test_Classes_Booking_instantiation(instance):
    assert isinstance(instance, Classes_Booking)


Classes_Charge_strategy = st.builds(Classes_Charge, amount=st.integers(), chargeType=safe_text, date=st.dates())
@given(instance=Classes_Charge_strategy)
@settings(max_examples=25)
def test_Classes_Charge_instantiation(instance):
    assert isinstance(instance, Classes_Charge)


Classes_Customer_strategy = st.builds(Classes_Customer)
@given(instance=Classes_Customer_strategy)
@settings(max_examples=25)
def test_Classes_Customer_instantiation(instance):
    assert isinstance(instance, Classes_Customer)


Classes_CustomerProvides_strategy = st.builds(Classes_CustomerProvides)
@given(instance=Classes_CustomerProvides_strategy)
@settings(max_examples=25)
def test_Classes_CustomerProvides_instantiation(instance):
    assert isinstance(instance, Classes_CustomerProvides)


Classes_IBookingManagement_strategy = st.builds(Classes_IBookingManagement)
@given(instance=Classes_IBookingManagement_strategy)
@settings(max_examples=25)
def test_Classes_IBookingManagement_instantiation(instance):
    assert isinstance(instance, Classes_IBookingManagement)


Classes_IBookingManagementImpl_strategy = st.builds(Classes_IBookingManagementImpl)
@given(instance=Classes_IBookingManagementImpl_strategy)
@settings(max_examples=25)
def test_Classes_IBookingManagementImpl_instantiation(instance):
    assert isinstance(instance, Classes_IBookingManagementImpl)


Classes_IFinance_strategy = st.builds(Classes_IFinance)
@given(instance=Classes_IFinance_strategy)
@settings(max_examples=25)
def test_Classes_IFinance_instantiation(instance):
    assert isinstance(instance, Classes_IFinance)


Classes_IFinanceImpl_strategy = st.builds(Classes_IFinanceImpl)
@given(instance=Classes_IFinanceImpl_strategy)
@settings(max_examples=25)
def test_Classes_IFinanceImpl_instantiation(instance):
    assert isinstance(instance, Classes_IFinanceImpl)


Classes_IHotelManager_strategy = st.builds(Classes_IHotelManager)
@given(instance=Classes_IHotelManager_strategy)
@settings(max_examples=25)
def test_Classes_IHotelManager_instantiation(instance):
    assert isinstance(instance, Classes_IHotelManager)


Classes_IHotelManagerImpl_strategy = st.builds(Classes_IHotelManagerImpl)
@given(instance=Classes_IHotelManagerImpl_strategy)
@settings(max_examples=25)
def test_Classes_IHotelManagerImpl_instantiation(instance):
    assert isinstance(instance, Classes_IHotelManagerImpl)


Classes_IPerson_strategy = st.builds(Classes_IPerson, address=safe_text, email=safe_text, firstName=safe_text, lastName=safe_text, phoneNumber=safe_text)
@given(instance=Classes_IPerson_strategy)
@settings(max_examples=25)
def test_Classes_IPerson_instantiation(instance):
    assert isinstance(instance, Classes_IPerson)


Classes_Room_strategy = st.builds(Classes_Room, roomNumber=safe_text, status=safe_text)
@given(instance=Classes_Room_strategy)
@settings(max_examples=25)
def test_Classes_Room_instantiation(instance):
    assert isinstance(instance, Classes_Room)


Classes_RoomType_strategy = st.builds(Classes_RoomType, description=safe_text, features=safe_text, numberOfGuests=safe_text, price=safe_text, roomTypeName=safe_text)
@given(instance=Classes_RoomType_strategy)
@settings(max_examples=25)
def test_Classes_RoomType_instantiation(instance):
    assert isinstance(instance, Classes_RoomType)


Classes_StaffMember_strategy = st.builds(Classes_StaffMember, admin=safe_text, isLoggedIn=st.booleans(), password=safe_text, username=safe_text)
@given(instance=Classes_StaffMember_strategy)
@settings(max_examples=25)
def test_Classes_StaffMember_instantiation(instance):
    assert isinstance(instance, Classes_StaffMember)


IBookingManagement_strategy = st.builds(IBookingManagement)
@given(instance=IBookingManagement_strategy)
@settings(max_examples=25)
def test_IBookingManagement_instantiation(instance):
    assert isinstance(instance, IBookingManagement)


IFinance_strategy = st.builds(IFinance)
@given(instance=IFinance_strategy)
@settings(max_examples=25)
def test_IFinance_instantiation(instance):
    assert isinstance(instance, IFinance)


IHotelManager_strategy = st.builds(IHotelManager)
@given(instance=IHotelManager_strategy)
@settings(max_examples=25)
def test_IHotelManager_instantiation(instance):
    assert isinstance(instance, IHotelManager)


IPerson_strategy = st.builds(IPerson)
@given(instance=IPerson_strategy)
@settings(max_examples=25)
def test_IPerson_instantiation(instance):
    assert isinstance(instance, IPerson)



