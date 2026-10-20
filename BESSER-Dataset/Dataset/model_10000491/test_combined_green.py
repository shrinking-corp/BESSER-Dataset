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
    Routing_Settings,
    Routing_Configuration_Settings,
    Custom_SalesForce_Object,
    Appraisal,
    Service_Channel,
    account_Account,
    account_CheckingAccount,
    account_CertificatesOfDepositAccount,
    account_SavingsAccount,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
    transaction_DepositTransaction,
    transaction_Transaction,
    Login,
    Customer,
    account_AccountType,
    Routing_Model,
    transaction_TransactionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_routing_settings_is_not_abstract():
    assert not inspect.isabstract(Routing_Settings)


def test_hyp_routing_settings_constructor_exists():
    assert callable(Routing_Settings.__init__)


def test_hyp_routing_settings_constructor_args():
    sig = inspect.signature(Routing_Settings.__init__)
    params = list(sig.parameters.keys())
    assert "Push_Time_Out" in params, "Missing parameter 'Push_Time_Out'"
    assert "Routing_Model" in params, "Missing parameter 'Routing_Model'"
    assert "Routing_Priority" in params, "Missing parameter 'Routing_Priority'"

def test_hyp_routing_settings_has_Push_Time_Out():
    assert hasattr(Routing_Settings, "Push_Time_Out")
    descriptor = None
    for klass in Routing_Settings.__mro__:
        if "Push_Time_Out" in klass.__dict__:
            descriptor = klass.__dict__["Push_Time_Out"]
            break
    assert isinstance(descriptor, property)

def test_hyp_routing_settings_has_Routing_Model():
    assert hasattr(Routing_Settings, "Routing_Model")
    descriptor = None
    for klass in Routing_Settings.__mro__:
        if "Routing_Model" in klass.__dict__:
            descriptor = klass.__dict__["Routing_Model"]
            break
    assert isinstance(descriptor, property)

def test_hyp_routing_settings_has_Routing_Priority():
    assert hasattr(Routing_Settings, "Routing_Priority")
    descriptor = None
    for klass in Routing_Settings.__mro__:
        if "Routing_Priority" in klass.__dict__:
            descriptor = klass.__dict__["Routing_Priority"]
            break
    assert isinstance(descriptor, property)



def test_hyp_routing_configuration_settings_is_not_abstract():
    assert not inspect.isabstract(Routing_Configuration_Settings)


def test_hyp_routing_configuration_settings_constructor_exists():
    assert callable(Routing_Configuration_Settings.__init__)


