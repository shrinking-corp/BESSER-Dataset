#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    AbstractFeature,
    Actor,
    ApplicationDomainUseCase,
    Asset,
    AssociationClassElement,
    Danger,
    Enum,
    Feature,
    FunctionalRequirement,
    Goal,
    GoalReference,
    GoalReferenceType,
    GoalType,
    MEDiagram,
    Mitigation,
    NonDomainElement,
    NonFunctionalRequirement,
    Product,
    Requirement,
    Service,
    SolutionDomainUseCase,
    Step,
    UnicaseModelElement,
    UrmlModelElement,
    UseCase,
    VariationPoint,
    VariationPointInstance,
    abstractmethod,
    date,
    datetime,
    goal_urml_Stakeholder,
    time,
    urml_EClass,
    urml_EStructuralFeature,
    urml_Phase,
    urml_PhaseSetEntry,
    urml_SetEntry,
    urml_Stakeholder,
    urml_StakeholderRole,
    urml_URMLDiagram,
    urml_UrmlModelElement,
    urml_UrmlProjectSettings,
    urml_danger_Asset,
    urml_danger_Danger,
    urml_danger_Mitigation,
    urml_danger_ProceduralMitigation,
    urml_feature_AbstractFeature,
    urml_feature_Feature,
    urml_feature_Product,
    urml_feature_VariationPoint,
    urml_feature_VariationPointInstance,
    urml_goal_Goal,
    urml_goal_GoalReference,
    urml_requirement_FunctionalRequirement,
    urml_requirement_NonFunctionalRequirement,
    urml_requirement_Requirement,
    urml_service_Service,
    urml_usecase_Actor,
    urml_usecase_ApplicationDomainUseCase,
    urml_usecase_SolutionDomainUseCase,
    urml_usecase_UseCase,
)


def test_0():
    var_7 = python_code_.urml_requirement_Requirement(
        terminal=True, satisfiedRequirements=set()
    )
    assert isinstance(var_7, python_code_.urml_requirement_Requirement)


def test_1():
    var_5 = python_code_.urml_requirement_Requirement(terminal=True)
    assert isinstance(var_5, python_code_.urml_requirement_Requirement)


def test_2():
    var_13 = python_code_.urml_feature_VariationPoint(
        multiplicity=-3467,
        optionalParentVariationPoint={-2516.44, -1842.82},
        AbstractFeature82=None,
        AbstractFeature42=None,
        AbstractFeature91=None,
        AbstractFeature37=None,
        AbstractFeature=None,
        AbstractFeature80=None,
    )
    assert isinstance(var_13, python_code_.urml_feature_VariationPoint)


def test_3():
    var_13 = python_code_.urml_feature_VariationPoint(
        multiplicity=3,
        AbstractFeature84=None,
        AbstractFeature78=None,
        AbstractFeature76=None,
    )
    assert isinstance(var_13, python_code_.urml_feature_VariationPoint)


def test_4():
    var_13 = python_code_.urml_feature_VariationPoint(
        multiplicity=-1566,
        optionalParentVariationPoint=set(),
        variationPoint=set(),
        AbstractFeature82=None,
        AbstractFeature78=None,
        AbstractFeature91=None,
        AbstractFeature37=None,
        AbstractFeature80=None,
    )
    assert isinstance(var_13, python_code_.urml_feature_VariationPoint)


def test_5():
    var_8 = python_code_.urml_goal_Goal(
        soft=True, type=")]zZdieZ\\6q2", target=set(), goals=set(), parentGoal=set()
    )
    assert isinstance(var_8, python_code_.urml_goal_Goal)


def test_6():
    var_8 = python_code_.urml_goal_Goal(soft=False, type="\tej$eKZ+", source=set())
    assert isinstance(var_8, python_code_.urml_goal_Goal)


def test_7():
    var_8 = python_code_.urml_goal_Goal(
        soft=False,
        type="_urml_goal_Goal__parentGoal:_urml_feature_VariationPoint__optionalParentVariationPoint:goal_urml_Stakeholder",
        goals={True, -1220.0, 3},
        source=set(),
        goals22=set(),
        detailedGoal=None,
    )
    assert isinstance(var_8, python_code_.urml_goal_Goal)


def test_8():
    var_5 = python_code_.urml_goal_GoalReference(
        weight="urml_UrmlModelElement Stakeholder", influencingGoals=None
    )
    assert isinstance(var_5, python_code_.urml_goal_GoalReference)


def test_9():
    var_8 = python_code_.urml_UrmlModelElement(reviewed=False)
    assert isinstance(var_8, python_code_.urml_UrmlModelElement)


def test_10():
    python_code_.urml_usecase_ApplicationDomainUseCase()


def test_11():
    var_15 = python_code_.urml_danger_ProceduralMitigation(mitigationProcedure=-2862.63)
    assert isinstance(var_15, python_code_.urml_danger_ProceduralMitigation)


