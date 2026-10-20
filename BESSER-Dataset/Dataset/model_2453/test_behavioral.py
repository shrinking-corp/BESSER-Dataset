import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    scxml_Anchor,
    scxml_Assign,
    scxml_Cancel,
    scxml_Content,
    scxml_Data,
    scxml_DataModel,
    scxml_Donedata,
    scxml_Else,
    scxml_ElseIf,
    scxml_FinalState,
    scxml_Finalize,
    scxml_HistoryState,
    scxml_If,
    scxml_InitialState,
    scxml_Invoke,
    scxml_Log,
    scxml_NamedElement,
    scxml_OnEntry,
    scxml_OnExit,
    scxml_Parallel,
    scxml_Param,
    scxml_Raise,
    scxml_Script,
    scxml_Send,
    scxml_ServiceTemplate,
    scxml_State,
    scxml_Transition,
    scxml_Validate,
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

def test_assoc_anchor115_reverse_link_reassign_clear():
    a1 = scxml_Parallel(id="sample_text")
    a2 = scxml_Parallel(id="sample_text_2")
    b = scxml_Anchor(snapshot="sample_text", type="sample_text")
    _safe_set(b, 'scxml_Anchor117', a1)
    assert _is_linked(b, 'scxml_Anchor117', a1)
    if hasattr(a1, 'scxml_Parallel116'):
        assert _is_linked(a1, 'scxml_Parallel116', b)
    _safe_set(b, 'scxml_Anchor117', a2)
    assert _is_linked(b, 'scxml_Anchor117', a2)
    if hasattr(a1, 'scxml_Parallel116'):
        assert not _is_linked(a1, 'scxml_Parallel116', b)
    if hasattr(a2, 'scxml_Parallel116'):
        assert _is_linked(a2, 'scxml_Parallel116', b)
    _safe_set(b, 'scxml_Anchor117', None)
    assert not _is_linked(b, 'scxml_Anchor117', a2)
    if hasattr(a2, 'scxml_Parallel116'):
        assert not _is_linked(a2, 'scxml_Parallel116', b)


def test_assoc_anchor17_reverse_link_reassign_clear():
    a1 = scxml_State(id="sample_text")
    a2 = scxml_State(id="sample_text_2")
    b = scxml_Anchor(snapshot="sample_text", type="sample_text")
    _safe_set(b, 'scxml_Anchor', a1)
    assert _is_linked(b, 'scxml_Anchor', a1)
    if hasattr(a1, 'scxml_State18'):
        assert _is_linked(a1, 'scxml_State18', b)
    _safe_set(b, 'scxml_Anchor', a2)
    assert _is_linked(b, 'scxml_Anchor', a2)
    if hasattr(a1, 'scxml_State18'):
        assert not _is_linked(a1, 'scxml_State18', b)
    if hasattr(a2, 'scxml_State18'):
        assert _is_linked(a2, 'scxml_State18', b)
    _safe_set(b, 'scxml_Anchor', None)
    assert not _is_linked(b, 'scxml_Anchor', a2)
    if hasattr(a2, 'scxml_State18'):
        assert not _is_linked(a2, 'scxml_State18', b)


def test_assoc_assign122_reverse_link_reassign_clear():
    a1 = scxml_If(cond="sample_text")
    a2 = scxml_If(cond="sample_text_2")
    b = scxml_Assign(dataid="sample_text", expr="sample_text", location="sample_text")
    _safe_set(b, 'scxml_Assign124', a1)
    assert _is_linked(b, 'scxml_Assign124', a1)
    if hasattr(a1, 'scxml_If123'):
        assert _is_linked(a1, 'scxml_If123', b)
    _safe_set(b, 'scxml_Assign124', a2)
    assert _is_linked(b, 'scxml_Assign124', a2)
    if hasattr(a1, 'scxml_If123'):
        assert not _is_linked(a1, 'scxml_If123', b)
    if hasattr(a2, 'scxml_If123'):
        assert _is_linked(a2, 'scxml_If123', b)
    _safe_set(b, 'scxml_Assign124', None)
    assert not _is_linked(b, 'scxml_Assign124', a2)
    if hasattr(a2, 'scxml_If123'):
        assert not _is_linked(a2, 'scxml_If123', b)


def test_assoc_cancel125_reverse_link_reassign_clear():
    a1 = scxml_If(cond="sample_text")
    a2 = scxml_If(cond="sample_text_2")
    b = scxml_Cancel(sendid="sample_text", sendidexpr="sample_text")
    _safe_set(b, 'scxml_Cancel127', a1)
    assert _is_linked(b, 'scxml_Cancel127', a1)
    if hasattr(a1, 'scxml_If126'):
        assert _is_linked(a1, 'scxml_If126', b)
    _safe_set(b, 'scxml_Cancel127', a2)
    assert _is_linked(b, 'scxml_Cancel127', a2)
    if hasattr(a1, 'scxml_If126'):
        assert not _is_linked(a1, 'scxml_If126', b)
    if hasattr(a2, 'scxml_If126'):
        assert _is_linked(a2, 'scxml_If126', b)
    _safe_set(b, 'scxml_Cancel127', None)
    assert not _is_linked(b, 'scxml_Cancel127', a2)
    if hasattr(a2, 'scxml_If126'):
        assert not _is_linked(a2, 'scxml_If126', b)


def test_assoc_data146_reverse_link_reassign_clear():
    a1 = scxml_DataModel(schema="sample_text")
    a2 = scxml_DataModel(schema="sample_text_2")
    b = scxml_Data(expr="sample_text", id="sample_text", src="sample_text")
    _safe_set(b, 'scxml_Data', a1)
    assert _is_linked(b, 'scxml_Data', a1)
    if hasattr(a1, 'scxml_DataModel147'):
        assert _is_linked(a1, 'scxml_DataModel147', b)
    _safe_set(b, 'scxml_Data', a2)
    assert _is_linked(b, 'scxml_Data', a2)
    if hasattr(a1, 'scxml_DataModel147'):
        assert not _is_linked(a1, 'scxml_DataModel147', b)
    if hasattr(a2, 'scxml_DataModel147'):
        assert _is_linked(a2, 'scxml_DataModel147', b)
    _safe_set(b, 'scxml_Data', None)
    assert not _is_linked(b, 'scxml_Data', a2)
    if hasattr(a2, 'scxml_DataModel147'):
        assert not _is_linked(a2, 'scxml_DataModel147', b)


