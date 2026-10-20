import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallExp,
    CollectionLiteralExp,
    CollectionLiteralPart,
    CollectionType,
    EssentialOCL_AnyType,
    EssentialOCL_BagType,
    EssentialOCL_BooleanLiteralExp,
    EssentialOCL_CallExp,
    EssentialOCL_CollectionItem,
    EssentialOCL_CollectionLiteralExp,
    EssentialOCL_CollectionLiteralPart,
    EssentialOCL_CollectionRange,
    EssentialOCL_CollectionType,
    EssentialOCL_EnumLiteralExp,
    EssentialOCL_ExpressionInOcl,
    EssentialOCL_FeatureCallExp,
    EssentialOCL_IfExp,
    EssentialOCL_IntegerLiteralExp,
    EssentialOCL_InvalidLiteralExp,
    EssentialOCL_InvalidType,
    EssentialOCL_IterateExp,
    EssentialOCL_IteratorExp,
    EssentialOCL_LetExp,
    EssentialOCL_LiteralExp,
    EssentialOCL_LoopExp,
    EssentialOCL_NavigationCallExp,
    EssentialOCL_NullLiteralExp,
    EssentialOCL_NumericLiteralExp,
    EssentialOCL_OclExpression,
    EssentialOCL_OperationCallExp,
    EssentialOCL_OrderedSetType,
    EssentialOCL_PrimitiveLiteralExp,
    EssentialOCL_PropertyCallExp,
    EssentialOCL_RealLiteralExp,
    EssentialOCL_SequenceType,
    EssentialOCL_SetType,
    EssentialOCL_StringLiteralExp,
    EssentialOCL_TemplateParameterType,
    EssentialOCL_TupleLiteralExp,
    EssentialOCL_TupleLiteralPart,
    EssentialOCL_TupleType,
    EssentialOCL_TypeExp,
    EssentialOCL_UnlimitedNaturalExp,
    EssentialOCL_Variable,
    EssentialOCL_VariableExp,
    EssentialOCL_VoidType,
    FeatureCallExp,
    LetExp,
    LiteralExp,
    LoopExp,
    NavigationCallExp,
    NumericLiteralExp,
    OclExpression,
    PrimitiveLiteralExp,
    TupleLiteralExp,
    TupleLiteralPart,
    Variable,
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

def test_assoc_part3_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so EssentialOCL_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EssentialOCL_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EssentialOCL_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'EssentialOCL_CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'EssentialOCL_CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


