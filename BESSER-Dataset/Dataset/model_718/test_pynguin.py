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
    AggregationKind,
    Artifact,
    Association,
    AssociationEnd,
    AssociationEndRole,
    Attribute,
    BehavioralFeature,
    Binding,
    BooleanExpression,
    CallAction,
    CallConcurrencyKind,
    CallEvent,
    ChangeableKind,
    Classifier,
    Collaboration,
    Comment,
    Component,
    Constraint,
    CreateAction,
    DataType,
    Dependency,
    Element,
    ElementResidence,
    Enum,
    Enumeration,
    EnumerationLiteral,
    Expression,
    Feature,
    Flow,
    GeneralizableElement,
    Generalization_,
    MappingExpression,
    Method,
    ModelElement,
    MultiplicityRange,
    Multiplicity_,
    Namespace,
    Node,
    Operation,
    OrderingKind,
    Parameter,
    ParameterDirectionKind,
    PresentationElement,
    ProcedureExpression,
    PseudostateKind,
    Relationship,
    ScopeKind,
    Signal,
    StateMachine,
    Stereotype,
    StructuralFeature,
    TagDefinition,
    TaggedValue,
    TemplateArgument,
    TemplateParameter,
    TypeExpression,
    VisibilityKind,
    abstractmethod,
    core_Association,
    core_Class,
    core_GeneralizableElement,
    core_Namespace,
    core_Relationship,
    date,
    datetime,
    foundation_core_Abstraction,
    foundation_core_Artifact,
    foundation_core_Association,
    foundation_core_AssociationClass,
    foundation_core_AssociationEnd,
    foundation_core_Attribute,
    foundation_core_BehavioralFeature,
    foundation_core_Binding,
    foundation_core_Class,
    foundation_core_Classifier,
    foundation_core_Comment,
    foundation_core_Component,
    foundation_core_Constraint,
    foundation_core_DataType,
    foundation_core_Dependency,
    foundation_core_Element,
    foundation_core_ElementResidence,
    foundation_core_Enumeration,
    foundation_core_EnumerationLiteral,
    foundation_core_Feature,
    foundation_core_Flow,
    foundation_core_GeneralizableElement,
    foundation_core_Generalization_,
    foundation_core_Interface,
    foundation_core_Method,
    foundation_core_ModelElement,
    foundation_core_Namespace,
    foundation_core_Node,
    foundation_core_Operation,
    foundation_core_Parameter,
    foundation_core_Permission,
    foundation_core_PresentationElement,
    foundation_core_Primitive,
    foundation_core_ProgrammingLanguageDataType,
    foundation_core_Relationship,
    foundation_core_Stereotype,
    foundation_core_StructuralFeature,
    foundation_core_TagDefinition,
    foundation_core_TaggedValue,
    foundation_core_TemplateArgument,
    foundation_core_TemplateParameter,
    foundation_core_Usage,
    foundation_data_types_ActionExpression,
    foundation_data_types_ArgListsExpression,
    foundation_data_types_BooleanExpression,
    foundation_data_types_Expression,
    foundation_data_types_IterationExpression,
    foundation_data_types_MappingExpression,
    foundation_data_types_MultiplicityRange,
    foundation_data_types_Multiplicity_,
    foundation_data_types_ObjectSetExpression,
    foundation_data_types_ProcedureExpression,
    foundation_data_types_TimeExpression,
    foundation_data_types_TypeExpression,
    time,
)


def test_0():
    python_code_.foundation_core_ElementResidence(visibility=-1322.91)


def test_1():
    var_51 = "#trf5f`."
    var_52 = python_code_.foundation_core_PresentationElement()
    python_code_.foundation_core_ElementResidence(
        visibility=var_51, elementResidence=var_52
    )
    var_83 = python_code_.foundation_core_BehavioralFeature(isQuery='B"fW')
    assert isinstance(var_83, python_code_.foundation_core_BehavioralFeature)


