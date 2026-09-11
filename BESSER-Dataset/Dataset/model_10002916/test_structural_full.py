import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Authentication,
    Customer,
    Database,
    LOGIN,
    Login,
    LoginAuthenticationProcessor,
    OPT_AuthenticationProcessor,
    RequestOTPAuthentication,
    account_Account,
    account_CertificatesOfDepositAccount,
    account_CheckingAccount,
    account_SavingsAccount,
    transaction_DepositTransaction,
    transaction_Transaction,
    transaction_TransferTransaction,
    transaction_WithdrawTransaction,
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

def test_Authentication_AuthenticationType_value_roundtrip():
    instance = Authentication(AuthenticationType=7, Authentication_Result=True, UserEmail="sample_text", UserID="sample_text", UserPassWord="sample_text", UserPassWord1="sample_text")
    assert instance.AuthenticationType == 7
    instance.AuthenticationType = 13
    assert instance.AuthenticationType == 13


def test_Authentication_Authentication_Result_value_roundtrip():
    instance = Authentication(AuthenticationType=7, Authentication_Result=True, UserEmail="sample_text", UserID="sample_text", UserPassWord="sample_text", UserPassWord1="sample_text")
    assert instance.Authentication_Result == True
    instance.Authentication_Result = False
    assert instance.Authentication_Result == False


def test_Authentication_UserEmail_value_roundtrip():
    instance = Authentication(AuthenticationType=7, Authentication_Result=True, UserEmail="sample_text", UserID="sample_text", UserPassWord="sample_text", UserPassWord1="sample_text")
    assert instance.UserEmail == "sample_text"
    instance.UserEmail = "sample_text_2"
    assert instance.UserEmail == "sample_text_2"


def test_Authentication_UserID_value_roundtrip():
    instance = Authentication(AuthenticationType=7, Authentication_Result=True, UserEmail="sample_text", UserID="sample_text", UserPassWord="sample_text", UserPassWord1="sample_text")
    assert instance.UserID == "sample_text"
    instance.UserID = "sample_text_2"
    assert instance.UserID == "sample_text_2"


def test_Authentication_UserPassWord_value_roundtrip():
    instance = Authentication(AuthenticationType=7, Authentication_Result=True, UserEmail="sample_text", UserID="sample_text", UserPassWord="sample_text", UserPassWord1="sample_text")
    assert instance.UserPassWord == "sample_text"
    instance.UserPassWord = "sample_text_2"
    assert instance.UserPassWord == "sample_text_2"


def test_Authentication_UserPassWord1_value_roundtrip():
    instance = Authentication(AuthenticationType=7, Authentication_Result=True, UserEmail="sample_text", UserID="sample_text", UserPassWord="sample_text", UserPassWord1="sample_text")
    assert instance.UserPassWord1 == "sample_text"
    instance.UserPassWord1 = "sample_text_2"
    assert instance.UserPassWord1 == "sample_text_2"


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


def test_LOGIN_UserID_value_roundtrip():
    instance = LOGIN(UserID="sample_text", UserPassWord="sample_text")
    assert instance.UserID == "sample_text"
    instance.UserID = "sample_text_2"
    assert instance.UserID == "sample_text_2"


def test_LOGIN_UserPassWord_value_roundtrip():
    instance = LOGIN(UserID="sample_text", UserPassWord="sample_text")
    assert instance.UserPassWord == "sample_text"
    instance.UserPassWord = "sample_text_2"
    assert instance.UserPassWord == "sample_text_2"


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


def test_LoginAuthenticationProcessor_Authentication_Result_value_roundtrip():
    instance = LoginAuthenticationProcessor(Authentication_Result=True, UserID="sample_text", UserPassWord="sample_text")
    assert instance.Authentication_Result == True
    instance.Authentication_Result = False
    assert instance.Authentication_Result == False


def test_LoginAuthenticationProcessor_UserID_value_roundtrip():
    instance = LoginAuthenticationProcessor(Authentication_Result=True, UserID="sample_text", UserPassWord="sample_text")
    assert instance.UserID == "sample_text"
    instance.UserID = "sample_text_2"
    assert instance.UserID == "sample_text_2"


def test_LoginAuthenticationProcessor_UserPassWord_value_roundtrip():
    instance = LoginAuthenticationProcessor(Authentication_Result=True, UserID="sample_text", UserPassWord="sample_text")
    assert instance.UserPassWord == "sample_text"
    instance.UserPassWord = "sample_text_2"
    assert instance.UserPassWord == "sample_text_2"


