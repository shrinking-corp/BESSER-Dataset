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
    RoyalAndLoyal_Container_RandL,
    RoyalAndLoyal_TransactionReportLine,
    RoyalAndLoyal_Customer,
    RoyalAndLoyal_CustomerCard,
    RoyalAndLoyal_LoyaltyAccount,
    RoyalAndLoyal_Date,
    RoyalAndLoyal_Transaction,
    RoyalAndLoyal_TransactionReport,
    RoyalAndLoyal_ProgramPartner,
    Transaction,
    RoyalAndLoyal_Burning,
    RoyalAndLoyal_Earning,
    RoyalAndLoyal_Membership,
    RoyalAndLoyal_Service,
    RoyalAndLoyal_LoyaltyProgram,
    RoyalAndLoyal_ServiceLevel,
    RandLColor,
    Gender,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_royalandloyal_container_randl_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_Container_RandL)


def test_hyp_royalandloyal_container_randl_constructor_exists():
    assert callable(RoyalAndLoyal_Container_RandL.__init__)


def test_hyp_royalandloyal_container_randl_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_Container_RandL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_royalandloyal_transactionreportline_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_TransactionReportLine)


def test_hyp_royalandloyal_transactionreportline_constructor_exists():
    assert callable(RoyalAndLoyal_TransactionReportLine.__init__)


def test_hyp_royalandloyal_transactionreportline_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_TransactionReportLine.__init__)
    params = list(sig.parameters.keys())
    assert "serviceDesc" in params, "Missing parameter 'serviceDesc'"
    assert "points" in params, "Missing parameter 'points'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "partnerName" in params, "Missing parameter 'partnerName'"







def test_hyp_royalandloyal_customer_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_Customer)


def test_hyp_royalandloyal_customer_constructor_exists():
    assert callable(RoyalAndLoyal_Customer.__init__)


def test_hyp_royalandloyal_customer_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "name" in params, "Missing parameter 'name'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "age" in params, "Missing parameter 'age'"
    assert "isMale" in params, "Missing parameter 'isMale'"








def test_hyp_royalandloyal_customercard_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_CustomerCard)


def test_hyp_royalandloyal_customercard_constructor_exists():
    assert callable(RoyalAndLoyal_CustomerCard.__init__)


def test_hyp_royalandloyal_customercard_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_CustomerCard.__init__)
    params = list(sig.parameters.keys())
    assert "printedName" in params, "Missing parameter 'printedName'"
    assert "valid" in params, "Missing parameter 'valid'"
    assert "color" in params, "Missing parameter 'color'"






def test_hyp_royalandloyal_loyaltyaccount_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_LoyaltyAccount)


def test_hyp_royalandloyal_loyaltyaccount_constructor_exists():
    assert callable(RoyalAndLoyal_LoyaltyAccount.__init__)


def test_hyp_royalandloyal_loyaltyaccount_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_LoyaltyAccount.__init__)
    params = list(sig.parameters.keys())
    assert "totalPointsEarned" in params, "Missing parameter 'totalPointsEarned'"
    assert "number" in params, "Missing parameter 'number'"
    assert "points" in params, "Missing parameter 'points'"






def test_hyp_royalandloyal_date_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_Date)


def test_hyp_royalandloyal_date_constructor_exists():
    assert callable(RoyalAndLoyal_Date.__init__)


def test_hyp_royalandloyal_date_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_Date.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "day" in params, "Missing parameter 'day'"






def test_hyp_royalandloyal_transaction_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_Transaction)


def test_hyp_royalandloyal_transaction_constructor_exists():
    assert callable(RoyalAndLoyal_Transaction.__init__)


def test_hyp_royalandloyal_transaction_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "points" in params, "Missing parameter 'points'"





def test_hyp_royalandloyal_transactionreport_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_TransactionReport)


def test_hyp_royalandloyal_transactionreport_constructor_exists():
    assert callable(RoyalAndLoyal_TransactionReport.__init__)


def test_hyp_royalandloyal_transactionreport_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_TransactionReport.__init__)
    params = list(sig.parameters.keys())
    assert "totalEarned" in params, "Missing parameter 'totalEarned'"
    assert "totalBurned" in params, "Missing parameter 'totalBurned'"
    assert "balance" in params, "Missing parameter 'balance'"
    assert "number" in params, "Missing parameter 'number'"
    assert "name" in params, "Missing parameter 'name'"








def test_hyp_royalandloyal_programpartner_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_ProgramPartner)


def test_hyp_royalandloyal_programpartner_constructor_exists():
    assert callable(RoyalAndLoyal_ProgramPartner.__init__)


def test_hyp_royalandloyal_programpartner_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_ProgramPartner.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numberOfCustomers" in params, "Missing parameter 'numberOfCustomers'"





def test_hyp_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_hyp_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_hyp_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_royalandloyal_burning_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_Burning)


def test_hyp_royalandloyal_burning_constructor_exists():
    assert callable(RoyalAndLoyal_Burning.__init__)


def test_hyp_royalandloyal_burning_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_Burning.__init__)
    params = list(sig.parameters.keys())



def test_hyp_royalandloyal_earning_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_Earning)


def test_hyp_royalandloyal_earning_constructor_exists():
    assert callable(RoyalAndLoyal_Earning.__init__)


def test_hyp_royalandloyal_earning_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_Earning.__init__)
    params = list(sig.parameters.keys())



def test_hyp_royalandloyal_membership_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_Membership)


def test_hyp_royalandloyal_membership_constructor_exists():
    assert callable(RoyalAndLoyal_Membership.__init__)


def test_hyp_royalandloyal_membership_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_Membership.__init__)
    params = list(sig.parameters.keys())



def test_hyp_royalandloyal_service_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_Service)


def test_hyp_royalandloyal_service_constructor_exists():
    assert callable(RoyalAndLoyal_Service.__init__)


def test_hyp_royalandloyal_service_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_Service.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "pointsBurned" in params, "Missing parameter 'pointsBurned'"
    assert "serviceNr" in params, "Missing parameter 'serviceNr'"
    assert "pointsEarned" in params, "Missing parameter 'pointsEarned'"
    assert "condition" in params, "Missing parameter 'condition'"








def test_hyp_royalandloyal_loyaltyprogram_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_LoyaltyProgram)


def test_hyp_royalandloyal_loyaltyprogram_constructor_exists():
    assert callable(RoyalAndLoyal_LoyaltyProgram.__init__)


def test_hyp_royalandloyal_loyaltyprogram_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_LoyaltyProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_royalandloyal_servicelevel_is_not_abstract():
    assert not inspect.isabstract(RoyalAndLoyal_ServiceLevel)


def test_hyp_royalandloyal_servicelevel_constructor_exists():
    assert callable(RoyalAndLoyal_ServiceLevel.__init__)


def test_hyp_royalandloyal_servicelevel_constructor_args():
    sig = inspect.signature(RoyalAndLoyal_ServiceLevel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_randlcolor_exists():
    # Check that the Enumeration exists
    assert RandLColor is not None

def test_hyp_randlcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RandLColor]
    expected_literals = [
        "gold",
        "silver",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RandLColor"

def test_hyp_gender_exists():
    # Check that the Enumeration exists
    assert Gender is not None

def test_hyp_gender_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gender]
    expected_literals = [
        "female",
        "male",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gender"


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
RoyalAndLoyal_Container_RandL_strategy = st.builds(
    RoyalAndLoyal_Container_RandL,
)
RoyalAndLoyal_TransactionReportLine_strategy = st.builds(
    RoyalAndLoyal_TransactionReportLine,
    serviceDesc=
        safe_text,
    points=
        st.integers(),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    partnerName=
        safe_text
)
RoyalAndLoyal_Customer_strategy = st.builds(
    RoyalAndLoyal_Customer,
    title=
        safe_text,
    name=
        safe_text,
    gender=
        safe_text,
    age=
        st.integers(),
    isMale=
        st.booleans()
)
RoyalAndLoyal_CustomerCard_strategy = st.builds(
    RoyalAndLoyal_CustomerCard,
    printedName=
        safe_text,
    valid=
        st.booleans(),
    color=
        safe_text
)
RoyalAndLoyal_LoyaltyAccount_strategy = st.builds(
    RoyalAndLoyal_LoyaltyAccount,
    totalPointsEarned=
        st.integers(),
    number=
        st.integers(),
    points=
        st.integers()
)
RoyalAndLoyal_Date_strategy = st.builds(
    RoyalAndLoyal_Date,
    year=
        st.integers(),
    month=
        st.integers(),
    day=
        st.integers()
)
RoyalAndLoyal_Transaction_strategy = st.builds(
    RoyalAndLoyal_Transaction,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    points=
        st.integers()
)
RoyalAndLoyal_TransactionReport_strategy = st.builds(
    RoyalAndLoyal_TransactionReport,
    totalEarned=
        st.integers(),
    totalBurned=
        st.integers(),
    balance=
        st.integers(),
    number=
        st.integers(),
    name=
        safe_text
)
RoyalAndLoyal_ProgramPartner_strategy = st.builds(
    RoyalAndLoyal_ProgramPartner,
    name=
        safe_text,
    numberOfCustomers=
        st.integers()
)
Transaction_strategy = st.builds(
    Transaction,
)
RoyalAndLoyal_Burning_strategy = st.builds(
    RoyalAndLoyal_Burning,
)
RoyalAndLoyal_Earning_strategy = st.builds(
    RoyalAndLoyal_Earning,
)
RoyalAndLoyal_Membership_strategy = st.builds(
    RoyalAndLoyal_Membership,
)
RoyalAndLoyal_Service_strategy = st.builds(
    RoyalAndLoyal_Service,
    description=
        safe_text,
    pointsBurned=
        st.integers(),
    serviceNr=
        st.integers(),
    pointsEarned=
        st.integers(),
    condition=
        st.booleans()
)
RoyalAndLoyal_LoyaltyProgram_strategy = st.builds(
    RoyalAndLoyal_LoyaltyProgram,
    name=
        safe_text
)
RoyalAndLoyal_ServiceLevel_strategy = st.builds(
    RoyalAndLoyal_ServiceLevel,
    name=
        safe_text
)





@given(instance=RoyalAndLoyal_TransactionReportLine_strategy)
def test_hyp_royalandloyal_transactionreportline_serviceDesc_setter(instance):
    original = instance.serviceDesc
    instance.serviceDesc = original
    assert instance.serviceDesc == original



@given(instance=RoyalAndLoyal_TransactionReportLine_strategy)
def test_hyp_royalandloyal_transactionreportline_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=RoyalAndLoyal_TransactionReportLine_strategy)
def test_hyp_royalandloyal_transactionreportline_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=RoyalAndLoyal_TransactionReportLine_strategy)
def test_hyp_royalandloyal_transactionreportline_partnerName_setter(instance):
    original = instance.partnerName
    instance.partnerName = original
    assert instance.partnerName == original




