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
    Annotation,
    CPNToolsTransitionAddin,
    Enum,
    HLAnnotation,
    HLAnnotationAddin,
    HLArcAddin,
    HLArcType,
    HLPlaceAddin,
    HLTransitionAddin,
    HasGraphics,
    HasId,
    HasLabel,
    HasName,
    HasToolInfo,
    Label,
    Node,
    Object,
    Place,
    PlaceNode,
    TransitionNode,
    abstractmethod,
    date,
    datetime,
    model_Annotation,
    model_Arc,
    model_Attribute,
    model_CPNToolsTransitionAddin,
    model_Code,
    model_Condition,
    model_DeclarationStructure,
    model_FusionGroup,
    model_HLAnnotation,
    model_HLAnnotationAddin,
    model_HLArcAddin,
    model_HLArcType_1,
    model_HLDeclaration,
    model_HLMarking,
    model_HLPlaceAddin,
    model_HLTransitionAddin,
    model_HasId,
    model_HasLabel,
    model_HasName,
    model_HasToolInfo,
    model_Instance,
    model_Label,
    model_Name,
    model_Node,
    model_Object,
    model_Page,
    model_ParameterAssignment,
    model_PetriNet,
    model_Place,
    model_PlaceNode,
    model_RefPlace,
    model_RefTrans,
    model_Time,
    model_ToolInfo,
    model_Transition,
    model_TransitionNode,
    model_Type,
    time,
)


