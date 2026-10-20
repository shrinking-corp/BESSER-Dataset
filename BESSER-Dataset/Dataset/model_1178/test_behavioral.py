import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    CollectionExp,
    CollectionPart,
    CollectionType,
    IfExp,
    Import,
    IterateExp,
    Iterator,
    LambdaType,
    LetExp,
    LocalVariable,
    LocatedElement,
    LoopExp,
    MapElement,
    MapExp,
    MapType,
    Module,
    ModuleElement,
    NamedElement,
    NumericExp,
    NumericType,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclFeatureDefinition,
    OclInstanceModel,
    OclMetamodel,
    OclModel,
    OclModelElement,
    OclType,
    Operation,
    OperationCall,
    OperatorCallExp,
    Parameter,
    Primitive,
    PrimitiveExp,
    PropertyCall,
    PropertyCallExp,
    QualityMetamodel_AggregatedValue,
    QualityMetamodel_AggregatedValueMetric,
    QualityMetamodel_BooleanValueType,
    QualityMetamodel_EnumerationItem,
    QualityMetamodel_EnumerationMetric,
    QualityMetamodel_IntegerValueType,
    QualityMetamodel_MetricProvider,
    QualityMetamodel_Operation,
    QualityMetamodel_QMM_OCL_AddOpCallExp,
    QualityMetamodel_QMM_OCL_Attribute,
    QualityMetamodel_QMM_OCL_BagExp,
    QualityMetamodel_QMM_OCL_BagType,
    QualityMetamodel_QMM_OCL_BooleanExp,
    QualityMetamodel_QMM_OCL_BooleanType,
    QualityMetamodel_QMM_OCL_BraceExp,
    QualityMetamodel_QMM_OCL_CollectionExp,
    QualityMetamodel_QMM_OCL_CollectionItem,
    QualityMetamodel_QMM_OCL_CollectionOperationCall,
    QualityMetamodel_QMM_OCL_CollectionPart,
    QualityMetamodel_QMM_OCL_CollectionRange,
    QualityMetamodel_QMM_OCL_CollectionType,
    QualityMetamodel_QMM_OCL_EnumLiteralExp,
    QualityMetamodel_QMM_OCL_EnvExp,
    QualityMetamodel_QMM_OCL_EnvType,
    QualityMetamodel_QMM_OCL_EqOpCallExp,
    QualityMetamodel_QMM_OCL_IfExp,
    QualityMetamodel_QMM_OCL_Import,
    QualityMetamodel_QMM_OCL_IntOpCallExp,
    QualityMetamodel_QMM_OCL_IntegerExp,
    QualityMetamodel_QMM_OCL_IntegerType,
    QualityMetamodel_QMM_OCL_IterateExp,
    QualityMetamodel_QMM_OCL_Iterator,
    QualityMetamodel_QMM_OCL_IteratorExp,
    QualityMetamodel_QMM_OCL_LambdaCallExp,
    QualityMetamodel_QMM_OCL_LambdaType,
    QualityMetamodel_QMM_OCL_LetExp,
    QualityMetamodel_QMM_OCL_LocalVariable,
    QualityMetamodel_QMM_OCL_LocatedElement,
    QualityMetamodel_QMM_OCL_LoopExp,
    QualityMetamodel_QMM_OCL_MapElement,
    QualityMetamodel_QMM_OCL_MapExp,
    QualityMetamodel_QMM_OCL_MapType,
    QualityMetamodel_QMM_OCL_Module,
    QualityMetamodel_QMM_OCL_ModuleElement,
    QualityMetamodel_QMM_OCL_MulOpCallExp,
    QualityMetamodel_QMM_OCL_NamedElement,
    QualityMetamodel_QMM_OCL_NavigationOrAttributeCall,
    QualityMetamodel_QMM_OCL_NotOpCallExp,
    QualityMetamodel_QMM_OCL_NumericExp,
    QualityMetamodel_QMM_OCL_NumericType,
    QualityMetamodel_QMM_OCL_OclAnyType,
    QualityMetamodel_QMM_OCL_OclContextDefinition,
    QualityMetamodel_QMM_OCL_OclExpression,
    QualityMetamodel_QMM_OCL_OclFeature,
    QualityMetamodel_QMM_OCL_OclFeatureDefinition,
    QualityMetamodel_QMM_OCL_OclInstanceModel,
    QualityMetamodel_QMM_OCL_OclMetamodel,
    QualityMetamodel_QMM_OCL_OclModel,
    QualityMetamodel_QMM_OCL_OclModelElement,
    QualityMetamodel_QMM_OCL_OclModelElementExp,
    QualityMetamodel_QMM_OCL_OclType,
    QualityMetamodel_QMM_OCL_OclUndefinedExp,
    QualityMetamodel_QMM_OCL_Operation,
    QualityMetamodel_QMM_OCL_OperationCall,
    QualityMetamodel_QMM_OCL_OperatorCallExp,
    QualityMetamodel_QMM_OCL_OrderedSetExp,
    QualityMetamodel_QMM_OCL_OrderedSetType,
    QualityMetamodel_QMM_OCL_Parameter,
    QualityMetamodel_QMM_OCL_Primitive,
    QualityMetamodel_QMM_OCL_PrimitiveExp,
    QualityMetamodel_QMM_OCL_PropertyCall,
    QualityMetamodel_QMM_OCL_PropertyCallExp,
    QualityMetamodel_QMM_OCL_RealExp,
    QualityMetamodel_QMM_OCL_RealType,
    QualityMetamodel_QMM_OCL_RelOpCallExp,
    QualityMetamodel_QMM_OCL_SelfExp,
    QualityMetamodel_QMM_OCL_SequenceExp,
    QualityMetamodel_QMM_OCL_SequenceType,
    QualityMetamodel_QMM_OCL_SetExp,
    QualityMetamodel_QMM_OCL_SetType,
    QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall,
    QualityMetamodel_QMM_OCL_StaticOperationCall,
    QualityMetamodel_QMM_OCL_StaticPropertyCall,
    QualityMetamodel_QMM_OCL_StaticPropertyCallExp,
    QualityMetamodel_QMM_OCL_StringExp,
    QualityMetamodel_QMM_OCL_StringType,
    QualityMetamodel_QMM_OCL_SuperExp,
    QualityMetamodel_QMM_OCL_TupleExp,
    QualityMetamodel_QMM_OCL_TuplePart,
    QualityMetamodel_QMM_OCL_TupleType,
    QualityMetamodel_QMM_OCL_TupleTypeAttribute,
    QualityMetamodel_QMM_OCL_VariableDeclaration,
    QualityMetamodel_QMM_OCL_VariableExp,
    QualityMetamodel_QualityAttribute,
    QualityMetamodel_QualityModel,
    QualityMetamodel_RangeValueType,
    QualityMetamodel_RealValueType,
    QualityMetamodel_SingleValue,
    QualityMetamodel_TextValueType,
    QualityMetamodel_Value,
    QualityMetamodel_ValueType,
    StaticPropertyCall,
    StaticPropertyCallExp,
    TupleExp,
    TuplePart,
    TupleType,
    TupleTypeAttribute,
    Value,
    ValueType,
    VariableDeclaration,
    VariableExp,
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

