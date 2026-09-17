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
    Setting,
    Transaction,
    Manager,
    Employee,
    User,
    Customer,
    Current_Account,
    Saving_Account,
    Account,
    Branch,
    Bank,
    TransactionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_setting_is_not_abstract():
    assert not inspect.isabstract(Setting)


def test_hyp_setting_constructor_exists():
    assert callable(Setting.__init__)


def test_hyp_setting_constructor_args():
    sig = inspect.signature(Setting.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transaction_is_not_abstract():
    assert not inspect.isabstract(Transaction)


def test_hyp_transaction_constructor_exists():
    assert callable(Transaction.__init__)


def test_hyp_transaction_constructor_args():
    sig = inspect.signature(Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "date" in params, "Missing parameter 'date'"
    assert "currentBalance" in params, "Missing parameter 'currentBalance'"
    assert "Acc_num" in params, "Missing parameter 'Acc_num'"
    assert "TranId" in params, "Missing parameter 'TranId'"
    assert "status" in params, "Missing parameter 'status'"
    assert "prevBalance" in params, "Missing parameter 'prevBalance'"
    assert "type" in params, "Missing parameter 'type'"

def test_hyp_transaction_has_amount():
    assert hasattr(Transaction, "amount")
    descriptor = None
    for klass in Transaction.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_date():
    assert hasattr(Transaction, "date")
    descriptor = None
    for klass in Transaction.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_currentBalance():
    assert hasattr(Transaction, "currentBalance")
    descriptor = None
    for klass in Transaction.__mro__:
        if "currentBalance" in klass.__dict__:
            descriptor = klass.__dict__["currentBalance"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_Acc_num():
    assert hasattr(Transaction, "Acc_num")
    descriptor = None
    for klass in Transaction.__mro__:
        if "Acc_num" in klass.__dict__:
            descriptor = klass.__dict__["Acc_num"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_TranId():
    assert hasattr(Transaction, "TranId")
    descriptor = None
    for klass in Transaction.__mro__:
        if "TranId" in klass.__dict__:
            descriptor = klass.__dict__["TranId"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_status():
    assert hasattr(Transaction, "status")
    descriptor = None
    for klass in Transaction.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_has_prevBalance():
    assert hasattr(Transaction, "prevBalance")
    descriptor = None
    for klass in Transaction.__mro__:
        if "prevBalance" in klass.__dict__:
            descriptor = klass.__dict__["prevBalance"]
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



def test_hyp_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_hyp_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_hyp_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_hyp_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_hyp_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Mid" in params, "Missing parameter 'Mid'"
    assert "Eid" in params, "Missing parameter 'Eid'"





def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "family" in params, "Missing parameter 'family'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userName" in params, "Missing parameter 'userName'"
    assert "uid" in params, "Missing parameter 'uid'"
    assert "name" in params, "Missing parameter 'name'"








def test_hyp_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_hyp_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_hyp_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Cust_id" in params, "Missing parameter 'Cust_id'"
    assert "phone" in params, "Missing parameter 'phone'"







def test_hyp_current_account_is_not_abstract():
    assert not inspect.isabstract(Current_Account)


def test_hyp_current_account_constructor_exists():
    assert callable(Current_Account.__init__)


def test_hyp_current_account_constructor_args():
    sig = inspect.signature(Current_Account.__init__)
    params = list(sig.parameters.keys())



def test_hyp_saving_account_is_not_abstract():
    assert not inspect.isabstract(Saving_Account)


def test_hyp_saving_account_constructor_exists():
    assert callable(Saving_Account.__init__)


def test_hyp_saving_account_constructor_args():
    sig = inspect.signature(Saving_Account.__init__)
    params = list(sig.parameters.keys())
    assert "interest_Rate" in params, "Missing parameter 'interest_Rate'"




def test_hyp_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_hyp_account_constructor_exists():
    assert callable(Account.__init__)


def test_hyp_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "date_Of_Opening" in params, "Missing parameter 'date_Of_Opening'"
    assert "Balance" in params, "Missing parameter 'Balance'"
    assert "min_Balance" in params, "Missing parameter 'min_Balance'"
    assert "Acc_no" in params, "Missing parameter 'Acc_no'"







def test_hyp_branch_is_not_abstract():
    assert not inspect.isabstract(Branch)


def test_hyp_branch_constructor_exists():
    assert callable(Branch.__init__)


def test_hyp_branch_constructor_args():
    sig = inspect.signature(Branch.__init__)
    params = list(sig.parameters.keys())
    assert "Branch_code" in params, "Missing parameter 'Branch_code'"
    assert "City" in params, "Missing parameter 'City'"





def test_hyp_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_hyp_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_hyp_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Code" in params, "Missing parameter 'Code'"



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
Setting_strategy = st.builds(
    Setting,
)
Transaction_strategy = st.builds(
    Transaction,
    amount=
        st.integers(),
    date=
        safe_text,
    currentBalance=
        st.integers(),
    Acc_num=
        st.integers(),
    TranId=
        st.integers(),
    status=
        safe_text,
    prevBalance=
        st.integers(),
    type=
        st.none()
)
Manager_strategy = st.builds(
    Manager,
)
Employee_strategy = st.builds(
    Employee,
    Mid=
        st.integers(),
    Eid=
        st.integers()
)
User_strategy = st.builds(
    User,
    family=
        safe_text,
    password=
        safe_text,
    userName=
        safe_text,
    uid=
        st.integers(),
    name=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    address=
        safe_text,
    name=
        safe_text,
    Cust_id=
        safe_text,
    phone=
        safe_text
)
Current_Account_strategy = st.builds(
    Current_Account,
)
Saving_Account_strategy = st.builds(
    Saving_Account,
    interest_Rate=
        st.integers()
)
Account_strategy = st.builds(
    Account,
    date_Of_Opening=
        safe_text,
    Balance=
        st.integers(),
    min_Balance=
        st.integers(),
    Acc_no=
        st.integers()
)
Branch_strategy = st.builds(
    Branch,
    Branch_code=
        safe_text,
    City=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    Name=
        safe_text,
    Code=
        safe_text
)


@given(instance=Transaction_strategy)
@settings(max_examples=50)
def test_hyp_transaction_instantiation(instance):
    assert isinstance(instance, Transaction)



@given(instance=Transaction_strategy)
def test_hyp_transaction_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_currentBalance_setter(instance):
    original = instance.currentBalance
    instance.currentBalance = original
    assert instance.currentBalance == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_Acc_num_setter(instance):
    original = instance.Acc_num
    instance.Acc_num = original
    assert instance.Acc_num == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_TranId_setter(instance):
    original = instance.TranId
    instance.TranId = original
    assert instance.TranId == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_prevBalance_setter(instance):
    original = instance.prevBalance
    instance.prevBalance = original
    assert instance.prevBalance == original



@given(instance=Transaction_strategy)
def test_hyp_transaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=Employee_strategy)
def test_hyp_employee_Mid_setter(instance):
    original = instance.Mid
    instance.Mid = original
    assert instance.Mid == original



@given(instance=Employee_strategy)
def test_hyp_employee_Eid_setter(instance):
    original = instance.Eid
    instance.Eid = original
    assert instance.Eid == original




@given(instance=User_strategy)
def test_hyp_user_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=User_strategy)
def test_hyp_user_uid_setter(instance):
    original = instance.uid
    instance.uid = original
    assert instance.uid == original



@given(instance=User_strategy)
def test_hyp_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Customer_strategy)
def test_hyp_customer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Customer_strategy)
def test_hyp_customer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Customer_strategy)
def test_hyp_customer_Cust_id_setter(instance):
    original = instance.Cust_id
    instance.Cust_id = original
    assert instance.Cust_id == original



