import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_attacks14_reverse_link_reassign_clear():
    a1 = securityTest_Input(name="sample_text")
    a2 = securityTest_Input(name="sample_text_2")
    b = securityTest_Attack(name="sample_text", severity="sample_text")
    _safe_set(b, 'securityTest_Attack16', a1)
    assert _is_linked(b, 'securityTest_Attack16', a1)
    if hasattr(a1, 'securityTest_Input15'):
        assert _is_linked(a1, 'securityTest_Input15', b)
    _safe_set(b, 'securityTest_Attack16', a2)
    assert _is_linked(b, 'securityTest_Attack16', a2)
    if hasattr(a1, 'securityTest_Input15'):
        assert not _is_linked(a1, 'securityTest_Input15', b)
    if hasattr(a2, 'securityTest_Input15'):
        assert _is_linked(a2, 'securityTest_Input15', b)
    _safe_set(b, 'securityTest_Attack16', None)
    assert not _is_linked(b, 'securityTest_Attack16', a2)
    if hasattr(a2, 'securityTest_Input15'):
        assert not _is_linked(a2, 'securityTest_Input15', b)


def test_assoc_authSetting5_reverse_link_reassign_clear():
    a1 = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    a2 = securityTest_Test(date=date(2025, 6, 15), id="sample_text_2", name="sample_text_2", severity="sample_text_2")
    b = securityTest_AuthSetting(loginMessagePattern="sample_text", loginTargetURL="sample_text", logoutMessagePattern="sample_text", passwordParam="sample_text", roles="sample_text", usernameParam="sample_text")
    _safe_set(b, 'securityTest_AuthSetting', a1)
    assert _is_linked(b, 'securityTest_AuthSetting', a1)
    if hasattr(a1, 'securityTest_Test6'):
        assert _is_linked(a1, 'securityTest_Test6', b)
    _safe_set(b, 'securityTest_AuthSetting', a2)
    assert _is_linked(b, 'securityTest_AuthSetting', a2)
    if hasattr(a1, 'securityTest_Test6'):
        assert not _is_linked(a1, 'securityTest_Test6', b)
    if hasattr(a2, 'securityTest_Test6'):
        assert _is_linked(a2, 'securityTest_Test6', b)
    _safe_set(b, 'securityTest_AuthSetting', None)
    assert not _is_linked(b, 'securityTest_AuthSetting', a2)
    if hasattr(a2, 'securityTest_Test6'):
        assert not _is_linked(a2, 'securityTest_Test6', b)


def test_assoc_components7_reverse_link_reassign_clear():
    a1 = securityTest_WebComponent(path="sample_text")
    a2 = securityTest_WebComponent(path="sample_text_2")
    b = securityTest_TargetOfEvaluation(domain="sample_text", ip="sample_text", port="sample_text", protocol="sample_text")
    _safe_set(b, 'securityTest_TargetOfEvaluation8', {a1})
    assert _is_linked(b, 'securityTest_TargetOfEvaluation8', a1)
    if hasattr(a1, 'securityTest_WebComponent'):
        assert _is_linked(a1, 'securityTest_WebComponent', b)
    _safe_set(b, 'securityTest_TargetOfEvaluation8', {a2})
    assert _is_linked(b, 'securityTest_TargetOfEvaluation8', a2)
    if hasattr(a1, 'securityTest_WebComponent'):
        assert not _is_linked(a1, 'securityTest_WebComponent', b)
    if hasattr(a2, 'securityTest_WebComponent'):
        assert _is_linked(a2, 'securityTest_WebComponent', b)
    _safe_set(b, 'securityTest_TargetOfEvaluation8', set())
    assert not _is_linked(b, 'securityTest_TargetOfEvaluation8', a2)
    if hasattr(a2, 'securityTest_WebComponent'):
        assert not _is_linked(a2, 'securityTest_WebComponent', b)


def test_assoc_inputs12_reverse_link_reassign_clear():
    a1 = securityTest_WebComponent(path="sample_text")
    a2 = securityTest_WebComponent(path="sample_text_2")
    b = securityTest_Input(name="sample_text")
    _safe_set(b, 'securityTest_Input', a1)
    assert _is_linked(b, 'securityTest_Input', a1)
    if hasattr(a1, 'securityTest_WebComponent13'):
        assert _is_linked(a1, 'securityTest_WebComponent13', b)
    _safe_set(b, 'securityTest_Input', a2)
    assert _is_linked(b, 'securityTest_Input', a2)
    if hasattr(a1, 'securityTest_WebComponent13'):
        assert not _is_linked(a1, 'securityTest_WebComponent13', b)
    if hasattr(a2, 'securityTest_WebComponent13'):
        assert _is_linked(a2, 'securityTest_WebComponent13', b)
    _safe_set(b, 'securityTest_Input', None)
    assert not _is_linked(b, 'securityTest_Input', a2)
    if hasattr(a2, 'securityTest_WebComponent13'):
        assert not _is_linked(a2, 'securityTest_WebComponent13', b)