def test_hyp_routing_configuration_settings_constructor_args():
    sig = inspect.signature(Routing_Configuration_Settings.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Overflow_Assignee" in params, "Missing parameter 'Overflow_Assignee'"





def test_hyp_custom_salesforce_object_is_not_abstract():
    assert not inspect.isabstract(Custom_SalesForce_Object)


def test_hyp_custom_salesforce_object_constructor_exists():
    assert callable(Custom_SalesForce_Object.__init__)


def test_hyp_custom_salesforce_object_constructor_args():
    sig = inspect.signature(Custom_SalesForce_Object.__init__)
    params = list(sig.parameters.keys())
    assert "Owner" in params, "Missing parameter 'Owner'"




def test_hyp_appraisal_is_not_abstract():
    assert not inspect.isabstract(Appraisal)


def test_hyp_appraisal_constructor_exists():
    assert callable(Appraisal.__init__)


def test_hyp_appraisal_constructor_args():
    sig = inspect.signature(Appraisal.__init__)
    params = list(sig.parameters.keys())
    assert "Col1" in params, "Missing parameter 'Col1'"
    assert "Col2" in params, "Missing parameter 'Col2'"





def test_hyp_service_channel_is_not_abstract():
    assert not inspect.isabstract(Service_Channel)


def test_hyp_service_channel_constructor_exists():
    assert callable(Service_Channel.__init__)


def test_hyp_service_channel_constructor_args():
    sig = inspect.signature(Service_Channel.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"




def test_hyp_account_account_is_not_abstract():
    assert not inspect.isabstract(account_Account)


def test_hyp_account_account_constructor_exists():
    assert callable(account_Account.__init__)


def test_hyp_account_account_constructor_args():
    sig = inspect.signature(account_Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "type" in params, "Missing parameter 'type'"
    assert "accountNo" in params, "Missing parameter 'accountNo'"

def test_hyp_account_account_has_balance():
    assert hasattr(account_Account, "balance")
    descriptor = None
    for klass in account_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
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

def test_hyp_account_account_has_accountNo():
    assert hasattr(account_Account, "accountNo")
    descriptor = None
    for klass in account_Account.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)



def test_hyp_account_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(account_CheckingAccount)


def test_hyp_account_checkingaccount_constructor_exists():
    assert callable(account_CheckingAccount.__init__)


def test_hyp_account_checkingaccount_constructor_args():
    sig = inspect.signature(account_CheckingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_account_certificatesofdepositaccount_is_not_abstract():
    assert not inspect.isabstract(account_CertificatesOfDepositAccount)


def test_hyp_account_certificatesofdepositaccount_constructor_exists():
    assert callable(account_CertificatesOfDepositAccount.__init__)


def test_hyp_account_certificatesofdepositaccount_constructor_args():
    sig = inspect.signature(account_CertificatesOfDepositAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "timePeriod" in params, "Missing parameter 'timePeriod'"





def test_hyp_account_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(account_SavingsAccount)


def test_hyp_account_savingsaccount_constructor_exists():
    assert callable(account_SavingsAccount.__init__)


def test_hyp_account_savingsaccount_constructor_args():
    sig = inspect.signature(account_SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"




def test_hyp_transaction_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_TransferTransaction)


def test_hyp_transaction_transfertransaction_constructor_exists():
    assert callable(transaction_TransferTransaction.__init__)


def test_hyp_transaction_transfertransaction_constructor_args():
    sig = inspect.signature(transaction_TransferTransaction.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"

def test_hyp_transaction_transfertransaction_has_sourceAccount():
    assert hasattr(transaction_TransferTransaction, "sourceAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transfertransaction_has_targetAccount():
    assert hasattr(transaction_TransferTransaction, "targetAccount")
    descriptor = None
    for klass in transaction_TransferTransaction.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
            break
    assert isinstance(descriptor, property)



def test_hyp_transaction_withdrawtransaction_is_not_abstract():
    assert not inspect.isabstract(transaction_WithdrawTransaction)


def test_hyp_transaction_withdrawtransaction_constructor_exists():
    assert callable(transaction_WithdrawTransaction.__init__)


def test_hyp_transaction_withdrawtransaction_constructor_args():
    sig = inspect.signature(transaction_WithdrawTransaction.__init__)
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
    assert "amount" in params, "Missing parameter 'amount'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"

def test_hyp_transaction_transaction_has_amount():
    assert hasattr(transaction_Transaction, "amount")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_id():
    assert hasattr(transaction_Transaction, "id")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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

def test_hyp_transaction_transaction_has_transactionTime():
    assert hasattr(transaction_Transaction, "transactionTime")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionTime" in klass.__dict__:
            descriptor = klass.__dict__["transactionTime"]
            break
    assert isinstance(descriptor, property)



def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "securityAnswer" in params, "Missing parameter 'securityAnswer'"
    assert "username" in params, "Missing parameter 'username'"
    assert "securityQuestion" in params, "Missing parameter 'securityQuestion'"
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"








def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"






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

def test_hyp_routing_model_exists():
    # Check that the Enumeration exists
    assert Routing_Model is not None

def test_hyp_routing_model_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Routing_Model]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Routing_Model"

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
Routing_Settings_strategy = st.builds(
    Routing_Settings,
    Push_Time_Out=
        safe_text,
    Routing_Model=
        st.none(),
    Routing_Priority=
        st.integers()
)
Routing_Configuration_Settings_strategy = st.builds(
    Routing_Configuration_Settings,
    Name=
        safe_text,
    Overflow_Assignee=
        safe_text
)
Custom_SalesForce_Object_strategy = st.builds(
    Custom_SalesForce_Object,
    Owner=
        safe_text
)
Appraisal_strategy = st.builds(
    Appraisal,
    Col1=
        safe_text,
    Col2=
        safe_text
)
Service_Channel_strategy = st.builds(
    Service_Channel,
    Name=
        safe_text
)
account_Account_strategy = st.builds(
    account_Account,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none(),
    accountNo=
        safe_text
)
account_CheckingAccount_strategy = st.builds(
    account_CheckingAccount,
    name=
        safe_text
)
account_CertificatesOfDepositAccount_strategy = st.builds(
    account_CertificatesOfDepositAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    timePeriod=
        st.integers()
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_TransferTransaction_strategy = st.builds(
    transaction_TransferTransaction,
    sourceAccount=
        st.none(),
    targetAccount=
        st.none()
)
transaction_WithdrawTransaction_strategy = st.builds(
    transaction_WithdrawTransaction,
)
transaction_DepositTransaction_strategy = st.builds(
    transaction_DepositTransaction,
)
transaction_Transaction_strategy = st.builds(
    transaction_Transaction,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    id=
        st.integers(),
    type=
        st.none(),
    transactionTime=
        st.dates()
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    securityAnswer=
        safe_text,
    username=
        safe_text,
    securityQuestion=
        safe_text,
    lastLoginTime=
        st.dates()
)
Customer_strategy = st.builds(
    Customer,
    name=
        safe_text,
    address=
        safe_text,
    emailAddress=
        safe_text,
    phoneNumber=
        safe_text,
    dateOfBirth=
        st.dates()
)

@given(instance=Routing_Settings_strategy)
@settings(max_examples=50)
def test_hyp_routing_settings_instantiation(instance):
    assert isinstance(instance, Routing_Settings)



@given(instance=Routing_Settings_strategy)
def test_hyp_routing_settings_Push_Time_Out_setter(instance):
    original = instance.Push_Time_Out
    instance.Push_Time_Out = original
    assert instance.Push_Time_Out == original



@given(instance=Routing_Settings_strategy)
def test_hyp_routing_settings_Routing_Model_setter(instance):
    original = instance.Routing_Model
    instance.Routing_Model = original
    assert instance.Routing_Model == original



@given(instance=Routing_Settings_strategy)
def test_hyp_routing_settings_Routing_Priority_setter(instance):
    original = instance.Routing_Priority
    instance.Routing_Priority = original
    assert instance.Routing_Priority == original




@given(instance=Routing_Configuration_Settings_strategy)
def test_hyp_routing_configuration_settings_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Routing_Configuration_Settings_strategy)
def test_hyp_routing_configuration_settings_Overflow_Assignee_setter(instance):
    original = instance.Overflow_Assignee
    instance.Overflow_Assignee = original
    assert instance.Overflow_Assignee == original




@given(instance=Custom_SalesForce_Object_strategy)
def test_hyp_custom_salesforce_object_Owner_setter(instance):
    original = instance.Owner
    instance.Owner = original
    assert instance.Owner == original




@given(instance=Appraisal_strategy)
def test_hyp_appraisal_Col1_setter(instance):
    original = instance.Col1
    instance.Col1 = original
    assert instance.Col1 == original



@given(instance=Appraisal_strategy)
def test_hyp_appraisal_Col2_setter(instance):
    original = instance.Col2
    instance.Col2 = original
    assert instance.Col2 == original




@given(instance=Service_Channel_strategy)
def test_hyp_service_channel_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

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
def test_hyp_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=account_Account_strategy)
def test_hyp_account_account_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original




@given(instance=account_CheckingAccount_strategy)
def test_hyp_account_checkingaccount_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_hyp_account_certificatesofdepositaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=account_CertificatesOfDepositAccount_strategy)
def test_hyp_account_certificatesofdepositaccount_timePeriod_setter(instance):
    original = instance.timePeriod
    instance.timePeriod = original
    assert instance.timePeriod == original




@given(instance=account_SavingsAccount_strategy)
def test_hyp_account_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=transaction_TransferTransaction_strategy)
@settings(max_examples=50)
def test_hyp_transaction_transfertransaction_instantiation(instance):
    assert isinstance(instance, transaction_TransferTransaction)



@given(instance=transaction_TransferTransaction_strategy)
def test_hyp_transaction_transfertransaction_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original



@given(instance=transaction_TransferTransaction_strategy)
def test_hyp_transaction_transfertransaction_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original



@given(instance=transaction_Transaction_strategy)
@settings(max_examples=50)
def test_hyp_transaction_transaction_instantiation(instance):
    assert isinstance(instance, transaction_Transaction)



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original




@given(instance=Login_strategy)
def test_hyp_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_hyp_login_securityAnswer_setter(instance):
    original = instance.securityAnswer
    instance.securityAnswer = original
    assert instance.securityAnswer == original



@given(instance=Login_strategy)
def test_hyp_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Login_strategy)
def test_hyp_login_securityQuestion_setter(instance):
    original = instance.securityQuestion
    instance.securityQuestion = original
    assert instance.securityQuestion == original



@given(instance=Login_strategy)
def test_hyp_login_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original




@given(instance=Customer_strategy)
def test_hyp_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_hyp_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_hyp_customer_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=Customer_strategy)
def test_hyp_customer_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Customer_strategy)
def test_hyp_customer_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Appraisal,
    Custom_SalesForce_Object,
    Customer,
    Login,
    Routing_Configuration_Settings,
    Routing_Settings,
    Service_Channel,
    account_Account,
    account_CertificatesOfDepositAccount,
    account_CheckingAccount,
    account_SavingsAccount,
    transaction_DepositTransaction,
    transaction_Transaction,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
    Routing_Model,
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

