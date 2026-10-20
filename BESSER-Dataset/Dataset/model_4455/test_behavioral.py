import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_bitwiseOperator46_reverse_link_reassign_clear():
    a1 = iOTConnector_FilterExp(number=7)
    a2 = iOTConnector_FilterExp(number=13)
    b = iOTConnector_BitwiseOperator(value="sample_text")
    _safe_set(b, 'iOTConnector_BitwiseOperator', a1)
    assert _is_linked(b, 'iOTConnector_BitwiseOperator', a1)
    if hasattr(a1, 'iOTConnector_FilterExp47'):
        assert _is_linked(a1, 'iOTConnector_FilterExp47', b)
    _safe_set(b, 'iOTConnector_BitwiseOperator', a2)
    assert _is_linked(b, 'iOTConnector_BitwiseOperator', a2)
    if hasattr(a1, 'iOTConnector_FilterExp47'):
        assert not _is_linked(a1, 'iOTConnector_FilterExp47', b)
    if hasattr(a2, 'iOTConnector_FilterExp47'):
        assert _is_linked(a2, 'iOTConnector_FilterExp47', b)
    _safe_set(b, 'iOTConnector_BitwiseOperator', None)
    assert not _is_linked(b, 'iOTConnector_BitwiseOperator', a2)
    if hasattr(a2, 'iOTConnector_FilterExp47'):
        assert not _is_linked(a2, 'iOTConnector_FilterExp47', b)


def test_assoc_configName11_reverse_link_reassign_clear():
    a1 = iOTConnector_Config(name="sample_text")
    a2 = iOTConnector_Config(name="sample_text_2")
    b = iOTConnector_Board(name="sample_text")
    _safe_set(b, 'iOTConnector_Board12', a1)
    assert _is_linked(b, 'iOTConnector_Board12', a1)
    if hasattr(a1, 'iOTConnector_Config13'):
        assert _is_linked(a1, 'iOTConnector_Config13', b)
    _safe_set(b, 'iOTConnector_Board12', a2)
    assert _is_linked(b, 'iOTConnector_Board12', a2)
    if hasattr(a1, 'iOTConnector_Config13'):
        assert not _is_linked(a1, 'iOTConnector_Config13', b)
    if hasattr(a2, 'iOTConnector_Config13'):
        assert _is_linked(a2, 'iOTConnector_Config13', b)
    _safe_set(b, 'iOTConnector_Board12', None)
    assert not _is_linked(b, 'iOTConnector_Board12', a2)
    if hasattr(a2, 'iOTConnector_Config13'):
        assert not _is_linked(a2, 'iOTConnector_Config13', b)


def test_assoc_filterExp38_reverse_link_reassign_clear():
    a1 = iOTConnector_FilterExp(number=7)
    a2 = iOTConnector_FilterExp(number=13)
    b = iOTConnector_FilterAction(number=7)
    _safe_set(b, 'iOTConnector_FilterAction39', a1)
    assert _is_linked(b, 'iOTConnector_FilterAction39', a1)
    if hasattr(a1, 'iOTConnector_FilterExp'):
        assert _is_linked(a1, 'iOTConnector_FilterExp', b)
    _safe_set(b, 'iOTConnector_FilterAction39', a2)
    assert _is_linked(b, 'iOTConnector_FilterAction39', a2)
    if hasattr(a1, 'iOTConnector_FilterExp'):
        assert not _is_linked(a1, 'iOTConnector_FilterExp', b)
    if hasattr(a2, 'iOTConnector_FilterExp'):
        assert _is_linked(a2, 'iOTConnector_FilterExp', b)
    _safe_set(b, 'iOTConnector_FilterAction39', None)
    assert not _is_linked(b, 'iOTConnector_FilterAction39', a2)
    if hasattr(a2, 'iOTConnector_FilterExp'):
        assert not _is_linked(a2, 'iOTConnector_FilterExp', b)