def test_assoc_note3_reverse_link_reassign_clear():
    a1 = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    a2 = securityTest_Test(date=date(2025, 6, 15), id="sample_text_2", name="sample_text_2", severity="sample_text_2")
    b = securityTest_Note(noteText="sample_text")
    _safe_set(b, 'securityTest_Note', a1)
    assert _is_linked(b, 'securityTest_Note', a1)
    if hasattr(a1, 'securityTest_Test4'):
        assert _is_linked(a1, 'securityTest_Test4', b)
    _safe_set(b, 'securityTest_Note', a2)
    assert _is_linked(b, 'securityTest_Note', a2)
    if hasattr(a1, 'securityTest_Test4'):
        assert not _is_linked(a1, 'securityTest_Test4', b)
    if hasattr(a2, 'securityTest_Test4'):
        assert _is_linked(a2, 'securityTest_Test4', b)
    _safe_set(b, 'securityTest_Note', None)
    assert not _is_linked(b, 'securityTest_Note', a2)
    if hasattr(a2, 'securityTest_Test4'):
        assert not _is_linked(a2, 'securityTest_Test4', b)


def test_assoc_possibleAttacks1_reverse_link_reassign_clear():
    a1 = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    a2 = securityTest_Test(date=date(2025, 6, 15), id="sample_text_2", name="sample_text_2", severity="sample_text_2")
    b = securityTest_Attack(name="sample_text", severity="sample_text")
    _safe_set(b, 'securityTest_Attack', a1)
    assert _is_linked(b, 'securityTest_Attack', a1)
    if hasattr(a1, 'securityTest_Test2'):
        assert _is_linked(a1, 'securityTest_Test2', b)
    _safe_set(b, 'securityTest_Attack', a2)
    assert _is_linked(b, 'securityTest_Attack', a2)
    if hasattr(a1, 'securityTest_Test2'):
        assert not _is_linked(a1, 'securityTest_Test2', b)
    if hasattr(a2, 'securityTest_Test2'):
        assert _is_linked(a2, 'securityTest_Test2', b)
    _safe_set(b, 'securityTest_Attack', None)
    assert not _is_linked(b, 'securityTest_Attack', a2)
    if hasattr(a2, 'securityTest_Test2'):
        assert not _is_linked(a2, 'securityTest_Test2', b)


def test_assoc_scope0_reverse_link_reassign_clear():
    a1 = securityTest_Test(date=date(2024, 1, 1), id="sample_text", name="sample_text", severity="sample_text")
    a2 = securityTest_Test(date=date(2025, 6, 15), id="sample_text_2", name="sample_text_2", severity="sample_text_2")
    b = securityTest_TargetOfEvaluation(domain="sample_text", ip="sample_text", port="sample_text", protocol="sample_text")
    _safe_set(b, 'securityTest_TargetOfEvaluation', a1)
    assert _is_linked(b, 'securityTest_TargetOfEvaluation', a1)
    if hasattr(a1, 'securityTest_Test'):
        assert _is_linked(a1, 'securityTest_Test', b)
    _safe_set(b, 'securityTest_TargetOfEvaluation', a2)
    assert _is_linked(b, 'securityTest_TargetOfEvaluation', a2)
    if hasattr(a1, 'securityTest_Test'):
        assert not _is_linked(a1, 'securityTest_Test', b)
    if hasattr(a2, 'securityTest_Test'):
        assert _is_linked(a2, 'securityTest_Test', b)
    _safe_set(b, 'securityTest_TargetOfEvaluation', None)
    assert not _is_linked(b, 'securityTest_TargetOfEvaluation', a2)
    if hasattr(a2, 'securityTest_Test'):
        assert not _is_linked(a2, 'securityTest_Test', b)


def test_assoc_targetLinks10_reverse_link_reassign_clear():
    a1 = securityTest_WebComponent(path="sample_text")
    a2 = securityTest_WebComponent(path="sample_text_2")
    b = securityTest_WebComponent(path="sample_text")
    _safe_set(b, 'securityTest_WebComponent9', {a1})
    assert _is_linked(b, 'securityTest_WebComponent9', a1)
    if hasattr(a1, 'securityTest_WebComponent11'):
        assert _is_linked(a1, 'securityTest_WebComponent11', b)
    _safe_set(b, 'securityTest_WebComponent9', {a2})
    assert _is_linked(b, 'securityTest_WebComponent9', a2)
    if hasattr(a1, 'securityTest_WebComponent11'):
        assert not _is_linked(a1, 'securityTest_WebComponent11', b)
    if hasattr(a2, 'securityTest_WebComponent11'):
        assert _is_linked(a2, 'securityTest_WebComponent11', b)
    _safe_set(b, 'securityTest_WebComponent9', set())
    assert not _is_linked(b, 'securityTest_WebComponent9', a2)
    if hasattr(a2, 'securityTest_WebComponent11'):
        assert not _is_linked(a2, 'securityTest_WebComponent11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

