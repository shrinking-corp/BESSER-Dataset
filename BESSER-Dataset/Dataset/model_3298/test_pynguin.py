#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
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
    abstractmethod,
    date,
    datetime,
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
    time,
)


def test_0():
    var_44 = python_code_.standard_SIRLabelValue(
        r=-5.02,
        standard_SIRLabelValue38=None,
        standard_SIRLabelValue44=None,
        standard_SIRLabelValue47=None,
    )
    assert isinstance(var_44, python_code_.standard_SIRLabelValue)


def test_1():
    var_39 = python_code_.standard_SIRLabel()
    var_40 = python_code_.standard_SIRLabelValue(
        r=-1530.67, standard_SIRLabelValue=var_39, standard_SIRLabelValue38=var_39
    )
    assert isinstance(var_40, python_code_.standard_SIRLabelValue)


def test_2():
    var_1 = lambda *args, **kwargs: False
    var_38 = python_code_.standard_SIRLabelValue(
        r=-1711.35, standard_SIRLabelValue41=var_1
    )
    assert isinstance(var_38, python_code_.standard_SIRLabelValue)


def test_3():
    var_45 = python_code_.standard_SILabelValue(i=-3385.18)
    assert isinstance(var_45, python_code_.standard_SILabelValue)


def test_4():
    var_1 = python_code_.standard_AggregatingSIRDiseaseModel()
    var_43 = python_code_.standard_SILabelValue(
        i=-3352.75, standard_SILabelValue34=var_1
    )
    assert isinstance(var_43, python_code_.standard_SILabelValue)


def test_5():
    var_2 = -692.9596310718761
    var_66 = python_code_.AggregatingSIRDiseaseModel
    var_67 = python_code_.standard_SILabelValue(
        i=var_2, standard_SILabelValue=var_66, standard_SILabelValue34=var_66
    )
    assert isinstance(var_67, python_code_.standard_SILabelValue)


def test_6():
    var_1 = lambda *args, **kwargs: False
    var_2 = python_code_.standard_SEIRLabelValue(
        e=550.36, standard_SEIRLabelValue12=var_1
    )
    assert isinstance(var_2, python_code_.standard_SEIRLabelValue)


def test_7():
    var_0 = 1260.44
    var_1 = lambda *args, **kwargs: False
    var_2 = python_code_.standard_SEIRLabelValue(
        e=var_0, standard_SEIRLabelValue18=var_1
    )
    assert isinstance(var_2, python_code_.standard_SEIRLabelValue)


def test_8():
    var_13 = python_code_.standard_SIDiseaseModelState
    var_15 = python_code_.standard_SEIRLabelValue(
        e=var_13, standard_SEIRLabelValue21=-1149.84
    )
    assert isinstance(var_15, python_code_.standard_SEIRLabelValue)


@pytest.mark.xfail(strict=True)
def test_9():
    var_1 = lambda *args, **kwargs: False
    var_44 = "_standard_SILabelValue__standard_SILabelValue25"
    var_45 = 909.95
    var_46 = bool
    var_47 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=b"/\xa8\x03Hu\xd8\r\xd9D\x8c\x1e\xeb0p\xe9\xb9We",
        totalPopulationCountReciprocal=var_45,
        totalArea=var_45,
        referencePopulationDensity=var_45,
        standard_StandardDiseaseModel=var_46,
    )
    assert isinstance(var_47, python_code_.standard_StandardDiseaseModel)
    python_code_.standard_Infector(
        targetURI=var_1,
        diseaseName=var_1,
        targetISOKey=1173.76,
        populationIdentifier=var_44,
        infectPercentage=var_44,
        standard_Infector=var_47,
        standard_Infector7=True,
    )


def test_10():
    var_2 = -737.04
    var_65 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=None,
        totalPopulationCountReciprocal={},
        totalArea=var_2,
        referencePopulationDensity={"standard_SEIRLabel17": 1},
    )
    assert isinstance(var_65, python_code_.standard_StandardDiseaseModel)
    var_66 = python_code_.AggregatingSIRDiseaseModel
    var_67 = python_code_.standard_SILabelValue(
        i=-613.26, standard_SILabelValue28=None, standard_SILabelValue31=None
    )
    assert isinstance(var_67, python_code_.standard_SILabelValue)
    var_68 = python_code_.SILabelValue()
    var_69 = "standard_SIRLabel,standard_SIRLabel37,standard_SILabel30"
    var_70 = ""
    var_71 = python_code_.standard_Infector(
        targetURI="standard_SILabel33standard_SILabel30",
        diseaseName=var_69,
        targetISOKey=var_69,
        populationIdentifier="_standard_InfectorInoculatorCollection__standard_InfectorInoculatorCollection_standard_StandardDiseaseModel__standard_StandardDiseaseModel",
        infectPercentage=True,
        standard_Infector7={var_66, var_66, True},
        standard_Infector51=var_67,
    )
    assert isinstance(var_71, python_code_.standard_Infector)
    var_74 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths=set(), populationCount=var_68, incidence=var_68
    )
    assert isinstance(var_74, python_code_.standard_DiseaseModelLabelValue)
    var_74.sub(standard_value=var_70)