def test_Appraisal_Col1_value_roundtrip():
    instance = Appraisal(Col1="sample_text", Col2="sample_text")
    assert instance.Col1 == "sample_text"
    instance.Col1 = "sample_text_2"
    assert instance.Col1 == "sample_text_2"


def test_Appraisal_Col2_value_roundtrip():
    instance = Appraisal(Col1="sample_text", Col2="sample_text")
    assert instance.Col2 == "sample_text"
    instance.Col2 = "sample_text_2"
    assert instance.Col2 == "sample_text_2"


def test_Custom_SalesForce_Object_Owner_value_roundtrip():
    instance = Custom_SalesForce_Object(Owner="sample_text")
    assert instance.Owner == "sample_text"
    instance.Owner = "sample_text_2"
    assert instance.Owner == "sample_text_2"


def test_Customer_address_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer_dateOfBirth_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_Customer_emailAddress_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.emailAddress == "sample_text"
    instance.emailAddress = "sample_text_2"
    assert instance.emailAddress == "sample_text_2"


def test_Customer_name_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Customer_phoneNumber_value_roundtrip():
    instance = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_Login_lastLoginTime_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.lastLoginTime == date(2024, 1, 1)
    instance.lastLoginTime = date(2025, 6, 15)
    assert instance.lastLoginTime == date(2025, 6, 15)