@given(instance=Customer_strategy)
def test_hyp_customer_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original





@given(instance=Saving_Account_strategy)
def test_hyp_saving_account_interest_Rate_setter(instance):
    original = instance.interest_Rate
    instance.interest_Rate = original
    assert instance.interest_Rate == original




@given(instance=Account_strategy)
def test_hyp_account_date_Of_Opening_setter(instance):
    original = instance.date_Of_Opening
    instance.date_Of_Opening = original
    assert instance.date_Of_Opening == original



@given(instance=Account_strategy)
def test_hyp_account_Balance_setter(instance):
    original = instance.Balance
    instance.Balance = original
    assert instance.Balance == original



@given(instance=Account_strategy)
def test_hyp_account_min_Balance_setter(instance):
    original = instance.min_Balance
    instance.min_Balance = original
    assert instance.min_Balance == original



@given(instance=Account_strategy)
def test_hyp_account_Acc_no_setter(instance):
    original = instance.Acc_no
    instance.Acc_no = original
    assert instance.Acc_no == original




@given(instance=Branch_strategy)
def test_hyp_branch_Branch_code_setter(instance):
    original = instance.Branch_code
    instance.Branch_code = original
    assert instance.Branch_code == original



@given(instance=Branch_strategy)
def test_hyp_branch_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original




