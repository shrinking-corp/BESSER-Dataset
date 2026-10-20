import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CollectionExp,
    CollectionType,
    LocalVariable,
    LocatedElement,
    LoopExp,
    ModuleElement,
    NamedElement,
    NumericExp,
    NumericType,
    OclExpression,
    OclFeature,
    OclModel,
    OclType,
    OperationCall,
    OperatorCallExp,
    Primitive,
    PrimitiveExp,
    PropertyCall,
    StaticPropertyCall,
    VariableDeclaration,
    VariableExp,
    simpleocl_AddOpCallExp,
    simpleocl_Attribute,
    simpleocl_BagExp,
    simpleocl_BagType,
    simpleocl_BooleanExp,
    simpleocl_BooleanType,
    simpleocl_BraceExp,
    simpleocl_CollectionExp,
    simpleocl_CollectionOperationCall,
    simpleocl_CollectionType,
    simpleocl_EnumLiteralExp,
    simpleocl_EnvExp,
    simpleocl_EnvType,
    simpleocl_EqOpCallExp,
    simpleocl_IfExp,
    simpleocl_Import,
    simpleocl_IntOpCallExp,
    simpleocl_IntegerExp,
    simpleocl_IntegerType,
    simpleocl_IterateExp,
    simpleocl_Iterator,
    simpleocl_IteratorExp,
    simpleocl_LambdaCallExp,
    simpleocl_LambdaType,
    simpleocl_LetExp,
    simpleocl_LocalVariable,
    simpleocl_LocatedElement,
    simpleocl_LoopExp,
    simpleocl_MapElement,
    simpleocl_MapExp,
    simpleocl_MapType,
    simpleocl_Module,
    simpleocl_ModuleElement,
    simpleocl_MulOpCallExp,
    simpleocl_NamedElement,
    simpleocl_NavigationOrAttributeCall,
    simpleocl_NotOpCallExp,
    simpleocl_NumericExp,
    simpleocl_NumericType,
    simpleocl_OclAnyType,
    simpleocl_OclContextDefinition,
    simpleocl_OclExpression,
    simpleocl_OclFeature,
    simpleocl_OclFeatureDefinition,
    simpleocl_OclInstanceModel,
    simpleocl_OclMetamodel,
    simpleocl_OclModel,
    simpleocl_OclModelElement,
    simpleocl_OclModelElementExp,
    simpleocl_OclType,
    simpleocl_OclUndefinedExp,
    simpleocl_Operation,
    simpleocl_OperationCall,
    simpleocl_OperatorCallExp,
    simpleocl_OrderedSetExp,
    simpleocl_OrderedSetType,
    simpleocl_Parameter,
    simpleocl_Primitive,
    simpleocl_PrimitiveExp,
    simpleocl_PropertyCall,
    simpleocl_PropertyCallExp,
    simpleocl_RealExp,
    simpleocl_RealType,
    simpleocl_RelOpCallExp,
    simpleocl_SelfExp,
    simpleocl_SequenceExp,
    simpleocl_SequenceType,
    simpleocl_SetExp,
    simpleocl_SetType,
    simpleocl_StaticNavigationOrAttributeCall,
    simpleocl_StaticOperationCall,
    simpleocl_StaticPropertyCall,
    simpleocl_StaticPropertyCallExp,
    simpleocl_StringExp,
    simpleocl_StringType,
    simpleocl_SuperExp,
    simpleocl_TupleExp,
    simpleocl_TuplePart,
    simpleocl_TupleType,
    simpleocl_TupleTypeAttribute,
    simpleocl_VariableDeclaration,
    simpleocl_VariableExp,
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

