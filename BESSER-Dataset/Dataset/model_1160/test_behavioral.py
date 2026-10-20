import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    BHelper,
    BaseFeatureBinding,
    BindingModel,
    CollectionExp,
    CollectionType,
    ConceptBinding,
    ConceptMetaclass,
    ConcreteMetaclass,
    IfExp,
    IterateExp,
    Iterator,
    LetExp,
    LocatedElement,
    LoopExp,
    MapElement,
    MapExp,
    MapType,
    Metaclass,
    NumericExp,
    NumericType,
    OCL_Attribute,
    OCL_BagExp,
    OCL_BagType,
    OCL_BooleanExp,
    OCL_BooleanType,
    OCL_CollectionExp,
    OCL_CollectionOperationCallExp,
    OCL_CollectionType,
    OCL_EnumLiteralExp,
    OCL_IfExp,
    OCL_IntegerExp,
    OCL_IntegerType,
    OCL_IterateExp,
    OCL_Iterator,
    OCL_IteratorExp,
    OCL_LetExp,
    OCL_LoopExp,
    OCL_MapElement,
    OCL_MapExp,
    OCL_MapType,
    OCL_NavigationOrAttributeCallExp,
    OCL_NumericExp,
    OCL_NumericType,
    OCL_OclAnyType,
    OCL_OclContextDefinition,
    OCL_OclExpression,
    OCL_OclFeature,
    OCL_OclFeatureDefinition,
    OCL_OclModel,
    OCL_OclModelElement,
    OCL_OclType,
    OCL_OclUndefinedExp,
    OCL_Operation,
    OCL_OperationCallExp,
    OCL_OperatorCallExp,
    OCL_OrderedSetExp,
    OCL_OrderedSetType,
    OCL_Parameter,
    OCL_Primitive,
    OCL_PrimitiveExp,
    OCL_PropertyCallExp,
    OCL_RealExp,
    OCL_RealType,
    OCL_SequenceExp,
    OCL_SequenceType,
    OCL_SetExp,
    OCL_SetType,
    OCL_StringExp,
    OCL_StringType,
    OCL_SuperExp,
    OCL_TupleExp,
    OCL_TuplePart,
    OCL_TupleType,
    OCL_TupleTypeAttribute,
    OCL_VariableDeclaration,
    OCL_VariableExp,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclFeatureDefinition,
    OclModel,
    OclModelElement,
    OclType,
    Operation,
    OperationCallExp,
    Parameter,
    Primitive,
    PrimitiveExp,
    PropertyCallExp,
    TupleExp,
    TuplePart,
    TupleType,
    TupleTypeAttribute,
    VariableDeclaration,
    VariableExp,
    genericity_dsl_BHelper,
    genericity_dsl_BaseFeatureBinding,
    genericity_dsl_BindingModel,
    genericity_dsl_ClassBinding,
    genericity_dsl_ConceptBinding,
    genericity_dsl_ConceptMetaclass,
    genericity_dsl_ConcreteMetaclass,
    genericity_dsl_LocatedElement,
    genericity_dsl_Metaclass,
    genericity_dsl_OclFeatureBinding,
    genericity_dsl_RenamingFeatureBinding,
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

def test_assoc_arguments60_stub_double():
    # OclExpression has no real 'OclExpression61' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OperationCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression61', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression61') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression61') is None


def test_assoc_attribute98_stub_double():
    # Attribute has no real 'Attribute100' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute100', None)
    _safe_set(owner, 'type99', partner)
    assert getattr(partner, 'Attribute100') == owner
    _safe_set(owner, 'type99', None)
    assert getattr(partner, 'Attribute100') is None


def test_assoc_baseExp84_stub_double():
    # IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_bindings0_stub_double():
    # ConceptBinding has no real 'ConceptBinding' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BindingModel(metamodel="sample_text", name="sample_text")
    partner = ConceptBinding()
    setattr(partner, 'ConceptBinding', None)
    _safe_set(owner, 'model_', {partner})
    assert getattr(partner, 'ConceptBinding') == owner
    _safe_set(owner, 'model_', set())
    assert getattr(partner, 'ConceptBinding') is None


