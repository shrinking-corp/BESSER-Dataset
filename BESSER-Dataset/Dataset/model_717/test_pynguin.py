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
    BehavioralFeature,
    Classifier,
    Dependency,
    DirectedRelationship,
    Element,
    Enum,
    Feature,
    NamedElement,
    Namespace,
    PackageableElement,
    Realization,
    Relationship,
    Type,
    TypedElement,
    VisibilityKind,
    abstractmethod,
    date,
    datetime,
    time,
    uml_Abstraction,
    uml_Association,
    uml_BehavioralFeature,
    uml_Class,
    uml_Classifier,
    uml_Comment,
    uml_Dependency,
    uml_DirectedRelationship,
    uml_Element,
    uml_ElementImport,
    uml_Feature,
    uml_Generalization,
    uml_Model,
    uml_NamedElement,
    uml_Namespace,
    uml_Operation,
    uml_Package,
    uml_PackageImport,
    uml_PackageableElement,
    uml_Parameter,
    uml_Property,
    uml_Realization,
    uml_Relationship,
    uml_Substitution,
    uml_Type,
    uml_TypedElement,
    uml_ValueSpecification,
)


def test_0():
    var_0 = "_uml_Classifier__uml_Classifier60_uml_Property__uml_Property93uml_Type83"
    var_1 = python_code_.uml_ElementImport(
        visibility=var_0, alias=[], ElementImport="p:K4h \x0b\nRN6I"
    )
    assert isinstance(var_1, python_code_.uml_ElementImport)
    var_2 = python_code_.Type()
    var_5 = "o_P`Vr~Z!5"
    var_6 = lambda *args, **kwargs: "Z#!l7i>9?Y+FvT"
    var_7 = python_code_.uml_Operation(
        isQuery=var_0,
        isOrdered=var_5,
        isUnique=var_1,
        lower=[],
        upper=var_6,
        uml_Operation78=var_2,
        uml_Operation76=var_5,
    )
    assert isinstance(var_7, python_code_.uml_Operation)
    var_9 = "'k]GjMu"
    python_code_.uml_Operation(
        isQuery=var_9,
        isOrdered=var_9,
        isUnique=None,
        lower=var_0,
        upper=var_9,
        ownedOperation=var_6,
        uml_Operation=None,
    )


def test_1():
    var_3 = python_code_.Namespace()
    var_6 = python_code_.uml_Abstraction()
    var_7 = "_uml_Classifier__uml_Classifier86-ownedType-uml_Classifier63"
    var_14 = "uml_Class"
    var_15 = python_code_.uml_Operation(
        isQuery=var_7,
        isOrdered=var_7,
        isUnique=var_3,
        lower=var_7,
        upper=var_14,
        ownedOperation=var_7,
        uml_Operation=var_6,
    )
    assert isinstance(var_15, python_code_.uml_Operation)


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = python_code_.Dependency()
    var_2 = python_code_.uml_Abstraction()
    var_7 = str
    var_8 = "uml_Property64 _uml_Class__Class"
    var_9 = "Dependency"
    var_23 = "^\n.:cDgq"
    var_24 = python_code_.uml_Operation(
        isQuery=var_7,
        isOrdered=var_23,
        isUnique=var_2,
        lower=var_1,
        upper="|Xq;-#${m_r.",
    )
    assert isinstance(var_24, python_code_.uml_Operation)
    var_25 = python_code_.uml_Operation(
        isQuery=var_7,
        isOrdered=var_9,
        isUnique=var_23,
        lower=var_9,
        upper=True,
        uml_Operation78=var_24,
    )
    assert isinstance(var_25, python_code_.uml_Operation)
    var_26 = set()
    python_code_.uml_Class(
        isActive=var_9,
        name=var_8,
        Class=var_24,
        uml_Class=None,
        uml_Class85=var_26,
        uml_Class88=var_26,
        uml_Class95=var_26,
    )


def test_3():
    var_1 = python_code_.uml_ValueSpecification()
    var_9 = "L t>wCyu>W\r:ZR3"
    python_code_.uml_Property(name=var_9, uml_Property93=var_1)


def test_4():
    var_1 = python_code_.uml_ValueSpecification()
    var_3 = "clientDependency"
    var_4 = python_code_.uml_Classifier(
        isAbstract=var_3,
        uml_Classifier86=var_1,
        uml_Classifier98=None,
        uml_Classifier="*08\x0c@`-4t)|A%[f']a",
        uml_Classifier55={
            "_uml_Classifier__uml_Classifier55-uml_Property45-_uml_Class__uml_Class90-_uml_Classifier__uml_Classifier55": -816,
            "%\\XG;.\\H>.\rI)": -1,
        },
    )
    assert isinstance(var_4, python_code_.uml_Classifier)
    var_5 = "_uml_Class__Class"
    var_6 = python_code_.uml_Association(isDerived=var_5)
    assert isinstance(var_6, python_code_.uml_Association)
    var_7 = python_code_.uml_Property(
        name=var_3, uml_Property64=var_4, uml_Property74=var_4, uml_Property=var_6
    )
    assert isinstance(var_7, python_code_.uml_Property)


