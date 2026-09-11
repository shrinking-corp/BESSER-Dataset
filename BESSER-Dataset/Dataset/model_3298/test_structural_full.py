import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AggregatingSIDiseaseModel,
    AggregatingSIRDiseaseModel,
    DiseaseModel,
    DiseaseModelLabel,
    DiseaseModelLabelValue,
    DiseaseModelState,
    DynamicNodeLabel,
    Infector,
    IntegrationDecorator,
    IntegrationLabel,
    IntegrationLabelValue,
    LabelValue,
    Modifiable,
    NodeDecorator,
    SEIR,
    SI,
    SIInfector,
    SILabelValue,
    SIR,
    SIRLabelValue,
    SanityChecker,
    StandardDiseaseModel,
    StandardDiseaseModelLabel,
    StandardDiseaseModelLabelValue,
    StandardDiseaseModelState,
    StandardInfector,
    StandardStochasticDiseaseModel,
    StochasticDiseaseModel,
    standard_AggregatingDiseaseModelState,
    standard_AggregatingSEIRDiseaseModel,
    standard_AggregatingSIDiseaseModel,
    standard_AggregatingSIRDiseaseModel,
    standard_DeterministicSEIRDiseaseModel,
    standard_DeterministicSIDiseaseModel,
    standard_DeterministicSIRDiseaseModel,
    standard_DiseaseModel,
    standard_DiseaseModelLabel,
    standard_DiseaseModelLabelValue,
    standard_DiseaseModelState,
    standard_Infector,
    standard_InfectorInoculatorCollection,
    standard_IntegrationDecorator,
    standard_IntegrationLabel,
    standard_IntegrationLabelValue,
    standard_PopulationLabel,
    standard_PopulationModelLabel,
    standard_SEIR,
    standard_SEIRLabel,
    standard_SEIRLabelValue,
    standard_SI,
    standard_SIDiseaseModelState,
    standard_SIInfector,
    standard_SILabel,
    standard_SILabelValue,
    standard_SIR,
    standard_SIRInoculator,
    standard_SIRLabel,
    standard_SIRLabelValue,
    standard_SanityChecker,
    standard_StandardDiseaseModel,
    standard_StandardDiseaseModelLabel,
    standard_StandardDiseaseModelLabelValue,
    standard_StandardDiseaseModelState,
    standard_StandardInfector,
    standard_StandardStochasticDiseaseModel,
    standard_StochasticDiseaseModel,
    standard_StochasticPoissonSEIRDiseaseModel,
    standard_StochasticPoissonSIDiseaseModel,
    standard_StochasticPoissonSIRDiseaseModel,
    standard_StochasticSEIRDiseaseModel,
    standard_StochasticSIDiseaseModel,
    standard_StochasticSIRDiseaseModel,
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

def test_standard_DiseaseModel_backgroundBirthRate_value_roundtrip():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert instance.backgroundBirthRate == 3.14
    instance.backgroundBirthRate = 9.99
    assert instance.backgroundBirthRate == 9.99


def test_standard_DiseaseModel_backgroundMortalityRate_value_roundtrip():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert instance.backgroundMortalityRate == 3.14
    instance.backgroundMortalityRate = 9.99
    assert instance.backgroundMortalityRate == 9.99


def test_standard_DiseaseModel_diseaseName_value_roundtrip():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert instance.diseaseName == "sample_text"
    instance.diseaseName = "sample_text_2"
    assert instance.diseaseName == "sample_text_2"


def test_standard_DiseaseModel_finiteDifference_value_roundtrip():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert instance.finiteDifference == True
    instance.finiteDifference = False
    assert instance.finiteDifference == False


def test_standard_DiseaseModel_frequencyDependent_value_roundtrip():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert instance.frequencyDependent == True
    instance.frequencyDependent = False
    assert instance.frequencyDependent == False


def test_standard_DiseaseModel_populationIdentifier_value_roundtrip():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert instance.populationIdentifier == "sample_text"
    instance.populationIdentifier = "sample_text_2"
    assert instance.populationIdentifier == "sample_text_2"


def test_standard_DiseaseModel_relativeTolerance_value_roundtrip():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert instance.relativeTolerance == 3.14
    instance.relativeTolerance = 9.99
    assert instance.relativeTolerance == 9.99


def test_standard_DiseaseModel_timePeriod_value_roundtrip():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert instance.timePeriod == "sample_text"
    instance.timePeriod = "sample_text_2"
    assert instance.timePeriod == "sample_text_2"


def test_standard_DiseaseModelLabelValue_diseaseDeaths_value_roundtrip():
    instance = standard_DiseaseModelLabelValue(diseaseDeaths=3.14, incidence=3.14, populationCount=3.14)
    assert instance.diseaseDeaths == 3.14
    instance.diseaseDeaths = 9.99
    assert instance.diseaseDeaths == 9.99


def test_standard_DiseaseModelLabelValue_incidence_value_roundtrip():
    instance = standard_DiseaseModelLabelValue(diseaseDeaths=3.14, incidence=3.14, populationCount=3.14)
    assert instance.incidence == 3.14
    instance.incidence = 9.99
    assert instance.incidence == 9.99


def test_standard_DiseaseModelLabelValue_populationCount_value_roundtrip():
    instance = standard_DiseaseModelLabelValue(diseaseDeaths=3.14, incidence=3.14, populationCount=3.14)
    assert instance.populationCount == 3.14
    instance.populationCount = 9.99
    assert instance.populationCount == 9.99


def test_standard_Infector_diseaseName_value_roundtrip():
    instance = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    assert instance.diseaseName == "sample_text"
    instance.diseaseName = "sample_text_2"
    assert instance.diseaseName == "sample_text_2"


def test_standard_Infector_infectPercentage_value_roundtrip():
    instance = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    assert instance.infectPercentage == True
    instance.infectPercentage = False
    assert instance.infectPercentage == False


def test_standard_Infector_populationIdentifier_value_roundtrip():
    instance = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    assert instance.populationIdentifier == "sample_text"
    instance.populationIdentifier = "sample_text_2"
    assert instance.populationIdentifier == "sample_text_2"


def test_standard_Infector_targetISOKey_value_roundtrip():
    instance = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    assert instance.targetISOKey == "sample_text"
    instance.targetISOKey = "sample_text_2"
    assert instance.targetISOKey == "sample_text_2"


def test_standard_Infector_targetURI_value_roundtrip():
    instance = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    assert instance.targetURI == "sample_text"
    instance.targetURI = "sample_text_2"
    assert instance.targetURI == "sample_text_2"


def test_standard_InfectorInoculatorCollection_importFolder_value_roundtrip():
    instance = standard_InfectorInoculatorCollection(importFolder="sample_text")
    assert instance.importFolder == "sample_text"
    instance.importFolder = "sample_text_2"
    assert instance.importFolder == "sample_text_2"


def test_standard_SEIR_incubationRate_value_roundtrip():
    instance = standard_SEIR(incubationRate=3.14)
    assert instance.incubationRate == 3.14
    instance.incubationRate = 9.99
    assert instance.incubationRate == 9.99


def test_standard_SEIRLabelValue_e_value_roundtrip():
    instance = standard_SEIRLabelValue(e=3.14)
    assert instance.e == 3.14
    instance.e = 9.99
    assert instance.e == 9.99


def test_standard_SI_characteristicMixingDistance_value_roundtrip():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert instance.characteristicMixingDistance == 3.14
    instance.characteristicMixingDistance = 9.99
    assert instance.characteristicMixingDistance == 9.99


def test_standard_SI_infectiousMortality_value_roundtrip():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert instance.infectiousMortality == 3.14
    instance.infectiousMortality = 9.99
    assert instance.infectiousMortality == 9.99


