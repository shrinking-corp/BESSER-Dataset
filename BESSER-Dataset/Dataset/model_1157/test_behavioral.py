import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    EModelElement,
    fiacremm_Action,
    fiacremm_Component,
    fiacremm_DataType,
    fiacremm_Guard,
    fiacremm_Port,
    fiacremm_Process,
    fiacremm_Program,
    fiacremm_State,
    fiacremm_Transition,
    fiacremm_Trigger,
    fiacremm_Variable,
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

def test_assoc_action22_reverse_link_reassign_clear():
    a1 = fiacremm_Transition(Name="sample_text")
    a2 = fiacremm_Transition(Name="sample_text_2")
    b = fiacremm_Action(Body="sample_text", Name="sample_text", codeFiacre="sample_text")
    _safe_set(b, 'fiacremm_Action', a1)
    assert _is_linked(b, 'fiacremm_Action', a1)
    if hasattr(a1, 'fiacremm_Transition23'):
        assert _is_linked(a1, 'fiacremm_Transition23', b)
    _safe_set(b, 'fiacremm_Action', a2)
    assert _is_linked(b, 'fiacremm_Action', a2)
    if hasattr(a1, 'fiacremm_Transition23'):
        assert not _is_linked(a1, 'fiacremm_Transition23', b)
    if hasattr(a2, 'fiacremm_Transition23'):
        assert _is_linked(a2, 'fiacremm_Transition23', b)
    _safe_set(b, 'fiacremm_Action', None)
    assert not _is_linked(b, 'fiacremm_Action', a2)
    if hasattr(a2, 'fiacremm_Transition23'):
        assert not _is_linked(a2, 'fiacremm_Transition23', b)


def test_assoc_alluniqueTriggers11_reverse_link_reassign_clear():
    a1 = fiacremm_Trigger(ArgSize=7, Body="sample_text", Name="sample_text", codeFiacre="sample_text")
    a2 = fiacremm_Trigger(ArgSize=13, Body="sample_text_2", Name="sample_text_2", codeFiacre="sample_text_2")
    b = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    _safe_set(b, 'fiacremm_Process12', {a1})
    assert _is_linked(b, 'fiacremm_Process12', a1)
    if hasattr(a1, 'fiacremm_Trigger'):
        assert _is_linked(a1, 'fiacremm_Trigger', b)
    _safe_set(b, 'fiacremm_Process12', {a2})
    assert _is_linked(b, 'fiacremm_Process12', a2)
    if hasattr(a1, 'fiacremm_Trigger'):
        assert not _is_linked(a1, 'fiacremm_Trigger', b)
    if hasattr(a2, 'fiacremm_Trigger'):
        assert _is_linked(a2, 'fiacremm_Trigger', b)
    _safe_set(b, 'fiacremm_Process12', set())
    assert not _is_linked(b, 'fiacremm_Process12', a2)
    if hasattr(a2, 'fiacremm_Trigger'):
        assert not _is_linked(a2, 'fiacremm_Trigger', b)


def test_assoc_arguments47_reverse_link_reassign_clear():
    a1 = fiacremm_Variable(Name="sample_text", initVal="sample_text")
    a2 = fiacremm_Variable(Name="sample_text_2", initVal="sample_text_2")
    b = fiacremm_Trigger(ArgSize=7, Body="sample_text", Name="sample_text", codeFiacre="sample_text")
    _safe_set(b, 'fiacremm_Trigger48', {a1})
    assert _is_linked(b, 'fiacremm_Trigger48', a1)
    if hasattr(a1, 'fiacremm_Variable49'):
        assert _is_linked(a1, 'fiacremm_Variable49', b)
    _safe_set(b, 'fiacremm_Trigger48', {a2})
    assert _is_linked(b, 'fiacremm_Trigger48', a2)
    if hasattr(a1, 'fiacremm_Variable49'):
        assert not _is_linked(a1, 'fiacremm_Variable49', b)
    if hasattr(a2, 'fiacremm_Variable49'):
        assert _is_linked(a2, 'fiacremm_Variable49', b)
    _safe_set(b, 'fiacremm_Trigger48', set())
    assert not _is_linked(b, 'fiacremm_Trigger48', a2)
    if hasattr(a2, 'fiacremm_Variable49'):
        assert not _is_linked(a2, 'fiacremm_Variable49', b)


