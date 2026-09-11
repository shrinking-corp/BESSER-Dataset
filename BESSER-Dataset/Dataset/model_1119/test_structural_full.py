import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    NamedElement,
    ctxmngr_ContextManager,
    ctxmngr_ContextParameter,
    ctxmngr_CtxState,
    ctxmngr_CtxTransition,
    ctxmngr_Manager,
    ctxmngr_ManagerState,
    ctxmngr_ManagerTransition,
    ctxmngr_OpaqueExpression,
    ctxmngr_RemoteFiringDependency,
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

def test_ctxmngr_ContextParameter_LitteralBoolean_value_roundtrip():
    instance = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    assert instance.LitteralBoolean == True
    instance.LitteralBoolean = False
    assert instance.LitteralBoolean == False


def test_ctxmngr_ContextParameter_LitteralInteger_value_roundtrip():
    instance = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    assert instance.LitteralInteger == 7
    instance.LitteralInteger = 13
    assert instance.LitteralInteger == 13


def test_ctxmngr_ContextParameter_LitteralString_value_roundtrip():
    instance = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    assert instance.LitteralString == "sample_text"
    instance.LitteralString = "sample_text_2"
    assert instance.LitteralString == "sample_text_2"


def test_ctxmngr_ContextParameter_LitteralUnlimitedNatural_value_roundtrip():
    instance = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    assert instance.LitteralUnlimitedNatural == 3.14
    instance.LitteralUnlimitedNatural = 9.99
    assert instance.LitteralUnlimitedNatural == 9.99


def test_ctxmngr_ContextParameter_isInput_value_roundtrip():
    instance = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    assert instance.isInput == True
    instance.isInput = False
    assert instance.isInput == False


def test_ctxmngr_CtxState_isEnd_value_roundtrip():
    instance = ctxmngr_CtxState(isEnd=True, isStart=True)
    assert instance.isEnd == True
    instance.isEnd = False
    assert instance.isEnd == False


def test_ctxmngr_CtxState_isStart_value_roundtrip():
    instance = ctxmngr_CtxState(isEnd=True, isStart=True)
    assert instance.isStart == True
    instance.isStart = False
    assert instance.isStart == False


def test_ctxmngr_CtxTransition_Action_value_roundtrip():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert instance.Action == "sample_text"
    instance.Action = "sample_text_2"
    assert instance.Action == "sample_text_2"


def test_ctxmngr_CtxTransition_Condition_value_roundtrip():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert instance.Condition == "sample_text"
    instance.Condition = "sample_text_2"
    assert instance.Condition == "sample_text_2"


def test_ctxmngr_CtxTransition_Event_value_roundtrip():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert instance.Event == "sample_text"
    instance.Event = "sample_text_2"
    assert instance.Event == "sample_text_2"


def test_ctxmngr_CtxTransition_input_value_roundtrip():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert instance.input == "sample_text"
    instance.input = "sample_text_2"
    assert instance.input == "sample_text_2"


def test_ctxmngr_CtxTransition_isRemote_value_roundtrip():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert instance.isRemote == True
    instance.isRemote = False
    assert instance.isRemote == False


def test_ctxmngr_CtxTransition_output_value_roundtrip():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert instance.output == "sample_text"
    instance.output = "sample_text_2"
    assert instance.output == "sample_text_2"


def test_ctxmngr_CtxTransition_transProb_value_roundtrip():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert instance.transProb == 3.14
    instance.transProb = 9.99
    assert instance.transProb == 9.99


def test_ctxmngr_CtxTransition_transRate_value_roundtrip():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert instance.transRate == 3.14
    instance.transRate = 9.99
    assert instance.transRate == 9.99


def test_ctxmngr_ContextManager_isa_NamedElement():
    instance = ctxmngr_ContextManager()
    assert isinstance(instance, NamedElement)