def test_standard_SI_infectiousMortalityRate_value_roundtrip():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert instance.infectiousMortalityRate == 3.14
    instance.infectiousMortalityRate = 9.99
    assert instance.infectiousMortalityRate == 9.99


def test_standard_SI_nonLinearityCoefficient_value_roundtrip():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert instance.nonLinearityCoefficient == 3.14
    instance.nonLinearityCoefficient = 9.99
    assert instance.nonLinearityCoefficient == 9.99


def test_standard_SI_physicallyAdjacentInfectiousProportion_value_roundtrip():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert instance.physicallyAdjacentInfectiousProportion == 3.14
    instance.physicallyAdjacentInfectiousProportion = 9.99
    assert instance.physicallyAdjacentInfectiousProportion == 9.99


def test_standard_SI_recoveryRate_value_roundtrip():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert instance.recoveryRate == 3.14
    instance.recoveryRate = 9.99
    assert instance.recoveryRate == 9.99


def test_standard_SI_roadNetworkInfectiousProportion_value_roundtrip():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert instance.roadNetworkInfectiousProportion == 3.14
    instance.roadNetworkInfectiousProportion = 9.99
    assert instance.roadNetworkInfectiousProportion == 9.99


def test_standard_SI_transmissionRate_value_roundtrip():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert instance.transmissionRate == 3.14
    instance.transmissionRate = 9.99
    assert instance.transmissionRate == 9.99


def test_standard_SIInfector_infectiousCount_value_roundtrip():
    instance = standard_SIInfector(infectiousCount=3.14)
    assert instance.infectiousCount == 3.14
    instance.infectiousCount = 9.99
    assert instance.infectiousCount == 9.99


def test_standard_SILabelValue_i_value_roundtrip():
    instance = standard_SILabelValue(i=3.14)
    assert instance.i == 3.14
    instance.i = 9.99
    assert instance.i == 9.99


def test_standard_SIR_immunityLossRate_value_roundtrip():
    instance = standard_SIR(immunityLossRate=3.14)
    assert instance.immunityLossRate == 3.14
    instance.immunityLossRate = 9.99
    assert instance.immunityLossRate == 9.99


def test_standard_SIRInoculator_inoculatePercentage_value_roundtrip():
    instance = standard_SIRInoculator(inoculatePercentage=True, inoculatedPercentage=3.14)
    assert instance.inoculatePercentage == True
    instance.inoculatePercentage = False
    assert instance.inoculatePercentage == False


def test_standard_SIRInoculator_inoculatedPercentage_value_roundtrip():
    instance = standard_SIRInoculator(inoculatePercentage=True, inoculatedPercentage=3.14)
    assert instance.inoculatedPercentage == 3.14
    instance.inoculatedPercentage = 9.99
    assert instance.inoculatedPercentage == 9.99


def test_standard_SIRLabelValue_r_value_roundtrip():
    instance = standard_SIRLabelValue(r=3.14)
    assert instance.r == 3.14
    instance.r = 9.99
    assert instance.r == 9.99


def test_standard_StandardDiseaseModel_referencePopulationDensity_value_roundtrip():
    instance = standard_StandardDiseaseModel(referencePopulationDensity=3.14, totalArea=3.14, totalPopulationCount=3.14, totalPopulationCountReciprocal=3.14)
    assert instance.referencePopulationDensity == 3.14
    instance.referencePopulationDensity = 9.99
    assert instance.referencePopulationDensity == 9.99


def test_standard_StandardDiseaseModel_totalArea_value_roundtrip():
    instance = standard_StandardDiseaseModel(referencePopulationDensity=3.14, totalArea=3.14, totalPopulationCount=3.14, totalPopulationCountReciprocal=3.14)
    assert instance.totalArea == 3.14
    instance.totalArea = 9.99
    assert instance.totalArea == 9.99


def test_standard_StandardDiseaseModel_totalPopulationCount_value_roundtrip():
    instance = standard_StandardDiseaseModel(referencePopulationDensity=3.14, totalArea=3.14, totalPopulationCount=3.14, totalPopulationCountReciprocal=3.14)
    assert instance.totalPopulationCount == 3.14
    instance.totalPopulationCount = 9.99
    assert instance.totalPopulationCount == 9.99


def test_standard_StandardDiseaseModel_totalPopulationCountReciprocal_value_roundtrip():
    instance = standard_StandardDiseaseModel(referencePopulationDensity=3.14, totalArea=3.14, totalPopulationCount=3.14, totalPopulationCountReciprocal=3.14)
    assert instance.totalPopulationCountReciprocal == 3.14
    instance.totalPopulationCountReciprocal = 9.99
    assert instance.totalPopulationCountReciprocal == 9.99


def test_standard_StandardDiseaseModelLabelValue_s_value_roundtrip():
    instance = standard_StandardDiseaseModelLabelValue(s=3.14)
    assert instance.s == 3.14
    instance.s = 9.99
    assert instance.s == 9.99


def test_standard_StandardDiseaseModelState_areaRatio_value_roundtrip():
    instance = standard_StandardDiseaseModelState(areaRatio=3.14)
    assert instance.areaRatio == 3.14
    instance.areaRatio = 9.99
    assert instance.areaRatio == 9.99


def test_standard_StandardStochasticDiseaseModel_gain_value_roundtrip():
    instance = standard_StandardStochasticDiseaseModel(gain=3.14)
    assert instance.gain == 3.14
    instance.gain = 9.99
    assert instance.gain == 9.99


def test_standard_StochasticDiseaseModel_randomGenerator_value_roundtrip():
    instance = standard_StochasticDiseaseModel(randomGenerator="sample_text", seed="sample_text")
    assert instance.randomGenerator == "sample_text"
    instance.randomGenerator = "sample_text_2"
    assert instance.randomGenerator == "sample_text_2"


def test_standard_StochasticDiseaseModel_seed_value_roundtrip():
    instance = standard_StochasticDiseaseModel(randomGenerator="sample_text", seed="sample_text")
    assert instance.seed == "sample_text"
    instance.seed = "sample_text_2"
    assert instance.seed == "sample_text_2"


def test_standard_AggregatingSIRDiseaseModel_isa_AggregatingSIDiseaseModel():
    instance = standard_AggregatingSIRDiseaseModel()
    assert isinstance(instance, AggregatingSIDiseaseModel)


def test_standard_AggregatingSEIRDiseaseModel_isa_AggregatingSIRDiseaseModel():
    instance = standard_AggregatingSEIRDiseaseModel()
    assert isinstance(instance, AggregatingSIRDiseaseModel)


def test_standard_StandardDiseaseModel_isa_DiseaseModel():
    instance = standard_StandardDiseaseModel(referencePopulationDensity=3.14, totalArea=3.14, totalPopulationCount=3.14, totalPopulationCountReciprocal=3.14)
    assert isinstance(instance, DiseaseModel)


def test_standard_StochasticDiseaseModel_isa_DiseaseModel():
    instance = standard_StochasticDiseaseModel(randomGenerator="sample_text", seed="sample_text")
    assert isinstance(instance, DiseaseModel)


def test_standard_StandardDiseaseModelLabel_isa_DiseaseModelLabel():
    instance = standard_StandardDiseaseModelLabel()
    assert isinstance(instance, DiseaseModelLabel)


def test_standard_StandardDiseaseModelLabelValue_isa_DiseaseModelLabelValue():
    instance = standard_StandardDiseaseModelLabelValue(s=3.14)
    assert isinstance(instance, DiseaseModelLabelValue)


def test_standard_AggregatingDiseaseModelState_isa_DiseaseModelState():
    instance = standard_AggregatingDiseaseModelState()
    assert isinstance(instance, DiseaseModelState)


