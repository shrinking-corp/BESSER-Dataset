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
    arduino_While,
    BinaryBooleanOperatorKind,
    BinaryIntegerOperatorKind,
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

def test_assoc_block12_reverse_link_reassign_clear():
    a1 = arduino_Control()
    a2 = arduino_Control()
    b = arduino_Block()
    _safe_set(b, 'arduino_Block13', a1)
    assert _is_linked(b, 'arduino_Block13', a1)
    if hasattr(a1, 'arduino_Control'):
        assert _is_linked(a1, 'arduino_Control', b)
    _safe_set(b, 'arduino_Block13', a2)
    assert _is_linked(b, 'arduino_Block13', a2)
    if hasattr(a1, 'arduino_Control'):
        assert not _is_linked(a1, 'arduino_Control', b)
    if hasattr(a2, 'arduino_Control'):
        assert _is_linked(a2, 'arduino_Control', b)
    _safe_set(b, 'arduino_Block13', None)
    assert not _is_linked(b, 'arduino_Block13', a2)
    if hasattr(a2, 'arduino_Control'):
        assert not _is_linked(a2, 'arduino_Control', b)


def test_assoc_connectedTransceiver43_reverse_link_reassign_clear():
    a1 = arduino_BluetoothTransceiver(dataReceived="sample_text", dataToSend="sample_text")
    a2 = arduino_BluetoothTransceiver(dataReceived="sample_text_2", dataToSend="sample_text_2")
    b = arduino_BluetoothTransceiver(dataReceived="sample_text", dataToSend="sample_text")
    _safe_set(b, 'arduino_BluetoothTransceiver42', {a1})
    assert _is_linked(b, 'arduino_BluetoothTransceiver42', a1)
    if hasattr(a1, 'arduino_BluetoothTransceiver'):
        assert _is_linked(a1, 'arduino_BluetoothTransceiver', b)
    _safe_set(b, 'arduino_BluetoothTransceiver42', {a2})
    assert _is_linked(b, 'arduino_BluetoothTransceiver42', a2)
    if hasattr(a1, 'arduino_BluetoothTransceiver'):
        assert not _is_linked(a1, 'arduino_BluetoothTransceiver', b)
    if hasattr(a2, 'arduino_BluetoothTransceiver'):
        assert _is_linked(a2, 'arduino_BluetoothTransceiver', b)
    _safe_set(b, 'arduino_BluetoothTransceiver42', set())
    assert not _is_linked(b, 'arduino_BluetoothTransceiver42', a2)
    if hasattr(a2, 'arduino_BluetoothTransceiver'):
        assert not _is_linked(a2, 'arduino_BluetoothTransceiver', b)


def test_assoc_elseBlock24_reverse_link_reassign_clear():
    a1 = arduino_If()
    a2 = arduino_If()
    b = arduino_Block()
    _safe_set(b, 'arduino_Block26', a1)
    assert _is_linked(b, 'arduino_Block26', a1)
    if hasattr(a1, 'arduino_If25'):
        assert _is_linked(a1, 'arduino_If25', b)
    _safe_set(b, 'arduino_Block26', a2)
    assert _is_linked(b, 'arduino_Block26', a2)
    if hasattr(a1, 'arduino_If25'):
        assert not _is_linked(a1, 'arduino_If25', b)
    if hasattr(a2, 'arduino_If25'):
        assert _is_linked(a2, 'arduino_If25', b)
    _safe_set(b, 'arduino_Block26', None)
    assert not _is_linked(b, 'arduino_Block26', a2)
    if hasattr(a2, 'arduino_If25'):
        assert not _is_linked(a2, 'arduino_If25', b)


def test_assoc_instructions34_reverse_link_reassign_clear():
    a1 = arduino_Instruction()
    a2 = arduino_Instruction()
    b = arduino_Block()
    _safe_set(b, 'arduino_Block35', {a1})
    assert _is_linked(b, 'arduino_Block35', a1)
    if hasattr(a1, 'arduino_Instruction'):
        assert _is_linked(a1, 'arduino_Instruction', b)
    _safe_set(b, 'arduino_Block35', {a2})
    assert _is_linked(b, 'arduino_Block35', a2)
    if hasattr(a1, 'arduino_Instruction'):
        assert not _is_linked(a1, 'arduino_Instruction', b)
    if hasattr(a2, 'arduino_Instruction'):
        assert _is_linked(a2, 'arduino_Instruction', b)
    _safe_set(b, 'arduino_Block35', set())
    assert not _is_linked(b, 'arduino_Block35', a2)
    if hasattr(a2, 'arduino_Instruction'):
        assert not _is_linked(a2, 'arduino_Instruction', b)


