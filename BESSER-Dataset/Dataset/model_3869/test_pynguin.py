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
    CORECompositionSpecification,
    COREFeatureRelationshipType,
    COREModel,
    COREModelElement,
    CORENamedElement,
    Enum,
    abstractmethod,
    core_COREBinding,
    core_CORECompositionSpecification,
    core_COREConcern,
    core_COREConfiguration,
    core_COREFeature,
    core_COREFeatureModel,
    core_COREImpactModel,
    core_COREImpactModelElement,
    core_COREInterface,
    core_COREMapping,
    core_COREModel,
    core_COREModelElement,
    core_CORENamedElement,
    core_COREPattern,
    core_COREReuse,
    core_COREStrategy,
    date,
    datetime,
    time,
)


def test_0():
    var_19 = python_code_.core_COREFeature(
        COREFeature=None, realizes={912}, core_COREFeature=set()
    )
    assert isinstance(var_19, python_code_.core_COREFeature)


def test_1():
    var_19 = python_code_.core_COREFeature(
        core_COREFeature11={
            "_core_COREFeature__realizescore_COREStrategy_core_COREFeature__core_COREFeature49_core_COREFeature__core_COREFeature11",
            False,
        },
        core_COREFeature43=None,
    )
    assert isinstance(var_19, python_code_.core_COREFeature)


def test_2():
    var_19 = python_code_.core_COREFeature(
        core_COREFeature={
            "_core_COREFeature__core_COREFeature26:core_COREReuse",
            474.33,
            -1683.56,
        },
        core_COREFeature11={947.16},
        core_COREFeature26=None,
    )
    assert isinstance(var_19, python_code_.core_COREFeature)


def test_3():
    var_19 = python_code_.core_COREFeature(
        core_COREFeature26=None, core_COREFeature49=None
    )
    assert isinstance(var_19, python_code_.core_COREFeature)


def test_4():
    var_25 = python_code_.core_COREFeature(
        core_COREFeature43=complex(-4066.0, 2107.68333)
    )
    assert isinstance(var_25, python_code_.core_COREFeature)


def test_5():
    var_28 = python_code_.core_COREFeature(core_COREFeature26=set())
    assert isinstance(var_28, python_code_.core_COREFeature)


def test_6():
    var_31 = python_code_.core_COREFeature(
        COREFeature=[
            "_core_COREFeature__core_COREFeature11,core_COREInterface25,_core_COREFeature__core_COREFeature11,OR",
            928,
            False,
        ],
        core_COREFeature26={
            "YjER0i11\x0biz$:p": 2875,
            "core_COREConfiguration:core_COREReuse42": -214,
            "z1/[GeV<vL*": 2109.74,
        },
    )
    assert isinstance(var_31, python_code_.core_COREFeature)
    var_31.rename(core_core_feature_name=[])


def test_7():
    var_41 = python_code_.core_COREFeature(core_COREFeature49=())
    assert isinstance(var_41, python_code_.core_COREFeature)


def test_8():
    python_code_.core_COREPattern()


def test_9():
    var_30 = python_code_.core_CORENamedElement(name=False)
    assert isinstance(var_30, python_code_.core_CORENamedElement)


def test_10():
    python_code_.core_COREFeatureModel()


def test_11():
    var_0 = python_code_.core_COREFeatureModel()
    var_0.getLocalRoot()


def test_12():
    var_28 = python_code_.core_COREFeature(core_COREFeature26=set())
    assert isinstance(var_28, python_code_.core_COREFeature)
    var_30 = python_code_.core_COREFeatureModel()
    var_30.getGlobalRoot()


def test_13():
    var_25 = python_code_.core_COREFeature(
        core_COREFeature43=complex(-4066.0, 2107.68333)
    )
    assert isinstance(var_25, python_code_.core_COREFeature)
    var_25.excludes(core_feature=var_25)


def test_14():
    var_25 = python_code_.core_COREFeature(
        core_COREFeature43=complex(-4066.0, 2107.68333)
    )
    assert isinstance(var_25, python_code_.core_COREFeature)
    var_25.changeLink(core_new_association=())


def test_15():
    var_25 = python_code_.core_COREFeature(
        core_COREFeature43=complex(-4066.0, 2107.68333)
    )
    assert isinstance(var_25, python_code_.core_COREFeature)
    var_25.addRealizedBy(core_model=var_25)


def test_16():
    var_25 = python_code_.core_COREFeature(
        core_COREFeature43=complex(-4066.0, 2107.68333)
    )
    assert isinstance(var_25, python_code_.core_COREFeature)
    var_25.requires(core_feature=var_25)


def test_17():
    var_25 = python_code_.core_COREFeature(
        core_COREFeature43=complex(-4066.0, 2107.68333)
    )
    assert isinstance(var_25, python_code_.core_COREFeature)
    var_25.addFeature(
        core_association=complex(1991.657, -59.478),
        core_child_name=complex(2574.16, 2403.032099),
    )


def test_18():
    var_25 = python_code_.core_COREFeature(
        core_COREFeature43=complex(-4066.0, 2107.68333)
    )
    assert isinstance(var_25, python_code_.core_COREFeature)
    var_25.delete()


def test_19():
    var_25 = python_code_.core_COREFeature(
        core_COREFeature43=complex(-4066.0, 2107.68333)
    )
    assert isinstance(var_25, python_code_.core_COREFeature)
    var_25.removeConstraint(core_feature=set())


def test_20():
    var_41 = python_code_.core_COREFeature(core_COREFeature49=())
    assert isinstance(var_41, python_code_.core_COREFeature)
    var_41.changeParent(core_feature=4007, core_new_association=var_41)
