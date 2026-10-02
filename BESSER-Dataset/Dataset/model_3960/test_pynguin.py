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
    Abstraction,
    Association,
    BehavioralFeature,
    Class,
    ClassesProv_Abstraction,
    ClassesProv_Association,
    ClassesProv_AssociationClass,
    ClassesProv_BehavioralFeature,
    ClassesProv_Class,
    ClassesProv_Classifier,
    ClassesProv_Constraint,
    ClassesProv_DataType,
    ClassesProv_Dependency,
    ClassesProv_DirectedRelationship,
    ClassesProv_Element,
    ClassesProv_ElementImport,
    ClassesProv_Enumeration,
    ClassesProv_EnumerationLiteral,
    ClassesProv_Expression,
    ClassesProv_Feature,
    ClassesProv_Generalization,
    ClassesProv_GeneralizationSet,
    ClassesProv_InstanceSpecification,
    ClassesProv_InstanceValue,
    ClassesProv_Interface,
    ClassesProv_InterfaceRealization,
    ClassesProv_LiteralBoolean,
    ClassesProv_LiteralInteger,
    ClassesProv_LiteralNull,
    ClassesProv_LiteralReal,
    ClassesProv_LiteralSpecification,
    ClassesProv_LiteralString,
    ClassesProv_LiteralUnilimitedNatural,
    ClassesProv_MultiplicityElement,
    ClassesProv_NamedElement,
    ClassesProv_Namespace,
    ClassesProv_OpaqueExpression,
    ClassesProv_Operation,
    ClassesProv_Package,
    ClassesProv_PackageImport,
    ClassesProv_PackageMerge,
    ClassesProv_PackageableElement,
    ClassesProv_Parameter,
    ClassesProv_PrimitiveType,
    ClassesProv_Property,
    ClassesProv_Realization,
    ClassesProv_RedefinableElement,
    ClassesProv_Relationship,
    ClassesProv_Slot,
    ClassesProv_StructuralFeature,
    ClassesProv_Substitution,
    ClassesProv_Type,
    ClassesProv_TypedElement,
    ClassesProv_Usage,
    ClassesProv_ValueSpecification,
    Classifier,
    DataType,
    Dependency,
    DirectedRelationship,
    Element,
    Feature,
    InstanceSpecification,
    LiteralSpecification,
    MultiplicityElement,
    NamedElement,
    Namespace,
    PackageableElement,
    Realization,
    RedefinableElement,
    Relationship,
    StructuralFeature,
    Type,
    TypedElement,
    ValueSpecification,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = False
    var_1 = python_code_.ClassesProv_Relationship
    var_2 = python_code_.ClassesProv_Operation(
        isQuery={},
        isOrdered=None,
        isUnique=var_0,
        upper=var_1,
        lower=var_0,
        ClassesProv_Operation191=var_0,
        ClassesProv_Operation204=var_0,
    )
    assert isinstance(var_2, python_code_.ClassesProv_Operation)
    var_46 = "ClassesProv_PackageMerge"
    var_47 = python_code_.ClassesProv_Type()
    var_48 = int
    var_49 = python_code_.ClassesProv_Package(
        URI=var_46,
        ClassesProv_Package74=var_47,
        ClassesProv_Package43=var_46,
        ClassesProv_Package235=var_48,
    )
    assert isinstance(var_49, python_code_.ClassesProv_Package)
    var_56 = "ClassesProv_Namespace17"
    var_57 = python_code_.ClassesProv_OpaqueExpression(body=var_56, language=var_46)
    assert isinstance(var_57, python_code_.ClassesProv_OpaqueExpression)
    var_59 = True
    var_60 = python_code_.ClassesProv_RedefinableElement(isLeaf=var_59)
    assert isinstance(var_60, python_code_.ClassesProv_RedefinableElement)


