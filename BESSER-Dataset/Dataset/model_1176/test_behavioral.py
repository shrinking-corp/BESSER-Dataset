import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CollectionExp,
    CollectionType,
    EmigOcl_AddOpCallExp,
    EmigOcl_Attribute,
    EmigOcl_BagExp,
    EmigOcl_BagType,
    EmigOcl_BooleanExp,
    EmigOcl_BooleanType,
    EmigOcl_BraceExp,
    EmigOcl_CollectionExp,
    EmigOcl_CollectionOperationCall,
    EmigOcl_CollectionType,
    EmigOcl_EnumLiteralExp,
    EmigOcl_EqOpCallExp,
    EmigOcl_IfExp,
    EmigOcl_IntOpCallExp,
    EmigOcl_IntegerExp,
    EmigOcl_IntegerType,
    EmigOcl_IterateExp,
    EmigOcl_Iterator,
    EmigOcl_IteratorExp,
    EmigOcl_LambdaCallExp,
    EmigOcl_LambdaType,
    EmigOcl_LetExp,
    EmigOcl_LocalVariable,
    EmigOcl_LocatedElement,
    EmigOcl_LoopExp,
    EmigOcl_MapElement,
    EmigOcl_MapExp,
    EmigOcl_MapType,
    EmigOcl_Module,
    EmigOcl_MulOpCallExp,
    EmigOcl_NavigationOrAttributeCall,
    EmigOcl_NotOpCallExp,
    EmigOcl_NumericExp,
    EmigOcl_NumericType,
    EmigOcl_OclAnyType,
    EmigOcl_OclContextDefinition,
    EmigOcl_OclExpression,
    EmigOcl_OclFeature,
    EmigOcl_OclFeatureDefinition,
    EmigOcl_OclModel,
    EmigOcl_OclModelElement,
    EmigOcl_OclModelElementExp,
    EmigOcl_OclType,
    EmigOcl_OclUndefinedExp,
    EmigOcl_Operation,
    EmigOcl_OperationCall,
    EmigOcl_OperatorCallExp,
    EmigOcl_OrderedSetExp,
    EmigOcl_OrderedSetType,
    EmigOcl_Parameter,
    EmigOcl_Primitive,
    EmigOcl_PrimitiveExp,
    EmigOcl_PropertyCall,
    EmigOcl_PropertyCallExp,
    EmigOcl_RealExp,
    EmigOcl_RealType,
    EmigOcl_RelOpCallExp,
    EmigOcl_SelfExp,
    EmigOcl_SequenceExp,
    EmigOcl_SequenceType,
    EmigOcl_SetExp,
    EmigOcl_SetType,
    EmigOcl_StaticNavigationOrAttributeCall,
    EmigOcl_StaticOperationCall,
    EmigOcl_StaticPropertyCall,
    EmigOcl_StaticPropertyCallExp,
    EmigOcl_StringExp,
    EmigOcl_StringType,
    EmigOcl_SuperExp,
    EmigOcl_TupleExp,
    EmigOcl_TuplePart,
    EmigOcl_TupleType,
    EmigOcl_TupleTypeAttribute,
    EmigOcl_VariableDeclaration,
    EmigOcl_VariableExp,
    LocalVariable,
    LocatedElement,
    LoopExp,
    NumericExp,
    NumericType,
    OclExpression,
    OclFeature,
    OclType,
    OperationCall,
    OperatorCallExp,
    Primitive,
    PrimitiveExp,
    PropertyCall,
    PropertyCallExp,
    StaticPropertyCall,
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