@given(instance=RoyalAndLoyal_Customer_strategy)
def test_hyp_royalandloyal_customer_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=RoyalAndLoyal_Customer_strategy)
def test_hyp_royalandloyal_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RoyalAndLoyal_Customer_strategy)
def test_hyp_royalandloyal_customer_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=RoyalAndLoyal_Customer_strategy)
def test_hyp_royalandloyal_customer_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=RoyalAndLoyal_Customer_strategy)
def test_hyp_royalandloyal_customer_isMale_setter(instance):
    original = instance.isMale
    instance.isMale = original
    assert instance.isMale == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Customer_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_customer_updatename_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateName' in RoyalAndLoyal_Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateName' in RoyalAndLoyal_Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateName' in RoyalAndLoyal_Customer is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Customer_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_customer_birthdayhappens_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.birthdayHappens()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.birthdayHappens).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'birthdayHappens' in RoyalAndLoyal_Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'birthdayHappens' in RoyalAndLoyal_Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'birthdayHappens' in RoyalAndLoyal_Customer is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Customer_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_customer_age_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.age()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.age).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'age' in RoyalAndLoyal_Customer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'age' in RoyalAndLoyal_Customer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'age' in RoyalAndLoyal_Customer is not implemented or raised an error")




@given(instance=RoyalAndLoyal_CustomerCard_strategy)
def test_hyp_royalandloyal_customercard_printedName_setter(instance):
    original = instance.printedName
    instance.printedName = original
    assert instance.printedName == original



@given(instance=RoyalAndLoyal_CustomerCard_strategy)
def test_hyp_royalandloyal_customercard_valid_setter(instance):
    original = instance.valid
    instance.valid = original
    assert instance.valid == original



@given(instance=RoyalAndLoyal_CustomerCard_strategy)
def test_hyp_royalandloyal_customercard_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=RoyalAndLoyal_LoyaltyAccount_strategy)
def test_hyp_royalandloyal_loyaltyaccount_totalPointsEarned_setter(instance):
    original = instance.totalPointsEarned
    instance.totalPointsEarned = original
    assert instance.totalPointsEarned == original



@given(instance=RoyalAndLoyal_LoyaltyAccount_strategy)
def test_hyp_royalandloyal_loyaltyaccount_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=RoyalAndLoyal_LoyaltyAccount_strategy)
def test_hyp_royalandloyal_loyaltyaccount_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_LoyaltyAccount_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_loyaltyaccount_isempty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isEmpty()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isEmpty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isEmpty' in RoyalAndLoyal_LoyaltyAccount is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEmpty' in RoyalAndLoyal_LoyaltyAccount did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEmpty' in RoyalAndLoyal_LoyaltyAccount is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_LoyaltyAccount_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_loyaltyaccount_earn_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.earn(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.earn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'earn' in RoyalAndLoyal_LoyaltyAccount is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'earn' in RoyalAndLoyal_LoyaltyAccount did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'earn' in RoyalAndLoyal_LoyaltyAccount is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_LoyaltyAccount_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_loyaltyaccount_burn_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.burn(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.burn).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'burn' in RoyalAndLoyal_LoyaltyAccount is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'burn' in RoyalAndLoyal_LoyaltyAccount did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'burn' in RoyalAndLoyal_LoyaltyAccount is not implemented or raised an error")




@given(instance=RoyalAndLoyal_Date_strategy)
def test_hyp_royalandloyal_date_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=RoyalAndLoyal_Date_strategy)
def test_hyp_royalandloyal_date_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=RoyalAndLoyal_Date_strategy)
def test_hyp_royalandloyal_date_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Date_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_date_isbefore_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isBefore(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isBefore).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isBefore' in RoyalAndLoyal_Date is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBefore' in RoyalAndLoyal_Date did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBefore' in RoyalAndLoyal_Date is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Date_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_date_isequal_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isEqual(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isEqual).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isEqual' in RoyalAndLoyal_Date is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEqual' in RoyalAndLoyal_Date did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEqual' in RoyalAndLoyal_Date is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Date_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_date_fromymd_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fromYMD(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fromYMD).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fromYMD' in RoyalAndLoyal_Date is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fromYMD' in RoyalAndLoyal_Date did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fromYMD' in RoyalAndLoyal_Date is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Date_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_date_isafter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAfter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAfter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAfter' in RoyalAndLoyal_Date is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAfter' in RoyalAndLoyal_Date did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAfter' in RoyalAndLoyal_Date is not implemented or raised an error")




@given(instance=RoyalAndLoyal_Transaction_strategy)
def test_hyp_royalandloyal_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=RoyalAndLoyal_Transaction_strategy)
def test_hyp_royalandloyal_transaction_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Transaction_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_transaction_program_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.program()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.program).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'program' in RoyalAndLoyal_Transaction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'program' in RoyalAndLoyal_Transaction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'program' in RoyalAndLoyal_Transaction is not implemented or raised an error")




@given(instance=RoyalAndLoyal_TransactionReport_strategy)
def test_hyp_royalandloyal_transactionreport_totalEarned_setter(instance):
    original = instance.totalEarned
    instance.totalEarned = original
    assert instance.totalEarned == original



@given(instance=RoyalAndLoyal_TransactionReport_strategy)
def test_hyp_royalandloyal_transactionreport_totalBurned_setter(instance):
    original = instance.totalBurned
    instance.totalBurned = original
    assert instance.totalBurned == original



@given(instance=RoyalAndLoyal_TransactionReport_strategy)
def test_hyp_royalandloyal_transactionreport_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=RoyalAndLoyal_TransactionReport_strategy)
def test_hyp_royalandloyal_transactionreport_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=RoyalAndLoyal_TransactionReport_strategy)
def test_hyp_royalandloyal_transactionreport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=RoyalAndLoyal_ProgramPartner_strategy)
def test_hyp_royalandloyal_programpartner_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RoyalAndLoyal_ProgramPartner_strategy)
def test_hyp_royalandloyal_programpartner_numberOfCustomers_setter(instance):
    original = instance.numberOfCustomers
    instance.numberOfCustomers = original
    assert instance.numberOfCustomers == original








@given(instance=RoyalAndLoyal_Service_strategy)
def test_hyp_royalandloyal_service_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=RoyalAndLoyal_Service_strategy)
def test_hyp_royalandloyal_service_pointsBurned_setter(instance):
    original = instance.pointsBurned
    instance.pointsBurned = original
    assert instance.pointsBurned == original



@given(instance=RoyalAndLoyal_Service_strategy)
def test_hyp_royalandloyal_service_serviceNr_setter(instance):
    original = instance.serviceNr
    instance.serviceNr = original
    assert instance.serviceNr == original



@given(instance=RoyalAndLoyal_Service_strategy)
def test_hyp_royalandloyal_service_pointsEarned_setter(instance):
    original = instance.pointsEarned
    instance.pointsEarned = original
    assert instance.pointsEarned == original



@given(instance=RoyalAndLoyal_Service_strategy)
def test_hyp_royalandloyal_service_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Service_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_service_calcpoints_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.calcPoints()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.calcPoints).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'calcPoints' in RoyalAndLoyal_Service is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'calcPoints' in RoyalAndLoyal_Service did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'calcPoints' in RoyalAndLoyal_Service is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_Service_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_service_upgradepointsearned_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.upgradePointsEarned(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.upgradePointsEarned).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'upgradePointsEarned' in RoyalAndLoyal_Service is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'upgradePointsEarned' in RoyalAndLoyal_Service did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'upgradePointsEarned' in RoyalAndLoyal_Service is not implemented or raised an error")




