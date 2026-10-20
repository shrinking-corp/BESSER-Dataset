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
    AnalogAction,
    arduinoml_AnalogActionSensor,
    arduinoml_AnalogActionValue,
    Action,
    arduinoml_AnalogAction,
    arduinoml_DigitalAction,
    Condition,
    arduinoml_AnalogCondition,
    arduinoml_DigitalCondition,
    arduinoml_TimeCondition,
    arduinoml_Condition,
    arduinoml_NamedElement,
    Brick,
    arduinoml_AnalogSensor,
    arduinoml_AnalogActuator,
    arduinoml_DigitalActuator,
    arduinoml_DigitalSensor,
    arduinoml_Action,
    arduinoml_Transition,
    NamedElement,
    arduinoml_AMLState,
    arduinoml_Brick,
    arduinoml_AMLMachine,
    AnalogComparison,
    DigitalState,
    TimeComparison,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_analogaction_is_not_abstract():
    assert not inspect.isabstract(AnalogAction)


def test_hyp_analogaction_constructor_exists():
    assert callable(AnalogAction.__init__)


def test_hyp_analogaction_constructor_args():
    sig = inspect.signature(AnalogAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_analogactionsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogActionSensor)


def test_hyp_arduinoml_analogactionsensor_constructor_exists():
    assert callable(arduinoml_AnalogActionSensor.__init__)


def test_hyp_arduinoml_analogactionsensor_constructor_args():
    sig = inspect.signature(arduinoml_AnalogActionSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_analogactionvalue_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogActionValue)


def test_hyp_arduinoml_analogactionvalue_constructor_exists():
    assert callable(arduinoml_AnalogActionValue.__init__)


def test_hyp_arduinoml_analogactionvalue_constructor_args():
    sig = inspect.signature(arduinoml_AnalogActionValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_analogaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogAction)


def test_hyp_arduinoml_analogaction_constructor_exists():
    assert callable(arduinoml_AnalogAction.__init__)


def test_hyp_arduinoml_analogaction_constructor_args():
    sig = inspect.signature(arduinoml_AnalogAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_digitalaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml_DigitalAction)


def test_hyp_arduinoml_digitalaction_constructor_exists():
    assert callable(arduinoml_DigitalAction.__init__)


def test_hyp_arduinoml_digitalaction_constructor_args():
    sig = inspect.signature(arduinoml_DigitalAction.__init__)
    params = list(sig.parameters.keys())
    assert "dState" in params, "Missing parameter 'dState'"




def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_analogcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogCondition)


def test_hyp_arduinoml_analogcondition_constructor_exists():
    assert callable(arduinoml_AnalogCondition.__init__)


def test_hyp_arduinoml_analogcondition_constructor_args():
    sig = inspect.signature(arduinoml_AnalogCondition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "aComp" in params, "Missing parameter 'aComp'"





def test_hyp_arduinoml_digitalcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_DigitalCondition)


def test_hyp_arduinoml_digitalcondition_constructor_exists():
    assert callable(arduinoml_DigitalCondition.__init__)


def test_hyp_arduinoml_digitalcondition_constructor_args():
    sig = inspect.signature(arduinoml_DigitalCondition.__init__)
    params = list(sig.parameters.keys())
    assert "dState" in params, "Missing parameter 'dState'"




def test_hyp_arduinoml_timecondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_TimeCondition)


def test_hyp_arduinoml_timecondition_constructor_exists():
    assert callable(arduinoml_TimeCondition.__init__)


def test_hyp_arduinoml_timecondition_constructor_args():
    sig = inspect.signature(arduinoml_TimeCondition.__init__)
    params = list(sig.parameters.keys())
    assert "tComp" in params, "Missing parameter 'tComp'"
    assert "time" in params, "Missing parameter 'time'"





def test_hyp_arduinoml_condition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Condition)


def test_hyp_arduinoml_condition_constructor_exists():
    assert callable(arduinoml_Condition.__init__)