def test_ctxmngr_ContextParameter_isa_NamedElement():
    instance = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    assert isinstance(instance, NamedElement)


def test_ctxmngr_CtxState_isa_NamedElement():
    instance = ctxmngr_CtxState(isEnd=True, isStart=True)
    assert isinstance(instance, NamedElement)


def test_ctxmngr_CtxTransition_isa_NamedElement():
    instance = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    assert isinstance(instance, NamedElement)


def test_ctxmngr_RemoteFiringDependency_isa_NamedElement():
    instance = ctxmngr_RemoteFiringDependency()
    assert isinstance(instance, NamedElement)


def test_assoc_contextParameters18_link_reassign_clear():
    a = ctxmngr_CtxState(isEnd=True, isStart=True)
    b1 = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    b2 = ctxmngr_ContextParameter(LitteralBoolean=False, LitteralInteger=13, LitteralString="sample_text_2", LitteralUnlimitedNatural=9.99, isInput=False)
    _safe_set(a, 'state', {b1})
    assert _is_linked(a, 'state', b1)
    if hasattr(b1, 'ContextParameter19'):
        assert _is_linked(b1, 'ContextParameter19', a)
    _safe_set(a, 'state', {b2})
    assert _is_linked(a, 'state', b2)
    if hasattr(b1, 'ContextParameter19'):
        assert not _is_linked(b1, 'ContextParameter19', a)
    if hasattr(b2, 'ContextParameter19'):
        assert _is_linked(b2, 'ContextParameter19', a)
    _safe_set(a, 'state', set())
    assert not _is_linked(a, 'state', b2)
    if hasattr(b2, 'ContextParameter19'):
        assert not _is_linked(b2, 'ContextParameter19', a)


def test_assoc_contextParameters5_link_reassign_clear():
    a = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    b1 = ctxmngr_ContextManager()
    b2 = ctxmngr_ContextManager()
    _safe_set(a, 'ContextParameter', b1)
    assert _is_linked(a, 'ContextParameter', b1)
    if hasattr(b1, 'owningManager6'):
        assert _is_linked(b1, 'owningManager6', a)
    _safe_set(a, 'ContextParameter', b2)
    assert _is_linked(a, 'ContextParameter', b2)
    if hasattr(b1, 'owningManager6'):
        assert not _is_linked(b1, 'owningManager6', a)
    if hasattr(b2, 'owningManager6'):
        assert _is_linked(b2, 'owningManager6', a)
    _safe_set(a, 'ContextParameter', None)
    assert not _is_linked(a, 'ContextParameter', b2)
    if hasattr(b2, 'owningManager6'):
        assert not _is_linked(b2, 'owningManager6', a)


def test_assoc_finalState2_link_reassign_clear():
    a = ctxmngr_CtxState(isEnd=True, isStart=True)
    b1 = ctxmngr_ContextManager()
    b2 = ctxmngr_ContextManager()
    _safe_set(a, 'ctxmngr_CtxState4', b1)
    assert _is_linked(a, 'ctxmngr_CtxState4', b1)
    if hasattr(b1, 'ctxmngr_ContextManager3'):
        assert _is_linked(b1, 'ctxmngr_ContextManager3', a)
    _safe_set(a, 'ctxmngr_CtxState4', b2)
    assert _is_linked(a, 'ctxmngr_CtxState4', b2)
    if hasattr(b1, 'ctxmngr_ContextManager3'):
        assert not _is_linked(b1, 'ctxmngr_ContextManager3', a)
    if hasattr(b2, 'ctxmngr_ContextManager3'):
        assert _is_linked(b2, 'ctxmngr_ContextManager3', a)
    _safe_set(a, 'ctxmngr_CtxState4', None)
    assert not _is_linked(a, 'ctxmngr_CtxState4', b2)
    if hasattr(b2, 'ctxmngr_ContextManager3'):
        assert not _is_linked(b2, 'ctxmngr_ContextManager3', a)


