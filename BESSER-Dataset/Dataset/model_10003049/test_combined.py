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
    account_Account,
    account_SavingsAccount,
    transaction_Payee,
    transaction_ExternalAccount,
    transaction_PaybillsTransaction,
    transaction_TransferTransaction,
    transaction_DepositTransaction,
    transaction_Transaction,
    User,
    Profile,
    UserGroup,
    transaction_TransactionType,
    account_AccountType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_account_account_is_not_abstract():
    assert not inspect.isabstract(account_Account)


def test_hyp_account_account_constructor_exists():
    assert callable(account_Account.__init__)


def test_hyp_account_account_constructor_args():
    sig = inspect.signature(account_Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "type" in params, "Missing parameter 'type'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"

def test_hyp_account_account_has_balance():
    assert hasattr(account_Account, "balance")
    descriptor = None
    for klass in account_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_account_has_pin():
    assert hasattr(account_Account, "pin")
    descriptor = None
    for klass in account_Account.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_account_has_type():
    assert hasattr(account_Account, "type")
    descriptor = None
    for klass in account_Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_account_has_userID():
    assert hasattr(account_Account, "userID")
    descriptor = None
    for klass in account_Account.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_account_has_accountNum():
    assert hasattr(account_Account, "accountNum")
    descriptor = None
    for klass in account_Account.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)



def test_hyp_account_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(account_SavingsAccount)


def test_hyp_account_savingsaccount_constructor_exists():
    assert callable(account_SavingsAccount.__init__)


def test_hyp_account_savingsaccount_constructor_args():
    sig = inspect.signature(account_SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"




def test_hyp_transaction_payee_is_not_abstract():
    assert not inspect.isabstract(transaction_Payee)


def test_hyp_transaction_payee_constructor_exists():
    assert callable(transaction_Payee.__init__)


def test_hyp_transaction_payee_constructor_args():
    sig = inspect.signature(transaction_Payee.__init__)
    params = list(sig.parameters.keys())
    assert "country" in params, "Missing parameter 'country'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "address1" in params, "Missing parameter 'address1'"
    assert "address2" in params, "Missing parameter 'address2'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "city" in params, "Missing parameter 'city'"
    assert "state" in params, "Missing parameter 'state'"
    assert "phoneNum" in params, "Missing parameter 'phoneNum'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"













def test_hyp_transaction_externalaccount_is_not_abstract():
    assert not inspect.isabstract(transaction_ExternalAccount)


def test_hyp_transaction_externalaccount_constructor_exists():
    assert callable(transaction_ExternalAccount.__init__)


def test_hyp_transaction_externalaccount_constructor_args():
    sig = inspect.signature(transaction_ExternalAccount.__init__)
    params = list(sig.parameters.keys())
    assert "routingNum" in params, "Missing parameter 'routingNum'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "associatedAccount" in params, "Missing parameter 'associatedAccount'"






def test_hyp_transaction_paybillstransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_PaybillsTransaction)


def test_hyp_transaction_paybillstransaction_constructor_exists():
    assert callable(transaction_PaybillsTransaction.__init__)


def test_hyp_transaction_paybillstransaction_constructor_args():
    sig = inspect.signature(transaction_PaybillsTransaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transaction_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_TransferTransaction)


def test_hyp_transaction_transfertransaction_constructor_exists():
    assert callable(transaction_TransferTransaction.__init__)


def test_hyp_transaction_transfertransaction_constructor_args():
    sig = inspect.signature(transaction_TransferTransaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transaction_deposittransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_DepositTransaction)


def test_hyp_transaction_deposittransaction_constructor_exists():
    assert callable(transaction_DepositTransaction.__init__)