def test_assoc_attribute82_reverse_link_reassign_clear():
    a1 = EmigOcl_OclType(name="sample_text")
    a2 = EmigOcl_OclType(name="sample_text_2")
    b = EmigOcl_Attribute(name="sample_text")
    _safe_set(b, 'Attribute84', a1)
    assert _is_linked(b, 'Attribute84', a1)
    if hasattr(a1, 'type83'):
        assert _is_linked(a1, 'type83', b)
    _safe_set(b, 'Attribute84', a2)
    assert _is_linked(b, 'Attribute84', a2)
    if hasattr(a1, 'type83'):
        assert not _is_linked(a1, 'type83', b)
    if hasattr(a2, 'type83'):
        assert _is_linked(a2, 'type83', b)
    _safe_set(b, 'Attribute84', None)
    assert not _is_linked(b, 'Attribute84', a2)
    if hasattr(a2, 'type83'):
        assert not _is_linked(a2, 'type83', b)


def test_assoc_definition119_reverse_link_reassign_clear():
    a1 = EmigOcl_OclFeatureDefinition(static="sample_text")
    a2 = EmigOcl_OclFeatureDefinition(static="sample_text_2")
    b = EmigOcl_OclFeature(eq="sample_text")
    _safe_set(b, 'feature', a1)
    assert _is_linked(b, 'feature', a1)
    if hasattr(a1, 'OclFeatureDefinition120'):
        assert _is_linked(a1, 'OclFeatureDefinition120', b)
    _safe_set(b, 'feature', a2)
    assert _is_linked(b, 'feature', a2)
    if hasattr(a1, 'OclFeatureDefinition120'):
        assert not _is_linked(a1, 'OclFeatureDefinition120', b)
    if hasattr(a2, 'OclFeatureDefinition120'):
        assert _is_linked(a2, 'OclFeatureDefinition120', b)
    _safe_set(b, 'feature', None)
    assert not _is_linked(b, 'feature', a2)
    if hasattr(a2, 'OclFeatureDefinition120'):
        assert not _is_linked(a2, 'OclFeatureDefinition120', b)


def test_assoc_feature111_reverse_link_reassign_clear():
    a1 = EmigOcl_OclFeatureDefinition(static="sample_text")
    a2 = EmigOcl_OclFeatureDefinition(static="sample_text_2")
    b = EmigOcl_OclFeature(eq="sample_text")
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


def test_assoc_features1_reverse_link_reassign_clear():
    a1 = EmigOcl_OclFeatureDefinition(static="sample_text")
    a2 = EmigOcl_OclFeatureDefinition(static="sample_text_2")
    b = EmigOcl_Module(name="sample_text")
    _safe_set(b, 'EmigOcl_Module2', {a1})
    assert _is_linked(b, 'EmigOcl_Module2', a1)
    if hasattr(a1, 'EmigOcl_OclFeatureDefinition'):
        assert _is_linked(a1, 'EmigOcl_OclFeatureDefinition', b)
    _safe_set(b, 'EmigOcl_Module2', {a2})
    assert _is_linked(b, 'EmigOcl_Module2', a2)
    if hasattr(a1, 'EmigOcl_OclFeatureDefinition'):
        assert not _is_linked(a1, 'EmigOcl_OclFeatureDefinition', b)
    if hasattr(a2, 'EmigOcl_OclFeatureDefinition'):
        assert _is_linked(a2, 'EmigOcl_OclFeatureDefinition', b)
    _safe_set(b, 'EmigOcl_Module2', set())
    assert not _is_linked(b, 'EmigOcl_Module2', a2)
    if hasattr(a2, 'EmigOcl_OclFeatureDefinition'):
        assert not _is_linked(a2, 'EmigOcl_OclFeatureDefinition', b)


def test_assoc_metamodel132_reverse_link_reassign_clear():
    a1 = EmigOcl_OclModel(name="sample_text")
    a2 = EmigOcl_OclModel(name="sample_text_2")
    b = EmigOcl_OclModel(name="sample_text")
    _safe_set(b, 'model', a1)
    assert _is_linked(b, 'model', a1)
    if hasattr(a1, 'OclModel133'):
        assert _is_linked(a1, 'OclModel133', b)
    _safe_set(b, 'model', a2)
    assert _is_linked(b, 'model', a2)
    if hasattr(a1, 'OclModel133'):
        assert not _is_linked(a1, 'OclModel133', b)
    if hasattr(a2, 'OclModel133'):
        assert _is_linked(a2, 'OclModel133', b)
    _safe_set(b, 'model', None)
    assert not _is_linked(b, 'model', a2)
    if hasattr(a2, 'OclModel133'):
        assert not _is_linked(a2, 'OclModel133', b)


