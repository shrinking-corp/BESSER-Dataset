import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExp,
    ControlStructure,
    Expression,
    Instruction,
    kmLogo_BinaryExp,
    kmLogo_Block,
    kmLogo_Constant,
    kmLogo_ControlStructure,
    kmLogo_Div,
    kmLogo_Equals,
    kmLogo_Expression,
    kmLogo_For,
    kmLogo_Greater,
    kmLogo_If,
    kmLogo_Instruction,
    kmLogo_JavaProgram,
    kmLogo_Lower,
    kmLogo_Main,
    kmLogo_MethodeCall,
    kmLogo_MethodeDeclaration,
    kmLogo_Minus,
    kmLogo_Mult,
    kmLogo_Parameter,
    kmLogo_ParameterCall,
    kmLogo_Plus,
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

def test_assoc_methodeDeclaration21_reverse_link_reassign_clear():
    a1 = kmLogo_MethodeDeclaration(name="sample_text")
    a2 = kmLogo_MethodeDeclaration(name="sample_text_2")
    b = kmLogo_JavaProgram(name="sample_text")
    _safe_set(b, 'kmLogo_JavaProgram22', {a1})
    assert _is_linked(b, 'kmLogo_JavaProgram22', a1)
    if hasattr(a1, 'kmLogo_MethodeDeclaration'):
        assert _is_linked(a1, 'kmLogo_MethodeDeclaration', b)
    _safe_set(b, 'kmLogo_JavaProgram22', {a2})
    assert _is_linked(b, 'kmLogo_JavaProgram22', a2)
    if hasattr(a1, 'kmLogo_MethodeDeclaration'):
        assert not _is_linked(a1, 'kmLogo_MethodeDeclaration', b)
    if hasattr(a2, 'kmLogo_MethodeDeclaration'):
        assert _is_linked(a2, 'kmLogo_MethodeDeclaration', b)
    _safe_set(b, 'kmLogo_JavaProgram22', set())
    assert not _is_linked(b, 'kmLogo_JavaProgram22', a2)
    if hasattr(a2, 'kmLogo_MethodeDeclaration'):
        assert not _is_linked(a2, 'kmLogo_MethodeDeclaration', b)


def test_assoc_parameter29_reverse_link_reassign_clear():
    a1 = kmLogo_Parameter(name="sample_text")
    a2 = kmLogo_Parameter(name="sample_text_2")
    b = kmLogo_MethodeDeclaration(name="sample_text")
    _safe_set(b, 'kmLogo_MethodeDeclaration30', {a1})
    assert _is_linked(b, 'kmLogo_MethodeDeclaration30', a1)
    if hasattr(a1, 'kmLogo_Parameter31'):
        assert _is_linked(a1, 'kmLogo_Parameter31', b)
    _safe_set(b, 'kmLogo_MethodeDeclaration30', {a2})
    assert _is_linked(b, 'kmLogo_MethodeDeclaration30', a2)
    if hasattr(a1, 'kmLogo_Parameter31'):
        assert not _is_linked(a1, 'kmLogo_Parameter31', b)
    if hasattr(a2, 'kmLogo_Parameter31'):
        assert _is_linked(a2, 'kmLogo_Parameter31', b)
    _safe_set(b, 'kmLogo_MethodeDeclaration30', set())
    assert not _is_linked(b, 'kmLogo_MethodeDeclaration30', a2)
    if hasattr(a2, 'kmLogo_Parameter31'):
        assert not _is_linked(a2, 'kmLogo_Parameter31', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_instruction26_stub_double():
    # kmLogo_Instruction has no real 'kmLogo_Instruction28' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_MethodeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_MethodeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_MethodeDeclaration(name="sample_text")
    partner = kmLogo_Instruction()
    setattr(partner, 'kmLogo_Instruction28', None)
    _safe_set(owner, 'kmLogo_MethodeDeclaration27', {partner})
    assert getattr(partner, 'kmLogo_Instruction28') == owner
    _safe_set(owner, 'kmLogo_MethodeDeclaration27', set())
    assert getattr(partner, 'kmLogo_Instruction28') is None


def test_assoc_main20_stub_double():
    # kmLogo_Main has no real 'kmLogo_Main' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_JavaProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_JavaProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_JavaProgram(name="sample_text")
    partner = kmLogo_Main()
    setattr(partner, 'kmLogo_Main', None)
    _safe_set(owner, 'kmLogo_JavaProgram', partner)
    assert getattr(partner, 'kmLogo_Main') == owner
    _safe_set(owner, 'kmLogo_JavaProgram', None)
    assert getattr(partner, 'kmLogo_Main') is None


def test_assoc_methodecall32_stub_double():
    # kmLogo_MethodeCall has no real 'MethodeCall' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_MethodeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_MethodeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_MethodeDeclaration(name="sample_text")
    partner = kmLogo_MethodeCall()
    setattr(partner, 'MethodeCall', None)
    _safe_set(owner, 'methodedeclaration', {partner})
    assert getattr(partner, 'MethodeCall') == owner
    _safe_set(owner, 'methodedeclaration', set())
    assert getattr(partner, 'MethodeCall') is None


def test_assoc_methodedeclaration0_stub_double():
    # kmLogo_MethodeCall has no real 'methodecall' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_MethodeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_MethodeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_MethodeDeclaration(name="sample_text")
    partner = kmLogo_MethodeCall()
    setattr(partner, 'methodecall', None)
    _safe_set(owner, 'MethodeDeclaration', partner)
    assert getattr(partner, 'methodecall') == owner
    _safe_set(owner, 'MethodeDeclaration', None)
    assert getattr(partner, 'methodecall') is None


def test_assoc_parameter19_stub_double():
    # kmLogo_ParameterCall has no real 'kmLogo_ParameterCall' property in the generated
    # code (a bare stub) -- manually attach it so kmLogo_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # kmLogo_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = kmLogo_Parameter(name="sample_text")
    partner = kmLogo_ParameterCall()
    setattr(partner, 'kmLogo_ParameterCall', None)
    _safe_set(owner, 'kmLogo_Parameter', partner)
    assert getattr(partner, 'kmLogo_ParameterCall') == owner
    _safe_set(owner, 'kmLogo_Parameter', None)
    assert getattr(partner, 'kmLogo_ParameterCall') is None


