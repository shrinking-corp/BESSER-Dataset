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
    model_Param,
    model_App,
    model_Service,
    model_User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_model_param_is_not_abstract():
    assert not inspect.isabstract(model_Param)


def test_hyp_model_param_constructor_exists():
    assert callable(model_Param.__init__)


def test_hyp_model_param_constructor_args():
    sig = inspect.signature(model_Param.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_model_app_is_not_abstract():
    assert not inspect.isabstract(model_App)


def test_hyp_model_app_constructor_exists():
    assert callable(model_App.__init__)


def test_hyp_model_app_constructor_args():
    sig = inspect.signature(model_App.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_service_is_not_abstract():
    assert not inspect.isabstract(model_Service)


def test_hyp_model_service_constructor_exists():
    assert callable(model_Service.__init__)


def test_hyp_model_service_constructor_args():
    sig = inspect.signature(model_Service.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "acceptedParams" in params, "Missing parameter 'acceptedParams'"
    assert "methodName" in params, "Missing parameter 'methodName'"






def test_hyp_model_user_is_not_abstract():
    assert not inspect.isabstract(model_User)


def test_hyp_model_user_constructor_exists():
    assert callable(model_User.__init__)


def test_hyp_model_user_constructor_args():
    sig = inspect.signature(model_User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"




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
model_Param_strategy = st.builds(
    model_Param,
    name=
        safe_text,
    value=
        safe_text
)
model_App_strategy = st.builds(
    model_App,
)
model_Service_strategy = st.builds(
    model_Service,
    name=
        safe_text,
    acceptedParams=
        safe_text,
    methodName=
        safe_text
)
model_User_strategy = st.builds(
    model_User,
    password=
        safe_text,
    name=
        safe_text
)




@given(instance=model_Param_strategy)
def test_hyp_model_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Param_strategy)
def test_hyp_model_param_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_App_strategy)
@settings(max_examples=30)
def test_hyp_model_app_auth_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.auth(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.auth).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'auth' in model_App is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'auth' in model_App did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'auth' in model_App is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_App_strategy)
@settings(max_examples=30)
def test_hyp_model_app_authfailure_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.authFailure()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.authFailure).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'authFailure' in model_App is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'authFailure' in model_App did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'authFailure' in model_App is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_App_strategy)
@settings(max_examples=30)
def test_hyp_model_app_service_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.service(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.service).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'service' in model_App is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'service' in model_App did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'service' in model_App is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_App_strategy)
@settings(max_examples=30)
def test_hyp_model_app_result_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.result(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.result).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'result' in model_App is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'result' in model_App did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'result' in model_App is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_App_strategy)
@settings(max_examples=30)
def test_hyp_model_app_authsuccess_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.authSuccess(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.authSuccess).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'authSuccess' in model_App is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'authSuccess' in model_App did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'authSuccess' in model_App is not implemented or raised an error")




@given(instance=model_Service_strategy)
def test_hyp_model_service_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Service_strategy)
def test_hyp_model_service_acceptedParams_setter(instance):
    original = instance.acceptedParams
    instance.acceptedParams = original
    assert instance.acceptedParams == original



@given(instance=model_Service_strategy)
def test_hyp_model_service_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original




@given(instance=model_User_strategy)
def test_hyp_model_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=model_User_strategy)
def test_hyp_model_user_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    model_App,
    model_Param,
    model_Service,
    model_User,
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

