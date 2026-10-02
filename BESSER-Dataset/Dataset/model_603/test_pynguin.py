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
    Annotable,
    AssociationType,
    Enum,
    UIComponent,
    abstractmethod,
    date,
    datetime,
    mvc_Action,
    mvc_Association,
    mvc_Attribute,
    mvc_Component,
    mvc_Controller,
    mvc_ControllerView,
    mvc_Entity,
    mvc_Event,
    mvc_EventAction,
    mvc_MVCModel,
    mvc_Model,
    mvc_UIActions,
    mvc_UIComponent,
    mvc_UIInput,
    mvc_UILayout,
    mvc_View,
    time,
)


def test_0():
    var_21 = "gH?ub`UVLo&)5#l0X"
    var_22 = python_code_.mvc_UILayout(orientation=var_21, columns=[932, True])
    assert isinstance(var_22, python_code_.mvc_UILayout)


def test_1():
    var_19 = python_code_.mvc_UILayout(
        orientation="E/zP*co|",
        columns=-1,
        mvc_UILayout57={-486.55},
        mvc_UILayout59=set(),
    )
    assert isinstance(var_19, python_code_.mvc_UILayout)


def test_2():
    var_0 = python_code_.Annotable()
    var_16 = "\nds~\ns"
    var_17 = -2417
    var_18 = python_code_.mvc_Association(
        name=var_16,
        containment=var_17,
        lowerBound=complex(-1969.714, -3510.0),
        upperBound=var_0,
        type=var_16,
    )
    assert isinstance(var_18, python_code_.mvc_Association)
    var_20 = python_code_.mvc_Model(name=var_16, mvc_Model2={var_0}, mvc_Model46=var_16)
    assert isinstance(var_20, python_code_.mvc_Model)
    var_30 = python_code_.mvc_View(name=None)
    assert isinstance(var_30, python_code_.mvc_View)


def test_3():
    var_0 = False
    var_1 = python_code_.mvc_Action
    var_2 = "_mvc_Entity__mvc_Entity4"
    var_3 = python_code_.mvc_Association(
        name="mvc_UIComponent:mvc_Event34:mvc_Controller49",
        containment=var_0,
        lowerBound=var_0,
        upperBound=281,
        type=var_2,
        mvc_Association9=var_1,
        mvc_Association12=var_0,
    )
    assert isinstance(var_3, python_code_.mvc_Association)
    var_25 = python_code_.mvc_Model(name=var_2)
    assert isinstance(var_25, python_code_.mvc_Model)


def test_4():
    var_26 = "\nds~\ns"
    var_27 = -2434
    var_28 = "|Pg\\;J`"
    var_29 = python_code_.mvc_Association(
        name=[],
        containment=complex(-1113.0822, 2972.463396),
        lowerBound=var_27,
        upperBound=var_28,
        type=var_26,
    )
    assert isinstance(var_29, python_code_.mvc_Association)
    var_30 = {var_29, var_29, var_29}
    var_31 = python_code_.mvc_Model(name=var_28, mvc_Model2=var_30)
    assert isinstance(var_31, python_code_.mvc_Model)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = python_code_.Annotable()
    var_1 = lambda *args, **kwargs: 3
    var_2 = "\nds~\ns"
    var_3 = -2434
    var_4 = python_code_.mvc_Association(
        name=var_2,
        containment=var_3,
        lowerBound=complex(-1969.714, -3510.0),
        upperBound=var_0,
        type=var_2,
    )
    assert isinstance(var_4, python_code_.mvc_Association)
    var_5 = python_code_.mvc_MVCModel(version=var_1, name=var_2)
    assert isinstance(var_5, python_code_.mvc_MVCModel)
    var_6 = python_code_.mvc_Model(name=142, mvc_Model16=var_5)
    assert isinstance(var_6, python_code_.mvc_Model)
    python_code_.mvc_Entity(
        name=var_2, mvc_Entity4="#-zDHUJc67rT)6-", mvc_Entity10=var_4, mvc_Entity=var_6
    )


def test_6():
    var_0 = len
    var_1 = "\x0c0|}lR2"
    var_2 = "mvc_Entity mvc_EventAction54 _mvc_Entity__mvc_Entity13 mvc_Entity4"
    var_3 = '6;;\x0c_4jl&:][qf_"C'
    var_4 = "{[4S_=X'"
    var_5 = set()
    var_6 = python_code_.mvc_MVCModel(
        version=var_3, name=var_4, mvc_MVCModel=var_2, mvc_MVCModel21=var_5
    )
    assert isinstance(var_6, python_code_.mvc_MVCModel)
    var_7 = python_code_.mvc_Model(name=var_2, mvc_Model16=var_6)
    assert isinstance(var_7, python_code_.mvc_Model)
    var_8 = python_code_.mvc_Association(
        name=var_0,
        containment=complex(740.1099167, 1585.020053),
        lowerBound=var_0,
        upperBound=var_0,
        type=var_1,
        mvc_Association=var_7,
        mvc_Association9=var_3,
    )
    assert isinstance(var_8, python_code_.mvc_Association)
    var_9 = "mvc_Controller"
    var_10 = "mvc_Event40mvc_MVCModel23"
    var_11 = python_code_.mvc_MVCModel(
        version=var_9,
        name=var_10,
        mvc_MVCModel18=var_5,
        mvc_MVCModel21=var_5,
        mvc_MVCModel23=var_4,
    )
    assert isinstance(var_11, python_code_.mvc_MVCModel)
    var_12 = "[-@k|$}A\x0b2-NHv#p"
    var_13 = python_code_.mvc_EventAction()
    var_14 = python_code_.mvc_Action(name=var_12, mvc_Action52=var_13, mvc_Action36=[])
    assert isinstance(var_14, python_code_.mvc_Action)
    python_code_.mvc_Model(name={"K7~=7<btb<2a[7ok", 3191}, mvc_Model16=var_11)
    var_18 = "FSgc4"
    var_19 = python_code_.mvc_Component(name=var_18)
    assert isinstance(var_19, python_code_.mvc_Component)
    var_21 = python_code_.mvc_EventAction()
    var_22 = python_code_.mvc_Event(name=var_1, mvc_Event55=var_21, mvc_Event40=var_0)
    assert isinstance(var_22, python_code_.mvc_Event)