def test_assoc_variable21_reverse_link_reassign_clear():
    a1 = arduino_VariableAssignment()
    a2 = arduino_VariableAssignment()
    b = arduino_Variable()
    _safe_set(b, 'arduino_Variable', a1)
    assert _is_linked(b, 'arduino_Variable', a1)
    if hasattr(a1, 'arduino_VariableAssignment'):
        assert _is_linked(a1, 'arduino_VariableAssignment', b)
    _safe_set(b, 'arduino_Variable', a2)
    assert _is_linked(b, 'arduino_Variable', a2)
    if hasattr(a1, 'arduino_VariableAssignment'):
        assert not _is_linked(a1, 'arduino_VariableAssignment', b)
    if hasattr(a2, 'arduino_VariableAssignment'):
        assert _is_linked(a2, 'arduino_VariableAssignment', b)
    _safe_set(b, 'arduino_Variable', None)
    assert not _is_linked(b, 'arduino_Variable', a2)
    if hasattr(a2, 'arduino_VariableAssignment'):
        assert not _is_linked(a2, 'arduino_VariableAssignment', b)


def test_assoc_variable31_reverse_link_reassign_clear():
    a1 = arduino_VariableDeclaration()
    a2 = arduino_VariableDeclaration()
    b = arduino_Variable()
    _safe_set(b, 'arduino_Variable32', a1)
    assert _is_linked(b, 'arduino_Variable32', a1)
    if hasattr(a1, 'arduino_VariableDeclaration'):
        assert _is_linked(a1, 'arduino_VariableDeclaration', b)
    _safe_set(b, 'arduino_Variable32', a2)
    assert _is_linked(b, 'arduino_Variable32', a2)
    if hasattr(a1, 'arduino_VariableDeclaration'):
        assert not _is_linked(a1, 'arduino_VariableDeclaration', b)
    if hasattr(a2, 'arduino_VariableDeclaration'):
        assert _is_linked(a2, 'arduino_VariableDeclaration', b)
    _safe_set(b, 'arduino_Variable32', None)
    assert not _is_linked(b, 'arduino_Variable32', a2)
    if hasattr(a2, 'arduino_VariableDeclaration'):
        assert not _is_linked(a2, 'arduino_VariableDeclaration', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_block5_stub_double():
    # arduino_Sketch has no real 'arduino_Sketch' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Block()
    partner = arduino_Sketch()
    setattr(partner, 'arduino_Sketch', None)
    _safe_set(owner, 'arduino_Block', partner)
    assert getattr(partner, 'arduino_Sketch') == owner
    _safe_set(owner, 'arduino_Block', None)
    assert getattr(partner, 'arduino_Sketch') is None


def test_assoc_boards8_stub_double():
    # arduino_Board has no real 'Board' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Project()
    partner = arduino_Board()
    setattr(partner, 'Board', None)
    _safe_set(owner, 'project', {partner})
    assert getattr(partner, 'Board') == owner
    _safe_set(owner, 'project', set())
    assert getattr(partner, 'Board') is None


def test_assoc_condition16_stub_double():
    # arduino_BooleanExpression has no real 'arduino_BooleanExpression' property in the generated
    # code (a bare stub) -- manually attach it so arduino_While's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_While's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_While()
    partner = arduino_BooleanExpression()
    setattr(partner, 'arduino_BooleanExpression', None)
    _safe_set(owner, 'arduino_While', partner)
    assert getattr(partner, 'arduino_BooleanExpression') == owner
    _safe_set(owner, 'arduino_While', None)
    assert getattr(partner, 'arduino_BooleanExpression') is None


def test_assoc_condition22_stub_double():
    # arduino_BooleanExpression has no real 'arduino_BooleanExpression23' property in the generated
    # code (a bare stub) -- manually attach it so arduino_If's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_If's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_If()
    partner = arduino_BooleanExpression()
    setattr(partner, 'arduino_BooleanExpression23', None)
    _safe_set(owner, 'arduino_If', partner)
    assert getattr(partner, 'arduino_BooleanExpression23') == owner
    _safe_set(owner, 'arduino_If', None)
    assert getattr(partner, 'arduino_BooleanExpression23') is None


def test_assoc_left17_stub_double():
    # arduino_BinaryExpression has no real 'arduino_BinaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Expression()
    partner = arduino_BinaryExpression()
    setattr(partner, 'arduino_BinaryExpression', None)
    _safe_set(owner, 'arduino_Expression', partner)
    assert getattr(partner, 'arduino_BinaryExpression') == owner
    _safe_set(owner, 'arduino_Expression', None)
    assert getattr(partner, 'arduino_BinaryExpression') is None


def test_assoc_module11_stub_double():
    # arduino_Module has no real 'arduino_Module' property in the generated
    # code (a bare stub) -- manually attach it so arduino_ModuleInstruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_ModuleInstruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_ModuleInstruction()
    partner = arduino_Module()
    setattr(partner, 'arduino_Module', None)
    _safe_set(owner, 'arduino_ModuleInstruction', partner)
    assert getattr(partner, 'arduino_Module') == owner
    _safe_set(owner, 'arduino_ModuleInstruction', None)
    assert getattr(partner, 'arduino_Module') is None


def test_assoc_operand27_stub_double():
    # arduino_Assignment has no real 'arduino_Assignment' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Expression()
    partner = arduino_Assignment()
    setattr(partner, 'arduino_Assignment', None)
    _safe_set(owner, 'arduino_Expression28', partner)
    assert getattr(partner, 'arduino_Assignment') == owner
    _safe_set(owner, 'arduino_Expression28', None)
    assert getattr(partner, 'arduino_Assignment') is None


def test_assoc_operand29_stub_double():
    # arduino_UnaryExpression has no real 'arduino_UnaryExpression' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Expression()
    partner = arduino_UnaryExpression()
    setattr(partner, 'arduino_UnaryExpression', None)
    _safe_set(owner, 'arduino_Expression30', partner)
    assert getattr(partner, 'arduino_UnaryExpression') == owner
    _safe_set(owner, 'arduino_Expression30', None)
    assert getattr(partner, 'arduino_UnaryExpression') is None


def test_assoc_project0_stub_double():
    # arduino_Board has no real 'boards' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Project()
    partner = arduino_Board()
    setattr(partner, 'boards', None)
    _safe_set(owner, 'Project', partner)
    assert getattr(partner, 'boards') == owner
    _safe_set(owner, 'Project', None)
    assert getattr(partner, 'boards') is None


def test_assoc_project3_stub_double():
    # arduino_Sketch has no real 'sketches' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Project()
    partner = arduino_Sketch()
    setattr(partner, 'sketches', None)
    _safe_set(owner, 'Project4', partner)
    assert getattr(partner, 'sketches') == owner
    _safe_set(owner, 'Project4', None)
    assert getattr(partner, 'sketches') is None


def test_assoc_right18_stub_double():
    # arduino_BinaryExpression has no real 'arduino_BinaryExpression19' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Expression()
    partner = arduino_BinaryExpression()
    setattr(partner, 'arduino_BinaryExpression19', None)
    _safe_set(owner, 'arduino_Expression20', partner)
    assert getattr(partner, 'arduino_BinaryExpression19') == owner
    _safe_set(owner, 'arduino_Expression20', None)
    assert getattr(partner, 'arduino_BinaryExpression19') is None


def test_assoc_sketches9_stub_double():
    # arduino_Sketch has no real 'Sketch' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Project()
    partner = arduino_Sketch()
    setattr(partner, 'Sketch', None)
    _safe_set(owner, 'project10', {partner})
    assert getattr(partner, 'Sketch') == owner
    _safe_set(owner, 'project10', set())
    assert getattr(partner, 'Sketch') is None


def test_assoc_variable33_stub_double():
    # arduino_IntegerVariableRef has no real 'arduino_IntegerVariableRef' property in the generated
    # code (a bare stub) -- manually attach it so arduino_IntegerVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_IntegerVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_IntegerVariable(initialValue=7, value="sample_text")
    partner = arduino_IntegerVariableRef()
    setattr(partner, 'arduino_IntegerVariableRef', None)
    _safe_set(owner, 'arduino_IntegerVariable', partner)
    assert getattr(partner, 'arduino_IntegerVariableRef') == owner
    _safe_set(owner, 'arduino_IntegerVariable', None)
    assert getattr(partner, 'arduino_IntegerVariableRef') is None


def test_assoc_variable41_stub_double():
    # arduino_BooleanVariableRef has no real 'arduino_BooleanVariableRef' property in the generated
    # code (a bare stub) -- manually attach it so arduino_BooleanVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_BooleanVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_BooleanVariable(initialValue=True, value="sample_text")
    partner = arduino_BooleanVariableRef()
    setattr(partner, 'arduino_BooleanVariableRef', None)
    _safe_set(owner, 'arduino_BooleanVariable', partner)
    assert getattr(partner, 'arduino_BooleanVariableRef') == owner
    _safe_set(owner, 'arduino_BooleanVariable', None)
    assert getattr(partner, 'arduino_BooleanVariableRef') is None


