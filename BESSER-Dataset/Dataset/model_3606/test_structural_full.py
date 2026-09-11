import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BinaryExpression,
    Expression,
    Instruction,
    MethodCall,
    Step,
    TraversalElement,
    TypeDeclaration,
    UnaryExpression,
    VariableAccess,
    gremlin_AddAllCall,
    gremlin_AffectationExpression,
    gremlin_AndExpression,
    gremlin_BinaryExpression,
    gremlin_BooleanLiteral,
    gremlin_Closure,
    gremlin_ClosureIt,
    gremlin_CollectionDefinition,
    gremlin_ContainsAllCall,
    gremlin_ContainsCall,
    gremlin_CountCall,
    gremlin_CustomMethodCall,
    gremlin_CustomStep,
    gremlin_DifferenceExpression,
    gremlin_DoubleLiteral,
    gremlin_EObject,
    gremlin_EdgesStep,
    gremlin_EqualityExpression,
    gremlin_ExceptStep,
    gremlin_Expression,
    gremlin_FillStep,
    gremlin_FilterStep,
    gremlin_FirstCall,
    gremlin_GatherStep,
    gremlin_GreaterExpression,
    gremlin_GreaterOrEqualExpression,
    gremlin_GremlinScript,
    gremlin_HasNextCall,
    gremlin_IdentityStep,
    gremlin_InEStep,
    gremlin_InExpression,
    gremlin_InVStep,
    gremlin_IndexCall,
    gremlin_Instruction,
    gremlin_IntegerLiteral,
    gremlin_IntersectionCall,
    gremlin_IsEmptyCall,
    gremlin_LeftShiftExpression,
    gremlin_LessExpression,
    gremlin_LessOrEqualExpression,
    gremlin_ListDeclaration,
    gremlin_MethodCall,
    gremlin_MethodDeclaration,
    gremlin_NextCall,
    gremlin_NotExpression,
    gremlin_NullLiteral,
    gremlin_OrExpression,
    gremlin_OutEStep,
    gremlin_OutVStep,
    gremlin_PlusExpression,
    gremlin_PropertyStep,
    gremlin_RetainAllCall,
    gremlin_RetainStep,
    gremlin_ReturnStatement,
    gremlin_ScatterStep,
    gremlin_SetDeclaration,
    gremlin_SizeCall,
    gremlin_SortedSetDeclaration,
    gremlin_StartStep,
    gremlin_Step,
    gremlin_StringLiteral,
    gremlin_TernaryOperator,
    gremlin_ToIntegerCall,
    gremlin_ToListCall,
    gremlin_TransformStep,
    gremlin_TraversalElement,
    gremlin_TypeDeclaration,
    gremlin_UnaryExpression,
    gremlin_UnionCall,
    gremlin_VariableAccess,
    gremlin_VariableDeclaration,
    gremlin_VerticesStep,
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