def test_7():
    var_9 = python_code_.mvc_MVCModel(
        version="f>/;jvK=D2\t;", name="mvc_Event40", mvc_MVCModel18={False, False}
    )
    assert isinstance(var_9, python_code_.mvc_MVCModel)


def test_8():
    var_19 = "KNUBDl^(<ZVnwfn\tz"
    var_20 = python_code_.mvc_Controller(name=var_19)
    assert isinstance(var_20, python_code_.mvc_Controller)
    var_21 = {var_20, var_20, var_20, var_20, var_20}
    var_22 = python_code_.mvc_MVCModel(
        version=var_19, name=var_19, mvc_MVCModel23=var_21, mvc_MVCModel25=var_21
    )
    assert isinstance(var_22, python_code_.mvc_MVCModel)


def test_9():
    var_11 = hash
    var_12 = python_code_.mvc_View(name=var_11, mvc_View=1960)
    assert isinstance(var_12, python_code_.mvc_View)
    var_14 = {var_12, var_12, var_12}
    var_15 = python_code_.mvc_MVCModel(
        version=(),
        name=b"\x13RvDys\x9d-\x85i\x08\rYS\xd9\x0c",
        mvc_MVCModel18=var_14,
        mvc_MVCModel21=b"@\x86\xd6;\\\x0fp\xac\x84L",
        mvc_MVCModel23=var_14,
    )
    assert isinstance(var_15, python_code_.mvc_MVCModel)


def test_10():
    var_0 = python_code_.mvc_Action(name="7PR[&", mvc_Action36=None, mvc_Action39=set())
    assert isinstance(var_0, python_code_.mvc_Action)


def test_11():
    var_0 = python_code_.mvc_Action(name="g", mvc_Action36=None)
    assert isinstance(var_0, python_code_.mvc_Action)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.mvc_Action(name="7PR[&", mvc_Action36=None, mvc_Action39=set())
    assert isinstance(var_0, python_code_.mvc_Action)
    python_code_.mvc_Event(name="_INLzG_qbGu", mvc_Event37=var_0)


def test_13():
    var_17 = "z"
    var_18 = python_code_.mvc_Entity(name=var_17, mvc_Entity7=None)
    assert isinstance(var_18, python_code_.mvc_Entity)
    var_20 = python_code_.mvc_Action(name="1M@S9MXh", mvc_Action36=var_18)
    assert isinstance(var_20, python_code_.mvc_Action)


def test_14():
    var_17 = "+6"
    var_18 = python_code_.mvc_Entity(name=var_17, mvc_Entity7=None)
    assert isinstance(var_18, python_code_.mvc_Entity)
    var_20 = python_code_.mvc_Action(
        name=var_17, mvc_Action=var_17, mvc_Action52=var_18
    )
    assert isinstance(var_20, python_code_.mvc_Action)


@pytest.mark.xfail(strict=True)
def test_15():
    var_55 = True
    var_58 = ""
    var_59 = "\r8Y\tV_{k^<N:Rt=X\x0b"
    var_60 = python_code_.mvc_Controller(name=var_59, mvc_Controller27=set())
    assert isinstance(var_60, python_code_.mvc_Controller)
    var_61 = python_code_.mvc_Action(name=var_55, mvc_Action=var_60)
    assert isinstance(var_61, python_code_.mvc_Action)
    var_62 = int
    python_code_.mvc_Event(
        name=var_58,
        mvc_Event34=var_61,
        mvc_Event55=var_62,
        mvc_Event64=var_59,
        mvc_Event37=var_61,
    )


def test_16():
    var_0 = hash
    var_1 = python_code_.mvc_Controller(name=var_0, mvc_Controller=())
    assert isinstance(var_1, python_code_.mvc_Controller)


def test_17():
    var_16 = "_mvc_MVCModel__mvc_MVCodel18,mVc_UILayout"
    var_24 = True
    var_31 = python_code_.mvc_Controller(
        name=var_16,
        mvc_Controller49=None,
        mvc_Controller27={var_16, var_24, True},
        mvc_Controller29={"]h9+\rgR#!<?6Q4hQ"},
        mvc_Controller31=set(),
    )
    assert isinstance(var_31, python_code_.mvc_Controller)


def test_18():
    var_60 = python_code_.mvc_View(name=None)
    assert isinstance(var_60, python_code_.mvc_View)
    var_64 = lambda *args, **kwargs: []
    var_65 = python_code_.mvc_Component(name=var_64)
    assert isinstance(var_65, python_code_.mvc_Component)
    var_67 = "mvc_MVCModel21"
    var_68 = python_code_.mvc_Controller(
        name=var_67,
        mvc_Controller49=var_65,
        mvc_Controller=False,
        mvc_Controller31=var_67,
    )
    assert isinstance(var_68, python_code_.mvc_Controller)


def test_19():
    var_2 = python_code_.mvc_Controller(
        name="_mvc_Event__mvc_Event-_mvc_Entity__mvc_Entity4", mvc_Controller31=set()
    )
    assert isinstance(var_2, python_code_.mvc_Controller)