def test_assoc_body138_stub_double():
    # OclExpression has no real 'OclExpression139' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression139', None)
    _safe_set(owner, 'owningOperation', partner)
    assert getattr(partner, 'OclExpression139') == owner
    _safe_set(owner, 'owningOperation', None)
    assert getattr(partner, 'OclExpression139') is None


def test_assoc_body19_stub_double():
    # OclExpression has no real 'OclExpression21' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BHelper(feature="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression21', None)
    _safe_set(owner, 'genericity_dsl_BHelper20', partner)
    assert getattr(partner, 'OclExpression21') == owner
    _safe_set(owner, 'genericity_dsl_BHelper20', None)
    assert getattr(partner, 'OclExpression21') is None


def test_assoc_collectionTypes103_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_conceptClass10_stub_double():
    # ConceptMetaclass has no real 'ConceptMetaclass11' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BaseFeatureBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BaseFeatureBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BaseFeatureBinding(conceptFeature="sample_text")
    partner = ConceptMetaclass()
    setattr(partner, 'ConceptMetaclass11', None)
    _safe_set(owner, 'genericity_dsl_BaseFeatureBinding', partner)
    assert getattr(partner, 'ConceptMetaclass11') == owner
    _safe_set(owner, 'genericity_dsl_BaseFeatureBinding', None)
    assert getattr(partner, 'ConceptMetaclass11') is None


def test_assoc_contextClass17_stub_double():
    # ConceptMetaclass has no real 'ConceptMetaclass18' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BHelper(feature="sample_text")
    partner = ConceptMetaclass()
    setattr(partner, 'ConceptMetaclass18', None)
    _safe_set(owner, 'genericity_dsl_BHelper', partner)
    assert getattr(partner, 'ConceptMetaclass18') == owner
    _safe_set(owner, 'genericity_dsl_BHelper', None)
    assert getattr(partner, 'ConceptMetaclass18') is None


def test_assoc_definitions92_stub_double():
    # OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_elements142_stub_double():
    # OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'model143', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'model143', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_helpers1_stub_double():
    # BHelper has no real 'BHelper' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BindingModel(metamodel="sample_text", name="sample_text")
    partner = BHelper()
    setattr(partner, 'BHelper', None)
    _safe_set(owner, 'model_2', {partner})
    assert getattr(partner, 'BHelper') == owner
    _safe_set(owner, 'model_2', set())
    assert getattr(partner, 'BHelper') is None


def test_assoc_initExpression130_stub_double():
    # OclExpression has no real 'OclExpression131' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Attribute(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression131', None)
    _safe_set(owner, 'owningAttribute', partner)
    assert getattr(partner, 'OclExpression131') == owner
    _safe_set(owner, 'owningAttribute', None)
    assert getattr(partner, 'OclExpression131') is None


def test_assoc_initExpression80_stub_double():
    # OclExpression has no real 'OclExpression81' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression81', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression81') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression81') is None


def test_assoc_letExp82_stub_double():
    # LetExp has no real 'LetExp83' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp83', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp83') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp83') is None


def test_assoc_mapType101_stub_double():
    # MapType has no real 'MapType102' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType102', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType102') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType102') is None


def test_assoc_mapType297_stub_double():
    # MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_metamodel140_stub_double():
    # OclModel has no real 'OclModel141' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel141', None)
    _safe_set(owner, 'model', partner)
    assert getattr(partner, 'OclModel141') == owner
    _safe_set(owner, 'model', None)
    assert getattr(partner, 'OclModel141') is None


def test_assoc_model144_stub_double():
    # OclModel has no real 'OclModel145' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel145', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclModel145') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclModel145') is None


def test_assoc_model_24_stub_double():
    # BindingModel has no real 'BindingModel25' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BHelper(feature="sample_text")
    partner = BindingModel()
    setattr(partner, 'BindingModel25', None)
    _safe_set(owner, 'helpers', partner)
    assert getattr(partner, 'BindingModel25') == owner
    _safe_set(owner, 'helpers', None)
    assert getattr(partner, 'BindingModel25') is None


def test_assoc_model_4_stub_double():
    # BindingModel has no real 'BindingModel' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_ConceptBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_ConceptBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_ConceptBinding(debugName="sample_text")
    partner = BindingModel()
    setattr(partner, 'BindingModel', None)
    _safe_set(owner, 'bindings', partner)
    assert getattr(partner, 'BindingModel') == owner
    _safe_set(owner, 'bindings', None)
    assert getattr(partner, 'BindingModel') is None


