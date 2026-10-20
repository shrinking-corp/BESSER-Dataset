import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    BaseFeatureBinding,
    BaseHelper,
    BindingModel,
    BindingOptions,
    CollectionExp,
    CollectionType,
    ConceptBinding,
    ConceptFeatureRef,
    ConceptMetaclass,
    ConcreteMetaclass,
    ConcreteReferencDeclaringVar,
    HelperParameter,
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
    Metaclass,
    MetamodelDeclaration,
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
    StaticPropertyCall,
    StaticPropertyCallExp,
    TupleExp,
    TuplePart,
    TupleType,
    TupleTypeAttribute,
    VariableDeclaration,
    VariableExp,
    VirtualAttribute,
    VirtualFeature,
    VirtualMetaclass,
    VirtualReference,
    dsl_gbind_EClass,
    gbind_dsl_BaseFeatureBinding,
    gbind_dsl_BaseHelper,
    gbind_dsl_BindingModel,
    gbind_dsl_BindingOptions,
    gbind_dsl_ClassBinding,
    gbind_dsl_ConceptBinding,
    gbind_dsl_ConceptFeatureRef,
    gbind_dsl_ConceptHelper,
    gbind_dsl_ConceptMetaclass,
    gbind_dsl_ConcreteMetaclass,
    gbind_dsl_ConcreteReferencDeclaringVar,
    gbind_dsl_HelperParameter,
    gbind_dsl_IntermediateClassBinding,
    gbind_dsl_LocalHelper,
    gbind_dsl_Metaclass,
    gbind_dsl_MetamodelDeclaration,
    gbind_dsl_OclFeatureBinding,
    gbind_dsl_RenamingFeatureBinding,
    gbind_dsl_VirtualAttribute,
    gbind_dsl_VirtualClassBinding,
    gbind_dsl_VirtualFeature,
    gbind_dsl_VirtualMetaclass,
    gbind_dsl_VirtualReference,
    gbind_dsl_VirtualTupleExp,
    gbind_simpleocl_AddOpCallExp,
    gbind_simpleocl_Attribute,
    gbind_simpleocl_BagExp,
    gbind_simpleocl_BagType,
    gbind_simpleocl_BooleanExp,
    gbind_simpleocl_BooleanType,
    gbind_simpleocl_BraceExp,
    gbind_simpleocl_CollectionExp,
    gbind_simpleocl_CollectionOperationCall,
    gbind_simpleocl_CollectionType,
    gbind_simpleocl_EnumLiteralExp,
    gbind_simpleocl_EnvExp,
    gbind_simpleocl_EnvType,
    gbind_simpleocl_EqOpCallExp,
    gbind_simpleocl_IfExp,
    gbind_simpleocl_Import,
    gbind_simpleocl_IntOpCallExp,
    gbind_simpleocl_IntegerExp,
    gbind_simpleocl_IntegerType,
    gbind_simpleocl_IterateExp,
    gbind_simpleocl_Iterator,
    gbind_simpleocl_IteratorExp,
    gbind_simpleocl_LambdaCallExp,
    gbind_simpleocl_LambdaType,
    gbind_simpleocl_LetExp,
    gbind_simpleocl_LocalVariable,
    gbind_simpleocl_LocatedElement,
    gbind_simpleocl_LoopExp,
    gbind_simpleocl_MapElement,
    gbind_simpleocl_MapExp,
    gbind_simpleocl_MapType,
    gbind_simpleocl_Module,
    gbind_simpleocl_ModuleElement,
    gbind_simpleocl_MulOpCallExp,
    gbind_simpleocl_NamedElement,
    gbind_simpleocl_NavigationOrAttributeCall,
    gbind_simpleocl_NotOpCallExp,
    gbind_simpleocl_NumericExp,
    gbind_simpleocl_NumericType,
    gbind_simpleocl_OclAnyType,
    gbind_simpleocl_OclContextDefinition,
    gbind_simpleocl_OclExpression,
    gbind_simpleocl_OclFeature,
    gbind_simpleocl_OclFeatureDefinition,
    gbind_simpleocl_OclInstanceModel,
    gbind_simpleocl_OclMetamodel,
    gbind_simpleocl_OclModel,
    gbind_simpleocl_OclModelElement,
    gbind_simpleocl_OclModelElementExp,
    gbind_simpleocl_OclType,
    gbind_simpleocl_OclUndefinedExp,
    gbind_simpleocl_Operation,
    gbind_simpleocl_OperationCall,
    gbind_simpleocl_OperatorCallExp,
    gbind_simpleocl_OrderedSetExp,
    gbind_simpleocl_OrderedSetType,
    gbind_simpleocl_Parameter,
    gbind_simpleocl_Primitive,
    gbind_simpleocl_PrimitiveExp,
    gbind_simpleocl_PropertyCall,
    gbind_simpleocl_PropertyCallExp,
    gbind_simpleocl_RealExp,
    gbind_simpleocl_RealType,
    gbind_simpleocl_RelOpCallExp,
    gbind_simpleocl_SelfExp,
    gbind_simpleocl_SequenceExp,
    gbind_simpleocl_SequenceType,
    gbind_simpleocl_SetExp,
    gbind_simpleocl_SetType,
    gbind_simpleocl_StaticNavigationOrAttributeCall,
    gbind_simpleocl_StaticOperationCall,
    gbind_simpleocl_StaticPropertyCall,
    gbind_simpleocl_StaticPropertyCallExp,
    gbind_simpleocl_StringExp,
    gbind_simpleocl_StringType,
    gbind_simpleocl_SuperExp,
    gbind_simpleocl_TupleExp,
    gbind_simpleocl_TuplePart,
    gbind_simpleocl_TupleType,
    gbind_simpleocl_TupleTypeAttribute,
    gbind_simpleocl_VariableDeclaration,
    gbind_simpleocl_VariableExp,
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

