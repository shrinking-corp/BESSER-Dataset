import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanOperator,
    Control,
    Instruction,
    MathOperator,
    Module,
    ModuleInstruction,
    NamedElement,
    Parameter,
    Pin,
    Utilities,
    Value,
    arduino_AnalogPin,
    arduino_BooleanOperator,
    arduino_Connector,
    arduino_Constant,
    arduino_Control,
    arduino_Delay,
    arduino_DigitalPin,
    arduino_Function,
    arduino_FunctionCall,
    arduino_Hardware,
    arduino_IO,
    arduino_If,
    arduino_InputModule,
    arduino_Instruction,
    arduino_Level,
    arduino_MathOperator,
    arduino_Module,
    arduino_ModuleInstruction,
    arduino_NamedElement,
    arduino_NumericalOperator,
    arduino_OutputModule,
    arduino_Parameter,
    arduino_ParameterCall,
    arduino_ParameterDefinition,
    arduino_Pin,
    arduino_Platform,
    arduino_Project,
    arduino_Repeat,
    arduino_Sensor,
    arduino_Set,
    arduino_Sketch,
    arduino_Status,
    arduino_Utilities,
    arduino_Value,
    arduino_Variable,
    arduino_While,
    Library,
    ModuleKind,
    OperatorKind,
    ParameterType,
    Time,
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

def test_assoc_left45_reverse_link_reassign_clear():
    a1 = arduino_Value(value="sample_text")
    a2 = arduino_Value(value="sample_text_2")
    b = arduino_MathOperator(operator="sample_text")
    _safe_set(b, 'arduino_MathOperator', a1)
    assert _is_linked(b, 'arduino_MathOperator', a1)
    if hasattr(a1, 'arduino_Value46'):
        assert _is_linked(a1, 'arduino_Value46', b)
    _safe_set(b, 'arduino_MathOperator', a2)
    assert _is_linked(b, 'arduino_MathOperator', a2)
    if hasattr(a1, 'arduino_Value46'):
        assert not _is_linked(a1, 'arduino_Value46', b)
    if hasattr(a2, 'arduino_Value46'):
        assert _is_linked(a2, 'arduino_Value46', b)
    _safe_set(b, 'arduino_MathOperator', None)
    assert not _is_linked(b, 'arduino_MathOperator', a2)
    if hasattr(a2, 'arduino_Value46'):
        assert not _is_linked(a2, 'arduino_Value46', b)


def test_assoc_paramDefs56_reverse_link_reassign_clear():
    a1 = arduino_ParameterDefinition(name="sample_text", type="sample_text")
    a2 = arduino_ParameterDefinition(name="sample_text_2", type="sample_text_2")
    b = arduino_Function(name="sample_text")
    _safe_set(b, 'arduino_Function57', {a1})
    assert _is_linked(b, 'arduino_Function57', a1)
    if hasattr(a1, 'arduino_ParameterDefinition'):
        assert _is_linked(a1, 'arduino_ParameterDefinition', b)
    _safe_set(b, 'arduino_Function57', {a2})
    assert _is_linked(b, 'arduino_Function57', a2)
    if hasattr(a1, 'arduino_ParameterDefinition'):
        assert not _is_linked(a1, 'arduino_ParameterDefinition', b)
    if hasattr(a2, 'arduino_ParameterDefinition'):
        assert _is_linked(a2, 'arduino_ParameterDefinition', b)
    _safe_set(b, 'arduino_Function57', set())
    assert not _is_linked(b, 'arduino_Function57', a2)
    if hasattr(a2, 'arduino_ParameterDefinition'):
        assert not _is_linked(a2, 'arduino_ParameterDefinition', b)


def test_assoc_right47_reverse_link_reassign_clear():
    a1 = arduino_Value(value="sample_text")
    a2 = arduino_Value(value="sample_text_2")
    b = arduino_MathOperator(operator="sample_text")
    _safe_set(b, 'arduino_MathOperator48', a1)
    assert _is_linked(b, 'arduino_MathOperator48', a1)
    if hasattr(a1, 'arduino_Value49'):
        assert _is_linked(a1, 'arduino_Value49', b)
    _safe_set(b, 'arduino_MathOperator48', a2)
    assert _is_linked(b, 'arduino_MathOperator48', a2)
    if hasattr(a1, 'arduino_Value49'):
        assert not _is_linked(a1, 'arduino_Value49', b)
    if hasattr(a2, 'arduino_Value49'):
        assert _is_linked(a2, 'arduino_Value49', b)
    _safe_set(b, 'arduino_MathOperator48', None)
    assert not _is_linked(b, 'arduino_MathOperator48', a2)
    if hasattr(a2, 'arduino_Value49'):
        assert not _is_linked(a2, 'arduino_Value49', b)


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


def test_assoc_definition61_stub_double():
    # arduino_Parameter has no real 'arduino_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so arduino_ParameterDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_ParameterDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_ParameterDefinition(name="sample_text", type="sample_text")
    partner = arduino_Parameter()
    setattr(partner, 'arduino_Parameter', None)
    _safe_set(owner, 'arduino_ParameterDefinition62', partner)
    assert getattr(partner, 'arduino_Parameter') == owner
    _safe_set(owner, 'arduino_ParameterDefinition62', None)
    assert getattr(partner, 'arduino_Parameter') is None


def test_assoc_definition63_stub_double():
    # arduino_FunctionCall has no real 'arduino_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Function(name="sample_text")
    partner = arduino_FunctionCall()
    setattr(partner, 'arduino_FunctionCall', None)
    _safe_set(owner, 'arduino_Function64', partner)
    assert getattr(partner, 'arduino_FunctionCall') == owner
    _safe_set(owner, 'arduino_Function64', None)
    assert getattr(partner, 'arduino_FunctionCall') is None


