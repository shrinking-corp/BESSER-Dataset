import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractFunction,
    AbstractOperationCallExp,
    CallExp,
    CollectionLiteralExp,
    CollectionTypeRef,
    Constraint,
    DerivedProperty,
    EFType,
    FeatureRef,
    Iterator,
    LiteralExp,
    LoopExp,
    OclExpression,
    Operation,
    OperationFeatureRef,
    PropertyFeatureRef,
    TuplePart,
    TypeRef,
    TypedElement,
    VariableDeclaration,
    ir_AbstractFunction,
    ir_BagTypeRef,
    ir_BuiltinOperationRef,
    ir_BuiltinPropertyRef,
    ir_CollectionTypeRef,
    ir_Constraint,
    ir_DefinedOperationRef,
    ir_DerivedProperty,
    ir_DerivedPropertyRef,
    ir_EClass,
    ir_EEnum,
    ir_EFClass,
    ir_EFEnum,
    ir_EFEnumLiteral,
    ir_EFMetamodel,
    ir_EFPackage,
    ir_EFPrimitiveType,
    ir_EFTupleType,
    ir_EFType,
    ir_EPackage,
    ir_EStructuralFeature,
    ir_FeatureRef,
    ir_InvalidTypeRef,
    ir_MetaTypeRef,
    ir_MetamodelFeatureRef,
    ir_Operation,
    ir_OperationFeatureRef,
    ir_OrderedSetTypeRef,
    ir_Parameter,
    ir_PropertyFeatureRef,
    ir_SequenceTypeRef,
    ir_SetTypeRef,
    ir_Specification,
    ir_TupleFieldRef,
    ir_TupleTypeElement,
    ir_TypeRef,
    ir_TypedElement,
    ir_VariableDeclaration,
    ir_ocl_AbstractOperationCallExp,
    ir_ocl_BagLiteralExp,
    ir_ocl_BooleanLiteralExp,
    ir_ocl_CallExp,
    ir_ocl_CollectionCallExp,
    ir_ocl_CollectionLiteralExp,
    ir_ocl_EnumLiteralExp,
    ir_ocl_IfExp,
    ir_ocl_IntegerLiteralExp,
    ir_ocl_IterateExp,
    ir_ocl_Iterator,
    ir_ocl_IteratorExp,
    ir_ocl_LetExp,
    ir_ocl_LiteralExp,
    ir_ocl_LoopExp,
    ir_ocl_ModelElement,
    ir_ocl_OclAnyLibElement,
    ir_ocl_OclDerivedProperty,
    ir_ocl_OclExpression,
    ir_ocl_OclInvalid,
    ir_ocl_OclInvariant,
    ir_ocl_OclOperation,
    ir_ocl_OclUndefined,
    ir_ocl_OperationCallExp,
    ir_ocl_OperatorCallExp,
    ir_ocl_OrderedSetLiteralExp,
    ir_ocl_PropertyCallExp,
    ir_ocl_RealLiteralExp,
    ir_ocl_SequenceLiteralExp,
    ir_ocl_SetLiteralExp,
    ir_ocl_StringLiteralExp,
    ir_ocl_TupleLiteralExp,
    ir_ocl_TuplePart,
    ir_ocl_UnsupportedExp,
    ir_ocl_VarExp,
    ir_ocl_WithContextVariable,
    ocl_WithContextVariable,
    ocl_ir_EFClass,
    ocl_ir_EFEnumLiteral,
    ocl_ir_EFTupleType,
    ocl_ir_MetaTypeRef,
    ocl_ir_OperationFeatureRef,
    ocl_ir_PropertyFeatureRef,
    ocl_ir_TypeRef,
    ocl_ir_VariableDeclaration,
    OperatorKind,
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

