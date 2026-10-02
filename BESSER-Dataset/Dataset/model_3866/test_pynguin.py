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
    COREConfiguration,
    COREFeatureRelationshipType,
    COREImpactNode,
    COREModel,
    COREModelElement,
    CORENamedElement,
    COREPartialityType,
    COREVisibilityType,
    Enum,
    abstractmethod,
    core_COREBinding,
    core_CORECompositionSpecification,
    core_COREConcern,
    core_COREConcernConfiguration,
    core_COREConfiguration,
    core_COREContribution,
    core_COREFeature,
    core_COREFeatureImpactNode,
    core_COREFeatureModel,
    core_COREImpactModel,
    core_COREImpactModelBinding,
    core_COREImpactNode,
    core_COREInterface,
    core_COREMapping,
    core_COREModel,
    core_COREModelCompositionSpecification,
    core_COREModelElement,
    core_COREModelReuse,
    core_CORENamedElement,
    core_COREPattern,
    core_CORERelativity,
    core_CORERelativity_Opt2,
    core_COREReuse,
    core_COREReuseConfiguration,
    core_COREWeightedMapping,
    core_EObject,
    core_LayoutContainerMap,
    core_LayoutElement,
    core_LayoutMap,
    date,
    datetime,
    time,
)


def test_0():
    python_code_.core_COREWeightedMapping(weight=218)


def test_1():
    var_40 = python_code_.core_COREWeightedMapping
    var_41 = python_code_.core_COREWeightedMapping(
        weight={
            "!VbB:LONWJg/Il3T9": True,
            '1Nl h)\rcxQ-@N\ts{_B"': -2790.46,
            '{,9x${+XA=4"y,~G\n': "core_COREFeature28,core_COREFeatureImpactNode106,public,core_COREFeature28",
        },
        core_COREWeightedMapping=var_40,
    )
    python_code_.core_CORERelativity_Opt2(probabilisticValue=var_41)


def test_2():
    var_0 = python_code_.COREImpactNode()
    var_3 = python_code_.core_COREFeatureImpactNode(
        relativeFeatureWeight=350,
        core_COREFeatureImpactNode=var_0,
        core_COREFeatureImpactNode106=set(),
    )
    assert isinstance(var_3, python_code_.core_COREFeatureImpactNode)


def test_3():
    var_3 = python_code_.core_COREFeatureImpactNode(relativeFeatureWeight=1925)
    assert isinstance(var_3, python_code_.core_COREFeatureImpactNode)


def test_4():
    var_0 = 2226.7
    var_1 = python_code_.core_LayoutElement(
        x=-2776.7, y=var_0, core_LayoutElement=var_0
    )
    assert isinstance(var_1, python_code_.core_LayoutElement)


def test_5():
    var_0 = 2226.7
    python_code_.core_LayoutElement(x=var_0, y=-4614.55)