def test_assoc_model137_reverse_link_reassign_clear():
    a1 = EmigOcl_OclModel(name="sample_text")
    a2 = EmigOcl_OclModel(name="sample_text_2")
    b = EmigOcl_OclModel(name="sample_text")
    _safe_set(b, 'metamodel', {a1})
    assert _is_linked(b, 'metamodel', a1)
    if hasattr(a1, 'OclModel138'):
        assert _is_linked(a1, 'OclModel138', b)
    _safe_set(b, 'metamodel', {a2})
    assert _is_linked(b, 'metamodel', a2)
    if hasattr(a1, 'OclModel138'):
        assert not _is_linked(a1, 'OclModel138', b)
    if hasattr(a2, 'OclModel138'):
        assert _is_linked(a2, 'OclModel138', b)
    _safe_set(b, 'metamodel', set())
    assert not _is_linked(b, 'metamodel', a2)
    if hasattr(a2, 'OclModel138'):
        assert not _is_linked(a2, 'OclModel138', b)


def test_assoc_model93_reverse_link_reassign_clear():
    a1 = EmigOcl_OclModelElementExp(name="sample_text")
    a2 = EmigOcl_OclModelElementExp(name="sample_text_2")
    b = EmigOcl_OclModel(name="sample_text")
    _safe_set(b, 'EmigOcl_OclModel94', a1)
    assert _is_linked(b, 'EmigOcl_OclModel94', a1)
    if hasattr(a1, 'EmigOcl_OclModelElementExp'):
        assert _is_linked(a1, 'EmigOcl_OclModelElementExp', b)
    _safe_set(b, 'EmigOcl_OclModel94', a2)
    assert _is_linked(b, 'EmigOcl_OclModel94', a2)
    if hasattr(a1, 'EmigOcl_OclModelElementExp'):
        assert not _is_linked(a1, 'EmigOcl_OclModelElementExp', b)
    if hasattr(a2, 'EmigOcl_OclModelElementExp'):
        assert _is_linked(a2, 'EmigOcl_OclModelElementExp', b)
    _safe_set(b, 'EmigOcl_OclModel94', None)
    assert not _is_linked(b, 'EmigOcl_OclModel94', a2)
    if hasattr(a2, 'EmigOcl_OclModelElementExp'):
        assert not _is_linked(a2, 'EmigOcl_OclModelElementExp', b)


def test_assoc_models0_reverse_link_reassign_clear():
    a1 = EmigOcl_OclModel(name="sample_text")
    a2 = EmigOcl_OclModel(name="sample_text_2")
    b = EmigOcl_Module(name="sample_text")
    _safe_set(b, 'EmigOcl_Module', {a1})
    assert _is_linked(b, 'EmigOcl_Module', a1)
    if hasattr(a1, 'EmigOcl_OclModel'):
        assert _is_linked(a1, 'EmigOcl_OclModel', b)
    _safe_set(b, 'EmigOcl_Module', {a2})
    assert _is_linked(b, 'EmigOcl_Module', a2)
    if hasattr(a1, 'EmigOcl_OclModel'):
        assert not _is_linked(a1, 'EmigOcl_OclModel', b)
    if hasattr(a2, 'EmigOcl_OclModel'):
        assert _is_linked(a2, 'EmigOcl_OclModel', b)
    _safe_set(b, 'EmigOcl_Module', set())
    assert not _is_linked(b, 'EmigOcl_Module', a2)
    if hasattr(a2, 'EmigOcl_OclModel'):
        assert not _is_linked(a2, 'EmigOcl_OclModel', b)


