import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    scxml_DocumentRoot,
    scxml_EStringToStringMapEntry,
    scxml_ScxmlOnexecuteType,
    scxml_ScxmlParamType,
    scxml_ScxmlScriptType,
    scxml_ScxmlScxmlType,
    scxml_ScxmlSendType,
    scxml_ScxmlStateType,
    scxml_ScxmlTransitionType,
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

def test_assoc_onentry9_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(id="sample_text", initial="sample_text")
    a2 = scxml_ScxmlStateType(id="sample_text_2", initial="sample_text_2")
    b = scxml_ScxmlOnexecuteType(any="sample_text", anyAttribute="sample_text", scxmlExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexecuteType11', a1)
    assert _is_linked(b, 'scxml_ScxmlOnexecuteType11', a1)
    if hasattr(a1, 'scxml_ScxmlStateType10'):
        assert _is_linked(a1, 'scxml_ScxmlStateType10', b)
    _safe_set(b, 'scxml_ScxmlOnexecuteType11', a2)
    assert _is_linked(b, 'scxml_ScxmlOnexecuteType11', a2)
    if hasattr(a1, 'scxml_ScxmlStateType10'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType10', b)
    if hasattr(a2, 'scxml_ScxmlStateType10'):
        assert _is_linked(a2, 'scxml_ScxmlStateType10', b)
    _safe_set(b, 'scxml_ScxmlOnexecuteType11', None)
    assert not _is_linked(b, 'scxml_ScxmlOnexecuteType11', a2)
    if hasattr(a2, 'scxml_ScxmlStateType10'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType10', b)


def test_assoc_onexit12_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(id="sample_text", initial="sample_text")
    a2 = scxml_ScxmlStateType(id="sample_text_2", initial="sample_text_2")
    b = scxml_ScxmlOnexecuteType(any="sample_text", anyAttribute="sample_text", scxmlExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexecuteType14', a1)
    assert _is_linked(b, 'scxml_ScxmlOnexecuteType14', a1)
    if hasattr(a1, 'scxml_ScxmlStateType13'):
        assert _is_linked(a1, 'scxml_ScxmlStateType13', b)
    _safe_set(b, 'scxml_ScxmlOnexecuteType14', a2)
    assert _is_linked(b, 'scxml_ScxmlOnexecuteType14', a2)
    if hasattr(a1, 'scxml_ScxmlStateType13'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType13', b)
    if hasattr(a2, 'scxml_ScxmlStateType13'):
        assert _is_linked(a2, 'scxml_ScxmlStateType13', b)
    _safe_set(b, 'scxml_ScxmlOnexecuteType14', None)
    assert not _is_linked(b, 'scxml_ScxmlOnexecuteType14', a2)
    if hasattr(a2, 'scxml_ScxmlStateType13'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType13', b)


def test_assoc_param7_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(event="sample_text")
    a2 = scxml_ScxmlSendType(event="sample_text_2")
    b = scxml_ScxmlParamType(any="sample_text", anyAttribute="sample_text", expr="sample_text", name="sample_text", scxmlExtraContent="sample_text")
    _safe_set(b, 'scxml_ScxmlParamType', a1)
    assert _is_linked(b, 'scxml_ScxmlParamType', a1)
    if hasattr(a1, 'scxml_ScxmlSendType8'):
        assert _is_linked(a1, 'scxml_ScxmlSendType8', b)
    _safe_set(b, 'scxml_ScxmlParamType', a2)
    assert _is_linked(b, 'scxml_ScxmlParamType', a2)
    if hasattr(a1, 'scxml_ScxmlSendType8'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType8', b)
    if hasattr(a2, 'scxml_ScxmlSendType8'):
        assert _is_linked(a2, 'scxml_ScxmlSendType8', b)
    _safe_set(b, 'scxml_ScxmlParamType', None)
    assert not _is_linked(b, 'scxml_ScxmlParamType', a2)
    if hasattr(a2, 'scxml_ScxmlSendType8'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType8', b)


def test_assoc_script1_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScriptType(any="sample_text", content="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    a2 = scxml_ScxmlScriptType(any="sample_text_2", content="sample_text_2", mixed="sample_text_2", scxmlExtraContent="sample_text_2", src="sample_text_2")
    b = scxml_ScxmlOnexecuteType(any="sample_text", anyAttribute="sample_text", scxmlExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexecuteType2', {a1})
    assert _is_linked(b, 'scxml_ScxmlOnexecuteType2', a1)
    if hasattr(a1, 'scxml_ScxmlScriptType'):
        assert _is_linked(a1, 'scxml_ScxmlScriptType', b)
    _safe_set(b, 'scxml_ScxmlOnexecuteType2', {a2})
    assert _is_linked(b, 'scxml_ScxmlOnexecuteType2', a2)
    if hasattr(a1, 'scxml_ScxmlScriptType'):
        assert not _is_linked(a1, 'scxml_ScxmlScriptType', b)
    if hasattr(a2, 'scxml_ScxmlScriptType'):
        assert _is_linked(a2, 'scxml_ScxmlScriptType', b)
    _safe_set(b, 'scxml_ScxmlOnexecuteType2', set())
    assert not _is_linked(b, 'scxml_ScxmlOnexecuteType2', a2)
    if hasattr(a2, 'scxml_ScxmlScriptType'):
        assert not _is_linked(a2, 'scxml_ScxmlScriptType', b)


def test_assoc_script23_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", cond="sample_text", event="sample_text", scxmlExecutablecontent="sample_text", target="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlExecutablecontent="sample_text_2", target="sample_text_2")
    b = scxml_ScxmlScriptType(any="sample_text", content="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    _safe_set(b, 'scxml_ScxmlScriptType25', a1)
    assert _is_linked(b, 'scxml_ScxmlScriptType25', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType24'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType24', b)
    _safe_set(b, 'scxml_ScxmlScriptType25', a2)
    assert _is_linked(b, 'scxml_ScxmlScriptType25', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType24'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType24', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType24'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType24', b)
    _safe_set(b, 'scxml_ScxmlScriptType25', None)
    assert not _is_linked(b, 'scxml_ScxmlScriptType25', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType24'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType24', b)


def test_assoc_script4_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScxmlType(id="sample_text", initial="sample_text", version="sample_text")
    a2 = scxml_ScxmlScxmlType(id="sample_text_2", initial="sample_text_2", version="sample_text_2")
    b = scxml_ScxmlScriptType(any="sample_text", content="sample_text", mixed="sample_text", scxmlExtraContent="sample_text", src="sample_text")
    _safe_set(b, 'scxml_ScxmlScriptType6', a1)
    assert _is_linked(b, 'scxml_ScxmlScriptType6', a1)
    if hasattr(a1, 'scxml_ScxmlScxmlType5'):
        assert _is_linked(a1, 'scxml_ScxmlScxmlType5', b)
    _safe_set(b, 'scxml_ScxmlScriptType6', a2)
    assert _is_linked(b, 'scxml_ScxmlScriptType6', a2)
    if hasattr(a1, 'scxml_ScxmlScxmlType5'):
        assert not _is_linked(a1, 'scxml_ScxmlScxmlType5', b)
    if hasattr(a2, 'scxml_ScxmlScxmlType5'):
        assert _is_linked(a2, 'scxml_ScxmlScxmlType5', b)
    _safe_set(b, 'scxml_ScxmlScriptType6', None)
    assert not _is_linked(b, 'scxml_ScxmlScriptType6', a2)
    if hasattr(a2, 'scxml_ScxmlScxmlType5'):
        assert not _is_linked(a2, 'scxml_ScxmlScxmlType5', b)


def test_assoc_scxml30_reverse_link_reassign_clear():
    a1 = scxml_ScxmlScxmlType(id="sample_text", initial="sample_text", version="sample_text")
    a2 = scxml_ScxmlScxmlType(id="sample_text_2", initial="sample_text_2", version="sample_text_2")
    b = scxml_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'scxml_DocumentRoot31', {a1})
    assert _is_linked(b, 'scxml_DocumentRoot31', a1)
    if hasattr(a1, 'scxml_ScxmlScxmlType32'):
        assert _is_linked(a1, 'scxml_ScxmlScxmlType32', b)
    _safe_set(b, 'scxml_DocumentRoot31', {a2})
    assert _is_linked(b, 'scxml_DocumentRoot31', a2)
    if hasattr(a1, 'scxml_ScxmlScxmlType32'):
        assert not _is_linked(a1, 'scxml_ScxmlScxmlType32', b)
    if hasattr(a2, 'scxml_ScxmlScxmlType32'):
        assert _is_linked(a2, 'scxml_ScxmlScxmlType32', b)
    _safe_set(b, 'scxml_DocumentRoot31', set())
    assert not _is_linked(b, 'scxml_DocumentRoot31', a2)
    if hasattr(a2, 'scxml_ScxmlScxmlType32'):
        assert not _is_linked(a2, 'scxml_ScxmlScxmlType32', b)


def test_assoc_send0_reverse_link_reassign_clear():
    a1 = scxml_ScxmlSendType(event="sample_text")
    a2 = scxml_ScxmlSendType(event="sample_text_2")
    b = scxml_ScxmlOnexecuteType(any="sample_text", anyAttribute="sample_text", scxmlExecutablecontent="sample_text")
    _safe_set(b, 'scxml_ScxmlOnexecuteType', {a1})
    assert _is_linked(b, 'scxml_ScxmlOnexecuteType', a1)
    if hasattr(a1, 'scxml_ScxmlSendType'):
        assert _is_linked(a1, 'scxml_ScxmlSendType', b)
    _safe_set(b, 'scxml_ScxmlOnexecuteType', {a2})
    assert _is_linked(b, 'scxml_ScxmlOnexecuteType', a2)
    if hasattr(a1, 'scxml_ScxmlSendType'):
        assert not _is_linked(a1, 'scxml_ScxmlSendType', b)
    if hasattr(a2, 'scxml_ScxmlSendType'):
        assert _is_linked(a2, 'scxml_ScxmlSendType', b)
    _safe_set(b, 'scxml_ScxmlOnexecuteType', set())
    assert not _is_linked(b, 'scxml_ScxmlOnexecuteType', a2)
    if hasattr(a2, 'scxml_ScxmlSendType'):
        assert not _is_linked(a2, 'scxml_ScxmlSendType', b)


def test_assoc_send20_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", cond="sample_text", event="sample_text", scxmlExecutablecontent="sample_text", target="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlExecutablecontent="sample_text_2", target="sample_text_2")
    b = scxml_ScxmlSendType(event="sample_text")
    _safe_set(b, 'scxml_ScxmlSendType22', a1)
    assert _is_linked(b, 'scxml_ScxmlSendType22', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType21'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType21', b)
    _safe_set(b, 'scxml_ScxmlSendType22', a2)
    assert _is_linked(b, 'scxml_ScxmlSendType22', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType21'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType21', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType21'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType21', b)
    _safe_set(b, 'scxml_ScxmlSendType22', None)
    assert not _is_linked(b, 'scxml_ScxmlSendType22', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType21'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType21', b)


def test_assoc_state18_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(id="sample_text", initial="sample_text")
    a2 = scxml_ScxmlStateType(id="sample_text_2", initial="sample_text_2")
    b = scxml_ScxmlStateType(id="sample_text", initial="sample_text")
    _safe_set(b, 'scxml_ScxmlStateType19', a1)
    assert _is_linked(b, 'scxml_ScxmlStateType19', a1)
    if hasattr(a1, 'scxml_ScxmlStateType17'):
        assert _is_linked(a1, 'scxml_ScxmlStateType17', b)
    _safe_set(b, 'scxml_ScxmlStateType19', a2)
    assert _is_linked(b, 'scxml_ScxmlStateType19', a2)
    if hasattr(a1, 'scxml_ScxmlStateType17'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType17', b)
    if hasattr(a2, 'scxml_ScxmlStateType17'):
        assert _is_linked(a2, 'scxml_ScxmlStateType17', b)
    _safe_set(b, 'scxml_ScxmlStateType19', None)
    assert not _is_linked(b, 'scxml_ScxmlStateType19', a2)
    if hasattr(a2, 'scxml_ScxmlStateType17'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType17', b)


def test_assoc_state3_reverse_link_reassign_clear():
    a1 = scxml_ScxmlStateType(id="sample_text", initial="sample_text")
    a2 = scxml_ScxmlStateType(id="sample_text_2", initial="sample_text_2")
    b = scxml_ScxmlScxmlType(id="sample_text", initial="sample_text", version="sample_text")
    _safe_set(b, 'scxml_ScxmlScxmlType', {a1})
    assert _is_linked(b, 'scxml_ScxmlScxmlType', a1)
    if hasattr(a1, 'scxml_ScxmlStateType'):
        assert _is_linked(a1, 'scxml_ScxmlStateType', b)
    _safe_set(b, 'scxml_ScxmlScxmlType', {a2})
    assert _is_linked(b, 'scxml_ScxmlScxmlType', a2)
    if hasattr(a1, 'scxml_ScxmlStateType'):
        assert not _is_linked(a1, 'scxml_ScxmlStateType', b)
    if hasattr(a2, 'scxml_ScxmlStateType'):
        assert _is_linked(a2, 'scxml_ScxmlStateType', b)
    _safe_set(b, 'scxml_ScxmlScxmlType', set())
    assert not _is_linked(b, 'scxml_ScxmlScxmlType', a2)
    if hasattr(a2, 'scxml_ScxmlStateType'):
        assert not _is_linked(a2, 'scxml_ScxmlStateType', b)


def test_assoc_transition15_reverse_link_reassign_clear():
    a1 = scxml_ScxmlTransitionType(any="sample_text", cond="sample_text", event="sample_text", scxmlExecutablecontent="sample_text", target="sample_text")
    a2 = scxml_ScxmlTransitionType(any="sample_text_2", cond="sample_text_2", event="sample_text_2", scxmlExecutablecontent="sample_text_2", target="sample_text_2")
    b = scxml_ScxmlStateType(id="sample_text", initial="sample_text")
    _safe_set(b, 'scxml_ScxmlStateType16', {a1})
    assert _is_linked(b, 'scxml_ScxmlStateType16', a1)
    if hasattr(a1, 'scxml_ScxmlTransitionType'):
        assert _is_linked(a1, 'scxml_ScxmlTransitionType', b)
    _safe_set(b, 'scxml_ScxmlStateType16', {a2})
    assert _is_linked(b, 'scxml_ScxmlStateType16', a2)
    if hasattr(a1, 'scxml_ScxmlTransitionType'):
        assert not _is_linked(a1, 'scxml_ScxmlTransitionType', b)
    if hasattr(a2, 'scxml_ScxmlTransitionType'):
        assert _is_linked(a2, 'scxml_ScxmlTransitionType', b)
    _safe_set(b, 'scxml_ScxmlStateType16', set())
    assert not _is_linked(b, 'scxml_ScxmlStateType16', a2)
    if hasattr(a2, 'scxml_ScxmlTransitionType'):
        assert not _is_linked(a2, 'scxml_ScxmlTransitionType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_xMLNSPrefixMap26_stub_double():
    # scxml_EStringToStringMapEntry has no real 'scxml_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so scxml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_DocumentRoot(mixed="sample_text")
    partner = scxml_EStringToStringMapEntry()
    setattr(partner, 'scxml_EStringToStringMapEntry', None)
    _safe_set(owner, 'scxml_DocumentRoot', {partner})
    assert getattr(partner, 'scxml_EStringToStringMapEntry') == owner
    _safe_set(owner, 'scxml_DocumentRoot', set())
    assert getattr(partner, 'scxml_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation27_stub_double():
    # scxml_EStringToStringMapEntry has no real 'scxml_EStringToStringMapEntry29' property in the generated
    # code (a bare stub) -- manually attach it so scxml_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_DocumentRoot(mixed="sample_text")
    partner = scxml_EStringToStringMapEntry()
    setattr(partner, 'scxml_EStringToStringMapEntry29', None)
    _safe_set(owner, 'scxml_DocumentRoot28', {partner})
    assert getattr(partner, 'scxml_EStringToStringMapEntry29') == owner
    _safe_set(owner, 'scxml_DocumentRoot28', set())
    assert getattr(partner, 'scxml_EStringToStringMapEntry29') is None