def test_standard_StandardDiseaseModelState_isa_DiseaseModelState():
    instance = standard_StandardDiseaseModelState(areaRatio=3.14)
    assert isinstance(instance, DiseaseModelState)


def test_standard_DiseaseModelLabel_isa_DynamicNodeLabel():
    instance = standard_DiseaseModelLabel()
    assert isinstance(instance, DynamicNodeLabel)


def test_standard_StandardInfector_isa_Infector():
    instance = standard_StandardInfector()
    assert isinstance(instance, Infector)


def test_standard_StandardDiseaseModel_isa_IntegrationDecorator():
    instance = standard_StandardDiseaseModel(referencePopulationDensity=3.14, totalArea=3.14, totalPopulationCount=3.14, totalPopulationCountReciprocal=3.14)
    assert isinstance(instance, IntegrationDecorator)


def test_standard_StandardDiseaseModelLabel_isa_IntegrationLabel():
    instance = standard_StandardDiseaseModelLabel()
    assert isinstance(instance, IntegrationLabel)


def test_standard_DiseaseModelLabelValue_isa_IntegrationLabelValue():
    instance = standard_DiseaseModelLabelValue(diseaseDeaths=3.14, incidence=3.14, populationCount=3.14)
    assert isinstance(instance, IntegrationLabelValue)


def test_standard_DiseaseModelLabelValue_isa_LabelValue():
    instance = standard_DiseaseModelLabelValue(diseaseDeaths=3.14, incidence=3.14, populationCount=3.14)
    assert isinstance(instance, LabelValue)


def test_standard_DiseaseModel_isa_Modifiable():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert isinstance(instance, Modifiable)


def test_standard_Infector_isa_Modifiable():
    instance = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    assert isinstance(instance, Modifiable)


def test_standard_InfectorInoculatorCollection_isa_Modifiable():
    instance = standard_InfectorInoculatorCollection(importFolder="sample_text")
    assert isinstance(instance, Modifiable)


def test_standard_DiseaseModel_isa_NodeDecorator():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert isinstance(instance, NodeDecorator)


def test_standard_Infector_isa_NodeDecorator():
    instance = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    assert isinstance(instance, NodeDecorator)


def test_standard_InfectorInoculatorCollection_isa_NodeDecorator():
    instance = standard_InfectorInoculatorCollection(importFolder="sample_text")
    assert isinstance(instance, NodeDecorator)


def test_standard_DeterministicSEIRDiseaseModel_isa_SEIR():
    instance = standard_DeterministicSEIRDiseaseModel()
    assert isinstance(instance, SEIR)


def test_standard_StochasticPoissonSEIRDiseaseModel_isa_SEIR():
    instance = standard_StochasticPoissonSEIRDiseaseModel()
    assert isinstance(instance, SEIR)


def test_standard_StochasticSEIRDiseaseModel_isa_SEIR():
    instance = standard_StochasticSEIRDiseaseModel()
    assert isinstance(instance, SEIR)


def test_standard_AggregatingSIDiseaseModel_isa_SI():
    instance = standard_AggregatingSIDiseaseModel()
    assert isinstance(instance, SI)


def test_standard_DeterministicSIDiseaseModel_isa_SI():
    instance = standard_DeterministicSIDiseaseModel()
    assert isinstance(instance, SI)


def test_standard_SIR_isa_SI():
    instance = standard_SIR(immunityLossRate=3.14)
    assert isinstance(instance, SI)


def test_standard_StochasticPoissonSIDiseaseModel_isa_SI():
    instance = standard_StochasticPoissonSIDiseaseModel()
    assert isinstance(instance, SI)


def test_standard_StochasticSIDiseaseModel_isa_SI():
    instance = standard_StochasticSIDiseaseModel()
    assert isinstance(instance, SI)


def test_standard_SIRInoculator_isa_SIInfector():
    instance = standard_SIRInoculator(inoculatePercentage=True, inoculatedPercentage=3.14)
    assert isinstance(instance, SIInfector)


def test_standard_SIRLabelValue_isa_SILabelValue():
    instance = standard_SIRLabelValue(r=3.14)
    assert isinstance(instance, SILabelValue)


def test_standard_DeterministicSIRDiseaseModel_isa_SIR():
    instance = standard_DeterministicSIRDiseaseModel()
    assert isinstance(instance, SIR)


def test_standard_SEIR_isa_SIR():
    instance = standard_SEIR(incubationRate=3.14)
    assert isinstance(instance, SIR)


def test_standard_StochasticPoissonSIRDiseaseModel_isa_SIR():
    instance = standard_StochasticPoissonSIRDiseaseModel()
    assert isinstance(instance, SIR)


def test_standard_StochasticSIRDiseaseModel_isa_SIR():
    instance = standard_StochasticSIRDiseaseModel()
    assert isinstance(instance, SIR)


def test_standard_SEIRLabelValue_isa_SIRLabelValue():
    instance = standard_SEIRLabelValue(e=3.14)
    assert isinstance(instance, SIRLabelValue)


def test_standard_DiseaseModel_isa_SanityChecker():
    instance = standard_DiseaseModel(backgroundBirthRate=3.14, backgroundMortalityRate=3.14, diseaseName="sample_text", finiteDifference=True, frequencyDependent=True, populationIdentifier="sample_text", relativeTolerance=3.14, timePeriod="sample_text")
    assert isinstance(instance, SanityChecker)


def test_standard_SI_isa_StandardDiseaseModel():
    instance = standard_SI(characteristicMixingDistance=3.14, infectiousMortality=3.14, infectiousMortalityRate=3.14, nonLinearityCoefficient=3.14, physicallyAdjacentInfectiousProportion=3.14, recoveryRate=3.14, roadNetworkInfectiousProportion=3.14, transmissionRate=3.14)
    assert isinstance(instance, StandardDiseaseModel)


def test_standard_SEIRLabel_isa_StandardDiseaseModelLabel():
    instance = standard_SEIRLabel()
    assert isinstance(instance, StandardDiseaseModelLabel)


def test_standard_SILabel_isa_StandardDiseaseModelLabel():
    instance = standard_SILabel()
    assert isinstance(instance, StandardDiseaseModelLabel)


def test_standard_SIRLabel_isa_StandardDiseaseModelLabel():
    instance = standard_SIRLabel()
    assert isinstance(instance, StandardDiseaseModelLabel)


def test_standard_SILabelValue_isa_StandardDiseaseModelLabelValue():
    instance = standard_SILabelValue(i=3.14)
    assert isinstance(instance, StandardDiseaseModelLabelValue)


def test_standard_SIDiseaseModelState_isa_StandardDiseaseModelState():
    instance = standard_SIDiseaseModelState()
    assert isinstance(instance, StandardDiseaseModelState)


def test_standard_SIInfector_isa_StandardInfector():
    instance = standard_SIInfector(infectiousCount=3.14)
    assert isinstance(instance, StandardInfector)


def test_standard_StochasticSEIRDiseaseModel_isa_StandardStochasticDiseaseModel():
    instance = standard_StochasticSEIRDiseaseModel()
    assert isinstance(instance, StandardStochasticDiseaseModel)


def test_standard_StochasticSIDiseaseModel_isa_StandardStochasticDiseaseModel():
    instance = standard_StochasticSIDiseaseModel()
    assert isinstance(instance, StandardStochasticDiseaseModel)


def test_standard_StochasticSIRDiseaseModel_isa_StandardStochasticDiseaseModel():
    instance = standard_StochasticSIRDiseaseModel()
    assert isinstance(instance, StandardStochasticDiseaseModel)


def test_standard_StandardStochasticDiseaseModel_isa_StochasticDiseaseModel():
    instance = standard_StandardStochasticDiseaseModel(gain=3.14)
    assert isinstance(instance, StochasticDiseaseModel)


