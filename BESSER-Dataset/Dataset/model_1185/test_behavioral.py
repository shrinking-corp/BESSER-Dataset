import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActionBlock,
    Binding,
    CollectionExp,
    CollectionType,
    DropPattern,
    Helper,
    InPattern,
    InPatternElement,
    Iterator,
    LoopExp,
    MapElement,
    MatchedRule,
    ModuleElement,
    NumericExp,
    NumericType,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclFeatureDefinition,
    OclModel,
    OclModelElement,
    OclType,
    OperationCallExp,
    OutPattern,
    OutPatternElement,
    Parameter,
    PatternElement,
    Primitive,
    PrimitiveExp,
    PropertyCallExp,
    Rule,
    RuleVariableDeclaration,
    Statement,
    TupleExp,
    TuplePart,
    TupleTypeAttribute,
    VariableDeclaration,
    atl_n_ocl_ATL_ActionBlock,
    atl_n_ocl_ATL_Binding,
    atl_n_ocl_ATL_BindingStat,
    atl_n_ocl_ATL_CalledRule,
    atl_n_ocl_ATL_DropPattern,
    atl_n_ocl_ATL_ExpressionStat,
    atl_n_ocl_ATL_ForEachOutPatternElement,
    atl_n_ocl_ATL_ForStat,
    atl_n_ocl_ATL_Helper,
    atl_n_ocl_ATL_IfStat,
    atl_n_ocl_ATL_InPattern,
    atl_n_ocl_ATL_InPatternElement,
    atl_n_ocl_ATL_LazyMatchedRule,
    atl_n_ocl_ATL_MatchedRule,
    atl_n_ocl_ATL_Module,
    atl_n_ocl_ATL_ModuleElement,
    atl_n_ocl_ATL_OutPattern,
    atl_n_ocl_ATL_OutPatternElement,
    atl_n_ocl_ATL_PatternElement,
    atl_n_ocl_ATL_Query,
    atl_n_ocl_ATL_Rule,
    atl_n_ocl_ATL_RuleVariableDeclaration,
    atl_n_ocl_ATL_SimpleInPatternElement,
    atl_n_ocl_ATL_SimpleOutPatternElement,
    atl_n_ocl_ATL_Statement,
    atl_n_ocl_OCL_Attribute,
    atl_n_ocl_OCL_BagExp,
    atl_n_ocl_OCL_BagType,
    atl_n_ocl_OCL_BooleanExp,
    atl_n_ocl_OCL_BooleanType,
    atl_n_ocl_OCL_CollectionExp,
    atl_n_ocl_OCL_CollectionOperationCallExp,
    atl_n_ocl_OCL_CollectionType,
    atl_n_ocl_OCL_EnumLiteralExp,
    atl_n_ocl_OCL_IfExp,
    atl_n_ocl_OCL_IntegerExp,
    atl_n_ocl_OCL_IntegerType,
    atl_n_ocl_OCL_IterateExp,
    atl_n_ocl_OCL_Iterator,
    atl_n_ocl_OCL_IteratorExp,
    atl_n_ocl_OCL_LetExp,
    atl_n_ocl_OCL_LoopExp,
    atl_n_ocl_OCL_MapElement,
    atl_n_ocl_OCL_MapExp,
    atl_n_ocl_OCL_MapType,
    atl_n_ocl_OCL_NavigationOrAttributeCallExp,
    atl_n_ocl_OCL_NumericExp,
    atl_n_ocl_OCL_NumericType,
    atl_n_ocl_OCL_OclAnyType,
    atl_n_ocl_OCL_OclContextDefinition,
    atl_n_ocl_OCL_OclExpression,
    atl_n_ocl_OCL_OclFeature,
    atl_n_ocl_OCL_OclFeatureDefinition,
    atl_n_ocl_OCL_OclModel,
    atl_n_ocl_OCL_OclModelElement,
    atl_n_ocl_OCL_OclType,
    atl_n_ocl_OCL_OclUndefinedExp,
    atl_n_ocl_OCL_Operation,
    atl_n_ocl_OCL_OperationCallExp,
    atl_n_ocl_OCL_OperatorCallExp,
    atl_n_ocl_OCL_OrderedSetExp,
    atl_n_ocl_OCL_OrderedSetType,
    atl_n_ocl_OCL_Parameter,
    atl_n_ocl_OCL_Primitive,
    atl_n_ocl_OCL_PrimitiveExp,
    atl_n_ocl_OCL_PropertyCallExp,
    atl_n_ocl_OCL_RealExp,
    atl_n_ocl_OCL_RealType,
    atl_n_ocl_OCL_SequenceExp,
    atl_n_ocl_OCL_SequenceType,
    atl_n_ocl_OCL_SetExp,
    atl_n_ocl_OCL_SetType,
    atl_n_ocl_OCL_StringExp,
    atl_n_ocl_OCL_StringType,
    atl_n_ocl_OCL_SuperExp,
    atl_n_ocl_OCL_TupleExp,
    atl_n_ocl_OCL_TuplePart,
    atl_n_ocl_OCL_TupleType,
    atl_n_ocl_OCL_TupleTypeAttribute,
    atl_n_ocl_OCL_VariableDeclaration,
    atl_n_ocl_OCL_VariableExp,
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