def test_5():
    var_10 = '\x0be0!D5lBWoe"'
    var_13 = "_uml_Class__Class"
    var_14 = python_code_.uml_Association(isDerived=var_13)
    assert isinstance(var_14, python_code_.uml_Association)
    var_15 = python_code_.uml_Property(
        name="uml_Package37", uml_Property64=None, uml_Property45=var_14
    )
    assert isinstance(var_15, python_code_.uml_Property)
    var_17 = python_code_.uml_Model(name=var_10)
    assert isinstance(var_17, python_code_.uml_Model)


def test_6():
    var_1 = python_code_.uml_ValueSpecification()
    var_3 = "clientDependency"
    var_4 = python_code_.uml_Classifier(
        isAbstract=var_3,
        uml_Classifier86=var_1,
        uml_Classifier98=None,
        uml_Classifier="*08\x0c@`-4t)|A%[f']a",
        uml_Classifier55={
            "_uml_Classifier__uml_Classifier55-uml_Property45-_uml_Class__uml_Class90-_uml_Classifier__uml_Classifier55": -816,
            "%\\XG;.\\H>.\rI)": -1,
        },
    )
    assert isinstance(var_4, python_code_.uml_Classifier)
    var_5 = "_uml_Class__Class"
    var_6 = python_code_.uml_Association(isDerived=var_5)
    assert isinstance(var_6, python_code_.uml_Association)
    var_7 = python_code_.uml_Property(
        name=var_5, uml_Property93=var_4, uml_Property51=var_6
    )
    assert isinstance(var_7, python_code_.uml_Property)


@pytest.mark.xfail(strict=True)
def test_7():
    var_1 = python_code_.uml_ValueSpecification()
    var_2 = '\x0be0!D5lBWoe"'
    var_3 = "clientDependency"
    var_4 = python_code_.uml_Classifier(
        isAbstract=var_3,
        uml_Classifier86=var_1,
        uml_Classifier98=None,
        uml_Classifier="*08\x0c@`-4t)|A%[f']a",
        uml_Classifier55={
            "_uml_Classifier__uml_Classifier55-uml_Property45-_uml_Class__uml_Class90-_uml_Classifier__uml_Classifier55": -816,
            "%\\XG;.\\H>.\rI)": -1,
        },
    )
    assert isinstance(var_4, python_code_.uml_Classifier)
    var_5 = "_uml_Class__Class"
    var_6 = python_code_.uml_Association(isDerived=var_5)
    assert isinstance(var_6, python_code_.uml_Association)
    var_7 = python_code_.uml_Property(
        name=var_3, uml_Property64=var_4, uml_Property74=var_4, uml_Property=var_6
    )
    assert isinstance(var_7, python_code_.uml_Property)
    python_code_.uml_Class(
        isActive=True,
        name=var_2,
        Class={'X}U?\x0c"?,("2u6eG{': -1212},
        uml_Class=var_7,
        class_=var_1,
    )


def test_8():
    var_1 = python_code_.uml_ValueSpecification()
    var_9 = "L t>wCyu>W\r:ZR"
    var_12 = python_code_.uml_Class(
        isActive="W1\t:Sz>!;bUcR42P", name=var_9, uml_Class=None, uml_Class90=var_1
    )
    assert isinstance(var_12, python_code_.uml_Class)
    var_13 = python_code_.uml_Generalization(isSubstitutable=b"D^\xec")
    assert isinstance(var_13, python_code_.uml_Generalization)


def test_9():
    var_1 = python_code_.uml_ValueSpecification()
    var_9 = "L t>wCyu>W\r:ZR"
    var_12 = python_code_.uml_Class(
        isActive="Ml$W4M o[H",
        name=var_9,
        uml_Class92={
            -366,
            "_uml_Classifier__Classifier69.uml_Namespace.uml_Classifier58.uml_Substitution",
            var_9,
        },
        uml_Class88=set(),
        uml_Class95={var_1, var_9},
    )
    assert isinstance(var_12, python_code_.uml_Class)


def test_10():
    var_30 = "^\n.:cDgq"
    var_32 = python_code_.uml_Association(
        isDerived=complex(2991.8, -407.8674), uml_Association44=set()
    )
    assert isinstance(var_32, python_code_.uml_Association)
    var_43 = python_code_.uml_PackageImport(visibility="fy &Q0'\\T-c~jlGC&wx")
    assert isinstance(var_43, python_code_.uml_PackageImport)
    var_45 = python_code_.uml_Substitution()
    var_48 = python_code_.BehavioralFeature
    var_49 = "*b;!ARa"
    python_code_.uml_Parameter(
        default=var_48, isException=var_49, isStream=[-670, -1773.48, 1514]
    )
    python_code_.uml_Property(name=449.81)
    var_53 = "iWygzshSfq_XGAbQRp"
    var_54 = python_code_.uml_PackageableElement()
    var_55 = python_code_.uml_BehavioralFeature(
        isAbstract=var_54, uml_BehavioralFeature={"uml_Namespace"}
    )
    assert isinstance(var_55, python_code_.uml_BehavioralFeature)
    var_56 = "uml_Class private"
    var_57 = {var_45}
    var_58 = python_code_.uml_Class(isActive=var_30, name=var_48)
    assert isinstance(var_58, python_code_.uml_Class)
    var_59 = python_code_.uml_Classifier(
        isAbstract=var_53,
        substitutingClassifier=var_57,
        uml_Classifier86=var_58,
        uml_Classifier67=var_45,
        featuringClassifier=var_57,
        uml_Classifier58=[],
    )
    assert isinstance(var_59, python_code_.uml_Classifier)
    var_60 = python_code_.uml_Property(name=var_56, uml_Property64=var_59)
    assert isinstance(var_60, python_code_.uml_Property)
    var_61 = python_code_.uml_Model(name=var_53)
    assert isinstance(var_61, python_code_.uml_Model)