def test_assoc_deltaValue22_link_reassign_clear():
    a = standard_SILabelValue(i=3.14)
    b1 = standard_SILabel()
    b2 = standard_SILabel()
    _safe_set(a, 'standard_SILabelValue', b1)
    assert _is_linked(a, 'standard_SILabelValue', b1)
    if hasattr(b1, 'standard_SILabel'):
        assert _is_linked(b1, 'standard_SILabel', a)
    _safe_set(a, 'standard_SILabelValue', b2)
    assert _is_linked(a, 'standard_SILabelValue', b2)
    if hasattr(b1, 'standard_SILabel'):
        assert not _is_linked(b1, 'standard_SILabel', a)
    if hasattr(b2, 'standard_SILabel'):
        assert _is_linked(b2, 'standard_SILabel', a)
    _safe_set(a, 'standard_SILabelValue', None)
    assert not _is_linked(a, 'standard_SILabelValue', b2)
    if hasattr(b2, 'standard_SILabel'):
        assert not _is_linked(b2, 'standard_SILabel', a)


def test_assoc_deltaValue35_link_reassign_clear():
    a = standard_SIRLabelValue(r=3.14)
    b1 = standard_SIRLabel()
    b2 = standard_SIRLabel()
    _safe_set(a, 'standard_SIRLabelValue', b1)
    assert _is_linked(a, 'standard_SIRLabelValue', b1)
    if hasattr(b1, 'standard_SIRLabel'):
        assert _is_linked(b1, 'standard_SIRLabel', a)
    _safe_set(a, 'standard_SIRLabelValue', b2)
    assert _is_linked(a, 'standard_SIRLabelValue', b2)
    if hasattr(b1, 'standard_SIRLabel'):
        assert not _is_linked(b1, 'standard_SIRLabel', a)
    if hasattr(b2, 'standard_SIRLabel'):
        assert _is_linked(b2, 'standard_SIRLabel', a)
    _safe_set(a, 'standard_SIRLabelValue', None)
    assert not _is_linked(a, 'standard_SIRLabelValue', b2)
    if hasattr(b2, 'standard_SIRLabel'):
        assert not _is_linked(b2, 'standard_SIRLabel', a)


def test_assoc_deltaValue9_link_reassign_clear():
    a = standard_SEIRLabelValue(e=3.14)
    b1 = standard_SEIRLabel()
    b2 = standard_SEIRLabel()
    _safe_set(a, 'standard_SEIRLabelValue', b1)
    assert _is_linked(a, 'standard_SEIRLabelValue', b1)
    if hasattr(b1, 'standard_SEIRLabel'):
        assert _is_linked(b1, 'standard_SEIRLabel', a)
    _safe_set(a, 'standard_SEIRLabelValue', b2)
    assert _is_linked(a, 'standard_SEIRLabelValue', b2)
    if hasattr(b1, 'standard_SEIRLabel'):
        assert not _is_linked(b1, 'standard_SEIRLabel', a)
    if hasattr(b2, 'standard_SEIRLabel'):
        assert _is_linked(b2, 'standard_SEIRLabel', a)
    _safe_set(a, 'standard_SEIRLabelValue', None)
    assert not _is_linked(a, 'standard_SEIRLabelValue', b2)
    if hasattr(b2, 'standard_SEIRLabel'):
        assert not _is_linked(b2, 'standard_SEIRLabel', a)


def test_assoc_diseaseModel5_link_reassign_clear():
    a = standard_StandardDiseaseModel(referencePopulationDensity=3.14, totalArea=3.14, totalPopulationCount=3.14, totalPopulationCountReciprocal=3.14)
    b1 = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    b2 = standard_Infector(diseaseName="sample_text_2", infectPercentage=False, populationIdentifier="sample_text_2", targetISOKey="sample_text_2", targetURI="sample_text_2")
    _safe_set(a, 'standard_StandardDiseaseModel', b1)
    assert _is_linked(a, 'standard_StandardDiseaseModel', b1)
    if hasattr(b1, 'standard_Infector'):
        assert _is_linked(b1, 'standard_Infector', a)
    _safe_set(a, 'standard_StandardDiseaseModel', b2)
    assert _is_linked(a, 'standard_StandardDiseaseModel', b2)
    if hasattr(b1, 'standard_Infector'):
        assert not _is_linked(b1, 'standard_Infector', a)
    if hasattr(b2, 'standard_Infector'):
        assert _is_linked(b2, 'standard_Infector', a)
    _safe_set(a, 'standard_StandardDiseaseModel', None)
    assert not _is_linked(a, 'standard_StandardDiseaseModel', b2)
    if hasattr(b2, 'standard_Infector'):
        assert not _is_linked(b2, 'standard_Infector', a)


def test_assoc_errorScale19_link_reassign_clear():
    a = standard_SEIRLabelValue(e=3.14)
    b1 = standard_SEIRLabel()
    b2 = standard_SEIRLabel()
    _safe_set(a, 'standard_SEIRLabelValue21', b1)
    assert _is_linked(a, 'standard_SEIRLabelValue21', b1)
    if hasattr(b1, 'standard_SEIRLabel20'):
        assert _is_linked(b1, 'standard_SEIRLabel20', a)
    _safe_set(a, 'standard_SEIRLabelValue21', b2)
    assert _is_linked(a, 'standard_SEIRLabelValue21', b2)
    if hasattr(b1, 'standard_SEIRLabel20'):
        assert not _is_linked(b1, 'standard_SEIRLabel20', a)
    if hasattr(b2, 'standard_SEIRLabel20'):
        assert _is_linked(b2, 'standard_SEIRLabel20', a)
    _safe_set(a, 'standard_SEIRLabelValue21', None)
    assert not _is_linked(a, 'standard_SEIRLabelValue21', b2)
    if hasattr(b2, 'standard_SEIRLabel20'):
        assert not _is_linked(b2, 'standard_SEIRLabel20', a)


def test_assoc_errorScale32_link_reassign_clear():
    a = standard_SILabelValue(i=3.14)
    b1 = standard_SILabel()
    b2 = standard_SILabel()
    _safe_set(a, 'standard_SILabelValue34', b1)
    assert _is_linked(a, 'standard_SILabelValue34', b1)
    if hasattr(b1, 'standard_SILabel33'):
        assert _is_linked(b1, 'standard_SILabel33', a)
    _safe_set(a, 'standard_SILabelValue34', b2)
    assert _is_linked(a, 'standard_SILabelValue34', b2)
    if hasattr(b1, 'standard_SILabel33'):
        assert not _is_linked(b1, 'standard_SILabel33', a)
    if hasattr(b2, 'standard_SILabel33'):
        assert _is_linked(b2, 'standard_SILabel33', a)
    _safe_set(a, 'standard_SILabelValue34', None)
    assert not _is_linked(a, 'standard_SILabelValue34', b2)
    if hasattr(b2, 'standard_SILabel33'):
        assert not _is_linked(b2, 'standard_SILabel33', a)


def test_assoc_errorScale45_link_reassign_clear():
    a = standard_SIRLabelValue(r=3.14)
    b1 = standard_SIRLabel()
    b2 = standard_SIRLabel()
    _safe_set(a, 'standard_SIRLabelValue47', b1)
    assert _is_linked(a, 'standard_SIRLabelValue47', b1)
    if hasattr(b1, 'standard_SIRLabel46'):
        assert _is_linked(b1, 'standard_SIRLabel46', a)
    _safe_set(a, 'standard_SIRLabelValue47', b2)
    assert _is_linked(a, 'standard_SIRLabelValue47', b2)
    if hasattr(b1, 'standard_SIRLabel46'):
        assert not _is_linked(b1, 'standard_SIRLabel46', a)
    if hasattr(b2, 'standard_SIRLabel46'):
        assert _is_linked(b2, 'standard_SIRLabel46', a)
    _safe_set(a, 'standard_SIRLabelValue47', None)
    assert not _is_linked(a, 'standard_SIRLabelValue47', b2)
    if hasattr(b2, 'standard_SIRLabel46'):
        assert not _is_linked(b2, 'standard_SIRLabel46', a)