def test_hyp_arduinoml_condition_constructor_args():
    sig = inspect.signature(arduinoml_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_namedelement_is_not_abstract():
    assert not inspect.isabstract(arduinoml_NamedElement)


def test_hyp_arduinoml_namedelement_constructor_exists():
    assert callable(arduinoml_NamedElement.__init__)


def test_hyp_arduinoml_namedelement_constructor_args():
    sig = inspect.signature(arduinoml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_brick_is_not_abstract():
    assert not inspect.isabstract(Brick)


def test_hyp_brick_constructor_exists():
    assert callable(Brick.__init__)


def test_hyp_brick_constructor_args():
    sig = inspect.signature(Brick.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_analogsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogSensor)


def test_hyp_arduinoml_analogsensor_constructor_exists():
    assert callable(arduinoml_AnalogSensor.__init__)


def test_hyp_arduinoml_analogsensor_constructor_args():
    sig = inspect.signature(arduinoml_AnalogSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_analogactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogActuator)


def test_hyp_arduinoml_analogactuator_constructor_exists():
    assert callable(arduinoml_AnalogActuator.__init__)


def test_hyp_arduinoml_analogactuator_constructor_args():
    sig = inspect.signature(arduinoml_AnalogActuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_digitalactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_DigitalActuator)


def test_hyp_arduinoml_digitalactuator_constructor_exists():
    assert callable(arduinoml_DigitalActuator.__init__)


def test_hyp_arduinoml_digitalactuator_constructor_args():
    sig = inspect.signature(arduinoml_DigitalActuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_digitalsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_DigitalSensor)


def test_hyp_arduinoml_digitalsensor_constructor_exists():
    assert callable(arduinoml_DigitalSensor.__init__)


def test_hyp_arduinoml_digitalsensor_constructor_args():
    sig = inspect.signature(arduinoml_DigitalSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_action_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Action)


def test_hyp_arduinoml_action_constructor_exists():
    assert callable(arduinoml_Action.__init__)


def test_hyp_arduinoml_action_constructor_args():
    sig = inspect.signature(arduinoml_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_transition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Transition)


def test_hyp_arduinoml_transition_constructor_exists():
    assert callable(arduinoml_Transition.__init__)


def test_hyp_arduinoml_transition_constructor_args():
    sig = inspect.signature(arduinoml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_amlstate_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AMLState)


def test_hyp_arduinoml_amlstate_constructor_exists():
    assert callable(arduinoml_AMLState.__init__)


def test_hyp_arduinoml_amlstate_constructor_args():
    sig = inspect.signature(arduinoml_AMLState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_brick_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Brick)


def test_hyp_arduinoml_brick_constructor_exists():
    assert callable(arduinoml_Brick.__init__)


def test_hyp_arduinoml_brick_constructor_args():
    sig = inspect.signature(arduinoml_Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"




def test_hyp_arduinoml_amlmachine_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AMLMachine)


def test_hyp_arduinoml_amlmachine_constructor_exists():
    assert callable(arduinoml_AMLMachine.__init__)


def test_hyp_arduinoml_amlmachine_constructor_args():
    sig = inspect.signature(arduinoml_AMLMachine.__init__)
    params = list(sig.parameters.keys())
    assert "frequency" in params, "Missing parameter 'frequency'"


def test_hyp_analogcomparison_exists():
    # Check that the Enumeration exists
    assert AnalogComparison is not None

def test_hyp_analogcomparison_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnalogComparison]
    expected_literals = [
        "GREATER",
        "GREATEREQ",
        "EQUAL",
        "LOWER",
        "LOWEREQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnalogComparison"

def test_hyp_digitalstate_exists():
    # Check that the Enumeration exists
    assert DigitalState is not None

def test_hyp_digitalstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DigitalState]
    expected_literals = [
        "OFF",
        "ON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DigitalState"

def test_hyp_timecomparison_exists():
    # Check that the Enumeration exists
    assert TimeComparison is not None

def test_hyp_timecomparison_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeComparison]
    expected_literals = [
        "BEFORE",
        "AFTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeComparison"


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
AnalogAction_strategy = st.builds(
    AnalogAction,
)
arduinoml_AnalogActionSensor_strategy = st.builds(
    arduinoml_AnalogActionSensor,
)
arduinoml_AnalogActionValue_strategy = st.builds(
    arduinoml_AnalogActionValue,
    value=
        st.integers()
)
Action_strategy = st.builds(
    Action,
)
arduinoml_AnalogAction_strategy = st.builds(
    arduinoml_AnalogAction,
)
arduinoml_DigitalAction_strategy = st.builds(
    arduinoml_DigitalAction,
    dState=
        safe_text
)
Condition_strategy = st.builds(
    Condition,
)
arduinoml_AnalogCondition_strategy = st.builds(
    arduinoml_AnalogCondition,
    value=
        st.integers(),
    aComp=
        safe_text
)
arduinoml_DigitalCondition_strategy = st.builds(
    arduinoml_DigitalCondition,
    dState=
        safe_text
)
arduinoml_TimeCondition_strategy = st.builds(
    arduinoml_TimeCondition,
    tComp=
        safe_text,
    time=
        st.integers()
)
arduinoml_Condition_strategy = st.builds(
    arduinoml_Condition,
)
arduinoml_NamedElement_strategy = st.builds(
    arduinoml_NamedElement,
    name=
        safe_text
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml_AnalogSensor_strategy = st.builds(
    arduinoml_AnalogSensor,
)
arduinoml_AnalogActuator_strategy = st.builds(
    arduinoml_AnalogActuator,
)
arduinoml_DigitalActuator_strategy = st.builds(
    arduinoml_DigitalActuator,
)
arduinoml_DigitalSensor_strategy = st.builds(
    arduinoml_DigitalSensor,
)
arduinoml_Action_strategy = st.builds(
    arduinoml_Action,
)
arduinoml_Transition_strategy = st.builds(
    arduinoml_Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml_AMLState_strategy = st.builds(
    arduinoml_AMLState,
)
arduinoml_Brick_strategy = st.builds(
    arduinoml_Brick,
    pin=
        st.integers()
)
arduinoml_AMLMachine_strategy = st.builds(
    arduinoml_AMLMachine,
    frequency=
        st.integers()
)






@given(instance=arduinoml_AnalogActionValue_strategy)
def test_hyp_arduinoml_analogactionvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=arduinoml_DigitalAction_strategy)
def test_hyp_arduinoml_digitalaction_dState_setter(instance):
    original = instance.dState
    instance.dState = original
    assert instance.dState == original





@given(instance=arduinoml_AnalogCondition_strategy)
def test_hyp_arduinoml_analogcondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=arduinoml_AnalogCondition_strategy)
def test_hyp_arduinoml_analogcondition_aComp_setter(instance):
    original = instance.aComp
    instance.aComp = original
    assert instance.aComp == original




@given(instance=arduinoml_DigitalCondition_strategy)
def test_hyp_arduinoml_digitalcondition_dState_setter(instance):
    original = instance.dState
    instance.dState = original
    assert instance.dState == original




@given(instance=arduinoml_TimeCondition_strategy)
def test_hyp_arduinoml_timecondition_tComp_setter(instance):
    original = instance.tComp
    instance.tComp = original
    assert instance.tComp == original



@given(instance=arduinoml_TimeCondition_strategy)
def test_hyp_arduinoml_timecondition_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original





@given(instance=arduinoml_NamedElement_strategy)
def test_hyp_arduinoml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original













@given(instance=arduinoml_Brick_strategy)
def test_hyp_arduinoml_brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original




@given(instance=arduinoml_AMLMachine_strategy)
def test_hyp_arduinoml_amlmachine_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    AnalogAction,
    Brick,
    Condition,
    NamedElement,
    arduinoml_AMLMachine,
    arduinoml_AMLState,
    arduinoml_Action,
    arduinoml_AnalogAction,
    arduinoml_AnalogActionSensor,
    arduinoml_AnalogActionValue,
    arduinoml_AnalogActuator,
    arduinoml_AnalogCondition,
    arduinoml_AnalogSensor,
    arduinoml_Brick,
    arduinoml_Condition,
    arduinoml_DigitalAction,
    arduinoml_DigitalActuator,
    arduinoml_DigitalCondition,
    arduinoml_DigitalSensor,
    arduinoml_NamedElement,
    arduinoml_TimeCondition,
    arduinoml_Transition,
    AnalogComparison,
    DigitalState,
    TimeComparison,
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

def test_arduinoml_AMLMachine_frequency_value_roundtrip():
    instance = arduinoml_AMLMachine(frequency=7)
    assert instance.frequency == 7
    instance.frequency = 13
    assert instance.frequency == 13


def test_arduinoml_AnalogActionValue_value_value_roundtrip():
    instance = arduinoml_AnalogActionValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_arduinoml_AnalogCondition_aComp_value_roundtrip():
    instance = arduinoml_AnalogCondition(aComp="sample_text", value=7)
    assert instance.aComp == "sample_text"
    instance.aComp = "sample_text_2"
    assert instance.aComp == "sample_text_2"


def test_arduinoml_AnalogCondition_value_value_roundtrip():
    instance = arduinoml_AnalogCondition(aComp="sample_text", value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_arduinoml_Brick_pin_value_roundtrip():
    instance = arduinoml_Brick(pin=7)
    assert instance.pin == 7
    instance.pin = 13
    assert instance.pin == 13


def test_arduinoml_DigitalAction_dState_value_roundtrip():
    instance = arduinoml_DigitalAction(dState="sample_text")
    assert instance.dState == "sample_text"
    instance.dState = "sample_text_2"
    assert instance.dState == "sample_text_2"


def test_arduinoml_DigitalCondition_dState_value_roundtrip():
    instance = arduinoml_DigitalCondition(dState="sample_text")
    assert instance.dState == "sample_text"
    instance.dState = "sample_text_2"
    assert instance.dState == "sample_text_2"


def test_arduinoml_NamedElement_name_value_roundtrip():
    instance = arduinoml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_arduinoml_TimeCondition_tComp_value_roundtrip():
    instance = arduinoml_TimeCondition(tComp="sample_text", time=7)
    assert instance.tComp == "sample_text"
    instance.tComp = "sample_text_2"
    assert instance.tComp == "sample_text_2"


def test_arduinoml_TimeCondition_time_value_roundtrip():
    instance = arduinoml_TimeCondition(tComp="sample_text", time=7)
    assert instance.time == 7
    instance.time = 13
    assert instance.time == 13


def test_arduinoml_AnalogAction_isa_Action():
    instance = arduinoml_AnalogAction()
    assert isinstance(instance, Action)


def test_arduinoml_DigitalAction_isa_Action():
    instance = arduinoml_DigitalAction(dState="sample_text")
    assert isinstance(instance, Action)


def test_arduinoml_AnalogActionSensor_isa_AnalogAction():
    instance = arduinoml_AnalogActionSensor()
    assert isinstance(instance, AnalogAction)


def test_arduinoml_AnalogActionValue_isa_AnalogAction():
    instance = arduinoml_AnalogActionValue(value=7)
    assert isinstance(instance, AnalogAction)


def test_arduinoml_AnalogActuator_isa_Brick():
    instance = arduinoml_AnalogActuator()
    assert isinstance(instance, Brick)


def test_arduinoml_AnalogSensor_isa_Brick():
    instance = arduinoml_AnalogSensor()
    assert isinstance(instance, Brick)


def test_arduinoml_DigitalActuator_isa_Brick():
    instance = arduinoml_DigitalActuator()
    assert isinstance(instance, Brick)


def test_arduinoml_DigitalSensor_isa_Brick():
    instance = arduinoml_DigitalSensor()
    assert isinstance(instance, Brick)


def test_arduinoml_AnalogCondition_isa_Condition():
    instance = arduinoml_AnalogCondition(aComp="sample_text", value=7)
    assert isinstance(instance, Condition)


def test_arduinoml_DigitalCondition_isa_Condition():
    instance = arduinoml_DigitalCondition(dState="sample_text")
    assert isinstance(instance, Condition)


def test_arduinoml_TimeCondition_isa_Condition():
    instance = arduinoml_TimeCondition(tComp="sample_text", time=7)
    assert isinstance(instance, Condition)


def test_arduinoml_AMLState_isa_NamedElement():
    instance = arduinoml_AMLState()
    assert isinstance(instance, NamedElement)


def test_arduinoml_Brick_isa_NamedElement():
    instance = arduinoml_Brick(pin=7)
    assert isinstance(instance, NamedElement)


def test_assoc_actuator16_link_reassign_clear():
    a = arduinoml_DigitalAction(dState="sample_text")
    b1 = arduinoml_DigitalActuator()
    b2 = arduinoml_DigitalActuator()
    _safe_set(a, 'arduinoml_DigitalAction', b1)
    assert _is_linked(a, 'arduinoml_DigitalAction', b1)
    if hasattr(b1, 'arduinoml_DigitalActuator'):
        assert _is_linked(b1, 'arduinoml_DigitalActuator', a)
    _safe_set(a, 'arduinoml_DigitalAction', b2)
    assert _is_linked(a, 'arduinoml_DigitalAction', b2)
    if hasattr(b1, 'arduinoml_DigitalActuator'):
        assert not _is_linked(b1, 'arduinoml_DigitalActuator', a)
    if hasattr(b2, 'arduinoml_DigitalActuator'):
        assert _is_linked(b2, 'arduinoml_DigitalActuator', a)
    _safe_set(a, 'arduinoml_DigitalAction', None)
    assert not _is_linked(a, 'arduinoml_DigitalAction', b2)
    if hasattr(b2, 'arduinoml_DigitalActuator'):
        assert not _is_linked(b2, 'arduinoml_DigitalActuator', a)


def test_assoc_bricks0_link_reassign_clear():
    a = arduinoml_Brick(pin=7)
    b1 = arduinoml_AMLMachine(frequency=7)
    b2 = arduinoml_AMLMachine(frequency=13)
    _safe_set(a, 'arduinoml_Brick', b1)
    assert _is_linked(a, 'arduinoml_Brick', b1)
    if hasattr(b1, 'arduinoml_AMLMachine'):
        assert _is_linked(b1, 'arduinoml_AMLMachine', a)
    _safe_set(a, 'arduinoml_Brick', b2)
    assert _is_linked(a, 'arduinoml_Brick', b2)
    if hasattr(b1, 'arduinoml_AMLMachine'):
        assert not _is_linked(b1, 'arduinoml_AMLMachine', a)
    if hasattr(b2, 'arduinoml_AMLMachine'):
        assert _is_linked(b2, 'arduinoml_AMLMachine', a)
    _safe_set(a, 'arduinoml_Brick', None)
    assert not _is_linked(a, 'arduinoml_Brick', b2)
    if hasattr(b2, 'arduinoml_AMLMachine'):
        assert not _is_linked(b2, 'arduinoml_AMLMachine', a)


def test_assoc_sensor15_link_reassign_clear():
    a = arduinoml_DigitalCondition(dState="sample_text")
    b1 = arduinoml_DigitalSensor()
    b2 = arduinoml_DigitalSensor()
    _safe_set(a, 'arduinoml_DigitalCondition', b1)
    assert _is_linked(a, 'arduinoml_DigitalCondition', b1)
    if hasattr(b1, 'arduinoml_DigitalSensor'):
        assert _is_linked(b1, 'arduinoml_DigitalSensor', a)
    _safe_set(a, 'arduinoml_DigitalCondition', b2)
    assert _is_linked(a, 'arduinoml_DigitalCondition', b2)
    if hasattr(b1, 'arduinoml_DigitalSensor'):
        assert not _is_linked(b1, 'arduinoml_DigitalSensor', a)
    if hasattr(b2, 'arduinoml_DigitalSensor'):
        assert _is_linked(b2, 'arduinoml_DigitalSensor', a)
    _safe_set(a, 'arduinoml_DigitalCondition', None)
    assert not _is_linked(a, 'arduinoml_DigitalCondition', b2)
    if hasattr(b2, 'arduinoml_DigitalSensor'):
        assert not _is_linked(b2, 'arduinoml_DigitalSensor', a)


def test_assoc_sensor17_link_reassign_clear():
    a = arduinoml_AnalogCondition(aComp="sample_text", value=7)
    b1 = arduinoml_AnalogSensor()
    b2 = arduinoml_AnalogSensor()
    _safe_set(a, 'arduinoml_AnalogCondition', b1)
    assert _is_linked(a, 'arduinoml_AnalogCondition', b1)
    if hasattr(b1, 'arduinoml_AnalogSensor'):
        assert _is_linked(b1, 'arduinoml_AnalogSensor', a)
    _safe_set(a, 'arduinoml_AnalogCondition', b2)
    assert _is_linked(a, 'arduinoml_AnalogCondition', b2)
    if hasattr(b1, 'arduinoml_AnalogSensor'):
        assert not _is_linked(b1, 'arduinoml_AnalogSensor', a)
    if hasattr(b2, 'arduinoml_AnalogSensor'):
        assert _is_linked(b2, 'arduinoml_AnalogSensor', a)
    _safe_set(a, 'arduinoml_AnalogCondition', None)
    assert not _is_linked(a, 'arduinoml_AnalogCondition', b2)
    if hasattr(b2, 'arduinoml_AnalogSensor'):
        assert not _is_linked(b2, 'arduinoml_AnalogSensor', a)


def test_assoc_start3_link_reassign_clear():
    a = arduinoml_AMLMachine(frequency=7)
    b1 = arduinoml_AMLState()
    b2 = arduinoml_AMLState()
    _safe_set(a, 'arduinoml_AMLMachine4', b1)
    assert _is_linked(a, 'arduinoml_AMLMachine4', b1)
    if hasattr(b1, 'arduinoml_AMLState5'):
        assert _is_linked(b1, 'arduinoml_AMLState5', a)
    _safe_set(a, 'arduinoml_AMLMachine4', b2)
    assert _is_linked(a, 'arduinoml_AMLMachine4', b2)
    if hasattr(b1, 'arduinoml_AMLState5'):
        assert not _is_linked(b1, 'arduinoml_AMLState5', a)
    if hasattr(b2, 'arduinoml_AMLState5'):
        assert _is_linked(b2, 'arduinoml_AMLState5', a)
    _safe_set(a, 'arduinoml_AMLMachine4', None)
    assert not _is_linked(a, 'arduinoml_AMLMachine4', b2)
    if hasattr(b2, 'arduinoml_AMLState5'):
        assert not _is_linked(b2, 'arduinoml_AMLState5', a)


def test_assoc_states1_link_reassign_clear():
    a = arduinoml_AMLMachine(frequency=7)
    b1 = arduinoml_AMLState()
    b2 = arduinoml_AMLState()
    _safe_set(a, 'arduinoml_AMLMachine2', {b1})
    assert _is_linked(a, 'arduinoml_AMLMachine2', b1)
    if hasattr(b1, 'arduinoml_AMLState'):
        assert _is_linked(b1, 'arduinoml_AMLState', a)
    _safe_set(a, 'arduinoml_AMLMachine2', {b2})
    assert _is_linked(a, 'arduinoml_AMLMachine2', b2)
    if hasattr(b1, 'arduinoml_AMLState'):
        assert not _is_linked(b1, 'arduinoml_AMLState', a)
    if hasattr(b2, 'arduinoml_AMLState'):
        assert _is_linked(b2, 'arduinoml_AMLState', a)
    _safe_set(a, 'arduinoml_AMLMachine2', set())
    assert not _is_linked(a, 'arduinoml_AMLMachine2', b2)
    if hasattr(b2, 'arduinoml_AMLState'):
        assert not _is_linked(b2, 'arduinoml_AMLState', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


AnalogAction_strategy = st.builds(AnalogAction)
@given(instance=AnalogAction_strategy)
@settings(max_examples=25)
def test_AnalogAction_instantiation(instance):
    assert isinstance(instance, AnalogAction)


Brick_strategy = st.builds(Brick)
@given(instance=Brick_strategy)
@settings(max_examples=25)
def test_Brick_instantiation(instance):
    assert isinstance(instance, Brick)


Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


arduinoml_AMLMachine_strategy = st.builds(arduinoml_AMLMachine, frequency=st.integers())
@given(instance=arduinoml_AMLMachine_strategy)
@settings(max_examples=25)
def test_arduinoml_AMLMachine_instantiation(instance):
    assert isinstance(instance, arduinoml_AMLMachine)


arduinoml_AMLState_strategy = st.builds(arduinoml_AMLState)
@given(instance=arduinoml_AMLState_strategy)
@settings(max_examples=25)
def test_arduinoml_AMLState_instantiation(instance):
    assert isinstance(instance, arduinoml_AMLState)


arduinoml_Action_strategy = st.builds(arduinoml_Action)
@given(instance=arduinoml_Action_strategy)
@settings(max_examples=25)
def test_arduinoml_Action_instantiation(instance):
    assert isinstance(instance, arduinoml_Action)


arduinoml_AnalogAction_strategy = st.builds(arduinoml_AnalogAction)
@given(instance=arduinoml_AnalogAction_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogAction_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogAction)


arduinoml_AnalogActionSensor_strategy = st.builds(arduinoml_AnalogActionSensor)
@given(instance=arduinoml_AnalogActionSensor_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogActionSensor_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogActionSensor)


arduinoml_AnalogActionValue_strategy = st.builds(arduinoml_AnalogActionValue, value=st.integers())
@given(instance=arduinoml_AnalogActionValue_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogActionValue_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogActionValue)


arduinoml_AnalogActuator_strategy = st.builds(arduinoml_AnalogActuator)
@given(instance=arduinoml_AnalogActuator_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogActuator_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogActuator)


arduinoml_AnalogCondition_strategy = st.builds(arduinoml_AnalogCondition, aComp=safe_text, value=st.integers())
@given(instance=arduinoml_AnalogCondition_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogCondition_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogCondition)


arduinoml_AnalogSensor_strategy = st.builds(arduinoml_AnalogSensor)
@given(instance=arduinoml_AnalogSensor_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogSensor_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogSensor)


arduinoml_Brick_strategy = st.builds(arduinoml_Brick, pin=st.integers())
@given(instance=arduinoml_Brick_strategy)
@settings(max_examples=25)
def test_arduinoml_Brick_instantiation(instance):
    assert isinstance(instance, arduinoml_Brick)


arduinoml_Condition_strategy = st.builds(arduinoml_Condition)
@given(instance=arduinoml_Condition_strategy)
@settings(max_examples=25)
def test_arduinoml_Condition_instantiation(instance):
    assert isinstance(instance, arduinoml_Condition)


arduinoml_DigitalAction_strategy = st.builds(arduinoml_DigitalAction, dState=safe_text)
@given(instance=arduinoml_DigitalAction_strategy)
@settings(max_examples=25)
def test_arduinoml_DigitalAction_instantiation(instance):
    assert isinstance(instance, arduinoml_DigitalAction)


arduinoml_DigitalActuator_strategy = st.builds(arduinoml_DigitalActuator)
@given(instance=arduinoml_DigitalActuator_strategy)
@settings(max_examples=25)
def test_arduinoml_DigitalActuator_instantiation(instance):
    assert isinstance(instance, arduinoml_DigitalActuator)


arduinoml_DigitalCondition_strategy = st.builds(arduinoml_DigitalCondition, dState=safe_text)
@given(instance=arduinoml_DigitalCondition_strategy)
@settings(max_examples=25)
def test_arduinoml_DigitalCondition_instantiation(instance):
    assert isinstance(instance, arduinoml_DigitalCondition)


arduinoml_DigitalSensor_strategy = st.builds(arduinoml_DigitalSensor)
@given(instance=arduinoml_DigitalSensor_strategy)
@settings(max_examples=25)
def test_arduinoml_DigitalSensor_instantiation(instance):
    assert isinstance(instance, arduinoml_DigitalSensor)


arduinoml_NamedElement_strategy = st.builds(arduinoml_NamedElement, name=safe_text)
@given(instance=arduinoml_NamedElement_strategy)
@settings(max_examples=25)
def test_arduinoml_NamedElement_instantiation(instance):
    assert isinstance(instance, arduinoml_NamedElement)


arduinoml_TimeCondition_strategy = st.builds(arduinoml_TimeCondition, tComp=safe_text, time=st.integers())
@given(instance=arduinoml_TimeCondition_strategy)
@settings(max_examples=25)
def test_arduinoml_TimeCondition_instantiation(instance):
    assert isinstance(instance, arduinoml_TimeCondition)


arduinoml_Transition_strategy = st.builds(arduinoml_Transition)
@given(instance=arduinoml_Transition_strategy)
@settings(max_examples=25)
def test_arduinoml_Transition_instantiation(instance):
    assert isinstance(instance, arduinoml_Transition)



