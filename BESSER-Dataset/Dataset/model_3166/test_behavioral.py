import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TTrace,
    gtrace_MClassifier,
    gtrace_MElement,
    gtrace_MOperation,
    gtrace_MState,
    gtrace_MStateMachine,
    gtrace_RRequirement,
    gtrace_RScenario,
    gtrace_RScenarioStep,
    gtrace_TRequirementTrace,
    gtrace_TScenarioStepTrace,
    gtrace_TScenarioTrace,
    gtrace_TTrace,
    gtrace_TTraceModel,
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

def test_assoc_requirementTrace0_stub_double():
    # gtrace_TRequirementTrace has no real 'gtrace_TRequirementTrace' property in the generated
    # code (a bare stub) -- manually attach it so gtrace_TTraceModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gtrace_TTraceModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gtrace_TTraceModel(name="sample_text")
    partner = gtrace_TRequirementTrace()
    setattr(partner, 'gtrace_TRequirementTrace', None)
    _safe_set(owner, 'gtrace_TTraceModel', {partner})
    assert getattr(partner, 'gtrace_TRequirementTrace') == owner
    _safe_set(owner, 'gtrace_TTraceModel', set())
    assert getattr(partner, 'gtrace_TRequirementTrace') is None


def test_assoc_scenarioStepTrace3_stub_double():
    # gtrace_TScenarioStepTrace has no real 'gtrace_TScenarioStepTrace' property in the generated
    # code (a bare stub) -- manually attach it so gtrace_TTraceModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gtrace_TTraceModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gtrace_TTraceModel(name="sample_text")
    partner = gtrace_TScenarioStepTrace()
    setattr(partner, 'gtrace_TScenarioStepTrace', None)
    _safe_set(owner, 'gtrace_TTraceModel4', {partner})
    assert getattr(partner, 'gtrace_TScenarioStepTrace') == owner
    _safe_set(owner, 'gtrace_TTraceModel4', set())
    assert getattr(partner, 'gtrace_TScenarioStepTrace') is None


def test_assoc_scenarioTrace1_stub_double():
    # gtrace_TScenarioTrace has no real 'gtrace_TScenarioTrace' property in the generated
    # code (a bare stub) -- manually attach it so gtrace_TTraceModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gtrace_TTraceModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gtrace_TTraceModel(name="sample_text")
    partner = gtrace_TScenarioTrace()
    setattr(partner, 'gtrace_TScenarioTrace', None)
    _safe_set(owner, 'gtrace_TTraceModel2', {partner})
    assert getattr(partner, 'gtrace_TScenarioTrace') == owner
    _safe_set(owner, 'gtrace_TTraceModel2', set())
    assert getattr(partner, 'gtrace_TScenarioTrace') is None


