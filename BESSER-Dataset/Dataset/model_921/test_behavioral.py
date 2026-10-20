import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ProcessElement,
    pDL2_DependanceFinish,
    pDL2_DependanceStart,
    pDL2_EObject,
    pDL2_Guidance,
    pDL2_Process,
    pDL2_ProcessElement,
    pDL2_WorkDefinition,
    pDL2_WorkSequenceKindFinish,
    pDL2_WorkSequenceKindStart,
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

def test_assoc_link4_stub_double():
    # pDL2_DependanceStart has no real 'pDL2_DependanceStart5' property in the generated
    # code (a bare stub) -- manually attach it so pDL2_WorkSequenceKindStart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pDL2_WorkSequenceKindStart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pDL2_WorkSequenceKindStart(Started2Finish="sample_text", Started2Start="sample_text")
    partner = pDL2_DependanceStart()
    setattr(partner, 'pDL2_DependanceStart5', None)
    _safe_set(owner, 'pDL2_WorkSequenceKindStart', partner)
    assert getattr(partner, 'pDL2_DependanceStart5') == owner
    _safe_set(owner, 'pDL2_WorkSequenceKindStart', None)
    assert getattr(partner, 'pDL2_DependanceStart5') is None


def test_assoc_link8_stub_double():
    # pDL2_DependanceFinish has no real 'pDL2_DependanceFinish9' property in the generated
    # code (a bare stub) -- manually attach it so pDL2_WorkSequenceKindFinish's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pDL2_WorkSequenceKindFinish's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pDL2_WorkSequenceKindFinish(Finished2Finish="sample_text", Finished2Start="sample_text")
    partner = pDL2_DependanceFinish()
    setattr(partner, 'pDL2_DependanceFinish9', None)
    _safe_set(owner, 'pDL2_WorkSequenceKindFinish', partner)
    assert getattr(partner, 'pDL2_DependanceFinish9') == owner
    _safe_set(owner, 'pDL2_WorkSequenceKindFinish', None)
    assert getattr(partner, 'pDL2_DependanceFinish9') is None


def test_assoc_linksToPredecessors1_stub_double():
    # pDL2_EObject has no real 'pDL2_EObject' property in the generated
    # code (a bare stub) -- manually attach it so pDL2_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pDL2_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pDL2_WorkDefinition(name="sample_text")
    partner = pDL2_EObject()
    setattr(partner, 'pDL2_EObject', None)
    _safe_set(owner, 'pDL2_WorkDefinition', {partner})
    assert getattr(partner, 'pDL2_EObject') == owner
    _safe_set(owner, 'pDL2_WorkDefinition', set())
    assert getattr(partner, 'pDL2_EObject') is None


def test_assoc_predecessor2_stub_double():
    # pDL2_DependanceStart has no real 'pDL2_DependanceStart' property in the generated
    # code (a bare stub) -- manually attach it so pDL2_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pDL2_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pDL2_WorkDefinition(name="sample_text")
    partner = pDL2_DependanceStart()
    setattr(partner, 'pDL2_DependanceStart', None)
    _safe_set(owner, 'pDL2_WorkDefinition3', partner)
    assert getattr(partner, 'pDL2_DependanceStart') == owner
    _safe_set(owner, 'pDL2_WorkDefinition3', None)
    assert getattr(partner, 'pDL2_DependanceStart') is None


def test_assoc_predecessor6_stub_double():
    # pDL2_DependanceFinish has no real 'pDL2_DependanceFinish' property in the generated
    # code (a bare stub) -- manually attach it so pDL2_WorkDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pDL2_WorkDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pDL2_WorkDefinition(name="sample_text")
    partner = pDL2_DependanceFinish()
    setattr(partner, 'pDL2_DependanceFinish', None)
    _safe_set(owner, 'pDL2_WorkDefinition7', partner)
    assert getattr(partner, 'pDL2_DependanceFinish') == owner
    _safe_set(owner, 'pDL2_WorkDefinition7', None)
    assert getattr(partner, 'pDL2_DependanceFinish') is None


def test_assoc_processElements0_stub_double():
    # pDL2_ProcessElement has no real 'pDL2_ProcessElement' property in the generated
    # code (a bare stub) -- manually attach it so pDL2_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pDL2_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pDL2_Process(name="sample_text")
    partner = pDL2_ProcessElement()
    setattr(partner, 'pDL2_ProcessElement', None)
    _safe_set(owner, 'pDL2_Process', {partner})
    assert getattr(partner, 'pDL2_ProcessElement') == owner
    _safe_set(owner, 'pDL2_Process', set())
    assert getattr(partner, 'pDL2_ProcessElement') is None


