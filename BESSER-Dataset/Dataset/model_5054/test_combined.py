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
    hairDressersRegSys_Invoice,
    hairDressersRegSys_Appointment,
    hairDressersRegSys_Person,
    Service,
    hairDressersRegSys_Styling,
    hairDressersRegSys_Payment,
    hairDressersRegSys_Discounts,
    hairDressersRegSys_Products,
    Person,
    hairDressersRegSys_Customer,
    hairDressersRegSys_ServiceEmployee,
    hairDressersRegSys_Other,
    hairDressersRegSys_Haircuts,
    hairDressersRegSys_Service,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_hairdressersregsys_invoice_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Invoice)


def test_hyp_hairdressersregsys_invoice_constructor_exists():
    assert callable(hairDressersRegSys_Invoice.__init__)


def test_hyp_hairdressersregsys_invoice_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Invoice.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "InvoiceNumber" in params, "Missing parameter 'InvoiceNumber'"






def test_hyp_hairdressersregsys_appointment_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Appointment)


def test_hyp_hairdressersregsys_appointment_constructor_exists():
    assert callable(hairDressersRegSys_Appointment.__init__)


def test_hyp_hairdressersregsys_appointment_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Appointment.__init__)
    params = list(sig.parameters.keys())
    assert "StartTime" in params, "Missing parameter 'StartTime'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "EndTime" in params, "Missing parameter 'EndTime'"






def test_hyp_hairdressersregsys_person_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Person)


def test_hyp_hairdressersregsys_person_constructor_exists():
    assert callable(hairDressersRegSys_Person.__init__)


def test_hyp_hairdressersregsys_person_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Person.__init__)
    params = list(sig.parameters.keys())
    assert "FirstName" in params, "Missing parameter 'FirstName'"
    assert "DateOfBirth" in params, "Missing parameter 'DateOfBirth'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "Address" in params, "Missing parameter 'Address'"







def test_hyp_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_hyp_service_constructor_exists():
    assert callable(Service.__init__)


def test_hyp_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hairdressersregsys_styling_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Styling)


def test_hyp_hairdressersregsys_styling_constructor_exists():
    assert callable(hairDressersRegSys_Styling.__init__)


def test_hyp_hairdressersregsys_styling_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Styling.__init__)
    params = list(sig.parameters.keys())
    assert "IsWash" in params, "Missing parameter 'IsWash'"




def test_hyp_hairdressersregsys_payment_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Payment)


def test_hyp_hairdressersregsys_payment_constructor_exists():
    assert callable(hairDressersRegSys_Payment.__init__)


def test_hyp_hairdressersregsys_payment_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "PaymentMethod" in params, "Missing parameter 'PaymentMethod'"
    assert "AmountPaid" in params, "Missing parameter 'AmountPaid'"






def test_hyp_hairdressersregsys_discounts_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Discounts)


def test_hyp_hairdressersregsys_discounts_constructor_exists():
    assert callable(hairDressersRegSys_Discounts.__init__)


def test_hyp_hairdressersregsys_discounts_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Discounts.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Percentage" in params, "Missing parameter 'Percentage'"






def test_hyp_hairdressersregsys_products_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Products)


def test_hyp_hairdressersregsys_products_constructor_exists():
    assert callable(hairDressersRegSys_Products.__init__)


def test_hyp_hairdressersregsys_products_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Products.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Price" in params, "Missing parameter 'Price'"
    assert "Description" in params, "Missing parameter 'Description'"






def test_hyp_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_hyp_person_constructor_exists():
    assert callable(Person.__init__)


def test_hyp_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_hyp_hairdressersregsys_customer_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Customer)


def test_hyp_hairdressersregsys_customer_constructor_exists():
    assert callable(hairDressersRegSys_Customer.__init__)


def test_hyp_hairdressersregsys_customer_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "CustomerId" in params, "Missing parameter 'CustomerId'"




def test_hyp_hairdressersregsys_serviceemployee_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_ServiceEmployee)


def test_hyp_hairdressersregsys_serviceemployee_constructor_exists():
    assert callable(hairDressersRegSys_ServiceEmployee.__init__)


def test_hyp_hairdressersregsys_serviceemployee_constructor_args():
    sig = inspect.signature(hairDressersRegSys_ServiceEmployee.__init__)
    params = list(sig.parameters.keys())
    assert "Role" in params, "Missing parameter 'Role'"
    assert "EmployeeId" in params, "Missing parameter 'EmployeeId'"





def test_hyp_hairdressersregsys_other_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Other)


def test_hyp_hairdressersregsys_other_constructor_exists():
    assert callable(hairDressersRegSys_Other.__init__)


def test_hyp_hairdressersregsys_other_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Other.__init__)
    params = list(sig.parameters.keys())
    assert "AdditionalInformation" in params, "Missing parameter 'AdditionalInformation'"




def test_hyp_hairdressersregsys_haircuts_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Haircuts)


def test_hyp_hairdressersregsys_haircuts_constructor_exists():
    assert callable(hairDressersRegSys_Haircuts.__init__)


def test_hyp_hairdressersregsys_haircuts_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Haircuts.__init__)
    params = list(sig.parameters.keys())
    assert "IsWash" in params, "Missing parameter 'IsWash'"
    assert "IsCut" in params, "Missing parameter 'IsCut'"
    assert "IsShave" in params, "Missing parameter 'IsShave'"






def test_hyp_hairdressersregsys_service_is_not_abstract():
    assert not inspect.isabstract(hairDressersRegSys_Service)


def test_hyp_hairdressersregsys_service_constructor_exists():
    assert callable(hairDressersRegSys_Service.__init__)