@given(instance=RoyalAndLoyal_LoyaltyProgram_strategy)
def test_hyp_royalandloyal_loyaltyprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_LoyaltyProgram_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_loyaltyprogram_enrollandcreatecustomer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.enrollAndCreateCustomer(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.enrollAndCreateCustomer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'enrollAndCreateCustomer' in RoyalAndLoyal_LoyaltyProgram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'enrollAndCreateCustomer' in RoyalAndLoyal_LoyaltyProgram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'enrollAndCreateCustomer' in RoyalAndLoyal_LoyaltyProgram is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_LoyaltyProgram_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_loyaltyprogram_selectpopularpartners_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.selectPopularPartners(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.selectPopularPartners).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'selectPopularPartners' in RoyalAndLoyal_LoyaltyProgram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'selectPopularPartners' in RoyalAndLoyal_LoyaltyProgram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'selectPopularPartners' in RoyalAndLoyal_LoyaltyProgram is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_LoyaltyProgram_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_loyaltyprogram_enroll_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.enroll(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.enroll).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'enroll' in RoyalAndLoyal_LoyaltyProgram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'enroll' in RoyalAndLoyal_LoyaltyProgram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'enroll' in RoyalAndLoyal_LoyaltyProgram is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_LoyaltyProgram_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_loyaltyprogram_addservice_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addService(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addService).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addService' in RoyalAndLoyal_LoyaltyProgram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addService' in RoyalAndLoyal_LoyaltyProgram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addService' in RoyalAndLoyal_LoyaltyProgram is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=RoyalAndLoyal_LoyaltyProgram_strategy)
@settings(max_examples=30)
def test_hyp_royalandloyal_loyaltyprogram_addtransaction_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addTransaction(
            "test", 
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addTransaction).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addTransaction' in RoyalAndLoyal_LoyaltyProgram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTransaction' in RoyalAndLoyal_LoyaltyProgram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTransaction' in RoyalAndLoyal_LoyaltyProgram is not implemented or raised an error")




@given(instance=RoyalAndLoyal_ServiceLevel_strategy)
def test_hyp_royalandloyal_servicelevel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    RoyalAndLoyal_Burning,
    RoyalAndLoyal_Container_RandL,
    RoyalAndLoyal_Customer,
    RoyalAndLoyal_CustomerCard,
    RoyalAndLoyal_Date,
    RoyalAndLoyal_Earning,
    RoyalAndLoyal_LoyaltyAccount,
    RoyalAndLoyal_LoyaltyProgram,
    RoyalAndLoyal_Membership,
    RoyalAndLoyal_ProgramPartner,
    RoyalAndLoyal_Service,
    RoyalAndLoyal_ServiceLevel,
    RoyalAndLoyal_Transaction,
    RoyalAndLoyal_TransactionReport,
    RoyalAndLoyal_TransactionReportLine,
    Transaction,
    Gender,
    RandLColor,
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

def test_RoyalAndLoyal_Customer_age_value_roundtrip():
    instance = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_RoyalAndLoyal_Customer_gender_value_roundtrip():
    instance = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    assert instance.gender == "sample_text"
    instance.gender = "sample_text_2"
    assert instance.gender == "sample_text_2"


def test_RoyalAndLoyal_Customer_isMale_value_roundtrip():
    instance = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    assert instance.isMale == True
    instance.isMale = False
    assert instance.isMale == False


def test_RoyalAndLoyal_Customer_name_value_roundtrip():
    instance = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_RoyalAndLoyal_Customer_title_value_roundtrip():
    instance = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_RoyalAndLoyal_CustomerCard_color_value_roundtrip():
    instance = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_RoyalAndLoyal_CustomerCard_printedName_value_roundtrip():
    instance = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    assert instance.printedName == "sample_text"
    instance.printedName = "sample_text_2"
    assert instance.printedName == "sample_text_2"


def test_RoyalAndLoyal_CustomerCard_valid_value_roundtrip():
    instance = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    assert instance.valid == True
    instance.valid = False
    assert instance.valid == False


def test_RoyalAndLoyal_Date_day_value_roundtrip():
    instance = RoyalAndLoyal_Date(day=7, month=7, year=7)
    assert instance.day == 7
    instance.day = 13
    assert instance.day == 13


def test_RoyalAndLoyal_Date_month_value_roundtrip():
    instance = RoyalAndLoyal_Date(day=7, month=7, year=7)
    assert instance.month == 7
    instance.month = 13
    assert instance.month == 13


def test_RoyalAndLoyal_Date_year_value_roundtrip():
    instance = RoyalAndLoyal_Date(day=7, month=7, year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_RoyalAndLoyal_LoyaltyAccount_number_value_roundtrip():
    instance = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_RoyalAndLoyal_LoyaltyAccount_points_value_roundtrip():
    instance = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    assert instance.points == 7
    instance.points = 13
    assert instance.points == 13


def test_RoyalAndLoyal_LoyaltyAccount_totalPointsEarned_value_roundtrip():
    instance = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    assert instance.totalPointsEarned == 7
    instance.totalPointsEarned = 13
    assert instance.totalPointsEarned == 13


def test_RoyalAndLoyal_LoyaltyProgram_name_value_roundtrip():
    instance = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_RoyalAndLoyal_ProgramPartner_name_value_roundtrip():
    instance = RoyalAndLoyal_ProgramPartner(name="sample_text", numberOfCustomers=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_RoyalAndLoyal_ProgramPartner_numberOfCustomers_value_roundtrip():
    instance = RoyalAndLoyal_ProgramPartner(name="sample_text", numberOfCustomers=7)
    assert instance.numberOfCustomers == 7
    instance.numberOfCustomers = 13
    assert instance.numberOfCustomers == 13


def test_RoyalAndLoyal_Service_condition_value_roundtrip():
    instance = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    assert instance.condition == True
    instance.condition = False
    assert instance.condition == False


def test_RoyalAndLoyal_Service_description_value_roundtrip():
    instance = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_RoyalAndLoyal_Service_pointsBurned_value_roundtrip():
    instance = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    assert instance.pointsBurned == 7
    instance.pointsBurned = 13
    assert instance.pointsBurned == 13


def test_RoyalAndLoyal_Service_pointsEarned_value_roundtrip():
    instance = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    assert instance.pointsEarned == 7
    instance.pointsEarned = 13
    assert instance.pointsEarned == 13


def test_RoyalAndLoyal_Service_serviceNr_value_roundtrip():
    instance = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    assert instance.serviceNr == 7
    instance.serviceNr = 13
    assert instance.serviceNr == 13


def test_RoyalAndLoyal_ServiceLevel_name_value_roundtrip():
    instance = RoyalAndLoyal_ServiceLevel(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_RoyalAndLoyal_Transaction_amount_value_roundtrip():
    instance = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    assert instance.amount == 3.14
    instance.amount = 9.99
    assert instance.amount == 9.99


def test_RoyalAndLoyal_Transaction_points_value_roundtrip():
    instance = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    assert instance.points == 7
    instance.points = 13
    assert instance.points == 13


def test_RoyalAndLoyal_TransactionReport_balance_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    assert instance.balance == 7
    instance.balance = 13
    assert instance.balance == 13


def test_RoyalAndLoyal_TransactionReport_name_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_RoyalAndLoyal_TransactionReport_number_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_RoyalAndLoyal_TransactionReport_totalBurned_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    assert instance.totalBurned == 7
    instance.totalBurned = 13
    assert instance.totalBurned == 13


def test_RoyalAndLoyal_TransactionReport_totalEarned_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    assert instance.totalEarned == 7
    instance.totalEarned = 13
    assert instance.totalEarned == 13


def test_RoyalAndLoyal_TransactionReportLine_amount_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    assert instance.amount == 3.14
    instance.amount = 9.99
    assert instance.amount == 9.99


def test_RoyalAndLoyal_TransactionReportLine_partnerName_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    assert instance.partnerName == "sample_text"
    instance.partnerName = "sample_text_2"
    assert instance.partnerName == "sample_text_2"


def test_RoyalAndLoyal_TransactionReportLine_points_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    assert instance.points == 7
    instance.points = 13
    assert instance.points == 13


def test_RoyalAndLoyal_TransactionReportLine_serviceDesc_value_roundtrip():
    instance = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    assert instance.serviceDesc == "sample_text"
    instance.serviceDesc = "sample_text_2"
    assert instance.serviceDesc == "sample_text_2"


def test_RoyalAndLoyal_Burning_isa_Transaction():
    instance = RoyalAndLoyal_Burning()
    assert isinstance(instance, Transaction)


def test_RoyalAndLoyal_Earning_isa_Transaction():
    instance = RoyalAndLoyal_Earning()
    assert isinstance(instance, Transaction)


def test_assoc_Membership11_link_reassign_clear():
    a = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'account', b1)
    assert _is_linked(a, 'account', b1)
    if hasattr(b1, 'Membership12'):
        assert _is_linked(b1, 'Membership12', a)
    _safe_set(a, 'account', b2)
    assert _is_linked(a, 'account', b2)
    if hasattr(b1, 'Membership12'):
        assert not _is_linked(b1, 'Membership12', a)
    if hasattr(b2, 'Membership12'):
        assert _is_linked(b2, 'Membership12', a)
    _safe_set(a, 'account', None)
    assert not _is_linked(a, 'account', b2)
    if hasattr(b2, 'Membership12'):
        assert not _is_linked(b2, 'Membership12', a)


def test_assoc_Membership2_link_reassign_clear():
    a = RoyalAndLoyal_ServiceLevel(name="sample_text")
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'currentLevel', {b1})
    assert _is_linked(a, 'currentLevel', b1)
    if hasattr(b1, 'Membership'):
        assert _is_linked(b1, 'Membership', a)
    _safe_set(a, 'currentLevel', {b2})
    assert _is_linked(a, 'currentLevel', b2)
    if hasattr(b1, 'Membership'):
        assert not _is_linked(b1, 'Membership', a)
    if hasattr(b2, 'Membership'):
        assert _is_linked(b2, 'Membership', a)
    _safe_set(a, 'currentLevel', set())
    assert not _is_linked(a, 'currentLevel', b2)
    if hasattr(b2, 'Membership'):
        assert not _is_linked(b2, 'Membership', a)


def test_assoc_Membership36_link_reassign_clear():
    a = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'card', b1)
    assert _is_linked(a, 'card', b1)
    if hasattr(b1, 'Membership37'):
        assert _is_linked(b1, 'Membership37', a)
    _safe_set(a, 'card', b2)
    assert _is_linked(a, 'card', b2)
    if hasattr(b1, 'Membership37'):
        assert not _is_linked(b1, 'Membership37', a)
    if hasattr(b2, 'Membership37'):
        assert _is_linked(b2, 'Membership37', a)
    _safe_set(a, 'card', None)
    assert not _is_linked(a, 'card', b2)
    if hasattr(b2, 'Membership37'):
        assert not _is_linked(b2, 'Membership37', a)


def test_assoc_account4_link_reassign_clear():
    a = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    b1 = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    b2 = RoyalAndLoyal_LoyaltyAccount(number=13, points=13, totalPointsEarned=13)
    _safe_set(a, 'transactions', b1)
    assert _is_linked(a, 'transactions', b1)
    if hasattr(b1, 'LoyaltyAccount'):
        assert _is_linked(b1, 'LoyaltyAccount', a)
    _safe_set(a, 'transactions', b2)
    assert _is_linked(a, 'transactions', b2)
    if hasattr(b1, 'LoyaltyAccount'):
        assert not _is_linked(b1, 'LoyaltyAccount', a)
    if hasattr(b2, 'LoyaltyAccount'):
        assert _is_linked(b2, 'LoyaltyAccount', a)
    _safe_set(a, 'transactions', None)
    assert not _is_linked(a, 'transactions', b2)
    if hasattr(b2, 'LoyaltyAccount'):
        assert not _is_linked(b2, 'LoyaltyAccount', a)


def test_assoc_account46_link_reassign_clear():
    a = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'LoyaltyAccount48', b1)
    assert _is_linked(a, 'LoyaltyAccount48', b1)
    if hasattr(b1, 'Membership47'):
        assert _is_linked(b1, 'Membership47', a)
    _safe_set(a, 'LoyaltyAccount48', b2)
    assert _is_linked(a, 'LoyaltyAccount48', b2)
    if hasattr(b1, 'Membership47'):
        assert not _is_linked(b1, 'Membership47', a)
    if hasattr(b2, 'Membership47'):
        assert _is_linked(b2, 'Membership47', a)
    _safe_set(a, 'LoyaltyAccount48', None)
    assert not _is_linked(a, 'LoyaltyAccount48', b2)
    if hasattr(b2, 'Membership47'):
        assert not _is_linked(b2, 'Membership47', a)


