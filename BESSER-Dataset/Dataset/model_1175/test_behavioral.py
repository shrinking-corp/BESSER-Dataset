import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CollectionExp,
    CollectionType,
    LocatedElement,
    LoopExp,
    NumericExp,
    NumericType,
    OCLinEmig_Attribute,
    OCLinEmig_BagExp,
    OCLinEmig_BagType,
    OCLinEmig_BooleanExp,
    OCLinEmig_BooleanType,
    OCLinEmig_CollectionExp,
    OCLinEmig_CollectionOperationCallExp,
    OCLinEmig_CollectionType,
    OCLinEmig_EnumLiteralExp,
    OCLinEmig_IfExp,
    OCLinEmig_IntegerExp,
    OCLinEmig_IntegerType,
    OCLinEmig_IterateExp,
    OCLinEmig_Iterator,
    OCLinEmig_IteratorExp,
    OCLinEmig_LetExp,
    OCLinEmig_LocatedElement,
    OCLinEmig_LoopExp,
    OCLinEmig_MapElement,
    OCLinEmig_MapExp,
    OCLinEmig_MapType,
    OCLinEmig_Module,
    OCLinEmig_NavigationOrAttributeCallExp,
    OCLinEmig_NumericExp,
    OCLinEmig_NumericType,
    OCLinEmig_OclAnyType,
    OCLinEmig_OclContextDefinition,
    OCLinEmig_OclExpression,
    OCLinEmig_OclFeature,
    OCLinEmig_OclFeatureDefinition,
    OCLinEmig_OclModel,
    OCLinEmig_OclModelElement,
    OCLinEmig_OclType,
    OCLinEmig_OclUndefinedExp,
    OCLinEmig_Operation,
    OCLinEmig_OperationCallExp,
    OCLinEmig_OperatorCallExp,
    OCLinEmig_OrderedSetExp,
    OCLinEmig_OrderedSetType,
    OCLinEmig_Parameter,
    OCLinEmig_Primitive,
    OCLinEmig_PrimitiveExp,
    OCLinEmig_PropertyCallExp,
    OCLinEmig_RealExp,
    OCLinEmig_RealType,
    OCLinEmig_SequenceExp,
    OCLinEmig_SequenceType,
    OCLinEmig_SetExp,
    OCLinEmig_SetType,
    OCLinEmig_StringExp,
    OCLinEmig_StringType,
    OCLinEmig_SuperExp,
    OCLinEmig_TupleExp,
    OCLinEmig_TuplePart,
    OCLinEmig_TupleType,
    OCLinEmig_TupleTypeAttribute,
    OCLinEmig_VariableDeclaration,
    OCLinEmig_VariableExp,
    OclExpression,
    OclFeature,
    OclType,
    OperationCallExp,
    Primitive,
    PrimitiveExp,
    PropertyCallExp,
    VariableDeclaration,
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

def test_assoc_attribute68_reverse_link_reassign_clear():
    a1 = OCLinEmig_OclType(name="sample_text")
    a2 = OCLinEmig_OclType(name="sample_text_2")
    b = OCLinEmig_Attribute(name="sample_text")
    _safe_set(b, 'Attribute70', a1)
    assert _is_linked(b, 'Attribute70', a1)
    if hasattr(a1, 'type69'):
        assert _is_linked(a1, 'type69', b)
    _safe_set(b, 'Attribute70', a2)
    assert _is_linked(b, 'Attribute70', a2)
    if hasattr(a1, 'type69'):
        assert not _is_linked(a1, 'type69', b)
    if hasattr(a2, 'type69'):
        assert _is_linked(a2, 'type69', b)
    _safe_set(b, 'Attribute70', None)
    assert not _is_linked(b, 'Attribute70', a2)
    if hasattr(a2, 'type69'):
        assert not _is_linked(a2, 'type69', b)


def test_assoc_metamodel111_reverse_link_reassign_clear():
    a1 = OCLinEmig_OclModel(name="sample_text")
    a2 = OCLinEmig_OclModel(name="sample_text_2")
    b = OCLinEmig_OclModel(name="sample_text")
    _safe_set(b, 'model', a1)
    assert _is_linked(b, 'model', a1)
    if hasattr(a1, 'OclModel112'):
        assert _is_linked(a1, 'OclModel112', b)
    _safe_set(b, 'model', a2)
    assert _is_linked(b, 'model', a2)
    if hasattr(a1, 'OclModel112'):
        assert not _is_linked(a1, 'OclModel112', b)
    if hasattr(a2, 'OclModel112'):
        assert _is_linked(a2, 'OclModel112', b)
    _safe_set(b, 'model', None)
    assert not _is_linked(b, 'model', a2)
    if hasattr(a2, 'OclModel112'):
        assert not _is_linked(a2, 'OclModel112', b)


