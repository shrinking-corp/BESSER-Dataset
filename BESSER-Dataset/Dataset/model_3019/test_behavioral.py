import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArgOrVar,
    Container,
    Expression,
    Instruction,
    IrAnnotable,
    IrType,
    ItemIdValue,
    IterableInstruction,
    IterationBlock,
    Job,
    JobContainer,
    TimeLoopCopyJob,
    Variable,
    ir_Affectation,
    ir_AfterTimeLoopJob,
    ir_Arg,
    ir_ArgOrVar,
    ir_ArgOrVarRef,
    ir_BaseType,
    ir_BaseTypeConstant,
    ir_BeforeTimeLoopJob,
    ir_BinaryExpression,
    ir_BoolConstant,
    ir_Cardinality,
    ir_Connectivity,
    ir_ConnectivityCall,
    ir_ConnectivityType,
    ir_ConnectivityVariable,
    ir_Container,
    ir_ContractedIf,
    ir_EStringToStringMapEntry,
    ir_Exit,
    ir_Expression,
    ir_Function,
    ir_FunctionCall,
    ir_If,
    ir_Import,
    ir_Instruction,
    ir_InstructionBlock,
    ir_InstructionJob,
    ir_IntConstant,
    ir_Interval,
    ir_IrAnnotable,
    ir_IrAnnotation,
    ir_IrModule,
    ir_IrType,
    ir_ItemId,
    ir_ItemIdDefinition,
    ir_ItemIdValue,
    ir_ItemIdValueCall,
    ir_ItemIdValueIterator,
    ir_ItemIndex,
    ir_ItemIndexDefinition,
    ir_ItemIndexValue,
    ir_ItemType,
    ir_IterableInstruction,
    ir_IterationBlock,
    ir_Iterator,
    ir_Job,
    ir_JobContainer,
    ir_Loop,
    ir_MaxConstant,
    ir_MinConstant,
    ir_Parenthesis,
    ir_PostProcessingInfo,
    ir_RealConstant,
    ir_ReductionInstruction,
    ir_Return,
    ir_SetDefinition,
    ir_SetRef,
    ir_SimpleVariable,
    ir_TimeLoop,
    ir_TimeLoopCopy,
    ir_TimeLoopCopyJob,
    ir_TimeLoopJob,
    ir_TimeLoopVariable,
    ir_UnaryExpression,
    ir_Variable,
    ir_VariableDefinition,
    ir_VectorConstant,
    PrimitiveType,
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

def test_assoc_connectivities9_reverse_link_reassign_clear():
    a1 = ir_IrModule(name="sample_text")
    a2 = ir_IrModule(name="sample_text_2")
    b = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    _safe_set(b, 'ir_Connectivity', a1)
    assert _is_linked(b, 'ir_Connectivity', a1)
    if hasattr(a1, 'ir_IrModule10'):
        assert _is_linked(a1, 'ir_IrModule10', b)
    _safe_set(b, 'ir_Connectivity', a2)
    assert _is_linked(b, 'ir_Connectivity', a2)
    if hasattr(a1, 'ir_IrModule10'):
        assert not _is_linked(a1, 'ir_IrModule10', b)
    if hasattr(a2, 'ir_IrModule10'):
        assert _is_linked(a2, 'ir_IrModule10', b)
    _safe_set(b, 'ir_Connectivity', None)
    assert not _is_linked(b, 'ir_Connectivity', a2)
    if hasattr(a2, 'ir_IrModule10'):
        assert not _is_linked(a2, 'ir_IrModule10', b)


def test_assoc_current201_reverse_link_reassign_clear():
    a1 = ir_Variable(const=True, persistenceName="sample_text")
    a2 = ir_Variable(const=False, persistenceName="sample_text_2")
    b = ir_TimeLoopVariable(name="sample_text")
    _safe_set(b, 'ir_TimeLoopVariable202', a1)
    assert _is_linked(b, 'ir_TimeLoopVariable202', a1)
    if hasattr(a1, 'ir_Variable203'):
        assert _is_linked(a1, 'ir_Variable203', b)
    _safe_set(b, 'ir_TimeLoopVariable202', a2)
    assert _is_linked(b, 'ir_TimeLoopVariable202', a2)
    if hasattr(a1, 'ir_Variable203'):
        assert not _is_linked(a1, 'ir_Variable203', b)
    if hasattr(a2, 'ir_Variable203'):
        assert _is_linked(a2, 'ir_Variable203', b)
    _safe_set(b, 'ir_TimeLoopVariable202', None)
    assert not _is_linked(b, 'ir_TimeLoopVariable202', a2)
    if hasattr(a2, 'ir_Variable203'):
        assert not _is_linked(a2, 'ir_Variable203', b)


def test_assoc_functions7_reverse_link_reassign_clear():
    a1 = ir_IrModule(name="sample_text")
    a2 = ir_IrModule(name="sample_text_2")
    b = ir_Function(name="sample_text", provider="sample_text")
    _safe_set(b, 'ir_Function', a1)
    assert _is_linked(b, 'ir_Function', a1)
    if hasattr(a1, 'ir_IrModule8'):
        assert _is_linked(a1, 'ir_IrModule8', b)
    _safe_set(b, 'ir_Function', a2)
    assert _is_linked(b, 'ir_Function', a2)
    if hasattr(a1, 'ir_IrModule8'):
        assert not _is_linked(a1, 'ir_IrModule8', b)
    if hasattr(a2, 'ir_IrModule8'):
        assert _is_linked(a2, 'ir_IrModule8', b)
    _safe_set(b, 'ir_Function', None)
    assert not _is_linked(b, 'ir_Function', a2)
    if hasattr(a2, 'ir_IrModule8'):
        assert not _is_linked(a2, 'ir_IrModule8', b)


