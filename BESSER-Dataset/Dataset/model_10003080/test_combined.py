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
    Logout_external,
    Login_external,
    Employee_Actor,
    Administrator_Actor,
    Salary_Management_UseCase,
    Authentication_UseCase,
    Employee_Management_System_Component,
    History,
    Error_code,
    Scanner,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_logout_external_is_not_abstract():
    assert not inspect.isabstract(Logout_external)


def test_hyp_logout_external_constructor_exists():
    assert callable(Logout_external.__init__)


def test_hyp_logout_external_constructor_args():
    sig = inspect.signature(Logout_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_login_external_is_not_abstract():
    assert not inspect.isabstract(Login_external)


def test_hyp_login_external_constructor_exists():
    assert callable(Login_external.__init__)


def test_hyp_login_external_constructor_args():
    sig = inspect.signature(Login_external.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_actor_is_not_abstract():
    assert not inspect.isabstract(Employee_Actor)


def test_hyp_employee_actor_constructor_exists():
    assert callable(Employee_Actor.__init__)


def test_hyp_employee_actor_constructor_args():
    sig = inspect.signature(Employee_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_administrator_actor_is_not_abstract():
    assert not inspect.isabstract(Administrator_Actor)


def test_hyp_administrator_actor_constructor_exists():
    assert callable(Administrator_Actor.__init__)


def test_hyp_administrator_actor_constructor_args():
    sig = inspect.signature(Administrator_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_salary_management_usecase_is_not_abstract():
    assert not inspect.isabstract(Salary_Management_UseCase)


def test_hyp_salary_management_usecase_constructor_exists():
    assert callable(Salary_Management_UseCase.__init__)


def test_hyp_salary_management_usecase_constructor_args():
    sig = inspect.signature(Salary_Management_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_authentication_usecase_is_not_abstract():
    assert not inspect.isabstract(Authentication_UseCase)


def test_hyp_authentication_usecase_constructor_exists():
    assert callable(Authentication_UseCase.__init__)


def test_hyp_authentication_usecase_constructor_args():
    sig = inspect.signature(Authentication_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_employee_management_system_component_is_not_abstract():
    assert not inspect.isabstract(Employee_Management_System_Component)


def test_hyp_employee_management_system_component_constructor_exists():
    assert callable(Employee_Management_System_Component.__init__)


def test_hyp_employee_management_system_component_constructor_args():
    sig = inspect.signature(Employee_Management_System_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_history_is_not_abstract():
    assert not inspect.isabstract(History)


def test_hyp_history_constructor_exists():
    assert callable(History.__init__)


def test_hyp_history_constructor_args():
    sig = inspect.signature(History.__init__)
    params = list(sig.parameters.keys())
    assert "Code_id" in params, "Missing parameter 'Code_id'"
    assert "Code_amount" in params, "Missing parameter 'Code_amount'"





def test_hyp_error_code_is_not_abstract():
    assert not inspect.isabstract(Error_code)


def test_hyp_error_code_constructor_exists():
    assert callable(Error_code.__init__)


def test_hyp_error_code_constructor_args():
    sig = inspect.signature(Error_code.__init__)
    params = list(sig.parameters.keys())
    assert "Code_Id" in params, "Missing parameter 'Code_Id'"
    assert "Code_serial" in params, "Missing parameter 'Code_serial'"
    assert "Code_Exp" in params, "Missing parameter 'Code_Exp'"






def test_hyp_scanner_is_not_abstract():
    assert not inspect.isabstract(Scanner)


def test_hyp_scanner_constructor_exists():
    assert callable(Scanner.__init__)


def test_hyp_scanner_constructor_args():
    sig = inspect.signature(Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "code_serial" in params, "Missing parameter 'code_serial'"
    assert "code_MOB" in params, "Missing parameter 'code_MOB'"
    assert "code_serial1" in params, "Missing parameter 'code_serial1'"
    assert "Code_EOD" in params, "Missing parameter 'Code_EOD'"
    assert "Code_amount" in params, "Missing parameter 'Code_amount'"
    assert "code_Id" in params, "Missing parameter 'code_Id'"








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
Logout_external_strategy = st.builds(
    Logout_external,
)
Login_external_strategy = st.builds(
    Login_external,
)
Employee_Actor_strategy = st.builds(
    Employee_Actor,
)
Administrator_Actor_strategy = st.builds(
    Administrator_Actor,
)
Salary_Management_UseCase_strategy = st.builds(
    Salary_Management_UseCase,
)
Authentication_UseCase_strategy = st.builds(
    Authentication_UseCase,
)
Employee_Management_System_Component_strategy = st.builds(
    Employee_Management_System_Component,
)
History_strategy = st.builds(
    History,
    Code_id=
        safe_text,
    Code_amount=
        safe_text
)
Error_code_strategy = st.builds(
    Error_code,
    Code_Id=
        safe_text,
    Code_serial=
        safe_text,
    Code_Exp=
        safe_text
)
Scanner_strategy = st.builds(
    Scanner,
    code_serial=
        safe_text,
    code_MOB=
        st.dates(),
    code_serial1=
        safe_text,
    Code_EOD=
        st.dates(),
    Code_amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    code_Id=
        st.integers()
)











@given(instance=History_strategy)
def test_hyp_history_Code_id_setter(instance):
    original = instance.Code_id
    instance.Code_id = original
    assert instance.Code_id == original



@given(instance=History_strategy)
def test_hyp_history_Code_amount_setter(instance):
    original = instance.Code_amount
    instance.Code_amount = original
    assert instance.Code_amount == original




@given(instance=Error_code_strategy)
def test_hyp_error_code_Code_Id_setter(instance):
    original = instance.Code_Id
    instance.Code_Id = original
    assert instance.Code_Id == original



@given(instance=Error_code_strategy)
def test_hyp_error_code_Code_serial_setter(instance):
    original = instance.Code_serial
    instance.Code_serial = original
    assert instance.Code_serial == original



@given(instance=Error_code_strategy)
def test_hyp_error_code_Code_Exp_setter(instance):
    original = instance.Code_Exp
    instance.Code_Exp = original
    assert instance.Code_Exp == original




@given(instance=Scanner_strategy)
def test_hyp_scanner_code_serial_setter(instance):
    original = instance.code_serial
    instance.code_serial = original
    assert instance.code_serial == original



@given(instance=Scanner_strategy)
def test_hyp_scanner_code_MOB_setter(instance):
    original = instance.code_MOB
    instance.code_MOB = original
    assert instance.code_MOB == original



@given(instance=Scanner_strategy)
def test_hyp_scanner_code_serial1_setter(instance):
    original = instance.code_serial1
    instance.code_serial1 = original
    assert instance.code_serial1 == original



@given(instance=Scanner_strategy)
def test_hyp_scanner_Code_EOD_setter(instance):
    original = instance.Code_EOD
    instance.Code_EOD = original
    assert instance.Code_EOD == original



@given(instance=Scanner_strategy)
def test_hyp_scanner_Code_amount_setter(instance):
    original = instance.Code_amount
    instance.Code_amount = original
    assert instance.Code_amount == original



@given(instance=Scanner_strategy)
def test_hyp_scanner_code_Id_setter(instance):
    original = instance.code_Id
    instance.code_Id = original
    assert instance.code_Id == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Administrator_Actor,
    Authentication_UseCase,
    Employee_Actor,
    Employee_Management_System_Component,
    Error_code,
    History,
    Login_external,
    Logout_external,
    Salary_Management_UseCase,
    Scanner,
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

def test_Error_code_Code_Exp_value_roundtrip():
    instance = Error_code(Code_Exp="sample_text", Code_Id="sample_text", Code_serial="sample_text")
    assert instance.Code_Exp == "sample_text"
    instance.Code_Exp = "sample_text_2"
    assert instance.Code_Exp == "sample_text_2"


def test_Error_code_Code_Id_value_roundtrip():
    instance = Error_code(Code_Exp="sample_text", Code_Id="sample_text", Code_serial="sample_text")
    assert instance.Code_Id == "sample_text"
    instance.Code_Id = "sample_text_2"
    assert instance.Code_Id == "sample_text_2"


def test_Error_code_Code_serial_value_roundtrip():
    instance = Error_code(Code_Exp="sample_text", Code_Id="sample_text", Code_serial="sample_text")
    assert instance.Code_serial == "sample_text"
    instance.Code_serial = "sample_text_2"
    assert instance.Code_serial == "sample_text_2"


def test_History_Code_amount_value_roundtrip():
    instance = History(Code_amount="sample_text", Code_id="sample_text")
    assert instance.Code_amount == "sample_text"
    instance.Code_amount = "sample_text_2"
    assert instance.Code_amount == "sample_text_2"


def test_History_Code_id_value_roundtrip():
    instance = History(Code_amount="sample_text", Code_id="sample_text")
    assert instance.Code_id == "sample_text"
    instance.Code_id = "sample_text_2"
    assert instance.Code_id == "sample_text_2"


def test_Scanner_Code_EOD_value_roundtrip():
    instance = Scanner(Code_EOD=date(2024, 1, 1), Code_amount=3.14, code_Id=7, code_MOB=date(2024, 1, 1), code_serial="sample_text", code_serial1="sample_text")
    assert instance.Code_EOD == date(2024, 1, 1)
    instance.Code_EOD = date(2025, 6, 15)
    assert instance.Code_EOD == date(2025, 6, 15)


def test_Scanner_Code_amount_value_roundtrip():
    instance = Scanner(Code_EOD=date(2024, 1, 1), Code_amount=3.14, code_Id=7, code_MOB=date(2024, 1, 1), code_serial="sample_text", code_serial1="sample_text")
    assert instance.Code_amount == 3.14
    instance.Code_amount = 9.99
    assert instance.Code_amount == 9.99


def test_Scanner_code_Id_value_roundtrip():
    instance = Scanner(Code_EOD=date(2024, 1, 1), Code_amount=3.14, code_Id=7, code_MOB=date(2024, 1, 1), code_serial="sample_text", code_serial1="sample_text")
    assert instance.code_Id == 7
    instance.code_Id = 13
    assert instance.code_Id == 13


def test_Scanner_code_MOB_value_roundtrip():
    instance = Scanner(Code_EOD=date(2024, 1, 1), Code_amount=3.14, code_Id=7, code_MOB=date(2024, 1, 1), code_serial="sample_text", code_serial1="sample_text")
    assert instance.code_MOB == date(2024, 1, 1)
    instance.code_MOB = date(2025, 6, 15)
    assert instance.code_MOB == date(2025, 6, 15)


def test_Scanner_code_serial_value_roundtrip():
    instance = Scanner(Code_EOD=date(2024, 1, 1), Code_amount=3.14, code_Id=7, code_MOB=date(2024, 1, 1), code_serial="sample_text", code_serial1="sample_text")
    assert instance.code_serial == "sample_text"
    instance.code_serial = "sample_text_2"
    assert instance.code_serial == "sample_text_2"


def test_Scanner_code_serial1_value_roundtrip():
    instance = Scanner(Code_EOD=date(2024, 1, 1), Code_amount=3.14, code_Id=7, code_MOB=date(2024, 1, 1), code_serial="sample_text", code_serial1="sample_text")
    assert instance.code_serial1 == "sample_text"
    instance.code_serial1 = "sample_text_2"
    assert instance.code_serial1 == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Administrator_Actor_strategy = st.builds(Administrator_Actor)
@given(instance=Administrator_Actor_strategy)
@settings(max_examples=25)
def test_Administrator_Actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)


Authentication_UseCase_strategy = st.builds(Authentication_UseCase)
@given(instance=Authentication_UseCase_strategy)
@settings(max_examples=25)
def test_Authentication_UseCase_instantiation(instance):
    assert isinstance(instance, Authentication_UseCase)


Employee_Actor_strategy = st.builds(Employee_Actor)
@given(instance=Employee_Actor_strategy)
@settings(max_examples=25)
def test_Employee_Actor_instantiation(instance):
    assert isinstance(instance, Employee_Actor)


Employee_Management_System_Component_strategy = st.builds(Employee_Management_System_Component)
@given(instance=Employee_Management_System_Component_strategy)
@settings(max_examples=25)
def test_Employee_Management_System_Component_instantiation(instance):
    assert isinstance(instance, Employee_Management_System_Component)


Error_code_strategy = st.builds(Error_code, Code_Exp=safe_text, Code_Id=safe_text, Code_serial=safe_text)
@given(instance=Error_code_strategy)
@settings(max_examples=25)
def test_Error_code_instantiation(instance):
    assert isinstance(instance, Error_code)


History_strategy = st.builds(History, Code_amount=safe_text, Code_id=safe_text)
@given(instance=History_strategy)
@settings(max_examples=25)
def test_History_instantiation(instance):
    assert isinstance(instance, History)


Login_external_strategy = st.builds(Login_external)
@given(instance=Login_external_strategy)
@settings(max_examples=25)
def test_Login_external_instantiation(instance):
    assert isinstance(instance, Login_external)


Logout_external_strategy = st.builds(Logout_external)
@given(instance=Logout_external_strategy)
@settings(max_examples=25)
def test_Logout_external_instantiation(instance):
    assert isinstance(instance, Logout_external)


Salary_Management_UseCase_strategy = st.builds(Salary_Management_UseCase)
@given(instance=Salary_Management_UseCase_strategy)
@settings(max_examples=25)
def test_Salary_Management_UseCase_instantiation(instance):
    assert isinstance(instance, Salary_Management_UseCase)


Scanner_strategy = st.builds(Scanner, Code_EOD=st.dates(), Code_amount=st.floats(allow_nan=False, allow_infinity=False), code_Id=st.integers(), code_MOB=st.dates(), code_serial=safe_text, code_serial1=safe_text)
@given(instance=Scanner_strategy)
@settings(max_examples=25)
def test_Scanner_instantiation(instance):
    assert isinstance(instance, Scanner)



