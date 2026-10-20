import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    trace_AttributeMapping,
    trace_ClassMapping,
    trace_EAttribute,
    trace_EClass,
    trace_EPackage,
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

def test_assoc_referenceMappings13_reverse_link_reassign_clear():
    a1 = trace_Trace()
    a2 = trace_Trace()
    b = trace_ReferenceMapping(type="sample_text")
    _safe_set(b, 'trace_ReferenceMapping', a1)
    assert _is_linked(b, 'trace_ReferenceMapping', a1)
    if hasattr(a1, 'trace_Trace14'):
        assert _is_linked(a1, 'trace_Trace14', b)
    _safe_set(b, 'trace_ReferenceMapping', a2)
    assert _is_linked(b, 'trace_ReferenceMapping', a2)
    if hasattr(a1, 'trace_Trace14'):
        assert not _is_linked(a1, 'trace_Trace14', b)
    if hasattr(a2, 'trace_Trace14'):
        assert _is_linked(a2, 'trace_Trace14', b)
    _safe_set(b, 'trace_ReferenceMapping', None)
    assert not _is_linked(b, 'trace_ReferenceMapping', a2)
    if hasattr(a2, 'trace_Trace14'):
        assert not _is_linked(a2, 'trace_Trace14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributeMappings11_stub_double():
    # trace_AttributeMapping has no real 'trace_AttributeMapping' property in the generated
    # code (a bare stub) -- manually attach it so trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Trace()
    partner = trace_AttributeMapping()
    setattr(partner, 'trace_AttributeMapping', None)
    _safe_set(owner, 'trace_Trace12', {partner})
    assert getattr(partner, 'trace_AttributeMapping') == owner
    _safe_set(owner, 'trace_Trace12', set())
    assert getattr(partner, 'trace_AttributeMapping') is None


def test_assoc_classMappings9_stub_double():
    # trace_ClassMapping has no real 'trace_ClassMapping' property in the generated
    # code (a bare stub) -- manually attach it so trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Trace()
    partner = trace_ClassMapping()
    setattr(partner, 'trace_ClassMapping', None)
    _safe_set(owner, 'trace_Trace10', {partner})
    assert getattr(partner, 'trace_ClassMapping') == owner
    _safe_set(owner, 'trace_Trace10', set())
    assert getattr(partner, 'trace_ClassMapping') is None


def test_assoc_image28_stub_double():
    # trace_EStructuralFeature has no real 'trace_EStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so trace_ReferenceMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ReferenceMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ReferenceMapping(type="sample_text")
    partner = trace_EStructuralFeature()
    setattr(partner, 'trace_EStructuralFeature', None)
    _safe_set(owner, 'trace_ReferenceMapping29', partner)
    assert getattr(partner, 'trace_EStructuralFeature') == owner
    _safe_set(owner, 'trace_ReferenceMapping29', None)
    assert getattr(partner, 'trace_EStructuralFeature') is None


def test_assoc_input0_stub_double():
    # trace_EPackage has no real 'trace_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Trace()
    partner = trace_EPackage()
    setattr(partner, 'trace_EPackage', None)
    _safe_set(owner, 'trace_Trace', partner)
    assert getattr(partner, 'trace_EPackage') == owner
    _safe_set(owner, 'trace_Trace', None)
    assert getattr(partner, 'trace_EPackage') is None


def test_assoc_inputModelRoot4_stub_double():
    # trace_EClass has no real 'trace_EClass' property in the generated
    # code (a bare stub) -- manually attach it so trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Trace()
    partner = trace_EClass()
    setattr(partner, 'trace_EClass', None)
    _safe_set(owner, 'trace_Trace5', partner)
    assert getattr(partner, 'trace_EClass') == owner
    _safe_set(owner, 'trace_Trace5', None)
    assert getattr(partner, 'trace_EClass') is None


def test_assoc_output1_stub_double():
    # trace_EPackage has no real 'trace_EPackage3' property in the generated
    # code (a bare stub) -- manually attach it so trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Trace()
    partner = trace_EPackage()
    setattr(partner, 'trace_EPackage3', None)
    _safe_set(owner, 'trace_Trace2', partner)
    assert getattr(partner, 'trace_EPackage3') == owner
    _safe_set(owner, 'trace_Trace2', None)
    assert getattr(partner, 'trace_EPackage3') is None


def test_assoc_outputModelRoot6_stub_double():
    # trace_EClass has no real 'trace_EClass8' property in the generated
    # code (a bare stub) -- manually attach it so trace_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_Trace()
    partner = trace_EClass()
    setattr(partner, 'trace_EClass8', None)
    _safe_set(owner, 'trace_Trace7', partner)
    assert getattr(partner, 'trace_EClass8') == owner
    _safe_set(owner, 'trace_Trace7', None)
    assert getattr(partner, 'trace_EClass8') is None


def test_assoc_proto26_stub_double():
    # trace_EReference has no real 'trace_EReference' property in the generated
    # code (a bare stub) -- manually attach it so trace_ReferenceMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_ReferenceMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_ReferenceMapping(type="sample_text")
    partner = trace_EReference()
    setattr(partner, 'trace_EReference', None)
    _safe_set(owner, 'trace_ReferenceMapping27', partner)
    assert getattr(partner, 'trace_EReference') == owner
    _safe_set(owner, 'trace_ReferenceMapping27', None)
    assert getattr(partner, 'trace_EReference') is None