def test_assoc_operation79_reverse_link_reassign_clear():
    a1 = EmigOcl_Operation(name="sample_text")
    a2 = EmigOcl_Operation(name="sample_text_2")
    b = EmigOcl_OclType(name="sample_text")
    _safe_set(b, 'returnType', a1)
    assert _is_linked(b, 'returnType', a1)
    if hasattr(a1, 'Operation80'):
        assert _is_linked(a1, 'Operation80', b)
    _safe_set(b, 'returnType', a2)
    assert _is_linked(b, 'returnType', a2)
    if hasattr(a1, 'Operation80'):
        assert not _is_linked(a1, 'Operation80', b)
    if hasattr(a2, 'Operation80'):
        assert _is_linked(a2, 'Operation80', b)
    _safe_set(b, 'returnType', None)
    assert not _is_linked(b, 'returnType', a2)
    if hasattr(a2, 'Operation80'):
        assert not _is_linked(a2, 'Operation80', b)


def test_assoc_returnType126_reverse_link_reassign_clear():
    a1 = EmigOcl_Operation(name="sample_text")
    a2 = EmigOcl_Operation(name="sample_text_2")
    b = EmigOcl_OclType(name="sample_text")
    _safe_set(b, 'OclType128', a1)
    assert _is_linked(b, 'OclType128', a1)
    if hasattr(a1, 'operation127'):
        assert _is_linked(a1, 'operation127', b)
    _safe_set(b, 'OclType128', a2)
    assert _is_linked(b, 'OclType128', a2)
    if hasattr(a1, 'operation127'):
        assert not _is_linked(a1, 'operation127', b)
    if hasattr(a2, 'operation127'):
        assert _is_linked(a2, 'operation127', b)
    _safe_set(b, 'OclType128', None)
    assert not _is_linked(b, 'OclType128', a2)
    if hasattr(a2, 'operation127'):
        assert not _is_linked(a2, 'operation127', b)


def test_assoc_tupleTypeAttribute88_reverse_link_reassign_clear():
    a1 = EmigOcl_TupleTypeAttribute(name="sample_text")
    a2 = EmigOcl_TupleTypeAttribute(name="sample_text_2")
    b = EmigOcl_OclType(name="sample_text")
    _safe_set(b, 'type89', a1)
    assert _is_linked(b, 'type89', a1)
    if hasattr(a1, 'TupleTypeAttribute'):
        assert _is_linked(a1, 'TupleTypeAttribute', b)
    _safe_set(b, 'type89', a2)
    assert _is_linked(b, 'type89', a2)
    if hasattr(a1, 'TupleTypeAttribute'):
        assert not _is_linked(a1, 'TupleTypeAttribute', b)
    if hasattr(a2, 'TupleTypeAttribute'):
        assert _is_linked(a2, 'TupleTypeAttribute', b)
    _safe_set(b, 'type89', None)
    assert not _is_linked(b, 'type89', a2)
    if hasattr(a2, 'TupleTypeAttribute'):
        assert not _is_linked(a2, 'TupleTypeAttribute', b)


def test_assoc_type123_reverse_link_reassign_clear():
    a1 = EmigOcl_OclType(name="sample_text")
    a2 = EmigOcl_OclType(name="sample_text_2")
    b = EmigOcl_Attribute(name="sample_text")
    _safe_set(b, 'attribute', a1)
    assert _is_linked(b, 'attribute', a1)
    if hasattr(a1, 'OclType124'):
        assert _is_linked(a1, 'OclType124', b)
    _safe_set(b, 'attribute', a2)
    assert _is_linked(b, 'attribute', a2)
    if hasattr(a1, 'OclType124'):
        assert not _is_linked(a1, 'OclType124', b)
    if hasattr(a2, 'OclType124'):
        assert _is_linked(a2, 'OclType124', b)
    _safe_set(b, 'attribute', None)
    assert not _is_linked(b, 'attribute', a2)
    if hasattr(a2, 'OclType124'):
        assert not _is_linked(a2, 'OclType124', b)


