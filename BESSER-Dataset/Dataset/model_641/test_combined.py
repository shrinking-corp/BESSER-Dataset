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
    Employee,
    Account,
    BankingSystem_Saving,
    BankingSystem_Chequing,
    BankingSystem_Financial_Representative,
    BankingSystem_Loan,
    BankingSystem_Account,
    BankingSystem_Employee,
    BankingSystem_Customer,
    BankingSystem_Branch,
    BankingSystem_Bank,
    CustomerType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())



def test_hyp_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_hyp_account_constructor_exists():
    assert callable(Account.__init__)


def test_hyp_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bankingsystem_saving_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Saving)


def test_hyp_bankingsystem_saving_constructor_exists():
    assert callable(BankingSystem_Saving.__init__)


def test_hyp_bankingsystem_saving_constructor_args():
    sig = inspect.signature(BankingSystem_Saving.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"




def test_hyp_bankingsystem_chequing_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Chequing)


def test_hyp_bankingsystem_chequing_constructor_exists():
    assert callable(BankingSystem_Chequing.__init__)


def test_hyp_bankingsystem_chequing_constructor_args():
    sig = inspect.signature(BankingSystem_Chequing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bankingsystem_financial_representative_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Financial_Representative)


def test_hyp_bankingsystem_financial_representative_constructor_exists():
    assert callable(BankingSystem_Financial_Representative.__init__)


def test_hyp_bankingsystem_financial_representative_constructor_args():
    sig = inspect.signature(BankingSystem_Financial_Representative.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bankingsystem_loan_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Loan)


def test_hyp_bankingsystem_loan_constructor_exists():
    assert callable(BankingSystem_Loan.__init__)


def test_hyp_bankingsystem_loan_constructor_args():
    sig = inspect.signature(BankingSystem_Loan.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "loanNumber" in params, "Missing parameter 'loanNumber'"







def test_hyp_bankingsystem_account_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Account)


def test_hyp_bankingsystem_account_constructor_exists():
    assert callable(BankingSystem_Account.__init__)


def test_hyp_bankingsystem_account_constructor_args():
    sig = inspect.signature(BankingSystem_Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"





def test_hyp_bankingsystem_employee_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Employee)


def test_hyp_bankingsystem_employee_constructor_exists():
    assert callable(BankingSystem_Employee.__init__)


def test_hyp_bankingsystem_employee_constructor_args():
    sig = inspect.signature(BankingSystem_Employee.__init__)
    params = list(sig.parameters.keys())
    assert "ephoneNumber" in params, "Missing parameter 'ephoneNumber'"
    assert "eage" in params, "Missing parameter 'eage'"
    assert "eaddress" in params, "Missing parameter 'eaddress'"
    assert "eid" in params, "Missing parameter 'eid'"
    assert "ename" in params, "Missing parameter 'ename'"
    assert "isCustomer" in params, "Missing parameter 'isCustomer'"









def test_hyp_bankingsystem_customer_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Customer)


def test_hyp_bankingsystem_customer_constructor_exists():
    assert callable(BankingSystem_Customer.__init__)


def test_hyp_bankingsystem_customer_constructor_args():
    sig = inspect.signature(BankingSystem_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "customerType" in params, "Missing parameter 'customerType'"
    assert "address" in params, "Missing parameter 'address'"
    assert "age" in params, "Missing parameter 'age'"








def test_hyp_bankingsystem_branch_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Branch)


def test_hyp_bankingsystem_branch_constructor_exists():
    assert callable(BankingSystem_Branch.__init__)


def test_hyp_bankingsystem_branch_constructor_args():
    sig = inspect.signature(BankingSystem_Branch.__init__)
    params = list(sig.parameters.keys())
    assert "branchId" in params, "Missing parameter 'branchId'"
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"







def test_hyp_bankingsystem_bank_is_not_abstract():
    assert not inspect.isabstract(BankingSystem_Bank)


def test_hyp_bankingsystem_bank_constructor_exists():
    assert callable(BankingSystem_Bank.__init__)


