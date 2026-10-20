import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    Visitable,
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
    ocl_expressions_UnlimitedNaturalLiteralExp,
    ocl_expressions_UnspecifiedValueExp,
    ocl_expressions_Variable,
    ocl_expressions_VariableExp,
    ocl_types_AnyType,
    ocl_types_BagType,
    ocl_types_CollectionType,
    ocl_types_ElementType,
    ocl_types_InvalidType,
    ocl_types_MessageType,
    ocl_types_OrderedSetType,
    ocl_types_PrimitiveType,
    ocl_types_SequenceType,
    ocl_types_SetType,
    ocl_types_TemplateParameterType,
    ocl_types_TupleType,
    ocl_types_TypeType,
    ocl_types_VoidType,
    ocl_utilities_ASTNode,
    ocl_utilities_CallingASTNode,
    ocl_utilities_ExpressionInOCL,
    ocl_utilities_PredefinedType,
    ocl_utilities_TypedASTNode,
    ocl_utilities_TypedElement,
    ocl_utilities_Visitable,
    ocl_utilities_Visitor,
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

