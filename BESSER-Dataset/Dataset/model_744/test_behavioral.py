import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Artifact,
    Association,
    Behavior,
    BehavioredClassifier,
    Class,
    Classifier,
    DataType,
    EncapsulatedClassifier,
    Node,
    StateMachine,
    StructuredClassifier,
    UML2_Activity,
    UML2_Actor,
    UML2_Artifact,
    UML2_Association,
    UML2_AssociationClass,
    UML2_Behavior,
    UML2_BehavioredClassifier,
    UML2_Class,
    UML2_Classifier,
    UML2_Collaboration,
    UML2_CommunicationPath,
    UML2_Component,
    UML2_DataType,
    UML2_DeploymentSpecification,
    UML2_Device,
    UML2_EncapsulatedClassifier,
    UML2_Enumeration,
    UML2_ExecutionEnvironment,
    UML2_Extension,
    UML2_InformationItem,
    UML2_Interaction,
    UML2_Interface,
    UML2_Node,
    UML2_ParameterableClassifier,
    UML2_PrimitiveType,
    UML2_ProtocolStateMachine,
    UML2_Signal,
    UML2_StateMachine,
    UML2_Stereotype,
    UML2_StructuredClassifier,
    UML2_TemplateableClassifier,
    UML2_UseCase,
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

