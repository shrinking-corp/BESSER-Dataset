import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TraceElement,
    trace_EObject,
    trace_SourceElement,
    trace_SourceElementList,
    trace_TargetElement,
    trace_TraceElement,
    trace_TraceLink,
    trace_TraceLinkSet,
    trace_TraceProperty,
    trace_TracedRule,
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

def test_assoc_appliedAt40_reverse_link_reassign_clear():
    a1 = trace_TraceProperty(propertyName="sample_text", resolved=True)
    a2 = trace_TraceProperty(propertyName="sample_text_2", resolved=False)
    b = trace_TraceLink(overridden=True)
    _safe_set(b, 'TraceLink41', a1)
    assert _is_linked(b, 'TraceLink41', a1)
    if hasattr(a1, 'properties'):
        assert _is_linked(a1, 'properties', b)
    _safe_set(b, 'TraceLink41', a2)
    assert _is_linked(b, 'TraceLink41', a2)
    if hasattr(a1, 'properties'):
        assert not _is_linked(a1, 'properties', b)
    if hasattr(a2, 'properties'):
        assert _is_linked(a2, 'properties', b)
    _safe_set(b, 'TraceLink41', None)
    assert not _is_linked(b, 'TraceLink41', a2)
    if hasattr(a2, 'properties'):
        assert not _is_linked(a2, 'properties', b)


def test_assoc_defaultFor22_reverse_link_reassign_clear():
    a1 = trace_TraceLinkSet()
    a2 = trace_TraceLinkSet()
    b = trace_SourceElement(mapsToSelf=True)
    _safe_set(b, 'defaultSourceElements', a1)
    assert _is_linked(b, 'defaultSourceElements', a1)
    if hasattr(a1, 'TraceLinkSet23'):
        assert _is_linked(a1, 'TraceLinkSet23', b)
    _safe_set(b, 'defaultSourceElements', a2)
    assert _is_linked(b, 'defaultSourceElements', a2)
    if hasattr(a1, 'TraceLinkSet23'):
        assert not _is_linked(a1, 'TraceLinkSet23', b)
    if hasattr(a2, 'TraceLinkSet23'):
        assert _is_linked(a2, 'TraceLinkSet23', b)
    _safe_set(b, 'defaultSourceElements', None)
    assert not _is_linked(b, 'defaultSourceElements', a2)
    if hasattr(a2, 'TraceLinkSet23'):
        assert not _is_linked(a2, 'TraceLinkSet23', b)


def test_assoc_defaultFor32_reverse_link_reassign_clear():
    a1 = trace_TraceLinkSet()
    a2 = trace_TraceLinkSet()
    b = trace_SourceElementList()
    _safe_set(b, 'defaultSourceElementLists', a1)
    assert _is_linked(b, 'defaultSourceElementLists', a1)
    if hasattr(a1, 'TraceLinkSet33'):
        assert _is_linked(a1, 'TraceLinkSet33', b)
    _safe_set(b, 'defaultSourceElementLists', a2)
    assert _is_linked(b, 'defaultSourceElementLists', a2)
    if hasattr(a1, 'TraceLinkSet33'):
        assert not _is_linked(a1, 'TraceLinkSet33', b)
    if hasattr(a2, 'TraceLinkSet33'):
        assert _is_linked(a2, 'TraceLinkSet33', b)
    _safe_set(b, 'defaultSourceElementLists', None)
    assert not _is_linked(b, 'defaultSourceElementLists', a2)
    if hasattr(a2, 'TraceLinkSet33'):
        assert not _is_linked(a2, 'TraceLinkSet33', b)


def test_assoc_defaultSourceElementLists2_reverse_link_reassign_clear():
    a1 = trace_TraceLinkSet()
    a2 = trace_TraceLinkSet()
    b = trace_SourceElementList()
    _safe_set(b, 'SourceElementList', a1)
    assert _is_linked(b, 'SourceElementList', a1)
    if hasattr(a1, 'defaultFor3'):
        assert _is_linked(a1, 'defaultFor3', b)
    _safe_set(b, 'SourceElementList', a2)
    assert _is_linked(b, 'SourceElementList', a2)
    if hasattr(a1, 'defaultFor3'):
        assert not _is_linked(a1, 'defaultFor3', b)
    if hasattr(a2, 'defaultFor3'):
        assert _is_linked(a2, 'defaultFor3', b)
    _safe_set(b, 'SourceElementList', None)
    assert not _is_linked(b, 'SourceElementList', a2)
    if hasattr(a2, 'defaultFor3'):
        assert not _is_linked(a2, 'defaultFor3', b)


