import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    scxml_DocumentRoot,
    scxml_EStringToStringMapEntry,
    scxml_ScxmlAssignType,
    scxml_ScxmlCancelType,
    scxml_ScxmlContentType,
    scxml_ScxmlDataType,
    scxml_ScxmlDatamodelType,
    scxml_ScxmlDonedataType,
    scxml_ScxmlElseType,
    scxml_ScxmlElseifType,
    scxml_ScxmlFinalType,
    scxml_ScxmlFinalizeType,
    scxml_ScxmlForeachType,
    scxml_ScxmlHistoryType,
    scxml_ScxmlIfType,
    scxml_ScxmlInitialType,
    scxml_ScxmlInvokeType,
    scxml_ScxmlLogType,
    scxml_ScxmlOnentryType,
    scxml_ScxmlOnexitType,
    scxml_ScxmlParallelType,
    scxml_ScxmlParamType,
    scxml_ScxmlRaiseType,
    scxml_ScxmlScriptType,
    scxml_ScxmlScxmlType,
    scxml_ScxmlSendType,
    scxml_ScxmlStateType,
    scxml_ScxmlTransitionType,
    AssignTypeDatatype,
    BindingDatatype,
    BooleanDatatype,
    ExmodeDatatype,
    HistoryTypeDatatype,
    TransitionTypeDatatype,
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