def test_11():
    var_0 = python_code_.standard_IntegrationLabelValue()
    var_1 = python_code_.standard_DiseaseModelLabel()
    var_2 = python_code_.standard_AggregatingSEIRDiseaseModel
    var_3 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_1,
        totalPopulationCountReciprocal=False,
        totalArea=var_2,
        referencePopulationDensity=var_2,
        standard_StandardDiseaseModel=var_0,
    )
    assert isinstance(var_3, python_code_.standard_StandardDiseaseModel)
    var_8 = python_code_.standard_SEIRLabelValue(
        e=var_2, standard_SEIRLabelValue21=-1149.84
    )
    assert isinstance(var_8, python_code_.standard_SEIRLabelValue)
    var_11 = 4337.83
    var_12 = "_standard_SIRLabelValue__standard_SIRLabelValue38"
    var_13 = True
    var_14 = True
    var_15 = 3284.03
    var_16 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=var_11,
        populationIdentifier=var_12,
        timePeriod=var_12,
        diseaseName=var_11,
        relativeTolerance=var_11,
        finiteDifference=var_13,
        frequencyDependent=var_14,
        backgroundBirthRate=var_15,
    )
    assert isinstance(var_16, python_code_.standard_DiseaseModel)
    var_16.createInfector()


def test_12():
    var_67 = 1550.5
    var_68 = python_code_.standard_StandardStochasticDiseaseModel(gain=var_67)
    assert isinstance(var_68, python_code_.standard_StandardStochasticDiseaseModel)
    var_68.computeNoise()
    var_70 = 5.0
    var_71 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_70,
        totalPopulationCountReciprocal=var_67,
        totalArea=var_70,
        referencePopulationDensity=var_67,
    )
    assert isinstance(var_71, python_code_.standard_StandardDiseaseModel)


def test_13():
    var_29 = "_standard_SIRLabelValue__standard_SIRLabelValue47-_standard_Infector__standard_Infector7-standard_SILabel30-standard_StandardDiseaseModel"
    var_30 = {
        "Uwb_&!YUM": True,
        "standard_SIRLabel": 923.04,
        "\t1B": -139.34,
        '/"*c\x0b(,m5WfWt\\Vpdsb': var_29,
        "-X": var_29,
    }
    var_31 = python_code_.standard_Infector(
        targetURI=var_30,
        diseaseName=True,
        targetISOKey=var_30,
        populationIdentifier=var_30,
        infectPercentage=var_30,
    )
    assert isinstance(var_31, python_code_.standard_Infector)


def test_14():
    var_57 = python_code_.standard_InfectorInoculatorCollection(
        importFolder="_standard_SEIRLabelValue__standard_SEIRLabelValue18 _standard_SEIRLabelValue__standard_SEIRLabelValue _standard_SIRLabelValue__standard_SIRLabelValue44"
    )
    assert isinstance(var_57, python_code_.standard_InfectorInoculatorCollection)


def test_15():
    python_code_.standard_SanityChecker()


def test_16():
    var_1 = -3077.29
    var_2 = python_code_.standard_SEIR(incubationRate=var_1)
    assert isinstance(var_2, python_code_.standard_SEIR)
    var_6 = python_code_.standard_IntegrationLabel()
    var_7 = 1085.28
    var_8 = python_code_.standard_SIRInoculator(
        inoculatedPercentage=var_7, inoculatePercentage=var_6
    )
    assert isinstance(var_8, python_code_.standard_SIRInoculator)
    var_9 = 2955.42
    var_10 = python_code_.DiseaseModel
    var_11 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_7,
        totalPopulationCountReciprocal=var_9,
        totalArea=var_7,
        referencePopulationDensity=var_10,
    )
    assert isinstance(var_11, python_code_.standard_StandardDiseaseModel)
    var_11.calculateDelta(
        standard_time=var_11, standard_timeDelta=var_8, standard_labels=var_10
    )
    var_16 = "|\nP)kXuz"
    var_17 = python_code_.standard_StochasticDiseaseModel(
        seed=var_10, randomGenerator=var_16
    )
    assert isinstance(var_17, python_code_.standard_StochasticDiseaseModel)
    var_18 = python_code_.standard_AggregatingSIRDiseaseModel()
    var_19 = python_code_.standard_InfectorInoculatorCollection(importFolder=var_18)
    assert isinstance(var_19, python_code_.standard_InfectorInoculatorCollection)
    var_27 = 4108.07
    var_28 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths=var_1, populationCount=var_27, incidence=None
    )
    assert isinstance(var_28, python_code_.standard_DiseaseModelLabelValue)
    var_29 = 3211.85
    var_30 = python_code_.standard_StandardStochasticDiseaseModel(gain=var_29)
    assert isinstance(var_30, python_code_.standard_StandardStochasticDiseaseModel)


def test_17():
    var_41 = 49.34247220850223
    var_42 = python_code_.AggregatingSIDiseaseModel
    var_43 = python_code_.standard_SILabelValue(
        i=var_41,
        standard_SILabelValue25=var_42,
        standard_SILabelValue34=complex(2943.0, 4078.1861466),
    )
    assert isinstance(var_43, python_code_.standard_SILabelValue)
    var_44 = python_code_.standard_IntegrationDecorator()
    var_44.isDeterministic()


def test_18():
    var_3 = python_code_.standard_IntegrationDecorator
    var_24 = 48.72804558343934
    var_27 = python_code_.standard_IntegrationLabel()
    var_29 = python_code_.standard_StochasticDiseaseModel(
        seed=var_24, randomGenerator=var_27
    )
    assert isinstance(var_29, python_code_.standard_StochasticDiseaseModel)
    var_30 = "*B\r5l"
    var_31 = False
    var_32 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=var_24,
        populationIdentifier=var_30,
        timePeriod=var_30,
        diseaseName=var_3,
        relativeTolerance={"\r&1(VqaW^/~S}": True},
        finiteDifference=var_31,
        frequencyDependent=b"I\nn\xa3\x14\xdd\xa8",
        backgroundBirthRate=var_24,
    )
    assert isinstance(var_32, python_code_.standard_DiseaseModel)
    var_32.getAdjustedBackgroundMortalityRate(standard_timeDelta=(393, 1039.72))