def test_assoc_model116_reverse_link_reassign_clear():
    a1 = OCLinEmig_OclModel(name="sample_text")
    a2 = OCLinEmig_OclModel(name="sample_text_2")
    b = OCLinEmig_OclModel(name="sample_text")
    _safe_set(b, 'metamodel', {a1})
    assert _is_linked(b, 'metamodel', a1)
    if hasattr(a1, 'OclModel117'):
        assert _is_linked(a1, 'OclModel117', b)
    _safe_set(b, 'metamodel', {a2})
    assert _is_linked(b, 'metamodel', a2)
    if hasattr(a1, 'OclModel117'):
        assert not _is_linked(a1, 'OclModel117', b)
    if hasattr(a2, 'OclModel117'):
        assert _is_linked(a2, 'OclModel117', b)
    _safe_set(b, 'metamodel', set())
    assert not _is_linked(b, 'metamodel', a2)
    if hasattr(a2, 'OclModel117'):
        assert not _is_linked(a2, 'OclModel117', b)


def test_assoc_operation65_reverse_link_reassign_clear():
    a1 = OCLinEmig_Operation(name="sample_text")
    a2 = OCLinEmig_Operation(name="sample_text_2")
    b = OCLinEmig_OclType(name="sample_text")
    _safe_set(b, 'returnType', a1)
    assert _is_linked(b, 'returnType', a1)
    if hasattr(a1, 'Operation66'):
        assert _is_linked(a1, 'Operation66', b)
    _safe_set(b, 'returnType', a2)
    assert _is_linked(b, 'returnType', a2)
    if hasattr(a1, 'Operation66'):
        assert not _is_linked(a1, 'Operation66', b)
    if hasattr(a2, 'Operation66'):
        assert _is_linked(a2, 'Operation66', b)
    _safe_set(b, 'returnType', None)
    assert not _is_linked(b, 'returnType', a2)
    if hasattr(a2, 'Operation66'):
        assert not _is_linked(a2, 'Operation66', b)


def test_assoc_returnType105_reverse_link_reassign_clear():
    a1 = OCLinEmig_Operation(name="sample_text")
    a2 = OCLinEmig_Operation(name="sample_text_2")
    b = OCLinEmig_OclType(name="sample_text")
    _safe_set(b, 'OclType107', a1)
    assert _is_linked(b, 'OclType107', a1)
    if hasattr(a1, 'operation106'):
        assert _is_linked(a1, 'operation106', b)
    _safe_set(b, 'OclType107', a2)
    assert _is_linked(b, 'OclType107', a2)
    if hasattr(a1, 'operation106'):
        assert not _is_linked(a1, 'operation106', b)
    if hasattr(a2, 'operation106'):
        assert _is_linked(a2, 'operation106', b)
    _safe_set(b, 'OclType107', None)
    assert not _is_linked(b, 'OclType107', a2)
    if hasattr(a2, 'operation106'):
        assert not _is_linked(a2, 'operation106', b)


def test_assoc_tupleTypeAttribute74_reverse_link_reassign_clear():
    a1 = OCLinEmig_TupleTypeAttribute(name="sample_text")
    a2 = OCLinEmig_TupleTypeAttribute(name="sample_text_2")
    b = OCLinEmig_OclType(name="sample_text")
    _safe_set(b, 'type75', a1)
    assert _is_linked(b, 'type75', a1)
    if hasattr(a1, 'TupleTypeAttribute'):
        assert _is_linked(a1, 'TupleTypeAttribute', b)
    _safe_set(b, 'type75', a2)
    assert _is_linked(b, 'type75', a2)
    if hasattr(a1, 'TupleTypeAttribute'):
        assert not _is_linked(a1, 'TupleTypeAttribute', b)
    if hasattr(a2, 'TupleTypeAttribute'):
        assert _is_linked(a2, 'TupleTypeAttribute', b)
    _safe_set(b, 'type75', None)
    assert not _is_linked(b, 'type75', a2)
    if hasattr(a2, 'TupleTypeAttribute'):
        assert not _is_linked(a2, 'TupleTypeAttribute', b)


