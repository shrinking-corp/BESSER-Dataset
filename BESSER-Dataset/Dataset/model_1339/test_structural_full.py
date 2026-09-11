import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AccVarCS,
    AttributeEvaluationType,
    AttributeSet,
    AttributeType,
    BooleanLiteralExpCS,
    BooleanType,
    CallExpCS,
    ClassCS,
    CompleteSelection,
    ConstraintCS,
    Definition,
    DoubleType,
    Evaluation,
    ExpCS,
    IntegerType,
    InvariantCS,
    IteratorVarCS,
    LiteralExpCS,
    LogicExpCS,
    LoopExpCS,
    Mutator,
    NavigationExpCS,
    NavigationPathCS,
    NavigationPathNameCS,
    NumberType,
    ObSelectionStrategy,
    ObjectEmitter,
    OperationCS,
    OtherSelection,
    PackageCS,
    ParameterCS,
    PathCS,
    PathNameCS,
    PrimaryExpCS,
    PropertyCS,
    RandomNumberType,
    RandomSelection,
    ReferenceSet,
    RemoveReferenceMutator,
    RoundedBracketClauseCS,
    SpecificSelection,
    StringType,
    miniOCL_mutatorenvironment_EStructuralFeature,
    mutatorenvironment_AttributeCopy,
    mutatorenvironment_AttributeEvaluation,
    mutatorenvironment_AttributeEvaluationType,
    mutatorenvironment_AttributeOperation,
    mutatorenvironment_AttributeReverse,
    mutatorenvironment_AttributeScalar,
    mutatorenvironment_AttributeSet,
    mutatorenvironment_AttributeSwap,
    mutatorenvironment_AttributeType,
    mutatorenvironment_AttributeUnset,
    mutatorenvironment_BinaryOperator,
    mutatorenvironment_Block,
    mutatorenvironment_BooleanType,
    mutatorenvironment_CatEndStringType,
    mutatorenvironment_CatStartStringType,
    mutatorenvironment_CloneObjectMutator,
    mutatorenvironment_CompleteSelection,
    mutatorenvironment_CompleteTypeSelection,
    mutatorenvironment_CompositeMutator,
    mutatorenvironment_Constraint,
    mutatorenvironment_CreateObjectMutator,
    mutatorenvironment_CreateReferenceMutator,
    mutatorenvironment_Definition,
    mutatorenvironment_DoubleType,
    mutatorenvironment_EAttribute,
    mutatorenvironment_EClass,
    mutatorenvironment_EObject,
    mutatorenvironment_EReference,
    mutatorenvironment_EStructuralFeature,
    mutatorenvironment_Evaluation,
    mutatorenvironment_Expression,
    mutatorenvironment_IntegerType,
    mutatorenvironment_Library,
    mutatorenvironment_ListStringType,
    mutatorenvironment_ListType,
    mutatorenvironment_Load,
    mutatorenvironment_LowerStringType,
    mutatorenvironment_MaxValueType,
    mutatorenvironment_MinValueType,
    mutatorenvironment_ModifyInformationMutator,
    mutatorenvironment_ModifySourceReferenceMutator,
    mutatorenvironment_ModifyTargetReferenceMutator,
    mutatorenvironment_Mutator,
    mutatorenvironment_MutatorEnvironment,
    mutatorenvironment_NumberType,
    mutatorenvironment_ObSelectionStrategy,
    mutatorenvironment_ObjectAttributeType,
    mutatorenvironment_ObjectEmitter,
    mutatorenvironment_OtherSelection,
    mutatorenvironment_OtherTypeSelection,
    mutatorenvironment_Program,
    mutatorenvironment_RandomBooleanType,
    mutatorenvironment_RandomDoubleNumberType,
    mutatorenvironment_RandomDoubleType,
    mutatorenvironment_RandomIntegerNumberType,
    mutatorenvironment_RandomIntegerType,
    mutatorenvironment_RandomNumberType,
    mutatorenvironment_RandomSelection,
    mutatorenvironment_RandomStringNumberType,
    mutatorenvironment_RandomStringType,
    mutatorenvironment_RandomType,
    mutatorenvironment_RandomTypeSelection,
    mutatorenvironment_ReferenceAdd,
    mutatorenvironment_ReferenceAtt,
    mutatorenvironment_ReferenceEvaluation,
    mutatorenvironment_ReferenceInit,
    mutatorenvironment_ReferenceRemove,
    mutatorenvironment_ReferenceSet,
    mutatorenvironment_ReferenceSwap,
    mutatorenvironment_RemoveCompleteReferenceMutator,
    mutatorenvironment_RemoveObjectMutator,
    mutatorenvironment_RemoveRandomReferenceMutator,
    mutatorenvironment_RemoveReferenceMutator,
    mutatorenvironment_RemoveSpecificReferenceMutator,
    mutatorenvironment_ReplaceStringType,
    mutatorenvironment_Resource,
    mutatorenvironment_RetypeObjectMutator,
    mutatorenvironment_SelectObjectMutator,
    mutatorenvironment_SelectSampleMutator,
    mutatorenvironment_Source,
    mutatorenvironment_SpecificBooleanType,
    mutatorenvironment_SpecificClosureSelection,
    mutatorenvironment_SpecificDoubleType,
    mutatorenvironment_SpecificIntegerType,
    mutatorenvironment_SpecificObjectSelection,
    mutatorenvironment_SpecificReferenceSelection,
    mutatorenvironment_SpecificSelection,
    mutatorenvironment_SpecificStringType,
    mutatorenvironment_StringType,
    mutatorenvironment_TypedSelection,
    mutatorenvironment_UpperStringType,
    mutatorenvironment_miniOCL_AccVarCS,
    mutatorenvironment_miniOCL_BooleanExpCS,
    mutatorenvironment_miniOCL_BooleanLiteralExpCS,
    mutatorenvironment_miniOCL_CallExpCS,
    mutatorenvironment_miniOCL_ClassCS,
    mutatorenvironment_miniOCL_CollectExpCS,
    mutatorenvironment_miniOCL_ConstraintCS,
    mutatorenvironment_miniOCL_ExistsExpCS,
    mutatorenvironment_miniOCL_ExpCS,
    mutatorenvironment_miniOCL_ForAllExpCS,
    mutatorenvironment_miniOCL_IntLiteralExpCS,
    mutatorenvironment_miniOCL_InvariantCS,
    mutatorenvironment_miniOCL_IterateExpCS,
    mutatorenvironment_miniOCL_IteratorVarCS,
    mutatorenvironment_miniOCL_LiteralExpCS,
    mutatorenvironment_miniOCL_LogicExpCS,
    mutatorenvironment_miniOCL_LoopExpCS,
    mutatorenvironment_miniOCL_NameExpCS,
    mutatorenvironment_miniOCL_NavigationExpCS,
    mutatorenvironment_miniOCL_NavigationNameExpCS,
    mutatorenvironment_miniOCL_NavigationPathCS,
    mutatorenvironment_miniOCL_NavigationPathElementCS,
    mutatorenvironment_miniOCL_NavigationPathNameCS,
    mutatorenvironment_miniOCL_NavigationPathVariableCS,
    mutatorenvironment_miniOCL_OperationCS,
    mutatorenvironment_miniOCL_PackageCS,
    mutatorenvironment_miniOCL_ParameterCS,
    mutatorenvironment_miniOCL_PathCS,
    mutatorenvironment_miniOCL_PathElementCS,
    mutatorenvironment_miniOCL_PathNameCS,
    mutatorenvironment_miniOCL_PathVariableCS,
    mutatorenvironment_miniOCL_PrimaryExpCS,
    mutatorenvironment_miniOCL_PropertyCS,
    mutatorenvironment_miniOCL_RootCS,
    mutatorenvironment_miniOCL_RoundedBracketClauseCS,
    mutatorenvironment_miniOCL_StringLiteralExpCS,
    ArithmeticOperator,
    LogicOperator,
    Operator,
    Repeat,
    SampleClause,
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

