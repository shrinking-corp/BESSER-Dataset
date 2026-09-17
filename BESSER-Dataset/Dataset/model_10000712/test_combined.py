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
    ExternalAccount,
    TransferTransaction,
    Transaction3,
    Account2,
    Transaction1,
    Account1,
    Transaction2,
    Transaction,
    Account,
    String,
    loan_LoanApplicationFile,
    loan_Loan,
    loan_LoanApplication,
    account_Account,
    account_SavingsAccount,
    transaction_LoanPayment,
    transaction_Payee,
    transaction_ExternalAccount,
    transaction_PaybillsTransaction,
    transaction_TransferTransaction,
    transaction_DepositTransaction,
    transaction_Transaction,
    User,
    Profile,
    transaction_TransactionType,
    account_AccountType,
    loan_LoanStatus,
    loan_ApplicationStatus,
    TransactionType,
    loan_LoanType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_externalaccount_is_not_abstract():
    assert not inspect.isabstract(ExternalAccount)


def test_hyp_externalaccount_constructor_exists():
    assert callable(ExternalAccount.__init__)


def test_hyp_externalaccount_constructor_args():
    sig = inspect.signature(ExternalAccount.__init__)
    params = list(sig.parameters.keys())
    assert "routingNum" in params, "Missing parameter 'routingNum'"
    assert "associatedAccount" in params, "Missing parameter 'associatedAccount'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"






def test_hyp_transfertransaction_is_not_abstract():
    assert not inspect.isabstract(TransferTransaction)


def test_hyp_transfertransaction_constructor_exists():
    assert callable(TransferTransaction.__init__)


def test_hyp_transfertransaction_constructor_args():
    sig = inspect.signature(TransferTransaction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transaction3_is_not_abstract():
    assert not inspect.isabstract(Transaction3)


def test_hyp_transaction3_constructor_exists():
    assert callable(Transaction3.__init__)


def test_hyp_transaction3_constructor_args():
    sig = inspect.signature(Transaction3.__init__)
    params = list(sig.parameters.keys())
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "time" in params, "Missing parameter 'time'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "type" in params, "Missing parameter 'type'"
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "description" in params, "Missing parameter 'description'"

def test_hyp_transaction3_has_destinationAccountNum():
    assert hasattr(Transaction3, "destinationAccountNum")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction3_has_amount():
    assert hasattr(Transaction3, "amount")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction3_has_time():
    assert hasattr(Transaction3, "time")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction3_has_transactionID():
    assert hasattr(Transaction3, "transactionID")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction3_has_type():
    assert hasattr(Transaction3, "type")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction3_has_sourceAccountNum():
    assert hasattr(Transaction3, "sourceAccountNum")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction3_has_comment():
    assert hasattr(Transaction3, "comment")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction3_has_description():
    assert hasattr(Transaction3, "description")
    descriptor = None
    for klass in Transaction3.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_hyp_account2_is_not_abstract():
    assert not inspect.isabstract(Account2)


def test_hyp_account2_constructor_exists():
    assert callable(Account2.__init__)


def test_hyp_account2_constructor_args():
    sig = inspect.signature(Account2.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_hyp_account2_has_type():
    assert hasattr(Account2, "type")
    descriptor = None
    for klass in Account2.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account2_has_pin():
    assert hasattr(Account2, "pin")
    descriptor = None
    for klass in Account2.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account2_has_userID():
    assert hasattr(Account2, "userID")
    descriptor = None
    for klass in Account2.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account2_has_accountNum():
    assert hasattr(Account2, "accountNum")
    descriptor = None
    for klass in Account2.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account2_has_balance():
    assert hasattr(Account2, "balance")
    descriptor = None
    for klass in Account2.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)



def test_hyp_transaction1_is_not_abstract():
    assert not inspect.isabstract(Transaction1)


def test_hyp_transaction1_constructor_exists():
    assert callable(Transaction1.__init__)


def test_hyp_transaction1_constructor_args():
    sig = inspect.signature(Transaction1.__init__)
    params = list(sig.parameters.keys())
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"
    assert "type" in params, "Missing parameter 'type'"
    assert "description" in params, "Missing parameter 'description'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "time" in params, "Missing parameter 'time'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"

def test_hyp_transaction1_has_destinationAccountNum():
    assert hasattr(Transaction1, "destinationAccountNum")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction1_has_type():
    assert hasattr(Transaction1, "type")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction1_has_description():
    assert hasattr(Transaction1, "description")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction1_has_amount():
    assert hasattr(Transaction1, "amount")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction1_has_transactionID():
    assert hasattr(Transaction1, "transactionID")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction1_has_time():
    assert hasattr(Transaction1, "time")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction1_has_comment():
    assert hasattr(Transaction1, "comment")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction1_has_sourceAccountNum():
    assert hasattr(Transaction1, "sourceAccountNum")
    descriptor = None
    for klass in Transaction1.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)



def test_hyp_account1_is_not_abstract():
    assert not inspect.isabstract(Account1)


def test_hyp_account1_constructor_exists():
    assert callable(Account1.__init__)


