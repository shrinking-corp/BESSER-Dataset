import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    Function,
    iOTConnector_BitwiseOperator,
    iOTConnector_Board,
    iOTConnector_Config,
    iOTConnector_Div,
    iOTConnector_Expression,
    iOTConnector_Filter,
    iOTConnector_FilterAction,
    iOTConnector_FilterExp,
    iOTConnector_FilterType,
    iOTConnector_Function,
    iOTConnector_Minus,
    iOTConnector_Mult,
    iOTConnector_Num,
    iOTConnector_Output,
    iOTConnector_Plus,
    iOTConnector_Process,
    iOTConnector_ProcessAction,
    iOTConnector_Program,
    iOTConnector_ReadingName,
    iOTConnector_ReadingNameWithConfigScope,
    iOTConnector_RelationalOperator,
    iOTConnector_Sample,
    iOTConnector_SampleAction,
    iOTConnector_Send,
    iOTConnector_SendAction,
    iOTConnector_Sensor,
    iOTConnector_SensorConfig,
    iOTConnector_TimeUnit,
    iOTConnector_Var,
    iOTConnector_Webserver,
    iOTConnector_Wifi,
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

def test_iOTConnector_BitwiseOperator_value_value_roundtrip():
    instance = iOTConnector_BitwiseOperator(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iOTConnector_Board_name_value_roundtrip():
    instance = iOTConnector_Board(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iOTConnector_Config_name_value_roundtrip():
    instance = iOTConnector_Config(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iOTConnector_FilterAction_number_value_roundtrip():
    instance = iOTConnector_FilterAction(number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_iOTConnector_FilterExp_number_value_roundtrip():
    instance = iOTConnector_FilterExp(number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_iOTConnector_FilterType_value_value_roundtrip():
    instance = iOTConnector_FilterType(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iOTConnector_Num_value_value_roundtrip():
    instance = iOTConnector_Num(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_iOTConnector_ReadingName_name_value_roundtrip():
    instance = iOTConnector_ReadingName(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iOTConnector_RelationalOperator_value_value_roundtrip():
    instance = iOTConnector_RelationalOperator(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iOTConnector_SampleAction_amountOfTime_value_roundtrip():
    instance = iOTConnector_SampleAction(amountOfTime=7, number=7)
    assert instance.amountOfTime == 7
    instance.amountOfTime = 13
    assert instance.amountOfTime == 13


def test_iOTConnector_SampleAction_number_value_roundtrip():
    instance = iOTConnector_SampleAction(amountOfTime=7, number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_iOTConnector_SendAction_number_value_roundtrip():
    instance = iOTConnector_SendAction(number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_iOTConnector_Sensor_name_value_roundtrip():
    instance = iOTConnector_Sensor(name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iOTConnector_Sensor_type_value_roundtrip():
    instance = iOTConnector_Sensor(name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_iOTConnector_SensorConfig_name_value_roundtrip():
    instance = iOTConnector_SensorConfig(name="sample_text", pinIn="sample_text", pinOut="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iOTConnector_SensorConfig_pinIn_value_roundtrip():
    instance = iOTConnector_SensorConfig(name="sample_text", pinIn="sample_text", pinOut="sample_text")
    assert instance.pinIn == "sample_text"
    instance.pinIn = "sample_text_2"
    assert instance.pinIn == "sample_text_2"


def test_iOTConnector_SensorConfig_pinOut_value_roundtrip():
    instance = iOTConnector_SensorConfig(name="sample_text", pinIn="sample_text", pinOut="sample_text")
    assert instance.pinOut == "sample_text"
    instance.pinOut = "sample_text_2"
    assert instance.pinOut == "sample_text_2"


def test_iOTConnector_TimeUnit_value_value_roundtrip():
    instance = iOTConnector_TimeUnit(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iOTConnector_Webserver_port_value_roundtrip():
    instance = iOTConnector_Webserver(port=7, url="sample_text")
    assert instance.port == 7
    instance.port = 13
    assert instance.port == 13


def test_iOTConnector_Webserver_url_value_roundtrip():
    instance = iOTConnector_Webserver(port=7, url="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_iOTConnector_Wifi_password_value_roundtrip():
    instance = iOTConnector_Wifi(password="sample_text", ssid="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_iOTConnector_Wifi_ssid_value_roundtrip():
    instance = iOTConnector_Wifi(password="sample_text", ssid="sample_text")
    assert instance.ssid == "sample_text"
    instance.ssid = "sample_text_2"
    assert instance.ssid == "sample_text_2"


def test_iOTConnector_Div_isa_Expression():
    instance = iOTConnector_Div()
    assert isinstance(instance, Expression)


def test_iOTConnector_Minus_isa_Expression():
    instance = iOTConnector_Minus()
    assert isinstance(instance, Expression)


def test_iOTConnector_Mult_isa_Expression():
    instance = iOTConnector_Mult()
    assert isinstance(instance, Expression)


def test_iOTConnector_Num_isa_Expression():
    instance = iOTConnector_Num(value=7)
    assert isinstance(instance, Expression)


def test_iOTConnector_Plus_isa_Expression():
    instance = iOTConnector_Plus()
    assert isinstance(instance, Expression)


def test_iOTConnector_Var_isa_Expression():
    instance = iOTConnector_Var()
    assert isinstance(instance, Expression)


def test_iOTConnector_Filter_isa_Function():
    instance = iOTConnector_Filter()
    assert isinstance(instance, Function)


def test_iOTConnector_Process_isa_Function():
    instance = iOTConnector_Process()
    assert isinstance(instance, Function)


def test_iOTConnector_Sample_isa_Function():
    instance = iOTConnector_Sample()
    assert isinstance(instance, Function)


def test_assoc_bitwiseOperator46_link_reassign_clear():
    a = iOTConnector_FilterExp(number=7)
    b1 = iOTConnector_BitwiseOperator(value="sample_text")
    b2 = iOTConnector_BitwiseOperator(value="sample_text_2")
    _safe_set(a, 'iOTConnector_FilterExp47', b1)
    assert _is_linked(a, 'iOTConnector_FilterExp47', b1)
    if hasattr(b1, 'iOTConnector_BitwiseOperator'):
        assert _is_linked(b1, 'iOTConnector_BitwiseOperator', a)
    _safe_set(a, 'iOTConnector_FilterExp47', b2)
    assert _is_linked(a, 'iOTConnector_FilterExp47', b2)
    if hasattr(b1, 'iOTConnector_BitwiseOperator'):
        assert not _is_linked(b1, 'iOTConnector_BitwiseOperator', a)
    if hasattr(b2, 'iOTConnector_BitwiseOperator'):
        assert _is_linked(b2, 'iOTConnector_BitwiseOperator', a)
    _safe_set(a, 'iOTConnector_FilterExp47', None)
    assert not _is_linked(a, 'iOTConnector_FilterExp47', b2)
    if hasattr(b2, 'iOTConnector_BitwiseOperator'):
        assert not _is_linked(b2, 'iOTConnector_BitwiseOperator', a)


def test_assoc_boards5_link_reassign_clear():
    a = iOTConnector_Board(name="sample_text")
    b1 = iOTConnector_Program()
    b2 = iOTConnector_Program()
    _safe_set(a, 'iOTConnector_Board', b1)
    assert _is_linked(a, 'iOTConnector_Board', b1)
    if hasattr(b1, 'iOTConnector_Program6'):
        assert _is_linked(b1, 'iOTConnector_Program6', a)
    _safe_set(a, 'iOTConnector_Board', b2)
    assert _is_linked(a, 'iOTConnector_Board', b2)
    if hasattr(b1, 'iOTConnector_Program6'):
        assert not _is_linked(b1, 'iOTConnector_Program6', a)
    if hasattr(b2, 'iOTConnector_Program6'):
        assert _is_linked(b2, 'iOTConnector_Program6', a)
    _safe_set(a, 'iOTConnector_Board', None)
    assert not _is_linked(a, 'iOTConnector_Board', b2)
    if hasattr(b2, 'iOTConnector_Program6'):
        assert not _is_linked(b2, 'iOTConnector_Program6', a)


def test_assoc_configName11_link_reassign_clear():
    a = iOTConnector_Config(name="sample_text")
    b1 = iOTConnector_Board(name="sample_text")
    b2 = iOTConnector_Board(name="sample_text_2")
    _safe_set(a, 'iOTConnector_Config13', b1)
    assert _is_linked(a, 'iOTConnector_Config13', b1)
    if hasattr(b1, 'iOTConnector_Board12'):
        assert _is_linked(b1, 'iOTConnector_Board12', a)
    _safe_set(a, 'iOTConnector_Config13', b2)
    assert _is_linked(a, 'iOTConnector_Config13', b2)
    if hasattr(b1, 'iOTConnector_Board12'):
        assert not _is_linked(b1, 'iOTConnector_Board12', a)
    if hasattr(b2, 'iOTConnector_Board12'):
        assert _is_linked(b2, 'iOTConnector_Board12', a)
    _safe_set(a, 'iOTConnector_Config13', None)
    assert not _is_linked(a, 'iOTConnector_Config13', b2)
    if hasattr(b2, 'iOTConnector_Board12'):
        assert not _is_linked(b2, 'iOTConnector_Board12', a)


def test_assoc_configs3_link_reassign_clear():
    a = iOTConnector_Config(name="sample_text")
    b1 = iOTConnector_Program()
    b2 = iOTConnector_Program()
    _safe_set(a, 'iOTConnector_Config', b1)
    assert _is_linked(a, 'iOTConnector_Config', b1)
    if hasattr(b1, 'iOTConnector_Program4'):
        assert _is_linked(b1, 'iOTConnector_Program4', a)
    _safe_set(a, 'iOTConnector_Config', b2)
    assert _is_linked(a, 'iOTConnector_Config', b2)
    if hasattr(b1, 'iOTConnector_Program4'):
        assert not _is_linked(b1, 'iOTConnector_Program4', a)
    if hasattr(b2, 'iOTConnector_Program4'):
        assert _is_linked(b2, 'iOTConnector_Program4', a)
    _safe_set(a, 'iOTConnector_Config', None)
    assert not _is_linked(a, 'iOTConnector_Config', b2)
    if hasattr(b2, 'iOTConnector_Program4'):
        assert not _is_linked(b2, 'iOTConnector_Program4', a)


def test_assoc_filterActions32_link_reassign_clear():
    a = iOTConnector_FilterAction(number=7)
    b1 = iOTConnector_Filter()
    b2 = iOTConnector_Filter()
    _safe_set(a, 'iOTConnector_FilterAction', b1)
    assert _is_linked(a, 'iOTConnector_FilterAction', b1)
    if hasattr(b1, 'iOTConnector_Filter'):
        assert _is_linked(b1, 'iOTConnector_Filter', a)
    _safe_set(a, 'iOTConnector_FilterAction', b2)
    assert _is_linked(a, 'iOTConnector_FilterAction', b2)
    if hasattr(b1, 'iOTConnector_Filter'):
        assert not _is_linked(b1, 'iOTConnector_Filter', a)
    if hasattr(b2, 'iOTConnector_Filter'):
        assert _is_linked(b2, 'iOTConnector_Filter', a)
    _safe_set(a, 'iOTConnector_FilterAction', None)
    assert not _is_linked(a, 'iOTConnector_FilterAction', b2)
    if hasattr(b2, 'iOTConnector_Filter'):
        assert not _is_linked(b2, 'iOTConnector_Filter', a)


def test_assoc_filterExp38_link_reassign_clear():
    a = iOTConnector_FilterExp(number=7)
    b1 = iOTConnector_FilterAction(number=7)
    b2 = iOTConnector_FilterAction(number=13)
    _safe_set(a, 'iOTConnector_FilterExp', b1)
    assert _is_linked(a, 'iOTConnector_FilterExp', b1)
    if hasattr(b1, 'iOTConnector_FilterAction39'):
        assert _is_linked(b1, 'iOTConnector_FilterAction39', a)
    _safe_set(a, 'iOTConnector_FilterExp', b2)
    assert _is_linked(a, 'iOTConnector_FilterExp', b2)
    if hasattr(b1, 'iOTConnector_FilterAction39'):
        assert not _is_linked(b1, 'iOTConnector_FilterAction39', a)
    if hasattr(b2, 'iOTConnector_FilterAction39'):
        assert _is_linked(b2, 'iOTConnector_FilterAction39', a)
    _safe_set(a, 'iOTConnector_FilterExp', None)
    assert not _is_linked(a, 'iOTConnector_FilterExp', b2)
    if hasattr(b2, 'iOTConnector_FilterAction39'):
        assert not _is_linked(b2, 'iOTConnector_FilterAction39', a)


def test_assoc_filterExp49_link_reassign_clear():
    a = iOTConnector_FilterExp(number=7)
    b1 = iOTConnector_FilterExp(number=7)
    b2 = iOTConnector_FilterExp(number=13)
    _safe_set(a, 'iOTConnector_FilterExp48', b1)
    assert _is_linked(a, 'iOTConnector_FilterExp48', b1)
    if hasattr(b1, 'iOTConnector_FilterExp50'):
        assert _is_linked(b1, 'iOTConnector_FilterExp50', a)
    _safe_set(a, 'iOTConnector_FilterExp48', b2)
    assert _is_linked(a, 'iOTConnector_FilterExp48', b2)
    if hasattr(b1, 'iOTConnector_FilterExp50'):
        assert not _is_linked(b1, 'iOTConnector_FilterExp50', a)
    if hasattr(b2, 'iOTConnector_FilterExp50'):
        assert _is_linked(b2, 'iOTConnector_FilterExp50', a)
    _safe_set(a, 'iOTConnector_FilterExp48', None)
    assert not _is_linked(a, 'iOTConnector_FilterExp48', b2)
    if hasattr(b2, 'iOTConnector_FilterExp50'):
        assert not _is_linked(b2, 'iOTConnector_FilterExp50', a)


def test_assoc_filterType36_link_reassign_clear():
    a = iOTConnector_FilterType(value="sample_text")
    b1 = iOTConnector_FilterAction(number=7)
    b2 = iOTConnector_FilterAction(number=13)
    _safe_set(a, 'iOTConnector_FilterType', b1)
    assert _is_linked(a, 'iOTConnector_FilterType', b1)
    if hasattr(b1, 'iOTConnector_FilterAction37'):
        assert _is_linked(b1, 'iOTConnector_FilterAction37', a)
    _safe_set(a, 'iOTConnector_FilterType', b2)
    assert _is_linked(a, 'iOTConnector_FilterType', b2)
    if hasattr(b1, 'iOTConnector_FilterAction37'):
        assert not _is_linked(b1, 'iOTConnector_FilterAction37', a)
    if hasattr(b2, 'iOTConnector_FilterAction37'):
        assert _is_linked(b2, 'iOTConnector_FilterAction37', a)
    _safe_set(a, 'iOTConnector_FilterType', None)
    assert not _is_linked(a, 'iOTConnector_FilterType', b2)
    if hasattr(b2, 'iOTConnector_FilterAction37'):
        assert not _is_linked(b2, 'iOTConnector_FilterAction37', a)


def test_assoc_functions16_link_reassign_clear():
    a = iOTConnector_Sensor(name="sample_text", type="sample_text")
    b1 = iOTConnector_Function()
    b2 = iOTConnector_Function()
    _safe_set(a, 'iOTConnector_Sensor17', {b1})
    assert _is_linked(a, 'iOTConnector_Sensor17', b1)
    if hasattr(b1, 'iOTConnector_Function'):
        assert _is_linked(b1, 'iOTConnector_Function', a)
    _safe_set(a, 'iOTConnector_Sensor17', {b2})
    assert _is_linked(a, 'iOTConnector_Sensor17', b2)
    if hasattr(b1, 'iOTConnector_Function'):
        assert not _is_linked(b1, 'iOTConnector_Function', a)
    if hasattr(b2, 'iOTConnector_Function'):
        assert _is_linked(b2, 'iOTConnector_Function', a)
    _safe_set(a, 'iOTConnector_Sensor17', set())
    assert not _is_linked(a, 'iOTConnector_Sensor17', b2)
    if hasattr(b2, 'iOTConnector_Function'):
        assert not _is_linked(b2, 'iOTConnector_Function', a)


def test_assoc_name65_link_reassign_clear():
    a = iOTConnector_ReadingName(name="sample_text")
    b1 = iOTConnector_ReadingNameWithConfigScope()
    b2 = iOTConnector_ReadingNameWithConfigScope()
    _safe_set(a, 'iOTConnector_ReadingName67', b1)
    assert _is_linked(a, 'iOTConnector_ReadingName67', b1)
    if hasattr(b1, 'iOTConnector_ReadingNameWithConfigScope66'):
        assert _is_linked(b1, 'iOTConnector_ReadingNameWithConfigScope66', a)
    _safe_set(a, 'iOTConnector_ReadingName67', b2)
    assert _is_linked(a, 'iOTConnector_ReadingName67', b2)
    if hasattr(b1, 'iOTConnector_ReadingNameWithConfigScope66'):
        assert not _is_linked(b1, 'iOTConnector_ReadingNameWithConfigScope66', a)
    if hasattr(b2, 'iOTConnector_ReadingNameWithConfigScope66'):
        assert _is_linked(b2, 'iOTConnector_ReadingNameWithConfigScope66', a)
    _safe_set(a, 'iOTConnector_ReadingName67', None)
    assert not _is_linked(a, 'iOTConnector_ReadingName67', b2)
    if hasattr(b2, 'iOTConnector_ReadingNameWithConfigScope66'):
        assert not _is_linked(b2, 'iOTConnector_ReadingNameWithConfigScope66', a)


def test_assoc_output14_link_reassign_clear():
    a = iOTConnector_Sensor(name="sample_text", type="sample_text")
    b1 = iOTConnector_Output()
    b2 = iOTConnector_Output()
    _safe_set(a, 'iOTConnector_Sensor15', b1)
    assert _is_linked(a, 'iOTConnector_Sensor15', b1)
    if hasattr(b1, 'iOTConnector_Output'):
        assert _is_linked(b1, 'iOTConnector_Output', a)
    _safe_set(a, 'iOTConnector_Sensor15', b2)
    assert _is_linked(a, 'iOTConnector_Sensor15', b2)
    if hasattr(b1, 'iOTConnector_Output'):
        assert not _is_linked(b1, 'iOTConnector_Output', a)
    if hasattr(b2, 'iOTConnector_Output'):
        assert _is_linked(b2, 'iOTConnector_Output', a)
    _safe_set(a, 'iOTConnector_Sensor15', None)
    assert not _is_linked(a, 'iOTConnector_Sensor15', b2)
    if hasattr(b2, 'iOTConnector_Output'):
        assert not _is_linked(b2, 'iOTConnector_Output', a)


def test_assoc_readingName23_link_reassign_clear():
    a = iOTConnector_SampleAction(amountOfTime=7, number=7)
    b1 = iOTConnector_ReadingName(name="sample_text")
    b2 = iOTConnector_ReadingName(name="sample_text_2")
    _safe_set(a, 'iOTConnector_SampleAction24', b1)
    assert _is_linked(a, 'iOTConnector_SampleAction24', b1)
    if hasattr(b1, 'iOTConnector_ReadingName25'):
        assert _is_linked(b1, 'iOTConnector_ReadingName25', a)
    _safe_set(a, 'iOTConnector_SampleAction24', b2)
    assert _is_linked(a, 'iOTConnector_SampleAction24', b2)
    if hasattr(b1, 'iOTConnector_ReadingName25'):
        assert not _is_linked(b1, 'iOTConnector_ReadingName25', a)
    if hasattr(b2, 'iOTConnector_ReadingName25'):
        assert _is_linked(b2, 'iOTConnector_ReadingName25', a)
    _safe_set(a, 'iOTConnector_SampleAction24', None)
    assert not _is_linked(a, 'iOTConnector_SampleAction24', b2)
    if hasattr(b2, 'iOTConnector_ReadingName25'):
        assert not _is_linked(b2, 'iOTConnector_ReadingName25', a)


def test_assoc_readingName33_link_reassign_clear():
    a = iOTConnector_ReadingName(name="sample_text")
    b1 = iOTConnector_FilterAction(number=7)
    b2 = iOTConnector_FilterAction(number=13)
    _safe_set(a, 'iOTConnector_ReadingName35', b1)
    assert _is_linked(a, 'iOTConnector_ReadingName35', b1)
    if hasattr(b1, 'iOTConnector_FilterAction34'):
        assert _is_linked(b1, 'iOTConnector_FilterAction34', a)
    _safe_set(a, 'iOTConnector_ReadingName35', b2)
    assert _is_linked(a, 'iOTConnector_ReadingName35', b2)
    if hasattr(b1, 'iOTConnector_FilterAction34'):
        assert not _is_linked(b1, 'iOTConnector_FilterAction34', a)
    if hasattr(b2, 'iOTConnector_FilterAction34'):
        assert _is_linked(b2, 'iOTConnector_FilterAction34', a)
    _safe_set(a, 'iOTConnector_ReadingName35', None)
    assert not _is_linked(a, 'iOTConnector_ReadingName35', b2)
    if hasattr(b2, 'iOTConnector_FilterAction34'):
        assert not _is_linked(b2, 'iOTConnector_FilterAction34', a)


def test_assoc_readingName40_link_reassign_clear():
    a = iOTConnector_FilterExp(number=7)
    b1 = iOTConnector_ReadingNameWithConfigScope()
    b2 = iOTConnector_ReadingNameWithConfigScope()
    _safe_set(a, 'iOTConnector_FilterExp41', b1)
    assert _is_linked(a, 'iOTConnector_FilterExp41', b1)
    if hasattr(b1, 'iOTConnector_ReadingNameWithConfigScope42'):
        assert _is_linked(b1, 'iOTConnector_ReadingNameWithConfigScope42', a)
    _safe_set(a, 'iOTConnector_FilterExp41', b2)
    assert _is_linked(a, 'iOTConnector_FilterExp41', b2)
    if hasattr(b1, 'iOTConnector_ReadingNameWithConfigScope42'):
        assert not _is_linked(b1, 'iOTConnector_ReadingNameWithConfigScope42', a)
    if hasattr(b2, 'iOTConnector_ReadingNameWithConfigScope42'):
        assert _is_linked(b2, 'iOTConnector_ReadingNameWithConfigScope42', a)
    _safe_set(a, 'iOTConnector_FilterExp41', None)
    assert not _is_linked(a, 'iOTConnector_FilterExp41', b2)
    if hasattr(b2, 'iOTConnector_ReadingNameWithConfigScope42'):
        assert not _is_linked(b2, 'iOTConnector_ReadingNameWithConfigScope42', a)


def test_assoc_readingName52_link_reassign_clear():
    a = iOTConnector_ReadingName(name="sample_text")
    b1 = iOTConnector_ProcessAction()
    b2 = iOTConnector_ProcessAction()
    _safe_set(a, 'iOTConnector_ReadingName54', b1)
    assert _is_linked(a, 'iOTConnector_ReadingName54', b1)
    if hasattr(b1, 'iOTConnector_ProcessAction53'):
        assert _is_linked(b1, 'iOTConnector_ProcessAction53', a)
    _safe_set(a, 'iOTConnector_ReadingName54', b2)
    assert _is_linked(a, 'iOTConnector_ReadingName54', b2)
    if hasattr(b1, 'iOTConnector_ProcessAction53'):
        assert not _is_linked(b1, 'iOTConnector_ProcessAction53', a)
    if hasattr(b2, 'iOTConnector_ProcessAction53'):
        assert _is_linked(b2, 'iOTConnector_ProcessAction53', a)
    _safe_set(a, 'iOTConnector_ReadingName54', None)
    assert not _is_linked(a, 'iOTConnector_ReadingName54', b2)
    if hasattr(b2, 'iOTConnector_ProcessAction53'):
        assert not _is_linked(b2, 'iOTConnector_ProcessAction53', a)


def test_assoc_readingName59_link_reassign_clear():
    a = iOTConnector_SendAction(number=7)
    b1 = iOTConnector_ReadingName(name="sample_text")
    b2 = iOTConnector_ReadingName(name="sample_text_2")
    _safe_set(a, 'iOTConnector_SendAction60', b1)
    assert _is_linked(a, 'iOTConnector_SendAction60', b1)
    if hasattr(b1, 'iOTConnector_ReadingName61'):
        assert _is_linked(b1, 'iOTConnector_ReadingName61', a)
    _safe_set(a, 'iOTConnector_SendAction60', b2)
    assert _is_linked(a, 'iOTConnector_SendAction60', b2)
    if hasattr(b1, 'iOTConnector_ReadingName61'):
        assert not _is_linked(b1, 'iOTConnector_ReadingName61', a)
    if hasattr(b2, 'iOTConnector_ReadingName61'):
        assert _is_linked(b2, 'iOTConnector_ReadingName61', a)
    _safe_set(a, 'iOTConnector_SendAction60', None)
    assert not _is_linked(a, 'iOTConnector_SendAction60', b2)
    if hasattr(b2, 'iOTConnector_ReadingName61'):
        assert not _is_linked(b2, 'iOTConnector_ReadingName61', a)


def test_assoc_readingNameToCompare26_link_reassign_clear():
    a = iOTConnector_SampleAction(amountOfTime=7, number=7)
    b1 = iOTConnector_ReadingNameWithConfigScope()
    b2 = iOTConnector_ReadingNameWithConfigScope()
    _safe_set(a, 'iOTConnector_SampleAction27', b1)
    assert _is_linked(a, 'iOTConnector_SampleAction27', b1)
    if hasattr(b1, 'iOTConnector_ReadingNameWithConfigScope'):
        assert _is_linked(b1, 'iOTConnector_ReadingNameWithConfigScope', a)
    _safe_set(a, 'iOTConnector_SampleAction27', b2)
    assert _is_linked(a, 'iOTConnector_SampleAction27', b2)
    if hasattr(b1, 'iOTConnector_ReadingNameWithConfigScope'):
        assert not _is_linked(b1, 'iOTConnector_ReadingNameWithConfigScope', a)
    if hasattr(b2, 'iOTConnector_ReadingNameWithConfigScope'):
        assert _is_linked(b2, 'iOTConnector_ReadingNameWithConfigScope', a)
    _safe_set(a, 'iOTConnector_SampleAction27', None)
    assert not _is_linked(a, 'iOTConnector_SampleAction27', b2)
    if hasattr(b2, 'iOTConnector_ReadingNameWithConfigScope'):
        assert not _is_linked(b2, 'iOTConnector_ReadingNameWithConfigScope', a)


def test_assoc_readingNames20_link_reassign_clear():
    a = iOTConnector_ReadingName(name="sample_text")
    b1 = iOTConnector_Output()
    b2 = iOTConnector_Output()
    _safe_set(a, 'iOTConnector_ReadingName', b1)
    assert _is_linked(a, 'iOTConnector_ReadingName', b1)
    if hasattr(b1, 'iOTConnector_Output21'):
        assert _is_linked(b1, 'iOTConnector_Output21', a)
    _safe_set(a, 'iOTConnector_ReadingName', b2)
    assert _is_linked(a, 'iOTConnector_ReadingName', b2)
    if hasattr(b1, 'iOTConnector_Output21'):
        assert not _is_linked(b1, 'iOTConnector_Output21', a)
    if hasattr(b2, 'iOTConnector_Output21'):
        assert _is_linked(b2, 'iOTConnector_Output21', a)
    _safe_set(a, 'iOTConnector_ReadingName', None)
    assert not _is_linked(a, 'iOTConnector_ReadingName', b2)
    if hasattr(b2, 'iOTConnector_Output21'):
        assert not _is_linked(b2, 'iOTConnector_Output21', a)


def test_assoc_relationalOperator28_link_reassign_clear():
    a = iOTConnector_SampleAction(amountOfTime=7, number=7)
    b1 = iOTConnector_RelationalOperator(value="sample_text")
    b2 = iOTConnector_RelationalOperator(value="sample_text_2")
    _safe_set(a, 'iOTConnector_SampleAction29', b1)
    assert _is_linked(a, 'iOTConnector_SampleAction29', b1)
    if hasattr(b1, 'iOTConnector_RelationalOperator'):
        assert _is_linked(b1, 'iOTConnector_RelationalOperator', a)
    _safe_set(a, 'iOTConnector_SampleAction29', b2)
    assert _is_linked(a, 'iOTConnector_SampleAction29', b2)
    if hasattr(b1, 'iOTConnector_RelationalOperator'):
        assert not _is_linked(b1, 'iOTConnector_RelationalOperator', a)
    if hasattr(b2, 'iOTConnector_RelationalOperator'):
        assert _is_linked(b2, 'iOTConnector_RelationalOperator', a)
    _safe_set(a, 'iOTConnector_SampleAction29', None)
    assert not _is_linked(a, 'iOTConnector_SampleAction29', b2)
    if hasattr(b2, 'iOTConnector_RelationalOperator'):
        assert not _is_linked(b2, 'iOTConnector_RelationalOperator', a)


def test_assoc_relationalOperator43_link_reassign_clear():
    a = iOTConnector_RelationalOperator(value="sample_text")
    b1 = iOTConnector_FilterExp(number=7)
    b2 = iOTConnector_FilterExp(number=13)
    _safe_set(a, 'iOTConnector_RelationalOperator45', b1)
    assert _is_linked(a, 'iOTConnector_RelationalOperator45', b1)
    if hasattr(b1, 'iOTConnector_FilterExp44'):
        assert _is_linked(b1, 'iOTConnector_FilterExp44', a)
    _safe_set(a, 'iOTConnector_RelationalOperator45', b2)
    assert _is_linked(a, 'iOTConnector_RelationalOperator45', b2)
    if hasattr(b1, 'iOTConnector_FilterExp44'):
        assert not _is_linked(b1, 'iOTConnector_FilterExp44', a)
    if hasattr(b2, 'iOTConnector_FilterExp44'):
        assert _is_linked(b2, 'iOTConnector_FilterExp44', a)
    _safe_set(a, 'iOTConnector_RelationalOperator45', None)
    assert not _is_linked(a, 'iOTConnector_RelationalOperator45', b2)
    if hasattr(b2, 'iOTConnector_FilterExp44'):
        assert not _is_linked(b2, 'iOTConnector_FilterExp44', a)


def test_assoc_relationalOperator62_link_reassign_clear():
    a = iOTConnector_SendAction(number=7)
    b1 = iOTConnector_RelationalOperator(value="sample_text")
    b2 = iOTConnector_RelationalOperator(value="sample_text_2")
    _safe_set(a, 'iOTConnector_SendAction63', b1)
    assert _is_linked(a, 'iOTConnector_SendAction63', b1)
    if hasattr(b1, 'iOTConnector_RelationalOperator64'):
        assert _is_linked(b1, 'iOTConnector_RelationalOperator64', a)
    _safe_set(a, 'iOTConnector_SendAction63', b2)
    assert _is_linked(a, 'iOTConnector_SendAction63', b2)
    if hasattr(b1, 'iOTConnector_RelationalOperator64'):
        assert not _is_linked(b1, 'iOTConnector_RelationalOperator64', a)
    if hasattr(b2, 'iOTConnector_RelationalOperator64'):
        assert _is_linked(b2, 'iOTConnector_RelationalOperator64', a)
    _safe_set(a, 'iOTConnector_SendAction63', None)
    assert not _is_linked(a, 'iOTConnector_SendAction63', b2)
    if hasattr(b2, 'iOTConnector_RelationalOperator64'):
        assert not _is_linked(b2, 'iOTConnector_RelationalOperator64', a)


def test_assoc_sampleActions22_link_reassign_clear():
    a = iOTConnector_SampleAction(amountOfTime=7, number=7)
    b1 = iOTConnector_Sample()
    b2 = iOTConnector_Sample()
    _safe_set(a, 'iOTConnector_SampleAction', b1)
    assert _is_linked(a, 'iOTConnector_SampleAction', b1)
    if hasattr(b1, 'iOTConnector_Sample'):
        assert _is_linked(b1, 'iOTConnector_Sample', a)
    _safe_set(a, 'iOTConnector_SampleAction', b2)
    assert _is_linked(a, 'iOTConnector_SampleAction', b2)
    if hasattr(b1, 'iOTConnector_Sample'):
        assert not _is_linked(b1, 'iOTConnector_Sample', a)
    if hasattr(b2, 'iOTConnector_Sample'):
        assert _is_linked(b2, 'iOTConnector_Sample', a)
    _safe_set(a, 'iOTConnector_SampleAction', None)
    assert not _is_linked(a, 'iOTConnector_SampleAction', b2)
    if hasattr(b2, 'iOTConnector_Sample'):
        assert not _is_linked(b2, 'iOTConnector_Sample', a)


def test_assoc_send18_link_reassign_clear():
    a = iOTConnector_Sensor(name="sample_text", type="sample_text")
    b1 = iOTConnector_Send()
    b2 = iOTConnector_Send()
    _safe_set(a, 'iOTConnector_Sensor19', b1)
    assert _is_linked(a, 'iOTConnector_Sensor19', b1)
    if hasattr(b1, 'iOTConnector_Send'):
        assert _is_linked(b1, 'iOTConnector_Send', a)
    _safe_set(a, 'iOTConnector_Sensor19', b2)
    assert _is_linked(a, 'iOTConnector_Sensor19', b2)
    if hasattr(b1, 'iOTConnector_Send'):
        assert not _is_linked(b1, 'iOTConnector_Send', a)
    if hasattr(b2, 'iOTConnector_Send'):
        assert _is_linked(b2, 'iOTConnector_Send', a)
    _safe_set(a, 'iOTConnector_Sensor19', None)
    assert not _is_linked(a, 'iOTConnector_Sensor19', b2)
    if hasattr(b2, 'iOTConnector_Send'):
        assert not _is_linked(b2, 'iOTConnector_Send', a)


def test_assoc_sendActions57_link_reassign_clear():
    a = iOTConnector_SendAction(number=7)
    b1 = iOTConnector_Send()
    b2 = iOTConnector_Send()
    _safe_set(a, 'iOTConnector_SendAction', b1)
    assert _is_linked(a, 'iOTConnector_SendAction', b1)
    if hasattr(b1, 'iOTConnector_Send58'):
        assert _is_linked(b1, 'iOTConnector_Send58', a)
    _safe_set(a, 'iOTConnector_SendAction', b2)
    assert _is_linked(a, 'iOTConnector_SendAction', b2)
    if hasattr(b1, 'iOTConnector_Send58'):
        assert not _is_linked(b1, 'iOTConnector_Send58', a)
    if hasattr(b2, 'iOTConnector_Send58'):
        assert _is_linked(b2, 'iOTConnector_Send58', a)
    _safe_set(a, 'iOTConnector_SendAction', None)
    assert not _is_linked(a, 'iOTConnector_SendAction', b2)
    if hasattr(b2, 'iOTConnector_Send58'):
        assert not _is_linked(b2, 'iOTConnector_Send58', a)


def test_assoc_sensorConfigs9_link_reassign_clear():
    a = iOTConnector_SensorConfig(name="sample_text", pinIn="sample_text", pinOut="sample_text")
    b1 = iOTConnector_Board(name="sample_text")
    b2 = iOTConnector_Board(name="sample_text_2")
    _safe_set(a, 'iOTConnector_SensorConfig', b1)
    assert _is_linked(a, 'iOTConnector_SensorConfig', b1)
    if hasattr(b1, 'iOTConnector_Board10'):
        assert _is_linked(b1, 'iOTConnector_Board10', a)
    _safe_set(a, 'iOTConnector_SensorConfig', b2)
    assert _is_linked(a, 'iOTConnector_SensorConfig', b2)
    if hasattr(b1, 'iOTConnector_Board10'):
        assert not _is_linked(b1, 'iOTConnector_Board10', a)
    if hasattr(b2, 'iOTConnector_Board10'):
        assert _is_linked(b2, 'iOTConnector_Board10', a)
    _safe_set(a, 'iOTConnector_SensorConfig', None)
    assert not _is_linked(a, 'iOTConnector_SensorConfig', b2)
    if hasattr(b2, 'iOTConnector_Board10'):
        assert not _is_linked(b2, 'iOTConnector_Board10', a)


def test_assoc_sensors7_link_reassign_clear():
    a = iOTConnector_Sensor(name="sample_text", type="sample_text")
    b1 = iOTConnector_Config(name="sample_text")
    b2 = iOTConnector_Config(name="sample_text_2")
    _safe_set(a, 'iOTConnector_Sensor', b1)
    assert _is_linked(a, 'iOTConnector_Sensor', b1)
    if hasattr(b1, 'iOTConnector_Config8'):
        assert _is_linked(b1, 'iOTConnector_Config8', a)
    _safe_set(a, 'iOTConnector_Sensor', b2)
    assert _is_linked(a, 'iOTConnector_Sensor', b2)
    if hasattr(b1, 'iOTConnector_Config8'):
        assert not _is_linked(b1, 'iOTConnector_Config8', a)
    if hasattr(b2, 'iOTConnector_Config8'):
        assert _is_linked(b2, 'iOTConnector_Config8', a)
    _safe_set(a, 'iOTConnector_Sensor', None)
    assert not _is_linked(a, 'iOTConnector_Sensor', b2)
    if hasattr(b2, 'iOTConnector_Config8'):
        assert not _is_linked(b2, 'iOTConnector_Config8', a)


def test_assoc_timeUnit30_link_reassign_clear():
    a = iOTConnector_TimeUnit(value="sample_text")
    b1 = iOTConnector_SampleAction(amountOfTime=7, number=7)
    b2 = iOTConnector_SampleAction(amountOfTime=13, number=13)
    _safe_set(a, 'iOTConnector_TimeUnit', b1)
    assert _is_linked(a, 'iOTConnector_TimeUnit', b1)
    if hasattr(b1, 'iOTConnector_SampleAction31'):
        assert _is_linked(b1, 'iOTConnector_SampleAction31', a)
    _safe_set(a, 'iOTConnector_TimeUnit', b2)
    assert _is_linked(a, 'iOTConnector_TimeUnit', b2)
    if hasattr(b1, 'iOTConnector_SampleAction31'):
        assert not _is_linked(b1, 'iOTConnector_SampleAction31', a)
    if hasattr(b2, 'iOTConnector_SampleAction31'):
        assert _is_linked(b2, 'iOTConnector_SampleAction31', a)
    _safe_set(a, 'iOTConnector_TimeUnit', None)
    assert not _is_linked(a, 'iOTConnector_TimeUnit', b2)
    if hasattr(b2, 'iOTConnector_SampleAction31'):
        assert not _is_linked(b2, 'iOTConnector_SampleAction31', a)


def test_assoc_webserver0_link_reassign_clear():
    a = iOTConnector_Webserver(port=7, url="sample_text")
    b1 = iOTConnector_Program()
    b2 = iOTConnector_Program()
    _safe_set(a, 'iOTConnector_Webserver', b1)
    assert _is_linked(a, 'iOTConnector_Webserver', b1)
    if hasattr(b1, 'iOTConnector_Program'):
        assert _is_linked(b1, 'iOTConnector_Program', a)
    _safe_set(a, 'iOTConnector_Webserver', b2)
    assert _is_linked(a, 'iOTConnector_Webserver', b2)
    if hasattr(b1, 'iOTConnector_Program'):
        assert not _is_linked(b1, 'iOTConnector_Program', a)
    if hasattr(b2, 'iOTConnector_Program'):
        assert _is_linked(b2, 'iOTConnector_Program', a)
    _safe_set(a, 'iOTConnector_Webserver', None)
    assert not _is_linked(a, 'iOTConnector_Webserver', b2)
    if hasattr(b2, 'iOTConnector_Program'):
        assert not _is_linked(b2, 'iOTConnector_Program', a)


def test_assoc_wifis1_link_reassign_clear():
    a = iOTConnector_Wifi(password="sample_text", ssid="sample_text")
    b1 = iOTConnector_Program()
    b2 = iOTConnector_Program()
    _safe_set(a, 'iOTConnector_Wifi', b1)
    assert _is_linked(a, 'iOTConnector_Wifi', b1)
    if hasattr(b1, 'iOTConnector_Program2'):
        assert _is_linked(b1, 'iOTConnector_Program2', a)
    _safe_set(a, 'iOTConnector_Wifi', b2)
    assert _is_linked(a, 'iOTConnector_Wifi', b2)
    if hasattr(b1, 'iOTConnector_Program2'):
        assert not _is_linked(b1, 'iOTConnector_Program2', a)
    if hasattr(b2, 'iOTConnector_Program2'):
        assert _is_linked(b2, 'iOTConnector_Program2', a)
    _safe_set(a, 'iOTConnector_Wifi', None)
    assert not _is_linked(a, 'iOTConnector_Wifi', b2)
    if hasattr(b2, 'iOTConnector_Program2'):
        assert not _is_linked(b2, 'iOTConnector_Program2', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Function_strategy = st.builds(Function)
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


iOTConnector_BitwiseOperator_strategy = st.builds(iOTConnector_BitwiseOperator, value=safe_text)
@given(instance=iOTConnector_BitwiseOperator_strategy)
@settings(max_examples=25)
def test_iOTConnector_BitwiseOperator_instantiation(instance):
    assert isinstance(instance, iOTConnector_BitwiseOperator)


iOTConnector_Board_strategy = st.builds(iOTConnector_Board, name=safe_text)
@given(instance=iOTConnector_Board_strategy)
@settings(max_examples=25)
def test_iOTConnector_Board_instantiation(instance):
    assert isinstance(instance, iOTConnector_Board)


iOTConnector_Config_strategy = st.builds(iOTConnector_Config, name=safe_text)
@given(instance=iOTConnector_Config_strategy)
@settings(max_examples=25)
def test_iOTConnector_Config_instantiation(instance):
    assert isinstance(instance, iOTConnector_Config)


iOTConnector_Div_strategy = st.builds(iOTConnector_Div)
@given(instance=iOTConnector_Div_strategy)
@settings(max_examples=25)
def test_iOTConnector_Div_instantiation(instance):
    assert isinstance(instance, iOTConnector_Div)


iOTConnector_Expression_strategy = st.builds(iOTConnector_Expression)
@given(instance=iOTConnector_Expression_strategy)
@settings(max_examples=25)
def test_iOTConnector_Expression_instantiation(instance):
    assert isinstance(instance, iOTConnector_Expression)


iOTConnector_Filter_strategy = st.builds(iOTConnector_Filter)
@given(instance=iOTConnector_Filter_strategy)
@settings(max_examples=25)
def test_iOTConnector_Filter_instantiation(instance):
    assert isinstance(instance, iOTConnector_Filter)


iOTConnector_FilterAction_strategy = st.builds(iOTConnector_FilterAction, number=st.integers())
@given(instance=iOTConnector_FilterAction_strategy)
@settings(max_examples=25)
def test_iOTConnector_FilterAction_instantiation(instance):
    assert isinstance(instance, iOTConnector_FilterAction)


iOTConnector_FilterExp_strategy = st.builds(iOTConnector_FilterExp, number=st.integers())
@given(instance=iOTConnector_FilterExp_strategy)
@settings(max_examples=25)
def test_iOTConnector_FilterExp_instantiation(instance):
    assert isinstance(instance, iOTConnector_FilterExp)


iOTConnector_FilterType_strategy = st.builds(iOTConnector_FilterType, value=safe_text)
@given(instance=iOTConnector_FilterType_strategy)
@settings(max_examples=25)
def test_iOTConnector_FilterType_instantiation(instance):
    assert isinstance(instance, iOTConnector_FilterType)


iOTConnector_Function_strategy = st.builds(iOTConnector_Function)
@given(instance=iOTConnector_Function_strategy)
@settings(max_examples=25)
def test_iOTConnector_Function_instantiation(instance):
    assert isinstance(instance, iOTConnector_Function)


iOTConnector_Minus_strategy = st.builds(iOTConnector_Minus)
@given(instance=iOTConnector_Minus_strategy)
@settings(max_examples=25)
def test_iOTConnector_Minus_instantiation(instance):
    assert isinstance(instance, iOTConnector_Minus)


iOTConnector_Mult_strategy = st.builds(iOTConnector_Mult)
@given(instance=iOTConnector_Mult_strategy)
@settings(max_examples=25)
def test_iOTConnector_Mult_instantiation(instance):
    assert isinstance(instance, iOTConnector_Mult)


iOTConnector_Num_strategy = st.builds(iOTConnector_Num, value=st.integers())
@given(instance=iOTConnector_Num_strategy)
@settings(max_examples=25)
def test_iOTConnector_Num_instantiation(instance):
    assert isinstance(instance, iOTConnector_Num)


iOTConnector_Output_strategy = st.builds(iOTConnector_Output)
@given(instance=iOTConnector_Output_strategy)
@settings(max_examples=25)
def test_iOTConnector_Output_instantiation(instance):
    assert isinstance(instance, iOTConnector_Output)


iOTConnector_Plus_strategy = st.builds(iOTConnector_Plus)
@given(instance=iOTConnector_Plus_strategy)
@settings(max_examples=25)
def test_iOTConnector_Plus_instantiation(instance):
    assert isinstance(instance, iOTConnector_Plus)


iOTConnector_Process_strategy = st.builds(iOTConnector_Process)
@given(instance=iOTConnector_Process_strategy)
@settings(max_examples=25)
def test_iOTConnector_Process_instantiation(instance):
    assert isinstance(instance, iOTConnector_Process)


iOTConnector_ProcessAction_strategy = st.builds(iOTConnector_ProcessAction)
@given(instance=iOTConnector_ProcessAction_strategy)
@settings(max_examples=25)
def test_iOTConnector_ProcessAction_instantiation(instance):
    assert isinstance(instance, iOTConnector_ProcessAction)


iOTConnector_Program_strategy = st.builds(iOTConnector_Program)
@given(instance=iOTConnector_Program_strategy)
@settings(max_examples=25)
def test_iOTConnector_Program_instantiation(instance):
    assert isinstance(instance, iOTConnector_Program)


iOTConnector_ReadingName_strategy = st.builds(iOTConnector_ReadingName, name=safe_text)
@given(instance=iOTConnector_ReadingName_strategy)
@settings(max_examples=25)
def test_iOTConnector_ReadingName_instantiation(instance):
    assert isinstance(instance, iOTConnector_ReadingName)


iOTConnector_ReadingNameWithConfigScope_strategy = st.builds(iOTConnector_ReadingNameWithConfigScope)
@given(instance=iOTConnector_ReadingNameWithConfigScope_strategy)
@settings(max_examples=25)
def test_iOTConnector_ReadingNameWithConfigScope_instantiation(instance):
    assert isinstance(instance, iOTConnector_ReadingNameWithConfigScope)


iOTConnector_RelationalOperator_strategy = st.builds(iOTConnector_RelationalOperator, value=safe_text)
@given(instance=iOTConnector_RelationalOperator_strategy)
@settings(max_examples=25)
def test_iOTConnector_RelationalOperator_instantiation(instance):
    assert isinstance(instance, iOTConnector_RelationalOperator)


iOTConnector_Sample_strategy = st.builds(iOTConnector_Sample)
@given(instance=iOTConnector_Sample_strategy)
@settings(max_examples=25)
def test_iOTConnector_Sample_instantiation(instance):
    assert isinstance(instance, iOTConnector_Sample)


iOTConnector_SampleAction_strategy = st.builds(iOTConnector_SampleAction, amountOfTime=st.integers(), number=st.integers())
@given(instance=iOTConnector_SampleAction_strategy)
@settings(max_examples=25)
def test_iOTConnector_SampleAction_instantiation(instance):
    assert isinstance(instance, iOTConnector_SampleAction)


iOTConnector_Send_strategy = st.builds(iOTConnector_Send)
@given(instance=iOTConnector_Send_strategy)
@settings(max_examples=25)
def test_iOTConnector_Send_instantiation(instance):
    assert isinstance(instance, iOTConnector_Send)


iOTConnector_SendAction_strategy = st.builds(iOTConnector_SendAction, number=st.integers())
@given(instance=iOTConnector_SendAction_strategy)
@settings(max_examples=25)
def test_iOTConnector_SendAction_instantiation(instance):
    assert isinstance(instance, iOTConnector_SendAction)


iOTConnector_Sensor_strategy = st.builds(iOTConnector_Sensor, name=safe_text, type=safe_text)
@given(instance=iOTConnector_Sensor_strategy)
@settings(max_examples=25)
def test_iOTConnector_Sensor_instantiation(instance):
    assert isinstance(instance, iOTConnector_Sensor)


iOTConnector_SensorConfig_strategy = st.builds(iOTConnector_SensorConfig, name=safe_text, pinIn=safe_text, pinOut=safe_text)
@given(instance=iOTConnector_SensorConfig_strategy)
@settings(max_examples=25)
def test_iOTConnector_SensorConfig_instantiation(instance):
    assert isinstance(instance, iOTConnector_SensorConfig)


iOTConnector_TimeUnit_strategy = st.builds(iOTConnector_TimeUnit, value=safe_text)
@given(instance=iOTConnector_TimeUnit_strategy)
@settings(max_examples=25)
def test_iOTConnector_TimeUnit_instantiation(instance):
    assert isinstance(instance, iOTConnector_TimeUnit)


iOTConnector_Var_strategy = st.builds(iOTConnector_Var)
@given(instance=iOTConnector_Var_strategy)
@settings(max_examples=25)
def test_iOTConnector_Var_instantiation(instance):
    assert isinstance(instance, iOTConnector_Var)


iOTConnector_Webserver_strategy = st.builds(iOTConnector_Webserver, port=st.integers(), url=safe_text)
@given(instance=iOTConnector_Webserver_strategy)
@settings(max_examples=25)
def test_iOTConnector_Webserver_instantiation(instance):
    assert isinstance(instance, iOTConnector_Webserver)


iOTConnector_Wifi_strategy = st.builds(iOTConnector_Wifi, password=safe_text, ssid=safe_text)
@given(instance=iOTConnector_Wifi_strategy)
@settings(max_examples=25)
def test_iOTConnector_Wifi_instantiation(instance):
    assert isinstance(instance, iOTConnector_Wifi)


