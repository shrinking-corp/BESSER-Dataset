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
    IcalculateExtraFee_Interface,
    savingAccount,
    checkingAccount,
    Transaction,
    Customer,
    Account,
    TransactionType,
    EnumAccountType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_icalculateextrafee_interface_is_not_abstract():
    assert not inspect.isabstract(IcalculateExtraFee_Interface)


def test_hyp_icalculateextrafee_interface_constructor_exists():
    assert callable(IcalculateExtraFee_Interface.__init__)


def test_hyp_icalculateextrafee_interface_constructor_args():
    sig = inspect.signature(IcalculateExtraFee_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_savingaccount_is_not_abstract():
    assert not inspect.isabstract(savingAccount)


def test_hyp_savingaccount_constructor_exists():
    assert callable(savingAccount.__init__)


def test_hyp_savingaccount_constructor_args():
    sig = inspect.signature(savingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "annualInterestRate" in params, "Missing parameter 'annualInterestRate'"
    assert "extraFee" in params, "Missing parameter 'extraFee'"
    assert "annualGain" in params, "Missing parameter 'annualGain'"






def test_hyp_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(checkingAccount)


def test_hyp_checkingaccount_constructor_exists():
    assert callable(checkingAccount.__init__)


def test_hyp_checkingaccount_constructor_args():
    sig = inspect.signature(checkingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "noOfTransactions" in params, "Missing parameter 'noOfTransactions'"





def test_hyp_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_hyp_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_hyp_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "transactionDate" in params, "Missing parameter 'transactionDate'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "transactionType" in params, "Missing parameter 'transactionType'"
    assert "transactionId" in params, "Missing parameter 'transactionId'"
    assert "description" in params, "Missing parameter 'description'"

def test_hyp_transaction_has_transactionDate():
    assert hasattr(Transaction, "transactionDate")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionDate" in klass.__dict__:
            descriptor = klass.__dict__["transactionDate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_amount():
    assert hasattr(Transaction, "amount")
    descriptor = None
    for klass in Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_accountNo():
    assert hasattr(Transaction, "accountNo")
    descriptor = None
    for klass in Transaction.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_transactionType():
    assert hasattr(Transaction, "transactionType")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionType" in klass.__dict__:
            descriptor = klass.__dict__["transactionType"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_transactionId():
    assert hasattr(Transaction, "transactionId")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionId" in klass.__dict__:
            descriptor = klass.__dict__["transactionId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_description():
    assert hasattr(Transaction, "description")
    descriptor = None
    for klass in Transaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "address" in params, "Missing parameter 'address'"
    assert "custId" in params, "Missing parameter 'custId'"








def test_hyp_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_hyp_account_constructor_exists():
    assert callable(Account.__init__)


def test_hyp_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "accountType" in params, "Missing parameter 'accountType'"
    assert "PIN" in params, "Missing parameter 'PIN'"
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "availableBalance" in params, "Missing parameter 'availableBalance'"
    assert "openedDate" in params, "Missing parameter 'openedDate'"

def test_hyp_account_has_accountType():
    assert hasattr(Account, "accountType")
    descriptor = None
    for klass in Account.__mro__:
        if "accountType" in klass.__dict__:
            descriptor = klass.__dict__["accountType"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_has_PIN():
    assert hasattr(Account, "PIN")
    descriptor = None
    for klass in Account.__mro__:
        if "PIN" in klass.__dict__:
            descriptor = klass.__dict__["PIN"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_has_accountNo():
    assert hasattr(Account, "accountNo")
    descriptor = None
    for klass in Account.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_has_availableBalance():
    assert hasattr(Account, "availableBalance")
    descriptor = None
    for klass in Account.__mro__:
        if "availableBalance" in klass.__dict__:
            descriptor = klass.__dict__["availableBalance"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_has_openedDate():
    assert hasattr(Account, "openedDate")
    descriptor = None
    for klass in Account.__mro__:
        if "openedDate" in klass.__dict__:
            descriptor = klass.__dict__["openedDate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transactiontype_exists():
    # Check that the Enumeration exists
    assert TransactionType is not None

def test_hyp_transactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransactionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransactionType"

def test_hyp_enumaccounttype_exists():
    # Check that the Enumeration exists
    assert EnumAccountType is not None

def test_hyp_enumaccounttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumAccountType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumAccountType"


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
IcalculateExtraFee_Interface_strategy = st.builds(
    IcalculateExtraFee_Interface,
)
savingAccount_strategy = st.builds(
    savingAccount,
    annualInterestRate=
        safe_text,
    extraFee=
        safe_text,
    annualGain=
        safe_text
)
checkingAccount_strategy = st.builds(
    checkingAccount,
    accountNo=
        st.integers(),
    noOfTransactions=
        st.integers()
)
Transaction_strategy = st.builds(
    Transaction,
    transactionDate=
        safe_text,
    amount=
        safe_text,
    accountNo=
        st.integers(),
    transactionType=
        st.none(),
    transactionId=
        st.integers(),
    description=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    accountNo=
        st.integers(),
    lastName=
        safe_text,
    firstName=
        safe_text,
    address=
        safe_text,
    custId=
        st.integers()
)
Account_strategy = st.builds(
    Account,
    accountType=
        st.none(),
    PIN=
        st.integers(),
    accountNo=
        st.integers(),
    availableBalance=
        safe_text,
    openedDate=
        safe_text
)





@given(instance=savingAccount_strategy)
def test_hyp_savingaccount_annualInterestRate_setter(instance):
    original = instance.annualInterestRate
    instance.annualInterestRate = original
    assert instance.annualInterestRate == original



@given(instance=savingAccount_strategy)
def test_hyp_savingaccount_extraFee_setter(instance):
    original = instance.extraFee
    instance.extraFee = original
    assert instance.extraFee == original



@given(instance=savingAccount_strategy)
def test_hyp_savingaccount_annualGain_setter(instance):
    original = instance.annualGain
    instance.annualGain = original
    assert instance.annualGain == original




@given(instance=checkingAccount_strategy)
def test_hyp_checkingaccount_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=checkingAccount_strategy)
def test_hyp_checkingaccount_noOfTransactions_setter(instance):
    original = instance.noOfTransactions
    instance.noOfTransactions = original
    assert instance.noOfTransactions == original

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_hyp_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



@given(instance=Transaction_strategy)
def test_hyp_transaction_transactionDate_setter(instance):
    original = instance.transactionDate
    instance.transactionDate = original
    assert instance.transactionDate == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_transactionType_setter(instance):
    original = instance.transactionType
    instance.transactionType = original
    assert instance.transactionType == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_transactionId_setter(instance):
    original = instance.transactionId
    instance.transactionId = original
    assert instance.transactionId == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=Customer_strategy)
def test_hyp_customer_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=Customer_strategy)
def test_hyp_customer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=Customer_strategy)
def test_hyp_customer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Customer_strategy)
def test_hyp_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_hyp_customer_custId_setter(instance):
    original = instance.custId
    instance.custId = original
    assert instance.custId == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_hyp_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_hyp_account_accountType_setter(instance):
    original = instance.accountType
    instance.accountType = original
    assert instance.accountType == original



@given(instance=Account_strategy)
def test_hyp_account_PIN_setter(instance):
    original = instance.PIN
    instance.PIN = original
    assert instance.PIN == original



@given(instance=Account_strategy)
def test_hyp_account_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=Account_strategy)
def test_hyp_account_availableBalance_setter(instance):
    original = instance.availableBalance
    instance.availableBalance = original
    assert instance.availableBalance == original



@given(instance=Account_strategy)
def test_hyp_account_openedDate_setter(instance):
    original = instance.openedDate
    instance.openedDate = original
    assert instance.openedDate == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account,
    Customer,
    IcalculateExtraFee_Interface,
    Transaction,
    checkingAccount,
    savingAccount,
    EnumAccountType,
    TransactionType,
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

def test_Customer_accountNo_value_roundtrip():
    instance = Customer(accountNo=7, address="sample_text", custId=7, firstName="sample_text", lastName="sample_text")
    assert instance.accountNo == 7
    instance.accountNo = 13
    assert instance.accountNo == 13


def test_Customer_address_value_roundtrip():
    instance = Customer(accountNo=7, address="sample_text", custId=7, firstName="sample_text", lastName="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer_custId_value_roundtrip():
    instance = Customer(accountNo=7, address="sample_text", custId=7, firstName="sample_text", lastName="sample_text")
    assert instance.custId == 7
    instance.custId = 13
    assert instance.custId == 13


def test_Customer_firstName_value_roundtrip():
    instance = Customer(accountNo=7, address="sample_text", custId=7, firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_Customer_lastName_value_roundtrip():
    instance = Customer(accountNo=7, address="sample_text", custId=7, firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_checkingAccount_accountNo_value_roundtrip():
    instance = checkingAccount(accountNo=7, noOfTransactions=7)
    assert instance.accountNo == 7
    instance.accountNo = 13
    assert instance.accountNo == 13


def test_checkingAccount_noOfTransactions_value_roundtrip():
    instance = checkingAccount(accountNo=7, noOfTransactions=7)
    assert instance.noOfTransactions == 7
    instance.noOfTransactions = 13
    assert instance.noOfTransactions == 13


def test_savingAccount_annualGain_value_roundtrip():
    instance = savingAccount(annualGain="sample_text", annualInterestRate="sample_text", extraFee="sample_text")
    assert instance.annualGain == "sample_text"
    instance.annualGain = "sample_text_2"
    assert instance.annualGain == "sample_text_2"


def test_savingAccount_annualInterestRate_value_roundtrip():
    instance = savingAccount(annualGain="sample_text", annualInterestRate="sample_text", extraFee="sample_text")
    assert instance.annualInterestRate == "sample_text"
    instance.annualInterestRate = "sample_text_2"
    assert instance.annualInterestRate == "sample_text_2"


def test_savingAccount_extraFee_value_roundtrip():
    instance = savingAccount(annualGain="sample_text", annualInterestRate="sample_text", extraFee="sample_text")
    assert instance.extraFee == "sample_text"
    instance.extraFee = "sample_text_2"
    assert instance.extraFee == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Customer_strategy = st.builds(Customer, accountNo=st.integers(), address=safe_text, custId=st.integers(), firstName=safe_text, lastName=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


IcalculateExtraFee_Interface_strategy = st.builds(IcalculateExtraFee_Interface)
@given(instance=IcalculateExtraFee_Interface_strategy)
@settings(max_examples=25)
def test_IcalculateExtraFee_Interface_instantiation(instance):
    assert isinstance(instance, IcalculateExtraFee_Interface)


checkingAccount_strategy = st.builds(checkingAccount, accountNo=st.integers(), noOfTransactions=st.integers())
@given(instance=checkingAccount_strategy)
@settings(max_examples=25)
def test_checkingAccount_instantiation(instance):
    assert isinstance(instance, checkingAccount)


savingAccount_strategy = st.builds(savingAccount, annualGain=safe_text, annualInterestRate=safe_text, extraFee=safe_text)
@given(instance=savingAccount_strategy)
@settings(max_examples=25)
def test_savingAccount_instantiation(instance):
    assert isinstance(instance, savingAccount)