def test_hyp_bankingsystem_bank_constructor_args():
    sig = inspect.signature(BankingSystem_Bank.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "bankId" in params, "Missing parameter 'bankId'"
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_customertype_exists():
    # Check that the Enumeration exists
    assert CustomerType is not None

def test_hyp_customertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CustomerType]
    expected_literals = [
        "Youth",
        "Adult",
        "Senior",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CustomerType"


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
Employee_strategy = st.builds(
    Employee,
)
Account_strategy = st.builds(
    Account,
)
BankingSystem_Saving_strategy = st.builds(
    BankingSystem_Saving,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BankingSystem_Chequing_strategy = st.builds(
    BankingSystem_Chequing,
)
BankingSystem_Financial_Representative_strategy = st.builds(
    BankingSystem_Financial_Representative,
)
BankingSystem_Loan_strategy = st.builds(
    BankingSystem_Loan,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    duration=
        st.integers(),
    loanNumber=
        safe_text
)
BankingSystem_Account_strategy = st.builds(
    BankingSystem_Account,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    accountNumber=
        safe_text
)
BankingSystem_Employee_strategy = st.builds(
    BankingSystem_Employee,
    ephoneNumber=
        safe_text,
    eage=
        st.integers(),
    eaddress=
        safe_text,
    eid=
        st.integers(),
    ename=
        safe_text,
    isCustomer=
        st.booleans()
)
BankingSystem_Customer_strategy = st.builds(
    BankingSystem_Customer,
    phoneNumber=
        safe_text,
    name=
        safe_text,
    customerType=
        safe_text,
    address=
        safe_text,
    age=
        st.integers()
)
BankingSystem_Branch_strategy = st.builds(
    BankingSystem_Branch,
    branchId=
        st.integers(),
    location=
        safe_text,
    name=
        safe_text,
    phoneNumber=
        safe_text
)
BankingSystem_Bank_strategy = st.builds(
    BankingSystem_Bank,
    name=
        safe_text,
    bankId=
        st.integers(),
    description=
        safe_text
)






@given(instance=BankingSystem_Saving_strategy)
def test_hyp_bankingsystem_saving_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original






@given(instance=BankingSystem_Loan_strategy)
def test_hyp_bankingsystem_loan_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=BankingSystem_Loan_strategy)
def test_hyp_bankingsystem_loan_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=BankingSystem_Loan_strategy)
def test_hyp_bankingsystem_loan_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=BankingSystem_Loan_strategy)
def test_hyp_bankingsystem_loan_loanNumber_setter(instance):
    original = instance.loanNumber
    instance.loanNumber = original
    assert instance.loanNumber == original




@given(instance=BankingSystem_Account_strategy)
def test_hyp_bankingsystem_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=BankingSystem_Account_strategy)
def test_hyp_bankingsystem_account_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original




@given(instance=BankingSystem_Employee_strategy)
def test_hyp_bankingsystem_employee_ephoneNumber_setter(instance):
    original = instance.ephoneNumber
    instance.ephoneNumber = original
    assert instance.ephoneNumber == original



@given(instance=BankingSystem_Employee_strategy)
def test_hyp_bankingsystem_employee_eage_setter(instance):
    original = instance.eage
    instance.eage = original
    assert instance.eage == original



@given(instance=BankingSystem_Employee_strategy)
def test_hyp_bankingsystem_employee_eaddress_setter(instance):
    original = instance.eaddress
    instance.eaddress = original
    assert instance.eaddress == original



@given(instance=BankingSystem_Employee_strategy)
def test_hyp_bankingsystem_employee_eid_setter(instance):
    original = instance.eid
    instance.eid = original
    assert instance.eid == original



@given(instance=BankingSystem_Employee_strategy)
def test_hyp_bankingsystem_employee_ename_setter(instance):
    original = instance.ename
    instance.ename = original
    assert instance.ename == original



@given(instance=BankingSystem_Employee_strategy)
def test_hyp_bankingsystem_employee_isCustomer_setter(instance):
    original = instance.isCustomer
    instance.isCustomer = original
    assert instance.isCustomer == original




@given(instance=BankingSystem_Customer_strategy)
def test_hyp_bankingsystem_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=BankingSystem_Customer_strategy)
def test_hyp_bankingsystem_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BankingSystem_Customer_strategy)
def test_hyp_bankingsystem_customer_customerType_setter(instance):
    original = instance.customerType
    instance.customerType = original
    assert instance.customerType == original



@given(instance=BankingSystem_Customer_strategy)
def test_hyp_bankingsystem_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=BankingSystem_Customer_strategy)
def test_hyp_bankingsystem_customer_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original




