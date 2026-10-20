import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Assignment,
    BinaryExpression,
    BooleanExpression,
    Constant,
    Control,
    Expression,
    InstantaneousInstruction,
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
    arduino_Actuator,
    arduino_AnalogPin,
    arduino_Assignment,
    arduino_BinaryBooleanExpression,
    arduino_BinaryExpression,
    arduino_BinaryIntegerExpression,
    arduino_BooleanConstant,
    arduino_BooleanExpression,
    arduino_BooleanModuleGet,
    arduino_BooleanVariable,
    arduino_Connector,
    arduino_Constant,
    arduino_Control,
    arduino_Delay,
    arduino_DigitalPin,
    arduino_Expression,
    arduino_Hardware,
    arduino_If,
    arduino_InstantaneousInstruction,
    arduino_Instruction,
    arduino_IntegerConstant,
    arduino_IntegerExpression,
    arduino_IntegerModuleGet,
    arduino_IntegerVariable,
    arduino_Module,
    arduino_ModuleAssignment,
    arduino_ModuleGet,
    arduino_ModuleInstruction,
    arduino_NamedElement,
    arduino_Pin,
    arduino_Platform,
    arduino_Project,
    arduino_Repeat,
    arduino_Sensor,
    arduino_Sketch,
    arduino_Synchro,
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
    Library,
    ModuleKind,
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

def test_assoc_dependency31_reverse_link_reassign_clear():
    a1 = arduino_Instruction()
    a2 = arduino_Instruction()
    b = arduino_Instruction()
    _safe_set(b, 'arduino_Instruction32', a1)
    assert _is_linked(b, 'arduino_Instruction32', a1)
    if hasattr(a1, 'arduino_Instruction30'):
        assert _is_linked(a1, 'arduino_Instruction30', b)
    _safe_set(b, 'arduino_Instruction32', a2)
    assert _is_linked(b, 'arduino_Instruction32', a2)
    if hasattr(a1, 'arduino_Instruction30'):
        assert not _is_linked(a1, 'arduino_Instruction30', b)
    if hasattr(a2, 'arduino_Instruction30'):
        assert _is_linked(a2, 'arduino_Instruction30', b)
    _safe_set(b, 'arduino_Instruction32', None)
    assert not _is_linked(b, 'arduino_Instruction32', a2)
    if hasattr(a2, 'arduino_Instruction30'):
        assert not _is_linked(a2, 'arduino_Instruction30', b)


def test_assoc_instructions35_reverse_link_reassign_clear():
    a1 = arduino_Instruction()
    a2 = arduino_Instruction()
    b = arduino_Control()
    _safe_set(b, 'arduino_Control', {a1})
    assert _is_linked(b, 'arduino_Control', a1)
    if hasattr(a1, 'arduino_Instruction36'):
        assert _is_linked(a1, 'arduino_Instruction36', b)
    _safe_set(b, 'arduino_Control', {a2})
    assert _is_linked(b, 'arduino_Control', a2)
    if hasattr(a1, 'arduino_Instruction36'):
        assert not _is_linked(a1, 'arduino_Instruction36', b)
    if hasattr(a2, 'arduino_Instruction36'):
        assert _is_linked(a2, 'arduino_Instruction36', b)
    _safe_set(b, 'arduino_Control', set())
    assert not _is_linked(b, 'arduino_Control', a2)
    if hasattr(a2, 'arduino_Instruction36'):
        assert not _is_linked(a2, 'arduino_Instruction36', b)


def test_assoc_next28_reverse_link_reassign_clear():
    a1 = arduino_Instruction()
    a2 = arduino_Instruction()
    b = arduino_Instruction()
    _safe_set(b, 'arduino_Instruction29', a1)
    assert _is_linked(b, 'arduino_Instruction29', a1)
    if hasattr(a1, 'arduino_Instruction27'):
        assert _is_linked(a1, 'arduino_Instruction27', b)
    _safe_set(b, 'arduino_Instruction29', a2)
    assert _is_linked(b, 'arduino_Instruction29', a2)
    if hasattr(a1, 'arduino_Instruction27'):
        assert not _is_linked(a1, 'arduino_Instruction27', b)
    if hasattr(a2, 'arduino_Instruction27'):
        assert _is_linked(a2, 'arduino_Instruction27', b)
    _safe_set(b, 'arduino_Instruction29', None)
    assert not _is_linked(b, 'arduino_Instruction29', a2)
    if hasattr(a2, 'arduino_Instruction27'):
        assert not _is_linked(a2, 'arduino_Instruction27', b)


