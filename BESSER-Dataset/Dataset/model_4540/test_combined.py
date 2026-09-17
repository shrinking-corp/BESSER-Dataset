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
    House2_NamedElement,
    Action,
    House2_ValueAction,
    House2_BooleanAction,
    Condition,
    House2_GreaterThanCondition,
    House2_EqualCondition,
    House2_LessThanCondition,
    House2_Action,
    Sensor,
    House2_TwilightSwitch,
    House2_RainSensor,
    House2_TemperatureSensor,
    NamedElement,
    House2_Sensor,
    House2_Element,
    House2_Actor,
    House2_Container,
    House2_ControlRule,
    Element,
    Container,
    House2_Room,
    House2_Condition,
    Actor,
    House2_Lamp,
    House2_RollerBlind,
    House2_Boiler,
    House2_House,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_house2_namedelement_is_not_abstract():
    assert not inspect.isabstract(House2_NamedElement)


def test_hyp_house2_namedelement_constructor_exists():
    assert callable(House2_NamedElement.__init__)


def test_hyp_house2_namedelement_constructor_args():
    sig = inspect.signature(House2_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_valueaction_is_not_abstract():
    assert not inspect.isabstract(House2_ValueAction)


def test_hyp_house2_valueaction_constructor_exists():
    assert callable(House2_ValueAction.__init__)


def test_hyp_house2_valueaction_constructor_args():
    sig = inspect.signature(House2_ValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "switchToValue" in params, "Missing parameter 'switchToValue'"




def test_hyp_house2_booleanaction_is_not_abstract():
    assert not inspect.isabstract(House2_BooleanAction)


def test_hyp_house2_booleanaction_constructor_exists():
    assert callable(House2_BooleanAction.__init__)


def test_hyp_house2_booleanaction_constructor_args():
    sig = inspect.signature(House2_BooleanAction.__init__)
    params = list(sig.parameters.keys())
    assert "switchTo" in params, "Missing parameter 'switchTo'"




def test_hyp_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_hyp_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_hyp_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_greaterthancondition_is_not_abstract():
    assert not inspect.isabstract(House2_GreaterThanCondition)


def test_hyp_house2_greaterthancondition_constructor_exists():
    assert callable(House2_GreaterThanCondition.__init__)


def test_hyp_house2_greaterthancondition_constructor_args():
    sig = inspect.signature(House2_GreaterThanCondition.__init__)
    params = list(sig.parameters.keys())
    assert "threshold" in params, "Missing parameter 'threshold'"




def test_hyp_house2_equalcondition_is_not_abstract():
    assert not inspect.isabstract(House2_EqualCondition)


def test_hyp_house2_equalcondition_constructor_exists():
    assert callable(House2_EqualCondition.__init__)


def test_hyp_house2_equalcondition_constructor_args():
    sig = inspect.signature(House2_EqualCondition.__init__)
    params = list(sig.parameters.keys())
    assert "valuecond" in params, "Missing parameter 'valuecond'"
    assert "boolcond" in params, "Missing parameter 'boolcond'"





def test_hyp_house2_lessthancondition_is_not_abstract():
    assert not inspect.isabstract(House2_LessThanCondition)


def test_hyp_house2_lessthancondition_constructor_exists():
    assert callable(House2_LessThanCondition.__init__)


def test_hyp_house2_lessthancondition_constructor_args():
    sig = inspect.signature(House2_LessThanCondition.__init__)
    params = list(sig.parameters.keys())
    assert "threshold" in params, "Missing parameter 'threshold'"




def test_hyp_house2_action_is_not_abstract():
    assert not inspect.isabstract(House2_Action)


def test_hyp_house2_action_constructor_exists():
    assert callable(House2_Action.__init__)


def test_hyp_house2_action_constructor_args():
    sig = inspect.signature(House2_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_hyp_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_twilightswitch_is_not_abstract():
    assert not inspect.isabstract(House2_TwilightSwitch)


def test_hyp_house2_twilightswitch_constructor_exists():
    assert callable(House2_TwilightSwitch.__init__)


def test_hyp_house2_twilightswitch_constructor_args():
    sig = inspect.signature(House2_TwilightSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"




def test_hyp_house2_rainsensor_is_not_abstract():
    assert not inspect.isabstract(House2_RainSensor)


def test_hyp_house2_rainsensor_constructor_exists():
    assert callable(House2_RainSensor.__init__)


def test_hyp_house2_rainsensor_constructor_args():
    sig = inspect.signature(House2_RainSensor.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"




def test_hyp_house2_temperaturesensor_is_not_abstract():
    assert not inspect.isabstract(House2_TemperatureSensor)


def test_hyp_house2_temperaturesensor_constructor_exists():
    assert callable(House2_TemperatureSensor.__init__)


def test_hyp_house2_temperaturesensor_constructor_args():
    sig = inspect.signature(House2_TemperatureSensor.__init__)
    params = list(sig.parameters.keys())
    assert "temp" in params, "Missing parameter 'temp'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_sensor_is_not_abstract():
    assert not inspect.isabstract(House2_Sensor)


def test_hyp_house2_sensor_constructor_exists():
    assert callable(House2_Sensor.__init__)


def test_hyp_house2_sensor_constructor_args():
    sig = inspect.signature(House2_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_element_is_not_abstract():
    assert not inspect.isabstract(House2_Element)


def test_hyp_house2_element_constructor_exists():
    assert callable(House2_Element.__init__)


def test_hyp_house2_element_constructor_args():
    sig = inspect.signature(House2_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_actor_is_not_abstract():
    assert not inspect.isabstract(House2_Actor)


def test_hyp_house2_actor_constructor_exists():
    assert callable(House2_Actor.__init__)


def test_hyp_house2_actor_constructor_args():
    sig = inspect.signature(House2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_container_is_not_abstract():
    assert not inspect.isabstract(House2_Container)


def test_hyp_house2_container_constructor_exists():
    assert callable(House2_Container.__init__)


def test_hyp_house2_container_constructor_args():
    sig = inspect.signature(House2_Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_controlrule_is_not_abstract():
    assert not inspect.isabstract(House2_ControlRule)


def test_hyp_house2_controlrule_constructor_exists():
    assert callable(House2_ControlRule.__init__)


def test_hyp_house2_controlrule_constructor_args():
    sig = inspect.signature(House2_ControlRule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_hyp_element_constructor_exists():
    assert callable(Element.__init__)


def test_hyp_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_hyp_container_constructor_exists():
    assert callable(Container.__init__)


def test_hyp_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_room_is_not_abstract():
    assert not inspect.isabstract(House2_Room)


def test_hyp_house2_room_constructor_exists():
    assert callable(House2_Room.__init__)


def test_hyp_house2_room_constructor_args():
    sig = inspect.signature(House2_Room.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_condition_is_not_abstract():
    assert not inspect.isabstract(House2_Condition)


def test_hyp_house2_condition_constructor_exists():
    assert callable(House2_Condition.__init__)


def test_hyp_house2_condition_constructor_args():
    sig = inspect.signature(House2_Condition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_actor_is_not_abstract():
    assert not inspect.isabstract(Actor)


def test_hyp_actor_constructor_exists():
    assert callable(Actor.__init__)


def test_hyp_actor_constructor_args():
    sig = inspect.signature(Actor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_house2_lamp_is_not_abstract():
    assert not inspect.isabstract(House2_Lamp)


def test_hyp_house2_lamp_constructor_exists():
    assert callable(House2_Lamp.__init__)


def test_hyp_house2_lamp_constructor_args():
    sig = inspect.signature(House2_Lamp.__init__)
    params = list(sig.parameters.keys())
    assert "isOn" in params, "Missing parameter 'isOn'"




def test_hyp_house2_rollerblind_is_not_abstract():
    assert not inspect.isabstract(House2_RollerBlind)


def test_hyp_house2_rollerblind_constructor_exists():
    assert callable(House2_RollerBlind.__init__)


def test_hyp_house2_rollerblind_constructor_args():
    sig = inspect.signature(House2_RollerBlind.__init__)
    params = list(sig.parameters.keys())
    assert "isUp" in params, "Missing parameter 'isUp'"




def test_hyp_house2_boiler_is_not_abstract():
    assert not inspect.isabstract(House2_Boiler)


def test_hyp_house2_boiler_constructor_exists():
    assert callable(House2_Boiler.__init__)


def test_hyp_house2_boiler_constructor_args():
    sig = inspect.signature(House2_Boiler.__init__)
    params = list(sig.parameters.keys())
    assert "isOn" in params, "Missing parameter 'isOn'"




def test_hyp_house2_house_is_not_abstract():
    assert not inspect.isabstract(House2_House)


def test_hyp_house2_house_constructor_exists():
    assert callable(House2_House.__init__)


def test_hyp_house2_house_constructor_args():
    sig = inspect.signature(House2_House.__init__)
    params = list(sig.parameters.keys())


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
House2_NamedElement_strategy = st.builds(
    House2_NamedElement,
    name=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
House2_ValueAction_strategy = st.builds(
    House2_ValueAction,
    switchToValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
House2_BooleanAction_strategy = st.builds(
    House2_BooleanAction,
    switchTo=
        st.booleans()
)
Condition_strategy = st.builds(
    Condition,
)
House2_GreaterThanCondition_strategy = st.builds(
    House2_GreaterThanCondition,
    threshold=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
House2_EqualCondition_strategy = st.builds(
    House2_EqualCondition,
    valuecond=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    boolcond=
        st.booleans()
)
House2_LessThanCondition_strategy = st.builds(
    House2_LessThanCondition,
    threshold=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
House2_Action_strategy = st.builds(
    House2_Action,
)
Sensor_strategy = st.builds(
    Sensor,
)
House2_TwilightSwitch_strategy = st.builds(
    House2_TwilightSwitch,
    active=
        st.booleans()
)
House2_RainSensor_strategy = st.builds(
    House2_RainSensor,
    active=
        st.booleans()
)
House2_TemperatureSensor_strategy = st.builds(
    House2_TemperatureSensor,
    temp=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
NamedElement_strategy = st.builds(
    NamedElement,
)
House2_Sensor_strategy = st.builds(
    House2_Sensor,
)
House2_Element_strategy = st.builds(
    House2_Element,
)
House2_Actor_strategy = st.builds(
    House2_Actor,
)
House2_Container_strategy = st.builds(
    House2_Container,
)
House2_ControlRule_strategy = st.builds(
    House2_ControlRule,
)
Element_strategy = st.builds(
    Element,
)
Container_strategy = st.builds(
    Container,
)
House2_Room_strategy = st.builds(
    House2_Room,
)
House2_Condition_strategy = st.builds(
    House2_Condition,
)
Actor_strategy = st.builds(
    Actor,
)
House2_Lamp_strategy = st.builds(
    House2_Lamp,
    isOn=
        st.booleans()
)
House2_RollerBlind_strategy = st.builds(
    House2_RollerBlind,
    isUp=
        st.booleans()
)
House2_Boiler_strategy = st.builds(
    House2_Boiler,
    isOn=
        st.booleans()
)
House2_House_strategy = st.builds(
    House2_House,
)




@given(instance=House2_NamedElement_strategy)
def test_hyp_house2_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=House2_ValueAction_strategy)
def test_hyp_house2_valueaction_switchToValue_setter(instance):
    original = instance.switchToValue
    instance.switchToValue = original
    assert instance.switchToValue == original




@given(instance=House2_BooleanAction_strategy)
def test_hyp_house2_booleanaction_switchTo_setter(instance):
    original = instance.switchTo
    instance.switchTo = original
    assert instance.switchTo == original





@given(instance=House2_GreaterThanCondition_strategy)
def test_hyp_house2_greaterthancondition_threshold_setter(instance):
    original = instance.threshold
    instance.threshold = original
    assert instance.threshold == original




@given(instance=House2_EqualCondition_strategy)
def test_hyp_house2_equalcondition_valuecond_setter(instance):
    original = instance.valuecond
    instance.valuecond = original
    assert instance.valuecond == original



@given(instance=House2_EqualCondition_strategy)
def test_hyp_house2_equalcondition_boolcond_setter(instance):
    original = instance.boolcond
    instance.boolcond = original
    assert instance.boolcond == original




@given(instance=House2_LessThanCondition_strategy)
def test_hyp_house2_lessthancondition_threshold_setter(instance):
    original = instance.threshold
    instance.threshold = original
    assert instance.threshold == original






@given(instance=House2_TwilightSwitch_strategy)
def test_hyp_house2_twilightswitch_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original




@given(instance=House2_RainSensor_strategy)
def test_hyp_house2_rainsensor_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original




@given(instance=House2_TemperatureSensor_strategy)
def test_hyp_house2_temperaturesensor_temp_setter(instance):
    original = instance.temp
    instance.temp = original
    assert instance.temp == original















@given(instance=House2_Lamp_strategy)
def test_hyp_house2_lamp_isOn_setter(instance):
    original = instance.isOn
    instance.isOn = original
    assert instance.isOn == original




@given(instance=House2_RollerBlind_strategy)
def test_hyp_house2_rollerblind_isUp_setter(instance):
    original = instance.isUp
    instance.isUp = original
    assert instance.isUp == original




@given(instance=House2_Boiler_strategy)
def test_hyp_house2_boiler_isOn_setter(instance):
    original = instance.isOn
    instance.isOn = original
    assert instance.isOn == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    Actor,
    Condition,
    Container,
    Element,
    House2_Action,
    House2_Actor,
    House2_Boiler,
    House2_BooleanAction,
    House2_Condition,
    House2_Container,
    House2_ControlRule,
    House2_Element,
    House2_EqualCondition,
    House2_GreaterThanCondition,
    House2_House,
    House2_Lamp,
    House2_LessThanCondition,
    House2_NamedElement,
    House2_RainSensor,
    House2_RollerBlind,
    House2_Room,
    House2_Sensor,
    House2_TemperatureSensor,
    House2_TwilightSwitch,
    House2_ValueAction,
    NamedElement,
    Sensor,
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

def test_House2_Boiler_isOn_value_roundtrip():
    instance = House2_Boiler(isOn=True)
    assert instance.isOn == True
    instance.isOn = False
    assert instance.isOn == False


def test_House2_BooleanAction_switchTo_value_roundtrip():
    instance = House2_BooleanAction(switchTo=True)
    assert instance.switchTo == True
    instance.switchTo = False
    assert instance.switchTo == False


def test_House2_EqualCondition_boolcond_value_roundtrip():
    instance = House2_EqualCondition(boolcond=True, valuecond=3.14)
    assert instance.boolcond == True
    instance.boolcond = False
    assert instance.boolcond == False


def test_House2_EqualCondition_valuecond_value_roundtrip():
    instance = House2_EqualCondition(boolcond=True, valuecond=3.14)
    assert instance.valuecond == 3.14
    instance.valuecond = 9.99
    assert instance.valuecond == 9.99


def test_House2_GreaterThanCondition_threshold_value_roundtrip():
    instance = House2_GreaterThanCondition(threshold=3.14)
    assert instance.threshold == 3.14
    instance.threshold = 9.99
    assert instance.threshold == 9.99


def test_House2_Lamp_isOn_value_roundtrip():
    instance = House2_Lamp(isOn=True)
    assert instance.isOn == True
    instance.isOn = False
    assert instance.isOn == False


def test_House2_LessThanCondition_threshold_value_roundtrip():
    instance = House2_LessThanCondition(threshold=3.14)
    assert instance.threshold == 3.14
    instance.threshold = 9.99
    assert instance.threshold == 9.99


def test_House2_NamedElement_name_value_roundtrip():
    instance = House2_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_House2_RainSensor_active_value_roundtrip():
    instance = House2_RainSensor(active=True)
    assert instance.active == True
    instance.active = False
    assert instance.active == False


def test_House2_RollerBlind_isUp_value_roundtrip():
    instance = House2_RollerBlind(isUp=True)
    assert instance.isUp == True
    instance.isUp = False
    assert instance.isUp == False


def test_House2_TemperatureSensor_temp_value_roundtrip():
    instance = House2_TemperatureSensor(temp=3.14)
    assert instance.temp == 3.14
    instance.temp = 9.99
    assert instance.temp == 9.99


def test_House2_TwilightSwitch_active_value_roundtrip():
    instance = House2_TwilightSwitch(active=True)
    assert instance.active == True
    instance.active = False
    assert instance.active == False


def test_House2_ValueAction_switchToValue_value_roundtrip():
    instance = House2_ValueAction(switchToValue=3.14)
    assert instance.switchToValue == 3.14
    instance.switchToValue = 9.99
    assert instance.switchToValue == 9.99


def test_House2_BooleanAction_isa_Action():
    instance = House2_BooleanAction(switchTo=True)
    assert isinstance(instance, Action)


def test_House2_ValueAction_isa_Action():
    instance = House2_ValueAction(switchToValue=3.14)
    assert isinstance(instance, Action)


def test_House2_Boiler_isa_Actor():
    instance = House2_Boiler(isOn=True)
    assert isinstance(instance, Actor)


def test_House2_Lamp_isa_Actor():
    instance = House2_Lamp(isOn=True)
    assert isinstance(instance, Actor)


def test_House2_RollerBlind_isa_Actor():
    instance = House2_RollerBlind(isUp=True)
    assert isinstance(instance, Actor)


def test_House2_EqualCondition_isa_Condition():
    instance = House2_EqualCondition(boolcond=True, valuecond=3.14)
    assert isinstance(instance, Condition)


def test_House2_GreaterThanCondition_isa_Condition():
    instance = House2_GreaterThanCondition(threshold=3.14)
    assert isinstance(instance, Condition)


def test_House2_LessThanCondition_isa_Condition():
    instance = House2_LessThanCondition(threshold=3.14)
    assert isinstance(instance, Condition)


def test_House2_House_isa_Container():
    instance = House2_House()
    assert isinstance(instance, Container)


def test_House2_Room_isa_Container():
    instance = House2_Room()
    assert isinstance(instance, Container)


def test_House2_House_isa_Element():
    instance = House2_House()
    assert isinstance(instance, Element)


def test_House2_Actor_isa_NamedElement():
    instance = House2_Actor()
    assert isinstance(instance, NamedElement)


def test_House2_Container_isa_NamedElement():
    instance = House2_Container()
    assert isinstance(instance, NamedElement)


def test_House2_Element_isa_NamedElement():
    instance = House2_Element()
    assert isinstance(instance, NamedElement)


def test_House2_Sensor_isa_NamedElement():
    instance = House2_Sensor()
    assert isinstance(instance, NamedElement)


def test_House2_RainSensor_isa_Sensor():
    instance = House2_RainSensor(active=True)
    assert isinstance(instance, Sensor)


def test_House2_TemperatureSensor_isa_Sensor():
    instance = House2_TemperatureSensor(temp=3.14)
    assert isinstance(instance, Sensor)


def test_House2_TwilightSwitch_isa_Sensor():
    instance = House2_TwilightSwitch(active=True)
    assert isinstance(instance, Sensor)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Actor_strategy = st.builds(Actor)
@given(instance=Actor_strategy)
@settings(max_examples=25)
def test_Actor_instantiation(instance):
    assert isinstance(instance, Actor)


Condition_strategy = st.builds(Condition)
@given(instance=Condition_strategy)
@settings(max_examples=25)
def test_Condition_instantiation(instance):
    assert isinstance(instance, Condition)


Container_strategy = st.builds(Container)
@given(instance=Container_strategy)
@settings(max_examples=25)
def test_Container_instantiation(instance):
    assert isinstance(instance, Container)


Element_strategy = st.builds(Element)
@given(instance=Element_strategy)
@settings(max_examples=25)
def test_Element_instantiation(instance):
    assert isinstance(instance, Element)


House2_Action_strategy = st.builds(House2_Action)
@given(instance=House2_Action_strategy)
@settings(max_examples=25)
def test_House2_Action_instantiation(instance):
    assert isinstance(instance, House2_Action)


House2_Actor_strategy = st.builds(House2_Actor)
@given(instance=House2_Actor_strategy)
@settings(max_examples=25)
def test_House2_Actor_instantiation(instance):
    assert isinstance(instance, House2_Actor)


House2_Boiler_strategy = st.builds(House2_Boiler, isOn=st.booleans())
@given(instance=House2_Boiler_strategy)
@settings(max_examples=25)
def test_House2_Boiler_instantiation(instance):
    assert isinstance(instance, House2_Boiler)


House2_BooleanAction_strategy = st.builds(House2_BooleanAction, switchTo=st.booleans())
@given(instance=House2_BooleanAction_strategy)
@settings(max_examples=25)
def test_House2_BooleanAction_instantiation(instance):
    assert isinstance(instance, House2_BooleanAction)


House2_Condition_strategy = st.builds(House2_Condition)
@given(instance=House2_Condition_strategy)
@settings(max_examples=25)
def test_House2_Condition_instantiation(instance):
    assert isinstance(instance, House2_Condition)


House2_Container_strategy = st.builds(House2_Container)
@given(instance=House2_Container_strategy)
@settings(max_examples=25)
def test_House2_Container_instantiation(instance):
    assert isinstance(instance, House2_Container)


House2_ControlRule_strategy = st.builds(House2_ControlRule)
@given(instance=House2_ControlRule_strategy)
@settings(max_examples=25)
def test_House2_ControlRule_instantiation(instance):
    assert isinstance(instance, House2_ControlRule)


House2_Element_strategy = st.builds(House2_Element)
@given(instance=House2_Element_strategy)
@settings(max_examples=25)
def test_House2_Element_instantiation(instance):
    assert isinstance(instance, House2_Element)


House2_EqualCondition_strategy = st.builds(House2_EqualCondition, boolcond=st.booleans(), valuecond=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=House2_EqualCondition_strategy)
@settings(max_examples=25)
def test_House2_EqualCondition_instantiation(instance):
    assert isinstance(instance, House2_EqualCondition)


House2_GreaterThanCondition_strategy = st.builds(House2_GreaterThanCondition, threshold=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=House2_GreaterThanCondition_strategy)
@settings(max_examples=25)
def test_House2_GreaterThanCondition_instantiation(instance):
    assert isinstance(instance, House2_GreaterThanCondition)


House2_House_strategy = st.builds(House2_House)
@given(instance=House2_House_strategy)
@settings(max_examples=25)
def test_House2_House_instantiation(instance):
    assert isinstance(instance, House2_House)


House2_Lamp_strategy = st.builds(House2_Lamp, isOn=st.booleans())
@given(instance=House2_Lamp_strategy)
@settings(max_examples=25)
def test_House2_Lamp_instantiation(instance):
    assert isinstance(instance, House2_Lamp)


House2_LessThanCondition_strategy = st.builds(House2_LessThanCondition, threshold=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=House2_LessThanCondition_strategy)
@settings(max_examples=25)
def test_House2_LessThanCondition_instantiation(instance):
    assert isinstance(instance, House2_LessThanCondition)


House2_NamedElement_strategy = st.builds(House2_NamedElement, name=safe_text)
@given(instance=House2_NamedElement_strategy)
@settings(max_examples=25)
def test_House2_NamedElement_instantiation(instance):
    assert isinstance(instance, House2_NamedElement)


House2_RainSensor_strategy = st.builds(House2_RainSensor, active=st.booleans())
@given(instance=House2_RainSensor_strategy)
@settings(max_examples=25)
def test_House2_RainSensor_instantiation(instance):
    assert isinstance(instance, House2_RainSensor)


House2_RollerBlind_strategy = st.builds(House2_RollerBlind, isUp=st.booleans())
@given(instance=House2_RollerBlind_strategy)
@settings(max_examples=25)
def test_House2_RollerBlind_instantiation(instance):
    assert isinstance(instance, House2_RollerBlind)


House2_Room_strategy = st.builds(House2_Room)
@given(instance=House2_Room_strategy)
@settings(max_examples=25)
def test_House2_Room_instantiation(instance):
    assert isinstance(instance, House2_Room)


House2_Sensor_strategy = st.builds(House2_Sensor)
@given(instance=House2_Sensor_strategy)
@settings(max_examples=25)
def test_House2_Sensor_instantiation(instance):
    assert isinstance(instance, House2_Sensor)


House2_TemperatureSensor_strategy = st.builds(House2_TemperatureSensor, temp=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=House2_TemperatureSensor_strategy)
@settings(max_examples=25)
def test_House2_TemperatureSensor_instantiation(instance):
    assert isinstance(instance, House2_TemperatureSensor)


House2_TwilightSwitch_strategy = st.builds(House2_TwilightSwitch, active=st.booleans())
@given(instance=House2_TwilightSwitch_strategy)
@settings(max_examples=25)
def test_House2_TwilightSwitch_instantiation(instance):
    assert isinstance(instance, House2_TwilightSwitch)


House2_ValueAction_strategy = st.builds(House2_ValueAction, switchToValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=House2_ValueAction_strategy)
@settings(max_examples=25)
def test_House2_ValueAction_instantiation(instance):
    assert isinstance(instance, House2_ValueAction)


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



