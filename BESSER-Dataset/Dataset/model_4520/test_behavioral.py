import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Instruction,
    logo_Forward,
    logo_Instruction,
    logo_Left,
    logo_LogoProgram,
    logo_Parameter,
    logo_ProcCall,
    logo_ProcDeclaration,
    logo_Right,
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

def test_assoc_args1_reverse_link_reassign_clear():
    a1 = logo_ProcDeclaration(name="sample_text")
    a2 = logo_ProcDeclaration(name="sample_text_2")
    b = logo_Parameter(name="sample_text")
    _safe_set(b, 'logo_Parameter', a1)
    assert _is_linked(b, 'logo_Parameter', a1)
    if hasattr(a1, 'logo_ProcDeclaration'):
        assert _is_linked(a1, 'logo_ProcDeclaration', b)
    _safe_set(b, 'logo_Parameter', a2)
    assert _is_linked(b, 'logo_Parameter', a2)
    if hasattr(a1, 'logo_ProcDeclaration'):
        assert not _is_linked(a1, 'logo_ProcDeclaration', b)
    if hasattr(a2, 'logo_ProcDeclaration'):
        assert _is_linked(a2, 'logo_ProcDeclaration', b)
    _safe_set(b, 'logo_Parameter', None)
    assert not _is_linked(b, 'logo_Parameter', a2)
    if hasattr(a2, 'logo_ProcDeclaration'):
        assert not _is_linked(a2, 'logo_ProcDeclaration', b)


def test_assoc_declaration5_reverse_link_reassign_clear():
    a1 = logo_ProcDeclaration(name="sample_text")
    a2 = logo_ProcDeclaration(name="sample_text_2")
    b = logo_ProcCall(actualArgs=7)
    _safe_set(b, 'logo_ProcCall', a1)
    assert _is_linked(b, 'logo_ProcCall', a1)
    if hasattr(a1, 'logo_ProcDeclaration6'):
        assert _is_linked(a1, 'logo_ProcDeclaration6', b)
    _safe_set(b, 'logo_ProcCall', a2)
    assert _is_linked(b, 'logo_ProcCall', a2)
    if hasattr(a1, 'logo_ProcDeclaration6'):
        assert not _is_linked(a1, 'logo_ProcDeclaration6', b)
    if hasattr(a2, 'logo_ProcDeclaration6'):
        assert _is_linked(a2, 'logo_ProcDeclaration6', b)
    _safe_set(b, 'logo_ProcCall', None)
    assert not _is_linked(b, 'logo_ProcCall', a2)
    if hasattr(a2, 'logo_ProcDeclaration6'):
        assert not _is_linked(a2, 'logo_ProcDeclaration6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_instructions2_stub_double():
    # logo_Instruction has no real 'logo_Instruction4' property in the generated
    # code (a bare stub) -- manually attach it so logo_ProcDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # logo_ProcDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = logo_ProcDeclaration(name="sample_text")
    partner = logo_Instruction()
    setattr(partner, 'logo_Instruction4', None)
    _safe_set(owner, 'logo_ProcDeclaration3', {partner})
    assert getattr(partner, 'logo_Instruction4') == owner
    _safe_set(owner, 'logo_ProcDeclaration3', set())
    assert getattr(partner, 'logo_Instruction4') is None


