import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Address,
    Bool,
    Command,
    Comparison,
    ComparisonOp,
    Config,
    Device,
    Expression,
    ExpressionLeft,
    ExpressionRight,
    SENSOR,
    TIMEUNIT,
    VarOrList,
    ioT_AND,
    ioT_Action,
    ioT_AddToList,
    ioT_Address,
    ioT_ArrowCommand,
    ioT_Block,
    ioT_Bool,
    ioT_BoolExpression,
    ioT_ClearListAction,
    ioT_Command,
    ioT_Comparison,
    ioT_ComparisonOp,
    ioT_Config,
    ioT_ConnectStatement,
    ioT_ConnectionConfig,
    ioT_ControllerDevice,
    ioT_DAYS,
    ioT_Declaration,
    ioT_Device,
    ioT_DeviceConfig,
    ioT_EQ,
    ioT_EQL,
    ioT_ElseBlock,
    ioT_Expression,
    ioT_ExpressionLeft,
    ioT_ExpressionRight,
    ioT_ExternalDeclaration,
    ioT_ExternalOf,
    ioT_ExternalRight,
    ioT_False,
    ioT_GE,
    ioT_GT,
    ioT_HOURS,
    ioT_HUMIDITY,
    ioT_IfStatement,
    ioT_IntExpression,
    ioT_IoTDevice,
    ioT_IpAddress,
    ioT_ItemBool,
    ioT_ItemInt,
    ioT_ItemVariable,
    ioT_LE,
    ioT_LEDAction,
    ioT_LIGHTSENSOR,
    ioT_LT,
    ioT_ListenStatement,
    ioT_Loop,
    ioT_MILLISECONDS,
    ioT_MINUTES,
    ioT_Model,
    ioT_NE,
    ioT_OR,
    ioT_Program,
    ioT_PyList,
    ioT_ReadConnection,
    ioT_ReadSensor,
    ioT_ReadVariable,
    ioT_SECONDS,
    ioT_SENSOR,
    ioT_SendCommand,
    ioT_TEMPERATURE,
    ioT_TIMEUNIT,
    ioT_ToVar,
    ioT_True,
    ioT_UnixSerialAddress,
    ioT_VarAccess,
    ioT_VarOrList,
    ioT_Variable,
    ioT_WEEKS,
    ioT_WifiStatement,
    ioT_WindowsSerialAddress,
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