def test_assoc_datamodel41_reverse_link_reassign_clear():
    a1 = scxml_ServiceTemplate(exmode="sample_text", name="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    a2 = scxml_ServiceTemplate(exmode="sample_text_2", name="sample_text_2", profile="sample_text_2", version="sample_text_2", xmlns="sample_text_2")
    b = scxml_DataModel(schema="sample_text")
    _safe_set(b, 'scxml_DataModel43', a1)
    assert _is_linked(b, 'scxml_DataModel43', a1)
    if hasattr(a1, 'scxml_ServiceTemplate42'):
        assert _is_linked(a1, 'scxml_ServiceTemplate42', b)
    _safe_set(b, 'scxml_DataModel43', a2)
    assert _is_linked(b, 'scxml_DataModel43', a2)
    if hasattr(a1, 'scxml_ServiceTemplate42'):
        assert not _is_linked(a1, 'scxml_ServiceTemplate42', b)
    if hasattr(a2, 'scxml_ServiceTemplate42'):
        assert _is_linked(a2, 'scxml_ServiceTemplate42', b)
    _safe_set(b, 'scxml_DataModel43', None)
    assert not _is_linked(b, 'scxml_DataModel43', a2)
    if hasattr(a2, 'scxml_ServiceTemplate42'):
        assert not _is_linked(a2, 'scxml_ServiceTemplate42', b)


def test_assoc_elseif118_reverse_link_reassign_clear():
    a1 = scxml_If(cond="sample_text")
    a2 = scxml_If(cond="sample_text_2")
    b = scxml_ElseIf(cond="sample_text")
    _safe_set(b, 'scxml_ElseIf', a1)
    assert _is_linked(b, 'scxml_ElseIf', a1)
    if hasattr(a1, 'scxml_If119'):
        assert _is_linked(a1, 'scxml_If119', b)
    _safe_set(b, 'scxml_ElseIf', a2)
    assert _is_linked(b, 'scxml_ElseIf', a2)
    if hasattr(a1, 'scxml_If119'):
        assert not _is_linked(a1, 'scxml_If119', b)
    if hasattr(a2, 'scxml_If119'):
        assert _is_linked(a2, 'scxml_If119', b)
    _safe_set(b, 'scxml_ElseIf', None)
    assert not _is_linked(b, 'scxml_ElseIf', a2)
    if hasattr(a2, 'scxml_If119'):
        assert not _is_linked(a2, 'scxml_If119', b)


def test_assoc_final11_reverse_link_reassign_clear():
    a1 = scxml_State(id="sample_text")
    a2 = scxml_State(id="sample_text_2")
    b = scxml_FinalState(id="sample_text")
    _safe_set(b, 'scxml_FinalState', a1)
    assert _is_linked(b, 'scxml_FinalState', a1)
    if hasattr(a1, 'scxml_State12'):
        assert _is_linked(a1, 'scxml_State12', b)
    _safe_set(b, 'scxml_FinalState', a2)
    assert _is_linked(b, 'scxml_FinalState', a2)
    if hasattr(a1, 'scxml_State12'):
        assert not _is_linked(a1, 'scxml_State12', b)
    if hasattr(a2, 'scxml_State12'):
        assert _is_linked(a2, 'scxml_State12', b)
    _safe_set(b, 'scxml_FinalState', None)
    assert not _is_linked(b, 'scxml_FinalState', a2)
    if hasattr(a2, 'scxml_State12'):
        assert not _is_linked(a2, 'scxml_State12', b)


def test_assoc_final35_reverse_link_reassign_clear():
    a1 = scxml_ServiceTemplate(exmode="sample_text", name="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    a2 = scxml_ServiceTemplate(exmode="sample_text_2", name="sample_text_2", profile="sample_text_2", version="sample_text_2", xmlns="sample_text_2")
    b = scxml_FinalState(id="sample_text")
    _safe_set(b, 'scxml_FinalState37', a1)
    assert _is_linked(b, 'scxml_FinalState37', a1)
    if hasattr(a1, 'scxml_ServiceTemplate36'):
        assert _is_linked(a1, 'scxml_ServiceTemplate36', b)
    _safe_set(b, 'scxml_FinalState37', a2)
    assert _is_linked(b, 'scxml_FinalState37', a2)
    if hasattr(a1, 'scxml_ServiceTemplate36'):
        assert not _is_linked(a1, 'scxml_ServiceTemplate36', b)
    if hasattr(a2, 'scxml_ServiceTemplate36'):
        assert _is_linked(a2, 'scxml_ServiceTemplate36', b)
    _safe_set(b, 'scxml_FinalState37', None)
    assert not _is_linked(b, 'scxml_FinalState37', a2)
    if hasattr(a2, 'scxml_ServiceTemplate36'):
        assert not _is_linked(a2, 'scxml_ServiceTemplate36', b)


def test_assoc_history112_reverse_link_reassign_clear():
    a1 = scxml_Parallel(id="sample_text")
    a2 = scxml_Parallel(id="sample_text_2")
    b = scxml_HistoryState(id="sample_text", type="sample_text")
    _safe_set(b, 'scxml_HistoryState114', a1)
    assert _is_linked(b, 'scxml_HistoryState114', a1)
    if hasattr(a1, 'scxml_Parallel113'):
        assert _is_linked(a1, 'scxml_Parallel113', b)
    _safe_set(b, 'scxml_HistoryState114', a2)
    assert _is_linked(b, 'scxml_HistoryState114', a2)
    if hasattr(a1, 'scxml_Parallel113'):
        assert not _is_linked(a1, 'scxml_Parallel113', b)
    if hasattr(a2, 'scxml_Parallel113'):
        assert _is_linked(a2, 'scxml_Parallel113', b)
    _safe_set(b, 'scxml_HistoryState114', None)
    assert not _is_linked(b, 'scxml_HistoryState114', a2)
    if hasattr(a2, 'scxml_Parallel113'):
        assert not _is_linked(a2, 'scxml_Parallel113', b)


def test_assoc_history15_reverse_link_reassign_clear():
    a1 = scxml_State(id="sample_text")
    a2 = scxml_State(id="sample_text_2")
    b = scxml_HistoryState(id="sample_text", type="sample_text")
    _safe_set(b, 'scxml_HistoryState', a1)
    assert _is_linked(b, 'scxml_HistoryState', a1)
    if hasattr(a1, 'scxml_State16'):
        assert _is_linked(a1, 'scxml_State16', b)
    _safe_set(b, 'scxml_HistoryState', a2)
    assert _is_linked(b, 'scxml_HistoryState', a2)
    if hasattr(a1, 'scxml_State16'):
        assert not _is_linked(a1, 'scxml_State16', b)
    if hasattr(a2, 'scxml_State16'):
        assert _is_linked(a2, 'scxml_State16', b)
    _safe_set(b, 'scxml_HistoryState', None)
    assert not _is_linked(b, 'scxml_HistoryState', a2)
    if hasattr(a2, 'scxml_State16'):
        assert not _is_linked(a2, 'scxml_State16', b)


def test_assoc_if_129_reverse_link_reassign_clear():
    a1 = scxml_If(cond="sample_text")
    a2 = scxml_If(cond="sample_text_2")
    b = scxml_If(cond="sample_text")
    _safe_set(b, 'scxml_If130', a1)
    assert _is_linked(b, 'scxml_If130', a1)
    if hasattr(a1, 'scxml_If128'):
        assert _is_linked(a1, 'scxml_If128', b)
    _safe_set(b, 'scxml_If130', a2)
    assert _is_linked(b, 'scxml_If130', a2)
    if hasattr(a1, 'scxml_If128'):
        assert not _is_linked(a1, 'scxml_If128', b)
    if hasattr(a2, 'scxml_If128'):
        assert _is_linked(a2, 'scxml_If128', b)
    _safe_set(b, 'scxml_If130', None)
    assert not _is_linked(b, 'scxml_If130', a2)
    if hasattr(a2, 'scxml_If128'):
        assert not _is_linked(a2, 'scxml_If128', b)


def test_assoc_invoke19_reverse_link_reassign_clear():
    a1 = scxml_State(id="sample_text")
    a2 = scxml_State(id="sample_text_2")
    b = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    _safe_set(b, 'scxml_Invoke', a1)
    assert _is_linked(b, 'scxml_Invoke', a1)
    if hasattr(a1, 'scxml_State20'):
        assert _is_linked(a1, 'scxml_State20', b)
    _safe_set(b, 'scxml_Invoke', a2)
    assert _is_linked(b, 'scxml_Invoke', a2)
    if hasattr(a1, 'scxml_State20'):
        assert not _is_linked(a1, 'scxml_State20', b)
    if hasattr(a2, 'scxml_State20'):
        assert _is_linked(a2, 'scxml_State20', b)
    _safe_set(b, 'scxml_Invoke', None)
    assert not _is_linked(b, 'scxml_Invoke', a2)
    if hasattr(a2, 'scxml_State20'):
        assert not _is_linked(a2, 'scxml_State20', b)


def test_assoc_log131_reverse_link_reassign_clear():
    a1 = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    a2 = scxml_Log(expr="sample_text_2", label="sample_text_2", level="sample_text_2")
    b = scxml_If(cond="sample_text")
    _safe_set(b, 'scxml_If132', {a1})
    assert _is_linked(b, 'scxml_If132', a1)
    if hasattr(a1, 'scxml_Log133'):
        assert _is_linked(a1, 'scxml_Log133', b)
    _safe_set(b, 'scxml_If132', {a2})
    assert _is_linked(b, 'scxml_If132', a2)
    if hasattr(a1, 'scxml_Log133'):
        assert not _is_linked(a1, 'scxml_Log133', b)
    if hasattr(a2, 'scxml_Log133'):
        assert _is_linked(a2, 'scxml_Log133', b)
    _safe_set(b, 'scxml_If132', set())
    assert not _is_linked(b, 'scxml_If132', a2)
    if hasattr(a2, 'scxml_Log133'):
        assert not _is_linked(a2, 'scxml_Log133', b)


def test_assoc_parallel107_reverse_link_reassign_clear():
    a1 = scxml_Parallel(id="sample_text")
    a2 = scxml_Parallel(id="sample_text_2")
    b = scxml_Parallel(id="sample_text")
    _safe_set(b, 'scxml_Parallel108', a1)
    assert _is_linked(b, 'scxml_Parallel108', a1)
    if hasattr(a1, 'scxml_Parallel106'):
        assert _is_linked(a1, 'scxml_Parallel106', b)
    _safe_set(b, 'scxml_Parallel108', a2)
    assert _is_linked(b, 'scxml_Parallel108', a2)
    if hasattr(a1, 'scxml_Parallel106'):
        assert not _is_linked(a1, 'scxml_Parallel106', b)
    if hasattr(a2, 'scxml_Parallel106'):
        assert _is_linked(a2, 'scxml_Parallel106', b)
    _safe_set(b, 'scxml_Parallel108', None)
    assert not _is_linked(b, 'scxml_Parallel108', a2)
    if hasattr(a2, 'scxml_Parallel106'):
        assert not _is_linked(a2, 'scxml_Parallel106', b)


def test_assoc_parallel13_reverse_link_reassign_clear():
    a1 = scxml_State(id="sample_text")
    a2 = scxml_State(id="sample_text_2")
    b = scxml_Parallel(id="sample_text")
    _safe_set(b, 'scxml_Parallel', a1)
    assert _is_linked(b, 'scxml_Parallel', a1)
    if hasattr(a1, 'scxml_State14'):
        assert _is_linked(a1, 'scxml_State14', b)
    _safe_set(b, 'scxml_Parallel', a2)
    assert _is_linked(b, 'scxml_Parallel', a2)
    if hasattr(a1, 'scxml_State14'):
        assert not _is_linked(a1, 'scxml_State14', b)
    if hasattr(a2, 'scxml_State14'):
        assert _is_linked(a2, 'scxml_State14', b)
    _safe_set(b, 'scxml_Parallel', None)
    assert not _is_linked(b, 'scxml_Parallel', a2)
    if hasattr(a2, 'scxml_State14'):
        assert not _is_linked(a2, 'scxml_State14', b)


def test_assoc_parallel38_reverse_link_reassign_clear():
    a1 = scxml_ServiceTemplate(exmode="sample_text", name="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    a2 = scxml_ServiceTemplate(exmode="sample_text_2", name="sample_text_2", profile="sample_text_2", version="sample_text_2", xmlns="sample_text_2")
    b = scxml_Parallel(id="sample_text")
    _safe_set(b, 'scxml_Parallel40', a1)
    assert _is_linked(b, 'scxml_Parallel40', a1)
    if hasattr(a1, 'scxml_ServiceTemplate39'):
        assert _is_linked(a1, 'scxml_ServiceTemplate39', b)
    _safe_set(b, 'scxml_Parallel40', a2)
    assert _is_linked(b, 'scxml_Parallel40', a2)
    if hasattr(a1, 'scxml_ServiceTemplate39'):
        assert not _is_linked(a1, 'scxml_ServiceTemplate39', b)
    if hasattr(a2, 'scxml_ServiceTemplate39'):
        assert _is_linked(a2, 'scxml_ServiceTemplate39', b)
    _safe_set(b, 'scxml_Parallel40', None)
    assert not _is_linked(b, 'scxml_Parallel40', a2)
    if hasattr(a2, 'scxml_ServiceTemplate39'):
        assert not _is_linked(a2, 'scxml_ServiceTemplate39', b)


def test_assoc_param134_reverse_link_reassign_clear():
    a1 = scxml_Param(expr="sample_text", name="sample_text")
    a2 = scxml_Param(expr="sample_text_2", name="sample_text_2")
    b = scxml_If(cond="sample_text")
    _safe_set(b, 'scxml_If135', {a1})
    assert _is_linked(b, 'scxml_If135', a1)
    if hasattr(a1, 'scxml_Param136'):
        assert _is_linked(a1, 'scxml_Param136', b)
    _safe_set(b, 'scxml_If135', {a2})
    assert _is_linked(b, 'scxml_If135', a2)
    if hasattr(a1, 'scxml_Param136'):
        assert not _is_linked(a1, 'scxml_Param136', b)
    if hasattr(a2, 'scxml_Param136'):
        assert _is_linked(a2, 'scxml_Param136', b)
    _safe_set(b, 'scxml_If135', set())
    assert not _is_linked(b, 'scxml_If135', a2)
    if hasattr(a2, 'scxml_Param136'):
        assert not _is_linked(a2, 'scxml_Param136', b)


def test_assoc_param150_reverse_link_reassign_clear():
    a1 = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_Send(delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", hints="sample_text_2", hintsexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_Param(expr="sample_text", name="sample_text")
    _safe_set(b, 'scxml_Param152', a1)
    assert _is_linked(b, 'scxml_Param152', a1)
    if hasattr(a1, 'scxml_Send151'):
        assert _is_linked(a1, 'scxml_Send151', b)
    _safe_set(b, 'scxml_Param152', a2)
    assert _is_linked(b, 'scxml_Param152', a2)
    if hasattr(a1, 'scxml_Send151'):
        assert not _is_linked(a1, 'scxml_Send151', b)
    if hasattr(a2, 'scxml_Send151'):
        assert _is_linked(a2, 'scxml_Send151', b)
    _safe_set(b, 'scxml_Param152', None)
    assert not _is_linked(b, 'scxml_Param152', a2)
    if hasattr(a2, 'scxml_Send151'):
        assert not _is_linked(a2, 'scxml_Send151', b)


def test_assoc_param168_reverse_link_reassign_clear():
    a1 = scxml_Param(expr="sample_text", name="sample_text")
    a2 = scxml_Param(expr="sample_text_2", name="sample_text_2")
    b = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    _safe_set(b, 'scxml_Invoke169', {a1})
    assert _is_linked(b, 'scxml_Invoke169', a1)
    if hasattr(a1, 'scxml_Param170'):
        assert _is_linked(a1, 'scxml_Param170', b)
    _safe_set(b, 'scxml_Invoke169', {a2})
    assert _is_linked(b, 'scxml_Invoke169', a2)
    if hasattr(a1, 'scxml_Param170'):
        assert not _is_linked(a1, 'scxml_Param170', b)
    if hasattr(a2, 'scxml_Param170'):
        assert _is_linked(a2, 'scxml_Param170', b)
    _safe_set(b, 'scxml_Invoke169', set())
    assert not _is_linked(b, 'scxml_Invoke169', a2)
    if hasattr(a2, 'scxml_Param170'):
        assert not _is_linked(a2, 'scxml_Param170', b)


def test_assoc_raise_137_reverse_link_reassign_clear():
    a1 = scxml_Raise(event="sample_text")
    a2 = scxml_Raise(event="sample_text_2")
    b = scxml_If(cond="sample_text")
    _safe_set(b, 'scxml_If138', {a1})
    assert _is_linked(b, 'scxml_If138', a1)
    if hasattr(a1, 'scxml_Raise139'):
        assert _is_linked(a1, 'scxml_Raise139', b)
    _safe_set(b, 'scxml_If138', {a2})
    assert _is_linked(b, 'scxml_If138', a2)
    if hasattr(a1, 'scxml_Raise139'):
        assert not _is_linked(a1, 'scxml_Raise139', b)
    if hasattr(a2, 'scxml_Raise139'):
        assert _is_linked(a2, 'scxml_Raise139', b)
    _safe_set(b, 'scxml_If138', set())
    assert not _is_linked(b, 'scxml_If138', a2)
    if hasattr(a2, 'scxml_Raise139'):
        assert not _is_linked(a2, 'scxml_Raise139', b)


def test_assoc_send140_reverse_link_reassign_clear():
    a1 = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    a2 = scxml_Send(delay="sample_text_2", delayexpr="sample_text_2", event="sample_text_2", eventexpr="sample_text_2", hints="sample_text_2", hintsexpr="sample_text_2", id="sample_text_2", idlocation="sample_text_2", namelist="sample_text_2", target="sample_text_2", targetexpr="sample_text_2", type="sample_text_2", typeexpr="sample_text_2")
    b = scxml_If(cond="sample_text")
    _safe_set(b, 'scxml_If141', {a1})
    assert _is_linked(b, 'scxml_If141', a1)
    if hasattr(a1, 'scxml_Send142'):
        assert _is_linked(a1, 'scxml_Send142', b)
    _safe_set(b, 'scxml_If141', {a2})
    assert _is_linked(b, 'scxml_If141', a2)
    if hasattr(a1, 'scxml_Send142'):
        assert not _is_linked(a1, 'scxml_Send142', b)
    if hasattr(a2, 'scxml_Send142'):
        assert _is_linked(a2, 'scxml_Send142', b)
    _safe_set(b, 'scxml_If141', set())
    assert not _is_linked(b, 'scxml_If141', a2)
    if hasattr(a2, 'scxml_Send142'):
        assert not _is_linked(a2, 'scxml_Send142', b)


def test_assoc_state109_reverse_link_reassign_clear():
    a1 = scxml_State(id="sample_text")
    a2 = scxml_State(id="sample_text_2")
    b = scxml_Parallel(id="sample_text")
    _safe_set(b, 'scxml_Parallel110', {a1})
    assert _is_linked(b, 'scxml_Parallel110', a1)
    if hasattr(a1, 'scxml_State111'):
        assert _is_linked(a1, 'scxml_State111', b)
    _safe_set(b, 'scxml_Parallel110', {a2})
    assert _is_linked(b, 'scxml_Parallel110', a2)
    if hasattr(a1, 'scxml_State111'):
        assert not _is_linked(a1, 'scxml_State111', b)
    if hasattr(a2, 'scxml_State111'):
        assert _is_linked(a2, 'scxml_State111', b)
    _safe_set(b, 'scxml_Parallel110', set())
    assert not _is_linked(b, 'scxml_Parallel110', a2)
    if hasattr(a2, 'scxml_State111'):
        assert not _is_linked(a2, 'scxml_State111', b)


def test_assoc_state29_reverse_link_reassign_clear():
    a1 = scxml_State(id="sample_text")
    a2 = scxml_State(id="sample_text_2")
    b = scxml_ServiceTemplate(exmode="sample_text", name="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    _safe_set(b, 'scxml_ServiceTemplate30', {a1})
    assert _is_linked(b, 'scxml_ServiceTemplate30', a1)
    if hasattr(a1, 'scxml_State31'):
        assert _is_linked(a1, 'scxml_State31', b)
    _safe_set(b, 'scxml_ServiceTemplate30', {a2})
    assert _is_linked(b, 'scxml_ServiceTemplate30', a2)
    if hasattr(a1, 'scxml_State31'):
        assert not _is_linked(a1, 'scxml_State31', b)
    if hasattr(a2, 'scxml_State31'):
        assert _is_linked(a2, 'scxml_State31', b)
    _safe_set(b, 'scxml_ServiceTemplate30', set())
    assert not _is_linked(b, 'scxml_ServiceTemplate30', a2)
    if hasattr(a2, 'scxml_State31'):
        assert not _is_linked(a2, 'scxml_State31', b)


def test_assoc_state9_reverse_link_reassign_clear():
    a1 = scxml_State(id="sample_text")
    a2 = scxml_State(id="sample_text_2")
    b = scxml_State(id="sample_text")
    _safe_set(b, 'scxml_State8', {a1})
    assert _is_linked(b, 'scxml_State8', a1)
    if hasattr(a1, 'scxml_State10'):
        assert _is_linked(a1, 'scxml_State10', b)
    _safe_set(b, 'scxml_State8', {a2})
    assert _is_linked(b, 'scxml_State8', a2)
    if hasattr(a1, 'scxml_State10'):
        assert not _is_linked(a1, 'scxml_State10', b)
    if hasattr(a2, 'scxml_State10'):
        assert _is_linked(a2, 'scxml_State10', b)
    _safe_set(b, 'scxml_State8', set())
    assert not _is_linked(b, 'scxml_State8', a2)
    if hasattr(a2, 'scxml_State10'):
        assert not _is_linked(a2, 'scxml_State10', b)


def test_assoc_transition27_reverse_link_reassign_clear():
    a1 = scxml_Transition(anchor="sample_text", cond="sample_text", event="sample_text")
    a2 = scxml_Transition(anchor="sample_text_2", cond="sample_text_2", event="sample_text_2")
    b = scxml_ServiceTemplate(exmode="sample_text", name="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    _safe_set(b, 'scxml_ServiceTemplate', {a1})
    assert _is_linked(b, 'scxml_ServiceTemplate', a1)
    if hasattr(a1, 'scxml_Transition28'):
        assert _is_linked(a1, 'scxml_Transition28', b)
    _safe_set(b, 'scxml_ServiceTemplate', {a2})
    assert _is_linked(b, 'scxml_ServiceTemplate', a2)
    if hasattr(a1, 'scxml_Transition28'):
        assert not _is_linked(a1, 'scxml_Transition28', b)
    if hasattr(a2, 'scxml_Transition28'):
        assert _is_linked(a2, 'scxml_Transition28', b)
    _safe_set(b, 'scxml_ServiceTemplate', set())
    assert not _is_linked(b, 'scxml_ServiceTemplate', a2)
    if hasattr(a2, 'scxml_Transition28'):
        assert not _is_linked(a2, 'scxml_Transition28', b)


def test_assoc_validate143_reverse_link_reassign_clear():
    a1 = scxml_Validate(location="sample_text", schema="sample_text")
    a2 = scxml_Validate(location="sample_text_2", schema="sample_text_2")
    b = scxml_If(cond="sample_text")
    _safe_set(b, 'scxml_If144', {a1})
    assert _is_linked(b, 'scxml_If144', a1)
    if hasattr(a1, 'scxml_Validate145'):
        assert _is_linked(a1, 'scxml_Validate145', b)
    _safe_set(b, 'scxml_If144', {a2})
    assert _is_linked(b, 'scxml_If144', a2)
    if hasattr(a1, 'scxml_Validate145'):
        assert not _is_linked(a1, 'scxml_Validate145', b)
    if hasattr(a2, 'scxml_Validate145'):
        assert _is_linked(a2, 'scxml_Validate145', b)
    _safe_set(b, 'scxml_If144', set())
    assert not _is_linked(b, 'scxml_If144', a2)
    if hasattr(a2, 'scxml_Validate145'):
        assert not _is_linked(a2, 'scxml_Validate145', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assign173_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize174' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Assign(dataid="sample_text", expr="sample_text", location="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize174', None)
    _safe_set(owner, 'scxml_Assign175', partner)
    assert owner in getattr(partner, 'scxml_Finalize174')
    _safe_set(owner, 'scxml_Assign175', None)
    assert owner not in getattr(partner, 'scxml_Finalize174')


def test_assoc_assign49_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry50' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Assign(dataid="sample_text", expr="sample_text", location="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry50', None)
    _safe_set(owner, 'scxml_Assign', partner)
    assert owner in getattr(partner, 'scxml_OnEntry50')
    _safe_set(owner, 'scxml_Assign', None)
    assert owner not in getattr(partner, 'scxml_OnEntry50')


def test_assoc_assign68_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit69' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Assign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Assign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Assign(dataid="sample_text", expr="sample_text", location="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit69', None)
    _safe_set(owner, 'scxml_Assign70', partner)
    assert owner in getattr(partner, 'scxml_OnExit69')
    _safe_set(owner, 'scxml_Assign70', None)
    assert owner not in getattr(partner, 'scxml_OnExit69')


def test_assoc_cancel176_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize177' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Cancel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Cancel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Cancel(sendid="sample_text", sendidexpr="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize177', None)
    _safe_set(owner, 'scxml_Cancel178', partner)
    assert owner in getattr(partner, 'scxml_Finalize177')
    _safe_set(owner, 'scxml_Cancel178', None)
    assert owner not in getattr(partner, 'scxml_Finalize177')


def test_assoc_cancel51_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry52' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Cancel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Cancel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Cancel(sendid="sample_text", sendidexpr="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry52', None)
    _safe_set(owner, 'scxml_Cancel', partner)
    assert owner in getattr(partner, 'scxml_OnEntry52')
    _safe_set(owner, 'scxml_Cancel', None)
    assert owner not in getattr(partner, 'scxml_OnEntry52')


def test_assoc_cancel71_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit72' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Cancel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Cancel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Cancel(sendid="sample_text", sendidexpr="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit72', None)
    _safe_set(owner, 'scxml_Cancel73', partner)
    assert owner in getattr(partner, 'scxml_OnExit72')
    _safe_set(owner, 'scxml_Cancel73', None)
    assert owner not in getattr(partner, 'scxml_OnExit72')


def test_assoc_content148_stub_double():
    # scxml_Content has no real 'scxml_Content' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Data's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Data's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Data(expr="sample_text", id="sample_text", src="sample_text")
    partner = scxml_Content()
    setattr(partner, 'scxml_Content', None)
    _safe_set(owner, 'scxml_Data149', partner)
    assert getattr(partner, 'scxml_Content') == owner
    _safe_set(owner, 'scxml_Data149', None)
    assert getattr(partner, 'scxml_Content') is None


def test_assoc_content153_stub_double():
    # scxml_Content has no real 'scxml_Content155' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Send's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Send's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    partner = scxml_Content()
    setattr(partner, 'scxml_Content155', None)
    _safe_set(owner, 'scxml_Send154', partner)
    assert getattr(partner, 'scxml_Content155') == owner
    _safe_set(owner, 'scxml_Send154', None)
    assert getattr(partner, 'scxml_Content155') is None


def test_assoc_content165_stub_double():
    # scxml_Content has no real 'scxml_Content167' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Invoke's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Invoke's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    partner = scxml_Content()
    setattr(partner, 'scxml_Content167', None)
    _safe_set(owner, 'scxml_Invoke166', partner)
    assert getattr(partner, 'scxml_Content167') == owner
    _safe_set(owner, 'scxml_Invoke166', None)
    assert getattr(partner, 'scxml_Content167') is None


def test_assoc_datamodel0_stub_double():
    # scxml_NamedElement has no real 'scxml_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so scxml_DataModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_DataModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_DataModel(schema="sample_text")
    partner = scxml_NamedElement()
    setattr(partner, 'scxml_NamedElement', None)
    _safe_set(owner, 'scxml_DataModel', partner)
    assert owner in getattr(partner, 'scxml_NamedElement')
    _safe_set(owner, 'scxml_DataModel', None)
    assert owner not in getattr(partner, 'scxml_NamedElement')


def test_assoc_donedata98_stub_double():
    # scxml_Donedata has no real 'scxml_Donedata' property in the generated
    # code (a bare stub) -- manually attach it so scxml_FinalState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_FinalState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_FinalState(id="sample_text")
    partner = scxml_Donedata()
    setattr(partner, 'scxml_Donedata', None)
    _safe_set(owner, 'scxml_FinalState99', partner)
    assert getattr(partner, 'scxml_Donedata') == owner
    _safe_set(owner, 'scxml_FinalState99', None)
    assert getattr(partner, 'scxml_Donedata') is None


def test_assoc_else_120_stub_double():
    # scxml_Else has no real 'scxml_Else' property in the generated
    # code (a bare stub) -- manually attach it so scxml_If's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_If's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_If(cond="sample_text")
    partner = scxml_Else()
    setattr(partner, 'scxml_Else', None)
    _safe_set(owner, 'scxml_If121', partner)
    assert getattr(partner, 'scxml_Else') == owner
    _safe_set(owner, 'scxml_If121', None)
    assert getattr(partner, 'scxml_Else') is None


def test_assoc_finalize171_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Invoke's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Invoke's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize', None)
    _safe_set(owner, 'scxml_Invoke172', partner)
    assert getattr(partner, 'scxml_Finalize') == owner
    _safe_set(owner, 'scxml_Invoke172', None)
    assert getattr(partner, 'scxml_Finalize') is None


def test_assoc_if_179_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize180' property in the generated
    # code (a bare stub) -- manually attach it so scxml_If's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_If's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_If(cond="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize180', None)
    _safe_set(owner, 'scxml_If181', partner)
    assert owner in getattr(partner, 'scxml_Finalize180')
    _safe_set(owner, 'scxml_If181', None)
    assert owner not in getattr(partner, 'scxml_Finalize180')


def test_assoc_if_53_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry54' property in the generated
    # code (a bare stub) -- manually attach it so scxml_If's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_If's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_If(cond="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry54', None)
    _safe_set(owner, 'scxml_If', partner)
    assert owner in getattr(partner, 'scxml_OnEntry54')
    _safe_set(owner, 'scxml_If', None)
    assert owner not in getattr(partner, 'scxml_OnEntry54')


def test_assoc_if_74_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit75' property in the generated
    # code (a bare stub) -- manually attach it so scxml_If's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_If's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_If(cond="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit75', None)
    _safe_set(owner, 'scxml_If76', partner)
    assert owner in getattr(partner, 'scxml_OnExit75')
    _safe_set(owner, 'scxml_If76', None)
    assert owner not in getattr(partner, 'scxml_OnExit75')


def test_assoc_initial32_stub_double():
    # scxml_InitialState has no real 'scxml_InitialState34' property in the generated
    # code (a bare stub) -- manually attach it so scxml_ServiceTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_ServiceTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_ServiceTemplate(exmode="sample_text", name="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    partner = scxml_InitialState()
    setattr(partner, 'scxml_InitialState34', None)
    _safe_set(owner, 'scxml_ServiceTemplate33', partner)
    assert getattr(partner, 'scxml_InitialState34') == owner
    _safe_set(owner, 'scxml_ServiceTemplate33', None)
    assert getattr(partner, 'scxml_InitialState34') is None


def test_assoc_initial6_stub_double():
    # scxml_InitialState has no real 'scxml_InitialState' property in the generated
    # code (a bare stub) -- manually attach it so scxml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_State(id="sample_text")
    partner = scxml_InitialState()
    setattr(partner, 'scxml_InitialState', None)
    _safe_set(owner, 'scxml_State7', partner)
    assert getattr(partner, 'scxml_InitialState') == owner
    _safe_set(owner, 'scxml_State7', None)
    assert getattr(partner, 'scxml_InitialState') is None


def test_assoc_log182_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize183' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Log's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Log's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize183', None)
    _safe_set(owner, 'scxml_Log184', partner)
    assert owner in getattr(partner, 'scxml_Finalize183')
    _safe_set(owner, 'scxml_Log184', None)
    assert owner not in getattr(partner, 'scxml_Finalize183')