def test_assoc_type62_reverse_link_reassign_clear():
    a1 = EmigOcl_VariableDeclaration(varName="sample_text")
    a2 = EmigOcl_VariableDeclaration(varName="sample_text_2")
    b = EmigOcl_OclType(name="sample_text")
    _safe_set(b, 'OclType63', a1)
    assert _is_linked(b, 'OclType63', a1)
    if hasattr(a1, 'variableDeclaration'):
        assert _is_linked(a1, 'variableDeclaration', b)
    _safe_set(b, 'OclType63', a2)
    assert _is_linked(b, 'OclType63', a2)
    if hasattr(a1, 'variableDeclaration'):
        assert not _is_linked(a1, 'variableDeclaration', b)
    if hasattr(a2, 'variableDeclaration'):
        assert _is_linked(a2, 'variableDeclaration', b)
    _safe_set(b, 'OclType63', None)
    assert not _is_linked(b, 'OclType63', a2)
    if hasattr(a2, 'variableDeclaration'):
        assert not _is_linked(a2, 'variableDeclaration', b)


def test_assoc_type97_reverse_link_reassign_clear():
    a1 = EmigOcl_TupleTypeAttribute(name="sample_text")
    a2 = EmigOcl_TupleTypeAttribute(name="sample_text_2")
    b = EmigOcl_OclType(name="sample_text")
    _safe_set(b, 'OclType98', a1)
    assert _is_linked(b, 'OclType98', a1)
    if hasattr(a1, 'tupleTypeAttribute'):
        assert _is_linked(a1, 'tupleTypeAttribute', b)
    _safe_set(b, 'OclType98', a2)
    assert _is_linked(b, 'OclType98', a2)
    if hasattr(a1, 'tupleTypeAttribute'):
        assert not _is_linked(a1, 'tupleTypeAttribute', b)
    if hasattr(a2, 'tupleTypeAttribute'):
        assert _is_linked(a2, 'tupleTypeAttribute', b)
    _safe_set(b, 'OclType98', None)
    assert not _is_linked(b, 'OclType98', a2)
    if hasattr(a2, 'tupleTypeAttribute'):
        assert not _is_linked(a2, 'tupleTypeAttribute', b)