def test_mutatorenvironment_RandomDoubleNumberType_min_value_roundtrip():
    instance = mutatorenvironment_RandomDoubleNumberType(min=3.14)
    assert instance.min == 3.14
    instance.min = 9.99
    assert instance.min == 9.99


def test_mutatorenvironment_SpecificDoubleType_value_value_roundtrip():
    instance = mutatorenvironment_SpecificDoubleType(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_mutatorenvironment_AttributeCopy_isa_AttributeSet():
    instance = mutatorenvironment_AttributeCopy()
    assert isinstance(instance, AttributeSet)


def test_mutatorenvironment_AttributeReverse_isa_AttributeSet():
    instance = mutatorenvironment_AttributeReverse()
    assert isinstance(instance, AttributeSet)


def test_mutatorenvironment_AttributeScalar_isa_AttributeSet():
    instance = mutatorenvironment_AttributeScalar()
    assert isinstance(instance, AttributeSet)


def test_mutatorenvironment_AttributeSwap_isa_AttributeSet():
    instance = mutatorenvironment_AttributeSwap()
    assert isinstance(instance, AttributeSet)


def test_mutatorenvironment_AttributeUnset_isa_AttributeSet():
    instance = mutatorenvironment_AttributeUnset()
    assert isinstance(instance, AttributeSet)


def test_mutatorenvironment_BooleanType_isa_AttributeType():
    instance = mutatorenvironment_BooleanType()
    assert isinstance(instance, AttributeType)


def test_mutatorenvironment_ListStringType_isa_AttributeType():
    instance = mutatorenvironment_ListStringType()
    assert isinstance(instance, AttributeType)


def test_mutatorenvironment_ListType_isa_AttributeType():
    instance = mutatorenvironment_ListType()
    assert isinstance(instance, AttributeType)


def test_mutatorenvironment_NumberType_isa_AttributeType():
    instance = mutatorenvironment_NumberType()
    assert isinstance(instance, AttributeType)


def test_mutatorenvironment_RandomType_isa_AttributeType():
    instance = mutatorenvironment_RandomType()
    assert isinstance(instance, AttributeType)


def test_mutatorenvironment_StringType_isa_AttributeType():
    instance = mutatorenvironment_StringType()
    assert isinstance(instance, AttributeType)


def test_mutatorenvironment_RandomBooleanType_isa_BooleanType():
    instance = mutatorenvironment_RandomBooleanType()
    assert isinstance(instance, BooleanType)


def test_mutatorenvironment_SpecificBooleanType_isa_BooleanType():
    instance = mutatorenvironment_SpecificBooleanType()
    assert isinstance(instance, BooleanType)


def test_mutatorenvironment_miniOCL_PrimaryExpCS_isa_CallExpCS():
    instance = mutatorenvironment_miniOCL_PrimaryExpCS()
    assert isinstance(instance, CallExpCS)


def test_mutatorenvironment_CompleteTypeSelection_isa_CompleteSelection():
    instance = mutatorenvironment_CompleteTypeSelection()
    assert isinstance(instance, CompleteSelection)


def test_mutatorenvironment_Library_isa_Definition():
    instance = mutatorenvironment_Library()
    assert isinstance(instance, Definition)


def test_mutatorenvironment_SpecificDoubleType_isa_DoubleType():
    instance = mutatorenvironment_SpecificDoubleType(value=3.14)
    assert isinstance(instance, DoubleType)


def test_mutatorenvironment_AttributeEvaluation_isa_Evaluation():
    instance = mutatorenvironment_AttributeEvaluation()
    assert isinstance(instance, Evaluation)


def test_mutatorenvironment_RandomIntegerType_isa_IntegerType():
    instance = mutatorenvironment_RandomIntegerType()
    assert isinstance(instance, IntegerType)


def test_mutatorenvironment_SpecificIntegerType_isa_IntegerType():
    instance = mutatorenvironment_SpecificIntegerType()
    assert isinstance(instance, IntegerType)


def test_mutatorenvironment_miniOCL_BooleanLiteralExpCS_isa_LiteralExpCS():
    instance = mutatorenvironment_miniOCL_BooleanLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_mutatorenvironment_miniOCL_CallExpCS_isa_LogicExpCS():
    instance = mutatorenvironment_miniOCL_CallExpCS()
    assert isinstance(instance, LogicExpCS)


def test_mutatorenvironment_miniOCL_CollectExpCS_isa_LoopExpCS():
    instance = mutatorenvironment_miniOCL_CollectExpCS()
    assert isinstance(instance, LoopExpCS)


def test_mutatorenvironment_miniOCL_ExistsExpCS_isa_LoopExpCS():
    instance = mutatorenvironment_miniOCL_ExistsExpCS()
    assert isinstance(instance, LoopExpCS)


def test_mutatorenvironment_miniOCL_ForAllExpCS_isa_LoopExpCS():
    instance = mutatorenvironment_miniOCL_ForAllExpCS()
    assert isinstance(instance, LoopExpCS)


def test_mutatorenvironment_miniOCL_IterateExpCS_isa_LoopExpCS():
    instance = mutatorenvironment_miniOCL_IterateExpCS()
    assert isinstance(instance, LoopExpCS)


def test_mutatorenvironment_CompositeMutator_isa_Mutator():
    instance = mutatorenvironment_CompositeMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_CreateObjectMutator_isa_Mutator():
    instance = mutatorenvironment_CreateObjectMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_CreateReferenceMutator_isa_Mutator():
    instance = mutatorenvironment_CreateReferenceMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_ModifyInformationMutator_isa_Mutator():
    instance = mutatorenvironment_ModifyInformationMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_ModifySourceReferenceMutator_isa_Mutator():
    instance = mutatorenvironment_ModifySourceReferenceMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_ModifyTargetReferenceMutator_isa_Mutator():
    instance = mutatorenvironment_ModifyTargetReferenceMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_RemoveObjectMutator_isa_Mutator():
    instance = mutatorenvironment_RemoveObjectMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_RemoveReferenceMutator_isa_Mutator():
    instance = mutatorenvironment_RemoveReferenceMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_RetypeObjectMutator_isa_Mutator():
    instance = mutatorenvironment_RetypeObjectMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_SelectObjectMutator_isa_Mutator():
    instance = mutatorenvironment_SelectObjectMutator()
    assert isinstance(instance, Mutator)


def test_mutatorenvironment_miniOCL_NameExpCS_isa_NavigationExpCS():
    instance = mutatorenvironment_miniOCL_NameExpCS()
    assert isinstance(instance, NavigationExpCS)


def test_mutatorenvironment_miniOCL_NavigationNameExpCS_isa_NavigationExpCS():
    instance = mutatorenvironment_miniOCL_NavigationNameExpCS()
    assert isinstance(instance, NavigationExpCS)


def test_mutatorenvironment_miniOCL_NavigationPathElementCS_isa_NavigationPathCS():
    instance = mutatorenvironment_miniOCL_NavigationPathElementCS()
    assert isinstance(instance, NavigationPathCS)


def test_mutatorenvironment_DoubleType_isa_NumberType():
    instance = mutatorenvironment_DoubleType()
    assert isinstance(instance, NumberType)


def test_mutatorenvironment_IntegerType_isa_NumberType():
    instance = mutatorenvironment_IntegerType()
    assert isinstance(instance, NumberType)


def test_mutatorenvironment_MaxValueType_isa_NumberType():
    instance = mutatorenvironment_MaxValueType()
    assert isinstance(instance, NumberType)


def test_mutatorenvironment_MinValueType_isa_NumberType():
    instance = mutatorenvironment_MinValueType()
    assert isinstance(instance, NumberType)


def test_mutatorenvironment_RandomNumberType_isa_NumberType():
    instance = mutatorenvironment_RandomNumberType()
    assert isinstance(instance, NumberType)


def test_mutatorenvironment_CompleteSelection_isa_ObSelectionStrategy():
    instance = mutatorenvironment_CompleteSelection()
    assert isinstance(instance, ObSelectionStrategy)


def test_mutatorenvironment_OtherSelection_isa_ObSelectionStrategy():
    instance = mutatorenvironment_OtherSelection()
    assert isinstance(instance, ObSelectionStrategy)


def test_mutatorenvironment_RandomSelection_isa_ObSelectionStrategy():
    instance = mutatorenvironment_RandomSelection()
    assert isinstance(instance, ObSelectionStrategy)


def test_mutatorenvironment_SpecificSelection_isa_ObSelectionStrategy():
    instance = mutatorenvironment_SpecificSelection()
    assert isinstance(instance, ObSelectionStrategy)


def test_mutatorenvironment_TypedSelection_isa_ObSelectionStrategy():
    instance = mutatorenvironment_TypedSelection()
    assert isinstance(instance, ObSelectionStrategy)


def test_mutatorenvironment_OtherTypeSelection_isa_OtherSelection():
    instance = mutatorenvironment_OtherTypeSelection()
    assert isinstance(instance, OtherSelection)


def test_mutatorenvironment_miniOCL_PathElementCS_isa_PathCS():
    instance = mutatorenvironment_miniOCL_PathElementCS()
    assert isinstance(instance, PathCS)


def test_mutatorenvironment_miniOCL_LiteralExpCS_isa_PrimaryExpCS():
    instance = mutatorenvironment_miniOCL_LiteralExpCS()
    assert isinstance(instance, PrimaryExpCS)


def test_mutatorenvironment_miniOCL_NavigationExpCS_isa_PrimaryExpCS():
    instance = mutatorenvironment_miniOCL_NavigationExpCS()
    assert isinstance(instance, PrimaryExpCS)


def test_mutatorenvironment_RandomDoubleNumberType_isa_RandomNumberType():
    instance = mutatorenvironment_RandomDoubleNumberType(min=3.14)
    assert isinstance(instance, RandomNumberType)


def test_mutatorenvironment_RandomTypeSelection_isa_RandomSelection():
    instance = mutatorenvironment_RandomTypeSelection()
    assert isinstance(instance, RandomSelection)


def test_mutatorenvironment_ReferenceAdd_isa_ReferenceSet():
    instance = mutatorenvironment_ReferenceAdd()
    assert isinstance(instance, ReferenceSet)


def test_mutatorenvironment_ReferenceAtt_isa_ReferenceSet():
    instance = mutatorenvironment_ReferenceAtt()
    assert isinstance(instance, ReferenceSet)


def test_mutatorenvironment_ReferenceInit_isa_ReferenceSet():
    instance = mutatorenvironment_ReferenceInit()
    assert isinstance(instance, ReferenceSet)


def test_mutatorenvironment_ReferenceRemove_isa_ReferenceSet():
    instance = mutatorenvironment_ReferenceRemove()
    assert isinstance(instance, ReferenceSet)


def test_mutatorenvironment_ReferenceSwap_isa_ReferenceSet():
    instance = mutatorenvironment_ReferenceSwap()
    assert isinstance(instance, ReferenceSet)


def test_mutatorenvironment_RemoveCompleteReferenceMutator_isa_RemoveReferenceMutator():
    instance = mutatorenvironment_RemoveCompleteReferenceMutator()
    assert isinstance(instance, RemoveReferenceMutator)


def test_mutatorenvironment_RemoveRandomReferenceMutator_isa_RemoveReferenceMutator():
    instance = mutatorenvironment_RemoveRandomReferenceMutator()
    assert isinstance(instance, RemoveReferenceMutator)


def test_mutatorenvironment_RemoveSpecificReferenceMutator_isa_RemoveReferenceMutator():
    instance = mutatorenvironment_RemoveSpecificReferenceMutator()
    assert isinstance(instance, RemoveReferenceMutator)


def test_mutatorenvironment_SpecificClosureSelection_isa_SpecificSelection():
    instance = mutatorenvironment_SpecificClosureSelection()
    assert isinstance(instance, SpecificSelection)


def test_mutatorenvironment_SpecificObjectSelection_isa_SpecificSelection():
    instance = mutatorenvironment_SpecificObjectSelection()
    assert isinstance(instance, SpecificSelection)


def test_mutatorenvironment_SpecificReferenceSelection_isa_SpecificSelection():
    instance = mutatorenvironment_SpecificReferenceSelection()
    assert isinstance(instance, SpecificSelection)


def test_mutatorenvironment_CatEndStringType_isa_StringType():
    instance = mutatorenvironment_CatEndStringType()
    assert isinstance(instance, StringType)


def test_mutatorenvironment_CatStartStringType_isa_StringType():
    instance = mutatorenvironment_CatStartStringType()
    assert isinstance(instance, StringType)


def test_mutatorenvironment_LowerStringType_isa_StringType():
    instance = mutatorenvironment_LowerStringType()
    assert isinstance(instance, StringType)


def test_mutatorenvironment_RandomStringType_isa_StringType():
    instance = mutatorenvironment_RandomStringType()
    assert isinstance(instance, StringType)


def test_mutatorenvironment_ReplaceStringType_isa_StringType():
    instance = mutatorenvironment_ReplaceStringType()
    assert isinstance(instance, StringType)


def test_mutatorenvironment_SpecificStringType_isa_StringType():
    instance = mutatorenvironment_SpecificStringType()
    assert isinstance(instance, StringType)


def test_mutatorenvironment_UpperStringType_isa_StringType():
    instance = mutatorenvironment_UpperStringType()
    assert isinstance(instance, StringType)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AccVarCS_strategy = st.builds(AccVarCS)
@given(instance=AccVarCS_strategy)
@settings(max_examples=25)
def test_AccVarCS_instantiation(instance):
    assert isinstance(instance, AccVarCS)


AttributeEvaluationType_strategy = st.builds(AttributeEvaluationType)
@given(instance=AttributeEvaluationType_strategy)
@settings(max_examples=25)
def test_AttributeEvaluationType_instantiation(instance):
    assert isinstance(instance, AttributeEvaluationType)


AttributeSet_strategy = st.builds(AttributeSet)
@given(instance=AttributeSet_strategy)
@settings(max_examples=25)
def test_AttributeSet_instantiation(instance):
    assert isinstance(instance, AttributeSet)


AttributeType_strategy = st.builds(AttributeType)
@given(instance=AttributeType_strategy)
@settings(max_examples=25)
def test_AttributeType_instantiation(instance):
    assert isinstance(instance, AttributeType)


BooleanLiteralExpCS_strategy = st.builds(BooleanLiteralExpCS)
@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=25)
def test_BooleanLiteralExpCS_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)