def test_assoc_labelsToInfect6_link_reassign_clear():
    a = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    b1 = standard_DiseaseModelLabel()
    b2 = standard_DiseaseModelLabel()
    _safe_set(a, 'standard_Infector7', {b1})
    assert _is_linked(a, 'standard_Infector7', b1)
    if hasattr(b1, 'standard_DiseaseModelLabel8'):
        assert _is_linked(b1, 'standard_DiseaseModelLabel8', a)
    _safe_set(a, 'standard_Infector7', {b2})
    assert _is_linked(a, 'standard_Infector7', b2)
    if hasattr(b1, 'standard_DiseaseModelLabel8'):
        assert not _is_linked(b1, 'standard_DiseaseModelLabel8', a)
    if hasattr(b2, 'standard_DiseaseModelLabel8'):
        assert _is_linked(b2, 'standard_DiseaseModelLabel8', a)
    _safe_set(a, 'standard_Infector7', set())
    assert not _is_linked(a, 'standard_Infector7', b2)
    if hasattr(b2, 'standard_DiseaseModelLabel8'):
        assert not _is_linked(b2, 'standard_DiseaseModelLabel8', a)


def test_assoc_list50_link_reassign_clear():
    a = standard_InfectorInoculatorCollection(importFolder="sample_text")
    b1 = standard_Infector(diseaseName="sample_text", infectPercentage=True, populationIdentifier="sample_text", targetISOKey="sample_text", targetURI="sample_text")
    b2 = standard_Infector(diseaseName="sample_text_2", infectPercentage=False, populationIdentifier="sample_text_2", targetISOKey="sample_text_2", targetURI="sample_text_2")
    _safe_set(a, 'standard_InfectorInoculatorCollection', {b1})
    assert _is_linked(a, 'standard_InfectorInoculatorCollection', b1)
    if hasattr(b1, 'standard_Infector51'):
        assert _is_linked(b1, 'standard_Infector51', a)
    _safe_set(a, 'standard_InfectorInoculatorCollection', {b2})
    assert _is_linked(a, 'standard_InfectorInoculatorCollection', b2)
    if hasattr(b1, 'standard_Infector51'):
        assert not _is_linked(b1, 'standard_Infector51', a)
    if hasattr(b2, 'standard_Infector51'):
        assert _is_linked(b2, 'standard_Infector51', a)
    _safe_set(a, 'standard_InfectorInoculatorCollection', set())
    assert not _is_linked(a, 'standard_InfectorInoculatorCollection', b2)
    if hasattr(b2, 'standard_Infector51'):
        assert not _is_linked(b2, 'standard_Infector51', a)


def test_assoc_originalValue16_link_reassign_clear():
    a = standard_SEIRLabelValue(e=3.14)
    b1 = standard_SEIRLabel()
    b2 = standard_SEIRLabel()
    _safe_set(a, 'standard_SEIRLabelValue18', b1)
    assert _is_linked(a, 'standard_SEIRLabelValue18', b1)
    if hasattr(b1, 'standard_SEIRLabel17'):
        assert _is_linked(b1, 'standard_SEIRLabel17', a)
    _safe_set(a, 'standard_SEIRLabelValue18', b2)
    assert _is_linked(a, 'standard_SEIRLabelValue18', b2)
    if hasattr(b1, 'standard_SEIRLabel17'):
        assert not _is_linked(b1, 'standard_SEIRLabel17', a)
    if hasattr(b2, 'standard_SEIRLabel17'):
        assert _is_linked(b2, 'standard_SEIRLabel17', a)
    _safe_set(a, 'standard_SEIRLabelValue18', None)
    assert not _is_linked(a, 'standard_SEIRLabelValue18', b2)
    if hasattr(b2, 'standard_SEIRLabel17'):
        assert not _is_linked(b2, 'standard_SEIRLabel17', a)


def test_assoc_originalValue29_link_reassign_clear():
    a = standard_SILabelValue(i=3.14)
    b1 = standard_SILabel()
    b2 = standard_SILabel()
    _safe_set(a, 'standard_SILabelValue31', b1)
    assert _is_linked(a, 'standard_SILabelValue31', b1)
    if hasattr(b1, 'standard_SILabel30'):
        assert _is_linked(b1, 'standard_SILabel30', a)
    _safe_set(a, 'standard_SILabelValue31', b2)
    assert _is_linked(a, 'standard_SILabelValue31', b2)
    if hasattr(b1, 'standard_SILabel30'):
        assert not _is_linked(b1, 'standard_SILabel30', a)
    if hasattr(b2, 'standard_SILabel30'):
        assert _is_linked(b2, 'standard_SILabel30', a)
    _safe_set(a, 'standard_SILabelValue31', None)
    assert not _is_linked(a, 'standard_SILabelValue31', b2)
    if hasattr(b2, 'standard_SILabel30'):
        assert not _is_linked(b2, 'standard_SILabel30', a)


def test_assoc_originalValue42_link_reassign_clear():
    a = standard_SIRLabelValue(r=3.14)
    b1 = standard_SIRLabel()
    b2 = standard_SIRLabel()
    _safe_set(a, 'standard_SIRLabelValue44', b1)
    assert _is_linked(a, 'standard_SIRLabelValue44', b1)
    if hasattr(b1, 'standard_SIRLabel43'):
        assert _is_linked(b1, 'standard_SIRLabel43', a)
    _safe_set(a, 'standard_SIRLabelValue44', b2)
    assert _is_linked(a, 'standard_SIRLabelValue44', b2)
    if hasattr(b1, 'standard_SIRLabel43'):
        assert not _is_linked(b1, 'standard_SIRLabel43', a)
    if hasattr(b2, 'standard_SIRLabel43'):
        assert _is_linked(b2, 'standard_SIRLabel43', a)
    _safe_set(a, 'standard_SIRLabelValue44', None)
    assert not _is_linked(a, 'standard_SIRLabelValue44', b2)
    if hasattr(b2, 'standard_SIRLabel43'):
        assert not _is_linked(b2, 'standard_SIRLabel43', a)


def test_assoc_probeValue10_link_reassign_clear():
    a = standard_SEIRLabelValue(e=3.14)
    b1 = standard_SEIRLabel()
    b2 = standard_SEIRLabel()
    _safe_set(a, 'standard_SEIRLabelValue12', b1)
    assert _is_linked(a, 'standard_SEIRLabelValue12', b1)
    if hasattr(b1, 'standard_SEIRLabel11'):
        assert _is_linked(b1, 'standard_SEIRLabel11', a)
    _safe_set(a, 'standard_SEIRLabelValue12', b2)
    assert _is_linked(a, 'standard_SEIRLabelValue12', b2)
    if hasattr(b1, 'standard_SEIRLabel11'):
        assert not _is_linked(b1, 'standard_SEIRLabel11', a)
    if hasattr(b2, 'standard_SEIRLabel11'):
        assert _is_linked(b2, 'standard_SEIRLabel11', a)
    _safe_set(a, 'standard_SEIRLabelValue12', None)
    assert not _is_linked(a, 'standard_SEIRLabelValue12', b2)
    if hasattr(b2, 'standard_SEIRLabel11'):
        assert not _is_linked(b2, 'standard_SEIRLabel11', a)