def test_20():
    var_2 = "\n@ds~\nZs"
    var_7 = python_code_.mvc_Entity(
        name=";y#\r4;0n5t/", mvc_Entity4=set(), mvc_Entity13=var_2
    )
    assert isinstance(var_7, python_code_.mvc_Entity)


def test_21():
    var_2 = "\nds~\nZs"
    var_7 = python_code_.mvc_Entity(name=var_2, mvc_Entity7=None)
    assert isinstance(var_7, python_code_.mvc_Entity)


def test_22():
    var_0 = python_code_.mvc_Controller(name=-697.16)
    assert isinstance(var_0, python_code_.mvc_Controller)
    var_4 = "_mvc_MVCModel__mvc_MVCModel18,mvc_UILayout"
    var_5 = python_code_.mvc_Entity(name=var_4, mvc_Entity13=-904.32)
    assert isinstance(var_5, python_code_.mvc_Entity)
    var_6 = python_code_.mvc_Entity(name=-589.42, mvc_Entity7=var_5)
    assert isinstance(var_6, python_code_.mvc_Entity)
    var_8 = python_code_.mvc_Component(name=var_4, mvc_Component=var_6)
    assert isinstance(var_8, python_code_.mvc_Component)
    var_9 = python_code_.mvc_UIActions
    python_code_.mvc_Entity(
        name=var_9,
        mvc_Entity4=b"\x01}t\xc0\x90\xdd\t0",
        mvc_Entity7=var_6,
        mvc_Entity10=2236.19,
    )


def test_23():
    var_16 = "_mvc_MVCModel__mvc_MVCModel18,mvc_UILayout"
    var_17 = python_code_.mvc_Entity(name=var_16, mvc_Entity13=-904.32)
    assert isinstance(var_17, python_code_.mvc_Entity)
    var_18 = python_code_.mvc_Entity(name=-589.42, mvc_Entity7=var_17)
    assert isinstance(var_18, python_code_.mvc_Entity)
    var_20 = python_code_.mvc_Component(name=var_16)
    assert isinstance(var_20, python_code_.mvc_Component)


def test_24():
    var_11 = ""
    var_18 = python_code_.mvc_Component(name="s}}6\x0b\"W9)w23'", mvc_Component=var_11)
    assert isinstance(var_18, python_code_.mvc_Component)


def test_25():
    var_11 = "bgvIaV<M"
    var_18 = python_code_.mvc_Component(name=var_11)
    assert isinstance(var_18, python_code_.mvc_Component)
    var_20 = python_code_.mvc_UIInput()
    var_21 = python_code_.mvc_Attribute(
        name=var_11, type=var_11, mvc_Attribute62=var_20
    )
    assert isinstance(var_21, python_code_.mvc_Attribute)


def test_26():
    var_15 = python_code_.mvc_Event(name=-2466.64, mvc_Event64=True, mvc_Event40=())
    assert isinstance(var_15, python_code_.mvc_Event)


def test_27():
    var_0 = "|.X"
    var_1 = python_code_.mvc_Event(name=var_0, mvc_Event34=var_0, mvc_Event40=var_0)
    assert isinstance(var_1, python_code_.mvc_Event)
    var_51 = python_code_.mvc_Entity(name=var_0, mvc_Entity7=None)
    assert isinstance(var_51, python_code_.mvc_Entity)


def test_28():
    var_1 = "+da#[42"
    var_2 = python_code_.mvc_EventAction()
    var_3 = python_code_.mvc_Event(name=var_1, mvc_Event55=var_2, mvc_Event40=76.42)
    assert isinstance(var_3, python_code_.mvc_Event)


def test_29():
    var_12 = python_code_.mvc_View(name="mvc_Action36", mvc_View19=None)
    assert isinstance(var_12, python_code_.mvc_View)
    var_15 = "-bGpHZaB!*|_-wL\n\t"
    var_16 = set()
    var_17 = python_code_.mvc_MVCModel(version=var_12, name=2092, mvc_MVCModel18=var_16)
    assert isinstance(var_17, python_code_.mvc_MVCModel)
    var_18 = python_code_.mvc_Event(name=var_15, mvc_Event=var_17)
    assert isinstance(var_18, python_code_.mvc_Event)


def test_30():
    var_12 = python_code_.mvc_View(
        name="mvc_View_mvc_UILayout__mvc_UILayout57mvc_Association12_mvc_Model__mvc_Model",
        mvc_View60=None,
    )
    assert isinstance(var_12, python_code_.mvc_View)
    var_19 = python_code_.mvc_UIComponent(name=(-498.6,), type=var_12)
    assert isinstance(var_19, python_code_.mvc_UIComponent)


def test_31():
    var_15 = lambda *args, **kwargs: -1
    var_16 = "_mvc_Action__mvc_Action33"
    var_17 = python_code_.mvc_UILayout(
        orientation=var_15, columns="_$WzJ:__]xRv|", mvc_UILayout=var_15
    )
    assert isinstance(var_17, python_code_.mvc_UILayout)
    var_18 = python_code_.mvc_UIComponent(
        name=var_15, type=var_16, mvc_UIComponent=var_17
    )
    assert isinstance(var_18, python_code_.mvc_UIComponent)


def test_32():
    var_12 = python_code_.mvc_View(name="mvc_Model2", mvc_View43=None)
    assert isinstance(var_12, python_code_.mvc_View)


def test_33():
    var_0 = "mvc_Event:_mvc_View__mvc_View19:_mvc_Controller__mvc_Controller49"
    var_1 = python_code_.mvc_Action(name=var_0, mvc_Action39=())
    assert isinstance(var_1, python_code_.mvc_Action)
    var_2 = python_code_.mvc_Controller(name=var_0)
    assert isinstance(var_2, python_code_.mvc_Controller)
    var_3 = hash
    var_4 = python_code_.mvc_View(name=var_3, mvc_View=1960)
    assert isinstance(var_4, python_code_.mvc_View)
    python_code_.mvc_View(
        name=[-1722, -271, True], mvc_View43=b",\xcf\x86?\xe0", mvc_View60=()
    )