@pytest.mark.xfail(strict=True)
def test_2():
    var_5 = python_code_.foundation_data_types_ProcedureExpression()
    var_6 = python_code_.Node()
    var_7 = "#trf5f`."
    var_9 = lambda *args, **kwargs: -907
    var_63 = python_code_.foundation_core_Component
    var_67 = ")Sh!\\ Ck"
    var_68 = "private:_foundation_core_BehavioralFeature__context62"
    var_69 = python_code_.foundation_core_Node()
    var_70 = python_code_.TagDefinition()
    var_71 = {var_70, var_70, var_70, var_70}
    var_72 = "join"
    var_73 = python_code_.foundation_core_Generalization_(discriminator=var_72)
    assert isinstance(var_73, python_code_.foundation_core_Generalization_)
    var_74 = python_code_.foundation_core_Stereotype(
        icon=var_6,
        baseClass=var_7,
        owner115=var_71,
        constrainedStereotype=var_71,
        GeneralizableElement79=("I\x0biB}Z,HqOGBQ b<", 1317, -60),
        GeneralizableElement=var_73,
    )
    assert isinstance(var_74, python_code_.foundation_core_Stereotype)
    var_75 = python_code_.foundation_core_Parameter(
        kind=False,
        foundation_core_Parameter=True,
        typedParameter=var_69,
        ModelElement117=var_74,
        ModelElement83={"ModelElementStereotype123": True},
        ModelElement=var_9,
    )
    assert isinstance(var_75, python_code_.foundation_core_Parameter)
    python_code_.foundation_core_Operation(
        concurrency=var_67,
        isRoot=var_67,
        isLeaf=var_7,
        isAbstract=var_68,
        specification=var_5,
        operation67=var_63,
        BehavioralFeature=var_75,
    )


def test_3():
    var_44 = python_code_.foundation_core_ProgrammingLanguageDataType()
    var_46 = python_code_.MappingExpression()
    var_47 = '3MgJuc5pX(~qh\x0cod".'
    var_48 = "D`\x0b"
    var_49 = "7x_U x"
    var_50 = python_code_.CallAction()
    var_51 = {var_50, var_50}
    var_52 = python_code_.foundation_core_Operation(
        concurrency=var_47,
        isRoot=var_48,
        isLeaf=var_46,
        isAbstract=var_49,
        specification=var_44,
        operation=var_51,
        BehavioralFeature=var_48,
    )
    assert isinstance(var_52, python_code_.foundation_core_Operation)
    var_54 = python_code_.foundation_core_Component
    var_55 = b"lA\xc5\xb3\x1aRP1jaU_\x85p=\xcf\xd4N"
    var_56 = python_code_.foundation_core_Stereotype(
        icon=var_47,
        baseClass=var_52,
        constrainedStereotype=var_47,
        GeneralizableElement79=var_54,
        GeneralizableElement=var_55,
    )
    assert isinstance(var_56, python_code_.foundation_core_Stereotype)


def test_4():
    var_1 = '}lrw*T|j"P'
    var_2 = python_code_.foundation_core_StructuralFeature(
        changeability=var_1, targetScope={0, False, 1586}, ordering=var_1
    )
    assert isinstance(var_2, python_code_.foundation_core_StructuralFeature)
    var_4 = python_code_.Constraint()
    var_9 = python_code_.ElementResidence()
    var_10 = python_code_.Signal()
    var_11 = python_code_.CallAction
    var_12 = set()
    var_13 = python_code_.foundation_core_Stereotype(
        icon="Classifier81", baseClass=var_11, stereotype=var_12
    )
    assert isinstance(var_13, python_code_.foundation_core_Stereotype)
    var_14 = python_code_.foundation_core_Namespace()
    var_15 = python_code_.foundation_core_Dependency()
    var_16 = python_code_.foundation_core_TaggedValue(
        dataValue=var_1,
        ModelElement117=var_13,
        ModelElement83=None,
        ModelElement88=False,
        ModelElement132=var_4,
        ModelElement100=var_9,
        ModelElement98="foundation_core_TemplateParameter:GeneralizableElement79:Constraint119",
        ModelElement=var_14,
        ModelElement85=var_15,
    )
    assert isinstance(var_16, python_code_.foundation_core_TaggedValue)
    var_20 = "TemplateParameter.initial"
    var_21 = python_code_.foundation_core_Constraint()
    var_22 = python_code_.foundation_core_Comment(
        body=var_20,
        ModelElement100=var_10,
        ModelElement98=b"\xa2\xec\t\xb8t\xd0\x94,\xcc\xe9",
        ModelElement49=var_21,
        ModelElement128=[],
    )
    assert isinstance(var_22, python_code_.foundation_core_Comment)
    var_24 = "Classifier46"
    python_code_.foundation_core_TaggedValue(
        dataValue=var_24,
        taggedValue=var_22,
        ModelElement117=var_13,
        ModelElement49=var_21,
        ModelElement128=41.2,
    )