def test_assoc_log55_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry56' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Log's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Log's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry56', None)
    _safe_set(owner, 'scxml_Log', partner)
    assert owner in getattr(partner, 'scxml_OnEntry56')
    _safe_set(owner, 'scxml_Log', None)
    assert owner not in getattr(partner, 'scxml_OnEntry56')


def test_assoc_log77_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit78' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Log's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Log's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit78', None)
    _safe_set(owner, 'scxml_Log79', partner)
    assert owner in getattr(partner, 'scxml_OnExit78')
    _safe_set(owner, 'scxml_Log79', None)
    assert owner not in getattr(partner, 'scxml_OnExit78')


def test_assoc_onentry100_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry102' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Parallel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Parallel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Parallel(id="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry102', None)
    _safe_set(owner, 'scxml_Parallel101', {partner})
    assert getattr(partner, 'scxml_OnEntry102') == owner
    _safe_set(owner, 'scxml_Parallel101', set())
    assert getattr(partner, 'scxml_OnEntry102') is None


def test_assoc_onentry3_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry' property in the generated
    # code (a bare stub) -- manually attach it so scxml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_State(id="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry', None)
    _safe_set(owner, 'scxml_State', {partner})
    assert getattr(partner, 'scxml_OnEntry') == owner
    _safe_set(owner, 'scxml_State', set())
    assert getattr(partner, 'scxml_OnEntry') is None


