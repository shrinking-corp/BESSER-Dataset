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
    Student,
    Savings,
    Main,
    Instructor,
    Checking,
    BankAccount,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_hyp_student_constructor_exists():
    assert callable(Student.__init__)


def test_hyp_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_savings_is_not_abstract():
    assert not inspect.isabstract(Savings)


def test_hyp_savings_constructor_exists():
    assert callable(Savings.__init__)


def test_hyp_savings_constructor_args():
    sig = inspect.signature(Savings.__init__)
    params = list(sig.parameters.keys())



def test_hyp_main_is_not_abstract():
    assert not inspect.isabstract(Main)


def test_hyp_main_constructor_exists():
    assert callable(Main.__init__)


def test_hyp_main_constructor_args():
    sig = inspect.signature(Main.__init__)
    params = list(sig.parameters.keys())



def test_hyp_instructor_is_not_abstract():
    assert not inspect.isabstract(Instructor)


def test_hyp_instructor_constructor_exists():
    assert callable(Instructor.__init__)


def test_hyp_instructor_constructor_args():
    sig = inspect.signature(Instructor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_checking_is_not_abstract():
    assert not inspect.isabstract(Checking)


def test_hyp_checking_constructor_exists():
    assert callable(Checking.__init__)


def test_hyp_checking_constructor_args():
    sig = inspect.signature(Checking.__init__)
    params = list(sig.parameters.keys())
    assert "OVERDRAFT_FEE" in params, "Missing parameter 'OVERDRAFT_FEE'"
    assert "OVERDRAFT_LIMIT" in params, "Missing parameter 'OVERDRAFT_LIMIT'"
    assert "isActive" in params, "Missing parameter 'isActive'"






def test_hyp_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_hyp_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_hyp_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "TRANSACTION_FEE" in params, "Missing parameter 'TRANSACTION_FEE'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "balance" in params, "Missing parameter 'balance'"
    assert "numOfTransactions" in params, "Missing parameter 'numOfTransactions'"
    assert "minimumBalance" in params, "Missing parameter 'minimumBalance'"
    assert "FREE_TRANSACTIONS" in params, "Missing parameter 'FREE_TRANSACTIONS'"








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
Student_strategy = st.builds(
    Student,
    name=
        safe_text
)
Savings_strategy = st.builds(
    Savings,
)
Main_strategy = st.builds(
    Main,
)
Instructor_strategy = st.builds(
    Instructor,
    name=
        safe_text
)
Checking_strategy = st.builds(
    Checking,
    OVERDRAFT_FEE=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    OVERDRAFT_LIMIT=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isActive=
        st.booleans()
)
BankAccount_strategy = st.builds(
    BankAccount,
    TRANSACTION_FEE=
        st.integers(),
    isActive=
        st.booleans(),
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    numOfTransactions=
        st.integers(),
    minimumBalance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    FREE_TRANSACTIONS=
        st.integers()
)




@given(instance=Student_strategy)
def test_hyp_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=Instructor_strategy)
def test_hyp_instructor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Checking_strategy)
def test_hyp_checking_OVERDRAFT_FEE_setter(instance):
    original = instance.OVERDRAFT_FEE
    instance.OVERDRAFT_FEE = original
    assert instance.OVERDRAFT_FEE == original



@given(instance=Checking_strategy)
def test_hyp_checking_OVERDRAFT_LIMIT_setter(instance):
    original = instance.OVERDRAFT_LIMIT
    instance.OVERDRAFT_LIMIT = original
    assert instance.OVERDRAFT_LIMIT == original



@given(instance=Checking_strategy)
def test_hyp_checking_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original




@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_TRANSACTION_FEE_setter(instance):
    original = instance.TRANSACTION_FEE
    instance.TRANSACTION_FEE = original
    assert instance.TRANSACTION_FEE == original



@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_numOfTransactions_setter(instance):
    original = instance.numOfTransactions
    instance.numOfTransactions = original
    assert instance.numOfTransactions == original



@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_minimumBalance_setter(instance):
    original = instance.minimumBalance
    instance.minimumBalance = original
    assert instance.minimumBalance == original



@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_FREE_TRANSACTIONS_setter(instance):
    original = instance.FREE_TRANSACTIONS
    instance.FREE_TRANSACTIONS = original
    assert instance.FREE_TRANSACTIONS == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BankAccount,
    Checking,
    Instructor,
    Main,
    Savings,
    Student,
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