def test_5():
    var_68 = python_code_.core_Class
    var_69 = python_code_.foundation_core_StructuralFeature(
        changeability=var_68,
        targetScope=var_68,
        ordering=var_68,
        foundation_core_StructuralFeature="T\t*P\ne0",
        typedFeature=[],
    )
    assert isinstance(var_69, python_code_.foundation_core_StructuralFeature)
    var_73 = "PresentationElement:GeneralizableElement79:foundation_core_Stereotype"
    var_84 = "D<!Zp'Y/h*"
    var_85 = python_code_.foundation_core_Generalization_(
        discriminator=var_84, specialization=var_68
    )
    assert isinstance(var_85, python_code_.foundation_core_Generalization_)
    var_86 = python_code_.foundation_core_Stereotype(
        icon=(),
        baseClass=var_73,
        GeneralizableElement79=var_85,
        GeneralizableElement=var_85,
    )
    assert isinstance(var_86, python_code_.foundation_core_Stereotype)


def test_6():
    var_5 = '3MgJuc5pX(~qh\x0cod".'
    var_8 = python_code_.CallAction()
    var_9 = {var_8, var_8}
    var_14 = python_code_.foundation_core_Generalization_(
        discriminator=var_5, powertypeRange=var_9
    )
    assert isinstance(var_14, python_code_.foundation_core_Generalization_)


def test_7():
    var_22 = python_code_.foundation_core_ProgrammingLanguageDataType()
    var_24 = python_code_.MappingExpression()
    var_25 = '3MgJuc5pXC(~qh\x0cod".'
    var_26 = "D`1"
    var_27 = "7_U x"
    var_28 = python_code_.CallAction()
    var_29 = {var_28, var_28}
    var_30 = python_code_.foundation_core_Operation(
        concurrency=var_25,
        isRoot=var_26,
        isLeaf=var_24,
        isAbstract=var_27,
        specification=var_22,
        operation=var_29,
        BehavioralFeature=var_26,
    )
    assert isinstance(var_30, python_code_.foundation_core_Operation)


def test_8():
    var_0 = python_code_.core_Association()
    var_1 = b"\x07Ir\x98\xab\x7f"
    var_2 = python_code_.foundation_core_StructuralFeature(
        changeability="fork",
        targetScope="_foundation_core_ModelElement__supplier",
        ordering="VY+SXcu\\i=1SGAr]\\",
        typedFeature=var_0,
        Feature=var_1,
    )
    assert isinstance(var_2, python_code_.foundation_core_StructuralFeature)


def test_9():
    var_1 = python_code_.OrderingKind.unordered
    var_2 = python_code_.foundation_core_StructuralFeature(
        changeability=var_1, targetScope={0, False, 1586}, ordering=var_1
    )
    assert isinstance(var_2, python_code_.foundation_core_StructuralFeature)
    var_42 = python_code_.core_Class
    var_43 = python_code_.foundation_core_StructuralFeature(
        changeability=var_42,
        targetScope=var_42,
        ordering=var_42,
        foundation_core_StructuralFeature="T\t*P\ne0",
        typedFeature=[],
    )
    assert isinstance(var_43, python_code_.foundation_core_StructuralFeature)
    var_68 = python_code_.foundation_core_BehavioralFeature(
        isQuery="*>@\x0c>qFb\tI7lkj"
    )
    assert isinstance(var_68, python_code_.foundation_core_BehavioralFeature)


def test_10():
    var_1 = b"\x07Ir\x98\xab\x7f"
    var_2 = python_code_.foundation_core_StructuralFeature(
        changeability=var_1, targetScope={0, False, 1586}, ordering=var_1
    )
    assert isinstance(var_2, python_code_.foundation_core_StructuralFeature)