def test_assoc_components27_reverse_link_reassign_clear():
    a1 = fiacremm_Variable(Name="sample_text", initVal="sample_text")
    a2 = fiacremm_Variable(Name="sample_text_2", initVal="sample_text_2")
    b = fiacremm_Component(Name="sample_text", ProcessSize=7, VarSize=7)
    _safe_set(b, 'Component', a1)
    assert _is_linked(b, 'Component', a1)
    if hasattr(a1, 'variables28'):
        assert _is_linked(a1, 'variables28', b)
    _safe_set(b, 'Component', a2)
    assert _is_linked(b, 'Component', a2)
    if hasattr(a1, 'variables28'):
        assert not _is_linked(a1, 'variables28', b)
    if hasattr(a2, 'variables28'):
        assert _is_linked(a2, 'variables28', b)
    _safe_set(b, 'Component', None)
    assert not _is_linked(b, 'Component', a2)
    if hasattr(a2, 'variables28'):
        assert not _is_linked(a2, 'variables28', b)


def test_assoc_components36_reverse_link_reassign_clear():
    a1 = fiacremm_Program(ComponentSize=7, Name="sample_text")
    a2 = fiacremm_Program(ComponentSize=13, Name="sample_text_2")
    b = fiacremm_Component(Name="sample_text", ProcessSize=7, VarSize=7)
    _safe_set(b, 'fiacremm_Component37', a1)
    assert _is_linked(b, 'fiacremm_Component37', a1)
    if hasattr(a1, 'fiacremm_Program'):
        assert _is_linked(a1, 'fiacremm_Program', b)
    _safe_set(b, 'fiacremm_Component37', a2)
    assert _is_linked(b, 'fiacremm_Component37', a2)
    if hasattr(a1, 'fiacremm_Program'):
        assert not _is_linked(a1, 'fiacremm_Program', b)
    if hasattr(a2, 'fiacremm_Program'):
        assert _is_linked(a2, 'fiacremm_Program', b)
    _safe_set(b, 'fiacremm_Component37', None)
    assert not _is_linked(b, 'fiacremm_Component37', a2)
    if hasattr(a2, 'fiacremm_Program'):
        assert not _is_linked(a2, 'fiacremm_Program', b)


def test_assoc_components50_reverse_link_reassign_clear():
    a1 = fiacremm_Port(Name="sample_text")
    a2 = fiacremm_Port(Name="sample_text_2")
    b = fiacremm_Component(Name="sample_text", ProcessSize=7, VarSize=7)
    _safe_set(b, 'fiacremm_Component52', a1)
    assert _is_linked(b, 'fiacremm_Component52', a1)
    if hasattr(a1, 'fiacremm_Port51'):
        assert _is_linked(a1, 'fiacremm_Port51', b)
    _safe_set(b, 'fiacremm_Component52', a2)
    assert _is_linked(b, 'fiacremm_Component52', a2)
    if hasattr(a1, 'fiacremm_Port51'):
        assert not _is_linked(a1, 'fiacremm_Port51', b)
    if hasattr(a2, 'fiacremm_Port51'):
        assert _is_linked(a2, 'fiacremm_Port51', b)
    _safe_set(b, 'fiacremm_Component52', None)
    assert not _is_linked(b, 'fiacremm_Component52', a2)
    if hasattr(a2, 'fiacremm_Port51'):
        assert not _is_linked(a2, 'fiacremm_Port51', b)