@pytest.mark.xfail(strict=True)
def test_1():
    var_3 = python_code_.ClassesProv_Type()
    var_7 = python_code_.ClassesProv_BehavioralFeature()
    var_14 = python_code_.ClassesProv_Slot()
    var_16 = "$6"
    var_18 = bool
    var_19 = True
    var_21 = True
    var_22 = False
    var_24 = True
    var_25 = False
    var_26 = False
    var_27 = {"Q"}
    var_28 = python_code_.ClassesProv_Property(
        isDerived=var_22,
        isDerivedUnion=var_21,
        default=var_16,
        isComposite=var_7,
        isID=var_26,
        ClassesProv_Property135=var_19,
        ClassesProv_Property133=var_27,
        ClassesProv_Property154=var_27,
        ClassesProv_Property210=b"\xc6\xa4\xa9",
        ClassesProv_Property137=var_7,
        ClassesProv_Property151=var_18,
        ClassesProv_Property219=None,
        ClassesProv_Property257=None,
    )
    assert isinstance(var_28, python_code_.ClassesProv_Property)
    python_code_.ClassesProv_Property(
        isDerived=var_24,
        isDerivedUnion=var_19,
        default=var_16,
        isComposite=var_25,
        isID=var_19,
        ClassesProv_Property159=var_28,
        ClassesProv_Property144=var_14,
        ClassesProv_Property142=var_28,
        ClassesProv_Property=var_21,
        ClassesProv_Property257=var_3,
    )


def test_2():
    var_0 = python_code_.ClassesProv_LiteralReal()
    var_1 = python_code_.ClassesProv_Feature(
        isStatic=-1028.45, ClassesProv_Feature=var_0
    )
    assert isinstance(var_1, python_code_.ClassesProv_Feature)


def test_3():
    var_0 = python_code_.ValueSpecification()
    var_1 = python_code_.ClassesProv_NamedElement(
        name=var_0, qualifiedName="ClassesProv_Feature129"
    )
    assert isinstance(var_1, python_code_.ClassesProv_NamedElement)
    var_2 = python_code_.ClassesProv_ElementImport(
        alias=var_0,
        ClassesProv_ElementImport26=b"\xba\x891\x0e\xbd\x9b\x94\x07\xc5\xe1p(@z\x8e\x01\x0f",
    )
    assert isinstance(var_2, python_code_.ClassesProv_ElementImport)
    var_4 = python_code_.ClassesProv_LiteralUnilimitedNatural()
    var_5 = "OE-Amg1',Hz{"
    var_6 = python_code_.ClassesProv_OpaqueExpression(body=var_4, language=var_5)
    assert isinstance(var_6, python_code_.ClassesProv_OpaqueExpression)
    var_7 = python_code_.ClassesProv_Expression(symbol=True)
    assert isinstance(var_7, python_code_.ClassesProv_Expression)
    var_14 = True
    var_15 = python_code_.ClassesProv_Slot()
    var_16 = python_code_.ClassesProv_StructuralFeature(
        isReadOnly=var_14, ClassesProv_StructuralFeature=var_15
    )
    assert isinstance(var_16, python_code_.ClassesProv_StructuralFeature)


def test_4():
    var_8 = python_code_.ClassesProv_LiteralBoolean()
    var_10 = python_code_.ClassesProv_StructuralFeature(isReadOnly=var_8)
    assert isinstance(var_10, python_code_.ClassesProv_StructuralFeature)
    var_33 = "UW[N/%"
    var_34 = python_code_.ClassesProv_OpaqueExpression(body=var_33, language=var_33)
    assert isinstance(var_34, python_code_.ClassesProv_OpaqueExpression)
    var_35 = (
        lambda *args, **kwargs: "ClassesProv_Property139:_ClassesProv_StructuralFeature__ClassesProv_StructuralFeature:ClassesProv_Class203"
    )
    var_36 = python_code_.ClassesProv_ElementImport(
        alias=var_35, ClassesProv_ElementImport23=var_35
    )
    assert isinstance(var_36, python_code_.ClassesProv_ElementImport)