def test_11():
    var_1 = python_code_.foundation_data_types_ObjectSetExpression()
    var_2 = python_code_.foundation_core_ModelElement(
        name="Constraint_foundation_core_Parameter__typedParameter",
        visibility='u8q""<o\\',
        isSpecification="?L]]",
        template=set(),
        ownedElement=var_1,
        client=set(),
        target=set(),
    )
    assert isinstance(var_2, python_code_.foundation_core_ModelElement)


def test_12():
    var_1 = python_code_.foundation_data_types_TypeExpression()
    var_2 = python_code_.foundation_core_ModelElement(
        name="",
        visibility="Classifier38",
        isSpecification="QyJ|88`@Z",
        annotatedElement={"tx?<xvz\\t", var_1, var_1},
        subject=set(),
        source=set(),
    )
    assert isinstance(var_2, python_code_.foundation_core_ModelElement)


@pytest.mark.xfail(strict=True)
def test_13():
    var_22 = "CallEvent Constraint119"
    var_23 = int
    var_24 = python_code_.foundation_core_StructuralFeature(
        changeability=var_22,
        targetScope=var_23,
        ordering=[],
        typedFeature=None,
        Feature=None,
    )
    assert isinstance(var_24, python_code_.foundation_core_StructuralFeature)
    var_25 = python_code_.TagDefinition()
    var_26 = {var_25, var_25, var_25, var_25, var_25}
    var_27 = python_code_.foundation_core_Stereotype(
        icon=var_22,
        baseClass=var_22,
        owner115=var_26,
        constrainedStereotype=[],
        GeneralizableElement=b"\xb2\x0e\x0c\xd8\x9b\x91\x86",
    )
    assert isinstance(var_27, python_code_.foundation_core_Stereotype)
    var_35 = python_code_.Artifact()
    var_40 = python_code_.foundation_core_Generalization_(discriminator=var_22)
    assert isinstance(var_40, python_code_.foundation_core_Generalization_)
    var_44 = "x0M&;,oTON-;tyn'\rsr"
    var_45 = "N`i/BJ#)|\x0btmSjz^e"
    var_46 = python_code_.TaggedValue()
    var_47 = {var_46}
    python_code_.foundation_core_ModelElement(
        name=var_22,
        visibility=var_44,
        isSpecification=var_45,
        modelElement=var_47,
        referenceValue=var_47,
        client=var_35,
    )


def test_14():
    var_0 = python_code_.Signal()
    var_77 = "mL6E?/@}9W"
    var_78 = python_code_.foundation_core_StructuralFeature(
        changeability={False},
        targetScope=var_77,
        ordering=var_77,
        Feature={False, -2616.39, 892.51},
    )
    assert isinstance(var_78, python_code_.foundation_core_StructuralFeature)
    var_80 = python_code_.VisibilityKind.package
    var_81 = python_code_.foundation_core_PresentationElement()
    var_82 = python_code_.foundation_core_TemplateArgument()
    var_83 = python_code_.foundation_core_GeneralizableElement(
        isRoot=var_80,
        isLeaf=-2193,
        isAbstract=var_77,
        ModelElement111=(
            "_foundation_core_AssociationEnd__specifiedEnd-ModelElement96-TaggedValue17-TaggedValue17",
        ),
        ModelElement88=var_81,
        ModelElement96=("Flow10",),
        ModelElement138=var_82,
    )
    assert isinstance(var_83, python_code_.foundation_core_GeneralizableElement)
    var_89 = "TemplateParameter.initial"
    var_90 = python_code_.foundation_core_Constraint()
    var_91 = python_code_.foundation_core_Comment(
        body=var_89,
        ModelElement100=var_0,
        ModelElement98=b"\xa2\xec\t\xb8t\xd0\x94,\xcc\xe9",
        ModelElement49=var_90,
        ModelElement128=[],
    )
    assert isinstance(var_91, python_code_.foundation_core_Comment)