def test_34():
    var_17 = "+6"
    var_18 = python_code_.mvc_Entity(name=var_17, mvc_Entity7=None)
    assert isinstance(var_18, python_code_.mvc_Entity)
    var_20 = python_code_.mvc_Action(
        name=var_17, mvc_Action=var_17, mvc_Action52=var_18
    )
    assert isinstance(var_20, python_code_.mvc_Action)
    var_26 = python_code_.mvc_View(name=None)
    assert isinstance(var_26, python_code_.mvc_View)
    var_27 = {var_26, var_26, var_26}
    var_28 = python_code_.mvc_UILayout(
        orientation=-1868, columns=var_18, mvc_UILayout59=var_27
    )
    assert isinstance(var_28, python_code_.mvc_UILayout)


def test_35():
    var_0 = "mvc_Event:_mvc_View__mvc_View19:_mvc_Controller__mvc_Controller49"
    var_47 = python_code_.mvc_View(name=var_0, mvc_View43={})
    assert isinstance(var_47, python_code_.mvc_View)


def test_36():
    var_1 = python_code_.mvc_Attribute(
        name=")ku4;DS-:CDE8Yj#pc2",
        type="_mvc_MVCModel__mvc_MVCModel23._mvc_Action__mvc_Action36._mvc_Attribute__mvc_Attribute",
        mvc_Attribute=None,
    )
    assert isinstance(var_1, python_code_.mvc_Attribute)


def test_37():
    var_1 = python_code_.mvc_Attribute(name={}, type=[False, "LJ", 1824.74])
    assert isinstance(var_1, python_code_.mvc_Attribute)
    var_2 = {var_1, var_1}
    var_3 = python_code_.mvc_Entity(name="xUX!>UL\rjau^5V-", mvc_Entity4=var_2)
    assert isinstance(var_3, python_code_.mvc_Entity)
    var_4 = python_code_.mvc_Model(
        name="`'xw`", mvc_Model2={'!ta@2xdLbA"*f2*', -1, var_1}
    )
    assert isinstance(var_4, python_code_.mvc_Model)


def test_38():
    var_1 = lambda *args, **kwargs: 3
    var_2 = "\nds~\ns"
    var_5 = python_code_.mvc_MVCModel(version=var_1, name=var_2)
    assert isinstance(var_5, python_code_.mvc_MVCModel)
    var_6 = python_code_.mvc_Model(name=142, mvc_Model16=var_5)
    assert isinstance(var_6, python_code_.mvc_Model)


def test_39():
    var_21 = python_code_.mvc_ControllerView()
    var_22 = python_code_.mvc_Model(name=">]=7\x0c\\9;Ou_`L", mvc_Model46=var_21)
    assert isinstance(var_22, python_code_.mvc_Model)


def test_40():
    python_code_.mvc_EventAction()


@pytest.mark.xfail(strict=True)
def test_41():
    var_0 = python_code_.mvc_UIInput()
    var_1 = "mvc_Event34.mvc_ControllerView45._mvc_View__mvc_View19._mvc_Component__mvc_Component"
    var_2 = python_code_.mvc_Model(name=var_1)
    assert isinstance(var_2, python_code_.mvc_Model)
    var_4 = python_code_.mvc_View(
        name=[-1722, -271, True], mvc_View43=b",\xcf\x86?\xe0", mvc_View60=()
    )
    assert isinstance(var_4, python_code_.mvc_View)
    var_5 = python_code_.mvc_ControllerView()
    var_6 = {var_4, var_4, var_4, var_4}
    var_7 = python_code_.mvc_MVCModel(
        version=(),
        name=b"\x13RvDys\x9d-\x85i\x08\rYS\xd9\x0c",
        mvc_MVCModel18=var_6,
        mvc_MVCModel21=b"@\x86\xd6;\\\x0fp\xac\x84L",
        mvc_MVCModel23=var_6,
    )
    assert isinstance(var_7, python_code_.mvc_MVCModel)
    var_8 = python_code_.mvc_EventAction()
    var_9 = python_code_.mvc_Action(name=var_1, mvc_Action33=var_7, mvc_Action52=var_8)
    assert isinstance(var_9, python_code_.mvc_Action)
    var_10 = python_code_.mvc_View
    var_11 = python_code_.mvc_Attribute(
        name=var_1, type=var_5, mvc_Attribute=var_10, mvc_Attribute62=var_0
    )
    assert isinstance(var_11, python_code_.mvc_Attribute)
    python_code_.mvc_MVCModel(
        version=var_1, name=var_1, mvc_MVCModel21=var_8, mvc_MVCModel25=var_6
    )