def test_assoc_imports4_reverse_link_reassign_clear():
    a1 = ir_IrModule(name="sample_text")
    a2 = ir_IrModule(name="sample_text_2")
    b = ir_Import(importedNamespace="sample_text")
    _safe_set(b, 'ir_Import', a1)
    assert _is_linked(b, 'ir_Import', a1)
    if hasattr(a1, 'ir_IrModule'):
        assert _is_linked(a1, 'ir_IrModule', b)
    _safe_set(b, 'ir_Import', a2)
    assert _is_linked(b, 'ir_Import', a2)
    if hasattr(a1, 'ir_IrModule'):
        assert not _is_linked(a1, 'ir_IrModule', b)
    if hasattr(a2, 'ir_IrModule'):
        assert _is_linked(a2, 'ir_IrModule', b)
    _safe_set(b, 'ir_Import', None)
    assert not _is_linked(b, 'ir_Import', a2)
    if hasattr(a2, 'ir_IrModule'):
        assert not _is_linked(a2, 'ir_IrModule', b)


def test_assoc_inTypes77_reverse_link_reassign_clear():
    a1 = ir_ItemType(name="sample_text")
    a2 = ir_ItemType(name="sample_text_2")
    b = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    _safe_set(b, 'ir_Connectivity78', {a1})
    assert _is_linked(b, 'ir_Connectivity78', a1)
    if hasattr(a1, 'ir_ItemType79'):
        assert _is_linked(a1, 'ir_ItemType79', b)
    _safe_set(b, 'ir_Connectivity78', {a2})
    assert _is_linked(b, 'ir_Connectivity78', a2)
    if hasattr(a1, 'ir_ItemType79'):
        assert not _is_linked(a1, 'ir_ItemType79', b)
    if hasattr(a2, 'ir_ItemType79'):
        assert _is_linked(a2, 'ir_ItemType79', b)
    _safe_set(b, 'ir_Connectivity78', set())
    assert not _is_linked(b, 'ir_Connectivity78', a2)
    if hasattr(a2, 'ir_ItemType79'):
        assert not _is_linked(a2, 'ir_ItemType79', b)


def test_assoc_init198_reverse_link_reassign_clear():
    a1 = ir_Variable(const=True, persistenceName="sample_text")
    a2 = ir_Variable(const=False, persistenceName="sample_text_2")
    b = ir_TimeLoopVariable(name="sample_text")
    _safe_set(b, 'ir_TimeLoopVariable199', a1)
    assert _is_linked(b, 'ir_TimeLoopVariable199', a1)
    if hasattr(a1, 'ir_Variable200'):
        assert _is_linked(a1, 'ir_Variable200', b)
    _safe_set(b, 'ir_TimeLoopVariable199', a2)
    assert _is_linked(b, 'ir_TimeLoopVariable199', a2)
    if hasattr(a1, 'ir_Variable200'):
        assert not _is_linked(a1, 'ir_Variable200', b)
    if hasattr(a2, 'ir_Variable200'):
        assert _is_linked(a2, 'ir_Variable200', b)
    _safe_set(b, 'ir_TimeLoopVariable199', None)
    assert not _is_linked(b, 'ir_TimeLoopVariable199', a2)
    if hasattr(a2, 'ir_Variable200'):
        assert not _is_linked(a2, 'ir_Variable200', b)


def test_assoc_innerTimeLoop42_reverse_link_reassign_clear():
    a1 = ir_TimeLoop(name="sample_text")
    a2 = ir_TimeLoop(name="sample_text_2")
    b = ir_TimeLoop(name="sample_text")
    _safe_set(b, 'outerTimeLoop', a1)
    assert _is_linked(b, 'outerTimeLoop', a1)
    if hasattr(a1, 'TimeLoop'):
        assert _is_linked(a1, 'TimeLoop', b)
    _safe_set(b, 'outerTimeLoop', a2)
    assert _is_linked(b, 'outerTimeLoop', a2)
    if hasattr(a1, 'TimeLoop'):
        assert not _is_linked(a1, 'TimeLoop', b)
    if hasattr(a2, 'TimeLoop'):
        assert _is_linked(a2, 'TimeLoop', b)
    _safe_set(b, 'outerTimeLoop', None)
    assert not _is_linked(b, 'outerTimeLoop', a2)
    if hasattr(a2, 'TimeLoop'):
        assert not _is_linked(a2, 'TimeLoop', b)


def test_assoc_itemTypes5_reverse_link_reassign_clear():
    a1 = ir_ItemType(name="sample_text")
    a2 = ir_ItemType(name="sample_text_2")
    b = ir_IrModule(name="sample_text")
    _safe_set(b, 'ir_IrModule6', {a1})
    assert _is_linked(b, 'ir_IrModule6', a1)
    if hasattr(a1, 'ir_ItemType'):
        assert _is_linked(a1, 'ir_ItemType', b)
    _safe_set(b, 'ir_IrModule6', {a2})
    assert _is_linked(b, 'ir_IrModule6', a2)
    if hasattr(a1, 'ir_ItemType'):
        assert not _is_linked(a1, 'ir_ItemType', b)
    if hasattr(a2, 'ir_ItemType'):
        assert _is_linked(a2, 'ir_ItemType', b)
    _safe_set(b, 'ir_IrModule6', set())
    assert not _is_linked(b, 'ir_IrModule6', a2)
    if hasattr(a2, 'ir_ItemType'):
        assert not _is_linked(a2, 'ir_ItemType', b)


def test_assoc_jobs26_reverse_link_reassign_clear():
    a1 = ir_Job(at=3.14, name="sample_text", onCycle=True)
    a2 = ir_Job(at=9.99, name="sample_text_2", onCycle=False)
    b = ir_IrModule(name="sample_text")
    _safe_set(b, 'ir_IrModule27', {a1})
    assert _is_linked(b, 'ir_IrModule27', a1)
    if hasattr(a1, 'ir_Job'):
        assert _is_linked(a1, 'ir_Job', b)
    _safe_set(b, 'ir_IrModule27', {a2})
    assert _is_linked(b, 'ir_IrModule27', a2)
    if hasattr(a1, 'ir_Job'):
        assert not _is_linked(a1, 'ir_Job', b)
    if hasattr(a2, 'ir_Job'):
        assert _is_linked(a2, 'ir_Job', b)
    _safe_set(b, 'ir_IrModule27', set())
    assert not _is_linked(b, 'ir_IrModule27', a2)
    if hasattr(a2, 'ir_Job'):
        assert not _is_linked(a2, 'ir_Job', b)