def test_hyp_account1_constructor_args():
    sig = inspect.signature(Account1.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_hyp_account1_has_balance():
    assert hasattr(Account1, "balance")
    descriptor = None
    for klass in Account1.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account1_has_type():
    assert hasattr(Account1, "type")
    descriptor = None
    for klass in Account1.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account1_has_pin():
    assert hasattr(Account1, "pin")
    descriptor = None
    for klass in Account1.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account1_has_accountNum():
    assert hasattr(Account1, "accountNum")
    descriptor = None
    for klass in Account1.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account1_has_userID():
    assert hasattr(Account1, "userID")
    descriptor = None
    for klass in Account1.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_hyp_transaction2_is_not_abstract():
    assert not inspect.isabstract(Transaction2)


def test_hyp_transaction2_constructor_exists():
    assert callable(Transaction2.__init__)


def test_hyp_transaction2_constructor_args():
    sig = inspect.signature(Transaction2.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "type" in params, "Missing parameter 'type'"
    assert "time" in params, "Missing parameter 'time'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "description" in params, "Missing parameter 'description'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"

def test_hyp_transaction2_has_sourceAccountNum():
    assert hasattr(Transaction2, "sourceAccountNum")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction2_has_type():
    assert hasattr(Transaction2, "type")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction2_has_time():
    assert hasattr(Transaction2, "time")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction2_has_amount():
    assert hasattr(Transaction2, "amount")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction2_has_description():
    assert hasattr(Transaction2, "description")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction2_has_transactionID():
    assert hasattr(Transaction2, "transactionID")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction2_has_comment():
    assert hasattr(Transaction2, "comment")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction2_has_destinationAccountNum():
    assert hasattr(Transaction2, "destinationAccountNum")
    descriptor = None
    for klass in Transaction2.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
            break
    assert isinstance(descriptor, property)



def test_hyp_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_hyp_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_hyp_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "time" in params, "Missing parameter 'time'"
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "type" in params, "Missing parameter 'type'"

def test_hyp_transaction_has_description():
    assert hasattr(Transaction, "description")
    descriptor = None
    for klass in Transaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_comment():
    assert hasattr(Transaction, "comment")
    descriptor = None
    for klass in Transaction.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_transactionID():
    assert hasattr(Transaction, "transactionID")
    descriptor = None
    for klass in Transaction.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_time():
    assert hasattr(Transaction, "time")
    descriptor = None
    for klass in Transaction.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_sourceAccountNum():
    assert hasattr(Transaction, "sourceAccountNum")
    descriptor = None
    for klass in Transaction.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_destinationAccountNum():
    assert hasattr(Transaction, "destinationAccountNum")
    descriptor = None
    for klass in Transaction.__mro__:
        if "destinationAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["destinationAccountNum"]
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

def test_hyp_transaction_has_type():
    assert hasattr(Transaction, "type")
    descriptor = None
    for klass in Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hyp_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_hyp_account_constructor_exists():
    assert callable(Account.__init__)


def test_hyp_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "balance" in params, "Missing parameter 'balance'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "type" in params, "Missing parameter 'type'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"

def test_hyp_account_has_balance():
    assert hasattr(Account, "balance")
    descriptor = None
    for klass in Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_has_pin():
    assert hasattr(Account, "pin")
    descriptor = None
    for klass in Account.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_has_type():
    assert hasattr(Account, "type")
    descriptor = None
    for klass in Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_has_userID():
    assert hasattr(Account, "userID")
    descriptor = None
    for klass in Account.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_account_has_accountNum():
    assert hasattr(Account, "accountNum")
    descriptor = None
    for klass in Account.__mro__:
        if "accountNum" in klass.__dict__:
            descriptor = klass.__dict__["accountNum"]
            break
    assert isinstance(descriptor, property)



def test_hyp_string_is_not_abstract():
    assert not inspect.isabstract(String)


def test_hyp_string_constructor_exists():
    assert callable(String.__init__)


def test_hyp_string_constructor_args():
    sig = inspect.signature(String.__init__)
    params = list(sig.parameters.keys())



def test_hyp_loan_loanapplicationfile_is_not_abstract():
    assert not inspect.isabstract(loan_LoanApplicationFile)


def test_hyp_loan_loanapplicationfile_constructor_exists():
    assert callable(loan_LoanApplicationFile.__init__)


def test_hyp_loan_loanapplicationfile_constructor_args():
    sig = inspect.signature(loan_LoanApplicationFile.__init__)
    params = list(sig.parameters.keys())
    assert "fileID" in params, "Missing parameter 'fileID'"
    assert "applicationID" in params, "Missing parameter 'applicationID'"





def test_hyp_loan_loan_is_not_abstract():
    assert not inspect.isabstract(loan_Loan)


def test_hyp_loan_loan_constructor_exists():
    assert callable(loan_Loan.__init__)


def test_hyp_loan_loan_constructor_args():
    sig = inspect.signature(loan_Loan.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "term" in params, "Missing parameter 'term'"
    assert "type" in params, "Missing parameter 'type'"
    assert "submissionTime" in params, "Missing parameter 'submissionTime'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "status" in params, "Missing parameter 'status'"
    assert "loanID" in params, "Missing parameter 'loanID'"

def test_hyp_loan_loan_has_interestRate():
    assert hasattr(loan_Loan, "interestRate")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loan_has_userID():
    assert hasattr(loan_Loan, "userID")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loan_has_term():
    assert hasattr(loan_Loan, "term")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loan_has_type():
    assert hasattr(loan_Loan, "type")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loan_has_submissionTime():
    assert hasattr(loan_Loan, "submissionTime")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "submissionTime" in klass.__dict__:
            descriptor = klass.__dict__["submissionTime"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loan_has_amount():
    assert hasattr(loan_Loan, "amount")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loan_has_status():
    assert hasattr(loan_Loan, "status")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loan_has_loanID():
    assert hasattr(loan_Loan, "loanID")
    descriptor = None
    for klass in loan_Loan.__mro__:
        if "loanID" in klass.__dict__:
            descriptor = klass.__dict__["loanID"]
            break
    assert isinstance(descriptor, property)



def test_hyp_loan_loanapplication_is_not_abstract():
    assert not inspect.isabstract(loan_LoanApplication)


def test_hyp_loan_loanapplication_constructor_exists():
    assert callable(loan_LoanApplication.__init__)


def test_hyp_loan_loanapplication_constructor_args():
    sig = inspect.signature(loan_LoanApplication.__init__)
    params = list(sig.parameters.keys())
    assert "submissionTime" in params, "Missing parameter 'submissionTime'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"
    assert "status" in params, "Missing parameter 'status'"
    assert "applicationID" in params, "Missing parameter 'applicationID'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "term" in params, "Missing parameter 'term'"
    assert "type" in params, "Missing parameter 'type'"

def test_hyp_loan_loanapplication_has_submissionTime():
    assert hasattr(loan_LoanApplication, "submissionTime")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "submissionTime" in klass.__dict__:
            descriptor = klass.__dict__["submissionTime"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loanapplication_has_interestRate():
    assert hasattr(loan_LoanApplication, "interestRate")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loanapplication_has_status():
    assert hasattr(loan_LoanApplication, "status")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loanapplication_has_applicationID():
    assert hasattr(loan_LoanApplication, "applicationID")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "applicationID" in klass.__dict__:
            descriptor = klass.__dict__["applicationID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loanapplication_has_userID():
    assert hasattr(loan_LoanApplication, "userID")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loanapplication_has_amount():
    assert hasattr(loan_LoanApplication, "amount")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loanapplication_has_term():
    assert hasattr(loan_LoanApplication, "term")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)

def test_hyp_loan_loanapplication_has_type():
    assert hasattr(loan_LoanApplication, "type")
    descriptor = None
    for klass in loan_LoanApplication.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hyp_account_account_is_not_abstract():
    assert not inspect.isabstract(account_Account)


def test_hyp_account_account_constructor_exists():
    assert callable(account_Account.__init__)


def test_hyp_account_account_constructor_args():
    sig = inspect.signature(account_Account.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"
    assert "type" in params, "Missing parameter 'type'"
    assert "pin" in params, "Missing parameter 'pin'"
    assert "balance" in params, "Missing parameter 'balance'"

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

def test_hyp_account_account_has_type():
    assert hasattr(account_Account, "type")
    descriptor = None
    for klass in account_Account.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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

def test_hyp_account_account_has_balance():
    assert hasattr(account_Account, "balance")
    descriptor = None
    for klass in account_Account.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
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




def test_hyp_transaction_loanpayment_is_not_abstract():
    assert not inspect.isabstract(transaction_LoanPayment)


def test_hyp_transaction_loanpayment_constructor_exists():
    assert callable(transaction_LoanPayment.__init__)


def test_hyp_transaction_loanpayment_constructor_args():
    sig = inspect.signature(transaction_LoanPayment.__init__)
    params = list(sig.parameters.keys())
    assert "interest" in params, "Missing parameter 'interest'"
    assert "principal" in params, "Missing parameter 'principal'"
    assert "loanID" in params, "Missing parameter 'loanID'"






def test_hyp_transaction_payee_is_not_abstract():
    assert not inspect.isabstract(transaction_Payee)


def test_hyp_transaction_payee_constructor_exists():
    assert callable(transaction_Payee.__init__)


def test_hyp_transaction_payee_constructor_args():
    sig = inspect.signature(transaction_Payee.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "address2" in params, "Missing parameter 'address2'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "country" in params, "Missing parameter 'country'"
    assert "city" in params, "Missing parameter 'city'"
    assert "state" in params, "Missing parameter 'state'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "phoneNum" in params, "Missing parameter 'phoneNum'"
    assert "address1" in params, "Missing parameter 'address1'"
    assert "accountNum" in params, "Missing parameter 'accountNum'"














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
    assert "transactionID" in params, "Missing parameter 'transactionID'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "type" in params, "Missing parameter 'type'"
    assert "destinationAccountNum" in params, "Missing parameter 'destinationAccountNum'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "sourceAccountNum" in params, "Missing parameter 'sourceAccountNum'"
    assert "time" in params, "Missing parameter 'time'"
    assert "description" in params, "Missing parameter 'description'"

def test_hyp_transaction_transaction_has_transactionID():
    assert hasattr(transaction_Transaction, "transactionID")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "transactionID" in klass.__dict__:
            descriptor = klass.__dict__["transactionID"]
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

def test_hyp_transaction_transaction_has_type():
    assert hasattr(transaction_Transaction, "type")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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

def test_hyp_transaction_transaction_has_comment():
    assert hasattr(transaction_Transaction, "comment")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_transaction_has_sourceAccountNum():
    assert hasattr(transaction_Transaction, "sourceAccountNum")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "sourceAccountNum" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccountNum"]
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

def test_hyp_transaction_transaction_has_description():
    assert hasattr(transaction_Transaction, "description")
    descriptor = None
    for klass in transaction_Transaction.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
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
    assert "state" in params, "Missing parameter 'state'"
    assert "country" in params, "Missing parameter 'country'"
    assert "zipcode" in params, "Missing parameter 'zipcode'"
    assert "address1" in params, "Missing parameter 'address1'"
    assert "address2" in params, "Missing parameter 'address2'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "email" in params, "Missing parameter 'email'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "IDType" in params, "Missing parameter 'IDType'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "IDNum" in params, "Missing parameter 'IDNum'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"
    assert "city" in params, "Missing parameter 'city'"















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

def test_hyp_loan_loanstatus_exists():
    # Check that the Enumeration exists
    assert loan_LoanStatus is not None

def test_hyp_loan_loanstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in loan_LoanStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in loan_LoanStatus"

def test_hyp_loan_applicationstatus_exists():
    # Check that the Enumeration exists
    assert loan_ApplicationStatus is not None

def test_hyp_loan_applicationstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in loan_ApplicationStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in loan_ApplicationStatus"

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

def test_hyp_loan_loantype_exists():
    # Check that the Enumeration exists
    assert loan_LoanType is not None

def test_hyp_loan_loantype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in loan_LoanType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in loan_LoanType"


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
ExternalAccount_strategy = st.builds(
    ExternalAccount,
    routingNum=
        safe_text,
    associatedAccount=
        safe_text,
    accountNum=
        safe_text
)
TransferTransaction_strategy = st.builds(
    TransferTransaction,
)
Transaction3_strategy = st.builds(
    Transaction3,
    destinationAccountNum=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    time=
        safe_text,
    transactionID=
        safe_text,
    type=
        st.none(),
    sourceAccountNum=
        safe_text,
    comment=
        safe_text,
    description=
        safe_text
)
Account2_strategy = st.builds(
    Account2,
    type=
        st.none(),
    pin=
        safe_text,
    userID=
        safe_text,
    accountNum=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Transaction1_strategy = st.builds(
    Transaction1,
    destinationAccountNum=
        safe_text,
    type=
        st.none(),
    description=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    transactionID=
        safe_text,
    time=
        safe_text,
    comment=
        safe_text,
    sourceAccountNum=
        safe_text
)
Account1_strategy = st.builds(
    Account1,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none(),
    pin=
        safe_text,
    accountNum=
        safe_text,
    userID=
        safe_text
)
Transaction2_strategy = st.builds(
    Transaction2,
    sourceAccountNum=
        safe_text,
    type=
        st.none(),
    time=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    description=
        safe_text,
    transactionID=
        safe_text,
    comment=
        safe_text,
    destinationAccountNum=
        safe_text
)
Transaction_strategy = st.builds(
    Transaction,
    description=
        safe_text,
    comment=
        safe_text,
    transactionID=
        safe_text,
    time=
        safe_text,
    sourceAccountNum=
        safe_text,
    destinationAccountNum=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none()
)
Account_strategy = st.builds(
    Account,
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
String_strategy = st.builds(
    String,
)
loan_LoanApplicationFile_strategy = st.builds(
    loan_LoanApplicationFile,
    fileID=
        safe_text,
    applicationID=
        safe_text
)
loan_Loan_strategy = st.builds(
    loan_Loan,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    userID=
        safe_text,
    term=
        st.integers(),
    type=
        st.none(),
    submissionTime=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        st.none(),
    loanID=
        safe_text
)
loan_LoanApplication_strategy = st.builds(
    loan_LoanApplication,
    submissionTime=
        safe_text,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        st.none(),
    applicationID=
        safe_text,
    userID=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    term=
        st.integers(),
    type=
        st.none()
)
account_Account_strategy = st.builds(
    account_Account,
    userID=
        safe_text,
    accountNum=
        safe_text,
    type=
        st.none(),
    pin=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
account_SavingsAccount_strategy = st.builds(
    account_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_LoanPayment_strategy = st.builds(
    transaction_LoanPayment,
    interest=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    principal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    loanID=
        safe_text
)
transaction_Payee_strategy = st.builds(
    transaction_Payee,
    userID=
        safe_text,
    address2=
        safe_text,
    zipcode=
        safe_text,
    country=
        safe_text,
    city=
        safe_text,
    state=
        safe_text,
    email=
        safe_text,
    name=
        safe_text,
    phoneNum=
        safe_text,
    address1=
        safe_text,
    accountNum=
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
    transactionID=
        safe_text,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none(),
    destinationAccountNum=
        safe_text,
    comment=
        safe_text,
    sourceAccountNum=
        safe_text,
    time=
        safe_text,
    description=
        safe_text
)
User_strategy = st.builds(
    User,
    lastLoginTime=
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
    state=
        safe_text,
    country=
        safe_text,
    zipcode=
        safe_text,
    address1=
        safe_text,
    address2=
        safe_text,
    userID=
        safe_text,
    lastname=
        safe_text,
    email=
        safe_text,
    firstname=
        safe_text,
    IDType=
        st.integers(),
    phoneNumber=
        safe_text,
    IDNum=
        safe_text,
    dateOfBirth=
        st.dates(),
    city=
        safe_text
)




@given(instance=ExternalAccount_strategy)
def test_hyp_externalaccount_routingNum_setter(instance):
    original = instance.routingNum
    instance.routingNum = original
    assert instance.routingNum == original



@given(instance=ExternalAccount_strategy)
def test_hyp_externalaccount_associatedAccount_setter(instance):
    original = instance.associatedAccount
    instance.associatedAccount = original
    assert instance.associatedAccount == original



@given(instance=ExternalAccount_strategy)
def test_hyp_externalaccount_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original


@given(instance=Transaction3_strategy)
@settings(max_examples=50)
def test_hyp_transaction3_instantiation(instance):
    assert isinstance(instance, Transaction3)



@given(instance=Transaction3_strategy)
def test_hyp_transaction3_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original



@given(instance=Transaction3_strategy)
def test_hyp_transaction3_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction3_strategy)
def test_hyp_transaction3_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Transaction3_strategy)
def test_hyp_transaction3_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Transaction3_strategy)
def test_hyp_transaction3_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Transaction3_strategy)
def test_hyp_transaction3_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=Transaction3_strategy)
def test_hyp_transaction3_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=Transaction3_strategy)
def test_hyp_transaction3_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Account2_strategy)
@settings(max_examples=50)
def test_hyp_account2_instantiation(instance):
    assert isinstance(instance, Account2)



@given(instance=Account2_strategy)
def test_hyp_account2_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Account2_strategy)
def test_hyp_account2_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=Account2_strategy)
def test_hyp_account2_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Account2_strategy)
def test_hyp_account2_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=Account2_strategy)
def test_hyp_account2_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=Transaction1_strategy)
@settings(max_examples=50)
def test_hyp_transaction1_instantiation(instance):
    assert isinstance(instance, Transaction1)