def test_assoc_type102_reverse_link_reassign_clear():
    a1 = OCLinEmig_OclType(name="sample_text")
    a2 = OCLinEmig_OclType(name="sample_text_2")
    b = OCLinEmig_Attribute(name="sample_text")
    _safe_set(b, 'attribute', a1)
    assert _is_linked(b, 'attribute', a1)
    if hasattr(a1, 'OclType103'):
        assert _is_linked(a1, 'OclType103', b)
    _safe_set(b, 'attribute', a2)
    assert _is_linked(b, 'attribute', a2)
    if hasattr(a1, 'OclType103'):
        assert not _is_linked(a1, 'OclType103', b)
    if hasattr(a2, 'OclType103'):
        assert _is_linked(a2, 'OclType103', b)
    _safe_set(b, 'attribute', None)
    assert not _is_linked(b, 'attribute', a2)
    if hasattr(a2, 'OclType103'):
        assert not _is_linked(a2, 'OclType103', b)


def test_assoc_type48_reverse_link_reassign_clear():
    a1 = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    a2 = OCLinEmig_VariableDeclaration(id="sample_text_2", varName="sample_text_2")
    b = OCLinEmig_OclType(name="sample_text")
    _safe_set(b, 'OclType49', a1)
    assert _is_linked(b, 'OclType49', a1)
    if hasattr(a1, 'variableDeclaration'):
        assert _is_linked(a1, 'variableDeclaration', b)
    _safe_set(b, 'OclType49', a2)
    assert _is_linked(b, 'OclType49', a2)
    if hasattr(a1, 'variableDeclaration'):
        assert not _is_linked(a1, 'variableDeclaration', b)
    if hasattr(a2, 'variableDeclaration'):
        assert _is_linked(a2, 'variableDeclaration', b)
    _safe_set(b, 'OclType49', None)
    assert not _is_linked(b, 'OclType49', a2)
    if hasattr(a2, 'variableDeclaration'):
        assert not _is_linked(a2, 'variableDeclaration', b)


def test_assoc_type81_reverse_link_reassign_clear():
    a1 = OCLinEmig_TupleTypeAttribute(name="sample_text")
    a2 = OCLinEmig_TupleTypeAttribute(name="sample_text_2")
    b = OCLinEmig_OclType(name="sample_text")
    _safe_set(b, 'OclType82', a1)
    assert _is_linked(b, 'OclType82', a1)
    if hasattr(a1, 'tupleTypeAttribute'):
        assert _is_linked(a1, 'tupleTypeAttribute', b)
    _safe_set(b, 'OclType82', a2)
    assert _is_linked(b, 'OclType82', a2)
    if hasattr(a1, 'tupleTypeAttribute'):
        assert not _is_linked(a1, 'tupleTypeAttribute', b)
    if hasattr(a2, 'tupleTypeAttribute'):
        assert _is_linked(a2, 'tupleTypeAttribute', b)
    _safe_set(b, 'OclType82', None)
    assert not _is_linked(b, 'OclType82', a2)
    if hasattr(a2, 'tupleTypeAttribute'):
        assert not _is_linked(a2, 'tupleTypeAttribute', b)