def test_19():
    var_0 = python_code_.standard_SIInfector(infectiousCount=0)
    assert isinstance(var_0, python_code_.standard_SIInfector)


def test_20():
    var_0 = 583.05
    var_1 = python_code_.standard_SI(
        transmissionRate={-475, False},
        nonLinearityCoefficient=b"\xcb?n\x06\xa3\xa1\xab\xf2\x95`l\xac\xc6",
        recoveryRate=b"o\x0e\xd13\x1c+E\xd3\xa8",
        infectiousMortalityRate=(),
        physicallyAdjacentInfectiousProportion=complex(-339.06435, -2135.932),
        roadNetworkInfectiousProportion=var_0,
        infectiousMortality=var_0,
        characteristicMixingDistance=var_0,
    )
    assert isinstance(var_1, python_code_.standard_SI)
    var_2 = var_1.getAdjustedInfectiousMortalityRate(standard_timeDelta=273)
    var_5 = 947.51
    var_6 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_0,
        totalPopulationCountReciprocal=var_0,
        totalArea=var_2,
        referencePopulationDensity=var_5,
    )
    assert isinstance(var_6, python_code_.standard_StandardDiseaseModel)
    var_6.doModelSpecificAdjustments(standard_label=var_0)


@pytest.mark.xfail(strict=True)
def test_21():
    var_0 = -495.86
    var_1 = "standard_SEIRLabel.standard_Infector._standard_SIRLabelValue__standard_SIRLabelValue38"
    var_2 = "b;4r_OQj=$@u@JI"
    var_3 = False
    var_4 = -2024.5
    var_5 = -1385.94
    var_6 = lambda *args, **kwargs: -1166
    var_7 = lambda *args, **kwargs: False
    var_8 = python_code_.standard_SI(
        transmissionRate=set(),
        nonLinearityCoefficient=var_0,
        recoveryRate=var_4,
        infectiousMortalityRate=var_5,
        physicallyAdjacentInfectiousProportion=var_6,
        roadNetworkInfectiousProportion=var_7,
        infectiousMortality=(1079.24, False),
        characteristicMixingDistance=var_7,
    )
    assert isinstance(var_8, python_code_.standard_SI)
    var_9 = var_8.getAdjustedTransmissionRate(standard_timeDelta=var_7)
    var_10 = python_code_.standard_Infector(
        targetURI=var_0,
        diseaseName=var_1,
        targetISOKey={
            "_standard_SIRLabelValue__standard_SIRLabelValue44,_standard_SIRLabelValue__standard_SIRLabelValue41,standard_Infector": "UQ[,W>&p<Bx9`",
            ";N0": -214.37,
        },
        populationIdentifier=var_2,
        infectPercentage=var_3,
        standard_Infector7=var_9,
    )
    assert isinstance(var_10, python_code_.standard_Infector)
    python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_0,
        totalPopulationCountReciprocal=var_0,
        totalArea=None,
        referencePopulationDensity=[],
        standard_StandardDiseaseModel=var_10,
    )


def test_22():
    var_2 = -737.04
    var_3 = python_code_.standard_SIRLabel()
    var_4 = python_code_.standard_SIRLabelValue(
        r=var_2, standard_SIRLabelValue38=True, standard_SIRLabelValue41=var_3
    )
    assert isinstance(var_4, python_code_.standard_SIRLabelValue)
    var_5 = python_code_.standard_DeterministicSIDiseaseModel()
    var_7 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=None,
        totalPopulationCountReciprocal={},
        totalArea=var_2,
        referencePopulationDensity={"standard_SEIRLabel17": 1},
    )
    assert isinstance(var_7, python_code_.standard_StandardDiseaseModel)
    var_8 = python_code_.standard_SIRLabel
    var_9 = python_code_.standard_SILabelValue(
        i=var_2, standard_SILabelValue=var_8, standard_SILabelValue34=var_8
    )
    assert isinstance(var_9, python_code_.standard_SILabelValue)
    var_11 = "standard_SIRLabel,standard_SIRLabel37,standard_SILabel30"
    var_12 = False
    var_13 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=var_7,
        populationIdentifier=[
            884.39,
            "_standard_SILabelValue__standard_SILabelValue25standard_SIRLabel37",
            False,
        ],
        timePeriod=2377,
        diseaseName=var_11,
        relativeTolerance=var_2,
        finiteDifference=var_7,
        frequencyDependent=var_12,
        backgroundBirthRate=var_5,
    )
    assert isinstance(var_13, python_code_.standard_DiseaseModel)
    var_16 = python_code_.standard_SI(
        transmissionRate=var_2,
        nonLinearityCoefficient=var_2,
        recoveryRate=var_12,
        infectiousMortalityRate="standard_SIRLabel.standard_SEIRLabel14.standard_SEIRLabel11",
        physicallyAdjacentInfectiousProportion=var_2,
        roadNetworkInfectiousProportion=var_8,
        infectiousMortality=var_3,
        characteristicMixingDistance=var_13,
    )
    assert isinstance(var_16, python_code_.standard_SI)
    var_16.getAdjustedRecoveryRate(standard_timeDelta=b"\xb5`\x0eM(\xa2\x02\x81\xc4")
    var_13.createDiseaseModelLabel()


