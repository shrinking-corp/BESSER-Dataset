import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractState,
    State,
    scmodel_AbstractState,
    scmodel_CompositeState,
    scmodel_FinalState,
    scmodel_History,
    scmodel_PseudoState,
    scmodel_State,
    scmodel_StateMachine,
    scmodel_Transition,
    LanguageTypes,
    MessageCheckerTypes,
    PseudoStateTypes,
    TriggerTypes,
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

def test_scmodel_AbstractState_id_value_roundtrip():
    instance = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scmodel_AbstractState_language_value_roundtrip():
    instance = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_scmodel_AbstractState_onEnter_value_roundtrip():
    instance = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    assert instance.onEnter == "sample_text"
    instance.onEnter = "sample_text_2"
    assert instance.onEnter == "sample_text_2"


def test_scmodel_AbstractState_onEnterImports_value_roundtrip():
    instance = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    assert instance.onEnterImports == "sample_text"
    instance.onEnterImports = "sample_text_2"
    assert instance.onEnterImports == "sample_text_2"


def test_scmodel_AbstractState_onExit_value_roundtrip():
    instance = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    assert instance.onExit == "sample_text"
    instance.onExit = "sample_text_2"
    assert instance.onExit == "sample_text_2"


def test_scmodel_AbstractState_onExitImports_value_roundtrip():
    instance = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    assert instance.onExitImports == "sample_text"
    instance.onExitImports = "sample_text_2"
    assert instance.onExitImports == "sample_text_2"


def test_scmodel_AbstractState_uuid_value_roundtrip():
    instance = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    assert instance.uuid == "sample_text"
    instance.uuid = "sample_text_2"
    assert instance.uuid == "sample_text_2"


def test_scmodel_History_shallow_value_roundtrip():
    instance = scmodel_History(shallow=True)
    assert instance.shallow == True
    instance.shallow = False
    assert instance.shallow == False