def test_15():
    var_0 = "!\r(qEk8Y"
    var_1 = python_code_.foundation_core_TemplateArgument()
    var_2 = python_code_.foundation_core_Dependency()
    var_3 = python_code_.foundation_core_Parameter(
        kind=var_0, ModelElement138=var_1, ModelElement85=var_2
    )
    assert isinstance(var_3, python_code_.foundation_core_Parameter)


def test_16():
    var_0 = "!\r(qEk8Y"
    var_1 = python_code_.foundation_core_TemplateArgument()
    var_2 = python_code_.foundation_core_Dependency()
    var_3 = python_code_.foundation_core_Parameter(
        kind=var_0, ModelElement138=var_1, ModelElement85=var_2
    )
    assert isinstance(var_3, python_code_.foundation_core_Parameter)
    var_4 = "aggregate"
    var_5 = python_code_.BehavioralFeature()
    var_6 = python_code_.Classifier()
    var_7 = ":HH[ub^4"
    var_8 = python_code_.foundation_core_ElementResidence(visibility=var_7)
    var_9 = python_code_.foundation_core_Constraint()
    python_code_.foundation_core_Parameter(
        kind=var_4,
        foundation_core_Parameter=var_2,
        parameter=var_5,
        typedParameter=var_6,
        ModelElement117={
            "-\tejWt~\x0cY&ahE": False,
            "foundation_core_Comment": "Expression",
        },
        ModelElement102=var_8,
        ModelElement100=var_0,
        ModelElement98=var_4,
        ModelElement49=var_9,
    )


def test_17():
    var_27 = "7_U R"
    var_28 = python_code_.CallAction()
    var_29 = {var_28, var_28}
    var_30 = python_code_.foundation_core_Operation(
        concurrency=var_27,
        isRoot="bClrCN\x0cG7",
        isLeaf="?<`ei?(;#ioTJ",
        isAbstract=var_27,
        specification="{:AL%B1`|",
        operation67=set(),
        representedOperation=var_29,
    )
    assert isinstance(var_30, python_code_.foundation_core_Operation)
    var_44 = python_code_.foundation_core_Constraint()
    var_45 = python_code_.MappingExpression
    var_46 = python_code_.foundation_core_Feature(
        ownerScope=complex(2181.9018157, 2552.434),
        feature=b"\xf7\x7f\x06",
        ModelElement98=complex(-2625.0, 2621.0),
        ModelElement49=var_44,
        ModelElement=var_45,
        ModelElement85=var_45,
    )
    assert isinstance(var_46, python_code_.foundation_core_Feature)


def test_18():
    var_1 = python_code_.Attribute()
    var_4 = python_code_.foundation_data_types_IterationExpression()
    var_6 = python_code_.Constraint
    var_7 = python_code_.foundation_core_Flow()
    var_8 = python_code_.foundation_core_Feature(
        ownerScope=var_4,
        ModelElement108=var_6,
        ModelElement111=var_1,
        ModelElement100=var_7,
    )
    assert isinstance(var_8, python_code_.foundation_core_Feature)
    var_9 = python_code_.foundation_core_Class(
        isActive=[False, '#qUQ\x0bZG"rD+e k\nkk4&'], Classifier=var_8
    )
    assert isinstance(var_9, python_code_.foundation_core_Class)
    var_10 = "x9k3CmB~~#X"
    var_11 = "@!"
    var_12 = "RC>tmh"
    var_13 = python_code_.foundation_core_Operation(
        concurrency=var_10,
        isRoot=-65.89,
        isLeaf=var_11,
        isAbstract=var_12,
        specification={
            "": False,
            "Constraint119 foundation_core_StructuralFeature _foundation_core_BehavioralFeature__behavioralFeature _foundation_core_Generalization___generalization": ";tiD2dN,|k?k#",
        },
        BehavioralFeature=var_7,
    )
    assert isinstance(var_13, python_code_.foundation_core_Operation)
    var_17 = "ADO*UyW?[UC@h"
    var_18 = python_code_.Component()
    python_code_.foundation_core_ElementResidence(
        visibility=var_17, residentElement=var_18
    )