def test_0():
    python_code_.model_ParameterAssignment(
        parameter="_model_PetriNet__PetriNet.HasLabel.Normal._model_Label__Label",
        value="ge\x0c `Uf[2T",
        ParameterAssignment=None,
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_30 = python_code_.model_Instance(subPageID="oOb;;", instance=set())
    assert isinstance(var_30, python_code_.model_Instance)
    python_code_.model_ParameterAssignment(
        parameter="Normal model_HLAnnotation",
        value="Test._model_ParameterAssignment__ParameterAssignment",
        parameterAssignment=var_30,
        ParameterAssignment=var_30,
    )


def test_2():
    var_30 = python_code_.model_Instance(subPageID=";07mn;GP${e|OuM4'_+")
    assert isinstance(var_30, python_code_.model_Instance)
    var_31 = python_code_.model_ParameterAssignment(
        parameter="TY", value="+,7H1\\3>.}NZ,>G.gh@", ParameterAssignment=var_30
    )
    assert isinstance(var_31, python_code_.model_ParameterAssignment)


def test_3():
    var_52 = python_code_.model_HLArcAddin(type={})
    assert isinstance(var_52, python_code_.model_HLArcAddin)


def test_4():
    var_22 = python_code_.model_Instance(
        subPageID="fusionGroups,model_ParameterAssignment,model_HasLabel,model_HasLabel"
    )
    assert isinstance(var_22, python_code_.model_Instance)


def test_5():
    var_22 = python_code_.model_Instance(
        subPageID="Test.fusionGroups",
        Instance=None,
        instance={1701.5, "Normal._model_Instance__instance"},
    )
    assert isinstance(var_22, python_code_.model_Instance)


def test_6():
    python_code_.model_ToolInfo(
        tool="U(C;&:(\x0c&*lE#\t", version="JoiI]fsp/eL|\\dh\x0c"
    )


def test_7():
    var_48 = "_mdel_Label__label NYrmal"
    var_50 = python_code_.model_ToolInfo(tool=var_48, version=var_48, toolinfo=var_48)
    assert isinstance(var_50, python_code_.model_ToolInfo)


def test_8():
    var_51 = python_code_.model_PetriNet(
        type="parent:Test:HasToolInfo",
        PetriNet=None,
        petriNet={
            -857.66,
            "_model_PetriNet__petriNet23:model_FusionGroup:model_HasToolInfo:model_HLAnnotation",
        },
        PetriNet40=None,
    )
    assert isinstance(var_51, python_code_.model_PetriNet)


def test_9():
    var_51 = python_code_.model_PetriNet(type="G7:$9(\n(rwm!3-i&O")
    assert isinstance(var_51, python_code_.model_PetriNet)


def test_10():
    var_50 = python_code_.model_Attribute()
    var_51 = python_code_.model_PetriNet(type=">c", PetriNet=var_50, PetriNet40=None)
    assert isinstance(var_51, python_code_.model_PetriNet)


def test_11():
    var_24 = python_code_.HasToolInfo()
    var_25 = python_code_.model_PetriNet(type={}, PetriNet40=var_24)
    assert isinstance(var_25, python_code_.model_PetriNet)


def test_12():
    var_7 = python_code_.model_Label(Label=None, label=None)
    assert isinstance(var_7, python_code_.model_Label)


def test_13():
    var_2 = python_code_.model_ParameterAssignment(parameter="HasLabel", value="DzPi")
    var_7 = python_code_.model_Label(Label=var_2)
    assert isinstance(var_7, python_code_.model_Label)


def test_14():
    var_57 = python_code_.model_Label(label=())
    assert isinstance(var_57, python_code_.model_Label)


def test_15():
    python_code_.model_Type()


def test_16():
    var_62 = python_code_.model_HLAnnotationAddin(text=None)
    assert isinstance(var_62, python_code_.model_HLAnnotationAddin)


def test_17():
    var_34 = python_code_.model_Label(
        label={"_model_Label__Label": ")x{A9#.\rj-y", "9": -3732}
    )
    assert isinstance(var_34, python_code_.model_Label)
    var_34.asString()


def test_18():
    var_10 = python_code_.model_HasId(id=b"\xc0\x87T\x13\n\x15\xed\x1d\xd2\xa6\x19b")
    assert isinstance(var_10, python_code_.model_HasId)


@pytest.mark.xfail(strict=True)
def test_19():
    var_37 = python_code_.HasLabel
    var_38 = "dN#\\2XyTY<6\x0b<;"
    var_39 = python_code_.model_ParameterAssignment(
        parameter=var_37,
        value=var_38,
        parameterAssignment=var_37,
        ParameterAssignment=var_37,
    )
    python_code_.model_Instance(subPageID=var_37, Instance=var_39)


def test_20():
    var_0 = 3
    var_13 = python_code_.model_Instance(
        subPageID="model_HLAnnotation,_model_PetriNet__petriNet23,_model_ParameterAssignment__parameterAssignment",
        Instance=var_0,
    )
    assert isinstance(var_13, python_code_.model_Instance)


def test_21():
    var_48 = "_model_Label__label NYrmal"
    var_49 = python_code_.model_HLArcAddin(type="Wh9'$ABpSDiJ", model_HLArcAddin=var_48)
    assert isinstance(var_49, python_code_.model_HLArcAddin)


def test_22():
    var_48 = "_mdel_Label__label NYrmal"
    var_50 = python_code_.model_ToolInfo(
        tool="model_ParameterAssignment_model_ParameterAssignment__parameterAssignment",
        version=var_48,
        ToolInfo=var_48,
    )
    assert isinstance(var_50, python_code_.model_ToolInfo)


def test_23():
    var_51 = python_code_.model_PetriNet(
        type="2f$j6QNzhk}jyG5", petriNet=set(), petriNet23=set(), PetriNet40=None
    )
    assert isinstance(var_51, python_code_.model_PetriNet)


@pytest.mark.xfail(strict=True)
def test_24():
    var_1 = python_code_.model_RefPlace
    var_2 = python_code_.model_HLAnnotationAddin(text=var_1)
    assert isinstance(var_2, python_code_.model_HLAnnotationAddin)
    python_code_.model_Label()
    var_11 = "'Zs_Ug"
    var_12 = "q.YyG8Hv`tlV}F"
    var_13 = "\t-k#.g,\x0c"
    var_14 = python_code_.model_Instance(
        subPageID=var_13, Instance=complex(4384.855, -1864.0)
    )
    assert isinstance(var_14, python_code_.model_Instance)
    python_code_.model_ParameterAssignment(
        parameter=var_11, value=var_12, parameterAssignment=var_14
    )
