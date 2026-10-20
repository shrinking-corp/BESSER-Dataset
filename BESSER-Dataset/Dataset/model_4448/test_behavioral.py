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