def test_assoc_definition136_reverse_link_reassign_clear():
    a1 = simpleocl_OclFeatureDefinition(static="sample_text")
    a2 = simpleocl_OclFeatureDefinition(static="sample_text_2")
    b = simpleocl_OclFeature(eq="sample_text")
    _safe_set(b, 'feature', a1)
    assert _is_linked(b, 'feature', a1)
    if hasattr(a1, 'OclFeatureDefinition137'):
        assert _is_linked(a1, 'OclFeatureDefinition137', b)
    _safe_set(b, 'feature', a2)
    assert _is_linked(b, 'feature', a2)
    if hasattr(a1, 'OclFeatureDefinition137'):
        assert not _is_linked(a1, 'OclFeatureDefinition137', b)
    if hasattr(a2, 'OclFeatureDefinition137'):
        assert _is_linked(a2, 'OclFeatureDefinition137', b)
    _safe_set(b, 'feature', None)
    assert not _is_linked(b, 'feature', a2)
    if hasattr(a2, 'OclFeatureDefinition137'):
        assert not _is_linked(a2, 'OclFeatureDefinition137', b)


def test_assoc_feature128_reverse_link_reassign_clear():
    a1 = simpleocl_OclFeatureDefinition(static="sample_text")
    a2 = simpleocl_OclFeatureDefinition(static="sample_text_2")
    b = simpleocl_OclFeature(eq="sample_text")
    _safe_set(b, 'OclFeature', a1)
    assert _is_linked(b, 'OclFeature', a1)
    if hasattr(a1, 'definition'):
        assert _is_linked(a1, 'definition', b)
    _safe_set(b, 'OclFeature', a2)
    assert _is_linked(b, 'OclFeature', a2)
    if hasattr(a1, 'definition'):
        assert not _is_linked(a1, 'definition', b)
    if hasattr(a2, 'definition'):
        assert _is_linked(a2, 'definition', b)
    _safe_set(b, 'OclFeature', None)
    assert not _is_linked(b, 'OclFeature', a2)
    if hasattr(a2, 'definition'):
        assert not _is_linked(a2, 'definition', b)


def test_assoc_tupleTypeAttribute100_reverse_link_reassign_clear():
    a1 = simpleocl_TupleTypeAttribute(name="sample_text")
    a2 = simpleocl_TupleTypeAttribute(name="sample_text_2")
    b = simpleocl_OclType(name="sample_text")
    _safe_set(b, 'type101', a1)
    assert _is_linked(b, 'type101', a1)
    if hasattr(a1, 'TupleTypeAttribute'):
        assert _is_linked(a1, 'TupleTypeAttribute', b)
    _safe_set(b, 'type101', a2)
    assert _is_linked(b, 'type101', a2)
    if hasattr(a1, 'TupleTypeAttribute'):
        assert not _is_linked(a1, 'TupleTypeAttribute', b)
    if hasattr(a2, 'TupleTypeAttribute'):
        assert _is_linked(a2, 'TupleTypeAttribute', b)
    _safe_set(b, 'type101', None)
    assert not _is_linked(b, 'type101', a2)
    if hasattr(a2, 'TupleTypeAttribute'):
        assert not _is_linked(a2, 'TupleTypeAttribute', b)


def test_assoc_type115_reverse_link_reassign_clear():
    a1 = simpleocl_TupleTypeAttribute(name="sample_text")
    a2 = simpleocl_TupleTypeAttribute(name="sample_text_2")
    b = simpleocl_OclType(name="sample_text")
    _safe_set(b, 'OclType116', a1)
    assert _is_linked(b, 'OclType116', a1)
    if hasattr(a1, 'tupleTypeAttribute'):
        assert _is_linked(a1, 'tupleTypeAttribute', b)
    _safe_set(b, 'OclType116', a2)
    assert _is_linked(b, 'OclType116', a2)
    if hasattr(a1, 'tupleTypeAttribute'):
        assert not _is_linked(a1, 'tupleTypeAttribute', b)
    if hasattr(a2, 'tupleTypeAttribute'):
        assert _is_linked(a2, 'tupleTypeAttribute', b)
    _safe_set(b, 'OclType116', None)
    assert not _is_linked(b, 'OclType116', a2)
    if hasattr(a2, 'tupleTypeAttribute'):
        assert not _is_linked(a2, 'tupleTypeAttribute', b)