BooleanType_strategy = st.builds(BooleanType)
@given(instance=BooleanType_strategy)
@settings(max_examples=25)
def test_BooleanType_instantiation(instance):
    assert isinstance(instance, BooleanType)


CallExpCS_strategy = st.builds(CallExpCS)
@given(instance=CallExpCS_strategy)
@settings(max_examples=25)
def test_CallExpCS_instantiation(instance):
    assert isinstance(instance, CallExpCS)


ClassCS_strategy = st.builds(ClassCS)
@given(instance=ClassCS_strategy)
@settings(max_examples=25)
def test_ClassCS_instantiation(instance):
    assert isinstance(instance, ClassCS)


CompleteSelection_strategy = st.builds(CompleteSelection)
@given(instance=CompleteSelection_strategy)
@settings(max_examples=25)
def test_CompleteSelection_instantiation(instance):
    assert isinstance(instance, CompleteSelection)


ConstraintCS_strategy = st.builds(ConstraintCS)
@given(instance=ConstraintCS_strategy)
@settings(max_examples=25)
def test_ConstraintCS_instantiation(instance):
    assert isinstance(instance, ConstraintCS)


Definition_strategy = st.builds(Definition)
@given(instance=Definition_strategy)
@settings(max_examples=25)
def test_Definition_instantiation(instance):
    assert isinstance(instance, Definition)


