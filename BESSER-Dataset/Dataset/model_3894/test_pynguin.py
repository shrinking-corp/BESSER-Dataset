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
    ActivityAspect,
    Atom,
    CaseAspect,
    Control,
    Document,
    DocumentCondition,
    DocumentDescriptor,
    DocumentType,
    Expression,
    GlobalAspect,
    ModelAspect,
    Operator,
    ProcessAspect,
    RuntimeGlobalAspect,
    RuntimeModelAspect,
    State,
    TaskAspect,
    TaskC,
    abstractmethod,
    date,
    datetime,
    time,
    workflow_Activity,
    workflow_ActivityAspect,
    workflow_ActivityC,
    workflow_ActivityI,
    workflow_ActivityO,
    workflow_Agent,
    workflow_AgentContainer,
    workflow_Arc,
    workflow_Atom,
    workflow_Case,
    workflow_CaseAspect,
    workflow_CaseC,
    workflow_CaseI,
    workflow_CaseO,
    workflow_ConstantAtom,
    workflow_Control,
    workflow_ControlAspect,
    workflow_CoreModel,
    workflow_DefaultDocument,
    workflow_DefaultDocumentCondition,
    workflow_DefaultDocumentDescriptor,
    workflow_DefaultDocumentType,
    workflow_Document,
    workflow_DocumentCondition,
    workflow_DocumentContainer,
    workflow_DocumentDescrAtom,
    workflow_DocumentDescriptor,
    workflow_DocumentType,
    workflow_DocumentTypeContainer,
    workflow_DotOperator,
    workflow_EnumField,
    workflow_EnumFieldAtom,
    workflow_EnumFieldValue,
    workflow_EnumLiteral,
    workflow_EnumLiteralAtom,
    workflow_EqualToOperator,
    workflow_Expression,
    workflow_Field,
    workflow_FieldAtom,
    workflow_FieldValue,
    workflow_GlobalAspect,
    workflow_GreaterThanOperator,
    workflow_Information,
    workflow_InformationAspect,
    workflow_InformationRuntimeAspect,
    workflow_LessThanOperator,
    workflow_Marking,
    workflow_ModelAspect,
    workflow_ModelRegistry,
    workflow_Operator,
    workflow_Organisation,
    workflow_OrganisationAspect,
    workflow_PetriNet,
    workflow_Place,
    workflow_Process,
    workflow_ProcessAspect,
    workflow_ProcessDocument,
    workflow_ProcessO,
    workflow_Role,
    workflow_RuntimeCoreModel,
    workflow_RuntimeGlobalAspect,
    workflow_RuntimeInformation,
    workflow_RuntimeModelAspect,
    workflow_State,
    workflow_String2DocumentMap,
    workflow_Task,
    workflow_TaskAspect,
    workflow_TaskC,
    workflow_TaskI,
    workflow_TaskO,
    workflow_Token,
    workflow_Transition,
    workflow_UnequalToOperator,
    workflow_WorkflowEngine,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.Control()
    var_1 = "jZ]"
    var_2 = True
    python_code_.workflow_Case(id=var_1, client=var_1, started=var_2, finished=var_2)
    var_4 = python_code_.workflow_EnumFieldAtom()
    python_code_.workflow_Activity(
        started=var_2,
        finished=var_2,
        workflow_Activity={3210.38, True},
        workflow_Activity15=var_4,
        Activity=var_0,
    )
    var_10 = python_code_.workflow_EnumFieldValue()
    var_14 = "workflow_TaskO1_workflow_EnumLiteral__workflow_EnumLiteral165_workflow_DefaultDocument__workflow_DefaultDocument132"
    var_15 = python_code_.workflow_TaskC(name=var_14)
    assert isinstance(var_15, python_code_.workflow_TaskC)
    python_code_.workflow_DocumentTypeContainer(
        name=(), workflow_DocumentTypeContainer=var_10
    )


def test_1():
    var_2 = "YEdcEX#j!XUEkg"
    var_3 = python_code_.workflow_DocumentTypeContainer(name=var_2)
    assert isinstance(var_3, python_code_.workflow_DocumentTypeContainer)
    var_5 = "i"
    var_6 = python_code_.workflow_DocumentType(name=var_5)
    assert isinstance(var_6, python_code_.workflow_DocumentType)
    var_7 = python_code_.workflow_Organisation(name=var_2)
    assert isinstance(var_7, python_code_.workflow_Organisation)
    var_9 = python_code_.workflow_AgentContainer(name=[])
    assert isinstance(var_9, python_code_.workflow_AgentContainer)