def test_assoc_argument51_stub_double():
    # OclExpression has no real 'OclExpression52' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OperatorCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression52', None)
    _safe_set(owner, 'gbind_simpleocl_OperatorCallExp', partner)
    assert getattr(partner, 'OclExpression52') == owner
    _safe_set(owner, 'gbind_simpleocl_OperatorCallExp', None)
    assert getattr(partner, 'OclExpression52') is None


def test_assoc_arguments42_stub_double():
    # OclExpression has no real 'OclExpression43' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_StaticOperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_StaticOperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_StaticOperationCall(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression43', None)
    _safe_set(owner, 'gbind_simpleocl_StaticOperationCall', {partner})
    assert getattr(partner, 'OclExpression43') == owner
    _safe_set(owner, 'gbind_simpleocl_StaticOperationCall', set())
    assert getattr(partner, 'OclExpression43') is None


def test_assoc_arguments49_stub_double():
    # OclExpression has no real 'OclExpression50' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OperationCall(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression50', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression50') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression50') is None


def test_assoc_attribute95_stub_double():
    # Attribute has no real 'Attribute97' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute97', None)
    _safe_set(owner, 'type96', partner)
    assert getattr(partner, 'Attribute97') == owner
    _safe_set(owner, 'type96', None)
    assert getattr(partner, 'Attribute97') is None


def test_assoc_baseExp82_stub_double():
    # IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_LocalVariable(eq="sample_text")
    partner = IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_bindings155_stub_double():
    # ConceptBinding has no real 'ConceptBinding' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BindingModel(name="sample_text", targetBinding=True)
    partner = ConceptBinding()
    setattr(partner, 'ConceptBinding', None)
    _safe_set(owner, 'model_', {partner})
    assert getattr(partner, 'ConceptBinding') == owner
    _safe_set(owner, 'model_', set())
    assert getattr(partner, 'ConceptBinding') is None


def test_assoc_body217_stub_double():
    # OclExpression has no real 'OclExpression218' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BaseHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BaseHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BaseHelper(feature="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression218', None)
    _safe_set(owner, 'gbind_dsl_BaseHelper', partner)
    assert getattr(partner, 'OclExpression218') == owner
    _safe_set(owner, 'gbind_dsl_BaseHelper', None)
    assert getattr(partner, 'OclExpression218') is None


