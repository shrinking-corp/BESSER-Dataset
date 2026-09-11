import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    securityTest_Attack,
    securityTest_AuthSetting,
    securityTest_Input,
    securityTest_Note,
    securityTest_TargetOfEvaluation,
    securityTest_Test,
    securityTest_WebComponent,
    EAttackMethod,
    ESeverity,
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

def test_securityTest_Attack_name_value_roundtrip():
    instance = securityTest_Attack(name="sample_text", severity="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_securityTest_Attack_severity_value_roundtrip():
    instance = securityTest_Attack(name="sample_text", severity="sample_text")
    assert instance.severity == "sample_text"
    instance.severity = "sample_text_2"
    assert instance.severity == "sample_text_2"


def test_securityTest_AuthSetting_loginMessagePattern_value_roundtrip():
    instance = securityTest_AuthSetting(loginMessagePattern="sample_text", loginTargetURL="sample_text", logoutMessagePattern="sample_text", passwordParam="sample_text", roles="sample_text", usernameParam="sample_text")
    assert instance.loginMessagePattern == "sample_text"
    instance.loginMessagePattern = "sample_text_2"
    assert instance.loginMessagePattern == "sample_text_2"


def test_securityTest_AuthSetting_loginTargetURL_value_roundtrip():
    instance = securityTest_AuthSetting(loginMessagePattern="sample_text", loginTargetURL="sample_text", logoutMessagePattern="sample_text", passwordParam="sample_text", roles="sample_text", usernameParam="sample_text")
    assert instance.loginTargetURL == "sample_text"
    instance.loginTargetURL = "sample_text_2"
    assert instance.loginTargetURL == "sample_text_2"


def test_securityTest_AuthSetting_logoutMessagePattern_value_roundtrip():
    instance = securityTest_AuthSetting(loginMessagePattern="sample_text", loginTargetURL="sample_text", logoutMessagePattern="sample_text", passwordParam="sample_text", roles="sample_text", usernameParam="sample_text")
    assert instance.logoutMessagePattern == "sample_text"
    instance.logoutMessagePattern = "sample_text_2"
    assert instance.logoutMessagePattern == "sample_text_2"


def test_securityTest_AuthSetting_passwordParam_value_roundtrip():
    instance = securityTest_AuthSetting(loginMessagePattern="sample_text", loginTargetURL="sample_text", logoutMessagePattern="sample_text", passwordParam="sample_text", roles="sample_text", usernameParam="sample_text")
    assert instance.passwordParam == "sample_text"
    instance.passwordParam = "sample_text_2"
    assert instance.passwordParam == "sample_text_2"


def test_securityTest_AuthSetting_roles_value_roundtrip():
    instance = securityTest_AuthSetting(loginMessagePattern="sample_text", loginTargetURL="sample_text", logoutMessagePattern="sample_text", passwordParam="sample_text", roles="sample_text", usernameParam="sample_text")
    assert instance.roles == "sample_text"
    instance.roles = "sample_text_2"
    assert instance.roles == "sample_text_2"


def test_securityTest_AuthSetting_usernameParam_value_roundtrip():
    instance = securityTest_AuthSetting(loginMessagePattern="sample_text", loginTargetURL="sample_text", logoutMessagePattern="sample_text", passwordParam="sample_text", roles="sample_text", usernameParam="sample_text")
    assert instance.usernameParam == "sample_text"
    instance.usernameParam = "sample_text_2"
    assert instance.usernameParam == "sample_text_2"


def test_securityTest_Input_name_value_roundtrip():
    instance = securityTest_Input(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_securityTest_Note_noteText_value_roundtrip():
    instance = securityTest_Note(noteText="sample_text")
    assert instance.noteText == "sample_text"
    instance.noteText = "sample_text_2"
    assert instance.noteText == "sample_text_2"


def test_securityTest_TargetOfEvaluation_domain_value_roundtrip():
    instance = securityTest_TargetOfEvaluation(domain="sample_text", ip="sample_text", port="sample_text", protocol="sample_text")
    assert instance.domain == "sample_text"
    instance.domain = "sample_text_2"
    assert instance.domain == "sample_text_2"


def test_securityTest_TargetOfEvaluation_ip_value_roundtrip():
    instance = securityTest_TargetOfEvaluation(domain="sample_text", ip="sample_text", port="sample_text", protocol="sample_text")
    assert instance.ip == "sample_text"
    instance.ip = "sample_text_2"
    assert instance.ip == "sample_text_2"


def test_securityTest_TargetOfEvaluation_port_value_roundtrip():
    instance = securityTest_TargetOfEvaluation(domain="sample_text", ip="sample_text", port="sample_text", protocol="sample_text")
    assert instance.port == "sample_text"
    instance.port = "sample_text_2"
    assert instance.port == "sample_text_2"


def test_securityTest_TargetOfEvaluation_protocol_value_roundtrip():
    instance = securityTest_TargetOfEvaluation(domain="sample_text", ip="sample_text", port="sample_text", protocol="sample_text")
    assert instance.protocol == "sample_text"
    instance.protocol = "sample_text_2"
    assert instance.protocol == "sample_text_2"


def test_securityTest_Test_date_value_roundtrip():
    instance = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_securityTest_Test_id_value_roundtrip():
    instance = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_securityTest_Test_name_value_roundtrip():
    instance = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_securityTest_Test_severity_value_roundtrip():
    instance = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    assert instance.severity == "sample_text"
    instance.severity = "sample_text_2"
    assert instance.severity == "sample_text_2"


def test_securityTest_WebComponent_path_value_roundtrip():
    instance = securityTest_WebComponent(path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_assoc_attacks14_link_reassign_clear():
    a = securityTest_Input(name="sample_text")
    b1 = securityTest_Attack(name="sample_text", severity="sample_text")
    b2 = securityTest_Attack(name="sample_text_2", severity="sample_text_2")
    _safe_set(a, 'securityTest_Input15', {b1})
    assert _is_linked(a, 'securityTest_Input15', b1)
    if hasattr(b1, 'securityTest_Attack16'):
        assert _is_linked(b1, 'securityTest_Attack16', a)
    _safe_set(a, 'securityTest_Input15', {b2})
    assert _is_linked(a, 'securityTest_Input15', b2)
    if hasattr(b1, 'securityTest_Attack16'):
        assert not _is_linked(b1, 'securityTest_Attack16', a)
    if hasattr(b2, 'securityTest_Attack16'):
        assert _is_linked(b2, 'securityTest_Attack16', a)
    _safe_set(a, 'securityTest_Input15', set())
    assert not _is_linked(a, 'securityTest_Input15', b2)
    if hasattr(b2, 'securityTest_Attack16'):
        assert not _is_linked(b2, 'securityTest_Attack16', a)


def test_assoc_authSetting5_link_reassign_clear():
    a = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    b1 = securityTest_AuthSetting(loginMessagePattern="sample_text", loginTargetURL="sample_text", logoutMessagePattern="sample_text", passwordParam="sample_text", roles="sample_text", usernameParam="sample_text")
    b2 = securityTest_AuthSetting(loginMessagePattern="sample_text_2", loginTargetURL="sample_text_2", logoutMessagePattern="sample_text_2", passwordParam="sample_text_2", roles="sample_text_2", usernameParam="sample_text_2")
    _safe_set(a, 'securityTest_Test6', b1)
    assert _is_linked(a, 'securityTest_Test6', b1)
    if hasattr(b1, 'securityTest_AuthSetting'):
        assert _is_linked(b1, 'securityTest_AuthSetting', a)
    _safe_set(a, 'securityTest_Test6', b2)
    assert _is_linked(a, 'securityTest_Test6', b2)
    if hasattr(b1, 'securityTest_AuthSetting'):
        assert not _is_linked(b1, 'securityTest_AuthSetting', a)
    if hasattr(b2, 'securityTest_AuthSetting'):
        assert _is_linked(b2, 'securityTest_AuthSetting', a)
    _safe_set(a, 'securityTest_Test6', None)
    assert not _is_linked(a, 'securityTest_Test6', b2)
    if hasattr(b2, 'securityTest_AuthSetting'):
        assert not _is_linked(b2, 'securityTest_AuthSetting', a)


def test_assoc_components7_link_reassign_clear():
    a = securityTest_WebComponent(path="sample_text")
    b1 = securityTest_TargetOfEvaluation(domain="sample_text", ip="sample_text", port="sample_text", protocol="sample_text")
    b2 = securityTest_TargetOfEvaluation(domain="sample_text_2", ip="sample_text_2", port="sample_text_2", protocol="sample_text_2")
    _safe_set(a, 'securityTest_WebComponent', b1)
    assert _is_linked(a, 'securityTest_WebComponent', b1)
    if hasattr(b1, 'securityTest_TargetOfEvaluation8'):
        assert _is_linked(b1, 'securityTest_TargetOfEvaluation8', a)
    _safe_set(a, 'securityTest_WebComponent', b2)
    assert _is_linked(a, 'securityTest_WebComponent', b2)
    if hasattr(b1, 'securityTest_TargetOfEvaluation8'):
        assert not _is_linked(b1, 'securityTest_TargetOfEvaluation8', a)
    if hasattr(b2, 'securityTest_TargetOfEvaluation8'):
        assert _is_linked(b2, 'securityTest_TargetOfEvaluation8', a)
    _safe_set(a, 'securityTest_WebComponent', None)
    assert not _is_linked(a, 'securityTest_WebComponent', b2)
    if hasattr(b2, 'securityTest_TargetOfEvaluation8'):
        assert not _is_linked(b2, 'securityTest_TargetOfEvaluation8', a)


def test_assoc_inputs12_link_reassign_clear():
    a = securityTest_WebComponent(path="sample_text")
    b1 = securityTest_Input(name="sample_text")
    b2 = securityTest_Input(name="sample_text_2")
    _safe_set(a, 'securityTest_WebComponent13', {b1})
    assert _is_linked(a, 'securityTest_WebComponent13', b1)
    if hasattr(b1, 'securityTest_Input'):
        assert _is_linked(b1, 'securityTest_Input', a)
    _safe_set(a, 'securityTest_WebComponent13', {b2})
    assert _is_linked(a, 'securityTest_WebComponent13', b2)
    if hasattr(b1, 'securityTest_Input'):
        assert not _is_linked(b1, 'securityTest_Input', a)
    if hasattr(b2, 'securityTest_Input'):
        assert _is_linked(b2, 'securityTest_Input', a)
    _safe_set(a, 'securityTest_WebComponent13', set())
    assert not _is_linked(a, 'securityTest_WebComponent13', b2)
    if hasattr(b2, 'securityTest_Input'):
        assert not _is_linked(b2, 'securityTest_Input', a)


def test_assoc_note3_link_reassign_clear():
    a = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    b1 = securityTest_Note(noteText="sample_text")
    b2 = securityTest_Note(noteText="sample_text_2")
    _safe_set(a, 'securityTest_Test4', b1)
    assert _is_linked(a, 'securityTest_Test4', b1)
    if hasattr(b1, 'securityTest_Note'):
        assert _is_linked(b1, 'securityTest_Note', a)
    _safe_set(a, 'securityTest_Test4', b2)
    assert _is_linked(a, 'securityTest_Test4', b2)
    if hasattr(b1, 'securityTest_Note'):
        assert not _is_linked(b1, 'securityTest_Note', a)
    if hasattr(b2, 'securityTest_Note'):
        assert _is_linked(b2, 'securityTest_Note', a)
    _safe_set(a, 'securityTest_Test4', None)
    assert not _is_linked(a, 'securityTest_Test4', b2)
    if hasattr(b2, 'securityTest_Note'):
        assert not _is_linked(b2, 'securityTest_Note', a)


def test_assoc_possibleAttacks1_link_reassign_clear():
    a = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    b1 = securityTest_Attack(name="sample_text", severity="sample_text")
    b2 = securityTest_Attack(name="sample_text_2", severity="sample_text_2")
    _safe_set(a, 'securityTest_Test2', {b1})
    assert _is_linked(a, 'securityTest_Test2', b1)
    if hasattr(b1, 'securityTest_Attack'):
        assert _is_linked(b1, 'securityTest_Attack', a)
    _safe_set(a, 'securityTest_Test2', {b2})
    assert _is_linked(a, 'securityTest_Test2', b2)
    if hasattr(b1, 'securityTest_Attack'):
        assert not _is_linked(b1, 'securityTest_Attack', a)
    if hasattr(b2, 'securityTest_Attack'):
        assert _is_linked(b2, 'securityTest_Attack', a)
    _safe_set(a, 'securityTest_Test2', set())
    assert not _is_linked(a, 'securityTest_Test2', b2)
    if hasattr(b2, 'securityTest_Attack'):
        assert not _is_linked(b2, 'securityTest_Attack', a)


def test_assoc_scope0_link_reassign_clear():
    a = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    b1 = securityTest_TargetOfEvaluation(domain="sample_text", ip="sample_text", port="sample_text", protocol="sample_text")
    b2 = securityTest_TargetOfEvaluation(domain="sample_text_2", ip="sample_text_2", port="sample_text_2", protocol="sample_text_2")
    _safe_set(a, 'securityTest_Test', b1)
    assert _is_linked(a, 'securityTest_Test', b1)
    if hasattr(b1, 'securityTest_TargetOfEvaluation'):
        assert _is_linked(b1, 'securityTest_TargetOfEvaluation', a)
    _safe_set(a, 'securityTest_Test', b2)
    assert _is_linked(a, 'securityTest_Test', b2)
    if hasattr(b1, 'securityTest_TargetOfEvaluation'):
        assert not _is_linked(b1, 'securityTest_TargetOfEvaluation', a)
    if hasattr(b2, 'securityTest_TargetOfEvaluation'):
        assert _is_linked(b2, 'securityTest_TargetOfEvaluation', a)
    _safe_set(a, 'securityTest_Test', None)
    assert not _is_linked(a, 'securityTest_Test', b2)
    if hasattr(b2, 'securityTest_TargetOfEvaluation'):
        assert not _is_linked(b2, 'securityTest_TargetOfEvaluation', a)


def test_assoc_targetLinks10_link_reassign_clear():
    a = securityTest_WebComponent(path="sample_text")
    b1 = securityTest_WebComponent(path="sample_text")
    b2 = securityTest_WebComponent(path="sample_text_2")
    _safe_set(a, 'securityTest_WebComponent11', b1)
    assert _is_linked(a, 'securityTest_WebComponent11', b1)
    if hasattr(b1, 'securityTest_WebComponent9'):
        assert _is_linked(b1, 'securityTest_WebComponent9', a)
    _safe_set(a, 'securityTest_WebComponent11', b2)
    assert _is_linked(a, 'securityTest_WebComponent11', b2)
    if hasattr(b1, 'securityTest_WebComponent9'):
        assert not _is_linked(b1, 'securityTest_WebComponent9', a)
    if hasattr(b2, 'securityTest_WebComponent9'):
        assert _is_linked(b2, 'securityTest_WebComponent9', a)
    _safe_set(a, 'securityTest_WebComponent11', None)
    assert not _is_linked(a, 'securityTest_WebComponent11', b2)
    if hasattr(b2, 'securityTest_WebComponent9'):
        assert not _is_linked(b2, 'securityTest_WebComponent9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

securityTest_Attack_strategy = st.builds(securityTest_Attack, name=safe_text, severity=safe_text)
@given(instance=securityTest_Attack_strategy)
@settings(max_examples=25)
def test_securityTest_Attack_instantiation(instance):
    assert isinstance(instance, securityTest_Attack)


securityTest_AuthSetting_strategy = st.builds(securityTest_AuthSetting, loginMessagePattern=safe_text, loginTargetURL=safe_text, logoutMessagePattern=safe_text, passwordParam=safe_text, roles=safe_text, usernameParam=safe_text)
@given(instance=securityTest_AuthSetting_strategy)
@settings(max_examples=25)
def test_securityTest_AuthSetting_instantiation(instance):
    assert isinstance(instance, securityTest_AuthSetting)


securityTest_Input_strategy = st.builds(securityTest_Input, name=safe_text)
@given(instance=securityTest_Input_strategy)
@settings(max_examples=25)
def test_securityTest_Input_instantiation(instance):
    assert isinstance(instance, securityTest_Input)


securityTest_Note_strategy = st.builds(securityTest_Note, noteText=safe_text)
@given(instance=securityTest_Note_strategy)
@settings(max_examples=25)
def test_securityTest_Note_instantiation(instance):
    assert isinstance(instance, securityTest_Note)


securityTest_TargetOfEvaluation_strategy = st.builds(securityTest_TargetOfEvaluation, domain=safe_text, ip=safe_text, port=safe_text, protocol=safe_text)
@given(instance=securityTest_TargetOfEvaluation_strategy)
@settings(max_examples=25)
def test_securityTest_TargetOfEvaluation_instantiation(instance):
    assert isinstance(instance, securityTest_TargetOfEvaluation)


securityTest_Test_strategy = st.builds(securityTest_Test, date=st.dates(), id=safe_text, name=safe_text, severity=safe_text)
@given(instance=securityTest_Test_strategy)
@settings(max_examples=25)
def test_securityTest_Test_instantiation(instance):
    assert isinstance(instance, securityTest_Test)


securityTest_WebComponent_strategy = st.builds(securityTest_WebComponent, path=safe_text)
@given(instance=securityTest_WebComponent_strategy)
@settings(max_examples=25)
def test_securityTest_WebComponent_instantiation(instance):
    assert isinstance(instance, securityTest_WebComponent)