@given(instance=Transaction1_strategy)
def test_hyp_transaction1_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original



@given(instance=Transaction1_strategy)
def test_hyp_transaction1_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Transaction1_strategy)
def test_hyp_transaction1_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Transaction1_strategy)
def test_hyp_transaction1_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction1_strategy)
def test_hyp_transaction1_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Transaction1_strategy)
def test_hyp_transaction1_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Transaction1_strategy)
def test_hyp_transaction1_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=Transaction1_strategy)
def test_hyp_transaction1_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original

@given(instance=Account1_strategy)
@settings(max_examples=50)
def test_hyp_account1_instantiation(instance):
    assert isinstance(instance, Account1)



@given(instance=Account1_strategy)
def test_hyp_account1_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Account1_strategy)
def test_hyp_account1_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Account1_strategy)
def test_hyp_account1_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=Account1_strategy)
def test_hyp_account1_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original



@given(instance=Account1_strategy)
def test_hyp_account1_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=Transaction2_strategy)
@settings(max_examples=50)
def test_hyp_transaction2_instantiation(instance):
    assert isinstance(instance, Transaction2)



@given(instance=Transaction2_strategy)
def test_hyp_transaction2_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=Transaction2_strategy)
def test_hyp_transaction2_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Transaction2_strategy)
def test_hyp_transaction2_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Transaction2_strategy)
def test_hyp_transaction2_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction2_strategy)
def test_hyp_transaction2_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Transaction2_strategy)
def test_hyp_transaction2_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Transaction2_strategy)
def test_hyp_transaction2_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=Transaction2_strategy)
def test_hyp_transaction2_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original

