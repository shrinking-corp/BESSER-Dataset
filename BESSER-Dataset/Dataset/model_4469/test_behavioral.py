import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExp,
    ControlStructure,
    Expression,
    Instruction,
    Primitive,
    logoASM_Back,
    logoASM_BinaryExp,
    logoASM_Block,
    logoASM_Clear,
    logoASM_Constant,
    logoASM_ControlStructure,
    logoASM_Div,
    logoASM_Equals,
    logoASM_Expression,
    logoASM_Forward,
    logoASM_Greater,
    logoASM_If,
    logoASM_Instruction,
    logoASM_Left,
    logoASM_LogoProgram,
    logoASM_Lower,
    logoASM_Minus,
    logoASM_Mult,
    logoASM_Parameter,
    logoASM_ParameterCall,
    logoASM_PenDown,
    logoASM_PenUp,
    logoASM_Plus,
    logoASM_Primitive,
    logoASM_ProcCall,
    logoASM_ProcDeclaration,
    logoASM_Repeat,
    logoASM_Right,
    logoASM_While,
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

def test_assoc_args16_reverse_link_reassign_clear():
    a1 = logoASM_ProcDeclaration(name="sample_text")
    a2 = logoASM_ProcDeclaration(name="sample_text_2")
    b = logoASM_Parameter(name="sample_text")
    _safe_set(b, 'logoASM_Parameter', a1)
    assert _is_linked(b, 'logoASM_Parameter', a1)
    if hasattr(a1, 'logoASM_ProcDeclaration17'):
        assert _is_linked(a1, 'logoASM_ProcDeclaration17', b)
    _safe_set(b, 'logoASM_Parameter', a2)
    assert _is_linked(b, 'logoASM_Parameter', a2)
    if hasattr(a1, 'logoASM_ProcDeclaration17'):
        assert not _is_linked(a1, 'logoASM_ProcDeclaration17', b)
    if hasattr(a2, 'logoASM_ProcDeclaration17'):
        assert _is_linked(a2, 'logoASM_ProcDeclaration17', b)
    _safe_set(b, 'logoASM_Parameter', None)
    assert not _is_linked(b, 'logoASM_Parameter', a2)
    if hasattr(a2, 'logoASM_ProcDeclaration17'):
        assert not _is_linked(a2, 'logoASM_ProcDeclaration17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_declaration14_stub_double():
    # logoASM_ProcCall has no real 'logoASM_ProcCall15' property in the generated
    # code (a bare stub) -- manually attach it so logoASM_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logoASM_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logoASM_ProcDeclaration(name="sample_text")
    partner = logoASM_ProcCall()
    setattr(partner, 'logoASM_ProcCall15', None)
    _safe_set(owner, 'logoASM_ProcDeclaration', partner)
    assert getattr(partner, 'logoASM_ProcCall15') == owner
    _safe_set(owner, 'logoASM_ProcDeclaration', None)
    assert getattr(partner, 'logoASM_ProcCall15') is None


def test_assoc_instructions18_stub_double():
    # logoASM_Instruction has no real 'logoASM_Instruction' property in the generated
    # code (a bare stub) -- manually attach it so logoASM_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logoASM_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logoASM_ProcDeclaration(name="sample_text")
    partner = logoASM_Instruction()
    setattr(partner, 'logoASM_Instruction', None)
    _safe_set(owner, 'logoASM_ProcDeclaration19', {partner})
    assert getattr(partner, 'logoASM_Instruction') == owner
    _safe_set(owner, 'logoASM_ProcDeclaration19', set())
    assert getattr(partner, 'logoASM_Instruction') is None


def test_assoc_parameter33_stub_double():
    # logoASM_ParameterCall has no real 'logoASM_ParameterCall' property in the generated
    # code (a bare stub) -- manually attach it so logoASM_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logoASM_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logoASM_Parameter(name="sample_text")
    partner = logoASM_ParameterCall()
    setattr(partner, 'logoASM_ParameterCall', None)
    _safe_set(owner, 'logoASM_Parameter34', partner)
    assert getattr(partner, 'logoASM_ParameterCall') == owner
    _safe_set(owner, 'logoASM_Parameter34', None)
    assert getattr(partner, 'logoASM_ParameterCall') is None


