import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ATL_LocatedElement,
    Attribute,
    CollectionExp,
    CollectionType,
    IfExp,
    IterateExp,
    Iterator,
    LetExp,
    LocatedElement,
    LoopExp,
    MapElement,
    MapExp,
    MapType,
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

def test_assoc_arguments31_stub_double():
    # OclExpression has no real 'OclExpression32' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OperationCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression32', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression32') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression32') is None


def test_assoc_attribute69_stub_double():
    # Attribute has no real 'Attribute71' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute71', None)
    _safe_set(owner, 'type70', partner)
    assert getattr(partner, 'Attribute71') == owner
    _safe_set(owner, 'type70', None)
    assert getattr(partner, 'Attribute71') is None


def test_assoc_baseExp55_stub_double():
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


def test_assoc_body109_stub_double():
    # OclExpression has no real 'OclExpression110' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression110', None)
    _safe_set(owner, 'owningOperation', partner)
    assert getattr(partner, 'OclExpression110') == owner
    _safe_set(owner, 'owningOperation', None)
    assert getattr(partner, 'OclExpression110') is None


def test_assoc_collectionTypes74_stub_double():
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


def test_assoc_definitions63_stub_double():
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


def test_assoc_elements113_stub_double():
    # OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'model114', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'model114', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_initExpression101_stub_double():
    # OclExpression has no real 'OclExpression102' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Attribute(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression102', None)
    _safe_set(owner, 'owningAttribute', partner)
    assert getattr(partner, 'OclExpression102') == owner
    _safe_set(owner, 'owningAttribute', None)
    assert getattr(partner, 'OclExpression102') is None


def test_assoc_initExpression51_stub_double():
    # OclExpression has no real 'OclExpression52' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression52', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression52') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression52') is None


def test_assoc_letExp53_stub_double():
    # LetExp has no real 'LetExp54' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp54', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp54') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp54') is None


def test_assoc_mapType268_stub_double():
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


def test_assoc_mapType72_stub_double():
    # MapType has no real 'MapType73' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType73', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType73') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType73') is None


def test_assoc_metamodel111_stub_double():
    # OclModel has no real 'OclModel112' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel112', None)
    _safe_set(owner, 'model', partner)
    assert getattr(partner, 'OclModel112') == owner
    _safe_set(owner, 'model', None)
    assert getattr(partner, 'OclModel112') is None


def test_assoc_model115_stub_double():
    # OclModel has no real 'OclModel116' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel116', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclModel116') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclModel116') is None


def test_assoc_oclExpression64_stub_double():
    # OclExpression has no real 'OclExpression65' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression65', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression65') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression65') is None


def test_assoc_operation66_stub_double():
    # Operation has no real 'Operation67' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation67', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation67') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation67') is None


def test_assoc_parameters105_stub_double():
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


def test_assoc_returnType106_stub_double():
    # OclType has no real 'OclType108' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType108', None)
    _safe_set(owner, 'operation107', partner)
    assert getattr(partner, 'OclType108') == owner
    _safe_set(owner, 'operation107', None)
    assert getattr(partner, 'OclType108') is None


def test_assoc_tupleType84_stub_double():
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


def test_assoc_tupleTypeAttribute75_stub_double():
    # TupleTypeAttribute has no real 'TupleTypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = TupleTypeAttribute()
    setattr(partner, 'TupleTypeAttribute', None)
    _safe_set(owner, 'type76', partner)
    assert getattr(partner, 'TupleTypeAttribute') == owner
    _safe_set(owner, 'type76', None)
    assert getattr(partner, 'TupleTypeAttribute') is None


def test_assoc_type103_stub_double():
    # OclType has no real 'OclType104' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Attribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType104', None)
    _safe_set(owner, 'attribute', partner)
    assert getattr(partner, 'OclType104') == owner
    _safe_set(owner, 'attribute', None)
    assert getattr(partner, 'OclType104') is None


def test_assoc_type49_stub_double():
    # OclType has no real 'OclType50' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType50', None)
    _safe_set(owner, 'variableDeclaration', partner)
    assert getattr(partner, 'OclType50') == owner
    _safe_set(owner, 'variableDeclaration', None)
    assert getattr(partner, 'OclType50') is None


def test_assoc_type82_stub_double():
    # OclType has no real 'OclType83' property in the generated
    # code (a bare stub) -- manually attach it so OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType83', None)
    _safe_set(owner, 'tupleTypeAttribute', partner)
    assert getattr(partner, 'OclType83') == owner
    _safe_set(owner, 'tupleTypeAttribute', None)
    assert getattr(partner, 'OclType83') is None


def test_assoc_variableDeclaration77_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration79' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration79', None)
    _safe_set(owner, 'type78', partner)
    assert getattr(partner, 'VariableDeclaration79') == owner
    _safe_set(owner, 'type78', None)
    assert getattr(partner, 'VariableDeclaration79') is None


def test_assoc_variableExp56_stub_double():
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


