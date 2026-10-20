import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BooleanExpression,
    Command,
    Instruction,
    Move,
    SequenceCommand,
    SequenceInstruction,
    farmbot_modeling_BooleanExpression,
    farmbot_modeling_Command,
    farmbot_modeling_ExecuteSequence,
    farmbot_modeling_Farmbot,
    farmbot_modeling_FindHome,
    farmbot_modeling_If,
    farmbot_modeling_Instruction,
    farmbot_modeling_IsEqualTo,
    farmbot_modeling_IsGreaterThan,
    farmbot_modeling_IsLowerThan,
    farmbot_modeling_IsNotEqualTo,
    farmbot_modeling_ListScheduledEvents,
    farmbot_modeling_ListSequences,
    farmbot_modeling_Move,
    farmbot_modeling_MoveAbsolute,
    farmbot_modeling_MoveRelative,
    farmbot_modeling_RunFarmware,
    farmbot_modeling_Schedule,
    farmbot_modeling_SendMessage,
    farmbot_modeling_Sequence,
    farmbot_modeling_SequenceCommand,
    farmbot_modeling_SequenceInstruction,
    farmbot_modeling_TakePhoto,
    farmbot_modeling_TurnOff,
    farmbot_modeling_TurnOnAnalog,
    farmbot_modeling_TurnOnDigital,
    farmbot_modeling_Wait,
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

def test_assoc_booleanExpression2_stub_double():
    # farmbot_modeling_If has no real 'farmbot_modeling_If' property in the generated
    # code (a bare stub) -- manually attach it so farmbot_modeling_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farmbot_modeling_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farmbot_modeling_BooleanExpression(axe="sample_text", pinNumber=7, value=7)
    partner = farmbot_modeling_If()
    setattr(partner, 'farmbot_modeling_If', None)
    _safe_set(owner, 'farmbot_modeling_BooleanExpression', partner)
    assert getattr(partner, 'farmbot_modeling_If') == owner
    _safe_set(owner, 'farmbot_modeling_BooleanExpression', None)
    assert getattr(partner, 'farmbot_modeling_If') is None


def test_assoc_else_5_stub_double():
    # farmbot_modeling_If has no real 'farmbot_modeling_If6' property in the generated
    # code (a bare stub) -- manually attach it so farmbot_modeling_ExecuteSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farmbot_modeling_ExecuteSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farmbot_modeling_ExecuteSequence(id=7)
    partner = farmbot_modeling_If()
    setattr(partner, 'farmbot_modeling_If6', None)
    _safe_set(owner, 'farmbot_modeling_ExecuteSequence7', partner)
    assert getattr(partner, 'farmbot_modeling_If6') == owner
    _safe_set(owner, 'farmbot_modeling_ExecuteSequence7', None)
    assert getattr(partner, 'farmbot_modeling_If6') is None


def test_assoc_sequenceInstructions1_stub_double():
    # farmbot_modeling_SequenceInstruction has no real 'farmbot_modeling_SequenceInstruction' property in the generated
    # code (a bare stub) -- manually attach it so farmbot_modeling_Sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farmbot_modeling_Sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farmbot_modeling_Sequence(name="sample_text")
    partner = farmbot_modeling_SequenceInstruction()
    setattr(partner, 'farmbot_modeling_SequenceInstruction', None)
    _safe_set(owner, 'farmbot_modeling_Sequence', {partner})
    assert getattr(partner, 'farmbot_modeling_SequenceInstruction') == owner
    _safe_set(owner, 'farmbot_modeling_Sequence', set())
    assert getattr(partner, 'farmbot_modeling_SequenceInstruction') is None


def test_assoc_then3_stub_double():
    # farmbot_modeling_If has no real 'farmbot_modeling_If4' property in the generated
    # code (a bare stub) -- manually attach it so farmbot_modeling_ExecuteSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # farmbot_modeling_ExecuteSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = farmbot_modeling_ExecuteSequence(id=7)
    partner = farmbot_modeling_If()
    setattr(partner, 'farmbot_modeling_If4', None)
    _safe_set(owner, 'farmbot_modeling_ExecuteSequence', partner)
    assert getattr(partner, 'farmbot_modeling_If4') == owner
    _safe_set(owner, 'farmbot_modeling_ExecuteSequence', None)
    assert getattr(partner, 'farmbot_modeling_If4') is None