@pytest.mark.xfail(strict=True)
def test_42():
    var_0 = python_code_.mvc_Controller(name=-697.16)
    assert isinstance(var_0, python_code_.mvc_Controller)
    var_4 = "_mvc_MVCModel__mvc_MVCModel18,mvc_UILayout"
    var_5 = python_code_.mvc_Entity(name=var_4, mvc_Entity13=-904.32)
    assert isinstance(var_5, python_code_.mvc_Entity)
    var_6 = python_code_.mvc_Entity(name=-589.42, mvc_Entity7=var_5)
    assert isinstance(var_6, python_code_.mvc_Entity)
    var_8 = python_code_.mvc_Component(name=var_4, mvc_Component=var_6)
    assert isinstance(var_8, python_code_.mvc_Component)
    var_9 = python_code_.mvc_UIActions
    var_10 = python_code_.mvc_Entity(
        name=var_9,
        mvc_Entity4=b"\x01}t\xc0\x90\xdd\t0",
        mvc_Entity7=var_6,
        mvc_Entity10=2236.19,
    )
    var_11 = "%e"
    var_12 = False
    var_13 = 4076
    var_14 = "q\n6D~5;/\rm_\x0c9>5Q 7"
    python_code_.mvc_Association(
        name=var_11,
        containment=var_12,
        lowerBound=var_13,
        upperBound=2620.75,
        type=var_14,
        mvc_Association9=var_10,
    )


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = "|.X"
    var_1 = python_code_.mvc_Event(name=var_0, mvc_Event34=var_0, mvc_Event40=var_0)
    assert isinstance(var_1, python_code_.mvc_Event)
    python_code_.mvc_Action(name=var_0, mvc_Action33=var_1, mvc_Action52=())


@pytest.mark.xfail(strict=True)
def test_44():
    var_0 = "mvc_Event:_mvc_View__mvc_View19:_mvc_Controller__=mvc_Controller49"
    var_1 = python_code_.mvc_Action(name=var_0, mvc_Action39=())
    assert isinstance(var_1, python_code_.mvc_Action)
    var_2 = python_code_.mvc_Controller(name=var_0)
    assert isinstance(var_2, python_code_.mvc_Controller)
    var_4 = python_code_.mvc_View(name=var_0, mvc_View19=var_2)
    assert isinstance(var_4, python_code_.mvc_View)
    var_45 = {var_4, var_4, var_4, 0}
    python_code_.mvc_UILayout(
        orientation="]f';OY", columns=-2649, mvc_UILayout=var_4, mvc_UILayout59=var_45
    )


def test_45():
    var_35 = "8"
    var_37 = set()
    var_38 = python_code_.mvc_MVCModel(version={}, name=var_35, mvc_MVCModel23=var_37)
    assert isinstance(var_38, python_code_.mvc_MVCModel)
    var_39 = python_code_.mvc_Component(
        name=set(), mvc_Component48=b"A\xd3\x96", mvc_Component=var_38
    )
    assert isinstance(var_39, python_code_.mvc_Component)


def test_46():
    var_8 = python_code_.mvc_View
    var_13 = python_code_.mvc_Action(name=var_8)
    assert isinstance(var_13, python_code_.mvc_Action)
    var_14 = "0+"
    var_15 = python_code_.mvc_Event(name=var_14, mvc_Event64="mvc_Entity7")
    assert isinstance(var_15, python_code_.mvc_Event)
    var_16 = "] m\r^d{B t#f:p{KB"
    var_17 = {var_15, var_15, var_15}
    var_18 = python_code_.mvc_Action(
        name=var_16, mvc_Action36=var_8, mvc_Action39=var_17
    )
    assert isinstance(var_18, python_code_.mvc_Action)


def test_47():
    var_27 = -2434
    var_28 = "|Pg\\;J`"
    var_29 = python_code_.mvc_Association(
        name=var_28,
        containment=True,
        lowerBound=214,
        upperBound=0,
        type="bf@Fy!o&r#wus",
        mvc_Association=var_27,
    )
    assert isinstance(var_29, python_code_.mvc_Association)
    var_30 = {var_29, var_29, var_29}
    var_31 = python_code_.mvc_Model(name=var_28, mvc_Model2=var_30)
    assert isinstance(var_31, python_code_.mvc_Model)


def test_48():
    var_2 = python_code_.mvc_Controller(
        name="52on#<\x0bXX41#-\nRlhy", mvc_Controller27={True}
    )
    assert isinstance(var_2, python_code_.mvc_Controller)


def test_49():
    var_0 = python_code_.mvc_UIInput()
    var_1 = "mvc_Event34.mvc_ControllerView45._mvc_View__mvc_View19._mvc_Component__mvc_Component"
    var_2 = python_code_.mvc_Model(name=var_1)
    assert isinstance(var_2, python_code_.mvc_Model)
    var_31 = "oT\\qg)\trMX}h['E"
    var_33 = python_code_.mvc_Model(name=var_31, mvc_Model=True)
    var_38 = python_code_.mvc_Entity(
        name=["a^dl(K?(", "RaLzAH?K&?k\x0c\\h`"], mvc_Entity7=var_33
    )
    assert isinstance(var_38, python_code_.mvc_Entity)
    var_39 = True
    var_40 = -3220
    var_41 = python_code_.mvc_Association(
        name={},
        containment=var_39,
        lowerBound=var_40,
        upperBound=var_33,
        type=var_31,
        mvc_Association=var_33,
        mvc_Association9=var_0,
    )
    assert isinstance(var_41, python_code_.mvc_Association)


def test_50():
    var_26 = python_code_.mvc_UIInput()
    var_27 = python_code_.mvc_Component(name="mvc_MVCModel21mvc_UIInput")
    assert isinstance(var_27, python_code_.mvc_Component)
    var_30 = python_code_.mvc_Controller
    var_31 = python_code_.mvc_UIComponent(
        name=var_26, type=var_30, mvc_UIComponent=var_30
    )
    assert isinstance(var_31, python_code_.mvc_UIComponent)
    var_32 = "3+~dV26&ifN f]>ov*"
    var_33 = python_code_.mvc_Controller(
        name=var_32,
        mvc_Controller=complex(-464.8326, 2374.05),
        mvc_Controller27=set(),
        mvc_Controller31={},
    )
    assert isinstance(var_33, python_code_.mvc_Controller)
    var_34 = sorted
    var_35 = python_code_.mvc_View(name=var_32, mvc_View43=var_34)
    assert isinstance(var_35, python_code_.mvc_View)
    var_36 = {var_35, var_35, var_35}
    var_37 = python_code_.mvc_MVCModel(
        version=var_32, name=var_30, mvc_MVCModel18=var_36
    )
    assert isinstance(var_37, python_code_.mvc_MVCModel)
    var_38 = python_code_.mvc_Controller(
        name=var_34, mvc_Controller=var_37, mvc_Controller27=var_36
    )
    assert isinstance(var_38, python_code_.mvc_Controller)
    var_39 = {var_33, var_38, var_38}
    var_40 = python_code_.mvc_Component(name=var_30, mvc_Component48=var_39)
    assert isinstance(var_40, python_code_.mvc_Component)


