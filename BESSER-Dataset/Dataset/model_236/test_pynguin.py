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
    EClassifier,
    EDataType,
    EModelElement,
    ENamedElement,
    EStructuralFeature,
    ETypedElement,
    abstractmethod,
    date,
    datetime,
    ecore_EAnnotation,
    ecore_EAttribute,
    ecore_EClass,
    ecore_EClassifier,
    ecore_EDataType,
    ecore_EEnum,
    ecore_EEnumLiteral,
    ecore_EFactory,
    ecore_EGenericType,
    ecore_EModelElement,
    ecore_ENamedElement,
    ecore_EObject,
    ecore_EOperation,
    ecore_EPackage,
    ecore_EParameter,
    ecore_EReference,
    ecore_EStringToStringMapEntry,
    ecore_EStructuralFeature,
    ecore_ETypeParameter,
    ecore_ETypedElement,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.ecore_EObject()
    python_code_.ecore_EEnum(eEnum=var_0, EEnum=var_0)


def test_1():
    python_code_.ecore_EFactory()
    var_7 = python_code_.ecore_EEnum()
    assert isinstance(var_7, python_code_.ecore_EEnum)
    var_26 = python_code_.ecore_EOperation(ecore_EOperation=False)
    assert isinstance(var_26, python_code_.ecore_EOperation)
    var_26.getOperationID()


def test_2():
    var_10 = "_ecore_EClass__ecore_EClass38"
    var_11 = "ecore_EEnum"
    var_12 = python_code_.ecore_EPackage(nsURI=[True], nsPrefix=None)
    assert isinstance(var_12, python_code_.ecore_EPackage)
    var_13 = False
    var_14 = float
    var_15 = lambda *args, **kwargs: True
    var_16 = python_code_.ecore_ETypedElement(
        ordered=var_13,
        unique=var_10,
        lowerBound=var_14,
        upperBound=var_15,
        many=var_11,
        required=-106,
    )
    assert isinstance(var_16, python_code_.ecore_ETypedElement)
    var_6 = python_code_.ecore_EOperation(ecore_EOperation=False)
    assert isinstance(var_6, python_code_.ecore_EOperation)