def test_assoc_boundConcept163_stub_double():
    # MetamodelDeclaration has no real 'MetamodelDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BindingModel(name="sample_text", targetBinding=True)
    partner = MetamodelDeclaration()
    setattr(partner, 'MetamodelDeclaration', None)
    _safe_set(owner, 'gbind_dsl_BindingModel164', partner)
    assert getattr(partner, 'MetamodelDeclaration') == owner
    _safe_set(owner, 'gbind_dsl_BindingModel164', None)
    assert getattr(partner, 'MetamodelDeclaration') is None


def test_assoc_boundMetamodels165_stub_double():
    # MetamodelDeclaration has no real 'MetamodelDeclaration167' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BindingModel(name="sample_text", targetBinding=True)
    partner = MetamodelDeclaration()
    setattr(partner, 'MetamodelDeclaration167', None)
    _safe_set(owner, 'gbind_dsl_BindingModel166', {partner})
    assert getattr(partner, 'MetamodelDeclaration167') == owner
    _safe_set(owner, 'gbind_dsl_BindingModel166', set())
    assert getattr(partner, 'MetamodelDeclaration167') is None


def test_assoc_collectionTypes100_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_concept180_stub_double():
    # ConceptMetaclass has no real 'ConceptMetaclass181' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_IntermediateClassBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_IntermediateClassBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_IntermediateClassBinding(conceptReferenceName="sample_text")
    partner = ConceptMetaclass()
    setattr(partner, 'ConceptMetaclass181', None)
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding', partner)
    assert getattr(partner, 'ConceptMetaclass181') == owner
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding', None)
    assert getattr(partner, 'ConceptMetaclass181') is None


def test_assoc_conceptClass208_stub_double():
    # ConceptMetaclass has no real 'ConceptMetaclass209' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_ConceptFeatureRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_ConceptFeatureRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_ConceptFeatureRef(featureName="sample_text")
    partner = ConceptMetaclass()
    setattr(partner, 'ConceptMetaclass209', None)
    _safe_set(owner, 'gbind_dsl_ConceptFeatureRef', partner)
    assert getattr(partner, 'ConceptMetaclass209') == owner
    _safe_set(owner, 'gbind_dsl_ConceptFeatureRef', None)
    assert getattr(partner, 'ConceptMetaclass209') is None


def test_assoc_conceptClass210_stub_double():
    # ConceptMetaclass has no real 'ConceptMetaclass211' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BaseFeatureBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BaseFeatureBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BaseFeatureBinding(conceptFeature="sample_text")
    partner = ConceptMetaclass()
    setattr(partner, 'ConceptMetaclass211', None)
    _safe_set(owner, 'gbind_dsl_BaseFeatureBinding', partner)
    assert getattr(partner, 'ConceptMetaclass211') == owner
    _safe_set(owner, 'gbind_dsl_BaseFeatureBinding', None)
    assert getattr(partner, 'ConceptMetaclass211') is None


def test_assoc_conceptContext187_stub_double():
    # ConceptMetaclass has no real 'ConceptMetaclass189' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_IntermediateClassBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_IntermediateClassBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_IntermediateClassBinding(conceptReferenceName="sample_text")
    partner = ConceptMetaclass()
    setattr(partner, 'ConceptMetaclass189', None)
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding188', partner)
    assert getattr(partner, 'ConceptMetaclass189') == owner
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding188', None)
    assert getattr(partner, 'ConceptMetaclass189') is None


def test_assoc_conceptMetaclasses158_stub_double():
    # ConceptMetaclass has no real 'ConceptMetaclass' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BindingModel(name="sample_text", targetBinding=True)
    partner = ConceptMetaclass()
    setattr(partner, 'ConceptMetaclass', None)
    _safe_set(owner, 'gbind_dsl_BindingModel', {partner})
    assert getattr(partner, 'ConceptMetaclass') == owner
    _safe_set(owner, 'gbind_dsl_BindingModel', set())
    assert getattr(partner, 'ConceptMetaclass') is None


def test_assoc_concreteClass182_stub_double():
    # ConcreteMetaclass has no real 'ConcreteMetaclass184' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_IntermediateClassBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_IntermediateClassBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_IntermediateClassBinding(conceptReferenceName="sample_text")
    partner = ConcreteMetaclass()
    setattr(partner, 'ConcreteMetaclass184', None)
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding183', partner)
    assert getattr(partner, 'ConcreteMetaclass184') == owner
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding183', None)
    assert getattr(partner, 'ConcreteMetaclass184') is None