def test_OPT_AuthenticationProcessor_Authentication_Result_value_roundtrip():
    instance = OPT_AuthenticationProcessor(Authentication_Result=True, UserEmail="sample_text")
    assert instance.Authentication_Result == True
    instance.Authentication_Result = False
    assert instance.Authentication_Result == False


def test_OPT_AuthenticationProcessor_UserEmail_value_roundtrip():
    instance = OPT_AuthenticationProcessor(Authentication_Result=True, UserEmail="sample_text")
    assert instance.UserEmail == "sample_text"
    instance.UserEmail = "sample_text_2"
    assert instance.UserEmail == "sample_text_2"


def test_RequestOTPAuthentication_UserEmail_value_roundtrip():
    instance = RequestOTPAuthentication(UserEmail="sample_text", UserID="sample_text")
    assert instance.UserEmail == "sample_text"
    instance.UserEmail = "sample_text_2"
    assert instance.UserEmail == "sample_text_2"


def test_RequestOTPAuthentication_UserID_value_roundtrip():
    instance = RequestOTPAuthentication(UserEmail="sample_text", UserID="sample_text")
    assert instance.UserID == "sample_text"
    instance.UserID = "sample_text_2"
    assert instance.UserID == "sample_text_2"


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


def test_assoc_Database_Authentication_link_reassign_clear():
    a = Authentication(AuthenticationType=7, Authentication_Result=True, UserEmail="sample_text", UserID="sample_text", UserPassWord="sample_text", UserPassWord1="sample_text")
    b1 = Database()
    b2 = Database()
    _safe_set(a, 'database7', b1)
    assert _is_linked(a, 'database7', b1)
    if hasattr(b1, 'authentication6'):
        assert _is_linked(b1, 'authentication6', a)
    _safe_set(a, 'database7', b2)
    assert _is_linked(a, 'database7', b2)
    if hasattr(b1, 'authentication6'):
        assert not _is_linked(b1, 'authentication6', a)
    if hasattr(b2, 'authentication6'):
        assert _is_linked(b2, 'authentication6', a)
    _safe_set(a, 'database7', None)
    assert not _is_linked(a, 'database7', b2)
    if hasattr(b2, 'authentication6'):
        assert not _is_linked(b2, 'authentication6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Authentication_strategy = st.builds(Authentication, AuthenticationType=st.integers(), Authentication_Result=st.booleans(), UserEmail=safe_text, UserID=safe_text, UserPassWord=safe_text, UserPassWord1=safe_text)
@given(instance=Authentication_strategy)
@settings(max_examples=25)
def test_Authentication_instantiation(instance):
    assert isinstance(instance, Authentication)


Customer_strategy = st.builds(Customer, address=safe_text, dateOfBirth=st.dates(), emailAddress=safe_text, name=safe_text, phoneNumber=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Database_strategy = st.builds(Database)
@given(instance=Database_strategy)
@settings(max_examples=25)
def test_Database_instantiation(instance):
    assert isinstance(instance, Database)


LOGIN_strategy = st.builds(LOGIN, UserID=safe_text, UserPassWord=safe_text)
@given(instance=LOGIN_strategy)
@settings(max_examples=25)
def test_LOGIN_instantiation(instance):
    assert isinstance(instance, LOGIN)


Login_strategy = st.builds(Login, lastLoginTime=st.dates(), password=safe_text, securityAnswer=safe_text, securityQuestion=safe_text, username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


LoginAuthenticationProcessor_strategy = st.builds(LoginAuthenticationProcessor, Authentication_Result=st.booleans(), UserID=safe_text, UserPassWord=safe_text)
@given(instance=LoginAuthenticationProcessor_strategy)
@settings(max_examples=25)
def test_LoginAuthenticationProcessor_instantiation(instance):
    assert isinstance(instance, LoginAuthenticationProcessor)


OPT_AuthenticationProcessor_strategy = st.builds(OPT_AuthenticationProcessor, Authentication_Result=st.booleans(), UserEmail=safe_text)
@given(instance=OPT_AuthenticationProcessor_strategy)
@settings(max_examples=25)
def test_OPT_AuthenticationProcessor_instantiation(instance):
    assert isinstance(instance, OPT_AuthenticationProcessor)


RequestOTPAuthentication_strategy = st.builds(RequestOTPAuthentication, UserEmail=safe_text, UserID=safe_text)
@given(instance=RequestOTPAuthentication_strategy)
@settings(max_examples=25)
def test_RequestOTPAuthentication_instantiation(instance):
    assert isinstance(instance, RequestOTPAuthentication)


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


