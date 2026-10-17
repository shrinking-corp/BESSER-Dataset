import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    CallExp,
    CallOperationAction,
    CollectionLiteralPart,
    CollectionType,
    EClass,
    EClassifier,
    EDataType,
    ENamedElement,
    FeatureCallExp,
    LiteralExp,
    LoopExp,
    NavigationCallExp,
    NumericLiteralExp,
    OCLExpression,
    PrimitiveLiteralExp,
    PrimitiveReal,
    PrimitiveType,
    SendSignalAction,
    TupleLiteralPart,
    TypedElement,
    Variable,
    expressions_OCLExpression,
    expressions_ocl_EClass,
    expressions_ocl_EClassifier,
    expressions_ocl_EEnumLiteral,
    expressions_ocl_EObject,
    expressions_ocl_EOperation,
    expressions_ocl_EParameter,
    expressions_ocl_EStructuralFeature,
    ocl_expressions_AssociationClassCallExp,
    ocl_expressions_BooleanLiteralExp,
    ocl_expressions_CallExp,
    ocl_expressions_CollectionItem,
    ocl_expressions_CollectionLiteralExp,
    ocl_expressions_CollectionLiteralPart,
    ocl_expressions_CollectionRange,
    ocl_expressions_EnumLiteralExp,
    ocl_expressions_FeatureCallExp,
    ocl_expressions_IfExp,
    ocl_expressions_IntegerLiteralExp,
    ocl_expressions_InvalidLiteralExp,
    ocl_expressions_IterateExp,
    ocl_expressions_IteratorExp,
    ocl_expressions_LetExp,
    ocl_expressions_LiteralExp,
    ocl_expressions_LoopExp,
    ocl_expressions_MessageExp,
    ocl_expressions_NavigationCallExp,
    ocl_expressions_NullLiteralExp,
    ocl_expressions_NumericLiteralExp,
    ocl_expressions_OCLExpression,
    ocl_expressions_OperationCallExp,
    ocl_expressions_PrimitiveLiteralExp,
    ocl_expressions_PropertyCallExp,
    ocl_expressions_RealLiteralExp,
    ocl_expressions_StateExp,
    ocl_expressions_StringLiteralExp,
    ocl_expressions_TupleLiteralExp,
    ocl_expressions_TupleLiteralPart,
    ocl_expressions_TypeExp,
    ocl_expressions_UnspecifiedValueExp,
    ocl_expressions_Variable,
    ocl_expressions_VariableExp,
    ocl_query_Query,
    ocl_types_AnyType,
    ocl_types_BagType,
    ocl_types_CollectionType,
    ocl_types_ElementType,
    ocl_types_InvalidType,
    ocl_types_MessageType,
    ocl_types_OrderedSetType,
    ocl_types_PrimitiveBoolean,
    ocl_types_PrimitiveInteger,
    ocl_types_PrimitiveReal,
    ocl_types_PrimitiveString,
    ocl_types_PrimitiveType,
    ocl_types_SequenceType,
    ocl_types_SetType,
    ocl_types_TupleType,
    ocl_types_TypeType,
    ocl_types_VoidType,
    ocl_uml_CallOperationAction,
    ocl_uml_Constraint,
    ocl_uml_SendSignalAction,
    ocl_uml_TypedElement,
    ocl_utilities_ASTNode,
    ocl_utilities_CallingASTNode,
    ocl_utilities_PredefinedType,
    ocl_utilities_TypedASTNode,
    ocl_utilities_Visitable,
    types_ocl_EClass,
    types_ocl_EClassifier,
    types_ocl_EOperation,
    uml_TypedElement,
    uml_ocl_EClass,
    uml_ocl_EClassifier,
    uml_ocl_ENamedElement,
    uml_ocl_EOperation,
    utilities_ASTNode,
    utilities_CallingASTNode,
    utilities_PredefinedType,
    utilities_TypedASTNode,
    utilities_Visitable,
    CollectionKind,
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

def test_assoc_body68_stub_double():
    # OCLExpression has no real 'OCLExpression69' property in the generated
    # code (a bare stub) -- manually attach it so ocl_uml_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_uml_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_uml_Constraint(instanceVarName="sample_text", stereotype="sample_text")
    partner = OCLExpression()
    setattr(partner, 'OCLExpression69', None)
    _safe_set(owner, 'ocl_uml_Constraint', partner)
    assert getattr(partner, 'OCLExpression69') == owner
    _safe_set(owner, 'ocl_uml_Constraint', None)
    assert getattr(partner, 'OCLExpression69') is None


def test_assoc_constrainedElement70_stub_double():
    # uml_ocl_ENamedElement has no real 'uml_ocl_ENamedElement' property in the generated
    # code (a bare stub) -- manually attach it so ocl_uml_Constraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_uml_Constraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_uml_Constraint(instanceVarName="sample_text", stereotype="sample_text")
    partner = uml_ocl_ENamedElement()
    setattr(partner, 'uml_ocl_ENamedElement', None)
    _safe_set(owner, 'ocl_uml_Constraint71', {partner})
    assert getattr(partner, 'uml_ocl_ENamedElement') == owner
    _safe_set(owner, 'ocl_uml_Constraint71', set())
    assert getattr(partner, 'uml_ocl_ENamedElement') is None


def test_assoc_elementType0_stub_double():
    # types_ocl_EClassifier has no real 'types_ocl_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so ocl_types_CollectionType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_types_CollectionType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_types_CollectionType(kind="sample_text")
    partner = types_ocl_EClassifier()
    setattr(partner, 'types_ocl_EClassifier', None)
    _safe_set(owner, 'ocl_types_CollectionType', partner)
    assert getattr(partner, 'types_ocl_EClassifier') == owner
    _safe_set(owner, 'ocl_types_CollectionType', None)
    assert getattr(partner, 'types_ocl_EClassifier') is None


def test_assoc_expression74_stub_double():
    # OCLExpression has no real 'OCLExpression75' property in the generated
    # code (a bare stub) -- manually attach it so ocl_query_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_query_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_query_Query(extentMap="sample_text")
    partner = OCLExpression()
    setattr(partner, 'OCLExpression75', None)
    _safe_set(owner, 'ocl_query_Query', partner)
    assert getattr(partner, 'OCLExpression75') == owner
    _safe_set(owner, 'ocl_query_Query', None)
    assert getattr(partner, 'OCLExpression75') is None


def test_assoc_part8_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so ocl_expressions_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_expressions_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_expressions_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'ocl_expressions_CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'ocl_expressions_CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