def test_2():
    var_0 = python_code_.workflow_Role(name="")
    var_4 = "0ZT5C|ZXV/\t2Pb"
    var_8 = lambda *args, **kwargs: True
    python_code_.workflow_RuntimeInformation(caseIdCount=var_8)
    var_11 = python_code_.workflow_Organisation(name=var_0, workflow_Organisation=())
    assert isinstance(var_11, python_code_.workflow_Organisation)
    var_12 = python_code_.workflow_TaskO(name=b"\xa4\xbfc\xff\x12\xf0\xc7\xf6\xdd")
    assert isinstance(var_12, python_code_.workflow_TaskO)
    var_26 = python_code_.workflow_AgentContainer(name=[])
    assert isinstance(var_26, python_code_.workflow_AgentContainer)
    python_code_.workflow_Role(name=var_4, workflow_Role21=set())


def test_3():
    var_43 = "O.gd=\x0c\tnk_'$["
    var_57 = python_code_.workflow_Organisation(name=var_43)
    assert isinstance(var_57, python_code_.workflow_Organisation)
    var_59 = python_code_.workflow_AgentContainer(name=[])
    assert isinstance(var_59, python_code_.workflow_AgentContainer)


def test_4():
    var_0 = "workflow_FieldValue-workflow_Field135-_workflow_DocumentType__workflow_DocumentType175"
    var_1 = python_code_.workflow_DocumentContainer(name=var_0)
    assert isinstance(var_1, python_code_.workflow_DocumentContainer)
    var_3 = python_code_.workflow_DocumentCondition(name=var_1)
    assert isinstance(var_3, python_code_.workflow_DocumentCondition)
    var_6 = python_code_.workflow_Organisation(name=var_0)
    assert isinstance(var_6, python_code_.workflow_Organisation)
    var_10 = lambda *args, **kwargs: False
    python_code_.workflow_FieldValue(
        value=var_0, workflow_FieldValue=var_10, workflow_FieldValue134=var_10
    )
    var_50 = python_code_.workflow_Role(
        name=var_0, workflow_Role17=var_1, workflow_Role169=var_6
    )
    assert isinstance(var_50, python_code_.workflow_Role)


def test_5():
    var_0 = python_code_.workflow_Role(name="")
    var_4 = "0ZT5C|!XV/\t2Pb"
    var_5 = python_code_.workflow_EnumFieldValue()
    python_code_.workflow_EnumLiteral(name=var_4, workflow_EnumLiteral161=var_5)
    var_8 = lambda *args, **kwargs: True
    python_code_.workflow_RuntimeInformation(caseIdCount=var_8)
    var_11 = python_code_.workflow_Organisation(name=var_0, workflow_Organisation=())
    assert isinstance(var_11, python_code_.workflow_Organisation)
    var_12 = python_code_.workflow_TaskO(name=b"\xa4\xbfc\xff\x12\xf0\xc7\xf6\xdd")
    assert isinstance(var_12, python_code_.workflow_TaskO)


def test_6():
    var_4 = " WgSW"
    var_5 = python_code_.workflow_EnumLiteralAtom()
    var_6 = python_code_.workflow_EnumLiteral(
        name=var_4,
        workflow_EnumLiteral155=[True, 2959, 0],
        workflow_EnumLiteral165=var_5,
    )
    assert isinstance(var_6, python_code_.workflow_EnumLiteral)
    var_9 = python_code_.workflow_TaskC(name=var_4)
    assert isinstance(var_9, python_code_.workflow_TaskC)
    var_14 = python_code_.workflow_DocumentContainer(name=var_4)
    assert isinstance(var_14, python_code_.workflow_DocumentContainer)
    python_code_.workflow_Role(name="workflow_DocumentType.workflow_Agent20")


def test_7():
    var_43 = "O.gd=\x0c\tnk_'$["
    var_57 = python_code_.workflow_Organisation(name=var_43)
    assert isinstance(var_57, python_code_.workflow_Organisation)
    var_59 = python_code_.workflow_AgentContainer(name=[])
    assert isinstance(var_59, python_code_.workflow_AgentContainer)
    var_62 = "Place._workflow_Place__Place.workflow_DocumentDescriptor"
    python_code_.workflow_Field(
        name=var_62, workflow_Field148="workflow_RuntimeCoreModel"
    )