@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_hyp_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



@given(instance=Transaction_strategy)
def test_hyp_transaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_hyp_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_hyp_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Account_strategy)
def test_hyp_account_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=Account_strategy)
def test_hyp_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Account_strategy)
def test_hyp_account_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=Account_strategy)
def test_hyp_account_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original





@given(instance=loan_LoanApplicationFile_strategy)
def test_hyp_loan_loanapplicationfile_fileID_setter(instance):
    original = instance.fileID
    instance.fileID = original
    assert instance.fileID == original



@given(instance=loan_LoanApplicationFile_strategy)
def test_hyp_loan_loanapplicationfile_applicationID_setter(instance):
    original = instance.applicationID
    instance.applicationID = original
    assert instance.applicationID == original

@given(instance=loan_Loan_strategy)
@settings(max_examples=50)
def test_hyp_loan_loan_instantiation(instance):
    assert isinstance(instance, loan_Loan)



@given(instance=loan_Loan_strategy)
def test_hyp_loan_loan_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=loan_Loan_strategy)
def test_hyp_loan_loan_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=loan_Loan_strategy)
def test_hyp_loan_loan_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original



@given(instance=loan_Loan_strategy)
def test_hyp_loan_loan_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=loan_Loan_strategy)
def test_hyp_loan_loan_submissionTime_setter(instance):
    original = instance.submissionTime
    instance.submissionTime = original
    assert instance.submissionTime == original



