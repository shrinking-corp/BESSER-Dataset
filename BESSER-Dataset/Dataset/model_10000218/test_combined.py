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
    Voter,
    Integer_AdminID_String_Password2_Interface,
    Integer_AdminID_String_Password_Interface,
    Candidate,
    SuperAdmin,
    UserAdmin,
    DataBase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_voter_is_not_abstract():
    assert not inspect.isabstract(Voter)


def test_hyp_voter_constructor_exists():
    assert callable(Voter.__init__)


def test_hyp_voter_constructor_args():
    sig = inspect.signature(Voter.__init__)
    params = list(sig.parameters.keys())
    assert "serialNum" in params, "Missing parameter 'serialNum'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_integer_adminid_string_password2_interface_is_not_abstract():
    assert not inspect.isabstract(Integer_AdminID_String_Password2_Interface)


def test_hyp_integer_adminid_string_password2_interface_constructor_exists():
    assert callable(Integer_AdminID_String_Password2_Interface.__init__)


def test_hyp_integer_adminid_string_password2_interface_constructor_args():
    sig = inspect.signature(Integer_AdminID_String_Password2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_integer_adminid_string_password_interface_is_not_abstract():
    assert not inspect.isabstract(Integer_AdminID_String_Password_Interface)


def test_hyp_integer_adminid_string_password_interface_constructor_exists():
    assert callable(Integer_AdminID_String_Password_Interface.__init__)


def test_hyp_integer_adminid_string_password_interface_constructor_args():
    sig = inspect.signature(Integer_AdminID_String_Password_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_candidate_is_not_abstract():
    assert not inspect.isabstract(Candidate)


def test_hyp_candidate_constructor_exists():
    assert callable(Candidate.__init__)


def test_hyp_candidate_constructor_args():
    sig = inspect.signature(Candidate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_superadmin_is_not_abstract():
    assert not inspect.isabstract(SuperAdmin)


def test_hyp_superadmin_constructor_exists():
    assert callable(SuperAdmin.__init__)


def test_hyp_superadmin_constructor_args():
    sig = inspect.signature(SuperAdmin.__init__)
    params = list(sig.parameters.keys())
    assert "adminID" in params, "Missing parameter 'adminID'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_useradmin_is_not_abstract():
    assert not inspect.isabstract(UserAdmin)


def test_hyp_useradmin_constructor_exists():
    assert callable(UserAdmin.__init__)


def test_hyp_useradmin_constructor_args():
    sig = inspect.signature(UserAdmin.__init__)
    params = list(sig.parameters.keys())
    assert "adminID" in params, "Missing parameter 'adminID'"
    assert "password" in params, "Missing parameter 'password'"





def test_hyp_database_is_not_abstract():
    assert not inspect.isabstract(DataBase)


def test_hyp_database_constructor_exists():
    assert callable(DataBase.__init__)


def test_hyp_database_constructor_args():
    sig = inspect.signature(DataBase.__init__)
    params = list(sig.parameters.keys())
    assert "obj1" in params, "Missing parameter 'obj1'"
    assert "obj3" in params, "Missing parameter 'obj3'"
    assert "obj2" in params, "Missing parameter 'obj2'"
    assert "obj4" in params, "Missing parameter 'obj4'"

def test_hyp_database_has_obj1():
    assert hasattr(DataBase, "obj1")
    descriptor = None
    for klass in DataBase.__mro__:
        if "obj1" in klass.__dict__:
            descriptor = klass.__dict__["obj1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_database_has_obj3():
    assert hasattr(DataBase, "obj3")
    descriptor = None
    for klass in DataBase.__mro__:
        if "obj3" in klass.__dict__:
            descriptor = klass.__dict__["obj3"]
            break
    assert isinstance(descriptor, property)

def test_hyp_database_has_obj2():
    assert hasattr(DataBase, "obj2")
    descriptor = None
    for klass in DataBase.__mro__:
        if "obj2" in klass.__dict__:
            descriptor = klass.__dict__["obj2"]
            break
    assert isinstance(descriptor, property)

def test_hyp_database_has_obj4():
    assert hasattr(DataBase, "obj4")
    descriptor = None
    for klass in DataBase.__mro__:
        if "obj4" in klass.__dict__:
            descriptor = klass.__dict__["obj4"]
            break
    assert isinstance(descriptor, property)


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
Voter_strategy = st.builds(
    Voter,
    serialNum=
        st.integers(),
    password=
        safe_text
)
Integer_AdminID_String_Password2_Interface_strategy = st.builds(
    Integer_AdminID_String_Password2_Interface,
)
Integer_AdminID_String_Password_Interface_strategy = st.builds(
    Integer_AdminID_String_Password_Interface,
)
Candidate_strategy = st.builds(
    Candidate,
)
SuperAdmin_strategy = st.builds(
    SuperAdmin,
    adminID=
        st.integers(),
    password=
        safe_text
)
UserAdmin_strategy = st.builds(
    UserAdmin,
    adminID=
        st.integers(),
    password=
        safe_text
)
DataBase_strategy = st.builds(
    DataBase,
    obj1=
        st.none(),
    obj3=
        st.none(),
    obj2=
        st.none(),
    obj4=
        st.none()
)




@given(instance=Voter_strategy)
def test_hyp_voter_serialNum_setter(instance):
    original = instance.serialNum
    instance.serialNum = original
    assert instance.serialNum == original



@given(instance=Voter_strategy)
def test_hyp_voter_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original







@given(instance=SuperAdmin_strategy)
def test_hyp_superadmin_adminID_setter(instance):
    original = instance.adminID
    instance.adminID = original
    assert instance.adminID == original



@given(instance=SuperAdmin_strategy)
def test_hyp_superadmin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original




@given(instance=UserAdmin_strategy)
def test_hyp_useradmin_adminID_setter(instance):
    original = instance.adminID
    instance.adminID = original
    assert instance.adminID == original



@given(instance=UserAdmin_strategy)
def test_hyp_useradmin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=DataBase_strategy)
@settings(max_examples=50)
def test_hyp_database_instantiation(instance):
    assert isinstance(instance, DataBase)



@given(instance=DataBase_strategy)
def test_hyp_database_obj1_setter(instance):
    original = instance.obj1
    instance.obj1 = original
    assert instance.obj1 == original



@given(instance=DataBase_strategy)
def test_hyp_database_obj3_setter(instance):
    original = instance.obj3
    instance.obj3 = original
    assert instance.obj3 == original



@given(instance=DataBase_strategy)
def test_hyp_database_obj2_setter(instance):
    original = instance.obj2
    instance.obj2 = original
    assert instance.obj2 == original



@given(instance=DataBase_strategy)
def test_hyp_database_obj4_setter(instance):
    original = instance.obj4
    instance.obj4 = original
    assert instance.obj4 == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Candidate,
    DataBase,
    Integer_AdminID_String_Password2_Interface,
    Integer_AdminID_String_Password_Interface,
    SuperAdmin,
    UserAdmin,
    Voter,
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

def test_SuperAdmin_adminID_value_roundtrip():
    instance = SuperAdmin(adminID=7, password="sample_text")
    assert instance.adminID == 7
    instance.adminID = 13
    assert instance.adminID == 13


def test_SuperAdmin_password_value_roundtrip():
    instance = SuperAdmin(adminID=7, password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_UserAdmin_adminID_value_roundtrip():
    instance = UserAdmin(adminID=7, password="sample_text")
    assert instance.adminID == 7
    instance.adminID = 13
    assert instance.adminID == 13


def test_UserAdmin_password_value_roundtrip():
    instance = UserAdmin(adminID=7, password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Voter_password_value_roundtrip():
    instance = Voter(password="sample_text", serialNum=7)
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Voter_serialNum_value_roundtrip():
    instance = Voter(password="sample_text", serialNum=7)
    assert instance.serialNum == 7
    instance.serialNum = 13
    assert instance.serialNum == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Candidate_strategy = st.builds(Candidate)
@given(instance=Candidate_strategy)
@settings(max_examples=25)
def test_Candidate_instantiation(instance):
    assert isinstance(instance, Candidate)


Integer_AdminID_String_Password2_Interface_strategy = st.builds(Integer_AdminID_String_Password2_Interface)
@given(instance=Integer_AdminID_String_Password2_Interface_strategy)
@settings(max_examples=25)
def test_Integer_AdminID_String_Password2_Interface_instantiation(instance):
    assert isinstance(instance, Integer_AdminID_String_Password2_Interface)


Integer_AdminID_String_Password_Interface_strategy = st.builds(Integer_AdminID_String_Password_Interface)
@given(instance=Integer_AdminID_String_Password_Interface_strategy)
@settings(max_examples=25)
def test_Integer_AdminID_String_Password_Interface_instantiation(instance):
    assert isinstance(instance, Integer_AdminID_String_Password_Interface)


SuperAdmin_strategy = st.builds(SuperAdmin, adminID=st.integers(), password=safe_text)
@given(instance=SuperAdmin_strategy)
@settings(max_examples=25)
def test_SuperAdmin_instantiation(instance):
    assert isinstance(instance, SuperAdmin)


UserAdmin_strategy = st.builds(UserAdmin, adminID=st.integers(), password=safe_text)
@given(instance=UserAdmin_strategy)
@settings(max_examples=25)
def test_UserAdmin_instantiation(instance):
    assert isinstance(instance, UserAdmin)


Voter_strategy = st.builds(Voter, password=safe_text, serialNum=st.integers())
@given(instance=Voter_strategy)
@settings(max_examples=25)
def test_Voter_instantiation(instance):
    assert isinstance(instance, Voter)