def test_3():
    var_5 = False
    var_10 = "_ecore_EClass__ecore_EClass38"
    var_11 = "ecore_EEnum"
    var_12 = python_code_.ecore_EPackage(nsURI=[True], nsPrefix=None)
    assert isinstance(var_12, python_code_.ecore_EPackage)
    var_13 = False
    var_14 = float
    var_15 = lambda *args, **kwargs: True
    var_16 = python_code_.ecore_ETypedElement(
        ordered=var_13,
        unique=var_10,
        lowerBound=var_14,
        upperBound=var_15,
        many=var_11,
        required=-106,
    )
    assert isinstance(
        python_code_.ecore_ETypedElement.ecore_ETypedElement,
        python_code_.ecore_EClassifier,
    )
    python_code_.ecore_EClassifier(
        instanceClass=var_5,
        defaultValue=var_10,
        instanceTypeName=var_11,
        instanceClassName=var_11,
        EClassifier=var_12,
        ecore_EClassifier83=var_16,
    )
    var_6 = python_code_.ecore_EOperation(ecore_EOperation=False)
    var_6.getOperationID()


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.ecore_EObject()
    var_76 = "\x0chR:o3+%:pm|bMqL2r]"
    var_77 = set
    var_78 = python_code_.ecore_EPackage(
        nsURI=var_76, nsPrefix=var_77, EPackage47=False
    )
    assert isinstance(var_78, python_code_.ecore_EPackage)
    var_79 = False
    var_80 = python_code_.ecore_ETypedElement(
        ordered=var_79,
        unique=var_77,
        lowerBound=var_78,
        upperBound=var_79,
        many=var_79,
        required=var_0,
        ecore_ETypedElement=753,
    )
    assert isinstance(
        python_code_.ecore_ETypedElement.ecore_ETypedElement,
        python_code_.ecore_EClassifier,
    )
    var_81 = ""
    var_82 = "_ecore_EPackage__ePackage62ecore_EReference18eOperations_ecore_EEnumLiteral__EEnumLiteral"
    var_83 = "-\r8T\x0bFHCvVqO+m0tT@d"
    var_84 = python_code_.ecore_EClassifier(
        instanceClass=var_77,
        defaultValue=var_81,
        instanceTypeName=var_82,
        instanceClassName=var_83,
        ecore_EClassifier56=var_76,
        ecore_EClassifier95=var_77,
    )
    python_code_.ecore_EGenericType(
        ecore_EGenericType41=var_77,
        ecore_EGenericType59=b"\xff$\xe3\xcf?\x90@\xa0&_\xe8c\x0f\xf6\xf3:",
        ecore_EGenericType86=var_80,
        ecore_EGenericType92={"xH5e,": 4300, "xO,U~pbxW}K8QA": "ecore_ETypedElement"},
        ecore_EGenericType94=var_84,
        ecore_EGenericType100=set(),
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = python_code_.ecore_ETypeParameter()
    var_1 = python_code_.ecore_ETypedElement
    var_2 = 'TFkjh9\x0b"SR'
    var_3 = python_code_.ecore_EClassifier(
        instanceClass=var_1,
        defaultValue=var_2,
        instanceTypeName=var_1,
        instanceClassName=var_2,
        eClassifiers=var_1,
        ecore_EClassifier83=var_1,
        ecore_EClassifier104=var_2,
    )
    assert isinstance(var_3, python_code_.ecore_EClassifier)
    python_code_.ecore_EGenericType(
        ecore_EGenericType41=True,
        ecore_EGenericType107=var_0,
        ecore_EGenericType96=var_0,
        ecore_EGenericType103=var_3,
    )


def test_6():
    var_12 = python_code_.ecore_EPackage(nsURI=[True], nsPrefix=None)
    assert isinstance(var_12, python_code_.ecore_EPackage)


def test_7():
    var_0 = "EClassifier"
    var_1 = python_code_.ecore_EPackage(
        nsURI="e?if&$*GJ=!\r|D!",
        nsPrefix=var_0,
        EPackage=var_0,
        EPackage47=None,
        ePackage=var_0,
    )
    assert isinstance(var_1, python_code_.ecore_EPackage)
    var_1.getEClassifier(ecore_name=complex(-193.3129231, 2062.324602))
    var_3 = python_code_.ecore_EFactory(eFactoryInstance=None, EFactory=None)
    assert isinstance(var_3, python_code_.ecore_EFactory)
    var_3.convertToString(
        ecore_instanceValue=bytes, ecore_eDataType=python_code_.ecore_EReference
    )


@pytest.mark.xfail(strict=True)
def test_8():
    var_0 = python_code_.ecore_ETypeParameter()
    python_code_.ecore_EGenericType(
        ecore_EGenericType90=set(), ecore_EGenericType94=None
    )
    var_35 = python_code_.ecore_EStructuralFeature(
        changeable=[False, 600.4],
        volatile=var_0,
        transient="TZ{6IC]",
        defaultValueLiteral=False,
        defaultValue=1560.01,
        unsettable=b"\r\x07upA\xe1Y\xec",
        derived="_ecore_EClass__ecore_EClass28",
    )
    assert isinstance(var_35, python_code_.ecore_EStructuralFeature)
    var_34 = python_code_.ecore_EDataType(
        serializable=(
            "eContainingClass36,ecore_EGenericType87,ecore_EPackage,_ecore_EAnnotation__eAnnotations",
        )
    )
    assert isinstance(var_34, python_code_.ecore_EDataType)
    var_36 = set
    python_code_.ecore_EAnnotation(source=var_36, ecore_EAnnotation6=var_34)


def test_9():
    var_0 = "eModelElement"
    var_3 = True
    var_4 = python_code_.ecore_EStructuralFeature(
        changeable=True,
        volatile=var_3,
        transient=True,
        defaultValueLiteral=var_0,
        defaultValue=var_0,
        unsettable=var_3,
        derived=True,
    )
    assert isinstance(var_4, python_code_.ecore_EStructuralFeature)


def test_10():
    var_1 = False
    var_7 = python_code_.ENamedElement()
    var_8 = False
    var_19 = python_code_.ecore_EParameter
    var_20 = "_ecore_EPackage__EPackage.ecore_ETypeParameter106._ecore_EGenericType__ecore_EGenericType90"
    var_21 = "$l\rwN"
    var_22 = python_code_.ecore_EStructuralFeature(
        changeable={"AkO{mZ{76": "/piq[Q#e"},
        volatile=var_8,
        transient=var_19,
        defaultValueLiteral=var_20,
        defaultValue=var_21,
        unsettable=(),
        derived=complex(-2121.16, -434.0),
        EStructuralFeature=var_7,
    )
    assert isinstance(var_22, python_code_.ecore_EStructuralFeature)
    var_23 = "'.Y"
    var_24 = python_code_.ecore_EClassifier(
        instanceClass=var_20,
        defaultValue=var_21,
        instanceTypeName=var_23,
        instanceClassName=var_23,
        EClassifier=var_1,
        ecore_EClassifier95=var_19,
    )
    assert isinstance(var_24, python_code_.ecore_EClassifier)
    var_24.isInstance(ecore_object=set())
    var_22.getFeatureID()


def test_11():
    var_0 = False
    var_1 = python_code_.ecore_EClass(
        abstract=True,
        interface=False,
        ecore_EClass20=set(),
        ecore_EClass23=set(),
        ecore_EClass28={True},
        ecore_EClass38=set(),
        EClass=None,
        EClass81=None,
    )
    assert isinstance(var_1, python_code_.ecore_EClass)
    var_1.getOverride(ecore_operation=None)
    var_5 = True
    var_6 = "_ecore_EPackage__ePackage62_ecore_ETypedElement__ecore_ETypedElement85"
    var_7 = False
    var_8 = False
    var_9 = python_code_.ecore_EStructuralFeature(
        changeable=var_0,
        volatile=complex(1731.79, -2746.7),
        transient=var_5,
        defaultValueLiteral=var_6,
        defaultValue=var_1,
        unsettable=var_7,
        derived=var_8,
        eStructuralFeatures={"?*/a\\-~P0$Vu": 671, ">v%QgCx%hj^T\x0b": -602.29},
    )
    assert isinstance(var_9, python_code_.ecore_EStructuralFeature)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.ecore_EFactory()
    var_1 = var_0.create(ecore_eClass=var_0)
    var_3 = lambda *args, **kwargs: [3]
    python_code_.ecore_EOperation(
        ecore_EOperation=var_1,
        eOperations=var_3,
        ecore_EOperation51=var_3,
        EOperation70=18.88,
    )


def test_13():
    var_15 = python_code_.ecore_EOperation(ecore_EOperation=False)
    assert isinstance(var_15, python_code_.ecore_EOperation)
    var_15.getOperationID()


def test_14():
    var_0 = True
    var_1 = python_code_.ecore_EDataType(serializable=var_0)
    assert isinstance(var_1, python_code_.ecore_EDataType)
    var_2 = int
    var_3 = python_code_.ecore_EAnnotation(source=var_2)
    assert isinstance(var_3, python_code_.ecore_EAnnotation)
    var_4 = python_code_.ecore_EObject(ecore_EObject7=var_3)
    var_4.eClass()
    var_6 = python_code_.ecore_EOperation(
        EOperation={}, ecore_EOperation=None, EOperation70=var_2
    )
    assert isinstance(var_6, python_code_.ecore_EOperation)
    var_6.isOverrideOf(ecore_someOperation=(-2774.32, 1003.37, "~bC"))


def test_15():
    var_0 = "-gQQ5?}\\>hV"
    var_5 = lambda *args, **kwargs: True
    var_7 = python_code_.ecore_EOperation(
        eOperations=None, eOperation={var_5, var_0, False}
    )
    assert isinstance(var_7, python_code_.ecore_EOperation)


def test_16():
    var_0 = False
    var_1 = python_code_.ecore_EClass(
        abstract=var_0,
        interface=var_0,
        eContainingClass={var_0, -568.16},
        ecore_EClass12=set(),
        ecore_EClass15={True, var_0, True},
        ecore_EClass17={-516},
        ecore_EClass23=set(),
        ecore_EClass29=set(),
        ecore_EClass33=var_0,
        eContainingClass36={-3340.67, "^oOPY#R-JfI6B", var_0},
        ecore_EClass38={"ecore_EClass40", ">1bWOncU`V |nx&", var_0},
        ecore_EClass8=set(),
        ecore_EClass76=None,
        EClass81=None,
    )
    assert isinstance(var_1, python_code_.ecore_EClass)


def test_17():
    var_0 = False
    var_1 = python_code_.ecore_EClass(
        abstract=True,
        interface=False,
        ecore_EClass20=set(),
        ecore_EClass23=set(),
        ecore_EClass28={True},
        ecore_EClass38=set(),
        EClass=None,
        EClass81=None,
    )
    assert isinstance(var_1, python_code_.ecore_EClass)
    var_2 = var_1.getOverride(ecore_operation=None)
    var_3 = False
    var_4 = python_code_.ecore_EReference(
        containment=var_0,
        container=var_1,
        resolveProxies=var_3,
        ecore_EReference78=var_2,
    )
    assert isinstance(var_4, python_code_.ecore_EReference)


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = True
    python_code_.ecore_EClass(
        abstract=var_0, interface=var_0, ecore_EClass29=var_0, ecore_EClass8=-1039
    )


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = True
    var_1 = python_code_.ecore_EOperation(EOperation70=var_0, ecore_EOperation55=None)
    assert isinstance(var_1, python_code_.ecore_EOperation)
    var_2 = var_1.getOperationID()
    var_3 = {-5.36, var_0, 753}
    var_4 = list
    python_code_.ecore_EClass(
        abstract=var_2,
        interface=var_0,
        ecore_EClass17=var_3,
        ecore_EClass26=var_4,
        ecore_EClass33=None,
        ecore_EClass40=b"y\xa3Y\xf9\xa0i\x83$`",
        ecore_EClass8=b"\xccr\xb6K0=\xca\x02\x85\x02'\xedB\xafx\xd9",
        ecore_EClass76=None,
    )


def test_20():
    python_code_.ecore_EObject(ecore_EObject=None, ecore_EObject7=None)


def test_21():
    var_0 = "eModel8lement"
    var_23 = python_code_.ecore_EAnnotation(
        source=complex(3272.0, 1756.0826),
        ecore_EAnnotation6=var_0,
        EAnnotation={
            "rS/I": -2818.13,
            "+H^": 67.12,
            "_ecore_EEnumLiteral__EEnumLiteral": 1161.6,
        },
    )
    assert isinstance(var_23, python_code_.ecore_EAnnotation)
    var_24 = python_code_.ecore_EObject(ecore_EObject=var_23, ecore_EObject7=var_0)
    var_24.eContainmentFeature()


def test_22():
    python_code_.ecore_EObject(ecore_EObject7=None)
    python_code_.ecore_EFactory()


def test_23():
    var_0 = "eModel8%lement"
    var_23 = python_code_.ecore_EAnnotation(
        source="_ecore_EClass__ecore_EClass_ecore_ETypedElement__ecore_ETypedElement_ecore_EAnnotation__ecore_EAnnotation",
        eAnnotations=None,
        EAnnotation=var_0,
    )
    assert isinstance(var_23, python_code_.ecore_EAnnotation)
    python_code_.ecore_EObject(ecore_EObject=var_23, ecore_EObject7=var_0)
    var_26 = python_code_.ecore_EPackage(nsURI=[True], nsPrefix=None)
    assert isinstance(var_26, python_code_.ecore_EPackage)


def test_24():
    var_0 = lambda *args, **kwargs: False
    var_1 = "qe%`"
    var_2 = False
    var_3 = "\niZ,w`>z|ZS8"
    var_4 = "Q+KW"
    var_5 = python_code_.ecore_EStructuralFeature(
        changeable=var_0,
        volatile=var_2,
        transient=[],
        defaultValueLiteral=var_3,
        defaultValue=var_4,
        unsettable="9D+!Z'lN^2O$U9L(W",
        derived=var_1,
    )
    assert isinstance(var_5, python_code_.ecore_EStructuralFeature)
    var_6 = var_5.getContainerClass()
    var_7 = python_code_.ecore_EAnnotation(source=var_1, ecore_EAnnotation6=var_6)
    assert isinstance(var_7, python_code_.ecore_EAnnotation)
    var_8 = python_code_.ecore_EObject(ecore_EObject=var_7)
    var_9 = var_8.eIsProxy()
    var_10 = False
    var_11 = True
    var_12 = python_code_.ecore_ETypedElement(
        ordered=False,
        unique=var_10,
        lowerBound=var_5,
        upperBound=var_10,
        many=var_3,
        required=var_11,
    )
    assert isinstance(var_12, python_code_.ecore_ETypedElement)
    python_code_.ecore_EClassifier(
        instanceClass=var_0,
        defaultValue=var_0,
        instanceTypeName=var_1,
        instanceClassName=set(),
        ecore_EClassifier=var_9,
        EClassifier=var_1,
        ecore_EClassifier83=var_12,
    )
    assert isinstance(var_12.ecore_ETypedElement, python_code_.ecore_EClassifier)


def test_25():
    var_0 = int
    var_1 = python_code_.ecore_EObject(ecore_EObject=var_0)
    var_1.eResource()


def test_26():
    var_0 = False
    var_2 = python_code_.ecore_EObject()
    var_3 = var_2.eCrossReferences()
    var_5 = True
    var_10 = python_code_.ecore_EReference(
        containment=var_5,
        container=var_2,
        resolveProxies=var_0,
        ecore_EReference24=var_3,
    )
    assert isinstance(var_10, python_code_.ecore_EReference)
    var_2.eIsSet(ecore_feature=var_2)
    var_2.eContents()
    var_29 = python_code_.ecore_EDataType(serializable=var_5)
    assert isinstance(var_29, python_code_.ecore_EDataType)


def test_27():
    var_0 = python_code_.ecore_EFactory()
    var_0.create(ecore_eClass=var_0)
    var_6 = "_ecore_EAttribute__ecore_EAttribute"
    var_7 = python_code_.ecore_EEnum()
    assert isinstance(var_7, python_code_.ecore_EEnum)
    var_8 = python_code_.ecore_EEnumLiteral(
        value=-3682, instance="ecore_EReference78", literal=var_6
    )
    assert isinstance(var_8, python_code_.ecore_EEnumLiteral)


def test_28():
    var_15 = python_code_.ecore_EOperation(ecore_EOperation=False)
    assert isinstance(var_15, python_code_.ecore_EOperation)
    var_15.getOperationID()
    var_18 = str
    var_19 = python_code_.ecore_EObject(ecore_EObject=var_18, ecore_EObject7="S;(")
    var_19.eContainer()


@pytest.mark.xfail(strict=True)
def test_29():
    var_0 = "-gQ5?}\\>hV"
    var_1 = python_code_.ecore_EFactory()
    python_code_.ecore_EPackage(
        nsURI=None, nsPrefix=var_0, EPackage47=var_1, ePackage=var_1
    )


def test_30():
    var_7 = python_code_.ENamedElement()
    var_46 = python_code_.ecore_EPackage(
        nsURI=":U",
        nsPrefix=",k2j*f",
        EPackage=var_7,
        EPackage65=var_7,
        EPackage68=var_7,
    )
    assert isinstance(var_46, python_code_.ecore_EPackage)
    var_47 = python_code_.ecore_EFactory(eFactoryInstance=None, EFactory=None)
    assert isinstance(var_47, python_code_.ecore_EFactory)
    python_code_.ecore_EObject()
    var_92 = python_code_.ecore_EEnum()
    assert isinstance(var_92, python_code_.ecore_EEnum)
    var_93 = python_code_.ecore_EOperation(ecore_EOperation=False)
    assert isinstance(var_93, python_code_.ecore_EOperation)
    var_93.getOperationID()


def test_31():
    var_0 = "eModelElement"
    var_3 = True
    var_4 = python_code_.ecore_EStructuralFeature(
        changeable=True,
        volatile=var_3,
        transient=True,
        defaultValueLiteral=var_0,
        defaultValue=var_0,
        unsettable=var_3,
        derived=True,
    )
    assert isinstance(var_4, python_code_.ecore_EStructuralFeature)
    var_23 = python_code_.ecore_ENamedElement(name=var_4)
    assert isinstance(var_23, python_code_.ecore_ENamedElement)


@pytest.mark.xfail(strict=True)
def test_32():
    var_2 = python_code_.ecore_EObject()
    var_3 = var_2.eCrossReferences()
    python_code_.ecore_EModelElement()
    var_42 = python_code_.ecore_EFactory()
    var_43 = (
        lambda *args, **kwargs: "_ecore_EGenericType__ecore_EGenericType59,ecore_EAttribute13,_ecore_EOperation__eOperation,_ecore_EGenericType__ecore_EGenericType"
    )
    var_42.convertToString(ecore_instanceValue=None, ecore_eDataType=var_43)
    var_46 = "_ecore_EClass__ecore_EClass76._ecore_EAnnotation__eAnnotations"
    var_48 = "_ecore_EPackage__EPackage.ecore_ETypeParameter106._ecore_EGenericType__ecore_EGenericType90"
    var_56 = python_code_.ecore_EPackage(
        nsURI=var_48, nsPrefix=var_46, EPackage=var_3, eSuperPackage=set()
    )
    assert isinstance(var_56, python_code_.ecore_EPackage)
    python_code_.ecore_EPackage(
        nsURI=var_48,
        nsPrefix=b"h\n\xfa\x82\xb4\xa2j:0/\x91\xce\r\xa3\xd1",
        eSubpackages=var_56,
    )


def test_33():
    var_8 = python_code_.ecore_EModelElement()
    var_8.getEAnnotation(ecore_source=None)


@pytest.mark.xfail(strict=True)
def test_34():
    var_0 = "eModelElement"
    var_1 = len
    var_3 = True
    var_24 = False
    var_25 = python_code_.ecore_EFactory()
    var_26 = (
        lambda *args, **kwargs: "_ecore_EGenericType__ecore_EGenericType59,ecore_EAttribute13,_ecore_EOperation__eOperation,_ecore_EGenericType__ecore_EGenericType"
    )
    var_25.convertToString(ecore_instanceValue=None, ecore_eDataType=var_26)
    var_30 = True
    var_31 = "_ecore_EPackage__EPackage.ecore_ETypeParameter106._ecore_EGenericType__ecore_EGenericType90"
    var_34 = False
    var_35 = python_code_.ecore_EDataType(serializable=var_34)
    assert isinstance(var_35, python_code_.ecore_EDataType)
    var_41 = python_code_.ecore_EObject(ecore_EObject=[])
    var_42 = var_41.eContainingFeature()
    var_43 = True
    var_44 = True
    var_45 = python_code_.ecore_EStructuralFeature(
        changeable=var_24,
        volatile=var_43,
        transient=var_44,
        defaultValueLiteral=var_1,
        defaultValue=var_0,
        unsettable=var_30,
        derived=var_44,
        eStructuralFeatures=[],
    )
    assert isinstance(var_45, python_code_.ecore_EStructuralFeature)
    var_46 = var_45.getContainerClass()
    var_47 = var_41.eContents()
    python_code_.ecore_EClass(
        abstract=var_3,
        interface=var_26,
        eContainingClass=(
            "_ecore_EStringToStringMapEntry__ecore_EStringToStringMapEntry_ecore_EGenericType__ecore_EGenericType94_ecore_EObject__ecore_EObject7",
            False,
            4446,
        ),
        ecore_EClass15=var_42,
        ecore_EClass17=var_31,
        ecore_EClass20=var_46,
        ecore_EClass28=var_47,
        ecore_EClass29=var_26,
        ecore_EClass=var_1,
    )


def test_35():
    var_0 = python_code_.ecore_EObject()
    var_0.eInvoke(ecore_arguments=var_0, ecore_operation=var_0)
    var_0.eContainmentFeature()
    var_52 = True
    var_0.eIsSet(ecore_feature=var_0)
    var_0.eContents()
    var_55 = python_code_.ecore_EDataType(serializable=var_52)
    assert isinstance(var_55, python_code_.ecore_EDataType)


@pytest.mark.xfail(strict=True)
def test_36():
    var_2 = python_code_.ecore_EObject()
    var_2.eCrossReferences()
    var_37 = python_code_.ecore_EModelElement()
    var_37.getEAnnotation(ecore_source=lambda *args, **kwargs: -2708)
    var_42 = python_code_.ecore_EFactory()
    var_43 = (
        lambda *args, **kwargs: "_ecore_EGenericType__ecore_EGenericType59,ecore_EAttribute13,_ecore_EOperation__eOperation,_ecore_EGenericType__ecore_EGenericType"
    )
    var_42.convertToString(ecore_instanceValue=None, ecore_eDataType=var_43)
    var_48 = "_ecore_EPackage__EPackage.ecore_ETypeParameter106._ecore_EGenericType__ecore_EGenericType90"
    var_52 = True
    var_53 = python_code_.ecore_EDataType(serializable=var_52)
    assert isinstance(var_53, python_code_.ecore_EDataType)
    var_56 = python_code_.ecore_EPackage(
        nsURI=complex(3311.278441, -2898.541218), nsPrefix=var_48, eSubpackages=[]
    )
    assert isinstance(var_56, python_code_.ecore_EPackage)
    python_code_.ecore_EPackage(
        nsURI=var_48,
        nsPrefix=b"h\n\xfa\x82\xb4\xa2j:0/\x91\xce\r\xa3\xd1",
        eSubpackages=var_56,
    )


@pytest.mark.xfail(strict=True)
def test_37():
    var_1 = python_code_.ecore_ETypedElement
    var_2 = 'TFkjh9\x0b"SR'
    var_3 = python_code_.ecore_EClassifier(
        instanceClass=var_1,
        defaultValue=var_2,
        instanceTypeName=var_1,
        instanceClassName=var_2,
        eClassifiers=var_1,
        ecore_EClassifier83=var_1,
        ecore_EClassifier104=var_2,
    )
    assert isinstance(var_3, python_code_.ecore_EClassifier)
    python_code_.ecore_EGenericType(
        ecore_EGenericType41=None,
        ecore_EGenericType89=var_3,
        ecore_EGenericType100=None,
    )
    python_code_.ecore_EModelElement(eModelElement=var_1)


@pytest.mark.xfail(strict=True)
def test_38():
    var_1 = "qe%`"
    var_2 = False
    var_15 = python_code_.ecore_EOperation(ecore_EOperation=False)
    assert isinstance(var_15, python_code_.ecore_EOperation)
    var_16 = var_15.getOperationID()
    var_18 = str
    var_26 = True
    var_27 = True
    var_28 = "ecore_EPackage _ecore_EClass__EClass81 EEnumLiteral"
    var_29 = python_code_.ecore_EAnnotation(
        source=var_28, ecore_EAnnotation6={2716.78}, EAnnotation=var_18
    )
    assert isinstance(var_29, python_code_.ecore_EAnnotation)
    var_30 = python_code_.ecore_EObject(ecore_EObject7=var_29)
    var_30.eIsSet(ecore_feature=var_1)
    var_32 = var_30.eUnset(ecore_feature=var_16)
    var_34 = True
    var_35 = var_30.eContainmentFeature()
    var_30.eContents()
    var_39 = var_30.eInvoke(ecore_arguments=var_2, ecore_operation=var_16)
    var_40 = python_code_.ecore_EEnum(eEnum=var_39)
    assert isinstance(var_40, python_code_.ecore_EEnum)
    var_41 = var_40.getEEnumLiteral(ecore_value=var_18)
    var_42 = {var_2, var_35}
    python_code_.ecore_EClass(
        abstract=var_27,
        interface=var_34,
        eContainingClass=var_41,
        ecore_EClass12=var_42,
        ecore_EClass26=var_26,
        eContainingClass36=var_42,
        ecore_EClass38=-1368,
        ecore_EClass=var_32,
    )


def test_39():
    var_7 = python_code_.ENamedElement()
    var_19 = python_code_.ecore_EParameter
    var_46 = python_code_.ecore_EPackage(
        nsURI=-2311.34, nsPrefix=var_7, EPackage=var_19
    )
    assert isinstance(var_46, python_code_.ecore_EPackage)
    var_47 = python_code_.ecore_EFactory(eFactoryInstance=None, EFactory=None)
    assert isinstance(var_47, python_code_.ecore_EFactory)
    var_51 = ",ei"
    var_52 = python_code_.ecore_EAnnotation(source=var_51)
    assert isinstance(var_52, python_code_.ecore_EAnnotation)
    var_53 = python_code_.ecore_EObject(ecore_EObject=var_52)
    var_53.eUnset(ecore_feature=var_19)
    var_78 = python_code_.ecore_EAnnotation(source=var_19)
    var_79 = python_code_.ecore_EObject(ecore_EObject7=var_78)
    var_79.eClass()
    var_81 = python_code_.ecore_EOperation(
        EOperation={}, ecore_EOperation=None, EOperation70=var_19
    )
    assert isinstance(var_81, python_code_.ecore_EOperation)
    var_81.isOverrideOf(ecore_someOperation=(-2774.32, 1003.37, "~bC"))


@pytest.mark.xfail(strict=True)
def test_40():
    var_7 = python_code_.ENamedElement()
    var_19 = python_code_.ecore_EParameter
    var_46 = python_code_.ecore_EPackage(
        nsURI=":U",
        nsPrefix=",k2j*f",
        EPackage=var_7,
        EPackage65=var_7,
        EPackage68=var_7,
    )
    assert isinstance(var_46, python_code_.ecore_EPackage)
    var_47 = python_code_.ecore_EFactory(eFactoryInstance=None, EFactory=None)
    assert isinstance(var_47, python_code_.ecore_EFactory)
    var_51 = ",ei"
    var_52 = python_code_.ecore_EAnnotation(source=var_51)
    assert isinstance(var_52, python_code_.ecore_EAnnotation)
    var_53 = python_code_.ecore_EObject(ecore_EObject=var_52)
    var_53.eUnset(ecore_feature=var_19)
    var_55 = True
    var_79 = python_code_.ecore_EObject()
    var_83 = python_code_.ecore_EFactory()
    var_84 = python_code_.ecore_EDataType(serializable=None)
    assert isinstance(var_84, python_code_.ecore_EDataType)
    var_85 = python_code_.ecore_EEnum(EEnum=var_7)
    assert isinstance(var_85, python_code_.ecore_EEnum)
    var_86 = python_code_.ecore_EEnumLiteral(
        value=var_19, instance=var_19, literal=None, EEnumLiteral=var_85
    )
    assert isinstance(var_86, python_code_.ecore_EEnumLiteral)
    var_87 = True
    var_88 = python_code_.ecore_EStructuralFeature(
        changeable=var_19,
        volatile=var_55,
        transient=var_87,
        defaultValueLiteral=var_19,
        defaultValue=var_51,
        unsettable=var_87,
        derived=var_87,
        ecore_EStructuralFeature=[675],
        EStructuralFeature=var_87,
    )
    assert isinstance(var_88, python_code_.ecore_EStructuralFeature)
    python_code_.ecore_EClass(
        abstract=var_87,
        interface=var_55,
        eContainingClass36=var_19,
        ecore_EClass=var_79,
        ecore_EClass76=var_83,
        EClass81=var_88,
    )


def test_41():
    var_0 = python_code_.ecore_EFactory()
    var_0.create(ecore_eClass=var_0)
    var_3 = lambda *args, **kwargs: [3]
    var_6 = "_ecore_EAttribute__ecore_EAttribute"
    var_7 = python_code_.ecore_EEnum()
    assert isinstance(var_7, python_code_.ecore_EEnum)
    var_8 = python_code_.ecore_EEnumLiteral(
        value=var_3, instance=var_6, literal=var_3, EEnumLiteral=var_7
    )
    assert isinstance(var_8, python_code_.ecore_EEnumLiteral)


@pytest.mark.xfail(strict=True)
def test_42():
    var_3 = "\niZ,w`>z|ZS8"
    var_32 = complex
    var_34 = python_code_.ecore_EObject()
    var_34.eCrossReferences()
    var_36 = "%<qF"
    var_37 = True
    var_38 = python_code_.ecore_EStructuralFeature(
        changeable=var_32,
        volatile=-890,
        transient=var_3,
        defaultValueLiteral=var_36,
        defaultValue=None,
        unsettable=True,
        derived=var_37,
        EStructuralFeature=var_32,
        eStructuralFeatures=[],
    )
    assert isinstance(var_38, python_code_.ecore_EStructuralFeature)
    var_38.getContainerClass()
    var_40 = True
    var_41 = var_34.eIsSet(ecore_feature=var_32)
    var_42 = var_34.eSet(ecore_newValue=(), ecore_feature=complex(-1335.488746, 1203.0))
    python_code_.ecore_EClass(
        abstract=var_37,
        interface=var_40,
        ecore_EClass15=829,
        ecore_EClass29=var_41,
        ecore_EClass8=var_42,
    )


@pytest.mark.xfail(strict=True)
def test_43():
    var_0 = python_code_.ecore_ETypeParameter()
    var_1 = python_code_.ecore_EGenericType
    var_2 = ".Q"
    var_3 = python_code_.ecore_EClassifier(
        instanceClass=var_1,
        defaultValue=var_2,
        instanceTypeName=var_1,
        instanceClassName=var_2,
        eClassifiers=var_1,
        ecore_EClassifier83=var_1,
        ecore_EClassifier104=var_2,
    )
    assert isinstance(var_3, python_code_.ecore_EClassifier)
    python_code_.ecore_EGenericType(
        ecore_EGenericType41=var_2,
        ecore_EGenericType90=set(),
        ecore_EGenericType94=var_3,
        ecore_EGenericType107=None,
        ecore_EGenericType98=None,
        ecore_EGenericType96=var_3,
        ecore_EGenericType100=var_0,
    )


def test_44():
    var_1 = python_code_.ecore_EFactory()
    var_3 = python_code_.ecore_EFactory(EFactory=var_1)
    assert isinstance(var_3, python_code_.ecore_EFactory)


@pytest.mark.xfail(strict=True)
def test_45():
    var_1 = python_code_.ecore_EFactory()
    var_5 = lambda *args, **kwargs: "ecore_ETypeParameter106"
    var_6 = python_code_.ecore_EEnum()
    assert isinstance(var_6, python_code_.ecore_EEnum)
    var_7 = var_6.getEEnumLiteralByLiteral(ecore_literal="Q\nM#fFX")
    var_8 = python_code_.ecore_EObject()
    var_9 = var_8.eContainer()
    var_10 = var_6.getEEnumLiteralByLiteral(ecore_literal=var_5)
    var_11 = (
        lambda *args, **kwargs: "_ecore_EAttribute__ecore_EAttribute13-EClassifier-ecore_EStructuralFeature"
    )
    python_code_.ecore_EClass(
        abstract=var_1,
        interface=var_5,
        ecore_EClass15=var_7,
        ecore_EClass17=var_9,
        ecore_EClass29=set(),
        eContainingClass36=var_10,
        ecore_EClass38=var_5,
        ecore_EClass40=var_5,
        ecore_EClass=var_5,
        ecore_EClass76=var_11,
    )


@pytest.mark.xfail(strict=True)
def test_46():
    var_0 = "eModelElement"
    var_3 = True
    var_4 = python_code_.ecore_EStructuralFeature(
        changeable=True,
        volatile=var_3,
        transient=True,
        defaultValueLiteral=var_0,
        defaultValue=var_0,
        unsettable=var_3,
        derived=True,
    )
    assert isinstance(var_4, python_code_.ecore_EStructuralFeature)
    var_24 = str
    var_25 = "_ecore_EReference__ecore_EReference75._ecore_EClass__ecore_EClass17"
    python_code_.ecore_EClassifier(
        instanceClass=var_0,
        defaultValue=var_25,
        instanceTypeName=var_24,
        instanceClassName=(),
        ecore_EClassifier=1,
    )


def test_47():
    var_0 = python_code_.ecore_ETypeParameter()
    var_1 = python_code_.ecore_EGenericType
    var_2 = ".LQ"
    var_3 = python_code_.ecore_EClassifier(
        instanceClass=var_1,
        defaultValue=var_2,
        instanceTypeName=var_1,
        instanceClassName=var_2,
        eClassifiers=var_1,
        ecore_EClassifier83=var_1,
        ecore_EClassifier104=var_2,
    )
    assert isinstance(var_3, python_code_.ecore_EClassifier)
    var_4 = python_code_.ecore_EGenericType(ecore_EGenericType41=var_2)
    var_36 = False
    var_37 = False
    var_38 = python_code_.ecore_EStructuralFeature(
        changeable=var_1,
        volatile=[],
        transient=var_36,
        defaultValueLiteral=(),
        defaultValue=var_4,
        unsettable=var_1,
        derived=var_37,
        EStructuralFeature=var_37,
    )
    assert isinstance(var_38, python_code_.ecore_EStructuralFeature)
    python_code_.ecore_EStructuralFeature(
        changeable=[False, 600.4],
        volatile=var_0,
        transient="TZ{6IC]",
        defaultValueLiteral=False,
        defaultValue=1560.01,
        unsettable=b"\r\x07upA\xe1Y\xec",
        derived="_ecore_EClass__ecore_EClass28",
    )
    var_34 = python_code_.ecore_EDataType(
        serializable=(
            "eContainingClass36,ecore_EGenericType87,ecore_EPackage,_ecore_EAnnotation__eAnnotations",
        )
    )
    assert isinstance(var_34, python_code_.ecore_EDataType)
    var_4.isInstance(ecore_object=False)
    var_6 = python_code_.ecore_EObject(ecore_EObject7=[-2430])
    var_6.eCrossReferences()