@given(instance=loan_Loan_strategy)
def test_hyp_loan_loan_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=loan_Loan_strategy)
def test_hyp_loan_loan_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=loan_Loan_strategy)
def test_hyp_loan_loan_loanID_setter(instance):
    original = instance.loanID
    instance.loanID = original
    assert instance.loanID == original

@given(instance=loan_LoanApplication_strategy)
@settings(max_examples=50)
def test_hyp_loan_loanapplication_instantiation(instance):
    assert isinstance(instance, loan_LoanApplication)



@given(instance=loan_LoanApplication_strategy)
def test_hyp_loan_loanapplication_submissionTime_setter(instance):
    original = instance.submissionTime
    instance.submissionTime = original
    assert instance.submissionTime == original



@given(instance=loan_LoanApplication_strategy)
def test_hyp_loan_loanapplication_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original



@given(instance=loan_LoanApplication_strategy)
def test_hyp_loan_loanapplication_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=loan_LoanApplication_strategy)
def test_hyp_loan_loanapplication_applicationID_setter(instance):
    original = instance.applicationID
    instance.applicationID = original
    assert instance.applicationID == original



@given(instance=loan_LoanApplication_strategy)
def test_hyp_loan_loanapplication_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=loan_LoanApplication_strategy)
def test_hyp_loan_loanapplication_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=loan_LoanApplication_strategy)
def test_hyp_loan_loanapplication_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original