@pytest.mark.xfail(strict=True)
def test_51():
    var_26 = "\nds~\ns\n"
    var_27 = -2434
    var_32 = python_code_.mvc_Association(
        name=var_26,
        containment=True,
        lowerBound=var_27,
        upperBound=-2369,
        type="mvc_View19._mvc_Model__mvc_Model16",
        mvc_Association9=None,
    )
    assert isinstance(var_32, python_code_.mvc_Association)
    python_code_.mvc_Entity(name={}, mvc_Entity13=var_32)


def test_52():
    var_16 = "_mvc_MVCModel__mvc_MVCModel18,mvc_UILayout"
    var_33 = "+sOg"
    var_34 = python_code_.mvc_UIComponent(
        name=var_16, type=var_33, mvc_UIComponent=var_33
    )
    assert isinstance(var_34, python_code_.mvc_UIComponent)


@pytest.mark.xfail(strict=True)
def test_53():
    var_1 = "mvc_Event34.mvc_ControllerView45._mvc_View__mvc_View19._mvc_Component1__mvc_Component"
    var_2 = python_code_.mvc_Model(name=var_1)
    assert isinstance(var_2, python_code_.mvc_Model)
    var_27 = python_code_.mvc_View(name=None)
    assert isinstance(var_27, python_code_.mvc_View)
    python_code_.mvc_Entity(name=False, mvc_Entity5=complex(1910.90805, 3459.1175793))


def test_54():
    var_55 = True
    var_57 = "q\n6D~5;/\rm_\x0c9>5Q 7"
    var_60 = python_code_.mvc_Controller(
        name=var_57, mvc_Controller31={-1487.96, var_55, "S\x0c }v)(?"}
    )
    assert isinstance(var_60, python_code_.mvc_Controller)
    var_61 = python_code_.mvc_Action(name=var_55, mvc_Action=var_60)
    assert isinstance(var_61, python_code_.mvc_Action)


def test_55():
    var_0 = python_code_.Annotable()
    var_32 = "mvc_Attribute"
    var_33 = python_code_.mvc_UIInput()
    var_34 = python_code_.mvc_Attribute(name=var_0, type=var_32, mvc_Attribute62=var_33)
    assert isinstance(var_34, python_code_.mvc_Attribute)
    var_35 = python_code_.mvc_EventAction()
    var_36 = python_code_.mvc_Event(
        name=var_33, mvc_Event="CLAUEO", mvc_Event55=var_35, mvc_Event64=var_0
    )
    assert isinstance(var_36, python_code_.mvc_Event)


@pytest.mark.xfail(strict=True)
def test_56():
    var_10 = True
    var_35 = 'C#nhu#`V"Qiy'
    var_36 = python_code_.mvc_View(name=var_35, mvc_View=-1609.99, mvc_View19=var_10)
    assert isinstance(var_36, python_code_.mvc_View)
    python_code_.mvc_UILayout(
        orientation=[],
        columns="=aX*2[XRw\tQ\x0c=XIq!",
        mvc_UILayout=var_36,
        mvc_UILayout57=True,
    )


@pytest.mark.xfail(strict=True)
def test_57():
    var_1 = lambda *args, **kwargs: 3
    var_29 = "ZXNmf>Kp]"
    var_32 = python_code_.mvc_ControllerView()
    var_34 = python_code_.mvc_Entity
    var_35 = -1549
    var_36 = 684
    var_37 = "|,pLX"
    var_38 = python_code_.mvc_Association(
        name=var_29,
        containment=var_29,
        lowerBound=var_35,
        upperBound=var_36,
        type=var_37,
    )
    assert isinstance(var_38, python_code_.mvc_Association)
    var_41 = python_code_.mvc_Model(name=None, mvc_Model46=var_32)
    assert isinstance(var_41, python_code_.mvc_Model)
    var_42 = python_code_.mvc_ControllerView()
    var_43 = python_code_.mvc_UILayout(
        orientation=var_34, columns=var_32, mvc_UILayout="*U3*O"
    )
    assert isinstance(var_43, python_code_.mvc_UILayout)
    python_code_.mvc_View(
        name=var_1,
        mvc_View=var_43,
        mvc_View19=b"\xc7C\x9a\\\xd7\xfb\x85\xb7t\x9cs",
        mvc_View43=var_42,
    )


@pytest.mark.xfail(strict=True)
def test_58():
    var_0 = python_code_.mvc_ControllerView()
    var_1 = python_code_.mvc_Attribute(name={}, type=[False, "LJ", 1824.74])
    assert isinstance(var_1, python_code_.mvc_Attribute)
    var_2 = {var_1, var_1}
    var_3 = python_code_.mvc_Entity(name=var_1, mvc_Entity4=var_2, mvc_Entity=())
    assert isinstance(var_3, python_code_.mvc_Entity)
    python_code_.mvc_Model(name=-1, mvc_Model2=var_0, mvc_Model=var_3)