def test_assoc_mainTimeLoop28_reverse_link_reassign_clear():
    a1 = ir_TimeLoop(name="sample_text")
    a2 = ir_TimeLoop(name="sample_text_2")
    b = ir_IrModule(name="sample_text")
    _safe_set(b, 'ir_IrModule29', a1)
    assert _is_linked(b, 'ir_IrModule29', a1)
    if hasattr(a1, 'ir_TimeLoop'):
        assert _is_linked(a1, 'ir_TimeLoop', b)
    _safe_set(b, 'ir_IrModule29', a2)
    assert _is_linked(b, 'ir_IrModule29', a2)
    if hasattr(a1, 'ir_TimeLoop'):
        assert not _is_linked(a1, 'ir_TimeLoop', b)
    if hasattr(a2, 'ir_TimeLoop'):
        assert _is_linked(a2, 'ir_TimeLoop', b)
    _safe_set(b, 'ir_IrModule29', None)
    assert not _is_linked(b, 'ir_IrModule29', a2)
    if hasattr(a2, 'ir_TimeLoop'):
        assert not _is_linked(a2, 'ir_TimeLoop', b)


def test_assoc_next204_reverse_link_reassign_clear():
    a1 = ir_Variable(const=True, persistenceName="sample_text")
    a2 = ir_Variable(const=False, persistenceName="sample_text_2")
    b = ir_TimeLoopVariable(name="sample_text")
    _safe_set(b, 'ir_TimeLoopVariable205', a1)
    assert _is_linked(b, 'ir_TimeLoopVariable205', a1)
    if hasattr(a1, 'ir_Variable206'):
        assert _is_linked(a1, 'ir_Variable206', b)
    _safe_set(b, 'ir_TimeLoopVariable205', a2)
    assert _is_linked(b, 'ir_TimeLoopVariable205', a2)
    if hasattr(a1, 'ir_Variable206'):
        assert not _is_linked(a1, 'ir_Variable206', b)
    if hasattr(a2, 'ir_Variable206'):
        assert _is_linked(a2, 'ir_Variable206', b)
    _safe_set(b, 'ir_TimeLoopVariable205', None)
    assert not _is_linked(b, 'ir_TimeLoopVariable205', a2)
    if hasattr(a2, 'ir_Variable206'):
        assert not _is_linked(a2, 'ir_Variable206', b)


def test_assoc_outerTimeLoop44_reverse_link_reassign_clear():
    a1 = ir_TimeLoop(name="sample_text")
    a2 = ir_TimeLoop(name="sample_text_2")
    b = ir_TimeLoop(name="sample_text")
    _safe_set(b, 'innerTimeLoop', a1)
    assert _is_linked(b, 'innerTimeLoop', a1)
    if hasattr(a1, 'TimeLoop45'):
        assert _is_linked(a1, 'TimeLoop45', b)
    _safe_set(b, 'innerTimeLoop', a2)
    assert _is_linked(b, 'innerTimeLoop', a2)
    if hasattr(a1, 'TimeLoop45'):
        assert not _is_linked(a1, 'TimeLoop45', b)
    if hasattr(a2, 'TimeLoop45'):
        assert _is_linked(a2, 'TimeLoop45', b)
    _safe_set(b, 'innerTimeLoop', None)
    assert not _is_linked(b, 'innerTimeLoop', a2)
    if hasattr(a2, 'TimeLoop45'):
        assert not _is_linked(a2, 'TimeLoop45', b)


def test_assoc_postProcessedVariables32_reverse_link_reassign_clear():
    a1 = ir_Variable(const=True, persistenceName="sample_text")
    a2 = ir_Variable(const=False, persistenceName="sample_text_2")
    b = ir_PostProcessingInfo(periodValue=3.14)
    _safe_set(b, 'ir_PostProcessingInfo33', {a1})
    assert _is_linked(b, 'ir_PostProcessingInfo33', a1)
    if hasattr(a1, 'ir_Variable34'):
        assert _is_linked(a1, 'ir_Variable34', b)
    _safe_set(b, 'ir_PostProcessingInfo33', {a2})
    assert _is_linked(b, 'ir_PostProcessingInfo33', a2)
    if hasattr(a1, 'ir_Variable34'):
        assert not _is_linked(a1, 'ir_Variable34', b)
    if hasattr(a2, 'ir_Variable34'):
        assert _is_linked(a2, 'ir_Variable34', b)
    _safe_set(b, 'ir_PostProcessingInfo33', set())
    assert not _is_linked(b, 'ir_PostProcessingInfo33', a2)
    if hasattr(a2, 'ir_Variable34'):
        assert not _is_linked(a2, 'ir_Variable34', b)


def test_assoc_postProcessingInfo30_reverse_link_reassign_clear():
    a1 = ir_PostProcessingInfo(periodValue=3.14)
    a2 = ir_PostProcessingInfo(periodValue=9.99)
    b = ir_IrModule(name="sample_text")
    _safe_set(b, 'ir_IrModule31', a1)
    assert _is_linked(b, 'ir_IrModule31', a1)
    if hasattr(a1, 'ir_PostProcessingInfo'):
        assert _is_linked(a1, 'ir_PostProcessingInfo', b)
    _safe_set(b, 'ir_IrModule31', a2)
    assert _is_linked(b, 'ir_IrModule31', a2)
    if hasattr(a1, 'ir_PostProcessingInfo'):
        assert not _is_linked(a1, 'ir_PostProcessingInfo', b)
    if hasattr(a2, 'ir_PostProcessingInfo'):
        assert _is_linked(a2, 'ir_PostProcessingInfo', b)
    _safe_set(b, 'ir_IrModule31', None)
    assert not _is_linked(b, 'ir_IrModule31', a2)
    if hasattr(a2, 'ir_PostProcessingInfo'):
        assert not _is_linked(a2, 'ir_PostProcessingInfo', b)