def test_5():
    var_0 = True
    var_1 = python_code_.ClassesProv_Relationship
    var_2 = python_code_.ClassesProv_Operation(
        isQuery=False,
        isOrdered=True,
        isUnique=var_0,
        upper=2431,
        lower=var_0,
        ClassesProv_Operation185={"7i/G\t,KK((\x0bNnaxe8A", var_1},
        ClassesProv_Operation191=None,
        ClassesProv_Operation194=None,
        ClassesProv_Operation260=var_0,
    )
    assert isinstance(var_2, python_code_.ClassesProv_Operation)
    var_47 = python_code_.ClassesProv_PackageableElement()
    var_51 = "^)c}'2D6yVb:X#}nqSB"
    var_53 = python_code_.ClassesProv_RedefinableElement(isLeaf=var_47)
    assert isinstance(var_53, python_code_.ClassesProv_RedefinableElement)
    var_54 = set()
    var_55 = python_code_.ClassesProv_RedefinableElement(
        isLeaf=[3144, 2, "K{X{i\x0bwGn=?''YB#%n"],
        ClassesProv_RedefinableElement=var_53,
        ClassesProv_RedefinableElement104=var_54,
    )
    var_56 = {var_53, var_55, var_53}
    python_code_.ClassesProv_RedefinableElement(
        isLeaf=[
            "~2/f_M{e.t",
            "ClassesProv_ConstraintClassesProv_Classifier127ClassesProv_Package36",
        ],
        ClassesProv_RedefinableElement104=var_56,
        ClassesProv_RedefinableElement107=var_54,
    )
    var_67 = python_code_.ClassesProv_Association(
        isDerived=True, ClassesProv_Association212=var_54
    )
    assert isinstance(var_67, python_code_.ClassesProv_Association)
    var_72 = python_code_.ClassesProv_ElementImport(
        alias=var_51,
        ClassesProv_ElementImport23=var_47,
        ClassesProv_ElementImport26={"|": -3979, '^\x0b2"x}=a': -1151.54},
    )
    assert isinstance(var_72, python_code_.ClassesProv_ElementImport)


def test_6():
    var_63 = set()
    var_86 = python_code_.ClassesProv_OpaqueExpression(
        body="ClassesProv_ValueSpecification178_ClassesProv_Association__ClassesProv_Association149",
        language="_ClassesProv_Feature__ClassesProv_Feature129ClassesProv_Classifier123",
    )
    assert isinstance(var_86, python_code_.ClassesProv_OpaqueExpression)
    var_91 = python_code_.Namespace
    var_92 = python_code_.ClassesProv_Association(
        isDerived=-2988,
        ClassesProv_Association149=var_91,
        ClassesProv_Association218=var_63,
    )
    assert isinstance(var_92, python_code_.ClassesProv_Association)
    var_96 = "xI,`9k7[1$\x0b[7H00"
    var_97 = python_code_.ClassesProv_Parameter(default=var_96)
    assert isinstance(var_97, python_code_.ClassesProv_Parameter)


@pytest.mark.xfail(strict=True)
def test_7():
    var_17 = python_code_.ClassesProv_Class()
    var_19 = True
    var_20 = True
    var_21 = False
    python_code_.ClassesProv_Association(
        isDerived=var_19,
        ClassesProv_Association=var_17,
        ClassesProv_Association149=var_21,
        ClassesProv_Association215=var_20,
    )


def test_8():
    var_75 = "UW[N/%"
    var_76 = python_code_.ClassesProv_OpaqueExpression(body=var_75, language=var_75)
    assert isinstance(var_76, python_code_.ClassesProv_OpaqueExpression)


def test_9():
    var_0 = python_code_.ValueSpecification()
    var_1 = python_code_.ClassesProv_NamedElement(
        name=var_0, qualifiedName="ClassesProv_Feature129"
    )
    assert isinstance(var_1, python_code_.ClassesProv_NamedElement)
    var_2 = python_code_.ClassesProv_ElementImport(
        alias=var_0,
        ClassesProv_ElementImport26=b"\xba\x891\x0e\xbd\x9b\x94\x07\xc5\xe1p(@z\x8e\x01\x0f",
    )
    assert isinstance(var_2, python_code_.ClassesProv_ElementImport)
    var_7 = python_code_.ClassesProv_Expression(symbol=True)
    assert isinstance(var_7, python_code_.ClassesProv_Expression)