def test_19():
    var_2 = python_code_.foundation_core_StructuralFeature(
        changeability="!n\t<2\x0bt",
        targetScope="_foundation_core_Parameter__typedParameter._foundation_core_TaggedValue__taggedValue.ModelElement",
        ordering="_foundation_core_StructuralFeature__typedFeature,_foundation_core_GeneralizableElement__parent",
        Feature=None,
    )
    assert isinstance(var_2, python_code_.foundation_core_StructuralFeature)
    var_6 = python_code_.Comment()
    var_50 = python_code_.foundation_core_BehavioralFeature(isQuery='B"fW')
    assert isinstance(var_50, python_code_.foundation_core_BehavioralFeature)
    var_54 = python_code_.foundation_core_Component()
    var_55 = "AiEM$#E` `R_$k"
    var_56 = python_code_.foundation_core_Dependency()
    var_57 = python_code_.Method
    var_58 = python_code_.foundation_core_TemplateParameter()
    var_59 = python_code_.foundation_core_PresentationElement()
    var_60 = python_code_.foundation_core_TaggedValue(
        dataValue=var_57,
        taggedValue=var_6,
        ModelElement108=var_58,
        ModelElement83=var_56,
        ModelElement88=var_59,
        ModelElement96='t^JHMID`V(P\nCw$^"',
    )
    assert isinstance(var_60, python_code_.foundation_core_TaggedValue)
    var_61 = python_code_.foundation_core_Feature(
        ownerScope=var_55,
        feature=var_54,
        ModelElement83=var_56,
        ModelElement132=var_60,
        ModelElement102={"y.^", 1770},
        ModelElement85=-1979.22,
    )
    assert isinstance(var_61, python_code_.foundation_core_Feature)


def test_20():
    var_7 = python_code_.foundation_core_Component()
    var_10 = python_code_.Multiplicity_()
    var_11 = python_code_.core_Association()
    var_12 = python_code_.Relationship()
    var_13 = python_code_.core_Class
    var_14 = python_code_.foundation_core_StructuralFeature(
        changeability=var_13,
        targetScope=var_13,
        ordering=var_13,
        foundation_core_StructuralFeature="T\t*P\ne0",
        typedFeature=[],
    )
    assert isinstance(var_14, python_code_.foundation_core_StructuralFeature)
    var_18 = "PresentationElement:GeneralizableElement79:foundation_core_Stereotype"
    var_19 = python_code_.foundation_core_TemplateParameter()
    var_20 = python_code_.foundation_core_Flow()
    var_21 = python_code_.foundation_core_Feature(
        ownerScope=var_18,
        ModelElement111=var_19,
        ModelElement83=var_13,
        ModelElement102=True,
        ModelElement100=var_20,
        ModelElement=var_10,
    )
    assert isinstance(var_21, python_code_.foundation_core_Feature)
    var_26 = python_code_.Generalization_()
    var_32 = python_code_.Stereotype()
    var_33 = python_code_.foundation_core_TagDefinition(
        tagType=1891,
        foundation_core_TagDefinition=var_11,
        definedTag=var_32,
        type125="Ym'\tZ7&yGI",
    )
    assert isinstance(var_33, python_code_.foundation_core_TagDefinition)
    var_43 = "guarded"
    python_code_.foundation_core_TagDefinition(
        tagType=var_43,
        definedTag=var_32,
        ModelElement98=var_20,
        ModelElement49=var_26,
        ModelElement106=var_19,
        ModelElement138=var_12,
        ModelElement85=var_7,
    )


def test_21():
    var_1 = b"\xc4"
    var_2 = python_code_.foundation_core_StructuralFeature(
        changeability=var_1, targetScope={0, False, 1586}, ordering=var_1
    )
    assert isinstance(var_2, python_code_.foundation_core_StructuralFeature)
    var_4 = python_code_.Constraint()
    var_43 = python_code_.foundation_core_ElementResidence(visibility=-1322.91)
    var_49 = python_code_.MappingExpression()
    var_51 = "Xj"
    var_55 = python_code_.StructuralFeature()
    var_56 = python_code_.foundation_core_Classifier
    var_57 = python_code_.foundation_core_Namespace()
    var_58 = python_code_.foundation_core_TagDefinition(
        tagType=var_51,
        ModelElement108=var_56,
        ModelElement102=var_43,
        ModelElement98=var_55,
        ModelElement96=var_49,
        ModelElement=var_57,
        ModelElement138=var_56,
        ModelElement85=var_4,
    )
    assert isinstance(var_58, python_code_.foundation_core_TagDefinition)


