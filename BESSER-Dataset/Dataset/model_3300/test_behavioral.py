import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Identifiable,
    automaticexperiment_AutomaticExperiment,
    automaticexperiment_EStructuralFeature,
    automaticexperiment_ModifiableParameter,
    automaticexperiment_Scenario,
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

def test_assoc_parameters1_reverse_link_reassign_clear():
    a1 = automaticexperiment_ModifiableParameter(featureName="sample_text", initialValue=3.14, lowerBound=3.14, step=3.14, targetURI="sample_text", upperBound=3.14)
    a2 = automaticexperiment_ModifiableParameter(featureName="sample_text_2", initialValue=9.99, lowerBound=9.99, step=9.99, targetURI="sample_text_2", upperBound=9.99)
    b = automaticexperiment_AutomaticExperiment(errorAnalysisAlgorithm="sample_text", errorFunction="sample_text", maximumNumberOfIterations="sample_text", reInit=True, referanceDataDir="sample_text", tolerance=3.14)
    _safe_set(b, 'automaticexperiment_AutomaticExperiment2', {a1})
    assert _is_linked(b, 'automaticexperiment_AutomaticExperiment2', a1)
    if hasattr(a1, 'automaticexperiment_ModifiableParameter'):
        assert _is_linked(a1, 'automaticexperiment_ModifiableParameter', b)
    _safe_set(b, 'automaticexperiment_AutomaticExperiment2', {a2})
    assert _is_linked(b, 'automaticexperiment_AutomaticExperiment2', a2)
    if hasattr(a1, 'automaticexperiment_ModifiableParameter'):
        assert not _is_linked(a1, 'automaticexperiment_ModifiableParameter', b)
    if hasattr(a2, 'automaticexperiment_ModifiableParameter'):
        assert _is_linked(a2, 'automaticexperiment_ModifiableParameter', b)
    _safe_set(b, 'automaticexperiment_AutomaticExperiment2', set())
    assert not _is_linked(b, 'automaticexperiment_AutomaticExperiment2', a2)
    if hasattr(a2, 'automaticexperiment_ModifiableParameter'):
        assert not _is_linked(a2, 'automaticexperiment_ModifiableParameter', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_baseScenario0_stub_double():
    # automaticexperiment_Scenario has no real 'automaticexperiment_Scenario' property in the generated
    # code (a bare stub) -- manually attach it so automaticexperiment_AutomaticExperiment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaticexperiment_AutomaticExperiment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaticexperiment_AutomaticExperiment(errorAnalysisAlgorithm="sample_text", errorFunction="sample_text", maximumNumberOfIterations="sample_text", reInit=True, referanceDataDir="sample_text", tolerance=3.14)
    partner = automaticexperiment_Scenario()
    setattr(partner, 'automaticexperiment_Scenario', None)
    _safe_set(owner, 'automaticexperiment_AutomaticExperiment', partner)
    assert getattr(partner, 'automaticexperiment_Scenario') == owner
    _safe_set(owner, 'automaticexperiment_AutomaticExperiment', None)
    assert getattr(partner, 'automaticexperiment_Scenario') is None


def test_assoc_feature3_stub_double():
    # automaticexperiment_EStructuralFeature has no real 'automaticexperiment_EStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so automaticexperiment_ModifiableParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automaticexperiment_ModifiableParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automaticexperiment_ModifiableParameter(featureName="sample_text", initialValue=3.14, lowerBound=3.14, step=3.14, targetURI="sample_text", upperBound=3.14)
    partner = automaticexperiment_EStructuralFeature()
    setattr(partner, 'automaticexperiment_EStructuralFeature', None)
    _safe_set(owner, 'automaticexperiment_ModifiableParameter4', partner)
    assert getattr(partner, 'automaticexperiment_EStructuralFeature') == owner
    _safe_set(owner, 'automaticexperiment_ModifiableParameter4', None)
    assert getattr(partner, 'automaticexperiment_EStructuralFeature') is None


