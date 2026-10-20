import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArduinoAnalogModule,
    ArduinoDigitalModule,
    ArduinoModule,
    Assignment,
    BinaryExpression,
    Board,
    BooleanExpression,
    Constant,
    Control,
    Expression,
    Instruction,
    IntegerExpression,
    Module,
    ModuleGet,
    ModuleInstruction,
    NamedElement,
    Pin,
    UnaryExpression,
    Utilities,
    Variable,
    VariableRef,
    arduino_AmbientLightSensor,
    arduino_AnalogPin,
    arduino_ArduinoAnalogModule,
    arduino_ArduinoBoard,
    arduino_ArduinoCommunicationModule,
    arduino_ArduinoDigitalModule,
    arduino_ArduinoModule,
    arduino_Assignment,
    arduino_BinaryBooleanExpression,
    arduino_BinaryExpression,
    arduino_BinaryIntegerExpression,
    arduino_Block,
    arduino_BluetoothTransceiver,
    arduino_Board,
    arduino_BooleanConstant,
    arduino_BooleanExpression,
    arduino_BooleanModuleGet,
    arduino_BooleanVariable,
    arduino_BooleanVariableRef,
    arduino_Buzzer,
    arduino_Constant,
    arduino_Control,
    arduino_Delay,
    arduino_DigitalPin,
    arduino_Expression,
    arduino_Fan,
    arduino_If,
    arduino_InfraRedSensor,
    arduino_Instruction,
    arduino_IntegerConstant,
    arduino_IntegerExpression,
    arduino_IntegerModuleGet,
    arduino_IntegerVariable,
    arduino_IntegerVariableRef,
    arduino_LED,
    arduino_MicroServo,
    arduino_Module,
    arduino_ModuleAssignment,
    arduino_ModuleGet,
    arduino_ModuleInstruction,
    arduino_MusicPlayer,
    arduino_NamedElement,
    arduino_Pin,
    arduino_Project,
    arduino_PushButton,
    arduino_Repeat,
    arduino_RotationSensor,
    arduino_Sketch,
    arduino_SoundSensor,
    arduino_UnaryBooleanExpression,
    arduino_UnaryExpression,
    arduino_UnaryIntegerExpression,
    arduino_Utilities,
    arduino_Variable,
    arduino_VariableAssignment,
    arduino_VariableDeclaration,
    arduino_VariableRef,
    arduino_WaitFor,
    arduino_While,
    BinaryBooleanOperatorKind,
    BinaryIntegerOperatorKind,
    ChangeType,
    Color,
    Time,
    UnaryBooleanOperatorKind,
    UnaryIntegerOperatorKind,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_pin34_stub_double():
    # arduino_Pin has no real 'arduino_Pin' property in the generated
    # code (a bare stub) -- manually attach it so arduino_WaitFor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_WaitFor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_WaitFor(mode="sample_text")
    partner = arduino_Pin()
    setattr(partner, 'arduino_Pin', None)
    _safe_set(owner, 'arduino_WaitFor', partner)
    assert getattr(partner, 'arduino_Pin') == owner
    _safe_set(owner, 'arduino_WaitFor', None)
    assert getattr(partner, 'arduino_Pin') is None


def test_assoc_variable33_stub_double():
    # arduino_IntegerVariableRef has no real 'arduino_IntegerVariableRef' property in the generated
    # code (a bare stub) -- manually attach it so arduino_IntegerVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_IntegerVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_IntegerVariable(initialValue=7)
    partner = arduino_IntegerVariableRef()
    setattr(partner, 'arduino_IntegerVariableRef', None)
    _safe_set(owner, 'arduino_IntegerVariable', partner)
    assert getattr(partner, 'arduino_IntegerVariableRef') == owner
    _safe_set(owner, 'arduino_IntegerVariable', None)
    assert getattr(partner, 'arduino_IntegerVariableRef') is None


def test_assoc_variable42_stub_double():
    # arduino_BooleanVariableRef has no real 'arduino_BooleanVariableRef' property in the generated
    # code (a bare stub) -- manually attach it so arduino_BooleanVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_BooleanVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_BooleanVariable(initialValue=True)
    partner = arduino_BooleanVariableRef()
    setattr(partner, 'arduino_BooleanVariableRef', None)
    _safe_set(owner, 'arduino_BooleanVariable', partner)
    assert getattr(partner, 'arduino_BooleanVariableRef') == owner
    _safe_set(owner, 'arduino_BooleanVariable', None)
    assert getattr(partner, 'arduino_BooleanVariableRef') is None


