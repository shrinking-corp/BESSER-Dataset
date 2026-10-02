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
    FSM,
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
    ecore_FSM,
    ecore_State,
    ecore_Transition,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = python_code_.EDataType()
    var_1 = python_code_.ecore_EObject(ecore_EObject=complex(2732.871627, 449.66))
    var_1.eGet(ecore_resolve=[], ecore_feature=var_0)
    var_3 = python_code_.ecore_EEnum()
    assert isinstance(var_3, python_code_.ecore_EEnum)
    var_4 = lambda *args, **kwargs: "V0z^9\t0V"
    var_3.getEEnumLiteralByLiteral(ecore_literal=var_4)
    var_7 = 'Mu\\4\x0b+{F"^zU "pd'
    var_8 = "ecore_EAttribute13"
    var_9 = python_code_.ecore_EClassifier(
        instanceClassName=var_7,
        instanceClass=var_8,
        defaultValue=var_4,
        instanceTypeName=b"\x13z\x9br\x1f8",
        ecore_EClassifier96=var_1,
    )
    assert isinstance(var_9, python_code_.ecore_EClassifier)
    var_9.isInstance(ecore_object=var_4)
    var_11 = True
    var_12 = complex
    var_13 = python_code_.ecore_FSM()
    var_14 = python_code_.ecore_State(
        name=var_8, ecore_State114=var_12, ownedState=var_13
    )
    assert isinstance(var_14, python_code_.ecore_State)
    python_code_.ecore_EClass(
        abstract=1587,
        interface=var_11,
        ecore_EClass={},
        ecore_EClass8=723.09,
        eContainingClass=0,
        ecore_EClass17=var_12,
        ecore_EClass31=var_12,
        ecore_EClass38=var_1,
        EClass=var_12,
        ecore_EClass121=var_14,
    )


def test_1():
    var_0 = python_code_.ecore_EEnum(eEnum=set())
    assert isinstance(var_0, python_code_.ecore_EEnum)
    var_28 = python_code_.ecore_EObject()
    var_28.eContainingFeature()
    var_30 = python_code_.EModelElement()
    var_31 = object
    var_28.eSet(ecore_feature=["(|CxL2%*xD{Gq\x0b", -329.33], ecore_newValue=var_31)
    var_40 = False
    var_28.eIsSet(ecore_feature=var_30)
    var_80 = var_28.eContainmentFeature()
    var_81 = python_code_.ecore_EOperation(
        eOperations=var_40, ecore_EOperation56=var_80
    )
    assert isinstance(var_81, python_code_.ecore_EOperation)


def test_2():
    var_0 = python_code_.ecore_EEnum(eEnum=None)
    assert isinstance(var_0, python_code_.ecore_EEnum)
    var_0.getEEnumLiteral(ecore_value=-1173.9)


def test_3():
    var_1 = python_code_.ecore_EObject()
    var_21 = "IZ)n  r/"
    var_22 = "-,~>_Vux$Q)KYhG7ue"
    var_23 = python_code_.ecore_EPackage(nsURI=var_21, nsPrefix=var_22, EPackage69=())
    assert isinstance(var_23, python_code_.ecore_EPackage)
    var_1.eIsProxy()


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.ecore_EModelElement()
    var_1 = lambda *args, **kwargs: -1747
    var_0.getEAnnotation(ecore_source=var_1)
    var_3 = python_code_.ecore_EObject()
    var_3.eContainingFeature()
    var_3.eIsProxy()
    var_12 = abs
    var_13 = python_code_.ecore_EFactory()
    python_code_.ecore_EPackage(
        nsURI=None, nsPrefix=var_12, eSuperPackage=580.04, EPackage47=var_13
    )


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = "ecore_EReference76 ecore_EClass12 Transition ecore_EReference79"
    var_1 = python_code_.ecore_EFactory()
    python_code_.ecore_EPackage(
        nsURI=(), nsPrefix=var_0, ePackage=var_1, ePackage63=None
    )


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = "K9E2m[Ib)@"
    var_1 = python_code_.ecore_ETypeParameter
    var_2 = python_code_.ecore_EObject()
    var_3 = var_2.eUnset(ecore_feature=var_2)
    var_4 = "tRhzhI6(VU+"
    var_5 = python_code_.ecore_EPackage(
        nsURI=var_4, nsPrefix=3175, EPackage66=var_3, EPackage69=var_0, EPackage47=var_2
    )
    assert isinstance(var_5, python_code_.ecore_EPackage)
    python_code_.ecore_EPackage(
        nsURI=var_0,
        nsPrefix=var_1,
        ePackage63=var_3,
        eSubpackages=var_5,
        EPackage=b"\xc2\x1b_\x9a{\x89\xb1\x98\xb4\\\x89",
    )