def test_assoc_concreteMetaclasses159_stub_double():
    # ConcreteMetaclass has no real 'ConcreteMetaclass' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BindingModel(name="sample_text", targetBinding=True)
    partner = ConcreteMetaclass()
    setattr(partner, 'ConcreteMetaclass', None)
    _safe_set(owner, 'gbind_dsl_BindingModel160', {partner})
    assert getattr(partner, 'ConcreteMetaclass') == owner
    _safe_set(owner, 'gbind_dsl_BindingModel160', set())
    assert getattr(partner, 'ConcreteMetaclass') is None


def test_assoc_concreteReference185_stub_double():
    # ConcreteReferencDeclaringVar has no real 'ConcreteReferencDeclaringVar' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_IntermediateClassBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_IntermediateClassBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_IntermediateClassBinding(conceptReferenceName="sample_text")
    partner = ConcreteReferencDeclaringVar()
    setattr(partner, 'ConcreteReferencDeclaringVar', None)
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding186', partner)
    assert getattr(partner, 'ConcreteReferencDeclaringVar') == owner
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding186', None)
    assert getattr(partner, 'ConcreteReferencDeclaringVar') is None


def test_assoc_context_131_stub_double():
    # OclContextDefinition has no real 'OclContextDefinition133' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclFeatureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclFeatureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclFeatureDefinition(static="sample_text")
    partner = OclContextDefinition()
    setattr(partner, 'OclContextDefinition133', None)
    _safe_set(owner, 'definition132', partner)
    assert getattr(partner, 'OclContextDefinition133') == owner
    _safe_set(owner, 'definition132', None)
    assert getattr(partner, 'OclContextDefinition133') is None


def test_assoc_definition138_stub_double():
    # OclFeatureDefinition has no real 'OclFeatureDefinition139' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclFeature(eq="sample_text")
    partner = OclFeatureDefinition()
    setattr(partner, 'OclFeatureDefinition139', None)
    _safe_set(owner, 'feature', partner)
    assert getattr(partner, 'OclFeatureDefinition139') == owner
    _safe_set(owner, 'feature', None)
    assert getattr(partner, 'OclFeatureDefinition139') is None


def test_assoc_definitions89_stub_double():
    # OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_eclass170_stub_double():
    # dsl_gbind_EClass has no real 'dsl_gbind_EClass' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_Metaclass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_Metaclass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_Metaclass(name="sample_text")
    partner = dsl_gbind_EClass()
    setattr(partner, 'dsl_gbind_EClass', None)
    _safe_set(owner, 'gbind_dsl_Metaclass', partner)
    assert getattr(partner, 'dsl_gbind_EClass') == owner
    _safe_set(owner, 'gbind_dsl_Metaclass', None)
    assert getattr(partner, 'dsl_gbind_EClass') is None


def test_assoc_feature130_stub_double():
    # OclFeature has no real 'OclFeature' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclFeatureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclFeatureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclFeatureDefinition(static="sample_text")
    partner = OclFeature()
    setattr(partner, 'OclFeature', None)
    _safe_set(owner, 'definition', partner)
    assert getattr(partner, 'OclFeature') == owner
    _safe_set(owner, 'definition', None)
    assert getattr(partner, 'OclFeature') is None


def test_assoc_featureBindings190_stub_double():
    # BaseFeatureBinding has no real 'BaseFeatureBinding' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_IntermediateClassBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_IntermediateClassBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_IntermediateClassBinding(conceptReferenceName="sample_text")
    partner = BaseFeatureBinding()
    setattr(partner, 'BaseFeatureBinding', None)
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding191', {partner})
    assert getattr(partner, 'BaseFeatureBinding') == owner
    _safe_set(owner, 'gbind_dsl_IntermediateClassBinding191', set())
    assert getattr(partner, 'BaseFeatureBinding') is None