def test_11():
    var_1 = python_code_.uml_ValueSpecification()
    var_3 = "clientDependency"
    var_4 = python_code_.uml_Classifier(
        isAbstract=var_3,
        uml_Classifier86=var_1,
        uml_Classifier98=None,
        uml_Classifier="*08\x0c@`-4t)|A%[f']a",
        uml_Classifier55={
            "_uml_Classifier__uml_Classifier55-uml_Property45-_uml_Class__uml_Class90-_uml_Classifier__uml_Classifier55": -816,
            "%\\XG;.\\H>.\rI)": -1,
        },
    )
    assert isinstance(var_4, python_code_.uml_Classifier)


def test_12():
    var_1 = python_code_.uml_ValueSpecification()
    var_11 = python_code_.uml_Feature(isStatic=(-583.47,), Feature=var_1)
    assert isinstance(var_11, python_code_.uml_Feature)
    var_14 = "_uml_Operation__uml_Operation78-uml_Classifier-_uml_NamedElement__ownedMember-_uml_Package__Package"
    var_15 = python_code_.uml_Property(name=var_14)
    var_16 = {var_15}
    var_17 = python_code_.uml_Classifier(
        isAbstract={},
        uml_Classifier63=var_16,
        featuringClassifier=var_16,
        uml_Classifier58=var_16,
    )
    assert isinstance(var_17, python_code_.uml_Classifier)
    var_24 = python_code_.uml_Association(
        isDerived=complex(2991.8, -407.8674), uml_Association44=set()
    )
    assert isinstance(var_24, python_code_.uml_Association)


@pytest.mark.xfail(strict=True)
def test_13():
    var_14 = python_code_.uml_PackageableElement
    python_code_.uml_Property(name=var_14, uml_Property45=var_14)
    python_code_.uml_Classifier(
        isAbstract=complex(3142.888, -609.0394),
        substitutingClassifier={"K": -1, '"FM"-~IpFINQ=jVo2': 332},
        Classifier69=var_14,
        uml_Classifier98=var_14,
        uml_Classifier67=var_14,
        uml_Classifier=var_14,
    )


def test_14():
    var_1 = python_code_.uml_ValueSpecification()
    var_11 = python_code_.uml_Feature(isStatic=(-583.47,), Feature=var_1)
    assert isinstance(var_11, python_code_.uml_Feature)
    var_13 = '@b"\tx'
    var_14 = "_uml_Operation__uml_Operation78-uml_Classifier-_uml_NamedElement__ownedMember-_uml_Package__Package"
    var_15 = python_code_.uml_Property(name=var_14)
    var_16 = {var_15}
    var_17 = python_code_.uml_Classifier(
        isAbstract={},
        uml_Classifier63=var_16,
        featuringClassifier=var_16,
        uml_Classifier58=var_16,
    )
    assert isinstance(var_17, python_code_.uml_Classifier)
    var_18 = {var_17, var_17}
    var_19 = python_code_.uml_Classifier(
        isAbstract=var_13, uml_Classifier57=644.81, uml_Classifier58=var_18
    )
    assert isinstance(var_19, python_code_.uml_Classifier)
    var_21 = {var_17}
    var_22 = python_code_.uml_Feature(isStatic=var_13, feature=var_21)
    assert isinstance(var_22, python_code_.uml_Feature)


def test_15():
    var_1 = lambda *args, **kwargs: "*\x0cv$zmT93BbZ"
    var_2 = set()
    var_3 = python_code_.uml_Substitution()
    var_4 = python_code_.uml_Classifier(
        isAbstract=var_1,
        uml_Classifier63=var_2,
        uml_Classifier86=set(),
        uml_Classifier67=var_3,
        uml_Classifier57=[],
        uml_Classifier60=var_1,
        uml_Classifier58=var_2,
    )
    assert isinstance(var_4, python_code_.uml_Classifier)
    var_6 = python_code_.uml_Abstraction()
    var_25 = "_uml_Operation__um@l_Operation78-uml_Classifier-_uml_NamedElement__ownedMember-_uml_Package__Package"
    var_26 = python_code_.uml_Property(
        name=var_25, uml_Property74=var_4, uml_Property=var_6
    )
    var_27 = {var_26}
    var_28 = python_code_.uml_Classifier(
        isAbstract={},
        uml_Classifier63=var_27,
        featuringClassifier=var_27,
        uml_Classifier58=var_27,
    )
    assert isinstance(var_28, python_code_.uml_Classifier)
    var_29 = {var_28, var_28}
    var_30 = python_code_.uml_Classifier(
        isAbstract=var_25, uml_Classifier57=644.81, uml_Classifier58=var_29
    )
    assert isinstance(var_30, python_code_.uml_Classifier)
    var_32 = {var_28}
    var_33 = python_code_.uml_Feature(isStatic="!\x0cG(r'$kJtpc", feature=var_32)
    assert isinstance(var_33, python_code_.uml_Feature)