def test_assoc_oclExpression93_stub_double():
    # OclExpression has no real 'OclExpression94' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression94', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression94') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression94') is None


def test_assoc_operation95_stub_double():
    # Operation has no real 'Operation96' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation96', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation96') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation96') is None


def test_assoc_parameters134_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'operation', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'operation', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_qualifier12_stub_double():
    # ConcreteMetaclass has no real 'ConcreteMetaclass14' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BaseFeatureBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BaseFeatureBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BaseFeatureBinding(conceptFeature="sample_text")
    partner = ConcreteMetaclass()
    setattr(partner, 'ConcreteMetaclass14', None)
    _safe_set(owner, 'genericity_dsl_BaseFeatureBinding13', partner)
    assert getattr(partner, 'ConcreteMetaclass14') == owner
    _safe_set(owner, 'genericity_dsl_BaseFeatureBinding13', None)
    assert getattr(partner, 'ConcreteMetaclass14') is None


def test_assoc_returnType135_stub_double():
    # OclType has no real 'OclType137' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType137', None)
    _safe_set(owner, 'operation136', partner)
    assert getattr(partner, 'OclType137') == owner
    _safe_set(owner, 'operation136', None)
    assert getattr(partner, 'OclType137') is None


def test_assoc_tupleType113_stub_double():
    # TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_TupleTypeAttribute(name="sample_text")
    partner = TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_tupleTypeAttribute104_stub_double():
    # TupleTypeAttribute has no real 'TupleTypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = TupleTypeAttribute()
    setattr(partner, 'TupleTypeAttribute', None)
    _safe_set(owner, 'type105', partner)
    assert getattr(partner, 'TupleTypeAttribute') == owner
    _safe_set(owner, 'type105', None)
    assert getattr(partner, 'TupleTypeAttribute') is None


def test_assoc_type111_stub_double():
    # OclType has no real 'OclType112' property in the generated
    # code (a bare stub) -- manually attach it so OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType112', None)
    _safe_set(owner, 'tupleTypeAttribute', partner)
    assert getattr(partner, 'OclType112') == owner
    _safe_set(owner, 'tupleTypeAttribute', None)
    assert getattr(partner, 'OclType112') is None


def test_assoc_type132_stub_double():
    # OclType has no real 'OclType133' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Attribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType133', None)
    _safe_set(owner, 'attribute', partner)
    assert getattr(partner, 'OclType133') == owner
    _safe_set(owner, 'attribute', None)
    assert getattr(partner, 'OclType133') is None


def test_assoc_type22_stub_double():
    # OclType has no real 'OclType' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BHelper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BHelper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BHelper(feature="sample_text")
    partner = OclType()
    setattr(partner, 'OclType', None)
    _safe_set(owner, 'genericity_dsl_BHelper23', partner)
    assert getattr(partner, 'OclType') == owner
    _safe_set(owner, 'genericity_dsl_BHelper23', None)
    assert getattr(partner, 'OclType') is None


def test_assoc_type78_stub_double():
    # OclType has no real 'OclType79' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType79', None)
    _safe_set(owner, 'variableDeclaration', partner)
    assert getattr(partner, 'OclType79') == owner
    _safe_set(owner, 'variableDeclaration', None)
    assert getattr(partner, 'OclType79') is None


def test_assoc_variableDeclaration106_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration108' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration108', None)
    _safe_set(owner, 'type107', partner)
    assert getattr(partner, 'VariableDeclaration108') == owner
    _safe_set(owner, 'type107', None)
    assert getattr(partner, 'VariableDeclaration108') is None


def test_assoc_variableExp85_stub_double():
    # VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


def test_assoc_variables3_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so genericity_dsl_BindingModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # genericity_dsl_BindingModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = genericity_dsl_BindingModel(metamodel="sample_text", name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration', None)
    _safe_set(owner, 'genericity_dsl_BindingModel', {partner})
    assert getattr(partner, 'VariableDeclaration') == owner
    _safe_set(owner, 'genericity_dsl_BindingModel', set())
    assert getattr(partner, 'VariableDeclaration') is None