@pytest.mark.xfail(strict=True)
def test_7():
    python_code_.ecore_EObject()
    var_83 = "IZ)n  r/"
    var_84 = "-,~>_Vux$Q)KYhG7ue"
    var_85 = python_code_.ecore_EPackage(nsURI=var_83, nsPrefix=var_84, EPackage69=())
    assert isinstance(var_85, python_code_.ecore_EPackage)
    python_code_.ecore_EFactory(eFactoryInstance=var_85)


def test_8():
    var_0 = False
    var_1 = "ecore_:EObject7"
    var_3 = lambda *args, **kwargs: [2109.21, 476.75]
    var_8 = True
    var_31 = python_code_.ecore_EStructuralFeature(
        changeable=None,
        volatile=var_0,
        transient=var_0,
        defaultValueLiteral=var_3,
        defaultValue=var_1,
        unsettable={},
        derived=None,
        EStructuralFeature=var_8,
    )
    assert isinstance(var_31, python_code_.ecore_EStructuralFeature)


def test_9():
    var_0 = python_code_.ecore_EEnum(eEnum=set())
    assert isinstance(var_0, python_code_.ecore_EEnum)
    var_5 = True
    var_8 = False
    var_9 = python_code_.ecore_EStructuralFeature(
        changeable=var_5,
        volatile=var_5,
        transient=var_8,
        defaultValueLiteral="7\nM[jGp@",
        defaultValue="_ecore_EPackage__eSubpackages-ecore_EAnnotation4",
        unsettable=var_5,
        derived=var_5,
        eStructuralFeatures=var_0,
        ecore_EStructuralFeature=var_8,
    )
    assert isinstance(var_9, python_code_.ecore_EStructuralFeature)
    var_9.getFeatureID()


def test_10():
    python_code_.ecore_EObject(ecore_EObject7=None)


def test_11():
    var_1 = python_code_.ecore_EObject(ecore_EObject=complex(2732.871627, 449.66))
    var_3 = python_code_.ecore_EEnum()
    assert isinstance(var_3, python_code_.ecore_EEnum)
    var_1.eContainer()


def test_12():
    var_0 = python_code_.ecore_EFactory(EFactory=None, eFactoryInstance=None)
    assert isinstance(var_0, python_code_.ecore_EFactory)
    var_0.convertToString(ecore_eDataType=float, ecore_instanceValue=var_0)


def test_13():
    var_80 = python_code_.ecore_EAttribute(iD=("", "_T s^/7#sv<m"))
    assert isinstance(var_80, python_code_.ecore_EAttribute)
    var_81 = python_code_.ecore_EAnnotation(source=var_80, eAnnotations=var_80)
    assert isinstance(var_81, python_code_.ecore_EAnnotation)
    var_82 = python_code_.ecore_EObject(ecore_EObject=var_81)
    var_82.eCrossReferences()


@pytest.mark.xfail(strict=True)
def test_14():
    var_0 = False
    var_1 = "ecore_EObject7"
    var_2 = "/2l]uo"
    var_3 = lambda *args, **kwargs: [2109.21, 476.75]
    var_4 = python_code_.ecore_EStructuralFeature(
        changeable=var_0,
        volatile=var_0,
        transient=var_0,
        defaultValueLiteral=var_1,
        defaultValue=var_2,
        unsettable=var_0,
        derived=var_3,
    )
    assert isinstance(var_4, python_code_.ecore_EStructuralFeature)
    python_code_.ecore_EAnnotation(
        source=var_2,
        eAnnotations=var_3,
        ecore_EAnnotation4=True,
        ecore_EAnnotation6=None,
        EAnnotation=None,
    )