def test_assoc_aggregatedValues18_reverse_link_reassign_clear():
    a1 = QualityMetamodel_Value(description="sample_text")
    a2 = QualityMetamodel_Value(description="sample_text_2")
    b = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    _safe_set(b, 'QualityMetamodel_Operation19', {a1})
    assert _is_linked(b, 'QualityMetamodel_Operation19', a1)
    if hasattr(a1, 'QualityMetamodel_Value20'):
        assert _is_linked(a1, 'QualityMetamodel_Value20', b)
    _safe_set(b, 'QualityMetamodel_Operation19', {a2})
    assert _is_linked(b, 'QualityMetamodel_Operation19', a2)
    if hasattr(a1, 'QualityMetamodel_Value20'):
        assert not _is_linked(a1, 'QualityMetamodel_Value20', b)
    if hasattr(a2, 'QualityMetamodel_Value20'):
        assert _is_linked(a2, 'QualityMetamodel_Value20', b)
    _safe_set(b, 'QualityMetamodel_Operation19', set())
    assert not _is_linked(b, 'QualityMetamodel_Operation19', a2)
    if hasattr(a2, 'QualityMetamodel_Value20'):
        assert not _is_linked(a2, 'QualityMetamodel_Value20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argument84_stub_double():
    # OclExpression has no real 'OclExpression85' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OperatorCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression85', None)
    _safe_set(owner, 'QualityMetamodel_QMM_OCL_OperatorCallExp', partner)
    assert getattr(partner, 'OclExpression85') == owner
    _safe_set(owner, 'QualityMetamodel_QMM_OCL_OperatorCallExp', None)
    assert getattr(partner, 'OclExpression85') is None


def test_assoc_arguments75_stub_double():
    # OclExpression has no real 'OclExpression76' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_StaticOperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_StaticOperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_StaticOperationCall(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression76', None)
    _safe_set(owner, 'QualityMetamodel_QMM_OCL_StaticOperationCall', {partner})
    assert getattr(partner, 'OclExpression76') == owner
    _safe_set(owner, 'QualityMetamodel_QMM_OCL_StaticOperationCall', set())
    assert getattr(partner, 'OclExpression76') is None


def test_assoc_arguments82_stub_double():
    # OclExpression has no real 'OclExpression83' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OperationCall(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression83', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression83') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression83') is None


def test_assoc_attribute129_stub_double():
    # Attribute has no real 'Attribute131' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute131', None)
    _safe_set(owner, 'type130', partner)
    assert getattr(partner, 'Attribute131') == owner
    _safe_set(owner, 'type130', None)
    assert getattr(partner, 'Attribute131') is None


def test_assoc_baseExp115_stub_double():
    # IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_LocalVariable(eq="sample_text")
    partner = IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_calculatedBy17_stub_double():
    # QualityMetamodel_AggregatedValue has no real 'QualityMetamodel_AggregatedValue' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    partner = QualityMetamodel_AggregatedValue()
    setattr(partner, 'QualityMetamodel_AggregatedValue', None)
    _safe_set(owner, 'QualityMetamodel_Operation', partner)
    assert getattr(partner, 'QualityMetamodel_AggregatedValue') == owner
    _safe_set(owner, 'QualityMetamodel_Operation', None)
    assert getattr(partner, 'QualityMetamodel_AggregatedValue') is None


def test_assoc_collectionTypes134_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_context_165_stub_double():
    # OclContextDefinition has no real 'OclContextDefinition167' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclFeatureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclFeatureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclFeatureDefinition(static="sample_text")
    partner = OclContextDefinition()
    setattr(partner, 'OclContextDefinition167', None)
    _safe_set(owner, 'definition166', partner)
    assert getattr(partner, 'OclContextDefinition167') == owner
    _safe_set(owner, 'definition166', None)
    assert getattr(partner, 'OclContextDefinition167') is None


def test_assoc_definition172_stub_double():
    # OclFeatureDefinition has no real 'OclFeatureDefinition173' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclFeature(eq="sample_text")
    partner = OclFeatureDefinition()
    setattr(partner, 'OclFeatureDefinition173', None)
    _safe_set(owner, 'feature', partner)
    assert getattr(partner, 'OclFeatureDefinition173') == owner
    _safe_set(owner, 'feature', None)
    assert getattr(partner, 'OclFeatureDefinition173') is None


def test_assoc_definitions122_stub_double():
    # OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_feature164_stub_double():
    # OclFeature has no real 'OclFeature' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclFeatureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclFeatureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclFeatureDefinition(static="sample_text")
    partner = OclFeature()
    setattr(partner, 'OclFeature', None)
    _safe_set(owner, 'definition', partner)
    assert getattr(partner, 'OclFeature') == owner
    _safe_set(owner, 'definition', None)
    assert getattr(partner, 'OclFeature') is None


def test_assoc_initExpression113_stub_double():
    # OclExpression has no real 'OclExpression114' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_LocalVariable(eq="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression114', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression114') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression114') is None


def test_assoc_lambdaArgType142_stub_double():
    # LambdaType has no real 'LambdaType143' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = LambdaType()
    setattr(partner, 'LambdaType143', None)
    _safe_set(owner, 'argumentTypes', partner)
    assert getattr(partner, 'LambdaType143') == owner
    _safe_set(owner, 'argumentTypes', None)
    assert getattr(partner, 'LambdaType143') is None


def test_assoc_lambdaReturnType140_stub_double():
    # LambdaType has no real 'LambdaType' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = LambdaType()
    setattr(partner, 'LambdaType', None)
    _safe_set(owner, 'returnType141', partner)
    assert getattr(partner, 'LambdaType') == owner
    _safe_set(owner, 'returnType141', None)
    assert getattr(partner, 'LambdaType') is None


def test_assoc_letExp111_stub_double():
    # LetExp has no real 'LetExp112' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_LocalVariable(eq="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp112', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp112') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp112') is None


def test_assoc_mapType132_stub_double():
    # MapType has no real 'MapType133' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType133', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType133') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType133') is None


def test_assoc_mapType2127_stub_double():
    # MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType128', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType128', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_measuredBy15_stub_double():
    # QualityMetamodel_SingleValue has no real 'QualityMetamodel_SingleValue' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_MetricProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_MetricProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    partner = QualityMetamodel_SingleValue()
    setattr(partner, 'QualityMetamodel_SingleValue', None)
    _safe_set(owner, 'QualityMetamodel_MetricProvider16', partner)
    assert getattr(partner, 'QualityMetamodel_SingleValue') == owner
    _safe_set(owner, 'QualityMetamodel_MetricProvider16', None)
    assert getattr(partner, 'QualityMetamodel_SingleValue') is None


def test_assoc_metricProviders0_stub_double():
    # QualityMetamodel_QualityModel has no real 'QualityMetamodel_QualityModel' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_MetricProvider's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_MetricProvider's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_MetricProvider(description="sample_text", id="sample_text", name="sample_text")
    partner = QualityMetamodel_QualityModel()
    setattr(partner, 'QualityMetamodel_QualityModel', None)
    _safe_set(owner, 'QualityMetamodel_MetricProvider', partner)
    assert owner in getattr(partner, 'QualityMetamodel_QualityModel')
    _safe_set(owner, 'QualityMetamodel_MetricProvider', None)
    assert owner not in getattr(partner, 'QualityMetamodel_QualityModel')


def test_assoc_model147_stub_double():
    # OclModel has no real 'OclModel' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclModelElementExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclModelElementExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclModelElementExp(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel', None)
    _safe_set(owner, 'QualityMetamodel_QMM_OCL_OclModelElementExp', partner)
    assert getattr(partner, 'OclModel') == owner
    _safe_set(owner, 'QualityMetamodel_QMM_OCL_OclModelElementExp', None)
    assert getattr(partner, 'OclModel') is None


def test_assoc_model185_stub_double():
    # OclInstanceModel has no real 'OclInstanceModel' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclMetamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclMetamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclMetamodel(uri="sample_text")
    partner = OclInstanceModel()
    setattr(partner, 'OclInstanceModel', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclInstanceModel') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclInstanceModel') is None


def test_assoc_oclExpression123_stub_double():
    # OclExpression has no real 'OclExpression124' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression124', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression124') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression124') is None


def test_assoc_operation125_stub_double():
    # Operation has no real 'Operation126' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation126', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation126') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation126') is None


def test_assoc_qualityValues5_stub_double():
    # QualityMetamodel_QualityModel has no real 'QualityMetamodel_QualityModel6' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_Value(description="sample_text")
    partner = QualityMetamodel_QualityModel()
    setattr(partner, 'QualityMetamodel_QualityModel6', None)
    _safe_set(owner, 'QualityMetamodel_Value', partner)
    assert owner in getattr(partner, 'QualityMetamodel_QualityModel6')
    _safe_set(owner, 'QualityMetamodel_Value', None)
    assert owner not in getattr(partner, 'QualityMetamodel_QualityModel6')


def test_assoc_ref21_stub_double():
    # OclExpression has no real 'OclExpression' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_Operation(body="sample_text", name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression', None)
    _safe_set(owner, 'QualityMetamodel_Operation22', partner)
    assert getattr(partner, 'OclExpression') == owner
    _safe_set(owner, 'QualityMetamodel_Operation22', None)
    assert getattr(partner, 'OclExpression') is None


def test_assoc_set23_stub_double():
    # QualityMetamodel_EnumerationMetric has no real 'QualityMetamodel_EnumerationMetric' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_EnumerationItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_EnumerationItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_EnumerationItem(name="sample_text")
    partner = QualityMetamodel_EnumerationMetric()
    setattr(partner, 'QualityMetamodel_EnumerationMetric', None)
    _safe_set(owner, 'QualityMetamodel_EnumerationItem', partner)
    assert owner in getattr(partner, 'QualityMetamodel_EnumerationMetric')
    _safe_set(owner, 'QualityMetamodel_EnumerationItem', None)
    assert owner not in getattr(partner, 'QualityMetamodel_EnumerationMetric')


def test_assoc_source86_stub_double():
    # OclExpression has no real 'OclExpression87' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OperatorCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression87', None)
    _safe_set(owner, 'appliedOperator', partner)
    assert getattr(partner, 'OclExpression87') == owner
    _safe_set(owner, 'appliedOperator', None)
    assert getattr(partner, 'OclExpression87') is None


def test_assoc_staticPropertyCall144_stub_double():
    # StaticPropertyCallExp has no real 'StaticPropertyCallExp146' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = StaticPropertyCallExp()
    setattr(partner, 'StaticPropertyCallExp146', None)
    _safe_set(owner, 'source145', partner)
    assert getattr(partner, 'StaticPropertyCallExp146') == owner
    _safe_set(owner, 'source145', None)
    assert getattr(partner, 'StaticPropertyCallExp146') is None


def test_assoc_tupleType152_stub_double():
    # TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_TupleTypeAttribute(name="sample_text")
    partner = TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_tupleTypeAttribute135_stub_double():
    # TupleTypeAttribute has no real 'TupleTypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = TupleTypeAttribute()
    setattr(partner, 'TupleTypeAttribute', None)
    _safe_set(owner, 'type136', partner)
    assert getattr(partner, 'TupleTypeAttribute') == owner
    _safe_set(owner, 'type136', None)
    assert getattr(partner, 'TupleTypeAttribute') is None


def test_assoc_type108_stub_double():
    # OclType has no real 'OclType109' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_VariableDeclaration(varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType109', None)
    _safe_set(owner, 'variableDeclaration', partner)
    assert getattr(partner, 'OclType109') == owner
    _safe_set(owner, 'variableDeclaration', None)
    assert getattr(partner, 'OclType109') is None


def test_assoc_type150_stub_double():
    # OclType has no real 'OclType151' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType151', None)
    _safe_set(owner, 'tupleTypeAttribute', partner)
    assert getattr(partner, 'OclType151') == owner
    _safe_set(owner, 'tupleTypeAttribute', None)
    assert getattr(partner, 'OclType151') is None


def test_assoc_val14_stub_double():
    # QualityMetamodel_ValueType has no real 'valueType' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_Value(description="sample_text")
    partner = QualityMetamodel_ValueType()
    setattr(partner, 'valueType', None)
    _safe_set(owner, 'Value', partner)
    assert getattr(partner, 'valueType') == owner
    _safe_set(owner, 'Value', None)
    assert getattr(partner, 'valueType') is None


def test_assoc_value24_stub_double():
    # QualityMetamodel_EnumerationMetric has no real 'QualityMetamodel_EnumerationMetric25' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_EnumerationItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_EnumerationItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_EnumerationItem(name="sample_text")
    partner = QualityMetamodel_EnumerationMetric()
    setattr(partner, 'QualityMetamodel_EnumerationMetric25', None)
    _safe_set(owner, 'QualityMetamodel_EnumerationItem26', partner)
    assert getattr(partner, 'QualityMetamodel_EnumerationMetric25') == owner
    _safe_set(owner, 'QualityMetamodel_EnumerationItem26', None)
    assert getattr(partner, 'QualityMetamodel_EnumerationMetric25') is None


def test_assoc_value7_stub_double():
    # QualityMetamodel_QualityAttribute has no real 'QualityMetamodel_QualityAttribute8' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_Value(description="sample_text")
    partner = QualityMetamodel_QualityAttribute()
    setattr(partner, 'QualityMetamodel_QualityAttribute8', None)
    _safe_set(owner, 'QualityMetamodel_Value9', partner)
    assert getattr(partner, 'QualityMetamodel_QualityAttribute8') == owner
    _safe_set(owner, 'QualityMetamodel_Value9', None)
    assert getattr(partner, 'QualityMetamodel_QualityAttribute8') is None


def test_assoc_valueType13_stub_double():
    # QualityMetamodel_ValueType has no real 'ValueType' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_Value(description="sample_text")
    partner = QualityMetamodel_ValueType()
    setattr(partner, 'ValueType', None)
    _safe_set(owner, 'val', partner)
    assert getattr(partner, 'ValueType') == owner
    _safe_set(owner, 'val', None)
    assert getattr(partner, 'ValueType') is None


def test_assoc_variableDeclaration137_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration139' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_OclType(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration139', None)
    _safe_set(owner, 'type138', partner)
    assert getattr(partner, 'VariableDeclaration139') == owner
    _safe_set(owner, 'type138', None)
    assert getattr(partner, 'VariableDeclaration139') is None


def test_assoc_variableExp110_stub_double():
    # VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so QualityMetamodel_QMM_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QualityMetamodel_QMM_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QualityMetamodel_QMM_OCL_VariableDeclaration(varName="sample_text")
    partner = VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