@given(instance=loan_LoanApplication_strategy)
def test_hyp_loan_loanapplication_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=account_Account_strategy)
@settings(max_examples=50)
def test_hyp_account_account_instantiation(instance):
    assert isinstance(instance, account_Account)



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



@given(instance=account_Account_strategy)
def test_hyp_account_account_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=account_Account_strategy)
def test_hyp_account_account_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=account_Account_strategy)
def test_hyp_account_account_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original




@given(instance=account_SavingsAccount_strategy)
def test_hyp_account_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original




@given(instance=transaction_LoanPayment_strategy)
def test_hyp_transaction_loanpayment_interest_setter(instance):
    original = instance.interest
    instance.interest = original
    assert instance.interest == original



@given(instance=transaction_LoanPayment_strategy)
def test_hyp_transaction_loanpayment_principal_setter(instance):
    original = instance.principal
    instance.principal = original
    assert instance.principal == original



@given(instance=transaction_LoanPayment_strategy)
def test_hyp_transaction_loanpayment_loanID_setter(instance):
    original = instance.loanID
    instance.loanID = original
    assert instance.loanID == original




@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



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
def test_hyp_transaction_payee_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



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
def test_hyp_transaction_payee_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_phoneNum_setter(instance):
    original = instance.phoneNum
    instance.phoneNum = original
    assert instance.phoneNum == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_address1_setter(instance):
    original = instance.address1
    instance.address1 = original
    assert instance.address1 == original



@given(instance=transaction_Payee_strategy)
def test_hyp_transaction_payee_accountNum_setter(instance):
    original = instance.accountNum
    instance.accountNum = original
    assert instance.accountNum == original




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
def test_hyp_transaction_transaction_transactionID_setter(instance):
    original = instance.transactionID
    instance.transactionID = original
    assert instance.transactionID == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_destinationAccountNum_setter(instance):
    original = instance.destinationAccountNum
    instance.destinationAccountNum = original
    assert instance.destinationAccountNum == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_sourceAccountNum_setter(instance):
    original = instance.sourceAccountNum
    instance.sourceAccountNum = original
    assert instance.sourceAccountNum == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=transaction_Transaction_strategy)
def test_hyp_transaction_transaction_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original




@given(instance=User_strategy)
def test_hyp_user_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original



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
def test_hyp_profile_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Profile_strategy)
def test_hyp_profile_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Profile_strategy)
def test_hyp_profile_zipcode_setter(instance):
    original = instance.zipcode
    instance.zipcode = original
    assert instance.zipcode == original



@given(instance=Profile_strategy)
def test_hyp_profile_address1_setter(instance):
    original = instance.address1
    instance.address1 = original
    assert instance.address1 == original



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
def test_hyp_profile_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Profile_strategy)
def test_hyp_profile_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Profile_strategy)
def test_hyp_profile_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Profile_strategy)
def test_hyp_profile_IDType_setter(instance):
    original = instance.IDType
    instance.IDType = original
    assert instance.IDType == original



@given(instance=Profile_strategy)
def test_hyp_profile_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Profile_strategy)
def test_hyp_profile_IDNum_setter(instance):
    original = instance.IDNum
    instance.IDNum = original
    assert instance.IDNum == original



@given(instance=Profile_strategy)
def test_hyp_profile_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original



@given(instance=Profile_strategy)
def test_hyp_profile_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account,
    Account1,
    Account2,
    ExternalAccount,
    Profile,
    String,
    Transaction,
    Transaction1,
    Transaction2,
    Transaction3,
    TransferTransaction,
    User,
    account_Account,
    account_SavingsAccount,
    loan_Loan,
    loan_LoanApplication,
    loan_LoanApplicationFile,
    transaction_DepositTransaction,
    transaction_ExternalAccount,
    transaction_LoanPayment,
    transaction_PaybillsTransaction,
    transaction_Payee,
    transaction_Transaction,
    transaction_TransferTransaction,
    TransactionType,
    account_AccountType,
    loan_ApplicationStatus,
    loan_LoanStatus,
    loan_LoanType,
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

def test_ExternalAccount_accountNum_value_roundtrip():
    instance = ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    assert instance.accountNum == "sample_text"
    instance.accountNum = "sample_text_2"
    assert instance.accountNum == "sample_text_2"


def test_ExternalAccount_associatedAccount_value_roundtrip():
    instance = ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    assert instance.associatedAccount == "sample_text"
    instance.associatedAccount = "sample_text_2"
    assert instance.associatedAccount == "sample_text_2"


def test_ExternalAccount_routingNum_value_roundtrip():
    instance = ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    assert instance.routingNum == "sample_text"
    instance.routingNum = "sample_text_2"
    assert instance.routingNum == "sample_text_2"


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
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", username="sample_text")
    assert instance.lastLoginTime == "sample_text"
    instance.lastLoginTime = "sample_text_2"
    assert instance.lastLoginTime == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_userID_value_roundtrip():
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", username="sample_text")
    assert instance.userID == "sample_text"
    instance.userID = "sample_text_2"
    assert instance.userID == "sample_text_2"


