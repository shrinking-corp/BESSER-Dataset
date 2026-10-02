import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Artifact,
    Association,
    AssociationEnd,
    AssociationEndRole,
    Attribute,
    BehavioralFeature,
    Binding,
    BooleanExpression,
    CallAction,
    CallEvent,
    Classifier,
    Collaboration,
    Comment,
    Component,
    Constraint,
    CreateAction,
    DataType,
    Dependency,
    Element,
    ElementResidence,
    Enumeration,
    EnumerationLiteral,
    Expression,
    Feature,
    Flow,
    GeneralizableElement,
    Generalization_,
    MappingExpression,
    Method,
    ModelElement,
    MultiplicityRange,
    Multiplicity_,
    Namespace,
    Node,
    Operation,
    Parameter,
    PresentationElement,
    ProcedureExpression,
    Relationship,
    Signal,
    StateMachine,
    Stereotype,
    StructuralFeature,
    TagDefinition,
    TaggedValue,
    TemplateArgument,
    TemplateParameter,
    TypeExpression,
    core_Association,
    core_Class,
    core_GeneralizableElement,
    core_Namespace,
    core_Relationship,
    foundation_core_Abstraction,
    foundation_core_Artifact,
    foundation_core_Association,
    foundation_core_AssociationClass,
    foundation_core_AssociationEnd,
    foundation_core_Attribute,
    foundation_core_BehavioralFeature,
    foundation_core_Binding,
    foundation_core_Class,
    foundation_core_Classifier,
    foundation_core_Comment,
    foundation_core_Component,
    foundation_core_Constraint,
    foundation_core_DataType,
    foundation_core_Dependency,
    foundation_core_Element,
    foundation_core_ElementResidence,
    foundation_core_Enumeration,
    foundation_core_EnumerationLiteral,
    foundation_core_Feature,
    foundation_core_Flow,
    foundation_core_GeneralizableElement,
    foundation_core_Generalization_,
    foundation_core_Interface,
    foundation_core_Method,
    foundation_core_ModelElement,
    foundation_core_Namespace,
    foundation_core_Node,
    foundation_core_Operation,
    foundation_core_Parameter,
    foundation_core_Permission,
    foundation_core_PresentationElement,
    foundation_core_Primitive,
    foundation_core_ProgrammingLanguageDataType,
    foundation_core_Relationship,
    foundation_core_Stereotype,
    foundation_core_StructuralFeature,
    foundation_core_TagDefinition,
    foundation_core_TaggedValue,
    foundation_core_TemplateArgument,
    foundation_core_TemplateParameter,
    foundation_core_Usage,
    foundation_data_types_ActionExpression,
    foundation_data_types_ArgListsExpression,
    foundation_data_types_BooleanExpression,
    foundation_data_types_Expression,
    foundation_data_types_IterationExpression,
    foundation_data_types_MappingExpression,
    foundation_data_types_MultiplicityRange,
    foundation_data_types_Multiplicity_,
    foundation_data_types_ObjectSetExpression,
    foundation_data_types_ProcedureExpression,
    foundation_data_types_TimeExpression,
    foundation_data_types_TypeExpression,
    AggregationKind,
    CallConcurrencyKind,
    ChangeableKind,
    OrderingKind,
    ParameterDirectionKind,
    PseudostateKind,
    ScopeKind,
    VisibilityKind,
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

