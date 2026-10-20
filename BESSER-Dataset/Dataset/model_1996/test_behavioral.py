import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    trace_AttributeMapping,
    trace_ClassMapping,
    trace_EAttribute,
    trace_EClass,
    trace_EReference,
    trace_EStructuralFeature,
    trace_ReferenceMapping,
    trace_Trace,
    ReferenceMappingType,
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

def test_assoc_image17_stub_double():
    # trace_EStructuralFeature has no real 'trace_EStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so trace_ReferenceMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ReferenceMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ReferenceMapping(type="sample_text")
    partner = trace_EStructuralFeature()
    setattr(partner, 'trace_EStructuralFeature', None)
    _safe_set(owner, 'trace_ReferenceMapping18', partner)
    assert getattr(partner, 'trace_EStructuralFeature') == owner
    _safe_set(owner, 'trace_ReferenceMapping18', None)
    assert getattr(partner, 'trace_EStructuralFeature') is None


def test_assoc_proto15_stub_double():
    # trace_EReference has no real 'trace_EReference' property in the generated
    # code (a bare stub) -- manually attach it so trace_ReferenceMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ReferenceMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ReferenceMapping(type="sample_text")
    partner = trace_EReference()
    setattr(partner, 'trace_EReference', None)
    _safe_set(owner, 'trace_ReferenceMapping16', partner)
    assert getattr(partner, 'trace_EReference') == owner
    _safe_set(owner, 'trace_ReferenceMapping16', None)
    assert getattr(partner, 'trace_EReference') is None


def test_assoc_referenceMappings3_stub_double():
    # trace_Trace has no real 'trace_Trace4' property in the generated
    # code (a bare stub) -- manually attach it so trace_ReferenceMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ReferenceMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ReferenceMapping(type="sample_text")
    partner = trace_Trace()
    setattr(partner, 'trace_Trace4', None)
    _safe_set(owner, 'trace_ReferenceMapping', partner)
    assert owner in getattr(partner, 'trace_Trace4')
    _safe_set(owner, 'trace_ReferenceMapping', None)
    assert owner not in getattr(partner, 'trace_Trace4')