def test_23():
    var_0 = python_code_.standard_IntegrationLabelValue()
    var_1 = python_code_.standard_DiseaseModelLabel()
    var_2 = python_code_.standard_SIDiseaseModelState
    var_3 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_1,
        totalPopulationCountReciprocal=False,
        totalArea=var_2,
        referencePopulationDensity=var_2,
        standard_StandardDiseaseModel=var_0,
    )
    assert isinstance(var_3, python_code_.standard_StandardDiseaseModel)
    var_3.addToTotalPopulationCount(standard_populationCount=())


def test_24():
    var_72 = lambda *args, **kwargs: False
    var_75 = python_code_.standard_DeterministicSIDiseaseModel()
    var_76 = 210.56
    var_77 = -329.2
    var_78 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_72,
        totalPopulationCountReciprocal=var_76,
        totalArea=var_77,
        referencePopulationDensity=complex(-4835.2705, 2938.8),
    )
    assert isinstance(var_78, python_code_.standard_StandardDiseaseModel)
    var_78.calculateDelta(
        standard_time=set(), standard_timeDelta=None, standard_labels=-1691
    )
    var_80 = 695.4
    var_81 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths=var_76, populationCount=var_75, incidence=var_80
    )
    assert isinstance(var_81, python_code_.standard_DiseaseModelLabelValue)
    var_81.sub(standard_value=var_72)


def test_25():
    var_0 = 1252.2213067601765
    var_1 = lambda *args, **kwargs: False
    var_2 = python_code_.standard_SEIRLabelValue(
        e=550.36, standard_SEIRLabelValue12=var_1
    )
    assert isinstance(var_2, python_code_.standard_SEIRLabelValue)
    var_39 = -2516.65
    var_40 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths=var_0, populationCount=var_0, incidence=var_39
    )
    assert isinstance(var_40, python_code_.standard_DiseaseModelLabelValue)
    var_40.scale(standard_scaleFactor=var_1)


def test_26():
    var_0 = python_code_.SanityChecker
    var_1 = python_code_.standard_StandardStochasticDiseaseModel(gain=var_0)
    assert isinstance(var_1, python_code_.standard_StandardStochasticDiseaseModel)
    var_2 = 1033.48
    var_3 = "standard_SEIRLabel14.standard_SILabel27"
    var_4 = False
    var_5 = True
    var_6 = -1079.93
    var_7 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=var_2,
        populationIdentifier=var_0,
        timePeriod="standard_InfectorInoculatorCollection,standard_SILabel33",
        diseaseName=var_3,
        relativeTolerance=var_2,
        finiteDifference=var_4,
        frequencyDependent=var_5,
        backgroundBirthRate=var_6,
    )
    assert isinstance(var_7, python_code_.standard_DiseaseModel)


def test_27():
    var_6 = python_code_.StochasticDiseaseModel()
    var_53 = python_code_.standard_AggregatingSIDiseaseModel()
    var_57 = float
    var_58 = python_code_.standard_SILabel()
    var_59 = python_code_.standard_SILabelValue(
        i=var_6,
        standard_SILabelValue25=var_57,
        standard_SILabelValue31=var_58,
        standard_SILabelValue34=var_58,
    )
    assert isinstance(var_59, python_code_.standard_SILabelValue)
    var_60 = -523.62
    var_61 = 1230.17
    var_62 = False
    var_63 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=var_60,
        populationIdentifier=var_57,
        timePeriod=var_57,
        diseaseName={"_xiN": 4008.6},
        relativeTolerance=var_61,
        finiteDifference=var_58,
        frequencyDependent=var_62,
        backgroundBirthRate=var_61,
    )
    assert isinstance(var_63, python_code_.standard_DiseaseModel)
    var_63.createDiseaseModelLabel()
    var_65 = 3200.1
    var_66 = python_code_.standard_SI(
        transmissionRate=var_60,
        nonLinearityCoefficient=-1311.45,
        recoveryRate=False,
        infectiousMortalityRate=var_65,
        physicallyAdjacentInfectiousProportion=var_65,
        roadNetworkInfectiousProportion=var_60,
        infectiousMortality=var_60,
        characteristicMixingDistance=False,
    )
    assert isinstance(var_66, python_code_.standard_SI)
    var_66.getAdjustedInfectiousMortalityRate(standard_timeDelta=var_53)


def test_28():
    var_0 = 1260.44
    var_1 = lambda *args, **kwargs: False
    var_2 = python_code_.standard_SEIRLabelValue(
        e=var_0, standard_SEIRLabelValue18=var_1
    )
    assert isinstance(var_2, python_code_.standard_SEIRLabelValue)
    var_3 = 602.41
    var_4 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_1,
        totalPopulationCountReciprocal=var_0,
        totalArea=var_3,
        referencePopulationDensity=var_1,
    )
    assert isinstance(var_4, python_code_.standard_StandardDiseaseModel)
    var_5 = var_4.calculateDelta(
        standard_time=1077.85, standard_timeDelta=var_0, standard_labels=var_1
    )
    var_6 = "standard_SIRLabel46._standard_SEIRLabelValue__standard_SEIRLabelValue"
    var_7 = 1613.16
    var_8 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=var_4,
        populationIdentifier=var_1,
        timePeriod=var_6,
        diseaseName=var_5,
        relativeTolerance=var_7,
        finiteDifference=complex(-135.29249, -2049.4503),
        frequencyDependent=set(),
        backgroundBirthRate=var_1,
    )
    assert isinstance(var_8, python_code_.standard_DiseaseModel)
    var_8.createDiseaseModelLabelValue()