def test_6():
    var_3 = python_code_.core_COREConcern()
    var_5 = python_code_.core_COREImpactNode
    python_code_.core_COREContribution(relativeWeight=var_5)
    var_7 = 1512.77
    var_8 = python_code_.core_COREFeatureModel()
    var_9 = python_code_.core_CORERelativity_Opt2(
        probabilisticValue=var_7,
        CORERelativity_Opt2=var_3,
        core_CORERelativity_Opt2=var_8,
        incoming120=b"!\xd9\xc5\x9e\xd0O\xce\xc6\xf7",
    )
    assert isinstance(var_9, python_code_.core_CORERelativity_Opt2)
    var_10 = python_code_.core_CORERelativity(
        probabilisticValue=complex(-66.7, 904.51), core_CORERelativity114=var_7
    )
    assert isinstance(var_10, python_code_.core_CORERelativity)
    python_code_.core_CORERelativity(
        probabilisticValue=(1, 1174.24, "mta4:rUkZp;i-R"), core_CORERelativity=var_9
    )
    var_13 = 20.990379344949755
    python_code_.core_LayoutElement(x=var_13, y=var_5, core_LayoutElement=var_5)
    python_code_.core_COREWeightedMapping(
        weight={
            "!VbB:LONWJg/Il3T9": True,
            '1Nl h)\rcxQ-@N\ts{_B"': -2790.46,
            '{,9x${+XA=4"y,~G\n': "core_COREFeature28,core_COREFeatureImpactNode106,public,core_COREFeature28",
        },
        core_COREWeightedMapping=var_5,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_20 = "R^"
    var_21 = "_core_COREFeature__core_COREFeature29"
    var_22 = python_code_.core_COREInterface()
    var_23 = python_code_.core_COREModelElement(
        partiality=var_20, visibility=var_21, core_COREModelElement42=var_22
    )
    assert isinstance(var_23, python_code_.core_COREModelElement)
    var_24 = python_code_.core_CORERelativity_Opt2
    python_code_.core_COREWeightedMapping(
        weight={
            "!VbB:LONWJg/Il3T9": True,
            '1Nl h)\rcxQ-@N\ts{_B"': -2790.46,
            '{,9x${+XA=4"y,~G\n': "core_COREFeature28,core_COREFeatureImpactNode106,public,core_COREFeature28",
        },
        core_COREWeightedMapping=var_24,
    )
    var_27 = python_code_.core_COREConfiguration()
    var_29 = set()
    var_30 = python_code_.core_COREFeatureModel()
    var_31 = python_code_.core_COREFeature(
        parentRelationship={},
        COREFeature22=b"n",
        children=True,
        core_COREFeature39=b'"',
        source=var_29,
        core_COREFeature77=var_30,
        core_COREFeature68=var_27,
        COREFeature118=var_21,
    )
    assert isinstance(var_31, python_code_.core_COREFeature)
    python_code_.core_CORERelativity_Opt2(
        probabilisticValue=376.26, incoming120=var_31, outgoing117=None
    )


def test_8():
    var_20 = "R^"
    var_21 = "_core_COREFeature__core_COREFeature29"
    var_22 = python_code_.core_COREInterface()
    var_23 = python_code_.core_COREModelElement(
        partiality=var_20, visibility=var_21, core_COREModelElement42=var_22
    )
    assert isinstance(var_23, python_code_.core_COREModelElement)
    var_24 = python_code_.core_CORERelativity_Opt2
    var_27 = python_code_.core_COREConfiguration()
    var_29 = {var_27}
    var_30 = python_code_.core_COREFeatureModel()
    var_31 = python_code_.core_COREFeature(
        parentRelationship={},
        COREFeature22=b"n",
        children=True,
        core_COREFeature39=b'"',
        source=var_29,
        core_COREFeature77=var_30,
        core_COREFeature68=var_27,
        COREFeature118=var_21,
    )
    assert isinstance(var_31, python_code_.core_COREFeature)
    python_code_.core_CORERelativity_Opt2(probabilisticValue=2801.93)
    var_37 = 1355
    python_code_.core_COREWeightedMapping(weight=var_37)
    var_35 = python_code_.core_CORERelativity_Opt2(
        probabilisticValue=("M3I5ZV\\OKj", -1856, 2),
        CORERelativity_Opt2=var_31,
        CORERelativity_Opt236=var_24,
        incoming120=var_24,
    )
    assert isinstance(var_35, python_code_.core_CORERelativity_Opt2)


def test_9():
    var_0 = python_code_.core_COREWeightedMapping(weight=1)
    var_2 = python_code_.core_COREModelElement(partiality=var_0, visibility=var_0)
    assert isinstance(var_2, python_code_.core_COREModelElement)


def test_10():
    var_11 = "Rr7JB\nvFlE{l}4"
    var_12 = "_core_COREFeature__core_COREFeature29"
    var_13 = python_code_.core_COREInterface()
    var_14 = python_code_.core_COREModelElement(
        partiality=var_11,
        visibility="_core_COREFeature__children _core_COREFeature__COREFeature _core_COREFeature__core_COREFeature80",
        core_COREModelElement=var_12,
        core_COREModelElement42=var_13,
        core_COREModelElement45=var_13,
    )
    assert isinstance(var_14, python_code_.core_COREModelElement)
    var_15 = python_code_.core_CORERelativity_Opt2
    python_code_.core_COREWeightedMapping(
        weight={
            "!VbB:LONWJg/Il3T9": True,
            '1Nl h)\rcxQ-@N\ts{_B"': -2790.46,
            '{,9x${+XA=4"y,~G\n': "core_COREFeature28,core_COREFeatureImpactNode106,public,core_COREFeature28",
        },
        core_COREWeightedMapping=var_15,
    )


def test_11():
    var_13 = python_code_.core_COREBinding()
    var_16 = python_code_.core_COREImpactModel()
    var_17 = lambda *args, **kwargs: -403
    var_18 = python_code_.core_COREModelElement(
        partiality=var_16, visibility=var_17, core_COREModelElement45=var_13
    )
    assert isinstance(var_18, python_code_.core_COREModelElement)


@pytest.mark.xfail(strict=True)
def test_12():
    python_code_.core_COREWeightedMapping(weight=1)
    var_2 = 4049.36
    var_3 = float
    var_4 = python_code_.core_COREConfiguration()
    python_code_.core_COREFeature(
        parentRelationship=var_2,
        realizes=var_3,
        core_COREFeature68=(">gK!v/chubscj6ZS/^",),
        core_COREFeature71=var_4,
    )


def test_13():
    var_21 = python_code_.core_COREConfiguration()
    var_22 = "68rPI?u\\]~1]`3XwH#"
    var_23 = set()
    var_24 = python_code_.core_COREFeatureModel()
    var_25 = python_code_.core_COREFeature(
        parentRelationship={},
        COREFeature22=b"n",
        children=True,
        core_COREFeature39=b'"',
        source=var_23,
        core_COREFeature77=var_24,
        core_COREFeature68=var_21,
        COREFeature118=var_22,
    )
    assert isinstance(var_25, python_code_.core_COREFeature)


def test_14():
    var_0 = python_code_.core_COREModelCompositionSpecification()
    var_4 = python_code_.CORENamedElement()
    var_7 = python_code_.core_COREReuse()
    var_8 = python_code_.core_COREReuse()
    var_9 = {var_7, var_8}
    var_10 = "\x0c\rv\nily'PzEOH!["
    var_11 = python_code_.core_COREConfiguration()
    var_12 = python_code_.core_COREFeature(
        parentRelationship=var_10,
        core_COREFeature=[],
        children={},
        core_COREFeature26=var_9,
        core_COREFeature31=complex(1900.3508708, 2812.0),
        core_COREFeature71=var_11,
        COREFeature118=var_0,
    )
    assert isinstance(var_12, python_code_.core_COREFeature)
    var_13 = python_code_.core_COREFeature(
        parentRelationship=var_9,
        core_COREFeature=var_9,
        parent=["*o>\\\\_3#C", 9.14, "s"],
        core_COREFeature28=var_12,
        core_COREFeature31=var_4,
        core_COREFeature29=var_9,
        core_COREFeature115=var_9,
    )
    assert isinstance(var_13, python_code_.core_COREFeature)


@pytest.mark.xfail(strict=True)
def test_15():
    var_0 = python_code_.COREConfiguration()
    var_1 = python_code_.core_COREInterface()
    var_2 = python_code_.core_COREModelElement(
        partiality=var_0,
        visibility=2,
        core_COREModelElement42=var_0,
        core_COREModelElement45=var_1,
    )
    assert isinstance(var_2, python_code_.core_COREModelElement)
    var_3 = -2037.74
    var_4 = python_code_.core_COREImpactNode(
        scalingFactor=var_3, offset=var_3, core_COREImpactNode48={True}
    )
    assert isinstance(var_4, python_code_.core_COREImpactNode)
    python_code_.core_COREContribution(
        relativeWeight=complex(1574.475452, 5482.4807),
        COREContribution=[-4034.34, 2393.79, False],
    )
    var_14 = python_code_.core_COREContribution
    python_code_.core_COREModelElement(partiality=var_14, visibility=var_14)
    python_code_.core_COREImpactNode(scalingFactor=(False, True), offset=var_14)
    var_20 = python_code_.core_COREConcern()
    var_27 = "core_CORERelativity_Opt2 _core_COREFeature__children _core_COREModelElement__core_COREModelElement42 _core_COREFeature__realizes"
    var_28 = 506.76
    var_29 = python_code_.core_COREFeatureModel()
    var_30 = python_code_.core_CORERelativity_Opt2(
        probabilisticValue=var_28, core_CORERelativity_Opt2=var_29, incoming120=var_14
    )
    var_31 = {var_30}
    python_code_.core_COREFeature(
        parentRelationship=var_27,
        COREFeature22=var_27,
        COREFeature25=var_20,
        core_COREFeature33=-658.84,
        features=var_31,
        COREFeature118=var_27,
    )


@pytest.mark.xfail(strict=True)
def test_16():
    var_0 = python_code_.core_COREModel()
    var_1 = {var_0}
    var_2 = object
    var_3 = python_code_.core_COREFeatureModel()
    var_4 = python_code_.core_COREFeatureImpactNode(relativeFeatureWeight=-1184)
    assert isinstance(var_4, python_code_.core_COREFeatureImpactNode)
    var_5 = "core_COREInterfacecore_COREContributioncore_COREInterface44_core_COREImpactNode__core_COREImpactNode"
    var_6 = python_code_.core_COREConfiguration()
    var_7 = python_code_.core_COREFeature(
        parentRelationship=var_5,
        core_COREFeature=var_1,
        COREFeature25=[False, True],
        source=var_1,
        features=var_1,
        core_COREFeature77=var_3,
        core_COREFeature68=var_6,
        core_COREFeature115=var_2,
        COREFeature118={},
    )
    assert isinstance(var_7, python_code_.core_COREFeature)
    python_code_.core_COREFeature(
        parentRelationship=var_5,
        core_COREFeature=var_1,
        COREFeature=var_0,
        core_COREFeature28=var_7,
        source=b"\xda\xcc;-",
        core_COREFeature80=var_2,
        core_COREFeature104=var_4,
        core_COREFeature68=var_6,
    )


def test_17():
    var_28 = -2632.24
    var_29 = python_code_.core_CORERelativity(probabilisticValue=var_28)
    assert isinstance(var_29, python_code_.core_CORERelativity)


@pytest.mark.xfail(strict=True)
def test_18():
    var_10 = -3825.57
    var_17 = set()
    var_18 = lambda *args, **kwargs: [2, 2799.81]
    var_19 = python_code_.core_COREContribution(relativeWeight=var_18)
    python_code_.core_COREImpactNode(
        scalingFactor=var_10,
        offset=(1166, -1546, "i]nY6nJb\\d"),
        source63=var_17,
        COREImpactNode93=var_19,
    )


def test_19():
    var_5 = 4072.4404746059076
    var_8 = 11
    var_9 = python_code_.core_COREWeightedMapping(weight=var_8)
    var_10 = {var_9, var_9, var_9}
    var_11 = python_code_.core_COREFeatureImpactNode(
        relativeFeatureWeight=-758.02, core_COREFeatureImpactNode106=var_10
    )
    assert isinstance(var_11, python_code_.core_COREFeatureImpactNode)
    var_16 = python_code_.core_COREImpactNode(
        scalingFactor=1155.6,
        offset=var_5,
        core_COREImpactNode=None,
        core_COREImpactNode48=None,
        COREImpactNode93=None,
        impacts=var_10,
    )
    assert isinstance(var_16, python_code_.core_COREImpactNode)


def test_20():
    var_2 = python_code_.core_COREMapping()
    var_5 = -3825.57
    var_6 = 1289.86
    var_7 = python_code_.core_LayoutElement(x=var_5, y=var_6)
    var_8 = python_code_.core_COREInterface()
    var_9 = python_code_.core_COREImpactNode(
        scalingFactor=var_6,
        offset=var_7,
        core_COREImpactNode48=var_8,
        COREImpactNode=var_2,
    )
    assert isinstance(var_9, python_code_.core_COREImpactNode)


@pytest.mark.xfail(strict=True)
def test_21():
    var_21 = 1881.87
    var_22 = 496.66
    var_23 = python_code_.core_COREContribution(relativeWeight=1039.5, incoming=set())
    var_24 = {var_23, var_23}
    python_code_.core_COREImpactNode(
        scalingFactor=var_21,
        offset=var_22,
        source63=var_24,
        COREImpactNode=var_23,
        COREImpactNode93=1,
    )


@pytest.mark.xfail(strict=True)
def test_22():
    var_0 = python_code_.COREImpactNode()
    var_5 = 4049.36
    python_code_.core_COREImpactNode(
        scalingFactor=var_5, offset={2379}, core_COREImpactNode=var_5, impacts=var_0
    )


def test_23():
    python_code_.core_COREWeightedMapping(weight=1729)
    var_3 = -1821
    var_4 = hash
    python_code_.core_COREContribution(
        relativeWeight=var_3, core_COREContribution=var_4, COREContribution65=var_4
    )


def test_24():
    python_code_.core_COREWeightedMapping(weight=1729)
    python_code_.core_COREContribution(relativeWeight=0, incoming=None)


def test_25():
    var_2 = float
    var_5 = 3
    var_6 = python_code_.core_COREImpactModel()
    python_code_.core_COREContribution(
        relativeWeight=var_5, core_COREContribution=var_6, outgoing=var_2, incoming=[]
    )


def test_26():
    var_0 = 711.35
    python_code_.core_LayoutElement(x=var_0, y={-2849})
    var_2 = python_code_.core_CORENamedElement(name={})
    assert isinstance(var_2, python_code_.core_CORENamedElement)
    var_6 = abs
    python_code_.core_COREContribution(relativeWeight=var_6, COREContribution65=var_2)
    var_46 = python_code_.core_COREInterface
    python_code_.core_COREWeightedMapping(
        weight={
            "!VbB:LONWJg/Il3T9": True,
            '1Nl h)\rcxQ-@N\ts{_B"': -2790.46,
            '{,9x${+XA=4"y,~G\n': "core_COREFeature28,core_COREFeatureImpactNode106,public,core_COREFeature28",
        },
        core_COREWeightedMapping=var_46,
    )


def test_27():
    var_0 = -469
    var_1 = 1801.83
    var_2 = python_code_.core_COREImpactNode(scalingFactor=var_1, offset="public")
    assert isinstance(var_2, python_code_.core_COREImpactNode)
    var_3 = python_code_.core_COREContribution(
        relativeWeight=var_0, COREContribution65=var_2
    )
    assert isinstance(var_3, python_code_.core_COREContribution)
    var_6 = -1201
    var_7 = python_code_.core_COREFeatureImpactNode(
        relativeFeatureWeight=var_6, core_COREFeatureImpactNode=var_3
    )
    assert isinstance(var_7, python_code_.core_COREFeatureImpactNode)


@pytest.mark.xfail(strict=True)
def test_28():
    var_22 = python_code_.COREModel()
    var_24 = python_code_.core_COREImpactModel()
    var_25 = float
    var_26 = -518.12
    var_27 = python_code_.core_COREInterface()
    var_28 = python_code_.core_COREImpactNode(
        scalingFactor=var_26,
        offset=569.37,
        core_COREImpactNode=var_24,
        core_COREImpactNode48=var_27,
        COREImpactNode93=var_25,
    )
    assert isinstance(var_28, python_code_.core_COREImpactNode)
    python_code_.core_COREContribution(
        relativeWeight=var_22,
        COREContribution=var_25,
        core_COREContribution=var_24,
        outgoing=var_28,
    )


def test_29():
    var_7 = python_code_.core_COREPattern
    python_code_.core_COREWeightedMapping(weight=var_7)
    var_18 = 2490.3
    var_19 = python_code_.core_CORERelativity(
        probabilisticValue=var_18, core_CORERelativity=var_7
    )
    assert isinstance(var_19, python_code_.core_CORERelativity)


def test_30():
    var_3 = python_code_.COREImpactNode()
    var_14 = len
    var_17 = python_code_.core_CORERelativity(
        probabilisticValue=var_14, core_CORERelativity114=var_3
    )
    assert isinstance(var_17, python_code_.core_CORERelativity)


@pytest.mark.xfail(strict=True)
def test_31():
    var_7 = python_code_.core_CORERelativity_Opt2
    python_code_.core_COREWeightedMapping(
        weight={
            "!VbB:LONWJg/Il3T9": True,
            '1Nl h)\rcxQ-@N\ts{_B"': -2790.46,
            '{,9x${+XA=4"y,~G\n': "core_COREFeature28,core_COREFeatureImpactNode106,public,core_COREFeature28",
        },
        core_COREWeightedMapping=var_7,
    )
    var_9 = python_code_.COREModel()
    var_19 = python_code_.core_COREInterface()
    var_24 = python_code_.core_CORERelativity_Opt2(
        probabilisticValue=-2235, core_CORERelativity_Opt2=var_19, outgoing117=None
    )
    python_code_.core_COREFeature(
        parentRelationship=var_7,
        COREFeature25=3925,
        core_COREFeature77=var_9,
        COREFeature118=var_24,
    )


def test_32():
    var_0 = 2226.7
    var_57 = python_code_.COREModel()
    var_59 = -1492.86
    var_62 = complex
    var_64 = python_code_.core_COREFeatureModel()
    var_68 = python_code_.core_CORERelativity(
        probabilisticValue=var_0, core_CORERelativity=var_62
    )
    assert isinstance(var_68, python_code_.core_CORERelativity)
    var_69 = set()
    var_70 = python_code_.core_COREFeature(
        parentRelationship=var_59,
        core_COREFeature=var_69,
        COREFeature22=complex(-362.026, -3301.0),
        core_COREFeature31=(True, "Z\x0bk \\z"),
        source=var_69,
        core_COREFeature77=var_64,
        core_COREFeature104=var_57,
    )
    assert isinstance(var_70, python_code_.core_COREFeature)


@pytest.mark.xfail(strict=True)
def test_33():
    var_0 = 2226.7
    python_code_.core_LayoutElement(x=None, y=var_0)
    var_4 = "_core_COREFeature__core_COREFeature29"
    var_7 = python_code_.core_CORERelativity_Opt2
    var_8 = python_code_.core_COREWeightedMapping(
        weight={
            "!VbB:LONWJg/Il3T9": True,
            '1Nl h)\rcxQ-@N\ts{_B"': -2790.46,
            '{,9x${+XA=4"y,~G\n': "core_COREFeature28,core_COREFeatureImpactNode106,public,core_COREFeature28",
        },
        core_COREWeightedMapping=var_7,
    )
    var_10 = python_code_.core_COREConfiguration()
    var_11 = "68rPI?u\\]~1]`3XwH#"
    var_12 = set()
    var_13 = python_code_.core_COREFeatureModel()
    var_14 = python_code_.core_COREFeature(
        parentRelationship={},
        COREFeature22=b"n",
        children=True,
        core_COREFeature39=b'"',
        source=var_12,
        core_COREFeature77=var_13,
        core_COREFeature68=var_10,
        COREFeature118=var_4,
    )
    assert isinstance(var_14, python_code_.core_COREFeature)
    var_15 = python_code_.core_CORERelativity_Opt2(probabilisticValue=var_8)
    python_code_.core_COREFeature(
        parentRelationship=var_11,
        COREFeature=2285,
        core_COREFeature28=(),
        core_COREFeature31=var_14,
        source=var_12,
        core_COREFeature77={},
        COREFeature118=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = python_code_.core_COREModelCompositionSpecification()
    var_4 = python_code_.CORENamedElement()
    var_7 = python_code_.core_COREReuse()
    var_8 = python_code_.core_COREReuse()
    var_9 = {var_7, var_8}
    var_10 = "\x0c\rv\nily'PzEOH!["
    var_11 = python_code_.core_COREConfiguration()
    var_12 = python_code_.core_COREFeature(
        parentRelationship=var_10,
        core_COREFeature=[],
        children={},
        core_COREFeature26=var_9,
        core_COREFeature31=complex(1900.3508708, 2812.0),
        core_COREFeature71=var_11,
        COREFeature118=var_0,
    )
    assert isinstance(var_12, python_code_.core_COREFeature)
    var_13 = python_code_.core_COREFeature(
        parentRelationship=var_9,
        core_COREFeature=var_9,
        parent=["*o>\\\\_3#C", 9.14, "s"],
        core_COREFeature28=var_12,
        core_COREFeature31=var_4,
        core_COREFeature29=var_9,
        core_COREFeature115=var_9,
    )
    assert isinstance(var_13, python_code_.core_COREFeature)
    var_14 = len
    var_15 = {var_12, var_12, var_13}
    python_code_.core_COREFeature(
        parentRelationship={
            "_core_COREModelElement__core_COREModelElement42:concern:_core_COREImpactNode__COREImpactNode93": True
        },
        COREFeature22=var_12,
        parent=var_14,
        core_COREFeature26=var_15,
        core_COREFeature31=var_13,
        source=False,
        features={
            "B%<f!JS'ZTv": "impacts",
            "incoming core_COREModel2 incoming": 571.9,
            "features:core_LayoutMap:_core_COREFeature__parent": "core_COREFeatureModel79-core_CORERelativity114-core_COREModel2-_core_COREFeature__core_COREFeature31",
        },
    )


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = 0
    var_1 = python_code_.core_COREContribution(relativeWeight=var_0)
    var_2 = python_code_.core_LayoutContainerMap()
    var_3 = -2800.74
    var_4 = {var_1, var_1, var_1, var_1, var_1}
    var_5 = python_code_.core_COREImpactNode(
        scalingFactor=3, offset=var_3, impacts=var_4
    )
    assert isinstance(var_5, python_code_.core_COREImpactNode)
    var_7 = python_code_.core_COREPattern()
    var_8 = 'wF5;]"<ijG'
    python_code_.core_COREFeature(
        parentRelationship=var_8,
        realizes=var_5,
        parent="_core_COREFeature__core_COREFeature68:_core_COREFeature__children",
        COREFeature={},
        core_COREFeature26={},
        core_COREFeature31=var_7,
        core_COREFeature33=var_1,
        core_COREFeature80=var_2,
        COREFeature121=var_3,
        core_COREFeature71=var_2,
        core_COREFeature115=False,
    )


@pytest.mark.xfail(strict=True)
def test_36():
    var_0 = python_code_.core_COREModelCompositionSpecification()
    var_4 = python_code_.CORENamedElement()
    var_6 = "public:core_COREConfiguration70:core_COREInterface44:core_COREImpactModel"
    var_7 = python_code_.core_COREReuse()
    var_8 = python_code_.core_COREReuse()
    var_9 = {var_7, var_8}
    var_10 = "\x0c\rv\nily'PzEUH!["
    var_11 = python_code_.core_COREConfiguration()
    var_12 = python_code_.core_COREFeature(
        parentRelationship=var_10,
        core_COREFeature=[],
        children={},
        core_COREFeature26=var_9,
        core_COREFeature31=complex(1900.3508708, 2812.0),
        core_COREFeature71=var_11,
        COREFeature118=var_0,
    )
    assert isinstance(var_12, python_code_.core_COREFeature)
    python_code_.core_COREFeature(
        parentRelationship=var_6,
        core_COREFeature=var_9,
        parent=var_9,
        children=var_12,
        COREFeature=var_10,
        core_COREFeature28=var_12,
        core_COREFeature31=var_12,
        core_COREFeature33={var_12, True, var_4},
        features=var_9,
        core_COREFeature104=var_10,
        COREFeature121=None,
        COREFeature118=var_11,
    )