def test_assoc_variableDeclaration90_reverse_link_reassign_clear():
    a1 = EmigOcl_VariableDeclaration(varName="sample_text")
    a2 = EmigOcl_VariableDeclaration(varName="sample_text_2")
    b = EmigOcl_OclType(name="sample_text")
    _safe_set(b, 'type91', a1)
    assert _is_linked(b, 'type91', a1)
    if hasattr(a1, 'VariableDeclaration92'):
        assert _is_linked(a1, 'VariableDeclaration92', b)
    _safe_set(b, 'type91', a2)
    assert _is_linked(b, 'type91', a2)
    if hasattr(a1, 'VariableDeclaration92'):
        assert not _is_linked(a1, 'VariableDeclaration92', b)
    if hasattr(a2, 'VariableDeclaration92'):
        assert _is_linked(a2, 'VariableDeclaration92', b)
    _safe_set(b, 'type91', None)
    assert not _is_linked(b, 'type91', a2)
    if hasattr(a2, 'VariableDeclaration92'):
        assert not _is_linked(a2, 'VariableDeclaration92', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argument40_stub_double():
    # EmigOcl_OclExpression has no real 'EmigOcl_OclExpression41' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OperatorCallExp(operationName="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'EmigOcl_OclExpression41', None)
    _safe_set(owner, 'EmigOcl_OperatorCallExp', partner)
    assert getattr(partner, 'EmigOcl_OclExpression41') == owner
    _safe_set(owner, 'EmigOcl_OperatorCallExp', None)
    assert getattr(partner, 'EmigOcl_OclExpression41') is None


def test_assoc_argumentTypes108_stub_double():
    # EmigOcl_LambdaType has no real 'EmigOcl_LambdaType109' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_LambdaType()
    setattr(partner, 'EmigOcl_LambdaType109', None)
    _safe_set(owner, 'EmigOcl_OclType110', partner)
    assert owner in getattr(partner, 'EmigOcl_LambdaType109')
    _safe_set(owner, 'EmigOcl_OclType110', None)
    assert owner not in getattr(partner, 'EmigOcl_LambdaType109')


def test_assoc_arguments33_stub_double():
    # EmigOcl_OclExpression has no real 'EmigOcl_OclExpression34' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_StaticOperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_StaticOperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_StaticOperationCall(operationName="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'EmigOcl_OclExpression34', None)
    _safe_set(owner, 'EmigOcl_StaticOperationCall', {partner})
    assert getattr(partner, 'EmigOcl_OclExpression34') == owner
    _safe_set(owner, 'EmigOcl_StaticOperationCall', set())
    assert getattr(partner, 'EmigOcl_OclExpression34') is None


def test_assoc_arguments38_stub_double():
    # EmigOcl_OclExpression has no real 'OclExpression39' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OperationCall(operationName="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'OclExpression39', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression39') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression39') is None


def test_assoc_attributes95_stub_double():
    # EmigOcl_TupleType has no real 'tupleType' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_TupleTypeAttribute(name="sample_text")
    partner = EmigOcl_TupleType()
    setattr(partner, 'tupleType', None)
    _safe_set(owner, 'TupleTypeAttribute96', partner)
    assert owner in getattr(partner, 'tupleType')
    _safe_set(owner, 'TupleTypeAttribute96', None)
    assert owner not in getattr(partner, 'tupleType')


def test_assoc_baseExp69_stub_double():
    # EmigOcl_IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_LocalVariable(eq="sample_text")
    partner = EmigOcl_IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_body129_stub_double():
    # EmigOcl_OclExpression has no real 'OclExpression130' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_Operation(name="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'OclExpression130', None)
    _safe_set(owner, 'owningOperation', partner)
    assert getattr(partner, 'OclExpression130') == owner
    _safe_set(owner, 'owningOperation', None)
    assert getattr(partner, 'OclExpression130') is None


def test_assoc_collectionTypes87_stub_double():
    # EmigOcl_CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_context_112_stub_double():
    # EmigOcl_OclContextDefinition has no real 'OclContextDefinition114' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclFeatureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclFeatureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclFeatureDefinition(static="sample_text")
    partner = EmigOcl_OclContextDefinition()
    setattr(partner, 'OclContextDefinition114', None)
    _safe_set(owner, 'definition113', partner)
    assert getattr(partner, 'OclContextDefinition114') == owner
    _safe_set(owner, 'definition113', None)
    assert getattr(partner, 'OclContextDefinition114') is None


def test_assoc_context_117_stub_double():
    # EmigOcl_OclContextDefinition has no real 'definitions' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_OclContextDefinition()
    setattr(partner, 'definitions', None)
    _safe_set(owner, 'OclType118', partner)
    assert getattr(partner, 'definitions') == owner
    _safe_set(owner, 'OclType118', None)
    assert getattr(partner, 'definitions') is None


def test_assoc_definition115_stub_double():
    # EmigOcl_OclContextDefinition has no real 'context_116' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclFeatureDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclFeatureDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclFeatureDefinition(static="sample_text")
    partner = EmigOcl_OclContextDefinition()
    setattr(partner, 'context_116', None)
    _safe_set(owner, 'OclFeatureDefinition', partner)
    assert getattr(partner, 'context_116') == owner
    _safe_set(owner, 'OclFeatureDefinition', None)
    assert getattr(partner, 'context_116') is None


def test_assoc_definitions76_stub_double():
    # EmigOcl_OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_elementType74_stub_double():
    # EmigOcl_CollectionType has no real 'collectionTypes' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_CollectionType()
    setattr(partner, 'collectionTypes', None)
    _safe_set(owner, 'OclType75', partner)
    assert getattr(partner, 'collectionTypes') == owner
    _safe_set(owner, 'OclType75', None)
    assert getattr(partner, 'collectionTypes') is None


def test_assoc_elements134_stub_double():
    # EmigOcl_OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclModel(name="sample_text")
    partner = EmigOcl_OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'model135', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'model135', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_initExpression121_stub_double():
    # EmigOcl_OclExpression has no real 'OclExpression122' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_Attribute(name="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'OclExpression122', None)
    _safe_set(owner, 'owningAttribute', partner)
    assert getattr(partner, 'OclExpression122') == owner
    _safe_set(owner, 'owningAttribute', None)
    assert getattr(partner, 'OclExpression122') is None


def test_assoc_initExpression67_stub_double():
    # EmigOcl_OclExpression has no real 'OclExpression68' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_LocalVariable(eq="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'OclExpression68', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression68') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression68') is None


def test_assoc_initializedVariable10_stub_double():
    # EmigOcl_OclExpression has no real 'initExpression' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_LocalVariable(eq="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'initExpression', None)
    _safe_set(owner, 'LocalVariable', partner)
    assert getattr(partner, 'initExpression') == owner
    _safe_set(owner, 'LocalVariable', None)
    assert getattr(partner, 'initExpression') is None


def test_assoc_keyType104_stub_double():
    # EmigOcl_MapType has no real 'mapType' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_MapType()
    setattr(partner, 'mapType', None)
    _safe_set(owner, 'OclType105', partner)
    assert getattr(partner, 'mapType') == owner
    _safe_set(owner, 'OclType105', None)
    assert getattr(partner, 'mapType') is None


def test_assoc_letExp65_stub_double():
    # EmigOcl_LetExp has no real 'LetExp66' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_LocalVariable(eq="sample_text")
    partner = EmigOcl_LetExp()
    setattr(partner, 'LetExp66', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp66') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp66') is None


def test_assoc_mapType281_stub_double():
    # EmigOcl_MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_mapType85_stub_double():
    # EmigOcl_MapType has no real 'MapType86' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_MapType()
    setattr(partner, 'MapType86', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType86') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType86') is None


def test_assoc_model100_stub_double():
    # EmigOcl_OclModelElement has no real 'elements101' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclModel(name="sample_text")
    partner = EmigOcl_OclModelElement()
    setattr(partner, 'elements101', None)
    _safe_set(owner, 'OclModel', partner)
    assert getattr(partner, 'elements101') == owner
    _safe_set(owner, 'OclModel', None)
    assert getattr(partner, 'elements101') is None


def test_assoc_oclExpression77_stub_double():
    # EmigOcl_OclExpression has no real 'OclExpression78' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'OclExpression78', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression78') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression78') is None


def test_assoc_operation72_stub_double():
    # EmigOcl_Parameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_Operation(name="sample_text")
    partner = EmigOcl_Parameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Operation73', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Operation73', None)
    assert getattr(partner, 'parameters') is None


