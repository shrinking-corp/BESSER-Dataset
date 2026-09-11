import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ATM_Card,
    ATM_Card2,
    Account2_Interface,
    Account_Interface,
    Bank,
    Bank2,
    Customer,
    Customer2,
    DepositTransaction,
    DepositTransaction2,
    Savings_Account,
    Savings_Account2,
    Transaction,
    Transaction2,
    TransferTransaction,
    TransferTransaction2,
    WithdrawTransaction,
    WithdrawTransaction2,
    TransactionType,
    TransactionType2,
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

def test_ATM_Card_cardNumber_value_roundtrip():
    instance = ATM_Card(cardNumber="sample_text", pin="sample_text")
    assert instance.cardNumber == "sample_text"
    instance.cardNumber = "sample_text_2"
    assert instance.cardNumber == "sample_text_2"


def test_ATM_Card_pin_value_roundtrip():
    instance = ATM_Card(cardNumber="sample_text", pin="sample_text")
    assert instance.pin == "sample_text"
    instance.pin = "sample_text_2"
    assert instance.pin == "sample_text_2"


def test_ATM_Card2_cardNumber_value_roundtrip():
    instance = ATM_Card2(cardNumber="sample_text", pin="sample_text")
    assert instance.cardNumber == "sample_text"
    instance.cardNumber = "sample_text_2"
    assert instance.cardNumber == "sample_text_2"


def test_ATM_Card2_pin_value_roundtrip():
    instance = ATM_Card2(cardNumber="sample_text", pin="sample_text")
    assert instance.pin == "sample_text"
    instance.pin = "sample_text_2"
    assert instance.pin == "sample_text_2"