def test_16():
    var_12 = "^\n.:cDgq"
    var_13 = set()
    var_14 = python_code_.uml_Classifier(
        isAbstract=var_12, uml_Classifier57=644.81, uml_Classifier58=var_13
    )
    assert isinstance(var_14, python_code_.uml_Classifier)
    var_16 = {var_14}
    var_17 = python_code_.uml_Feature(isStatic=var_12, feature=var_16)
    assert isinstance(var_17, python_code_.uml_Feature)


def test_17():
    var_14 = "ownedOperation _uml_BehavioralFeature__uml_BehavioralFeature"
    var_15 = "class_"
    var_16 = python_code_.uml_ElementImport(visibility=var_14, alias=var_15)
    assert isinstance(var_16, python_code_.uml_ElementImport)
    var_19 = ".{>x4J1)"
    var_20 = python_code_.uml_PackageImport(visibility=var_19)
    assert isinstance(var_20, python_code_.uml_PackageImport)


def test_18():
    var_1 = python_code_.uml_ValueSpecification()
    var_9 = "L t>wCyu>W\r:ZR"
    var_11 = python_code_.uml_Association(isDerived=var_9)
    assert isinstance(var_11, python_code_.uml_Association)
    var_12 = python_code_.uml_Class(
        isActive="Ml$W4M o[H",
        name=var_9,
        uml_Class92={
            -366,
            "_uml_Classifier__Classifier69.uml_Namespace.uml_Classifier58.uml_Substitution",
            var_9,
        },
        uml_Class88=set(),
        uml_Class95={var_1, var_9},
    )
    assert isinstance(var_12, python_code_.uml_Class)


def test_19():
    var_16 = "-DS]\x0c?Du#&kLy"
    var_17 = python_code_.uml_Type()
    var_18 = {var_17, var_17}
    var_19 = python_code_.uml_Package(name=var_16, package=var_18, Package=var_16)
    assert isinstance(var_19, python_code_.uml_Package)


def test_20():
    var_0 = python_code_.PackageableElement()
    var_5 = python_code_.Abstraction()
    var_7 = "_uml_Classifier__uml_Classifier86-ownedType-uml_Classifier63"
    var_8 = python_code_.uml_NamedElement(
        name=-2562, visibility=var_7, qualifiedName=var_5, uml_NamedElement26=var_0
    )
    assert isinstance(var_8, python_code_.uml_NamedElement)
    var_9 = python_code_.Feature()
    var_10 = python_code_.uml_Package(name=b"h\x99", Package=var_9)
    assert isinstance(var_10, python_code_.uml_Package)


@pytest.mark.xfail(strict=True)
def test_21():
    var_29 = "_uml_Classifier__uml_Classifier63 uml_PackageableElement33 namespace _uml_Generalization__uml_Generalization97"
    var_30 = python_code_.uml_Generalization(
        isSubstitutable=var_29, uml_Generalization97=var_29
    )
    assert isinstance(var_30, python_code_.uml_Generalization)
    var_31 = 'r}"m(;AVgA5XuermZ'
    var_33 = "ln-h\nnoVQf?eCRa"
    var_34 = python_code_.TypedElement
    var_40 = python_code_.uml_Association(
        isDerived=complex(2991.8, -407.8674), uml_Association44=set()
    )
    assert isinstance(var_40, python_code_.uml_Association)
    python_code_.uml_NamedElement(
        name=var_33,
        visibility=complex(1075.1, -2387.0),
        qualifiedName=var_34,
        client=var_34,
        ownedMember=var_34,
        uml_NamedElement=var_31,
    )


def test_22():
    var_0 = python_code_.Feature()
    var_1 = "uml_NamedElement54,uml_Parameter80,_uml_Classifier__uml_Classifier98"
    var_2 = "5z[d\rFRtqFtmNtHPg@p"
    var_3 = python_code_.uml_Namespace()
    var_4 = python_code_.uml_NamedElement(
        name=var_1,
        visibility=var_1,
        qualifiedName=var_2,
        ownedMember=var_0,
        NamedElement31=var_3,
    )
    assert isinstance(var_4, python_code_.uml_NamedElement)


def test_23():
    var_1 = python_code_.uml_ValueSpecification()
    var_9 = "L t>wCyu>W\r:ZR"
    var_12 = python_code_.uml_Class(
        isActive="W1\t:Sz>!;bUcR42P", name=var_9, uml_Class=None, uml_Class90=var_1
    )
    assert isinstance(var_12, python_code_.uml_Class)
    var_18 = python_code_.uml_Model(name={'pJc"i])5:0R~Ux+iE ': 2183})
    assert isinstance(var_18, python_code_.uml_Model)
    var_19 = "uml_Class"
    var_20 = lambda *args, **kwargs: -29
    var_21 = python_code_.uml_NamedElement(
        name=var_9, visibility=var_18, qualifiedName=var_19, NamedElement31=var_20
    )
    assert isinstance(var_21, python_code_.uml_NamedElement)


def test_24():
    var_4 = "_uml_Generalization__uml_Generalization97"
    var_5 = python_code_.uml_Comment(body=var_4, uml_Comment8=-556.25)
    assert isinstance(var_5, python_code_.uml_Comment)
    var_44 = "_uml_Class__Class"
    var_45 = python_code_.uml_Association(isDerived=var_44)
    assert isinstance(var_45, python_code_.uml_Association)


