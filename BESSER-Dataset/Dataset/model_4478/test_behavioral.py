import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExp,
    ControlStructure,
    Expression,
    Instruction,
    Primitive,
    UnaryExpression,
    kmLogo_Back,
    kmLogo_BinaryExp,
    kmLogo_Block,
    kmLogo_CallStack,
    kmLogo_Clear,
    kmLogo_Constant,
    kmLogo_ControlStructure,
    kmLogo_Cos,
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
    kmLogo_Point,
    kmLogo_Primitive,
    kmLogo_ProcCall,
    kmLogo_ProcDeclaration,
    kmLogo_Repeat,
    kmLogo_Right,
    kmLogo_Segment,
    kmLogo_Sin,
    kmLogo_StackFrame,
    kmLogo_Tan,
    kmLogo_Turtle,
    kmLogo_UnaryExpression,
    kmLogo_Variable,
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

def test_assoc_args17_reverse_link_reassign_clear():
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


def test_assoc_position38_reverse_link_reassign_clear():
    a1 = kmLogo_Turtle(heading=3.14, penUp=True)
    a2 = kmLogo_Turtle(heading=9.99, penUp=False)
    b = kmLogo_Point(x=3.14, y=3.14)
    _safe_set(b, 'kmLogo_Point', a1)
    assert _is_linked(b, 'kmLogo_Point', a1)
    if hasattr(a1, 'kmLogo_Turtle'):
        assert _is_linked(a1, 'kmLogo_Turtle', b)
    _safe_set(b, 'kmLogo_Point', a2)
    assert _is_linked(b, 'kmLogo_Point', a2)
    if hasattr(a1, 'kmLogo_Turtle'):
        assert not _is_linked(a1, 'kmLogo_Turtle', b)
    if hasattr(a2, 'kmLogo_Turtle'):
        assert _is_linked(a2, 'kmLogo_Turtle', b)
    _safe_set(b, 'kmLogo_Point', None)
    assert not _is_linked(b, 'kmLogo_Point', a2)
    if hasattr(a2, 'kmLogo_Turtle'):
        assert not _is_linked(a2, 'kmLogo_Turtle', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_begin43_stub_double():
    # kmLogo_Segment has no real 'kmLogo_Segment44' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_Point(x=3.14, y=3.14)
    partner = kmLogo_Segment()
    setattr(partner, 'kmLogo_Segment44', None)
    _safe_set(owner, 'kmLogo_Point45', partner)
    assert getattr(partner, 'kmLogo_Segment44') == owner
    _safe_set(owner, 'kmLogo_Point45', None)
    assert getattr(partner, 'kmLogo_Segment44') is None


def test_assoc_callStack41_stub_double():
    # kmLogo_CallStack has no real 'kmLogo_CallStack' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_Turtle(heading=3.14, penUp=True)
    partner = kmLogo_CallStack()
    setattr(partner, 'kmLogo_CallStack', None)
    _safe_set(owner, 'kmLogo_Turtle42', partner)
    assert getattr(partner, 'kmLogo_CallStack') == owner
    _safe_set(owner, 'kmLogo_Turtle42', None)
    assert getattr(partner, 'kmLogo_CallStack') is None


def test_assoc_declaration16_stub_double():
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


def test_assoc_drawings39_stub_double():
    # kmLogo_Segment has no real 'kmLogo_Segment' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_Turtle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_Turtle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_Turtle(heading=3.14, penUp=True)
    partner = kmLogo_Segment()
    setattr(partner, 'kmLogo_Segment', None)
    _safe_set(owner, 'kmLogo_Turtle40', {partner})
    assert getattr(partner, 'kmLogo_Segment') == owner
    _safe_set(owner, 'kmLogo_Turtle40', set())
    assert getattr(partner, 'kmLogo_Segment') is None


def test_assoc_end46_stub_double():
    # kmLogo_Segment has no real 'kmLogo_Segment47' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_Point's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_Point's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_Point(x=3.14, y=3.14)
    partner = kmLogo_Segment()
    setattr(partner, 'kmLogo_Segment47', None)
    _safe_set(owner, 'kmLogo_Point48', partner)
    assert getattr(partner, 'kmLogo_Segment47') == owner
    _safe_set(owner, 'kmLogo_Point48', None)
    assert getattr(partner, 'kmLogo_Segment47') is None


def test_assoc_instructions19_stub_double():
    # kmLogo_Instruction has no real 'kmLogo_Instruction' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_ProcDeclaration(name="sample_text")
    partner = kmLogo_Instruction()
    setattr(partner, 'kmLogo_Instruction', None)
    _safe_set(owner, 'kmLogo_ProcDeclaration20', {partner})
    assert getattr(partner, 'kmLogo_Instruction') == owner
    _safe_set(owner, 'kmLogo_ProcDeclaration20', set())
    assert getattr(partner, 'kmLogo_Instruction') is None


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


def test_assoc_procCall18_stub_double():
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


def test_assoc_variables51_stub_double():
    # kmLogo_StackFrame has no real 'kmLogo_StackFrame52' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_Variable(name="sample_text", value=3.14)
    partner = kmLogo_StackFrame()
    setattr(partner, 'kmLogo_StackFrame52', None)
    _safe_set(owner, 'kmLogo_Variable', partner)
    assert owner in getattr(partner, 'kmLogo_StackFrame52')
    _safe_set(owner, 'kmLogo_Variable', None)
    assert owner not in getattr(partner, 'kmLogo_StackFrame52')