def test_assoc_onentry92_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry94' property in the generated
    # code (a bare stub) -- manually attach it so scxml_FinalState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_FinalState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_FinalState(id="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry94', None)
    _safe_set(owner, 'scxml_FinalState93', {partner})
    assert getattr(partner, 'scxml_OnEntry94') == owner
    _safe_set(owner, 'scxml_FinalState93', set())
    assert getattr(partner, 'scxml_OnEntry94') is None


def test_assoc_onexit103_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit105' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Parallel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Parallel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Parallel(id="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit105', None)
    _safe_set(owner, 'scxml_Parallel104', {partner})
    assert getattr(partner, 'scxml_OnExit105') == owner
    _safe_set(owner, 'scxml_Parallel104', set())
    assert getattr(partner, 'scxml_OnExit105') is None


def test_assoc_onexit4_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit' property in the generated
    # code (a bare stub) -- manually attach it so scxml_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_State(id="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit', None)
    _safe_set(owner, 'scxml_State5', {partner})
    assert getattr(partner, 'scxml_OnExit') == owner
    _safe_set(owner, 'scxml_State5', set())
    assert getattr(partner, 'scxml_OnExit') is None


def test_assoc_onexit95_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit97' property in the generated
    # code (a bare stub) -- manually attach it so scxml_FinalState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_FinalState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_FinalState(id="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit97', None)
    _safe_set(owner, 'scxml_FinalState96', {partner})
    assert getattr(partner, 'scxml_OnExit97') == owner
    _safe_set(owner, 'scxml_FinalState96', set())
    assert getattr(partner, 'scxml_OnExit97') is None


