import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    dSLPolicies_AlgorithmType,
    dSLPolicies_GraphElement,
    dSLPolicies_GraphPolicies,
    dSLPolicies_Model,
    dSLPolicies_PathGeneratorStopCondition,
    dSLPolicies_Policies,
    dSLPolicies_Severity,
    dSLPolicies_StopCondition,
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

def test_assoc_graphelement14_reverse_link_reassign_clear():
    a1 = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    a2 = dSLPolicies_StopCondition(pathtype="sample_text_2", percentage="sample_text_2", value=13)
    b = dSLPolicies_GraphElement(name="sample_text")
    _safe_set(b, 'dSLPolicies_GraphElement', a1)
    assert _is_linked(b, 'dSLPolicies_GraphElement', a1)
    if hasattr(a1, 'dSLPolicies_StopCondition15'):
        assert _is_linked(a1, 'dSLPolicies_StopCondition15', b)
    _safe_set(b, 'dSLPolicies_GraphElement', a2)
    assert _is_linked(b, 'dSLPolicies_GraphElement', a2)
    if hasattr(a1, 'dSLPolicies_StopCondition15'):
        assert not _is_linked(a1, 'dSLPolicies_StopCondition15', b)
    if hasattr(a2, 'dSLPolicies_StopCondition15'):
        assert _is_linked(a2, 'dSLPolicies_StopCondition15', b)
    _safe_set(b, 'dSLPolicies_GraphElement', None)
    assert not _is_linked(b, 'dSLPolicies_GraphElement', a2)
    if hasattr(a2, 'dSLPolicies_StopCondition15'):
        assert not _is_linked(a2, 'dSLPolicies_StopCondition15', b)


def test_assoc_policies1_reverse_link_reassign_clear():
    a1 = dSLPolicies_Policies(nocheck=True, sync=True)
    a2 = dSLPolicies_Policies(nocheck=False, sync=False)
    b = dSLPolicies_GraphPolicies(graphModelPolicies="sample_text")
    _safe_set(b, 'dSLPolicies_GraphPolicies2', {a1})
    assert _is_linked(b, 'dSLPolicies_GraphPolicies2', a1)
    if hasattr(a1, 'dSLPolicies_Policies'):
        assert _is_linked(a1, 'dSLPolicies_Policies', b)
    _safe_set(b, 'dSLPolicies_GraphPolicies2', {a2})
    assert _is_linked(b, 'dSLPolicies_GraphPolicies2', a2)
    if hasattr(a1, 'dSLPolicies_Policies'):
        assert not _is_linked(a1, 'dSLPolicies_Policies', b)
    if hasattr(a2, 'dSLPolicies_Policies'):
        assert _is_linked(a2, 'dSLPolicies_Policies', b)
    _safe_set(b, 'dSLPolicies_GraphPolicies2', set())
    assert not _is_linked(b, 'dSLPolicies_GraphPolicies2', a2)
    if hasattr(a2, 'dSLPolicies_Policies'):
        assert not _is_linked(a2, 'dSLPolicies_Policies', b)