def test_10():
    var_43 = python_code_.ClassesProv_Namespace()
    var_51 = "_ClassesProv_NamedElement__ClassesProv_NamedElement.ClassesProv_ValueSpecification178.ClassesProv_Association215.ClassesProv_Classifier113"
    var_52 = python_code_.ClassesProv_Dependency()
    var_53 = {var_52, var_52}
    var_54 = python_code_.ClassesProv_NamedElement(
        name=var_51,
        qualifiedName=var_51,
        ClassesProv_NamedElement=var_43,
        ClassesProv_NamedElement7=var_53,
        ClassesProv_NamedElement15=var_43,
    )
    assert isinstance(var_54, python_code_.ClassesProv_NamedElement)
    var_55 = {var_54, var_54, var_54}
    var_56 = False
    var_57 = python_code_.ClassesProv_Feature(
        isStatic=var_56, ClassesProv_Feature129=var_53
    )
    assert isinstance(var_57, python_code_.ClassesProv_Feature)
    var_76 = False
    var_77 = python_code_.ClassesProv_LiteralInteger
    var_78 = python_code_.ClassesProv_GeneralizationSet(
        isCovering=var_76,
        isDisjoint=b"\x87\x1b\x00E\xf5G\xb5\n\xc7\x16\xe6*",
        ClassesProv_GeneralizationSet168=var_77,
        ClassesProv_GeneralizationSet267=var_55,
    )
    assert isinstance(var_78, python_code_.ClassesProv_GeneralizationSet)
    var_63 = "}/r??.VE)0N'F("
    var_64 = python_code_.ClassesProv_OpaqueExpression(body=var_63, language=var_63)
    assert isinstance(var_64, python_code_.ClassesProv_OpaqueExpression)
    var_69 = python_code_.Namespace
    var_70 = python_code_.ClassesProv_Association(
        isDerived=-2988,
        ClassesProv_Association149=var_69,
        ClassesProv_Association218=var_53,
    )
    assert isinstance(var_70, python_code_.ClassesProv_Association)
    var_74 = "xI,`9k7[1$\x0b[7H00"
    var_75 = python_code_.ClassesProv_Parameter(default=var_74)
    assert isinstance(var_75, python_code_.ClassesProv_Parameter)


def test_11():
    var_81 = python_code_.StructuralFeature()
    var_82 = python_code_.TypedElement()
    var_87 = True
    var_88 = python_code_.ClassesProv_Generalization(
        isSubstitutable=None, ClassesProv_Generalization164=var_81
    )
    assert isinstance(var_88, python_code_.ClassesProv_Generalization)
    var_89 = python_code_.ClassesProv_GeneralizationSet(
        isCovering=var_82, isDisjoint=var_87, ClassesProv_GeneralizationSet168=var_88
    )
    assert isinstance(var_89, python_code_.ClassesProv_GeneralizationSet)


@pytest.mark.xfail(strict=True)
def test_12():
    var_5 = python_code_.ClassesProv_Interface()
    var_8 = python_code_.ClassesProv_LiteralBoolean()
    var_10 = python_code_.ClassesProv_StructuralFeature(isReadOnly=var_8)
    assert isinstance(var_10, python_code_.ClassesProv_StructuralFeature)
    var_16 = python_code_.StructuralFeature()
    var_17 = python_code_.TypedElement()
    var_18 = True
    var_19 = False
    var_20 = python_code_.ClassesProv_InterfaceRealization
    var_21 = set()
    var_22 = True
    var_23 = python_code_.ClassesProv_Generalization(
        isSubstitutable=None, ClassesProv_Generalization164=var_16
    )
    assert isinstance(var_23, python_code_.ClassesProv_Generalization)
    var_24 = python_code_.ClassesProv_GeneralizationSet(
        isCovering=var_17, isDisjoint=var_22, ClassesProv_GeneralizationSet168=var_23
    )
    assert isinstance(var_24, python_code_.ClassesProv_GeneralizationSet)
    python_code_.ClassesProv_Classifier(
        isAbstract=var_18,
        isFinalSpecialization=var_19,
        ClassesProv_Classifier=var_20,
        ClassesProv_Classifier162=None,
        ClassesProv_Classifier201=var_20,
        ClassesProv_Classifier125=var_21,
        ClassesProv_Classifier265=var_24,
        ClassesProv_Classifier251=var_5,
    )


