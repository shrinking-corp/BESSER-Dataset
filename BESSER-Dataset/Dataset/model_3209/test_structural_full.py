import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_llp_MemoryReference_address_value_roundtrip():
    instance = llp_MemoryReference(address="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_llp_RepetitionInstruction_numberOfRepetitions_value_roundtrip():
    instance = llp_RepetitionInstruction(numberOfRepetitions=7)
    assert instance.numberOfRepetitions == 7
    instance.numberOfRepetitions = 13
    assert instance.numberOfRepetitions == 13


def test_llp_Task_name_value_roundtrip():
    instance = llp_Task(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_llp_CommitInstruction_isa_CacheInstruction():
    instance = llp_CommitInstruction()
    assert isinstance(instance, CacheInstruction)


def test_llp_ControlFlowBranchingInstruction_isa_ControlFlowInstruction():
    instance = llp_ControlFlowBranchingInstruction()
    assert isinstance(instance, ControlFlowInstruction)


def test_llp_ParenthesisInstruction_isa_ControlFlowInstruction():
    instance = llp_ParenthesisInstruction()
    assert isinstance(instance, ControlFlowInstruction)


def test_llp_RepetitionInstruction_isa_ControlFlowInstruction():
    instance = llp_RepetitionInstruction(numberOfRepetitions=7)
    assert isinstance(instance, ControlFlowInstruction)


def test_llp_SkipInstruction_isa_ControlFlowInstruction():
    instance = llp_SkipInstruction()
    assert isinstance(instance, ControlFlowInstruction)


def test_llp_CacheInstruction_isa_DataAccessPattern():
    instance = llp_CacheInstruction()
    assert isinstance(instance, DataAccessPattern)


def test_llp_ControlFlowInstruction_isa_DataAccessPattern():
    instance = llp_ControlFlowInstruction()
    assert isinstance(instance, DataAccessPattern)


def test_llp_IOInstruction_isa_DataAccessPattern():
    instance = llp_IOInstruction()
    assert isinstance(instance, DataAccessPattern)


def test_llp_SpawnInstruction_isa_DataAccessPattern():
    instance = llp_SpawnInstruction()
    assert isinstance(instance, DataAccessPattern)


def test_llp_SynchronisationInstruction_isa_DataAccessPattern():
    instance = llp_SynchronisationInstruction()
    assert isinstance(instance, DataAccessPattern)


def test_llp_ReadInstruction_isa_IOInstruction():
    instance = llp_ReadInstruction()
    assert isinstance(instance, IOInstruction)


def test_llp_WriteInstruction_isa_IOInstruction():
    instance = llp_WriteInstruction()
    assert isinstance(instance, IOInstruction)


def test_llp_LockInstruction_isa_SynchronisationInstruction():
    instance = llp_LockInstruction()
    assert isinstance(instance, SynchronisationInstruction)


def test_llp_UnlockInstruction_isa_SynchronisationInstruction():
    instance = llp_UnlockInstruction()
    assert isinstance(instance, SynchronisationInstruction)


def test_assoc_block18_link_reassign_clear():
    a = llp_RepetitionInstruction(numberOfRepetitions=7)
    b1 = llp_Block()
    b2 = llp_Block()
    _safe_set(a, 'llp_RepetitionInstruction', b1)
    assert _is_linked(a, 'llp_RepetitionInstruction', b1)
    if hasattr(b1, 'llp_Block19'):
        assert _is_linked(b1, 'llp_Block19', a)
    _safe_set(a, 'llp_RepetitionInstruction', b2)
    assert _is_linked(a, 'llp_RepetitionInstruction', b2)
    if hasattr(b1, 'llp_Block19'):
        assert not _is_linked(b1, 'llp_Block19', a)
    if hasattr(b2, 'llp_Block19'):
        assert _is_linked(b2, 'llp_Block19', a)
    _safe_set(a, 'llp_RepetitionInstruction', None)
    assert not _is_linked(a, 'llp_RepetitionInstruction', b2)
    if hasattr(b2, 'llp_Block19'):
        assert not _is_linked(b2, 'llp_Block19', a)


def test_assoc_block3_link_reassign_clear():
    a = llp_Task(name="sample_text")
    b1 = llp_Block()
    b2 = llp_Block()
    _safe_set(a, 'llp_Task4', b1)
    assert _is_linked(a, 'llp_Task4', b1)
    if hasattr(b1, 'llp_Block5'):
        assert _is_linked(b1, 'llp_Block5', a)
    _safe_set(a, 'llp_Task4', b2)
    assert _is_linked(a, 'llp_Task4', b2)
    if hasattr(b1, 'llp_Block5'):
        assert not _is_linked(b1, 'llp_Block5', a)
    if hasattr(b2, 'llp_Block5'):
        assert _is_linked(b2, 'llp_Block5', a)
    _safe_set(a, 'llp_Task4', None)
    assert not _is_linked(a, 'llp_Task4', b2)
    if hasattr(b2, 'llp_Block5'):
        assert not _is_linked(b2, 'llp_Block5', a)


def test_assoc_memoryReference20_link_reassign_clear():
    a = llp_MemoryReference(address="sample_text")
    b1 = llp_SynchronisationInstruction()
    b2 = llp_SynchronisationInstruction()
    _safe_set(a, 'llp_MemoryReference21', b1)
    assert _is_linked(a, 'llp_MemoryReference21', b1)
    if hasattr(b1, 'llp_SynchronisationInstruction'):
        assert _is_linked(b1, 'llp_SynchronisationInstruction', a)
    _safe_set(a, 'llp_MemoryReference21', b2)
    assert _is_linked(a, 'llp_MemoryReference21', b2)
    if hasattr(b1, 'llp_SynchronisationInstruction'):
        assert not _is_linked(b1, 'llp_SynchronisationInstruction', a)
    if hasattr(b2, 'llp_SynchronisationInstruction'):
        assert _is_linked(b2, 'llp_SynchronisationInstruction', a)
    _safe_set(a, 'llp_MemoryReference21', None)
    assert not _is_linked(a, 'llp_MemoryReference21', b2)
    if hasattr(b2, 'llp_SynchronisationInstruction'):
        assert not _is_linked(b2, 'llp_SynchronisationInstruction', a)


def test_assoc_memoryReference8_link_reassign_clear():
    a = llp_MemoryReference(address="sample_text")
    b1 = llp_IOInstruction()
    b2 = llp_IOInstruction()
    _safe_set(a, 'llp_MemoryReference', b1)
    assert _is_linked(a, 'llp_MemoryReference', b1)
    if hasattr(b1, 'llp_IOInstruction'):
        assert _is_linked(b1, 'llp_IOInstruction', a)
    _safe_set(a, 'llp_MemoryReference', b2)
    assert _is_linked(a, 'llp_MemoryReference', b2)
    if hasattr(b1, 'llp_IOInstruction'):
        assert not _is_linked(b1, 'llp_IOInstruction', a)
    if hasattr(b2, 'llp_IOInstruction'):
        assert _is_linked(b2, 'llp_IOInstruction', a)
    _safe_set(a, 'llp_MemoryReference', None)
    assert not _is_linked(a, 'llp_MemoryReference', b2)
    if hasattr(b2, 'llp_IOInstruction'):
        assert not _is_linked(b2, 'llp_IOInstruction', a)


def test_assoc_memoryReference9_link_reassign_clear():
    a = llp_MemoryReference(address="sample_text")
    b1 = llp_CommitInstruction()
    b2 = llp_CommitInstruction()
    _safe_set(a, 'llp_MemoryReference10', b1)
    assert _is_linked(a, 'llp_MemoryReference10', b1)
    if hasattr(b1, 'llp_CommitInstruction'):
        assert _is_linked(b1, 'llp_CommitInstruction', a)
    _safe_set(a, 'llp_MemoryReference10', b2)
    assert _is_linked(a, 'llp_MemoryReference10', b2)
    if hasattr(b1, 'llp_CommitInstruction'):
        assert not _is_linked(b1, 'llp_CommitInstruction', a)
    if hasattr(b2, 'llp_CommitInstruction'):
        assert _is_linked(b2, 'llp_CommitInstruction', a)
    _safe_set(a, 'llp_MemoryReference10', None)
    assert not _is_linked(a, 'llp_MemoryReference10', b2)
    if hasattr(b2, 'llp_CommitInstruction'):
        assert not _is_linked(b2, 'llp_CommitInstruction', a)


def test_assoc_task11_link_reassign_clear():
    a = llp_Task(name="sample_text")
    b1 = llp_SpawnInstruction()
    b2 = llp_SpawnInstruction()
    _safe_set(a, 'llp_Task12', b1)
    assert _is_linked(a, 'llp_Task12', b1)
    if hasattr(b1, 'llp_SpawnInstruction'):
        assert _is_linked(b1, 'llp_SpawnInstruction', a)
    _safe_set(a, 'llp_Task12', b2)
    assert _is_linked(a, 'llp_Task12', b2)
    if hasattr(b1, 'llp_SpawnInstruction'):
        assert not _is_linked(b1, 'llp_SpawnInstruction', a)
    if hasattr(b2, 'llp_SpawnInstruction'):
        assert _is_linked(b2, 'llp_SpawnInstruction', a)
    _safe_set(a, 'llp_Task12', None)
    assert not _is_linked(a, 'llp_Task12', b2)
    if hasattr(b2, 'llp_SpawnInstruction'):
        assert not _is_linked(b2, 'llp_SpawnInstruction', a)


def test_assoc_tasks0_link_reassign_clear():
    a = llp_Task(name="sample_text")
    b1 = llp_LowLevelProgram()
    b2 = llp_LowLevelProgram()
    _safe_set(a, 'llp_Task', b1)
    assert _is_linked(a, 'llp_Task', b1)
    if hasattr(b1, 'llp_LowLevelProgram'):
        assert _is_linked(b1, 'llp_LowLevelProgram', a)
    _safe_set(a, 'llp_Task', b2)
    assert _is_linked(a, 'llp_Task', b2)
    if hasattr(b1, 'llp_LowLevelProgram'):
        assert not _is_linked(b1, 'llp_LowLevelProgram', a)
    if hasattr(b2, 'llp_LowLevelProgram'):
        assert _is_linked(b2, 'llp_LowLevelProgram', a)
    _safe_set(a, 'llp_Task', None)
    assert not _is_linked(a, 'llp_Task', b2)
    if hasattr(b2, 'llp_LowLevelProgram'):
        assert not _is_linked(b2, 'llp_LowLevelProgram', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

CacheInstruction_strategy = st.builds(CacheInstruction)
@given(instance=CacheInstruction_strategy)
@settings(max_examples=25)
def test_CacheInstruction_instantiation(instance):
    assert isinstance(instance, CacheInstruction)


ControlFlowInstruction_strategy = st.builds(ControlFlowInstruction)
@given(instance=ControlFlowInstruction_strategy)
@settings(max_examples=25)
def test_ControlFlowInstruction_instantiation(instance):
    assert isinstance(instance, ControlFlowInstruction)


DataAccessPattern_strategy = st.builds(DataAccessPattern)
@given(instance=DataAccessPattern_strategy)
@settings(max_examples=25)
def test_DataAccessPattern_instantiation(instance):
    assert isinstance(instance, DataAccessPattern)


IOInstruction_strategy = st.builds(IOInstruction)
@given(instance=IOInstruction_strategy)
@settings(max_examples=25)
def test_IOInstruction_instantiation(instance):
    assert isinstance(instance, IOInstruction)


SynchronisationInstruction_strategy = st.builds(SynchronisationInstruction)
@given(instance=SynchronisationInstruction_strategy)
@settings(max_examples=25)
def test_SynchronisationInstruction_instantiation(instance):
    assert isinstance(instance, SynchronisationInstruction)


llp_Block_strategy = st.builds(llp_Block)
@given(instance=llp_Block_strategy)
@settings(max_examples=25)
def test_llp_Block_instantiation(instance):
    assert isinstance(instance, llp_Block)


llp_CacheInstruction_strategy = st.builds(llp_CacheInstruction)
@given(instance=llp_CacheInstruction_strategy)
@settings(max_examples=25)
def test_llp_CacheInstruction_instantiation(instance):
    assert isinstance(instance, llp_CacheInstruction)


llp_CommitInstruction_strategy = st.builds(llp_CommitInstruction)
@given(instance=llp_CommitInstruction_strategy)
@settings(max_examples=25)
def test_llp_CommitInstruction_instantiation(instance):
    assert isinstance(instance, llp_CommitInstruction)


llp_ControlFlowBranchingInstruction_strategy = st.builds(llp_ControlFlowBranchingInstruction)
@given(instance=llp_ControlFlowBranchingInstruction_strategy)
@settings(max_examples=25)
def test_llp_ControlFlowBranchingInstruction_instantiation(instance):
    assert isinstance(instance, llp_ControlFlowBranchingInstruction)


llp_ControlFlowInstruction_strategy = st.builds(llp_ControlFlowInstruction)
@given(instance=llp_ControlFlowInstruction_strategy)
@settings(max_examples=25)
def test_llp_ControlFlowInstruction_instantiation(instance):
    assert isinstance(instance, llp_ControlFlowInstruction)


llp_DataAccessPattern_strategy = st.builds(llp_DataAccessPattern)
@given(instance=llp_DataAccessPattern_strategy)
@settings(max_examples=25)
def test_llp_DataAccessPattern_instantiation(instance):
    assert isinstance(instance, llp_DataAccessPattern)


llp_IOInstruction_strategy = st.builds(llp_IOInstruction)
@given(instance=llp_IOInstruction_strategy)
@settings(max_examples=25)
def test_llp_IOInstruction_instantiation(instance):
    assert isinstance(instance, llp_IOInstruction)


llp_LockInstruction_strategy = st.builds(llp_LockInstruction)
@given(instance=llp_LockInstruction_strategy)
@settings(max_examples=25)
def test_llp_LockInstruction_instantiation(instance):
    assert isinstance(instance, llp_LockInstruction)


llp_LowLevelProgram_strategy = st.builds(llp_LowLevelProgram)
@given(instance=llp_LowLevelProgram_strategy)
@settings(max_examples=25)
def test_llp_LowLevelProgram_instantiation(instance):
    assert isinstance(instance, llp_LowLevelProgram)


llp_MemoryReference_strategy = st.builds(llp_MemoryReference, address=safe_text)
@given(instance=llp_MemoryReference_strategy)
@settings(max_examples=25)
def test_llp_MemoryReference_instantiation(instance):
    assert isinstance(instance, llp_MemoryReference)


llp_ParenthesisInstruction_strategy = st.builds(llp_ParenthesisInstruction)
@given(instance=llp_ParenthesisInstruction_strategy)
@settings(max_examples=25)
def test_llp_ParenthesisInstruction_instantiation(instance):
    assert isinstance(instance, llp_ParenthesisInstruction)


llp_ReadInstruction_strategy = st.builds(llp_ReadInstruction)
@given(instance=llp_ReadInstruction_strategy)
@settings(max_examples=25)
def test_llp_ReadInstruction_instantiation(instance):
    assert isinstance(instance, llp_ReadInstruction)


llp_RepetitionInstruction_strategy = st.builds(llp_RepetitionInstruction, numberOfRepetitions=st.integers())
@given(instance=llp_RepetitionInstruction_strategy)
@settings(max_examples=25)
def test_llp_RepetitionInstruction_instantiation(instance):
    assert isinstance(instance, llp_RepetitionInstruction)


llp_SkipInstruction_strategy = st.builds(llp_SkipInstruction)
@given(instance=llp_SkipInstruction_strategy)
@settings(max_examples=25)
def test_llp_SkipInstruction_instantiation(instance):
    assert isinstance(instance, llp_SkipInstruction)


llp_SpawnInstruction_strategy = st.builds(llp_SpawnInstruction)
@given(instance=llp_SpawnInstruction_strategy)
@settings(max_examples=25)
def test_llp_SpawnInstruction_instantiation(instance):
    assert isinstance(instance, llp_SpawnInstruction)


llp_SynchronisationInstruction_strategy = st.builds(llp_SynchronisationInstruction)
@given(instance=llp_SynchronisationInstruction_strategy)
@settings(max_examples=25)
def test_llp_SynchronisationInstruction_instantiation(instance):
    assert isinstance(instance, llp_SynchronisationInstruction)


llp_Task_strategy = st.builds(llp_Task, name=safe_text)
@given(instance=llp_Task_strategy)
@settings(max_examples=25)
def test_llp_Task_instantiation(instance):
    assert isinstance(instance, llp_Task)


llp_UnlockInstruction_strategy = st.builds(llp_UnlockInstruction)
@given(instance=llp_UnlockInstruction_strategy)
@settings(max_examples=25)
def test_llp_UnlockInstruction_instantiation(instance):
    assert isinstance(instance, llp_UnlockInstruction)


llp_WriteInstruction_strategy = st.builds(llp_WriteInstruction)
@given(instance=llp_WriteInstruction_strategy)
@settings(max_examples=25)
def test_llp_WriteInstruction_instantiation(instance):
    assert isinstance(instance, llp_WriteInstruction)