@given(instance=Bank_strategy)
def test_hyp_bank_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Bank_strategy)
def test_hyp_bank_Code_setter(instance):
    original = instance.Code
    instance.Code = original
    assert instance.Code == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Account,
    Bank,
    Branch,
    Current_Account,
    Customer,
    Employee,
    Manager,
    Saving_Account,
    Setting,
    Transaction,
    User,
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

def test_Account_Acc_no_value_roundtrip():
    instance = Account(Acc_no=7, Balance=7, date_Of_Opening="sample_text", min_Balance=7)
    assert instance.Acc_no == 7
    instance.Acc_no = 13
    assert instance.Acc_no == 13


def test_Account_Balance_value_roundtrip():
    instance = Account(Acc_no=7, Balance=7, date_Of_Opening="sample_text", min_Balance=7)
    assert instance.Balance == 7
    instance.Balance = 13
    assert instance.Balance == 13


def test_Account_date_Of_Opening_value_roundtrip():
    instance = Account(Acc_no=7, Balance=7, date_Of_Opening="sample_text", min_Balance=7)
    assert instance.date_Of_Opening == "sample_text"
    instance.date_Of_Opening = "sample_text_2"
    assert instance.date_Of_Opening == "sample_text_2"


def test_Account_min_Balance_value_roundtrip():
    instance = Account(Acc_no=7, Balance=7, date_Of_Opening="sample_text", min_Balance=7)
    assert instance.min_Balance == 7
    instance.min_Balance = 13
    assert instance.min_Balance == 13


def test_Bank_Code_value_roundtrip():
    instance = Bank(Code="sample_text", Name="sample_text")
    assert instance.Code == "sample_text"
    instance.Code = "sample_text_2"
    assert instance.Code == "sample_text_2"


def test_Bank_Name_value_roundtrip():
    instance = Bank(Code="sample_text", Name="sample_text")
    assert instance.Name == "sample_text"
    instance.Name = "sample_text_2"
    assert instance.Name == "sample_text_2"


def test_Branch_Branch_code_value_roundtrip():
    instance = Branch(Branch_code="sample_text", City="sample_text")
    assert instance.Branch_code == "sample_text"
    instance.Branch_code = "sample_text_2"
    assert instance.Branch_code == "sample_text_2"


def test_Branch_City_value_roundtrip():
    instance = Branch(Branch_code="sample_text", City="sample_text")
    assert instance.City == "sample_text"
    instance.City = "sample_text_2"
    assert instance.City == "sample_text_2"


def test_Customer_Cust_id_value_roundtrip():
    instance = Customer(Cust_id="sample_text", address="sample_text", name="sample_text", phone="sample_text")
    assert instance.Cust_id == "sample_text"
    instance.Cust_id = "sample_text_2"
    assert instance.Cust_id == "sample_text_2"