def test_29():
    var_0 = python_code_.DiseaseModelLabel()
    var_2 = python_code_.standard_DeterministicSIRDiseaseModel()
    var_3 = "6~7D\x0c"
    var_4 = True
    var_5 = -1245.23
    var_6 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=[924.2, -371, -1476.59],
        populationIdentifier=var_2,
        timePeriod=var_0,
        diseaseName=var_3,
        relativeTolerance=var_0,
        finiteDifference=var_4,
        frequencyDependent=4359.79,
        backgroundBirthRate=var_5,
    )
    assert isinstance(var_6, python_code_.standard_DiseaseModel)
    var_6.createDiseaseModelState()
    var_10 = python_code_.standard_SEIRLabel()
    var_11 = python_code_.standard_SEIRLabelValue(
        e=True, standard_SEIRLabelValue21=var_10
    )
    assert isinstance(var_11, python_code_.standard_SEIRLabelValue)
    python_code_.standard_IntegrationDecorator()


def test_30():
    var_0 = 1260.44
    var_38 = python_code_.standard_SIRLabelValue(
        r=3546.91, standard_SIRLabelValue38=var_0
    )
    assert isinstance(var_38, python_code_.standard_SIRLabelValue)
    var_39 = python_code_.standard_SEIR(incubationRate=var_0)
    assert isinstance(var_39, python_code_.standard_SEIR)


def test_31():
    var_1 = python_code_.standard_SILabel()
    var_2 = -737.04
    var_9 = python_code_.standard_SILabelValue(
        i=var_2,
        standard_SILabelValue25=None,
        standard_SILabelValue28=var_1,
        standard_SILabelValue31=var_1,
    )
    assert isinstance(var_9, python_code_.standard_SILabelValue)


@pytest.mark.xfail(strict=True)
def test_32():
    var_51 = python_code_.standard_SIDiseaseModelState
    var_54 = python_code_.standard_SEIRLabelValue(
        e=var_51, standard_SEIRLabelValue21=-1149.84
    )
    assert isinstance(var_54, python_code_.standard_SEIRLabelValue)
    python_code_.standard_InfectorInoculatorCollection(
        importFolder=var_51, standard_InfectorInoculatorCollection=var_51
    )


def test_33():
    var_0 = python_code_.StandardInfector()
    var_1 = python_code_.standard_SILabel()
    var_2 = -737.04
    var_3 = python_code_.standard_SIRLabel()
    var_4 = python_code_.standard_SIRLabelValue(
        r=var_2, standard_SIRLabelValue38=True, standard_SIRLabelValue41=var_3
    )
    assert isinstance(var_4, python_code_.standard_SIRLabelValue)
    var_7 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=None,
        totalPopulationCountReciprocal={},
        totalArea=var_2,
        referencePopulationDensity={"standard_SEIRLabel17": 1},
    )
    assert isinstance(var_7, python_code_.standard_StandardDiseaseModel)
    var_55 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths=var_1,
        populationCount=complex(2169.703, -363.7328),
        incidence=var_0,
    )
    assert isinstance(var_55, python_code_.standard_DiseaseModelLabelValue)
    var_55.set(standard_value="%=PNh:9.w_4j")
    var_55.add(standard_value=None)


def test_34():
    var_2 = -749.2067589884549
    var_66 = python_code_.AggregatingSIRDiseaseModel
    var_67 = python_code_.standard_SILabelValue(
        i=var_2, standard_SILabelValue=var_66, standard_SILabelValue34=var_66
    )
    assert isinstance(var_67, python_code_.standard_SILabelValue)
    var_73 = 1078.2237538832376
    var_77 = python_code_.standard_SIR(immunityLossRate=var_73)
    assert isinstance(var_77, python_code_.standard_SIR)
    var_77.getAdjustedImmunityLossRate(standard_timeDelta=var_2)


def test_35():
    var_2 = -737.04
    var_3 = python_code_.standard_SIRLabel()
    var_4 = python_code_.standard_SIRLabelValue(
        r=var_2, standard_SIRLabelValue38=True, standard_SIRLabelValue41=var_3
    )
    assert isinstance(var_4, python_code_.standard_SIRLabelValue)
    var_5 = python_code_.standard_DeterministicSIDiseaseModel()
    var_7 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=None,
        totalPopulationCountReciprocal={},
        totalArea=var_2,
        referencePopulationDensity={"standard_SEIRLabel17": 1},
    )
    assert isinstance(var_7, python_code_.standard_StandardDiseaseModel)
    var_8 = python_code_.standard_SIRLabel
    var_9 = python_code_.standard_SILabelValue(
        i=var_2, standard_SILabelValue=var_8, standard_SILabelValue34=var_8
    )
    assert isinstance(var_9, python_code_.standard_SILabelValue)
    var_11 = "standard_SIRLabel,standard_SIRLabel37,standard_SILabel30"
    var_50 = ""
    var_51 = python_code_.standard_Infector(
        targetURI=var_11,
        diseaseName=var_11,
        targetISOKey=var_50,
        populationIdentifier=None,
        infectPercentage=complex(3469.485, 3299.996),
    )
    assert isinstance(var_51, python_code_.standard_Infector)
    var_52 = 21.91
    var_53 = 1100.42
    var_54 = 2968.0
    var_55 = python_code_.standard_SI(
        transmissionRate=var_9,
        nonLinearityCoefficient=var_52,
        recoveryRate=var_52,
        infectiousMortalityRate=var_52,
        physicallyAdjacentInfectiousProportion=var_53,
        roadNetworkInfectiousProportion=var_54,
        infectiousMortality=(1931.02, True),
        characteristicMixingDistance=var_5,
    )
    assert isinstance(var_55, python_code_.standard_SI)
    var_55.getNormalizedEffectiveInfectious(
        standard_onsiteInfectious=var_8,
        standard_node=-222.8,
        standard_diseaseLabel=var_2,
    )