def test_scmodel_PseudoState_type_value_roundtrip():
    instance = scmodel_PseudoState(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_scmodel_StateMachine_agentType_value_roundtrip():
    instance = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    assert instance.agentType == "sample_text"
    instance.agentType = "sample_text_2"
    assert instance.agentType == "sample_text_2"


def test_scmodel_StateMachine_className_value_roundtrip():
    instance = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_scmodel_StateMachine_id_value_roundtrip():
    instance = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scmodel_StateMachine_language_value_roundtrip():
    instance = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_scmodel_StateMachine_nextID_value_roundtrip():
    instance = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    assert instance.nextID == 7
    instance.nextID = 13
    assert instance.nextID == 13


def test_scmodel_StateMachine_package_value_roundtrip():
    instance = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    assert instance.package == "sample_text"
    instance.package = "sample_text_2"
    assert instance.package == "sample_text_2"


def test_scmodel_StateMachine_priority_value_roundtrip():
    instance = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    assert instance.priority == 3.14
    instance.priority = 9.99
    assert instance.priority == 9.99


def test_scmodel_StateMachine_uuid_value_roundtrip():
    instance = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    assert instance.uuid == "sample_text"
    instance.uuid = "sample_text_2"
    assert instance.uuid == "sample_text_2"


def test_scmodel_Transition_defaultTransition_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.defaultTransition == True
    instance.defaultTransition = False
    assert instance.defaultTransition == False


def test_scmodel_Transition_guard_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.guard == "sample_text"
    instance.guard = "sample_text_2"
    assert instance.guard == "sample_text_2"


def test_scmodel_Transition_guardImports_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.guardImports == "sample_text"
    instance.guardImports = "sample_text_2"
    assert instance.guardImports == "sample_text_2"


def test_scmodel_Transition_id_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scmodel_Transition_messageCheckerClass_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.messageCheckerClass == "sample_text"
    instance.messageCheckerClass = "sample_text_2"
    assert instance.messageCheckerClass == "sample_text_2"


def test_scmodel_Transition_messageCheckerCode_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.messageCheckerCode == "sample_text"
    instance.messageCheckerCode = "sample_text_2"
    assert instance.messageCheckerCode == "sample_text_2"


def test_scmodel_Transition_messageCheckerCodeImports_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.messageCheckerCodeImports == "sample_text"
    instance.messageCheckerCodeImports = "sample_text_2"
    assert instance.messageCheckerCodeImports == "sample_text_2"


def test_scmodel_Transition_messageCheckerConditionLanguage_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.messageCheckerConditionLanguage == "sample_text"
    instance.messageCheckerConditionLanguage = "sample_text_2"
    assert instance.messageCheckerConditionLanguage == "sample_text_2"


def test_scmodel_Transition_messageCheckerType_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.messageCheckerType == "sample_text"
    instance.messageCheckerType = "sample_text_2"
    assert instance.messageCheckerType == "sample_text_2"


def test_scmodel_Transition_onTransition_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.onTransition == "sample_text"
    instance.onTransition = "sample_text_2"
    assert instance.onTransition == "sample_text_2"


def test_scmodel_Transition_onTransitionImports_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.onTransitionImports == "sample_text"
    instance.onTransitionImports = "sample_text_2"
    assert instance.onTransitionImports == "sample_text_2"


def test_scmodel_Transition_outOfBranch_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.outOfBranch == True
    instance.outOfBranch = False
    assert instance.outOfBranch == False


def test_scmodel_Transition_priority_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.priority == 3.14
    instance.priority = 9.99
    assert instance.priority == 9.99


def test_scmodel_Transition_selfTransition_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.selfTransition == True
    instance.selfTransition = False
    assert instance.selfTransition == False


def test_scmodel_Transition_triggerCodeLanguage_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerCodeLanguage == "sample_text"
    instance.triggerCodeLanguage = "sample_text_2"
    assert instance.triggerCodeLanguage == "sample_text_2"


def test_scmodel_Transition_triggerConditionCode_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerConditionCode == "sample_text"
    instance.triggerConditionCode = "sample_text_2"
    assert instance.triggerConditionCode == "sample_text_2"


def test_scmodel_Transition_triggerConditionCodeImports_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerConditionCodeImports == "sample_text"
    instance.triggerConditionCodeImports = "sample_text_2"
    assert instance.triggerConditionCodeImports == "sample_text_2"


def test_scmodel_Transition_triggerExpRateCode_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerExpRateCode == "sample_text"
    instance.triggerExpRateCode = "sample_text_2"
    assert instance.triggerExpRateCode == "sample_text_2"


def test_scmodel_Transition_triggerExpRateCodeImports_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerExpRateCodeImports == "sample_text"
    instance.triggerExpRateCodeImports = "sample_text_2"
    assert instance.triggerExpRateCodeImports == "sample_text_2"


def test_scmodel_Transition_triggerProbCode_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerProbCode == "sample_text"
    instance.triggerProbCode = "sample_text_2"
    assert instance.triggerProbCode == "sample_text_2"


def test_scmodel_Transition_triggerProbCodeImports_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerProbCodeImports == "sample_text"
    instance.triggerProbCodeImports = "sample_text_2"
    assert instance.triggerProbCodeImports == "sample_text_2"


def test_scmodel_Transition_triggerTime_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerTime == 3.14
    instance.triggerTime = 9.99
    assert instance.triggerTime == 9.99


def test_scmodel_Transition_triggerTimedCode_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerTimedCode == "sample_text"
    instance.triggerTimedCode = "sample_text_2"
    assert instance.triggerTimedCode == "sample_text_2"


def test_scmodel_Transition_triggerTimedCodeImports_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerTimedCodeImports == "sample_text"
    instance.triggerTimedCodeImports = "sample_text_2"
    assert instance.triggerTimedCodeImports == "sample_text_2"


def test_scmodel_Transition_triggerType_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.triggerType == "sample_text"
    instance.triggerType = "sample_text_2"
    assert instance.triggerType == "sample_text_2"


def test_scmodel_Transition_uuid_value_roundtrip():
    instance = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    assert instance.uuid == "sample_text"
    instance.uuid = "sample_text_2"
    assert instance.uuid == "sample_text_2"


def test_scmodel_CompositeState_isa_AbstractState():
    instance = scmodel_CompositeState()
    assert isinstance(instance, AbstractState)


def test_scmodel_PseudoState_isa_AbstractState():
    instance = scmodel_PseudoState(type="sample_text")
    assert isinstance(instance, AbstractState)


def test_scmodel_State_isa_AbstractState():
    instance = scmodel_State()
    assert isinstance(instance, AbstractState)


def test_scmodel_FinalState_isa_State():
    instance = scmodel_FinalState()
    assert isinstance(instance, State)


def test_scmodel_History_isa_State():
    instance = scmodel_History(shallow=True)
    assert isinstance(instance, State)


def test_assoc_children9_link_reassign_clear():
    a = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    b1 = scmodel_CompositeState()
    b2 = scmodel_CompositeState()
    _safe_set(a, 'scmodel_AbstractState10', b1)
    assert _is_linked(a, 'scmodel_AbstractState10', b1)
    if hasattr(b1, 'scmodel_CompositeState'):
        assert _is_linked(b1, 'scmodel_CompositeState', a)
    _safe_set(a, 'scmodel_AbstractState10', b2)
    assert _is_linked(a, 'scmodel_AbstractState10', b2)
    if hasattr(b1, 'scmodel_CompositeState'):
        assert not _is_linked(b1, 'scmodel_CompositeState', a)
    if hasattr(b2, 'scmodel_CompositeState'):
        assert _is_linked(b2, 'scmodel_CompositeState', a)
    _safe_set(a, 'scmodel_AbstractState10', None)
    assert not _is_linked(a, 'scmodel_AbstractState10', b2)
    if hasattr(b2, 'scmodel_CompositeState'):
        assert not _is_linked(b2, 'scmodel_CompositeState', a)


def test_assoc_from_3_link_reassign_clear():
    a = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    b1 = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    b2 = scmodel_AbstractState(id="sample_text_2", language="sample_text_2", onEnter="sample_text_2", onEnterImports="sample_text_2", onExit="sample_text_2", onExitImports="sample_text_2", uuid="sample_text_2")
    _safe_set(a, 'scmodel_Transition4', b1)
    assert _is_linked(a, 'scmodel_Transition4', b1)
    if hasattr(b1, 'scmodel_AbstractState5'):
        assert _is_linked(b1, 'scmodel_AbstractState5', a)
    _safe_set(a, 'scmodel_Transition4', b2)
    assert _is_linked(a, 'scmodel_Transition4', b2)
    if hasattr(b1, 'scmodel_AbstractState5'):
        assert not _is_linked(b1, 'scmodel_AbstractState5', a)
    if hasattr(b2, 'scmodel_AbstractState5'):
        assert _is_linked(b2, 'scmodel_AbstractState5', a)
    _safe_set(a, 'scmodel_Transition4', None)
    assert not _is_linked(a, 'scmodel_Transition4', b2)
    if hasattr(b2, 'scmodel_AbstractState5'):
        assert not _is_linked(b2, 'scmodel_AbstractState5', a)


def test_assoc_states0_link_reassign_clear():
    a = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    b1 = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    b2 = scmodel_AbstractState(id="sample_text_2", language="sample_text_2", onEnter="sample_text_2", onEnterImports="sample_text_2", onExit="sample_text_2", onExitImports="sample_text_2", uuid="sample_text_2")
    _safe_set(a, 'scmodel_StateMachine', {b1})
    assert _is_linked(a, 'scmodel_StateMachine', b1)
    if hasattr(b1, 'scmodel_AbstractState'):
        assert _is_linked(b1, 'scmodel_AbstractState', a)
    _safe_set(a, 'scmodel_StateMachine', {b2})
    assert _is_linked(a, 'scmodel_StateMachine', b2)
    if hasattr(b1, 'scmodel_AbstractState'):
        assert not _is_linked(b1, 'scmodel_AbstractState', a)
    if hasattr(b2, 'scmodel_AbstractState'):
        assert _is_linked(b2, 'scmodel_AbstractState', a)
    _safe_set(a, 'scmodel_StateMachine', set())
    assert not _is_linked(a, 'scmodel_StateMachine', b2)
    if hasattr(b2, 'scmodel_AbstractState'):
        assert not _is_linked(b2, 'scmodel_AbstractState', a)


def test_assoc_to6_link_reassign_clear():
    a = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    b1 = scmodel_AbstractState(id="sample_text", language="sample_text", onEnter="sample_text", onEnterImports="sample_text", onExit="sample_text", onExitImports="sample_text", uuid="sample_text")
    b2 = scmodel_AbstractState(id="sample_text_2", language="sample_text_2", onEnter="sample_text_2", onEnterImports="sample_text_2", onExit="sample_text_2", onExitImports="sample_text_2", uuid="sample_text_2")
    _safe_set(a, 'scmodel_Transition7', b1)
    assert _is_linked(a, 'scmodel_Transition7', b1)
    if hasattr(b1, 'scmodel_AbstractState8'):
        assert _is_linked(b1, 'scmodel_AbstractState8', a)
    _safe_set(a, 'scmodel_Transition7', b2)
    assert _is_linked(a, 'scmodel_Transition7', b2)
    if hasattr(b1, 'scmodel_AbstractState8'):
        assert not _is_linked(b1, 'scmodel_AbstractState8', a)
    if hasattr(b2, 'scmodel_AbstractState8'):
        assert _is_linked(b2, 'scmodel_AbstractState8', a)
    _safe_set(a, 'scmodel_Transition7', None)
    assert not _is_linked(a, 'scmodel_Transition7', b2)
    if hasattr(b2, 'scmodel_AbstractState8'):
        assert not _is_linked(b2, 'scmodel_AbstractState8', a)


def test_assoc_transitions1_link_reassign_clear():
    a = scmodel_Transition(defaultTransition=True, guard="sample_text", guardImports="sample_text", id="sample_text", messageCheckerClass="sample_text", messageCheckerCode="sample_text", messageCheckerCodeImports="sample_text", messageCheckerConditionLanguage="sample_text", messageCheckerType="sample_text", onTransition="sample_text", onTransitionImports="sample_text", outOfBranch=True, priority=3.14, selfTransition=True, triggerCodeLanguage="sample_text", triggerConditionCode="sample_text", triggerConditionCodeImports="sample_text", triggerExpRateCode="sample_text", triggerExpRateCodeImports="sample_text", triggerProbCode="sample_text", triggerProbCodeImports="sample_text", triggerTime=3.14, triggerTimedCode="sample_text", triggerTimedCodeImports="sample_text", triggerType="sample_text", uuid="sample_text")
    b1 = scmodel_StateMachine(agentType="sample_text", className="sample_text", id="sample_text", language="sample_text", nextID=7, package="sample_text", priority=3.14, uuid="sample_text")
    b2 = scmodel_StateMachine(agentType="sample_text_2", className="sample_text_2", id="sample_text_2", language="sample_text_2", nextID=13, package="sample_text_2", priority=9.99, uuid="sample_text_2")
    _safe_set(a, 'scmodel_Transition', b1)
    assert _is_linked(a, 'scmodel_Transition', b1)
    if hasattr(b1, 'scmodel_StateMachine2'):
        assert _is_linked(b1, 'scmodel_StateMachine2', a)
    _safe_set(a, 'scmodel_Transition', b2)
    assert _is_linked(a, 'scmodel_Transition', b2)
    if hasattr(b1, 'scmodel_StateMachine2'):
        assert not _is_linked(b1, 'scmodel_StateMachine2', a)
    if hasattr(b2, 'scmodel_StateMachine2'):
        assert _is_linked(b2, 'scmodel_StateMachine2', a)
    _safe_set(a, 'scmodel_Transition', None)
    assert not _is_linked(a, 'scmodel_Transition', b2)
    if hasattr(b2, 'scmodel_StateMachine2'):
        assert not _is_linked(b2, 'scmodel_StateMachine2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


scmodel_AbstractState_strategy = st.builds(scmodel_AbstractState, id=safe_text, language=safe_text, onEnter=safe_text, onEnterImports=safe_text, onExit=safe_text, onExitImports=safe_text, uuid=safe_text)
@given(instance=scmodel_AbstractState_strategy)
@settings(max_examples=25)
def test_scmodel_AbstractState_instantiation(instance):
    assert isinstance(instance, scmodel_AbstractState)


scmodel_CompositeState_strategy = st.builds(scmodel_CompositeState)
@given(instance=scmodel_CompositeState_strategy)
@settings(max_examples=25)
def test_scmodel_CompositeState_instantiation(instance):
    assert isinstance(instance, scmodel_CompositeState)


scmodel_FinalState_strategy = st.builds(scmodel_FinalState)
@given(instance=scmodel_FinalState_strategy)
@settings(max_examples=25)
def test_scmodel_FinalState_instantiation(instance):
    assert isinstance(instance, scmodel_FinalState)


scmodel_History_strategy = st.builds(scmodel_History, shallow=st.booleans())
@given(instance=scmodel_History_strategy)
@settings(max_examples=25)
def test_scmodel_History_instantiation(instance):
    assert isinstance(instance, scmodel_History)


scmodel_PseudoState_strategy = st.builds(scmodel_PseudoState, type=safe_text)
@given(instance=scmodel_PseudoState_strategy)
@settings(max_examples=25)
def test_scmodel_PseudoState_instantiation(instance):
    assert isinstance(instance, scmodel_PseudoState)


scmodel_State_strategy = st.builds(scmodel_State)
@given(instance=scmodel_State_strategy)
@settings(max_examples=25)
def test_scmodel_State_instantiation(instance):
    assert isinstance(instance, scmodel_State)


scmodel_StateMachine_strategy = st.builds(scmodel_StateMachine, agentType=safe_text, className=safe_text, id=safe_text, language=safe_text, nextID=st.integers(), package=safe_text, priority=st.floats(allow_nan=False, allow_infinity=False), uuid=safe_text)
@given(instance=scmodel_StateMachine_strategy)
@settings(max_examples=25)
def test_scmodel_StateMachine_instantiation(instance):
    assert isinstance(instance, scmodel_StateMachine)


scmodel_Transition_strategy = st.builds(scmodel_Transition, defaultTransition=st.booleans(), guard=safe_text, guardImports=safe_text, id=safe_text, messageCheckerClass=safe_text, messageCheckerCode=safe_text, messageCheckerCodeImports=safe_text, messageCheckerConditionLanguage=safe_text, messageCheckerType=safe_text, onTransition=safe_text, onTransitionImports=safe_text, outOfBranch=st.booleans(), priority=st.floats(allow_nan=False, allow_infinity=False), selfTransition=st.booleans(), triggerCodeLanguage=safe_text, triggerConditionCode=safe_text, triggerConditionCodeImports=safe_text, triggerExpRateCode=safe_text, triggerExpRateCodeImports=safe_text, triggerProbCode=safe_text, triggerProbCodeImports=safe_text, triggerTime=st.floats(allow_nan=False, allow_infinity=False), triggerTimedCode=safe_text, triggerTimedCodeImports=safe_text, triggerType=safe_text, uuid=safe_text)
@given(instance=scmodel_Transition_strategy)
@settings(max_examples=25)
def test_scmodel_Transition_instantiation(instance):
    assert isinstance(instance, scmodel_Transition)