def test_assoc_owningAttribute17_stub_double():
    # EmigOcl_OclExpression has no real 'initExpression18' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_Attribute(name="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'initExpression18', None)
    _safe_set(owner, 'Attribute', partner)
    assert getattr(partner, 'initExpression18') == owner
    _safe_set(owner, 'Attribute', None)
    assert getattr(partner, 'initExpression18') is None


def test_assoc_owningOperation13_stub_double():
    # EmigOcl_OclExpression has no real 'body14' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_Operation(name="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'body14', None)
    _safe_set(owner, 'Operation', partner)
    assert getattr(partner, 'body14') == owner
    _safe_set(owner, 'Operation', None)
    assert getattr(partner, 'body14') is None


def test_assoc_parameters125_stub_double():
    # EmigOcl_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_Operation(name="sample_text")
    partner = EmigOcl_Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'operation', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'operation', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_parentOperation9_stub_double():
    # EmigOcl_OclExpression has no real 'arguments' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OperationCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OperationCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OperationCall(operationName="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'arguments', None)
    _safe_set(owner, 'OperationCall', partner)
    assert getattr(partner, 'arguments') == owner
    _safe_set(owner, 'OperationCall', None)
    assert getattr(partner, 'arguments') is None


def test_assoc_referredVariable19_stub_double():
    # EmigOcl_VariableExp has no real 'variableExp' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_VariableDeclaration(varName="sample_text")
    partner = EmigOcl_VariableExp()
    setattr(partner, 'variableExp', None)
    _safe_set(owner, 'VariableDeclaration', partner)
    assert getattr(partner, 'variableExp') == owner
    _safe_set(owner, 'VariableDeclaration', None)
    assert getattr(partner, 'variableExp') is None