def test_36():
    var_4 = python_code_.StandardDiseaseModelState()
    var_6 = python_code_.standard_SIR(immunityLossRate=None)
    assert isinstance(var_6, python_code_.standard_SIR)
    var_6.getAdjustedImmunityLossRate(standard_timeDelta=var_4)
    var_13 = -1341.03
    var_14 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_13,
        totalPopulationCountReciprocal=complex(-338.756, -2869.72733),
        totalArea=var_13,
        referencePopulationDensity=var_13,
    )
    assert isinstance(var_14, python_code_.standard_StandardDiseaseModel)
    var_14.addToTotalArea(standard_area=True)


def test_37():
    var_24 = 48.72804558343934
    var_25 = python_code_.AggregatingSIDiseaseModel
    var_26 = python_code_.standard_SILabelValue(
        i=var_24,
        standard_SILabelValue25=var_25,
        standard_SILabelValue34=complex(2943.0, 4078.1861466),
    )
    assert isinstance(var_26, python_code_.standard_SILabelValue)


def test_38():
    var_1 = python_code_.standard_AggregatingSIRDiseaseModel()
    var_43 = python_code_.standard_SILabelValue(
        i=-2479.2,
        standard_SILabelValue25=None,
        standard_SILabelValue28=var_1,
        standard_SILabelValue34=None,
    )
    assert isinstance(var_43, python_code_.standard_SILabelValue)


def test_39():
    var_2 = -737.04
    var_3 = python_code_.standard_SIRLabel()
    var_4 = python_code_.standard_SIRLabelValue(
        r=var_2, standard_SIRLabelValue38=True, standard_SIRLabelValue41=var_3
    )
    assert isinstance(var_4, python_code_.standard_SIRLabelValue)
    var_58 = python_code_.standard_StandardDiseaseModelState(areaRatio=-2252.96)
    assert isinstance(var_58, python_code_.standard_StandardDiseaseModelState)


def test_40():
    var_39 = set()
    var_42 = python_code_.standard_SIRLabelValue(
        r=-2747, standard_SIRLabelValue44=var_39
    )
    assert isinstance(var_42, python_code_.standard_SIRLabelValue)


def test_41():
    var_0 = 1086.41
    var_1 = "*}! m\\\naO V%3\to\x0cM^"
    var_2 = True
    var_3 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=var_0,
        populationIdentifier=var_1,
        timePeriod=var_0,
        diseaseName=1534.58,
        relativeTolerance=var_0,
        finiteDifference=var_2,
        frequencyDependent={},
        backgroundBirthRate=var_1,
    )
    assert isinstance(var_3, python_code_.standard_DiseaseModel)
    var_3.createInfector()
    var_5 = python_code_.IntegrationLabel
    var_6 = 1164.71
    var_7 = python_code_.standard_SI(
        transmissionRate=var_0,
        nonLinearityCoefficient=445,
        recoveryRate=var_0,
        infectiousMortalityRate=var_0,
        physicallyAdjacentInfectiousProportion=var_3,
        roadNetworkInfectiousProportion=var_5,
        infectiousMortality=var_0,
        characteristicMixingDistance=var_6,
    )
    assert isinstance(var_7, python_code_.standard_SI)
    var_8 = var_7.getAdjustedInfectiousMortalityRate(standard_timeDelta=var_7)
    var_11 = python_code_.standard_StandardDiseaseModelLabelValue(s=var_0)
    assert isinstance(var_11, python_code_.standard_StandardDiseaseModelLabelValue)
    var_3.createDiseaseModelLabel()
    var_15 = 2126.11
    var_16 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths=var_15, populationCount=var_2, incidence=var_2
    )
    assert isinstance(var_16, python_code_.standard_DiseaseModelLabelValue)
    var_16.scale(standard_scaleFactor=(False, "I&N\\m-!_)^4;KB,Yv", True))
    var_19 = python_code_.StandardDiseaseModel()
    var_21 = python_code_.standard_SIR(immunityLossRate=var_5)
    assert isinstance(var_21, python_code_.standard_SIR)
    var_22 = var_21.getAdjustedImmunityLossRate(standard_timeDelta=var_5)
    var_24 = '%x"'
    var_25 = python_code_.standard_StochasticDiseaseModel(
        seed=var_1, randomGenerator=var_24
    )
    assert isinstance(var_25, python_code_.standard_StochasticDiseaseModel)
    var_3.getAdjustedBackgroundBirthRate(standard_timeDelta=var_22)
    python_code_.standard_IntegrationDecorator()
    var_31 = 1602.33
    var_32 = python_code_.standard_SEIR(incubationRate=var_31)
    assert isinstance(var_32, python_code_.standard_SEIR)
    var_33 = var_32.getAdjustedIncubationRate(standard_timeDelta=var_5)
    var_3.getAdjustedBackgroundMortalityRate(standard_timeDelta=var_19)
    var_38 = -670.01
    var_39 = -1029.4
    var_40 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_38,
        totalPopulationCountReciprocal=var_6,
        totalArea=var_39,
        referencePopulationDensity=var_38,
    )
    assert isinstance(var_40, python_code_.standard_StandardDiseaseModel)
    var_40.calculateDelta(
        standard_time=["#G?>fo@g`b+\x0bKVj D", "rV0n+\tqc"],
        standard_timeDelta=var_33,
        standard_labels=var_8,
    )


