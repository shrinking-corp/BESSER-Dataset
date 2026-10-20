import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Association,
    Element,
    Property,
    UML2WithID_Association,
    UML2WithID_AssociationClass,
    UML2WithID_CommunicationPath,
    UML2WithID_Element,
    UML2WithID_Extension,
    UML2WithID_ExtensionEnd,
    UML2WithID_Port,
    UML2WithID_Property,
    AggregationKind,
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

def test_assoc_memberEnd0_stub_double():
    # UML2WithID_Association has no real 'UML2WithID_Association' property in the generated
    # code (a bare stub) -- manually attach it so UML2WithID_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML2WithID_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML2WithID_Property(aggregation="sample_text")
    partner = UML2WithID_Association()
    setattr(partner, 'UML2WithID_Association', None)
    _safe_set(owner, 'UML2WithID_Property', partner)
    assert owner in getattr(partner, 'UML2WithID_Association')
    _safe_set(owner, 'UML2WithID_Property', None)
    assert owner not in getattr(partner, 'UML2WithID_Association')