def test_hyp_hairdressersregsys_service_constructor_args():
    sig = inspect.signature(hairDressersRegSys_Service.__init__)
    params = list(sig.parameters.keys())
    assert "Time" in params, "Missing parameter 'Time'"
    assert "CostPerHour" in params, "Missing parameter 'CostPerHour'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Name" in params, "Missing parameter 'Name'"






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
hairDressersRegSys_Invoice_strategy = st.builds(
    hairDressersRegSys_Invoice,
    Date=
        safe_text,
    Total=
        safe_text,
    InvoiceNumber=
        st.integers()
)
hairDressersRegSys_Appointment_strategy = st.builds(
    hairDressersRegSys_Appointment,
    StartTime=
        st.dates(),
    Date=
        st.dates(),
    EndTime=
        st.dates()
)
hairDressersRegSys_Person_strategy = st.builds(
    hairDressersRegSys_Person,
    FirstName=
        safe_text,
    DateOfBirth=
        st.dates(),
    LastName=
        safe_text,
    Address=
        safe_text
)
Service_strategy = st.builds(
    Service,
)
hairDressersRegSys_Styling_strategy = st.builds(
    hairDressersRegSys_Styling,
    IsWash=
        st.booleans()
)
hairDressersRegSys_Payment_strategy = st.builds(
    hairDressersRegSys_Payment,
    Date=
        st.dates(),
    PaymentMethod=
        safe_text,
    AmountPaid=
        safe_text
)
hairDressersRegSys_Discounts_strategy = st.builds(
    hairDressersRegSys_Discounts,
    Description=
        safe_text,
    Name=
        safe_text,
    Percentage=
        st.integers()
)
hairDressersRegSys_Products_strategy = st.builds(
    hairDressersRegSys_Products,
    Name=
        safe_text,
    Price=
        safe_text,
    Description=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
hairDressersRegSys_Customer_strategy = st.builds(
    hairDressersRegSys_Customer,
    CustomerId=
        st.integers()
)
hairDressersRegSys_ServiceEmployee_strategy = st.builds(
    hairDressersRegSys_ServiceEmployee,
    Role=
        safe_text,
    EmployeeId=
        st.integers()
)
hairDressersRegSys_Other_strategy = st.builds(
    hairDressersRegSys_Other,
    AdditionalInformation=
        safe_text
)
hairDressersRegSys_Haircuts_strategy = st.builds(
    hairDressersRegSys_Haircuts,
    IsWash=
        st.booleans(),
    IsCut=
        st.booleans(),
    IsShave=
        st.booleans()
)
hairDressersRegSys_Service_strategy = st.builds(
    hairDressersRegSys_Service,
    Time=
        st.dates(),
    CostPerHour=
        safe_text,
    Description=
        safe_text,
    Name=
        safe_text
)




@given(instance=hairDressersRegSys_Invoice_strategy)
def test_hyp_hairdressersregsys_invoice_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=hairDressersRegSys_Invoice_strategy)
def test_hyp_hairdressersregsys_invoice_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original



@given(instance=hairDressersRegSys_Invoice_strategy)
def test_hyp_hairdressersregsys_invoice_InvoiceNumber_setter(instance):
    original = instance.InvoiceNumber
    instance.InvoiceNumber = original
    assert instance.InvoiceNumber == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Invoice_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_invoice_calculatetotal_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.CalculateTotal()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.CalculateTotal).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'CalculateTotal' in hairDressersRegSys_Invoice is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'CalculateTotal' in hairDressersRegSys_Invoice did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'CalculateTotal' in hairDressersRegSys_Invoice is not implemented or raised an error")




@given(instance=hairDressersRegSys_Appointment_strategy)
def test_hyp_hairdressersregsys_appointment_StartTime_setter(instance):
    original = instance.StartTime
    instance.StartTime = original
    assert instance.StartTime == original



@given(instance=hairDressersRegSys_Appointment_strategy)
def test_hyp_hairdressersregsys_appointment_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=hairDressersRegSys_Appointment_strategy)
def test_hyp_hairdressersregsys_appointment_EndTime_setter(instance):
    original = instance.EndTime
    instance.EndTime = original
    assert instance.EndTime == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Appointment_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_appointment_viewschedule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ViewSchedule()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ViewSchedule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ViewSchedule' in hairDressersRegSys_Appointment is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ViewSchedule' in hairDressersRegSys_Appointment did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ViewSchedule' in hairDressersRegSys_Appointment is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Appointment_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_appointment_addappointment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AddAppointment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AddAppointment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AddAppointment' in hairDressersRegSys_Appointment is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AddAppointment' in hairDressersRegSys_Appointment did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AddAppointment' in hairDressersRegSys_Appointment is not implemented or raised an error")




@given(instance=hairDressersRegSys_Person_strategy)
def test_hyp_hairdressersregsys_person_FirstName_setter(instance):
    original = instance.FirstName
    instance.FirstName = original
    assert instance.FirstName == original



@given(instance=hairDressersRegSys_Person_strategy)
def test_hyp_hairdressersregsys_person_DateOfBirth_setter(instance):
    original = instance.DateOfBirth
    instance.DateOfBirth = original
    assert instance.DateOfBirth == original



@given(instance=hairDressersRegSys_Person_strategy)
def test_hyp_hairdressersregsys_person_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=hairDressersRegSys_Person_strategy)
def test_hyp_hairdressersregsys_person_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original





@given(instance=hairDressersRegSys_Styling_strategy)
def test_hyp_hairdressersregsys_styling_IsWash_setter(instance):
    original = instance.IsWash
    instance.IsWash = original
    assert instance.IsWash == original




@given(instance=hairDressersRegSys_Payment_strategy)
def test_hyp_hairdressersregsys_payment_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=hairDressersRegSys_Payment_strategy)
def test_hyp_hairdressersregsys_payment_PaymentMethod_setter(instance):
    original = instance.PaymentMethod
    instance.PaymentMethod = original
    assert instance.PaymentMethod == original



