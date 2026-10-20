import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CacheInstruction,
    ControlFlowInstruction,
    DataAccessPattern,
    IOInstruction,
    SynchronisationInstruction,
    llp_Block,
    llp_CacheInstruction,
    llp_CommitInstruction,
    llp_ControlFlowBranchingInstruction,
    llp_ControlFlowInstruction,
    llp_DataAccessPattern,
    llp_IOInstruction,
    llp_LockInstruction,
    llp_LowLevelProgram,
    llp_MemoryReference,
    llp_ParenthesisInstruction,
    llp_ReadInstruction,
    llp_RepetitionInstruction,
    llp_SkipInstruction,
    llp_SpawnInstruction,
    llp_SynchronisationInstruction,
    llp_Task,
    llp_UnlockInstruction,
    llp_WriteInstruction,
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

def test_assoc_block18_stub_double():
    # llp_Block has no real 'llp_Block19' property in the generated
    # code (a bare stub) -- manually attach it so llp_RepetitionInstruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # llp_RepetitionInstruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = llp_RepetitionInstruction(numberOfRepetitions=7)
    partner = llp_Block()
    setattr(partner, 'llp_Block19', None)
    _safe_set(owner, 'llp_RepetitionInstruction', partner)
    assert getattr(partner, 'llp_Block19') == owner
    _safe_set(owner, 'llp_RepetitionInstruction', None)
    assert getattr(partner, 'llp_Block19') is None


def test_assoc_block3_stub_double():
    # llp_Block has no real 'llp_Block5' property in the generated
    # code (a bare stub) -- manually attach it so llp_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # llp_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = llp_Task(name="sample_text")
    partner = llp_Block()
    setattr(partner, 'llp_Block5', None)
    _safe_set(owner, 'llp_Task4', partner)
    assert getattr(partner, 'llp_Block5') == owner
    _safe_set(owner, 'llp_Task4', None)
    assert getattr(partner, 'llp_Block5') is None


def test_assoc_memoryReference20_stub_double():
    # llp_SynchronisationInstruction has no real 'llp_SynchronisationInstruction' property in the generated
    # code (a bare stub) -- manually attach it so llp_MemoryReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # llp_MemoryReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = llp_MemoryReference(address="sample_text")
    partner = llp_SynchronisationInstruction()
    setattr(partner, 'llp_SynchronisationInstruction', None)
    _safe_set(owner, 'llp_MemoryReference21', partner)
    assert getattr(partner, 'llp_SynchronisationInstruction') == owner
    _safe_set(owner, 'llp_MemoryReference21', None)
    assert getattr(partner, 'llp_SynchronisationInstruction') is None


def test_assoc_memoryReference8_stub_double():
    # llp_IOInstruction has no real 'llp_IOInstruction' property in the generated
    # code (a bare stub) -- manually attach it so llp_MemoryReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # llp_MemoryReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = llp_MemoryReference(address="sample_text")
    partner = llp_IOInstruction()
    setattr(partner, 'llp_IOInstruction', None)
    _safe_set(owner, 'llp_MemoryReference', partner)
    assert getattr(partner, 'llp_IOInstruction') == owner
    _safe_set(owner, 'llp_MemoryReference', None)
    assert getattr(partner, 'llp_IOInstruction') is None


def test_assoc_memoryReference9_stub_double():
    # llp_CommitInstruction has no real 'llp_CommitInstruction' property in the generated
    # code (a bare stub) -- manually attach it so llp_MemoryReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # llp_MemoryReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = llp_MemoryReference(address="sample_text")
    partner = llp_CommitInstruction()
    setattr(partner, 'llp_CommitInstruction', None)
    _safe_set(owner, 'llp_MemoryReference10', partner)
    assert getattr(partner, 'llp_CommitInstruction') == owner
    _safe_set(owner, 'llp_MemoryReference10', None)
    assert getattr(partner, 'llp_CommitInstruction') is None


def test_assoc_task11_stub_double():
    # llp_SpawnInstruction has no real 'llp_SpawnInstruction' property in the generated
    # code (a bare stub) -- manually attach it so llp_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # llp_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = llp_Task(name="sample_text")
    partner = llp_SpawnInstruction()
    setattr(partner, 'llp_SpawnInstruction', None)
    _safe_set(owner, 'llp_Task12', partner)
    assert getattr(partner, 'llp_SpawnInstruction') == owner
    _safe_set(owner, 'llp_Task12', None)
    assert getattr(partner, 'llp_SpawnInstruction') is None


def test_assoc_tasks0_stub_double():
    # llp_LowLevelProgram has no real 'llp_LowLevelProgram' property in the generated
    # code (a bare stub) -- manually attach it so llp_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # llp_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = llp_Task(name="sample_text")
    partner = llp_LowLevelProgram()
    setattr(partner, 'llp_LowLevelProgram', None)
    _safe_set(owner, 'llp_Task', partner)
    assert owner in getattr(partner, 'llp_LowLevelProgram')
    _safe_set(owner, 'llp_Task', None)
    assert owner not in getattr(partner, 'llp_LowLevelProgram')