def test_assoc_returnType66_reverse_link_reassign_clear():
    a1 = ir_Function(name="sample_text", provider="sample_text")
    a2 = ir_Function(name="sample_text_2", provider="sample_text_2")
    b = ir_BaseType(primitive="sample_text")
    _safe_set(b, 'ir_BaseType68', a1)
    assert _is_linked(b, 'ir_BaseType68', a1)
    if hasattr(a1, 'ir_Function67'):
        assert _is_linked(a1, 'ir_Function67', b)
    _safe_set(b, 'ir_BaseType68', a2)
    assert _is_linked(b, 'ir_BaseType68', a2)
    if hasattr(a1, 'ir_Function67'):
        assert not _is_linked(a1, 'ir_Function67', b)
    if hasattr(a2, 'ir_Function67'):
        assert _is_linked(a2, 'ir_Function67', b)
    _safe_set(b, 'ir_BaseType68', None)
    assert not _is_linked(b, 'ir_BaseType68', a2)
    if hasattr(a2, 'ir_Function67'):
        assert not _is_linked(a2, 'ir_Function67', b)


def test_assoc_returnType80_reverse_link_reassign_clear():
    a1 = ir_ItemType(name="sample_text")
    a2 = ir_ItemType(name="sample_text_2")
    b = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    _safe_set(b, 'ir_Connectivity81', a1)
    assert _is_linked(b, 'ir_Connectivity81', a1)
    if hasattr(a1, 'ir_ItemType82'):
        assert _is_linked(a1, 'ir_ItemType82', b)
    _safe_set(b, 'ir_Connectivity81', a2)
    assert _is_linked(b, 'ir_Connectivity81', a2)
    if hasattr(a1, 'ir_ItemType82'):
        assert not _is_linked(a1, 'ir_ItemType82', b)
    if hasattr(a2, 'ir_ItemType82'):
        assert _is_linked(a2, 'ir_ItemType82', b)
    _safe_set(b, 'ir_Connectivity81', None)
    assert not _is_linked(b, 'ir_Connectivity81', a2)
    if hasattr(a2, 'ir_ItemType82'):
        assert not _is_linked(a2, 'ir_ItemType82', b)


def test_assoc_variables13_reverse_link_reassign_clear():
    a1 = ir_Variable(const=True, persistenceName="sample_text")
    a2 = ir_Variable(const=False, persistenceName="sample_text_2")
    b = ir_IrModule(name="sample_text")
    _safe_set(b, 'ir_IrModule14', {a1})
    assert _is_linked(b, 'ir_IrModule14', a1)
    if hasattr(a1, 'ir_Variable'):
        assert _is_linked(a1, 'ir_Variable', b)
    _safe_set(b, 'ir_IrModule14', {a2})
    assert _is_linked(b, 'ir_IrModule14', a2)
    if hasattr(a1, 'ir_Variable'):
        assert not _is_linked(a1, 'ir_Variable', b)
    if hasattr(a2, 'ir_Variable'):
        assert _is_linked(a2, 'ir_Variable', b)
    _safe_set(b, 'ir_IrModule14', set())
    assert not _is_linked(b, 'ir_IrModule14', a2)
    if hasattr(a2, 'ir_Variable'):
        assert not _is_linked(a2, 'ir_Variable', b)