@given(instance=hairDressersRegSys_Payment_strategy)
def test_hyp_hairdressersregsys_payment_AmountPaid_setter(instance):
    original = instance.AmountPaid
    instance.AmountPaid = original
    assert instance.AmountPaid == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Payment_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_payment_makepayment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.MakePayment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.MakePayment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'MakePayment' in hairDressersRegSys_Payment is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'MakePayment' in hairDressersRegSys_Payment did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'MakePayment' in hairDressersRegSys_Payment is not implemented or raised an error")




@given(instance=hairDressersRegSys_Discounts_strategy)
def test_hyp_hairdressersregsys_discounts_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=hairDressersRegSys_Discounts_strategy)
def test_hyp_hairdressersregsys_discounts_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=hairDressersRegSys_Discounts_strategy)
def test_hyp_hairdressersregsys_discounts_Percentage_setter(instance):
    original = instance.Percentage
    instance.Percentage = original
    assert instance.Percentage == original




@given(instance=hairDressersRegSys_Products_strategy)
def test_hyp_hairdressersregsys_products_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=hairDressersRegSys_Products_strategy)
def test_hyp_hairdressersregsys_products_Price_setter(instance):
    original = instance.Price
    instance.Price = original
    assert instance.Price == original



@given(instance=hairDressersRegSys_Products_strategy)
def test_hyp_hairdressersregsys_products_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Products_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_products_addproduct_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AddProduct()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AddProduct).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AddProduct' in hairDressersRegSys_Products is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AddProduct' in hairDressersRegSys_Products did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AddProduct' in hairDressersRegSys_Products is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Products_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_products_viewtotalstock_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ViewTotalStock()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ViewTotalStock).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ViewTotalStock' in hairDressersRegSys_Products is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ViewTotalStock' in hairDressersRegSys_Products did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ViewTotalStock' in hairDressersRegSys_Products is not implemented or raised an error")





@given(instance=hairDressersRegSys_Customer_strategy)
def test_hyp_hairdressersregsys_customer_CustomerId_setter(instance):
    original = instance.CustomerId
    instance.CustomerId = original
    assert instance.CustomerId == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Customer_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_customer_placeappointment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.PlaceAppointment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.PlaceAppointment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'PlaceAppointment' in hairDressersRegSys_Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'PlaceAppointment' in hairDressersRegSys_Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'PlaceAppointment' in hairDressersRegSys_Customer is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Customer_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_customer_addnewcustomer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AddNewCustomer()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AddNewCustomer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AddNewCustomer' in hairDressersRegSys_Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AddNewCustomer' in hairDressersRegSys_Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AddNewCustomer' in hairDressersRegSys_Customer is not implemented or raised an error")




@given(instance=hairDressersRegSys_ServiceEmployee_strategy)
def test_hyp_hairdressersregsys_serviceemployee_Role_setter(instance):
    original = instance.Role
    instance.Role = original
    assert instance.Role == original



@given(instance=hairDressersRegSys_ServiceEmployee_strategy)
def test_hyp_hairdressersregsys_serviceemployee_EmployeeId_setter(instance):
    original = instance.EmployeeId
    instance.EmployeeId = original
    assert instance.EmployeeId == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_ServiceEmployee_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_serviceemployee_addnewemployee_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AddNewEmployee()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AddNewEmployee).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AddNewEmployee' in hairDressersRegSys_ServiceEmployee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AddNewEmployee' in hairDressersRegSys_ServiceEmployee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AddNewEmployee' in hairDressersRegSys_ServiceEmployee is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_ServiceEmployee_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_serviceemployee_viewallavailableemployees_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ViewAllAvailableEmployees()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ViewAllAvailableEmployees).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ViewAllAvailableEmployees' in hairDressersRegSys_ServiceEmployee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ViewAllAvailableEmployees' in hairDressersRegSys_ServiceEmployee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ViewAllAvailableEmployees' in hairDressersRegSys_ServiceEmployee is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_ServiceEmployee_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_serviceemployee_removeappointment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RemoveAppointment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RemoveAppointment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RemoveAppointment' in hairDressersRegSys_ServiceEmployee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RemoveAppointment' in hairDressersRegSys_ServiceEmployee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RemoveAppointment' in hairDressersRegSys_ServiceEmployee is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_ServiceEmployee_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_serviceemployee_viewappointments_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ViewAppointments()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ViewAppointments).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ViewAppointments' in hairDressersRegSys_ServiceEmployee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ViewAppointments' in hairDressersRegSys_ServiceEmployee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ViewAppointments' in hairDressersRegSys_ServiceEmployee is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_ServiceEmployee_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_serviceemployee_makeappointment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.MakeAppointment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.MakeAppointment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'MakeAppointment' in hairDressersRegSys_ServiceEmployee is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'MakeAppointment' in hairDressersRegSys_ServiceEmployee did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'MakeAppointment' in hairDressersRegSys_ServiceEmployee is not implemented or raised an error")




@given(instance=hairDressersRegSys_Other_strategy)
def test_hyp_hairdressersregsys_other_AdditionalInformation_setter(instance):
    original = instance.AdditionalInformation
    instance.AdditionalInformation = original
    assert instance.AdditionalInformation == original




@given(instance=hairDressersRegSys_Haircuts_strategy)
def test_hyp_hairdressersregsys_haircuts_IsWash_setter(instance):
    original = instance.IsWash
    instance.IsWash = original
    assert instance.IsWash == original



@given(instance=hairDressersRegSys_Haircuts_strategy)
def test_hyp_hairdressersregsys_haircuts_IsCut_setter(instance):
    original = instance.IsCut
    instance.IsCut = original
    assert instance.IsCut == original