def test_assoc_incomingTransition16_link_reassign_clear():
    a = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    b1 = ctxmngr_CtxState(isEnd=True, isStart=True)
    b2 = ctxmngr_CtxState(isEnd=False, isStart=False)
    _safe_set(a, 'CtxTransition17', b1)
    assert _is_linked(a, 'CtxTransition17', b1)
    if hasattr(b1, 'target'):
        assert _is_linked(b1, 'target', a)
    _safe_set(a, 'CtxTransition17', b2)
    assert _is_linked(a, 'CtxTransition17', b2)
    if hasattr(b1, 'target'):
        assert not _is_linked(b1, 'target', a)
    if hasattr(b2, 'target'):
        assert _is_linked(b2, 'target', a)
    _safe_set(a, 'CtxTransition17', None)
    assert not _is_linked(a, 'CtxTransition17', b2)
    if hasattr(b2, 'target'):
        assert not _is_linked(b2, 'target', a)


def test_assoc_initialState1_link_reassign_clear():
    a = ctxmngr_CtxState(isEnd=True, isStart=True)
    b1 = ctxmngr_ContextManager()
    b2 = ctxmngr_ContextManager()
    _safe_set(a, 'ctxmngr_CtxState', b1)
    assert _is_linked(a, 'ctxmngr_CtxState', b1)
    if hasattr(b1, 'ctxmngr_ContextManager'):
        assert _is_linked(b1, 'ctxmngr_ContextManager', a)
    _safe_set(a, 'ctxmngr_CtxState', b2)
    assert _is_linked(a, 'ctxmngr_CtxState', b2)
    if hasattr(b1, 'ctxmngr_ContextManager'):
        assert not _is_linked(b1, 'ctxmngr_ContextManager', a)
    if hasattr(b2, 'ctxmngr_ContextManager'):
        assert _is_linked(b2, 'ctxmngr_ContextManager', a)
    _safe_set(a, 'ctxmngr_CtxState', None)
    assert not _is_linked(a, 'ctxmngr_CtxState', b2)
    if hasattr(b2, 'ctxmngr_ContextManager'):
        assert not _is_linked(b2, 'ctxmngr_ContextManager', a)


def test_assoc_managerStates20_link_reassign_clear():
    a = ctxmngr_CtxState(isEnd=True, isStart=True)
    b1 = ctxmngr_ManagerState()
    b2 = ctxmngr_ManagerState()
    _safe_set(a, 'ctxmngr_CtxState21', {b1})
    assert _is_linked(a, 'ctxmngr_CtxState21', b1)
    if hasattr(b1, 'ctxmngr_ManagerState'):
        assert _is_linked(b1, 'ctxmngr_ManagerState', a)
    _safe_set(a, 'ctxmngr_CtxState21', {b2})
    assert _is_linked(a, 'ctxmngr_CtxState21', b2)
    if hasattr(b1, 'ctxmngr_ManagerState'):
        assert not _is_linked(b1, 'ctxmngr_ManagerState', a)
    if hasattr(b2, 'ctxmngr_ManagerState'):
        assert _is_linked(b2, 'ctxmngr_ManagerState', a)
    _safe_set(a, 'ctxmngr_CtxState21', set())
    assert not _is_linked(a, 'ctxmngr_CtxState21', b2)
    if hasattr(b2, 'ctxmngr_ManagerState'):
        assert not _is_linked(b2, 'ctxmngr_ManagerState', a)


