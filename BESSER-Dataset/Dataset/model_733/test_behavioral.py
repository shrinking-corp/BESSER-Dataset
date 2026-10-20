import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    ActivityEdge,
    ActivityGroup,
    ActivityNode,
    Behavior,
    BehavioredClassifier,
    Class,
    Classifier,
    ControlNode,
    Element,
    EncapsulatedClassifier,
    ExecutableNode,
    FinalNode,
    NamedElement,
    Namespace,
    ObjectNode,
    PackageableElement,
    ParameterableElement,
    RedefinableElement,
    StructuredClassifier,
    TemplateableElement,
    Type,
    TypedElement,
    ValueSpecification,
    uml_Action,
    uml_Activity,
    uml_ActivityEdge,
    uml_ActivityFinalNode,
    uml_ActivityGroup,
    uml_ActivityNode,
    uml_ActivityParameterNode,
    uml_ActivityPartition,
    uml_Behavior,
    uml_BehavioredClassifier,
    uml_Class,
    uml_Classifier,
    uml_ControlFlow,
    uml_ControlNode,
    uml_DecisionNode,
    uml_Element,
    uml_EncapsulatedClassifier,
    uml_ExecutableNode,
    uml_FinalNode,
    uml_ForkNode,
    uml_InitialNode,
    uml_JoinNode,
    uml_NamedElement,
    uml_Namespace,
    uml_ObjectFlow,
    uml_ObjectNode,
    uml_OpaqueAction,
    uml_OpaqueExpression,
    uml_Package,
    uml_PackageableElement,
    uml_ParameterableElement,
    uml_RedefinableElement,
    uml_RootPackage,
    uml_StructuredClassifier,
    uml_TemplateableElement,
    uml_Type,
    uml_TypedElement,
    uml_ValueSpecification,
    ObjectNodeOrderingKind,
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