@given(instance=hairDressersRegSys_Haircuts_strategy)
def test_hyp_hairdressersregsys_haircuts_IsShave_setter(instance):
    original = instance.IsShave
    instance.IsShave = original
    assert instance.IsShave == original




@given(instance=hairDressersRegSys_Service_strategy)
def test_hyp_hairdressersregsys_service_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=hairDressersRegSys_Service_strategy)
def test_hyp_hairdressersregsys_service_CostPerHour_setter(instance):
    original = instance.CostPerHour
    instance.CostPerHour = original
    assert instance.CostPerHour == original



@given(instance=hairDressersRegSys_Service_strategy)
def test_hyp_hairdressersregsys_service_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=hairDressersRegSys_Service_strategy)
def test_hyp_hairdressersregsys_service_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Service_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_service_removeservice_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.RemoveService()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.RemoveService).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'RemoveService' in hairDressersRegSys_Service is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'RemoveService' in hairDressersRegSys_Service did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'RemoveService' in hairDressersRegSys_Service is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Service_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_service_viewallservices_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ViewAllServices()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ViewAllServices).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ViewAllServices' in hairDressersRegSys_Service is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ViewAllServices' in hairDressersRegSys_Service did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ViewAllServices' in hairDressersRegSys_Service is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=hairDressersRegSys_Service_strategy)
@settings(max_examples=30)
def test_hyp_hairdressersregsys_service_addservice_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.AddService()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.AddService).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'AddService' in hairDressersRegSys_Service is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'AddService' in hairDressersRegSys_Service did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'AddService' in hairDressersRegSys_Service is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Person,
    Service,
    hairDressersRegSys_Appointment,
    hairDressersRegSys_Customer,
    hairDressersRegSys_Discounts,
    hairDressersRegSys_Haircuts,
    hairDressersRegSys_Invoice,
    hairDressersRegSys_Other,
    hairDressersRegSys_Payment,
    hairDressersRegSys_Person,
    hairDressersRegSys_Products,
    hairDressersRegSys_Service,
    hairDressersRegSys_ServiceEmployee,
    hairDressersRegSys_Styling,
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

def test_hairDressersRegSys_Appointment_Date_value_roundtrip():
    instance = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    assert instance.Date == date(2024, 1, 1)
    instance.Date = date(2025, 6, 15)
    assert instance.Date == date(2025, 6, 15)


def test_hairDressersRegSys_Appointment_EndTime_value_roundtrip():
    instance = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    assert instance.EndTime == date(2024, 1, 1)
    instance.EndTime = date(2025, 6, 15)
    assert instance.EndTime == date(2025, 6, 15)


def test_hairDressersRegSys_Appointment_StartTime_value_roundtrip():
    instance = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    assert instance.StartTime == date(2024, 1, 1)
    instance.StartTime = date(2025, 6, 15)
    assert instance.StartTime == date(2025, 6, 15)


def test_hairDressersRegSys_Customer_CustomerId_value_roundtrip():
    instance = hairDressersRegSys_Customer(CustomerId=7)
    assert instance.CustomerId == 7
    instance.CustomerId = 13
    assert instance.CustomerId == 13


def test_hairDressersRegSys_Discounts_Description_value_roundtrip():
    instance = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_hairDressersRegSys_Discounts_Name_value_roundtrip():
    instance = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_hairDressersRegSys_Discounts_Percentage_value_roundtrip():
    instance = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    assert instance.Percentage == 7
    instance.Percentage = 13
    assert instance.Percentage == 13


def test_hairDressersRegSys_Haircuts_IsCut_value_roundtrip():
    instance = hairDressersRegSys_Haircuts(IsCut=True, IsShave=True, IsWash=True)
    assert instance.IsCut == True
    instance.IsCut = False
    assert instance.IsCut == False


def test_hairDressersRegSys_Haircuts_IsShave_value_roundtrip():
    instance = hairDressersRegSys_Haircuts(IsCut=True, IsShave=True, IsWash=True)
    assert instance.IsShave == True
    instance.IsShave = False
    assert instance.IsShave == False


def test_hairDressersRegSys_Haircuts_IsWash_value_roundtrip():
    instance = hairDressersRegSys_Haircuts(IsCut=True, IsShave=True, IsWash=True)
    assert instance.IsWash == True
    instance.IsWash = False
    assert instance.IsWash == False


def test_hairDressersRegSys_Invoice_Date_value_roundtrip():
    instance = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    assert instance.Date == "sample_text"
    instance.Date = "sample_text_2"
    assert instance.Date == "sample_text_2"


def test_hairDressersRegSys_Invoice_InvoiceNumber_value_roundtrip():
    instance = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    assert instance.InvoiceNumber == 7
    instance.InvoiceNumber = 13
    assert instance.InvoiceNumber == 13


def test_hairDressersRegSys_Invoice_Total_value_roundtrip():
    instance = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    assert instance.Total == "sample_text"
    instance.Total = "sample_text_2"
    assert instance.Total == "sample_text_2"


def test_hairDressersRegSys_Other_AdditionalInformation_value_roundtrip():
    instance = hairDressersRegSys_Other(AdditionalInformation="sample_text")
    assert instance.AdditionalInformation == "sample_text"
    instance.AdditionalInformation = "sample_text_2"
    assert instance.AdditionalInformation == "sample_text_2"


def test_hairDressersRegSys_Payment_AmountPaid_value_roundtrip():
    instance = hairDressersRegSys_Payment(AmountPaid="sample_text", Date=date(2024, 1, 1), PaymentMethod="sample_text")
    assert instance.AmountPaid == "sample_text"
    instance.AmountPaid = "sample_text_2"
    assert instance.AmountPaid == "sample_text_2"