@pytest.mark.xfail(strict=True)
def test_15():
    var_0 = python_code_.ecore_EEnum(eEnum=None)
    assert isinstance(var_0, python_code_.ecore_EEnum)
    var_3 = True
    var_7 = lambda *args, **kwargs: True
    var_8 = False
    var_9 = python_code_.ecore_EReference(
        containment=var_3,
        container=var_8,
        resolveProxies=var_3,
        ecore_EReference24=var_7,
    )
    assert isinstance(var_9, python_code_.ecore_EReference)
    var_10 = "h`5"
    var_11 = "Dya4S1<-ZH\x0b "
    var_12 = python_code_.ecore_EClassifier(
        instanceClassName=var_10,
        instanceClass=var_10,
        defaultValue=var_11,
        instanceTypeName=None,
    )
    assert isinstance(var_12, python_code_.ecore_EClassifier)
    var_12.getClassifierID()
    var_14 = python_code_.ecore_EOperation()
    var_14.isOverrideOf(ecore_someOperation=var_7)
    var_17 = False
    var_18 = repr
    var_19 = set()
    python_code_.ecore_EClass(
        abstract=var_17,
        interface=var_18,
        ecore_EClass28=var_19,
        ecore_EClass=var_14,
        eContainingClass=True,
        ecore_EClass20=var_19,
        ecore_EClass23=var_19,
        ecore_EClass26=set(),
    )


@pytest.mark.xfail(strict=True)
def test_16():
    var_1 = python_code_.ecore_ETypeParameter
    var_2 = python_code_.ecore_EObject()
    var_3 = var_2.eUnset(ecore_feature=var_1)
    var_11 = True
    python_code_.ecore_EReference(
        containment=2477.72,
        container=var_11,
        resolveProxies=var_3,
        ecore_EReference74={},
        ecore_EReference79=3,
    )