def test_22():
    var_0 = python_code_.core_Relationship()
    var_4 = python_code_.foundation_core_Flow()
    var_5 = python_code_.Classifier()
    var_8 = python_code_.Multiplicity_()
    var_9 = lambda *args, **kwargs: "4wO./)qjMrc6/s"
    var_10 = python_code_.foundation_core_Constraint()
    var_11 = python_code_.foundation_core_TagDefinition(
        tagType=False,
        foundation_core_TagDefinition=var_8,
        definedTag=var_0,
        ModelElement117=var_9,
        ModelElement83=var_9,
        ModelElement49=var_10,
        ModelElement=var_9,
    )
    assert isinstance(var_11, python_code_.foundation_core_TagDefinition)
    var_12 = python_code_.foundation_core_TemplateArgument()
    var_14 = "_foundation_core_Parameter__typedParameter"
    var_15 = python_code_.foundation_core_BehavioralFeature(isQuery=var_14)
    assert isinstance(var_15, python_code_.foundation_core_BehavioralFeature)
    python_code_.foundation_data_types_MultiplicityRange(lower=var_5, upper=var_14)
    var_20 = python_code_.foundation_data_types_BooleanExpression()
    var_23 = python_code_.foundation_core_Dependency()
    var_24 = python_code_.foundation_core_PresentationElement()
    var_25 = python_code_.foundation_core_Flow()
    var_26 = python_code_.foundation_core_Namespace()
    python_code_.foundation_core_TagDefinition(
        tagType=True,
        ModelElement83=var_23,
        ModelElement88=var_24,
        ModelElement132=var_14,
        ModelElement102=b"\x17\x08\x9e\xc4L,",
        ModelElement100=var_4,
        ModelElement98=var_25,
        ModelElement106=var_9,
        ModelElement=var_26,
        ModelElement138=var_12,
    )
    python_code_.foundation_data_types_Expression(body=var_20, language=237)


def test_23():
    python_code_.DataType()


def test_24():
    var_1 = '}lrw*T|j"P'
    var_2 = python_code_.foundation_core_StructuralFeature(
        changeability=var_1, targetScope={0, False, 1586}, ordering=var_1
    )
    assert isinstance(var_2, python_code_.foundation_core_StructuralFeature)
    var_38 = python_code_.VisibilityKind.package
    var_39 = python_code_.foundation_core_PresentationElement()
    var_40 = python_code_.foundation_core_TemplateArgument()
    var_41 = python_code_.foundation_core_GeneralizableElement(
        isRoot=var_38,
        isLeaf=-2193,
        isAbstract=var_1,
        ModelElement111=(
            "_foundation_core_AssociationEnd__specifiedEnd-ModelElement96-TaggedValue17-TaggedValue17",
        ),
        ModelElement88=var_39,
        ModelElement96=("Flow10",),
        ModelElement138=var_40,
    )
    assert isinstance(var_41, python_code_.foundation_core_GeneralizableElement)


def test_25():
    var_27 = "7_U R"
    var_28 = python_code_.CallAction()
    var_29 = {var_28, var_28}
    var_30 = python_code_.foundation_core_Operation(
        concurrency=var_27,
        isRoot="bClrCN\x0cG7",
        isLeaf="?<`ei?(;#ioTJ",
        isAbstract=var_27,
        specification="{:AL%B1`|",
        operation67=set(),
        representedOperation=var_29,
    )
    assert isinstance(var_30, python_code_.foundation_core_Operation)


def test_26():
    var_2 = python_code_.foundation_data_types_ArgListsExpression
    var_3 = python_code_.foundation_core_Classifier()
    var_4 = python_code_.foundation_core_BehavioralFeature(isQuery=var_2, Feature=var_3)
    assert isinstance(var_4, python_code_.foundation_core_BehavioralFeature)