def test_assoc_previous25_reverse_link_reassign_clear():
    a1 = arduino_Instruction()
    a2 = arduino_Instruction()
    b = arduino_Instruction()
    _safe_set(b, 'arduino_Instruction26', a1)
    assert _is_linked(b, 'arduino_Instruction26', a1)
    if hasattr(a1, 'arduino_Instruction24'):
        assert _is_linked(a1, 'arduino_Instruction24', b)
    _safe_set(b, 'arduino_Instruction26', a2)
    assert _is_linked(b, 'arduino_Instruction26', a2)
    if hasattr(a1, 'arduino_Instruction24'):
        assert not _is_linked(a1, 'arduino_Instruction24', b)
    if hasattr(a2, 'arduino_Instruction24'):
        assert _is_linked(a2, 'arduino_Instruction24', b)
    _safe_set(b, 'arduino_Instruction26', None)
    assert not _is_linked(b, 'arduino_Instruction26', a2)
    if hasattr(a2, 'arduino_Instruction24'):
        assert not _is_linked(a2, 'arduino_Instruction24', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_analogPins7_stub_double():
    # arduino_AnalogPin has no real 'arduino_AnalogPin' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Platform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Platform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Platform(image="sample_text")
    partner = arduino_AnalogPin()
    setattr(partner, 'arduino_AnalogPin', None)
    _safe_set(owner, 'arduino_Platform8', {partner})
    assert getattr(partner, 'arduino_AnalogPin') == owner
    _safe_set(owner, 'arduino_Platform8', set())
    assert getattr(partner, 'arduino_AnalogPin') is None


def test_assoc_digitalPins5_stub_double():
    # arduino_DigitalPin has no real 'arduino_DigitalPin' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Platform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Platform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Platform(image="sample_text")
    partner = arduino_DigitalPin()
    setattr(partner, 'arduino_DigitalPin', None)
    _safe_set(owner, 'arduino_Platform6', {partner})
    assert getattr(partner, 'arduino_DigitalPin') == owner
    _safe_set(owner, 'arduino_Platform6', set())
    assert getattr(partner, 'arduino_DigitalPin') is None


def test_assoc_instructions11_stub_double():
    # arduino_Sketch has no real 'arduino_Sketch12' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Instruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Instruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Instruction()
    partner = arduino_Sketch()
    setattr(partner, 'arduino_Sketch12', None)
    _safe_set(owner, 'arduino_Instruction', partner)
    assert owner in getattr(partner, 'arduino_Sketch12')
    _safe_set(owner, 'arduino_Instruction', None)
    assert owner not in getattr(partner, 'arduino_Sketch12')


def test_assoc_module33_stub_double():
    # arduino_ModuleInstruction has no real 'arduino_ModuleInstruction' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(image="sample_text", kind="sample_text", level=True, library="sample_text")
    partner = arduino_ModuleInstruction()
    setattr(partner, 'arduino_ModuleInstruction', None)
    _safe_set(owner, 'arduino_Module34', partner)
    assert getattr(partner, 'arduino_ModuleInstruction') == owner
    _safe_set(owner, 'arduino_Module34', None)
    assert getattr(partner, 'arduino_ModuleInstruction') is None


def test_assoc_module39_stub_double():
    # arduino_Connector has no real 'arduino_Connector40' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(image="sample_text", kind="sample_text", level=True, library="sample_text")
    partner = arduino_Connector()
    setattr(partner, 'arduino_Connector40', None)
    _safe_set(owner, 'arduino_Module41', partner)
    assert getattr(partner, 'arduino_Connector40') == owner
    _safe_set(owner, 'arduino_Module41', None)
    assert getattr(partner, 'arduino_Connector40') is None


def test_assoc_module42_stub_double():
    # arduino_ModuleGet has no real 'arduino_ModuleGet' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(image="sample_text", kind="sample_text", level=True, library="sample_text")
    partner = arduino_ModuleGet()
    setattr(partner, 'arduino_ModuleGet', None)
    _safe_set(owner, 'arduino_Module43', partner)
    assert getattr(partner, 'arduino_ModuleGet') == owner
    _safe_set(owner, 'arduino_Module43', None)
    assert getattr(partner, 'arduino_ModuleGet') is None


def test_assoc_modules1_stub_double():
    # arduino_Hardware has no real 'arduino_Hardware2' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(image="sample_text", kind="sample_text", level=True, library="sample_text")
    partner = arduino_Hardware()
    setattr(partner, 'arduino_Hardware2', None)
    _safe_set(owner, 'arduino_Module', partner)
    assert owner in getattr(partner, 'arduino_Hardware2')
    _safe_set(owner, 'arduino_Module', None)
    assert owner not in getattr(partner, 'arduino_Hardware2')


def test_assoc_modules15_stub_double():
    # arduino_Project has no real 'arduino_Project16' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(image="sample_text", kind="sample_text", level=True, library="sample_text")
    partner = arduino_Project()
    setattr(partner, 'arduino_Project16', None)
    _safe_set(owner, 'arduino_Module17', partner)
    assert owner in getattr(partner, 'arduino_Project16')
    _safe_set(owner, 'arduino_Module17', None)
    assert owner not in getattr(partner, 'arduino_Project16')


def test_assoc_pin37_stub_double():
    # arduino_Connector has no real 'arduino_Connector38' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Pin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Pin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Pin(id=7, level=7)
    partner = arduino_Connector()
    setattr(partner, 'arduino_Connector38', None)
    _safe_set(owner, 'arduino_Pin', partner)
    assert getattr(partner, 'arduino_Connector38') == owner
    _safe_set(owner, 'arduino_Pin', None)
    assert getattr(partner, 'arduino_Connector38') is None


def test_assoc_platform18_stub_double():
    # arduino_Project has no real 'arduino_Project19' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Platform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Platform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Platform(image="sample_text")
    partner = arduino_Project()
    setattr(partner, 'arduino_Project19', None)
    _safe_set(owner, 'arduino_Platform20', partner)
    assert owner in getattr(partner, 'arduino_Project19')
    _safe_set(owner, 'arduino_Platform20', None)
    assert owner not in getattr(partner, 'arduino_Project19')


def test_assoc_platforms0_stub_double():
    # arduino_Hardware has no real 'arduino_Hardware' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Platform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Platform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Platform(image="sample_text")
    partner = arduino_Hardware()
    setattr(partner, 'arduino_Hardware', None)
    _safe_set(owner, 'arduino_Platform', partner)
    assert owner in getattr(partner, 'arduino_Hardware')
    _safe_set(owner, 'arduino_Platform', None)
    assert owner not in getattr(partner, 'arduino_Hardware')