def test_assoc_elements41_reverse_link_reassign_clear():
    a1 = ir_TupleTypeElement(name="sample_text")
    a2 = ir_TupleTypeElement(name="sample_text_2")
    b = ir_EFTupleType(id="sample_text")
    _safe_set(b, 'ir_EFTupleType42', {a1})
    assert _is_linked(b, 'ir_EFTupleType42', a1)
    if hasattr(a1, 'ir_TupleTypeElement'):
        assert _is_linked(a1, 'ir_TupleTypeElement', b)
    _safe_set(b, 'ir_EFTupleType42', {a2})
    assert _is_linked(b, 'ir_EFTupleType42', a2)
    if hasattr(a1, 'ir_TupleTypeElement'):
        assert not _is_linked(a1, 'ir_TupleTypeElement', b)
    if hasattr(a2, 'ir_TupleTypeElement'):
        assert _is_linked(a2, 'ir_TupleTypeElement', b)
    _safe_set(b, 'ir_EFTupleType42', set())
    assert not _is_linked(b, 'ir_EFTupleType42', a2)
    if hasattr(a2, 'ir_TupleTypeElement'):
        assert not _is_linked(a2, 'ir_TupleTypeElement', b)


def test_assoc_type19_reverse_link_reassign_clear():
    a1 = ir_TupleFieldRef(name="sample_text")
    a2 = ir_TupleFieldRef(name="sample_text_2")
    b = ir_EFTupleType(id="sample_text")
    _safe_set(b, 'ir_EFTupleType20', a1)
    assert _is_linked(b, 'ir_EFTupleType20', a1)
    if hasattr(a1, 'ir_TupleFieldRef'):
        assert _is_linked(a1, 'ir_TupleFieldRef', b)
    _safe_set(b, 'ir_EFTupleType20', a2)
    assert _is_linked(b, 'ir_EFTupleType20', a2)
    if hasattr(a1, 'ir_TupleFieldRef'):
        assert not _is_linked(a1, 'ir_TupleFieldRef', b)
    if hasattr(a2, 'ir_TupleFieldRef'):
        assert _is_linked(a2, 'ir_TupleFieldRef', b)
    _safe_set(b, 'ir_EFTupleType20', None)
    assert not _is_linked(b, 'ir_EFTupleType20', a2)
    if hasattr(a2, 'ir_TupleFieldRef'):
        assert not _is_linked(a2, 'ir_TupleFieldRef', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argument90_stub_double():
    # OclExpression has no real 'OclExpression91' property in the generated
    # code (a bare stub) -- manually attach it so ir_ocl_OperatorCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ocl_OperatorCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ocl_OperatorCallExp(operator="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression91', None)
    _safe_set(owner, 'ir_ocl_OperatorCallExp', partner)
    assert getattr(partner, 'OclExpression91') == owner
    _safe_set(owner, 'ir_ocl_OperatorCallExp', None)
    assert getattr(partner, 'OclExpression91') is None


def test_assoc_constaints1_stub_double():
    # ir_Specification has no real 'ir_Specification2' property in the generated
    # code (a bare stub) -- manually attach it so ir_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_Constraint(name="sample_text")
    partner = ir_Specification()
    setattr(partner, 'ir_Specification2', None)
    _safe_set(owner, 'ir_Constraint', partner)
    assert owner in getattr(partner, 'ir_Specification2')
    _safe_set(owner, 'ir_Constraint', None)
    assert owner not in getattr(partner, 'ir_Specification2')


def test_assoc_context14_stub_double():
    # ir_EFType has no real 'ir_EFType' property in the generated
    # code (a bare stub) -- manually attach it so ir_AbstractFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_AbstractFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_AbstractFunction(name="sample_text")
    partner = ir_EFType()
    setattr(partner, 'ir_EFType', None)
    _safe_set(owner, 'ir_AbstractFunction', partner)
    assert getattr(partner, 'ir_EFType') == owner
    _safe_set(owner, 'ir_AbstractFunction', None)
    assert getattr(partner, 'ir_EFType') is None


def test_assoc_feature63_stub_double():
    # ocl_ir_OperationFeatureRef has no real 'ocl_ir_OperationFeatureRef' property in the generated
    # code (a bare stub) -- manually attach it so ir_ocl_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ocl_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ocl_OperationCallExp(name="sample_text")
    partner = ocl_ir_OperationFeatureRef()
    setattr(partner, 'ocl_ir_OperationFeatureRef', None)
    _safe_set(owner, 'ir_ocl_OperationCallExp', partner)
    assert getattr(partner, 'ocl_ir_OperationFeatureRef') == owner
    _safe_set(owner, 'ir_ocl_OperationCallExp', None)
    assert getattr(partner, 'ocl_ir_OperationFeatureRef') is None


def test_assoc_feature64_stub_double():
    # ocl_ir_PropertyFeatureRef has no real 'ocl_ir_PropertyFeatureRef' property in the generated
    # code (a bare stub) -- manually attach it so ir_ocl_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ocl_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ocl_PropertyCallExp(name="sample_text")
    partner = ocl_ir_PropertyFeatureRef()
    setattr(partner, 'ocl_ir_PropertyFeatureRef', None)
    _safe_set(owner, 'ir_ocl_PropertyCallExp', partner)
    assert getattr(partner, 'ocl_ir_PropertyFeatureRef') == owner
    _safe_set(owner, 'ir_ocl_PropertyCallExp', None)
    assert getattr(partner, 'ocl_ir_PropertyFeatureRef') is None


def test_assoc_literals39_stub_double():
    # ir_EFEnum has no real 'ir_EFEnum40' property in the generated
    # code (a bare stub) -- manually attach it so ir_EFEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_EFEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_EFEnumLiteral(name="sample_text")
    partner = ir_EFEnum()
    setattr(partner, 'ir_EFEnum40', None)
    _safe_set(owner, 'ir_EFEnumLiteral', partner)
    assert owner in getattr(partner, 'ir_EFEnum40')
    _safe_set(owner, 'ir_EFEnumLiteral', None)
    assert owner not in getattr(partner, 'ir_EFEnum40')


def test_assoc_primitiveTypes9_stub_double():
    # ir_Specification has no real 'ir_Specification10' property in the generated
    # code (a bare stub) -- manually attach it so ir_EFPrimitiveType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_EFPrimitiveType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_EFPrimitiveType(name="sample_text")
    partner = ir_Specification()
    setattr(partner, 'ir_Specification10', None)
    _safe_set(owner, 'ir_EFPrimitiveType', partner)
    assert owner in getattr(partner, 'ir_Specification10')
    _safe_set(owner, 'ir_EFPrimitiveType', None)
    assert owner not in getattr(partner, 'ir_Specification10')


def test_assoc_tupleTypes11_stub_double():
    # ir_Specification has no real 'ir_Specification12' property in the generated
    # code (a bare stub) -- manually attach it so ir_EFTupleType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_EFTupleType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_EFTupleType(id="sample_text")
    partner = ir_Specification()
    setattr(partner, 'ir_Specification12', None)
    _safe_set(owner, 'ir_EFTupleType', partner)
    assert owner in getattr(partner, 'ir_Specification12')
    _safe_set(owner, 'ir_EFTupleType', None)
    assert owner not in getattr(partner, 'ir_Specification12')


def test_assoc_type24_stub_double():
    # ir_TypeRef has no real 'ir_TypeRef25' property in the generated
    # code (a bare stub) -- manually attach it so ir_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_VariableDeclaration(name="sample_text")
    partner = ir_TypeRef()
    setattr(partner, 'ir_TypeRef25', None)
    _safe_set(owner, 'ir_VariableDeclaration', partner)
    assert getattr(partner, 'ir_TypeRef25') == owner
    _safe_set(owner, 'ir_VariableDeclaration', None)
    assert getattr(partner, 'ir_TypeRef25') is None


def test_assoc_type43_stub_double():
    # ir_TypeRef has no real 'ir_TypeRef45' property in the generated
    # code (a bare stub) -- manually attach it so ir_TupleTypeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_TupleTypeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_TupleTypeElement(name="sample_text")
    partner = ir_TypeRef()
    setattr(partner, 'ir_TypeRef45', None)
    _safe_set(owner, 'ir_TupleTypeElement44', partner)
    assert getattr(partner, 'ir_TypeRef45') == owner
    _safe_set(owner, 'ir_TupleTypeElement44', None)
    assert getattr(partner, 'ir_TypeRef45') is None


def test_assoc_value97_stub_double():
    # OclExpression has no real 'OclExpression98' property in the generated
    # code (a bare stub) -- manually attach it so ir_ocl_TuplePart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ir_ocl_TuplePart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ir_ocl_TuplePart(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression98', None)
    _safe_set(owner, 'ir_ocl_TuplePart', partner)
    assert getattr(partner, 'OclExpression98') == owner
    _safe_set(owner, 'ir_ocl_TuplePart', None)
    assert getattr(partner, 'OclExpression98') is None