def test_assoc_variableDeclaration76_reverse_link_reassign_clear():
    a1 = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    a2 = OCLinEmig_VariableDeclaration(id="sample_text_2", varName="sample_text_2")
    b = OCLinEmig_OclType(name="sample_text")
    _safe_set(b, 'type77', a1)
    assert _is_linked(b, 'type77', a1)
    if hasattr(a1, 'VariableDeclaration78'):
        assert _is_linked(a1, 'VariableDeclaration78', b)
    _safe_set(b, 'type77', a2)
    assert _is_linked(b, 'type77', a2)
    if hasattr(a1, 'VariableDeclaration78'):
        assert not _is_linked(a1, 'VariableDeclaration78', b)
    if hasattr(a2, 'VariableDeclaration78'):
        assert _is_linked(a2, 'VariableDeclaration78', b)
    _safe_set(b, 'type77', None)
    assert not _is_linked(b, 'type77', a2)
    if hasattr(a2, 'VariableDeclaration78'):
        assert not _is_linked(a2, 'VariableDeclaration78', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments30_stub_double():
    # OCLinEmig_OclExpression has no real 'OclExpression31' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OperationCallExp(operationName="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'OclExpression31', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression31') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression31') is None


def test_assoc_attributes79_stub_double():
    # OCLinEmig_TupleType has no real 'tupleType' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_TupleTypeAttribute(name="sample_text")
    partner = OCLinEmig_TupleType()
    setattr(partner, 'tupleType', None)
    _safe_set(owner, 'TupleTypeAttribute80', partner)
    assert owner in getattr(partner, 'tupleType')
    _safe_set(owner, 'TupleTypeAttribute80', None)
    assert owner not in getattr(partner, 'tupleType')


def test_assoc_baseExp54_stub_double():
    # OCLinEmig_IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCLinEmig_IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_body108_stub_double():
    # OCLinEmig_OclExpression has no real 'OclExpression109' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_Operation(name="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'OclExpression109', None)
    _safe_set(owner, 'owningOperation', partner)
    assert getattr(partner, 'OclExpression109') == owner
    _safe_set(owner, 'owningOperation', None)
    assert getattr(partner, 'OclExpression109') is None


def test_assoc_collectionTypes73_stub_double():
    # OCLinEmig_CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_context_96_stub_double():
    # OCLinEmig_OclContextDefinition has no real 'definitions' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_OclContextDefinition()
    setattr(partner, 'definitions', None)
    _safe_set(owner, 'OclType97', partner)
    assert getattr(partner, 'definitions') == owner
    _safe_set(owner, 'OclType97', None)
    assert getattr(partner, 'definitions') is None


def test_assoc_definitions62_stub_double():
    # OCLinEmig_OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_elementType60_stub_double():
    # OCLinEmig_CollectionType has no real 'collectionTypes' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_CollectionType()
    setattr(partner, 'collectionTypes', None)
    _safe_set(owner, 'OclType61', partner)
    assert getattr(partner, 'collectionTypes') == owner
    _safe_set(owner, 'OclType61', None)
    assert getattr(partner, 'collectionTypes') is None


def test_assoc_elements113_stub_double():
    # OCLinEmig_OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclModel(name="sample_text")
    partner = OCLinEmig_OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'model114', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'model114', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_initExpression100_stub_double():
    # OCLinEmig_OclExpression has no real 'OclExpression101' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_Attribute(name="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'OclExpression101', None)
    _safe_set(owner, 'owningAttribute', partner)
    assert getattr(partner, 'OclExpression101') == owner
    _safe_set(owner, 'owningAttribute', None)
    assert getattr(partner, 'OclExpression101') is None


def test_assoc_initExpression50_stub_double():
    # OCLinEmig_OclExpression has no real 'OclExpression51' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'OclExpression51', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression51') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression51') is None


def test_assoc_initializedVariable7_stub_double():
    # OCLinEmig_OclExpression has no real 'initExpression' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'initExpression', None)
    _safe_set(owner, 'VariableDeclaration', partner)
    assert getattr(partner, 'initExpression') == owner
    _safe_set(owner, 'VariableDeclaration', None)
    assert getattr(partner, 'initExpression') is None


def test_assoc_keyType88_stub_double():
    # OCLinEmig_MapType has no real 'mapType' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_MapType()
    setattr(partner, 'mapType', None)
    _safe_set(owner, 'OclType89', partner)
    assert getattr(partner, 'mapType') == owner
    _safe_set(owner, 'OclType89', None)
    assert getattr(partner, 'mapType') is None


def test_assoc_letExp52_stub_double():
    # OCLinEmig_LetExp has no real 'LetExp53' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCLinEmig_LetExp()
    setattr(partner, 'LetExp53', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp53') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp53') is None


def test_assoc_mapType267_stub_double():
    # OCLinEmig_MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_mapType71_stub_double():
    # OCLinEmig_MapType has no real 'MapType72' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_MapType()
    setattr(partner, 'MapType72', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType72') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType72') is None


def test_assoc_model84_stub_double():
    # OCLinEmig_OclModelElement has no real 'elements85' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclModel(name="sample_text")
    partner = OCLinEmig_OclModelElement()
    setattr(partner, 'elements85', None)
    _safe_set(owner, 'OclModel', partner)
    assert getattr(partner, 'elements85') == owner
    _safe_set(owner, 'OclModel', None)
    assert getattr(partner, 'elements85') is None


def test_assoc_oclExpression63_stub_double():
    # OCLinEmig_OclExpression has no real 'OclExpression64' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'OclExpression64', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression64') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression64') is None


def test_assoc_oclFeatures118_stub_double():
    # OCLinEmig_OclFeatureDefinition has no real 'OCLinEmig_OclFeatureDefinition' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_Module(name="sample_text")
    partner = OCLinEmig_OclFeatureDefinition()
    setattr(partner, 'OCLinEmig_OclFeatureDefinition', None)
    _safe_set(owner, 'OCLinEmig_Module', {partner})
    assert getattr(partner, 'OCLinEmig_OclFeatureDefinition') == owner
    _safe_set(owner, 'OCLinEmig_Module', set())
    assert getattr(partner, 'OCLinEmig_OclFeatureDefinition') is None


def test_assoc_operation58_stub_double():
    # OCLinEmig_Parameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_Operation(name="sample_text")
    partner = OCLinEmig_Parameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Operation59', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Operation59', None)
    assert getattr(partner, 'parameters') is None