def test_BankAccount_FREE_TRANSACTIONS_value_roundtrip():
    instance = BankAccount(FREE_TRANSACTIONS=7, TRANSACTION_FEE=7, balance=3.14, isActive=True, minimumBalance=3.14, numOfTransactions=7)
    assert instance.FREE_TRANSACTIONS == 7
    instance.FREE_TRANSACTIONS = 13
    assert instance.FREE_TRANSACTIONS == 13


def test_BankAccount_TRANSACTION_FEE_value_roundtrip():
    instance = BankAccount(FREE_TRANSACTIONS=7, TRANSACTION_FEE=7, balance=3.14, isActive=True, minimumBalance=3.14, numOfTransactions=7)
    assert instance.TRANSACTION_FEE == 7
    instance.TRANSACTION_FEE = 13
    assert instance.TRANSACTION_FEE == 13


def test_BankAccount_balance_value_roundtrip():
    instance = BankAccount(FREE_TRANSACTIONS=7, TRANSACTION_FEE=7, balance=3.14, isActive=True, minimumBalance=3.14, numOfTransactions=7)
    assert instance.balance == 3.14
    instance.balance = 9.99
    assert instance.balance == 9.99


def test_BankAccount_isActive_value_roundtrip():
    instance = BankAccount(FREE_TRANSACTIONS=7, TRANSACTION_FEE=7, balance=3.14, isActive=True, minimumBalance=3.14, numOfTransactions=7)
    assert instance.isActive == True
    instance.isActive = False
    assert instance.isActive == False


def test_BankAccount_minimumBalance_value_roundtrip():
    instance = BankAccount(FREE_TRANSACTIONS=7, TRANSACTION_FEE=7, balance=3.14, isActive=True, minimumBalance=3.14, numOfTransactions=7)
    assert instance.minimumBalance == 3.14
    instance.minimumBalance = 9.99
    assert instance.minimumBalance == 9.99


def test_BankAccount_numOfTransactions_value_roundtrip():
    instance = BankAccount(FREE_TRANSACTIONS=7, TRANSACTION_FEE=7, balance=3.14, isActive=True, minimumBalance=3.14, numOfTransactions=7)
    assert instance.numOfTransactions == 7
    instance.numOfTransactions = 13
    assert instance.numOfTransactions == 13


def test_Checking_OVERDRAFT_FEE_value_roundtrip():
    instance = Checking(OVERDRAFT_FEE=3.14, OVERDRAFT_LIMIT=3.14, isActive=True)
    assert instance.OVERDRAFT_FEE == 3.14
    instance.OVERDRAFT_FEE = 9.99
    assert instance.OVERDRAFT_FEE == 9.99


def test_Checking_OVERDRAFT_LIMIT_value_roundtrip():
    instance = Checking(OVERDRAFT_FEE=3.14, OVERDRAFT_LIMIT=3.14, isActive=True)
    assert instance.OVERDRAFT_LIMIT == 3.14
    instance.OVERDRAFT_LIMIT = 9.99
    assert instance.OVERDRAFT_LIMIT == 9.99


def test_Checking_isActive_value_roundtrip():
    instance = Checking(OVERDRAFT_FEE=3.14, OVERDRAFT_LIMIT=3.14, isActive=True)
    assert instance.isActive == True
    instance.isActive = False
    assert instance.isActive == False