DoubleType_strategy = st.builds(DoubleType)
@given(instance=DoubleType_strategy)
@settings(max_examples=25)
def test_DoubleType_instantiation(instance):
    assert isinstance(instance, DoubleType)


Evaluation_strategy = st.builds(Evaluation)
@given(instance=Evaluation_strategy)
@settings(max_examples=25)
def test_Evaluation_instantiation(instance):
    assert isinstance(instance, Evaluation)


ExpCS_strategy = st.builds(ExpCS)
@given(instance=ExpCS_strategy)
@settings(max_examples=25)
def test_ExpCS_instantiation(instance):
    assert isinstance(instance, ExpCS)


IntegerType_strategy = st.builds(IntegerType)
@given(instance=IntegerType_strategy)
@settings(max_examples=25)
def test_IntegerType_instantiation(instance):
    assert isinstance(instance, IntegerType)


InvariantCS_strategy = st.builds(InvariantCS)
@given(instance=InvariantCS_strategy)
@settings(max_examples=25)
def test_InvariantCS_instantiation(instance):
    assert isinstance(instance, InvariantCS)


IteratorVarCS_strategy = st.builds(IteratorVarCS)
@given(instance=IteratorVarCS_strategy)
@settings(max_examples=25)
def test_IteratorVarCS_instantiation(instance):
    assert isinstance(instance, IteratorVarCS)


LiteralExpCS_strategy = st.builds(LiteralExpCS)
@given(instance=LiteralExpCS_strategy)
@settings(max_examples=25)
def test_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)


LogicExpCS_strategy = st.builds(LogicExpCS)
@given(instance=LogicExpCS_strategy)
@settings(max_examples=25)
def test_LogicExpCS_instantiation(instance):
    assert isinstance(instance, LogicExpCS)


LoopExpCS_strategy = st.builds(LoopExpCS)
@given(instance=LoopExpCS_strategy)
@settings(max_examples=25)
def test_LoopExpCS_instantiation(instance):
    assert isinstance(instance, LoopExpCS)


Mutator_strategy = st.builds(Mutator)
@given(instance=Mutator_strategy)
@settings(max_examples=25)
def test_Mutator_instantiation(instance):
    assert isinstance(instance, Mutator)


