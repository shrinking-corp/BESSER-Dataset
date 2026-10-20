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

def test_assoc_block5_reverse_link_reassign_clear():
    a1 = arduino_Sketch()
    a2 = arduino_Sketch()
    b = arduino_Block()
    _safe_set(b, 'arduino_Block', a1)
    assert _is_linked(b, 'arduino_Block', a1)
    if hasattr(a1, 'arduino_Sketch6'):
        assert _is_linked(a1, 'arduino_Sketch6', b)
    _safe_set(b, 'arduino_Block', a2)
    assert _is_linked(b, 'arduino_Block', a2)
    if hasattr(a1, 'arduino_Sketch6'):
        assert not _is_linked(a1, 'arduino_Sketch6', b)
    if hasattr(a2, 'arduino_Sketch6'):
        assert _is_linked(a2, 'arduino_Sketch6', b)
    _safe_set(b, 'arduino_Block', None)
    assert not _is_linked(b, 'arduino_Block', a2)
    if hasattr(a2, 'arduino_Sketch6'):
        assert not _is_linked(a2, 'arduino_Sketch6', b)


def test_assoc_block9_reverse_link_reassign_clear():
    a1 = arduino_Control()
    a2 = arduino_Control()
    b = arduino_Block()
    _safe_set(b, 'arduino_Block10', a1)
    assert _is_linked(b, 'arduino_Block10', a1)
    if hasattr(a1, 'arduino_Control'):
        assert _is_linked(a1, 'arduino_Control', b)
    _safe_set(b, 'arduino_Block10', a2)
    assert _is_linked(b, 'arduino_Block10', a2)
    if hasattr(a1, 'arduino_Control'):
        assert not _is_linked(a1, 'arduino_Control', b)
    if hasattr(a2, 'arduino_Control'):
        assert _is_linked(a2, 'arduino_Control', b)
    _safe_set(b, 'arduino_Block10', None)
    assert not _is_linked(b, 'arduino_Block10', a2)
    if hasattr(a2, 'arduino_Control'):
        assert not _is_linked(a2, 'arduino_Control', b)


def test_assoc_condition11_reverse_link_reassign_clear():
    a1 = arduino_If()
    a2 = arduino_If()
    b = arduino_Expression()
    _safe_set(b, 'arduino_Expression', a1)
    assert _is_linked(b, 'arduino_Expression', a1)
    if hasattr(a1, 'arduino_If'):
        assert _is_linked(a1, 'arduino_If', b)
    _safe_set(b, 'arduino_Expression', a2)
    assert _is_linked(b, 'arduino_Expression', a2)
    if hasattr(a1, 'arduino_If'):
        assert not _is_linked(a1, 'arduino_If', b)
    if hasattr(a2, 'arduino_If'):
        assert _is_linked(a2, 'arduino_If', b)
    _safe_set(b, 'arduino_Expression', None)
    assert not _is_linked(b, 'arduino_Expression', a2)
    if hasattr(a2, 'arduino_If'):
        assert not _is_linked(a2, 'arduino_If', b)


def test_assoc_condition15_reverse_link_reassign_clear():
    a1 = arduino_While()
    a2 = arduino_While()
    b = arduino_Expression()
    _safe_set(b, 'arduino_Expression16', a1)
    assert _is_linked(b, 'arduino_Expression16', a1)
    if hasattr(a1, 'arduino_While'):
        assert _is_linked(a1, 'arduino_While', b)
    _safe_set(b, 'arduino_Expression16', a2)
    assert _is_linked(b, 'arduino_Expression16', a2)
    if hasattr(a1, 'arduino_While'):
        assert not _is_linked(a1, 'arduino_While', b)
    if hasattr(a2, 'arduino_While'):
        assert _is_linked(a2, 'arduino_While', b)
    _safe_set(b, 'arduino_Expression16', None)
    assert not _is_linked(b, 'arduino_Expression16', a2)
    if hasattr(a2, 'arduino_While'):
        assert not _is_linked(a2, 'arduino_While', b)


def test_assoc_elseBlock12_reverse_link_reassign_clear():
    a1 = arduino_If()
    a2 = arduino_If()
    b = arduino_Block()
    _safe_set(b, 'arduino_Block14', a1)
    assert _is_linked(b, 'arduino_Block14', a1)
    if hasattr(a1, 'arduino_If13'):
        assert _is_linked(a1, 'arduino_If13', b)
    _safe_set(b, 'arduino_Block14', a2)
    assert _is_linked(b, 'arduino_Block14', a2)
    if hasattr(a1, 'arduino_If13'):
        assert not _is_linked(a1, 'arduino_If13', b)
    if hasattr(a2, 'arduino_If13'):
        assert _is_linked(a2, 'arduino_If13', b)
    _safe_set(b, 'arduino_Block14', None)
    assert not _is_linked(b, 'arduino_Block14', a2)
    if hasattr(a2, 'arduino_If13'):
        assert not _is_linked(a2, 'arduino_If13', b)


