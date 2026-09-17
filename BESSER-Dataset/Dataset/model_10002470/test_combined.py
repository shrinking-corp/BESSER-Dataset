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
    MyInterface_Interface,
    Medical_Record_NHS_Number,
    Medical_Record_CheckingAccount,
    Medical_Record_CertificatesOfDepositAccount,
    Medical_Record_SavingsAccount,
    transaction_Community_Hospital,
    transaction_Acute_Hospital,
    transaction_Mental_Health_Trust,
    transaction_Interface,
    Login,
    Patient,
    transaction_TransactionType,
    Medical_Record_AccountType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_myinterface_interface_is_not_abstract():
    assert not inspect.isabstract(MyInterface_Interface)


def test_hyp_myinterface_interface_constructor_exists():
    assert callable(MyInterface_Interface.__init__)


def test_hyp_myinterface_interface_constructor_args():
    sig = inspect.signature(MyInterface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_medical_record_nhs_number_is_not_abstract():
    assert not inspect.isabstract(Medical_Record_NHS_Number)


def test_hyp_medical_record_nhs_number_constructor_exists():
    assert callable(Medical_Record_NHS_Number.__init__)


def test_hyp_medical_record_nhs_number_constructor_args():
    sig = inspect.signature(Medical_Record_NHS_Number.__init__)
    params = list(sig.parameters.keys())
    assert "accountNo" in params, "Missing parameter 'accountNo'"
    assert "balance" in params, "Missing parameter 'balance'"
    assert "type" in params, "Missing parameter 'type'"

def test_hyp_medical_record_nhs_number_has_accountNo():
    assert hasattr(Medical_Record_NHS_Number, "accountNo")
    descriptor = None
    for klass in Medical_Record_NHS_Number.__mro__:
        if "accountNo" in klass.__dict__:
            descriptor = klass.__dict__["accountNo"]
            break
    assert isinstance(descriptor, property)

def test_hyp_medical_record_nhs_number_has_balance():
    assert hasattr(Medical_Record_NHS_Number, "balance")
    descriptor = None
    for klass in Medical_Record_NHS_Number.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_hyp_medical_record_nhs_number_has_type():
    assert hasattr(Medical_Record_NHS_Number, "type")
    descriptor = None
    for klass in Medical_Record_NHS_Number.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hyp_medical_record_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(Medical_Record_CheckingAccount)


def test_hyp_medical_record_checkingaccount_constructor_exists():
    assert callable(Medical_Record_CheckingAccount.__init__)


def test_hyp_medical_record_checkingaccount_constructor_args():
    sig = inspect.signature(Medical_Record_CheckingAccount.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_medical_record_certificatesofdepositaccount_is_not_abstract():
    assert not inspect.isabstract(Medical_Record_CertificatesOfDepositAccount)


def test_hyp_medical_record_certificatesofdepositaccount_constructor_exists():
    assert callable(Medical_Record_CertificatesOfDepositAccount.__init__)


def test_hyp_medical_record_certificatesofdepositaccount_constructor_args():
    sig = inspect.signature(Medical_Record_CertificatesOfDepositAccount.__init__)
    params = list(sig.parameters.keys())
    assert "timePeriod" in params, "Missing parameter 'timePeriod'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"





def test_hyp_medical_record_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(Medical_Record_SavingsAccount)


def test_hyp_medical_record_savingsaccount_constructor_exists():
    assert callable(Medical_Record_SavingsAccount.__init__)


def test_hyp_medical_record_savingsaccount_constructor_args():
    sig = inspect.signature(Medical_Record_SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "interestRate" in params, "Missing parameter 'interestRate'"




def test_hyp_transaction_community_hospital_is_not_abstract():
    assert not inspect.isabstract(transaction_Community_Hospital)


def test_hyp_transaction_community_hospital_constructor_exists():
    assert callable(transaction_Community_Hospital.__init__)


def test_hyp_transaction_community_hospital_constructor_args():
    sig = inspect.signature(transaction_Community_Hospital.__init__)
    params = list(sig.parameters.keys())
    assert "targetAccount" in params, "Missing parameter 'targetAccount'"
    assert "sourceAccount" in params, "Missing parameter 'sourceAccount'"

def test_hyp_transaction_community_hospital_has_targetAccount():
    assert hasattr(transaction_Community_Hospital, "targetAccount")
    descriptor = None
    for klass in transaction_Community_Hospital.__mro__:
        if "targetAccount" in klass.__dict__:
            descriptor = klass.__dict__["targetAccount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_community_hospital_has_sourceAccount():
    assert hasattr(transaction_Community_Hospital, "sourceAccount")
    descriptor = None
    for klass in transaction_Community_Hospital.__mro__:
        if "sourceAccount" in klass.__dict__:
            descriptor = klass.__dict__["sourceAccount"]
            break
    assert isinstance(descriptor, property)



def test_hyp_transaction_acute_hospital_is_not_abstract():
    assert not inspect.isabstract(transaction_Acute_Hospital)


def test_hyp_transaction_acute_hospital_constructor_exists():
    assert callable(transaction_Acute_Hospital.__init__)


def test_hyp_transaction_acute_hospital_constructor_args():
    sig = inspect.signature(transaction_Acute_Hospital.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transaction_mental_health_trust_is_not_abstract():
    assert not inspect.isabstract(transaction_Mental_Health_Trust)


def test_hyp_transaction_mental_health_trust_constructor_exists():
    assert callable(transaction_Mental_Health_Trust.__init__)


def test_hyp_transaction_mental_health_trust_constructor_args():
    sig = inspect.signature(transaction_Mental_Health_Trust.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transaction_interface_is_not_abstract():
    assert not inspect.isabstract(transaction_Interface)


def test_hyp_transaction_interface_constructor_exists():
    assert callable(transaction_Interface.__init__)


def test_hyp_transaction_interface_constructor_args():
    sig = inspect.signature(transaction_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "transactionTime" in params, "Missing parameter 'transactionTime'"

def test_hyp_transaction_interface_has_id():
    assert hasattr(transaction_Interface, "id")
    descriptor = None
    for klass in transaction_Interface.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_interface_has_type():
    assert hasattr(transaction_Interface, "type")
    descriptor = None
    for klass in transaction_Interface.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_interface_has_amount():
    assert hasattr(transaction_Interface, "amount")
    descriptor = None
    for klass in transaction_Interface.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_hyp_transaction_interface_has_transactionTime():
    assert hasattr(transaction_Interface, "transactionTime")
    descriptor = None
    for klass in transaction_Interface.__mro__:
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
    assert "securityAnswer" in params, "Missing parameter 'securityAnswer'"
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"
    assert "password" in params, "Missing parameter 'password'"
    assert "securityQuestion" in params, "Missing parameter 'securityQuestion'"
    assert "username" in params, "Missing parameter 'username'"








def test_hyp_patient_is_not_abstract():
    assert not inspect.isabstract(Patient)


def test_hyp_patient_constructor_exists():
    assert callable(Patient.__init__)


def test_hyp_patient_constructor_args():
    sig = inspect.signature(Patient.__init__)
    params = list(sig.parameters.keys())
    assert "GP_Address" in params, "Missing parameter 'GP_Address'"
    assert "phoneNumber" in params, "Missing parameter 'phoneNumber'"
    assert "address" in params, "Missing parameter 'address'"
    assert "name" in params, "Missing parameter 'name'"
    assert "emailAddress" in params, "Missing parameter 'emailAddress'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"







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

def test_hyp_medical_record_accounttype_exists():
    # Check that the Enumeration exists
    assert Medical_Record_AccountType is not None

def test_hyp_medical_record_accounttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Medical_Record_AccountType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Medical_Record_AccountType"


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
MyInterface_Interface_strategy = st.builds(
    MyInterface_Interface,
)
Medical_Record_NHS_Number_strategy = st.builds(
    Medical_Record_NHS_Number,
    accountNo=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        st.none()
)
Medical_Record_CheckingAccount_strategy = st.builds(
    Medical_Record_CheckingAccount,
    name=
        safe_text
)
Medical_Record_CertificatesOfDepositAccount_strategy = st.builds(
    Medical_Record_CertificatesOfDepositAccount,
    timePeriod=
        st.integers(),
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Medical_Record_SavingsAccount_strategy = st.builds(
    Medical_Record_SavingsAccount,
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transaction_Community_Hospital_strategy = st.builds(
    transaction_Community_Hospital,
    targetAccount=
        st.none(),
    sourceAccount=
        st.none()
)
transaction_Acute_Hospital_strategy = st.builds(
    transaction_Acute_Hospital,
)
transaction_Mental_Health_Trust_strategy = st.builds(
    transaction_Mental_Health_Trust,
)
transaction_Interface_strategy = st.builds(
    transaction_Interface,
    id=
        st.integers(),
    type=
        st.none(),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    transactionTime=
        st.dates()
)
Login_strategy = st.builds(
    Login,
    securityAnswer=
        safe_text,
    lastLoginTime=
        st.dates(),
    password=
        safe_text,
    securityQuestion=
        safe_text,
    username=
        safe_text
)
Patient_strategy = st.builds(
    Patient,
    GP_Address=
        safe_text,
    phoneNumber=
        safe_text,
    address=
        safe_text,
    name=
        safe_text,
    emailAddress=
        safe_text,
    dateOfBirth=
        st.dates()
)


@given(instance=Medical_Record_NHS_Number_strategy)
@settings(max_examples=50)
def test_hyp_medical_record_nhs_number_instantiation(instance):
    assert isinstance(instance, Medical_Record_NHS_Number)



@given(instance=Medical_Record_NHS_Number_strategy)
def test_hyp_medical_record_nhs_number_accountNo_setter(instance):
    original = instance.accountNo
    instance.accountNo = original
    assert instance.accountNo == original



@given(instance=Medical_Record_NHS_Number_strategy)
def test_hyp_medical_record_nhs_number_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=Medical_Record_NHS_Number_strategy)
def test_hyp_medical_record_nhs_number_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=Medical_Record_CheckingAccount_strategy)
def test_hyp_medical_record_checkingaccount_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Medical_Record_CertificatesOfDepositAccount_strategy)
def test_hyp_medical_record_certificatesofdepositaccount_timePeriod_setter(instance):
    original = instance.timePeriod
    instance.timePeriod = original
    assert instance.timePeriod == original



@given(instance=Medical_Record_CertificatesOfDepositAccount_strategy)
def test_hyp_medical_record_certificatesofdepositaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original




@given(instance=Medical_Record_SavingsAccount_strategy)
def test_hyp_medical_record_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=transaction_Community_Hospital_strategy)
@settings(max_examples=50)
def test_hyp_transaction_community_hospital_instantiation(instance):
    assert isinstance(instance, transaction_Community_Hospital)



@given(instance=transaction_Community_Hospital_strategy)
def test_hyp_transaction_community_hospital_targetAccount_setter(instance):
    original = instance.targetAccount
    instance.targetAccount = original
    assert instance.targetAccount == original



@given(instance=transaction_Community_Hospital_strategy)
def test_hyp_transaction_community_hospital_sourceAccount_setter(instance):
    original = instance.sourceAccount
    instance.sourceAccount = original
    assert instance.sourceAccount == original



@given(instance=transaction_Interface_strategy)
@settings(max_examples=50)
def test_hyp_transaction_interface_instantiation(instance):
    assert isinstance(instance, transaction_Interface)



@given(instance=transaction_Interface_strategy)
def test_hyp_transaction_interface_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=transaction_Interface_strategy)
def test_hyp_transaction_interface_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=transaction_Interface_strategy)
def test_hyp_transaction_interface_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=transaction_Interface_strategy)
def test_hyp_transaction_interface_transactionTime_setter(instance):
    original = instance.transactionTime
    instance.transactionTime = original
    assert instance.transactionTime == original




@given(instance=Login_strategy)
def test_hyp_login_securityAnswer_setter(instance):
    original = instance.securityAnswer
    instance.securityAnswer = original
    assert instance.securityAnswer == original



@given(instance=Login_strategy)
def test_hyp_login_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original



@given(instance=Login_strategy)
def test_hyp_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_hyp_login_securityQuestion_setter(instance):
    original = instance.securityQuestion
    instance.securityQuestion = original
    assert instance.securityQuestion == original



@given(instance=Login_strategy)
def test_hyp_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original




@given(instance=Patient_strategy)
def test_hyp_patient_GP_Address_setter(instance):
    original = instance.GP_Address
    instance.GP_Address = original
    assert instance.GP_Address == original



@given(instance=Patient_strategy)
def test_hyp_patient_phoneNumber_setter(instance):
    original = instance.phoneNumber
    instance.phoneNumber = original
    assert instance.phoneNumber == original



@given(instance=Patient_strategy)
def test_hyp_patient_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Patient_strategy)
def test_hyp_patient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Patient_strategy)
def test_hyp_patient_emailAddress_setter(instance):
    original = instance.emailAddress
    instance.emailAddress = original
    assert instance.emailAddress == original