def test_13():
    var_0 = False
    var_1 = python_code_.ClassesProv_Relationship
    var_2 = python_code_.ClassesProv_Operation(
        isQuery=var_0,
        isOrdered=True,
        isUnique=False,
        upper=var_0,
        lower=0,
        ClassesProv_Operation185=set(),
        ClassesProv_Operation194=var_0,
        ClassesProv_Operation260=var_0,
        ClassesProv_Operation225=var_1,
    )
    assert isinstance(var_2, python_code_.ClassesProv_Operation)
    var_3 = python_code_.ClassesProv_DataType()
    var_11 = python_code_.ClassesProv_GeneralizationSet(
        isCovering=var_3,
        isDisjoint=None,
        ClassesProv_GeneralizationSet=var_0,
        ClassesProv_GeneralizationSet264=None,
    )
    assert isinstance(var_11, python_code_.ClassesProv_GeneralizationSet)
    var_47 = False
    var_48 = python_code_.ClassesProv_Generalization(isSubstitutable=var_47)
    assert isinstance(var_48, python_code_.ClassesProv_Generalization)


@pytest.mark.xfail(strict=True)
def test_14():
    var_0 = False
    var_1 = python_code_.ClassesProv_Relationship
    var_3 = python_code_.ClassesProv_DataType()
    var_8 = python_code_.ClassesProv_Namespace()
    var_11 = python_code_.ClassesProv_GeneralizationSet(
        isCovering=var_3,
        isDisjoint=None,
        ClassesProv_GeneralizationSet=var_0,
        ClassesProv_GeneralizationSet264=None,
    )
    assert isinstance(var_11, python_code_.ClassesProv_GeneralizationSet)
    var_16 = False
    var_17 = "_ClassesProv_NamedElement__ClassesProv_NamedElement.ClassesProv_ValueSpecification178.ClassesProv_Association215.ClassesProv_Classifier113"
    var_18 = python_code_.ClassesProv_Dependency()
    var_19 = {var_18, var_18}
    var_20 = python_code_.ClassesProv_NamedElement(
        name=var_17,
        qualifiedName=var_17,
        ClassesProv_NamedElement=var_8,
        ClassesProv_NamedElement7=var_19,
        ClassesProv_NamedElement15=var_8,
    )
    assert isinstance(var_20, python_code_.ClassesProv_NamedElement)
    var_21 = {var_20, var_20, var_20}
    var_22 = python_code_.ClassesProv_Classifier(
        isAbstract=var_1,
        isFinalSpecialization=var_1,
        ClassesProv_Classifier110=var_21,
        ClassesProv_Classifier115=(538.61,),
        ClassesProv_Classifier121=-713.04,
        ClassesProv_Classifier125=var_19,
        ClassesProv_Classifier245={},
    )
    assert isinstance(var_22, python_code_.ClassesProv_Classifier)
    python_code_.ClassesProv_Generalization(
        isSubstitutable=var_16, ClassesProv_Generalization161=var_22
    )


@pytest.mark.xfail(strict=True)
def test_15():
    var_2 = python_code_.ClassesProv_PackageImport()
    var_4 = python_code_.DirectedRelationship()
    var_7 = False
    var_8 = python_code_.ValueSpecification
    var_9 = python_code_.ClassesProv_InstanceSpecification()
    var_10 = False
    var_11 = True
    var_12 = python_code_.ClassesProv_Generalization(
        isSubstitutable=var_11, ClassesProv_Generalization164=var_9
    )
    assert isinstance(var_12, python_code_.ClassesProv_Generalization)
    var_13 = set()
    var_14 = python_code_.ClassesProv_GeneralizationSet(
        isCovering=var_10,
        isDisjoint=var_7,
        ClassesProv_GeneralizationSet168=var_12,
        ClassesProv_GeneralizationSet267=var_13,
    )
    assert isinstance(var_14, python_code_.ClassesProv_GeneralizationSet)
    var_15 = {var_14, var_14, var_14}
    python_code_.ClassesProv_Classifier(
        isAbstract=-417.01,
        isFinalSpecialization=var_4,
        ClassesProv_Classifier113=var_8,
        ClassesProv_Classifier119={
            "ClassesProv_PackageImport29 _ClassesProv_Operation__ClassesProv_Operation _ClassesProv_Generalization__ClassesProv_Generalization167": True,
            "_ClassesProv_Property__ClassesProv_Property148ClassesProv_Classifier130_ClassesProv_Property__ClassesProv_Property216_ClassesProv_Classifier__ClassesProv_Classifier119": -2681.89,
        },
        ClassesProv_Classifier127=var_15,
        ClassesProv_Classifier265=var_2,
    )