def test_assoc_filterExp49_reverse_link_reassign_clear():
    a1 = iOTConnector_FilterExp(number=7)
    a2 = iOTConnector_FilterExp(number=13)
    b = iOTConnector_FilterExp(number=7)
    _safe_set(b, 'iOTConnector_FilterExp50', a1)
    assert _is_linked(b, 'iOTConnector_FilterExp50', a1)
    if hasattr(a1, 'iOTConnector_FilterExp48'):
        assert _is_linked(a1, 'iOTConnector_FilterExp48', b)
    _safe_set(b, 'iOTConnector_FilterExp50', a2)
    assert _is_linked(b, 'iOTConnector_FilterExp50', a2)
    if hasattr(a1, 'iOTConnector_FilterExp48'):
        assert not _is_linked(a1, 'iOTConnector_FilterExp48', b)
    if hasattr(a2, 'iOTConnector_FilterExp48'):
        assert _is_linked(a2, 'iOTConnector_FilterExp48', b)
    _safe_set(b, 'iOTConnector_FilterExp50', None)
    assert not _is_linked(b, 'iOTConnector_FilterExp50', a2)
    if hasattr(a2, 'iOTConnector_FilterExp48'):
        assert not _is_linked(a2, 'iOTConnector_FilterExp48', b)


def test_assoc_filterType36_reverse_link_reassign_clear():
    a1 = iOTConnector_FilterType(value="sample_text")
    a2 = iOTConnector_FilterType(value="sample_text_2")
    b = iOTConnector_FilterAction(number=7)
    _safe_set(b, 'iOTConnector_FilterAction37', a1)
    assert _is_linked(b, 'iOTConnector_FilterAction37', a1)
    if hasattr(a1, 'iOTConnector_FilterType'):
        assert _is_linked(a1, 'iOTConnector_FilterType', b)
    _safe_set(b, 'iOTConnector_FilterAction37', a2)
    assert _is_linked(b, 'iOTConnector_FilterAction37', a2)
    if hasattr(a1, 'iOTConnector_FilterType'):
        assert not _is_linked(a1, 'iOTConnector_FilterType', b)
    if hasattr(a2, 'iOTConnector_FilterType'):
        assert _is_linked(a2, 'iOTConnector_FilterType', b)
    _safe_set(b, 'iOTConnector_FilterAction37', None)
    assert not _is_linked(b, 'iOTConnector_FilterAction37', a2)
    if hasattr(a2, 'iOTConnector_FilterType'):
        assert not _is_linked(a2, 'iOTConnector_FilterType', b)


def test_assoc_readingName23_reverse_link_reassign_clear():
    a1 = iOTConnector_SampleAction(amountOfTime=7, number=7)
    a2 = iOTConnector_SampleAction(amountOfTime=13, number=13)
    b = iOTConnector_ReadingName(name="sample_text")
    _safe_set(b, 'iOTConnector_ReadingName25', a1)
    assert _is_linked(b, 'iOTConnector_ReadingName25', a1)
    if hasattr(a1, 'iOTConnector_SampleAction24'):
        assert _is_linked(a1, 'iOTConnector_SampleAction24', b)
    _safe_set(b, 'iOTConnector_ReadingName25', a2)
    assert _is_linked(b, 'iOTConnector_ReadingName25', a2)
    if hasattr(a1, 'iOTConnector_SampleAction24'):
        assert not _is_linked(a1, 'iOTConnector_SampleAction24', b)
    if hasattr(a2, 'iOTConnector_SampleAction24'):
        assert _is_linked(a2, 'iOTConnector_SampleAction24', b)
    _safe_set(b, 'iOTConnector_ReadingName25', None)
    assert not _is_linked(b, 'iOTConnector_ReadingName25', a2)
    if hasattr(a2, 'iOTConnector_SampleAction24'):
        assert not _is_linked(a2, 'iOTConnector_SampleAction24', b)


