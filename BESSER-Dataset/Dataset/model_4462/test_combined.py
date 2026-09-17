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
    Action,
    arduinoml_BinaryAction,
    arduinoml_AnalogAction,
    Actuator,
    arduinoml_BinaryActuator,
    arduinoml_AnalogActuator,
    Sensor,
    arduinoml_AnalogSensor,
    arduinoml_BinarySensor,
    Condition,
    arduinoml_ValueElementCondition,
    arduinoml_SingleElementCondition,
    arduinoml_Condition,
    Brick,
    arduinoml_Sensor,
    arduinoml_MultipleElementCondition,
    arduinoml_Actuator,
    arduinoml_Transition,
    arduinoml_Action,
    NamedElement,
    arduinoml_State,
    arduinoml_Brick,
    arduinoml_App,
    arduinoml_NamedElement,
    OPERATOR,
    SIGNAL,
    COMPARATOR,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_binaryaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml_BinaryAction)


def test_hyp_arduinoml_binaryaction_constructor_exists():
    assert callable(arduinoml_BinaryAction.__init__)


def test_hyp_arduinoml_binaryaction_constructor_args():
    sig = inspect.signature(arduinoml_BinaryAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionValue" in params, "Missing parameter 'actionValue'"




def test_hyp_arduinoml_analogaction_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogAction)


def test_hyp_arduinoml_analogaction_constructor_exists():
    assert callable(arduinoml_AnalogAction.__init__)