def test_59():
    var_55 = True
    var_67 = python_code_.mvc_Controller(
        name="_mvc_Event__mvc_Event-_mvc_Entity__mvc_Entity4", mvc_Controller31=set()
    )
    assert isinstance(var_67, python_code_.mvc_Controller)
    var_69 = "3]3shtEfYzS6H+I2+#"
    var_70 = python_code_.mvc_MVCModel(version=var_69, name=var_67, mvc_MVCModel25={})
    assert isinstance(var_70, python_code_.mvc_MVCModel)
    var_71 = python_code_.mvc_Component(name=var_55, mvc_Component=var_70)
    assert isinstance(var_71, python_code_.mvc_Component)


def test_60():
    var_0 = "mvc_Event:_mvc_View__mvc_View19:_mvc_Controller__mvc_Controller49"
    var_1 = python_code_.mvc_Action(name=var_0, mvc_Action39=())
    assert isinstance(var_1, python_code_.mvc_Action)
    var_2 = python_code_.mvc_Controller(name=var_0)
    assert isinstance(var_2, python_code_.mvc_Controller)
    var_44 = python_code_.mvc_Event(name=var_0, mvc_Event55=None, mvc_Event40=var_1)
    assert isinstance(var_44, python_code_.mvc_Event)
    var_47 = python_code_.mvc_View(name=var_0, mvc_View43={})
    assert isinstance(var_47, python_code_.mvc_View)


@pytest.mark.xfail(strict=True)
def test_61():
    var_0 = "mvc_View,_mvc_Model__mvc_Model,mvc_View60,mvc_Entity10"
    var_1 = object
    var_2 = python_code_.mvc_Entity(name=2451)
    assert isinstance(var_2, python_code_.mvc_Entity)
    var_3 = {var_2, var_2, var_2}
    var_4 = python_code_.mvc_Entity(
        name=var_0, mvc_Entity5=var_3, mvc_Entity13=var_1, mvc_Entity=var_0
    )
    assert isinstance(var_4, python_code_.mvc_Entity)
    var_5 = {var_2}
    var_6 = "mvc_Association12"
    var_7 = "s@$"
    python_code_.mvc_MVCModel(
        version=var_6, name=var_7, mvc_MVCModel21=var_5, mvc_MVCModel23=True
    )


@pytest.mark.xfail(strict=True)
def test_62():
    var_11 = "mvc_Action39"
    var_25 = 242
    var_26 = python_code_.mvc_UILayout(orientation=var_11, columns=var_25)
    assert isinstance(var_26, python_code_.mvc_UILayout)
    var_27 = python_code_.mvc_UIInput()
    var_28 = python_code_.mvc_ControllerView()
    var_29 = python_code_.mvc_Model(name=">]=7\x0c\\9;Ou_`L", mvc_Model46=var_28)
    assert isinstance(var_29, python_code_.mvc_Model)
    python_code_.mvc_Entity(name=var_27, mvc_Entity10=None, mvc_Entity=var_29)


def test_63():
    var_0 = "mvc_Event:_mvc_View__mvc_View19:_mvc_Controller__mvc_Controller49"
    var_1 = python_code_.mvc_Action(name="", mvc_Action=var_0)
    assert isinstance(var_1, python_code_.mvc_Action)
    var_2 = python_code_.mvc_Controller(
        name=var_0,
        mvc_Controller49=var_0,
        mvc_Controller27={2707.92, 2563.51, "mvc_Association12"},
    )
    assert isinstance(var_2, python_code_.mvc_Controller)
    var_4 = python_code_.mvc_View(name=var_0, mvc_View60=var_1)
    assert isinstance(var_4, python_code_.mvc_View)
    python_code_.mvc_View(name=var_0)
    var_10 = python_code_.mvc_UILayout(orientation=True, columns=-241)
    assert isinstance(var_10, python_code_.mvc_UILayout)
    var_11 = python_code_.mvc_UIComponent(
        name=var_1, type=var_4, mvc_UIComponent=var_10
    )
    assert isinstance(var_11, python_code_.mvc_UIComponent)


@pytest.mark.xfail(strict=True)
def test_64():
    var_0 = ""
    var_1 = set()
    var_2 = python_code_.mvc_MVCModel(version=var_0, name=var_0, mvc_MVCModel23=var_1)
    assert isinstance(var_2, python_code_.mvc_MVCModel)
    var_3 = python_code_.mvc_Attribute
    var_4 = python_code_.mvc_Attribute(
        name=var_1, type=var_0, mvc_Attribute=var_3, mvc_Attribute62="#s`T^"
    )
    assert isinstance(var_4, python_code_.mvc_Attribute)
    var_6 = "_mvc_View__mvc_View19:mvc_Attribute"
    var_7 = python_code_.mvc_View(name=var_6, mvc_View=var_3)
    assert isinstance(var_7, python_code_.mvc_View)
    var_8 = python_code_.UIComponent()
    var_9 = "i}eDSxx@7f=oie`\x0b;U"
    var_10 = python_code_.mvc_Event(name=var_9, mvc_Event=var_4)
    assert isinstance(var_10, python_code_.mvc_Event)
    var_11 = "_mvc_UILayout__mvc_UILayout"
    var_12 = python_code_.mvc_Entity(name=var_11, mvc_Entity7=var_8, mvc_Entity10=var_3)
    assert isinstance(var_12, python_code_.mvc_Entity)
    var_13 = python_code_.mvc_ControllerView()
    var_14 = python_code_.mvc_View(name=var_0, mvc_View43=var_13)
    var_15 = python_code_.mvc_UIComponent(name=[], type=var_14, mvc_UIComponent=set())
    assert isinstance(var_15, python_code_.mvc_UIComponent)
    var_17 = python_code_.UIComponent()
    var_18 = "mvc_View19"
    python_code_.mvc_Event(name=var_18, mvc_Event55=var_17, mvc_Event37=var_3)
    var_20 = 'l2+]+g">qN:9ij'
    python_code_.mvc_Action(name=var_20, mvc_Action=var_14, mvc_Action36=var_10)