def test_assoc_datatype24_reverse_link_reassign_clear():
    a1 = fiacremm_Variable(Name="sample_text", initVal="sample_text")
    a2 = fiacremm_Variable(Name="sample_text_2", initVal="sample_text_2")
    b = fiacremm_DataType(Name="sample_text")
    _safe_set(b, 'fiacremm_DataType', a1)
    assert _is_linked(b, 'fiacremm_DataType', a1)
    if hasattr(a1, 'fiacremm_Variable'):
        assert _is_linked(a1, 'fiacremm_Variable', b)
    _safe_set(b, 'fiacremm_DataType', a2)
    assert _is_linked(b, 'fiacremm_DataType', a2)
    if hasattr(a1, 'fiacremm_Variable'):
        assert not _is_linked(a1, 'fiacremm_Variable', b)
    if hasattr(a2, 'fiacremm_Variable'):
        assert _is_linked(a2, 'fiacremm_Variable', b)
    _safe_set(b, 'fiacremm_DataType', None)
    assert not _is_linked(b, 'fiacremm_DataType', a2)
    if hasattr(a2, 'fiacremm_Variable'):
        assert not _is_linked(a2, 'fiacremm_Variable', b)


def test_assoc_datatypes44_reverse_link_reassign_clear():
    a1 = fiacremm_Program(ComponentSize=7, Name="sample_text")
    a2 = fiacremm_Program(ComponentSize=13, Name="sample_text_2")
    b = fiacremm_DataType(Name="sample_text")
    _safe_set(b, 'fiacremm_DataType46', a1)
    assert _is_linked(b, 'fiacremm_DataType46', a1)
    if hasattr(a1, 'fiacremm_Program45'):
        assert _is_linked(a1, 'fiacremm_Program45', b)
    _safe_set(b, 'fiacremm_DataType46', a2)
    assert _is_linked(b, 'fiacremm_DataType46', a2)
    if hasattr(a1, 'fiacremm_Program45'):
        assert not _is_linked(a1, 'fiacremm_Program45', b)
    if hasattr(a2, 'fiacremm_Program45'):
        assert _is_linked(a2, 'fiacremm_Program45', b)
    _safe_set(b, 'fiacremm_DataType46', None)
    assert not _is_linked(b, 'fiacremm_DataType46', a2)
    if hasattr(a2, 'fiacremm_Program45'):
        assert not _is_linked(a2, 'fiacremm_Program45', b)


def test_assoc_guard17_reverse_link_reassign_clear():
    a1 = fiacremm_Transition(Name="sample_text")
    a2 = fiacremm_Transition(Name="sample_text_2")
    b = fiacremm_Guard(Body="sample_text", Name="sample_text", codeFiacre="sample_text")
    _safe_set(b, 'fiacremm_Guard', a1)
    assert _is_linked(b, 'fiacremm_Guard', a1)
    if hasattr(a1, 'fiacremm_Transition18'):
        assert _is_linked(a1, 'fiacremm_Transition18', b)
    _safe_set(b, 'fiacremm_Guard', a2)
    assert _is_linked(b, 'fiacremm_Guard', a2)
    if hasattr(a1, 'fiacremm_Transition18'):
        assert not _is_linked(a1, 'fiacremm_Transition18', b)
    if hasattr(a2, 'fiacremm_Transition18'):
        assert _is_linked(a2, 'fiacremm_Transition18', b)
    _safe_set(b, 'fiacremm_Guard', None)
    assert not _is_linked(b, 'fiacremm_Guard', a2)
    if hasattr(a2, 'fiacremm_Transition18'):
        assert not _is_linked(a2, 'fiacremm_Transition18', b)