@pytest.mark.xfail(strict=True)
def test_27():
    var_4 = "n"
    var_5 = python_code_.foundation_core_Generalization_(
        discriminator=var_4, powertypeRange=-1249.52, generalization=-383.61
    )
    assert isinstance(var_5, python_code_.foundation_core_Generalization_)
    var_7 = "ElementResidence TaggedValue"
    var_9 = lambda *args, **kwargs: False
    var_14 = set()
    python_code_.foundation_core_Stereotype(
        icon=(),
        baseClass=[-3202.54, False],
        owner115=var_14,
        stereotype=var_9,
        constrainedStereotype=var_14,
        GeneralizableElement79=var_7,
    )


@pytest.mark.xfail(strict=True)
def test_28():
    var_4 = "G"
    var_5 = python_code_.foundation_core_Generalization_(
        discriminator=var_4, powertypeRange=-1249.52, generalization=-383.61
    )
    assert isinstance(var_5, python_code_.foundation_core_Generalization_)
    var_6 = "shallowHistory"
    var_7 = "ElementResidence TaggedValue"
    var_8 = "kDAmM}Ma]jp6:\r#OqV"
    var_9 = lambda *args, **kwargs: False
    var_10 = python_code_.foundation_core_Dependency()
    python_code_.foundation_core_GeneralizableElement(
        isRoot=var_6,
        isLeaf=var_7,
        isAbstract=var_8,
        parent=3,
        ModelElement108=[-1173.7, 1483, "*X)5XW\nzia\n="],
        ModelElement83=var_9,
        ModelElement85=var_10,
    )


def test_29():
    var_2 = python_code_.foundation_core_ModelElement(
        name="!VZ\x0c{xgsyD ",
        visibility="_foundation_core_BehavioralFeature__behavioralFeature",
        isSpecification="!RYm[o$:e",
        annotatedElement=set(),
        context=set(),
        client=set(),
        constrainedElement=set(),
    )
    assert isinstance(var_2, python_code_.foundation_core_ModelElement)
    var_3 = python_code_.Signal()
    var_6 = "mL6,E?/@}9W"
    var_7 = python_code_.foundation_core_StructuralFeature(
        changeability="\\jj=",
        targetScope=var_6,
        ordering="8x\n^51u@:i\x0bDV\r #_$",
        typedFeature=var_3,
    )
    assert isinstance(var_7, python_code_.foundation_core_StructuralFeature)


def test_30():
    var_0 = python_code_.core_Association()
    var_2 = python_code_.foundation_core_StructuralFeature(
        changeability="lorkR+fL\x0c8;0UXO+",
        targetScope=".5FkMn-.",
        ordering="Namespace",
        typedFeature=var_0,
        Feature=None,
    )
    assert isinstance(var_2, python_code_.foundation_core_StructuralFeature)
    var_44 = python_code_.foundation_core_BehavioralFeature(
        isQuery="_foundation_core_TaggedValue__taggedValue"
    )
    assert isinstance(var_44, python_code_.foundation_core_BehavioralFeature)
    var_49 = python_code_.foundation_core_TemplateArgument
    var_50 = "_foundation_coreModelElement__modelElement"
    python_code_.foundation_data_types_MultiplicityRange(lower=var_49, upper=var_50)


@pytest.mark.xfail(strict=True)
def test_31():
    var_0 = python_code_.foundation_core_PresentationElement()
    var_6 = python_code_.Namespace()
    var_7 = "FLvl]LD==elY\x0c2oP2"
    var_8 = python_code_.foundation_core_Stereotype(icon=var_6, baseClass=var_7)
    assert isinstance(var_8, python_code_.foundation_core_Stereotype)
    var_9 = python_code_.Relationship()
    var_10 = python_code_.TagDefinition()
    var_16 = python_code_.foundation_data_types_ProcedureExpression()
    var_20 = python_code_.foundation_core_TemplateParameter()
    var_21 = python_code_.foundation_core_Flow()
    python_code_.foundation_core_TaggedValue(
        dataValue=var_0,
        referenceTag=var_10,
        ModelElement108=var_20,
        ModelElement83=var_9,
        ModelElement132=var_16,
        ModelElement98=var_21,
    )


def test_32():
    var_17 = "ADO*UyW?[UC@h"
    var_18 = python_code_.Component()
    python_code_.foundation_core_ElementResidence(
        visibility=var_17, residentElement=var_18
    )