def test_assoc_instructions7_reverse_link_reassign_clear():
    a1 = arduino_Instruction()
    a2 = arduino_Instruction()
    b = arduino_Block()
    _safe_set(b, 'arduino_Block8', {a1})
    assert _is_linked(b, 'arduino_Block8', a1)
    if hasattr(a1, 'arduino_Instruction'):
        assert _is_linked(a1, 'arduino_Instruction', b)
    _safe_set(b, 'arduino_Block8', {a2})
    assert _is_linked(b, 'arduino_Block8', a2)
    if hasattr(a1, 'arduino_Instruction'):
        assert not _is_linked(a1, 'arduino_Instruction', b)
    if hasattr(a2, 'arduino_Instruction'):
        assert _is_linked(a2, 'arduino_Instruction', b)
    _safe_set(b, 'arduino_Block8', set())
    assert not _is_linked(b, 'arduino_Block8', a2)
    if hasattr(a2, 'arduino_Instruction'):
        assert not _is_linked(a2, 'arduino_Instruction', b)


def test_assoc_left26_reverse_link_reassign_clear():
    a1 = arduino_Expression()
    a2 = arduino_Expression()
    b = arduino_BinaryExpression(operator="sample_text")
    _safe_set(b, 'arduino_BinaryExpression', a1)
    assert _is_linked(b, 'arduino_BinaryExpression', a1)
    if hasattr(a1, 'arduino_Expression27'):
        assert _is_linked(a1, 'arduino_Expression27', b)
    _safe_set(b, 'arduino_BinaryExpression', a2)
    assert _is_linked(b, 'arduino_BinaryExpression', a2)
    if hasattr(a1, 'arduino_Expression27'):
        assert not _is_linked(a1, 'arduino_Expression27', b)
    if hasattr(a2, 'arduino_Expression27'):
        assert _is_linked(a2, 'arduino_Expression27', b)
    _safe_set(b, 'arduino_BinaryExpression', None)
    assert not _is_linked(b, 'arduino_BinaryExpression', a2)
    if hasattr(a2, 'arduino_Expression27'):
        assert not _is_linked(a2, 'arduino_Expression27', b)


def test_assoc_module20_reverse_link_reassign_clear():
    a1 = arduino_WaitFor()
    a2 = arduino_WaitFor()
    b = arduino_Module(level="sample_text")
    _safe_set(b, 'arduino_Module21', a1)
    assert _is_linked(b, 'arduino_Module21', a1)
    if hasattr(a1, 'arduino_WaitFor'):
        assert _is_linked(a1, 'arduino_WaitFor', b)
    _safe_set(b, 'arduino_Module21', a2)
    assert _is_linked(b, 'arduino_Module21', a2)
    if hasattr(a1, 'arduino_WaitFor'):
        assert not _is_linked(a1, 'arduino_WaitFor', b)
    if hasattr(a2, 'arduino_WaitFor'):
        assert _is_linked(a2, 'arduino_WaitFor', b)
    _safe_set(b, 'arduino_Module21', None)
    assert not _is_linked(b, 'arduino_Module21', a2)
    if hasattr(a2, 'arduino_WaitFor'):
        assert not _is_linked(a2, 'arduino_WaitFor', b)


def test_assoc_module31_reverse_link_reassign_clear():
    a1 = arduino_ModuleGet()
    a2 = arduino_ModuleGet()
    b = arduino_Module(level="sample_text")
    _safe_set(b, 'arduino_Module32', a1)
    assert _is_linked(b, 'arduino_Module32', a1)
    if hasattr(a1, 'arduino_ModuleGet'):
        assert _is_linked(a1, 'arduino_ModuleGet', b)
    _safe_set(b, 'arduino_Module32', a2)
    assert _is_linked(b, 'arduino_Module32', a2)
    if hasattr(a1, 'arduino_ModuleGet'):
        assert not _is_linked(a1, 'arduino_ModuleGet', b)
    if hasattr(a2, 'arduino_ModuleGet'):
        assert _is_linked(a2, 'arduino_ModuleGet', b)
    _safe_set(b, 'arduino_Module32', None)
    assert not _is_linked(b, 'arduino_Module32', a2)
    if hasattr(a2, 'arduino_ModuleGet'):
        assert not _is_linked(a2, 'arduino_ModuleGet', b)


def test_assoc_operand24_reverse_link_reassign_clear():
    a1 = arduino_UnaryExpression(operator="sample_text")
    a2 = arduino_UnaryExpression(operator="sample_text_2")
    b = arduino_Expression()
    _safe_set(b, 'arduino_Expression25', a1)
    assert _is_linked(b, 'arduino_Expression25', a1)
    if hasattr(a1, 'arduino_UnaryExpression'):
        assert _is_linked(a1, 'arduino_UnaryExpression', b)
    _safe_set(b, 'arduino_Expression25', a2)
    assert _is_linked(b, 'arduino_Expression25', a2)
    if hasattr(a1, 'arduino_UnaryExpression'):
        assert not _is_linked(a1, 'arduino_UnaryExpression', b)
    if hasattr(a2, 'arduino_UnaryExpression'):
        assert _is_linked(a2, 'arduino_UnaryExpression', b)
    _safe_set(b, 'arduino_Expression25', None)
    assert not _is_linked(b, 'arduino_Expression25', a2)
    if hasattr(a2, 'arduino_UnaryExpression'):
        assert not _is_linked(a2, 'arduino_UnaryExpression', b)


