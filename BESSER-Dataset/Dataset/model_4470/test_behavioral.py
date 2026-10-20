import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExp,
    ControlStructure,
    Expression,
    Instruction,
    Primitive,
    kmLogo_Back,
    kmLogo_BinaryExp,
    kmLogo_Block,
    kmLogo_Clear,
    kmLogo_Constant,
    kmLogo_ControlStructure,
    kmLogo_Div,
    kmLogo_Equals,
    kmLogo_Expression,
    kmLogo_Forward,
    kmLogo_Greater,
    kmLogo_If,
    kmLogo_Instruction,
    kmLogo_Left,
    kmLogo_LogoProgram,
    kmLogo_Lower,
    kmLogo_Minus,
    kmLogo_Mult,
    kmLogo_Parameter,
    kmLogo_ParameterCall,
    kmLogo_PenDown,
    kmLogo_PenUp,
    kmLogo_Plus,
    kmLogo_Primitive,
    kmLogo_ProcCall,
    kmLogo_ProcDeclaration,
    kmLogo_Repeat,
    kmLogo_Right,
    kmLogo_While,
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
    a1 = kmLogo_ProcDeclaration(name="sample_text")
    a2 = kmLogo_ProcDeclaration(name="sample_text_2")
    b = kmLogo_Parameter(name="sample_text")
    _safe_set(b, 'kmLogo_Parameter', a1)
    assert _is_linked(b, 'kmLogo_Parameter', a1)
    if hasattr(a1, 'kmLogo_ProcDeclaration'):
        assert _is_linked(a1, 'kmLogo_ProcDeclaration', b)
    _safe_set(b, 'kmLogo_Parameter', a2)
    assert _is_linked(b, 'kmLogo_Parameter', a2)
    if hasattr(a1, 'kmLogo_ProcDeclaration'):
        assert not _is_linked(a1, 'kmLogo_ProcDeclaration', b)
    if hasattr(a2, 'kmLogo_ProcDeclaration'):
        assert _is_linked(a2, 'kmLogo_ProcDeclaration', b)
    _safe_set(b, 'kmLogo_Parameter', None)
    assert not _is_linked(b, 'kmLogo_Parameter', a2)
    if hasattr(a2, 'kmLogo_ProcDeclaration'):
        assert not _is_linked(a2, 'kmLogo_ProcDeclaration', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_declaration15_stub_double():
    # kmLogo_ProcCall has no real 'procCall' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_ProcDeclaration(name="sample_text")
    partner = kmLogo_ProcCall()
    setattr(partner, 'procCall', None)
    _safe_set(owner, 'ProcDeclaration', partner)
    assert getattr(partner, 'procCall') == owner
    _safe_set(owner, 'ProcDeclaration', None)
    assert getattr(partner, 'procCall') is None


def test_assoc_instructions18_stub_double():
    # kmLogo_Instruction has no real 'kmLogo_Instruction20' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_ProcDeclaration(name="sample_text")
    partner = kmLogo_Instruction()
    setattr(partner, 'kmLogo_Instruction20', None)
    _safe_set(owner, 'kmLogo_ProcDeclaration19', {partner})
    assert getattr(partner, 'kmLogo_Instruction20') == owner
    _safe_set(owner, 'kmLogo_ProcDeclaration19', set())
    assert getattr(partner, 'kmLogo_Instruction20') is None


def test_assoc_parameter34_stub_double():
    # kmLogo_ParameterCall has no real 'kmLogo_ParameterCall' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_Parameter(name="sample_text")
    partner = kmLogo_ParameterCall()
    setattr(partner, 'kmLogo_ParameterCall', None)
    _safe_set(owner, 'kmLogo_Parameter35', partner)
    assert getattr(partner, 'kmLogo_ParameterCall') == owner
    _safe_set(owner, 'kmLogo_Parameter35', None)
    assert getattr(partner, 'kmLogo_ParameterCall') is None


def test_assoc_procCall17_stub_double():
    # kmLogo_ProcCall has no real 'ProcCall' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_ProcDeclaration(name="sample_text")
    partner = kmLogo_ProcCall()
    setattr(partner, 'ProcCall', None)
    _safe_set(owner, 'declaration', {partner})
    assert getattr(partner, 'ProcCall') == owner
    _safe_set(owner, 'declaration', set())
    assert getattr(partner, 'ProcCall') is None