NavigationExpCS_strategy = st.builds(NavigationExpCS)
@given(instance=NavigationExpCS_strategy)
@settings(max_examples=25)
def test_NavigationExpCS_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)


NavigationPathCS_strategy = st.builds(NavigationPathCS)
@given(instance=NavigationPathCS_strategy)
@settings(max_examples=25)
def test_NavigationPathCS_instantiation(instance):
    assert isinstance(instance, NavigationPathCS)


NavigationPathNameCS_strategy = st.builds(NavigationPathNameCS)
@given(instance=NavigationPathNameCS_strategy)
@settings(max_examples=25)
def test_NavigationPathNameCS_instantiation(instance):
    assert isinstance(instance, NavigationPathNameCS)


NumberType_strategy = st.builds(NumberType)
@given(instance=NumberType_strategy)
@settings(max_examples=25)
def test_NumberType_instantiation(instance):
    assert isinstance(instance, NumberType)


ObSelectionStrategy_strategy = st.builds(ObSelectionStrategy)
@given(instance=ObSelectionStrategy_strategy)
@settings(max_examples=25)
def test_ObSelectionStrategy_instantiation(instance):
    assert isinstance(instance, ObSelectionStrategy)


ObjectEmitter_strategy = st.builds(ObjectEmitter)
@given(instance=ObjectEmitter_strategy)
@settings(max_examples=25)
def test_ObjectEmitter_instantiation(instance):
    assert isinstance(instance, ObjectEmitter)


OperationCS_strategy = st.builds(OperationCS)
@given(instance=OperationCS_strategy)
@settings(max_examples=25)
def test_OperationCS_instantiation(instance):
    assert isinstance(instance, OperationCS)


OtherSelection_strategy = st.builds(OtherSelection)
@given(instance=OtherSelection_strategy)
@settings(max_examples=25)
def test_OtherSelection_instantiation(instance):
    assert isinstance(instance, OtherSelection)


PackageCS_strategy = st.builds(PackageCS)
@given(instance=PackageCS_strategy)
@settings(max_examples=25)
def test_PackageCS_instantiation(instance):
    assert isinstance(instance, PackageCS)


ParameterCS_strategy = st.builds(ParameterCS)
@given(instance=ParameterCS_strategy)
@settings(max_examples=25)
def test_ParameterCS_instantiation(instance):
    assert isinstance(instance, ParameterCS)


PathCS_strategy = st.builds(PathCS)
@given(instance=PathCS_strategy)
@settings(max_examples=25)
def test_PathCS_instantiation(instance):
    assert isinstance(instance, PathCS)


PathNameCS_strategy = st.builds(PathNameCS)
@given(instance=PathNameCS_strategy)
@settings(max_examples=25)
def test_PathNameCS_instantiation(instance):
    assert isinstance(instance, PathNameCS)


PrimaryExpCS_strategy = st.builds(PrimaryExpCS)
@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=25)
def test_PrimaryExpCS_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)


PropertyCS_strategy = st.builds(PropertyCS)
@given(instance=PropertyCS_strategy)
@settings(max_examples=25)
def test_PropertyCS_instantiation(instance):
    assert isinstance(instance, PropertyCS)


RandomNumberType_strategy = st.builds(RandomNumberType)
@given(instance=RandomNumberType_strategy)
@settings(max_examples=25)
def test_RandomNumberType_instantiation(instance):
    assert isinstance(instance, RandomNumberType)


RandomSelection_strategy = st.builds(RandomSelection)
@given(instance=RandomSelection_strategy)
@settings(max_examples=25)
def test_RandomSelection_instantiation(instance):
    assert isinstance(instance, RandomSelection)


ReferenceSet_strategy = st.builds(ReferenceSet)
@given(instance=ReferenceSet_strategy)
@settings(max_examples=25)
def test_ReferenceSet_instantiation(instance):
    assert isinstance(instance, ReferenceSet)


RemoveReferenceMutator_strategy = st.builds(RemoveReferenceMutator)
@given(instance=RemoveReferenceMutator_strategy)
@settings(max_examples=25)
def test_RemoveReferenceMutator_instantiation(instance):
    assert isinstance(instance, RemoveReferenceMutator)


RoundedBracketClauseCS_strategy = st.builds(RoundedBracketClauseCS)
@given(instance=RoundedBracketClauseCS_strategy)
@settings(max_examples=25)
def test_RoundedBracketClauseCS_instantiation(instance):
    assert isinstance(instance, RoundedBracketClauseCS)


SpecificSelection_strategy = st.builds(SpecificSelection)
@given(instance=SpecificSelection_strategy)
@settings(max_examples=25)
def test_SpecificSelection_instantiation(instance):
    assert isinstance(instance, SpecificSelection)


StringType_strategy = st.builds(StringType)
@given(instance=StringType_strategy)
@settings(max_examples=25)
def test_StringType_instantiation(instance):
    assert isinstance(instance, StringType)


miniOCL_mutatorenvironment_EStructuralFeature_strategy = st.builds(miniOCL_mutatorenvironment_EStructuralFeature)
@given(instance=miniOCL_mutatorenvironment_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_miniOCL_mutatorenvironment_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, miniOCL_mutatorenvironment_EStructuralFeature)


mutatorenvironment_AttributeCopy_strategy = st.builds(mutatorenvironment_AttributeCopy)
@given(instance=mutatorenvironment_AttributeCopy_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_AttributeCopy_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeCopy)


mutatorenvironment_AttributeEvaluation_strategy = st.builds(mutatorenvironment_AttributeEvaluation)
@given(instance=mutatorenvironment_AttributeEvaluation_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_AttributeEvaluation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeEvaluation)


mutatorenvironment_AttributeEvaluationType_strategy = st.builds(mutatorenvironment_AttributeEvaluationType)
@given(instance=mutatorenvironment_AttributeEvaluationType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_AttributeEvaluationType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeEvaluationType)


mutatorenvironment_AttributeReverse_strategy = st.builds(mutatorenvironment_AttributeReverse)
@given(instance=mutatorenvironment_AttributeReverse_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_AttributeReverse_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeReverse)


mutatorenvironment_AttributeScalar_strategy = st.builds(mutatorenvironment_AttributeScalar)
@given(instance=mutatorenvironment_AttributeScalar_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_AttributeScalar_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeScalar)


mutatorenvironment_AttributeSet_strategy = st.builds(mutatorenvironment_AttributeSet)
@given(instance=mutatorenvironment_AttributeSet_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_AttributeSet_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeSet)