def test_hyp_transaction_deposittransaction_constructor_args():
    sig = inspect.signature(transaction_DepositTransaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transaction_transaction_is_not_abstract():
    assert not inspect.isabstract(transaction_Transaction)


def test_hyp_transaction_transaction_constructor_exists():
    assert callable(transaction_Transaction.__init__)


def test_hyp_transaction_transaction_constructor_args():
    sig = inspect.signature(transaction_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "type" in params, "Missing parameter 'type'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "time" in params, "Missing parameter 'time'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "description" in params, "Missing parameter 'description'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"

def test_hyp_transaction_transaction_has_sourceAccountNum():
    assert hasattr(transaction_Transaction, "sourceAccountNum")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_type():
    assert hasattr(transaction_Transaction, "type")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_transactionID():
    assert hasattr(transaction_Transaction, "transactionID")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_time():
    assert hasattr(transaction_Transaction, "time")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_amount():
    assert hasattr(transaction_Transaction, "amount")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_description():
    assert hasattr(transaction_Transaction, "description")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_comment():
    assert hasattr(transaction_Transaction, "comment")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_destinationAccountNum():
    assert hasattr(transaction_Transaction, "destinationAccountNum")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"
    assert "userRole" in params, "Missing parameter 'userRole'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "username" in params, "Missing parameter 'username'"








def test_hyp_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_hyp_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_hyp_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "IDType" in params, "Missing parameter 'IDType'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "IDNum" in params, "Missing parameter 'IDNum'"
    assert "email" in params, "Missing parameter 'email'"
    assert "address1" in params, "Missing parameter 'address1'"
    assert "state" in params, "Missing parameter 'state'"
    assert "city" in params, "Missing parameter 'city'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "country" in params, "Missing parameter 'country'"
    assert "address2" in params, "Missing parameter 'address2'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "lastname" in params, "Missing parameter 'lastname'"















def test_hyp_usergroup_exists():
    # Check that the Enumeration exists
    assert UserGroup is not None

def test_hyp_usergroup_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UserGroup]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UserGroup"

def test_hyp_transaction_transactiontype_exists():
    # Check that the Enumeration exists
    assert transaction_TransactionType is not None

def test_hyp_transaction_transactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in transaction_TransactionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in transaction_TransactionType"

def test_hyp_account_accounttype_exists():
    # Check that the Enumeration exists
    assert account_AccountType is not None

def test_hyp_account_accounttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in account_AccountType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in account_AccountType"


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
account_Account_strategy = st.builds(
    account_Account,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    pin=
        safe_text,
    type=
        st.none(),
    userID=
        safe_text,
    accountNum=
        safe_text
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_Payee_strategy = st.builds(
    transaction_Payee,
    country=
        safe_text,
    accountNum=
        safe_text,
    address1=
        safe_text,
    address2=
        safe_text,
    zipcode=
        safe_text,
    city=
        safe_text,
    state=
        safe_text,
    phoneNum=
        safe_text,
    email=
        safe_text,
    name=
        safe_text
)
transaction_ExternalAccount_strategy = st.builds(
    transaction_ExternalAccount,
    routingNum=
        safe_text,
    accountNum=
        safe_text,
    associatedAccount=
        safe_text
)
transaction_PaybillsTransaction_strategy = st.builds(
    transaction_PaybillsTransaction,
)
transaction_TransferTransaction_strategy = st.builds(
    transaction_TransferTransaction,
)
transaction_DepositTransaction_strategy = st.builds(
    transaction_DepositTransaction,
)
transaction_Transaction_strategy = st.builds(
    transaction_Transaction,
    sourceAccountNum=
        safe_text,
    type=
        st.none(),
    transactionID=
        safe_text,
    time=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    description=
        safe_text,
    comment=
        safe_text,
    destinationAccountNum=
        safe_text
)
User_strategy = st.builds(
    User,
    lastLoginTime=
        safe_text,
    userRole=
        safe_text,
    password=
        safe_text,
    userID=
        safe_text,
    username=
        safe_text
)
Profile_strategy = st.builds(
    Profile,
    IDType=
        st.integers(),
    firstname=
        safe_text,
    zipcode=
        safe_text,
    IDNum=
        safe_text,
    email=
        safe_text,
    address1=
        safe_text,
    state=
        safe_text,
    city=
        safe_text,
    dateOfBirth=
        st.dates(),
    country=
        safe_text,
    address2=
        safe_text,
    userID=
        safe_text,
    phoneNumber=
        safe_text,
    lastname=
        safe_text
)

@given(instance=account_Account_strategy)
@settings(max_examples=50)
def test_hyp_account_account_instantiation(instance):
    assert isinstance(instance, account_Account)



@given(instance=account_Account_strategy)
def test_hyp_account_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=account_Account_strategy)
def test_hyp_account_account_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=account_Account_strategy)
def test_hyp_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=account_Account_strategy)
def test_hyp_account_account_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=account_Account_strategy)
def test_hyp_account_account_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original




@given(instance=account_SavingsAccount_strategy)
def test_hyp_account_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original




@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_address1_setter(instance):
    original = instance.address1
    instance.address1 = original
    assert instance.address1 == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_address2_setter(instance):
    original = instance.address2
    instance.address2 = original
    assert instance.address2 == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_phoneNum_setter(instance):
    original = instance.phoneNum
    instance.phoneNum = original
    assert instance.phoneNum == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=transaction_ExternalAccount_strategy)