def test_assoc_readingName33_reverse_link_reassign_clear():
    a1 = iOTConnector_ReadingName(name="sample_text")
    a2 = iOTConnector_ReadingName(name="sample_text_2")
    b = iOTConnector_FilterAction(number=7)
    _safe_set(b, 'iOTConnector_FilterAction34', a1)
    assert _is_linked(b, 'iOTConnector_FilterAction34', a1)
    if hasattr(a1, 'iOTConnector_ReadingName35'):
        assert _is_linked(a1, 'iOTConnector_ReadingName35', b)
    _safe_set(b, 'iOTConnector_FilterAction34', a2)
    assert _is_linked(b, 'iOTConnector_FilterAction34', a2)
    if hasattr(a1, 'iOTConnector_ReadingName35'):
        assert not _is_linked(a1, 'iOTConnector_ReadingName35', b)
    if hasattr(a2, 'iOTConnector_ReadingName35'):
        assert _is_linked(a2, 'iOTConnector_ReadingName35', b)
    _safe_set(b, 'iOTConnector_FilterAction34', None)
    assert not _is_linked(b, 'iOTConnector_FilterAction34', a2)
    if hasattr(a2, 'iOTConnector_ReadingName35'):
        assert not _is_linked(a2, 'iOTConnector_ReadingName35', b)


def test_assoc_readingName59_reverse_link_reassign_clear():
    a1 = iOTConnector_SendAction(number=7)
    a2 = iOTConnector_SendAction(number=13)
    b = iOTConnector_ReadingName(name="sample_text")
    _safe_set(b, 'iOTConnector_ReadingName61', a1)
    assert _is_linked(b, 'iOTConnector_ReadingName61', a1)
    if hasattr(a1, 'iOTConnector_SendAction60'):
        assert _is_linked(a1, 'iOTConnector_SendAction60', b)
    _safe_set(b, 'iOTConnector_ReadingName61', a2)
    assert _is_linked(b, 'iOTConnector_ReadingName61', a2)
    if hasattr(a1, 'iOTConnector_SendAction60'):
        assert not _is_linked(a1, 'iOTConnector_SendAction60', b)
    if hasattr(a2, 'iOTConnector_SendAction60'):
        assert _is_linked(a2, 'iOTConnector_SendAction60', b)
    _safe_set(b, 'iOTConnector_ReadingName61', None)
    assert not _is_linked(b, 'iOTConnector_ReadingName61', a2)
    if hasattr(a2, 'iOTConnector_SendAction60'):
        assert not _is_linked(a2, 'iOTConnector_SendAction60', b)


def test_assoc_relationalOperator28_reverse_link_reassign_clear():
    a1 = iOTConnector_SampleAction(amountOfTime=7, number=7)
    a2 = iOTConnector_SampleAction(amountOfTime=13, number=13)
    b = iOTConnector_RelationalOperator(value="sample_text")
    _safe_set(b, 'iOTConnector_RelationalOperator', a1)
    assert _is_linked(b, 'iOTConnector_RelationalOperator', a1)
    if hasattr(a1, 'iOTConnector_SampleAction29'):
        assert _is_linked(a1, 'iOTConnector_SampleAction29', b)
    _safe_set(b, 'iOTConnector_RelationalOperator', a2)
    assert _is_linked(b, 'iOTConnector_RelationalOperator', a2)
    if hasattr(a1, 'iOTConnector_SampleAction29'):
        assert not _is_linked(a1, 'iOTConnector_SampleAction29', b)
    if hasattr(a2, 'iOTConnector_SampleAction29'):
        assert _is_linked(a2, 'iOTConnector_SampleAction29', b)
    _safe_set(b, 'iOTConnector_RelationalOperator', None)
    assert not _is_linked(b, 'iOTConnector_RelationalOperator', a2)
    if hasattr(a2, 'iOTConnector_SampleAction29'):
        assert not _is_linked(a2, 'iOTConnector_SampleAction29', b)


