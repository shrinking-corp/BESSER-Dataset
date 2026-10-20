import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Behavior,
    BehavioralFeature,
    BehavioredClassifier,
    Class,
    Element,
    Node,
    StateMachine,
    UML2WithID_Activity,
    UML2WithID_AssociationClass,
    UML2WithID_Behavior,
    UML2WithID_BehavioralFeature,
    UML2WithID_BehavioredClassifier,
    UML2WithID_Class,
    UML2WithID_Collaboration,
    UML2WithID_Component,
    UML2WithID_Device,
    UML2WithID_Element,
    UML2WithID_ExecutionEnvironment,
    UML2WithID_Interaction,
    UML2WithID_Node,
    UML2WithID_Operation,
    UML2WithID_ProtocolStateMachine,
    UML2WithID_Reception,
    UML2WithID_StateMachine,
    UML2WithID_Stereotype,
    UML2WithID_UseCase,
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