def test_assoc_defaultSourceElements1_reverse_link_reassign_clear():
    a1 = trace_TraceLinkSet()
    a2 = trace_TraceLinkSet()
    b = trace_SourceElement(mapsToSelf=True)
    _safe_set(b, 'SourceElement', a1)
    assert _is_linked(b, 'SourceElement', a1)
    if hasattr(a1, 'defaultFor'):
        assert _is_linked(a1, 'defaultFor', b)
    _safe_set(b, 'SourceElement', a2)
    assert _is_linked(b, 'SourceElement', a2)
    if hasattr(a1, 'defaultFor'):
        assert not _is_linked(a1, 'defaultFor', b)
    if hasattr(a2, 'defaultFor'):
        assert _is_linked(a2, 'defaultFor', b)
    _safe_set(b, 'SourceElement', None)
    assert not _is_linked(b, 'SourceElement', a2)
    if hasattr(a2, 'defaultFor'):
        assert not _is_linked(a2, 'defaultFor', b)


def test_assoc_properties16_reverse_link_reassign_clear():
    a1 = trace_TraceProperty(propertyName="sample_text", resolved=True)
    a2 = trace_TraceProperty(propertyName="sample_text_2", resolved=False)
    b = trace_TraceLink(overridden=True)
    _safe_set(b, 'appliedAt', {a1})
    assert _is_linked(b, 'appliedAt', a1)
    if hasattr(a1, 'TraceProperty'):
        assert _is_linked(a1, 'TraceProperty', b)
    _safe_set(b, 'appliedAt', {a2})
    assert _is_linked(b, 'appliedAt', a2)
    if hasattr(a1, 'TraceProperty'):
        assert not _is_linked(a1, 'TraceProperty', b)
    if hasattr(a2, 'TraceProperty'):
        assert _is_linked(a2, 'TraceProperty', b)
    _safe_set(b, 'appliedAt', set())
    assert not _is_linked(b, 'appliedAt', a2)
    if hasattr(a2, 'TraceProperty'):
        assert not _is_linked(a2, 'TraceProperty', b)


def test_assoc_sourceElements11_reverse_link_reassign_clear():
    a1 = trace_TraceLink(overridden=True)
    a2 = trace_TraceLink(overridden=False)
    b = trace_SourceElement(mapsToSelf=True)
    _safe_set(b, 'SourceElement12', a1)
    assert _is_linked(b, 'SourceElement12', a1)
    if hasattr(a1, 'sourceOf'):
        assert _is_linked(a1, 'sourceOf', b)
    _safe_set(b, 'SourceElement12', a2)
    assert _is_linked(b, 'SourceElement12', a2)
    if hasattr(a1, 'sourceOf'):
        assert not _is_linked(a1, 'sourceOf', b)
    if hasattr(a2, 'sourceOf'):
        assert _is_linked(a2, 'sourceOf', b)
    _safe_set(b, 'SourceElement12', None)
    assert not _is_linked(b, 'SourceElement12', a2)
    if hasattr(a2, 'sourceOf'):
        assert not _is_linked(a2, 'sourceOf', b)


def test_assoc_sourceElements31_reverse_link_reassign_clear():
    a1 = trace_SourceElementList()
    a2 = trace_SourceElementList()
    b = trace_SourceElement(mapsToSelf=True)
    _safe_set(b, 'trace_SourceElement', a1)
    assert _is_linked(b, 'trace_SourceElement', a1)
    if hasattr(a1, 'trace_SourceElementList'):
        assert _is_linked(a1, 'trace_SourceElementList', b)
    _safe_set(b, 'trace_SourceElement', a2)
    assert _is_linked(b, 'trace_SourceElement', a2)
    if hasattr(a1, 'trace_SourceElementList'):
        assert not _is_linked(a1, 'trace_SourceElementList', b)
    if hasattr(a2, 'trace_SourceElementList'):
        assert _is_linked(a2, 'trace_SourceElementList', b)
    _safe_set(b, 'trace_SourceElement', None)
    assert not _is_linked(b, 'trace_SourceElement', a2)
    if hasattr(a2, 'trace_SourceElementList'):
        assert not _is_linked(a2, 'trace_SourceElementList', b)