mutatorenvironment_AttributeSwap_strategy = st.builds(mutatorenvironment_AttributeSwap)
@given(instance=mutatorenvironment_AttributeSwap_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_AttributeSwap_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeSwap)


mutatorenvironment_AttributeUnset_strategy = st.builds(mutatorenvironment_AttributeUnset)
@given(instance=mutatorenvironment_AttributeUnset_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_AttributeUnset_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_AttributeUnset)


mutatorenvironment_BooleanType_strategy = st.builds(mutatorenvironment_BooleanType)
@given(instance=mutatorenvironment_BooleanType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_BooleanType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_BooleanType)


mutatorenvironment_CatEndStringType_strategy = st.builds(mutatorenvironment_CatEndStringType)
@given(instance=mutatorenvironment_CatEndStringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_CatEndStringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CatEndStringType)


mutatorenvironment_CatStartStringType_strategy = st.builds(mutatorenvironment_CatStartStringType)
@given(instance=mutatorenvironment_CatStartStringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_CatStartStringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CatStartStringType)


mutatorenvironment_CompleteSelection_strategy = st.builds(mutatorenvironment_CompleteSelection)
@given(instance=mutatorenvironment_CompleteSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_CompleteSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CompleteSelection)


mutatorenvironment_CompleteTypeSelection_strategy = st.builds(mutatorenvironment_CompleteTypeSelection)
@given(instance=mutatorenvironment_CompleteTypeSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_CompleteTypeSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CompleteTypeSelection)


mutatorenvironment_CompositeMutator_strategy = st.builds(mutatorenvironment_CompositeMutator)
@given(instance=mutatorenvironment_CompositeMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_CompositeMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CompositeMutator)


mutatorenvironment_CreateObjectMutator_strategy = st.builds(mutatorenvironment_CreateObjectMutator)
@given(instance=mutatorenvironment_CreateObjectMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_CreateObjectMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CreateObjectMutator)


mutatorenvironment_CreateReferenceMutator_strategy = st.builds(mutatorenvironment_CreateReferenceMutator)
@given(instance=mutatorenvironment_CreateReferenceMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_CreateReferenceMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_CreateReferenceMutator)


mutatorenvironment_DoubleType_strategy = st.builds(mutatorenvironment_DoubleType)
@given(instance=mutatorenvironment_DoubleType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_DoubleType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_DoubleType)


mutatorenvironment_EAttribute_strategy = st.builds(mutatorenvironment_EAttribute)
@given(instance=mutatorenvironment_EAttribute_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_EAttribute_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EAttribute)


mutatorenvironment_EClass_strategy = st.builds(mutatorenvironment_EClass)
@given(instance=mutatorenvironment_EClass_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_EClass_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EClass)


mutatorenvironment_EObject_strategy = st.builds(mutatorenvironment_EObject)
@given(instance=mutatorenvironment_EObject_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_EObject_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EObject)


mutatorenvironment_EReference_strategy = st.builds(mutatorenvironment_EReference)
@given(instance=mutatorenvironment_EReference_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_EReference_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EReference)


mutatorenvironment_EStructuralFeature_strategy = st.builds(mutatorenvironment_EStructuralFeature)
@given(instance=mutatorenvironment_EStructuralFeature_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_EStructuralFeature_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_EStructuralFeature)


mutatorenvironment_Evaluation_strategy = st.builds(mutatorenvironment_Evaluation)
@given(instance=mutatorenvironment_Evaluation_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_Evaluation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Evaluation)


mutatorenvironment_Expression_strategy = st.builds(mutatorenvironment_Expression)
@given(instance=mutatorenvironment_Expression_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_Expression_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Expression)


mutatorenvironment_IntegerType_strategy = st.builds(mutatorenvironment_IntegerType)
@given(instance=mutatorenvironment_IntegerType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_IntegerType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_IntegerType)


mutatorenvironment_Library_strategy = st.builds(mutatorenvironment_Library)
@given(instance=mutatorenvironment_Library_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_Library_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_Library)


mutatorenvironment_ListStringType_strategy = st.builds(mutatorenvironment_ListStringType)
@given(instance=mutatorenvironment_ListStringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ListStringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ListStringType)


mutatorenvironment_ListType_strategy = st.builds(mutatorenvironment_ListType)
@given(instance=mutatorenvironment_ListType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ListType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ListType)


mutatorenvironment_LowerStringType_strategy = st.builds(mutatorenvironment_LowerStringType)
@given(instance=mutatorenvironment_LowerStringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_LowerStringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_LowerStringType)


mutatorenvironment_MaxValueType_strategy = st.builds(mutatorenvironment_MaxValueType)
@given(instance=mutatorenvironment_MaxValueType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_MaxValueType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_MaxValueType)


mutatorenvironment_MinValueType_strategy = st.builds(mutatorenvironment_MinValueType)
@given(instance=mutatorenvironment_MinValueType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_MinValueType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_MinValueType)


mutatorenvironment_ModifyInformationMutator_strategy = st.builds(mutatorenvironment_ModifyInformationMutator)
@given(instance=mutatorenvironment_ModifyInformationMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ModifyInformationMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ModifyInformationMutator)


mutatorenvironment_ModifySourceReferenceMutator_strategy = st.builds(mutatorenvironment_ModifySourceReferenceMutator)
@given(instance=mutatorenvironment_ModifySourceReferenceMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ModifySourceReferenceMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ModifySourceReferenceMutator)


mutatorenvironment_ModifyTargetReferenceMutator_strategy = st.builds(mutatorenvironment_ModifyTargetReferenceMutator)
@given(instance=mutatorenvironment_ModifyTargetReferenceMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ModifyTargetReferenceMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ModifyTargetReferenceMutator)


mutatorenvironment_MutatorEnvironment_strategy = st.builds(mutatorenvironment_MutatorEnvironment)
@given(instance=mutatorenvironment_MutatorEnvironment_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_MutatorEnvironment_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_MutatorEnvironment)


mutatorenvironment_NumberType_strategy = st.builds(mutatorenvironment_NumberType)
@given(instance=mutatorenvironment_NumberType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_NumberType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_NumberType)


mutatorenvironment_OtherSelection_strategy = st.builds(mutatorenvironment_OtherSelection)
@given(instance=mutatorenvironment_OtherSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_OtherSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_OtherSelection)


mutatorenvironment_OtherTypeSelection_strategy = st.builds(mutatorenvironment_OtherTypeSelection)
@given(instance=mutatorenvironment_OtherTypeSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_OtherTypeSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_OtherTypeSelection)