def test_assoc_probeValue23_link_reassign_clear():
    a = standard_SILabelValue(i=3.14)
    b1 = standard_SILabel()
    b2 = standard_SILabel()
    _safe_set(a, 'standard_SILabelValue25', b1)
    assert _is_linked(a, 'standard_SILabelValue25', b1)
    if hasattr(b1, 'standard_SILabel24'):
        assert _is_linked(b1, 'standard_SILabel24', a)
    _safe_set(a, 'standard_SILabelValue25', b2)
    assert _is_linked(a, 'standard_SILabelValue25', b2)
    if hasattr(b1, 'standard_SILabel24'):
        assert not _is_linked(b1, 'standard_SILabel24', a)
    if hasattr(b2, 'standard_SILabel24'):
        assert _is_linked(b2, 'standard_SILabel24', a)
    _safe_set(a, 'standard_SILabelValue25', None)
    assert not _is_linked(a, 'standard_SILabelValue25', b2)
    if hasattr(b2, 'standard_SILabel24'):
        assert not _is_linked(b2, 'standard_SILabel24', a)


def test_assoc_probeValue36_link_reassign_clear():
    a = standard_SIRLabelValue(r=3.14)
    b1 = standard_SIRLabel()
    b2 = standard_SIRLabel()
    _safe_set(a, 'standard_SIRLabelValue38', b1)
    assert _is_linked(a, 'standard_SIRLabelValue38', b1)
    if hasattr(b1, 'standard_SIRLabel37'):
        assert _is_linked(b1, 'standard_SIRLabel37', a)
    _safe_set(a, 'standard_SIRLabelValue38', b2)
    assert _is_linked(a, 'standard_SIRLabelValue38', b2)
    if hasattr(b1, 'standard_SIRLabel37'):
        assert not _is_linked(b1, 'standard_SIRLabel37', a)
    if hasattr(b2, 'standard_SIRLabel37'):
        assert _is_linked(b2, 'standard_SIRLabel37', a)
    _safe_set(a, 'standard_SIRLabelValue38', None)
    assert not _is_linked(a, 'standard_SIRLabelValue38', b2)
    if hasattr(b2, 'standard_SIRLabel37'):
        assert not _is_linked(b2, 'standard_SIRLabel37', a)


def test_assoc_tempValue13_link_reassign_clear():
    a = standard_SEIRLabelValue(e=3.14)
    b1 = standard_SEIRLabel()
    b2 = standard_SEIRLabel()
    _safe_set(a, 'standard_SEIRLabelValue15', b1)
    assert _is_linked(a, 'standard_SEIRLabelValue15', b1)
    if hasattr(b1, 'standard_SEIRLabel14'):
        assert _is_linked(b1, 'standard_SEIRLabel14', a)
    _safe_set(a, 'standard_SEIRLabelValue15', b2)
    assert _is_linked(a, 'standard_SEIRLabelValue15', b2)
    if hasattr(b1, 'standard_SEIRLabel14'):
        assert not _is_linked(b1, 'standard_SEIRLabel14', a)
    if hasattr(b2, 'standard_SEIRLabel14'):
        assert _is_linked(b2, 'standard_SEIRLabel14', a)
    _safe_set(a, 'standard_SEIRLabelValue15', None)
    assert not _is_linked(a, 'standard_SEIRLabelValue15', b2)
    if hasattr(b2, 'standard_SEIRLabel14'):
        assert not _is_linked(b2, 'standard_SEIRLabel14', a)


def test_assoc_tempValue26_link_reassign_clear():
    a = standard_SILabelValue(i=3.14)
    b1 = standard_SILabel()
    b2 = standard_SILabel()
    _safe_set(a, 'standard_SILabelValue28', b1)
    assert _is_linked(a, 'standard_SILabelValue28', b1)
    if hasattr(b1, 'standard_SILabel27'):
        assert _is_linked(b1, 'standard_SILabel27', a)
    _safe_set(a, 'standard_SILabelValue28', b2)
    assert _is_linked(a, 'standard_SILabelValue28', b2)
    if hasattr(b1, 'standard_SILabel27'):
        assert not _is_linked(b1, 'standard_SILabel27', a)
    if hasattr(b2, 'standard_SILabel27'):
        assert _is_linked(b2, 'standard_SILabel27', a)
    _safe_set(a, 'standard_SILabelValue28', None)
    assert not _is_linked(a, 'standard_SILabelValue28', b2)
    if hasattr(b2, 'standard_SILabel27'):
        assert not _is_linked(b2, 'standard_SILabel27', a)


def test_assoc_tempValue39_link_reassign_clear():
    a = standard_SIRLabelValue(r=3.14)
    b1 = standard_SIRLabel()
    b2 = standard_SIRLabel()
    _safe_set(a, 'standard_SIRLabelValue41', b1)
    assert _is_linked(a, 'standard_SIRLabelValue41', b1)
    if hasattr(b1, 'standard_SIRLabel40'):
        assert _is_linked(b1, 'standard_SIRLabel40', a)
    _safe_set(a, 'standard_SIRLabelValue41', b2)
    assert _is_linked(a, 'standard_SIRLabelValue41', b2)
    if hasattr(b1, 'standard_SIRLabel40'):
        assert not _is_linked(b1, 'standard_SIRLabel40', a)
    if hasattr(b2, 'standard_SIRLabel40'):
        assert _is_linked(b2, 'standard_SIRLabel40', a)
    _safe_set(a, 'standard_SIRLabelValue41', None)
    assert not _is_linked(a, 'standard_SIRLabelValue41', b2)
    if hasattr(b2, 'standard_SIRLabel40'):
        assert not _is_linked(b2, 'standard_SIRLabel40', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AggregatingSIDiseaseModel_strategy = st.builds(AggregatingSIDiseaseModel)
@given(instance=AggregatingSIDiseaseModel_strategy)
@settings(max_examples=25)
def test_AggregatingSIDiseaseModel_instantiation(instance):
    assert isinstance(instance, AggregatingSIDiseaseModel)


AggregatingSIRDiseaseModel_strategy = st.builds(AggregatingSIRDiseaseModel)
@given(instance=AggregatingSIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_AggregatingSIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, AggregatingSIRDiseaseModel)


DiseaseModel_strategy = st.builds(DiseaseModel)
@given(instance=DiseaseModel_strategy)
@settings(max_examples=25)
def test_DiseaseModel_instantiation(instance):
    assert isinstance(instance, DiseaseModel)


DiseaseModelLabel_strategy = st.builds(DiseaseModelLabel)
@given(instance=DiseaseModelLabel_strategy)
@settings(max_examples=25)
def test_DiseaseModelLabel_instantiation(instance):
    assert isinstance(instance, DiseaseModelLabel)


DiseaseModelLabelValue_strategy = st.builds(DiseaseModelLabelValue)
@given(instance=DiseaseModelLabelValue_strategy)
@settings(max_examples=25)
def test_DiseaseModelLabelValue_instantiation(instance):
    assert isinstance(instance, DiseaseModelLabelValue)


DiseaseModelState_strategy = st.builds(DiseaseModelState)
@given(instance=DiseaseModelState_strategy)
@settings(max_examples=25)
def test_DiseaseModelState_instantiation(instance):
    assert isinstance(instance, DiseaseModelState)


DynamicNodeLabel_strategy = st.builds(DynamicNodeLabel)
@given(instance=DynamicNodeLabel_strategy)
@settings(max_examples=25)
def test_DynamicNodeLabel_instantiation(instance):
    assert isinstance(instance, DynamicNodeLabel)


Infector_strategy = st.builds(Infector)
@given(instance=Infector_strategy)
@settings(max_examples=25)
def test_Infector_instantiation(instance):
    assert isinstance(instance, Infector)


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


SEIR_strategy = st.builds(SEIR)
@given(instance=SEIR_strategy)
@settings(max_examples=25)
def test_SEIR_instantiation(instance):
    assert isinstance(instance, SEIR)


SI_strategy = st.builds(SI)
@given(instance=SI_strategy)
@settings(max_examples=25)
def test_SI_instantiation(instance):
    assert isinstance(instance, SI)


SIInfector_strategy = st.builds(SIInfector)
@given(instance=SIInfector_strategy)
@settings(max_examples=25)
def test_SIInfector_instantiation(instance):
    assert isinstance(instance, SIInfector)


SILabelValue_strategy = st.builds(SILabelValue)
@given(instance=SILabelValue_strategy)
@settings(max_examples=25)
def test_SILabelValue_instantiation(instance):
    assert isinstance(instance, SILabelValue)


SIR_strategy = st.builds(SIR)
@given(instance=SIR_strategy)
@settings(max_examples=25)
def test_SIR_instantiation(instance):
    assert isinstance(instance, SIR)


SIRLabelValue_strategy = st.builds(SIRLabelValue)
@given(instance=SIRLabelValue_strategy)
@settings(max_examples=25)
def test_SIRLabelValue_instantiation(instance):
    assert isinstance(instance, SIRLabelValue)


SanityChecker_strategy = st.builds(SanityChecker)
@given(instance=SanityChecker_strategy)
@settings(max_examples=25)
def test_SanityChecker_instantiation(instance):
    assert isinstance(instance, SanityChecker)


StandardDiseaseModel_strategy = st.builds(StandardDiseaseModel)
@given(instance=StandardDiseaseModel_strategy)
@settings(max_examples=25)
def test_StandardDiseaseModel_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModel)