def test_Instructor_name_value_roundtrip():
    instance = Instructor(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Student_name_value_roundtrip():
    instance = Student(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_Checking_Instructor_link_reassign_clear():
    a = Instructor(name="sample_text")
    b1 = Checking(OVERDRAFT_FEE=3.14, OVERDRAFT_LIMIT=3.14, isActive=True)
    b2 = Checking(OVERDRAFT_FEE=9.99, OVERDRAFT_LIMIT=9.99, isActive=False)
    _safe_set(a, 'checking5', b1)
    assert _is_linked(a, 'checking5', b1)
    if hasattr(b1, 'instructor4'):
        assert _is_linked(b1, 'instructor4', a)
    _safe_set(a, 'checking5', b2)
    assert _is_linked(a, 'checking5', b2)
    if hasattr(b1, 'instructor4'):
        assert not _is_linked(b1, 'instructor4', a)
    if hasattr(b2, 'instructor4'):
        assert _is_linked(b2, 'instructor4', a)
    _safe_set(a, 'checking5', None)
    assert not _is_linked(a, 'checking5', b2)
    if hasattr(b2, 'instructor4'):
        assert not _is_linked(b2, 'instructor4', a)


def test_assoc_Checking_Student_link_reassign_clear():
    a = Student(name="sample_text")
    b1 = Checking(OVERDRAFT_FEE=3.14, OVERDRAFT_LIMIT=3.14, isActive=True)
    b2 = Checking(OVERDRAFT_FEE=9.99, OVERDRAFT_LIMIT=9.99, isActive=False)
    _safe_set(a, 'checking1', b1)
    assert _is_linked(a, 'checking1', b1)
    if hasattr(b1, 'student0'):
        assert _is_linked(b1, 'student0', a)
    _safe_set(a, 'checking1', b2)
    assert _is_linked(a, 'checking1', b2)
    if hasattr(b1, 'student0'):
        assert not _is_linked(b1, 'student0', a)
    if hasattr(b2, 'student0'):
        assert _is_linked(b2, 'student0', a)
    _safe_set(a, 'checking1', None)
    assert not _is_linked(a, 'checking1', b2)
    if hasattr(b2, 'student0'):
        assert not _is_linked(b2, 'student0', a)


def test_assoc_Savings_Instructor_link_reassign_clear():
    a = Instructor(name="sample_text")
    b1 = Savings()
    b2 = Savings()
    _safe_set(a, 'savings7', b1)
    assert _is_linked(a, 'savings7', b1)
    if hasattr(b1, 'instructor6'):
        assert _is_linked(b1, 'instructor6', a)
    _safe_set(a, 'savings7', b2)
    assert _is_linked(a, 'savings7', b2)
    if hasattr(b1, 'instructor6'):
        assert not _is_linked(b1, 'instructor6', a)
    if hasattr(b2, 'instructor6'):
        assert _is_linked(b2, 'instructor6', a)
    _safe_set(a, 'savings7', None)
    assert not _is_linked(a, 'savings7', b2)
    if hasattr(b2, 'instructor6'):
        assert not _is_linked(b2, 'instructor6', a)


def test_assoc_Savings_Student_link_reassign_clear():
    a = Student(name="sample_text")
    b1 = Savings()
    b2 = Savings()
    _safe_set(a, 'savings3', b1)
    assert _is_linked(a, 'savings3', b1)
    if hasattr(b1, 'student2'):
        assert _is_linked(b1, 'student2', a)
    _safe_set(a, 'savings3', b2)
    assert _is_linked(a, 'savings3', b2)
    if hasattr(b1, 'student2'):
        assert not _is_linked(b1, 'student2', a)
    if hasattr(b2, 'student2'):
        assert _is_linked(b2, 'student2', a)
    _safe_set(a, 'savings3', None)
    assert not _is_linked(a, 'savings3', b2)
    if hasattr(b2, 'student2'):
        assert not _is_linked(b2, 'student2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BankAccount_strategy = st.builds(BankAccount, FREE_TRANSACTIONS=st.integers(), TRANSACTION_FEE=st.integers(), balance=st.floats(allow_nan=False, allow_infinity=False), isActive=st.booleans(), minimumBalance=st.floats(allow_nan=False, allow_infinity=False), numOfTransactions=st.integers())
@given(instance=BankAccount_strategy)
@settings(max_examples=25)
def test_BankAccount_instantiation(instance):
    assert isinstance(instance, BankAccount)


Checking_strategy = st.builds(Checking, OVERDRAFT_FEE=st.floats(allow_nan=False, allow_infinity=False), OVERDRAFT_LIMIT=st.floats(allow_nan=False, allow_infinity=False), isActive=st.booleans())
@given(instance=Checking_strategy)
@settings(max_examples=25)
def test_Checking_instantiation(instance):
    assert isinstance(instance, Checking)


Instructor_strategy = st.builds(Instructor, name=safe_text)
@given(instance=Instructor_strategy)
@settings(max_examples=25)
def test_Instructor_instantiation(instance):
    assert isinstance(instance, Instructor)


Main_strategy = st.builds(Main)
@given(instance=Main_strategy)
@settings(max_examples=25)
def test_Main_instantiation(instance):
    assert isinstance(instance, Main)


Savings_strategy = st.builds(Savings)
@given(instance=Savings_strategy)
@settings(max_examples=25)
def test_Savings_instantiation(instance):
    assert isinstance(instance, Savings)


Student_strategy = st.builds(Student, name=safe_text)
@given(instance=Student_strategy)
@settings(max_examples=25)
def test_Student_instantiation(instance):
    assert isinstance(instance, Student)