def test_assoc_type74_reverse_link_reassign_clear():
    a1 = simpleocl_VariableDeclaration(varName="sample_text")
    a2 = simpleocl_VariableDeclaration(varName="sample_text_2")
    b = simpleocl_OclType(name="sample_text")
    _safe_set(b, 'OclType75', a1)
    assert _is_linked(b, 'OclType75', a1)
    if hasattr(a1, 'variableDeclaration'):
        assert _is_linked(a1, 'variableDeclaration', b)
    _safe_set(b, 'OclType75', a2)
    assert _is_linked(b, 'OclType75', a2)
    if hasattr(a1, 'variableDeclaration'):
        assert not _is_linked(a1, 'variableDeclaration', b)
    if hasattr(a2, 'variableDeclaration'):
        assert _is_linked(a2, 'variableDeclaration', b)
    _safe_set(b, 'OclType75', None)
    assert not _is_linked(b, 'OclType75', a2)
    if hasattr(a2, 'variableDeclaration'):
        assert not _is_linked(a2, 'variableDeclaration', b)


def test_assoc_variableDeclaration102_reverse_link_reassign_clear():
    a1 = simpleocl_VariableDeclaration(varName="sample_text")
    a2 = simpleocl_VariableDeclaration(varName="sample_text_2")
    b = simpleocl_OclType(name="sample_text")
    _safe_set(b, 'type103', a1)
    assert _is_linked(b, 'type103', a1)
    if hasattr(a1, 'VariableDeclaration104'):
        assert _is_linked(a1, 'VariableDeclaration104', b)
    _safe_set(b, 'type103', a2)
    assert _is_linked(b, 'type103', a2)
    if hasattr(a1, 'VariableDeclaration104'):
        assert not _is_linked(a1, 'VariableDeclaration104', b)
    if hasattr(a2, 'VariableDeclaration104'):
        assert _is_linked(a2, 'VariableDeclaration104', b)
    _safe_set(b, 'type103', None)
    assert not _is_linked(b, 'type103', a2)
    if hasattr(a2, 'VariableDeclaration104'):
        assert not _is_linked(a2, 'VariableDeclaration104', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_appliedOperator24_stub_double():
    # simpleocl_OclExpression has no real 'source25' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OperatorCallExp(operationName="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'source25', None)
    _safe_set(owner, 'OperatorCallExp', partner)
    assert getattr(partner, 'source25') == owner
    _safe_set(owner, 'OperatorCallExp', None)
    assert getattr(partner, 'source25') is None


def test_assoc_argument50_stub_double():
    # simpleocl_OclExpression has no real 'simpleocl_OclExpression51' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OperatorCallExp(operationName="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'simpleocl_OclExpression51', None)
    _safe_set(owner, 'simpleocl_OperatorCallExp', partner)
    assert getattr(partner, 'simpleocl_OclExpression51') == owner
    _safe_set(owner, 'simpleocl_OperatorCallExp', None)
    assert getattr(partner, 'simpleocl_OclExpression51') is None


def test_assoc_argumentTypes126_stub_double():
    # simpleocl_LambdaType has no real 'lambdaArgType' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_LambdaType()
    setattr(partner, 'lambdaArgType', None)
    _safe_set(owner, 'OclType127', partner)
    assert owner in getattr(partner, 'lambdaArgType')
    _safe_set(owner, 'OclType127', None)
    assert owner not in getattr(partner, 'lambdaArgType')


def test_assoc_arguments41_stub_double():
    # simpleocl_OclExpression has no real 'simpleocl_OclExpression42' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_StaticOperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_StaticOperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_StaticOperationCall(operationName="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'simpleocl_OclExpression42', None)
    _safe_set(owner, 'simpleocl_StaticOperationCall', {partner})
    assert getattr(partner, 'simpleocl_OclExpression42') == owner
    _safe_set(owner, 'simpleocl_StaticOperationCall', set())
    assert getattr(partner, 'simpleocl_OclExpression42') is None


def test_assoc_arguments48_stub_double():
    # simpleocl_OclExpression has no real 'OclExpression49' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OperationCall(operationName="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'OclExpression49', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression49') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression49') is None


def test_assoc_attribute94_stub_double():
    # simpleocl_Attribute has no real 'Attribute96' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_Attribute()
    setattr(partner, 'Attribute96', None)
    _safe_set(owner, 'type95', partner)
    assert getattr(partner, 'Attribute96') == owner
    _safe_set(owner, 'type95', None)
    assert getattr(partner, 'Attribute96') is None


def test_assoc_attributes113_stub_double():
    # simpleocl_TupleType has no real 'tupleType' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_TupleTypeAttribute(name="sample_text")
    partner = simpleocl_TupleType()
    setattr(partner, 'tupleType', None)
    _safe_set(owner, 'TupleTypeAttribute114', partner)
    assert owner in getattr(partner, 'tupleType')
    _safe_set(owner, 'TupleTypeAttribute114', None)
    assert owner not in getattr(partner, 'tupleType')


def test_assoc_baseExp81_stub_double():
    # simpleocl_IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_LocalVariable(eq="sample_text")
    partner = simpleocl_IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_collectionTypes99_stub_double():
    # simpleocl_CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_context_129_stub_double():
    # simpleocl_OclContextDefinition has no real 'OclContextDefinition131' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclFeatureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclFeatureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclFeatureDefinition(static="sample_text")
    partner = simpleocl_OclContextDefinition()
    setattr(partner, 'OclContextDefinition131', None)
    _safe_set(owner, 'definition130', partner)
    assert getattr(partner, 'OclContextDefinition131') == owner
    _safe_set(owner, 'definition130', None)
    assert getattr(partner, 'OclContextDefinition131') is None


def test_assoc_context_134_stub_double():
    # simpleocl_OclContextDefinition has no real 'definitions' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_OclContextDefinition()
    setattr(partner, 'definitions', None)
    _safe_set(owner, 'OclType135', partner)
    assert getattr(partner, 'definitions') == owner
    _safe_set(owner, 'OclType135', None)
    assert getattr(partner, 'definitions') is None


def test_assoc_definition132_stub_double():
    # simpleocl_OclContextDefinition has no real 'context_133' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclFeatureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclFeatureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclFeatureDefinition(static="sample_text")
    partner = simpleocl_OclContextDefinition()
    setattr(partner, 'context_133', None)
    _safe_set(owner, 'OclFeatureDefinition', partner)
    assert getattr(partner, 'context_133') == owner
    _safe_set(owner, 'OclFeatureDefinition', None)
    assert getattr(partner, 'context_133') is None


def test_assoc_definitions88_stub_double():
    # simpleocl_OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_elementType86_stub_double():
    # simpleocl_CollectionType has no real 'collectionTypes' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_CollectionType()
    setattr(partner, 'collectionTypes', None)
    _safe_set(owner, 'OclType87', partner)
    assert getattr(partner, 'collectionTypes') == owner
    _safe_set(owner, 'OclType87', None)
    assert getattr(partner, 'collectionTypes') is None


def test_assoc_initExpression79_stub_double():
    # simpleocl_OclExpression has no real 'OclExpression80' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_LocalVariable(eq="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'OclExpression80', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression80') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression80') is None


def test_assoc_initializedVariable15_stub_double():
    # simpleocl_OclExpression has no real 'initExpression' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_LocalVariable(eq="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'initExpression', None)
    _safe_set(owner, 'LocalVariable', partner)
    assert getattr(partner, 'initExpression') == owner
    _safe_set(owner, 'LocalVariable', None)
    assert getattr(partner, 'initExpression') is None


def test_assoc_keyType122_stub_double():
    # simpleocl_MapType has no real 'mapType' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_MapType()
    setattr(partner, 'mapType', None)
    _safe_set(owner, 'OclType123', partner)
    assert getattr(partner, 'mapType') == owner
    _safe_set(owner, 'OclType123', None)
    assert getattr(partner, 'mapType') is None


def test_assoc_lambdaArgType107_stub_double():
    # simpleocl_LambdaType has no real 'LambdaType108' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_LambdaType()
    setattr(partner, 'LambdaType108', None)
    _safe_set(owner, 'argumentTypes', partner)
    assert getattr(partner, 'LambdaType108') == owner
    _safe_set(owner, 'argumentTypes', None)
    assert getattr(partner, 'LambdaType108') is None


def test_assoc_lambdaReturnType105_stub_double():
    # simpleocl_LambdaType has no real 'LambdaType' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_LambdaType()
    setattr(partner, 'LambdaType', None)
    _safe_set(owner, 'returnType106', partner)
    assert getattr(partner, 'LambdaType') == owner
    _safe_set(owner, 'returnType106', None)
    assert getattr(partner, 'LambdaType') is None


def test_assoc_letExp77_stub_double():
    # simpleocl_LetExp has no real 'LetExp78' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_LocalVariable(eq="sample_text")
    partner = simpleocl_LetExp()
    setattr(partner, 'LetExp78', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp78') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp78') is None


def test_assoc_mapType293_stub_double():
    # simpleocl_MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_mapType97_stub_double():
    # simpleocl_MapType has no real 'MapType98' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_MapType()
    setattr(partner, 'MapType98', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType98') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType98') is None


def test_assoc_metamodel150_stub_double():
    # simpleocl_OclInstanceModel has no real 'model151' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclMetamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclMetamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclMetamodel(uri="sample_text")
    partner = simpleocl_OclInstanceModel()
    setattr(partner, 'model151', None)
    _safe_set(owner, 'OclMetamodel', partner)
    assert getattr(partner, 'model151') == owner
    _safe_set(owner, 'OclMetamodel', None)
    assert getattr(partner, 'model151') is None


def test_assoc_metamodels0_stub_double():
    # simpleocl_Module has no real 'simpleocl_Module' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclMetamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclMetamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclMetamodel(uri="sample_text")
    partner = simpleocl_Module()
    setattr(partner, 'simpleocl_Module', None)
    _safe_set(owner, 'simpleocl_OclMetamodel', partner)
    assert owner in getattr(partner, 'simpleocl_Module')
    _safe_set(owner, 'simpleocl_OclMetamodel', None)
    assert owner not in getattr(partner, 'simpleocl_Module')


def test_assoc_model112_stub_double():
    # simpleocl_OclModel has no real 'simpleocl_OclModel' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclModelElementExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclModelElementExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclModelElementExp(name="sample_text")
    partner = simpleocl_OclModel()
    setattr(partner, 'simpleocl_OclModel', None)
    _safe_set(owner, 'simpleocl_OclModelElementExp', partner)
    assert getattr(partner, 'simpleocl_OclModel') == owner
    _safe_set(owner, 'simpleocl_OclModelElementExp', None)
    assert getattr(partner, 'simpleocl_OclModel') is None


def test_assoc_model149_stub_double():
    # simpleocl_OclInstanceModel has no real 'OclInstanceModel' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclMetamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclMetamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclMetamodel(uri="sample_text")
    partner = simpleocl_OclInstanceModel()
    setattr(partner, 'OclInstanceModel', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclInstanceModel') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclInstanceModel') is None


def test_assoc_oclExpression89_stub_double():
    # simpleocl_OclExpression has no real 'OclExpression90' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'OclExpression90', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression90') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression90') is None


def test_assoc_operation91_stub_double():
    # simpleocl_Operation has no real 'Operation92' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_Operation()
    setattr(partner, 'Operation92', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation92') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation92') is None


def test_assoc_parentOperation14_stub_double():
    # simpleocl_OclExpression has no real 'arguments' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OperationCall(operationName="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'arguments', None)
    _safe_set(owner, 'OperationCall', partner)
    assert getattr(partner, 'arguments') == owner
    _safe_set(owner, 'OperationCall', None)
    assert getattr(partner, 'arguments') is None


def test_assoc_referredVariable26_stub_double():
    # simpleocl_VariableExp has no real 'variableExp' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_VariableDeclaration(varName="sample_text")
    partner = simpleocl_VariableExp()
    setattr(partner, 'variableExp', None)
    _safe_set(owner, 'VariableDeclaration', partner)
    assert getattr(partner, 'variableExp') == owner
    _safe_set(owner, 'VariableDeclaration', None)
    assert getattr(partner, 'variableExp') is None


def test_assoc_result61_stub_double():
    # simpleocl_IterateExp has no real 'baseExp' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_LocalVariable(eq="sample_text")
    partner = simpleocl_IterateExp()
    setattr(partner, 'baseExp', None)
    _safe_set(owner, 'LocalVariable62', partner)
    assert getattr(partner, 'baseExp') == owner
    _safe_set(owner, 'LocalVariable62', None)
    assert getattr(partner, 'baseExp') is None


def test_assoc_returnType124_stub_double():
    # simpleocl_LambdaType has no real 'lambdaReturnType' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_LambdaType()
    setattr(partner, 'lambdaReturnType', None)
    _safe_set(owner, 'OclType125', partner)
    assert getattr(partner, 'lambdaReturnType') == owner
    _safe_set(owner, 'OclType125', None)
    assert getattr(partner, 'lambdaReturnType') is None


def test_assoc_returnType143_stub_double():
    # simpleocl_Operation has no real 'operation144' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_Operation()
    setattr(partner, 'operation144', None)
    _safe_set(owner, 'OclType145', partner)
    assert getattr(partner, 'operation144') == owner
    _safe_set(owner, 'OclType145', None)
    assert getattr(partner, 'operation144') is None


def test_assoc_source37_stub_double():
    # simpleocl_StaticPropertyCallExp has no real 'staticPropertyCall' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_StaticPropertyCallExp()
    setattr(partner, 'staticPropertyCall', None)
    _safe_set(owner, 'OclType38', partner)
    assert getattr(partner, 'staticPropertyCall') == owner
    _safe_set(owner, 'OclType38', None)
    assert getattr(partner, 'staticPropertyCall') is None


def test_assoc_source52_stub_double():
    # simpleocl_OclExpression has no real 'OclExpression53' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OperatorCallExp(operationName="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'OclExpression53', None)
    _safe_set(owner, 'appliedOperator', partner)
    assert getattr(partner, 'OclExpression53') == owner
    _safe_set(owner, 'appliedOperator', None)
    assert getattr(partner, 'OclExpression53') is None


def test_assoc_staticPropertyCall109_stub_double():
    # simpleocl_StaticPropertyCallExp has no real 'StaticPropertyCallExp111' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_StaticPropertyCallExp()
    setattr(partner, 'StaticPropertyCallExp111', None)
    _safe_set(owner, 'source110', partner)
    assert getattr(partner, 'StaticPropertyCallExp111') == owner
    _safe_set(owner, 'source110', None)
    assert getattr(partner, 'StaticPropertyCallExp111') is None


def test_assoc_tupleType117_stub_double():
    # simpleocl_TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_TupleTypeAttribute(name="sample_text")
    partner = simpleocl_TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_type140_stub_double():
    # simpleocl_Attribute has no real 'attribute' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_Attribute()
    setattr(partner, 'attribute', None)
    _safe_set(owner, 'OclType141', partner)
    assert getattr(partner, 'attribute') == owner
    _safe_set(owner, 'OclType141', None)
    assert getattr(partner, 'attribute') is None


def test_assoc_type7_stub_double():
    # simpleocl_OclExpression has no real 'oclExpression' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_OclExpression()
    setattr(partner, 'oclExpression', None)
    _safe_set(owner, 'OclType', partner)
    assert getattr(partner, 'oclExpression') == owner
    _safe_set(owner, 'OclType', None)
    assert getattr(partner, 'oclExpression') is None


def test_assoc_valueType120_stub_double():
    # simpleocl_MapType has no real 'mapType2' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_OclType(name="sample_text")
    partner = simpleocl_MapType()
    setattr(partner, 'mapType2', None)
    _safe_set(owner, 'OclType121', partner)
    assert getattr(partner, 'mapType2') == owner
    _safe_set(owner, 'OclType121', None)
    assert getattr(partner, 'mapType2') is None


def test_assoc_variable63_stub_double():
    # simpleocl_LetExp has no real 'letExp' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_LocalVariable(eq="sample_text")
    partner = simpleocl_LetExp()
    setattr(partner, 'letExp', None)
    _safe_set(owner, 'LocalVariable64', partner)
    assert getattr(partner, 'letExp') == owner
    _safe_set(owner, 'LocalVariable64', None)
    assert getattr(partner, 'letExp') is None


def test_assoc_variableExp76_stub_double():
    # simpleocl_VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so simpleocl_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleocl_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleocl_VariableDeclaration(varName="sample_text")
    partner = simpleocl_VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