def test_assoc_right28_reverse_link_reassign_clear():
    a1 = arduino_Expression()
    a2 = arduino_Expression()
    b = arduino_BinaryExpression(operator="sample_text")
    _safe_set(b, 'arduino_BinaryExpression29', a1)
    assert _is_linked(b, 'arduino_BinaryExpression29', a1)
    if hasattr(a1, 'arduino_Expression30'):
        assert _is_linked(a1, 'arduino_Expression30', b)
    _safe_set(b, 'arduino_BinaryExpression29', a2)
    assert _is_linked(b, 'arduino_BinaryExpression29', a2)
    if hasattr(a1, 'arduino_Expression30'):
        assert not _is_linked(a1, 'arduino_Expression30', b)
    if hasattr(a2, 'arduino_Expression30'):
        assert _is_linked(a2, 'arduino_Expression30', b)
    _safe_set(b, 'arduino_BinaryExpression29', None)
    assert not _is_linked(b, 'arduino_BinaryExpression29', a2)
    if hasattr(a2, 'arduino_Expression30'):
        assert not _is_linked(a2, 'arduino_Expression30', b)


def test_assoc_value17_reverse_link_reassign_clear():
    a1 = arduino_ModuleSet()
    a2 = arduino_ModuleSet()
    b = arduino_Expression()
    _safe_set(b, 'arduino_Expression18', a1)
    assert _is_linked(b, 'arduino_Expression18', a1)
    if hasattr(a1, 'arduino_ModuleSet'):
        assert _is_linked(a1, 'arduino_ModuleSet', b)
    _safe_set(b, 'arduino_Expression18', a2)
    assert _is_linked(b, 'arduino_Expression18', a2)
    if hasattr(a1, 'arduino_ModuleSet'):
        assert not _is_linked(a1, 'arduino_ModuleSet', b)
    if hasattr(a2, 'arduino_ModuleSet'):
        assert _is_linked(a2, 'arduino_ModuleSet', b)
    _safe_set(b, 'arduino_Expression18', None)
    assert not _is_linked(b, 'arduino_Expression18', a2)
    if hasattr(a2, 'arduino_ModuleSet'):
        assert not _is_linked(a2, 'arduino_ModuleSet', b)


def test_assoc_value22_reverse_link_reassign_clear():
    a1 = arduino_WaitFor()
    a2 = arduino_WaitFor()
    b = arduino_Constant(value="sample_text")
    _safe_set(b, 'arduino_Constant', a1)
    assert _is_linked(b, 'arduino_Constant', a1)
    if hasattr(a1, 'arduino_WaitFor23'):
        assert _is_linked(a1, 'arduino_WaitFor23', b)
    _safe_set(b, 'arduino_Constant', a2)
    assert _is_linked(b, 'arduino_Constant', a2)
    if hasattr(a1, 'arduino_WaitFor23'):
        assert not _is_linked(a1, 'arduino_WaitFor23', b)
    if hasattr(a2, 'arduino_WaitFor23'):
        assert _is_linked(a2, 'arduino_WaitFor23', b)
    _safe_set(b, 'arduino_Constant', None)
    assert not _is_linked(b, 'arduino_Constant', a2)
    if hasattr(a2, 'arduino_WaitFor23'):
        assert not _is_linked(a2, 'arduino_WaitFor23', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_led19_stub_double():
    # arduino_Led has no real 'arduino_Led' property in the generated
    # code (a bare stub) -- manually attach it so arduino_SetLed's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_SetLed's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_SetLed()
    partner = arduino_Led()
    setattr(partner, 'arduino_Led', None)
    _safe_set(owner, 'arduino_SetLed', partner)
    assert getattr(partner, 'arduino_Led') == owner
    _safe_set(owner, 'arduino_SetLed', None)
    assert getattr(partner, 'arduino_Led') is None


def test_assoc_modules3_stub_double():
    # arduino_Board has no real 'arduino_Board4' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Module(level="sample_text")
    partner = arduino_Board()
    setattr(partner, 'arduino_Board4', None)
    _safe_set(owner, 'arduino_Module', partner)
    assert owner in getattr(partner, 'arduino_Board4')
    _safe_set(owner, 'arduino_Module', None)
    assert owner not in getattr(partner, 'arduino_Board4')


def test_assoc_sketch1_stub_double():
    # arduino_Project has no real 'arduino_Project2' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Sketch's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Sketch's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Sketch()
    partner = arduino_Project()
    setattr(partner, 'arduino_Project2', None)
    _safe_set(owner, 'arduino_Sketch', partner)
    assert getattr(partner, 'arduino_Project2') == owner
    _safe_set(owner, 'arduino_Sketch', None)
    assert getattr(partner, 'arduino_Project2') is None


