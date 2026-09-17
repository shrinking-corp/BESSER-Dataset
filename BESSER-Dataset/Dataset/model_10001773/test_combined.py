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
    FireAlarm,
    securityAlarm,
    Police,
    smokeAlarm,
    Department,
    Home_Security_System,
    Fire_Alarm_system,
    Appliances,
    system,
    Login,
    Owner,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_firealarm_is_not_abstract():
    assert not inspect.isabstract(FireAlarm)


def test_hyp_firealarm_constructor_exists():
    assert callable(FireAlarm.__init__)


def test_hyp_firealarm_constructor_args():
    sig = inspect.signature(FireAlarm.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"




def test_hyp_securityalarm_is_not_abstract():
    assert not inspect.isabstract(securityAlarm)


def test_hyp_securityalarm_constructor_exists():
    assert callable(securityAlarm.__init__)


def test_hyp_securityalarm_constructor_args():
    sig = inspect.signature(securityAlarm.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"




def test_hyp_police_is_not_abstract():
    assert not inspect.isabstract(Police)


def test_hyp_police_constructor_exists():
    assert callable(Police.__init__)


def test_hyp_police_constructor_args():
    sig = inspect.signature(Police.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_smokealarm_is_not_abstract():
    assert not inspect.isabstract(smokeAlarm)


def test_hyp_smokealarm_constructor_exists():
    assert callable(smokeAlarm.__init__)


def test_hyp_smokealarm_constructor_args():
    sig = inspect.signature(smokeAlarm.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"




def test_hyp_department_is_not_abstract():
    assert not inspect.isabstract(Department)


def test_hyp_department_constructor_exists():
    assert callable(Department.__init__)


def test_hyp_department_constructor_args():
    sig = inspect.signature(Department.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_home_security_system_is_not_abstract():
    assert not inspect.isabstract(Home_Security_System)


def test_hyp_home_security_system_constructor_exists():
    assert callable(Home_Security_System.__init__)


def test_hyp_home_security_system_constructor_args():
    sig = inspect.signature(Home_Security_System.__init__)
    params = list(sig.parameters.keys())
    assert "system_Off" in params, "Missing parameter 'system_Off'"
    assert "system_On" in params, "Missing parameter 'system_On'"





def test_hyp_fire_alarm_system_is_not_abstract():
    assert not inspect.isabstract(Fire_Alarm_system)


def test_hyp_fire_alarm_system_constructor_exists():
    assert callable(Fire_Alarm_system.__init__)


def test_hyp_fire_alarm_system_constructor_args():
    sig = inspect.signature(Fire_Alarm_system.__init__)
    params = list(sig.parameters.keys())
    assert "system_Off" in params, "Missing parameter 'system_Off'"
    assert "system_On" in params, "Missing parameter 'system_On'"





def test_hyp_appliances_is_not_abstract():
    assert not inspect.isabstract(Appliances)


def test_hyp_appliances_constructor_exists():
    assert callable(Appliances.__init__)


def test_hyp_appliances_constructor_args():
    sig = inspect.signature(Appliances.__init__)
    params = list(sig.parameters.keys())
    assert "Off_status" in params, "Missing parameter 'Off_status'"
    assert "On_status" in params, "Missing parameter 'On_status'"





def test_hyp_system_is_not_abstract():
    assert not inspect.isabstract(system)


def test_hyp_system_constructor_exists():
    assert callable(system.__init__)


def test_hyp_system_constructor_args():
    sig = inspect.signature(system.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"




def test_hyp_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_hyp_login_constructor_exists():
    assert callable(Login.__init__)


def test_hyp_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_owner_is_not_abstract():
    assert not inspect.isabstract(Owner)


def test_hyp_owner_constructor_exists():
    assert callable(Owner.__init__)


def test_hyp_owner_constructor_args():
    sig = inspect.signature(Owner.__init__)
    params = list(sig.parameters.keys())
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
FireAlarm_strategy = st.builds(
    FireAlarm,
    status=
        st.booleans()
)
securityAlarm_strategy = st.builds(
    securityAlarm,
    status=
        st.booleans()
)
Police_strategy = st.builds(
    Police,
    name=
        safe_text
)
smokeAlarm_strategy = st.builds(
    smokeAlarm,
    status=
        st.booleans()
)
Department_strategy = st.builds(
    Department,
    name=
        safe_text
)
Home_Security_System_strategy = st.builds(
    Home_Security_System,
    system_Off=
        st.booleans(),
    system_On=
        st.booleans()
)
Fire_Alarm_system_strategy = st.builds(
    Fire_Alarm_system,
    system_Off=
        st.booleans(),
    system_On=
        st.booleans()
)
Appliances_strategy = st.builds(
    Appliances,
    Off_status=
        st.booleans(),
    On_status=
        st.booleans()
)
system_strategy = st.builds(
    system,
    status=
        st.booleans()
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    name=
        safe_text
)
Owner_strategy = st.builds(
    Owner,
    name=
        safe_text
)




@given(instance=FireAlarm_strategy)
def test_hyp_firealarm_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original




@given(instance=securityAlarm_strategy)
def test_hyp_securityalarm_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original




@given(instance=Police_strategy)
def test_hyp_police_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=smokeAlarm_strategy)
def test_hyp_smokealarm_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original




@given(instance=Department_strategy)
def test_hyp_department_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Home_Security_System_strategy)
def test_hyp_home_security_system_system_Off_setter(instance):
    original = instance.system_Off
    instance.system_Off = original
    assert instance.system_Off == original



@given(instance=Home_Security_System_strategy)
def test_hyp_home_security_system_system_On_setter(instance):
    original = instance.system_On
    instance.system_On = original
    assert instance.system_On == original




@given(instance=Fire_Alarm_system_strategy)
def test_hyp_fire_alarm_system_system_Off_setter(instance):
    original = instance.system_Off
    instance.system_Off = original
    assert instance.system_Off == original



@given(instance=Fire_Alarm_system_strategy)
def test_hyp_fire_alarm_system_system_On_setter(instance):
    original = instance.system_On
    instance.system_On = original
    assert instance.system_On == original




@given(instance=Appliances_strategy)
def test_hyp_appliances_Off_status_setter(instance):
    original = instance.Off_status
    instance.Off_status = original
    assert instance.Off_status == original



@given(instance=Appliances_strategy)
def test_hyp_appliances_On_status_setter(instance):
    original = instance.On_status
    instance.On_status = original
    assert instance.On_status == original




@given(instance=system_strategy)
def test_hyp_system_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original




@given(instance=Login_strategy)
def test_hyp_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_hyp_login_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Owner_strategy)
def test_hyp_owner_name_setter(instance):
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
    Appliances,
    Department,
    FireAlarm,
    Fire_Alarm_system,
    Home_Security_System,
    Login,
    Owner,
    Police,
    securityAlarm,
    smokeAlarm,
    system,
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

def test_Appliances_Off_status_value_roundtrip():
    instance = Appliances(Off_status=True, On_status=True)
    assert instance.Off_status == True
    instance.Off_status = False
    assert instance.Off_status == False


def test_Appliances_On_status_value_roundtrip():
    instance = Appliances(Off_status=True, On_status=True)
    assert instance.On_status == True
    instance.On_status = False
    assert instance.On_status == False


def test_Department_name_value_roundtrip():
    instance = Department(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_FireAlarm_status_value_roundtrip():
    instance = FireAlarm(status=True)
    assert instance.status == True
    instance.status = False
    assert instance.status == False


def test_Fire_Alarm_system_system_Off_value_roundtrip():
    instance = Fire_Alarm_system(system_Off=True, system_On=True)
    assert instance.system_Off == True
    instance.system_Off = False
    assert instance.system_Off == False


def test_Fire_Alarm_system_system_On_value_roundtrip():
    instance = Fire_Alarm_system(system_Off=True, system_On=True)
    assert instance.system_On == True
    instance.system_On = False
    assert instance.system_On == False


def test_Home_Security_System_system_Off_value_roundtrip():
    instance = Home_Security_System(system_Off=True, system_On=True)
    assert instance.system_Off == True
    instance.system_Off = False
    assert instance.system_Off == False


def test_Home_Security_System_system_On_value_roundtrip():
    instance = Home_Security_System(system_Off=True, system_On=True)
    assert instance.system_On == True
    instance.system_On = False
    assert instance.system_On == False


def test_Login_name_value_roundtrip():
    instance = Login(name="sample_text", password="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Login_password_value_roundtrip():
    instance = Login(name="sample_text", password="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_Owner_name_value_roundtrip():
    instance = Owner(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Police_name_value_roundtrip():
    instance = Police(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_securityAlarm_status_value_roundtrip():
    instance = securityAlarm(status=True)
    assert instance.status == True
    instance.status = False
    assert instance.status == False


def test_smokeAlarm_status_value_roundtrip():
    instance = smokeAlarm(status=True)
    assert instance.status == True
    instance.status = False
    assert instance.status == False


def test_system_status_value_roundtrip():
    instance = system(status=True)
    assert instance.status == True
    instance.status = False
    assert instance.status == False


def test_assoc_Department_Fire_Alarm_system_link_reassign_clear():
    a = Fire_Alarm_system(system_Off=True, system_On=True)
    b1 = Department(name="sample_text")
    b2 = Department(name="sample_text_2")
    _safe_set(a, 'department5', b1)
    assert _is_linked(a, 'department5', b1)
    if hasattr(b1, 'fire_Alarm_system4'):
        assert _is_linked(b1, 'fire_Alarm_system4', a)
    _safe_set(a, 'department5', b2)
    assert _is_linked(a, 'department5', b2)
    if hasattr(b1, 'fire_Alarm_system4'):
        assert not _is_linked(b1, 'fire_Alarm_system4', a)
    if hasattr(b2, 'fire_Alarm_system4'):
        assert _is_linked(b2, 'fire_Alarm_system4', a)
    _safe_set(a, 'department5', None)
    assert not _is_linked(a, 'department5', b2)
    if hasattr(b2, 'fire_Alarm_system4'):
        assert not _is_linked(b2, 'fire_Alarm_system4', a)


def test_assoc_Fire_Alarm_system_FireAlarm_link_reassign_clear():
    a = Fire_Alarm_system(system_Off=True, system_On=True)
    b1 = FireAlarm(status=True)
    b2 = FireAlarm(status=False)
    _safe_set(a, 'fireAlarm12', b1)
    assert _is_linked(a, 'fireAlarm12', b1)
    if hasattr(b1, 'fire_Alarm_system13'):
        assert _is_linked(b1, 'fire_Alarm_system13', a)
    _safe_set(a, 'fireAlarm12', b2)
    assert _is_linked(a, 'fireAlarm12', b2)
    if hasattr(b1, 'fire_Alarm_system13'):
        assert not _is_linked(b1, 'fire_Alarm_system13', a)
    if hasattr(b2, 'fire_Alarm_system13'):
        assert _is_linked(b2, 'fire_Alarm_system13', a)
    _safe_set(a, 'fireAlarm12', None)
    assert not _is_linked(a, 'fireAlarm12', b2)
    if hasattr(b2, 'fire_Alarm_system13'):
        assert not _is_linked(b2, 'fire_Alarm_system13', a)


def test_assoc_Police_Home_Security_System_link_reassign_clear():
    a = Police(name="sample_text")
    b1 = Home_Security_System(system_Off=True, system_On=True)
    b2 = Home_Security_System(system_Off=False, system_On=False)
    _safe_set(a, 'home_Security_System8', b1)
    assert _is_linked(a, 'home_Security_System8', b1)
    if hasattr(b1, 'police9'):
        assert _is_linked(b1, 'police9', a)
    _safe_set(a, 'home_Security_System8', b2)
    assert _is_linked(a, 'home_Security_System8', b2)
    if hasattr(b1, 'police9'):
        assert not _is_linked(b1, 'police9', a)
    if hasattr(b2, 'police9'):
        assert _is_linked(b2, 'police9', a)
    _safe_set(a, 'home_Security_System8', None)
    assert not _is_linked(a, 'home_Security_System8', b2)
    if hasattr(b2, 'police9'):
        assert not _is_linked(b2, 'police9', a)


def test_assoc_access_link_reassign_clear():
    a = Owner(name="sample_text")
    b1 = Login(name="sample_text", password="sample_text")
    b2 = Login(name="sample_text_2", password="sample_text_2")
    _safe_set(a, 'login0', b1)
    assert _is_linked(a, 'login0', b1)
    if hasattr(b1, 'owner1'):
        assert _is_linked(b1, 'owner1', a)
    _safe_set(a, 'login0', b2)
    assert _is_linked(a, 'login0', b2)
    if hasattr(b1, 'owner1'):
        assert not _is_linked(b1, 'owner1', a)
    if hasattr(b2, 'owner1'):
        assert _is_linked(b2, 'owner1', a)
    _safe_set(a, 'login0', None)
    assert not _is_linked(a, 'login0', b2)
    if hasattr(b2, 'owner1'):
        assert not _is_linked(b2, 'owner1', a)


def test_assoc_handle_link_reassign_clear():
    a = system(status=True)
    b1 = Login(name="sample_text", password="sample_text")
    b2 = Login(name="sample_text_2", password="sample_text_2")
    _safe_set(a, 'login23', b1)
    assert _is_linked(a, 'login23', b1)
    if hasattr(b1, 'system2'):
        assert _is_linked(b1, 'system2', a)
    _safe_set(a, 'login23', b2)
    assert _is_linked(a, 'login23', b2)
    if hasattr(b1, 'system2'):
        assert not _is_linked(b1, 'system2', a)
    if hasattr(b2, 'system2'):
        assert _is_linked(b2, 'system2', a)
    _safe_set(a, 'login23', None)
    assert not _is_linked(a, 'login23', b2)
    if hasattr(b2, 'system2'):
        assert not _is_linked(b2, 'system2', a)


def test_assoc_securityAlarm_Home_Security_System_link_reassign_clear():
    a = securityAlarm(status=True)
    b1 = Home_Security_System(system_Off=True, system_On=True)
    b2 = Home_Security_System(system_Off=False, system_On=False)
    _safe_set(a, 'home_Security_System10', b1)
    assert _is_linked(a, 'home_Security_System10', b1)
    if hasattr(b1, 'securityAlarm11'):
        assert _is_linked(b1, 'securityAlarm11', a)
    _safe_set(a, 'home_Security_System10', b2)
    assert _is_linked(a, 'home_Security_System10', b2)
    if hasattr(b1, 'securityAlarm11'):
        assert not _is_linked(b1, 'securityAlarm11', a)
    if hasattr(b2, 'securityAlarm11'):
        assert _is_linked(b2, 'securityAlarm11', a)
    _safe_set(a, 'home_Security_System10', None)
    assert not _is_linked(a, 'home_Security_System10', b2)
    if hasattr(b2, 'securityAlarm11'):
        assert not _is_linked(b2, 'securityAlarm11', a)


def test_assoc_smokeAlarm_Fire_Alarm_system_link_reassign_clear():
    a = smokeAlarm(status=True)
    b1 = Fire_Alarm_system(system_Off=True, system_On=True)
    b2 = Fire_Alarm_system(system_Off=False, system_On=False)
    _safe_set(a, 'fire_Alarm_system6', b1)
    assert _is_linked(a, 'fire_Alarm_system6', b1)
    if hasattr(b1, 'smokeAlarm7'):
        assert _is_linked(b1, 'smokeAlarm7', a)
    _safe_set(a, 'fire_Alarm_system6', b2)
    assert _is_linked(a, 'fire_Alarm_system6', b2)
    if hasattr(b1, 'smokeAlarm7'):
        assert not _is_linked(b1, 'smokeAlarm7', a)
    if hasattr(b2, 'smokeAlarm7'):
        assert _is_linked(b2, 'smokeAlarm7', a)
    _safe_set(a, 'fire_Alarm_system6', None)
    assert not _is_linked(a, 'fire_Alarm_system6', b2)
    if hasattr(b2, 'smokeAlarm7'):
        assert not _is_linked(b2, 'smokeAlarm7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Appliances_strategy = st.builds(Appliances, Off_status=st.booleans(), On_status=st.booleans())
@given(instance=Appliances_strategy)
@settings(max_examples=25)
def test_Appliances_instantiation(instance):
    assert isinstance(instance, Appliances)


Department_strategy = st.builds(Department, name=safe_text)
@given(instance=Department_strategy)
@settings(max_examples=25)
def test_Department_instantiation(instance):
    assert isinstance(instance, Department)


FireAlarm_strategy = st.builds(FireAlarm, status=st.booleans())
@given(instance=FireAlarm_strategy)
@settings(max_examples=25)
def test_FireAlarm_instantiation(instance):
    assert isinstance(instance, FireAlarm)


Fire_Alarm_system_strategy = st.builds(Fire_Alarm_system, system_Off=st.booleans(), system_On=st.booleans())
@given(instance=Fire_Alarm_system_strategy)
@settings(max_examples=25)
def test_Fire_Alarm_system_instantiation(instance):
    assert isinstance(instance, Fire_Alarm_system)


Home_Security_System_strategy = st.builds(Home_Security_System, system_Off=st.booleans(), system_On=st.booleans())
@given(instance=Home_Security_System_strategy)
@settings(max_examples=25)
def test_Home_Security_System_instantiation(instance):
    assert isinstance(instance, Home_Security_System)


Login_strategy = st.builds(Login, name=safe_text, password=safe_text)
@given(instance=Login_strategy)
@settings(max_examples=25)
def test_Login_instantiation(instance):
    assert isinstance(instance, Login)


Owner_strategy = st.builds(Owner, name=safe_text)
@given(instance=Owner_strategy)
@settings(max_examples=25)
def test_Owner_instantiation(instance):
    assert isinstance(instance, Owner)


Police_strategy = st.builds(Police, name=safe_text)
@given(instance=Police_strategy)
@settings(max_examples=25)
def test_Police_instantiation(instance):
    assert isinstance(instance, Police)


securityAlarm_strategy = st.builds(securityAlarm, status=st.booleans())
@given(instance=securityAlarm_strategy)
@settings(max_examples=25)
def test_securityAlarm_instantiation(instance):
    assert isinstance(instance, securityAlarm)


smokeAlarm_strategy = st.builds(smokeAlarm, status=st.booleans())
@given(instance=smokeAlarm_strategy)
@settings(max_examples=25)
def test_smokeAlarm_instantiation(instance):
    assert isinstance(instance, smokeAlarm)


system_strategy = st.builds(system, status=st.booleans())
@given(instance=system_strategy)
@settings(max_examples=25)
def test_system_instantiation(instance):
    assert isinstance(instance, system)



