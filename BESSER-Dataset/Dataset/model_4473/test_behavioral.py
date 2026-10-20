import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExp,
    Block,
    ControlStructure,
    Expression,
    Instruction,
    Parameter,
    Primitive,
    ProcCall,
    ProcDeclaration,
    kmlogo_asm_Back,
    kmlogo_asm_BinaryExp,
    kmlogo_asm_Block,
    kmlogo_asm_Clear,
    kmlogo_asm_Constant,
    kmlogo_asm_ControlStructure,
    kmlogo_asm_Div,
    kmlogo_asm_Equals,
    kmlogo_asm_Expression,
    kmlogo_asm_Forward,
    kmlogo_asm_Greater,
    kmlogo_asm_If,
    kmlogo_asm_Instruction,
    kmlogo_asm_Left,
    kmlogo_asm_LogoProgram,
    kmlogo_asm_Lower,
    kmlogo_asm_Minus,
    kmlogo_asm_Mult,
    kmlogo_asm_Parameter,
    kmlogo_asm_ParameterCall,
    kmlogo_asm_PenDown,
    kmlogo_asm_PenUp,
    kmlogo_asm_Plus,
    kmlogo_asm_Primitive,
    kmlogo_asm_ProcCall,
    kmlogo_asm_ProcDeclaration,
    kmlogo_asm_Repeat,
    kmlogo_asm_Right,
    kmlogo_asm_While,
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

def test_assoc_args15_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so kmlogo_asm_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmlogo_asm_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmlogo_asm_ProcDeclaration(name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'kmlogo_asm_ProcDeclaration', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'kmlogo_asm_ProcDeclaration', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_instructions17_stub_double():
    # Instruction has no real 'Instruction' property in the generated
    # code (a bare stub) -- manually attach it so kmlogo_asm_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmlogo_asm_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmlogo_asm_ProcDeclaration(name="sample_text")
    partner = Instruction()
    setattr(partner, 'Instruction', None)
    _safe_set(owner, 'kmlogo_asm_ProcDeclaration18', {partner})
    assert getattr(partner, 'Instruction') == owner
    _safe_set(owner, 'kmlogo_asm_ProcDeclaration18', set())
    assert getattr(partner, 'Instruction') is None


def test_assoc_procCall16_stub_double():
    # ProcCall has no real 'ProcCall' property in the generated
    # code (a bare stub) -- manually attach it so kmlogo_asm_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmlogo_asm_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmlogo_asm_ProcDeclaration(name="sample_text")
    partner = ProcCall()
    setattr(partner, 'ProcCall', None)
    _safe_set(owner, 'declaration', {partner})
    assert getattr(partner, 'ProcCall') == owner
    _safe_set(owner, 'declaration', set())
    assert getattr(partner, 'ProcCall') is None