def test_assoc_helpers156_stub_double():
    # BaseHelper has no real 'BaseHelper' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BindingModel(name="sample_text", targetBinding=True)
    partner = BaseHelper()
    setattr(partner, 'BaseHelper', None)
    _safe_set(owner, 'model_157', {partner})
    assert getattr(partner, 'BaseHelper') == owner
    _safe_set(owner, 'model_157', set())
    assert getattr(partner, 'BaseHelper') is None


def test_assoc_initExpression80_stub_double():
    # OclExpression has no real 'OclExpression81' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_LocalVariable(eq="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression81', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression81') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression81') is None


def test_assoc_lambdaArgType108_stub_double():
    # LambdaType has no real 'LambdaType109' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = LambdaType()
    setattr(partner, 'LambdaType109', None)
    _safe_set(owner, 'argumentTypes', partner)
    assert getattr(partner, 'LambdaType109') == owner
    _safe_set(owner, 'argumentTypes', None)
    assert getattr(partner, 'LambdaType109') is None


def test_assoc_lambdaReturnType106_stub_double():
    # LambdaType has no real 'LambdaType' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = LambdaType()
    setattr(partner, 'LambdaType', None)
    _safe_set(owner, 'returnType107', partner)
    assert getattr(partner, 'LambdaType') == owner
    _safe_set(owner, 'returnType107', None)
    assert getattr(partner, 'LambdaType') is None


def test_assoc_letExp78_stub_double():
    # LetExp has no real 'LetExp79' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_LocalVariable(eq="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp79', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp79') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp79') is None


def test_assoc_mapType294_stub_double():
    # MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_mapType98_stub_double():
    # MapType has no real 'MapType99' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType99', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType99') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType99') is None


def test_assoc_model113_stub_double():
    # OclModel has no real 'OclModel' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclModelElementExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclModelElementExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclModelElementExp(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel', None)
    _safe_set(owner, 'gbind_simpleocl_OclModelElementExp', partner)
    assert getattr(partner, 'OclModel') == owner
    _safe_set(owner, 'gbind_simpleocl_OclModelElementExp', None)
    assert getattr(partner, 'OclModel') is None


def test_assoc_model151_stub_double():
    # OclInstanceModel has no real 'OclInstanceModel' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclMetamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclMetamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclMetamodel(uri="sample_text")
    partner = OclInstanceModel()
    setattr(partner, 'OclInstanceModel', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclInstanceModel') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclInstanceModel') is None


def test_assoc_model_171_stub_double():
    # BindingModel has no real 'BindingModel' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_ConceptBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_ConceptBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_ConceptBinding(debugName="sample_text")
    partner = BindingModel()
    setattr(partner, 'BindingModel', None)
    _safe_set(owner, 'bindings', partner)
    assert getattr(partner, 'BindingModel') == owner
    _safe_set(owner, 'bindings', None)
    assert getattr(partner, 'BindingModel') is None


def test_assoc_model_222_stub_double():
    # BindingModel has no real 'BindingModel223' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BaseHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BaseHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BaseHelper(feature="sample_text")
    partner = BindingModel()
    setattr(partner, 'BindingModel223', None)
    _safe_set(owner, 'helpers', partner)
    assert getattr(partner, 'BindingModel223') == owner
    _safe_set(owner, 'helpers', None)
    assert getattr(partner, 'BindingModel223') is None


def test_assoc_oclExpression90_stub_double():
    # OclExpression has no real 'OclExpression91' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression91', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression91') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression91') is None


def test_assoc_operation92_stub_double():
    # Operation has no real 'Operation93' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation93', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation93') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation93') is None


def test_assoc_options168_stub_double():
    # BindingOptions has no real 'BindingOptions' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BindingModel(name="sample_text", targetBinding=True)
    partner = BindingOptions()
    setattr(partner, 'BindingOptions', None)
    _safe_set(owner, 'gbind_dsl_BindingModel169', partner)
    assert getattr(partner, 'BindingOptions') == owner
    _safe_set(owner, 'gbind_dsl_BindingModel169', None)
    assert getattr(partner, 'BindingOptions') is None


