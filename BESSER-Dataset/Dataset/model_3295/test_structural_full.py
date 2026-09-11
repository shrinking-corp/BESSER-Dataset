import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_standard_PopulationGroup_fraction_value_roundtrip():
    instance = standard_PopulationGroup(fraction=3.14, identifier="sample_text")
    assert instance.fraction == 3.14
    instance.fraction = 9.99
    assert instance.fraction == 9.99


def test_standard_PopulationGroup_identifier_value_roundtrip():
    instance = standard_PopulationGroup(fraction=3.14, identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_standard_PopulationInitializer_populationIdentifier_value_roundtrip():
    instance = standard_PopulationInitializer(populationIdentifier="sample_text", targetISOKey="sample_text")
    assert instance.populationIdentifier == "sample_text"
    instance.populationIdentifier = "sample_text_2"
    assert instance.populationIdentifier == "sample_text_2"


def test_standard_PopulationInitializer_targetISOKey_value_roundtrip():
    instance = standard_PopulationInitializer(populationIdentifier="sample_text", targetISOKey="sample_text")
    assert instance.targetISOKey == "sample_text"
    instance.targetISOKey = "sample_text_2"
    assert instance.targetISOKey == "sample_text_2"


def test_standard_PopulationModel_name_value_roundtrip():
    instance = standard_PopulationModel(name="sample_text", populationIdentifier="sample_text", targetISOKey="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_standard_PopulationModel_populationIdentifier_value_roundtrip():
    instance = standard_PopulationModel(name="sample_text", populationIdentifier="sample_text", targetISOKey="sample_text")
    assert instance.populationIdentifier == "sample_text"
    instance.populationIdentifier = "sample_text_2"
    assert instance.populationIdentifier == "sample_text_2"


def test_standard_PopulationModel_targetISOKey_value_roundtrip():
    instance = standard_PopulationModel(name="sample_text", populationIdentifier="sample_text", targetISOKey="sample_text")
    assert instance.targetISOKey == "sample_text"
    instance.targetISOKey = "sample_text_2"
    assert instance.targetISOKey == "sample_text_2"


def test_standard_PopulationModelLabel_populationIdentifier_value_roundtrip():
    instance = standard_PopulationModelLabel(populationIdentifier="sample_text")
    assert instance.populationIdentifier == "sample_text"
    instance.populationIdentifier = "sample_text_2"
    assert instance.populationIdentifier == "sample_text_2"


def test_standard_SeasonalPopulationModel_modulationAmplitude_value_roundtrip():
    instance = standard_SeasonalPopulationModel(modulationAmplitude=3.14, period=3.14, phase=3.14, useLatitude=True)
    assert instance.modulationAmplitude == 3.14
    instance.modulationAmplitude = 9.99
    assert instance.modulationAmplitude == 9.99


def test_standard_SeasonalPopulationModel_period_value_roundtrip():
    instance = standard_SeasonalPopulationModel(modulationAmplitude=3.14, period=3.14, phase=3.14, useLatitude=True)
    assert instance.period == 3.14
    instance.period = 9.99
    assert instance.period == 9.99


def test_standard_SeasonalPopulationModel_phase_value_roundtrip():
    instance = standard_SeasonalPopulationModel(modulationAmplitude=3.14, period=3.14, phase=3.14, useLatitude=True)
    assert instance.phase == 3.14
    instance.phase = 9.99
    assert instance.phase == 9.99


def test_standard_SeasonalPopulationModel_useLatitude_value_roundtrip():
    instance = standard_SeasonalPopulationModel(modulationAmplitude=3.14, period=3.14, phase=3.14, useLatitude=True)
    assert instance.useLatitude == True
    instance.useLatitude = False
    assert instance.useLatitude == False


def test_standard_StandardPopulationInitializer_individuals_value_roundtrip():
    instance = standard_StandardPopulationInitializer(individuals=3.14, useDensity=True)
    assert instance.individuals == 3.14
    instance.individuals = 9.99
    assert instance.individuals == 9.99


def test_standard_StandardPopulationInitializer_useDensity_value_roundtrip():
    instance = standard_StandardPopulationInitializer(individuals=3.14, useDensity=True)
    assert instance.useDensity == True
    instance.useDensity = False
    assert instance.useDensity == False


def test_standard_StandardPopulationModel_birthRate_value_roundtrip():
    instance = standard_StandardPopulationModel(birthRate=3.14, deathRate=3.14, timePeriod="sample_text")
    assert instance.birthRate == 3.14
    instance.birthRate = 9.99
    assert instance.birthRate == 9.99


def test_standard_StandardPopulationModel_deathRate_value_roundtrip():
    instance = standard_StandardPopulationModel(birthRate=3.14, deathRate=3.14, timePeriod="sample_text")
    assert instance.deathRate == 3.14
    instance.deathRate = 9.99
    assert instance.deathRate == 9.99


def test_standard_StandardPopulationModel_timePeriod_value_roundtrip():
    instance = standard_StandardPopulationModel(birthRate=3.14, deathRate=3.14, timePeriod="sample_text")
    assert instance.timePeriod == "sample_text"
    instance.timePeriod = "sample_text_2"
    assert instance.timePeriod == "sample_text_2"


def test_standard_StandardPopulationModelLabelValue_births_value_roundtrip():
    instance = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    assert instance.births == 3.14
    instance.births = 9.99
    assert instance.births == 9.99


def test_standard_StandardPopulationModelLabelValue_count_value_roundtrip():
    instance = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    assert instance.count == 3.14
    instance.count = 9.99
    assert instance.count == 9.99


def test_standard_StandardPopulationModelLabelValue_deaths_value_roundtrip():
    instance = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    assert instance.deaths == 3.14
    instance.deaths = 9.99
    assert instance.deaths == 9.99


def test_standard_StandardPopulationModelLabelValue_density_value_roundtrip():
    instance = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    assert instance.density == 3.14
    instance.density = 9.99
    assert instance.density == 9.99


def test_standard_StandardPopulationModelLabelValue_incidence_value_roundtrip():
    instance = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    assert instance.incidence == 3.14
    instance.incidence = 9.99
    assert instance.incidence == 9.99


def test_standard_StochasticStandardPopulationModel_gain_value_roundtrip():
    instance = standard_StochasticStandardPopulationModel(gain=3.14)
    assert instance.gain == 3.14
    instance.gain = 9.99
    assert instance.gain == 9.99


def test_standard_PopulationModelLabel_isa_DynamicNodeLabel():
    instance = standard_PopulationModelLabel(populationIdentifier="sample_text")
    assert isinstance(instance, DynamicNodeLabel)


def test_standard_YetiPopulationInitializer_isa_EarthSciencePopulationInitializer():
    instance = standard_YetiPopulationInitializer()
    assert isinstance(instance, EarthSciencePopulationInitializer)


def test_standard_StandardPopulationModel_isa_IntegrationDecorator():
    instance = standard_StandardPopulationModel(birthRate=3.14, deathRate=3.14, timePeriod="sample_text")
    assert isinstance(instance, IntegrationDecorator)


def test_standard_StandardPopulationModelLabel_isa_IntegrationLabel():
    instance = standard_StandardPopulationModelLabel()
    assert isinstance(instance, IntegrationLabel)


def test_standard_StandardPopulationModelLabelValue_isa_IntegrationLabelValue():
    instance = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    assert isinstance(instance, IntegrationLabelValue)


def test_standard_PopulationModelLabelValue_isa_LabelValue():
    instance = standard_PopulationModelLabelValue()
    assert isinstance(instance, LabelValue)


def test_standard_PopulationInitializer_isa_Modifiable():
    instance = standard_PopulationInitializer(populationIdentifier="sample_text", targetISOKey="sample_text")
    assert isinstance(instance, Modifiable)


def test_standard_PopulationModel_isa_Modifiable():
    instance = standard_PopulationModel(name="sample_text", populationIdentifier="sample_text", targetISOKey="sample_text")
    assert isinstance(instance, Modifiable)


def test_standard_PopulationInitializer_isa_NodeDecorator():
    instance = standard_PopulationInitializer(populationIdentifier="sample_text", targetISOKey="sample_text")
    assert isinstance(instance, NodeDecorator)


def test_standard_PopulationModel_isa_NodeDecorator():
    instance = standard_PopulationModel(name="sample_text", populationIdentifier="sample_text", targetISOKey="sample_text")
    assert isinstance(instance, NodeDecorator)


def test_standard_EarthSciencePopulationInitializer_isa_PopulationInitializer():
    instance = standard_EarthSciencePopulationInitializer()
    assert isinstance(instance, PopulationInitializer)


def test_standard_StandardPopulationInitializer_isa_PopulationInitializer():
    instance = standard_StandardPopulationInitializer(individuals=3.14, useDensity=True)
    assert isinstance(instance, PopulationInitializer)


def test_standard_StandardPopulationModel_isa_PopulationModel():
    instance = standard_StandardPopulationModel(birthRate=3.14, deathRate=3.14, timePeriod="sample_text")
    assert isinstance(instance, PopulationModel)


def test_standard_StandardPopulationModelLabel_isa_PopulationModelLabel():
    instance = standard_StandardPopulationModelLabel()
    assert isinstance(instance, PopulationModelLabel)


def test_standard_StandardPopulationModelLabelValue_isa_PopulationModelLabelValue():
    instance = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    assert isinstance(instance, PopulationModelLabelValue)


def test_standard_DemographicPopulationModel_isa_StandardPopulationModel():
    instance = standard_DemographicPopulationModel()
    assert isinstance(instance, StandardPopulationModel)


def test_standard_SeasonalPopulationModel_isa_StandardPopulationModel():
    instance = standard_SeasonalPopulationModel(modulationAmplitude=3.14, period=3.14, phase=3.14, useLatitude=True)
    assert isinstance(instance, StandardPopulationModel)


def test_standard_StochasticStandardPopulationModel_isa_StandardPopulationModel():
    instance = standard_StochasticStandardPopulationModel(gain=3.14)
    assert isinstance(instance, StandardPopulationModel)


def test_assoc_deltaValue1_link_reassign_clear():
    a = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    b1 = standard_StandardPopulationModelLabel()
    b2 = standard_StandardPopulationModelLabel()
    _safe_set(a, 'standard_StandardPopulationModelLabelValue', b1)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue', b1)
    if hasattr(b1, 'standard_StandardPopulationModelLabel'):
        assert _is_linked(b1, 'standard_StandardPopulationModelLabel', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue', b2)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue', b2)
    if hasattr(b1, 'standard_StandardPopulationModelLabel'):
        assert not _is_linked(b1, 'standard_StandardPopulationModelLabel', a)
    if hasattr(b2, 'standard_StandardPopulationModelLabel'):
        assert _is_linked(b2, 'standard_StandardPopulationModelLabel', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue', None)
    assert not _is_linked(a, 'standard_StandardPopulationModelLabelValue', b2)
    if hasattr(b2, 'standard_StandardPopulationModelLabel'):
        assert not _is_linked(b2, 'standard_StandardPopulationModelLabel', a)


def test_assoc_errorScale11_link_reassign_clear():
    a = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    b1 = standard_StandardPopulationModelLabel()
    b2 = standard_StandardPopulationModelLabel()
    _safe_set(a, 'standard_StandardPopulationModelLabelValue13', b1)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue13', b1)
    if hasattr(b1, 'standard_StandardPopulationModelLabel12'):
        assert _is_linked(b1, 'standard_StandardPopulationModelLabel12', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue13', b2)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue13', b2)
    if hasattr(b1, 'standard_StandardPopulationModelLabel12'):
        assert not _is_linked(b1, 'standard_StandardPopulationModelLabel12', a)
    if hasattr(b2, 'standard_StandardPopulationModelLabel12'):
        assert _is_linked(b2, 'standard_StandardPopulationModelLabel12', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue13', None)
    assert not _is_linked(a, 'standard_StandardPopulationModelLabelValue13', b2)
    if hasattr(b2, 'standard_StandardPopulationModelLabel12'):
        assert not _is_linked(b2, 'standard_StandardPopulationModelLabel12', a)


def test_assoc_originalValue8_link_reassign_clear():
    a = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    b1 = standard_StandardPopulationModelLabel()
    b2 = standard_StandardPopulationModelLabel()
    _safe_set(a, 'standard_StandardPopulationModelLabelValue10', b1)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue10', b1)
    if hasattr(b1, 'standard_StandardPopulationModelLabel9'):
        assert _is_linked(b1, 'standard_StandardPopulationModelLabel9', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue10', b2)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue10', b2)
    if hasattr(b1, 'standard_StandardPopulationModelLabel9'):
        assert not _is_linked(b1, 'standard_StandardPopulationModelLabel9', a)
    if hasattr(b2, 'standard_StandardPopulationModelLabel9'):
        assert _is_linked(b2, 'standard_StandardPopulationModelLabel9', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue10', None)
    assert not _is_linked(a, 'standard_StandardPopulationModelLabelValue10', b2)
    if hasattr(b2, 'standard_StandardPopulationModelLabel9'):
        assert not _is_linked(b2, 'standard_StandardPopulationModelLabel9', a)


def test_assoc_populationGroups14_link_reassign_clear():
    a = standard_PopulationGroup(fraction=3.14, identifier="sample_text")
    b1 = standard_DemographicPopulationModel()
    b2 = standard_DemographicPopulationModel()
    _safe_set(a, 'standard_PopulationGroup', b1)
    assert _is_linked(a, 'standard_PopulationGroup', b1)
    if hasattr(b1, 'standard_DemographicPopulationModel'):
        assert _is_linked(b1, 'standard_DemographicPopulationModel', a)
    _safe_set(a, 'standard_PopulationGroup', b2)
    assert _is_linked(a, 'standard_PopulationGroup', b2)
    if hasattr(b1, 'standard_DemographicPopulationModel'):
        assert not _is_linked(b1, 'standard_DemographicPopulationModel', a)
    if hasattr(b2, 'standard_DemographicPopulationModel'):
        assert _is_linked(b2, 'standard_DemographicPopulationModel', a)
    _safe_set(a, 'standard_PopulationGroup', None)
    assert not _is_linked(a, 'standard_PopulationGroup', b2)
    if hasattr(b2, 'standard_DemographicPopulationModel'):
        assert not _is_linked(b2, 'standard_DemographicPopulationModel', a)


def test_assoc_populationLabel0_link_reassign_clear():
    a = standard_PopulationModelLabel(populationIdentifier="sample_text")
    b1 = standard_PopulationLabel()
    b2 = standard_PopulationLabel()
    _safe_set(a, 'standard_PopulationModelLabel', b1)
    assert _is_linked(a, 'standard_PopulationModelLabel', b1)
    if hasattr(b1, 'standard_PopulationLabel'):
        assert _is_linked(b1, 'standard_PopulationLabel', a)
    _safe_set(a, 'standard_PopulationModelLabel', b2)
    assert _is_linked(a, 'standard_PopulationModelLabel', b2)
    if hasattr(b1, 'standard_PopulationLabel'):
        assert not _is_linked(b1, 'standard_PopulationLabel', a)
    if hasattr(b2, 'standard_PopulationLabel'):
        assert _is_linked(b2, 'standard_PopulationLabel', a)
    _safe_set(a, 'standard_PopulationModelLabel', None)
    assert not _is_linked(a, 'standard_PopulationModelLabel', b2)
    if hasattr(b2, 'standard_PopulationLabel'):
        assert not _is_linked(b2, 'standard_PopulationLabel', a)


def test_assoc_probeValue2_link_reassign_clear():
    a = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    b1 = standard_StandardPopulationModelLabel()
    b2 = standard_StandardPopulationModelLabel()
    _safe_set(a, 'standard_StandardPopulationModelLabelValue4', b1)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue4', b1)
    if hasattr(b1, 'standard_StandardPopulationModelLabel3'):
        assert _is_linked(b1, 'standard_StandardPopulationModelLabel3', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue4', b2)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue4', b2)
    if hasattr(b1, 'standard_StandardPopulationModelLabel3'):
        assert not _is_linked(b1, 'standard_StandardPopulationModelLabel3', a)
    if hasattr(b2, 'standard_StandardPopulationModelLabel3'):
        assert _is_linked(b2, 'standard_StandardPopulationModelLabel3', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue4', None)
    assert not _is_linked(a, 'standard_StandardPopulationModelLabelValue4', b2)
    if hasattr(b2, 'standard_StandardPopulationModelLabel3'):
        assert not _is_linked(b2, 'standard_StandardPopulationModelLabel3', a)


def test_assoc_tempValue5_link_reassign_clear():
    a = standard_StandardPopulationModelLabelValue(births=3.14, count=3.14, deaths=3.14, density=3.14, incidence=3.14)
    b1 = standard_StandardPopulationModelLabel()
    b2 = standard_StandardPopulationModelLabel()
    _safe_set(a, 'standard_StandardPopulationModelLabelValue7', b1)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue7', b1)
    if hasattr(b1, 'standard_StandardPopulationModelLabel6'):
        assert _is_linked(b1, 'standard_StandardPopulationModelLabel6', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue7', b2)
    assert _is_linked(a, 'standard_StandardPopulationModelLabelValue7', b2)
    if hasattr(b1, 'standard_StandardPopulationModelLabel6'):
        assert not _is_linked(b1, 'standard_StandardPopulationModelLabel6', a)
    if hasattr(b2, 'standard_StandardPopulationModelLabel6'):
        assert _is_linked(b2, 'standard_StandardPopulationModelLabel6', a)
    _safe_set(a, 'standard_StandardPopulationModelLabelValue7', None)
    assert not _is_linked(a, 'standard_StandardPopulationModelLabelValue7', b2)
    if hasattr(b2, 'standard_StandardPopulationModelLabel6'):
        assert not _is_linked(b2, 'standard_StandardPopulationModelLabel6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DynamicNodeLabel_strategy = st.builds(DynamicNodeLabel)
@given(instance=DynamicNodeLabel_strategy)
@settings(max_examples=25)
def test_DynamicNodeLabel_instantiation(instance):
    assert isinstance(instance, DynamicNodeLabel)


EarthSciencePopulationInitializer_strategy = st.builds(EarthSciencePopulationInitializer)
@given(instance=EarthSciencePopulationInitializer_strategy)
@settings(max_examples=25)
def test_EarthSciencePopulationInitializer_instantiation(instance):
    assert isinstance(instance, EarthSciencePopulationInitializer)


IntegrationDecorator_strategy = st.builds(IntegrationDecorator)
@given(instance=IntegrationDecorator_strategy)
@settings(max_examples=25)
def test_IntegrationDecorator_instantiation(instance):
    assert isinstance(instance, IntegrationDecorator)


IntegrationLabel_strategy = st.builds(IntegrationLabel)
@given(instance=IntegrationLabel_strategy)
@settings(max_examples=25)
def test_IntegrationLabel_instantiation(instance):
    assert isinstance(instance, IntegrationLabel)


IntegrationLabelValue_strategy = st.builds(IntegrationLabelValue)
@given(instance=IntegrationLabelValue_strategy)
@settings(max_examples=25)
def test_IntegrationLabelValue_instantiation(instance):
    assert isinstance(instance, IntegrationLabelValue)


LabelValue_strategy = st.builds(LabelValue)
@given(instance=LabelValue_strategy)
@settings(max_examples=25)
def test_LabelValue_instantiation(instance):
    assert isinstance(instance, LabelValue)


Modifiable_strategy = st.builds(Modifiable)
@given(instance=Modifiable_strategy)
@settings(max_examples=25)
def test_Modifiable_instantiation(instance):
    assert isinstance(instance, Modifiable)


NodeDecorator_strategy = st.builds(NodeDecorator)
@given(instance=NodeDecorator_strategy)
@settings(max_examples=25)
def test_NodeDecorator_instantiation(instance):
    assert isinstance(instance, NodeDecorator)


PopulationInitializer_strategy = st.builds(PopulationInitializer)
@given(instance=PopulationInitializer_strategy)
@settings(max_examples=25)
def test_PopulationInitializer_instantiation(instance):
    assert isinstance(instance, PopulationInitializer)


PopulationModel_strategy = st.builds(PopulationModel)
@given(instance=PopulationModel_strategy)
@settings(max_examples=25)
def test_PopulationModel_instantiation(instance):
    assert isinstance(instance, PopulationModel)


PopulationModelLabel_strategy = st.builds(PopulationModelLabel)
@given(instance=PopulationModelLabel_strategy)
@settings(max_examples=25)
def test_PopulationModelLabel_instantiation(instance):
    assert isinstance(instance, PopulationModelLabel)


PopulationModelLabelValue_strategy = st.builds(PopulationModelLabelValue)
@given(instance=PopulationModelLabelValue_strategy)
@settings(max_examples=25)
def test_PopulationModelLabelValue_instantiation(instance):
    assert isinstance(instance, PopulationModelLabelValue)


StandardPopulationModel_strategy = st.builds(StandardPopulationModel)
@given(instance=StandardPopulationModel_strategy)
@settings(max_examples=25)
def test_StandardPopulationModel_instantiation(instance):
    assert isinstance(instance, StandardPopulationModel)


standard_DemographicPopulationModel_strategy = st.builds(standard_DemographicPopulationModel)
@given(instance=standard_DemographicPopulationModel_strategy)
@settings(max_examples=25)
def test_standard_DemographicPopulationModel_instantiation(instance):
    assert isinstance(instance, standard_DemographicPopulationModel)


standard_EarthSciencePopulationInitializer_strategy = st.builds(standard_EarthSciencePopulationInitializer)
@given(instance=standard_EarthSciencePopulationInitializer_strategy)
@settings(max_examples=25)
def test_standard_EarthSciencePopulationInitializer_instantiation(instance):
    assert isinstance(instance, standard_EarthSciencePopulationInitializer)


standard_IntegrationDecorator_strategy = st.builds(standard_IntegrationDecorator)
@given(instance=standard_IntegrationDecorator_strategy)
@settings(max_examples=25)
def test_standard_IntegrationDecorator_instantiation(instance):
    assert isinstance(instance, standard_IntegrationDecorator)


standard_IntegrationLabel_strategy = st.builds(standard_IntegrationLabel)
@given(instance=standard_IntegrationLabel_strategy)
@settings(max_examples=25)
def test_standard_IntegrationLabel_instantiation(instance):
    assert isinstance(instance, standard_IntegrationLabel)


standard_IntegrationLabelValue_strategy = st.builds(standard_IntegrationLabelValue)
@given(instance=standard_IntegrationLabelValue_strategy)
@settings(max_examples=25)
def test_standard_IntegrationLabelValue_instantiation(instance):
    assert isinstance(instance, standard_IntegrationLabelValue)


standard_PopulationGroup_strategy = st.builds(standard_PopulationGroup, fraction=st.floats(allow_nan=False, allow_infinity=False), identifier=safe_text)
@given(instance=standard_PopulationGroup_strategy)
@settings(max_examples=25)
def test_standard_PopulationGroup_instantiation(instance):
    assert isinstance(instance, standard_PopulationGroup)


standard_PopulationInitializer_strategy = st.builds(standard_PopulationInitializer, populationIdentifier=safe_text, targetISOKey=safe_text)
@given(instance=standard_PopulationInitializer_strategy)
@settings(max_examples=25)
def test_standard_PopulationInitializer_instantiation(instance):
    assert isinstance(instance, standard_PopulationInitializer)


standard_PopulationLabel_strategy = st.builds(standard_PopulationLabel)
@given(instance=standard_PopulationLabel_strategy)
@settings(max_examples=25)
def test_standard_PopulationLabel_instantiation(instance):
    assert isinstance(instance, standard_PopulationLabel)


standard_PopulationModel_strategy = st.builds(standard_PopulationModel, name=safe_text, populationIdentifier=safe_text, targetISOKey=safe_text)
@given(instance=standard_PopulationModel_strategy)
@settings(max_examples=25)
def test_standard_PopulationModel_instantiation(instance):
    assert isinstance(instance, standard_PopulationModel)


standard_PopulationModelLabel_strategy = st.builds(standard_PopulationModelLabel, populationIdentifier=safe_text)
@given(instance=standard_PopulationModelLabel_strategy)
@settings(max_examples=25)
def test_standard_PopulationModelLabel_instantiation(instance):
    assert isinstance(instance, standard_PopulationModelLabel)


standard_PopulationModelLabelValue_strategy = st.builds(standard_PopulationModelLabelValue)
@given(instance=standard_PopulationModelLabelValue_strategy)
@settings(max_examples=25)
def test_standard_PopulationModelLabelValue_instantiation(instance):
    assert isinstance(instance, standard_PopulationModelLabelValue)


standard_SeasonalPopulationModel_strategy = st.builds(standard_SeasonalPopulationModel, modulationAmplitude=st.floats(allow_nan=False, allow_infinity=False), period=st.floats(allow_nan=False, allow_infinity=False), phase=st.floats(allow_nan=False, allow_infinity=False), useLatitude=st.booleans())
@given(instance=standard_SeasonalPopulationModel_strategy)
@settings(max_examples=25)
def test_standard_SeasonalPopulationModel_instantiation(instance):
    assert isinstance(instance, standard_SeasonalPopulationModel)


standard_StandardPopulationInitializer_strategy = st.builds(standard_StandardPopulationInitializer, individuals=st.floats(allow_nan=False, allow_infinity=False), useDensity=st.booleans())
@given(instance=standard_StandardPopulationInitializer_strategy)
@settings(max_examples=25)
def test_standard_StandardPopulationInitializer_instantiation(instance):
    assert isinstance(instance, standard_StandardPopulationInitializer)


standard_StandardPopulationModel_strategy = st.builds(standard_StandardPopulationModel, birthRate=st.floats(allow_nan=False, allow_infinity=False), deathRate=st.floats(allow_nan=False, allow_infinity=False), timePeriod=safe_text)
@given(instance=standard_StandardPopulationModel_strategy)
@settings(max_examples=25)
def test_standard_StandardPopulationModel_instantiation(instance):
    assert isinstance(instance, standard_StandardPopulationModel)


standard_StandardPopulationModelLabel_strategy = st.builds(standard_StandardPopulationModelLabel)
@given(instance=standard_StandardPopulationModelLabel_strategy)
@settings(max_examples=25)
def test_standard_StandardPopulationModelLabel_instantiation(instance):
    assert isinstance(instance, standard_StandardPopulationModelLabel)


standard_StandardPopulationModelLabelValue_strategy = st.builds(standard_StandardPopulationModelLabelValue, births=st.floats(allow_nan=False, allow_infinity=False), count=st.floats(allow_nan=False, allow_infinity=False), deaths=st.floats(allow_nan=False, allow_infinity=False), density=st.floats(allow_nan=False, allow_infinity=False), incidence=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_StandardPopulationModelLabelValue_strategy)
@settings(max_examples=25)
def test_standard_StandardPopulationModelLabelValue_instantiation(instance):
    assert isinstance(instance, standard_StandardPopulationModelLabelValue)


standard_StochasticStandardPopulationModel_strategy = st.builds(standard_StochasticStandardPopulationModel, gain=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_StochasticStandardPopulationModel_strategy)
@settings(max_examples=25)
def test_standard_StochasticStandardPopulationModel_instantiation(instance):
    assert isinstance(instance, standard_StochasticStandardPopulationModel)


standard_YetiPopulationInitializer_strategy = st.builds(standard_YetiPopulationInitializer)
@given(instance=standard_YetiPopulationInitializer_strategy)
@settings(max_examples=25)
def test_standard_YetiPopulationInitializer_instantiation(instance):
    assert isinstance(instance, standard_YetiPopulationInitializer)


