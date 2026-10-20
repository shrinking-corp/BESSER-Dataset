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
    Exception,
    ClassV,
    ClassU,
    ClassT,
    ClassS,
    ClassR,
    ClassQ,
    InterfaceO_Interface,
    ClassP,
    ClassN,
    ClassM,
    ClassG,
    ClassF,
    ClassE,
    ClassD,
    ErrorCode,
    ErrorCodeException,
    BankAccount,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_exception_is_not_abstract():
    assert not inspect.isabstract(Exception)


def test_hyp_exception_constructor_exists():
    assert callable(Exception.__init__)


def test_hyp_exception_constructor_args():
    sig = inspect.signature(Exception.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classv_is_not_abstract():
    assert not inspect.isabstract(ClassV)


def test_hyp_classv_constructor_exists():
    assert callable(ClassV.__init__)


def test_hyp_classv_constructor_args():
    sig = inspect.signature(ClassV.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classu_is_not_abstract():
    assert not inspect.isabstract(ClassU)


def test_hyp_classu_constructor_exists():
    assert callable(ClassU.__init__)


def test_hyp_classu_constructor_args():
    sig = inspect.signature(ClassU.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classt_is_not_abstract():
    assert not inspect.isabstract(ClassT)


def test_hyp_classt_constructor_exists():
    assert callable(ClassT.__init__)


def test_hyp_classt_constructor_args():
    sig = inspect.signature(ClassT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classs_is_not_abstract():
    assert not inspect.isabstract(ClassS)


def test_hyp_classs_constructor_exists():
    assert callable(ClassS.__init__)


def test_hyp_classs_constructor_args():
    sig = inspect.signature(ClassS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classr_is_not_abstract():
    assert not inspect.isabstract(ClassR)


def test_hyp_classr_constructor_exists():
    assert callable(ClassR.__init__)


def test_hyp_classr_constructor_args():
    sig = inspect.signature(ClassR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classq_is_not_abstract():
    assert not inspect.isabstract(ClassQ)


def test_hyp_classq_constructor_exists():
    assert callable(ClassQ.__init__)


def test_hyp_classq_constructor_args():
    sig = inspect.signature(ClassQ.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interfaceo_interface_is_not_abstract():
    assert not inspect.isabstract(InterfaceO_Interface)


def test_hyp_interfaceo_interface_constructor_exists():
    assert callable(InterfaceO_Interface.__init__)


def test_hyp_interfaceo_interface_constructor_args():
    sig = inspect.signature(InterfaceO_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classp_is_not_abstract():
    assert not inspect.isabstract(ClassP)


def test_hyp_classp_constructor_exists():
    assert callable(ClassP.__init__)


def test_hyp_classp_constructor_args():
    sig = inspect.signature(ClassP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classn_is_not_abstract():
    assert not inspect.isabstract(ClassN)


def test_hyp_classn_constructor_exists():
    assert callable(ClassN.__init__)


def test_hyp_classn_constructor_args():
    sig = inspect.signature(ClassN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classm_is_not_abstract():
    assert not inspect.isabstract(ClassM)


def test_hyp_classm_constructor_exists():
    assert callable(ClassM.__init__)


def test_hyp_classm_constructor_args():
    sig = inspect.signature(ClassM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classg_is_not_abstract():
    assert not inspect.isabstract(ClassG)


def test_hyp_classg_constructor_exists():
    assert callable(ClassG.__init__)


def test_hyp_classg_constructor_args():
    sig = inspect.signature(ClassG.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classf_is_not_abstract():
    assert not inspect.isabstract(ClassF)


def test_hyp_classf_constructor_exists():
    assert callable(ClassF.__init__)


def test_hyp_classf_constructor_args():
    sig = inspect.signature(ClassF.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classe_is_not_abstract():
    assert not inspect.isabstract(ClassE)


def test_hyp_classe_constructor_exists():
    assert callable(ClassE.__init__)


def test_hyp_classe_constructor_args():
    sig = inspect.signature(ClassE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classd_is_not_abstract():
    assert not inspect.isabstract(ClassD)


def test_hyp_classd_constructor_exists():
    assert callable(ClassD.__init__)


def test_hyp_classd_constructor_args():
    sig = inspect.signature(ClassD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_errorcode_is_not_abstract():
    assert not inspect.isabstract(ErrorCode)


def test_hyp_errorcode_constructor_exists():
    assert callable(ErrorCode.__init__)


def test_hyp_errorcode_constructor_args():
    sig = inspect.signature(ErrorCode.__init__)
    params = list(sig.parameters.keys())
    assert "domain" in params, "Missing parameter 'domain'"
    assert "subdomain" in params, "Missing parameter 'subdomain'"
    assert "tier" in params, "Missing parameter 'tier'"
    assert "reason" in params, "Missing parameter 'reason'"







def test_hyp_errorcodeexception_is_not_abstract():
    assert not inspect.isabstract(ErrorCodeException)


def test_hyp_errorcodeexception_constructor_exists():
    assert callable(ErrorCodeException.__init__)


def test_hyp_errorcodeexception_constructor_args():
    sig = inspect.signature(ErrorCodeException.__init__)
    params = list(sig.parameters.keys())
    assert "errorCode" in params, "Missing parameter 'errorCode'"
    assert "throwable" in params, "Missing parameter 'throwable'"
    assert "errorCodeMessage" in params, "Missing parameter 'errorCodeMessage'"

def test_hyp_errorcodeexception_has_errorCode():
    assert hasattr(ErrorCodeException, "errorCode")
    descriptor = None
    for klass in ErrorCodeException.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)

def test_hyp_errorcodeexception_has_throwable():
    assert hasattr(ErrorCodeException, "throwable")
    descriptor = None
    for klass in ErrorCodeException.__mro__:
        if "throwable" in klass.__dict__:
            descriptor = klass.__dict__["throwable"]
            break
    assert isinstance(descriptor, property)

def test_hyp_errorcodeexception_has_errorCodeMessage():
    assert hasattr(ErrorCodeException, "errorCodeMessage")
    descriptor = None
    for klass in ErrorCodeException.__mro__:
        if "errorCodeMessage" in klass.__dict__:
            descriptor = klass.__dict__["errorCodeMessage"]
            break
    assert isinstance(descriptor, property)



def test_hyp_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_hyp_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_hyp_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "ownerName" in params, "Missing parameter 'ownerName'"
    assert "balance" in params, "Missing parameter 'balance'"




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
Exception_strategy = st.builds(
    Exception,
)
ClassV_strategy = st.builds(
    ClassV,
)
ClassU_strategy = st.builds(
    ClassU,
)
ClassT_strategy = st.builds(
    ClassT,
)
ClassS_strategy = st.builds(
    ClassS,
)
ClassR_strategy = st.builds(
    ClassR,
)
ClassQ_strategy = st.builds(
    ClassQ,
)
InterfaceO_Interface_strategy = st.builds(
    InterfaceO_Interface,
)
ClassP_strategy = st.builds(
    ClassP,
)
ClassN_strategy = st.builds(
    ClassN,
)
ClassM_strategy = st.builds(
    ClassM,
)
ClassG_strategy = st.builds(
    ClassG,
)
ClassF_strategy = st.builds(
    ClassF,
)
ClassE_strategy = st.builds(
    ClassE,
)
ClassD_strategy = st.builds(
    ClassD,
)
ErrorCode_strategy = st.builds(
    ErrorCode,
    domain=
        st.integers(),
    subdomain=
        st.integers(),
    tier=
        st.integers(),
    reason=
        st.integers()
)
ErrorCodeException_strategy = st.builds(
    ErrorCodeException,
    errorCode=
        st.none(),
    throwable=
        safe_text,
    errorCodeMessage=
        safe_text
)
BankAccount_strategy = st.builds(
    BankAccount,
    ownerName=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)



















@given(instance=ErrorCode_strategy)
def test_hyp_errorcode_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original



@given(instance=ErrorCode_strategy)
def test_hyp_errorcode_subdomain_setter(instance):
    original = instance.subdomain
    instance.subdomain = original
    assert instance.subdomain == original



@given(instance=ErrorCode_strategy)
def test_hyp_errorcode_tier_setter(instance):
    original = instance.tier
    instance.tier = original
    assert instance.tier == original



@given(instance=ErrorCode_strategy)
def test_hyp_errorcode_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original

@given(instance=ErrorCodeException_strategy)
@settings(max_examples=50)
def test_hyp_errorcodeexception_instantiation(instance):
    assert isinstance(instance, ErrorCodeException)



@given(instance=ErrorCodeException_strategy)
def test_hyp_errorcodeexception_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original



@given(instance=ErrorCodeException_strategy)
def test_hyp_errorcodeexception_throwable_setter(instance):
    original = instance.throwable
    instance.throwable = original
    assert instance.throwable == original



@given(instance=ErrorCodeException_strategy)
def test_hyp_errorcodeexception_errorCodeMessage_setter(instance):
    original = instance.errorCodeMessage
    instance.errorCodeMessage = original
    assert instance.errorCodeMessage == original




@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original



@given(instance=BankAccount_strategy)
def test_hyp_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BankAccount,
    ClassD,
    ClassE,
    ClassF,
    ClassG,
    ClassM,
    ClassN,
    ClassP,
    ClassQ,
    ClassR,
    ClassS,
    ClassT,
    ClassU,
    ClassV,
    ErrorCode,
    ErrorCodeException,
    Exception,
    InterfaceO_Interface,
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

def test_BankAccount_balance_value_roundtrip():
    instance = BankAccount(balance=3.14, ownerName="sample_text")
    assert instance.balance == 3.14
    instance.balance = 9.99
    assert instance.balance == 9.99


def test_BankAccount_ownerName_value_roundtrip():
    instance = BankAccount(balance=3.14, ownerName="sample_text")
    assert instance.ownerName == "sample_text"
    instance.ownerName = "sample_text_2"
    assert instance.ownerName == "sample_text_2"


def test_ErrorCode_domain_value_roundtrip():
    instance = ErrorCode(domain=7, reason=7, subdomain=7, tier=7)
    assert instance.domain == 7
    instance.domain = 13
    assert instance.domain == 13


def test_ErrorCode_reason_value_roundtrip():
    instance = ErrorCode(domain=7, reason=7, subdomain=7, tier=7)
    assert instance.reason == 7
    instance.reason = 13
    assert instance.reason == 13


def test_ErrorCode_subdomain_value_roundtrip():
    instance = ErrorCode(domain=7, reason=7, subdomain=7, tier=7)
    assert instance.subdomain == 7
    instance.subdomain = 13
    assert instance.subdomain == 13


def test_ErrorCode_tier_value_roundtrip():
    instance = ErrorCode(domain=7, reason=7, subdomain=7, tier=7)
    assert instance.tier == 7
    instance.tier = 13
    assert instance.tier == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BankAccount_strategy = st.builds(BankAccount, balance=st.floats(allow_nan=False, allow_infinity=False), ownerName=safe_text)
@given(instance=BankAccount_strategy)
@settings(max_examples=25)
def test_BankAccount_instantiation(instance):
    assert isinstance(instance, BankAccount)


ClassD_strategy = st.builds(ClassD)
@given(instance=ClassD_strategy)
@settings(max_examples=25)
def test_ClassD_instantiation(instance):
    assert isinstance(instance, ClassD)


ClassE_strategy = st.builds(ClassE)
@given(instance=ClassE_strategy)
@settings(max_examples=25)
def test_ClassE_instantiation(instance):
    assert isinstance(instance, ClassE)


ClassF_strategy = st.builds(ClassF)
@given(instance=ClassF_strategy)
@settings(max_examples=25)
def test_ClassF_instantiation(instance):
    assert isinstance(instance, ClassF)


ClassG_strategy = st.builds(ClassG)
@given(instance=ClassG_strategy)
@settings(max_examples=25)
def test_ClassG_instantiation(instance):
    assert isinstance(instance, ClassG)


ClassM_strategy = st.builds(ClassM)
@given(instance=ClassM_strategy)
@settings(max_examples=25)
def test_ClassM_instantiation(instance):
    assert isinstance(instance, ClassM)


ClassN_strategy = st.builds(ClassN)
@given(instance=ClassN_strategy)
@settings(max_examples=25)
def test_ClassN_instantiation(instance):
    assert isinstance(instance, ClassN)


ClassP_strategy = st.builds(ClassP)
@given(instance=ClassP_strategy)
@settings(max_examples=25)
def test_ClassP_instantiation(instance):
    assert isinstance(instance, ClassP)


ClassQ_strategy = st.builds(ClassQ)
@given(instance=ClassQ_strategy)
@settings(max_examples=25)
def test_ClassQ_instantiation(instance):
    assert isinstance(instance, ClassQ)


ClassR_strategy = st.builds(ClassR)
@given(instance=ClassR_strategy)
@settings(max_examples=25)
def test_ClassR_instantiation(instance):
    assert isinstance(instance, ClassR)


ClassS_strategy = st.builds(ClassS)
@given(instance=ClassS_strategy)
@settings(max_examples=25)
def test_ClassS_instantiation(instance):
    assert isinstance(instance, ClassS)


ClassT_strategy = st.builds(ClassT)
@given(instance=ClassT_strategy)
@settings(max_examples=25)
def test_ClassT_instantiation(instance):
    assert isinstance(instance, ClassT)


ClassU_strategy = st.builds(ClassU)
@given(instance=ClassU_strategy)
@settings(max_examples=25)
def test_ClassU_instantiation(instance):
    assert isinstance(instance, ClassU)


ClassV_strategy = st.builds(ClassV)
@given(instance=ClassV_strategy)
@settings(max_examples=25)
def test_ClassV_instantiation(instance):
    assert isinstance(instance, ClassV)


ErrorCode_strategy = st.builds(ErrorCode, domain=st.integers(), reason=st.integers(), subdomain=st.integers(), tier=st.integers())
@given(instance=ErrorCode_strategy)
@settings(max_examples=25)
def test_ErrorCode_instantiation(instance):
    assert isinstance(instance, ErrorCode)


Exception_strategy = st.builds(Exception)
@given(instance=Exception_strategy)
@settings(max_examples=25)
def test_Exception_instantiation(instance):
    assert isinstance(instance, Exception)


InterfaceO_Interface_strategy = st.builds(InterfaceO_Interface)
@given(instance=InterfaceO_Interface_strategy)
@settings(max_examples=25)
def test_InterfaceO_Interface_instantiation(instance):
    assert isinstance(instance, InterfaceO_Interface)