def test_25():
    python_code_.uml_ValueSpecification()


def test_26():
    var_21 = 'HE\x0c7"(<H^L'
    python_code_.uml_Property(name=var_21, uml_Property45=(), uml_Property51=True)
    var_23 = python_code_.uml_Association(isDerived=var_21)
    assert isinstance(var_23, python_code_.uml_Association)


@pytest.mark.xfail(strict=True)
def test_27():
    var_1 = python_code_.BehavioralFeature()
    var_4 = python_code_.uml_Type()
    var_5 = python_code_.Feature()
    var_6 = python_code_.Abstraction()
    var_7 = set()
    var_8 = "_uml_Comment__uml_Comment8,_uml_Class__Class,uml_Package"
    var_9 = python_code_.uml_Class
    var_10 = python_code_.uml_Classifier(
        isAbstract=var_8,
        Classifier69=var_9,
        uml_Classifier67=var_1,
        featuringClassifier=var_7,
        uml_Classifier55=var_7,
        uml_Classifier60=var_5,
    )
    assert isinstance(var_10, python_code_.uml_Classifier)
    python_code_.uml_Classifier(
        isAbstract=var_5,
        uml_Classifier63=var_7,
        Classifier=-1596,
        uml_Classifier98=var_6,
        featuringClassifier=var_4,
        uml_Classifier57=var_10,
    )


def test_28():
    var_9 = python_code_.uml_Model(name={'pJc"i])5:0R~Ux+iE ': 2183})
    assert isinstance(var_9, python_code_.uml_Model)


def test_29():
    var_0 = "_uml_Classifier__uml_Classifier60_uml_Property__uml_Property93uml_Type83"
    var_1 = python_code_.uml_ElementImport(
        visibility=var_0, alias=[], ElementImport="p:K4h \x0b\nRN6I"
    )
    assert isinstance(var_1, python_code_.uml_ElementImport)


def test_30():
    var_8 = "X@!"
    var_9 = python_code_.uml_ElementImport(visibility=var_8, alias=var_8)
    assert isinstance(var_9, python_code_.uml_ElementImport)


def test_31():
    var_12 = python_code_.uml_Association(
        isDerived=complex(2991.8, -407.8674), uml_Association44=set()
    )
    assert isinstance(var_12, python_code_.uml_Association)


def test_32():
    var_14 = "ownedOperation _uml_BehavioralFeature__uml_BehavioralFeature"
    var_15 = "class_"
    var_16 = python_code_.uml_ElementImport(visibility=var_14, alias=var_15)
    assert isinstance(var_16, python_code_.uml_ElementImport)
    var_20 = python_code_.uml_PackageImport(visibility=var_14, PackageImport=None)
    assert isinstance(var_20, python_code_.uml_PackageImport)
    var_22 = python_code_.uml_Comment(body=var_14, uml_Comment=(444,))
    assert isinstance(var_22, python_code_.uml_Comment)


def test_33():
    var_0 = python_code_.Feature()
    var_1 = "uml_NamedElement54,uml_Parameter80,_uml_Classifier__uml_Classifier98"
    var_2 = "5z[d\rFRtqFtmNtHPg@p"
    var_3 = python_code_.uml_Namespace()
    var_4 = python_code_.uml_NamedElement(
        name=var_1,
        visibility=var_1,
        qualifiedName=var_2,
        ownedMember=var_0,
        NamedElement31=var_3,
    )
    assert isinstance(var_4, python_code_.uml_NamedElement)
    var_7 = python_code_.uml_Dependency()
    var_8 = {var_4}
    var_9 = python_code_.uml_Classifier(
        isAbstract=var_2,
        uml_Classifier=var_8,
        uml_Classifier57=var_7,
        uml_Classifier58=var_8,
    )
    assert isinstance(var_9, python_code_.uml_Classifier)
    var_10 = python_code_.uml_Association(
        isDerived=var_1, uml_Association47=var_8, uml_Association50=var_8
    )
    assert isinstance(var_10, python_code_.uml_Association)
    var_11 = python_code_.uml_Property(
        name=-205.38, uml_Property64=var_9, uml_Property=var_10
    )
    assert isinstance(var_11, python_code_.uml_Property)


@pytest.mark.xfail(strict=True)
def test_34():
    var_1 = python_code_.Feature()
    var_27 = '\x0be0!D5lBWoe"'
    var_29 = "j(a?z"
    var_30 = "^\n.:cDgq"
    var_32 = python_code_.uml_Association(
        isDerived=complex(2991.8, -407.8674), uml_Association44=set()
    )
    assert isinstance(var_32, python_code_.uml_Association)
    var_35 = python_code_.Type
    var_36 = "-\np{WIBE#L=ljv^"
    var_37 = "b8bU}/WR{(#D[qPm"
    var_38 = python_code_.uml_Parameter(
        default="uml_Class,_uml_Classifier__Classifier,uml_Association,class_",
        isException=var_27,
        isStream="_uml_NamedElement__NamedElement31",
        uml_Parameter=var_37,
        uml_Parameter80=var_29,
    )
    assert isinstance(var_38, python_code_.uml_Parameter)
    python_code_.uml_Operation(
        isQuery=var_35,
        isOrdered=var_30,
        isUnique=var_36,
        lower=var_1,
        upper=var_35,
        uml_Operation=var_38,
        Operation=1956.97,
    )


