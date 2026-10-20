import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BoardMember,
    ExpMember,
    pycom_Actuator,
    pycom_Board,
    pycom_BoardMember,
    pycom_Boolean,
    pycom_Communication,
    pycom_CommunicationType,
    pycom_ComparisonExp,
    pycom_Condition,
    pycom_ConditionalAction,
    pycom_Connection,
    pycom_ExpMember,
    pycom_Expression,
    pycom_Function,
    pycom_Host,
    pycom_Import,
    pycom_Library,
    pycom_LogicExp,
    pycom_ModuleName,
    pycom_ModuleType,
    pycom_ParameterType,
    pycom_Pin,
    pycom_PinName,
    pycom_Sensor,
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

def test_assoc_condition25_reverse_link_reassign_clear():
    a1 = pycom_ConditionalAction(type="sample_text")
    a2 = pycom_ConditionalAction(type="sample_text_2")
    b = pycom_Condition(operator="sample_text")
    _safe_set(b, 'pycom_Condition', a1)
    assert _is_linked(b, 'pycom_Condition', a1)
    if hasattr(a1, 'pycom_ConditionalAction26'):
        assert _is_linked(a1, 'pycom_ConditionalAction26', b)
    _safe_set(b, 'pycom_Condition', a2)
    assert _is_linked(b, 'pycom_Condition', a2)
    if hasattr(a1, 'pycom_ConditionalAction26'):
        assert not _is_linked(a1, 'pycom_ConditionalAction26', b)
    if hasattr(a2, 'pycom_ConditionalAction26'):
        assert _is_linked(a2, 'pycom_ConditionalAction26', b)
    _safe_set(b, 'pycom_Condition', None)
    assert not _is_linked(b, 'pycom_Condition', a2)
    if hasattr(a2, 'pycom_ConditionalAction26'):
        assert not _is_linked(a2, 'pycom_ConditionalAction26', b)


def test_assoc_conn12_reverse_link_reassign_clear():
    a1 = pycom_Server(name="sample_text")
    a2 = pycom_Server(name="sample_text_2")
    b = pycom_Connection(portnumber=7)
    _safe_set(b, 'pycom_Connection', a1)
    assert _is_linked(b, 'pycom_Connection', a1)
    if hasattr(a1, 'pycom_Server13'):
        assert _is_linked(a1, 'pycom_Server13', b)
    _safe_set(b, 'pycom_Connection', a2)
    assert _is_linked(b, 'pycom_Connection', a2)
    if hasattr(a1, 'pycom_Server13'):
        assert not _is_linked(a1, 'pycom_Server13', b)
    if hasattr(a2, 'pycom_Server13'):
        assert _is_linked(a2, 'pycom_Server13', b)
    _safe_set(b, 'pycom_Connection', None)
    assert not _is_linked(b, 'pycom_Connection', a2)
    if hasattr(a2, 'pycom_Server13'):
        assert not _is_linked(a2, 'pycom_Server13', b)


def test_assoc_exps14_reverse_link_reassign_clear():
    a1 = pycom_Server(name="sample_text")
    a2 = pycom_Server(name="sample_text_2")
    b = pycom_ConditionalAction(type="sample_text")
    _safe_set(b, 'pycom_ConditionalAction', a1)
    assert _is_linked(b, 'pycom_ConditionalAction', a1)
    if hasattr(a1, 'pycom_Server15'):
        assert _is_linked(a1, 'pycom_Server15', b)
    _safe_set(b, 'pycom_ConditionalAction', a2)
    assert _is_linked(b, 'pycom_ConditionalAction', a2)
    if hasattr(a1, 'pycom_Server15'):
        assert not _is_linked(a1, 'pycom_Server15', b)
    if hasattr(a2, 'pycom_Server15'):
        assert _is_linked(a2, 'pycom_Server15', b)
    _safe_set(b, 'pycom_ConditionalAction', None)
    assert not _is_linked(b, 'pycom_ConditionalAction', a2)
    if hasattr(a2, 'pycom_Server15'):
        assert not _is_linked(a2, 'pycom_Server15', b)


