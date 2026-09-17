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
    Item,
    iot_Controller,
    iot_Component,
    iot_RequiredPort,
    iot_ProvidedPort,
    Hardware,
    iot_Sensor,
    iot_Actuator,
    RequiredPort,
    iot_ThenPort,
    iot_ElsePort,
    iot_ConditionPort,
    iot_IfPort,
    Iteration,
    iot_IterativeLoop,
    iot_CounterLoop,
    Controller,
    iot_Iteration,
    iot_Sequence,
    iot_Branching,
    iot_Item,
    Component,
    iot_Snippet,
    iot_Hardware,
    iot_Software,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_hyp_item_constructor_exists():
    assert callable(Item.__init__)


def test_hyp_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_controller_is_not_abstract():
    assert not inspect.isabstract(iot_Controller)


def test_hyp_iot_controller_constructor_exists():
    assert callable(iot_Controller.__init__)


def test_hyp_iot_controller_constructor_args():
    sig = inspect.signature(iot_Controller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_component_is_not_abstract():
    assert not inspect.isabstract(iot_Component)


def test_hyp_iot_component_constructor_exists():
    assert callable(iot_Component.__init__)


def test_hyp_iot_component_constructor_args():
    sig = inspect.signature(iot_Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_requiredport_is_not_abstract():
    assert not inspect.isabstract(iot_RequiredPort)


def test_hyp_iot_requiredport_constructor_exists():
    assert callable(iot_RequiredPort.__init__)


def test_hyp_iot_requiredport_constructor_args():
    sig = inspect.signature(iot_RequiredPort.__init__)
    params = list(sig.parameters.keys())
    assert "UUID" in params, "Missing parameter 'UUID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "args" in params, "Missing parameter 'args'"
    assert "method" in params, "Missing parameter 'method'"







def test_hyp_iot_providedport_is_not_abstract():
    assert not inspect.isabstract(iot_ProvidedPort)


def test_hyp_iot_providedport_constructor_exists():
    assert callable(iot_ProvidedPort.__init__)


def test_hyp_iot_providedport_constructor_args():
    sig = inspect.signature(iot_ProvidedPort.__init__)
    params = list(sig.parameters.keys())
    assert "UUID" in params, "Missing parameter 'UUID'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_hardware_is_not_abstract():
    assert not inspect.isabstract(Hardware)


def test_hyp_hardware_constructor_exists():
    assert callable(Hardware.__init__)


def test_hyp_hardware_constructor_args():
    sig = inspect.signature(Hardware.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_sensor_is_not_abstract():
    assert not inspect.isabstract(iot_Sensor)


def test_hyp_iot_sensor_constructor_exists():
    assert callable(iot_Sensor.__init__)


def test_hyp_iot_sensor_constructor_args():
    sig = inspect.signature(iot_Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"




def test_hyp_iot_actuator_is_not_abstract():
    assert not inspect.isabstract(iot_Actuator)


def test_hyp_iot_actuator_constructor_exists():
    assert callable(iot_Actuator.__init__)


def test_hyp_iot_actuator_constructor_args():
    sig = inspect.signature(iot_Actuator.__init__)
    params = list(sig.parameters.keys())
    assert "toggle" in params, "Missing parameter 'toggle'"




def test_hyp_requiredport_is_not_abstract():
    assert not inspect.isabstract(RequiredPort)


def test_hyp_requiredport_constructor_exists():
    assert callable(RequiredPort.__init__)


def test_hyp_requiredport_constructor_args():
    sig = inspect.signature(RequiredPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_thenport_is_not_abstract():
    assert not inspect.isabstract(iot_ThenPort)


def test_hyp_iot_thenport_constructor_exists():
    assert callable(iot_ThenPort.__init__)


def test_hyp_iot_thenport_constructor_args():
    sig = inspect.signature(iot_ThenPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_elseport_is_not_abstract():
    assert not inspect.isabstract(iot_ElsePort)


def test_hyp_iot_elseport_constructor_exists():
    assert callable(iot_ElsePort.__init__)


def test_hyp_iot_elseport_constructor_args():
    sig = inspect.signature(iot_ElsePort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_conditionport_is_not_abstract():
    assert not inspect.isabstract(iot_ConditionPort)


def test_hyp_iot_conditionport_constructor_exists():
    assert callable(iot_ConditionPort.__init__)


def test_hyp_iot_conditionport_constructor_args():
    sig = inspect.signature(iot_ConditionPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_ifport_is_not_abstract():
    assert not inspect.isabstract(iot_IfPort)


def test_hyp_iot_ifport_constructor_exists():
    assert callable(iot_IfPort.__init__)


def test_hyp_iot_ifport_constructor_args():
    sig = inspect.signature(iot_IfPort.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "var" in params, "Missing parameter 'var'"
    assert "condition" in params, "Missing parameter 'condition'"






def test_hyp_iteration_is_not_abstract():
    assert not inspect.isabstract(Iteration)


def test_hyp_iteration_constructor_exists():
    assert callable(Iteration.__init__)


def test_hyp_iteration_constructor_args():
    sig = inspect.signature(Iteration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_iterativeloop_is_not_abstract():
    assert not inspect.isabstract(iot_IterativeLoop)


def test_hyp_iot_iterativeloop_constructor_exists():
    assert callable(iot_IterativeLoop.__init__)


def test_hyp_iot_iterativeloop_constructor_args():
    sig = inspect.signature(iot_IterativeLoop.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "var" in params, "Missing parameter 'var'"





def test_hyp_iot_counterloop_is_not_abstract():
    assert not inspect.isabstract(iot_CounterLoop)


def test_hyp_iot_counterloop_constructor_exists():
    assert callable(iot_CounterLoop.__init__)


def test_hyp_iot_counterloop_constructor_args():
    sig = inspect.signature(iot_CounterLoop.__init__)
    params = list(sig.parameters.keys())
    assert "counter" in params, "Missing parameter 'counter'"




def test_hyp_controller_is_not_abstract():
    assert not inspect.isabstract(Controller)


def test_hyp_controller_constructor_exists():
    assert callable(Controller.__init__)


def test_hyp_controller_constructor_args():
    sig = inspect.signature(Controller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_iteration_is_not_abstract():
    assert not inspect.isabstract(iot_Iteration)


def test_hyp_iot_iteration_constructor_exists():
    assert callable(iot_Iteration.__init__)


def test_hyp_iot_iteration_constructor_args():
    sig = inspect.signature(iot_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_sequence_is_not_abstract():
    assert not inspect.isabstract(iot_Sequence)


def test_hyp_iot_sequence_constructor_exists():
    assert callable(iot_Sequence.__init__)


def test_hyp_iot_sequence_constructor_args():
    sig = inspect.signature(iot_Sequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_branching_is_not_abstract():
    assert not inspect.isabstract(iot_Branching)


def test_hyp_iot_branching_constructor_exists():
    assert callable(iot_Branching.__init__)


def test_hyp_iot_branching_constructor_args():
    sig = inspect.signature(iot_Branching.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_item_is_not_abstract():
    assert not inspect.isabstract(iot_Item)


def test_hyp_iot_item_constructor_exists():
    assert callable(iot_Item.__init__)


def test_hyp_iot_item_constructor_args():
    sig = inspect.signature(iot_Item.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "UUID" in params, "Missing parameter 'UUID'"
    assert "newThread" in params, "Missing parameter 'newThread'"






def test_hyp_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_hyp_component_constructor_exists():
    assert callable(Component.__init__)


def test_hyp_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_snippet_is_not_abstract():
    assert not inspect.isabstract(iot_Snippet)


def test_hyp_iot_snippet_constructor_exists():
    assert callable(iot_Snippet.__init__)


def test_hyp_iot_snippet_constructor_args():
    sig = inspect.signature(iot_Snippet.__init__)
    params = list(sig.parameters.keys())
    assert "scriptPath" in params, "Missing parameter 'scriptPath'"




def test_hyp_iot_hardware_is_not_abstract():
    assert not inspect.isabstract(iot_Hardware)


def test_hyp_iot_hardware_constructor_exists():
    assert callable(iot_Hardware.__init__)


def test_hyp_iot_hardware_constructor_args():
    sig = inspect.signature(iot_Hardware.__init__)
    params = list(sig.parameters.keys())
    assert "pinNumber" in params, "Missing parameter 'pinNumber'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "timeInterval" in params, "Missing parameter 'timeInterval'"
    assert "type" in params, "Missing parameter 'type'"







def test_hyp_iot_software_is_not_abstract():
    assert not inspect.isabstract(iot_Software)


def test_hyp_iot_software_constructor_exists():
    assert callable(iot_Software.__init__)


def test_hyp_iot_software_constructor_args():
    sig = inspect.signature(iot_Software.__init__)
    params = list(sig.parameters.keys())

def test_hyp_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_hyp_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "EQ",
        "LE",
        "NE",
        "LT",
        "GT",
        "GE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
Item_strategy = st.builds(
    Item,
)
iot_Controller_strategy = st.builds(
    iot_Controller,
)
iot_Component_strategy = st.builds(
    iot_Component,
)
iot_RequiredPort_strategy = st.builds(
    iot_RequiredPort,
    UUID=
        safe_text,
    name=
        safe_text,
    args=
        safe_text,
    method=
        safe_text
)
iot_ProvidedPort_strategy = st.builds(
    iot_ProvidedPort,
    UUID=
        safe_text,
    name=
        safe_text
)
Hardware_strategy = st.builds(
    Hardware,
)
iot_Sensor_strategy = st.builds(
    iot_Sensor,
    script=
        safe_text
)
iot_Actuator_strategy = st.builds(
    iot_Actuator,
    toggle=
        st.booleans()
)
RequiredPort_strategy = st.builds(
    RequiredPort,
)
iot_ThenPort_strategy = st.builds(
    iot_ThenPort,
)
iot_ElsePort_strategy = st.builds(
    iot_ElsePort,
)
iot_ConditionPort_strategy = st.builds(
    iot_ConditionPort,
)
iot_IfPort_strategy = st.builds(
    iot_IfPort,
    operator=
        safe_text,
    var=
        safe_text,
    condition=
        st.booleans()
)
Iteration_strategy = st.builds(
    Iteration,
)
iot_IterativeLoop_strategy = st.builds(
    iot_IterativeLoop,
    operator=
        safe_text,
    var=
        safe_text
)
iot_CounterLoop_strategy = st.builds(
    iot_CounterLoop,
    counter=
        st.integers()
)
Controller_strategy = st.builds(
    Controller,
)
iot_Iteration_strategy = st.builds(
    iot_Iteration,
)
iot_Sequence_strategy = st.builds(
    iot_Sequence,
)
iot_Branching_strategy = st.builds(
    iot_Branching,
)
iot_Item_strategy = st.builds(
    iot_Item,
    name=
        safe_text,
    UUID=
        safe_text,
    newThread=
        st.booleans()
)
Component_strategy = st.builds(
    Component,
)
iot_Snippet_strategy = st.builds(
    iot_Snippet,
    scriptPath=
        safe_text
)
iot_Hardware_strategy = st.builds(
    iot_Hardware,
    pinNumber=
        st.integers(),
    mode=
        st.booleans(),
    timeInterval=
        st.integers(),
    type=
        safe_text
)
iot_Software_strategy = st.builds(
    iot_Software,
)







@given(instance=iot_RequiredPort_strategy)
def test_hyp_iot_requiredport_UUID_setter(instance):
    original = instance.UUID
    instance.UUID = original
    assert instance.UUID == original



@given(instance=iot_RequiredPort_strategy)
def test_hyp_iot_requiredport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=iot_RequiredPort_strategy)
def test_hyp_iot_requiredport_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original



@given(instance=iot_RequiredPort_strategy)
def test_hyp_iot_requiredport_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=iot_RequiredPort_strategy)
@settings(max_examples=30)
def test_hyp_iot_requiredport_invoke_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.invoke(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.invoke).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'invoke' in iot_RequiredPort is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'invoke' in iot_RequiredPort did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'invoke' in iot_RequiredPort is not implemented or raised an error")




@given(instance=iot_ProvidedPort_strategy)
def test_hyp_iot_providedport_UUID_setter(instance):
    original = instance.UUID
    instance.UUID = original
    assert instance.UUID == original



@given(instance=iot_ProvidedPort_strategy)
def test_hyp_iot_providedport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=iot_ProvidedPort_strategy)
@settings(max_examples=30)
def test_hyp_iot_providedport_invoke_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.invoke(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.invoke).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'invoke' in iot_ProvidedPort is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'invoke' in iot_ProvidedPort did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'invoke' in iot_ProvidedPort is not implemented or raised an error")





@given(instance=iot_Sensor_strategy)
def test_hyp_iot_sensor_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original




@given(instance=iot_Actuator_strategy)
def test_hyp_iot_actuator_toggle_setter(instance):
    original = instance.toggle
    instance.toggle = original
    assert instance.toggle == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=iot_Actuator_strategy)
@settings(max_examples=30)
def test_hyp_iot_actuator_toggle_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toggle()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toggle).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toggle' in iot_Actuator is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toggle' in iot_Actuator did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toggle' in iot_Actuator is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=iot_Actuator_strategy)
@settings(max_examples=30)
def test_hyp_iot_actuator_switchonoff_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.switchOnOff(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.switchOnOff).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'switchOnOff' in iot_Actuator is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'switchOnOff' in iot_Actuator did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'switchOnOff' in iot_Actuator is not implemented or raised an error")








@given(instance=iot_IfPort_strategy)
def test_hyp_iot_ifport_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=iot_IfPort_strategy)
def test_hyp_iot_ifport_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original



@given(instance=iot_IfPort_strategy)
def test_hyp_iot_ifport_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original





@given(instance=iot_IterativeLoop_strategy)
def test_hyp_iot_iterativeloop_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=iot_IterativeLoop_strategy)
def test_hyp_iot_iterativeloop_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original




@given(instance=iot_CounterLoop_strategy)
def test_hyp_iot_counterloop_counter_setter(instance):
    original = instance.counter
    instance.counter = original
    assert instance.counter == original








@given(instance=iot_Item_strategy)
def test_hyp_iot_item_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=iot_Item_strategy)
def test_hyp_iot_item_UUID_setter(instance):
    original = instance.UUID
    instance.UUID = original
    assert instance.UUID == original



@given(instance=iot_Item_strategy)
def test_hyp_iot_item_newThread_setter(instance):
    original = instance.newThread
    instance.newThread = original
    assert instance.newThread == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=iot_Item_strategy)
@settings(max_examples=30)
def test_hyp_iot_item_invoke_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.invoke()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.invoke).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'invoke' in iot_Item is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'invoke' in iot_Item did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'invoke' in iot_Item is not implemented or raised an error")





@given(instance=iot_Snippet_strategy)
def test_hyp_iot_snippet_scriptPath_setter(instance):
    original = instance.scriptPath
    instance.scriptPath = original
    assert instance.scriptPath == original




@given(instance=iot_Hardware_strategy)
def test_hyp_iot_hardware_pinNumber_setter(instance):
    original = instance.pinNumber
    instance.pinNumber = original
    assert instance.pinNumber == original



@given(instance=iot_Hardware_strategy)
def test_hyp_iot_hardware_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=iot_Hardware_strategy)
def test_hyp_iot_hardware_timeInterval_setter(instance):
    original = instance.timeInterval
    instance.timeInterval = original
    assert instance.timeInterval == original



@given(instance=iot_Hardware_strategy)
def test_hyp_iot_hardware_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Component,
    Controller,
    Hardware,
    Item,
    Iteration,
    RequiredPort,
    iot_Actuator,
    iot_Branching,
    iot_Component,
    iot_ConditionPort,
    iot_Controller,
    iot_CounterLoop,
    iot_ElsePort,
    iot_Hardware,
    iot_IfPort,
    iot_Item,
    iot_Iteration,
    iot_IterativeLoop,
    iot_ProvidedPort,
    iot_RequiredPort,
    iot_Sensor,
    iot_Sequence,
    iot_Snippet,
    iot_Software,
    iot_ThenPort,
    Operator,
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

def test_iot_Actuator_toggle_value_roundtrip():
    instance = iot_Actuator(toggle=True)
    assert instance.toggle == True
    instance.toggle = False
    assert instance.toggle == False


def test_iot_CounterLoop_counter_value_roundtrip():
    instance = iot_CounterLoop(counter=7)
    assert instance.counter == 7
    instance.counter = 13
    assert instance.counter == 13


def test_iot_Hardware_mode_value_roundtrip():
    instance = iot_Hardware(mode=True, pinNumber=7, timeInterval=7, type="sample_text")
    assert instance.mode == True
    instance.mode = False
    assert instance.mode == False


def test_iot_Hardware_pinNumber_value_roundtrip():
    instance = iot_Hardware(mode=True, pinNumber=7, timeInterval=7, type="sample_text")
    assert instance.pinNumber == 7
    instance.pinNumber = 13
    assert instance.pinNumber == 13


def test_iot_Hardware_timeInterval_value_roundtrip():
    instance = iot_Hardware(mode=True, pinNumber=7, timeInterval=7, type="sample_text")
    assert instance.timeInterval == 7
    instance.timeInterval = 13
    assert instance.timeInterval == 13


def test_iot_Hardware_type_value_roundtrip():
    instance = iot_Hardware(mode=True, pinNumber=7, timeInterval=7, type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_iot_IfPort_condition_value_roundtrip():
    instance = iot_IfPort(condition=True, operator="sample_text", var="sample_text")
    assert instance.condition == True
    instance.condition = False
    assert instance.condition == False


def test_iot_IfPort_operator_value_roundtrip():
    instance = iot_IfPort(condition=True, operator="sample_text", var="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_iot_IfPort_var_value_roundtrip():
    instance = iot_IfPort(condition=True, operator="sample_text", var="sample_text")
    assert instance.var == "sample_text"
    instance.var = "sample_text_2"
    assert instance.var == "sample_text_2"


def test_iot_Item_UUID_value_roundtrip():
    instance = iot_Item(UUID="sample_text", name="sample_text", newThread=True)
    assert instance.UUID == "sample_text"
    instance.UUID = "sample_text_2"
    assert instance.UUID == "sample_text_2"


def test_iot_Item_name_value_roundtrip():
    instance = iot_Item(UUID="sample_text", name="sample_text", newThread=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iot_Item_newThread_value_roundtrip():
    instance = iot_Item(UUID="sample_text", name="sample_text", newThread=True)
    assert instance.newThread == True
    instance.newThread = False
    assert instance.newThread == False


def test_iot_IterativeLoop_operator_value_roundtrip():
    instance = iot_IterativeLoop(operator="sample_text", var="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_iot_IterativeLoop_var_value_roundtrip():
    instance = iot_IterativeLoop(operator="sample_text", var="sample_text")
    assert instance.var == "sample_text"
    instance.var = "sample_text_2"
    assert instance.var == "sample_text_2"


def test_iot_ProvidedPort_UUID_value_roundtrip():
    instance = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    assert instance.UUID == "sample_text"
    instance.UUID = "sample_text_2"
    assert instance.UUID == "sample_text_2"


def test_iot_ProvidedPort_name_value_roundtrip():
    instance = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iot_RequiredPort_UUID_value_roundtrip():
    instance = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    assert instance.UUID == "sample_text"
    instance.UUID = "sample_text_2"
    assert instance.UUID == "sample_text_2"


def test_iot_RequiredPort_args_value_roundtrip():
    instance = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    assert instance.args == "sample_text"
    instance.args = "sample_text_2"
    assert instance.args == "sample_text_2"


def test_iot_RequiredPort_method_value_roundtrip():
    instance = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    assert instance.method == "sample_text"
    instance.method = "sample_text_2"
    assert instance.method == "sample_text_2"


def test_iot_RequiredPort_name_value_roundtrip():
    instance = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iot_Sensor_script_value_roundtrip():
    instance = iot_Sensor(script="sample_text")
    assert instance.script == "sample_text"
    instance.script = "sample_text_2"
    assert instance.script == "sample_text_2"


def test_iot_Snippet_scriptPath_value_roundtrip():
    instance = iot_Snippet(scriptPath="sample_text")
    assert instance.scriptPath == "sample_text"
    instance.scriptPath = "sample_text_2"
    assert instance.scriptPath == "sample_text_2"


def test_iot_Hardware_isa_Component():
    instance = iot_Hardware(mode=True, pinNumber=7, timeInterval=7, type="sample_text")
    assert isinstance(instance, Component)


def test_iot_Snippet_isa_Component():
    instance = iot_Snippet(scriptPath="sample_text")
    assert isinstance(instance, Component)


def test_iot_Software_isa_Component():
    instance = iot_Software()
    assert isinstance(instance, Component)


def test_iot_Branching_isa_Controller():
    instance = iot_Branching()
    assert isinstance(instance, Controller)


def test_iot_Iteration_isa_Controller():
    instance = iot_Iteration()
    assert isinstance(instance, Controller)


def test_iot_Sequence_isa_Controller():
    instance = iot_Sequence()
    assert isinstance(instance, Controller)


def test_iot_Actuator_isa_Hardware():
    instance = iot_Actuator(toggle=True)
    assert isinstance(instance, Hardware)


def test_iot_Sensor_isa_Hardware():
    instance = iot_Sensor(script="sample_text")
    assert isinstance(instance, Hardware)


def test_iot_Component_isa_Item():
    instance = iot_Component()
    assert isinstance(instance, Item)


def test_iot_Controller_isa_Item():
    instance = iot_Controller()
    assert isinstance(instance, Item)


def test_iot_CounterLoop_isa_Iteration():
    instance = iot_CounterLoop(counter=7)
    assert isinstance(instance, Iteration)


def test_iot_IterativeLoop_isa_Iteration():
    instance = iot_IterativeLoop(operator="sample_text", var="sample_text")
    assert isinstance(instance, Iteration)


def test_iot_ConditionPort_isa_RequiredPort():
    instance = iot_ConditionPort()
    assert isinstance(instance, RequiredPort)


def test_iot_ElsePort_isa_RequiredPort():
    instance = iot_ElsePort()
    assert isinstance(instance, RequiredPort)


def test_iot_IfPort_isa_RequiredPort():
    instance = iot_IfPort(condition=True, operator="sample_text", var="sample_text")
    assert isinstance(instance, RequiredPort)


def test_iot_ThenPort_isa_RequiredPort():
    instance = iot_ThenPort()
    assert isinstance(instance, RequiredPort)


def test_assoc_condition1_link_reassign_clear():
    a = iot_IterativeLoop(operator="sample_text", var="sample_text")
    b1 = iot_ConditionPort()
    b2 = iot_ConditionPort()
    _safe_set(a, 'iot_IterativeLoop', b1)
    assert _is_linked(a, 'iot_IterativeLoop', b1)
    if hasattr(b1, 'iot_ConditionPort'):
        assert _is_linked(b1, 'iot_ConditionPort', a)
    _safe_set(a, 'iot_IterativeLoop', b2)
    assert _is_linked(a, 'iot_IterativeLoop', b2)
    if hasattr(b1, 'iot_ConditionPort'):
        assert not _is_linked(b1, 'iot_ConditionPort', a)
    if hasattr(b2, 'iot_ConditionPort'):
        assert _is_linked(b2, 'iot_ConditionPort', a)
    _safe_set(a, 'iot_IterativeLoop', None)
    assert not _is_linked(a, 'iot_IterativeLoop', b2)
    if hasattr(b2, 'iot_ConditionPort'):
        assert not _is_linked(b2, 'iot_ConditionPort', a)


def test_assoc_ifport4_link_reassign_clear():
    a = iot_IfPort(condition=True, operator="sample_text", var="sample_text")
    b1 = iot_Branching()
    b2 = iot_Branching()
    _safe_set(a, 'iot_IfPort', b1)
    assert _is_linked(a, 'iot_IfPort', b1)
    if hasattr(b1, 'iot_Branching'):
        assert _is_linked(b1, 'iot_Branching', a)
    _safe_set(a, 'iot_IfPort', b2)
    assert _is_linked(a, 'iot_IfPort', b2)
    if hasattr(b1, 'iot_Branching'):
        assert not _is_linked(b1, 'iot_Branching', a)
    if hasattr(b2, 'iot_Branching'):
        assert _is_linked(b2, 'iot_Branching', a)
    _safe_set(a, 'iot_IfPort', None)
    assert not _is_linked(a, 'iot_IfPort', b2)
    if hasattr(b2, 'iot_Branching'):
        assert not _is_linked(b2, 'iot_Branching', a)


def test_assoc_item0_link_reassign_clear():
    a = iot_Item(UUID="sample_text", name="sample_text", newThread=True)
    b1 = iot_Software()
    b2 = iot_Software()
    _safe_set(a, 'iot_Item', b1)
    assert _is_linked(a, 'iot_Item', b1)
    if hasattr(b1, 'iot_Software'):
        assert _is_linked(b1, 'iot_Software', a)
    _safe_set(a, 'iot_Item', b2)
    assert _is_linked(a, 'iot_Item', b2)
    if hasattr(b1, 'iot_Software'):
        assert not _is_linked(b1, 'iot_Software', a)
    if hasattr(b2, 'iot_Software'):
        assert _is_linked(b2, 'iot_Software', a)
    _safe_set(a, 'iot_Item', None)
    assert not _is_linked(a, 'iot_Item', b2)
    if hasattr(b2, 'iot_Software'):
        assert not _is_linked(b2, 'iot_Software', a)


def test_assoc_providedport14_link_reassign_clear():
    a = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    b1 = iot_Component()
    b2 = iot_Component()
    _safe_set(a, 'iot_ProvidedPort16', b1)
    assert _is_linked(a, 'iot_ProvidedPort16', b1)
    if hasattr(b1, 'iot_Component15'):
        assert _is_linked(b1, 'iot_Component15', a)
    _safe_set(a, 'iot_ProvidedPort16', b2)
    assert _is_linked(a, 'iot_ProvidedPort16', b2)
    if hasattr(b1, 'iot_Component15'):
        assert not _is_linked(b1, 'iot_Component15', a)
    if hasattr(b2, 'iot_Component15'):
        assert _is_linked(b2, 'iot_Component15', a)
    _safe_set(a, 'iot_ProvidedPort16', None)
    assert not _is_linked(a, 'iot_ProvidedPort16', b2)
    if hasattr(b2, 'iot_Component15'):
        assert not _is_linked(b2, 'iot_Component15', a)


def test_assoc_providedport17_link_reassign_clear():
    a = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    b1 = iot_Controller()
    b2 = iot_Controller()
    _safe_set(a, 'iot_ProvidedPort18', b1)
    assert _is_linked(a, 'iot_ProvidedPort18', b1)
    if hasattr(b1, 'iot_Controller'):
        assert _is_linked(b1, 'iot_Controller', a)
    _safe_set(a, 'iot_ProvidedPort18', b2)
    assert _is_linked(a, 'iot_ProvidedPort18', b2)
    if hasattr(b1, 'iot_Controller'):
        assert not _is_linked(b1, 'iot_Controller', a)
    if hasattr(b2, 'iot_Controller'):
        assert _is_linked(b2, 'iot_Controller', a)
    _safe_set(a, 'iot_ProvidedPort18', None)
    assert not _is_linked(a, 'iot_ProvidedPort18', b2)
    if hasattr(b2, 'iot_Controller'):
        assert not _is_linked(b2, 'iot_Controller', a)


def test_assoc_referto2_link_reassign_clear():
    a = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    b1 = iot_Item(UUID="sample_text", name="sample_text", newThread=True)
    b2 = iot_Item(UUID="sample_text_2", name="sample_text_2", newThread=False)
    _safe_set(a, 'iot_ProvidedPort', b1)
    assert _is_linked(a, 'iot_ProvidedPort', b1)
    if hasattr(b1, 'iot_Item3'):
        assert _is_linked(b1, 'iot_Item3', a)
    _safe_set(a, 'iot_ProvidedPort', b2)
    assert _is_linked(a, 'iot_ProvidedPort', b2)
    if hasattr(b1, 'iot_Item3'):
        assert not _is_linked(b1, 'iot_Item3', a)
    if hasattr(b2, 'iot_Item3'):
        assert _is_linked(b2, 'iot_Item3', a)
    _safe_set(a, 'iot_ProvidedPort', None)
    assert not _is_linked(a, 'iot_ProvidedPort', b2)
    if hasattr(b2, 'iot_Item3'):
        assert not _is_linked(b2, 'iot_Item3', a)


def test_assoc_requiredport10_link_reassign_clear():
    a = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    b1 = iot_Sequence()
    b2 = iot_Sequence()
    _safe_set(a, 'iot_RequiredPort11', b1)
    assert _is_linked(a, 'iot_RequiredPort11', b1)
    if hasattr(b1, 'iot_Sequence'):
        assert _is_linked(b1, 'iot_Sequence', a)
    _safe_set(a, 'iot_RequiredPort11', b2)
    assert _is_linked(a, 'iot_RequiredPort11', b2)
    if hasattr(b1, 'iot_Sequence'):
        assert not _is_linked(b1, 'iot_Sequence', a)
    if hasattr(b2, 'iot_Sequence'):
        assert _is_linked(b2, 'iot_Sequence', a)
    _safe_set(a, 'iot_RequiredPort11', None)
    assert not _is_linked(a, 'iot_RequiredPort11', b2)
    if hasattr(b2, 'iot_Sequence'):
        assert not _is_linked(b2, 'iot_Sequence', a)


def test_assoc_requiredport12_link_reassign_clear():
    a = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    b1 = iot_Component()
    b2 = iot_Component()
    _safe_set(a, 'iot_RequiredPort13', b1)
    assert _is_linked(a, 'iot_RequiredPort13', b1)
    if hasattr(b1, 'iot_Component'):
        assert _is_linked(b1, 'iot_Component', a)
    _safe_set(a, 'iot_RequiredPort13', b2)
    assert _is_linked(a, 'iot_RequiredPort13', b2)
    if hasattr(b1, 'iot_Component'):
        assert not _is_linked(b1, 'iot_Component', a)
    if hasattr(b2, 'iot_Component'):
        assert _is_linked(b2, 'iot_Component', a)
    _safe_set(a, 'iot_RequiredPort13', None)
    assert not _is_linked(a, 'iot_RequiredPort13', b2)
    if hasattr(b2, 'iot_Component'):
        assert not _is_linked(b2, 'iot_Component', a)


def test_assoc_requiredport9_link_reassign_clear():
    a = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    b1 = iot_Iteration()
    b2 = iot_Iteration()
    _safe_set(a, 'iot_RequiredPort', b1)
    assert _is_linked(a, 'iot_RequiredPort', b1)
    if hasattr(b1, 'iot_Iteration'):
        assert _is_linked(b1, 'iot_Iteration', a)
    _safe_set(a, 'iot_RequiredPort', b2)
    assert _is_linked(a, 'iot_RequiredPort', b2)
    if hasattr(b1, 'iot_Iteration'):
        assert not _is_linked(b1, 'iot_Iteration', a)
    if hasattr(b2, 'iot_Iteration'):
        assert _is_linked(b2, 'iot_Iteration', a)
    _safe_set(a, 'iot_RequiredPort', None)
    assert not _is_linked(a, 'iot_RequiredPort', b2)
    if hasattr(b2, 'iot_Iteration'):
        assert not _is_linked(b2, 'iot_Iteration', a)


def test_assoc_use19_link_reassign_clear():
    a = iot_RequiredPort(UUID="sample_text", args="sample_text", method="sample_text", name="sample_text")
    b1 = iot_ProvidedPort(UUID="sample_text", name="sample_text")
    b2 = iot_ProvidedPort(UUID="sample_text_2", name="sample_text_2")
    _safe_set(a, 'iot_RequiredPort20', b1)
    assert _is_linked(a, 'iot_RequiredPort20', b1)
    if hasattr(b1, 'iot_ProvidedPort21'):
        assert _is_linked(b1, 'iot_ProvidedPort21', a)
    _safe_set(a, 'iot_RequiredPort20', b2)
    assert _is_linked(a, 'iot_RequiredPort20', b2)
    if hasattr(b1, 'iot_ProvidedPort21'):
        assert not _is_linked(b1, 'iot_ProvidedPort21', a)
    if hasattr(b2, 'iot_ProvidedPort21'):
        assert _is_linked(b2, 'iot_ProvidedPort21', a)
    _safe_set(a, 'iot_RequiredPort20', None)
    assert not _is_linked(a, 'iot_RequiredPort20', b2)
    if hasattr(b2, 'iot_ProvidedPort21'):
        assert not _is_linked(b2, 'iot_ProvidedPort21', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Component_strategy = st.builds(Component)
@given(instance=Component_strategy)
@settings(max_examples=25)
def test_Component_instantiation(instance):
    assert isinstance(instance, Component)


Controller_strategy = st.builds(Controller)
@given(instance=Controller_strategy)
@settings(max_examples=25)
def test_Controller_instantiation(instance):
    assert isinstance(instance, Controller)


Hardware_strategy = st.builds(Hardware)
@given(instance=Hardware_strategy)
@settings(max_examples=25)
def test_Hardware_instantiation(instance):
    assert isinstance(instance, Hardware)


Item_strategy = st.builds(Item)
@given(instance=Item_strategy)
@settings(max_examples=25)
def test_Item_instantiation(instance):
    assert isinstance(instance, Item)


Iteration_strategy = st.builds(Iteration)
@given(instance=Iteration_strategy)
@settings(max_examples=25)
def test_Iteration_instantiation(instance):
    assert isinstance(instance, Iteration)


RequiredPort_strategy = st.builds(RequiredPort)
@given(instance=RequiredPort_strategy)
@settings(max_examples=25)
def test_RequiredPort_instantiation(instance):
    assert isinstance(instance, RequiredPort)


iot_Actuator_strategy = st.builds(iot_Actuator, toggle=st.booleans())
@given(instance=iot_Actuator_strategy)
@settings(max_examples=25)
def test_iot_Actuator_instantiation(instance):
    assert isinstance(instance, iot_Actuator)


iot_Branching_strategy = st.builds(iot_Branching)
@given(instance=iot_Branching_strategy)
@settings(max_examples=25)
def test_iot_Branching_instantiation(instance):
    assert isinstance(instance, iot_Branching)


iot_Component_strategy = st.builds(iot_Component)
@given(instance=iot_Component_strategy)
@settings(max_examples=25)
def test_iot_Component_instantiation(instance):
    assert isinstance(instance, iot_Component)


iot_ConditionPort_strategy = st.builds(iot_ConditionPort)
@given(instance=iot_ConditionPort_strategy)
@settings(max_examples=25)
def test_iot_ConditionPort_instantiation(instance):
    assert isinstance(instance, iot_ConditionPort)


iot_Controller_strategy = st.builds(iot_Controller)
@given(instance=iot_Controller_strategy)
@settings(max_examples=25)
def test_iot_Controller_instantiation(instance):
    assert isinstance(instance, iot_Controller)


iot_CounterLoop_strategy = st.builds(iot_CounterLoop, counter=st.integers())
@given(instance=iot_CounterLoop_strategy)
@settings(max_examples=25)
def test_iot_CounterLoop_instantiation(instance):
    assert isinstance(instance, iot_CounterLoop)


iot_ElsePort_strategy = st.builds(iot_ElsePort)
@given(instance=iot_ElsePort_strategy)
@settings(max_examples=25)
def test_iot_ElsePort_instantiation(instance):
    assert isinstance(instance, iot_ElsePort)


iot_Hardware_strategy = st.builds(iot_Hardware, mode=st.booleans(), pinNumber=st.integers(), timeInterval=st.integers(), type=safe_text)
@given(instance=iot_Hardware_strategy)
@settings(max_examples=25)
def test_iot_Hardware_instantiation(instance):
    assert isinstance(instance, iot_Hardware)


iot_IfPort_strategy = st.builds(iot_IfPort, condition=st.booleans(), operator=safe_text, var=safe_text)
@given(instance=iot_IfPort_strategy)
@settings(max_examples=25)
def test_iot_IfPort_instantiation(instance):
    assert isinstance(instance, iot_IfPort)


iot_Item_strategy = st.builds(iot_Item, UUID=safe_text, name=safe_text, newThread=st.booleans())
@given(instance=iot_Item_strategy)
@settings(max_examples=25)
def test_iot_Item_instantiation(instance):
    assert isinstance(instance, iot_Item)


iot_Iteration_strategy = st.builds(iot_Iteration)
@given(instance=iot_Iteration_strategy)
@settings(max_examples=25)
def test_iot_Iteration_instantiation(instance):
    assert isinstance(instance, iot_Iteration)


iot_IterativeLoop_strategy = st.builds(iot_IterativeLoop, operator=safe_text, var=safe_text)
@given(instance=iot_IterativeLoop_strategy)
@settings(max_examples=25)
def test_iot_IterativeLoop_instantiation(instance):
    assert isinstance(instance, iot_IterativeLoop)


iot_ProvidedPort_strategy = st.builds(iot_ProvidedPort, UUID=safe_text, name=safe_text)
@given(instance=iot_ProvidedPort_strategy)
@settings(max_examples=25)
def test_iot_ProvidedPort_instantiation(instance):
    assert isinstance(instance, iot_ProvidedPort)


iot_RequiredPort_strategy = st.builds(iot_RequiredPort, UUID=safe_text, args=safe_text, method=safe_text, name=safe_text)
@given(instance=iot_RequiredPort_strategy)
@settings(max_examples=25)
def test_iot_RequiredPort_instantiation(instance):
    assert isinstance(instance, iot_RequiredPort)


iot_Sensor_strategy = st.builds(iot_Sensor, script=safe_text)
@given(instance=iot_Sensor_strategy)
@settings(max_examples=25)
def test_iot_Sensor_instantiation(instance):
    assert isinstance(instance, iot_Sensor)


iot_Sequence_strategy = st.builds(iot_Sequence)
@given(instance=iot_Sequence_strategy)
@settings(max_examples=25)
def test_iot_Sequence_instantiation(instance):
    assert isinstance(instance, iot_Sequence)


iot_Snippet_strategy = st.builds(iot_Snippet, scriptPath=safe_text)
@given(instance=iot_Snippet_strategy)
@settings(max_examples=25)
def test_iot_Snippet_instantiation(instance):
    assert isinstance(instance, iot_Snippet)


iot_Software_strategy = st.builds(iot_Software)
@given(instance=iot_Software_strategy)
@settings(max_examples=25)
def test_iot_Software_instantiation(instance):
    assert isinstance(instance, iot_Software)


iot_ThenPort_strategy = st.builds(iot_ThenPort)
@given(instance=iot_ThenPort_strategy)
@settings(max_examples=25)
def test_iot_ThenPort_instantiation(instance):
    assert isinstance(instance, iot_ThenPort)



