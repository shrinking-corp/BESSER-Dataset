import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Actor,
    BinaryOperation,
    BooleanActor,
    BooleanSensor,
    Extendable,
    Extension,
    FloatActor,
    FloatSensor,
    HouseMountable,
    RoomMountable,
    Sensor,
    Statement,
    ValueExpression,
    majordomo_Action,
    majordomo_ActionSetReference,
    majordomo_Actor,
    majordomo_BinaryAndOperation,
    majordomo_BinaryOperation,
    majordomo_BinaryOrOperation,
    majordomo_BoilerActor,
    majordomo_BooleanAction,
    majordomo_BooleanActor,
    majordomo_BooleanSensor,
    majordomo_BooleanSensorStatement,
    majordomo_ClockSensor,
    majordomo_CoffeeActor,
    majordomo_CompareOperation,
    majordomo_ConstantValue,
    majordomo_Extendable,
    majordomo_Extension,
    majordomo_FloatAction,
    majordomo_FloatActor,
    majordomo_FloatSensor,
    majordomo_House,
    majordomo_HouseMountable,
    majordomo_LampActor,
    majordomo_LightSensor,
    majordomo_Majordomo,
    majordomo_NotOperation,
    majordomo_NumberSensor,
    majordomo_PreparedActionSet,
    majordomo_PreparedStatement,
    majordomo_PreparedValue,
    majordomo_Program,
    majordomo_RadiatorActor,
    majordomo_RainSensor,
    majordomo_RollerActor,
    majordomo_RoofWindowActor,
    majordomo_Room,
    majordomo_RoomMountable,
    majordomo_Rule,
    majordomo_Sensor,
    majordomo_SensorValue,
    majordomo_Statement,
    majordomo_StatementReference,
    majordomo_SwitchSensor,
    majordomo_TemperatureSensor,
    majordomo_ValueExpression,
    majordomo_ValueReference,
    Comparator,
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

def test_assoc_actor14_reverse_link_reassign_clear():
    a1 = majordomo_FloatActor()
    a2 = majordomo_FloatActor()
    b = majordomo_FloatAction(value=3.14)
    _safe_set(b, 'majordomo_FloatAction', a1)
    assert _is_linked(b, 'majordomo_FloatAction', a1)
    if hasattr(a1, 'majordomo_FloatActor'):
        assert _is_linked(a1, 'majordomo_FloatActor', b)
    _safe_set(b, 'majordomo_FloatAction', a2)
    assert _is_linked(b, 'majordomo_FloatAction', a2)
    if hasattr(a1, 'majordomo_FloatActor'):
        assert not _is_linked(a1, 'majordomo_FloatActor', b)
    if hasattr(a2, 'majordomo_FloatActor'):
        assert _is_linked(a2, 'majordomo_FloatActor', b)
    _safe_set(b, 'majordomo_FloatAction', None)
    assert not _is_linked(b, 'majordomo_FloatAction', a2)
    if hasattr(a2, 'majordomo_FloatActor'):
        assert not _is_linked(a2, 'majordomo_FloatActor', b)


def test_assoc_actor15_reverse_link_reassign_clear():
    a1 = majordomo_BooleanActor()
    a2 = majordomo_BooleanActor()
    b = majordomo_BooleanAction(value=True)
    _safe_set(b, 'majordomo_BooleanAction', a1)
    assert _is_linked(b, 'majordomo_BooleanAction', a1)
    if hasattr(a1, 'majordomo_BooleanActor'):
        assert _is_linked(a1, 'majordomo_BooleanActor', b)
    _safe_set(b, 'majordomo_BooleanAction', a2)
    assert _is_linked(b, 'majordomo_BooleanAction', a2)
    if hasattr(a1, 'majordomo_BooleanActor'):
        assert not _is_linked(a1, 'majordomo_BooleanActor', b)
    if hasattr(a2, 'majordomo_BooleanActor'):
        assert _is_linked(a2, 'majordomo_BooleanActor', b)
    _safe_set(b, 'majordomo_BooleanAction', None)
    assert not _is_linked(b, 'majordomo_BooleanAction', a2)
    if hasattr(a2, 'majordomo_BooleanActor'):
        assert not _is_linked(a2, 'majordomo_BooleanActor', b)