def test_65():
    var_35 = "8"
    var_37 = set()
    var_38 = python_code_.mvc_MVCModel(version={}, name=var_35, mvc_MVCModel23=var_37)
    assert isinstance(var_38, python_code_.mvc_MVCModel)
    var_39 = python_code_.mvc_Component(
        name=set(), mvc_Component48=b"A\xd3\x96", mvc_Component=var_38
    )
    assert isinstance(var_39, python_code_.mvc_Component)
    var_40 = python_code_.mvc_Controller(
        name=var_35,
        mvc_Controller49=var_39,
        mvc_Controller=var_38,
        mvc_Controller27=var_37,
    )
    assert isinstance(var_40, python_code_.mvc_Controller)


@pytest.mark.xfail(strict=True)
def test_66():
    var_0 = "@*f|s\n\r[PB 98]"
    var_1 = python_code_.mvc_Controller(
        name=var_0,
        mvc_Controller27=b"r\xb7\x961wgJ\xd9\xa4\x105\xf6\xa5\x07\xe8",
        mvc_Controller29=var_0,
    )
    assert isinstance(var_1, python_code_.mvc_Controller)
    var_2 = 3818
    var_3 = python_code_.mvc_Attribute
    var_4 = -31
    var_5 = python_code_.mvc_UIComponent(name=var_0, type=var_1)
    assert isinstance(var_5, python_code_.mvc_UIComponent)
    var_6 = {var_5}
    var_7 = python_code_.mvc_UILayout(
        orientation=var_2,
        columns=var_4,
        mvc_UILayout=var_3,
        mvc_UILayout57=var_6,
        mvc_UILayout59=var_6,
    )
    assert isinstance(var_7, python_code_.mvc_UILayout)
    var_8 = python_code_.mvc_MVCModel(
        version=complex(3735.0, 444.026654),
        name=var_3,
        mvc_MVCModel=var_6,
        mvc_MVCModel23={},
    )
    assert isinstance(var_8, python_code_.mvc_MVCModel)
    python_code_.mvc_View(
        name=var_3, mvc_View=var_7, mvc_View19=var_8, mvc_View60=var_7
    )


@pytest.mark.xfail(strict=True)
def test_67():
    var_60 = python_code_.mvc_View(name=None)
    assert isinstance(var_60, python_code_.mvc_View)
    var_64 = lambda *args, **kwargs: []
    var_65 = python_code_.mvc_Component(name=var_64)
    assert isinstance(var_65, python_code_.mvc_Component)
    var_66 = python_code_.mvc_EventAction()
    var_67 = "mvc_MVCModel21"
    var_69 = python_code_.mvc_Controller(
        name=var_67,
        mvc_Controller49=var_65,
        mvc_Controller=False,
        mvc_Controller31=var_67,
    )
    assert isinstance(var_69, python_code_.mvc_Controller)
    var_70 = python_code_.mvc_UILayout(orientation=False, columns=var_65)
    assert isinstance(var_70, python_code_.mvc_UILayout)
    var_71 = True
    var_72 = python_code_.mvc_Entity(name=None, mvc_Entity13=3545.45)
    assert isinstance(var_72, python_code_.mvc_Entity)
    python_code_.mvc_Association(
        name=var_69,
        containment=var_71,
        lowerBound=var_69,
        upperBound=var_66,
        type=var_60,
        mvc_Association9=var_70,
        mvc_Association12=var_72,
    )


@pytest.mark.xfail(strict=True)
def test_68():
    var_8 = python_code_.mvc_View
    var_13 = python_code_.mvc_Action(name=var_8)
    assert isinstance(var_13, python_code_.mvc_Action)
    var_14 = "0+"
    var_15 = python_code_.mvc_Event(name=var_14, mvc_Event64="mvc_Entity7")
    assert isinstance(var_15, python_code_.mvc_Event)
    var_16 = "] m\r^d{B t#f:p{KB"
    var_17 = {var_15, var_15, var_15}
    var_18 = python_code_.mvc_Action(
        name=var_16, mvc_Action36=var_8, mvc_Action39=var_17
    )
    assert isinstance(var_18, python_code_.mvc_Action)
    var_19 = "_mvc_Model__mvc_Model46 _mvc_UILayout__mvc_UILayout57"
    var_20 = python_code_.mvc_MVCModel(
        version=var_19, name=var_14, mvc_MVCModel21=var_17
    )
    assert isinstance(var_20, python_code_.mvc_MVCModel)
    var_21 = -923
    var_22 = "mvc_Entity"
    var_23 = python_code_.mvc_Entity(name=var_22, mvc_Entity13={926.78, "D", -3304.63})
    assert isinstance(var_23, python_code_.mvc_Entity)
    python_code_.mvc_Association(
        name=var_19,
        containment="",
        lowerBound=var_21,
        upperBound=var_17,
        type=var_8,
        mvc_Association=var_13,
        mvc_Association12=var_23,
    )


def test_69():
    var_17 = "+6"
    var_18 = python_code_.mvc_Entity(name=var_17, mvc_Entity7=None)
    assert isinstance(var_18, python_code_.mvc_Entity)
    var_26 = python_code_.mvc_MVCModel(
        version="f>/;jvK=D2\t;", name="mvc_Event40", mvc_MVCModel18={False, False}
    )
    assert isinstance(var_26, python_code_.mvc_MVCModel)
    var_28 = lambda *args, **kwargs: False
    var_29 = python_code_.mvc_Model(name=var_26, mvc_Model16=var_28, mvc_Model46=var_28)
    assert isinstance(var_29, python_code_.mvc_Model)