def test_16():
    var_0 = python_code_.ClassesProv_LiteralReal()
    var_1 = python_code_.ClassesProv_Feature(
        isStatic=-1028.45, ClassesProv_Feature=var_0
    )
    assert isinstance(var_1, python_code_.ClassesProv_Feature)
    var_8 = "ClassesProv_PackageMerge"
    var_9 = python_code_.ClassesProv_Type()
    var_10 = python_code_.ClassesProv_LiteralString
    var_11 = python_code_.ClassesProv_Package(
        URI=var_8,
        ClassesProv_Package74=var_9,
        ClassesProv_Package43=var_8,
        ClassesProv_Package235=var_10,
    )
    assert isinstance(var_11, python_code_.ClassesProv_Package)


def test_17():
    var_38 = False
    var_39 = python_code_.ClassesProv_Generalization(isSubstitutable=var_38)
    assert isinstance(var_39, python_code_.ClassesProv_Generalization)


def test_18():
    var_0 = True
    var_1 = python_code_.ClassesProv_Relationship
    var_2 = python_code_.ClassesProv_Operation(
        isQuery=False,
        isOrdered=True,
        isUnique=var_0,
        upper=2431,
        lower=var_0,
        ClassesProv_Operation185={"7i/G\t,KK((\x0bNnaxe8A", var_1},
        ClassesProv_Operation191=None,
        ClassesProv_Operation194=None,
        ClassesProv_Operation260=var_0,
    )
    assert isinstance(var_2, python_code_.ClassesProv_Operation)
    var_47 = python_code_.ClassesProv_PackageableElement()
    var_53 = python_code_.ClassesProv_RedefinableElement(isLeaf=var_47)
    assert isinstance(var_53, python_code_.ClassesProv_RedefinableElement)
    var_54 = set()
    var_55 = python_code_.ClassesProv_RedefinableElement(
        isLeaf=[3144, 2, "K{X{i\x0bwGn=?''YB#%n"],
        ClassesProv_RedefinableElement=var_53,
        ClassesProv_RedefinableElement104=var_54,
    )
    var_56 = {var_53, var_55, var_53}
    python_code_.ClassesProv_RedefinableElement(
        isLeaf=[
            "~2/f_M{e.t",
            "ClassesProv_ConstraintClassesProv_Classifier127ClassesProv_Package36",
        ],
        ClassesProv_RedefinableElement104=var_56,
        ClassesProv_RedefinableElement107=var_54,
    )


def test_19():
    var_0 = python_code_.ClassesProv_LiteralReal()
    var_1 = python_code_.ClassesProv_Feature(
        isStatic=-1028.45, ClassesProv_Feature=var_0
    )
    assert isinstance(var_1, python_code_.ClassesProv_Feature)
    var_13 = "ClassesProv_Namespace17"
    var_14 = python_code_.ClassesProv_OpaqueExpression(body=var_13, language=var_13)
    assert isinstance(var_14, python_code_.ClassesProv_OpaqueExpression)
    var_16 = True
    var_17 = python_code_.ClassesProv_RedefinableElement(isLeaf=var_16)
    assert isinstance(var_17, python_code_.ClassesProv_RedefinableElement)


def test_20():
    var_4 = python_code_.ClassesProv_PackageableElement()
    var_7 = python_code_.TypedElement()
    var_8 = python_code_.ClassesProv_PackageImport()
    var_11 = False
    var_12 = python_code_.ClassesProv_Generalization(isSubstitutable=var_11)
    assert isinstance(var_12, python_code_.ClassesProv_Generalization)
    var_17 = '.DFBf|LA"FLDC'
    var_18 = python_code_.ClassesProv_Expression(symbol=var_17)
    assert isinstance(var_18, python_code_.ClassesProv_Expression)
    var_20 = True
    var_21 = python_code_.ClassesProv_MultiplicityElement(
        isOrdered=var_11,
        isUnique=var_20,
        upper=var_7,
        lower=complex(2857.22, -2142.8789),
        ClassesProv_MultiplicityElement59=var_8,
    )
    assert isinstance(var_21, python_code_.ClassesProv_MultiplicityElement)
    var_25 = python_code_.ClassesProv_ElementImport(
        alias=var_17,
        ClassesProv_ElementImport23=var_4,
        ClassesProv_ElementImport26={"|": -3979, '^\x0b2"x}=a': -1151.54},
    )
    assert isinstance(var_25, python_code_.ClassesProv_ElementImport)
    var_26 = python_code_.ClassesProv_RedefinableElement(
        isLeaf=complex(-277.56, 2757.00142)
    )
    assert isinstance(var_26, python_code_.ClassesProv_RedefinableElement)