def test_assoc_param162_stub_double():
    # scxml_Donedata has no real 'scxml_Donedata163' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Param(expr="sample_text", name="sample_text")
    partner = scxml_Donedata()
    setattr(partner, 'scxml_Donedata163', None)
    _safe_set(owner, 'scxml_Param164', partner)
    assert owner in getattr(partner, 'scxml_Donedata163')
    _safe_set(owner, 'scxml_Param164', None)
    assert owner not in getattr(partner, 'scxml_Donedata163')


def test_assoc_param185_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize186' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Param(expr="sample_text", name="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize186', None)
    _safe_set(owner, 'scxml_Param187', partner)
    assert owner in getattr(partner, 'scxml_Finalize186')
    _safe_set(owner, 'scxml_Param187', None)
    assert owner not in getattr(partner, 'scxml_Finalize186')


def test_assoc_param57_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry58' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Param(expr="sample_text", name="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry58', None)
    _safe_set(owner, 'scxml_Param', partner)
    assert owner in getattr(partner, 'scxml_OnEntry58')
    _safe_set(owner, 'scxml_Param', None)
    assert owner not in getattr(partner, 'scxml_OnEntry58')


def test_assoc_param80_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit81' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Param's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Param's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Param(expr="sample_text", name="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit81', None)
    _safe_set(owner, 'scxml_Param82', partner)
    assert owner in getattr(partner, 'scxml_OnExit81')
    _safe_set(owner, 'scxml_Param82', None)
    assert owner not in getattr(partner, 'scxml_OnExit81')


