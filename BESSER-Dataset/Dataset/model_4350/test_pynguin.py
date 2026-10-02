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
    DifferenceElement,
    EAnnotation,
    EAttribute,
    EClass,
    EClassifier,
    EClassifier_Wildcard,
    EDataType,
    EEnum,
    EEnumLiteral,
    EFactory,
    EGenericType,
    EModelElement,
    ENamedElement,
    EObject,
    EOperation,
    EPackage,
    EParameter,
    EReference,
    EStringToStringMapEntry,
    EStructuralFeature,
    EStructuralFeature_Wildcard,
    ETypeParameter,
    ETypedElement,
    abstractmethod,
    date,
    datetime,
    ecoreDiff_AddedEAnnotation,
    ecoreDiff_AddedEAttribute,
    ecoreDiff_AddedEClass,
    ecoreDiff_AddedEClassifier,
    ecoreDiff_AddedEClassifier_Wildcard,
    ecoreDiff_AddedEDataType,
    ecoreDiff_AddedEEnum,
    ecoreDiff_AddedEEnumLiteral,
    ecoreDiff_AddedEFactory,
    ecoreDiff_AddedEGenericType,
    ecoreDiff_AddedEModelElement,
    ecoreDiff_AddedENamedElement,
    ecoreDiff_AddedEObject,
    ecoreDiff_AddedEOperation,
    ecoreDiff_AddedEPackage,
    ecoreDiff_AddedEParameter,
    ecoreDiff_AddedEReference,
    ecoreDiff_AddedEStringToStringMapEntry,
    ecoreDiff_AddedEStructuralFeature,
    ecoreDiff_AddedEStructuralFeature_Wildcard,
    ecoreDiff_AddedETypeParameter,
    ecoreDiff_AddedETypedElement,
    ecoreDiff_ChangedEAnnotation,
    ecoreDiff_ChangedEAttribute,
    ecoreDiff_ChangedEClass,
    ecoreDiff_ChangedEClassifier,
    ecoreDiff_ChangedEClassifier_Wildcard,
    ecoreDiff_ChangedEDataType,
    ecoreDiff_ChangedEEnum,
    ecoreDiff_ChangedEEnumLiteral,
    ecoreDiff_ChangedEFactory,
    ecoreDiff_ChangedEGenericType,
    ecoreDiff_ChangedEModelElement,
    ecoreDiff_ChangedENamedElement,
    ecoreDiff_ChangedEObject,
    ecoreDiff_ChangedEOperation,
    ecoreDiff_ChangedEPackage,
    ecoreDiff_ChangedEParameter,
    ecoreDiff_ChangedEReference,
    ecoreDiff_ChangedEStringToStringMapEntry,
    ecoreDiff_ChangedEStructuralFeature,
    ecoreDiff_ChangedEStructuralFeature_Wildcard,
    ecoreDiff_ChangedETypeParameter,
    ecoreDiff_ChangedETypedElement,
    ecoreDiff_DeletedEAnnotation,
    ecoreDiff_DeletedEAttribute,
    ecoreDiff_DeletedEClass,
    ecoreDiff_DeletedEClassifier,
    ecoreDiff_DeletedEClassifier_Wildcard,
    ecoreDiff_DeletedEDataType,
    ecoreDiff_DeletedEEnum,
    ecoreDiff_DeletedEEnumLiteral,
    ecoreDiff_DeletedEFactory,
    ecoreDiff_DeletedEGenericType,
    ecoreDiff_DeletedEModelElement,
    ecoreDiff_DeletedENamedElement,
    ecoreDiff_DeletedEObject,
    ecoreDiff_DeletedEOperation,
    ecoreDiff_DeletedEPackage,
    ecoreDiff_DeletedEParameter,
    ecoreDiff_DeletedEReference,
    ecoreDiff_DeletedEStringToStringMapEntry,
    ecoreDiff_DeletedEStructuralFeature,
    ecoreDiff_DeletedEStructuralFeature_Wildcard,
    ecoreDiff_DeletedETypeParameter,
    ecoreDiff_DeletedETypedElement,
    ecoreDiff_DifferenceElement,
    ecoreDiff_DifferenceModel,
    ecoreDiff_EAnnotation,
    ecoreDiff_EAttribute,
    ecoreDiff_EClass,
    ecoreDiff_EClassifier,
    ecoreDiff_EClassifier_Wildcard,
    ecoreDiff_EDataType,
    ecoreDiff_EEnum,
    ecoreDiff_EEnumLiteral,
    ecoreDiff_EFactory,
    ecoreDiff_EGenericType,
    ecoreDiff_EModelElement,
    ecoreDiff_ENamedElement,
    ecoreDiff_EObject,
    ecoreDiff_EOperation,
    ecoreDiff_EPackage,
    ecoreDiff_EParameter,
    ecoreDiff_EReference,
    ecoreDiff_EStringToStringMapEntry,
    ecoreDiff_EStructuralFeature,
    ecoreDiff_EStructuralFeature_Wildcard,
    ecoreDiff_ETypeParameter,
    ecoreDiff_ETypedElement,
    time,
)