def test_21():
    var_0 = True
    var_1 = python_code_.ClassesProv_InstanceSpecification
    var_2 = python_code_.ClassesProv_Operation(
        isQuery=False,
        isOrdered=True,
        isUnique=var_0,
        upper=2431,
        lower=var_0,
        ClassesProv_Operation185={"7i/G\t,KK((\x0bNnaxe8A", var_1},
        ClassesProv_Operation191=None,
        ClassesProv_Operation194=None,
        ClassesProv_Operation260=var_0,
    )
    assert isinstance(var_2, python_code_.ClassesProv_Operation)
    var_47 = python_code_.ClassesProv_PackageableElement()
    var_53 = python_code_.ClassesProv_RedefinableElement(isLeaf=var_47)
    assert isinstance(var_53, python_code_.ClassesProv_RedefinableElement)
    var_87 = '.DFBf|LA"FLDC'
    var_88 = python_code_.ClassesProv_Expression(symbol=var_87)
    assert isinstance(var_88, python_code_.ClassesProv_Expression)


def test_22():
    var_0 = python_code_.ValueSpecification()
    var_1 = python_code_.ClassesProv_NamedElement(
        name=var_0, qualifiedName="ClassesProv_Feature129"
    )
    assert isinstance(var_1, python_code_.ClassesProv_NamedElement)
    var_2 = python_code_.ClassesProv_ElementImport(
        alias=var_0,
        ClassesProv_ElementImport26=b"\xba\x891\x0e\xbd\x9b\x94\x07\xc5\xe1p(@z\x8e\x01\x0f",
    )
    assert isinstance(var_2, python_code_.ClassesProv_ElementImport)
    var_4 = python_code_.ClassesProv_LiteralUnilimitedNatural()
    var_5 = "OE-Amg1',Hz{"
    var_6 = python_code_.ClassesProv_OpaqueExpression(body=var_4, language=var_5)
    assert isinstance(var_6, python_code_.ClassesProv_OpaqueExpression)
    var_7 = python_code_.ClassesProv_Expression(symbol=True)
    assert isinstance(var_7, python_code_.ClassesProv_Expression)
    var_10 = python_code_.ClassesProv_LiteralReal()
    var_14 = True
    var_15 = python_code_.ClassesProv_Slot()
    var_16 = python_code_.ClassesProv_StructuralFeature(
        isReadOnly=var_14, ClassesProv_StructuralFeature=var_15
    )
    assert isinstance(var_16, python_code_.ClassesProv_StructuralFeature)
    var_23 = lambda *args, **kwargs: "_R?9eQ.kz"
    var_24 = python_code_.ClassesProv_Parameter(
        default=var_23, ClassesProv_Parameter174=var_10
    )
    assert isinstance(var_24, python_code_.ClassesProv_Parameter)


def test_23():
    var_66 = python_code_.ClassesProv_Enumeration()
    var_73 = "ClassesProv_Slot"
    var_74 = python_code_.ClassesProv_BehavioralFeature()
    var_75 = python_code_.ClassesProv_Parameter(
        default=var_73,
        ClassesProv_Parameter=b"\x81\xbb\x9d^\x8c\xbc\x90~\x0c\x9c\xff\x84\xb2X",
        ClassesProv_Parameter174=var_74,
    )
    assert isinstance(var_75, python_code_.ClassesProv_Parameter)
    var_76 = False
    var_77 = python_code_.ClassesProv_Feature(
        isStatic=var_76, ClassesProv_Feature=var_66
    )
    assert isinstance(var_77, python_code_.ClassesProv_Feature)


def test_24():
    var_3 = python_code_.ClassesProv_ValueSpecification()
    var_4 = "ClassesProv_PackageMerge"
    var_7 = python_code_.ClassesProv_Package(
        URI="!g2Zx NOj",
        ClassesProv_Package74=None,
        ClassesProv_Package33={2630},
        ClassesProv_Package235=var_3,
    )
    assert isinstance(var_7, python_code_.ClassesProv_Package)
    var_14 = "CElassesProv_Namespace17"
    var_15 = python_code_.ClassesProv_OpaqueExpression(body=var_14, language=var_4)
    assert isinstance(var_15, python_code_.ClassesProv_OpaqueExpression)