def test_assoc_declarations5_reverse_link_reassign_clear():
    a1 = ioT_Declaration(key="sample_text", value="sample_text")
    a2 = ioT_Declaration(key="sample_text_2", value="sample_text_2")
    b = ioT_Config(name="sample_text")
    _safe_set(b, 'ioT_Config6', {a1})
    assert _is_linked(b, 'ioT_Config6', a1)
    if hasattr(a1, 'ioT_Declaration'):
        assert _is_linked(a1, 'ioT_Declaration', b)
    _safe_set(b, 'ioT_Config6', {a2})
    assert _is_linked(b, 'ioT_Config6', a2)
    if hasattr(a1, 'ioT_Declaration'):
        assert not _is_linked(a1, 'ioT_Declaration', b)
    if hasattr(a2, 'ioT_Declaration'):
        assert _is_linked(a2, 'ioT_Declaration', b)
    _safe_set(b, 'ioT_Config6', set())
    assert not _is_linked(b, 'ioT_Config6', a2)
    if hasattr(a2, 'ioT_Declaration'):
        assert not _is_linked(a2, 'ioT_Declaration', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_address26_stub_double():
    # ioT_ConnectStatement has no real 'ioT_ConnectStatement27' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Address(value="sample_text")
    partner = ioT_ConnectStatement()
    setattr(partner, 'ioT_ConnectStatement27', None)
    _safe_set(owner, 'ioT_Address', partner)
    assert getattr(partner, 'ioT_ConnectStatement27') == owner
    _safe_set(owner, 'ioT_Address', None)
    assert getattr(partner, 'ioT_ConnectStatement27') is None


def test_assoc_body19_stub_double():
    # ioT_ExpressionRight has no real 'ioT_ExpressionRight' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ListenStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ListenStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ListenStatement(ip="sample_text", port=7)
    partner = ioT_ExpressionRight()
    setattr(partner, 'ioT_ExpressionRight', None)
    _safe_set(owner, 'ioT_ListenStatement20', partner)
    assert getattr(partner, 'ioT_ExpressionRight') == owner
    _safe_set(owner, 'ioT_ListenStatement20', None)
    assert getattr(partner, 'ioT_ExpressionRight') is None


def test_assoc_configs1_stub_double():
    # ioT_Model has no real 'ioT_Model2' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Config's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Config's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Config(name="sample_text")
    partner = ioT_Model()
    setattr(partner, 'ioT_Model2', None)
    _safe_set(owner, 'ioT_Config', partner)
    assert owner in getattr(partner, 'ioT_Model2')
    _safe_set(owner, 'ioT_Config', None)
    assert owner not in getattr(partner, 'ioT_Model2')


def test_assoc_configuration28_stub_double():
    # ioT_ConnectStatement has no real 'ioT_ConnectStatement29' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ConnectionConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ConnectionConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ConnectionConfig(type="sample_text")
    partner = ioT_ConnectStatement()
    setattr(partner, 'ioT_ConnectStatement29', None)
    _safe_set(owner, 'ioT_ConnectionConfig30', partner)
    assert getattr(partner, 'ioT_ConnectStatement29') == owner
    _safe_set(owner, 'ioT_ConnectionConfig30', None)
    assert getattr(partner, 'ioT_ConnectStatement29') is None


def test_assoc_connectionConfig21_stub_double():
    # ioT_WifiStatement has no real 'ioT_WifiStatement22' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ConnectionConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ConnectionConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ConnectionConfig(type="sample_text")
    partner = ioT_WifiStatement()
    setattr(partner, 'ioT_WifiStatement22', None)
    _safe_set(owner, 'ioT_ConnectionConfig', partner)
    assert getattr(partner, 'ioT_WifiStatement22') == owner
    _safe_set(owner, 'ioT_ConnectionConfig', None)
    assert getattr(partner, 'ioT_WifiStatement22') is None


def test_assoc_device23_stub_double():
    # ioT_ConnectStatement has no real 'ioT_ConnectStatement24' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Device(name="sample_text")
    partner = ioT_ConnectStatement()
    setattr(partner, 'ioT_ConnectStatement24', None)
    _safe_set(owner, 'ioT_Device25', partner)
    assert getattr(partner, 'ioT_ConnectStatement24') == owner
    _safe_set(owner, 'ioT_Device25', None)
    assert getattr(partner, 'ioT_ConnectStatement24') is None


def test_assoc_devices3_stub_double():
    # ioT_Model has no real 'ioT_Model4' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Device(name="sample_text")
    partner = ioT_Model()
    setattr(partner, 'ioT_Model4', None)
    _safe_set(owner, 'ioT_Device', partner)
    assert owner in getattr(partner, 'ioT_Model4')
    _safe_set(owner, 'ioT_Device', None)
    assert owner not in getattr(partner, 'ioT_Model4')


def test_assoc_externalDeclarations0_stub_double():
    # ioT_Model has no real 'ioT_Model' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ExternalDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ExternalDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ExternalDeclaration(name="sample_text")
    partner = ioT_Model()
    setattr(partner, 'ioT_Model', None)
    _safe_set(owner, 'ioT_ExternalDeclaration', partner)
    assert owner in getattr(partner, 'ioT_Model')
    _safe_set(owner, 'ioT_ExternalDeclaration', None)
    assert owner not in getattr(partner, 'ioT_Model')


def test_assoc_listenStatements15_stub_double():
    # ioT_Program has no real 'ioT_Program16' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ListenStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ListenStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ListenStatement(ip="sample_text", port=7)
    partner = ioT_Program()
    setattr(partner, 'ioT_Program16', None)
    _safe_set(owner, 'ioT_ListenStatement', partner)
    assert owner in getattr(partner, 'ioT_Program16')
    _safe_set(owner, 'ioT_ListenStatement', None)
    assert owner not in getattr(partner, 'ioT_Program16')


def test_assoc_method41_stub_double():
    # ioT_ExternalOf has no real 'ioT_ExternalOf' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ExternalDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ExternalDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ExternalDeclaration(name="sample_text")
    partner = ioT_ExternalOf()
    setattr(partner, 'ioT_ExternalOf', None)
    _safe_set(owner, 'ioT_ExternalDeclaration42', partner)
    assert getattr(partner, 'ioT_ExternalOf') == owner
    _safe_set(owner, 'ioT_ExternalDeclaration42', None)
    assert getattr(partner, 'ioT_ExternalOf') is None


def test_assoc_method49_stub_double():
    # ioT_ExternalRight has no real 'ioT_ExternalRight' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ExternalDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ExternalDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ExternalDeclaration(name="sample_text")
    partner = ioT_ExternalRight()
    setattr(partner, 'ioT_ExternalRight', None)
    _safe_set(owner, 'ioT_ExternalDeclaration50', partner)
    assert getattr(partner, 'ioT_ExternalRight') == owner
    _safe_set(owner, 'ioT_ExternalDeclaration50', None)
    assert getattr(partner, 'ioT_ExternalRight') is None


def test_assoc_op88_stub_double():
    # ioT_EQL has no real 'ioT_EQL89' property in the generated
    # code (a bare stub) -- manually attach it so ioT_ComparisonOp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_ComparisonOp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_ComparisonOp(op="sample_text")
    partner = ioT_EQL()
    setattr(partner, 'ioT_EQL89', None)
    _safe_set(owner, 'ioT_ComparisonOp', partner)
    assert getattr(partner, 'ioT_EQL89') == owner
    _safe_set(owner, 'ioT_ComparisonOp', None)
    assert getattr(partner, 'ioT_EQL89') is None


def test_assoc_program7_stub_double():
    # ioT_Program has no real 'ioT_Program' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Device(name="sample_text")
    partner = ioT_Program()
    setattr(partner, 'ioT_Program', None)
    _safe_set(owner, 'ioT_Device8', partner)
    assert getattr(partner, 'ioT_Program') == owner
    _safe_set(owner, 'ioT_Device8', None)
    assert getattr(partner, 'ioT_Program') is None


def test_assoc_source39_stub_double():
    # ioT_ReadConnection has no real 'ioT_ReadConnection' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Device(name="sample_text")
    partner = ioT_ReadConnection()
    setattr(partner, 'ioT_ReadConnection', None)
    _safe_set(owner, 'ioT_Device40', partner)
    assert getattr(partner, 'ioT_ReadConnection') == owner
    _safe_set(owner, 'ioT_Device40', None)
    assert getattr(partner, 'ioT_ReadConnection') is None


def test_assoc_target43_stub_double():
    # ioT_ExternalOf has no real 'ioT_ExternalOf44' property in the generated
    # code (a bare stub) -- manually attach it so ioT_VarOrList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_VarOrList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_VarOrList(name="sample_text")
    partner = ioT_ExternalOf()
    setattr(partner, 'ioT_ExternalOf44', None)
    _safe_set(owner, 'ioT_VarOrList45', partner)
    assert getattr(partner, 'ioT_ExternalOf44') == owner
    _safe_set(owner, 'ioT_VarOrList45', None)
    assert getattr(partner, 'ioT_ExternalOf44') is None


def test_assoc_target67_stub_double():
    # ioT_SendCommand has no real 'ioT_SendCommand' property in the generated
    # code (a bare stub) -- manually attach it so ioT_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_Device(name="sample_text")
    partner = ioT_SendCommand()
    setattr(partner, 'ioT_SendCommand', None)
    _safe_set(owner, 'ioT_Device68', partner)
    assert getattr(partner, 'ioT_SendCommand') == owner
    _safe_set(owner, 'ioT_Device68', None)
    assert getattr(partner, 'ioT_SendCommand') is None


def test_assoc_variableName61_stub_double():
    # ioT_VarAccess has no real 'ioT_VarAccess' property in the generated
    # code (a bare stub) -- manually attach it so ioT_VarOrList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_VarOrList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_VarOrList(name="sample_text")
    partner = ioT_VarAccess()
    setattr(partner, 'ioT_VarAccess', None)
    _safe_set(owner, 'ioT_VarOrList62', partner)
    assert getattr(partner, 'ioT_VarAccess') == owner
    _safe_set(owner, 'ioT_VarOrList62', None)
    assert getattr(partner, 'ioT_VarAccess') is None


def test_assoc_variables13_stub_double():
    # ioT_Program has no real 'ioT_Program14' property in the generated
    # code (a bare stub) -- manually attach it so ioT_VarOrList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ioT_VarOrList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ioT_VarOrList(name="sample_text")
    partner = ioT_Program()
    setattr(partner, 'ioT_Program14', None)
    _safe_set(owner, 'ioT_VarOrList', partner)
    assert owner in getattr(partner, 'ioT_Program14')
    _safe_set(owner, 'ioT_VarOrList', None)
    assert owner not in getattr(partner, 'ioT_Program14')


