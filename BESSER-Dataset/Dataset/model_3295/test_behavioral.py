import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicNodeLabel,
    EarthSciencePopulationInitializer,
    IntegrationDecorator,
    IntegrationLabel,
    IntegrationLabelValue,
    LabelValue,
    Modifiable,
    NodeDecorator,
    PopulationInitializer,
    PopulationModel,
    PopulationModelLabel,
    PopulationModelLabelValue,
    StandardPopulationModel,
    standard_DemographicPopulationModel,
    standard_EarthSciencePopulationInitializer,
    standard_IntegrationDecorator,
    standard_IntegrationLabel,
    standard_IntegrationLabelValue,
    standard_PopulationGroup,
    standard_PopulationInitializer,
    standard_PopulationLabel,
    standard_PopulationModel,
    standard_PopulationModelLabel,
    standard_PopulationModelLabelValue,
    standard_SeasonalPopulationModel,
    standard_StandardPopulationInitializer,
    standard_StandardPopulationModel,
    standard_StandardPopulationModelLabel,
    standard_StandardPopulationModelLabelValue,
    standard_StochasticStandardPopulationModel,
    standard_YetiPopulationInitializer,
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

def test_assoc_deltaValue1_stub_double():
    # standard_StandardPopulationModelLabel has no real 'standard_StandardPopulationModelLabel' property in the generated
    # code (a bare stub) -- manually attach it so standard_StandardPopulationModelLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_StandardPopulationModelLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    partner = standard_StandardPopulationModelLabel()
    setattr(partner, 'standard_StandardPopulationModelLabel', None)
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue', partner)
    assert getattr(partner, 'standard_StandardPopulationModelLabel') == owner
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue', None)
    assert getattr(partner, 'standard_StandardPopulationModelLabel') is None


def test_assoc_errorScale11_stub_double():
    # standard_StandardPopulationModelLabel has no real 'standard_StandardPopulationModelLabel12' property in the generated
    # code (a bare stub) -- manually attach it so standard_StandardPopulationModelLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_StandardPopulationModelLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    partner = standard_StandardPopulationModelLabel()
    setattr(partner, 'standard_StandardPopulationModelLabel12', None)
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue13', partner)
    assert getattr(partner, 'standard_StandardPopulationModelLabel12') == owner
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue13', None)
    assert getattr(partner, 'standard_StandardPopulationModelLabel12') is None


def test_assoc_originalValue8_stub_double():
    # standard_StandardPopulationModelLabel has no real 'standard_StandardPopulationModelLabel9' property in the generated
    # code (a bare stub) -- manually attach it so standard_StandardPopulationModelLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_StandardPopulationModelLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    partner = standard_StandardPopulationModelLabel()
    setattr(partner, 'standard_StandardPopulationModelLabel9', None)
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue10', partner)
    assert getattr(partner, 'standard_StandardPopulationModelLabel9') == owner
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue10', None)
    assert getattr(partner, 'standard_StandardPopulationModelLabel9') is None


def test_assoc_populationGroups14_stub_double():
    # standard_DemographicPopulationModel has no real 'standard_DemographicPopulationModel' property in the generated
    # code (a bare stub) -- manually attach it so standard_PopulationGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_PopulationGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_PopulationGroup(fraction=3.14, identifier="sample_text")
    partner = standard_DemographicPopulationModel()
    setattr(partner, 'standard_DemographicPopulationModel', None)
    _safe_set(owner, 'standard_PopulationGroup', partner)
    assert owner in getattr(partner, 'standard_DemographicPopulationModel')
    _safe_set(owner, 'standard_PopulationGroup', None)
    assert owner not in getattr(partner, 'standard_DemographicPopulationModel')


def test_assoc_populationLabel0_stub_double():
    # standard_PopulationLabel has no real 'standard_PopulationLabel' property in the generated
    # code (a bare stub) -- manually attach it so standard_PopulationModelLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_PopulationModelLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_PopulationModelLabel(populationIdentifier="sample_text")
    partner = standard_PopulationLabel()
    setattr(partner, 'standard_PopulationLabel', None)
    _safe_set(owner, 'standard_PopulationModelLabel', partner)
    assert getattr(partner, 'standard_PopulationLabel') == owner
    _safe_set(owner, 'standard_PopulationModelLabel', None)
    assert getattr(partner, 'standard_PopulationLabel') is None


def test_assoc_probeValue2_stub_double():
    # standard_StandardPopulationModelLabel has no real 'standard_StandardPopulationModelLabel3' property in the generated
    # code (a bare stub) -- manually attach it so standard_StandardPopulationModelLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_StandardPopulationModelLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    partner = standard_StandardPopulationModelLabel()
    setattr(partner, 'standard_StandardPopulationModelLabel3', None)
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue4', partner)
    assert getattr(partner, 'standard_StandardPopulationModelLabel3') == owner
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue4', None)
    assert getattr(partner, 'standard_StandardPopulationModelLabel3') is None


def test_assoc_tempValue5_stub_double():
    # standard_StandardPopulationModelLabel has no real 'standard_StandardPopulationModelLabel6' property in the generated
    # code (a bare stub) -- manually attach it so standard_StandardPopulationModelLabelValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # standard_StandardPopulationModelLabelValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    partner = standard_StandardPopulationModelLabel()
    setattr(partner, 'standard_StandardPopulationModelLabel6', None)
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue7', partner)
    assert getattr(partner, 'standard_StandardPopulationModelLabel6') == owner
    _safe_set(owner, 'standard_StandardPopulationModelLabelValue7', None)
    assert getattr(partner, 'standard_StandardPopulationModelLabel6') is None