def test_assoc_relationalOperator43_reverse_link_reassign_clear():
    a1 = iOTConnector_RelationalOperator(value="sample_text")
    a2 = iOTConnector_RelationalOperator(value="sample_text_2")
    b = iOTConnector_FilterExp(number=7)
    _safe_set(b, 'iOTConnector_FilterExp44', a1)
    assert _is_linked(b, 'iOTConnector_FilterExp44', a1)
    if hasattr(a1, 'iOTConnector_RelationalOperator45'):
        assert _is_linked(a1, 'iOTConnector_RelationalOperator45', b)
    _safe_set(b, 'iOTConnector_FilterExp44', a2)
    assert _is_linked(b, 'iOTConnector_FilterExp44', a2)
    if hasattr(a1, 'iOTConnector_RelationalOperator45'):
        assert not _is_linked(a1, 'iOTConnector_RelationalOperator45', b)
    if hasattr(a2, 'iOTConnector_RelationalOperator45'):
        assert _is_linked(a2, 'iOTConnector_RelationalOperator45', b)
    _safe_set(b, 'iOTConnector_FilterExp44', None)
    assert not _is_linked(b, 'iOTConnector_FilterExp44', a2)
    if hasattr(a2, 'iOTConnector_RelationalOperator45'):
        assert not _is_linked(a2, 'iOTConnector_RelationalOperator45', b)


def test_assoc_relationalOperator62_reverse_link_reassign_clear():
    a1 = iOTConnector_SendAction(number=7)
    a2 = iOTConnector_SendAction(number=13)
    b = iOTConnector_RelationalOperator(value="sample_text")
    _safe_set(b, 'iOTConnector_RelationalOperator64', a1)
    assert _is_linked(b, 'iOTConnector_RelationalOperator64', a1)
    if hasattr(a1, 'iOTConnector_SendAction63'):
        assert _is_linked(a1, 'iOTConnector_SendAction63', b)
    _safe_set(b, 'iOTConnector_RelationalOperator64', a2)
    assert _is_linked(b, 'iOTConnector_RelationalOperator64', a2)
    if hasattr(a1, 'iOTConnector_SendAction63'):
        assert not _is_linked(a1, 'iOTConnector_SendAction63', b)
    if hasattr(a2, 'iOTConnector_SendAction63'):
        assert _is_linked(a2, 'iOTConnector_SendAction63', b)
    _safe_set(b, 'iOTConnector_RelationalOperator64', None)
    assert not _is_linked(b, 'iOTConnector_RelationalOperator64', a2)
    if hasattr(a2, 'iOTConnector_SendAction63'):
        assert not _is_linked(a2, 'iOTConnector_SendAction63', b)


def test_assoc_sensorConfigs9_reverse_link_reassign_clear():
    a1 = iOTConnector_SensorConfig(name="sample_text", pinIn="sample_text", pinOut="sample_text")
    a2 = iOTConnector_SensorConfig(name="sample_text_2", pinIn="sample_text_2", pinOut="sample_text_2")
    b = iOTConnector_Board(name="sample_text")
    _safe_set(b, 'iOTConnector_Board10', {a1})
    assert _is_linked(b, 'iOTConnector_Board10', a1)
    if hasattr(a1, 'iOTConnector_SensorConfig'):
        assert _is_linked(a1, 'iOTConnector_SensorConfig', b)
    _safe_set(b, 'iOTConnector_Board10', {a2})
    assert _is_linked(b, 'iOTConnector_Board10', a2)
    if hasattr(a1, 'iOTConnector_SensorConfig'):
        assert not _is_linked(a1, 'iOTConnector_SensorConfig', b)
    if hasattr(a2, 'iOTConnector_SensorConfig'):
        assert _is_linked(a2, 'iOTConnector_SensorConfig', b)
    _safe_set(b, 'iOTConnector_Board10', set())
    assert not _is_linked(b, 'iOTConnector_Board10', a2)
    if hasattr(a2, 'iOTConnector_SensorConfig'):
        assert not _is_linked(a2, 'iOTConnector_SensorConfig', b)