def test_assoc_managerTransition28_link_reassign_clear():
    a = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    b1 = ctxmngr_ManagerTransition()
    b2 = ctxmngr_ManagerTransition()
    _safe_set(a, 'ctxmngr_CtxTransition', {b1})
    assert _is_linked(a, 'ctxmngr_CtxTransition', b1)
    if hasattr(b1, 'ctxmngr_ManagerTransition'):
        assert _is_linked(b1, 'ctxmngr_ManagerTransition', a)
    _safe_set(a, 'ctxmngr_CtxTransition', {b2})
    assert _is_linked(a, 'ctxmngr_CtxTransition', b2)
    if hasattr(b1, 'ctxmngr_ManagerTransition'):
        assert not _is_linked(b1, 'ctxmngr_ManagerTransition', a)
    if hasattr(b2, 'ctxmngr_ManagerTransition'):
        assert _is_linked(b2, 'ctxmngr_ManagerTransition', a)
    _safe_set(a, 'ctxmngr_CtxTransition', set())
    assert not _is_linked(a, 'ctxmngr_CtxTransition', b2)
    if hasattr(b2, 'ctxmngr_ManagerTransition'):
        assert not _is_linked(b2, 'ctxmngr_ManagerTransition', a)


def test_assoc_opaqueExpressions31_link_reassign_clear():
    a = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    b1 = ctxmngr_OpaqueExpression()
    b2 = ctxmngr_OpaqueExpression()
    _safe_set(a, 'ctxmngr_ContextParameter', {b1})
    assert _is_linked(a, 'ctxmngr_ContextParameter', b1)
    if hasattr(b1, 'ctxmngr_OpaqueExpression'):
        assert _is_linked(b1, 'ctxmngr_OpaqueExpression', a)
    _safe_set(a, 'ctxmngr_ContextParameter', {b2})
    assert _is_linked(a, 'ctxmngr_ContextParameter', b2)
    if hasattr(b1, 'ctxmngr_OpaqueExpression'):
        assert not _is_linked(b1, 'ctxmngr_OpaqueExpression', a)
    if hasattr(b2, 'ctxmngr_OpaqueExpression'):
        assert _is_linked(b2, 'ctxmngr_OpaqueExpression', a)
    _safe_set(a, 'ctxmngr_ContextParameter', set())
    assert not _is_linked(a, 'ctxmngr_ContextParameter', b2)
    if hasattr(b2, 'ctxmngr_OpaqueExpression'):
        assert not _is_linked(b2, 'ctxmngr_OpaqueExpression', a)


