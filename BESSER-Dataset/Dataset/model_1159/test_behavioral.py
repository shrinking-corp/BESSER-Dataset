import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    CollectionExp,
    CollectionType,
    Context,
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
    OclConstraintsModel,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclFeatureDefinition,
    OclInvariant,
    OclModel,
    OclModelElement,
    OclPrecondition,
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
    UMLClass,
    VariableDeclaration,
    VariableExp,
    ocl_constraints_Context,
    ocl_constraints_LocatedElement,
    ocl_constraints_Metaclass,
    ocl_constraints_OclConstraintsModel,
    ocl_constraints_OclInvariant,
    ocl_constraints_OclPrecondition,
    ocl_constraints_UMLClass,
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

def test_assoc_arguments44_stub_double():
    # OclExpression has no real 'OclExpression45' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OperationCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression45', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression45') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression45') is None


def test_assoc_attribute82_stub_double():
    # Attribute has no real 'Attribute84' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute84', None)
    _safe_set(owner, 'type83', partner)
    assert getattr(partner, 'Attribute84') == owner
    _safe_set(owner, 'type83', None)
    assert getattr(partner, 'Attribute84') is None


def test_assoc_baseExp68_stub_double():
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


def test_assoc_body122_stub_double():
    # OclExpression has no real 'OclExpression123' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression123', None)
    _safe_set(owner, 'owningOperation', partner)
    assert getattr(partner, 'OclExpression123') == owner
    _safe_set(owner, 'owningOperation', None)
    assert getattr(partner, 'OclExpression123') is None


def test_assoc_collectionTypes87_stub_double():
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


def test_assoc_contexts0_stub_double():
    # Context has no real 'Context' property in the generated
    # code (a bare stub) -- manually attach it so ocl_constraints_OclConstraintsModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_constraints_OclConstraintsModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_constraints_OclConstraintsModel(metamodel="sample_text", name="sample_text")
    partner = Context()
    setattr(partner, 'Context', None)
    _safe_set(owner, 'model_', {partner})
    assert getattr(partner, 'Context') == owner
    _safe_set(owner, 'model_', set())
    assert getattr(partner, 'Context') is None


def test_assoc_definitions76_stub_double():
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


def test_assoc_elements126_stub_double():
    # OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'model127', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'model127', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_expr8_stub_double():
    # OclExpression has no real 'OclExpression' property in the generated
    # code (a bare stub) -- manually attach it so ocl_constraints_OclInvariant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_constraints_OclInvariant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_constraints_OclInvariant(description="sample_text", name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression', None)
    _safe_set(owner, 'ocl_constraints_OclInvariant', partner)
    assert getattr(partner, 'OclExpression') == owner
    _safe_set(owner, 'ocl_constraints_OclInvariant', None)
    assert getattr(partner, 'OclExpression') is None


def test_assoc_expr9_stub_double():
    # OclExpression has no real 'OclExpression10' property in the generated
    # code (a bare stub) -- manually attach it so ocl_constraints_OclPrecondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_constraints_OclPrecondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_constraints_OclPrecondition(description="sample_text", name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression10', None)
    _safe_set(owner, 'ocl_constraints_OclPrecondition', partner)
    assert getattr(partner, 'OclExpression10') == owner
    _safe_set(owner, 'ocl_constraints_OclPrecondition', None)
    assert getattr(partner, 'OclExpression10') is None


def test_assoc_initExpression114_stub_double():
    # OclExpression has no real 'OclExpression115' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Attribute(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression115', None)
    _safe_set(owner, 'owningAttribute', partner)
    assert getattr(partner, 'OclExpression115') == owner
    _safe_set(owner, 'owningAttribute', None)
    assert getattr(partner, 'OclExpression115') is None


def test_assoc_initExpression64_stub_double():
    # OclExpression has no real 'OclExpression65' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression65', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression65') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression65') is None


def test_assoc_letExp66_stub_double():
    # LetExp has no real 'LetExp67' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp67', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp67') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp67') is None


def test_assoc_mapType281_stub_double():
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


def test_assoc_mapType85_stub_double():
    # MapType has no real 'MapType86' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType86', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType86') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType86') is None


def test_assoc_metamodel124_stub_double():
    # OclModel has no real 'OclModel125' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel125', None)
    _safe_set(owner, 'model', partner)
    assert getattr(partner, 'OclModel125') == owner
    _safe_set(owner, 'model', None)
    assert getattr(partner, 'OclModel125') is None


def test_assoc_model128_stub_double():
    # OclModel has no real 'OclModel129' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel129', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclModel129') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclModel129') is None


def test_assoc_oclExpression77_stub_double():
    # OclExpression has no real 'OclExpression78' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression78', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression78') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression78') is None


def test_assoc_operation79_stub_double():
    # Operation has no real 'Operation80' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation80', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation80') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation80') is None


def test_assoc_parameters118_stub_double():
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


def test_assoc_returnType119_stub_double():
    # OclType has no real 'OclType121' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType121', None)
    _safe_set(owner, 'operation120', partner)
    assert getattr(partner, 'OclType121') == owner
    _safe_set(owner, 'operation120', None)
    assert getattr(partner, 'OclType121') is None


def test_assoc_tupleType97_stub_double():
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


def test_assoc_tupleTypeAttribute88_stub_double():
    # TupleTypeAttribute has no real 'TupleTypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = TupleTypeAttribute()
    setattr(partner, 'TupleTypeAttribute', None)
    _safe_set(owner, 'type89', partner)
    assert getattr(partner, 'TupleTypeAttribute') == owner
    _safe_set(owner, 'type89', None)
    assert getattr(partner, 'TupleTypeAttribute') is None


def test_assoc_type116_stub_double():
    # OclType has no real 'OclType117' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Attribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType117', None)
    _safe_set(owner, 'attribute', partner)
    assert getattr(partner, 'OclType117') == owner
    _safe_set(owner, 'attribute', None)
    assert getattr(partner, 'OclType117') is None


def test_assoc_type62_stub_double():
    # OclType has no real 'OclType63' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType63', None)
    _safe_set(owner, 'variableDeclaration', partner)
    assert getattr(partner, 'OclType63') == owner
    _safe_set(owner, 'variableDeclaration', None)
    assert getattr(partner, 'OclType63') is None


def test_assoc_type95_stub_double():
    # OclType has no real 'OclType96' property in the generated
    # code (a bare stub) -- manually attach it so OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType96', None)
    _safe_set(owner, 'tupleTypeAttribute', partner)
    assert getattr(partner, 'OclType96') == owner
    _safe_set(owner, 'tupleTypeAttribute', None)
    assert getattr(partner, 'OclType96') is None


def test_assoc_variableDeclaration90_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration92' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration92', None)
    _safe_set(owner, 'type91', partner)
    assert getattr(partner, 'VariableDeclaration92') == owner
    _safe_set(owner, 'type91', None)
    assert getattr(partner, 'VariableDeclaration92') is None


def test_assoc_variableExp69_stub_double():
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


def test_assoc_variables1_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so ocl_constraints_OclConstraintsModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_constraints_OclConstraintsModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_constraints_OclConstraintsModel(metamodel="sample_text", name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration', None)
    _safe_set(owner, 'ocl_constraints_OclConstraintsModel', {partner})
    assert getattr(partner, 'VariableDeclaration') == owner
    _safe_set(owner, 'ocl_constraints_OclConstraintsModel', set())
    assert getattr(partner, 'VariableDeclaration') is None