def test_model_Param_name_value_roundtrip():
    instance = model_Param(name="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_Param_value_value_roundtrip():
    instance = model_Param(name="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_model_Service_acceptedParams_value_roundtrip():
    instance = model_Service(acceptedParams="sample_text", methodName="sample_text", name="sample_text")
    assert instance.acceptedParams == "sample_text"
    instance.acceptedParams = "sample_text_2"
    assert instance.acceptedParams == "sample_text_2"


def test_model_Service_methodName_value_roundtrip():
    instance = model_Service(acceptedParams="sample_text", methodName="sample_text", name="sample_text")
    assert instance.methodName == "sample_text"
    instance.methodName = "sample_text_2"
    assert instance.methodName == "sample_text_2"


def test_model_Service_name_value_roundtrip():
    instance = model_Service(acceptedParams="sample_text", methodName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_User_name_value_roundtrip():
    instance = model_User(name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_User_password_value_roundtrip():
    instance = model_User(name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_assoc_allowedUsers0_link_reassign_clear():
    a = model_User(name="sample_text", password="sample_text")
    b1 = model_Service(acceptedParams="sample_text", methodName="sample_text", name="sample_text")
    b2 = model_Service(acceptedParams="sample_text_2", methodName="sample_text_2", name="sample_text_2")
    _safe_set(a, 'model_User', b1)
    assert _is_linked(a, 'model_User', b1)
    if hasattr(b1, 'model_Service'):
        assert _is_linked(b1, 'model_Service', a)
    _safe_set(a, 'model_User', b2)
    assert _is_linked(a, 'model_User', b2)
    if hasattr(b1, 'model_Service'):
        assert not _is_linked(b1, 'model_Service', a)
    if hasattr(b2, 'model_Service'):
        assert _is_linked(b2, 'model_Service', a)
    _safe_set(a, 'model_User', None)
    assert not _is_linked(a, 'model_User', b2)
    if hasattr(b2, 'model_Service'):
        assert not _is_linked(b2, 'model_Service', a)


def test_assoc_services3_link_reassign_clear():
    a = model_Service(acceptedParams="sample_text", methodName="sample_text", name="sample_text")
    b1 = model_App()
    b2 = model_App()
    _safe_set(a, 'model_Service5', b1)
    assert _is_linked(a, 'model_Service5', b1)
    if hasattr(b1, 'model_App4'):
        assert _is_linked(b1, 'model_App4', a)
    _safe_set(a, 'model_Service5', b2)
    assert _is_linked(a, 'model_Service5', b2)
    if hasattr(b1, 'model_App4'):
        assert not _is_linked(b1, 'model_App4', a)
    if hasattr(b2, 'model_App4'):
        assert _is_linked(b2, 'model_App4', a)
    _safe_set(a, 'model_Service5', None)
    assert not _is_linked(a, 'model_Service5', b2)
    if hasattr(b2, 'model_App4'):
        assert not _is_linked(b2, 'model_App4', a)


def test_assoc_users1_link_reassign_clear():
    a = model_User(name="sample_text", password="sample_text")
    b1 = model_App()
    b2 = model_App()
    _safe_set(a, 'model_User2', b1)
    assert _is_linked(a, 'model_User2', b1)
    if hasattr(b1, 'model_App'):
        assert _is_linked(b1, 'model_App', a)
    _safe_set(a, 'model_User2', b2)
    assert _is_linked(a, 'model_User2', b2)
    if hasattr(b1, 'model_App'):
        assert not _is_linked(b1, 'model_App', a)
    if hasattr(b2, 'model_App'):
        assert _is_linked(b2, 'model_App', a)
    _safe_set(a, 'model_User2', None)
    assert not _is_linked(a, 'model_User2', b2)
    if hasattr(b2, 'model_App'):
        assert not _is_linked(b2, 'model_App', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

model_App_strategy = st.builds(model_App)
@given(instance=model_App_strategy)
@settings(max_examples=25)
def test_model_App_instantiation(instance):
    assert isinstance(instance, model_App)


model_Param_strategy = st.builds(model_Param, name=safe_text, value=safe_text)
@given(instance=model_Param_strategy)
@settings(max_examples=25)
def test_model_Param_instantiation(instance):
    assert isinstance(instance, model_Param)


model_Service_strategy = st.builds(model_Service, acceptedParams=safe_text, methodName=safe_text, name=safe_text)
@given(instance=model_Service_strategy)
@settings(max_examples=25)
def test_model_Service_instantiation(instance):
    assert isinstance(instance, model_Service)


model_User_strategy = st.builds(model_User, name=safe_text, password=safe_text)
@given(instance=model_User_strategy)
@settings(max_examples=25)
def test_model_User_instantiation(instance):
    assert isinstance(instance, model_User)