def test_0():
    var_0 = python_code_.ecoreDiff_ChangedEEnumLiteral()
    var_4 = "_ecoreDiff_EStructuralFeature__eStructuralFeatures"
    var_5 = python_code_.ecoreDiff_ChangedENamedElement()
    var_6 = python_code_.ecoreDiff_ENamedElement(
        name=var_4, ecoreDiff_ENamedElement=var_5
    )
    assert isinstance(var_6, python_code_.ecoreDiff_ENamedElement)
    var_9 = python_code_.EDataType
    var_12 = -6587
    var_13 = python_code_.ecoreDiff_EEnumLiteral(
        value=var_12, instance=var_9, literal=var_4, ecoreDiff_EEnumLiteral=var_0
    )
    assert isinstance(var_13, python_code_.ecoreDiff_EEnumLiteral)


def test_1():
    var_14 = python_code_.ecoreDiff_EEnum()
    var_18 = "_ecoreDiff_EPackage__EPackage,eStructuralFeatures,_ecoreDiff_EEnumLiteral__ecoreDiff_EEnumLiteral,ePackage50"
    var_19 = python_code_.ecoreDiff_EEnumLiteral(
        value=1,
        instance="EPackage45:_ecoreDiff_EPackage__eSuperPackage:ecoreDiff_EClass",
        literal=var_18,
        EEnumLiteral=var_14,
    )
    assert isinstance(var_19, python_code_.ecoreDiff_EEnumLiteral)


def test_2():
    var_0 = python_code_.ecoreDiff_ChangedEEnumLiteral()
    var_4 = "_ecoreDiff_EStructuralFeature__eStructuralFeatures"
    var_5 = python_code_.ecoreDiff_ChangedENamedElement()
    var_6 = python_code_.ecoreDiff_ENamedElement(
        name=var_4, ecoreDiff_ENamedElement=var_5
    )
    assert isinstance(var_6, python_code_.ecoreDiff_ENamedElement)
    var_9 = python_code_.EDataType
    var_10 = python_code_.ecoreDiff_EPackage(
        nsURI=var_6,
        nsPrefix=b"\x82\x83r\x98-}\xf1\xfa\xcc\xe1\x95\xa8",
        ePackage=var_9,
        EPackage45=var_5,
        ePackage50=[2076, False, False],
        EPackage52=var_5,
    )
    assert isinstance(var_10, python_code_.ecoreDiff_EPackage)
    var_12 = -6587
    var_13 = python_code_.ecoreDiff_EEnumLiteral(
        value=var_12, instance=var_9, literal=var_4, ecoreDiff_EEnumLiteral=var_0
    )
    assert isinstance(var_13, python_code_.ecoreDiff_EEnumLiteral)


def test_3():
    var_0 = "\"F6\nOg\x0bd'1Dl~Nf"
    var_1 = python_code_.ecoreDiff_EClassifier(
        instanceClassName=var_0,
        instanceClass=True,
        defaultValue=var_0,
        instanceTypeName="",
        ecoreDiff_EClassifier64=b"\x7f\xb2\xf1\x0e",
        ecoreDiff_EClassifier140=var_0,
        ecoreDiff_EClassifier80=2686.43,
    )
    assert isinstance(var_1, python_code_.ecoreDiff_EClassifier)