@pytest.mark.xfail(strict=True)
def test_17():
    var_0 = python_code_.ecore_Transition
    var_1 = True
    var_2 = True
    var_3 = True
    var_4 = python_code_.ecore_EReference(
        containment=var_2,
        container=var_0,
        resolveProxies=var_1,
        ecore_EReference18=var_3,
    )
    assert isinstance(var_4, python_code_.ecore_EReference)
    var_5 = python_code_.ecore_EObject(ecore_EObject=var_0)
    var_6 = var_5.eCrossReferences()
    python_code_.ecore_EReference(
        containment=var_0,
        container=var_2,
        resolveProxies=var_3,
        ecore_EReference74=var_4,
        ecore_EReference76=var_2,
        ecore_EReference79=var_6,
        ecore_EReference=-1366,
        ecore_EReference18=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_18():
    var_0 = python_code_.EStructuralFeature()
    var_1 = True
    var_2 = lambda *args, **kwargs: "+b\n#X3Pmxm~{%L"
    python_code_.ecore_EClass(
        abstract=var_1,
        interface=var_2,
        ecore_EClass=-3039.08,
        ecore_EClass12=var_2,
        ecore_EClass17=b"\x7f/\x91$\xbc\x83/",
        eContainingClass36=var_0,
        ecore_EClass121=[],
    )


@pytest.mark.xfail(strict=True)
def test_19():
    var_0 = python_code_.ecore_EEnum(eEnum=set())
    assert isinstance(var_0, python_code_.ecore_EEnum)
    var_2 = python_code_.EModelElement()
    var_3 = python_code_.ecore_EObject()
    var_3.eContents()
    var_5 = True
    var_7 = python_code_.ecore_EAnnotation
    var_8 = False
    var_9 = python_code_.ecore_EStructuralFeature(
        changeable=var_7,
        volatile=var_5,
        transient=var_8,
        defaultValueLiteral=[-419.3, "rjYShS.*X"],
        defaultValue=-1545,
        unsettable=var_0,
        derived=var_5,
        eStructuralFeatures=var_7,
        ecore_EStructuralFeature={},
    )
    assert isinstance(var_9, python_code_.ecore_EStructuralFeature)
    var_11 = False
    var_12 = lambda *args, **kwargs: [False, "{T,", False]
    var_13 = var_3.eGet(ecore_resolve=var_12, ecore_feature=-3053)
    var_14 = var_3.eContainingFeature()
    var_15 = var_9.getFeatureID()
    python_code_.ecore_EClass(
        abstract=var_11,
        interface=var_7,
        ecore_EClass=var_12,
        ecore_EClass17=var_13,
        ecore_EClass20=var_12,
        ecore_EClass23=var_2,
        ecore_EClass26=542,
        ecore_EClass29=var_14,
        eContainingClass36=var_15,
        ecore_EClass38=var_15,
    )


def test_20():
    var_5 = python_code_.ecore_EOperation(
        ecore_EOperation=None, ecore_EOperation56=set()
    )
    assert isinstance(var_5, python_code_.ecore_EOperation)
    var_6 = python_code_.ecore_EFactory()
    var_10 = python_code_.ecore_EObject(ecore_EObject=var_6)
    var_10.eCrossReferences()
    var_21 = python_code_.FSM()
    var_10.eUnset(ecore_feature=var_21)


def test_21():
    var_0 = python_code_.ecore_EEnum(eEnum=set())
    assert isinstance(var_0, python_code_.ecore_EEnum)
    var_3 = python_code_.ecore_EObject()
    var_5 = True
    var_7 = python_code_.ecore_EAnnotation
    var_8 = False
    var_9 = python_code_.ecore_EStructuralFeature(
        changeable=var_7,
        volatile=var_5,
        transient=var_8,
        defaultValueLiteral=[-419.3, "rjYShS.*X"],
        defaultValue=-1545,
        unsettable=var_0,
        derived=var_5,
        eStructuralFeatures=var_7,
        ecore_EStructuralFeature={},
    )
    assert isinstance(var_9, python_code_.ecore_EStructuralFeature)
    var_9.getFeatureID()
    var_12 = lambda *args, **kwargs: [False, "{T,", False]
    var_3.eGet(ecore_resolve=var_12, ecore_feature=-3053)
    var_3.eResource()
    var_3.eIsSet(ecore_feature=())
    var_0.getEEnumLiteral(ecore_value=914.3)


def test_22():
    var_2 = python_code_.ecore_EObject()
    var_2.eContents()


def test_23():
    var_0 = python_code_.ecore_EFactory(EFactory=None, eFactoryInstance=None)
    assert isinstance(var_0, python_code_.ecore_EFactory)
    var_4 = python_code_.ecore_EObject()
    var_4.eContainingFeature()
    var_6 = python_code_.EModelElement()
    var_7 = object
    var_4.eSet(ecore_feature=var_7, ecore_newValue=var_6)
    python_code_.ecore_EGenericType(
        ecore_EGenericType87=-2924.59,
        ecore_EGenericType=var_7,
        ecore_EGenericType104=128.67,
    )
    var_15 = False
    var_16 = python_code_.ecore_EAttribute(iD=var_15, ecore_EAttribute80=var_15)
    assert isinstance(var_16, python_code_.ecore_EAttribute)


def test_24():
    var_0 = python_code_.EDataType()
    python_code_.ecore_EObject(ecore_EObject=complex(2732.871627, 449.66))
    var_3 = python_code_.ecore_EEnum()
    assert isinstance(var_3, python_code_.ecore_EEnum)
    var_21 = "IZ)n  r/"
    var_22 = "-,~>_Vux$Q)KYhG7ue"
    var_23 = python_code_.ecore_EPackage(nsURI=var_21, nsPrefix=var_22, EPackage69=())
    assert isinstance(var_23, python_code_.ecore_EPackage)
    var_23.getEClassifier(ecore_name=var_0)


def test_25():
    var_0 = python_code_.ecore_EFactory(EFactory=None, eFactoryInstance=None)
    assert isinstance(var_0, python_code_.ecore_EFactory)
    var_4 = python_code_.ecore_EObject()
    var_4.eContainingFeature()
    var_7 = object
    var_4.eSet(ecore_feature=["(|CxL2%*xD{Gq\x0b", -329.33], ecore_newValue=var_7)
    var_9 = python_code_.ecore_EGenericType(
        ecore_EGenericType87=-2924.59,
        ecore_EGenericType=var_7,
        ecore_EGenericType104=128.67,
    )
    var_9.isInstance(ecore_object=var_7)


def test_26():
    var_1 = python_code_.EDataType()
    var_2 = python_code_.ecore_EObject(ecore_EObject=var_1)
    var_2.eContainingFeature()
    var_2.eClass()


def test_27():
    var_47 = python_code_.EClassifier()
    var_74 = python_code_.ecore_EClass
    var_76 = False
    var_77 = False
    var_78 = python_code_.ecore_EStructuralFeature(
        changeable=1112.59,
        volatile=var_76,
        transient=var_77,
        defaultValueLiteral=var_74,
        defaultValue=var_47,
        unsettable=var_76,
        derived=1,
        EStructuralFeature=var_74,
    )
    assert isinstance(var_78, python_code_.ecore_EStructuralFeature)


@pytest.mark.xfail(strict=True)
def test_28():
    var_0 = "^"
    var_1 = lambda *args, **kwargs: 1921
    python_code_.ecore_State(
        name=var_0,
        source=complex(-135.743744, 1730.5354),
        ecore_State120=[],
        State123=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_29():
    var_0 = python_code_.EDataType()
    var_1 = python_code_.ecore_EObject(ecore_EObject=complex(2732.871627, 449.66))
    var_1.eGet(ecore_resolve=[], ecore_feature=var_0)
    var_3 = python_code_.ecore_EEnum()
    assert isinstance(var_3, python_code_.ecore_EEnum)
    var_4 = lambda *args, **kwargs: "V0z^9\t0V"
    var_3.getEEnumLiteralByLiteral(ecore_literal=var_4)
    var_7 = 'Mu\\4\x0b+{F"^zU "pd'
    var_8 = "ecore_EAttribute13"
    var_9 = python_code_.ecore_EClassifier(
        instanceClassName=var_7,
        instanceClass=var_8,
        defaultValue=var_4,
        instanceTypeName=b"\x13z\x9br\x1f8",
        ecore_EClassifier96=var_1,
    )
    assert isinstance(var_9, python_code_.ecore_EClassifier)
    var_10 = var_9.isInstance(ecore_object=var_4)
    var_11 = True
    var_12 = complex
    var_13 = python_code_.ecore_FSM()
    var_14 = python_code_.ecore_State(
        name=var_7, ecore_State114=var_13, target=set(), ecore_State120={var_9, var_10}
    )
    assert isinstance(var_14, python_code_.ecore_State)
    python_code_.ecore_EClass(
        abstract=1587,
        interface=var_11,
        ecore_EClass={},
        ecore_EClass8=723.09,
        eContainingClass=0,
        ecore_EClass17=var_12,
        ecore_EClass31=var_12,
        ecore_EClass38=var_1,
        EClass=var_12,
        ecore_EClass121=var_14,
    )


@pytest.mark.xfail(strict=True)
def test_30():
    var_0 = python_code_.EDataType()
    var_1 = python_code_.ecore_EObject(ecore_EObject=complex(2732.871627, 449.66))
    var_1.eGet(ecore_resolve=[], ecore_feature=var_0)
    var_3 = python_code_.ecore_EEnum()
    assert isinstance(var_3, python_code_.ecore_EEnum)
    var_4 = lambda *args, **kwargs: "V0z^9\t0V"
    var_3.getEEnumLiteralByLiteral(ecore_literal=var_4)
    var_7 = 'Mu\\4\x0b+{F"^zU "pd'
    var_8 = "ecore_EAttribute13"
    var_9 = python_code_.ecore_EClassifier(
        instanceClassName=var_7,
        instanceClass="flQl}Q\x0b+V4IiA}",
        defaultValue=var_7,
        instanceTypeName=var_8,
        EClassifier=var_0,
        ecore_EClassifier84=var_3,
        eClassifiers=None,
        ecore_EClassifier=set(),
        ecore_EClassifier105=None,
        ecore_EClassifier96=None,
    )
    assert isinstance(var_9, python_code_.ecore_EClassifier)
    var_9.isInstance(ecore_object=var_4)
    var_11 = True
    var_12 = complex
    var_13 = python_code_.ecore_FSM()
    var_14 = python_code_.ecore_State(
        name=var_8, ecore_State114=var_12, ownedState=var_13
    )
    assert isinstance(var_14, python_code_.ecore_State)
    python_code_.ecore_EClass(
        abstract=1587,
        interface=var_11,
        ecore_EClass={},
        ecore_EClass8=723.09,
        eContainingClass=0,
        ecore_EClass17=var_12,
        ecore_EClass31=var_12,
        ecore_EClass38=var_1,
        EClass=var_12,
        ecore_EClass121=var_14,
    )


def test_31():
    python_code_.ecore_EObject()
    var_21 = python_code_.ecore_EFactory(eFactoryInstance=False)
    assert isinstance(var_21, python_code_.ecore_EFactory)
    var_25 = python_code_.ecore_EOperation(EOperation=complex(1103.4, -7002.5135))
    assert isinstance(var_25, python_code_.ecore_EOperation)


def test_32():
    var_6 = False
    var_7 = python_code_.ecore_EClass
    var_8 = python_code_.ecore_EFactory(eFactoryInstance=var_7)
    assert isinstance(var_8, python_code_.ecore_EFactory)
    var_8.create(ecore_eClass=())
    var_13 = False
    var_14 = python_code_.ecore_EAttribute(iD=var_13, ecore_EAttribute80=var_6)
    assert isinstance(var_14, python_code_.ecore_EAttribute)


@pytest.mark.xfail(strict=True)
def test_33():
    var_2 = python_code_.ecore_EObject()
    var_3 = var_2.eContainmentFeature()
    var_4 = var_2.eContainer()
    var_5 = False
    var_6 = "\n\\s"
    var_7 = dict
    var_8 = python_code_.ecore_EStructuralFeature(
        changeable=var_5,
        volatile=var_5,
        transient=None,
        defaultValueLiteral=var_6,
        defaultValue=var_6,
        unsettable=[],
        derived=None,
        eStructuralFeatures=var_7,
    )
    assert isinstance(var_8, python_code_.ecore_EStructuralFeature)
    var_9 = var_8.getFeatureID()
    python_code_.ecore_EClass(
        abstract=var_4,
        interface=var_5,
        ecore_EClass28=var_5,
        ecore_EClass12=var_9,
        ecore_EClass15=var_3,
    )


def test_34():
    var_7 = python_code_.ecore_EObject()
    var_14 = True
    var_29 = python_code_.ecore_EDataType(serializable=var_14, ecore_EDataType=var_14)
    assert isinstance(var_29, python_code_.ecore_EDataType)
    var_7.eIsProxy()
    var_7.eInvoke(ecore_arguments=var_14, ecore_operation=[-1044.7, True])
    var_7.eContents()


def test_35():
    var_5 = python_code_.ecore_EOperation(ecore_EOperation56=[2, -846])
    assert isinstance(var_5, python_code_.ecore_EOperation)
    var_6 = python_code_.ecore_EFactory()
    var_34 = python_code_.ecore_EDataType(serializable=var_5)
    assert isinstance(var_34, python_code_.ecore_EDataType)
    var_10 = python_code_.ecore_EObject(ecore_EObject=var_6)
    var_10.eCrossReferences()
    var_21 = python_code_.FSM()
    var_10.eUnset(ecore_feature=var_21)


@pytest.mark.xfail(strict=True)
def test_36():
    var_0 = True
    var_1 = python_code_.ecore_EObject()
    var_2 = var_1.eContents()
    var_3 = python_code_.ecore_EFactory
    var_4 = python_code_.ecore_ETypeParameter
    python_code_.ecore_EClass(
        abstract=var_0,
        interface=var_0,
        EClass82=(188.93, True),
        ecore_EClass28=var_2,
        ecore_EClass8=var_0,
        eContainingClass=var_0,
        ecore_EClass20="EEnumLiteral-_ecore_EClass__eContainingClass",
        ecore_EClass31=var_3,
        ecore_EClass29=var_4,
        ecore_EClass33=var_4,
    )


def test_37():
    var_1 = python_code_.ecore_EObject(ecore_EObject=complex(2732.871627, 449.66))
    var_3 = python_code_.ecore_EEnum()
    assert isinstance(var_3, python_code_.ecore_EEnum)
    var_3.getEEnumLiteral(ecore_value=-1173.9)
    var_28 = lambda *args, **kwargs: 1
    var_1.eInvoke(ecore_arguments=var_28, ecore_operation=var_28)


def test_38():
    var_0 = "K9EWmU[Ib)@"
    var_44 = 2402
    var_45 = python_code_.ecore_EEnumLiteral(
        value=var_44, instance=var_0, literal=var_0
    )
    assert isinstance(var_45, python_code_.ecore_EEnumLiteral)


def test_39():
    var_46 = "ecore_EClassifier96.eAnnotations.EPackage"
    var_47 = True
    var_48 = True
    var_49 = True
    var_50 = python_code_.ecore_ETypedElement(
        ordered=var_47,
        unique=var_48,
        lowerBound=var_46,
        upperBound={},
        many=var_47,
        required=var_49,
    )
    assert isinstance(var_50, python_code_.ecore_ETypedElement)
    python_code_.ecore_EObject(ecore_EObject7=var_48)


def test_40():
    var_33 = python_code_.ecore_EObject(ecore_EObject7=None)
    var_33.eAllContents()