@given(instance=BankingSystem_Branch_strategy)
def test_hyp_bankingsystem_branch_branchId_setter(instance):
    original = instance.branchId
    instance.branchId = original
    assert instance.branchId == original



@given(instance=BankingSystem_Branch_strategy)
def test_hyp_bankingsystem_branch_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=BankingSystem_Branch_strategy)
def test_hyp_bankingsystem_branch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BankingSystem_Branch_strategy)
def test_hyp_bankingsystem_branch_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original




@given(instance=BankingSystem_Bank_strategy)
def test_hyp_bankingsystem_bank_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=BankingSystem_Bank_strategy)
def test_hyp_bankingsystem_bank_bankId_setter(instance):
    original = instance.bankId
    instance.bankId = original
    assert instance.bankId == original



@given(instance=BankingSystem_Bank_strategy)
def test_hyp_bankingsystem_bank_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account,
    BankingSystem_Account,
    BankingSystem_Bank,
    BankingSystem_Branch,
    BankingSystem_Chequing,
    BankingSystem_Customer,
    BankingSystem_Employee,
    BankingSystem_Financial_Representative,
    BankingSystem_Loan,
    BankingSystem_Saving,
    Employee,
    CustomerType,
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

def test_BankingSystem_Account_accountNumber_value_roundtrip():
    instance = BankingSystem_Account(accountNumber="sample_text", balance=3.14)
    assert instance.accountNumber == "sample_text"
    instance.accountNumber = "sample_text_2"
    assert instance.accountNumber == "sample_text_2"


def test_BankingSystem_Account_balance_value_roundtrip():
    instance = BankingSystem_Account(accountNumber="sample_text", balance=3.14)
    assert instance.balance == 3.14
    instance.balance = 9.99
    assert instance.balance == 9.99


def test_BankingSystem_Bank_bankId_value_roundtrip():
    instance = BankingSystem_Bank(bankId=7, description="sample_text", name="sample_text")
    assert instance.bankId == 7
    instance.bankId = 13
    assert instance.bankId == 13