def test_12():
    var_11 = ":k~^t./lRA"
    var_12 = python_code_.urml_goal_Goal(
        soft=b"\x1a\xb5\xf7\xc0\x88(\x9b\xab\xb2D\xa8^\xcc\xaf\x0b\xad\x94\x99",
        type=var_11,
        source=var_11,
        detailedGoal=False,
    )
    assert isinstance(var_12, python_code_.urml_goal_Goal)


def test_13():
    var_16 = python_code_.Goal()
    var_17 = python_code_.urml_goal_GoalReference(
        weight=-385.87, influencedGoals=var_16, influencingGoals=var_16
    )
    assert isinstance(var_17, python_code_.urml_goal_GoalReference)


def test_14():
    var_17 = python_code_.urml_goal_GoalReference(
        weight=-705.96, influencedGoals=-1158.32
    )
    assert isinstance(var_17, python_code_.urml_goal_GoalReference)


def test_15():
    var_12 = python_code_.urml_UrmlModelElement(
        reviewed=complex(3088.73, -1099.9502), urml_UrmlModelElement=-802
    )
    assert isinstance(var_12, python_code_.urml_UrmlModelElement)


def test_16():
    var_8 = python_code_.urml_UrmlModelElement(
        reviewed=False, urml_UrmlModelElement0={"Yt'\rn1luz|IR"}
    )
    assert isinstance(var_8, python_code_.urml_UrmlModelElement)


def test_17():
    var_2 = python_code_.urml_feature_Feature()
    var_6 = python_code_.urml_goal_Goal(
        soft=False,
        type="S\rl0e",
        target={var_2},
        goals22={var_2, var_2},
        subGoals=var_2,
    )
    assert isinstance(var_6, python_code_.urml_goal_Goal)


def test_18():
    var_10 = python_code_.urml_UrmlModelElement(reviewed=True)
    assert isinstance(var_10, python_code_.urml_UrmlModelElement)
    var_12 = python_code_.urml_UrmlModelElement(
        reviewed=True, urml_UrmlModelElement=var_10
    )
    assert isinstance(var_12, python_code_.urml_UrmlModelElement)


def test_19():
    var_6 = python_code_.urml_UrmlModelElement(
        reviewed=True, urml_UrmlModelElement=None
    )
    assert isinstance(var_6, python_code_.urml_UrmlModelElement)
    var_7 = {var_6, var_6, var_6, var_6}
    var_8 = python_code_.urml_UrmlModelElement(
        reviewed=False, urml_UrmlModelElement0=var_7
    )
    assert isinstance(var_8, python_code_.urml_UrmlModelElement)
    var_10 = {"_urml_goal_Goal__detailedGoal", var_6}
    var_11 = python_code_.urml_UrmlModelElement(
        reviewed=[-4589, -2592.29], urml_UrmlModelElement0=var_10
    )
    assert isinstance(var_11, python_code_.urml_UrmlModelElement)


def test_20():
    var_5 = python_code_.urml_goal_GoalReference(
        weight=",lfrz\nJ\tF", influencingGoals=None
    )
    assert isinstance(var_5, python_code_.urml_goal_GoalReference)
    var_10 = python_code_.urml_UrmlProjectSettings()
    var_11 = False
    var_12 = python_code_.urml_UrmlModelElement(reviewed=set())
    assert isinstance(var_12, python_code_.urml_UrmlModelElement)
    var_13 = {var_12}
    var_14 = python_code_.urml_UrmlModelElement(
        reviewed=var_11, urml_UrmlModelElement0=var_13
    )
    assert isinstance(var_14, python_code_.urml_UrmlModelElement)
    var_15 = python_code_.urml_UrmlModelElement(
        reviewed=var_10,
        urml_UrmlModelElement=var_13,
        urml_UrmlModelElement0="AbstractFeature",
    )
    assert isinstance(var_15, python_code_.urml_UrmlModelElement)
    var_16 = {var_12, var_14, var_15, var_15, var_15}
    var_17 = python_code_.urml_UrmlModelElement(
        reviewed={"_urml_goal_GoalReference__influencingGoals": "Goal34"},
        urml_UrmlModelElement0=var_16,
    )
    assert isinstance(var_17, python_code_.urml_UrmlModelElement)


def test_21():
    var_8 = python_code_.urml_goal_Goal(soft=True, type="q(=ZFlnx|Ily5", goals=set())
    assert isinstance(var_8, python_code_.urml_goal_Goal)
    var_16 = python_code_.urml_danger_Danger()
    var_17 = False
    var_18 = python_code_.urml_UrmlModelElement(
        reviewed=var_17, urml_UrmlModelElement0="^7]F2xx=88Z'JU"
    )
    assert isinstance(var_18, python_code_.urml_UrmlModelElement)
    var_19 = {var_18}
    var_20 = python_code_.urml_UrmlModelElement(
        reviewed=var_16, urml_UrmlModelElement=var_18, urml_UrmlModelElement0=var_19
    )
    assert isinstance(var_20, python_code_.urml_UrmlModelElement)