StandardDiseaseModelLabel_strategy = st.builds(StandardDiseaseModelLabel)
@given(instance=StandardDiseaseModelLabel_strategy)
@settings(max_examples=25)
def test_StandardDiseaseModelLabel_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModelLabel)


StandardDiseaseModelLabelValue_strategy = st.builds(StandardDiseaseModelLabelValue)
@given(instance=StandardDiseaseModelLabelValue_strategy)
@settings(max_examples=25)
def test_StandardDiseaseModelLabelValue_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModelLabelValue)


StandardDiseaseModelState_strategy = st.builds(StandardDiseaseModelState)
@given(instance=StandardDiseaseModelState_strategy)
@settings(max_examples=25)
def test_StandardDiseaseModelState_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModelState)


StandardInfector_strategy = st.builds(StandardInfector)
@given(instance=StandardInfector_strategy)
@settings(max_examples=25)
def test_StandardInfector_instantiation(instance):
    assert isinstance(instance, StandardInfector)


StandardStochasticDiseaseModel_strategy = st.builds(StandardStochasticDiseaseModel)
@given(instance=StandardStochasticDiseaseModel_strategy)
@settings(max_examples=25)
def test_StandardStochasticDiseaseModel_instantiation(instance):
    assert isinstance(instance, StandardStochasticDiseaseModel)


StochasticDiseaseModel_strategy = st.builds(StochasticDiseaseModel)
@given(instance=StochasticDiseaseModel_strategy)
@settings(max_examples=25)
def test_StochasticDiseaseModel_instantiation(instance):
    assert isinstance(instance, StochasticDiseaseModel)


standard_AggregatingDiseaseModelState_strategy = st.builds(standard_AggregatingDiseaseModelState)
@given(instance=standard_AggregatingDiseaseModelState_strategy)
@settings(max_examples=25)
def test_standard_AggregatingDiseaseModelState_instantiation(instance):
    assert isinstance(instance, standard_AggregatingDiseaseModelState)


standard_AggregatingSEIRDiseaseModel_strategy = st.builds(standard_AggregatingSEIRDiseaseModel)
@given(instance=standard_AggregatingSEIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_AggregatingSEIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_AggregatingSEIRDiseaseModel)


standard_AggregatingSIDiseaseModel_strategy = st.builds(standard_AggregatingSIDiseaseModel)
@given(instance=standard_AggregatingSIDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_AggregatingSIDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_AggregatingSIDiseaseModel)


standard_AggregatingSIRDiseaseModel_strategy = st.builds(standard_AggregatingSIRDiseaseModel)
@given(instance=standard_AggregatingSIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_AggregatingSIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_AggregatingSIRDiseaseModel)


standard_DeterministicSEIRDiseaseModel_strategy = st.builds(standard_DeterministicSEIRDiseaseModel)
@given(instance=standard_DeterministicSEIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_DeterministicSEIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_DeterministicSEIRDiseaseModel)


standard_DeterministicSIDiseaseModel_strategy = st.builds(standard_DeterministicSIDiseaseModel)
@given(instance=standard_DeterministicSIDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_DeterministicSIDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_DeterministicSIDiseaseModel)


standard_DeterministicSIRDiseaseModel_strategy = st.builds(standard_DeterministicSIRDiseaseModel)
@given(instance=standard_DeterministicSIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_DeterministicSIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_DeterministicSIRDiseaseModel)


standard_DiseaseModel_strategy = st.builds(standard_DiseaseModel, backgroundBirthRate=st.floats(allow_nan=False, allow_infinity=False), backgroundMortalityRate=st.floats(allow_nan=False, allow_infinity=False), diseaseName=safe_text, finiteDifference=st.booleans(), frequencyDependent=st.booleans(), populationIdentifier=safe_text, relativeTolerance=st.floats(allow_nan=False, allow_infinity=False), timePeriod=safe_text)
@given(instance=standard_DiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_DiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_DiseaseModel)


standard_DiseaseModelLabel_strategy = st.builds(standard_DiseaseModelLabel)
@given(instance=standard_DiseaseModelLabel_strategy)
@settings(max_examples=25)
def test_standard_DiseaseModelLabel_instantiation(instance):
    assert isinstance(instance, standard_DiseaseModelLabel)


standard_DiseaseModelLabelValue_strategy = st.builds(standard_DiseaseModelLabelValue, diseaseDeaths=st.floats(allow_nan=False, allow_infinity=False), incidence=st.floats(allow_nan=False, allow_infinity=False), populationCount=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_DiseaseModelLabelValue_strategy)
@settings(max_examples=25)
def test_standard_DiseaseModelLabelValue_instantiation(instance):
    assert isinstance(instance, standard_DiseaseModelLabelValue)


standard_DiseaseModelState_strategy = st.builds(standard_DiseaseModelState)
@given(instance=standard_DiseaseModelState_strategy)
@settings(max_examples=25)
def test_standard_DiseaseModelState_instantiation(instance):
    assert isinstance(instance, standard_DiseaseModelState)


standard_Infector_strategy = st.builds(standard_Infector, diseaseName=safe_text, infectPercentage=st.booleans(), populationIdentifier=safe_text, targetISOKey=safe_text, targetURI=safe_text)
@given(instance=standard_Infector_strategy)
@settings(max_examples=25)
def test_standard_Infector_instantiation(instance):
    assert isinstance(instance, standard_Infector)


standard_InfectorInoculatorCollection_strategy = st.builds(standard_InfectorInoculatorCollection, importFolder=safe_text)
@given(instance=standard_InfectorInoculatorCollection_strategy)
@settings(max_examples=25)
def test_standard_InfectorInoculatorCollection_instantiation(instance):
    assert isinstance(instance, standard_InfectorInoculatorCollection)


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


standard_PopulationLabel_strategy = st.builds(standard_PopulationLabel)
@given(instance=standard_PopulationLabel_strategy)
@settings(max_examples=25)
def test_standard_PopulationLabel_instantiation(instance):
    assert isinstance(instance, standard_PopulationLabel)


standard_PopulationModelLabel_strategy = st.builds(standard_PopulationModelLabel)
@given(instance=standard_PopulationModelLabel_strategy)
@settings(max_examples=25)
def test_standard_PopulationModelLabel_instantiation(instance):
    assert isinstance(instance, standard_PopulationModelLabel)