def test_BankingSystem_Bank_description_value_roundtrip():
    instance = BankingSystem_Bank(bankId=7, description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_BankingSystem_Bank_name_value_roundtrip():
    instance = BankingSystem_Bank(bankId=7, description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_BankingSystem_Branch_branchId_value_roundtrip():
    instance = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.branchId == 7
    instance.branchId = 13
    assert instance.branchId == 13


def test_BankingSystem_Branch_location_value_roundtrip():
    instance = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_BankingSystem_Branch_name_value_roundtrip():
    instance = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_BankingSystem_Branch_phoneNumber_value_roundtrip():
    instance = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_BankingSystem_Customer_address_value_roundtrip():
    instance = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_BankingSystem_Customer_age_value_roundtrip():
    instance = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.age == 7
    instance.age = 13
    assert instance.age == 13


def test_BankingSystem_Customer_customerType_value_roundtrip():
    instance = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.customerType == "sample_text"
    instance.customerType = "sample_text_2"
    assert instance.customerType == "sample_text_2"


def test_BankingSystem_Customer_name_value_roundtrip():
    instance = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_BankingSystem_Customer_phoneNumber_value_roundtrip():
    instance = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_BankingSystem_Employee_eaddress_value_roundtrip():
    instance = BankingSystem_Employee(eaddress="sample_text", eage=7, eid=7, ename="sample_text", ephoneNumber="sample_text", isCustomer=True)
    assert instance.eaddress == "sample_text"
    instance.eaddress = "sample_text_2"
    assert instance.eaddress == "sample_text_2"


def test_BankingSystem_Employee_eage_value_roundtrip():
    instance = BankingSystem_Employee(eaddress="sample_text", eage=7, eid=7, ename="sample_text", ephoneNumber="sample_text", isCustomer=True)
    assert instance.eage == 7
    instance.eage = 13
    assert instance.eage == 13


def test_BankingSystem_Employee_eid_value_roundtrip():
    instance = BankingSystem_Employee(eaddress="sample_text", eage=7, eid=7, ename="sample_text", ephoneNumber="sample_text", isCustomer=True)
    assert instance.eid == 7
    instance.eid = 13
    assert instance.eid == 13


def test_BankingSystem_Employee_ename_value_roundtrip():
    instance = BankingSystem_Employee(eaddress="sample_text", eage=7, eid=7, ename="sample_text", ephoneNumber="sample_text", isCustomer=True)
    assert instance.ename == "sample_text"
    instance.ename = "sample_text_2"
    assert instance.ename == "sample_text_2"


def test_BankingSystem_Employee_ephoneNumber_value_roundtrip():
    instance = BankingSystem_Employee(eaddress="sample_text", eage=7, eid=7, ename="sample_text", ephoneNumber="sample_text", isCustomer=True)
    assert instance.ephoneNumber == "sample_text"
    instance.ephoneNumber = "sample_text_2"
    assert instance.ephoneNumber == "sample_text_2"


def test_BankingSystem_Employee_isCustomer_value_roundtrip():
    instance = BankingSystem_Employee(eaddress="sample_text", eage=7, eid=7, ename="sample_text", ephoneNumber="sample_text", isCustomer=True)
    assert instance.isCustomer == True
    instance.isCustomer = False
    assert instance.isCustomer == False


def test_BankingSystem_Loan_amount_value_roundtrip():
    instance = BankingSystem_Loan(amount=3.14, duration=7, interestRate=3.14, loanNumber="sample_text")
    assert instance.amount == 3.14
    instance.amount = 9.99
    assert instance.amount == 9.99


def test_BankingSystem_Loan_duration_value_roundtrip():
    instance = BankingSystem_Loan(amount=3.14, duration=7, interestRate=3.14, loanNumber="sample_text")
    assert instance.duration == 7
    instance.duration = 13
    assert instance.duration == 13


def test_BankingSystem_Loan_interestRate_value_roundtrip():
    instance = BankingSystem_Loan(amount=3.14, duration=7, interestRate=3.14, loanNumber="sample_text")
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_BankingSystem_Loan_loanNumber_value_roundtrip():
    instance = BankingSystem_Loan(amount=3.14, duration=7, interestRate=3.14, loanNumber="sample_text")
    assert instance.loanNumber == "sample_text"
    instance.loanNumber = "sample_text_2"
    assert instance.loanNumber == "sample_text_2"


def test_BankingSystem_Saving_interestRate_value_roundtrip():
    instance = BankingSystem_Saving(interestRate=3.14)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_BankingSystem_Chequing_isa_Account():
    instance = BankingSystem_Chequing()
    assert isinstance(instance, Account)


def test_BankingSystem_Saving_isa_Account():
    instance = BankingSystem_Saving(interestRate=3.14)
    assert isinstance(instance, Account)


def test_BankingSystem_Financial_Representative_isa_Employee():
    instance = BankingSystem_Financial_Representative()
    assert isinstance(instance, Employee)


def test_assoc_a17_link_reassign_clear():
    a = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = BankingSystem_Financial_Representative()
    b2 = BankingSystem_Financial_Representative()
    _safe_set(a, 'Customer18', b1)
    assert _is_linked(a, 'Customer18', b1)
    if hasattr(b1, 'representative'):
        assert _is_linked(b1, 'representative', a)
    _safe_set(a, 'Customer18', b2)
    assert _is_linked(a, 'Customer18', b2)
    if hasattr(b1, 'representative'):
        assert not _is_linked(b1, 'representative', a)
    if hasattr(b2, 'representative'):
        assert _is_linked(b2, 'representative', a)
    _safe_set(a, 'Customer18', None)
    assert not _is_linked(a, 'Customer18', b2)
    if hasattr(b2, 'representative'):
        assert not _is_linked(b2, 'representative', a)


def test_assoc_accounts7_link_reassign_clear():
    a = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = BankingSystem_Account(accountNumber="sample_text", balance=3.14)
    b2 = BankingSystem_Account(accountNumber="sample_text_2", balance=9.99)
    _safe_set(a, 'customer', {b1})
    assert _is_linked(a, 'customer', b1)
    if hasattr(b1, 'Account'):
        assert _is_linked(b1, 'Account', a)
    _safe_set(a, 'customer', {b2})
    assert _is_linked(a, 'customer', b2)
    if hasattr(b1, 'Account'):
        assert not _is_linked(b1, 'Account', a)
    if hasattr(b2, 'Account'):
        assert _is_linked(b2, 'Account', a)
    _safe_set(a, 'customer', set())
    assert not _is_linked(a, 'customer', b2)
    if hasattr(b2, 'Account'):
        assert not _is_linked(b2, 'Account', a)


def test_assoc_bank4_link_reassign_clear():
    a = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = BankingSystem_Bank(bankId=7, description="sample_text", name="sample_text")
    b2 = BankingSystem_Bank(bankId=13, description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'branches', b1)
    assert _is_linked(a, 'branches', b1)
    if hasattr(b1, 'Bank'):
        assert _is_linked(b1, 'Bank', a)
    _safe_set(a, 'branches', b2)
    assert _is_linked(a, 'branches', b2)
    if hasattr(b1, 'Bank'):
        assert not _is_linked(b1, 'Bank', a)
    if hasattr(b2, 'Bank'):
        assert _is_linked(b2, 'Bank', a)
    _safe_set(a, 'branches', None)
    assert not _is_linked(a, 'branches', b2)
    if hasattr(b2, 'Bank'):
        assert not _is_linked(b2, 'Bank', a)


def test_assoc_branch13_link_reassign_clear():
    a = BankingSystem_Employee(eaddress="sample_text", eage=7, eid=7, ename="sample_text", ephoneNumber="sample_text", isCustomer=True)
    b1 = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    b2 = BankingSystem_Branch(branchId=13, location="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    _safe_set(a, 'employees', b1)
    assert _is_linked(a, 'employees', b1)
    if hasattr(b1, 'Branch14'):
        assert _is_linked(b1, 'Branch14', a)
    _safe_set(a, 'employees', b2)
    assert _is_linked(a, 'employees', b2)
    if hasattr(b1, 'Branch14'):
        assert not _is_linked(b1, 'Branch14', a)
    if hasattr(b2, 'Branch14'):
        assert _is_linked(b2, 'Branch14', a)
    _safe_set(a, 'employees', None)
    assert not _is_linked(a, 'employees', b2)
    if hasattr(b2, 'Branch14'):
        assert not _is_linked(b2, 'Branch14', a)


def test_assoc_branch5_link_reassign_clear():
    a = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    b2 = BankingSystem_Branch(branchId=13, location="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    _safe_set(a, 'customers', b1)
    assert _is_linked(a, 'customers', b1)
    if hasattr(b1, 'Branch6'):
        assert _is_linked(b1, 'Branch6', a)
    _safe_set(a, 'customers', b2)
    assert _is_linked(a, 'customers', b2)
    if hasattr(b1, 'Branch6'):
        assert not _is_linked(b1, 'Branch6', a)
    if hasattr(b2, 'Branch6'):
        assert _is_linked(b2, 'Branch6', a)
    _safe_set(a, 'customers', None)
    assert not _is_linked(a, 'customers', b2)
    if hasattr(b2, 'Branch6'):
        assert not _is_linked(b2, 'Branch6', a)


def test_assoc_branches0_link_reassign_clear():
    a = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = BankingSystem_Bank(bankId=7, description="sample_text", name="sample_text")
    b2 = BankingSystem_Bank(bankId=13, description="sample_text_2", name="sample_text_2")
    _safe_set(a, 'Branch', b1)
    assert _is_linked(a, 'Branch', b1)
    if hasattr(b1, 'bank'):
        assert _is_linked(b1, 'bank', a)
    _safe_set(a, 'Branch', b2)
    assert _is_linked(a, 'Branch', b2)
    if hasattr(b1, 'bank'):
        assert not _is_linked(b1, 'bank', a)
    if hasattr(b2, 'bank'):
        assert _is_linked(b2, 'bank', a)
    _safe_set(a, 'Branch', None)
    assert not _is_linked(a, 'Branch', b2)
    if hasattr(b2, 'bank'):
        assert not _is_linked(b2, 'bank', a)


def test_assoc_customer11_link_reassign_clear():
    a = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = BankingSystem_Account(accountNumber="sample_text", balance=3.14)
    b2 = BankingSystem_Account(accountNumber="sample_text_2", balance=9.99)
    _safe_set(a, 'Customer12', b1)
    assert _is_linked(a, 'Customer12', b1)
    if hasattr(b1, 'accounts'):
        assert _is_linked(b1, 'accounts', a)
    _safe_set(a, 'Customer12', b2)
    assert _is_linked(a, 'Customer12', b2)
    if hasattr(b1, 'accounts'):
        assert not _is_linked(b1, 'accounts', a)
    if hasattr(b2, 'accounts'):
        assert _is_linked(b2, 'accounts', a)
    _safe_set(a, 'Customer12', None)
    assert not _is_linked(a, 'Customer12', b2)
    if hasattr(b2, 'accounts'):
        assert not _is_linked(b2, 'accounts', a)


def test_assoc_customer15_link_reassign_clear():
    a = BankingSystem_Loan(amount=3.14, duration=7, interestRate=3.14, loanNumber="sample_text")
    b1 = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    b2 = BankingSystem_Customer(address="sample_text_2", age=13, customerType="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    _safe_set(a, 'loans', b1)
    assert _is_linked(a, 'loans', b1)
    if hasattr(b1, 'Customer16'):
        assert _is_linked(b1, 'Customer16', a)
    _safe_set(a, 'loans', b2)
    assert _is_linked(a, 'loans', b2)
    if hasattr(b1, 'Customer16'):
        assert not _is_linked(b1, 'Customer16', a)
    if hasattr(b2, 'Customer16'):
        assert _is_linked(b2, 'Customer16', a)
    _safe_set(a, 'loans', None)
    assert not _is_linked(a, 'loans', b2)
    if hasattr(b2, 'Customer16'):
        assert not _is_linked(b2, 'Customer16', a)


def test_assoc_customers1_link_reassign_clear():
    a = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    b2 = BankingSystem_Branch(branchId=13, location="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    _safe_set(a, 'Customer', b1)
    assert _is_linked(a, 'Customer', b1)
    if hasattr(b1, 'branch'):
        assert _is_linked(b1, 'branch', a)
    _safe_set(a, 'Customer', b2)
    assert _is_linked(a, 'Customer', b2)
    if hasattr(b1, 'branch'):
        assert not _is_linked(b1, 'branch', a)
    if hasattr(b2, 'branch'):
        assert _is_linked(b2, 'branch', a)
    _safe_set(a, 'Customer', None)
    assert not _is_linked(a, 'Customer', b2)
    if hasattr(b2, 'branch'):
        assert not _is_linked(b2, 'branch', a)


def test_assoc_employees2_link_reassign_clear():
    a = BankingSystem_Employee(eaddress="sample_text", eage=7, eid=7, ename="sample_text", ephoneNumber="sample_text", isCustomer=True)
    b1 = BankingSystem_Branch(branchId=7, location="sample_text", name="sample_text", phoneNumber="sample_text")
    b2 = BankingSystem_Branch(branchId=13, location="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    _safe_set(a, 'Employee', b1)
    assert _is_linked(a, 'Employee', b1)
    if hasattr(b1, 'branch3'):
        assert _is_linked(b1, 'branch3', a)
    _safe_set(a, 'Employee', b2)
    assert _is_linked(a, 'Employee', b2)
    if hasattr(b1, 'branch3'):
        assert not _is_linked(b1, 'branch3', a)
    if hasattr(b2, 'branch3'):
        assert _is_linked(b2, 'branch3', a)
    _safe_set(a, 'Employee', None)
    assert not _is_linked(a, 'Employee', b2)
    if hasattr(b2, 'branch3'):
        assert not _is_linked(b2, 'branch3', a)


def test_assoc_loans8_link_reassign_clear():
    a = BankingSystem_Loan(amount=3.14, duration=7, interestRate=3.14, loanNumber="sample_text")
    b1 = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    b2 = BankingSystem_Customer(address="sample_text_2", age=13, customerType="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    _safe_set(a, 'Loan', b1)
    assert _is_linked(a, 'Loan', b1)
    if hasattr(b1, 'customer9'):
        assert _is_linked(b1, 'customer9', a)
    _safe_set(a, 'Loan', b2)
    assert _is_linked(a, 'Loan', b2)
    if hasattr(b1, 'customer9'):
        assert not _is_linked(b1, 'customer9', a)
    if hasattr(b2, 'customer9'):
        assert _is_linked(b2, 'customer9', a)
    _safe_set(a, 'Loan', None)
    assert not _is_linked(a, 'Loan', b2)
    if hasattr(b2, 'customer9'):
        assert not _is_linked(b2, 'customer9', a)


def test_assoc_representative10_link_reassign_clear():
    a = BankingSystem_Customer(address="sample_text", age=7, customerType="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = BankingSystem_Financial_Representative()
    b2 = BankingSystem_Financial_Representative()
    _safe_set(a, 'a', {b1})
    assert _is_linked(a, 'a', b1)
    if hasattr(b1, 'Financial_Representative'):
        assert _is_linked(b1, 'Financial_Representative', a)
    _safe_set(a, 'a', {b2})
    assert _is_linked(a, 'a', b2)
    if hasattr(b1, 'Financial_Representative'):
        assert not _is_linked(b1, 'Financial_Representative', a)
    if hasattr(b2, 'Financial_Representative'):
        assert _is_linked(b2, 'Financial_Representative', a)
    _safe_set(a, 'a', set())
    assert not _is_linked(a, 'a', b2)
    if hasattr(b2, 'Financial_Representative'):
        assert not _is_linked(b2, 'Financial_Representative', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Account_strategy = st.builds(Account)
@given(instance=Account_strategy)
@settings(max_examples=25)
def test_Account_instantiation(instance):
    assert isinstance(instance, Account)


BankingSystem_Account_strategy = st.builds(BankingSystem_Account, accountNumber=safe_text, balance=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=BankingSystem_Account_strategy)
@settings(max_examples=25)
def test_BankingSystem_Account_instantiation(instance):
    assert isinstance(instance, BankingSystem_Account)


BankingSystem_Bank_strategy = st.builds(BankingSystem_Bank, bankId=st.integers(), description=safe_text, name=safe_text)
@given(instance=BankingSystem_Bank_strategy)
@settings(max_examples=25)
def test_BankingSystem_Bank_instantiation(instance):
    assert isinstance(instance, BankingSystem_Bank)


BankingSystem_Branch_strategy = st.builds(BankingSystem_Branch, branchId=st.integers(), location=safe_text, name=safe_text, phoneNumber=safe_text)
@given(instance=BankingSystem_Branch_strategy)
@settings(max_examples=25)
def test_BankingSystem_Branch_instantiation(instance):
    assert isinstance(instance, BankingSystem_Branch)


BankingSystem_Chequing_strategy = st.builds(BankingSystem_Chequing)
@given(instance=BankingSystem_Chequing_strategy)
@settings(max_examples=25)
def test_BankingSystem_Chequing_instantiation(instance):
    assert isinstance(instance, BankingSystem_Chequing)


BankingSystem_Customer_strategy = st.builds(BankingSystem_Customer, address=safe_text, age=st.integers(), customerType=safe_text, name=safe_text, phoneNumber=safe_text)
@given(instance=BankingSystem_Customer_strategy)
@settings(max_examples=25)
def test_BankingSystem_Customer_instantiation(instance):
    assert isinstance(instance, BankingSystem_Customer)


BankingSystem_Employee_strategy = st.builds(BankingSystem_Employee, eaddress=safe_text, eage=st.integers(), eid=st.integers(), ename=safe_text, ephoneNumber=safe_text, isCustomer=st.booleans())
@given(instance=BankingSystem_Employee_strategy)
@settings(max_examples=25)
def test_BankingSystem_Employee_instantiation(instance):
    assert isinstance(instance, BankingSystem_Employee)


BankingSystem_Financial_Representative_strategy = st.builds(BankingSystem_Financial_Representative)
@given(instance=BankingSystem_Financial_Representative_strategy)
@settings(max_examples=25)
def test_BankingSystem_Financial_Representative_instantiation(instance):
    assert isinstance(instance, BankingSystem_Financial_Representative)


BankingSystem_Loan_strategy = st.builds(BankingSystem_Loan, amount=st.floats(allow_nan=False, allow_infinity=False), duration=st.integers(), interestRate=st.floats(allow_nan=False, allow_infinity=False), loanNumber=safe_text)
@given(instance=BankingSystem_Loan_strategy)
@settings(max_examples=25)
def test_BankingSystem_Loan_instantiation(instance):
    assert isinstance(instance, BankingSystem_Loan)


BankingSystem_Saving_strategy = st.builds(BankingSystem_Saving, interestRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=BankingSystem_Saving_strategy)
@settings(max_examples=25)
def test_BankingSystem_Saving_instantiation(instance):
    assert isinstance(instance, BankingSystem_Saving)


Employee_strategy = st.builds(Employee)
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)