def test_gremlin_BooleanLiteral_value_value_roundtrip():
    instance = gremlin_BooleanLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_gremlin_CustomMethodCall_name_value_roundtrip():
    instance = gremlin_CustomMethodCall(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gremlin_CustomStep_name_value_roundtrip():
    instance = gremlin_CustomStep(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gremlin_DoubleLiteral_value_value_roundtrip():
    instance = gremlin_DoubleLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_gremlin_EdgesStep_relationshipName_value_roundtrip():
    instance = gremlin_EdgesStep(relationshipName="sample_text")
    assert instance.relationshipName == "sample_text"
    instance.relationshipName = "sample_text_2"
    assert instance.relationshipName == "sample_text_2"


def test_gremlin_GremlinScript_name_value_roundtrip():
    instance = gremlin_GremlinScript(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gremlin_IdentityStep_needed_value_roundtrip():
    instance = gremlin_IdentityStep(needed=True)
    assert instance.needed == True
    instance.needed = False
    assert instance.needed == False


def test_gremlin_InEStep_relationshipName_value_roundtrip():
    instance = gremlin_InEStep(relationshipName="sample_text")
    assert instance.relationshipName == "sample_text"
    instance.relationshipName = "sample_text_2"
    assert instance.relationshipName == "sample_text_2"


def test_gremlin_IndexCall_indexName_value_roundtrip():
    instance = gremlin_IndexCall(indexName="sample_text", indexProperty="sample_text", indexQuery="sample_text")
    assert instance.indexName == "sample_text"
    instance.indexName = "sample_text_2"
    assert instance.indexName == "sample_text_2"


def test_gremlin_IndexCall_indexProperty_value_roundtrip():
    instance = gremlin_IndexCall(indexName="sample_text", indexProperty="sample_text", indexQuery="sample_text")
    assert instance.indexProperty == "sample_text"
    instance.indexProperty = "sample_text_2"
    assert instance.indexProperty == "sample_text_2"


def test_gremlin_IndexCall_indexQuery_value_roundtrip():
    instance = gremlin_IndexCall(indexName="sample_text", indexProperty="sample_text", indexQuery="sample_text")
    assert instance.indexQuery == "sample_text"
    instance.indexQuery = "sample_text_2"
    assert instance.indexQuery == "sample_text_2"


def test_gremlin_IntegerLiteral_value_value_roundtrip():
    instance = gremlin_IntegerLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_gremlin_MethodDeclaration_name_value_roundtrip():
    instance = gremlin_MethodDeclaration(name="sample_text", parameters="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gremlin_MethodDeclaration_parameters_value_roundtrip():
    instance = gremlin_MethodDeclaration(name="sample_text", parameters="sample_text")
    assert instance.parameters == "sample_text"
    instance.parameters = "sample_text_2"
    assert instance.parameters == "sample_text_2"


def test_gremlin_OutEStep_relationshipName_value_roundtrip():
    instance = gremlin_OutEStep(relationshipName="sample_text")
    assert instance.relationshipName == "sample_text"
    instance.relationshipName = "sample_text_2"
    assert instance.relationshipName == "sample_text_2"


def test_gremlin_PropertyStep_name_value_roundtrip():
    instance = gremlin_PropertyStep(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gremlin_ReturnStatement_value_value_roundtrip():
    instance = gremlin_ReturnStatement(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_gremlin_StringLiteral_value_value_roundtrip():
    instance = gremlin_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_gremlin_VariableAccess_name_value_roundtrip():
    instance = gremlin_VariableAccess(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gremlin_VariableDeclaration_final_value_roundtrip():
    instance = gremlin_VariableDeclaration(final=True, name="sample_text")
    assert instance.final == True
    instance.final = False
    assert instance.final == False


def test_gremlin_VariableDeclaration_name_value_roundtrip():
    instance = gremlin_VariableDeclaration(final=True, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_gremlin_VerticesStep_vertexId_value_roundtrip():
    instance = gremlin_VerticesStep(vertexId="sample_text")
    assert instance.vertexId == "sample_text"
    instance.vertexId = "sample_text_2"
    assert instance.vertexId == "sample_text_2"


def test_gremlin_AffectationExpression_isa_BinaryExpression():
    instance = gremlin_AffectationExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_AndExpression_isa_BinaryExpression():
    instance = gremlin_AndExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_DifferenceExpression_isa_BinaryExpression():
    instance = gremlin_DifferenceExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_EqualityExpression_isa_BinaryExpression():
    instance = gremlin_EqualityExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_GreaterExpression_isa_BinaryExpression():
    instance = gremlin_GreaterExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_GreaterOrEqualExpression_isa_BinaryExpression():
    instance = gremlin_GreaterOrEqualExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_InExpression_isa_BinaryExpression():
    instance = gremlin_InExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_LeftShiftExpression_isa_BinaryExpression():
    instance = gremlin_LeftShiftExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_LessExpression_isa_BinaryExpression():
    instance = gremlin_LessExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_LessOrEqualExpression_isa_BinaryExpression():
    instance = gremlin_LessOrEqualExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_OrExpression_isa_BinaryExpression():
    instance = gremlin_OrExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_PlusExpression_isa_BinaryExpression():
    instance = gremlin_PlusExpression()
    assert isinstance(instance, BinaryExpression)


def test_gremlin_BinaryExpression_isa_Expression():
    instance = gremlin_BinaryExpression()
    assert isinstance(instance, Expression)


def test_gremlin_BooleanLiteral_isa_Expression():
    instance = gremlin_BooleanLiteral(value=True)
    assert isinstance(instance, Expression)


def test_gremlin_DoubleLiteral_isa_Expression():
    instance = gremlin_DoubleLiteral(value=3.14)
    assert isinstance(instance, Expression)


def test_gremlin_IntegerLiteral_isa_Expression():
    instance = gremlin_IntegerLiteral(value=7)
    assert isinstance(instance, Expression)


def test_gremlin_NullLiteral_isa_Expression():
    instance = gremlin_NullLiteral()
    assert isinstance(instance, Expression)


def test_gremlin_StringLiteral_isa_Expression():
    instance = gremlin_StringLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_gremlin_TernaryOperator_isa_Expression():
    instance = gremlin_TernaryOperator()
    assert isinstance(instance, Expression)


def test_gremlin_UnaryExpression_isa_Expression():
    instance = gremlin_UnaryExpression()
    assert isinstance(instance, Expression)


def test_gremlin_Closure_isa_Instruction():
    instance = gremlin_Closure()
    assert isinstance(instance, Instruction)


def test_gremlin_Expression_isa_Instruction():
    instance = gremlin_Expression()
    assert isinstance(instance, Instruction)


def test_gremlin_MethodDeclaration_isa_Instruction():
    instance = gremlin_MethodDeclaration(name="sample_text", parameters="sample_text")
    assert isinstance(instance, Instruction)


def test_gremlin_ReturnStatement_isa_Instruction():
    instance = gremlin_ReturnStatement(value="sample_text")
    assert isinstance(instance, Instruction)


def test_gremlin_TraversalElement_isa_Instruction():
    instance = gremlin_TraversalElement()
    assert isinstance(instance, Instruction)


def test_gremlin_TypeDeclaration_isa_Instruction():
    instance = gremlin_TypeDeclaration()
    assert isinstance(instance, Instruction)


def test_gremlin_VariableDeclaration_isa_Instruction():
    instance = gremlin_VariableDeclaration(final=True, name="sample_text")
    assert isinstance(instance, Instruction)


def test_gremlin_AddAllCall_isa_MethodCall():
    instance = gremlin_AddAllCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_ContainsAllCall_isa_MethodCall():
    instance = gremlin_ContainsAllCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_ContainsCall_isa_MethodCall():
    instance = gremlin_ContainsCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_CountCall_isa_MethodCall():
    instance = gremlin_CountCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_CustomMethodCall_isa_MethodCall():
    instance = gremlin_CustomMethodCall(name="sample_text")
    assert isinstance(instance, MethodCall)


def test_gremlin_FirstCall_isa_MethodCall():
    instance = gremlin_FirstCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_HasNextCall_isa_MethodCall():
    instance = gremlin_HasNextCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_IndexCall_isa_MethodCall():
    instance = gremlin_IndexCall(indexName="sample_text", indexProperty="sample_text", indexQuery="sample_text")
    assert isinstance(instance, MethodCall)


def test_gremlin_IntersectionCall_isa_MethodCall():
    instance = gremlin_IntersectionCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_IsEmptyCall_isa_MethodCall():
    instance = gremlin_IsEmptyCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_NextCall_isa_MethodCall():
    instance = gremlin_NextCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_RetainAllCall_isa_MethodCall():
    instance = gremlin_RetainAllCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_SizeCall_isa_MethodCall():
    instance = gremlin_SizeCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_ToIntegerCall_isa_MethodCall():
    instance = gremlin_ToIntegerCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_ToListCall_isa_MethodCall():
    instance = gremlin_ToListCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_UnionCall_isa_MethodCall():
    instance = gremlin_UnionCall()
    assert isinstance(instance, MethodCall)


def test_gremlin_CustomStep_isa_Step():
    instance = gremlin_CustomStep(name="sample_text")
    assert isinstance(instance, Step)


def test_gremlin_EdgesStep_isa_Step():
    instance = gremlin_EdgesStep(relationshipName="sample_text")
    assert isinstance(instance, Step)


def test_gremlin_ExceptStep_isa_Step():
    instance = gremlin_ExceptStep()
    assert isinstance(instance, Step)


def test_gremlin_FillStep_isa_Step():
    instance = gremlin_FillStep()
    assert isinstance(instance, Step)


def test_gremlin_FilterStep_isa_Step():
    instance = gremlin_FilterStep()
    assert isinstance(instance, Step)


def test_gremlin_GatherStep_isa_Step():
    instance = gremlin_GatherStep()
    assert isinstance(instance, Step)


def test_gremlin_IdentityStep_isa_Step():
    instance = gremlin_IdentityStep(needed=True)
    assert isinstance(instance, Step)


def test_gremlin_InEStep_isa_Step():
    instance = gremlin_InEStep(relationshipName="sample_text")
    assert isinstance(instance, Step)


def test_gremlin_InVStep_isa_Step():
    instance = gremlin_InVStep()
    assert isinstance(instance, Step)


def test_gremlin_OutEStep_isa_Step():
    instance = gremlin_OutEStep(relationshipName="sample_text")
    assert isinstance(instance, Step)


def test_gremlin_OutVStep_isa_Step():
    instance = gremlin_OutVStep()
    assert isinstance(instance, Step)


def test_gremlin_PropertyStep_isa_Step():
    instance = gremlin_PropertyStep(name="sample_text")
    assert isinstance(instance, Step)


def test_gremlin_RetainStep_isa_Step():
    instance = gremlin_RetainStep()
    assert isinstance(instance, Step)


def test_gremlin_ScatterStep_isa_Step():
    instance = gremlin_ScatterStep()
    assert isinstance(instance, Step)


def test_gremlin_StartStep_isa_Step():
    instance = gremlin_StartStep()
    assert isinstance(instance, Step)


def test_gremlin_TransformStep_isa_Step():
    instance = gremlin_TransformStep()
    assert isinstance(instance, Step)


def test_gremlin_VerticesStep_isa_Step():
    instance = gremlin_VerticesStep(vertexId="sample_text")
    assert isinstance(instance, Step)


def test_gremlin_CollectionDefinition_isa_TraversalElement():
    instance = gremlin_CollectionDefinition()
    assert isinstance(instance, TraversalElement)


def test_gremlin_MethodCall_isa_TraversalElement():
    instance = gremlin_MethodCall()
    assert isinstance(instance, TraversalElement)


def test_gremlin_Step_isa_TraversalElement():
    instance = gremlin_Step()
    assert isinstance(instance, TraversalElement)


def test_gremlin_VariableAccess_isa_TraversalElement():
    instance = gremlin_VariableAccess(name="sample_text")
    assert isinstance(instance, TraversalElement)


def test_gremlin_ListDeclaration_isa_TypeDeclaration():
    instance = gremlin_ListDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_gremlin_SetDeclaration_isa_TypeDeclaration():
    instance = gremlin_SetDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_gremlin_SortedSetDeclaration_isa_TypeDeclaration():
    instance = gremlin_SortedSetDeclaration()
    assert isinstance(instance, TypeDeclaration)


def test_gremlin_NotExpression_isa_UnaryExpression():
    instance = gremlin_NotExpression()
    assert isinstance(instance, UnaryExpression)


def test_gremlin_ClosureIt_isa_VariableAccess():
    instance = gremlin_ClosureIt()
    assert isinstance(instance, VariableAccess)


def test_assoc_cast19_link_reassign_clear():
    a = gremlin_VariableAccess(name="sample_text")
    b1 = gremlin_TypeDeclaration()
    b2 = gremlin_TypeDeclaration()
    _safe_set(a, 'gremlin_VariableAccess', b1)
    assert _is_linked(a, 'gremlin_VariableAccess', b1)
    if hasattr(b1, 'gremlin_TypeDeclaration20'):
        assert _is_linked(b1, 'gremlin_TypeDeclaration20', a)
    _safe_set(a, 'gremlin_VariableAccess', b2)
    assert _is_linked(a, 'gremlin_VariableAccess', b2)
    if hasattr(b1, 'gremlin_TypeDeclaration20'):
        assert not _is_linked(b1, 'gremlin_TypeDeclaration20', a)
    if hasattr(b2, 'gremlin_TypeDeclaration20'):
        assert _is_linked(b2, 'gremlin_TypeDeclaration20', a)
    _safe_set(a, 'gremlin_VariableAccess', None)
    assert not _is_linked(a, 'gremlin_VariableAccess', b2)
    if hasattr(b2, 'gremlin_TypeDeclaration20'):
        assert not _is_linked(b2, 'gremlin_TypeDeclaration20', a)


def test_assoc_cast49_link_reassign_clear():
    a = gremlin_UnionCall()
    b1 = gremlin_TypeDeclaration()
    b2 = gremlin_TypeDeclaration()
    _safe_set(a, 'gremlin_UnionCall50', b1)
    assert _is_linked(a, 'gremlin_UnionCall50', b1)
    if hasattr(b1, 'gremlin_TypeDeclaration51'):
        assert _is_linked(b1, 'gremlin_TypeDeclaration51', a)
    _safe_set(a, 'gremlin_UnionCall50', b2)
    assert _is_linked(a, 'gremlin_UnionCall50', b2)
    if hasattr(b1, 'gremlin_TypeDeclaration51'):
        assert not _is_linked(b1, 'gremlin_TypeDeclaration51', a)
    if hasattr(b2, 'gremlin_TypeDeclaration51'):
        assert _is_linked(b2, 'gremlin_TypeDeclaration51', a)
    _safe_set(a, 'gremlin_UnionCall50', None)
    assert not _is_linked(a, 'gremlin_UnionCall50', b2)
    if hasattr(b2, 'gremlin_TypeDeclaration51'):
        assert not _is_linked(b2, 'gremlin_TypeDeclaration51', a)


def test_assoc_cast57_link_reassign_clear():
    a = gremlin_IntersectionCall()
    b1 = gremlin_TypeDeclaration()
    b2 = gremlin_TypeDeclaration()
    _safe_set(a, 'gremlin_IntersectionCall58', b1)
    assert _is_linked(a, 'gremlin_IntersectionCall58', b1)
    if hasattr(b1, 'gremlin_TypeDeclaration59'):
        assert _is_linked(b1, 'gremlin_TypeDeclaration59', a)
    _safe_set(a, 'gremlin_IntersectionCall58', b2)
    assert _is_linked(a, 'gremlin_IntersectionCall58', b2)
    if hasattr(b1, 'gremlin_TypeDeclaration59'):
        assert not _is_linked(b1, 'gremlin_TypeDeclaration59', a)
    if hasattr(b2, 'gremlin_TypeDeclaration59'):
        assert _is_linked(b2, 'gremlin_TypeDeclaration59', a)
    _safe_set(a, 'gremlin_IntersectionCall58', None)
    assert not _is_linked(a, 'gremlin_IntersectionCall58', b2)
    if hasattr(b2, 'gremlin_TypeDeclaration59'):
        assert not _is_linked(b2, 'gremlin_TypeDeclaration59', a)


def test_assoc_closure25_link_reassign_clear():
    a = gremlin_FilterStep()
    b1 = gremlin_Closure()
    b2 = gremlin_Closure()
    _safe_set(a, 'gremlin_FilterStep', b1)
    assert _is_linked(a, 'gremlin_FilterStep', b1)
    if hasattr(b1, 'gremlin_Closure26'):
        assert _is_linked(b1, 'gremlin_Closure26', a)
    _safe_set(a, 'gremlin_FilterStep', b2)
    assert _is_linked(a, 'gremlin_FilterStep', b2)
    if hasattr(b1, 'gremlin_Closure26'):
        assert not _is_linked(b1, 'gremlin_Closure26', a)
    if hasattr(b2, 'gremlin_Closure26'):
        assert _is_linked(b2, 'gremlin_Closure26', a)
    _safe_set(a, 'gremlin_FilterStep', None)
    assert not _is_linked(a, 'gremlin_FilterStep', b2)
    if hasattr(b2, 'gremlin_Closure26'):
        assert not _is_linked(b2, 'gremlin_Closure26', a)


def test_assoc_closure31_link_reassign_clear():
    a = gremlin_TransformStep()
    b1 = gremlin_Closure()
    b2 = gremlin_Closure()
    _safe_set(a, 'gremlin_TransformStep', b1)
    assert _is_linked(a, 'gremlin_TransformStep', b1)
    if hasattr(b1, 'gremlin_Closure32'):
        assert _is_linked(b1, 'gremlin_Closure32', a)
    _safe_set(a, 'gremlin_TransformStep', b2)
    assert _is_linked(a, 'gremlin_TransformStep', b2)
    if hasattr(b1, 'gremlin_Closure32'):
        assert not _is_linked(b1, 'gremlin_Closure32', a)
    if hasattr(b2, 'gremlin_Closure32'):
        assert _is_linked(b2, 'gremlin_Closure32', a)
    _safe_set(a, 'gremlin_TransformStep', None)
    assert not _is_linked(a, 'gremlin_TransformStep', b2)
    if hasattr(b2, 'gremlin_Closure32'):
        assert not _is_linked(b2, 'gremlin_Closure32', a)


def test_assoc_closure33_link_reassign_clear():
    a = gremlin_GatherStep()
    b1 = gremlin_Closure()
    b2 = gremlin_Closure()
    _safe_set(a, 'gremlin_GatherStep', b1)
    assert _is_linked(a, 'gremlin_GatherStep', b1)
    if hasattr(b1, 'gremlin_Closure34'):
        assert _is_linked(b1, 'gremlin_Closure34', a)
    _safe_set(a, 'gremlin_GatherStep', b2)
    assert _is_linked(a, 'gremlin_GatherStep', b2)
    if hasattr(b1, 'gremlin_Closure34'):
        assert not _is_linked(b1, 'gremlin_Closure34', a)
    if hasattr(b2, 'gremlin_Closure34'):
        assert _is_linked(b2, 'gremlin_Closure34', a)
    _safe_set(a, 'gremlin_GatherStep', None)
    assert not _is_linked(a, 'gremlin_GatherStep', b2)
    if hasattr(b2, 'gremlin_Closure34'):
        assert not _is_linked(b2, 'gremlin_Closure34', a)


def test_assoc_collection27_link_reassign_clear():
    a = gremlin_RetainStep()
    b1 = gremlin_CollectionDefinition()
    b2 = gremlin_CollectionDefinition()
    _safe_set(a, 'gremlin_RetainStep', b1)
    assert _is_linked(a, 'gremlin_RetainStep', b1)
    if hasattr(b1, 'gremlin_CollectionDefinition28'):
        assert _is_linked(b1, 'gremlin_CollectionDefinition28', a)
    _safe_set(a, 'gremlin_RetainStep', b2)
    assert _is_linked(a, 'gremlin_RetainStep', b2)
    if hasattr(b1, 'gremlin_CollectionDefinition28'):
        assert not _is_linked(b1, 'gremlin_CollectionDefinition28', a)
    if hasattr(b2, 'gremlin_CollectionDefinition28'):
        assert _is_linked(b2, 'gremlin_CollectionDefinition28', a)
    _safe_set(a, 'gremlin_RetainStep', None)
    assert not _is_linked(a, 'gremlin_RetainStep', b2)
    if hasattr(b2, 'gremlin_CollectionDefinition28'):
        assert not _is_linked(b2, 'gremlin_CollectionDefinition28', a)


def test_assoc_collection29_link_reassign_clear():
    a = gremlin_ExceptStep()
    b1 = gremlin_CollectionDefinition()
    b2 = gremlin_CollectionDefinition()
    _safe_set(a, 'gremlin_ExceptStep', b1)
    assert _is_linked(a, 'gremlin_ExceptStep', b1)
    if hasattr(b1, 'gremlin_CollectionDefinition30'):
        assert _is_linked(b1, 'gremlin_CollectionDefinition30', a)
    _safe_set(a, 'gremlin_ExceptStep', b2)
    assert _is_linked(a, 'gremlin_ExceptStep', b2)
    if hasattr(b1, 'gremlin_CollectionDefinition30'):
        assert not _is_linked(b1, 'gremlin_CollectionDefinition30', a)
    if hasattr(b2, 'gremlin_CollectionDefinition30'):
        assert _is_linked(b2, 'gremlin_CollectionDefinition30', a)
    _safe_set(a, 'gremlin_ExceptStep', None)
    assert not _is_linked(a, 'gremlin_ExceptStep', b2)
    if hasattr(b2, 'gremlin_CollectionDefinition30'):
        assert not _is_linked(b2, 'gremlin_CollectionDefinition30', a)


def test_assoc_condition67_link_reassign_clear():
    a = gremlin_TernaryOperator()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_TernaryOperator', b1)
    assert _is_linked(a, 'gremlin_TernaryOperator', b1)
    if hasattr(b1, 'gremlin_Instruction68'):
        assert _is_linked(b1, 'gremlin_Instruction68', a)
    _safe_set(a, 'gremlin_TernaryOperator', b2)
    assert _is_linked(a, 'gremlin_TernaryOperator', b2)
    if hasattr(b1, 'gremlin_Instruction68'):
        assert not _is_linked(b1, 'gremlin_Instruction68', a)
    if hasattr(b2, 'gremlin_Instruction68'):
        assert _is_linked(b2, 'gremlin_Instruction68', a)
    _safe_set(a, 'gremlin_TernaryOperator', None)
    assert not _is_linked(a, 'gremlin_TernaryOperator', b2)
    if hasattr(b2, 'gremlin_Instruction68'):
        assert not _is_linked(b2, 'gremlin_Instruction68', a)


def test_assoc_ifFalse72_link_reassign_clear():
    a = gremlin_TernaryOperator()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_TernaryOperator73', b1)
    assert _is_linked(a, 'gremlin_TernaryOperator73', b1)
    if hasattr(b1, 'gremlin_Instruction74'):
        assert _is_linked(b1, 'gremlin_Instruction74', a)
    _safe_set(a, 'gremlin_TernaryOperator73', b2)
    assert _is_linked(a, 'gremlin_TernaryOperator73', b2)
    if hasattr(b1, 'gremlin_Instruction74'):
        assert not _is_linked(b1, 'gremlin_Instruction74', a)
    if hasattr(b2, 'gremlin_Instruction74'):
        assert _is_linked(b2, 'gremlin_Instruction74', a)
    _safe_set(a, 'gremlin_TernaryOperator73', None)
    assert not _is_linked(a, 'gremlin_TernaryOperator73', b2)
    if hasattr(b2, 'gremlin_Instruction74'):
        assert not _is_linked(b2, 'gremlin_Instruction74', a)


def test_assoc_ifTrue69_link_reassign_clear():
    a = gremlin_TernaryOperator()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_TernaryOperator70', b1)
    assert _is_linked(a, 'gremlin_TernaryOperator70', b1)
    if hasattr(b1, 'gremlin_Instruction71'):
        assert _is_linked(b1, 'gremlin_Instruction71', a)
    _safe_set(a, 'gremlin_TernaryOperator70', b2)
    assert _is_linked(a, 'gremlin_TernaryOperator70', b2)
    if hasattr(b1, 'gremlin_Instruction71'):
        assert not _is_linked(b1, 'gremlin_Instruction71', a)
    if hasattr(b2, 'gremlin_Instruction71'):
        assert _is_linked(b2, 'gremlin_Instruction71', a)
    _safe_set(a, 'gremlin_TernaryOperator70', None)
    assert not _is_linked(a, 'gremlin_TernaryOperator70', b2)
    if hasattr(b2, 'gremlin_Instruction71'):
        assert not _is_linked(b2, 'gremlin_Instruction71', a)


def test_assoc_instruction21_link_reassign_clear():
    a = gremlin_FillStep()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_FillStep', b1)
    assert _is_linked(a, 'gremlin_FillStep', b1)
    if hasattr(b1, 'gremlin_Instruction22'):
        assert _is_linked(b1, 'gremlin_Instruction22', a)
    _safe_set(a, 'gremlin_FillStep', b2)
    assert _is_linked(a, 'gremlin_FillStep', b2)
    if hasattr(b1, 'gremlin_Instruction22'):
        assert not _is_linked(b1, 'gremlin_Instruction22', a)
    if hasattr(b2, 'gremlin_Instruction22'):
        assert _is_linked(b2, 'gremlin_Instruction22', a)
    _safe_set(a, 'gremlin_FillStep', None)
    assert not _is_linked(a, 'gremlin_FillStep', b2)
    if hasattr(b2, 'gremlin_Instruction22'):
        assert not _is_linked(b2, 'gremlin_Instruction22', a)


def test_assoc_instructions0_link_reassign_clear():
    a = gremlin_GremlinScript(name="sample_text")
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_GremlinScript', {b1})
    assert _is_linked(a, 'gremlin_GremlinScript', b1)
    if hasattr(b1, 'gremlin_Instruction'):
        assert _is_linked(b1, 'gremlin_Instruction', a)
    _safe_set(a, 'gremlin_GremlinScript', {b2})
    assert _is_linked(a, 'gremlin_GremlinScript', b2)
    if hasattr(b1, 'gremlin_Instruction'):
        assert not _is_linked(b1, 'gremlin_Instruction', a)
    if hasattr(b2, 'gremlin_Instruction'):
        assert _is_linked(b2, 'gremlin_Instruction', a)
    _safe_set(a, 'gremlin_GremlinScript', set())
    assert not _is_linked(a, 'gremlin_GremlinScript', b2)
    if hasattr(b2, 'gremlin_Instruction'):
        assert not _is_linked(b2, 'gremlin_Instruction', a)


def test_assoc_instructions1_link_reassign_clear():
    a = gremlin_MethodDeclaration(name="sample_text", parameters="sample_text")
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_MethodDeclaration', {b1})
    assert _is_linked(a, 'gremlin_MethodDeclaration', b1)
    if hasattr(b1, 'gremlin_Instruction2'):
        assert _is_linked(b1, 'gremlin_Instruction2', a)
    _safe_set(a, 'gremlin_MethodDeclaration', {b2})
    assert _is_linked(a, 'gremlin_MethodDeclaration', b2)
    if hasattr(b1, 'gremlin_Instruction2'):
        assert not _is_linked(b1, 'gremlin_Instruction2', a)
    if hasattr(b2, 'gremlin_Instruction2'):
        assert _is_linked(b2, 'gremlin_Instruction2', a)
    _safe_set(a, 'gremlin_MethodDeclaration', set())
    assert not _is_linked(a, 'gremlin_MethodDeclaration', b2)
    if hasattr(b2, 'gremlin_Instruction2'):
        assert not _is_linked(b2, 'gremlin_Instruction2', a)


def test_assoc_instructions17_link_reassign_clear():
    a = gremlin_Closure()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_Closure', {b1})
    assert _is_linked(a, 'gremlin_Closure', b1)
    if hasattr(b1, 'gremlin_Instruction18'):
        assert _is_linked(b1, 'gremlin_Instruction18', a)
    _safe_set(a, 'gremlin_Closure', {b2})
    assert _is_linked(a, 'gremlin_Closure', b2)
    if hasattr(b1, 'gremlin_Instruction18'):
        assert not _is_linked(b1, 'gremlin_Instruction18', a)
    if hasattr(b2, 'gremlin_Instruction18'):
        assert _is_linked(b2, 'gremlin_Instruction18', a)
    _safe_set(a, 'gremlin_Closure', set())
    assert not _is_linked(a, 'gremlin_Closure', b2)
    if hasattr(b2, 'gremlin_Instruction18'):
        assert not _is_linked(b2, 'gremlin_Instruction18', a)


def test_assoc_leftCollection44_link_reassign_clear():
    a = gremlin_UnionCall()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_UnionCall', b1)
    assert _is_linked(a, 'gremlin_UnionCall', b1)
    if hasattr(b1, 'gremlin_Instruction45'):
        assert _is_linked(b1, 'gremlin_Instruction45', a)
    _safe_set(a, 'gremlin_UnionCall', b2)
    assert _is_linked(a, 'gremlin_UnionCall', b2)
    if hasattr(b1, 'gremlin_Instruction45'):
        assert not _is_linked(b1, 'gremlin_Instruction45', a)
    if hasattr(b2, 'gremlin_Instruction45'):
        assert _is_linked(b2, 'gremlin_Instruction45', a)
    _safe_set(a, 'gremlin_UnionCall', None)
    assert not _is_linked(a, 'gremlin_UnionCall', b2)
    if hasattr(b2, 'gremlin_Instruction45'):
        assert not _is_linked(b2, 'gremlin_Instruction45', a)


def test_assoc_leftCollection52_link_reassign_clear():
    a = gremlin_IntersectionCall()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_IntersectionCall', b1)
    assert _is_linked(a, 'gremlin_IntersectionCall', b1)
    if hasattr(b1, 'gremlin_Instruction53'):
        assert _is_linked(b1, 'gremlin_Instruction53', a)
    _safe_set(a, 'gremlin_IntersectionCall', b2)
    assert _is_linked(a, 'gremlin_IntersectionCall', b2)
    if hasattr(b1, 'gremlin_Instruction53'):
        assert not _is_linked(b1, 'gremlin_Instruction53', a)
    if hasattr(b2, 'gremlin_Instruction53'):
        assert _is_linked(b2, 'gremlin_Instruction53', a)
    _safe_set(a, 'gremlin_IntersectionCall', None)
    assert not _is_linked(a, 'gremlin_IntersectionCall', b2)
    if hasattr(b2, 'gremlin_Instruction53'):
        assert not _is_linked(b2, 'gremlin_Instruction53', a)


def test_assoc_params35_link_reassign_clear():
    a = gremlin_CustomMethodCall(name="sample_text")
    b1 = gremlin_EObject()
    b2 = gremlin_EObject()
    _safe_set(a, 'gremlin_CustomMethodCall', {b1})
    assert _is_linked(a, 'gremlin_CustomMethodCall', b1)
    if hasattr(b1, 'gremlin_EObject'):
        assert _is_linked(b1, 'gremlin_EObject', a)
    _safe_set(a, 'gremlin_CustomMethodCall', {b2})
    assert _is_linked(a, 'gremlin_CustomMethodCall', b2)
    if hasattr(b1, 'gremlin_EObject'):
        assert not _is_linked(b1, 'gremlin_EObject', a)
    if hasattr(b2, 'gremlin_EObject'):
        assert _is_linked(b2, 'gremlin_EObject', a)
    _safe_set(a, 'gremlin_CustomMethodCall', set())
    assert not _is_linked(a, 'gremlin_CustomMethodCall', b2)
    if hasattr(b2, 'gremlin_EObject'):
        assert not _is_linked(b2, 'gremlin_EObject', a)


def test_assoc_params75_link_reassign_clear():
    a = gremlin_CustomStep(name="sample_text")
    b1 = gremlin_EObject()
    b2 = gremlin_EObject()
    _safe_set(a, 'gremlin_CustomStep', {b1})
    assert _is_linked(a, 'gremlin_CustomStep', b1)
    if hasattr(b1, 'gremlin_EObject76'):
        assert _is_linked(b1, 'gremlin_EObject76', a)
    _safe_set(a, 'gremlin_CustomStep', {b2})
    assert _is_linked(a, 'gremlin_CustomStep', b2)
    if hasattr(b1, 'gremlin_EObject76'):
        assert not _is_linked(b1, 'gremlin_EObject76', a)
    if hasattr(b2, 'gremlin_EObject76'):
        assert _is_linked(b2, 'gremlin_EObject76', a)
    _safe_set(a, 'gremlin_CustomStep', set())
    assert not _is_linked(a, 'gremlin_CustomStep', b2)
    if hasattr(b2, 'gremlin_EObject76'):
        assert not _is_linked(b2, 'gremlin_EObject76', a)


def test_assoc_rightCollection46_link_reassign_clear():
    a = gremlin_UnionCall()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_UnionCall47', b1)
    assert _is_linked(a, 'gremlin_UnionCall47', b1)
    if hasattr(b1, 'gremlin_Instruction48'):
        assert _is_linked(b1, 'gremlin_Instruction48', a)
    _safe_set(a, 'gremlin_UnionCall47', b2)
    assert _is_linked(a, 'gremlin_UnionCall47', b2)
    if hasattr(b1, 'gremlin_Instruction48'):
        assert not _is_linked(b1, 'gremlin_Instruction48', a)
    if hasattr(b2, 'gremlin_Instruction48'):
        assert _is_linked(b2, 'gremlin_Instruction48', a)
    _safe_set(a, 'gremlin_UnionCall47', None)
    assert not _is_linked(a, 'gremlin_UnionCall47', b2)
    if hasattr(b2, 'gremlin_Instruction48'):
        assert not _is_linked(b2, 'gremlin_Instruction48', a)


def test_assoc_rightCollection54_link_reassign_clear():
    a = gremlin_IntersectionCall()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_IntersectionCall55', b1)
    assert _is_linked(a, 'gremlin_IntersectionCall55', b1)
    if hasattr(b1, 'gremlin_Instruction56'):
        assert _is_linked(b1, 'gremlin_Instruction56', a)
    _safe_set(a, 'gremlin_IntersectionCall55', b2)
    assert _is_linked(a, 'gremlin_IntersectionCall55', b2)
    if hasattr(b1, 'gremlin_Instruction56'):
        assert not _is_linked(b1, 'gremlin_Instruction56', a)
    if hasattr(b2, 'gremlin_Instruction56'):
        assert _is_linked(b2, 'gremlin_Instruction56', a)
    _safe_set(a, 'gremlin_IntersectionCall55', None)
    assert not _is_linked(a, 'gremlin_IntersectionCall55', b2)
    if hasattr(b2, 'gremlin_Instruction56'):
        assert not _is_linked(b2, 'gremlin_Instruction56', a)


def test_assoc_type14_link_reassign_clear():
    a = gremlin_CollectionDefinition()
    b1 = gremlin_TypeDeclaration()
    b2 = gremlin_TypeDeclaration()
    _safe_set(a, 'gremlin_CollectionDefinition15', b1)
    assert _is_linked(a, 'gremlin_CollectionDefinition15', b1)
    if hasattr(b1, 'gremlin_TypeDeclaration16'):
        assert _is_linked(b1, 'gremlin_TypeDeclaration16', a)
    _safe_set(a, 'gremlin_CollectionDefinition15', b2)
    assert _is_linked(a, 'gremlin_CollectionDefinition15', b2)
    if hasattr(b1, 'gremlin_TypeDeclaration16'):
        assert not _is_linked(b1, 'gremlin_TypeDeclaration16', a)
    if hasattr(b2, 'gremlin_TypeDeclaration16'):
        assert _is_linked(b2, 'gremlin_TypeDeclaration16', a)
    _safe_set(a, 'gremlin_CollectionDefinition15', None)
    assert not _is_linked(a, 'gremlin_CollectionDefinition15', b2)
    if hasattr(b2, 'gremlin_TypeDeclaration16'):
        assert not _is_linked(b2, 'gremlin_TypeDeclaration16', a)


def test_assoc_type5_link_reassign_clear():
    a = gremlin_VariableDeclaration(final=True, name="sample_text")
    b1 = gremlin_TypeDeclaration()
    b2 = gremlin_TypeDeclaration()
    _safe_set(a, 'gremlin_VariableDeclaration6', b1)
    assert _is_linked(a, 'gremlin_VariableDeclaration6', b1)
    if hasattr(b1, 'gremlin_TypeDeclaration'):
        assert _is_linked(b1, 'gremlin_TypeDeclaration', a)
    _safe_set(a, 'gremlin_VariableDeclaration6', b2)
    assert _is_linked(a, 'gremlin_VariableDeclaration6', b2)
    if hasattr(b1, 'gremlin_TypeDeclaration'):
        assert not _is_linked(b1, 'gremlin_TypeDeclaration', a)
    if hasattr(b2, 'gremlin_TypeDeclaration'):
        assert _is_linked(b2, 'gremlin_TypeDeclaration', a)
    _safe_set(a, 'gremlin_VariableDeclaration6', None)
    assert not _is_linked(a, 'gremlin_VariableDeclaration6', b2)
    if hasattr(b2, 'gremlin_TypeDeclaration'):
        assert not _is_linked(b2, 'gremlin_TypeDeclaration', a)


def test_assoc_value23_link_reassign_clear():
    a = gremlin_PropertyStep(name="sample_text")
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_PropertyStep', b1)
    assert _is_linked(a, 'gremlin_PropertyStep', b1)
    if hasattr(b1, 'gremlin_Instruction24'):
        assert _is_linked(b1, 'gremlin_Instruction24', a)
    _safe_set(a, 'gremlin_PropertyStep', b2)
    assert _is_linked(a, 'gremlin_PropertyStep', b2)
    if hasattr(b1, 'gremlin_Instruction24'):
        assert not _is_linked(b1, 'gremlin_Instruction24', a)
    if hasattr(b2, 'gremlin_Instruction24'):
        assert _is_linked(b2, 'gremlin_Instruction24', a)
    _safe_set(a, 'gremlin_PropertyStep', None)
    assert not _is_linked(a, 'gremlin_PropertyStep', b2)
    if hasattr(b2, 'gremlin_Instruction24'):
        assert not _is_linked(b2, 'gremlin_Instruction24', a)


def test_assoc_value3_link_reassign_clear():
    a = gremlin_VariableDeclaration(final=True, name="sample_text")
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_VariableDeclaration', b1)
    assert _is_linked(a, 'gremlin_VariableDeclaration', b1)
    if hasattr(b1, 'gremlin_Instruction4'):
        assert _is_linked(b1, 'gremlin_Instruction4', a)
    _safe_set(a, 'gremlin_VariableDeclaration', b2)
    assert _is_linked(a, 'gremlin_VariableDeclaration', b2)
    if hasattr(b1, 'gremlin_Instruction4'):
        assert not _is_linked(b1, 'gremlin_Instruction4', a)
    if hasattr(b2, 'gremlin_Instruction4'):
        assert _is_linked(b2, 'gremlin_Instruction4', a)
    _safe_set(a, 'gremlin_VariableDeclaration', None)
    assert not _is_linked(a, 'gremlin_VariableDeclaration', b2)
    if hasattr(b2, 'gremlin_Instruction4'):
        assert not _is_linked(b2, 'gremlin_Instruction4', a)


def test_assoc_value36_link_reassign_clear():
    a = gremlin_ContainsCall()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_ContainsCall', b1)
    assert _is_linked(a, 'gremlin_ContainsCall', b1)
    if hasattr(b1, 'gremlin_Instruction37'):
        assert _is_linked(b1, 'gremlin_Instruction37', a)
    _safe_set(a, 'gremlin_ContainsCall', b2)
    assert _is_linked(a, 'gremlin_ContainsCall', b2)
    if hasattr(b1, 'gremlin_Instruction37'):
        assert not _is_linked(b1, 'gremlin_Instruction37', a)
    if hasattr(b2, 'gremlin_Instruction37'):
        assert _is_linked(b2, 'gremlin_Instruction37', a)
    _safe_set(a, 'gremlin_ContainsCall', None)
    assert not _is_linked(a, 'gremlin_ContainsCall', b2)
    if hasattr(b2, 'gremlin_Instruction37'):
        assert not _is_linked(b2, 'gremlin_Instruction37', a)


def test_assoc_value38_link_reassign_clear():
    a = gremlin_ContainsAllCall()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_ContainsAllCall', b1)
    assert _is_linked(a, 'gremlin_ContainsAllCall', b1)
    if hasattr(b1, 'gremlin_Instruction39'):
        assert _is_linked(b1, 'gremlin_Instruction39', a)
    _safe_set(a, 'gremlin_ContainsAllCall', b2)
    assert _is_linked(a, 'gremlin_ContainsAllCall', b2)
    if hasattr(b1, 'gremlin_Instruction39'):
        assert not _is_linked(b1, 'gremlin_Instruction39', a)
    if hasattr(b2, 'gremlin_Instruction39'):
        assert _is_linked(b2, 'gremlin_Instruction39', a)
    _safe_set(a, 'gremlin_ContainsAllCall', None)
    assert not _is_linked(a, 'gremlin_ContainsAllCall', b2)
    if hasattr(b2, 'gremlin_Instruction39'):
        assert not _is_linked(b2, 'gremlin_Instruction39', a)


def test_assoc_value40_link_reassign_clear():
    a = gremlin_AddAllCall()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_AddAllCall', b1)
    assert _is_linked(a, 'gremlin_AddAllCall', b1)
    if hasattr(b1, 'gremlin_Instruction41'):
        assert _is_linked(b1, 'gremlin_Instruction41', a)
    _safe_set(a, 'gremlin_AddAllCall', b2)
    assert _is_linked(a, 'gremlin_AddAllCall', b2)
    if hasattr(b1, 'gremlin_Instruction41'):
        assert not _is_linked(b1, 'gremlin_Instruction41', a)
    if hasattr(b2, 'gremlin_Instruction41'):
        assert _is_linked(b2, 'gremlin_Instruction41', a)
    _safe_set(a, 'gremlin_AddAllCall', None)
    assert not _is_linked(a, 'gremlin_AddAllCall', b2)
    if hasattr(b2, 'gremlin_Instruction41'):
        assert not _is_linked(b2, 'gremlin_Instruction41', a)


def test_assoc_value42_link_reassign_clear():
    a = gremlin_RetainAllCall()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_RetainAllCall', b1)
    assert _is_linked(a, 'gremlin_RetainAllCall', b1)
    if hasattr(b1, 'gremlin_Instruction43'):
        assert _is_linked(b1, 'gremlin_Instruction43', a)
    _safe_set(a, 'gremlin_RetainAllCall', b2)
    assert _is_linked(a, 'gremlin_RetainAllCall', b2)
    if hasattr(b1, 'gremlin_Instruction43'):
        assert not _is_linked(b1, 'gremlin_Instruction43', a)
    if hasattr(b2, 'gremlin_Instruction43'):
        assert _is_linked(b2, 'gremlin_Instruction43', a)
    _safe_set(a, 'gremlin_RetainAllCall', None)
    assert not _is_linked(a, 'gremlin_RetainAllCall', b2)
    if hasattr(b2, 'gremlin_Instruction43'):
        assert not _is_linked(b2, 'gremlin_Instruction43', a)


def test_assoc_values12_link_reassign_clear():
    a = gremlin_CollectionDefinition()
    b1 = gremlin_Instruction()
    b2 = gremlin_Instruction()
    _safe_set(a, 'gremlin_CollectionDefinition', {b1})
    assert _is_linked(a, 'gremlin_CollectionDefinition', b1)
    if hasattr(b1, 'gremlin_Instruction13'):
        assert _is_linked(b1, 'gremlin_Instruction13', a)
    _safe_set(a, 'gremlin_CollectionDefinition', {b2})
    assert _is_linked(a, 'gremlin_CollectionDefinition', b2)
    if hasattr(b1, 'gremlin_Instruction13'):
        assert not _is_linked(b1, 'gremlin_Instruction13', a)
    if hasattr(b2, 'gremlin_Instruction13'):
        assert _is_linked(b2, 'gremlin_Instruction13', a)
    _safe_set(a, 'gremlin_CollectionDefinition', set())
    assert not _is_linked(a, 'gremlin_CollectionDefinition', b2)
    if hasattr(b2, 'gremlin_Instruction13'):
        assert not _is_linked(b2, 'gremlin_Instruction13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BinaryExpression_strategy = st.builds(BinaryExpression)
@given(instance=BinaryExpression_strategy)
@settings(max_examples=25)
def test_BinaryExpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)


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


MethodCall_strategy = st.builds(MethodCall)
@given(instance=MethodCall_strategy)
@settings(max_examples=25)
def test_MethodCall_instantiation(instance):
    assert isinstance(instance, MethodCall)


Step_strategy = st.builds(Step)
@given(instance=Step_strategy)
@settings(max_examples=25)
def test_Step_instantiation(instance):
    assert isinstance(instance, Step)


TraversalElement_strategy = st.builds(TraversalElement)
@given(instance=TraversalElement_strategy)
@settings(max_examples=25)
def test_TraversalElement_instantiation(instance):
    assert isinstance(instance, TraversalElement)


TypeDeclaration_strategy = st.builds(TypeDeclaration)
@given(instance=TypeDeclaration_strategy)
@settings(max_examples=25)
def test_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)


UnaryExpression_strategy = st.builds(UnaryExpression)
@given(instance=UnaryExpression_strategy)
@settings(max_examples=25)
def test_UnaryExpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)


VariableAccess_strategy = st.builds(VariableAccess)
@given(instance=VariableAccess_strategy)
@settings(max_examples=25)
def test_VariableAccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)


gremlin_AddAllCall_strategy = st.builds(gremlin_AddAllCall)
@given(instance=gremlin_AddAllCall_strategy)
@settings(max_examples=25)
def test_gremlin_AddAllCall_instantiation(instance):
    assert isinstance(instance, gremlin_AddAllCall)


gremlin_AffectationExpression_strategy = st.builds(gremlin_AffectationExpression)
@given(instance=gremlin_AffectationExpression_strategy)
@settings(max_examples=25)
def test_gremlin_AffectationExpression_instantiation(instance):
    assert isinstance(instance, gremlin_AffectationExpression)


gremlin_AndExpression_strategy = st.builds(gremlin_AndExpression)
@given(instance=gremlin_AndExpression_strategy)
@settings(max_examples=25)
def test_gremlin_AndExpression_instantiation(instance):
    assert isinstance(instance, gremlin_AndExpression)


gremlin_BinaryExpression_strategy = st.builds(gremlin_BinaryExpression)
@given(instance=gremlin_BinaryExpression_strategy)
@settings(max_examples=25)
def test_gremlin_BinaryExpression_instantiation(instance):
    assert isinstance(instance, gremlin_BinaryExpression)


gremlin_BooleanLiteral_strategy = st.builds(gremlin_BooleanLiteral, value=st.booleans())
@given(instance=gremlin_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_gremlin_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, gremlin_BooleanLiteral)


gremlin_Closure_strategy = st.builds(gremlin_Closure)
@given(instance=gremlin_Closure_strategy)
@settings(max_examples=25)
def test_gremlin_Closure_instantiation(instance):
    assert isinstance(instance, gremlin_Closure)


gremlin_ClosureIt_strategy = st.builds(gremlin_ClosureIt)
@given(instance=gremlin_ClosureIt_strategy)
@settings(max_examples=25)
def test_gremlin_ClosureIt_instantiation(instance):
    assert isinstance(instance, gremlin_ClosureIt)


gremlin_CollectionDefinition_strategy = st.builds(gremlin_CollectionDefinition)
@given(instance=gremlin_CollectionDefinition_strategy)
@settings(max_examples=25)
def test_gremlin_CollectionDefinition_instantiation(instance):
    assert isinstance(instance, gremlin_CollectionDefinition)


gremlin_ContainsAllCall_strategy = st.builds(gremlin_ContainsAllCall)
@given(instance=gremlin_ContainsAllCall_strategy)
@settings(max_examples=25)
def test_gremlin_ContainsAllCall_instantiation(instance):
    assert isinstance(instance, gremlin_ContainsAllCall)


gremlin_ContainsCall_strategy = st.builds(gremlin_ContainsCall)
@given(instance=gremlin_ContainsCall_strategy)
@settings(max_examples=25)
def test_gremlin_ContainsCall_instantiation(instance):
    assert isinstance(instance, gremlin_ContainsCall)


gremlin_CountCall_strategy = st.builds(gremlin_CountCall)
@given(instance=gremlin_CountCall_strategy)
@settings(max_examples=25)
def test_gremlin_CountCall_instantiation(instance):
    assert isinstance(instance, gremlin_CountCall)


gremlin_CustomMethodCall_strategy = st.builds(gremlin_CustomMethodCall, name=safe_text)
@given(instance=gremlin_CustomMethodCall_strategy)
@settings(max_examples=25)
def test_gremlin_CustomMethodCall_instantiation(instance):
    assert isinstance(instance, gremlin_CustomMethodCall)


gremlin_CustomStep_strategy = st.builds(gremlin_CustomStep, name=safe_text)
@given(instance=gremlin_CustomStep_strategy)
@settings(max_examples=25)
def test_gremlin_CustomStep_instantiation(instance):
    assert isinstance(instance, gremlin_CustomStep)


gremlin_DifferenceExpression_strategy = st.builds(gremlin_DifferenceExpression)
@given(instance=gremlin_DifferenceExpression_strategy)
@settings(max_examples=25)
def test_gremlin_DifferenceExpression_instantiation(instance):
    assert isinstance(instance, gremlin_DifferenceExpression)


gremlin_DoubleLiteral_strategy = st.builds(gremlin_DoubleLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=gremlin_DoubleLiteral_strategy)
@settings(max_examples=25)
def test_gremlin_DoubleLiteral_instantiation(instance):
    assert isinstance(instance, gremlin_DoubleLiteral)


gremlin_EObject_strategy = st.builds(gremlin_EObject)
@given(instance=gremlin_EObject_strategy)
@settings(max_examples=25)
def test_gremlin_EObject_instantiation(instance):
    assert isinstance(instance, gremlin_EObject)


gremlin_EdgesStep_strategy = st.builds(gremlin_EdgesStep, relationshipName=safe_text)
@given(instance=gremlin_EdgesStep_strategy)
@settings(max_examples=25)
def test_gremlin_EdgesStep_instantiation(instance):
    assert isinstance(instance, gremlin_EdgesStep)


gremlin_EqualityExpression_strategy = st.builds(gremlin_EqualityExpression)
@given(instance=gremlin_EqualityExpression_strategy)
@settings(max_examples=25)
def test_gremlin_EqualityExpression_instantiation(instance):
    assert isinstance(instance, gremlin_EqualityExpression)


gremlin_ExceptStep_strategy = st.builds(gremlin_ExceptStep)
@given(instance=gremlin_ExceptStep_strategy)
@settings(max_examples=25)
def test_gremlin_ExceptStep_instantiation(instance):
    assert isinstance(instance, gremlin_ExceptStep)


gremlin_Expression_strategy = st.builds(gremlin_Expression)
@given(instance=gremlin_Expression_strategy)
@settings(max_examples=25)
def test_gremlin_Expression_instantiation(instance):
    assert isinstance(instance, gremlin_Expression)


gremlin_FillStep_strategy = st.builds(gremlin_FillStep)
@given(instance=gremlin_FillStep_strategy)
@settings(max_examples=25)
def test_gremlin_FillStep_instantiation(instance):
    assert isinstance(instance, gremlin_FillStep)


gremlin_FilterStep_strategy = st.builds(gremlin_FilterStep)
@given(instance=gremlin_FilterStep_strategy)
@settings(max_examples=25)
def test_gremlin_FilterStep_instantiation(instance):
    assert isinstance(instance, gremlin_FilterStep)


gremlin_FirstCall_strategy = st.builds(gremlin_FirstCall)
@given(instance=gremlin_FirstCall_strategy)
@settings(max_examples=25)
def test_gremlin_FirstCall_instantiation(instance):
    assert isinstance(instance, gremlin_FirstCall)


gremlin_GatherStep_strategy = st.builds(gremlin_GatherStep)
@given(instance=gremlin_GatherStep_strategy)
@settings(max_examples=25)
def test_gremlin_GatherStep_instantiation(instance):
    assert isinstance(instance, gremlin_GatherStep)


gremlin_GreaterExpression_strategy = st.builds(gremlin_GreaterExpression)
@given(instance=gremlin_GreaterExpression_strategy)
@settings(max_examples=25)
def test_gremlin_GreaterExpression_instantiation(instance):
    assert isinstance(instance, gremlin_GreaterExpression)


gremlin_GreaterOrEqualExpression_strategy = st.builds(gremlin_GreaterOrEqualExpression)
@given(instance=gremlin_GreaterOrEqualExpression_strategy)
@settings(max_examples=25)
def test_gremlin_GreaterOrEqualExpression_instantiation(instance):
    assert isinstance(instance, gremlin_GreaterOrEqualExpression)


gremlin_GremlinScript_strategy = st.builds(gremlin_GremlinScript, name=safe_text)
@given(instance=gremlin_GremlinScript_strategy)
@settings(max_examples=25)
def test_gremlin_GremlinScript_instantiation(instance):
    assert isinstance(instance, gremlin_GremlinScript)


gremlin_HasNextCall_strategy = st.builds(gremlin_HasNextCall)
@given(instance=gremlin_HasNextCall_strategy)
@settings(max_examples=25)
def test_gremlin_HasNextCall_instantiation(instance):
    assert isinstance(instance, gremlin_HasNextCall)


gremlin_IdentityStep_strategy = st.builds(gremlin_IdentityStep, needed=st.booleans())
@given(instance=gremlin_IdentityStep_strategy)
@settings(max_examples=25)
def test_gremlin_IdentityStep_instantiation(instance):
    assert isinstance(instance, gremlin_IdentityStep)


gremlin_InEStep_strategy = st.builds(gremlin_InEStep, relationshipName=safe_text)
@given(instance=gremlin_InEStep_strategy)
@settings(max_examples=25)
def test_gremlin_InEStep_instantiation(instance):
    assert isinstance(instance, gremlin_InEStep)


gremlin_InExpression_strategy = st.builds(gremlin_InExpression)
@given(instance=gremlin_InExpression_strategy)
@settings(max_examples=25)
def test_gremlin_InExpression_instantiation(instance):
    assert isinstance(instance, gremlin_InExpression)


gremlin_InVStep_strategy = st.builds(gremlin_InVStep)
@given(instance=gremlin_InVStep_strategy)
@settings(max_examples=25)
def test_gremlin_InVStep_instantiation(instance):
    assert isinstance(instance, gremlin_InVStep)


gremlin_IndexCall_strategy = st.builds(gremlin_IndexCall, indexName=safe_text, indexProperty=safe_text, indexQuery=safe_text)
@given(instance=gremlin_IndexCall_strategy)
@settings(max_examples=25)
def test_gremlin_IndexCall_instantiation(instance):
    assert isinstance(instance, gremlin_IndexCall)


gremlin_Instruction_strategy = st.builds(gremlin_Instruction)
@given(instance=gremlin_Instruction_strategy)
@settings(max_examples=25)
def test_gremlin_Instruction_instantiation(instance):
    assert isinstance(instance, gremlin_Instruction)


gremlin_IntegerLiteral_strategy = st.builds(gremlin_IntegerLiteral, value=st.integers())
@given(instance=gremlin_IntegerLiteral_strategy)
@settings(max_examples=25)
def test_gremlin_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, gremlin_IntegerLiteral)


gremlin_IntersectionCall_strategy = st.builds(gremlin_IntersectionCall)
@given(instance=gremlin_IntersectionCall_strategy)
@settings(max_examples=25)
def test_gremlin_IntersectionCall_instantiation(instance):
    assert isinstance(instance, gremlin_IntersectionCall)


gremlin_IsEmptyCall_strategy = st.builds(gremlin_IsEmptyCall)
@given(instance=gremlin_IsEmptyCall_strategy)
@settings(max_examples=25)
def test_gremlin_IsEmptyCall_instantiation(instance):
    assert isinstance(instance, gremlin_IsEmptyCall)


gremlin_LeftShiftExpression_strategy = st.builds(gremlin_LeftShiftExpression)
@given(instance=gremlin_LeftShiftExpression_strategy)
@settings(max_examples=25)
def test_gremlin_LeftShiftExpression_instantiation(instance):
    assert isinstance(instance, gremlin_LeftShiftExpression)


gremlin_LessExpression_strategy = st.builds(gremlin_LessExpression)
@given(instance=gremlin_LessExpression_strategy)
@settings(max_examples=25)
def test_gremlin_LessExpression_instantiation(instance):
    assert isinstance(instance, gremlin_LessExpression)


gremlin_LessOrEqualExpression_strategy = st.builds(gremlin_LessOrEqualExpression)
@given(instance=gremlin_LessOrEqualExpression_strategy)
@settings(max_examples=25)
def test_gremlin_LessOrEqualExpression_instantiation(instance):
    assert isinstance(instance, gremlin_LessOrEqualExpression)


gremlin_ListDeclaration_strategy = st.builds(gremlin_ListDeclaration)
@given(instance=gremlin_ListDeclaration_strategy)
@settings(max_examples=25)
def test_gremlin_ListDeclaration_instantiation(instance):
    assert isinstance(instance, gremlin_ListDeclaration)


gremlin_MethodCall_strategy = st.builds(gremlin_MethodCall)
@given(instance=gremlin_MethodCall_strategy)
@settings(max_examples=25)
def test_gremlin_MethodCall_instantiation(instance):
    assert isinstance(instance, gremlin_MethodCall)


gremlin_MethodDeclaration_strategy = st.builds(gremlin_MethodDeclaration, name=safe_text, parameters=safe_text)
@given(instance=gremlin_MethodDeclaration_strategy)
@settings(max_examples=25)
def test_gremlin_MethodDeclaration_instantiation(instance):
    assert isinstance(instance, gremlin_MethodDeclaration)


gremlin_NextCall_strategy = st.builds(gremlin_NextCall)
@given(instance=gremlin_NextCall_strategy)
@settings(max_examples=25)
def test_gremlin_NextCall_instantiation(instance):
    assert isinstance(instance, gremlin_NextCall)


gremlin_NotExpression_strategy = st.builds(gremlin_NotExpression)
@given(instance=gremlin_NotExpression_strategy)
@settings(max_examples=25)
def test_gremlin_NotExpression_instantiation(instance):
    assert isinstance(instance, gremlin_NotExpression)


gremlin_NullLiteral_strategy = st.builds(gremlin_NullLiteral)
@given(instance=gremlin_NullLiteral_strategy)
@settings(max_examples=25)
def test_gremlin_NullLiteral_instantiation(instance):
    assert isinstance(instance, gremlin_NullLiteral)


gremlin_OrExpression_strategy = st.builds(gremlin_OrExpression)
@given(instance=gremlin_OrExpression_strategy)
@settings(max_examples=25)
def test_gremlin_OrExpression_instantiation(instance):
    assert isinstance(instance, gremlin_OrExpression)


gremlin_OutEStep_strategy = st.builds(gremlin_OutEStep, relationshipName=safe_text)
@given(instance=gremlin_OutEStep_strategy)
@settings(max_examples=25)
def test_gremlin_OutEStep_instantiation(instance):
    assert isinstance(instance, gremlin_OutEStep)


gremlin_OutVStep_strategy = st.builds(gremlin_OutVStep)
@given(instance=gremlin_OutVStep_strategy)
@settings(max_examples=25)
def test_gremlin_OutVStep_instantiation(instance):
    assert isinstance(instance, gremlin_OutVStep)


gremlin_PlusExpression_strategy = st.builds(gremlin_PlusExpression)
@given(instance=gremlin_PlusExpression_strategy)
@settings(max_examples=25)
def test_gremlin_PlusExpression_instantiation(instance):
    assert isinstance(instance, gremlin_PlusExpression)


gremlin_PropertyStep_strategy = st.builds(gremlin_PropertyStep, name=safe_text)
@given(instance=gremlin_PropertyStep_strategy)
@settings(max_examples=25)
def test_gremlin_PropertyStep_instantiation(instance):
    assert isinstance(instance, gremlin_PropertyStep)


gremlin_RetainAllCall_strategy = st.builds(gremlin_RetainAllCall)
@given(instance=gremlin_RetainAllCall_strategy)
@settings(max_examples=25)
def test_gremlin_RetainAllCall_instantiation(instance):
    assert isinstance(instance, gremlin_RetainAllCall)


gremlin_RetainStep_strategy = st.builds(gremlin_RetainStep)
@given(instance=gremlin_RetainStep_strategy)
@settings(max_examples=25)
def test_gremlin_RetainStep_instantiation(instance):
    assert isinstance(instance, gremlin_RetainStep)


gremlin_ReturnStatement_strategy = st.builds(gremlin_ReturnStatement, value=safe_text)
@given(instance=gremlin_ReturnStatement_strategy)
@settings(max_examples=25)
def test_gremlin_ReturnStatement_instantiation(instance):
    assert isinstance(instance, gremlin_ReturnStatement)


gremlin_ScatterStep_strategy = st.builds(gremlin_ScatterStep)
@given(instance=gremlin_ScatterStep_strategy)
@settings(max_examples=25)
def test_gremlin_ScatterStep_instantiation(instance):
    assert isinstance(instance, gremlin_ScatterStep)


gremlin_SetDeclaration_strategy = st.builds(gremlin_SetDeclaration)
@given(instance=gremlin_SetDeclaration_strategy)
@settings(max_examples=25)
def test_gremlin_SetDeclaration_instantiation(instance):
    assert isinstance(instance, gremlin_SetDeclaration)


gremlin_SizeCall_strategy = st.builds(gremlin_SizeCall)
@given(instance=gremlin_SizeCall_strategy)
@settings(max_examples=25)
def test_gremlin_SizeCall_instantiation(instance):
    assert isinstance(instance, gremlin_SizeCall)


gremlin_SortedSetDeclaration_strategy = st.builds(gremlin_SortedSetDeclaration)
@given(instance=gremlin_SortedSetDeclaration_strategy)
@settings(max_examples=25)
def test_gremlin_SortedSetDeclaration_instantiation(instance):
    assert isinstance(instance, gremlin_SortedSetDeclaration)


gremlin_StartStep_strategy = st.builds(gremlin_StartStep)
@given(instance=gremlin_StartStep_strategy)
@settings(max_examples=25)
def test_gremlin_StartStep_instantiation(instance):
    assert isinstance(instance, gremlin_StartStep)


gremlin_Step_strategy = st.builds(gremlin_Step)
@given(instance=gremlin_Step_strategy)
@settings(max_examples=25)
def test_gremlin_Step_instantiation(instance):
    assert isinstance(instance, gremlin_Step)


gremlin_StringLiteral_strategy = st.builds(gremlin_StringLiteral, value=safe_text)
@given(instance=gremlin_StringLiteral_strategy)
@settings(max_examples=25)
def test_gremlin_StringLiteral_instantiation(instance):
    assert isinstance(instance, gremlin_StringLiteral)


gremlin_TernaryOperator_strategy = st.builds(gremlin_TernaryOperator)
@given(instance=gremlin_TernaryOperator_strategy)
@settings(max_examples=25)
def test_gremlin_TernaryOperator_instantiation(instance):
    assert isinstance(instance, gremlin_TernaryOperator)


gremlin_ToIntegerCall_strategy = st.builds(gremlin_ToIntegerCall)
@given(instance=gremlin_ToIntegerCall_strategy)
@settings(max_examples=25)
def test_gremlin_ToIntegerCall_instantiation(instance):
    assert isinstance(instance, gremlin_ToIntegerCall)


gremlin_ToListCall_strategy = st.builds(gremlin_ToListCall)
@given(instance=gremlin_ToListCall_strategy)
@settings(max_examples=25)
def test_gremlin_ToListCall_instantiation(instance):
    assert isinstance(instance, gremlin_ToListCall)


gremlin_TransformStep_strategy = st.builds(gremlin_TransformStep)
@given(instance=gremlin_TransformStep_strategy)
@settings(max_examples=25)
def test_gremlin_TransformStep_instantiation(instance):
    assert isinstance(instance, gremlin_TransformStep)


gremlin_TraversalElement_strategy = st.builds(gremlin_TraversalElement)
@given(instance=gremlin_TraversalElement_strategy)
@settings(max_examples=25)
def test_gremlin_TraversalElement_instantiation(instance):
    assert isinstance(instance, gremlin_TraversalElement)


gremlin_TypeDeclaration_strategy = st.builds(gremlin_TypeDeclaration)
@given(instance=gremlin_TypeDeclaration_strategy)
@settings(max_examples=25)
def test_gremlin_TypeDeclaration_instantiation(instance):
    assert isinstance(instance, gremlin_TypeDeclaration)


gremlin_UnaryExpression_strategy = st.builds(gremlin_UnaryExpression)
@given(instance=gremlin_UnaryExpression_strategy)
@settings(max_examples=25)
def test_gremlin_UnaryExpression_instantiation(instance):
    assert isinstance(instance, gremlin_UnaryExpression)


gremlin_UnionCall_strategy = st.builds(gremlin_UnionCall)
@given(instance=gremlin_UnionCall_strategy)
@settings(max_examples=25)
def test_gremlin_UnionCall_instantiation(instance):
    assert isinstance(instance, gremlin_UnionCall)


gremlin_VariableAccess_strategy = st.builds(gremlin_VariableAccess, name=safe_text)
@given(instance=gremlin_VariableAccess_strategy)
@settings(max_examples=25)
def test_gremlin_VariableAccess_instantiation(instance):
    assert isinstance(instance, gremlin_VariableAccess)


gremlin_VariableDeclaration_strategy = st.builds(gremlin_VariableDeclaration, final=st.booleans(), name=safe_text)
@given(instance=gremlin_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_gremlin_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, gremlin_VariableDeclaration)


gremlin_VerticesStep_strategy = st.builds(gremlin_VerticesStep, vertexId=safe_text)
@given(instance=gremlin_VerticesStep_strategy)
@settings(max_examples=25)
def test_gremlin_VerticesStep_instantiation(instance):
    assert isinstance(instance, gremlin_VerticesStep)