def test_4():
    var_2 = python_code_.ecoreDiff_DeletedEOperation()
    var_5 = python_code_.ecoreDiff_ChangedENamedElement()
    var_6 = python_code_.ecoreDiff_ENamedElement(
        name="_ecoreDiff_EAnnotation__ecoreDiff_EAnnotation112:_ecoreDiff_EClass__ecoreDiff_EClass17:ecoreDiff_EClass29",
        ecoreDiff_ENamedElement=var_5,
    )
    assert isinstance(var_6, python_code_.ecoreDiff_ENamedElement)
    var_9 = python_code_.EDataType
    var_14 = "ecoreDiff_EOperation"
    var_15 = python_code_.ecoreDiff_EGenericType()
    var_16 = python_code_.ecoreDiff_EClassifier(
        instanceClassName=var_9,
        instanceClass=[],
        defaultValue=var_2,
        instanceTypeName=var_14,
        EClassifier=False,
        ecoreDiff_EClassifier73=var_15,
    )
    assert isinstance(var_16, python_code_.ecoreDiff_EClassifier)


def test_5():
    var_0 = python_code_.ecoreDiff_AddedEEnum()
    var_2 = True
    var_3 = True
    var_4 = python_code_.ETypeParameter
    var_5 = python_code_.ecoreDiff_EReference(
        containment=var_2,
        container=var_0,
        resolveProxies=var_3,
        ecoreDiff_EReference=None,
        ecoreDiff_EReference24=var_4,
        ecoreDiff_EReference98=2046,
        ecoreDiff_EReference96=-1405.41,
    )
    assert isinstance(var_5, python_code_.ecoreDiff_EReference)


def test_6():
    var_0 = python_code_.ENamedElement()
    var_1 = python_code_.EPackage()
    var_4 = python_code_.ecoreDiff_DeletedEAnnotation()
    var_5 = python_code_.ecoreDiff_ChangedEDataType()
    var_7 = lambda *args, **kwargs: False
    python_code_.ecoreDiff_EStringToStringMapEntry(
        key=var_1, value=var_1, ecoreDiff_EStringToStringMapEntry119=var_7
    )
    var_24 = False
    var_25 = False
    var_26 = python_code_.ecoreDiff_ChangedEReference()
    var_27 = python_code_.ecoreDiff_EReference(
        containment=var_24,
        container=var_24,
        resolveProxies=var_25,
        ecoreDiff_EReference18=var_5,
        ecoreDiff_EReference100=(),
        ecoreDiff_EReference232=var_26,
    )
    assert isinstance(var_27, python_code_.ecoreDiff_EReference)
    var_30 = python_code_.ecoreDiff_EStructuralFeature(
        changeable=var_4,
        volatile=-270,
        transient=var_5,
        defaultValueLiteral=b"\x9fO+\x82\x9a\xbe%\x14bm\x97:4",
        defaultValue=var_0,
        unsettable=var_7,
        derived=var_25,
        EStructuralFeature=3,
    )
    assert isinstance(var_30, python_code_.ecoreDiff_EStructuralFeature)


def test_7():
    var_4 = True
    var_5 = True
    var_6 = True
    var_7 = lambda *args, **kwargs: "_ecoreDiff_EEnumLiteral__EEnumLiteral:EOperation"
    var_8 = python_code_.ecoreDiff_EStructuralFeature(
        changeable=var_4,
        volatile=var_5,
        transient=var_6,
        defaultValueLiteral=var_7,
        defaultValue=None,
        unsettable={},
        derived=var_4,
    )
    assert isinstance(var_8, python_code_.ecoreDiff_EStructuralFeature)


def test_8():
    var_6 = python_code_.EAttribute()
    var_10 = lambda *args, **kwargs: True
    var_12 = True
    var_14 = False
    var_15 = python_code_.ecoreDiff_ChangedEStructuralFeature()
    var_18 = True
    var_19 = python_code_.ecoreDiff_EStructuralFeature(
        changeable=var_14,
        volatile=(),
        transient=var_14,
        defaultValueLiteral=var_10,
        defaultValue=(),
        unsettable=var_18,
        derived=var_12,
        ecoreDiff_EStructuralFeature=var_6,
        ecoreDiff_EStructuralFeature219=var_15,
    )
    assert isinstance(var_19, python_code_.ecoreDiff_EStructuralFeature)