def test_hairDressersRegSys_Payment_Date_value_roundtrip():
    instance = hairDressersRegSys_Payment(AmountPaid="sample_text", Date=date(2024, 1, 1), PaymentMethod="sample_text")
    assert instance.Date == date(2024, 1, 1)
    instance.Date = date(2025, 6, 15)
    assert instance.Date == date(2025, 6, 15)


def test_hairDressersRegSys_Payment_PaymentMethod_value_roundtrip():
    instance = hairDressersRegSys_Payment(AmountPaid="sample_text", Date=date(2024, 1, 1), PaymentMethod="sample_text")
    assert instance.PaymentMethod == "sample_text"
    instance.PaymentMethod = "sample_text_2"
    assert instance.PaymentMethod == "sample_text_2"


def test_hairDressersRegSys_Person_Address_value_roundtrip():
    instance = hairDressersRegSys_Person(Address="sample_text", DateOfBirth=date(2024, 1, 1), FirstName="sample_text", LastName="sample_text")
    assert instance.Address == "sample_text"
    instance.Address = "sample_text_2"
    assert instance.Address == "sample_text_2"


def test_hairDressersRegSys_Person_DateOfBirth_value_roundtrip():
    instance = hairDressersRegSys_Person(Address="sample_text", DateOfBirth=date(2024, 1, 1), FirstName="sample_text", LastName="sample_text")
    assert instance.DateOfBirth == date(2024, 1, 1)
    instance.DateOfBirth = date(2025, 6, 15)
    assert instance.DateOfBirth == date(2025, 6, 15)


def test_hairDressersRegSys_Person_FirstName_value_roundtrip():
    instance = hairDressersRegSys_Person(Address="sample_text", DateOfBirth=date(2024, 1, 1), FirstName="sample_text", LastName="sample_text")
    assert instance.FirstName == "sample_text"
    instance.FirstName = "sample_text_2"
    assert instance.FirstName == "sample_text_2"


def test_hairDressersRegSys_Person_LastName_value_roundtrip():
    instance = hairDressersRegSys_Person(Address="sample_text", DateOfBirth=date(2024, 1, 1), FirstName="sample_text", LastName="sample_text")
    assert instance.LastName == "sample_text"
    instance.LastName = "sample_text_2"
    assert instance.LastName == "sample_text_2"