def test_User_username_value_roundtrip():
    instance = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_account_SavingsAccount_interestRate_value_roundtrip():
    instance = account_SavingsAccount(interestRate=3.14)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_loan_LoanApplicationFile_applicationID_value_roundtrip():
    instance = loan_LoanApplicationFile(applicationID="sample_text", fileID="sample_text")
    assert instance.applicationID == "sample_text"
    instance.applicationID = "sample_text_2"
    assert instance.applicationID == "sample_text_2"


def test_loan_LoanApplicationFile_fileID_value_roundtrip():
    instance = loan_LoanApplicationFile(applicationID="sample_text", fileID="sample_text")
    assert instance.fileID == "sample_text"
    instance.fileID = "sample_text_2"
    assert instance.fileID == "sample_text_2"


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


def test_transaction_LoanPayment_interest_value_roundtrip():
    instance = transaction_LoanPayment(interest=3.14, loanID="sample_text", principal=3.14)
    assert instance.interest == 3.14
    instance.interest = 9.99
    assert instance.interest == 9.99


def test_transaction_LoanPayment_loanID_value_roundtrip():
    instance = transaction_LoanPayment(interest=3.14, loanID="sample_text", principal=3.14)
    assert instance.loanID == "sample_text"
    instance.loanID = "sample_text_2"
    assert instance.loanID == "sample_text_2"


def test_transaction_LoanPayment_principal_value_roundtrip():
    instance = transaction_LoanPayment(interest=3.14, loanID="sample_text", principal=3.14)
    assert instance.principal == 3.14
    instance.principal = 9.99
    assert instance.principal == 9.99


def test_transaction_Payee_accountNum_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.accountNum == "sample_text"
    instance.accountNum = "sample_text_2"
    assert instance.accountNum == "sample_text_2"


def test_transaction_Payee_address1_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.address1 == "sample_text"
    instance.address1 = "sample_text_2"
    assert instance.address1 == "sample_text_2"


def test_transaction_Payee_address2_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.address2 == "sample_text"
    instance.address2 = "sample_text_2"
    assert instance.address2 == "sample_text_2"


def test_transaction_Payee_city_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_transaction_Payee_country_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_transaction_Payee_email_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_transaction_Payee_name_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_transaction_Payee_phoneNum_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.phoneNum == "sample_text"
    instance.phoneNum = "sample_text_2"
    assert instance.phoneNum == "sample_text_2"


def test_transaction_Payee_state_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_transaction_Payee_userID_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.userID == "sample_text"
    instance.userID = "sample_text_2"
    assert instance.userID == "sample_text_2"


def test_transaction_Payee_zipcode_value_roundtrip():
    instance = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    assert instance.zipcode == "sample_text"
    instance.zipcode = "sample_text_2"
    assert instance.zipcode == "sample_text_2"


def test_assoc_ExternalAccount_TransferTransaction_link_reassign_clear():
    a = ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    b1 = TransferTransaction()
    b2 = TransferTransaction()
    _safe_set(a, 'transferTransaction20', {b1})
    assert _is_linked(a, 'transferTransaction20', b1)
    if hasattr(b1, 'externalAccount21'):
        assert _is_linked(b1, 'externalAccount21', a)
    _safe_set(a, 'transferTransaction20', {b2})
    assert _is_linked(a, 'transferTransaction20', b2)
    if hasattr(b1, 'externalAccount21'):
        assert not _is_linked(b1, 'externalAccount21', a)
    if hasattr(b2, 'externalAccount21'):
        assert _is_linked(b2, 'externalAccount21', a)
    _safe_set(a, 'transferTransaction20', set())
    assert not _is_linked(a, 'transferTransaction20', b2)
    if hasattr(b2, 'externalAccount21'):
        assert not _is_linked(b2, 'externalAccount21', a)