def test_8():
    var_1 = "lx:"
    var_2 = python_code_.workflow_DocumentType
    python_code_.workflow_Field(name=var_1, workflow_Field=var_2)
    var_4 = python_code_.workflow_PetriNet()
    python_code_.workflow_Place(name=var_1, workflow_Place30=var_4)


@pytest.mark.xfail(strict=True)
def test_9():
    var_7 = python_code_.workflow_OrganisationAspect()
    var_11 = python_code_.DocumentType()
    var_21 = python_code_.workflow_TaskC(name=var_11)
    assert isinstance(var_21, python_code_.workflow_TaskC)
    var_24 = python_code_.workflow_InformationRuntimeAspect
    var_25 = "o_M-6G,/\x0cGR-"
    var_26 = python_code_.workflow_Document(
        name=var_24, id=var_25, workflow_Document=var_7, workflow_Document143=None
    )
    assert isinstance(var_26, python_code_.workflow_Document)
    python_code_.workflow_String2DocumentMap(
        key=var_24, workflow_String2DocumentMap142=var_26
    )


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = "workflow_TaskO1:_workflow_DocumentDescriptor__workflow_DocumentDescriptor72:_workflow_Organisation__workflow_Organisation:workflow_ActivityI"
    var_1 = python_code_.workflow_Organisation(name=var_0, workflow_Organisation=var_0)
    assert isinstance(var_1, python_code_.workflow_Organisation)
    var_8 = "0wCS:g2TjBD*Zq\\b"
    var_9 = python_code_.workflow_CaseI()
    var_10 = python_code_.workflow_String2DocumentMap(
        key=var_8, workflow_String2DocumentMap=var_9
    )
    var_12 = python_code_.workflow_Case
    python_code_.workflow_Process(
        name=var_0, Process=b"\x98\x01\n\xdcD\xdfg\x01\x12vM", Process102=var_12
    )
    var_15 = False
    python_code_.workflow_Case(
        id=var_12, client=var_8, started=var_15, finished=True, core=var_10
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = (
        lambda *args, **kwargs: "_workflow_TaskO__workflow_TaskO1 workflow_String2DocumentMap142 workflow_Document143"
    )
    var_2 = "YEdcEX#j!XUEkg"
    var_3 = python_code_.workflow_DocumentTypeContainer(name=var_2)
    assert isinstance(var_3, python_code_.workflow_DocumentTypeContainer)
    var_15 = python_code_.workflow_Document(name=var_0, id=None)
    assert isinstance(var_15, python_code_.workflow_Document)
    python_code_.workflow_DocumentType(name=b"*\xd0", workflow_DocumentType82=var_15)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = "_workflow_String2DocumentMap__workflow_String2DocumentMap142.workflow_RuntimeCoreModel117"
    var_1 = python_code_.workflow_EnumLiteralAtom
    var_2 = python_code_.workflow_DocumentType(name=var_0, workflow_DocumentType=var_1)
    assert isinstance(var_2, python_code_.workflow_DocumentType)
    var_5 = "n(Zh-@"
    var_6 = python_code_.workflow_Information()
    python_code_.workflow_ProcessDocument(name=var_5, workflow_ProcessDocument=var_6)
    var_10 = python_code_.workflow_CaseI()
    var_15 = python_code_.workflow_CaseI()
    var_19 = python_code_.Operator()
    var_20 = python_code_.workflow_DotOperator()
    var_21 = python_code_.GlobalAspect()
    var_24 = python_code_.workflow_CaseO()
    python_code_.workflow_Field(name=var_15)
    python_code_.workflow_ProcessDocument(name=var_5)
    python_code_.workflow_Case(
        id=var_19,
        client={2539, "workflow_DocumentType", -84},
        started=var_21,
        finished=var_20,
        core=var_24,
        workflow_Case8=var_10,
        cases=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_13():
    var_4 = " WgSW"
    var_5 = python_code_.workflow_EnumLiteralAtom()
    var_6 = python_code_.workflow_EnumLiteral(
        name=var_4,
        workflow_EnumLiteral155=[True, 2959, 0],
        workflow_EnumLiteral165=var_5,
    )
    assert isinstance(var_6, python_code_.workflow_EnumLiteral)
    var_7 = python_code_.workflow_OrganisationAspect()
    var_42 = python_code_.workflow_TaskC(name=var_4)
    assert isinstance(var_42, python_code_.workflow_TaskC)
    var_45 = python_code_.workflow_DocumentTypeContainer(
        name={
            '<cI\x0c\t"Z[': 2732,
            "np7Y5L^6o\rB": False,
            "_workflow_Document__workflow_Document143.in_": -2073,
        }
    )
    assert isinstance(var_45, python_code_.workflow_DocumentTypeContainer)
    var_46 = python_code_.workflow_DocumentType(
        name=complex(3308.068565, 754.89), workflow_DocumentType175=var_45
    )
    assert isinstance(var_46, python_code_.workflow_DocumentType)
    var_47 = python_code_.workflow_DocumentContainer(name=var_4)
    assert isinstance(var_47, python_code_.workflow_DocumentContainer)
    var_57 = python_code_.workflow_InformationRuntimeAspect
    var_58 = "o_M-6G,/\x0cGR-"
    var_59 = python_code_.workflow_Document(
        name=var_57, id=var_58, workflow_Document=var_7, workflow_Document143=None
    )
    assert isinstance(var_59, python_code_.workflow_Document)
    python_code_.workflow_String2DocumentMap(
        key=var_57, workflow_String2DocumentMap142=var_59
    )


def test_14():
    var_0 = (
        lambda *args, **kwargs: "_workflow_TaskO__workflow_TaskO1 workflow_String2DocumentMap142 workflow_Document143"
    )
    var_2 = "YEdcEX#j!XUEkg"
    var_3 = python_code_.workflow_DocumentTypeContainer(name=var_2)
    assert isinstance(var_3, python_code_.workflow_DocumentTypeContainer)
    var_5 = ""
    var_6 = python_code_.workflow_DocumentType(name=var_5)
    assert isinstance(var_6, python_code_.workflow_DocumentType)
    var_7 = python_code_.workflow_Organisation(name=var_2)
    assert isinstance(var_7, python_code_.workflow_Organisation)
    var_10 = "m"
    python_code_.workflow_RuntimeInformation(caseIdCount=var_10)
    python_code_.workflow_Place(name=var_0, workflow_Place=var_5)
    var_13 = python_code_.workflow_DocumentDescriptor(
        name=var_10,
        workflow_DocumentDescriptor=var_2,
        workflow_DocumentDescriptor65=None,
        workflow_DocumentDescriptor74=None,
    )
    assert isinstance(var_13, python_code_.workflow_DocumentDescriptor)


def test_15():
    var_1 = "Ogd=\x0c\tnk_'$["
    python_code_.workflow_Process(name=var_1, process=[False, False])
    var_25 = "m-"
    python_code_.workflow_RuntimeInformation(caseIdCount=var_25)
    var_27 = python_code_.workflow_DocumentDescriptor(name=86.7)
    assert isinstance(var_27, python_code_.workflow_DocumentDescriptor)


@pytest.mark.xfail(strict=True)
def test_16():
    var_7 = python_code_.workflow_FieldAtom()
    var_8 = "?41C3=\x0csLY"
    var_9 = python_code_.workflow_TaskI()
    var_10 = python_code_.workflow_DocumentDescriptor(
        name=var_8,
        workflow_DocumentDescriptor146=(564.46, 3285),
        workflow_DocumentDescriptor=var_9,
        workflow_DocumentDescriptor72=var_7,
    )
    assert isinstance(var_10, python_code_.workflow_DocumentDescriptor)
    var_11 = python_code_.workflow_DocumentTypeContainer(name=var_8)
    assert isinstance(var_11, python_code_.workflow_DocumentTypeContainer)
    var_48 = ""
    var_59 = python_code_.workflow_TaskAspect()
    python_code_.workflow_Task(
        name=var_48, Task=var_59, core112=complex(2572.205, 539.166)
    )


@pytest.mark.xfail(strict=True)
def test_17():
    var_0 = "workflow_FieldValue-workflow_Field135-_workflow_DocumentType__workflow_DocumentType175"
    var_1 = python_code_.workflow_DocumentContainer(name=var_0)
    assert isinstance(var_1, python_code_.workflow_DocumentContainer)
    var_3 = python_code_.workflow_DocumentCondition(name=var_1)
    assert isinstance(var_3, python_code_.workflow_DocumentCondition)
    var_6 = python_code_.workflow_Organisation(name=var_0)
    assert isinstance(var_6, python_code_.workflow_Organisation)
    var_10 = lambda *args, **kwargs: False
    python_code_.workflow_FieldValue(
        value=var_0, workflow_FieldValue=var_10, workflow_FieldValue134=var_10
    )
    var_12 = "_workflow_Activity__core11 workflow_TaskI67 _workflow_DocumentTypeContainer__workflow_DocumentTypeContainer"
    var_13 = python_code_.workflow_Information()
    var_14 = lambda *args, **kwargs: True
    var_15 = python_code_.workflow_DocumentDescriptor(
        name=var_0,
        workflow_DocumentDescriptor65=var_14,
        workflow_DocumentDescriptor74={
            "_workflow_Agent__workflow_Agent20_workflow_Role__workflow_Role": 723,
            "_workflow_ProcessDocument__workflow_ProcessDocument139": 2576,
        },
    )
    assert isinstance(var_15, python_code_.workflow_DocumentDescriptor)
    python_code_.workflow_ProcessDocument(
        name=var_12, workflow_ProcessDocument=var_13, workflow_ProcessDocument75=var_15
    )


@pytest.mark.xfail(strict=True)
def test_18():
    var_25 = "_workflow_Activity__core11 workflow_TaskI67 _workflow_DocumentTypeontainer__workflow_DocumentTypeContainer"
    var_28 = python_code_.workflow_DocumentDescriptor(name=var_25)
    assert isinstance(var_28, python_code_.workflow_DocumentDescriptor)
    python_code_.workflow_ProcessDocument(
        name=var_25, workflow_ProcessDocument=None, workflow_ProcessDocument75=var_28
    )


def test_19():
    var_0 = (
        lambda *args, **kwargs: "_workflow_TaskO__workflow_TaskO1 workflow_String2DocumentMap142 workflow_Document143"
    )
    python_code_.workflow_Role(
        name=var_0,
        workflow_Role21="\tgYPgkm{8}a\nU",
        workflow_Role169=complex(-68.700568, 2662.57),
    )
    var_2 = "_workflow_Document__workflow_Document143"
    var_3 = python_code_.workflow_ProcessO()
    python_code_.workflow_Role(name=var_2, workflow_Role126=var_3)
    python_code_.workflow_RuntimeInformation(caseIdCount=var_2)
    var_7 = python_code_.workflow_CaseO
    var_8 = python_code_.workflow_EnumField(name="uOI_j", workflow_EnumField154=var_7)
    assert isinstance(var_8, python_code_.workflow_EnumField)
    var_10 = python_code_.workflow_Arc(name=var_2, out41=var_7)
    var_11 = {var_10, var_10, var_10}
    var_12 = python_code_.workflow_PetriNet()
    var_13 = python_code_.workflow_Token()
    python_code_.workflow_Place(
        name=var_2,
        targetPlace=var_11,
        workflow_Place=None,
        workflow_Place33=var_12,
        Place39={
            "`sQLP]q": '</{l2oCki"UExw%Y',
            "'j": "_workflow_Role__workflow_Role17:_workflow_EnumField__workflow_EnumField152",
            "8{": True,
        },
        workflow_Place55=var_13,
    )


def test_20():
    var_43 = "O.gd=\x0c\tnk_'$["
    python_code_.workflow_Process(name=var_43, process=[False, False])
    var_52 = python_code_.workflow_EnumFieldAtom
    var_53 = python_code_.workflow_DefaultDocument(placeholder=var_52)
    assert isinstance(var_53, python_code_.workflow_DefaultDocument)


def test_21():
    var_0 = python_code_.Control()
    var_1 = "jZ]"
    var_2 = True
    python_code_.workflow_Case(id=var_1, client=var_1, started=var_2, finished=var_2)
    var_4 = python_code_.workflow_EnumFieldAtom()
    python_code_.workflow_Activity(
        started=var_2,
        finished=var_2,
        workflow_Activity={3210.38, True},
        workflow_Activity15=var_4,
        Activity=var_0,
    )


def test_22():
    var_0 = (
        lambda *args, **kwargs: "_workflow_TaskO__workflow_TaskO1 workflow_String2DocumentMap142 workflow_Document143"
    )
    python_code_.workflow_Role(
        name=var_0,
        workflow_Role21="\tgYPgkm{8}a\nU",
        workflow_Role169=complex(-68.700568, 2662.57),
    )


def test_23():
    var_1 = set()
    var_2 = python_code_.workflow_TaskO(
        name=(), workflow_TaskO=var_1, workflow_TaskO1=var_1
    )
    assert isinstance(var_2, python_code_.workflow_TaskO)
    var_5 = python_code_.workflow_AgentContainer(name=var_2)
    assert isinstance(var_5, python_code_.workflow_AgentContainer)
    var_11 = python_code_.workflow_Organisation(name=var_2, workflow_Organisation=var_1)
    assert isinstance(var_11, python_code_.workflow_Organisation)
    var_14 = python_code_.workflow_EnumFieldValue()
    var_16 = "9J\n%}<iZ%V"
    var_17 = python_code_.workflow_DefaultDocumentCondition
    python_code_.workflow_Role(
        name=var_16, workflow_Role21=var_17, workflow_Role169=var_14
    )


@pytest.mark.xfail(strict=True)
def test_24():
    var_0 = "_workflow_Task__workflow_Task106:workflow_DocumentDescrAtom:_workflow_CoreModel__workflow_CoreModel:_workflow_Arc__in_43"
    var_1 = set()
    var_2 = python_code_.workflow_TaskO(
        name=(), workflow_TaskO=var_1, workflow_TaskO1=var_1
    )
    assert isinstance(var_2, python_code_.workflow_TaskO)
    python_code_.workflow_TaskO(name=var_0, workflow_TaskO=var_1, workflow_TaskO3=var_2)


def test_25():
    var_5 = "t"
    var_6 = python_code_.workflow_TaskC(name=var_5)
    assert isinstance(var_6, python_code_.workflow_TaskC)


def test_26():
    var_2 = python_code_.workflow_Task
    var_3 = python_code_.workflow_DefaultDocument(placeholder=var_2)
    assert isinstance(var_3, python_code_.workflow_DefaultDocument)


@pytest.mark.xfail(strict=True)
def test_27():
    var_0 = python_code_.Control()
    var_1 = "jZ]"
    var_2 = True
    python_code_.workflow_Case(
        id="7;M2LbS0",
        client=var_1,
        started=var_2,
        finished=False,
        core={var_2, -611.4, True},
        workflow_Case8=var_1,
        Case=var_2,
    )
    var_4 = python_code_.workflow_EnumFieldAtom()
    python_code_.workflow_Activity(
        started=var_2,
        finished=var_2,
        workflow_Activity={3210.38, True},
        workflow_Activity15=var_4,
        Activity=var_0,
    )
    var_10 = python_code_.workflow_EnumFieldValue()
    var_14 = "workflow_TaskO1_workflow_EnumLiteral__workflow_EnumLiteral165_workflow_DefaultDocument__workflow_DefaultDocument132"
    var_15 = python_code_.workflow_TaskC(name=var_14)
    assert isinstance(var_15, python_code_.workflow_TaskC)
    python_code_.workflow_DocumentTypeContainer(
        name=(), workflow_DocumentTypeContainer=var_10
    )


def test_28():
    var_3 = python_code_.workflow_ConstantAtom(value=-70)
    assert isinstance(var_3, python_code_.workflow_ConstantAtom)


def test_29():
    var_0 = (
        lambda *args, **kwargs: "_workflow_TaskO__workflow_TaskO1 workflow_String2DocumentMap142 workflow_Document143"
    )
    python_code_.workflow_Role(
        name=var_0,
        workflow_Role21="\tgYPgkm{8}a\nU",
        workflow_Role169=complex(-68.700568, 2662.57),
    )
    var_2 = "_workflow_Document__workflow_Document143"
    var_3 = python_code_.workflow_ProcessO()
    python_code_.workflow_Role(name=var_2, workflow_Role126=var_3)


def test_30():
    python_code_.workflow_Role(name="workflow_DocumentType.workflow_Agent20")


def test_31():
    var_9 = "VVdOp\tC/n\\Soj6c2H="
    python_code_.workflow_RuntimeInformation(caseIdCount=var_9)
    var_11 = python_code_.workflow_CaseO
    var_12 = python_code_.workflow_EnumField(name="uOI_j", workflow_EnumField154=var_11)
    assert isinstance(var_12, python_code_.workflow_EnumField)


@pytest.mark.xfail(strict=True)
def test_32():
    var_0 = (
        lambda *args, **kwargs: "_workflow_TaskO__workflow_TaskO1 workflow_String2DocumentMap142 workflow_Document143"
    )
    var_5 = python_code_.workflow_TaskI()
    var_6 = python_code_.workflow_DocumentCondition(
        name=var_0, workflow_DocumentCondition=var_5
    )
    assert isinstance(var_6, python_code_.workflow_DocumentCondition)
    var_8 = python_code_.workflow_DocumentType(name=complex(808.0, 2070.39502))
    assert isinstance(var_8, python_code_.workflow_DocumentType)
    var_13 = python_code_.workflow_Document(name=var_0, id=None)
    assert isinstance(var_13, python_code_.workflow_Document)
    python_code_.workflow_DocumentType(name=b"*\xd0", workflow_DocumentType82=var_13)


def test_33():
    var_10 = python_code_.DocumentType()
    var_12 = False
    python_code_.workflow_Activity(started=var_12, finished=var_10)


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = (
        lambda *args, **kwargs: "_workflow_TaskO__workflow_TaskO1 workflow_String2DocumentMap142 workflow_Document143"
    )
    var_2 = "YEdcEX#j!XUEkg"
    var_3 = python_code_.workflow_DocumentTypeContainer(name=var_2)
    assert isinstance(var_3, python_code_.workflow_DocumentTypeContainer)
    var_7 = python_code_.workflow_Organisation(
        name="_workflow_Arc__outworkflow_ActivityI78_workflow_DocumentDescriptor__workflow_DocumentDescriptor72"
    )
    assert isinstance(var_7, python_code_.workflow_Organisation)
    var_9 = python_code_.workflow_AgentContainer(name=[])
    assert isinstance(var_9, python_code_.workflow_AgentContainer)
    python_code_.workflow_DocumentContainer(
        name=var_7, workflow_DocumentContainer=var_0
    )


def test_35():
    var_4 = " WgSW"
    var_5 = python_code_.workflow_EnumLiteralAtom()
    var_6 = python_code_.workflow_EnumLiteral(
        name=var_4,
        workflow_EnumLiteral155=[True, 2959, 0],
        workflow_EnumLiteral165=var_5,
    )
    assert isinstance(var_6, python_code_.workflow_EnumLiteral)
    var_9 = python_code_.workflow_TaskC(name=var_4)
    assert isinstance(var_9, python_code_.workflow_TaskC)
    var_14 = python_code_.workflow_DocumentContainer(name=var_4)
    assert isinstance(var_14, python_code_.workflow_DocumentContainer)
    python_code_.workflow_Role(name="workflow_DocumentType.workflow_Agent20")
    var_44 = python_code_.workflow_ModelRegistry()
    python_code_.workflow_CoreModel(name=var_4, coreModels=var_44)


@pytest.mark.xfail(strict=True)
def test_36():
    var_4 = " WgMW"
    var_5 = python_code_.workflow_EnumLiteralAtom()
    var_6 = python_code_.workflow_EnumLiteral(
        name=var_4,
        workflow_EnumLiteral155=[True, 2959, 0],
        workflow_EnumLiteral165=var_5,
    )
    assert isinstance(var_6, python_code_.workflow_EnumLiteral)
    var_7 = python_code_.workflow_OrganisationAspect()
    var_42 = python_code_.workflow_TaskC(name=var_4)
    assert isinstance(var_42, python_code_.workflow_TaskC)
    var_43 = python_code_.RuntimeGlobalAspect()
    var_45 = python_code_.workflow_DocumentTypeContainer(
        name={
            '<cI\x0c\t"Z[': 2732,
            "np7Y5L^6o\rB": False,
            "_workflow_Document__workflow_Document143.in_": -2073,
        }
    )
    assert isinstance(var_45, python_code_.workflow_DocumentTypeContainer)
    var_47 = python_code_.workflow_DocumentContainer(name=var_4)
    assert isinstance(var_47, python_code_.workflow_DocumentContainer)
    var_56 = ""
    var_57 = python_code_.workflow_InformationRuntimeAspect
    var_58 = "o_M-6G,/\x0cGR-"
    var_59 = python_code_.workflow_Document(
        name=var_57, id=var_58, workflow_Document=var_7, workflow_Document143=None
    )
    assert isinstance(var_59, python_code_.workflow_Document)
    var_60 = python_code_.workflow_String2DocumentMap(key=var_58)
    python_code_.workflow_Document(
        name=var_56, id=var_43, workflow_Document81=var_57, workflow_Document143=var_60
    )