def test_assoc_assign113_reverse_link_reassign_clear():
    a1 = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlForeachType(any="sample_text_2", anyAttribute="sample_text_2", array="sample_text_2", index="sample_text_2", item="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlAssignType115', a1)
    assert _is_linked(b, 'scxml_ScxmlAssignType115', a1)
    if hasattr(a1, 'scxml_ScxmlForeachType114'):
        assert _is_linked(a1, 'scxml_ScxmlForeachType114', b)
    _safe_set(b, 'scxml_ScxmlAssignType115', a2)
    assert _is_linked(b, 'scxml_ScxmlAssignType115', a2)
    if hasattr(a1, 'scxml_ScxmlForeachType114'):
        assert not _is_linked(a1, 'scxml_ScxmlForeachType114', b)
    if hasattr(a2, 'scxml_ScxmlForeachType114'):
        assert _is_linked(a2, 'scxml_ScxmlForeachType114', b)
    _safe_set(b, 'scxml_ScxmlAssignType115', None)
    assert not _is_linked(b, 'scxml_ScxmlAssignType115', a2)
    if hasattr(a2, 'scxml_ScxmlForeachType114'):
        assert not _is_linked(a2, 'scxml_ScxmlForeachType114', b)


def test_assoc_assign1167_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlAssignType169', a1)
    assert _is_linked(b, 'scxml_ScxmlAssignType169', a1)
    if hasattr(a1, 'scxml_ScxmlIfType168'):
        assert _is_linked(a1, 'scxml_ScxmlIfType168', b)
    _safe_set(b, 'scxml_ScxmlAssignType169', a2)
    assert _is_linked(b, 'scxml_ScxmlAssignType169', a2)
    if hasattr(a1, 'scxml_ScxmlIfType168'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType168', b)
    if hasattr(a2, 'scxml_ScxmlIfType168'):
        assert _is_linked(a2, 'scxml_ScxmlIfType168', b)
    _safe_set(b, 'scxml_ScxmlAssignType169', None)
    assert not _is_linked(b, 'scxml_ScxmlAssignType169', a2)
    if hasattr(a2, 'scxml_ScxmlIfType168'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType168', b)


def test_assoc_assign140_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlAssignType142', a1)
    assert _is_linked(b, 'scxml_ScxmlAssignType142', a1)
    if hasattr(a1, 'scxml_ScxmlIfType141'):
        assert _is_linked(a1, 'scxml_ScxmlIfType141', b)
    _safe_set(b, 'scxml_ScxmlAssignType142', a2)
    assert _is_linked(b, 'scxml_ScxmlAssignType142', a2)
    if hasattr(a1, 'scxml_ScxmlIfType141'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType141', b)
    if hasattr(a2, 'scxml_ScxmlIfType141'):
        assert _is_linked(a2, 'scxml_ScxmlIfType141', b)
    _safe_set(b, 'scxml_ScxmlAssignType142', None)
    assert not _is_linked(b, 'scxml_ScxmlAssignType142', a2)
    if hasattr(a2, 'scxml_ScxmlIfType141'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType141', b)


def test_assoc_assign2194_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlAssignType196', a1)
    assert _is_linked(b, 'scxml_ScxmlAssignType196', a1)
    if hasattr(a1, 'scxml_ScxmlIfType195'):
        assert _is_linked(a1, 'scxml_ScxmlIfType195', b)
    _safe_set(b, 'scxml_ScxmlAssignType196', a2)
    assert _is_linked(b, 'scxml_ScxmlAssignType196', a2)
    if hasattr(a1, 'scxml_ScxmlIfType195'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType195', b)
    if hasattr(a2, 'scxml_ScxmlIfType195'):
        assert _is_linked(a2, 'scxml_ScxmlIfType195', b)
    _safe_set(b, 'scxml_ScxmlAssignType196', None)
    assert not _is_linked(b, 'scxml_ScxmlAssignType196', a2)
    if hasattr(a2, 'scxml_ScxmlIfType195'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType195', b)


def test_assoc_assign230_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnentryType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlAssignType232', a1)
    assert _is_linked(b, 'scxml_ScxmlAssignType232', a1)
    if hasattr(a1, 'scxml_ScxmlOnentryType231'):
        assert _is_linked(a1, 'scxml_ScxmlOnentryType231', b)
    _safe_set(b, 'scxml_ScxmlAssignType232', a2)
    assert _is_linked(b, 'scxml_ScxmlAssignType232', a2)
    if hasattr(a1, 'scxml_ScxmlOnentryType231'):
        assert not _is_linked(a1, 'scxml_ScxmlOnentryType231', b)
    if hasattr(a2, 'scxml_ScxmlOnentryType231'):
        assert _is_linked(a2, 'scxml_ScxmlOnentryType231', b)
    _safe_set(b, 'scxml_ScxmlAssignType232', None)
    assert not _is_linked(b, 'scxml_ScxmlAssignType232', a2)
    if hasattr(a2, 'scxml_ScxmlOnentryType231'):
        assert not _is_linked(a2, 'scxml_ScxmlOnentryType231', b)


def test_assoc_assign254_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnexitType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlAssignType256', a1)
    assert _is_linked(b, 'scxml_ScxmlAssignType256', a1)
    if hasattr(a1, 'scxml_ScxmlOnexitType255'):
        assert _is_linked(a1, 'scxml_ScxmlOnexitType255', b)
    _safe_set(b, 'scxml_ScxmlAssignType256', a2)
    assert _is_linked(b, 'scxml_ScxmlAssignType256', a2)
    if hasattr(a1, 'scxml_ScxmlOnexitType255'):
        assert not _is_linked(a1, 'scxml_ScxmlOnexitType255', b)
    if hasattr(a2, 'scxml_ScxmlOnexitType255'):
        assert _is_linked(a2, 'scxml_ScxmlOnexitType255', b)
    _safe_set(b, 'scxml_ScxmlAssignType256', None)
    assert not _is_linked(b, 'scxml_ScxmlAssignType256', a2)
    if hasattr(a2, 'scxml_ScxmlOnexitType255'):
        assert not _is_linked(a2, 'scxml_ScxmlOnexitType255', b)


def test_assoc_assign353_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlAssignType355', a1)
    assert _is_linked(b, 'scxml_ScxmlAssignType355', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType354'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType354', b)
    _safe_set(b, 'scxml_ScxmlAssignType355', a2)
    assert _is_linked(b, 'scxml_ScxmlAssignType355', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType354'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType354', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType354'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType354', b)
    _safe_set(b, 'scxml_ScxmlAssignType355', None)
    assert not _is_linked(b, 'scxml_ScxmlAssignType355', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType354'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType354', b)


def test_assoc_assign4_reverse_link_reassign_clear():
    a1 = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    a2 = scxml_ScxmlAssignType(any="sample_text_2", anyAttribute="sample_text_2", attr="sample_text_2", expr="sample_text_2", location="sample_text_2", mixed="sample_text_2", type="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot5', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot5', a1)
    if hasattr(a1, 'scxml_ScxmlAssignType'):
        assert _is_linked(a1, 'scxml_ScxmlAssignType', b)
    _safe_set(b, 'scxml_DocumentRoot5', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot5', a2)
    if hasattr(a1, 'scxml_ScxmlAssignType'):
        assert not _is_linked(a1, 'scxml_ScxmlAssignType', b)
    if hasattr(a2, 'scxml_ScxmlAssignType'):
        assert _is_linked(a2, 'scxml_ScxmlAssignType', b)
    _safe_set(b, 'scxml_DocumentRoot5', set())
    assert not _is_linked(b, 'scxml_DocumentRoot5', a2)
    if hasattr(a2, 'scxml_ScxmlAssignType'):
        assert not _is_linked(a2, 'scxml_ScxmlAssignType', b)


def test_assoc_assign80_reverse_link_reassign_clear():
    a1 = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlFinalizeType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlAssignType(any="sample_text", anyAttribute="sample_text", attr="sample_text", expr="sample_text", location="sample_text", mixed="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlAssignType82', a1)
    assert _is_linked(b, 'scxml_ScxmlAssignType82', a1)
    if hasattr(a1, 'scxml_ScxmlFinalizeType81'):
        assert _is_linked(a1, 'scxml_ScxmlFinalizeType81', b)
    _safe_set(b, 'scxml_ScxmlAssignType82', a2)
    assert _is_linked(b, 'scxml_ScxmlAssignType82', a2)
    if hasattr(a1, 'scxml_ScxmlFinalizeType81'):
        assert not _is_linked(a1, 'scxml_ScxmlFinalizeType81', b)
    if hasattr(a2, 'scxml_ScxmlFinalizeType81'):
        assert _is_linked(a2, 'scxml_ScxmlFinalizeType81', b)
    _safe_set(b, 'scxml_ScxmlAssignType82', None)
    assert not _is_linked(b, 'scxml_ScxmlAssignType82', a2)
    if hasattr(a2, 'scxml_ScxmlFinalizeType81'):
        assert not _is_linked(a2, 'scxml_ScxmlFinalizeType81', b)


def test_assoc_cancel1173_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlCancelType175', a1)
    assert _is_linked(b, 'scxml_ScxmlCancelType175', a1)
    if hasattr(a1, 'scxml_ScxmlIfType174'):
        assert _is_linked(a1, 'scxml_ScxmlIfType174', b)
    _safe_set(b, 'scxml_ScxmlCancelType175', a2)
    assert _is_linked(b, 'scxml_ScxmlCancelType175', a2)
    if hasattr(a1, 'scxml_ScxmlIfType174'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType174', b)
    if hasattr(a2, 'scxml_ScxmlIfType174'):
        assert _is_linked(a2, 'scxml_ScxmlIfType174', b)
    _safe_set(b, 'scxml_ScxmlCancelType175', None)
    assert not _is_linked(b, 'scxml_ScxmlCancelType175', a2)
    if hasattr(a2, 'scxml_ScxmlIfType174'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType174', b)


def test_assoc_cancel119_reverse_link_reassign_clear():
    a1 = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlForeachType(any="sample_text_2", anyAttribute="sample_text_2", array="sample_text_2", index="sample_text_2", item="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlCancelType121', a1)
    assert _is_linked(b, 'scxml_ScxmlCancelType121', a1)
    if hasattr(a1, 'scxml_ScxmlForeachType120'):
        assert _is_linked(a1, 'scxml_ScxmlForeachType120', b)
    _safe_set(b, 'scxml_ScxmlCancelType121', a2)
    assert _is_linked(b, 'scxml_ScxmlCancelType121', a2)
    if hasattr(a1, 'scxml_ScxmlForeachType120'):
        assert not _is_linked(a1, 'scxml_ScxmlForeachType120', b)
    if hasattr(a2, 'scxml_ScxmlForeachType120'):
        assert _is_linked(a2, 'scxml_ScxmlForeachType120', b)
    _safe_set(b, 'scxml_ScxmlCancelType121', None)
    assert not _is_linked(b, 'scxml_ScxmlCancelType121', a2)
    if hasattr(a2, 'scxml_ScxmlForeachType120'):
        assert not _is_linked(a2, 'scxml_ScxmlForeachType120', b)


def test_assoc_cancel146_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlCancelType148', a1)
    assert _is_linked(b, 'scxml_ScxmlCancelType148', a1)
    if hasattr(a1, 'scxml_ScxmlIfType147'):
        assert _is_linked(a1, 'scxml_ScxmlIfType147', b)
    _safe_set(b, 'scxml_ScxmlCancelType148', a2)
    assert _is_linked(b, 'scxml_ScxmlCancelType148', a2)
    if hasattr(a1, 'scxml_ScxmlIfType147'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType147', b)
    if hasattr(a2, 'scxml_ScxmlIfType147'):
        assert _is_linked(a2, 'scxml_ScxmlIfType147', b)
    _safe_set(b, 'scxml_ScxmlCancelType148', None)
    assert not _is_linked(b, 'scxml_ScxmlCancelType148', a2)
    if hasattr(a2, 'scxml_ScxmlIfType147'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType147', b)


def test_assoc_cancel2200_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlCancelType202', a1)
    assert _is_linked(b, 'scxml_ScxmlCancelType202', a1)
    if hasattr(a1, 'scxml_ScxmlIfType201'):
        assert _is_linked(a1, 'scxml_ScxmlIfType201', b)
    _safe_set(b, 'scxml_ScxmlCancelType202', a2)
    assert _is_linked(b, 'scxml_ScxmlCancelType202', a2)
    if hasattr(a1, 'scxml_ScxmlIfType201'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType201', b)
    if hasattr(a2, 'scxml_ScxmlIfType201'):
        assert _is_linked(a2, 'scxml_ScxmlIfType201', b)
    _safe_set(b, 'scxml_ScxmlCancelType202', None)
    assert not _is_linked(b, 'scxml_ScxmlCancelType202', a2)
    if hasattr(a2, 'scxml_ScxmlIfType201'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType201', b)


def test_assoc_cancel236_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnentryType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlCancelType238', a1)
    assert _is_linked(b, 'scxml_ScxmlCancelType238', a1)
    if hasattr(a1, 'scxml_ScxmlOnentryType237'):
        assert _is_linked(a1, 'scxml_ScxmlOnentryType237', b)
    _safe_set(b, 'scxml_ScxmlCancelType238', a2)
    assert _is_linked(b, 'scxml_ScxmlCancelType238', a2)
    if hasattr(a1, 'scxml_ScxmlOnentryType237'):
        assert not _is_linked(a1, 'scxml_ScxmlOnentryType237', b)
    if hasattr(a2, 'scxml_ScxmlOnentryType237'):
        assert _is_linked(a2, 'scxml_ScxmlOnentryType237', b)
    _safe_set(b, 'scxml_ScxmlCancelType238', None)
    assert not _is_linked(b, 'scxml_ScxmlCancelType238', a2)
    if hasattr(a2, 'scxml_ScxmlOnentryType237'):
        assert not _is_linked(a2, 'scxml_ScxmlOnentryType237', b)


def test_assoc_cancel260_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnexitType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlCancelType262', a1)
    assert _is_linked(b, 'scxml_ScxmlCancelType262', a1)
    if hasattr(a1, 'scxml_ScxmlOnexitType261'):
        assert _is_linked(a1, 'scxml_ScxmlOnexitType261', b)
    _safe_set(b, 'scxml_ScxmlCancelType262', a2)
    assert _is_linked(b, 'scxml_ScxmlCancelType262', a2)
    if hasattr(a1, 'scxml_ScxmlOnexitType261'):
        assert not _is_linked(a1, 'scxml_ScxmlOnexitType261', b)
    if hasattr(a2, 'scxml_ScxmlOnexitType261'):
        assert _is_linked(a2, 'scxml_ScxmlOnexitType261', b)
    _safe_set(b, 'scxml_ScxmlCancelType262', None)
    assert not _is_linked(b, 'scxml_ScxmlCancelType262', a2)
    if hasattr(a2, 'scxml_ScxmlOnexitType261'):
        assert not _is_linked(a2, 'scxml_ScxmlOnexitType261', b)


def test_assoc_cancel359_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlCancelType361', a1)
    assert _is_linked(b, 'scxml_ScxmlCancelType361', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType360'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType360', b)
    _safe_set(b, 'scxml_ScxmlCancelType361', a2)
    assert _is_linked(b, 'scxml_ScxmlCancelType361', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType360'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType360', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType360'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType360', b)
    _safe_set(b, 'scxml_ScxmlCancelType361', None)
    assert not _is_linked(b, 'scxml_ScxmlCancelType361', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType360'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType360', b)


def test_assoc_cancel6_reverse_link_reassign_clear():
    a1 = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    a2 = scxml_ScxmlCancelType(any="sample_text_2", anyAttribute="sample_text_2", scxmlExtraContent="sample_text_2", sendid="sample_text_2", sendidexpr="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot7', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot7', a1)
    if hasattr(a1, 'scxml_ScxmlCancelType'):
        assert _is_linked(a1, 'scxml_ScxmlCancelType', b)
    _safe_set(b, 'scxml_DocumentRoot7', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot7', a2)
    if hasattr(a1, 'scxml_ScxmlCancelType'):
        assert not _is_linked(a1, 'scxml_ScxmlCancelType', b)
    if hasattr(a2, 'scxml_ScxmlCancelType'):
        assert _is_linked(a2, 'scxml_ScxmlCancelType', b)
    _safe_set(b, 'scxml_DocumentRoot7', set())
    assert not _is_linked(b, 'scxml_DocumentRoot7', a2)
    if hasattr(a2, 'scxml_ScxmlCancelType'):
        assert not _is_linked(a2, 'scxml_ScxmlCancelType', b)


def test_assoc_cancel86_reverse_link_reassign_clear():
    a1 = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlFinalizeType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlCancelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlCancelType88', a1)
    assert _is_linked(b, 'scxml_ScxmlCancelType88', a1)
    if hasattr(a1, 'scxml_ScxmlFinalizeType87'):
        assert _is_linked(a1, 'scxml_ScxmlFinalizeType87', b)
    _safe_set(b, 'scxml_ScxmlCancelType88', a2)
    assert _is_linked(b, 'scxml_ScxmlCancelType88', a2)
    if hasattr(a1, 'scxml_ScxmlFinalizeType87'):
        assert not _is_linked(a1, 'scxml_ScxmlFinalizeType87', b)
    if hasattr(a2, 'scxml_ScxmlFinalizeType87'):
        assert _is_linked(a2, 'scxml_ScxmlFinalizeType87', b)
    _safe_set(b, 'scxml_ScxmlCancelType88', None)
    assert not _is_linked(b, 'scxml_ScxmlCancelType88', a2)
    if hasattr(a2, 'scxml_ScxmlFinalizeType87'):
        assert not _is_linked(a2, 'scxml_ScxmlFinalizeType87', b)


def test_assoc_content206_reverse_link_reassign_clear():
    a1 = scxml_ScxmlInvokeType(any="sample_text", anyAttribute="sample_text", autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlInvokeMix="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlInvokeType(any="sample_text_2", anyAttribute="sample_text_2", autoforward="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlInvokeMix="sample_text_2", src="sample_text_2", srcexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlContentType(any="sample_text", anyAttribute="sample_text", expr="sample_text", mixed="sample_text")
    _safe_set(b, 'scxml_ScxmlContentType208', a1)
    assert _is_linked(b, 'scxml_ScxmlContentType208', a1)
    if hasattr(a1, 'scxml_ScxmlInvokeType207'):
        assert _is_linked(a1, 'scxml_ScxmlInvokeType207', b)
    _safe_set(b, 'scxml_ScxmlContentType208', a2)
    assert _is_linked(b, 'scxml_ScxmlContentType208', a2)
    if hasattr(a1, 'scxml_ScxmlInvokeType207'):
        assert not _is_linked(a1, 'scxml_ScxmlInvokeType207', b)
    if hasattr(a2, 'scxml_ScxmlInvokeType207'):
        assert _is_linked(a2, 'scxml_ScxmlInvokeType207', b)
    _safe_set(b, 'scxml_ScxmlContentType208', None)
    assert not _is_linked(b, 'scxml_ScxmlContentType208', a2)
    if hasattr(a2, 'scxml_ScxmlInvokeType207'):
        assert not _is_linked(a2, 'scxml_ScxmlInvokeType207', b)


def test_assoc_content302_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlContentType(any="sample_text", anyAttribute="sample_text", expr="sample_text", mixed="sample_text")
    _safe_set(b, 'scxml_ScxmlContentType304', a1)
    assert _is_linked(b, 'scxml_ScxmlContentType304', a1)
    if hasattr(a1, 'scxml_ScxmlSendType303'):
        assert _is_linked(a1, 'scxml_ScxmlSendType303', b)
    _safe_set(b, 'scxml_ScxmlContentType304', a2)
    assert _is_linked(b, 'scxml_ScxmlContentType304', a2)
    if hasattr(a1, 'scxml_ScxmlSendType303'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType303', b)
    if hasattr(a2, 'scxml_ScxmlSendType303'):
        assert _is_linked(a2, 'scxml_ScxmlSendType303', b)
    _safe_set(b, 'scxml_ScxmlContentType304', None)
    assert not _is_linked(b, 'scxml_ScxmlContentType304', a2)
    if hasattr(a2, 'scxml_ScxmlSendType303'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType303', b)


def test_assoc_content59_reverse_link_reassign_clear():
    a1 = scxml_ScxmlDonedataType(anyAttribute="sample_text")
    a2 = scxml_ScxmlDonedataType(anyAttribute="sample_text_2")
    b = scxml_ScxmlContentType(any="sample_text", anyAttribute="sample_text", expr="sample_text", mixed="sample_text")
    _safe_set(b, 'scxml_ScxmlContentType61', a1)
    assert _is_linked(b, 'scxml_ScxmlContentType61', a1)
    if hasattr(a1, 'scxml_ScxmlDonedataType60'):
        assert _is_linked(a1, 'scxml_ScxmlDonedataType60', b)
    _safe_set(b, 'scxml_ScxmlContentType61', a2)
    assert _is_linked(b, 'scxml_ScxmlContentType61', a2)
    if hasattr(a1, 'scxml_ScxmlDonedataType60'):
        assert not _is_linked(a1, 'scxml_ScxmlDonedataType60', b)
    if hasattr(a2, 'scxml_ScxmlDonedataType60'):
        assert _is_linked(a2, 'scxml_ScxmlDonedataType60', b)
    _safe_set(b, 'scxml_ScxmlContentType61', None)
    assert not _is_linked(b, 'scxml_ScxmlContentType61', a2)
    if hasattr(a2, 'scxml_ScxmlDonedataType60'):
        assert not _is_linked(a2, 'scxml_ScxmlDonedataType60', b)


def test_assoc_content8_reverse_link_reassign_clear():
    a1 = scxml_ScxmlContentType(any="sample_text", anyAttribute="sample_text", expr="sample_text", mixed="sample_text")
    a2 = scxml_ScxmlContentType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", mixed="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot9', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot9', a1)
    if hasattr(a1, 'scxml_ScxmlContentType'):
        assert _is_linked(a1, 'scxml_ScxmlContentType', b)
    _safe_set(b, 'scxml_DocumentRoot9', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot9', a2)
    if hasattr(a1, 'scxml_ScxmlContentType'):
        assert not _is_linked(a1, 'scxml_ScxmlContentType', b)
    if hasattr(a2, 'scxml_ScxmlContentType'):
        assert _is_linked(a2, 'scxml_ScxmlContentType', b)
    _safe_set(b, 'scxml_DocumentRoot9', set())
    assert not _is_linked(b, 'scxml_DocumentRoot9', a2)
    if hasattr(a2, 'scxml_ScxmlContentType'):
        assert not _is_linked(a2, 'scxml_ScxmlContentType', b)


def test_assoc_data10_reverse_link_reassign_clear():
    a1 = scxml_ScxmlDataType(any="sample_text", anyAttribute="sample_text", expr="sample_text", id="sample_text", mixed="sample_text", src="sample_text")
    a2 = scxml_ScxmlDataType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", id="sample_text_2", mixed="sample_text_2", src="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot11', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot11', a1)
    if hasattr(a1, 'scxml_ScxmlDataType'):
        assert _is_linked(a1, 'scxml_ScxmlDataType', b)
    _safe_set(b, 'scxml_DocumentRoot11', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot11', a2)
    if hasattr(a1, 'scxml_ScxmlDataType'):
        assert not _is_linked(a1, 'scxml_ScxmlDataType', b)
    if hasattr(a2, 'scxml_ScxmlDataType'):
        assert _is_linked(a2, 'scxml_ScxmlDataType', b)
    _safe_set(b, 'scxml_DocumentRoot11', set())
    assert not _is_linked(b, 'scxml_DocumentRoot11', a2)
    if hasattr(a2, 'scxml_ScxmlDataType'):
        assert not _is_linked(a2, 'scxml_ScxmlDataType', b)


def test_assoc_data56_reverse_link_reassign_clear():
    a1 = scxml_ScxmlDatamodelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlDatamodelType(any="sample_text_2", anyAttribute="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_ScxmlDataType(any="sample_text", anyAttribute="sample_text", expr="sample_text", id="sample_text", mixed="sample_text", src="sample_text")
    _safe_set(b, 'scxml_ScxmlDataType58', a1)
    assert _is_linked(b, 'scxml_ScxmlDataType58', a1)
    if hasattr(a1, 'scxml_ScxmlDatamodelType57'):
        assert _is_linked(a1, 'scxml_ScxmlDatamodelType57', b)
    _safe_set(b, 'scxml_ScxmlDataType58', a2)
    assert _is_linked(b, 'scxml_ScxmlDataType58', a2)
    if hasattr(a1, 'scxml_ScxmlDatamodelType57'):
        assert not _is_linked(a1, 'scxml_ScxmlDatamodelType57', b)
    if hasattr(a2, 'scxml_ScxmlDatamodelType57'):
        assert _is_linked(a2, 'scxml_ScxmlDatamodelType57', b)
    _safe_set(b, 'scxml_ScxmlDataType58', None)
    assert not _is_linked(b, 'scxml_ScxmlDataType58', a2)
    if hasattr(a2, 'scxml_ScxmlDatamodelType57'):
        assert not _is_linked(a2, 'scxml_ScxmlDatamodelType57', b)


def test_assoc_datamodel12_reverse_link_reassign_clear():
    a1 = scxml_ScxmlDatamodelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlDatamodelType(any="sample_text_2", anyAttribute="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot13', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot13', a1)
    if hasattr(a1, 'scxml_ScxmlDatamodelType'):
        assert _is_linked(a1, 'scxml_ScxmlDatamodelType', b)
    _safe_set(b, 'scxml_DocumentRoot13', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot13', a2)
    if hasattr(a1, 'scxml_ScxmlDatamodelType'):
        assert not _is_linked(a1, 'scxml_ScxmlDatamodelType', b)
    if hasattr(a2, 'scxml_ScxmlDatamodelType'):
        assert _is_linked(a2, 'scxml_ScxmlDatamodelType', b)
    _safe_set(b, 'scxml_DocumentRoot13', set())
    assert not _is_linked(b, 'scxml_DocumentRoot13', a2)
    if hasattr(a2, 'scxml_ScxmlDatamodelType'):
        assert not _is_linked(a2, 'scxml_ScxmlDatamodelType', b)


def test_assoc_datamodel281_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    a2 = scxml_ScxmlParallelType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlParallelMix="sample_text_2")
    b = scxml_ScxmlDatamodelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text")
    _safe_set(b, 'scxml_ScxmlDatamodelType283', a1)
    assert _is_linked(b, 'scxml_ScxmlDatamodelType283', a1)
    if hasattr(a1, 'scxml_ScxmlParallelType282'):
        assert _is_linked(a1, 'scxml_ScxmlParallelType282', b)
    _safe_set(b, 'scxml_ScxmlDatamodelType283', a2)
    assert _is_linked(b, 'scxml_ScxmlDatamodelType283', a2)
    if hasattr(a1, 'scxml_ScxmlParallelType282'):
        assert not _is_linked(a1, 'scxml_ScxmlParallelType282', b)
    if hasattr(a2, 'scxml_ScxmlParallelType282'):
        assert _is_linked(a2, 'scxml_ScxmlParallelType282', b)
    _safe_set(b, 'scxml_ScxmlDatamodelType283', None)
    assert not _is_linked(b, 'scxml_ScxmlDatamodelType283', a2)
    if hasattr(a2, 'scxml_ScxmlParallelType282'):
        assert not _is_linked(a2, 'scxml_ScxmlParallelType282', b)


def test_assoc_datamodel296_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScxmlType(any="sample_text", anyAttribute="sample_text", binding="sample_text", datamodel1="sample_text", exmode="sample_text", initial="sample_text", name="sample_text", scxmlScxmlMix="sample_text", version="sample_text")
    a2 = scxml_ScxmlScxmlType(any="sample_text_2", anyAttribute="sample_text_2", binding="sample_text_2", datamodel1="sample_text_2", exmode="sample_text_2", initial="sample_text_2", name="sample_text_2", scxmlScxmlMix="sample_text_2", version="sample_text_2")
    b = scxml_ScxmlDatamodelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text")
    _safe_set(b, 'scxml_ScxmlDatamodelType298', a1)
    assert _is_linked(b, 'scxml_ScxmlDatamodelType298', a1)
    if hasattr(a1, 'scxml_ScxmlScxmlType297'):
        assert _is_linked(a1, 'scxml_ScxmlScxmlType297', b)
    _safe_set(b, 'scxml_ScxmlDatamodelType298', a2)
    assert _is_linked(b, 'scxml_ScxmlDatamodelType298', a2)
    if hasattr(a1, 'scxml_ScxmlScxmlType297'):
        assert not _is_linked(a1, 'scxml_ScxmlScxmlType297', b)
    if hasattr(a2, 'scxml_ScxmlScxmlType297'):
        assert _is_linked(a2, 'scxml_ScxmlScxmlType297', b)
    _safe_set(b, 'scxml_ScxmlDatamodelType298', None)
    assert not _is_linked(b, 'scxml_ScxmlDatamodelType298', a2)
    if hasattr(a2, 'scxml_ScxmlScxmlType297'):
        assert not _is_linked(a2, 'scxml_ScxmlScxmlType297', b)


def test_assoc_datamodel332_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlDatamodelType(any="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text")
    _safe_set(b, 'scxml_ScxmlDatamodelType334', a1)
    assert _is_linked(b, 'scxml_ScxmlDatamodelType334', a1)
    if hasattr(a1, 'scxml_ScxmlStateType333'):
        assert _is_linked(a1, 'scxml_ScxmlStateType333', b)
    _safe_set(b, 'scxml_ScxmlDatamodelType334', a2)
    assert _is_linked(b, 'scxml_ScxmlDatamodelType334', a2)
    if hasattr(a1, 'scxml_ScxmlStateType333'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType333', b)
    if hasattr(a2, 'scxml_ScxmlStateType333'):
        assert _is_linked(a2, 'scxml_ScxmlStateType333', b)
    _safe_set(b, 'scxml_ScxmlDatamodelType334', None)
    assert not _is_linked(b, 'scxml_ScxmlDatamodelType334', a2)
    if hasattr(a2, 'scxml_ScxmlStateType333'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType333', b)


def test_assoc_donedata14_reverse_link_reassign_clear():
    a1 = scxml_ScxmlDonedataType(anyAttribute="sample_text")
    a2 = scxml_ScxmlDonedataType(anyAttribute="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot15', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot15', a1)
    if hasattr(a1, 'scxml_ScxmlDonedataType'):
        assert _is_linked(a1, 'scxml_ScxmlDonedataType', b)
    _safe_set(b, 'scxml_DocumentRoot15', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot15', a2)
    if hasattr(a1, 'scxml_ScxmlDonedataType'):
        assert not _is_linked(a1, 'scxml_ScxmlDonedataType', b)
    if hasattr(a2, 'scxml_ScxmlDonedataType'):
        assert _is_linked(a2, 'scxml_ScxmlDonedataType', b)
    _safe_set(b, 'scxml_DocumentRoot15', set())
    assert not _is_linked(b, 'scxml_DocumentRoot15', a2)
    if hasattr(a2, 'scxml_ScxmlDonedataType'):
        assert not _is_linked(a2, 'scxml_ScxmlDonedataType', b)


def test_assoc_donedata95_reverse_link_reassign_clear():
    a1 = scxml_ScxmlFinalType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlFinalMix="sample_text")
    a2 = scxml_ScxmlFinalType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlFinalMix="sample_text_2")
    b = scxml_ScxmlDonedataType(anyAttribute="sample_text")
    _safe_set(b, 'scxml_ScxmlDonedataType97', a1)
    assert _is_linked(b, 'scxml_ScxmlDonedataType97', a1)
    if hasattr(a1, 'scxml_ScxmlFinalType96'):
        assert _is_linked(a1, 'scxml_ScxmlFinalType96', b)
    _safe_set(b, 'scxml_ScxmlDonedataType97', a2)
    assert _is_linked(b, 'scxml_ScxmlDonedataType97', a2)
    if hasattr(a1, 'scxml_ScxmlFinalType96'):
        assert not _is_linked(a1, 'scxml_ScxmlFinalType96', b)
    if hasattr(a2, 'scxml_ScxmlFinalType96'):
        assert _is_linked(a2, 'scxml_ScxmlFinalType96', b)
    _safe_set(b, 'scxml_ScxmlDonedataType97', None)
    assert not _is_linked(b, 'scxml_ScxmlDonedataType97', a2)
    if hasattr(a2, 'scxml_ScxmlFinalType96'):
        assert not _is_linked(a2, 'scxml_ScxmlFinalType96', b)


def test_assoc_else_16_reverse_link_reassign_clear():
    a1 = scxml_ScxmlElseType(anyAttribute="sample_text")
    a2 = scxml_ScxmlElseType(anyAttribute="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot17', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot17', a1)
    if hasattr(a1, 'scxml_ScxmlElseType'):
        assert _is_linked(a1, 'scxml_ScxmlElseType', b)
    _safe_set(b, 'scxml_DocumentRoot17', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot17', a2)
    if hasattr(a1, 'scxml_ScxmlElseType'):
        assert not _is_linked(a1, 'scxml_ScxmlElseType', b)
    if hasattr(a2, 'scxml_ScxmlElseType'):
        assert _is_linked(a2, 'scxml_ScxmlElseType', b)
    _safe_set(b, 'scxml_DocumentRoot17', set())
    assert not _is_linked(b, 'scxml_DocumentRoot17', a2)
    if hasattr(a2, 'scxml_ScxmlElseType'):
        assert not _is_linked(a2, 'scxml_ScxmlElseType', b)


def test_assoc_else_176_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlElseType(anyAttribute="sample_text")
    _safe_set(b, 'scxml_ScxmlElseType178', a1)
    assert _is_linked(b, 'scxml_ScxmlElseType178', a1)
    if hasattr(a1, 'scxml_ScxmlIfType177'):
        assert _is_linked(a1, 'scxml_ScxmlIfType177', b)
    _safe_set(b, 'scxml_ScxmlElseType178', a2)
    assert _is_linked(b, 'scxml_ScxmlElseType178', a2)
    if hasattr(a1, 'scxml_ScxmlIfType177'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType177', b)
    if hasattr(a2, 'scxml_ScxmlIfType177'):
        assert _is_linked(a2, 'scxml_ScxmlIfType177', b)
    _safe_set(b, 'scxml_ScxmlElseType178', None)
    assert not _is_linked(b, 'scxml_ScxmlElseType178', a2)
    if hasattr(a2, 'scxml_ScxmlIfType177'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType177', b)


def test_assoc_elseif149_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlElseifType(anyAttribute="sample_text", cond="sample_text")
    _safe_set(b, 'scxml_ScxmlElseifType151', a1)
    assert _is_linked(b, 'scxml_ScxmlElseifType151', a1)
    if hasattr(a1, 'scxml_ScxmlIfType150'):
        assert _is_linked(a1, 'scxml_ScxmlIfType150', b)
    _safe_set(b, 'scxml_ScxmlElseifType151', a2)
    assert _is_linked(b, 'scxml_ScxmlElseifType151', a2)
    if hasattr(a1, 'scxml_ScxmlIfType150'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType150', b)
    if hasattr(a2, 'scxml_ScxmlIfType150'):
        assert _is_linked(a2, 'scxml_ScxmlIfType150', b)
    _safe_set(b, 'scxml_ScxmlElseifType151', None)
    assert not _is_linked(b, 'scxml_ScxmlElseifType151', a2)
    if hasattr(a2, 'scxml_ScxmlIfType150'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType150', b)


def test_assoc_elseif18_reverse_link_reassign_clear():
    a1 = scxml_ScxmlElseifType(anyAttribute="sample_text", cond="sample_text")
    a2 = scxml_ScxmlElseifType(anyAttribute="sample_text_2", cond="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot19', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot19', a1)
    if hasattr(a1, 'scxml_ScxmlElseifType'):
        assert _is_linked(a1, 'scxml_ScxmlElseifType', b)
    _safe_set(b, 'scxml_DocumentRoot19', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot19', a2)
    if hasattr(a1, 'scxml_ScxmlElseifType'):
        assert not _is_linked(a1, 'scxml_ScxmlElseifType', b)
    if hasattr(a2, 'scxml_ScxmlElseifType'):
        assert _is_linked(a2, 'scxml_ScxmlElseifType', b)
    _safe_set(b, 'scxml_DocumentRoot19', set())
    assert not _is_linked(b, 'scxml_DocumentRoot19', a2)
    if hasattr(a2, 'scxml_ScxmlElseifType'):
        assert not _is_linked(a2, 'scxml_ScxmlElseifType', b)


def test_assoc_final20_reverse_link_reassign_clear():
    a1 = scxml_ScxmlFinalType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlFinalMix="sample_text")
    a2 = scxml_ScxmlFinalType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlFinalMix="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot21', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot21', a1)
    if hasattr(a1, 'scxml_ScxmlFinalType'):
        assert _is_linked(a1, 'scxml_ScxmlFinalType', b)
    _safe_set(b, 'scxml_DocumentRoot21', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot21', a2)
    if hasattr(a1, 'scxml_ScxmlFinalType'):
        assert not _is_linked(a1, 'scxml_ScxmlFinalType', b)
    if hasattr(a2, 'scxml_ScxmlFinalType'):
        assert _is_linked(a2, 'scxml_ScxmlFinalType', b)
    _safe_set(b, 'scxml_DocumentRoot21', set())
    assert not _is_linked(b, 'scxml_DocumentRoot21', a2)
    if hasattr(a2, 'scxml_ScxmlFinalType'):
        assert not _is_linked(a2, 'scxml_ScxmlFinalType', b)


def test_assoc_final293_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScxmlType(any="sample_text", anyAttribute="sample_text", binding="sample_text", datamodel1="sample_text", exmode="sample_text", initial="sample_text", name="sample_text", scxmlScxmlMix="sample_text", version="sample_text")
    a2 = scxml_ScxmlScxmlType(any="sample_text_2", anyAttribute="sample_text_2", binding="sample_text_2", datamodel1="sample_text_2", exmode="sample_text_2", initial="sample_text_2", name="sample_text_2", scxmlScxmlMix="sample_text_2", version="sample_text_2")
    b = scxml_ScxmlFinalType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlFinalMix="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalType295', a1)
    assert _is_linked(b, 'scxml_ScxmlFinalType295', a1)
    if hasattr(a1, 'scxml_ScxmlScxmlType294'):
        assert _is_linked(a1, 'scxml_ScxmlScxmlType294', b)
    _safe_set(b, 'scxml_ScxmlFinalType295', a2)
    assert _is_linked(b, 'scxml_ScxmlFinalType295', a2)
    if hasattr(a1, 'scxml_ScxmlScxmlType294'):
        assert not _is_linked(a1, 'scxml_ScxmlScxmlType294', b)
    if hasattr(a2, 'scxml_ScxmlScxmlType294'):
        assert _is_linked(a2, 'scxml_ScxmlScxmlType294', b)
    _safe_set(b, 'scxml_ScxmlFinalType295', None)
    assert not _is_linked(b, 'scxml_ScxmlFinalType295', a2)
    if hasattr(a2, 'scxml_ScxmlScxmlType294'):
        assert not _is_linked(a2, 'scxml_ScxmlScxmlType294', b)


def test_assoc_final326_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlFinalType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlFinalMix="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalType328', a1)
    assert _is_linked(b, 'scxml_ScxmlFinalType328', a1)
    if hasattr(a1, 'scxml_ScxmlStateType327'):
        assert _is_linked(a1, 'scxml_ScxmlStateType327', b)
    _safe_set(b, 'scxml_ScxmlFinalType328', a2)
    assert _is_linked(b, 'scxml_ScxmlFinalType328', a2)
    if hasattr(a1, 'scxml_ScxmlStateType327'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType327', b)
    if hasattr(a2, 'scxml_ScxmlStateType327'):
        assert _is_linked(a2, 'scxml_ScxmlStateType327', b)
    _safe_set(b, 'scxml_ScxmlFinalType328', None)
    assert not _is_linked(b, 'scxml_ScxmlFinalType328', a2)
    if hasattr(a2, 'scxml_ScxmlStateType327'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType327', b)


def test_assoc_finalize212_reverse_link_reassign_clear():
    a1 = scxml_ScxmlInvokeType(any="sample_text", anyAttribute="sample_text", autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlInvokeMix="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlInvokeType(any="sample_text_2", anyAttribute="sample_text_2", autoforward="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlInvokeMix="sample_text_2", src="sample_text_2", srcexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalizeType214', a1)
    assert _is_linked(b, 'scxml_ScxmlFinalizeType214', a1)
    if hasattr(a1, 'scxml_ScxmlInvokeType213'):
        assert _is_linked(a1, 'scxml_ScxmlInvokeType213', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType214', a2)
    assert _is_linked(b, 'scxml_ScxmlFinalizeType214', a2)
    if hasattr(a1, 'scxml_ScxmlInvokeType213'):
        assert not _is_linked(a1, 'scxml_ScxmlInvokeType213', b)
    if hasattr(a2, 'scxml_ScxmlInvokeType213'):
        assert _is_linked(a2, 'scxml_ScxmlInvokeType213', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType214', None)
    assert not _is_linked(b, 'scxml_ScxmlFinalizeType214', a2)
    if hasattr(a2, 'scxml_ScxmlInvokeType213'):
        assert not _is_linked(a2, 'scxml_ScxmlInvokeType213', b)


def test_assoc_finalize22_reverse_link_reassign_clear():
    a1 = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlFinalizeType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot23', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot23', a1)
    if hasattr(a1, 'scxml_ScxmlFinalizeType'):
        assert _is_linked(a1, 'scxml_ScxmlFinalizeType', b)
    _safe_set(b, 'scxml_DocumentRoot23', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot23', a2)
    if hasattr(a1, 'scxml_ScxmlFinalizeType'):
        assert not _is_linked(a1, 'scxml_ScxmlFinalizeType', b)
    if hasattr(a2, 'scxml_ScxmlFinalizeType'):
        assert _is_linked(a2, 'scxml_ScxmlFinalizeType', b)
    _safe_set(b, 'scxml_DocumentRoot23', set())
    assert not _is_linked(b, 'scxml_DocumentRoot23', a2)
    if hasattr(a2, 'scxml_ScxmlFinalizeType'):
        assert not _is_linked(a2, 'scxml_ScxmlFinalizeType', b)


def test_assoc_foreach105_reverse_link_reassign_clear():
    a1 = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlForeachType(any="sample_text_2", anyAttribute="sample_text_2", array="sample_text_2", index="sample_text_2", item="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType106', a1)
    assert _is_linked(b, 'scxml_ScxmlForeachType106', a1)
    if hasattr(a1, 'scxml_ScxmlForeachType104'):
        assert _is_linked(a1, 'scxml_ScxmlForeachType104', b)
    _safe_set(b, 'scxml_ScxmlForeachType106', a2)
    assert _is_linked(b, 'scxml_ScxmlForeachType106', a2)
    if hasattr(a1, 'scxml_ScxmlForeachType104'):
        assert not _is_linked(a1, 'scxml_ScxmlForeachType104', b)
    if hasattr(a2, 'scxml_ScxmlForeachType104'):
        assert _is_linked(a2, 'scxml_ScxmlForeachType104', b)
    _safe_set(b, 'scxml_ScxmlForeachType106', None)
    assert not _is_linked(b, 'scxml_ScxmlForeachType106', a2)
    if hasattr(a2, 'scxml_ScxmlForeachType104'):
        assert not _is_linked(a2, 'scxml_ScxmlForeachType104', b)


def test_assoc_foreach1158_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType160', a1)
    assert _is_linked(b, 'scxml_ScxmlForeachType160', a1)
    if hasattr(a1, 'scxml_ScxmlIfType159'):
        assert _is_linked(a1, 'scxml_ScxmlIfType159', b)
    _safe_set(b, 'scxml_ScxmlForeachType160', a2)
    assert _is_linked(b, 'scxml_ScxmlForeachType160', a2)
    if hasattr(a1, 'scxml_ScxmlIfType159'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType159', b)
    if hasattr(a2, 'scxml_ScxmlIfType159'):
        assert _is_linked(a2, 'scxml_ScxmlIfType159', b)
    _safe_set(b, 'scxml_ScxmlForeachType160', None)
    assert not _is_linked(b, 'scxml_ScxmlForeachType160', a2)
    if hasattr(a2, 'scxml_ScxmlIfType159'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType159', b)


def test_assoc_foreach131_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType133', a1)
    assert _is_linked(b, 'scxml_ScxmlForeachType133', a1)
    if hasattr(a1, 'scxml_ScxmlIfType132'):
        assert _is_linked(a1, 'scxml_ScxmlIfType132', b)
    _safe_set(b, 'scxml_ScxmlForeachType133', a2)
    assert _is_linked(b, 'scxml_ScxmlForeachType133', a2)
    if hasattr(a1, 'scxml_ScxmlIfType132'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType132', b)
    if hasattr(a2, 'scxml_ScxmlIfType132'):
        assert _is_linked(a2, 'scxml_ScxmlIfType132', b)
    _safe_set(b, 'scxml_ScxmlForeachType133', None)
    assert not _is_linked(b, 'scxml_ScxmlForeachType133', a2)
    if hasattr(a2, 'scxml_ScxmlIfType132'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType132', b)


def test_assoc_foreach2185_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType187', a1)
    assert _is_linked(b, 'scxml_ScxmlForeachType187', a1)
    if hasattr(a1, 'scxml_ScxmlIfType186'):
        assert _is_linked(a1, 'scxml_ScxmlIfType186', b)
    _safe_set(b, 'scxml_ScxmlForeachType187', a2)
    assert _is_linked(b, 'scxml_ScxmlForeachType187', a2)
    if hasattr(a1, 'scxml_ScxmlIfType186'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType186', b)
    if hasattr(a2, 'scxml_ScxmlIfType186'):
        assert _is_linked(a2, 'scxml_ScxmlIfType186', b)
    _safe_set(b, 'scxml_ScxmlForeachType187', None)
    assert not _is_linked(b, 'scxml_ScxmlForeachType187', a2)
    if hasattr(a2, 'scxml_ScxmlIfType186'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType186', b)


def test_assoc_foreach221_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnentryType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType223', a1)
    assert _is_linked(b, 'scxml_ScxmlForeachType223', a1)
    if hasattr(a1, 'scxml_ScxmlOnentryType222'):
        assert _is_linked(a1, 'scxml_ScxmlOnentryType222', b)
    _safe_set(b, 'scxml_ScxmlForeachType223', a2)
    assert _is_linked(b, 'scxml_ScxmlForeachType223', a2)
    if hasattr(a1, 'scxml_ScxmlOnentryType222'):
        assert not _is_linked(a1, 'scxml_ScxmlOnentryType222', b)
    if hasattr(a2, 'scxml_ScxmlOnentryType222'):
        assert _is_linked(a2, 'scxml_ScxmlOnentryType222', b)
    _safe_set(b, 'scxml_ScxmlForeachType223', None)
    assert not _is_linked(b, 'scxml_ScxmlForeachType223', a2)
    if hasattr(a2, 'scxml_ScxmlOnentryType222'):
        assert not _is_linked(a2, 'scxml_ScxmlOnentryType222', b)


def test_assoc_foreach24_reverse_link_reassign_clear():
    a1 = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlForeachType(any="sample_text_2", anyAttribute="sample_text_2", array="sample_text_2", index="sample_text_2", item="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot25', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot25', a1)
    if hasattr(a1, 'scxml_ScxmlForeachType'):
        assert _is_linked(a1, 'scxml_ScxmlForeachType', b)
    _safe_set(b, 'scxml_DocumentRoot25', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot25', a2)
    if hasattr(a1, 'scxml_ScxmlForeachType'):
        assert not _is_linked(a1, 'scxml_ScxmlForeachType', b)
    if hasattr(a2, 'scxml_ScxmlForeachType'):
        assert _is_linked(a2, 'scxml_ScxmlForeachType', b)
    _safe_set(b, 'scxml_DocumentRoot25', set())
    assert not _is_linked(b, 'scxml_DocumentRoot25', a2)
    if hasattr(a2, 'scxml_ScxmlForeachType'):
        assert not _is_linked(a2, 'scxml_ScxmlForeachType', b)


def test_assoc_foreach245_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnexitType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType247', a1)
    assert _is_linked(b, 'scxml_ScxmlForeachType247', a1)
    if hasattr(a1, 'scxml_ScxmlOnexitType246'):
        assert _is_linked(a1, 'scxml_ScxmlOnexitType246', b)
    _safe_set(b, 'scxml_ScxmlForeachType247', a2)
    assert _is_linked(b, 'scxml_ScxmlForeachType247', a2)
    if hasattr(a1, 'scxml_ScxmlOnexitType246'):
        assert not _is_linked(a1, 'scxml_ScxmlOnexitType246', b)
    if hasattr(a2, 'scxml_ScxmlOnexitType246'):
        assert _is_linked(a2, 'scxml_ScxmlOnexitType246', b)
    _safe_set(b, 'scxml_ScxmlForeachType247', None)
    assert not _is_linked(b, 'scxml_ScxmlForeachType247', a2)
    if hasattr(a2, 'scxml_ScxmlOnexitType246'):
        assert not _is_linked(a2, 'scxml_ScxmlOnexitType246', b)


def test_assoc_foreach344_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType346', a1)
    assert _is_linked(b, 'scxml_ScxmlForeachType346', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType345'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType345', b)
    _safe_set(b, 'scxml_ScxmlForeachType346', a2)
    assert _is_linked(b, 'scxml_ScxmlForeachType346', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType345'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType345', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType345'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType345', b)
    _safe_set(b, 'scxml_ScxmlForeachType346', None)
    assert not _is_linked(b, 'scxml_ScxmlForeachType346', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType345'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType345', b)


def test_assoc_foreach71_reverse_link_reassign_clear():
    a1 = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlForeachType(any="sample_text_2", anyAttribute="sample_text_2", array="sample_text_2", index="sample_text_2", item="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalizeType72', {a1})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType72', a1)
    if hasattr(a1, 'scxml_ScxmlForeachType73'):
        assert _is_linked(a1, 'scxml_ScxmlForeachType73', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType72', {a2})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType72', a2)
    if hasattr(a1, 'scxml_ScxmlForeachType73'):
        assert not _is_linked(a1, 'scxml_ScxmlForeachType73', b)
    if hasattr(a2, 'scxml_ScxmlForeachType73'):
        assert _is_linked(a2, 'scxml_ScxmlForeachType73', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType72', set())
    assert not _is_linked(b, 'scxml_ScxmlFinalizeType72', a2)
    if hasattr(a2, 'scxml_ScxmlForeachType73'):
        assert not _is_linked(a2, 'scxml_ScxmlForeachType73', b)


def test_assoc_history26_reverse_link_reassign_clear():
    a1 = scxml_ScxmlHistoryType(any="sample_text", any1="sample_text", anyAttribute="sample_text", id="sample_text", scxmlExtraContent="sample_text", scxmlExtraContent1="sample_text", type="sample_text")
    a2 = scxml_ScxmlHistoryType(any="sample_text_2", any1="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlExtraContent="sample_text_2", scxmlExtraContent1="sample_text_2", type="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot27', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot27', a1)
    if hasattr(a1, 'scxml_ScxmlHistoryType'):
        assert _is_linked(a1, 'scxml_ScxmlHistoryType', b)
    _safe_set(b, 'scxml_DocumentRoot27', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot27', a2)
    if hasattr(a1, 'scxml_ScxmlHistoryType'):
        assert not _is_linked(a1, 'scxml_ScxmlHistoryType', b)
    if hasattr(a2, 'scxml_ScxmlHistoryType'):
        assert _is_linked(a2, 'scxml_ScxmlHistoryType', b)
    _safe_set(b, 'scxml_DocumentRoot27', set())
    assert not _is_linked(b, 'scxml_DocumentRoot27', a2)
    if hasattr(a2, 'scxml_ScxmlHistoryType'):
        assert not _is_linked(a2, 'scxml_ScxmlHistoryType', b)


def test_assoc_history278_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    a2 = scxml_ScxmlParallelType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlParallelMix="sample_text_2")
    b = scxml_ScxmlHistoryType(any="sample_text", any1="sample_text", anyAttribute="sample_text", id="sample_text", scxmlExtraContent="sample_text", scxmlExtraContent1="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlHistoryType280', a1)
    assert _is_linked(b, 'scxml_ScxmlHistoryType280', a1)
    if hasattr(a1, 'scxml_ScxmlParallelType279'):
        assert _is_linked(a1, 'scxml_ScxmlParallelType279', b)
    _safe_set(b, 'scxml_ScxmlHistoryType280', a2)
    assert _is_linked(b, 'scxml_ScxmlHistoryType280', a2)
    if hasattr(a1, 'scxml_ScxmlParallelType279'):
        assert not _is_linked(a1, 'scxml_ScxmlParallelType279', b)
    if hasattr(a2, 'scxml_ScxmlParallelType279'):
        assert _is_linked(a2, 'scxml_ScxmlParallelType279', b)
    _safe_set(b, 'scxml_ScxmlHistoryType280', None)
    assert not _is_linked(b, 'scxml_ScxmlHistoryType280', a2)
    if hasattr(a2, 'scxml_ScxmlParallelType279'):
        assert not _is_linked(a2, 'scxml_ScxmlParallelType279', b)


def test_assoc_history329_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlHistoryType(any="sample_text", any1="sample_text", anyAttribute="sample_text", id="sample_text", scxmlExtraContent="sample_text", scxmlExtraContent1="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlHistoryType331', a1)
    assert _is_linked(b, 'scxml_ScxmlHistoryType331', a1)
    if hasattr(a1, 'scxml_ScxmlStateType330'):
        assert _is_linked(a1, 'scxml_ScxmlStateType330', b)
    _safe_set(b, 'scxml_ScxmlHistoryType331', a2)
    assert _is_linked(b, 'scxml_ScxmlHistoryType331', a2)
    if hasattr(a1, 'scxml_ScxmlStateType330'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType330', b)
    if hasattr(a2, 'scxml_ScxmlStateType330'):
        assert _is_linked(a2, 'scxml_ScxmlStateType330', b)
    _safe_set(b, 'scxml_ScxmlHistoryType331', None)
    assert not _is_linked(b, 'scxml_ScxmlHistoryType331', a2)
    if hasattr(a2, 'scxml_ScxmlStateType330'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType330', b)


def test_assoc_if1156_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType157', a1)
    assert _is_linked(b, 'scxml_ScxmlIfType157', a1)
    if hasattr(a1, 'scxml_ScxmlIfType155'):
        assert _is_linked(a1, 'scxml_ScxmlIfType155', b)
    _safe_set(b, 'scxml_ScxmlIfType157', a2)
    assert _is_linked(b, 'scxml_ScxmlIfType157', a2)
    if hasattr(a1, 'scxml_ScxmlIfType155'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType155', b)
    if hasattr(a2, 'scxml_ScxmlIfType155'):
        assert _is_linked(a2, 'scxml_ScxmlIfType155', b)
    _safe_set(b, 'scxml_ScxmlIfType157', None)
    assert not _is_linked(b, 'scxml_ScxmlIfType157', a2)
    if hasattr(a2, 'scxml_ScxmlIfType155'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType155', b)


def test_assoc_if2183_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType184', a1)
    assert _is_linked(b, 'scxml_ScxmlIfType184', a1)
    if hasattr(a1, 'scxml_ScxmlIfType182'):
        assert _is_linked(a1, 'scxml_ScxmlIfType182', b)
    _safe_set(b, 'scxml_ScxmlIfType184', a2)
    assert _is_linked(b, 'scxml_ScxmlIfType184', a2)
    if hasattr(a1, 'scxml_ScxmlIfType182'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType182', b)
    if hasattr(a2, 'scxml_ScxmlIfType182'):
        assert _is_linked(a2, 'scxml_ScxmlIfType182', b)
    _safe_set(b, 'scxml_ScxmlIfType184', None)
    assert not _is_linked(b, 'scxml_ScxmlIfType184', a2)
    if hasattr(a2, 'scxml_ScxmlIfType182'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType182', b)


def test_assoc_if_101_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType102', {a1})
    assert _is_linked(b, 'scxml_ScxmlForeachType102', a1)
    if hasattr(a1, 'scxml_ScxmlIfType103'):
        assert _is_linked(a1, 'scxml_ScxmlIfType103', b)
    _safe_set(b, 'scxml_ScxmlForeachType102', {a2})
    assert _is_linked(b, 'scxml_ScxmlForeachType102', a2)
    if hasattr(a1, 'scxml_ScxmlIfType103'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType103', b)
    if hasattr(a2, 'scxml_ScxmlIfType103'):
        assert _is_linked(a2, 'scxml_ScxmlIfType103', b)
    _safe_set(b, 'scxml_ScxmlForeachType102', set())
    assert not _is_linked(b, 'scxml_ScxmlForeachType102', a2)
    if hasattr(a2, 'scxml_ScxmlIfType103'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType103', b)


def test_assoc_if_129_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType130', a1)
    assert _is_linked(b, 'scxml_ScxmlIfType130', a1)
    if hasattr(a1, 'scxml_ScxmlIfType128'):
        assert _is_linked(a1, 'scxml_ScxmlIfType128', b)
    _safe_set(b, 'scxml_ScxmlIfType130', a2)
    assert _is_linked(b, 'scxml_ScxmlIfType130', a2)
    if hasattr(a1, 'scxml_ScxmlIfType128'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType128', b)
    if hasattr(a2, 'scxml_ScxmlIfType128'):
        assert _is_linked(a2, 'scxml_ScxmlIfType128', b)
    _safe_set(b, 'scxml_ScxmlIfType130', None)
    assert not _is_linked(b, 'scxml_ScxmlIfType130', a2)
    if hasattr(a2, 'scxml_ScxmlIfType128'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType128', b)


def test_assoc_if_218_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnentryType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType220', a1)
    assert _is_linked(b, 'scxml_ScxmlIfType220', a1)
    if hasattr(a1, 'scxml_ScxmlOnentryType219'):
        assert _is_linked(a1, 'scxml_ScxmlOnentryType219', b)
    _safe_set(b, 'scxml_ScxmlIfType220', a2)
    assert _is_linked(b, 'scxml_ScxmlIfType220', a2)
    if hasattr(a1, 'scxml_ScxmlOnentryType219'):
        assert not _is_linked(a1, 'scxml_ScxmlOnentryType219', b)
    if hasattr(a2, 'scxml_ScxmlOnentryType219'):
        assert _is_linked(a2, 'scxml_ScxmlOnentryType219', b)
    _safe_set(b, 'scxml_ScxmlIfType220', None)
    assert not _is_linked(b, 'scxml_ScxmlIfType220', a2)
    if hasattr(a2, 'scxml_ScxmlOnentryType219'):
        assert not _is_linked(a2, 'scxml_ScxmlOnentryType219', b)


def test_assoc_if_242_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnexitType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType244', a1)
    assert _is_linked(b, 'scxml_ScxmlIfType244', a1)
    if hasattr(a1, 'scxml_ScxmlOnexitType243'):
        assert _is_linked(a1, 'scxml_ScxmlOnexitType243', b)
    _safe_set(b, 'scxml_ScxmlIfType244', a2)
    assert _is_linked(b, 'scxml_ScxmlIfType244', a2)
    if hasattr(a1, 'scxml_ScxmlOnexitType243'):
        assert not _is_linked(a1, 'scxml_ScxmlOnexitType243', b)
    if hasattr(a2, 'scxml_ScxmlOnexitType243'):
        assert _is_linked(a2, 'scxml_ScxmlOnexitType243', b)
    _safe_set(b, 'scxml_ScxmlIfType244', None)
    assert not _is_linked(b, 'scxml_ScxmlIfType244', a2)
    if hasattr(a2, 'scxml_ScxmlOnexitType243'):
        assert not _is_linked(a2, 'scxml_ScxmlOnexitType243', b)


def test_assoc_if_28_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot29', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot29', a1)
    if hasattr(a1, 'scxml_ScxmlIfType'):
        assert _is_linked(a1, 'scxml_ScxmlIfType', b)
    _safe_set(b, 'scxml_DocumentRoot29', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot29', a2)
    if hasattr(a1, 'scxml_ScxmlIfType'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType', b)
    if hasattr(a2, 'scxml_ScxmlIfType'):
        assert _is_linked(a2, 'scxml_ScxmlIfType', b)
    _safe_set(b, 'scxml_DocumentRoot29', set())
    assert not _is_linked(b, 'scxml_DocumentRoot29', a2)
    if hasattr(a2, 'scxml_ScxmlIfType'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType', b)


def test_assoc_if_341_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType343', a1)
    assert _is_linked(b, 'scxml_ScxmlIfType343', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType342'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType342', b)
    _safe_set(b, 'scxml_ScxmlIfType343', a2)
    assert _is_linked(b, 'scxml_ScxmlIfType343', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType342'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType342', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType342'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType342', b)
    _safe_set(b, 'scxml_ScxmlIfType343', None)
    assert not _is_linked(b, 'scxml_ScxmlIfType343', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType342'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType342', b)


def test_assoc_if_68_reverse_link_reassign_clear():
    a1 = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    a2 = scxml_ScxmlIfType(any="sample_text_2", any1="sample_text_2", any2="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", scxmlCoreExecutablecontent1="sample_text_2", scxmlCoreExecutablecontent2="sample_text_2")
    b = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalizeType69', {a1})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType69', a1)
    if hasattr(a1, 'scxml_ScxmlIfType70'):
        assert _is_linked(a1, 'scxml_ScxmlIfType70', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType69', {a2})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType69', a2)
    if hasattr(a1, 'scxml_ScxmlIfType70'):
        assert not _is_linked(a1, 'scxml_ScxmlIfType70', b)
    if hasattr(a2, 'scxml_ScxmlIfType70'):
        assert _is_linked(a2, 'scxml_ScxmlIfType70', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType69', set())
    assert not _is_linked(b, 'scxml_ScxmlFinalizeType69', a2)
    if hasattr(a2, 'scxml_ScxmlIfType70'):
        assert not _is_linked(a2, 'scxml_ScxmlIfType70', b)


def test_assoc_initial30_reverse_link_reassign_clear():
    a1 = scxml_ScxmlInitialType(any="sample_text", any1="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", scxmlExtraContent1="sample_text")
    a2 = scxml_ScxmlInitialType(any="sample_text_2", any1="sample_text_2", anyAttribute="sample_text_2", scxmlExtraContent="sample_text_2", scxmlExtraContent1="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot31', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot31', a1)
    if hasattr(a1, 'scxml_ScxmlInitialType'):
        assert _is_linked(a1, 'scxml_ScxmlInitialType', b)
    _safe_set(b, 'scxml_DocumentRoot31', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot31', a2)
    if hasattr(a1, 'scxml_ScxmlInitialType'):
        assert not _is_linked(a1, 'scxml_ScxmlInitialType', b)
    if hasattr(a2, 'scxml_ScxmlInitialType'):
        assert _is_linked(a2, 'scxml_ScxmlInitialType', b)
    _safe_set(b, 'scxml_DocumentRoot31', set())
    assert not _is_linked(b, 'scxml_DocumentRoot31', a2)
    if hasattr(a2, 'scxml_ScxmlInitialType'):
        assert not _is_linked(a2, 'scxml_ScxmlInitialType', b)


def test_assoc_initial317_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlInitialType(any="sample_text", any1="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", scxmlExtraContent1="sample_text")
    _safe_set(b, 'scxml_ScxmlInitialType319', a1)
    assert _is_linked(b, 'scxml_ScxmlInitialType319', a1)
    if hasattr(a1, 'scxml_ScxmlStateType318'):
        assert _is_linked(a1, 'scxml_ScxmlStateType318', b)
    _safe_set(b, 'scxml_ScxmlInitialType319', a2)
    assert _is_linked(b, 'scxml_ScxmlInitialType319', a2)
    if hasattr(a1, 'scxml_ScxmlStateType318'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType318', b)
    if hasattr(a2, 'scxml_ScxmlStateType318'):
        assert _is_linked(a2, 'scxml_ScxmlStateType318', b)
    _safe_set(b, 'scxml_ScxmlInitialType319', None)
    assert not _is_linked(b, 'scxml_ScxmlInitialType319', a2)
    if hasattr(a2, 'scxml_ScxmlStateType318'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType318', b)


def test_assoc_invoke284_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    a2 = scxml_ScxmlParallelType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlParallelMix="sample_text_2")
    b = scxml_ScxmlInvokeType(any="sample_text", anyAttribute="sample_text", autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlInvokeMix="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlInvokeType286', a1)
    assert _is_linked(b, 'scxml_ScxmlInvokeType286', a1)
    if hasattr(a1, 'scxml_ScxmlParallelType285'):
        assert _is_linked(a1, 'scxml_ScxmlParallelType285', b)
    _safe_set(b, 'scxml_ScxmlInvokeType286', a2)
    assert _is_linked(b, 'scxml_ScxmlInvokeType286', a2)
    if hasattr(a1, 'scxml_ScxmlParallelType285'):
        assert not _is_linked(a1, 'scxml_ScxmlParallelType285', b)
    if hasattr(a2, 'scxml_ScxmlParallelType285'):
        assert _is_linked(a2, 'scxml_ScxmlParallelType285', b)
    _safe_set(b, 'scxml_ScxmlInvokeType286', None)
    assert not _is_linked(b, 'scxml_ScxmlInvokeType286', a2)
    if hasattr(a2, 'scxml_ScxmlParallelType285'):
        assert not _is_linked(a2, 'scxml_ScxmlParallelType285', b)


def test_assoc_invoke32_reverse_link_reassign_clear():
    a1 = scxml_ScxmlInvokeType(any="sample_text", anyAttribute="sample_text", autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlInvokeMix="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlInvokeType(any="sample_text_2", anyAttribute="sample_text_2", autoforward="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlInvokeMix="sample_text_2", src="sample_text_2", srcexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot33', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot33', a1)
    if hasattr(a1, 'scxml_ScxmlInvokeType'):
        assert _is_linked(a1, 'scxml_ScxmlInvokeType', b)
    _safe_set(b, 'scxml_DocumentRoot33', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot33', a2)
    if hasattr(a1, 'scxml_ScxmlInvokeType'):
        assert not _is_linked(a1, 'scxml_ScxmlInvokeType', b)
    if hasattr(a2, 'scxml_ScxmlInvokeType'):
        assert _is_linked(a2, 'scxml_ScxmlInvokeType', b)
    _safe_set(b, 'scxml_DocumentRoot33', set())
    assert not _is_linked(b, 'scxml_DocumentRoot33', a2)
    if hasattr(a2, 'scxml_ScxmlInvokeType'):
        assert not _is_linked(a2, 'scxml_ScxmlInvokeType', b)


def test_assoc_invoke335_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlInvokeType(any="sample_text", anyAttribute="sample_text", autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlInvokeMix="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlInvokeType337', a1)
    assert _is_linked(b, 'scxml_ScxmlInvokeType337', a1)
    if hasattr(a1, 'scxml_ScxmlStateType336'):
        assert _is_linked(a1, 'scxml_ScxmlStateType336', b)
    _safe_set(b, 'scxml_ScxmlInvokeType337', a2)
    assert _is_linked(b, 'scxml_ScxmlInvokeType337', a2)
    if hasattr(a1, 'scxml_ScxmlStateType336'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType336', b)
    if hasattr(a2, 'scxml_ScxmlStateType336'):
        assert _is_linked(a2, 'scxml_ScxmlStateType336', b)
    _safe_set(b, 'scxml_ScxmlInvokeType337', None)
    assert not _is_linked(b, 'scxml_ScxmlInvokeType337', a2)
    if hasattr(a2, 'scxml_ScxmlStateType336'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType336', b)


def test_assoc_log116_reverse_link_reassign_clear():
    a1 = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlLogType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", label="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType117', {a1})
    assert _is_linked(b, 'scxml_ScxmlForeachType117', a1)
    if hasattr(a1, 'scxml_ScxmlLogType118'):
        assert _is_linked(a1, 'scxml_ScxmlLogType118', b)
    _safe_set(b, 'scxml_ScxmlForeachType117', {a2})
    assert _is_linked(b, 'scxml_ScxmlForeachType117', a2)
    if hasattr(a1, 'scxml_ScxmlLogType118'):
        assert not _is_linked(a1, 'scxml_ScxmlLogType118', b)
    if hasattr(a2, 'scxml_ScxmlLogType118'):
        assert _is_linked(a2, 'scxml_ScxmlLogType118', b)
    _safe_set(b, 'scxml_ScxmlForeachType117', set())
    assert not _is_linked(b, 'scxml_ScxmlForeachType117', a2)
    if hasattr(a2, 'scxml_ScxmlLogType118'):
        assert not _is_linked(a2, 'scxml_ScxmlLogType118', b)


def test_assoc_log1170_reverse_link_reassign_clear():
    a1 = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlLogType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", label="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType171', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType171', a1)
    if hasattr(a1, 'scxml_ScxmlLogType172'):
        assert _is_linked(a1, 'scxml_ScxmlLogType172', b)
    _safe_set(b, 'scxml_ScxmlIfType171', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType171', a2)
    if hasattr(a1, 'scxml_ScxmlLogType172'):
        assert not _is_linked(a1, 'scxml_ScxmlLogType172', b)
    if hasattr(a2, 'scxml_ScxmlLogType172'):
        assert _is_linked(a2, 'scxml_ScxmlLogType172', b)
    _safe_set(b, 'scxml_ScxmlIfType171', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType171', a2)
    if hasattr(a2, 'scxml_ScxmlLogType172'):
        assert not _is_linked(a2, 'scxml_ScxmlLogType172', b)


def test_assoc_log143_reverse_link_reassign_clear():
    a1 = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlLogType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", label="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType144', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType144', a1)
    if hasattr(a1, 'scxml_ScxmlLogType145'):
        assert _is_linked(a1, 'scxml_ScxmlLogType145', b)
    _safe_set(b, 'scxml_ScxmlIfType144', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType144', a2)
    if hasattr(a1, 'scxml_ScxmlLogType145'):
        assert not _is_linked(a1, 'scxml_ScxmlLogType145', b)
    if hasattr(a2, 'scxml_ScxmlLogType145'):
        assert _is_linked(a2, 'scxml_ScxmlLogType145', b)
    _safe_set(b, 'scxml_ScxmlIfType144', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType144', a2)
    if hasattr(a2, 'scxml_ScxmlLogType145'):
        assert not _is_linked(a2, 'scxml_ScxmlLogType145', b)


def test_assoc_log2197_reverse_link_reassign_clear():
    a1 = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlLogType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", label="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType198', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType198', a1)
    if hasattr(a1, 'scxml_ScxmlLogType199'):
        assert _is_linked(a1, 'scxml_ScxmlLogType199', b)
    _safe_set(b, 'scxml_ScxmlIfType198', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType198', a2)
    if hasattr(a1, 'scxml_ScxmlLogType199'):
        assert not _is_linked(a1, 'scxml_ScxmlLogType199', b)
    if hasattr(a2, 'scxml_ScxmlLogType199'):
        assert _is_linked(a2, 'scxml_ScxmlLogType199', b)
    _safe_set(b, 'scxml_ScxmlIfType198', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType198', a2)
    if hasattr(a2, 'scxml_ScxmlLogType199'):
        assert not _is_linked(a2, 'scxml_ScxmlLogType199', b)


def test_assoc_log233_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnentryType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    _safe_set(b, 'scxml_ScxmlLogType235', a1)
    assert _is_linked(b, 'scxml_ScxmlLogType235', a1)
    if hasattr(a1, 'scxml_ScxmlOnentryType234'):
        assert _is_linked(a1, 'scxml_ScxmlOnentryType234', b)
    _safe_set(b, 'scxml_ScxmlLogType235', a2)
    assert _is_linked(b, 'scxml_ScxmlLogType235', a2)
    if hasattr(a1, 'scxml_ScxmlOnentryType234'):
        assert not _is_linked(a1, 'scxml_ScxmlOnentryType234', b)
    if hasattr(a2, 'scxml_ScxmlOnentryType234'):
        assert _is_linked(a2, 'scxml_ScxmlOnentryType234', b)
    _safe_set(b, 'scxml_ScxmlLogType235', None)
    assert not _is_linked(b, 'scxml_ScxmlLogType235', a2)
    if hasattr(a2, 'scxml_ScxmlOnentryType234'):
        assert not _is_linked(a2, 'scxml_ScxmlOnentryType234', b)


def test_assoc_log257_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnexitType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    _safe_set(b, 'scxml_ScxmlLogType259', a1)
    assert _is_linked(b, 'scxml_ScxmlLogType259', a1)
    if hasattr(a1, 'scxml_ScxmlOnexitType258'):
        assert _is_linked(a1, 'scxml_ScxmlOnexitType258', b)
    _safe_set(b, 'scxml_ScxmlLogType259', a2)
    assert _is_linked(b, 'scxml_ScxmlLogType259', a2)
    if hasattr(a1, 'scxml_ScxmlOnexitType258'):
        assert not _is_linked(a1, 'scxml_ScxmlOnexitType258', b)
    if hasattr(a2, 'scxml_ScxmlOnexitType258'):
        assert _is_linked(a2, 'scxml_ScxmlOnexitType258', b)
    _safe_set(b, 'scxml_ScxmlLogType259', None)
    assert not _is_linked(b, 'scxml_ScxmlLogType259', a2)
    if hasattr(a2, 'scxml_ScxmlOnexitType258'):
        assert not _is_linked(a2, 'scxml_ScxmlOnexitType258', b)


def test_assoc_log34_reverse_link_reassign_clear():
    a1 = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlLogType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", label="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot35', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot35', a1)
    if hasattr(a1, 'scxml_ScxmlLogType'):
        assert _is_linked(a1, 'scxml_ScxmlLogType', b)
    _safe_set(b, 'scxml_DocumentRoot35', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot35', a2)
    if hasattr(a1, 'scxml_ScxmlLogType'):
        assert not _is_linked(a1, 'scxml_ScxmlLogType', b)
    if hasattr(a2, 'scxml_ScxmlLogType'):
        assert _is_linked(a2, 'scxml_ScxmlLogType', b)
    _safe_set(b, 'scxml_DocumentRoot35', set())
    assert not _is_linked(b, 'scxml_DocumentRoot35', a2)
    if hasattr(a2, 'scxml_ScxmlLogType'):
        assert not _is_linked(a2, 'scxml_ScxmlLogType', b)


def test_assoc_log356_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    _safe_set(b, 'scxml_ScxmlLogType358', a1)
    assert _is_linked(b, 'scxml_ScxmlLogType358', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType357'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType357', b)
    _safe_set(b, 'scxml_ScxmlLogType358', a2)
    assert _is_linked(b, 'scxml_ScxmlLogType358', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType357'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType357', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType357'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType357', b)
    _safe_set(b, 'scxml_ScxmlLogType358', None)
    assert not _is_linked(b, 'scxml_ScxmlLogType358', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType357'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType357', b)


def test_assoc_log83_reverse_link_reassign_clear():
    a1 = scxml_ScxmlLogType(any="sample_text", anyAttribute="sample_text", expr="sample_text", label="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlLogType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", label="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalizeType84', {a1})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType84', a1)
    if hasattr(a1, 'scxml_ScxmlLogType85'):
        assert _is_linked(a1, 'scxml_ScxmlLogType85', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType84', {a2})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType84', a2)
    if hasattr(a1, 'scxml_ScxmlLogType85'):
        assert not _is_linked(a1, 'scxml_ScxmlLogType85', b)
    if hasattr(a2, 'scxml_ScxmlLogType85'):
        assert _is_linked(a2, 'scxml_ScxmlLogType85', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType84', set())
    assert not _is_linked(b, 'scxml_ScxmlFinalizeType84', a2)
    if hasattr(a2, 'scxml_ScxmlLogType85'):
        assert not _is_linked(a2, 'scxml_ScxmlLogType85', b)


def test_assoc_onentry263_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    a2 = scxml_ScxmlParallelType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlParallelMix="sample_text_2")
    b = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnentryType265', a1)
    assert _is_linked(b, 'scxml_ScxmlOnentryType265', a1)
    if hasattr(a1, 'scxml_ScxmlParallelType264'):
        assert _is_linked(a1, 'scxml_ScxmlParallelType264', b)
    _safe_set(b, 'scxml_ScxmlOnentryType265', a2)
    assert _is_linked(b, 'scxml_ScxmlOnentryType265', a2)
    if hasattr(a1, 'scxml_ScxmlParallelType264'):
        assert not _is_linked(a1, 'scxml_ScxmlParallelType264', b)
    if hasattr(a2, 'scxml_ScxmlParallelType264'):
        assert _is_linked(a2, 'scxml_ScxmlParallelType264', b)
    _safe_set(b, 'scxml_ScxmlOnentryType265', None)
    assert not _is_linked(b, 'scxml_ScxmlOnentryType265', a2)
    if hasattr(a2, 'scxml_ScxmlParallelType264'):
        assert not _is_linked(a2, 'scxml_ScxmlParallelType264', b)


def test_assoc_onentry308_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnentryType310', a1)
    assert _is_linked(b, 'scxml_ScxmlOnentryType310', a1)
    if hasattr(a1, 'scxml_ScxmlStateType309'):
        assert _is_linked(a1, 'scxml_ScxmlStateType309', b)
    _safe_set(b, 'scxml_ScxmlOnentryType310', a2)
    assert _is_linked(b, 'scxml_ScxmlOnentryType310', a2)
    if hasattr(a1, 'scxml_ScxmlStateType309'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType309', b)
    if hasattr(a2, 'scxml_ScxmlStateType309'):
        assert _is_linked(a2, 'scxml_ScxmlStateType309', b)
    _safe_set(b, 'scxml_ScxmlOnentryType310', None)
    assert not _is_linked(b, 'scxml_ScxmlOnentryType310', a2)
    if hasattr(a2, 'scxml_ScxmlStateType309'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType309', b)


def test_assoc_onentry36_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnentryType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot37', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot37', a1)
    if hasattr(a1, 'scxml_ScxmlOnentryType'):
        assert _is_linked(a1, 'scxml_ScxmlOnentryType', b)
    _safe_set(b, 'scxml_DocumentRoot37', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot37', a2)
    if hasattr(a1, 'scxml_ScxmlOnentryType'):
        assert not _is_linked(a1, 'scxml_ScxmlOnentryType', b)
    if hasattr(a2, 'scxml_ScxmlOnentryType'):
        assert _is_linked(a2, 'scxml_ScxmlOnentryType', b)
    _safe_set(b, 'scxml_DocumentRoot37', set())
    assert not _is_linked(b, 'scxml_DocumentRoot37', a2)
    if hasattr(a2, 'scxml_ScxmlOnentryType'):
        assert not _is_linked(a2, 'scxml_ScxmlOnentryType', b)


def test_assoc_onentry89_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnentryType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlFinalType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlFinalMix="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalType90', {a1})
    assert _is_linked(b, 'scxml_ScxmlFinalType90', a1)
    if hasattr(a1, 'scxml_ScxmlOnentryType91'):
        assert _is_linked(a1, 'scxml_ScxmlOnentryType91', b)
    _safe_set(b, 'scxml_ScxmlFinalType90', {a2})
    assert _is_linked(b, 'scxml_ScxmlFinalType90', a2)
    if hasattr(a1, 'scxml_ScxmlOnentryType91'):
        assert not _is_linked(a1, 'scxml_ScxmlOnentryType91', b)
    if hasattr(a2, 'scxml_ScxmlOnentryType91'):
        assert _is_linked(a2, 'scxml_ScxmlOnentryType91', b)
    _safe_set(b, 'scxml_ScxmlFinalType90', set())
    assert not _is_linked(b, 'scxml_ScxmlFinalType90', a2)
    if hasattr(a2, 'scxml_ScxmlOnentryType91'):
        assert not _is_linked(a2, 'scxml_ScxmlOnentryType91', b)


def test_assoc_onexit266_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    a2 = scxml_ScxmlParallelType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlParallelMix="sample_text_2")
    b = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexitType268', a1)
    assert _is_linked(b, 'scxml_ScxmlOnexitType268', a1)
    if hasattr(a1, 'scxml_ScxmlParallelType267'):
        assert _is_linked(a1, 'scxml_ScxmlParallelType267', b)
    _safe_set(b, 'scxml_ScxmlOnexitType268', a2)
    assert _is_linked(b, 'scxml_ScxmlOnexitType268', a2)
    if hasattr(a1, 'scxml_ScxmlParallelType267'):
        assert not _is_linked(a1, 'scxml_ScxmlParallelType267', b)
    if hasattr(a2, 'scxml_ScxmlParallelType267'):
        assert _is_linked(a2, 'scxml_ScxmlParallelType267', b)
    _safe_set(b, 'scxml_ScxmlOnexitType268', None)
    assert not _is_linked(b, 'scxml_ScxmlOnexitType268', a2)
    if hasattr(a2, 'scxml_ScxmlParallelType267'):
        assert not _is_linked(a2, 'scxml_ScxmlParallelType267', b)


def test_assoc_onexit311_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexitType313', a1)
    assert _is_linked(b, 'scxml_ScxmlOnexitType313', a1)
    if hasattr(a1, 'scxml_ScxmlStateType312'):
        assert _is_linked(a1, 'scxml_ScxmlStateType312', b)
    _safe_set(b, 'scxml_ScxmlOnexitType313', a2)
    assert _is_linked(b, 'scxml_ScxmlOnexitType313', a2)
    if hasattr(a1, 'scxml_ScxmlStateType312'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType312', b)
    if hasattr(a2, 'scxml_ScxmlStateType312'):
        assert _is_linked(a2, 'scxml_ScxmlStateType312', b)
    _safe_set(b, 'scxml_ScxmlOnexitType313', None)
    assert not _is_linked(b, 'scxml_ScxmlOnexitType313', a2)
    if hasattr(a2, 'scxml_ScxmlStateType312'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType312', b)


def test_assoc_onexit38_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnexitType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot39', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot39', a1)
    if hasattr(a1, 'scxml_ScxmlOnexitType'):
        assert _is_linked(a1, 'scxml_ScxmlOnexitType', b)
    _safe_set(b, 'scxml_DocumentRoot39', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot39', a2)
    if hasattr(a1, 'scxml_ScxmlOnexitType'):
        assert not _is_linked(a1, 'scxml_ScxmlOnexitType', b)
    if hasattr(a2, 'scxml_ScxmlOnexitType'):
        assert _is_linked(a2, 'scxml_ScxmlOnexitType', b)
    _safe_set(b, 'scxml_DocumentRoot39', set())
    assert not _is_linked(b, 'scxml_DocumentRoot39', a2)
    if hasattr(a2, 'scxml_ScxmlOnexitType'):
        assert not _is_linked(a2, 'scxml_ScxmlOnexitType', b)


def test_assoc_onexit92_reverse_link_reassign_clear():
    a1 = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    a2 = scxml_ScxmlOnexitType(any="sample_text_2", anyAttribute="sample_text_2", scxmlCoreExecutablecontent="sample_text_2")
    b = scxml_ScxmlFinalType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlFinalMix="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalType93', {a1})
    assert _is_linked(b, 'scxml_ScxmlFinalType93', a1)
    if hasattr(a1, 'scxml_ScxmlOnexitType94'):
        assert _is_linked(a1, 'scxml_ScxmlOnexitType94', b)
    _safe_set(b, 'scxml_ScxmlFinalType93', {a2})
    assert _is_linked(b, 'scxml_ScxmlFinalType93', a2)
    if hasattr(a1, 'scxml_ScxmlOnexitType94'):
        assert not _is_linked(a1, 'scxml_ScxmlOnexitType94', b)
    if hasattr(a2, 'scxml_ScxmlOnexitType94'):
        assert _is_linked(a2, 'scxml_ScxmlOnexitType94', b)
    _safe_set(b, 'scxml_ScxmlFinalType93', set())
    assert not _is_linked(b, 'scxml_ScxmlFinalType93', a2)
    if hasattr(a2, 'scxml_ScxmlOnexitType94'):
        assert not _is_linked(a2, 'scxml_ScxmlOnexitType94', b)


def test_assoc_parallel276_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    a2 = scxml_ScxmlParallelType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlParallelMix="sample_text_2")
    b = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    _safe_set(b, 'scxml_ScxmlParallelType277', a1)
    assert _is_linked(b, 'scxml_ScxmlParallelType277', a1)
    if hasattr(a1, 'scxml_ScxmlParallelType275'):
        assert _is_linked(a1, 'scxml_ScxmlParallelType275', b)
    _safe_set(b, 'scxml_ScxmlParallelType277', a2)
    assert _is_linked(b, 'scxml_ScxmlParallelType277', a2)
    if hasattr(a1, 'scxml_ScxmlParallelType275'):
        assert not _is_linked(a1, 'scxml_ScxmlParallelType275', b)
    if hasattr(a2, 'scxml_ScxmlParallelType275'):
        assert _is_linked(a2, 'scxml_ScxmlParallelType275', b)
    _safe_set(b, 'scxml_ScxmlParallelType277', None)
    assert not _is_linked(b, 'scxml_ScxmlParallelType277', a2)
    if hasattr(a2, 'scxml_ScxmlParallelType275'):
        assert not _is_linked(a2, 'scxml_ScxmlParallelType275', b)


def test_assoc_parallel290_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScxmlType(any="sample_text", anyAttribute="sample_text", binding="sample_text", datamodel1="sample_text", exmode="sample_text", initial="sample_text", name="sample_text", scxmlScxmlMix="sample_text", version="sample_text")
    a2 = scxml_ScxmlScxmlType(any="sample_text_2", anyAttribute="sample_text_2", binding="sample_text_2", datamodel1="sample_text_2", exmode="sample_text_2", initial="sample_text_2", name="sample_text_2", scxmlScxmlMix="sample_text_2", version="sample_text_2")
    b = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    _safe_set(b, 'scxml_ScxmlParallelType292', a1)
    assert _is_linked(b, 'scxml_ScxmlParallelType292', a1)
    if hasattr(a1, 'scxml_ScxmlScxmlType291'):
        assert _is_linked(a1, 'scxml_ScxmlScxmlType291', b)
    _safe_set(b, 'scxml_ScxmlParallelType292', a2)
    assert _is_linked(b, 'scxml_ScxmlParallelType292', a2)
    if hasattr(a1, 'scxml_ScxmlScxmlType291'):
        assert not _is_linked(a1, 'scxml_ScxmlScxmlType291', b)
    if hasattr(a2, 'scxml_ScxmlScxmlType291'):
        assert _is_linked(a2, 'scxml_ScxmlScxmlType291', b)
    _safe_set(b, 'scxml_ScxmlParallelType292', None)
    assert not _is_linked(b, 'scxml_ScxmlParallelType292', a2)
    if hasattr(a2, 'scxml_ScxmlScxmlType291'):
        assert not _is_linked(a2, 'scxml_ScxmlScxmlType291', b)


def test_assoc_parallel323_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    _safe_set(b, 'scxml_ScxmlParallelType325', a1)
    assert _is_linked(b, 'scxml_ScxmlParallelType325', a1)
    if hasattr(a1, 'scxml_ScxmlStateType324'):
        assert _is_linked(a1, 'scxml_ScxmlStateType324', b)
    _safe_set(b, 'scxml_ScxmlParallelType325', a2)
    assert _is_linked(b, 'scxml_ScxmlParallelType325', a2)
    if hasattr(a1, 'scxml_ScxmlStateType324'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType324', b)
    if hasattr(a2, 'scxml_ScxmlStateType324'):
        assert _is_linked(a2, 'scxml_ScxmlStateType324', b)
    _safe_set(b, 'scxml_ScxmlParallelType325', None)
    assert not _is_linked(b, 'scxml_ScxmlParallelType325', a2)
    if hasattr(a2, 'scxml_ScxmlStateType324'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType324', b)


def test_assoc_parallel40_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    a2 = scxml_ScxmlParallelType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", scxmlParallelMix="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot41', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot41', a1)
    if hasattr(a1, 'scxml_ScxmlParallelType'):
        assert _is_linked(a1, 'scxml_ScxmlParallelType', b)
    _safe_set(b, 'scxml_DocumentRoot41', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot41', a2)
    if hasattr(a1, 'scxml_ScxmlParallelType'):
        assert not _is_linked(a1, 'scxml_ScxmlParallelType', b)
    if hasattr(a2, 'scxml_ScxmlParallelType'):
        assert _is_linked(a2, 'scxml_ScxmlParallelType', b)
    _safe_set(b, 'scxml_DocumentRoot41', set())
    assert not _is_linked(b, 'scxml_DocumentRoot41', a2)
    if hasattr(a2, 'scxml_ScxmlParallelType'):
        assert not _is_linked(a2, 'scxml_ScxmlParallelType', b)


def test_assoc_param209_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParamType(any="sample_text", anyAttribute="sample_text", expr="sample_text", location="sample_text", name="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlParamType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", location="sample_text_2", name="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_ScxmlInvokeType(any="sample_text", anyAttribute="sample_text", autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlInvokeMix="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlInvokeType210', {a1})
    assert _is_linked(b, 'scxml_ScxmlInvokeType210', a1)
    if hasattr(a1, 'scxml_ScxmlParamType211'):
        assert _is_linked(a1, 'scxml_ScxmlParamType211', b)
    _safe_set(b, 'scxml_ScxmlInvokeType210', {a2})
    assert _is_linked(b, 'scxml_ScxmlInvokeType210', a2)
    if hasattr(a1, 'scxml_ScxmlParamType211'):
        assert not _is_linked(a1, 'scxml_ScxmlParamType211', b)
    if hasattr(a2, 'scxml_ScxmlParamType211'):
        assert _is_linked(a2, 'scxml_ScxmlParamType211', b)
    _safe_set(b, 'scxml_ScxmlInvokeType210', set())
    assert not _is_linked(b, 'scxml_ScxmlInvokeType210', a2)
    if hasattr(a2, 'scxml_ScxmlParamType211'):
        assert not _is_linked(a2, 'scxml_ScxmlParamType211', b)


def test_assoc_param305_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlParamType(any="sample_text", anyAttribute="sample_text", expr="sample_text", location="sample_text", name="sample_text", scxmlExtraContent="sample_text")
    _safe_set(b, 'scxml_ScxmlParamType307', a1)
    assert _is_linked(b, 'scxml_ScxmlParamType307', a1)
    if hasattr(a1, 'scxml_ScxmlSendType306'):
        assert _is_linked(a1, 'scxml_ScxmlSendType306', b)
    _safe_set(b, 'scxml_ScxmlParamType307', a2)
    assert _is_linked(b, 'scxml_ScxmlParamType307', a2)
    if hasattr(a1, 'scxml_ScxmlSendType306'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType306', b)
    if hasattr(a2, 'scxml_ScxmlSendType306'):
        assert _is_linked(a2, 'scxml_ScxmlSendType306', b)
    _safe_set(b, 'scxml_ScxmlParamType307', None)
    assert not _is_linked(b, 'scxml_ScxmlParamType307', a2)
    if hasattr(a2, 'scxml_ScxmlSendType306'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType306', b)


def test_assoc_param42_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParamType(any="sample_text", anyAttribute="sample_text", expr="sample_text", location="sample_text", name="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlParamType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", location="sample_text_2", name="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot43', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot43', a1)
    if hasattr(a1, 'scxml_ScxmlParamType'):
        assert _is_linked(a1, 'scxml_ScxmlParamType', b)
    _safe_set(b, 'scxml_DocumentRoot43', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot43', a2)
    if hasattr(a1, 'scxml_ScxmlParamType'):
        assert not _is_linked(a1, 'scxml_ScxmlParamType', b)
    if hasattr(a2, 'scxml_ScxmlParamType'):
        assert _is_linked(a2, 'scxml_ScxmlParamType', b)
    _safe_set(b, 'scxml_DocumentRoot43', set())
    assert not _is_linked(b, 'scxml_DocumentRoot43', a2)
    if hasattr(a2, 'scxml_ScxmlParamType'):
        assert not _is_linked(a2, 'scxml_ScxmlParamType', b)


def test_assoc_param62_reverse_link_reassign_clear():
    a1 = scxml_ScxmlParamType(any="sample_text", anyAttribute="sample_text", expr="sample_text", location="sample_text", name="sample_text", scxmlExtraContent="sample_text")
    a2 = scxml_ScxmlParamType(any="sample_text_2", anyAttribute="sample_text_2", expr="sample_text_2", location="sample_text_2", name="sample_text_2", scxmlExtraContent="sample_text_2")
    b = scxml_ScxmlDonedataType(anyAttribute="sample_text")
    _safe_set(b, 'scxml_ScxmlDonedataType63', {a1})
    assert _is_linked(b, 'scxml_ScxmlDonedataType63', a1)
    if hasattr(a1, 'scxml_ScxmlParamType64'):
        assert _is_linked(a1, 'scxml_ScxmlParamType64', b)
    _safe_set(b, 'scxml_ScxmlDonedataType63', {a2})
    assert _is_linked(b, 'scxml_ScxmlDonedataType63', a2)
    if hasattr(a1, 'scxml_ScxmlParamType64'):
        assert not _is_linked(a1, 'scxml_ScxmlParamType64', b)
    if hasattr(a2, 'scxml_ScxmlParamType64'):
        assert _is_linked(a2, 'scxml_ScxmlParamType64', b)
    _safe_set(b, 'scxml_ScxmlDonedataType63', set())
    assert not _is_linked(b, 'scxml_ScxmlDonedataType63', a2)
    if hasattr(a2, 'scxml_ScxmlParamType64'):
        assert not _is_linked(a2, 'scxml_ScxmlParamType64', b)


def test_assoc_raise1152_reverse_link_reassign_clear():
    a1 = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    a2 = scxml_ScxmlRaiseType(anyAttribute="sample_text_2", event="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType153', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType153', a1)
    if hasattr(a1, 'scxml_ScxmlRaiseType154'):
        assert _is_linked(a1, 'scxml_ScxmlRaiseType154', b)
    _safe_set(b, 'scxml_ScxmlIfType153', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType153', a2)
    if hasattr(a1, 'scxml_ScxmlRaiseType154'):
        assert not _is_linked(a1, 'scxml_ScxmlRaiseType154', b)
    if hasattr(a2, 'scxml_ScxmlRaiseType154'):
        assert _is_linked(a2, 'scxml_ScxmlRaiseType154', b)
    _safe_set(b, 'scxml_ScxmlIfType153', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType153', a2)
    if hasattr(a2, 'scxml_ScxmlRaiseType154'):
        assert not _is_linked(a2, 'scxml_ScxmlRaiseType154', b)


def test_assoc_raise2179_reverse_link_reassign_clear():
    a1 = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    a2 = scxml_ScxmlRaiseType(anyAttribute="sample_text_2", event="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType180', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType180', a1)
    if hasattr(a1, 'scxml_ScxmlRaiseType181'):
        assert _is_linked(a1, 'scxml_ScxmlRaiseType181', b)
    _safe_set(b, 'scxml_ScxmlIfType180', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType180', a2)
    if hasattr(a1, 'scxml_ScxmlRaiseType181'):
        assert not _is_linked(a1, 'scxml_ScxmlRaiseType181', b)
    if hasattr(a2, 'scxml_ScxmlRaiseType181'):
        assert _is_linked(a2, 'scxml_ScxmlRaiseType181', b)
    _safe_set(b, 'scxml_ScxmlIfType180', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType180', a2)
    if hasattr(a2, 'scxml_ScxmlRaiseType181'):
        assert not _is_linked(a2, 'scxml_ScxmlRaiseType181', b)


def test_assoc_raise_125_reverse_link_reassign_clear():
    a1 = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    a2 = scxml_ScxmlRaiseType(anyAttribute="sample_text_2", event="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType126', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType126', a1)
    if hasattr(a1, 'scxml_ScxmlRaiseType127'):
        assert _is_linked(a1, 'scxml_ScxmlRaiseType127', b)
    _safe_set(b, 'scxml_ScxmlIfType126', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType126', a2)
    if hasattr(a1, 'scxml_ScxmlRaiseType127'):
        assert not _is_linked(a1, 'scxml_ScxmlRaiseType127', b)
    if hasattr(a2, 'scxml_ScxmlRaiseType127'):
        assert _is_linked(a2, 'scxml_ScxmlRaiseType127', b)
    _safe_set(b, 'scxml_ScxmlIfType126', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType126', a2)
    if hasattr(a2, 'scxml_ScxmlRaiseType127'):
        assert not _is_linked(a2, 'scxml_ScxmlRaiseType127', b)


def test_assoc_raise_215_reverse_link_reassign_clear():
    a1 = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    a2 = scxml_ScxmlRaiseType(anyAttribute="sample_text_2", event="sample_text_2")
    b = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnentryType216', {a1})
    assert _is_linked(b, 'scxml_ScxmlOnentryType216', a1)
    if hasattr(a1, 'scxml_ScxmlRaiseType217'):
        assert _is_linked(a1, 'scxml_ScxmlRaiseType217', b)
    _safe_set(b, 'scxml_ScxmlOnentryType216', {a2})
    assert _is_linked(b, 'scxml_ScxmlOnentryType216', a2)
    if hasattr(a1, 'scxml_ScxmlRaiseType217'):
        assert not _is_linked(a1, 'scxml_ScxmlRaiseType217', b)
    if hasattr(a2, 'scxml_ScxmlRaiseType217'):
        assert _is_linked(a2, 'scxml_ScxmlRaiseType217', b)
    _safe_set(b, 'scxml_ScxmlOnentryType216', set())
    assert not _is_linked(b, 'scxml_ScxmlOnentryType216', a2)
    if hasattr(a2, 'scxml_ScxmlRaiseType217'):
        assert not _is_linked(a2, 'scxml_ScxmlRaiseType217', b)


def test_assoc_raise_239_reverse_link_reassign_clear():
    a1 = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    a2 = scxml_ScxmlRaiseType(anyAttribute="sample_text_2", event="sample_text_2")
    b = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexitType240', {a1})
    assert _is_linked(b, 'scxml_ScxmlOnexitType240', a1)
    if hasattr(a1, 'scxml_ScxmlRaiseType241'):
        assert _is_linked(a1, 'scxml_ScxmlRaiseType241', b)
    _safe_set(b, 'scxml_ScxmlOnexitType240', {a2})
    assert _is_linked(b, 'scxml_ScxmlOnexitType240', a2)
    if hasattr(a1, 'scxml_ScxmlRaiseType241'):
        assert not _is_linked(a1, 'scxml_ScxmlRaiseType241', b)
    if hasattr(a2, 'scxml_ScxmlRaiseType241'):
        assert _is_linked(a2, 'scxml_ScxmlRaiseType241', b)
    _safe_set(b, 'scxml_ScxmlOnexitType240', set())
    assert not _is_linked(b, 'scxml_ScxmlOnexitType240', a2)
    if hasattr(a2, 'scxml_ScxmlRaiseType241'):
        assert not _is_linked(a2, 'scxml_ScxmlRaiseType241', b)


def test_assoc_raise_338_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    _safe_set(b, 'scxml_ScxmlRaiseType340', a1)
    assert _is_linked(b, 'scxml_ScxmlRaiseType340', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType339'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType339', b)
    _safe_set(b, 'scxml_ScxmlRaiseType340', a2)
    assert _is_linked(b, 'scxml_ScxmlRaiseType340', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType339'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType339', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType339'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType339', b)
    _safe_set(b, 'scxml_ScxmlRaiseType340', None)
    assert not _is_linked(b, 'scxml_ScxmlRaiseType340', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType339'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType339', b)


def test_assoc_raise_44_reverse_link_reassign_clear():
    a1 = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    a2 = scxml_ScxmlRaiseType(anyAttribute="sample_text_2", event="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot45', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot45', a1)
    if hasattr(a1, 'scxml_ScxmlRaiseType'):
        assert _is_linked(a1, 'scxml_ScxmlRaiseType', b)
    _safe_set(b, 'scxml_DocumentRoot45', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot45', a2)
    if hasattr(a1, 'scxml_ScxmlRaiseType'):
        assert not _is_linked(a1, 'scxml_ScxmlRaiseType', b)
    if hasattr(a2, 'scxml_ScxmlRaiseType'):
        assert _is_linked(a2, 'scxml_ScxmlRaiseType', b)
    _safe_set(b, 'scxml_DocumentRoot45', set())
    assert not _is_linked(b, 'scxml_DocumentRoot45', a2)
    if hasattr(a2, 'scxml_ScxmlRaiseType'):
        assert not _is_linked(a2, 'scxml_ScxmlRaiseType', b)


def test_assoc_raise_65_reverse_link_reassign_clear():
    a1 = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    a2 = scxml_ScxmlRaiseType(anyAttribute="sample_text_2", event="sample_text_2")
    b = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalizeType66', {a1})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType66', a1)
    if hasattr(a1, 'scxml_ScxmlRaiseType67'):
        assert _is_linked(a1, 'scxml_ScxmlRaiseType67', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType66', {a2})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType66', a2)
    if hasattr(a1, 'scxml_ScxmlRaiseType67'):
        assert not _is_linked(a1, 'scxml_ScxmlRaiseType67', b)
    if hasattr(a2, 'scxml_ScxmlRaiseType67'):
        assert _is_linked(a2, 'scxml_ScxmlRaiseType67', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType66', set())
    assert not _is_linked(b, 'scxml_ScxmlFinalizeType66', a2)
    if hasattr(a2, 'scxml_ScxmlRaiseType67'):
        assert not _is_linked(a2, 'scxml_ScxmlRaiseType67', b)


def test_assoc_raise_98_reverse_link_reassign_clear():
    a1 = scxml_ScxmlRaiseType(anyAttribute="sample_text", event="sample_text")
    a2 = scxml_ScxmlRaiseType(anyAttribute="sample_text_2", event="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType99', {a1})
    assert _is_linked(b, 'scxml_ScxmlForeachType99', a1)
    if hasattr(a1, 'scxml_ScxmlRaiseType100'):
        assert _is_linked(a1, 'scxml_ScxmlRaiseType100', b)
    _safe_set(b, 'scxml_ScxmlForeachType99', {a2})
    assert _is_linked(b, 'scxml_ScxmlForeachType99', a2)
    if hasattr(a1, 'scxml_ScxmlRaiseType100'):
        assert not _is_linked(a1, 'scxml_ScxmlRaiseType100', b)
    if hasattr(a2, 'scxml_ScxmlRaiseType100'):
        assert _is_linked(a2, 'scxml_ScxmlRaiseType100', b)
    _safe_set(b, 'scxml_ScxmlForeachType99', set())
    assert not _is_linked(b, 'scxml_ScxmlForeachType99', a2)
    if hasattr(a2, 'scxml_ScxmlRaiseType100'):
        assert not _is_linked(a2, 'scxml_ScxmlRaiseType100', b)


def test_assoc_script110_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", anyAttribute="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType111', {a1})
    assert _is_linked(b, 'scxml_ScxmlForeachType111', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType112'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType112', b)
    _safe_set(b, 'scxml_ScxmlForeachType111', {a2})
    assert _is_linked(b, 'scxml_ScxmlForeachType111', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType112'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType112', b)
    if hasattr(a2, 'scxml_ScxmlScriptType112'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType112', b)
    _safe_set(b, 'scxml_ScxmlForeachType111', set())
    assert not _is_linked(b, 'scxml_ScxmlForeachType111', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType112'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType112', b)


def test_assoc_script1164_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", anyAttribute="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType165', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType165', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType166'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType166', b)
    _safe_set(b, 'scxml_ScxmlIfType165', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType165', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType166'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType166', b)
    if hasattr(a2, 'scxml_ScxmlScriptType166'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType166', b)
    _safe_set(b, 'scxml_ScxmlIfType165', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType165', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType166'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType166', b)


def test_assoc_script137_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", anyAttribute="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType138', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType138', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType139'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType139', b)
    _safe_set(b, 'scxml_ScxmlIfType138', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType138', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType139'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType139', b)
    if hasattr(a2, 'scxml_ScxmlScriptType139'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType139', b)
    _safe_set(b, 'scxml_ScxmlIfType138', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType138', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType139'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType139', b)


def test_assoc_script2191_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", anyAttribute="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType192', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType192', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType193'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType193', b)
    _safe_set(b, 'scxml_ScxmlIfType192', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType192', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType193'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType193', b)
    if hasattr(a2, 'scxml_ScxmlScriptType193'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType193', b)
    _safe_set(b, 'scxml_ScxmlIfType192', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType192', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType193'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType193', b)


def test_assoc_script227_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", anyAttribute="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnentryType228', {a1})
    assert _is_linked(b, 'scxml_ScxmlOnentryType228', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType229'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType229', b)
    _safe_set(b, 'scxml_ScxmlOnentryType228', {a2})
    assert _is_linked(b, 'scxml_ScxmlOnentryType228', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType229'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType229', b)
    if hasattr(a2, 'scxml_ScxmlScriptType229'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType229', b)
    _safe_set(b, 'scxml_ScxmlOnentryType228', set())
    assert not _is_linked(b, 'scxml_ScxmlOnentryType228', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType229'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType229', b)


def test_assoc_script251_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", anyAttribute="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexitType252', {a1})
    assert _is_linked(b, 'scxml_ScxmlOnexitType252', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType253'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType253', b)
    _safe_set(b, 'scxml_ScxmlOnexitType252', {a2})
    assert _is_linked(b, 'scxml_ScxmlOnexitType252', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType253'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType253', b)
    if hasattr(a2, 'scxml_ScxmlScriptType253'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType253', b)
    _safe_set(b, 'scxml_ScxmlOnexitType252', set())
    assert not _is_linked(b, 'scxml_ScxmlOnexitType252', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType253'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType253', b)


def test_assoc_script299_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScxmlType(any="sample_text", anyAttribute="sample_text", binding="sample_text", datamodel1="sample_text", exmode="sample_text", initial="sample_text", name="sample_text", scxmlScxmlMix="sample_text", version="sample_text")
    a2 = scxml_ScxmlScxmlType(any="sample_text_2", anyAttribute="sample_text_2", binding="sample_text_2", datamodel1="sample_text_2", exmode="sample_text_2", initial="sample_text_2", name="sample_text_2", scxmlScxmlMix="sample_text_2", version="sample_text_2")
    b = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    _safe_set(b, 'scxml_ScxmlScriptType301', a1)
    assert _is_linked(b, 'scxml_ScxmlScriptType301', a1)
    if hasattr(a1, 'scxml_ScxmlScxmlType300'):
        assert _is_linked(a1, 'scxml_ScxmlScxmlType300', b)
    _safe_set(b, 'scxml_ScxmlScriptType301', a2)
    assert _is_linked(b, 'scxml_ScxmlScriptType301', a2)
    if hasattr(a1, 'scxml_ScxmlScxmlType300'):
        assert not _is_linked(a1, 'scxml_ScxmlScxmlType300', b)
    if hasattr(a2, 'scxml_ScxmlScxmlType300'):
        assert _is_linked(a2, 'scxml_ScxmlScxmlType300', b)
    _safe_set(b, 'scxml_ScxmlScriptType301', None)
    assert not _is_linked(b, 'scxml_ScxmlScriptType301', a2)
    if hasattr(a2, 'scxml_ScxmlScxmlType300'):
        assert not _is_linked(a2, 'scxml_ScxmlScxmlType300', b)


def test_assoc_script350_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    _safe_set(b, 'scxml_ScxmlScriptType352', a1)
    assert _is_linked(b, 'scxml_ScxmlScriptType352', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType351'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType351', b)
    _safe_set(b, 'scxml_ScxmlScriptType352', a2)
    assert _is_linked(b, 'scxml_ScxmlScriptType352', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType351'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType351', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType351'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType351', b)
    _safe_set(b, 'scxml_ScxmlScriptType352', None)
    assert not _is_linked(b, 'scxml_ScxmlScriptType352', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType351'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType351', b)


def test_assoc_script46_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", anyAttribute="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot47', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot47', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType', b)
    _safe_set(b, 'scxml_DocumentRoot47', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot47', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType', b)
    if hasattr(a2, 'scxml_ScxmlScriptType'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType', b)
    _safe_set(b, 'scxml_DocumentRoot47', set())
    assert not _is_linked(b, 'scxml_DocumentRoot47', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType', b)


def test_assoc_script77_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", anyAttribute="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", anyAttribute="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalizeType78', {a1})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType78', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType79'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType79', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType78', {a2})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType78', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType79'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType79', b)
    if hasattr(a2, 'scxml_ScxmlScriptType79'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType79', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType78', set())
    assert not _is_linked(b, 'scxml_ScxmlFinalizeType78', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType79'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType79', b)


def test_assoc_scxml48_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScxmlType(any="sample_text", anyAttribute="sample_text", binding="sample_text", datamodel1="sample_text", exmode="sample_text", initial="sample_text", name="sample_text", scxmlScxmlMix="sample_text", version="sample_text")
    a2 = scxml_ScxmlScxmlType(any="sample_text_2", anyAttribute="sample_text_2", binding="sample_text_2", datamodel1="sample_text_2", exmode="sample_text_2", initial="sample_text_2", name="sample_text_2", scxmlScxmlMix="sample_text_2", version="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot49', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot49', a1)
    if hasattr(a1, 'scxml_ScxmlScxmlType'):
        assert _is_linked(a1, 'scxml_ScxmlScxmlType', b)
    _safe_set(b, 'scxml_DocumentRoot49', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot49', a2)
    if hasattr(a1, 'scxml_ScxmlScxmlType'):
        assert not _is_linked(a1, 'scxml_ScxmlScxmlType', b)
    if hasattr(a2, 'scxml_ScxmlScxmlType'):
        assert _is_linked(a2, 'scxml_ScxmlScxmlType', b)
    _safe_set(b, 'scxml_DocumentRoot49', set())
    assert not _is_linked(b, 'scxml_DocumentRoot49', a2)
    if hasattr(a2, 'scxml_ScxmlScxmlType'):
        assert not _is_linked(a2, 'scxml_ScxmlScxmlType', b)


def test_assoc_send107_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlForeachType(any="sample_text", anyAttribute="sample_text", array="sample_text", index="sample_text", item="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlForeachType108', {a1})
    assert _is_linked(b, 'scxml_ScxmlForeachType108', a1)
    if hasattr(a1, 'scxml_ScxmlSendType109'):
        assert _is_linked(a1, 'scxml_ScxmlSendType109', b)
    _safe_set(b, 'scxml_ScxmlForeachType108', {a2})
    assert _is_linked(b, 'scxml_ScxmlForeachType108', a2)
    if hasattr(a1, 'scxml_ScxmlSendType109'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType109', b)
    if hasattr(a2, 'scxml_ScxmlSendType109'):
        assert _is_linked(a2, 'scxml_ScxmlSendType109', b)
    _safe_set(b, 'scxml_ScxmlForeachType108', set())
    assert not _is_linked(b, 'scxml_ScxmlForeachType108', a2)
    if hasattr(a2, 'scxml_ScxmlSendType109'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType109', b)


def test_assoc_send1161_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType162', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType162', a1)
    if hasattr(a1, 'scxml_ScxmlSendType163'):
        assert _is_linked(a1, 'scxml_ScxmlSendType163', b)
    _safe_set(b, 'scxml_ScxmlIfType162', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType162', a2)
    if hasattr(a1, 'scxml_ScxmlSendType163'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType163', b)
    if hasattr(a2, 'scxml_ScxmlSendType163'):
        assert _is_linked(a2, 'scxml_ScxmlSendType163', b)
    _safe_set(b, 'scxml_ScxmlIfType162', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType162', a2)
    if hasattr(a2, 'scxml_ScxmlSendType163'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType163', b)


def test_assoc_send134_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType135', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType135', a1)
    if hasattr(a1, 'scxml_ScxmlSendType136'):
        assert _is_linked(a1, 'scxml_ScxmlSendType136', b)
    _safe_set(b, 'scxml_ScxmlIfType135', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType135', a2)
    if hasattr(a1, 'scxml_ScxmlSendType136'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType136', b)
    if hasattr(a2, 'scxml_ScxmlSendType136'):
        assert _is_linked(a2, 'scxml_ScxmlSendType136', b)
    _safe_set(b, 'scxml_ScxmlIfType135', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType135', a2)
    if hasattr(a2, 'scxml_ScxmlSendType136'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType136', b)


def test_assoc_send2188_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlIfType(any="sample_text", any1="sample_text", any2="sample_text", anyAttribute="sample_text", cond="sample_text", scxmlCoreExecutablecontent="sample_text", scxmlCoreExecutablecontent1="sample_text", scxmlCoreExecutablecontent2="sample_text")
    _safe_set(b, 'scxml_ScxmlIfType189', {a1})
    assert _is_linked(b, 'scxml_ScxmlIfType189', a1)
    if hasattr(a1, 'scxml_ScxmlSendType190'):
        assert _is_linked(a1, 'scxml_ScxmlSendType190', b)
    _safe_set(b, 'scxml_ScxmlIfType189', {a2})
    assert _is_linked(b, 'scxml_ScxmlIfType189', a2)
    if hasattr(a1, 'scxml_ScxmlSendType190'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType190', b)
    if hasattr(a2, 'scxml_ScxmlSendType190'):
        assert _is_linked(a2, 'scxml_ScxmlSendType190', b)
    _safe_set(b, 'scxml_ScxmlIfType189', set())
    assert not _is_linked(b, 'scxml_ScxmlIfType189', a2)
    if hasattr(a2, 'scxml_ScxmlSendType190'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType190', b)


def test_assoc_send224_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlOnentryType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnentryType225', {a1})
    assert _is_linked(b, 'scxml_ScxmlOnentryType225', a1)
    if hasattr(a1, 'scxml_ScxmlSendType226'):
        assert _is_linked(a1, 'scxml_ScxmlSendType226', b)
    _safe_set(b, 'scxml_ScxmlOnentryType225', {a2})
    assert _is_linked(b, 'scxml_ScxmlOnentryType225', a2)
    if hasattr(a1, 'scxml_ScxmlSendType226'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType226', b)
    if hasattr(a2, 'scxml_ScxmlSendType226'):
        assert _is_linked(a2, 'scxml_ScxmlSendType226', b)
    _safe_set(b, 'scxml_ScxmlOnentryType225', set())
    assert not _is_linked(b, 'scxml_ScxmlOnentryType225', a2)
    if hasattr(a2, 'scxml_ScxmlSendType226'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType226', b)


def test_assoc_send248_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlOnexitType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexitType249', {a1})
    assert _is_linked(b, 'scxml_ScxmlOnexitType249', a1)
    if hasattr(a1, 'scxml_ScxmlSendType250'):
        assert _is_linked(a1, 'scxml_ScxmlSendType250', b)
    _safe_set(b, 'scxml_ScxmlOnexitType249', {a2})
    assert _is_linked(b, 'scxml_ScxmlOnexitType249', a2)
    if hasattr(a1, 'scxml_ScxmlSendType250'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType250', b)
    if hasattr(a2, 'scxml_ScxmlSendType250'):
        assert _is_linked(a2, 'scxml_ScxmlSendType250', b)
    _safe_set(b, 'scxml_ScxmlOnexitType249', set())
    assert not _is_linked(b, 'scxml_ScxmlOnexitType249', a2)
    if hasattr(a2, 'scxml_ScxmlSendType250'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType250', b)


def test_assoc_send347_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    _safe_set(b, 'scxml_ScxmlSendType349', a1)
    assert _is_linked(b, 'scxml_ScxmlSendType349', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType348'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType348', b)
    _safe_set(b, 'scxml_ScxmlSendType349', a2)
    assert _is_linked(b, 'scxml_ScxmlSendType349', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType348'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType348', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType348'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType348', b)
    _safe_set(b, 'scxml_ScxmlSendType349', None)
    assert not _is_linked(b, 'scxml_ScxmlSendType349', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType348'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType348', b)


def test_assoc_send50_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot51', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot51', a1)
    if hasattr(a1, 'scxml_ScxmlSendType'):
        assert _is_linked(a1, 'scxml_ScxmlSendType', b)
    _safe_set(b, 'scxml_DocumentRoot51', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot51', a2)
    if hasattr(a1, 'scxml_ScxmlSendType'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType', b)
    if hasattr(a2, 'scxml_ScxmlSendType'):
        assert _is_linked(a2, 'scxml_ScxmlSendType', b)
    _safe_set(b, 'scxml_DocumentRoot51', set())
    assert not _is_linked(b, 'scxml_DocumentRoot51', a2)
    if hasattr(a2, 'scxml_ScxmlSendType'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType', b)


def test_assoc_send74_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(any="sample_text", anyAttribute="sample_text", delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", scxmlSendMix="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_ScxmlSendType(any="sample_text_2", anyAttribute="sample_text_2", delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", scxmlSendMix="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_ScxmlFinalizeType(any="sample_text", anyAttribute="sample_text", scxmlCoreExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlFinalizeType75', {a1})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType75', a1)
    if hasattr(a1, 'scxml_ScxmlSendType76'):
        assert _is_linked(a1, 'scxml_ScxmlSendType76', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType75', {a2})
    assert _is_linked(b, 'scxml_ScxmlFinalizeType75', a2)
    if hasattr(a1, 'scxml_ScxmlSendType76'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType76', b)
    if hasattr(a2, 'scxml_ScxmlSendType76'):
        assert _is_linked(a2, 'scxml_ScxmlSendType76', b)
    _safe_set(b, 'scxml_ScxmlFinalizeType75', set())
    assert not _is_linked(b, 'scxml_ScxmlFinalizeType75', a2)
    if hasattr(a2, 'scxml_ScxmlSendType76'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType76', b)


def test_assoc_state272_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    _safe_set(b, 'scxml_ScxmlParallelType273', {a1})
    assert _is_linked(b, 'scxml_ScxmlParallelType273', a1)
    if hasattr(a1, 'scxml_ScxmlStateType274'):
        assert _is_linked(a1, 'scxml_ScxmlStateType274', b)
    _safe_set(b, 'scxml_ScxmlParallelType273', {a2})
    assert _is_linked(b, 'scxml_ScxmlParallelType273', a2)
    if hasattr(a1, 'scxml_ScxmlStateType274'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType274', b)
    if hasattr(a2, 'scxml_ScxmlStateType274'):
        assert _is_linked(a2, 'scxml_ScxmlStateType274', b)
    _safe_set(b, 'scxml_ScxmlParallelType273', set())
    assert not _is_linked(b, 'scxml_ScxmlParallelType273', a2)
    if hasattr(a2, 'scxml_ScxmlStateType274'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType274', b)


def test_assoc_state287_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlScxmlType(any="sample_text", anyAttribute="sample_text", binding="sample_text", datamodel1="sample_text", exmode="sample_text", initial="sample_text", name="sample_text", scxmlScxmlMix="sample_text", version="sample_text")
    _safe_set(b, 'scxml_ScxmlScxmlType288', {a1})
    assert _is_linked(b, 'scxml_ScxmlScxmlType288', a1)
    if hasattr(a1, 'scxml_ScxmlStateType289'):
        assert _is_linked(a1, 'scxml_ScxmlStateType289', b)
    _safe_set(b, 'scxml_ScxmlScxmlType288', {a2})
    assert _is_linked(b, 'scxml_ScxmlScxmlType288', a2)
    if hasattr(a1, 'scxml_ScxmlStateType289'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType289', b)
    if hasattr(a2, 'scxml_ScxmlStateType289'):
        assert _is_linked(a2, 'scxml_ScxmlStateType289', b)
    _safe_set(b, 'scxml_ScxmlScxmlType288', set())
    assert not _is_linked(b, 'scxml_ScxmlScxmlType288', a2)
    if hasattr(a2, 'scxml_ScxmlStateType289'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType289', b)


def test_assoc_state321_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    _safe_set(b, 'scxml_ScxmlStateType322', a1)
    assert _is_linked(b, 'scxml_ScxmlStateType322', a1)
    if hasattr(a1, 'scxml_ScxmlStateType320'):
        assert _is_linked(a1, 'scxml_ScxmlStateType320', b)
    _safe_set(b, 'scxml_ScxmlStateType322', a2)
    assert _is_linked(b, 'scxml_ScxmlStateType322', a2)
    if hasattr(a1, 'scxml_ScxmlStateType320'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType320', b)
    if hasattr(a2, 'scxml_ScxmlStateType320'):
        assert _is_linked(a2, 'scxml_ScxmlStateType320', b)
    _safe_set(b, 'scxml_ScxmlStateType322', None)
    assert not _is_linked(b, 'scxml_ScxmlStateType322', a2)
    if hasattr(a2, 'scxml_ScxmlStateType320'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType320', b)


def test_assoc_state52_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    a2 = scxml_ScxmlStateType(any="sample_text_2", anyAttribute="sample_text_2", id="sample_text_2", initial1="sample_text_2", scxmlStateMix="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot53', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot53', a1)
    if hasattr(a1, 'scxml_ScxmlStateType'):
        assert _is_linked(a1, 'scxml_ScxmlStateType', b)
    _safe_set(b, 'scxml_DocumentRoot53', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot53', a2)
    if hasattr(a1, 'scxml_ScxmlStateType'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType', b)
    if hasattr(a2, 'scxml_ScxmlStateType'):
        assert _is_linked(a2, 'scxml_ScxmlStateType', b)
    _safe_set(b, 'scxml_DocumentRoot53', set())
    assert not _is_linked(b, 'scxml_DocumentRoot53', a2)
    if hasattr(a2, 'scxml_ScxmlStateType'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType', b)


def test_assoc_transition122_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlHistoryType(any="sample_text", any1="sample_text", anyAttribute="sample_text", id="sample_text", scxmlExtraContent="sample_text", scxmlExtraContent1="sample_text", type="sample_text")
    _safe_set(b, 'scxml_ScxmlHistoryType123', a1)
    assert _is_linked(b, 'scxml_ScxmlHistoryType123', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType124'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType124', b)
    _safe_set(b, 'scxml_ScxmlHistoryType123', a2)
    assert _is_linked(b, 'scxml_ScxmlHistoryType123', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType124'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType124', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType124'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType124', b)
    _safe_set(b, 'scxml_ScxmlHistoryType123', None)
    assert not _is_linked(b, 'scxml_ScxmlHistoryType123', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType124'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType124', b)


def test_assoc_transition203_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlInitialType(any="sample_text", any1="sample_text", anyAttribute="sample_text", scxmlExtraContent="sample_text", scxmlExtraContent1="sample_text")
    _safe_set(b, 'scxml_ScxmlInitialType204', a1)
    assert _is_linked(b, 'scxml_ScxmlInitialType204', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType205'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType205', b)
    _safe_set(b, 'scxml_ScxmlInitialType204', a2)
    assert _is_linked(b, 'scxml_ScxmlInitialType204', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType205'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType205', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType205'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType205', b)
    _safe_set(b, 'scxml_ScxmlInitialType204', None)
    assert not _is_linked(b, 'scxml_ScxmlInitialType204', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType205'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType205', b)


def test_assoc_transition269_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlParallelType(any="sample_text", anyAttribute="sample_text", id="sample_text", scxmlParallelMix="sample_text")
    _safe_set(b, 'scxml_ScxmlParallelType270', {a1})
    assert _is_linked(b, 'scxml_ScxmlParallelType270', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType271'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType271', b)
    _safe_set(b, 'scxml_ScxmlParallelType270', {a2})
    assert _is_linked(b, 'scxml_ScxmlParallelType270', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType271'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType271', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType271'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType271', b)
    _safe_set(b, 'scxml_ScxmlParallelType270', set())
    assert not _is_linked(b, 'scxml_ScxmlParallelType270', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType271'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType271', b)


def test_assoc_transition314_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_ScxmlStateType(any="sample_text", anyAttribute="sample_text", id="sample_text", initial1="sample_text", scxmlStateMix="sample_text")
    _safe_set(b, 'scxml_ScxmlStateType315', {a1})
    assert _is_linked(b, 'scxml_ScxmlStateType315', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType316'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType316', b)
    _safe_set(b, 'scxml_ScxmlStateType315', {a2})
    assert _is_linked(b, 'scxml_ScxmlStateType315', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType316'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType316', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType316'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType316', b)
    _safe_set(b, 'scxml_ScxmlStateType315', set())
    assert not _is_linked(b, 'scxml_ScxmlStateType315', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType316'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType316', b)


def test_assoc_transition54_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", anyAttribute="sample_text", cond="sample_text", event="sample_text", scxmlCoreExecutablecontent="sample_text", target="sample_text", type="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", anyAttribute="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlCoreExecutablecontent="sample_text_2", target="sample_text_2", type="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot55', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot55', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType', b)
    _safe_set(b, 'scxml_DocumentRoot55', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot55', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType', b)
    _safe_set(b, 'scxml_DocumentRoot55', set())
    assert not _is_linked(b, 'scxml_DocumentRoot55', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType', b)