@pytest.mark.xfail(strict=True)
def test_9():
    var_0 = python_code_.ENamedElement()
    var_1 = python_code_.EPackage()
    var_4 = python_code_.ecoreDiff_DeletedEAnnotation()
    var_5 = python_code_.ecoreDiff_ChangedEDataType()
    var_7 = lambda *args, **kwargs: False
    python_code_.ecoreDiff_EStringToStringMapEntry(
        key=var_1, value=var_1, ecoreDiff_EStringToStringMapEntry119=var_7
    )
    var_12 = python_code_.ecoreDiff_DeletedEClassifier()
    var_17 = python_code_.ecoreDiff_EParameter()
    var_20 = python_code_.ecoreDiff_DeletedEClassifier_Wildcard()
    var_22 = "EPackage,EClassifier,ecoreDiff_ChangedEEnumLiteral"
    var_23 = python_code_.ecoreDiff_EClassifier(
        instanceClassName=var_22,
        instanceClass=var_22,
        defaultValue=var_22,
        instanceTypeName=var_7,
        ecoreDiff_EClassifier140=var_12,
    )
    assert isinstance(var_23, python_code_.ecoreDiff_EClassifier)
    var_24 = False
    var_25 = False
    var_26 = python_code_.ecoreDiff_ChangedEReference()
    var_27 = python_code_.ecoreDiff_EReference(
        containment=var_24,
        container=var_24,
        resolveProxies=var_25,
        ecoreDiff_EReference18=var_5,
        ecoreDiff_EReference100=(),
        ecoreDiff_EReference232=var_26,
    )
    assert isinstance(var_27, python_code_.ecoreDiff_EReference)
    var_30 = python_code_.ecoreDiff_EStructuralFeature(
        changeable=var_4,
        volatile=-270,
        transient=var_5,
        defaultValueLiteral=b"\x9fO+\x82\x9a\xbe%\x14bm\x97:4",
        defaultValue=var_0,
        unsettable=var_7,
        derived=var_25,
        EStructuralFeature=3,
    )
    assert isinstance(var_30, python_code_.ecoreDiff_EStructuralFeature)
    var_31 = python_code_.EFactory()
    var_33 = python_code_.ecoreDiff_DeletedEClassifier_Wildcard()
    var_35 = "}?>@$pE"
    var_36 = python_code_.ecoreDiff_EStructuralFeature(
        changeable=var_31,
        volatile=False,
        transient=False,
        defaultValueLiteral=var_7,
        defaultValue=var_35,
        unsettable=var_23,
        derived=var_7,
        ecoreDiff_EStructuralFeature=var_33,
        eStructuralFeatures=var_7,
    )
    var_38 = False
    var_40 = {var_30, var_36, var_36, var_36}
    python_code_.ecoreDiff_EClass(
        abstract=var_36,
        interface=var_17,
        eContainingClass=var_4,
        eContainingClass13=var_40,
        ecoreDiff_EClass15=var_31,
        ecoreDiff_EClass20=var_40,
        ecoreDiff_EClass23=var_7,
        ecoreDiff_EClass26=var_20,
        ecoreDiff_EClass29=var_38,
        ecoreDiff_EClass33=[],
        ecoreDiff_EClass101=var_27,
    )


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = False
    var_1 = python_code_.ecoreDiff_AddedETypedElement
    var_2 = python_code_.ecoreDiff_ChangedEClass()
    python_code_.ecoreDiff_EClass(
        abstract=var_0,
        interface=var_1,
        ecoreDiff_EClass={
            "_ecoreDiff_EStructuralFeature__eStructuralFeatures": 17.15,
            "4=?Zv/ lm(N\\^|Y": False,
        },
        ecoreDiff_EClass11=var_1,
        eContainingClass13=set(),
        ecoreDiff_EClass26=var_0,
        ecoreDiff_EClass133=var_2,
        EClass=var_1,
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_1 = True
    var_2 = True
    var_3 = python_code_.ecoreDiff_EOperation
    var_4 = set()
    python_code_.ecoreDiff_EClass(
        abstract={},
        interface=var_2,
        eContainingClass=var_3,
        ecoreDiff_EClass28=set(),
        ecoreDiff_EClass31=var_1,
        ecoreDiff_EClass29=var_4,
    )


@pytest.mark.xfail(strict=True)
def test_12():
    var_55 = True
    var_56 = False
    var_57 = python_code_.ecoreDiff_EOperation
    var_58 = set()
    var_59 = python_code_.ecoreDiff_EClass(
        abstract=var_55,
        interface=var_55,
        ecoreDiff_EClass7=set(),
        eContainingClass=var_58,
        ecoreDiff_EClass11=var_58,
        eContainingClass13={"<'a6", var_55, var_57},
        ecoreDiff_EClass15=var_58,
        ecoreDiff_EClass31=None,
        ecoreDiff_EClass33=None,
        ecoreDiff_EClass133=var_57,
        EClass=var_56,
    )
    assert isinstance(var_59, python_code_.ecoreDiff_EClass)
    python_code_.ecoreDiff_EClass(
        abstract=var_55,
        interface={"EI@": "|\x0bNSlAw~N"},
        ecoreDiff_EClass=var_59,
        ecoreDiff_EClass7=var_58,
        ecoreDiff_EClass26=var_57,
        ecoreDiff_EClass29=[3, True],
        ecoreDiff_EClass33=var_58,
    )


def test_13():
    var_0 = "\"F6\nOg\x0bd'1Dl~Nf"
    var_1 = python_code_.ecoreDiff_EClassifier(
        instanceClassName=var_0,
        instanceClass=True,
        defaultValue=var_0,
        instanceTypeName="",
        ecoreDiff_EClassifier64=b"\x7f\xb2\xf1\x0e",
        ecoreDiff_EClassifier140=var_0,
        ecoreDiff_EClassifier80=2686.43,
    )
    assert isinstance(var_1, python_code_.ecoreDiff_EClassifier)
    var_3 = "_ecoreDiff_EAttribute__ecoreDiff_EAttribute93.ecoreDiff_EGenericType89"
    var_4 = python_code_.ecoreDiff_EClassifier
    var_5 = python_code_.ecoreDiff_EAnnotation(source=var_0)
    assert isinstance(var_5, python_code_.ecoreDiff_EAnnotation)
    var_6 = python_code_.ecoreDiff_EStringToStringMapEntry(
        key=var_3, value=var_4, ecoreDiff_EStringToStringMapEntry=var_5
    )
    assert isinstance(var_6, python_code_.ecoreDiff_EStringToStringMapEntry)


def test_14():
    var_1 = python_code_.EPackage()
    var_7 = lambda *args, **kwargs: False
    python_code_.ecoreDiff_EStringToStringMapEntry(
        key=var_1, value=var_1, ecoreDiff_EStringToStringMapEntry119=var_7
    )


def test_15():
    var_4 = 'F>p/|YD%l2p?"3'
    var_5 = python_code_.ecoreDiff_ChangedENamedElement()
    var_6 = python_code_.ecoreDiff_ENamedElement(
        name=var_4, ecoreDiff_ENamedElement=var_5
    )
    assert isinstance(var_6, python_code_.ecoreDiff_ENamedElement)


def test_16():
    var_0 = "\"F6\nOg\x0bd'1Dl~Nf"
    var_1 = python_code_.ecoreDiff_EClassifier(
        instanceClassName=var_0,
        instanceClass=True,
        defaultValue=var_0,
        instanceTypeName="",
        ecoreDiff_EClassifier64=b"\x7f\xb2\xf1\x0e",
        ecoreDiff_EClassifier140=var_0,
        ecoreDiff_EClassifier80=2686.43,
    )
    assert isinstance(var_1, python_code_.ecoreDiff_EClassifier)
    var_5 = python_code_.ecoreDiff_EAnnotation(source=var_0)
    assert isinstance(var_5, python_code_.ecoreDiff_EAnnotation)


def test_17():
    python_code_.EFactory()


def test_18():
    var_3 = "_ecoreDiff_EAttribute__ecoreDiff_EAttribute93.ecoreDiff_EGenericType89"
    var_5 = python_code_.ecoreDiff_EAnnotation(
        source="ecoreDiff_EModelElement.EPackage._ecoreDiff_EClass__ecoreDiff_EClass26",
        ecoreDiff_EAnnotation5=set(),
        eAnnotations=var_3,
    )
    assert isinstance(var_5, python_code_.ecoreDiff_EAnnotation)


@pytest.mark.xfail(strict=True)
def test_19():
    var_7 = python_code_.ecoreDiff_AddedEClass()
    var_8 = python_code_.ecoreDiff_AddedETypeParameter()
    var_19 = python_code_.ecoreDiff_DifferenceModel
    var_20 = True
    var_23 = True
    var_24 = "]`"
    var_25 = python_code_.ecoreDiff_EStructuralFeature(
        changeable=var_20,
        volatile=var_23,
        transient={2928, True},
        defaultValueLiteral=var_19,
        defaultValue=var_24,
        unsettable=b"O\x0bW\xd6\xd1",
        derived=var_20,
        EStructuralFeature=var_7,
    )
    assert isinstance(var_25, python_code_.ecoreDiff_EStructuralFeature)
    var_26 = {var_25, var_25}
    var_30 = True
    python_code_.ecoreDiff_EClass(
        abstract=var_30,
        interface=var_7,
        ecoreDiff_EClass=var_8,
        ecoreDiff_EClass7=var_26,
        ecoreDiff_EClass15=var_26,
        ecoreDiff_EClass17=complex(887.4610077, -997.7356),
        ecoreDiff_EClass38=b"\x00Z))\x1f\xfd\x99\xe3\xa3\x12\xb9.\xf8\x85\xe4",
        EClass=None,
        EClass95=var_25,
    )


def test_20():
    var_3 = python_code_.ecoreDiff_EOperation
    var_7 = python_code_.ecoreDiff_EGenericType()
    var_8 = python_code_.ecoreDiff_EClassifier(
        instanceClassName=None,
        instanceClass=var_7,
        defaultValue=var_3,
        instanceTypeName=var_7,
    )
    assert isinstance(var_8, python_code_.ecoreDiff_EClassifier)
    var_11 = python_code_.ecoreDiff_EStructuralFeature_Wildcard()
    var_12 = python_code_.ecoreDiff_EEnum()
    var_15 = "_ecoreDiff_EClass__ecoreDiff_EClass20"
    var_16 = "_ecoreDiff_EPackage__EPackage,eStructuralFeatures,_ecoreDiff_EEnumLiteral__ecoreDiff_EEnumLiteral,ePackage50"
    var_17 = python_code_.ecoreDiff_EEnumLiteral(
        value=var_3,
        instance=var_15,
        literal=var_16,
        eLiterals=var_11,
        EEnumLiteral=var_12,
    )
    assert isinstance(var_17, python_code_.ecoreDiff_EEnumLiteral)


def test_21():
    var_58 = {True}
    var_65 = python_code_.ecoreDiff_EStructuralFeature_Wildcard()
    var_66 = python_code_.ecoreDiff_EEnum()
    var_68 = python_code_.ecoreDiff_AddedENamedElement()
    var_70 = "_ecoreDiff_EPackage__EPackage,eStructuralFeatures,_ecoreDiff_EEnumLiteral__ecoreDiff_EEnumLiteral,ePackage50"
    var_71 = python_code_.ecoreDiff_EEnumLiteral(
        value=1,
        instance="EPackage45:_ecoreDiff_EPackage__eSuperPackage:ecoreDiff_EClass",
        literal=var_70,
        EEnumLiteral=var_66,
    )
    assert isinstance(var_71, python_code_.ecoreDiff_EEnumLiteral)
    var_79 = python_code_.ecoreDiff_EPackage(
        nsURI=var_68,
        nsPrefix=var_70,
        ePackage=var_70,
        eSuperPackage=var_58,
        eSubpackages=False,
        ePackage50=var_58,
        ecoreDiff_EPackage=var_65,
    )
    assert isinstance(var_79, python_code_.ecoreDiff_EPackage)


@pytest.mark.xfail(strict=True)
def test_22():
    var_0 = python_code_.ENamedElement()
    var_55 = python_code_.ecoreDiff_AddedEClassifier_Wildcard()
    var_57 = python_code_.ecoreDiff_EClassifier
    var_58 = "L\x0camh"
    python_code_.ecoreDiff_EClassifier(
        instanceClassName=var_58,
        instanceClass=var_55,
        defaultValue=var_57,
        instanceTypeName=var_57,
        eClassifiers=var_57,
        ecoreDiff_EClassifier=var_0,
        ecoreDiff_EClassifier64="I2^$s 7)=YZQJs*,\t",
    )