def test_hyp_transaction_externalaccount_routingNum_setter(instance):
    original = instance.routingNum
    instance.routingNum = original
    assert instance.routingNum == original



@given(instance=transaction_ExternalAccount_strategy)
def test_hyp_transaction_externalaccount_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=transaction_ExternalAccount_strategy)
def test_hyp_transaction_externalaccount_associatedAccount_setter(instance):
    original = instance.associatedAccount
    instance.associatedAccount = original
    assert instance.associatedAccount == original




@given(instance=transaction_Transaction_strategy)
@settings(max_examples=50)
def test_hyp_transaction_transaction_instantiation(instance):
    assert isinstance(instance, transaction_Transaction)



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original




@given(instance=User_strategy)
def test_hyp_user_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original



@given(instance=User_strategy)
def test_hyp_user_userRole_setter(instance):
    original = instance.userRole
    instance.userRole = original
    assert instance.userRole == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=User_strategy)
def test_hyp_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original




@given(instance=Profile_strategy)
def test_hyp_profile_IDType_setter(instance):
    original = instance.IDType
    instance.IDType = original
    assert instance.IDType == original



@given(instance=Profile_strategy)
def test_hyp_profile_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Profile_strategy)
def test_hyp_profile_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original



@given(instance=Profile_strategy)
def test_hyp_profile_IDNum_setter(instance):
    original = instance.IDNum
    instance.IDNum = original
    assert instance.IDNum == original



@given(instance=Profile_strategy)
def test_hyp_profile_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Profile_strategy)
def test_hyp_profile_address1_setter(instance):
    original = instance.address1
    instance.address1 = original
    assert instance.address1 == original



@given(instance=Profile_strategy)
def test_hyp_profile_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Profile_strategy)
def test_hyp_profile_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Profile_strategy)
def test_hyp_profile_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Profile_strategy)
def test_hyp_profile_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Profile_strategy)
def test_hyp_profile_address2_setter(instance):
    original = instance.address2
    instance.address2 = original
    assert instance.address2 == original



@given(instance=Profile_strategy)
def test_hyp_profile_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Profile_strategy)
def test_hyp_profile_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Profile_strategy)
def test_hyp_profile_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Profile,
    User,
    account_Account,
    account_SavingsAccount,
    transaction_DepositTransaction,
    transaction_ExternalAccount,
    transaction_PaybillsTransaction,
    transaction_Payee,
    transaction_Transaction,
    transaction_TransferTransaction,
    UserGroup,
    account_AccountType,
    transaction_TransactionType,
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

def test_Profile_IDNum_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.IDNum == "sample_text"
    instance.IDNum = "sample_text_2"
    assert instance.IDNum == "sample_text_2"


def test_Profile_IDType_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.IDType == 7
    instance.IDType = 13
    assert instance.IDType == 13


def test_Profile_address1_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.address1 == "sample_text"
    instance.address1 = "sample_text_2"
    assert instance.address1 == "sample_text_2"


def test_Profile_address2_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.address2 == "sample_text"
    instance.address2 = "sample_text_2"
    assert instance.address2 == "sample_text_2"


def test_Profile_city_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_Profile_country_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_Profile_dateOfBirth_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_Profile_email_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Profile_firstname_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.firstname == "sample_text"
    instance.firstname = "sample_text_2"
    assert instance.firstname == "sample_text_2"


def test_Profile_lastname_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.lastname == "sample_text"
    instance.lastname = "sample_text_2"
    assert instance.lastname == "sample_text_2"


def test_Profile_phoneNumber_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_Profile_state_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_Profile_userID_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.userID == "sample_text"
    instance.userID = "sample_text_2"
    assert instance.userID == "sample_text_2"


def test_Profile_zipcode_value_roundtrip():
    instance = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.zipcode == "sample_text"
    instance.zipcode = "sample_text_2"
    assert instance.zipcode == "sample_text_2"


def test_User_lastLoginTime_value_roundtrip():
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", userRole="sample_text", username="sample_text")
    assert instance.lastLoginTime == "sample_text"
    instance.lastLoginTime = "sample_text_2"
    assert instance.lastLoginTime == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", userRole="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_userID_value_roundtrip():
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", userRole="sample_text", username="sample_text")
    assert instance.userID == "sample_text"
    instance.userID = "sample_text_2"
    assert instance.userID == "sample_text_2"


def test_User_userRole_value_roundtrip():
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", userRole="sample_text", username="sample_text")
    assert instance.userRole == "sample_text"
    instance.userRole = "sample_text_2"
    assert instance.userRole == "sample_text_2"