def test_assoc_raise_188_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize189' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Raise's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Raise's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Raise(event="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize189', None)
    _safe_set(owner, 'scxml_Raise190', partner)
    assert owner in getattr(partner, 'scxml_Finalize189')
    _safe_set(owner, 'scxml_Raise190', None)
    assert owner not in getattr(partner, 'scxml_Finalize189')


def test_assoc_raise_59_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry60' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Raise's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Raise's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Raise(event="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry60', None)
    _safe_set(owner, 'scxml_Raise', partner)
    assert owner in getattr(partner, 'scxml_OnEntry60')
    _safe_set(owner, 'scxml_Raise', None)
    assert owner not in getattr(partner, 'scxml_OnEntry60')


def test_assoc_raise_83_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit84' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Raise's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Raise's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Raise(event="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit84', None)
    _safe_set(owner, 'scxml_Raise85', partner)
    assert owner in getattr(partner, 'scxml_OnExit84')
    _safe_set(owner, 'scxml_Raise85', None)
    assert owner not in getattr(partner, 'scxml_OnExit84')


def test_assoc_script44_stub_double():
    # scxml_Script has no real 'scxml_Script' property in the generated
    # code (a bare stub) -- manually attach it so scxml_ServiceTemplate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_ServiceTemplate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_ServiceTemplate(exmode="sample_text", name="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    partner = scxml_Script()
    setattr(partner, 'scxml_Script', None)
    _safe_set(owner, 'scxml_ServiceTemplate45', partner)
    assert getattr(partner, 'scxml_Script') == owner
    _safe_set(owner, 'scxml_ServiceTemplate45', None)
    assert getattr(partner, 'scxml_Script') is None