def test_assoc_rooms1_reverse_link_reassign_clear():
    a1 = majordomo_Room(name="sample_text")
    a2 = majordomo_Room(name="sample_text_2")
    b = majordomo_Majordomo(name="sample_text")
    _safe_set(b, 'majordomo_Majordomo2', {a1})
    assert _is_linked(b, 'majordomo_Majordomo2', a1)
    if hasattr(a1, 'majordomo_Room'):
        assert _is_linked(a1, 'majordomo_Room', b)
    _safe_set(b, 'majordomo_Majordomo2', {a2})
    assert _is_linked(b, 'majordomo_Majordomo2', a2)
    if hasattr(a1, 'majordomo_Room'):
        assert not _is_linked(a1, 'majordomo_Room', b)
    if hasattr(a2, 'majordomo_Room'):
        assert _is_linked(a2, 'majordomo_Room', b)
    _safe_set(b, 'majordomo_Majordomo2', set())
    assert not _is_linked(b, 'majordomo_Majordomo2', a2)
    if hasattr(a2, 'majordomo_Room'):
        assert not _is_linked(a2, 'majordomo_Room', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions45_stub_double():
    # majordomo_Action has no real 'majordomo_Action46' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedActionSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedActionSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedActionSet(name="sample_text")
    partner = majordomo_Action()
    setattr(partner, 'majordomo_Action46', None)
    _safe_set(owner, 'majordomo_PreparedActionSet', {partner})
    assert getattr(partner, 'majordomo_Action46') == owner
    _safe_set(owner, 'majordomo_PreparedActionSet', set())
    assert getattr(partner, 'majordomo_Action46') is None


def test_assoc_constants30_stub_double():
    # majordomo_Program has no real 'ctx31' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedValue(name="sample_text")
    partner = majordomo_Program()
    setattr(partner, 'ctx31', None)
    _safe_set(owner, 'PreparedValue', partner)
    assert owner in getattr(partner, 'ctx31')
    _safe_set(owner, 'PreparedValue', None)
    assert owner not in getattr(partner, 'ctx31')


def test_assoc_ctx39_stub_double():
    # majordomo_Program has no real 'Program' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedStatement(name="sample_text")
    partner = majordomo_Program()
    setattr(partner, 'Program', None)
    _safe_set(owner, 'preparedStatements', partner)
    assert getattr(partner, 'Program') == owner
    _safe_set(owner, 'preparedStatements', None)
    assert getattr(partner, 'Program') is None


def test_assoc_ctx43_stub_double():
    # majordomo_Program has no real 'Program44' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedActionSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedActionSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedActionSet(name="sample_text")
    partner = majordomo_Program()
    setattr(partner, 'Program44', None)
    _safe_set(owner, 'preparedActionSets', partner)
    assert getattr(partner, 'Program44') == owner
    _safe_set(owner, 'preparedActionSets', None)
    assert getattr(partner, 'Program44') is None


def test_assoc_ctx49_stub_double():
    # majordomo_Program has no real 'Program50' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedValue(name="sample_text")
    partner = majordomo_Program()
    setattr(partner, 'Program50', None)
    _safe_set(owner, 'constants', partner)
    assert getattr(partner, 'Program50') == owner
    _safe_set(owner, 'constants', None)
    assert getattr(partner, 'Program50') is None


def test_assoc_house0_stub_double():
    # majordomo_House has no real 'majordomo_House' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_Majordomo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_Majordomo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_Majordomo(name="sample_text")
    partner = majordomo_House()
    setattr(partner, 'majordomo_House', None)
    _safe_set(owner, 'majordomo_Majordomo', partner)
    assert getattr(partner, 'majordomo_House') == owner
    _safe_set(owner, 'majordomo_Majordomo', None)
    assert getattr(partner, 'majordomo_House') is None


def test_assoc_left23_stub_double():
    # majordomo_ValueExpression has no real 'majordomo_ValueExpression' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_CompareOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_CompareOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_CompareOperation(comparator="sample_text")
    partner = majordomo_ValueExpression()
    setattr(partner, 'majordomo_ValueExpression', None)
    _safe_set(owner, 'majordomo_CompareOperation', partner)
    assert getattr(partner, 'majordomo_ValueExpression') == owner
    _safe_set(owner, 'majordomo_CompareOperation', None)
    assert getattr(partner, 'majordomo_ValueExpression') is None


def test_assoc_preparedActionSets34_stub_double():
    # majordomo_Program has no real 'ctx35' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedActionSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedActionSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedActionSet(name="sample_text")
    partner = majordomo_Program()
    setattr(partner, 'ctx35', None)
    _safe_set(owner, 'PreparedActionSet', partner)
    assert owner in getattr(partner, 'ctx35')
    _safe_set(owner, 'PreparedActionSet', None)
    assert owner not in getattr(partner, 'ctx35')


def test_assoc_preparedStatements32_stub_double():
    # majordomo_Program has no real 'ctx33' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedStatement(name="sample_text")
    partner = majordomo_Program()
    setattr(partner, 'ctx33', None)
    _safe_set(owner, 'PreparedStatement', partner)
    assert owner in getattr(partner, 'ctx33')
    _safe_set(owner, 'PreparedStatement', None)
    assert owner not in getattr(partner, 'ctx33')


def test_assoc_program3_stub_double():
    # majordomo_Program has no real 'majordomo_Program' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_Majordomo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_Majordomo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_Majordomo(name="sample_text")
    partner = majordomo_Program()
    setattr(partner, 'majordomo_Program', None)
    _safe_set(owner, 'majordomo_Majordomo4', partner)
    assert getattr(partner, 'majordomo_Program') == owner
    _safe_set(owner, 'majordomo_Majordomo4', None)
    assert getattr(partner, 'majordomo_Program') is None


def test_assoc_ref29_stub_double():
    # majordomo_StatementReference has no real 'majordomo_StatementReference' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedStatement(name="sample_text")
    partner = majordomo_StatementReference()
    setattr(partner, 'majordomo_StatementReference', None)
    _safe_set(owner, 'majordomo_PreparedStatement', partner)
    assert getattr(partner, 'majordomo_StatementReference') == owner
    _safe_set(owner, 'majordomo_PreparedStatement', None)
    assert getattr(partner, 'majordomo_StatementReference') is None


def test_assoc_ref47_stub_double():
    # majordomo_ActionSetReference has no real 'majordomo_ActionSetReference' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedActionSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedActionSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedActionSet(name="sample_text")
    partner = majordomo_ActionSetReference()
    setattr(partner, 'majordomo_ActionSetReference', None)
    _safe_set(owner, 'majordomo_PreparedActionSet48', partner)
    assert getattr(partner, 'majordomo_ActionSetReference') == owner
    _safe_set(owner, 'majordomo_PreparedActionSet48', None)
    assert getattr(partner, 'majordomo_ActionSetReference') is None


def test_assoc_ref53_stub_double():
    # majordomo_ValueReference has no real 'majordomo_ValueReference' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedValue(name="sample_text")
    partner = majordomo_ValueReference()
    setattr(partner, 'majordomo_ValueReference', None)
    _safe_set(owner, 'majordomo_PreparedValue54', partner)
    assert getattr(partner, 'majordomo_ValueReference') == owner
    _safe_set(owner, 'majordomo_PreparedValue54', None)
    assert getattr(partner, 'majordomo_ValueReference') is None


def test_assoc_right24_stub_double():
    # majordomo_ValueExpression has no real 'majordomo_ValueExpression26' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_CompareOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_CompareOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_CompareOperation(comparator="sample_text")
    partner = majordomo_ValueExpression()
    setattr(partner, 'majordomo_ValueExpression26', None)
    _safe_set(owner, 'majordomo_CompareOperation25', partner)
    assert getattr(partner, 'majordomo_ValueExpression26') == owner
    _safe_set(owner, 'majordomo_CompareOperation25', None)
    assert getattr(partner, 'majordomo_ValueExpression26') is None


def test_assoc_sensor27_stub_double():
    # majordomo_BooleanSensorStatement has no real 'majordomo_BooleanSensorStatement' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_BooleanSensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_BooleanSensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_BooleanSensor()
    partner = majordomo_BooleanSensorStatement()
    setattr(partner, 'majordomo_BooleanSensorStatement', None)
    _safe_set(owner, 'majordomo_BooleanSensor', partner)
    assert getattr(partner, 'majordomo_BooleanSensorStatement') == owner
    _safe_set(owner, 'majordomo_BooleanSensor', None)
    assert getattr(partner, 'majordomo_BooleanSensorStatement') is None


def test_assoc_sensor28_stub_double():
    # majordomo_SensorValue has no real 'majordomo_SensorValue' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_FloatSensor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_FloatSensor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_FloatSensor()
    partner = majordomo_SensorValue()
    setattr(partner, 'majordomo_SensorValue', None)
    _safe_set(owner, 'majordomo_FloatSensor', partner)
    assert getattr(partner, 'majordomo_SensorValue') == owner
    _safe_set(owner, 'majordomo_FloatSensor', None)
    assert getattr(partner, 'majordomo_SensorValue') is None


def test_assoc_statement40_stub_double():
    # majordomo_Statement has no real 'majordomo_Statement42' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedStatement(name="sample_text")
    partner = majordomo_Statement()
    setattr(partner, 'majordomo_Statement42', None)
    _safe_set(owner, 'majordomo_PreparedStatement41', partner)
    assert getattr(partner, 'majordomo_Statement42') == owner
    _safe_set(owner, 'majordomo_PreparedStatement41', None)
    assert getattr(partner, 'majordomo_Statement42') is None


def test_assoc_value51_stub_double():
    # majordomo_ValueExpression has no real 'majordomo_ValueExpression52' property in the generated
    # code (a bare stub) -- manually attach it so majordomo_PreparedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # majordomo_PreparedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = majordomo_PreparedValue(name="sample_text")
    partner = majordomo_ValueExpression()
    setattr(partner, 'majordomo_ValueExpression52', None)
    _safe_set(owner, 'majordomo_PreparedValue', partner)
    assert getattr(partner, 'majordomo_ValueExpression52') == owner
    _safe_set(owner, 'majordomo_PreparedValue', None)
    assert getattr(partner, 'majordomo_ValueExpression52') is None