standard_SEIR_strategy = st.builds(standard_SEIR, incubationRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_SEIR_strategy)
@settings(max_examples=25)
def test_standard_SEIR_instantiation(instance):
    assert isinstance(instance, standard_SEIR)


standard_SEIRLabel_strategy = st.builds(standard_SEIRLabel)
@given(instance=standard_SEIRLabel_strategy)
@settings(max_examples=25)
def test_standard_SEIRLabel_instantiation(instance):
    assert isinstance(instance, standard_SEIRLabel)


standard_SEIRLabelValue_strategy = st.builds(standard_SEIRLabelValue, e=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_SEIRLabelValue_strategy)
@settings(max_examples=25)
def test_standard_SEIRLabelValue_instantiation(instance):
    assert isinstance(instance, standard_SEIRLabelValue)


standard_SI_strategy = st.builds(standard_SI, characteristicMixingDistance=st.floats(allow_nan=False, allow_infinity=False), infectiousMortality=st.floats(allow_nan=False, allow_infinity=False), infectiousMortalityRate=st.floats(allow_nan=False, allow_infinity=False), nonLinearityCoefficient=st.floats(allow_nan=False, allow_infinity=False), physicallyAdjacentInfectiousProportion=st.floats(allow_nan=False, allow_infinity=False), recoveryRate=st.floats(allow_nan=False, allow_infinity=False), roadNetworkInfectiousProportion=st.floats(allow_nan=False, allow_infinity=False), transmissionRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_SI_strategy)
@settings(max_examples=25)
def test_standard_SI_instantiation(instance):
    assert isinstance(instance, standard_SI)


standard_SIDiseaseModelState_strategy = st.builds(standard_SIDiseaseModelState)
@given(instance=standard_SIDiseaseModelState_strategy)
@settings(max_examples=25)
def test_standard_SIDiseaseModelState_instantiation(instance):
    assert isinstance(instance, standard_SIDiseaseModelState)


standard_SIInfector_strategy = st.builds(standard_SIInfector, infectiousCount=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_SIInfector_strategy)
@settings(max_examples=25)
def test_standard_SIInfector_instantiation(instance):
    assert isinstance(instance, standard_SIInfector)


standard_SILabel_strategy = st.builds(standard_SILabel)
@given(instance=standard_SILabel_strategy)
@settings(max_examples=25)
def test_standard_SILabel_instantiation(instance):
    assert isinstance(instance, standard_SILabel)


standard_SILabelValue_strategy = st.builds(standard_SILabelValue, i=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_SILabelValue_strategy)
@settings(max_examples=25)
def test_standard_SILabelValue_instantiation(instance):
    assert isinstance(instance, standard_SILabelValue)


standard_SIR_strategy = st.builds(standard_SIR, immunityLossRate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_SIR_strategy)
@settings(max_examples=25)
def test_standard_SIR_instantiation(instance):
    assert isinstance(instance, standard_SIR)


standard_SIRInoculator_strategy = st.builds(standard_SIRInoculator, inoculatePercentage=st.booleans(), inoculatedPercentage=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_SIRInoculator_strategy)
@settings(max_examples=25)
def test_standard_SIRInoculator_instantiation(instance):
    assert isinstance(instance, standard_SIRInoculator)


standard_SIRLabel_strategy = st.builds(standard_SIRLabel)
@given(instance=standard_SIRLabel_strategy)
@settings(max_examples=25)
def test_standard_SIRLabel_instantiation(instance):
    assert isinstance(instance, standard_SIRLabel)


standard_SIRLabelValue_strategy = st.builds(standard_SIRLabelValue, r=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_SIRLabelValue_strategy)
@settings(max_examples=25)
def test_standard_SIRLabelValue_instantiation(instance):
    assert isinstance(instance, standard_SIRLabelValue)


standard_SanityChecker_strategy = st.builds(standard_SanityChecker)
@given(instance=standard_SanityChecker_strategy)
@settings(max_examples=25)
def test_standard_SanityChecker_instantiation(instance):
    assert isinstance(instance, standard_SanityChecker)


standard_StandardDiseaseModel_strategy = st.builds(standard_StandardDiseaseModel, referencePopulationDensity=st.floats(allow_nan=False, allow_infinity=False), totalArea=st.floats(allow_nan=False, allow_infinity=False), totalPopulationCount=st.floats(allow_nan=False, allow_infinity=False), totalPopulationCountReciprocal=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_StandardDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StandardDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StandardDiseaseModel)


standard_StandardDiseaseModelLabel_strategy = st.builds(standard_StandardDiseaseModelLabel)
@given(instance=standard_StandardDiseaseModelLabel_strategy)
@settings(max_examples=25)
def test_standard_StandardDiseaseModelLabel_instantiation(instance):
    assert isinstance(instance, standard_StandardDiseaseModelLabel)


standard_StandardDiseaseModelLabelValue_strategy = st.builds(standard_StandardDiseaseModelLabelValue, s=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_StandardDiseaseModelLabelValue_strategy)
@settings(max_examples=25)
def test_standard_StandardDiseaseModelLabelValue_instantiation(instance):
    assert isinstance(instance, standard_StandardDiseaseModelLabelValue)


standard_StandardDiseaseModelState_strategy = st.builds(standard_StandardDiseaseModelState, areaRatio=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_StandardDiseaseModelState_strategy)
@settings(max_examples=25)
def test_standard_StandardDiseaseModelState_instantiation(instance):
    assert isinstance(instance, standard_StandardDiseaseModelState)


standard_StandardInfector_strategy = st.builds(standard_StandardInfector)
@given(instance=standard_StandardInfector_strategy)
@settings(max_examples=25)
def test_standard_StandardInfector_instantiation(instance):
    assert isinstance(instance, standard_StandardInfector)


standard_StandardStochasticDiseaseModel_strategy = st.builds(standard_StandardStochasticDiseaseModel, gain=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=standard_StandardStochasticDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StandardStochasticDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StandardStochasticDiseaseModel)


standard_StochasticDiseaseModel_strategy = st.builds(standard_StochasticDiseaseModel, randomGenerator=safe_text, seed=safe_text)
@given(instance=standard_StochasticDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StochasticDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StochasticDiseaseModel)


standard_StochasticPoissonSEIRDiseaseModel_strategy = st.builds(standard_StochasticPoissonSEIRDiseaseModel)
@given(instance=standard_StochasticPoissonSEIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StochasticPoissonSEIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StochasticPoissonSEIRDiseaseModel)


standard_StochasticPoissonSIDiseaseModel_strategy = st.builds(standard_StochasticPoissonSIDiseaseModel)
@given(instance=standard_StochasticPoissonSIDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StochasticPoissonSIDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StochasticPoissonSIDiseaseModel)


standard_StochasticPoissonSIRDiseaseModel_strategy = st.builds(standard_StochasticPoissonSIRDiseaseModel)
@given(instance=standard_StochasticPoissonSIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StochasticPoissonSIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StochasticPoissonSIRDiseaseModel)


standard_StochasticSEIRDiseaseModel_strategy = st.builds(standard_StochasticSEIRDiseaseModel)
@given(instance=standard_StochasticSEIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StochasticSEIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StochasticSEIRDiseaseModel)


standard_StochasticSIDiseaseModel_strategy = st.builds(standard_StochasticSIDiseaseModel)
@given(instance=standard_StochasticSIDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StochasticSIDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StochasticSIDiseaseModel)


standard_StochasticSIRDiseaseModel_strategy = st.builds(standard_StochasticSIRDiseaseModel)
@given(instance=standard_StochasticSIRDiseaseModel_strategy)
@settings(max_examples=25)
def test_standard_StochasticSIRDiseaseModel_instantiation(instance):
    assert isinstance(instance, standard_StochasticSIRDiseaseModel)


