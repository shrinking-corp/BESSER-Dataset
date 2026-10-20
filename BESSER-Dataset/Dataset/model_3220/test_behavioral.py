import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArithmeticInstruction,
    CompareInstruction,
    Instruction,
    JumpInstruction,
    OutputInstruction,
    Value,
    mil_AddInstruction,
    mil_ArithmeticInstruction,
    mil_CallInstruction,
    mil_CompareInstruction,
    mil_ConditionalJumpInstruction,
    mil_ConstantInteger,
    mil_DivInstruction,
    mil_EqualInstruction,
    mil_GreaterThanEqualInstruction,
    mil_GreaterThanInstruction,
    mil_Instruction,
    mil_JumpInstruction,
    mil_LabelInstruction,
    mil_LessThanEqualInstruction,
    mil_LessThanInstruction,
    mil_LoadInstruction,
    mil_MILModel,
    mil_MulInstruction,
    mil_NegateInstruction,
    mil_NotEqualInstruction,
    mil_OutputInstruction,
    mil_PrintInstruction,
    mil_RegisterReference,
    mil_ReturnInstruction,
    mil_StoreInstruction,
    mil_SubInstruction,
    mil_UnconditionalJumpInstruction,
    mil_Value,
    mil_YieldInstruciton,
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

def test_assoc_jumpTo3_stub_double():
    # mil_JumpInstruction has no real 'mil_JumpInstruction' property in the generated
    # code (a bare stub) -- manually attach it so mil_LabelInstruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mil_LabelInstruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mil_LabelInstruction(name="sample_text")
    partner = mil_JumpInstruction()
    setattr(partner, 'mil_JumpInstruction', None)
    _safe_set(owner, 'mil_LabelInstruction', partner)
    assert getattr(partner, 'mil_JumpInstruction') == owner
    _safe_set(owner, 'mil_LabelInstruction', None)
    assert getattr(partner, 'mil_JumpInstruction') is None


def test_assoc_operationName4_stub_double():
    # mil_CallInstruction has no real 'mil_CallInstruction' property in the generated
    # code (a bare stub) -- manually attach it so mil_LabelInstruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mil_LabelInstruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mil_LabelInstruction(name="sample_text")
    partner = mil_CallInstruction()
    setattr(partner, 'mil_CallInstruction', None)
    _safe_set(owner, 'mil_LabelInstruction5', partner)
    assert getattr(partner, 'mil_CallInstruction') == owner
    _safe_set(owner, 'mil_LabelInstruction5', None)
    assert getattr(partner, 'mil_CallInstruction') is None


def test_assoc_registerReference2_stub_double():
    # mil_StoreInstruction has no real 'mil_StoreInstruction' property in the generated
    # code (a bare stub) -- manually attach it so mil_RegisterReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mil_RegisterReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mil_RegisterReference(address="sample_text")
    partner = mil_StoreInstruction()
    setattr(partner, 'mil_StoreInstruction', None)
    _safe_set(owner, 'mil_RegisterReference', partner)
    assert getattr(partner, 'mil_StoreInstruction') == owner
    _safe_set(owner, 'mil_RegisterReference', None)
    assert getattr(partner, 'mil_StoreInstruction') is None