def test_42():
    var_1 = lambda *args, **kwargs: False
    var_44 = python_code_.standard_SIRLabelValue(
        r=2807.91, standard_SIRLabelValue41=var_1, standard_SIRLabelValue47=var_1
    )
    assert isinstance(var_44, python_code_.standard_SIRLabelValue)


def test_43():
    var_1 = [-1, 576.57]
    var_38 = python_code_.standard_SIRLabelValue(
        r=993.6, standard_SIRLabelValue38=None, standard_SIRLabelValue47=var_1
    )
    assert isinstance(var_38, python_code_.standard_SIRLabelValue)
    var_39 = 637.88
    var_40 = bool
    var_41 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_39,
        totalPopulationCountReciprocal=var_39,
        totalArea=var_40,
        referencePopulationDensity=var_1,
    )
    assert isinstance(var_41, python_code_.standard_StandardDiseaseModel)
    var_41.computeTotalPopulationCountReciprocal()


def test_44():
    var_2 = -737.04
    var_3 = python_code_.standard_SIRLabel()
    var_4 = python_code_.standard_SIRLabelValue(
        r=454.79, standard_SIRLabelValue38=var_3
    )
    assert isinstance(var_4, python_code_.standard_SIRLabelValue)
    var_7 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=None,
        totalPopulationCountReciprocal={},
        totalArea=var_2,
        referencePopulationDensity={"standard_SEIRLabel17": 1},
    )
    assert isinstance(var_7, python_code_.standard_StandardDiseaseModel)
    var_8 = python_code_.standard_SIRLabel
    var_9 = python_code_.standard_SILabelValue(
        i=var_2, standard_SILabelValue=var_8, standard_SILabelValue34=var_8
    )
    assert isinstance(var_9, python_code_.standard_SILabelValue)
    var_11 = "standard_SIRLabel,standard_SIRLabel37,standard_SILabel30"
    var_57 = "\t"
    var_58 = python_code_.standard_Infector(
        targetURI=var_11,
        diseaseName=var_11,
        targetISOKey=var_57,
        populationIdentifier=None,
        infectPercentage=complex(3469.485, 3299.996),
    )
    assert isinstance(var_58, python_code_.standard_Infector)
    var_65 = 485.36
    var_66 = -1535.01
    var_67 = python_code_.standard_SI(
        transmissionRate=var_2,
        nonLinearityCoefficient=var_9,
        recoveryRate=var_65,
        infectiousMortalityRate=[],
        physicallyAdjacentInfectiousProportion=var_2,
        roadNetworkInfectiousProportion=var_66,
        infectiousMortality=var_9,
        characteristicMixingDistance=var_58,
    )
    assert isinstance(var_67, python_code_.standard_SI)
    var_67.getEffectiveInfectious(
        standard_diseaseLabel=var_65,
        standard_onsiteInfectious=var_8,
        standard_node=var_8,
    )


def test_45():
    var_1 = lambda *args, **kwargs: False
    var_43 = python_code_.DiseaseModelState()
    var_44 = "_standard_SILabelValue__standard_SILabelValue25 _standard_SILabelValue__standard_SILabelValue31 standard_SILabel"
    var_45 = python_code_.standard_Infector(
        targetURI=var_1,
        diseaseName=var_44,
        targetISOKey=var_1,
        populationIdentifier=var_43,
        infectPercentage=var_44,
        standard_Infector51=var_1,
    )
    assert isinstance(var_45, python_code_.standard_Infector)


def test_46():
    var_0 = "u\x0c1kjL+);.\tg_x%=d8C"
    var_1 = python_code_.standard_Infector(
        targetURI=[
            -2396.46,
            False,
            "_standard_SIRLabelValue__standard_SIRLabelValue38,standard_SEIRLabel17,_standard_SIRLabelValue__standard_SIRLabelValue38,_standard_SEIRLabelValue__standard_SEIRLabelValue21",
        ],
        diseaseName="standard_SILabel24",
        targetISOKey=(),
        populationIdentifier=var_0,
        infectPercentage=b"\xc4\xd1G$\xefa\xe4B04",
        standard_Infector=False,
        standard_Infector51=var_0,
    )
    assert isinstance(var_1, python_code_.standard_Infector)
    var_2 = 659.91
    var_3 = lambda *args, **kwargs: "ju>,4|@g}/?"
    var_4 = 348.81
    var_5 = -2232.21
    var_6 = 1488.06
    var_7 = python_code_.standard_SI(
        transmissionRate=var_2,
        nonLinearityCoefficient=var_1,
        recoveryRate=var_3,
        infectiousMortalityRate=var_4,
        physicallyAdjacentInfectiousProportion=var_2,
        roadNetworkInfectiousProportion=var_5,
        infectiousMortality=var_0,
        characteristicMixingDistance=var_6,
    )
    assert isinstance(var_7, python_code_.standard_SI)
    var_7.getNormalizedEffectiveInfectious(
        standard_onsiteInfectious=var_7,
        standard_node=var_3,
        standard_diseaseLabel=var_3,
    )
    var_9 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths=var_2, populationCount=var_5, incidence=None
    )
    assert isinstance(var_9, python_code_.standard_DiseaseModelLabelValue)
    var_9.scale(standard_scaleFactor=var_3)