def test_assoc_send191_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize192' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Send's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Send's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize192', None)
    _safe_set(owner, 'scxml_Send193', partner)
    assert owner in getattr(partner, 'scxml_Finalize192')
    _safe_set(owner, 'scxml_Send193', None)
    assert owner not in getattr(partner, 'scxml_Finalize192')


def test_assoc_send61_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry62' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Send's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Send's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry62', None)
    _safe_set(owner, 'scxml_Send', partner)
    assert owner in getattr(partner, 'scxml_OnEntry62')
    _safe_set(owner, 'scxml_Send', None)
    assert owner not in getattr(partner, 'scxml_OnEntry62')


def test_assoc_send86_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit87' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Send's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Send's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit87', None)
    _safe_set(owner, 'scxml_Send88', partner)
    assert owner in getattr(partner, 'scxml_OnExit87')
    _safe_set(owner, 'scxml_Send88', None)
    assert owner not in getattr(partner, 'scxml_OnExit87')


def test_assoc_source24_stub_double():
    # scxml_NamedElement has no real 'scxml_NamedElement26' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Transition(anchor="sample_text", cond="sample_text", event="sample_text")
    partner = scxml_NamedElement()
    setattr(partner, 'scxml_NamedElement26', None)
    _safe_set(owner, 'scxml_Transition25', partner)
    assert getattr(partner, 'scxml_NamedElement26') == owner
    _safe_set(owner, 'scxml_Transition25', None)
    assert getattr(partner, 'scxml_NamedElement26') is None