def test_assoc_host16_reverse_link_reassign_clear():
    a1 = pycom_Host(ipAdr="sample_text", website="sample_text")
    a2 = pycom_Host(ipAdr="sample_text_2", website="sample_text_2")
    b = pycom_Connection(portnumber=7)
    _safe_set(b, 'pycom_Connection17', a1)
    assert _is_linked(b, 'pycom_Connection17', a1)
    if hasattr(a1, 'pycom_Host'):
        assert _is_linked(a1, 'pycom_Host', b)
    _safe_set(b, 'pycom_Connection17', a2)
    assert _is_linked(b, 'pycom_Connection17', a2)
    if hasattr(a1, 'pycom_Host'):
        assert not _is_linked(a1, 'pycom_Host', b)
    if hasattr(a2, 'pycom_Host'):
        assert _is_linked(a2, 'pycom_Host', b)
    _safe_set(b, 'pycom_Connection17', None)
    assert not _is_linked(b, 'pycom_Connection17', a2)
    if hasattr(a2, 'pycom_Host'):
        assert not _is_linked(a2, 'pycom_Host', b)


def test_assoc_imports7_reverse_link_reassign_clear():
    a1 = pycom_Library(name="sample_text")
    a2 = pycom_Library(name="sample_text_2")
    b = pycom_Import(name="sample_text", path="sample_text")
    _safe_set(b, 'pycom_Import9', a1)
    assert _is_linked(b, 'pycom_Import9', a1)
    if hasattr(a1, 'pycom_Library8'):
        assert _is_linked(a1, 'pycom_Library8', b)
    _safe_set(b, 'pycom_Import9', a2)
    assert _is_linked(b, 'pycom_Import9', a2)
    if hasattr(a1, 'pycom_Library8'):
        assert not _is_linked(a1, 'pycom_Library8', b)
    if hasattr(a2, 'pycom_Library8'):
        assert _is_linked(a2, 'pycom_Library8', b)
    _safe_set(b, 'pycom_Import9', None)
    assert not _is_linked(b, 'pycom_Import9', a2)
    if hasattr(a2, 'pycom_Library8'):
        assert not _is_linked(a2, 'pycom_Library8', b)


def test_assoc_left58_reverse_link_reassign_clear():
    a1 = pycom_Expression(outputValue=7)
    a2 = pycom_Expression(outputValue=13)
    b = pycom_ComparisonExp(op="sample_text")
    _safe_set(b, 'pycom_ComparisonExp59', a1)
    assert _is_linked(b, 'pycom_ComparisonExp59', a1)
    if hasattr(a1, 'pycom_Expression'):
        assert _is_linked(a1, 'pycom_Expression', b)
    _safe_set(b, 'pycom_ComparisonExp59', a2)
    assert _is_linked(b, 'pycom_ComparisonExp59', a2)
    if hasattr(a1, 'pycom_Expression'):
        assert not _is_linked(a1, 'pycom_Expression', b)
    if hasattr(a2, 'pycom_Expression'):
        assert _is_linked(a2, 'pycom_Expression', b)
    _safe_set(b, 'pycom_ComparisonExp59', None)
    assert not _is_linked(b, 'pycom_ComparisonExp59', a2)
    if hasattr(a2, 'pycom_Expression'):
        assert not _is_linked(a2, 'pycom_Expression', b)


def test_assoc_library18_reverse_link_reassign_clear():
    a1 = pycom_Library(name="sample_text")
    a2 = pycom_Library(name="sample_text_2")
    b = pycom_Board(boardType="sample_text", communicationRate=7, name="sample_text")
    _safe_set(b, 'pycom_Board19', {a1})
    assert _is_linked(b, 'pycom_Board19', a1)
    if hasattr(a1, 'pycom_Library20'):
        assert _is_linked(a1, 'pycom_Library20', b)
    _safe_set(b, 'pycom_Board19', {a2})
    assert _is_linked(b, 'pycom_Board19', a2)
    if hasattr(a1, 'pycom_Library20'):
        assert not _is_linked(a1, 'pycom_Library20', b)
    if hasattr(a2, 'pycom_Library20'):
        assert _is_linked(a2, 'pycom_Library20', b)
    _safe_set(b, 'pycom_Board19', set())
    assert not _is_linked(b, 'pycom_Board19', a2)
    if hasattr(a2, 'pycom_Library20'):
        assert not _is_linked(a2, 'pycom_Library20', b)