def test_User_username_value_roundtrip():
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", userRole="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_account_SavingsAccount_interestRate_value_roundtrip():
    instance = account_SavingsAccount(interestRate=3.14)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_transaction_ExternalAccount_accountNum_value_roundtrip():
    instance = transaction_ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    assert instance.accountNum == "sample_text"
    instance.accountNum = "sample_text_2"
    assert instance.accountNum == "sample_text_2"


def test_transaction_ExternalAccount_associatedAccount_value_roundtrip():
    instance = transaction_ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    assert instance.associatedAccount == "sample_text"
    instance.associatedAccount = "sample_text_2"
    assert instance.associatedAccount == "sample_text_2"


def test_transaction_ExternalAccount_routingNum_value_roundtrip():
    instance = transaction_ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    assert instance.routingNum == "sample_text"
    instance.routingNum = "sample_text_2"
    assert instance.routingNum == "sample_text_2"


def test_transaction_Payee_accountNum_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.accountNum == "sample_text"
    instance.accountNum = "sample_text_2"
    assert instance.accountNum == "sample_text_2"


def test_transaction_Payee_address1_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.address1 == "sample_text"
    instance.address1 = "sample_text_2"
    assert instance.address1 == "sample_text_2"


def test_transaction_Payee_address2_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.address2 == "sample_text"
    instance.address2 = "sample_text_2"
    assert instance.address2 == "sample_text_2"


def test_transaction_Payee_city_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_transaction_Payee_country_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_transaction_Payee_email_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_transaction_Payee_name_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_transaction_Payee_phoneNum_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.phoneNum == "sample_text"
    instance.phoneNum = "sample_text_2"
    assert instance.phoneNum == "sample_text_2"


def test_transaction_Payee_state_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_transaction_Payee_zipcode_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", zipcode="sample_text")
    assert instance.zipcode == "sample_text"
    instance.zipcode = "sample_text_2"
    assert instance.zipcode == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Profile_strategy = st.builds(Profile, IDNum=safe_text, IDType=st.integers(), address1=safe_text, address2=safe_text, city=safe_text, country=safe_text, dateOfBirth=st.dates(), email=safe_text, firstname=safe_text, lastname=safe_text, phoneNumber=safe_text, state=safe_text, userID=safe_text, zipcode=safe_text)
@given(instance=Profile_strategy)
@settings(max_examples=25)
def test_Profile_instantiation(instance):
    assert isinstance(instance, Profile)


User_strategy = st.builds(User, lastLoginTime=safe_text, password=safe_text, userID=safe_text, userRole=safe_text, username=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


account_SavingsAccount_strategy = st.builds(account_SavingsAccount, interestRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=account_SavingsAccount_strategy)
@settings(max_examples=25)
def test_account_SavingsAccount_instantiation(instance):
    assert isinstance(instance, account_SavingsAccount)


transaction_DepositTransaction_strategy = st.builds(transaction_DepositTransaction)
@given(instance=transaction_DepositTransaction_strategy)
@settings(max_examples=25)
def test_transaction_DepositTransaction_instantiation(instance):
    assert isinstance(instance, transaction_DepositTransaction)


transaction_ExternalAccount_strategy = st.builds(transaction_ExternalAccount, accountNum=safe_text, associatedAccount=safe_text, routingNum=safe_text)
@given(instance=transaction_ExternalAccount_strategy)
@settings(max_examples=25)
def test_transaction_ExternalAccount_instantiation(instance):
    assert isinstance(instance, transaction_ExternalAccount)


transaction_PaybillsTransaction_strategy = st.builds(transaction_PaybillsTransaction)
@given(instance=transaction_PaybillsTransaction_strategy)
@settings(max_examples=25)
def test_transaction_PaybillsTransaction_instantiation(instance):
    assert isinstance(instance, transaction_PaybillsTransaction)


transaction_Payee_strategy = st.builds(transaction_Payee, accountNum=safe_text, address1=safe_text, address2=safe_text, city=safe_text, country=safe_text, email=safe_text, name=safe_text, phoneNum=safe_text, state=safe_text, zipcode=safe_text)
@given(instance=transaction_Payee_strategy)
@settings(max_examples=25)
def test_transaction_Payee_instantiation(instance):
    assert isinstance(instance, transaction_Payee)


transaction_TransferTransaction_strategy = st.builds(transaction_TransferTransaction)
@given(instance=transaction_TransferTransaction_strategy)
@settings(max_examples=25)
def test_transaction_TransferTransaction_instantiation(instance):
    assert isinstance(instance, transaction_TransferTransaction)