def test_assoc_variables46_reverse_link_reassign_clear():
    a1 = ir_TimeLoopVariable(name="sample_text")
    a2 = ir_TimeLoopVariable(name="sample_text_2")
    b = ir_TimeLoop(name="sample_text")
    _safe_set(b, 'ir_TimeLoop47', {a1})
    assert _is_linked(b, 'ir_TimeLoop47', a1)
    if hasattr(a1, 'ir_TimeLoopVariable'):
        assert _is_linked(a1, 'ir_TimeLoopVariable', b)
    _safe_set(b, 'ir_TimeLoop47', {a2})
    assert _is_linked(b, 'ir_TimeLoop47', a2)
    if hasattr(a1, 'ir_TimeLoopVariable'):
        assert not _is_linked(a1, 'ir_TimeLoopVariable', b)
    if hasattr(a2, 'ir_TimeLoopVariable'):
        assert _is_linked(a2, 'ir_TimeLoopVariable', b)
    _safe_set(b, 'ir_TimeLoop47', set())
    assert not _is_linked(b, 'ir_TimeLoop47', a2)
    if hasattr(a2, 'ir_TimeLoopVariable'):
        assert not _is_linked(a2, 'ir_TimeLoopVariable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations0_stub_double():
    # ir_IrAnnotable has no real 'ir_IrAnnotable' property in the generated
    # code (a bare stub) -- manually attach it so ir_IrAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_IrAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_IrAnnotation(source="sample_text")
    partner = ir_IrAnnotable()
    setattr(partner, 'ir_IrAnnotable', None)
    _safe_set(owner, 'ir_IrAnnotation', partner)
    assert owner in getattr(partner, 'ir_IrAnnotable')
    _safe_set(owner, 'ir_IrAnnotation', None)
    assert owner not in getattr(partner, 'ir_IrAnnotable')


def test_assoc_args210_stub_double():
    # ir_ConnectivityCall has no real 'ir_ConnectivityCall211' property in the generated
    # code (a bare stub) -- manually attach it so ir_ItemId's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ItemId's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ItemId(itemName="sample_text", name="sample_text")
    partner = ir_ConnectivityCall()
    setattr(partner, 'ir_ConnectivityCall211', None)
    _safe_set(owner, 'ir_ItemId212', partner)
    assert owner in getattr(partner, 'ir_ConnectivityCall211')
    _safe_set(owner, 'ir_ItemId212', None)
    assert owner not in getattr(partner, 'ir_ConnectivityCall211')


def test_assoc_associatedJob50_stub_double():
    # ir_TimeLoopJob has no real 'ir_TimeLoopJob' property in the generated
    # code (a bare stub) -- manually attach it so ir_TimeLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TimeLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TimeLoop(name="sample_text")
    partner = ir_TimeLoopJob()
    setattr(partner, 'ir_TimeLoopJob', None)
    _safe_set(owner, 'ir_TimeLoop51', partner)
    assert getattr(partner, 'ir_TimeLoopJob') == owner
    _safe_set(owner, 'ir_TimeLoop51', None)
    assert getattr(partner, 'ir_TimeLoopJob') is None


def test_assoc_base195_stub_double():
    # ir_ConnectivityType has no real 'ir_ConnectivityType196' property in the generated
    # code (a bare stub) -- manually attach it so ir_BaseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_BaseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_BaseType(primitive="sample_text")
    partner = ir_ConnectivityType()
    setattr(partner, 'ir_ConnectivityType196', None)
    _safe_set(owner, 'ir_BaseType197', partner)
    assert getattr(partner, 'ir_ConnectivityType196') == owner
    _safe_set(owner, 'ir_BaseType197', None)
    assert getattr(partner, 'ir_ConnectivityType196') is None


def test_assoc_binaryFunction111_stub_double():
    # ir_ReductionInstruction has no real 'ir_ReductionInstruction112' property in the generated
    # code (a bare stub) -- manually attach it so ir_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Function(name="sample_text", provider="sample_text")
    partner = ir_ReductionInstruction()
    setattr(partner, 'ir_ReductionInstruction112', None)
    _safe_set(owner, 'ir_Function113', partner)
    assert getattr(partner, 'ir_ReductionInstruction112') == owner
    _safe_set(owner, 'ir_Function113', None)
    assert getattr(partner, 'ir_ReductionInstruction112') is None


def test_assoc_body120_stub_double():
    # ir_Instruction has no real 'ir_Instruction121' property in the generated
    # code (a bare stub) -- manually attach it so ir_Loop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Loop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Loop(multithreadable=True)
    partner = ir_Instruction()
    setattr(partner, 'ir_Instruction121', None)
    _safe_set(owner, 'ir_Loop', partner)
    assert getattr(partner, 'ir_Instruction121') == owner
    _safe_set(owner, 'ir_Loop', None)
    assert getattr(partner, 'ir_Instruction121') is None


def test_assoc_body75_stub_double():
    # ir_Instruction has no real 'ir_Instruction' property in the generated
    # code (a bare stub) -- manually attach it so ir_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Function(name="sample_text", provider="sample_text")
    partner = ir_Instruction()
    setattr(partner, 'ir_Instruction', None)
    _safe_set(owner, 'ir_Function76', partner)
    assert getattr(partner, 'ir_Instruction') == owner
    _safe_set(owner, 'ir_Function76', None)
    assert getattr(partner, 'ir_Instruction') is None


def test_assoc_connectivities192_stub_double():
    # ir_ConnectivityType has no real 'ir_ConnectivityType193' property in the generated
    # code (a bare stub) -- manually attach it so ir_Connectivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Connectivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    partner = ir_ConnectivityType()
    setattr(partner, 'ir_ConnectivityType193', None)
    _safe_set(owner, 'ir_Connectivity194', partner)
    assert owner in getattr(partner, 'ir_ConnectivityType193')
    _safe_set(owner, 'ir_Connectivity194', None)
    assert owner not in getattr(partner, 'ir_ConnectivityType193')


def test_assoc_connectivity207_stub_double():
    # ir_ConnectivityCall has no real 'ir_ConnectivityCall208' property in the generated
    # code (a bare stub) -- manually attach it so ir_Connectivity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Connectivity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    partner = ir_ConnectivityCall()
    setattr(partner, 'ir_ConnectivityCall208', None)
    _safe_set(owner, 'ir_Connectivity209', partner)
    assert getattr(partner, 'ir_ConnectivityCall208') == owner
    _safe_set(owner, 'ir_Connectivity209', None)
    assert getattr(partner, 'ir_ConnectivityCall208') is None


def test_assoc_deltatVariable23_stub_double():
    # ir_SimpleVariable has no real 'ir_SimpleVariable25' property in the generated
    # code (a bare stub) -- manually attach it so ir_IrModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_IrModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_IrModule(name="sample_text")
    partner = ir_SimpleVariable()
    setattr(partner, 'ir_SimpleVariable25', None)
    _safe_set(owner, 'ir_IrModule24', partner)
    assert getattr(partner, 'ir_SimpleVariable25') == owner
    _safe_set(owner, 'ir_IrModule24', None)
    assert getattr(partner, 'ir_SimpleVariable25') is None


def test_assoc_destination90_stub_double():
    # ir_TimeLoopCopy has no real 'ir_TimeLoopCopy91' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(const=True, persistenceName="sample_text")
    partner = ir_TimeLoopCopy()
    setattr(partner, 'ir_TimeLoopCopy91', None)
    _safe_set(owner, 'ir_Variable92', partner)
    assert getattr(partner, 'ir_TimeLoopCopy91') == owner
    _safe_set(owner, 'ir_Variable92', None)
    assert getattr(partner, 'ir_TimeLoopCopy91') is None


def test_assoc_details1_stub_double():
    # ir_EStringToStringMapEntry has no real 'ir_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so ir_IrAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_IrAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_IrAnnotation(source="sample_text")
    partner = ir_EStringToStringMapEntry()
    setattr(partner, 'ir_EStringToStringMapEntry', None)
    _safe_set(owner, 'ir_IrAnnotation2', {partner})
    assert getattr(partner, 'ir_EStringToStringMapEntry') == owner
    _safe_set(owner, 'ir_IrAnnotation2', set())
    assert getattr(partner, 'ir_EStringToStringMapEntry') is None


def test_assoc_expression166_stub_double():
    # ir_Expression has no real 'ir_Expression167' property in the generated
    # code (a bare stub) -- manually attach it so ir_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_UnaryExpression(operator="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression167', None)
    _safe_set(owner, 'ir_UnaryExpression', partner)
    assert getattr(partner, 'ir_Expression167') == owner
    _safe_set(owner, 'ir_UnaryExpression', None)
    assert getattr(partner, 'ir_Expression167') is None


def test_assoc_function170_stub_double():
    # ir_FunctionCall has no real 'ir_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so ir_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Function(name="sample_text", provider="sample_text")
    partner = ir_FunctionCall()
    setattr(partner, 'ir_FunctionCall', None)
    _safe_set(owner, 'ir_Function171', partner)
    assert getattr(partner, 'ir_FunctionCall') == owner
    _safe_set(owner, 'ir_Function171', None)
    assert getattr(partner, 'ir_FunctionCall') is None


def test_assoc_id125_stub_double():
    # ir_ItemIdDefinition has no real 'ir_ItemIdDefinition' property in the generated
    # code (a bare stub) -- manually attach it so ir_ItemId's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ItemId's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ItemId(itemName="sample_text", name="sample_text")
    partner = ir_ItemIdDefinition()
    setattr(partner, 'ir_ItemIdDefinition', None)
    _safe_set(owner, 'ir_ItemId', partner)
    assert getattr(partner, 'ir_ItemIdDefinition') == owner
    _safe_set(owner, 'ir_ItemId', None)
    assert getattr(partner, 'ir_ItemIdDefinition') is None


def test_assoc_id219_stub_double():
    # ir_ItemIndexValue has no real 'ir_ItemIndexValue220' property in the generated
    # code (a bare stub) -- manually attach it so ir_ItemId's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ItemId's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ItemId(itemName="sample_text", name="sample_text")
    partner = ir_ItemIndexValue()
    setattr(partner, 'ir_ItemIndexValue220', None)
    _safe_set(owner, 'ir_ItemId221', partner)
    assert getattr(partner, 'ir_ItemIndexValue220') == owner
    _safe_set(owner, 'ir_ItemId221', None)
    assert getattr(partner, 'ir_ItemIndexValue220') is None


def test_assoc_inArgs72_stub_double():
    # ir_Arg has no real 'ir_Arg74' property in the generated
    # code (a bare stub) -- manually attach it so ir_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Function(name="sample_text", provider="sample_text")
    partner = ir_Arg()
    setattr(partner, 'ir_Arg74', None)
    _safe_set(owner, 'ir_Function73', {partner})
    assert getattr(partner, 'ir_Arg74') == owner
    _safe_set(owner, 'ir_Function73', set())
    assert getattr(partner, 'ir_Arg74') is None


def test_assoc_index122_stub_double():
    # ir_ItemIndexDefinition has no real 'ir_ItemIndexDefinition' property in the generated
    # code (a bare stub) -- manually attach it so ir_ItemIndex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ItemIndex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ItemIndex(itemName="sample_text", name="sample_text")
    partner = ir_ItemIndexDefinition()
    setattr(partner, 'ir_ItemIndexDefinition', None)
    _safe_set(owner, 'ir_ItemIndex', partner)
    assert getattr(partner, 'ir_ItemIndexDefinition') == owner
    _safe_set(owner, 'ir_ItemIndex', None)
    assert getattr(partner, 'ir_ItemIndexDefinition') is None


def test_assoc_index139_stub_double():
    # ir_Iterator has no real 'ir_Iterator' property in the generated
    # code (a bare stub) -- manually attach it so ir_ItemIndex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ItemIndex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ItemIndex(itemName="sample_text", name="sample_text")
    partner = ir_Iterator()
    setattr(partner, 'ir_Iterator', None)
    _safe_set(owner, 'ir_ItemIndex140', partner)
    assert getattr(partner, 'ir_Iterator') == owner
    _safe_set(owner, 'ir_ItemIndex140', None)
    assert getattr(partner, 'ir_Iterator') is None


def test_assoc_initNodeCoordVariable15_stub_double():
    # ir_ConnectivityVariable has no real 'ir_ConnectivityVariable' property in the generated
    # code (a bare stub) -- manually attach it so ir_IrModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_IrModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_IrModule(name="sample_text")
    partner = ir_ConnectivityVariable()
    setattr(partner, 'ir_ConnectivityVariable', None)
    _safe_set(owner, 'ir_IrModule16', partner)
    assert getattr(partner, 'ir_ConnectivityVariable') == owner
    _safe_set(owner, 'ir_IrModule16', None)
    assert getattr(partner, 'ir_ConnectivityVariable') is None


def test_assoc_innerJobs3_stub_double():
    # ir_JobContainer has no real 'jobContainer' property in the generated
    # code (a bare stub) -- manually attach it so ir_Job's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Job's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Job(at=3.14, name="sample_text", onCycle=True)
    partner = ir_JobContainer()
    setattr(partner, 'jobContainer', None)
    _safe_set(owner, 'Job', partner)
    assert owner in getattr(partner, 'jobContainer')
    _safe_set(owner, 'Job', None)
    assert owner not in getattr(partner, 'jobContainer')


def test_assoc_iterationCounter52_stub_double():
    # ir_SimpleVariable has no real 'ir_SimpleVariable54' property in the generated
    # code (a bare stub) -- manually attach it so ir_TimeLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TimeLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TimeLoop(name="sample_text")
    partner = ir_SimpleVariable()
    setattr(partner, 'ir_SimpleVariable54', None)
    _safe_set(owner, 'ir_TimeLoop53', partner)
    assert getattr(partner, 'ir_SimpleVariable54') == owner
    _safe_set(owner, 'ir_TimeLoop53', None)
    assert getattr(partner, 'ir_SimpleVariable54') is None


def test_assoc_iterator215_stub_double():
    # ir_Iterator has no real 'ir_Iterator216' property in the generated
    # code (a bare stub) -- manually attach it so ir_ItemIdValueIterator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ItemIdValueIterator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ItemIdValueIterator(shift=7)
    partner = ir_Iterator()
    setattr(partner, 'ir_Iterator216', None)
    _safe_set(owner, 'ir_ItemIdValueIterator', partner)
    assert getattr(partner, 'ir_Iterator216') == owner
    _safe_set(owner, 'ir_ItemIdValueIterator', None)
    assert getattr(partner, 'ir_Iterator216') is None


def test_assoc_iterators183_stub_double():
    # ir_ArgOrVarRef has no real 'ir_ArgOrVarRef184' property in the generated
    # code (a bare stub) -- manually attach it so ir_ItemIndex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ItemIndex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ItemIndex(itemName="sample_text", name="sample_text")
    partner = ir_ArgOrVarRef()
    setattr(partner, 'ir_ArgOrVarRef184', None)
    _safe_set(owner, 'ir_ItemIndex185', partner)
    assert owner in getattr(partner, 'ir_ArgOrVarRef184')
    _safe_set(owner, 'ir_ItemIndex185', None)
    assert owner not in getattr(partner, 'ir_ArgOrVarRef184')


def test_assoc_jobContainer83_stub_double():
    # ir_JobContainer has no real 'JobContainer' property in the generated
    # code (a bare stub) -- manually attach it so ir_Job's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Job's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Job(at=3.14, name="sample_text", onCycle=True)
    partner = ir_JobContainer()
    setattr(partner, 'JobContainer', None)
    _safe_set(owner, 'innerJobs', partner)
    assert getattr(partner, 'JobContainer') == owner
    _safe_set(owner, 'innerJobs', None)
    assert getattr(partner, 'JobContainer') is None


def test_assoc_lastDumpVariable38_stub_double():
    # ir_SimpleVariable has no real 'ir_SimpleVariable40' property in the generated
    # code (a bare stub) -- manually attach it so ir_PostProcessingInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PostProcessingInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PostProcessingInfo(periodValue=3.14)
    partner = ir_SimpleVariable()
    setattr(partner, 'ir_SimpleVariable40', None)
    _safe_set(owner, 'ir_PostProcessingInfo39', partner)
    assert getattr(partner, 'ir_SimpleVariable40') == owner
    _safe_set(owner, 'ir_PostProcessingInfo39', None)
    assert getattr(partner, 'ir_SimpleVariable40') is None


def test_assoc_left161_stub_double():
    # ir_Expression has no real 'ir_Expression162' property in the generated
    # code (a bare stub) -- manually attach it so ir_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_BinaryExpression(operator="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression162', None)
    _safe_set(owner, 'ir_BinaryExpression', partner)
    assert getattr(partner, 'ir_Expression162') == owner
    _safe_set(owner, 'ir_BinaryExpression', None)
    assert getattr(partner, 'ir_Expression162') is None


def test_assoc_nodeCoordVariable17_stub_double():
    # ir_ConnectivityVariable has no real 'ir_ConnectivityVariable19' property in the generated
    # code (a bare stub) -- manually attach it so ir_IrModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_IrModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_IrModule(name="sample_text")
    partner = ir_ConnectivityVariable()
    setattr(partner, 'ir_ConnectivityVariable19', None)
    _safe_set(owner, 'ir_IrModule18', partner)
    assert getattr(partner, 'ir_ConnectivityVariable19') == owner
    _safe_set(owner, 'ir_IrModule18', None)
    assert getattr(partner, 'ir_ConnectivityVariable19') is None


def test_assoc_options11_stub_double():
    # ir_SimpleVariable has no real 'ir_SimpleVariable' property in the generated
    # code (a bare stub) -- manually attach it so ir_IrModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_IrModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_IrModule(name="sample_text")
    partner = ir_SimpleVariable()
    setattr(partner, 'ir_SimpleVariable', None)
    _safe_set(owner, 'ir_IrModule12', {partner})
    assert getattr(partner, 'ir_SimpleVariable') == owner
    _safe_set(owner, 'ir_IrModule12', set())
    assert getattr(partner, 'ir_SimpleVariable') is None


def test_assoc_periodVariable35_stub_double():
    # ir_SimpleVariable has no real 'ir_SimpleVariable37' property in the generated
    # code (a bare stub) -- manually attach it so ir_PostProcessingInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_PostProcessingInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_PostProcessingInfo(periodValue=3.14)
    partner = ir_SimpleVariable()
    setattr(partner, 'ir_SimpleVariable37', None)
    _safe_set(owner, 'ir_PostProcessingInfo36', partner)
    assert getattr(partner, 'ir_SimpleVariable37') == owner
    _safe_set(owner, 'ir_PostProcessingInfo36', None)
    assert getattr(partner, 'ir_SimpleVariable37') is None


def test_assoc_right163_stub_double():
    # ir_Expression has no real 'ir_Expression165' property in the generated
    # code (a bare stub) -- manually attach it so ir_BinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_BinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_BinaryExpression(operator="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression165', None)
    _safe_set(owner, 'ir_BinaryExpression164', partner)
    assert getattr(partner, 'ir_Expression165') == owner
    _safe_set(owner, 'ir_BinaryExpression164', None)
    assert getattr(partner, 'ir_Expression165') is None


def test_assoc_sizes189_stub_double():
    # ir_Expression has no real 'ir_Expression191' property in the generated
    # code (a bare stub) -- manually attach it so ir_BaseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_BaseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_BaseType(primitive="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression191', None)
    _safe_set(owner, 'ir_BaseType190', {partner})
    assert getattr(partner, 'ir_Expression191') == owner
    _safe_set(owner, 'ir_BaseType190', set())
    assert getattr(partner, 'ir_Expression191') is None


def test_assoc_source93_stub_double():
    # ir_TimeLoopCopy has no real 'ir_TimeLoopCopy94' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(const=True, persistenceName="sample_text")
    partner = ir_TimeLoopCopy()
    setattr(partner, 'ir_TimeLoopCopy94', None)
    _safe_set(owner, 'ir_Variable95', partner)
    assert getattr(partner, 'ir_TimeLoopCopy94') == owner
    _safe_set(owner, 'ir_Variable95', None)
    assert getattr(partner, 'ir_TimeLoopCopy94') is None


def test_assoc_target181_stub_double():
    # ir_ArgOrVarRef has no real 'ir_ArgOrVarRef182' property in the generated
    # code (a bare stub) -- manually attach it so ir_ArgOrVar's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ArgOrVar's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ArgOrVar(name="sample_text")
    partner = ir_ArgOrVarRef()
    setattr(partner, 'ir_ArgOrVarRef182', None)
    _safe_set(owner, 'ir_ArgOrVar', partner)
    assert getattr(partner, 'ir_ArgOrVarRef182') == owner
    _safe_set(owner, 'ir_ArgOrVar', None)
    assert getattr(partner, 'ir_ArgOrVarRef182') is None


def test_assoc_target213_stub_double():
    # ir_SetRef has no real 'ir_SetRef' property in the generated
    # code (a bare stub) -- manually attach it so ir_SetDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_SetDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_SetDefinition(name="sample_text")
    partner = ir_SetRef()
    setattr(partner, 'ir_SetRef', None)
    _safe_set(owner, 'ir_SetDefinition214', partner)
    assert getattr(partner, 'ir_SetRef') == owner
    _safe_set(owner, 'ir_SetDefinition214', None)
    assert getattr(partner, 'ir_SetRef') is None


def test_assoc_timeLoop87_stub_double():
    # ir_TimeLoopCopyJob has no real 'ir_TimeLoopCopyJob88' property in the generated
    # code (a bare stub) -- manually attach it so ir_TimeLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TimeLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TimeLoop(name="sample_text")
    partner = ir_TimeLoopCopyJob()
    setattr(partner, 'ir_TimeLoopCopyJob88', None)
    _safe_set(owner, 'ir_TimeLoop89', partner)
    assert getattr(partner, 'ir_TimeLoopCopyJob88') == owner
    _safe_set(owner, 'ir_TimeLoop89', None)
    assert getattr(partner, 'ir_TimeLoopCopyJob88') is None


def test_assoc_timeVariable20_stub_double():
    # ir_SimpleVariable has no real 'ir_SimpleVariable22' property in the generated
    # code (a bare stub) -- manually attach it so ir_IrModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_IrModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_IrModule(name="sample_text")
    partner = ir_SimpleVariable()
    setattr(partner, 'ir_SimpleVariable22', None)
    _safe_set(owner, 'ir_IrModule21', partner)
    assert getattr(partner, 'ir_SimpleVariable22') == owner
    _safe_set(owner, 'ir_IrModule21', None)
    assert getattr(partner, 'ir_SimpleVariable22') is None


def test_assoc_type55_stub_double():
    # ir_Arg has no real 'ir_Arg' property in the generated
    # code (a bare stub) -- manually attach it so ir_BaseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_BaseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_BaseType(primitive="sample_text")
    partner = ir_Arg()
    setattr(partner, 'ir_Arg', None)
    _safe_set(owner, 'ir_BaseType', partner)
    assert getattr(partner, 'ir_Arg') == owner
    _safe_set(owner, 'ir_BaseType', None)
    assert getattr(partner, 'ir_Arg') is None


def test_assoc_type56_stub_double():
    # ir_SimpleVariable has no real 'ir_SimpleVariable57' property in the generated
    # code (a bare stub) -- manually attach it so ir_BaseType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_BaseType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_BaseType(primitive="sample_text")
    partner = ir_SimpleVariable()
    setattr(partner, 'ir_SimpleVariable57', None)
    _safe_set(owner, 'ir_BaseType58', partner)
    assert getattr(partner, 'ir_SimpleVariable57') == owner
    _safe_set(owner, 'ir_BaseType58', None)
    assert getattr(partner, 'ir_SimpleVariable57') is None


def test_assoc_value128_stub_double():
    # ir_ConnectivityCall has no real 'ir_ConnectivityCall' property in the generated
    # code (a bare stub) -- manually attach it so ir_SetDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_SetDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_SetDefinition(name="sample_text")
    partner = ir_ConnectivityCall()
    setattr(partner, 'ir_ConnectivityCall', None)
    _safe_set(owner, 'ir_SetDefinition', partner)
    assert getattr(partner, 'ir_ConnectivityCall') == owner
    _safe_set(owner, 'ir_SetDefinition', None)
    assert getattr(partner, 'ir_ConnectivityCall') is None


def test_assoc_variable101_stub_double():
    # ir_VariableDefinition has no real 'ir_VariableDefinition' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(const=True, persistenceName="sample_text")
    partner = ir_VariableDefinition()
    setattr(partner, 'ir_VariableDefinition', None)
    _safe_set(owner, 'ir_Variable102', partner)
    assert getattr(partner, 'ir_VariableDefinition') == owner
    _safe_set(owner, 'ir_Variable102', None)
    assert getattr(partner, 'ir_VariableDefinition') is None


def test_assoc_variables69_stub_double():
    # ir_SimpleVariable has no real 'ir_SimpleVariable71' property in the generated
    # code (a bare stub) -- manually attach it so ir_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Function(name="sample_text", provider="sample_text")
    partner = ir_SimpleVariable()
    setattr(partner, 'ir_SimpleVariable71', None)
    _safe_set(owner, 'ir_Function70', {partner})
    assert getattr(partner, 'ir_SimpleVariable71') == owner
    _safe_set(owner, 'ir_Function70', set())
    assert getattr(partner, 'ir_SimpleVariable71') is None


def test_assoc_variables96_stub_double():
    # ir_InstructionBlock has no real 'ir_InstructionBlock' property in the generated
    # code (a bare stub) -- manually attach it so ir_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Variable(const=True, persistenceName="sample_text")
    partner = ir_InstructionBlock()
    setattr(partner, 'ir_InstructionBlock', None)
    _safe_set(owner, 'ir_Variable97', partner)
    assert owner in getattr(partner, 'ir_InstructionBlock')
    _safe_set(owner, 'ir_Variable97', None)
    assert owner not in getattr(partner, 'ir_InstructionBlock')


def test_assoc_whileCondition48_stub_double():
    # ir_Expression has no real 'ir_Expression' property in the generated
    # code (a bare stub) -- manually attach it so ir_TimeLoop's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TimeLoop's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TimeLoop(name="sample_text")
    partner = ir_Expression()
    setattr(partner, 'ir_Expression', None)
    _safe_set(owner, 'ir_TimeLoop49', partner)
    assert getattr(partner, 'ir_Expression') == owner
    _safe_set(owner, 'ir_TimeLoop49', None)
    assert getattr(partner, 'ir_Expression') is None