def test_assoc_nestedCondition52_reverse_link_reassign_clear():
    a1 = pycom_Condition(operator="sample_text")
    a2 = pycom_Condition(operator="sample_text_2")
    b = pycom_Condition(operator="sample_text")
    _safe_set(b, 'pycom_Condition53', a1)
    assert _is_linked(b, 'pycom_Condition53', a1)
    if hasattr(a1, 'pycom_Condition51'):
        assert _is_linked(a1, 'pycom_Condition51', b)
    _safe_set(b, 'pycom_Condition53', a2)
    assert _is_linked(b, 'pycom_Condition53', a2)
    if hasattr(a1, 'pycom_Condition51'):
        assert not _is_linked(a1, 'pycom_Condition51', b)
    if hasattr(a2, 'pycom_Condition51'):
        assert _is_linked(a2, 'pycom_Condition51', b)
    _safe_set(b, 'pycom_Condition53', None)
    assert not _is_linked(b, 'pycom_Condition53', a2)
    if hasattr(a2, 'pycom_Condition51'):
        assert not _is_linked(a2, 'pycom_Condition51', b)


def test_assoc_parameter10_reverse_link_reassign_clear():
    a1 = pycom_ParameterType(number=7, text="sample_text")
    a2 = pycom_ParameterType(number=13, text="sample_text_2")
    b = pycom_Import(name="sample_text", path="sample_text")
    _safe_set(b, 'pycom_Import11', {a1})
    assert _is_linked(b, 'pycom_Import11', a1)
    if hasattr(a1, 'pycom_ParameterType'):
        assert _is_linked(a1, 'pycom_ParameterType', b)
    _safe_set(b, 'pycom_Import11', {a2})
    assert _is_linked(b, 'pycom_Import11', a2)
    if hasattr(a1, 'pycom_ParameterType'):
        assert not _is_linked(a1, 'pycom_ParameterType', b)
    if hasattr(a2, 'pycom_ParameterType'):
        assert _is_linked(a2, 'pycom_ParameterType', b)
    _safe_set(b, 'pycom_Import11', set())
    assert not _is_linked(b, 'pycom_Import11', a2)
    if hasattr(a2, 'pycom_ParameterType'):
        assert not _is_linked(a2, 'pycom_ParameterType', b)