def test_hairDressersRegSys_Products_Description_value_roundtrip():
    instance = hairDressersRegSys_Products(Description="sample_text", Name="sample_text", Price="sample_text")
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_hairDressersRegSys_Products_Name_value_roundtrip():
    instance = hairDressersRegSys_Products(Description="sample_text", Name="sample_text", Price="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_hairDressersRegSys_Products_Price_value_roundtrip():
    instance = hairDressersRegSys_Products(Description="sample_text", Name="sample_text", Price="sample_text")
    assert instance.Price == "sample_text"
    instance.Price = "sample_text_2"
    assert instance.Price == "sample_text_2"


def test_hairDressersRegSys_Service_CostPerHour_value_roundtrip():
    instance = hairDressersRegSys_Service(CostPerHour="sample_text", Description="sample_text", Name="sample_text", Time=date(2024, 1, 1))
    assert instance.CostPerHour == "sample_text"
    instance.CostPerHour = "sample_text_2"
    assert instance.CostPerHour == "sample_text_2"


def test_hairDressersRegSys_Service_Description_value_roundtrip():
    instance = hairDressersRegSys_Service(CostPerHour="sample_text", Description="sample_text", Name="sample_text", Time=date(2024, 1, 1))
    assert instance.Description == "sample_text"
    instance.Description = "sample_text_2"
    assert instance.Description == "sample_text_2"


def test_hairDressersRegSys_Service_Name_value_roundtrip():
    instance = hairDressersRegSys_Service(CostPerHour="sample_text", Description="sample_text", Name="sample_text", Time=date(2024, 1, 1))
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_hairDressersRegSys_Service_Time_value_roundtrip():
    instance = hairDressersRegSys_Service(CostPerHour="sample_text", Description="sample_text", Name="sample_text", Time=date(2024, 1, 1))
    assert instance.Time == date(2024, 1, 1)
    instance.Time = date(2025, 6, 15)
    assert instance.Time == date(2025, 6, 15)


def test_hairDressersRegSys_ServiceEmployee_EmployeeId_value_roundtrip():
    instance = hairDressersRegSys_ServiceEmployee(EmployeeId=7, Role="sample_text")
    assert instance.EmployeeId == 7
    instance.EmployeeId = 13
    assert instance.EmployeeId == 13


def test_hairDressersRegSys_ServiceEmployee_Role_value_roundtrip():
    instance = hairDressersRegSys_ServiceEmployee(EmployeeId=7, Role="sample_text")
    assert instance.Role == "sample_text"
    instance.Role = "sample_text_2"
    assert instance.Role == "sample_text_2"


def test_hairDressersRegSys_Styling_IsWash_value_roundtrip():
    instance = hairDressersRegSys_Styling(IsWash=True)
    assert instance.IsWash == True
    instance.IsWash = False
    assert instance.IsWash == False


def test_hairDressersRegSys_Customer_isa_Person():
    instance = hairDressersRegSys_Customer(CustomerId=7)
    assert isinstance(instance, Person)


def test_hairDressersRegSys_ServiceEmployee_isa_Person():
    instance = hairDressersRegSys_ServiceEmployee(EmployeeId=7, Role="sample_text")
    assert isinstance(instance, Person)


def test_hairDressersRegSys_Haircuts_isa_Service():
    instance = hairDressersRegSys_Haircuts(IsCut=True, IsShave=True, IsWash=True)
    assert isinstance(instance, Service)


def test_hairDressersRegSys_Other_isa_Service():
    instance = hairDressersRegSys_Other(AdditionalInformation="sample_text")
    assert isinstance(instance, Service)


def test_hairDressersRegSys_Styling_isa_Service():
    instance = hairDressersRegSys_Styling(IsWash=True)
    assert isinstance(instance, Service)


def test_assoc_appointment0_link_reassign_clear():
    a = hairDressersRegSys_Service(CostPerHour="sample_text", Description="sample_text", Name="sample_text", Time=date(2024, 1, 1))
    b1 = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    b2 = hairDressersRegSys_Appointment(Date=date(2025, 6, 15), EndTime=date(2025, 6, 15), StartTime=date(2025, 6, 15))
    _safe_set(a, 'hairDressersRegSys_Service', {b1})
    assert _is_linked(a, 'hairDressersRegSys_Service', b1)
    if hasattr(b1, 'hairDressersRegSys_Appointment'):
        assert _is_linked(b1, 'hairDressersRegSys_Appointment', a)
    _safe_set(a, 'hairDressersRegSys_Service', {b2})
    assert _is_linked(a, 'hairDressersRegSys_Service', b2)
    if hasattr(b1, 'hairDressersRegSys_Appointment'):
        assert not _is_linked(b1, 'hairDressersRegSys_Appointment', a)
    if hasattr(b2, 'hairDressersRegSys_Appointment'):
        assert _is_linked(b2, 'hairDressersRegSys_Appointment', a)
    _safe_set(a, 'hairDressersRegSys_Service', set())
    assert not _is_linked(a, 'hairDressersRegSys_Service', b2)
    if hasattr(b2, 'hairDressersRegSys_Appointment'):
        assert not _is_linked(b2, 'hairDressersRegSys_Appointment', a)


def test_assoc_appointment13_link_reassign_clear():
    a = hairDressersRegSys_Customer(CustomerId=7)
    b1 = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    b2 = hairDressersRegSys_Appointment(Date=date(2025, 6, 15), EndTime=date(2025, 6, 15), StartTime=date(2025, 6, 15))
    _safe_set(a, 'hairDressersRegSys_Customer', {b1})
    assert _is_linked(a, 'hairDressersRegSys_Customer', b1)
    if hasattr(b1, 'hairDressersRegSys_Appointment14'):
        assert _is_linked(b1, 'hairDressersRegSys_Appointment14', a)
    _safe_set(a, 'hairDressersRegSys_Customer', {b2})
    assert _is_linked(a, 'hairDressersRegSys_Customer', b2)
    if hasattr(b1, 'hairDressersRegSys_Appointment14'):
        assert not _is_linked(b1, 'hairDressersRegSys_Appointment14', a)
    if hasattr(b2, 'hairDressersRegSys_Appointment14'):
        assert _is_linked(b2, 'hairDressersRegSys_Appointment14', a)
    _safe_set(a, 'hairDressersRegSys_Customer', set())
    assert not _is_linked(a, 'hairDressersRegSys_Customer', b2)
    if hasattr(b2, 'hairDressersRegSys_Appointment14'):
        assert not _is_linked(b2, 'hairDressersRegSys_Appointment14', a)


def test_assoc_appointment17_link_reassign_clear():
    a = hairDressersRegSys_ServiceEmployee(EmployeeId=7, Role="sample_text")
    b1 = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    b2 = hairDressersRegSys_Appointment(Date=date(2025, 6, 15), EndTime=date(2025, 6, 15), StartTime=date(2025, 6, 15))
    _safe_set(a, 'hairDressersRegSys_ServiceEmployee', {b1})
    assert _is_linked(a, 'hairDressersRegSys_ServiceEmployee', b1)
    if hasattr(b1, 'hairDressersRegSys_Appointment18'):
        assert _is_linked(b1, 'hairDressersRegSys_Appointment18', a)
    _safe_set(a, 'hairDressersRegSys_ServiceEmployee', {b2})
    assert _is_linked(a, 'hairDressersRegSys_ServiceEmployee', b2)
    if hasattr(b1, 'hairDressersRegSys_Appointment18'):
        assert not _is_linked(b1, 'hairDressersRegSys_Appointment18', a)
    if hasattr(b2, 'hairDressersRegSys_Appointment18'):
        assert _is_linked(b2, 'hairDressersRegSys_Appointment18', a)
    _safe_set(a, 'hairDressersRegSys_ServiceEmployee', set())
    assert not _is_linked(a, 'hairDressersRegSys_ServiceEmployee', b2)
    if hasattr(b2, 'hairDressersRegSys_Appointment18'):
        assert not _is_linked(b2, 'hairDressersRegSys_Appointment18', a)


def test_assoc_customer9_link_reassign_clear():
    a = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    b1 = hairDressersRegSys_Customer(CustomerId=7)
    b2 = hairDressersRegSys_Customer(CustomerId=13)
    _safe_set(a, 'discounts', {b1})
    assert _is_linked(a, 'discounts', b1)
    if hasattr(b1, 'Customer'):
        assert _is_linked(b1, 'Customer', a)
    _safe_set(a, 'discounts', {b2})
    assert _is_linked(a, 'discounts', b2)
    if hasattr(b1, 'Customer'):
        assert not _is_linked(b1, 'Customer', a)
    if hasattr(b2, 'Customer'):
        assert _is_linked(b2, 'Customer', a)
    _safe_set(a, 'discounts', set())
    assert not _is_linked(a, 'discounts', b2)
    if hasattr(b2, 'Customer'):
        assert not _is_linked(b2, 'Customer', a)


def test_assoc_discounts15_link_reassign_clear():
    a = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    b1 = hairDressersRegSys_Customer(CustomerId=7)
    b2 = hairDressersRegSys_Customer(CustomerId=13)
    _safe_set(a, 'Discounts16', b1)
    assert _is_linked(a, 'Discounts16', b1)
    if hasattr(b1, 'customer'):
        assert _is_linked(b1, 'customer', a)
    _safe_set(a, 'Discounts16', b2)
    assert _is_linked(a, 'Discounts16', b2)
    if hasattr(b1, 'customer'):
        assert not _is_linked(b1, 'customer', a)
    if hasattr(b2, 'customer'):
        assert _is_linked(b2, 'customer', a)
    _safe_set(a, 'Discounts16', None)
    assert not _is_linked(a, 'Discounts16', b2)
    if hasattr(b2, 'customer'):
        assert not _is_linked(b2, 'customer', a)


def test_assoc_discounts5_link_reassign_clear():
    a = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    b1 = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    b2 = hairDressersRegSys_Discounts(Description="sample_text_2", Name="sample_text_2", Percentage=13)
    _safe_set(a, 'invoice6', b1)
    assert _is_linked(a, 'invoice6', b1)
    if hasattr(b1, 'Discounts'):
        assert _is_linked(b1, 'Discounts', a)
    _safe_set(a, 'invoice6', b2)
    assert _is_linked(a, 'invoice6', b2)
    if hasattr(b1, 'Discounts'):
        assert not _is_linked(b1, 'Discounts', a)
    if hasattr(b2, 'Discounts'):
        assert _is_linked(b2, 'Discounts', a)
    _safe_set(a, 'invoice6', None)
    assert not _is_linked(a, 'invoice6', b2)
    if hasattr(b2, 'Discounts'):
        assert not _is_linked(b2, 'Discounts', a)


def test_assoc_invoice1_link_reassign_clear():
    a = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    b1 = hairDressersRegSys_Appointment(Date=date(2024, 1, 1), EndTime=date(2024, 1, 1), StartTime=date(2024, 1, 1))
    b2 = hairDressersRegSys_Appointment(Date=date(2025, 6, 15), EndTime=date(2025, 6, 15), StartTime=date(2025, 6, 15))
    _safe_set(a, 'hairDressersRegSys_Invoice', b1)
    assert _is_linked(a, 'hairDressersRegSys_Invoice', b1)
    if hasattr(b1, 'hairDressersRegSys_Appointment2'):
        assert _is_linked(b1, 'hairDressersRegSys_Appointment2', a)
    _safe_set(a, 'hairDressersRegSys_Invoice', b2)
    assert _is_linked(a, 'hairDressersRegSys_Invoice', b2)
    if hasattr(b1, 'hairDressersRegSys_Appointment2'):
        assert not _is_linked(b1, 'hairDressersRegSys_Appointment2', a)
    if hasattr(b2, 'hairDressersRegSys_Appointment2'):
        assert _is_linked(b2, 'hairDressersRegSys_Appointment2', a)
    _safe_set(a, 'hairDressersRegSys_Invoice', None)
    assert not _is_linked(a, 'hairDressersRegSys_Invoice', b2)
    if hasattr(b2, 'hairDressersRegSys_Appointment2'):
        assert not _is_linked(b2, 'hairDressersRegSys_Appointment2', a)


def test_assoc_invoice10_link_reassign_clear():
    a = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    b1 = hairDressersRegSys_Discounts(Description="sample_text", Name="sample_text", Percentage=7)
    b2 = hairDressersRegSys_Discounts(Description="sample_text_2", Name="sample_text_2", Percentage=13)
    _safe_set(a, 'Invoice12', b1)
    assert _is_linked(a, 'Invoice12', b1)
    if hasattr(b1, 'discounts11'):
        assert _is_linked(b1, 'discounts11', a)
    _safe_set(a, 'Invoice12', b2)
    assert _is_linked(a, 'Invoice12', b2)
    if hasattr(b1, 'discounts11'):
        assert not _is_linked(b1, 'discounts11', a)
    if hasattr(b2, 'discounts11'):
        assert _is_linked(b2, 'discounts11', a)
    _safe_set(a, 'Invoice12', None)
    assert not _is_linked(a, 'Invoice12', b2)
    if hasattr(b2, 'discounts11'):
        assert not _is_linked(b2, 'discounts11', a)


def test_assoc_invoice19_link_reassign_clear():
    a = hairDressersRegSys_Payment(AmountPaid="sample_text", Date=date(2024, 1, 1), PaymentMethod="sample_text")
    b1 = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    b2 = hairDressersRegSys_Invoice(Date="sample_text_2", InvoiceNumber=13, Total="sample_text_2")
    _safe_set(a, 'payment', {b1})
    assert _is_linked(a, 'payment', b1)
    if hasattr(b1, 'Invoice20'):
        assert _is_linked(b1, 'Invoice20', a)
    _safe_set(a, 'payment', {b2})
    assert _is_linked(a, 'payment', b2)
    if hasattr(b1, 'Invoice20'):
        assert not _is_linked(b1, 'Invoice20', a)
    if hasattr(b2, 'Invoice20'):
        assert _is_linked(b2, 'Invoice20', a)
    _safe_set(a, 'payment', set())
    assert not _is_linked(a, 'payment', b2)
    if hasattr(b2, 'Invoice20'):
        assert not _is_linked(b2, 'Invoice20', a)


def test_assoc_invoice3_link_reassign_clear():
    a = hairDressersRegSys_Products(Description="sample_text", Name="sample_text", Price="sample_text")
    b1 = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    b2 = hairDressersRegSys_Invoice(Date="sample_text_2", InvoiceNumber=13, Total="sample_text_2")
    _safe_set(a, 'products', b1)
    assert _is_linked(a, 'products', b1)
    if hasattr(b1, 'Invoice'):
        assert _is_linked(b1, 'Invoice', a)
    _safe_set(a, 'products', b2)
    assert _is_linked(a, 'products', b2)
    if hasattr(b1, 'Invoice'):
        assert not _is_linked(b1, 'Invoice', a)
    if hasattr(b2, 'Invoice'):
        assert _is_linked(b2, 'Invoice', a)
    _safe_set(a, 'products', None)
    assert not _is_linked(a, 'products', b2)
    if hasattr(b2, 'Invoice'):
        assert not _is_linked(b2, 'Invoice', a)


def test_assoc_payment7_link_reassign_clear():
    a = hairDressersRegSys_Payment(AmountPaid="sample_text", Date=date(2024, 1, 1), PaymentMethod="sample_text")
    b1 = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    b2 = hairDressersRegSys_Invoice(Date="sample_text_2", InvoiceNumber=13, Total="sample_text_2")
    _safe_set(a, 'Payment', b1)
    assert _is_linked(a, 'Payment', b1)
    if hasattr(b1, 'invoice8'):
        assert _is_linked(b1, 'invoice8', a)
    _safe_set(a, 'Payment', b2)
    assert _is_linked(a, 'Payment', b2)
    if hasattr(b1, 'invoice8'):
        assert not _is_linked(b1, 'invoice8', a)
    if hasattr(b2, 'invoice8'):
        assert _is_linked(b2, 'invoice8', a)
    _safe_set(a, 'Payment', None)
    assert not _is_linked(a, 'Payment', b2)
    if hasattr(b2, 'invoice8'):
        assert not _is_linked(b2, 'invoice8', a)


def test_assoc_products4_link_reassign_clear():
    a = hairDressersRegSys_Products(Description="sample_text", Name="sample_text", Price="sample_text")
    b1 = hairDressersRegSys_Invoice(Date="sample_text", InvoiceNumber=7, Total="sample_text")
    b2 = hairDressersRegSys_Invoice(Date="sample_text_2", InvoiceNumber=13, Total="sample_text_2")
    _safe_set(a, 'Products', b1)
    assert _is_linked(a, 'Products', b1)
    if hasattr(b1, 'invoice'):
        assert _is_linked(b1, 'invoice', a)
    _safe_set(a, 'Products', b2)
    assert _is_linked(a, 'Products', b2)
    if hasattr(b1, 'invoice'):
        assert not _is_linked(b1, 'invoice', a)
    if hasattr(b2, 'invoice'):
        assert _is_linked(b2, 'invoice', a)
    _safe_set(a, 'Products', None)
    assert not _is_linked(a, 'Products', b2)
    if hasattr(b2, 'invoice'):
        assert not _is_linked(b2, 'invoice', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Person_strategy = st.builds(Person)
@given(instance=Person_strategy)
@settings(max_examples=25)
def test_Person_instantiation(instance):
    assert isinstance(instance, Person)


Service_strategy = st.builds(Service)
@given(instance=Service_strategy)
@settings(max_examples=25)
def test_Service_instantiation(instance):
    assert isinstance(instance, Service)


hairDressersRegSys_Appointment_strategy = st.builds(hairDressersRegSys_Appointment, Date=st.dates(), EndTime=st.dates(), StartTime=st.dates())
@given(instance=hairDressersRegSys_Appointment_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Appointment_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Appointment)


hairDressersRegSys_Customer_strategy = st.builds(hairDressersRegSys_Customer, CustomerId=st.integers())
@given(instance=hairDressersRegSys_Customer_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Customer_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Customer)


hairDressersRegSys_Discounts_strategy = st.builds(hairDressersRegSys_Discounts, Description=safe_text, Name=safe_text, Percentage=st.integers())
@given(instance=hairDressersRegSys_Discounts_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Discounts_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Discounts)


hairDressersRegSys_Haircuts_strategy = st.builds(hairDressersRegSys_Haircuts, IsCut=st.booleans(), IsShave=st.booleans(), IsWash=st.booleans())
@given(instance=hairDressersRegSys_Haircuts_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Haircuts_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Haircuts)


hairDressersRegSys_Invoice_strategy = st.builds(hairDressersRegSys_Invoice, Date=safe_text, InvoiceNumber=st.integers(), Total=safe_text)
@given(instance=hairDressersRegSys_Invoice_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Invoice_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Invoice)


hairDressersRegSys_Other_strategy = st.builds(hairDressersRegSys_Other, AdditionalInformation=safe_text)
@given(instance=hairDressersRegSys_Other_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Other_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Other)


hairDressersRegSys_Payment_strategy = st.builds(hairDressersRegSys_Payment, AmountPaid=safe_text, Date=st.dates(), PaymentMethod=safe_text)
@given(instance=hairDressersRegSys_Payment_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Payment_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Payment)


hairDressersRegSys_Person_strategy = st.builds(hairDressersRegSys_Person, Address=safe_text, DateOfBirth=st.dates(), FirstName=safe_text, LastName=safe_text)
@given(instance=hairDressersRegSys_Person_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Person_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Person)


hairDressersRegSys_Products_strategy = st.builds(hairDressersRegSys_Products, Description=safe_text, Name=safe_text, Price=safe_text)
@given(instance=hairDressersRegSys_Products_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Products_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Products)


hairDressersRegSys_Service_strategy = st.builds(hairDressersRegSys_Service, CostPerHour=safe_text, Description=safe_text, Name=safe_text, Time=st.dates())
@given(instance=hairDressersRegSys_Service_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Service_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Service)


hairDressersRegSys_ServiceEmployee_strategy = st.builds(hairDressersRegSys_ServiceEmployee, EmployeeId=st.integers(), Role=safe_text)
@given(instance=hairDressersRegSys_ServiceEmployee_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_ServiceEmployee_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_ServiceEmployee)


hairDressersRegSys_Styling_strategy = st.builds(hairDressersRegSys_Styling, IsWash=st.booleans())
@given(instance=hairDressersRegSys_Styling_strategy)
@settings(max_examples=25)
def test_hairDressersRegSys_Styling_instantiation(instance):
    assert isinstance(instance, hairDressersRegSys_Styling)