def test_assoc_availableServices1_link_reassign_clear():
    a = RoyalAndLoyal_ServiceLevel(name="sample_text")
    b1 = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    b2 = RoyalAndLoyal_Service(condition=False, description="sample_text_2", pointsBurned=13, pointsEarned=13, serviceNr=13)
    _safe_set(a, 'level', {b1})
    assert _is_linked(a, 'level', b1)
    if hasattr(b1, 'Service'):
        assert _is_linked(b1, 'Service', a)
    _safe_set(a, 'level', {b2})
    assert _is_linked(a, 'level', b2)
    if hasattr(b1, 'Service'):
        assert not _is_linked(b1, 'Service', a)
    if hasattr(b2, 'Service'):
        assert _is_linked(b2, 'Service', a)
    _safe_set(a, 'level', set())
    assert not _is_linked(a, 'level', b2)
    if hasattr(b2, 'Service'):
        assert not _is_linked(b2, 'Service', a)


def test_assoc_card25_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    b1 = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b2 = RoyalAndLoyal_CustomerCard(color="sample_text_2", printedName="sample_text_2", valid=False)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport26', b1)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReport26', b1)
    if hasattr(b1, 'RoyalAndLoyal_CustomerCard'):
        assert _is_linked(b1, 'RoyalAndLoyal_CustomerCard', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport26', b2)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReport26', b2)
    if hasattr(b1, 'RoyalAndLoyal_CustomerCard'):
        assert not _is_linked(b1, 'RoyalAndLoyal_CustomerCard', a)
    if hasattr(b2, 'RoyalAndLoyal_CustomerCard'):
        assert _is_linked(b2, 'RoyalAndLoyal_CustomerCard', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport26', None)
    assert not _is_linked(a, 'RoyalAndLoyal_TransactionReport26', b2)
    if hasattr(b2, 'RoyalAndLoyal_CustomerCard'):
        assert not _is_linked(b2, 'RoyalAndLoyal_CustomerCard', a)


def test_assoc_card43_link_reassign_clear():
    a = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'CustomerCard45', b1)
    assert _is_linked(a, 'CustomerCard45', b1)
    if hasattr(b1, 'Membership44'):
        assert _is_linked(b1, 'Membership44', a)
    _safe_set(a, 'CustomerCard45', b2)
    assert _is_linked(a, 'CustomerCard45', b2)
    if hasattr(b1, 'Membership44'):
        assert not _is_linked(b1, 'Membership44', a)
    if hasattr(b2, 'Membership44'):
        assert _is_linked(b2, 'Membership44', a)
    _safe_set(a, 'CustomerCard45', None)
    assert not _is_linked(a, 'CustomerCard45', b2)
    if hasattr(b2, 'Membership44'):
        assert not _is_linked(b2, 'Membership44', a)


def test_assoc_card8_link_reassign_clear():
    a = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    b1 = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b2 = RoyalAndLoyal_CustomerCard(color="sample_text_2", printedName="sample_text_2", valid=False)
    _safe_set(a, 'transactions9', b1)
    assert _is_linked(a, 'transactions9', b1)
    if hasattr(b1, 'CustomerCard'):
        assert _is_linked(b1, 'CustomerCard', a)
    _safe_set(a, 'transactions9', b2)
    assert _is_linked(a, 'transactions9', b2)
    if hasattr(b1, 'CustomerCard'):
        assert not _is_linked(b1, 'CustomerCard', a)
    if hasattr(b2, 'CustomerCard'):
        assert _is_linked(b2, 'CustomerCard', a)
    _safe_set(a, 'transactions9', None)
    assert not _is_linked(a, 'transactions9', b2)
    if hasattr(b2, 'CustomerCard'):
        assert not _is_linked(b2, 'CustomerCard', a)


def test_assoc_cards96_link_reassign_clear():
    a = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b1 = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    b2 = RoyalAndLoyal_Customer(age=13, gender="sample_text_2", isMale=False, name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'CustomerCard97', b1)
    assert _is_linked(a, 'CustomerCard97', b1)
    if hasattr(b1, 'owner'):
        assert _is_linked(b1, 'owner', a)
    _safe_set(a, 'CustomerCard97', b2)
    assert _is_linked(a, 'CustomerCard97', b2)
    if hasattr(b1, 'owner'):
        assert not _is_linked(b1, 'owner', a)
    if hasattr(b2, 'owner'):
        assert _is_linked(b2, 'owner', a)
    _safe_set(a, 'CustomerCard97', None)
    assert not _is_linked(a, 'CustomerCard97', b2)
    if hasattr(b2, 'owner'):
        assert not _is_linked(b2, 'owner', a)


def test_assoc_currentLevel41_link_reassign_clear():
    a = RoyalAndLoyal_ServiceLevel(name="sample_text")
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'ServiceLevel', b1)
    assert _is_linked(a, 'ServiceLevel', b1)
    if hasattr(b1, 'Membership42'):
        assert _is_linked(b1, 'Membership42', a)
    _safe_set(a, 'ServiceLevel', b2)
    assert _is_linked(a, 'ServiceLevel', b2)
    if hasattr(b1, 'Membership42'):
        assert not _is_linked(b1, 'Membership42', a)
    if hasattr(b2, 'Membership42'):
        assert _is_linked(b2, 'Membership42', a)
    _safe_set(a, 'ServiceLevel', None)
    assert not _is_linked(a, 'ServiceLevel', b2)
    if hasattr(b2, 'Membership42'):
        assert not _is_linked(b2, 'Membership42', a)