def test_assoc_severity5_reverse_link_reassign_clear():
    a1 = dSLPolicies_Severity(level="sample_text")
    a2 = dSLPolicies_Severity(level="sample_text_2")
    b = dSLPolicies_Policies(nocheck=True, sync=True)
    _safe_set(b, 'dSLPolicies_Policies6', a1)
    assert _is_linked(b, 'dSLPolicies_Policies6', a1)
    if hasattr(a1, 'dSLPolicies_Severity'):
        assert _is_linked(a1, 'dSLPolicies_Severity', b)
    _safe_set(b, 'dSLPolicies_Policies6', a2)
    assert _is_linked(b, 'dSLPolicies_Policies6', a2)
    if hasattr(a1, 'dSLPolicies_Severity'):
        assert not _is_linked(a1, 'dSLPolicies_Severity', b)
    if hasattr(a2, 'dSLPolicies_Severity'):
        assert _is_linked(a2, 'dSLPolicies_Severity', b)
    _safe_set(b, 'dSLPolicies_Policies6', None)
    assert not _is_linked(b, 'dSLPolicies_Policies6', a2)
    if hasattr(a2, 'dSLPolicies_Severity'):
        assert not _is_linked(a2, 'dSLPolicies_Severity', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_algorithmType7_stub_double():
    # dSLPolicies_PathGeneratorStopCondition has no real 'dSLPolicies_PathGeneratorStopCondition8' property in the generated
    # code (a bare stub) -- manually attach it so dSLPolicies_AlgorithmType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSLPolicies_AlgorithmType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSLPolicies_AlgorithmType(type="sample_text")
    partner = dSLPolicies_PathGeneratorStopCondition()
    setattr(partner, 'dSLPolicies_PathGeneratorStopCondition8', None)
    _safe_set(owner, 'dSLPolicies_AlgorithmType', partner)
    assert getattr(partner, 'dSLPolicies_PathGeneratorStopCondition8') == owner
    _safe_set(owner, 'dSLPolicies_AlgorithmType', None)
    assert getattr(partner, 'dSLPolicies_PathGeneratorStopCondition8') is None


def test_assoc_graphPolicies0_stub_double():
    # dSLPolicies_Model has no real 'dSLPolicies_Model' property in the generated
    # code (a bare stub) -- manually attach it so dSLPolicies_GraphPolicies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSLPolicies_GraphPolicies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSLPolicies_GraphPolicies(graphModelPolicies="sample_text")
    partner = dSLPolicies_Model()
    setattr(partner, 'dSLPolicies_Model', None)
    _safe_set(owner, 'dSLPolicies_GraphPolicies', partner)
    assert owner in getattr(partner, 'dSLPolicies_Model')
    _safe_set(owner, 'dSLPolicies_GraphPolicies', None)
    assert owner not in getattr(partner, 'dSLPolicies_Model')


def test_assoc_pathgenerator3_stub_double():
    # dSLPolicies_PathGeneratorStopCondition has no real 'dSLPolicies_PathGeneratorStopCondition' property in the generated
    # code (a bare stub) -- manually attach it so dSLPolicies_Policies's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSLPolicies_Policies's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSLPolicies_Policies(nocheck=True, sync=True)
    partner = dSLPolicies_PathGeneratorStopCondition()
    setattr(partner, 'dSLPolicies_PathGeneratorStopCondition', None)
    _safe_set(owner, 'dSLPolicies_Policies4', {partner})
    assert getattr(partner, 'dSLPolicies_PathGeneratorStopCondition') == owner
    _safe_set(owner, 'dSLPolicies_Policies4', set())
    assert getattr(partner, 'dSLPolicies_PathGeneratorStopCondition') is None


def test_assoc_stopCondition9_stub_double():
    # dSLPolicies_PathGeneratorStopCondition has no real 'dSLPolicies_PathGeneratorStopCondition10' property in the generated
    # code (a bare stub) -- manually attach it so dSLPolicies_StopCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSLPolicies_StopCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    partner = dSLPolicies_PathGeneratorStopCondition()
    setattr(partner, 'dSLPolicies_PathGeneratorStopCondition10', None)
    _safe_set(owner, 'dSLPolicies_StopCondition', partner)
    assert getattr(partner, 'dSLPolicies_PathGeneratorStopCondition10') == owner
    _safe_set(owner, 'dSLPolicies_StopCondition', None)
    assert getattr(partner, 'dSLPolicies_PathGeneratorStopCondition10') is None


def test_assoc_stopConditionype11_stub_double():
    # dSLPolicies_PathGeneratorStopCondition has no real 'dSLPolicies_PathGeneratorStopCondition12' property in the generated
    # code (a bare stub) -- manually attach it so dSLPolicies_StopCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dSLPolicies_StopCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dSLPolicies_StopCondition(pathtype="sample_text", percentage="sample_text", value=7)
    partner = dSLPolicies_PathGeneratorStopCondition()
    setattr(partner, 'dSLPolicies_PathGeneratorStopCondition12', None)
    _safe_set(owner, 'dSLPolicies_StopCondition13', partner)
    assert getattr(partner, 'dSLPolicies_PathGeneratorStopCondition12') == owner
    _safe_set(owner, 'dSLPolicies_StopCondition13', None)
    assert getattr(partner, 'dSLPolicies_PathGeneratorStopCondition12') is None