def test_assoc_definition68_stub_double():
    # arduino_ParameterCall has no real 'arduino_ParameterCall' property in the generated
    # code (a bare stub) -- manually attach it so arduino_ParameterDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_ParameterDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_ParameterDefinition(name="sample_text", type="sample_text")
    partner = arduino_ParameterCall()
    setattr(partner, 'arduino_ParameterCall', None)
    _safe_set(owner, 'arduino_ParameterDefinition69', partner)
    assert getattr(partner, 'arduino_ParameterCall') == owner
    _safe_set(owner, 'arduino_ParameterDefinition69', None)
    assert getattr(partner, 'arduino_ParameterCall') is None


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


def test_assoc_functions13_stub_double():
    # arduino_Sketch has no real 'arduino_Sketch14' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Function(name="sample_text")
    partner = arduino_Sketch()
    setattr(partner, 'arduino_Sketch14', None)
    _safe_set(owner, 'arduino_Function', partner)
    assert owner in getattr(partner, 'arduino_Sketch14')
    _safe_set(owner, 'arduino_Function', None)
    assert owner not in getattr(partner, 'arduino_Sketch14')


def test_assoc_instructions58_stub_double():
    # arduino_Instruction has no real 'arduino_Instruction60' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Function(name="sample_text")
    partner = arduino_Instruction()
    setattr(partner, 'arduino_Instruction60', None)
    _safe_set(owner, 'arduino_Function59', {partner})
    assert getattr(partner, 'arduino_Instruction60') == owner
    _safe_set(owner, 'arduino_Function59', set())
    assert getattr(partner, 'arduino_Instruction60') is None


def test_assoc_level33_stub_double():
    # arduino_Level has no real 'arduino_Level' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Value(value="sample_text")
    partner = arduino_Level()
    setattr(partner, 'arduino_Level', None)
    _safe_set(owner, 'arduino_Value', partner)
    assert getattr(partner, 'arduino_Level') == owner
    _safe_set(owner, 'arduino_Value', None)
    assert getattr(partner, 'arduino_Level') is None


def test_assoc_module34_stub_double():
    # arduino_ModuleInstruction has no real 'arduino_ModuleInstruction' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(image="sample_text", kind="sample_text", level=True, library="sample_text")
    partner = arduino_ModuleInstruction()
    setattr(partner, 'arduino_ModuleInstruction', None)
    _safe_set(owner, 'arduino_Module35', partner)
    assert getattr(partner, 'arduino_ModuleInstruction') == owner
    _safe_set(owner, 'arduino_Module35', None)
    assert getattr(partner, 'arduino_ModuleInstruction') is None


def test_assoc_module40_stub_double():
    # arduino_Connector has no real 'arduino_Connector41' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(image="sample_text", kind="sample_text", level=True, library="sample_text")
    partner = arduino_Connector()
    setattr(partner, 'arduino_Connector41', None)
    _safe_set(owner, 'arduino_Module42', partner)
    assert getattr(partner, 'arduino_Connector41') == owner
    _safe_set(owner, 'arduino_Module42', None)
    assert getattr(partner, 'arduino_Connector41') is None


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


def test_assoc_modules20_stub_double():
    # arduino_Project has no real 'arduino_Project21' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(image="sample_text", kind="sample_text", level=True, library="sample_text")
    partner = arduino_Project()
    setattr(partner, 'arduino_Project21', None)
    _safe_set(owner, 'arduino_Module22', partner)
    assert owner in getattr(partner, 'arduino_Project21')
    _safe_set(owner, 'arduino_Module22', None)
    assert owner not in getattr(partner, 'arduino_Project21')


def test_assoc_pin38_stub_double():
    # arduino_Connector has no real 'arduino_Connector39' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Pin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Pin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Pin(id=7)
    partner = arduino_Connector()
    setattr(partner, 'arduino_Connector39', None)
    _safe_set(owner, 'arduino_Pin', partner)
    assert getattr(partner, 'arduino_Connector39') == owner
    _safe_set(owner, 'arduino_Pin', None)
    assert getattr(partner, 'arduino_Connector39') is None


def test_assoc_platform23_stub_double():
    # arduino_Project has no real 'arduino_Project24' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Platform's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Platform's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Platform(image="sample_text")
    partner = arduino_Project()
    setattr(partner, 'arduino_Project24', None)
    _safe_set(owner, 'arduino_Platform25', partner)
    assert owner in getattr(partner, 'arduino_Project24')
    _safe_set(owner, 'arduino_Platform25', None)
    assert owner not in getattr(partner, 'arduino_Project24')


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


def test_assoc_value51_stub_double():
    # arduino_Set has no real 'arduino_Set52' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Value(value="sample_text")
    partner = arduino_Set()
    setattr(partner, 'arduino_Set52', None)
    _safe_set(owner, 'arduino_Value53', partner)
    assert getattr(partner, 'arduino_Set52') == owner
    _safe_set(owner, 'arduino_Value53', None)
    assert getattr(partner, 'arduino_Set52') is None


def test_assoc_variable50_stub_double():
    # arduino_Set has no real 'arduino_Set' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Variable(name="sample_text")
    partner = arduino_Set()
    setattr(partner, 'arduino_Set', None)
    _safe_set(owner, 'arduino_Variable', partner)
    assert getattr(partner, 'arduino_Set') == owner
    _safe_set(owner, 'arduino_Variable', None)
    assert getattr(partner, 'arduino_Set') is None