def test_35():
    var_7 = "_uml_Classifier__uml_Classifier86-ownedType-uml_Classifier63"
    python_code_.uml_Parameter(default=var_7, isException=var_7, isStream="h}/GD")


def test_36():
    var_22 = "j(a?z"
    var_24 = python_code_.uml_Association(
        isDerived=complex(2991.8, -407.8674), uml_Association44=set()
    )
    assert isinstance(var_24, python_code_.uml_Association)
    var_29 = "-\np{WIBE#L=ljv^"
    var_30 = "b8bU}/WR{(#D[qPm"
    var_31 = python_code_.uml_Parameter(
        default="uml_Class,_uml_Classifier__Classifier,uml_Association,class_",
        isException=var_29,
        isStream="_uml_NamedElement__NamedElement31",
        uml_Parameter=var_30,
        uml_Parameter80=var_22,
    )
    assert isinstance(var_31, python_code_.uml_Parameter)


def test_37():
    var_1 = python_code_.uml_ValueSpecification()
    var_11 = python_code_.uml_Feature(isStatic=(-583.47,), Feature=var_1)
    assert isinstance(var_11, python_code_.uml_Feature)
    var_13 = '@b"\tx'
    var_14 = "_uml_Package__uml_Package37"
    python_code_.uml_Property(name=var_14)
    var_24 = python_code_.uml_Class(
        isActive="Ml$W4M o[H",
        name=var_13,
        uml_Class92={
            -366,
            "_uml_Classifier__Classifier69.uml_Namespace.uml_Classifier58.uml_Substitution",
            var_13,
        },
        uml_Class88=set(),
        uml_Class95={var_1, var_13},
    )
    assert isinstance(var_24, python_code_.uml_Class)


@pytest.mark.xfail(strict=True)
def test_38():
    var_1 = python_code_.uml_ValueSpecification()
    python_code_.uml_Package(name=var_1, uml_Package=complex(-4217.7, -1133.2294676))


@pytest.mark.xfail(strict=True)
def test_39():
    var_17 = "_uml_Class__Class"
    var_18 = python_code_.uml_Association(isDerived=var_17)
    assert isinstance(var_18, python_code_.uml_Association)
    var_19 = "uml_Class:_uml_Classifier__uml_Classifier58"
    var_20 = "i\r[|v 0E]b7+QW2"
    var_21 = python_code_.Element
    var_22 = python_code_.uml_Generalization(isSubstitutable=var_20)
    assert isinstance(var_22, python_code_.uml_Generalization)
    var_25 = "_uml_Operation__uml_Operation78-uml_Classifier-_uml_NamedElement__ownedMember-_uml_Package__Package"
    var_26 = python_code_.uml_Property(name=var_25)
    var_27 = {var_26}
    var_28 = python_code_.uml_Classifier(
        isAbstract={},
        uml_Classifier63=var_27,
        featuringClassifier=var_27,
        uml_Classifier58=var_27,
    )
    assert isinstance(var_28, python_code_.uml_Classifier)
    var_31 = python_code_.uml_Classifier(
        isAbstract=var_21,
        uml_Classifier57=var_28,
        uml_Classifier55=var_19,
        uml_Classifier58=b"\x19\xdb\x00\xc4\xea\xd3y\xd1\x95\xfd\x8e\x83-,\x9e\xe8",
    )
    assert isinstance(var_31, python_code_.uml_Classifier)
    python_code_.uml_Classifier(
        isAbstract=var_20,
        Classifier69=var_21,
        uml_Classifier86={},
        uml_Classifier101=var_22,
        uml_Classifier57=var_28,
        uml_Classifier55=var_27,
        uml_Classifier60=-2845,
    )


def test_40():
    var_7 = [-1685]
    var_17 = python_code_.uml_Model(name={'pJc"i])5:0R~Ux+iE ': 2183})
    assert isinstance(var_17, python_code_.uml_Model)
    var_20 = python_code_.uml_BehavioralFeature(isAbstract=var_7)
    assert isinstance(var_20, python_code_.uml_BehavioralFeature)


def test_41():
    var_1 = python_code_.uml_ValueSpecification()
    var_29 = "_uml_Classifier__uml_Classifier63 uml_PackageableElement33 namespace _uml_Generalization__uml_Generalization97"
    var_30 = python_code_.uml_Generalization(
        isSubstitutable=var_29, uml_Generalization97=var_29
    )
    assert isinstance(var_30, python_code_.uml_Generalization)
    var_32 = 'I"8\x0bZP'
    var_33 = "ln-h\nnoVQf?eCRa"
    python_code_.uml_Property(name=var_33)
    var_48 = python_code_.uml_Class(
        isActive="Ml$W4M o[H",
        name=var_32,
        uml_Class92={
            -366,
            "_uml_Classifier__Classifier69.uml_Namespace.uml_Classifier58.uml_Substitution",
            var_32,
        },
        uml_Class88=set(),
        uml_Class95={var_1, var_32},
    )
    assert isinstance(var_48, python_code_.uml_Class)