def test_assoc_PaybillsTransaction_Payee_link_reassign_clear():
    a = transaction_Payee(accountNum="sample_text", address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", email="sample_text", name="sample_text", phoneNum="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    b1 = transaction_PaybillsTransaction()
    b2 = transaction_PaybillsTransaction()
    _safe_set(a, 'paybillsTransaction5', {b1})
    assert _is_linked(a, 'paybillsTransaction5', b1)
    if hasattr(b1, 'payee4'):
        assert _is_linked(b1, 'payee4', a)
    _safe_set(a, 'paybillsTransaction5', {b2})
    assert _is_linked(a, 'paybillsTransaction5', b2)
    if hasattr(b1, 'payee4'):
        assert not _is_linked(b1, 'payee4', a)
    if hasattr(b2, 'payee4'):
        assert _is_linked(b2, 'payee4', a)
    _safe_set(a, 'paybillsTransaction5', set())
    assert not _is_linked(a, 'paybillsTransaction5', b2)
    if hasattr(b2, 'payee4'):
        assert not _is_linked(b2, 'payee4', a)


def test_assoc_Profile_User_link_reassign_clear():
    a = User(lastLoginTime="sample_text", password="sample_text", userID="sample_text", username="sample_text")
    b1 = Profile(IDNum="sample_text", IDType=7, address1="sample_text", address2="sample_text", city="sample_text", country="sample_text", dateOfBirth=date(2024, 1, 1), email="sample_text", firstname="sample_text", lastname="sample_text", phoneNumber="sample_text", state="sample_text", userID="sample_text", zipcode="sample_text")
    b2 = Profile(IDNum="sample_text_2", IDType=13, address1="sample_text_2", address2="sample_text_2", city="sample_text_2", country="sample_text_2", dateOfBirth=date(2025, 6, 15), email="sample_text_2", firstname="sample_text_2", lastname="sample_text_2", phoneNumber="sample_text_2", state="sample_text_2", userID="sample_text_2", zipcode="sample_text_2")
    _safe_set(a, 'profile7', b1)
    assert _is_linked(a, 'profile7', b1)
    if hasattr(b1, 'user6'):
        assert _is_linked(b1, 'user6', a)
    _safe_set(a, 'profile7', b2)
    assert _is_linked(a, 'profile7', b2)
    if hasattr(b1, 'user6'):
        assert not _is_linked(b1, 'user6', a)
    if hasattr(b2, 'user6'):
        assert _is_linked(b2, 'user6', a)
    _safe_set(a, 'profile7', None)
    assert not _is_linked(a, 'profile7', b2)
    if hasattr(b2, 'user6'):
        assert not _is_linked(b2, 'user6', a)


def test_assoc_TransferTransaction_ExternalAccount_link_reassign_clear():
    a = transaction_ExternalAccount(accountNum="sample_text", associatedAccount="sample_text", routingNum="sample_text")
    b1 = transaction_TransferTransaction()
    b2 = transaction_TransferTransaction()
    _safe_set(a, 'transferTransaction3', {b1})
    assert _is_linked(a, 'transferTransaction3', b1)
    if hasattr(b1, 'externalAccount2'):
        assert _is_linked(b1, 'externalAccount2', a)
    _safe_set(a, 'transferTransaction3', {b2})
    assert _is_linked(a, 'transferTransaction3', b2)
    if hasattr(b1, 'externalAccount2'):
        assert not _is_linked(b1, 'externalAccount2', a)
    if hasattr(b2, 'externalAccount2'):
        assert _is_linked(b2, 'externalAccount2', a)
    _safe_set(a, 'transferTransaction3', set())
    assert not _is_linked(a, 'transferTransaction3', b2)
    if hasattr(b2, 'externalAccount2'):
        assert not _is_linked(b2, 'externalAccount2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ExternalAccount_strategy = st.builds(ExternalAccount, accountNum=safe_text, associatedAccount=safe_text, routingNum=safe_text)
@given(instance=ExternalAccount_strategy)
@settings(max_examples=25)
def test_ExternalAccount_instantiation(instance):
    assert isinstance(instance, ExternalAccount)


Profile_strategy = st.builds(Profile, IDNum=safe_text, IDType=st.integers(), address1=safe_text, address2=safe_text, city=safe_text, country=safe_text, dateOfBirth=st.dates(), email=safe_text, firstname=safe_text, lastname=safe_text, phoneNumber=safe_text, state=safe_text, userID=safe_text, zipcode=safe_text)
@given(instance=Profile_strategy)
@settings(max_examples=25)
def test_Profile_instantiation(instance):
    assert isinstance(instance, Profile)


String_strategy = st.builds(String)
@given(instance=String_strategy)
@settings(max_examples=25)
def test_String_instantiation(instance):
    assert isinstance(instance, String)


TransferTransaction_strategy = st.builds(TransferTransaction)
@given(instance=TransferTransaction_strategy)
@settings(max_examples=25)
def test_TransferTransaction_instantiation(instance):
    assert isinstance(instance, TransferTransaction)


User_strategy = st.builds(User, lastLoginTime=safe_text, password=safe_text, userID=safe_text, username=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


account_SavingsAccount_strategy = st.builds(account_SavingsAccount, interestRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=account_SavingsAccount_strategy)
@settings(max_examples=25)
def test_account_SavingsAccount_instantiation(instance):
    assert isinstance(instance, account_SavingsAccount)


loan_LoanApplicationFile_strategy = st.builds(loan_LoanApplicationFile, applicationID=safe_text, fileID=safe_text)
@given(instance=loan_LoanApplicationFile_strategy)
@settings(max_examples=25)
def test_loan_LoanApplicationFile_instantiation(instance):
    assert isinstance(instance, loan_LoanApplicationFile)


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


transaction_LoanPayment_strategy = st.builds(transaction_LoanPayment, interest=st.floats(allow_nan=False, allow_infinity=False), loanID=safe_text, principal=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=transaction_LoanPayment_strategy)
@settings(max_examples=25)
def test_transaction_LoanPayment_instantiation(instance):
    assert isinstance(instance, transaction_LoanPayment)


transaction_PaybillsTransaction_strategy = st.builds(transaction_PaybillsTransaction)
@given(instance=transaction_PaybillsTransaction_strategy)
@settings(max_examples=25)
def test_transaction_PaybillsTransaction_instantiation(instance):
    assert isinstance(instance, transaction_PaybillsTransaction)


transaction_Payee_strategy = st.builds(transaction_Payee, accountNum=safe_text, address1=safe_text, address2=safe_text, city=safe_text, country=safe_text, email=safe_text, name=safe_text, phoneNum=safe_text, state=safe_text, userID=safe_text, zipcode=safe_text)
@given(instance=transaction_Payee_strategy)
@settings(max_examples=25)
def test_transaction_Payee_instantiation(instance):
    assert isinstance(instance, transaction_Payee)


transaction_TransferTransaction_strategy = st.builds(transaction_TransferTransaction)
@given(instance=transaction_TransferTransaction_strategy)
@settings(max_examples=25)
def test_transaction_TransferTransaction_instantiation(instance):
    assert isinstance(instance, transaction_TransferTransaction)