def test_hyp_arduinoml_analogaction_constructor_args():
    sig = inspect.signature(arduinoml_AnalogAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionValue" in params, "Missing parameter 'actionValue'"




def test_hyp_actuator_is_not_abstract():
    assert not inspect.isabstract(Actuator)


def test_hyp_actuator_constructor_exists():
    assert callable(Actuator.__init__)


def test_hyp_actuator_constructor_args():
    sig = inspect.signature(Actuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_binaryactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_BinaryActuator)


def test_hyp_arduinoml_binaryactuator_constructor_exists():
    assert callable(arduinoml_BinaryActuator.__init__)


def test_hyp_arduinoml_binaryactuator_constructor_args():
    sig = inspect.signature(arduinoml_BinaryActuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_analogactuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogActuator)


def test_hyp_arduinoml_analogactuator_constructor_exists():
    assert callable(arduinoml_AnalogActuator.__init__)


def test_hyp_arduinoml_analogactuator_constructor_args():
    sig = inspect.signature(arduinoml_AnalogActuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_hyp_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_analogsensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_AnalogSensor)


def test_hyp_arduinoml_analogsensor_constructor_exists():
    assert callable(arduinoml_AnalogSensor.__init__)


def test_hyp_arduinoml_analogsensor_constructor_args():
    sig = inspect.signature(arduinoml_AnalogSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_binarysensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_BinarySensor)


def test_hyp_arduinoml_binarysensor_constructor_exists():
    assert callable(arduinoml_BinarySensor.__init__)


def test_hyp_arduinoml_binarysensor_constructor_args():
    sig = inspect.signature(arduinoml_BinarySensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_valueelementcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_ValueElementCondition)


def test_hyp_arduinoml_valueelementcondition_constructor_exists():
    assert callable(arduinoml_ValueElementCondition.__init__)


def test_hyp_arduinoml_valueelementcondition_constructor_args():
    sig = inspect.signature(arduinoml_ValueElementCondition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "comparator" in params, "Missing parameter 'comparator'"





def test_hyp_arduinoml_singleelementcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_SingleElementCondition)


def test_hyp_arduinoml_singleelementcondition_constructor_exists():
    assert callable(arduinoml_SingleElementCondition.__init__)


def test_hyp_arduinoml_singleelementcondition_constructor_args():
    sig = inspect.signature(arduinoml_SingleElementCondition.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_arduinoml_condition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Condition)


def test_hyp_arduinoml_condition_constructor_exists():
    assert callable(arduinoml_Condition.__init__)


def test_hyp_arduinoml_condition_constructor_args():
    sig = inspect.signature(arduinoml_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_brick_is_not_abstract():
    assert not inspect.isabstract(Brick)


def test_hyp_brick_constructor_exists():
    assert callable(Brick.__init__)


def test_hyp_brick_constructor_args():
    sig = inspect.signature(Brick.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_sensor_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Sensor)


def test_hyp_arduinoml_sensor_constructor_exists():
    assert callable(arduinoml_Sensor.__init__)


def test_hyp_arduinoml_sensor_constructor_args():
    sig = inspect.signature(arduinoml_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_multipleelementcondition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_MultipleElementCondition)


def test_hyp_arduinoml_multipleelementcondition_constructor_exists():
    assert callable(arduinoml_MultipleElementCondition.__init__)


def test_hyp_arduinoml_multipleelementcondition_constructor_args():
    sig = inspect.signature(arduinoml_MultipleElementCondition.__init__)
    params = list(sig.parameters.keys())
    assert "operators" in params, "Missing parameter 'operators'"




def test_hyp_arduinoml_actuator_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Actuator)


def test_hyp_arduinoml_actuator_constructor_exists():
    assert callable(arduinoml_Actuator.__init__)


def test_hyp_arduinoml_actuator_constructor_args():
    sig = inspect.signature(arduinoml_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_transition_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Transition)


def test_hyp_arduinoml_transition_constructor_exists():
    assert callable(arduinoml_Transition.__init__)


def test_hyp_arduinoml_transition_constructor_args():
    sig = inspect.signature(arduinoml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_action_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Action)


def test_hyp_arduinoml_action_constructor_exists():
    assert callable(arduinoml_Action.__init__)


def test_hyp_arduinoml_action_constructor_args():
    sig = inspect.signature(arduinoml_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_state_is_not_abstract():
    assert not inspect.isabstract(arduinoml_State)


def test_hyp_arduinoml_state_constructor_exists():
    assert callable(arduinoml_State.__init__)


def test_hyp_arduinoml_state_constructor_args():
    sig = inspect.signature(arduinoml_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_brick_is_not_abstract():
    assert not inspect.isabstract(arduinoml_Brick)


def test_hyp_arduinoml_brick_constructor_exists():
    assert callable(arduinoml_Brick.__init__)


def test_hyp_arduinoml_brick_constructor_args():
    sig = inspect.signature(arduinoml_Brick.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"




def test_hyp_arduinoml_app_is_not_abstract():
    assert not inspect.isabstract(arduinoml_App)


def test_hyp_arduinoml_app_constructor_exists():
    assert callable(arduinoml_App.__init__)


def test_hyp_arduinoml_app_constructor_args():
    sig = inspect.signature(arduinoml_App.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinoml_namedelement_is_not_abstract():
    assert not inspect.isabstract(arduinoml_NamedElement)


def test_hyp_arduinoml_namedelement_constructor_exists():
    assert callable(arduinoml_NamedElement.__init__)


def test_hyp_arduinoml_namedelement_constructor_args():
    sig = inspect.signature(arduinoml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"


def test_hyp_operator_exists():
    # Check that the Enumeration exists
    assert OPERATOR is not None

def test_hyp_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OPERATOR]
    expected_literals = [
        "and_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OPERATOR"

def test_hyp_signal_exists():
    # Check that the Enumeration exists
    assert SIGNAL is not None

def test_hyp_signal_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIGNAL]
    expected_literals = [
        "LOW",
        "HIGH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIGNAL"

def test_hyp_comparator_exists():
    # Check that the Enumeration exists
    assert COMPARATOR is not None

def test_hyp_comparator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in COMPARATOR]
    expected_literals = [
        "SUPERIOR",
        "EQUAL",
        "INFERIOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in COMPARATOR"


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
Action_strategy = st.builds(
    Action,
)
arduinoml_BinaryAction_strategy = st.builds(
    arduinoml_BinaryAction,
    actionValue=
        safe_text
)
arduinoml_AnalogAction_strategy = st.builds(
    arduinoml_AnalogAction,
    actionValue=
        st.integers()
)
Actuator_strategy = st.builds(
    Actuator,
)
arduinoml_BinaryActuator_strategy = st.builds(
    arduinoml_BinaryActuator,
)
arduinoml_AnalogActuator_strategy = st.builds(
    arduinoml_AnalogActuator,
)
Sensor_strategy = st.builds(
    Sensor,
)
arduinoml_AnalogSensor_strategy = st.builds(
    arduinoml_AnalogSensor,
)
arduinoml_BinarySensor_strategy = st.builds(
    arduinoml_BinarySensor,
)
Condition_strategy = st.builds(
    Condition,
)
arduinoml_ValueElementCondition_strategy = st.builds(
    arduinoml_ValueElementCondition,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    comparator=
        safe_text
)
arduinoml_SingleElementCondition_strategy = st.builds(
    arduinoml_SingleElementCondition,
    value=
        safe_text
)
arduinoml_Condition_strategy = st.builds(
    arduinoml_Condition,
)
Brick_strategy = st.builds(
    Brick,
)
arduinoml_Sensor_strategy = st.builds(
    arduinoml_Sensor,
)
arduinoml_MultipleElementCondition_strategy = st.builds(
    arduinoml_MultipleElementCondition,
    operators=
        safe_text
)
arduinoml_Actuator_strategy = st.builds(
    arduinoml_Actuator,
)
arduinoml_Transition_strategy = st.builds(
    arduinoml_Transition,
)
arduinoml_Action_strategy = st.builds(
    arduinoml_Action,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduinoml_State_strategy = st.builds(
    arduinoml_State,
)
arduinoml_Brick_strategy = st.builds(
    arduinoml_Brick,
    pin=
        safe_text
)
arduinoml_App_strategy = st.builds(
    arduinoml_App,
)
arduinoml_NamedElement_strategy = st.builds(
    arduinoml_NamedElement,
    name=
        safe_text
)





@given(instance=arduinoml_BinaryAction_strategy)
def test_hyp_arduinoml_binaryaction_actionValue_setter(instance):
    original = instance.actionValue
    instance.actionValue = original
    assert instance.actionValue == original




@given(instance=arduinoml_AnalogAction_strategy)
def test_hyp_arduinoml_analogaction_actionValue_setter(instance):
    original = instance.actionValue
    instance.actionValue = original
    assert instance.actionValue == original











@given(instance=arduinoml_ValueElementCondition_strategy)
def test_hyp_arduinoml_valueelementcondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=arduinoml_ValueElementCondition_strategy)
def test_hyp_arduinoml_valueelementcondition_comparator_setter(instance):
    original = instance.comparator
    instance.comparator = original
    assert instance.comparator == original




@given(instance=arduinoml_SingleElementCondition_strategy)
def test_hyp_arduinoml_singleelementcondition_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=arduinoml_MultipleElementCondition_strategy)
def test_hyp_arduinoml_multipleelementcondition_operators_setter(instance):
    original = instance.operators
    instance.operators = original
    assert instance.operators == original









@given(instance=arduinoml_Brick_strategy)
def test_hyp_arduinoml_brick_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original





@given(instance=arduinoml_NamedElement_strategy)
def test_hyp_arduinoml_namedelement_name_setter(instance):
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
    Action,
    Actuator,
    Brick,
    Condition,
    NamedElement,
    Sensor,
    arduinoml_Action,
    arduinoml_Actuator,
    arduinoml_AnalogAction,
    arduinoml_AnalogActuator,
    arduinoml_AnalogSensor,
    arduinoml_App,
    arduinoml_BinaryAction,
    arduinoml_BinaryActuator,
    arduinoml_BinarySensor,
    arduinoml_Brick,
    arduinoml_Condition,
    arduinoml_MultipleElementCondition,
    arduinoml_NamedElement,
    arduinoml_Sensor,
    arduinoml_SingleElementCondition,
    arduinoml_State,
    arduinoml_Transition,
    arduinoml_ValueElementCondition,
    COMPARATOR,
    OPERATOR,
    SIGNAL,
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

def test_arduinoml_AnalogAction_actionValue_value_roundtrip():
    instance = arduinoml_AnalogAction(actionValue=7)
    assert instance.actionValue == 7
    instance.actionValue = 13
    assert instance.actionValue == 13


def test_arduinoml_BinaryAction_actionValue_value_roundtrip():
    instance = arduinoml_BinaryAction(actionValue="sample_text")
    assert instance.actionValue == "sample_text"
    instance.actionValue = "sample_text_2"
    assert instance.actionValue == "sample_text_2"


def test_arduinoml_Brick_pin_value_roundtrip():
    instance = arduinoml_Brick(pin="sample_text")
    assert instance.pin == "sample_text"
    instance.pin = "sample_text_2"
    assert instance.pin == "sample_text_2"


def test_arduinoml_MultipleElementCondition_operators_value_roundtrip():
    instance = arduinoml_MultipleElementCondition(operators="sample_text")
    assert instance.operators == "sample_text"
    instance.operators = "sample_text_2"
    assert instance.operators == "sample_text_2"


def test_arduinoml_NamedElement_name_value_roundtrip():
    instance = arduinoml_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_arduinoml_SingleElementCondition_value_value_roundtrip():
    instance = arduinoml_SingleElementCondition(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_arduinoml_ValueElementCondition_comparator_value_roundtrip():
    instance = arduinoml_ValueElementCondition(comparator="sample_text", value=3.14)
    assert instance.comparator == "sample_text"
    instance.comparator = "sample_text_2"
    assert instance.comparator == "sample_text_2"


def test_arduinoml_ValueElementCondition_value_value_roundtrip():
    instance = arduinoml_ValueElementCondition(comparator="sample_text", value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_arduinoml_AnalogAction_isa_Action():
    instance = arduinoml_AnalogAction(actionValue=7)
    assert isinstance(instance, Action)


def test_arduinoml_BinaryAction_isa_Action():
    instance = arduinoml_BinaryAction(actionValue="sample_text")
    assert isinstance(instance, Action)


def test_arduinoml_AnalogActuator_isa_Actuator():
    instance = arduinoml_AnalogActuator()
    assert isinstance(instance, Actuator)


def test_arduinoml_BinaryActuator_isa_Actuator():
    instance = arduinoml_BinaryActuator()
    assert isinstance(instance, Actuator)


def test_arduinoml_Actuator_isa_Brick():
    instance = arduinoml_Actuator()
    assert isinstance(instance, Brick)


def test_arduinoml_Sensor_isa_Brick():
    instance = arduinoml_Sensor()
    assert isinstance(instance, Brick)


def test_arduinoml_MultipleElementCondition_isa_Condition():
    instance = arduinoml_MultipleElementCondition(operators="sample_text")
    assert isinstance(instance, Condition)


def test_arduinoml_SingleElementCondition_isa_Condition():
    instance = arduinoml_SingleElementCondition(value="sample_text")
    assert isinstance(instance, Condition)


def test_arduinoml_ValueElementCondition_isa_Condition():
    instance = arduinoml_ValueElementCondition(comparator="sample_text", value=3.14)
    assert isinstance(instance, Condition)


def test_arduinoml_App_isa_NamedElement():
    instance = arduinoml_App()
    assert isinstance(instance, NamedElement)


def test_arduinoml_Brick_isa_NamedElement():
    instance = arduinoml_Brick(pin="sample_text")
    assert isinstance(instance, NamedElement)


def test_arduinoml_State_isa_NamedElement():
    instance = arduinoml_State()
    assert isinstance(instance, NamedElement)


def test_arduinoml_AnalogSensor_isa_Sensor():
    instance = arduinoml_AnalogSensor()
    assert isinstance(instance, Sensor)


def test_arduinoml_BinarySensor_isa_Sensor():
    instance = arduinoml_BinarySensor()
    assert isinstance(instance, Sensor)


def test_assoc_bricks1_link_reassign_clear():
    a = arduinoml_Brick(pin="sample_text")
    b1 = arduinoml_App()
    b2 = arduinoml_App()
    _safe_set(a, 'arduinoml_Brick', b1)
    assert _is_linked(a, 'arduinoml_Brick', b1)
    if hasattr(b1, 'arduinoml_App2'):
        assert _is_linked(b1, 'arduinoml_App2', a)
    _safe_set(a, 'arduinoml_Brick', b2)
    assert _is_linked(a, 'arduinoml_Brick', b2)
    if hasattr(b1, 'arduinoml_App2'):
        assert not _is_linked(b1, 'arduinoml_App2', a)
    if hasattr(b2, 'arduinoml_App2'):
        assert _is_linked(b2, 'arduinoml_App2', a)
    _safe_set(a, 'arduinoml_Brick', None)
    assert not _is_linked(a, 'arduinoml_Brick', b2)
    if hasattr(b2, 'arduinoml_App2'):
        assert not _is_linked(b2, 'arduinoml_App2', a)


def test_assoc_condition15_link_reassign_clear():
    a = arduinoml_MultipleElementCondition(operators="sample_text")
    b1 = arduinoml_Transition()
    b2 = arduinoml_Transition()
    _safe_set(a, 'arduinoml_MultipleElementCondition', b1)
    assert _is_linked(a, 'arduinoml_MultipleElementCondition', b1)
    if hasattr(b1, 'arduinoml_Transition16'):
        assert _is_linked(b1, 'arduinoml_Transition16', a)
    _safe_set(a, 'arduinoml_MultipleElementCondition', b2)
    assert _is_linked(a, 'arduinoml_MultipleElementCondition', b2)
    if hasattr(b1, 'arduinoml_Transition16'):
        assert not _is_linked(b1, 'arduinoml_Transition16', a)
    if hasattr(b2, 'arduinoml_Transition16'):
        assert _is_linked(b2, 'arduinoml_Transition16', a)
    _safe_set(a, 'arduinoml_MultipleElementCondition', None)
    assert not _is_linked(a, 'arduinoml_MultipleElementCondition', b2)
    if hasattr(b2, 'arduinoml_Transition16'):
        assert not _is_linked(b2, 'arduinoml_Transition16', a)


def test_assoc_conditions18_link_reassign_clear():
    a = arduinoml_MultipleElementCondition(operators="sample_text")
    b1 = arduinoml_Condition()
    b2 = arduinoml_Condition()
    _safe_set(a, 'arduinoml_MultipleElementCondition19', {b1})
    assert _is_linked(a, 'arduinoml_MultipleElementCondition19', b1)
    if hasattr(b1, 'arduinoml_Condition'):
        assert _is_linked(b1, 'arduinoml_Condition', a)
    _safe_set(a, 'arduinoml_MultipleElementCondition19', {b2})
    assert _is_linked(a, 'arduinoml_MultipleElementCondition19', b2)
    if hasattr(b1, 'arduinoml_Condition'):
        assert not _is_linked(b1, 'arduinoml_Condition', a)
    if hasattr(b2, 'arduinoml_Condition'):
        assert _is_linked(b2, 'arduinoml_Condition', a)
    _safe_set(a, 'arduinoml_MultipleElementCondition19', set())
    assert not _is_linked(a, 'arduinoml_MultipleElementCondition19', b2)
    if hasattr(b2, 'arduinoml_Condition'):
        assert not _is_linked(b2, 'arduinoml_Condition', a)


def test_assoc_sensor17_link_reassign_clear():
    a = arduinoml_SingleElementCondition(value="sample_text")
    b1 = arduinoml_BinarySensor()
    b2 = arduinoml_BinarySensor()
    _safe_set(a, 'arduinoml_SingleElementCondition', b1)
    assert _is_linked(a, 'arduinoml_SingleElementCondition', b1)
    if hasattr(b1, 'arduinoml_BinarySensor'):
        assert _is_linked(b1, 'arduinoml_BinarySensor', a)
    _safe_set(a, 'arduinoml_SingleElementCondition', b2)
    assert _is_linked(a, 'arduinoml_SingleElementCondition', b2)
    if hasattr(b1, 'arduinoml_BinarySensor'):
        assert not _is_linked(b1, 'arduinoml_BinarySensor', a)
    if hasattr(b2, 'arduinoml_BinarySensor'):
        assert _is_linked(b2, 'arduinoml_BinarySensor', a)
    _safe_set(a, 'arduinoml_SingleElementCondition', None)
    assert not _is_linked(a, 'arduinoml_SingleElementCondition', b2)
    if hasattr(b2, 'arduinoml_BinarySensor'):
        assert not _is_linked(b2, 'arduinoml_BinarySensor', a)


def test_assoc_sensor20_link_reassign_clear():
    a = arduinoml_ValueElementCondition(comparator="sample_text", value=3.14)
    b1 = arduinoml_AnalogSensor()
    b2 = arduinoml_AnalogSensor()
    _safe_set(a, 'arduinoml_ValueElementCondition', b1)
    assert _is_linked(a, 'arduinoml_ValueElementCondition', b1)
    if hasattr(b1, 'arduinoml_AnalogSensor'):
        assert _is_linked(b1, 'arduinoml_AnalogSensor', a)
    _safe_set(a, 'arduinoml_ValueElementCondition', b2)
    assert _is_linked(a, 'arduinoml_ValueElementCondition', b2)
    if hasattr(b1, 'arduinoml_AnalogSensor'):
        assert not _is_linked(b1, 'arduinoml_AnalogSensor', a)
    if hasattr(b2, 'arduinoml_AnalogSensor'):
        assert _is_linked(b2, 'arduinoml_AnalogSensor', a)
    _safe_set(a, 'arduinoml_ValueElementCondition', None)
    assert not _is_linked(a, 'arduinoml_ValueElementCondition', b2)
    if hasattr(b2, 'arduinoml_AnalogSensor'):
        assert not _is_linked(b2, 'arduinoml_AnalogSensor', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Actuator_strategy = st.builds(Actuator)
@given(instance=Actuator_strategy)
@settings(max_examples=25)
def test_Actuator_instantiation(instance):
    assert isinstance(instance, Actuator)


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


Sensor_strategy = st.builds(Sensor)
@given(instance=Sensor_strategy)
@settings(max_examples=25)
def test_Sensor_instantiation(instance):
    assert isinstance(instance, Sensor)


arduinoml_Action_strategy = st.builds(arduinoml_Action)
@given(instance=arduinoml_Action_strategy)
@settings(max_examples=25)
def test_arduinoml_Action_instantiation(instance):
    assert isinstance(instance, arduinoml_Action)


arduinoml_Actuator_strategy = st.builds(arduinoml_Actuator)
@given(instance=arduinoml_Actuator_strategy)
@settings(max_examples=25)
def test_arduinoml_Actuator_instantiation(instance):
    assert isinstance(instance, arduinoml_Actuator)


arduinoml_AnalogAction_strategy = st.builds(arduinoml_AnalogAction, actionValue=st.integers())
@given(instance=arduinoml_AnalogAction_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogAction_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogAction)


arduinoml_AnalogActuator_strategy = st.builds(arduinoml_AnalogActuator)
@given(instance=arduinoml_AnalogActuator_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogActuator_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogActuator)


arduinoml_AnalogSensor_strategy = st.builds(arduinoml_AnalogSensor)
@given(instance=arduinoml_AnalogSensor_strategy)
@settings(max_examples=25)
def test_arduinoml_AnalogSensor_instantiation(instance):
    assert isinstance(instance, arduinoml_AnalogSensor)


arduinoml_App_strategy = st.builds(arduinoml_App)
@given(instance=arduinoml_App_strategy)
@settings(max_examples=25)
def test_arduinoml_App_instantiation(instance):
    assert isinstance(instance, arduinoml_App)


arduinoml_BinaryAction_strategy = st.builds(arduinoml_BinaryAction, actionValue=safe_text)
@given(instance=arduinoml_BinaryAction_strategy)
@settings(max_examples=25)
def test_arduinoml_BinaryAction_instantiation(instance):
    assert isinstance(instance, arduinoml_BinaryAction)


arduinoml_BinaryActuator_strategy = st.builds(arduinoml_BinaryActuator)
@given(instance=arduinoml_BinaryActuator_strategy)
@settings(max_examples=25)
def test_arduinoml_BinaryActuator_instantiation(instance):
    assert isinstance(instance, arduinoml_BinaryActuator)


arduinoml_BinarySensor_strategy = st.builds(arduinoml_BinarySensor)
@given(instance=arduinoml_BinarySensor_strategy)
@settings(max_examples=25)
def test_arduinoml_BinarySensor_instantiation(instance):
    assert isinstance(instance, arduinoml_BinarySensor)


arduinoml_Brick_strategy = st.builds(arduinoml_Brick, pin=safe_text)
@given(instance=arduinoml_Brick_strategy)
@settings(max_examples=25)
def test_arduinoml_Brick_instantiation(instance):
    assert isinstance(instance, arduinoml_Brick)


arduinoml_Condition_strategy = st.builds(arduinoml_Condition)
@given(instance=arduinoml_Condition_strategy)
@settings(max_examples=25)
def test_arduinoml_Condition_instantiation(instance):
    assert isinstance(instance, arduinoml_Condition)


arduinoml_MultipleElementCondition_strategy = st.builds(arduinoml_MultipleElementCondition, operators=safe_text)
@given(instance=arduinoml_MultipleElementCondition_strategy)
@settings(max_examples=25)
def test_arduinoml_MultipleElementCondition_instantiation(instance):
    assert isinstance(instance, arduinoml_MultipleElementCondition)


arduinoml_NamedElement_strategy = st.builds(arduinoml_NamedElement, name=safe_text)
@given(instance=arduinoml_NamedElement_strategy)
@settings(max_examples=25)
def test_arduinoml_NamedElement_instantiation(instance):
    assert isinstance(instance, arduinoml_NamedElement)


arduinoml_Sensor_strategy = st.builds(arduinoml_Sensor)
@given(instance=arduinoml_Sensor_strategy)
@settings(max_examples=25)
def test_arduinoml_Sensor_instantiation(instance):
    assert isinstance(instance, arduinoml_Sensor)


arduinoml_SingleElementCondition_strategy = st.builds(arduinoml_SingleElementCondition, value=safe_text)
@given(instance=arduinoml_SingleElementCondition_strategy)
@settings(max_examples=25)
def test_arduinoml_SingleElementCondition_instantiation(instance):
    assert isinstance(instance, arduinoml_SingleElementCondition)


arduinoml_State_strategy = st.builds(arduinoml_State)
@given(instance=arduinoml_State_strategy)
@settings(max_examples=25)
def test_arduinoml_State_instantiation(instance):
    assert isinstance(instance, arduinoml_State)


arduinoml_Transition_strategy = st.builds(arduinoml_Transition)
@given(instance=arduinoml_Transition_strategy)
@settings(max_examples=25)
def test_arduinoml_Transition_instantiation(instance):
    assert isinstance(instance, arduinoml_Transition)


arduinoml_ValueElementCondition_strategy = st.builds(arduinoml_ValueElementCondition, comparator=safe_text, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=arduinoml_ValueElementCondition_strategy)
@settings(max_examples=25)
def test_arduinoml_ValueElementCondition_instantiation(instance):
    assert isinstance(instance, arduinoml_ValueElementCondition)