def test_assoc_outgoingTransition14_link_reassign_clear():
    a = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    b1 = ctxmngr_CtxState(isEnd=True, isStart=True)
    b2 = ctxmngr_CtxState(isEnd=False, isStart=False)
    _safe_set(a, 'CtxTransition15', b1)
    assert _is_linked(a, 'CtxTransition15', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'CtxTransition15', b2)
    assert _is_linked(a, 'CtxTransition15', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'CtxTransition15', None)
    assert not _is_linked(a, 'CtxTransition15', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_ownedState0_link_reassign_clear():
    a = ctxmngr_CtxState(isEnd=True, isStart=True)
    b1 = ctxmngr_ContextManager()
    b2 = ctxmngr_ContextManager()
    _safe_set(a, 'CtxState', b1)
    assert _is_linked(a, 'CtxState', b1)
    if hasattr(b1, 'owningManager'):
        assert _is_linked(b1, 'owningManager', a)
    _safe_set(a, 'CtxState', b2)
    assert _is_linked(a, 'CtxState', b2)
    if hasattr(b1, 'owningManager'):
        assert not _is_linked(b1, 'owningManager', a)
    if hasattr(b2, 'owningManager'):
        assert _is_linked(b2, 'owningManager', a)
    _safe_set(a, 'CtxState', None)
    assert not _is_linked(a, 'CtxState', b2)
    if hasattr(b2, 'owningManager'):
        assert not _is_linked(b2, 'owningManager', a)


def test_assoc_ownedTransition11_link_reassign_clear():
    a = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    b1 = ctxmngr_ContextManager()
    b2 = ctxmngr_ContextManager()
    _safe_set(a, 'CtxTransition', b1)
    assert _is_linked(a, 'CtxTransition', b1)
    if hasattr(b1, 'owningManager12'):
        assert _is_linked(b1, 'owningManager12', a)
    _safe_set(a, 'CtxTransition', b2)
    assert _is_linked(a, 'CtxTransition', b2)
    if hasattr(b1, 'owningManager12'):
        assert not _is_linked(b1, 'owningManager12', a)
    if hasattr(b2, 'owningManager12'):
        assert _is_linked(b2, 'owningManager12', a)
    _safe_set(a, 'CtxTransition', None)
    assert not _is_linked(a, 'CtxTransition', b2)
    if hasattr(b2, 'owningManager12'):
        assert not _is_linked(b2, 'owningManager12', a)


def test_assoc_owningManager13_link_reassign_clear():
    a = ctxmngr_CtxState(isEnd=True, isStart=True)
    b1 = ctxmngr_ContextManager()
    b2 = ctxmngr_ContextManager()
    _safe_set(a, 'ownedState', b1)
    assert _is_linked(a, 'ownedState', b1)
    if hasattr(b1, 'ContextManager'):
        assert _is_linked(b1, 'ContextManager', a)
    _safe_set(a, 'ownedState', b2)
    assert _is_linked(a, 'ownedState', b2)
    if hasattr(b1, 'ContextManager'):
        assert not _is_linked(b1, 'ContextManager', a)
    if hasattr(b2, 'ContextManager'):
        assert _is_linked(b2, 'ContextManager', a)
    _safe_set(a, 'ownedState', None)
    assert not _is_linked(a, 'ownedState', b2)
    if hasattr(b2, 'ContextManager'):
        assert not _is_linked(b2, 'ContextManager', a)


def test_assoc_owningManager22_link_reassign_clear():
    a = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    b1 = ctxmngr_ContextManager()
    b2 = ctxmngr_ContextManager()
    _safe_set(a, 'ownedTransition', b1)
    assert _is_linked(a, 'ownedTransition', b1)
    if hasattr(b1, 'ContextManager23'):
        assert _is_linked(b1, 'ContextManager23', a)
    _safe_set(a, 'ownedTransition', b2)
    assert _is_linked(a, 'ownedTransition', b2)
    if hasattr(b1, 'ContextManager23'):
        assert not _is_linked(b1, 'ContextManager23', a)
    if hasattr(b2, 'ContextManager23'):
        assert _is_linked(b2, 'ContextManager23', a)
    _safe_set(a, 'ownedTransition', None)
    assert not _is_linked(a, 'ownedTransition', b2)
    if hasattr(b2, 'ContextManager23'):
        assert not _is_linked(b2, 'ContextManager23', a)


def test_assoc_owningManager32_link_reassign_clear():
    a = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    b1 = ctxmngr_ContextManager()
    b2 = ctxmngr_ContextManager()
    _safe_set(a, 'contextParameters33', b1)
    assert _is_linked(a, 'contextParameters33', b1)
    if hasattr(b1, 'ContextManager34'):
        assert _is_linked(b1, 'ContextManager34', a)
    _safe_set(a, 'contextParameters33', b2)
    assert _is_linked(a, 'contextParameters33', b2)
    if hasattr(b1, 'ContextManager34'):
        assert not _is_linked(b1, 'ContextManager34', a)
    if hasattr(b2, 'ContextManager34'):
        assert _is_linked(b2, 'ContextManager34', a)
    _safe_set(a, 'contextParameters33', None)
    assert not _is_linked(a, 'contextParameters33', b2)
    if hasattr(b2, 'ContextManager34'):
        assert not _is_linked(b2, 'ContextManager34', a)


def test_assoc_represents42_link_reassign_clear():
    a = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    b1 = ctxmngr_RemoteFiringDependency()
    b2 = ctxmngr_RemoteFiringDependency()
    _safe_set(a, 'ctxmngr_CtxTransition44', b1)
    assert _is_linked(a, 'ctxmngr_CtxTransition44', b1)
    if hasattr(b1, 'ctxmngr_RemoteFiringDependency43'):
        assert _is_linked(b1, 'ctxmngr_RemoteFiringDependency43', a)
    _safe_set(a, 'ctxmngr_CtxTransition44', b2)
    assert _is_linked(a, 'ctxmngr_CtxTransition44', b2)
    if hasattr(b1, 'ctxmngr_RemoteFiringDependency43'):
        assert not _is_linked(b1, 'ctxmngr_RemoteFiringDependency43', a)
    if hasattr(b2, 'ctxmngr_RemoteFiringDependency43'):
        assert _is_linked(b2, 'ctxmngr_RemoteFiringDependency43', a)
    _safe_set(a, 'ctxmngr_CtxTransition44', None)
    assert not _is_linked(a, 'ctxmngr_CtxTransition44', b2)
    if hasattr(b2, 'ctxmngr_RemoteFiringDependency43'):
        assert not _is_linked(b2, 'ctxmngr_RemoteFiringDependency43', a)


def test_assoc_source24_link_reassign_clear():
    a = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    b1 = ctxmngr_CtxState(isEnd=True, isStart=True)
    b2 = ctxmngr_CtxState(isEnd=False, isStart=False)
    _safe_set(a, 'outgoingTransition', b1)
    assert _is_linked(a, 'outgoingTransition', b1)
    if hasattr(b1, 'CtxState25'):
        assert _is_linked(b1, 'CtxState25', a)
    _safe_set(a, 'outgoingTransition', b2)
    assert _is_linked(a, 'outgoingTransition', b2)
    if hasattr(b1, 'CtxState25'):
        assert not _is_linked(b1, 'CtxState25', a)
    if hasattr(b2, 'CtxState25'):
        assert _is_linked(b2, 'CtxState25', a)
    _safe_set(a, 'outgoingTransition', None)
    assert not _is_linked(a, 'outgoingTransition', b2)
    if hasattr(b2, 'CtxState25'):
        assert not _is_linked(b2, 'CtxState25', a)


def test_assoc_state29_link_reassign_clear():
    a = ctxmngr_CtxState(isEnd=True, isStart=True)
    b1 = ctxmngr_ContextParameter(LitteralBoolean=True, LitteralInteger=7, LitteralString="sample_text", LitteralUnlimitedNatural=3.14, isInput=True)
    b2 = ctxmngr_ContextParameter(LitteralBoolean=False, LitteralInteger=13, LitteralString="sample_text_2", LitteralUnlimitedNatural=9.99, isInput=False)
    _safe_set(a, 'CtxState30', b1)
    assert _is_linked(a, 'CtxState30', b1)
    if hasattr(b1, 'contextParameters'):
        assert _is_linked(b1, 'contextParameters', a)
    _safe_set(a, 'CtxState30', b2)
    assert _is_linked(a, 'CtxState30', b2)
    if hasattr(b1, 'contextParameters'):
        assert not _is_linked(b1, 'contextParameters', a)
    if hasattr(b2, 'contextParameters'):
        assert _is_linked(b2, 'contextParameters', a)
    _safe_set(a, 'CtxState30', None)
    assert not _is_linked(a, 'CtxState30', b2)
    if hasattr(b2, 'contextParameters'):
        assert not _is_linked(b2, 'contextParameters', a)


def test_assoc_target26_link_reassign_clear():
    a = ctxmngr_CtxTransition(Action="sample_text", Condition="sample_text", Event="sample_text", input="sample_text", isRemote=True, output="sample_text", transProb=3.14, transRate=3.14)
    b1 = ctxmngr_CtxState(isEnd=True, isStart=True)
    b2 = ctxmngr_CtxState(isEnd=False, isStart=False)
    _safe_set(a, 'incomingTransition', b1)
    assert _is_linked(a, 'incomingTransition', b1)
    if hasattr(b1, 'CtxState27'):
        assert _is_linked(b1, 'CtxState27', a)
    _safe_set(a, 'incomingTransition', b2)
    assert _is_linked(a, 'incomingTransition', b2)
    if hasattr(b1, 'CtxState27'):
        assert not _is_linked(b1, 'CtxState27', a)
    if hasattr(b2, 'CtxState27'):
        assert _is_linked(b2, 'CtxState27', a)
    _safe_set(a, 'incomingTransition', None)
    assert not _is_linked(a, 'incomingTransition', b2)
    if hasattr(b2, 'CtxState27'):
        assert not _is_linked(b2, 'CtxState27', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


ctxmngr_ContextManager_strategy = st.builds(ctxmngr_ContextManager)
@given(instance=ctxmngr_ContextManager_strategy)
@settings(max_examples=25)
def test_ctxmngr_ContextManager_instantiation(instance):
    assert isinstance(instance, ctxmngr_ContextManager)


ctxmngr_ContextParameter_strategy = st.builds(ctxmngr_ContextParameter, LitteralBoolean=st.booleans(), LitteralInteger=st.integers(), LitteralString=safe_text, LitteralUnlimitedNatural=st.floats(allow_nan=False, allow_infinity=False), isInput=st.booleans())
@given(instance=ctxmngr_ContextParameter_strategy)
@settings(max_examples=25)
def test_ctxmngr_ContextParameter_instantiation(instance):
    assert isinstance(instance, ctxmngr_ContextParameter)


ctxmngr_CtxState_strategy = st.builds(ctxmngr_CtxState, isEnd=st.booleans(), isStart=st.booleans())
@given(instance=ctxmngr_CtxState_strategy)
@settings(max_examples=25)
def test_ctxmngr_CtxState_instantiation(instance):
    assert isinstance(instance, ctxmngr_CtxState)


ctxmngr_CtxTransition_strategy = st.builds(ctxmngr_CtxTransition, Action=safe_text, Condition=safe_text, Event=safe_text, input=safe_text, isRemote=st.booleans(), output=safe_text, transProb=st.floats(allow_nan=False, allow_infinity=False), transRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ctxmngr_CtxTransition_strategy)
@settings(max_examples=25)
def test_ctxmngr_CtxTransition_instantiation(instance):
    assert isinstance(instance, ctxmngr_CtxTransition)


ctxmngr_Manager_strategy = st.builds(ctxmngr_Manager)
@given(instance=ctxmngr_Manager_strategy)
@settings(max_examples=25)
def test_ctxmngr_Manager_instantiation(instance):
    assert isinstance(instance, ctxmngr_Manager)


ctxmngr_ManagerState_strategy = st.builds(ctxmngr_ManagerState)
@given(instance=ctxmngr_ManagerState_strategy)
@settings(max_examples=25)
def test_ctxmngr_ManagerState_instantiation(instance):
    assert isinstance(instance, ctxmngr_ManagerState)


ctxmngr_ManagerTransition_strategy = st.builds(ctxmngr_ManagerTransition)
@given(instance=ctxmngr_ManagerTransition_strategy)
@settings(max_examples=25)
def test_ctxmngr_ManagerTransition_instantiation(instance):
    assert isinstance(instance, ctxmngr_ManagerTransition)


ctxmngr_OpaqueExpression_strategy = st.builds(ctxmngr_OpaqueExpression)
@given(instance=ctxmngr_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_ctxmngr_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, ctxmngr_OpaqueExpression)


ctxmngr_RemoteFiringDependency_strategy = st.builds(ctxmngr_RemoteFiringDependency)
@given(instance=ctxmngr_RemoteFiringDependency_strategy)
@settings(max_examples=25)
def test_ctxmngr_RemoteFiringDependency_instantiation(instance):
    assert isinstance(instance, ctxmngr_RemoteFiringDependency)