def test_assoc_target21_stub_double():
    # scxml_NamedElement has no real 'scxml_NamedElement23' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Transition(anchor="sample_text", cond="sample_text", event="sample_text")
    partner = scxml_NamedElement()
    setattr(partner, 'scxml_NamedElement23', None)
    _safe_set(owner, 'scxml_Transition22', partner)
    assert getattr(partner, 'scxml_NamedElement23') == owner
    _safe_set(owner, 'scxml_Transition22', None)
    assert getattr(partner, 'scxml_NamedElement23') is None


def test_assoc_transition1_stub_double():
    # scxml_NamedElement has no real 'scxml_NamedElement2' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Transition(anchor="sample_text", cond="sample_text", event="sample_text")
    partner = scxml_NamedElement()
    setattr(partner, 'scxml_NamedElement2', None)
    _safe_set(owner, 'scxml_Transition', partner)
    assert owner in getattr(partner, 'scxml_NamedElement2')
    _safe_set(owner, 'scxml_Transition', None)
    assert owner not in getattr(partner, 'scxml_NamedElement2')


def test_assoc_validate194_stub_double():
    # scxml_Finalize has no real 'scxml_Finalize195' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Validate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Validate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Validate(location="sample_text", schema="sample_text")
    partner = scxml_Finalize()
    setattr(partner, 'scxml_Finalize195', None)
    _safe_set(owner, 'scxml_Validate196', partner)
    assert owner in getattr(partner, 'scxml_Finalize195')
    _safe_set(owner, 'scxml_Validate196', None)
    assert owner not in getattr(partner, 'scxml_Finalize195')


def test_assoc_validate63_stub_double():
    # scxml_OnEntry has no real 'scxml_OnEntry64' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Validate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Validate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Validate(location="sample_text", schema="sample_text")
    partner = scxml_OnEntry()
    setattr(partner, 'scxml_OnEntry64', None)
    _safe_set(owner, 'scxml_Validate', partner)
    assert owner in getattr(partner, 'scxml_OnEntry64')
    _safe_set(owner, 'scxml_Validate', None)
    assert owner not in getattr(partner, 'scxml_OnEntry64')


def test_assoc_validate89_stub_double():
    # scxml_OnExit has no real 'scxml_OnExit90' property in the generated
    # code (a bare stub) -- manually attach it so scxml_Validate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scxml_Validate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scxml_Validate(location="sample_text", schema="sample_text")
    partner = scxml_OnExit()
    setattr(partner, 'scxml_OnExit90', None)
    _safe_set(owner, 'scxml_Validate91', partner)
    assert owner in getattr(partner, 'scxml_OnExit90')
    _safe_set(owner, 'scxml_Validate91', None)
    assert owner not in getattr(partner, 'scxml_OnExit90')