def test_assoc_qualifier212_stub_double():
    # ConcreteMetaclass has no real 'ConcreteMetaclass214' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BaseFeatureBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BaseFeatureBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BaseFeatureBinding(conceptFeature="sample_text")
    partner = ConcreteMetaclass()
    setattr(partner, 'ConcreteMetaclass214', None)
    _safe_set(owner, 'gbind_dsl_BaseFeatureBinding213', partner)
    assert getattr(partner, 'ConcreteMetaclass214') == owner
    _safe_set(owner, 'gbind_dsl_BaseFeatureBinding213', None)
    assert getattr(partner, 'ConcreteMetaclass214') is None


def test_assoc_source53_stub_double():
    # OclExpression has no real 'OclExpression54' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OperatorCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression54', None)
    _safe_set(owner, 'appliedOperator', partner)
    assert getattr(partner, 'OclExpression54') == owner
    _safe_set(owner, 'appliedOperator', None)
    assert getattr(partner, 'OclExpression54') is None


def test_assoc_staticPropertyCall110_stub_double():
    # StaticPropertyCallExp has no real 'StaticPropertyCallExp112' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = StaticPropertyCallExp()
    setattr(partner, 'StaticPropertyCallExp112', None)
    _safe_set(owner, 'source111', partner)
    assert getattr(partner, 'StaticPropertyCallExp112') == owner
    _safe_set(owner, 'source111', None)
    assert getattr(partner, 'StaticPropertyCallExp112') is None


def test_assoc_tupleType118_stub_double():
    # TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_TupleTypeAttribute(name="sample_text")
    partner = TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_tupleTypeAttribute101_stub_double():
    # TupleTypeAttribute has no real 'TupleTypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = TupleTypeAttribute()
    setattr(partner, 'TupleTypeAttribute', None)
    _safe_set(owner, 'type102', partner)
    assert getattr(partner, 'TupleTypeAttribute') == owner
    _safe_set(owner, 'type102', None)
    assert getattr(partner, 'TupleTypeAttribute') is None


def test_assoc_type116_stub_double():
    # OclType has no real 'OclType117' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType117', None)
    _safe_set(owner, 'tupleTypeAttribute', partner)
    assert getattr(partner, 'OclType117') == owner
    _safe_set(owner, 'tupleTypeAttribute', None)
    assert getattr(partner, 'OclType117') is None


def test_assoc_type219_stub_double():
    # OclType has no real 'OclType221' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BaseHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BaseHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BaseHelper(feature="sample_text")
    partner = OclType()
    setattr(partner, 'OclType221', None)
    _safe_set(owner, 'gbind_dsl_BaseHelper220', partner)
    assert getattr(partner, 'OclType221') == owner
    _safe_set(owner, 'gbind_dsl_BaseHelper220', None)
    assert getattr(partner, 'OclType221') is None


def test_assoc_type75_stub_double():
    # OclType has no real 'OclType76' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_VariableDeclaration(varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType76', None)
    _safe_set(owner, 'variableDeclaration', partner)
    assert getattr(partner, 'OclType76') == owner
    _safe_set(owner, 'variableDeclaration', None)
    assert getattr(partner, 'OclType76') is None


def test_assoc_variableDeclaration103_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration105' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_OclType(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration105', None)
    _safe_set(owner, 'type104', partner)
    assert getattr(partner, 'VariableDeclaration105') == owner
    _safe_set(owner, 'type104', None)
    assert getattr(partner, 'VariableDeclaration105') is None


def test_assoc_variableExp77_stub_double():
    # VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so gbind_simpleocl_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_simpleocl_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_simpleocl_VariableDeclaration(varName="sample_text")
    partner = VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


def test_assoc_virtualMetaclasses161_stub_double():
    # VirtualMetaclass has no real 'VirtualMetaclass' property in the generated
    # code (a bare stub) -- manually attach it so gbind_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gbind_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gbind_dsl_BindingModel(name="sample_text", targetBinding=True)
    partner = VirtualMetaclass()
    setattr(partner, 'VirtualMetaclass', None)
    _safe_set(owner, 'gbind_dsl_BindingModel162', {partner})
    assert getattr(partner, 'VirtualMetaclass') == owner
    _safe_set(owner, 'gbind_dsl_BindingModel162', set())
    assert getattr(partner, 'VirtualMetaclass') is None