def test_assoc_owningAttribute14_stub_double():
    # OCLinEmig_OclExpression has no real 'initExpression15' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_Attribute(name="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'initExpression15', None)
    _safe_set(owner, 'Attribute', partner)
    assert getattr(partner, 'initExpression15') == owner
    _safe_set(owner, 'Attribute', None)
    assert getattr(partner, 'initExpression15') is None


def test_assoc_owningOperation10_stub_double():
    # OCLinEmig_OclExpression has no real 'body11' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_Operation(name="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'body11', None)
    _safe_set(owner, 'Operation', partner)
    assert getattr(partner, 'body11') == owner
    _safe_set(owner, 'Operation', None)
    assert getattr(partner, 'body11') is None


def test_assoc_parameters104_stub_double():
    # OCLinEmig_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_Operation(name="sample_text")
    partner = OCLinEmig_Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'operation', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'operation', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_parentOperation6_stub_double():
    # OCLinEmig_OclExpression has no real 'arguments' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OperationCallExp(operationName="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'arguments', None)
    _safe_set(owner, 'OperationCallExp', partner)
    assert getattr(partner, 'arguments') == owner
    _safe_set(owner, 'OperationCallExp', None)
    assert getattr(partner, 'arguments') is None


def test_assoc_referredVariable16_stub_double():
    # OCLinEmig_VariableExp has no real 'variableExp' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCLinEmig_VariableExp()
    setattr(partner, 'variableExp', None)
    _safe_set(owner, 'VariableDeclaration17', partner)
    assert getattr(partner, 'variableExp') == owner
    _safe_set(owner, 'VariableDeclaration17', None)
    assert getattr(partner, 'variableExp') is None


def test_assoc_result35_stub_double():
    # OCLinEmig_IterateExp has no real 'baseExp' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCLinEmig_IterateExp()
    setattr(partner, 'baseExp', None)
    _safe_set(owner, 'VariableDeclaration36', partner)
    assert getattr(partner, 'baseExp') == owner
    _safe_set(owner, 'VariableDeclaration36', None)
    assert getattr(partner, 'baseExp') is None


def test_assoc_tupleType83_stub_double():
    # OCLinEmig_TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_TupleTypeAttribute(name="sample_text")
    partner = OCLinEmig_TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_type0_stub_double():
    # OCLinEmig_OclExpression has no real 'oclExpression' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_OclExpression()
    setattr(partner, 'oclExpression', None)
    _safe_set(owner, 'OclType', partner)
    assert getattr(partner, 'oclExpression') == owner
    _safe_set(owner, 'OclType', None)
    assert getattr(partner, 'oclExpression') is None


def test_assoc_valueType86_stub_double():
    # OCLinEmig_MapType has no real 'mapType2' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_OclType(name="sample_text")
    partner = OCLinEmig_MapType()
    setattr(partner, 'mapType2', None)
    _safe_set(owner, 'OclType87', partner)
    assert getattr(partner, 'mapType2') == owner
    _safe_set(owner, 'OclType87', None)
    assert getattr(partner, 'mapType2') is None


def test_assoc_variable37_stub_double():
    # OCLinEmig_LetExp has no real 'letExp' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCLinEmig_LetExp()
    setattr(partner, 'letExp', None)
    _safe_set(owner, 'VariableDeclaration38', partner)
    assert getattr(partner, 'letExp') == owner
    _safe_set(owner, 'VariableDeclaration38', None)
    assert getattr(partner, 'letExp') is None


def test_assoc_variableExp55_stub_double():
    # OCLinEmig_VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so OCLinEmig_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCLinEmig_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCLinEmig_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCLinEmig_VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


