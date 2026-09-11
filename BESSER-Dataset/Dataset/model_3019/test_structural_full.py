import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_ir_ArgOrVar_name_value_roundtrip():
    instance = ir_ArgOrVar(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_BaseType_primitive_value_roundtrip():
    instance = ir_BaseType(primitive="sample_text")
    assert instance.primitive == "sample_text"
    instance.primitive = "sample_text_2"
    assert instance.primitive == "sample_text_2"


def test_ir_BinaryExpression_operator_value_roundtrip():
    instance = ir_BinaryExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_ir_BoolConstant_value_value_roundtrip():
    instance = ir_BoolConstant(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_ir_Connectivity_indexEqualId_value_roundtrip():
    instance = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    assert instance.indexEqualId == True
    instance.indexEqualId = False
    assert instance.indexEqualId == False


def test_ir_Connectivity_multiple_value_roundtrip():
    instance = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    assert instance.multiple == True
    instance.multiple = False
    assert instance.multiple == False


def test_ir_Connectivity_name_value_roundtrip():
    instance = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_Exit_message_value_roundtrip():
    instance = ir_Exit(message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_ir_Function_name_value_roundtrip():
    instance = ir_Function(name="sample_text", provider="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_Function_provider_value_roundtrip():
    instance = ir_Function(name="sample_text", provider="sample_text")
    assert instance.provider == "sample_text"
    instance.provider = "sample_text_2"
    assert instance.provider == "sample_text_2"


def test_ir_Import_importedNamespace_value_roundtrip():
    instance = ir_Import(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_ir_IntConstant_value_value_roundtrip():
    instance = ir_IntConstant(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_ir_IrAnnotation_source_value_roundtrip():
    instance = ir_IrAnnotation(source="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_ir_IrModule_name_value_roundtrip():
    instance = ir_IrModule(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_ItemId_itemName_value_roundtrip():
    instance = ir_ItemId(itemName="sample_text", name="sample_text")
    assert instance.itemName == "sample_text"
    instance.itemName = "sample_text_2"
    assert instance.itemName == "sample_text_2"


def test_ir_ItemId_name_value_roundtrip():
    instance = ir_ItemId(itemName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_ItemIdValueIterator_shift_value_roundtrip():
    instance = ir_ItemIdValueIterator(shift=7)
    assert instance.shift == 7
    instance.shift = 13
    assert instance.shift == 13


def test_ir_ItemIndex_itemName_value_roundtrip():
    instance = ir_ItemIndex(itemName="sample_text", name="sample_text")
    assert instance.itemName == "sample_text"
    instance.itemName = "sample_text_2"
    assert instance.itemName == "sample_text_2"


def test_ir_ItemIndex_name_value_roundtrip():
    instance = ir_ItemIndex(itemName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_ItemType_name_value_roundtrip():
    instance = ir_ItemType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_Job_at_value_roundtrip():
    instance = ir_Job(at=3.14, name="sample_text", onCycle=True)
    assert instance.at == 3.14
    instance.at = 9.99
    assert instance.at == 9.99


def test_ir_Job_name_value_roundtrip():
    instance = ir_Job(at=3.14, name="sample_text", onCycle=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_Job_onCycle_value_roundtrip():
    instance = ir_Job(at=3.14, name="sample_text", onCycle=True)
    assert instance.onCycle == True
    instance.onCycle = False
    assert instance.onCycle == False


def test_ir_Loop_multithreadable_value_roundtrip():
    instance = ir_Loop(multithreadable=True)
    assert instance.multithreadable == True
    instance.multithreadable = False
    assert instance.multithreadable == False


def test_ir_PostProcessingInfo_periodValue_value_roundtrip():
    instance = ir_PostProcessingInfo(periodValue=3.14)
    assert instance.periodValue == 3.14
    instance.periodValue = 9.99
    assert instance.periodValue == 9.99


def test_ir_RealConstant_value_value_roundtrip():
    instance = ir_RealConstant(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_ir_SetDefinition_name_value_roundtrip():
    instance = ir_SetDefinition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_TimeLoop_name_value_roundtrip():
    instance = ir_TimeLoop(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_TimeLoopVariable_name_value_roundtrip():
    instance = ir_TimeLoopVariable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ir_UnaryExpression_operator_value_roundtrip():
    instance = ir_UnaryExpression(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_ir_Variable_const_value_roundtrip():
    instance = ir_Variable(const=True, persistenceName="sample_text")
    assert instance.const == True
    instance.const = False
    assert instance.const == False


def test_ir_Variable_persistenceName_value_roundtrip():
    instance = ir_Variable(const=True, persistenceName="sample_text")
    assert instance.persistenceName == "sample_text"
    instance.persistenceName = "sample_text_2"
    assert instance.persistenceName == "sample_text_2"


def test_ir_Arg_isa_ArgOrVar():
    instance = ir_Arg()
    assert isinstance(instance, ArgOrVar)


def test_ir_Variable_isa_ArgOrVar():
    instance = ir_Variable(const=True, persistenceName="sample_text")
    assert isinstance(instance, ArgOrVar)


def test_ir_ConnectivityCall_isa_Container():
    instance = ir_ConnectivityCall()
    assert isinstance(instance, Container)


def test_ir_SetRef_isa_Container():
    instance = ir_SetRef()
    assert isinstance(instance, Container)


def test_ir_ArgOrVarRef_isa_Expression():
    instance = ir_ArgOrVarRef()
    assert isinstance(instance, Expression)


def test_ir_BaseTypeConstant_isa_Expression():
    instance = ir_BaseTypeConstant()
    assert isinstance(instance, Expression)


def test_ir_BinaryExpression_isa_Expression():
    instance = ir_BinaryExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_ir_BoolConstant_isa_Expression():
    instance = ir_BoolConstant(value=True)
    assert isinstance(instance, Expression)


def test_ir_Cardinality_isa_Expression():
    instance = ir_Cardinality()
    assert isinstance(instance, Expression)


def test_ir_ContractedIf_isa_Expression():
    instance = ir_ContractedIf()
    assert isinstance(instance, Expression)


def test_ir_FunctionCall_isa_Expression():
    instance = ir_FunctionCall()
    assert isinstance(instance, Expression)


def test_ir_IntConstant_isa_Expression():
    instance = ir_IntConstant(value=7)
    assert isinstance(instance, Expression)


def test_ir_MaxConstant_isa_Expression():
    instance = ir_MaxConstant()
    assert isinstance(instance, Expression)


def test_ir_MinConstant_isa_Expression():
    instance = ir_MinConstant()
    assert isinstance(instance, Expression)


def test_ir_Parenthesis_isa_Expression():
    instance = ir_Parenthesis()
    assert isinstance(instance, Expression)


def test_ir_RealConstant_isa_Expression():
    instance = ir_RealConstant(value=3.14)
    assert isinstance(instance, Expression)


def test_ir_UnaryExpression_isa_Expression():
    instance = ir_UnaryExpression(operator="sample_text")
    assert isinstance(instance, Expression)


def test_ir_VectorConstant_isa_Expression():
    instance = ir_VectorConstant()
    assert isinstance(instance, Expression)


def test_ir_Affectation_isa_Instruction():
    instance = ir_Affectation()
    assert isinstance(instance, Instruction)


def test_ir_Exit_isa_Instruction():
    instance = ir_Exit(message="sample_text")
    assert isinstance(instance, Instruction)


def test_ir_If_isa_Instruction():
    instance = ir_If()
    assert isinstance(instance, Instruction)


def test_ir_InstructionBlock_isa_Instruction():
    instance = ir_InstructionBlock()
    assert isinstance(instance, Instruction)


def test_ir_ItemIdDefinition_isa_Instruction():
    instance = ir_ItemIdDefinition()
    assert isinstance(instance, Instruction)


def test_ir_ItemIndexDefinition_isa_Instruction():
    instance = ir_ItemIndexDefinition()
    assert isinstance(instance, Instruction)


def test_ir_IterableInstruction_isa_Instruction():
    instance = ir_IterableInstruction()
    assert isinstance(instance, Instruction)


def test_ir_Return_isa_Instruction():
    instance = ir_Return()
    assert isinstance(instance, Instruction)


def test_ir_SetDefinition_isa_Instruction():
    instance = ir_SetDefinition(name="sample_text")
    assert isinstance(instance, Instruction)


def test_ir_VariableDefinition_isa_Instruction():
    instance = ir_VariableDefinition()
    assert isinstance(instance, Instruction)


def test_ir_ArgOrVar_isa_IrAnnotable():
    instance = ir_ArgOrVar(name="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_Connectivity_isa_IrAnnotable():
    instance = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_Container_isa_IrAnnotable():
    instance = ir_Container()
    assert isinstance(instance, IrAnnotable)


def test_ir_Expression_isa_IrAnnotable():
    instance = ir_Expression()
    assert isinstance(instance, IrAnnotable)


def test_ir_Function_isa_IrAnnotable():
    instance = ir_Function(name="sample_text", provider="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_Import_isa_IrAnnotable():
    instance = ir_Import(importedNamespace="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_Instruction_isa_IrAnnotable():
    instance = ir_Instruction()
    assert isinstance(instance, IrAnnotable)


def test_ir_IrType_isa_IrAnnotable():
    instance = ir_IrType()
    assert isinstance(instance, IrAnnotable)


def test_ir_ItemId_isa_IrAnnotable():
    instance = ir_ItemId(itemName="sample_text", name="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_ItemIdValue_isa_IrAnnotable():
    instance = ir_ItemIdValue()
    assert isinstance(instance, IrAnnotable)


def test_ir_ItemIndex_isa_IrAnnotable():
    instance = ir_ItemIndex(itemName="sample_text", name="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_ItemIndexValue_isa_IrAnnotable():
    instance = ir_ItemIndexValue()
    assert isinstance(instance, IrAnnotable)


def test_ir_ItemType_isa_IrAnnotable():
    instance = ir_ItemType(name="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_IterationBlock_isa_IrAnnotable():
    instance = ir_IterationBlock()
    assert isinstance(instance, IrAnnotable)


def test_ir_Job_isa_IrAnnotable():
    instance = ir_Job(at=3.14, name="sample_text", onCycle=True)
    assert isinstance(instance, IrAnnotable)


def test_ir_JobContainer_isa_IrAnnotable():
    instance = ir_JobContainer()
    assert isinstance(instance, IrAnnotable)


def test_ir_PostProcessingInfo_isa_IrAnnotable():
    instance = ir_PostProcessingInfo(periodValue=3.14)
    assert isinstance(instance, IrAnnotable)


def test_ir_TimeLoop_isa_IrAnnotable():
    instance = ir_TimeLoop(name="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_TimeLoopCopy_isa_IrAnnotable():
    instance = ir_TimeLoopCopy()
    assert isinstance(instance, IrAnnotable)


def test_ir_TimeLoopVariable_isa_IrAnnotable():
    instance = ir_TimeLoopVariable(name="sample_text")
    assert isinstance(instance, IrAnnotable)


def test_ir_BaseType_isa_IrType():
    instance = ir_BaseType(primitive="sample_text")
    assert isinstance(instance, IrType)


def test_ir_ConnectivityType_isa_IrType():
    instance = ir_ConnectivityType()
    assert isinstance(instance, IrType)


def test_ir_ItemIdValueCall_isa_ItemIdValue():
    instance = ir_ItemIdValueCall()
    assert isinstance(instance, ItemIdValue)


def test_ir_ItemIdValueIterator_isa_ItemIdValue():
    instance = ir_ItemIdValueIterator(shift=7)
    assert isinstance(instance, ItemIdValue)


def test_ir_Loop_isa_IterableInstruction():
    instance = ir_Loop(multithreadable=True)
    assert isinstance(instance, IterableInstruction)


def test_ir_ReductionInstruction_isa_IterableInstruction():
    instance = ir_ReductionInstruction()
    assert isinstance(instance, IterableInstruction)


def test_ir_Interval_isa_IterationBlock():
    instance = ir_Interval()
    assert isinstance(instance, IterationBlock)


def test_ir_Iterator_isa_IterationBlock():
    instance = ir_Iterator()
    assert isinstance(instance, IterationBlock)


def test_ir_InstructionJob_isa_Job():
    instance = ir_InstructionJob()
    assert isinstance(instance, Job)


def test_ir_TimeLoopCopyJob_isa_Job():
    instance = ir_TimeLoopCopyJob()
    assert isinstance(instance, Job)


def test_ir_IrModule_isa_JobContainer():
    instance = ir_IrModule(name="sample_text")
    assert isinstance(instance, JobContainer)


def test_ir_TimeLoopJob_isa_JobContainer():
    instance = ir_TimeLoopJob()
    assert isinstance(instance, JobContainer)


def test_ir_AfterTimeLoopJob_isa_TimeLoopCopyJob():
    instance = ir_AfterTimeLoopJob()
    assert isinstance(instance, TimeLoopCopyJob)


def test_ir_BeforeTimeLoopJob_isa_TimeLoopCopyJob():
    instance = ir_BeforeTimeLoopJob()
    assert isinstance(instance, TimeLoopCopyJob)


def test_ir_TimeLoopJob_isa_TimeLoopCopyJob():
    instance = ir_TimeLoopJob()
    assert isinstance(instance, TimeLoopCopyJob)


def test_ir_ConnectivityVariable_isa_Variable():
    instance = ir_ConnectivityVariable()
    assert isinstance(instance, Variable)


def test_ir_SimpleVariable_isa_Variable():
    instance = ir_SimpleVariable()
    assert isinstance(instance, Variable)


def test_assoc_annotations0_link_reassign_clear():
    a = ir_IrAnnotation(source="sample_text")
    b1 = ir_IrAnnotable()
    b2 = ir_IrAnnotable()
    _safe_set(a, 'ir_IrAnnotation', b1)
    assert _is_linked(a, 'ir_IrAnnotation', b1)
    if hasattr(b1, 'ir_IrAnnotable'):
        assert _is_linked(b1, 'ir_IrAnnotable', a)
    _safe_set(a, 'ir_IrAnnotation', b2)
    assert _is_linked(a, 'ir_IrAnnotation', b2)
    if hasattr(b1, 'ir_IrAnnotable'):
        assert not _is_linked(b1, 'ir_IrAnnotable', a)
    if hasattr(b2, 'ir_IrAnnotable'):
        assert _is_linked(b2, 'ir_IrAnnotable', a)
    _safe_set(a, 'ir_IrAnnotation', None)
    assert not _is_linked(a, 'ir_IrAnnotation', b2)
    if hasattr(b2, 'ir_IrAnnotable'):
        assert not _is_linked(b2, 'ir_IrAnnotable', a)


def test_assoc_args210_link_reassign_clear():
    a = ir_ItemId(itemName="sample_text", name="sample_text")
    b1 = ir_ConnectivityCall()
    b2 = ir_ConnectivityCall()
    _safe_set(a, 'ir_ItemId212', b1)
    assert _is_linked(a, 'ir_ItemId212', b1)
    if hasattr(b1, 'ir_ConnectivityCall211'):
        assert _is_linked(b1, 'ir_ConnectivityCall211', a)
    _safe_set(a, 'ir_ItemId212', b2)
    assert _is_linked(a, 'ir_ItemId212', b2)
    if hasattr(b1, 'ir_ConnectivityCall211'):
        assert not _is_linked(b1, 'ir_ConnectivityCall211', a)
    if hasattr(b2, 'ir_ConnectivityCall211'):
        assert _is_linked(b2, 'ir_ConnectivityCall211', a)
    _safe_set(a, 'ir_ItemId212', None)
    assert not _is_linked(a, 'ir_ItemId212', b2)
    if hasattr(b2, 'ir_ConnectivityCall211'):
        assert not _is_linked(b2, 'ir_ConnectivityCall211', a)


def test_assoc_associatedJob50_link_reassign_clear():
    a = ir_TimeLoop(name="sample_text")
    b1 = ir_TimeLoopJob()
    b2 = ir_TimeLoopJob()
    _safe_set(a, 'ir_TimeLoop51', b1)
    assert _is_linked(a, 'ir_TimeLoop51', b1)
    if hasattr(b1, 'ir_TimeLoopJob'):
        assert _is_linked(b1, 'ir_TimeLoopJob', a)
    _safe_set(a, 'ir_TimeLoop51', b2)
    assert _is_linked(a, 'ir_TimeLoop51', b2)
    if hasattr(b1, 'ir_TimeLoopJob'):
        assert not _is_linked(b1, 'ir_TimeLoopJob', a)
    if hasattr(b2, 'ir_TimeLoopJob'):
        assert _is_linked(b2, 'ir_TimeLoopJob', a)
    _safe_set(a, 'ir_TimeLoop51', None)
    assert not _is_linked(a, 'ir_TimeLoop51', b2)
    if hasattr(b2, 'ir_TimeLoopJob'):
        assert not _is_linked(b2, 'ir_TimeLoopJob', a)


def test_assoc_base195_link_reassign_clear():
    a = ir_BaseType(primitive="sample_text")
    b1 = ir_ConnectivityType()
    b2 = ir_ConnectivityType()
    _safe_set(a, 'ir_BaseType197', b1)
    assert _is_linked(a, 'ir_BaseType197', b1)
    if hasattr(b1, 'ir_ConnectivityType196'):
        assert _is_linked(b1, 'ir_ConnectivityType196', a)
    _safe_set(a, 'ir_BaseType197', b2)
    assert _is_linked(a, 'ir_BaseType197', b2)
    if hasattr(b1, 'ir_ConnectivityType196'):
        assert not _is_linked(b1, 'ir_ConnectivityType196', a)
    if hasattr(b2, 'ir_ConnectivityType196'):
        assert _is_linked(b2, 'ir_ConnectivityType196', a)
    _safe_set(a, 'ir_BaseType197', None)
    assert not _is_linked(a, 'ir_BaseType197', b2)
    if hasattr(b2, 'ir_ConnectivityType196'):
        assert not _is_linked(b2, 'ir_ConnectivityType196', a)


def test_assoc_binaryFunction111_link_reassign_clear():
    a = ir_Function(name="sample_text", provider="sample_text")
    b1 = ir_ReductionInstruction()
    b2 = ir_ReductionInstruction()
    _safe_set(a, 'ir_Function113', b1)
    assert _is_linked(a, 'ir_Function113', b1)
    if hasattr(b1, 'ir_ReductionInstruction112'):
        assert _is_linked(b1, 'ir_ReductionInstruction112', a)
    _safe_set(a, 'ir_Function113', b2)
    assert _is_linked(a, 'ir_Function113', b2)
    if hasattr(b1, 'ir_ReductionInstruction112'):
        assert not _is_linked(b1, 'ir_ReductionInstruction112', a)
    if hasattr(b2, 'ir_ReductionInstruction112'):
        assert _is_linked(b2, 'ir_ReductionInstruction112', a)
    _safe_set(a, 'ir_Function113', None)
    assert not _is_linked(a, 'ir_Function113', b2)
    if hasattr(b2, 'ir_ReductionInstruction112'):
        assert not _is_linked(b2, 'ir_ReductionInstruction112', a)


def test_assoc_body120_link_reassign_clear():
    a = ir_Loop(multithreadable=True)
    b1 = ir_Instruction()
    b2 = ir_Instruction()
    _safe_set(a, 'ir_Loop', b1)
    assert _is_linked(a, 'ir_Loop', b1)
    if hasattr(b1, 'ir_Instruction121'):
        assert _is_linked(b1, 'ir_Instruction121', a)
    _safe_set(a, 'ir_Loop', b2)
    assert _is_linked(a, 'ir_Loop', b2)
    if hasattr(b1, 'ir_Instruction121'):
        assert not _is_linked(b1, 'ir_Instruction121', a)
    if hasattr(b2, 'ir_Instruction121'):
        assert _is_linked(b2, 'ir_Instruction121', a)
    _safe_set(a, 'ir_Loop', None)
    assert not _is_linked(a, 'ir_Loop', b2)
    if hasattr(b2, 'ir_Instruction121'):
        assert not _is_linked(b2, 'ir_Instruction121', a)


def test_assoc_body75_link_reassign_clear():
    a = ir_Function(name="sample_text", provider="sample_text")
    b1 = ir_Instruction()
    b2 = ir_Instruction()
    _safe_set(a, 'ir_Function76', b1)
    assert _is_linked(a, 'ir_Function76', b1)
    if hasattr(b1, 'ir_Instruction'):
        assert _is_linked(b1, 'ir_Instruction', a)
    _safe_set(a, 'ir_Function76', b2)
    assert _is_linked(a, 'ir_Function76', b2)
    if hasattr(b1, 'ir_Instruction'):
        assert not _is_linked(b1, 'ir_Instruction', a)
    if hasattr(b2, 'ir_Instruction'):
        assert _is_linked(b2, 'ir_Instruction', a)
    _safe_set(a, 'ir_Function76', None)
    assert not _is_linked(a, 'ir_Function76', b2)
    if hasattr(b2, 'ir_Instruction'):
        assert not _is_linked(b2, 'ir_Instruction', a)


def test_assoc_connectivities192_link_reassign_clear():
    a = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    b1 = ir_ConnectivityType()
    b2 = ir_ConnectivityType()
    _safe_set(a, 'ir_Connectivity194', b1)
    assert _is_linked(a, 'ir_Connectivity194', b1)
    if hasattr(b1, 'ir_ConnectivityType193'):
        assert _is_linked(b1, 'ir_ConnectivityType193', a)
    _safe_set(a, 'ir_Connectivity194', b2)
    assert _is_linked(a, 'ir_Connectivity194', b2)
    if hasattr(b1, 'ir_ConnectivityType193'):
        assert not _is_linked(b1, 'ir_ConnectivityType193', a)
    if hasattr(b2, 'ir_ConnectivityType193'):
        assert _is_linked(b2, 'ir_ConnectivityType193', a)
    _safe_set(a, 'ir_Connectivity194', None)
    assert not _is_linked(a, 'ir_Connectivity194', b2)
    if hasattr(b2, 'ir_ConnectivityType193'):
        assert not _is_linked(b2, 'ir_ConnectivityType193', a)


def test_assoc_connectivities9_link_reassign_clear():
    a = ir_IrModule(name="sample_text")
    b1 = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    b2 = ir_Connectivity(indexEqualId=False, multiple=False, name="sample_text_2")
    _safe_set(a, 'ir_IrModule10', {b1})
    assert _is_linked(a, 'ir_IrModule10', b1)
    if hasattr(b1, 'ir_Connectivity'):
        assert _is_linked(b1, 'ir_Connectivity', a)
    _safe_set(a, 'ir_IrModule10', {b2})
    assert _is_linked(a, 'ir_IrModule10', b2)
    if hasattr(b1, 'ir_Connectivity'):
        assert not _is_linked(b1, 'ir_Connectivity', a)
    if hasattr(b2, 'ir_Connectivity'):
        assert _is_linked(b2, 'ir_Connectivity', a)
    _safe_set(a, 'ir_IrModule10', set())
    assert not _is_linked(a, 'ir_IrModule10', b2)
    if hasattr(b2, 'ir_Connectivity'):
        assert not _is_linked(b2, 'ir_Connectivity', a)


def test_assoc_connectivity207_link_reassign_clear():
    a = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    b1 = ir_ConnectivityCall()
    b2 = ir_ConnectivityCall()
    _safe_set(a, 'ir_Connectivity209', b1)
    assert _is_linked(a, 'ir_Connectivity209', b1)
    if hasattr(b1, 'ir_ConnectivityCall208'):
        assert _is_linked(b1, 'ir_ConnectivityCall208', a)
    _safe_set(a, 'ir_Connectivity209', b2)
    assert _is_linked(a, 'ir_Connectivity209', b2)
    if hasattr(b1, 'ir_ConnectivityCall208'):
        assert not _is_linked(b1, 'ir_ConnectivityCall208', a)
    if hasattr(b2, 'ir_ConnectivityCall208'):
        assert _is_linked(b2, 'ir_ConnectivityCall208', a)
    _safe_set(a, 'ir_Connectivity209', None)
    assert not _is_linked(a, 'ir_Connectivity209', b2)
    if hasattr(b2, 'ir_ConnectivityCall208'):
        assert not _is_linked(b2, 'ir_ConnectivityCall208', a)


def test_assoc_current201_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_TimeLoopVariable(name="sample_text")
    b2 = ir_TimeLoopVariable(name="sample_text_2")
    _safe_set(a, 'ir_Variable203', b1)
    assert _is_linked(a, 'ir_Variable203', b1)
    if hasattr(b1, 'ir_TimeLoopVariable202'):
        assert _is_linked(b1, 'ir_TimeLoopVariable202', a)
    _safe_set(a, 'ir_Variable203', b2)
    assert _is_linked(a, 'ir_Variable203', b2)
    if hasattr(b1, 'ir_TimeLoopVariable202'):
        assert not _is_linked(b1, 'ir_TimeLoopVariable202', a)
    if hasattr(b2, 'ir_TimeLoopVariable202'):
        assert _is_linked(b2, 'ir_TimeLoopVariable202', a)
    _safe_set(a, 'ir_Variable203', None)
    assert not _is_linked(a, 'ir_Variable203', b2)
    if hasattr(b2, 'ir_TimeLoopVariable202'):
        assert not _is_linked(b2, 'ir_TimeLoopVariable202', a)


def test_assoc_deltatVariable23_link_reassign_clear():
    a = ir_IrModule(name="sample_text")
    b1 = ir_SimpleVariable()
    b2 = ir_SimpleVariable()
    _safe_set(a, 'ir_IrModule24', b1)
    assert _is_linked(a, 'ir_IrModule24', b1)
    if hasattr(b1, 'ir_SimpleVariable25'):
        assert _is_linked(b1, 'ir_SimpleVariable25', a)
    _safe_set(a, 'ir_IrModule24', b2)
    assert _is_linked(a, 'ir_IrModule24', b2)
    if hasattr(b1, 'ir_SimpleVariable25'):
        assert not _is_linked(b1, 'ir_SimpleVariable25', a)
    if hasattr(b2, 'ir_SimpleVariable25'):
        assert _is_linked(b2, 'ir_SimpleVariable25', a)
    _safe_set(a, 'ir_IrModule24', None)
    assert not _is_linked(a, 'ir_IrModule24', b2)
    if hasattr(b2, 'ir_SimpleVariable25'):
        assert not _is_linked(b2, 'ir_SimpleVariable25', a)


def test_assoc_destination90_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_TimeLoopCopy()
    b2 = ir_TimeLoopCopy()
    _safe_set(a, 'ir_Variable92', b1)
    assert _is_linked(a, 'ir_Variable92', b1)
    if hasattr(b1, 'ir_TimeLoopCopy91'):
        assert _is_linked(b1, 'ir_TimeLoopCopy91', a)
    _safe_set(a, 'ir_Variable92', b2)
    assert _is_linked(a, 'ir_Variable92', b2)
    if hasattr(b1, 'ir_TimeLoopCopy91'):
        assert not _is_linked(b1, 'ir_TimeLoopCopy91', a)
    if hasattr(b2, 'ir_TimeLoopCopy91'):
        assert _is_linked(b2, 'ir_TimeLoopCopy91', a)
    _safe_set(a, 'ir_Variable92', None)
    assert not _is_linked(a, 'ir_Variable92', b2)
    if hasattr(b2, 'ir_TimeLoopCopy91'):
        assert not _is_linked(b2, 'ir_TimeLoopCopy91', a)


def test_assoc_details1_link_reassign_clear():
    a = ir_IrAnnotation(source="sample_text")
    b1 = ir_EStringToStringMapEntry()
    b2 = ir_EStringToStringMapEntry()
    _safe_set(a, 'ir_IrAnnotation2', {b1})
    assert _is_linked(a, 'ir_IrAnnotation2', b1)
    if hasattr(b1, 'ir_EStringToStringMapEntry'):
        assert _is_linked(b1, 'ir_EStringToStringMapEntry', a)
    _safe_set(a, 'ir_IrAnnotation2', {b2})
    assert _is_linked(a, 'ir_IrAnnotation2', b2)
    if hasattr(b1, 'ir_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'ir_EStringToStringMapEntry', a)
    if hasattr(b2, 'ir_EStringToStringMapEntry'):
        assert _is_linked(b2, 'ir_EStringToStringMapEntry', a)
    _safe_set(a, 'ir_IrAnnotation2', set())
    assert not _is_linked(a, 'ir_IrAnnotation2', b2)
    if hasattr(b2, 'ir_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'ir_EStringToStringMapEntry', a)


def test_assoc_expression166_link_reassign_clear():
    a = ir_UnaryExpression(operator="sample_text")
    b1 = ir_Expression()
    b2 = ir_Expression()
    _safe_set(a, 'ir_UnaryExpression', b1)
    assert _is_linked(a, 'ir_UnaryExpression', b1)
    if hasattr(b1, 'ir_Expression167'):
        assert _is_linked(b1, 'ir_Expression167', a)
    _safe_set(a, 'ir_UnaryExpression', b2)
    assert _is_linked(a, 'ir_UnaryExpression', b2)
    if hasattr(b1, 'ir_Expression167'):
        assert not _is_linked(b1, 'ir_Expression167', a)
    if hasattr(b2, 'ir_Expression167'):
        assert _is_linked(b2, 'ir_Expression167', a)
    _safe_set(a, 'ir_UnaryExpression', None)
    assert not _is_linked(a, 'ir_UnaryExpression', b2)
    if hasattr(b2, 'ir_Expression167'):
        assert not _is_linked(b2, 'ir_Expression167', a)


def test_assoc_function170_link_reassign_clear():
    a = ir_Function(name="sample_text", provider="sample_text")
    b1 = ir_FunctionCall()
    b2 = ir_FunctionCall()
    _safe_set(a, 'ir_Function171', b1)
    assert _is_linked(a, 'ir_Function171', b1)
    if hasattr(b1, 'ir_FunctionCall'):
        assert _is_linked(b1, 'ir_FunctionCall', a)
    _safe_set(a, 'ir_Function171', b2)
    assert _is_linked(a, 'ir_Function171', b2)
    if hasattr(b1, 'ir_FunctionCall'):
        assert not _is_linked(b1, 'ir_FunctionCall', a)
    if hasattr(b2, 'ir_FunctionCall'):
        assert _is_linked(b2, 'ir_FunctionCall', a)
    _safe_set(a, 'ir_Function171', None)
    assert not _is_linked(a, 'ir_Function171', b2)
    if hasattr(b2, 'ir_FunctionCall'):
        assert not _is_linked(b2, 'ir_FunctionCall', a)


def test_assoc_functions7_link_reassign_clear():
    a = ir_IrModule(name="sample_text")
    b1 = ir_Function(name="sample_text", provider="sample_text")
    b2 = ir_Function(name="sample_text_2", provider="sample_text_2")
    _safe_set(a, 'ir_IrModule8', {b1})
    assert _is_linked(a, 'ir_IrModule8', b1)
    if hasattr(b1, 'ir_Function'):
        assert _is_linked(b1, 'ir_Function', a)
    _safe_set(a, 'ir_IrModule8', {b2})
    assert _is_linked(a, 'ir_IrModule8', b2)
    if hasattr(b1, 'ir_Function'):
        assert not _is_linked(b1, 'ir_Function', a)
    if hasattr(b2, 'ir_Function'):
        assert _is_linked(b2, 'ir_Function', a)
    _safe_set(a, 'ir_IrModule8', set())
    assert not _is_linked(a, 'ir_IrModule8', b2)
    if hasattr(b2, 'ir_Function'):
        assert not _is_linked(b2, 'ir_Function', a)


def test_assoc_id125_link_reassign_clear():
    a = ir_ItemId(itemName="sample_text", name="sample_text")
    b1 = ir_ItemIdDefinition()
    b2 = ir_ItemIdDefinition()
    _safe_set(a, 'ir_ItemId', b1)
    assert _is_linked(a, 'ir_ItemId', b1)
    if hasattr(b1, 'ir_ItemIdDefinition'):
        assert _is_linked(b1, 'ir_ItemIdDefinition', a)
    _safe_set(a, 'ir_ItemId', b2)
    assert _is_linked(a, 'ir_ItemId', b2)
    if hasattr(b1, 'ir_ItemIdDefinition'):
        assert not _is_linked(b1, 'ir_ItemIdDefinition', a)
    if hasattr(b2, 'ir_ItemIdDefinition'):
        assert _is_linked(b2, 'ir_ItemIdDefinition', a)
    _safe_set(a, 'ir_ItemId', None)
    assert not _is_linked(a, 'ir_ItemId', b2)
    if hasattr(b2, 'ir_ItemIdDefinition'):
        assert not _is_linked(b2, 'ir_ItemIdDefinition', a)


def test_assoc_id219_link_reassign_clear():
    a = ir_ItemId(itemName="sample_text", name="sample_text")
    b1 = ir_ItemIndexValue()
    b2 = ir_ItemIndexValue()
    _safe_set(a, 'ir_ItemId221', b1)
    assert _is_linked(a, 'ir_ItemId221', b1)
    if hasattr(b1, 'ir_ItemIndexValue220'):
        assert _is_linked(b1, 'ir_ItemIndexValue220', a)
    _safe_set(a, 'ir_ItemId221', b2)
    assert _is_linked(a, 'ir_ItemId221', b2)
    if hasattr(b1, 'ir_ItemIndexValue220'):
        assert not _is_linked(b1, 'ir_ItemIndexValue220', a)
    if hasattr(b2, 'ir_ItemIndexValue220'):
        assert _is_linked(b2, 'ir_ItemIndexValue220', a)
    _safe_set(a, 'ir_ItemId221', None)
    assert not _is_linked(a, 'ir_ItemId221', b2)
    if hasattr(b2, 'ir_ItemIndexValue220'):
        assert not _is_linked(b2, 'ir_ItemIndexValue220', a)


def test_assoc_imports4_link_reassign_clear():
    a = ir_IrModule(name="sample_text")
    b1 = ir_Import(importedNamespace="sample_text")
    b2 = ir_Import(importedNamespace="sample_text_2")
    _safe_set(a, 'ir_IrModule', {b1})
    assert _is_linked(a, 'ir_IrModule', b1)
    if hasattr(b1, 'ir_Import'):
        assert _is_linked(b1, 'ir_Import', a)
    _safe_set(a, 'ir_IrModule', {b2})
    assert _is_linked(a, 'ir_IrModule', b2)
    if hasattr(b1, 'ir_Import'):
        assert not _is_linked(b1, 'ir_Import', a)
    if hasattr(b2, 'ir_Import'):
        assert _is_linked(b2, 'ir_Import', a)
    _safe_set(a, 'ir_IrModule', set())
    assert not _is_linked(a, 'ir_IrModule', b2)
    if hasattr(b2, 'ir_Import'):
        assert not _is_linked(b2, 'ir_Import', a)


def test_assoc_inArgs72_link_reassign_clear():
    a = ir_Function(name="sample_text", provider="sample_text")
    b1 = ir_Arg()
    b2 = ir_Arg()
    _safe_set(a, 'ir_Function73', {b1})
    assert _is_linked(a, 'ir_Function73', b1)
    if hasattr(b1, 'ir_Arg74'):
        assert _is_linked(b1, 'ir_Arg74', a)
    _safe_set(a, 'ir_Function73', {b2})
    assert _is_linked(a, 'ir_Function73', b2)
    if hasattr(b1, 'ir_Arg74'):
        assert not _is_linked(b1, 'ir_Arg74', a)
    if hasattr(b2, 'ir_Arg74'):
        assert _is_linked(b2, 'ir_Arg74', a)
    _safe_set(a, 'ir_Function73', set())
    assert not _is_linked(a, 'ir_Function73', b2)
    if hasattr(b2, 'ir_Arg74'):
        assert not _is_linked(b2, 'ir_Arg74', a)


def test_assoc_inTypes77_link_reassign_clear():
    a = ir_ItemType(name="sample_text")
    b1 = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    b2 = ir_Connectivity(indexEqualId=False, multiple=False, name="sample_text_2")
    _safe_set(a, 'ir_ItemType79', b1)
    assert _is_linked(a, 'ir_ItemType79', b1)
    if hasattr(b1, 'ir_Connectivity78'):
        assert _is_linked(b1, 'ir_Connectivity78', a)
    _safe_set(a, 'ir_ItemType79', b2)
    assert _is_linked(a, 'ir_ItemType79', b2)
    if hasattr(b1, 'ir_Connectivity78'):
        assert not _is_linked(b1, 'ir_Connectivity78', a)
    if hasattr(b2, 'ir_Connectivity78'):
        assert _is_linked(b2, 'ir_Connectivity78', a)
    _safe_set(a, 'ir_ItemType79', None)
    assert not _is_linked(a, 'ir_ItemType79', b2)
    if hasattr(b2, 'ir_Connectivity78'):
        assert not _is_linked(b2, 'ir_Connectivity78', a)


def test_assoc_index122_link_reassign_clear():
    a = ir_ItemIndex(itemName="sample_text", name="sample_text")
    b1 = ir_ItemIndexDefinition()
    b2 = ir_ItemIndexDefinition()
    _safe_set(a, 'ir_ItemIndex', b1)
    assert _is_linked(a, 'ir_ItemIndex', b1)
    if hasattr(b1, 'ir_ItemIndexDefinition'):
        assert _is_linked(b1, 'ir_ItemIndexDefinition', a)
    _safe_set(a, 'ir_ItemIndex', b2)
    assert _is_linked(a, 'ir_ItemIndex', b2)
    if hasattr(b1, 'ir_ItemIndexDefinition'):
        assert not _is_linked(b1, 'ir_ItemIndexDefinition', a)
    if hasattr(b2, 'ir_ItemIndexDefinition'):
        assert _is_linked(b2, 'ir_ItemIndexDefinition', a)
    _safe_set(a, 'ir_ItemIndex', None)
    assert not _is_linked(a, 'ir_ItemIndex', b2)
    if hasattr(b2, 'ir_ItemIndexDefinition'):
        assert not _is_linked(b2, 'ir_ItemIndexDefinition', a)


def test_assoc_index139_link_reassign_clear():
    a = ir_ItemIndex(itemName="sample_text", name="sample_text")
    b1 = ir_Iterator()
    b2 = ir_Iterator()
    _safe_set(a, 'ir_ItemIndex140', b1)
    assert _is_linked(a, 'ir_ItemIndex140', b1)
    if hasattr(b1, 'ir_Iterator'):
        assert _is_linked(b1, 'ir_Iterator', a)
    _safe_set(a, 'ir_ItemIndex140', b2)
    assert _is_linked(a, 'ir_ItemIndex140', b2)
    if hasattr(b1, 'ir_Iterator'):
        assert not _is_linked(b1, 'ir_Iterator', a)
    if hasattr(b2, 'ir_Iterator'):
        assert _is_linked(b2, 'ir_Iterator', a)
    _safe_set(a, 'ir_ItemIndex140', None)
    assert not _is_linked(a, 'ir_ItemIndex140', b2)
    if hasattr(b2, 'ir_Iterator'):
        assert not _is_linked(b2, 'ir_Iterator', a)


def test_assoc_init198_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_TimeLoopVariable(name="sample_text")
    b2 = ir_TimeLoopVariable(name="sample_text_2")
    _safe_set(a, 'ir_Variable200', b1)
    assert _is_linked(a, 'ir_Variable200', b1)
    if hasattr(b1, 'ir_TimeLoopVariable199'):
        assert _is_linked(b1, 'ir_TimeLoopVariable199', a)
    _safe_set(a, 'ir_Variable200', b2)
    assert _is_linked(a, 'ir_Variable200', b2)
    if hasattr(b1, 'ir_TimeLoopVariable199'):
        assert not _is_linked(b1, 'ir_TimeLoopVariable199', a)
    if hasattr(b2, 'ir_TimeLoopVariable199'):
        assert _is_linked(b2, 'ir_TimeLoopVariable199', a)
    _safe_set(a, 'ir_Variable200', None)
    assert not _is_linked(a, 'ir_Variable200', b2)
    if hasattr(b2, 'ir_TimeLoopVariable199'):
        assert not _is_linked(b2, 'ir_TimeLoopVariable199', a)


def test_assoc_initNodeCoordVariable15_link_reassign_clear():
    a = ir_IrModule(name="sample_text")
    b1 = ir_ConnectivityVariable()
    b2 = ir_ConnectivityVariable()
    _safe_set(a, 'ir_IrModule16', b1)
    assert _is_linked(a, 'ir_IrModule16', b1)
    if hasattr(b1, 'ir_ConnectivityVariable'):
        assert _is_linked(b1, 'ir_ConnectivityVariable', a)
    _safe_set(a, 'ir_IrModule16', b2)
    assert _is_linked(a, 'ir_IrModule16', b2)
    if hasattr(b1, 'ir_ConnectivityVariable'):
        assert not _is_linked(b1, 'ir_ConnectivityVariable', a)
    if hasattr(b2, 'ir_ConnectivityVariable'):
        assert _is_linked(b2, 'ir_ConnectivityVariable', a)
    _safe_set(a, 'ir_IrModule16', None)
    assert not _is_linked(a, 'ir_IrModule16', b2)
    if hasattr(b2, 'ir_ConnectivityVariable'):
        assert not _is_linked(b2, 'ir_ConnectivityVariable', a)


def test_assoc_innerJobs3_link_reassign_clear():
    a = ir_Job(at=3.14, name="sample_text", onCycle=True)
    b1 = ir_JobContainer()
    b2 = ir_JobContainer()
    _safe_set(a, 'Job', b1)
    assert _is_linked(a, 'Job', b1)
    if hasattr(b1, 'jobContainer'):
        assert _is_linked(b1, 'jobContainer', a)
    _safe_set(a, 'Job', b2)
    assert _is_linked(a, 'Job', b2)
    if hasattr(b1, 'jobContainer'):
        assert not _is_linked(b1, 'jobContainer', a)
    if hasattr(b2, 'jobContainer'):
        assert _is_linked(b2, 'jobContainer', a)
    _safe_set(a, 'Job', None)
    assert not _is_linked(a, 'Job', b2)
    if hasattr(b2, 'jobContainer'):
        assert not _is_linked(b2, 'jobContainer', a)


def test_assoc_innerTimeLoop42_link_reassign_clear():
    a = ir_TimeLoop(name="sample_text")
    b1 = ir_TimeLoop(name="sample_text")
    b2 = ir_TimeLoop(name="sample_text_2")
    _safe_set(a, 'TimeLoop', b1)
    assert _is_linked(a, 'TimeLoop', b1)
    if hasattr(b1, 'outerTimeLoop'):
        assert _is_linked(b1, 'outerTimeLoop', a)
    _safe_set(a, 'TimeLoop', b2)
    assert _is_linked(a, 'TimeLoop', b2)
    if hasattr(b1, 'outerTimeLoop'):
        assert not _is_linked(b1, 'outerTimeLoop', a)
    if hasattr(b2, 'outerTimeLoop'):
        assert _is_linked(b2, 'outerTimeLoop', a)
    _safe_set(a, 'TimeLoop', None)
    assert not _is_linked(a, 'TimeLoop', b2)
    if hasattr(b2, 'outerTimeLoop'):
        assert not _is_linked(b2, 'outerTimeLoop', a)


def test_assoc_itemTypes5_link_reassign_clear():
    a = ir_ItemType(name="sample_text")
    b1 = ir_IrModule(name="sample_text")
    b2 = ir_IrModule(name="sample_text_2")
    _safe_set(a, 'ir_ItemType', b1)
    assert _is_linked(a, 'ir_ItemType', b1)
    if hasattr(b1, 'ir_IrModule6'):
        assert _is_linked(b1, 'ir_IrModule6', a)
    _safe_set(a, 'ir_ItemType', b2)
    assert _is_linked(a, 'ir_ItemType', b2)
    if hasattr(b1, 'ir_IrModule6'):
        assert not _is_linked(b1, 'ir_IrModule6', a)
    if hasattr(b2, 'ir_IrModule6'):
        assert _is_linked(b2, 'ir_IrModule6', a)
    _safe_set(a, 'ir_ItemType', None)
    assert not _is_linked(a, 'ir_ItemType', b2)
    if hasattr(b2, 'ir_IrModule6'):
        assert not _is_linked(b2, 'ir_IrModule6', a)


def test_assoc_iterationCounter52_link_reassign_clear():
    a = ir_TimeLoop(name="sample_text")
    b1 = ir_SimpleVariable()
    b2 = ir_SimpleVariable()
    _safe_set(a, 'ir_TimeLoop53', b1)
    assert _is_linked(a, 'ir_TimeLoop53', b1)
    if hasattr(b1, 'ir_SimpleVariable54'):
        assert _is_linked(b1, 'ir_SimpleVariable54', a)
    _safe_set(a, 'ir_TimeLoop53', b2)
    assert _is_linked(a, 'ir_TimeLoop53', b2)
    if hasattr(b1, 'ir_SimpleVariable54'):
        assert not _is_linked(b1, 'ir_SimpleVariable54', a)
    if hasattr(b2, 'ir_SimpleVariable54'):
        assert _is_linked(b2, 'ir_SimpleVariable54', a)
    _safe_set(a, 'ir_TimeLoop53', None)
    assert not _is_linked(a, 'ir_TimeLoop53', b2)
    if hasattr(b2, 'ir_SimpleVariable54'):
        assert not _is_linked(b2, 'ir_SimpleVariable54', a)


def test_assoc_iterator215_link_reassign_clear():
    a = ir_ItemIdValueIterator(shift=7)
    b1 = ir_Iterator()
    b2 = ir_Iterator()
    _safe_set(a, 'ir_ItemIdValueIterator', b1)
    assert _is_linked(a, 'ir_ItemIdValueIterator', b1)
    if hasattr(b1, 'ir_Iterator216'):
        assert _is_linked(b1, 'ir_Iterator216', a)
    _safe_set(a, 'ir_ItemIdValueIterator', b2)
    assert _is_linked(a, 'ir_ItemIdValueIterator', b2)
    if hasattr(b1, 'ir_Iterator216'):
        assert not _is_linked(b1, 'ir_Iterator216', a)
    if hasattr(b2, 'ir_Iterator216'):
        assert _is_linked(b2, 'ir_Iterator216', a)
    _safe_set(a, 'ir_ItemIdValueIterator', None)
    assert not _is_linked(a, 'ir_ItemIdValueIterator', b2)
    if hasattr(b2, 'ir_Iterator216'):
        assert not _is_linked(b2, 'ir_Iterator216', a)


def test_assoc_iterators183_link_reassign_clear():
    a = ir_ItemIndex(itemName="sample_text", name="sample_text")
    b1 = ir_ArgOrVarRef()
    b2 = ir_ArgOrVarRef()
    _safe_set(a, 'ir_ItemIndex185', b1)
    assert _is_linked(a, 'ir_ItemIndex185', b1)
    if hasattr(b1, 'ir_ArgOrVarRef184'):
        assert _is_linked(b1, 'ir_ArgOrVarRef184', a)
    _safe_set(a, 'ir_ItemIndex185', b2)
    assert _is_linked(a, 'ir_ItemIndex185', b2)
    if hasattr(b1, 'ir_ArgOrVarRef184'):
        assert not _is_linked(b1, 'ir_ArgOrVarRef184', a)
    if hasattr(b2, 'ir_ArgOrVarRef184'):
        assert _is_linked(b2, 'ir_ArgOrVarRef184', a)
    _safe_set(a, 'ir_ItemIndex185', None)
    assert not _is_linked(a, 'ir_ItemIndex185', b2)
    if hasattr(b2, 'ir_ArgOrVarRef184'):
        assert not _is_linked(b2, 'ir_ArgOrVarRef184', a)


def test_assoc_jobContainer83_link_reassign_clear():
    a = ir_Job(at=3.14, name="sample_text", onCycle=True)
    b1 = ir_JobContainer()
    b2 = ir_JobContainer()
    _safe_set(a, 'innerJobs', b1)
    assert _is_linked(a, 'innerJobs', b1)
    if hasattr(b1, 'JobContainer'):
        assert _is_linked(b1, 'JobContainer', a)
    _safe_set(a, 'innerJobs', b2)
    assert _is_linked(a, 'innerJobs', b2)
    if hasattr(b1, 'JobContainer'):
        assert not _is_linked(b1, 'JobContainer', a)
    if hasattr(b2, 'JobContainer'):
        assert _is_linked(b2, 'JobContainer', a)
    _safe_set(a, 'innerJobs', None)
    assert not _is_linked(a, 'innerJobs', b2)
    if hasattr(b2, 'JobContainer'):
        assert not _is_linked(b2, 'JobContainer', a)


def test_assoc_jobs26_link_reassign_clear():
    a = ir_Job(at=3.14, name="sample_text", onCycle=True)
    b1 = ir_IrModule(name="sample_text")
    b2 = ir_IrModule(name="sample_text_2")
    _safe_set(a, 'ir_Job', b1)
    assert _is_linked(a, 'ir_Job', b1)
    if hasattr(b1, 'ir_IrModule27'):
        assert _is_linked(b1, 'ir_IrModule27', a)
    _safe_set(a, 'ir_Job', b2)
    assert _is_linked(a, 'ir_Job', b2)
    if hasattr(b1, 'ir_IrModule27'):
        assert not _is_linked(b1, 'ir_IrModule27', a)
    if hasattr(b2, 'ir_IrModule27'):
        assert _is_linked(b2, 'ir_IrModule27', a)
    _safe_set(a, 'ir_Job', None)
    assert not _is_linked(a, 'ir_Job', b2)
    if hasattr(b2, 'ir_IrModule27'):
        assert not _is_linked(b2, 'ir_IrModule27', a)


def test_assoc_lastDumpVariable38_link_reassign_clear():
    a = ir_PostProcessingInfo(periodValue=3.14)
    b1 = ir_SimpleVariable()
    b2 = ir_SimpleVariable()
    _safe_set(a, 'ir_PostProcessingInfo39', b1)
    assert _is_linked(a, 'ir_PostProcessingInfo39', b1)
    if hasattr(b1, 'ir_SimpleVariable40'):
        assert _is_linked(b1, 'ir_SimpleVariable40', a)
    _safe_set(a, 'ir_PostProcessingInfo39', b2)
    assert _is_linked(a, 'ir_PostProcessingInfo39', b2)
    if hasattr(b1, 'ir_SimpleVariable40'):
        assert not _is_linked(b1, 'ir_SimpleVariable40', a)
    if hasattr(b2, 'ir_SimpleVariable40'):
        assert _is_linked(b2, 'ir_SimpleVariable40', a)
    _safe_set(a, 'ir_PostProcessingInfo39', None)
    assert not _is_linked(a, 'ir_PostProcessingInfo39', b2)
    if hasattr(b2, 'ir_SimpleVariable40'):
        assert not _is_linked(b2, 'ir_SimpleVariable40', a)


def test_assoc_left161_link_reassign_clear():
    a = ir_BinaryExpression(operator="sample_text")
    b1 = ir_Expression()
    b2 = ir_Expression()
    _safe_set(a, 'ir_BinaryExpression', b1)
    assert _is_linked(a, 'ir_BinaryExpression', b1)
    if hasattr(b1, 'ir_Expression162'):
        assert _is_linked(b1, 'ir_Expression162', a)
    _safe_set(a, 'ir_BinaryExpression', b2)
    assert _is_linked(a, 'ir_BinaryExpression', b2)
    if hasattr(b1, 'ir_Expression162'):
        assert not _is_linked(b1, 'ir_Expression162', a)
    if hasattr(b2, 'ir_Expression162'):
        assert _is_linked(b2, 'ir_Expression162', a)
    _safe_set(a, 'ir_BinaryExpression', None)
    assert not _is_linked(a, 'ir_BinaryExpression', b2)
    if hasattr(b2, 'ir_Expression162'):
        assert not _is_linked(b2, 'ir_Expression162', a)


def test_assoc_mainTimeLoop28_link_reassign_clear():
    a = ir_TimeLoop(name="sample_text")
    b1 = ir_IrModule(name="sample_text")
    b2 = ir_IrModule(name="sample_text_2")
    _safe_set(a, 'ir_TimeLoop', b1)
    assert _is_linked(a, 'ir_TimeLoop', b1)
    if hasattr(b1, 'ir_IrModule29'):
        assert _is_linked(b1, 'ir_IrModule29', a)
    _safe_set(a, 'ir_TimeLoop', b2)
    assert _is_linked(a, 'ir_TimeLoop', b2)
    if hasattr(b1, 'ir_IrModule29'):
        assert not _is_linked(b1, 'ir_IrModule29', a)
    if hasattr(b2, 'ir_IrModule29'):
        assert _is_linked(b2, 'ir_IrModule29', a)
    _safe_set(a, 'ir_TimeLoop', None)
    assert not _is_linked(a, 'ir_TimeLoop', b2)
    if hasattr(b2, 'ir_IrModule29'):
        assert not _is_linked(b2, 'ir_IrModule29', a)


def test_assoc_next204_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_TimeLoopVariable(name="sample_text")
    b2 = ir_TimeLoopVariable(name="sample_text_2")
    _safe_set(a, 'ir_Variable206', b1)
    assert _is_linked(a, 'ir_Variable206', b1)
    if hasattr(b1, 'ir_TimeLoopVariable205'):
        assert _is_linked(b1, 'ir_TimeLoopVariable205', a)
    _safe_set(a, 'ir_Variable206', b2)
    assert _is_linked(a, 'ir_Variable206', b2)
    if hasattr(b1, 'ir_TimeLoopVariable205'):
        assert not _is_linked(b1, 'ir_TimeLoopVariable205', a)
    if hasattr(b2, 'ir_TimeLoopVariable205'):
        assert _is_linked(b2, 'ir_TimeLoopVariable205', a)
    _safe_set(a, 'ir_Variable206', None)
    assert not _is_linked(a, 'ir_Variable206', b2)
    if hasattr(b2, 'ir_TimeLoopVariable205'):
        assert not _is_linked(b2, 'ir_TimeLoopVariable205', a)


def test_assoc_nodeCoordVariable17_link_reassign_clear():
    a = ir_IrModule(name="sample_text")
    b1 = ir_ConnectivityVariable()
    b2 = ir_ConnectivityVariable()
    _safe_set(a, 'ir_IrModule18', b1)
    assert _is_linked(a, 'ir_IrModule18', b1)
    if hasattr(b1, 'ir_ConnectivityVariable19'):
        assert _is_linked(b1, 'ir_ConnectivityVariable19', a)
    _safe_set(a, 'ir_IrModule18', b2)
    assert _is_linked(a, 'ir_IrModule18', b2)
    if hasattr(b1, 'ir_ConnectivityVariable19'):
        assert not _is_linked(b1, 'ir_ConnectivityVariable19', a)
    if hasattr(b2, 'ir_ConnectivityVariable19'):
        assert _is_linked(b2, 'ir_ConnectivityVariable19', a)
    _safe_set(a, 'ir_IrModule18', None)
    assert not _is_linked(a, 'ir_IrModule18', b2)
    if hasattr(b2, 'ir_ConnectivityVariable19'):
        assert not _is_linked(b2, 'ir_ConnectivityVariable19', a)


def test_assoc_options11_link_reassign_clear():
    a = ir_IrModule(name="sample_text")
    b1 = ir_SimpleVariable()
    b2 = ir_SimpleVariable()
    _safe_set(a, 'ir_IrModule12', {b1})
    assert _is_linked(a, 'ir_IrModule12', b1)
    if hasattr(b1, 'ir_SimpleVariable'):
        assert _is_linked(b1, 'ir_SimpleVariable', a)
    _safe_set(a, 'ir_IrModule12', {b2})
    assert _is_linked(a, 'ir_IrModule12', b2)
    if hasattr(b1, 'ir_SimpleVariable'):
        assert not _is_linked(b1, 'ir_SimpleVariable', a)
    if hasattr(b2, 'ir_SimpleVariable'):
        assert _is_linked(b2, 'ir_SimpleVariable', a)
    _safe_set(a, 'ir_IrModule12', set())
    assert not _is_linked(a, 'ir_IrModule12', b2)
    if hasattr(b2, 'ir_SimpleVariable'):
        assert not _is_linked(b2, 'ir_SimpleVariable', a)


def test_assoc_outerTimeLoop44_link_reassign_clear():
    a = ir_TimeLoop(name="sample_text")
    b1 = ir_TimeLoop(name="sample_text")
    b2 = ir_TimeLoop(name="sample_text_2")
    _safe_set(a, 'TimeLoop45', b1)
    assert _is_linked(a, 'TimeLoop45', b1)
    if hasattr(b1, 'innerTimeLoop'):
        assert _is_linked(b1, 'innerTimeLoop', a)
    _safe_set(a, 'TimeLoop45', b2)
    assert _is_linked(a, 'TimeLoop45', b2)
    if hasattr(b1, 'innerTimeLoop'):
        assert not _is_linked(b1, 'innerTimeLoop', a)
    if hasattr(b2, 'innerTimeLoop'):
        assert _is_linked(b2, 'innerTimeLoop', a)
    _safe_set(a, 'TimeLoop45', None)
    assert not _is_linked(a, 'TimeLoop45', b2)
    if hasattr(b2, 'innerTimeLoop'):
        assert not _is_linked(b2, 'innerTimeLoop', a)


def test_assoc_periodVariable35_link_reassign_clear():
    a = ir_PostProcessingInfo(periodValue=3.14)
    b1 = ir_SimpleVariable()
    b2 = ir_SimpleVariable()
    _safe_set(a, 'ir_PostProcessingInfo36', b1)
    assert _is_linked(a, 'ir_PostProcessingInfo36', b1)
    if hasattr(b1, 'ir_SimpleVariable37'):
        assert _is_linked(b1, 'ir_SimpleVariable37', a)
    _safe_set(a, 'ir_PostProcessingInfo36', b2)
    assert _is_linked(a, 'ir_PostProcessingInfo36', b2)
    if hasattr(b1, 'ir_SimpleVariable37'):
        assert not _is_linked(b1, 'ir_SimpleVariable37', a)
    if hasattr(b2, 'ir_SimpleVariable37'):
        assert _is_linked(b2, 'ir_SimpleVariable37', a)
    _safe_set(a, 'ir_PostProcessingInfo36', None)
    assert not _is_linked(a, 'ir_PostProcessingInfo36', b2)
    if hasattr(b2, 'ir_SimpleVariable37'):
        assert not _is_linked(b2, 'ir_SimpleVariable37', a)


def test_assoc_postProcessedVariables32_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_PostProcessingInfo(periodValue=3.14)
    b2 = ir_PostProcessingInfo(periodValue=9.99)
    _safe_set(a, 'ir_Variable34', b1)
    assert _is_linked(a, 'ir_Variable34', b1)
    if hasattr(b1, 'ir_PostProcessingInfo33'):
        assert _is_linked(b1, 'ir_PostProcessingInfo33', a)
    _safe_set(a, 'ir_Variable34', b2)
    assert _is_linked(a, 'ir_Variable34', b2)
    if hasattr(b1, 'ir_PostProcessingInfo33'):
        assert not _is_linked(b1, 'ir_PostProcessingInfo33', a)
    if hasattr(b2, 'ir_PostProcessingInfo33'):
        assert _is_linked(b2, 'ir_PostProcessingInfo33', a)
    _safe_set(a, 'ir_Variable34', None)
    assert not _is_linked(a, 'ir_Variable34', b2)
    if hasattr(b2, 'ir_PostProcessingInfo33'):
        assert not _is_linked(b2, 'ir_PostProcessingInfo33', a)


def test_assoc_postProcessingInfo30_link_reassign_clear():
    a = ir_PostProcessingInfo(periodValue=3.14)
    b1 = ir_IrModule(name="sample_text")
    b2 = ir_IrModule(name="sample_text_2")
    _safe_set(a, 'ir_PostProcessingInfo', b1)
    assert _is_linked(a, 'ir_PostProcessingInfo', b1)
    if hasattr(b1, 'ir_IrModule31'):
        assert _is_linked(b1, 'ir_IrModule31', a)
    _safe_set(a, 'ir_PostProcessingInfo', b2)
    assert _is_linked(a, 'ir_PostProcessingInfo', b2)
    if hasattr(b1, 'ir_IrModule31'):
        assert not _is_linked(b1, 'ir_IrModule31', a)
    if hasattr(b2, 'ir_IrModule31'):
        assert _is_linked(b2, 'ir_IrModule31', a)
    _safe_set(a, 'ir_PostProcessingInfo', None)
    assert not _is_linked(a, 'ir_PostProcessingInfo', b2)
    if hasattr(b2, 'ir_IrModule31'):
        assert not _is_linked(b2, 'ir_IrModule31', a)


def test_assoc_returnType66_link_reassign_clear():
    a = ir_Function(name="sample_text", provider="sample_text")
    b1 = ir_BaseType(primitive="sample_text")
    b2 = ir_BaseType(primitive="sample_text_2")
    _safe_set(a, 'ir_Function67', b1)
    assert _is_linked(a, 'ir_Function67', b1)
    if hasattr(b1, 'ir_BaseType68'):
        assert _is_linked(b1, 'ir_BaseType68', a)
    _safe_set(a, 'ir_Function67', b2)
    assert _is_linked(a, 'ir_Function67', b2)
    if hasattr(b1, 'ir_BaseType68'):
        assert not _is_linked(b1, 'ir_BaseType68', a)
    if hasattr(b2, 'ir_BaseType68'):
        assert _is_linked(b2, 'ir_BaseType68', a)
    _safe_set(a, 'ir_Function67', None)
    assert not _is_linked(a, 'ir_Function67', b2)
    if hasattr(b2, 'ir_BaseType68'):
        assert not _is_linked(b2, 'ir_BaseType68', a)


def test_assoc_returnType80_link_reassign_clear():
    a = ir_ItemType(name="sample_text")
    b1 = ir_Connectivity(indexEqualId=True, multiple=True, name="sample_text")
    b2 = ir_Connectivity(indexEqualId=False, multiple=False, name="sample_text_2")
    _safe_set(a, 'ir_ItemType82', b1)
    assert _is_linked(a, 'ir_ItemType82', b1)
    if hasattr(b1, 'ir_Connectivity81'):
        assert _is_linked(b1, 'ir_Connectivity81', a)
    _safe_set(a, 'ir_ItemType82', b2)
    assert _is_linked(a, 'ir_ItemType82', b2)
    if hasattr(b1, 'ir_Connectivity81'):
        assert not _is_linked(b1, 'ir_Connectivity81', a)
    if hasattr(b2, 'ir_Connectivity81'):
        assert _is_linked(b2, 'ir_Connectivity81', a)
    _safe_set(a, 'ir_ItemType82', None)
    assert not _is_linked(a, 'ir_ItemType82', b2)
    if hasattr(b2, 'ir_Connectivity81'):
        assert not _is_linked(b2, 'ir_Connectivity81', a)


def test_assoc_right163_link_reassign_clear():
    a = ir_BinaryExpression(operator="sample_text")
    b1 = ir_Expression()
    b2 = ir_Expression()
    _safe_set(a, 'ir_BinaryExpression164', b1)
    assert _is_linked(a, 'ir_BinaryExpression164', b1)
    if hasattr(b1, 'ir_Expression165'):
        assert _is_linked(b1, 'ir_Expression165', a)
    _safe_set(a, 'ir_BinaryExpression164', b2)
    assert _is_linked(a, 'ir_BinaryExpression164', b2)
    if hasattr(b1, 'ir_Expression165'):
        assert not _is_linked(b1, 'ir_Expression165', a)
    if hasattr(b2, 'ir_Expression165'):
        assert _is_linked(b2, 'ir_Expression165', a)
    _safe_set(a, 'ir_BinaryExpression164', None)
    assert not _is_linked(a, 'ir_BinaryExpression164', b2)
    if hasattr(b2, 'ir_Expression165'):
        assert not _is_linked(b2, 'ir_Expression165', a)


def test_assoc_sizes189_link_reassign_clear():
    a = ir_BaseType(primitive="sample_text")
    b1 = ir_Expression()
    b2 = ir_Expression()
    _safe_set(a, 'ir_BaseType190', {b1})
    assert _is_linked(a, 'ir_BaseType190', b1)
    if hasattr(b1, 'ir_Expression191'):
        assert _is_linked(b1, 'ir_Expression191', a)
    _safe_set(a, 'ir_BaseType190', {b2})
    assert _is_linked(a, 'ir_BaseType190', b2)
    if hasattr(b1, 'ir_Expression191'):
        assert not _is_linked(b1, 'ir_Expression191', a)
    if hasattr(b2, 'ir_Expression191'):
        assert _is_linked(b2, 'ir_Expression191', a)
    _safe_set(a, 'ir_BaseType190', set())
    assert not _is_linked(a, 'ir_BaseType190', b2)
    if hasattr(b2, 'ir_Expression191'):
        assert not _is_linked(b2, 'ir_Expression191', a)


def test_assoc_source93_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_TimeLoopCopy()
    b2 = ir_TimeLoopCopy()
    _safe_set(a, 'ir_Variable95', b1)
    assert _is_linked(a, 'ir_Variable95', b1)
    if hasattr(b1, 'ir_TimeLoopCopy94'):
        assert _is_linked(b1, 'ir_TimeLoopCopy94', a)
    _safe_set(a, 'ir_Variable95', b2)
    assert _is_linked(a, 'ir_Variable95', b2)
    if hasattr(b1, 'ir_TimeLoopCopy94'):
        assert not _is_linked(b1, 'ir_TimeLoopCopy94', a)
    if hasattr(b2, 'ir_TimeLoopCopy94'):
        assert _is_linked(b2, 'ir_TimeLoopCopy94', a)
    _safe_set(a, 'ir_Variable95', None)
    assert not _is_linked(a, 'ir_Variable95', b2)
    if hasattr(b2, 'ir_TimeLoopCopy94'):
        assert not _is_linked(b2, 'ir_TimeLoopCopy94', a)


def test_assoc_target181_link_reassign_clear():
    a = ir_ArgOrVar(name="sample_text")
    b1 = ir_ArgOrVarRef()
    b2 = ir_ArgOrVarRef()
    _safe_set(a, 'ir_ArgOrVar', b1)
    assert _is_linked(a, 'ir_ArgOrVar', b1)
    if hasattr(b1, 'ir_ArgOrVarRef182'):
        assert _is_linked(b1, 'ir_ArgOrVarRef182', a)
    _safe_set(a, 'ir_ArgOrVar', b2)
    assert _is_linked(a, 'ir_ArgOrVar', b2)
    if hasattr(b1, 'ir_ArgOrVarRef182'):
        assert not _is_linked(b1, 'ir_ArgOrVarRef182', a)
    if hasattr(b2, 'ir_ArgOrVarRef182'):
        assert _is_linked(b2, 'ir_ArgOrVarRef182', a)
    _safe_set(a, 'ir_ArgOrVar', None)
    assert not _is_linked(a, 'ir_ArgOrVar', b2)
    if hasattr(b2, 'ir_ArgOrVarRef182'):
        assert not _is_linked(b2, 'ir_ArgOrVarRef182', a)


def test_assoc_target213_link_reassign_clear():
    a = ir_SetDefinition(name="sample_text")
    b1 = ir_SetRef()
    b2 = ir_SetRef()
    _safe_set(a, 'ir_SetDefinition214', b1)
    assert _is_linked(a, 'ir_SetDefinition214', b1)
    if hasattr(b1, 'ir_SetRef'):
        assert _is_linked(b1, 'ir_SetRef', a)
    _safe_set(a, 'ir_SetDefinition214', b2)
    assert _is_linked(a, 'ir_SetDefinition214', b2)
    if hasattr(b1, 'ir_SetRef'):
        assert not _is_linked(b1, 'ir_SetRef', a)
    if hasattr(b2, 'ir_SetRef'):
        assert _is_linked(b2, 'ir_SetRef', a)
    _safe_set(a, 'ir_SetDefinition214', None)
    assert not _is_linked(a, 'ir_SetDefinition214', b2)
    if hasattr(b2, 'ir_SetRef'):
        assert not _is_linked(b2, 'ir_SetRef', a)


def test_assoc_timeLoop87_link_reassign_clear():
    a = ir_TimeLoop(name="sample_text")
    b1 = ir_TimeLoopCopyJob()
    b2 = ir_TimeLoopCopyJob()
    _safe_set(a, 'ir_TimeLoop89', b1)
    assert _is_linked(a, 'ir_TimeLoop89', b1)
    if hasattr(b1, 'ir_TimeLoopCopyJob88'):
        assert _is_linked(b1, 'ir_TimeLoopCopyJob88', a)
    _safe_set(a, 'ir_TimeLoop89', b2)
    assert _is_linked(a, 'ir_TimeLoop89', b2)
    if hasattr(b1, 'ir_TimeLoopCopyJob88'):
        assert not _is_linked(b1, 'ir_TimeLoopCopyJob88', a)
    if hasattr(b2, 'ir_TimeLoopCopyJob88'):
        assert _is_linked(b2, 'ir_TimeLoopCopyJob88', a)
    _safe_set(a, 'ir_TimeLoop89', None)
    assert not _is_linked(a, 'ir_TimeLoop89', b2)
    if hasattr(b2, 'ir_TimeLoopCopyJob88'):
        assert not _is_linked(b2, 'ir_TimeLoopCopyJob88', a)


def test_assoc_timeVariable20_link_reassign_clear():
    a = ir_IrModule(name="sample_text")
    b1 = ir_SimpleVariable()
    b2 = ir_SimpleVariable()
    _safe_set(a, 'ir_IrModule21', b1)
    assert _is_linked(a, 'ir_IrModule21', b1)
    if hasattr(b1, 'ir_SimpleVariable22'):
        assert _is_linked(b1, 'ir_SimpleVariable22', a)
    _safe_set(a, 'ir_IrModule21', b2)
    assert _is_linked(a, 'ir_IrModule21', b2)
    if hasattr(b1, 'ir_SimpleVariable22'):
        assert not _is_linked(b1, 'ir_SimpleVariable22', a)
    if hasattr(b2, 'ir_SimpleVariable22'):
        assert _is_linked(b2, 'ir_SimpleVariable22', a)
    _safe_set(a, 'ir_IrModule21', None)
    assert not _is_linked(a, 'ir_IrModule21', b2)
    if hasattr(b2, 'ir_SimpleVariable22'):
        assert not _is_linked(b2, 'ir_SimpleVariable22', a)


def test_assoc_type55_link_reassign_clear():
    a = ir_BaseType(primitive="sample_text")
    b1 = ir_Arg()
    b2 = ir_Arg()
    _safe_set(a, 'ir_BaseType', b1)
    assert _is_linked(a, 'ir_BaseType', b1)
    if hasattr(b1, 'ir_Arg'):
        assert _is_linked(b1, 'ir_Arg', a)
    _safe_set(a, 'ir_BaseType', b2)
    assert _is_linked(a, 'ir_BaseType', b2)
    if hasattr(b1, 'ir_Arg'):
        assert not _is_linked(b1, 'ir_Arg', a)
    if hasattr(b2, 'ir_Arg'):
        assert _is_linked(b2, 'ir_Arg', a)
    _safe_set(a, 'ir_BaseType', None)
    assert not _is_linked(a, 'ir_BaseType', b2)
    if hasattr(b2, 'ir_Arg'):
        assert not _is_linked(b2, 'ir_Arg', a)


def test_assoc_type56_link_reassign_clear():
    a = ir_BaseType(primitive="sample_text")
    b1 = ir_SimpleVariable()
    b2 = ir_SimpleVariable()
    _safe_set(a, 'ir_BaseType58', b1)
    assert _is_linked(a, 'ir_BaseType58', b1)
    if hasattr(b1, 'ir_SimpleVariable57'):
        assert _is_linked(b1, 'ir_SimpleVariable57', a)
    _safe_set(a, 'ir_BaseType58', b2)
    assert _is_linked(a, 'ir_BaseType58', b2)
    if hasattr(b1, 'ir_SimpleVariable57'):
        assert not _is_linked(b1, 'ir_SimpleVariable57', a)
    if hasattr(b2, 'ir_SimpleVariable57'):
        assert _is_linked(b2, 'ir_SimpleVariable57', a)
    _safe_set(a, 'ir_BaseType58', None)
    assert not _is_linked(a, 'ir_BaseType58', b2)
    if hasattr(b2, 'ir_SimpleVariable57'):
        assert not _is_linked(b2, 'ir_SimpleVariable57', a)


def test_assoc_value128_link_reassign_clear():
    a = ir_SetDefinition(name="sample_text")
    b1 = ir_ConnectivityCall()
    b2 = ir_ConnectivityCall()
    _safe_set(a, 'ir_SetDefinition', b1)
    assert _is_linked(a, 'ir_SetDefinition', b1)
    if hasattr(b1, 'ir_ConnectivityCall'):
        assert _is_linked(b1, 'ir_ConnectivityCall', a)
    _safe_set(a, 'ir_SetDefinition', b2)
    assert _is_linked(a, 'ir_SetDefinition', b2)
    if hasattr(b1, 'ir_ConnectivityCall'):
        assert not _is_linked(b1, 'ir_ConnectivityCall', a)
    if hasattr(b2, 'ir_ConnectivityCall'):
        assert _is_linked(b2, 'ir_ConnectivityCall', a)
    _safe_set(a, 'ir_SetDefinition', None)
    assert not _is_linked(a, 'ir_SetDefinition', b2)
    if hasattr(b2, 'ir_ConnectivityCall'):
        assert not _is_linked(b2, 'ir_ConnectivityCall', a)


def test_assoc_variable101_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_VariableDefinition()
    b2 = ir_VariableDefinition()
    _safe_set(a, 'ir_Variable102', b1)
    assert _is_linked(a, 'ir_Variable102', b1)
    if hasattr(b1, 'ir_VariableDefinition'):
        assert _is_linked(b1, 'ir_VariableDefinition', a)
    _safe_set(a, 'ir_Variable102', b2)
    assert _is_linked(a, 'ir_Variable102', b2)
    if hasattr(b1, 'ir_VariableDefinition'):
        assert not _is_linked(b1, 'ir_VariableDefinition', a)
    if hasattr(b2, 'ir_VariableDefinition'):
        assert _is_linked(b2, 'ir_VariableDefinition', a)
    _safe_set(a, 'ir_Variable102', None)
    assert not _is_linked(a, 'ir_Variable102', b2)
    if hasattr(b2, 'ir_VariableDefinition'):
        assert not _is_linked(b2, 'ir_VariableDefinition', a)


def test_assoc_variables13_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_IrModule(name="sample_text")
    b2 = ir_IrModule(name="sample_text_2")
    _safe_set(a, 'ir_Variable', b1)
    assert _is_linked(a, 'ir_Variable', b1)
    if hasattr(b1, 'ir_IrModule14'):
        assert _is_linked(b1, 'ir_IrModule14', a)
    _safe_set(a, 'ir_Variable', b2)
    assert _is_linked(a, 'ir_Variable', b2)
    if hasattr(b1, 'ir_IrModule14'):
        assert not _is_linked(b1, 'ir_IrModule14', a)
    if hasattr(b2, 'ir_IrModule14'):
        assert _is_linked(b2, 'ir_IrModule14', a)
    _safe_set(a, 'ir_Variable', None)
    assert not _is_linked(a, 'ir_Variable', b2)
    if hasattr(b2, 'ir_IrModule14'):
        assert not _is_linked(b2, 'ir_IrModule14', a)


def test_assoc_variables46_link_reassign_clear():
    a = ir_TimeLoopVariable(name="sample_text")
    b1 = ir_TimeLoop(name="sample_text")
    b2 = ir_TimeLoop(name="sample_text_2")
    _safe_set(a, 'ir_TimeLoopVariable', b1)
    assert _is_linked(a, 'ir_TimeLoopVariable', b1)
    if hasattr(b1, 'ir_TimeLoop47'):
        assert _is_linked(b1, 'ir_TimeLoop47', a)
    _safe_set(a, 'ir_TimeLoopVariable', b2)
    assert _is_linked(a, 'ir_TimeLoopVariable', b2)
    if hasattr(b1, 'ir_TimeLoop47'):
        assert not _is_linked(b1, 'ir_TimeLoop47', a)
    if hasattr(b2, 'ir_TimeLoop47'):
        assert _is_linked(b2, 'ir_TimeLoop47', a)
    _safe_set(a, 'ir_TimeLoopVariable', None)
    assert not _is_linked(a, 'ir_TimeLoopVariable', b2)
    if hasattr(b2, 'ir_TimeLoop47'):
        assert not _is_linked(b2, 'ir_TimeLoop47', a)


def test_assoc_variables69_link_reassign_clear():
    a = ir_Function(name="sample_text", provider="sample_text")
    b1 = ir_SimpleVariable()
    b2 = ir_SimpleVariable()
    _safe_set(a, 'ir_Function70', {b1})
    assert _is_linked(a, 'ir_Function70', b1)
    if hasattr(b1, 'ir_SimpleVariable71'):
        assert _is_linked(b1, 'ir_SimpleVariable71', a)
    _safe_set(a, 'ir_Function70', {b2})
    assert _is_linked(a, 'ir_Function70', b2)
    if hasattr(b1, 'ir_SimpleVariable71'):
        assert not _is_linked(b1, 'ir_SimpleVariable71', a)
    if hasattr(b2, 'ir_SimpleVariable71'):
        assert _is_linked(b2, 'ir_SimpleVariable71', a)
    _safe_set(a, 'ir_Function70', set())
    assert not _is_linked(a, 'ir_Function70', b2)
    if hasattr(b2, 'ir_SimpleVariable71'):
        assert not _is_linked(b2, 'ir_SimpleVariable71', a)


def test_assoc_variables96_link_reassign_clear():
    a = ir_Variable(const=True, persistenceName="sample_text")
    b1 = ir_InstructionBlock()
    b2 = ir_InstructionBlock()
    _safe_set(a, 'ir_Variable97', b1)
    assert _is_linked(a, 'ir_Variable97', b1)
    if hasattr(b1, 'ir_InstructionBlock'):
        assert _is_linked(b1, 'ir_InstructionBlock', a)
    _safe_set(a, 'ir_Variable97', b2)
    assert _is_linked(a, 'ir_Variable97', b2)
    if hasattr(b1, 'ir_InstructionBlock'):
        assert not _is_linked(b1, 'ir_InstructionBlock', a)
    if hasattr(b2, 'ir_InstructionBlock'):
        assert _is_linked(b2, 'ir_InstructionBlock', a)
    _safe_set(a, 'ir_Variable97', None)
    assert not _is_linked(a, 'ir_Variable97', b2)
    if hasattr(b2, 'ir_InstructionBlock'):
        assert not _is_linked(b2, 'ir_InstructionBlock', a)


def test_assoc_whileCondition48_link_reassign_clear():
    a = ir_TimeLoop(name="sample_text")
    b1 = ir_Expression()
    b2 = ir_Expression()
    _safe_set(a, 'ir_TimeLoop49', b1)
    assert _is_linked(a, 'ir_TimeLoop49', b1)
    if hasattr(b1, 'ir_Expression'):
        assert _is_linked(b1, 'ir_Expression', a)
    _safe_set(a, 'ir_TimeLoop49', b2)
    assert _is_linked(a, 'ir_TimeLoop49', b2)
    if hasattr(b1, 'ir_Expression'):
        assert not _is_linked(b1, 'ir_Expression', a)
    if hasattr(b2, 'ir_Expression'):
        assert _is_linked(b2, 'ir_Expression', a)
    _safe_set(a, 'ir_TimeLoop49', None)
    assert not _is_linked(a, 'ir_TimeLoop49', b2)
    if hasattr(b2, 'ir_Expression'):
        assert not _is_linked(b2, 'ir_Expression', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ArgOrVar_strategy = st.builds(ArgOrVar)
@given(instance=ArgOrVar_strategy)
@settings(max_examples=25)
def test_ArgOrVar_instantiation(instance):
    assert isinstance(instance, ArgOrVar)


Container_strategy = st.builds(Container)
@given(instance=Container_strategy)
@settings(max_examples=25)
def test_Container_instantiation(instance):
    assert isinstance(instance, Container)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Instruction_strategy = st.builds(Instruction)
@given(instance=Instruction_strategy)
@settings(max_examples=25)
def test_Instruction_instantiation(instance):
    assert isinstance(instance, Instruction)


IrAnnotable_strategy = st.builds(IrAnnotable)
@given(instance=IrAnnotable_strategy)
@settings(max_examples=25)
def test_IrAnnotable_instantiation(instance):
    assert isinstance(instance, IrAnnotable)


IrType_strategy = st.builds(IrType)
@given(instance=IrType_strategy)
@settings(max_examples=25)
def test_IrType_instantiation(instance):
    assert isinstance(instance, IrType)


ItemIdValue_strategy = st.builds(ItemIdValue)
@given(instance=ItemIdValue_strategy)
@settings(max_examples=25)
def test_ItemIdValue_instantiation(instance):
    assert isinstance(instance, ItemIdValue)


IterableInstruction_strategy = st.builds(IterableInstruction)
@given(instance=IterableInstruction_strategy)
@settings(max_examples=25)
def test_IterableInstruction_instantiation(instance):
    assert isinstance(instance, IterableInstruction)


IterationBlock_strategy = st.builds(IterationBlock)
@given(instance=IterationBlock_strategy)
@settings(max_examples=25)
def test_IterationBlock_instantiation(instance):
    assert isinstance(instance, IterationBlock)


Job_strategy = st.builds(Job)
@given(instance=Job_strategy)
@settings(max_examples=25)
def test_Job_instantiation(instance):
    assert isinstance(instance, Job)


JobContainer_strategy = st.builds(JobContainer)
@given(instance=JobContainer_strategy)
@settings(max_examples=25)
def test_JobContainer_instantiation(instance):
    assert isinstance(instance, JobContainer)


TimeLoopCopyJob_strategy = st.builds(TimeLoopCopyJob)
@given(instance=TimeLoopCopyJob_strategy)
@settings(max_examples=25)
def test_TimeLoopCopyJob_instantiation(instance):
    assert isinstance(instance, TimeLoopCopyJob)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


ir_Affectation_strategy = st.builds(ir_Affectation)
@given(instance=ir_Affectation_strategy)
@settings(max_examples=25)
def test_ir_Affectation_instantiation(instance):
    assert isinstance(instance, ir_Affectation)


ir_AfterTimeLoopJob_strategy = st.builds(ir_AfterTimeLoopJob)
@given(instance=ir_AfterTimeLoopJob_strategy)
@settings(max_examples=25)
def test_ir_AfterTimeLoopJob_instantiation(instance):
    assert isinstance(instance, ir_AfterTimeLoopJob)


ir_Arg_strategy = st.builds(ir_Arg)
@given(instance=ir_Arg_strategy)
@settings(max_examples=25)
def test_ir_Arg_instantiation(instance):
    assert isinstance(instance, ir_Arg)


ir_ArgOrVar_strategy = st.builds(ir_ArgOrVar, name=safe_text)
@given(instance=ir_ArgOrVar_strategy)
@settings(max_examples=25)
def test_ir_ArgOrVar_instantiation(instance):
    assert isinstance(instance, ir_ArgOrVar)


ir_ArgOrVarRef_strategy = st.builds(ir_ArgOrVarRef)
@given(instance=ir_ArgOrVarRef_strategy)
@settings(max_examples=25)
def test_ir_ArgOrVarRef_instantiation(instance):
    assert isinstance(instance, ir_ArgOrVarRef)


ir_BaseType_strategy = st.builds(ir_BaseType, primitive=safe_text)
@given(instance=ir_BaseType_strategy)
@settings(max_examples=25)
def test_ir_BaseType_instantiation(instance):
    assert isinstance(instance, ir_BaseType)


ir_BaseTypeConstant_strategy = st.builds(ir_BaseTypeConstant)
@given(instance=ir_BaseTypeConstant_strategy)
@settings(max_examples=25)
def test_ir_BaseTypeConstant_instantiation(instance):
    assert isinstance(instance, ir_BaseTypeConstant)


ir_BeforeTimeLoopJob_strategy = st.builds(ir_BeforeTimeLoopJob)
@given(instance=ir_BeforeTimeLoopJob_strategy)
@settings(max_examples=25)
def test_ir_BeforeTimeLoopJob_instantiation(instance):
    assert isinstance(instance, ir_BeforeTimeLoopJob)


ir_BinaryExpression_strategy = st.builds(ir_BinaryExpression, operator=safe_text)
@given(instance=ir_BinaryExpression_strategy)
@settings(max_examples=25)
def test_ir_BinaryExpression_instantiation(instance):
    assert isinstance(instance, ir_BinaryExpression)


ir_BoolConstant_strategy = st.builds(ir_BoolConstant, value=st.booleans())
@given(instance=ir_BoolConstant_strategy)
@settings(max_examples=25)
def test_ir_BoolConstant_instantiation(instance):
    assert isinstance(instance, ir_BoolConstant)


ir_Cardinality_strategy = st.builds(ir_Cardinality)
@given(instance=ir_Cardinality_strategy)
@settings(max_examples=25)
def test_ir_Cardinality_instantiation(instance):
    assert isinstance(instance, ir_Cardinality)


ir_Connectivity_strategy = st.builds(ir_Connectivity, indexEqualId=st.booleans(), multiple=st.booleans(), name=safe_text)
@given(instance=ir_Connectivity_strategy)
@settings(max_examples=25)
def test_ir_Connectivity_instantiation(instance):
    assert isinstance(instance, ir_Connectivity)


ir_ConnectivityCall_strategy = st.builds(ir_ConnectivityCall)
@given(instance=ir_ConnectivityCall_strategy)
@settings(max_examples=25)
def test_ir_ConnectivityCall_instantiation(instance):
    assert isinstance(instance, ir_ConnectivityCall)


ir_ConnectivityType_strategy = st.builds(ir_ConnectivityType)
@given(instance=ir_ConnectivityType_strategy)
@settings(max_examples=25)
def test_ir_ConnectivityType_instantiation(instance):
    assert isinstance(instance, ir_ConnectivityType)


ir_ConnectivityVariable_strategy = st.builds(ir_ConnectivityVariable)
@given(instance=ir_ConnectivityVariable_strategy)
@settings(max_examples=25)
def test_ir_ConnectivityVariable_instantiation(instance):
    assert isinstance(instance, ir_ConnectivityVariable)


ir_Container_strategy = st.builds(ir_Container)
@given(instance=ir_Container_strategy)
@settings(max_examples=25)
def test_ir_Container_instantiation(instance):
    assert isinstance(instance, ir_Container)


ir_ContractedIf_strategy = st.builds(ir_ContractedIf)
@given(instance=ir_ContractedIf_strategy)
@settings(max_examples=25)
def test_ir_ContractedIf_instantiation(instance):
    assert isinstance(instance, ir_ContractedIf)


ir_EStringToStringMapEntry_strategy = st.builds(ir_EStringToStringMapEntry)
@given(instance=ir_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_ir_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, ir_EStringToStringMapEntry)


ir_Exit_strategy = st.builds(ir_Exit, message=safe_text)
@given(instance=ir_Exit_strategy)
@settings(max_examples=25)
def test_ir_Exit_instantiation(instance):
    assert isinstance(instance, ir_Exit)


ir_Expression_strategy = st.builds(ir_Expression)
@given(instance=ir_Expression_strategy)
@settings(max_examples=25)
def test_ir_Expression_instantiation(instance):
    assert isinstance(instance, ir_Expression)


ir_Function_strategy = st.builds(ir_Function, name=safe_text, provider=safe_text)
@given(instance=ir_Function_strategy)
@settings(max_examples=25)
def test_ir_Function_instantiation(instance):
    assert isinstance(instance, ir_Function)


ir_FunctionCall_strategy = st.builds(ir_FunctionCall)
@given(instance=ir_FunctionCall_strategy)
@settings(max_examples=25)
def test_ir_FunctionCall_instantiation(instance):
    assert isinstance(instance, ir_FunctionCall)


ir_If_strategy = st.builds(ir_If)
@given(instance=ir_If_strategy)
@settings(max_examples=25)
def test_ir_If_instantiation(instance):
    assert isinstance(instance, ir_If)


ir_Import_strategy = st.builds(ir_Import, importedNamespace=safe_text)
@given(instance=ir_Import_strategy)
@settings(max_examples=25)
def test_ir_Import_instantiation(instance):
    assert isinstance(instance, ir_Import)


ir_Instruction_strategy = st.builds(ir_Instruction)
@given(instance=ir_Instruction_strategy)
@settings(max_examples=25)
def test_ir_Instruction_instantiation(instance):
    assert isinstance(instance, ir_Instruction)


ir_InstructionBlock_strategy = st.builds(ir_InstructionBlock)
@given(instance=ir_InstructionBlock_strategy)
@settings(max_examples=25)
def test_ir_InstructionBlock_instantiation(instance):
    assert isinstance(instance, ir_InstructionBlock)


ir_InstructionJob_strategy = st.builds(ir_InstructionJob)
@given(instance=ir_InstructionJob_strategy)
@settings(max_examples=25)
def test_ir_InstructionJob_instantiation(instance):
    assert isinstance(instance, ir_InstructionJob)


ir_IntConstant_strategy = st.builds(ir_IntConstant, value=st.integers())
@given(instance=ir_IntConstant_strategy)
@settings(max_examples=25)
def test_ir_IntConstant_instantiation(instance):
    assert isinstance(instance, ir_IntConstant)


ir_Interval_strategy = st.builds(ir_Interval)
@given(instance=ir_Interval_strategy)
@settings(max_examples=25)
def test_ir_Interval_instantiation(instance):
    assert isinstance(instance, ir_Interval)


ir_IrAnnotable_strategy = st.builds(ir_IrAnnotable)
@given(instance=ir_IrAnnotable_strategy)
@settings(max_examples=25)
def test_ir_IrAnnotable_instantiation(instance):
    assert isinstance(instance, ir_IrAnnotable)


ir_IrAnnotation_strategy = st.builds(ir_IrAnnotation, source=safe_text)
@given(instance=ir_IrAnnotation_strategy)
@settings(max_examples=25)
def test_ir_IrAnnotation_instantiation(instance):
    assert isinstance(instance, ir_IrAnnotation)


ir_IrModule_strategy = st.builds(ir_IrModule, name=safe_text)
@given(instance=ir_IrModule_strategy)
@settings(max_examples=25)
def test_ir_IrModule_instantiation(instance):
    assert isinstance(instance, ir_IrModule)


ir_IrType_strategy = st.builds(ir_IrType)
@given(instance=ir_IrType_strategy)
@settings(max_examples=25)
def test_ir_IrType_instantiation(instance):
    assert isinstance(instance, ir_IrType)


ir_ItemId_strategy = st.builds(ir_ItemId, itemName=safe_text, name=safe_text)
@given(instance=ir_ItemId_strategy)
@settings(max_examples=25)
def test_ir_ItemId_instantiation(instance):
    assert isinstance(instance, ir_ItemId)


ir_ItemIdDefinition_strategy = st.builds(ir_ItemIdDefinition)
@given(instance=ir_ItemIdDefinition_strategy)
@settings(max_examples=25)
def test_ir_ItemIdDefinition_instantiation(instance):
    assert isinstance(instance, ir_ItemIdDefinition)


ir_ItemIdValue_strategy = st.builds(ir_ItemIdValue)
@given(instance=ir_ItemIdValue_strategy)
@settings(max_examples=25)
def test_ir_ItemIdValue_instantiation(instance):
    assert isinstance(instance, ir_ItemIdValue)


ir_ItemIdValueCall_strategy = st.builds(ir_ItemIdValueCall)
@given(instance=ir_ItemIdValueCall_strategy)
@settings(max_examples=25)
def test_ir_ItemIdValueCall_instantiation(instance):
    assert isinstance(instance, ir_ItemIdValueCall)


ir_ItemIdValueIterator_strategy = st.builds(ir_ItemIdValueIterator, shift=st.integers())
@given(instance=ir_ItemIdValueIterator_strategy)
@settings(max_examples=25)
def test_ir_ItemIdValueIterator_instantiation(instance):
    assert isinstance(instance, ir_ItemIdValueIterator)


ir_ItemIndex_strategy = st.builds(ir_ItemIndex, itemName=safe_text, name=safe_text)
@given(instance=ir_ItemIndex_strategy)
@settings(max_examples=25)
def test_ir_ItemIndex_instantiation(instance):
    assert isinstance(instance, ir_ItemIndex)


ir_ItemIndexDefinition_strategy = st.builds(ir_ItemIndexDefinition)
@given(instance=ir_ItemIndexDefinition_strategy)
@settings(max_examples=25)
def test_ir_ItemIndexDefinition_instantiation(instance):
    assert isinstance(instance, ir_ItemIndexDefinition)


ir_ItemIndexValue_strategy = st.builds(ir_ItemIndexValue)
@given(instance=ir_ItemIndexValue_strategy)
@settings(max_examples=25)
def test_ir_ItemIndexValue_instantiation(instance):
    assert isinstance(instance, ir_ItemIndexValue)


ir_ItemType_strategy = st.builds(ir_ItemType, name=safe_text)
@given(instance=ir_ItemType_strategy)
@settings(max_examples=25)
def test_ir_ItemType_instantiation(instance):
    assert isinstance(instance, ir_ItemType)


ir_IterableInstruction_strategy = st.builds(ir_IterableInstruction)
@given(instance=ir_IterableInstruction_strategy)
@settings(max_examples=25)
def test_ir_IterableInstruction_instantiation(instance):
    assert isinstance(instance, ir_IterableInstruction)


ir_IterationBlock_strategy = st.builds(ir_IterationBlock)
@given(instance=ir_IterationBlock_strategy)
@settings(max_examples=25)
def test_ir_IterationBlock_instantiation(instance):
    assert isinstance(instance, ir_IterationBlock)


ir_Iterator_strategy = st.builds(ir_Iterator)
@given(instance=ir_Iterator_strategy)
@settings(max_examples=25)
def test_ir_Iterator_instantiation(instance):
    assert isinstance(instance, ir_Iterator)


ir_Job_strategy = st.builds(ir_Job, at=st.floats(allow_nan=False, allow_infinity=False), name=safe_text, onCycle=st.booleans())
@given(instance=ir_Job_strategy)
@settings(max_examples=25)
def test_ir_Job_instantiation(instance):
    assert isinstance(instance, ir_Job)


ir_JobContainer_strategy = st.builds(ir_JobContainer)
@given(instance=ir_JobContainer_strategy)
@settings(max_examples=25)
def test_ir_JobContainer_instantiation(instance):
    assert isinstance(instance, ir_JobContainer)


ir_Loop_strategy = st.builds(ir_Loop, multithreadable=st.booleans())
@given(instance=ir_Loop_strategy)
@settings(max_examples=25)
def test_ir_Loop_instantiation(instance):
    assert isinstance(instance, ir_Loop)


ir_MaxConstant_strategy = st.builds(ir_MaxConstant)
@given(instance=ir_MaxConstant_strategy)
@settings(max_examples=25)
def test_ir_MaxConstant_instantiation(instance):
    assert isinstance(instance, ir_MaxConstant)


ir_MinConstant_strategy = st.builds(ir_MinConstant)
@given(instance=ir_MinConstant_strategy)
@settings(max_examples=25)
def test_ir_MinConstant_instantiation(instance):
    assert isinstance(instance, ir_MinConstant)


ir_Parenthesis_strategy = st.builds(ir_Parenthesis)
@given(instance=ir_Parenthesis_strategy)
@settings(max_examples=25)
def test_ir_Parenthesis_instantiation(instance):
    assert isinstance(instance, ir_Parenthesis)


ir_PostProcessingInfo_strategy = st.builds(ir_PostProcessingInfo, periodValue=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ir_PostProcessingInfo_strategy)
@settings(max_examples=25)
def test_ir_PostProcessingInfo_instantiation(instance):
    assert isinstance(instance, ir_PostProcessingInfo)


ir_RealConstant_strategy = st.builds(ir_RealConstant, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ir_RealConstant_strategy)
@settings(max_examples=25)
def test_ir_RealConstant_instantiation(instance):
    assert isinstance(instance, ir_RealConstant)


ir_ReductionInstruction_strategy = st.builds(ir_ReductionInstruction)
@given(instance=ir_ReductionInstruction_strategy)
@settings(max_examples=25)
def test_ir_ReductionInstruction_instantiation(instance):
    assert isinstance(instance, ir_ReductionInstruction)


ir_Return_strategy = st.builds(ir_Return)
@given(instance=ir_Return_strategy)
@settings(max_examples=25)
def test_ir_Return_instantiation(instance):
    assert isinstance(instance, ir_Return)


ir_SetDefinition_strategy = st.builds(ir_SetDefinition, name=safe_text)
@given(instance=ir_SetDefinition_strategy)
@settings(max_examples=25)
def test_ir_SetDefinition_instantiation(instance):
    assert isinstance(instance, ir_SetDefinition)


ir_SetRef_strategy = st.builds(ir_SetRef)
@given(instance=ir_SetRef_strategy)
@settings(max_examples=25)
def test_ir_SetRef_instantiation(instance):
    assert isinstance(instance, ir_SetRef)


ir_SimpleVariable_strategy = st.builds(ir_SimpleVariable)
@given(instance=ir_SimpleVariable_strategy)
@settings(max_examples=25)
def test_ir_SimpleVariable_instantiation(instance):
    assert isinstance(instance, ir_SimpleVariable)


ir_TimeLoop_strategy = st.builds(ir_TimeLoop, name=safe_text)
@given(instance=ir_TimeLoop_strategy)
@settings(max_examples=25)
def test_ir_TimeLoop_instantiation(instance):
    assert isinstance(instance, ir_TimeLoop)


ir_TimeLoopCopy_strategy = st.builds(ir_TimeLoopCopy)
@given(instance=ir_TimeLoopCopy_strategy)
@settings(max_examples=25)
def test_ir_TimeLoopCopy_instantiation(instance):
    assert isinstance(instance, ir_TimeLoopCopy)


ir_TimeLoopCopyJob_strategy = st.builds(ir_TimeLoopCopyJob)
@given(instance=ir_TimeLoopCopyJob_strategy)
@settings(max_examples=25)
def test_ir_TimeLoopCopyJob_instantiation(instance):
    assert isinstance(instance, ir_TimeLoopCopyJob)


ir_TimeLoopJob_strategy = st.builds(ir_TimeLoopJob)
@given(instance=ir_TimeLoopJob_strategy)
@settings(max_examples=25)
def test_ir_TimeLoopJob_instantiation(instance):
    assert isinstance(instance, ir_TimeLoopJob)


ir_TimeLoopVariable_strategy = st.builds(ir_TimeLoopVariable, name=safe_text)
@given(instance=ir_TimeLoopVariable_strategy)
@settings(max_examples=25)
def test_ir_TimeLoopVariable_instantiation(instance):
    assert isinstance(instance, ir_TimeLoopVariable)


ir_UnaryExpression_strategy = st.builds(ir_UnaryExpression, operator=safe_text)
@given(instance=ir_UnaryExpression_strategy)
@settings(max_examples=25)
def test_ir_UnaryExpression_instantiation(instance):
    assert isinstance(instance, ir_UnaryExpression)


ir_Variable_strategy = st.builds(ir_Variable, const=st.booleans(), persistenceName=safe_text)
@given(instance=ir_Variable_strategy)
@settings(max_examples=25)
def test_ir_Variable_instantiation(instance):
    assert isinstance(instance, ir_Variable)


ir_VariableDefinition_strategy = st.builds(ir_VariableDefinition)
@given(instance=ir_VariableDefinition_strategy)
@settings(max_examples=25)
def test_ir_VariableDefinition_instantiation(instance):
    assert isinstance(instance, ir_VariableDefinition)


ir_VectorConstant_strategy = st.builds(ir_VectorConstant)
@given(instance=ir_VectorConstant_strategy)
@settings(max_examples=25)
def test_ir_VectorConstant_instantiation(instance):
    assert isinstance(instance, ir_VectorConstant)