def test_25():
    var_4 = python_code_.ClassesProv_PackageableElement()
    var_7 = python_code_.TypedElement()
    var_8 = python_code_.ClassesProv_PackageImport()
    var_11 = False
    var_12 = python_code_.ClassesProv_Generalization(isSubstitutable=var_11)
    assert isinstance(var_12, python_code_.ClassesProv_Generalization)
    var_17 = '.DFBf|LA"FLDC'
    var_18 = python_code_.ClassesProv_Expression(symbol=var_17)
    assert isinstance(var_18, python_code_.ClassesProv_Expression)
    var_20 = True
    var_21 = python_code_.ClassesProv_MultiplicityElement(
        isOrdered=var_11,
        isUnique=var_20,
        upper=var_7,
        lower=complex(2857.22, -2142.8789),
        ClassesProv_MultiplicityElement59=var_8,
    )
    assert isinstance(var_21, python_code_.ClassesProv_MultiplicityElement)
    var_25 = python_code_.ClassesProv_ElementImport(
        alias=var_17,
        ClassesProv_ElementImport23=var_4,
        ClassesProv_ElementImport26={"|": -3979, '^\x0b2"x}=a': -1151.54},
    )
    assert isinstance(var_25, python_code_.ClassesProv_ElementImport)
    var_26 = python_code_.ClassesProv_RedefinableElement(
        isLeaf=complex(-277.56, 2757.00142)
    )
    assert isinstance(var_26, python_code_.ClassesProv_RedefinableElement)
    python_code_.ClassesProv_ElementImport(alias=1588, ClassesProv_ElementImport=var_25)


def test_26():
    var_9 = python_code_.ClassesProv_ValueSpecification()
    var_15 = python_code_.ClassesProv_Interface()
    var_16 = "$6"
    var_23 = True
    var_61 = True
    var_62 = python_code_.ClassesProv_MultiplicityElement(
        isOrdered=var_61,
        isUnique=[],
        upper=var_16,
        lower=var_15,
        ClassesProv_MultiplicityElement55=var_9,
        ClassesProv_MultiplicityElement62=var_23,
    )
    assert isinstance(var_62, python_code_.ClassesProv_MultiplicityElement)


def test_27():
    var_1 = python_code_.ClassesProv_LiteralUnilimitedNatural()
    var_43 = python_code_.ClassesProv_Namespace()
    var_51 = "_ClassesProv_NamedElement__ClassesProv_NamedElement.ClassesProv_ValueSpecification178.ClassesProv_Association215.ClassesProv_Classifier113"
    var_52 = python_code_.ClassesProv_Dependency()
    var_53 = {var_52, var_52}
    var_54 = python_code_.ClassesProv_NamedElement(
        name=var_51,
        qualifiedName=var_51,
        ClassesProv_NamedElement=var_43,
        ClassesProv_NamedElement7=var_53,
        ClassesProv_NamedElement15=var_43,
    )
    assert isinstance(var_54, python_code_.ClassesProv_NamedElement)
    var_56 = False
    var_57 = python_code_.ClassesProv_Feature(
        isStatic=var_56, ClassesProv_Feature129=var_53
    )
    assert isinstance(var_57, python_code_.ClassesProv_Feature)
    var_63 = "}/r??.VE)0N'F("
    var_64 = python_code_.ClassesProv_OpaqueExpression(body=var_63, language=var_63)
    assert isinstance(var_64, python_code_.ClassesProv_OpaqueExpression)
    var_81 = -610
    var_82 = python_code_.ClassesProv_Operation(
        isQuery=var_1,
        isOrdered=var_63,
        isUnique=None,
        upper=var_81,
        lower={
            "_ClassesProv_Association__ClassesProv_Association149",
            "_ClassesProv_GeneralizationSet__ClassesProv_GeneralizationSet267:ClassesProv_Dependency237:ClassesProv_Namespace27:ClassesProv_Property159",
        },
        ClassesProv_Operation204=complex(-5425.214, -893.083),
        ClassesProv_Operation260={},
    )
    assert isinstance(var_82, python_code_.ClassesProv_Operation)