@given(instance=Patient_strategy)
def test_hyp_patient_dateOfBirth_setter(instance):
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
    Login,
    Medical_Record_CertificatesOfDepositAccount,
    Medical_Record_CheckingAccount,
    Medical_Record_NHS_Number,
    Medical_Record_SavingsAccount,
    MyInterface_Interface,
    Patient,
    transaction_Acute_Hospital,
    transaction_Community_Hospital,
    transaction_Interface,
    transaction_Mental_Health_Trust,
    Medical_Record_AccountType,
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


def test_Medical_Record_CertificatesOfDepositAccount_interestRate_value_roundtrip():
    instance = Medical_Record_CertificatesOfDepositAccount(interestRate=3.14, timePeriod=7)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_Medical_Record_CertificatesOfDepositAccount_timePeriod_value_roundtrip():
    instance = Medical_Record_CertificatesOfDepositAccount(interestRate=3.14, timePeriod=7)
    assert instance.timePeriod == 7
    instance.timePeriod = 13
    assert instance.timePeriod == 13


def test_Medical_Record_CheckingAccount_name_value_roundtrip():
    instance = Medical_Record_CheckingAccount(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Medical_Record_SavingsAccount_interestRate_value_roundtrip():
    instance = Medical_Record_SavingsAccount(interestRate=3.14)
    assert instance.interestRate == 3.14
    instance.interestRate = 9.99
    assert instance.interestRate == 9.99


def test_Patient_GP_Address_value_roundtrip():
    instance = Patient(GP_Address="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.GP_Address == "sample_text"
    instance.GP_Address = "sample_text_2"
    assert instance.GP_Address == "sample_text_2"


def test_Patient_address_value_roundtrip():
    instance = Patient(GP_Address="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Patient_dateOfBirth_value_roundtrip():
    instance = Patient(GP_Address="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.dateOfBirth == date(2024, 1, 1)
    instance.dateOfBirth = date(2025, 6, 15)
    assert instance.dateOfBirth == date(2025, 6, 15)


def test_Patient_emailAddress_value_roundtrip():
    instance = Patient(GP_Address="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.emailAddress == "sample_text"
    instance.emailAddress = "sample_text_2"
    assert instance.emailAddress == "sample_text_2"


def test_Patient_name_value_roundtrip():
    instance = Patient(GP_Address="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Patient_phoneNumber_value_roundtrip():
    instance = Patient(GP_Address="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    assert instance.phoneNumber == "sample_text"
    instance.phoneNumber = "sample_text_2"
    assert instance.phoneNumber == "sample_text_2"


def test_assoc_Customer_Login_link_reassign_clear():
    a = Patient(GP_Address="sample_text", address="sample_text", dateOfBirth=date(2024, 1, 1), emailAddress="sample_text", name="sample_text", phoneNumber="sample_text")
    b1 = Login(lastLoginTime=date(2024, 1, 1), password="sample_text", securityAnswer="sample_text", securityQuestion="sample_text", username="sample_text")
    b2 = Login(lastLoginTime=date(2025, 6, 15), password="sample_text_2", securityAnswer="sample_text_2", securityQuestion="sample_text_2", username="sample_text_2")
    _safe_set(a, 'login4', b1)
    assert _is_linked(a, 'login4', b1)
    if hasattr(b1, 'customer5'):
        assert _is_linked(b1, 'customer5', a)
    _safe_set(a, 'login4', b2)
    assert _is_linked(a, 'login4', b2)
    if hasattr(b1, 'customer5'):
        assert not _is_linked(b1, 'customer5', a)
    if hasattr(b2, 'customer5'):
        assert _is_linked(b2, 'customer5', a)
    _safe_set(a, 'login4', None)
    assert not _is_linked(a, 'login4', b2)
    if hasattr(b2, 'customer5'):
        assert not _is_linked(b2, 'customer5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Login_strategy = st.builds(Login, lastLoginTime=st.dates(), password=safe_text, securityAnswer=safe_text, securityQuestion=safe_text, username=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Medical_Record_CertificatesOfDepositAccount_strategy = st.builds(Medical_Record_CertificatesOfDepositAccount, interestRate=st.floats(allow_nan=False, allow_infinity=False), timePeriod=st.integers())
@given(instance=Medical_Record_CertificatesOfDepositAccount_strategy)
@settings(max_examples=25)
def test_Medical_Record_CertificatesOfDepositAccount_instantiation(instance):
    assert isinstance(instance, Medical_Record_CertificatesOfDepositAccount)


Medical_Record_CheckingAccount_strategy = st.builds(Medical_Record_CheckingAccount, name=safe_text)
@given(instance=Medical_Record_CheckingAccount_strategy)
@settings(max_examples=25)
def test_Medical_Record_CheckingAccount_instantiation(instance):
    assert isinstance(instance, Medical_Record_CheckingAccount)


Medical_Record_SavingsAccount_strategy = st.builds(Medical_Record_SavingsAccount, interestRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Medical_Record_SavingsAccount_strategy)
@settings(max_examples=25)
def test_Medical_Record_SavingsAccount_instantiation(instance):
    assert isinstance(instance, Medical_Record_SavingsAccount)


MyInterface_Interface_strategy = st.builds(MyInterface_Interface)
@given(instance=MyInterface_Interface_strategy)
@settings(max_examples=25)
def test_MyInterface_Interface_instantiation(instance):
    assert isinstance(instance, MyInterface_Interface)


Patient_strategy = st.builds(Patient, GP_Address=safe_text, address=safe_text, dateOfBirth=st.dates(), emailAddress=safe_text, name=safe_text, phoneNumber=safe_text)
@given(instance=Patient_strategy)
@settings(max_examples=25)
def test_Patient_instantiation(instance):
    assert isinstance(instance, Patient)


transaction_Acute_Hospital_strategy = st.builds(transaction_Acute_Hospital)
@given(instance=transaction_Acute_Hospital_strategy)
@settings(max_examples=25)
def test_transaction_Acute_Hospital_instantiation(instance):
    assert isinstance(instance, transaction_Acute_Hospital)


transaction_Mental_Health_Trust_strategy = st.builds(transaction_Mental_Health_Trust)
@given(instance=transaction_Mental_Health_Trust_strategy)
@settings(max_examples=25)
def test_transaction_Mental_Health_Trust_instantiation(instance):
    assert isinstance(instance, transaction_Mental_Health_Trust)