def test_47():
    var_0 = python_code_.standard_SIInfector(infectiousCount=0)
    assert isinstance(var_0, python_code_.standard_SIInfector)
    var_7 = python_code_.standard_SIRLabelValue
    var_9 = python_code_.standard_SEIRLabelValue(
        e=3982.3, standard_SEIRLabelValue12=var_0, standard_SEIRLabelValue15=var_7
    )
    assert isinstance(var_9, python_code_.standard_SEIRLabelValue)
    var_11 = python_code_.standard_SIRLabel()
    var_12 = python_code_.standard_SIRLabelValue(
        r=-2747, standard_SIRLabelValue44=var_11
    )
    assert isinstance(var_12, python_code_.standard_SIRLabelValue)


def test_48():
    var_42 = "L'{Sl{&"
    var_43 = python_code_.standard_SEIRLabelValue(
        e=2116.14, standard_SEIRLabelValue=var_42, standard_SEIRLabelValue12=None
    )
    assert isinstance(var_43, python_code_.standard_SEIRLabelValue)


def test_49():
    var_77 = 48.72804558343934
    var_78 = python_code_.AggregatingSIDiseaseModel
    var_79 = python_code_.standard_SILabelValue(
        i=var_77,
        standard_SILabelValue25=var_78,
        standard_SILabelValue34=complex(2943.0, 4078.1861466),
    )
    assert isinstance(var_79, python_code_.standard_SILabelValue)
    var_80 = -784.64
    var_81 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths={
            "_standard_Infector__standard_Infector": True,
            "<@m]h@s)MVf,/(4$  E": "standard_SIRLabel46,_standard_SIRLabelValue__standard_SIRLabelValue41,standard_DiseaseModelLabel,standard_Infector51",
        },
        populationCount=(-1,),
        incidence=var_80,
    )
    assert isinstance(var_81, python_code_.standard_DiseaseModelLabelValue)
    var_81.zeroOutPopulationCount()


def test_50():
    var_0 = python_code_.AggregatingSIRDiseaseModel()
    var_1 = 4082.77
    var_2 = python_code_.standard_DiseaseModelLabelValue(
        diseaseDeaths=var_1,
        populationCount=315,
        incidence="_standard_SEIRLabelValue__standard_SEIRLabelValue21standard_SEIRLabel14",
    )
    assert isinstance(var_2, python_code_.standard_DiseaseModelLabelValue)
    var_4 = python_code_.AggregatingSIDiseaseModel()
    var_5 = python_code_.SI
    var_6 = python_code_.standard_SEIRLabelValue(
        e=var_4,
        standard_SEIRLabelValue=None,
        standard_SEIRLabelValue12=2310,
        standard_SEIRLabelValue15=var_4,
        standard_SEIRLabelValue18=var_5,
    )
    assert isinstance(var_6, python_code_.standard_SEIRLabelValue)
    var_7 = python_code_.standard_StochasticDiseaseModel(
        seed=var_5, randomGenerator=var_5
    )
    assert isinstance(var_7, python_code_.standard_StochasticDiseaseModel)
    var_8 = python_code_.standard_SILabel()
    var_9 = python_code_.standard_SILabelValue(i=var_1, standard_SILabelValue31=var_8)
    assert isinstance(var_9, python_code_.standard_SILabelValue)
    var_12 = -1109.64
    var_13 = "[r|h0mV3+"
    var_14 = True
    var_15 = python_code_.standard_DiseaseModel(
        backgroundMortalityRate=var_12,
        populationIdentifier=[1624.26, False, 126],
        timePeriod=var_12,
        diseaseName=var_13,
        relativeTolerance=var_2,
        finiteDifference=var_6,
        frequencyDependent=var_14,
        backgroundBirthRate=var_1,
    )
    assert isinstance(var_15, python_code_.standard_DiseaseModel)
    var_15.initializeDiseaseState(standard_diseaseModelLabel=-3903.04)
    var_17 = python_code_.standard_SEIR(incubationRate=var_1)
    assert isinstance(var_17, python_code_.standard_SEIR)
    var_18 = python_code_.standard_StandardDiseaseModel(
        totalPopulationCount=var_9,
        totalPopulationCountReciprocal=var_5,
        totalArea=var_14,
        referencePopulationDensity=var_4,
    )
    assert isinstance(var_18, python_code_.standard_StandardDiseaseModel)
    var_18.addToTotalArea(standard_area=var_0)
    var_23 = python_code_.standard_SEIRLabel()
    var_25 = -567.46
    python_code_.standard_SEIRLabelValue(
        e=var_25, standard_SEIRLabelValue=var_23, standard_SEIRLabelValue18=var_23
    )
    var_15.createDiseaseModelState()


def test_51():
    var_35 = python_code_.DynamicNodeLabel
    var_36 = ')"\\SAs]m0'
    var_37 = "_standard_Infector__standard_Infector7,_standard_SILabelValue__standard_SILabelValue25,_standard_InfectorInoculatorCollection__standard_InfectorInoculatorCollection"
    var_38 = python_code_.standard_InfectorInoculatorCollection(importFolder=var_37)
    assert isinstance(var_38, python_code_.standard_InfectorInoculatorCollection)
    var_39 = python_code_.standard_Infector(
        targetURI=var_35,
        diseaseName=[],
        targetISOKey=var_35,
        populationIdentifier=var_36,
        infectPercentage=-583.92,
        standard_Infector51=var_38,
    )
    assert isinstance(var_39, python_code_.standard_Infector)