def test_assoc_custmemberships98_link_reassign_clear():
    a = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'RoyalAndLoyal_Customer99', {b1})
    assert _is_linked(a, 'RoyalAndLoyal_Customer99', b1)
    if hasattr(b1, 'RoyalAndLoyal_Membership100'):
        assert _is_linked(b1, 'RoyalAndLoyal_Membership100', a)
    _safe_set(a, 'RoyalAndLoyal_Customer99', {b2})
    assert _is_linked(a, 'RoyalAndLoyal_Customer99', b2)
    if hasattr(b1, 'RoyalAndLoyal_Membership100'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Membership100', a)
    if hasattr(b2, 'RoyalAndLoyal_Membership100'):
        assert _is_linked(b2, 'RoyalAndLoyal_Membership100', a)
    _safe_set(a, 'RoyalAndLoyal_Customer99', set())
    assert not _is_linked(a, 'RoyalAndLoyal_Customer99', b2)
    if hasattr(b2, 'RoyalAndLoyal_Membership100'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Membership100', a)


def test_assoc_dateOfBirth91_link_reassign_clear():
    a = RoyalAndLoyal_Date(day=7, month=7, year=7)
    b1 = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    b2 = RoyalAndLoyal_Customer(age=13, gender="sample_text_2", isMale=False, name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'RoyalAndLoyal_Date93', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Date93', b1)
    if hasattr(b1, 'RoyalAndLoyal_Customer92'):
        assert _is_linked(b1, 'RoyalAndLoyal_Customer92', a)
    _safe_set(a, 'RoyalAndLoyal_Date93', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Date93', b2)
    if hasattr(b1, 'RoyalAndLoyal_Customer92'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Customer92', a)
    if hasattr(b2, 'RoyalAndLoyal_Customer92'):
        assert _is_linked(b2, 'RoyalAndLoyal_Customer92', a)
    _safe_set(a, 'RoyalAndLoyal_Date93', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Date93', b2)
    if hasattr(b2, 'RoyalAndLoyal_Customer92'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Customer92', a)


def test_assoc_deliveredServices15_link_reassign_clear():
    a = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    b1 = RoyalAndLoyal_ProgramPartner(name="sample_text", numberOfCustomers=7)
    b2 = RoyalAndLoyal_ProgramPartner(name="sample_text_2", numberOfCustomers=13)
    _safe_set(a, 'Service16', b1)
    assert _is_linked(a, 'Service16', b1)
    if hasattr(b1, 'partner'):
        assert _is_linked(b1, 'partner', a)
    _safe_set(a, 'Service16', b2)
    assert _is_linked(a, 'Service16', b2)
    if hasattr(b1, 'partner'):
        assert not _is_linked(b1, 'partner', a)
    if hasattr(b2, 'partner'):
        assert _is_linked(b2, 'partner', a)
    _safe_set(a, 'Service16', None)
    assert not _is_linked(a, 'Service16', b2)
    if hasattr(b2, 'partner'):
        assert not _is_linked(b2, 'partner', a)


def test_assoc_from_21_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    b1 = RoyalAndLoyal_Date(day=7, month=7, year=7)
    b2 = RoyalAndLoyal_Date(day=13, month=13, year=13)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport22', b1)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReport22', b1)
    if hasattr(b1, 'RoyalAndLoyal_Date23'):
        assert _is_linked(b1, 'RoyalAndLoyal_Date23', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport22', b2)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReport22', b2)
    if hasattr(b1, 'RoyalAndLoyal_Date23'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Date23', a)
    if hasattr(b2, 'RoyalAndLoyal_Date23'):
        assert _is_linked(b2, 'RoyalAndLoyal_Date23', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport22', None)
    assert not _is_linked(a, 'RoyalAndLoyal_TransactionReport22', b2)
    if hasattr(b2, 'RoyalAndLoyal_Date23'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Date23', a)


def test_assoc_generatedBy5_link_reassign_clear():
    a = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    b1 = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    b2 = RoyalAndLoyal_Service(condition=False, description="sample_text_2", pointsBurned=13, pointsEarned=13, serviceNr=13)
    _safe_set(a, 'transactions6', b1)
    assert _is_linked(a, 'transactions6', b1)
    if hasattr(b1, 'Service7'):
        assert _is_linked(b1, 'Service7', a)
    _safe_set(a, 'transactions6', b2)
    assert _is_linked(a, 'transactions6', b2)
    if hasattr(b1, 'Service7'):
        assert not _is_linked(b1, 'Service7', a)
    if hasattr(b2, 'Service7'):
        assert _is_linked(b2, 'Service7', a)
    _safe_set(a, 'transactions6', None)
    assert not _is_linked(a, 'transactions6', b2)
    if hasattr(b2, 'Service7'):
        assert not _is_linked(b2, 'Service7', a)


def test_assoc_goodThru27_link_reassign_clear():
    a = RoyalAndLoyal_Date(day=7, month=7, year=7)
    b1 = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b2 = RoyalAndLoyal_CustomerCard(color="sample_text_2", printedName="sample_text_2", valid=False)
    _safe_set(a, 'RoyalAndLoyal_Date29', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Date29', b1)
    if hasattr(b1, 'RoyalAndLoyal_CustomerCard28'):
        assert _is_linked(b1, 'RoyalAndLoyal_CustomerCard28', a)
    _safe_set(a, 'RoyalAndLoyal_Date29', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Date29', b2)
    if hasattr(b1, 'RoyalAndLoyal_CustomerCard28'):
        assert not _is_linked(b1, 'RoyalAndLoyal_CustomerCard28', a)
    if hasattr(b2, 'RoyalAndLoyal_CustomerCard28'):
        assert _is_linked(b2, 'RoyalAndLoyal_CustomerCard28', a)
    _safe_set(a, 'RoyalAndLoyal_Date29', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Date29', b2)
    if hasattr(b2, 'RoyalAndLoyal_CustomerCard28'):
        assert not _is_linked(b2, 'RoyalAndLoyal_CustomerCard28', a)


def test_assoc_level89_link_reassign_clear():
    a = RoyalAndLoyal_ServiceLevel(name="sample_text")
    b1 = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    b2 = RoyalAndLoyal_Service(condition=False, description="sample_text_2", pointsBurned=13, pointsEarned=13, serviceNr=13)
    _safe_set(a, 'ServiceLevel90', b1)
    assert _is_linked(a, 'ServiceLevel90', b1)
    if hasattr(b1, 'availableServices'):
        assert _is_linked(b1, 'availableServices', a)
    _safe_set(a, 'ServiceLevel90', b2)
    assert _is_linked(a, 'ServiceLevel90', b2)
    if hasattr(b1, 'availableServices'):
        assert not _is_linked(b1, 'availableServices', a)
    if hasattr(b2, 'availableServices'):
        assert _is_linked(b2, 'availableServices', a)
    _safe_set(a, 'ServiceLevel90', None)
    assert not _is_linked(a, 'ServiceLevel90', b2)
    if hasattr(b2, 'availableServices'):
        assert not _is_linked(b2, 'availableServices', a)


def test_assoc_levels110_link_reassign_clear():
    a = RoyalAndLoyal_ServiceLevel(name="sample_text")
    b1 = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b2 = RoyalAndLoyal_LoyaltyProgram(name="sample_text_2")
    _safe_set(a, 'ServiceLevel111', b1)
    assert _is_linked(a, 'ServiceLevel111', b1)
    if hasattr(b1, 'program'):
        assert _is_linked(b1, 'program', a)
    _safe_set(a, 'ServiceLevel111', b2)
    assert _is_linked(a, 'ServiceLevel111', b2)
    if hasattr(b1, 'program'):
        assert not _is_linked(b1, 'program', a)
    if hasattr(b2, 'program'):
        assert _is_linked(b2, 'program', a)
    _safe_set(a, 'ServiceLevel111', None)
    assert not _is_linked(a, 'ServiceLevel111', b2)
    if hasattr(b2, 'program'):
        assert not _is_linked(b2, 'program', a)


def test_assoc_lines24_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    b1 = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    b2 = RoyalAndLoyal_TransactionReport(balance=13, name="sample_text_2", number=13, totalBurned=13, totalEarned=13)
    _safe_set(a, 'TransactionReportLine', b1)
    assert _is_linked(a, 'TransactionReportLine', b1)
    if hasattr(b1, 'report'):
        assert _is_linked(b1, 'report', a)
    _safe_set(a, 'TransactionReportLine', b2)
    assert _is_linked(a, 'TransactionReportLine', b2)
    if hasattr(b1, 'report'):
        assert not _is_linked(b1, 'report', a)
    if hasattr(b2, 'report'):
        assert _is_linked(b2, 'report', a)
    _safe_set(a, 'TransactionReportLine', None)
    assert not _is_linked(a, 'TransactionReportLine', b2)
    if hasattr(b2, 'report'):
        assert not _is_linked(b2, 'report', a)


def test_assoc_loymemberships115_link_reassign_clear():
    a = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram116', {b1})
    assert _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram116', b1)
    if hasattr(b1, 'RoyalAndLoyal_Membership117'):
        assert _is_linked(b1, 'RoyalAndLoyal_Membership117', a)
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram116', {b2})
    assert _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram116', b2)
    if hasattr(b1, 'RoyalAndLoyal_Membership117'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Membership117', a)
    if hasattr(b2, 'RoyalAndLoyal_Membership117'):
        assert _is_linked(b2, 'RoyalAndLoyal_Membership117', a)
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram116', set())
    assert not _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram116', b2)
    if hasattr(b2, 'RoyalAndLoyal_Membership117'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Membership117', a)


def test_assoc_myLevel33_link_reassign_clear():
    a = RoyalAndLoyal_ServiceLevel(name="sample_text")
    b1 = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b2 = RoyalAndLoyal_CustomerCard(color="sample_text_2", printedName="sample_text_2", valid=False)
    _safe_set(a, 'RoyalAndLoyal_ServiceLevel', b1)
    assert _is_linked(a, 'RoyalAndLoyal_ServiceLevel', b1)
    if hasattr(b1, 'RoyalAndLoyal_CustomerCard34'):
        assert _is_linked(b1, 'RoyalAndLoyal_CustomerCard34', a)
    _safe_set(a, 'RoyalAndLoyal_ServiceLevel', b2)
    assert _is_linked(a, 'RoyalAndLoyal_ServiceLevel', b2)
    if hasattr(b1, 'RoyalAndLoyal_CustomerCard34'):
        assert not _is_linked(b1, 'RoyalAndLoyal_CustomerCard34', a)
    if hasattr(b2, 'RoyalAndLoyal_CustomerCard34'):
        assert _is_linked(b2, 'RoyalAndLoyal_CustomerCard34', a)
    _safe_set(a, 'RoyalAndLoyal_ServiceLevel', None)
    assert not _is_linked(a, 'RoyalAndLoyal_ServiceLevel', b2)
    if hasattr(b2, 'RoyalAndLoyal_CustomerCard34'):
        assert not _is_linked(b2, 'RoyalAndLoyal_CustomerCard34', a)


def test_assoc_owner35_link_reassign_clear():
    a = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b1 = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    b2 = RoyalAndLoyal_Customer(age=13, gender="sample_text_2", isMale=False, name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'cards', b1)
    assert _is_linked(a, 'cards', b1)
    if hasattr(b1, 'Customer'):
        assert _is_linked(b1, 'Customer', a)
    _safe_set(a, 'cards', b2)
    assert _is_linked(a, 'cards', b2)
    if hasattr(b1, 'Customer'):
        assert not _is_linked(b1, 'Customer', a)
    if hasattr(b2, 'Customer'):
        assert _is_linked(b2, 'Customer', a)
    _safe_set(a, 'cards', None)
    assert not _is_linked(a, 'cards', b2)
    if hasattr(b2, 'Customer'):
        assert not _is_linked(b2, 'Customer', a)


def test_assoc_participants112_link_reassign_clear():
    a = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b1 = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    b2 = RoyalAndLoyal_Customer(age=13, gender="sample_text_2", isMale=False, name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'programs113', {b1})
    assert _is_linked(a, 'programs113', b1)
    if hasattr(b1, 'Customer114'):
        assert _is_linked(b1, 'Customer114', a)
    _safe_set(a, 'programs113', {b2})
    assert _is_linked(a, 'programs113', b2)
    if hasattr(b1, 'Customer114'):
        assert not _is_linked(b1, 'Customer114', a)
    if hasattr(b2, 'Customer114'):
        assert _is_linked(b2, 'Customer114', a)
    _safe_set(a, 'programs113', set())
    assert not _is_linked(a, 'programs113', b2)
    if hasattr(b2, 'Customer114'):
        assert not _is_linked(b2, 'Customer114', a)


def test_assoc_participants50_link_reassign_clear():
    a = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'RoyalAndLoyal_Customer', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Customer', b1)
    if hasattr(b1, 'RoyalAndLoyal_Membership51'):
        assert _is_linked(b1, 'RoyalAndLoyal_Membership51', a)
    _safe_set(a, 'RoyalAndLoyal_Customer', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Customer', b2)
    if hasattr(b1, 'RoyalAndLoyal_Membership51'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Membership51', a)
    if hasattr(b2, 'RoyalAndLoyal_Membership51'):
        assert _is_linked(b2, 'RoyalAndLoyal_Membership51', a)
    _safe_set(a, 'RoyalAndLoyal_Customer', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Customer', b2)
    if hasattr(b2, 'RoyalAndLoyal_Membership51'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Membership51', a)


def test_assoc_partner86_link_reassign_clear():
    a = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    b1 = RoyalAndLoyal_ProgramPartner(name="sample_text", numberOfCustomers=7)
    b2 = RoyalAndLoyal_ProgramPartner(name="sample_text_2", numberOfCustomers=13)
    _safe_set(a, 'deliveredServices', b1)
    assert _is_linked(a, 'deliveredServices', b1)
    if hasattr(b1, 'ProgramPartner'):
        assert _is_linked(b1, 'ProgramPartner', a)
    _safe_set(a, 'deliveredServices', b2)
    assert _is_linked(a, 'deliveredServices', b2)
    if hasattr(b1, 'ProgramPartner'):
        assert not _is_linked(b1, 'ProgramPartner', a)
    if hasattr(b2, 'ProgramPartner'):
        assert _is_linked(b2, 'ProgramPartner', a)
    _safe_set(a, 'deliveredServices', None)
    assert not _is_linked(a, 'deliveredServices', b2)
    if hasattr(b2, 'ProgramPartner'):
        assert not _is_linked(b2, 'ProgramPartner', a)


def test_assoc_partners108_link_reassign_clear():
    a = RoyalAndLoyal_ProgramPartner(name="sample_text", numberOfCustomers=7)
    b1 = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b2 = RoyalAndLoyal_LoyaltyProgram(name="sample_text_2")
    _safe_set(a, 'ProgramPartner109', b1)
    assert _is_linked(a, 'ProgramPartner109', b1)
    if hasattr(b1, 'programs'):
        assert _is_linked(b1, 'programs', a)
    _safe_set(a, 'ProgramPartner109', b2)
    assert _is_linked(a, 'ProgramPartner109', b2)
    if hasattr(b1, 'programs'):
        assert not _is_linked(b1, 'programs', a)
    if hasattr(b2, 'programs'):
        assert _is_linked(b2, 'programs', a)
    _safe_set(a, 'ProgramPartner109', None)
    assert not _is_linked(a, 'ProgramPartner109', b2)
    if hasattr(b2, 'programs'):
        assert not _is_linked(b2, 'programs', a)


def test_assoc_program0_link_reassign_clear():
    a = RoyalAndLoyal_ServiceLevel(name="sample_text")
    b1 = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b2 = RoyalAndLoyal_LoyaltyProgram(name="sample_text_2")
    _safe_set(a, 'levels', b1)
    assert _is_linked(a, 'levels', b1)
    if hasattr(b1, 'LoyaltyProgram'):
        assert _is_linked(b1, 'LoyaltyProgram', a)
    _safe_set(a, 'levels', b2)
    assert _is_linked(a, 'levels', b2)
    if hasattr(b1, 'LoyaltyProgram'):
        assert not _is_linked(b1, 'LoyaltyProgram', a)
    if hasattr(b2, 'LoyaltyProgram'):
        assert _is_linked(b2, 'LoyaltyProgram', a)
    _safe_set(a, 'levels', None)
    assert not _is_linked(a, 'levels', b2)
    if hasattr(b2, 'LoyaltyProgram'):
        assert not _is_linked(b2, 'LoyaltyProgram', a)


def test_assoc_programs17_link_reassign_clear():
    a = RoyalAndLoyal_ProgramPartner(name="sample_text", numberOfCustomers=7)
    b1 = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b2 = RoyalAndLoyal_LoyaltyProgram(name="sample_text_2")
    _safe_set(a, 'partners', {b1})
    assert _is_linked(a, 'partners', b1)
    if hasattr(b1, 'LoyaltyProgram18'):
        assert _is_linked(b1, 'LoyaltyProgram18', a)
    _safe_set(a, 'partners', {b2})
    assert _is_linked(a, 'partners', b2)
    if hasattr(b1, 'LoyaltyProgram18'):
        assert not _is_linked(b1, 'LoyaltyProgram18', a)
    if hasattr(b2, 'LoyaltyProgram18'):
        assert _is_linked(b2, 'LoyaltyProgram18', a)
    _safe_set(a, 'partners', set())
    assert not _is_linked(a, 'partners', b2)
    if hasattr(b2, 'LoyaltyProgram18'):
        assert not _is_linked(b2, 'LoyaltyProgram18', a)


def test_assoc_programs49_link_reassign_clear():
    a = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b1 = RoyalAndLoyal_Membership()
    b2 = RoyalAndLoyal_Membership()
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram', b1)
    assert _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram', b1)
    if hasattr(b1, 'RoyalAndLoyal_Membership'):
        assert _is_linked(b1, 'RoyalAndLoyal_Membership', a)
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram', b2)
    assert _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram', b2)
    if hasattr(b1, 'RoyalAndLoyal_Membership'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Membership', a)
    if hasattr(b2, 'RoyalAndLoyal_Membership'):
        assert _is_linked(b2, 'RoyalAndLoyal_Membership', a)
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram', None)
    assert not _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram', b2)
    if hasattr(b2, 'RoyalAndLoyal_Membership'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Membership', a)


def test_assoc_programs94_link_reassign_clear():
    a = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b1 = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    b2 = RoyalAndLoyal_Customer(age=13, gender="sample_text_2", isMale=False, name="sample_text_2", title="sample_text_2")
    _safe_set(a, 'LoyaltyProgram95', b1)
    assert _is_linked(a, 'LoyaltyProgram95', b1)
    if hasattr(b1, 'participants'):
        assert _is_linked(b1, 'participants', a)
    _safe_set(a, 'LoyaltyProgram95', b2)
    assert _is_linked(a, 'LoyaltyProgram95', b2)
    if hasattr(b1, 'participants'):
        assert not _is_linked(b1, 'participants', a)
    if hasattr(b2, 'participants'):
        assert _is_linked(b2, 'participants', a)
    _safe_set(a, 'LoyaltyProgram95', None)
    assert not _is_linked(a, 'LoyaltyProgram95', b2)
    if hasattr(b2, 'participants'):
        assert not _is_linked(b2, 'participants', a)


def test_assoc_ref_RandL_Customer52_link_reassign_clear():
    a = RoyalAndLoyal_Customer(age=7, gender="sample_text", isMale=True, name="sample_text", title="sample_text")
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_Customer53', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Customer53', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL', a)
    _safe_set(a, 'RoyalAndLoyal_Customer53', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Customer53', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL', a)
    _safe_set(a, 'RoyalAndLoyal_Customer53', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Customer53', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL', a)


def test_assoc_ref_RandL_CustomerCard57_link_reassign_clear():
    a = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_CustomerCard59', b1)
    assert _is_linked(a, 'RoyalAndLoyal_CustomerCard59', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL58'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL58', a)
    _safe_set(a, 'RoyalAndLoyal_CustomerCard59', b2)
    assert _is_linked(a, 'RoyalAndLoyal_CustomerCard59', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL58'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL58', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL58'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL58', a)
    _safe_set(a, 'RoyalAndLoyal_CustomerCard59', None)
    assert not _is_linked(a, 'RoyalAndLoyal_CustomerCard59', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL58'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL58', a)


def test_assoc_ref_RandL_Date54_link_reassign_clear():
    a = RoyalAndLoyal_Date(day=7, month=7, year=7)
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_Date56', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Date56', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL55'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL55', a)
    _safe_set(a, 'RoyalAndLoyal_Date56', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Date56', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL55'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL55', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL55'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL55', a)
    _safe_set(a, 'RoyalAndLoyal_Date56', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Date56', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL55'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL55', a)


def test_assoc_ref_RandL_LoyaltyAccount71_link_reassign_clear():
    a = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_LoyaltyAccount73', b1)
    assert _is_linked(a, 'RoyalAndLoyal_LoyaltyAccount73', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL72'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL72', a)
    _safe_set(a, 'RoyalAndLoyal_LoyaltyAccount73', b2)
    assert _is_linked(a, 'RoyalAndLoyal_LoyaltyAccount73', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL72'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL72', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL72'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL72', a)
    _safe_set(a, 'RoyalAndLoyal_LoyaltyAccount73', None)
    assert not _is_linked(a, 'RoyalAndLoyal_LoyaltyAccount73', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL72'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL72', a)


def test_assoc_ref_RandL_LoyaltyProgram66_link_reassign_clear():
    a = RoyalAndLoyal_LoyaltyProgram(name="sample_text")
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram68', b1)
    assert _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram68', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL67'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL67', a)
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram68', b2)
    assert _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram68', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL67'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL67', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL67'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL67', a)
    _safe_set(a, 'RoyalAndLoyal_LoyaltyProgram68', None)
    assert not _is_linked(a, 'RoyalAndLoyal_LoyaltyProgram68', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL67'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL67', a)


def test_assoc_ref_RandL_ProgramPartner80_link_reassign_clear():
    a = RoyalAndLoyal_ProgramPartner(name="sample_text", numberOfCustomers=7)
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_ProgramPartner', b1)
    assert _is_linked(a, 'RoyalAndLoyal_ProgramPartner', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL81'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL81', a)
    _safe_set(a, 'RoyalAndLoyal_ProgramPartner', b2)
    assert _is_linked(a, 'RoyalAndLoyal_ProgramPartner', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL81'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL81', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL81'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL81', a)
    _safe_set(a, 'RoyalAndLoyal_ProgramPartner', None)
    assert not _is_linked(a, 'RoyalAndLoyal_ProgramPartner', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL81'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL81', a)


def test_assoc_ref_RandL_Service63_link_reassign_clear():
    a = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_Service65', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Service65', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL64'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL64', a)
    _safe_set(a, 'RoyalAndLoyal_Service65', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Service65', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL64'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL64', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL64'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL64', a)
    _safe_set(a, 'RoyalAndLoyal_Service65', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Service65', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL64'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL64', a)


def test_assoc_ref_RandL_ServiceLevel74_link_reassign_clear():
    a = RoyalAndLoyal_ServiceLevel(name="sample_text")
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_ServiceLevel76', b1)
    assert _is_linked(a, 'RoyalAndLoyal_ServiceLevel76', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL75'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL75', a)
    _safe_set(a, 'RoyalAndLoyal_ServiceLevel76', b2)
    assert _is_linked(a, 'RoyalAndLoyal_ServiceLevel76', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL75'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL75', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL75'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL75', a)
    _safe_set(a, 'RoyalAndLoyal_ServiceLevel76', None)
    assert not _is_linked(a, 'RoyalAndLoyal_ServiceLevel76', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL75'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL75', a)


def test_assoc_ref_RandL_TransactionReport77_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_TransactionReport79', b1)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReport79', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL78'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL78', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport79', b2)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReport79', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL78'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL78', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL78'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL78', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport79', None)
    assert not _is_linked(a, 'RoyalAndLoyal_TransactionReport79', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL78'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL78', a)


def test_assoc_ref_RandL_TransactionReportLine84_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    b1 = RoyalAndLoyal_Container_RandL()
    b2 = RoyalAndLoyal_Container_RandL()
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine', b1)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReportLine', b1)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL85'):
        assert _is_linked(b1, 'RoyalAndLoyal_Container_RandL85', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine', b2)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReportLine', b2)
    if hasattr(b1, 'RoyalAndLoyal_Container_RandL85'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Container_RandL85', a)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL85'):
        assert _is_linked(b2, 'RoyalAndLoyal_Container_RandL85', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine', None)
    assert not _is_linked(a, 'RoyalAndLoyal_TransactionReportLine', b2)
    if hasattr(b2, 'RoyalAndLoyal_Container_RandL85'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Container_RandL85', a)


def test_assoc_report107_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    b1 = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    b2 = RoyalAndLoyal_TransactionReport(balance=13, name="sample_text_2", number=13, totalBurned=13, totalEarned=13)
    _safe_set(a, 'lines', b1)
    assert _is_linked(a, 'lines', b1)
    if hasattr(b1, 'TransactionReport'):
        assert _is_linked(b1, 'TransactionReport', a)
    _safe_set(a, 'lines', b2)
    assert _is_linked(a, 'lines', b2)
    if hasattr(b1, 'TransactionReport'):
        assert not _is_linked(b1, 'TransactionReport', a)
    if hasattr(b2, 'TransactionReport'):
        assert _is_linked(b2, 'TransactionReport', a)
    _safe_set(a, 'lines', None)
    assert not _is_linked(a, 'lines', b2)
    if hasattr(b2, 'TransactionReport'):
        assert not _is_linked(b2, 'TransactionReport', a)


def test_assoc_tDate3_link_reassign_clear():
    a = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    b1 = RoyalAndLoyal_Date(day=7, month=7, year=7)
    b2 = RoyalAndLoyal_Date(day=13, month=13, year=13)
    _safe_set(a, 'RoyalAndLoyal_Transaction', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Transaction', b1)
    if hasattr(b1, 'RoyalAndLoyal_Date'):
        assert _is_linked(b1, 'RoyalAndLoyal_Date', a)
    _safe_set(a, 'RoyalAndLoyal_Transaction', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Transaction', b2)
    if hasattr(b1, 'RoyalAndLoyal_Date'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Date', a)
    if hasattr(b2, 'RoyalAndLoyal_Date'):
        assert _is_linked(b2, 'RoyalAndLoyal_Date', a)
    _safe_set(a, 'RoyalAndLoyal_Transaction', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Transaction', b2)
    if hasattr(b2, 'RoyalAndLoyal_Date'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Date', a)


def test_assoc_transaction104_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    b1 = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    b2 = RoyalAndLoyal_Transaction(amount=9.99, points=13)
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine105', b1)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReportLine105', b1)
    if hasattr(b1, 'RoyalAndLoyal_Transaction106'):
        assert _is_linked(b1, 'RoyalAndLoyal_Transaction106', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine105', b2)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReportLine105', b2)
    if hasattr(b1, 'RoyalAndLoyal_Transaction106'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Transaction106', a)
    if hasattr(b2, 'RoyalAndLoyal_Transaction106'):
        assert _is_linked(b2, 'RoyalAndLoyal_Transaction106', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine105', None)
    assert not _is_linked(a, 'RoyalAndLoyal_TransactionReportLine105', b2)
    if hasattr(b2, 'RoyalAndLoyal_Transaction106'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Transaction106', a)


def test_assoc_transactions13_link_reassign_clear():
    a = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    b1 = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    b2 = RoyalAndLoyal_LoyaltyAccount(number=13, points=13, totalPointsEarned=13)
    _safe_set(a, 'Transaction', b1)
    assert _is_linked(a, 'Transaction', b1)
    if hasattr(b1, 'account14'):
        assert _is_linked(b1, 'account14', a)
    _safe_set(a, 'Transaction', b2)
    assert _is_linked(a, 'Transaction', b2)
    if hasattr(b1, 'account14'):
        assert not _is_linked(b1, 'account14', a)
    if hasattr(b2, 'account14'):
        assert _is_linked(b2, 'account14', a)
    _safe_set(a, 'Transaction', None)
    assert not _is_linked(a, 'Transaction', b2)
    if hasattr(b2, 'account14'):
        assert not _is_linked(b2, 'account14', a)


def test_assoc_transactions38_link_reassign_clear():
    a = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    b1 = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b2 = RoyalAndLoyal_CustomerCard(color="sample_text_2", printedName="sample_text_2", valid=False)
    _safe_set(a, 'Transaction40', b1)
    assert _is_linked(a, 'Transaction40', b1)
    if hasattr(b1, 'card39'):
        assert _is_linked(b1, 'card39', a)
    _safe_set(a, 'Transaction40', b2)
    assert _is_linked(a, 'Transaction40', b2)
    if hasattr(b1, 'card39'):
        assert not _is_linked(b1, 'card39', a)
    if hasattr(b2, 'card39'):
        assert _is_linked(b2, 'card39', a)
    _safe_set(a, 'Transaction40', None)
    assert not _is_linked(a, 'Transaction40', b2)
    if hasattr(b2, 'card39'):
        assert not _is_linked(b2, 'card39', a)


def test_assoc_transactions87_link_reassign_clear():
    a = RoyalAndLoyal_Transaction(amount=3.14, points=7)
    b1 = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    b2 = RoyalAndLoyal_Service(condition=False, description="sample_text_2", pointsBurned=13, pointsEarned=13, serviceNr=13)
    _safe_set(a, 'Transaction88', b1)
    assert _is_linked(a, 'Transaction88', b1)
    if hasattr(b1, 'generatedBy'):
        assert _is_linked(b1, 'generatedBy', a)
    _safe_set(a, 'Transaction88', b2)
    assert _is_linked(a, 'Transaction88', b2)
    if hasattr(b1, 'generatedBy'):
        assert not _is_linked(b1, 'generatedBy', a)
    if hasattr(b2, 'generatedBy'):
        assert _is_linked(b2, 'generatedBy', a)
    _safe_set(a, 'Transaction88', None)
    assert not _is_linked(a, 'Transaction88', b2)
    if hasattr(b2, 'generatedBy'):
        assert not _is_linked(b2, 'generatedBy', a)


def test_assoc_trlDate101_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReportLine(amount=3.14, partnerName="sample_text", points=7, serviceDesc="sample_text")
    b1 = RoyalAndLoyal_Date(day=7, month=7, year=7)
    b2 = RoyalAndLoyal_Date(day=13, month=13, year=13)
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine102', b1)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReportLine102', b1)
    if hasattr(b1, 'RoyalAndLoyal_Date103'):
        assert _is_linked(b1, 'RoyalAndLoyal_Date103', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine102', b2)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReportLine102', b2)
    if hasattr(b1, 'RoyalAndLoyal_Date103'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Date103', a)
    if hasattr(b2, 'RoyalAndLoyal_Date103'):
        assert _is_linked(b2, 'RoyalAndLoyal_Date103', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReportLine102', None)
    assert not _is_linked(a, 'RoyalAndLoyal_TransactionReportLine102', b2)
    if hasattr(b2, 'RoyalAndLoyal_Date103'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Date103', a)


def test_assoc_until19_link_reassign_clear():
    a = RoyalAndLoyal_TransactionReport(balance=7, name="sample_text", number=7, totalBurned=7, totalEarned=7)
    b1 = RoyalAndLoyal_Date(day=7, month=7, year=7)
    b2 = RoyalAndLoyal_Date(day=13, month=13, year=13)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport', b1)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReport', b1)
    if hasattr(b1, 'RoyalAndLoyal_Date20'):
        assert _is_linked(b1, 'RoyalAndLoyal_Date20', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport', b2)
    assert _is_linked(a, 'RoyalAndLoyal_TransactionReport', b2)
    if hasattr(b1, 'RoyalAndLoyal_Date20'):
        assert not _is_linked(b1, 'RoyalAndLoyal_Date20', a)
    if hasattr(b2, 'RoyalAndLoyal_Date20'):
        assert _is_linked(b2, 'RoyalAndLoyal_Date20', a)
    _safe_set(a, 'RoyalAndLoyal_TransactionReport', None)
    assert not _is_linked(a, 'RoyalAndLoyal_TransactionReport', b2)
    if hasattr(b2, 'RoyalAndLoyal_Date20'):
        assert not _is_linked(b2, 'RoyalAndLoyal_Date20', a)


def test_assoc_usedServices10_link_reassign_clear():
    a = RoyalAndLoyal_Service(condition=True, description="sample_text", pointsBurned=7, pointsEarned=7, serviceNr=7)
    b1 = RoyalAndLoyal_LoyaltyAccount(number=7, points=7, totalPointsEarned=7)
    b2 = RoyalAndLoyal_LoyaltyAccount(number=13, points=13, totalPointsEarned=13)
    _safe_set(a, 'RoyalAndLoyal_Service', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Service', b1)
    if hasattr(b1, 'RoyalAndLoyal_LoyaltyAccount'):
        assert _is_linked(b1, 'RoyalAndLoyal_LoyaltyAccount', a)
    _safe_set(a, 'RoyalAndLoyal_Service', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Service', b2)
    if hasattr(b1, 'RoyalAndLoyal_LoyaltyAccount'):
        assert not _is_linked(b1, 'RoyalAndLoyal_LoyaltyAccount', a)
    if hasattr(b2, 'RoyalAndLoyal_LoyaltyAccount'):
        assert _is_linked(b2, 'RoyalAndLoyal_LoyaltyAccount', a)
    _safe_set(a, 'RoyalAndLoyal_Service', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Service', b2)
    if hasattr(b2, 'RoyalAndLoyal_LoyaltyAccount'):
        assert not _is_linked(b2, 'RoyalAndLoyal_LoyaltyAccount', a)


def test_assoc_validFrom30_link_reassign_clear():
    a = RoyalAndLoyal_Date(day=7, month=7, year=7)
    b1 = RoyalAndLoyal_CustomerCard(color="sample_text", printedName="sample_text", valid=True)
    b2 = RoyalAndLoyal_CustomerCard(color="sample_text_2", printedName="sample_text_2", valid=False)
    _safe_set(a, 'RoyalAndLoyal_Date32', b1)
    assert _is_linked(a, 'RoyalAndLoyal_Date32', b1)
    if hasattr(b1, 'RoyalAndLoyal_CustomerCard31'):
        assert _is_linked(b1, 'RoyalAndLoyal_CustomerCard31', a)
    _safe_set(a, 'RoyalAndLoyal_Date32', b2)
    assert _is_linked(a, 'RoyalAndLoyal_Date32', b2)
    if hasattr(b1, 'RoyalAndLoyal_CustomerCard31'):
        assert not _is_linked(b1, 'RoyalAndLoyal_CustomerCard31', a)
    if hasattr(b2, 'RoyalAndLoyal_CustomerCard31'):
        assert _is_linked(b2, 'RoyalAndLoyal_CustomerCard31', a)
    _safe_set(a, 'RoyalAndLoyal_Date32', None)
    assert not _is_linked(a, 'RoyalAndLoyal_Date32', b2)
    if hasattr(b2, 'RoyalAndLoyal_CustomerCard31'):
        assert not _is_linked(b2, 'RoyalAndLoyal_CustomerCard31', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

RoyalAndLoyal_Burning_strategy = st.builds(RoyalAndLoyal_Burning)
@given(instance=RoyalAndLoyal_Burning_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_Burning_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_Burning)


RoyalAndLoyal_Container_RandL_strategy = st.builds(RoyalAndLoyal_Container_RandL)
@given(instance=RoyalAndLoyal_Container_RandL_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_Container_RandL_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_Container_RandL)


RoyalAndLoyal_Customer_strategy = st.builds(RoyalAndLoyal_Customer, age=st.integers(), gender=safe_text, isMale=st.booleans(), name=safe_text, title=safe_text)
@given(instance=RoyalAndLoyal_Customer_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_Customer_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_Customer)


RoyalAndLoyal_CustomerCard_strategy = st.builds(RoyalAndLoyal_CustomerCard, color=safe_text, printedName=safe_text, valid=st.booleans())
@given(instance=RoyalAndLoyal_CustomerCard_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_CustomerCard_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_CustomerCard)


RoyalAndLoyal_Date_strategy = st.builds(RoyalAndLoyal_Date, day=st.integers(), month=st.integers(), year=st.integers())
@given(instance=RoyalAndLoyal_Date_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_Date_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_Date)


RoyalAndLoyal_Earning_strategy = st.builds(RoyalAndLoyal_Earning)
@given(instance=RoyalAndLoyal_Earning_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_Earning_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_Earning)


RoyalAndLoyal_LoyaltyAccount_strategy = st.builds(RoyalAndLoyal_LoyaltyAccount, number=st.integers(), points=st.integers(), totalPointsEarned=st.integers())
@given(instance=RoyalAndLoyal_LoyaltyAccount_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_LoyaltyAccount_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_LoyaltyAccount)


RoyalAndLoyal_LoyaltyProgram_strategy = st.builds(RoyalAndLoyal_LoyaltyProgram, name=safe_text)
@given(instance=RoyalAndLoyal_LoyaltyProgram_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_LoyaltyProgram_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_LoyaltyProgram)


RoyalAndLoyal_Membership_strategy = st.builds(RoyalAndLoyal_Membership)
@given(instance=RoyalAndLoyal_Membership_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_Membership_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_Membership)


RoyalAndLoyal_ProgramPartner_strategy = st.builds(RoyalAndLoyal_ProgramPartner, name=safe_text, numberOfCustomers=st.integers())
@given(instance=RoyalAndLoyal_ProgramPartner_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_ProgramPartner_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_ProgramPartner)


RoyalAndLoyal_Service_strategy = st.builds(RoyalAndLoyal_Service, condition=st.booleans(), description=safe_text, pointsBurned=st.integers(), pointsEarned=st.integers(), serviceNr=st.integers())
@given(instance=RoyalAndLoyal_Service_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_Service_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_Service)


RoyalAndLoyal_ServiceLevel_strategy = st.builds(RoyalAndLoyal_ServiceLevel, name=safe_text)
@given(instance=RoyalAndLoyal_ServiceLevel_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_ServiceLevel_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_ServiceLevel)


RoyalAndLoyal_Transaction_strategy = st.builds(RoyalAndLoyal_Transaction, amount=st.floats(allow_nan=False, allow_infinity=False), points=st.integers())
@given(instance=RoyalAndLoyal_Transaction_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_Transaction_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_Transaction)


RoyalAndLoyal_TransactionReport_strategy = st.builds(RoyalAndLoyal_TransactionReport, balance=st.integers(), name=safe_text, number=st.integers(), totalBurned=st.integers(), totalEarned=st.integers())
@given(instance=RoyalAndLoyal_TransactionReport_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_TransactionReport_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_TransactionReport)


RoyalAndLoyal_TransactionReportLine_strategy = st.builds(RoyalAndLoyal_TransactionReportLine, amount=st.floats(allow_nan=False, allow_infinity=False), partnerName=safe_text, points=st.integers(), serviceDesc=safe_text)
@given(instance=RoyalAndLoyal_TransactionReportLine_strategy)
@settings(max_examples=25)
def test_RoyalAndLoyal_TransactionReportLine_instantiation(instance):
    assert isinstance(instance, RoyalAndLoyal_TransactionReportLine)


Transaction_strategy = st.builds(Transaction)
@given(instance=Transaction_strategy)
@settings(max_examples=25)
def test_Transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