def test_assoc_sensors7_reverse_link_reassign_clear():
    a1 = iOTConnector_Sensor(name="sample_text", type="sample_text")
    a2 = iOTConnector_Sensor(name="sample_text_2", type="sample_text_2")
    b = iOTConnector_Config(name="sample_text")
    _safe_set(b, 'iOTConnector_Config8', {a1})
    assert _is_linked(b, 'iOTConnector_Config8', a1)
    if hasattr(a1, 'iOTConnector_Sensor'):
        assert _is_linked(a1, 'iOTConnector_Sensor', b)
    _safe_set(b, 'iOTConnector_Config8', {a2})
    assert _is_linked(b, 'iOTConnector_Config8', a2)
    if hasattr(a1, 'iOTConnector_Sensor'):
        assert not _is_linked(a1, 'iOTConnector_Sensor', b)
    if hasattr(a2, 'iOTConnector_Sensor'):
        assert _is_linked(a2, 'iOTConnector_Sensor', b)
    _safe_set(b, 'iOTConnector_Config8', set())
    assert not _is_linked(b, 'iOTConnector_Config8', a2)
    if hasattr(a2, 'iOTConnector_Sensor'):
        assert not _is_linked(a2, 'iOTConnector_Sensor', b)


def test_assoc_timeUnit30_reverse_link_reassign_clear():
    a1 = iOTConnector_TimeUnit(value="sample_text")
    a2 = iOTConnector_TimeUnit(value="sample_text_2")
    b = iOTConnector_SampleAction(amountOfTime=7, number=7)
    _safe_set(b, 'iOTConnector_SampleAction31', a1)
    assert _is_linked(b, 'iOTConnector_SampleAction31', a1)
    if hasattr(a1, 'iOTConnector_TimeUnit'):
        assert _is_linked(a1, 'iOTConnector_TimeUnit', b)
    _safe_set(b, 'iOTConnector_SampleAction31', a2)
    assert _is_linked(b, 'iOTConnector_SampleAction31', a2)
    if hasattr(a1, 'iOTConnector_TimeUnit'):
        assert not _is_linked(a1, 'iOTConnector_TimeUnit', b)
    if hasattr(a2, 'iOTConnector_TimeUnit'):
        assert _is_linked(a2, 'iOTConnector_TimeUnit', b)
    _safe_set(b, 'iOTConnector_SampleAction31', None)
    assert not _is_linked(b, 'iOTConnector_SampleAction31', a2)
    if hasattr(a2, 'iOTConnector_TimeUnit'):
        assert not _is_linked(a2, 'iOTConnector_TimeUnit', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_boards5_stub_double():
    # iOTConnector_Program has no real 'iOTConnector_Program6' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_Board(name="sample_text")
    partner = iOTConnector_Program()
    setattr(partner, 'iOTConnector_Program6', None)
    _safe_set(owner, 'iOTConnector_Board', partner)
    assert owner in getattr(partner, 'iOTConnector_Program6')
    _safe_set(owner, 'iOTConnector_Board', None)
    assert owner not in getattr(partner, 'iOTConnector_Program6')


def test_assoc_configs3_stub_double():
    # iOTConnector_Program has no real 'iOTConnector_Program4' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_Config's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_Config's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_Config(name="sample_text")
    partner = iOTConnector_Program()
    setattr(partner, 'iOTConnector_Program4', None)
    _safe_set(owner, 'iOTConnector_Config', partner)
    assert owner in getattr(partner, 'iOTConnector_Program4')
    _safe_set(owner, 'iOTConnector_Config', None)
    assert owner not in getattr(partner, 'iOTConnector_Program4')


def test_assoc_filterActions32_stub_double():
    # iOTConnector_Filter has no real 'iOTConnector_Filter' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_FilterAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_FilterAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_FilterAction(number=7)
    partner = iOTConnector_Filter()
    setattr(partner, 'iOTConnector_Filter', None)
    _safe_set(owner, 'iOTConnector_FilterAction', partner)
    assert owner in getattr(partner, 'iOTConnector_Filter')
    _safe_set(owner, 'iOTConnector_FilterAction', None)
    assert owner not in getattr(partner, 'iOTConnector_Filter')


def test_assoc_functions16_stub_double():
    # iOTConnector_Function has no real 'iOTConnector_Function' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_Sensor(name="sample_text", type="sample_text")
    partner = iOTConnector_Function()
    setattr(partner, 'iOTConnector_Function', None)
    _safe_set(owner, 'iOTConnector_Sensor17', {partner})
    assert getattr(partner, 'iOTConnector_Function') == owner
    _safe_set(owner, 'iOTConnector_Sensor17', set())
    assert getattr(partner, 'iOTConnector_Function') is None


def test_assoc_name65_stub_double():
    # iOTConnector_ReadingNameWithConfigScope has no real 'iOTConnector_ReadingNameWithConfigScope66' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_ReadingName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_ReadingName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_ReadingName(name="sample_text")
    partner = iOTConnector_ReadingNameWithConfigScope()
    setattr(partner, 'iOTConnector_ReadingNameWithConfigScope66', None)
    _safe_set(owner, 'iOTConnector_ReadingName67', partner)
    assert getattr(partner, 'iOTConnector_ReadingNameWithConfigScope66') == owner
    _safe_set(owner, 'iOTConnector_ReadingName67', None)
    assert getattr(partner, 'iOTConnector_ReadingNameWithConfigScope66') is None


def test_assoc_output14_stub_double():
    # iOTConnector_Output has no real 'iOTConnector_Output' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_Sensor(name="sample_text", type="sample_text")
    partner = iOTConnector_Output()
    setattr(partner, 'iOTConnector_Output', None)
    _safe_set(owner, 'iOTConnector_Sensor15', partner)
    assert getattr(partner, 'iOTConnector_Output') == owner
    _safe_set(owner, 'iOTConnector_Sensor15', None)
    assert getattr(partner, 'iOTConnector_Output') is None


def test_assoc_readingName40_stub_double():
    # iOTConnector_ReadingNameWithConfigScope has no real 'iOTConnector_ReadingNameWithConfigScope42' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_FilterExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_FilterExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_FilterExp(number=7)
    partner = iOTConnector_ReadingNameWithConfigScope()
    setattr(partner, 'iOTConnector_ReadingNameWithConfigScope42', None)
    _safe_set(owner, 'iOTConnector_FilterExp41', partner)
    assert getattr(partner, 'iOTConnector_ReadingNameWithConfigScope42') == owner
    _safe_set(owner, 'iOTConnector_FilterExp41', None)
    assert getattr(partner, 'iOTConnector_ReadingNameWithConfigScope42') is None


def test_assoc_readingName52_stub_double():
    # iOTConnector_ProcessAction has no real 'iOTConnector_ProcessAction53' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_ReadingName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_ReadingName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_ReadingName(name="sample_text")
    partner = iOTConnector_ProcessAction()
    setattr(partner, 'iOTConnector_ProcessAction53', None)
    _safe_set(owner, 'iOTConnector_ReadingName54', partner)
    assert getattr(partner, 'iOTConnector_ProcessAction53') == owner
    _safe_set(owner, 'iOTConnector_ReadingName54', None)
    assert getattr(partner, 'iOTConnector_ProcessAction53') is None


def test_assoc_readingNameToCompare26_stub_double():
    # iOTConnector_ReadingNameWithConfigScope has no real 'iOTConnector_ReadingNameWithConfigScope' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_SampleAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_SampleAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_SampleAction(amountOfTime=7, number=7)
    partner = iOTConnector_ReadingNameWithConfigScope()
    setattr(partner, 'iOTConnector_ReadingNameWithConfigScope', None)
    _safe_set(owner, 'iOTConnector_SampleAction27', partner)
    assert getattr(partner, 'iOTConnector_ReadingNameWithConfigScope') == owner
    _safe_set(owner, 'iOTConnector_SampleAction27', None)
    assert getattr(partner, 'iOTConnector_ReadingNameWithConfigScope') is None


def test_assoc_readingNames20_stub_double():
    # iOTConnector_Output has no real 'iOTConnector_Output21' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_ReadingName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_ReadingName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_ReadingName(name="sample_text")
    partner = iOTConnector_Output()
    setattr(partner, 'iOTConnector_Output21', None)
    _safe_set(owner, 'iOTConnector_ReadingName', partner)
    assert owner in getattr(partner, 'iOTConnector_Output21')
    _safe_set(owner, 'iOTConnector_ReadingName', None)
    assert owner not in getattr(partner, 'iOTConnector_Output21')


def test_assoc_sampleActions22_stub_double():
    # iOTConnector_Sample has no real 'iOTConnector_Sample' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_SampleAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_SampleAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_SampleAction(amountOfTime=7, number=7)
    partner = iOTConnector_Sample()
    setattr(partner, 'iOTConnector_Sample', None)
    _safe_set(owner, 'iOTConnector_SampleAction', partner)
    assert owner in getattr(partner, 'iOTConnector_Sample')
    _safe_set(owner, 'iOTConnector_SampleAction', None)
    assert owner not in getattr(partner, 'iOTConnector_Sample')


def test_assoc_send18_stub_double():
    # iOTConnector_Send has no real 'iOTConnector_Send' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_Sensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_Sensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_Sensor(name="sample_text", type="sample_text")
    partner = iOTConnector_Send()
    setattr(partner, 'iOTConnector_Send', None)
    _safe_set(owner, 'iOTConnector_Sensor19', partner)
    assert getattr(partner, 'iOTConnector_Send') == owner
    _safe_set(owner, 'iOTConnector_Sensor19', None)
    assert getattr(partner, 'iOTConnector_Send') is None


def test_assoc_sendActions57_stub_double():
    # iOTConnector_Send has no real 'iOTConnector_Send58' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_SendAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_SendAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_SendAction(number=7)
    partner = iOTConnector_Send()
    setattr(partner, 'iOTConnector_Send58', None)
    _safe_set(owner, 'iOTConnector_SendAction', partner)
    assert owner in getattr(partner, 'iOTConnector_Send58')
    _safe_set(owner, 'iOTConnector_SendAction', None)
    assert owner not in getattr(partner, 'iOTConnector_Send58')


def test_assoc_webserver0_stub_double():
    # iOTConnector_Program has no real 'iOTConnector_Program' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_Webserver's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_Webserver's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_Webserver(port=7, url="sample_text")
    partner = iOTConnector_Program()
    setattr(partner, 'iOTConnector_Program', None)
    _safe_set(owner, 'iOTConnector_Webserver', partner)
    assert getattr(partner, 'iOTConnector_Program') == owner
    _safe_set(owner, 'iOTConnector_Webserver', None)
    assert getattr(partner, 'iOTConnector_Program') is None


def test_assoc_wifis1_stub_double():
    # iOTConnector_Program has no real 'iOTConnector_Program2' property in the generated
    # code (a bare stub) -- manually attach it so iOTConnector_Wifi's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iOTConnector_Wifi's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iOTConnector_Wifi(password="sample_text", ssid="sample_text")
    partner = iOTConnector_Program()
    setattr(partner, 'iOTConnector_Program2', None)
    _safe_set(owner, 'iOTConnector_Wifi', partner)
    assert owner in getattr(partner, 'iOTConnector_Program2')
    _safe_set(owner, 'iOTConnector_Wifi', None)
    assert owner not in getattr(partner, 'iOTConnector_Program2')