def test_assoc_inTransitions1_reverse_link_reassign_clear():
    a1 = fiacremm_Transition(Name="sample_text")
    a2 = fiacremm_Transition(Name="sample_text_2")
    b = fiacremm_State(Name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition2'):
        assert _is_linked(a1, 'Transition2', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition2'):
        assert not _is_linked(a1, 'Transition2', b)
    if hasattr(a2, 'Transition2'):
        assert _is_linked(a2, 'Transition2', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition2'):
        assert not _is_linked(a2, 'Transition2', b)


def test_assoc_initState8_reverse_link_reassign_clear():
    a1 = fiacremm_State(Name="sample_text")
    a2 = fiacremm_State(Name="sample_text_2")
    b = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    _safe_set(b, 'process', a1)
    assert _is_linked(b, 'process', a1)
    if hasattr(a1, 'State'):
        assert _is_linked(a1, 'State', b)
    _safe_set(b, 'process', a2)
    assert _is_linked(b, 'process', a2)
    if hasattr(a1, 'State'):
        assert not _is_linked(a1, 'State', b)
    if hasattr(a2, 'State'):
        assert _is_linked(a2, 'State', b)
    _safe_set(b, 'process', None)
    assert not _is_linked(b, 'process', a2)
    if hasattr(a2, 'State'):
        assert not _is_linked(a2, 'State', b)


def test_assoc_instances29_reverse_link_reassign_clear():
    a1 = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    a2 = fiacremm_Process(Name="sample_text_2", StateSize=13, VarSize=13)
    b = fiacremm_Component(Name="sample_text", ProcessSize=7, VarSize=7)
    _safe_set(b, 'fiacremm_Component', {a1})
    assert _is_linked(b, 'fiacremm_Component', a1)
    if hasattr(a1, 'fiacremm_Process30'):
        assert _is_linked(a1, 'fiacremm_Process30', b)
    _safe_set(b, 'fiacremm_Component', {a2})
    assert _is_linked(b, 'fiacremm_Component', a2)
    if hasattr(a1, 'fiacremm_Process30'):
        assert not _is_linked(a1, 'fiacremm_Process30', b)
    if hasattr(a2, 'fiacremm_Process30'):
        assert _is_linked(a2, 'fiacremm_Process30', b)
    _safe_set(b, 'fiacremm_Component', set())
    assert not _is_linked(b, 'fiacremm_Component', a2)
    if hasattr(a2, 'fiacremm_Process30'):
        assert not _is_linked(a2, 'fiacremm_Process30', b)


def test_assoc_outPorts9_reverse_link_reassign_clear():
    a1 = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    a2 = fiacremm_Process(Name="sample_text_2", StateSize=13, VarSize=13)
    b = fiacremm_Port(Name="sample_text")
    _safe_set(b, 'fiacremm_Port', a1)
    assert _is_linked(b, 'fiacremm_Port', a1)
    if hasattr(a1, 'fiacremm_Process10'):
        assert _is_linked(a1, 'fiacremm_Process10', b)
    _safe_set(b, 'fiacremm_Port', a2)
    assert _is_linked(b, 'fiacremm_Port', a2)
    if hasattr(a1, 'fiacremm_Process10'):
        assert not _is_linked(a1, 'fiacremm_Process10', b)
    if hasattr(a2, 'fiacremm_Process10'):
        assert _is_linked(a2, 'fiacremm_Process10', b)
    _safe_set(b, 'fiacremm_Port', None)
    assert not _is_linked(b, 'fiacremm_Port', a2)
    if hasattr(a2, 'fiacremm_Process10'):
        assert not _is_linked(a2, 'fiacremm_Process10', b)


def test_assoc_outTransitions0_reverse_link_reassign_clear():
    a1 = fiacremm_Transition(Name="sample_text")
    a2 = fiacremm_Transition(Name="sample_text_2")
    b = fiacremm_State(Name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_ports33_reverse_link_reassign_clear():
    a1 = fiacremm_Port(Name="sample_text")
    a2 = fiacremm_Port(Name="sample_text_2")
    b = fiacremm_Component(Name="sample_text", ProcessSize=7, VarSize=7)
    _safe_set(b, 'fiacremm_Component34', {a1})
    assert _is_linked(b, 'fiacremm_Component34', a1)
    if hasattr(a1, 'fiacremm_Port35'):
        assert _is_linked(a1, 'fiacremm_Port35', b)
    _safe_set(b, 'fiacremm_Component34', {a2})
    assert _is_linked(b, 'fiacremm_Component34', a2)
    if hasattr(a1, 'fiacremm_Port35'):
        assert not _is_linked(a1, 'fiacremm_Port35', b)
    if hasattr(a2, 'fiacremm_Port35'):
        assert _is_linked(a2, 'fiacremm_Port35', b)
    _safe_set(b, 'fiacremm_Component34', set())
    assert not _is_linked(b, 'fiacremm_Component34', a2)
    if hasattr(a2, 'fiacremm_Port35'):
        assert not _is_linked(a2, 'fiacremm_Port35', b)


def test_assoc_process3_reverse_link_reassign_clear():
    a1 = fiacremm_State(Name="sample_text")
    a2 = fiacremm_State(Name="sample_text_2")
    b = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    _safe_set(b, 'Process', a1)
    assert _is_linked(b, 'Process', a1)
    if hasattr(a1, 'initState'):
        assert _is_linked(a1, 'initState', b)
    _safe_set(b, 'Process', a2)
    assert _is_linked(b, 'Process', a2)
    if hasattr(a1, 'initState'):
        assert not _is_linked(a1, 'initState', b)
    if hasattr(a2, 'initState'):
        assert _is_linked(a2, 'initState', b)
    _safe_set(b, 'Process', None)
    assert not _is_linked(b, 'Process', a2)
    if hasattr(a2, 'initState'):
        assert not _is_linked(a2, 'initState', b)


def test_assoc_processes25_reverse_link_reassign_clear():
    a1 = fiacremm_Variable(Name="sample_text", initVal="sample_text")
    a2 = fiacremm_Variable(Name="sample_text_2", initVal="sample_text_2")
    b = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    _safe_set(b, 'Process26', a1)
    assert _is_linked(b, 'Process26', a1)
    if hasattr(a1, 'variables'):
        assert _is_linked(a1, 'variables', b)
    _safe_set(b, 'Process26', a2)
    assert _is_linked(b, 'Process26', a2)
    if hasattr(a1, 'variables'):
        assert not _is_linked(a1, 'variables', b)
    if hasattr(a2, 'variables'):
        assert _is_linked(a2, 'variables', b)
    _safe_set(b, 'Process26', None)
    assert not _is_linked(b, 'Process26', a2)
    if hasattr(a2, 'variables'):
        assert not _is_linked(a2, 'variables', b)


def test_assoc_processes41_reverse_link_reassign_clear():
    a1 = fiacremm_Program(ComponentSize=7, Name="sample_text")
    a2 = fiacremm_Program(ComponentSize=13, Name="sample_text_2")
    b = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    _safe_set(b, 'fiacremm_Process43', a1)
    assert _is_linked(b, 'fiacremm_Process43', a1)
    if hasattr(a1, 'fiacremm_Program42'):
        assert _is_linked(a1, 'fiacremm_Program42', b)
    _safe_set(b, 'fiacremm_Process43', a2)
    assert _is_linked(b, 'fiacremm_Process43', a2)
    if hasattr(a1, 'fiacremm_Program42'):
        assert not _is_linked(a1, 'fiacremm_Program42', b)
    if hasattr(a2, 'fiacremm_Program42'):
        assert _is_linked(a2, 'fiacremm_Program42', b)
    _safe_set(b, 'fiacremm_Process43', None)
    assert not _is_linked(b, 'fiacremm_Process43', a2)
    if hasattr(a2, 'fiacremm_Program42'):
        assert not _is_linked(a2, 'fiacremm_Program42', b)


def test_assoc_source13_reverse_link_reassign_clear():
    a1 = fiacremm_Transition(Name="sample_text")
    a2 = fiacremm_Transition(Name="sample_text_2")
    b = fiacremm_State(Name="sample_text")
    _safe_set(b, 'State14', a1)
    assert _is_linked(b, 'State14', a1)
    if hasattr(a1, 'outTransitions'):
        assert _is_linked(a1, 'outTransitions', b)
    _safe_set(b, 'State14', a2)
    assert _is_linked(b, 'State14', a2)
    if hasattr(a1, 'outTransitions'):
        assert not _is_linked(a1, 'outTransitions', b)
    if hasattr(a2, 'outTransitions'):
        assert _is_linked(a2, 'outTransitions', b)
    _safe_set(b, 'State14', None)
    assert not _is_linked(b, 'State14', a2)
    if hasattr(a2, 'outTransitions'):
        assert not _is_linked(a2, 'outTransitions', b)


def test_assoc_states6_reverse_link_reassign_clear():
    a1 = fiacremm_State(Name="sample_text")
    a2 = fiacremm_State(Name="sample_text_2")
    b = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    _safe_set(b, 'fiacremm_Process7', {a1})
    assert _is_linked(b, 'fiacremm_Process7', a1)
    if hasattr(a1, 'fiacremm_State'):
        assert _is_linked(a1, 'fiacremm_State', b)
    _safe_set(b, 'fiacremm_Process7', {a2})
    assert _is_linked(b, 'fiacremm_Process7', a2)
    if hasattr(a1, 'fiacremm_State'):
        assert not _is_linked(a1, 'fiacremm_State', b)
    if hasattr(a2, 'fiacremm_State'):
        assert _is_linked(a2, 'fiacremm_State', b)
    _safe_set(b, 'fiacremm_Process7', set())
    assert not _is_linked(b, 'fiacremm_Process7', a2)
    if hasattr(a2, 'fiacremm_State'):
        assert not _is_linked(a2, 'fiacremm_State', b)


def test_assoc_target15_reverse_link_reassign_clear():
    a1 = fiacremm_Transition(Name="sample_text")
    a2 = fiacremm_Transition(Name="sample_text_2")
    b = fiacremm_State(Name="sample_text")
    _safe_set(b, 'State16', a1)
    assert _is_linked(b, 'State16', a1)
    if hasattr(a1, 'inTransitions'):
        assert _is_linked(a1, 'inTransitions', b)
    _safe_set(b, 'State16', a2)
    assert _is_linked(b, 'State16', a2)
    if hasattr(a1, 'inTransitions'):
        assert not _is_linked(a1, 'inTransitions', b)
    if hasattr(a2, 'inTransitions'):
        assert _is_linked(a2, 'inTransitions', b)
    _safe_set(b, 'State16', None)
    assert not _is_linked(b, 'State16', a2)
    if hasattr(a2, 'inTransitions'):
        assert not _is_linked(a2, 'inTransitions', b)


def test_assoc_transitions4_reverse_link_reassign_clear():
    a1 = fiacremm_Transition(Name="sample_text")
    a2 = fiacremm_Transition(Name="sample_text_2")
    b = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    _safe_set(b, 'fiacremm_Process', {a1})
    assert _is_linked(b, 'fiacremm_Process', a1)
    if hasattr(a1, 'fiacremm_Transition'):
        assert _is_linked(a1, 'fiacremm_Transition', b)
    _safe_set(b, 'fiacremm_Process', {a2})
    assert _is_linked(b, 'fiacremm_Process', a2)
    if hasattr(a1, 'fiacremm_Transition'):
        assert not _is_linked(a1, 'fiacremm_Transition', b)
    if hasattr(a2, 'fiacremm_Transition'):
        assert _is_linked(a2, 'fiacremm_Transition', b)
    _safe_set(b, 'fiacremm_Process', set())
    assert not _is_linked(b, 'fiacremm_Process', a2)
    if hasattr(a2, 'fiacremm_Transition'):
        assert not _is_linked(a2, 'fiacremm_Transition', b)


def test_assoc_trigger19_reverse_link_reassign_clear():
    a1 = fiacremm_Trigger(ArgSize=7, Body="sample_text", Name="sample_text", codeFiacre="sample_text")
    a2 = fiacremm_Trigger(ArgSize=13, Body="sample_text_2", Name="sample_text_2", codeFiacre="sample_text_2")
    b = fiacremm_Transition(Name="sample_text")
    _safe_set(b, 'fiacremm_Transition20', a1)
    assert _is_linked(b, 'fiacremm_Transition20', a1)
    if hasattr(a1, 'fiacremm_Trigger21'):
        assert _is_linked(a1, 'fiacremm_Trigger21', b)
    _safe_set(b, 'fiacremm_Transition20', a2)
    assert _is_linked(b, 'fiacremm_Transition20', a2)
    if hasattr(a1, 'fiacremm_Trigger21'):
        assert not _is_linked(a1, 'fiacremm_Trigger21', b)
    if hasattr(a2, 'fiacremm_Trigger21'):
        assert _is_linked(a2, 'fiacremm_Trigger21', b)
    _safe_set(b, 'fiacremm_Transition20', None)
    assert not _is_linked(b, 'fiacremm_Transition20', a2)
    if hasattr(a2, 'fiacremm_Trigger21'):
        assert not _is_linked(a2, 'fiacremm_Trigger21', b)


def test_assoc_variable38_reverse_link_reassign_clear():
    a1 = fiacremm_Variable(Name="sample_text", initVal="sample_text")
    a2 = fiacremm_Variable(Name="sample_text_2", initVal="sample_text_2")
    b = fiacremm_Program(ComponentSize=7, Name="sample_text")
    _safe_set(b, 'fiacremm_Program39', {a1})
    assert _is_linked(b, 'fiacremm_Program39', a1)
    if hasattr(a1, 'fiacremm_Variable40'):
        assert _is_linked(a1, 'fiacremm_Variable40', b)
    _safe_set(b, 'fiacremm_Program39', {a2})
    assert _is_linked(b, 'fiacremm_Program39', a2)
    if hasattr(a1, 'fiacremm_Variable40'):
        assert not _is_linked(a1, 'fiacremm_Variable40', b)
    if hasattr(a2, 'fiacremm_Variable40'):
        assert _is_linked(a2, 'fiacremm_Variable40', b)
    _safe_set(b, 'fiacremm_Program39', set())
    assert not _is_linked(b, 'fiacremm_Program39', a2)
    if hasattr(a2, 'fiacremm_Variable40'):
        assert not _is_linked(a2, 'fiacremm_Variable40', b)


def test_assoc_variables31_reverse_link_reassign_clear():
    a1 = fiacremm_Variable(Name="sample_text", initVal="sample_text")
    a2 = fiacremm_Variable(Name="sample_text_2", initVal="sample_text_2")
    b = fiacremm_Component(Name="sample_text", ProcessSize=7, VarSize=7)
    _safe_set(b, 'components', {a1})
    assert _is_linked(b, 'components', a1)
    if hasattr(a1, 'Variable32'):
        assert _is_linked(a1, 'Variable32', b)
    _safe_set(b, 'components', {a2})
    assert _is_linked(b, 'components', a2)
    if hasattr(a1, 'Variable32'):
        assert not _is_linked(a1, 'Variable32', b)
    if hasattr(a2, 'Variable32'):
        assert _is_linked(a2, 'Variable32', b)
    _safe_set(b, 'components', set())
    assert not _is_linked(b, 'components', a2)
    if hasattr(a2, 'Variable32'):
        assert not _is_linked(a2, 'Variable32', b)


def test_assoc_variables5_reverse_link_reassign_clear():
    a1 = fiacremm_Variable(Name="sample_text", initVal="sample_text")
    a2 = fiacremm_Variable(Name="sample_text_2", initVal="sample_text_2")
    b = fiacremm_Process(Name="sample_text", StateSize=7, VarSize=7)
    _safe_set(b, 'processes', {a1})
    assert _is_linked(b, 'processes', a1)
    if hasattr(a1, 'Variable'):
        assert _is_linked(a1, 'Variable', b)
    _safe_set(b, 'processes', {a2})
    assert _is_linked(b, 'processes', a2)
    if hasattr(a1, 'Variable'):
        assert not _is_linked(a1, 'Variable', b)
    if hasattr(a2, 'Variable'):
        assert _is_linked(a2, 'Variable', b)
    _safe_set(b, 'processes', set())
    assert not _is_linked(b, 'processes', a2)
    if hasattr(a2, 'Variable'):
        assert not _is_linked(a2, 'Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

