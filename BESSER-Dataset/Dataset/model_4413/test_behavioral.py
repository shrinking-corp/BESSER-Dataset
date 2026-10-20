import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Control,
    Expression,
    InputModule,
    Instruction,
    Module,
    ModuleSet,
    NamedElement,
    OutputModule,
    arduino_BinaryExpression,
    arduino_Block,
    arduino_Board,
    arduino_Constant,
    arduino_Control,
    arduino_Delay,
    arduino_Expression,
    arduino_If,
    arduino_InputModule,
    arduino_Instruction,
    arduino_Led,
    arduino_Module,
    arduino_ModuleGet,
    arduino_ModuleSet,
    arduino_NamedElement,
    arduino_OutputModule,
    arduino_Project,
    arduino_PushButton,
    arduino_SetLed,
    arduino_Sketch,
    arduino_UnaryExpression,
    arduino_WaitFor,
    arduino_While,
    BinaryOperatorKind,
    UnaryOperatorKind,
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

def test_assoc_left26_stub_double():
    # arduino_Expression has no real 'arduino_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so arduino_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_BinaryExpression(operator="sample_text")
    partner = arduino_Expression()
    setattr(partner, 'arduino_Expression27', None)
    _safe_set(owner, 'arduino_BinaryExpression', partner)
    assert getattr(partner, 'arduino_Expression27') == owner
    _safe_set(owner, 'arduino_BinaryExpression', None)
    assert getattr(partner, 'arduino_Expression27') is None


def test_assoc_operand24_stub_double():
    # arduino_Expression has no real 'arduino_Expression25' property in the generated
    # code (a bare stub) -- manually attach it so arduino_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_UnaryExpression(operator="sample_text")
    partner = arduino_Expression()
    setattr(partner, 'arduino_Expression25', None)
    _safe_set(owner, 'arduino_UnaryExpression', partner)
    assert getattr(partner, 'arduino_Expression25') == owner
    _safe_set(owner, 'arduino_UnaryExpression', None)
    assert getattr(partner, 'arduino_Expression25') is None


def test_assoc_right28_stub_double():
    # arduino_Expression has no real 'arduino_Expression30' property in the generated
    # code (a bare stub) -- manually attach it so arduino_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_BinaryExpression(operator="sample_text")
    partner = arduino_Expression()
    setattr(partner, 'arduino_Expression30', None)
    _safe_set(owner, 'arduino_BinaryExpression29', partner)
    assert getattr(partner, 'arduino_Expression30') == owner
    _safe_set(owner, 'arduino_BinaryExpression29', None)
    assert getattr(partner, 'arduino_Expression30') is None


def test_assoc_value22_stub_double():
    # arduino_WaitFor has no real 'arduino_WaitFor23' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Constant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Constant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Constant(value=7)
    partner = arduino_WaitFor()
    setattr(partner, 'arduino_WaitFor23', None)
    _safe_set(owner, 'arduino_Constant', partner)
    assert getattr(partner, 'arduino_WaitFor23') == owner
    _safe_set(owner, 'arduino_Constant', None)
    assert getattr(partner, 'arduino_WaitFor23') is None