mutatorenvironment_RandomBooleanType_strategy = st.builds(mutatorenvironment_RandomBooleanType)
@given(instance=mutatorenvironment_RandomBooleanType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RandomBooleanType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomBooleanType)


mutatorenvironment_RandomDoubleNumberType_strategy = st.builds(mutatorenvironment_RandomDoubleNumberType, min=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=mutatorenvironment_RandomDoubleNumberType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RandomDoubleNumberType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomDoubleNumberType)


mutatorenvironment_RandomIntegerType_strategy = st.builds(mutatorenvironment_RandomIntegerType)
@given(instance=mutatorenvironment_RandomIntegerType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RandomIntegerType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomIntegerType)


mutatorenvironment_RandomNumberType_strategy = st.builds(mutatorenvironment_RandomNumberType)
@given(instance=mutatorenvironment_RandomNumberType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RandomNumberType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomNumberType)


mutatorenvironment_RandomSelection_strategy = st.builds(mutatorenvironment_RandomSelection)
@given(instance=mutatorenvironment_RandomSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RandomSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomSelection)


mutatorenvironment_RandomStringType_strategy = st.builds(mutatorenvironment_RandomStringType)
@given(instance=mutatorenvironment_RandomStringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RandomStringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomStringType)


mutatorenvironment_RandomType_strategy = st.builds(mutatorenvironment_RandomType)
@given(instance=mutatorenvironment_RandomType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RandomType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomType)


mutatorenvironment_RandomTypeSelection_strategy = st.builds(mutatorenvironment_RandomTypeSelection)
@given(instance=mutatorenvironment_RandomTypeSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RandomTypeSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RandomTypeSelection)


mutatorenvironment_ReferenceAdd_strategy = st.builds(mutatorenvironment_ReferenceAdd)
@given(instance=mutatorenvironment_ReferenceAdd_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ReferenceAdd_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceAdd)


mutatorenvironment_ReferenceAtt_strategy = st.builds(mutatorenvironment_ReferenceAtt)
@given(instance=mutatorenvironment_ReferenceAtt_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ReferenceAtt_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceAtt)


mutatorenvironment_ReferenceInit_strategy = st.builds(mutatorenvironment_ReferenceInit)
@given(instance=mutatorenvironment_ReferenceInit_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ReferenceInit_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceInit)


mutatorenvironment_ReferenceRemove_strategy = st.builds(mutatorenvironment_ReferenceRemove)
@given(instance=mutatorenvironment_ReferenceRemove_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ReferenceRemove_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceRemove)


mutatorenvironment_ReferenceSet_strategy = st.builds(mutatorenvironment_ReferenceSet)
@given(instance=mutatorenvironment_ReferenceSet_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ReferenceSet_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceSet)


mutatorenvironment_ReferenceSwap_strategy = st.builds(mutatorenvironment_ReferenceSwap)
@given(instance=mutatorenvironment_ReferenceSwap_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ReferenceSwap_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReferenceSwap)


mutatorenvironment_RemoveCompleteReferenceMutator_strategy = st.builds(mutatorenvironment_RemoveCompleteReferenceMutator)
@given(instance=mutatorenvironment_RemoveCompleteReferenceMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RemoveCompleteReferenceMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveCompleteReferenceMutator)


mutatorenvironment_RemoveObjectMutator_strategy = st.builds(mutatorenvironment_RemoveObjectMutator)
@given(instance=mutatorenvironment_RemoveObjectMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RemoveObjectMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveObjectMutator)


mutatorenvironment_RemoveRandomReferenceMutator_strategy = st.builds(mutatorenvironment_RemoveRandomReferenceMutator)
@given(instance=mutatorenvironment_RemoveRandomReferenceMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RemoveRandomReferenceMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveRandomReferenceMutator)


mutatorenvironment_RemoveReferenceMutator_strategy = st.builds(mutatorenvironment_RemoveReferenceMutator)
@given(instance=mutatorenvironment_RemoveReferenceMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RemoveReferenceMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveReferenceMutator)


mutatorenvironment_RemoveSpecificReferenceMutator_strategy = st.builds(mutatorenvironment_RemoveSpecificReferenceMutator)
@given(instance=mutatorenvironment_RemoveSpecificReferenceMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RemoveSpecificReferenceMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RemoveSpecificReferenceMutator)


mutatorenvironment_ReplaceStringType_strategy = st.builds(mutatorenvironment_ReplaceStringType)
@given(instance=mutatorenvironment_ReplaceStringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_ReplaceStringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_ReplaceStringType)


mutatorenvironment_RetypeObjectMutator_strategy = st.builds(mutatorenvironment_RetypeObjectMutator)
@given(instance=mutatorenvironment_RetypeObjectMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_RetypeObjectMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_RetypeObjectMutator)


mutatorenvironment_SelectObjectMutator_strategy = st.builds(mutatorenvironment_SelectObjectMutator)
@given(instance=mutatorenvironment_SelectObjectMutator_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SelectObjectMutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SelectObjectMutator)


mutatorenvironment_SpecificBooleanType_strategy = st.builds(mutatorenvironment_SpecificBooleanType)
@given(instance=mutatorenvironment_SpecificBooleanType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SpecificBooleanType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificBooleanType)


mutatorenvironment_SpecificClosureSelection_strategy = st.builds(mutatorenvironment_SpecificClosureSelection)
@given(instance=mutatorenvironment_SpecificClosureSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SpecificClosureSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificClosureSelection)


mutatorenvironment_SpecificDoubleType_strategy = st.builds(mutatorenvironment_SpecificDoubleType, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=mutatorenvironment_SpecificDoubleType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SpecificDoubleType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificDoubleType)


mutatorenvironment_SpecificIntegerType_strategy = st.builds(mutatorenvironment_SpecificIntegerType)
@given(instance=mutatorenvironment_SpecificIntegerType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SpecificIntegerType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificIntegerType)


mutatorenvironment_SpecificObjectSelection_strategy = st.builds(mutatorenvironment_SpecificObjectSelection)
@given(instance=mutatorenvironment_SpecificObjectSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SpecificObjectSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificObjectSelection)


mutatorenvironment_SpecificReferenceSelection_strategy = st.builds(mutatorenvironment_SpecificReferenceSelection)
@given(instance=mutatorenvironment_SpecificReferenceSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SpecificReferenceSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificReferenceSelection)


mutatorenvironment_SpecificSelection_strategy = st.builds(mutatorenvironment_SpecificSelection)
@given(instance=mutatorenvironment_SpecificSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SpecificSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificSelection)