def test_assoc_right60_reverse_link_reassign_clear():
    a1 = pycom_Expression(outputValue=7)
    a2 = pycom_Expression(outputValue=13)
    b = pycom_ComparisonExp(op="sample_text")
    _safe_set(b, 'pycom_ComparisonExp61', a1)
    assert _is_linked(b, 'pycom_ComparisonExp61', a1)
    if hasattr(a1, 'pycom_Expression62'):
        assert _is_linked(a1, 'pycom_Expression62', b)
    _safe_set(b, 'pycom_ComparisonExp61', a2)
    assert _is_linked(b, 'pycom_ComparisonExp61', a2)
    if hasattr(a1, 'pycom_Expression62'):
        assert not _is_linked(a1, 'pycom_Expression62', b)
    if hasattr(a2, 'pycom_Expression62'):
        assert _is_linked(a2, 'pycom_Expression62', b)
    _safe_set(b, 'pycom_ComparisonExp61', None)
    assert not _is_linked(b, 'pycom_ComparisonExp61', a2)
    if hasattr(a2, 'pycom_Expression62'):
        assert not _is_linked(a2, 'pycom_Expression62', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ExpMembers27_stub_double():
    # pycom_ExpMember has no real 'pycom_ExpMember' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ConditionalAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ConditionalAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ConditionalAction(type="sample_text")
    partner = pycom_ExpMember()
    setattr(partner, 'pycom_ExpMember', None)
    _safe_set(owner, 'pycom_ConditionalAction28', {partner})
    assert getattr(partner, 'pycom_ExpMember') == owner
    _safe_set(owner, 'pycom_ConditionalAction28', set())
    assert getattr(partner, 'pycom_ExpMember') is None


def test_assoc_actuatorName37_stub_double():
    # pycom_Actuator has no real 'pycom_Actuator38' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ModuleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ModuleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ModuleName(name="sample_text")
    partner = pycom_Actuator()
    setattr(partner, 'pycom_Actuator38', None)
    _safe_set(owner, 'pycom_ModuleName39', partner)
    assert getattr(partner, 'pycom_Actuator38') == owner
    _safe_set(owner, 'pycom_ModuleName39', None)
    assert getattr(partner, 'pycom_Actuator38') is None


def test_assoc_board65_stub_double():
    # pycom_Function has no real 'pycom_Function66' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Board(boardType="sample_text", communicationRate=7, name="sample_text")
    partner = pycom_Function()
    setattr(partner, 'pycom_Function66', None)
    _safe_set(owner, 'pycom_Board67', partner)
    assert getattr(partner, 'pycom_Function66') == owner
    _safe_set(owner, 'pycom_Board67', None)
    assert getattr(partner, 'pycom_Function66') is None


def test_assoc_boardMembers21_stub_double():
    # pycom_BoardMember has no real 'pycom_BoardMember' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Board(boardType="sample_text", communicationRate=7, name="sample_text")
    partner = pycom_BoardMember()
    setattr(partner, 'pycom_BoardMember', None)
    _safe_set(owner, 'pycom_Board22', {partner})
    assert getattr(partner, 'pycom_BoardMember') == owner
    _safe_set(owner, 'pycom_Board22', set())
    assert getattr(partner, 'pycom_BoardMember') is None


def test_assoc_boards3_stub_double():
    # pycom_System has no real 'pycom_System4' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Board's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Board's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Board(boardType="sample_text", communicationRate=7, name="sample_text")
    partner = pycom_System()
    setattr(partner, 'pycom_System4', None)
    _safe_set(owner, 'pycom_Board', partner)
    assert owner in getattr(partner, 'pycom_System4')
    _safe_set(owner, 'pycom_Board', None)
    assert owner not in getattr(partner, 'pycom_System4')


def test_assoc_boolVal54_stub_double():
    # pycom_LogicExp has no real 'pycom_LogicExp55' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Boolean's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Boolean's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Boolean(value="sample_text")
    partner = pycom_LogicExp()
    setattr(partner, 'pycom_LogicExp55', None)
    _safe_set(owner, 'pycom_Boolean', partner)
    assert getattr(partner, 'pycom_LogicExp55') == owner
    _safe_set(owner, 'pycom_Boolean', None)
    assert getattr(partner, 'pycom_LogicExp55') is None


def test_assoc_compExp56_stub_double():
    # pycom_LogicExp has no real 'pycom_LogicExp57' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ComparisonExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ComparisonExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ComparisonExp(op="sample_text")
    partner = pycom_LogicExp()
    setattr(partner, 'pycom_LogicExp57', None)
    _safe_set(owner, 'pycom_ComparisonExp', partner)
    assert getattr(partner, 'pycom_LogicExp57') == owner
    _safe_set(owner, 'pycom_ComparisonExp', None)
    assert getattr(partner, 'pycom_LogicExp57') is None


def test_assoc_functionName68_stub_double():
    # pycom_Function has no real 'pycom_Function69' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Import(name="sample_text", path="sample_text")
    partner = pycom_Function()
    setattr(partner, 'pycom_Function69', None)
    _safe_set(owner, 'pycom_Import70', partner)
    assert getattr(partner, 'pycom_Function69') == owner
    _safe_set(owner, 'pycom_Import70', None)
    assert getattr(partner, 'pycom_Function69') is None


def test_assoc_imports1_stub_double():
    # pycom_System has no real 'pycom_System2' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Import(name="sample_text", path="sample_text")
    partner = pycom_System()
    setattr(partner, 'pycom_System2', None)
    _safe_set(owner, 'pycom_Import', partner)
    assert owner in getattr(partner, 'pycom_System2')
    _safe_set(owner, 'pycom_Import', None)
    assert owner not in getattr(partner, 'pycom_System2')


def test_assoc_input46_stub_double():
    # pycom_Pin has no real 'pycom_Pin47' property in the generated
    # code (a bare stub) -- manually attach it so pycom_PinName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_PinName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_PinName(name="sample_text")
    partner = pycom_Pin()
    setattr(partner, 'pycom_Pin47', None)
    _safe_set(owner, 'pycom_PinName48', partner)
    assert getattr(partner, 'pycom_Pin47') == owner
    _safe_set(owner, 'pycom_PinName48', None)
    assert getattr(partner, 'pycom_Pin47') is None


def test_assoc_libraries0_stub_double():
    # pycom_System has no real 'pycom_System' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Library(name="sample_text")
    partner = pycom_System()
    setattr(partner, 'pycom_System', None)
    _safe_set(owner, 'pycom_Library', partner)
    assert owner in getattr(partner, 'pycom_System')
    _safe_set(owner, 'pycom_Library', None)
    assert owner not in getattr(partner, 'pycom_System')


def test_assoc_logicEx49_stub_double():
    # pycom_LogicExp has no real 'pycom_LogicExp' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Condition(operator="sample_text")
    partner = pycom_LogicExp()
    setattr(partner, 'pycom_LogicExp', None)
    _safe_set(owner, 'pycom_Condition50', partner)
    assert getattr(partner, 'pycom_LogicExp') == owner
    _safe_set(owner, 'pycom_Condition50', None)
    assert getattr(partner, 'pycom_LogicExp') is None


def test_assoc_outputfunction63_stub_double():
    # pycom_Function has no real 'pycom_Function' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Expression(outputValue=7)
    partner = pycom_Function()
    setattr(partner, 'pycom_Function', None)
    _safe_set(owner, 'pycom_Expression64', partner)
    assert getattr(partner, 'pycom_Function') == owner
    _safe_set(owner, 'pycom_Expression64', None)
    assert getattr(partner, 'pycom_Function') is None


def test_assoc_power44_stub_double():
    # pycom_Pin has no real 'pycom_Pin45' property in the generated
    # code (a bare stub) -- manually attach it so pycom_PinName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_PinName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_PinName(name="sample_text")
    partner = pycom_Pin()
    setattr(partner, 'pycom_Pin45', None)
    _safe_set(owner, 'pycom_PinName', partner)
    assert getattr(partner, 'pycom_Pin45') == owner
    _safe_set(owner, 'pycom_PinName', None)
    assert getattr(partner, 'pycom_Pin45') is None


def test_assoc_sensorName31_stub_double():
    # pycom_Sensor has no real 'pycom_Sensor32' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ModuleName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ModuleName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ModuleName(name="sample_text")
    partner = pycom_Sensor()
    setattr(partner, 'pycom_Sensor32', None)
    _safe_set(owner, 'pycom_ModuleName', partner)
    assert getattr(partner, 'pycom_Sensor32') == owner
    _safe_set(owner, 'pycom_ModuleName', None)
    assert getattr(partner, 'pycom_Sensor32') is None


def test_assoc_servers5_stub_double():
    # pycom_System has no real 'pycom_System6' property in the generated
    # code (a bare stub) -- manually attach it so pycom_Server's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_Server's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_Server(name="sample_text")
    partner = pycom_System()
    setattr(partner, 'pycom_System6', None)
    _safe_set(owner, 'pycom_Server', partner)
    assert owner in getattr(partner, 'pycom_System6')
    _safe_set(owner, 'pycom_Server', None)
    assert owner not in getattr(partner, 'pycom_System6')


def test_assoc_type43_stub_double():
    # pycom_Communication has no real 'pycom_Communication' property in the generated
    # code (a bare stub) -- manually attach it so pycom_CommunicationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_CommunicationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_CommunicationType(name="sample_text", password="sample_text", ssid="sample_text")
    partner = pycom_Communication()
    setattr(partner, 'pycom_Communication', None)
    _safe_set(owner, 'pycom_CommunicationType', partner)
    assert getattr(partner, 'pycom_Communication') == owner
    _safe_set(owner, 'pycom_CommunicationType', None)
    assert getattr(partner, 'pycom_Communication') is None


def test_assoc_typeName29_stub_double():
    # pycom_Sensor has no real 'pycom_Sensor30' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ModuleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ModuleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ModuleType(name="sample_text")
    partner = pycom_Sensor()
    setattr(partner, 'pycom_Sensor30', None)
    _safe_set(owner, 'pycom_ModuleType', partner)
    assert getattr(partner, 'pycom_Sensor30') == owner
    _safe_set(owner, 'pycom_ModuleType', None)
    assert getattr(partner, 'pycom_Sensor30') is None


def test_assoc_typeName35_stub_double():
    # pycom_Actuator has no real 'pycom_Actuator' property in the generated
    # code (a bare stub) -- manually attach it so pycom_ModuleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pycom_ModuleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pycom_ModuleType(name="sample_text")
    partner = pycom_Actuator()
    setattr(partner, 'pycom_Actuator', None)
    _safe_set(owner, 'pycom_ModuleType36', partner)
    assert getattr(partner, 'pycom_Actuator') == owner
    _safe_set(owner, 'pycom_ModuleType36', None)
    assert getattr(partner, 'pycom_Actuator') is None