def test_42():
    var_17 = python_code_.uml_Model(name={'pJc"i])5:0R~Ux+iE ': 2183})
    assert isinstance(var_17, python_code_.uml_Model)
    var_18 = "uml_Class"
    var_20 = python_code_.uml_BehavioralFeature(
        isAbstract=var_18, uml_BehavioralFeature={True, var_17}
    )
    assert isinstance(var_20, python_code_.uml_BehavioralFeature)


def test_43():
    var_32 = python_code_.uml_Association(
        isDerived=complex(2991.8, -407.8674), uml_Association44=set()
    )
    assert isinstance(var_32, python_code_.uml_Association)
    var_35 = python_code_.Type
    var_36 = "-\np{WIBE#L=ljv^"
    var_44 = python_code_.uml_Model(name={'pJc"i])5:0R~Ux+iE ': 2183})
    assert isinstance(var_44, python_code_.uml_Model)
    var_46 = python_code_.uml_Namespace()
    var_47 = python_code_.uml_ElementImport(
        visibility=var_35,
        alias={"uml_Type": True, "uml_PackageImport": False},
        uml_ElementImport=var_36,
        elementImport=var_46,
    )
    assert isinstance(var_47, python_code_.uml_ElementImport)


def test_44():
    var_8 = "X@c"
    var_9 = {"\tgtnZ.@$DFC7a[\te%:B"}
    var_21 = python_code_.uml_Feature(isStatic=var_8, feature=var_9)
    assert isinstance(var_21, python_code_.uml_Feature)


@pytest.mark.xfail(strict=True)
def test_45():
    var_0 = "uml_Property74"
    var_1 = python_code_.uml_Parameter(
        default=b"\xfb\xda\xf1F_\xeal\xd0\xb36\xc9R\xd2\xa2!\xad\xc0\xc3B",
        isException=[],
        isStream=var_0,
        uml_Parameter72=b"\x9fC",
    )
    assert isinstance(var_1, python_code_.uml_Parameter)
    var_2 = python_code_.uml_Namespace()
    var_3 = python_code_.uml_ElementImport(
        visibility=b"J8\xcc+6.\xd29e\xe0", alias=var_1, ElementImport=var_2
    )
    assert isinstance(var_3, python_code_.uml_ElementImport)
    python_code_.uml_Association(
        isDerived={},
        uml_Association44=895,
        uml_Association47=None,
        uml_Association50=(-42.87, ""),
    )


@pytest.mark.xfail(strict=True)
def test_46():
    var_1 = python_code_.Abstraction()
    var_2 = "uml_Property64-uml_Class90-_uml_Property__uml_Property64-_uml_Operation__Operation"
    var_3 = python_code_.uml_Property(name=var_2)
    var_4 = python_code_.uml_Feature(isStatic=var_1)
    assert isinstance(var_4, python_code_.uml_Feature)
    var_5 = python_code_.uml_Generalization(
        isSubstitutable=False, uml_Generalization100=var_2
    )
    assert isinstance(var_5, python_code_.uml_Generalization)
    var_6 = python_code_.uml_Parameter
    python_code_.uml_Class(isActive=1860.55, name=var_3, uml_Class85=var_6)


@pytest.mark.xfail(strict=True)
def test_47():
    var_14 = "class_,_uml_Classifier__uml_Classifier60"
    var_15 = python_code_.uml_BehavioralFeature
    python_code_.uml_Model(name=var_14, uml_Model=var_15)


@pytest.mark.xfail(strict=True)
def test_48():
    var_0 = "uml_Property-uml_Package-uml_Association-_uml_NamedElement__NamedElement"
    var_1 = lambda *args, **kwargs: "*\x0cv$zmT93BbZ"
    var_2 = set()
    var_3 = python_code_.uml_Substitution()
    var_4 = python_code_.uml_Classifier(
        isAbstract=var_1,
        uml_Classifier63=var_2,
        uml_Classifier86=set(),
        uml_Classifier67=var_3,
        uml_Classifier57=[],
        uml_Classifier60=var_1,
        uml_Classifier58=var_2,
    )
    assert isinstance(var_4, python_code_.uml_Classifier)
    var_5 = python_code_.uml_Feature(isStatic=var_0, Feature=var_4)
    assert isinstance(var_5, python_code_.uml_Feature)
    var_13 = python_code_.uml_Dependency()
    var_14 = python_code_.uml_NamedElement(
        name=var_0,
        visibility=var_3,
        qualifiedName=var_0,
        ownedMember=[],
        NamedElement=var_13,
    )
    assert isinstance(var_14, python_code_.uml_NamedElement)
    var_15 = "_uml_BehavioralFeature__uml_BehavioralFeature82 _uml_Property__uml_Property93 _uml_Property__uml_Property45 ownedOperation"
    python_code_.uml_NamedElement(name=var_0, visibility=var_0, qualifiedName=var_15)
    python_code_.uml_BehavioralFeature(isAbstract=False, uml_BehavioralFeature82=var_1)