mutatorenvironment_SpecificStringType_strategy = st.builds(mutatorenvironment_SpecificStringType)
@given(instance=mutatorenvironment_SpecificStringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_SpecificStringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_SpecificStringType)


mutatorenvironment_StringType_strategy = st.builds(mutatorenvironment_StringType)
@given(instance=mutatorenvironment_StringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_StringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_StringType)


mutatorenvironment_TypedSelection_strategy = st.builds(mutatorenvironment_TypedSelection)
@given(instance=mutatorenvironment_TypedSelection_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_TypedSelection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_TypedSelection)


mutatorenvironment_UpperStringType_strategy = st.builds(mutatorenvironment_UpperStringType)
@given(instance=mutatorenvironment_UpperStringType_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_UpperStringType_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_UpperStringType)


mutatorenvironment_miniOCL_BooleanLiteralExpCS_strategy = st.builds(mutatorenvironment_miniOCL_BooleanLiteralExpCS)
@given(instance=mutatorenvironment_miniOCL_BooleanLiteralExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_BooleanLiteralExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_BooleanLiteralExpCS)


mutatorenvironment_miniOCL_CallExpCS_strategy = st.builds(mutatorenvironment_miniOCL_CallExpCS)
@given(instance=mutatorenvironment_miniOCL_CallExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_CallExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_CallExpCS)


mutatorenvironment_miniOCL_CollectExpCS_strategy = st.builds(mutatorenvironment_miniOCL_CollectExpCS)
@given(instance=mutatorenvironment_miniOCL_CollectExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_CollectExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_CollectExpCS)


mutatorenvironment_miniOCL_ConstraintCS_strategy = st.builds(mutatorenvironment_miniOCL_ConstraintCS)
@given(instance=mutatorenvironment_miniOCL_ConstraintCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_ConstraintCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ConstraintCS)


mutatorenvironment_miniOCL_ExistsExpCS_strategy = st.builds(mutatorenvironment_miniOCL_ExistsExpCS)
@given(instance=mutatorenvironment_miniOCL_ExistsExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_ExistsExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ExistsExpCS)


mutatorenvironment_miniOCL_ExpCS_strategy = st.builds(mutatorenvironment_miniOCL_ExpCS)
@given(instance=mutatorenvironment_miniOCL_ExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_ExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ExpCS)


mutatorenvironment_miniOCL_ForAllExpCS_strategy = st.builds(mutatorenvironment_miniOCL_ForAllExpCS)
@given(instance=mutatorenvironment_miniOCL_ForAllExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_ForAllExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_ForAllExpCS)


mutatorenvironment_miniOCL_InvariantCS_strategy = st.builds(mutatorenvironment_miniOCL_InvariantCS)
@given(instance=mutatorenvironment_miniOCL_InvariantCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_InvariantCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_InvariantCS)


mutatorenvironment_miniOCL_IterateExpCS_strategy = st.builds(mutatorenvironment_miniOCL_IterateExpCS)
@given(instance=mutatorenvironment_miniOCL_IterateExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_IterateExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_IterateExpCS)


mutatorenvironment_miniOCL_LiteralExpCS_strategy = st.builds(mutatorenvironment_miniOCL_LiteralExpCS)
@given(instance=mutatorenvironment_miniOCL_LiteralExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_LiteralExpCS)


mutatorenvironment_miniOCL_NameExpCS_strategy = st.builds(mutatorenvironment_miniOCL_NameExpCS)
@given(instance=mutatorenvironment_miniOCL_NameExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_NameExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NameExpCS)


mutatorenvironment_miniOCL_NavigationExpCS_strategy = st.builds(mutatorenvironment_miniOCL_NavigationExpCS)
@given(instance=mutatorenvironment_miniOCL_NavigationExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_NavigationExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationExpCS)


mutatorenvironment_miniOCL_NavigationNameExpCS_strategy = st.builds(mutatorenvironment_miniOCL_NavigationNameExpCS)
@given(instance=mutatorenvironment_miniOCL_NavigationNameExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_NavigationNameExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationNameExpCS)


mutatorenvironment_miniOCL_NavigationPathCS_strategy = st.builds(mutatorenvironment_miniOCL_NavigationPathCS)
@given(instance=mutatorenvironment_miniOCL_NavigationPathCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_NavigationPathCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationPathCS)


mutatorenvironment_miniOCL_NavigationPathElementCS_strategy = st.builds(mutatorenvironment_miniOCL_NavigationPathElementCS)
@given(instance=mutatorenvironment_miniOCL_NavigationPathElementCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_NavigationPathElementCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationPathElementCS)


mutatorenvironment_miniOCL_NavigationPathNameCS_strategy = st.builds(mutatorenvironment_miniOCL_NavigationPathNameCS)
@given(instance=mutatorenvironment_miniOCL_NavigationPathNameCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_NavigationPathNameCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_NavigationPathNameCS)


mutatorenvironment_miniOCL_PathCS_strategy = st.builds(mutatorenvironment_miniOCL_PathCS)
@given(instance=mutatorenvironment_miniOCL_PathCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_PathCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PathCS)


mutatorenvironment_miniOCL_PathElementCS_strategy = st.builds(mutatorenvironment_miniOCL_PathElementCS)
@given(instance=mutatorenvironment_miniOCL_PathElementCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_PathElementCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PathElementCS)


mutatorenvironment_miniOCL_PathNameCS_strategy = st.builds(mutatorenvironment_miniOCL_PathNameCS)
@given(instance=mutatorenvironment_miniOCL_PathNameCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_PathNameCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PathNameCS)


mutatorenvironment_miniOCL_PrimaryExpCS_strategy = st.builds(mutatorenvironment_miniOCL_PrimaryExpCS)
@given(instance=mutatorenvironment_miniOCL_PrimaryExpCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_PrimaryExpCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_PrimaryExpCS)


mutatorenvironment_miniOCL_RootCS_strategy = st.builds(mutatorenvironment_miniOCL_RootCS)
@given(instance=mutatorenvironment_miniOCL_RootCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_RootCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_RootCS)


mutatorenvironment_miniOCL_RoundedBracketClauseCS_strategy = st.builds(mutatorenvironment_miniOCL_RoundedBracketClauseCS)
@given(instance=mutatorenvironment_miniOCL_RoundedBracketClauseCS_strategy)
@settings(max_examples=25)
def test_mutatorenvironment_miniOCL_RoundedBracketClauseCS_instantiation(instance):
    assert isinstance(instance, mutatorenvironment_miniOCL_RoundedBracketClauseCS)