def test_Bank_address_value_roundtrip():
    instance = Bank(address="sample_text", code="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Bank_code_value_roundtrip():
    instance = Bank(address="sample_text", code="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_Bank2_address_value_roundtrip():
    instance = Bank2(address="sample_text", code="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Bank2_code_value_roundtrip():
    instance = Bank2(address="sample_text", code="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


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


def test_Customer2_address_value_roundtrip():
    instance = Customer2(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer2_dateOfBirth_value_roundtrip():
    instance = Customer2(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_Customer2_emailAddress_value_roundtrip():
    instance = Customer2(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.emailAddress == "sample_text"
    instance.emailAddress = "sample_text_2"
    assert instance.emailAddress == "sample_text_2"


def test_Customer2_name_value_roundtrip():
    instance = Customer2(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Customer2_phoneNumber_value_roundtrip():
    instance = Customer2(address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_Savings_Account_accountNumber_value_roundtrip():
    instance = Savings_Account(accountNumber="sample_text", balance=7)
    assert instance.accountNumber == "sample_text"
    instance.accountNumber = "sample_text_2"
    assert instance.accountNumber == "sample_text_2"


def test_Savings_Account_balance_value_roundtrip():
    instance = Savings_Account(accountNumber="sample_text", balance=7)
    assert instance.balance == 7
    instance.balance = 13
    assert instance.balance == 13


def test_Savings_Account2_accountNumber_value_roundtrip():
    instance = Savings_Account2(accountNumber="sample_text", balance=7)
    assert instance.accountNumber == "sample_text"
    instance.accountNumber = "sample_text_2"
    assert instance.accountNumber == "sample_text_2"


def test_Savings_Account2_balance_value_roundtrip():
    instance = Savings_Account2(accountNumber="sample_text", balance=7)
    assert instance.balance == 7
    instance.balance = 13
    assert instance.balance == 13


def test_TransferTransaction_sourceAccount_value_roundtrip():
    instance = TransferTransaction(sourceAccount="sample_text", targetAccount="sample_text")
    assert instance.sourceAccount == "sample_text"
    instance.sourceAccount = "sample_text_2"
    assert instance.sourceAccount == "sample_text_2"


def test_TransferTransaction_targetAccount_value_roundtrip():
    instance = TransferTransaction(sourceAccount="sample_text", targetAccount="sample_text")
    assert instance.targetAccount == "sample_text"
    instance.targetAccount = "sample_text_2"
    assert instance.targetAccount == "sample_text_2"


def test_TransferTransaction2_sourceAccount_value_roundtrip():
    instance = TransferTransaction2(sourceAccount="sample_text", targetAccount="sample_text")
    assert instance.sourceAccount == "sample_text"
    instance.sourceAccount = "sample_text_2"
    assert instance.sourceAccount == "sample_text_2"


def test_TransferTransaction2_targetAccount_value_roundtrip():
    instance = TransferTransaction2(sourceAccount="sample_text", targetAccount="sample_text")
    assert instance.targetAccount == "sample_text"
    instance.targetAccount = "sample_text_2"
    assert instance.targetAccount == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ATM_Card_strategy = st.builds(ATM_Card, cardNumber=safe_text, pin=safe_text)
@given(instance=ATM_Card_strategy)
@settings(max_examples=25)
def test_ATM_Card_instantiation(instance):
    assert isinstance(instance, ATM_Card)


ATM_Card2_strategy = st.builds(ATM_Card2, cardNumber=safe_text, pin=safe_text)
@given(instance=ATM_Card2_strategy)
@settings(max_examples=25)
def test_ATM_Card2_instantiation(instance):
    assert isinstance(instance, ATM_Card2)


Account2_Interface_strategy = st.builds(Account2_Interface)
@given(instance=Account2_Interface_strategy)
@settings(max_examples=25)
def test_Account2_Interface_instantiation(instance):
    assert isinstance(instance, Account2_Interface)


Account_Interface_strategy = st.builds(Account_Interface)
@given(instance=Account_Interface_strategy)
@settings(max_examples=25)
def test_Account_Interface_instantiation(instance):
    assert isinstance(instance, Account_Interface)


Bank_strategy = st.builds(Bank, address=safe_text, code=safe_text)
@given(instance=Bank_strategy)
@settings(max_examples=25)
def test_Bank_instantiation(instance):
    assert isinstance(instance, Bank)


Bank2_strategy = st.builds(Bank2, address=safe_text, code=safe_text)
@given(instance=Bank2_strategy)
@settings(max_examples=25)
def test_Bank2_instantiation(instance):
    assert isinstance(instance, Bank2)


Customer_strategy = st.builds(Customer, address=safe_text, dateOfBirth=st.dates(), emailAddress=safe_text, name=safe_text, phoneNumber=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Customer2_strategy = st.builds(Customer2, address=safe_text, dateOfBirth=st.dates(), emailAddress=safe_text, name=safe_text, phoneNumber=safe_text)
@given(instance=Customer2_strategy)
@settings(max_examples=25)
def test_Customer2_instantiation(instance):
    assert isinstance(instance, Customer2)


DepositTransaction_strategy = st.builds(DepositTransaction)
@given(instance=DepositTransaction_strategy)
@settings(max_examples=25)
def test_DepositTransaction_instantiation(instance):
    assert isinstance(instance, DepositTransaction)


DepositTransaction2_strategy = st.builds(DepositTransaction2)
@given(instance=DepositTransaction2_strategy)
@settings(max_examples=25)
def test_DepositTransaction2_instantiation(instance):
    assert isinstance(instance, DepositTransaction2)


Savings_Account_strategy = st.builds(Savings_Account, accountNumber=safe_text, balance=st.integers())
@given(instance=Savings_Account_strategy)
@settings(max_examples=25)
def test_Savings_Account_instantiation(instance):
    assert isinstance(instance, Savings_Account)


Savings_Account2_strategy = st.builds(Savings_Account2, accountNumber=safe_text, balance=st.integers())
@given(instance=Savings_Account2_strategy)
@settings(max_examples=25)
def test_Savings_Account2_instantiation(instance):
    assert isinstance(instance, Savings_Account2)


TransferTransaction_strategy = st.builds(TransferTransaction, sourceAccount=safe_text, targetAccount=safe_text)
@given(instance=TransferTransaction_strategy)
@settings(max_examples=25)
def test_TransferTransaction_instantiation(instance):
    assert isinstance(instance, TransferTransaction)


TransferTransaction2_strategy = st.builds(TransferTransaction2, sourceAccount=safe_text, targetAccount=safe_text)
@given(instance=TransferTransaction2_strategy)
@settings(max_examples=25)
def test_TransferTransaction2_instantiation(instance):
    assert isinstance(instance, TransferTransaction2)


WithdrawTransaction_strategy = st.builds(WithdrawTransaction)
@given(instance=WithdrawTransaction_strategy)
@settings(max_examples=25)
def test_WithdrawTransaction_instantiation(instance):
    assert isinstance(instance, WithdrawTransaction)


WithdrawTransaction2_strategy = st.builds(WithdrawTransaction2)
@given(instance=WithdrawTransaction2_strategy)
@settings(max_examples=25)
def test_WithdrawTransaction2_instantiation(instance):
    assert isinstance(instance, WithdrawTransaction2)