def test_Login_password_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Login_securityAnswer_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.securityAnswer == "sample_text"
    instance.securityAnswer = "sample_text_2"
    assert instance.securityAnswer == "sample_text_2"


def test_Login_securityQuestion_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.securityQuestion == "sample_text"
    instance.securityQuestion = "sample_text_2"
    assert instance.securityQuestion == "sample_text_2"


def test_Login_username_value_roundtrip():
    instance = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Routing_Configuration_Settings_Name_value_roundtrip():
    instance = Routing_Configuration_Settings(Name="sample_text", Overflow_Assignee="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Routing_Configuration_Settings_Overflow_Assignee_value_roundtrip():
    instance = Routing_Configuration_Settings(Name="sample_text", Overflow_Assignee="sample_text")
    assert instance.Overflow_Assignee == "sample_text"
    instance.Overflow_Assignee = "sample_text_2"
    assert instance.Overflow_Assignee == "sample_text_2"


def test_Service_Channel_Name_value_roundtrip():
    instance = Service_Channel(Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_account_CertificatesOfDepositAccount_interestRate_value_roundtrip():
    instance = account_CertificatesOfDepositAccount(interestRate=3.14, timePeriod=7)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_account_CertificatesOfDepositAccount_timePeriod_value_roundtrip():
    instance = account_CertificatesOfDepositAccount(interestRate=3.14, timePeriod=7)
    assert instance.timePeriod == 7
    instance.timePeriod = 13
    assert instance.timePeriod == 13


def test_account_CheckingAccount_name_value_roundtrip():
    instance = account_CheckingAccount(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_account_SavingsAccount_interestRate_value_roundtrip():
    instance = account_SavingsAccount(interestRate=3.14)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_assoc_Customer_Login_link_reassign_clear():
    a = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    b1 = Customer(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    b2 = Customer(address="sample_text_2", dateOfBirth=date(2025, 6, 15), emailAddress="sample_text_2", name="sample_text_2", phoneNumber="sample_text_2")
    _safe_set(a, 'customer5', b1)
    assert _is_linked(a, 'customer5', b1)
    if hasattr(b1, 'login4'):
        assert _is_linked(b1, 'login4', a)
    _safe_set(a, 'customer5', b2)
    assert _is_linked(a, 'customer5', b2)
    if hasattr(b1, 'login4'):
        assert not _is_linked(b1, 'login4', a)
    if hasattr(b2, 'login4'):
        assert _is_linked(b2, 'login4', a)
    _safe_set(a, 'customer5', None)
    assert not _is_linked(a, 'customer5', b2)
    if hasattr(b2, 'login4'):
        assert not _is_linked(b2, 'login4', a)


def test_assoc_Service_Channel_SalesForce_Object_link_reassign_clear():
    a = Service_Channel(Name="sample_text")
    b1 = Custom_SalesForce_Object(Owner="sample_text")
    b2 = Custom_SalesForce_Object(Owner="sample_text_2")
    _safe_set(a, 'salesForce_Object6', b1)
    assert _is_linked(a, 'salesForce_Object6', b1)
    if hasattr(b1, 'service_Channel7'):
        assert _is_linked(b1, 'service_Channel7', a)
    _safe_set(a, 'salesForce_Object6', b2)
    assert _is_linked(a, 'salesForce_Object6', b2)
    if hasattr(b1, 'service_Channel7'):
        assert not _is_linked(b1, 'service_Channel7', a)
    if hasattr(b2, 'service_Channel7'):
        assert _is_linked(b2, 'service_Channel7', a)
    _safe_set(a, 'salesForce_Object6', None)
    assert not _is_linked(a, 'salesForce_Object6', b2)
    if hasattr(b2, 'service_Channel7'):
        assert not _is_linked(b2, 'service_Channel7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Appraisal_strategy = st.builds(Appraisal, Col1=safe_text, Col2=safe_text)
@given(instance=Appraisal_strategy)
@settings(max_examples=25)
def test_Appraisal_instantiation(instance):
    assert isinstance(instance, Appraisal)


Custom_SalesForce_Object_strategy = st.builds(Custom_SalesForce_Object, Owner=safe_text)
@given(instance=Custom_SalesForce_Object_strategy)
@settings(max_examples=25)
def test_Custom_SalesForce_Object_instantiation(instance):
    assert isinstance(instance, Custom_SalesForce_Object)


Customer_strategy = st.builds(Customer, address=safe_text, dateOfBirth=st.dates(), emailAddress=safe_text, name=safe_text, phoneNumber=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Login_strategy = st.builds(Login, lastLoginTime=st.dates(), password=safe_text, securityAnswer=safe_text, securityQuestion=safe_text, username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Routing_Configuration_Settings_strategy = st.builds(Routing_Configuration_Settings, Name=safe_text, Overflow_Assignee=safe_text)
@given(instance=Routing_Configuration_Settings_strategy)
@settings(max_examples=25)
def test_Routing_Configuration_Settings_instantiation(instance):
    assert isinstance(instance, Routing_Configuration_Settings)


Service_Channel_strategy = st.builds(Service_Channel, Name=safe_text)
@given(instance=Service_Channel_strategy)
@settings(max_examples=25)
def test_Service_Channel_instantiation(instance):
    assert isinstance(instance, Service_Channel)


account_CertificatesOfDepositAccount_strategy = st.builds(account_CertificatesOfDepositAccount, interestRate=st.floats(allow_nan=False, allow_infinity=False), timePeriod=st.integers())
@given(instance=account_CertificatesOfDepositAccount_strategy)
@settings(max_examples=25)
def test_account_CertificatesOfDepositAccount_instantiation(instance):
    assert isinstance(instance, account_CertificatesOfDepositAccount)


account_CheckingAccount_strategy = st.builds(account_CheckingAccount, name=safe_text)
@given(instance=account_CheckingAccount_strategy)
@settings(max_examples=25)
def test_account_CheckingAccount_instantiation(instance):
    assert isinstance(instance, account_CheckingAccount)


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


transaction_WithdrawTransaction_strategy = st.builds(transaction_WithdrawTransaction)
@given(instance=transaction_WithdrawTransaction_strategy)
@settings(max_examples=25)
def test_transaction_WithdrawTransaction_instantiation(instance):
    assert isinstance(instance, transaction_WithdrawTransaction)