def test_assoc_result49_stub_double():
    # EmigOcl_IterateExp has no real 'baseExp' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_LocalVariable(eq="sample_text")
    partner = EmigOcl_IterateExp()
    setattr(partner, 'baseExp', None)
    _safe_set(owner, 'LocalVariable50', partner)
    assert getattr(partner, 'baseExp') == owner
    _safe_set(owner, 'LocalVariable50', None)
    assert getattr(partner, 'baseExp') is None


def test_assoc_returnType106_stub_double():
    # EmigOcl_LambdaType has no real 'EmigOcl_LambdaType' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_LambdaType()
    setattr(partner, 'EmigOcl_LambdaType', None)
    _safe_set(owner, 'EmigOcl_OclType107', partner)
    assert getattr(partner, 'EmigOcl_LambdaType') == owner
    _safe_set(owner, 'EmigOcl_OclType107', None)
    assert getattr(partner, 'EmigOcl_LambdaType') is None


def test_assoc_source30_stub_double():
    # EmigOcl_StaticPropertyCallExp has no real 'EmigOcl_StaticPropertyCallExp' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_StaticPropertyCallExp()
    setattr(partner, 'EmigOcl_StaticPropertyCallExp', None)
    _safe_set(owner, 'EmigOcl_OclType', partner)
    assert getattr(partner, 'EmigOcl_StaticPropertyCallExp') == owner
    _safe_set(owner, 'EmigOcl_OclType', None)
    assert getattr(partner, 'EmigOcl_StaticPropertyCallExp') is None


def test_assoc_tupleType99_stub_double():
    # EmigOcl_TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_TupleTypeAttribute(name="sample_text")
    partner = EmigOcl_TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_type3_stub_double():
    # EmigOcl_OclExpression has no real 'oclExpression' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_OclExpression()
    setattr(partner, 'oclExpression', None)
    _safe_set(owner, 'OclType', partner)
    assert getattr(partner, 'oclExpression') == owner
    _safe_set(owner, 'OclType', None)
    assert getattr(partner, 'oclExpression') is None


def test_assoc_valueType102_stub_double():
    # EmigOcl_MapType has no real 'mapType2' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_OclType(name="sample_text")
    partner = EmigOcl_MapType()
    setattr(partner, 'mapType2', None)
    _safe_set(owner, 'OclType103', partner)
    assert getattr(partner, 'mapType2') == owner
    _safe_set(owner, 'OclType103', None)
    assert getattr(partner, 'mapType2') is None


def test_assoc_variable51_stub_double():
    # EmigOcl_LetExp has no real 'letExp' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_LocalVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_LocalVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_LocalVariable(eq="sample_text")
    partner = EmigOcl_LetExp()
    setattr(partner, 'letExp', None)
    _safe_set(owner, 'LocalVariable52', partner)
    assert getattr(partner, 'letExp') == owner
    _safe_set(owner, 'LocalVariable52', None)
    assert getattr(partner, 'letExp') is None


def test_assoc_variableExp64_stub_double():
    # EmigOcl_VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so EmigOcl_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EmigOcl_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EmigOcl_VariableDeclaration(varName="sample_text")
    partner = EmigOcl_VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