def test_49():
    var_21 = python_code_.Type
    var_23 = "-\np{WIBE#L=lZjv^"
    var_25 = python_code_.uml_Model(name={'pJc"i])5:0R~Ux+iE ': 2183})
    assert isinstance(var_25, python_code_.uml_Model)
    var_26 = "Namespace39 uml_Element7"
    var_27 = python_code_.uml_Namespace()
    var_28 = python_code_.uml_ElementImport(
        visibility=var_21,
        alias={"uml_Type": True, "uml_PackageImport": False},
        uml_ElementImport=var_23,
        elementImport=var_27,
    )
    assert isinstance(var_28, python_code_.uml_ElementImport)
    var_29 = "private"
    var_30 = python_code_.uml_NamedElement(
        name=var_29, visibility=var_26, qualifiedName=var_23, NamedElement=False
    )
    assert isinstance(var_30, python_code_.uml_NamedElement)


@pytest.mark.xfail(strict=True)
def test_50():
    var_1 = python_code_.uml_ValueSpecification()
    var_11 = python_code_.uml_Feature(isStatic=(-583.47,), Feature=var_1)
    assert isinstance(var_11, python_code_.uml_Feature)
    var_12 = python_code_.uml_Substitution()
    var_13 = '@b"\tx'
    var_24 = python_code_.Realization()
    var_28 = python_code_.uml_Dependency()
    var_29 = python_code_.uml_NamedElement(
        name=var_13,
        visibility=var_12,
        qualifiedName=var_13,
        ownedMember=[],
        NamedElement=var_28,
    )
    assert isinstance(var_29, python_code_.uml_NamedElement)
    var_30 = "_uml_BehavioralFeature__uml_BehavioralFeature82 _uml_Property__uml_Property93 _uml_Property__uml_Property45 ownedOperation"
    var_31 = python_code_.uml_NamedElement(
        name=var_13, visibility=var_13, qualifiedName=var_30
    )
    var_37 = python_code_.Element()
    var_38 = python_code_.Classifier()
    var_40 = python_code_.uml_Property(
        name={"^:HHI9nwMs", "G$m\x0c5\rB iaT"},
        uml_Property93=var_31,
        uml_Property51=var_38,
    )
    var_41 = {var_40, var_40}
    python_code_.uml_Association(
        isDerived=var_37, uml_Association=var_24, uml_Association44=var_41
    )


@pytest.mark.xfail(strict=True)
def test_51():
    var_0 = ""
    var_1 = "Operation _uml_Classifier__Classifier"
    python_code_.uml_Parameter(default=var_0, isException=var_0, isStream=var_1)
    var_3 = python_code_.DirectedRelationship()
    var_4 = python_code_.Element()
    var_6 = python_code_.uml_Substitution()
    var_7 = python_code_.uml_DirectedRelationship()
    var_8 = python_code_.uml_Relationship()
    var_9 = "o)d0\r\x0clH"
    var_10 = python_code_.uml_Feature(isStatic=var_9, feature=var_9)
    assert isinstance(var_10, python_code_.uml_Feature)
    var_12 = python_code_.Element()
    var_14 = bool
    var_15 = python_code_.uml_BehavioralFeature(isAbstract=var_14)
    assert isinstance(var_15, python_code_.uml_BehavioralFeature)
    var_16 = python_code_.Feature()
    var_17 = "lT&`R_4"
    var_18 = "@Cd6P/]x|f(?<\nG"
    var_19 = python_code_.uml_Class(
        isActive=var_18, name=var_14, uml_Class88={"uml_Class85:uml_Property": 1738}
    )
    assert isinstance(var_19, python_code_.uml_Class)
    var_20 = python_code_.uml_Class(
        isActive=complex(-1800.394, -660.522896),
        name=var_17,
        uml_Class85=(),
        uml_Class90=var_19,
    )
    assert isinstance(var_20, python_code_.uml_Class)
    var_21 = python_code_.uml_Classifier(
        isAbstract={}, Classifier69=var_3, uml_Classifier86=var_19
    )
    assert isinstance(var_21, python_code_.uml_Classifier)
    var_22 = python_code_.TypedElement()
    var_23 = python_code_.uml_Package(name=[True, -1282.13])
    assert isinstance(var_23, python_code_.uml_Package)
    var_24 = python_code_.uml_Namespace()
    var_25 = python_code_.uml_NamedElement(
        name={
            "uml_Property45 uml_Class92 namespace _uml_Class__uml_Class92",
            1994,
            "Feature",
        },
        visibility=var_12,
        qualifiedName=[],
        NamedElement=var_7,
        uml_NamedElement=var_16,
        NamedElement31=var_24,
        uml_NamedElement26=var_24,
        uml_NamedElement54=319,
    )
    assert isinstance(var_25, python_code_.uml_NamedElement)
    var_26 = "'\\V\x0clP"
    python_code_.uml_Property(
        name=var_26, uml_Property64=var_14, uml_Property45=(), uml_Property51=var_14
    )
    var_28 = "-h1h!!-.<j"
    var_29 = python_code_.uml_Operation(
        isQuery=var_19,
        isOrdered=var_3,
        isUnique=var_28,
        lower=var_28,
        upper=var_4,
        uml_Operation={"uml_Parameter:_uml_NamedElement__ownedMember": -5338.24},
    )
    assert isinstance(var_29, python_code_.uml_Operation)
    python_code_.uml_Parameter(
        default=var_6,
        isException=var_9,
        isStream=var_22,
        uml_Parameter=var_29,
        uml_Parameter72={
            ",&|-JD,=": True,
            "uml_Association50": -128.23,
            "'F&aq\x0bAb2~uHvmw": 61.24,
        },
        uml_Parameter80=var_8,
    )
