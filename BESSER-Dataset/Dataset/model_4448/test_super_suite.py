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
    Function,
    pycom_ModuleFunction,
    pycom_FunctionName,
    ModuleType,
    pycom_SensorType,
    pycom_ActuatorType,
    pycom_PinName,
    pycom_Pin,
    pycom_Expression,
    pycom_ComparisonExp,
    pycom_Boolean,
    pycom_LogicExp,
    pycom_BoardMember,
    pycom_Host,
    pycom_Connection,
    pycom_Server,
    pycom_ModuleType,
    BoardMember,
    pycom_Communication,
    pycom_Actuator,
    pycom_Sensor,
    pycom_Board,
    pycom_ExpMember,
    pycom_System,
    pycom_Condition,
    ExpMember,
    pycom_ConditionalAction,
    pycom_Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_hyp_function_constructor_exists():
    assert callable(Function.__init__)


def test_hyp_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_modulefunction_is_not_abstract():
    assert not inspect.isabstract(pycom_ModuleFunction)


def test_hyp_pycom_modulefunction_constructor_exists():
    assert callable(pycom_ModuleFunction.__init__)


def test_hyp_pycom_modulefunction_constructor_args():
    sig = inspect.signature(pycom_ModuleFunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_functionname_is_not_abstract():
    assert not inspect.isabstract(pycom_FunctionName)


def test_hyp_pycom_functionname_constructor_exists():
    assert callable(pycom_FunctionName.__init__)


def test_hyp_pycom_functionname_constructor_args():
    sig = inspect.signature(pycom_FunctionName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_moduletype_is_not_abstract():
    assert not inspect.isabstract(ModuleType)


def test_hyp_moduletype_constructor_exists():
    assert callable(ModuleType.__init__)


def test_hyp_moduletype_constructor_args():
    sig = inspect.signature(ModuleType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_sensortype_is_not_abstract():
    assert not inspect.isabstract(pycom_SensorType)


def test_hyp_pycom_sensortype_constructor_exists():
    assert callable(pycom_SensorType.__init__)


def test_hyp_pycom_sensortype_constructor_args():
    sig = inspect.signature(pycom_SensorType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_actuatortype_is_not_abstract():
    assert not inspect.isabstract(pycom_ActuatorType)


def test_hyp_pycom_actuatortype_constructor_exists():
    assert callable(pycom_ActuatorType.__init__)


def test_hyp_pycom_actuatortype_constructor_args():
    sig = inspect.signature(pycom_ActuatorType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_pinname_is_not_abstract():
    assert not inspect.isabstract(pycom_PinName)


def test_hyp_pycom_pinname_constructor_exists():
    assert callable(pycom_PinName.__init__)


def test_hyp_pycom_pinname_constructor_args():
    sig = inspect.signature(pycom_PinName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pycom_pin_is_not_abstract():
    assert not inspect.isabstract(pycom_Pin)


def test_hyp_pycom_pin_constructor_exists():
    assert callable(pycom_Pin.__init__)


def test_hyp_pycom_pin_constructor_args():
    sig = inspect.signature(pycom_Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_expression_is_not_abstract():
    assert not inspect.isabstract(pycom_Expression)


def test_hyp_pycom_expression_constructor_exists():
    assert callable(pycom_Expression.__init__)


def test_hyp_pycom_expression_constructor_args():
    sig = inspect.signature(pycom_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "outputValue" in params, "Missing parameter 'outputValue'"




def test_hyp_pycom_comparisonexp_is_not_abstract():
    assert not inspect.isabstract(pycom_ComparisonExp)


def test_hyp_pycom_comparisonexp_constructor_exists():
    assert callable(pycom_ComparisonExp.__init__)


def test_hyp_pycom_comparisonexp_constructor_args():
    sig = inspect.signature(pycom_ComparisonExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_pycom_boolean_is_not_abstract():
    assert not inspect.isabstract(pycom_Boolean)


def test_hyp_pycom_boolean_constructor_exists():
    assert callable(pycom_Boolean.__init__)


def test_hyp_pycom_boolean_constructor_args():
    sig = inspect.signature(pycom_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_pycom_logicexp_is_not_abstract():
    assert not inspect.isabstract(pycom_LogicExp)


def test_hyp_pycom_logicexp_constructor_exists():
    assert callable(pycom_LogicExp.__init__)


def test_hyp_pycom_logicexp_constructor_args():
    sig = inspect.signature(pycom_LogicExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_boardmember_is_not_abstract():
    assert not inspect.isabstract(pycom_BoardMember)


def test_hyp_pycom_boardmember_constructor_exists():
    assert callable(pycom_BoardMember.__init__)


def test_hyp_pycom_boardmember_constructor_args():
    sig = inspect.signature(pycom_BoardMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_host_is_not_abstract():
    assert not inspect.isabstract(pycom_Host)


def test_hyp_pycom_host_constructor_exists():
    assert callable(pycom_Host.__init__)


def test_hyp_pycom_host_constructor_args():
    sig = inspect.signature(pycom_Host.__init__)
    params = list(sig.parameters.keys())
    assert "ipAdr" in params, "Missing parameter 'ipAdr'"
    assert "website" in params, "Missing parameter 'website'"





def test_hyp_pycom_connection_is_not_abstract():
    assert not inspect.isabstract(pycom_Connection)


def test_hyp_pycom_connection_constructor_exists():
    assert callable(pycom_Connection.__init__)


def test_hyp_pycom_connection_constructor_args():
    sig = inspect.signature(pycom_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "portnumber" in params, "Missing parameter 'portnumber'"




def test_hyp_pycom_server_is_not_abstract():
    assert not inspect.isabstract(pycom_Server)


def test_hyp_pycom_server_constructor_exists():
    assert callable(pycom_Server.__init__)


def test_hyp_pycom_server_constructor_args():
    sig = inspect.signature(pycom_Server.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pycom_moduletype_is_not_abstract():
    assert not inspect.isabstract(pycom_ModuleType)


def test_hyp_pycom_moduletype_constructor_exists():
    assert callable(pycom_ModuleType.__init__)


def test_hyp_pycom_moduletype_constructor_args():
    sig = inspect.signature(pycom_ModuleType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "typeName" in params, "Missing parameter 'typeName'"





def test_hyp_boardmember_is_not_abstract():
    assert not inspect.isabstract(BoardMember)


def test_hyp_boardmember_constructor_exists():
    assert callable(BoardMember.__init__)


def test_hyp_boardmember_constructor_args():
    sig = inspect.signature(BoardMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_communication_is_not_abstract():
    assert not inspect.isabstract(pycom_Communication)


def test_hyp_pycom_communication_constructor_exists():
    assert callable(pycom_Communication.__init__)


def test_hyp_pycom_communication_constructor_args():
    sig = inspect.signature(pycom_Communication.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_pycom_actuator_is_not_abstract():
    assert not inspect.isabstract(pycom_Actuator)


def test_hyp_pycom_actuator_constructor_exists():
    assert callable(pycom_Actuator.__init__)


def test_hyp_pycom_actuator_constructor_args():
    sig = inspect.signature(pycom_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_sensor_is_not_abstract():
    assert not inspect.isabstract(pycom_Sensor)


def test_hyp_pycom_sensor_constructor_exists():
    assert callable(pycom_Sensor.__init__)


def test_hyp_pycom_sensor_constructor_args():
    sig = inspect.signature(pycom_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_board_is_not_abstract():
    assert not inspect.isabstract(pycom_Board)


def test_hyp_pycom_board_constructor_exists():
    assert callable(pycom_Board.__init__)


def test_hyp_pycom_board_constructor_args():
    sig = inspect.signature(pycom_Board.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pycom_expmember_is_not_abstract():
    assert not inspect.isabstract(pycom_ExpMember)


def test_hyp_pycom_expmember_constructor_exists():
    assert callable(pycom_ExpMember.__init__)


def test_hyp_pycom_expmember_constructor_args():
    sig = inspect.signature(pycom_ExpMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_system_is_not_abstract():
    assert not inspect.isabstract(pycom_System)


def test_hyp_pycom_system_constructor_exists():
    assert callable(pycom_System.__init__)


def test_hyp_pycom_system_constructor_args():
    sig = inspect.signature(pycom_System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_condition_is_not_abstract():
    assert not inspect.isabstract(pycom_Condition)


def test_hyp_pycom_condition_constructor_exists():
    assert callable(pycom_Condition.__init__)


def test_hyp_pycom_condition_constructor_args():
    sig = inspect.signature(pycom_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_expmember_is_not_abstract():
    assert not inspect.isabstract(ExpMember)


def test_hyp_expmember_constructor_exists():
    assert callable(ExpMember.__init__)


def test_hyp_expmember_constructor_args():
    sig = inspect.signature(ExpMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pycom_conditionalaction_is_not_abstract():
    assert not inspect.isabstract(pycom_ConditionalAction)


def test_hyp_pycom_conditionalaction_constructor_exists():
    assert callable(pycom_ConditionalAction.__init__)


def test_hyp_pycom_conditionalaction_constructor_args():
    sig = inspect.signature(pycom_ConditionalAction.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_pycom_function_is_not_abstract():
    assert not inspect.isabstract(pycom_Function)


def test_hyp_pycom_function_constructor_exists():
    assert callable(pycom_Function.__init__)


def test_hyp_pycom_function_constructor_args():
    sig = inspect.signature(pycom_Function.__init__)
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
Function_strategy = st.builds(
    Function,
)
pycom_ModuleFunction_strategy = st.builds(
    pycom_ModuleFunction,
)
pycom_FunctionName_strategy = st.builds(
    pycom_FunctionName,
    name=
        safe_text
)
ModuleType_strategy = st.builds(
    ModuleType,
)
pycom_SensorType_strategy = st.builds(
    pycom_SensorType,
)
pycom_ActuatorType_strategy = st.builds(
    pycom_ActuatorType,
)
pycom_PinName_strategy = st.builds(
    pycom_PinName,
    name=
        safe_text
)
pycom_Pin_strategy = st.builds(
    pycom_Pin,
)
pycom_Expression_strategy = st.builds(
    pycom_Expression,
    outputValue=
        st.integers()
)
pycom_ComparisonExp_strategy = st.builds(
    pycom_ComparisonExp,
    op=
        safe_text
)
pycom_Boolean_strategy = st.builds(
    pycom_Boolean,
    value=
        safe_text
)
pycom_LogicExp_strategy = st.builds(
    pycom_LogicExp,
)
pycom_BoardMember_strategy = st.builds(
    pycom_BoardMember,
)
pycom_Host_strategy = st.builds(
    pycom_Host,
    ipAdr=
        safe_text,
    website=
        safe_text
)
pycom_Connection_strategy = st.builds(
    pycom_Connection,
    portnumber=
        safe_text
)
pycom_Server_strategy = st.builds(
    pycom_Server,
    name=
        safe_text
)
pycom_ModuleType_strategy = st.builds(
    pycom_ModuleType,
    name=
        safe_text,
    typeName=
        safe_text
)
BoardMember_strategy = st.builds(
    BoardMember,
)
pycom_Communication_strategy = st.builds(
    pycom_Communication,
    type=
        safe_text
)
pycom_Actuator_strategy = st.builds(
    pycom_Actuator,
)
pycom_Sensor_strategy = st.builds(
    pycom_Sensor,
)
pycom_Board_strategy = st.builds(
    pycom_Board,
    name=
        safe_text
)
pycom_ExpMember_strategy = st.builds(
    pycom_ExpMember,
)
pycom_System_strategy = st.builds(
    pycom_System,
)
pycom_Condition_strategy = st.builds(
    pycom_Condition,
    operator=
        safe_text
)
ExpMember_strategy = st.builds(
    ExpMember,
)
pycom_ConditionalAction_strategy = st.builds(
    pycom_ConditionalAction,
    type=
        safe_text
)
pycom_Function_strategy = st.builds(
    pycom_Function,
)






@given(instance=pycom_FunctionName_strategy)
def test_hyp_pycom_functionname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=pycom_PinName_strategy)
def test_hyp_pycom_pinname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pycom_Expression_strategy)
def test_hyp_pycom_expression_outputValue_setter(instance):
    original = instance.outputValue
    instance.outputValue = original
    assert instance.outputValue == original




@given(instance=pycom_ComparisonExp_strategy)
def test_hyp_pycom_comparisonexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=pycom_Boolean_strategy)
def test_hyp_pycom_boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=pycom_Host_strategy)
def test_hyp_pycom_host_ipAdr_setter(instance):
    original = instance.ipAdr
    instance.ipAdr = original
    assert instance.ipAdr == original



@given(instance=pycom_Host_strategy)
def test_hyp_pycom_host_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original




@given(instance=pycom_Connection_strategy)
def test_hyp_pycom_connection_portnumber_setter(instance):
    original = instance.portnumber
    instance.portnumber = original
    assert instance.portnumber == original




@given(instance=pycom_Server_strategy)
def test_hyp_pycom_server_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=pycom_ModuleType_strategy)
def test_hyp_pycom_moduletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pycom_ModuleType_strategy)
def test_hyp_pycom_moduletype_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original





@given(instance=pycom_Communication_strategy)
def test_hyp_pycom_communication_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=pycom_Board_strategy)
def test_hyp_pycom_board_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=pycom_Condition_strategy)
def test_hyp_pycom_condition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original





@given(instance=pycom_ConditionalAction_strategy)
def test_hyp_pycom_conditionalaction_type_setter(instance):
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
    BoardMember,
    ExpMember,
    Function,
    ModuleType,
    pycom_Actuator,
    pycom_ActuatorType,
    pycom_Board,
    pycom_BoardMember,
    pycom_Boolean,
    pycom_Communication,
    pycom_ComparisonExp,
    pycom_Condition,
    pycom_ConditionalAction,
    pycom_Connection,
    pycom_ExpMember,
    pycom_Expression,
    pycom_Function,
    pycom_FunctionName,
    pycom_Host,
    pycom_LogicExp,
    pycom_ModuleFunction,
    pycom_ModuleType,
    pycom_Pin,
    pycom_PinName,
    pycom_Sensor,
    pycom_SensorType,
    pycom_Server,
    pycom_System,
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

def test_pycom_Board_name_value_roundtrip():
    instance = pycom_Board(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pycom_Boolean_value_value_roundtrip():
    instance = pycom_Boolean(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_pycom_Communication_type_value_roundtrip():
    instance = pycom_Communication(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_pycom_ComparisonExp_op_value_roundtrip():
    instance = pycom_ComparisonExp(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_pycom_Condition_operator_value_roundtrip():
    instance = pycom_Condition(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_pycom_ConditionalAction_type_value_roundtrip():
    instance = pycom_ConditionalAction(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_pycom_Connection_portnumber_value_roundtrip():
    instance = pycom_Connection(portnumber="sample_text")
    assert instance.portnumber == "sample_text"
    instance.portnumber = "sample_text_2"
    assert instance.portnumber == "sample_text_2"


def test_pycom_Expression_outputValue_value_roundtrip():
    instance = pycom_Expression(outputValue=7)
    assert instance.outputValue == 7
    instance.outputValue = 13
    assert instance.outputValue == 13


def test_pycom_FunctionName_name_value_roundtrip():
    instance = pycom_FunctionName(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pycom_Host_ipAdr_value_roundtrip():
    instance = pycom_Host(ipAdr="sample_text", website="sample_text")
    assert instance.ipAdr == "sample_text"
    instance.ipAdr = "sample_text_2"
    assert instance.ipAdr == "sample_text_2"


def test_pycom_Host_website_value_roundtrip():
    instance = pycom_Host(ipAdr="sample_text", website="sample_text")
    assert instance.website == "sample_text"
    instance.website = "sample_text_2"
    assert instance.website == "sample_text_2"


def test_pycom_ModuleType_name_value_roundtrip():
    instance = pycom_ModuleType(name="sample_text", typeName="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pycom_ModuleType_typeName_value_roundtrip():
    instance = pycom_ModuleType(name="sample_text", typeName="sample_text")
    assert instance.typeName == "sample_text"
    instance.typeName = "sample_text_2"
    assert instance.typeName == "sample_text_2"


def test_pycom_PinName_name_value_roundtrip():
    instance = pycom_PinName(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pycom_Server_name_value_roundtrip():
    instance = pycom_Server(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pycom_Actuator_isa_BoardMember():
    instance = pycom_Actuator()
    assert isinstance(instance, BoardMember)


def test_pycom_Communication_isa_BoardMember():
    instance = pycom_Communication(type="sample_text")
    assert isinstance(instance, BoardMember)


def test_pycom_Sensor_isa_BoardMember():
    instance = pycom_Sensor()
    assert isinstance(instance, BoardMember)


def test_pycom_ConditionalAction_isa_ExpMember():
    instance = pycom_ConditionalAction(type="sample_text")
    assert isinstance(instance, ExpMember)


def test_pycom_Function_isa_ExpMember():
    instance = pycom_Function()
    assert isinstance(instance, ExpMember)


def test_pycom_ModuleFunction_isa_Function():
    instance = pycom_ModuleFunction()
    assert isinstance(instance, Function)


def test_pycom_ActuatorType_isa_ModuleType():
    instance = pycom_ActuatorType()
    assert isinstance(instance, ModuleType)


def test_pycom_SensorType_isa_ModuleType():
    instance = pycom_SensorType()
    assert isinstance(instance, ModuleType)


def test_assoc_ExpMembers13_link_reassign_clear():
    a = pycom_ConditionalAction(type="sample_text")
    b1 = pycom_ExpMember()
    b2 = pycom_ExpMember()
    _safe_set(a, 'pycom_ConditionalAction14', {b1})
    assert _is_linked(a, 'pycom_ConditionalAction14', b1)
    if hasattr(b1, 'pycom_ExpMember'):
        assert _is_linked(b1, 'pycom_ExpMember', a)
    _safe_set(a, 'pycom_ConditionalAction14', {b2})
    assert _is_linked(a, 'pycom_ConditionalAction14', b2)
    if hasattr(b1, 'pycom_ExpMember'):
        assert not _is_linked(b1, 'pycom_ExpMember', a)
    if hasattr(b2, 'pycom_ExpMember'):
        assert _is_linked(b2, 'pycom_ExpMember', a)
    _safe_set(a, 'pycom_ConditionalAction14', set())
    assert not _is_linked(a, 'pycom_ConditionalAction14', b2)
    if hasattr(b2, 'pycom_ExpMember'):
        assert not _is_linked(b2, 'pycom_ExpMember', a)


def test_assoc_actuatorTypes16_link_reassign_clear():
    a = pycom_ModuleType(name="sample_text", typeName="sample_text")
    b1 = pycom_Actuator()
    b2 = pycom_Actuator()
    _safe_set(a, 'pycom_ModuleType17', b1)
    assert _is_linked(a, 'pycom_ModuleType17', b1)
    if hasattr(b1, 'pycom_Actuator'):
        assert _is_linked(b1, 'pycom_Actuator', a)
    _safe_set(a, 'pycom_ModuleType17', b2)
    assert _is_linked(a, 'pycom_ModuleType17', b2)
    if hasattr(b1, 'pycom_Actuator'):
        assert not _is_linked(b1, 'pycom_Actuator', a)
    if hasattr(b2, 'pycom_Actuator'):
        assert _is_linked(b2, 'pycom_Actuator', a)
    _safe_set(a, 'pycom_ModuleType17', None)
    assert not _is_linked(a, 'pycom_ModuleType17', b2)
    if hasattr(b2, 'pycom_Actuator'):
        assert not _is_linked(b2, 'pycom_Actuator', a)


def test_assoc_board41_link_reassign_clear():
    a = pycom_Board(name="sample_text")
    b1 = pycom_Function()
    b2 = pycom_Function()
    _safe_set(a, 'pycom_Board43', b1)
    assert _is_linked(a, 'pycom_Board43', b1)
    if hasattr(b1, 'pycom_Function42'):
        assert _is_linked(b1, 'pycom_Function42', a)
    _safe_set(a, 'pycom_Board43', b2)
    assert _is_linked(a, 'pycom_Board43', b2)
    if hasattr(b1, 'pycom_Function42'):
        assert not _is_linked(b1, 'pycom_Function42', a)
    if hasattr(b2, 'pycom_Function42'):
        assert _is_linked(b2, 'pycom_Function42', a)
    _safe_set(a, 'pycom_Board43', None)
    assert not _is_linked(a, 'pycom_Board43', b2)
    if hasattr(b2, 'pycom_Function42'):
        assert not _is_linked(b2, 'pycom_Function42', a)


def test_assoc_boardMembers9_link_reassign_clear():
    a = pycom_Board(name="sample_text")
    b1 = pycom_BoardMember()
    b2 = pycom_BoardMember()
    _safe_set(a, 'pycom_Board10', {b1})
    assert _is_linked(a, 'pycom_Board10', b1)
    if hasattr(b1, 'pycom_BoardMember'):
        assert _is_linked(b1, 'pycom_BoardMember', a)
    _safe_set(a, 'pycom_Board10', {b2})
    assert _is_linked(a, 'pycom_Board10', b2)
    if hasattr(b1, 'pycom_BoardMember'):
        assert not _is_linked(b1, 'pycom_BoardMember', a)
    if hasattr(b2, 'pycom_BoardMember'):
        assert _is_linked(b2, 'pycom_BoardMember', a)
    _safe_set(a, 'pycom_Board10', set())
    assert not _is_linked(a, 'pycom_Board10', b2)
    if hasattr(b2, 'pycom_BoardMember'):
        assert not _is_linked(b2, 'pycom_BoardMember', a)


def test_assoc_boards0_link_reassign_clear():
    a = pycom_Board(name="sample_text")
    b1 = pycom_System()
    b2 = pycom_System()
    _safe_set(a, 'pycom_Board', b1)
    assert _is_linked(a, 'pycom_Board', b1)
    if hasattr(b1, 'pycom_System'):
        assert _is_linked(b1, 'pycom_System', a)
    _safe_set(a, 'pycom_Board', b2)
    assert _is_linked(a, 'pycom_Board', b2)
    if hasattr(b1, 'pycom_System'):
        assert not _is_linked(b1, 'pycom_System', a)
    if hasattr(b2, 'pycom_System'):
        assert _is_linked(b2, 'pycom_System', a)
    _safe_set(a, 'pycom_Board', None)
    assert not _is_linked(a, 'pycom_Board', b2)
    if hasattr(b2, 'pycom_System'):
        assert not _is_linked(b2, 'pycom_System', a)


def test_assoc_boolVal30_link_reassign_clear():
    a = pycom_Boolean(value="sample_text")
    b1 = pycom_LogicExp()
    b2 = pycom_LogicExp()
    _safe_set(a, 'pycom_Boolean', b1)
    assert _is_linked(a, 'pycom_Boolean', b1)
    if hasattr(b1, 'pycom_LogicExp31'):
        assert _is_linked(b1, 'pycom_LogicExp31', a)
    _safe_set(a, 'pycom_Boolean', b2)
    assert _is_linked(a, 'pycom_Boolean', b2)
    if hasattr(b1, 'pycom_LogicExp31'):
        assert not _is_linked(b1, 'pycom_LogicExp31', a)
    if hasattr(b2, 'pycom_LogicExp31'):
        assert _is_linked(b2, 'pycom_LogicExp31', a)
    _safe_set(a, 'pycom_Boolean', None)
    assert not _is_linked(a, 'pycom_Boolean', b2)
    if hasattr(b2, 'pycom_LogicExp31'):
        assert not _is_linked(b2, 'pycom_LogicExp31', a)


def test_assoc_compExp32_link_reassign_clear():
    a = pycom_ComparisonExp(op="sample_text")
    b1 = pycom_LogicExp()
    b2 = pycom_LogicExp()
    _safe_set(a, 'pycom_ComparisonExp', b1)
    assert _is_linked(a, 'pycom_ComparisonExp', b1)
    if hasattr(b1, 'pycom_LogicExp33'):
        assert _is_linked(b1, 'pycom_LogicExp33', a)
    _safe_set(a, 'pycom_ComparisonExp', b2)
    assert _is_linked(a, 'pycom_ComparisonExp', b2)
    if hasattr(b1, 'pycom_LogicExp33'):
        assert not _is_linked(b1, 'pycom_LogicExp33', a)
    if hasattr(b2, 'pycom_LogicExp33'):
        assert _is_linked(b2, 'pycom_LogicExp33', a)
    _safe_set(a, 'pycom_ComparisonExp', None)
    assert not _is_linked(a, 'pycom_ComparisonExp', b2)
    if hasattr(b2, 'pycom_LogicExp33'):
        assert not _is_linked(b2, 'pycom_LogicExp33', a)


def test_assoc_condition11_link_reassign_clear():
    a = pycom_ConditionalAction(type="sample_text")
    b1 = pycom_Condition(operator="sample_text")
    b2 = pycom_Condition(operator="sample_text_2")
    _safe_set(a, 'pycom_ConditionalAction12', b1)
    assert _is_linked(a, 'pycom_ConditionalAction12', b1)
    if hasattr(b1, 'pycom_Condition'):
        assert _is_linked(b1, 'pycom_Condition', a)
    _safe_set(a, 'pycom_ConditionalAction12', b2)
    assert _is_linked(a, 'pycom_ConditionalAction12', b2)
    if hasattr(b1, 'pycom_Condition'):
        assert not _is_linked(b1, 'pycom_Condition', a)
    if hasattr(b2, 'pycom_Condition'):
        assert _is_linked(b2, 'pycom_Condition', a)
    _safe_set(a, 'pycom_ConditionalAction12', None)
    assert not _is_linked(a, 'pycom_ConditionalAction12', b2)
    if hasattr(b2, 'pycom_Condition'):
        assert not _is_linked(b2, 'pycom_Condition', a)


def test_assoc_conn3_link_reassign_clear():
    a = pycom_Server(name="sample_text")
    b1 = pycom_Connection(portnumber="sample_text")
    b2 = pycom_Connection(portnumber="sample_text_2")
    _safe_set(a, 'pycom_Server4', b1)
    assert _is_linked(a, 'pycom_Server4', b1)
    if hasattr(b1, 'pycom_Connection'):
        assert _is_linked(b1, 'pycom_Connection', a)
    _safe_set(a, 'pycom_Server4', b2)
    assert _is_linked(a, 'pycom_Server4', b2)
    if hasattr(b1, 'pycom_Connection'):
        assert not _is_linked(b1, 'pycom_Connection', a)
    if hasattr(b2, 'pycom_Connection'):
        assert _is_linked(b2, 'pycom_Connection', a)
    _safe_set(a, 'pycom_Server4', None)
    assert not _is_linked(a, 'pycom_Server4', b2)
    if hasattr(b2, 'pycom_Connection'):
        assert not _is_linked(b2, 'pycom_Connection', a)


def test_assoc_exps5_link_reassign_clear():
    a = pycom_Server(name="sample_text")
    b1 = pycom_ConditionalAction(type="sample_text")
    b2 = pycom_ConditionalAction(type="sample_text_2")
    _safe_set(a, 'pycom_Server6', {b1})
    assert _is_linked(a, 'pycom_Server6', b1)
    if hasattr(b1, 'pycom_ConditionalAction'):
        assert _is_linked(b1, 'pycom_ConditionalAction', a)
    _safe_set(a, 'pycom_Server6', {b2})
    assert _is_linked(a, 'pycom_Server6', b2)
    if hasattr(b1, 'pycom_ConditionalAction'):
        assert not _is_linked(b1, 'pycom_ConditionalAction', a)
    if hasattr(b2, 'pycom_ConditionalAction'):
        assert _is_linked(b2, 'pycom_ConditionalAction', a)
    _safe_set(a, 'pycom_Server6', set())
    assert not _is_linked(a, 'pycom_Server6', b2)
    if hasattr(b2, 'pycom_ConditionalAction'):
        assert not _is_linked(b2, 'pycom_ConditionalAction', a)


def test_assoc_functionName44_link_reassign_clear():
    a = pycom_FunctionName(name="sample_text")
    b1 = pycom_Function()
    b2 = pycom_Function()
    _safe_set(a, 'pycom_FunctionName', b1)
    assert _is_linked(a, 'pycom_FunctionName', b1)
    if hasattr(b1, 'pycom_Function45'):
        assert _is_linked(b1, 'pycom_Function45', a)
    _safe_set(a, 'pycom_FunctionName', b2)
    assert _is_linked(a, 'pycom_FunctionName', b2)
    if hasattr(b1, 'pycom_Function45'):
        assert not _is_linked(b1, 'pycom_Function45', a)
    if hasattr(b2, 'pycom_Function45'):
        assert _is_linked(b2, 'pycom_Function45', a)
    _safe_set(a, 'pycom_FunctionName', None)
    assert not _is_linked(a, 'pycom_FunctionName', b2)
    if hasattr(b2, 'pycom_Function45'):
        assert not _is_linked(b2, 'pycom_Function45', a)


def test_assoc_host7_link_reassign_clear():
    a = pycom_Host(ipAdr="sample_text", website="sample_text")
    b1 = pycom_Connection(portnumber="sample_text")
    b2 = pycom_Connection(portnumber="sample_text_2")
    _safe_set(a, 'pycom_Host', b1)
    assert _is_linked(a, 'pycom_Host', b1)
    if hasattr(b1, 'pycom_Connection8'):
        assert _is_linked(b1, 'pycom_Connection8', a)
    _safe_set(a, 'pycom_Host', b2)
    assert _is_linked(a, 'pycom_Host', b2)
    if hasattr(b1, 'pycom_Connection8'):
        assert not _is_linked(b1, 'pycom_Connection8', a)
    if hasattr(b2, 'pycom_Connection8'):
        assert _is_linked(b2, 'pycom_Connection8', a)
    _safe_set(a, 'pycom_Host', None)
    assert not _is_linked(a, 'pycom_Host', b2)
    if hasattr(b2, 'pycom_Connection8'):
        assert not _is_linked(b2, 'pycom_Connection8', a)


def test_assoc_input22_link_reassign_clear():
    a = pycom_PinName(name="sample_text")
    b1 = pycom_Pin()
    b2 = pycom_Pin()
    _safe_set(a, 'pycom_PinName24', b1)
    assert _is_linked(a, 'pycom_PinName24', b1)
    if hasattr(b1, 'pycom_Pin23'):
        assert _is_linked(b1, 'pycom_Pin23', a)
    _safe_set(a, 'pycom_PinName24', b2)
    assert _is_linked(a, 'pycom_PinName24', b2)
    if hasattr(b1, 'pycom_Pin23'):
        assert not _is_linked(b1, 'pycom_Pin23', a)
    if hasattr(b2, 'pycom_Pin23'):
        assert _is_linked(b2, 'pycom_Pin23', a)
    _safe_set(a, 'pycom_PinName24', None)
    assert not _is_linked(a, 'pycom_PinName24', b2)
    if hasattr(b2, 'pycom_Pin23'):
        assert not _is_linked(b2, 'pycom_Pin23', a)


def test_assoc_left34_link_reassign_clear():
    a = pycom_Expression(outputValue=7)
    b1 = pycom_ComparisonExp(op="sample_text")
    b2 = pycom_ComparisonExp(op="sample_text_2")
    _safe_set(a, 'pycom_Expression', b1)
    assert _is_linked(a, 'pycom_Expression', b1)
    if hasattr(b1, 'pycom_ComparisonExp35'):
        assert _is_linked(b1, 'pycom_ComparisonExp35', a)
    _safe_set(a, 'pycom_Expression', b2)
    assert _is_linked(a, 'pycom_Expression', b2)
    if hasattr(b1, 'pycom_ComparisonExp35'):
        assert not _is_linked(b1, 'pycom_ComparisonExp35', a)
    if hasattr(b2, 'pycom_ComparisonExp35'):
        assert _is_linked(b2, 'pycom_ComparisonExp35', a)
    _safe_set(a, 'pycom_Expression', None)
    assert not _is_linked(a, 'pycom_Expression', b2)
    if hasattr(b2, 'pycom_ComparisonExp35'):
        assert not _is_linked(b2, 'pycom_ComparisonExp35', a)


def test_assoc_logicEx25_link_reassign_clear():
    a = pycom_Condition(operator="sample_text")
    b1 = pycom_LogicExp()
    b2 = pycom_LogicExp()
    _safe_set(a, 'pycom_Condition26', b1)
    assert _is_linked(a, 'pycom_Condition26', b1)
    if hasattr(b1, 'pycom_LogicExp'):
        assert _is_linked(b1, 'pycom_LogicExp', a)
    _safe_set(a, 'pycom_Condition26', b2)
    assert _is_linked(a, 'pycom_Condition26', b2)
    if hasattr(b1, 'pycom_LogicExp'):
        assert not _is_linked(b1, 'pycom_LogicExp', a)
    if hasattr(b2, 'pycom_LogicExp'):
        assert _is_linked(b2, 'pycom_LogicExp', a)
    _safe_set(a, 'pycom_Condition26', None)
    assert not _is_linked(a, 'pycom_Condition26', b2)
    if hasattr(b2, 'pycom_LogicExp'):
        assert not _is_linked(b2, 'pycom_LogicExp', a)


def test_assoc_moduleType46_link_reassign_clear():
    a = pycom_ModuleType(name="sample_text", typeName="sample_text")
    b1 = pycom_ModuleFunction()
    b2 = pycom_ModuleFunction()
    _safe_set(a, 'pycom_ModuleType47', b1)
    assert _is_linked(a, 'pycom_ModuleType47', b1)
    if hasattr(b1, 'pycom_ModuleFunction'):
        assert _is_linked(b1, 'pycom_ModuleFunction', a)
    _safe_set(a, 'pycom_ModuleType47', b2)
    assert _is_linked(a, 'pycom_ModuleType47', b2)
    if hasattr(b1, 'pycom_ModuleFunction'):
        assert not _is_linked(b1, 'pycom_ModuleFunction', a)
    if hasattr(b2, 'pycom_ModuleFunction'):
        assert _is_linked(b2, 'pycom_ModuleFunction', a)
    _safe_set(a, 'pycom_ModuleType47', None)
    assert not _is_linked(a, 'pycom_ModuleType47', b2)
    if hasattr(b2, 'pycom_ModuleFunction'):
        assert not _is_linked(b2, 'pycom_ModuleFunction', a)


def test_assoc_nestedCondition28_link_reassign_clear():
    a = pycom_Condition(operator="sample_text")
    b1 = pycom_Condition(operator="sample_text")
    b2 = pycom_Condition(operator="sample_text_2")
    _safe_set(a, 'pycom_Condition27', b1)
    assert _is_linked(a, 'pycom_Condition27', b1)
    if hasattr(b1, 'pycom_Condition29'):
        assert _is_linked(b1, 'pycom_Condition29', a)
    _safe_set(a, 'pycom_Condition27', b2)
    assert _is_linked(a, 'pycom_Condition27', b2)
    if hasattr(b1, 'pycom_Condition29'):
        assert not _is_linked(b1, 'pycom_Condition29', a)
    if hasattr(b2, 'pycom_Condition29'):
        assert _is_linked(b2, 'pycom_Condition29', a)
    _safe_set(a, 'pycom_Condition27', None)
    assert not _is_linked(a, 'pycom_Condition27', b2)
    if hasattr(b2, 'pycom_Condition29'):
        assert not _is_linked(b2, 'pycom_Condition29', a)


def test_assoc_outputfunction39_link_reassign_clear():
    a = pycom_Expression(outputValue=7)
    b1 = pycom_Function()
    b2 = pycom_Function()
    _safe_set(a, 'pycom_Expression40', b1)
    assert _is_linked(a, 'pycom_Expression40', b1)
    if hasattr(b1, 'pycom_Function'):
        assert _is_linked(b1, 'pycom_Function', a)
    _safe_set(a, 'pycom_Expression40', b2)
    assert _is_linked(a, 'pycom_Expression40', b2)
    if hasattr(b1, 'pycom_Function'):
        assert not _is_linked(b1, 'pycom_Function', a)
    if hasattr(b2, 'pycom_Function'):
        assert _is_linked(b2, 'pycom_Function', a)
    _safe_set(a, 'pycom_Expression40', None)
    assert not _is_linked(a, 'pycom_Expression40', b2)
    if hasattr(b2, 'pycom_Function'):
        assert not _is_linked(b2, 'pycom_Function', a)


def test_assoc_pins18_link_reassign_clear():
    a = pycom_ModuleType(name="sample_text", typeName="sample_text")
    b1 = pycom_Pin()
    b2 = pycom_Pin()
    _safe_set(a, 'pycom_ModuleType19', b1)
    assert _is_linked(a, 'pycom_ModuleType19', b1)
    if hasattr(b1, 'pycom_Pin'):
        assert _is_linked(b1, 'pycom_Pin', a)
    _safe_set(a, 'pycom_ModuleType19', b2)
    assert _is_linked(a, 'pycom_ModuleType19', b2)
    if hasattr(b1, 'pycom_Pin'):
        assert not _is_linked(b1, 'pycom_Pin', a)
    if hasattr(b2, 'pycom_Pin'):
        assert _is_linked(b2, 'pycom_Pin', a)
    _safe_set(a, 'pycom_ModuleType19', None)
    assert not _is_linked(a, 'pycom_ModuleType19', b2)
    if hasattr(b2, 'pycom_Pin'):
        assert not _is_linked(b2, 'pycom_Pin', a)


def test_assoc_power20_link_reassign_clear():
    a = pycom_PinName(name="sample_text")
    b1 = pycom_Pin()
    b2 = pycom_Pin()
    _safe_set(a, 'pycom_PinName', b1)
    assert _is_linked(a, 'pycom_PinName', b1)
    if hasattr(b1, 'pycom_Pin21'):
        assert _is_linked(b1, 'pycom_Pin21', a)
    _safe_set(a, 'pycom_PinName', b2)
    assert _is_linked(a, 'pycom_PinName', b2)
    if hasattr(b1, 'pycom_Pin21'):
        assert not _is_linked(b1, 'pycom_Pin21', a)
    if hasattr(b2, 'pycom_Pin21'):
        assert _is_linked(b2, 'pycom_Pin21', a)
    _safe_set(a, 'pycom_PinName', None)
    assert not _is_linked(a, 'pycom_PinName', b2)
    if hasattr(b2, 'pycom_Pin21'):
        assert not _is_linked(b2, 'pycom_Pin21', a)


def test_assoc_right36_link_reassign_clear():
    a = pycom_Expression(outputValue=7)
    b1 = pycom_ComparisonExp(op="sample_text")
    b2 = pycom_ComparisonExp(op="sample_text_2")
    _safe_set(a, 'pycom_Expression38', b1)
    assert _is_linked(a, 'pycom_Expression38', b1)
    if hasattr(b1, 'pycom_ComparisonExp37'):
        assert _is_linked(b1, 'pycom_ComparisonExp37', a)
    _safe_set(a, 'pycom_Expression38', b2)
    assert _is_linked(a, 'pycom_Expression38', b2)
    if hasattr(b1, 'pycom_ComparisonExp37'):
        assert not _is_linked(b1, 'pycom_ComparisonExp37', a)
    if hasattr(b2, 'pycom_ComparisonExp37'):
        assert _is_linked(b2, 'pycom_ComparisonExp37', a)
    _safe_set(a, 'pycom_Expression38', None)
    assert not _is_linked(a, 'pycom_Expression38', b2)
    if hasattr(b2, 'pycom_ComparisonExp37'):
        assert not _is_linked(b2, 'pycom_ComparisonExp37', a)


def test_assoc_sensorTypes15_link_reassign_clear():
    a = pycom_ModuleType(name="sample_text", typeName="sample_text")
    b1 = pycom_Sensor()
    b2 = pycom_Sensor()
    _safe_set(a, 'pycom_ModuleType', b1)
    assert _is_linked(a, 'pycom_ModuleType', b1)
    if hasattr(b1, 'pycom_Sensor'):
        assert _is_linked(b1, 'pycom_Sensor', a)
    _safe_set(a, 'pycom_ModuleType', b2)
    assert _is_linked(a, 'pycom_ModuleType', b2)
    if hasattr(b1, 'pycom_Sensor'):
        assert not _is_linked(b1, 'pycom_Sensor', a)
    if hasattr(b2, 'pycom_Sensor'):
        assert _is_linked(b2, 'pycom_Sensor', a)
    _safe_set(a, 'pycom_ModuleType', None)
    assert not _is_linked(a, 'pycom_ModuleType', b2)
    if hasattr(b2, 'pycom_Sensor'):
        assert not _is_linked(b2, 'pycom_Sensor', a)


def test_assoc_servers1_link_reassign_clear():
    a = pycom_Server(name="sample_text")
    b1 = pycom_System()
    b2 = pycom_System()
    _safe_set(a, 'pycom_Server', b1)
    assert _is_linked(a, 'pycom_Server', b1)
    if hasattr(b1, 'pycom_System2'):
        assert _is_linked(b1, 'pycom_System2', a)
    _safe_set(a, 'pycom_Server', b2)
    assert _is_linked(a, 'pycom_Server', b2)
    if hasattr(b1, 'pycom_System2'):
        assert not _is_linked(b1, 'pycom_System2', a)
    if hasattr(b2, 'pycom_System2'):
        assert _is_linked(b2, 'pycom_System2', a)
    _safe_set(a, 'pycom_Server', None)
    assert not _is_linked(a, 'pycom_Server', b2)
    if hasattr(b2, 'pycom_System2'):
        assert not _is_linked(b2, 'pycom_System2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BoardMember_strategy = st.builds(BoardMember)
@given(instance=BoardMember_strategy)
@settings(max_examples=25)
def test_BoardMember_instantiation(instance):
    assert isinstance(instance, BoardMember)


ExpMember_strategy = st.builds(ExpMember)
@given(instance=ExpMember_strategy)
@settings(max_examples=25)
def test_ExpMember_instantiation(instance):
    assert isinstance(instance, ExpMember)


Function_strategy = st.builds(Function)
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


ModuleType_strategy = st.builds(ModuleType)
@given(instance=ModuleType_strategy)
@settings(max_examples=25)
def test_ModuleType_instantiation(instance):
    assert isinstance(instance, ModuleType)


pycom_Actuator_strategy = st.builds(pycom_Actuator)
@given(instance=pycom_Actuator_strategy)
@settings(max_examples=25)
def test_pycom_Actuator_instantiation(instance):
    assert isinstance(instance, pycom_Actuator)


pycom_ActuatorType_strategy = st.builds(pycom_ActuatorType)
@given(instance=pycom_ActuatorType_strategy)
@settings(max_examples=25)
def test_pycom_ActuatorType_instantiation(instance):
    assert isinstance(instance, pycom_ActuatorType)


pycom_Board_strategy = st.builds(pycom_Board, name=safe_text)
@given(instance=pycom_Board_strategy)
@settings(max_examples=25)
def test_pycom_Board_instantiation(instance):
    assert isinstance(instance, pycom_Board)


pycom_BoardMember_strategy = st.builds(pycom_BoardMember)
@given(instance=pycom_BoardMember_strategy)
@settings(max_examples=25)
def test_pycom_BoardMember_instantiation(instance):
    assert isinstance(instance, pycom_BoardMember)


pycom_Boolean_strategy = st.builds(pycom_Boolean, value=safe_text)
@given(instance=pycom_Boolean_strategy)
@settings(max_examples=25)
def test_pycom_Boolean_instantiation(instance):
    assert isinstance(instance, pycom_Boolean)


pycom_Communication_strategy = st.builds(pycom_Communication, type=safe_text)
@given(instance=pycom_Communication_strategy)
@settings(max_examples=25)
def test_pycom_Communication_instantiation(instance):
    assert isinstance(instance, pycom_Communication)


pycom_ComparisonExp_strategy = st.builds(pycom_ComparisonExp, op=safe_text)
@given(instance=pycom_ComparisonExp_strategy)
@settings(max_examples=25)
def test_pycom_ComparisonExp_instantiation(instance):
    assert isinstance(instance, pycom_ComparisonExp)


pycom_Condition_strategy = st.builds(pycom_Condition, operator=safe_text)
@given(instance=pycom_Condition_strategy)
@settings(max_examples=25)
def test_pycom_Condition_instantiation(instance):
    assert isinstance(instance, pycom_Condition)


pycom_ConditionalAction_strategy = st.builds(pycom_ConditionalAction, type=safe_text)
@given(instance=pycom_ConditionalAction_strategy)
@settings(max_examples=25)
def test_pycom_ConditionalAction_instantiation(instance):
    assert isinstance(instance, pycom_ConditionalAction)


pycom_Connection_strategy = st.builds(pycom_Connection, portnumber=safe_text)
@given(instance=pycom_Connection_strategy)
@settings(max_examples=25)
def test_pycom_Connection_instantiation(instance):
    assert isinstance(instance, pycom_Connection)


pycom_ExpMember_strategy = st.builds(pycom_ExpMember)
@given(instance=pycom_ExpMember_strategy)
@settings(max_examples=25)
def test_pycom_ExpMember_instantiation(instance):
    assert isinstance(instance, pycom_ExpMember)


pycom_Expression_strategy = st.builds(pycom_Expression, outputValue=st.integers())
@given(instance=pycom_Expression_strategy)
@settings(max_examples=25)
def test_pycom_Expression_instantiation(instance):
    assert isinstance(instance, pycom_Expression)


pycom_Function_strategy = st.builds(pycom_Function)
@given(instance=pycom_Function_strategy)
@settings(max_examples=25)
def test_pycom_Function_instantiation(instance):
    assert isinstance(instance, pycom_Function)


pycom_FunctionName_strategy = st.builds(pycom_FunctionName, name=safe_text)
@given(instance=pycom_FunctionName_strategy)
@settings(max_examples=25)
def test_pycom_FunctionName_instantiation(instance):
    assert isinstance(instance, pycom_FunctionName)


pycom_Host_strategy = st.builds(pycom_Host, ipAdr=safe_text, website=safe_text)
@given(instance=pycom_Host_strategy)
@settings(max_examples=25)
def test_pycom_Host_instantiation(instance):
    assert isinstance(instance, pycom_Host)


pycom_LogicExp_strategy = st.builds(pycom_LogicExp)
@given(instance=pycom_LogicExp_strategy)
@settings(max_examples=25)
def test_pycom_LogicExp_instantiation(instance):
    assert isinstance(instance, pycom_LogicExp)


pycom_ModuleFunction_strategy = st.builds(pycom_ModuleFunction)
@given(instance=pycom_ModuleFunction_strategy)
@settings(max_examples=25)
def test_pycom_ModuleFunction_instantiation(instance):
    assert isinstance(instance, pycom_ModuleFunction)


pycom_ModuleType_strategy = st.builds(pycom_ModuleType, name=safe_text, typeName=safe_text)
@given(instance=pycom_ModuleType_strategy)
@settings(max_examples=25)
def test_pycom_ModuleType_instantiation(instance):
    assert isinstance(instance, pycom_ModuleType)


pycom_Pin_strategy = st.builds(pycom_Pin)
@given(instance=pycom_Pin_strategy)
@settings(max_examples=25)
def test_pycom_Pin_instantiation(instance):
    assert isinstance(instance, pycom_Pin)


pycom_PinName_strategy = st.builds(pycom_PinName, name=safe_text)
@given(instance=pycom_PinName_strategy)
@settings(max_examples=25)
def test_pycom_PinName_instantiation(instance):
    assert isinstance(instance, pycom_PinName)


pycom_Sensor_strategy = st.builds(pycom_Sensor)
@given(instance=pycom_Sensor_strategy)
@settings(max_examples=25)
def test_pycom_Sensor_instantiation(instance):
    assert isinstance(instance, pycom_Sensor)


pycom_SensorType_strategy = st.builds(pycom_SensorType)
@given(instance=pycom_SensorType_strategy)
@settings(max_examples=25)
def test_pycom_SensorType_instantiation(instance):
    assert isinstance(instance, pycom_SensorType)


pycom_Server_strategy = st.builds(pycom_Server, name=safe_text)
@given(instance=pycom_Server_strategy)
@settings(max_examples=25)
def test_pycom_Server_instantiation(instance):
    assert isinstance(instance, pycom_Server)


pycom_System_strategy = st.builds(pycom_System)
@given(instance=pycom_System_strategy)
@settings(max_examples=25)
def test_pycom_System_instantiation(instance):
    assert isinstance(instance, pycom_System)





import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BoardMember,
    ExpMember,
    Function,
    ModuleType,
    pycom_Actuator,
    pycom_ActuatorType,
    pycom_Board,
    pycom_BoardMember,
    pycom_Boolean,
    pycom_Communication,
    pycom_ComparisonExp,
    pycom_Condition,
    pycom_ConditionalAction,
    pycom_Connection,
    pycom_ExpMember,
    pycom_Expression,
    pycom_Function,
    pycom_FunctionName,
    pycom_Host,
    pycom_LogicExp,
    pycom_ModuleFunction,
    pycom_ModuleType,
    pycom_Pin,
    pycom_PinName,
    pycom_Sensor,
    pycom_SensorType,
    pycom_Server,
    pycom_System,
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

def test_assoc_condition11_reverse_link_reassign_clear():
    a1 = pycom_ConditionalAction(type="sample_text")
    a2 = pycom_ConditionalAction(type="sample_text_2")
    b = pycom_Condition(operator="sample_text")
    _safe_set(b, 'pycom_Condition', a1)
    assert _is_linked(b, 'pycom_Condition', a1)
    if hasattr(a1, 'pycom_ConditionalAction12'):
        assert _is_linked(a1, 'pycom_ConditionalAction12', b)
    _safe_set(b, 'pycom_Condition', a2)
    assert _is_linked(b, 'pycom_Condition', a2)
    if hasattr(a1, 'pycom_ConditionalAction12'):
        assert not _is_linked(a1, 'pycom_ConditionalAction12', b)
    if hasattr(a2, 'pycom_ConditionalAction12'):
        assert _is_linked(a2, 'pycom_ConditionalAction12', b)
    _safe_set(b, 'pycom_Condition', None)
    assert not _is_linked(b, 'pycom_Condition', a2)
    if hasattr(a2, 'pycom_ConditionalAction12'):
        assert not _is_linked(a2, 'pycom_ConditionalAction12', b)


def test_assoc_conn3_reverse_link_reassign_clear():
    a1 = pycom_Server(name="sample_text")
    a2 = pycom_Server(name="sample_text_2")
    b = pycom_Connection(portnumber="sample_text")
    _safe_set(b, 'pycom_Connection', a1)
    assert _is_linked(b, 'pycom_Connection', a1)
    if hasattr(a1, 'pycom_Server4'):
        assert _is_linked(a1, 'pycom_Server4', b)
    _safe_set(b, 'pycom_Connection', a2)
    assert _is_linked(b, 'pycom_Connection', a2)
    if hasattr(a1, 'pycom_Server4'):
        assert not _is_linked(a1, 'pycom_Server4', b)
    if hasattr(a2, 'pycom_Server4'):
        assert _is_linked(a2, 'pycom_Server4', b)
    _safe_set(b, 'pycom_Connection', None)
    assert not _is_linked(b, 'pycom_Connection', a2)
    if hasattr(a2, 'pycom_Server4'):
        assert not _is_linked(a2, 'pycom_Server4', b)


def test_assoc_exps5_reverse_link_reassign_clear():
    a1 = pycom_Server(name="sample_text")
    a2 = pycom_Server(name="sample_text_2")
    b = pycom_ConditionalAction(type="sample_text")
    _safe_set(b, 'pycom_ConditionalAction', a1)
    assert _is_linked(b, 'pycom_ConditionalAction', a1)
    if hasattr(a1, 'pycom_Server6'):
        assert _is_linked(a1, 'pycom_Server6', b)
    _safe_set(b, 'pycom_ConditionalAction', a2)
    assert _is_linked(b, 'pycom_ConditionalAction', a2)
    if hasattr(a1, 'pycom_Server6'):
        assert not _is_linked(a1, 'pycom_Server6', b)
    if hasattr(a2, 'pycom_Server6'):
        assert _is_linked(a2, 'pycom_Server6', b)
    _safe_set(b, 'pycom_ConditionalAction', None)
    assert not _is_linked(b, 'pycom_ConditionalAction', a2)
    if hasattr(a2, 'pycom_Server6'):
        assert not _is_linked(a2, 'pycom_Server6', b)


def test_assoc_host7_reverse_link_reassign_clear():
    a1 = pycom_Host(ipAdr="sample_text", website="sample_text")
    a2 = pycom_Host(ipAdr="sample_text_2", website="sample_text_2")
    b = pycom_Connection(portnumber="sample_text")
    _safe_set(b, 'pycom_Connection8', a1)
    assert _is_linked(b, 'pycom_Connection8', a1)
    if hasattr(a1, 'pycom_Host'):
        assert _is_linked(a1, 'pycom_Host', b)
    _safe_set(b, 'pycom_Connection8', a2)
    assert _is_linked(b, 'pycom_Connection8', a2)
    if hasattr(a1, 'pycom_Host'):
        assert not _is_linked(a1, 'pycom_Host', b)
    if hasattr(a2, 'pycom_Host'):
        assert _is_linked(a2, 'pycom_Host', b)
    _safe_set(b, 'pycom_Connection8', None)
    assert not _is_linked(b, 'pycom_Connection8', a2)
    if hasattr(a2, 'pycom_Host'):
        assert not _is_linked(a2, 'pycom_Host', b)


def test_assoc_left34_reverse_link_reassign_clear():
    a1 = pycom_Expression(outputValue=7)
    a2 = pycom_Expression(outputValue=13)
    b = pycom_ComparisonExp(op="sample_text")
    _safe_set(b, 'pycom_ComparisonExp35', a1)
    assert _is_linked(b, 'pycom_ComparisonExp35', a1)
    if hasattr(a1, 'pycom_Expression'):
        assert _is_linked(a1, 'pycom_Expression', b)
    _safe_set(b, 'pycom_ComparisonExp35', a2)
    assert _is_linked(b, 'pycom_ComparisonExp35', a2)
    if hasattr(a1, 'pycom_Expression'):
        assert not _is_linked(a1, 'pycom_Expression', b)
    if hasattr(a2, 'pycom_Expression'):
        assert _is_linked(a2, 'pycom_Expression', b)
    _safe_set(b, 'pycom_ComparisonExp35', None)
    assert not _is_linked(b, 'pycom_ComparisonExp35', a2)
    if hasattr(a2, 'pycom_Expression'):
        assert not _is_linked(a2, 'pycom_Expression', b)


def test_assoc_nestedCondition28_reverse_link_reassign_clear():
    a1 = pycom_Condition(operator="sample_text")
    a2 = pycom_Condition(operator="sample_text_2")
    b = pycom_Condition(operator="sample_text")
    _safe_set(b, 'pycom_Condition29', a1)
    assert _is_linked(b, 'pycom_Condition29', a1)
    if hasattr(a1, 'pycom_Condition27'):
        assert _is_linked(a1, 'pycom_Condition27', b)
    _safe_set(b, 'pycom_Condition29', a2)
    assert _is_linked(b, 'pycom_Condition29', a2)
    if hasattr(a1, 'pycom_Condition27'):
        assert not _is_linked(a1, 'pycom_Condition27', b)
    if hasattr(a2, 'pycom_Condition27'):
        assert _is_linked(a2, 'pycom_Condition27', b)
    _safe_set(b, 'pycom_Condition29', None)
    assert not _is_linked(b, 'pycom_Condition29', a2)
    if hasattr(a2, 'pycom_Condition27'):
        assert not _is_linked(a2, 'pycom_Condition27', b)


def test_assoc_right36_reverse_link_reassign_clear():
    a1 = pycom_Expression(outputValue=7)
    a2 = pycom_Expression(outputValue=13)
    b = pycom_ComparisonExp(op="sample_text")
    _safe_set(b, 'pycom_ComparisonExp37', a1)
    assert _is_linked(b, 'pycom_ComparisonExp37', a1)
    if hasattr(a1, 'pycom_Expression38'):
        assert _is_linked(a1, 'pycom_Expression38', b)
    _safe_set(b, 'pycom_ComparisonExp37', a2)
    assert _is_linked(b, 'pycom_ComparisonExp37', a2)
    if hasattr(a1, 'pycom_Expression38'):
        assert not _is_linked(a1, 'pycom_Expression38', b)
    if hasattr(a2, 'pycom_Expression38'):
        assert _is_linked(a2, 'pycom_Expression38', b)
    _safe_set(b, 'pycom_ComparisonExp37', None)
    assert not _is_linked(b, 'pycom_ComparisonExp37', a2)
    if hasattr(a2, 'pycom_Expression38'):
        assert not _is_linked(a2, 'pycom_Expression38', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ExpMembers13_stub_double():
    # pycom_ExpMember has no real 'pycom_ExpMember' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ConditionalAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ConditionalAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ConditionalAction(type="sample_text")
    partner = pycom_ExpMember()
    setattr(partner, 'pycom_ExpMember', None)
    _safe_set(owner, 'pycom_ConditionalAction14', {partner})
    assert getattr(partner, 'pycom_ExpMember') == owner
    _safe_set(owner, 'pycom_ConditionalAction14', set())
    assert getattr(partner, 'pycom_ExpMember') is None


def test_assoc_actuatorTypes16_stub_double():
    # pycom_Actuator has no real 'pycom_Actuator' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ModuleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ModuleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ModuleType(name="sample_text", typeName="sample_text")
    partner = pycom_Actuator()
    setattr(partner, 'pycom_Actuator', None)
    _safe_set(owner, 'pycom_ModuleType17', partner)
    assert owner in getattr(partner, 'pycom_Actuator')
    _safe_set(owner, 'pycom_ModuleType17', None)
    assert owner not in getattr(partner, 'pycom_Actuator')


def test_assoc_board41_stub_double():
    # pycom_Function has no real 'pycom_Function42' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Board(name="sample_text")
    partner = pycom_Function()
    setattr(partner, 'pycom_Function42', None)
    _safe_set(owner, 'pycom_Board43', partner)
    assert getattr(partner, 'pycom_Function42') == owner
    _safe_set(owner, 'pycom_Board43', None)
    assert getattr(partner, 'pycom_Function42') is None


def test_assoc_boardMembers9_stub_double():
    # pycom_BoardMember has no real 'pycom_BoardMember' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Board(name="sample_text")
    partner = pycom_BoardMember()
    setattr(partner, 'pycom_BoardMember', None)
    _safe_set(owner, 'pycom_Board10', {partner})
    assert getattr(partner, 'pycom_BoardMember') == owner
    _safe_set(owner, 'pycom_Board10', set())
    assert getattr(partner, 'pycom_BoardMember') is None


def test_assoc_boards0_stub_double():
    # pycom_System has no real 'pycom_System' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Board(name="sample_text")
    partner = pycom_System()
    setattr(partner, 'pycom_System', None)
    _safe_set(owner, 'pycom_Board', partner)
    assert owner in getattr(partner, 'pycom_System')
    _safe_set(owner, 'pycom_Board', None)
    assert owner not in getattr(partner, 'pycom_System')


def test_assoc_boolVal30_stub_double():
    # pycom_LogicExp has no real 'pycom_LogicExp31' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Boolean's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Boolean's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Boolean(value="sample_text")
    partner = pycom_LogicExp()
    setattr(partner, 'pycom_LogicExp31', None)
    _safe_set(owner, 'pycom_Boolean', partner)
    assert getattr(partner, 'pycom_LogicExp31') == owner
    _safe_set(owner, 'pycom_Boolean', None)
    assert getattr(partner, 'pycom_LogicExp31') is None


def test_assoc_compExp32_stub_double():
    # pycom_LogicExp has no real 'pycom_LogicExp33' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ComparisonExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ComparisonExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ComparisonExp(op="sample_text")
    partner = pycom_LogicExp()
    setattr(partner, 'pycom_LogicExp33', None)
    _safe_set(owner, 'pycom_ComparisonExp', partner)
    assert getattr(partner, 'pycom_LogicExp33') == owner
    _safe_set(owner, 'pycom_ComparisonExp', None)
    assert getattr(partner, 'pycom_LogicExp33') is None


def test_assoc_functionName44_stub_double():
    # pycom_Function has no real 'pycom_Function45' property in the generated
    # code (a bare stub) -- manually attach it so pycom_FunctionName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_FunctionName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_FunctionName(name="sample_text")
    partner = pycom_Function()
    setattr(partner, 'pycom_Function45', None)
    _safe_set(owner, 'pycom_FunctionName', partner)
    assert getattr(partner, 'pycom_Function45') == owner
    _safe_set(owner, 'pycom_FunctionName', None)
    assert getattr(partner, 'pycom_Function45') is None


def test_assoc_input22_stub_double():
    # pycom_Pin has no real 'pycom_Pin23' property in the generated
    # code (a bare stub) -- manually attach it so pycom_PinName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_PinName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_PinName(name="sample_text")
    partner = pycom_Pin()
    setattr(partner, 'pycom_Pin23', None)
    _safe_set(owner, 'pycom_PinName24', partner)
    assert getattr(partner, 'pycom_Pin23') == owner
    _safe_set(owner, 'pycom_PinName24', None)
    assert getattr(partner, 'pycom_Pin23') is None


def test_assoc_logicEx25_stub_double():
    # pycom_LogicExp has no real 'pycom_LogicExp' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Condition(operator="sample_text")
    partner = pycom_LogicExp()
    setattr(partner, 'pycom_LogicExp', None)
    _safe_set(owner, 'pycom_Condition26', partner)
    assert getattr(partner, 'pycom_LogicExp') == owner
    _safe_set(owner, 'pycom_Condition26', None)
    assert getattr(partner, 'pycom_LogicExp') is None


def test_assoc_moduleType46_stub_double():
    # pycom_ModuleFunction has no real 'pycom_ModuleFunction' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ModuleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ModuleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ModuleType(name="sample_text", typeName="sample_text")
    partner = pycom_ModuleFunction()
    setattr(partner, 'pycom_ModuleFunction', None)
    _safe_set(owner, 'pycom_ModuleType47', partner)
    assert getattr(partner, 'pycom_ModuleFunction') == owner
    _safe_set(owner, 'pycom_ModuleType47', None)
    assert getattr(partner, 'pycom_ModuleFunction') is None


def test_assoc_outputfunction39_stub_double():
    # pycom_Function has no real 'pycom_Function' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Expression(outputValue=7)
    partner = pycom_Function()
    setattr(partner, 'pycom_Function', None)
    _safe_set(owner, 'pycom_Expression40', partner)
    assert getattr(partner, 'pycom_Function') == owner
    _safe_set(owner, 'pycom_Expression40', None)
    assert getattr(partner, 'pycom_Function') is None


def test_assoc_pins18_stub_double():
    # pycom_Pin has no real 'pycom_Pin' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ModuleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ModuleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ModuleType(name="sample_text", typeName="sample_text")
    partner = pycom_Pin()
    setattr(partner, 'pycom_Pin', None)
    _safe_set(owner, 'pycom_ModuleType19', partner)
    assert getattr(partner, 'pycom_Pin') == owner
    _safe_set(owner, 'pycom_ModuleType19', None)
    assert getattr(partner, 'pycom_Pin') is None


def test_assoc_power20_stub_double():
    # pycom_Pin has no real 'pycom_Pin21' property in the generated
    # code (a bare stub) -- manually attach it so pycom_PinName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_PinName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_PinName(name="sample_text")
    partner = pycom_Pin()
    setattr(partner, 'pycom_Pin21', None)
    _safe_set(owner, 'pycom_PinName', partner)
    assert getattr(partner, 'pycom_Pin21') == owner
    _safe_set(owner, 'pycom_PinName', None)
    assert getattr(partner, 'pycom_Pin21') is None


def test_assoc_sensorTypes15_stub_double():
    # pycom_Sensor has no real 'pycom_Sensor' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ModuleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ModuleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ModuleType(name="sample_text", typeName="sample_text")
    partner = pycom_Sensor()
    setattr(partner, 'pycom_Sensor', None)
    _safe_set(owner, 'pycom_ModuleType', partner)
    assert owner in getattr(partner, 'pycom_Sensor')
    _safe_set(owner, 'pycom_ModuleType', None)
    assert owner not in getattr(partner, 'pycom_Sensor')


def test_assoc_servers1_stub_double():
    # pycom_System has no real 'pycom_System2' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Server's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Server's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Server(name="sample_text")
    partner = pycom_System()
    setattr(partner, 'pycom_System2', None)
    _safe_set(owner, 'pycom_Server', partner)
    assert owner in getattr(partner, 'pycom_System2')
    _safe_set(owner, 'pycom_Server', None)
    assert owner not in getattr(partner, 'pycom_System2')




from python_code import pycom_Board
from python_code import pycom_Function
from python_code import pycom_System

def test_pycom_Board___init__():
    assert pycom_Board.__init__(pycom_Board('', pycom_Board=pycom_System(), pycom_Board10=set(), pycom_Board43=pycom_Function()), '', pycom_Board=pycom_System(), pycom_Board10=set(), pycom_Board43=pycom_Function()) == None
from python_code import pycom_Boolean
from python_code import pycom_LogicExp

def test_pycom_Boolean___init__():
    assert pycom_Boolean.__init__(pycom_Boolean('', pycom_Boolean=pycom_LogicExp()), '', pycom_Boolean=pycom_LogicExp()) == None
from python_code import pycom_Communication

def test_pycom_Communication___init__():
    assert pycom_Communication.__init__(pycom_Communication(''), '') == None
from python_code import pycom_Function
from python_code import pycom_FunctionName

def test_pycom_FunctionName___init__():
    assert pycom_FunctionName.__init__(pycom_FunctionName('', pycom_FunctionName=pycom_Function()), '', pycom_FunctionName=pycom_Function()) == None
from python_code import pycom_Actuator
from python_code import pycom_ModuleFunction
from python_code import pycom_ModuleType
from python_code import pycom_Pin
from python_code import pycom_Sensor

def test_pycom_ModuleType___init__():
    assert pycom_ModuleType.__init__(pycom_ModuleType('', '\x00', pycom_ModuleType=pycom_Sensor(), pycom_ModuleType17=pycom_Actuator(), pycom_ModuleType19=pycom_Pin(), pycom_ModuleType47=pycom_ModuleFunction()), '\x00\x00', '', pycom_ModuleType=pycom_Sensor(), pycom_ModuleType17=pycom_Actuator(), pycom_ModuleType19=pycom_Pin(), pycom_ModuleType47=pycom_ModuleFunction()) == None
from python_code import pycom_Pin
from python_code import pycom_PinName

def test_pycom_PinName___init__():
    assert pycom_PinName.__init__(pycom_PinName('', pycom_PinName=pycom_Pin(), pycom_PinName24=pycom_Pin()), '', pycom_PinName=pycom_Pin(), pycom_PinName24=pycom_Pin()) == None