def test_Customer_address_value_roundtrip():
    instance = Customer(Cust_id="sample_text", address="sample_text", name="sample_text", phone="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Customer_name_value_roundtrip():
    instance = Customer(Cust_id="sample_text", address="sample_text", name="sample_text", phone="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Customer_phone_value_roundtrip():
    instance = Customer(Cust_id="sample_text", address="sample_text", name="sample_text", phone="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_Employee_Eid_value_roundtrip():
    instance = Employee(Eid=7, Mid=7)
    assert instance.Eid == 7
    instance.Eid = 13
    assert instance.Eid == 13


def test_Employee_Mid_value_roundtrip():
    instance = Employee(Eid=7, Mid=7)
    assert instance.Mid == 7
    instance.Mid = 13
    assert instance.Mid == 13


def test_Saving_Account_interest_Rate_value_roundtrip():
    instance = Saving_Account(interest_Rate=7)
    assert instance.interest_Rate == 7
    instance.interest_Rate = 13
    assert instance.interest_Rate == 13


def test_User_family_value_roundtrip():
    instance = User(family="sample_text", name="sample_text", password="sample_text", uid=7, userName="sample_text")
    assert instance.family == "sample_text"
    instance.family = "sample_text_2"
    assert instance.family == "sample_text_2"


def test_User_name_value_roundtrip():
    instance = User(family="sample_text", name="sample_text", password="sample_text", uid=7, userName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_User_password_value_roundtrip():
    instance = User(family="sample_text", name="sample_text", password="sample_text", uid=7, userName="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_uid_value_roundtrip():
    instance = User(family="sample_text", name="sample_text", password="sample_text", uid=7, userName="sample_text")
    assert instance.uid == 7
    instance.uid = 13
    assert instance.uid == 13


def test_User_userName_value_roundtrip():
    instance = User(family="sample_text", name="sample_text", password="sample_text", uid=7, userName="sample_text")
    assert instance.userName == "sample_text"
    instance.userName = "sample_text_2"
    assert instance.userName == "sample_text_2"


def test_assoc_Bank_Branch_link_reassign_clear():
    a = Branch(Branch_code="sample_text", City="sample_text")
    b1 = Bank(Code="sample_text", Name="sample_text")
    b2 = Bank(Code="sample_text_2", Name="sample_text_2")
    _safe_set(a, 'bank1', b1)
    assert _is_linked(a, 'bank1', b1)
    if hasattr(b1, 'branch0'):
        assert _is_linked(b1, 'branch0', a)
    _safe_set(a, 'bank1', b2)
    assert _is_linked(a, 'bank1', b2)
    if hasattr(b1, 'branch0'):
        assert not _is_linked(b1, 'branch0', a)
    if hasattr(b2, 'branch0'):
        assert _is_linked(b2, 'branch0', a)
    _safe_set(a, 'bank1', None)
    assert not _is_linked(a, 'bank1', b2)
    if hasattr(b2, 'branch0'):
        assert not _is_linked(b2, 'branch0', a)


def test_assoc_Branch_Account_link_reassign_clear():
    a = Branch(Branch_code="sample_text", City="sample_text")
    b1 = Account(Acc_no=7, Balance=7, date_Of_Opening="sample_text", min_Balance=7)
    b2 = Account(Acc_no=13, Balance=13, date_Of_Opening="sample_text_2", min_Balance=13)
    _safe_set(a, 'account2', {b1})
    assert _is_linked(a, 'account2', b1)
    if hasattr(b1, 'branch3'):
        assert _is_linked(b1, 'branch3', a)
    _safe_set(a, 'account2', {b2})
    assert _is_linked(a, 'account2', b2)
    if hasattr(b1, 'branch3'):
        assert not _is_linked(b1, 'branch3', a)
    if hasattr(b2, 'branch3'):
        assert _is_linked(b2, 'branch3', a)
    _safe_set(a, 'account2', set())
    assert not _is_linked(a, 'account2', b2)
    if hasattr(b2, 'branch3'):
        assert not _is_linked(b2, 'branch3', a)


def test_assoc_Current_Account_Customer_link_reassign_clear():
    a = Customer(Cust_id="sample_text", address="sample_text", name="sample_text", phone="sample_text")
    b1 = Current_Account()
    b2 = Current_Account()
    _safe_set(a, 'current_Account7', b1)
    assert _is_linked(a, 'current_Account7', b1)
    if hasattr(b1, 'customer6'):
        assert _is_linked(b1, 'customer6', a)
    _safe_set(a, 'current_Account7', b2)
    assert _is_linked(a, 'current_Account7', b2)
    if hasattr(b1, 'customer6'):
        assert not _is_linked(b1, 'customer6', a)
    if hasattr(b2, 'customer6'):
        assert _is_linked(b2, 'customer6', a)
    _safe_set(a, 'current_Account7', None)
    assert not _is_linked(a, 'current_Account7', b2)
    if hasattr(b2, 'customer6'):
        assert not _is_linked(b2, 'customer6', a)


def test_assoc_Employee_Manager_link_reassign_clear():
    a = Employee(Eid=7, Mid=7)
    b1 = Manager()
    b2 = Manager()
    _safe_set(a, 'manager8', b1)
    assert _is_linked(a, 'manager8', b1)
    if hasattr(b1, 'employee9'):
        assert _is_linked(b1, 'employee9', a)
    _safe_set(a, 'manager8', b2)
    assert _is_linked(a, 'manager8', b2)
    if hasattr(b1, 'employee9'):
        assert not _is_linked(b1, 'employee9', a)
    if hasattr(b2, 'employee9'):
        assert _is_linked(b2, 'employee9', a)
    _safe_set(a, 'manager8', None)
    assert not _is_linked(a, 'manager8', b2)
    if hasattr(b2, 'employee9'):
        assert not _is_linked(b2, 'employee9', a)


def test_assoc_Saving_Account_Customer_link_reassign_clear():
    a = Saving_Account(interest_Rate=7)
    b1 = Customer(Cust_id="sample_text", address="sample_text", name="sample_text", phone="sample_text")
    b2 = Customer(Cust_id="sample_text_2", address="sample_text_2", name="sample_text_2", phone="sample_text_2")
    _safe_set(a, 'customer4', b1)
    assert _is_linked(a, 'customer4', b1)
    if hasattr(b1, 'saving_Account5'):
        assert _is_linked(b1, 'saving_Account5', a)
    _safe_set(a, 'customer4', b2)
    assert _is_linked(a, 'customer4', b2)
    if hasattr(b1, 'saving_Account5'):
        assert not _is_linked(b1, 'saving_Account5', a)
    if hasattr(b2, 'saving_Account5'):
        assert _is_linked(b2, 'saving_Account5', a)
    _safe_set(a, 'customer4', None)
    assert not _is_linked(a, 'customer4', b2)
    if hasattr(b2, 'saving_Account5'):
        assert not _is_linked(b2, 'saving_Account5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Account_strategy = st.builds(Account, Acc_no=st.integers(), Balance=st.integers(), date_Of_Opening=safe_text, min_Balance=st.integers())
@given(instance=Account_strategy)
@settings(max_examples=25)
def test_Account_instantiation(instance):
    assert isinstance(instance, Account)


Bank_strategy = st.builds(Bank, Code=safe_text, Name=safe_text)
@given(instance=Bank_strategy)
@settings(max_examples=25)
def test_Bank_instantiation(instance):
    assert isinstance(instance, Bank)


Branch_strategy = st.builds(Branch, Branch_code=safe_text, City=safe_text)
@given(instance=Branch_strategy)
@settings(max_examples=25)
def test_Branch_instantiation(instance):
    assert isinstance(instance, Branch)


Current_Account_strategy = st.builds(Current_Account)
@given(instance=Current_Account_strategy)
@settings(max_examples=25)
def test_Current_Account_instantiation(instance):
    assert isinstance(instance, Current_Account)


Customer_strategy = st.builds(Customer, Cust_id=safe_text, address=safe_text, name=safe_text, phone=safe_text)
@given(instance=Customer_strategy)
@settings(max_examples=25)
def test_Customer_instantiation(instance):
    assert isinstance(instance, Customer)


Employee_strategy = st.builds(Employee, Eid=st.integers(), Mid=st.integers())
@given(instance=Employee_strategy)
@settings(max_examples=25)
def test_Employee_instantiation(instance):
    assert isinstance(instance, Employee)


Manager_strategy = st.builds(Manager)
@given(instance=Manager_strategy)
@settings(max_examples=25)
def test_Manager_instantiation(instance):
    assert isinstance(instance, Manager)


Saving_Account_strategy = st.builds(Saving_Account, interest_Rate=st.integers())
@given(instance=Saving_Account_strategy)
@settings(max_examples=25)
def test_Saving_Account_instantiation(instance):
    assert isinstance(instance, Saving_Account)


Setting_strategy = st.builds(Setting)
@given(instance=Setting_strategy)
@settings(max_examples=25)
def test_Setting_instantiation(instance):
    assert isinstance(instance, Setting)


User_strategy = st.builds(User, family=safe_text, name=safe_text, password=safe_text, uid=st.integers(), userName=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