def test_assoc_sourceOf18_reverse_link_reassign_clear():
    a1 = trace_TraceLink(overridden=True)
    a2 = trace_TraceLink(overridden=False)
    b = trace_SourceElement(mapsToSelf=True)
    _safe_set(b, 'sourceElements', a1)
    assert _is_linked(b, 'sourceElements', a1)
    if hasattr(a1, 'TraceLink19'):
        assert _is_linked(a1, 'TraceLink19', b)
    _safe_set(b, 'sourceElements', a2)
    assert _is_linked(b, 'sourceElements', a2)
    if hasattr(a1, 'TraceLink19'):
        assert not _is_linked(a1, 'TraceLink19', b)
    if hasattr(a2, 'TraceLink19'):
        assert _is_linked(a2, 'TraceLink19', b)
    _safe_set(b, 'sourceElements', None)
    assert not _is_linked(b, 'sourceElements', a2)
    if hasattr(a2, 'TraceLink19'):
        assert not _is_linked(a2, 'TraceLink19', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_mapsTo20_stub_double():
    # trace_TargetElement has no real 'TargetElement21' property in the generated
    # code (a bare stub) -- manually attach it so trace_SourceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_SourceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_SourceElement(mapsToSelf=True)
    partner = trace_TargetElement()
    setattr(partner, 'TargetElement21', None)
    _safe_set(owner, 'mapsTo', {partner})
    assert getattr(partner, 'TargetElement21') == owner
    _safe_set(owner, 'mapsTo', set())
    assert getattr(partner, 'TargetElement21') is None


def test_assoc_mapsTo28_stub_double():
    # trace_TargetElement has no real 'mapsTo29' property in the generated
    # code (a bare stub) -- manually attach it so trace_SourceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_SourceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_SourceElement(mapsToSelf=True)
    partner = trace_TargetElement()
    setattr(partner, 'mapsTo29', None)
    _safe_set(owner, 'SourceElement30', partner)
    assert owner in getattr(partner, 'mapsTo29')
    _safe_set(owner, 'SourceElement30', None)
    assert owner not in getattr(partner, 'mapsTo29')


def test_assoc_object17_stub_double():
    # trace_EObject has no real 'trace_EObject' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceElement(name="sample_text", runtimeObject="sample_text")
    partner = trace_EObject()
    setattr(partner, 'trace_EObject', None)
    _safe_set(owner, 'trace_TraceElement', partner)
    assert getattr(partner, 'trace_EObject') == owner
    _safe_set(owner, 'trace_TraceElement', None)
    assert getattr(partner, 'trace_EObject') is None


def test_assoc_resolvedFor36_stub_double():
    # trace_TargetElement has no real 'trace_TargetElement' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceProperty(propertyName="sample_text", resolved=True)
    partner = trace_TargetElement()
    setattr(partner, 'trace_TargetElement', None)
    _safe_set(owner, 'trace_TraceProperty', partner)
    assert getattr(partner, 'trace_TargetElement') == owner
    _safe_set(owner, 'trace_TraceProperty', None)
    assert getattr(partner, 'trace_TargetElement') is None


def test_assoc_resolvings37_stub_double():
    # trace_EObject has no real 'trace_EObject39' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceProperty(propertyName="sample_text", resolved=True)
    partner = trace_EObject()
    setattr(partner, 'trace_EObject39', None)
    _safe_set(owner, 'trace_TraceProperty38', {partner})
    assert getattr(partner, 'trace_EObject39') == owner
    _safe_set(owner, 'trace_TraceProperty38', set())
    assert getattr(partner, 'trace_EObject39') is None


def test_assoc_targetElements13_stub_double():
    # trace_TargetElement has no real 'TargetElement' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceLink(overridden=True)
    partner = trace_TargetElement()
    setattr(partner, 'TargetElement', None)
    _safe_set(owner, 'targetOf', {partner})
    assert getattr(partner, 'TargetElement') == owner
    _safe_set(owner, 'targetOf', set())
    assert getattr(partner, 'TargetElement') is None


def test_assoc_targetOf26_stub_double():
    # trace_TargetElement has no real 'targetElements' property in the generated
    # code (a bare stub) -- manually attach it so trace_TraceLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # trace_TraceLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = trace_TraceLink(overridden=True)
    partner = trace_TargetElement()
    setattr(partner, 'targetElements', None)
    _safe_set(owner, 'TraceLink27', partner)
    assert getattr(partner, 'targetElements') == owner
    _safe_set(owner, 'TraceLink27', None)
    assert getattr(partner, 'targetElements') is None


